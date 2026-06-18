# PR Body Template — agent-agile-master → awesome-copilot

> Copy this body verbatim when opening the Draft PR in `github/awesome-copilot`.
> Branch base: **`staged`** (NOT `main` — see CONTRIBUTING.md).

---

## Title

```
feat(agents): add agent-agile-master agile ritual orchestrator for cross-functional teams 🤖🤖🤖
```

The `🤖🤖🤖` suffix fast-tracks the PR per CONTRIBUTING.md "If you are an AI agent, we have a
process to optimise your contribution."

## Body

```markdown
## What this PR adds

A new **agent** for GitHub Copilot Chat: `agent-agile-master` — an agile master orchestrator
for **product designers, product owners, and scrum masters** working in cross-functional teams.

## Why

Product designers, product owners, and scrum masters working in cross-functional teams often
need a thinking partner to prepare and facilitate agile rituals — sprint planning, retrospectives,
estimation, story mapping, OKR reviews, team health checks. They need something that knows which
ceremony fits the current situation and how to run it step-by-step.

`agent-agile-master` routes to the right ritual, loads only the knowledge needed (token
discipline), and facilitates in two modes: **prepare** (thinking through a session solo before
entering the room) and **facilitate** (running the ritual live with the team). Built and tested
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
description: "Agile master orchestrator for product designers, product owners, and scrum masters working in cross-functional teams — routes to the right ritual and loads only the knowledge that the situation needs."
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
  source: https://github.com/monikazapisekstudio/design-engineering-playbook/tree/main/agents/agent-agile-master
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
[ATTRIBUTION.md](https://github.com/monikazapisekstudio/design-engineering-playbook/blob/main/agents/agent-agile-master/ATTRIBUTION.md)
and [EVIDENCE.md](https://github.com/monikazapisekstudio/design-engineering-playbook/blob/main/agents/agent-agile-master/EVIDENCE.md)
in the source repository.

## Related

- Source repo: [monikazapisekstudio/design-engineering-playbook → agents/agent-agile-master](https://github.com/monikazapisekstudio/design-engineering-playbook/tree/main/agents/agent-agile-master)
- License: MIT
- Author: Monika Zapisek
- Project: Design Engineering Playbook

---

🤖 Generated with assistance from Claude following the awesome-copilot `CONTRIBUTING.md` requirements.
```

## Post-submission checklist

After opening the Draft PR:

- [ ] Verify PR targets `staged` branch (NOT `main`)
- [ ] Verify `npm start` ran clean in the fork (README auto-updated)
- [ ] Verify CI check passed
- [ ] Watch for reviewer feedback — respond within 48h
- [ ] If reviewer requests changes, update the file in **both** the awesome-copilot fork
      AND `integrations/awesome-copilot/agent-agile-master.agent.md` in our source repo

## What NOT to do

- ❌ Do not target `main` branch
- ❌ Do not commit `node_modules/` or build artifacts
- ❌ Do not modify any other files in the fork
- ❌ Do not include private repo references — all sources must be public
