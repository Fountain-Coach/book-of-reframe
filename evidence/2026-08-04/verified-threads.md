# `/threads` live acceptance — Polyxsupershow Courier reading surface

Snapshot date: 2026-08-04

## Scope and ownership

- Source: `Thepolyxsupershow 6th Draft Source`.
- Publisher declaration: Benedikt Eickhoff declares possession and copyright of the manuscript material shown in this
  evidence.
- Public scope: one read-only `/threads` GUI result, including the uncertainty score/lane rack and Copilot result.
- Review: the publisher declared that the captured scope contains no personal data, third-party material, credentials,
  or secrets. No raw FountainStore export or private runtime source is included.
- Image treatment: full fidelity. The asset is not obfuscated because the declared purpose is to show the actual
  reading surface and the publisher owns the displayed manuscript material.

## Drive

1. Started Reframe from the managed store `/tmp/reframe-polyx-courier-live-20260804.fountainstore` with flagship seed
   disabled.
2. Opened AX manuscript `library-manuscript-fixture`.
3. Confirmed AX composer `studio-chat-input` and sent `/threads` through `studio-chat-send`.
4. Confirmed the score was disclosed by default: `story-uncertainty-band`, `uncertainty-map-viewport`,
   `uncertainty-lane-storifyStructure`, and `uncertainty-lane-storifyOpenQuestions` were present in the AX tree.
5. Confirmed the result and asynchronous terminal activity through `chat-row-message-*` and
   `copilot-capability-activity`.

## Authorities

- Visual: CoreGraphics window ID `27039`; capture `threads-live-polyx-courier-20260804.png` (3840×2160).
- Behavioral: FountainStore lifecycle `copilot:capability-event:fixture:e4125a02-2b1c-4b5b-a15c-9ba070574fb2`, with
  phases `requested → accepted → running → succeeded`.
- Result: five open questions; `/threads` was read-only and did not mutate the manuscript or author baseline.
- Release boundary: development/live-accepted slash origin only; no released App build is claimed.
