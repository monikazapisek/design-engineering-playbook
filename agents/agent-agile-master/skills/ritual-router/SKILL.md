---
created: 2026-06-18
updated: 2026-06-18
version: 1.2
description: Decision logic for selecting which agile ritual to run based on current situation. Covers 7 skills and ~25 rituals as of v1.2.
agent: agent-agile-master
attribution: ATTRIBUTION.md
extends: ../../AGENT.md
---

# Ritual Router

Decision logic: which ceremony fits the current need.

## Input: What's the situation?

Read the user's description. Map to one of these triggers:

### Core rituals (sprint / iteration cycle)

| Trigger signal | → Ritual | Skill to load |
|---|---|---|
| "nowy sprint", "co robimy", "planowanie", "start sprintu" | Sprint Planning | `sprint-planning/SKILL.md` |
| "retro", "koniec sprintu", "co zadziałało", "podsumowanie" | Retrospective | `retrospective/SKILL.md` |
| "quarterly review", "Q[X] review", "koniec kwartału" | Quarterly OKR Review | `retrospective/SKILL.md` (extended) |
| "ile to zajmie", "estymacja", "story points", "velocity" | Estimation Session | `workshop-facilitation/SKILL.md` Workshop 1 |
| "story map", "user journey", "nowy feature", "mapowanie" | Story Mapping | `workshop-facilitation/SKILL.md` Workshop 2 |
| "backlog rośnie", "uporządkuj", "priorytety" | Backlog Refinement | `sprint-planning/SKILL.md` (subset) |
| "release", "kilka sprintów", "roadmapa" | Release Planning | `sprint-planning/SKILL.md` (extended) |

### Discovery & product strategy

| Trigger signal | → Ritual | Skill to load |
|---|---|---|
| "discovery", "czy idziemy dobrze", "badanie", "OST" | Discovery Check-in | `workshop-facilitation/SKILL.md` Workshop 3 |
| "outcome vs output", "mierzymy outputy", "czy to ma sens" | Outcomes vs Outputs Audit | `workshop-facilitation/SKILL.md` Workshop 5 |
| "build trap", "wszystko o feature'ach", "mamy za dużo" | Build Trap Diagnostic | `workshop-facilitation/SKILL.md` Workshop 6 |
| "specyfikacja wykonywalna", "BDD", "ATDD", "Given-When-Then" | BDD/ATDD Scenario | `workshop-facilitation/SKILL.md` Workshop 7 |
| "wywiad z klientem", "customer interview", "discovery rozmowa" | Customer Interview | `workshop-facilitation/SKILL.md` Workshop 8 |
| "nie wiem czy to działa", "mam za dużo metryk", "OMTM" | Metrics Audit + OMTM | `metrics-strategist/SKILL.md` Framework 1-2 |
| "OKR planning", "Q[X] planning", "ustalmy OKR-y" | OKR Quarterly Planning | `metrics-strategist/SKILL.md` Framework 3 |
| "weekly check-in OKR", "KR review" | OKR Weekly Check-in | `metrics-strategist/SKILL.md` Framework 4 |
| "north star", "NSM" | North Star Metric Definition | `metrics-strategist/SKILL.md` Framework 5 |

### Team health & dynamics

| Trigger signal | → Ritual | Skill to load |
|---|---|---|
| "zespół nie działa", "brak zaufania", "ludzie milczą" | Team Health Check | `team-healer/SKILL.md` Framework 1 |
| "konflikt w teamie", "ktoś blokuje", "hoarder" | Hoarder Confrontation | `team-healer/SKILL.md` Framework 2 |
| "psych safety", "build trust", "nowy zespół" | Psych Safety Workshop | `team-healer/SKILL.md` Framework 3 |
| "ktoś zakłóca sprint", "scope creep", "sheepdog" | Sheepdog Rounds | `team-healer/SKILL.md` Framework 4 |

### Change management & adoption

| Trigger signal | → Ritual | Skill to load |
|---|---|---|
| "wprowadzam agile", "adopcja", "pilot" | Change Kickoff | `change-agent/SKILL.md` Framework 1 |
| "trudna rozmowa", "1:1 difficult", "ORID" | ORID Conversation | `change-agent/SKILL.md` Framework 2 |
| "tablica", "kanban design", "information radiator" | Info Radiator Design | `change-agent/SKILL.md` Framework 3 |
| "adopt agile w zespole", "scrum master adoption" | Agile Adoption Roadmap | `change-agent/SKILL.md` Framework 4 |

### Meta

| Trigger signal | → Action | Skill to load |
|---|---|---|
| "nie wiem co teraz", "pomóż zdecydować" | **Diagnose first** | Read § Diagnosis below |

## Diagnosis: when unsure

If the user says "nie wiem co teraz" or the signal is ambiguous:

1. **Ask 4 questions** (in order):
   - Czy zaczynasz nowy sprint, kończysz, czy jesteś w środku? → Planning / Retro / During-sprint work
   - Czy masz już backlog uporządkowany? → If no: Backlog Refinement first
   - Czy wiesz, czy budujesz właściwą rzecz? → If unsure: Discovery / Outcomes audit
   - Czy zespół (lub ty) ma problem systemowy? → If yes: team-healer

2. **Default sequence for solo practitioner:**
   ```
   Start of sprint     → Sprint Planning (30-45 min)
   During sprint       → on-demand Estimation / Story Mapping / Customer Interview
   End of sprint       → Retrospective (20-30 min)
   Co 6-8 sprintów     → Quarterly OKR Review (45-60 min)
   Co kwartał          → OKR Quarterly Planning (60-90 min)
   ```

3. **If project is brand new:** Start with Story Mapping → then Sprint Planning

4. **If signs of dysfunction** (people quiet, blame culture, no action items in retro): Run team-healer Framework 1 diagnostic BEFORE another sprint planning.

5. **If signs of output-only thinking** (roadmap = feature list, no outcomes owned): Run Outcomes vs Outputs Audit (Workshop 5) before next sprint.

6. **If adopting new process** (agile, OKR, BDD): Use change-agent Framework 1 (Kotter) for sequencing — don't change everything at once.

## Routing rules

- **One ritual at a time.** Don't combine planning + retro in one session.
- **Timebox respected.** If time runs out, stop. Continue next session.
- **Knowledge loading:** Load MAX 2 summaries per ritual. Prefer the most relevant one.
- **Solo context:** All facilitation techniques adapted for 1 person (self-reflection, written exercises).
- **Dual mode skills (team-healer, change-agent, metrics-strategist):** Default to solo mode unless user says "w zespole" / "team" / "kilka osób".
- **Cross-skill dependencies:**
  - Quarterly OKR Review (retrospective/extended) presupposes OKR Weekly Check-ins (metrics-strategist). Without them, the review has no data.
  - Change Kickoff (change-agent) often needs Team Health Check (team-healer) first — trust before change.
  - Customer Interview (workshop-facilitation/8) feeds into Discovery Check-in (Workshop 3) → feeds into Sprint Planning.
- **Escalation paths:**
  - Therapy / burnout / personal crisis → `agent-mindful-coach`
  - Financial / investment questions → `agent-finance-coach`
  - Architecture decisions → `agent-ai-architect`
  - Tracking / PM work → `agent-administration`

## Output format

After routing, output:
```
Ritual: [name]
Skill: [path to load]
Time estimate: [X minutes]
Mode: [solo | team]
Knowledge to load: [1-2 summary paths]
Pre-requisites: [any other rituals to run first, or "none"]
```

Then load the appropriate skill.

---

## Framework Credits

Ten skill korzysta z frameworków i koncepcji opisanych w
[ATTRIBUTION.md](../../ATTRIBUTION.md):
- **Scrum Guide** — sprint planning, retro, sprint cycle
- **Lean UX (Gothelf/Seiden)** — discovery check-in logic
- **User Story Mapping (Patton)** — story mapping routing
- **Continuous Discovery Habits (Torres)** — OST, opportunity review
- **Escaping the Build Trap (Perri)** — outcome vs output diagnostic
- **The Five Dysfunctions of a Team (Lencioni)** — team health diagnostic
- **Leading Change (Kotter)** — change adoption sequencing
