---
created: 2026-06-18
updated: 2026-06-18
version: 1.3
description: Navigation guide for agent-agile-master (v1.3 — minor expansion adding Working Genius, Toxic Behavior Playbook, Personal User Manuals, Prime Directive, emotional safety)
---

# agent-agile-master

Agile master orchestrator for solo practitioners, with optional team-mode extensions.
Knows which ritual to run when, routes to specialized skills, facilitates using
best practices from 18+ validated frameworks.

Licensed under **MIT** — see [LICENSE](./LICENSE).

## What's new in v1.3 (minor: deepening existing skills)

- **`team-healer/`** (was 318 lines → now ~520 lines):
  - **Framework 3 extension**: Personal User Manuals (1-page "how to work with me")
  - **Framework 5 [NEW]**: Toxic Behavior Playbook (Monopolizer / Ghost / Critic archetypes with NVC scripts + environmental fixes)
  - **Framework 6 [NEW]**: Working Genius (Lencioni 2022 — 6 talent types for talent-task matching)
- **`retrospective/`** (was 265 lines → now ~330 lines):
  - **Stage 0 [NEW]**: Prime Directive (Derby/Larsen) as mandatory opening ceremony, full quote, solo/team usage
  - **Stage 3 extension**: Managing difficult emotions in retro (crying, yelling, silence, walking out — neutral facilitation protocol)
- **ATTRIBUTION.md**: 2 new frameworks (Working Genius, Personal User Manuals)
- **EVIDENCE.md**: 4 new evidence levels + 5 new risk notes for v1.3 additions

## What's new in v1.2 (recap)

- **3 new skills**: `team-healer/`, `metrics-strategist/`, `change-agent/` (dual mode: solo + team)
- **4 new workshops** in `workshop-facilitation/`: Outcomes vs Outputs (5), Build Trap Diagnostic (6), BDD/ATDD (7), Customer Interview (8)
- **Discovery Check-in expanded** to full Torres Continuous Discovery methodology with OST templates
- **Quarterly OKR Review** added to `retrospective/` as extended section
- **25+ rituals** now routable via `ritual-router/`

## Structure

```
agent-agile-master/
├── AGENT.md                          # Main: role, scope, rituals, knowledge sources, decision authority
├── PERSONA.md                        # Voice, opinions, hard rules
├── ATTRIBUTION.md                    # Third-party framework attributions (18+ sources)
├── EVIDENCE.md                       # Skill evaluation and evidence base
├── LICENSE                           # MIT license
├── README.md                         # This file (navigation)
├── INSTALL.md                        # Installation guide (3 options)
└── skills/                           # Ritual procedures
    ├── ritual-router/                # Decision logic: which ritual when (~30 rituals)
    │   └── SKILL.md
    ├── sprint-planning/              # Sprint planning ceremony
    │   └── SKILL.md
    ├── retrospective/                # Retrospective + Prime Directive + Quarterly OKR Review
    │   └── SKILL.md                  # + Managing difficult emotions
    ├── workshop-facilitation/        # 8 workshops: estimation, story mapping, discovery (Torres OST),
    │   └── SKILL.md                  # outcomes vs outputs, build trap, BDD/ATDD, customer interview
    ├── team-healer/                  # Lencioni 5 dysfunctions, hoarders, psych safety,
    │   └── SKILL.md                  # sheepdog, toxic behaviors, Working Genius, Personal User Manuals
    ├── metrics-strategist/           # OKR, OMTM, actionable vs vanity, North Star Metric
    │   └── SKILL.md
    └── change-agent/                 # Kotter 8 steps, ORID, Information Radiators, agile adoption
        └── SKILL.md
```

## Load order

This folder is loaded when:
- Starting a new sprint (planning)
- Ending a sprint (retrospective)
- Needing to estimate or story-map
- Unsure which ceremony fits the current situation
- Team health intervention needed (`team-healer`)
- Setting OKRs or reviewing metrics (`metrics-strategist`)
- Adopting new process / pivot / change (`change-agent`)
- Quarterly review (Wodtke cadence)
- Toxic behavior pattern recognized (Monopolizer/Ghost/Critic → `team-healer/F5`)
- Talent-task mismatch suspected (`team-healer/F6`)

## When to use which file

| File | Read for |
|---|---|
| **AGENT.md** | scope, rituals list, knowledge sources, decision authority, version history |
| **PERSONA.md** | voice, hard rules, anti-persona |
| **ATTRIBUTION.md** | framework citations and licensing details (18+ sources) |
| **EVIDENCE.md** | validation, token budget, quality gates, risk notes |
| **skills/ritual-router/SKILL.md** | "what should I do now?" decisions |
| **skills/sprint-planning/SKILL.md** | sprint planning, backlog refinement |
| **skills/retrospective/SKILL.md** | sprint retrospective + Prime Directive + quarterly OKR review + emotional safety |
| **skills/workshop-facilitation/SKILL.md** | estimation, story mapping, discovery, outcomes, build trap, BDD, customer interview |
| **skills/team-healer/SKILL.md** | team dysfunction, hoarders, psych safety, sheepdog, toxic behaviors, Working Genius, Personal User Manuals |
| **skills/metrics-strategist/SKILL.md** | OKR planning, weekly check-in, OMTM, NSM, metrics audit |
| **skills/change-agent/SKILL.md** | change adoption, ORID conversations, information radiators |

## Public mirror

Public version available at:
`projects/design-engineering-playbook/agents/agent-agile-master/`

Canonical version (with private knowledge references) lives in `.agents/agents/agent-agile-master/`.
