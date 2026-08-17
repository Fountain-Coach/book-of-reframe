# Publication provenance

## Snapshot: Governance Chapter 79 — default semantic manuscript projection — 2026-08-17

- Governance source: `Fountain-Coach/Reframe-Refactoring@1cbe5f2`.
- Integration source: private `Fountain-Coach/midi2-gpu-fabric@03302ce2`.
- Public projection: `GOVERNANCE-79.md` and `/governance/default-semantic-manuscript-projection/`.
- Signature illustration: `site/assets/reframe-default-semantic-workspace.jpg`; design reference only, with no runtime,
  AX, FountainStore, visual-regression, live-acceptance, or release claim.
- Claim boundary: public governance explanation only; Questions, Movements, Read coverage, Copilot, and MIDI2 peer
  presentation are described without promoting an implementation or released App surface.
- Deterministic prepublication: strict scan passed with 0 errors and 0 warnings, including external canonical-host
  checks. Local route and image asset returned successfully.
- Browser acceptance: the bundled Chrome CDP runner could not start because no dedicated CDP browser was available;
  AX/VRT acceptance remains explicitly unestablished and is not claimed here.
- Publication commit: pending.

## Snapshot: public Scenario-Driven Development method — 2026-08-17

- Runtime and scenario infrastructure source: private `Fountain-Coach/midi2-gpu-fabric@add3acec`.
- Governance source: public `Fountain-Coach/Reframe-Refactoring@e3068dc`, Chapter 78 and its reading-index entry.
- Public reusable kit: `Fountain-Coach/FountainScenarioKit@ec3a06c`; `v0.1.1` remains the Reframe consumer dependency,
  while this newer main commit updates public README/compliance presentation.
- Projection: `SCENARIO-DRIVEN-DEVELOPMENT.md`, `E2E-SCENARIOS.md`, and `/scenario-driven-development/`.
- Claim boundary: public method and package explanation only. No private runtime source, Store data, manuscript,
  credentials, deployment details, or hardware-interoperability claim is published.
- Acceptance: local deterministic prepublish passed with 0 errors and 1 canonical-host warning; Chrome CDP AX/VRT
  checks passed for the homepage, scenarios index, new method route, and linked capability page. The external scan
  reached all content checks but one GitHub URL timed out; deployment and live-host verification remain separate.
- Publication: `Fountain-Coach/book-of-reframe@9946725`.
- Deployment: the reviewed `site/` projection from `book-of-reframe@19d7735` was synchronized to the fixed
  `book.fountain.coach` publication root. Live HTTPS returned 200 for `/`, `/commands/commands/`, `/commands/ground/`,
  `/commands/readings/`, `/scenario-driven-development/`, `/scenarios/`, and the MIDI2 capability page.

## Snapshot: `/commands` scenario reconciliation — 2026-08-15

- Scenario: `commands-discover`; capability: `app.commands.discover`; status: `live-accepted`.
- Runtime source commit: `Fountain-Coach/midi2-gpu-fabric@cefee09c`.
- Three isolated slash-origin runs reached terminal `succeeded` in one fresh managed Store; private receipt IDs and
  process identifiers remain outside this public projection.
- Independent witness: AX result surface plus CoreGraphics window-ID capture at 1920×1050; public snapshot is
  `evidence/2026-08-15/commands-scenario-live-20260815.png`.
- Current result projection: 82 available, 5 unavailable, and 3 compatibility-only entries; the older 95-entry
  Ulysses inventory remains historical evidence, not proof for this scenario.
- Resolver classification: `consistent`; no Book/runtime/capability status drift remains for this scenario.

## Snapshot: `/threads` scenario reconciliation — 2026-08-15

- Scenario: `threads`; capability: `manuscript.reading.inspect`; status: `live-accepted` for the slash origin only.
- Runtime source commit: `Fountain-Coach/midi2-gpu-fabric@6ba5e2f1`.
- One isolated governed run reached terminal `succeeded`; AX exposed `story-uncertainty-band`, FountainStore recorded
  the capability lifecycle, and the external-display window-ID capture showed the matching terminal result.
- Public snapshot: `evidence/2026-08-15/threads-live-20260815.png`; sanitized acceptance record:
  `evidence/2026-08-15/verified-threads.md`.
- Natural-language origin parity, the never-read case, and a released App build remain unestablished.
- Publication: Book commit `Fountain-Coach/book-of-reframe@d8fb20a`; deployed to
  `https://book.fountain.coach/` from the fixed dedicated root after strict external prepublication checks passed.

## Snapshot: scenario work session — 2026-08-15

- Development entry point: `reframe-scenario-work-session`.
- The public Book explains one bounded Codex/Reframe loop: resolve scenario, bound source slice, implement and test,
  execute in isolation, independently witness, and report one work card.
- Runtime source/governance integration commit: `Fountain-Coach/midi2-gpu-fabric@cefee09c`.
- Governance: Chapter 69 now treats scenario work as core source development/operator work; deployment and release
  promotion remain separate scopes.

## Snapshot: public reference and maintainer projection — 2026-08-15

- The public Book remains the canonical human reference at `https://book.fountain.coach/`.
- `scenarios/registry.json` documents the future maintainer snapshot boundary: same reviewed Book commit and digest,
  role `maintainer`, no writer-facing retrieval, and runtime ingestion not yet enabled.
- Governance: Chapter 68 defines the scenario publication unit; Chapter 69 defines the public/maintainer dual
  projection and preserves runtime, Store, and independent witness authority.

## Snapshot: internal E2E capability publication gate — 2026-08-15

- Machine-readable projection: `scenarios/registry.json` declares the maintainer-only
  `reframe.e2e.scenario.run` contract, fresh-store default, independent-witness requirement, and no-self-approval
  rule.
- Runtime source commit: `Fountain-Coach/midi2-gpu-fabric@21d89b28`.
- Human-readable projection: `E2E-SCENARIOS.md` and `/scenarios/` explain the internal behavioral receipt versus the
  independent Live Drive AX/CoreGraphics/VRT witness.
- Local acceptance: Google Chrome via CDP passed `/`, `/commands/commands/`, and `/scenarios/` at
  `http://127.0.0.1:4173/`; screenshots are under `site/evidence/vrt/local-cdp/`.
- Strict prepublication scan: 0 errors, 1 expected warning that the canonical host was not externally checked in the
  local gate.
- Publication boundary: the Book contains only sanitized contract and evidence vocabulary; no private runtime or
  Store data is included.

### Deployment

- Published commit: `Fountain-Coach/book-of-reframe@64157a8`.
- Deployment tuple: `book.fountain.coach` → `65.109.14.71` → `/var/www/book-of-reframe`; DNS and Caddy were not
  changed.
- Live verification: `/`, `/scenarios/`, and `/commands/commands/` returned HTTPS 200; `/scenarios/` contained the
  `reframe.e2e.scenario.run` capability marker.

This book is published from the integration repository:

- Runtime and registry: private `Fountain-Coach/midi2-gpu-fabric` (access required; not a public source link)
- Governance and agent practice: https://github.com/Fountain-Coach/Reframe-Refactoring
- Publication boundary: [PUBLICATION-POLICY.md](PUBLICATION-POLICY.md) and [governance Chapter 44](https://github.com/Fountain-Coach/Reframe-Refactoring/blob/main/docs/44-publication-and-source-policy.md)
- Policy PRs: org FCIS [#4](https://github.com/Fountain-Coach/.github/pull/4), governance
  [#7](https://github.com/Fountain-Coach/Reframe-Refactoring/pull/7), runtime
  [#21](https://github.com/Fountain-Coach/midi2-gpu-fabric/pull/21), and this Book projection
  [#9](https://github.com/Fountain-Coach/book-of-reframe/pull/9).
- Maintenance skill: `midi2-gpu-fabric/.codex/skills/book-of-reframe-maintenance`

## Snapshot: governed E2E scenario projection — 2026-08-15

- Governance: Chapter 68, “The Reframe E2E Scenario Is the Publication Unit”.
- Runtime scenario source: `Fountain-Coach/midi2-gpu-fabric/apps/modernization-studio/LiveScenarios/`.
- Coverage: five draft contracts for the published commands plus the upcoming `world-after-storify` prerequisite
  scenario for `/world`.
- Validation: 6 scenarios / 6 command identities and all 5 command pages pass deterministic validation; Chrome via CDP passed
  the home, `/commands/commands/`, and `/scenarios/` routes; strict prepublish passed with 0 errors and 1 canonical-
  host warning.
- Boundary: legacy screenshots and records remain linked but are not new scenario acceptance. No private Store data,
  prompts, manuscript text, secrets, or released App capability is published.

## Snapshot: 2026-08-03

- Source runtime store: fresh managed integration store; sanitized projection is retained in `evidence/2026-08-03/`
- Capability: `app.commands.discover`
- Proof source: `copilot:capability:reframe-ulysses:c42a180c-7990-4f44-ae4b-373855daf323`
- Runtime count: 95 command entries, 92 available, 3 unavailable, 3 `//`-only within the available count
- Publication projection: `COMMAND-ATLAS.md` and `evidence/2026-08-03/verified-command-catalog.md`
- Individually documented command: [`/pipeline status`](commands/pipeline-status.md), with three repeated fixture
  runs, AX result semantics, CoreGraphics window-ID capture, and persisted FountainStore proof in
  `evidence/2026-08-03/verified-pipeline-status.md`.
- Individually documented command: [`/threads`](commands/threads.md), with a fresh fixture run, AX result semantics,
  CoreGraphics window-ID capture, and persisted FountainStore proof in `evidence/2026-08-03/verified-threads.md`.
  This proves the slash-command origin only; the broader capability closure remains pending origin-parity acceptance.
- Release boundary: `RELEASE-SURFACE.md` and `evidence/2026-08-03/reframe-release-surface.json`; current status is
  `no-released-build` with an empty capability allow-list.
- Social publication procedure: mirrored `book-of-reframe-social-publish` skill; packages are local review artifacts
  until an explicitly authorized Facebook post is returned by the platform.
- Social preview: the official Fountain Coach organization avatar is vendored as `site/assets/fountain-coach-logo.png`
  from the public GitHub organization profile; homepage and command routes expose Facebook/Twitter metadata while
  command pages retain their own live-drive snapshot as the preview image.
- iPhone sticker: `site/assets/fountain-coach-sticker.png` is a transparent, small-size emoji-style rendering of the
  mark; `/sticker/` explains how to add it to the iPhone keyboard sticker drawer.
- Canonical web projection: `site/`, published at `https://book.fountain.coach/` after DNS and HTTPS verification on
  2026-08-03. GitHub remains the source and provenance record; the custom host is the canonical reader destination.

The local temporary store path is provenance for the generating workspace only; it is not a public dependency. The
sanitized catalog and screenshot in `evidence/2026-08-03/` are the publication evidence.

## Snapshot: 2026-08-15 — paid-first governance reconciliation

- Source runtime: private `Fountain-Coach/midi2-gpu-fabric`, commit `767f75ec0d969313586c55a75b6b9c10a054af9d`.
- Governance correction: Chapter 37 now reports the generated 55-identity boundary (24 executable, 31 unavailable)
  and no longer teaches the retired Manuscript Guide as a current Copilot offer. The scoped runtime guide now records
  paid availability as the default writer-facing lane election, with explicit local-only override.
- Release boundary: `evidence/2026-08-15/reframe-release-surface.json` remains `no-released-build` with an empty
  capability allow-list. The 95/92/3 command inventory remains the last separately verified command-catalog snapshot;
  it is not promoted to a new live command acceptance claim here.
- Capability projection: the Book now records 55 identities, 24 executable, 31 unavailable, and 2 live-accepted
  (`app.commands.discover` and `pipeline.status`). New executable-but-unaccepted rows are listed without claiming
  completion.
- Paid-lane policy: [`LANE-POLICY.md`](LANE-POLICY.md) explains paid-first election, bounded on-device delegation,
  local-only override, and the distinction between policy, executable status, live acceptance, and release.
- Evidence boundary: the isolated DraCor import drive and its screenshot remain unpromoted because the registry still
  marks `screenplay.source.import` unavailable and its public rights/scope review is not recorded in this snapshot.
- Next acceptance target: `world.reference.research`, because its registry policy explicitly requires a paid answering
  lane; it is not yet a published or live-accepted command.
- Publication commit: `Fountain-Coach/book-of-reframe@6c78d8d`.
- Validation: release validator passed; local strict prepublish scan passed with 0 errors and 1 canonical-host warning
  (external check deferred until the new paths are pushed). The bundled Chrome CDP runner could not obtain a dedicated
  CDP endpoint, so no new browser AX/VRT evidence is claimed.

### Deployment: 2026-08-15

- Reviewed `site/` deployed with `secure-publishing/scripts/deploy_book_site.sh --apply --confirm-deploy`.
- Tuple: `book.fountain.coach` → `65.109.14.71` → `/var/www/book-of-reframe`; DNS and Caddy were not changed.
- Live verification: `/`, `/commands/commands/`, `/commands/ground/`, and `/commands/readings/` returned HTTPS 200.
- Content verification: the live homepage reports snapshot `2026-08-15`, 55 capability identities, 24 executable, 31
  unavailable, 2 live-accepted, and the paid-first routing section. Local-only preview tooling was not deployed.

## Snapshot: 2026-08-04 — `/threads` full-fidelity owned evidence

- Owned source: Thepolyxsupershow 6th Draft Source, publisher-declared copyright/possession of Benedikt Eickhoff.
- Scope: one read-only `/threads` GUI result, including the open uncertainty score/lane rack and Courier Copilot
  result; no raw FountainStore documents or private runtime implementation are published.
- Review: publisher declared no personal data, third-party material, credentials, or secrets in the captured scope.
- Visual evidence: `evidence/2026-08-04/threads-live-polyx-courier-20260804.png`.
- AX evidence: `story-uncertainty-band`, `uncertainty-lane-storifyStructure`,
  `uncertainty-lane-storifyOpenQuestions`, `uncertainty-map-viewport`, `chat-row-message-*`, and
  `copilot-capability-activity`.
- Behavioral evidence: `evidence/2026-08-04/verified-threads.md`; lifecycle
  `copilot:capability-event:fixture:e4125a02-2b1c-4b5b-a15c-9ba070574fb2`, requested → accepted → running →
  succeeded.

The 2026-08-04 image is intentionally full fidelity. The publication policy requires a rights/scope review, not
automatic obfuscation, when the publisher owns the manuscript and the purpose is to illustrate the actual product.
Publication commit: `bfb3a2431e2f4556525efea1b3e85fa6a38bac8e` (merged PR #12).

The command-page contract is snapshot-gated: each completed page begins with its own live-drive GUI image, with AX
and FountainStore evidence recorded alongside it. The catalog screenshot is not reused as command proof.

The local site acceptance pass for the preceding publication used Google Chrome via CDP at `http://127.0.0.1:4173/`: home and
`/commands/commands/` AX/VRT checks passed, and `/commands/pipeline-status/` returned HTTP 200 with its canonical,
Open Graph, alt-text, and evidence image metadata. The strict prepublish scan passed with `--check-external` (0 errors,
0 warnings). Publication commit `5b0d155` was synchronized to `/var/www/book-of-reframe`; the new route and image
now return HTTPS `200` from the canonical host. Local-only preview launchers remain excluded.

## Snapshot: 2026-08-09 — `/ground` and `/readings` on Ulysses, episode 15 (Circe)

- Source runtime: private `Fountain-Coach/midi2-gpu-fabric`, source commit `7fb9f794`, SPM debug build
  `ReframeApp` (no distribution artifact).
- Drive store: `~/circe-book-drive.fountainstore`, a working copy of the writer's Circe drive store
  (`~/circe-flagship.fountainstore`, corpus `reframe-ulysses`), copied so the original keeps its pristine
  two-reading state as the reproducible baseline. Neither is the writer's managed library, which was not touched.
- Manuscript: James Joyce, *Ulysses*, episode 15 (Circe), lines 20051–25573. Public domain, assembled by Reframe's
  own corpus API. The publisher directed that screenshots may be published; the captured scope was reviewed and
  contains no personal data, third-party licensed material, credentials, or secrets. Images are full fidelity.
- Window: CoreGraphics window ID `42036`, bounds `127,-1080 1920x1080`, native full screen on the attached
  external display; AX-verified before capture.
- Lane: `stay on device` was sent before either command ran and the Copilot answered *"I'll keep this work on
  your device."* Only two `telemetry:llm` records and two `llm-cache` entries were written in the whole session,
  all belonging to that instruction; neither `/ground` nor `/readings` recorded a paid model call. That is a
  measured absence of paid calls, not a reading of provider state: the stored lane grant was never opened, so no
  claim is made here that the lane was switched.
- Individually documented command: [`/ground`](commands/ground.md) — capability `prep.grounding.propose`, origin
  `slash`, terminal aggregate `copilot:capability:reframe-ulysses:41e02fb6-aed9-45f7-a891-67fc9737a60c`
  (`phase=succeeded`, `grounding.proposal=false`, `grounding.changed=false`,
  `grounding.blockedBy=readingHasHoles`), AX projection `copilot-capability-activity`, persisted rounds
  `chat:reframe-ulysses:round:19` and `:21`. Evidence: `evidence/2026-08-09/verified-ground.md`. This records the
  slash origin only; the natural-language origin and the accepted-lens path remain unproven, so the capability
  stays `executable-not-live-accepted`.
- Individually documented command: [`/readings`](commands/readings.md) — local orchestration with no capability
  identity; computed from `storify:run:reframe-ulysses:stf-9512cc87` and `:stf-66e626a2` (same span, same grounding
  identity `83651a50…e008ec0a`), persisted rounds `chat:reframe-ulysses:round:20` and `:22`. Evidence:
  `evidence/2026-08-09/verified-readings.md`.
- Repetition: both commands were driven twice, on two separate launches of the same store. `/ground` reproduced
  identically; `/readings` reproduced its structural report byte-for-byte and re-reasoned its closing paragraph to
  the same conclusion.
- Release boundary unchanged: `RELEASE-SURFACE.md` remains `no-released-build` with an empty capability allow-list.
  Nothing in this snapshot enters a released surface.
- Correction recorded in this change: `COMMAND-ATLAS.md` stated the capability registry counts (53/22/2/31) as
  current. Those are the 2026-08-03 figures; the registry has since been re-audited to 49 identities, 18 available,
  31 unavailable. The atlas now dates that figure and points at `CAPABILITY-ATLAS.md` as the authority.

### Correction: 2026-08-10 — a lane claim narrowed to what was measured

This snapshot originally stated that the writer's key was turned to on-device before `/ground` and `/readings`
ran, and that the closing paragraph of the `/readings` report was reasoned on the on-device lane. Neither was
established. Both were inferred from the ABSENCE of a paid-lane telemetry record; the stored lane grant was never
read back, so the provider state at that moment is unknown.

What the store does show is unchanged and stands: `stay on device` was sent, the Copilot answered *"I'll keep this
work on your device."*, and only two `telemetry:llm` records and two `llm-cache` entries were written in the whole
session — all four belonging to that instruction, none to `/ground` or `/readings`. No paid model call was
recorded for either command.

The affected wording in `evidence/2026-08-09/verified-ground.md`,
`evidence/2026-08-09/verified-readings.md`, `commands/readings.md` and the lane line above has been narrowed to
that measured absence. No other claim in this snapshot is affected: the capability aggregate, the persisted
rounds, the AX projections and the window-ID captures were each read back from their own artifact.

### European register re-review at this snapshot

`eu_publication_gate.py --strict` initially returned **NO-GO** for this snapshot: 0 errors and 0 `requires_review`
rows, but every row in `compliance/register.yaml` was past its `review_date` of 2026-08-04, and two rows were
materially changed here:

- **copyright** — the Book now publishes public-domain third-party text (James Joyce, *Ulysses*) as evidence, a
  class the previous rationale did not cover. The reasoning is recorded in
  `compliance/evidence/asset-review-2026-08-09.md`.
- **ai-act-transparency** — the command pages publish Reframe's own generated output (Copilot replies, reading
  questions) as system-output evidence, labelled as such on each page.

The publisher instructed on 2026-08-09 that these screenshots may be published and that this snapshot should go
live. That instruction is recorded as the decision basis on the affected rows, and the next review date moved to
2026-09-09. The gate now returns **GO** within the documented scope; it remains a scope-consistency check, not a
legal certification, and the limits recorded on each row still stand.

### Publication and deployment

- Pull request [#14](https://github.com/Fountain-Coach/book-of-reframe/pull/14), merged to `main` as `e3c7d1e`.
- Deployed to `/var/www/book-of-reframe` on the publishing host (`book.fountain.coach` → `65.109.14.71`, Caddy,
  root owned `caddy:caddy`) with `secure-publishing/scripts/deploy_book_site.sh --apply --confirm-deploy`. The
  helper is scoped to that one publication tuple, plans by default, excludes the local-only preview tooling
  (`dev-server.py`, `open-local-preview.sh`), and deleted nothing. DNS, Caddy, and permissions were not changed.
- Live verification from the canonical host: `/`, `/commands/commands/`, `/commands/ground/`, and
  `/commands/readings/` return HTTPS `200`; both evidence images return `200 image/png`; canonical and `og:image`
  resolve to `book.fountain.coach`. The two new routes were driven again against the live host through Chrome CDP —
  landmarks, `h1`, breadcrumb, skip link, image alt text, and no horizontal overflow — with captures under
  `site/evidence/vrt/live-check/`.
- Pre-publication scan with `--check-external --strict`: **0 errors, 0 warnings**.

### `/pipeline status` scenario reconciliation — 2026-08-15

The `/pipeline status` Book projection is now live-accepted from the reusable `pipeline-status` scenario. Three
repetitions on integration source revision `55461f0f` agreed across AX, FountainStore, and one external-display
window-ID capture. The command remained read-only and honestly reported the empty active-manuscript state. The
sanitized record is `evidence/2026-08-15/verified-pipeline-status.md`; no private Store path or raw runtime identifiers
are published. Scenario validation passed 6/6, site AX/VRT passed, and the strict prepublish scan with external checks
passed with 0 errors and 0 warnings.

### `/readings` scenario reconciliation — 2026-08-15

The current public status is sourced from the governed `readings-comparison` scenario and its independent witness, not
from the older Ulysses screenshot alone. The witness used the original fixture corpus, proved two distinct paid-lane
reading executions by lifecycle UUID, and observed `/readings` through AX and FountainStore. Its sanitized record is
`evidence/2026-08-15/verified-readings-scenario.md`; the runtime acceptance source was `94a7b327`, and the Book
projection is `3c34b9d`. No private Store path, raw export, runtime source, or release capability is published.

### Reframe-to-Reframe MIDI2 peer projection — 2026-08-16

The Book now publishes the first system-capability projection that is not a writer command. The scenario
`reframe-to-reframe-peer-projection` exercised the existing `storify.source.start` operation between two separate
Reframe processes over MIDI2. The target retained mediation, consent, execution, and Store authority; the peer
received the correlated terminal lifecycle; and the target's `MIDI2 peers` projection exposed the completed relationship.

The sanitized record is [`evidence/2026-08-16/reframe-peer-terminal.md`](evidence/2026-08-16/reframe-peer-terminal.md),
with the matching window-ID capture. Runtime source revision: `Fountain-Coach/midi2-gpu-fabric@cbf31bdb`.
This is software-peer acceptance only; no physical hardware interoperability, Bluetooth behavior, or unbounded peer
capacity is claimed. The release surface remains `no-released-build` with an empty allow-list.

### Publication and deployment — MIDI2 peer capability

- Book commit: `c9c022c`, pushed to `Fountain-Coach/book-of-reframe@main`.
- Deployment: the reviewed `site/` projection was synchronized to the fixed `book.fountain.coach` publication root;
  local preview tooling and repository Markdown were excluded by the scoped deploy helper. DNS, Caddy, ownership, and
  permissions were not changed.
- Live HTTP: `/`, `/scenarios/`, `/capabilities/reframe-to-reframe-peer-projection/`, and the peer evidence image
  returned HTTP 200 from the canonical host.
- Live Chrome CDP: the capability route exposed its heading, `Primary navigation`, six named menu links, `Menu` →
  `Close` with `aria-expanded`, evidence alt text, an eight-link footer, and no horizontal overflow.
- Prepublication: `--check-external --strict` passed with 0 errors and 0 warnings before deployment.

### Scenario development cycle — 2026-08-16

Governance Chapter 73 now defines the scenario as Reframe's reusable development unit across commands, capabilities,
system boundaries, projections, and failure/recovery paths. The Book coverage manifest records `scenarioKind` for
each entry. Executable YAML remains canonical beside the implementation; this public repository contains only the
sanitized projection. No separate scenario repository is introduced.

The governance source commit is `Fountain-Coach/Reframe-Refactoring@0e42b7d`; the synchronized integration/runtime
commit is `Fountain-Coach/midi2-gpu-fabric@cb2cf559`. Scenario validation passed all 8 contracts, governance parity
reported 76 identical chapters, and Codex/Claude skill parity passed.

The final Book projection, including the Chapter 73 links and `scenarioKind` manifest, is
`Fountain-Coach/book-of-reframe@84bff9f` and is the revision deployed to `book.fountain.coach`.
