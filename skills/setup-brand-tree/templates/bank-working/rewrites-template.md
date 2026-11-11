---
piece: <piece id>
date: <yyyy-mm-dd>
format: <fmt-linkedin-post / fmt-substack-essay>
draft: <draft-vN.md the person rewrote>
detector_draft: <Pangram label and ai fraction on the studio's draft, from the review; or "not run">
detector_final: <Pangram label and ai fraction on the person's version, one call by the producer; or "not run">
written_by: <producer / learn>
---
# <piece id>: the studio's draft and the person's version

## The studio wrote

<the `## Post` section of the draft, as it was>

## The person wrote

<their version, exactly as they handed it back>

## What changed

<Three to six lines, each one move, in plain words, with the before and after quoted, and a rule tag at the end. Only what's visible in the two texts; no guesses about why.>

- <the move ("before" → "after")> · rule: <H<n> / W<n> / new / piece>

<The tag says which rule the change touches:
- `H<n>` or `W<n>`: the studio's draft broke that house rule (`skills/craft-house-rules`) or voice-guide rule (`canon/voice/voice-guide.md`), as the rule is written. Tag a rule only when the "before" plainly breaks it; when in doubt, it's `new`.
- `new`: a move the person made that no rule covers yet.
- `piece`: about this piece only (a fact, the argument, a date, a call to action), with no lesson about how they write.
When a `new` move later becomes a voice rule, whoever writes the rule changes this tag to the rule's W number. A pair with no `new` and no untagged line left is closed: its lessons are in the rules, and the writer reads open pairs first (`scripts/rewrites.py pick`).>
