# Command pages

Every file in this directory begins with an alt-texted GUI snapshot showing the command execute and its result. The
image is visual evidence only: the linked live drive must also provide AX semantics and persisted FountainStore
proof.

The maintenance skill refuses to publish a page without all three authorities. The complete 95-entry inventory stays
in [`../COMMAND-ATLAS.md`](../COMMAND-ATLAS.md); commands not yet individually driven are listed in
[`../evidence/2026-08-03/command-evidence.json`](../evidence/2026-08-03/command-evidence.json).

## Documented commands

| Command | What it is for | Evidence |
| --- | --- | --- |
| [`/pipeline status`](pipeline-status.md) | Current pipeline truth: state, stage, blocker, next action. | `../evidence/2026-08-03/verified-pipeline-status.md` |
| [`/threads`](threads.md) | The questions the current reading is still holding open. | `../evidence/2026-08-04/verified-threads.md` |
| [`/ground`](ground.md) | Propose a reading lens from what the reading is unsure of — or say why it cannot. | `../evidence/2026-08-09/verified-ground.md` |
| [`/readings`](readings.md) | Compare two readings of the same lines: what held, what moved, what it cannot tell. | `../evidence/2026-08-09/verified-readings.md` |

`/ground` is a slash alias of the governed capability `prep.grounding.propose`; `/readings`, `/threads`, and
`/pipeline status` are catalog entries. None of them is in a released App surface — see
[`../RELEASE-SURFACE.md`](../RELEASE-SURFACE.md).
