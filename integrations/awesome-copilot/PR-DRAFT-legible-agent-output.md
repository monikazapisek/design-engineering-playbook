# PR draft: Add legible-agent-output skill to awesome-copilot

> Copy-paste this into the PR body when opening the PR.

## What

Adds `legible-agent-output` to `skills/` in `github/awesome-copilot`. The skill enforces plain-language output from AI agents — replaces opaque codes (A127, ENOENT), framework jargon, raw error strings, and bare percentages with human-readable titles, status messages, and error descriptions.

## Why

AI agents routinely surface internal identifiers and framework vocabulary as if they were human-readable labels. This is a documented UX failure in agentic AI, not a quirk. The pattern is established in agentic-UX literature under names like "Intent Preview" (Smashing Magazine) and "Invisible actions / Unclear state" (Hatchworks).

A senior baseline (no skill) running a realistic eval prompt leaked the server file path `/tmp/profile.jpg` in an error message. The same agent with the skill loaded correctly translated to: *"Your profile photo couldn't be uploaded because the file is missing or was moved."* No leak. See `EVIDENCE.md` in the upstream playbook for the full Path B eval.

## File added

- `skills/legible-agent-output.skill.md` — the skill file, formatted per the awesome-copilot pattern (mirrors `integrations/awesome-copilot/legible-agent-output.skill.md` in the upstream repo `monikazapisekstudio/design-engineering-playbook`)

## Source

Canonical source: https://github.com/monikazapisekstudio/design-engineering-playbook/tree/main/skills/legible-agent-output

The skill ships with:
- 7 laws for plain-language user-facing strings
- 6-category failure-mode taxonomy
- 30 worked before/after transformations
- 3-prompt eval loop
- Anti-fluency and anti-sycophancy hardening (high-stakes skills)
- 6 published UX sources, all verified 2026-06-30
- Path B eval (with vs without skill) showing measurable improvement on error translation

## Tested with

Claude Sonnet 4.5 (Mavis / Claude Code). Designed for Claude Code, Codex, VS Code, OpenCode, Cursor, GitHub Copilot. No MCP, no external dependencies.

## Author

Monika Zapisek (Product Designer / Design Engineer, https://monikazapisek.com)
Project: Design Engineering Playbook
License: MIT

## Related PRs

- #2051 — agent-agile-master (pending)
- #2053 — kano-model-strategist + socratic-dialogue (pending)

This PR continues the same submission pattern. Order in strategy-and-roadmap.md §4.3: agent-agile-master → kano → socratic → **legible-agent-output**.

## Checklist

- [x] Skill has one clear `job` (single responsibility) — replace opaque codes/jargon with plain language
- [x] Frontmatter has `name` + `description` with "use when" AND "do NOT use" trigger phrases
- [x] Path B eval documented in upstream EVIDENCE.md
- [x] MIT license, `author: Monika Zapisek`, `project: Design Engineering Playbook` in frontmatter
- [x] Tested with Claude Sonnet 4.5 (Mavis / Claude Code)
- [x] Anti-fluency + anti-sycophancy hardening for high-stakes output
- [x] Source repository linked from frontmatter
- [x] Compatible with awesome-copilot frontmatter schema
