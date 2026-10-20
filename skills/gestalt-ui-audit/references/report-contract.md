# Report contract

Loaded in Step 3: scoring applies from Step 3, the report structure in Step 5.

## Scoring

### Principle scores

| Score | Meaning |
|---|---|
| Pass | Tests pass; the principle supports the intended structure |
| Partial | Mostly holds, with local breaks or a weak cue |
| Fail | The principle produces a mismatch or blocks a test |
| Not assessed | The evidence is not in the input: a state, motion, or measurement |
| N/A | The subject is absent from the screen: no connectors, overlay, or icons |

- Single tests can be N/A (PX-3 on a screen without helper text); a principle is N/A only when all
  its tests are N/A.
- Fail when a failed test causes a mismatch on the main task's path, or when several tests fail.
  Partial when the failures are isolated local breaks, or when a stronger cue repairs the grouping
  (see `principle-conflicts.md`); name the repairing cue.
- One issue is one finding, listing every test ID it fails.
- Label pixel values *estimated* unless they come from Figma.

### Mismatch types

| Type | Meaning |
|---|---|
| False group | Elements look related but are not, including look-alikes in other regions |
| Split group | Related elements look separate |
| Wrong owner | An element attaches to the wrong group (label, helper, action) |
| Flat hierarchy | Groups exist but none dominates |
| Wrong figure | A region outside the main task dominates the region where the task happens |

### Severity

The same scale applies to findings and conflicts, whatever their origin:

- **High:** can cause a wrong action, a wrong entry, or a missed item in the main task
- **Medium:** slows scanning or forces re-reading; the user still succeeds
- **Low:** polish; no effect on task success

When severity depends on an open question, rate what a user who sees only this screen would
reasonably conclude, and state what would lower the rating. For tasks that must cover every item
("find all", "reassign every"), anything that can hide items or make a partial set look complete is
High.

### Effort

- **Low:** a style, token, or spacing change inside one element or group
- **Medium:** moving or restructuring elements inside one region
- **High:** restructuring across regions or changing the flow

*Outside Gestalt* findings take `—` for effort; the receiving workflow estimates it.

### Fixes

State the change in relative terms: "label-to-field gap clearly smaller than field-to-field gap",
not "improve spacing". Pixel values appear only as a labelled working value; exact values go to a
vertical-spacing audit. When the intended structure is ambiguous, give a conditional fix.

## Report structure

Keep it scannable: sections 1–4 are for the reader who stops early; 5–10 are the evidence.

### 1. Audit frame

Screen and state; image size (device or scale only if given); main task; intended structure
(supplied or inferred); measurement mode; states observed.

### 2. Verdict

Two sentences: the main problem for the task, and the fix to make first. No numeric score.

Layout health: **Coherent** (only Low findings), **Friction** (at least one Medium, no High), or
**Misleading** (at least one High).

### 3. Findings, ranked

Twelve rows at most; group small issues. High before Medium before Low; within a level, lower effort
first.

| # | Origin | Test IDs | Finding | Screen evidence | Severity | Effort | Fix |
|---|---|---|---|---|---|---|---|

Origin is `T1`, `T2`, ... for a task-pass obstacle, or `tests` for a finding the tests added.
Obstacles no principle explains carry `outside Gestalt` in the Test IDs column and name the
workflow to hand them to.

### 4. What passed

Elements and patterns a redesign should keep.

### 5. Task pass

The obstacles as written in Step 2, before the principles were applied.

### 6. Grouping map

| ID | Perceived group | Cue that forms it | Location |
|---|---|---|---|

| ID | Intended group | Source (supplied or inferred) | Location |
|---|---|---|---|

| # | Mismatch type | Elements | Perceived as | Intended as | Location |
|---|---|---|---|---|---|

List groups, not every element. In the mismatch table, cite the finding number instead of repeating
its fix; list a mismatch in full only when no finding covers it.

### 7. Principle matrix

| Principle | Score | Tests that failed | Evidence (one line) |
|---|---|---|---|
| GP-PX Proximity | | | |
| GP-SM Similarity | | | |
| GP-CR Common region | | | |
| GP-UC Uniform connectedness | | | |
| GP-CN Continuity | | | |
| GP-CL Closure | | | |
| GP-FG Figure/ground | | | |
| GP-CF Common fate | | | |
| GP-PR Prägnanz | | | |

Give the reason for every Not assessed and N/A.

### 8. Conflicts

One entry each: elements, competing principles, winning grouping, match with the intended structure,
severity, and the finding number it supports. Skip conflicts that only restate a finding.

### 9. Not assessed

Each unscored test and the input that would allow it: a state to capture, a prototype link, or Figma
access for measurements.

### 10. Sources

Full references for every source cited, from this list:

- Koffka, K. (1935). *Principles of Gestalt Psychology.* Harcourt, Brace.
- Palmer, S. E. (1992). Common region: A new principle of perceptual grouping. *Cognitive
  Psychology, 24*(3), 436–447.
- Palmer, S. E., & Rock, I. (1994). Rethinking perceptual organization: The role of uniform
  connectedness. *Psychonomic Bulletin & Review, 1*(1), 29–55. https://doi.org/10.3758/BF03200760
- Quinlan, P. T., & Wilton, R. N. (1998). Grouping by proximity or similarity? Competition between
  the Gestalt principles in vision. *Perception, 27*(4), 417–430. https://doi.org/10.1068/p270417
- Rubin, E. (1915). *Synsoplevede Figurer.* Gyldendal.
- Wagemans, J., Elder, J. H., Kubovy, M., Palmer, S. E., Peterson, M. A., Singh, M., & von der
  Heydt, R. (2012). A century of Gestalt psychology in visual perception: I. Perceptual grouping
  and figure–ground organization. *Psychological Bulletin, 138*(6), 1172–1217.
  https://doi.org/10.1037/a0029333
- Wertheimer, M. (1923). Untersuchungen zur Lehre von der Gestalt. II. *Psychologische Forschung,
  4*, 301–350.

## Citation rules

- Cite principles as author and year: `(Palmer 1992)`.
- Paraphrase. No quotation longer than one short sentence, at most one per report.
- Never present a working value as a research finding.
