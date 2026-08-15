# Reframe E2E scenarios

The Book publishes a command only through a named, reusable end-to-end scenario. A scenario is the checked writer
journey behind a command page: prerequisites, semantic AX actions, state-based waits, paid-lane consent, terminal
AX state, FountainStore effects, window-ID visual evidence, provenance, and honest failure states.

The runtime and governance repositories remain authoritative. This directory is a sanitized publication projection.
It contains no prompts, manuscript text, private Store data, secrets, or deployment details.

## Internal E2E capability

Reframe now owns the reusable scenario semantics through the maintainer-only capability
`reframe.e2e.scenario.run`. Its machine-readable contract is [`scenarios/registry.json`](scenarios/registry.json).
The internal capability discovers scenarios, validates prerequisites, executes typed application behavior, and records
Store receipts. It does not approve itself: Live Drive remains the independent witness for AX state, CoreGraphics
window-ID capture, and visual regression. A scenario becomes `live-accepted` only where both evidence authorities
agree.

This division makes the development cycle efficient without making proof circular:

```text
internal Reframe capability → behavioral receipt
independent Live Drive → AX/window/VRT evidence
Book → sanitized intersection of both
```

## One public reference, one maintainer projection

The Book remains public at [book.fountain.coach](https://book.fountain.coach/) so another human can inspect the
scenario model, its evidence vocabulary, its statuses, and the request loop. Reframe may later consume a separate,
role-gated maintainer snapshot generated from the same reviewed Book commit and content digest. That snapshot may add
internal procedure references, but it is not a manuscript, an execution authorization, or a writer-facing retrieval
source.

The maintainer request is deliberately simple: “Add the next scenario for `/world`.” Reframe resolves the public
scenario identity, reports prerequisites and terminal artifacts, authors or repairs the private contract, validates and
runs the typed capability, invokes independent Live Drive, and updates the public projection only from the resulting
evidence bundle.

For Codex-driven source development, this is one governed scenario work session: resolve the scenario, bound the source
slice, implement and focus-test it, run the isolated scenario, independently witness the surface, and report one work
card with observed versus unestablished results. Deployment and release promotion remain separate, higher-privilege
operations.

## Coverage

The current published command pages are pinned in [`scenarios/coverage.json`](scenarios/coverage.json). Older evidence
remains linked as history; current status is promoted only after the scenario contract and independent witness agree.

| Command | Scenario | Current status |
| --- | --- | --- |
| `/commands` | `commands-discover` | Live-accepted; three-run scenario evidence |
| `/pipeline status` | `pipeline-status` | Draft; legacy evidence requires scenario run |
| `/threads` | `threads` | Draft; legacy evidence requires scenario run |
| `/ground` | `ground-after-reading` | Draft; legacy evidence requires scenario run |
| `/readings` | `readings-comparison` | Draft; legacy evidence requires scenario run |

The governing method is [Chapter 68 — The Reframe E2E Scenario Is the Publication Unit](https://github.com/Fountain-Coach/Reframe-Refactoring/blob/main/docs/68-the-reframe-e2e-scenario-is-the-publication-unit.md), together with [Chapter 69 — The Book of Reframe Is a Dual Projection](https://github.com/Fountain-Coach/Reframe-Refactoring/blob/main/docs/69-the-book-of-reframe-is-a-dual-projection.md).

The next scenario target is `world-after-storify`: import a source, complete `/storify! source auto` with explicit
confirmation, then run `/world`. The paid-default scenario is now live-accepted; `/world` remains unpublished by the
manifest until a command page is authored.

An isolated run is never presented as the writer's current UI. A command becomes `live-accepted` only when one run
binds its AX observations, CoreGraphics window-ID capture, FountainStore read-back, executable, Store, PID, and
source commit, and reaches the declared terminal result.
