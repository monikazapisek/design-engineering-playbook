# gestalt-ui-audit

Audit one interface screen against nine Gestalt principles and find where the groups people see
differ from the structure the screen intends.

## What it does

- Maps the groups the eye perceives and compares them with the intended structure
- Names each mismatch: false group, split group, wrong owner, flat hierarchy
- Scores proximity, similarity, common region, uniform connectedness, continuity, closure,
  figure/ground, common fate, and Prägnanz as Pass, Partial, Fail, or Not assessed
- Predicts which cue wins when two principles conflict
- Ranks layout fixes by severity and effort

## What it does not do

- Check exact spacing values against a grid
- Audit conversion, ROI, copy, or WCAG compliance
- Judge motion or interactive states from a static screenshot
- Give an overall score

## Files

| File | Purpose |
|---|---|
| `SKILL.md` | Procedure, inputs, failure handling, quality checklist |
| `references/principles.md` | Definitions, tests, and typical violations for each principle |
| `references/principle-conflicts.md` | What happens when two principles compete |
| `references/report-contract.md` | Report structure and citation rules |
| `examples/sample-audit.md` | A blind run on a synthetic dashboard, judged against a hidden answer key |
| `EVIDENCE.md` | What was tested and what was not |
| `ATTRIBUTION.md` | Bibliography and reuse notes |
| `INSTALL.md` | Installation for Claude Code, Claude web/chat, and Cowork |
| `figma/gestalt-ui-audit.md` | Single-file version for the Figma agent: audits a selected frame, report only |
| `LISTING.md` | Figma Community listing copy |

## Example prompts

- "Run a Gestalt audit on this dashboard screenshot."
- "Why does this settings page feel cluttered? Check the grouping."
- "Is it clear which label belongs to which field in this form?"
- "Audit the selected frame for proximity and similarity problems."

## Sources

Built on Wertheimer (1923), Rubin (1915), Koffka (1935), Palmer (1992), Palmer & Rock (1994),
Quinlan & Wilton (1998), and Wagemans et al. (2012). See `ATTRIBUTION.md`.

## Status

Version 1.0, draft: not ready to publish. See `EVIDENCE.md` for the tests run and the gates still
open.

## Author and project

- **Author:** [Monika Zapisek](https://monikazapisek.com)
- **Project:** Design Engineering Playbook

## License

MIT for the skill's own text and structure. The cited works remain under their authors' copyright.
