---
created: 2026-06-18
updated: 2026-06-18
version: 1.2
description: Synchronization guide for canonical (private) ↔ public mirror (v1.2 — expanded file inventory)
---

# Synchronization Guide

This agent lives in two locations. This document describes how to keep them
in sync without exposing private information in the public mirror.

## Locations

| Role | Path | Visibility |
|---|---|---|
| **Source of Truth (canonical)** | `.agents/agents/agent-agile-master/` | Private (local) |
| **Public mirror** | `projects/design-engineering-playbook/agents/agent-agile-master/` | Public (GitHub) |

## Sync Flow

```
Canonical (private)  ──→  [sanitize]  ──→  Public mirror (playbook)
     ↑                                              │
     │                                              │
     └──────────────────────────────────────────────┘
               Copy command (when stable)
```

## When to Sync

- After a significant enhancement to AGENT.md or skills
- After adding new skills (v1.1 → v1.2 added 3 new skills)
- Before a public release / tag
- When ATTRIBUTION.md changes

## Sanitization Rules (canonical → public)

Before copying to the public mirror, replace or remove:

| Pattern | Action | Example |
|---|---|---|
| `_knowledge/...` paths | Remove or replace with public ISBN/book title | `Continuous Discovery Habits (Torres, 2021)` |
| `Google Drive/.../mountain-goat-software courses/` | Remove entire knowledge table row | Keep only public frameworks |
| `extends: ../../../AGENTS.md` | Replace with `extends: ../../AGENTS.md` | (playbook-relative) |
| Canonical file paths (like `C:\Users\...`) | Remove from junction sections, keep only relative paths | |
| Private junction targets | Remove or comment out | |
| `memory/` references pointing to private locations | Keep only if they exist in public repo | |
| Specific page/line references in private PDFs | Remove, keep only framework names | |

## Sync Procedure

```bash
# 1. Ensure canonical is committed
cd C:\Users\Monika\_meta-space
git add .agents/agents/agent-agile-master/
git commit -m "agent-agile-master: update before public sync"

# 2. Copy with sanitization
#    (manual: copy files one by one, applying sanitization rules above)

# 3. Commit to playbook
cd C:\Users\Monika\_meta-space\projects\design-engineering-playbook
git add agents/agent-agile-master/
git commit -m "feat(agents): add agent-agile-master vX.Y"
git push
```

## File Inventory

Files that MUST exist in both locations:

| File | Canonical | Public | Notes |
|---|---|---|---|
| AGENT.md | ✅ | ✅ | Content differs — public version sanitized |
| PERSONA.md | ✅ | ✅ | Content differs — public version sanitized |
| README.md | ✅ | ✅ | Content differs — paths adjusted |
| ATTRIBUTION.md | ✅ | ✅ | Same content (public frameworks only) |
| EVIDENCE.md | ✅ | ✅ | Same content (no private paths) |
| LICENSE | ✅ | ✅ | Same content (MIT) |
| SYNCHRONIZATION.md | ✅ | ✅ | Same content (meta-guide) |
| INSTALL.md | ✅ | ✅ | Same content (user-facing installation guide) |
| skills/ritual-router/SKILL.md | ✅ | ✅ | Content differs — knowledge refs sanitized |
| skills/sprint-planning/SKILL.md | ✅ | ✅ | Content differs — knowledge refs sanitized |
| skills/retrospective/SKILL.md | ✅ | ✅ | Content differs — knowledge refs sanitized |
| skills/workshop-facilitation/SKILL.md | ✅ | ✅ | Content differs — knowledge refs sanitized |
| skills/team-healer/SKILL.md | ✅ | ✅ | **NEW v1.2** — content differs (knowledge refs sanitized) |
| skills/metrics-strategist/SKILL.md | ✅ | ✅ | **NEW v1.2** — content differs (knowledge refs sanitized) |
| skills/change-agent/SKILL.md | ✅ | ✅ | **NEW v1.2** — content differs (knowledge refs sanitized) |

## Version History

| Version | Date | Changes |
|---|---|---|
| 1.0 | 2026-06-18 | Initial release (4 skills: ritual-router, sprint-planning, retrospective, workshop-facilitation) |
| 1.1 | 2026-06-18 | Minor fixes to all skills |
| 1.2 | 2026-06-18 | **Major expansion**: 3 new skills (team-healer, metrics-strategist, change-agent), 4 new workshops in workshop-facilitation, quarterly OKR review added, 25+ rituals routable |
