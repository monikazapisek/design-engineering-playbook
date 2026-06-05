# Skills Guideline

Standard for creating and editing skills in the Design Engineering Playbook.

## Definition

A skill is a reusable AI workflow that teaches an assistant how to perform one specific task. It turns a repeatable procedure into a loadable instruction set.

## When to create a skill

Create a skill when the same procedure, checklist, review process, or workflow will be reused across multiple sessions or projects.

## When NOT to create a skill

Do not create a skill for:
- one-off notes or single-use instructions
- generic AI advice not grounded in design engineering practice
- random prompts not tied to a specific workflow
- private project context, client data, or personal information
- content that belongs in `prompts/` (copy-paste prompt patterns for humans)

## Standard single-skill structure

```
skills/
  README.md
  AGENTS.md
  skills-guideline.md
  <skill-name>/
    SKILL.md              # required: main instructions
    references/           # optional: background material
    examples/             # optional: sample outputs
    scripts/              # optional: executable helpers
```

### Folder and file roles

| Path | Required | Purpose |
|---|---|---|
| `SKILL.md` | Yes | Source of truth. Contains frontmatter, purpose, use cases, inputs, outputs, workflow, checklist, and references. |
| `references/` | No | Longer supporting material that should not always load into context. Load on demand. |
| `examples/` | No | Sample outputs or good/bad examples that help the agent produce consistent results. |
| `scripts/` | No | Executable helpers, validators, converters, or checkers. Use only when the workflow benefits from automation. |

**No per-skill `README.md` by default.** It duplicates `SKILL.md`. Add one only if the user explicitly asks.

## Recommended SKILL.md structure

```markdown
---
name: skill-name
description: "Use when [specific trigger or use case]."
---

# Skill Name

## Purpose

One paragraph. What does this skill achieve?

## When To Use

When should an agent load this skill? What signals trigger it?

## Inputs

What information does the skill need to work? (file paths, URLs, parameters, etc.)

## Outputs

What does the skill produce? How is the result reported or stored?

## Workflow

Numbered steps. Each step has a clear action, expected result, and any decision points.

## Quality Checklist

- [ ] Checkable items that verify the workflow ran correctly
- [ ] Second check if applicable

## References

Links to related skills, tools, or external documentation.
```

### Frontmatter

| Field | Required | Description |
|---|---|---|
| `name` | Yes | Hyphenated kebab-case matching the folder name |
| `description` | Yes | One line — trigger conditions and summary. Agents use this to decide when to load the skill |

## Authoring rules

- one skill = one job. Do not combine unrelated workflows.
- keep `SKILL.md` concise. Use step-by-step instructions, not essays.
- use clear trigger language in the `description` frontmatter field.
- define expected inputs and outputs explicitly.
- write actionable steps — each step should produce a visible result.
- include a quality checklist at the end of every skill.
- move long background material to `references/` — keep the main file lean.
- include examples only when they demonstrably improve output quality.
- add scripts only when there is a real executable workflow (validation, conversion, checking).
- keep everything public-safe. No client names, project specifics, or private data.

## Editing rules

- preserve the skill's original scope. Do not silently broaden a skill to cover multiple jobs.
- update `references/` and `examples/` if the workflow changes.
- avoid breaking existing file paths that other skills or tools may rely on.
- ask before deleting or renaming a skill — someone may depend on it.

## References

- [Claude Code Skills](https://code.claude.com/docs/en/skills)
- [Agent Skills open standard](https://agentskills.io)
