# Explainer and Documentation Structure

Load when writing a help-center article, a concept explainer, a design decision doc, a release
note, or any long-form piece that has to make a complex product problem understandable.

## The default shape: inverted pyramid

Conclusion first. Then the reasoning. Then the detail. Most readers stop after the first screen —
build for that, not against it.

```
TL;DR            ← the answer, 2–4 lines, useful alone
What this is     ← the concept in one paragraph, no jargon
Why it matters   ← the consequence for this reader
How it works     ← the mechanism, scannable, one idea per section
Worked example   ← concrete, with real values
Edge cases       ← what breaks and what to do
What to do next  ← a single, specific action
```

The TL;DR is not a teaser. Someone who reads only the TL;DR must be able to act correctly.

---

## Scannability rules

- **One idea per paragraph.** If a paragraph has two ideas, it has two paragraphs.
- **3–5 sentences maximum** per paragraph in web copy.
- **Descriptive headings**, not labels: *Why reconciliation fails when dates don't match*, not
  *Background*. A reader should navigate by headings alone.
- **Front-load every heading, sentence, and list item.** The first three words carry the meaning.
- **Bold the decision-relevant phrase**, not random emphasis. Bolding everything bolds nothing.
- **Tables for comparisons, lists for sequences, prose for reasoning.** Choosing the wrong
  container is the most common structural failure.
- **Code, values, and UI labels in the exact form the user sees them.**

---

## Explaining something genuinely complex

The order that works, tested against the way people actually build understanding:

1. **Anchor to what they know.** One analogy, close to their domain. One — not a running metaphor.
2. **Name the thing.** Give the concept its real name immediately; a reader who cannot name it
   cannot search for it or ask about it.
3. **State the mental model in one sentence.** If you cannot, you do not understand it well
   enough to write about it yet.
4. **Show the smallest complete example.** Real values, not `foo`. The example must run or apply
   end to end — a partial example teaches a partial model.
5. **Then complicate.** Add the exceptions after the model holds, never during.
6. **Close the loop.** State explicitly what the reader can now do that they could not before.

Anti-patterns specific to explainers:

- **Definition chains** — explaining term A with terms B and C, which are themselves undefined.
  Check every noun in your first paragraph against your assumed vocabulary.
- **History first.** Nobody needs the origin story before the answer. Move it to the end or cut it.
- **Completeness over usefulness.** An article covering every edge case teaches none of them.
  Cut to the 80 % path; link the rest.
- **The metaphor that keeps paying rent.** One analogy, used once, then dropped.

---

## Article types and their shapes

| Type | Reader's state | Shape |
|---|---|---|
| Task / how-to | Wants to finish something now | Prerequisites → numbered steps → result → troubleshooting |
| Concept explainer | Wants to understand a model | Inverted pyramid, above |
| Troubleshooting | Blocked, frustrated | Symptom → likely cause → fix, per symptom. No preamble. |
| Design decision doc | Evaluating a choice | Context → options considered → decision → consequences → revisit trigger |
| Release note | Scanning for impact | What changed → who it affects → what you need to do → link to detail |
| FAQ | Has a specific question | Real questions in the user's phrasing, answer in the first sentence |

**Numbered steps rules:** one action per step; the outcome stated in the step where it appears
(*Click Save. The invoice moves to Sent.*); UI labels quoted exactly; screenshots only where the
target is genuinely hard to find; never bury a prerequisite in step 4.

**Troubleshooting rules:** organize by the symptom the user sees, never by the system's internal
cause. Users search with what is on their screen.

---

## Writing for domain experts

When the audience knows the domain better than the product team:

- Use their vocabulary exactly. Translating their nouns into consumer language reads as
  condescension and costs credibility on the first paragraph.
- Lead with the mechanism, not the reassurance. Experts want to know what the system does, then
  decide for themselves whether to be reassured.
- State limits and failure modes explicitly. Experts probe edges; a doc that hides them loses trust.
- Cite the standard, regulation, or spec by name and number where one governs the behaviour.
- Skip the analogy. Analogies help novices and slow experts down.

---

## Quality checklist

- [ ] TL;DR is complete and actionable read alone
- [ ] The answer appears before the reasoning
- [ ] Headings are descriptive; the article navigates by headings alone
- [ ] Every jargon term is defined at first use or replaced
- [ ] One worked example with real values
- [ ] Edge cases named, with what to do
- [ ] Ends with one specific next action
- [ ] Tables for comparison, lists for sequence, prose for reasoning — not mixed up
- [ ] Passes read-aloud
- [ ] Nothing promised that the product does not do
