# Changelog — gestalt-ui-audit

All notable changes to this skill are documented here.
Format follows [Keep a Changelog](https://keepachangelog.com/en/1.1.0/) and semantic versioning.

## v1.0.0 — 2026-10-14

Initial release.

- Nine principles with test IDs: proximity, similarity, common region, uniform connectedness,
  continuity, closure, figure/ground, common fate, Prägnanz.
- Perceived-versus-intended grouping map as the core step; mismatches are the strongest findings.
- Conflict rules between principles, framed as predictions that depend on cue strength.
- Pass / Partial / Fail / Not assessed scoring; no overall numeric score.
- Optional Figma measurement mode; static screenshots mark dynamic criteria *Not assessed*.
- Single-file Figma agent version in `figma/gestalt-ui-audit.md`.

### Changed after the unseen-dashboard run

- Severity: an open question no longer lowers the rating; for "find every" tasks, anything that can
  hide items or make a partial set look complete is High.
- Task pass asks whether the user could believe the task is done while part of it is out of view.
- Principle score: Fail for a mismatch on the task path or several failed tests; isolated local
  breaks are Partial. Single tests can be N/A.
- *Outside Gestalt* findings take `—` for effort; contradictory counts and filters route to
  functional QA.
- Report contract loads whole in Step 3. Grouping map and conflicts cite findings, not restate them.
- New sample audit: the blind run on the dashboard, replacing the job-details example.

### Rebuilt: task pass before principles

The cross-region patch fixed one miss, not its cause: a principle-first, region-by-region procedure
narrows attention to what the checklist asks. The procedure now runs in this order:

- Step 2, task pass: look at the whole screen as the user doing the main task and write the 3–5
  biggest obstacles in plain words, before any reference is loaded.
- Step 3, explain then extend: each obstacle is explained with tests and evidence, or kept as
  *outside Gestalt*; then the full principle sweep adds findings marked *from tests*.
- The report leads with ranked findings and what passed; task pass, grouping map, matrix, and
  conflicts follow as evidence. Findings carry an Origin column.
- Same order in the Figma agent version.

### Changed after the harder-screen run

- Cross-region sweep in Step 3; new tests SM-5 (look-alikes outside the task) and SM-6 (tile frames).
- New mismatch type *Wrong figure*.
- Principle score follows the worst test unless a stronger cue repairs the grouping.
- Capture crops, conditional severity, and double counting handled explicitly.
- Effort levels and fix wording moved to `report-contract.md`.

### Changed after the blind run

- One severity rule for findings and conflicts; missed requirements in the main task are High.
- *N/A* (subject absent) separated from *Not assessed* (evidence missing).
- Effort levels, grouping-map tables, and relative fixes specified.
- Step 3 cue order is a starting point adjusted for cue strength.
- Ambiguous intended structure handled with conditional fixes.
- Reference list moved into `report-contract.md`.

### Changed from the first draft

- Removed labels that were not synonyms of the principles (emergence, reification, invariance,
  multistability).
- Split "connectedness" into common region (Palmer 1992) and uniform connectedness (Palmer & Rock
  1994).
- Added common fate.
- Prägnanz no longer requires symmetry.
- Replaced the persona prompt with a procedure, inputs, and failure handling.
