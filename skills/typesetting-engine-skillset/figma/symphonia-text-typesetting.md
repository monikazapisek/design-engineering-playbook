---
name: symphonia-text-typesetting
description: Use whenever selected Figma text needs a line-height, tracking, vertical-trim, figure-style, kerning, dash, or hanging-punctuation audit. Read styled ranges, variables, and text styles first; compute one source-labelled recommendation per range; report before asking; and never write until the user explicitly approves the exact changes.
---

# Symphonia Text Typesetting

Audit and, only on approval, correct a selected Figma text node.

## Operating contract

- Read first; ask only for a missing value that changes the result.
- Report every proposed value before a write.
- Ask before x-height measurement and before any node, style, or variable mutation.
- A style or variable owns its value. Do not create a local override unless the user asks for one.
- Load all fonts from `getStyledTextSegments(["fontName"])` before writing.

## 1. Read the selected text

Read per styled range when any property is mixed:

- `fontName`, including `variationSettings`
- `fontSize`, `fontWeight`, `lineHeight`, `letterSpacing`
- `textCase`, `leadingTrim`, `openTypeFeatures`
- `hangingPunctuation`, `textStyleId`, and relevant `boundVariables`

State what came from a style, a variable, or a local value.

## 2. Compute line-height

Ranges:

- Body: `1.2–1.45`, source-backed.
- Heading: `1.1–1.3`, working value.
- Label/caption: `1.2–1.4`, working value.

If measured x-height ratio `xr` exists:

`t = clamp((xr - 0.447) / (0.545 - 0.447), 0, 1)`

`LH = LH_min + t × (LH_max - LH_min)`

Measuring x-height creates, flattens, and removes a temporary layer; ask first. Otherwise use and label a family fallback.

Read `leadingTrim` before finalizing. Do not claim a universal numeric correction for trim; report that the optical result depends on the font metrics and visible glyphs.

## 3. Compute tracking

Branch on `textCase` first.

For `UPPER`, `SMALL_CAPS`, or `SMALL_CAPS_FORCED`:

`TS = max(3%, min(12%, 160 / FS))`

For sentence/title case:

- Below 24 px: `0%`.
- 24–35 px: `-1.5%` sans or `-0.75%` serif.
- 36 px and above: `-2%` sans or `-1%` serif.

Apply the weight modifier after the case/size result: about `×0.7` at 700+, `×1.15` at 300 or below, and interpolate actual variable-font `wght`. If an `opsz` axis is active, reduce the manual correction and say why.

## 4. Audit OpenType and punctuation

- `openTypeFeatures` is read-only. Report explicit `KERN: false`, figure-style needs (`ONUM`, `LNUM`, `TNUM`), `CASE`, or ligature needs as manual Type-panel actions; never report them as applied. If `KERN` is absent, say "not explicitly overridden," not "verified on."
- Do not treat absent keys as false: the object reports explicit deviations from font defaults.
- For a display heading beginning with `"`, `“`, `„`, `«`, or `(`, offer `hangingPunctuation = true` and verify visually after approval. A live Inter probe confirmed those marks; it did not move `—`.
- For dash collisions, propose a local `+3%` range adjustment covering the dash and one adjacent character on each side; apply only after visual confirmation and approval.

## 5. Report, then write

Return a table per styled range: current value, recommended value, source or working-value label, owner (style/variable/local), and writable/manual status. After approval, change only the listed properties and return every mutated node or style ID.

## About

Part of the Symphonia Typesetting Engine by Monika Zapisek: [project site](https://monikazapisek.com) · [source and documentation](https://github.com/monikazapisek/design-engineering-playbook).

Run `/symphonia-glyph-fidelity` next for all-caps, ligature, acronym, and missing-glyph checks; otherwise run `/symphonia-vertical-spacing`.
