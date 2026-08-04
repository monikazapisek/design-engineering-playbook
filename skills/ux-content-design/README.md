# ux-content-design

A **Claude Agent Skill** for content design in product teams: UI microcopy, error and system
messages, design system content guidelines, and explainers for complex product problems.

[![License: MIT](./LICENSE)](./LICENSE)

This is the GitHub-facing landing page. The agent-facing working document is
[`SKILL.md`](./SKILL.md) — full procedure, output contracts, failure handling, and quality checklist.

## What it's for

Most copy defects live in states that never make it into the mockup:

- The empty state reused as the no-results state, so the user thinks their data is gone
- The error that says *something went wrong* without saying whether the payment went through
- The Polish string that overflows the button by four characters, found by a customer screenshot
- The third word for the same action — *Delete*, *Remove*, *Erase* — because there was no glossary

Review usually looks at the screen in the mockup, so these get through. The skill writes them,
in a fixed order, and hands back one recommendation rather than three options to choose between.

It also has a specific job you may care about if you have asked an AI for copy before: **it does
not write like an AI.** Marketing register is out of scope by design, and the procedure carries a
named list of the rhetorical habits that make machine-written copy recognizable — antithesis,
escalating triples, fragments for emphasis, *unlock / elevate / supercharge* — with a read-aloud
gate that has to pass before anything else is checked. Details in
[`references/golden-standards.md`](./references/golden-standards.md).

## The procedure

1. **Brief** — surface, user, emotional state, goal (Inform / Influence / Interact), constraints.
   Unknowns are marked `ASSUMED:`, never silently guessed.
2. **Draft** — three labelled variants and one **named recommendation with a reason**. The axis
   depends on the goal: Direct / Guided / Character for UI strings, problem-led / outcome-led /
   stake-led when the job is to move a decision.
3. **Stress-test** — what/why/next, context-free CTA, dark pattern check, length budget with
   localization headroom, glossary consistency, accessibility, truthfulness, read-aloud. Failures
   get fixed, not footnoted. When a string busts its budget there is a defined cut order — and a
   never-cut list: the consequence, the recovery path, whether money moved, the object and count.
4. **Ship** — as a UI string spec, a design system content section, an explainer article, or an
   audit report.

### Core stance

- **Copy is interface, not decoration.** A label is a control. If the words fail, the component fails.
- **Shortest version that still leaves the user in control.** Cut words, never cut the answer to
  "what happens if I click this?"
- **Every message answers what happened, why, and what next.** No third part = not finished.
- **Personality is a budget spent in calm moments.** Zero on payments, security, and data loss —
  the skill writes "variant C not appropriate here" and says why.
- **One concept, one word, forever.** *Delete* / *Remove* / *Erase* for the same action is a bug.
- **Never make the user feel stupid, guilty, or trapped.** Ten dark patterns get declined in one
  sentence, with the honest alternative delivered in their place.

## When to use

- Naming a button, label, tooltip, placeholder, helper text, or menu item
- Errors, empty states, loading, success, permission prompts, destructive confirmations
- Onboarding, paywall, cancellation, and downgrade flows
- Voice & tone definition, or the content section of a design system component
- Help-center articles and explainers for complex product concepts
- Auditing existing copy for jargon, inconsistency, or dark patterns
- Bilingual PL/EN work, including length budgeting against a fixed frame

Triggers: "microcopy", "UX writing", "content design", "copy for this screen", "write the error
message", "voice and tone", "content guidelines", "explain this to users".

## When NOT to use

- Sales and campaign copy, ads, conversion landing pages
- Pure API reference docs with no end-user UI surface
- SEO keyword strategy
- Visual and typographic decisions — that is the `typesetting-engine-skillset`

## Bilingual by design

Writes natively in Polish or English — never translates. Handles Polish gender-neutral
constructions, the three plural forms, imperative conventions on buttons, and the ~20–30 % length
expansion from English. Delivers both languages side by side with character counts, and flags
every pair diverging by more than 30 % as a layout risk before handoff.

## Structure

```
ux-content-design/
├── SKILL.md                                   # Agent-facing working document (required)
├── README.md                                  # This file (GitHub landing page)
├── EVIDENCE.md                                # What was tested, what was not, defects found and fixed
├── LISTING.md                                 # Marketplace and repo copy, written by the skill itself
├── ATTRIBUTION.md                             # Source citations and license chain
├── CHANGELOG.md                               # Release history
├── LICENSE                                    # MIT
├── references/
│   ├── golden-standards.md                    # Loaded before drafting: 12 pastiche tells, read-aloud gate, 15 good/bad pairs, product vs marketing, few-shot template, iteration loop
│   ├── voice-chart.md                         # The single home for voice: adjective latching, tone clusters, "this but not that" with bull's-eye logic, full constraint chart
│   ├── microcopy-patterns.md                  # Inverted pyramid on small screens, buttons, labels, empty states, modals, toasts, onboarding, permissions, cancellation, numbers & variables
│   ├── error-message-anatomy.md               # 3-part contract, severity ladder, fault assignment, validation, payment & security, codes, offline, retries
│   ├── voice-and-tone.md                      # Tone map by emotional state, escalation rule, register by expertise, bilingual PL/EN rules and expansion factors
│   ├── influence-copy.md                      # Outcome vs output, the "so what?" test, three framings, specificity over intensity, honesty rules for claims
│   ├── design-system-content-guidelines.md    # Component content template, enforceable Dos & Don'ts, product glossary, governance
│   ├── explainer-article-structure.md         # Inverted pyramid, scannability, explaining complexity, writing for domain experts
│   └── antipatterns-and-dark-patterns.md      # 10 dark patterns with honest alternatives, 17 craft anti-patterns, audit procedure
└── examples/
    └── before-after.md                        # 4 complete runs: string spec, error message, design system section, explainer opening
```

`golden-standards.md` loads on every run. The rest load on demand, one at a time.

## Compatibility — Claude only

**Built for and tested on Claude** (Claude Code, claude.ai, Claude Desktop). Not evaluated on GPT,
Gemini, Copilot, or any local model. The procedure leans on Claude's instruction-following and its
handling of long on-demand references; it may degrade elsewhere, and that is untested rather than
denied.

Testing was a **single-model smoke test**, not a blind eval against a no-skill baseline. Three real
defects were found and fixed during it — including one found by a user rejecting the skill's own
listing copy, which exposed a structural gap: the brief recorded the goal and nothing downstream
used it. Full disclosure of what was and was not verified is in [`EVIDENCE.md`](./EVIDENCE.md).

No dependencies, no MCP, no network access at runtime.

## Composes with

- **`legible-agent-output`** — the same plain-language law applied to strings emitted by AI agents.
  Use that one when the writer is a machine; this one when the writer is a product team.
- **`typesetting-engine-skillset`** — once the string exists, line length, spacing, and glyph
  fidelity are that family's job.
- **`socratic-dialogue`** — when a stakeholder's copy claim needs testing rather than accommodating.
- **`kano-model-strategist`** — when "the copy is confusing" is really "the feature should not exist".

## Sources

Built on the NN/g 3 C's (Clarity, Concision, Character) and 3 I's (Inform, Influence, Interact),
Torrey Podmajersky's *Strategic Writing for UX*, Yael Ben-David's *The Fundamentals of UX Writing*,
Fenton & Lee's *Nicely Said*, Nielsen's error-recovery heuristic, and Harry Brignull's dark
patterns taxonomy. All wording, tables, and examples are original — no text is reproduced from any
book, article, or vendor style guide. Full citations in [`ATTRIBUTION.md`](./ATTRIBUTION.md).

Regulatory mentions (DSA, GDPR, UCPD, FTC negative option guidance) are context for why certain
patterns are treated as defects. **Not legal advice.**

## License

MIT — see [`LICENSE`](./LICENSE). Author: **[Monika Zapisek](https://monikazapisek.com)**.
Project: **Design Engineering Playbook**.

---

*Part of the [Design Engineering Playbook](https://github.com/monikazapisekstudio/design-engineering-playbook) — AI-assisted workflow artefacts for product designers working in agile and lean environments.*
