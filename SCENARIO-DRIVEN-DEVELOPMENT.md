# Scenario-Driven Development

Scenario-Driven Development is the development method behind Reframe's E2E infrastructure. A scenario is not a
loose test script and not a screenshot checklist. It is a versioned contract that declares a journey before its source
slice is implemented: prerequisites, actors, typed actions, lifecycle events, terminal predicates, evidence bindings,
failure states, cleanup, and the boundary of the claim.

## Why it changes the development cycle

Without a shared scenario contract, end-to-end work is repeatedly reconstructed from prose. One person launches an
app, another writes automation, a third reads a screenshot, and a fourth infers success from a timeout or a log. The
system may appear to work while the process, Store, source commit, or definition of completion silently changes.

Scenario-Driven Development carries those decisions forward as one inspectable identity:

```text
contract → focused source slice → typed execution → independent evidence → correction → public projection
```

That relieves development from improvisation and babysitting. A failure remains attached to the exact scenario, source
commit, executable, process, Store, window, and evidence root that produced it. A maintainer can ask for the next
scenario by identity, and Reframe can resolve its prerequisites and expected proof before work begins.

## What MIDI2 contributes

Historically, end-to-end development evolved from unit tests and acceptance-test-driven development through CI
pipelines, contract tests, and message-oriented integration. Those practices made software more repeatable, but the
test runner could still speak a private command language and reconstruct progress through sleeps, polling, and log
interpretation.

MIDI 2.0 gives Reframe a natural event-driven substrate. A scenario actor can participate as a software peer, invoke the
same typed operation boundary as a production peer, and receive correlated lifecycle events over Universal MIDI
Packets. Admission, running, terminal success, refusal, failure, reconnect, duplicate, resume, and capacity outcomes
become explicit protocol events rather than guesses from elapsed time.

MIDI2 does not make a test pass by itself and it does not replace independent proof. Accessibility proves what the
writer-facing surface exposed and accepted. CoreGraphics/VRT proves rendered appearance. FountainStore proves durable
behavior. Telemetry explains resource and timing conditions. A MIDI2 lifecycle event alone is never visual or behavioral
proof.

## The organizational infrastructure

The generic lifecycle and MIDI2 transport seam is released as the public
[FountainScenarioKit](https://github.com/Fountain-Coach/FountainScenarioKit). The kit owns generic contracts,
idempotent lifecycle, UMP encoding, and deterministic fixtures. Reframe owns its product operation identity, Store
adapter, AX and window witnesses, scenario corpus, and acceptance claim. This is the FCIS-KIT boundary: a reusable seam
is released upstream, tested in its own repository, and consumed by version; product meaning remains local to the
consumer.

The public Book explains the method for humans. Reframe's maintainer projection may later provide role-gated procedure
context from the same reviewed Book commit and digest. Neither projection is runtime authority. The runtime IDL, live
FountainStore state, generated capability facts, and independent Live Drive remain authoritative.

## Historical perspective and future

Scenario-Driven Development is the next layer above CI: the scenario itself becomes a protocol-bound development
participant with durable evidence and a public explanation. MIDI-CI discovery and Property Exchange can extend this
from one product to negotiated software peers. Future Fountain Coach kits can share lifecycle, transport, fixture,
and evidence seams while each product keeps authority over its own behavior and UI.

The longer-term direction is a network of cooperating development peers: a Reframe instance, a stage, a service, or a
future physical MIDI2 device can advertise typed roles, negotiate capabilities, exchange correlated lifecycle events,
and retain independent witnesses. Software-peer acceptance is already meaningful; physical hardware interoperability
remains a separate claim that requires a hardware witness.

## Governing references

- [Chapter 77 — The Scenario Runtime Is Swift and MIDI2-Native](https://github.com/Fountain-Coach/Reframe-Refactoring/blob/main/docs/77-swift-midi2-scenario-runtime.md)
- [Chapter 78 — Scenario-Driven Development Is Org Infrastructure](https://github.com/Fountain-Coach/Reframe-Refactoring/blob/main/docs/78-scenario-driven-development-as-org-infrastructure.md)
- [E2E scenario coverage](E2E-SCENARIOS.md)
- [FountainScenarioKit](https://github.com/Fountain-Coach/FountainScenarioKit)
