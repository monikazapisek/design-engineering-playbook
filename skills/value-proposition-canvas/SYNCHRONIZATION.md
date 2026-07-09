# Synchronization

This skill intentionally exists in **two locations** in this monorepo:

1. `_meta-space/.agents/skills/value-proposition-canvas/` — **source of truth** (authoritative; edit here first)
2. `_meta-space/projects/design-engineering-playbook/skills/value-proposition-canvas/` — public release copy (in the `design-engineering-playbook` subrepo that ships to GitHub)

The reason for the duplication: the `design-engineering-playbook` subrepo is itself a separate GitHub repo (`monikazapisekstudio/design-engineering-playbook`) and is periodically snapshotted out of the monorepo. Skills intended for public release live in `design-engineering-playbook/skills/`.

## Origin note (this skill is non-standard)

This skill was created **directly in the public playbook copy** on 2026-07-09, in a single authoring session that combined the original Osterwalder framework with secondary sources (IxDF, Steve Blank, Gothelf, Ries, etc.) and prior conversation context. It is being mirrored to the source-of-truth location (`.agents/skills/value-proposition-canvas/`) as part of the publication prep.

**Future edits must originate in `.agents/skills/value-proposition-canvas/`**, not the public copy. This brings the skill into the normal edit-then-mirror flow used by the other mature skills (`kano-model-strategist`, `legible-agent-output`).

## How to keep them in sync

When you edit the skill:

1. Edit the **source of truth** in `.agents/skills/value-proposition-canvas/`.
2. Run the skill's quality checklist (in `SKILL.md`, section "Quality Checklist") to confirm structural integrity.
3. Mirror the changes to `projects/design-engineering-playbook/skills/value-proposition-canvas/` (Copy-Item -Recurse from PowerShell, or `cp -r` from bash).
4. Confirm parity by re-running the quality checklist on the public copy.

## Cursor mirror

There is a third copy of `SKILL.md` at:

3. `_meta-space/projects/design-engineering-playbook/.cursor/skills/value-proposition-canvas/SKILL.md`

This is the Cursor-specific subset: only the `SKILL.md` (the agent-facing working document) is mirrored. `references/`, `examples/`, and the meta files (`README.md`, `ATTRIBUTION.md`, `LICENSE`, `SYNCHRONIZATION.md`, `EVIDENCE.md` when it exists) live in the playbook copy only. Cursor loads the `SKILL.md` directly; the other tools (Claude Code, OpenCode) follow the `references/` and `examples/` paths declared in the SKILL frontmatter.

When you update `SKILL.md`, mirror it to the Cursor copy at the same time as the playbook copy.

## What to NOT do

- **Do not edit the public copy first.** Edits must originate in the source of truth; the public copy is downstream.
- **Do not delete one copy "to dedupe."** Both copies serve different audiences: the source of truth is what the local Mavis agent runtime loads; the public copy is what GitHub users see. Removing either breaks that audience.
- **Do not symlink.** Windows symlinks for skill directories are flaky across Git, Drive, and OneDrive syncing. Two real copies is more reliable.
- **Do not add `README.md` to the source-of-truth copy.** The README is the GitHub public-landing page and exists only in the playbook copy. The source-of-truth copy is loaded by the local agent runtime and has no need for human-facing landing copy.
- **Do not add `EVIDENCE.md` to either copy until Path B eval has been run.** The eval results go in `EVIDENCE.md` only after a real test, not as a placeholder.
