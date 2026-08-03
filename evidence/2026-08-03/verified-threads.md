# `/threads` live-drive evidence

Date: 2026-08-03

## Scenario

- Fixture: fresh managed integration store, corpus `fixture`.
- Input: `/threads`, entered through `studio-chat-input` and submitted with `studio-chat-send`.
- Window proof: CoreGraphics window-ID capture, window `26594`.
- Snapshot: [sanitized GUI result](threads-live-20260803.png).

## AX result

The result was present in `chat-row-message-*`. The capability activity surface exposed:

`Inspect reading doubts, wants, and learning. Phase succeeded.`

The result reported five open questions. The public record deliberately omits their manuscript-derived wording.

## Persisted result

FountainStore recorded lifecycle event `copilot:capability-event:fixture:ba0d7ce4-9b4b-4b18-acab-7dedafdf6f1b` with the terminal phase sequence:

`requested → accepted → running → succeeded`

The event is the behavioural authority for this command. The run was read-only and did not mutate the manuscript.

## Grounding context

The managed fixture also recorded the active reader-lens grounding session and carried its grounding identity into the reading workflow. This supports the product invariant that grounding changes what `/threads` inspects. It is not evidence that a full Storify pagination run completed; that separate run remained non-terminal and was not published as a result.

## Acceptance boundary

This proves the `/threads` slash origin only. The natural-language origin and the never-read failure case remain open in the capability closure ledger. This is development/live-accepted command evidence, not a released App-surface claim.
