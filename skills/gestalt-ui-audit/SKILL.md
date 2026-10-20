---
name: gestalt-ui-audit
description: |
  Audit one interface screen against nine Gestalt grouping and figure/ground principles: proximity,
  similarity, common region, uniform connectedness, continuity, closure, figure/ground, common fate,
  and Prägnanz. Starts with a task-first look at the whole screen, then explains and extends it with
  testable principles, compares the groups people see with the structure the screen intends, and
  ranks layout fixes. Use when asked for a "Gestalt audit", "gestalt review", "visual grouping
  check", "why does this layout feel cluttered", "is the hierarchy clear", or "check proximity and
  similarity". Do NOT use for copywriting, WCAG compliance, conversion or ROI audits, exact spacing
  values against a grid, or code review without a rendered screen.
license: MIT
compatibility: |
  Designed for Claude Code, Claude.ai, and Cowork. Requires an image-capable model.
  No MCP required. Optional: Figma MCP, used only to read measured spacing, fills, strokes, and
  component variants when the user supplies a Figma link.
metadata:
  author: Monika Zapisek
  project: Design Engineering Playbook
  version: "1.0"
---

# Gestalt UI Audit

Judge whether a screen's visual structure supports the user's task. Look first, as the user would;
check second, with the principles. The principles explain and extend what the look finds; they never
replace it. Taste is out of scope.

## When to use

One screen, frame, or state per run: dashboards, forms, tables, settings, detail pages, modals,
mobile screens. Hand off instead of stretching the audit:

| Request | Route to |
|---|---|
| Exact spacing values, grid alignment, text rhythm | A vertical-spacing audit |
| Conversion, business impact, ROI | `ui-roi-audit` |
| Microcopy, labels, error wording | A content-design workflow |
| Contrast ratios, colour-only meaning (WCAG 1.4.1, 1.4.3) | An accessibility audit |
| Counts, filters, or data that contradict each other | Functional QA |

## Load on demand

| Step | Load |
|---|---|
| Step 2 | Nothing. Do the task pass before reading any reference. |
| Step 3 | `references/principles.md` and `references/report-contract.md` |
| Step 4, when two principles disagree | `references/principle-conflicts.md` |
| A format example is needed (optional) | `examples/sample-audit.md` |

## Required inputs

1. **Screen:** a screenshot, or a Figma link to one frame (adds measurements).
2. **Main task:** what the user does on this screen. If missing, infer it, say so, and continue.
3. **Optional:** intended structure, other states (hover, selected, loading, error), prototype link.

Ask only when the screen is missing or too small to read element boundaries.

## Procedure

### 1. Frame

State the screen, image size (device or scale only if given), main task, source of the intended
structure (supplied or inferred from headings and labels), measurement mode (*measured* from Figma
or *estimated* from pixels), and observed states. Where the intended structure is ambiguous, keep
both readings and carry them into conditional fixes. Edges cut by the capture are not UI clipping.

**Output:** audit frame.

### 2. Task pass: look before you check

Look at the whole screen as the user doing the main task. Do not load any reference yet.

- Where does the eye land first, second, third? Is the task's area among them?
- What competes with the task's items, anywhere on the screen? Look across regions: a comment
  styled like a headline or an alert styled like a table row competes from far away.
- Where would the user hesitate, misread which element belongs to which, or act on the wrong thing?
- Could the user believe the task is done while part of it is out of view: on another page, behind
  a filter or range, or in another region?

Write the 3–5 biggest obstacles in plain words, without principle IDs. Keep every obstacle, even one
you cannot yet name.

**Output:** task-pass list (T1, T2, ...).

### 3. Explain, then extend

Load `references/principles.md` and `references/report-contract.md`.

1. **Explain:** for each task-pass obstacle, find the tests that explain it and the screen evidence.
   An obstacle no principle explains stays in the ranking, marked *outside Gestalt*, with the
   workflow to hand it to.
2. **Extend:** build the grouping map (perceived vs intended groups, mismatches) and run every test
   in the principle file. Each new problem becomes a finding marked *from tests*.

**Output:** explained obstacles, grouping map, principle matrix.

### 4. Resolve conflicts

Where two principles point to different groupings, load `references/principle-conflicts.md`,
predict which cue wins on this screen, and check the result against the intended structure.

**Output:** conflict list.

### 5. Rank and report

Rate every finding by severity and effort using the report contract, then rank it: by severity,
regardless of whether it came from the task pass or the tests. Write the report in the contract's
order: findings and fixes first, evidence after.

**Output:** report.

## Failure handling

| Situation | Action |
|---|---|
| Several screens supplied | Audit the one tied to the main task; list the others for later runs |
| Image too small or cropped | Ask for a full-resolution capture of one screen |
| Dynamic behaviour asked from a static image | Score what is visible; mark the rest *Not assessed* and name the state to capture |
| User wants a redesign | Finish the audit, then offer layout options as a separate step |
| Brand or design-system rule blocks a fix | Record the constraint next to the finding |

## Quality checklist

- [ ] The task pass was written before any reference was loaded, and every obstacle is in the report.
- [ ] Every finding has screen evidence, a severity, and either test IDs or the *outside Gestalt* mark.
- [ ] Look-alikes across regions were checked against the task's items.
- [ ] Pixel values are labelled *measured* or *estimated*; working thresholds are labelled.
- [ ] Unobservable tests are *Not assessed*, absent subjects *N/A*; neither is Fail.
- [ ] The report keeps what passed, so a redesign preserves it.
