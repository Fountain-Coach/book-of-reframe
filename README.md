# The Book of Reframe

The Book of Reframe is the public, human-readable guide to what Reframe can do: its commands, capabilities,
preconditions, costs, evidence, and the reasoning behind its writer-facing surfaces.

This repository is a publication, not the runtime contract. The application and governed capability registry live in
[`Fountain-Coach/midi2-gpu-fabric`](https://github.com/Fountain-Coach/midi2-gpu-fabric). The governing architecture and
agent practice live in [`Fountain-Coach/Reframe-Refactoring`](https://github.com/Fountain-Coach/Reframe-Refactoring).

## Start here

- [`COMMAND-ATLAS.md`](COMMAND-ATLAS.md) — the first verified numbered command atlas, with writer-facing explanations;
- [`CAPABILITY-ATLAS.md`](CAPABILITY-ATLAS.md) — the current Copilot boundary and closure status;
- [`RELEASE-SURFACE.md`](RELEASE-SURFACE.md) — what a named App build is allowed to promise;
- [`HISTORICAL-COMMANDS.md`](HISTORICAL-COMMANDS.md) — why the development command inventory is broader than a release;
- [`evidence/2026-08-03/verified-command-catalog.md`](evidence/2026-08-03/verified-command-catalog.md) — the
  machine-shaped catalog projection from the live app.

## Publication rule

The book is updated from live runtime and persisted evidence. A command count is not a capability count; aliases are
not new powers; “available” is not the same as live-accepted; and a feature is not documented as working merely
because a prompt or UI title mentions it.

The integration repository's `book-of-reframe-maintenance` skill defines the maintenance workflow.

Each completed command page begins with the GUI snapshot of that command executing and showing its result. The
snapshot is paired with AX evidence and persisted FountainStore proof; commands not yet driven remain explicitly
pending. FCIS status is tracked in [`FCIS_AUDIT.md`](FCIS_AUDIT.md) and
[`FCIS_COMPLIANCE_PLAN.md`](FCIS_COMPLIANCE_PLAN.md).

The current publication records **no released App surface**. The 95-entry command atlas is a development/runtime
inventory, not a shipped capability promise.

Canonical standards: [FCIS-AX](https://github.com/Fountain-Coach/.github/blob/main/docs/FCIS-AX-Standard.md) and
[FCIS-VRT](https://github.com/Fountain-Coach/.github/blob/main/docs/FCIS-VRT-Standard.md).
