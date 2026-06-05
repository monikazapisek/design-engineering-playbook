# Skills

Reusable AI workflows for design engineering tasks.

## What are skills

Skills are step-by-step workflows that teach an AI assistant how to perform one specific task. Each skill has a single job — a repeatable process, checklist, review procedure, or workflow — stored in a `SKILL.md` file.

They are not random prompts. A skill is a structured, versioned, reviewable artifact.

## Why this repo uses them

Design engineering spans strategy, design systems, prototyping, AI-assisted development, and design-to-code. Skills make these workflows repeatable:

- load a skill instead of re-explaining a process
- keep workflows consistent across sessions and contributors
- separate reusable methodology from one-off instructions

## How to use skills with an AI assistant

During a session, tell your AI assistant to load a specific skill:

```
Load the <skill-name> skill.
```

The assistant reads `SKILL.md` and follows the defined workflow. No need to re-describe the process.

## Standard structure

```
skills/
  README.md              # this file
  AGENTS.md              # instructions for AI agents
  skills-guideline.md    # detailed authoring rules
  <skill-name>/
    SKILL.md             # required: main instructions
    references/          # optional: background material
    examples/            # optional: sample outputs
    scripts/             # optional: executable helpers
```

## Detailed authoring rules

See `skills-guideline.md` for the full standard — when to create a skill, folder layout, required `SKILL.md` structure, quality checklist, and editing rules.
