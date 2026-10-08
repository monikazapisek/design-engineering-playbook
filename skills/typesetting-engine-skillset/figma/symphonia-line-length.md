---
name: symphonia-line-length
description: Use whenever a wrapping Figma text block needs its reading measure checked or fixed. Read the selected text node, font, width, resize mode, parent Auto Layout, styles, and variable bindings; estimate characters per line; report desktop and mobile verdicts in pixels; and ask before resizing the text node or its container.
---

# Symphonia Line Length

Audit the reading measure of selected body text. Do not use this skill for headings, labels, buttons, or intentionally single-line strings.

## Operating contract

- Read and report before asking.
- Ask only when a missing value changes the verdict.
- Always ask before resizing any node or changing Auto Layout sizing.
- Preserve style and variable bindings.

## 1. Resolve the target

Require one wrapping body-text node. Read:

- `characters`, `width`, `fontSize`, `fontName`
- `textAutoResize`, `textTruncation`, `maxLines`
- parent `layoutMode`, sizing mode, width, padding, and bound variables

Handle resize modes:

- `HEIGHT` or `NONE`: width is measurable.
- `WIDTH_AND_HEIGHT`: no fixed measure and no wrap; report this before computing a verdict.
- `TRUNCATE`: deprecated fixed-box behaviour; measure the width and flag hidden text. Prefer the current `textTruncation` property for new fixes.

If the text fills an Auto Layout parent, report the effective content width after padding and whether changing the text width would require changing the parent.

## 2. Estimate characters per line

The target ranges are:

- Desktop body text: 45–75 characters, with about 65 as the classic centre.
- Mobile body text: 35–45 characters.

Use rendered line count when it can be estimated from node height and resolved line-height; otherwise estimate from width, font size, and the current text. Label every estimate. Do not convert the result to `ch`; Figma writes pixel widths.

## 3. Report the verdict

Return:

- target node and whether it is eligible body text
- current effective width
- measured or estimated characters per line
- desktop and mobile verdicts
- proposed pixel width and the assumptions used
- parent/layout constraint that must change, if any
- style or variable binding that owns the width or text metrics

If the line is too wide, prefer a fixed-width wrapping text box with `textAutoResize = "HEIGHT"`. If it is too narrow, identify padding or parent constraints before proposing a larger width.

## 4. Apply only after approval

Load the node's fonts. Resize the smallest correct owner: the text node when locally sized, or the parent/variable when it controls the width. Do not replace a binding with a raw value. Return every mutated node ID and the final width.

## About

Part of the Symphonia Typesetting Engine by Monika Zapisek: [project site](https://monikazapisek.com) · [source and documentation](https://github.com/monikazapisek/design-engineering-playbook).

Run `/symphonia-text-typesetting` next because line-height may need compensation after the measure changes.
