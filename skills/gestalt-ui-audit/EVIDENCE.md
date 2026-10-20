# Evidence — gestalt-ui-audit

**Date:** 2026-10-14
**Version tested:** 1.0, rebuilt task-first
**Status:** draft, not ready to publish. Run 1 (easy synthetic screen): tie on detection. Run 2
(real news page): the baseline found more, including the biggest problem. After the task-first
rebuild, run 3 (unseen dense dashboard with a blind answer key): tie on detection, both 10 of 13,
including every cross-region look-alike the baseline found; the baseline still prioritised better.
The severity rule behind that is fixed but not re-tested. A real product screen and the Figma agent
run are still open.

## Gap check (BR-1)

Searched `skills/` and `agents/` before creating the skill.

| Existing asset | Overlap | Boundary |
|---|---|---|
| `ui-roi-audit` | Both audit a screen and rank fixes | ROI judges business impact; this skill judges perceived grouping and hierarchy |
| `vertical-spacing` (typesetting skillset) | Both use the proximity rule | Vertical-spacing sets exact values against a grid; this skill finds grouping mismatches and hands values over |
| `ux-content-design` | None in scope | Copy is handed off |

## Test inventory

| Test | Result |
|---|---|
| Synthetic job-details screen, default state | Pass, with author bias (see below) |
| Trigger routing: 5 positive and 5 negative requests | 10/10 at description level |
| Blind run by a fresh agent on the same screen | 10/10 planted problems found; borderline case passed correctly |
| With-skill vs no-skill baseline | Tie on detection; skill wins on auditability, baseline on brevity |
| Harder screen: real news-aggregator page, blind vs baseline | Baseline wins on detection: skill missed the biggest problem |
| Unseen dashboard with blind answer key, task-first rebuild | Tie on detection (10/13 each); baseline wins on prioritisation. `examples/sample-audit.md` |
| Live run in the Figma agent (`figma/gestalt-ui-audit.md`) | **Not run** |
| Figma MCP measurement mode in Claude | **Not run** |

## Synthetic-screen run

### Setup

A 1280 × 800 job-details screen built in HTML with eleven planted layout properties: ten problems
and one borderline case (a very faint card border on a white card).

### Result

| Planted property | Detected as |
|---|---|
| Equal label gaps above and below fields | PX-1, PX-2 |
| Helper text far from its field | PX-3, conflict 3 |
| Status chip in the primary-button style | SM-2, conflict 1 |
| Missing stepper connector | UC-2, conflict 2 |
| Indented form row | CN-1 |
| Photo strip cut at a gap | CL-1, CL-2 |
| Destructive button as loud as the primary | FG-4 |
| Form submit in the header | CR-1, CN-3 |
| Blue dates in the history list | SM-2 |
| Swapped label/value styles in the customer card | SM-1 |
| Faint card border (borderline) | Correctly scored Pass: the white fill carries the region |

One unplanted issue was also found: the select uses the browser's grey fill while inputs are white
(SM-1). Common fate was correctly marked *Not assessed*.

**Limitation:** the same session built the screen and ran the audit, so it knew what was planted.
This run proves the procedure and report format work end to end. It does not prove detection on an
unseen screen. The blind run and baseline below close that gap.

## Blind run and baseline (2026-10-14)

### Setup

Two fresh agents audited the job-details screenshot (since replaced in `examples/` by the run 3
dashboard) with the same request: "Run a Gestalt audit on
this screenshot. It is a job-details screen from a field-service app; the main task is assigning a
technician to the job." The blind agent could read only `SKILL.md`, `references/`, and the image; it
had no access to the planted list, this file, or the sample audit. The baseline agent could read only
the image and used its own judgment and format. Neither used the internet.

### Detection

| Planted problem | With skill (blind) | Baseline |
|---|---|---|
| Equal label gaps | Found | Found |
| Helper text far from its field | Found, High | Found, High |
| Status chip in the primary-button style | Found | Found |
| Missing stepper connector | Found | Found |
| Indented form row | Found | Found |
| Photo strip cut at a gap | Found | Found |
| Destructive button as loud as the primary | Found, High | Found, Critical |
| Form submit in the header | Found, Medium | Found, Critical, ranked first |
| Blue dates in the history list | Found | Found |
| Swapped customer label/value styles | Found | Found |
| Faint card border (borderline, should pass) | Passed correctly (CR-3) | Not mentioned |

Both found all ten. Both also found the unplanted grey select and suggested filtering the technician
list to licensed technicians.

### Five-point comparison

| # | Rubric | With skill | Baseline | Winner |
|---|---|---|---|---|
| 1 | Detection | 10/10, plus the borderline case judged | 10/10 | Tie |
| 2 | Prioritization | Rated the detached submit Medium under the old severity rule | Ranked the detached submit first | Baseline |
| 3 | Evidence and limits | Estimated values labelled; Not assessed list with inputs needed; uncited observations separated | Pixel values given as fact; no limits stated | With skill |
| 4 | Reasoning | Six conflicts explained with cue strength and citations | Principles named per issue, no conflict reasoning | With skill |
| 5 | Economy | Long report, about 2.5× the tokens | Short, directly actionable | Baseline |

**Score: with skill 2, baseline 2, one tie.**

### Verdict

On this screen the skill does not find more problems than a strong model without it. The planted
problems are visible to any experienced reviewer, so this screen cannot show a detection advantage.
The skill's value here is an auditable report: measured vs estimated values, explicit limits, cited
reasoning, and what to keep. Its cost is length.

### Fixes applied after the blind run

The blind agent listed ten points of friction. Fixed in `SKILL.md`, the references, and the Figma
version:

1. One severity rule for findings and conflicts; "missed requirement in the main task" is High. The
   detached submit now rates High in the sample audit, matching the baseline.
2. New checklist item: check the main task's fields and commit action for split groups.
3. The cue order in Step 3 is now a starting point adjusted for cue strength, matching the
   conflicts file.
4. *N/A* (subject absent) separated from *Not assessed* (evidence missing).
5. Effort levels defined.
6. Grouping map tables specified: perceived groups, intended groups, mismatches.
7. Fixes are relative; pixel values only as labelled working values.
8. Ambiguous intended structure: keep both readings, give a conditional fix.
9. Frame states the image size; device scale only when given.
10. The reference list now sits in `report-contract.md`, so the report no longer depends on
    `ATTRIBUTION.md`.

Not re-tested after these fixes.

## Harder screen: real news-aggregator page (2026-10-14)

### Setup

A 1715 × 932 screenshot of a dense, third-party news-aggregator homepage section, supplied by the
author: a thumbnail carousel, a section banner over two category columns of thumbnail-plus-headline
items, a decorative quote card, and a Recent Comments sidebar. No problems were planted. The image
is not stored in this repository because it contains third-party editorial content and photographs
of real people. Both agents were told to audit layout only. The blind agent ran v1.0 after the first
round of fixes; the baseline agent had no skill.

### Detection, judged by the author against the screenshot

| Problem on screen | With skill | Baseline |
|---|---|---|
| Sidebar comments set like headlines, competing with the task's items | **Missed** | Found, ranked first |
| Inline icons after headlines: fused, inconsistent, one wraps alone | Found | Found |
| Section headers: same bar style for parent and child, three header systems | Found | Found |
| Quote card, scrollbar track, and carousel out-shout the headline lists | Found | Found |
| Carousel tiles framed inconsistently | Missed | Found |
| Comment action icons far from their comment | Missed | Found |
| Column gutter tight at header level | Measured from text and passed | Found |
| Sidebar left edges drift | Found | Found |
| Category header closer to the banner than to its own items | Found | Missed |
| Comment body-to-author gap equals the gap to the next comment | Found | Missed |
| Carousel tiles have no text titles | Found, as an uncited observation | Found |

### Five-point comparison

| # | Rubric | With skill | Baseline | Winner |
|---|---|---|---|---|
| 1 | Detection | 8 of 11; missed the most important | 9 of 11, including the most important | Baseline |
| 2 | Prioritization | First fix: quote card and icons | First fix: comments that look like headlines | Baseline |
| 3 | Evidence and limits | Estimated values, conditional severity, capture crops separated from UI clipping | Rough values, no limits | With skill |
| 4 | Reasoning | Four conflicts with cue strength | Principles named per issue | With skill |
| 5 | Economy | Long | Short | Baseline |

**Score: with skill 2, baseline 3.**

### Diagnosis

The procedure keeps attention inside regions: it maps groups region by region and compares each
group with its own intended structure. A look-alike in another region, such as comments styled
like headlines, never becomes a candidate group, so no test catches it. The baseline looked at the
whole screen from the task's point of view and caught it first.

### Fixes applied after this run

1. New cross-region sweep in Step 3: compare the main task's items with everything else on screen.
2. New tests SM-5 (look-alikes outside the task) and SM-6 (one frame treatment per tile set).
3. New mismatch type *Wrong figure*: a non-task region dominates the task region.
4. Scoring rule: a principle takes its worst test's score unless a stronger cue repairs the grouping.
5. Capture crops go to *Not assessed*, not to closure tests.
6. Conditional severity: rate the lower level, state what raises it; health uses confirmed findings.
7. One issue, one finding, with every failed test ID.
8. Checklist covers browsing tasks, not only forms.

These fixes were derived from this screen, so a re-run on it would not be a fair test. Not
re-tested.

## Third screen, unseen: dense dashboard with a blind answer key (2026-10-14)

### Why the procedure was rebuilt first

The run 2 fixes (SM-5, cross-region sweep) patched the one miss that screen showed. The cause was the
order of work: a principle checklist applied region by region narrows attention to what the list
asks. The procedure now starts with a task pass, in which the agent looks at the whole screen as the
user doing the task and lists the biggest obstacles before loading any reference. The principles
then explain those obstacles and add what the look missed. See `CHANGELOG.md`.

### Setup

- **Screen:** a separate agent built a 1440 × 900 logistics operations console (fictional product,
  carriers, and people). It has a filter rail, KPI row, a 16-row shipments table with date sections
  and a bulk bar, and a right rail with Needs attention, a promo card, and Activity. Main task:
  "find every overdue Northline Freight shipment and reassign it to another carrier."
- **Answer key:** the same agent planted 13 problems, 6 local and 7 cross-region (4 High, 7 Medium,
  2 Low), plus 2 borderline elements that should pass. It wrote them to a key that the orchestrating
  session opened only after both audits were written. No fix in the skill was derived from this
  screen before the run.
- **Runs:** as in runs 1 and 2. The blind agent could read `SKILL.md`, `references/`, and the image.
  The baseline agent could read only the image. Both got the same one-sentence brief.

### Detection against the key

| Key | Planted problem | Scale | Key severity | With skill | Baseline |
|---|---|---|---|---|---|
| P1 | CARRIER heading tight under Status, divider below it | Local | Medium | Found, Medium | Found, Major |
| P2 | Overdue and At risk share one KPI card | Local | Low | Found, Low | Found |
| P3 | ETA and Weight headers right-aligned over left-aligned values | Local | Medium | Partly: ETA only | Partly: ETA only |
| P4 | Overdue in two badge styles; Delayed in the filled-Overdue red | Local | High | Found, High, ranked first | Found, Critical, ranked first |
| P5 | Bulk bar below pagination; Reassign is a weak outline button | Local | Medium | Found, Medium | Found, Major |
| P6 | Date-group header rows look like data rows | Local | Low–Medium | Missed | Missed |
| P7 | Needs attention mimics the table and has stronger Reassign buttons | Cross-region | High | Found, Medium (High if taken as the full list) | Found, Major |
| P8 | Gradient promo dominates the screen | Cross-region | Medium | Found (*Wrong figure*) | Found |
| P9 | Filter chips in the global search, far from the table; count unfiltered | Cross-region | High | Found, Medium (High if chips and checkboxes diverge) | Found, Critical |
| P10 | Date range styled as a KPI tile, silently limits the table | Cross-region | High | Partly: styling, Low; scope missed | Partly: styling; scope missed |
| P11 | Filter rail merges with the dark nav rail | Cross-region | Medium | Missed; listed the dark panel as a pass | Missed; listed the dark rail as a pass |
| P12 | Three equal filled header buttons; the task action is weakest | Cross-region | Medium | Found | Found, Major |
| P13 | Apply filters pinned far from the filters; zigzag reading path | Cross-region | Medium | Found (CN-3 path) | Found (pending vs applied) |
| B1 | Value column right-aligned (correct) | Borderline | Pass | Not flagged | Not flagged |
| B2 | Muted monospace IDs, separated kebab column | Borderline | Pass | Not flagged | Not flagged |

**Count:** found 10, partly 2 (counted as half), missed 1 per auditor: both 10 of 13 on the same
items. Both missed P6 and P11; both passed both borderline elements.

Unkeyed but valid: the baseline noted that selection covers only the current page and offers no
"select all matching", which matters for a "find every" task. The skill noted the saved-view
highlight that contradicts the table title, and routed the count contradiction to functional QA as
*outside Gestalt*.

### Five-point comparison

| # | Rubric | With skill | Baseline | Winner |
|---|---|---|---|---|
| 1 | Detection | 10/13, same items, all found in the task pass | 10/13 | Tie |
| 2 | Prioritization | 1 of 4 key Highs rated High; P7 and P9 held at Medium by the "rate the lower level" rule | 2 of 4 key Highs rated Critical; also rated one non-key item Critical | Baseline |
| 3 | Evidence and limits | Estimated values, Not assessed with the capture needed, conditional severities, data issue routed out | Rough values, no limits | With skill |
| 4 | Reasoning | Grouping map, conflicts with cue strength, *Wrong figure* named | Principles named per issue; good task walk-through table | With skill |
| 5 | Economy | About 2× the baseline length; grouping map and conflicts restate findings | Short, directly actionable | Baseline |

**Score: with skill 2, baseline 2, one tie.**

### Verdict

The rebuild fixed the failure mode from run 2. On an unseen screen with seven cross-region problems,
the skill found everything the baseline found, and it found all of it in the task pass, before any
principle was loaded. This meets the detection condition of open gate 2. The principle sweep added
only low-severity items (KPI card, date-range styling, alignment, icons). On this screen its value
was evidence and limits, not detection.

The skill still does not beat the baseline. Its severity rule demoted two High problems, and its
report is longer. Both auditors share blind spots: neither saw the date-group headers or the merged
dark rails, and both counted the merged rails as a strength.

### Fixes applied after this run

From the comparison and the blind agent's friction list. No new principle tests were added, so no
fix targets this screen's specific problems:

1. **Severity:** an open question no longer pulls severity down. Rate what a user who sees only the
   screen would reasonably conclude, and state what would lower the rating. For "find every" tasks,
   anything that can hide items or make a partial set look complete is High.
2. **Task pass:** one more question: could the user believe the task is done while part of it is on
   another page, behind a filter or range, or in another region?
3. **Principle scores:** Fail when a failed test causes a mismatch on the task path or several tests
   fail; isolated local breaks are Partial. This removes the clash with the Partial definition.
4. Single tests can be N/A.
5. *Outside Gestalt* findings take `—` for effort. A new handoff row routes contradictory counts,
   filters, or data to functional QA.
6. The report contract loads whole in Step 3; the split into scoring and structure was notional.
7. The grouping-map mismatch table and the conflicts cite finding numbers instead of restating them.

Not re-tested. Fixes 1 and 2 would have raised P7 and P9 to High, and possibly caught the scope of
P10. Confirming that needs another unseen screen.

## Trigger routing (description level)

### Should invoke

| Request | Result |
|---|---|
| "Run a Gestalt audit on this dashboard." | Invoke |
| "Why does this settings page feel cluttered?" | Invoke |
| "Is it clear which label belongs to which field?" | Invoke |
| "Check this screen for proximity and similarity problems." | Invoke |
| "Is the visual hierarchy of this modal clear?" | Invoke |

### Should not invoke

| Request | Route instead |
|---|---|
| "Will this landing page redesign pay off?" | `ui-roi-audit` |
| "Set spacing tokens on an 8 px grid for this card." | Vertical-spacing audit |
| "Rewrite the error messages in this form." | Content design |
| "Check this screen against WCAG 2.2 AA." | Accessibility audit |
| "Review this React component's code." | Code review |

## Open gates before publication

1. ~~**Blind run.**~~ Closed 2026-10-14; see above.
2. ~~**Third screen, unseen.**~~ Detection condition met 2026-10-14 (tie, 10/13 each, every
   cross-region look-alike the baseline found). Prioritisation still lost; the severity fix needs
   confirming on gate 3.
3. **Real screen, unseen:** one screen from a real product, with permission or from a public demo,
   with an answer key written before either audit runs. Pass condition: detection at least equal
   to the baseline, and the key's High items rated High.
4. **Figma agent:** one live run of `figma/gestalt-ui-audit.md` on a selected frame, including the
   comment-consent step.
5. ~~**Citations:** check the volume and page numbers of Palmer & Rock 1994 and Wagemans et al.
   2012.~~ Closed 2026-10-14: both confirmed with DOIs; see `ATTRIBUTION.md`.

## Token budget

| File | Loaded |
|---|---|
| `SKILL.md` | Always, on trigger |
| `references/principles.md` | Step 3, after the task pass |
| `references/report-contract.md` | Scoring section in Step 3; report structure in Step 5 |
| `references/principle-conflicts.md` | Step 4, only when conflicts exist |
| `examples/sample-audit.md` | Only when a format example is needed |
