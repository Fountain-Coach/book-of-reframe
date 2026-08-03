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

The command-page contract is snapshot-gated: each completed page begins with its own live-drive GUI image, with AX
and FountainStore evidence recorded alongside it. The catalog screenshot is not reused as command proof.

The local site acceptance pass for this update used Google Chrome via CDP at `http://127.0.0.1:4173/`: home and
`/commands/commands/` AX/VRT checks passed, and `/commands/pipeline-status/` returned HTTP 200 with its canonical,
Open Graph, alt-text, and evidence image metadata. The strict prepublish scan passed with `--check-external` (0 errors,
0 warnings). Publication commit `5b0d155` was synchronized to `/var/www/book-of-reframe`; the new route and image
now return HTTPS `200` from the canonical host. Local-only preview launchers remain excluded.
