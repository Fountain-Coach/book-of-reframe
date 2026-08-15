# Copilot Capability Audit

Generated: 2026-08-15

The v2 registry contains **55** identities: **24** executable, **31** unavailable, **2** live-accepted, and **0** contract-drift findings.

A capability is fully empowered only when its adapter, policy, focused tests, persisted proof, telemetry, AX result, and required live acceptance are recorded.

## Next implementation batch

Prioritize available-but-unaccepted capabilities first, then implement unavailable rows in dependency order. The ledger is the durable progress record.

## Capability ledger

| Capability | Registry | Audit status | Native operation | Origins | Next step |
| --- | --- | --- | --- | --- | --- |
| `analytics.local` | unavailable | unavailable-adapter-proof | `unavailable` | — | build adapter and proof |
| `app.commands.discover` | available | live-accepted | `discoverCommands` | natural language, /commands | Maintain acceptance evidence; future command capabilities require their own adapter, policy, and live matrix. |
| `continuity.audit` | unavailable | unavailable-adapter-proof | `unavailable` | — | build adapter and proof |
| `continuity.status` | unavailable | unavailable-adapter-proof | `unavailable` | — | build adapter and proof |
| `fountain.fix` | unavailable | unavailable-adapter-proof | `unavailable` | — | build adapter and proof |
| `fountain.lint` | unavailable | unavailable-adapter-proof | `unavailable` | — | build adapter and proof |
| `fountain.project.export` | available | executable-not-live-accepted | `exportFountainProject` | natural language | record live acceptance |
| `fountainstore.document.read` | unavailable | unavailable-adapter-proof | `unavailable` | — | build adapter and proof |
| `fountainstore.document.write` | unavailable | unavailable-adapter-proof | `unavailable` | — | build adapter and proof |
| `launcher.library.open` | available | executable-not-live-accepted | `openLibrary` | natural language | record live acceptance |
| `launcher.project.create` | unavailable | unavailable-adapter-proof | `unavailable` | — | build adapter and proof |
| `launcher.project.import` | unavailable | unavailable-adapter-proof | `unavailable` | — | build adapter and proof |
| `launcher.project.open` | unavailable | unavailable-adapter-proof | `unavailable` | — | build adapter and proof |
| `launcher.shelf.read` | unavailable | unavailable-adapter-proof | `unavailable` | — | build adapter and proof |
| `lora.dataset.prepare` | unavailable | unavailable-adapter-proof | `unavailable` | — | build adapter and proof |
| `lora.eval` | unavailable | unavailable-adapter-proof | `unavailable` | — | build adapter and proof |
| `lora.promote` | unavailable | unavailable-adapter-proof | `unavailable` | — | build adapter and proof |
| `lora.train` | unavailable | unavailable-adapter-proof | `unavailable` | — | build adapter and proof |
| `git.library.candidate.create` | available | executable-not-live-accepted | `createLibraryCandidate` | natural language | record live acceptance |
| `git.library.candidate.promote` | available | executable-not-live-accepted | `promoteLibraryCandidate` | natural language | record live acceptance |
| `git.project.commit` | available | executable-not-live-accepted | `commitManagedProject` | natural language | record live acceptance |
| `git.project.provision` | available | executable-not-live-accepted | `provisionProject` | natural language | record live acceptance |
| `manuscript.reading.inspect` | available | executable-not-live-accepted | `inspectReading` | natural language, /threads | live-drive both origins on a fresh managed store: /threads and a natural-language "what does this reading still doubt?", plus the never-read case, then record AX + FountainStore proof and promote to live-accepted |
| `maintenance.health.verify` | available | executable-not-live-accepted | `verifyMaintenanceHealth` | natural language, /maintenance health | record live acceptance |
| `pipeline.readiness` | unavailable | unavailable-adapter-proof | `unavailable` | — | build adapter and proof |
| `pipeline.rerun` | unavailable | unavailable-adapter-proof | `unavailable` | — | build adapter and proof |
| `pipeline.sla` | unavailable | unavailable-adapter-proof | `unavailable` | — | build adapter and proof |
| `pipeline.status` | available | live-accepted | `showPipelineStatus` | natural language, /pipeline status | maintain acceptance evidence |
| `prep.frame.switch` | available | executable-not-live-accepted | `switchPrepFrame` | natural language | record live acceptance |
| `prep.grounding.propose` | available | executable-not-live-accepted | `confirmGrounding` | natural language, /ground | slash origin recorded 2026-08-09 ([`/ground`](commands/ground.md): terminal aggregate, AX, FountainStore, repeated); still needed: the natural-language origin, and the accepted-lens path on a reading without holes |
| `screenplay.beat.read` | unavailable | unavailable-adapter-proof | `unavailable` | — | build adapter and proof |
| `screenplay.beat.write` | unavailable | unavailable-adapter-proof | `unavailable` | — | build adapter and proof |
| `screenplay.note` | unavailable | unavailable-adapter-proof | `unavailable` | — | build adapter and proof |
| `screenplay.patch` | unavailable | unavailable-adapter-proof | `unavailable` | — | build adapter and proof |
| `screenplay.read` | unavailable | unavailable-adapter-proof | `unavailable` | — | build adapter and proof |
| `screenplay.source.import` | unavailable | unavailable-adapter-proof | `unavailable` | — | build adapter and proof |
| `screenplay.write.draft` | unavailable | unavailable-adapter-proof | `unavailable` | — | build adapter and proof |
| `semantic_memory.read` | unavailable | unavailable-adapter-proof | `unavailable` | — | build adapter and proof |
| `semantic_memory.write` | unavailable | unavailable-adapter-proof | `unavailable` | — | build adapter and proof |
| `storify.assign` | unavailable | unavailable-adapter-proof | `unavailable` | — | build adapter and proof |
| `storify.draft.start` | unavailable | unavailable-adapter-proof | `unavailable` | — | build adapter and proof |
| `storify.guide` | unavailable | unavailable-adapter-proof | `unavailable` | — | build adapter and proof |
| `storify.run.stop` | available | executable-not-live-accepted | `stopStorifyRun` | natural language, /storify! stop, storify-stop | record live acceptance |
| `storify.source.start` | available | executable-not-live-accepted | `startStorifySource` | natural language, /storify! source auto, /storify! source auto restart, /beats start, /beats refresh, storify-source-start | record live acceptance |
| `storify.synopsis` | unavailable | unavailable-adapter-proof | `unavailable` | — | build adapter and proof |
| `work.citation.add` | available | executable-not-live-accepted | `addCitation` | natural language, /cite | record live acceptance |
| `work.citation.verify` | available | executable-not-live-accepted | `verifyCitations` | natural language, /cite verify | record live acceptance |
| `world.identity.escalate` | available | executable-not-live-accepted | `escalateUnresolvedIdentities` | natural language, /world ask | drive the natural-language origin for each verb, and one session on a paid answering lane |
| `world.ledger.clear` | available | executable-not-live-accepted | `clearWorldLedger` | natural language, /world clear | drive the natural-language origin for each verb, and one session on a paid answering lane |
| `world.ledger.read` | available | executable-not-live-accepted | `readWorldLedger` | natural language, /world | drive the natural-language origin for each verb, and one session on a paid answering lane |
| `world.reference.accept` | available | executable-not-live-accepted | `acceptReferenceStep` | natural language, /world yes | drive the natural-language origin for each verb, and one session on a paid answering lane |
| `world.reference.decline` | available | executable-not-live-accepted | `declineReferenceStep` | natural language, /world no | drive the natural-language origin for each verb, and one session on a paid answering lane |
| `world.reference.log` | available | executable-not-live-accepted | `readReferenceLog` | natural language, /world references | drive the natural-language origin for each verb, and one session on a paid answering lane |
| `world.reference.research` | available | executable-not-live-accepted | `proposeReferenceResearch` | natural language, /world research | drive the natural-language origin for each verb, and one session on a paid answering lane |
| `world.reference.widen` | available | executable-not-live-accepted | `widenReferenceToPaidLane` | natural language, /world widen | drive the natural-language origin for each verb, and one session on a paid answering lane |

## Contract drift

- None detected by the deterministic registry audit.

## Generated contract

- Tracked GeneratedCopilotCapabilities.swift: present

## Live acceptance evidence

### `app.commands.discover`

- **fullCatalogAX**: Fresh `/commands` drive exposes command-results-all as a scrollable AXScrollArea with the complete catalog; AX enumerated available entries beyond the previous six-row audit subset.
- **fullCatalogWindowCapture**: evidence/2026-08-03/commands-live-fullcatalog-20260803.png
- **naturalLanguageAX**: Fresh-store natural-language request rendered command-results with 92 available and 3 unavailable entries; copilot-capability-activity reports Phase succeeded.
- **naturalLanguageFountainStore**: sanitized live proof recorded in evidence/2026-08-03/copilot-capability-closure.json — app.commands.discover naturalLanguage lifecycle requested → accepted → running → succeeded; execution 41821923-3655-4f87-81d6-fb20533352c2
- **naturalLanguageProof**: Aggregate copilot:capability:reframe-ulysses:41821923-3655-4f87-81d6-fb20533352c2 records command.catalog.entries and command.catalog.source=slashCommandIndex.
- **naturalLanguageWindowCapture**: the full-catalog visual capture is in evidence/2026-08-03/commands-live-fullcatalog-20260803.png
- **slashAX**: AX command-results exposes 92 available and 3 unavailable entries with reasons; copilot-capability-activity reports Phase succeeded.
- **slashFountainStore**: sanitized live proof recorded in evidence/2026-08-03/copilot-capability-closure.json — app.commands.discover slash lifecycle requested → accepted → running → succeeded; execution b0781a46-eaba-4ec3-8b8b-2a6602eb2175
- **slashProof**: Aggregate copilot:capability:reframe-ulysses:b0781a46-eaba-4ec3-8b8b-2a6602eb2175 records command.catalog.entries and command.catalog.source=slashCommandIndex.

### `pipeline.status`

- **acceptedOn**: 2026-08-01
- **ax**: projection `copilot-capability-activity` reported phase `succeeded`
- **proof**: the store-backed chat round contains the proof-bearing pipeline result
- **response**: writer-facing response was `PIPELINE STATUS`, with no legacy `STORIFY SYNOPSIS` surface
- **scenario**: Reframe moved to the secondary 1920x1080 display at {127,-1080}, full-screen, “Show pipeline status” submitted through AX
- **screenshot**: CoreGraphics window-ID capture from the integration live-drive evidence
- **store**: fresh managed store used by the integration live drive, Romeo and Juliet imported from DraCor
