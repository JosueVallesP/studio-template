---
doc: voice-guide
layer: voice
version: 2
last_reviewed: <date>
owner: <person's name>
status: default until the person's own rules replace these
---
# Voice guide

Built from how they actually talk (transcripts, voice-dictated answers) and from samples they approved. Grows as they edit drafts (`bank/rewrites/`).

**The default.** Until the interviews and the person's rewrites fill this in, the studio writes in the default register below: how a person talks when they explain something to someone they respect. It was distilled from the studio author's own rewrites of studio drafts, with everything personal to him removed. None of it is a phrase; all of it is a habit of plain speech, and the examples are neutral on purpose.

**How the rules are numbered.** The ten default rules are W1 to W10, each `status: default`. The person's own rules take the next free W number (W11, W12 and on). A default rule the person reads and says yes to becomes `status: confirmed` and keeps its number. Default rules don't count toward the minimum canon's three W rules (`canon/progress.md`); only the person's own or confirmed rules do.

**Who replaces a default rule.** The map (`skills/job-map`) writes the person's own rules as `status: draft` W entries beside these, each with the lines from their material it was read from. When the material shows a different habit from a default rule, the map or the voice interview drafts the person's rule and proposes the default one as `retired`; the person says yes before either changes. A default rule is never stacked under a rule of theirs that contradicts it. The checks (`scripts/voice-diff.py`) always measure against the person's own words, never against this default, so the default stops pulling the moment they have material.

Point of view comes first (`skills/craft-house-rules`): nothing here makes a piece theirs if the idea isn't.

## Rules

### W1 · A soft first-person frame, then a firm claim
status: default
rule: An opinion opens with the speaker in it ("I think", "I'd say", "the way I see it") and then states the claim flat. The frame is the way in, not a hedge on the claim.
before: "Onboarding is broken."
after: "I think most onboarding ends too early."
sources: default register

### W2 · Claim, then its bound, in the same breath
status: default
rule: After a strong claim, the condition that makes it true follows at once ("not always, but...", "unless..."). Don't drop the bound to sound more certain.
before: "Long emails don't get read."
after: "Long emails mostly don't get read, unless the reader asked for the detail."
sources: default register

### W3 · Stance words where a talker would put them
status: default
rule: "just", "really", "a bit", "a lot", "actually" carry how hard the speaker leans. Keep them where speech would put them; never bolt them onto a flat sentence afterwards (`skills/craft-human`, pattern 5).
before: "This is difficult."
after: "This is hard, and it's a lot harder than it looks."
sources: default register

### W4 · Lists of examples stay open
status: default
rule: A run of examples ends open, with a sign that the list could go on, not on a tidy third item. Three items chosen for rhythm is a machine tell (house rule H29).
before: "Use a spreadsheet, a notebook or a whiteboard."
after: "A spreadsheet, a notebook, a whiteboard, the back of an envelope, whatever is nearby."
sources: default register

### W5 · A reaction after an example, not a lesson
status: default
rule: After a comparison or an example, the line that follows says how the speaker feels about what they just showed, in a few plain words, never a moral drawn from it (house rule H30).
before: "The second version is shorter, which is the key to a good subject line."
after: "The second version is half the length. I like it a lot more."
sources: default register

### W6 · Talk to the reader when advising; stay "I" when telling
status: default
rule: Advice goes to "you". Experience stays "I". Never generalize the speaker's own experience into "someone" or "people" (house rule H13).
before: "When someone gets a vague brief, they stall."
after: "When I get a vague brief, I stall."
sources: default register

### W7 · Say why, right after the verdict
status: default
rule: "Hard", "abstract", "better", "worse" are followed by the reason in the next clause (house rule H7).
before: "That plan is unrealistic."
after: "That plan is unrealistic. It needs three people and there's one."
sources: default register

### W8 · Name the real thing
status: default
rule: Frameworks, tools, people and numbers by name, never "a template", "a tool", "a few" (house rule H3). Numbers as digits.
before: "I use a few tools to plan the week."
after: "I plan the week in Notion and on a paper calendar, and it takes about 20 minutes."
sources: default register

### W9 · Questions one per line
status: default
rule: A set of test questions goes one per line, no bullets, the way someone asks them in their head.
sources: default register

### W10 · A flat close
status: default
rule: Pieces end on the last real thing said, or on a plain handoff ("Let me know what you think"). Never a restated lesson, never "Hope that's helpful", never a line that exists to sound final.
sources: default register

## Signature moves
What this voice does especially well, named so the writer can reach for them (replace with the person's own as they appear):
- The honest concession before the point: say what works about the other view, then the real disagreement.
- Claim, bound, example, reaction.
- The named list that ends open.

## Vocabulary
- Phrases they use: <…>
- Terms they coined: <…>
- Words they'd never use: <…>

## House-rule exceptions
Things the house rules ban that this person actually uses (`skills/craft-house-rules`, the exception principle). One per line, with the quoted evidence and where it came from, and only after the person said yes to it. Empty by default: the default register has no exceptions. Two kinds of line:

- A word or phrase. The scripts let that phrase through.
- A whole rule, for a pattern a phrase can't hold (an "it's not about X, it's about Y" line written a dozen different ways). Write `rule` and the rule ID. It comes from the "Rules you break yourself" list in `bank/voiceprint/voice-targets.md`, with its counts. The scripts flag each use of the rule instead of failing it, so the judge still sees every one, and voiceprint's "Above your own rate" flags a draft that uses it more often than the person does.

The studio uses either kind about as often as the person does, never more.

- <word or phrase>: "<the line they wrote>" (<source>)
- rule <rule ID>: "<the line they wrote>" (<source>; in <n> of <n> pieces, <rate> per 1,000 words)

## Approved samples
- <title or link> (<format>): <what makes it sound like them>

## Rejected samples
- <title or link>: <why they rejected it>

## Register by channel
- <channel>: <how they sound there, if different>
