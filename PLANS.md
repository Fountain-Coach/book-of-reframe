# Publication plan

## 2026-08-17 — publish Governance Chapter 79 and the default semantic manuscript projection

- Publish a sanitized public projection of Governance Chapter 79: Reframe's continuous Courier/Fountain manuscript,
  semantic Questions/Movements/Read coverage navigation, right Copilot, bottom MIDI2 peer projection, and the explicit
  exclusion of A4 cards, horizontal timelines, and Slugline application chrome.
- Add the approved signature illustration to the Book site and public source projection. It is design evidence only,
  not runtime, AX, FountainStore, visual-regression, or release proof.
- Add the stable site route `/governance/default-semantic-manuscript-projection/`, interlink it from the home and
  Scenario-Driven Development pages, and preserve the existing navigation/footer semantics.
- Source governance: `Fountain-Coach/Reframe-Refactoring@1cbe5f2`; integration source:
  `Fountain-Coach/midi2-gpu-fabric@03302ce2`.
- No command, capability, release, live-acceptance, or runtime claim is promoted by this publication.

### Planned gates

- deterministic site-data, route, asset, metadata, link, and private-source scan;
- local browser AX/VRT acceptance for home, method, and new governance route;
- strict Book prepublication scan;
- commit and push the Book projection, then deploy the reviewed site and verify HTTPS routes/assets.
- Publication commits: `498fd6f` (initial projection), `a8b01a6` (template-fit correction); deployment pending.

## 2026-08-17 — public Scenario-Driven Development method and FountainScenarioKit

- Publish a human-readable explanation of Scenario-Driven Development, its historical relationship to E2E/CI/contract
  testing, and the role of MIDI2 as an event-driven software-peer substrate.
- Link the public FountainScenarioKit, Chapter 78, Chapter 77, the E2E coverage projection, and the public/maintainer
  boundary.
- Add the stable site route `/scenario-driven-development/`, with semantic navigation, breadcrumbs, related records,
  canonical/Open Graph metadata, and the same footer shell as the existing method and capability pages.
- Preserve the claim boundary: the kit is reusable public infrastructure; Reframe runtime, Store, AX, visual, and
  hardware claims remain separately governed and the release surface remains unchanged.

### Provenance and acceptance

- Runtime integration: `Fountain-Coach/midi2-gpu-fabric@add3acec`.
- Governance: `Fountain-Coach/Reframe-Refactoring@e3068dc`.
- Public kit: `Fountain-Coach/FountainScenarioKit@ec3a06c` (public visibility decision, README, and research references).
- Local checks: strict prepublication passed with 0 errors and 1 expected canonical-host warning; internal-link/
  metadata scan passed; Chrome CDP AX/VRT passed for `/`, `/scenarios/`, `/scenario-driven-development/`, and the
  MIDI2 capability page. The external scan reached all content checks but one GitHub URL timed out; deployment remains
  a separate handoff.
- Publication commit: `Fountain-Coach/book-of-reframe@9946725`.
- Deployment: `book-of-reframe@19d7735` deployed through the fixed `book.fountain.coach` tuple; live HTTPS and the
  new route returned 200.

## 2026-08-16 — Reframe-to-Reframe MIDI2 peer capability projection

- Add the first non-command system-capability page: `reframe.midi2.software_peer_projection`.
- Link the typed runtime scenario, sanitized evidence record, three governing MIDI2 chapters, and the visible `MIDI2 peers` projection.
- Keep the command atlas unchanged: `storify.source.start` is the exercised existing operation, not a new `/midi2` command.
- Preserve the boundary between software-peer acceptance and physical hardware interoperability; do not change the release allow-list.
- Validate all routes, internal links, navigation/menu semantics, footer consistency, mobile menu state, and desktop/mobile VRT before deployment.

### Acceptance record

- Local preview: `http://127.0.0.1:4173/`; Google Chrome via CDP, with capability-route AX and VRT checks.
- Deterministic prepublish: `--check-external --strict` passed with 0 errors and 0 warnings.
- AX: capability page exposed a unique `h1`, `Breadcrumb`, `Primary navigation`, six named navigation links, a
  `Menu` → `Close` state transition with `aria-expanded`, evidence alt text, and an eight-link consistent footer.
- VRT: desktop 1440×1000 and mobile menu-open 390×844 captures are under
  `site/evidence/vrt/local-cdp-20260816/`; the desktop capture was visually reviewed.
- Route and interlink checks passed for the homepage, E2E coverage page, capability page, evidence image, governance
  links, related records, and release boundary. The command atlas remains unchanged.
- Publication source evidence: `Fountain-Coach/midi2-gpu-fabric@cbf31bdb`; no release allow-list change.

### Deployment record

- Book commit `c9c022c` was pushed to `Fountain-Coach/book-of-reframe@main` and deployed through the fixed
  `book.fountain.coach` publication tuple.
- Live HTTPS returned 200 for `/`, `/scenarios/`, `/capabilities/reframe-to-reframe-peer-projection/`, and the peer
  evidence image.
- Live Chrome CDP repeated the capability-route AX/menu/footer checks successfully. The release surface remains
  `no-released-build` with an empty allow-list.

## 2026-08-16 — finalized scenario development cycle

- Published the sanitized `scenarioKind` projection and linked Governance Chapter 73 from the E2E page, homepage, and
  machine-readable coverage manifest.
- Confirmed the canonical authority split: executable YAML stays in the integration repository; the Book remains a
  public/maintainer projection; no separate scenario repository is introduced.
- Source governance: `Reframe-Refactoring@0e42b7d`; synchronized integration: `midi2-gpu-fabric@cb2cf559`.
- Final Book projection and deployed site revision: `book-of-reframe@84bff9f`.

## 2026-08-15 — `/commands` scenario reconciliation

- Resolved `commands-discover` through the cross-repository status gate; integration, Book coverage, and capability
  atlas now agree on `live-accepted`.
- Ran the executable scenario three times in one fresh managed Store. Each run reached `app.commands.discover`
  `succeeded`; independent AX evidence observed the result and CoreGraphics capture bound the 1920×1050 Reframe
  window.
- Published sanitized scenario evidence at `evidence/2026-08-15/commands-scenario-live.md` with its own GUI snapshot;
  legacy Ulysses catalog evidence remains historical.
- Local Google Chrome CDP AX/VRT passed home, `/commands/commands/`, and `/scenarios/`; strict prepublication with
  external canonical-host checking passed with 0 errors and 0 warnings.

## 2026-08-15 — `/threads` scenario reconciliation

- Resolved the cross-repository drift: the executable `threads` scenario and successful live authorities now promote
  the public `/threads` projection from draft to `live-accepted` for the slash origin only.
- Added sanitized evidence with the command's own window-ID capture; raw Store paths, identifiers, and manuscript
  material remain out of the public projection. The older 2026-08-03/04 records remain historical legacy evidence.
- Updated the coverage manifest, capability atlas, release snapshot, command page, scenario matrix, and generated site
  status to three live-accepted capabilities.
- Pending boundary: natural-language origin parity and never-read acceptance.
- Published as Book commit `d8fb20a` and deployed to `book.fountain.coach` from the dedicated publication root; live
  HTTP verification returned 200 for the home and command routes.

## 2026-08-15 — public reference and maintainer projection

- Keep `book.fountain.coach` as the public human reference for scenario discovery, evidence vocabulary, statuses, and
  the maintainer request loop.
- Define a future role-gated maintainer snapshot from the same reviewed Book commit and digest; it may add internal
  procedure references but cannot authorize execution or enter writer-facing retrieval.
- Link the public explanation to governance Chapter 69 and keep the public registry explicit about the snapshot being
  specified but not yet runtime-ingested.
- Validate the public projection with FCIS-AX/VRT and strict prepublication checks; do not claim maintainer ingestion
  until a separate role-boundary and provenance gate exists.
- The public scenario reference names `reframe-scenario-work-session` as the Codex-facing development entry point;
  deployment and release promotion remain separate scopes.

## 2026-08-15 — internal E2E capability publication gate

- Local preview: `http://127.0.0.1:4173/`, Google Chrome via the bundled CDP runner.
- AX/VRT acceptance passed for `/`, `/commands/commands/`, and `/scenarios/`; the drive asserted landmarks,
  navigation/menu state, skip-link focus, command metadata, breadcrumb, evidence alt text, related records, and the
  scenario-page heading and coverage grid.
- VRT captures: `site/evidence/vrt/local-cdp/home-desktop-light-1440x1000.png`,
  `home-mobile-light-390x844.png`, `home-mobile-menu-open-light-390x844.png`, and
  `scenarios-desktop-light-1440x1000.png`.
- Generated-data and strict prepublication scan passed with 0 errors and 1 expected canonical-host warning.
- The public projection adds the maintainer-only `reframe.e2e.scenario.run` registry contract; it publishes no raw
  runtime, Store, manuscript, credential, or deployment data.
- Deployment completed from Book commit `64157a8`; HTTPS 200 verified for `/`, `/scenarios/`, and
  `/commands/commands/`, with the new capability marker present on `/scenarios/`.

## 2026-08-15 — governed E2E scenario infrastructure

- Make the Book an integral projection of Reframe's reusable E2E live-drive scenarios, with the governing doctrine
  authored first in Reframe-Refactoring and mirrored into the integration repository.
- Add a Book site section that explains scenario contracts, AX/window-ID/FountainStore evidence, paid-lane consent,
  state-based waits, provenance, and the difference between command inventory, capability acceptance, and release.
- Create a coverage manifest that pins every currently published command page to a scenario identity: `/commands`,
  `/ground`, `/pipeline status`, `/readings`, and `/threads`.
- Import existing evidence into the scenario format where possible; mark slash-only, partial, unavailable, or
  origin-parity gaps explicitly. Do not upgrade claims merely because a page already exists.
- Require every future command page to link to its scenario and every scenario to link back to the governing chapter
  and runtime evidence. The first new target is `/storify! source auto` → `/world`, with source import as a mandatory
  setup step.
- Keep the public projection sanitized: no manuscript text, private FountainStore data, credentials, deployment
  details, or raw internal identifiers.

### Planned validation and publication gates

- Governance validator and docs parity check pass for the new chapter and mirrored reading index.
- Scenario schema/runner tests pass, including missing-prerequisite, confirmation, timeout, failed-terminal, and
  evidence-binding cases.
- Every published page has a scenario coverage row and an honest status.
- Book site local preview, browser AX/VRT acceptance, generated-data checks, strict prepublish scan, and deployment
  verification pass before publication.

## 2026-08-03 — public/private publication policy

- Replace misleading public-facing runtime links with an explicit private-runtime access note.
- Publish `PUBLICATION-POLICY.md` and link the public governance Chapter 44.
- Keep the Book limited to reviewed command/capability projections, release boundaries, provenance, and AX/VRT proof.
- Validate public links, route metadata, FCIS-AX/VRT site acceptance, and `git diff --check`.
- Review order: org FCIS PR #4, governance PR #7, runtime PR #21, then Book PR #9.

## 2026-08-03 — technical introduction

- Add a concise “What is Reframe?” overview to the public site without changing the evidence or release boundary.
- Explain purpose, system boundary, and reader contract in corporate technical-document language.
- Validate responsive navigation, AX semantics, fixed-viewport VRT, route delivery, and reload workflow.

## 2026-08-03 — first verified Book of Reframe snapshot

- Import the live `/commands` catalog from `app.commands.discover`.
- Separate command-entry count from governed capability count.
- Publish a writer-facing atlas and a machine-shaped evidence projection.
- Link the publication back to the runtime and governance repositories.

Completion requires the source runtime proof, sanitized evidence, and reciprocal links to remain together.

## 2026-08-03 — named release-surface boundary

- Separate the development command inventory from governed capabilities, live acceptance, and a named-build release
  allow-list.
- Publish the sanitized release manifest and state explicitly that no released App surface is currently recorded.
- Do not populate the allow-list from `/commands`, screenshots, `main`, or executable-but-unaccepted registry rows.

## 2026-08-03 — canonical web publishing

- Provide stable command URLs with Facebook/Open Graph metadata and the command snapshot as the social image.
- Deploy the static `site/` projection through GitHub Pages; keep a custom `CNAME` unset until the domain is chosen.
- Keep Facebook posting as a separate explicit action that shares the canonical site URL.

## 2026-08-03 — FCIS command pages and visual evidence

- Add one writer-facing document per published command, with the GUI snapshot as its first non-empty line.
- Require a governed live drive to reach the command's execution/result state, then join AX, window-ID capture, and
  persisted proof before publication.
- Add FCIS RFC 0001 audit/plan files and keep the Codex/Claude maintenance skill copies identical.
- Publish only commands with evidence; retain the complete catalog and a pending inventory for commands not yet
  driven. Never use the existing catalog screenshot as proof for another command.

## 2026-08-03 — repository-derived web projection

- Replace the lorem-ipsum responsive specimen with a neutral, GitHub-like projection of `README.md`,
  `COMMAND-ATLAS.md`, `CAPABILITY-ATLAS.md`, `RELEASE-SURFACE.md`, and `SOURCE.md`.
- Keep command inventory, governed capability status, live evidence, and release status visibly separate.
- Give the `/commands` route the same publication shell, typography, metadata, and evidence/status vocabulary as the
  overview page.
- Validate routes, metadata, FCIS-AX semantics, fixed desktop/mobile VRT, and local reload behavior.

## 2026-08-03 — bilingual legal publication surface

- Record the publisher, contact, purpose, ownership, AI-assistance, hosting, logging, privacy, and accessibility
  facts supplied by Benedikt Eickhoff.
- Publish bilingual legal, privacy, accessibility, copyright, and compliance routes inside the Book site, with the
  compliance route exposing the current decision rather than hiding it.
- Keep GDPR, AI Act transparency, and hosting/security as `requires_review` until qualified review and enforceable
  evidence exist; do not convert a self-attestation into a legal clearance. This was resolved by the publisher review
  wizard on 2026-08-03 and is recorded in the register with explicit scope limits.
- Correct canonical-host and Open Graph metadata to use `https://book.fountain.coach/`.
- Validate generated data, strict European compliance, strict prepublication scanning, internal routes, metadata,
  FCIS-AX/VRT acceptance, and `git diff --check` before any deployment decision.

## 2026-08-03 — no-go closure work

- **Chapters read:** 07 planning discipline and validation behavior; 08 persisted/evidence authorities and acceptance;
  43 rules 1–7 (named-build/release boundary); 44 rules 1–6 (reviewed public projection/private implementation).
- **What they forbid here:** treating the command catalog, screenshots, or a green technical scan as a released App or
  as legal clearance; publishing private runtime material; silently converting a declared policy into an observed fact.
- **Conflicts:** none. The request to reach GO is bounded by the compliance skill's rule that `requires_review` is a
  blocker and that automation is not legal certification.
- **Excluded, and why:** qualified GDPR/AI Act classification and Member-State review are not invented here; raw server
  logs, credentials, and unrestricted infrastructure configuration remain excluded by Chapter 44.
- **Evidence update:** the live audit verified DNS/HTTPS/Caddy/root. The guarded retention operation now verifies
  `MaxRetentionSec=3day`; applying it reduced journal usage from 3.7 GB to 91.5 MB. Hosting remains `requires_review`
  for access, backup/rollback, incident ownership, and processor review.
- **Current gate:** rerun the strict European compliance and prepublication scans after recording the publisher
  decisions. Local legal routes and FCIS-AX/VRT acceptance pass; GO remains limited to the recorded scope.

## 2026-08-03 — production publication

- Prepublish scan: `GO`, 0 errors, 0 warnings; FCIS-AX/VRT acceptance passed through Chrome CDP.
- Deployment: reviewed `site/` synchronized to the dedicated `/var/www/book-of-reframe` root on `book.fountain.coach`;
  local-only `dev-server.py` and `open-local-preview.sh` were excluded.
- Live verification: `/`, `/legal/`, `/privacy/`, `/accessibility/`, `/copyright/`, `/compliance/`, and
  `/commands/commands/` returned HTTP 200; canonical host and scoped GO status were confirmed.
- Production permissions: `caddy:caddy`, directories `755`, files `644`. Source and evidence remain in GitHub; no
  named released App build is claimed.

## 2026-08-03 — Facebook preview optimization

- Added the official public Fountain Coach organization avatar as a local brand asset and structured publisher logo.
- Added Facebook/Twitter metadata, accurate preview-image dimensions, favicon/touch icon links, and a typed homepage
  publisher record.
- Built a reversible `/commands` Facebook package from its own live-accepted GUI snapshot; `externalPublish: false`.
- Verified with a `facebookexternalhit/1.1` probe that homepage and command metadata, canonical URLs, preview image,
  logo asset, and HTTP 200 delivery are visible on the live host. No external post was created.

## 2026-08-03 — iPhone sticker asset

- Created a transparent 1254×1254 emoji-style Fountain Coach mark from the official logo, with transparent corners and
  thick small-size strokes.
- Added the downloadable `/sticker/` route and instructions for saving the PNG to Photos and choosing **Add Sticker**.
- This is an iPhone keyboard sticker/Genmoji-adjacent asset, not a new Unicode character.

## 2026-08-03 — sticker correction

- Replaced the first sticker rendering because the fountain/spring was not sufficiently readable.
- Corrected asset preserves the open hand plus the central fountain jet and four curved side jets; RGBA corners remain
  transparent.
- iOS subject detection still separated the floating spring from the hand. The final correction adds one contiguous
  white sticker backing around the complete hand-and-fountain silhouette so Photos selects the entire mark as one
  sticker subject.

## 2026-08-03 — next command: `/pipeline status`

- Goal: publish a writer-facing command page only after a fresh live drive reaches the pipeline-status result.
- Scope: integration live drive, AX/window-ID/FountainStore evidence, sanitized command snapshot, `commands/pipeline-status.md`,
  and the command-page index/projection if evidence passes.
- Non-goals: no runtime change, no release-surface promotion, no claim that the development command is shipped.
- Authority: capability `pipeline.status`, native operation `showPipelineStatus`, existing live-accepted evidence in
  `evidence/2026-08-03/copilot-capability-closure.json`; this phase adds command-specific visual proof.
- Validation: governed fresh-store drive, AX result inspection, `ReframeStoreDump` proof, window-ID screenshot review,
  command-page verification, site acceptance, strict prepublish scan, and `git diff --check`.

### Completion record

- Live drive completed on a tiny managed fixture, not the local FountainStore library.
- Three `/pipeline status` runs persisted as complete `requested → accepted → running → succeeded` lifecycles.
- Added the command page, sanitized live evidence, own GUI snapshot, command index link, and stable site route
  `/commands/pipeline-status/`.
- No runtime or release-surface change was made; the page remains explicitly development evidence.
- Local site acceptance: Google Chrome via CDP passed home and `/commands/commands/` AX/VRT checks; the new route and
  image/metadata returned HTTP 200. Strict prepublish scan with `--check-external`: 0 errors, 0 warnings.
- Publication: commit `5b0d155` synchronized to `/var/www/book-of-reframe`; HTTPS route and image verified `200`,
  local preview launchers verified absent (`404`), and deployed permissions verified as `caddy:caddy`, directories
  `755`, files `644`.

# Full-fidelity owned `/threads` evidence and Courier reading hierarchy — 2026-08-04

- Re-run `/threads` against the Polyxsupershow sixth-draft managed store after the Copilot typography change.
- Make Copilot Courier prose smaller than atoms, keep interface labels system-font, add bullets/space to listings, and
  disclose the uncertainty score/lane rack by default.
- Publish the actual window-ID capture only after recording the publisher's ownership, exact public scope, and review
  for personal data, third-party material, credentials, and secrets. Do not obfuscate owned manuscript evidence when
  the purpose is to illustrate the real product surface.
- Visual proof: `evidence/2026-08-04/threads-live-polyx-courier-20260804.png`; AX proof includes the uncertainty band,
  both producer lanes, shared map viewport, result row, and terminal activity. Behavioral proof is the persisted
  `requested → accepted → running → succeeded` lifecycle in `evidence/2026-08-04/verified-threads.md`.
- Prepublish: site data regenerated; strict scan completed with 0 errors. The compliance register review date was
  refreshed to 2026-08-04; canonical-host reachability remains the deployment gate.
# European publication compliance gate — 2026-08-03

**Goal:** Require a documented European regulatory applicability decision before the Book can be called publishable.

**Result:** Added `COMPLIANCE.md` and `compliance/register.yaml`; unresolved GDPR, AI Act, accessibility, copyright,
and hosting/security decisions intentionally produce `NO-GO` until reviewed.

**Validation:** The integration prepublish scan invokes the European compliance gate; the standalone gate output is
recorded below after execution.

**Demo result:** `NO-GO` — 8 requirements registered, 5 require review: GDPR, AI Act transparency, accessibility,
copyright, and hosting/security. Existing technical warnings remain: canonical host reachability and missing LICENSE.

**Implementation pass:** Added `LEGAL-NOTICES.md`, `COPYRIGHT.md`, `ACCESSIBILITY.md`, `LICENSE`, visible site links,
and explicit reduced-motion/high-contrast/44px control safeguards. Local Chrome CDP AX/VRT passed. Publication remains
NO-GO until the five register decisions and the live canonical host are resolved.

**Infrastructure and asset pass:** The read-only server audit found no active custom-domain DNS or Book deployment root.
The command evidence image was sanitized to remove manuscript-reading content and its public caption/alt text now says
so. AX/VRT was rerun successfully. DNS, deployment, production logging, and rights/legal decisions remain explicit
release gates.

**Deployment:** The isolated Book root and Caddy site block are now installed on the publishing server. HTTPS cannot
complete until the `book.fountain.coach` DNS record exists; no public release claim is made before that verification.

# Paid-first runtime reconciliation and Book projection — 2026-08-15

**Goal:** update the Book from the current governed runtime snapshot while preserving the explicit no-released-build
boundary.

**Source:** integration `midi2-gpu-fabric` at `ef756360`; registry, generated audit, release manifest, governance
Chapter 37/43/51, live evidence, and current command/runtime history.

**Publication target:** refreshed capability and command projections, release surface, site data, paid-lane policy,
and provenance in `SOURCE.md`.

**Excluded:** no runtime source, private FountainStore data, unowned manuscript material, or unaccepted command is
published; `world.reference.research` is a next acceptance target, not a completed command; no release allow-list is
created.

**Governance record:** Chapter 37 is being corrected upstream because its census and guide workflow are stale;
Chapter 43 keeps the release status at `no-released-build`; Chapter 51 makes paid availability the default election,
with local-only as the explicit override. The Book will describe policy separately from live acceptance.

**Evidence:** the existing 2026-08-09 Circe evidence remains accurately described as an on-device instruction with no
paid call recorded. The isolated 2026-08-15 Romeo-and-Juliet DraCor drive is not promoted as Book evidence until the
registry identity and rights/scope review are reconciled.

**Validation:** regenerate site data, run capability/release/governance/docs-sync checks, run local route and metadata
checks, run Book AX/VRT acceptance where available, and pass the strict prepublish scan with external checks.

**Validation record:** site data regenerated from `evidence/2026-08-15/reframe-release-surface.json`; release validator
passed; local route/metadata scan passed with 0 errors using an isolated PyYAML environment. The bundled Chrome CDP
acceptance runner could not obtain a dedicated CDP endpoint, so browser AX/VRT evidence is not claimed in this phase.
External references to the new GitHub paths remain pending until this commit is pushed; the canonical host remains the
publication gate.

## 2026-08-15 — reconcile `/ground` after contract enforcement

- Integration `1784e067` now validates typed setup entries for every scenario and provides the reusable managed-Store
  preparation executor. The `/ground` contract is executable and has been prepared against a fresh Store; no live
  acceptance claim is made until Storify, `/ground`, AX, window-ID, and Store evidence agree.
- Governance source `Reframe-Refactoring@9b733c3` adds the explicit rule that the complete scenario is written before
implementation and that prose-only setup cannot become executable.

### Complete existing scenario contracts

- The integration now carries canonical YAML contracts for all six existing scenario identities, with validator-enforced
  parity against the JSON runtime projections. This is contract authoring only; legacy live evidence remains historical
until each current prerequisite chain and independent witness are rerun.

### Reconcile `/readings` contract

- `readings-comparison` now declares source preparation and two explicit Storify reading terminal receipts before the
  comparison. It is executable but remains pending current AX, window-ID, and FountainStore acceptance.

## 2026-08-15 — governed E2E scenario implementation record

- Governance Chapter 68 is authored in the authoritative Reframe-Refactoring checkout and synchronized into the
  integration copy; remote parity remains pending the governance publication commit.
- Added five draft scenario contracts and a coverage manifest for every existing command page. Legacy evidence is
  explicitly retained as legacy and is not promoted to new scenario acceptance.
- Added the public `E2E-SCENARIOS.md` projection and `/scenarios/` site route, with links from the site home and every
  command page.
- Scenario validation passed: 6 scenarios / 6 command identities, including the upcoming `/world` prerequisite
  chain. Command-page validation passed for all 5 published pages.
- Local strict prepublish scan passed with 0 errors and 1 canonical-host warning. Chrome CDP site acceptance passed for
  the home, commands, and scenarios routes; screenshots were captured under `/tmp/book-e2e-acceptance-final.JZCUJA/`.
- No scenario has yet been promoted to `live-accepted` by the new runner; the next tranche must execute the inventory
  and replace each `draft` row only after same-run AX/Store/window-ID proof.

### `/pipeline status` reconciliation — 2026-08-15

- Promoted `pipeline-status` to `live-accepted` after three governed runner repetitions on source revision
  `55461f0f`.
- AX, FountainStore, and the external-display window-ID capture agreed: `PIPELINE STATUS` appeared and each run
  persisted `requested → accepted → running → succeeded` for `pipeline.status` without a draft mutation.
- The public page and sanitized evidence were refreshed with the honest empty-active-manuscript result; the prior
  2026-08-03 evidence remains historical legacy evidence.
- Scenario validation passed (6/6); site AX/VRT passed; strict prepublish with external checks passed with 0 errors
  and 0 warnings after the transient GitHub timeout cleared.

### `/readings` scenario reconciliation — 2026-08-15

- The current typed `readings-comparison` contract was executed against the small original fixture corpus so the
  publication witness is bounded and repeatable; the older Ulysses drive remains historical product evidence.
- The runner was corrected to require a new lifecycle execution UUID for each repeated reading. The final witness
  bound PID `69337`, window ID `58927`, the managed Store, executable, and integration source commit `94a7b327`.
- Two paid ChatGPT-plan Storify executions reached `succeeded`, and `/readings` reached both AX and Store terminal
  checks. The sanitized current record is `evidence/2026-08-15/verified-readings-scenario.md`.
- Public Book commit `3c34b9d` promotes `/readings` to `live-accepted`; release status remains `no-released-build`.
- Static site commit `12bc941` was deployed to the fixed `book.fountain.coach` publication tuple; HTTPS verification
  returned 200 for `/`, `/commands/commands/`, `/commands/ground/`, and `/commands/readings/`.
- Local Chrome CDP acceptance passed for the home and scenarios routes with desktop, mobile, and menu-open captures;
  the first attempt failed only because the dedicated CDP endpoint was not yet serving, then passed after the existing
  local preview was confirmed.
