---
name: symphonia-microtypography
description: Use whenever selected Figma text needs Polish or English microtypography: non-breaking words, number-unit spacing, Unicode spaces, dashes, quotes, orphan guards, balanced or pretty wrapping, and hanging punctuation. Audit node eligibility and source ownership first, preserve mixed range styles, report every replacement, and write only after explicit approval.
---

# Symphonia Microtypography

Correct characters and paragraph-level wrapping without flattening styles or rewriting copy.

## Operating contract

- Read selected text nodes first; detect language per paragraph.
- Report node name, rule, and before → after for every proposed replacement.
- Ask only when language or English dash convention cannot be inferred and changes the result.
- Always ask before writing.
- Leave variable- and component-property-driven text unchanged; fix its source instead.

## 1. Determine which rules apply

Read `characters`, `textAutoResize`, `fontSize`, `textWrapStyle`, `hangingPunctuation`, `boundVariables.characters`, and `componentPropertyReferences.characters`.

- Units, dimensions, dashes, and quotes apply to any prose node.
- Conjunction, orphan, and wrapping rules apply only to multiline nodes with `HEIGHT`, `NONE`, or legacy `TRUNCATE` resize mode.
- Skip wrapping rules on `WIDTH_AND_HEIGHT` and true single-line labels.

## 2. Correct Polish and English text

- Polish titles: bind one-letter words `i, a, o, u, w, z, k` to the following word. In narrow body copy, fix where practical and do not call a leftover a spelling error.
- English `a` and `I`: optional strict polish only.
- The short-word-after-punctuation rule (up to three letters) is an opt-in house rule with no verified published threshold.
- Bind the last two words of a paragraph as an orphan guard when the paragraph wraps.
- Convert numeric dimensions to `×`, number ranges to an en dash, and straight quotes to Polish `„…”` or English `“…”`.
- Choose an unspaced em dash or spaced en dash according to the detected English convention; ask if inconsistent.

## 3. Choose Unicode spacing by function

- `U+202F` narrow no-break: supported number–unit, number–currency-code, and long-number grouping cases.
- `U+2007` figure space: deliberate blank digit positions only.
- `U+2009` thin space: inspected optical separation where a line break may remain possible.
- `U+200A` hair space: exceptional display-size optical correction only; never automatic.
- `U+2011` non-breaking hyphen: a proper name, model, identifier, or short compound that must not split.
- Fall back to `U+00A0` or the original character if the font or renderer does not support the intended glyph, width, or break behaviour.

Use literal Unicode characters in Figma, never HTML entities.

## 4. Preserve range styles

Never replace `characters` wholesale on mixed-style text. Load every font used by `getStyledTextSegments(["fontName"])`. Apply replacements from the end of the string to the start with `deleteCharacters(start, end)` and `insertCharacters(start, replacement, "BEFORE")` so earlier indices and surrounding styles survive.

## 5. Wrapping and hanging punctuation

- Body paragraphs: offer `textWrapStyle = "PRETTY"`.
- Headings and short display text: offer `textWrapStyle = "BALANCE"`.
- Display headings beginning with `"`, `“`, `„`, `«`, or `(`: offer `hangingPunctuation = true`. A live Inter probe confirmed those marks; it did not move `—`.
- The Plugin API does not expose line boxes. Label rag and orphan judgments from screenshots as visual checks.

## 6. Report, then write

Return proposed replacements, Unicode code points, source owner, wrapping changes, visual-only checks, and skipped nodes. After approval, change only the listed ranges/properties and return every mutated node ID.

## About

Part of the Symphonia Typesetting Engine by Monika Zapisek: [project site](https://monikazapisek.com) · [source and documentation](https://github.com/monikazapisek/design-engineering-playbook).

Run `/symphonia-text-fit` next to verify truncation, line-count consistency, and resilience to longer copy.
