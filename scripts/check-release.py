#!/usr/bin/env python3
"""Check a bounded documentation candidate. Passing does not authorize release."""
# SPDX-License-Identifier: Apache-2.0
# Copyright 2026 Edward Wee, to the extent copyright subsists.
import argparse
import csv
import hashlib
import io
import json
from pathlib import Path
import re
import subprocess
import sys
from urllib.parse import unquote, urlsplit

ROOT = Path(__file__).resolve().parents[1]
INVENTORY = 'docs/governance/ORR-REG-REL-001_RELEASE-INVENTORY.csv'
REVISIONS = {'ORR-STD-BRD-001': 'r03', 'ORR-FWK-REP-001': 'r03',
             'ORR-SOP-IMP-001': 'r03', 'ORR-FRM-IMP-001': 'r03',
             'ORR-PLN-IMP-001': 'r03', 'ORR-STD-DOC-001': 'r02',
             'ORR-REG-REL-001': 'r02'}
FIELDS = ['path', 'document_id', 'revision', 'status', 'licence', 'source_basis', 'sha256']

def candidate_paths():
    names = subprocess.check_output(
        ['git', 'ls-files', '--cached', '--others', '--exclude-standard'],
        cwd=ROOT, text=True).splitlines()
    return sorted(set(names + [INVENTORY]))

def allocation(name):
    if name.startswith('LICENSES/'):
        return 'Licence-text', 'Unmodified publisher licence text'
    if name.startswith('brand/') and not name.endswith('.md'):
        return 'Apache-2.0', 'Original AI-assisted project asset/code'
    if name.endswith('.py') or name == '.gitignore':
        return 'Apache-2.0', 'Original AI-assisted project code/configuration'
    return 'CC-BY-4.0', 'Original AI-assisted project documentation/data; source review separate'

def expected_inventory(names):
    out = io.StringIO(newline='')
    writer = csv.DictWriter(out, fieldnames=FIELDS, lineterminator='\n')
    writer.writeheader()
    for name in names:
        p = ROOT / name
        match = re.match(r'(ORR-[A-Z]+-[A-Z]+-\d+)_', p.name)
        identity = match.group(1) if match else 'Not-controlled'
        if match and identity not in REVISIONS:
            raise ValueError(f'Unregistered controlled identity: {identity}')
        licence, source = allocation(name)
        writer.writerow(dict(path=name, document_id=identity,
            revision=REVISIONS.get(identity, 'Not-applicable'),
            status='Draft' if match else 'Licence-text' if licence == 'Licence-text' else 'Candidate',
            licence=licence, source_basis=source,
            sha256='SELF' if name == INVENTORY else hashlib.sha256(p.read_bytes()).hexdigest()))
    return out.getvalue()

def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--write-inventory', action='store_true')
    args = parser.parse_args()
    names = candidate_paths()
    errors = []
    patterns = {
        'private host path': r'/(?:home/edward|srv/orrery)/',
        'credential pattern': r'(?:gh[pousr]_[A-Za-z0-9]{20,}|sk-[A-Za-z0-9]{24,}|-----BEGIN (?:RSA |EC |OPENSSH )?PRIVATE KEY-----)',
    }
    allowed_suffixes = {'.md', '.json', '.csv', '.css', '.html', '.py', '.txt'}
    for name in names:
        p = ROOT / name
        if name == INVENTORY and not p.exists():
            continue
        if p.is_symlink() or not p.is_file() or ROOT not in p.resolve().parents:
            errors.append(f'Unsafe/non-file path: {name}'); continue
        if name.startswith(('.local/', '.codex', 'sources/')) or p.name == 'AGENTS.md':
            errors.append(f'Private path selected: {name}')
        if p.suffix not in allowed_suffixes and name != '.gitignore':
            errors.append(f'Unexpected format: {name}')
        text = p.read_text(encoding='utf-8')
        for label, pattern in patterns.items():
            if re.search(pattern, text): errors.append(f'{label}: {name}')
        if p.suffix == '.md':
            for link in re.findall(r'\]\(([^)]+)\)', text):
                target = urlsplit(link.strip('<>'))
                if target.scheme or not target.path: continue
                dest = (p.parent / unquote(target.path)).resolve()
                if ROOT not in dest.parents or not dest.is_file():
                    # The inventory may be created in this invocation.
                    if str(dest) != str(ROOT / INVENTORY):
                        errors.append(f'Broken/outside link: {name}: {link}')
                elif str(dest.relative_to(ROOT)) not in names:
                    errors.append(f'Link outside selected files: {name}: {link}')
        if p.suffix == '.html':
            for link in re.findall(r'(?:src|href)=["\x27]([^"\x27]+)', text):
                target = urlsplit(link)
                if target.scheme or not target.path: continue
                if not (p.parent / unquote(target.path)).is_file():
                    errors.append(f'Broken HTML link: {name}: {link}')
            if re.search(r'<(?:script|iframe)[^>]+src=["\x27]https?://',text):
                errors.append(f'External executable content: {name}')
        if p.suffix == '.json': json.loads(text)
        if p.suffix == '.py': compile(text, name, 'exec')
    data = json.loads((ROOT/'docs/ORR-FWK-REP-001_FICTIONAL-DATA.json').read_text())
    ids = {r['id'] for r in data['records']}
    if len(ids) != len(data['records']) or data['evidence_items']:
        errors.append('Fixture IDs duplicated or actual evidence added')
    for record in data['records']:
        if record.get('origin') != 'fictional' or record.get('scope_id') != 'scope-demo':
            errors.append('Fixture origin/scope mismatch')
        for key, val in record.items():
            if key.endswith('_id') and val is not None and key not in ('scope_id','process_id') and val not in ids:
                errors.append(f'Unresolved fixture link: {record["id"]}.{key}')
    if data['revision'] != REVISIONS[data['document_id']]: errors.append('Fixture revision mismatch')
    for name in names:
        p=ROOT/name
        match=re.match(r'(ORR-[A-Z]+-[A-Z]+-\d+)_',p.name)
        if match and p.suffix=='.md':
            text=p.read_text(); identity=match.group(1)
            if not re.search(re.escape(identity)+r'\s*/\s*[A-Z]+\s*/\s*'+REVISIONS[identity],text):
                errors.append(f'Metadata identity/revision mismatch: {name}')
    expected = expected_inventory(names)
    if errors:
        print(json.dumps({'result':'FAIL','findings':errors},indent=2));return 1
    if args.write_inventory:
        (ROOT/INVENTORY).write_text(expected)
    elif not (ROOT/INVENTORY).exists() or (ROOT/INVENTORY).read_text()!=expected:
        print(json.dumps({'result':'FAIL','findings':['Inventory missing or stale; regenerate after reviewed changes']}));return 1
    print(json.dumps({'result':'PASS','files':len(names),'controlled_identities':len(REVISIONS),
        'fixture_records':len(ids),'limits':'Author technical checks only; no source-rights, trademark, legal, independent audit or release approval.'},indent=2))
    return 0

if __name__=='__main__':
    sys.exit(main())
