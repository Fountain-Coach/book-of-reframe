# Publication provenance

This book is published from the integration repository:

- Runtime and registry: private `Fountain-Coach/midi2-gpu-fabric` (access required; not a public source link)
- Governance and agent practice: https://github.com/Fountain-Coach/Reframe-Refactoring
- Publication boundary: [PUBLICATION-POLICY.md](PUBLICATION-POLICY.md) and [governance Chapter 44](https://github.com/Fountain-Coach/Reframe-Refactoring/blob/main/docs/44-publication-and-source-policy.md)
- Policy PRs: org FCIS [#4](https://github.com/Fountain-Coach/.github/pull/4), governance
  [#7](https://github.com/Fountain-Coach/Reframe-Refactoring/pull/7), runtime
  [#21](https://github.com/Fountain-Coach/midi2-gpu-fabric/pull/21), and this Book projection
  [#9](https://github.com/Fountain-Coach/book-of-reframe/pull/9).
- Maintenance skill: `midi2-gpu-fabric/.codex/skills/book-of-reframe-maintenance`

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
