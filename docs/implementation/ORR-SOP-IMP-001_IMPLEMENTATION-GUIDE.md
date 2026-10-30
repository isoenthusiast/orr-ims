# ORR IMS Implementation Guide

| Control field | Value |
|---|---|
| Document ID / type / revision | ORR-SOP-IMP-001 / SOP / r03 |
| Status / prepared | Draft; not approved or effective / 2026-10-30 |
| Scope / layer | Reusable adoption guidance; Layer 1, for future organization-specific configuration |
| Module | Implementation support / design-r01 unreleased |
| Owner / author | Implementation lead, Unassigned / Codex at Edward Wee's request |
| Reviewer / approver | Competent IMS reviewer, Unassigned / Product governance authority, Unassigned |
| Classification / lifecycle | Public draft; organizational approval pending / Maintained |
| Review trigger | Before adoption; material scope, source, workflow or product changes |
| Canonical location | This file; candidate inventory ORR-REG-REL-001 |
| Basis / supersedes / deviations | OIMS-STD-DOC-001 r05; public basis ORR-STD-DOC-001 r02 / r02 retained locally / None |

## 1. Purpose and scope

Help an organization adapt ORR IMS to its existing management system and build
traceable evidence of how it works. This is proposed implementation guidance,
not a certification scheme, clause interpretation or guarantee of audit success.
The repository currently contains design documents and examples; a working app,
complete operating template pack and commercial plugins are not supplied here.

Begin with the organization's current processes. Retain what works, adapt what
needs improvement, and replace only where justified. Use the
[Adoption Assessment](ORR-FRM-IMP-001_ADOPTION-ASSESSMENT.md) to establish the baseline
and the [Implementation Plan](ORR-PLN-IMP-001_IMPLEMENTATION-PLAN.md) to manage work.

## 2. Responsibilities and interfaces

| Role to appoint | Responsibility and decision boundary |
|---|---|
| Executive sponsor | Agree outcomes, resources and scope; resolve cross-functional obstacles within delegated authority |
| Implementation lead | Coordinate assessment, plan, dependencies, rollout and reporting |
| Process owner | Confirm actual work, risks, controls, competence and acceptance criteria for their process |
| Workers and users | Demonstrate current practice; trial proposed workflows; report gaps and usability issues |
| Document controller / evidence custodian | Maintain versions, access, record index, correction history and retention arrangements |
| Technical/system owner | Configure and validate selected tools, interfaces, permissions, backup and recovery |
| Competent reviewer / assurance lead | Verify source applicability, evaluate evidence and report limitations; preserve required independence |
| Authorized decision-maker | Approve exact configurations and residual-risk decisions within recorded delegation |

Record named appointments and delegations. Combining roles requires a recorded
rationale and must preserve applicable independent review requirements. An author
check is not independent assurance.

## 3. Prerequisites and choices

Obtain sponsor commitment, access to process users and existing records, a secure
working location, and competent access to applicable authoritative requirements.
Record source titles, editions/amendments, applicability and access rights; do
not infer current applicability from this draft's references.

Choose a route and identify the authoritative system for each record type:

- **Documentation-led:** use existing approved tools and controlled templates.
- **Connected systems:** retain existing applications, such as a CMMS, with
  defined record links and reconciled interfaces. ORR integrations remain future work.
- **Integrated application:** a future option subject to software availability,
  validation, security and deployment readiness. Do not plan as if it exists today.

No commercial plugin is mandatory for adopting the management approach. Track
missing technology as a dependency; an approved manual method may be used where
it meets the organization's needs and applicable requirements.

## 4. Implementation sequence and controls

Each gate records scope, exact versions, evidence references, reviewer, authorized
decision-maker, decision date and open conditions. Unknowns stay visible. A
material unresolved gap holds the affected rollout or claim; it is not a pass.

| Stage / accountable role | Activities and inputs | Outputs and acceptance gate |
|---|---|---|
| 1. Understand / sponsor | Discuss intended outcomes, business context, interested parties and existing system strengths with process owners | Named sponsor and lead; agreed objectives and decision authority |
| 2. Scope / implementation lead | Identify sites, services, activities, interfaces, selected standards and other obligations; record exclusions with justification | Scope boundary, authoritative source list and applicability decisions reviewed by competent persons |
| 3. Assess / process owners | Walk through actual work; inspect a justified sample of records; map applicable requirements to process, owner, control and evidence; distinguish absent evidence from absent activity | Assessment completed with unknowns, gaps, impacts and priorities; no unsupported coverage claims |
| 4. Design / process owners | Retain, adapt or replace each process; connect objectives to risks, discrete controls and assurance; agree authority and escalation | Process interactions, control statements and acceptance criteria reviewed; unresolved technical criteria block affected use |
| 5. Configure / system and process owners | Configure documents, forms, roles, workflows, evidence stores and interfaces; test permissions, exceptions, retrieval and recovery as applicable | Exact configuration accepted; named users briefed and competence needs addressed; recovery and fallback arrangements evidenced |
| 6. Pilot / implementation lead | Run a bounded, authorized pilot using real work; record failures, rework and user feedback; verify end-to-end handoffs | Pilot criteria met with real records; defects closed or explicitly held; authorized decision to expand |
| 7. Operate and verify / process owners and assurance lead | Extend coverage, monitor performance and overdue work, assess controls, conduct planned audits and management review, track corrective actions | Traceable operating evidence, assurance findings and leadership decisions; continued monitoring with unresolved gaps visible |

### Process coverage and workflow design

Inventory every in-scope process, including interfaces and outsourced activities;
the pilot is a subset, not the coverage boundary. Reconcile this inventory to the
existing P01–P23 design catalogue when that catalogue is available for authorized
use. Do not invent its missing definitions. Preserve the established ORCA model,
four fundamentals, ten elements, twelve planned internal standards and four
deployment layers; this guide does not redefine them or claim they are supplied
as a complete public pack. Record unavailable reference material as a dependency.

For each process capture: owner; trigger and inputs; outputs and receiving role;
workflow states; performer and decision authority; acceptance/stop criteria;
required records; exception route; performance measure; and authoritative tool.
Version workflow definitions separately from execution records.

A control is a discrete, testable activity addressing a specific risk and
objective. Record **who, what, when, where, why, how and evidence**. Link the
control to a method and frequency of assurance. Do not equate an uploaded
procedure, completed task or green dashboard with control effectiveness.

Pilot ordinary and exception paths: a missing input, rejected decision, overdue
action, failed check, reassignment and correction of a record. For cross-system
work, verify identifiers, handoffs, reconciliation, failed-transfer handling and
ownership of the original record. Organization-specific technical work requires
its own competent instructions and authorization; this guide supplies none.

## 5. Acceptance, holds and escalation

The sponsor authorizes rollout only within delegated authority and after the
affected owners confirm acceptance. Missing responsibility, required criteria,
material evidence or reliable access blocks the affected gate. Record the gap,
impact, owner, next action and reassessment date in the plan. Continue unaffected
work where justified. A management decision cannot waive an external obligation.

Tailor wording, layout, examples, sequencing and tools to the organization while
preserving identity, authority, applicable duties and evidence. Record material
departures and their risk, scope, compensating measures, authority and expiry.
Seek appropriate external authorization where required; do not treat internal
acceptance as permission to depart from external requirements.

Set duration from the assessment, available people, process complexity and the
operating cycles needed to gather evidence. Estimate effort and elapsed time
separately, identify dependencies, and review the forecast after the pilot. This
guide supplies no universal duration or guaranteed certification date.

## 6. Outputs, records and ongoing review

Maintain a private adoption record index covering scope/source decisions,
assessment, plan, process maps, controlled configurations, appointments,
training, pilot records, assurance, leadership decisions and corrective actions.
Each record needs identity, actor, event date/time and time zone where relevant,
scope, originating template/configuration revision, evidence location and decision
history. Correct by attributable amendment; preserve the original entry.

Before live use, assign a custodian, access permissions, retention schedule and
legal-hold/disposal authority for each record class; test retrieval and recovery
proportionately. While unresolved, preserve records and disable automatic disposal.
Keep organization data and completed assessments out of the public repository.

Review the implementation plan at its agreed cadence and on material change.
Track scope coverage, unresolved gaps, overdue actions, evidence availability and
assurance findings separately. Review effectiveness against agreed criteria; do
not use document completion alone as the success measure. Certification, if
sought, needs its own agreed scope and independent assessment arrangements.

## 7. Sources, attribution and change history

Original project guidance based on Edward Wee's requested adoption journey and
the [repository blueprint](../ORR-FWK-REP-001_REPOSITORY-BLUEPRINT.md), r03.
Document structure follows OIMS-STD-DOC-001 r05 as a private authoring dependency;
that dependency is not included or cleared for redistribution by this guide.
A self-contained public control draft now accompanies this guide; competent
review and historical source-rights disposition remain release dependencies.
No publisher text or clause-by-clause requirements are reproduced here.
See [project attribution](../../AUTHORS.md): Edward's compilation/application
design credit does not claim authorship of IOGP, ORCA or referenced standards.

SOP profile mapping: purpose/scope §1; responsibilities §2; prerequisites §3;
sequence/controls §4; acceptance/escalation §5; outputs/records §6.
Author checks are retained locally; competent review, user trial and approval
remain pending. r01 — 2026-10-30: initial draft; no predecessor or deviations.

Public control basis: [ORR-STD-DOC-001 r02](../governance/ORR-STD-DOC-001_DOCUMENT-CONTROL.md).
Distribution identity/status: [candidate inventory](../governance/ORR-REG-REL-001_RELEASE-INVENTORY.csv).
r02 — 2026-10-30: add self-contained public control basis and inventory; preserve
private authoring provenance. Draft; no organizational approval or effectiveness.

## Draft publication decision — r03

2026-10-30: Edward Wee authorized public draft distribution with recorded
unresolved risks accepted, superseding the earlier publication hold for this
selection. This decision does not close those findings, grant third-party rights
or approve organizational use. See [GOVERNANCE.md](../../GOVERNANCE.md).
Earlier preparation/release-pending statements describe the retained drafting
context; this decision controls public distribution only. Previous r02 bytes
are retained in private history. Operational status remains Draft, not effective.
