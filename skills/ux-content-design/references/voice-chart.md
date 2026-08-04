# Voice Chart

**The single home for voice.** Load when defining a product's voice, or when the copy keeps
coming out as pastiche and nobody can say why.

Voice is constant — who the product is, unchanged between a payment failure and a success screen.
How much room that voice gets in a given moment is **tone**, and that lives in
`voice-and-tone.md`. Come back here for *who we are*; go there for *how intense we are right now*.

---

## Step 0 — The rough position (a sketch, not the definition)

Before the constraints, put a pin in the map. Four axes, one position each:

| Dimension | Left | Right |
|---|---|---|
| Formality | Casual (*you'll*, *let's*) | Formal (*you will*, no contractions) |
| Warmth | Warm (acknowledges feeling) | Neutral (states facts only) |
| Authority | Peer (*we suggest*) | Expert (*do this*) |
| Density | Expansive (context first) | Terse (answer first) |

**Stop there.** A position on a scale is still an adjective with no ceiling — hand a model
"warm" and it writes gush. The axes only tell you which direction to aim; everything below is what
makes the aim hold. A voice that exists only as axes and adjectives will produce pastiche no
matter how carefully those adjectives were chosen.

## Why adjectives fail: adjective latching

Tell a model the voice is "friendly" and it writes a caricature of friendly. Tell it "confident"
and it writes a sales deck. The mechanism has a name: **adjective latching**. A single descriptor
has no ceiling, so the model maximizes it — "happy" becomes *delightful*, *magical*, *thrilled to
help*, on a screen about a failed file upload.

Three fixes, in order of how reliably they work:

1. **Mechanical constraints beat adjectives.** Models follow countable rules far more reliably
   than subjective ones. Replace "make it conversational" with: *sentences under 15 words, active
   voice, contractions allowed, no word a 12-year-old would need to look up.* Replace "keep it
   short" with a character count.
2. **Tone clusters beat single words.** If you must use adjectives, use three that pull against
   each other. "Warm" alone produces gush. *"Warm, plain, unhurried"* produces something a person
   would say. Each word caps the others.
3. **Guardrails beat descriptions.** That is Part 1 below.

Never hand a model one adjective and expect calibration. It has no way to know where you wanted
it to stop.

---

## Part 1 — This, But Not That

Write 3–5 pairs. Each names the quality *and* the failure mode it turns into when overdone.

**Bull's-eye logic:** the first word is the target; the second is the ring you land in when you
overshoot. Both must be plausible outcomes of the same intention.

**Avoid the synonym trap.** *Direct, but not indirect* is worthless — nobody overshoots "direct"
into "indirect". The "not" word has to be **something a writer would actually hit by accident
while trying to get the first one right.** *Direct, but not curt* is a real risk. *Friendly, but
not familiar.* *Knowledgeable, but not pedantic.* *Steady, but not boring.*

Test: if you cannot imagine a good writer producing the "not" version on a sincere attempt, the
pair is decorative.

```
Helpful, but not servile.
    → we tell you what to do next; we don't apologize three times first

Direct, but not curt.
    → we lead with the answer; we don't drop it on you without the consequence

Precise, but not academic.
    → we use the exact term once; we don't define it for four sentences

Warm, but not chummy.
    → we acknowledge a bad moment; we don't use slang, jokes, or emoji in it

Confident, but not promotional.
    → we state what the product does; we never claim it's the best at doing it
```

The second half is the working half. A reviewer holds the draft against it and rejects with a
specific line: *"that's servile — three apologies before the fix."*

**Test each pair:** if the "not" side describes something no one would ever write, the pair is
decorative. *Honest, but not deceitful* is useless. *Honest, but not confessional* is a rule.

The method is public practice. Mailchimp's voice guide is the widely cited example — *fun but not
childish, confident but not cocky, expert but not bossy* — and the pattern generalizes to any
product. Write your own; borrowed pairs describe someone else's product.

---

## Part 2 — The chart

Columns are your product principles — three, chosen for how you want the user to feel. Rows are
the aspects of the text where a decision actually gets made.

|  | **Helpful** | **Trustworthy** | **Focused on the task** |
|---|---|---|---|
| **Concepts**<br>*what we write about* | The user's next step. The relief: what stops being hard. | What actually happened, including when it's our fault. Limits stated where the claim is made. | One idea per string. The task at hand, not the roadmap. |
| **Concepts — never** | Our cleverness. Features described as features. | Promises about things we don't control. Guesses stated as facts. | Cross-sells, tips, "did you know", anything that isn't this task. |
| **Vocabulary**<br>*words we use* | Plain verbs: *save, send, undo, retry*. The user's noun for the object. | Exact quantities, dates, names. *We* for our failures. | The glossary term, every time, unchanged. |
| **Vocabulary — banned** | *simply, just, easily, obviously* — they blame the user for finding it hard | *amazing, revolutionary, powerful, seamless, effortless, best-in-class, game-changing, unlock, elevate, supercharge* | *and more, etc., various options* — vagueness dressed as brevity |
| **Verbosity**<br>*how much* | The shortest version that still says what happens next. | One sentence of context when the reason changes what they do. Otherwise none. | Labels: 1–3 words. Body: 1–2 sentences. Errors: the fix fits on one line. |
| **Grammar**<br>*how it's built* | Active voice. Imperative for actions: *Save changes*. | Subject–verb–object. One clause where possible. | Present tense. Second person only when addressing the user directly. |
| **Grammar — never** | Passive for anything the system did: *an error was encountered* | Nominalizations: *perform a deletion* → *delete* | Rhetorical questions, antithesis, sentence fragments for effect |
| **Punctuation** | No exclamation marks in errors, warnings, confirmations. One per screen, maximum, anywhere. | No em-dash used as a dramatic reveal. No ellipsis for suspense. | No colons setting up a punchline. |
| **Mechanics**<br>*countable rules* | Sentences under 15 words. Contractions allowed. No word needing a dictionary. | Every number, date, and name exact. Uncertainty stated as uncertainty. | Labels 1–3 words. Body 1–2 sentences. One CTA per surface. |

Fill this once per product. It replaces every conversation that starts "should this sound more…".

**The chart says what the voice is. It does not say how much of it to spend.** A user three
failed exports into a deadline gets the same voice as a user on a success screen, at a fraction of
the intensity — no character, no warmth performance, just the plain useful sentence. That decision
comes from the tone map in `voice-and-tone.md`, and the escalation rule there overrides any
personality this chart permits.

---

## Part 3 — Using it in review

The chart is only worth building if it is used to reject drafts. In review, cite the cell:

> "*Grammar — never*: that's an antithesis. Rewrite as one statement."
> "*Vocabulary — banned*: 'simply' — remove it, the user didn't find it simple."
> "*Verbosity*: three sentences before the fix. The fix goes first."

If a draft is bad and no cell explains why, the chart has a gap. Add the row and move on — that is
how it stays alive.

---

## Worked example: the same message through the chart

**Draft:** *"Oops! It looks like something went wrong on our end. We're really sorry for the
inconvenience — our team is working hard to fix it. Please try again in a bit!"*

| Cell | Violation |
|---|---|
| Punctuation | Two exclamation marks in an error |
| Vocabulary — banned | *Oops* trivializes; *working hard* is unverifiable |
| Verbosity | Four sentences, none of which say what the user does now |
| Concepts | Nothing about what actually failed or what survived |
| Grammar | *It looks like* hedges a fact we know |
| Trustworthy | *In a bit* is a promise about timing we don't control |

**Rewrite:** *"We couldn't save your changes. They're still here — try again, or copy your text
somewhere safe first."*

Four cells satisfied: it says what happened, what survived, and two things to do, in one sentence
each, with no apology performance.
