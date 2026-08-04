# Error Message Anatomy

Load when writing anything that reports a failure, a block, a limit, or a degraded state.

## The three-part contract

Every error answers, in this order:

1. **What happened** — in the user's vocabulary, describing the effect, not the mechanism.
2. **Why** — only when the reason changes what the user does. Skip it otherwise.
3. **What next** — a concrete action, ideally as a control in the message itself.

If you cannot write part 3, the message is not finished. "Something went wrong" with no recovery
path is a dead end and always counts as a defect.

```
Couldn't upload "budget.xlsx" — the file is 48 MB, the limit is 25 MB.
[Compress and retry]  [Choose another file]
```

---

## Severity ladder

Match the interruption to the consequence. Escalating past the real severity trains dismissal.

| Severity | User impact | Surface | Tone |
|---|---|---|---|
| Validation | Input not accepted yet | Inline, next to field | Neutral, instructive |
| Recoverable | Action failed, retry works | Inline or toast with retry | Factual, brief |
| Blocking | User cannot proceed | Banner or modal | Factual + explicit next step |
| Systemic | Product-wide degradation | Persistent banner + status link | Honest, timestamped, no promises |
| Data loss risk | Irreversible consequence | Modal, destructive styling | Plain, unambiguous, no personality |

---

## Assigning fault

Name the cause without blaming the person.

| Cause | Correct framing | Wrong |
|---|---|---|
| User input | Describe the rule: *Passwords need at least 12 characters* | *You entered an invalid password* |
| System failure | Own it once: *We couldn't save your changes* | *An unexpected error occurred* |
| Third party | Name it: *Our payment provider is not responding* | *Error contacting service* |
| Network | Neutral: *No connection. We'll retry automatically.* | *Your internet is down* |
| Permissions | State the gate and the route: *Only workspace admins can invite. Ask <name> to add them.* | *Access denied* |

Rule: use "we" for system failures, avoid "you" for user errors. *We couldn't process this card*
rather than *You entered a wrong card number* — the user cannot always tell which is true.

---

## Validation copy

- Fire on blur or on submit, never on every keystroke of a field the user is still typing.
- State the rule, not the violation: *Use at least 12 characters* beats *Password too short*.
- Show the rule as helper text before validation, so the error is a reminder, not a surprise.
- One error per field. If three rules fail, state the first unmet rule.
- Never clear the user's input on error. Never clear a form on a failed submit.
- Tie the message to the field programmatically (`aria-describedby`) and never signal error state
  by colour alone.

---

## Payment, security, and account errors

These carry money or safety, so: **zero personality, zero apology inflation, maximum precision.**

- Say what did and did not happen: *The payment didn't go through. You have not been charged.*
- Do not speculate about the cause when the provider gives a generic decline. Give the two real
  options: retry with the same method, or use another.
- Never disclose which half of a credential was wrong. *Email or password is incorrect.*
- For security actions (password change, new device), state the fact and the escalation:
  *If this wasn't you, reset your password now.*
- Never blame the user's bank, and never promise a refund timeline the system does not control.

---

## Codes, IDs, and technical details

Users get plain language. Support gets identifiers. Both can be true in one message.

```
We couldn't load your invoices. Try again in a minute.
Still stuck? Contact support and give them this code: 8F2C-41.
```

Rules:

- The code is never the headline and never the only content.
- Put stack traces, raw responses, and correlation IDs behind a "details" affordance, and make
  them copyable in one action.
- Never surface `null`, `undefined`, `NaN`, `[object Object]`, or an unformatted enum
  (`PAYMENT_INTENT_AUTHENTICATION_FAILURE`) to a user, in any state, ever.

---

## Empty vs. error vs. loading

Three distinct conditions that are routinely collapsed into one string. Distinguish them:

| Condition | Meaning | Copy shape |
|---|---|---|
| Loading | We don't know yet | Skeleton or *Loading invoices…* — no error tone |
| Empty | We know, there is nothing | Empty-state pattern with an action |
| Error | We know, we failed | Error contract with a retry |
| Partial | Some data failed | State what's missing and what's shown: *Showing 40 of 52 — 12 couldn't load. [Retry]* |

Never render an error as an empty state ("No invoices" when the request actually failed) — the
user concludes their data is gone.

---

## Offline and degraded states

- Say what still works: *You're offline. You can keep editing — changes sync when you reconnect.*
- Say what does not: *Sending is paused until you're back online.*
- Never promise automatic recovery the client does not implement.
- On reconnect, confirm resolution explicitly rather than silently removing the banner.

---

## Timeouts and retries

- Never show "retrying" without a bound. State attempt or time: *Retrying… (2 of 3)*.
- After the last attempt, escalate to a real action, not a repeat of the same message.
- Never auto-retry a non-idempotent action (payment, send) without telling the user.

---

## Error copy review checklist

- [ ] Answers what / why / what next
- [ ] Contains no code, enum, or stack fragment as the headline
- [ ] Assigns fault correctly, blames no one
- [ ] Offers an action the user can actually take right now
- [ ] Severity matches the interruption level
- [ ] No exclamation mark, no apology inflation, no mascot
- [ ] Distinguishable from the empty and loading states of the same component
- [ ] Preserves the user's input
- [ ] Support path included when self-recovery is impossible
