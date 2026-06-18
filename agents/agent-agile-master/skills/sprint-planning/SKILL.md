---
created: 2026-06-18
updated: 2026-06-18
version: 1.2
description: Sprint planning ceremony — step-by-step for solo practitioner
agent: agent-agile-master
attribution: ATTRIBUTION.md
extends: ../../AGENT.md
---

# Sprint Planning

## Purpose

Decide what to build in the next sprint. For solo: clarify goals, select items from backlog, break into tasks, set definition of done.

## When to run

- Start of every sprint (weekly in ultra-lean)
- When backlog is messy and needs structure
- When starting a new feature/project

## Duration

- **Solo:** 30-45 minutes
- **With context:** up to 60 minutes

## Knowledge to load (on demand)

| Situation | Reference |
|---|---|
| Need estimation help | Cohn, *Estimating With Story Points* (Modules 1-2) — Mountain Goat Software |
| Need story splitting help | Cohn, *Better User Stories* (Modules 1-2) — Mountain Goat Software |
| Need sprint length guidance | Cohn, *Scrum Repair Guide* (Module 3: Sprinting) — Mountain Goat Software |
| Need planning context | Gothelf & Seiden, *Lean UX* — collaborative design, MVPs |

**Reguła:** load only the specific module/section needed, not the full course.

## Step-by-step

### Step 1: Context Review (5 min)

Read current state:
- What's in the backlog?
- What's the project's current focus? (Check `strategy/` or `memory/decisions.md`)
- Any blockers from last retro?

Output: "Current state: [1-2 sentences]"

### Step 2: Sprint Goal (5 min)

Answer: **"What's the one thing that makes this sprint successful?"**

For solo, this is critical — without a team to distribute work, focus is everything.

Format: "This sprint I will [concrete outcome] so that [reason]."

Examples:
- "This sprint I will ship the Button component spec so that I can start selling it."
- "This sprint I will complete the token mapping for 3 components so that code generation works."

### Step 3: Backlog Selection (10 min)

From the backlog, select items that serve the sprint goal.

**Selection criteria:**
1. Directly serves sprint goal? → Must have
2. Enables future work? → Nice to have
3. "Would be cool"? → Parking lot (defer)

**For solo:** max 3-5 items per sprint. Less is more.

**Estimation (if needed):**
- Use t-shirt sizing (XS/S/M/L/XL) for quick relative sizing
- Story points only if you have velocity history
- If no history: just sequence by priority, don't estimate yet

### Step 4: Task Breakdown (10 min)

For each selected item, break into tasks:

**Task format:**
```
[ ] Task description (owner: me, estimated: X hours/days)
```

**Rules:**
- Max 2 days per task. If bigger → split further.
- Each task should produce something visible (code, spec, design)
- Include "done" criteria per task

### Step 5: Definition of Done (5 min)

For this sprint, what does "done" mean?

**Component-level DoD (for design-handoff-lab):**
- [ ] Spec.md written
- [ ] Tokens JSON generated
- [ ] React/HTML code working in Storybook
- [ ] Figma source reference documented
- [ ] Changelog updated

**Sprint-level DoD:**
- [ ] All selected items completed
- [ ] Retro completed
- [ ] Backlog updated with learnings

### Step 6: Commit (5 min)

Write sprint commitment to `memory/decisions.md` or project tracking:

```
## Sprint [N] — [date]
Goal: [one sentence]
Items: [list]
DoD: [confirmed]
```

## Anti-patterns to watch

- **Too many items.** If you select >5 items for a solo sprint, you're dreaming. Cut to 3.
- **No sprint goal.** Without a goal, you're just doing random tasks. Always have one.
- **Skipping estimation.** Even rough sizing prevents overcommitment.
- **No task breakdown.** "Build feature X" is not a task. Break it down.
- **Planning too long.** 45 min max for solo. If it takes longer, your backlog needs refinement first.

## After planning

- Start working on item #1 immediately
- Daily check-in (5 min self-scrum): "What did I do? What's next? Any blockers?"
- Track actual vs planned for velocity building

---

## Framework Credits

Ten skill korzysta z frameworków i koncepcji opisanych w
[ATTRIBUTION.md](../../ATTRIBUTION.md):
- **Scrum Guide (Schwaber & Sutherland)** — sprint, sprint goal, DoD
- **Agile Estimating and Planning (Cohn)** — velocity, relative sizing
- **Planning Poker (Grenning)** — Fibonacci-scale estimation
- **Better User Stories (Cohn)** — story splitting, INVEST
