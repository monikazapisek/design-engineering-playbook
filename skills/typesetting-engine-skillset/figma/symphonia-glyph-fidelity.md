---
name: symphonia-glyph-fidelity
description: Use whenever selected Figma text contains all-caps, small caps, tight tracking, inline acronyms, language-specific characters, or suspected fallback glyphs. Compute one all-caps tracking value, inspect read-only OpenType state and missing fonts, report visual checks separately, and ask before changing any range.
---

# Symphonia Glyph Fidelity

Protect letterforms after case and tracking transforms.

## Operating contract

- Read styled ranges first and report before asking.
- Ask only when a missing decision changes the result.
- Always ask before changing case, tracking, or font size.
- OpenType features are read-only through the Plugin API; report manual actions honestly.

## 1. Read the text

Read per styled range:

- `characters`, `fontName`, `fontSize`, `fontWeight`
- `textCase`, `letterSpacing`, `openTypeFeatures`
- `hasMissingFont`, `textStyleId`, and relevant variable bindings

Load fonts only when a write is approved.

## 2. All-caps tracking

For `UPPER`, `SMALL_CAPS`, or `SMALL_CAPS_FORCED`, compute:

`TS = max(3%, min(12%, 160 / FS))`

Apply the weight modifier after the formula: about `×0.7` at 700+, `×1.15` at 300 or below, and interpolate variable-font `wght`. Return one value per range; do not combine formula and size bands.

## 3. Small caps and ligatures

- Prefer real `SMALL_CAPS`; never silently fake it by shrinking capitals.
- If native small caps are unavailable, explain the limitation and ask whether to simulate or stop.
- When tracking is below `-2%` and the text contains `fi`, `fl`, `ffi`, or `ffl`, read `getRangeOpenTypeFeatures`. If ligatures collide visually, report the range and ask the user to disable `LIGA` in the Type panel. Do not claim to have changed it.

## 4. Inline acronyms

In sentence-case body text, flag runs of three or more capital letters. Propose `+5%` tracking and `-1 px` font size on that subrange only. Do not apply this to all-caps headings or real small caps.

## 5. Missing glyphs

- If `hasMissingFont` is true, report it first and do not trust further visual conclusions.
- Check Polish letters, typographic quotes, en/em dashes, multiplication, currency signs, and every shipping language.
- The Plugin API cannot expose a single glyph borrowed from a fallback font. Inspect a screenshot and label this as a visual check, not an API result.

## 6. Report, then write

Return node/range, current state, formula inputs, recommendation, binding owner, API-readable evidence, and visual-only evidence. After approval, load all fonts and change only the named ranges with range setters; return the mutated node IDs.

## About

Part of the Symphonia Typesetting Engine by Monika Zapisek: [project site](https://monikazapisek.com) · [source and documentation](https://github.com/monikazapisek/design-engineering-playbook).

Run `/symphonia-microtypography` next to correct the actual punctuation and spacing characters.
