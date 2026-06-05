# Agent Instructions — skills/

You are working in the `skills/` directory of the Design Engineering Playbook.

## Rules

- Follow `skills-guideline.md` when creating or editing any skill.
- Every skill must have one clear job. Do not create multi-purpose skills.
- Create one folder per skill. The folder name must match the skill name in kebab-case.
- Every skill folder must contain `SKILL.md` — the source of truth for that skill.
- Optional subfolders (use only when the skill genuinely needs them):
  - `references/` — longer background material loaded on demand
  - `examples/` — sample outputs or format examples
  - `scripts/` — executable helpers, validators, or converters
- Do not add a per-skill `README.md` unless the user explicitly asks for it.
- Do not copy content from private workspaces directly (`agent-os`, `.claude`, `.agents`, `_vault`).
- Keep all content generic, public, and reusable.
- Avoid client-specific, personal, or secret data.
- Do not edit the root `README.md` without explicit user approval.
