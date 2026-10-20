# Sample audit: shipments table of a logistics ops console

A blind run of the skill, kept as a format reference. The screen is synthetic: an invented logistics
dashboard (`sample-screen.png`, 1440 × 900), built by a separate agent with a private answer key
the auditing agent never saw. It contains no real product, company, or person.

The run used the task-first procedure before the later rule changes (see `EVIDENCE.md`). Frame,
verdict, findings, and task pass are as the agent wrote them; under the current severity rule,
findings 3 and 5 would rate High. Edited to the current format: the grouping map and conflicts are
condensed and cite finding numbers, uniform connectedness is rescored Partial under the current
scoring rule, and the sources are shortened.

## 1. Audit frame

| Item | Value |
|---|---|
| Screen and state | Shipments list, Operations / Outbound. Filter chips "Carrier is Northline Freight" and "Status is Open" in the global search bar; sidebar has Open (all) and Northline Freight checked; saved view "My open shipments" highlighted; 3 rows selected and the bulk-action bar visible; page 1 of 86. |
| Image size | 1440 × 900 px. No device or scale given. |
| Main task | Find every overdue Northline Freight shipment and reassign it to a different carrier (supplied). |
| Intended structure | Inferred from headings, labels, and selection state: header and actions, KPI row, "All shipments" table with date sections, pagination and bulk bar; left icon nav and filter panel; right rail with Needs attention, promo, Activity. **Ambiguous:** Overdue appears filled and outlined: two sub-states or an inconsistency. Both readings carried into the fixes. |
| Measurement mode | *Estimated* from pixels. |
| States observed | Default with a 3-row selection. No hover, loading, empty, pending-filter, or post-action state. |

## 2. Verdict

The overdue signal the user scans for is unreliable: Overdue appears in two badge styles, and
Delayed uses the same filled red as one of them, so colour groups Delayed with Overdue and splits off
the outlined Overdue rows. The current selection shows the error: one Delayed row is in it and three
outlined Overdue rows are not. Fix that first, then move the bulk *Reassign carrier* next to the
selection and make it the strongest action.

**Layout health:** Misleading

## 3. Findings, ranked

| # | Origin | Test IDs | Finding | Screen evidence | Severity | Effort | Fix |
|---|---|---|---|---|---|---|---|
| 1 | T1 | SM-1, SM-3, PR-3 | Overdue rows do not form one visual group. Two Overdue styles; Delayed shares the filled red. Colour binds filled Overdue with Delayed (Quinlan & Wilton 1998). | Filled Overdue: SH-48213, 48152, 48071, 48031. Outlined: 48196, 48147, 48052. Filled red Delayed: 48207, 48141, 48066. The selection includes Delayed 48207 and misses all outlined Overdue rows. | High | Low | One style per status; Delayed differs from Overdue in fill and hue. If outlined Overdue is a sub-state, keep the base style and add a secondary mark: the difference between two Overdue badges clearly smaller than between Overdue and Delayed. |
| 2 | T5 | PX-1, PX-2, UC-3 | The CARRIER heading belongs to the Status group: about 8 px under "Delivered", about 32 px above its first item (*estimated*), with a divider between heading and list. | Left panel. STATUS and ORIGIN HUB have the larger gap above; CARRIER reverses it. | Medium | Low | Larger gap and divider above CARRIER; heading-to-list gap clearly smaller (working value: at least 1.5×). |
| 3 | T4 | SM-5, FG-4, CR-1 | The right-rail Reassign buttons read as the task's action set: four filled blue buttons, louder than the bulk action, identical for Northline Overdue and a Coastway Delayed item. The rail shows 4 items against 47 overdue; two IDs are not on the visible page. | Needs attention vs the outlined bulk bar. | Medium; High if the rail is treated as the complete list | Low | Make rail actions secondary; keep the bulk action as the only filled reassign. Filter the rail to match the table, or label it "4 of 47". |
| 4 | T4 | FG-1, FG-4, PR-2, PR-4 | Wrong figure: the gradient promo ("auto-reassign") and three filled header buttons outrank the table where the task happens. | Promo in the right rail; Import, Export CSV, New shipment top right. | Medium | Low | Neutralise the promo or move it below Activity; one filled header button at most; reserve filled primary for the selection's action. |
| 5 | T2 | CR-1, PX-1, CN-3 | The filter state is split across three places with no shared region: chips in the global search, checkboxes in the left panel with Apply about 185 px below (*estimated*), and a saved-view highlight that contradicts "All shipments 1,284". | Top bar, sidebar, table header. | Medium; High if chips and checkboxes can diverge | Medium | One active-filter chip row in the table card header, mirrored by the sidebar; show a pending state if Apply stays; clear the saved-view highlight when filters no longer match. |
| 6 | T3 | CF-2, PX-1, FG-4, CN-3 | The bulk-action bar sits below the pagination, far from the selection, and reads as the list footer. Its buttons are the weakest in the main area. | Selected rows in the upper table; bar at the bottom. | Medium | Medium | Replace the table toolbar with the selection bar while rows are selected, or make it sticky above the rows; *Reassign carrier* the one filled button. |
| 7 | T2 | CR-2, SM-3, CN-3 | Overdue rows are scattered across Due today, Due yesterday, and Earlier, and across 86 pages. | 3 overdue under Due today, 2 under Due yesterday, 3 under Earlier. | Medium | Medium | Conditional: if date grouping is the intended primary structure, surface the Overdue status filter by the table; otherwise group or sort by status when filtering for Overdue. |
| 8 | T2 | outside Gestalt → functional QA | Counts contradict each other: Northline 318, table 1,284 results over 86 pages, saved view 212, KPI scope unclear. The user cannot confirm "every". | Sidebar, table header, KPI row. | Medium; High if the table is really unfiltered | — | Verify filter logic; label the scope of each count. |
| 9 | tests | CR-2 | Overdue and At risk share one KPI card without a divider. | KPI tile 2. | Low | Low | Split the card or add an inner divider. |
| 10 | tests | SM-2, SM-6 | The Date range control is styled as a KPI tile. | Last KPI tile. | Low | Low | Style it as a control and place it with the header or toolbar. |
| 11 | tests | CN-2 | ETA header right-aligned over left-aligned values; numeric columns aligned inconsistently. | Table columns. | Low | Low | Align each header with its values; right-align numeric columns. |
| 12 | tests | CL-4 | Two gear-like glyphs in the icon rail. | Icon rail. | Low | Low | Distinct glyphs or labels. |

## 4. What passed

- Table scanning: clean rows and columns (PX-4); monospace IDs as a clear key column.
- Red lateness marker in ETA (+5h, +7d): only on overdue rows, the most reliable overdue cue.
- Selection marking: checkbox and row tint change together (CF-1).
- Filter panel alignment (CN-1).
- Five nameable regions (PR-1) with deliberate asymmetric balance (PR-5).
- Truncation and paging signal more content (CL-1, CL-2).

## 5. Task pass

Written before any reference was loaded:

- **T1.** Overdue looks like two different things. Delayed shares the filled red, so scanning for red
  pills catches Delayed rows and skips outlined Overdue rows. The selection shows this.
- **T2.** I can't tell whether the list holds all Northline overdue shipments: filters in three
  places, 1,284 results over 86 pages, overdue rows spread across the date sections.
- **T3.** The bulk *Reassign carrier* is small and outlined, under the pagination, far from the
  selected rows.
- **T4.** The rail's filled Reassign buttons (one for a Coastway Delayed shipment), the gradient
  promo, and the three blue header buttons all outrank the table.
- **T5.** The CARRIER label looks like part of the Status list, with a divider under it.

## 6. Grouping map

| ID | Perceived group | Cue that forms it | Location |
|---|---|---|---|
| P1 | Filled red pills: Overdue (filled) + Delayed | Similarity | Table, rail |
| P2 | Outlined Overdue pills | Similarity | Table |
| P3 | Status list + CARRIER heading | Proximity, divider | Left panel |
| P4 | Filled blue actions: header buttons + rail Reassign | Similarity across regions | Header, rail |
| P5 | Promo as the dominant figure | Figure/ground | Rail |
| P6 | Bulk bar + pager as the list footer | Proximity | Table bottom |

| ID | Intended group | Source | Location |
|---|---|---|---|
| I1 | All Overdue shipments as one category | Inferred | Table, rail |
| I2 | CARRIER heading + carriers | Inferred | Left panel |
| I3 | Selected rows + bulk actions | Inferred | Table |
| I4 | One active filter set controlling the table | Inferred | Top bar, left panel |

| # | Mismatch type | Elements | Finding |
|---|---|---|---|
| M1 | Split group + False group | Overdue styles; Delayed with filled Overdue | 1 |
| M2 | Wrong owner | CARRIER heading | 2 |
| M3 | False group | Rail Reassign buttons as the task's actions | 3 |
| M4 | Wrong figure | Promo, header buttons | 4 |
| M5 | Split group | Chips, sidebar, Apply, saved view | 5 |
| M6 | Split group | Bulk bar vs selected rows | 6 |
| M7 | False group | Overdue + At risk; Date range as a KPI | 9, 10 |

## 7. Principle matrix

| Principle | Score | Tests that failed | Evidence (one line) |
|---|---|---|---|
| GP-PX Proximity | Fail | PX-1, PX-2 | CARRIER gap reversed; bulk bar binds to the pager. PX-3 N/A (no helper text). |
| GP-SM Similarity | Fail | SM-1, SM-2, SM-3, SM-5, SM-6 | Two Overdue styles; Delayed shares the fill; rail Reassign looks like the task action. SM-4 Not assessed. |
| GP-CR Common region | Fail | CR-1, CR-2 | Chips outside the table they filter; two KPIs in one card. |
| GP-UC Uniform connectedness | Partial | UC-3 | One divider splits CARRIER from its list. UC-1, UC-2 N/A (no connectors). |
| GP-CN Continuity | Partial | CN-2, CN-3 | Mixed alignment; the task path zigzags top → left → bottom left → table → bottom bar. |
| GP-CL Closure | Partial | CL-4 | Two similar gear icons. CL-3 Not assessed (no loading capture). |
| GP-FG Figure/ground | Fail | FG-1, FG-4 | Promo and filled header buttons outrank the table. FG-2 N/A (no overlay). |
| GP-CF Common fate | Partial | CF-2 | Selection marking is uniform; the bar is detached from the rows. CF-3, CF-4 Not assessed. |
| GP-PR Prägnanz | Partial | PR-2, PR-3, PR-4 | Competing focal points, inconsistent badge pattern, decorative promo. |

## 8. Conflicts

| # | Elements | Competing principles | Winning grouping | Matches intended? | Severity | Finding |
|---|---|---|---|---|---|---|
| C1 | Status badges | Colour similarity vs label text | Colour: Delayed joins filled Overdue | No | High | 1 |
| C2 | Rail Reassign vs bulk action | Cross-region similarity and figure strength vs the table's region | The rail | No | Medium | 3 |
| C3 | Overdue rows | Date-section region vs badge similarity | Date sections: the overdue set fragments | Partly | Medium | 7 |

## 9. Not assessed

- SM-4: needs Figma; would also show whether the two Overdue styles are separate variants by design.
- CF-2 stickiness, CF-3, CF-4: need a prototype or video.
- CL-3: needs a loading-state capture.
- Pending vs applied filters: needs a capture after toggling a checkbox, before *Apply filters*.
- Clickability of KPI and rail items: needs hover states.
- Exact pixel values: need Figma. All values here are *estimated*.

## 10. Sources

Koffka 1935; Palmer 1992; Palmer & Rock 1994; Quinlan & Wilton 1998; Rubin 1915; Wagemans et al.
2012; Wertheimer 1923. Full references in `references/report-contract.md`. The 1.5× gap ratio is a
working value, not a research finding.
