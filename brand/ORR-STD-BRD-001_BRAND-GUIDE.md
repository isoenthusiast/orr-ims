# ORR IMS brand guide

**04 — Engineered Layers · vibrant refinement**

| Control field | Value |
|---|---|
| Document ID / type / revision | ORR-STD-BRD-001 / STD / r03 |
| Status / prepared | Draft — local design basis, not effective / 2026-10-30 |
| Purpose / scope | Consistent ORR IMS identity across future software, documents and diagrams; this brand kit only |
| Module / layer | Public-edition branding, design-r01 unreleased / Layer 1 product reference |
| Governing standard | ORR-STD-DOC-001 r02 — public control draft; historical basis OIMS-STD-DOC-001 r05 |
| Owner role / appointee | Brand steward / Unassigned |
| Author | Codex, at Edward's request |
| Reviewer role / appointee | Brand and accessibility reviewer / Unassigned |
| Approver role / appointee | Product governance authority / Unassigned |
| Approval / effective date | Not approved / Not effective |
| Classification / lifecycle | Public draft; organizational approval pending / Maintained |
| Authoritative location / index | This guide with token master; ORR-REG-REL-001 candidate inventory |
| Source basis | User selected direction 04; requested more vibrant colours and this kit; proposed supporting rules below |
| Review trigger | Before adoption/public release; colour, typography, component, platform or identity change |
| Supersedes / deviations | r02 retained in private publication snapshot / No content deviations; owner publication decision recorded below |
| Retention | Preserve revisions and checks; no automatic disposal; schedule and custodian pending |

## 1. Purpose and design status

Express interconnected work through a stable foundation, modular capabilities and
traceable evidence. Be precise, approachable and energetic. The selected direction
is **Engineered Layers**. The five-colour vibrant refinement is the working basis
requested for this kit; typography, supporting shades and component rules are
author proposals for review. This is not approval of every detail shown here.

ORR IMS is a provisional name. The kit does not clear the trademark. Licence allocations are stated in
[LICENSING.md](../LICENSING.md). The proposed line is **Connected systems. Clear evidence.** ORCA remains
Objective → Risk → Control → Assurance; branding does not rename the operating model.

## 2. Responsibilities and applicability

The brand steward maintains tokens and examples. Designers use the guide and test
real layouts. Developers consume tokens and test implemented controls. The reviewer
checks visual consistency, accessibility and claims; the approver decides exact
release scope. All actual appointments remain pending.

Apply to new public-edition drafts, including a future core and plugin interface.
Plugin identity may add a module name but must preserve readable shared controls,
status meanings and identity boundaries. Client identity overlays require a scoped
configuration and renewed contrast checks. This kit builds no application.

## 3. Colour system

The [JSON tokens](ORR-STD-BRD-001_TOKENS.json) are the machine-readable colour
master. The [CSS](ORR-STD-BRD-001_TOKENS.css) and
[palette CSV](ORR-STD-BRD-001_PALETTE.csv) are generated from it. Edit JSON first,
then regenerate and verify; do not maintain competing values in CSS or images.

| Colour | Exact sRGB hex | Intended role | Foreground |
|---|---|---|---|
| Deep navy | #10243A | Text, navigation, core foundation | White on navy |
| Electric cobalt | #315CFF | Primary action, selected navigation, brand emphasis | White |
| Vivid teal | #00B8A9 | Connection accents, plugin illustration | Navy |
| Bright amber | #FFB627 | Module/evidence highlights in brand illustration | Navy |
| Cool white | #F5F8FF | Page canvas | Navy |

Use white #FFFFFF for raised surfaces. Start with predominantly light surfaces,
navy structure and a small amount of vivid colour; a useful composition target is
roughly 70% light, 20% navy and 10% vivid accents, not a compulsory pixel quota.
One dominant accent per region is preferable to colouring every module equally.

Bright teal and amber are **not** small-text colours on white. Use teal ink #007C72
for meaningful connection strokes/text on light surfaces; amber ink #8A4B00 for
amber-family text. White text on bright teal/amber is not an allowed pairing.
Use cobalt hover #2448D8 rather than reducing text opacity; also use that darker
cobalt for selected text on pale cobalt #EBF0FF. Subtle border #CFD9E8
is for nonessential separators; input boundaries use #7C8CA3.

The concept raster is inspiration only: it contains an incorrect teal code and
does not define exact colour or geometry. **#00B8A9 is authoritative.** Do not sample
colours from it. Print conversions require an actual output profile and proof;
this kit does not invent CMYK or Pantone equivalents. Dark mode is not specified.

## 4. Status and accessibility

Brand colour is separate from an assurance conclusion. Amber evidence tiles in an
illustration are not warnings; teal modules are not evidence of passing controls.
Operational status always has an explicit label and, where useful, a distinct shape.

| Semantic state | Text / background | Meaning boundary |
|---|---|---|
| Passed | #18713A / #E8F5EC | Only for an evidenced result against stated criteria |
| Needs attention | #8A4B00 / #FFF3D6 | Review/action needed; not automatically failure |
| Failed | #B42318 / #FDECE9 | A recorded criterion failed; expose detail and action |
| Not assessed | #526174 / #EDF0F4 | Unknown or unassessed, never silently green |

BRD-01: normal text must meet 4.5:1 against its actual background; meaningful UI
boundaries and graphical cues must meet 3:1 where required. These are selected
WCAG 2.2 AA criteria, not a complete conformance claim. This kit aims for 4.5:1 even
on large text. Test actual rendered combinations, not a palette in isolation.

BRD-02: never use colour alone for status, selection, required fields or connections.
Label routes and nodes. Underline inline links. Add visible field labels and errors.

BRD-03: keyboard focus uses a navy outline separated by a white gap, including on
navy backgrounds. Preserve browser/forced-colour focus. Avoid clipped focus rings.
Use a 44px minimum interaction target as a product usability rule; retain semantic
HTML, keyboard access, zoom and reduced-motion support. Do not disable user scaling.

BRD-04: no auto-rotating 3D diagrams, pulsing alarm decoration, flashing status or
animation required to understand work. If needed, use 160ms transitions and remove
them under reduced-motion preferences. Brand motion never substitutes for a record.

## 5. Typography and provisional wordmark

Use a system sans-serif stack: system-ui, -apple-system, BlinkMacSystemFont,
Segoe UI, sans-serif. Use system monospace for IDs and technical values. No font
files are bundled or downloaded. Rendered fonts vary by device and need review.

| Use | Size / weight | Notes |
|---|---|---|
| Brand/hero statement | 40px / 700 | Reduce to 32px on small screens |
| Section heading | 28px / 600 | Clear hierarchy, sentence case |
| Subheading | 20px / 600 | Short and concrete |
| Body / editable fields | 16px / 400 | Line-height 1.5 |
| Labels / table body | 14px / 400–600 | Do not shrink dense tables to fit |
| Nonessential metadata | 12px / 400 | Never the only location of a critical condition |

Use the plain text lockup **ORR IMS**: ORR at weight 700, IMS at 400–600, with a
clear gap. Prefer navy on light surfaces or white on navy. Preserve at least half
the capital-letter height around it; use at least 24px type in standard headers.
This is a provisional typographic lockup, not a final custom logo or trademark.
The raster's decorative serif treatment is not adopted by this guide; the system
sans proposal prioritizes readable operational use. No ™/® or endorsement seals.

Do not stretch, rotate, outline or insert a plugin name inside the lockup. A plugin
descriptor belongs below/beside it: “ORR IMS / Maintenance” with clear separation.
Do not imply that a third-party plugin is first-party merely through the lockup.

## 6. Layout and reusable components

Use the spacing scale 4, 8, 12, 16, 24, 32, 48, 64px. Use 8px control corners and
12px panel corners. Align text and controls to a consistent grid; avoid excessive
cards, gradient backgrounds and decorative shadows around every object.

Desktop product direction: slim navy navigation, light main workspace, local task
context, work area and an optional evidence/history panel. Preserve IMS Design and
IMS Operations as the two principal workspaces; Processes, Controls and Evidence
are contextual destinations, not new independent top-level systems. On narrow
screens stack panels and provide labelled navigation; do not shrink a desktop UI.

BRD-05: use cobalt + white for a primary action; use a bordered light secondary
action. Links stay underlined in prose. Destructive actions use a labelled failure
colour and appropriate workflow confirmation; do not make every warning destructive.

BRD-06: show document ID, revision, scope and Draft/Effective state where relevant.
Presentation must not hide unresolved conditions, approval boundaries or required
evidence. Tables need readable headers and explicit unknown values. Never replace
“Not assessed” with a zero or a green badge. Examples must be labelled fictional.

Documents: use a restrained navy title, cobalt section accents, simple rules,
generous margins and a visible control block. Slides: one claim/diagram per slide,
clear source/status footer. Monochrome copies must retain labels and structure.
Brand styling must never remove required document controls.

## 7. Drawing and image direction

Use clean isometric engineering illustrations for explanations: a stable core
plane, separable plugin blocks, visible connections and a distinct evidence plane.
Use consistent approximately 30° isometric axes, restrained depth and lighting.
Core is navy/cobalt; plugin accents teal/cobalt; evidence highlights amber. This
is an explanatory convention, not a claim that evidence is owned by a separate
runtime layer or that only plugins create evidence.

BRD-07: labels and leader lines must explain relationships. Keep meaningful lines
at least 2px at final display size and sufficiently contrasted. Number crowded
callouts; supply text alternatives and a flat reading order. Decorative geometry
must not be mistaken for a real system topology or implemented capability.

Use flat 2D diagrams for workflows, decision gates and daily task navigation. Keep
isometric illustrations for brand/application explanations. Do not use transparent
glass, neon glow, rainbow gradients, orbital motifs, stock safety seals or fake
technical schematics. Do not recolour a failure to make a page match the palette.

Icon direction: consistent 2px monoline shapes on a 24px grid, paired with text for
important actions. No icon library is bundled or selected; review its licence and
attribution before adopting one. Avoid drawing new symbols that resemble ISO or
other publisher marks. Photos, if later used, need rights and appropriate consent;
prefer real work context over staged dashboards or unsafe practices.

The AI-generated reference board is retained only under ignored local references,
with provenance; it is not part of the distributable kit or a final production logo.

## 8. Voice and examples

Write directly about who does what, what happens next and what evidence is needed.
Prefer “Review the risk and assign an owner” to vague transformation language.
Prefer “Evidence missing” to “System healthy” when the state is unknown. Avoid
“guaranteed compliance”, “ISO certified software” and unsupported coverage claims.

The [brand preview](ORR-STD-BRD-001_BRAND-PREVIEW.html) shows colours, typography,
buttons, states and a fictional process example. It is a static brand specimen,
not a working IMS or a claim of approval. Its links work; specimen controls are
explicitly illustrative and create no records.

## 9. Implementation, verification and change

Load `ORR-STD-BRD-001_TOKENS.css` before component styles. Use semantic variables
such as `--orr-primary`, `--orr-text` and `--orr-failure-text`; use raw palette
variables for illustrations only. JSON is a project schema, not a claim of DTCG
standard compatibility. CSS, palette CSV and contrast results derive from it.

BRD-08: run `python3 brand/ORR-STD-BRD-001_BUILD-ASSETS.py --check` from the repo
root to compare generated files and calculate all declared pairs. Regenerate with
`--write` after an intentional change. The builder does not approve a revision.

Before acceptance: verify tokens/renditions match, links and ID/revision match the
local register, all declared contrast pairs pass, preview reflows at 320/768/1280px,
and keyboard focus/zoom remain usable. Obtain representative-user and competent
brand/accessibility review. Automated checks are bounded author checks only.

STD profile map: purpose §1; scope/roles §2; requirements §§3–8; implementation and
verification §9; deviations §10; records §10; sources §11; history §12. No mandatory
content deviation is used. V01–V09 author dispositions are retained locally with
exact hashes; actual approval, release and operational evidence remain pending.

## 10. Exceptions, records and unresolved items

Routine diagrams may vary in composition while preserving identity, readability
and meaning. Material colour/type changes require token updates and renewed checks.
For a mandatory-rule departure, record affected rule, scope, rationale, impact,
compensating measures, owner, authority, expiry and closure evidence; hold effective
use until legitimately decided. An internal exception cannot waive external duties.

Preserve prior guide, tokens, renditions, register and checks before changing an
assessed revision. The local document controller maintains the ORR-only index;
the private OIMS index remains separate and unchanged. Keep working assessments
and reference-image provenance under ignored local storage. No automatic disposal.

Remaining decisions: name/trademark clearance; final logo; typography acceptance;
actual reviewers and approver; dark theme; print proof; third-party source rights;
representative user trials; and public-release clearance. None blocks local draft
design work, and none is implied completed by the generated preview.

## 11. Sources and provenance

- User discussion: direction 04 selected; more vibrant colours requested; exact
  written palette takes precedence over AI-rendered swatch text.
- OIMS-STD-DOC-001 r05 is a private authoring dependency retained outside this
  candidate. Its exact identity/hash is recorded in local checks; no private source
  content is copied into the kit. A standalone [public control draft](../docs/governance/ORR-STD-DOC-001_DOCUMENT-CONTROL.md)
  is now supplied; competent review and source-rights disposition remain pending.
- [W3C contrast minimum](https://www.w3.org/WAI/WCAG22/Understanding/contrast-minimum.html),
  [non-text contrast](https://www.w3.org/WAI/WCAG22/Understanding/non-text-contrast.html),
  and [use of colour](https://www.w3.org/WAI/WCAG22/Understanding/use-of-color.html),
  consulted for the limited criteria in §4. These are explanatory guidance;
  this brand kit is not a full WCAG audit or certification.
- Supporting shades, layouts, wording and component proposals are newly authored
  for this task. No third-party fonts, icons or publisher publications are bundled.

## 12. Revision history

| Revision | Date | Change | State |
|---|---|---|---|
| r01 | 2026-10-30 | Initial vibrant Engineered Layers kit, tokens, palette, preview and author checks | Draft; no effective/public release |

| r02 | 2026-10-30 | Add public control/inventory links and confirmed licence boundary; visual tokens unchanged | Draft; release acceptance pending |

See the [candidate inventory](../docs/governance/ORR-REG-REL-001_RELEASE-INVENTORY.csv)
for distribution identity. The public control draft does not retrospectively clear
historical source use.

## Draft publication decision — r03

2026-10-30: Edward Wee authorized public draft distribution with recorded
unresolved risks accepted, superseding the earlier publication hold for this
selection. This decision does not close those findings, grant third-party rights
or approve organizational use. See [GOVERNANCE.md](../GOVERNANCE.md).
Earlier preparation/release-pending statements describe the retained drafting
context; this decision controls public distribution only. Previous r02 bytes
are retained in private history. Operational status remains Draft, not effective.
