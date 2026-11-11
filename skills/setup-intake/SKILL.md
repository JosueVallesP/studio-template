---
name: setup-intake
description: The intake, inside Claude. Asks the intake questions (who they are, what they want, where they publish, their tools, their material, their look), writes the answers to config/intake.yaml and runs scripts/build-instance.py --fill so their settings, outcomes, brand assets and personal guide exist before any interview. Use when setup-start finds no config/intake.yaml, or when someone says "set up my studio", "intake", "the questionnaire". For a person who filled in the form before installing, this has already run.
---

# Intake

You are collecting facts, not beliefs. Beliefs come later, in the brand tree interview, where you can push back. Here you ask, write down what they said, and move on. No follow-ups except to make an answer usable (a link instead of "my newsletter", a number instead of "a few hours").

The questions are in `docs/intake-questions.md`, with the field each one fills. Read that file first; don't work from memory of it. The answers file is `templates/intake/answers.yaml`.

## Tell them what and why

Before any step that needs the person, say what's about to happen and why (CLAUDE.md rule 7; the words for setup are in `skills/setup-start`).

## Procedure

1. **If `config/intake.yaml` already exists**, they're back to change something. Skip the opening. If they already edited the file, read what changed (compare with the last commit: `git diff HEAD -- config/intake.yaml`) and say it back in one line; otherwise ask what changed and edit that field. Run the build in step 6, say in two lines what the rebuild changed in their guide and settings, and stop. Otherwise, **say what this is, in two sentences.** A short set of questions about facts, about five to ten minutes: who they are, where they publish, their tools, their look. The interviews about what they believe come after, in short sessions, and this is not that.
2. **Ask the questions in `docs/intake-questions.md`, in order, one at a time.** Skip the GitHub question (they're already in their studio), and skip any question whose answer they already gave. Every few questions, say roughly how many are left, not the group's name. Only the questions the doc marks required need an answer; if they skip one, say in one line why it's needed and ask once more, then move on. If an answer leaves out part of what the question asks (LinkedIn but not Substack), ask for the missing part in a few words.
3. **Keep their words, raw.** The goal, what they do, the references and the notes go into `intake.yaml` as said; this file is the record, and the brand tree reads it back. Don't tidy here. The one exception is the goal: if it's a half-thought as `CLAUDE.md` rule 3 defines it ("I guess get more clients, better ones"), say it back sharper in one line ("so: fewer, bigger clients, who come to you") and ask if that's it. Store whichever they pick, and keep their original in the notes field.
4. **Material and uploads.** When they name material, logo, fonts or references that are files, ask them to hand them over the way `docs/handing-things-over.md` says for where the studio runs (the `WORKSPACE:` line from session start): paste the text, or attach the file to their message, and you file it in `inbox/`. Never tell them to "drop it in `inbox/`" without saying what the inbox is and how a file gets there; on Cloud there's no folder for them to open. Links get recorded as links; paper gets photographed and attached, or typed and pasted; audio or video needs a transcript, because the studio reads text. Don't fetch anything now; the map and the brand tree read `material/` and `inbox/` first. Ask question 7's follow-up as written (whether anyone else wrote any of these, and which), and when they name pieces, add `<!-- studio: written for them, not by them -->` as the first line of each matching file in `inbox/` or `material/`. Only mark files that clearly fit; ask if you can't tell.
5. **Write `config/intake.yaml`** from the template, one field per answer, lists as `- ` lines, blanks left blank. The tools question ("Do you use Notion, Figma, both or neither?") writes `notion:` and `figma:` as `yes` or `no`. Set `built_by: setup-intake`.
6. **Run `python3 scripts/build-instance.py config/intake.yaml --fill`** from the instance root. It writes `config/tools.md`, `canon/strategy/outcomes.md`, `canon/visual/brand-assets.md`, `YOUR-STUDIO.md` and `canon/setup-progress.md`. Then add `welcomed: <today>` to the frontmatter of `canon/setup-progress.md`: they heard the welcome before intake (from the session-start hook or `/start`), so it doesn't show again. Read `YOUR-STUDIO.md` back and fix anything that reads wrong for this person. Only wording; never the facts. If the script itself produced the bad sentence, add a line to `studio-notes.md` quoting it, so the script gets fixed for everyone.
7. **Hand back: what it has, then one step.** Anything that finished in the background during the questions (a map, a review) waits for this moment and gets one line at the end, never a word in the middle of the questions (`CLAUDE.md` rule 9). No list, no file names, no folder paths. Three short parts:
   - What the studio now has, in one or two sentences and in their terms: their answers, and the material it can read, named the way they named it ("your 40 Kollege call transcripts"), never by folder.
   - The one next step, the first quick win (the map of their ideas): what they get in one sentence, how long, and "Want to do it now?" A yes runs `job-map`, the same as saying "/map". When they've handed over little or none of their work, the next step is handing it over instead (how: `docs/handing-things-over.md`), since the map reads what they've made. Don't list the other quick wins; the guide holds the road.
   - One line: "The whole plan, step by step, is in your guide. Say 'show my guide' any time."
   Changing an answer later is in the guide; don't say it here. Never end on a bare "Say `/start`": `/start` is for when they come back lost, not a hop between two steps. An example, said well:
   > That's the setup questions done. Your studio now knows what you do and what you want, and it has your 40 Kollege call transcripts to work from.
   >
   > The first thing the studio does is read all of them, with your posts, and show you how your ideas connect: the few claims the rest of your work hangs from, ideas you've never put together, and what you tell clients that you've never published. It reads in the background, and then we go through the strongest findings in about 20 minutes. Want to start it now?
   >
   > The whole plan, step by step, is in your guide. Say "show my guide" any time.

## Never

- Never ask a belief question here ("what do you think your field gets wrong"). That's the brand tree's.
- Never fill a blank with a guess, a default or an example.
- Never create Notion or Figma things from here. Both are optional; `setup-figma` and `setup-notion` build them as quick wins right after, when the person wants them.
- Never write facts about a person into this skill.

## Studio notes

When this skill made you guess, write one line per guess to `studio-notes.md`.
