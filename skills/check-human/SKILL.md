---
name: check-human
description: Reads a draft against the six patterns in craft-human and marks the lines that read as machine-written, with the mechanical counts from scripts/check-human.py beside them. Pass or fix. Runs inside the judge on every draft (the format judge stage's human check; the editor's and the judge agent's reviews include it), and whenever someone says "this reads like AI", "humanize this" or "check this for AI". Never rewrites.
---

# Check: does this read like a person?

You read a draft the way a stranger would and say whether a person wrote it. You don't fix it. You mark what fails and hand it back.

Read `skills/craft-human/SKILL.md` first. The six patterns there are the whole checklist.

## Procedure

1. Run `python3 scripts/check-human.py <draft>` if a shell is available. It measures the `## Post` section when the file has one (each of Posts A, B and C on its own when there are three), so the counts are about the post and not about the notes around it. The script measures patterns 1 to 4 and the decoration adverbs; you read patterns 5 and 6 (its stance count is only a note). Its counts are evidence for the verdict rule in step 4, never fails on their own; a draft can have good numbers and still fail by reading, or the reverse.
2. Read the draft once straight through without stopping, as a reader who doesn't know the person. Note where your attention flagged. That's usually pattern 2 or 4.
3. Go through the six patterns in order and, for each one, quote the lines that show it. Quote the draft's exact words so the writer can find them.
   - 1 Nobody in the room: is there a speaker and an occasion in the first three sentences?
   - 2 Same weight: read five consecutive sentences aloud in your head. Do they all land the same?
   - 3 Ladders and triads: any "X. Then Y. Then Z.", lists of three for rhythm, "Not X. Y." pairs, parallel fragments.
   - 4 Landing lines: how many paragraphs end on a short impersonal line that closes the loop?
   - 5 No stance: count the words that show the speaker leaning. Zero in a piece over eighty words is a note: read for stance. Also flag decoration adverbs; those fail the writing rules.
   - 6 Every loop closed: does the draft pre-answer every objection and leave the reader nothing to do?
4. Verdict:
   - **Pass**: two patterns or fewer, none in more than two places.
   - **Fix**: three or more patterns, or any one pattern in three or more places. Say which lines and which pattern. Don't propose the rewrite; the writer says it again.
5. The detector line. With `--detector`, `check-human.py` sends the post to Pangram once and prints the label ("Human", "Mixed", "AI"), the fractions and the flagged windows, and `detector: <label>` with no pass or fail. It's a paid call; who makes it and when is in `CLAUDE.md`'s detector paragraph. Inside a review, whoever judges records the reading, from the "Detector" row of the gates table in `skills/role-editor`, which makes the one call for that pass; when this check runs as part of a judge stage, record that reading and don't call again. A run of this check on its own (someone asks "does this read like AI") doesn't call it. Rewriting against the score keeps the score (`skills/craft-human` has the runs behind this). The label is recorded for the person as a reading. The six patterns are still the reading that drives fixes: a model-written label with a pass by reading means read again, because the patterns missed something (`skills/craft-human` has the run). What moves the label is the person's own rewrite, kept in `bank/rewrites/`.

## Output

When the editor runs this, the block below goes into the review's check-human section and no separate file is written. When run on its own (someone asks "does this read like AI"), give it in the reply:

```
VERDICT     pass / fix
PATTERNS    which of the six, each with the quoted lines
COUNTS      the script's flags line, or "no shell"
DETECTOR    the label and fractions and which draft it was run on, or "not run" with the reason
NEXT        who acts: writer says it again / on to the judge
```

## Never

- Never rewrite or suggest replacement lines. Saying it again is the writer's job, and a line bolted on to pass a check reads bolted on.
- Never pass a draft because the voice guide calls for short sentences or a formal register. The standard sits under the voice; a formal person still has an occasion and a stance.
- Never recommend planting typos or slang to move a detector score.
- Never treat the detector as the verdict; it is a reading recorded for the person, and the patterns are what drive fixes.
- Never report a detector that did not run as a pass, and never leave the DETECTOR line out.
- Never call the detector outside the two points in `CLAUDE.md`'s detector paragraph: never on a revised draft, never from the writer's pass.
- Never count a line the person wrote, quoted word for word from their material or their final edits, toward a pattern. Mark it "theirs" and leave it. Count only what the studio wrote. The exemption covers a line, never a post: when more "theirs" lines appear than the cap in `templates/piece/draft.md` allows (two in a post, four in an essay, a starting default), or two "theirs" lines from different pieces sit side by side, that is the stitched-quotes gate in the editor's table, and the post fails whatever the patterns say.
