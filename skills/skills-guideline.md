# Skills Guideline

## What Is A Skill?

A skill is a reusable AI workflow that teaches an assistant how to perform one specific task.

## When To Create A Skill

Create a skill when the same procedure, checklist, review process, or multi-step workflow will be reused.

## When Not To Create A Skill

Do not create a skill for one-off notes, generic advice, random prompts, private project context, or anything that should be a simple prompt/template instead.

## Design Principles

1. One skill = one repeatable workflow.
2. Start with 2-3 concrete use cases before writing the skill.
3. Use progressive disclosure: keep `SKILL.md` focused; move long supporting material to linked files.
4. Make the skill composable: it should work alongside other skills.
5. Define expected inputs and outputs.
6. Write actionable steps, not essays.
7. Include a quality checklist.
8. Test triggering, output quality, and edge cases.
9. Iterate from real use.
10. Keep everything public-safe.

## Standard Skill Structure

```text
skills/
└─ skill-name/
   ├─ SKILL.md              # required
   ├─ references/           # optional
   ├─ examples/             # optional
   └─ scripts/              # optional
```

Explain:

- `SKILL.md`: required source of truth for the skill; contains frontmatter, purpose, use cases, inputs, outputs, workflow, quality checklist, and references.
- `references/`: optional; longer supporting material loaded only when needed.
- `examples/`: optional; sample outputs or good/bad examples that help the agent match the expected format.
- `scripts/`: optional; executable helpers, validators, converters, or checkers.
- No per-skill `README.md` by default because it duplicates `SKILL.md`.

## Naming Rules

- Skill folder names use kebab-case.
- No spaces.
- No underscores.
- No capitals.
- `SKILL.md` must be named exactly `SKILL.md`.

## Recommended SKILL.md Template

```markdown
---
name: skill-name
description: Use when [specific trigger/use case].
---

# Skill Name

## Purpose

## When To Use

## Inputs

## Outputs

## Workflow

## Quality Checklist

## References
```

## Frontmatter Rules

- `name` should match the folder name.
- `description` should explain what the skill does and when to use it.
- Use specific trigger language.
- Avoid vague descriptions.
- Keep metadata concise.
- Do not put private or sensitive content in frontmatter.

## Editing Existing Skills

- Preserve the original scope.
- Do not silently turn one skill into multiple jobs.
- Update references/examples if the workflow changes.
- Avoid breaking existing file paths.
- Ask before deleting or renaming a skill.

## Testing Skills

- Test whether the skill triggers for obvious relevant requests.
- Test paraphrased requests.
- Test that it does not trigger for unrelated work.
- Check output structure and quality.
- Check edge cases.
- Compare whether the skill reduces repeated prompting.

## Public Safety Rules

- No private workspace context.
- No client data.
- No secrets.
- No personal notes.
- No proprietary material copied into the skill.
- Generic examples only unless publication permission exists.

## References

This guideline is adapted from public Claude Skills guidance and rewritten for the Design Engineering Playbook.

- [Claude Code Skills documentation](https://code.claude.com/docs/en/skills)
- [The Complete Guide to Building Skills for Claude](https://resources.anthropic.com/hubfs/The-Complete-Guide-to-Building-Skill-for-Claude.pdf)
- [Introduction to Agent Skills](https://anthropic.skilljar.com/introduction-to-agent-skills)
- [Agent Skills open standard](https://agentskills.io)
