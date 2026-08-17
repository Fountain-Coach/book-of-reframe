# The Book of Reframe

The Book of Reframe is the public, human-readable guide to what Reframe can do: its commands, capabilities,
preconditions, costs, evidence, and the reasoning behind its writer-facing surfaces.

The Book also records system-capability projections that are not writer commands. The first is
[Reframe-to-Reframe MIDI2 software-peer projection](capabilities/reframe-to-reframe-peer-projection.md): an
evidence-backed software-peer acceptance in which the target Reframe retains mediation, consent, execution, and Store
authority.

This repository is a public, sanitized publication, not the runtime contract or a source mirror. The application and
governed capability registry live in the private `Fountain-Coach/midi2-gpu-fabric` repository; readers without access
may see GitHub's 404. The public explanation of this boundary is
[`PUBLICATION-POLICY.md`](PUBLICATION-POLICY.md) and
[`Fountain-Coach/Reframe-Refactoring` governance Chapter 44](https://github.com/Fountain-Coach/Reframe-Refactoring/blob/main/docs/44-publication-and-source-policy.md).

## Start here

- [`COMMAND-ATLAS.md`](COMMAND-ATLAS.md) — the first verified numbered command atlas, with writer-facing explanations;
- [`CAPABILITY-ATLAS.md`](CAPABILITY-ATLAS.md) — the current Copilot boundary and closure status;
- [`RELEASE-SURFACE.md`](RELEASE-SURFACE.md) — what a named App build is allowed to promise;
- [`PUBLICATION-POLICY.md`](PUBLICATION-POLICY.md) — what the public Book may expose and what remains private;
- [`HISTORICAL-COMMANDS.md`](HISTORICAL-COMMANDS.md) — why the development command inventory is broader than a release;
- [`LANE-POLICY.md`](LANE-POLICY.md) — the paid-first routing contract and its evidence boundary;
- [`SCENARIO-DRIVEN-DEVELOPMENT.md`](SCENARIO-DRIVEN-DEVELOPMENT.md) — how versioned scenarios and MIDI2 relieve the development cycle;
- [`GOVERNANCE-79.md`](GOVERNANCE-79.md) — the public projection of the default semantic manuscript workspace;
- [`E2E-SCENARIOS.md`](E2E-SCENARIOS.md) — the machine-linked scenario publication boundary;
- [`evidence/2026-08-03/verified-command-catalog.md`](evidence/2026-08-03/verified-command-catalog.md) — the
  machine-shaped catalog projection from the live app.

## Publication rule

The book is updated from live runtime and persisted evidence. A command count is not a capability count; aliases are
not new powers; “available” is not the same as live-accepted; and a feature is not documented as working merely
because a prompt or UI title mentions it.

The integration repository's `book-of-reframe-maintenance` skill defines the maintenance workflow.

The generic scenario lifecycle and MIDI2 transport seam is publicly released as
[FountainScenarioKit](https://github.com/Fountain-Coach/FountainScenarioKit). The kit is reusable infrastructure,
not a public mirror of Reframe's private runtime; its product-specific Store, AX, window-ID, and acceptance evidence
remain in the integration and Book projections.

Each completed command page begins with the GUI snapshot of that command executing and showing its result. The
snapshot is paired with AX evidence and persisted FountainStore proof; commands not yet driven remain explicitly
pending. FCIS status is tracked in [`FCIS_AUDIT.md`](FCIS_AUDIT.md) and
[`FCIS_COMPLIANCE_PLAN.md`](FCIS_COMPLIANCE_PLAN.md).

The current publication records **no released App surface**. The 95-entry command atlas is a development/runtime
inventory, not a shipped capability promise.

For social promotion, the mirrored `book-of-reframe-social-publish` skill prepares a reviewable Facebook package from
an individually verified command page. It uses that page's GUI snapshot as the post image and requires explicit
confirmation before any external publication.

Canonical standards: [FCIS-AX](https://github.com/Fountain-Coach/.github/blob/main/docs/FCIS-AX-Standard.md) and
[FCIS-VRT](https://github.com/Fountain-Coach/.github/blob/main/docs/FCIS-VRT-Standard.md).
