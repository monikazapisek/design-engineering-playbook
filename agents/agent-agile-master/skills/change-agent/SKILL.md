---
created: 2026-06-18
updated: 2026-06-18
version: 1.0
description: Change management and facilitation — Kotter 8 steps, ORID structured conversation, Information Radiators. Dual mode: personal change narrative and organizational transformation.
agent: agent-agile-master
attribution: ATTRIBUTION.md
extends: ../../AGENT.md
---

# Change Agent

Facylitacja zmiany: model Kottera (8 kroków transformacji), struktura rozmowy ORID (Institute of Cultural Affairs), wizualizacja pracy (Information Radiators). Dla liderów, którzy wprowadzają agile, dla founderów pivotujących produkt, dla każdego, kto chce świadomie poprowadzić zmianę.

> **Tryb pracy:** dual mode jak w `team-healer/SKILL.md`:
> - **Solo mode** — ty sam/sama przechodzisz przez zmianę (karierę, nawyk, kierunek projektu)
> - **Team / Org mode** — moderujesz zmianę w grupie 2-5 osób (team) lub 5+ (organizacja)
>
> Kotter oryginalnie dotyczy organizacji — adaptacja solo jest nietrywialna ale możliwa (zamieniasz "firma" na "ja").

---

## Purpose

Kiedy:
- wprowadzasz agile do zespołu, który tego nie zna
- chcesz pivotować produkt / kierunek, ale ludzie (albo ty) się boją
- wiesz, że "coś trzeba zmienić", ale nie wiesz od czego zacząć
- masz ważną rozmowę i chcesz ją przeprowadzić strukturalnie
- chcesz, żeby proces był widoczny dla wszystkich (visual management)

...ten skill daje framework, nie gotowe odpowiedzi. Output: plan zmiany + rytuały podtrzymujące.

---

## When to run

| Trigger | Tryb |
|---|---|
| "chcę wprowadzić agile w naszym zespole" | Org mode (5+ osób) |
| "pivotuję produkt, jak to zakomunikować" | Solo lub Team |
| "muszę mieć trudną rozmowę z szefem / klientem" | Solo (ORID script) |
| "tablica w pokoju jest bezużyteczna" | Either (Information Radiators) |
| "ludzie nie kupują mojej wizji" | Either |
| "nasz process umiera, potrzebuję refresh" | Team mode |
| "sam chcę zmienić nawyk / kierunek" | Solo mode (Kotter adapted) |

**NIE uruchamiaj** jeśli zmiana dotyczy:
- zwolnień / cięć (potrzebujesz HR + prawnika, nie frameworku agile)
- bezpośredniego kryzysu (ogień w domu — najpierw gaś, potem analizuj)
- wartości osobistych (religia, polityka, etyka — inne ramy)

---

## Duration

- **Solo Kotter reflection:** 60-90 min (jednorazowo, ale cyklicznie co kwartał)
- **Team change kickoff:** 90-120 min
- **ORID conversation:** 30-60 min
- **Information Radiator design:** 30-60 min

---

## Knowledge to load (on demand)

| Situation | Reference |
|---|---|
| Pełne tło Kotter 8 steps | Kotter, *Leading Change* (1996) — Chapters 1-3 |
| ORID deep dive | Wbudowane w tym skillu (wystarczające dla praktyki) |
| Information Radiators | Wbudowane + Poppendieck, *Lean Software Development* (2003) |
| Change management w agile | Cohn, *Scrum Repair Guide* (Mountain Goat Software) — Module 6: Adoption |

**Reguła:** Kotter w szczegółach ma 8 kroków z wieloma subtletnościami. Dla większości sytuacji wbudowany opis wystarcza. Ładuj PDF tylko jeśli user chce deep dive.

---

## Framework 1: Kotter 8 Steps (adapted for solo + team)

### Original (organizacja) vs Solo (jednostka)

| Krok | Org mode (Kotter original) | Solo mode (adapted) |
|---|---|---|
| 1. Create urgency | "Sprzedaż spadnie 30% w rok" | "Jeśli nie zmienię X, w Q[X] nie osiągnę Y" |
| 2. Build coalition | Leadership team wspiera | Znajdź 1-2 osoby, które też chcą zmiany (accountability partners) |
| 3. Form vision | "Będziemy najszybszą firmą w branży" | "Chcę być osobą, która [wizja]" |
| 4. Communicate vision | Town hall, all-hands | Napisz manifest, publikuj, podziel się z 3 osobami |
| 5. Remove obstacles | Zmiany strukturalne, budżet | Zidentyfikuj 1 blocker, który uniemożliwia start |
| 6. Create short wins | Pilots, quick wins | Pierwszy tydzień: 1 mała, dostarczalna wygrana |
| 7. Sustain acceleration | Rytuały, celebrations | Cotygodniowy review: "Co się udało?" |
| 8. Institute change | Nowe DNA firmy | Zinternalizuj nawyk, nie wymaga już świadomego effort |

### 70% failure rate — dlaczego zmiany nie udają się

Kotter po 30 latach badań: **70% transformacji zawodzi**. Najczęstsze przyczyny:
- Brak pilności (krok 1) — "to nie jest tak źle"
- Koalicja za słaba (krok 2) — tylko top leader wierzy
- Wizja za ogólnikowa (krok 3) — "będziemy lepsi"
- Komunikacja jednorazowa (krok 4) — ogłoszenie zamiast powtarzania
- Brak short wins (krok 6) — zmiana trwa miesiącami bez widocznych efektów
- Victory declared too early (krok 7-8) — "już się zmieniliśmy", a tak naprawdę nie

### Solo Diagnostic: Where are you in the 8 steps?

Wybierz zmianę, którą próbujesz przeprowadzić. Oceń każdy krok 1-5:

| Krok | Pytanie | Score |
|---|---|---|
| 1 | Czy mam jasny, emocjonalny powód "dlaczego teraz"? | /5 |
| 2 | Czy mam wsparcie (ludzie, nie tylko ja)? | /5 |
| 3 | Czy potrafię powiedzieć wizję w 1 zdaniu? | /5 |
| 4 | Czy regularnie o tym mówię / piszę? | /5 |
| 5 | Czy wiem, co konkretnie mnie blokuje? | /5 |
| 6 | Czy mam zaplanowane 1-2 quick wins? | /5 |
| 7 | Czy mam rytuał podtrzymujący (np. weekly check-in)? | /5 |
| 8 | Czy widzę zmianę jako "nowy normal", czy wciąż "projekt"? | /5 |

**Najniższy score = następny krok do pracy.** NIE przeskakuj. Krok 3 (wizja) bez kroku 1 (pilność) to wishful thinking.

### Team Kickoff Workshop (90 min)

**Struktura:**

1. **Step 1 — Pilność (20 min)**
   - Round-robin: "Co się stanie, jeśli NIE zmienimy nic w ciągu 6 miesięcy?"
   - Facylitator: zapisz 3-5 najczarniejszych scenariuszy
   - Output: 1 zdanie pilności w stylu "Jeśli nie [X], to [Y]"
2. **Step 2 — Koalicja (10 min)**
   - "Kto z nas jest gotów poświęcić czas na tę zmianę? Kto może?"
   - Output: lista 3-5 osób, które są w coalition
3. **Step 3 — Wizja (20 min)**
   - Burza mózgów: każdy pisze 1 zdanie wizji (2 min)
   - Grupowanie podobnych
   - Wspólne pisanie 1 wersji finalnej
   - Kryteria dobrej wizji: [poniżej]
4. **Step 4 — Komunikacja (15 min)**
   - "Jak zakomunikujemy wizję osobom poza coalition?"
   - Output: 3 kanały komunikacji (np. email, all-hands, 1:1 z szefem)
5. **Step 5 — Blockery (15 min)**
   - "Co nas blokuje? Struktura? Proces? Ludzie? Nawyki?"
   - Output: top 1-2 blockers do natychmiastowego usunięcia
6. **Step 6 — Quick wins (10 min)**
   - "Co możemy zrobić W TYM TYGODNIU, co pokazuje że zmiana się dzieje?"
   - Output: 1 konkretny quick win z ownerem i deadline'em

**Dobra wizja (po Kotter):**
- Wyobrażalna (widzisz ją jak film)
- Pożądana (ludzie CHCĄ do niej dążyć, nie tylko "muszą")
- Wykonalna (realistyczna w 3-5 lat)
- Skupiona (jeden kierunek, nie 5)
- Elastyczna (daje miejsce na interpretację i inicjatywę)

**Zła wizja (anty-wzorzec):**
- "Będziemy najlepsi" — za ogólnikowe
- "Zwiększymy przychody o 50%" — to KR, nie wizja
- "Zrobimy agile" — środek, nie cel

---

## Framework 2: ORID Structured Conversation

### Co to jest ORID?

Model facylitacji rozmowy z Institute of Cultural Affairs (ICA), używany w:
- retrospektywach
- 1:1 meetings
- discovery interviews
- trudnych rozmowach
- design thinking sessions

4 poziomy kolejno:

```
O — Objective    (Co widać / słyszeć? Fakty.)
  ↓
R — Reflective   (Jak się z tym czujesz? Reakcje.)
  ↓
I — Interpretive (Co to znaczy? Dlaczego to ważne?)
  ↓
D — Decisional   (Co z tym zrobimy? Konkretna decyzja.)
```

### Dlaczego ta kolejność ma znaczenie

Większość ludzi przeskakuje do "D" (decyzja) bezpośrednio, pomijając O-R-I. Efekt: decyzje na podstawie ukrytych założeń i emocji, które nie zostały nazwane.

ORID wymusza:
- Fakty najpierw (nie opinie)
- Emocje potem (nie ukryte)
- Interpretacja dopiero po zrozumieniu perspektywy
- Decyzja jako konsensus, nie narzucenie

### Solo ORID (własna refleksja, 20-30 min)

Użyj gdy masz ważną decyzję do podjęcia i czujesz, że coś ci umyka.

**Format (pisemnie):**

```
## Decyzja: [co rozważam]

### O — Objective (fakty)
- Co dokładnie wiem o sytuacji?
- Jakie dane, liczby, fakty mam?
- Co powiedziały konkretne osoby?

### R — Reflective (uczucia)
- Jak się z tym czuję? (lista emocji)
- Co mnie niepokoi / cieszy / złości?
- Jak moje ciało reaguje? (napięcie, spokój)

### I — Interpretive (znaczenie)
- Co to dla mnie znaczy? Dlaczego to ważne?
- Jakie wartości są w grze?
- Co by się stało, gdybym wybrał A vs B? Dla kogo?

### D — Decisional (decyzja)
- Co konkretnie zrobię?
- Kiedy?
- Jak poznam, że to była dobra decyzja?
```

### Team ORID (facylitated 1:1 lub mała grupa, 30-60 min)

**Przykład: trudna rozmowa z kolegą o spadającej jakości jego pracy**

**Facylitator (lub ty, jeśli rozmawiasz sam):**

**O (10 min):**
- "W ostatnim sprincie zauważyłem, że 2 z 4 twoich stories wróciły z review z feedbackiem o niepełnych testach. To było 50% twoich commitów, podczas gdy średnia zespołu to 15%."

**R (10 min):**
- "Jak się czujesz, kiedy to mówię? Czy jest coś, co ciężko ci w ostatnim czasie — poza pracą — co wpływa na twoją dostępność?"
- [Czekaj na odpowiedź. Nie bagatelizuj, nie dodawaj "ale".]
- "Widzę, że cię to dotyka. Czy jest coś, w czym mógłbym pomóc?"

**I (15 min):**
- "Co Twoim zdaniem jest przyczyną tej sytuacji? Jak to widzisz?"
- "Co by pomogło — więcej review, mniej scope, inny proces, szkolenie z testów?"
- "Jak twoja praca wpływa na resztę zespołu?"

**D (10-15 min):**
- "Co konkretnie zrobisz w następnym sprincie?"
- "Czego potrzebujesz ode mnie / zespołu?"
- "Kiedy się zobaczymy, żeby to sprawdzić?"

**Zasady facylitacji ORID:**
- NIE przeskakuj poziomów
- NIE dodawaj interpretacji za rozmówcę
- NIE rozwiązuj problemu w fazie O ani R (to czas słuchania)
- Decyzja (D) to KONSENSUS, nie dyktat

---

## Framework 3: Information Radiators (Visual Management)

### Co to jest?

Tom Poppendieck: "Information radiator is a display placed in a high-traffic area that passers-by can read without effort." Zasady:
- Wysoki ruch ludzi (każdy widzi)
- Czytelny na odległość (1-2 metry)
- Aktualizowany na bieżąco
- Nie wymaga zapytania "jaki jest status"

### 8 typów Information Radiators (kanon)

| Type | Best for | Format |
|---|---|---|
| **Kanban board** | Flow pracy, WIP limits | Kolumny: Backlog → In Progress → Review → Done |
| **Burndown chart** | Sprint progress | Oś X = dni sprintu, Y = pozostałe story points |
| **Cumulative flow diagram** | Trend flow w czasie | Wykres warstwowy: ile w każdej kolumnie dziennie |
| **Sprint board** | Daily standup | Stories przypisane do osób, status widoczny |
| **Story map** | User journey, MVP scope | Patrz `workshop-facilitation/SKILL.md` |
| **Heat map** | Patterns (np. gdzie są bugi) | Kolorowa siatka z natężeniem |
| **OKR dashboard** | Quarterly progress | Status per KR (🟢🟡🔴), ownership |
| **Decision log** | "Dlaczego tak zrobiliśmy?" | Chronologiczna lista kluczowych decyzji |

### Design Principles

1. **Big and visible.** Tablica 2x1m w pokoju, lub full-screen dashboard w monitorze.
2. **Updated in real-time.** Nie raz na tydzień. Codziennie lub przy każdej zmianie stanu.
3. **No "ask" needed.** Jeśli ktoś musi zapytać "co to znaczy" → redesign.
4. **Single source of truth.** NIE DUPLIKUJ w innych narzędziach. "Wszystko jest na tablicy" musi być prawdą.
5. **Public by default.** Nikt nie ma prywatnych statusów. Wszyscy widzą to samo.

### Solo adaptation: Personal Information Radiators

Nawet solo, wizualizacja pomaga. Opcje:

1. **Physical wall** — tablica korkowa w domu, post-ity w 3 kolumnach (To do / Doing / Done)
2. **Markdown dashboard** — `status.md` w root projektu, aktualizowany codziennie
3. **GitHub Project / Notion** — dla zespołu rozproszonego

**Anty-wzorce:**
- "Beautiful dashboard, ale nikt nie patrzy" → zły placement lub zbyt skomplikowany
- "Tablica, ale aktualizowana co tydzień" → nie jest radiator, jest raportem
- "Tablica, ale ma 50 metryk" → za dużo. Maks 3-5 obszarów.

---

## Framework 4: Adopting Agile (Scrum Repair Guide, Cohn)

### 5 błędów w agile adoption (Cohn)

1. **"Doing Scrum" zamiast "being agile"** — adoptujesz ceremonie bez zmiany myślenia. Output: process theatre.
2. **Nie usuwanie przeszkód** — Scrum Master robi notatki, ale nic nie zmienia w organizacji. Zespół traci wiarę.
3. **PO bez empowerment** — Product Owner nie ma władzy decyzyjnej, tylko "kolekcjonuje wymagania". Sprint planning = prośba o pozwolenie.
4. **Zbyt wiele zmian naraz** — adoptujesz Scrum + Kanban + XP + DevOps + OKR w jednym kwartale. Ludzie nie nadążają.
5. **Brak management buy-in** — team adopts agile, ale manager mierzy ich starymi metrykami. Sprzeczność.

### Adoption Roadmap (Kotter steps condensed)

```
Quarter 1: Steps 1-2 (urgency + coalition)
  - Znajdź 1 sponsora na executive level
  - Pokaż dlaczego current state nie działa (data, nie opinie)
  - Zbuduj małą koalicję (2-3 osoby)

Quarter 2: Steps 3-4 (vision + communication)
  - Sformułuj wizję "dlaczego agile" w 1 zdaniu
  - Powtarzaj ją na każdym spotkaniu, w każdym emailu
  - Zacznij od 1 pilotażowego zespołu (nie całej firmy)

Quarter 3: Steps 5-6 (remove obstacles + quick wins)
  - Pokaż, że pilot ma wyniki (np. velocity +30%, defects -40%)
  - Rozszerz na 2-3 zespoły
  - Address management concerns (to nie rewolucja, ewolucja)

Quarter 4: Steps 7-8 (sustain + institutionalize)
  - Nowe metryki dla managerów
  - Celebration wins
  - Agile nie jest już "projekt", jest "jak pracujemy"
```

**Anty-wzorzec:** "Big Bang adoption" — od jutra cała firma pracuje agile. Zawsze kończy się powrotem do starego po 3 miesiącach.

---

## Anti-patterns

| Anti-pattern | Dlaczego zły | Fix |
|---|---|---|
| Brak pilności | Ludzie nie mają powodu do zmiany. "Fajnie, ale po co?" | Step 1 Kotter. Konkretne dane, nie opinie. |
| Skakanie do rozwiązania | "Musimy wprowadzić Scrum!" bez wizji | Cofnij się. Dlaczego Scrum? Co ma zmienić? |
| Komunikacja jednorazowa | Town hall raz, potem cisza | Powtarzaj wizję minimum 5x różnymi kanałami w 1 miesiącu. |
| Brak quick wins | "Zmiana potrwa 2 lata" — nikt nie wytrzyma | Co tydzień 1 mała, widoczna wygrana. |
| Victory declared too early | "Mamy OKR-y, jesteśmy agile" — a tak naprawdę nie | Kotter krok 8: dopiero gdy nowy sposób pracy jest "default", nie "projekt". |
| ORID: przeskakiwanie poziomów | Od razu do "co robimy?" | Facylitator pilnuje: O → R → I → D. Zero skrótów. |
| Information radiator nieaktualizowany | Martwa tablica. Ludzie przestają patrzeć. | Update ritual: daily / weekly. Owner per radiator. |
| Tablica z 20 metrykami | Nikt nie wie, na co patrzeć | Maks 3-5 kluczowych obszarów. |
| Adoption bez sponsorów na górze | Team adoptuje, manager sabotuje | Bez executive buy-in: nie startuj. Znajdź sponsora najpierw. |

---

## Integration z innymi skilleami

| Skill | Jak współpracuje |
|---|---|
| `team-healer/SKILL.md` | Change zaczyna się od trust. Jeśli zespół nie ufa, żaden framework nie pomoże. Heal first, change second. |
| `metrics-strategist/SKILL.md` | "Czy nasza metryka się poprawiła?" = miernik sukcesu zmiany. OKR-y anchor change. |
| `sprint-planning/SKILL.md` | Nowy process = nowe sprint planning. Wdróż zmiany w sprincie pilotażowym. |
| `retrospective/SKILL.md` | Co 2-4 sprinty: "Czy nasza adoptcja agile postępuje? Gdzie jesteśmy w 8 krokach Kottera?" |

---

## When this skill is NOT enough

- **Restrukturyzacja firmy, zwolnienia, M&A** → nie framework, a doradztwo strategiczne + prawnik
- **Coaching życiowy / kariera** → `agent-mindful-coach` lub kariera coach
- **Konflikt wartości / religia / polityka** → inne ramy
- **Szkolenia z agile / certyfikacje Scrum Master** → ten skill daje fundament, nie certyfikat

---

## Framework Credits

Ten skill korzysta z frameworków i koncepcji opisanych w
[ATTRIBUTION.md](../../ATTRIBUTION.md):

- **Leading Change (Kotter, 1996)** — 8-step change model, urgency, coalition, vision
- **ORID (Institute of Cultural Affairs, 1980s)** — Objective / Reflective / Interpretive / Decisional conversation structure
- **Lean Software Development (Poppendieck, 2003)** — Information Radiator concept
- **Agile Retrospectives (Derby & Larsen)** — facilitation techniques referenced in ORID
- **Mountain Goat Software — Scrum Repair Guide (Cohn)** — Module 6: Adoption, common adoption mistakes (public course reference)
- **Switch: How to Change Things When Change Is Hard (Heath & Heath, 2010)** — rider / elephant / path metaphor (użyteczny framework dla change narrative — wbudowany)
