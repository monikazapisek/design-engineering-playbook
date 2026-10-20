---
created: 2026-10-14
updated: 2026-10-14
version: 1.0
author: Monika Zapisek
status: accepted
description: Installation instructions for gestalt-ui-audit in Claude Code, Claude web chat, Cowork, and the Figma agent.
project: design-engineering-playbook
source-of-truth: true
---

# Install gestalt-ui-audit

Install the complete `gestalt-ui-audit` folder. Keep its internal paths unchanged so `SKILL.md` can
load `references/` and `examples/`.

## Claude Code CLI

Copy the folder to your personal skills directory:

```text
~/.claude/skills/gestalt-ui-audit/
```

For a project-only installation, place it under the project's `.claude/skills/` directory. Start a
new session, then ask for a Gestalt audit of one screenshot.

## Claude web or chat

1. Create a ZIP whose top-level folder is `gestalt-ui-audit` and includes `SKILL.md`.
2. Enable code execution and file creation in Settings if your plan requires it.
3. Open **Customize → Skills**, choose **+ → Create skill → Upload a skill**, and upload the ZIP.
4. Enable the skill in the skills list.

## Claude Cowork

Upload and enable the ZIP through **Customize → Skills** as above. Skills uploaded there are shared
between chat and Cowork for the same account.

## Figma agent

Use the single-file version in `figma/gestalt-ui-audit.md`. It reads the selected frame's layers
instead of a screenshot and reports only; it asks before adding comments.

## Optional: Figma measurements in Claude

With the Figma MCP server connected, add a Figma link to one frame to your request. The audit then
labels spacing values as *measured* instead of *estimated*. Without the connection, the skill works
from the screenshot alone.

## Verify the installation

Try:

> Run a Gestalt audit on this screenshot. The main task is assigning a technician to a job.

The response should state the audit frame, build a grouping map, score all nine principles, and mark
anything it cannot see as *Not assessed*.
