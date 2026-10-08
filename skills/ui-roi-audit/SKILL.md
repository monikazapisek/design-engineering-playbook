---
name: ui-roi-audit
description: |
  Audit web pages and task-driven interfaces against source-cited conversion, usability, and ROI criteria, rank fixes by expected return, and estimate a conservative 12-month ROI when data exists. Use for ROI or conversion audits of landing, home, category, product, form, or checkout pages, including “why does this page not convert?” and “what should we fix first?”. Do not use to write copy or perform SEO, brand-voice, or WCAG compliance audits.
license: MIT
metadata:
  author: Monika Zapisek
  project: Design Engineering Playbook
  version: "2.0"
---

# UI ROI Audit

Judge one page by whether it moves a visitor toward the action the business pays for, then rank the
fixes by likely return. Taste is out of scope. A sourced finding needs a criterion ID; anything else
must be labelled as the auditor's own observation and kept out of the ranking.

## When to use

Use for “ROI audit”, “conversion audit”, “audyt ROI”, “audyt konwersji”, “why does this page not
convert?”, prioritizing page fixes by business impact, or justifying a page investment. Supported
types: landing, home, category, product, form, and checkout.

Do not use for copywriting, SEO, brand voice, WCAG compliance, or a revenue commitment. A browser
or screenshot helps but is optional; the workflow has no external dependency.

## Load on demand

| Situation | Load |
|---|---|
| Page type is known | Only that section of `references/page-type-criteria.md` |
| The conversion control is a form or checkout embedded in another page | Also load the matching form or checkout section |
| Every audit | `references/content-and-trust-criteria.md` |
| Estimating value or answering “is it worth it?” | `references/roi-model.md` |
| User requests usability, or the page is task-driven software | `references/usability-roi-module.md` |
| Before using a statistic or benchmark | `references/source-limitations.md` |
| Preparing the final report | `references/report-contract.md` |
| A format example is needed | `examples/sample-audit.md` |

Bibliography and reuse notes: `ATTRIBUTION.md`.

## Operating principles

- **Conversion before traffic.** A conversion gain applies to current and future traffic; paid
  traffic produces value only while it is bought (Loveday & Niehaus 2008, ch. 2).
- **Audit where money is lost.** Follow funnel drop-off rather than page prestige (ch. 3).
- **Evidence over taste.** Do not attach a source to an observation the criteria do not cover.
- **Conservative numbers.** Use ranges and explicit assumptions; never promise uplift.

## Required inputs

1. Page: URL, screenshot, or pasted content; one page per run.
2. Page type: landing, home, category, detail/product, form, or checkout.
3. One conversion goal: purchase, lead form, signup, call, or another observable action.
4. Traffic source for a landing page: the ad or link that sends visitors there.
5. If available: monthly visits, conversion rate, average order/lead value, implementation cost,
   and funnel drop-off.

Ask for missing items 1–3 before auditing. Without item 5, continue qualitatively and never invent
numbers.

## Procedure

### 1. Frame

State page, type, goal, audience, traffic source, data, and observed viewport. If a page mixes
types, name the primary type and any conversion-control type you will score.

**Output:** audit frame.

### 2. Inventory

Record the page in reading order: headline, value proposition, primary action, supporting content,
images, price, trust signals, navigation, forms, and observable states. Mark what is in the first
screen. Mark unavailable states as *not observed*.

**Output:** content inventory with viewport and observation limits.

### 3. Score content and page criteria

Load the relevant page-type section(s) and all cross-cutting criteria. Score each applicable item:

| Score | Meaning |
|---|---|
| Pass | Present and doing its job |
| Partial | Present but weak, buried, or contradicted |
| Fail | Missing or working against the goal |
| N/A | Not applicable or not observable |

**Output:** scored criteria table; every Partial and Fail has page evidence.

### 4. Score usability when applicable

For a requested usability review or task-driven interface, load the usability module and keep its
findings separate from content findings.

**Output:** separate usability table, or a note that the module was not run.

### 5. Prioritize and estimate value

Rate each Partial and Fail High / Medium / Low on:

- **Exposure:** how much traffic meets it; first screen > later content > secondary state.
- **Severity:** how directly it blocks the conversion goal.
- **Effort:** work needed to fix it.

Rank high-exposure, high-severity, low-effort gaps first. If the user supplied the required numbers,
load the ROI model and calculate a conservative 12-month range for the top fixes. Otherwise state
“no data — qualitative” and name the missing inputs.

**Output:** ranked top three with ROI range or qualitative status.

### 6. Report

Load `references/report-contract.md`, follow its output contract, citation rules, failure handling,
and final checklist.

**Output:** complete audit report.

## Anti-patterns

- Treating a general best practice as if either source stated it.
- Scoring an unobserved error, mobile, or post-submit state as a failure.
- Turning a scenario assumption into a benchmark or guaranteed uplift.
- Auditing an entire site when funnel data can identify the page with the largest loss.
- Drafting replacement copy inside the audit; hand that work to a content-design workflow.

## Related skills

- `ux-content-design` — drafts copy after the audit.
- `kano-model-strategist` — decides whether a feature should exist.
- `socratic-dialogue` — stress-tests ROI assumptions.

## Framework credits

Built on Loveday & Niehaus (2008) and Marcus (2004). See `ATTRIBUTION.md` for the full bibliography,
verification notes, and reuse rules.
