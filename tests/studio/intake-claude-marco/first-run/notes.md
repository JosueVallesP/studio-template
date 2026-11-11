# Notes for the author: the front door, run cold with Marco Bellini

Blunt, in the order a new person meets things. Quotes are from the files as they stand in this instance (studio 0.12.0).

## 1. How much gets read before he hears a word

Three files are required before the first `/start` can answer: `CLAUDE.md` (it says to read the skill), `.claude/skills/start/SKILL.md` (one line: "Read `skills/setup-start/SKILL.md` and follow it exactly"), and `skills/setup-start/SKILL.md` (about 120 lines). Then step 1 of the skill checks three files that don't exist yet and lists `pieces/`. I also read the four folder READMEs and `config/tools.example.md` to know what the folders hold, which a careful run will do every time. Call it 3 reads, 4 existence checks, 4 optional reads. Not heavy, but the welcome is composed each time from a paragraph of instructions ("Say in four or five plain sentences what the studio is..."), so no two people get the same welcome. If the welcome matters, write it out once and let the skill paste it.

The second `/start` reads the same three plus `canon/setup-progress.md`, `config/tools.md`, `config/intake.yaml` and `inbox/`. Fine.

## 2. The docs disagree with each other about who does what

The build moved to two phases in 0.12 and several files still describe 0.11.

- `README.md` still says "This is version 0.11" and, twice, that `/start` "asks two questions and then points you at the brand tree interview" ("Front door" bullet and "How to start" step 2). There is no intake in the README at all. A person who reads the README before typing `/start` is told the wrong road.
- `canon/README.md`: "setup-progress.md    where you are in setup (written by /start)". `setup-start` says "Setup progress: `canon/setup-progress.md`. The person owns it. Intake creates it." `setup-check.sh` sides with the old README: "FAIL  canon/setup-progress.md missing: /start hasn't run". Three files, two stories.
- `canon/README.md` also says "Say `/start` the first time, or "start my brand tree" to go straight to the interview." Going straight skips intake, so `outcomes.md`, `tools.md` and `YOUR-STUDIO.md` never exist. Either the brand tree skill must cope with that or this sentence has to go.
- `config/tools.example.md`: "`/start` creates `config/tools.md` from this file". `setup-start`: "Their tools: `config/tools.md`, copied from `config/tools.example.md`." Neither is true now. `build-instance.py` writes `tools.md` from a string inside the script, with a different shape (adds `wanted:`, `account:`, `language:`, a Team section). `tools.example.md` is dead and will mislead anyone who copies it by hand.
- The `tools.md` the script writes opens with "`/start` and the setup skills fill this in". `/start` never writes it.
- `setup-start` "Where things are": "Templates: `templates/setup-progress.md` and `templates/outcomes.md` in this skill's folder are what `build-instance.py` writes from". The script does not open them; the text is hard-coded in `fill()`. They have already drifted: the template says "sources: welcome, <date>" and "- <date> written at welcome", the script writes "sources: intake" and "written from intake"; the template's Notion line is "- [ ] Notion dashboard (if wanted; setup-notion runs when connected)", the script writes "- [x] Notion dashboard (not wanted)". Same for `templates/intake/your-studio.md`: the template's "## You" is "<name>, <what you do, as you said it>." and the script writes `Marco Bellini. In your words: "..."`. Pick one source of truth. Either the script reads the templates, or delete the templates.
- `templates/intake/your-studio.md` ends with "## Where you are in setup / <the stage line from canon/setup-progress.md, and the one next step>" and its header says "The studio keeps this file up to date as your setup changes". The script writes a fixed sentence there ("Intake done on 2026-10-22. Next: say `/start`...") and no skill ever touches `YOUR-STUDIO.md` again. `setup-start` doesn't update it. So the "one page written for them" tells them to say `/start` forever, including after setup is done, when `setup-start` itself says "`/status` is now their front door".

## 3. The questions doc and the answers template

Mostly aligned on field names. Where they aren't:

- Q4 is one question with two fields: "Where are you based, and in which language will your content be? `location`, `language`". Marco answered "Bologna" and nothing else. The skill lets me follow up only "to make an answer usable", and a blank language is usable, so `language` is blank and `tools.md` now says "language: <not given>". A double question in a one-at-a-time interview will lose the second half often. Split it, or make the skill ask for the missing half.
- Q13: "Do you use Notion? If yes, the workspace name, and whether you'd like the studio's dashboard ... built there. `notion`, `notion_workspace`". Three facts, two fields. There is no field for "I use Notion but don't want the dashboard". The script reads `notion: yes` as wanted ("wanted: yes"). Same for Q14 and Figma. Add a `notion_dashboard: yes/no` or drop the "whether you'd like" clause.
- Q11 and Q12 overlap whenever the material is video or audio of the person. Marco's 40 videos are both. He answered Q12 with "The same forty videos", so the yaml has them twice and `YOUR-STUDIO.md` listed them twice (see section 5). Say in Q12 "besides what you just named", or let the skill skip Q12 when Q11 already holds recordings.
- Q18 asks for "Three things ... with links or uploads. One line each on what you like about it." That's three asks in one question, and the template holds a flat list. Marco gave two names and no reasons. The script's `refs()` splits each item on the first colon to make "- reference: reason", which also means a reference with a URL in it ("Stripe docs https://stripe.com: the restraint") splits at "https" and prints "- Stripe docs https: //stripe.com: the restraint".
- Q15 to Q17 say "Upload." In Claude Code there is nothing to upload to. The skill's step 4 says to drop material in `inbox/` but says nothing about the look files. I guessed `inbox/`.
- Q16: "If you don't, say so; the studio proposes some from your references." Nothing built proposes colors (`setup-visual-identity` is in the "Not built yet" list in `CLAUDE.md`). The question promises something the studio can't do yet.
- The template's trailing comment: "# Filled by the build, not the form: intake_date / built_by". In `--fill` mode the build does not fill them. `main()` only rewrites the yaml when `os.path.abspath(answers_path) != os.path.abspath(rec)`, and in `--fill` they're the same file. After the run `config/intake.yaml` still says `intake_date: ""`. The skill's step 5 says "Set `built_by: setup-intake`" by hand, which is why that one isn't blank; `intake_date` has nobody.

## 4. How long intake felt and what a real person resents

21 questions, 7 group announcements, an opener and a hand-back: about 30 studio turns, each waiting on a model reply. The doc says "about ten minutes". One at a time in chat it is closer to twenty, and for Marco 11 of the 21 answers were "no", "skip" or "I don't have one". The groups that cost the most and gave the least:

- **Tools** (Q13, Q14): two separate turns to say no twice. For a woodworker these read as "this wasn't built for you". One turn: "Do you use Notion or Figma? If yes, which."
- **Your look** (Q15, Q16, Q17): three turns of "no" before the two questions that matter (Q18, Q19). Fold logo, colors and fonts into one question.
- **Q3** "Your business or practice, if it has a name" right after he said "my workshop". Resented.
- **Q10** "Who else touches your content? ... Names and what each one does." To someone with five hours a week and a 3,000-subscriber channel, this reads as a question for a different customer.
- **Q6** right after Q5. Marco's goal ("workshops filled a year out") is already its own measure, so Q6 made him say the same thing again.
- **Q20** "One word your look should never be" is hard to answer cold. He skipped it. The six examples help, but it's still a copywriter's question.
- The skill says "Say the group's name when you move to it, so they can feel the progress." Seven labels for 21 questions is a lot of ceremony. Say the count instead ("Six more").

Keep: Q2, Q5, Q7, Q9, Q11, Q12, Q19. Q19 ("the more useful of the two") got the sharpest answer of the whole intake.

## 5. The script's output for Marco, lines that read wrong

Quoted as written by `build-instance.py` before I touched anything.

`YOUR-STUDIO.md`:

- "You publish on YouTube (about 3,000 subscribers), Instagram (I hate it), and you can give this about 5 hours a week." Two problems. A two-item list joined with a comma, so the sentence runs on. And his first-person aside sits inside a second-person sentence. Q7 invites this ("a newsletter and where it lives") and the script copies whatever he said into every channel line: `outcomes.md`, `tools.md` and `status.sh` all now print "Instagram (I hate it)". Either separate the channel name from the note in the template, or strip parentheticals when joining.
- "You'd know it happened by: Next year's workshop dates are booked by this time next year.." Double period (the script appends "." to an answer that already ends in one) and a capital letter after a colon.
- "the rest goes to the pieces themselves and whatever you keep feeding it (The same 40 YouTube videos, that's me talking; 40 YouTube videos; I can export the transcripts and drop them in inbox/; A handwritten notebook of workshop notes; it's on paper, on my bench)." The script joins `recordings + material` with "; " inside parentheses, so his own semicolons collide with the separator, recordings come before the material they duplicate, and his asides ("that's me talking", "on my bench") land in his guide. Any answer longer than a label breaks this line. Use a list, or just "whatever you keep feeding it" with no parenthesis.
- "Intake done on 2026-10-22. Next: say `/start`" is correct today and wrong from the next session on (section 2).

I fixed the first three as step 6 allows ("Only wording; never the facts"). What I changed is in `TRANSCRIPT.md`. Step 6 only lets the skill touch `YOUR-STUDIO.md`, so the rest below is still in the files:

`canon/setup-progress.md`:

- "- 2026-10-22: intake done; wants I want my workshops filled a year out instead of month to month." The template's "wants <one line from outcomes.md>" plus a goal that starts with "I want" gives "wants I want". Quote the goal, or drop "wants".

`config/tools.md`:

- "## Team / - nobody else touches the content". Marco skipped Q10. The script's `bullets(lst(a.get("team")), "nobody else touches the content")` turned a blank into a claim. `setup-intake` says "Never fill a blank with a guess, a default or an example" and the script's docstring says "It never guesses: a blank answer stays blank." This is a guess. Write "<not given>" like the other blanks.

`build-instance.py`, things I didn't hit but will bite the next person:

- `channels = ... [f"{c[0].lower() + c[1:]} (wants to start)" ...]` lowercases the first letter of every wanted channel: "LinkedIn" becomes "linkedIn (wants to start)", "Substack" becomes "substack".
- `read_answers()` strips `\s+#.*$` from every value before it removes the quotes, so any answer with a space before a `#` is cut off and keeps a stray quote. Tested: `notes: "my handle is #marcomakes"` comes back as `"my handle is` (opening quote included). Hex codes survive only because they start the string.
- In `--fill` mode the closing line is "Then: open the instance in Claude Code and say /start." The person is already in Claude Code; the skill is about to tell them the same thing. Print it only in form mode.

The script otherwise did what it says: five files, correct frontmatter, Notion and Figma ticked as not wanted, no em dashes, outcomes in his words.

## 6. Did the second `/start` use what intake produced?

Yes. It greeted him by name from `setup-progress.md`, found Notion and Figma not wanted in `tools.md`, read `material` and `recordings` from `intake.yaml`, saw `inbox/` empty, and told him to export the transcripts before the brand tree session, which is the one useful new thing it said. The stage logic landed on "Brand tree, not started" because `canon/progress.md` doesn't exist. The one log line went in.

But it said almost nothing new. `setup-intake` step 7 ends with: guide is `YOUR-STUDIO.md`, answers in `intake.yaml`, tools run in files, "Say `/start`". `setup-start` step 2 then opens with: "name the three things that exist for them: `YOUR-STUDIO.md` ..., their answers in `config/intake.yaml` ..., and their dashboard and templates if `config/tools.md` says a tool is connected", then "say the road in one paragraph". Marco heard the three things twice and the road twice (welcome, then this greeting) inside ten minutes, and `YOUR-STUDIO.md` says the three things a third time. The skill has no branch for "intake happened in this same session". Add one: if `setup-progress.md` `started` is today and the log has only the intake line, skip the greeting and the road and go to step 4.

Two smaller things in `setup-start`:

- Step 3: "Update `canon/setup-progress.md` to match: the stage, today's date, and one line in the log. On the first session the template already says the right stage, so write one log line, not two." The "first session" with `setup-progress.md` present is the second `/start`, because the first `/start` (no intake) writes nothing per the table ("write nothing to `setup-progress.md`, intake creates it"). The sentence reads as if it's about the first `/start`. Say "the first session after intake".
- Step 4, "Brand tree, not started": "if they named material that isn't in `inbox/` yet, name it and ask them to drop it in before that session." A handwritten notebook can't be dropped in. The skill has no line for material that isn't a file. I asked him how he wanted to get it in, which is a question the skill didn't give me and the "Never ask" list arguably forbids.
- Step 4, "Brand tree, in progress": "Name how many of the minimum canon items are done out of nine." The Never list says "Never use "canon" ... with the person without saying what it means for them in the same sentence." The skill tells you to say "minimum canon items" to him. The word "brand tree" is also used to the person throughout without a gloss; I added one ("the set of interviews where the studio learns what you believe..."). Give the skill a sentence for it.
- The welcome says the first stage "gives them their settings and their own guide". A woodworker doesn't know what "settings" are in a folder of markdown. Say "where things are and a one-page guide".

## 7. The two scripts at this stage

`status.sh` prints 14 lines of "missing" for someone who has done everything asked of him so far. It doesn't print the setup stage, doesn't mention `setup-progress.md`, `outcomes.md`, `brand-assets.md` or `YOUR-STUDIO.md`, and the "CANON / none yet" branch can't fire because `canon/` now has `setup-progress.md` and two subfolders. Either print the stage from `setup-progress.md` first and hide the per-file list until the brand tree has started, or say "not started yet" instead of "missing". "Missing" reads as broken.

`setup-check.sh` fails 9 checks and says "Fix these before the test piece." All nine are the brand tree and strategy not having run, which is the right state. But the message tells a person at stage two to fix files only an interview can produce. The skill `setup-check` is meant to run at the last stage, and `/check` is a slash command anyone can type at any time. Have the script read the stage from `setup-progress.md` and, below "check", print "You're at <stage>; `/check` runs after your first piece ships" and exit 0. Also "FAIL  canon/setup-progress.md missing: /start hasn't run" names the wrong author (section 2).

## 8. What a real client would find confusing

- Three different ways to make the studio do things, met in the first five minutes: a slash command (`/start`), a quoted phrase ("set up my studio"), another quoted phrase ("start my brand tree"). The skill wants him to "learn" the phrases by saying them. Pick one mechanism for setup or explain in one line why both exist.
- "Brand tree", "the whole crew", "the strategy", "gates", "your settings" all arrive before they're explained. The Never rule bans "canon" but the rest get through.
- `inbox/` is the only way in, and it only takes files. Marco's richest material is on paper. Nothing in intake or `/start` tells him what to do about that; the honest answer is "photograph it and drop the photos in, or type it", and the skill should say which, because `/capture` has to be able to read it.
- Q16 and Q18 promise things ("the studio proposes some from your references", "links or uploads") the current build can't act on. He'll expect colors to come back.
- The hand-back says "edit that file any time", meaning `config/intake.yaml`. Nothing says the guide and `tools.md` don't update themselves when he does; he'd have to rerun the script, and nobody tells him the command. Either say "then say `set up my studio` again" and make the skill reread, or say nothing about editing.
- `YOUR-STUDIO.md` lists `/brief`, `/review`, `/correct` and "continue my brand tree" to a person who hasn't done his first interview. It's the right page a month from now. Today it's a menu for a restaurant that isn't open. Consider writing a shorter version at intake and the full one at "Setup done".
- The welcome says "A few weeks at your pace" and the "Setup done" text says "about a year before it works in a real way". He'll meet the second number eventually; better to say both at the start than to look like the goalposts moved.

## 9. Run guesses

Nine lines appended to `studio-notes.md`, one per guess, as `setup-intake` and `setup-start` direct.
