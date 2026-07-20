# figjam-storymap-llm

> Turn a FigJam Story Map (Jeff Patton methodology) into LLM-readable Markdown / JSON — without manual transcription, without OCR hallucinations, without losing spatial semantics.

[![License: MIT](./LICENSE)](./LICENSE)

An **Agent Skill** that audits and parses FigJam User Story Maps into a deterministic backlog format for Notion / Linear / Jira, or as context for coding agents (Cursor, Claude Code, Copilot).

This is the GitHub-facing landing page. The agent-facing working document is [`SKILL.md`](./SKILL.md).

## Why

After a Story Mapping workshop, the team typically transcribes hundreds of sticky notes by hand into Jira / Linear. That is the worst kind of waste: workshop intent gets lost, the spatial semantics of the map are flattened, and the backlog drifts away from what was actually agreed.

**This skill eliminates the transcription step.** It reads the FigJam board via Figma REST API (deterministic, no OCR) and renders a structured Markdown / JSON backlog preserving:

- Activity → Task → User Story hierarchy (Patton backbone)
- Release slicing (V1 / V2 / V3)
- Acceptance Criteria inline with each story
- Owner and priority (V1 only — Lean UX rule)
- Connector relationships (dependencies, blockers, branching)

## Structure

```
figjam-storymap-llm/
├── SKILL.md                          # Agent-facing working document (required)
├── LICENSE                           # MIT
├── README.md                        # This file (GitHub landing page)
├── references/
│   ├── llm-ready-figjam-guidelines.md   # Condensed guidelines + industry sources
│   ├── system-prompt.md                 # System Prompt for AI agent (audit + synthesis)
│   └── figjam-template-spec.md          # Canonical FigJam template spec + checklist
└── scripts/
    └── figjam_parser.py                # Python parser (Figma REST API → Markdown / JSON)
```

## Quick start

### Option A — Run the parser (CLI)

```bash
pip install requests
export FIGMA_TOKEN=your_figma_personal_access_token

python scripts/figjam_parser.py \
  --file-key qCvyzr7Ucf7jcWJsWljluF \
  --token $FIGMA_TOKEN > story-map.md

# JSON output for PM tooling import
python scripts/figjam_parser.py \
  --file-key qCvyzr7Ucf7jcWJsWljluF \
  --token $FIGMA_TOKEN --format json > story-map.json
```

### Option B — Use as an Agent Skill

Copy this folder into your `.agents/skills/` directory (or `.claude/skills/` for Claude Code). Then load it on demand:

- **Claude Code CLI:** tell Claude "load the figjam-storymap-llm skill and audit my FigJam board"
- **Cursor / Copilot:** paste `SKILL.md` + `references/system-prompt.md` as project context

### Option C — Audit a board (no parsing)

Paste the `references/system-prompt.md` content as System Instructions, then share a screenshot of your FigJam board (or JSON). The agent returns an LLM-readiness audit.

## Canonical FigJam template

```
[STORY_MAP]                                    ← root SECTION (wrapper)
├── [00_SECTION_AI_Readme]                      ← embedded system prompt + legend
├── [USER_SEGMENT_or_PERSONA]                   ← persona
├── [01_SECTION_BACKBONE_Activities]             ← [ACT_01] Activity, [ACT_02] Activity
├── [02_SECTION_BACKBONE_User_Tasks]            ← [TASK_01] Task, [TASK_02] Task, ...
├── [03_SECTION_Release_1] Core Value Proof     ← V1 (full taxonomy: [P*], @Owner, AC)
├── [04_SECTION_Release_2] Business Goal ...    ← V2 (clean — no [P*], no @Owner)
└── [05_SECTION_Release_3] Business Goal ...    ← V3 (clean — no [P*], no @Owner)
```

Full template spec (colors, typography, sticky syntax, connectors): see [`references/figjam-template-spec.md`](./references/figjam-template-spec.md).

## How the X-axis mapping works

FigJam does not support 2D section grids (Section × Section). So:

- **Sections for releases** (rows on Y axis): `[03_SECTION_Release_1]`, `[04_SECTION_Release_2]`, ...
- **Chronology encoded in X position** of `[TASK_*]` backbone cards
- **Stories mapped to tasks algorithmically:**

  ```
  for each [STORY] sticky:
    center_x = sticky.x + sticky.width / 2
    find [TASK] whose range (task.x .. task.x + task.width) contains center_x
    fallback: nearest task center on X axis
  ```

You can drag stories around freely in the FigJam workshop without editing any IDs — the parser tracks the column automatically.

## Methodology

This skill adapts and combines:

- **Jeff Patton — User Story Mapping** (O'Reilly, 2014) — Backbone + Slices + Walking Skeleton
- **Gothelf & Seiden — Lean UX** (2013) — Hypothesis-driven, no Big Upfront Design in V2 / V3
- **Mike Cohn — User Stories Applied** (2004) — INVEST, AC inline
- **Figma REST API** — Node types (SECTION, STICKY, SHAPE_WITH_TEXT, CONNECTOR)
- **Anthropic Vision Guidelines** — Layout & spatial data in Vision LLM prompts
- **tldraw / Make Real** — Open-source canvas-to-JSON architecture reference

## Industry references

- Figma REST API: https://www.figma.com/developers/api
- Anthropic Vision: https://docs.anthropic.com/en/docs/build-with-claude/vision
- tldraw (canvas-to-JSON reference): https://github.com/tldraw/tldraw
- Jeff Patton — User Story Mapping: https://www.jpattonassociates.com/user-story-mapping/

## License

MIT — see [`LICENSE`](./LICENSE).

## Trademarks

FigJam and Figma are registered trademarks of Figma, Inc. This project is an independent open-source tool and is not affiliated with, endorsed by, or sponsored by Figma, Inc. The name "figjam" in the repository and skill identifiers is used for nominative fair use — to describe compatibility with the FigJam platform.