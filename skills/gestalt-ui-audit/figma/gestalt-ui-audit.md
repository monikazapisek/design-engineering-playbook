---
name: gestalt-ui-audit
description: Use whenever a selected Figma frame needs a Gestalt audit, a visual grouping or hierarchy check, or an answer to "why does this layout feel cluttered". Look at the frame as the user doing its main task first, then read the layers, compare the groups people will see with the structure the frame intends, score proximity, similarity, common region, uniform connectedness, continuity, closure, figure/ground, common fate, and Prägnanz, and rank layout fixes. Report only; ask before adding comments.
---

# Gestalt UI Audit

Judge whether the selected frame's visual structure supports the user's task. Look first, as the
user would; check second, with the principles. The principles explain and extend what the look
finds; they never replace it. A finding needs layer evidence and either a test ID or the *outside
Gestalt* mark. Taste is out of scope.

## Operating contract

- Read the selection and report before asking anything else.
- Never change layers. Adding comments on the canvas requires explicit approval.
- Do not set exact spacing values, write copy, or audit WCAG compliance; name the follow-up instead.
- Thresholds marked *working value* are conventions, not research findings. Say so in the report.
- Never score a state that is not in the file. Mark it *Not assessed*.

## 1. Frame the audit

Require one selected top-level frame: one screen or state per run. If several are selected, audit
the first and list the others for later runs.

State: frame name and node ID, width, purpose (ask only if the frame does not show it; otherwise
infer and say so), intended structure (from layer names, headings, and labels, unless the user gives
it), and states available as separate frames or prototype links. Where the intended structure is
ambiguous, keep both readings and give a conditional fix.

## 2. Task pass: look before you check

Look at the frame as rendered, the whole frame at once, as the user doing the main task. Do not read
layer properties or the principle list yet.

- Where does the eye land first, second, third? Is the task's area among them?
- What competes with the task's items, anywhere in the frame? Look across regions: a comment styled
  like a headline or an alert styled like a table row competes from far away.
- Where would the user hesitate, misread which element belongs to which, or act on the wrong thing?
- Could the user believe the task is done while part of it is out of view: on another page, behind
  a filter or range, or in another region?

Write the 3–5 biggest obstacles in plain words (T1, T2, ...), without principle IDs. Keep every
obstacle, even one you cannot yet name.

## 3. Read the layers

Read visible layers only (`visible !== false`), top to bottom, then left to right. Record:

- **Position and size:** `absoluteBoundingBox`, to measure gaps between siblings
- **Auto Layout:** `layoutMode`, `itemSpacing`, `counterAxisSpacing`, padding values, and any
  `boundVariables` on them
- **Containers:** frames with a visible fill, stroke, or drop shadow (`fills`, `strokes`,
  `strokeWeight`, `effects`, `cornerRadius`)
- **Connectors:** lines, vectors, and thin rectangles joining other elements
- **Text:** `characters`, `fontSize`, `fontName`, `fills`, `textStyleId`
- **Instances:** main component name and variant properties
- **Clipping:** `clipsContent` and `overflowDirection` on frames whose children extend past the edge
- **Interaction:** prototype `reactions` and transition types, for common fate

Gaps measured from bounding boxes are *measured*. When a text layer has no vertical trim, note that
the visible gap is smaller than the measured one.

## 4. Explain, then extend

**Explain:** for each task-pass obstacle, find the tests below that explain it and the layer
evidence. An obstacle no principle explains stays in the ranking, marked *outside Gestalt*, with the
workflow to hand it to.

**Extend:** build the grouping map and score all nine principles. Each new problem becomes a finding
marked *from tests*.

### Grouping map

Build the perceived grouping. Start from the usual order of binding strength (enclosure in a
container, explicit connection, spacing gaps, shared colour, shared size or shape), then adjust for
how strong each cue is in this frame: a large gap can beat a faint container. List perceived groups
(P1, P2, ...) and intended groups (I1, I2, ...), compare them, and name each mismatch:

- **False group:** elements look related but are not
- **Split group:** related elements look separate
- **Wrong owner:** a label, helper, or action attaches to the wrong group
- **Flat hierarchy:** groups exist but none dominates
- **Wrong figure:** a region outside the main task dominates the region where the task happens

Then sweep across regions: does anything outside the main task share the size, colour, type, or
shape of the task's items? A look-alike elsewhere is a false group even when far away.

### Principle scores

Score each Pass, Partial, Fail, Not assessed (evidence missing: a state, motion, or measurement), or
N/A (subject absent: no connectors, overlay, or icons). A principle takes its worst test's score
when a failed test causes a mismatch on the main task's path or several tests fail; Partial for
isolated local breaks or when a stronger cue repairs the grouping, naming that cue. Single tests can
be N/A. One issue is one finding
with every test ID it fails. Every Partial and Fail cites layer evidence.

**Proximity** (Wertheimer 1923)
- PX-1 Gap inside a group is smaller than the gap to the next group (label → field < field → next
  label; icon → text < pair → pair)
- PX-2 Equal or reversed gaps fail; outer gap below 1.5× inner is Partial (working value)
- PX-3 Helper and error text closer to their field than to the next one
- PX-4 Row and column gaps in tables do not compete

**Similarity** (Wertheimer 1923; Quinlan & Wilton 1998)
- SM-1 Same function, same component variant, style, and token
- SM-2 Different functions do not share a look (status vs button, static text vs link)
- SM-3 Colour codes mean the same thing everywhere in the frame
- SM-4 Same-role instances use the same variant and bound variables
- SM-5 Nothing outside the main task looks like the task's items (comments vs headlines, ads vs
  results); check across regions
- SM-6 Repeated tiles in one set share one frame treatment

**Common region** (Palmer 1992)
- CR-1 Each container holds one logical group; nothing related sits outside it
- CR-2 No container mixes unrelated groups without an inner divider
- CR-3 Container fill, stroke, or shadow is distinct from its parent's fill
- CR-4 Each nesting level has a reason

**Uniform connectedness** (Palmer & Rock 1994)
- UC-1 Steppers, timelines, and trees connect every member and no outsider
- UC-2 Connectors are unbroken unless the break carries meaning
- UC-3 Dividers separate groups and never cut one in half

**Continuity** (Wertheimer 1923)
- CN-1 Left edges in one column share an x position
- CN-2 Table columns align their contents consistently
- CN-3 Reading order follows task order; submit comes after the fields it submits
- CN-4 Scroll rows and steppers point in the direction of progress

**Closure** (Koffka 1935)
- CL-1 Content cut at a clipped edge shows enough of the next item to signal more
- CL-2 The cut happens at a clear container edge, not mid-gap
- CL-3 Skeleton frames match the loaded layout (only if a loading frame exists)
- CL-4 Outline icons stay recognizable at their size

**Figure/ground** (Rubin 1915; Wagemans et al. 2012)
- FG-1 One clear figure for the task
- FG-2 Overlays separate from the page with a scrim or elevation (only if an overlay exists)
- FG-3 Text sits on a calm ground
- FG-4 No two elements compete at the top emphasis level

**Common fate** (Wertheimer 1923)
- CF-1 A selected-state frame changes every part of the selected item together
- CF-2 Bulk selection marks every item the same way; the bulk bar attaches to them
- CF-3, CF-4 Expand, drag, and live updates move whole groups: score only from prototype
  transitions; otherwise Not assessed

**Prägnanz** (Koffka 1935; Wagemans et al. 2012)
- PR-1 A few top-level regions, nameable in one sentence
- PR-2 One type hierarchy, no competing focal points
- PR-3 Repeated items follow one pattern
- PR-4 Minimal decoration that carries no information
- PR-5 Balance; asymmetry passes when deliberate. Symmetry is never required.

## 5. Resolve conflicts

Cue strength decides; there is no fixed ranking (Quinlan & Wilton 1998; Wagemans et al. 2012).
Default predictions, to check against the frame:

- A visible container usually beats proximity (Palmer 1992)
- A connecting line usually beats proximity and similarity (Palmer & Rock 1994)
- Strong colour can beat a small gap; shape rarely does (Quinlan & Wilton 1998)
- Figure/ground beats decorative continuity

For each conflict: elements, competing principles, winning grouping, and whether it matches the
intended structure.

## 6. Report

Rank every finding by severity, whether it came from the task pass or the tests. Severity, for
findings and conflicts alike: **High** = can cause a wrong action, a wrong entry, or a
missed requirement in the main task; **Medium** = slows scanning or forces re-reading; **Low** =
polish.

Effort: **Low** = style, token, or spacing change in one group; **Medium** = restructuring inside one
region; **High** = restructuring across regions or changing the flow.

When severity depends on an open question, rate what a user who sees only this frame would
reasonably conclude, and say what would lower it. For tasks that must cover every item, anything
that can hide items or make a partial set look complete is High. Fixes are relative; pixel values only as labelled working
values. Before ranking, check the main task's path: fields and their commit action for forms; the
items to scan and open, and their look-alikes elsewhere, for browsing.

Findings and fixes first; sections 5–10 are the evidence.

1. **Audit frame:** frame, node ID, width, purpose, intended structure source, states available
2. **Verdict:** two sentences, main problem and first fix; layout health Coherent (only Low),
   Friction (a Medium, no High), or Misleading (a High)
3. **Findings, ranked:** twelve rows at most; High before Medium before Low, lower effort first
   within a level

   | # | Origin | Test IDs | Finding | Layer evidence | Severity | Effort | Fix |
   |---|---|---|---|---|---|---|---|

   Origin is `T1`, `T2`, ... or `tests`. An obstacle no principle explains carries `outside
   Gestalt` in Test IDs and names the workflow to hand it to.
4. **What passed:** what a redesign should keep
5. **Task pass:** the obstacles as written in step 2
6. **Grouping map:** mismatch type, elements, perceived as, intended as, layer names
7. **Principle matrix:** nine rows, score, failed tests, evidence
8. **Conflicts**
9. **Not assessed:** each unscored test and the frame or prototype link that would allow it
10. **Sources:** full references below for every source cited

Then offer, without doing it: "Add each High and Medium finding as a comment on its layer?" Post
comments only after a yes.

## Failure handling

| Situation | Action |
|---|---|
| No frame selected | Ask the user to select one frame |
| Whole page or file requested | Ask which screen carries the main task; audit that frame |
| Frame is a component or icon, not a screen | Say the audit needs a screen; offer to audit a frame that uses it |
| User asks to fix the layout | Finish the report; offer fixes as a separate, approved step |

## Sources

- Koffka, K. (1935). *Principles of Gestalt Psychology.* Harcourt, Brace.
- Palmer, S. E. (1992). Common region: A new principle of perceptual grouping. *Cognitive
  Psychology, 24*(3), 436–447.
- Palmer, S. E., & Rock, I. (1994). Rethinking perceptual organization: The role of uniform
  connectedness. *Psychonomic Bulletin & Review, 1*(1), 29–55.
- Quinlan, P. T., & Wilton, R. N. (1998). Grouping by proximity or similarity? Competition between
  the Gestalt principles in vision. *Perception, 27*(4), 417–430.
- Rubin, E. (1915). *Synsoplevede Figurer.* Gyldendal.
- Wagemans, J., et al. (2012). A century of Gestalt psychology in visual perception: I. Perceptual
  grouping and figure–ground organization. *Psychological Bulletin, 138*(6), 1172–1217.
- Wertheimer, M. (1923). Untersuchungen zur Lehre von der Gestalt. II. *Psychologische Forschung,
  4*, 301–350.

## About

Gestalt UI Audit by Monika Zapisek: [project site](https://monikazapisek.com) · [source and documentation](https://github.com/monikazapisek/design-engineering-playbook).
