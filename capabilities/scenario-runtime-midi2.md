# Reframe Swift/MIDI2 scenario runtime

Reframe's internal scenario capability executes one tracked E2E contract through the owned Swift/MIDI2 runtime. This is
a development/operator system boundary, not a new writer command and not a second Copilot persona.

## Current status

The contract is `scenario-runtime-midi2`, with capability `reframe.e2e.scenario.run`. Its YAML authoring contract and
checked JSON projection live in the private Reframe repository. The current public status is `executable`: the generic
runtime contract and MIDI2 lifecycle are present, but the scenario-specific projection and independent acceptance
evidence are still required before promotion to `live-accepted`.

## Intended acceptance

The scenario actor discovers the typed operation, invokes the tracked contract, receives correlated admitted/running/
terminal events, and observes the target's resulting accepted beats. FountainStore proves durable lifecycle and target
behavior; AX proves the exposed operation and result; CoreGraphics/window-ID capture proves the rendered surface;
telemetry and provenance bind the run. No single MIDI2 event self-approves the scenario.

## Claim boundary

This projection makes no claim about physical MIDI2 hardware, Bluetooth, unrestricted remote capacity, or a released App
surface. It documents a software-peer and development-runtime capability only. Reframe retains operation semantics,
Store authority, UI witnesses, and acceptance status.

## Where it appears

- Scenario identity: [`scenario-runtime-midi2`](../scenarios/coverage.json)
- Governing Chapter 77: [Swift/MIDI2 scenario runtime](https://github.com/Fountain-Coach/Reframe-Refactoring/blob/main/docs/77-swift-midi2-scenario-runtime.md)
- Governing Chapter 78: [Scenario-Driven Development](https://github.com/Fountain-Coach/Reframe-Refactoring/blob/main/docs/78-scenario-driven-development-as-org-infrastructure.md)
- Public method: [`SCENARIO-DRIVEN-DEVELOPMENT.md`](../SCENARIO-DRIVEN-DEVELOPMENT.md)
