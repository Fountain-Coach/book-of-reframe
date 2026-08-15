# `/threads` — governed live acceptance

Date: 2026-08-15

Scenario: `threads` · capability: `manuscript.reading.inspect` · source revision: `6ba5e2f1`

The reusable scenario was executed once through the governed AX runner against one isolated, authority-managed
FountainStore and one verified Reframe executable. The scenario submitted `/threads` through the semantic composer,
waited for the uncertainty result, and then waited for the declared `manuscript.reading.inspect` terminal phase.

Observed authorities agreed:

- AX exposed the terminal uncertainty result through `story-uncertainty-band`, with the value `What this reading is
  unsure of. 14 open questions.`
- FountainStore recorded `manuscript.reading.inspect` as `requested → accepted → running → succeeded`.
- The CoreGraphics window-ID capture shows the same terminal Reframe surface on the attached external display.
- The command was read-only; no manuscript or author-baseline mutation was claimed.

The scenario is live-accepted for the `/threads` slash origin in development. This does not claim natural-language
origin parity, a complete Storify run, or a released App capability. The 2026-08-03 and 2026-08-04 records remain
historical legacy evidence.
