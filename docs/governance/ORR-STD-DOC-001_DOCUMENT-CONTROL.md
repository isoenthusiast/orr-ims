# ORR IMS public-edition document control

| Control field | Value |
|---|---|
| Document ID / type / revision | ORR-STD-DOC-001 / STD / r02 |
| Status / prepared | Draft; not approved or effective / 2026-10-30 |
| Scope / module / layer | Public-edition documentation / Documentation governance, design-r01 / Layer 1 |
| Owner / author | Documentation steward, Unassigned / Codex at Edward Wee's request |
| Reviewer / approver | Competent document-control reviewer, Unassigned / Product governance authority, Unassigned |
| Classification / lifecycle | Public draft; organizational approval pending / Maintained |
| Review trigger | Before adoption or publication; change to type, source, workflow or release boundary |
| Canonical location | This file; candidate inventory ORR-REG-REL-001 |
| Governing authoring basis | OIMS-STD-DOC-001 r05; private predecessor design basis, not included |
| Supersedes / deviations | r01 retained in private publication snapshot / No content deviations; owner publication decision recorded below |

## 1. Purpose and scope

Provide a self-contained set of proposed internal documentation rules for this
edition. These rules are project design choices, not quotations or interpretations
of ISO requirements. They apply to this standard itself and the controlled
documents listed in the candidate inventory. Publishing a draft for comment is
separate from approving it as an organization's effective working instruction.

Organizations adopting templates must create their own scoped configuration,
assign competent people, check applicable obligations and authorize actual use.
This document does not rename ORCA, the four fundamentals, ten elements, twelve
planned internal standards, four deployment layers or P01–P23 design identities.
Their detailed public specifications are not supplied by this control document.

## 2. Roles and authority

The document owner maintains the technical content and applicability. The author
prepares the draft and identifies missing inputs. The reviewer checks scope,
sources, interfaces and usability. The approver records a decision on the exact
version within delegated authority. The controller maintains the current index,
distribution and supersession trail. The record custodian protects evidence and
manages authorized retention. Users report ambiguity and select the revision
authorized for their scope. Record actual appointments separately from role names.

Roles may be combined with a recorded rationale where appropriate, but an author
check must not be called independent review. Vacancies remain explicit and block
effective organizational use. Project attribution is not a reviewer appointment.

## 3. Required controls

“Must” below describes proposed internal requirements upon adoption. These are
not external legal requirements or evidence that a draft is already effective.

| Rule | Requirement |
|---|---|
| PDC-01 Identity | Assign a stable unique ID, title, type, revision and status. Controlled filenames begin with the exact ID and underscore. Renditions share the identity and revision of their master. |
| PDC-02 Context | Identify scope, module/layer, classification, lifecycle, owner and actual appointment state, author, reviewer, approver, preparation date, approval/effectiveness state and review trigger. Identify the canonical file, control basis, sources, predecessor and any deviation. |
| PDC-03 Content | Apply the type profile in §4. Instructions identify inputs, responsible roles, decisions, limits, required evidence and what happens if an input or check fails. |
| PDC-04 Traceability | Distinguish externally sourced requirements, project rules, proposals and fictional examples. Link each claimed requirement to its receiving content and evidence, or record a gap. Cite exact source editions where applicable; a citation alone does not prove coverage. |
| PDC-05 Version and approval | Preserve assessed versions before revision; change the revision when assessed content changes. Keep preparation, review, approval, publication and effectiveness distinct. Pin decisions to exact revisions or hashes and their scope. |
| PDC-06 Tailoring | Adapt layout and wording while preserving required content, evidence, authority and applicable obligations. Record a content map when reorganizing sections. Unknown is not not-applicable; exclusions require reasons. |
| PDC-07 Records | Preserve event identity, scope, actor, time, originating configuration and evidence links. Record corrections with prior value, actor, date and reason. A maintained blank form is distinct from its completed record. |
| PDC-08 Protection | Define access, authoritative storage, retrieval, backup/recovery, retention, holds and disposal authority to suit the information. Until retention is decided, preserve without automatic deletion. A Git ignore rule alone does not secure records. |
| PDC-09 Index | Keep one authoritative working index for the controlled set. Release inventories are generated snapshots, not competing editable masters. Individual execution records use a named private operational index and custodian. |
| PDC-10 Verification | Perform §6 checks, record their exact scope and limits, and resolve material findings before the corresponding decision. No pass is inferred from an empty field or an automated scan alone. |

## 4. Document type profiles

Start with the control block. Include sources and change history. Use field-based
layouts for forms/registers; equivalent headings and combined sections are allowed.

| Type | Required content |
|---|---|
| FWK framework | Purpose, scope/context, architecture, governance, process interactions, applicability/deployment, navigation and assurance |
| POL policy | Purpose/applicability, commitments, accountability, communication/implementation and review |
| STD standard | Purpose, scope, roles, identifiable requirements, implementation/interfaces, verification, deviations, records, sources and history |
| PRO process | Purpose/scope, owner/interfaces, trigger/inputs, activities/controls, outputs/receivers, measures/acceptance, exceptions and records |
| SOP procedure | Purpose/scope, roles, prerequisites/resources, sequence/controls, acceptance/hold/escalation and outputs/records |
| WI instruction | Task/scope, prerequisites/authorization, tools, ordered actions, checks/limits, stop/escalation and handback evidence |
| PLN plan | Purpose/scope/objectives, authority, activities/resources/schedule, interfaces/communication, success/activation criteria, contingencies, review and records |
| FRM form | Template identity/revision, use instructions, context, mandatory/conditional/optional fields, validation and unknown/N/A treatment, evidence/decision, sign-off and filing |
| REG register/schema | Identity/scope/custodian, field dictionary, ID/entry rules, update/correction rules, status/validation, retrieval/access and history/retention |
| REC record | Identity, event/scope/actor, actual origin/configuration, observations, evidence/decisions, necessary sign-off and correction trail |
| ASP assurance protocol | Claim/scope, criteria/source, competence/independence, sampling/method, evidence, decision/hold rules and follow-up |
| RPT report | Purpose/scope, method, evidence/results, findings/limits, conclusion, actions/owners, review and attachments; assurance reports also state sampling and freshness/confidence |

Digital forms and workflow specifications additionally identify configuration,
trigger, validation, permissions, approvals, exceptions and audit events. Their
execution records remain separate. Mixed documents declare a primary type and
cover the relevant additional components.

## 5. Lifecycle, exceptions and interfaces

Create and register a draft with a named intended owner role. Review the exact
content, sources and interfaces; retain findings. An authorized approver records
approval and any conditions separately from the effective date. Before effective
use, confirm access, necessary briefings/competence and applicable configuration.
For changes, preserve prior evidence, assess affected documents/tools/training,
increment revisions and repeat affected review. Mark obsolete views without
destroying retained evidence or deliberately authorized older configurations.

A proposed mandatory departure records the affected rule/document/revision,
scope, rationale, risk, alternatives, compensating measures, owner, authority,
expiry and closure conditions. Hold affected effective use until legitimately
decided. Internal authority cannot waive an external obligation. This draft has
no approved deviations.

The public inventory is a distribution view. The maintainer's private preparation
index remains the authoring master. Neither public copies nor stable links confer
approval. A future organization establishes its own authorized index and records.

## 6. Verification and acceptance

For each applicable check record Pass, Fail, Pending or Not applicable with a
reason: identity/filename/index consistency; type-profile completeness; source and
requirement traceability; authority and appointments; tailoring/deviations;
links and usability; version/configuration access; evidence protection/history;
and exact review/approval/effectiveness conditions. Separate content presence,
design adequacy, user trials and observed operating effectiveness.

Draft publication additionally requires an exact reviewed file inventory,
rights/licensing disposition, source/privacy/security checks and satisfaction of
the project's recorded release gate. Publication must retain draft labels and
cannot substitute for operational acceptance. Independent or specialist review
is not supplied by this author-created document.

## 7. Records, sources and history

Retain assessments, findings, decisions, deviations, exact snapshots, distribution
records and correction trails. The adopting custodian must establish a schedule
from actual obligations before disposal; no universal retention period is implied.
Keep private client data, source libraries, credentials and internal review records
out of the public candidate. The current local preservation arrangement does not
claim tested backup or restore capability.

This is a newly authored scoped formulation of the project's internal rules,
prepared under OIMS-STD-DOC-001 r05. It does not reproduce publisher standards.
Historical source-use permissions remain a separate audit question; this new
document does not erase provenance or resolve third-party rights.

STD map: purpose/scope §1; roles §2; requirements §§3–4; implementation/deviations
§5; verification §6; records/sources/history §7. r01, 2026-10-30: initial draft
for release-readiness review. Author checks retained locally; competent review,
approval and organizational effectiveness pending.

## Draft publication decision — r02

2026-10-30: Edward Wee authorized public draft distribution with recorded
unresolved risks accepted, superseding the earlier publication hold for this
selection. This decision does not close those findings, grant third-party rights
or approve organizational use. See [GOVERNANCE.md](../../GOVERNANCE.md).
Earlier preparation/release-pending statements describe the retained drafting
context; this decision controls public distribution only. Previous r01 bytes
are retained in private history. Operational status remains Draft, not effective.
