# Notes for the skills' author: first session with Tomás Reyes

Run on 2026-10-23 against a fresh instance (studio 0.10.0). Full exchange in `TRANSCRIPT.md`. I played both sides and followed the skills as written, so what follows is what the skills made happen, not what I'd have chosen.

## How many files I read before the person heard a word

36 files to run one first session:

- 10 for `/start`: CLAUDE.md, `.claude/skills/start/SKILL.md`, `skills/setup-start/SKILL.md`, its 2 templates, `config/tools.example.md`, `canon/README.md`, `inbox/README.md`, `pieces/README.md`, `studio-source.md`. (The last four weren't required; I read them to check the layout. The first six are.)
- 26 for the brand tree: `SKILL.md`, 4 references, 20 templates, plus `templates/piece/README.md` because setup-start points there for a later stage.

The 20 templates are the problem. Step 5 says "create the canon files from `templates/`" and the only way to know what that means is to open all of them. A manifest line in SKILL.md ("create these 17 files; not these 3") would cut the reading in half and remove a guess (see below).

## Where setup-start was unclear or made the person wait

1. **The welcome and the brand tree explain the same thing twice, back to back.** `setup-start` step 2 says: files about what you believe, several short sessions, nothing invented. Two minutes later `setup-brand-tree` step 1 says: files about what you believe, several short sessions, you can stop any time. Tomás said "You told me most of that already. Go." A real impatient person would. Either the brand tree skill should skip step 1 when `canon/setup-progress.md` exists (it means `/start` already did the welcome), or setup-start should drop its version and let the brand tree explain. The only new facts in the second explanation are "answer by voice" and "I'll push back". Keep those two sentences, cut the rest.

2. **Two "say two things plainly" sentences land after the questions, before the next step, with nothing to attach to.** "This takes about a year" and "the studio drafts from what you give it" are true and useful, but they arrive as a lecture between the third question and "here's where you are". A person who just said "I publish nothing" doesn't yet have anything to be patient about. Move them to the "Setup done" stage, or to the first-piece stage, where they mean something.

3. **The year-from-now question comes before the person knows what the studio does for them.** Tomás answered it fine, but the sequence is: four sentences of what the studio is, then "what do you want to have happened a year from now". The vehicle session asks the goal again later ("What do you want to have happen in the next year or two? Be specific"). Two near-identical questions in two sessions. Either make the welcome question the goal (and have the vehicle session refine, not re-ask), or say in the welcome that this is a rough first answer and you'll come back to it. The outcomes template already says "the goal in vehicle.md refines this", so the intent is there; the person never hears it.

4. **The Notion/Figma question is dead weight for someone like Tomás.** He said "No. Neither." and the skill then forbids mentioning tools until setup is done. So the question's only effect in the first session was to make him wonder why he was asked. If the answer changes nothing for months, ask it when it matters (the "Setup done" stage already says this is "the first time the tools come up", which contradicts asking at the welcome).

5. **Step 3's stage table can't be wrong on day one, but the skill still says to "update setup-progress.md to match" right after creating it from a template that already says "brand tree, not started".** Harmless, but the log ends up with two lines for one session. Fine; just noting that the template and step 3 overlap.

6. **"Don't explain the whole setup sequence"** is good, and it worked. The one next step was clear. This is the part of setup-start that held up.

## Where setup-brand-tree was unclear, contradictory or repetitive

1. **Intake Q2 has no branch for "I have material but not with me."** The skill routes on "lots / some / none", and routing.md counts "nothing" as none. Tomás had two talks and a folder of proposals on his drive and offered a story instead. Nothing tells the studio what to do: route as "none" and ask for the material next session (what I did), or stop and wait, or take the story now. This will be the common case. Most people arrive knowing they have stuff they haven't dug out. Add one line: "If they have material but haven't shared it, route on what's in hand, write what they'll bring into progress.md, and plan extraction for the next session."

2. **Session plan in routing.md and the entry point disagree about what session 2 is.** Routing says "strong opinions, little material: start with POVs" and the typical plan puts POVs in session 3, values in session 2. For a POV start, the plan should swap 2 and 3, the way it says the thesis start swaps 2 and 4. It only names swaps for the thesis and business starts. I guessed and put more POVs plus extraction in session 2.

3. **Step 5 "create the canon files from templates/" doesn't say which.** `templates/` holds 20 files. Three are written by other skills (content-plan.md by strategy-brand, channels/channel.md by strategy-brand, core-summary.md at minimum canon). progress.md's table lists content-plan and core-summary as "not written", which suggests they shouldn't be created, but SKILL.md doesn't say so. I created 17. Name them.

4. **"Fill in what's known so far" at step 5 pulls against "don't put words in their mouth".** Known so far: his year-from-now answer (already in outcomes.md), his job, his two client types. Do I copy the goal into vehicle.md? Make G1 and G2 from "city governments" and "developers"? I did both as drafts with sources, but it's a judgment call the skill should make. Suggest: copy the goal from outcomes.md into vehicle.md as draft (the template already says the vehicle refines it), write intake answers only into progress.md "About them", and leave every other file at template.

5. **Step 5 comes after step 3 and 4 in the text but the files should exist before the interview loop starts writing entries.** In practice the order is fine (create, then interview), but the heading order "Explain, Intake, Route, Extraction, Create files" reads as if files come last. A person watching the studio pause to create 17 files right before the first real question gets a dead moment. It's one message; just say what's happening, which I did ("Your canon files exist now").

6. **Ending step 4 was written for a chat without a file system.** "Remind them to save progress.md and the canon files (or keep them in the project) and to start the next session by sharing them." In the repo they're already saved, and `/start` or "continue my brand tree" finds them. Telling Tomás to "share" files that are sitting in his folder is confusing. The skill should say: in the repo, say where the files are and the phrase to resume; elsewhere, print them.

7. **Stories aren't confirmed by the skill's own flow.** The rules say an entry is confirmed only when they've said it's right, and S1 was told once and never read back. P1's read-back mentioned "saved as story S1" and he said yes to P1, which the rules say isn't confirmation of S1's parts. So S1 stays draft after a 25-minute session in which the person told a full, dated, permissioned story. The questions.md "Stories" section lists the parts to get (when, who, what they said, what happened after, permission) but not a read-back step. Add: "After the story's parts are in, read back the `what` and `result` lines and the permission, and confirm it in the same breath as the entry it supports." Otherwise every story waits a session.

8. **Permission question wording is heavy.** fields.md: "Can that story appear in public as it is, with names removed, or not at all?" I said it with "with the town and the firm named, with the names removed, or not at all", which is seven more words than a person needs. The skill could allow "Can I use that one with names, without names, or not at all?"

9. **`from` on every POV points at value IDs that don't exist yet when you start from POVs.** Both P1 and P2 have `from: <V IDs, not yet found>`. Routing explicitly says POV-first people get values later ("ask why each opinion matters to them, which leads down to values"), so the field is always empty in session 1 for this route. Fine, but fields.md should say the `from` field fills when values are found, so a stricter run doesn't try to ask "which value is that from?" of someone with no values written down.

10. **The capacity question is orphaned.** questions.md puts "How many hours a week can you give this, honestly" under Content plan, which isn't asked in the interview, and says to record it in vehicle.md under constraints. The vehicle template has no constraints section. No session in the plan owns it. Tomás has about three hours a week and nobody asked. I added a "Constraints" section to his vehicle.md so it has a home. Assign the question to the vehicle session (6), or to the welcome, where "three hours" is the kind of thing someone says next to "LinkedIn".

11. **"Check in at natural breaks, roughly every 20 to 30 minutes."** With a 25-minute first session, the first natural break and the end of the session are the same moment. That's fine, but the skill also says session 1 covers "intake, routing, extraction, and the first layer from the entry point". With no extraction, the first layer got one confirmed entry in the time left. Setup-start promises "about half an hour". Both are honest; the person just leaves with one POV. Worth saying in setup-start's promise: "You'll leave with one or two things written down in your words, not a finished tree."

12. **Praise rule held, but "Noted" and "Changed" are the only neutral acknowledgements available, and they sound curt in a row.** Not a contradiction. The rule is right. Just flagging that the studio's turns read clipped (Noted. Changed. Confirmed.), and a person who talks out loud may read that as cold. A single line in the writing rules, "acknowledge by restating what you captured, not by rating it", would give the studio something to say.

## What a real person would find confusing or long

- The welcome's "Your words." after question 1 reads as an instruction to a transcript, not to a person.
- The brand tree explanation uses "canon" without saying what it is; setup-start says "those files are your canon" once and never again. Pick one word and define it once, or don't use it with the person at all. "Your files" is enough.
- The intake Q2 list ("Posts, essays, a newsletter, talks, podcast appearances, a book, sales pages, course material, client results") is nine items read aloud to someone who publishes nothing. Shorten to "talks, proposals, anything you've written or said in public" and let them name the rest.
- "Then it stays at forming" needed explaining. Tomás didn't know what "forming" means; the studio said "it won't feed content as a settled opinion before that", which is the explanation. The skill should give that sentence, not the label.
- The end-of-session summary is five sentences. Right length. The "share them and say continue" reminder is the only wasted one (see 6 above).

## What got created and whether it matches the templates

By `setup-start`:

- `canon/strategy/outcomes.md`: matches template. His answer word for word in `want`. `measured by` filled from his own "two or three of those jobs a year", not invented.
- `config/tools.md`: copied from `tools.example.md`, both tools `connected: no`, channels line set. The example's first paragraph ("Copy this file to config/tools.md") is still in the copy, which is template residue a person will see. The example should lose that line or the skill should strip it.
- `canon/setup-progress.md`: matches template; welcome ticked, stage "brand tree, not started", two log lines.

By `setup-brand-tree` (17 files):

- `canon/progress.md`: matches template; About them, layer table, minimum canon checklist (P1 counted as 1 of 5), session plan adjusted for the POV start, next session, log.
- `canon/canon-index.md`: matches; P1 confirmed, P2 draft, S1 draft, G1 and G2 draft, G2 added as a second row (template only has G1).
- `canon/person/povs.md`: P1 confirmed with every field except `from`; P2 draft, confidence forming, limits empty with his words on why.
- `canon/bank/stories.md`: S1 draft, raw word for word, permission anonymized with his reason.
- `canon/vehicle/vehicle.md`: goal copied from outcomes as draft; business paragraph from intake marked as such; a `Constraints` section the template doesn't have.
- `canon/strategy/brand-strategy.md`: G1 and G2 named from intake, every other field marked not yet asked.
- Template copies with only owner and date filled, nothing else: `person/values.md`, `behaviors.md`, `philosophy.md`, `thesis.md`, `branches.md`, `stop-list.md`; `bank/proof.md`, `ideas.md`, `questions.md`, `evidence.md`; `strategy/audience.md`; `voice/voice-guide.md`. These still carry their `## V1 · <short name>` placeholder blocks, and `scripts/status.sh` counts them. I ran it against this canon: it reports `values.md: draft=1`, `behaviors.md: draft=1`, `thesis.md: draft=1`, `philosophy.md: draft=1`, `voice-guide.md: draft=1`, `stories.md: draft=1` (that one is real), `brand-strategy.md: draft=3` (two real, one is the frontmatter `status: draft`), and `ideas.md: ready entries: 1` and `proposals: open: 1` for files that hold only their template example. A person running `/status` after session 1 would see 14 drafts when they have 3. Either the skill strips placeholder blocks when it creates the files, or the script skips any entry whose heading contains `<`, or the templates keep their examples in a comment. The script also flags `strategy/content-plan.md: missing`, so it expects the file the brand tree skill (by my reading) shouldn't create; one of the two needs to change.

Not created, by guess: `strategy/content-plan.md`, `strategy/channels/`, `core-summary.md`. `canon/setup-progress.md` still says "brand tree, not started" because setup-start owns it and the brand tree skill never touches it; `/start` will re-derive the stage next time. Between sessions it's stale.

Five run guesses went into `studio-notes.md`.

## The short version

The front door works: one next step, said as a phrase, and he said it. The costs are the double explanation, a goal question asked twice across two skills, a tools question with no consequence, a missing branch for "material exists but isn't here", and a story that a person told in full and that the skill's own confirmation rule leaves as draft. Fix the first and the last two and session 1 gets a confirmed POV and a confirmed story in the same half hour.
