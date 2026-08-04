# Design System Content Guidelines

Load when writing the content section of a design system component, a term glossary, or
product-wide writing rules.

## Why content belongs in the design system

A component without content rules ships inconsistently no matter how well its props are typed.
The content section is the part that stops the same button from being called *Save*, *Apply*, and
*Update* in three squads.

Content guidance lives **next to the component**, not in a separate wiki nobody opens.

---

## The component content template

Use this exact shape for every component. Keep it to one screen.

```markdown
## Content

### Purpose
One sentence: what this component communicates and when to reach for it.

### Anatomy
| Slot | Required | Max length | Rule |
|---|---|---|---|
| Title | yes | 40 chars | Sentence case, no period, front-loaded |
| Body | no | 140 chars | One idea, one sentence where possible |
| Primary action | yes | 20 chars | Verb + object, matches the title's promise |
| Secondary action | no | 20 chars | Names the alternative outcome, never "Cancel" in a cancel dialog |

### Voice in this component
Two lines on tone in this specific context, including the moments where personality is banned.

### Do
- Enforceable rule
- Enforceable rule
- Enforceable rule

### Don't
- Named failure with the reason it fails
- Named failure with the reason it fails
- Named failure with the reason it fails

### Example
| | Copy |
|---|---|
| ❌ Before | … |
| ✅ After | … |
| Why | One sentence. |

### Related terms
Link the glossary entries this component depends on.
```

### What makes a Do/Don't rule enforceable

A rule is enforceable when a reviewer can reject a specific draft with it.

| Enforceable | Not enforceable |
|---|---|
| Max 3 words in a primary CTA | Keep CTAs short |
| Never use "Cancel" as the dismiss action in a cancellation dialog | Avoid ambiguity |
| No exclamation marks in error, warning, or confirmation copy | Use a friendly tone |
| Always name the object being deleted, including its count | Be specific |
| Helper text states the rule before validation fires | Help the user succeed |

Write 3–5 per side. More than five and nobody reads them; fewer than three and the component is
under-specified.

---

## The product glossary

The single highest-leverage content artifact. One table, product-wide, owned by the design system.

| Term | Definition | Use for | Never use | Notes |
|---|---|---|---|---|
| Delete | Permanently removes the object | Irreversible removal | Remove, Erase, Destroy | Always paired with a consequence statement |
| Remove | Detaches an object from a container, object survives | Removing a member from a team | Delete | |
| Archive | Hides from default views, fully recoverable | Completed projects | Hide, Close | |
| Workspace | Top-level container for teams and projects | | Organization, Account, Tenant | "Account" means billing entity only |

Rules for maintaining it:

- **One concept, one word.** Every synonym listed under "Never use" is a lint rule waiting to
  be written.
- **Define by user consequence**, not by implementation. If two words map to the same user
  outcome, one of them dies.
- New term = a PR against the glossary, not a Slack message.
- Deprecating a term requires a migration list of every surface using it.
- Internal engineering vocabulary (tenant, entity, payload, job) is banned from user-facing
  strings and can stay in code.

---

## Product-wide content rules

The short list every squad must follow. Keep it under fifteen items or it becomes a document
nobody applies.

**Capitalization** — sentence case for headings, buttons, labels, menu items, tabs. Title Case
only for proper nouns and product names.

**Punctuation** — no period on labels, buttons, single-sentence tooltips, or headings. Periods on
body copy of two or more sentences. Serial comma in EN. No exclamation marks in errors, warnings,
or confirmations; maximum one per screen anywhere.

**Numbers** — digits everywhere in UI. Absolute dates for actionable deadlines, relative for
recency. Explicit currency codes in multi-currency products.

**Terminology** — glossary is binding. Unlisted term = write it, then add it.

**Voice** — the "we are X, not Y" pairs, verbatim, so they are enforceable in review.

**Accessibility** — every control has an accessible name that works read alone; no meaning by
colour or icon alone; error text tied to its field.

**Localization** — no concatenated sentences; semantic variable names; all plural forms defined;
30 % length headroom on constrained surfaces.

---

## Reviewing copy against the system

Use this in design review, not after handoff.

- [ ] Every string maps to a component slot with a length rule
- [ ] Terms match the glossary
- [ ] Capitalization and punctuation follow the product rules
- [ ] All component states are written, not just the mockup's state
- [ ] Variables are named, pluralized, and have fallbacks
- [ ] Both languages present where the product is bilingual, with counts
- [ ] No new term introduced without a glossary entry
- [ ] Dos and Don'ts of the component are satisfied — cite the rule when rejecting

## Governance

- Content rules live in the same repo as the components and version with them.
- A copy change to a shared component is a system change: it needs the same review as a prop
  change, and a migration note.
- Track exceptions explicitly. An undocumented exception becomes precedent within two sprints.
