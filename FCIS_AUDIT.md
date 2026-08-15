# FCIS Audit

## Executive summary

Status: PARTIAL — the publication now has the required FCIS layering, snapshot-gated command-page contract, and an
explicit no-release boundary;
individual live-drive evidence is complete for `/commands` and remains pending for the other catalog entries.

## Repository inventory

- Behavioral law and routing: `AGENTS.md`
- Long-task intent: `PLANS.md`
- Publication projection: `README.md`, `COMMAND-ATLAS.md`, `CAPABILITY-ATLAS.md`, `commands/`
- Evidence and provenance: `evidence/`, `SOURCE.md`
- Release boundary: `RELEASE-SURFACE.md`, `evidence/2026-08-03/reframe-release-surface.json`
- Org standards: Fountain-Coach `.github` FCIS-AX and FCIS-VRT

## Compliance matrix

| Requirement | Status | Evidence | Fix / maintenance rule |
| --- | --- | --- | --- |
| FCIS-AGENTS-1 | PASS | `AGENTS.md` declares invariants and routing, not a runbook. | Keep procedures in skills. |
| FCIS-PLANS-1 | PASS | `PLANS.md` records publication and snapshot-gated phases. | Update before high-risk publication work. |
| FCIS-SKILLS-1 | PASS | Source repository contains mirrored maintenance skills. | Keep copies byte-identical. |
| FCIS-LAYERS-1 | PASS | Law, intent, procedure, and publication evidence are separated. | Reject duplicated procedures. |
| FCIS-AX-01/04/05 | PASS | Pages and `/scenarios/` link AX/result proof; publication does not claim from pixels alone. | Preserve AX identifiers in evidence. |
| FCIS-VRT-01/04 | PARTIAL | `evidence/` stores versioned window-ID snapshots; gate is manual/opt-in. | Add a snapshot for each command before marking complete. |
| RELEASE-SURFACE-01 | PASS | Release manifest says `no-released-build` and has an empty allow-list. | Populate only from a named accepted build. |
| FCIS-PROVENANCE-1 | PASS | `SOURCE.md` links runtime, governance, snapshot, and publication provenance. | Update reciprocal commits/PRs. |
| FCIS-CONTENT-1 | PASS | Evidence contains no runtime source, private store export, credentials, or secrets. The 2026-08-04 `/threads` image is full fidelity under the recorded publisher ownership/scope review for the Polyxsupershow source. | Repeat the ownership, personal-data, third-party, and secret review for every owned manuscript asset. |
| FCIS-BOOK-PROJECTION-1 | PASS | Public Book is the human reference; the maintainer snapshot is separately role-gated, source-bound, and not an execution authority. | Keep the public commit/digest and maintainer snapshot identity aligned when ingestion is enabled. |

## Orthogonality violations

None found in the publication layer after this change. The existing runtime catalog remains source truth; pages are a
projection and do not define capabilities.

## Risks / drift vectors

- A command page could be added without its own live-drive result unless the validator is run.
- AX, screenshot, and FountainStore evidence can drift if only one is refreshed.
- The manual VRT gate can be skipped unless publication review runs the page validator.
- The public `/scenarios/` page and the future maintainer snapshot can drift unless both carry the same reviewed Book
  commit and content digest.

## Current evidence boundary

`/commands` is live-accepted. The remaining entries are intentionally not represented as completed command pages until
their individual drives capture execution and result.
