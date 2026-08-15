# Reframe E2E scenarios

The Book publishes a command only through a named, reusable end-to-end scenario. A scenario is the checked writer
journey behind a command page: prerequisites, semantic AX actions, state-based waits, paid-lane consent, terminal
AX state, FountainStore effects, window-ID visual evidence, provenance, and honest failure states.

The runtime and governance repositories remain authoritative. This directory is a sanitized publication projection.
It contains no prompts, manuscript text, private Store data, secrets, or deployment details.

## Coverage

The current published command pages are pinned in [`scenarios/coverage.json`](scenarios/coverage.json). The first
records are deliberately marked `draft`: their older evidence remains linked as legacy evidence, but it has not been
re-executed through the new scenario contract yet.

| Command | Scenario | Current status |
| --- | --- | --- |
| `/commands` | `commands-discover` | Draft; legacy evidence requires scenario run |
| `/pipeline status` | `pipeline-status` | Draft; legacy evidence requires scenario run |
| `/threads` | `threads` | Draft; legacy evidence requires scenario run |
| `/ground` | `ground-after-reading` | Draft; legacy evidence requires scenario run |
| `/readings` | `readings-comparison` | Draft; legacy evidence requires scenario run |

The governing method is [Chapter 68 — The Reframe E2E Scenario Is the Publication Unit](https://github.com/Fountain-Coach/Reframe-Refactoring/blob/main/docs/68-the-reframe-e2e-scenario-is-the-publication-unit.md).

The next scenario target is `world-after-storify`: import a source, complete `/storify! source auto` with explicit
confirmation, then run `/world`. The paid-default scenario is now live-accepted; `/world` remains unpublished by the
manifest until a command page is authored.

An isolated run is never presented as the writer's current UI. A command becomes `live-accepted` only when one run
binds its AX observations, CoreGraphics window-ID capture, FountainStore read-back, executable, Store, PID, and
source commit, and reaches the declared terminal result.
