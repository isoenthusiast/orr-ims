# ORR IMS — draft public edition

**ORR IMS is an open-source integrated management system guidance project,
providing practical guidance, reusable templates and examples to help implementers
develop and improve their own management systems.**

**Current status: Draft.** The content is under development and welcomes review
and practical feedback. Start with the implementation documents below.

**Compilation and application design led by [Edward Wee](https://www.linkedin.com/in/edwardbhwee/).**
This credit covers this project's compilation, documentation structure and
proposed application architecture. Edward does not claim authorship of IOGP
publications, ORCA (Objective → Risk → Control → Assurance), ISO standards or
other referenced frameworks and standards. Those contributions remain credited
to their respective originators, authors and publishers.
See [project attribution](AUTHORS.md) for contribution scope and acknowledgments.

The intended scope is original management-system guidance and a future software
core. Specialist commercial plugins and client material are outside this edition.
No application or complete management-system template pack is implemented here yet.
The [learning template starter](docs/templates/README.md) adds all twelve document
types for one bounded workflow as a public learning draft; it is not the complete
process library or an approved ISO mapping.

Content is selected and reviewed individually. No private repository history,
publisher publications, converted source texts or client records are included in
this candidate. This repository does not establish ISO certification,
regulatory compliance, publisher endorsement or operational effectiveness.

Original documentation is licensed under CC BY 4.0; code and specified design
assets use Apache-2.0. See [LICENSING.md](LICENSING.md) for the exact allocation,
third-party exclusions and the distinction between licensing and release approval.

Edward Wee authorized the earlier 27-file draft publication on 2026-10-30 with the recorded
unresolved risks accepted. The learning additions have a separate 2026-10-31 draft publication decision.
That historical decision is not independent legal clearance or approval
for organizational operation. See
[governance](GOVERNANCE.md), [source acknowledgments](SOURCES.md) and
[candidate inventory](docs/governance/ORR-REG-REL-001_RELEASE-INVENTORY.csv).

## Start here — implementation

Use these draft adoption documents to assess your existing system and plan a
scoped implementation. They are guidance and blank templates, not an implemented
application, approved operating instructions or a guarantee of certification.

1. [Implementation Guide](docs/implementation/ORR-SOP-IMP-001_IMPLEMENTATION-GUIDE.md)
   — responsibilities, adoption routes, stages, acceptance gates and evidence.
2. [Adoption Assessment](docs/implementation/ORR-FRM-IMP-001_ADOPTION-ASSESSMENT.md)
   — map current practices, requirements, evidence and gaps.
3. [Implementation Plan](docs/implementation/ORR-PLN-IMP-001_IMPLEMENTATION-PLAN.md)
   — assign actions, resources, dependencies, pilot criteria and rollout decisions.

Retain useful existing processes and tools. Keep completed organizational records
in private storage. All three documents are r03 Draft; review and approval remain
pending.

## Progressing beyond draft

The proposed progression is **Draft → Release candidate → Stable documentation
release**. These labels describe the maturity of the published guidance, not
certification or approval of an organization using it.

Before calling a defined documentation package stable, we propose to:

1. **Define and complete the release scope.** List the processes, guides, forms
   and examples included, their dependencies and exclusions. Provide usable
   end-to-end coverage for that scope; do not imply the entire planned IMS exists.
2. **Obtain competent review.** Have reviewers with relevant management-system
   and implementation experience assess correctness, clarity, applicability and
   source traceability. Keep author checks distinct from independent review.
3. **Trial it with representative implementers.** Demonstrate that users can
   assess their existing system, tailor a process, assign responsibilities, use
   the forms and retrieve evidence. Exercise exceptions and record problems.
   Label fictional demonstrations separately from real implementation evidence.
4. **Resolve material findings.** Correct missing instructions, contradictions,
   broken links and unusable forms; verify the fixes. Disposition source/rights
   and naming issues with evidence, recording any remaining limitations.
5. **Approve an exact version.** Record the maintainer's release decision against
   the defined criteria, reviewed revisions and file inventory. Include release
   notes, known limitations and guidance for adopters upgrading earlier versions.
6. **Maintain it.** Assign document owners, a reporting route and review triggers;
   preserve revision history and respond to corrections and source changes.

A release candidate is a complete proposed package undergoing final validation.
A stable documentation release is a reviewed, trialled and maintained baseline
for its declared scope. Stability is earned through evidence, not simply elapsed
time or removal of a Draft label. These maturity criteria are proposals for
maintainer adoption; no review, pilot or stable-release decision is implied here.

The future application has its own readiness criteria, including functional,
security, privacy, migration and recovery testing. A stable documentation release
does not require the app to exist. Each adopting organization still needs to
authorize its own configuration and demonstrate operating effectiveness.

## Brand kit — draft


The working visual direction is **04 — Engineered Layers**, with a vibrant
navy, cobalt, teal, amber and cool-white palette.

- [Brand guide](brand/ORR-STD-BRD-001_BRAND-GUIDE.md): colour, typography, layout,
  illustration, component and accessibility rules.
- [Browser preview](brand/ORR-STD-BRD-001_BRAND-PREVIEW.html): open locally to see
  the palette and illustrative components; this is not the application.
- [Token master](brand/ORR-STD-BRD-001_TOKENS.json),
  [CSS variables](brand/ORR-STD-BRD-001_TOKENS.css), and
  [palette CSV](brand/ORR-STD-BRD-001_PALETTE.csv).

Run `python3 brand/ORR-STD-BRD-001_BUILD-ASSETS.py --check` to verify generated
renditions and declared contrast pairs. Use `--write` after intentional token
changes. The kit is ORR-STD-BRD-001 r03, Draft; name clearance, final logo,
competent review and organizational approval remain pending. No external fonts or icon packs
are bundled. Local control records and concept-image provenance are excluded
from the candidate payload.

## Repository and data preview

Read the [repository blueprint](docs/ORR-FWK-REP-001_REPOSITORY-BLUEPRINT.md) for
the proposed public folder tree, future core/plugin boundaries and logical data
model. The paired [fictional JSON](docs/ORR-FWK-REP-001_FICTIONAL-DATA.json) shows
a risk-to-leadership journey with no actual operating evidence. These are r03
drafts; application folders, schemas and runtime remain proposed.

## Learning draft publication — 2026-10-31

Edward Wee authorized publication of the reviewed 43-file learning draft,
including the twelve-type starter and release-control fixes, with the stated
unresolved risks retained. Historical source-use permissions, name clearance and
independent competent review remain open; two proposed ISO mapping rows remain
unverified. This decision does not establish legal clearance or organizational
approval. The 2026-10-30 decision remains tied to its earlier selection. See the [publication register guide](docs/governance/ORR-REG-REL-002_PUBLICATION-GUIDE.md)
for file-level provenance, unresolved rights questions and current decision status.
