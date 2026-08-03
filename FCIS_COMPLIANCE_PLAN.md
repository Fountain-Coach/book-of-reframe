# FCIS Compliance Plan

## Goal and scope

Keep the Book of Reframe compliant with FCIS RFC 0001 while making every command page a truthful, visually legible,
live-drive-backed teaching artifact.

## Minimal-change strategy

Keep the existing catalog and capability atlas. Add only the FCIS declaration files, mirrored procedure contract,
command-page directory, and evidence inventory needed to prevent unsupported publication claims.

## Phased plan and acceptance criteria

### Phase 0: Safety

- Preserve the runtime repository as authority.
- Keep prompts, private store data, secrets, and local filesystem paths out of the book.
- Acceptance: `SOURCE.md` identifies reciprocal provenance and, for owned manuscript evidence, the explicit ownership,
  public-scope, and personal-data/third-party/secrets review.

### Phase 1: Required structure

- Maintain `AGENTS.md`, `PLANS.md`, `FCIS_AUDIT.md`, and this plan.
- Maintain byte-identical Codex and Claude maintenance skills in the source repository.
- Acceptance: the audit matrix passes layering, provenance, and skill-parity checks.

### Phase 2: Snapshot-gated command pages

- Drive each command through the governed live-drive path.
- Capture the result window by CoreGraphics window ID and retain AX and FountainStore proof.
- Generate a page only when all three evidence authorities are present; make the first non-empty line an alt-texted
  image.
- Acceptance: the page validator passes and the evidence inventory has no false `live-accepted` entries.

### Phase 3: Validation and enforcement

- Run the catalog exporter, command-page validator, capability audit, governance checks, and `git diff --check`.
- Review the rendered snapshots at reading size; AX remains the semantic check.
- Acceptance: publication PR records the evidence IDs and does not mark pending commands complete.

## Current status

Phase 0 and Phase 1 are complete. Phase 2 is complete for `/commands`; the other entries are pending governed drives.
Phase 3 is the publication review gate for every update.
