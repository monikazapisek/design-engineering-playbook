# NotebookLM Guide: Design Engineering Playbook Asset Finder

Use this file as a reusable NotebookLM source when analyzing notes, transcripts,
research, workshop outputs, project docs, or existing AI instructions. Its job is
to help NotebookLM identify which content should become a reusable asset in the
Design Engineering Playbook.

The Design Engineering Playbook is an AI-native workspace for senior product
designers, design engineers, and AI-assisted product teams. It turns real product
work into reusable, public-safe methods, workflows, agents, skills, commands,
rules, prompts, templates, tools, and integrations.

## How NotebookLM Should Use This Source

When reviewing any notebook sources, classify reusable content into one of these
asset types:

| Asset type | Use when the source contains | Do not use when |
|---|---|---|
| `playbook/` | Long-form methodology, principles, strategy, operating models, or conceptual frameworks | The content is only a step-by-step reusable workflow |
| `skills/` | A repeatable AI workflow that teaches an assistant how to perform one specific task | The content is a one-off note, generic advice, or private context |
| `agents/` | A reusable AI role with its own scope, identity, decision authority, and operating style | The content is only a procedure inside an existing role |
| `rules/` | Always-on guardrails, constraints, quality rules, or non-negotiable operating standards | The content is a situational workflow |
| `commands/` | A repeatable command-style action an agent can run on demand | The content is broad methodology or a role definition |
| `prompts/` | Copy-paste prompt patterns for human use with AI tools | The content needs a full workflow, tests, or runtime discovery |
| `doc-templates/` | Reusable project artifacts, document structures, checklists, or working templates | The content is mainly instructions for an AI runtime |
| `tools/` | Scripts, validators, converters, checkers, or small helpers | The content can be handled with plain instructions |
| `integrations/` | Setup guides and workflows for external tools and platforms | The content is tool-agnostic methodology |

NotebookLM should not try to force every useful idea into a skill or agent. The
default should be: choose the smallest reusable asset that preserves the source's
real value.

## Public Safety Rules

All proposed assets must be safe to publish.

Reject or sanitize any candidate that contains:

- client data
- private project details
- personal notes
- secrets, tokens, credentials, API keys, or environment variables
- private filesystem paths
- proprietary material copied without permission
- claims that cannot be supported by the available sources

Use generic examples unless the source clearly has publication permission.

## Repository Source Of Truth

Use these repo conventions when deciding where content belongs:

- `README.md` is the public positioning source of truth.
- `playbook/` is for long-form methodology.
- `skills/` is for reusable AI workflows.
- `rules/` is for operating guardrails.
- `commands/` is for repeatable agent actions.
- `prompts/` is for copy-paste prompt patterns.
- `doc-templates/` is for reusable project artifacts.
- `agents/` is for role definitions.
- `tools/` is for scripts and helpers.
- `integrations/` is for setup guides and external tool workflows.

Prefer practical, reusable, senior-level material over generic AI advice.

## Decision Tree

Use this routing logic before proposing an asset.

1. Is it a durable method or operating model?
   - Yes: propose `playbook/`.
2. Is it a repeatable procedure an AI assistant can execute?
   - Yes: propose `skills/`.
3. Does it define a role with scope, voice, decision authority, and boundaries?
   - Yes: propose `agents/`.
4. Is it a hard operating constraint that should apply across work?
   - Yes: propose `rules/`.
5. Is it a named action that should be run on demand?
   - Yes: propose `commands/`.
6. Is it mainly a reusable prompt for a human to paste into an AI tool?
   - Yes: propose `prompts/`.
7. Is it a reusable document shape or project artifact?
   - Yes: propose `doc-templates/`.
8. Is it executable or validation logic?
   - Yes: propose `tools/`.
9. Is it about configuring or using an external platform?
   - Yes: propose `integrations/`.
10. If none apply, classify it as `not reusable yet` and explain what evidence is missing.

## Skill Quality Requirements

Create a skill only when the same procedure, checklist, review process, or
multi-step workflow will be reused.

A good skill has:

- one clear job
- two or three concrete use cases before writing
- specific trigger phrases in `description`
- explicit "use when" and "do not use when" guidance
- expected inputs and outputs
- actionable steps, not an essay
- progressive disclosure: short `SKILL.md`, longer material in `references/`
- a quality checklist
- trigger tests with at least five realistic user queries
- edge-case tests
- public-safe examples
- attribution when it uses external frameworks or sources
- evidence of testing and quality gates

Do not create a skill for:

- one-off notes
- generic advice
- random prompts
- private project context
- content that should be a simple prompt or document template
- content that duplicates an existing skill

Recommended skill folder:

```text
skills/
└── skill-name/
    ├── SKILL.md
    ├── references/
    ├── examples/
    └── scripts/
```

Only `SKILL.md` is required. Do not create empty optional folders unless the
asset needs them.

Recommended portable `SKILL.md` frontmatter:

```yaml
---
name: kebab-case-skill-name
description: |
  Specific one- to three-sentence trigger description. Say what the skill does,
  when to use it, and when not to use it.
license: MIT
compatibility: |
  Designed for Claude Code, OpenCode, Codex CLI, VS Code + GitHub Copilot.
metadata:
  author: Monika Zapisek
  project: Design Engineering Playbook
  version: "1.0"
  status: draft
---
```

Skill readiness checklist:

- `name` matches folder name
- folder name is kebab-case
- description is specific and under 1024 characters
- one skill equals one responsibility
- no hidden dependency on private files or services
- no external MCP or API dependency unless declared and justified
- body is lean enough for agent use
- references are loaded only when needed
- every workflow step has a concrete output
- evidence file records tests, edge cases, and quality gates
- root README index is updated only when the asset is ready for publication

## Agent Quality Requirements

Create an agent when the content describes a reusable role, not just a workflow.

An agent is appropriate when the source includes:

- a domain and identity
- clear scope
- clear anti-scope: what the agent is not
- decision authority
- voice or operating style
- workflows the role can run
- routing rules to other roles, skills, or sources
- rules for when to act autonomously, suggest, or ask first

Do not create an agent when the source only explains how to do one task. That is
usually a skill.

Recommended agent folder:

```text
agents/
└── agent-name/
    ├── AGENT.md
    ├── PERSONA.md
    ├── EVIDENCE.md
    ├── ATTRIBUTION.md
    └── skills/
```

Only include files the role actually needs.

An `AGENT.md` should include:

- what this agent is
- what this agent is not
- scope
- framework or approach
- workflows
- decision authority
- related skills, rules, commands, and sources

A `PERSONA.md` is useful only when the agent needs a distinct voice, hard rules,
or anti-persona.

Agent readiness checklist:

- the role cannot be reduced to a single workflow
- scope is narrow enough to prevent role creep
- "not this agent" cases are explicit
- decision authority includes what it can do alone, what it can suggest, and what it must ask about
- workflows have clear triggers
- no private paths or unpublished context
- compatibility requirements are explicit

## Rule Quality Requirements

Create a rule when a constraint should guide many tasks, agents, or workflows.

A good rule is:

- short
- enforceable
- written in imperative language
- tied to a failure mode
- easy to test during review
- clear about exceptions

Good rule candidates often contain phrases like:

- "always"
- "never"
- "must"
- "do not"
- "before publishing"
- "before editing"
- "when reviewing"
- "reject if"

Do not turn a whole methodology into a rule. Extract only the guardrail.

## Command Quality Requirements

Create a command when the source describes a repeatable action that an agent
should run on demand.

A good command includes:

- command name
- purpose
- inputs
- pre-checks
- ordered steps
- expected output
- verification
- failure handling

Command candidates often begin with verbs:

- audit
- review
- generate
- compare
- convert
- validate
- prepare
- publish
- sync

Do not create a command for broad strategic thinking. That belongs in
`playbook/`, `skills/`, or `agents/`.

## Prompt Pattern Quality Requirements

Create a prompt when the value is a copy-paste interaction pattern for a human.

A good prompt pattern includes:

- when to use it
- the prompt text
- placeholders
- expected answer shape
- follow-up prompts
- quality checks for the user

Do not create a prompt when the workflow needs multiple steps, references,
testing, or runtime discovery. That is probably a skill.

## Document Template Quality Requirements

Create a document template when the source describes a reusable project artifact.

A good document template includes:

- artifact purpose
- intended audience
- sections
- required fields
- optional fields
- completion criteria
- examples of good entries
- anti-patterns

Document templates are for artifacts humans and agents fill in repeatedly:
briefs, audits, specs, handoff docs, planning docs, case studies, checklists, and
retrospective notes.

## Playbook Quality Requirements

Create playbook content when the source explains a durable method, not a
runtime-specific instruction.

Good playbook content:

- explains why the method exists
- gives principles and tradeoffs
- includes practical operating guidance
- uses examples from generic or public-safe scenarios
- links to related skills, rules, commands, prompts, or templates
- avoids vendor-specific assumptions unless the section is explicitly about a tool

Do not use `playbook/` for raw prompt snippets, command recipes, or single-task
agent workflows.

## Integration Quality Requirements

Create integration content when the source explains how to configure or operate
an external tool or platform.

A good integration guide includes:

- tool name
- supported use cases
- prerequisites
- setup steps
- verification steps
- common failure states
- security notes
- maintenance notes

Keep integrations separate from general methodology. For example, "how to use
Figma MCP in a workflow" is integration content; "how to review design-system
component quality" is playbook, skill, or command content.

## Evidence And Testing Requirements

Before proposing an asset as "ready", NotebookLM should check whether the source
contains enough evidence to support it.

Minimum evidence for a skill or agent:

- at least two realistic use cases
- at least five trigger or invocation examples
- at least one near-miss case where it should not trigger
- expected output shape
- edge cases or failure modes
- public-safe examples
- source attribution if external methods are used
- compatibility assumptions

If the evidence is missing, mark the asset as `candidate`, not `ready`.

Readiness labels:

| Label | Meaning |
|---|---|
| `ready` | Enough source material exists to draft the asset now |
| `candidate` | The idea is reusable, but examples, triggers, tests, or evidence are missing |
| `merge with existing` | The source belongs inside an existing asset |
| `prompt only` | Useful, but too small for a skill or command |
| `not reusable yet` | Interesting source, but no repeatable pattern is visible |
| `reject` | Private, unsafe, duplicate, unsupported, or too generic |

## NotebookLM Output Format

When asked to analyze sources, NotebookLM should answer with this structure.

```markdown
# Reusable Asset Opportunities

## Strong Candidates

| Candidate | Asset Type | Why It Fits | Source Signals | Proposed Location | Status |
|---|---|---|---|---|---|

## Needs More Evidence

| Candidate | Missing Evidence | What To Ask Or Collect Next | Status |
|---|---|---|---|

## Do Not Convert

| Source Pattern | Reason | Better Use |
|---|---|---|

## Draft Asset Briefs

### [asset-name]

- Type:
- Proposed location:
- Job:
- Use when:
- Do not use when:
- Inputs:
- Outputs:
- Required files:
- Evidence needed:
- Risks:
- Related existing assets:
```

NotebookLM should keep recommendations concrete. Avoid vague outputs like "make
this a skill about strategy". Name the actual workflow, trigger, output, and
quality bar.

## Anti-Patterns

Reject these patterns:

- generic AI advice with no unique method
- "mega-skill" that combines multiple jobs
- agent with no decision authority
- skill with no trigger phrases
- command with no verification step
- rule that is too broad to enforce
- prompt that secretly requires a multi-step workflow
- playbook section that is just a long prompt
- private project notes disguised as methodology
- external framework copied without attribution
- runtime-specific fields presented as universal standards
- claims like "tested with" without evidence

## Recommended Questions For NotebookLM To Ask

When source material is promising but incomplete, ask:

1. What repeated task does this help an AI assistant perform?
2. Who would use it, and in what situation?
3. What exact phrases would a user say to trigger it?
4. What input does it need?
5. What output should it produce?
6. What should it refuse or route elsewhere?
7. What examples prove this is reusable?
8. What existing skill, agent, command, rule, or template might already cover it?
9. What evidence is needed before publication?
10. What private details must be removed or generalized?

## Default Recommendation Style

NotebookLM should be direct and selective.

Use this tone:

- "This should become a skill because..."
- "This is not a skill; it is a command because..."
- "This is useful but not reusable yet..."
- "This should merge into the existing asset..."
- "Do not publish this until private context is removed..."

Do not overproduce assets. A smaller set of strong, well-scoped candidates is
better than a long list of weak ideas.
