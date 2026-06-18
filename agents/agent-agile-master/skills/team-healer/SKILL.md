---
created: 2026-06-18
updated: 2026-06-18
version: 1.1
description: Diagnose and heal team dysfunction — Lencioni 5 dysfunctions, agile hoarders, psychological safety, sheepdog protection, Working Genius talent alignment, toxic behavior playbook (Monopolizer/Ghost/Critic), Personal User Manuals. Dual mode: solo self-coaching and team facilitation.
agent: agent-agile-master
attribution: ATTRIBUTION.md
extends: ../../AGENT.md
---

# Team Healer

Diagnozuj i uzdrawiaj dynamikę zespołu. Skille oparte na modelu Patricka Lencioni (5 dysfunkcji pracy zespołowej), pracach Amy Edmondson (psychological safety) i roli "owczarka" (sheepdog) — ochrony zespołu przed zakłóceniami.

> **Tryb pracy:** ten skill działa w dwóch wariantach:
> - **Solo mode** — sam jesteś zespołem. Diagnozujesz siebie, swoje nawyki, swoje blokery.
> - **Team mode** — moderujesz sesję dla 2-5 osób. Facylitacja aktywna, techniki grupowe.
>
> Każda technika poniżej ma obie wersje. Wybór trybu deklarujesz na początku sesji.

---

## Purpose

Kiedy zespół (albo ty sam) ma problemy z:
- zaufaniem między członkami
- konfliktem, który nikt nie chce zaadresować
- brakiem zaangażowania w decyzje
- unikaniem odpowiedzialności za wynik
- brakiem dbałości o rezultaty (focus na busy-work zamiast outcome)

...wtedy uruchamiasz ten skill. Output: konkretne action items na następny sprint (max 3, zgodnie z hard rule retro).

---

## When to run

| Trigger | Tryb |
|---|---|
| "zespół nie działa", "brak zaufania", "ludzie milczą" | Team mode |
| "konflikt w teamie", "ktoś blokuje", "hoarder" | Team mode |
| "sam nie wierzę w swój plan", "prokrastynuję", "unikam trudnych decyzji" | Solo mode |
| "czuję że tonę w pracy", "nie mam energii", "burnout" | Solo mode |
| Retro ujawnia problem systemowy (nie konkretny bug) | Either |
| Co 4-6 sprintów — health check prewencyjny | Either |

**NIE uruchamiaj** dla terapii osobistej, kryzysu emocjonalnego, problemów poza pracą → `agent-mindful-coach`.

---

## Duration

- **Solo health check:** 20-30 min
- **Team session (2-5 osób):** 60-90 min
- **Deep intervention (chronic dysfunction):** 2-3 spotkania po 60 min

---

## Knowledge to load (on demand)

| Situation | Reference |
|---|---|
| Pełne tło Lencioni (team dysfunctions) | Lencioni, *The Five Dysfunctions of a Team* (2002) — Chapters 1-2 |
| Psychological safety dla zespołu technicznego | Edmondson, *Fearless Organization* (2018) — 4 stages (Inclusion, Learner, Contributor, Challenger safety) |
| Trudna rozmowa 1:1 | Cohn, *Scrum Repair Guide* (Mountain Goat Software) — Module 5: Dysfunctional teams |
| Solo reflection frameworks | Wbudowane (nie wymaga dodatkowego ładowania) |

**Reguła:** w tym skillu ładuj wiedzę oszczędnie. Większość technik jest wbudowana. Dodatkowe źródła konsultuj tylko gdy user pyta o głębokie tło.

---

## Framework 1: Lencioni 5 Dysfunctions — Diagnostic

### The pyramid (bottom-up)

```
        5. Inattention to Results
       /
     4. Avoidance of Accountability
    /
  3. Lack of Commitment
 /
2. Fear of Conflict
/
1. Absence of Trust
```

Każdy poziom zależy od poprzedniego. Nie da się naprawić #5 bez #1.

### Solo diagnostic (15 min)

Przeczytaj każde stwierdzenie i oceń 1-5 (1=nieprawda, 5=zdecydowanie tak):

| # | Pytanie | Score |
|---|---|---|
| 1 | Czy potrafię przyznać się do błędu w notesie/retro bez dramatyzowania? | /5 |
| 2 | Czy pytam o pomoc, gdy czegoś nie wiem, czy raczej improwizuję sam? | /5 |
| 3 | Czy mówię wprost, gdy nie zgadzam się z kierunkiem projektu? | /5 |
| 4 | Czy dotrzymuję własnych zobowiązań sprintowych? | /5 |
| 5 | Czy mierzę swój sukces wartością biznesową, czy liczbą odhaczonych tasków? | /5 |

**Interpretacja:**
- Score 1-2: fundament kruchy. Zanim zrobisz cokolwiek innego, pracuj nad #1 (trust).
- Score 3: gdzieś jest wyciek. Znajdź najniższy score i address tylko ten.
- Score 4-5: zdrowy self-leadership. Przejdź do Framework 3 (psych safety) dla prewencji.

### Team diagnostic (30 min)

**Technika "5 Dysfunctions Mapping":**

1. **Rozdaj karteczki** (albo otwórz wspólny doc) — każdy dostaje 5 kolorów, każdy kolor = jeden poziom.
2. **Cicho (5 min)** — każdy pisze 1 konkretny przykład z ostatniego sprintu dla każdego poziomu, gdzie widział dysfunkcję. Bez nazwisk.
3. **Round-robin (15 min)** — każdy czyta swoje notatki. Facylitator grupuje podobne.
4. **Vote (5 min)** — każdy głosuje na najważniejszy dysfunction do address w tym sprincie. Max 3 głosy na osobę.
5. **Output:** jeden dysfunction wybrany, jeden action item na sprint.

**Zasada facylitacji:** jeśli zespół wskaże "Lack of Trust" jako #1 problem — to dobry znak (są samoświadomi). Jeśli wskażą tylko #3-5, prawdopodobnie #1-2 są niebezpiecznie niezauważone. Facylitator: "Zauważam, że nikt nie napisał o zaufaniu. Czy to znaczy, że jest dobrze, czy że nikt nie chce o tym mówić?"

---

## Framework 2: Confronting Agile Hoarders

### Co to jest "agile hoarder"?

Osoba (lub ty sam), która:
- blokuje wiedzę ("nie mam czasu ci tego wytłumaczyć, sam zrobię")
- tworzy pojedyncze punkty awarii (single point of failure)
- unika parowania / code review / wspólnej pracy
- używa wiedzy jako waluty politycznej ("ty nie rozumiesz, ja się na tym znam")

### Solo: Self-diagnostic (10 min)

Odpowiedz szczerze:

1. Czy w ostatnim sprincie ktoś inny mógłby wykonać którąś z moich prac, gdybym mu pokazał jak? Jeśli nie — gdzie są moje "hoarding hotspots"?
2. Czy mam dokumentację / decision log, czy trzymam kontekst w głowie?
3. Czy proszę o code review / feedback, czy raczej pushuję "done" bez weryfikacji?

**Jeśli 2+ odpowiedzi "nie" / "raczej nie"** — masz hoarding pattern. Action: w następnym sprincie wybierz 1 aktywność, którą zrobisz w parze lub z dokumentacją.

### Team: Confrontation script (15-20 min per osoba)

**Kiedy użyć:** kiedy masz konkretnego hoardera w zespole. NIE rób tego ad-hoc. Umów się na 1:1.

**Struktura rozmowy (NVC — Nonviolent Communication, Rosenberg):**

```
1. OBSERVATION:  "W ostatnim sprincie zauważyłem, że [konkretny fakt]."
                  (Np. "Moduł X był tylko twój, 3 sprinty z rzędu.")

2. FEELING:      "Czuję [emocja] w związku z tym."
                  (Np. "Czuję niepokój, bo jeśli będziesz chory/na urlopie,
                   projekt stanie.")

3. NEED:         "Potrzebuję [uniwersalna potrzeba]."
                  (Np. "Potrzebuję redundancy wiedzy, żeby zespół
                   był odporny.")

4. REQUEST:      "Czy mógłbyś [konkretna, wykonalna prośba]?"
                  (Np. "Czy mógłbyś w przyszłym sprincie zrobić 1
                   sesję pair-working z Kim nad modułem X?")
```

**Hard rules:**
- NIE diagnozuj ("jesteś kontrolującym typem"). Mów o zachowaniu i skutku.
- NIE generalizuj ("zawsze tak robisz"). Jeden konkretny przykład.
- NIE atakuj w grupie. Zawsze 1:1, w bezpiecznej przestrzeni.
- Jeśli reakcja to defensywność → "Widzę, że to trudne. Możemy wrócić do tego jutro?"

**Solo adaptation:** zamień "kolegę" na "siebie sprzed 3 miesięcy". Napisz do siebie email / notatkę z tą strukturą. Niesamowicie skuteczne dla self-hoarding.

---

## Framework 3: Psychological Safety (Edmondson)

### 4 Stages of Psychological Safety (in order)

```
1. Inclusion safety      → "Mogę być sobą w tej grupie"
2. Learner safety        → "Mogę pytać i nie wiedzieć"
3. Contributor safety    → "Mogę dodać wartość bez obawy"
4. Challenger safety     → "Mogę zakwestionować status quo"
```

Bez #1 nie da się zbudować #4. Skoki w tej hierarchii powodują opór.

### Solo: Self-assessment (10 min)

Dla każdego stage'u oceń: "Czy w moim obecnym środowisku pracy (nawet solo) czuję ten poziom bezpieczeństwa?"

| Stage | Pytanie | Score 1-5 |
|---|---|---|
| 1 | Czy mam przestrzeń, gdzie mogę eksperymentować bez konsekwencji? | /5 |
| 2 | Czy mogę przyznać "nie wiem" bez utraty wiarygodności? | /5 |
| 3 | Czy mam sposób na regularne dowozienie wartości? | /5 |
| 4 | Czy potrafię zakwestionować własne wcześniejsze decyzje? | /5 |

**Niski score na 1-2:** wprowadź rytuał, w którym regularnie dajesz sobie pozwolenie na eksperyment. Np. "Piątkowe 30 min na brzydkie prototypy, bez commit".

**Niski score na 3-4:** problem z feedback loop. Zacznij od małych, dostarczalnych commitów i review własnej pracy co tydzień.

### Team: Building safety (60-90 min workshop)

**Ćwiczenie "Personal Histories" (Edmondson):**

Każdy członek zespołu opowiada 5-10 min o sobie — nie o pracy, tylko o życiu. Może być:
- Skąd jestem
- Najciekawsza rzecz, którą robiłem/am poza pracą
- Coś, czego nikt tu o mnie nie wie
- Moja największa porażka i czego mnie nauczyła

**Zasady:**
- 1 osoba mówi, reszta słucha BEZ przerywania i komentowania
- Facylitator pilnuje czasu
- Po każdej historii — 1 min ciszy, potem pytania (ale NIE komentarze typu "o, super")

**Dlaczego to działa:** vulnerability lidera sygnalizuje, że vulnerability jest OK. Po 1-2 historiach reszta zespołu zaczyna się otwierać.

**Wariant solo:** napisz 4-5 własnych "personal histories" w notatniku. Nie musisz ich nikomu opowiadać. Chodzi o to, żebyś sam/sama poznał/a kontekst swoich decyzji.

### Team: Personal User Manuals (wariant dla mniejszych zespołów 2-5 osób)

**Kiedy użyć:** gdy zespół jest mały i każdy ma indywidualny styl pracy, który nawzajem się irytuje. Lżejsza wersja niż Personal Histories — bardziej operacyjna.

**Format:** każdy pisze 1-stronicowy dokument pt. "Jak pracować ze mną / czego potrzebuję", zawierający:

```
# Personal User Manual — [imię]

## Moje mocne strony
- [2-3 rzeczy, w których jestem dobry]

## Jak komunikować się ze mną
- Preferowany kanał: [Slack / twarzą w twarz / email / async doc]
- Tempo odpowiedzi: [szybko / w ciągu dnia / mogę potrzebować 24h]
- Styl: [bezpośredni / delikatny / szczegółowy / big-picture]

## Co mnie blokuje / frustruje
- [1-2 konkretne zachowania, np. "niespodziewane zmiany scope", "spotkania bez agendy"]

## Jak mogę pomóc
- [Co przychodzi mi łatwo, czego mogę nauczyć innych]

## Czego potrzebuję od zespołu
- [Czego NIE potrzebuję też — np. "nie potrzebuję stand-up, wolę status w piątek"]
```

**Wymiana:** dokumenty krążą w zespole. Każdy czyta wszystkie (15 min). Potem 30 min rozmowy: co Cię zaskoczyło? co już wiesz o sobie, ale warto powiedzieć wprost?

**Solo:** napisz swój własny PUM. Przeczytaj za miesiąc — czy nadal pasuje? Jeśli zmieniłeś/aś sposób pracy, zaktualizuj.

**Anty-wzorzec:** PUM jako jednorazowy exercise, po którym nikt go nie czyta. Bez użycia = zmarnowany dokument.

---

## Framework 4: Sheepdog — Protecting the Team

### Co to jest rola sheepdoga?

Metafora odpowiedzialności Scrum Mastera (inspirowana "Sheepdog" metaphor w leadership literature):
- **Owce** = zespół, deliverujący wartość
- **Wilki** = zakłócenia, presja, scope creep, niejasne priorytety
- **Owczarek** = Scrum Master / Agile Coach, który stoi między nimi

### Kiedy sheepdog interweniuje

| Sygnał | Interwencja |
|---|---|
| Product Owner zmienia priorytety 3x w sprincie | "Zauważam, że scope się zmienił 3 razy. Czy możemy zamrozić priorytety do następnego review?" |
| Manager pyta o status codziennie | "Daily standup raportuję w Decks/Docs. Cotygodniowy status jest w piątek. Czy to wystarczy?" |
| Zespół pracuje po godzinach regularnie | Sprawdź cause: za dużo scope? za mało ludzi? brak automatyzacji? |
| Scope creep w trakcie sprintu | "To jest nowa praca. Dodajmy do następnego sprintu albo zamieńmy z czymś. Co wyrzucamy?" |
| Ktoś jest chory / na urlopie | "Redystrybuujemy zadania. Kto może przejąć X?" |

### Solo: Self-protection rituals

Ty jesteś jednocześnie wilkiem, owcą i owczarkiem. Wprowadź rytuały ochronne:

1. **Friday Review (15 min):** "Co mnie w tym tygodniu rozproszyło? Które zakłócenia były prawdziwymi priorytetami, a które noise?"
2. **Sprint Commitment Lock:** w trakcie sprintu NIE zmieniam scope. Nowe idee → backlog na następny sprint.
3. **Saying No Script:** "Nie, nie w tym sprincie. Mogę to zrobić [alternatywny termin]." Nie tłumacz się z bycia zajętym.
4. **Time Blocking:** kalendarz blokuje "focus time" — nie meetings. Traktuj to jak spotkanie z najważniejszym stakeholderem (sobą).

### Team: "Sheepdog Rounds" (5 min, codziennie lub co 2-3 dni)

Facylitator pyta:
1. "Czy ktoś ma zakłócenie, które blokuje mu robotę?"
2. "Czy coś z zewnętrznego (PO, manager, klient) próbuje wedrzeć się do sprintu?"
3. "Kto potrzebuje ochrony przed czymś?"

Output: lista 1-3 rzeczy, które sheepdog (SM/PO) zaadresuje w ciągu 24h.

---

## Framework 5: Toxic Behavior Playbook (3 klasy archetypów)

### Po co ten framework?

Nie każdy problem zespołowy to dysfunkcja Lencioniego. Czasem konkretna osoba ma nawyk, który regularnie blokuje pracę. Trzy najczęstsze archetypy:

### A) Monopolizator (The Monopolizer)

**Profil:** mówi 70% czasu na spotkaniach, przerywa, zawsze ma odpowiedź na każdy temat. Często myśli, że pomaga (mówi dużo = daje dużo).

**Diagnostyka (zespół, 5 min):** Policz czas mówienia per osoba na 2-3 spotkaniach. Jeśli ktoś ma >40% czasu i reszta milczy — masz monopolizatora.

**Solo diagnostyka:** Nagraj się na stand-upie lub rozmowie. Odsłuchaj. Jeśli mówisz >50% czasu i zadajesz pytania retoryczne zamiast czekać — to dotyczy też Ciebie.

**Interwencja (1:1 NVC script):**

```
1. OBSERVATION: "Na ostatnich 3 spotkaniach zauważyłem, że mówiłeś/aś
                  ok. 60% czasu. Reszta zespołu milczała."
2. FEELING:    "Czuję niepokój, bo wiem, że mamy mądrych ludzi w zespole,
                a ich głos się nie pojawia."
3. NEED:       "Potrzebuję, żeby każdy członek zespołu miał równe szanse
                na wniesienie perspektywy."
4. REQUEST:    "Czy mógłbyś w następnym sprincie celowo ograniczyć się
                do [X]% czasu mówienia i zostawić 2-3 min ciszy po każdym
                pytaniu?"
```

**Środowiskowy fix (dla całego zespołu):**
- **Round-robin** — każdy mówi po kolei, monopolizator nie może mówić drugi raz, dopóki wszyscy się nie wypowiedzą
- **Time-box per wypowiedź** — fizyczny timer (np. 2 min), kto przekroczy — oddaje głos
- **Silent brainstorm** — 5 min pisemnie przed dyskusją. Eliminuje dominację głosu.

### B) Duch (The Ghost)

**Profil:** obecny na spotkaniach, ale nie daje konkretnych informacji. "OK, robię to" / "Myślę nad tym" / "Zobaczymy". Po 2 tygodniach nic się nie zmienia. Nie złośliwie — po prostu unika konfrontacji z konkretem.

**Diagnostyka (zespół):** W retrospektywach pytaj: "Które zobowiązania z ostatniego sprintu wziął Duch? Ile z nich zostało zrealizowane?" Jeśli <50% — masz problem.

**Solo diagnostyka:** Przejrzyj swoje notesy z ostatnich 4 tygodni. Ile razy napisałeś/aś "TODO", "sprawdzić", "przygotować" — bez konkretnej daty i definicji done? Jeśli >5 — masz ghost pattern.

**Interwencja (1:1 NVC script):**

```
1. OBSERVATION: "W ostatnich 3 sprintach zobowiązałeś/aś się do X, Y, Z.
                  Żadne z nich nie zostało dowiezione w terminie."
2. FEELING:    "Czuję frustrację, bo nie mogę planować sprintu bez
                pewności, że stories będą gotowe."
3. NEED:       "Potrzebuję pewności. Jeśli zobowiązujesz się do czegoś,
                chcę móc na tym polegać."
4. REQUEST:    "Dwie opcje: albo (a) mówisz mi realnie, ile czasu potrzebujesz,
                albo (b) dzielisz zobowiązanie na mniejsze, do zrobienia w 1-2 dni.
                Co wolisz?"
```

**Środowiskowy fix:**
- **Definition of Done obowiązkowe** — każdy commitment ma konkretne kryterium "kiedy to uznam za gotowe"
- **Daily check-in** (niekoniecznie stand-up) — 5 min "co zrobiłeś wczoraj, co dziś" z konkretnym outputem
- **Pair / mob programming** — Duch nie może być duchem, jeśli jest w parze. Wymusza widoczność.

### C) Krytyk (The Critic)

**Profil:** regularnie podważa wybory innych — nie konstruktywnie, ale żeby pokazać, że on/ona widzi problem. Często zaczyna od "ale", "nie zgadzam się", "to nie zadziała". Każda decyzja jest challenge'owana. Efekt: zespół przestaje proponować.

**Diagnostyka:** Policz na spotkaniach: ile razy Krytyk zaczyna wypowiedź od słowa "ale" vs "i"? Jeśli >3x na spotkanie — masz Krytyka. Drugi sygnał: po spotkaniu ludzie mówią "nie warto było proponować".

**Solo diagnostyka:** Sprawdź swój ostatni tydzień feedbacku. Ile Twoich uwag zaczynało się od "ale" / "nie zgadzam się" / "to nie zadziała"? Ile od "doceniam X, ale..." (z konkretnym uzupełnieniem)? Jeśli dominuje pierwsza kategoria — Ty jesteś Krytykiem.

**Interwencja (1:1 NVC script):**

```
1. OBSERVATION: "W ostatnim sprincie zauważyłem, że 4 z 5 moich propozycji
                  spotkały się z Twoją krytyką na spotkaniu."
2. FEELING:    "Czuję zniechęcenie, bo zaczynam unikać proponowania pomysłów."
3. NEED:       "Potrzebuję krytyki, która POMAGA, a nie blokuje. Chcę
                czuć, że moje pomysły są bezpieczne do wygłoszenia."
4. REQUEST:    "Czy mógłbyś w następnym sprincie, zanim skrytykujesz pomysł,
                powiedzieć najpierw co w nim działa? Potem dopiero krytyka."
```

**Środowiskowy fix:**
- **Yes-And rule** — każda krytyka musi być poprzedzona "doceniam X, a proponuję Y" (improwizacja jazzowa)
- **Criticism budget** — max 1 krytyka per osoba per spotkanie. Powyżej — publiczna informacja zwrotna.
- **Separate ideation from critique** — najpierw 10 min generowanie pomysłów (bez oceny), potem 10 min krytyka. Oddzielnie.

### Diagnostyka na poziomie zespołu (30 min)

**Ćwiczenie "Behavior Audit":**

1. Każdy członek zespołu (anonimowo) wymienia 1 zachowanie, które go blokuje w pracy zespołowej (nie osobę — zachowanie).
2. Facylitator grupuje podobne zachowania w 3-5 kategorii.
3. Głosujemy na TOP 1 zachowanie do address w tym sprincie.
4. Przypisujemy 1 konkretny fix (środowiskowy lub 1:1).

**Output:** 1 zachowanie + 1 fix + 1 owner + 1 deadline. Mniej = więcej.

---

## Framework 6: Working Genius — talent-based team design (Lencioni 2022)

### Co to jest?

Patrick Lencioni (autor 5 Dysfunctions) wrócił w 2022 z modelem dopasowania **zadań do naturalnych talentów**. Idea: frustracja i wypalenie zwykle nie wynikają z "trudnej pracy", ale z pracy, do której nie mamy talentu.

### 6 rodzajów "Working Genius"

| Typ | Co kocha | Co kochają robić | Czego NIE lubi |
|---|---|---|---|
| **Wonder** (Zdumienie) | Zadawanie pytań "dlaczego?" | Kwestionować status quo, szukać nowych możliwości | Egzekucji, szczegółów, "zamykania" |
| **Invention** (Wynalazek) | Tworzenie nowych rozwiązań | Brainstorming, prototypowanie, "a co jeśli..." | Powtarzalności, utrzymywania |
| **Discernment** (Osąd) | Ocena i instynkt | Patrzeć na coś i wiedzieć "to zadziała / nie zadziała" | Syntezy wielu pomysłów, tworzenia |
| **Galvanizing** (Galwanizacja) | Poruszanie ludzi | Inspirować, motywować, tworzyć energię do działania | Detalami, follow-throughem |
| **Enablement** (Umożliwienie) | Pomaganie innym | Wspierać, odpowiadać na prośby, usuwać blokery | Samodzielnym "gwiazdorstwu" |
| **Tenacity** (Wytrwałość) | Dokończenie do końca | Finalizacja, follow-through, finishowanie | Nowości, zmian, "eksploracji" |

### Kiedy użyć tego frameworku

- **Burnout, frustracja, "nie lubię tej pracy"** — możliwe, że robisz zadania spoza swoich genius loci
- **Konflikt w zespole o podział obowiązków** — różni ludzie mają różne geniuses, podział powinien to uwzględniać
- **Sprint planning dla zespołu** — match story type do genius
- **Rekrutacja / self-selection** — wiedzieć, kto pasuje do jakiej roli

### Solo: Working Genius Self-Assessment (20 min)

Każdy z 6 typów oceń w 3 wymiarach:

| Typ | Jak często to kocham? (1-5) | Jak często jestem w tym dobry? (1-5) | Jak często to robię? (1-5) |
|---|---|---|---|
| Wonder | | | |
| Invention | | | |
| Discernment | | | |
| Galvanizing | | | |
| Enablement | | | |
| Tenacity | | | |

**Interpretacja:**
- **Wysokie kocham + wysokie dobry + niskie robię** → NIEDOSTATEK. Czas dodać więcej tych zadań do swojej pracy.
- **Wysokie kocham + niskie dobry** → potencjał do rozwoju, ale nie talent naturalny.
- **Niskie kocham + wysokie dobry** → jesteś dobry, ale to Cię wyczerpuje. Szukaj kogoś, kto to kocha.
- **Niskie kocham + niskie dobry + wysokie robię** → red flag. Albo zmień rolę, albo zmień zakres obowiązków.

### Team: Working Genius Mapping (60 min)

**Warsztat:**

1. **Self-assessment** (15 min) — każdy wypełnia tabelę powyżej
2. **Pair-share** (15 min) — w parach opowiedz "moje top 3 geniuses i jak się objawiają w pracy"
3. **Team map** (15 min) — na tablicy: dla każdego genius type, kto go ma w zespole? Czy mamy coverage?
4. **Role assignment** (15 min) — dla następnego sprintu: kto bierze Wonder (discovery), kto Tenacity (finish)?

**Coverage red flags:**
- Brak kogoś z Tenacity w zespole → projekty nie kończą się na czas
- Wszyscy mają Wonder i Invention, nikt Discernment → zespół ma 100 pomysłów, 0 decyzji
- Tylko 1 osoba ma Enablement → ta osoba jest overworked

### Integracja z innymi frameworkami

- **Lencioni 5 Dysfunctions (F1)** — Working Genius uzupełnia: mówi CO dopasować, 5 Dysfunctions mówią JAK zdiagnozować problemy
- **Psych Safety (F3)** — bez psych safety ludzie boją się mówić "nie lubię tego robić". Z psych safety → szczere rozmowy o talentach.
- **Sheepdog (F4)** — sheepdog chroni zespół przed assignments, które nie pasują do geniuses (np. Tenacity osoba nie powinna robić tylko Wonder pracy).

### Krytyczne uwagi

- **To nie MBTI.** Working Genius jest oparty na obserwacji, nie statystycznej walidacji. Traktuj jako **heurystykę do rozmowy**, nie test osobowości.
- **Kontekst zmienia genius.** To, co kochasz robić w pracy, może nie być tym, co kochasz robić w domu. Oceń w kontekście.
- **Nie etykietuj ludzi.** "Jesteś Wonder-typem" to pułapka. Ludzie mają wszystkie 6, w różnym natężeniu. To mapa, nie wyrok.

---

## Anti-patterns

| Anti-pattern | Dlaczego zły | Co robić zamiast |
|---|---|---|
| Diagnozujesz innych, nie siebie | "Kolega jest toksyczny" to nie diagnosis, to projekcja | Zacznij od self-diagnostic. Zmiana zaczyna się od Ciebie. |
| Confrontation w grupie | Publiczne zawstydzanie niszczy trust | Zawsze 1:1, w bezpiecznej przestrzeni, z NVC script |
| "Brak zaufania" jako jedyny wniosek | Lencioni #1 to fundament, ale nie jedyny problem | Zrób pełną mapę 5 poziomów. Głosuj na najważniejszy. |
| Ignorowanie hoarderów | "On/ona się nie zmieni" to wyrok, nie diagnoza | Confrontation script. Jeśli 2 próby bez zmiany → eskalacja do managera. |
| "Psych safety" jako wymówka by unikać konfliktów | Edmondson: psych safety ≠ comfort zone. To bezpieczeństwo do challenging, nie do milczenia. | Po #1-2 (inclusion + learner), AKTYWNIE zachęcaj do niezgody. |
| Sheepdog jako gatekeeper | SM/Coach blokuje wszystko, staje się bottleneckiem | Sheepdog chroni zespół, ale NIE decyduje za zespół. Empowerment, nie kontrola. |
| Brak follow-up po diagnozie | "Zrobiliśmy super warsztat" i nic się nie zmienia | Każdy health check = max 1 action item na sprint. Mierz w retro. |

---

## Solo vs Team — Quick chooser

| Twoja sytuacja | Tryb |
|---|---|
| Jesteś sam/sama w projekcie, masz wewnętrzny blok | **Solo** |
| Pracujesz z 2-5 innymi osobami | **Team** |
| Chcesz zrozumieć własny wzorzec (np. hoarding) | **Solo** |
| Chcesz zbudować trust w małym zespole | **Team** |
| Planujesz zmianę procesu / narzędzia | **Solo** + konsultacja z teamem |
| Burnout / chronic stress | **Solo** (ale rozważ też `agent-mindful-coach`) |
| Ktoś w zespole jest wyraźnym blockerem | **Team** mode, 1:1 confrontation script |

---

## When this skill is NOT enough

- **Terapia / trauma / kryzys emocjonalny** → `agent-mindful-coach` (nie próbuj leczyć team dynamics przez terapię)
- **Problemy HR / wynagrodzenia / struktura firmy** → eskalacja do managera / HR
- **Toksyczny manager / systemowy mobbing** → poza scope agile coacha. Dokumentuj, eskaluj, rozważ zmianę środowiska.
- **Konflikt wartości / etyki** → inne ramy, nie team dynamics

---

## After this skill

1. Zaloguj diagnosis do `memory/decisions.md` (jeśli solo) lub wspólnego notatnika (jeśli team)
2. Wybierz **max 1** dysfunction / problem do address w następnym sprincie
3. Zaplanuj **konkretne rytuały** (nie deklaracje typu "będziemy bardziej ufać")
4. Sprawdź postępy w następnej retro (Stage 1 retro: review last sprint actions)

---

## Framework Credits

Ten skill korzysta z frameworków i koncepcji opisanych w
[ATTRIBUTION.md](../../ATTRIBUTION.md):

- **The Five Dysfunctions of a Team (Lencioni, 2002)** — piramida 5 dysfunkcji, hierarchy of trust
- **Fearless Organization (Edmondson, 2018)** — 4 stages of psychological safety
- **Nonviolent Communication (Rosenberg, 2003)** — 4-krokowy script konfrontacji
- **Crucial Conversations (Patterson et al., 2002)** — narzędzia trudnych rozmów (1:1 confrontation)
- **Scrum Guide (Schwaber & Sutherland)** — implicit: rola Scrum Mastera jako servant-leader i sheepdog
- **Mountain Goat Software — Scrum Repair Guide (Cohn)** — Module 5: Dysfunctional teams (public course reference)
