# Typesetting Engine Skillset

**Seven single-responsibility skills covering the full typography/layout pipeline — from character-level polish to Figma-native design tokens.**

Each skill does one job and hands off to its neighbors rather than duplicating logic. Use one in isolation, or run the relevant subset in sequence for a full pass on a design or a piece of body copy.

## The skills

| Skill | Scope | Design-tool aware |
|---|---|---|
| [`microtypography`](./microtypography/) | Character-level text polish: hanging single-letter conjunctions, numbers/units, smart dashes/quotes, widows/orphans, ragged edges, hanging punctuation (detection). Format-agnostic — markdown, HTML, plain text. | Yes — edits `TextNode.characters` without flattening range styles, sets `textWrapStyle` and `hangingPunctuation` |
| [`line-length-optimizer`](./line-length-optimizer/) | Column width (measure): 45–75 characters desktop, 35–45 mobile. Outputs a `ch`-based CSS fix or resizes a Figma text node. | Yes — reads `textAutoResize` |
| [`text-typesetting`](./text-typesetting/) | Line-height, letter-spacing/tracking (case-, x-height-, weight-, variable-axis-aware), vertical-trim, OpenType number styles, kerning integrity, dash rendering, hanging-punctuation computation. The most detailed skill in the set. | Yes — reads/writes most `TextNode` properties |
| [`vertical-spacing`](./vertical-spacing/) | Margin/padding/Auto Layout gap against a grid base, vertical-trim optical correction, paragraph/list rhythm, Figma margin-collapse guard. | Yes — reads/writes `FrameNode` Auto Layout properties |
| [`type-scale-generator`](./type-scale-generator/) | Generates a font-size scale from a base size and ratio (8 named musical/geometric ratios, Fibonacci, classic Garamond steps), rounded to avoid subpixel rendering, with line-height and tracking for each step. | Yes — base from the selected text; creates variables, text styles bound to them, and a specimen |
| [`glyph-fidelity`](./glyph-fidelity/) | All-caps tracking formula, ligature-collision guard under negative tracking, inline-acronym subrange treatment. Holds the all-caps tracking formula that `text-typesetting` uses. | Yes — reads `textCase`, writes range tracking and size; ligature changes are reported, since Figma has no setter for them |
| [`text-fit`](./text-fit/) | Text against its container: line counts across sibling components, a character budget, truncation with reachable full text, resilience to longer copy, translation and larger text. Draft. | Yes — reads `textAutoResize`, `textTruncation`, `maxLines` |

## How they hand off to each other

For code-capable agents, a typical full pass is `type-scale-generator` → `line-length-optimizer` → `text-typesetting` (+ `glyph-fidelity` for all-caps) → `vertical-spacing` → `microtypography` → `text-fit`.

Figma runs only the first skill named in a prompt. The seven files in [`figma/`](./figma/) are therefore standalone: each repeats the neighbouring rules it needs and ends by naming the next slash command. Run them one at a time:

1. `/symphonia-type-scale`
2. `/symphonia-line-length`
3. `/symphonia-text-typesetting`
4. `/symphonia-glyph-fidelity` when the selection contains all-caps, small caps, acronyms, tight ligatures, or suspected fallback glyphs
5. `/symphonia-vertical-spacing`
6. `/symphonia-microtypography`
7. `/symphonia-text-fit`

Every Figma skill follows the same boundary: read → report → ask only for missing consequential information → ask before every write. A value owned by a style or variable is reported at that owner and is not silently overridden on one node.

## When to use the whole set vs. one skill

- **One skill**: a narrow, specific ask ("what line-height for this heading", "fix hanging conjunctions in this paragraph").
- **The full set in sequence**: setting up a new design system's type foundation, or auditing an existing Figma file end-to-end for typographic correctness.

## Sources: three layers

Every value a skill produces should be traceable. The sources are used in three layers, and a lower layer never silently overrides a higher one.

| Layer | Sources | What it decides |
|---|---|---|
| 1. Typesetting rules | Bringhurst, Felici, Butterick, Latin, Hochuli, Wolański, PWN | Where a value comes from |
| 2. Platform constraints | Apple Human Interface Guidelines, Material Design 3, WCAG | Floors and requirements the result must not break: minimum sizes, access to truncated text, resilience to larger text |
| 3. Usability evidence | Nielsen Norman Group | Why a rule matters in an interface |

A skill states the value from layer 1 and flags separately when it breaks a constraint from layer 2. Platform size lists are not used as scales. Where no source was found for a number, the skill says so and labels the number as its own working value.

## License

Each skill carries its own `LICENSE` (MIT) and `README.md`. See the individual skill folders for full authoring, references, and attribution.

---

*Part of the [Design Engineering Playbook](https://github.com/monikazapisek/design-engineering-playbook) — AI-assisted workflow artefacts for product designers working in agile and lean environments.*
