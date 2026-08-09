# `/readings` live acceptance — Ulysses, episode 15 (Circe)

Snapshot date: 2026-08-09

## Scope and ownership

- Source: James Joyce, *Ulysses*, episode 15 (Circe), lines 20051–25573 of the manuscript source document. The text
  is in the public domain and is assembled by Reframe's own corpus API; the reading questions and the comparison
  narration in the capture are Reframe's own output.
- Public scope: one read-only `/readings` GUI result, the disclosed uncertainty score, and two visible manuscript
  beats.
- Review: the captured scope contains no personal data, third-party licensed material, credentials, or secrets. No
  raw FountainStore export and no runtime source are published.
- Image treatment: full fidelity, under the publisher's direction that screenshots may be published.

## The state the command was asked to compare

The store held two persisted readings of the **same** Circe span, made weeks apart by different readers:

| run | reader | windows | grounding identity | scope |
| --- | --- | ---: | --- | --- |
| `reframe-ulysses:stf-9512cc87` | `openai` | 2 | `83651a50…e008ec0a` | ll. 20051–25573 |
| `reframe-ulysses:stf-66e626a2` | `codex` | 11 | `83651a50…e008ec0a` | ll. 20051–25573 |

Both carry the **same** grounding identity. That is the case governance chapter 46 rules 20–21 exist for, and it is
why this drive was worth publishing: the honest report here is not a finding.

## Drive

1. Same launch, staging, and chapter-opening sequence as [`verified-ground.md`](verified-ground.md), on the same
   store copy `~/circe-book-drive.fountainstore`, with the writer's key turned to on-device first.
2. Sent `/readings` through `studio-chat-input` and `studio-chat-send`.

## Authorities

- **Visual** — CoreGraphics window ID `42036` (bounds `127,-1080 1920x1080`); capture
  `readings-live-ulysses-circe-20260809.png` (3840×2160).
- **Semantic (AX)** — the reply rendered as `chat-row-message-9F91C476-16B7-49BD-BFA7-5951F98067D0` inside
  `studio-chat-scroll`, alongside the disclosed score (`story-uncertainty-band`, value `20`) and the reading's
  provenance strip (`reading-provenance-quality`).
- **Behavioural (FountainStore)** — the persisted turn `chat:reframe-ulysses:round:20`
  (`createdAt 2026-08-09T18:00:38Z`, `durationMs` 15814). The report's numbers are traceable to the two
  `storify:run:reframe-ulysses:*` documents and their `storify:window:*` children; nothing is drawn from the
  transcript.

## Result

The report opened with the count of readings, then stated the thing that makes it honest:

> Both readings went through the SAME lens, so nothing below is the effect of reading differently — it is how much
> this reader varies between two passes over the same lines.

It then listed, addressed to their lines:

- **held open by both passes** — three questions, including *"Will Bloom survive the confrontation with Mrs. Breen?"*
  and *"What street is Bloom on?"*;
- **only the earlier reading held these open** — fourteen questions the later pass settled or stopped asking;
- **only the later reading holds these open** — thirty-three questions the second pass opened;
- **the same lines divided differently** — twelve line numbers where one reading cut a beat and the other did not.

It closed by handing the writer the material rather than a verdict:

> The passage genuinely leaves open whether Bloom will survive the confrontation with Mrs. Breen and what street
> Bloom is on. The other questions were not stable across readings, so they appear to be artifacts of the reading
> process rather than securely supported ambiguities.

## Repetition

Repeated on a second launch of the same store (`chat:reframe-ulysses:round:22`, `2026-08-09T18:06:20Z`). The
structural report was byte-identical; the closing reflection was re-reasoned and reached the same conclusion,
including the third honest outcome in the writer's terms:

> …beyond that, the readings agree too closely to support a more specific lens.

## Cost

No paid model call was recorded for either `/readings` turn. Across the whole session only two `telemetry:llm`
records and two `llm-cache` entries were written, all four at 17:58–17:59 UTC and all belonging to the preceding
`stay on device` instruction. The comparison itself is arithmetic over persisted readings; the closing paragraph was
reasoned on the on-device lane the writer had just elected.

## Boundary

`/readings` is **local orchestration**, not a governed capability identity: it is entry 12 of the development command
catalog, routed inside the runtime rather than through the Copilot capability registry, so it has no
`copilot:capability:*` aggregate and no AX capability-activity projection. Its proof is the persisted round and the
two readings it is computed from. This evidence therefore does not add a capability to the registry, and the release
manifest remains `no-released-build` with an empty allow-list.
