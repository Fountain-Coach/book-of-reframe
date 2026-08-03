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
- This public repository is a reviewed projection. It must not publish runtime source, private store data, secrets,
  unowned manuscript material, deployment details, or an unaudited claim. Publisher-owned manuscript evidence may be
  published only under the recorded rights-review gate. The private runtime is named with an access note; public
  governance Chapter 44 explains the boundary.
