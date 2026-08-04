# Changelog — ux-content-design

All notable changes to this skill are documented here.
Format follows [Keep a Changelog](https://keepachangelog.com/en/1.1.0/) and semantic versioning.

## v1.1.0 — 2026-08-04

### Register: product copy, not marketing copy

The skill could tell good UI copy from bad UI copy and had nothing separating product copy from
advertising. Under pressure to sound less dull it drifted toward advertising, because that is the
register with the most available devices. Two rejected drafts of its own listing exposed it —
first a feature list, then a tagline. See `EVIDENCE.md`, Run 5.

- **New `references/golden-standards.md`**, loaded before drafting rather than on demand:
  taxonomy of 12 pastiche tells with plain-sentence replacements; the read-aloud gate; 15 golden
  good/bad pairs across errors, empty states, onboarding, buttons, login, sensitive facts, and
  confirmations; product-vs-marketing comparison; few-shot prompt template; iteration loop.
- **New `references/voice-chart.md`**: voice defined by constraints, not adjectives.
  Adjective latching named and countered — mechanical rules over adjectives, tone clusters over
  single words, bounded "this but not that" pairs with bull's-eye logic and the synonym-trap test.
- **`SKILL.md`**: identity changed to "not a copywriter, not selling anything". Read-aloud
  promoted to the first stress-test check — a string that fails it cannot be saved by passing the
  others. Pastiche-tell check and adjective audit added. Brief gained *coming from* /
  *leaving with*. Anti-patterns added for the tagline reflex and marketing register.
- **`references/influence-copy.md`** rewritten: "Influence" now means giving someone what they
  need to choose correctly, including choosing no. Stake-led framing and hooks removed.
- **`references/microcopy-patterns.md`**: inverted pyramid for small screens — first-word action,
  descriptive titles, title-to-CTA continuity, keyword placement, modular blocks.
- **Voice / tone split resolved.** Voice now lives only in `voice-chart.md`, including the
  four-axis rough position that used to sit in `voice-and-tone.md` (kept as an explicit sketch,
  with the warning that axes alone still latch). `voice-and-tone.md` is now tone and bilingual
  register only, and the escalation rule there overrides any personality the chart permits.
- `LISTING.md` and `README.md` rewritten without rhetorical devices.
- `ATTRIBUTION.md`: added the "this but not that" method (Mailchimp's public style guide cited as
  the widely used example), voice chart structure, and the few-shot / adjective-latching sources.

## v1.0.0 — 2026-08-04

### Initial release

- 4-phase procedure: brief (with `ASSUMED:` marking) → three labelled variants with one named
  recommendation → stress-test → ship
- Four output contracts: UI string spec, design system content section, explainer article,
  audit report
- Six reference libraries, loaded on demand: microcopy patterns, error message anatomy, voice
  and tone, design system content guidelines, explainer structure, anti-patterns and dark patterns
- Four complete worked runs in `examples/before-after.md`
- Bilingual PL/EN — native writing, gender-neutral Polish constructions, three plural forms,
  expansion factors, >30 % divergence flagged as a layout risk
- MIT license, full source attribution in `ATTRIBUTION.md`

### Fixes from testing on Claude (see `EVIDENCE.md`)

Three defects found and fixed before release:

- **Cut order missing.** The length check fired but gave no guidance on what to cut first — the
  natural failure mode was trimming the recovery window out of a destructive modal while keeping
  the filler. Phase 3 now carries an explicit cut order and a never-cut list (consequence,
  recovery path, whether money moved, object and count), plus an escape hatch when the frame
  itself is wrong.
- **Response language leaked.** A Polish prompt got an English answer, because nothing separated
  the language of the conversation from the language of the strings. The bilingual section now
  distinguishes them explicitly.
- **Influence goal recorded and never used.** Phase 1 logged `Goal: Influence` and Phase 2 still
  drafted on the UI-string axis, producing feature lists on persuasive surfaces; no Phase 3 check
  asked whether the reader learns what changes for them. Found when a user rejected the skill's
  own listing copy. Added `references/influence-copy.md` (outcome-vs-output ladder, the "so what?"
  test, three framings, specificity over intensity, honesty rules, inverted length rule), a
  goal-based branch in Phase 2, an outcome check in Phase 3, and two anti-patterns.

### Honesty pass

- `compatibility` corrected to **Claude only**. The initial draft copied the repo's convention
  line claiming tests on GPT-5.5, MiniMax-m3, and GitHub Copilot — none of which had been run.
- `EVIDENCE.md` states that testing was a single-model smoke test by the same session that
  authored the skill, not a blind eval against a no-skill baseline.
- Regulatory references (DSA, GDPR, UCPD, FTC) labelled as context, not legal advice.
