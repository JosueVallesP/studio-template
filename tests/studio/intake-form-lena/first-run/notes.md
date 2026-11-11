# Notes for the skills' author: Lena Okafor, first session from a form-built instance

Run on 2026-10-22, studio 0.12.0, instance built by the form (`built_by: form`). Full exchange in `TRANSCRIPT.md`. I followed the skills as written, so what follows is what they made happen.

## The short version

The form-built front door works. `/start` used her name, named the three files the form produced, saw the export in `inbox/` and named the two things that weren't there. The brand tree skipped the two intake questions it already had and read the goal back instead of asking it again. That is the improvement over the Tomás run, and it held.

What didn't hold: `/start` promises a read-back of her material "before asking anything", and the brand tree can't deliver it in a first session with 60 posts; three files the form built read like a template dumped a YAML list into a sentence; `setup-check.sh` has a voice-rule check that can never pass against the voice template; `status.sh` counts a frontmatter `status: draft` as an entry; and two stop-list facts she gave at intake sit in a visual file where the stop list will never look, so session 7 will ask her for them again.

## How many files before she heard a word

- `/start`: 7 files and 3 directory listings. `CLAUDE.md`, `.claude/skills/start/SKILL.md`, `skills/setup-start/SKILL.md`, `canon/setup-progress.md`, `config/tools.md`, `config/intake.yaml`, `YOUR-STUDIO.md`; listings of `pieces/`, `inbox/`, and a check for `canon/progress.md`. Two of those seven aren't in step 1's read list (see below).
- Brand tree, before its first question: 25. `SKILL.md`, 4 references, 20 templates. Step 5 names the 17 files to create, which is better than before, but you still open all 20 templates to know what each one's example block looks like so you can strip it.
- Total: 32 files for about twelve minutes of her time. The brand tree's 20 templates are still two thirds of it.

## setup-start

1. **Step 1's read list is missing the two files step 2 needs.** Step 1: "Read `canon/setup-progress.md` if it exists, then `canon/progress.md` if it exists, then `config/tools.md` if it exists. Count the pieces in `pieces/`." Step 2 then says "Greet them by name" and "name the three things that exist for them: `YOUR-STUDIO.md` ... their answers in `config/intake.yaml`". The name is only in `intake.yaml`. Add both to step 1. (The "Where things are" list above step 1 does name them, so this is a procedure gap, not a knowledge gap.)

2. **The road paragraph is written once, for first contact, and reused for the phase-1-done case.** Step 2 for the intake-done case ends "Then say the road in one paragraph, and go to step 3", but the only road text is the first-contact one, which starts "first ten minutes of questions about facts, which gives them their settings and their own guide". Lena already did that. I dropped the first stage and kept the rest; the skill should say so, or give a second, shorter road for people who arrive from the form ("material read-back, interviews, strategy, first post").

3. **The material read-back gets said twice in one message.** The road paragraph says "if they have material, the studio reads it and shows them what it found before asking anything", and step 4 for "Brand tree, not started" says "if material is there, say the studio reads it first and shows them what it found before asking anything". Both land in the same `/start` reply, three sentences apart. Keep it in step 4 (where it's tied to what is in `inbox/`) and cut it from the road.

4. **That promise is one the brand tree can't keep in a first session.** `/start` told Lena: "the studio reads your posts first and shows you what it found." `YOUR-STUDIO.md` says the same: "If you sent material, the studio reads it first and shows you what it found before asking anything." The brand tree's own plan says session 1 is "Intake, routing, extraction if the material is in hand, and the first layer from the entry point" in 20 to 40 minutes. Reading 60 posts back layer by layer is a session on its own. And `CLAUDE.md` "State of the build" lists "the extraction read-back before the interview" under *Not built yet*. So two person-facing files promise something the build says doesn't exist. Either stop promising it at `/start` or make extraction its own session when the material is more than a few posts, and say that at `/start`: "the first session reads your posts back to you; the questions start the session after."

5. **Recordings that aren't transcribed have no instruction.** Step 4: "if they named material that isn't in `inbox/` yet, name it and ask them to drop it in before that session." Lena's intake says "Four client onboarding calls, recorded, not transcribed yet." Dropping four audio files into `inbox/` does nothing the skills can read (`role-capture` reads text). I asked for transcripts. The skill should say what to do with audio: ask for a transcript, or say the studio can't read audio yet.

6. **Log line on the same day.** Step 3: "On the first session the template already says the right stage, so write one log line, not two." The built `setup-progress.md` already carried "2026-10-22: intake done; wants ..." from the form. I added a second dated line for `/start`, which is now two lines for one day. Harmless, but the skill's sentence assumes `/start` wrote the first line, and with the form it didn't.

7. **The half-sentence about Notion worked.** "You said you want Notion, so your dashboard gets built in Okafor Finance once Notion is connected; until then the studio runs in files." That's the right size. Keep the rule.

8. **`setup-start/templates/outcomes.md` is stale.** It says "Written at the welcome" and "sources: welcome, <date>", while the built `canon/strategy/outcomes.md` says "Written at intake" and "sources: intake". SKILL.md says "this skill no longer creates them itself", so either delete the two templates from this folder or point at the ones `build-instance.py` really uses.

## setup-brand-tree

1. **It did not re-ask what intake had.** Step 2's "Only if `what_you_do` is blank" and "Only if `material` and `recordings` are both blank" did their job. The vehicle question "Read back the year-from-now answer in `strategy/outcomes.md` and ask: 'Still true? What would you change?'" is the best moment in the session: she sharpened the goal ("before the panic") instead of restating it. Keep this pattern and copy it to the places below that still re-ask.

2. **Three questions later in the bank will re-ask intake anyway.**
   - Stop list: "Are there names, clients or companies you'll never mention?" and "What words make you cringe?" She already said "I'll never name a client. Never use the word 'unlock'" in the form. `build-instance.py` filed that under `canon/visual/brand-assets.md` "Notes from intake", a visual file. Step 5's fill rule says "Leave every other file at its template. Nothing else is known yet", so `stop-list.md` is empty and the stop list session will ask her again. Either route the intake `notes` field into `stop-list.md` as draft X entries at build time, or add them to step 5's list of what's known.
   - Brand strategy: "Where do you publish now, and where do you want to?" is in `intake.yaml` (`publishes_on`, `wants_to_start`) and already in `config/tools.md`. Make it a read-back like the goal.
   - Voice: "Share three to five pieces you wrote that sound most like you." She has 60 posts in `inbox/`. The skill should say "pick three to five from the export" rather than ask for pieces as if none were in hand.

3. **"Read them back in one sentence" produces a 70-word sentence.** Step 2: "read them back in one sentence so they know you have them." With five intake fields (what she does, channels, posts, checklist, calls) that's a run-on, which breaks the studio's own "written the way a person talks" rule. Say "in two or three sentences".

4. **Routing has two true rows and no tie-break.** Step 3's table: "Lots of material: Extraction, then confirm" and "Working business, no clear big idea (or answered b): Vehicle and client results". Lena is both. routing.md's size scale ("A book or years of posts counts as a lot. A few posts or a sales page counts as some") leaves 60 posts in the middle. I guessed: vehicle as the first layer, extraction read-back moved to session 2. Add one line: "When material is in hand and they also answered b or c, extract first and route the interview on their answer", or the reverse, but pick one.

5. **The "typical session plan" says what to swap for a vehicle start but not where extraction goes.** routing.md: "For someone starting from the business, session 6 moves to session 2." Fine. But with material in hand and session 1 spent on intake plus one question, extraction has no slot. I put it at the top of session 2 and pushed everything down a session. Say that's the move.

6. **Step 5's strip rule misses two kinds of placeholder, and `status.sh` counts them.** Rule: "strip the template's example entry (the block whose heading still holds `<...>`)". Two things survive it:
   - `thesis.md`'s block is headed `## T` with no `<`, so it stays, with eleven placeholder fields and a "Versions considered" bullet `- <date> "<earlier version>": <why it changed>`. `status.sh` happens not to count it (all fields are still `<...>`), but a person opening the file sees a form.
   - `philosophy.md` and `brand-strategy.md` carry `status: draft` in their frontmatter. `status.sh` counts a frontmatter status as an entry (`if (fm ~ rx) n++`), so after this session it prints `philosophy.md: draft=1` and `brand-strategy.md: draft=2` when the person has one real draft in each file at most (none in philosophy). `vehicle.md: draft=1` is the one true count. Either the script skips frontmatter or the templates don't put `status:` there.

7. **Step 5's fill list is good and I followed it; one item is a near-guess.** "name the client types from intake as draft segments (G IDs) in `brand-strategy.md`, marked as from intake." Her `what_you_do` gives one client type (seed-stage founders before their first real board meeting), so G1 is clear. For someone whose `what_you_do` names no client, the instruction yields nothing, and the skill doesn't say to leave the section empty rather than guess. One clause would do: "if `what_you_do` names no client type, leave it."

8. **Partial entries have no status rule.** "An entry is confirmed only when they've said it's right." She said the goal line is right after the read-back. But the Goal entry also has `known_for`, `do` and `learn`, two of which weren't asked, and the minimum canon says "Goal and target association (passed the two-directions test)". I left `status: draft` and wrote in the log that the goal line was agreed. A reader of `vehicle.md` can't tell from the status that the main line is hers. Say explicitly: "the goal stays draft until the two-directions test, even when the person has agreed the wording", or allow a per-field note.

9. **Vehicle `known_for` and brand strategy's target association are the same question twice.** Vehicle: "What would you need to be known for so that happens?" Brand strategy: "When someone hears your name, what's the first thing you want them to think of?" Lena answered the first with "the person who gets a seed-stage founder ready for their first board meeting", which is a target association in all but name. Session 8 will ask it again. Say in the brand strategy section: "Read back `vehicle.md` known_for and ask if that's the first thing, or something else."

10. **`progress.md`'s first line is chat residue and contradicts the ending step.** Template line: "Share this file and your canon files at the start of every session, then say 'continue my brand tree'." SKILL.md "Ending a session" step 4: "Don't ask them to share or upload files that are sitting in their folder." The file the person is most likely to open tells them to do what the skill forbids. Cut the line in the repo version.

11. **questions.md still says `/start` asks the capacity question.** Content plan section: "`/start` asks it at the welcome and records it in `strategy/outcomes.md` under Capacity." Since 0.12 intake asks it (`hours_per_week`) and `/start` asks nothing. Stale.

12. **Step 1's "two new things" worked.** Two sentences, then straight to intake. Lena didn't hear the studio explain itself twice. This fixed the loudest complaint from the Tomás run.

13. **Writing rule on labels worked but costs a clause each time.** "Don't use a studio label ... without saying what it means for them in the same sentence." Saying "a draft, which means it is in your file but it will not feed content until you have confirmed it" once was fine. If every draft entry earns that clause the session gets wordy. Suggest: define "draft" once in session 1, then use it bare.

## The scripts

1. **`setup-check.sh` voice check can never pass with the current template.** The check: `n="$(grep -cE '^- W[0-9]+' canon/voice/voice-guide.md)"; [ "$n" -ge 3 ]`. It counts lines that start `- W1`. The voice-guide template writes rules as headings: `### W1 · <short label>`. A person who confirms ten voice rules the way the template lays them out still gets `FAIL voice guide has 0 rules (need 3)`. Change the pattern to `^###? W[0-9]+` or change the template.

2. **`setup-check.sh` at the brand-tree stage prints 6 FAIL and "Fix these before the test piece."** All six are expected before the strategy exists (minimum canon, core summary, brand strategy, content plan, channels, voice rules). `/check` is meant for the Check stage, but `CLAUDE.md` routes "is everything working" to it at any time, and a person who tries it after session 1 reads six failures as a broken install. Make the PERSON block say "not yet: expected until setup reaches strategy" instead of FAIL when `setup-progress.md` says the stage is earlier than check.

3. **`setup-check.sh` reports the stage from `setup-progress.md`, which is stale after any brand tree session.** It printed `stage: brand tree, not started` with `canon/progress.md` sitting right there. The brand tree skill never touches `setup-progress.md` ("`setup-start` reads and updates this file") and `/start` only re-derives it when run. Any session that ends through "continue my brand tree" leaves the stage wrong until the next `/start`. Either the brand tree's "Ending a session" updates the stage line, or the scripts derive the stage the way `/start` does.

4. **`status.sh` frontmatter counting**: see brand tree note 6.

## The built files, as a person would read them

`YOUR-STUDIO.md` is the file she is most likely to open, and three of its sentences are a YAML list poured into prose:

- "You publish on LinkedIn, a newsletter (wants to start), and you can give this about 4 hours a week." She doesn't publish on a newsletter; the parenthesis contradicts the verb. Should read: "You publish on LinkedIn and want to start a newsletter."
- "Also touching the content: Rui, assistant: schedules posts and books calls." Two colons, no verb, the raw `team` line. Should read: "Rui, your assistant, schedules posts and books calls."
- "You'd know it happened by: Inbound conversations from founders I haven't met." A capital after a colon and a first-person "I" inside a "you" sentence. Should read: "You'd know it happened when founders you haven't met start conversations with you." (Or keep her words in quotes.)
- "the rest goes to the pieces themselves and whatever you keep feeding it (Four client onboarding calls, recorded, not transcribed yet; LinkedIn posts, about 60, export in inbox/linkedin-posts.csv; A board-prep checklist I send clients)." Three list items with their capitals and a first-person "I" inside a parenthesis. `setup-intake` step 6 tells the in-Claude path to "Read `YOUR-STUDIO.md` back and fix anything that reads wrong for this person (a list that came out as a run-on ...)". The form path has nobody doing that read-back, so form-built instances ship with the run-ons. Either `build-instance.py` renders lists as sentences, or `/start` does the read-back step on a form-built instance.
- "The studio keeps this file up to date as your setup changes." Nothing does. After this session it still says "Next: say `/start`, and it points you at the brand tree interview." `setup-start` doesn't touch it ("Never write anything into `canon/` other than `setup-progress.md`" is about canon, but the skill lists no write to `YOUR-STUDIO.md` either). Either a skill owns the "Where you are in setup" section or the file shouldn't claim to be kept current.
- "Where you are in setup ... If you sent material, the studio reads it first and shows you what it found before asking anything." See setup-start note 4; the build says this isn't built.

`canon/visual/brand-assets.md`: "Notes from intake: I'll never name a client. Never use the word 'unlock'." These are stop-list facts, not visual ones. The field is a catch-all `notes` box on the form, and the build puts it in the one file whose skill (`setup-visual-identity`) doesn't exist yet. The brand tree never reads this file. Her two clearest rules are invisible to every skill that writes.

`canon/setup-progress.md`: "- [x] Figma file (not wanted)" ticks a box for something that won't happen. A person reads a tick as done. "- [ ] Figma file: not wanted" or dropping the line would be clearer.

`config/tools.md`: "idea bank database: <id, set by setup-notion>" and four more `<...>` lines a person sees in their own tools file. Fine for the studio, odd for her. Since she's told the file is hers ("This folder belongs to the person"), the placeholders should say "not yet" in words.

`canon/strategy/outcomes.md`: correct and in her words. Good.

`canon/README.md`: lists `core-summary.md` and `canon-index.md` in the layout without saying the first one appears later, so after session 1 she sees a file promised that isn't there. Minor.

## What a real client would find confusing

- Being told at `/start` that the studio "reads your posts first and shows you what it found before asking anything", then having the first brand tree message start with questions. Lena would ask "what about my posts?" I had the studio correct itself mid-session, which is the honest move but shouldn't be needed.
- `/check` after a first session: six red FAIL lines.
- `YOUR-STUDIO.md` sentences that read like a form, in a file that says it was "written for how you said you work".
- The word "extraction" in `progress.md` ("Starting point: extraction / POVs / vehicle / thesis"). She'll read that file. "Reading your posts" is the plain version.
- "the two-directions test", "target association", "G1" in `progress.md` and `brand-strategy.md`, which the skill writes in files it then tells her are hers, with no gloss. The in-conversation rule about labels doesn't reach the files.

## What held up

- Greeting by name, naming the three files, half a sentence on Notion.
- Skipping intake questions 1 and 2.
- The goal read-back instead of a re-ask, and the follow-up "Be specific. What does it look like when it has happened?" which produced the only sharpening of the session.
- Step 1's two sentences instead of a second welcome.
- "Your files exist now; here's the first question" gave the pause a reason.
- Ending step 4: "Say 'continue my brand tree'" and "Bring the two talks" shape, adapted to the checklist and the transcripts.
