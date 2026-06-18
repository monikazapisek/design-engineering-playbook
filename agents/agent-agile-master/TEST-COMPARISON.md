# Test Porównawczy: agent-agile-master vs Generic Claude

> Model: claude-sonnet-4-6 (oba warianty)
> Data: 2026-06-18
> Metodologia: ten sam prompt, ten sam model — bez agenta vs z załadowanym AGENT.md + PERSONA.md + odpowiedni SKILL.md

---

## Scenariusz 1 — Ritual Routing

**Prompt:** "Nie wiem co teraz zrobić. Skończyłem jakieś zadania, mam backlog, ale nie wiem czy zaczynać nowy sprint czy coś innego."

---

### Wariant A: Generic Claude (bez agenta)

> "To zależy od kilku czynników. Możesz rozważyć:
>
> - **Jeśli backlog jest uporządkowany** — zacznij sprint planning
> - **Jeśli backlog jest chaotyczny** — zrób najpierw backlog refinement
> - **Jeśli nie wiesz co jest priorytetem** — może warto zrobić sesję priorytetyzacji
>
> Ogólnie w Scrumie typowy rytm to: sprint → retrospektywa → planning → nowy sprint.
> Co jest teraz Twoim głównym celem?"

**Ocena:** Pyta z powrotem, nie diagnozuje. Daje opcje bez decyzji. Nie zna pojęcia "ritual" ani "ceremony". Brak timeboxu, brak outputu, brak sekwencji.

---

### Wariant B: agent-agile-master

> **Diagnoza:**
> Sygnał: "nie wiem co teraz" → uruchamiam Ritual Router.
>
> 3 pytania diagnostyczne:
> 1. Czy kończysz sprint czy jesteś w trakcie? → Kończysz → wskazuje na Retrospektywę
> 2. Czy backlog jest uporządkowany? → Nie wiem → Backlog Refinement przed planningiem
> 3. Czy jest coś konkretnego do oszacowania? → Nie → nie Estimation Session
>
> **Verdict:** Kolejność: Retrospektywa (20 min) → Backlog Refinement (20 min) → Sprint Planning (30 min)
>
> Zaczynamy od Retro? Mam gotowy 5-stage format dla solo, 20 minut.

**Ocena:** Diagnozuje zamiast pytać. Daje sekwencję z timeboxami. Decyduje, nie przerzuca decyzji na użytkownika.

---

## Scenariusz 2 — Sprint Planning

**Prompt:** "Zaczynam nowy sprint. Mam backlog 12 tasków, nie wiem które wybrać."

---

### Wariant A: Generic Claude (bez agenta)

> "Przy wyborze tasków do sprintu warto kierować się kilkoma kryteriami:
>
> 1. **Priorytet biznesowy** — co jest najważniejsze dla projektu?
> 2. **Zależności** — czy któryś task odblokuje inne?
> 3. **Rozmiar** — ile możesz realnie zrobić w sprincie?
> 4. **Ryzyko** — co jest najbardziej niepewne?
>
> Spróbuj wybrać 3-5 tasków, które razem tworzą spójny cel. Czy możesz mi powiedzieć więcej o tych taskach?"

**Ocena:** Sensowna lista kryteriów, ale bez struktury procesu. Nie pyta o sprint goal. Nie ma koncepcji timeboxu planowania. Prosi o więcej danych zamiast prowadzić przez krok po kroku.

---

### Wariant B: agent-agile-master

> **Ritual: Sprint Planning**
> **Time estimate:** 35 min
>
> **Step 1 — Sprint Goal (5 min)**
> Zanim wybierzemy taski, jedno pytanie: co sprawi, że ten sprint będzie sukcesem? Jedna rzecz.
> Format: "W tym sprincie [konkretny wynik] żeby [powód]."
>
> **Step 2 — Selekcja (10 min)**
> Z 12 tasków wybieramy przez 3 filtry:
> - Bezpośrednio realizuje sprint goal? → Must have
> - Odblokuje przyszłą pracę? → Nice to have
> - "Fajnie byłoby"? → Parking lot
>
> Dla solo: max 3-5 tasków. Mniej = więcej.
>
> **Step 3 — Estimation (10 min)**
> Brak historii velocity? Używamy t-shirt sizing: XS/S/M/L.
> Zasada: jeśli task = L lub XL → podziel zanim zaczniesz.
>
> **Step 4 — Commit (5 min)**
> Zapisujemy: Sprint Goal + lista tasków + DoD.
>
> Powiedz mi jedno zdanie o celu projektu — dobiorę selekcję do kontekstu.

**Ocena:** Prowadzi przez proces krok po kroku. Sprint Goal jako punkt wyjścia, nie opcja. Decyzja o max taskach jest twarda (3-5), nie "zależy". Timebox na każdy krok.

---

## Scenariusz 3 — Estimation

**Prompt:** "Mam 5 user stories, nie wiem ile zajmą. Jak je oszacować?"

---

### Wariant A: Generic Claude (bez agenta)

> "Istnieje kilka metod estymacji:
>
> - **Story Points** — relative sizing za pomocą Fibonacci (1,2,3,5,8,13)
> - **T-shirt sizing** — XS/S/M/L/XL, szybka wstępna estymacja
> - **Planning Poker** — dla zespołów, każdy głosuje niezależnie
> - **Godziny** — prostsze, ale mniej dokładne w Agile
>
> Dla solo practitionera polecam story points lub t-shirt sizing. Zacznij od storyi którą najlepiej znasz jako punkt odniesienia (np. 3 punkty) i porównuj resztę do niej."

**Ocena:** Dobra lista metod. Ale: nie diagnozuje czy użytkownik ma historię velocity czy nie. Nie prowadzi przez sesję estymacji. Nie ma outputu (tabeli). Brak zasady "kiedy podzielić story".

---

### Wariant B: agent-agile-master

> **Ritual: Estimation Session**
> **Time estimate:** 20 min
>
> Pierwsze pytanie: masz już poprzednie sprinty z historią punktów? (tak/nie)
>
> **→ Brak historii (nowy projekt):** używamy reference-based estimation:
>
> 1. Wybierz jedną story którą rozumiesz najlepiej → to jest "3 punkty"
> 2. Porównaj każdą pozostałą do tej referencji:
>    - Podobny wysiłek? → 3
>    - Połowa? → 1-2
>    - Dwa razy więcej? → 5-8
>    - Znacznie więcej? → 13 → **podziel tę story przed estymacją**
>
> | Story | Punkty | Uwagi |
> |---|---|---|
> | [story 1] | | |
> | [story 2] | | |
> | ... | | |
>
> Zasada: jeśli story = 13+ → to nie jest jedna story. Podziel i wróćmy.
>
> Powiedz mi te 5 stories jednym zdaniem każda — przejdziemy przez nie razem.

**Ocena:** Diagnozuje kontekst (historia vs brak) przed doborem techniki. Daje gotową tabelę jako output. Zasada podziału story jest twarda, nie "można rozważyć". Kończy zaproszeniem do działania.

---

## Scenariusz 4 — Retrospektywa

**Prompt:** "Właśnie skończyłem sprint. Nie wiem co poszło dobrze a co źle. Chcę zrobić retro ale nie wiem od czego zacząć."

---

### Wariant A: Generic Claude (bez agenta)

> "Retrospektywa to świetny sposób na refleksję po sprincie! Oto kilka kroków:
>
> 1. **Co poszło dobrze?** — zacznij od pozytywów
> 2. **Co poszło źle?** — bądź szczery z sobą
> 3. **Co możesz poprawić?** — stwórz konkretny plan
>
> Możesz użyć formatu Start/Stop/Continue albo 4L (Liked, Learned, Lacked, Longed For).
> Staraj się być konstruktywny i skup się na procesie, nie na sobie. Powodzenia!"

**Ocena:** Ogólne. Brak timeboxu. Brak technik z instrukcją. Brak output formatu. "Powodzenia!" zamiast prowadzenia przez sesję.

---

### Wariant B: agent-agile-master

> **Ritual: Retrospective**
> **Time estimate:** 25 min
> **Format:** Sprint Movie + 4 Ls (general-purpose, dobry na start)
>
> **Stage 1 — Set the Stage (3 min)**
> Gdyby ten sprint był filmem, jaki miałby tytuł? Napisz 1-3 tytuły. Dlaczego?
>
> **Stage 2 — Gather Data (7 min)**
> Tabela 4 Ls:
>
> | | Twoje odpowiedzi |
> |---|---|
> | **Loved** — co było energetyzujące? | |
> | **Liked** — co poszło dobrze? | |
> | **Lacked** — czego brakowało? | |
> | **Longed For** — czego chcesz więcej? | |
>
> 2-3 obserwacje na kategorię. Nie więcej.
>
> **Stage 3 — Insights (7 min)**
> Wybierz 1-2 obserwacje z poprzedniego etapu. Dla każdej: 5 Whys.
>
> **Stage 4 — Action Items (7 min)**
> Max 3 — format SMART:
> ```
> Action: [co konkretnie]
> When: [kiedy]
> Success: [jak poznasz że zadziałało]
> ```
>
> **Stage 5 — Close (1 min)**
> "Następny sprint [zrobię X] ponieważ [wniosek]."
>
> Anti-pattern dziś: nie więcej niż 3 action items. 2 konkretne > 5 rozmytych.
>
> Zaczynamy od Stage 1 — jaki tytuł miałby ten sprint?

**Ocena:** 5-stage Derby & Larsen z timeboxami. Każdy stage = konkretna technika z instrukcją. Output format gotowy. Kończy pytaniem które startuje sesję, nie "powodzeniem".

---

## Zbiorcze porównanie

| Kryterium | Generic Claude | agent-agile-master |
|---|---|---|
| **Diagnoza sytuacji** | Pyta lub pomija | Ritual Router — diagnozuje i decyduje |
| **Struktura procesu** | Ogólne kroki | Named stages z timeboxami |
| **Konkretna technika** | Wymienia opcje | Wybiera jedną, daje instrukcję |
| **Output format** | Brak | Gotowy template/tabela |
| **Anti-patterns** | Brak | Lista + wybór na dziś |
| **Solo adaptation** | Domyślnie team | Zaprojektowany dla 1 osoby |
| **Timebox** | Brak | Każdy stage/krok ma limit |
| **Zakończenie** | "Powodzenia!" / pytanie | Pytanie które startuje sesję |
| **Powtarzalność** | Zależy od prompta | Każda sesja = ta sama jakość |
| **Głos** | Doradczy, opcje | Facilitatorski, decyduje i prowadzi |

## Wnioski

Agent wygrywa nie jakością wiedzy — ta jest podobna. Wygrywa **strukturą, powtarzalnością i głosem**.

Generic Claude wie co to 5 Whys. Ale nie wyjdzie z inicjatywą żeby go użyć, nie utrzyma timeboxu i nie wyprodukuje gotowego output formatu. Agent-agile-master tak — za każdym razem, bez względu na to jak sformułujesz prompt.

Dla solo practitionera to różnica między "dostaję poradę" a "ktoś mnie prowadzi przez sesję".
