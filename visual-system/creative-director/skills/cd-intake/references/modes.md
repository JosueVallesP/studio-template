# Settling the mode

The mode decides what the rest of the repo does for this brand, so settle it before talking about style.

## The four modes

| Mode | When | What the interview then focuses on |
| --- | --- | --- |
| `keep` | They have a brand that works and want it protected while more gets made | An inventory: every color, font, layout habit, image style, and the pieces they consider right |
| `refresh` | They like their brand, but it feels dated or no longer matches where they are | The inventory, plus what people recognize, plus what feels tired and why |
| `rebrand` | Their brand no longer fits who they are or where they're going | The full diagnosis, and a clear reason the old brand stopped fitting |
| `new` | No real brand yet, or only defaults | The full diagnosis; references carry more weight |

## Questions that settle it

Ask in this order and stop when it's clear:

1. "Do you have a look today that you'd call yours? Show me a piece that feels most like you."
2. "If we made a hundred more pieces in that look, would you be happy?"
3. If no: "What's wrong with it? Is it the look itself, or that it doesn't match where you are now?"

"The look itself is fine, it's just tired" points to refresh. "It's not me anymore" points to rebrand. "I've never really had one" points to new.

## When what they say and what you see disagree

Sometimes a person asks for keep mode when their brand is the generic default of the tool they used. Or they ask for a rebrand when their brand has strong recognition they'd lose. Say what you see, kindly and with the evidence, and let them choose. Record both their choice and your reading in `mode_reason`. Their choice stands; the framer decides.

## What each mode changes downstream

- **keep:** `cd-direction` extracts rules instead of writing new ones, and everything it extracts is locked. Reviews lead with fidelity.
- **refresh:** `cd-direction` writes `equities.md` first and protects those. Reviews check equities survive.
- **rebrand:** the old brand goes into `references.md` as "move away from," with the reason.
- **new:** no constraints from the past. The contradiction and the references do most of the work.

A brand can change mode later. A new brand becomes keep once its direction is approved and canon exists. Note the change in `log.md`.
