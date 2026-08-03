# Copilot Capability Audit

Generated: 2026-08-03

The v2 registry contains **53** identities: **22** executable, **31** unavailable, **2** live-accepted, and **0** contract-drift findings.

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
| `manuscript.reading.inspect` | available | executable-not-live-accepted | `inspectReading` | natural language, /threads | live-drive both origins on a fresh managed store: /threads and a natural-language "what does this reading still doubt?", plus the never-read case, then record AX + FountainStore proof and promote to live-accepted |
| `pipeline.readiness` | unavailable | unavailable-adapter-proof | `unavailable` | — | build adapter and proof |
| `pipeline.rerun` | unavailable | unavailable-adapter-proof | `unavailable` | — | build adapter and proof |
| `pipeline.sla` | unavailable | unavailable-adapter-proof | `unavailable` | — | build adapter and proof |
| `pipeline.status` | available | live-accepted | `showPipelineStatus` | natural language, /pipeline status | maintain acceptance evidence |
| `prep.frame.switch` | available | executable-not-live-accepted | `switchPrepFrame` | natural language | record live acceptance |
| `prep.grounding.confirm` | available | executable-not-live-accepted | `confirmGrounding` | natural language | record live acceptance |
| `prep.guide.adopt` | available | executable-not-live-accepted | `adoptPrepGuide` | natural language | record live acceptance |
| `prep.guide.generate` | available | executable-not-live-accepted | `generatePrepGuide` | natural language | record live acceptance |
| `prep.guide.publish` | available | executable-not-live-accepted | `publishPrepGuide` | natural language | record live acceptance |
| `prep.guide.review` | available | executable-not-live-accepted | `reviewPrepGuide` | natural language | record live acceptance |
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
- **fullCatalogWindowCapture**: /tmp/commands-live-fullcatalog-20260803.png
- **naturalLanguageAX**: Fresh-store natural-language request rendered command-results with 92 available and 3 unavailable entries; copilot-capability-activity reports Phase succeeded.
- **naturalLanguageFountainStore**: /tmp/commands-live-20260803-nl-fixed.fountainstore — app.commands.discover naturalLanguage lifecycle requested → accepted → running → succeeded; execution 41821923-3655-4f87-81d6-fb20533352c2
- **naturalLanguageProof**: Aggregate copilot:capability:reframe-ulysses:41821923-3655-4f87-81d6-fb20533352c2 records command.catalog.entries and command.catalog.source=slashCommandIndex.
- **naturalLanguageWindowCapture**: /tmp/commands-live-natural-20260803.png
- **slashAX**: AX command-results exposes 92 available and 3 unavailable entries with reasons; copilot-capability-activity reports Phase succeeded.
- **slashFountainStore**: /tmp/commands-live-20260803-2.fountainstore — app.commands.discover slash lifecycle requested → accepted → running → succeeded; execution b0781a46-eaba-4ec3-8b8b-2a6602eb2175
- **slashProof**: Aggregate copilot:capability:reframe-ulysses:b0781a46-eaba-4ec3-8b8b-2a6602eb2175 records command.catalog.entries and command.catalog.source=slashCommandIndex.

### `pipeline.status`

- **acceptedOn**: 2026-08-01
- **ax**: projection `copilot-capability-activity` reported phase `succeeded`
- **proof**: the store-backed chat round contains the proof-bearing pipeline result
- **response**: writer-facing response was `PIPELINE STATUS`, with no legacy `STORIFY SYNOPSIS` surface
- **scenario**: Reframe moved to the secondary 1920x1080 display at {127,-1080}, full-screen, “Show pipeline status” submitted through AX
- **screenshot**: CoreGraphics window-ID capture at `/tmp/secondary-governed-drive.png`
- **store**: fresh managed store `/tmp/secondary-governed-drive.1PYA6y`, Romeo and Juliet imported from DraCor
