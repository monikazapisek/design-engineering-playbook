---
created: 2026-06-18
updated: 2026-06-18
version: 1.3
description: Retrospective ceremony — five-stage pattern adapted for solo practitioner, with OKR/quarterly review integration, Derby/Larsen Prime Directive as opening ceremony
agent: agent-agile-master
attribution: ATTRIBUTION.md
extends: ../../AGENT.md
---

# Retrospective

## Purpose

Inspect the last sprint and adapt. Primary mechanism for continuous improvement (kaizen). For solo: structured self-reflection that leads to concrete changes.

## When to run

- **End of every sprint.** No exceptions. Even if "nothing happened."
- After a major milestone or failure
- When process feels broken

## Duration

- **Solo:** 20-30 minutes
- **With context:** up to 45 minutes

## Knowledge to load (on demand)

| Situation | Reference |
|---|---|
| Retro feels stale/boring | Cohn, *Better Retrospectives* — Menu + Engaging formats (Modules 3-4) |
| Retro not producing action items | Cohn, *Better Retrospectives* — Action Items (Module 5) |
| Need facilitation techniques | Cohn, *Better Retrospectives* — Facilitation (Module 2) |
| Retro keeps surfacing same issues | Cohn, *Retrospectives Repair Guide* (Mountain Goat Software) |

## The Five Stages (Derby & Larsen pattern)

### Stage 0: Prime Directive (opening ceremony, 2 min)

**Purpose:** Establish psychological safety before anything else. Bez tego ludzie (albo ty sam) będą bronić, racjonować, obwiniać zamiast analizować proces.

**Pełny tekst Prime Directive** (Esther Derby & Diana Larsen, "Agile Retrospectives", 2006):

> *"Regardless of what we discover, we understand and truly believe that everyone did the best job they could, given what was known at the time, their skills and abilities, the resources available, and the situation at hand."*

> *"At the end of a project everyone knows how to do it better. The next time we will all do it better."*

**Jak użyć:**

**Solo (czytaj na głos lub przepisz na początku każdej retro):**
- Napisz Prime Directive na kartce i powieś nad biurkiem
- Przed rozpoczęciem retro przeczytaj go na głos. To nie rytuał — to deklaracja: "w tej przestrzeni zakładamy dobre intencje"
- Jeśli złamiesz zasadę w trakcie retro (zaczynasz się obwiniać: "powinienem był..."), wróć do Prime Directive: "co BYŁO możliwe z wiedzą, którą miałem wtedy?"

**Team (facylitator czyta na głos na początku każdego retro):**
- Facylitator czyta lub zacytuje z pamięci — nie czytaj z kartki (pokazuje, że to integralne, nie dekoracja)
- Jeśli ktoś zaczyna obwiniać kogoś, przerwij i powiedz: "Prime Directive — zakładamy dobre intencje. Co sprawiło, że to była najlepsza decyzja w tamtym momencie?"
- Nie jako wymówka dla złej pracy — jako bezpieczna przestrzeń do analizy procesu, nie osądu osób

**Anty-wzorce:**
- "To oczywiste, po co to czytać" → właśnie dla tych retro, gdzie NIE jest oczywiste (kryzys, napięcie)
- "Przeczytajmy to szybko" → tempo zabija intencję. 30 sekund ciszy po przeczytaniu.
- "To nie działa, bo i tak ludzie obwiniają" → bo nie internalizujesz, tylko recytujesz. Facylitator musi sam w to wierzyć.

---

### Stage 1: Set the Stage (3 min)

**Purpose:** Open the retro, get into reflection mode.

**Solo technique — "Sprint Movie":**
If this sprint were a movie, what title would it be? Write 1-3 titles. Why?

Examples:
- "Groundhog Day" — same problems repeating
- "The Martian" — solving problems alone, creative solutions
- "The Social Network" — rapid iteration, shipping fast

**Alternative — "One Word":** Describe the sprint in one word. Then explain why.

### Stage 2: Gather Data (7 min)

**Purpose:** What actually happened? Facts, not feelings.

**Solo technique — "Sprint Timeline":**
Walk through the sprint day by day. For each day, note:
- What I planned to do
- What I actually did
- What surprised me

**Or use "4 Ls" (adapted for solo):**
- **Loved:** What was energizing? What did I enjoy?
- **Liked:** What went well? What was satisfying?
- **Lacked:** What was missing? What do I wish I had?
- **Longed For:** What do I want more of next sprint?

**Output:** 2-3 key observations. Not 10. Focus.

### Stage 3: Generate Insights (7 min)

**Purpose:** Why did these things happen? Root causes.

**Solo technique — "5 Whys" (pick 1-2 items max):**
For each key observation, ask "why?" five times.

Example:
1. "I didn't finish the button spec." Why?
2. "I spent too time on token mapping." Why?
3. "I didn't know which tokens to map." Why?
4. "I didn't review the Figma file before starting." Why?
5. "I skipped the preflight step." → **Root cause: skipping preparation**

**Solo technique — "Fishbone" (for complex issues):**
Categorize causes: People, Process, Tools, Environment.

**Output:** 1-2 root causes, clearly stated.

### Managing difficult emotions in retro (kiedy Stage 3 wychodzi poza analizę)

**Kiedy to użyć:** Gdy retro zamiast analizy procesu staje się sesją terapeutyczną — ktoś płacze, ktoś krzyczy, ktoś milczy godzinami, ktoś wychodzi. Albo: ty sam zaczynasz internalizować i masz fizyczną reakcję.

**Zasada facylitatora:** neutralne komentowanie zachowania + przywracanie koncentracji na celu.

| Sygnał | Co NIE robić | Co robić |
|---|---|---|
| **Płacz** (ktoś płacze po podzieleniu się porażką) | "Nie płacz", "Ogarnij się", szybkie przejście do następnego tematu | "Widzę, że to Cię poruszyło. Dziękuję za odwagę, że to powiedziałeś/aś. Chcesz kontynuować, czy zrobić przerwę?" → czekaj na odpowiedź |
| **Krzyk / agresja** (ktoś podnosi głos, jest sarkastyczny) | "Uspokój się", "To nie jest personalne", defensywność | "Widzę, że jesteś zdenerwowany/a. Co konkretnie Cię tak poruszyło?" → pozwól wypowiedzieć, NIE eskaluj głosem |
| **Cisza** (ktoś milczy przez 5+ min) | "Dlaczego się nie odzywasz?", wymuszanie odpowiedzi | "Widzę ciszę. Czy masz coś do powiedzenia, czy cisza jest Twoją odpowiedzią?" → uszanuj obie opcje |
| **Wyjście** (ktoś wychodzi w trakcie) | "Wracaj, omawiamy ważne rzeczy" | "OK, możesz wrócić kiedy będziesz gotowy/a. Kto chce kontynuować?" |
| **Ty sam w emocjach** (solo retro, czujesz overwhelm, złość na siebie) | Kontynuowanie na siłę, udawanie że OK | Przerwij retro. 10 min spacer / woda. Wróć do Prime Directive. Może przenieś na jutro. |

**Solo technika:** Jeśli podczas retro zaczynasz odczuwać silne emocje (złość, wstyd, bezradność) — to nie znaczy, że retro się nie udało. To znaczy, że dotknąłeś/aś czegoś ważnego. Zapisz: "[ten temat] wymaga osobnej sesji, nie retro". Wróć do tematu z `agent-mindful-coach` lub z terapeutą.

**Po intensywnej retro:**
- Zapisz 1-2 zdania: "Co wywołało emocje? Dlaczego?"
- Zaplanuj 1:1 z osobą (lub z sobą), żeby to dograć poza retro
- Następna retro zacznij od Prime Directive — tym bardziej potrzebne po trudnej sesji

**Anty-wzorce:**
- Facylitator jako terapeuta — to nie rola SM/coacha. Bezpieczna przestrzeń TAK, terapia NIE.
- "Emocje są nieprofesjonalne" → emocje są informacją. Tłumienie = ukryte dane.
- "Mamy mało czasu, idźmy dalej" → pomijanie = temat wraca silniejszy w następnej retro
- Rozwiązywanie w grupie spraw osobistych — publiczne odgrzebywanie ran = naruszenie bezpieczeństwa

### Stage 4: Decide What to Do (7 min)

**Purpose:** Concrete action items for next sprint.

**Solo technique — "SMART Action Items":**

Format:
```
Action: [specific thing I will do]
When: [in next sprint / before next retro / immediately]
Success: [how I'll know it worked]
```

**Rules:**
- **Max 3 action items.** More = nothing gets done.
- **Be specific.** "Improve estimation" → bad. "Use planning poker for all stories >3 points" → good.
- **Stack small steps.** Big problems need incremental progress, not one big fix.

Example:
```
Action: Review Figma file BEFORE starting any component work (preflight)
When: Every component start
Success: Zero "I didn't know this was there" moments
```

### Stage 5: Close (3 min)

**Purpose:** Recap, commit, close definitively.

**Solo technique — "Commitment Statement":**
Write one sentence: "Next sprint I will [action] because [insight]."

**Optional — "Temperature Check":**
Rate the retro itself: 1-5. Was it useful? What to change about the format?

**Output:** Written commitment in `memory/decisions.md`:
```
## Retro Sprint [N] — [date]
Key insight: [one sentence]
Action items:
1. [action] (success criteria: [how to measure])
2. [action] (success criteria: [how to measure])
3. [action] (success criteria: [how to measure])
Commitment: [one sentence]
```

## Retro formats to rotate

Don't use the same format every time. Rotate to keep it fresh:

| Format | Best for | Time |
|---|---|---|
| Sprint Movie + 4 Ls | General purpose | 25 min |
| Starfish (Keep/More/Less/Start/Stop) | Process-focused | 20 min |
| Sailboat (Wind/Anchors/Island/Rocks) | Visual thinkers | 25 min |
| Timeline + 5 Whys | When things went wrong | 30 min |
| Rose/Thorn/Bud | Quick and simple | 15 min |

**Use Retromat (retromat.org) for inspiration** — free tool to mix and match retro activities.

## Anti-patterns to watch

- **Skipping retro.** "Nothing to discuss" = biggest anti-pattern. Always do it.
- **No action items.** Retro without actions = venting session. Always produce ≤3 SMART items.
- **Same format every time.** Boredom kills retros. Rotate formats.
- **Too many items.** >3 actions = none will be done. Cut to essentials.
- **Blame culture.** Even solo: blame the process, not yourself. "I failed" → "The process didn't support me."
- **Not reviewing past actions.** Start every retro by checking: did last sprint's actions happen?

## After retro

- Log actions to `memory/decisions.md`
- Update backlog if needed
- Start next sprint with the actions in mind
- Check actions at next retro (Stage 1: review commitments)

---

## Extended: Quarterly OKR Review (co 6-8 sprintów)

Standardowy retro działa co sprint. Ale **co kwartał** (lub co 6-8 sprintów dla ultra-lean) potrzebujesz głębszego review, który patrzy **nie na ostatni sprint, ale na ostatni kwartał**. To jest most między sprint-level i OKR-level.

### Kiedy uruchomić

- Co 6-8 sprintów (co kwartał dla typowego tempa)
- Na koniec kwartału kalendarzowego
- Gdy OKR-y mają formalny deadline
- Gdy czujesz "kręcimy się w kółko" — potrzebujesz bird's eye view

### Czas

- **Solo:** 45-60 min
- **Team (2-5 osób):** 90-120 min

### Format (inspirowany Wodtke + Derby & Larsen)

#### Stage 1: OKR Recall (10 min)

Otwórz OKR-y z początku kwartału. Dla każdego Key Result zapisz:
- 🟢 Achieved (>= 100%)
- 🟡 Partially achieved (60-99%)
- 🔴 Missed (< 60%)

#### Stage 2: Sprint Timeline (10 min)

Przejdź sprint po sprincie. Dla każdego sprintu 1-2 słowa: co się działo? Wzloty, upadki, zmiany kierunku.

#### Stage 3: Pattern Recognition (15 min)

Zadaj pytania (solo lub w grupie):
- "Co NAS zaskoczyło w tym kwartale?" (pozytywne i negatywne)
- "Które KRs osiągnęliśmy łatwo? Co to mówi o naszych aspiracjach?"
- "Które KRs spudłowały? Dlaczego — zły target, czy zła strategia?"
- "Czy pracowaliśmy nad właściwymi rzeczami?"

#### Stage 4: Learning Extraction (15 min)

Wypisz 3-5 najważniejszych lekcji:

```
Lekcja: [co zrozumieliśmy]
Wynik:  [jak to zmieni nasze podejście w przyszłym kwartale]
```

#### Stage 5: Next Quarter Preview (10 min)

- Czy obecne OKR-y nadal mają sens? (Pivot, czy hold?)
- Czy chcemy je utrzymać, dostosować, czy wymienić?
- Czy OMTM (z `metrics-strategist`) wymaga rewizji?

#### Output

```
## Quarterly Review — Q[X] [year]
OKR outcome: 🟢 X / 🟡 X / 🔴 X

Top 3 lessons:
1. [...]
2. [...]
3. [...]

Decision: [hold OKRs / pivot / adjust]
Next quarter preview: [1-2 zdania co się zmieni]
```

### Anty-wzorce (quarterly review)

- **Zamienianie w performance evaluation** — "Kto zawalił?" vs "Co się nauczyliśmy?"
- **Skip bo "mamy OKR-y, wystarczy"** — OKR weekly check-in to nie to samo co quarterly reflection
- **Brak Stage 1** — bez otwarcia OKR-ów, łatwo wpaść w recency bias (tylko ostatni sprint)
- **Setup na failure** — "Musimy w tym kwartale osiągnąć X" → gdy nie dowieźliśmy, retro = wstyd. Nie. Uczymy się.

### Kiedy NIE potrzebujesz tego formatu

- **Mniej niż 4 sprinty od ostatniego review** — za wcześnie, repeat
- **Dramatyczny pivot / zmiana produktu** — potrzebujesz pełnego strategic review, nie quarterly
- **Brak OKR-ów** — wtedy ten review to retrospective z dodatkowym krokiem, nie pełny quarterly

### Pełna integracja z metrics-strategist

Ten review jest **konsumpcją** weekly OKR check-in (patrz `metrics-strategist/SKILL.md` Framework 4). Jeśli robisz weekly check-ins regularnie, ten quarterly review to synteza, nie analiza od zera.

---

## Framework Credits

Ten skill korzysta z frameworków i koncepcji opisanych w
[ATTRIBUTION.md](../../ATTRIBUTION.md):
- **Agile Retrospectives (Derby & Larsen)** — 5-stage pattern, Sailboat, Starfish, Timeline
- **Better Retrospectives (Cohn)** — action items, facilitation techniques
- **Retrospectives Repair Guide (Cohn)** — fixing broken retros
- **SMART Goals (Doran)** — action item format
- **5 Whys (Toyoda / Toyota)** — root cause analysis
- **Fishbone Diagram (Ishikawa)** — complex issue categorization
- **Radical Focus (Wodtke)** — quarterly review cadence, OKR vs sprint reflection
- **Objective-Based Planning (Cagan)** — outcomes as anchor for retrospective reflection
