"""Regression tests for fail-closed candidate selection; no publication occurs."""
# SPDX-License-Identifier: Apache-2.0
# Copyright 2026 Edward Wee, to the extent copyright subsists.
import json
from pathlib import Path
import shutil
import subprocess
import sys
import tempfile
import unittest

ROOT = Path(__file__).resolve().parents[1]
REGISTER = 'docs/governance/ORR-REG-REL-002_PUBLICATION-REGISTER.json'
INVENTORY = 'docs/governance/ORR-REG-REL-001_RELEASE-INVENTORY.csv'


class ReleaseSelectionTests(unittest.TestCase):
    def setUp(self):
        self.tmp = tempfile.TemporaryDirectory()
        self.addCleanup(self.tmp.cleanup)
        self.root = Path(self.tmp.name)
        self.data = json.loads((ROOT / REGISTER).read_text())
        for row in self.data['files']:
            source = ROOT / row['path']
            dest = self.root / row['path']
            dest.parent.mkdir(parents=True, exist_ok=True)
            shutil.copyfile(source, dest)
        subprocess.run(['git', 'init', '-q', str(self.root)], check=True)

    def save_register(self):
        (self.root / REGISTER).write_text(json.dumps(self.data, indent=2) + '\n')

    def check(self, expected, fragment=None, write=True):
        command = [sys.executable, str(self.root / 'scripts/check-release.py')]
        if write:
            command.append('--write-inventory')
        result = subprocess.run(command, cwd=self.root, text=True, capture_output=True)
        self.assertEqual(result.returncode, expected, result.stdout + result.stderr)
        output = json.loads(result.stdout)
        self.assertEqual(output['result'], 'PASS' if expected == 0 else 'FAIL')
        if fragment:
            self.assertIn(fragment, result.stdout)

    def test_selected_candidate_and_regenerated_inventory(self):
        self.check(0)
        self.check(0, write=False)

    def test_unregistered_file_is_rejected_without_inventory_write(self):
        original = (self.root / INVENTORY).read_bytes()
        (self.root / 'unreviewed.md').write_text('Unreviewed document')
        self.check(1, 'Unregistered files')
        self.assertEqual((self.root / INVENTORY).read_bytes(), original)

    def test_missing_rights_basis(self):
        del self.data['files'][0]['rights_basis']
        self.save_register()
        self.check(1, 'Missing source/rights/review fields')

    def test_unknown_source_reference(self):
        self.data['files'][0]['source_refs'] = ['unknown']
        self.save_register()
        self.check(1, 'Unresolved source references')

    def test_unreviewed_entry(self):
        self.data['files'][0]['author_review'] = 'Pending'
        self.save_register()
        self.check(1, 'Unreviewed selection')

    def test_duplicate_path(self):
        self.data['files'].append(self.data['files'][0].copy())
        self.save_register()
        self.check(1, 'Unsafe or duplicate')

    def test_path_traversal(self):
        self.data['files'][0]['path'] = '../outside.md'
        self.save_register()
        self.check(1, 'Unsafe or duplicate')

    def test_symlink(self):
        target = self.root / 'README.md'
        target.unlink()
        target.symlink_to(self.root / 'NOTICE.md')
        self.check(1, 'Unsafe or duplicate')

    def test_licence_conflicts_with_allocation(self):
        row = next(r for r in self.data['files'] if r['path'] == 'README.md')
        row['licence'] = 'Apache-2.0'
        self.save_register()
        self.check(1, 'Licence conflicts')

    def test_missing_file(self):
        (self.root / 'NOTICE.md').unlink()
        self.check(1, 'Missing selected file')

    def test_metadata_revision_mismatch(self):
        path = self.root / 'docs/templates/ORR-POL-GEN-001_EVIDENCE-POLICY.md'
        path.write_text(path.read_text().replace('/ POL / r01', '/ POL / r99'))
        self.check(1, 'Metadata identity/revision mismatch')

    def test_fictional_fixture_cannot_become_actual(self):
        path = self.root / 'docs/ORR-FWK-REP-001_FICTIONAL-DATA.json'
        data = json.loads(path.read_text())
        data['records'][0]['origin'] = 'actual'
        path.write_text(json.dumps(data))
        self.check(1, 'Fixture origin/scope mismatch')

    def test_private_host_path(self):
        path = self.root / 'README.md'
        path.write_text(path.read_text() + '\n' + '/home/' + 'edward/private.txt\n')
        self.check(1, 'private host path')

    def test_broken_local_link(self):
        path = self.root / 'README.md'
        path.write_text(path.read_text() + '\n[missing](absent.md)\n')
        self.check(1, 'Broken/outside link')

    def test_stale_inventory(self):
        self.check(0)
        path = self.root / 'README.md'
        path.write_text(path.read_text() + '\nChanged after snapshot.\n')
        self.check(1, 'Inventory missing or stale', write=False)

    def test_register_cannot_self_approve_publication(self):
        self.data['publication_decision'] = 'Approved'
        self.save_register()
        self.check(1, 'Unexpected publication decision')


if __name__ == '__main__':
    unittest.main()
