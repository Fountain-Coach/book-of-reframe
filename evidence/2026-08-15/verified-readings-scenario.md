# `/readings` scenario acceptance — repeatable fixture drive

Snapshot date: 2026-08-15

This is the current governed scenario witness for `/readings`. It uses Reframe's small original fixture corpus so the
publication test is bounded and repeatable; the older Ulysses drive remains linked as historical product evidence.

## Contract

- Scenario: `readings-comparison`
- Sequence: request a paid-lane Storify reading, confirm it, repeat with restart, then run `/readings`.
- Prerequisite: the managed Store contains the declared fixture source document.
- Terminal proof: each reading has a distinct new `storify.source.start` execution reaching `succeeded`; `/readings`
  is observed in both AX and the persisted Store readback.

## Independent witness

- AX drove `studio-chat-input` and `studio-chat-send` for every step.
- The window was captured by CoreGraphics window ID, not display coordinates.
- The evidence bundle was bound to one Reframe PID, one managed Store, one verified executable, and source commit
  `94a7b327`.
- The paid lane was visible in the running app as “ChatGPT plan (Codex)”.

The runner requires a new lifecycle execution ID for each repeated reading step. Historical success from the first
reading cannot satisfy the second step.

## Result

The scenario completed its declared terminal sequence: two distinct Storify lifecycle executions succeeded and the
`/readings` comparison was observed through AX and Store readback. No manuscript edit or release promotion was part
of this acceptance.

Private raw Store exports, runtime source, local paths, credentials, and the fixture evidence image are not published.
