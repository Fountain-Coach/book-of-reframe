# Publication plan

## 2026-08-03 — public/private publication policy

- Replace misleading public-facing runtime links with an explicit private-runtime access note.
- Publish `PUBLICATION-POLICY.md` and link the public governance Chapter 44.
- Keep the Book limited to sanitized command/capability projections, release boundaries, provenance, and AX/VRT proof.
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
