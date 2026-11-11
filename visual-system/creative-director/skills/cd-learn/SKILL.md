---
name: cd-learn
description: Use after a batch of pieces or on a schedule. Reads the log of approvals and rejections across brands and turns the keepers into lessons and proposed rule changes.
argument-hint: "[brand slug | all] [since YYYY-MM-DD] [refresh] [mode:non-interactive]"
---

# /cd-learn

**Outcome:** the lessons from recent work that would otherwise be lost, written as learnings in `<ws>/learnings/`, and any rule changes they justify proposed as diffs for a person to accept.

**Done:** every log line and review round since the last run has been read; each candidate lesson passed or failed the durable bar with a reason; the studio owner accepted or declined each proposal; accepted ones are written; the run ends on one of the last lines below.

**Next:** better reviews and directions on the next brand. `cd-direction`, `cd-make` and `cd-review` load learnings automatically.

**Not:** a summary of what happened. A lesson earns a file only if losing it would cause the same mistake again.

## Step 0. Load

Resolve paths as `<plugin>/AGENTS.md` describes. Read `<ws>/context.md` and `<ws>/learnings/.last-run` (two dates: `learn:` and `refresh:`; if the file is missing, read everything).

Read, since the `learn:` date, skipping template folders:

- every brand's `log.md`, or only the named brand's;
- every round in each piece's `review.md`, including "Possible new defaults" notes;
- any files in `<ws>/learnings/proposed/` that a person hasn't decided yet.

## Step 1. Find candidate lessons

Look for patterns, not single events:

- The same kind of rejection on two or more pieces, or across brands.
- A person overruling a reviewer: a round flagged something and the approver approved anyway, or a round passed something the approver rejected. Either the rule or the reviewer is off.
- A tool behaving the same bad way more than once.
- A look the sameness reviewer listed as a possible new default on more than one piece.

## Step 2. Apply the durable bar

Read `references/durable-bar.md` before deciding any candidate. It holds the test that keeps the learnings folder from filling with noise.

For each candidate, write one line: passes or fails, and why.

## Step 3. Propose

Read `references/rule-edits.md` before proposing a rule change. It says when a lesson becomes a rule edit and how to show the diff.

- A passing lesson becomes one proposed learning file, in the format of `<ws>/learnings/README.md`. If an existing learning covers it, propose an update to that file instead.
- A lesson that changes what every brand must honor becomes a proposed edit to a rule in `<ws>/taste/rules/`.
- A lesson about a tool becomes a proposed edit to that tool's `hands/` notes, flagged for the plugin's maintainer.

Show each proposal to the studio owner as a diff, with the evidence lines. Apply only what they accept. Record each decision in `<ws>/learnings/log.md`, with their words.

## Step 4. Refresh

Run this step when `refresh` is in the arguments, or when the `refresh:` date is more than a month old. Check older learnings and `generic-tells.md` for staleness: a tell that no longer shows up in rejections, a learning that recent work contradicts. Propose removals or updates the same way, with evidence.

## Step 5. Close

Write today's date to `learn:` in `<ws>/learnings/.last-run` (and to `refresh:` if Step 4 ran). Add a line under Recent activity in `<ws>/context.md`.

## Non-interactive runs

Do Steps 0 to 2, write each passing candidate and its evidence to `<ws>/learnings/proposed/<date>-<slug>.md`, change nothing else, and end on `Learning proposed: <n> waiting on a person`. The next interactive run picks them up in Step 0.

## Last lines

- `Learning written: <n> lessons, <n> rule edits`
- `Learning declined: <n> proposals, none accepted`
- `Learning proposed: <n> waiting on a person`
- `Learning skipped: nothing durable`
