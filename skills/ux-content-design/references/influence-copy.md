# Copy That Helps a Decision

Load when the brief says **Goal: Influence** — copy whose job is to help someone choose, rather
than to label a control or report a fact.

Surfaces: onboarding value propositions, empty-state activation, plan comparisons, upgrade
prompts, permission requests, release note headlines, feature announcements.

> **Read `golden-standards.md` first.** This is the reference most likely to pull you toward
> marketing register, and Part 3 of that file is the guardrail.

---

## What "Influence" means here, and what it does not

It does **not** mean persuasion. Inside a product, the reader has already arrived. They are not
deciding whether to trust the brand; they are deciding whether to click one specific thing in the
next four seconds.

**Your job is to give them what they need to choose correctly — including choosing no.**

A person who upgrades because a sentence was clever churns in a month and files a support ticket
first. A person who upgrades because they understood exactly what they were getting stays. Copy
that wins a click by being exciting has moved the problem, not solved it.

So: state what it does, what it costs, what happens if they don't. Then stop.

---

## The failure this reference exists to prevent

Two failures, and they look opposite while coming from the same place.

**Failure 1 — the feature list.** *"Strings with states, character budgets, variables, and plural
rules."* Every word true, nothing said. It is what happens when someone who knows the product
describes the contents, because from the inside the contents feel like the value.

**Failure 2 — the tagline.** *"Your product doesn't have a writing problem."* This is the
overcorrection: reaching for a rhetorical device to fix a boring sentence. It is worse than the
feature list, because the feature list is merely useless while the tagline is useless *and* sounds
like an ad, which costs trust.

The way out is neither. It is a plain sentence about what the reader can now do.

| Feature list | Tagline | What to write |
|---|---|---|
| Automated invoice numbering, PDF export, VAT tables | *"Invoicing, finally handled."* | *"Send an invoice without opening a spreadsheet."* |
| Real-time collaborative editing with CRDT sync | *"Collaboration, reimagined."* | *"Two people can edit the same document at once."* |
| Advanced role-based permission model | *"Security you can trust."* | *"Contractors see only the project they're on."* |
| 200+ integrations | *"Your stack, unified."* | *"Connects to Slack, Notion, and Linear."* |

The third column is duller than the second. That is the point — it is also the only one a reader
can check, and the only one that survives contact with the product.

---

## The "so what?" ladder

Read the sentence, then say *"so what?"* out loud.

*Character budgets* → so what? → *strings fit the button* → so what? → *the Polish version doesn't
overflow in production*.

Stop at the first rung the reader actually cares about. Two failure modes:

- **Stopping too early** leaves a feature list.
- **Going one rung too far** lands in benefit language — *ship with confidence*, *work smarter* —
  which is unfalsifiable and therefore worse than the feature.

The right rung is usually concrete enough to picture and specific enough to be wrong.

---

## Specificity instead of intensity

Weak copy reaches for a stronger adjective. Strong copy reaches for a concrete noun or a number.

| Weak | Strong |
|---|---|
| Dramatically improves your workflow | Cuts the handoff from three rounds to one |
| Powerful error handling | Says whether the payment went through |
| Comprehensive localization support | Flags the Polish string that overflows the button |

One example a reader recognizes from last month beats three superlatives. If you cannot produce
a concrete example, you do not yet understand the value well enough to write the sentence.

---

## Honesty rules

This is where truthfulness fails first, because the incentive runs the other way.

- **No outcome the product doesn't control.** *"Clears review the first time"* is a claim about
  someone else's behaviour.
- **No absolutes** — *always*, *never*, *eliminates*, *guaranteed* — unless literally true and you
  can name the mechanism.
- **Scope limits go next to the claim**, not in a footnote. A limit disclosed up front reads as
  confidence; the same limit found later reads as concealment.
- **Numbers need a source.** No invented percentages, no *10x*, no *saves hours per week*.
- **No manufactured urgency or false scarcity**, ever. If processing takes 30 seconds, say
  30 seconds. See `antipatterns-and-dark-patterns.md`.

---

## Length behaviour

Opposite to UI microcopy. A button gets shorter under pressure; a value proposition gets *vaguer*,
which is worse than being long.

When an Influence string busts its budget, cut **scope**, not **specificity**. One true concrete
thing beats three abstract ones. Dropping the third example is right; replacing three examples
with the word *comprehensive* is the failure.

---

## Checklist

- [ ] Read aloud — a person could say this to another person
- [ ] Zero pastiche tells (`golden-standards.md`, Part 1)
- [ ] "So what?" answerable from the sentence, at the right rung
- [ ] Concrete nouns and numbers, not intensifiers
- [ ] Every claim is one the product actually controls
- [ ] Scope limits stated near the claim
- [ ] The reader has enough to choose **no**, and that path is stated neutrally
- [ ] Nothing here would work as a billboard — if it would, rewrite it
