# `/pipeline status` — live acceptance evidence

Date: 2026-08-03

## Scenario

- A fresh fixture FountainStore bundle was built with `Scripts/build-fixture-store`.
- Reframe was launched with `MODERNIZATION_MANAGED_STORE_PATH=<fixture>` and `REFRAME_DISABLE_FLAGSHIP_SEED=1`.
- The fixture manuscript was opened through the library AX control.
- `/pipeline status` was entered through `studio-chat-input` and submitted through `studio-chat-send`.
- The window was resolved by CoreGraphics window ID, moved to the attached secondary 1920×1080 display, entered full
  screen, and captured after the result appeared.
- The same command was repeated until three persisted rounds existed.

## AX proof

The result exposed these semantic controls and values:

- `chat-row-message-*`: user prompt `/pipeline status` and the assistant response beginning `PIPELINE STATUS`.
- `copilot-capability-activity`: `Show pipeline status. Phase succeeded.`
- `copilot-activity-details`: `Activity details` disclosure control.

The result was therefore readable and stateful in AX; the screenshot is not the semantic authority.

## FountainStore proof

`ReframeStoreDump <fixture> lifecycle` returned 15 lifecycle documents: three complete
`pipeline.status` sequences, each `requested → accepted → running → succeeded`, with origin `slash`.

The succeeded summaries were:

`Pipeline truth: ✓ Ingestion -> ✓ Parse + Convert -> ✓ Translate -> ○ Baselines -> ○ Reading (full) -> ○ Storify Annotation -> ○ Continuity Audit (advisory) -> ✓ Editor Unlock`

`ReframeStoreDump <fixture> list --corpus fixture` returned three persisted chat rounds:
`chat:fixture:round:1`, `chat:fixture:round:2`, and `chat:fixture:round:3`.

The persisted round recorded `user.text=/pipeline status`, `viewContentMutated=false`, and `storedDraft=false`.

## Visual proof

- Capture: [`pipeline-status-live-20260803.png`](pipeline-status-live-20260803.png)
- Authority: CoreGraphics window-ID capture, not a display-coordinate screenshot.

## Boundary

This is development-runtime evidence on the tiny fixture corpus. It is not evidence that the current App release
surface includes this command.
