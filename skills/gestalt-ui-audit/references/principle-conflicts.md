# Conflicts between principles

Load this file in Step 4, when two principles point to different groupings of the same elements.

## Ground rule

Grouping principles do not have a fixed ranking. How strongly each cue binds depends on how strong
it is on this screen: a large gap beats a faint colour difference, a strong colour difference beats
a small gap (Quinlan & Wilton 1998; Wagemans et al. 2012). Treat the default orders below as
predictions, then check them against the strength of each cue on the screen.

For every conflict, record:

1. The elements involved and the two groupings each principle suggests
2. Which grouping wins on this screen, and why (cue strength)
3. Whether the winning grouping matches the intended structure
4. The fix: make the cues agree, or remove the weaker one

A conflict whose winning grouping matches the intended structure is still a finding when the losing
cue adds noise. Score it Low unless it slows scanning.

## Common conflicts in product UI

### Common region vs proximity

**Default prediction:** the container wins. Elements in one card read as one group even when far
apart, and close elements in different cards read as separate (Palmer 1992).

**What to check:** whether the container boundary is strong enough. A faint border on a background
of nearly the same colour may lose to a large gap.

**Typical case:** a card holds a title at the top and its action at the bottom, with a large empty
area between. The card keeps them together; if the card edge is faint, the action reads as
belonging to the next element down.

### Uniform connectedness vs proximity and similarity

**Default prediction:** the connection wins. A line joining two elements binds them more strongly
than closeness or shared colour (Palmer & Rock 1994). The strength of this cue relative to others
is debated in later work; see Wagemans et al. 2012.

**Typical case:** a divider line placed between a label and its value. The line visually separates
what the spacing joins, so the label reads as a heading for the row below.

### Similarity vs proximity

**Default prediction:** proximity usually wins over shape. Colour can beat proximity when the colour
difference is strong and the gap difference is small (Quinlan & Wilton 1998).

**Typical case:** a status chip in the same colour as the primary button next to it. The shared
colour pulls the status into the action group, and users try to click it.

### Similarity vs common region

**Default prediction:** the region wins for grouping, but strong similarity across regions creates a
second, competing reading: "these coloured things across cards are one category".

**When that is intended:** status colours repeated across cards. **When it is not:** a decorative
accent colour reused on unrelated elements in several cards.

### Figure/ground vs continuity

**Default prediction:** figure/ground wins. A decorative line or image passing behind text breaks
the flow and the separation of text from background.

**Fix direction:** give text a solid or blurred backing, or end the decorative path before the text.

### Prägnanz vs grouping density

**Default prediction:** when too many weak groups compete, people simplify by ignoring some of them.
A dashboard with many equally weighted widgets is often scanned as "one grid of boxes", and nothing
stands out.

**Fix direction:** reduce the number of top-level regions or vary their emphasis so one dominates.

## Severity of conflicts

Use the severity scale in `report-contract.md`. For conflicts it reads:

| The winning grouping... | Severity |
|---|---|
| Contradicts the intended structure and can cause a wrong action, entry, or missed requirement | High |
| Contradicts the intended structure; users recover by re-reading | Medium |
| Matches the intended structure; the losing cue only adds noise | Low |
