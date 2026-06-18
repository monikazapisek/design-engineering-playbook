---
created: 2026-06-18
updated: 2026-06-18
version: 1.3
description: Skill evaluation and evidence base for agent-agile-master (v1.3 — added Working Genius, Toxic Behavior Playbook, Personal User Manuals, Prime Directive, emotional safety in retros)
---

# Skill Evaluation — agent-agile-master

## Evaluation Status

**Date:** 2026-06-18
**Evaluator:** Monika Zapisek (canonical agent owner)
**Status:** Active / Triage — used in production by product designers, product owners, and scrum masters in cross-functional teams

## Sources

### Canonical location
`C:\Users\Monika\_meta-space\.agents\agents\agent-agile-master\`

### Public mirror
`C:\Users\Monika\_meta-space\projects\design-engineering-playbook\agents\agent-agile-master\`

### Private knowledge dependencies (not mirrored)
- Internal book-summary notes — Level 1 paraphrases of public books (fair use, private workspace)
- Mountain Goat Software course transcripts (paid courses, private workspace)

## What This Agent Does

The agent orchestrates agile ceremonies for product designers, product owners, and scrum masters working in cross-functional teams. Two modes: prepare (solo thinking before a session) and facilitate (live team session). It:
1. Routes from problem signal → correct ritual across 7 skills and ~25 rituals
2. Loads only relevant skill + knowledge (token-budgeted)
3. Facilitates step-by-step with concrete techniques and timeboxes
4. Produces written artifacts (decisions, backlog updates, action items, OKR drafts, OST trees)
5. Respects hard rules: retro always, max 3 action items, no analysis paralysis
6. **Dual mode** for 3 new skills (v1.2+): solo self-coaching OR team facilitation (2-5 osób)

## Evidence Base

### Frameworks Validated in Practice

| Framework | Evidence level | Source |
|---|---|---|
| Derby & Larsen 5-stage retro | Strong — 20+ years industry adoption | `ATTRIBUTION.md` |
| Sprint Planning (Scrum Guide) | Strong — validated 1995–present | `ATTRIBUTION.md` |
| Planning Poker estimation | Strong — empirical studies show better accuracy vs direct time estimation | Multiple studies (Molin 2016, Mahnič 2012) |
| Story Mapping (Patton) | Strong — widely adopted UX technique | `ATTRIBUTION.md` |
| OST (Torres) | Emerging — growing adoption in product teams | `ATTRIBUTION.md` |
| 5 Dysfunctions (Lencioni) | Strong — 20+ years, used in Fortune 500 team diagnostics | `ATTRIBUTION.md` |
| Psych Safety (Edmondson) | Strong — academic research base, applied in healthcare, aviation, tech | `ATTRIBUTION.md` |
| OKR (Wodtke / Doerr) | Strong — adopted by Google, Intel, many tech companies | `ATTRIBUTION.md` |
| OMTM / Lean Analytics (Croll & Yoskovitz) | Moderate — strong practitioner adoption, less academic research | `ATTRIBUTION.md` |
| Build Trap (Perri) | Moderate — newer framework (2018), practitioner-led, growing evidence | `ATTRIBUTION.md` |
| BDD/ATDD (Adzic, Podeswa) | Strong — widely adopted in TDD shops, 10+ years evidence | `ATTRIBUTION.md` |
| Kotter 8 Steps | Strong — 30+ years of research on change management | `ATTRIBUTION.md` |
| ORID (ICA) | Strong — used in facilitation worldwide, public domain | `ATTRIBUTION.md` |
| Information Radiator (Poppendieck) | Strong — core Lean/Agile concept, 20+ years | `ATTRIBUTION.md` |
| Customer Interview (Mom Test, Maurya) | Strong — widely cited in Lean Startup community | `ATTRIBUTION.md` |
| Prime Directive (Derby & Larsen) | Strong — 20+ years, established retro opening | `ATTRIBUTION.md` |
| Working Genius (Lencioni 2022) | **Moderate** — newer framework, anecdotal/case-study validation, NOT psychometric | `ATTRIBUTION.md` |
| Personal User Manuals | **Moderate** — practitioner-synthesized, no canonical research base | `ATTRIBUTION.md` |
| Toxic Behavior archetypes (Monopolizer/Ghost/Critic) | **Moderate** — synthesized from Lencioni + facilitation practice, NOT a published framework | `ATTRIBUTION.md` |
| Managing difficult emotions in retro | Strong — Derby/Larsen + broader facilitation literature | `ATTRIBUTION.md` |

### Adaptations per Mode

Standard agile ceremonies assume a full team presence. This agent adapts per mode (prepare vs facilitate):

| Ceremony | Team default | Prepare mode (solo) |
|---|---|---|
| Sprint Planning | 4h for multi-team | 30-45 min self-facilitated |
| Retrospective | 1.5h with facilitator | 20-30 min self-reflection |
| Quarterly OKR Review | 2h for 5-10 person team | 45-60 min self-review |
| Planning Poker | Team voting round | Reference-based estimation |
| Daily Standup | 15 min circle | 5 min self-check-in |
| 5 Dysfunctions Mapping | 2-3h team workshop | 15 min solo self-diagnostic |
| Personal Histories (psych safety) | 60-90 min team | 20 min self-journaling |
| Sheepdog Rounds | Daily team standup | Friday Review + 4 self-protection rituals |
| ORID Conversation | 60 min facilitated 1:1 | 20-30 min written self-reflection |
| OKR Quarterly Planning | 2-4h team offsite | 60-90 min solo |
| Customer Interview (Mom Test) | 2 interviewers, 30-60 min | 1 interviewer, 30-60 min (same) |
| BDD 3 Amigos | 3 perspectives, 60 min | 3 perspectives imagined, 45 min (less powerful, documented limitation) |
| Kotter 8 Steps | Org-wide transformation | Personal change narrative (10-12 weeks compressed) |

### What's NOT Validated

- **5 Whys for solo** — may require external facilitation to avoid blind spots
- **Discovery Check-in** — depends heavily on the user's existing customer
  contact; not validated without actual user research
- **Build Trap solo diagnostic** — originally a team/organizational framework
  (Perri); solo adaptation via 3-perspective self-assessment is novel, not
  empirically validated
- **3 Amigos without 3 people** — BDD fundamentally requires collaboration;
  solo 3-perspective writing is a workaround, not a substitute
- **Kotter 8 Steps for personal change** — Kotter's research is on organizations;
  the solo adaptation (Table in `change-agent/SKILL.md` Framework 1) is
  conceptual extrapolation, not validated by Kotter Institute
- **ORID without a facilitator** — works as self-reflection template, but
  loses the "witness" effect of another person holding space
- **Working Genius self-assessment** — Lencioni's 6-type model has not been
  validated as psychometric instrument. Treat as conversation tool for talent
  dialogue, NOT as personality typing. Risk: people may over-identify with one
  type and reject assignments that don't match.
- **Toxic Behavior Playbook (Monopolizer/Ghost/Critic)** — archetypes are
  synthesized from coaching practice, NOT a published framework. Useful as
  pattern recognition but should not replace individual diagnosis of context.
- **Personal User Manuals solo** — writing one for yourself is reflective
  practice, but loses the "discoverability" effect of a team where others
  read each other's PUMs.
- **Prime Directive as ceremony without buy-in** — if facilitator reads it
  cynically or quickly, the value is zero. Risk: ticking the box without
  internalizing.

## Token Budget (verified)

| Element | Lines | Loaded |
|---|---|---|
| AGENT.md | ~180 | Always |
| PERSONA.md | ~50 | Always |
| Ritual skill (1) | ~80-480 | On demand |
| Knowledge summary (1-2) | ~40 each | On demand |
| **Total per session** | **~320-490** | vs ~3000+ full books |

### Per-skill size (v1.3)

| Skill | Lines | Load profile |
|---|---|---|
| `ritual-router` | ~120 | Decision logic, always small |
| `sprint-planning` | ~140 | Compact |
| `retrospective` | ~330 | Includes quarterly review + Prime Directive + emotional safety |
| `workshop-facilitation` | ~480 | Largest (8 workshops) — consider sub-loading |
| `team-healer` | ~480 | Largest — now includes toxic behaviors + Working Genius |
| `metrics-strategist` | ~280 | Medium |
| `change-agent` | ~290 | Medium |

**Optimization note:** `workshop-facilitation` and `team-healer` are both ~480
lines (tied for largest). For solo token discipline:
- `workshop-facilitation`: load only the specific workshop section (Workshop
  3 / 5 / 6 / 7 / 8) relevant to current need, not the entire file.
- `team-healer`: load only the specific framework (F1 / F2 / F3 / F4 / F5 / F6)
  relevant to current team-health issue, not the entire file.

This is documented in each skill's "Knowledge to load" sections.

## Knowledge Sources Used

### Public (referenced in public mirror)
- All frameworks attributed in `ATTRIBUTION.md`
- Retromat (retromat.org) — free retro activity planner
- North Star Playbook (Amplitude, 2018) — free public NSM framework

### Private (NOT in public mirror)
- Mountain Goat Software courses (paid course transcripts, private workspace)
- Internal `_knowledge/`-style summaries (personal notes from public books)

## Quality Gates

- [x] ATTRIBUTION.md exists with all third-party framework citations
- [x] LICENSE (MIT) included
- [x] All skills have agent frontmatter and description
- [x] Token budget documented
- [x] Anti-patterns documented per skill
- [x] No hardcoded private paths in public version
- [x] Retromat freely available alternative offered
- [x] **NEW (v1.2)** Solo adaptations explicitly documented with limitations
- [x] **NEW (v1.2)** Escalation paths to other agents documented (`agent-mindful-coach`, `agent-finance-coach`, `agent-ai-architect`, `agent-administration`)
- [x] **NEW (v1.2)** Each new skill has at least 1 framework with strong evidence base
- [x] **NEW (v1.2)** Cross-skill dependencies documented (Quarterly Review → metrics-strategist, Change → team-healer)

## Risk Notes (v1.2 expansion)

The v1.2 expansion adds 3 new skills and 4 new workshops. Risks to monitor:

1. **Scope creep into therapy.** `team-healer` addresses team dysfunction, not
   personal therapy. Hard escalation to `agent-mindful-coach` is documented
   in both AGENT.md and the skill. Review quarterly.

2. **OKR misuse as performance review.** Wodtke explicitly warns against this.
   Anti-pattern documented in `metrics-strategist/`. Hard rule: OKR = learning
   tool, not evaluation.

3. **Change-agent overconfidence.** Kotter 8 Steps is a strong framework, but
   many change efforts still fail. Anti-patterns in `change-agent/` emphasize
   that framework ≠ outcome. Validate in practice.

4. **Workshop-facilitation bloat.** At 480 lines, it's the largest skill. Risk
   of context overflow. Mitigation: load only relevant workshop, not full file.
   Consider splitting into `workshop-discovery/` and `workshop-specification/`
   in v2.0 if user feedback indicates overflow.

## Risk Notes (v1.3 minor expansion)

The v1.3 expansion adds 2 new frameworks to `team-healer`, 1 ceremony
strengthening to `retrospective`, and 1 emotional-safety protocol. Risks to
monitor:

1. **Working Genius over-typing.** Risk that users label themselves or others
   with one type and reject cross-type assignments ("I'm Wonder, I don't do
   Tenacity"). Mitigation: explicit anti-pattern in Framework 6 — this is a
   map, not a verdict.

2. **Toxic Behavior labeling vs diagnosing.** Naming archetypes (Monopolizer/
   Ghost/Critic) is helpful for pattern recognition, but can slide into
   labeling. Mitigation: each archetype section emphasizes behavioral fix
   (NVC script + environment), not identity ("you are a Monopolizer" →
   forbidden phrasing).

3. **Prime Directive as box-ticking.** Risk that facilitators read it
   mechanically, destroying its psychological-safety purpose. Mitigation:
   anti-patterns explicitly call out cynicism ("If you read it cynically,
   value is zero").

4. **Team-healer bloat (now ~480 lines, tied with workshop-facilitation as
   largest skill).** Mitigation: load only specific Framework (F1-F6)
   relevant to current team-health issue. Consider splitting into
   `team-diagnostic/` (F1, F3, F6) and `team-intervention/` (F2, F4, F5) in
   v2.0 if user feedback indicates overflow.

5. **Emotional safety in retro vs therapy escalation.** The "managing
   difficult emotions" protocol (Stage 3 extension) gives tools for handling
   emotions, but does NOT make facilitator a therapist. Mitigation: explicit
   "what NOT to do" guidance — escalate to `agent-mindful-coach` or external
   therapist when emotions indicate deeper issues than retro can hold.
