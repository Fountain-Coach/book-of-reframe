# `/ground` live acceptance — Ulysses, episode 15 (Circe)

Snapshot date: 2026-08-09

## Scope and ownership

- Source: James Joyce, *Ulysses*, episode 15 (Circe), lines 20051–25573 of the manuscript source document. The text
  is in the public domain and is assembled by Reframe's own corpus API; the Copilot text in the capture is Reframe's
  own output.
- Public scope: one read-only `/ground` GUI result, the disclosed uncertainty score, and two visible manuscript
  beats.
- Review: the captured scope contains no personal data, third-party licensed material, credentials, or secrets. No
  raw FountainStore export and no runtime source are published.
- Image treatment: full fidelity. The publisher directed that screenshots may be published; the policy requires a
  rights and scope review, not automatic obfuscation.

## Drive

1. Copied the writer's Circe drive store to `~/circe-book-drive.fountainstore` so the original keeps its pristine
   two-reading state as the reproducible baseline.
2. Launched Reframe with `MODERNIZATION_MANAGED_STORE_PATH=~/circe-book-drive.fountainstore` and
   `REFRAME_DISABLE_FLAGSHIP_SEED=1`. There is no `.app` bundle; the SPM binary is the app.
3. Placed the window on the attached external display through AX (`window place 127 -1080 1920 1080`), raised it,
   and entered native full screen there. AX reported `position=127,-1080 size=1920x1080 fullscreen=true`.
4. Opened the chapter by identity, not by pressing the manuscript: `library-chapters-toggle-reframe-ulysses` →
   `library-chapter-group-reframe-ulysses-odyssey` → `library-chapter-reframe-ulysses-15`
   (AX description: *Ulysses, chapter 15, Circe*).
5. Asked for the free lane before anything could spend: sent `stay on device`, and the Copilot answered
   *"I'll keep this work on your device."* What the store shows is the reply and the absence of any paid call
   afterwards; the provider state itself was not read back, so this record does not claim the lane was switched.
6. Sent `/ground` through `studio-chat-input` and `studio-chat-send`.

## Authorities

- **Visual** — CoreGraphics window ID `42036` (bounds `127,-1080 1920x1080`); capture
  `ground-live-ulysses-circe-20260809.png` (3840×2160).
- **Semantic (AX)** — the result was projected as `copilot-capability-activity`, reading
  *"Propose a reading lens · succeeded"*, with `copilot-capability-details` as its disclosure.
- **Behavioural (FountainStore)** — capability aggregate
  `copilot:capability:reframe-ulysses:41e02fb6-aed9-45f7-a891-67fc9737a60c`:

  | field | value |
  | --- | --- |
  | `capabilityId` | `prep.grounding.propose` |
  | `origin` | `slash` |
  | `phase` | `succeeded` |
  | `terminal` | `true` |
  | `eventCount` | 4 |
  | `occurredAt` | `2026-08-09T17:59:55Z` |
  | `runtimeState` | `grounding.proposal=false`, `grounding.changed=false`, `grounding.blockedBy=readingHasHoles` |
  | `axProjectionIdentifiers` | `copilot-capability-activity` |

  The lifecycle events are `copilot:capability-event:reframe-ulysses:41e02fb6-…:000000–000003`. The persisted turn
  is `chat:reframe-ulysses:round:19`.

## Result

`/ground` refused to propose a lens, and said why:

> I can't ground this reading yet, and the reason is worth seeing rather than working around. This reading is
> carrying 1 hole(s) — places where nothing was read, or where the reading broke:
>
> - [failure] lines 22744–25573: Unread stretch · lines 22744–25573 — This stretch was never read — 2830 lines with
>   no reading behind them. Nothing here is settled, and nothing here is ambiguous; it is simply unknown. (would be
>   closed by: the manuscript: read this stretch)
>
> A grounding lens changes how the work is READ; it cannot close a gap where the work has not been read at all.
> There are also 8 open question(s) in this reading, but they are not what to change first: a reading lens changes
> how the work is attended to, and it cannot fill a stretch that has no reading behind it. Nothing has changed.

The runtime state confirms the prose: no proposal was persisted, no grounding identity changed, and the block is
named (`readingHasHoles`). This is the governed behaviour, not a failure of the command — a score-derived lens is an
offer, and an offer over an unread stretch would be a claim the evidence cannot support.

## Repetition

The reading-score computation behind the command was repeated on a second launch of the same store and reproduced
identically: `[GROUNDING-PROPOSAL] run=reframe-ulysses:stf-66e626a2 lanes=2 items=20 gaps=9 holes=1` on both passes,
with the same refusal text persisted as `chat:reframe-ulysses:round:21`.

## Cost

No paid model call was recorded for this turn. The two `telemetry:llm` records written during the session
(`091b66c9-…`, `525ce2be-…`, purposes `staged-studio-intent` and `chat`) both belong to the preceding
`stay on device` instruction at 17:58 UTC. `/ground` at 17:59:55 added none: the stance is derived from the
persisted UncertaintyScore, not from a new reading.

## Boundary

This is development, live-accepted evidence for the slash-command origin of `prep.grounding.propose`. It does not
promote the capability into a released App surface — the release manifest remains `no-released-build` with an empty
allow-list — and it does not claim live acceptance for the natural-language origin or for the acceptance half of the
grounding flow (a writer confirming a proposed lens), which this reading's holes made unreachable.
