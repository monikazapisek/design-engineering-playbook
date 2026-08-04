# Worked Examples

Four complete runs of the procedure, one per output contract. Use these to match the expected
shape, not to copy the strings.

---

## Example 1 — UI string spec (empty state)

**Request:** "Write copy for the empty invoices table."

### Phase 1 — Brief

```
Surface: Invoices table, first-run empty state (user has never created an invoice)
Goal: Interact (activate) + Inform
User: Freelancer, first week, no accounting background
Emotion: Neutral, slightly unsure what this screen is for
Constraint: Title ≤ 40 chars, body ≤ 140, CTA ≤ 20. PL + EN. Illustration above.
```

### Phase 2 — Variants

| | Title | Body | CTA |
|---|---|---|---|
| **A — Direct** | No invoices yet | | Create invoice |
| **B — Guided** | Create your first invoice | Add a client and your rate — we'll format, number, and send it as a PDF. | Create invoice |
| **C — Character** | Nothing billed yet | Your future self would like some income. Let's fix that. | Create invoice |

**Recommendation: B.** First-run is the product's best teaching surface; A wastes it, and C is
charming once and annoying on the second visit. B states the outcome and the effort in one line.

### Phase 3 — Stress-test

- What / why / next: ✅
- Context-free CTA: ✅ *Create invoice* stands alone
- Length: title 25 EN / 28 PL, body 78 EN / 96 PL, CTA 14 EN / 14 PL — all within budget
- Consistency: glossary uses *invoice*, not *bill* ✅
- Distinguishable from the no-results state ✅ (separate string, below)

### Phase 4 — Ship

| Key | Element | EN | chars | PL | chars |
|---|---|---|---|---|---|
| `invoices.empty.title` | Title | Create your first invoice | 25 | Wystaw pierwszą fakturę | 23 |
| `invoices.empty.body` | Body | Add a client and your rate — we'll format, number, and send it as a PDF. | 71 | Dodaj klienta i stawkę — sformatujemy, ponumerujemy i wyślemy fakturę w PDF. | 75 |
| `invoices.empty.cta` | Primary CTA | Create invoice | 14 | Utwórz fakturę | 14 |
| `invoices.noresults.title` | No-results title | No results for "{query}" | — | Brak wyników dla „{query}" | — |
| `invoices.noresults.body` | No-results body | Try a different client name or clear the date filter. | — | Spróbuj innej nazwy klienta lub wyczyść filtr dat. | — |
| `invoices.error.title` | Load failure | We couldn't load your invoices. | — | Nie udało się wczytać faktur. | — |
| `invoices.error.cta` | Retry | Try again | — | Spróbuj ponownie | — |

Variables: `{query}` — user's raw search string, truncated at 40 chars with an ellipsis.
Fallback if empty: use `invoices.empty.*`.

---

## Example 2 — Error message

**Before**

```
Error: PAYMENT_INTENT_AUTHENTICATION_FAILURE (code 402)
```

**Brief:** Checkout, blocking failure | Goal: Inform + Interact | User: consumer, anxious about
whether money moved | Constraint: modal, ≤ 2 lines body.

**After**

```
We couldn't confirm the payment with your bank.
You haven't been charged. Try again, or use a different card.

[Try again]  [Use another card]
Details: code 402 · ref 8F2C-41
```

Why: names what happened in the user's terms, resolves the only question that matters at that
moment ("did my money move?"), gives two real actions, and keeps the code where support needs it
but the user does not have to read it. No apology inflation, no personality, no exclamation.

---

## Example 3 — Design system content section (destructive confirmation dialog)

```markdown
## Content

### Purpose
Interrupts the user before an action that cannot be undone or that affects other people.
Not for reversible actions — those use an undo toast.

### Anatomy
| Slot | Required | Max | Rule |
|---|---|---|---|
| Title | yes | 40 | Question naming the action and the object, including count |
| Body | yes | 140 | States what is lost, what survives, and any recovery window |
| Confirm | yes | 20 | Repeats the destructive verb — never "Confirm" or "OK" |
| Dismiss | yes | 20 | Names the safe outcome — never "Cancel" |

### Voice in this component
Plain and unambiguous. No personality, no softening, no euphemism. The user is about to lose
something; clarity outranks warmth.

### Do
- Name the object and the count: *Delete 3 files?*
- State the recovery window if one exists: *Recoverable for 30 days.*
- Name related consequences: shared links, scheduled jobs, team access
- Style the confirm as destructive and keep it the non-default focus

### Don't
- "Are you sure?" — it states no consequence
- "Cancel" as the dismiss label in any dialog that cancels something
- Exclamation marks or apologies
- Use this dialog for reversible actions — it trains dismissal and weakens the real ones

### Example
| | Copy |
|---|---|
| ❌ Before | Are you sure? · [OK] [Cancel] |
| ✅ After | Delete "Q3 report"? · This also removes its shared links. Recoverable from trash for 30 days. · [Delete report] [Keep report] |
| Why | The user learns the blast radius and the recovery window, and both buttons name their outcome. |

### Related terms
`Delete` · `Archive` · `Remove` — see glossary.
```

---

## Example 4 — Explainer article (opening)

**Request:** "Explain why invoice reconciliation sometimes shows unmatched entries."

**Before** (typical first draft)

> ## Background
> Reconciliation is the process by which the system compares entries. Historically, matching was
> performed nightly against the bank feed provided by our integration partner…

**After**

> ## Why some entries don't match
>
> **TL;DR** — We match bank transactions to invoices by amount, date, and reference. If any one of
> those differs — a partial payment, a transfer that landed a day late, a missing reference — the
> entry stays unmatched and waits for you. Nothing is lost. Match it manually from the
> Unmatched tab, and we'll remember that pairing for next time.
>
> ### What matching actually compares
> Three fields, in this order: amount, date (±3 days), payment reference. All three must agree.
>
> ### Why partial payments never auto-match
> A client paying 4 000 PLN against a 5 000 PLN invoice fails the amount check…

Why: the answer, the reassurance, and the action are in the TL;DR; headings are navigable; the
mechanism appears as three named fields rather than a paragraph of prose; the history is gone.
