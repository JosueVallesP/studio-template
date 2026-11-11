---
name: check-voiceprint
description: Measures how the person writes from their own material (stylometry), meaning the small words they use without choosing, sentence length and spread, punctuation and contractions, and reads a draft against it, with a verdict only when the numbers can tell. Builds the profile and the writer's voice targets, reads one draft once as a recorded reading, and measures what the person's rewrites in bank/rewrites/ have in common. Runs inside the judge on a piece's first judged draft once a profile exists, and whenever someone says "/voiceprint", "does this sound like me, measured", "build my voiceprint" or "what do my rewrites have in common". Never rewrites.
---

# Check: does this draft carry the person's habits?

Stylometry measures habits in writing that people don't choose: how often they use small words like "just", "so", "of" and "I", how long their sentences run and how much they vary, which punctuation they lean on. Those rates stay steady across everything a person writes, which is how the authorship of the Federalist Papers was settled. This skill measures them on the person's own writing and reads a draft against them.

It sits beside `scripts/voice-diff.py`, not in place of it. `voice-diff.py` checks six markers for drift toward the machine average on every draft. Voiceprint is the fuller reading: it compares the draft with the person's own pieces and with other writers and the studio's own drafts, on hundreds of words and 29 style measures, and says how sure it is. Both are readings for the judge, and neither is a verdict on whether the piece is good.

What it can't do matters as much. It measures the surface of the person's voice. It can't see their point of view, and a draft can match every number and still say what anyone could say. Point of view before sound (`CLAUDE.md`, writing rules): the person's beliefs, stories and words come first, and voiceprint checks what comes out.

Read `references/methods.md` before changing the script, and `references/reading-a-report.md` before explaining a report to the person.

## What it reads and writes

All paths are from the instance root. `scripts/voiceprint.py` uses them as defaults.

| Path | What | Notes |
| --- | --- | --- |
| `material/` | The person's own writing | Files with "transcript" in the path are skipped: a call transcript carries other people's voices. A mixed file (their post with a long quote) is fine; a file written with AI or by a ghostwriter isn't, and the person should move it out or the profile learns the wrong voice. Files marked in their first lines as written for them or as a summary are skipped. |
| `bank/voiceprint/others/` | Other writers in the person's formats | Files or a CSV with a text column. Twenty or more pieces. The folder starts empty; the person or the studio fills it with posts or essays by people who write like their peers. Until it's filled, the studio's libraries make a starting comparison set: the full texts of 357 LinkedIn posts in `skills/fmt-linkedin-post/library/posts/` and 57 Substack essays in `skills/fmt-substack-essay/library/essays/`, passed with `--others <that folder>`. |
| `bank/rewrites/` | The studio's side of every pair joins the comparison set | Read in place. These matter most: the question the studio asks is whether a draft sounds like the person or like the studio. |
| `bank/voiceprint/profile.json` | The measured profile | Rewritten by every `profile` run. Its `house_rules` part counts each house-rule pattern in their pieces, with quotes. |
| `bank/voiceprint/voice-targets.md` | The writer's brief, in plain words | Rewritten by every `profile` run. The person's decisions about it go in the voice guide, never here. |
| `bank/voiceprint/readings.jsonl` | One line per reading | Appended by `score`. |

`bank/` belongs to the person, so an update never touches any of it.

## The four jobs

### 1. Build the profile

When: once the person has about 5,000 words in `material/`, and again when they add ten or more pieces, when a batch of rewrites lands, or every couple of months. People's writing drifts.

1. Count what's in `material/` (the script prints it). Below about 5,000 words or 10 pieces, tell the person in plain words what's there, what the profile needs and why (rule 7), and offer to wait. The script still builds a profile; it marks the gaps.
2. Check `bank/voiceprint/others/`. Fewer than 20 pieces means the "how you differ" lines measure against too little. Say so and suggest what to add: posts or essays by people in the person's field and format, never the person's own.
3. Run `python3 scripts/voiceprint.py profile`.
4. Read `bank/voiceprint/voice-targets.md` with the person: the few measures that set them apart, and their marker words. Topic words show up among the markers ("brand", "clients"); ask which words are habits and which are their subject, one question at a time. What they confirm or reject goes into `canon/voice/voice-guide.md` as a proposal (rule 6), quoted with the numbers behind it.
5. Read the "Rules you break yourself" section with them. The profile runs the house-rule checks (`scripts/studio_checks.py`, the same ones every draft gets) over each of their pieces and lists the patterns their own writing uses in at least 30% of their pieces, or more than twice per 1,000 words, and in at least three pieces: an "it's not about X, it's about Y" line, em dashes, semicolon chains and the rest. Each one goes to `proposals.md` as its own entry, kind `voice rule`, with the rule ID, how many of their pieces use it, the rate per 1,000 words and the quotes the section gives. Ask about one at a time: "you write this in 5 of your 6 pieces; is it yours, or a habit you'd rather lose?" Only their yes puts it in the voice guide's "House-rule exceptions" section, as `- rule H17: "<their line>" (<source>)`. For a rule matched word by word (H2, H19, H20, H21) the section names the words they use; propose those words as phrase exceptions instead of the whole rule. A no is final until the next profile shows something new.

### 2. Brief the writer

The writer reads `bank/voiceprint/voice-targets.md` with the voice guide, after the person's material and the brief, when it exists. The targets describe how the person already writes. They are never quotas: a writer aiming at 4.2 contractions per 100 words writes worse, not more like the person.

The marker words are the person's habits, never words to aim for. A writer that learns from someone's pieces drifts toward their most frequent choices: a word they use once a piece shows up five times, the next draft learns from that one, and the person turns into a caricature of themselves. So the writer reads the markers to know what sounds like the person, and uses a marker only where the sentence needs it, never to sound more like them. The score report's "Above your own rate" section is how the judge catches the drift (job 3).

Where a target clashes with a house rule (a person who uses dashes, under H16), the exception principle in `skills/craft-house-rules` decides: the habit shows up in their own writing, so it's theirs. The targets file is evidence for that, quoted, the same way a line from their material is. A rule the person said yes to (job 1, step 5) stays a flag on every use, never a free pass: the writer uses the pattern where they would, about as often as they do.

### 3. Read a draft, once

When: on a piece's first judged draft, by the `judge` agent, once `bank/voiceprint/profile.json` exists. Or when the person asks for it.

1. Run `python3 scripts/voiceprint.py score <draft>`. It measures the `## Post` section when the file has one and ignores the source map. A file with Posts A, B and C needs `--draft` and the label of the one the judge picked: the reading runs once per piece. The impostor test takes a few seconds; `--no-impostors` skips it.
2. Put the reading in the review as the VOICEPRINT block below. The verdict is a reading, like the detector's label. It never fails a draft by itself and it never starts a rewrite loop.
3. Flags the draft breaks go to the writer as evidence for the gates they touch. "No contractions where the person uses plenty" is evidence for the "not theirs" gate in `skills/role-editor`, read beside `voice-diff.py` and the swap test. The judge decides.
4. Read the "Above your own rate" section. It lists what the draft does more than the person's own pieces do: a marker word used past the rate of most of their pieces (and at least twice), the most repeated sentence opener, paragraphs that end on a line of eight words or fewer, a house-rule pattern they use themselves (H17, a dash, a semicolon chain) used at least twice and past the rate of most of their pieces, and how the piece closes beside how often they close that way. The house-rule lines hold even when the rule is excepted in the voice guide: an exception lets the person's pattern through at their rate, never above it. Each line gives the draft's number and the person's usual number. A line there is evidence for the editor, worded to the writer as "this is more X than you usually write" (more "frankly", more paragraphs ending on a short line), never as a fail, and it never changes the verdict. With fewer than five of the person's pieces the section says it can't be read yet; say that and move on.
5. A revised draft isn't read again. Rewriting until the number rises teaches the draft to imitate the person's averages, and averages are what model text already looks like (`references/methods.md`, "Design choices").

### 4. Measure the rewrites

When: from `/learn`, `/end` or the librarian once there are three or more pairs in `bank/rewrites/`, or when the person asks what their rewrites have in common.

1. Run `python3 scripts/voiceprint.py patterns`.
2. It lists the measures that moved the same way in most rewrites ("in 7 of 9 rewrites, contractions went up") and the words the person keeps adding or cutting. Compare them with the pairs' "What changed" lines and the voice guide. A pattern no line or rule records yet is a candidate: tag the lines it shows up in `new` if they aren't, and write a voice-guide proposal with the counts as evidence. The person decides. A pattern that would hold for anyone goes to `studio-notes.md` as a candidate house rule.
3. For one pair on its own, `python3 scripts/voiceprint.py patterns <draft> <their-version>` prints what changed without reading the folder.

## Output

When the judge runs it, this block goes into the review and no separate file is written. Run on its own, give it in the reply.

```
VOICEPRINT  reads like you / close / off / no verdict yet, and the fit (with the person's own spread from the report)
SURE        the separation figure and what it means in a few words, or why there's no verdict
FLAGS       the top flags, each with the draft's value, the person's range and the fix, in the report's words
ABOVE       each "Above your own rate" line as "more X than you usually write" with both numbers, or "none", or "can't be read yet"
WORDS       AI-typical words found, or "none"
NEXT        evidence for the writer / nothing to act on
```

## Talking to the person about it

Plain words, the point first (house rules, Part 2). Say "how your writing measures", not "stylometric profile". Explain fit the first time: it's how close the draft sits to their writing, compared with their own pieces, and a typical piece of theirs scores around 30%; the report shows their own spread every time. Never present a reading as proof that a draft is or isn't theirs.

## Never

- Never put writing in the person's profile that isn't theirs: ghostwritten, AI-drafted, heavily edited or someone else's words. When in doubt, leave it out.
- Never read a file whose first lines say `<!-- studio: written for them, not by them -->` (the posts the intake says an agency, a ghostwriter or a team member wrote) or `<!-- studio: looks like a summary, not their words` (a recorder's summary, marked by `scripts/inbox-to-text.py`). `scripts/voiceprint.py` leaves both out of the profile; the voice guide and the voice rules skip them too. The map still reads a ghostwritten file for claims the person approved.
- Never rewrite, and never suggest replacement lines. Saying it again is the writer's job.
- Never loop on the score, and never read a revised draft again.
- Never treat the verdict as a pass or a fail. It's a reading; the gates decide.
- Never report a verdict the report withheld. "No verdict yet" is the reading.
- Never write to the canon. Voice-guide changes are proposals.
- Never write facts about a person into this skill.

## Studio notes

When this skill made you guess, write one line per guess to `studio-notes.md`.
