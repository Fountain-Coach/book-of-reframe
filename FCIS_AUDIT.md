# FCIS Audit

## Executive summary

Status: PARTIAL — the publication now has the required FCIS layering and a snapshot-gated command-page contract;
individual live-drive evidence is complete for `/commands` and remains pending for the other catalog entries.

## Repository inventory

- Behavioral law and routing: `AGENTS.md`
- Long-task intent: `PLANS.md`
- Publication projection: `README.md`, `COMMAND-ATLAS.md`, `CAPABILITY-ATLAS.md`, `commands/`
- Evidence and provenance: `evidence/`, `SOURCE.md`
- Org standards: Fountain-Coach `.github` FCIS-AX and FCIS-VRT

## Compliance matrix

| Requirement | Status | Evidence | Fix / maintenance rule |
| --- | --- | --- | --- |
| FCIS-AGENTS-1 | PASS | `AGENTS.md` declares invariants and routing, not a runbook. | Keep procedures in skills. |
| FCIS-PLANS-1 | PASS | `PLANS.md` records publication and snapshot-gated phases. | Update before high-risk publication work. |
| FCIS-SKILLS-1 | PASS | Source repository contains mirrored maintenance skills. | Keep copies byte-identical. |
| FCIS-LAYERS-1 | PASS | Law, intent, procedure, and publication evidence are separated. | Reject duplicated procedures. |
| FCIS-AX-01/04/05 | PASS | Pages link AX/result proof; publication does not claim from pixels alone. | Preserve AX identifiers in evidence. |
| FCIS-VRT-01/04 | PARTIAL | `evidence/` stores versioned window-ID snapshots; gate is manual/opt-in. | Add a snapshot for each command before marking complete. |
| FCIS-PROVENANCE-1 | PASS | `SOURCE.md` links runtime, governance, snapshot, and publication provenance. | Update reciprocal commits/PRs. |
| FCIS-CONTENT-1 | PASS | Evidence is sanitized and contains no prompts or private store data. | Keep publication projections sanitized. |

## Orthogonality violations

None found in the publication layer after this change. The existing runtime catalog remains source truth; pages are a
projection and do not define capabilities.

## Risks / drift vectors

- A command page could be added without its own live-drive result unless the validator is run.
- AX, screenshot, and FountainStore evidence can drift if only one is refreshed.
- The manual VRT gate can be skipped unless publication review runs the page validator.

## Current evidence boundary

`/commands` is live-accepted. The remaining entries are intentionally not represented as completed command pages until
their individual drives capture execution and result.
