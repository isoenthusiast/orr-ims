# Candidate distribution inventory

| Control field | Value |
|---|---|
| Document ID / type / revision | ORR-REG-REL-001 / REG / r02 |
| Status / prepared | Draft; not approved or effective / 2026-10-30 |
| Scope / module / layer | Exact candidate files, not private working records / Release preparation, design-r01 / Layer 1 |
| Custodian / author | Release controller, Unassigned / Codex at Edward Wee's request |
| Reviewer / approver | Competent release reviewer, Unassigned / Product governance authority, Unassigned |
| Classification / lifecycle | Public draft; organizational approval pending / Maintained schema; generated snapshot |
| Basis | ORR-STD-DOC-001 r02; prepared under OIMS-STD-DOC-001 r05 |
| Review trigger / supersedes / deviations | Any selected file, rights or status change / None / None |

## Scope and authority

Canonical distribution data is
[ORR-REG-REL-001_RELEASE-INVENTORY.csv](ORR-REG-REL-001_RELEASE-INVENTORY.csv).
It is a generated snapshot, not a second authoring master or evidence of organizational approval.
The private preparation register is the authoring master; private findings,
historical snapshots and source records are intentionally excluded.

## Fields and rules

| Field | Meaning / validation |
|---|---|
| path | Unique repository-relative file path; no traversal, symlink or private storage |
| document_id | Controlled identity where applicable; Not-controlled for ordinary repository/code/licence metadata |
| revision | Controlled revision; Not-applicable for unversioned navigation/code outside a controlled family |
| status | Draft for controlled content; Candidate for navigation/code; Licence-text for exact third-party licence text |
| licence | CC-BY-4.0, Apache-2.0 or Licence-text; see LICENSING.md for exclusions |
| source_basis | Origin category, not legal clearance; source-specific findings may still block release |
| sha256 | Exact bytes; SELF for this CSV only to avoid self-referential hashing |

The release envelope retained with the audit hashes every file, including this
CSV. That envelope resolves the self-hash exception. It proves file identity,
not truth, ownership or suitability. The fixed snapshot revision is r02; any
later assessed revision requires a preserved predecessor and updated revision.

## Updating, access and retention

Generate with `python3 scripts/check-release.py --write-inventory`, then verify
with `python3 scripts/check-release.py`. Do not edit CSV rows manually. Adding a
controlled identity requires the maintainer to register its master, owner,
review state and source basis before updating this view. Reconcile every path,
identity and revision; unsupported formats or unknown identities fail the check.

Readers may retrieve the CSV alongside its exact candidate. A future maintainer
must preserve release manifests and attributable corrections, establish actual
access/backup and retention arrangements, and retain material under hold. Until
those arrangements are set, preserve and do not dispose automatically. Any
changed candidate requires renewed affected review; a successful command does
not authorize publication or organizational use.

## Verification and history

REG profile: scope/custodian above; dictionary and entry/status rules §Fields;
updates, access and retention §Updating. Author checks retained locally;
competent review and approval pending. r01, 2026-10-30: initial generated
distribution view; no deviations.

## Draft publication decision — r02

2026-10-30: Edward Wee authorized public draft distribution with recorded
unresolved risks accepted, superseding the earlier publication hold for this
selection. This decision does not close those findings, grant third-party rights
or approve organizational use. See [GOVERNANCE.md](../../GOVERNANCE.md).
Earlier preparation/release-pending statements describe the retained drafting
context; this decision controls public distribution only. Previous r01 bytes
are retained in private history. Operational status remains Draft, not effective.
