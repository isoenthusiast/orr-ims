# Concern, action and assurance register — schema

| Control field | Value |
|---|---|
| Document ID / type / revision | ORR-REG-GEN-001 / REG / r01 |
| Prepared / status | 2026-10-31 / Draft — not approved or effective |
| Scope / module / layer | Original public learning starter / Generic documentation demonstrations / Layer 1 |
| Owner / actual appointment | Adopting process owner / Unassigned |
| Author | Codex at Edward Wee's request; AI-assisted original project drafting |
| Reviewer / approver | Competent scoped reviewer / Adopting authority; both Unassigned |
| Approval / effective date | Not approved / Not effective |
| Basis | ORR-STD-DOC-001 r02; prepared under OIMS-STD-DOC-001 r05 |
| Classification / lifecycle | Public candidate draft / Maintained template/schema |
| Canonical / index | This file; distribution inventory ORR-REG-REL-001; working preparation index retained privately |
| Review trigger | Changed scope, source, authority, decision rule or user finding; before adoption |
| Retention / access | Public blank/example only; real records stay in authorized private storage; preserve until actual schedule and holds are decided |
| Supersedes / deviations | None / None; renamed headings preserve type-profile content |

## 1. Scope and custodian

Index scoped concern/action records and decisions; do not replace their evidence. Actual custodian: [appoint before adoption]. The public file is a schema, not an operational register. One concern may link multiple actions and controls; retain separate identifiers and outcomes.

## 2. Fields and entry rules

| Field | Definition / validation |
|---|---|
| concern_id / action_id / control_id | Stable unique IDs in their respective namespaces; link rather than reuse one ID for different objects |
| scope / objective / risk | Context and reason for the control/action; preserve changed scope |
| receiving_owner / decision_authority | Named actual role and delegated limit; unassigned blocks dependent decisions |
| status | new, assessing, decision_pending, implementing, outcome_pending, held, closed |
| next_action / due_trigger / escalation_owner | Required for every nonclosed item; use actual adopted deadlines |
| criterion / implementation_refs / outcome_refs | Separate agreed criterion and evidence sets; no unsupported closure |
| review_ref / decision_ref / acknowledgment_ref | Trace receiving review, authority and handoff |
| version / prior_entry / changed_by / changed_at / reason | Attributable append-only correction trail |
| access_class / retention_basis / hold | Actual configured record protections; unknown means preserve and resolve |

## 3. Update and status validation

Intake owner creates a scoped entry; assigned owner updates progress; reviewer records outcome conclusion; delegated authority records closure. A completed implementation moves to outcome_pending unless adequate reviewed outcome evidence already exists. held needs a gap owner and restoration criterion. closed needs current scope, criterion, sufficient reviewed evidence and authorized decision; related items do not close by implication. Changed or invalidated evidence triggers reassessment with earlier status retained.

## 4. Retrieval, access and retention

Retrieve by stable ID and current revision; expose history to authorized reviewers. Use actual private evidence storage, not public issue attachments. Configure access, recovery, retention and holds; no automatic deletion while basis is unknown. Exported reports identify snapshot date and limits rather than implying live completeness.

## 5. History

r01: original schema; permitted field-based REG profile. No operating records or actual effectiveness claimed.
