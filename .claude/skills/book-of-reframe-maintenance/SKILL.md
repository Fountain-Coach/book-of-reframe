---
name: book-of-reframe-maintenance
description: Maintain and publish the verified Book of Reframe command and capability documentation. Use when `/commands`, the capability registry, runtime command ownership, or live acceptance evidence changes, or when publishing the public Fountain-Coach book.
---

# Book of Reframe Maintenance

Maintain the public `Fountain-Coach/book-of-reframe` publication from verified Reframe runtime evidence. The
integration repository is authoritative for command and capability behavior; the book is a reviewed projection, never
a second runtime contract.

## Authority and safety

- Read root and scoped `AGENTS.md`, the current `PLANS.md` phase, and governance chapters before editing.
- Treat `schema/modernization-studio-capabilities.json`, generated reasoning artifacts, live FountainStore state, AX,
  and runtime proof as the authority chain.
- Distinguish command entries from capabilities. Count aliases and compatibility spellings as entries, but document
  them as aliases; never present them as independent powers.
- Distinguish `available` from live-accepted. A readiness label is not proof that every argument or workflow succeeds.
- Do not document a capability as executable because a prompt, title, slash entry, or historical screenshot mentions it.
- Never copy prompts, private store data, or unowned manuscript material into the public book. Publisher-owned
  manuscript evidence may be included only when the page records the ownership declaration, exact public scope, and
  review for personal data, third-party material, and secrets. Do not apply obfuscation to owned material merely to
  make a screenshot look sanitized; the evidence must show the command's actual reading surface.

## Workflow

1. **Plan.** Add a `PLANS.md` phase naming the source, publication target, scope, exclusions, and validation.
2. **Resolve release status.** Read `releases/reframe-release-surface.json` before describing what the App ships.
   A named release/build and non-empty capability allow-list are required for a released-surface claim. If the
   manifest says `no-released-build` or `development-snapshot`, publish that status and keep its allow-list empty.
3. **Inspect source.** Run the Copilot capability audit and inspect the registry, generated manifest, slash index, and
   command catalog codec. Search the router when a command's ownership is unclear.
4. **Drive.** For a changed command surface, run a governed fresh-store live drive. Use AX for interaction and
   semantics, CoreGraphics window-ID capture for visual proof, and `ReframeStoreDump` for behavioral proof. A
   command page is not publishable until the drive reaches that command's executed/result state and captures the
   relevant Reframe window by ID; never reuse a generic catalog screenshot as command proof.
5. **Extract.** Read the persisted `app.commands.discover` aggregate with `--corpus`, then run
   `scripts/export_command_catalog.py` to produce a sanitized numbered catalog. The script must preserve the raw
   runtime count, availability, visibility, titles, details, and aliases; it must not invent descriptions.
6. **Reconcile.** Compare command entries with `docs/copilot-capability-audit.md` and the registry. Record commands
   that are aliases, local orchestration, unavailable, `//`-only, or lacking a governed capability identity.
7. **Teach.** Add human-readable explanations, examples, required state, cost/confirmation, persisted effects, AX
   result identifiers, and live-proof links only when those facts are sourced. Every command document MUST begin
   with its own alt-texted GUI snapshot image showing the command's execution/result moment, followed by the
   command title and explanation. Keep the numbered raw catalog alongside the teaching chapters so the book remains
   auditable.
8. **Validate.** Run `scripts/verify_release_surface.py releases/reframe-release-surface.json`, the export check,
   capability audit, governance validator, focused tests, `git diff --check`, and
   `Scripts/sync-agent-skills --check`. If runtime or UI changed, run the relevant build/live proof as well.
9. **Publish.** Push the reviewed projection to `Fountain-Coach/book-of-reframe`. Link it back to
   `Fountain-Coach/midi2-gpu-fabric` and the governance repository `Fountain-Coach/Reframe-Refactoring`. Do not push
   unrelated integration work.
10. **Record.** Update the integration `PLANS.md` and the book's `SOURCE.md` with snapshot date, source commit, live
   store/evidence IDs, and publication commit.

Optional: after publication, use the mirrored `book-of-reframe-social-publish` skill to prepare a Facebook post
package from the command page. Social copy is a publication projection, never capability or release authority; actual
external posting always requires separate explicit confirmation.

## Publication shape

The public repository should contain:

- `README.md` — what Reframe is and how the book relates to runtime truth;
- `COMMAND-ATLAS.md` — numbered verified command inventory and writer-facing explanations;
- `CAPABILITY-ATLAS.md` — governed capability identities, status, owners, and proof links;
- `RELEASE-SURFACE.md` — the named-build release manifest projection and explicit no-release state;
- `HISTORICAL-COMMANDS.md` — commands retained for development, compatibility, aliases, help, or maintainer use;
- `commands/<slug>.md` — one writer-facing command document per command, each beginning with its own live-drive GUI
  snapshot;
- `site/` — canonical static web projection with stable command URLs and Open Graph metadata;
- `evidence/` — generated catalog, acceptance metadata, and explicitly rights-reviewed owned evidence only;
- `SOURCE.md` — reciprocal source links and provenance.

The page exporter and validator must fail closed when a command lacks a matching window-ID screenshot, AX/result
proof, or an image as its first non-empty line. Commands without proof remain in the pending inventory and are not
published as completed documentation.

The publication must never derive `RELEASE-SURFACE.md` from the command atlas. It is generated from the release
manifest and may contain an empty allow-list when no named distribution build exists.

The site is the canonical social destination. Build each command URL with an absolute HTTPS canonical URL and
`og:image` pointing to that command's own snapshot. Keep custom-domain configuration separate from content; do not
invent or register a domain during routine maintenance.

Keep the book useful to writers: explain intent and outcomes before implementation terms. Keep it useful to
maintainers: every claim must be traceable to a registry row, runtime owner, persisted proof, or explicitly marked
historical/design material.

## Required final report

Report the verified command-entry count, available/unavailable count, alias count if known, capability counts from the
audit, live evidence IDs, publication URL/commit, and any commands that remain unverified or unavailable.
