# The Book of Reframe — Development Command Atlas

Status: first verified inventory, 2026-08-03

This is the human-facing inventory of what the current development runtime knows: command spellings, aliases,
compatibility routes, conditional entries, and maintainer-facing tools. It is not the released App capability list.
See [`RELEASE-SURFACE.md`](RELEASE-SURFACE.md) for the named-build boundary.

## What the number means

The current local command catalog contains **95 command entries**:

- **92 available now** in the verified Ulysses session;
- **3 unavailable in that session** because their preconditions are absent;
- **3 available but `//`-only**, so they are not shown in the normal writer-facing palette.

These are command spellings, not independent product capabilities. Aliases and compatibility spellings count as
separate entries. The governed Copilot capability registry is the other side of the map: it currently contains 53
capability identities, 22 executable, 2 live-accepted, and 31 unavailable. One capability can have several commands, and some local
commands are orchestration, help, or compatibility surfaces rather than one IDL operation.

The Book keeps four projections separate: this development command inventory, the governed capability atlas, the
live-accepted evidence ledger, and the named-build release surface. A slash entry does not enter the released surface
merely because it appears here.

## How this inventory was verified

The list was read from the live `app.commands.discover` result, whose source is
`ReframeViewModel.slashCommandIndex`. The acceptance drive's sanitized snapshot is in
`evidence/2026-08-03/verified-command-catalog.md` with its accompanying proof record.

The terminal FountainStore proof reports `command.catalog.entries=95` and
`command.catalog.source=slashCommandIndex`. The catalog result was also inspected through AX as the
`command-results-all` scroll surface. “Available” means the runtime's current readiness evaluator accepted the
entry; it does not mean that every possible manuscript state or argument is valid.

## The command atlas

The number is the catalog position in the verified snapshot. “Alias” means the entry forwards to another command;
it is documented because writers may encounter it, but it is not a new capability.

### Re-author a beat

| # | Command | What it does |
|---:|---|---|
| 1 | `/modernize` | Move a beat to the present day while changing era and language. |
| 2 | `/adapt` | Recast a beat into another genre, style, world, or setting. |
| 3 | `/re-tone` | Shift a beat's mood or register while preserving its world and era. |
| 4 | `/translate` | Render a beat in another language without otherwise changing it. |
| 5 | `/develop` | Expand and deepen a beat while preserving era, setting, and intent. |
| 39 | `/rewrite` | Rewrite the current beat. |
| 40 | `/rewrite!` | Rewrite the current beat with the Codex CLI route. |
| 41 | `/rewrite-beat` | Force a beat rewrite. |

### Understand the manuscript and its world

| # | Command | What it does |
|---:|---|---|
| 10 | `/world` | Show established identities, unresolved names, references, and current wants in the manuscript world ledger. |
| 11 | `/threads` | Show the open question threads held by the current reading and what could close them. |
| 12 | `/readings` | Compare manuscript readings: what stayed open and what the next reading should look for. |
| 13 | `/noodles` | Explain the visible beat-to-composer citation-wire connections. |
| 77 | `/diff` | Show diff queries for draft, source, and beat history. |
| 80 | `/ask` | Ask a character a question using `NAME: question`. |
| 81 | `/interview` | Alias for `/ask`. |

### Inspect the live workspace

| # | Command | What it does |
|---:|---|---|
| 6 | `/help` | Print the local command list without a model call. |
| 7 | `/version` | Print build metadata and the Git SHA when available. |
| 8 | `/commands` | Alias for `/help`; returns the governed structured command catalog. |
| 9 | `/about` | Compatibility alias for `/version`. |
| 14 | `/status` | Print source, pipeline, cost diagnostics, and active gateway notices. |
| 15 | `/context` | Compatibility alias for `/status`. |
| 16 | `/pipeline status` | Show terse pipeline truth: state, stage, blocker, current activity, and next action. |
| 17 | `/pipeline status verbose` | Show full stage details, flags, cohort eligibility, and dirty scope. |
| 18 | `/pipeline sla` | Show recent p50/p90 stage timings against chain budgets. |
| 19 | `/pipeline rerun` | Rerun a pipeline stage; usage is `/pipeline rerun <semantic\|storify\|continuity\|compose\|lora> [scope]`. |
| 20 | `/engine-room` | Pin the Engine Room in Chat for live stage status. |
| 21 | `/machine-room` | Compatibility alias for `/engine-room`. |
| 74 | `/analytics` | Inspect chat rounds and telemetry while testing. |
| 75 | `/analytics!` | Open analytics controls or toggle full capture with `on`, `off`, or `status`. |
| 95 | `/store-health` | Probe FountainStore health and distinguish `NOT_FOUND` from `READ_FAILED`. |

### Grounding and the reading stance

| # | Command | What it does |
|---:|---|---|
| 22 | `/baseline` | Explain the Author Baseline, Reader Lens, their gates, and Workbench navigation. |
| 23 | `/baseline workbench` | Open the side-by-side Author Baseline and Reader Lens editors. |
| 24 | `/baseline storify` | Open the Storify Editor as the recommended next step after baselines. |
| 25 | `/baseline beats` | Legacy alias for `/baseline storify`. |
| 26 | `/baseline gate` | Open the baseline gate. |
| 27 | `/baseline author` | Open the Author Baseline. |
| 28 | `/baseline reader` | Open the Reader Lens. |
| 29 | `/lens` | Alias for `/baseline reader`. |

### Beats, Storify, and the Cut Script

| # | Command | What it does |
|---:|---|---|
| 30 | `/fork` | Fork the manuscript from the current draft. |
| 31 | `/beats` | Explain the Storify/Cut Script command family. |
| 32 | `/beats panel` | Open the Cut Script. |
| 33 | `/beats start` | Alias for starting Storify source processing automatically. |
| 34 | `/beats status` | Show beat/Storify readiness status. |
| 35 | `/beats refresh` | Alias for the Storify source run. |
| 36 | `/beats arc` | Alias for the continuity-scene operation. |
| 37 | `/beats repair` | Alias for Storify assignment repair. |
| 38 | `/beats context` | Alias for the Storify Editor. |
| 42 | `/storify` | Explain the Storify command family. |
| 43 | `/storify!` | Run the Storify pass from noise toward an arc. |
| 44 | `/storify! assign current` | Reassign the current Cut Script unit. |
| 45 | `/storify! assign full` | Reassign the full Cut Script. |
| 46 | `/storify! assign status` | Show the staged assignment. |
| 47 | `/storify! assign apply` | Apply the staged assignment. |
| 48 | `/storify! assign discard` | Discard the staged assignment. |
| 49 | `/storify! draft auto` | Start a chunked Storify draft run. |
| 50 | `/storify! draft auto restart` | Restart the Storify draft run. |
| 51 | `/storify! source auto` | Start a chunked Storify source run. |
| 52 | `/storify! source auto restart` | Restart the Storify source run. |
| 53 | `/storify! guide on` | Enable the Storify guide host. |
| 54 | `/storify! guide apply` | Apply a guide proposal. |
| 55 | `/storify! guide next` | Move to the next guide proposal. |
| 56 | `/storify! guide status` | Show guide-host status. |
| 57 | `/storify! guide off` | Disable the Storify guide host. |
| 58 | `/storify! stop` | Stop the current Storify chunked run. **Unavailable until a Storify run is active.** |
| 59 | `/storify machine-room` | Legacy alias for opening the Storify Editor. |

### Continuity

| # | Command | What it does |
|---:|---|---|
| 60 | `/continuity` | Explain continuity-audit commands. |
| 61 | `/continuity!` | Run a continuity audit across source, scene, or draft scope. |
| 62 | `/continuity machine-room` | Open the Continuity Machine Room window. |
| 69 | `/continue` | Continue the last continuity run, or accept a supplied resume token. |
| 70 | `/continue auto` | Page continuity windows internally until completion. |
| 71 | `/continue stop` | Cancel the current continuity auto-paging chain. |
| 72 | `/continue!` | Alias for `/continue`. |
| 73 | `/resume` | Alias for `/continue`. |

### Fountain structure and import tools

| # | Command | What it does |
|---:|---|---|
| 63 | `/fountain` | Explain Fountain lint and fix commands. |
| 64 | `/fountain!` | Show Fountain lint/fix commands. |
| 65 | `/fountain! lint` | Lint the current unit. |
| 66 | `/fountain! fix` | Fix the current unit. |
| 67 | `/fountain! lint full` | Lint the full Cut Script. |
| 68 | `/fountain! fix full` | Fix the full Cut Script. |
| 76 | `/facebook` | Use Facebook import tools for self posts, text, and images. |
| 78 | `/describe` | Describe attached images into image beats. **Unavailable until images are attached.** |
| 79 | `/describe!` | Describe image beats through the Codex CLI. **Unavailable until images are attached.** |

### Promotion and persistence

| # | Command | What it does |
|---:|---|---|
| 85 | `/promote help` | Show explicit promotion targets and usage. |
| 86 | `/promote task` | Persist a task artifact in the modernization pipeline. |
| 87 | `/promote arc` | Persist an arc-alignment note with provenance. |
| 88 | `/promote objective` | Persist rewrite intent for downstream pipeline use. |
| 89 | `/promote decision` | Persist an explicit decision record from chat. |
| 90 | `/promote task last` | Use the latest assistant response as the promotion payload. |
| 91 | `/store-path` | Switch the active store path; use `/store-fresh` to mark a blank store. |
| 92 | `/storepath` | Alias for `/store-path`. |
| 93 | `/store-fresh` | Switch to a fresh store path and skip demo installation. |
| 94 | `/fresh-store` | Alias for `/store-fresh`. |

### Maintainer-only UI learning

| # | Command | What it does |
|---:|---|---|
| 82 | `/gui-learn` | Record short claims about UI or pipeline behavior. `//`-only. |
| 83 | `/gui-learning` | Alias for `/gui-learn`. `//`-only. |
| 84 | `/gui-remember` | Alias for `/gui-learn`. `//`-only. |

## What this atlas does not yet claim

This snapshot proves enumeration and current readiness, not a successful end-to-end run of all 92 available
commands. The next documentation pass should add, for each non-alias command:

1. a plain-language example;
2. its governed capability identity, if one exists;
3. required state and confirmation/paid-lane behavior;
4. the persisted FountainStore effect;
5. AX result identifiers and a live acceptance reference;
6. a short “when to use this” explanation for writers.

That is the difference between a command list and the Book of Reframe: the list says what exists; the book teaches
what kind of work Reframe can do, what it needs, and how the writer can check that it happened.
