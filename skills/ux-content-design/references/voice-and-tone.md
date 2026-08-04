# Tone and Bilingual Register

Load when choosing register for a specific moment, or writing bilingual PL/EN copy.

**Voice lives in `voice-chart.md`.** This file is only about how that fixed voice adapts to the
moment, and how it behaves across two languages. If the question is *who is this product*, you
are in the wrong file.

## Voice vs. tone

- **Voice** is constant. It is who the product is. It does not change between a payment failure
  and a confetti screen. Defined once, as constraints, in `voice-chart.md`.
- **Tone** is situational. It is how that voice adapts to the user's emotional state right now.
  That is this file.

A product with a "playful" voice does not become unplayful during an outage — it becomes a
serious, direct version of the same product, which in practice means: drop the jokes, keep the
plain sentence structure and the short words. The voice chart still applies; the tone map decides
how much room the voice gets.

## Tone map

Set tone by the user's emotional state, not by the screen's importance.

| Moment | User feels | Tone | Never |
|---|---|---|---|
| First run | Curious, unsure | Warm, encouraging, concrete | Overwhelming, feature-listing |
| Routine task | Focused | Invisible, terse | Chatty, congratulatory |
| Validation error | Mildly annoyed | Neutral, instructive | Apologetic, cute |
| Failed payment | Anxious | Precise, calm, factual | Personality, exclamation marks |
| Data loss risk | Alarmed | Blunt, unambiguous | Softening, euphemism |
| Success on a hard task | Relieved | Brief acknowledgement, then out of the way | Confetti on every save |
| Cancellation | Decided | Respectful, neutral, complete | Guilt, retention pleading |
| Outage | Blocked, distrustful | Honest, timestamped, no promises | Vague reassurance |

**The escalation rule:** the higher the user's anxiety, the lower the personality. Personality is
a budget spent in calm moments.

## Register by expertise

Domain experts and novices need opposite things. Getting this wrong is the most common
mis-calibration in B2B products.

| | Novice | Domain expert |
|---|---|---|
| Terminology | Plain word first, term in parentheses once | The precise term, immediately |
| What they want to know | What happens to me | Which mechanism fired |
| Over-explaining costs | Nothing | Credibility and speed |
| Under-explaining costs | Abandonment | Nothing |

For expert audiences: use their vocabulary exactly, do not translate their nouns into consumer
language, and put the detail in the primary text rather than behind a disclosure. *Reconciliation
failed: 3 entries have no matching bank record* is right for an accountant and wrong for a consumer.

When both audiences share a screen, use **progressive disclosure**: expert-precise headline,
plain-language body, mechanism behind "details".

## Words to remove on sight

| Remove | Because | Use |
|---|---|---|
| Please | Adds length, adds nothing | (drop it) |
| Simply, just, easily | Tells the user their difficulty is their fault | (drop it) |
| Oops, whoops, uh-oh | Trivializes a real failure | State what happened |
| Sorry (repeated) | Apology inflation reads as insincere | One apology maximum, for real system failures |
| Utilize, leverage, facilitate | Corporate padding | Use, use, help |
| Invalid, illegal | Accusatory | Describe the rule |
| Are you sure? | Says nothing about consequences | Name the consequence |
| Click here | Meaningless out of context | Name the destination |

## Bilingual: Polish and English

**Never translate.** Write natively in each language, from the same brief. Translated UI copy
reads as translated within one sentence.

### Length expansion

Budget for the longest language in the frame.

| Target | Typical expansion from EN | Practical rule |
|---|---|---|
| Polish | +20–30 % | Give buttons ~30 % headroom |
| German | +30–35 % | Worst case for compound nouns |
| French | +15–20 % | |
| Spanish | +15–25 % | |

Short EN strings expand worst: a 6-character button can grow past 12. Test buttons and tabs first.

### Polish-specific rules

- **Gender.** Avoid forms that force the user's gender. Prefer impersonal constructions
  (*Nie udało się zapisać zmian*) over past-tense personal forms (*Zapisałeś / Zapisałaś*).
  Use nouns over participles where the participle would need agreement.
- **Formality.** Pick one register and hold it product-wide. Impersonal (*Zapisz zmiany*,
  *Nie udało się…*) is the safest default for B2B; direct *ty* forms suit consumer products but
  must then be used everywhere, including legal-adjacent screens.
- **Imperatives on buttons.** Polish UI convention uses the bare imperative: *Zapisz*, *Usuń*,
  *Anuluj subskrypcję* — not infinitives (*Zapisywanie*) and not nouns.
- **Plurals.** Three forms (1 / 2–4 / 5+). Never fake it with "(y)" or by always using 5+ form.
  Every count string needs all three variants defined.
- **Do not calque English idiom.** *Get started*, *You're all set*, *Oops!* have no natural Polish
  equivalent — write the Polish sentence that does that job, not the Polish words of the English one.
- **Terms of art.** Some English terms are the domain standard in Polish product contexts
  (*deploy*, *sprint*, *onboarding*). Keep them if the audience uses them; do not invent Polish
  neologisms for terms your users already say in English. Decide per term, record in the glossary.

### Delivering bilingual copy

Deliver as a table with both languages side by side and character counts for both. Flag any pair
where lengths diverge by more than 30 % — that is a layout risk to resolve before handoff, not a
localization detail to discover in production.

| Key | EN | chars | PL | chars | Note |
|---|---|---|---|---|---|
| `invoice.empty.title` | No invoices yet | 15 | Brak faktur | 11 | |
| `invoice.empty.cta` | Create invoice | 14 | Utwórz fakturę | 14 | |
