# Publication source and rights register

| Control field | Value |
|---|---|
| Document ID / type / revision | ORR-REG-REL-002 / REG / r02 |
| Prepared / status | 2026-10-31 / Draft — not approved or effective |
| Scope / module / layer | Exact public candidate selection / Release preparation / Layer 1 |
| Owner / actual appointment | Release controller / Unassigned |
| Author | Codex at Edward Wee's request; AI-assisted original project drafting |
| Reviewer / approver | Competent release reviewer / Product governance authority; both Unassigned |
| Approval / effective date | Not approved / Not effective |
| Basis | ORR-STD-DOC-001 r02; prepared under OIMS-STD-DOC-001 r05 |
| Classification / lifecycle | Public candidate draft / Maintained template/schema |
| Canonical / index | Paired publication JSON; this file is its guide; distribution inventory ORR-REG-REL-001; working preparation index retained privately |
| Review trigger | Changed scope, source, authority, decision rule or user finding; before adoption |
| Retention / access | Public blank/example only; real records stay in authorized private storage; preserve until actual schedule and holds are decided |
| Supersedes / deviations | r01 retained in private history / None; renamed headings preserve type-profile content |

## 1. Scope, custodian and identity

The paired JSON is the authoritative per-file source/rights/selection register
for this candidate. It is not a second document metadata master; ORR-REG-DOC-001
remains the private preparation index and ORR-REG-REL-001 is the generated exact
distribution snapshot. Proposed custodian: release controller; actual unassigned.

## 2. Fields and entry rules

Each unique repository-relative path records document ID/revision where applicable,
intended licence, origin, source references, rights basis, author-review disposition,
limitations and publication decision. Include only regular repository-contained
files; no symlinks, traversal or local review files. Bibliographic references are
not permission grants. Unmodified licence texts have their separate allocation.

| JSON field | Meaning and validation |
|---|---|
| document_id / revision / status / prepared_date | Register identity and draft configuration; paired guide shares the revision |
| custodian_role / actual_custodian / author / reviewer | Proposed authority and actual review extent; unassigned is not approval |
| publication_decision / source_rights_scope | Exact candidate decision state and assessment limits, not a rights grant |
| decision_record / accepted_risk_ids | Public decision narrative and scoped residual-risk IDs; acceptance does not close findings |
| sources | Referenced provenance identifiers, descriptions or URLs, checked date where recorded and limitations |
| files[].path | Unique repository-relative regular-file path; explicit selection only |
| files[].document_id / revision | Controlled identity/revision, or Not-controlled / Not-applicable |
| files[].licence | Explicit allocation consistent with LICENSING.md; not permission inferred from format |
| files[].origin / third_party_content | Actual drafting origin and identified included third-party material, with review limits |
| files[].source_refs / rights_basis | Existing source IDs and asserted authority; a nonempty value is not proof of legal sufficiency |
| files[].author_review / limitations | Author-review disposition and unresolved limitations; never independent clearance by implication |
| files[].publication_decision | Must match the register's current decision state |

Canonical data: [publication register](ORR-REG-REL-002_PUBLICATION-REGISTER.json).
Current state is `Authorized draft publication; unresolved risks retained`. A future release-state change
requires an attributable decision and corresponding controlled revision, including
updates to the checker's accepted state. Code cannot confer publication authority.

The owner-confirmed original-contribution authority is a provenance input, not an
independent ownership opinion. Initial rows are author-reviewed within the stated
scope; competent legal/name/source-processing questions remain unresolved.
Candidate selection does not mean published or independently accepted.

## 3. Update and validation

Assess sources and permission needs before adding a path. Record actual third-party
content or explicitly none identified within author scope. If permission is needed,
retain its exact scope and evidence privately and publish only an appropriate
reference; do not declare it obtained without evidence. Private or restricted
content is not an eligible default. Unknown rights need scoped resolution or
exclusion, not an inferred licence. Revalidate changed dependencies and preserve
prior versions before material revisions. The checker rejects undeclared paths,
missing review decisions, unsafe paths and inconsistent metadata/licences.

## 4. Retrieval, release and retention

Generate inventory only after completing author review and registering identities.
Verify exact hashes, source/rights disposition, draft claims and findings; obtain
the exact maintainer release decision. Do not mirror private repository history.
Keep sensitive contracts and review evidence private. Preserve this schema and
decision history; retention and disposal authority remain unassigned.

## 5. History and limits

r01, 2026-10-31: initial explicit publication selection and provenance register.
No third-party licence, legal opinion, independent assurance or publication of this
new candidate is implied. JSON source references are factual provenance, not a
statement that linked sources were copied into the release.

## r02 — maintainer draft publication decision

2026-10-31: Edward Wee accepted the recommendation and instructed publication of
this reviewed learning draft with its stated unresolved limitations. This is a
scoped distribution decision, not full compliance-audit acceptance or a grant of
third-party rights. Prior r01 bytes and findings remain retained privately.
See [governance](../../GOVERNANCE.md) for the current decision.
