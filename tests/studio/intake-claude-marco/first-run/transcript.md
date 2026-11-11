# Transcript: Marco Bellini's first session in a bare studio

Date: 2026-10-22. Instance: this folder, fresh from the studio repo, nothing filled in. Both sides played by the tester. The studio follows the skills as written; Marco answers only with what the brief gives him.

[Read before Marco heard a word: `CLAUDE.md`, `.claude/skills/start/SKILL.md`, `skills/setup-start/SKILL.md`. Then step 1 of setup-start: looked for `canon/setup-progress.md` (absent), `canon/progress.md` (absent), `config/tools.md` (absent), listed `pieces/` (only `README.md`). Also looked at `canon/README.md`, `pieces/README.md`, `inbox/README.md`, `config/tools.example.md` to know what the folders hold. No `config/intake.yaml`, so this is first contact.]

---

MARCO: /start

STUDIO: This is a content studio. It learns what you believe, what you've done and how you talk, and writes that down in a set of files, your files. From those files it produces posts and visuals that sound like you. It drafts from what you give it (your videos, your workshop notes, stories, anything you've written) and from a few interviews, and you make the call on every piece. Nothing gets invented about you; if the studio doesn't know something, it asks.

Here's the road. First, about ten minutes of questions about facts: who you are, where you publish, how much time you have, what you already have. That gives you your settings and a one-page guide written for you. Then, if you have material, the studio reads it and shows you what it found before it asks you anything. Then a few short interviews to confirm and fill the gaps. Then the strategy, every choice with its reason, for you to say yes or no to. Then your first post through the whole crew. A few weeks, at your pace.

Say "set up my studio".

[Wrote nothing. The step 3 table says intake creates `setup-progress.md`.]

---

MARCO: set up my studio

[Read: `skills/setup-intake/SKILL.md`, `docs/intake-questions.md`, `templates/intake/answers.yaml`. Also read `templates/intake/your-studio.md`, `templates/intake/brand-assets.md` and `scripts/build-instance.py` to know what the build would write.]

STUDIO: This is about ten minutes of questions about facts: who you are, where you publish, your tools, your look. The interviews about what you believe come after, in short sessions, and this is not that.

First group: about you.

Your name, as you'd like it to appear.

MARCO: Marco Bellini.

STUDIO: What do you do, and who do you do it for? A few sentences, the way you'd say it to someone at a dinner.

MARCO: I make furniture by hand in Bologna, and I teach amateurs how to make it. People come to my workshop for a few days and leave with a piece they built themselves.

STUDIO: Your business or practice, if it has a name.

MARCO: Skip that.

STUDIO: Where are you based, and in which language will your content be?

MARCO: Bologna.

[Marco answered half the question. The skill says follow up only to make an answer usable; a blank language is usable, so no follow-up. Guess, noted in `studio-notes.md`.]

STUDIO: Next group: what you want.

A year from now, what do you want to have happened because of this content? Clients, a book, a reputation for something specific. In your own words; a rough answer is fine, the interview comes back to it.

MARCO: I want my workshops filled a year out instead of month to month.

STUDIO: How would you know it happened? A number, a kind of client, a phone call you'd get. Leave it blank if you don't know.

MARCO: Next year's workshop dates are booked by this time next year.

STUDIO: Next group: where and how often.

Where do you publish now? LinkedIn, a newsletter and where it lives, a podcast, a site, YouTube, nowhere yet.

MARCO: YouTube, about 3,000 subscribers. And Instagram, which I hate.

STUDIO: Where do you want to start publishing, if anywhere new?

MARCO: Nothing new.

STUDIO: About how many hours a week can you give this when work is busy?

MARCO: Five.

STUDIO: Who else touches your content? An assistant, a designer, a team, nobody. Names and what each one does.

MARCO: Skip.

STUDIO: Next group: your material.

What have you already made that shows how you think? Posts, essays, a newsletter, talks, a podcast, a book, course material. For each, where it lives: a link, an export, a folder you'll send.

MARCO: Forty YouTube videos. I could export the transcripts. And a handwritten notebook of workshop notes.

STUDIO: Where are they? If the transcripts are files, drop them in `inbox/`. Where is the notebook?

MARCO: The transcripts I'd have to export, I haven't yet. The notebook is on paper, on my bench.

STUDIO: Do you have recordings or transcripts of yourself talking? Sales calls, podcast appearances, workshops, voice memos. These matter more than polished writing for getting your voice right.

MARCO: The same forty videos. That's me talking.

STUDIO: Next group: your tools.

Do you use Notion?

MARCO: No.

STUDIO: Do you use Figma?

MARCO: No.

STUDIO: Next group: your look.

Your logo, if you have one. If it's a file, drop it in `inbox/`.

MARCO: I don't have one.

STUDIO: Your colors, if you have them. Hex codes or a brand guide. If you don't, say so; the studio proposes some from your references.

MARCO: I don't have any.

STUDIO: Your fonts, if you have them.

MARCO: No.

STUDIO: Three things whose look you like. Brands, sites, posts, books, anything. One line each on what you like about it.

MARCO: Old tool catalogs. Japanese woodworking books. I don't have a third.

[No "one line each" came back and no third. The skill bans follow-ups except for usability. Moved on. Guess, noted.]

STUDIO: Three things whose look you can't stand. Same. This is the more useful of the two.

MARCO: The maker-influencer look. That's the one.

STUDIO: One word your look should never be. Corporate, playful, techy, luxury, loud, bland.

MARCO: Skip.

STUDIO: Last one. Anything the studio should know before it starts? A topic you won't touch, a client you'll never name, a word you hate.

MARCO: No.

STUDIO: That's all of them. Writing your answers down now.

[Wrote `config/intake.yaml` from `templates/intake/answers.yaml`, one field per answer, lists as `- ` lines, blanks blank, `built_by: "setup-intake"`. Videos recorded under both `material` and `recordings` (guess, noted). Then ran, from the instance root:]

```
$ python3 scripts/build-instance.py config/intake.yaml --fill
Filling the person's files
  wrote .../bare-studio/config/tools.md
  wrote .../bare-studio/canon/strategy/outcomes.md
  wrote .../bare-studio/canon/visual/brand-assets.md
  wrote .../bare-studio/YOUR-STUDIO.md
  wrote .../bare-studio/canon/setup-progress.md

Done. No tools wanted; the studio runs in files.
Then: open the instance in Claude Code and say /start.
exit=0
```

[Read back `YOUR-STUDIO.md` as step 6 says. Three lines read wrong. As written by the script:

1. "You publish on YouTube (about 3,000 subscribers), Instagram (I hate it), and you can give this about 5 hours a week." Changed to "You publish on YouTube (about 3,000 subscribers) and Instagram (which you said you hate), and you can give this about 5 hours a week."
2. "You'd know it happened by: Next year's workshop dates are booked by this time next year.." (double period, capital mid-sentence). Changed to "You'd know it happened when next year's workshop dates are booked by this time next year."
3. "the rest goes to the pieces themselves and whatever you keep feeding it (The same 40 YouTube videos, that's me talking; 40 YouTube videos; I can export the transcripts and drop them in inbox/; A handwritten notebook of workshop notes; it's on paper, on my bench)." Changed to "the rest goes to the pieces themselves and whatever you keep feeding it: the transcripts of your 40 YouTube videos, and your handwritten notebook of workshop notes."

Left alone (outside what step 6 allows): `canon/setup-progress.md` log line "wants I want my workshops filled a year out instead of month to month."; `config/tools.md` "Team: nobody else touches the content" written from a blank; `config/intake.yaml` `intake_date: ""` which the build did not fill. All in NOTES.md.]

STUDIO: Done. Three things exist for you now.

Your guide is `YOUR-STUDIO.md`, one page, written for you from what you just said. Your answers are in `config/intake.yaml`; edit that file any time and the guide follows. You said no to Notion and Figma, so the studio runs in files, which is all it needs.

Two things before the next step. Export the transcripts of your 40 videos and drop them in `inbox/`; the studio reads them before it asks you anything about what you believe. The notebook is on paper, so the studio can't read it as it is; when you want it in, tell me how you'd like to get it in and we'll sort that out then.

Say `/start`.

---

MARCO: /start

[Read: `.claude/skills/start/SKILL.md`, `skills/setup-start/SKILL.md` again (not from memory). Step 1: read `canon/setup-progress.md` (stage: brand tree, not started; intake ticked), `config/tools.md` (Notion no, Figma no, channels YouTube and Instagram); `canon/progress.md` absent; `pieces/` has no piece folders. `config/intake.yaml` exists, so phase 1 is done. Step 3: no `canon/progress.md`, so "Brand tree, not started". Step 4 says to read `config/intake.yaml` `material` and `recordings` and look in `inbox/`: material is named, `inbox/` holds only `README.md`. Updated `canon/setup-progress.md`: `last_session` already today, stage unchanged, added one log line.]

STUDIO: Hi Marco. Your studio is set up from your answers. Three things exist for you: `YOUR-STUDIO.md`, one page on how your studio works, written for you; your answers in `config/intake.yaml`, yours to edit; and since you said no to Notion and Figma, everything runs in files.

The road from here: the studio reads whatever material you give it and shows you what it found, then a few short interviews to confirm and fill the gaps, then the strategy with a reason beside each choice, then your first post through the whole crew. A few weeks, at your pace.

Intake is done. You're at the brand tree, not started. That's the set of interviews where the studio learns what you believe about furniture, teaching and the people who come to your workshop, and writes it down in your words. The first session takes about half an hour, you can stop at any point, and you'll leave it with one or two things written down in your own words, not a finished tree.

You named two things the studio should read first: the transcripts of your 40 YouTube videos and your handwritten notebook. Neither is in `inbox/` yet. Export the transcripts and drop them in `inbox/` before that session, and the studio reads them and shows you what it found before it asks you anything.

Say "start my brand tree".

---

MARCO: (runs the two scripts)

```
$ bash scripts/status.sh
STUDIO
  version: 0.12.0
CANON
  person/values.md: missing
  person/behaviors.md: missing
  person/povs.md: missing
  person/philosophy.md: missing
  person/thesis.md: missing
  person/branches.md: missing
  person/stop-list.md: missing
  bank/stories.md: missing
  bank/proof.md: missing
  vehicle/vehicle.md: missing
  strategy/brand-strategy.md: missing
  strategy/audience.md: missing
  strategy/content-plan.md: not yet written (strategy-brand writes it)
  voice/voice-guide.md: missing
INPUT
  no idea bank yet
  inbox files waiting: 0
PIECES
  none yet
PROPOSALS
  open: 0
TOOLS
  Notion: connected: no
  Figma: connected: no
  Publishing: channels: YouTube (about 3,000 subscribers), Instagram (I hate it)
exit=0
```

```
$ bash scripts/setup-check.sh
STUDIO FILES
  ok    CLAUDE.md
  ok    README.md
  ok    studio.manifest.yaml
  ok    templates/piece/brief.md
  ok    templates/piece/draft.md
  ok    templates/piece/review.md
  ok    templates/piece/log.md
  ok    templates/piece/final.md
  ok    templates/piece/index.md
  ok    templates/piece/shortlist.md
  ok    templates/proposals.md
  ok    templates/inbox/README.md
  ok    docs/operating-guide.md
  ok    docs/strategy-method.md
  ok    skills/setup-start
  ok    skills/setup-intake
  ok    skills/check-status
  ok    skills/setup-brand-tree
  ok    skills/strategy-brand
  ok    skills/role-capture
  ok    skills/role-strategist
  ok    skills/role-writer
  ok    skills/role-editor
  ok    skills/role-designer
  ok    skills/role-librarian
  ok    skills/role-producer
  ok    skills/fmt-linkedin-post
  ok    skills/fmt-post-visual
  ok    skills/craft-copylosophy
  ok    skills/craft-visual-philosophy
  ok    skills/craft-contradiction
  ok    skills/craft-human
  ok    skills/check-human
  ok    skills/setup-check
  ok    agent capture
  ok    agent strategist
  ok    agent writer
  ok    agent editor
  ok    agent designer
  ok    agent librarian
  ok    /start
  ok    /status
  ok    /capture
  ok    /brief
  ok    /review
  ok    /design
  ok    /librarian
  ok    /correct
  ok    /update
  ok    /check
SCRIPTS
  ok    scripts/build-instance.py
  ok    scripts/status.sh
  ok    scripts/check-human.py
  ok    scripts/check-mechanical.py
  ok    scripts/make-skill-zips.sh
  ok    scripts/update-studio.sh
  ok    scripts/setup-check.sh
  ok    python3 3.13.16
  ok    python modules
  ok    status.sh runs
MANIFEST
  ok    studio version 0.12.0
  ok    studio-source.md matches (0.12.0)
  ok    canon/
  ok    pieces/
  ok    config/
  ok    inbox/
  ok    canon/ is client-owned in the manifest
PERSON
  ok    setup-progress.md (stage: brand tree, not started)
  FAIL  canon/progress.md missing: the brand tree interview hasn't started
  ok    config/intake.yaml
  ok    YOUR-STUDIO.md
  ok    canon/visual/brand-assets.md
  FAIL  canon/canon-index.md missing
  FAIL  canon/core-summary.md missing
  FAIL  canon/bank/ideas.md missing
  FAIL  canon/bank/evidence.md missing
  ok    canon/strategy/outcomes.md
  ok    config/tools.md
  ok    proposals.md
  FAIL  canon/strategy/brand-strategy.md missing
  FAIL  canon/strategy/content-plan.md missing
  FAIL  no channel files
  FAIL  canon/voice/voice-guide.md missing
WRITING RULES IN THE CANON
  ok    no em dashes in canon/

setup-check: 9 FAIL. Fix these before the test piece.
exit=1
```

[The nine FAILs are all the brand tree and strategy not having run yet, which is right for this stage. Appended nine run guesses to `studio-notes.md`.]

Files written in this run: `config/intake.yaml` (by hand), `config/tools.md`, `canon/strategy/outcomes.md`, `canon/visual/brand-assets.md`, `YOUR-STUDIO.md`, `canon/setup-progress.md` (by the script; `YOUR-STUDIO.md` then edited for wording, `setup-progress.md` given one log line), `studio-notes.md` (appended), `TRANSCRIPT.md`, `NOTES.md`.
