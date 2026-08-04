# Microcopy Patterns

Per-component rules and string inventories. Load when writing any UI string.

Rule of thumb for every component below: **write every state, not just the one in the mockup.**
A component ships with empty, loading, partial, error, success, and permission-denied states.
Missing states are where copy debt accumulates.

---

## Frontloading and the inverted pyramid on small screens

The inverted pyramid is usually taught for articles. It matters more in UI, and most of all on
mobile, where the reader sees three words before deciding whether to keep going.

- **First word carries the action.** *Apply in 5 minutes* beats *In 5 minutes you can apply*.
  If the user reads only the first word, they should still know what this is.
- **Descriptive titles, not category labels.** *Delivery is delayed by 2 days* beats *Order
  update*. A good title lets someone stop after one line and still act correctly.
- **Title-to-CTA continuity.** Many people read the title, skip the body, and press the button.
  Read those two alone: do they make sense together? *Delete "Q3 report"?* → *Delete report* works.
  *Delete "Q3 report"?* → *Confirm* does not.
- **Lead with the constraint.** *Out of stock — back on 14 March*, not *We expect this item to be
  back in stock on 14 March, as it is currently out of stock.*
- **Modular blocks.** Each section stands alone, because people enter mid-screen and leave early.
  Nothing should depend on a sentence three blocks up.
- **Keyword placement.** Scanning concentrates on the beginning of lines and, to a lesser degree,
  their ends. Meaningful words go there; filler goes in the middle or gets cut.
- **Bullets over paragraphs** whenever the content is a list in disguise.

## Buttons and CTAs

| Rule | Do | Don't |
|---|---|---|
| Verb + object, 1–3 words | *Save changes*, *Delete project* | *Submit*, *OK*, *Click here* |
| Match the heading's promise | Modal "Delete project?" → button *Delete project* | Modal "Delete project?" → button *Confirm* |
| Never make the destructive option the calm one | *Delete* (destructive styling) vs *Keep project* | *OK* vs *Cancel* for a delete |
| Read alone | *Buy access* | *Continue* (continue to what?) |
| Sentence case | *Add payment method* | *Add Payment Method* |

**Cancel vs. the honest alternative.** `Cancel` is ambiguous in any dialog that itself cancels
something ("Cancel subscription?" → `Cancel` / `Cancel`). Name both outcomes:
*Keep subscription* / *Cancel subscription*.

**Loading and in-flight labels.** Use the progressive form of the same verb: *Save changes* →
*Saving…*. Never swap to an unrelated word. Keep the button width stable — reserve for the
longest state.

Character budget: primary CTA ≤ 20 chars EN, ≤ 26 chars PL. Beyond that the button wraps on mobile.

---

## Labels, placeholders, helper text

Three distinct jobs. Do not merge them.

| Element | Job | Persistent? | Example |
|---|---|---|---|
| Label | Names the field | Yes — never hide it | *Email* |
| Helper text | Explains a constraint or consequence | Yes, when the rule is not obvious | *We use this for receipts only* |
| Placeholder | Shows a format example | No — disappears on focus | *name@company.com* |

Hard rules:

- Never use a placeholder as the label. It disappears exactly when the user needs it, and screen
  readers treat it inconsistently.
- Never repeat the label in the placeholder.
- Helper text states the rule *before* the user breaks it (*At least 12 characters*), so the
  error message is a fallback rather than the primary teaching moment.
- No "Please" and no trailing colon-instructions in labels. *Email*, not *Please enter email:*.
- Optional fields are marked, required fields are not — unless most of the form is optional, then
  invert. Mark whichever is the minority.

---

## Empty states

Three kinds, three different jobs. Choosing the wrong kind is the most common empty-state failure.

| Kind | Trigger | Job | Shape |
|---|---|---|---|
| First-run | User has never created data | Teach + activate | What this is (1 line) → why it helps (1 line) → primary action |
| Cleared | User finished everything | Confirm + close the loop | Acknowledge → optional next action |
| No results | Filter or search returned nothing | Recover | What was searched → why nothing matched → how to widen |

Never use the same string for all three. "No invoices" as a first-run state wastes the single best
teaching moment in the product.

No-results copy must echo the query: *No results for "acme corp"* — this alone resolves a large
share of "the search is broken" tickets, because the user sees their typo.

---

## Modals and confirmations

Structure: **Title = the question. Body = the consequence. Buttons = the two outcomes.**

- Title is a question or a noun phrase naming the action: *Delete 3 files?*
- Body states what is irreversible and what is not, and what happens to related data:
  *This also removes the shared links. Files in the trash are recoverable for 30 days.*
- Include the count and the name of the object. *Delete "Q3 report"?* beats *Delete this item?*
- Only interrupt for consequences that are irreversible, expensive, or affect other people.
  Everything else gets an undo toast instead of a modal.
- Prefer **undo over confirm**. A confirmation dialog trains dismissal; an undo affordance
  actually protects the user.

Destructive confirmation requiring typed input (type the project name) is reserved for
genuinely unrecoverable, high-blast-radius actions. Overusing it produces muscle-memory typing.

---

## Toasts, banners, inline messages

| Surface | Use for | Lifetime | Rule |
|---|---|---|---|
| Inline | Field-level validation, contextual help | Persistent | Sits next to the cause |
| Toast | Transient success, undo | 4–8 s | Never for errors that need action |
| Banner | System-wide state, degraded service, billing | Until resolved | Dismissible only if non-blocking |

Never put a required action inside a disappearing toast. Never stack more than one banner —
if two conditions are live, write one message that covers the more severe.

---

## Onboarding and first-run

- Explain the **outcome**, not the feature: *Get paid faster*, not *Invoicing module*.
- One idea per step. If a step needs two sentences of setup, it is two steps or a bad step.
- Always offer a visible skip. Copy on the skip is neutral: *Skip for now* — never *No thanks,
  I don't want to get paid faster*.
- Empty-state teaching beats a tour. Prefer copy placed where the work happens.
- Progress copy states remaining effort honestly: *Step 2 of 3*, not *Almost done!*

---

## Permissions and sensitive prompts

Ask **at the moment of need**, never on launch, and state the exchange:

```
<What we need>  →  <what the user gets>  →  <what we won't do>
Allow notifications so you know when a client pays.
You can turn this off anytime in Settings.
```

Never claim a benefit the permission does not deliver. Never pre-check consent. Never bundle
marketing consent with functional consent in one control.

---

## Cancellation, downgrade, deletion

The hardest test of a content system's honesty.

- State exactly what the user loses and when: *Your plan stays active until 14 March. After that,
  exports are read-only.*
- Offer a genuine alternative once (pause, downgrade), phrased neutrally, and never as a
  precondition for continuing.
- The confirm button says what happens: *Cancel subscription*.
- No guilt, no sad mascots, no "are you sure you want to abandon your progress?"

---

## Notifications and system messages

- Subject/first line answers "why is this on my screen right now".
- Name the actor and the object: *Anna commented on "Q3 report"*.
- No notification without a destination — every one deep-links to the thing it describes.
- Batch, don't spam: *3 new comments on "Q3 report"*.

---

## Numbers, dates, units, variables

- Digits for all quantities, including one through nine, in UI (prose can differ).
- Absolute dates for anything actionable (*Due 14 March*), relative for recency (*2 hours ago*).
  Never relative for deadlines, contracts, or billing.
- Currency with explicit code where multi-currency exists: *1 200,00 PLN*.
- Name variables semantically: `{fileName}`, `{count}`, `{planName}` — never `%s` or `{0}`.
- Every variable needs a fallback string and a pluralization rule. Polish has three plural
  forms (1 / 2–4 / 5+); English has two. Never build a plural by concatenating "(s)".
- Never build a sentence by concatenating fragments across the codebase — it breaks in every
  language with different word order.
