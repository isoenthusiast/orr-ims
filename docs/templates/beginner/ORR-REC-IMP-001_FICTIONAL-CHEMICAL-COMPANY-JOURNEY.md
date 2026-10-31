# Fictional chemical company journey

| Control field | Value |
|---|---|
| Document ID / type / revision | ORR-REC-IMP-001 / REC / r01 |
| Status / prepared | Draft; not approved or effective / 2026-11-01 |
| Scope / module / layer | Beginner implementation learning kit / IMS implementation, design-r01 unreleased / Layer 1 reusable design; fictional Layer 2–4 applications explicitly labelled |
| Owner / actual appointment | Learning example custodian / Unassigned |
| Author | Codex at Edward Wee's request; original AI-assisted drafting |
| Reviewer / approver | Competent IMS and relevant discipline reviewer / Authorized adopting management; both Unassigned |
| Approval / effective date | Not approved / Not effective |
| Classification / lifecycle | Candidate public learning draft; no real operational data / Retained fictional demonstration |
| Basis | ORR-STD-DOC-001 r02; OIMS-STD-DOC-001 r05 private authoring basis |
| Canonical / index | This Markdown file; public candidate inventory ORR-REG-REL-001; private authoring index ORR-REG-DOC-001 |
| Review trigger | Before adoption/publication; changed scope, obligation, workflow, evidence or user finding |
| Access / retention | Public blank or fictional example only; adopted records in authorized private storage. Preserve pending retention schedule and holds; no automatic deletion |
| Supersedes / deviations | None / None; combined headings retain type-profile content |

## Record origin and fictional setting

**All people, events, quantities, decisions and evidence below are fabricated for
learning. No plant event, real approval, observed test or participant trial occurred.**
Example configuration: FC-DEMO-01, created 2026-11-01 by Codex. Origin: the five
ORR-FRM-CTX/RSK/OBJ/DOC/MRV-001 r01 worksheets and their paired r01 procedures.
This is a combined worked record; the table sections map to those five forms.
Scenario dates are fictional and in Asia/Kuala_Lumpur. Narrator: Codex; fictional
roles below are actors within the story, not actual reviewers of this package.

Fictional company: **Cedar Estuary Blending**, a single-site industrial cleaning
liquid blender with two shifts, a dispatch office and an outsourced transporter.
No chemical recipe, hazard classification, permit determination or repair instruction
is supplied. The example addresses customer-specification communication only.

| Fictional person | Role and scenario responsibility |
|---|---|
| Maya Tan | Implementation manager / context and coordination |
| Arun Das | Shift supervisor / point-of-work communication control |
| Lina Rahman | Quality coordinator / specification owner and data custodian |
| Ben Lim | Maintenance planner / consulted on equipment-change interfaces |
| Sofia Lee | Site director / scoped resource and risk decisions |
| Daniel Wong | Internal reviewer / sampled administrative outcome checks; fictional independence limited to not performing the sampled control |

## 1. Completed context worksheet — FC-CTX-001

Origin ORR-FRM-CTX-001 r01 / FC-DEMO-01. Maya records 2026-09-01 09:00 +08:00.
Scope: customer order review through blending, quality release and dispatch at
the one site, both shifts; procurement, maintenance and transporter interfaces
included. Broader environmental, OH&S and continuity assessment remains pending.
Parties: customer needs agreed specification at dispatch; operators need an accessible
authorized instruction; transporter needs correct dispatch information. Source
FC-E01 is a fictional customer-change note, not a real contract.

No design exclusion is assumed; applicability assessor Maya has action FC-A00 due
2026-09-15 to obtain competent advice on scope/obligations. Legal applicability is
**assessment pending**, not “compliant.” Potential quality impact: incorrect customer
specification. Environment/OH&S effects of any physical change require specialist
assessment; this case authorizes no physical change. Continuity dependency: authorized
specifications must remain accessible during an information-system outage; recovery
criteria/strategy not yet assessed. Scope decision FC-D01, Sofia, 2026-09-02:
accept the administrative pilot boundary only; do not claim full-system coverage.
Maya briefs all process owners under FC-E02; next review at material change or 2026-10-01.

## 2. Completed risk/control worksheet — FC-RSK-001

Origin ORR-FRM-RSK-001 r01. Arun reports 2026-09-03 08:00 +08:00 that the night-shift
folder still contains the prior customer-specification instruction. Facts are from
fictional folder inspection FC-E03; no incorrect dispatch is assumed. Triage:
administrative exposure, route to Lina and site director the same day; any actual
unsafe situation would require the site's authorized response, outside this case.
Lina acknowledges and owns the risk; linked objective FC-OBJ-001.

Cause → event → consequence: an unconfirmed handoff allows an obsolete specification
to be selected, potentially causing an incorrect batch/dispatch and customer rejection.
Existing control: daytime email distribution; no night-shift acknowledgment evidence.
Assessment criteria FC-CRIT-01, fictional internal pilot rule: an unverified current
specification blocks the affected release decision. No numeric matrix is used;
consequence/likelihood remain uncertain. Quality, shift and maintenance representatives
are consulted; physical change applicability remains a separate specialist question.

Sofia decides FC-D02 on 2026-09-04, under fictional delegation FC-AUTH-01 for this
administrative pilot: treat the communication risk; fund two shift briefings and
controlled-access checks. She does not accept technical/legal risks or waive duties.
Review expires 2026-10-01 or on a missed control execution. Related meeting FC-MRV-001.

**FC-CTL-001 — discrete control statement**

- Who: shift supervisor.
- What: verify the approved customer-specification revision and affected-operator acknowledgment.
- When: before the first affected batch after each authorized specification change.
- Where: the blending workpoint and authorized specification index for the affected order.
- Why: prevent obsolete-specification use, addressing FC-RSK-001 and FC-OBJ-001.
- How: match order/specification ID and revision to the effective index, verify each
  affected operator's acknowledgment, and hold the affected release decision if either
  check fails. Escalate to the quality coordinator; do not substitute a draft.
- Evidence: attributable check recording order/change, revision, operator coverage,
  supervisor/date, result and any hold/escalation reference.

Action FC-A01: Lina prepares the revised distribution method by 2026-09-06.
FC-A02: Arun briefs both shifts and verifies access by 2026-09-08. Daniel samples
every affected pilot change during September against the control criteria. Test
frequency thereafter is to be decided at review; the risk remains monitored, not erased.

## 3. Completed objective worksheet — FC-OBJ-001

Origin ORR-FRM-OBJ-001 r01. Lina owns outcome and data. Objective: every pilot
specification change has verified shift coverage before its first affected batch.
Baseline FC-E04: August fictional review, 3 of 4 changes evidenced (75%); one
missing record is “not evidenced,” not an assumed successful briefing.
Measure: evidenced changes divided by all applicable pilot changes, times 100.
Population includes both shifts; no unexplained exclusions. Target: 100% for September,
deadline 2026-09-30. This is a teaching target, not an ISO or legal threshold.
Zero changes → not measurable, not 100%. Missing evidence remains in the denominator
and is reported separately. Lina validates the change index against the schedule.

Plan: FC-A01/FC-A02; two briefing sessions and supervisor time approved in FC-D02.
Milestone: controlled release before first affected use. September FC-E08 result:
4 of 5 changes evidenced on time = 80%; one missing night-shift acknowledgment.
Target **missed**, despite the procedure being issued. Review FC-D04 orders follow-up
FC-A03; no retrospective target change. Original measure and target remain intact.

## 4. Completed document-control worksheet — FC-DOC-001

Origin ORR-FRM-DOC-001 r01. Lina drafts fictional internal procedure FC-SOP-01 r01,
scope both shifts, replacing an informal email-only method retained as FC-E05.
This fictional procedure is not an additional supplied master or hidden attachment.
Dependencies: shift instruction, check form, access permissions and briefing roster.
Basis: FC-CTL-001 and FC-D02; no external clause interpretation is claimed.
Daniel's fictional review FC-E06 on 2026-09-06 finds the night-shift roster missing;
status **In review / hold**. Lina adds the roster and resubmits an identified r02.
Sofia approves that fictional r02 on 2026-09-07; approval alone does not make it effective.

On 2026-09-08, Arun has only day-shift briefing evidence: **Approved / Not effective**
for the intended both-shift release. The director holds affected new-use authorization;
the example does not invent an emergency operating workaround. On 2026-09-09, fictional
FC-E07 records both-shift briefing and access checks, index update and obsolete-copy
withdrawal. The authorized r02 becomes effective for the pilot only. FC-A01/FC-A02
are implementation-complete; outcome remains pending. September's later missed
execution is a control failure after release, not a reason to erase the release history.

Storage: fictional private IMS index, custodian Lina, role-limited access. Retention
schedule and recovery test are **pending**; FC-A05 assigned to Maya due 2026-10-10.
No tested backup/recovery claim is made. All substantive records are preserved.

## 5. Completed management-review worksheet — FC-MRV-001 and FC-MRV-002

Origin ORR-FRM-MRV-001 r01. FC-MRV-001, 2026-09-04 10:00 +08:00: Sofia chairs with
Maya, Lina, Arun and Ben; FC-AUTH-01 covers only pilot administrative resources and
decisions. Inputs: FC-CTX-001/FC-RSK-001, proposed FC-OBJ-001 and FC-E03/04.
Options: continue email only (rejected for missing coverage), controlled acknowledgment
(selected), defer all action (rejected). Arun notes workload concern; Sofia allocates
briefing time. FC-D02 and actions FC-A01/02 recorded; recipients acknowledge same day.
Full-system assurance, legal applicability and continuity inputs are absent; those
conclusions are held and assigned FC-A00/04, not described as reviewed satisfactorily.

FC-MRV-002, 2026-10-01 10:00 +08:00: same participants plus Daniel. FC-E08 proves
4/5, not 5/5. FC-D04 records objective missed and FC-RSK-001 **reopened**; no claim
of sustained control effectiveness. FC-A03: Arun to repair the relief-supervisor
handoff and demonstrate the next two eligible executions by 2026-10-15; if fewer
occur, extend observation and keep outcome_pending. Resources: one handoff session.
Lina owns FC-A04, due 2026-10-15, to scope continuity dependency assessment with a
competent lead; this is not a completed BIA. FC-A00 remains overdue: escalate to
Sofia, no obligation-compliance conclusion. Next review 2026-10-16.

FC-E09 on 2026-10-14 shows the next two eligible changes had both-shift coverage.
Daniel records a scoped 2/2 test, limited confidence and no broader sampling claim.
FC-D05, Sofia, 2026-10-16: close FC-A03 for its stated pilot criterion; return the
risk to **monitored**, review 2026-11-16 or earlier failure. September's 80% result
and missed target remain unchanged. FC-A00/04/05 remain open or overdue unless
separately evidenced; no company-wide effectiveness or certification conclusion.

## Evidence index, correction and limits

These evidence IDs refer to the fictional descriptions above, **not existing source
files, signed records or attachments**. In real use each must resolve to retained
evidence in the private operational index.

| Evidence | Description / relationship |
|---|---|
| FC-E01 / FC-E02 | Customer-change note / context briefing; FC-CTX-001 |
| FC-E03 / FC-E04 | Obsolete-folder observation / August 3-of-4 baseline; FC-RSK-001, FC-OBJ-001 |
| FC-E05 / FC-E06 / FC-E07 | Prior method / reviewer hold / release conditions satisfied; FC-DOC-001 |
| FC-E08 | September 4-of-5 result; FC-D04 reopening |
| FC-E09 | Two subsequent eligible executions passed; FC-D05 scoped follow-up decision |

Fictional correction FC-COR-01: Lina, 2026-10-01 09:00 +08:00, corrects the initial
September summary “5/5” to “4/5”; original retained, reason: one change lacked
night-shift acknowledgment. FC-E08 and FC-D04 use the corrected value. A real
system would retain both source entry and amendment with access history.

Preparers/reviewers/sign-offs in the narrative are fictional. Actual package
author check is separate and cannot be substituted for them. This case demonstrates
normal, held, failed, corrected and reopened paths; it is not evidence of usability,
legal compliance, technical safety, operating effectiveness or certification readiness.

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
