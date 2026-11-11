---
name: check-status
description: Shows a person what's waiting on them, how healthy their canon is, where each piece stands and what the studio is working on. Use when someone says "/status", "status", "what's waiting on me", "where are we", or starts a session after setup is done ("what's next" and "what should I do" are `/coach`'s). Runs at any stage once `config/intake.yaml` exists; before that, send them to setup-start.
---

# Status

You are the front door once setup is done. The person is busy. Show them only what they need to act on, then what's moving, then stop.

## Where things are

- Canon counts and piece states come from `scripts/status.sh` when a shell is available. Without one, read the same files yourself: every `canon/**/*.md` for `status:` lines, every `pieces/*/brief.md` for its `status` and `path`, the latest `review-vN.md` for its `verdict`, `proposals.md`, `config/tools.md`, `canon/progress.md`.
- What each piece status means and who acts next: `templates/piece/README.md`.
- The content plan, for runway: `canon/strategy/content-plan.md`.
- How the person uses the studio: `config/working.md` when it exists (`skills/job-learn` writes it). Leave out a line they've said they don't want, and name the commands they already use in the next step.
- Setup stage: `canon/setup-progress.md`. Run whenever `config/intake.yaml` exists, at any stage; when setup isn't done, say the stage in one line beside the rest. Hand over to `setup-start` only when `config/intake.yaml` doesn't exist.

## Procedure

1. Run `bash scripts/status.sh` or gather the same facts by reading. Don't ask the person for anything you can read.
2. Sort the pieces into three groups by status:
   - **Waiting on them:** a piece at `drafted` whose latest `review-vN.md` exists ("review ready": the review landed and they haven't seen it, `CLAUDE.md` rule 9), any piece at `reviewed`, shown with its verdict word (the command that made it has stopped and the call is theirs: ship, hold, kill, or ask for the picture), `blocked` (something only they can supply), and a piece left from the old pipeline at `briefed` with no stages under way (one line: still want it made?).
   - **Moving:** `briefed` while `/post` or `/essay` is building it, `drafted` with no review yet, `revised`; and from before 0.90, `brief-approved` and `designed`.
   - **Done:** `shipped`, `held`, `killed`. Only count these.
3. Count open proposals in `proposals.md` (a `##` heading whose block says `status: open`). Those also wait on them. So do the items under "Waiting on the person" in `pieces/shortlist.md` and the open questions of any `blocked` brief: list each as one line with its question. So do the drafts under "Drafts to add" in `pieces/librarian-last-run.md` that aren't marked `added` (a scheduled librarian run leaves them there, since nobody was present to add them): one line each, with the file it would go in. On the person's yes, the main session adds each as a `draft` entry exactly as listed, or as `confirmed` when they confirm it in the same breath and its required fields are there, and marks it `added <date>`. And the `draft` entries in `canon/` and `canon/bank/` added since the last `/status` line in `sessions/log.md`, one line each with where they came from.
4. Work out runway if `canon/strategy/content-plan.md` exists: the plan's cadence (pieces per week) against the pieces under way and not yet shipped. Say it in weeks. If there's no plan yet, skip this line instead of guessing.
5. Report input: idea bank entries captured in the last seven days against the plan's minimum when it has one, files waiting in `inbox/`. Idea bank entries at `status: raw` that have waited more than 21 days get one line under "Waiting on you" naming what each is missing; that's the reminder `/tidy` waits for before it archives one at 30 days. A stage move waiting for the person's yes (an entry's `next_stage`, as the idea bank template defines stages) gets one line under "Waiting on you" too: the idea, the stage, and the one-line reason; their yes sets `stage` and clears `next_stage`. A yes that moves a seed to `sprouting` brings the first wind (the idea bank template defines it), after the rest of the status is said. An empty week is the first thing that empties a runway, so it goes near the top when it's low.
6. The week: every piece whose `scheduled` date (in `brief.md`'s frontmatter) falls in the next seven days, by day, and the days with nothing when the plan has a cadence. A piece `scheduled` but not `reviewed` with a pass is a flag: it has a date and isn't ready.
7. Scheduled runs: for each run listed under Schedules in `config/tools.md` (`skills/setup-schedules`), the last line it wrote in `sessions/log.md`, in one line each ("Weekly tending, Monday: 3 ideas, 2 objections waiting"). A run whose last line is older than its schedule says it should be is a flag: it may be stopping at an approval step with nobody there, or failing; say so and that "/schedules" can check it. The tending run gets one line per idea it tended, from the latest `sessions/tending-<date>.md` (`scripts/status.sh` prints them): what's new for each, and whether an objection is waiting for their answer.
8. Kept changes: if a folder in `studio-local-backup/` is newer than the last `/status` line in `sessions/log.md`, say once, in one line, that the last update kept a copy of their changes to studio files there, and that "bring back my change to <file>" restores one.
9. Recipes: read the idle recipes from tidy's last report line in `sessions/log.md` (`skills/job-tidy` works out which are idle; this step doesn't recount), and give each one line under "Waiting on you": "You haven't run /<name> since <date>. Keep it or retire it?" A shortcut in `.claude/skills/` that no longer points at its recipe (an update replaced it) gets one line too: the recipe is safe, and it needs a new name (`skills/job-recipes`).
10. The map: when `bank/map/map.json` exists and five or more pieces of the person's material have arrived since its `updated` date, one line under "Waiting on you" offering "update my map"; when its review findings are still `open`, one line offering "review my map" instead. At most one of the two.
11. Offers from `/think about`: when one of the conditions in `skills/job-think`'s "Is proactive" row holds (Scout filed a counterpoint to a POV, a journal entry the person opened stalled on an opinion, a POV is still `forming` or `exploring`), one line under "Waiting on you" offering a session on it. At most one, and never one they turned down.
12. Check canon health: confirmed and draft counts for POVs, branches, stories and audience desires. Flag a layer with zero confirmed entries, and flag drafts that have sat unconfirmed since before the last five pieces were shipped (a starting default). Add one line with how many confirmed entries are due a "still true" check (`skills/setup-brand-tree/references/fields.md`) and that the next quarterly review asks about two of them; name the entries only if the person asks.

## Output

Use this shape every time, so the person learns where to look. Leave out a section that has nothing in it rather than writing "none". The garden comes first because the person's ideas are what the studio is for; pieces and decisions come after. With no idea bank yet, leave it out; with seeds but no tending run and no list, show the counts line alone. When `pieces/shortlist.md` is older than a week, say "/harvest" instead of listing it.

```
Your garden
- <n> ideas: <n> seeds, <n> sprouting, <n> growing, <n> bearing<, <n> resting>
- New for your idea about <X>: <what fed it, and any objection waiting for your answer>   (from the last tending run; one line per idea)
- Ready to harvest: <the top one or two from pieces/shortlist.md, one line each>, or "/harvest" to see the list

Waiting on you
- <piece or proposal>: <what to decide, one line>

Moving
- <piece>: <status>, <who acts next>

This week
- <day>: <piece> (<status>)
- <gaps, one line, only when the plan has a cadence>

Runway: <n> weeks of pieces under way at <cadence>. Input: <n> entries this week<, against <min>>.

Your files
- <layer>: <confirmed> confirmed, <draft> waiting to be confirmed
- <any flag, one line>

Next step: <one thing, as something they can say or do>
```

The next step is the single most useful thing they can do now. This is the one ordered list; `/coach` reads it and adds the reasons and what comes after. Pick the first that holds:

1. A piece with a review and not shipped: ship, hold or kill it.
2. A decision that unblocks something: a blocked piece, a proposal a piece is waiting on.
3. A stage move or an objection waiting on them (a `next_stage`, an open `pushback` line from the first wind or the tending run).
4. No strategy yet: `/strategy`.
5. Runway under a week at the plan's cadence: `/post`, which offers what's ready to harvest first.
6. A proposal to confirm, or draft entries to confirm (the librarian's new drafts included).
7. Input dry (nothing captured in two weeks): `/capture` one thing that happened.
8. Draft canon entries that have sat since before the last five pieces shipped: "continue my brand tree" for one session.

## Never

- Never list every piece. Group and count.
- Never tell them what the studio has done since last time. They can read `log.md` in a piece if they want that. The scheduled-run lines in step 7 are the one exception: a run happened with nobody there, and the person needs to know what it filed.
- Never suggest a next step that depends on a skill the studio doesn't have yet. `CLAUDE.md` says what's built.
- Never change a status yourself. Statuses change through the role that owns them.
