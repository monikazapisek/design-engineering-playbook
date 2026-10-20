# The nine principles: definitions, tests, typical violations

Load this file in Step 3, after the task pass is written. Use it twice: to explain each task-pass
obstacle with tests and evidence, then as a full sweep that catches what the task pass missed. Each
principle has an ID, a one-line definition, checkable tests, typical violations in product UI, and
the condition under which it is *Not assessed*. Definitions are paraphrased; full references are in
`report-contract.md`.

Thresholds marked **working value** are practitioner conventions, not research findings. Name them
as such in the report.

---

## GP-PX — Proximity

Elements separated by smaller gaps are read as one group; larger gaps read as boundaries
(Wertheimer 1923).

**Tests**
- PX-1 Inside a group, the gap between related items is smaller than the gap to the next group:
  label → field < field → next label; title → body < body → next section; icon → text < pair → pair.
- PX-2 Equal or reversed gaps fail. A difference too small to notice is Partial (working value:
  outer gap below 1.5× the inner gap).
- PX-3 Helper and error text sit closer to their field than to the next field.
- PX-4 In tables and lists, row gaps and column gaps do not compete: data scans in the intended
  direction.

**Typical violations:** a label equidistant between two inputs; card actions closer to the next
card than to their own; a section heading closer to the previous section than to its content.

**Not assessed:** never; spacing is always visible. Label values *estimated* without Figma data.

## GP-SM — Similarity

Elements sharing colour, size, shape, weight, or texture are read as the same kind of thing, even
when apart (Wertheimer 1923). Colour usually binds more strongly than shape (Quinlan & Wilton 1998).

**Tests**
- SM-1 Elements with the same function share the same appearance: one style per role for primary,
  secondary, and destructive actions, links, status badges, and section headings.
- SM-2 Elements with different functions do not share an appearance: static text does not look like
  a link, decoration does not look like a button, a status badge does not look like a filter chip.
- SM-3 The status or category colour code is used consistently across the screen.
- SM-4 With Figma data: same-role instances use the same component variant and token.
- SM-5 Nothing outside the main task looks like the task's items: comments vs headlines, ads vs
  results, read-only rows vs editable rows. Check across regions, not only within one.
- SM-6 Repeated tiles in one set share one frame treatment: border, radius, and bleed.

**Typical violations:** sidebar comments set in the same type as the headlines beside them; links in
three different styles on one screen; a non-clickable tag styled
as a button; the same colour meaning "warning" in one table and "selected" in another.

**Not assessed:** SM-4 without Figma data.

## GP-CR — Common region

Elements inside a shared boundary, such as a card, filled panel, or bordered box, are read as one
group, and this can override proximity and similarity (Palmer 1992).

**Tests**
- CR-1 Every container encloses one logical group; no related element sits outside its container.
- CR-2 No container encloses two unrelated groups without an inner divider.
- CR-3 The container boundary is visible enough to work: a fill or border distinct from the
  background, or a shadow.
- CR-4 Nesting depth is justified: a card in a card in a panel needs a reason at each level.

**Typical violations:** a form split across two cards with one field orphaned; a toolbar inside a
card that controls the whole page; four levels of nested boxes on a settings screen.

**Not assessed:** never.

## GP-UC — Uniform connectedness

Elements joined by a line, arrow, or shared connected surface are read as one unit, more strongly
than by proximity alone (Palmer & Rock 1994). Keep this separate from common region: a connector
links elements; a region encloses them.

**Tests**
- UC-1 Steppers, timelines, trees, and flow diagrams connect every node that belongs to the
  sequence and no node that does not.
- UC-2 Connectors are unbroken unless a break carries meaning, such as a skipped or blocked step.
- UC-3 Divider lines separate groups; they do not run through a group and cut it in half.

**Typical violations:** a stepper line that stops before the last step; a divider between a label
and its value; a tree whose child lines attach to the wrong parent.

**N/A:** when the screen has no connectors.

## GP-CN — Continuity

The eye follows smooth lines and shared alignment and reads elements on one path as related
(Wertheimer 1923).

**Tests**
- CN-1 Left edges of labels, inputs, and text in one column share an alignment line.
- CN-2 Table columns align numbers and text consistently in each column.
- CN-3 The reading path follows the task order: no backtracking to reach the next step.
- CN-4 Horizontal scroll rows, carousels, and steppers point the eye in the direction of progress.

**Typical violations:** form fields with three different left edges; a primary action placed above
the fields it submits; a stepper running right to left in a left-to-right interface.

**Not assessed:** never.

## GP-CL — Closure

People complete incomplete shapes and infer content that is partly hidden (Koffka 1935).

**Tests**
- CL-1 Content cut at a container edge signals more content: a partly visible card, a fade, or a
  scroll affordance.
- CL-2 Cut content does not look like a rendering error: clipping happens at a clear container edge.
- CL-3 Skeleton or loading states mirror the structure of the content they replace.
- CL-4 Outline and broken-line icons stay recognizable at the size used.

**Typical violations:** a horizontal list cut exactly between two cards, so nothing signals scroll;
a skeleton with a different layout from the loaded screen.

**Not assessed:** CL-3 without a loading-state capture. **N/A:** CL-4 when the screen has no
outline or broken-line icons.

## GP-FG — Figure/ground

The visual system splits a scene into a figure that has shape and is in front and a ground that
continues behind it (Rubin 1915; Wagemans et al. 2012).

**Tests**
- FG-1 One region is the clear figure for the current task: the active modal, panel, or primary
  action.
- FG-2 Modal and popover layers separate from the page behind: scrim, elevation, or both.
- FG-3 Text and controls sit on a ground that does not compete: no busy image or pattern under text
  without a solid or blurred backing.
- FG-4 Several elements do not compete as the figure at the same level of emphasis.

**Typical violations:** a modal with no scrim that blends into the page; two filled buttons of equal
weight; a coloured banner louder than the content it introduces.

**N/A:** FG-2 when no overlay is shown.

## GP-CF — Common fate

Elements that change together, by moving, appearing, or changing state at the same time, are read
as one group (Wertheimer 1923; Wagemans et al. 2012).

**Tests**
- CF-1 Selecting an item changes all of its parts together: row, checkbox, and actions.
- CF-2 Bulk selection marks every selected item the same way, and the bulk-action bar appears
  attached to them.
- CF-3 Expanding, collapsing, and dragging move the whole group, not part of it.
- CF-4 Live updates such as status changes or counters animate only what changed.

**Typical violations:** a selected row highlights while its action buttons stay unchanged; drag
handles that move the label but not the attached metadata.

**Not assessed:** whenever motion or state change is not captured. CF-1 and CF-2 can be scored from
a screenshot of the selected state; CF-3 and CF-4 need a prototype or video.

## GP-PR — Prägnanz

People prefer the simplest, most stable organization the image allows; a layout with one clear
reading is processed faster than one that needs interpretation (Koffka 1935; Wagemans et al. 2012).
Symmetry is one way to achieve this, not a requirement.

**Tests**
- PR-1 The screen resolves into a small number of top-level regions, which can be named in one
  sentence.
- PR-2 One visual hierarchy: a single dominant heading level, a consistent type scale, no competing
  focal points.
- PR-3 Repeated items use one consistent pattern.
- PR-4 Decoration that carries no information is minimal.
- PR-5 Balance: asymmetric layouts pass when weight is distributed deliberately.

**Typical violations:** a dashboard with eight equally loud widgets; four font weights in one card;
tables, cards, and lists mixed for the same kind of data.

**Not assessed:** never.
