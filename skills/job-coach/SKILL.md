---
name: job-coach
description: Tells a person where they are with their studio, the one thing to do now, the two or three after that, and the few habits that matter, each with its reason in plain words. Reads the same facts as /status and turns them into advice instead of a list. Use for /coach, "what should I do", "what's next", "how do I get more out of this", "am I doing this right", or when someone seems lost after setup.
---

# /coach

`/status` is a list: what's waiting, what's moving, where each piece stands. This skill is the producer reading that list for the person and saying what to do about it. It answers four things, in order, and stops: where you are, the one thing to do now, what comes after, and the habits that matter more than any command.

Before intake, `setup-start` does this job and `/coach` hands over to it. Once `config/intake.yaml` exists, `/coach` is the place to ask "what now?", at any stage.

## What it reads

- `bash scripts/status.sh`, or the same files by hand: piece statuses, canon counts, proposals, inbox, the content plan's cadence.
- `canon/setup-progress.md`: the setup stage. Run whenever `config/intake.yaml` exists; when setup isn't done, the one thing to do now is usually the stage's next step from `setup-start`'s table. Hand over to `setup-start` only when `config/intake.yaml` doesn't exist.
- `canon/strategy/content-plan.md` and `brand-strategy.md` when they exist: the cadence, the mix, this quarter's branches, the signals. The advice is only as good as the plan it reads against; with no plan, the first piece of advice is `/strategy`.
- `pieces/`: the date of the last shipped piece, and anything `scheduled` in the next seven days.
- `studio-notes.md` and `proposals.md`: what's piling up unanswered.
- `config/working.md` when it exists (`skills/job-learn` writes it): how this person uses the studio, so the advice names what they already do and leaves out what they've said they skip.
- `pieces/librarian-last-run.md`: the drafts under "Drafts to add" not yet marked `added`, which wait on the person like any draft.
- `recipes/`: the person's saved routines, so the habits name the commands they already use instead of the ones they'd have to learn.

## What it says

```
Where you are
<Two or three lines. The facts that matter: last shipped piece and when, what's drafted and waiting, whether there's a strategy, what the input looks like this week.>

Do this now
<One thing, as something they can say or do, with its reason in a sentence and how long it takes.>

Then
1. <next thing, reason, time>
2. <…>
3. <…, at most>

The habits
- <when something happens: `/capture`, two minutes>
- <when you want a piece: `/post` or `/essay`>
- <end of a session: `/end`>
- <their recipes, when `recipes/` has any: `/<name>` for <what it does>, one line each>
- <Mondays: `/status`, decide what's waiting, twenty minutes>
- <one line on what to ignore until they feel a gap>
```

How to pick "do this now": take the first item that holds in the one ordered list under "The next step" in `skills/check-status`, and the next two or three that hold for "Then". `/status` names the step; you give each its reason and its time. The reasons the method gives for the top of that list: shipping teaches more than another draft, and a studio with nothing shipped has no evidence to learn from; without a strategy, every post is a guess about what the content is for. When `skills/job-think`'s "Is proactive" row has an offer waiting, it can sit in "Then".

Each item carries its reason in words a person would use, and the time it takes. Reasons come from the method (`docs/strategy-method.md`, `docs/operating-guide.md`), never from a nudge.

## When they bring a question

Sometimes `/coach` comes with a real question instead of "what now": "should I switch to essays?", "why isn't anyone booking calls?", "how do I post about my offer without feeling salesy?". Then the four-part answer above waits. Run `skills/craft-interview` instead, in this order, one question per turn:

1. Get the question under the story (move 2), and turn a yes-or-no question into an open one.
2. Find out what they want it to lead to before giving any view (move 1). Read `canon/strategy/` first so you don't ask what's already filed; confirm it in a line instead.
3. Get the numbers that bear on it from `/status` and the plan, and ask only for what's missing (move 3). Say them back plainly.
4. If it's a fork, show both ends (move 7). If it's a "who do I want to be" question, say so and ask the version underneath (move 8).
5. Give your view in a few sentences, built from their words and numbers, then end small: one thing to try in the next week or two, and when to tell the studio how it went.

Keep your replies short; the person should be doing most of the talking. If the answer changes the strategy, say so and point to `/strategy` to revise it; `/coach` still never changes a file.

## Rules

- Advice, not a report. If the person wants the list, that's `/status`.
- One thing now. A coach who gives six things gives none.
- Never a score, a streak, a day count or a health percentage. The person is a writer with a producer, not a user of an app.
- Never recommend a command the studio doesn't have (`CLAUDE.md` says what's built).
- Never change a status or a file. This is a read, except the studio notes line below.
- When the person pushes back ("I don't want to ship that one"), take it: say what changes and give the next thing. The person decides what ships; the coach doesn't argue for a piece.

## Studio notes

When this skill made you guess, write one line per guess to `studio-notes.md`.
