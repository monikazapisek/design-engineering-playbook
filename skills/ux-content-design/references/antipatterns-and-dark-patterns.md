# Anti-patterns and Dark Patterns

Load when auditing existing copy, reviewing a flow, or when a stakeholder requests a pattern that
should be refused.

## Dark patterns with a copy root cause

These are not tone problems. Several are regulated in the EU (Digital Services Act, GDPR consent
rules, and the Unfair Commercial Practices Directive) and in the US (FTC guidance on negative
option marketing). Treat them as defects, not preferences.

| Pattern | What it looks like | Why it fails | The honest version |
|---|---|---|---|
| **Confirmshaming** | *No thanks, I like wasting money* | Coerces via guilt; measurable trust cost, no durable conversion gain | *Not now* |
| **Asymmetric options** | Accept is a button, decline is grey small-caps text | Choice architecture, not copy — but the copy sells it | Equal weight, equal legibility, both named by outcome |
| **Bundled consent** | One checkbox for terms + marketing | Consent must be separable and specific under GDPR | Separate, unchecked controls, each named |
| **Trick wording** | *Uncheck to not opt out of emails* | Double negatives defeat comprehension by design | *Send me product emails* — unchecked |
| **Roach motel** | Sign-up is 2 clicks, cancel is a phone call | Deliberate asymmetry of exit | Cancel path as short as the join path |
| **False urgency** | *Only 2 left!* when stock is unlimited | Untrue claim, straightforwardly deceptive | State real scarcity or say nothing |
| **Hidden cost reveal** | Fees appear at the last step | Deception by sequencing | Total price on the first price shown |
| **Disguised ad** | Promoted content styled as system content | Misattributes the source | Label it, and say who paid |
| **Forced continuity** | Trial converts silently to paid | Consent gap at the moment money moves | Explicit reminder before the charge, with the amount and date |
| **Nagging** | Repeated modal asking for the permission already declined | Overrides a decision the user made | Ask once, offer the setting, stop |

**When asked to write one:** decline that specific framing in one sentence, deliver the honest
alternative, and state the trade-off factually (what conversion effect is claimed, what the
regulatory and trust exposure is). Then continue with the rest of the work.

---

## Craft anti-patterns

| Anti-pattern | Example | Fix |
|---|---|---|
| **Robotic over-apology** | *We sincerely apologize for any inconvenience this may have caused* | *We couldn't save your changes. Try again.* |
| **Personality in a crisis** | *Whoops! Something went wonky 🙈* on a failed payment | Zero personality above the anxiety threshold |
| **The bare code** | *Error 500* as the headline | Plain sentence; code behind "details" |
| **Silo naming** | Delete / Remove / Erase for the same action | Glossary + lint rule |
| **Dead-end error** | *Something went wrong.* | Always a next step |
| **Label as instruction** | *Please enter your email address here* as the field label | Label: *Email* |
| **Placeholder as label** | Only *name@company.com* in an unlabelled field | Persistent label, placeholder is the format hint only |
| **Fake progress cheer** | *Almost done!* at step 2 of 7 | *Step 2 of 7* |
| **Congratulating routine work** | Confetti on every save | Acknowledge hard tasks; stay invisible on routine ones |
| **Empty state that teaches nothing** | *No data* | First-run states are the best teaching surface in the product |
| **Error rendered as empty** | *No invoices* when the request failed | The user concludes their data is gone — distinguish always |
| **Concatenated sentences** | `"You have " + n + " item(s)"` | Full strings per plural form, semantic variables |
| **Jargon leakage** | *Tenant*, *payload*, *entity*, *job queue* in user copy | Engineering vocabulary stays in code |
| **Truncation as concision** | Cutting the consequence out of a destructive confirmation | Cut words, never cut the answer |
| **Copy patching a broken flow** | Three sentences explaining a confusing control | Say it is a flow problem, then write the best copy for the flow that exists |

---

## Audit procedure

For a copy audit, work surface by surface and produce one findings table.

1. **Inventory** — list every string on the surface, including states not in the mockup
   (empty, loading, error, partial, permission-denied). Missing states are findings.
2. **Classify each finding** by severity:

   | Severity | Definition |
   |---|---|
   | **Critical** | Dark pattern, false claim, regulatory exposure, data-loss copy that hides the consequence |
   | **High** | Dead-end error, wrong-audience register, missing state, misleading label |
   | **Medium** | Term inconsistency, jargon leak, weak CTA, apology inflation |
   | **Low** | Capitalization, punctuation, minor length overrun |

3. **Report** as `Location | Current | Issue | Severity | Rewrite`, ordered by severity.
4. **Name the systemic patterns.** Twelve instances of *Remove* vs *Delete* is one finding
   ("no glossary"), not twelve. An audit that lists only symptoms produces a ticket backlog;
   an audit that names the system produces a fix.
5. **Recommend the smallest structural change** that prevents recurrence — usually a glossary
   entry, a component content rule, or a lint rule — not just the rewrites.
