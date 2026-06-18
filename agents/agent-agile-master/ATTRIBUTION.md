# Third-Party Attributions

This agent synthesizes ideas from multiple academic and practitioner sources.
The implementation, phrasing, and structure of the agent itself are original work
licensed under MIT (see `LICENSE`). The underlying frameworks and concepts are
attributed below.

## Core Agile Frameworks

**Scrum Guide (2020).** *Ken Schwaber & Jeff Sutherland.*
The Scrum framework — sprints, sprint planning, retrospectives, sprint review,
daily scrum — forms the structural backbone of this agent's ritual definitions.
This agent adapts Scrum ceremonies for solo practitioners; it does not require
a team.

**Kanban Method (David J. Anderson, 2010).**
Flow-based work management informing backlog refinement and WIP limits in
sprint planning.

**Lean Software Development (Mary & Tom Poppendieck, 2003).**
Lean principles — eliminate waste, amplify learning, decide as late as possible
— inform the estimation philosophy (relative sizing, not time prediction).

## Retrospective Frameworks

**Agile Retrospectives (Esther Derby & Diana Larsen, 2006).**
The "Five Stages" pattern (Set the Stage → Gather Data → Generate Insights →
Decide What to Do → Close) is the primary structure for all retrospective
formats in this agent. The Starfish, Sailboat, Timeline, and 4 Ls formats are
drawn from the Derby/Larsen tradition, adapted for solo self-reflection.

**Retromat / retromat.org**
Used as a reference for rotating retro formats. Retromat is a free, open
activity planner for retrospectives. Referenced in `skills/retrospective/` as a
source of format inspiration.

## Estimation and Planning

**Planning Poker / Wideband Delphi (James Grenning, 2002; popularized by
Mike Cohn, 2005).**
The Fibonacci-scale estimation technique (1-2-3-5-8-13) and reference-story
method are adaptations of Planning Poker for solo practice.

**Agile Estimating and Planning (Mike Cohn, 2005).**
Concepts of velocity-based forecasting, relative sizing, and sprint planning
horizons influence the estimation and planning workflows in this agent.

## Story Mapping

**User Story Mapping (Jeff Patton, 2014).**
The horizontal journey / vertical prioritization model, release-line slicing,
and MVP identification are drawn from Patton's work. Adapted for solo
practitioners (no facilitation of a room).

## Discovery and Product Management

**Continuous Discovery Habits (Teresa Torres, 2021).**
The Opportunity Solution Tree (OST) framework and assumption-testing approach
inform the Discovery Check-in workshop in `skills/workshop-facilitation/`.

**Escaping the Build Trap (Melissa Perri, 2018).**
Outcomes-over-outputs philosophy referenced in the agent's prioritization
logic.

## Additional Techniques Referenced

| Technique | Source | Used in |
|---|---|---|
| 5 Whys | Sakichi Toyoda / Toyota Production System | `skills/retrospective/` — root cause analysis |
| SMART Goals | Doran (1981) | `skills/retrospective/` — action item format |
| T-Shirt Sizing | Industry standard, origin unknown | `skills/sprint-planning/` — quick estimation |
| Fishbone (Ishikawa) Diagram | Kaoru Ishikawa | `skills/retrospective/` — complex issue analysis |
| INVEST | Bill Wake (2003) | `skills/workshop-facilitation/` — story quality check |
| Starfish Format | Patrick Kua (Agile Alliance) | `skills/retrospective/` — retro format |

## Team Dynamics & Health (v1.2+)

**The Five Dysfunctions of a Team (Patrick Lencioni, 2002).**
The pyramid model (absence of trust → fear of conflict → lack of commitment →
avoidance of accountability → inattention to results) is the primary diagnostic
framework in `skills/team-healer/`. The "5 Dysfunctions Mapping" team workshop
adapts Lencioni's approach for solo practice and small teams.

**Fearless Organization (Amy Edmondson, 2018).**
The 4 stages of psychological safety (inclusion, learner, contributor, challenger)
and the "Personal Histories" team exercise are the foundation of `skills/team-healer/`
Framework 3. Edmondson's research on psychological safety in healthcare and aviation
teams informs the "psych safety ≠ comfort zone" anti-pattern guidance.

**Nonviolent Communication (Marshall Rosenberg, 2003).**
The 4-step confrontation script (Observation / Feeling / Need / Request) used in
`skills/team-healer/` Framework 2 for confronting agile hoarders is adapted from
NVC's nonviolent communication framework. The script is also applicable to solo
self-confrontation for hoarding patterns.

**Crucial Conversations (Patterson, Grenny, McMillan, Switzler, 2002).**
References and complementary tools for the difficult conversation workflow used in
`skills/team-healer/` and `skills/change-agent/`. NVC and Crucial Conversations are
deeply complementary — this agent uses NVC's script structure with Crucial
Conversations' emphasis on creating safety and mutual purpose.

**The Working Genius (Patrick Lencioni, 2022).**
The 6-types talent assessment (Wonder / Invention / Discernment / Galvanizing /
Enablement / Tenacity) used in `skills/team-healer/` Framework 6 is adapted from
Lencioni's follow-up to "Five Dysfunctions". Used as heuristic for matching work
to natural talent, not as psychometric test. Solo self-assessment and team
mapping workshop both adapted from the book's protocol. **Note:** validation
evidence is anecdotal/case-study based, not statistical — treat as conversation
tool, not personality typing.

**Personal User Manuals (various practitioner origins, popularized by Lara
Hogan / Aha! / engineering management blogs).**
The 1-page "how to work with me" template in `skills/team-healer/` Framework 3
extension is adapted from the Personal User Manual format circulating in tech
leadership communities since ~2018. No single canonical source — synthesized
from multiple practitioner write-ups.

## Metrics, OKR & Product Strategy (v1.2+)

**Radical Focus (Christina Wodtke, 2016).**
The OKR quarterly cadence, weekly check-in format with 🟢🟡🔴 status indicators, and
the "Radical Focus" weekly review template are the foundation of
`skills/metrics-strategist/` Frameworks 3 and 4. Wodtke's "high-level goals + small
bets + weekly review" pattern informs the Q[X] planning workflow.

**Lean Analytics (Alistair Croll & Benjamin Yoskovitz, 2013).**
The "Actionable vs Vanity Metrics" diagnostic (Framework 1), One Metric That Matters
(OMTM) concept (Framework 2), and 5 startup stages with their typical OMTMs are
the backbone of `skills/metrics-strategist/`. The "stages-based metric selection"
informs the OMTM Selection Workshop.

**Measure What Matters (John Doerr, 2018).**
Referenced as case-study source for OKR implementations. The CFR (Conversations,
Feedback, Recognition) extension is NOT implemented in this agent because it belongs
to performance management domain, not product strategy. Use only OKR core concepts
from Doerr's book.

**Escaping the Build Trap (Melissa Perri, 2018).**
The outcomes-vs-outputs philosophy, the Build Trap diagnostic scorecard, and the
"rewrite output as outcome" technique are the foundation of `skills/workshop-facilitation/`
Workshops 5 and 6. Perri's research on product organizations informs the "kill
criteria" concept in OKR Key Results.

**Lean Startup (Eric Ries, 2011).**
The Build-Measure-Learn loop and MVP taxonomy (concierge, smoke test, fake door,
Wizard of Oz) are referenced in `skills/workshop-facilitation/` Workshops 5 and 8.
The "validated learning" concept anchors the "don't ship without measurement"
anti-pattern.

**The Mom Test (Rob Fitzpatrick, 2013).**
The "ask about their life, not your idea" principle and the open-ended question
patterns in `skills/workshop-facilitation/` Workshop 8 (Customer Interview) are
adapted from Fitzpatrick's book. Critical for avoiding confirmation bias in
discovery interviews.

**North Star Playbook (Amplitude, 2018, free online publication).**
The North Star Metric framework, input/output metrics hierarchy, and the
"3 testing questions" for NSM are used in `skills/metrics-strategist/` Framework 5.
Free public resource.

## Executable Specifications & BDD (v1.2+)

**Specification by Example (Gojko Adzic, 2011).**
The Given-When-Then scenario format, the "3 Amigos" workshop structure, and the
"living documentation" concept are the foundation of `skills/workshop-facilitation/`
Workshop 7 (BDD/ATDD). Adzic's "key examples" methodology informs scenario selection.

**ATDD by Example (Howard Podeswa, 2012).**
Practical Acceptance Test-Driven Development patterns and the "narrative test
structure" approach. Referenced alongside Adzic for BDD/ATDD implementation in
`skills/workshop-facilitation/` Workshop 7.

**Running Lean (Ash Maurya, 2012).**
The "Problem Interview" framework referenced in `skills/workshop-facilitation/`
Workshop 8 complements Mom Test for early-stage discovery.

## Change Management & Facilitation (v1.2+)

**Leading Change (John Kotter, 1996).**
The 8-step change model (urgency → coalition → vision → communication → obstacles
→ short wins → acceleration → institutionalize) is the foundation of
`skills/change-agent/` Framework 1. Kotter's research on the 70% failure rate of
change initiatives informs the "anti-patterns" guidance. The Solo adaptation
table is original to this agent.

**Switch: How to Change Things When Change Is Hard (Chip & Dan Heath, 2010).**
The rider/elephant/path metaphor for change narrative is referenced in
`skills/change-agent/` Framework 1 (Solo mode for personal change). The book
informs why "rational arguments" (rider) often fail without "emotional appeal"
(elephant) and "environment design" (path).

**ORID — Objective, Reflective, Interpretive, Decisional (Institute of Cultural Affairs, 1980s).**
The 4-level structured conversation framework used in `skills/change-agent/`
Framework 2. ORID originates from the "Art of Focused Conversation" methodology
developed by ICA and is in the public domain. Used widely in facilitation,
coaching, and group dynamics work.

**Information Radiator (Tom Poppendieck, 2003).**
The "Information Radiator" concept (a display in a high-traffic area, readable
without effort, always up-to-date) used in `skills/change-agent/` Framework 3
originates from Mary & Tom Poppendieck's "Lean Software Development" book.
Adapted here to include 8 specific radiator types and design principles.

## Additional Frameworks Referenced in v1.2+ Skills

| Framework | Source | Used in |
|---|---|---|
| 4 Stages of Psych Safety | Edmondson (2018) | `skills/team-healer/` Framework 3 |
| Sheepdog metaphor | Industry leadership metaphor, popularized in "Leadership and Self-Deception" (Arbinger Institute) | `skills/team-healer/` Framework 4 |
| OKR Confidence Scoring | Wodtke (2016) | `skills/metrics-strategist/` Framework 4 |
| AARRR / Pirate Metrics | Dave McClure (2007) | `skills/metrics-strategist/` Framework 1 (referenced) |
| Personal Histories exercise | Edmondson (2018) | `skills/team-healer/` Framework 3 |
| Personal User Manual | Practitioner-synthesized (Lara Hogan, Aha!, eng-mgmt blogs ~2018) | `skills/team-healer/` Framework 3 extension |
| Working Genius (6 types) | Lencioni (2022) | `skills/team-healer/` Framework 6 |
| Toxic Behavior archetypes (Monopolizer/Ghost/Critic) | Synthesized from Lencioni + various agile coaching practice | `skills/team-healer/` Framework 5 |
| North Star + Input Metrics | Amplitude (2018) | `skills/metrics-strategist/` Framework 5 |
| 3 Amigos Workshop | Various BDD practitioners, popularized by Adzic | `skills/workshop-facilitation/` Workshop 7 |
| Prime Directive | Derby & Larsen (2006) | `skills/retrospective/` Stage 0 |
| Managing difficult emotions in retro | Derby & Larsen + various facilitation practice | `skills/retrospective/` Stage 3 extension |

## What This Agent Is NOT Derived From

- No text was copied from any specific book, blog, or article.
- No proprietary consulting frameworks (BCG/McKinsey/Gartner) are reproduced.
- No paid courseware content is reproduced verbatim — only public framework
  concepts (Scrum, Kanban, Lean) are referenced.
- No copyrighted material is included. All instructions are original synthesis
  of public-domain frameworks and practitioner experience.

## How to Attribute When You Remix

If you build a derivative agent or fork this one, please keep:

1. This `ATTRIBUTION.md` file
2. The MIT `LICENSE`
3. A visible link back to the original sources (listed above) in your derived
   work

That keeps the chain of credit intact without burdening downstream users.
