# Figma Community listing copy

Ready-to-paste copy for seven separate, free Figma skills. Update this file whenever the standalone files in
`figma/` change.

## Content brief

Surface: Figma Community skill listing | Goal: Influence  
User: product and visual designers working on selected Figma text | Emotion: neutral, evaluating fit  
Coming from: Community search, a shared link, or the Symphonia skillset documentation  
Leaving with: a clear choice of one narrow typography audit and an accurate expectation of what it may change  
Constraint: separate listing per skill; English; no paid claims; no promise of automatic multi-skill chaining

## Positioning options

| Variant | Positioning | Assessment |
|---|---|---|
| A — Direct | State the exact audit and its write boundary | Clearest in search results |
| B — Guided | Explain the audit order and ownership safeguards | Useful in full descriptions |
| C — Character | Lead with the Symphonia name and typographic craft | Rejected: brand-first wording hides the task |

**Recommendation: A — Direct**, with one Guided sentence in each description explaining report-first behavior
and style or variable ownership.

## Shared publishing fields

- Creator: Monika Zapisek
- Price: Free
- Support website: https://monikazapisek.com
- Source and documentation: https://github.com/monikazapisek/design-engineering-playbook
- Community images: one 1920 × 1080 cover and up to nine 1920 × 1080 examples per skill
- Contributors: none unless added before publication
- License checkpoint: GitHub source is MIT. Figma currently presents Community resources under its Community
  Free Resource License; confirm acceptance for each skill before publishing.
- Test disclosure: `symphonia-text-typesetting` passed live invocation, ownership, repeatability, and pre-write
  consent tests. The other six passed Plugin API and static validation but were not run in the Figma agent.

---

## symphonia-type-scale

**Name**

```text
symphonia-type-scale
```

**Tagline**

```text
Build a Figma type scale with sizes, line heights, tracking, text styles, and variables shown before anything is created.
```

**Description**

```text
Start from selected text or a stated base size. The skill proposes a rounded scale, flags collisions, and shows the resulting sizes, line heights, and tracking in a table. It checks existing local styles and variables before asking whether to create or update anything.
```

**Category:** Design systems

**Cover text**

```text
Build the type scale before creating the styles.
```

---

## symphonia-text-typesetting

**Name**

```text
symphonia-text-typesetting
```

**Tagline**

```text
Audit line height, tracking, kerning state, vertical trim, and hanging punctuation on selected Figma text.
```

**Description**

```text
Read styled ranges, text styles, and variables before recommending a change. The skill labels measured values, source-backed ranges, working values, and family fallbacks separately. It reports first, preserves ownership, and asks before writing an exact correction.
```

**Category:** Critique

**Cover text**

```text
See what owns each typography value before changing it.
```

---

## symphonia-line-length

**Name**

```text
symphonia-line-length
```

**Tagline**

```text
Check whether selected body text is too narrow or too wide without confusing pixels with characters per line.
```

**Description**

```text
Audit effective content width, wrapping mode, estimated characters per line, and Auto Layout ownership. The skill distinguishes fixed text width from a parent-controlled fill width, reports the constraint that must change, and asks before resizing a node or its parent.
```

**Category:** Critique

**Cover text**

```text
Find the constraint behind an unreadable text measure.
```

---

## symphonia-vertical-spacing

**Name**

```text
symphonia-vertical-spacing
```

**Tagline**

```text
Audit paragraph rhythm, list spacing, padding, and Auto Layout gaps while preserving variables and text styles.
```

**Description**

```text
Inspect the selected section as a hierarchy, not as isolated gaps. The skill reads paragraph and list spacing alongside Auto Layout padding and item spacing, identifies the value owner, and separates hierarchy problems from numeric spacing problems before asking to write.
```

**Category:** Critique

**Cover text**

```text
Check the rhythm and the hierarchy behind each gap.
```

---

## symphonia-glyph-fidelity

**Name**

```text
symphonia-glyph-fidelity
```

**Tagline**

```text
Check all-caps tracking, acronyms, language-specific glyphs, missing fonts, and read-only OpenType state.
```

**Description**

```text
Audit selected text for all-caps spacing, false small caps, fallback glyphs, and local acronym treatment. The skill uses one size-based tracking formula, reports OpenType features as manual Type-panel actions, and does not replace a missing glyph with an unverified font.
```

**Category:** Critique

**Cover text**

```text
Check the glyphs and spacing that survive at display size.
```

---

## symphonia-microtypography

**Name**

```text
symphonia-microtypography
```

**Tagline**

```text
Audit Polish or English spacing, dashes, quotes, wrapping, orphan risks, and hanging punctuation in Figma text.
```

**Description**

```text
Review selected prose without rewriting it. The skill reports each Unicode replacement, preserves mixed range styles, skips copy owned by variables or component properties, and treats the three-letter post-punctuation rule as an optional house rule rather than a published standard.
```

**Category:** Workflows

**Cover text**

```text
Fix the characters without flattening the text styles.
```

---

## symphonia-text-fit

**Name**

```text
symphonia-text-fit
```

**Tagline**

```text
Stress-test selected UI components with longer copy before text clips, truncates, or breaks the layout.
```

**Description**

```text
Inspect text in user interface components: resizing, visible height, estimated line count, truncation, and parent constraints. The skill proposes realistic stress-copy cases without shrinking the font as a default fix, then asks before duplicating frames, replacing content, or changing layout values.
```

**Category:** Critique

**Cover text**

```text
Find the copy length that breaks the component.
```

## Stress-test summary

- Read-aloud: all strings are plain task descriptions; no slogan structures or rhetorical questions.
- Outcome: each tagline states what the user can inspect or prevent, not a list of internal features alone.
- Truthfulness: no adoption, time-saving, quality, or compatibility claims without evidence.
- Scope: report-first behavior and ownership limits are stated where they affect the decision.
- Consistency: all names use the Figma-only `symphonia-` prefix; GitHub skill names remain unchanged.
- Test status: disclosed in the shared fields instead of implying that all seven passed the same live evaluation.
