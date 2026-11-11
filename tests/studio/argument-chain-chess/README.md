# Test: the argument chain on a post that passes line by line

A real first post from the author's own studio (24 Oct 2026), adapted by `/post` from one of his essays. The judge passed most lines and sent it back for two local seams, but the post doesn't hold as one argument. This test checks that the chain check (`skills/craft-copylosophy`, "The chain check"), the one-idea check (LinkedIn judge 11a) and the outside-case check catch what the first run missed.

## What to stage

- `draft.md` beside this README, as `pieces/test-chess/draft-v1.md`, with a minimal brief: `path: direct`, `format: fmt-linkedin-post`, `adapted_from: material/<the essay>` (any essay file; the source text isn't part of this test).

## What to run

The `judge` agent on the piece, in a fresh context.

## Properties the review must have

1. An "Argument chain" section with the post as numbered steps and the one idea stated (or a note that it needs an "and").
2. Check 11b fails at least four times, naming these links (wording may differ, the link must be the same):
   - **Example next to the claim:** the chess win is about humans choosing what the machines look at; the post uses it for an objective vs. subjective split, and "Your work splits the same way" carries the gap.
   - **Shifted test:** "Ask two smart people" becomes "Anything I can write a rule for" and then "depends on my experience, my values or my taste".
   - **A group nobody defined:** the two-way split becomes three with "Anything in the middle".
   - **Taken back:** "I'm not saying AI can't help with the hard calls" weakens "On the second half it falls flat" instead of stating a condition.
   - **The close breaks the body:** "If they wouldn't, take it back" drops the "we do together" group.
3. Check 11a fails: the post holds the conclusions of more than one idea from the essay; the review names one idea the post could carry alone (for example, the "would two smart people give the same answer" test).
4. Verdict `redo` (two or more fails in section B, which the gates table in `skills/role-editor` grades redo under "Format: body").
5. An "Outside cases" section: the 2005 freestyle tournament checked against a source the judge opened in this run, with a link, or marked "not checked" with the details to confirm (the year, "two amateur players", "three computers") and named in "For the person". A line saying it was checked from memory fails the test.
6. Still caught, as in the first run: "Is the post under the character limit" refers to a post never mentioned (unresolved reference), and "The result came down to how the work was divided" repeats line 2's reason.

## Why it matters

Every line here is plain, sourced and in the author's voice, and the premise check alone passed it. The failure is between the lines. If a change to the judge stops this test from coming back `redo`, revert it.
