---
name: symphonia-vertical-spacing
description: Use whenever selected Figma frames need vertical rhythm, Auto Layout gaps, padding, paragraph spacing, or list spacing audited against a grid and the Gestalt proximity rule. Read bindings and text trim first, compare groups from the inside out, report exact owners and proposed values, and require explicit approval before every write.
---

# Symphonia Vertical Spacing

Audit a selected frame and its text rhythm without replacing design-token bindings with raw numbers.

## Operating contract

- Read first and report before asking.
- Infer the grid from existing spacing values or variables; ask whether it is 4 px or 8 px only when the file does not show it.
- Always ask before changing a frame, text node, style, or variable.
- Do not invent an optical-gap estimate when vertical trim is off.

## 1. Read the spacing context

For the selected frame, read:

- `layoutMode`, `itemSpacing`, and all padding values
- bound variables for gap and padding
- child hierarchy and semantic names
- each child text node's `leadingTrim`, `lineHeight`, `paragraphSpacing`, `paragraphIndent`, and `listSpacing`

If `layoutMode` is `NONE`, report that Auto Layout gap rules do not apply and stop before suggesting `itemSpacing`.

## 2. Audit grid alignment

Flag raw spacing values that are not multiples of the confirmed grid. When a value is variable-bound, name the binding and propose the nearest suitable existing variable; never replace it with a raw number.

## 3. Audit grouping from the inside out

Internal spacing must not exceed the spacing around the group. Compare:

- title to description versus one group to the next
- label to field versus one field group to the next
- field to helper/error versus label to field
- list item to item versus list to surrounding content
- icon to label versus one icon-label pair to the next
- heading to introduced text versus heading to preceding content

Flag reversed groupings and equal gaps that make hierarchy ambiguous. The sources provide the proximity principle, not a universal ratio. If using a 2–3× heading ratio, label it as a working value.

## 4. Account for text metrics

When `leadingTrim` is `NONE`, the configured gap includes font-internal leading and the visible gap may be smaller. Do not claim an exact correction without a rendered measurement. Offer either visual measurement or `leadingTrim = "CAP_HEIGHT"`, and ask before applying it.

For native text rhythm:

- paragraph spacing: `0.50–0.75 × body line-height`
- list-item spacing: `0.25–0.33 × body line-height`
- list block to surrounding paragraph: same range as paragraph spacing

Show formulas and resolved pixels. If the grid and formula conflict, state which constraint wins.

## 5. Report, then write

Return each finding with current value, proposed value, grid status, group meaning, owner (variable/frame/text), and source or working-value label. After approval, mutate only the agreed owners and return all IDs.

## About

Part of the Symphonia Typesetting Engine by Monika Zapisek: [project site](https://monikazapisek.com) · [source and documentation](https://github.com/monikazapisek/design-engineering-playbook).

Run `/symphonia-microtypography` next for character-level spacing, wrapping, and punctuation.
