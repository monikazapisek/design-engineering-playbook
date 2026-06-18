---
created: 2026-06-18
updated: 2026-06-18
version: 1.0
description: Metrics and OKR strategy — set inspiring Objectives and measurable Key Results, identify One Metric That Matters, distinguish actionable from vanity metrics. Christina Wodtke + Lean Analytics.
agent: agent-agile-master
attribution: ATTRIBUTION.md
extends: ../../AGENT.md
---

# Metrics Strategist

Strategia mierzenia sukcesu: OKR (Objectives & Key Results), OMTM (One Metric That Matters), rozróżnienie actionable vs vanity metrics. Dla founderów, PO i każdego, kto chce wiedzieć czy idzie w dobrym kierunku.

> **Filozofia:** mierz **zachowanie użytkownika** (co robią), nie **output** (co zbudowałeś). Melissa Perri nazywa to "Escaping the Build Trap". Bez tej zmiany mentalnej OKR-y zamieniają się w listę tasków.

---

## Purpose

Kiedy:
- budujesz coś i nie wiesz, czy to działa
- masz dashboard z 20 metrykami, ale żadna nie mówi ci co robić
- zespół (albo ty) pracuje ciężko, ale nie widać efektów
- chcesz ustalić kwartalny / sprintowy focus
- musisz pitchować inwestorom / stakeholderom i potrzebujesz jednej liczby

...wtedy ten skill pomaga: wybrać właściwe metryki, zbudować OKR-y, stworzyć rytuał weekly check-in.

---

## When to run

| Trigger | Output |
|---|---|
| "nie wiem czy to działa" | Audit metryk + proposal OMTM |
| "ustalmy OKR-y" / "Q[X] planning" | Pełny OKR draft |
| "mam za dużo metryk" | Actionable vs Vanity diagnostic + OMTM selection |
| "co founderzy chcą widzieć" | North Star Metric + input metrics |
| "weekly check-in, jak to robić" | OKR weekly review format |
| Retro ujawnia: "nie wiemy czy robimy postęp" | Propozycja metryki do śledzenia |

**NIE uruchamiaj** jeśli nie masz jeszcze produktu / user base. Najpierw `workshop-facilitation` Workshop 3 (Discovery), potem metryki.

---

## Duration

- **Metrics audit + OMTM selection:** 30-45 min
- **OKR quarterly planning:** 60-90 min
- **OKR weekly check-in:** 15-20 min (powtarzalne)
- **North Star Metric definition:** 45-60 min

---

## Knowledge to load (on demand)

| Situation | Reference |
|---|---|
| Pełne tło OKR | Wodtke, *Radical Focus* (2016) — Chapters 3-4 |
| Lean Analytics methodology | Croll & Yoskovitz, *Lean Analytics* (2013) — Chapters 1-2 |
| Outcomes vs outputs | Perri, *Escaping the Build Trap* (2018) — Chapters 2-3 |
| AARRR / Pirate Metrics | Wbudowane w tym skillu (nie wymaga ładowania) |
| North Star framework | Wbudowane |

**Reguła:** w tym skillu ładuj wiedzę tylko jeśli user chce deep dive. Większość frameworków jest wbudowana w SKILL.md.

---

## Framework 1: Actionable vs Vanity Metrics (Alistair Croll & Ben Yoskovitz)

### Definicja

| Type | Co mierzy | Czy prowadzi do decyzji? | Przykład |
|---|---|---|---|
| **Vanity** | Output / aktywność | NIE — cieszy ego, ale nie mówi co zmienić | "Mamy 10,000 pobrań apki" |
| **Actionable** | Zachowanie użytkownika → wpływ na biznes | TAK — widzisz co rośnie/maleje i wiesz co z tym zrobić | "30% pobierających wraca w ciągu 7 dni" |

### Diagnostic (15 min)

1. **Wylistuj** wszystkie metryki, które aktualnie śledzisz (max 10)
2. **Dla każdej** zadaj pytanie: "Gdy ta metryka spadnie o 20% w przyszłym tygodniu, czy wiem CO zrobić?"
   - **TAK** → actionable. Zostaw.
   - **NIE** → vanity. Zamień lub usuń.
3. **Jeśli masz 0 actionable** → masz krytyczny problem: budujesz w ciemno.

### Przykłady transformacji

| Vanity | → Actionable |
|---|---|
| 10,000 pobrań | 30% D7 retention |
| 50,000 page views | 8% conversion rate z landing page |
| 200 GitHub stars | 5 kontributorów w ostatnim kwartale |
| "Mamy 3 klientów" | NPS score 50+ (ci sami 3 klienci) |

---

## Framework 2: One Metric That Matters (OMTM)

### Definicja (Lean Analytics)

Jedna metryka, która w danym momencie jest **najważniejsza dla wzrostu**. Wszystkie inne metryki są drugorzędne. Zmienia się w czasie, gdy firma wchodzi w nowy stage.

### 5 Stages startupu i typowe OMTM

| Stage | Cel | Typowe OMTM |
|---|---|---|
| 1. **Empathy** | Zrozumieć problem | Liczba quality interviews / insights z discovery |
| 2. **Stickiness** | Czy użytkownicy wracają? | Retention rate (D1, D7, D30) |
| 3. **Virality** | Czy użytkownicy przyprowadzają innych? | Viral coefficient (K-factor) |
| 4. **Revenue** | Czy to się sprzedaje? | MRR / ARR / LTV |
| 5. **Scale** | Czy rośniemy efektywnie? | CAC payback period, burn multiple |

### OMTM Selection Workshop (30 min)

**Solo:**

1. Na którym stage'u jesteś? (bądź szczery — często ludzie myślą, że są na 4, a są na 1)
2. Z listy actionable metrics wybierz tę, która najlepiej reprezentuje przejście do następnego stage'u
3. Napisz: "Moje OMTM to [X], bo jestem na stage [N] i chcę przejść do [N+1]"
4. Przestań śledzić inne metryki jako primary. Mogą być secondary, ale OMTM = north star.

**Team (2-5 osób):**

1. **Round-robin:** każdy proponuje 1 OMTM (2 min na osobę)
2. **Whiteboard:** wszystkie propozycje, bez dyskusji
3. **Vote:** każdy ma 3 głosy (1 głos na jedną metrykę)
4. **Tie-break:** jeśli brak konsensusu → głosuje PO / founder (ostateczna decyzja)
5. **Commit:** ogłoś OMTM w zespole. Wszystkie decyzje productowe powinny uwzględniać wpływ na OMTM.

### Kiedy zmienić OMTM

- Twój aktualny OMTM jest stabilny i wysoki (np. retention 60%+) → czas przejść do następnego stage
- Twój biznes zmienia model (np. B2C → B2B) → reset
- Kwartalnie podczas OKR planningu → review czy OMTM nadal pasuje

---

## Framework 3: OKR (Objectives & Key Results) — Christina Wodtke

### Struktura

```
Objective:  [Inspiring, qualitative, time-bound goal]
             ↑ Co chcesz osiągnąć (nie jak)

Key Result 1:  [Measurable, quantitative, ambitious]
Key Result 2:  [Measurable, quantitative, ambitious]
Key Result 3:  [Measurable, quantitative, ambitious]
             ↑ Jak poznasz, że objective jest osiągnięty
```

### Zasady (Wodtke, "Radical Focus")

1. **Max 3 Objectives** na kwartał. Więcej = brak focus.
2. **3-5 Key Results per Objective**. Mniej = nieprecyzyjne. Więcej = zbyt rozproszone.
3. **Objectives są inspirujące**, nie mierzalne. "Zbudować najlepszą aplikację do X" ✓. "Zwiększyć retention o 50%" ✗ (to KR).
4. **Key Results są mierzalne i agresywne** (70% completion = success, 100% = za łatwe).
5. **Public visibility** — cały zespół widzi OKR-y.
6. **Weekly check-in** — 15 min, scentralizowany rytuał (patrz Framework 4).

### Przykład (solo founder, Q[X] 2026)

```yaml
Objective:  "Stać się zaufanym źródłem wiedzy o design systemach w PL"

KR1:  Publish 12 artykułów na Medium (avg 200 reads)
KR2:  500 subskrybentów newslettera do końca kwartału
KR3:  3 prelekcje / warsztaty w społeczności (meetup / konferencja)
```

### Anti-patterns OKR

| Anty-wzorzec | Dlaczego zły | Fix |
|---|---|---|
| KR = lista tasków | "Napisać 5 artykułów" to output, nie outcome | "5 artykułów, które generują 50 subskrypcji" |
| Objective = output | "Zbudować feature X" | "Sprawić, że użytkownicy kochają X" |
| 10 Objectives, 30 KRs | Brak focus | Wytnij do 3 Objectives, 3-5 KRs każdy |
| KR 100% zawsze | Za łatwe KRs = brak aspiracji | Powinny być 0.6-0.7 typical completion |
| Bez weekly check-in | OKR-y umierają po 2 tygodniach | Wprowadź 15 min weekly rytuał |
| OKR = performance review | Ludzie ustawiają łatwe KRs by wyglądać dobrze | OKR to learning tool, nie ocena |

---

## Framework 4: OKR Weekly Check-in (15 min)

### Format (Radical Focus)

Każdy KR ma 3 stany:

| State | Znaczenie |
|---|---|
| 🟢 **On track** | Będzie osiągnięty na czas |
| 🟡 **At risk** | Może nie być osiągnięty, ale mam plan |
| 🔴 **Off track** | Nie zostanie osiągnięty. Potrzebuję pomocy. |

### Check-in pytania (per KR)

1. **Confidence:** "Jestem [X]% pewny, że osiągnę ten KR" (X to liczba)
2. **Progress:** "Co zrobiliśmy w tym tygodniu, co przybliża nas do KR?"
3. **Blockers:** "Co nas blokuje? Kto/co może pomóc?"
4. **Next week:** "Co konkretnie zrobimy w następnym tygodniu?"

### Output (zapisuj co tydzień)

```
## OKR Check-in — Week [N], [date]

### Objective 1: [text]
- KR1: [text] — 🟡 60% confidence, progress: [1 line], next: [1 line]
- KR2: [text] — 🟢 80% confidence, progress: [1 line], next: [1 line]
- KR3: [text] — 🔴 30% confidence, blocker: [1 line], need: [1 line]

### Objective 2: [text]
- ...
```

### Red flags w weekly check-in

- Wszystko 🟢 przez 4+ tygodnie → KRs są za łatwe. Podnieś poprzeczkę.
- Wszystko 🔴 → Objective jest niewykonalny. Zmień go lub skasuj KR.
- Ciągle te same blokery → problem systemowy, nie wykonawczy. Eskalacja / pivot.
- Check-in trwa 5 min → znaczy, że nikt się nie przygotował. Wróć do dyscypliny.

---

## Framework 5: North Star Metric (NSM)

### Definicja

Jedna metryka, która najlepiej oddaje **wartość, którą dostarczasz użytkownikowi**. Różni się od OMTM tym, że:
- **NSM** jest stabilna (nie zmienia się co kwartał)
- **OMTM** zmienia się wraz ze stage'em firmy

### Przykłady NSM (z znanych firm)

| Firma | NSM |
|---|---|
| Airbnb | Noclegi zarezerwowane |
| Spotify | Czas słuchania muzyki |
| Facebook (Meta) | Daily Active Users |
| Uber | Rides completed per week |
| Medium | Czytelnicy (nie współtwórcy) |

### Definiowanie NSM (45 min)

**3 pytania testujące:**

1. **Czy reprezentuje value delivery?** "Czy wzrost tej metryki = więcej wartości dla użytkownika?" Jeśli nie → to vanity.
2. **Czy użytkownik ją napędza?** "Czy użytkownik swoim zachowaniem podbija tę metrykę?" Jeśli nie (np. "revenue" jest generowany przez sales, nie usera) → szukaj bliżej usera.
3. **Czy leading indicator?** "Czy zmiana w NSM przewiduje przyszły sukces biznesowy?" Jeśli NSM rośnie, ale revenue spada → to nie prawdziwa NSM.

**Warsztat (solo lub team, 30 min):**

1. Wypisz 5-8 metryk, które uważasz za ważne
2. Przejdź 3 pytania testujące dla każdej
3. Wybierz 1, która przechodzi wszystkie 3
4. Zidentyfikuj 2-3 **input metrics** (co napędza NSM) — te mierz co tydzień

**Przykład:**

```
NSM:         Weekly active users completing ≥3 sessions
Input 1:     Onboarding completion rate (% who finish first session)
Input 2:     D7 retention (returning users)
Input 3:     Avg sessions per WAU per week
```

Wszystkie 3 input metrics powinny rosnąć, żeby NSM rósł. Jeśli NSM rośnie, ale któryś input spada → masz ukryty problem.

---

## Solo Application: "I'm a one-person company, what do I track?"

### Minimum Viable Metrics (MVM) — 3 metryki max

1. **1 North Star Metric** (reprezentuje wartość dla usera)
2. **1 Counter-metric** (reprezentuje zdrowie systemu, np. error rate, churn, burn)
3. **1 Velocity metric** (reprezentuje tempo twojej pracy, np. stories per sprint)

Przykład dla solo design-handoff-lab:
```
NSM:         Designerów, którzy używają wygenerowany tokens w Storybook ≥1x/tydzień
Counter:     Critical bugs reported per release
Velocity:    Komponenty shipped per sprint
```

### Kiedy dodać kolejną metrykę?

Dopiero gdy masz 4+ tygodnie danych dla poprzednich i wiesz, że podejmujesz na ich podstawie złe decyzje. Więcej metryk ≠ lepsze decyzje.

---

## Anti-patterns

| Anti-pattern | Dlaczego zły | Fix |
|---|---|---|
| 20 metryk w dashboardzie | Nie wiesz, która jest ważna | OMTM + 2-3 input metrics. Reszta to noise. |
| Metryki bez actionability | "Mamy 1000 userów" — i co? | Zawsze pytaj: "gdy to spadnie, co zrobię?" |
| OKR-y jako performance review | Ludzie grają gierkę (ustawiają łatwe KRs) | OKR = learning tool. Oceniaj aspirację, nie completion. |
| Q1 OKR ustawiony w Q1 Week 8 | Za późno. W Week 8 powinieneś mieć już 6 weekly check-inów | Ustawiaj OKR w ostatnim tygodniu poprzedniego kwartału. |
| Bez weekly check-in | OKR-y umierają | 15 min co tydzień, non-negotiable. |
| NSM = revenue | Revenue to outcome, nie leading indicator | NSM powinno poprzedzać revenue w łańcuchu przyczynowym. |
| Kopiowanie OKR-ów Google / Facebook | Twoje stage i kontekst są inne | Zacznij od pytania: "Na jakim stage'u jestem?" (Framework 2) |
| Vanity metrics w pitch deck | Inwestorzy to widzą. Podważa wiarygodność. | Pitch = NSM trajectory + input metrics. Wyjaśnij dlaczego te metryki. |

---

## Integration z innymi skilleami

| Skill | Jak współpracuje |
|---|---|
| `sprint-planning/SKILL.md` | OKR-y → Sprint Goal. Sprint Selection criteria powinny uwzględniać wpływ na KR. |
| `retrospective/SKILL.md` | Co 4-6 sprintów: "Czy nasze effort przybliża nas do KRs?" Dodaj do Stage 1 retro review. |
| `workshop-facilitation/SKILL.md` Workshop 3 (Discovery) | Discovery insights powinny informować NSM. Nowe user insight = "czy nasza NSM nadal pasuje?" |
| `change-agent/SKILL.md` | Jeśli wprowadzasz OKR-y do zespołu, który ich nie używa → użyj change-agent dla adoption. |

---

## When this skill is NOT enough

- **Strategia biznesowa, model revenue, pricing** → poza scope. Konsultuj z founder / advisor.
- **Analityka danych (SQL, dashboards, segmentacja)** → to implementation, nie strategy. Ten skill mówi CO mierzyć, nie JAK mierzyć.
- **A/B testing methodology** → wbudowane podstawy, ale dla advanced → `data-analyst` agent (jeśli istnieje) lub data team.
- **Statystyczna istotność, sample size** → statystyka, nie agile.

---

## Framework Credits

Ten skill korzysta z frameworków i koncepcji opisanych w
[ATTRIBUTION.md](../../ATTRIBUTION.md):

- **Radical Focus (Wodtke, 2016)** — OKR methodology, weekly check-in format
- **Lean Analytics (Croll & Yoskovitz, 2013)** — OMTM, 5 stages of startup, actionable vs vanity
- **Measure What Matters (Doerr, 2018)** — OKR case studies, CFR (Conversations, Feedback, Recognition) — pominięte tu, bo dotyczy performance management, nie product strategy
- **Escaping the Build Trap (Perri, 2018)** — outcomes vs outputs, anti-pattern output thinking
- **North Star Playbook (Amplitude)** — NSM framework, input metrics
- **Lean Startup (Ries, 2011)** — build-measure-learn loop, validated learning
