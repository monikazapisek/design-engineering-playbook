---
name: symphonia-text-overflow
description: Use whenever user interface cards, list rows, or components in Figma need text-overflow, line-count, character-budget, truncation, clipping, localisation, or larger-text resilience checked. Compare matched sibling layers, label line counts as estimates, verify that full text remains reachable, duplicate before stress testing, never rewrite copy, and ask before every write.
---

# Symphonia Text Overflow

Measure text against its container. Do not shorten, pad, or rewrite the copy.

## Operating contract

- Read and report before asking.
- Ask only for target languages or the full-text destination when the file does not show them.
- Always ask before duplicating frames, replacing stress-test text, changing spacing, resizing, or changing truncation.
- Run destructive stress tests only on a duplicate and remove it after reporting.

## 1. Find comparable text

Use selected frames or sibling instances of the same component. Match text nodes across siblings by layer name and role. Read:

- `characters`, `width`, `height`, `fontSize`, `lineHeight`
- `textAutoResize`, `textTruncation`, `maxLines`
- parent Auto Layout sizing and fixed-height constraints
- text style and variable bindings

## 2. Estimate line counts

Figma does not expose line boxes. For `textAutoResize = "HEIGHT"`, resolve line-height to pixels and estimate:

`lines = round(height / lineHeightPx)`

Label it as an estimate. Report minimum, maximum, most common count, and outliers per text role. Uneven counts are measurements, not rule violations.

## 3. Derive a character budget

`characters per line = characters / estimated lines`

`budget = characters per line × target lines`

Take target lines from the most common sibling value or an explicit design constraint. Return a range and state the font, size, width, and language it depends on.

## 4. Audit truncation and clipping

- `textTruncation = "ENDING"` with `maxLines` means the node may truncate with an ellipsis.
- Legacy `textAutoResize = "TRUNCATE"` is deprecated; report it.
- `textTruncation = "DISABLED"` plus fixed height can clip without an ellipsis; treat that as more serious.
- For every truncated text, name where the full value is reachable: detail view, expand action, or another explicit destination. If none is visible, report `full text not reachable`.
- Flag fixed-height text and fixed-height parents on the text axis.

## 5. Stress test on a duplicate

After approval, duplicate the selected component/frame and test:

- the longest real string already present in the file
- real target-language strings
- WCAG 1.4.12 robustness values: line-height `1.5`, paragraph spacing `2×`, letter spacing `0.12×`, word spacing `0.16×`
- the platform's larger-text setting

These are tests, not recommended design values. Report the first condition causing loss, overlap, or hierarchy failure. Remove the duplicate after the report.

## 6. Apply only approved structural fixes

Offer flexible height (`textAutoResize = "HEIGHT"`) or agreed truncation only when full text remains reachable. Never edit `characters` to force fit. Preserve bindings and return all mutated node IDs.

## About

Part of the Symphonia Typesetting Engine by Monika Zapisek: [project site](https://monikazapisek.com) · [source and documentation](https://github.com/monikazapisek/design-engineering-playbook).

Run `/symphonia-microtypography` next for the final character-level and line-ending pass.
