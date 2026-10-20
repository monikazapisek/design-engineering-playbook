---
name: ui-roi-audit
description: Use whenever a selected Figma frame shows a landing, home, category, product, form, or checkout page, or a task-driven interface screen, and the request is an ROI, conversion, or usability audit, or which fix to make first. Read the frame's layers, score them against source-cited criteria, rank fixes by exposure, severity, and effort, and estimate a 12-month ROI range only from numbers the user supplies. Report only; ask before adding comments.
---

# UI ROI Audit

Judge one selected frame by whether it moves a person toward the conversion or task the organization
values, then rank fixes by likely return. Taste is out of scope. A sourced finding needs a criterion
ID; anything else is labelled as the auditor's own observation and kept out of the ranking.

## Operating contract

- Read the selection and report before asking anything else.
- Ask only for inputs that change the result: the success goal, the page type if the frame does not
  show it, and the traffic source for a landing page.
- Never change layers. Adding comments on the canvas requires explicit approval.
- Do not write replacement copy, and do not audit SEO, brand voice, or WCAG compliance.
- Never invent traffic, conversion, or cost numbers. Without them, the estimate is qualitative.

## 1. Frame the audit

Require one selected top-level frame: one page, screen, or task step per run. If several frames are
selected, audit the first and list the others as candidates for later runs.

State:

- target frame name and node ID
- type: landing, home, category, product/detail, form, checkout, or task-driven interface
- one success goal: purchase, lead, signup, call, completed task, time saved, or cost avoided
- users or audience, and the traffic source for a landing page
- available data: monthly visits, conversion rate, average order or lead value, implementation
  cost, funnel drop-off, support or task-time volumes
- viewport: frame width, and the first-screen height used (see step 2)

If the success goal is missing, stop and ask for the one outcome that counts.

## 2. Inventory the frame

Read visible layers only (`visible !== false`), in reading order: top to bottom, then left to right
within a row. Record:

- text layers: `characters`, `fontSize`, `fontWeight`
- instances: main component name and variant properties (button, input, nav, card, rating, price)
- images: nodes with an `IMAGE` fill, and what they appear to show
- position: `absoluteBoundingBox` y, to decide what falls inside the first screen
- prototype `reactions` on the primary action, if any

**First screen.** Use the top area of the frame at the height of the user's stated device. If none is
stated, use a working assumption of 900 px for frames 1024 px or wider and 800 px for frames below
480 px, and say so in the report. Mobile reading of "above the fold" means within the first screen on
the user's device.

**States.** Error, loading, empty, success, and post-submit states count as observed only when they
exist as separate frames the user points to or the prototype links to. Otherwise mark them
*not observed*. Never score an unobserved state as a failure.

## 3. Score page and content criteria

For conversion pages, score the section for the page type plus the cross-cutting criteria. For a
purely task-driven interface, skip to step 4.

| Score | Meaning |
|---|---|
| Pass | Present and doing its job |
| Partial | Present but weak, buried, or contradicted |
| Fail | Missing or working against the goal |
| N/A | Not applicable or not observable in the frame |

Every Partial and Fail needs layer evidence: layer name, text, or position.

Source key: **LN08** = Loveday & Niehaus 2008. Criteria are paraphrased, checkable restatements.

### Landing page (LN08, ch. 4)

- LP-1 Headline repeats the promise of the ad or link that brought the visitor
- LP-2 Images match the ad's subject
- LP-3 One primary call to action inside the first screen
- LP-4 Navigation and links leading away from the goal are removed or reduced

### Home page (LN08, ch. 5)

- HP-1 What is offered, and for whom, is clear within seconds
- HP-2 Logo and identity are clearly visible
- HP-3 A clear call to action points to the main conversion path
- HP-4 Navigation is clear and easy to scan
- HP-5 No splash screen or intro stands before the content

### Category page (LN08, ch. 6)

- CP-1 Filters relevant to the category narrow the list
- CP-2 Sorting on the attributes buyers compare
- CP-3 Thumbnails are large and clear enough to recognize
- CP-4 Price shown in the list

### Product / detail page (LN08, ch. 7)

- DP-1 High-quality images that can be enlarged
- DP-2 Prominent add-to-cart or equivalent action
- DP-3 Description states the properties a buyer needs
- DP-4 Reviews or ratings shown
- DP-5 Availability and shipping shown before the cart
- DP-6 Price visible next to the action

### Form (LN08, ch. 8)

- FM-1 Clear vertical flow, normally one column; short related fields may share a row
- FM-2 Labels close to fields, in a consistent top- or right-aligned pattern
- FM-3 Known data is pre-filled
- FM-4 Help sits next to the field that needs it
- FM-5 Error messages meet ER-1 to ER-3
- FM-6 Privacy and data-use reassurance near the submit action

### Checkout (LN08, ch. 9)

- CO-1 Site navigation and unrelated links removed
- CO-2 Step indicator shows position and what remains
- CO-3 Purchase possible without an account
- CO-4 Security and guarantee assurances where payment data is entered
- CO-5 No charge appears that was hidden earlier (also ch. 6, ch. 7)

### Cross-cutting content and trust (LN08)

- VP-1 Headline states a concrete benefit, readable in seconds (ch. 4, ch. 5)
- VP-2 Plain wording, no vague corporate language in place of the offer (ch. 4, ch. 5)
- VP-3 Value proposition inside the first screen (ch. 5)
- CA-1 Primary call to action is the most visually dominant interactive element: compare size,
  fill, weight, and position with other buttons and links (ch. 4, ch. 5)
- CA-2 Its label starts with a verb and says what happens next (ch. 4)
- CA-3 It sits inside the first screen (ch. 4)
- CA-4 Competing actions are fewer and quieter (ch. 4, ch. 9)
- PC-1 Descriptions are concise and lead with buyer-relevant advantages (ch. 7)
- PC-2 Key points are scannable, not buried in a paragraph (ch. 7)
- PC-3 Images show the product in enough detail to judge it (ch. 6, ch. 7)
- PR-1 Price stated openly; no charge first appears at the final step (ch. 6, ch. 7)
- PR-2 Discounts and savings shown explicitly (ch. 7)
- TR-1 Security assurance where personal or payment data is requested (ch. 8, ch. 9)
- TR-2 Privacy-policy link next to forms collecting personal data (ch. 8)
- TR-3 Returns and guarantee terms stated before purchase (ch. 9)
- TR-4 Full contact details easy to find (ch. 5, ch. 8, ch. 9)
- TR-5 Customer opinions or other third-party proof present (ch. 7)
- ER-1 Error message next to the field that caused it (ch. 8)
- ER-2 It says what is wrong and how to fix it (ch. 8)
- ER-3 Correct data is kept after an error (ch. 8)

ER criteria need an observed error-state frame; otherwise N/A, listed under Not assessed.

## 4. Score usability when applicable

Run for every task-driven interface, or when the user asks for usability. Keep these findings in a
separate table from step 3.

Source key: **M04** = Marcus 2004.

| ID | Check | Financial link | Source |
|---|---|---|---|
| US-1 | Target content or product is reachable in few steps | Lost visitors and sales | M04; LN08 ch. 5, 6 |
| US-2 | Structure is predictable; the user knows where they are | Traffic reaching converting pages | M04; LN08 ch. 5 |
| US-3 | Search returns expected items; filters narrow results | Lead and sale volume | M04; LN08 ch. 6 |
| US-4 | Data entry is short, clearly labelled, forgiving | Completions, throughput | M04; LN08 ch. 8 |
| US-5 | Errors are prevented where possible and easy to recover from | Support cost, abandonment | M04; LN08 ch. 8 |
| US-6 | A first-time user can finish the main task unaided | Productivity, support and training | M04 |
| US-7 | Usable with little or no training | Training and documentation | M04 |
| US-8 | Repeat use is at least as easy as the first | Retention, repeat revenue | M04 |

A single frame rarely proves US-1, US-6, or US-8; score them only when the flow frames are selected or
linked, otherwise mark them N/A. Neither source covers load time or accessibility; do not cite them
for those topics.

## 5. Prioritize and estimate value

Rate each Partial and Fail High / Medium / Low on:

- **Exposure:** first screen > later content > secondary state
- **Severity:** how directly it blocks the success goal
- **Effort:** work needed to fix it

Rank high-exposure, high-severity, low-effort first.

**Conversion pages** (LN08, ch. 2):

```
Revenue per month = visits × conversion rate × average value
Net gain          = revenue attributable to the change − investment
ROI (%)           = net gain ÷ investment × 100
```

**Task interfaces** (cost avoided, categories from M04):

```
Annual value = contacts or hours avoided per year × cost per contact or hour
ROI (%)      = (annual value − investment) ÷ investment × 100
```

Rules:

- Use the user's numbers only. Give a low and a high assumption, never a single point.
- Report twelve-month value and the payback month.
- Name what the model ignores: seasonality, traffic mix, price changes (LN08, ch. 2, ch. 3).
- No data, no number: write "no data — qualitative" and name the missing inputs.
- A conversion gain keeps paying on all later traffic; bought traffic pays only while it is bought
  (LN08, ch. 2). Use this when the user asks "ads or fix the page".

## 6. Report

1. **Audit frame** — frame, node ID, type, goal, users, traffic source, data, viewport and
   first-screen height.
2. **Verdict** — two sentences: biggest cost and first fix.
3. **Findings** — fewer than 15 rows; group minor issues.

   | # | ID | Finding | Layer evidence | Score | Exposure | Severity | Effort | Source |
   |---|---|---|---|---|---|---|---|---|

4. **Top three fixes** — change, expected effect, ROI range or qualitative status, assumptions.
5. **What passed** — elements a redesign should keep.
6. **Not assessed** — unobserved states and how to check them (frame to add, data to pull).
7. **Observations outside the criteria** — optional, uncited, excluded from ranking.
8. **Sources** — full references below for every cited source.

Then offer, without doing it: "Add each top finding as a comment on its layer?" Post comments only
after a yes.

### Citation rules

- Cite as author, year, chapter: `(Loveday & Niehaus 2008, ch. 8)`.
- Paraphrase; do not reproduce source passages or tables. At most one quote under 15 words.
- Statistics reported by Marcus are secondary: `(Nielsen 1997, as cited in Marcus 2004)`. They date
  from 1981–2001; never present them as current benchmarks or apply one product's figure to another.

### Failure handling

| Situation | Action |
|---|---|
| No frame selected | Ask the user to select one frame |
| No success goal | Stop and ask for it |
| Whole file or product requested | Ask for funnel or task data, then audit the frame with the largest loss |
| No value data | Audit qualitatively; name missing inputs |
| Guaranteed uplift requested | Decline; give a range and assumptions |
| Copy rewrite requested | Finish the audit, then suggest a content-design skill |

## Sources

- Loveday, L., & Niehaus, S. (2008). *Web Design for ROI: Turning Browsers into Buyers & Prospects
  into Leads.* New Riders. ISBN 978-0-321-48982-1.
- Marcus, A. (2004). *Return on Investment for Usable User-Interface Design: Examples and
  Statistics.* AM+A White Paper, version of 1 April 2004. Also published as Chapter 2 in Bias &
  Mayhew (Eds.), *Cost-Justifying Usability* (2nd ed., 2005), Morgan Kaufmann.

## About

UI ROI Audit by Monika Zapisek: [project site](https://monikazapisek.com) · [source and documentation](https://github.com/monikazapisek/design-engineering-playbook).
