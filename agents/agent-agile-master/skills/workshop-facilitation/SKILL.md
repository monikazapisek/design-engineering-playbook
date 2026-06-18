---
created: 2026-06-18
updated: 2026-06-18
version: 1.2
description: Workshop facilitation — estimation, story mapping, discovery (Torres OST), outcomes vs outputs (Perri), BDD/ATDD, and other collaborative exercises
agent: agent-agile-master
attribution: ATTRIBUTION.md
extends: ../../AGENT.md
---

# Workshop Facilitation

## Purpose

Facilitate specific exercises: estimation, story mapping, discovery, and ad-hoc workshops. Each workshop has a clear format, timebox, and output.

## When to run

- Need to estimate stories or features
- Need to map user journey for a new feature
- Need to check discovery status
- Need structured thinking about a problem

## Duration

- **Estimation:** 15-30 min
- **Story Mapping:** 45-60 min
- **Discovery Check-in:** 20-30 min

## Knowledge to load (on demand)

| Workshop | Reference |
|---|---|
| Estimation | Cohn, *Estimating With Story Points* (Modules 1-3) — Mountain Goat Software |
| Story writing | Cohn, *Better User Stories* (Modules 1-3) — Mountain Goat Software |
| Story mapping | Patton, *User Story Mapping* (2014) |
| Discovery | Torres, *Continuous Discovery Habits* (2021) |
| Lean UX process | Gothelf & Seiden, *Lean UX* (2013/2016) |

---

## Workshop 1: Estimation Session

### Purpose

Relative sizing of backlog items. Not time estimation — relative complexity/effort.

### Format: Planning Poker (solo adaptation)

Since you're solo, use **reference-based estimation**:

1. **Pick a reference story** — one you've completed, well-understood. Call it "3 points."
2. **Compare each new story** to the reference:
   - Same effort? → 3
   - Half the effort? → 1-2
   - Double the effort? → 5-8
   - Way bigger? → 13+ (split it!)
3. **If uncertain** between two sizes, pick the larger one.

### Story Point Scale (Fibonacci)

| Points | Meaning | Solo reference |
|---|---|---|
| 1 | Trivial | < 1 hour, obvious solution |
| 2 | Small | 1-3 hours, clear path |
| 3 | Medium (reference) | 3-8 hours, some unknowns |
| 5 | Large | 1-2 days, significant work |
| 8 | Very Large | 2-3 days, complex |
| 13 | Huge | > 3 days, SPLIT THIS |

### Output

```
| Story | Points | Notes |
|---|---|---|
| Button component | 3 | Reference story |
| Input component | 5 | More variants |
| Modal component | 8 | Accessibility heavy |
```

### When to use velocity

After 3+ sprints with estimation, calculate velocity:
```
Velocity = total points completed / number of sprints
```

Use velocity for forecasting: "At 15 pts/sprint, this 60-point feature takes ~4 sprints."

---

## Workshop 2: Story Mapping

### Purpose

Map user journey horizontally, prioritize vertically. Create release plan from user perspective.

### Format (solo adaptation)

1. **Define the user** — who is this for? (Check `strategy/URD/personas.md`)

2. **Map the journey horizontally** — steps the user takes, left to right:
   ```
   [Step 1] → [Step 2] → [Step 3] → [Step 4] → [Step 5]
   ```

3. **Under each step, list stories vertically** — from must-have (top) to nice-to-have (bottom):
   ```
   Step 1          Step 2          Step 3
   ─────────       ─────────       ─────────
   [US-1.1 MVP]   [US-2.1 MVP]   [US-3.1 MVP]     ← Release 1
   [US-1.2]       [US-2.2]       [US-3.2]          ← Release 2
   [US-1.3]       [US-2.3]       [US-3.3]          ← Release 3
   ```

4. **Draw the release line** — what goes in MVP vs future releases?

5. **Identify gaps** — any steps missing? Any steps with no stories?

### Output

User story map document with releases identified.

### Knowledge source

For detailed methodology: load `user-story-mapping-patton-summary.md`

---

## Workshop 3: Discovery Check-in (Torres Continuous Discovery)

### Purpose

Are we building the right thing? Quick assessment of whether the team is still solving the most valuable customer problem. Based on Teresa Torres' Continuous Discovery Habits — assumes ongoing (weekly) customer contact, not annual research.

### Format (solo adaptation, 20-30 min)

#### Step 1: Opportunity Review (5 min)

Customer opportunities = unmet needs, desires, or pain points. NOT solutions.

```
| Opportunity | Confidence (1-5) | Evidence | Last touched |
|---|---|---|---|
| [User pain/problem in user language] | 4 | 3 interviews | 2 weeks ago |
| [Another opportunity] | 2 | 1 interview | 1 month ago |
```

Pick the top 1 — the one you're MOST UNCERTAIN about. That's where learning lives.

#### Step 2: Assumption Audit (10 min)

List top 3 assumptions for the chosen opportunity. Use Desirability / Viability / Feasibility:

```
Assumption: [what I believe to be true]
Type:       [D / V / F]
Evidence:   [what supports this — interviews, data, prior experience]
Risk:       [what happens to the product if I'm wrong?]
Test:       [smallest experiment to validate/invalidate]
```

**Type legend:**
- **D (Desirability)** — "Customers want this"
- **V (Viability)** — "This works for our business"
- **F (Feasibility)** — "We can build this"

#### Step 3: Next Experiment (5 min)

Based on highest-risk assumption, design ONE small experiment (max 1 week to run):

| Experiment type | When to use | Time | Cost |
|---|---|---|---|
| Customer interview | Need qualitative depth | 30-60 min prep + 30 min interview | Low |
| Prototype test | Need to test interaction | 2-4 hours | Low |
| Concierge MVP | Need to validate end-to-end flow | 1-3 days | Medium |
| A/B test | Need quantitative validation | 1-2 weeks | High |
| Smoke test (landing page) | Need to gauge interest | 1-2 days | Low |
| Fake door / Wizard of Oz | Need to test intent | 1 week | Low |

#### Output

```
## Discovery Check-in — [date]

Top opportunity: [description, user language]
Highest-risk assumption: [assumption + type]
Next experiment: [what, when, success criteria]
Decided: [what we will/won't do based on this check-in]
```

### Opportunity Solution Tree (OST) — Torres

A 4-level visual map of how customer needs connect to solutions:

```
                    OUTCOME
                       ↑
                  OPPORTUNITY (customer need)
                  ↑      ↑      ↑
              SOLUTION  SOLUTION  SOLUTION
                 ↑        ↑        ↑
             ASSUMPTION ...   ...
```

- **Outcome** — business metric you want to move (connect to OMTM in `metrics-strategist`)
- **Opportunity** — customer problem (NOT a feature)
- **Solutions** — possible ways to address the opportunity
- **Assumptions** — what must be true for each solution to work

**Why OST > feature backlog:** It forces you to ask "WHY this feature?" before "HOW to build it." Solves the Build Trap (Workshop 6).

**Solo OST template:**

```
OUTCOME: [business metric, e.g. "30% D7 retention"]

OPPORTUNITY: [customer need, e.g. "Users don't know if they should return after first session"]
  Evidence: [interview X, data Y]

  SOLUTION A: [feature/change idea]
    Assumption: [what must be true for this to work]
    Test:       [experiment]
    Status:     [untested / validated / invalidated]

  SOLUTION B: [...]
    ...

  SOLUTION C: [...]
    ...
```

### Knowledge source

For detailed OST methodology: load `continuous-discovery-habits-torres-summary.md`

---

## Workshop 4: Backlog Grooming

### Purpose

Clean up the backlog. Remove stale items, reprioritize, split large items.

### Format (solo, 20 min)

1. **Delete** anything >3 months old with no action → if it was important, it'll come back
2. **Split** any item >8 points → break into smaller stories
3. **Clarify** any item without clear acceptance criteria → add AC or delete
4. **Prioritize** using simple ranking:
   - Must ship (this sprint)
   - Should ship (next 1-2 sprints)
   - Could ship (sometime)
   - Won't ship (remove or parking lot)

5. **Output:** Updated backlog with clear priority tiers

---

## Workshop 5: Outcomes vs Outputs Diagnostic (Perri)

### Purpose

Czy organizacja (albo ty) mierzy sukces **zachowaniem użytkownika** (outcome) czy **liczbą dostarczonych funkcji** (output)? Melissa Perri nazywa ten drugi stan "Build Trap" — kiedy roadmap = lista funkcji, a nie lista efektów.

### Format (solo, 20 min)

#### Step 1: Audit current roadmap (5 min)

Wylistuj 5 ostatnich "shipped" items:

```
| Feature shipped | Date | Original "why" | Outcome measured? (Y/N) |
|---|---|---|---|
| [feature] | [date] | [reason] | [N] |
| [feature] | [date] | [reason] | [Y] |
```

#### Step 2: Score each feature (10 min)

Dla każdej feature, odpowiedz na 3 pytania:

1. **Outcome ownership** — "Czy istnieje osoba, która czuje się odpowiedzialna za EFEKT tej funkcji (nie jej dostarczenie)?"
2. **Measured behavior** — "Czy mierzymy ZMIANĘ ZACHOWANIA użytkownika po ship-cie? (nie liczbę pobrań, ale np. retention, time-on-task, completion rate)"
3. **Kill criteria** — "Czy wiemy, przy jakim wyniku WYCOFAMY tę funkcję jako porażkę?"

#### Step 3: Score (5 min)

Policz ile features ma 3/3 — to outcome-owned features. Reszta to output-only.

```
## Outcomes vs Outputs Audit — [date]
Features audited: 5
Outcome-owned: 2/5  (40%)
Output-only:    3/5  (60%)

Top output-only feature: [name]
Question to ask: "If we ship this, what user behavior do we expect to change?"
```

#### Step 4: Rewrite 1 output as outcome (5 min)

Weź najgorszy output-only feature i przeformułuj:

```
BEFORE (output):  "Ship the new dashboard with 4 widgets"

AFTER (outcome):  "Increase daily engagement of returning users from 25% to 40%
                   by providing at-a-glance status of [X] they're tracking"
```

### Kiedy jesteś w Build Trap (red flags)

- "Musimy dowieźć X funkcji w Q[Y]" (commitment to output, nie outcome)
- "Nie możemy anulować feature, bo już ją zapowiedzieliśmy" (sunk cost fallacy)
- "Stakeholderzy oczekują X features" (output pressure bez outcome ownership)
- Brak mierzenia zachowań użytkownika po release

### Output

`memory/decisions.md` lub `discovery/outcomes-audit-[date].md` z pełnym audit + przeformułowanym top feature.

### Knowledge source

For full framework: load `Escaping the Build Trap (Perri).md` Chapter 2-3.

---

## Workshop 6: Build Trap Deep Diagnostic (Perri)

### Purpose

Pełniejszy diagnostic dla organizacji / zespołu, który podejrzewa, że utknął w Build Trap. Perri: "Organizations that fall into the build trap prioritize shipping features over creating value."

### Format (team 2-5 osób, 60 min) — można zaadaptować do solo reflection

#### Step 1: Scorecard (15 min)

Każdy członek zespołu (albo ty, w 3 różnych rolach: founder, PO, dev) ocenia 8 stwierdzeń 1-5:

| # | Stwierdzenie | Score |
|---|---|---|
| 1 | Wiemy, jakiego customer behavior chcemy zmienić dla każdej feature | /5 |
| 2 | Mamy ownership outcome'ów (nie tylko outputów) | /5 |
| 3 | Discovery to ongoing practice, nie projekt | /5 |
| 4 | Używamy OKR-ów (lub podobnego framework outcome-based) | /5 |
| 5 | "Done" = outcome delivered, nie feature shipped | /5 |
| 6 | Mamy proces decyzji kill / iterate for features that don't work | /5 |
| 7 | Customer feedback wpływa na roadmap w tym kwartale | /5 |
| 8 | Zespół ma empowerment decydować o priorytetach | /5 |

**Sum scores:**
- 8-15: deep in Build Trap. Workshop 5 + 6 + re-prioritize metrics.
- 16-24: emerging awareness. Workshops 5-6, 1:1 conversations.
- 25-32: outcome-driven. Maintain with weekly check-ins.

#### Step 2: Pick top 3 weakest areas (10 min)

Nie próbuj naprawić wszystkich 8. Wybierz 3 najsłabsze i address je w tym kwartale.

#### Step 3: For each, define 1 experiment (15 min)

```
Weakness #3: "Discovery is project, not ongoing"
Experiment:  Schedule weekly 30-min customer interview slot in calendar
             (treat as non-negotiable meeting, like a 1:1 with CEO)
Success:     8 weeks of consecutive customer interviews by end of Q[X]
```

#### Step 4: Assign owners + deadlines (10 min)

Każdy experiment: owner + deadline + review date.

#### Step 5: Review in next monthly retrospective (10 min)

Output: 3 experiments z owners, zaplanowane review.

---

## Workshop 7: BDD / ATDD — Executable Specifications

### Purpose

Twórz specyfikacje wykonywalne (Given-When-Then), które:
- zamykają lukę między "biznes chce X" a "dev buduje Y"
- są jednocześnie dokumentacją, kryteriami akceptacji i testami automatycznymi
- eliminują wiele rund review "to nie to miałem na myśli"

### Czym różni się BDD od ATDD

| | ATDD (Acceptance Test-Driven Development) | BDD (Behavior-Driven Development) |
|---|---|---|
| Fokus | Czy akceptujemy feature? | Czy system zachowuje się zgodnie z oczekiwaniami? |
| Język | Test cases w formie Given-When-Then | Scenariusze w formie Given-When-Then |
| Autor | Zespół (3 amigos: dev, tester, biznes) | Zespół (3 amigos) |
| Kiedy | Przed implementacją | Przed implementacją |
| Output | Testy automatyczne | Testy automatyczne + living documentation |

W praktyce: te same techniki, inna nazwa. Ten workshop dotyczy obu.

### Format Given-When-Then

```
Feature: [user-facing capability]

  Scenario: [concrete situation]
    Given [initial context]
    When  [action]
    Then  [expected outcome]
```

**Przykład (design-handoff-lab, feature: design token export):**

```
Feature: Export design tokens from Figma to JSON

  Scenario: Designer exports tokens from active Figma file
    Given I have a Figma file with 3 published variables
    When  I run the export script
    Then  I get a tokens.json file
    And   the file contains all 3 variables as key-value pairs
    And   the file is valid JSON (parses without errors)

  Scenario: Designer exports from empty file
    Given I have a Figma file with 0 published variables
    When  I run the export script
    Then  I get a tokens.json file with empty object {}
    And   the script exits with code 0 (no error)

  Scenario: Export fails on Figma API error
    Given the Figma API returns 500 error
    When  I run the export script
    Then  the script exits with code 1
    And   the error message is "Figma API unavailable, retry later"
```

### 3 Amigos Workshop (45-60 min, team mode)

**3 Amigos** = 3 perspektywy w jednej rozmowie:
- **Biznes / PO** — "Co user próbuje osiągnąć?"
- **Dev** — "Jak to zbudujemy?"
- **Tester / QA** — "Co może pójść nie tak?"

**Struktura (per user story):**

1. **(5 min) Story review** — PO czyta story i AC
2. **(15 min) Scenario brainstorm** — wszystkie 3 perspektywy piszą Given-When-Then
   - Start z happy path
   - Potem edge cases (empty, max, error states)
   - Potem non-functional (performance, security, accessibility)
3. **(10 min) Concrete examples** — "Dla tej sceny, daj mi konkretny przykład z liczbami"
4. **(10 min) Out-of-scope decision** — co celowo POMIJAMY w tej story
5. **(5 min) Automation decision** — które scenarios automatyzujemy, które zostają jako manual checks

**Solo adaptation:** Napisz 3-5 scenarios sam, ale dla każdego zadaj sobie pytania z 3 perspektyw:

```
Story: [user-facing capability]

Jako user, chcę [action], żeby [outcome].

Scenarios:
1. [happy path]
2. [empty state]
3. [error state]
4. [edge case]
5. [performance / non-functional]

Out of scope: [co celowo pomijam]
```

### Kiedy NIE używać BDD/ATDD

- **Throwaway prototypes** — overkill dla kodu, który żyje 1 sprint
- **Performance-critical code** — gdzie Given-When-Then przesłania rzeczywistą złożoność
- **Zespół <2 osób, bez QA** — bez 3 amigos, technika traci sens

### Output

Pliki `.feature` (Gherkin syntax) w repo, np. `features/tokens-export.feature`. Automatyzacja: Cucumber / Behave / SpecFlow / godog (zależy od stacku).

### Knowledge source

- **Specification by Example (Adzic, 2011)** — full BDD methodology
- **ATDD by Example (Podeswa, 2012)** — practical patterns

---

## Workshop 8: Customer Interview (Discovery Foundation)

### Purpose

Jeden z najważniejszych skilli w continuous discovery. Bez regularnych rozmów z klientami, cały OST / Outcomes / OKR staje się educated guessing. Ten workshop daje Ci strukturę pojedynczej rozmowy.

### Format (30-60 min interview, solo lub pair)

#### Pre-interview (15 min)

1. **Pick a topic** — jedno OST opportunity (Workshop 3), jedno assumption do zwalidowania
2. **Recruit 1 person** — kto pasuje do persony, ale jeszcze NIE jest power userem
3. **Set context** — "Rozmawiamy o [temat], to nie jest sprzedaż, chcę zrozumieć Twoje doświadczenie"
4. **Prepare 3-5 pytań otwartych** (patrz niżej)
5. **Pola do zapisków:** dosłowny cytat (verbatim), emocje, kontekst, "co zaskakujące"

#### Pytania otwarte (zamiast "czy..." użyj "co... jak... kiedy...")

| Zamiast | Pytaj |
|---|---|
| "Czy używasz X?" | "Opowiedz mi ostatni raz, kiedy próbowałeś zrobić [X]" |
| "Czy to jest problem?" | "Co jest najtrudniejsze w [obszar]?" |
| "Czy chciałbyś feature Y?" | "Gdybyś mógł magicznie rozwiązać jedną rzecz w [obszar], co by to było?" |
| "Czy kupisz to?" | "Jak teraz radzisz sobie z [problem]? Co Ci to kosztuje?" |
| "Jak oceniasz nasz produkt?" | "Co ostatnio sprawiło, że pomyślałeś 'wow, to działa' / 'ugh, nie znowu'?" |

#### W trakcie rozmowy (30-60 min)

- **80/20 rule** — Ty mówisz 20%, user 80%
- **Cisza jest OK** — po odpowiedzi, poczekaj 5 sekund. User doda kontekst.
- **"Tell me more"** — Twoje najlepsze pytanie. Użyj 5-10x w rozmowie.
- **Nie sprzedawaj** — gdy user mówi o problemie, NIE mów "mamy na to rozwiązanie!"
- **Zapisuj dosłownie** — parafrazy tracą niuanse. Pozwól sobie na nagranie (za zgodą).

#### Post-interview (15 min)

1. **Highlight reel** (2 min) — 3 cytaty, które Cię zaskoczyły
2. **Patterns** (5 min) — czy to potwierdza / obala assumption?
3. **New questions** (3 min) — co jeszcze nie wiem?
4. **OST update** (5 min) — update evidence column w OST

#### Output

```
## Customer Interview — [date]
Participant: [role/persona, NOT name if private]
Topic: [OST opportunity / assumption tested]

Top 3 verbatim quotes:
1. "[exact words]"
2. "[exact words]"
3. "[exact words]"

Patterns: [what this confirms/denies/challenges]
New questions: [what I still don't know]
OST update: [evidence column update]
```

### Anti-patterns (customer interview)

- **Pytania zamknięte** — "Czy podoba Ci się X?" → user odpowiada uprzejmie. Zmarnowany interview.
- **Sprzedawanie** — gdy mówisz o swoim produkcie, user przestaje mówić szczerze.
- **Za dużo pytań** — 20 pytań w 30 min = user czuje się jak na przesłuchaniu. Max 5-7.
- **Brak follow-up** — po interview nic się nie zmienia w OST. Wtedy po co rozmawiałeś?
- **Jednorazowość** — 1 rozmowa na rok to nie continuous discovery. Torres: minimum 1 rozmowa/tydzień.

---

## Anti-patterns for all workshops

- **No timebox.** Every workshop has a max time. When time's up, stop.
- **No output.** Every workshop produces a document/artifact. If nothing is written, it didn't happen.
- **Analysis paralysis.** Estimation is relative, not precise. Move on.
- **Skipping the why.** Story mapping without user context = useless exercise.
- **Not revisiting.** Discovery check-ins are useless if you don't act on them.
- **Build Trap.** "Musimy dowieźć X features" = output thinking. Outcomes first.
- **3 Amigos bez 3 osób.** BDD/ATDD bez dev+QA+PO traci sens. Solo: pisz z 3 perspektyw, ale bądź świadomy ograniczeń.
- **Customer interview jako sales pitch.** Gdy zaczynasz sprzedawać, user przestaje mówić szczerze.
- **OST bez evidence column.** Drzewo bez evidence to wishful thinking, nie discovery.
- **Workshop bez follow-up action.** Jeśli kończysz warsztat i nic nie commitujesz — zmarnowany czas.

---

## Framework Credits

Ten skill korzysta z frameworków i koncepcji opisanych w
[ATTRIBUTION.md](../../ATTRIBUTION.md):
- **User Story Mapping (Patton)** — journey mapping, release slicing
- **Continuous Discovery Habits (Torres)** — OST, assumption audit, opportunity review
- **Lean UX (Gothelf/Seiden)** — build-measure-learn, collaborative design
- **Escaping the Build Trap (Perri)** — outcomes vs outputs, Build Trap diagnostic
- **Lean Startup (Ries)** — build-measure-learn loop, MVP types (concierge, smoke test, fake door)
- **Planning Poker (Grenning)** — Fibonacci-scale estimation
- **Agile Estimating and Planning (Cohn)** — velocity forecasting
- **Specification by Example (Adzic, 2011)** — BDD/Gherkin scenarios
- **ATDD by Example (Podeswa, 2012)** — Acceptance Test-Driven Development patterns
- **Mom Test (Fitzpatrick, 2013)** — customer interview question design (anti-bias)
- **The Lean Startup Way (Maurya, 2012)** — Running Lean, problem interview framework
