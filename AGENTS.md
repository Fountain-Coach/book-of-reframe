# Publishing-focused entrance (author-directed revision, 24 October 2026)

The Book domain's staged editorial purpose is explaining and demonstrating **publishing source-bound readable editions**, rather than making the command/scenario inventory its present-day chapters. Inherit FCIS Goal Fidelity and Non-Invention from Fountain-Coach/.github. The public First Reading is the bounded example; use its original route. Do not claim unverified Store membership, rights/title, public publisher receipts or App release status. The earlier Book of Reframe technical material remains a separate dated historical reference; existing command-page verification rules continue to apply to it.

Use the single existing registered Ubuntu WLAN staging environment for review. Public production requires separate owner authorization. A writer-admitted Bookshelf is distinct from a public edition.

---

# Book of Reframe publication guide

This repository contains reviewed documentation projections from Reframe's integration repository.

- Do not invent command behavior from prose, screenshots, or names.
- Prefer the integration registry, live FountainStore proof, AX evidence, and generated artifacts.
- Preserve the distinction between command entries, aliases, capabilities, availability, and live acceptance.
- Keep `SOURCE.md` and the snapshot evidence current whenever the book changes.
- This repository follows FCIS RFC 0001: `AGENTS.md` states law, `PLANS.md` states intent, and skills state
  procedures. Multi-step or high-risk publication work requires a plan before edits.
- Every command page under `commands/` MUST begin with an alt-texted GUI snapshot of that command's live execution
  and result. A page is not complete without matching AX semantics, window-ID visual evidence, and persisted proof.
- FCIS-AX is the semantic authority; FCIS-VRT is the visual authority. A screenshot cannot substitute for AX or
  FountainStore proof, and AX cannot substitute for looking at the rendered image.
- The book is a publication projection, not a runtime contract. It must not contain prompts, private store data,
  secrets, or invented behavior. Publisher-owned manuscript evidence is permitted only with an explicit ownership,
  scope, and personal-data/third-party/secrets review; it is not automatically obfuscated when the real GUI is the
  subject of the illustration.

## FCIS routing

- `FCIS_AUDIT.md` records the current compliance matrix and evidence.
- `FCIS_COMPLIANCE_PLAN.md` records minimal remediation and acceptance criteria.
- `.codex/skills/` and `.claude/skills/` contain identical publication procedures.
- The canonical standards are published in [Fountain-Coach/.github](https://github.com/Fountain-Coach/.github/tree/main/docs).
- The canonical web site is a static publication projection. Stable command URLs MUST carry Open Graph metadata whose
  `og:image` is that command's own live-drive GUI snapshot; GitHub remains source and provenance authority.
- The runtime repository is authoritative for implementation; this repository is authoritative only for publication text.
- Publication law: `scenarios/coverage.json` is the reviewed scenario input and `site/publication-manifest.json` is its
  deterministic projection. A command route is eligible only when its named scenario has an independent terminal
  `live-accepted` result and the reviewed page exists. `/command` inventory or legacy evidence alone never publishes
  or promotes a page. Accepted scenarios without pages remain `accepted-no-page`; system-boundary capabilities never
  become writer command routes. Scenario acceptance and named release status are separate axes: live-accepted is not
  released, and release claims require the named release surface and allow-list.
- Before local GO, run `python3 scripts/build-publication-manifest.py --check` and `python3 site/build-site-data.py`,
  then run the site AX/VRT and strict prepublication gates. Do not deploy or push while the local GO is pending.
- This public repository is a reviewed projection. It must not publish runtime source, private store data, secrets,
  unowned manuscript material, deployment details, or an unaudited claim. Publisher-owned manuscript evidence may be
  published only under the recorded rights-review gate. The private runtime is named with an access note; public
  governance Chapter 44 explains the boundary.
