---
created: 2026-07-20
updated: 2026-07-20
version: 1.0
description: Skondensowane wytyczne "AI-Ready FigJam" — jak budować FigJam, aby był bezbłędnie czytelny dla LLM-ów (Vision i REST API). Z referencjami branżowymi.
---

# LLM-Ready FigJam — wytyczne

Najlepsze praktyki zebrane z zespołów R&D pracujących z Vision LLM-ami i narzędziami Figma AI. Figma nie wydała oficjalnej dokumentacji "Design for AI Agents" — te wytyczne są nieoficjalnym standardem zbieranym przez badaczy LLM.

## 1. Architektura przestrzenna (semantyka zamiast czytania z "powietrza")

Agenci znacznie lepiej radzą sobie z hierarchią drzewiastą niż ze swobodnym układem przestrzennym.

- **Sekcje (Section / Frame) jako kontenery kontekstu.** Agent łatwo gubi się w otwartej przestrzeni. Zamykaj logiczne obszary w sekcje i nadawaj im jednoznaczne nazwy (`[03_SECTION_Release_1] Core Value Proof`).
- **Kolejność czytania Z-pattern / F-pattern.** Sekcje i macierze od lewej do prawej, od góry do dołu. Agenci przetwarzają obiekty po współrzędnych X/Y lub sekwencyjnie z drzewa warstw.
- **Tytuły macierzy jawne.** Nie polegaj na pozycji kartki w prawym górnym rogu. Dodaj nagłówki osi lub kwadrantów jako osobne etykiety tekstowe.
- **Root SECTION zbiorcza.** W FigJam owij wszystko w jedną root SECTION (`[STORY_MAP]`). Bez tego kartki trafiają do `unsectioned_nodes` w JSON.

## 2. Wewnętrzne nagłówki tekstowe (defense vs utratę nazwy sekcji)

W FigJam nazwa SECTION renderuje się na zewnętrznej krawędzi ramki. `Copy as PNG` ucina etykiety lub renderuje je poza kadrem.

- **Wstaw wewnątrz każdej sekcji zwykły blok tekstowy** z nagłówkiem (`### SECTION: V1_MVP (Core Value)`). Niezależnie od zaznaczenia do eksportu, nagłówek zawsze trafia na zrzut ekranu.
- **Klikaj w nazwę SECTION, nie w kartki**, żeby zaznaczyć całą ramkę z nagłówkiem.
- **Panel Export → PNG → Include background** zachowuje etykiety i tła.
- **Parser REST API** pomija ten problem — pobiera `node.name` z JSON niezależnie od widoczności na zrzucie.

## 3. Sticky notes — składnia i taksonomia

Mieszanie kolorów i dowolnego tekstu = halucynacje agenta. Najbardziej deterministyczna metoda (zarówno dla JSON, jak i Vision) to **taksonomia prefiksowa w nawiasach kwadratowych**.

### Składnia kanoniczna

```
[TYPE] [PRIORITY] Treść właściwa [METADATA]
```

### Prefiksy

| Kategoria | Tagi | Przykład |
|---|---|---|
| Typ elementu | `[INSIGHT]`, `[PROBLEM]`, `[IDEA]`, `[RISK]`, `[DECISION]`, `[ACTION]`, `[STORY]`, `[ACT]`, `[TASK]` | `[PROBLEM] Koszyk nie zapamiętuje metody dostawy.` |
| Priorytet | `[P1]`, `[P2]`, `[P3]` lub `[MUST]`, `[SHOULD]`, `[COULD]` | `[IDEA] [P1] Szybki checkout BLIK.` |
| Stan / status | `[OPEN]`, `[IN_REVIEW]`, `[DONE]`, `[BLOCKED]` | `[ACTION] [BLOCKED] Walidacja prawna.` |
| Przypisanie | `@UX`, `@DEV`, `@PM`, `@BIZ` | `[ACTION] Sprawdzić logi GA4. @DEV` |
| Release | `[V1]`, `[V2]`, `[V3]` | `[STORY] [V1] [P1] ... @DEV` |

### Dlaczego nie natywne Badge / Stamps FigJam?

Stample i naklejki w FigJam są w JSON osobnymi obiektami wektorowymi (`STAMP` / `STICKER`), często niepowiązanymi z kartką relacją rodzic-dziecko. Dla agenta czytającego drzewo to osobne ikony leżące obok. Prefiks tekstowy wpisany w kartce jest nie do pomylenia.

## 4. `[00_SECTION_AI_ReadMe]` — System Prompt wbudowany w kanwę

Sekcja na początku kanwy (najlepiej `x: 0, y: 0` względem roota) jako instrukcja obsługi dla agenta — szczególnie przydatna dla Vision LLM i eksportu PNG.

Przykładowa treść:

```text
==================================================
SYSTEM INSTRUCTIONS FOR AI AGENT (FIGJAM PARSER)
==================================================
PURPOSE:
Ten plik zawiera syntezę warsztatu UX z podziałem na sekcje.

CANVAS STRUCTURE:
- Sekcje ułożone horyzontalnie: [01_BACKBONE_Activities] -> [02_BACKBONE_User_Tasks] -> [03_Release_1] -> [04_Release_2] -> [05_Release_3]

COLOR SEMANTICS:
- Zielony (#B3EFBD) = Activities (backbone L1)
- Cyan (#B3F4EF) = Tasks (backbone L2)
- Pomarańczowy (#FFD3A8) = Release 1 (V1, MVP)
- Fioletowy (#D3BDFF) = Release 2 / 3 (V2/V3, hipotezy)

CONNECTOR RULES:
- Strzałka A -> B = relacja przyczynowo-skutkowa (A wywołuje B)
- Krawędzie czerwone = blokady (A BLOCKS B)

OUTPUT EXPECTED:
Markdown backlog z podziałem Release -> Activity -> Task -> User Stories (z AC + Owner)
==================================================
```

## 5. Semantyka przestrzenna dla macierzy

FigJam Section nie może tworzyć klasycznej siatki 2D (Section × Section). Rozwiązanie hybrydowe dla LLM:

- **Sekcje (SECTION) dla rzędów (Releases):** główne kontenery logiczne w JSON (`[03_SECTION_Release_1]`, `[04_SECTION_Release_2]`).
- **Chronologia (oś X) kodowana w identyfikatorach zadań lub pozycji X:** `[TASK_01]`, `[TASK_02]`, `[TASK_03]` w backbone. Każda `[STORY]` w release dziedziczy identyfikator taska, nad którym leży — **algorytmicznie po osi X**, nie przez ręczne ID na kartce.
- **Jawne etykiety osi** dla macierzy (opcjonalnie): `[AXIS_X_MIN]`, `[AXIS_X_MAX]`, `[AXIS_Y_MIN]`, `[AXIS_Y_MAX]`.

## 6. Relacje i połączenia (Connectors)

### Kiedy STOSOWAĆ

- **Odgałęzienia / przepływy alternatywne (Branching):** `[STORY_05] --[IF_FAIL]--> [STORY_05B] Ekran błędu`.
- **Twarde zależności między wydananiami (Cross-Release Dependencies):** `[STORY_12_V2] --[REQUIRES]--> [STORY_03_V1]`.
- **Kryteria akceptacji / notatki:** doprecyzowująca kartka przyłączone do głównej Story (choć preferowane: AC w tej samej kartce).

### Kiedy UNIKAĆ

- **Liniowy przepływ chronologiczny (krok 1 → krok 2 → krok 3).** 100 strzałek = spaghetti payload w JSON. Chronologię agent odczytuje z pozycji X + numeracji `[TASK_*]`.

### API Figmy — pola Connector

- `connectorStart.endpointNodeId` — ID startowego węzła
- `connectorEnd.endpointNodeId` — ID końcowego węzła
- `characters` — etykieta tekstowa relacji

Używaj **natywnych Connectors** (nie linii rysowanych pen-toolem — te są w JSON zbiorem wektorów bez semantyki relacji).

## 7. Parsowanie — co kiedy używać

| Metoda | Kiedy | Plusy | Minusy |
|---|---|---|---|
| **Figma REST API (JSON)** | Produkcja, duże boardy, >50 kartek | 100% deterministyczne, zero OCR, niski koszt tokenów, metadane (x,y, sekcja, connectory) | Wymaga ważnego `FIGMA_TOKEN` |
| **Vision LLM (PNG)** | Szybki wrzut, małe boardy | Brak tokenu API | OCR przekłamania przy >100 kartkach, gubienie metadanych przestrzennych |
| **PDF export** | NIGDY | — | Wektory tekstu, najgorsze do ekstrakcji (x,y) |

## 8. Semantyka kolorów

Kolor w JSON to tylko HEX. Agent nie wie, że żółty = ryzyko, chyba że ma legendę.

- **Sekcja Legenda w `[00_SECTION_AI_ReadMe]`** (Czerwony = Bloker, Zielony = Pomysł)
- **Prefiksy tekstowe na kartkach** (deterministyczne, czytane i przez JSON, i przez Vision)

## 9. Hygiena kanwy (3 zasady dla parsera X-axis mapping)

- **Układaj w pionowych słupkach:** kartki tego samego taska jedna pod drugą.
- **Zachowaj odstępy 40–60px między kolumnami:** daje algorytmowi ogromny margines błędu.
- **Nie nakładaj kolumn na siebie:** dopóki kartka z jednej kolumny nie wjedzie do połowy szerokości pod sąsiednie zadanie, parser się nie pomyli.

## 10. Lean UX — priorytety i ownerzy tylko w V1

- **V1 (MVP):** precyzyjne — `[P1]/[P2]/[P3]` + `@Owner` (UX/DEV/PM), bo wchodzi do najbliższego sprintu.
- **V2, V3:** opcje i hipotezy — zero priorytetów, zero ownerów. Planowanie wykonawców dla wydań, które i tak ulegną zmianie po zderzeniu V1 z rynkiem, to Big Upfront Design (Patton + Lean UX).

## 11. AC inline (w tej samej kartce co Story)

- **Kryteria akceptacji w tej samej kartce co `[STORY]`**, pod zdaniem story, po `AC:`.
- Osobna kartka obok Story = dwa rozłączne obiekty w JSON — agent musi zgadywać relację po (x,y).

## 12. Słownik Patton (oficjalne terminy)

| Pojęcie | Tag | Poziom |
|---|---|---|
| User Activity | `[ACT_01]`, `[ACT_02]` | Backbone L1 (główny cel użytkownika) |
| User Task | `[TASK_01]`, `[TASK_02]` | Backbone L2 (krok w procedurze) |
| User Story | `[STORY]` | Release (plasterek funkcjonalności) |
| Release Slice / Version | `[V1]`, `[V2]`, `[V3]` | Rząd horyzontalny |
| Backbone | `[01_SECTION_BACKBONE_Activities]` + `[02_SECTION_BACKBONE_User_Tasks]` | Statyczna struktura nagłówkowa |
| User Journey | Przepływ chronologiczny wzdłuż osi X | Pojęcie procesowe (czas) |

**Używaj `Task`, nie `Step`.** "Step" jest terminem User Journey Mapping (mapowanie ścieżki), ale w Story Mappingu Pattona standardem branżowym jest `Task`.

## 13. Product Discovery — MDP, Torres, Gothelf

Story Map to discovery artifact, nie execution backlog. Żyje w trójkącie Patton (struktura) + Gothelf (Lean UX) + Torres (Continuous Discovery). Te trzy zasady chronią zespół przed przeładowaniem zakresu (Scope Creep) i przed traktowaniem V2/V3 jako "resztka wszystkiego".

### MDP > MVP (Minimum Desirable Product)

- **MVP** (Minimum Viable Product) pyta: "co najmniej możemy wysłać, żeby to działało?"
- **MDP** (Minimum Desirable Product) pyta: "co najmniej możemy wysłać, żeby użytkownik tego **chciał**?"
- W Story Mappingu V1 powinno być MDP, nie MVP. Slice, który jest tylko viable ale nie desirable, uczy zły sygnał — użytkownik go nie używa, nie dostajesz feedbacku, marnujesz sprint.
- W praktyce: jeśli V1 ma >12–15 stories per Activity, prawdopodobnie to MVP, nie MDP. Odetnij do doświadczenia, które użytkownik faktycznie chce mieć (a nie "wszystko co potrzebne, żeby to w ogóle działało").
- Źródło: Gothelf & Seiden, *Lean UX* (2013) — hypothesis-driven; Torres, *Continuous Discovery Habits* (2023) — opportunity-solution tree napędzana weekly interviews.

### Torres — Continuous Discovery cadence

Story Map nie jest jednorazowym warsztatem. Jest living artifact, aktualizowany w rytmie Continuous Discovery:

- **Weekly opportunity interviews** → odkrywasz nowe opportunities
- **Opportunity-Solution Tree (OST)** → mapujesz opportunities → solutions → experiments
- **Story Map aktualizacji** → nowy `[ACT_*]` lub `[TASK_*]` tylko gdy wchodzi nowy duży obszar discovery; w istniejących Taskach dodajesz story do odpowiedniego release
- **V1 zamrożone w trakcie sprintu** — V2/V3 otwarte na hipotezy z interviews
- Źródło: Teresa Torres, *Continuous Discovery Habits* (2023) — https://www.producttalk.org/

### Gothelf — Lean UX w Story Map

- **Story Map to hipoteza, nie specyfikacja.** Każde `[STORY]` to "wierzymy, że użytkownik X chce Y, żeby osiągnąć Z" — nie "budujemy Y".
- **V2/V3 czyste (zero `[P*]`, zero `@Owner`)** = kluczowa reguła Lean UX. Planowanie wykonawców i priorytetów dla hipotez = Big Upfront Design. V1 się zweryfikuje z rynkiem, V2/V3 ulegną zmianie.
- **Outcome over output.** Release nazwy z business goal (`Core Value Proof`, `Business Goal or Outcome`), nie "v2 dla v2". Patton zachęca do podawania krótkiego celu biznesowego obok numeru wersji.
- **Build-Measure-Learn loop** (Ries): V1 → ship → measure → learn → aktualizuj V2/V3 (lub anuluj). Story Map musi być aktualizowalna bez muda — dlatego `figjam-storymap-llm` parsuje algorytmicznie po osi X, żeby zespół mógł przeciągać kartki bez przepisywania ID.
- Źródło: Gothelf & Seiden, *Lean UX* (2013); Eric Ries, *The Lean Startup* (2011).

### Scope creep — sygnały ostrzegawcze w Story Map

- V1 > 12–15 stories per Activity → prawdopodobnie MVP, nie MDP
- V2/V3 z `[P*]` lub `@Owner` → Big Upfront Design
- `[STORY]` w build-first voice ("Build X", "Implement Y") → anty-wzorzec Patton (story map = perspektywa usera)
- Puste `[TASK_*]` (bez story w żadnym release) → albo martwy eksperyment, albo brakujące discovery
- Cykle connectorów w tym samym release → podejrzenie duplikatu story lub brakującej zależności
- Connectors dla liniowego przepływu (krok 1 → krok 2 → krok 3) → spaghetti payload, chronologia kodowana w X + numeracji `[TASK_*]`

### Coaching stance

Agent pracujący z Story Mapą nie jest pasywnym readerem — jest **Structure Guardian**:

- Flaga problemu z node ID / sticky name
- Proponuje najmniejszą konkretną zmianę (nie "refactoruj to", tylko "zmień `[STORY] [V1] Build login API @DEV` na `[STORY] [V1] User signs in with Google @DEV`")
- Nie cicho naprawia — raportuje, żeby zespół uczył się wzorca
- Pyta przed cięciem scope'u: "czy to jest viable, czy desirable?" — wymusza MDP, nie MVP

---

## Referencje branżowe

### Oficjalna dokumentacja i struktury danych

- **Figma REST API Documentation — Node Types** — https://www.figma.com/developers/api
  Opis struktur: SECTION, STICKY, CONNECTOR, WIDGET, SHAPE_WITH_TEXT w drzewie JSON. Specyficzne dla FigJam: https://www.figma.com/developers/api#figjam-nodes

- **Figma Plugin API — StickyNode & SectionNode** — https://www.figma.com/plugin-docs/
  Właściwości obiektów FigJam dostępne programistycznie (kolor, author, textContent, boundingBox).

### Standardy promptowania przestrzennego i Vision LLM

- **Anthropic Claude Vision — Image & Layout Guidelines** — https://docs.anthropic.com/en/docs/build-with-claude/vision
  Wytyczne dostarczania obrazów, diagramów i struktur przestrzennych do modeli wizyjnych.

- **OpenAI Cookbook — Processing Spatial & Visual Data** — https://cookbook.openai.com/
  Najlepsze praktyki dla struktur tabelarycznych, wykresów i zrzutów ekranu do GPT-4o.

- **OpenAI GPT-4o Vision System Card** — https://openai.com/index/hello-gpt-4o/
  Ograniczenia OCR w gęstych układach i rekomendacje strukturyzacji.

### Architektury canvas-to-JSON (open-source references)

- **tldraw / Make Real Documentation** — https://github.com/tldraw/tldraw / https://makereal.tldraw.com/
  Jeden z najbardziej zaawansowanych projektów łączących nieskończoną kanwę z agentami AI. Architektura transkrypcji kształtów na prompty (Canvas-to-Code / Canvas-to-JSON) to obecny standard branżowy dla narzędzi typu whiteboard.

- **Excalidraw + AI experiments** — https://github.com/excalidraw/excalidraw
  Open-source alternatywa, przydatna do porównania wzorców kanwa → struktura.

### Metodyka (kanoniczne źródła)

- **Jeff Patton — User Story Mapping** (O'Reilly, 2014) — https://www.oreilly.com/library/view/user-story-mapping/9781491973899/
  Backbone + Slices + Walking Skeleton.

- **Jeff Patton — www.jpattonassociates.com** — https://www.jpattonassociates.com/user-story-mapping/
  Komentarze autora, wzorce, case studies.

- **Lean UX (Gothelf & Seiden, 2013)** — https://www.jeffgothelf.com/lean-ux-book/
  Hypothesis-driven, MVPs, kolaboracyjny design, walka z Big Upfront Design.

- **Mike Cohn — User Stories Applied (2004)** — https://www.mountaingoatsoftware.com/books/user-stories-applied
  INVEST, AC inline, story splitting.

- **Mountain Goat Software — Better User Stories course** — https://www.mountaingoatsoftware.com/courses/better-user-stories
  Transkrypcja kursu stosowana w `agent-agile-master`.

- **Teresa Torres — Continuous Discovery Habits (2023)** — https://www.producttalk.org/
  Story Map jako living artifact w weekly discovery cadence; Opportunity-Solution Tree.

- **Eric Ries — The Lean Startup (2011)** — http://theleanstartup.com/
  Build-Measure-Learn loop; story map musi być edytowalna bez muda.

### Wzorce dla AI-ready warsztatów

- **Atlassian — How to run a remote workshop with Confluence + Jira** — https://www.atlassian.com/agile/project-management/workshops
  Industry template dla warsztatów → backlog.

- **Miro Academy — AI in workshops** — https://help.miro.com/hc/en-us/categories/360002318013
  Wzorce tagowania i strukturyzacji kanwy (analogiczne do FigJam).

---

## Kolejność priorytetów źródeł

1. **Figma REST API** (techniczne — struktury węzłów) — https://www.figma.com/developers/api
2. **Anthropic Vision Guidelines** (prompt engineering) — https://docs.anthropic.com/en/docs/build-with-claude/vision
3. **tldraw / Make Real** (architecture reference) — https://github.com/tldraw/tldraw
4. **Patton (User Story Mapping)** (metodyka) — https://www.jpattonassociates.com/user-story-mapping/

Te cztery źródła pokrywają 90% wytycznych. Reszta to uzupełnienia branżowe.