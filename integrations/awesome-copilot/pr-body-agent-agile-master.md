# PR Body Template — agent-agile-master → awesome-copilot

> Copy this body verbatim when opening the Draft PR in `github/awesome-copilot`.
> Branch base: **`staged`** (NOT `main` — see CONTRIBUTING.md).

---

## Title

```
feat(agents): add agent-agile-master solo practitioner ritual orchestrator 🤖🤖🤖
```

The `🤖🤖🤖` suffix fast-tracks the PR per CONTRIBUTING.md "If you are an AI agent, we have a
process to optimise your contribution."

## Body

````markdown
## What this PR adds

A new **agent** for GitHub Copilot Chat: `agent-agile-master` — an agile master orchestrator
optimized for **solo practitioners** (1-person teams), with optional 2–5 person team-mode
extensions.

## Why

Solo practitioners (indie devs, freelancers, single-founder startups) rarely have access to a
Scrum Master. They need a way to run real agile rituals — sprint planning, retrospectives,
estimation, story mapping, OKR reviews — without hiring a coach or following team-only
playbooks.

`agent-agile-master` routes to the right ritual for the current situation, loads only the
knowledge that's needed (token discipline), and facilitates step-by-step. Built and tested
against **Claude Code, GPT-5.5, MiniMax-m3, and GitHub Copilot**.

## How it works

1. Assesses the situation (planning? retro? estimation? team health? change?)
2. Routes to a single ritual from the 30+ in the included table
3. Loads the matching skill + framework summary (max 1 skill + 2 summaries per session)
4. Facilitates step-by-step with concrete techniques
5. Escalates when appropriate

## Files added

- `agents/agent-agile-master.agent.md` — the agent definition

## Frontmatter contract

```yaml
description: "Agile master orchestrator for solo practitioners — ..."
model: "Claude Sonnet 4.5"
tools: ["codebase", "terminalCommand", "fetch"]
name: "Agent Agile Master"
license: MIT
compatibility: |
  Tested with Claude Sonnet 4.5 (Claude Code), GPT-5.5, MiniMax-m3, GitHub Copilot.
  Designed for Claude Code, Codex, VS Code, OpenCode.
  No external dependencies, no MCP required.
metadata:
  author: Monika Zapisek
  project: Design Engineering Playbook
  version: 1.3
  source: https://github.com/monikazapisekstudio/meta-space/tree/master/projects/design-engineering-playbook/agents/agent-agile-master
```

## Quality gates passed

- [x] Frontmatter satisfies `playbook/distribution/strategy-and-roadmap.md` §4.2 contract
      (Tested with vs Designed for distinction)
- [x] Smoke test passed in Claude Sonnet 4.5 (Claude Code), GPT-5.5, MiniMax-m3, GitHub Copilot
      (evidence: `integrations/copilot-smoke-test.md` in source repo)
- [x] `DOD-CHECKLIST.md` fully ticked (in source repo)
- [x] No MCP deps, no external services, no network access at runtime
- [x] MIT license + clear author (Monika Zapisek) + project (Design Engineering Playbook)
- [x] Self-review against awesome-copilot `CONTRIBUTING.md` completed
- [x] Token budget documented (max 1 skill + 2 framework summaries per session, ~320–700 tokens)

## Sources and attribution

This agent is built on **publicly available frameworks only**: Torres, Gothelf, Patton, Cagan,
Ries, Croll & Yoskovitz, Perri, Wodtke, Lencioni, Edmondson, Rosenberg, Patterson, Adzic,
Podeswa, Fitzpatrick, Kotter, Doerr, Heath & Heath, Kahneman, Kim et al., plus the Mountain
Goat Software course catalog (Cohn).

Full bibliography with ISBNs and per-source evaluation in
[ATTRIBUTION.md](https://github.com/monikazapisekstudio/meta-space/blob/master/projects/design-engineering-playbook/agents/agent-agile-master/ATTRIBUTION.md)
and [EVIDENCE.md](https://github.com/monikazapisekstudio/meta-space/blob/master/projects/design-engineering-playbook/agents/agent-agile-master/EVIDENCE.md)
in the canonical source repository.

## Related

- Canonical source repo:
  [`monikazapisekstudio/meta-space` → `projects/design-engineering-playbook/agents/agent-agile-master`](https://github.com/monikazapisekstudio/meta-space/tree/master/projects/design-engineering-playbook/agents/agent-agile-master)
- License: MIT
- Author: Monika Zapisek
- Project: Design Engineering Playbook

---

🤖 Generated with assistance from Claude (Mavis) following the awesome-copilot
`CONTRIBUTING.md` requirements.
````

## Post-submission checklist

After opening the Draft PR:

- [ ] Verify PR targets `staged` branch (NOT `main`)
- [ ] Verify `npm start` ran clean in the fork (README auto-updated)
- [ ] Verify CI check passed (per CONTRIBUTING — "If the README.md would be modified by
      running the script, the PR check will fail")
- [ ] Add a comment with `🤖🤖🤖` if it didn't make it into the title
- [ ] Watch for reviewer feedback — respond within 48h
- [ ] If reviewer requests changes, update the file in **both** the awesome-copilot fork
      AND `integrations/awesome-copilot/agent-agile-master.agent.md` in our source repo
      (to keep them in sync)

## What NOT to do

- ❌ Do not target `main` branch (CONTRIBUTING is explicit about this)
- ❌ Do not commit the `node_modules/` or build artifacts
- ❌ Do not modify any other files in the fork
- ❌ Do not include private references — all sources must be public (per BR-1, FR-5)