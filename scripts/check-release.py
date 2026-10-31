#!/usr/bin/env python3
"""Check a bounded documentation candidate. Passing does not authorize release."""
# SPDX-License-Identifier: Apache-2.0
# Copyright 2026 Edward Wee, to the extent copyright subsists.
import argparse
import csv
import hashlib
import io
import json
from pathlib import Path, PurePosixPath
import re
import subprocess
import sys
from urllib.parse import unquote, urlsplit

ROOT = Path(__file__).resolve().parents[1]
INVENTORY = 'docs/governance/ORR-REG-REL-001_RELEASE-INVENTORY.csv'
PUBLICATION = 'docs/governance/ORR-REG-REL-002_PUBLICATION-REGISTER.json'
FIELDS = ['path', 'document_id', 'revision', 'status', 'licence', 'source_basis', 'sha256']

def safe_path(name):
    if not isinstance(name, str) or not name or '\\' in name:
        return False
    path = PurePosixPath(name)
    if path.is_absolute() or str(path) != name or '..' in path.parts:
        return False
    if any(part.startswith('.') for part in path.parts) and name != '.gitignore':
        return False
    if path.parts[0] == 'sources' or path.name == 'AGENTS.md':
        return False
    full = ROOT / name
    return (ROOT in full.resolve().parents
            and not any(p.is_symlink() for p in (full, *full.parents) if p != ROOT))

def reviewed_selection():
    """Fail closed: Git discovery detects extras; it never grants selection/rights."""
    if not safe_path(PUBLICATION):
        raise ValueError('Unsafe publication register path')
    data = json.loads((ROOT / PUBLICATION).read_text(encoding='utf-8'))
    if data.get('document_id') != 'ORR-REG-REL-002' or data.get('revision') != 'r02':
        raise ValueError('Publication register identity/revision mismatch')
    if data.get('status') != 'Draft' or data.get('publication_decision') != 'Authorized draft publication; unresolved risks retained':
        raise ValueError('Unexpected publication decision; revise checker with release governance')
    sources = data.get('sources', {})
    rows = data.get('files')
    if not isinstance(rows, list) or not rows:
        raise ValueError('Missing explicit file selection')
    entries, revisions = {}, {}
    for row in rows:
        if not isinstance(row, dict):
            raise ValueError('Invalid publication row')
        name = row.get('path')
        if not safe_path(name) or name in entries:
            raise ValueError(f'Unsafe or duplicate selection: {name}')
        required = ('document_id', 'revision', 'licence', 'origin', 'rights_basis',
                    'author_review', 'limitations', 'publication_decision', 'third_party_content')
        if any(not isinstance(row.get(k), str) or not row[k].strip() for k in required):
            raise ValueError(f'Missing source/rights/review fields: {name}')
        if row['author_review'] != 'Author-reviewed within stated limits':
            raise ValueError(f'Unreviewed selection: {name}')
        if row['publication_decision'] != data['publication_decision']:
            raise ValueError(f'Inconsistent publication decision: {name}')
        refs = row.get('source_refs')
        if not isinstance(refs, list) or not refs or any(not isinstance(r, str) or r not in sources for r in refs):
            raise ValueError(f'Unresolved source references: {name}')
        licence = row['licence']
        if licence not in {'CC-BY-4.0', 'Apache-2.0', 'Licence-text'}:
            raise ValueError(f'Unsupported licence: {name}')
        # Enforce the documented allocation, but do not infer rights from it.
        expected = ('Licence-text' if name.startswith('LICENSES/') else
                    'Apache-2.0' if name.endswith('.py') or name == '.gitignore'
                    or (name.startswith('brand/') and not name.endswith('.md')) else 'CC-BY-4.0')
        if licence != expected:
            raise ValueError(f'Licence conflicts with LICENSING.md: {name}')
        match = re.match(r'(ORR-[A-Z]+-[A-Z]+-\d+)_', PurePosixPath(name).name)
        identity = match.group(1) if match else 'Not-controlled'
        if row['document_id'] != identity:
            raise ValueError(f'Publication identity mismatch: {name}')
        revision = row['revision']
        if match:
            if not re.fullmatch(r'r\d{2}', revision) or revisions.get(identity, revision) != revision:
                raise ValueError(f'Conflicting/invalid revision: {name}')
            revisions[identity] = revision
        elif revision != 'Not-applicable':
            raise ValueError(f'Unexpected uncontrolled revision: {name}')
        if not (ROOT / name).is_file() and name != INVENTORY:
            raise ValueError(f'Missing selected file: {name}')
        entries[name] = row
    observed = set(subprocess.check_output(
        ['git', 'ls-files', '--cached', '--others', '--exclude-standard'],
        cwd=ROOT, text=True).splitlines())
    if observed - entries.keys():
        raise ValueError('Unregistered files: ' + ', '.join(sorted(observed - entries.keys())))
    if not {INVENTORY, PUBLICATION} <= entries.keys():
        raise ValueError('Selection must include both publication register and generated inventory')
    return entries, revisions

def expected_inventory(entries):
    out = io.StringIO(newline='')
    writer = csv.DictWriter(out, fieldnames=FIELDS, lineterminator='\n')
    writer.writeheader()
    for name, entry in sorted(entries.items()):
        p = ROOT / name
        match = re.match(r'(ORR-[A-Z]+-[A-Z]+-\d+)_', p.name)
        identity = match.group(1) if match else 'Not-controlled'
        licence, source = entry['licence'], entry['origin']
        writer.writerow(dict(path=name, document_id=identity,
            revision=entry['revision'],
            status='Draft' if match else 'Licence-text' if licence == 'Licence-text' else 'Candidate',
            licence=licence, source_basis=source,
            sha256='SELF' if name == INVENTORY else hashlib.sha256(p.read_bytes()).hexdigest()))
    return out.getvalue()

def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--write-inventory', action='store_true')
    args = parser.parse_args()
    entries, revisions = reviewed_selection()
    names = sorted(entries)
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
    if data['revision'] != revisions[data['document_id']]: errors.append('Fixture revision mismatch')
    for name in names:
        p=ROOT/name
        match=re.match(r'(ORR-[A-Z]+-[A-Z]+-\d+)_',p.name)
        if match and p.suffix=='.md':
            text=p.read_text(); identity=match.group(1)
            if not re.search(re.escape(identity)+r'\s*/\s*[A-Z]+\s*/\s*'+revisions[identity]+r'\s*\|',text):
                errors.append(f'Metadata identity/revision mismatch: {name}')
    expected = expected_inventory(entries)
    if errors:
        print(json.dumps({'result':'FAIL','findings':errors},indent=2));return 1
    if args.write_inventory:
        (ROOT/INVENTORY).write_text(expected)
    elif not (ROOT/INVENTORY).exists() or (ROOT/INVENTORY).read_text()!=expected:
        print(json.dumps({'result':'FAIL','findings':['Inventory missing or stale; regenerate after reviewed changes']}));return 1
    print(json.dumps({'result':'PASS','files':len(names),'controlled_identities':len(revisions),
        'fixture_records':len(ids),'limits':'Author technical checks only; no source-rights, trademark, legal, independent audit or release approval.'},indent=2))
    return 0

if __name__=='__main__':
    try:
        sys.exit(main())
    except (OSError, ValueError, KeyError, TypeError, subprocess.CalledProcessError) as exc:
        print(json.dumps({'result': 'FAIL', 'findings': [str(exc)]}, indent=2))
        sys.exit(1)
