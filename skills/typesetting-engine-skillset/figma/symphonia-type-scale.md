---
name: symphonia-type-scale
description: Use whenever a Figma file needs a coherent type scale, type ramp, font-size variables, text styles, or a specimen built from selected body text. Read the file first, show every computed size, line-height, and tracking value before writing, preserve existing naming and bindings, and require explicit approval for x-height measurement and each write operation.
---

# Symphonia Type Scale

Build a type scale from selected body text without restyling existing layers.

## Operating contract

- Read first. Report before asking.
- Ask only when a value cannot be read and changes the result. Ask one question at a time.
- Always ask before measuring x-height, creating variables, creating text styles, or creating a specimen.
- Never overwrite or detach an existing style or variable binding without explicit approval.
- Load every font before any text or text-style mutation.

## 1. Resolve the base

- No selection or no text node: ask the user to select body text and stop.
- One text node: read its first styled segment with `getStyledTextSegments(["fontName", "fontSize"])`.
- Several text nodes: list name, family, style, and size; ask which is body text.
- If the node has mixed styles, say that the first segment is the proposed base.
- Confirm the family, style, and base size before computing.

## 2. Choose and compute the scale

Use a ratio the user supplied. Otherwise offer a short relevant choice and default to `1.200` only after saying so.

Geometric size formula:

`size(step) = base × ratio^step`

Show raw values before rounding. Round to the nearest even integer; prefer a multiple of 4 only when it is within about 1 px and does not collapse neighbouring steps. If two steps become equal or the scale collapses into equal arithmetic jumps, use even-integer rounding or propose a wider ratio.

Flag sizes below 12 px. Platform minimums are constraints, not replacement scales.

## 3. Add line-height and tracking

Line-height ranges:

- Body: `1.2–1.45`, sourced from Butterick.
- Heading: `1.1–1.3`, a working range of this skillset.
- Caption/small: `1.2–1.4`, a working range of this skillset.

If x-height ratio `xr` is available:

`t = clamp((xr - 0.447) / (0.545 - 0.447), 0, 1)`

`LH = LH_min + t × (LH_max - LH_min)`

In Figma, measuring `xr` creates a temporary 100 px `x`, flattens it, reads its height, and removes it. Explain that and wait for permission. Without permission, use a labelled family fallback; never call it measured.

Sentence/title-case tracking:

- Below 24 px: `0%`.
- 24–35 px: `-1.5%` sans, `-0.75%` serif.
- 36 px and above: `-2%` sans, `-1%` serif.

All-caps tracking:

`TS = max(3%, min(12%, 160 / FS))`

State the assumed case and weight for each style.

## 4. Show the proposal

Before any write, return a table with token, role, step, raw size, rounded size, line-height ratio and pixels, tracking, and source status. Then inspect `getLocalTextStylesAsync()` and `getLocalVariableCollectionsAsync()` and report name collisions and current conventions.

## 5. Write only what was approved

- Variables: use an approved collection; create `FLOAT` size and line-height variables with `FONT_SIZE` and `LINE_HEIGHT` scopes.
- Text styles: match existing names, load the font, set the rounded values, and bind size and line-height with `TextStyle.setBoundVariable` when approved variables exist.
- Specimen: create one Auto Layout frame away from existing content; each row uses the created text style with no local overrides.
- Do not apply new styles to existing layers.
- Return created names, counts, and node IDs, plus anything skipped.

## About

Part of the Symphonia Typesetting Engine by Monika Zapisek: [project site](https://monikazapisek.com) · [source and documentation](https://github.com/monikazapisek/design-engineering-playbook).

Run `/symphonia-text-typesetting` next to audit the resulting line-height, tracking, and OpenType state.
