# Agent Instructions

This repository is an AI-native design engineering workspace.

When working in this repo:

- treat `README.md` as the public positioning source of truth
- use `playbook/` for long-form methodology
- use `skills/` for reusable workflows
- use `rules/` for operating guardrails
- use `commands/` for repeatable agent actions
- use `prompts/` for copy-paste prompt patterns
- use `doc-templates/` for reusable project artifacts
- use `agents/` for role definitions
- use `tools/` for scripts and helpers
- use `integrations/` for setup guides and external tool workflows

Do not add private project data, client data, secrets, or personal notes.

Prefer practical, reusable, senior-level material over generic AI advice.

## Available agents

- `agents/agent-agile-master/AGENT.md` — Agile master for solo practitioners. Routes to 25+ rituals: sprint planning, retrospective, estimation, story mapping, OKR, team health, change management. Load with PERSONA.md.

## Available skills

- `skills/legible-agent-output/SKILL.md` — Enforce plain-language output from AI agents. Replace opaque codes (A127, ENOENT), framework jargon, raw error strings, and bare percentages with human-readable titles, status messages, and error descriptions. Cross-cutting rule for any agent emitting user-facing strings.
- `skills/kano-model-strategist/SKILL.md` — Feature prioritization using Kano model. Cut waste, build MDP over MVP.
- `skills/socratic-dialogue/SKILL.md` — Reasoning rigor and anti-sycophancy guard for high-stakes decisions.
- `skills/value-proposition-canvas/SKILL.md` — Run a Value Proposition Canvas workshop through Phase 1 (Customer Profile) + Phase 2 (Value Map: Pain Relievers, Gain Creators, Products & Services) + Phase 2.5 (Framework Selection). Tables as primary output. Number rules (1-2 main Jobs + 3-5 supporting, 3-5 Pains, 3-5 Gains). Explicit user acceptance gates between every step. Soft rigor (Hypothesis welcomed, not rejected). Multi-file output: produces `vpc-result.md` + `shadow-backlog.md` starter; user writes `Value-proposition.md` after Kano. Composes with `socratic-dialogue` (validation) and `kano-model-strategist` (next step).
- `skills/typesetting-engine-skillset/` — six-skill typography/layout family (see `typesetting-engine-skillset/README.md` for the map): `microtypography`, `line-length-optimizer`, `text-typesetting`, `vertical-spacing`, `type-scale-generator`, `glyph-fidelity`.
