# ClawHub Submission Package

**Created:** 2026-06-30
**Source author:** Monika Zapisek
**Project:** Design Engineering Playbook (`monikazapisekstudio/design-engineering-playbook`)
**Submission target:** https://clawhub.ai/submit (manual submission — `hermes skills publish --to clawhub` is not yet implemented in hermes CLI; it only prints the URL)

## Why this file

The hermes CLI's `publish --to clawhub` subcommand is not yet implemented in the version installed locally (Hermes Agent v0.17.0). The CLI prints the manual URL and exits. This file is the bridge: it pre-stages everything you need to do the manual submission efficiently — three zips, three pre-filled form payloads, and a step-by-step checklist.

## Pre-flight: what's in the package

| File | Path | Status |
|---|---|---|
| Zip 1 | `publishing/clawhub/legible-agent-output.zip` | ✅ Hermes scan: SAFE |
| Zip 2 | `publishing/clawhub/kano-model-strategist.zip` | ✅ Hermes scan: SAFE |
| Zip 3 | (skipped — socratic-dialog blocked by hermes scan, see below) | ❌ DANGEROUS verdict |

### Why socratic-dialog was skipped

`hermes skills publish` self-scans before publish. socratic-dialog came back with a **DANGEROUS** verdict (4 CRITICAL persistence findings in `README.md` lines 79, 87, 171, 174 — installation instructions referencing `AGENTS.md` and `~/.codex/skills/`, which the scanner flags as potential agent-environment persistence). The scanner does not allow `--force` override on DANGEROUS verdicts (`--force does not override a dangerous verdict`, hermes source `hermes_cli/skills_hub.py`).

Two options if you want socratic-dialog on ClawHub later: (1) move the installation instructions to a separate `INSTALL.md` and have `README.md` reference it instead of containing the persistence patterns, or (2) rephrase the install steps to avoid the literal `AGENTS.md` and `~/.codex/skills/` strings. Both are 5-minute edits; flag if you want me to do them.

---

## Skill 1 — legible-agent-output

### Hermes scan result

```
Scanning 'legible-agent-output' before publish...
Scan: legible-agent-output (self/community)  Verdict: SAFE
Decision: ALLOWED — Allowed (community source, safe verdict)
```

(Verified 2026-06-30, after fixing a path-traversal finding in `SKILL.md:188` that originally had `../../../LICENSE`. Commit `c97a99c` in the playbook repo.)

### Pre-filled form fields

| Form field | Value |
|---|---|
| **Skill name** | `legible-agent-output` |
| **Short description** (1-2 sentences) | Force every user-facing string from an AI agent to be readable by a non-technical human without external context. Replaces opaque codes (A127, ENOENT), framework jargon, raw error strings, and bare percentages with plain-language titles, status messages, and error descriptions. |
| **Long description** | (paste the full `description:` block from `SKILL.md` frontmatter — lines 3-4) |
| **Version** | `1.0` |
| **Author** | `Monika Zapisek` |
| **Project** | `Design Engineering Playbook` |
| **License** | `MIT` |
| **Repository URL** | `https://github.com/monikazapisekstudio/design-engineering-playbook/tree/main/skills/legible-agent-output` |
| **Source folder** | `skills/legible-agent-output/` |
| **Tags** (suggested) | `agent-ux`, `plain-language`, `anti-jargon`, `user-facing`, `legibility`, `output-contract`, `claude-skill`, `design-engineering` |
| **Category** (suggested) | `software-development` or `agent-orchestration` |
| **Compatibility** | Tested with: Claude Sonnet 4.5 (Mavis / Claude Code). Designed for: Claude Code, Codex, VS Code, OpenCode, Cursor, GitHub Copilot. |
| **Dependencies** | None (no MCP, no external services, no network) |
| **Trigger phrases** (for the search engine) | `agent uses cryptic codes`, `agent output is illegible`, `task titles are opaque`, `too much jargon in plan`, `agent said A127`, `what does this code mean?` |
| **Do NOT use for** (per the skill's own description) | backend logging, developer-only output, internal RPC payloads, debug dumps, system-to-system messages |

### Upload artifacts

- **Zip:** `publishing/clawhub/legible-agent-output.zip` (contains the full skill: `SKILL.md`, `ATTRIBUTION.md`, `EVIDENCE.md`, `LICENSE`, `SYNCHRONIZATION.md`, `references/`, `examples/`)
- **Source URL** (alternative to uploading zip): `https://raw.githubusercontent.com/monikazapisekstudio/design-engineering-playbook/main/skills/legible-agent-output/SKILL.md`

### Notes for the reviewer

- Path B eval (5-point rubric) recorded in `EVIDENCE.md`. Verdict: **PASS** (with-skill wins 1 outright on error translation — caught a real file-path leak in the senior baseline).
- 6 published UX-research sources, all verified 2026-06-30. Full attribution chain in `ATTRIBUTION.md`.
- Synthesis note: this skill's descriptive terms (`plain-language action preview`, `legible agent state`) are coined for naming convenience; the literature uses `Intent Preview` (Smashing Magazine) and `Invisible actions` / `Unclear state` (Hatchworks). The two pairs map 1:1.
- MIT license; safe to redistribute; please keep the `ATTRIBUTION.md` and `LICENSE` files when forking.

---

## Skill 2 — kano-model-strategist

### Hermes scan result

```
Scanning 'kano-model-strategist' before publish...
Scan: kano-model-strategist (self/community)  Verdict: SAFE
Decision: ALLOWED — Allowed (community source, safe verdict)
```

(Verified 2026-06-30. No fixes needed — this skill was already lint-clean.)

### Pre-filled form fields

| Form field | Value |
|---|---|
| **Skill name** | `kano-model-strategist` |
| **Short description** (1-2 sentences) | Classify product features into Kano categories (Must-be / Performance / Attractive / Indifferent / Reverse) and prune the backlog to prevent Experience Rot. Forces a "Start with NO" stance on new features. |
| **Long description** | (paste the full `description:` block from `SKILL.md` frontmatter — lines 3-10) |
| **Version** | `1.1` |
| **Author** | `Monika Zapisek` |
| **Project** | `Design Engineering Playbook` |
| **License** | `MIT` |
| **Repository URL** | `https://github.com/monikazapisekstudio/design-engineering-playbook/tree/main/skills/kano-model-strategist` |
| **Source folder** | `skills/kano-model-strategist/` |
| **Tags** (suggested) | `kano-model`, `feature-prioritization`, `mvp-vs-mdp`, `experience-rot`, `backlog-pruning`, `product-strategy`, `claude-skill`, `design-engineering` |
| **Category** (suggested) | `product-management` or `software-development` |
| **Compatibility** | Tested with: Claude Sonnet 4.5 (Claude Code), GPT-5.5, MiniMax-m3, GitHub Copilot. Designed for: Claude Code, Codex, VS Code, OpenCode. |
| **Dependencies** | None (no MCP, no external services, no network) |
| **Trigger phrases** (for the search engine) | `kano`, `feature pruning`, `should we build this feature`, `cut features`, `is this a must-have`, `is this delight`, `ultra-lean backlog review`, `MDP vs MVP`, `start with NO` |
| **Do NOT use for** (per the skill's own description) | general project management, Gantt charts, non-feature design decisions (visual polish, copy editing) |

### Upload artifacts

- **Zip:** `publishing/clawhub/kano-model-strategist.zip` (contains the full skill: `SKILL.md`, `ATTRIBUTION.md`, `EVIDENCE.md`, `LICENSE`, `SYNCHRONIZATION.md`, `references/`)
- **Source URL** (alternative to uploading zip): `https://raw.githubusercontent.com/monikazapisekstudio/design-engineering-playbook/main/skills/kano-model-strategist/SKILL.md`

### Notes for the reviewer

- Path B eval (5-point rubric) recorded in `EVIDENCE.md`. Verdict: with-skill wins 2 (procedural adherence + output contract compliance), ties 3. Senior baseline was already strong; the skill's value is in *consistent* output structure, not in making the model smarter.
- Primary academic source: Kano, N. (1984), *Attractive Quality and Must-be Quality*, Hinshitsu / Journal of the Japanese Society for Quality Control, 14(2), 39–44. The Kano model itself is a published academic framework and is not copyrightable; only specific expressions of it are. The wording in this skill is original.
- Practitioner source attribution: Jared Spool's UX strategy work on Kano prioritization.
- MIT license; safe to redistribute; please keep the `ATTRIBUTION.md` and `LICENSE` files when forking.

---

## Step-by-step manual submission

For each of the 2 skills above:

1. Open `https://clawhub.ai/submit` in your browser.
2. Sign in (or create a ClawHub account if you don't have one yet).
3. Click **Submit a new skill**.
4. Fill in the form fields by copying the values from the "Pre-filled form fields" table above.
5. For the file upload, either:
   - Upload the corresponding zip from `publishing/clawhub/<skill-name>.zip`, OR
   - Provide the **Source URL** listed in "Upload artifacts" (clawhub can pull from GitHub).
6. Add any reviewer notes from the "Notes for the reviewer" section.
7. Submit. ClawHub will review the submission and either approve or request changes.
8. After approval, the skill will be discoverable via `hermes skills search <name> --source clawhub` for any hermes user.

### Expected review timeline

Per clawhub's review process (estimate, not contractual): 3-7 days for community-source skills. Faster if the review queue is short. The hermes scan that already ran (SAFE verdict) should help — it shows the skill has passed hermes's own security check.

---

## After submission

When both skills are live on ClawHub, update the playbook README to reflect it. Suggested addition to `README.md` History section:

```
* **2026-06-30** — Published legible-agent-output and kano-model-strategist to
  [ClawHub](https://clawhub.ai) for hermes users. (socratic-dialog deferred
  until AGENTS.md persistence findings are addressed.)
```

And add to `integrations/README.md` (already done for `legible-agent-output`, kano would be added in a follow-up commit if you want).
