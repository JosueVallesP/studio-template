# Transcript: first session with Lena Okafor

Run on 2026-10-22 against an instance built from the intake form (studio 0.12.0). I played both sides and followed the skills as written. Bracketed lines are what the studio read or wrote at that point, not things Lena saw.

---

[Read before anything: `CLAUDE.md`.]

LENA: /start

[Read: `.claude/skills/start/SKILL.md` (one line: read `skills/setup-start/SKILL.md`). Read: `skills/setup-start/SKILL.md`.]

[Step 1, "read before you speak": read `canon/setup-progress.md` (exists, stage "brand tree, not started"). Looked for `canon/progress.md` (missing). Read `config/tools.md` (Notion wanted, not connected; Figma not wanted; LinkedIn, newsletter wanted). Listed `pieces/` (only README.md, zero pieces). Step 2 needs her name and the three things that exist for her, so also read `config/intake.yaml` and `YOUR-STUDIO.md`, which step 1 does not list. Step 4 needs `material`, `recordings` and `inbox/`: listed `inbox/` (README.md and `linkedin-posts.csv`). Seven files and three directory listings before she heard a word.]

[Step 3: no `canon/progress.md`, so the stage is "brand tree, not started". The template already said that. Wrote one log line to `canon/setup-progress.md`: first `/start`, stage, next step, what is and is not in `inbox/`.]

STUDIO: Hi Lena. Your studio is set up from the answers you gave in the form. Three things exist for you already. `YOUR-STUDIO.md` is one page on how your studio works, written for you. `config/intake.yaml` holds your answers, and you can edit that file any time. You said you want Notion, so your dashboard gets built in Okafor Finance once Notion is connected; until then the studio runs in files.

Here is the road from here. Next, since you sent material, the studio reads it and shows you what it found before it asks you anything. Then come a few short interviews to confirm what it found and fill the gaps. Then the strategy: what you should be known for, to whom, where and how often, every choice with its reason for you to say yes or no to. Then your first post goes through the whole crew. A few weeks, at your pace.

Where you are: intake is done. The brand tree is next, and it has not started. Say "start my brand tree". The first session takes about half an hour, you can stop at any point, and you will leave it with one or two things written down in your own words, not a finished tree. Your LinkedIn export is in `inbox/`, so the studio reads your posts first and shows you what it found. Two things you named are not in `inbox/` yet: the board-prep checklist you send clients, and the four onboarding calls. Drop the checklist in before that session. The calls are not transcribed, so the studio can read them only once they are; if you can get transcripts, drop those in too.

LENA: Ok. Rui can transcribe the calls, I'll get him on it. The checklist is a PDF, I'll drop it in later today. Start my brand tree.

[Read: `skills/setup-brand-tree/SKILL.md`, `references/routing.md`, `references/questions.md`, `references/fields.md`, `references/tests.md`, and all 20 files under `templates/` (SKILL.md names 17 to create, but you have to open each to know what to strip). Checked for `canon/progress.md`: missing, so this is session 1. `canon/setup-progress.md` exists, so step 1 says only the two new things.]

STUDIO: Two things before we begin. Answering by voice works better than typing, because it captures how you really talk. And I will push back on vague answers. That is the point, not rudeness.

[Step 2, intake: read `config/intake.yaml` again. `what_you_do`, `material` and `recordings` are all filled, so questions 1 and 2 are skipped. Checked `inbox/`: `linkedin-posts.csv` is there; the checklist and the calls are not.]

STUDIO: From your form I have that you run finance for seed-stage startups, three at a time, as a fractional CFO, that founders hire you when their first real board meeting is coming and they cannot explain their own numbers, that you post on LinkedIn and want to start a newsletter, and that you have about 60 posts in `inbox/linkedin-posts.csv`, a board-prep checklist and four recorded onboarding calls, the last two not in the inbox yet. Two questions I do not have. First: do you think better out loud or in writing?

LENA: In writing, mostly. I think in spreadsheets and memos. I can talk, but I edit as I go.

STUDIO: In writing, then. I will give you a bit more room per question and still follow up on each answer. Second: which of these feels clearest to you right now?
a. What I believe about my field
b. What I sell and the results I get
c. The one big idea I want to be known for
d. None of them, honestly

LENA: b. I know exactly what I sell and what happens for the founders who hire me. The big idea, no. I have opinions but I would not call any of them "the" idea.

[Step 3, routing. Two rows of the table apply at once: "Lots of material: extraction, then confirm" and "answered b: vehicle and client results, then work backward". routing.md counts "a few posts" as some and "years of posts" as a lot; 60 posts sits between. Guess: the posts get extracted and read back, and the interview's first layer is the vehicle. Noted in `studio-notes.md`.]

STUDIO: Here is where I will start and why. You said what you sell and the results you get is clearest, so the interview starts with the goal and the business, and we work backward from your client results to what you believe. You also brought about 60 posts, so before the next interview question I read those and show you what I found, as drafts for you to confirm or kill.

[Step 4, extraction. Opened `inbox/linkedin-posts.csv`. In this test the file is a one-line stub with no post text, so nothing was extracted and nothing is shown below. In a real run this is where the studio reads all 60 rows and shows candidate entries one layer at a time: POVs she keeps returning to, stories, how she already phrases her big idea, the topics she repeats, and a first pass at voice (sentence length, words she uses, words she avoids). Each candidate would carry `status: draft`, its source (post date or row number), her exact words in `quote`, and a confidence of strong, medium or weak. Values would not be extracted from what she says she values, only from choices she describes. That read-back alone would fill the half hour, so for this short session the extraction is planned for session 2 and the studio moves to the first interview question instead.]

STUDIO: A correction to that: reading 60 posts back to you properly takes most of a session, and you have about ten minutes today. So I will do the read-back next session and use today for the goal.

[Step 5, create the files. Created 17 files under `canon/` from `skills/setup-brand-tree/templates/`: `progress.md`, `canon-index.md`, `person/values.md`, `behaviors.md`, `povs.md`, `philosophy.md`, `thesis.md`, `branches.md`, `stop-list.md`, `bank/stories.md`, `proof.md`, `ideas.md`, `questions.md`, `evidence.md`, `vehicle/vehicle.md`, `strategy/brand-strategy.md`, `audience.md`, `voice/voice-guide.md`. Stripped every example block whose heading holds `<...>`; set owner and date in the frontmatter only. Did not create `strategy/content-plan.md`, `strategy/channels/` or `core-summary.md`. Filled in what is known: the year-from-now answer from `canon/strategy/outcomes.md` into `vehicle.md` as the draft goal; the 4 hours into `vehicle.md` Constraints; her intake answers into `progress.md` "About them"; one segment G1 in `brand-strategy.md` from `what_you_do`, marked as from intake. Left the intake notes ("I'll never name a client. Never use the word 'unlock'") out of `stop-list.md`, because the skill says to leave every other file at its template. Noted both guesses in `studio-notes.md`.]

STUDIO: Your files exist now; here is the first question. In the form you said that a year from now you want "two or three new fractional clients a year coming to me, instead of me chasing them through referrals", and that you would know it happened by inbound conversations from founders you have not met. Still true? What would you change?

LENA: Still true. One thing I'd change: I want them to come before the panic. Right now every founder calls me two weeks before their first board meeting. I'd rather they find me when the round closes.

STUDIO: Before the panic, when the round closes rather than two weeks before the board meeting. Be specific. What does it look like when it has happened?

LENA: A founder I've never met messages me on LinkedIn, says they just closed their seed round and read something of mine, and asks if I have room. That happens two or three times in a year, and I haven't asked a former client for an intro in that whole year.

STUDIO: So the goal reads: two or three founders a year you have never met message you after reading something of yours, around the time their seed round closes, and you go a full year without asking a former client for an intro. Is that right, or did I change something?

LENA: That's right. Drop "on LinkedIn", it doesn't have to be there.

[Wrote the goal line into `canon/vehicle/vehicle.md` without "on LinkedIn", her three answers word for word in `quote`, log line "goal line revised by Lena and read back, she said it's right". Status stays `draft`: the entry's other fields (known_for, do, learn) are not filled and the goal is only confirmed at the two-directions test.]

STUDIO: Dropped. The goal is written in your words. Next: what would you need to be known for, so that happens?

LENA: The person who gets a seed-stage founder ready for their first board meeting. Honestly, more than that: the one who explains the numbers in plain words so the founder can explain them. Half my job is translation.

STUDIO: Two things there: getting a founder board-ready, and making the numbers plain enough that the founder can say them. Which do you want a founder to say first when your name comes up?

LENA: Board-ready is what they search for. Plain numbers is why they stay. Lead with board-ready.

STUDIO: Board-ready first, plain numbers underneath it as the reason they stay. I have written that down as a draft, which means it is in your file but it will not feed content until you have confirmed it as part of the whole goal, with what you need to do and learn to be known for that. That is the next question, but we are at about twelve minutes. Do you want to keep going or stop here?

LENA: Stop here. I have a call.

[Ending a session. Updated `canon/vehicle/vehicle.md` (known_for and its quote), `canon/progress.md` (About them, status by layer, session plan for a vehicle start with the extraction moved to session 2, next session, log), `canon/canon-index.md` (G1 row). `canon/setup-progress.md` still says "brand tree, not started"; this skill never touches it and `/start` re-derives the stage next time.]

STUDIO: Here is what got done. Your goal is now in your words: two or three founders a year you have never met, messaging you after reading something of yours around the time their round closes, and a year without asking a former client for an intro. Underneath it, a draft of what you need to be known for: board-ready first, plain numbers as the reason they stay. Your files are saved in `canon/`. Next session I read your 60 posts back to you as drafts, then we finish the goal with what you need to do and learn, and move to what you sell. Bring the board-prep checklist and the transcripts of the four calls if Rui has them. Say "continue my brand tree".

LENA: Ok.

---

## Scripts, run at the end

### `bash scripts/status.sh`

```
STUDIO
  version: 0.12.0
CANON
  person/values.md: confirmed=0 draft=0 retired=0
  person/behaviors.md: confirmed=0 draft=0 retired=0
  person/povs.md: confirmed=0 draft=0 retired=0
  person/philosophy.md: confirmed=0 draft=1 retired=0
  person/thesis.md: confirmed=0 draft=0 retired=0
  person/branches.md: confirmed=0 draft=0 retired=0
  person/stop-list.md: confirmed=0 draft=0 retired=0
  bank/stories.md: confirmed=0 draft=0 retired=0
  bank/proof.md: confirmed=0 draft=0 retired=0
  vehicle/vehicle.md: confirmed=0 draft=1 retired=0
  strategy/brand-strategy.md: confirmed=0 draft=2 retired=0
  strategy/audience.md: confirmed=0 draft=0 retired=0
  strategy/content-plan.md: not yet written (strategy-brand writes it)
  voice/voice-guide.md: confirmed=0 draft=0 retired=0
  minimum canon: 0 of 9 items checked
  next session: Start with: extraction of `inbox/linkedin-posts.csv` (about 60 posts) and the board-prep checklist if she drops it in; show draft candidates layer by layer, each as draft with its source row. Then pick the goal back up at `do`: "What would you need to do to be known for getting a seed-stage founder board-ready?" Bring: the board-prep checklist; transcripts of the four onboarding calls (or the recordings, if the studio can transcribe them).
INPUT
  idea bank entries captured in the last 7 days: 0
  ready entries: 0
  inbox files waiting: 1
PIECES
  none yet
PROPOSALS
  open: 0
TOOLS
  Notion: connected: no
  Figma: connected: no
  Publishing: channels: LinkedIn, a newsletter (wants to start)
```

### `bash scripts/setup-check.sh` (exit 1)

```
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
  FAIL  minimum canon 0/9
  ok    config/intake.yaml
  ok    YOUR-STUDIO.md
  ok    canon/visual/brand-assets.md
  ok    canon/canon-index.md
  FAIL  canon/core-summary.md missing
  ok    canon/bank/ideas.md
  ok    canon/bank/evidence.md
  ok    canon/strategy/outcomes.md
  ok    config/tools.md
  ok    proposals.md
  FAIL  canon/strategy/brand-strategy.md not confirmed
  FAIL  canon/strategy/content-plan.md missing
  FAIL  no channel files
  FAIL  voice guide has 0 rules (need 3)
WRITING RULES IN THE CANON
  ok    no em dashes in canon/

setup-check: 6 FAIL. Fix these before the test piece.
```
