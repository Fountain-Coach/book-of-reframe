# `/pipeline status` — governed live acceptance

Date: 2026-08-15

Scenario: `pipeline-status` · capability: `pipeline.status` · source revision: `55461f0f`

The scenario was executed three times through the governed AX runner against one isolated, authority-managed
FountainStore and one verified Reframe executable. The window was resolved by CoreGraphics window ID and placed on
the attached external display before interaction.

Observed authorities agreed:

- AX exposed `studio-chat-input`, `studio-chat-send`, and assistant responses containing `PIPELINE STATUS`.
- FountainStore recorded `pipeline.status` as `requested → accepted → running → succeeded` for all three runs.
- The result was read-only and reported the actual empty active-manuscript state: source missing, with `Storify Source
  Auto` as the next action.
- The window-ID capture shows the same result on the external display.

The scenario is live-accepted for the diagnostic command. This evidence does not claim source import, Storify, or a
released App surface.

The preceding 2026-08-03 record remains historical legacy evidence.
