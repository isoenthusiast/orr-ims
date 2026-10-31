# Control documents and records worksheet

| Control field | Value |
|---|---|
| Document ID / type / revision | ORR-FRM-DOC-001 / FRM / r01 |
| Status / prepared | Draft; not approved or effective / 2026-11-01 |
| Scope / module / layer | Beginner implementation learning kit / IMS implementation, design-r01 unreleased / Layer 1 reusable design; fictional Layer 2–4 applications explicitly labelled |
| Owner / actual appointment | Document controller / Unassigned |
| Author | Codex at Edward Wee's request; original AI-assisted drafting |
| Reviewer / approver | Competent IMS and relevant discipline reviewer / Authorized adopting management; both Unassigned |
| Approval / effective date | Not approved / Not effective |
| Classification / lifecycle | Candidate public learning draft; no real operational data / Maintained template |
| Basis | ORR-STD-DOC-001 r02; OIMS-STD-DOC-001 r05 private authoring basis |
| Canonical / index | This Markdown file; public candidate inventory ORR-REG-REL-001; private authoring index ORR-REG-DOC-001 |
| Review trigger | Before adoption/publication; changed scope, obligation, workflow, evidence or user finding |
| Access / retention | Public blank or fictional example only; adopted records in authorized private storage. Preserve pending retention schedule and holds; no automatic deletion |
| Supersedes / deviations | None / None; combined headings retain type-profile content |

## Purpose and instructions

Use with [the procedure](ORR-SOP-DOC-001_CONTROL-DOCUMENTS-AND-RECORDS.md) for P08. Copy this blank worksheet
into the organization's private record store and assign an event/record ID.
For multiple risks, controls, parties, decisions or results, repeat the relevant
field group or use linked child records; never compress distinct decisions into
one untestable statement. This form is not a completed record or approval.

M = mandatory; C = conditional when the event described occurs; O = optional.
For a mandatory unknown enter **Unknown — owner — due date — action ID** and
hold the affected decision. For a conditional item not triggered enter **N/A —
reason**; blank is not N/A. Optional supporting notes may be omitted. All dates
use YYYY-MM-DD; event times include a time zone. Evidence references identify
the retained file/version or immutable event, not a mutable homepage alone.

## Context and data fields

| Field | Required | Meaning / validation | Value |
|---|---|---|---|
| record_id | M | Unique execution ID, separate from this blank template ID | [enter] |
| origin | M | ORR-FRM-DOC-001 r01; adopted configuration/version and governing procedure | [enter] |
| actor_time | M | Creator role/name; event date/time zone; recorded date if different | [enter] |
| document_id_title_type | M | Stable document ID, meaningful title and type | [enter] |
| revision_scope_status | M | Revision, sites/roles/processes; Draft / In review / Approved / Effective / Superseded / Withdrawn | [enter] |
| owner_author | M | Owner, author and actual appointments | [enter] |
| change_and_dependencies | M | Reason, predecessor location/hash and affected forms/training/systems | [enter] |
| source_basis | M | Internal rules and exact external source/edition when applicable; rights/access limits | [enter] |
| review | M | Reviewer, competence, exact revision/hash, findings and disposition; Pending until complete | [enter] |
| approval | M | Delegated authority, exact decision/content/date; Not approved until evidenced | [enter] |
| release_effective | M | Distribution, all affected users/shifts, briefing/access checks and effective date; Not effective until conditions met | [enter] |
| canonical_access_retention | M | Authoritative location, access roles, custodian, retention basis/hold, backup/recovery checks | [enter] |
| correction_supersession | C | Original/new entry, actor/date/reason and supersession/disposal authority where applicable | [enter] |
| supporting_notes | O | Additional explanation; distinguish facts and assumptions | [enter] |

## Review, decision and filing

Before submission the preparer checks required fields, linked IDs, evidence access
and any pending decisions. Reviewer records name/role, date, exact record version,
Pass/Fail/Pending/N/A with reason, findings and disposition. Decision-maker records
authority, decision, conditions and date; no signature or blank field implies approval.
These fields must be completed in the adopted private record:

| Field | Required | Value |
|---|---|---|
| preparer_check_and_date | M | [enter] |
| reviewer_findings_and_date | M | Pending until reviewed |
| authorized_decision_and_date | M | Pending until decided |
| custodian_index_and_location | M | [enter private operational index / location] |
| correction_history | C | [prior value, new value, actor, date, reason; otherwise N/A — initial entry] |

Custodian: Document controller, actual unassigned until adoption. Maintain an index with
record ID, process, event date, owner, state, canonical location, parent/child IDs
and current version. Never reuse IDs. Protect access by role; prohibit public
posting of real operational records. Preserve history and holds; determine retention
from applicable obligations before disposal. Correct with an attributable amendment,
not silent overwrite. Duplicate IDs and unsupported closed/effective states are
invalid. Reject incomplete submissions back to the owner, preserving the intake.

The editable spreadsheet is a manual capture aid, not an enforcement system.
Its Instructions sheet is part of the form; no formula or signature proves approval.

## Sources, tailoring and history

Original ORR learning design, based on the user-requested ORCA chain and practical
implementation needs. A purchased commercial pack was reviewed privately for
coverage and usability lessons before drafting; this is not a clean-room claim.
No vendor procedure, diagram, spreadsheet, clause text or completed record is
included. Source provenance and limits are recorded in ORR-REG-REL-002. Existing
ORCA attribution remains in the repository SOURCES.md. These are proposed internal
methods, not verified interpretations of ISO requirements or a certification checklist.

Adopters may change layout, terminology, software and proportional detail. Keep
traceable identity, accountable decisions, applicable obligations, evidence,
failure routes and approval boundaries. Unknown is not not-applicable. A mandatory
departure requires a recorded decision within legitimate authority; internal
acceptance cannot waive external duties. Use the linked document-control procedure.

r01 — 2026-11-01: initial original beginner-kit draft. Actual appointments,
competent review, representative user trial, approval and effectiveness pending.
Fictional decisions never authorize real work. Editable renditions, where supplied,
share this identity/revision; this Markdown is the master. Record a new derivative
identity/configuration when adapting, and reconcile changes before release.
