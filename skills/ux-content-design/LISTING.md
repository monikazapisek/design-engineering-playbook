# Listing copy

Ready-to-paste marketplace and repo copy.

Written under the skill's own constraint: describe what it does, no rhetorical devices, nothing
that would work as a billboard. Two earlier versions of this file failed — the first listed
features, the second reached for a tagline. Both are recorded in `EVIDENCE.md` because they are
the two failure modes the skill now exists to prevent.

Update this file when scope changes, so the listings never drift from `SKILL.md`.

---

## ClawHub

**Name**

```
ux-content-design
```

**Tagline**

```
A content design procedure for product teams — microcopy, error messages, design system content,
and explainers. Writes every state, not just the one in the mockup.
```

**Short description** (card body)

```
UX writing that doesn't read like it came from an AI. Marketing register is out of scope: the
skill carries a named list of the habits that make machine-written copy recognizable, and a
read-aloud gate that runs before any other check. Fixed 4-phase procedure ending in a string spec
an engineer can paste. Bilingual PL/EN. Claude only.
```

**Full description** (listing page)

```markdown
Most copy defects live in states that never make it into a mockup:

- The empty state reused as the no-results state, so the user thinks their data is gone
- The error that says "something went wrong" without saying whether the payment went through
- The Polish string that overflows the button by four characters
- The third word for one action — Delete, Remove, Erase — because there was no glossary

Review looks at the screen in the mockup, so these ship. This skill writes them.

### It also doesn't write like an AI

That is a design goal, not a side effect. Ask a model for microcopy and you usually get a
pastiche: "Oops! Something went wrong on our end. We're working hard to fix it!" — or the
overcorrected version, which is a tagline with an antithesis in it.

Three mechanisms prevent it:

- **Marketing register is out of scope.** The reader is already inside the product, mid-task.
  Nothing written here should work as a slide title.
- **A named list of pastiche tells** — antithesis, rhetorical question openers, escalating
  triples, fragments for emphasis, em-dash reveals, "unlock / elevate / supercharge". Each one
  means: delete the sentence, state the fact.
- **A read-aloud gate that runs first.** Would a person say this to another person sitting next
  to them? A string that fails cannot be saved by passing the other checks.

Voice is defined by constraints rather than adjectives, because a single adjective has no ceiling
— tell a model "friendly" and it writes a caricature. The voice chart uses bounded pairs
("helpful, but not servile"), countable mechanics (sentences under 15 words), and banned-word
lists.

### The procedure

1. **Brief** — surface, user, emotional state, goal, where they came from, what they leave with.
   Unknowns are marked `ASSUMED:`, never silently guessed.
2. **Draft** — three labelled variants and one named recommendation with a reason. Not three
   options handed back for you to choose between.
3. **Stress-test** — read-aloud, pastiche tells, adjective audit, dark patterns, length budget
   with localization headroom, glossary consistency, accessibility, truthfulness. Failures get
   fixed, not footnoted.
4. **Ship** — a UI string spec, a design system content section, an explainer, or an audit report.

### Bilingual

Writes natively in Polish or English, never translates. Polish gender-neutral constructions,
three plural forms, button imperatives, ~20–30 % expansion from English. Both languages with
character counts; any pair diverging by more than 30 % is flagged as a layout risk before handoff.

### Scope

**Claude only** — built and tested on Claude, not evaluated on any other model. Testing was a
single-model smoke test, not a blind eval against a baseline. Four defects were found and fixed
during it, two of them by users rejecting the skill's own output; `EVIDENCE.md` documents all of
them.

Not for: marketing and campaign copy, ads, conversion landing pages, SEO, pure API reference
docs, or typography.

MIT. No dependencies, no MCP, no network access at runtime.
```

**Tags**

```
ux-writing, content-design, microcopy, design-system, documentation, error-messages,
voice-and-tone, accessibility, localization, product-design, claude
```

**Category**

```
Design / Product
```

---

## GitHub

**Repo description** (≤ 160 chars)

```
Content design skill for Claude: microcopy, error messages, design system content, explainers. Writes every state, and doesn't sound like an AI wrote it.
```

**Topics**

```
claude, claude-code, agent-skills, ux-writing, content-design, microcopy, design-systems,
voice-and-tone, product-design, accessibility
```

---

## Short form

**One sentence**

```
A content design procedure for product teams, with a read-aloud gate that rejects anything that
sounds like an ad.
```

**Three lines**

```
UX writing for product teams: microcopy, errors, design system content, explainers.
Writes the states that never reach the mockup — empty, error, offline, the other language.
Marketing register out of scope by design. Claude only, MIT.
```
