# Changelog — figjam-storymap-llm

All notable changes to this skill are documented here.
Format follows [Keep a Changelog](https://keepachangelog.com/en/1.1.0/) and semantic versioning.

## v1.1.0 — 2026-07-20

### Parser bug fixes (`scripts/figjam_parser.py`)

- `get_color` now correctly extracts `#RRGGBB` from Figma API `fills[].color` dict (was returning None)
- `is_release_section` now supports any release index via regex (was hardcoded to `[03_` / `[04_` / `[05_`)
- `map_tasks_to_activities` implemented (was dead code) — X-axis overlap mapping, like story → task
- `ActivityItem` got `x / y / width / height` fields for positional mapping
- Added retry with exponential backoff on Figma API 429 / 5xx
- Added clear error messages for 403 (token expired), 404 (wrong file_key), missing token / file-key
- Added `X_MAPPING_MAX_DISTANCE_PX = 400` threshold — distant stories now flag as `UNASSIGNED` instead of being force-mapped
- Forced UTF-8 stdout / stderr on Windows to avoid `cp1252` `UnicodeEncodeError` (FigJam uses `\u2028` LINE SEPARATOR)
- Strip emoji from sticky text (priority tags like `[💓P1]` → `[P1]`, decorative emoji removed)
- Normalize newlines in task / activity names via `clean_name` helper (`[TASK_01]\nTask` → `[TASK_01] Task`)
- BOM-tolerant JSON input reading (`utf-8-sig`) — PowerShell `Set-Content -Encoding UTF8` no longer crashes the parser
- Handle `FileNotFoundError` and `JSONDecodeError` for `--input` mode with clear error messages

### Taxonomy & spec changes

- AC marker changed from `AC:` to `Acceptance Criteria:` across all skill files (parser, spec, AI Readme, system prompt)
- Owner tags aligned to `@UX @DEV @PM @QA` consistently (removed stray `@BIZ` from parser regex + guidelines)

### New content

- Expanded `[00_SECTION_AI_Readme]` block: parsing procedure (9 steps), output format, "what not to do" (8 prohibitions), expanded FLAG list (10 anti-patterns with smallest concrete fix)
- Added `RECOMMENDED READING` section (Patton, Cohn, Torres, Perri, Gothelf & Seiden)
- Added `references/figjam-executive-summary.md` — human-facing canvas cover page (Executive Summary + ClawHub + GitHub links + Recommended Reading)
- Cross-referenced published FigJam Community template: https://www.figma.com/community/file/1661156551667594442

### Honesty pass

- Corrected misleading "parser outputs Notion / Jira backlog" claims. Parser produces Markdown + JSON only. Notion / Jira / Linear are downstream conversions the user does themselves (manually or via MCP). Added explicit value statement: "no information loss, with legend, following industry best practices (Patton, Cohn, Lean UX)"
- Updated `[TEMPLATE_META]` GitHub URL to new handle (`monikazapisek` instead of `monikazapisekstudio`)

### Translation

- Translated all Polish comments / docstrings / argparse help in `figjam_parser.py` to English
- Translated Polish `(legenda, instrukcje)` in system-prompt tree diagram to English

## v1.0.0 — 2026-07-20

### Initial release

- FigJam Story Map parser (Figma REST API → Markdown / JSON)
- Canonical FigJam template spec (colors, typography, sticky syntax, connectors, pre-publish checklist)
- System prompt for AI agent (audit mode + synthesis)
- Map Structure Guardian (active coach for Patton + Cohn INVEST rules)
- Lean UX rules baked in (V1 tagged, V2 / V3 clean)
- MIT license