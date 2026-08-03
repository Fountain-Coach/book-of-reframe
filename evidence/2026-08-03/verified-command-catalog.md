# Verified Reframe Command Catalog

Snapshot: 2026-08-03

- Entries: **95**
- Available in the captured runtime state: **92**
- Unavailable in the captured runtime state: **3**
- `//`-only entries: **3**
- Explicit aliases/compatibility spellings: **22**

This is a runtime projection, not the capability registry. Aliases are entries but not independent powers.

| # | Command | Title | Availability | Visibility | Detail |
|---:|---|---|---|---|---|
| 1 | `/modernize` | Reframe — Modernize | available | userFacing | Move a beat to the present day (contemporary era + language). |
| 2 | `/adapt` | Reframe — Adapt | available | userFacing | Recast a beat into a different genre, style, world, or setting. |
| 3 | `/re-tone` | Reframe — Re-tone | available | userFacing | Shift a beat's mood/register, keeping its world and era. |
| 4 | `/translate` | Reframe — Translate | available | userFacing | Render a beat in another language, otherwise unchanged. |
| 5 | `/develop` | Reframe — Develop | available | userFacing | Expand and deepen a beat, keeping its era, setting, and intent. |
| 6 | `/help` | Show command help | available | userFacing | Print a local command list (no model call). |
| 7 | `/version` | Show app version | available | userFacing | Print build metadata + git SHA (when available). |
| 8 | `/commands` | Alias for /help | available | userFacing |  |
| 9 | `/about` | Alias for /version | available | userFacing | Compatibility alias. |
| 10 | `/world` | Show the manuscript world ledger | available | userFacing | Report established identities, unresolved names, references, and current wants. |
| 11 | `/threads` | Show questions this reading holds open | available | userFacing | Report the current reading's open question threads and what could close them. |
| 12 | `/readings` | Compare manuscript readings | available | userFacing | Show what stayed open and what the next reading should look for. |
| 13 | `/noodles` | Show citation-wire status | available | userFacing | Explain the visible beat-to-composer citation connections. |
| 14 | `/status` | Show system status | available | userFacing | Print source/pipeline/cost diagnostics and active gateway notices. |
| 15 | `/context` | Alias for /status | available | userFacing | Compatibility alias. |
| 16 | `/pipeline status` | Show chain pipeline status | available | userFacing | Terse truth view (state, stage, blocker, current activity, next action). |
| 17 | `/pipeline status verbose` | Show verbose pipeline status | available | userFacing | Full stage details, flags, cohort eligibility, and dirty scope. |
| 18 | `/pipeline sla` | Show SLA metrics | available | userFacing | Recent p50/p90 stage timings against chain budgets. |
| 19 | `/pipeline rerun` | Rerun pipeline stage | available | userFacing | Use: /pipeline rerun <semantic\|storify\|continuity\|compose\|lora> [scope]. |
| 20 | `/engine-room` | Open Engine Room panel | available | userFacing | Pin Engine Room in Chat for live stage status. |
| 21 | `/machine-room` | Alias for /engine-room (compat) | available | userFacing | Compatibility alias. |
| 22 | `/baseline` | Baselines help | available | userFacing | Author baseline + Reader lens gates and Workbench navigation. |
| 23 | `/baseline workbench` | Open Baseline Workbench | available | userFacing | Side-by-side Author baseline + Reader lens editors. |
| 24 | `/baseline storify` | Open Storify Editor | available | userFacing | Recommended next step after baselines (second-pass semantic filtering). |
| 25 | `/baseline beats` | Legacy alias: Baseline -> Storify | available | userFacing | Compatibility alias; use /baseline storify. |
| 26 | `/baseline gate` | Open baseline gate | available | userFacing | Focuses Baselines tab and prepares gate requirements. |
| 27 | `/baseline author` | Open author baseline | available | userFacing | Opens Baseline Workbench (writer-facing constraints). |
| 28 | `/baseline reader` | Open reader lens | available | userFacing | Opens Baseline Workbench (reader-facing lens). |
| 29 | `/lens` | Alias for /baseline reader | available | userFacing |  |
| 30 | `/fork` | Fork manuscript from draft | available | userFacing | Create a new manuscript where Source == current Draft. |
| 31 | `/beats` | Storify/Cut Script aliases | available | userFacing | Compatibility commands routed to Storify and continuity. |
| 32 | `/beats panel` | Alias: open Cut Script | available | userFacing | Opens the Cut Script workbench. |
| 33 | `/beats start` | Alias: Storify source auto | available | userFacing | Runs /storify! source auto. |
| 34 | `/beats status` | Alias readiness status | available | userFacing | Shows Storify/Cut Script readiness summary. |
| 35 | `/beats refresh` | Alias: Storify source | available | userFacing | Runs /storify! source. |
| 36 | `/beats arc` | Alias: continuity scene | available | userFacing | Runs /continuity! scene. |
| 37 | `/beats repair` | Alias: Storify assign | available | userFacing | Runs /storify! assign current (or full with index). |
| 38 | `/beats context` | Alias: Storify Editor | available | userFacing | Opens Storify Editor (machine-room alias). |
| 39 | `/rewrite` | Rewrite the current beat | available | userFacing | Uses the default writer route. |
| 40 | `/rewrite!` | Rewrite with Codex CLI | available | userFacing | Requires Codex CLI installed + signed in. |
| 41 | `/rewrite-beat` | Force a beat rewrite | available | userFacing | Skips image-beat rewrite and targets the selected beat. |
| 42 | `/storify` | Storify help | available | userFacing | Print the Storify usage guide. |
| 43 | `/storify!` | Storify pass (noise → arc) | available | userFacing | Run on draft/source to extract signal + ordering. |
| 44 | `/storify! assign current` | Reassign current unit | available | userFacing | Repost selected Cut Script unit to Storify and log assignment reasoning. |
| 45 | `/storify! assign full` | Reassign full cut script | available | userFacing | Repost full Cut Script to Storify and log assignment reasoning. |
| 46 | `/storify! assign status` | Show staged assignment | available | userFacing | Report staged assignment patch status before apply/discard. |
| 47 | `/storify! assign apply` | Apply staged assignment | available | userFacing | Apply staged assignment patch to the active unit mapping. |
| 48 | `/storify! assign discard` | Discard staged assignment | available | userFacing | Discard staged assignment patch and keep current mapping. |
| 49 | `/storify! draft auto` | Storify chunked run | available | userFacing | Run draft chunks internally until completion. |
| 50 | `/storify! draft auto restart` | Restart Storify draft run | available | userFacing | Ignore saved continue points and read the draft scope from its beginning. Add `max N` to bound passages. |
| 51 | `/storify! source auto` | Storify source chunked run | available | userFacing | Run source chunks internally until completion and write Storify annotations into source. |
| 52 | `/storify! source auto restart` | Restart Storify source run | available | userFacing | Ignore saved continue points and read the source scope from its beginning. Add `max N` to bound passages. |
| 53 | `/storify! guide on` | Enable Storify guide host | available | userFacing | Turns on guided semantic window navigation. |
| 54 | `/storify! guide apply` | Apply guide proposal | available | userFacing | Focuses the currently proposed guide window and advances. |
| 55 | `/storify! guide next` | Next guide proposal | available | userFacing | Skips current guide proposal and suggests the next window. |
| 56 | `/storify! guide status` | Guide host status | available | userFacing | Shows guide state and current proposal. |
| 57 | `/storify! guide off` | Disable Storify guide host | available | userFacing | Turns off guided semantic window navigation. |
| 58 | `/storify! stop` | Stop Storify chunked run | unavailable: No Storify run is active. | userFacing | Cancel the current Storify chunked run. |
| 59 | `/storify machine-room` | Legacy alias: Open Storify Editor | available | userFacing | Compatibility alias; opens Storify Editor. |
| 60 | `/continuity` | Continuity audit help | available | userFacing | Character/persona consistency report with paging + resume tokens. |
| 61 | `/continuity!` | Continuity audit (source/scene/draft) | available | userFacing | Reports anchors + contradictions. FYI: “scene” derives from INT./EXT. headings; if none, it collapses to scene:preface. |
| 62 | `/continuity machine-room` | Open Continuity Machine Room window | available | userFacing | Show the latest continuity audit as a structured window (Pipeline / Characters / Contradictions). |
| 63 | `/fountain` | Fountain lint/fix help | available | userFacing | Validity gate tools for Cut Script save/apply. |
| 64 | `/fountain!` | Fountain lint/fix commands | available | userFacing | Run structural lint/fix for current unit or full script. |
| 65 | `/fountain! lint` | Lint Current Unit | available | userFacing | Run validity checks on the selected unit. |
| 66 | `/fountain! fix` | Fix Current Unit | available | userFacing | Apply safe structural fixes to the selected unit. |
| 67 | `/fountain! lint full` | Lint Full Cut Script | available | userFacing | Run validity checks across all units. |
| 68 | `/fountain! fix full` | Fix Full Cut Script | available | userFacing | Apply safe structural fixes across all units. |
| 69 | `/continue` | Continue last continuity run | available | userFacing | Uses the last resume token (or provide one). |
| 70 | `/continue auto` | Auto-continue continuity run | available | userFacing | Page continuity windows internally until completion. |
| 71 | `/continue stop` | Stop continuity auto paging | available | userFacing | Cancel the current continuity chain reaction. |
| 72 | `/continue!` | Alias for /continue | available | userFacing |  |
| 73 | `/resume` | Alias for /continue | available | userFacing |  |
| 74 | `/analytics` | Analytics help | available | userFacing | Inspect chat rounds + telemetry while testing. |
| 75 | `/analytics!` | Analytics controls | available | userFacing | Open sheet or toggle full capture (on/off/status). |
| 76 | `/facebook` | Facebook import tools | available | userFacing | status, import, more, clear (self posts; text + images). |
| 77 | `/diff` | Diff help | available | userFacing | Shows diff queries for draft/source/beat history. |
| 78 | `/describe` | Describe attached images into image beats | unavailable: Attach at least one image first. | userFacing | Attach images first; optional instruction after the command. |
| 79 | `/describe!` | Describe image beats with Codex CLI | unavailable: Attach at least one image first. | userFacing | Attach images first; requires Codex CLI. |
| 80 | `/ask` | Ask a character | available | userFacing | Format: /ask NAME: question (or /interview NAME: question). |
| 81 | `/interview` | Alias for /ask | available | userFacing |  |
| 82 | `/gui-learn` | Record GUI learning claims | available | fullCatalogOnly | Store short claims about the UI/pipeline behavior. |
| 83 | `/gui-learning` | Alias for /gui-learn | available | fullCatalogOnly |  |
| 84 | `/gui-remember` | Alias for /gui-learn | available | fullCatalogOnly |  |
| 85 | `/promote help` | Promotion command help | available | userFacing | Show explicit promote targets and usage. |
| 86 | `/promote task` | Promote to Task | available | userFacing | Persist a task artifact in the modernization pipeline. |
| 87 | `/promote arc` | Promote to Arc Note | available | userFacing | Persist an arc-alignment note with provenance. |
| 88 | `/promote objective` | Promote to Rewrite Objective | available | userFacing | Persist rewrite intent for downstream pipeline use. |
| 89 | `/promote decision` | Promote to Decision Record | available | userFacing | Persist an explicit decision record from chat. |
| 90 | `/promote task last` | Promote latest assistant text | available | userFacing | Uses the latest assistant response as promotion payload. |
| 91 | `/store-path` | Switch store path | available | userFacing | Use /store-fresh to mark as a blank store. |
| 92 | `/storepath` | Alias for /store-path | available | userFacing |  |
| 93 | `/store-fresh` | Switch to a fresh store path | available | userFacing | Marks the store as fresh (skips demo install). |
| 94 | `/fresh-store` | Alias for /store-fresh | available | userFacing |  |
| 95 | `/store-health` | Probe FountainStore health | available | userFacing | Checks source/baseline/memory docs and distinguishes NOT_FOUND vs READ_FAILED. |
