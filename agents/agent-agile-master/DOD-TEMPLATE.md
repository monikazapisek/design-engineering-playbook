# Definition of Done — Agent & Skill Template

## Purpose

This template defines the **Definition of Done** for publishing an AI agent or
skill in the [design-engineering-playbook](https://github.com/monikazapisekstudio/meta-space).
Use it as a checklist before committing any new or updated agent/skill to the
public repo.

Two tiers:
- **SKILL** — a reusable workflow (e.g. `sprint-planning/SKILL.md`)
- **AGENT** — a complete role definition (e.g. `agent-agile-master/`)

---

## SKILL Definition of Done

| # | Criteria | Pass/Fail | Notes |
|---|---|---|---|
| 1 | **Frontmatter complete** — `created`, `updated`, `version`, `description`, `agent` (or `attribution`) fields present | ☐ | |
| 2 | **Purpose section** — answers "why does this skill exist?" | ☐ | |
| 3 | **When to run** — clear trigger conditions | ☐ | |
| 4 | **Duration** — time estimate for the ceremony/workshop | ☐ | |
| 5 | **Step-by-step** — actionable, numbered steps with timeboxes | ☐ | |
| 6 | **Output format** — what artifact is produced | ☐ | |
| 7 | **Anti-patterns** — ≥3 common mistakes to avoid | ☐ | |
| 8 | **Framework Credits** — links to `ATTRIBUTION.md`, lists frameworks used | ☐ | |
| 9 | **Knowledge sources public** — no `_knowledge/` or `Google Drive/` paths (public version) | ☐ | |
| 10 | **Token budget** — no full PDFs, only summaries/paraphrases | ☐ | |
| 11 | **Solo adaptation** — adapted for 1-person practice (if applicable) | ☐ | |
| 12 | **Original content** — no verbatim copies of copyrighted material | ☐ | |
| 13 | **MIT-compatible** — all referenced frameworks allow commercial use | ☐ | |

### SKILL DoD Gate: PASS / PASS WITH NOTES / FAIL

---

## AGENT Definition of Done

| # | Criteria | Pass/Fail | Notes |
|---|---|---|---|
| 1 | **Frontmatter complete** — `created`, `updated`, `version`, `status`, `description`, `extends` | ☐ | |
| 2 | **AGENT.md: Role clarity** — "Czym jestem" + "Czym NIE jestem" sections | ☐ | |
| 3 | **AGENT.md: Scope** — rituals/actions list with triggers and skill routing | ☐ | |
| 4 | **AGENT.md: Decision authority** — autonomicznie / sugeruje / pyta zawsze | ☐ | |
| 5 | **AGENT.md: Token budget** — estimated lines per element | ☐ | |
| 6 | **AGENT.md: Quality Gates** — ≥6 gates documented | ☐ | |
| 7 | **AGENT.md: Public version note** — explains canonical vs public split | ☐ | |
| 8 | **PERSONA.md** — voice, hard rules (≥5), anti-persona, when to stay silent | ☐ | |
| 9 | **ATTRIBUTION.md** — all third-party frameworks cited with sources | ☐ | |
| 10 | **EVIDENCE.md** — evaluation, adaptacje solo, co jest/nie jest validated | ☐ | |
| 11 | **LICENSE** — MIT, matching playbook | ☐ | |
| 12 | **README.md** — structure, load order, file navigation, public mirror note | ☐ | |
| 13 | **SYNCHRONIZATION.md** — canonical-to-public sync procedure (if dual-location) | ☐ | |
| 14 | **Skills** — each skill meets SKILL DoD | ☐ | |
| 15 | **No private paths** — no `_knowledge/`, `Google Drive/`, `C:\Users\...` in public version | ☐ | |
| 16 | **No verbatim copyright** — all content is original synthesis, not copied | ☐ | |
| 17 | **MIT license compliance** — no GPL/AGPL dependencies or viral licenses | ☐ | |
| 18 | **`extends` path correct** — points to playbook `../../AGENTS.md` in public version | ☐ | |

### AGENT DoD Gate: PASS / PASS WITH NOTES / FAIL

---

## Usage

1. Copy this file to the agent/skill folder as `DOD-CHECKLIST.md` (or use inline)
2. Run through each criteria, mark Pass/Fail
3. If any FAIL — fix before publishing
4. Append filled checklist to `EVIDENCE.md` or keep as standalone artifact
