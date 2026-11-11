---
name: setup-schedules
description: >-
  Sets up the studio's scheduled runs: jobs that start on their own at a set time, in a fresh session of the person's studio, do one job and leave the result in their files and in /status. The ones the studio offers: a weekly tending run, a weekly librarian run, a tidy twice a week, and a weekly pull of their published numbers when a results source is connected. Every one is off until the person says yes. Use for "/schedules", "set up my schedules", "run scout every week", "tidy on its own", "what runs on its own", "stop the weekly tending", or when another skill offers a scheduled run.
---

# Schedules

Some jobs are worth doing every week whether or not the person remembers: coming back to their ideas with something new for each, counting what shipped and what they changed, clearing out what's gone stale. A schedule does those jobs while they're away, so the studio is a little ahead each time they open it.

A scheduled run is a fresh session of their studio that starts at a set time with one standing instruction. It can't ask the person anything, because nobody is there. So it only does jobs that need no answer, writes what it found to the files, and leaves every decision for the person's next session. That's the whole design: runs find and file; the person decides.

## What the studio offers

Offer only the ones that fit where the person is. Each is off until they say yes.

| Run | When | What it does | Offer it when | Skill it follows |
| --- | --- | --- | --- | --- |
| **Weekly tending** | Once a week, early on their first work day | Comes back to two or three of their ideas that haven't been touched in a while and brings each one thing that feeds it (a case, evidence, a story of theirs) and one thing that pushes against it (the best argument against); adds both to the idea's record and one line per idea in `/status` | They've confirmed at least two ideas (stage `sprouting` or later), or have confirmed points of view or a content plan | `skills/job-scout`, "The tending run" |
| **Weekly librarian** | Once a week, at the end of their week | Counts what shipped and what they changed between draft and final, keeps the body of work true, writes proposals for their yes | They've shipped pieces through the studio | `skills/role-librarian`, part A |
| **Tidy** | Twice a week (three or four days apart) | Moves expired outside entries and stale raw ideas to the archive, merges duplicates, archives shipped drafts, flags contradictions, compacts old log lines; never the canon, never deletes | The idea bank has started to fill | `skills/job-tidy` |
| **Weekly numbers** | Once a week, the day before the librarian | Pulls the published numbers for the last week's pieces from the results source and logs the signals the person's route watches | A results source is connected (`skills/setup-sources`) | `skills/setup-sources`, "Results" |

Not offered as a scheduled run, on purpose:

- **Anything that drafts.** A draft needs the person's material picked and a brief they approved. A run that drafts on its own makes pieces nobody asked for.
- **Anything that writes the canon.** Rule 6: only the person changes it. Runs write proposals at most.
- **A journal reminder.** A run can't wait for an answer, so it can't journal with them. A reminder is a calendar event or a phone reminder the person sets: offer the time they want and the one phrase to say when it goes off ("log today's story").

## Tell them what and why

Before any step that needs the person, say what's about to happen and why (`CLAUDE.md` rule 7). For this skill, in one short paragraph: some jobs are worth doing every week without them having to remember; a scheduled run does one of them at a set time and leaves what it found in their files and in `/status`; it never drafts, never changes what they've confirmed, and never decides for them; each is off until they say yes; setting them up takes about five minutes.

## Procedure

### 1. Read before you ask

Read `config/tools.md` (the Schedules section, the Sources section), `canon/strategy/content-plan.md` (their channels, cadence and which day they publish), `canon/person/povs.md`, `pieces/index.md` and `bank/ideas.md`. From these, work out which runs fit (the table above). If `config/tools.md` has `time zone:` under Schedules, use it; otherwise ask once: "What city or time zone are you in?" Write the answer as an IANA name (`Europe/London`) on that line.

### 2. Offer what fits, in one message

List only the runs that fit, each in one line: what it does for them and when it would run, with a time that suits their week (for example, scout on their first work morning, the librarian on their last work afternoon). Ask which they want. Also say once that every run uses a little of their Claude usage, the same as a short session.

### 3. Create each one

Use the scheduling tools this session has. They vary: load them through tool search if they're listed but not loaded, and go by each tool's own description. Use a tool that creates a scheduled task that starts a fresh session of this studio. Never use a tool that only schedules inside the current session (the local cron tools): it vanishes when the session ends and the person never finds out.

For each run:

- **Name:** what the person would call it: "Weekly tending", "Weekly librarian", "Tidy", "Weekly numbers".
- **When:** in the person's time zone, on the days and times they picked. Avoid exactly on the hour or half hour, when the tool's description asks for that.
- **The instruction.** Every run starts with no memory of this conversation, so the instruction stands on its own. Use this shape, filling only the run's own line:

  > This is a scheduled run of the content studio in this repository; nobody is watching, so don't ask questions and make no decision that belongs to the person. Read `CLAUDE.md`, then follow `<the skill and part from the table>` for its scheduled run. <The run's own line, below.> Write only where that skill says to write. End with one line in `sessions/log.md`: the date, the run's name and what it found, or that it found nothing. Then stop; the stop hook saves.

  The run's own line:
  - Weekly tending: "Run the tending run: two or three seeds, one feed and one push each, `tended` set, the report in `sessions/tending-<date>.md`; never change a stage; if a find contradicts a confirmed point of view, write the proposal, nothing more."
  - Weekly librarian: "Run part A on every piece that shipped since your last run; write proposals, never canon changes."
  - Tidy: "Run the full tidy, not the dry run; never touch the canon, the journal, `material/` or `inbox/`."
  - Weekly numbers: "Pull the numbers for every piece shipped in the last fourteen days from the results source in `config/tools.md`, as `skills/setup-sources` says under Results; if the source doesn't answer, write that one line and stop."

After each one is created, say in one sentence which approval setting it got, from the tool's result. If its runs will stop to ask for approval, say plainly that a run with nobody there to approve will stop at that step, and that they can switch the task to automatic approval in its settings, if their account allows it. Don't promise a setting the tool didn't report.

### 4. Record

Under Schedules in `config/tools.md`, one line per run: `- tending: Mondays 08:47 Europe/London · "Weekly tending" · set <date>`. The same for `librarian`, `tidy` and `numbers`. A run they turned down: `- tending: no`. A line still named `scout` is the same run from before 0.88; leave it. Tick the schedules line in `canon/setup-progress.md` if it has one.

### 5. Hand over

In three lines: what will run and when; where they'll see it (one line in `/status` and in `sessions/log.md` after each run, and the new entries or proposals waiting for them); and how to change it ("stop the weekly tending", "move tidy to Fridays", or "/schedules").

## Changing or stopping one

When they ask to stop, move or change a run, use the same scheduling tools to update or delete the task by its name, then rewrite its line in `config/tools.md`. Stopping one is never a loss to explain at length: say what it did, and that "/schedules" brings it back.

## Rules

- Off until they say yes, every one, every time.
- A scheduled run never drafts, never changes the canon, never decides, and never messages anyone.
- A run that finds nothing says so in one line. Silence looks like a broken run.
- Never create a schedule the person didn't pick.
- If no scheduling tool turns up, say once that this session can't set schedules, and that they can create a scheduled task for their studio from the Claude app with the instruction above, which you give them to paste.

## Studio notes

When this skill made you guess, write one line per guess to `studio-notes.md`: the date, the skill, what was unclear.
