# Evidence

## What was tested, and what was not

**Tested:** Claude Opus 5, running in Claude Code, 2026-08-04. Three runs: one full procedure
execution, one reference-routing check, one negative-trigger check.

**Not tested:** no other model. Not GPT, not Gemini, not Copilot, not any local model. The
`compatibility` field says Claude-only because that is the only claim the evidence supports.

**Not a blind eval.** The same session authored the skill and then ran it, so this is a
**smoke test**, not a Path B parallel-producer comparison against a no-skill baseline. It answers
"does the procedure execute and catch real defects" — it does not answer "is the output better
than a senior writer working without the skill". Treat the findings below as debugging output,
not as a quality claim.

---

## Run 1 — Full procedure, Polish brief, destructive modal

**Prompt:** *"napisz copy do modala usuwania konta"* — deliberately underspecified: no user
segment, no character budget, no language for the strings stated.

**What the skill produced**

Phase 1 correctly refused to guess and emitted a brief with explicit assumptions:

```
Surface: Modal, trwałe usunięcie konta, Ustawienia > Konto
Goal: Inform + Interact
User: ASSUMED — obecny klient płacący, decyzja podjęta
Emotion: zdecydowany, ale zaniepokojony o dane
Constraint: ASSUMED — title ≤ 40, body ≤ 140, CTA ≤ 20
```

Phase 2 produced A and B, and correctly **refused to produce variant C**, citing the data-loss
rule rather than writing a "charming" version of an account deletion. That is the behaviour the
skill is built to force, and it held without prompting.

Phase 3 caught a real defect in its own recommended variant: variant B's body ran **150 characters
against a 140 budget**. The check fired on the recommendation, not only on the rejected options.

Both dismiss labels avoided the `Cancel`-in-a-cancel-dialog trap without being reminded
(*Zachowaj konto* / *Usuń konto*).

**Verdict:** procedure executes end to end. The stress-test is not decorative — it failed the
skill's own preferred draft.

### Defect found → fixed

The length check fired, but `SKILL.md` said only *"revise and re-run"* — no guidance on **what to
cut first**. Left as-is, the natural failure mode is trimming from the end of the string, which
in a destructive modal deletes the recovery window ("recoverable for 30 days") and keeps the
filler. That is the single most damaging possible cut on that screen.

**Fix applied:** Phase 3 now carries an explicit cut order (filler → restating the UI →
justification → second example → the "why") and a never-cut list (consequence, recovery path,
whether money moved, object name and count), plus an escape hatch: if it still does not fit,
the frame is wrong — propose the component change instead of truncating.

---

## Run 2 — Reference routing

**Prompt:** *"błąd płatności — karta odrzucona, co napisać"*

Loaded `references/error-message-anatomy.md` and nothing else. Did not pull the other five
references. The routing table at the top of `SKILL.md` does its job — this matters because loading
all six references on every request would defeat the progressive-disclosure structure.

Output correctly led with the money question (*"Nie obciążyliśmy Cię"*) before the retry options,
which is the payment-specific rule from that reference rather than the generic error contract.

### Defect found → fixed

The reply came back **in English** to a **Polish prompt**. The skill is written in English, and
nothing in it distinguished *the language of the conversation* from *the language of the strings*
— so the English of the instructions leaked into the response.

**Fix applied:** the bilingual section now opens by separating the two explicitly — match the user
for commentary, take the copy language from the product, ask once if unstated.

---

## Run 3 — Negative trigger

**Prompt:** *"napisz post na LinkedIn o nowym feature"*

Skill did not engage the 4-phase procedure. `do_not_use_for` lists sales and campaign copy, and
the boundary held — no brief, no three variants, no character budget imposed on a social post.

This matters more than it sounds: a skill that fires on everything gets uninstalled. The
negative triggers are load-bearing.

---

## Run 4 — Influence copy (found in real use, not in a designed test)

**Prompt:** *"napisz teksty na GitHub i ClawHub"* — the skill applied to its own listing.

**What it produced**

```
Turns "write some copy" into an implementation-ready spec — strings with states,
character budgets, variables, and plural rules.
```

The user rejected it, correctly: it lists **what the skill contains**, not what changes for the
reader. Every word is true and the sentence does no work.

**Why the procedure did not catch it**

Phase 1 recorded `Goal: Influence`, and then Phase 2 drafted with the Direct / Guided / Character
axis — which is a **UI-string axis**. On a persuasive surface it produces three grades of feature
list. Phase 3 then passed the draft, because every check in it was built for UI strings: does the
CTA work read alone, does it fit the frame, is the term in the glossary. **Not one check asked
whether the reader learns what changes for them.**

So the skill logged the right goal in Phase 1 and then had nothing downstream that used it. The
3 I's were recorded and never spent.

This is the most useful defect found so far, because it was found in production use rather than
in a test written by the same person who wrote the procedure.

### Fix applied

- New `references/influence-copy.md` — outcome-vs-output ladder, the "so what?" test, the three
  framings (problem-led / outcome-led / stake-led), specificity over intensity, honesty rules for
  claims, and the inverted length rule (cut scope, never specificity).
- `SKILL.md` Phase 2 now **branches on the goal**: an Influence brief loads the reference and
  switches the variant axis before drafting, instead of defaulting to the UI-string axis.
- `SKILL.md` Phase 3 gained the outcome check, with the standalone-one-liner rule (a lone
  tagline must carry problem *and* outcome; a hook may carry one, but only above a paragraph).
- Two anti-patterns added: the feature list posing as a value proposition, and intensity
  substituted for specificity.
- Routing table and quality checklist updated.

**Residual risk:** the fix is verified only against the case that exposed it. Whether the branch
fires reliably on other Influence surfaces — paywall, upgrade prompt, release headline — is
untested.

## Run 5 — The pastiche defect (found by the user, twice)

**Prompt:** the corrected listing copy from Run 4.

```
Your product doesn't have a writing problem. It has an unwritten-states problem.
```

Rejected again, and correctly. Run 4 fixed *feature list* by producing *tagline* — an antithesis,
which is a slogan structure, not something a person says out loud. The fix for one failure walked
straight into the other.

Worse: `references/influence-copy.md`, written as the Run 4 fix, actively encouraged it. It
offered "stake-led framing" and sanctioned "hooks". The repair had installed the defect.

**Root cause.** The skill had no concept of **register**. It knew about clarity, length, states,
dark patterns — everything that separates good UI copy from bad UI copy — and nothing that
separates product copy from advertising. So under pressure to sound less dull, the only direction
available was toward advertising, because that is the register with the most available devices.

Contributing: voice was specified as a 4-dimension adjective model. A single adjective has no
ceiling, so it gets maximized — the mechanism the user named as *adjective latching*.

### Fix applied

- **`references/golden-standards.md`** — loaded before drafting, not on demand. A taxonomy of 12
  pastiche tells with the plain-sentence replacement for each; the read-aloud gate ("would a
  person say this to another person sitting next to them?"); 15 golden pairs across errors, empty
  states, onboarding, buttons, login, sensitive facts, and confirmations; a product-vs-marketing
  comparison; a few-shot prompt template; and an iteration loop (ask for 3–5 variants, test with
  a frustrated user, promote winners into the example set).
- **`references/voice-chart.md`** — voice defined by constraints instead of adjectives.
  Adjective latching named and countered three ways: mechanical rules over adjectives, tone
  clusters over single words, bounded pairs over descriptions. Bull's-eye logic and the
  synonym-trap test for "this but not that". Full chart with a mechanics row.
- **`SKILL.md`** — identity line changed to "you are not a copywriter and you are not selling
  anything". Read-aloud promoted to the first stress-test check, with the rule that a string
  failing it cannot be saved by passing the others. Pastiche-tell check and adjective audit
  added. Brief gained *coming from* / *leaving with*. Two anti-patterns added: the tagline reflex,
  and marketing register inside the product.
- **`references/influence-copy.md`** — rewritten. "Influence" now explicitly means giving someone
  what they need to choose correctly, including choosing no. Stake-led framing and hooks removed.
  The feature-list and tagline failures are shown side by side with the plain sentence that beats
  both.
- **`references/microcopy-patterns.md`** — inverted pyramid for small screens: first-word action,
  descriptive titles, title-to-CTA continuity read in a vacuum, keyword placement, modular blocks.

**Residual risk.** The read-aloud gate is a judgement call executed by the same model that
produced the string. It is a real constraint, not a guarantee — the honest expectation is that it
catches the obvious tells and that a human still catches the subtle ones.

## Run 6 — Stress case: verifying the Run 5 fix

The anti-pastiche machinery from Run 5 was written and shipped without a single prompt run
through it. This run exists to close that gap.

**Scenario, chosen to be hostile:** a 2 GB export fails for the third consecutive time. The user
has a deadline today and has already lost 16 minutes to two failed attempts. Frustration is high,
which is where brand voice usually leaks in as false cheer or apology performance.

**Output (variant B, recommended)**

```
Eksport przerwany po 8 minutach, trzeci raz. Przy 2 GB połączenie zrywa się przed końcem.
Podziel na kwartały — każda paczka schodzi w około 2 minuty.
[Podziel eksport]  [Spróbuj ponownie mimo to]
```

**Variant C was refused**, unprompted, on the grounds that a third failure under deadline is not a
moment for brand character. That is the behaviour the skill is built to force, and it held under
the conditions most likely to break it.

### What held

| Check | Result |
|---|---|
| Read-aloud gate | Passes — a colleague would say this across a desk |
| Pastiche tells | Zero. No antithesis, no apology performance, no exclamation, no *niestety* |
| Adjective audit | One adjective survives (*za duży*) and it carries information |
| What / why / what next | All three, in that order |
| Blame | None assigned to the user; the cause is stated as a size limit, not a mistake |
| Retry honesty | Repeating a thrice-failed action is not offered as the primary advice, but the door is left open neutrally for someone who wants it anyway |
| Quantified alternative | *~2 minutes per quarter* — checkable, not "faster" |

### What this does and does not prove

It proves the register holds on one hostile scenario, in Polish, with an anxious user. That is the
condition under which the failure was expected, so it is a meaningful check.

It does not prove the fix generalizes. One run, one language, one surface, self-assessed by the
same model that produced the string. The read-aloud gate in particular is a judgement call made by
the author of the sentence — it catches the obvious tells reliably and should not be trusted to
catch the subtle ones. A human still reads the output.

## Known limits

- **Single-model, single-session.** No baseline comparison, no second rater, no blind run.
- **Character counts are computed by the model** and should be verified in the actual frame.
  The skill says this; it does not enforce it.
- **The 30 % PL/DE expansion factors are planning heuristics**, not measurements of your product's
  strings. They are there to force headroom, not to predict a specific overflow.
- **Regulatory references are context, not legal advice.** The dark-patterns table points at DSA,
  GDPR, UCPD, and FTC guidance to explain *why* a pattern is treated as a defect. It is not a
  compliance assessment.
- **Untested at scale.** Every run above was a single surface. Behaviour on a 200-string audit
  across a whole product is unverified.

## What would strengthen this

1. A Path B run: same three prompts to a no-skill Claude, both outputs rated blind on a 5-point
   rubric (brief completeness, variant discipline, defect catch rate, output-contract compliance,
   dark-pattern refusal).
2. One real product audit, to test the audit contract at volume.
3. A native Polish speaker reviewing the PL strings in `examples/before-after.md` for register,
   not just correctness.
