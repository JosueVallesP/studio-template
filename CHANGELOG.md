# Changelog

## 0.92.1

The kit is out of the visual system. It was written while building one person's visual system and still carried that person's mark and art as its samples, which is theirs and should never have shipped. `visual-system/creative-director/kit/` now holds a note only. `/visual-system` runs through intake, directions and the approved values, and stops before the package. `/visual` works as it did before 0.92.0. The kit returns when its samples are neutral.

## 0.92.0

An idea gets developed before it becomes a piece, the person's own visual system ships with the studio, and a studio can belong to the client.

**Ideas**

- **`/develop` (`skills/job-develop`)** works one idea through on paper into an idea sheet: the question under it, the claim, when it holds and when it doesn't, real cases, and what a reader leaves with. The sheet takes the shape the idea has, with no fixed headings. It closes with what is the person's, what the studio proposed, what to check and what to ask, and it names the pieces the idea asks for. It checks what the person has already published before it writes, so an idea that argues against their own posts is caught first. Sheets live in `bank/sheets/`. It drafts nothing.
- **57 idea briefs and a wiki in the LinkedIn library** (`skills/fmt-linkedin-post/library/idea-briefs.md`, `briefs/`, `wiki.md`, `wiki/`). Each brief names the idea under a group of posts that worked and lists what a person needs in order to write their own. Every post file now has a `brief` line. The moves stage holds the inventory against the brief's "What you need" list, and `/develop` uses the same list to say which posts can be written from what's on file.

**Writing rules**

- **A new piece is new writing** (`CLAUDE.md`, `skills/craft-house-rules`, the writer's sheet). A story, a scene or an opening the person has already published is not told again, and a new piece never opens where an old one opened. The fact can be named in a line. A story they haven't told can only come from them.
- **Propose before asking** (S3). When the files hold enough to make the next thing, the studio makes it and lets the person react. A list of open questions stops people.

**The visual system**

- **`/visual-system` (`skills/job-visual-system`)** builds the person's own visual system in stages: an intake, three directions shown on real pieces, one system with exact values, and a package with one script that any AI session can make an on-brand piece from. Every approval is the person's.
- **`visual-system/`** ships the method: creative director (`cd-*`, with its kit, taste rules, tool notes and format specs), art direction (`ad-*`) and design (`dsn-*`). An update replaces it; nothing in it is edited in a person's studio.
- **`visual/`** is the person's visual workspace: their brief, directions, system, package, rules and learnings. An update never touches it.
- **`/visual` uses the package** when one exists, in place of the Figma kit or the neutral SVG.
- **What has not been tested.** The visual method has been run with one person. The kit has not been run on a second, and the package has had no cold test since its last edits. `/develop` has produced three sheets with the author; no piece has yet gone from a sheet to a shipped post.

**A studio can belong to the client.** For people who won't keep their thinking in someone else's account.

- **`scripts/hand-over.sh`** moves a client's studio to their own GitHub account: the template brought up to date, `studio-source.md` pointed at it, read access to it for them, the studio taken off the update job's list, and the transfer requested. Once they accept, the seller has no access. `make-client.sh --hand-over` does it for a new client.
- **Updates by pull for those studios.** `/update` fetches the template and replaces the studio's own files only. It explains what to do when the session can't see the template, and never suggests giving anyone access to the person's studio.
- **The template follows each version:** "Push updates" rebuilds it when the variable `TEMPLATE_URL` is set.
- `docs/automation.md`, "Handing a studio over", says how.

## 0.91.0

`/status` opens with the garden. Step 7, the last of the garden audit.

- **"Your garden" comes first:** the ideas by stage, one line per idea the last tending run brought something new to (what fed it, any objection waiting for an answer), and the top of what's ready to harvest. Pieces, decisions and the person's files follow. With no idea bank it's left out; a list older than a week becomes "/harvest".
- `scripts/status.sh` prints the top three candidates from `pieces/shortlist.md` with the list's date.
- Tests: `tests/studio/seed-record/` covers the harvest lines.

## 0.90.0

The pipeline folds into the job commands. There is now one way to make a piece: the person shapes the idea in the stops of `/post` or `/essay`, the writer drafts in a fresh context, the judge reads it cold, and the person decides. The pipeline's brief approval did the same job as the stops, with the person signing off on a plan instead of shaping the idea. Step 6 of the garden audit.

- **What stays.** Capture (planting), the writer, the judge, the producer (ship, hold, kill, the rewrite pairs) and the librarian (learning from what shipped).
- **The shortlist becomes `/harvest`:** what's ready to harvest. `skills/role-strategist` keeps only its list, now ranked with the seed record too (a `growing` idea outranks a `sprouting` one; a seed whose meaning isn't confirmed isn't listed), and works without a confirmed strategy. The person picks by number, and `/post 2` or `/essay 2` builds it from that seed.
- **What goes.** `/brief` and the brief approval, `/design` and `skills/role-designer` (`/visual` makes the picture, now also for "design this"), and the `strategist`, `editor` and `designer` agents. `skills/role-editor` stays as the gates table the judge uses. The guard hooks drop the retired agents.
- **One revision cap:** one revision, then the person decides.
- `/status`'s next steps lose "a brief to approve" and gain stage moves and objections waiting on the person.
- **For instances:** the update moves the retired files to `studio-local-backup/`, as it does for any file the studio no longer has. Pieces from before this version that say `brief-approved`, `designed` or `path: pipeline` are read as before; a piece still waiting on a brief approval gets one question in `/review`: still want it made?

## 0.89.0

The first wind. An idea used to meet its first real objection inside a draft, when it was already being harvested. Now it meets one the moment the person confirms what it says. Step 5 of the garden audit.

- **One objection when a seed sprouts** (the idea bank template defines it): the strongest case against the idea and how they'd answer it. An objection a real reader or client raised comes first, from their files; otherwise the studio builds the strongest one itself, steelmanned, and says it's the studio's. Their answer goes in `pushback`; "I don't know yet" stays `open` for `/scout` or the tending run. They can skip it.
- **Where it runs:** `/shape` after a card's yes, `/status` after a yes to a proposed `sprouting`. `/post` and `/essay` already test the idea's premises in stage 1, which counts as its first wind; no second objection follows.
- **The tending run** puts a sprouting seed that skipped its first wind ahead of the queue, and brings it the push first.

## 0.88.0

The weekly tending run, in place of the weekly scout. Step 4 of the garden audit.

- **What it does** (`skills/job-scout`, "The tending run"): once a week it picks two or three of the person's ideas at `sprouting`, `growing` or `bearing`, the ones untouched longest first, and brings each one thing that feeds it and one thing that pushes against it. The feed can come from outside, or be a story or result of theirs already on file that carries the idea and isn't linked yet. The push is the best argument against, filed as an open objection; a seed that already has one waiting gets a feed only, so objections don't pile up. It sets a new `tended` date on each seed, never changes a stage, and drafts nothing.
- **Where the person sees it.** `sessions/tending-<date>.md`, and one line per idea in `/status` ("new for your idea about X"), which `scripts/status.sh` now prints from the latest run.
- **The schedule.** `/schedules` offers "Weekly tending" instead of "Weekly scout", once two ideas are confirmed. A scheduled task still named "Weekly scout" runs the tending run, so nobody's existing schedule breaks.
- Tests: `tests/studio/seed-record/` covers the `tended` field and the status lines.

## 0.87.0

Scout feeds seeds. Before this, scout only looked for confirmed views and this quarter's branches, so a young idea got nothing, and what scout found expired and floated loose in the bank. Step 3 of the garden audit.

- **Seeds first.** With no topic, `/scout` takes up to three seeds at `sprouting` or `growing` with the fewest `fed` and `pushback` lines, then the branches and POVs as before. `/scout I<n>` scouts one seed.
- **What it finds goes into the seed's record.** A case, evidence, historical texture or someone else's idea it builds on goes in the seed's `fed`. The best argument against goes in its `pushback` as `open`, so the person meets it and answers it. Scout never changes a stage; a find that would move one waits in `next_stage`.
- **What fed an idea stays with it.** An outside entry a seed names gets `expires: with the seed` (capture) and `/tidy` archives it only with its seed. The live conversation still expires after fourteen days; it's a timing signal, not food.
- The weekly scout's prompt (`skills/setup-schedules`) scouts seeds first too, until step 4 replaces it with the weekly tending run.

## 0.86.0

The seed record. An idea used to be marked `used` once a piece shipped, as if it were finished. Now every idea bank entry the person planted is a seed with a record of how it's growing, and an idea that bore fruit once stays in the garden to bear again. Step 2 of the garden audit.

- **Six new lines on every planted entry** (the idea bank template is the one definition): `stage` (seed, sprouting, growing, bearing, resting, cut), `next_stage` (a proposed move and its reason, waiting for the person's yes), `fed` (the outside finds and stories that feed it), `pushback` (each objection, where it came from and the person's answer, or `open`), `fruit` (the pieces it grew, replacing `used_in`) and `became` (the canon entry it grew into). `status` stays and answers one question: can this feed a piece today? Outside entries are food for seeds, not seeds, and get no stage.
- **The studio proposes, the person confirms.** In a session the move is said in one line as it happens; with nobody there it waits in `next_stage`, and `/status` lists it under "Waiting on you".
- **Who writes what.** Capture starts every planted entry at `seed` and adds an objection or an outside find to the seed it touches. `/shape` carries a doubt about whether an idea holds into `pushback` (before, it was buried in `fails`), and the person's yes to the translated line moves it to `sprouting`. `/post` and `/essay` name the seed in the brief's new `seed:` line, record the doubts stage 1 meets with the person's answers, and add the piece to `fruit` as drafted. The librarian marks it shipped and proposes `bearing`. `/tidy` archives a seed only when the person cut it or it's still a raw seed gone stale, and merges seed records with the entries.
- `scripts/status.sh` counts seeds by stage and lists the stage moves waiting for a yes.
- Tests: `tests/studio/seed-record/`.

## 0.85.0

The swipe file, made useful without making it copyable. Before this, `/teardown` wrote to a file nothing ever read.

- **Two halves, kept apart.** The teardown (the job, the moves, what transfers) stays in `bank/swipe-file.md`, now with `full`, `carries` and `moves` lines. The whole post goes to `bank/swipe/<ID>.md`, for the person to read when they want inspiration.
- **The writer never sees the whole post.** A new read guard (`.claude/hooks/guard-reads.py`, on Read, Grep and Glob) denies every crew agent `bank/swipe/`. The crew works from the moves and one short quote, so there are no sentences to borrow. Five hook tests added.
- **Reading it back.** "Show me my swipe file", "read me W3", "I need inspiration" and "what have I saved that fits this?" show the saved posts whole, in the main session, with the move each could lend (`job-teardown`, "Reading it back").
- **The saved moves get used.** `/post`'s openings stop may offer a move from a saved post as one of its three to five options, when the move fits the idea, built from the person's own material and naming where it came from. `/think` reads the teardowns and raises a pattern in what the person keeps saving. `/scout` counts a saved post that carries a POV as outside material it already has.
- **Someone else's words never count as the person's.** `check-mechanical.py` and `check-proposals.py` skip both halves of the swipe file when they look for the person's words, so a name or a line from a saved post can't pass as theirs.

## 0.84.0

The studio's philosophy, said once where the model reads first. The studio is a garden for one person's ideas: the person plants the seeds and decides what's worth growing, and the studio never plants one of its own. Every command does at least one of five jobs (plant, feed, strengthen, prune, harvest); setup and the checks are the tool shed.

- **`CLAUDE.md` opens with the garden** in place of "turns one person's beliefs, material and voice into posts". It names the five jobs with the commands that do each, the test that follows (a part that does none of them doesn't belong), and the split of the work: the person owns the ideas, the studio can share the sentences, so it works as a thinking partner and writing coach more than a ghostwriter.
- **`docs/spec.md`, "Why the studio exists"**, starts from the garden; removing the writer's guesses is now framed as what the garden holds for the harvest.
- First of seven steps from the garden audit (in the studio Project, `briefs/garden-audit.md`); the next is the seed record on idea bank entries. No skill changed.

## 0.83.0

Fixes from a fourth batch of outside repos, read for how they interview people. Most change what the interviews ask, because the writer may never add a detail the person didn't give, so the interview is the only place those details come from.

- **Stories come back with the scene.** Before the parts of a story, the interviewer puts the person back in the moment once: where they were, who was there, what they could see or hear, what went through their head. Two new optional story fields, `scene` and `thought_then`, hold the answers word for word. The owned-story type takes its one piece of sensory texture from `scene` or asks for it; it never invents one. The journal's story modes ask the same question once when an entry is a summary. From the cognitive interview (Fisher and Geiselman).
- **Facts are asked open; wording is offered only for beliefs.** A question with the answer in it ("did she say it was too expensive?") gets agreed to and filed as fact. `craft-interview` move 3a: recall for facts, recognition for beliefs. A story told for years is asked for a record of the facts that matter, and every story records `told: first-hand / heard`.
- **Values have a limit.** A new value follow-up asks how much bigger the cost would have had to be before they chose the other way, into an optional `limit` field. With no limit on file, a piece never states the value as absolute ("I'd never...").
- **Branches start from the field's normal.** When the steps of a method don't come, the interviewer guesses how most people in their field do it and asks where they differ; a "yes, that's it" is the field's practice, not their branch. The interviewer never invents a baseline it doesn't know.
- **No more "why" questions.** "Why does that matter to you?" and "What have you stopped talking about, and why?" are gone: "why" asks for a justification, and a justification is made up on the spot. In their place: "What else was on the table then? What did you weigh?" and "When did you last catch yourself about to say it?"
- **A story bank that only has wins.** `/think` and the map look for a thirteenth kind of finding: every story ends with the person right. Raised from three stories or more, as a `seen` proposal with one question: "Is there a time this went the other way for you?"
- **A review is of one exact draft.** The judge and the editor write the draft's sha256 into the review; `/status` says "draft-vN.md edited after its review" when it no longer matches, so a pass never covers text nobody judged.
- **Ten reports of one study are one source.** `/scout` traces evidence back to its original before filing and says how many outlets repeated it; the editor's outside-case check counts sources by where they came from.
- **Who spoke on a recorded call.** On a video call, a recorder's microphone channel is the person's. On a call recorded in one room on one device, the labels say nothing about who spoke, so it's marked `speaker unclear`.
- Tests: `tests/studio/review-hash/`.

## 0.82.0

Seven fixes from a third batch of outside repos (setec-voiceprint, Nadiem Mahmoud's essay pipeline, Joe Amditis' journalism skills, JobMentis' career skills, the Substack skills, praneybehl's LLM wiki). Each closes a gap in a promise the studio already makes about the person's words and voice.

- **The house rules give way to the person's own habits as a pattern, not only a phrase.** A person whose essays say "it's not about X, it's about Y" a dozen ways had every one failed, because exceptions matched one exact phrase. Now `voiceprint.py profile` counts every house-rule pattern in their own pieces and writes "Rules you break yourself" to `voice-targets.md`, with counts and quotes; each goes to `proposals.md` for their yes. A `rule H17` line in the voice guide's exceptions turns that rule's fails into flags, so the judge still sees each one, and "Above your own rate" keeps a draft from using it more often than they do. From setec-voiceprint (method only; its code is GPL).
- **A draft can't sound surer than the person.** `voice-diff.py --source` now flags a draft line that dropped a bound the source had ("usually", "in my experience", "I think"), turned "might" into "will", added a booster ("obviously", "always") or turned an "I" sentence into a general claim, with both lines side by side. The scripts used to push only toward fewer hedges; nothing pushed back. From setec-voiceprint.
- **A term the person coined stays theirs.** The same check flags a quoted coined term, a capitalised name, a hyphenated compound or a voice-guide term that the draft swapped for another word while saying the same thing (rule 3 had no script).
- **A view they no longer hold can't come back as theirs.** When they tell the map or `/think` they've moved on from a view, the claim becomes `held before` with the date and their reason, linked `replaced_by` to the one they hold, with a draft stop-list entry offered. The packet lists it for the writer, the mechanical check fails a post that says it again as theirs, `/recall` shows it apart, and the map page lists it under "Views you no longer hold". From praneybehl's LLM wiki.
- **Facts made bigger without changing a number.** The editor's stretch gate names role words upgraded ("helped" to "led", "co-founded" to "founded"), one case made many ("a client" to "my clients") and dropped hedges; `check-mechanical.py` notes a role word or plural in a `said again` row that isn't in what it cites. From JobMentis' application reviewer ("mutations are as serious as inventions").
- **Stories made better than they were.** The same gate and the writer sheet name the drifts inside a true story: dialogue nobody said, sensory detail, thoughts at the time, what others felt, a sharper timeline, a stronger feeling, a change of mind staged for the piece. From the Substack skills' anti-fabrication reference.
- **True, but out of context.** The editor's outside-case check reads around each detail for what the source says next to it ("in the pilot only", "up to 40%") and fails a line whose reading it changes; capture keeps the whole of what a client said, never the flattering half. From Joe Amditis' fact-check workflow ("half true").
- Tests: `tests/studio/voice-diff/`, `tests/studio/voiceprint/own_rules.py`, four new house-rule cases, held-before and inflation cases in `tests/studio/claims/` and `tests/studio/map/`.
- Known gap: `check-human.py` counts em dashes and reveal lines on its own, so a `rule H16` or `rule H18` exception doesn't reach it yet.

## 0.81.0

Fixes from a second read of the fifteen outside repos with the most substance, looking only for what the first readers missed. Three of them close gaps in things 0.79 and 0.80 had just shipped.

- **A save never pushes a half-finished git step.** The save runs a git update inside the stop hook, which has a time limit. If that update was cut off halfway, or two versions of a file clashed and weren't settled, the next save could commit files still holding both sides of the clash and push them. Now the save checks first and stops, and the next session says so in plain words. From Gauthier Thiry's company OS, where a rebase cut off this way once hid twelve days of work.
- **The publish guard goes by what a tool does, not three names.** 0.79's hook knew Blotato, Metricool and AuthoredUp; a Gmail send, a HubSpot blog post, a Make scenario run or a LinkedIn, Buffer or Typefully connector could still go out without a prompt. It now asks before any tool that sends, posts, publishes or books, any write on a platform where the person posts or sends, any automation run, and any change to a public page or campaign, whatever the connector is called. Reading and email drafts pass. From Trinity's notes: a guard is only as tight as its least-guarded way out.
- **A recorder can mishear.** A number or name that comes only from a call or talk transcript is kept as heard, marked `heard: recorder, check with the person`, and can't feed a piece until the person confirms it; the mechanical check fails a draft that cites one. The number and quote checks prove a figure is in the file, never that the recorder heard it right. From the interview-mapper skill in alirezarezvani's library.
- **The journal saves from the first real message,** then updates the same file, so a session that just ends keeps the entry; the entry holds the person's messages word for word, never a summary. From Mycelium AI's brain starter.
- **"Whatever you think" isn't a yes.** In the interviews, a hand-back gets two versions built from the person's own words; a second hand-back leaves the entry `draft` with "delegated" in its log.
- **`/recall` searches the person's own words for a topic** (their voice guide vocabulary, the map's other versions of a claim) before saying they never said it, and names the words it searched when it finds nothing. From Eugeniu Ghelbur's Obsidian second brain, where a false "not there" was the most common failure.
- **Text pasted from ChatGPT is marked.** `inbox-to-text.py` finds the tokens ChatGPT leaves in copied text (`oaicite`, `contentReference[`, `turn0search0`, its citation brackets, `utm_source=chatgpt.com`), marks the file "written for them, not by them" with the token, and lists it so the studio asks which parts are theirs; voice work skips it.
- **LinkedIn comments as material.** The archive's Comments.csv, loose or inside the ZIP, becomes `linkedin-comments.md` with each comment's date and the post it was on, for the map and capture to read for the positions the person takes. Voiceprint and voice-diff leave it out: comments are too short to measure a voice by.
- **A skill cut off in the middle is caught.** `check-descriptions.py` also fails a skill file holding a truncation placeholder ("[Rest of document continues...]") and a SKILL.md naming a reference file that isn't there, so a broken upload doesn't ship. From Business of Software's BoS OS, which shipped one cut off after step 5.
- Tests: `tests/studio/save-stuck/`, `tests/studio/inbox-summary/chatgpt_comments.py`, 15 new publish-guard cases, and a recorder-heard case in `tests/studio/canon-status/`.

## 0.80.0

Ten fixes from reading a second batch of 27 outside repos (Creative Content Crafts' LinkedIn skills, COG, Business of Software's BoS OS, Gauthier Thiry's company OS, Eugeniu Ghelbur's Obsidian second brain, three skills inside alirezarezvani's library, and the rest; the Project's `briefs/borrowed-outside-repos.md` lists them all). Each one closes a gap in something the studio already promised.

- **The "Not X. Y." check catches the swaps.** H17 was marked "script (both forms)", yet "This isn't a tactic. This is a philosophy.", "The real problem isn't money, it's attention." and "Not a tactic, but a habit." passed with nothing raised. `studio_checks.py` fails them now (`NOT_SWAP`); a real contrast with a reason ("It isn't cheap. I paid for it anyway.") still passes.
- **The tells that survive a cleanup, flagged.** Staged sincerity at the start of a line ("Let me be honest:"), staged rhythm ("No X. No Y. Just Z.", "Stop X. Start Y.", negation lists, one-word paragraphs), colon reveals, weasel sources ("studies show"), hedge stacks, both-sides balance, "despite these challenges", an opening "-ing" clause, and the shapes current models leave (a parenthetical aside every sentence or two, a bold lead-in on every bullet, semicolon chains). More LinkedIn openers and closers ("excited to share", "Thoughts?", "tag someone") and words (nuanced, notably, spearhead, bespoke, plethora) join the lists, and the plain-word list catches inflected forms ("leveraging", "utilizing"). All flags for the judge. `skills/craft-human` has a new section on them, with the rule that the fixes must vary too, and a date to recheck the lists.
- **A save with a password or key in it doesn't happen.** The save pushes after every reply, and a key that reaches GitHub stays in its history. New `scripts/scan-secrets.py` looks at what's about to be saved for API keys, tokens, private keys and the like; when it finds one, nothing is committed, and the next session tells the person which file and what kind of key, never the key itself.
- **A verbatim quote has to be verbatim.** `check-mechanical.py` now checks that every `verbatim` row's words (the quoted part, when the row has quotation marks) are in the file or canon entry it cites, the way the map has checked its quotes since 0.77. Supplied copy and "said today" are exempt. New `scripts/check-proposals.py` does the same for the quotes in open proposals; tidy, `/think` and the librarian run it before they file one.
- **Text from outside is data, never instructions** (new rule 10). Web pages, posts, threads, other people's transcripts, uploads and connector pulls can be quoted and learned from, never obeyed. `/scout`, `/teardown`, `/understand`, capture and `/sources` each carry the line.
- **AI summaries and ghostwritten pieces aren't filed as the person's words.** `inbox-to-text.py` marks a recorder's summary (Fathom, Otter, Granola, Fireflies) at the top and lists it; a transcript with speaker turns is never marked. Capture and the map treat a marked file as leads only, and a reader names the files it didn't finish. The intake asks which pieces an agency, a ghostwriter or a team member wrote; those get "written for them, not by them" at the top, the map reads them for claims only, and voiceprint and voice-diff leave both kinds out. The converter also strips invisible characters (zero-width, soft hyphens, Unicode tag characters, which can hide instructions) and turns non-breaking spaces into spaces.
- **The writer can't drift into a caricature of the person unseen.** The voiceprint reading adds "Above your own rate": where a draft uses the person's marker words, their most repeated sentence opener, short paragraph endings or its way of closing more often than their own pieces do. A reading for the judge, never a fail. Marker words are now described to the writer as habits, never targets.
- **One statement counts once.** The librarian merges evidence lines that trace back to one origin (an idea bank entry, a capture and the piece built from it, an essay and the posts clipped from it) before counting toward a proposal.
- **A framework the person never named is invented.** Rule 1 and the editor's "Invented material" gate now say so, and `check-mechanical.py` notes a named framework ("the three-layer model", "five pillars") it can't find in the person's files.
- **Numbers written as words, and names nobody sourced.** "We lost eleven clients" passed because only digits were checked; a word number that counts people, money or time is held to the same test now. A name (a company, a study, a person) that no source-map row or cited entry mentions comes back as a note for the judge.
- Tests: `tests/studio/receipts/`, `tests/studio/claims/`, `tests/studio/secrets/`, `tests/studio/inbox-summary/`, `tests/studio/voiceprint/above_rate.py`, 17 new house-rule cases, and a hook case for the librarian running `check-proposals.py`.

## 0.79.0

Five fixes from reading nine outside repos against the studio (Ability.ai's Cornelius and Trinity, Corey Haines' marketing skills, Eric Siu's marketing skills, Builder.io's Agent-Native, the Company OS starter kit, Charlie Hills' social media skills, a second social media skills set, a GTM plugin and an AI marketing suite). Each one closes a gap that was open in 0.78.0. The rest of what was worth borrowing is in the Project's `briefs/borrowed-outside-repos.md`, not built yet.

- **A retired belief can't feed a piece anymore.** `check-mechanical.py` used to accept any ID that appeared in the canon, whatever its status. Now a cited entry that's `retired` fails the check, and a canon `draft`, or an idea or credibility entry that isn't `ready` or `used`, comes back as a note for the judge (rule 2, in the script instead of only in the instructions). From Cornelius' dependency graph.
- **When the person changes or retires an entry, the work leaning on it is flagged.** New `scripts/cites.py <ID>` lists the open pieces whose brief or drafts cite it, and whether `canon/core-summary.md` names it. The producer runs it on every accepted change or retire, logs a line in each piece it finds, tells the person which pieces lean on it, and rewrites the core summary's sentence when it names the entry.
- **Commands that destroy work ask first.** The main session used to run anything, and the save after every reply pushes to GitHub, so a deleted folder or a rewritten history was backed up before anyone noticed, and the people the studio is for can't dig it back out of git. `guard-bash.py` now returns "ask" for deleting a folder, `git reset --hard`, a force push, `git clean`, throwing away every change and deleting a branch with `-D`. The app shows its own approval prompt. Deleting inside a temp folder and the studio's own scripts pass. From the Company OS starter kit's safety guard.
- **Booking a post asks first, through the app.** A new hook, `guard-publish.py`, makes any booking, post, move or cancel through Blotato, Metricool or AuthoredUp go through the app's approval prompt, so the person's yes is a click, not a line Claude says it heard. Reading the schedule or the numbers passes. `skills/setup-sources` already said to book only on a yes; now a bad run can't skip it.
- **A dashboard that stopped updating says so.** The stop hook used to throw away the syncs' output, so a Notion board or the dashboard app could go stale and still look current. Now a sync that fails leaves one line with its reason (`.claude/.sync-failed-<name>`, not saved to GitHub), the next session start tells the person their dashboard may be out of date and offers to fix it, and the next sync that works clears it. A sync that isn't set up still says nothing. From Agent-Native's rule that a failure must never look like success.
- **Every skill fits the Claude app's upload limit.** `setup-sources`' description was 1,278 characters, over the 1,024 the app accepts, so its zip was turned away. It's shorter now, and new `scripts/check-descriptions.py` runs in `test-all.sh` and stops `make-skill-zips.sh` before it builds a zip the app won't take. From Charlie Hills' skill validator.
- Tests: `tests/studio/canon-status/` (a retired ID fails, a draft and a raw idea are notes, a ready idea passes; `cites.py` finds open pieces, skips shipped ones, names the core summary), and 23 new hook cases in `tests/studio/hooks/` (destructive commands ask, ordinary ones pass; publishing writes ask, reads pass). The hook test runner now knows "ask".

## 0.78.0

What's worth borrowing from Trinity (Ability.ai's agent platform) and Ruby (their public content-publishing agent), fitted into what the studio already has instead of added beside it. Clients still open their studio in the Claude app; nothing here needs a server.

- **The studio checks itself after an update.** The first session after a new version arrives (pushed into a built-for-you studio, or `/update`), the session-start hook runs the install half of `/check` once and passes on only the FAIL and warn lines, after the person's first message and never inside a guided flow. A check that passes says nothing. The version checked is kept in `sessions/.checked-version`, so a Cloud session that starts from a fresh copy still knows. The first session ever, or one before the intake, only records the version.
- **Two new parts in `scripts/setup-check.sh`.** Routing fails when a studio command is missing from CLAUDE.md's routing table. Size warns (never fails) when a bank or log the studio reads often has grown past the point where a session wades through it, and points to `/tidy`.
- **Publishing, the sixth kind of source.** Blotato (one account for LinkedIn, X, Threads, Bluesky, Instagram and the rest) or Metricool's planner can book a passed piece for a set time. The studio shows the platform, the account, the exact text and the time with its zone, and books only on a clear yes to that message, for that piece. No standing rule and no scheduled run publishes. The booked text goes to `final.md`, the booking to the piece's log with the tool's ID, and the tool keeps the queue: "what's booked?" asks the tool, not a copy. Moving or cancelling happens only on the person's ask. AuthoredUp's drafts sit in the same section now. The producer (`/review`, "book it for Tuesday at 9") follows it.
- **Metricool as a results source,** beside AuthoredUp and Substack, for people who post on several channels. It works on every Metricool plan. Ruby found that LinkedIn only gave numbers for posts scheduled through Metricool itself; the first test pull checks whether that still holds and, if it does, says so and that booking LinkedIn posts through Metricool is the way round it.
- **`/scout`: the live conversation means the last fourteen days,** with the date read on the page, never guessed from a snippet. A case, an opponent, evidence or historical texture can be any age. Every find names the POV or branch it serves; one that serves none is dropped, and the report says how many.
- **The map turns.** `map.html` has a View switch: "orbit" shows the same map in 3D on a canvas you drag around, the spine in the middle, each claim's stories and frameworks around it, the interview questions hanging below. No library, so the page still works offline; the filters and the findings panel work the same in both views, and it holds still for anyone who has reduced motion set.
- **Left out on purpose:** Trinity itself (servers and Docker, for people who aren't technical; Claude's scheduled tasks already run the weekly jobs), a separate router file (CLAUDE.md's routing table, the writer's sheet and the packet already do that job, and the new routing check keeps the table whole), Klap clipping (no connector Claude can use, and the studio's workspace can't reach its API; `/shape` already finds the ideas in a long talk), and Ruby's one-pass articles, per-platform tone switches, AI avatar videos and viral-speed scoring.

## 0.77.0

Testing setup cold, the first thing after the setup questions was a one-page summary of the person, written before the studio had read anything. All it could hand back was what they'd just typed. The people the studio is for have years of material, so the first thing it does now is read all of it and show them what it adds up to.

- **The map (`/map`, `skills/job-map`) replaces the read-back and comes first.** It reads everything the person handed over, public and private, finds the claims they make (sentences someone could disagree with, never topics), the stories and frameworks that carry them and how they connect, and hands back the findings they can't see from inside their own work. Each finding quotes their lines and ends in a post idea, a question for the interviews, or a yes or no. Then a 20-minute review of the strongest ten, which is also the first brand tree session. "Update my map" adds new material without losing their answers.
- **Twelve kinds of finding, one list.** `skills/job-think` keeps the one definition and adds six that need a whole body of work at once: the spine, a gap, a dropped idea, how the thinking changed, a story that could carry a claim, and said in private, never published. `/think` reads the map first instead of rereading everything.
- **Roots are questions.** The map stops short of values: for each claim on the spine it writes one question about an event for the interviews, never "your value is X". The build refuses a root that isn't a question.
- **Private material, marked.** Calls, memos and notes are read and shown on the map marked private, and nothing from a private source goes into a piece without the person's yes. Personal matters (health, family, faith, money per client) still stay out.
- **One data file, three views, every quote checked.** The map lives in `bank/map/map.json`. `scripts/map-render.py` checks it, then builds `findings.md` (the page), `map.html` (a tree that opens in any browser, works offline, with the findings beside it and filters for public or private and confirmed or guessed) and `map.canvas` (the same map for Obsidian). Every quote is checked against the files its source names, word for word; one that isn't there stops the build. Looked at InfraNodus, Kumu and Obsidian first; the brief (`docs/briefs/map.md`) says why the studio builds its own.
- **The road, reordered.** The map is the first quick win (`setup-start`, the intake's hand-back, the welcome, the quick start, the guide `build-instance.py` writes). `/about` moves to the end of setup, offered once, and now writes from the map and what the person confirmed. An older studio's "One page about you" quick-win line is rewritten as the map's, and `canon/readback.md` still works where it exists.
- **Background work stays quiet.** Rule 9 now covers work running in the background: readers going through material are never narrated ("three of four are back"), and the result waits until a guided flow like the intake is done. The test run that prompted this had that line cut into the middle of the setup questions.
- **`/status`** offers "review my map" while its findings are open, and "update my map" when five or more new pieces have arrived since.
- Tests: `tests/studio/map/` (a good map builds all three files; a root that states a value, an outright claim with no quote, a finding with one quote, a private finding quoting a public piece, a link to nowhere, a quote that isn't in the files and the rest are refused), run by `scripts/test-all.sh`.

## 0.76.0

Setting the studio up cold felt overwhelming. The hand-back after the setup questions named two files and a folder the person can't open, listed five quick wins at once, and ended on "Say `/start`" with no reason. The guide put a table of folders first and the next step last, and talked about briefs, gates and proposals to someone who hadn't made anything yet.

- **The hand-back says what the studio has, then one step.** `setup-intake` step 7: the material named the way the person named it ("your 40 Kollege call transcripts"), the first quick win with what it gives and how long, and "Want to do it now?". A yes runs it. No file names, no list of what comes after, no bare "Say `/start`". The step carries a worked example.
- **A yes counts as the phrase.** `/start` runs the step it just offered when the person says yes, and says once which phrase does it next time.
- **The guide, rebuilt around the next step.** `YOUR-STUDIO.md` now opens with "Your next step" (one step, what you get, how long, what to say), then "The road": every setup step with one plain line on what it gives, how long it takes and its phrase, marked "(done <date>)" as it passes. Then how to hand things over, the three commands worth knowing on day one, the person's own answers, their links, and the weekly rhythm under "Once you're set up", marked as not needed yet. The folder table is gone: nobody needs to open `canon/` or `bank/`.
- **"Show my guide"** puts the guide in the chat, since on Cloud there's no folder to open it from. The hand-back, `/start` and the guide itself point to it instead of to the file.
- **Old guides carry over.** A rebuild reads the old "Where you are in setup" section as the next step and marks the quick wins done when the old guide had closed them; the dashboard sync reads either heading.
Every direct piece now names who it's for and what it has to get done before the argument is built, so the writer stops writing for a generic reader.

- **The reader and the job, at stage 1.** `/post` (and `/essay`, which follows it) opens stage 1 by settling one real reader (a person, named or described by what they do and believe now, never a segment like "founders") and the job (what that reader thinks, feels or does after, what the piece is for, test or cornerstone). The studio guesses both from what was handed over, the strategy and the banks, shows them at the top of the stage 1 message marked "my guess", and the person confirms them with the same yes as the argument. It asks one question only when nothing points anywhere. The format is still decided later, by the idea and this reader's questions.
- **The brief carries them.** `templates/piece/brief.md` has a `One real reader:` line under "The reader", and Outcome now names what that reader should think, feel or do. Both already reach the writer through the packet.
- **The writer writes to that person.** The writer's sheet says to pick the examples, the objection and the level of detail for the one reader, toward the outcome.
- **The judge reads it as that person.** New post check 5b and essay check 9b, and a "Format: wrong reader" gate in `skills/role-editor`: written for a different reader is a redo, stopping short of the outcome is a revise. Older briefs with no named reader skip it.

## 0.75.0

Every direct piece now names who it's for and what it has to get done before the argument is built, so the writer stops writing for a generic reader.

- **The reader and the job, at stage 1.** `/post` (and `/essay`, which follows it) opens stage 1 by settling one real reader (a person, named or described by what they do and believe now, never a segment like "founders") and the job (what that reader thinks, feels or does after, what the piece is for, test or cornerstone). The studio guesses both from what was handed over, the strategy and the banks, shows them at the top of the stage 1 message marked "my guess", and the person confirms them with the same yes as the argument. It asks one question only when nothing points anywhere. The format is still decided later, by the idea and this reader's questions.
- **The brief carries them.** `templates/piece/brief.md` has a `One real reader:` line under "The reader", and Outcome now names what that reader should think, feel or do. Both already reach the writer through the packet.
- **The writer writes to that person.** The writer's sheet says to pick the examples, the objection and the level of detail for the one reader, toward the outcome.
- **The judge reads it as that person.** New post check 5b and essay check 9b, and a "Format: wrong reader" gate in `skills/role-editor`: written for a different reader is a redo, stopping short of the outcome is a revise. Older briefs with no named reader skip it.

## 0.74.0

The studio told people to "drop the files in `inbox/`" without saying what the inbox is or where to find it. On Cloud, where every built-for-you client works, there's no such folder on their computer at all.

- **One page for handing things over.** `docs/handing-things-over.md` says how a file gets from the person to the studio (paste text; attach a file to the message and the studio files it; GitHub's upload page, from a link the studio builds, for a file the chat won't take; the inbox folder on a Local install), how audio, paper and links are handled, and the plain words for each place the studio might name. Every skill that asks for a file follows it.
- **House rule S14.** A folder or file named to the person comes with what it is and how they reach it, the first time in a conversation. Better, they hand it over in the chat and the studio files it.
- **The session start says where the studio runs.** A `WORKSPACE: cloud` or `WORKSPACE: local` line, so the instructions fit.
- **The lines people actually read, rewritten:** the intake's material and brand questions, `setup-intake`, the quick-win and interview lines in `/start` and the brand tree, the welcome (with a new "Handing things over" paragraph), the quick start, the getting-started guide (a new "Handing over files" section), the operating guide, the form's intro text and the "Where things are" row of each person's guide.
- **Attached files have a home.** A new routing row: a file attached to a message is copied into `inbox/` under its own name, and an upload on GitHub is pulled into the session.

## 0.73.0

The POV interview, after a real session asked a question that picked the person's topic for them and lost its place.

- **The interviews ask the layer's questions, not new ones.** A new rule in `setup-brand-tree` ("Ask the layer's questions, not new ones"): the first question comes from the layer file's table or from a story or draft on file, and never names a topic the person didn't. The session had asked about "the last time you watched someone use AI to make content", which narrowed the person's beliefs to the studio's own subject.
- **No "what did you see that they didn't?"** The POV file's fifth question asked for a cause "nobody else" saw, which is the banned abstraction with a story in front of it. It now asks what didn't work and what they think happened; who else missed it is left to the follow-up on what the POV rejects. `routing.md` says the same.
- **A fresh start is handled on purpose.** When the person says their older material no longer speaks for them, the drafts stay out of the questions unless they point at one, the question stays about their work as a whole, and if their focus changed the first question asks what it is now. "Next session" in `progress.md` is rewritten so no older plan contradicts the choice.
- **The waiting question is saved word for word.** Every question asked goes into `progress.md` as `Waiting on:`, replaced on each new question and cleared on an answer, so a session that ends without `/end` resumes on the same question. The template has the line.
- **A shorter opening.** The session doesn't repeat the minimum-list count when `/start` or `/status` just gave it, keeps to four sentences, and glosses or drops studio words.

## 0.72.0

The rest of the outside audit of 0.66.0, checked again against 0.71 before each change (0.67 had already fixed part of it). About a hundred findings: things that broke silently, private material that shipped to every client, and rules written in several files that had drifted apart. Each decision below is applied everywhere at once.

**Fixed because they broke or leaked**

- **The Notion and dashboard syncs run again.** The config reader dropped every key with a space in it (`page id`, `app id`), so both syncs stopped without a word. Keys with spaces are read; a sync that stops early says why when run by hand. New test `tests/studio/sync-config/`.
- **A failed save shows up.** `save.sh` leaves out any file over 50 MB and names it, audio and video in `inbox/` are no longer committed, and a push that fails (or work that went to a session branch after a clash) writes a marker the next session start shows. The stop hook saves first and syncs after.
- **Keys work on Cloud.** The scripts read environment variables before `.env`; the install guide says to set the Pangram, Notion and dashboard keys as the Cloud environment's variables; `/check` warns when one is missing.
- **`build-instance.py` runs on Python 3.8 to 3.11** (a backslash inside an f-string); `/check` fails on a Python older than 3.8.
- **The command guard.** A lone `&` is denied, output flags (`--out`, `--log`, `--targets`) must point under `pieces/` or `bank/voiceprint/`, the librarian may run `rewrites.py` and may no longer call the paid detector. 28 hook tests.
- **The detector refuses a second call.** `check-human.py --detector` returns the reading already recorded in the piece's review instead of paying again; the producer's call on a changed final passes `--force`. `check-human.py` exits 1 only on banned devices; pattern flags are evidence for the judge.
- **Private people out of the selling skills.** `/pricing-tests` and `/diagnosis-call` named members of a paid coaching community with their incomes and private details, cited by call number. Each case now describes the person by what they do, and the cases never go in a piece.
- **The author's voice out of every client's defaults.** The default voice guide's rules are W1 to W10 with `status: default` (D is audience desires), carry the habits with neutral examples and none of the author's phrases, and don't count toward the minimum canon. The default rewrite pairs lost the author's name, his idioms, a Project pointer and a placeholder line; their tags point at house rules or default W rules; `rewrites.py` hands out only pairs of the piece's own format, and the writer reads a default pair's "What changed" lines only.
- **Other people's posts aren't the person's words.** `/teardown` writes to `bank/swipe-file.md`, not `material/`; the voice scripts skip swipe files, READMEs and transcripts and read only the person's side of a rewrite pair.
- **What ships to clients.** `docs/briefs/`, `docs/history/`, `tests/prose/` (the author's writing samples) and `tests/studio/readback-josue/` stay in the studio repo; the manifest lists docs and test folders one by one. An update now moves a file the studio no longer ships into `studio-local-backup/<date>/` instead of leaving it live forever. Managed client repos carry `studio: managed`, and `/update` there says updates arrive on their own. Command descriptions say "the owned-story type", not the author's name; examples use `Europe/London`; the guide's course link comes from `GUIDE_URL` and is left out when it isn't set.
- **"Credibility position: expert"** failed the house-rule hook on every strategy write. The values are now proven, student and broker.

**One rule each, applied everywhere**

- **A new finding is a draft entry.** A belief, story, method or offer the studio picks up goes into its canon or bank file as `draft` with its quote and source. `proposals.md` holds changes to confirmed entries, contradictions, `seen` connections and `inferred` lines only (kinds in `templates/proposals.md`). A crew agent that can't write the canon hands the draft to the main session. Eleven skills followed the other route; they follow this one.
- **Offers** carry `status: draft | confirmed | retired` like every entry, and the market state moves to `availability:`. A change to a confirmed offer is a proposal, never a direct edit.
- **The crew agents run as agents.** `/capture`, `/brief` and `/librarian` launch their agent, so the write guard applies. The designer runs in the main session (Figma lives there) and keeps rule 6 by instruction; the designer agent builds SVG only.
- **One verdict ladder.** A fail is a redo only when the editor's gates table grades it redo; opening craft and "promise kept" are revise in every format. New gates rows for the format checks; a hedged outside fact marked `source: not found` and named to the person passes.
- **The interviews never gate making content.** The minimum canon is what the pipeline and `strategy-brand` need. `/strategy` gives a draft plan from material. "Strategy in use" means `person_confirmed:` or `status: confirmed`, read the same way by `/start` and `/check`. Skipping the interviews writes `stage: interviews-skipped`, which `/check` passes on the direct path's needs.
- **Essays get the 0.65 order.** The reader's questions come before the structure, the structure's parts are a check rather than a form, titles are written after the body (the stage-2 opening pick stays), length is a guide, and the essay judge gains check 11a, shape fits the idea. Essays use Post A, B and C like posts.
- **The writer's pipeline.** `revised` pieces go to the writer (the editor no longer judges them without a new draft); the writer revises from THE ONE THING plus every graded fail; review templates gain The one thing and Voiceprint sections; the brief gains `visual:` and TYPE NOTES; the judge agent judges sales copy through `craft-sales-copy`.
- **Where first material goes:** paste it or drop it in `inbox/`; skills check both `material/` and `inbox/`.
- **Visuals.** 22 moves and nineteen variants everywhere; SVG without Figma; one place each for where `visual-brief.md` goes, what gives an idea a shape and the picture tests; a new move goes to `studio-notes.md` as a candidate, never into the shipped library; the author's taste and file keys are out.
- **Smaller fixes:** `/recall` reads open journal entries only; tidy keeps the last draft and review and owns expired outside entries; `/shape` cards wait as `shaped`; `/learn`'s yes on a correction applies it like `/correct`; `/coach` reads `/status`'s next-step list; the librarian's drafts and "review ready" pieces show at session start and in `/status`; proposal writers check the five-open cap; `/end` runs the Notion connector sync; the missing `job-pamphlet-power/references/marketing-ascension.md` is written; positioning lines and About sections go through `craft-sales-copy`; the three tenses are then, now and future; stale test expectations (Tomas, Marco, Mara) match the current flow; the voiceprint test runs from the shipped essays and joins `test-all.sh`; the briefs say which skill superseded them.

## 0.71.0

Two banks, built side by side. The idea bank held what the person thinks; what makes a reader trust them on it (a result, a client, a line a client said) was one "type" among seven inside it, or waited for an interview to reach the canon's proof file. Now it has its own working bank, and everything that reads the person's material fills both in the same pass.

- **The credibility bank.** `bank/credibility.md`, K IDs, from `skills/setup-brand-tree/templates/bank-working/credibility.md`. Eight kinds: result, client, said-about, before-after, track-record, recognition, artifact, vouched. Each entry keeps the passage word for word, the fact in one line with the number exactly as given, what it backs (`backs:` a POV, branch or idea entry), the idea entry filed from the same passage (`pair:`), permission (anything about someone else is `anonymize` until the person says otherwise) and when the person last said it's still true (`checked:`).
- **Filled in the same pass as the idea bank.** Capture reads every input twice, once for ideas and once for credibility (`role-capture` step 3a); a passage that's both gets an entry in each, paired. `/shape`'s whole-material sweep does the same. `/post` stage 1 files what the person says on the way: the trust it surfaces to credibility, the ideas to the idea bank. The strategist's and producer's interview answers go to whichever bank they belong in. The idea bank's `proof` type is gone; it lives here now.
- **Read where trust is needed.** `/post` stage 1 backs the point from the credibility bank first; `/post` alone weighs ideas with strong results behind them higher. Both moves stages read it for RESULT, DOCUMENT, LINE and the proof under any move, so a "proof, then payoff" opening only appears when a real number is there. `/recall` searches it.
- **The gaps show.** `/status` counts both banks and lists the confirmed views with nothing in the credibility bank behind them; the librarian names them too and proposes shipped, confirmed entries for `canon/bank/proof.md`. `/tidy` asks "still true?" about any entry not checked in a year, since a number true last year can be wrong in a post today.
- The crew's write guard, the ID check (`K` in `check-mechanical.py`), `setup-check.sh`, the setup that creates the banks, `CLAUDE.md` (rules 1 and 2, the folder table) and the spec all know the new bank. The Notion dashboard sync doesn't show it yet.

## 0.70.0

Built with the person, not handed over. The author's point: the studio shouldn't write a post or an essay in one go and then ask "do you like it?", because that leaves the person one thing to say about a finished piece. `/post` and `/essay` now build the piece in stops, each decision shown on its own and agreed before the next is built on it.

- **Stage 1, what you're saying.** Copylosophy's writer pass runs as a conversation: the claim found in what they gave, the reasons, the premises tested, the contrarian and provocation tests when the idea goes against common advice, the belief gate against their files. Questions are about events, three at most. The person sees the point in one sentence, why it's true, when it holds, what it cuts against and what backs it up, and says yes or what's off. If it won't hold, the studio says which part breaks; if it still can't be said in one sentence, it offers `/think about` and stops.
- **No studio words for the person.** People don't think in premises or theses and won't arrive with one. `/post` names the ways people actually start (something happened, a thought or a rant, something they read, a long piece of theirs, nothing, a type by name, or a point or opening they already have) and meets each one; the labels stay in the files.
- **Backed by their files, and by the world when they want it.** Stage 1 says what in their material supports the point and offers once to look outside. On a yes, `/scout` runs on that one idea (new "Called from a piece" note: up to three finds, filed as outside entries, shown one line each). A find is never their view; in the piece it's `borrowed: verify`.
- **Stage 2, the openings.** Three to five openings, each written out and tied to the post it leads into, in plain words (a story, a list, an argument, a borrowed story). Only shapes the reader's questions allow and the material can fill make the set, so the idea still decides which kinds of post are on the table and the opening decides which of those this one is. The pick sets the shape, hook move and type; its words go in a new OPENING line in the format plan, which the draft stages keep (the three drafts differ in wording around it, never in which opening). For an essay, the options are a title with its opening lines, each tied to a structure.
- **Stage 3, the outline.** The beats in plain words, where each one's facts come from, the length. Yes, or what to move, cut or add. Then the packet and the draft in a fresh context, and the judge in another, as in 0.69.
- **Skipping.** "Just write it", or nobody there to answer, goes straight through and says at the top what it took.
- **The idea bank first.** `/post` alone reads `bank/ideas.md` before `material/`, and when the bank is empty and the material is large it offers to fill it. `/shape` gains a whole-material sweep ("fill my idea bank", "go through all my material"), filing cards file by file so a sweep that stops halfway keeps what it found.

## 0.69.0

A writer who reads less. The author asked whether the size of the repo makes the model drift from its principles. It does: a `/post` run had about 44,000 words of instructions in front of it at the moment of writing (`CLAUDE.md`, the command, the writer, the house rules, craft-human, copylosophy, the format skill, the moves and draft stages, both move libraries, a type file, the default rewrite pairs), plus the material and the example posts. A model with that much in front of it follows the last concrete rule it read, favours whatever has a script behind it, and silently drops one of any two files that say the same thing differently. The stitching fixed in 0.68 came from exactly that. This version cuts what the writer reads to about 14,000 words, of which 4,000 are the person's own writing; the rest of the repo is read by the stages that need it.

- **The writer's sheet.** `skills/craft-house-rules/writer-sheet.md`: the rules and the method on one page (where the words come from, the facts and the five source kinds, the argument check, the sentence rules, three drafts, self-check). The full house rules, `craft-human` and `craft-copylosophy` are now the judge's reading; the sheet says so, and `SKILL.md` wins when they disagree.
- **The writer's packet.** `scripts/packet.py pieces/<id>` writes `packet.md`: the sheet, the brief's sections, only the cards the format plan named (cut from the libraries by their headers: the hook move, the shape, the inside moves, the close), the type's draft step when a TYPE is named (its judge checks left out), and the voice (the rewrite pairs `rewrites.py` picks, the voice guide, five to eight of the person's own pieces, cut at 700 words each). Files the brief cites aren't copied in; the brief's material lines carry the quoted words, which is also how lines stop getting lifted.
- **The writer reads the packet and the draft stage, nothing else.** Both draft stages, `role-writer` ("Inputs") and the `writer` agent now say so; the agent no longer reads `CLAUDE.md` or the libraries, and the writer doesn't open the example posts (the plan's EXAMPLES line holds their hook lines; other people's posts in full at the moment of writing is where borrowed tics come from). The command guard lets the writer run `packet.py` and `rewrites.py`.
- **`/post` and `/essay` run in three contexts.** The plan (the moves stage, the person's yes) in the main session, which then builds the packet; the draft in the `writer` agent, in the foreground; the judge in a third. A writer that needs the person sets the piece `blocked` with one question in `log.md`; the main session asks, writes the answer into the brief as `said today`, rebuilds the packet and hands it back. Revisions run in the writer agent too, so the planning context never writes a sentence of the post.
- **Test** in `tests/studio/packet/`, part of `test-all.sh`.

Still to cut: `role-writer` (2,600 words) and the LinkedIn draft stage (2,300) are procedure the writer does read; a later version can fold the parts that repeat the sheet.

## 0.68.0

Said fresh, not stitched. The author's reading of the first real posts: they read as collages of things he once said, lifted from different places and pinned into the piece. The cause was in the rules, not the model: a citation that asked for "the quoted words", a judge that counted sources, a skeleton built one beat per source, and a "keep their sentences" rule with no edge. The writer's cheapest way to prove a line was the person's was to keep their words.

- **The writer proves meaning, not wording.** `CLAUDE.md` rule 1: a piece cites where a fact came from (an ID, a file and the line it rests on), and the test of a `said again` line is that it means what the source means, never that it keeps the source's words. Two new tie-breakers: an example the person used to teach (a workshop case, a figure given to illustrate, someone else's situation in their material) is a fact about how they teach, never about what they did or refuse; and a beat the sources can't carry is cut or the piece is marked blocked, never stretched from the nearest fragment. A thin source bank makes a shorter piece.
- **Source quotes are said again by default** (rule 3). Their words stay word for word only when the exact words are the point: a term they coined, a number as they said it, a line the piece is about. Those are marked `verbatim` and sit inside the cap (two in a post, four in an essay, unchanged).
- **"Their words before a summary" now has an edge.** `skills/craft-house-rules` ("Point of view before sound" and "How the sentences get written"): keeping the person's sentences is the method when they wrote them about this thing (a memo, a journal entry, a draft on this idea, an answer about it). Lines from a workshop, an old post on another point or a call about something else are read for what they think and written fresh. New rule H34, "Said fresh, not stitched", with its script half and its judge half.
- **The skeleton names the source, not the quote.** The LinkedIn draft stage's beat lines carry the file or ID and what the beat tells the reader; the quoted words stay in the brief. Both draft stages say the facts are written fresh in the person's register and name the one case where their sentences are kept.
- **`scripts/check-stitch.py`.** Finds every run of eight or more words a draft shares with `material/`, `inbox/` or `canon/` (never the piece's own folder). A run inside a `verbatim` row passes as a quote on purpose; any other fails with the fix. The verbatim cap is enforced here too (`--cap`, 2 by default, 4 for an essay). Runs as the fifth step of `self-check.py`, in the draft hook (which reads the cap from the piece's brief), and in both judges as a new check (18a in the post judge, 29a in the essay judge), which also read for the two things the script can't see: a teaching example presented as the person's own act, and a stretched beat. A piece stitched in three or more places is a redo, rewritten with the sources closed. The command guard lets the writer, the editor and the judge run it. Test in `tests/studio/stitch/`, part of `test-all.sh`.

## 0.67.0

Fixes from an outside audit of the repo, checked against the files before changing anything.

- **No version reaches a client untested.** `scripts/test-all.sh` runs every automated suite in one go (the house-rule set, the hook guards, the rewrite pairs, the house-rule cases and the new three-draft checks). The "Push updates" job now runs it first and stops before touching any client repo if anything fails. The voiceprint test stays out because its full-text CSV lives in the Project, not the repo. The tests still don't measure post quality; the 20 post briefs in `tests/README.md` are still to come and need the author's approval.
- **The three drafts each get checked.** The draft stages asked for Posts A, B and C, but the template had one `## Post` section and every check script read only that one, so drafts B and C were either skipped or measured as one block. The template now has `## Post A`, `## Post B` and `## Post C` (a revision of the picked draft keeps a single `## Post`). `check-mechanical`, `check-human`, `check-prose` and `voice-diff` measure each draft on its own and report it under its own heading, with `--draft A` to check one (shared helpers `post_section` and `per_draft` in `studio_checks.py`). The once-per-piece readings never run three times: `check-human --detector` and `voiceprint score` ask for `--draft` with the label of the draft the judge picked. The judge stages, the editor, the producer and the skills that describe the scripts say so. The draft hook now shows flags from any of the three drafts, not only when the first one is clean.
- **One self-check, and the writer may run it.** The writer ran `check-mechanical` and `check-human`; the draft stages told it to run `check-prose` and `voice-diff`, which the command guard didn't let the writer run. `scripts/self-check.py` runs all four (never the detector) and says pass or fix. The writer, the draft stages and the house rules point to it, and the guard lets the writer, the editor and the judge run it and the four scripts it calls.
- **One voice order, defined once.** The job commands read rewrite pairs, then the voice guide, then three to five posts; the draft stages said "write plain" when there was no voice guide; the house rules said five to eight pieces. `skills/craft-house-rules` now has "The voice order": the rewrite pairs, the voice guide when it exists, five to eight of the person's own pieces from `material/` every time, and plain writing only when none of those exists, with the earlier source winning a disagreement. `job-post`, `role-writer`, both format skills and both draft stages point to it. A new client's first post now reads their own writing even with no voice guide.
- **Material isn't canon-only.** `fmt-linkedin-post` and `fmt-substack-essay` said material comes from the canon only; they now name the four places in `CLAUDE.md` rule 1, with `material/` among them, as `job-post` already did.
- **The journal's privacy, said plainly.** Private entries are never read by any skill, but `save.sh` backs up every file, journal included, to the person's GitHub repository, which the studio's builder can also open. Keeping the folder out of git would lose entries written in a cloud session, so the journal now says what private means the first time someone journals, and `CLAUDE.md` and the getting-started guide say it too.
- **Tests documented.** `tests/studio/house-rules/` and `tests/studio/drafts/` have READMEs and are listed in `tests/README.md`; the voiceprint README says where its CSV is; the studio note about `studio-notes.md` being overwritten is closed (it's been person-owned since the version that added the five job commands).

## 0.66.0

- **Recipes: the routines a person repeats, saved as one command.** New skill `job-recipes`, command `/recipes`. A recipe is a saved route through commands the studio already has, with the person's own choices for each step in their words ("only my client calls", "the short format", "skip the visual") and the stops where they decide. It never holds a method, a writing rule or a fact about the person, and it never changes a studio skill: the theory stays in the skills, and a recipe only saves how this person chains them. Each recipe is the person's (`recipes/<name>.md`, from `templates/recipe.md`) and runs as its own command through a three-line shortcut in `.claude/skills/<name>/`, which an update leaves alone because the manifest lists the studio's commands one by one. A name that's already a command is refused; if a later version ships a command with the same name, the shortcut goes to `studio-local-backup/` with the rest, the recipe stays, and `/recipes` and `/status` ask for a new name. Running a recipe runs each command's own skill with every check, hook and required stop intact.
- **`/end` offers a recipe when a routine shows up.** `/end` now writes one `ran:` line per session: the commands it chained, in order, with the person's choices. When the same chain with the same choices shows up in three separate sessions within 60 days, `/end` offers to save it, after `/learn` and before the session entry: at most one offer a session, never one the person declined (`recipe declined:` in the log), never with nobody there to answer. The person can also say "save this as a recipe" any time. Because the `ran:` lines start with this version, the first offer comes after three sessions on 0.66.0.
- **Requests about how a studio skill works go to the author, not into the skill.** When a person keeps correcting the same thing in a command's output and it isn't a voice rule, or keeps asking by hand for something no command does, the studio writes it to `studio-notes.md` (`person keeps asking:` or `missing command:`) and says it's noted for the next version.
- **Recipes stay few.** `/tidy` names recipes nobody has run in 60 days, `/status` asks whether to keep or retire each, and retiring moves a recipe to `recipes/archive/` where "bring back <name>" restores it. `/coach` lists the person's recipes among their habits. `recipes/` joins the manifest's person-owned paths.
- **Carried over from the 24 Oct experiment (not yet on main), unchanged:**
  - **A short piece carries one idea from a long one.** `skills/job-adapt` gains "One idea per piece": going from an essay or a talk to a post, pick one idea you can say with no "and" and give it every step it needs, instead of keeping every conclusion and cutting the steps between them. The rest stays in the source, or becomes its own clip; the post may point to the long version as an offer at the end, never as the place missing context lives. `/post` handed a finished long piece now offers the two or three ideas in it a post can carry whole and writes the one the person picks, with `adapted_from:` in the brief. The LinkedIn judge adds check 11a, one idea carried whole.
  - **The judge reads the argument as one argument.** New "chain check" in `skills/craft-copylosophy`, run by every judge after the premise verdicts: write the piece as numbered steps, name the one idea, and fail a shifted test or term, a group nobody defined, an example that sits next to the claim instead of under it, a claim taken back, or a close that breaks the body. LinkedIn judge check 11b and essay judge check 20a grade it; two fails in the body section make a redo. Both review templates gain an "Argument chain" section.
  - **Outside cases are checked against a source opened in the run, never from memory.** New "Checking an outside case" in `skills/role-editor`: list each detail the piece uses, open the named source or search for a primary one, compare detail by detail, record the link. No web tool or no source: "not checked", with the details to confirm in the person's lines. The judge and editor agents get WebFetch and WebSearch. Both review templates gain an "Outside cases" section.
  - **Finished work waits its turn.** New `CLAUDE.md` rule 9: a review or piece that lands while the person is in a guided flow (intake, an interview, a journal session) never cuts into a waiting question; it shows at the end of the flow in one line, or at the start of the next session. `/post`, `/essay` and the first post run the judge in the foreground. `scripts/status.sh` marks a piece whose review exists but which the person hasn't seen as "review ready, not shown yet", and the session-start state says to show it after the person's first message.
  - New test `tests/studio/argument-chain-chess/`: a real post that passed line by line, with the five broken links, the one-idea fail and the outside-case record the judge must now produce.

## 0.65.1

- **The reader's questions stay off the page.** The questions the moves stage writes decide what a post covers and in what order; the draft stage now says plainly that they never appear in the post (no question-and-answer pairs, no questions as headers, no FAQ), and the post judge fails a draft that sets them out and answers them in turn (check 5, a revise).

## 0.65.0

- **The idea decides the shape of a post, and the library comes after.** The LinkedIn moves stage used to pick a hook move from the material and then take the body structure from the hook move's usual pair, so the shape was set before anyone asked what the idea needed. It now runs in this order: the material (unchanged), the idea in one sentence (cold, one idea, more than a platitude; if it won't go into a sentence, `/think` instead of a draft), what the idea gives the reader and where the reader starts, the questions the reader would ask in order (each one a beat), the shape those questions add up to (a table from the questions to the nine structures), and the length that follows from the beats, with no target word count. Only then the moves: a hook move whose gate is open and that opens this shape, the inside moves beat by beat, the close that answers the last question, and examples pulled by shape first. The hook-to-structure pairs from the library become a check: an uncommon pair is allowed when the plan says why. A post type the person names still sets the shape; when the reader's questions point elsewhere, the studio says so and lets them choose. The format plan gains GIVES, READER NOW, QUESTIONS, SHAPE, LENGTH and PAIRING (`templates/piece/brief.md`).
- **Posts are drafted in stages, not in one pass.** The draft stage now writes a skeleton first (one line per beat with its source, read as a stranger: does the idea come through, does each beat earn its place, is a question left hanging), then the body from the skeleton, then three hooks written against the finished body (each checked for its mechanism and for promising only what the body gives), then the close, then assembly with a length test (cover each paragraph; if nothing is lost, cut it). The three drafts keep the skeleton's beats and differ in what leads and how the sentences move. A brief written before this version, with no QUESTIONS line, gets them from the moves stage before drafting, so pieces already in flight still run.
- **`/post` shows the plan before writing.** After the moves stage, `/post` sends one short message (the idea, the shape and its beats as the reader's questions, the opening it would use) and asks whether it says what the person means in an order that works. Changes go into the brief; "just write it" or nobody there skips the step, and the result says which idea and shape it took.
- **The judge checks the shape.** Check 5 of the post judge now rebuilds the reader's questions from the post as a stranger before reading the plan, and fails a question left hanging, padding (a paragraph that answers nothing the reader would ask or the idea needs), or the wrong shape (only when it can name the better one and say why); a wrong shape or a post carrying a different idea is a redo. Check 6 checks the skeleton's beats instead of a fixed parts list per structure. `craft-refine` counts a shape that doesn't fit the idea as a legibility fail. The writer, the strategist, the first post and the skill overview follow the new order.

## 0.64.0

- **Results as a source, limited to the signals the route watches.** `setup-sources` gains a fifth kind: AuthoredUp's connector for LinkedIn (per-post reactions, comments, reposts, engagement, followers over time; every AuthoredUp plan) and Substack's own read-only connector (Bestseller publications only). It's offered only after the strategy is confirmed, and only to routes that watch a number the tool gives (route-buyers, route-pipeline); route-clients, route-role and route-referrals watch referrals and conversations, which no dashboard shows, so they aren't offered one. The weekly pull (a `/schedules` run, or "pull my numbers") matches each piece shipped in the last fourteen days, reads only the metrics the content plan's signals name, and adds a dated `signal` line to the piece's log, never overwriting, so the librarian sees how it moved. The person's own report of who replied still outranks any count. The producer logs a post's link when the person gives it, and can put a final into AuthoredUp as a draft with its scheduled date when the person asks; the studio never publishes. `config/tools.md` gains `results:`.
- **"Still true?" for old beliefs.** A confirmed values, behaviors, POV, philosophy, thesis or stop-list entry whose last `confirmed` or `still true` log line is over six months old is due a check (`setup-brand-tree/references/fields.md`, "Still true"). At each quarterly review `strategy-brand` asks about at most two, the most cited in shipped pieces first, as a question about events ("since <month>, has anything happened that made this less true, or more true?"). Kept: `still true` with the date. Changed: their raw words, a sharper version beside them, and a `change to <ID>` proposal for their yes. `/status` shows only the count due.

## 0.63.0

- **Schedules that actually exist.** `/scout`, `/tidy` and the journal promised scheduled runs and pointed to `docs/automation.md`, which only covers the owner's client-build job, so nobody could turn them on. New skill `setup-schedules`, command `/schedules`: it offers the runs that fit where the person is (a weekly scout, a weekly librarian, a tidy twice a week, and weekly numbers once a results source exists), each off until they say yes, and creates each as a scheduled task that starts a fresh session of their studio with a standing instruction that needs no answer. Runs find and file; they never draft, never touch the canon, never decide. Each run writes one line to `sessions/log.md`, `/status` shows the last line of each and flags a run that has gone quiet (often one stopping at an approval step with nobody there). The journal reminder is now a calendar or phone reminder the person sets, because a run can't wait for an answer. `config/tools.md` gains a Schedules section (time zone and one line per run), kept on a rebuild. `/start` mentions `/schedules` once when setup is done.
- **An update no longer erases the person's changes to studio files.** `scripts/update-studio.sh` now writes a checksum of every studio file it installs (`.studio-installed`). On the next update, any studio file whose checksum changed (the person, or Claude at their request, edited it) or that someone added inside a studio folder is copied to `studio-local-backup/<date>/` with a note before it's replaced. The update job puts the count in its commit message and in the owner's email, `/status` says it once, and "bring back my change to <file>" restores the change into the new version. The first update of an existing studio only writes the checksums; protection starts with the one after.
- **The post judge checks for repetition.** New check 15c in `fmt-linkedin-post/stages/judge.md`, matching the essay judge's "not a template": a draft fails when it repeats the opening words or build, the closing line or sign-off of one of the person's last six shipped posts, or the hook move and structure of two of the last three. The person's own signature lines don't count. Three drafts (A, B, C) that share an opening build or a close also fail 15b.

## 0.62.0

- **Talks and podcasts are a source.** `setup-sources` gains a fourth kind: transcripts of the person's own talks, podcast guest spots, webinars and videos (their material), and of other people's talks they want to learn from (outside material). YouTube comes in through a TranscriptAPI custom connector (`https://transcriptapi.com/mcp`, OAuth, paid with free starting credits); the studio can't fetch YouTube itself, because YouTube blocks the cloud servers it runs on (a script from the workspace was tested and refused). A podcast comes in through its YouTube upload, the transcript on its episode page (web fetch), or an export in `inbox/`. Pulled talks land at `inbox/<date>-talk-<name>.md`. Because these transcripts rarely carry speaker labels and an interview mixes the host with the person, the studio never guesses a speaker: lines are labeled only where it's plain, the rest are marked `speaker unclear`, and capture files only the person's plain lines as theirs. Another person's talk is marked `not the person's`, stays out of the read-back and the interviews, and reaches a piece only as `borrowed: verify` or through `/teardown`. `/adapt` and `/teardown` take a pulled talk; `/capture` and `/shape` pull from a pasted link. `config/tools.md` gains `talks:` under Sources.

## 0.61.0

- **Sources: the studio pulls in the raw material that lives in other tools.** New skill `setup-sources`, command `/sources` ("connect my sources"). It connects three kinds of source in Claude's Connectors, each optional and offered only when it fits: a call recorder (Granola, or Fireflies, tl;dv, Read AI and the like, all in the directory), Readwise (in the directory), and a Reddit research connector (a custom connector, run by a third party). It holds the one definition of pulling: the person picks each call or book (or sets a standing rule in `config/tools.md`), nothing is pulled twice (the source ID sits in each file's top note), calls come in as transcripts word for word, never the tool's summary, and reading notes come in split into "My notes" (theirs) and "Highlighted passages" (the author's, never theirs). Every pulled file lands in `inbox/`, so rule 1 and the inbox rules (capture's permission defaults included) apply unchanged. Wired in: `/shape` pulls a named call that isn't in the inbox, the read-back offers one pull before reading, `/understand` reads Reddit through the connector and treats the client's side of a call as reader language, `/scout` names what's in reach, `/think` reads only the person's own notes in reading files, and `/start` mentions it once where material isn't in yet. `config/tools.md` gains a Sources section, kept on a rebuild by `scripts/build-instance.py`.

## 0.60.1

- **`scripts/save.sh` saves nothing in the studio's own repo.** It added every changed file and pushed the current branch to `main`, so `/end` run in the master would sweep in unready work (a private journal, half-done changes) and land a branch like `experiments` on the master's `main`. It now uses the same check as `on-stop.sh` (`studio.manifest.yaml` present, `studio-source.md` absent), says why it saved nothing, and stops. Every instance carries `studio-source.md`, so instances save exactly as before. `job-end` says to commit the session files by hand there, on the current branch, and push nothing.

## 0.60.0

- **Every studio shows the person its libraries.** The libraries already reach every client studio (they live in `skills/`, which is studio-owned), but nothing showed them to the person, so most buyers never knew they had them. New quick win `setup-libraries`, command `/libraries`: it counts what's there, reads the person's material, picks the three hook moves and one body move their material can carry today (two moves for Substack), shows each with a real example from the library by ID and names what in their material fits it, then shows two or three visual moves from the Moves page of their own Figma kit when it's connected. It never recites the library and never shows a move as theirs when they lack what it needs. It sits in the quick wins after Figma and Notion and before the first post (`setup-start`, `docs/welcome.md`, `docs/quick-start.md`, `canon/setup-progress.md` from `scripts/build-instance.py`), and is routed in `CLAUDE.md` and listed in the manifest.

## 0.59.3

- The buyer email says its steps are the same as Lesson 6 of the course, and points to one guide only: the Notion course at `GUIDE_URL`, or, when that isn't set, "the course I sent you" and its Lesson 13. It no longer links `docs/getting-started.md` on GitHub as a second guide.

## 0.59.2

- The buyer email and `docs/getting-started.md` follow the order in the Notion course's Lesson 6: open Code (left sidebar) and choose Cloud, then connect GitHub from the prompt the first Cloud session shows, with Settings, Connectors as the fallback, then pick the studio by the name the email gives.

## 0.59.1

- **A built-for-you studio opens in the Claude app, not the browser.** The buyer email (`.github/ops/new-clients.py`) now gives the studio's name, then five steps in the order a non-technical buyer does them: accept the GitHub invite, install the Claude app (with the Mac and the Windows steps), connect GitHub in the app's Settings, Connectors, open the Code tab with the **Cloud** environment and their studio, then `/start`. It says plainly that the Claude app is the only install: no terminal, no Node.js, no code. It ends with how to open the studio next time. `docs/getting-started.md` (every client's README), `docs/install-in-claude.md`, `docs/automation.md` and `scripts/make-client.sh` say the same. Cloud on purpose: Local would need Git, a clone and bash on the buyer's machine, and the update job only reaches a fresh clone.

## 0.59.0

- **The new visual moves are in the Figma master, so every studio gets them.** V18 to V22 and the nineteen variants from 0.58.0 are now drawn on the master's Moves page (rows four to eight), at 1080x1350 like V1 to V17, with the Studio text styles, the Style variables and a note under each, so a person's Brand mode restyles them with everything else. The Start here page counts twenty-two moves. `visual-moves.md` lists their node IDs in the kit section. A person who already duplicated the master doesn't get the new frames by themselves: new moves reach people through their next duplicate (`setup-figma`), or they can copy the rows from the master into their file.

## 0.58.1

- One timeline everywhere a person reads it: a week or two to set up, then a month or two for the content to work in a real way (`docs/welcome.md`, `docs/quick-start.md`, `docs/strategy-method.md`, the strategy template and `strategy-brand`). A business outcome stays a separate, longer horizon.

## 0.58.0

- **Five new visual moves and nineteen new drawings of old ones.** `fmt-post-visual/library/visual-moves.md` gains V18 the cycle, V19 the loop, V20 the wheel, V21 the gears and V22 the foundation, each with the full card, and a new relation, interlock (parts that move or fail together). Nineteen variants join existing cards: the ladder as a pyramid, stages of growth and rising steps; the sequence as a timeline with pins, over and under, and chevrons; the path as footsteps; the branching as a prism, many into one, a funnel, a signpost and a hub; the rings as a target with arrows and nested triangles; the anatomy as a head in sections and puzzle pieces; the side by side as versus; the overlap as four circles. All 24 are drawn as neutral 1500x1800 templates in the author's Visual Moves Figma file (node IDs in the kit section), not yet in the master. They were picked from a third-party infographic kit, 24 structures out of 301 diagrams.

## 0.57.0

Every skill in the studio can now be reached.

- **The ten post types are wired in.** `skills/fmt-linkedin-post/types/` held Josué's post-type methods, but nothing read them. The moves stage now picks a type (step 2b: the person names one, or the stage offers the one the material fits), the draft stage follows its draft step, and the judge runs its "Checks the judge adds". `/post` takes a type, and each type is a command: `/owned-story`, `/borrowed-story`, `/arbitraged-content`, `/newsjacking`, `/op-ed`, `/power-listicle`, `/simple-listicle`, `/proof-post`, `/shorties`, `/super-specific-how`.
- **Three type methods written:** `newsjacking.md`, `op-ed.md` and `arbitraged-content.md` existed only as example files pointing at methods that weren't there. Converted from Josué's own skills to the studio's bar, beside the other seven.
- **The selling tools are commands:** `/offer-designer`, `/pricing-tests`, `/diagnosis-call`, `/pamphlet-power` and `/turning-prospects-into-collaborators` had skills that already referred to each other by those names, but no command files. Added, routed in `CLAUDE.md`, and listed in the manifest so they reach every client studio.
- `docs/operating-guide.md` and `docs/state.md` list every command; sales copy is no longer marked parked.

## 0.56.0

- **The author's own methods reach every client studio.** `/visual-philosophy`, `/genius-of-contradiction`, `/copylosophy`, `/articulation-ladder`, `/three-tenses`, `/finding-your-personal-monopoly` and `/building-your-message` were in the master but missing from `studio.manifest.yaml`, so new builds and updates left them out. They are studio-owned now, and `CLAUDE.md` names and routes all seven.

## 0.55.0

- **A welcome on a person's first visit.** The session-start hook now spots a person who hasn't been welcomed (a person's studio with no `welcomed:` line in `canon/setup-progress.md`) and asks the first reply, whatever they typed, to open with `docs/welcome.md`: what the studio is, the nine setup steps in order with the phrase and the time for each, what they can do any time before the interviews, what waits for them, and `/start`, `/status` and `/end`. If they typed a question, it gets answered after the welcome. The words live in one file; `/start` says the same welcome, and the form path gets it with their name and step 1 marked done. Intake in Claude adds `welcomed:` so it shows once. The studio's own master repo never sees it. The person's README (`docs/getting-started.md`) says the studio opens with a welcome whatever they type first.

## 0.54.6

- The one-page guide (`YOUR-STUDIO.md`, written by `scripts/build-instance.py`) points to the Notion course, and its first post, capture and week match it: paste or use form uploads (no folder dropping on the web), about two hours a week with a journal and `/end`. The Notion master's "How your studio works", Home and top page now say what the dashboard is for and that decisions are recorded with `/review`.

## 0.54.5

- The buyer email (`.github/ops/new-clients.py`) and `docs/getting-started.md` match the Notion course: the session starts from the repository picker and the first message (no start button), "Only select repositories" when connecting GitHub, the "Accept invitation" label and the 7-day invite expiry, one line on the permission prompt, and `/about` first among the quick wins. Figma and Notion are connected when the studio gets there, not as a setup step. The GitHub Desktop path is gone from both, since the course doesn't teach it.
- New repo variable `GUIDE_URL`: the email links the Notion course as the full guide when it's set, and `docs/getting-started.md` until then (`docs/automation.md`).

## 0.54.4

- Saves land on main from any branch: `scripts/save.sh` pushes `HEAD` to the repo's default branch (rebasing onto it first when it moved), so a Claude Code on the web session, which runs on its own branch, never hides work from the next one. The session-start hook fast-forwards to the latest main before anything else.
- The read-back reads `material/` as well as `inbox/` (`skills/setup-readback`), converting Word, PDF and ZIP files uploaded straight to `material/`.
- Two routes in `CLAUDE.md`: "save this to my material" writes pasted text there word for word; "update my dashboard" runs the Notion sync.
- `docs/automation.md`: the buyer email now points to claude.ai/code.

## 0.54.3

- Updates reach clients on their own: the job "Push updates" (`.github/workflows/push-updates.yml`, `.github/ops/push-updates.py`) pushes each new version into every client studio, studio files only. `make-client.sh` tags each new repo `content-studio-instance` so the job finds it; `.github/ops/update-include.txt` and `update-skip.txt` add or hold back a studio. `/update` says so for a studio built this way. `docs/automation.md` has the section and the token fix for "createRepository".

## 0.54.2

- `voiceprint.py patterns`: measure names keep their capitals ("sentences starting with I", "I / me / my").

## 0.54.1

- The buyer path is Claude Code on the web: the buyer email (`.github/ops/new-clients.py`), `docs/getting-started.md` (now with a section for a studio built for you) and `docs/install-in-claude.md` lead with claude.ai/code and keep GitHub Desktop plus the desktop app as the way to have the files locally.

## 0.54.0 · 2026-10-23

Voiceprint: the person's writing habits, measured.

- **New check, `check-voiceprint` (`/voiceprint`), with `scripts/voiceprint.py`:** stylometry on the person's own writing. Builds a profile from `material/` (transcripts skipped, since they carry other voices) against a comparison set of other writers in `bank/voiceprint/others/` and the studio's side of every pair in `bank/rewrites/`, read in place. Measures the most frequent words (Burrows's Delta and Cosine Delta), General Impostors verification, marker words (Craig's Zeta) and 29 style measures. Writes `bank/voiceprint/profile.json` and `voice-targets.md`, the writer's brief in plain words. The research and its limits are in `references/methods.md`.
- **One reading per piece.** The judge stages run `voiceprint.py score` on a piece's first judged draft once a profile exists, and record the VOICEPRINT block in the review: reads like you, close, off, or no verdict yet. A reading like the detector's label, never a fail by itself, never read again on a revised draft. The fit takes the lower of the word measure and the style measure, because model text sits near the person's average word habits while missing their style; the verdict is withheld below 3,000 words of the person's writing or when the method can't tell their pieces from the comparison set at the draft's length.
- **The rewrites, measured.** `voiceprint.py patterns` reads every pair in `bank/rewrites/` and lists the measures that moved the same way in most rewrites and the words the person keeps adding or cutting, as candidates for `new` tags and voice-guide proposals.
- The command guard lets the editor, the judge and the librarian run `voiceprint.py`, never the writer (rule 4), with two hook tests. `tests/studio/voiceprint/` checks the script on six writers' essays it hasn't seen.

## 0.53.1

- `docs/briefs/`: the design notes behind every skill built on 2026-10-23 (shape, journal, refine, manifesto, think, understand, adapt, tidy, teardown, visual extensions, formats, librarian results, coach, the house-rules draft), so the reasoning travels with the code.

## 0.53.0 · 2026-10-23

The docs catch up with the road.

- `docs/quick-start.md`: the new commands in "what works now" (shape, journal, refine, adapt, teardown, understand; the manifesto waits for the thesis), the manifesto as a step after the interviews and before the look, and the week as minutes not hours (capture by voice, ten minutes of journal, one production session).
- `docs/operating-guide.md`: "What you say" rows for every new command, and `/think about`.
- `docs/state.md`: "Not built yet" rewritten to what's actually left.

## 0.52.0 · 2026-10-23

The pending edits to existing skills.

- **`job-visual`:** art direction (a brief an illustrator, photographer or image tool executes, through visual philosophy, legible on its own) and data visuals (numbers as one more idea visual philosophy gives a shape to; the plain chart is the fallback; honest proportions; real, sourced numbers only). From `briefs/visual-extensions.md`.
- **`job-scout`:** a weekly scheduled run (off by default), the live-conversation sources named with an honest line about which were out of reach, and a fifth kind: historical texture.
- **`job-learn`:** keeps `config/working.md`, how this person uses the studio (the commands they reach for, the journal modes, when they work, what they skip), read by `/coach` and `/status` to suggest less and the right things.
- **`role-capture`:** voice first. A voice note or a call recording is the preferred input, since the person's own words are the strongest lever the studio has; transcripts are cleaned only as rule 3 allows.

## 0.51.0 · 2026-10-23

Adapt, Tidy, Teardown.

- **`job-adapt` (`/adapt`):** one piece into another format or channel by clipping, not chopping: Shape's two jobs with a finished piece as the raw material. The idea, facts, stance and ground stay; context, frame, form and length change. Completeness is the usual failure (a clip leaning on the original), fixed by bringing the context in, never by pointing back. Every adapted piece and visual stands alone; nothing new about the person; only clips that meet the bar get adapted; the brief records `adapted_from` so the body of work shows how ideas spread.
- **`job-tidy` (`/tidy`):** the 48-to-72-hour cleanup: expired outside entries and stale raw ideas to an archive, duplicates merged with both sources kept, shipped pieces' drafts archived after 14 days, contradictions flagged to `proposals.md` for the person to settle, old log lines compacted. Never the canon, never the journal, never a delete.
- **`job-teardown` (`/teardown`):** why one specific piece works: the job, the moves named with the studio's libraries, why it lands through Shape's chain, what transfers. Learn the move, never copy the piece. Goes to `material/swipe-file.md`; a move the libraries lack becomes a candidate in `studio-notes.md`. Distinct from the site-teardown skill.
- The briefs these were built from are `briefs/adapt.md`, `briefs/tidy.md` and `briefs/teardown.md` in the Project.

## 0.50.0 · 2026-10-23

Understand: audience research that starts from caring about the reader.

- **New skill, `job-understand` (`/understand`):** mines first-party sources only (the person's own comments, DMs and calls; interviews they run; Reddit, Quora, forums; reviews; never articles) for pains, frustrations, desires and goals in the reader's words, and for the why behind them: what they believe that makes the behavior reasonable, what they've tried, the struggling moment (Indi Young's practical empathy; Moesta's Jobs to Be Done). Four gates: every entry a real quote with its source, the "that's exactly it" test, care not leverage, patterns need repeats with counts. Reads each segment's awareness stage from the quotes and the field's sophistication from a peer landscape of the claims the reader has already heard, which also shows where the person's POVs cut against their field. Drafts into `canon/strategy/audience.md`, which gains `reasoning`, `tried`, `struggling_moment`, `language_bank`, `peer_landscape`, `sophistication` and counts. The brief it was built from is `briefs/understand.md` in the Project.

## 0.49.0 · 2026-10-23

`/think about X`: the studio as thinking partner for one idea.

- **`job-think`** gains a one-idea mode. What a good thinking partner does, each with its mechanism: shows a different perspective (invert it; steelman the other side by Rapoport's rules; change the seat; run the three tenses; change the level), finds ideas the person wouldn't find alone (connections in their files, an analogy where the relation carries over), gives context (`/scout`), pushes back (copylosophy on the premise; the ground and the condition), and is proactive (offers a session when Scout filed a counterpoint, a journal entry stalled, a POV is still forming, a draft argues something the canon doesn't hold; never starts on its own). The gate: the conclusion is theirs; the studio never says "here's what you think". A session ends with a POV candidate (claim, ground, condition) in `proposals.md`, or a note that the idea didn't hold. The journal's think-it-through mode is the same session in writing. The brief it was built from is `briefs/think.md` in the Project.

## 0.48.0 · 2026-10-23

The manifesto.

- **New skill, `job-manifesto` (`/manifesto`):** the person's manifesto from their confirmed canon: thesis, philosophy, POVs and the three tenses (then, now, future) set in relation to the cause. Built from a structural study of 28 manifestos: the ten moves most of them share, how the person's layers map onto those moves (catalyst to the why, philosophy to the founding claim, POV conditions to the concession, behaviors to the vow), four shapes to pick from by what the material is strongest in, fourteen moves worth borrowing, and the finding that the future is the tense most manifestos skip. Form follows how people meet the brand (essay, short cut, charter); "we" only when a real group stands behind it. Three drafts, seven gates (every claim traces, every belief has its ground, the swap test, all three tenses, evidence in the now, one concession, a checkable vow), the judge picks. Runs after the thesis is confirmed and before the visual identity, which now reads it first.
- The brief it was built from is `briefs/manifesto.md` in the Project.

## 0.47.0 · 2026-10-23

Refine: good to great without over-polishing.

- **New standard, `craft-refine`:** what great means (relevant to the person, on strategy, fully legible, genuinely valuable; everything else is a lever), two cautions (don't over-optimize, since on social media overthinking means testing less; great can't be fully known in isolation), the test-versus-cornerstone split (one fix then ship, or another round and a comparison), and the one-constraint rule: seven levers walked deepest first (idea, legibility, concreteness, examples, analogy, frame, craft), fix the deepest one that fails, compare against the best of its kind and the person's own best, cut, judge. A piece that fails relevance or strategy stops; polish doesn't fix it.
- **New command, `/refine` (`job-refine`):** runs the standard on any piece the person brings, including their own drafts. Says one thing, then the verdict.
- The editor and both judge stages report THE ONE THING before the ranked issues; the writer revises from that line and takes the "should" lines only on a cornerstone; the brief carries `kind: test` or `kind: cornerstone`. The brief it was built from is `briefs/refine.md` in the Project.

## 0.46.0 · 2026-10-23

Journal: a place to find out what you think.

- **New skill, `job-journal` (`/journal`):** five modes, each on a proven method: free write (Elbow's freewriting, Cameron's morning pages), today's story (Dicks' Homework for Life), turning points (Progoff's Steppingstones), make sense of it (Gibbs' reflective cycle, or what, so what, now what), think it through (Elbow's loop writing; the written form of `/think about X`). Questions are about events, never abstractions; one follow-up when an entry stalls, then quiet. The studio suggests a mode from what's going on (a transcript landed, no story in a week, Scout found a counterpoint) and the person can always pick. Entries live in `journal/`, person-owned, `private` by default: no skill reads them, the hooks never check them, the studio never comments on the writing. Opening an entry lets `/shape` look for ideas; keeping a clip takes a second yes.
- `journal/` is a person-owned path in the manifest. The brief it was built from is `briefs/journal.md` in the Project.

## 0.45.0 · 2026-10-23

Shape: which ideas become pieces, and what form each one wants.

- **New skill, `job-shape` (`/shape`):** finds the ideas in raw material (a call, a memo, an open journal entry, notes, an old post, or the idea bank's raw and maybe entries) that can stand on their own, the way a short is cut from a long interview. Each candidate runs through the chain a reader goes through: complete, legible, transferable, unexpected (more than a platitude: not common practice, whatever the phrasing), useful. No fixed number comes back; only the steps an idea fails are reported, each with the one question that fixes it. Two questions decide the form (what it gives the reader: do, see, believe, direction; at what level), then one of five translation moves with a principle and a gate each (divide, contrast, reveal, transfer, name). The fidelity gate follows rule 3: raw words kept, the translated idea beside them, "is this what you meant, or closer to it?". Writes idea cards (a `shape:` block on idea bank entries) and hands to `/post`, `/essay` or `/visual`. Never drafts.
- `role-capture` names the split: capture files, Shape judges. The idea bank template carries the `shape:` block. The brief it was built from is `briefs/shape.md` in the Project.

## 0.44.0 · 2026-10-23

The default voice, so no one starts from the model's.

- **The voice guide template is now a default register**, not an empty form: ten rules (D1 to D10) distilled from the studio author's rewrites with everything personal to him removed (a soft first-person frame then a firm claim; claim then its bound; stance words where speech puts them; lists of examples left open; a reaction after an example, not a lesson; talk to the reader when advising, stay "I" when telling; say why after a verdict; name the real thing; questions one per line; a flat close), plus a signature-moves section. Every rule is `status: default` and gets replaced, not stacked, as the person's own habits show. `voice-diff.py` always measures against the person's own words, never the default, so the default stops pulling the moment they have material.
- **Ten default rewrite pairs** ship in `skills/setup-brand-tree/templates/bank-working/rewrites-default/`: the studio's draft beside the author's version, every change tagged with its rule. `scripts/rewrites.py pick` lists them only while a person has fewer than three pairs of their own, labeled `default: read for what was cut, never for the words`. The tenth pair has no rewrite: round 4 of the calibration, written from the author's own paragraph with the three-draft method, read as human by the detector.
- The writer skills say the same in one line. `docs/house-rules-research.md` notes the three Every guides read today and what they add (a voice guide built by reacting to lines; spoken capture as the way to the person's own words). The round-4 post joins the pass tests.

## 0.43.0 · 2026-10-23

Every rewrite points at a rule, so each one either finds a hole in the checks or starts a new rule.

- **Rule tags on rewrite pairs:** every line under "What changed" ends with `· rule:` and one of four tags. An H or W number means the draft broke a house rule or voice-guide rule the studio already has. `new` means the person made a move no rule covers. `piece` means the change was about this piece only. The producer and `/learn` tag as they write the pair; when in doubt, it's `new`. The template and the folder's README explain the tags.
- **Open and closed pairs:** a pair stays open while any line is `new` or untagged. When a `new` move becomes a voice rule (through `/learn` or an accepted proposal), whoever writes the rule changes the tag to its W number, and a pair with nothing `new` left is closed.
- **How the writer picks:** `python3 scripts/rewrites.py pick --format <format>` lists ten pairs: open pairs in the same format first, then open pairs in other formats, then closed ones, newest first in each group. It replaces "the last ten by date", which mixed formats and dropped early lessons the studio still got wrong. `role-writer`, `job-post` and `job-essay` use it.
- **Gaps in the checks:** a rewrite line tagged with a rule that no review of the piece named means the checks let it through. The librarian writes it to `studio-notes.md` as a `checks` line; the same rule missed twice becomes a proposed skill fix for whatever checks that rule (script, flag or judge, per the house rules' column; a W rule is the editor's). `new` lines go to the evidence ledger as voice edits, where two pieces earn a proposed voice rule, as before.
- **Reviews name the rule:** the editor's writing-rule and machine-pattern fails, and the judge's on the direct path, now start with the rule number (H16, W4, H27 to H32), so reviews and rewrites are counted against the same list. A broken voice-guide rule is a writing-rule fail.
- **`/end` says the tally:** `python3 scripts/rewrites.py tally --since <today>` gives one line, such as "3 rewrites, 7 changes: 4 broke a rule the reviews missed, 2 are new, 1 was about the piece only." It goes in the session entry. The first number should fall toward zero as the checks catch up.
- Pairs written before this version have no tags. They count as open, so the writer still reads them, and the librarian sorts their lines the old way.
- **Test set:** `tests/studio/rewrites/` (pick order and tally counts on five fixture pairs). `setup-check.sh` checks the script exists.

## 0.42.2 · 2026-10-23

The two house-rules builds merged (see 0.41.0 below for the whole): `check-prose.py`, `voice-diff.py`, the three-draft draft stages, the swap-test judges, the reply hook that sends a breaking reply back once, and `tests/prose/`. One list source, `scripts/studio_checks.py`.

## 0.42.1 · 2026-10-23

Fixes from a fresh-eyes review of the interviews.

- A thesis is never drafted before the philosophy and the goal; a big idea someone arrives with is kept as a draft and tested as POVs land. The session estimate gives the goal and the thesis a session each.
- A behavior stays a draft until the value it ties to is confirmed.
- The philosophy's gate is the brief's (explains three confirmed POVs, the person says it's the thread); "no POV contradicts it" is part of the done test. The lens table in `fields.md` asks about events, as the session file does.
- The last direct POV question is gone from `/strategy`, which now shows the opinions found in the material and asks about events for more. The stop-list and brand-strategy questions open with an event.
- "limits" says "condition" wherever it means a POV's; follow-ups only when a field is missing.
- An older `progress.md` gets the Philosophy item when the interviews open it, and a thesis confirmed with no philosophy under it gets a `seen` proposal instead of being unconfirmed.
- The session plan in `progress.md` starts empty, one row per session. The core summary includes the philosophy's thread.

## 0.42.0 · 2026-10-23

The interviews: one short session per layer, asking about events.

- **The method, in `setup-brand-tree`:** people can't report abstractions about themselves on demand, but they can report events. Every interview asks what happened, the studio finds the value or belief in it, and hands it back in plain words with the person's lines under it for them to correct or add to.
- **Five session files in `skills/setup-brand-tree/interviews/`:** values, behaviors, POVs, philosophy, thesis. Each says what the layer is and isn't, the evidence it leaves, the event questions that point at that evidence, a pushback table, how the studio finds the entry, the handback and the gate to confirm. The philosophy and the thesis ask for nothing directly: the studio finds the thread under three confirmed POVs, and drafts the thesis from the philosophy and the goal.
- **No fixed order, only dependencies:** values, behaviors and POVs in any order; the philosophy after three confirmed POVs; the thesis after the philosophy and the goal. The studio suggests the next layer from what the person needs now or has the most material for, and says why. `references/routing.md` replaces the eight-session plan with this.
- **The shape of every session:** one layer, 20 to 30 minutes, one to three entries handed back (numbered, titled, their lines under each), stories filed as they come, cross-layer findings to `proposals.md` as `seen`.
- **POVs have three parts:** the claim, the ground (what they saw) and the condition (when it's true). The template's `reasoning` and `limits` become `ground` and `condition`; older files keep working.
- **The philosophy** has a `thread` and an `explains` line; **the thesis** has a `from` line (the philosophy, the POVs, the goal). The minimum canon now includes a confirmed philosophy, since the thesis needs it.
- `references/questions.md` keeps the questions for the other layers; the direct questions are gone and listed under "Questions to never ask". `references/fields.md` and `references/tests.md` carry each layer's definition and gate.
- **New command, `/interview`** (with a layer, or nothing for a suggestion). `setup-start`, the quick start and `CLAUDE.md` present the interviews as short sessions that each pay off the day they're confirmed, not one long stage.

## 0.41.0 · 2026-10-23

The house rules, and why studio prose came out generic.

- **New standard, `skills/craft-house-rules`:** one file for every universal writing rule, for every person and every output, the studio's own replies included (Part 1: 33 rules for everything it writes; Part 2: 13 for how it talks to the person). It opens with the order that matters: point of view before sound (Rick Rubin's test: AI can sound like anything and has no point of view to show), the person's words before a summary, their pieces before the rules. It states the exception principle (a rule gives way only to the person's own quoted words and to supplied copy) and the drafting method the research supports: read five to eight of the person's pieces first; keep their sentences when they've said the thing; write three distinct drafts and let the judge pick; measure what a rewrite removes; put the bans in scripts, not prompts; expect and learn from the person's own edit. The research is in `docs/house-rules-research.md`.
- **New script, `scripts/check-prose.py`:** the mechanical half of the house rules, on any text (piece, canon page, reply). Fails on em dashes, reveal devices, decoration adverbs, "expert", both forms of negative parallelism, placeholders, chat residue and the opener family, "delve" and "tapestry", the "important to note" family, and clusters of machine vocabulary (three or more distinct per 500 words; one or two flag). Flags Latinate words with the plain one beside them, passive-by, trailing -ing clauses, decorative ranges, copula avoidance, rhetorical openers, flat rhythm, landing lines, ladders, a speaker who drops out, synonym cycling (neighbouring sentences that never repeat a word, the strongest measured separator), and, in reply mode, filler openers, process narration, studio labels, too many questions and length. `--voice` drops anything the voice guide marks as the person's own.
- **New script, `scripts/voice-diff.py`:** measures a draft against the person's own corpus (`material/`, their side of `bank/rewrites/`, the voice guide's samples) on the markers a model rewrite moves: contractions, first person, causal connectives, commas, word length, sentence spread; and with `--source`, how many of their sentences survived. Two drifts flag.
- **The lists** (`AI_TELLS`, `AI_VOCAB`, `AI_LIKELY`, `LATINATE`, structural regexes) live in `scripts/studio_checks.py` so nothing drifts. "genuinely" moved from decoration to stance.
- **Hooks:** `check-draft` now runs on every person-facing file (`pieces/`, `canon/` except the person's banks, `YOUR-STUDIO.md`, `proposals.md`), with `check-prose` and `voice-diff`; the person's own words are never checked. New `check-reply` (Stop): the house rules on every reply before it goes out; a script fail sends it back once.
- **Draft stages** (`fmt-linkedin-post`, `fmt-substack-essay`) and `role-writer` read the house rules first, draft from the person's words when they exist, write three full drafts (POSTS A, B, C) and run both scripts before the judge; the post body is written as one person talking and checked against the parts afterwards, not built part by part. **Judges** (`fmt-*/stages/judge.md`, `role-editor`) run the scripts, read for H1, H7, H8 and H24, apply the swap test ("not theirs" is a revise), and pick among the three drafts without merging.
- **`CLAUDE.md`:** the writing rules section is now the short form plus a pointer; a routing row for "is this generic?"; the hooks row updated. `craft-human` points at the house rules and states point of view first.
- **Tests:** `tests/prose/` (fail, pass, reply-fail, drift, corpus) and `scripts/test-prose.sh`; the pass set includes the person's own rewrites from three calibration rounds.

## 0.40.0 · 2026-10-23

How the studio asks.

- **New standard, `skills/craft-interview`:** eight moves for getting past the first, polished answer: find out what they want before advising, get the question under the story, turn hedges into plain numbers and do the arithmetic out loud, ask where a round number came from, follow the reasoning until it holds or breaks, listen for the half-sentence, show both ends of a choice, and notice a "who, not what" question. Plus how to carry it (hold the answer until they've made the pieces, reflect in their words, one hard thing at a time with a check on how they are, end with one small step) and a table of which skill leans on which move. The question budget still holds.
- **`setup-brand-tree`** points to it under "The rules"; a belief that breaks under move 5 goes in as a draft of what replaces it, never confirmed as stated.
- **`job-strategy`** gives the goal the most care: move 1 before any recommendation, one move-4 question for a round goal (the intake's too), the arithmetic against their hours, both ends of a fork.
- **`strategy-brand`** asks once what a round goal is for, or lists it first in the open questions.
- **`job-think`** follows a correction with moves 5 and 6, at most three questions per finding.
- **`job-coach`** has a new path for when the person brings a real question instead of "what now": get the question, what they want, the numbers, both ends or the question underneath, a short view, one small test. It still changes no file.
- `setup-check.sh` checks the new skill exists.

## 0.39.0 · 2026-10-23

Step 6 of the cleanup, the last: defaults marked as defaults, and every condition tied to a check.

- Every number nothing tests (the verbatim cap, two revisions, the last ten rewrites, up to six findings, the librarian's thresholds, four to eight sessions, one to three values, five POVs, "about a year") is marked "a starting default" in the one file that owns it; the other files point at the owner.
- "Reads like a person wrote it" now means passes craft-human and reads like the right-hand side of the rewrites pairs. The bar test has a check in craft-human (a word absent from the person's material and samples where a plainer one exists); the judge stages point at it. "A move the material can carry" means every required material line of the move's gate is in the inventory. "A half-thought" is defined once, in rule 3. "With force" and "with weight" are gone.
- check-human says once which patterns the script measures (1 to 4 and decoration) and which the judge reads (5 and 6), and that the counts are evidence, never fails on their own.

## 0.38.0 · 2026-10-23

Step 5 of the cleanup: one owner per procedure, and the studio's docs describe the studio as built.

- **The spec.** The pre-build design is archived at `docs/history/spec-2026-10-19.md`; `docs/spec.md` is a short current design (principles by rule number, the brand tree, the fractal structure, the canon and bank files with their statuses, the crew and piece states, the permissions table copied from the guard, the gates, the failure rules). No pricing, no open decisions, no version numbers on roles, no scores.
- **The docs** say what's true: one command table in the operating guide, the template path first in the install guide, `material/` for what you've made and `inbox/` for what just happened, Verdict instead of Score in the Notion and dashboard schemas (and the sync scripts), five hooks, Notion and Figma optional. `docs/state.md` is a built / not-built list. README is short and has no version.
- **The owner's material is out of the shipped files:** the private run notes under `tests/studio/readback-josue/` are gone, strategy-method names methods instead of a person and a client, the two working Figma keys are out of the visual library, and the craft skills carry one attribution line.
- **Pasted paragraphs became pointers:** the rule 7 words (in ten setup skills), the sync step (in seven role skills; the stop hook runs it), the writing rules (in eight places; `CLAUDE.md` owns them), copylosophy's own 130-line writing-rules section, job-post's copy of the writer's procedure, the visual chain in role-designer and job-visual (fmt-post-visual owns it), the outside-entry rules (role-capture owns them), the seeing kinds (job-think owns them), the proposals cap (the template owns it). The librarian asks the producer for a missing rewrites pair instead of writing it. The dead setup-start templates and the chat-without-files fallbacks are deleted.
- `/think` writes to `sessions/`; the pieces README names every side file in `pieces/`.

## 0.37.0 · 2026-10-23

Step 4 of the cleanup: setup routing without dead ends.

- **Intake** points at `docs/intake-questions.md` with no counts or numbers in the skill; `email`, `github`, `notion` and `figma` are fields. "Phase" is gone; it's intake, the quick wins, the interviews.
- **The minimum canon** is one list of exact field conditions in the progress template; the thesis is confirmed on claim, for and catalyst, with one confirmed branch; the target association has its own status line under "Known for"; the voice rules need a first draft the person has read. Tests that need someone outside the studio are marked "later, by the person". Session counts agree everywhere.
- **One route for a picked-up belief:** a draft entry in its canon file with quote and sources, never a proposal; `/learn`'s yes confirms only when the required fields are present; a blanket yes confirms only fields that came from the person.
- **One question budget** (three per step; a check-back is one question; a crew agent with nobody present writes questions to the brief). Follow-ups only when a required field is empty or the answer matches a weak example.
- **Names:** strategy routes are route-clients, route-pipeline, route-buyers, route-role, route-referrals (not letters); paces are "clients soon" and "body of work first"; readback codes are post-01 / essay-01; the person sees "Your files", not "Canon", and plain words in the strategy review.
- **Overlaps:** the "first piece" stage is gone (`/check`'s test piece is the run through the crew); the one page about the person builds from the read-back when it exists, with one shared threshold; Notion and Figma are optional; buyers' dashboard is Notion, and the app path runs only when `config/tools.md` says `dashboard: app`.
- `build-instance.py --fill` no longer crashes on a missing list field.

## 0.36.0 · 2026-10-23

Step 3 of the cleanup: one review chain.

- **One verdict ladder**, pass / revise / redo, in both judge stages, the editor, the direct review, the job commands, `/status` and the dashboards. The weighted score is gone (`references/scoring.md` deleted); the gates decide and the editor may add up to three ungraded "should" lines.
- **The fidelity grades live once**, in the editor's gates table (new invention and a false premise are redo; a stretch, a false writer line, an unverified borrowed case, no writer rows, supplied copy changed, stitched quotes are revise). Both judge stages point there and have ladders with no gaps.
- **Rule 4 holds in the draft file:** `## Brief defects` (read with the draft) and `## Argument check` (read only after the editor's own premise verdicts) replace the PLAN NOTE. The card number in the plan wins; the writer logs a mismatch instead of picking its own card.
- **The detector, once:** on the first judged draft by whoever judges, and on the shipped final by the producer when it differs. Stated the same way in every file; the 93% figure appears once, as one run.
- **The direct path:** `review-quick-start.md` is `review-direct.md`, used for any direct piece; the editor sends direct pieces to the judge; `/status` shows a direct piece's verdict word.
- **The copylosophy call** is defined once, by caller (writer pass, judge pass, the short version for a story or a result), in craft-copylosophy; the belief gate on a direct piece runs against a quoted line in the material instead of a `quick_start` exemption.

## 0.35.0 · 2026-10-23

Step 2 of the cleanup: three definitions get one owner each, and every restatement becomes a pointer.

- **Rule 1** defines the five source-map kinds in one place with a decidable test (`writer` is a line that would be true whoever said it; `inferred` states what the person believes, did or saw and isn't in the sources) and two tie-breakers (a claim about the person's clients or results is a fact; a number from an outside case is `borrowed: verify`). `seen` is a proposal origin, not a kind. When material and a canon entry disagree, the canon wins and the clash is flagged.
- **Rule 2** says what feeds content: canon entries when `confirmed`, idea bank entries when `ready` or `used`, material as it is. Statuses are draft, confirmed, retired; `forming` is only a confidence level, and a forming POV feeds a piece only when the brief has `thinks_out_loud: yes`.
- **Rule 3** names "supplied copy" (what the person hands over for this piece: kept as written, exempt from the cap and the writing rules) and "source quotes" (from material or canon: may be said again, count toward the cap). Judge checks 24 and 34 narrow to supplied copy.
- **Rule 8** splits seeing (the files only; output a `seen` proposal) from scouting (outside; output an `outside` entry, usable as `borrowed: verify`).
- **The brief template** owns the scene rule (one concrete thing: a scene of the person's or a borrowed case; their earlier sentences alone don't count), `thinks_out_loud`, the parent line for direct pieces, material lines as `SLOT source: "words"`, and `writer:` for "Why it's true" when the canon holds no why. The strategist's and writer's "when the idea can carry it" clause is gone.
- The judge and the editor append each `inferred` line to proposals and name it to the person in the review before anything ships. The "Seen connection" gate is gone.
- Fifteen restatements of the words rule, the scene rule and the kinds in the role, job, format and craft files are now one-line pointers.

## 0.34.0 · 2026-10-23

Step 1 of the coherence cleanup (the audit is in the Project at `audit/coherence-audit-2026-10-22.md`): the code and the routing that broke runs.

- **The working banks moved out of `canon/`.** `bank/ideas.md`, `bank/questions.md`, `bank/evidence.md` and `bank/rewrites/` are person-owned and beside the canon; `canon/bank/stories.md` and `proof.md` stay, because they are confirmed entries. "Canon" now means the confirmed entries and the folder boundary matches rule 6. The guards, the manifest, the scripts and every skill path follow.
- **The guards match the skills.** The strategist may write the index and the canon index; capture gets `inbox-done.py` for the move and may add `also:` blocks to stories and proof; the bash guard rejects redirects, `$(`, backticks and newlines, and gives each role a short script list (`--detector` only for the editor, the judge and the librarian). A subagent call with no `agent_type` is noted once per session in `studio-notes.md`. `tests/studio/hooks/run.sh` runs 13 recorded payloads.
- **One shared check module** (`scripts/studio_checks.py`): signposts fail only in the withhold form ("Here's why:" with the reason after it passes); "Not X. Y." flags only short fragment pairs; the speaker regex is case-insensitive; IDs are read from the source column only and never from a path; numbers count as sourced only from verbatim, said again or borrowed rows; "13" is no longer skipped; the Kind column is parsed and unknown kinds warned. check-human prints `detector: <label>` as a reading. The draft hook hands back mechanical fails as fails and human flags as evidence.
- **Saving.** The stop hook does nothing in the master studio repo (so unfinished skills never auto-push to the branch instances update from). Skills no longer call `save.sh` themselves; `save.sh` writes the session-log line itself, once per commit. `/update` shows the diff and says how to undo it.
- **The manifest lists the studio's files inside `.claude/` one by one**, so a person's own agents, commands and local settings survive an update. README.md is person-owned (the getting-started page becomes it on init). `studio-source.md` is studio-owned.
- **Proposals have statuses** (`open | accepted | declined | edited`); `/status` counts open ones.
- **Routing:** the writer accepts `ready` idea-bank entries (they are never `confirmed`); `/post` reads `bank/ideas.md`; the editor records `redo` and routes it to the strategist; the producer sets `brief-approved` when an answer completes an approved brief; the writer agent accepts a direct piece with revise; the direct revision runs in the main session; a new stage "Interviews skipped (job commands)" lets `/status` and `/coach` run for anyone past intake.

## 0.33.0 · 2026-10-22

The foundational tier. A person should get the smallest useful version of the studio before any of the rest: one page about them that works in any AI.

- **`setup-about-you` / `/about`:** the first quick win after intake. One page from the intake answers and the person's own material: who they are, what they're working toward, what they keep saying (marked as read from their writing until the interviews confirm it), how they talk (their own lines), what they've done, what never to say, how to work with them; then the same page as a plain paste block with no studio words. Every line traces to a quote or an intake field. Rewritten on `/about` as the canon grows. `canon/about-you.md` is person-owned.
- **`/think` reads in bundles.** Past a few tens of thousands of words a single read gets vague, so `/think` reads the files bundle by bundle, keeps a scratch list of candidates with quotes, and finds the connections in the list.
- `setup-start`, `build-instance.py` and `docs/quick-start.md` carry the new quick win first in the order.

## 0.32.1 · 2026-10-22

- **`guard-bash.py`:** a crew agent may run the studio's scripts and read-only git, nothing else; denied with the reason otherwise. The main session is never limited. The roles keep Bash because the checks and the syncs are scripts.
- **`CLAUDE.md` trimmed:** the build-state paragraph moved to `docs/state.md`; the file is the rules and the routing table.

## 0.32.0 · 2026-10-22

The thought partner. Everything so far guarded against the studio inventing the person. Nothing asked it to see for the person: the belief stated three ways that is one belief, the method implied by the stories they keep telling, the shape they haven't drawn, the outside case that makes a point of view concrete. That's the other half of the job, and it's now a rule and two commands.

- **Rule 8 in `CLAUDE.md`:** the studio is a thought partner, not a transcriber. Seeing is putting things already in the files side by side; inventing is adding what isn't there. Everything seen is offered with its evidence quoted and one question, marked `seen`, and the person says whether it's true.
- **`/think`** (`skills/job-think`): reads the canon, material, banks and shipped pieces together and reports three to six findings of six kinds (one belief in three coats, an unwritten method, a shape, an unstated belief, a contradiction worth having, an unmade piece), each with every quote it rests on. Yeses go to `proposals.md` as kind `seen`; unmade pieces go to the idea bank for the strategist; noes are remembered.
- **`/scout`** (`skills/job-scout`): searches the web for each confirmed POV: a checkable case, the best argument against, evidence, the live conversation. Files `outside` entries with source, quote, what it adds and an expiry; a strong contradiction becomes a proposal. Never the person's view, never the stop list.
- **The roles see as they go:** the interviewer says when answers rhyme ("Say what you see"), the librarian proposes `seen` shapes from the count, the strategist has a fourth candidate source (the unmade piece).
- `seen` is a kind in proposals and in the source map (six kinds now); the editor passes a confirmed `seen` line and treats an unconfirmed one as `inferred`.

## 0.31.0 · 2026-10-22

Keep their words, and help them say it better. Rule 3 in `CLAUDE.md` was written for copy the person chose on purpose, and the interview skills read it as a rule for everything a person says, so a half-formed answer got filed as final and the studio said "I'll keep that as you said it". The interviewer's job is the opposite: record the raw words, then offer the sharper version and let the person pick.

- **Rule 3** now names three kinds of words and their treatments: copy they chose (as written), a spoken answer (raw kept in `quote` or `raw`; a sharper version offered beside it when it's a half-thought, theirs if they take it), and their vocabulary (never swapped, though a piece may gloss a term for the reader). The stock acknowledgment is banned; restating the content is the acknowledgment.
- **`setup-brand-tree`:** "Keep their words" rewritten as "Keep their words, and help them say it better", with the test for a tightened claim (more exact, never more than they said) and how to log it. "Don't praise" points at it.
- **`setup-intake`:** raw stays raw in the record, with one exception for a half-thought goal, said back sharper and stored as the person chooses.
- **`craft-contradiction`:** same rule, one line.
- **`role-writer`:** may gloss a person's term for the reader in plain words from how the canon uses it (a `writer` line); still may not invent the method behind it.
- **`role-strategist`:** the "no scene" kill rule caught up with 0.28: a candidate the writer can carry on reasoning or a real example from the world isn't killed; the brief says so.

## 0.30.1 · 2026-10-22

- **A clone never pushes to the template.** A fresh clone's `origin` is the template repo, and `save.sh` pushes to `origin`. Now `save.sh` renames that remote to `template` and skips the push when `origin` is the studio's URL from `studio-source.md`, and `setup-start` does the rename up front before offering the backup. Found by Claude Code on the first real paste of the one-line setup.

## 0.30.0 · 2026-10-22

The simple way in. The form, the converter, the GitHub Action and the invites existed to build a person's instance before they opened Claude. The studio can do that itself (`setup-intake` runs the questionnaire in the chat), so the whole path is now: copy the template, open it in Claude Code, say `/start`.

- **The public template.** `scripts/make-template.sh <url>` builds an empty instance and pushes it as the template repo's main branch; run it after every version. `docs/getting-started.md` is the template's README, and its first step is one line to paste into the Claude app's Code tab in an empty folder: clone the template, then `/start`.
- **`/update` from a URL.** `update-studio.sh` takes a folder, a git URL, or nothing (it reads the URL from `studio-source.md`). `/update` is now one word.
- **Backup, offered once in `/start`.** The studio inits git if needed, offers a private GitHub repo in the person's own account (through `gh` when it's signed in, otherwise the GitHub Desktop steps), and never nags.
- The Tally, `make-client.sh` and automation docs stay, under an "optional, not needed" heading in `docs/install-in-claude.md`.

## 0.29.0 · 2026-10-22

Hooks. Until now every rule the studio relied on was a sentence in a skill: run the checks, run save.sh, never write the canon. A sentence can be skipped on a bad run. This version adds four hooks that run on their own (`docs/hooks.md`), and the session's closing command.

- **`session-start.sh`**: the studio's state (from `scripts/status.sh`), the inbox count and the last session lines are in Claude's context before the first prompt.
- **`guard-writes.py`**: each crew agent (capture, strategist, writer, editor, judge, designer, librarian) is held to the files its role writes, by path. A crew agent writing anywhere else, the canon first of all, is denied with the reason. The main session is never blocked. Rule 6 is enforced now, not asked for.
- **`check-draft.py`**: a write to `pieces/*/draft-v*.md` runs `check-mechanical.py` and `check-human.py` and hands the fails back. No detector call.
- **`on-stop.sh`**: after every reply that changed files, one line to `sessions/log.md` (time, files changed), the dashboard syncs, and `scripts/save.sh`. The auto-commit the spec asked for.
- **`/end`** (`skills/job-end`): the session said back in three lines (made, decided, waiting), `/learn`, an entry in `sessions/log.md`, save. `sessions/` is person-owned in the manifest.
- `CLAUDE.md` names the hooks and the log; `docs/operating-guide.md` says what runs on its own.

## 0.28.0 · 2026-10-22

The writer thinks. Since the spec, every line of a draft had to trace to a file, and the editor failed anything it couldn't source as "invented material". That rule was meant to stop made-up stories, clients and numbers, and it also stopped the writer from doing the writing: the reasoning, the explanation, the framing, the analogy, the example from the world. A writer who may only restate entries produces the person's old sentences set side by side, which is the post that scored 93% AI in the first real run. This version splits the rule in two.

- **Rule 1 in `CLAUDE.md`** now says what the writer brings. Facts about the person (a story, a number, a client, a result, a quote, a belief they've stated) still come only from the four sources and are still cited. Everything else is the writer's own work, needs no source, and is marked `writer` in the source map so the editor checks it for truth and soundness, not for a file.
- **Five kinds in the source map** (`templates/piece/draft.md`): `verbatim`, `said again`, `writer`, `borrowed: verify`, `inferred`. `inferred` is a belief the writer read into the person's material; the editor copies it to `proposals.md` for a yes and doesn't block the piece. The kind is now the second column; `check-mechanical.py` reads IDs from any column and notes a source map with no `writer` rows.
- **`job-post`, `role-writer`, the LinkedIn draft stage:** rewritten to match. "A line you can't source gets cut" now applies to facts about the person only. A brief with opinions and no scene can still be drafted on reasoning or a real example from the world, with the gap noted for the editor.
- **`role-editor`, both judge stages, the `judge` agent:** the invented-material gate is scoped to facts about the person. Two new gates: "Writer lines" (true, and supported by the material; a draft with none at all is a FIX) and "Inferred belief" (supported, to `proposals.md`; unsupported, FIX; never a REDO).
- **Docs:** `spec.md` failure rules, `operating-guide.md`, `quick-start.md` and `setup-start` say the same thing in the person's words.

## 0.27.0 · 2026-10-22

The job commands. The first outputs from real material came out generic, and the cause was the path, not the moves: a post had to wait for interviews, a canon, a brief, an approval, a strategist and an editor, and every handoff wrote from summaries of the person instead of from their words. This version adds a short path next to the pipeline and makes the canon optional.

- **Five job commands,** one thing each from one command: `/post` (`skills/job-post`), `/essay` (`job-essay`), `/strategy` (`job-strategy`), `/visual` (`job-visual`), `/identity` (`job-identity`). They keep what makes a piece good (real material, a move the material can carry, the person's voice, a judge who didn't write it, the human check) and skip the shortlist, the brief approval, the editor's score and the librarian. A piece they make still lands in `pieces/`, so `/status`, `/review` and `/librarian` see it. `/strategy` and `/identity` hand over to `strategy-brand` and `setup-visual-identity` when the canon is confirmed, and run a short version from the material and a conversation when it isn't; they write the same files, marked `draft` with `person_confirmed`.
- **`material/`,** person-owned: everything they've already made, in their own words. Every job command and format skill reads it directly. The canon adds to it and no longer replaces it. `build-instance.py` and `update-studio.sh` create it with its README.
- **Rules 1 and 2 in `CLAUDE.md`:** facts come from four places (what the person says, `material/`, `inbox/`, the canon), each cited as a canon ID, a file and quoted words, or `said today`. Only canon entries need confirming; the person's own material and words don't.
- **The `judge` agent:** judges a direct piece in a fresh context against its brief, draft and material, with the format's judge stage and the quick-start review template. No score.
- **`setup-first-post`** now runs `job-post` with the setup framing, instead of carrying its own copy of the chain.
- **`studio-notes.md` is person-owned.** An update adds it once and never replaces it, so an instance's own run notes survive (the note from the first `/update` of an instance).
- **Three helpers, borrowed from the Second Brain's command set and rebuilt for the studio:** `/recall` (`job-recall`: what the person has said, written or shipped about a topic, quoted with its source, across `material/`, the canon, the idea bank and `pieces/`), `/learn` (`job-learn`: at the end of a session, the choices made in it, listed, and the yeses saved to the voice guide, the canon or `proposals.md`), `/coach` (`job-coach`: where you are, the one thing to do now, what comes after, the habits, each with its reason; no scores, streaks or day counts). `/status` stays the list; `/coach` is the advice.
- **A `scheduled` date on pieces.** `/review` sets it ("queue it for Tuesday"), `status.sh` prints it, and `/status` shows the next seven days with the gaps when the plan has a cadence. The studio still never publishes.
- **The detector runs once, as a reading, not in a loop.** `check-human.py` calls Pangram only with `--detector`; the judge makes that call once per piece and the producer once on a shipped final. The writer never calls it and never rewrites against it: every real run scored 100% AI on every rewrite, because a model rewriting a model's draft keeps the fingerprint, and each loop cost four or five paid calls. The pattern flags are the gate; the label is recorded for the person. The editor's Detector gate is now a recorded reading.
- **`canon/voice/rewrites/`.** When the person rewrites a draft, the pair (the studio's draft, their version, the detector's reading on each, what changed) is kept as its own file: the producer writes it on ship, `/learn` writes it the moment a rewrite is handed back. The writer reads the last ten pairs before every draft and writes like the right-hand side. The voice guide's rules become the summary; the pairs are the thing the studio learns from.
- `templates/piece/brief.md` has a `path:` field (`pipeline` or `direct`); `setup-check.sh` checks the new skills, agent and commands.

Not changed: the pipeline, the crew, the format chains and their libraries, the strategy method.

## 0.26.0 · 2026-10-22

The form asks only what day one needs. Everything else waits for the step that uses it, where the studio can follow up.

- **`docs/tally-form.md`: 13 questions on 4 pages, about five minutes** (was 24 on 6). Kept: name, email, GitHub username, what they do, the year-from-now goal, LinkedIn and Substack status, hours, the two uploads, logo, colors, fonts. A "What moved to later" table says where each cut question is asked now.
- **`docs/intake-questions.md`: eight questions**, the same set inside Claude.
- **Moved questions have a home.** Business name: the vehicle session. How they'd know: already in the vehicle session. Anything they can't upload: the interviews' intake step. Other channels and links: `strategy-brand` step 5. Team: `strategy-brand` step 6. Looks they like and can't stand, and the never word: `setup-visual-identity`. Topics and names to avoid: the stop list session.
- **Language isn't asked.** `setup-first-post` writes in the language of the material, and asks when the material mixes languages; `role-writer` follows the voice guide's samples.
- **`build-instance.py`** writes "not asked yet: <the step> asks" for a blank, so each later step knows to ask. The converter still reads older forms.

## 0.25.0 · 2026-10-22

The first real post through the crew scored 93% AI on Pangram and read as sentences set side by side. Four fixes, one per cause.

- **The detector is a gate and fails closed.** `scripts/check-human.py` calls Pangram 4 (`text.external-api.pangram.com`, key in `.env`), prints the label, the fractions and each flagged window, and a `detector: pass` only when the label is "Human". No key, no credits or a failed call prints `detector: FAIL` with the reason and exits 2; before, it printed "skipped" and the writer and editor both reported check-human as a pass. The writer can't set `drafted` on a FAIL (three re-says, then `blocked`); the editor has a Detector gate; the producer tells the person what's missing when it didn't run.
- **Quotes are anchors, not the body.** The writer uses at most two of the person's lines verbatim in a post (four in an essay) and says the rest again in their voice; the source map marks each line `verbatim` or `said again`. The editor has a stitched-quotes gate and an unresolved-reference gate ("these people" with no people introduced). check-human's "theirs" exemption covers a line, never a post built from lines.
- **A brief needs a scene.** The strategist sends a candidate whose only material is the person's earlier sentences to the waiting list with "what happened that made you think this?"; the brief template says so; the writer stops and asks when a brief arrives without one.

## 0.24.1 · 2026-10-22

- **LinkedIn posts:** the form and the intake now ask buyers to copy their best 15 to 30 posts into one document. LinkedIn's data archive doesn't reliably include a Shares.csv, so it's mentioned only as an alternative when their archive has one.
- **Substack exports hold the subscriber list.** `inbox-to-text.py` keeps only the posts and deletes the ZIP, so subscribers' emails never reach a studio or its repo. The form's help text says so.

## 0.24.0 · 2026-10-22

The form asks only what the studio can use, and promises only what it can do.

- **`docs/tally-form.md` rewritten** (24 fields, 6 pages), with a table of what reads each answer.
  - **Channels:** "LinkedIn: where are you now?" and "Substack: where are you now?" (now, want to start, not for now), under a line saying the studio writes for both and the strategy decides which leads, with them. "Anywhere else you publish?" and "Your links" are context; the help text says the studio can't read posts from a link.
  - **Material:** uploads first ("Upload what you've already written", "Upload transcripts of you talking"), with how to export LinkedIn posts (Shares.csv from the data archive) and a Substack archive, and that audio and video need a transcript. "Anything you've made that you can't upload?" replaces the old promise that the studio reads whatever they list.
  - **Hours** is a choice of four ranges; **language** defaults to English when blank.
- **`scripts/inbox-to-text.py`.** Turns uploads into text the studio can read: LinkedIn's Shares.csv into one file of posts with dates, a Substack export into one file of published essays with titles, subtitles and dates, Word and HTML into text, ZIPs unpacked. Originals move to `inbox/originals/`; audio, video and unknown formats are listed with what to do. `make-client.sh` runs it after the build; `setup-readback`, `setup-first-post` and `role-capture` run it before reading the inbox.
- **`tally-to-answers.py`** reads the new questions (and still reads old exports); **`build-instance.py`** records other channels and links as context in `outcomes.md` and the guide, and no longer requires a "where you publish" list.
- **`docs/intake-questions.md`** asks the same way inside Claude.

## 0.23.0 · 2026-10-22

Notion, Figma and GitHub are required, not asked about.

- **The Tally form drops "Do you use Figma?", "Do you use Notion?" and the two follow-ups** (23 fields on 6 pages now). The form sits inside the Notion onboarding page, which explains the three accounts first. The GitHub username is required, since it's how the buyer gets access.
- **Every studio is built for Notion and Figma:** `tally-to-answers.py` writes `notion: yes` and `figma: yes`, and `build-instance.py` treats a blank as yes (only an explicit "no" from an older intake turns one off). `setup-intake` doesn't ask either.
- **The buyer's welcome email, `docs/getting-started.md` and `docs/quick-start.md`** say to connect Notion and Figma, and list the three free accounts under "What you need". The thank-you text on the form says the email comes within the hour.

## 0.22.0 · 2026-10-22

The automated delivery: a Tally submission becomes a buyer's studio and a welcome email, with nobody at the keyboard.

- **`.github/workflows/new-clients.yml` and `.github/ops/new-clients.py`.** Every 30 minutes, GitHub Actions asks Tally's API for new completed submissions, runs `make-client.sh` for each (build, private repo, invite), emails the buyer their link and five steps from your Gmail, emails you a note, and remembers the last submission in the repo variable `TALLY_LAST_ID`. A submission that fails is reported and skipped, so it never blocks the next. It lives in `.github/`, outside the manifest, so it never reaches a buyer's studio. Off until `TALLY_FORM_ID` is set. `DRY_RUN=<file>` runs it locally with printed emails.
- **`docs/automation.md`.** The one-time setup: a GitHub token, the Tally API key and form ID, a Gmail app password, the sender name, and a test on yourself.
- **`make-client.sh`** picks a free repo name (`-2`, `-3`) when two buyers share a name, and `--result FILE` writes the outcome for automation. **`tally-to-answers.py`** reads answers from Tally's API as well as its webhooks and CSV.
- Why not Make: the Make account connected here belongs to a client.

## 0.21.0 · 2026-10-22

Fixes from the second buyer dry run (`tests/studio/quickstart-dana/`). The nine problems from the first run held as fixed.

- **A rebuild no longer reopens the quick wins:** `build-instance.py` keeps the "Start here" line once `/start` has closed it.
- **A first post still failing after one revision** is shown with each remaining fail as one plain line, and the person chooses: post it, fix those lines, or one more pass. A second REDO offers the next strongest opening.
- **`templates/piece/review-quick-start.md`**, the review a quick-start judge writes: verdict, fails, human check, no score.
- **The verdict ladder in `stages/judge.md`** reads top down and covers every combination (any fail in E is a REDO).
- **The belief gate** has the quick-start exception in `stages/draft.md` and `craft-copylosophy` too, not only in `setup-first-post`.
- **Stale counts** from older material get their date or today's number.
- **A stated limit** the argument needs never counts as "every loop closed" in `craft-human`.
- **`check-human.py`**: more stance phrases ("I get why", "to be fair", "I suspect"), and a zero count is a note to read for stance, not a flag.
- **The first post's progress line** reads "drafted, waiting on their call" until the producer records shipped, killed or held; `/start` counts its reminders in `first_post_reminders`.
- **`setup-intake` re-runs** read what the person changed, skip the opening, say what the rebuild changed and save.
- **Small fixes:** `setup-figma` checks the connection before promising anything; `check-human` hands over to the right judge.

## 0.20.1 · 2026-10-22

- `scripts/setup-check.sh`: an em dash inside the person's own quoted words no longer fails the check; only the studio's prose around the quotes counts, and `canon/readback.md` is skipped. Found on the first real instance, where a quoted essay draft carried two.
- `studio-notes.md`: `update-studio` replaces an instance's notes, since the file is studio-owned; noted for the next version (the fix is to make it person-owned or merge).

## 0.20.0 · 2026-10-22

Fixes from the first dry run of a buyer going from the Tally form to a first post (`tests/studio/quickstart-dana/`).

- **The first post can't stall.** `setup-first-post` says how a quick-start piece differs: the material is the only source, an opinion in the material counts as the person's position (no belief gate, nothing to `proposals.md`), their verbatim lines don't count toward the human-check patterns, dated words can change, and the brief's canon fields get stated values. The judge is `stages/judge.md` in its own pass against the material, with a verdict and no score; `role-editor` refuses quick-start pieces. All the material in `inbox/` is read as one set.
- **Rebuilding from changed intake keeps everything set up since.** `build-instance.py` merges `config/tools.md` (connections, IDs, links stay), keeps `canon/setup-progress.md` and adds a log line, and keeps the setup section and links in `YOUR-STUDIO.md`.
- **`/start` welcomes once** (`welcomed:` in setup-progress), mentions a first post waiting for the person's call, gives one step for a tool that isn't connected, and writes done, skipped and "waiting on Connectors" lines in one exact format. When the quick wins are done, the "Start here" list in `YOUR-STUDIO.md` becomes one line.
- **The dashboard isn't double-booked:** the dashboard app is "wanted: no" when the person uses Notion.
- **`setup-figma` and `setup-notion`** check the connection with a real call (Figma `whoami`, a Notion search) and handle "not connected" the same way.
- **Readable guide:** channel names lowercase their article and drop trailing notes ("a newsletter on Substack"), and the goal in the log isn't cut mid-word.
- **Checks:** `check-human` runs inside the judge (check 29), not again around it; `check-human.py` counts stance words as whole words and knows negated ones ("I don't think"); the Pangram key moved to `.env` (config/ is pushed to GitHub); `__pycache__/` is ignored.
- **Writing standards agree:** `craft-copylosophy` defers to `craft-human` on signposts, real stance words and verbatim lines.
- **Library:** pairing rows for the line someone said, do this right now and the announcement; the CSV's column names are listed; examples are for the move, never the wording.

## 0.19.0 · 2026-10-22

The Substack essay, the second format.

- **`skills/fmt-substack-essay`.** Moves, draft and judge stages, built the way `fmt-linkedin-post` is and run by the same crew. Two differences came out of the library. The hook is three things the reader meets in order (title, subtitle, opening), each with its own job. And on Substack the title doesn't predict the structure, so the moves stage picks the structure from the material first (a real progression asks for a ladder, a method for a protocol or a worked case, a lived story for a story essay) and then the title, subtitle and opening that sell what it delivers. The judge adds checks a post never needed: the title and subtitle work alone in an inbox, the opening reaches the reader's problem fast and ends on a promise, one idea runs through every section, bridges carry a long essay, and a paywall never sits at the turn.
- **The library, a pilot from 57 essays** (the top 10 of five newsletters and the 7 essays in one writer's "Ambition" tag). `library/hook-moves.md`: 16 title moves, 9 subtitle jobs, 15 opening moves. `library/body-moves.md`: 13 structures, 19 inside moves long-form adds on top of M1 to M9, 9 new closes, and the furniture (paywalls, plugs, sign-offs). `library/essays-sorted.csv` and `library/essays/<ID>.md`: every essay tagged on every layer, with engagement relative to its own writer's set and the full text (paid essays hold the free preview only). Every quoted title, opening and figure on the cards was checked against the essays by a separate pass. Five cards rest on one example each and are marked thin.
- **Wiring.** The brief template has the essay's format plan. `role-writer` knows the essay's draft order and that section headers inside the essay are `###`, because the checks measure the `## Post` section and stop at the next `##`. The editor's scoring treats title, subtitle and opening together as an essay's hook. `CLAUDE.md`, `README.md`, `docs/operating-guide.md`, `docs/spec.md`, `scripts/setup-check.sh` and `scripts/sync-dashboard.py` know the new skill.
- Not yet: essay test briefs in `tests/`, the Substack series, and `strategy-substack`.

## 0.18.0 · 2026-10-22

The read-back met a real body of work, and the brand tree learned to take a yes for everything.

- **`setup-readback`, rules from the first real run** (26 posts, 15 essays, a workshop, an 80,000-word journal). A journal mixes the person's entries with book quotes and pasted AI answers; only the first is their voice, and an AI-polished version of their own idea is never quoted as their words. Private material (prayers, family, money per client) stays off the page unless it's already public, and the page says in one line what was read and left out. Pieces without titles get codes listed at the top. Export backslashes are stripped and said so. A post and its essay version count once. "Things you never do" come from counts, not a reading. Borrowed frameworks carry their credit. Drafts: values only from costly choices, a proposed falsifier is marked as the read-back's, a belief with weight but one piece goes to the files at weak confidence and not on the page, second-hand client words are labelled "his report", inbox files stay for `/capture`. The template splits frameworks into published, notes only and borrowed.
- **`setup-brand-tree`: when they say yes to everything.** A blanket yes confirms every draft, with the sentence they said in each entry's log; read-back readings stay marked as accepted, not rewritten as theirs; a rule they give for their own contradictions goes under the contradictions in `progress.md` and pieces reason them out inside the piece; the facts no draft holds (price, link, target association) are still asked one at a time and never confirmed by the blanket yes.
- Ninth studio test, `tests/studio/readback-josue/`: the runner's notes only; the material stays in the person's instance.

## 0.17.0 · 2026-10-22

From a Tally submission to a buyer's own studio in one command.

- **`docs/tally-form.md`.** The intake form as Tally fields: 27 titles to paste, their types, which are required, help text, the conditional fields, uploads, and settings. Adds the buyer's email and GitHub username. Tally's free plan covers it.
- **`scripts/tally-to-answers.py`.** Reads Tally's CSV export (picks a submission by row or email) or a webhook body, matches questions by the start of their titles, writes the answers file the build reads, and downloads uploads for the buyer's inbox.
- **`scripts/make-client.sh`.** One command: convert, build the instance, put it in git, create a private GitHub repo with the GitHub CLI, record its URL, invite the buyer, push. `--no-github` builds and commits locally.
- **`docs/getting-started.md`.** The buyer's page: accept the invite, clone with GitHub Desktop, open the folder in the Claude app's Code tab, connect Figma and Notion, say /start.

## 0.16.0 · 2026-10-22

Placements: every place a person's look shows up, not just posts.

- **LinkedIn placements and Substack placements** in the Figma visual kit, rebuilt from Josué's "LinkedIn - Substack Templates" file on the kit's variables and text styles. LinkedIn: profile photo, profile banner, infographic portrait and square, newsletter or article cover, newsletter logo, link preview, company page logo and cover. Substack: publication logo, wordmark, welcome page cover, post featured image, email header banner, in-post image. Each at the platform's size, with its crop notes and a Guides layer to hide before export. They take the person's brand with the rest of the kit.
- **The Carousel page** is now that file's six-slide set (cover, point, point, diagram, statement, end) in 4:5 and square, with page numbers, a progress bar and safe-area guides. It replaces the seven frame types from 0.14.
- **`setup-figma`** checks for the new pages, puts the person's name in every "Your name" (`footer-name.js` now covers every page and upper case), and shows the profile banner or the Substack featured image as one of the three proofs. **`setup-visual-identity`** fills the channel assets once the interviews have confirmed the words (banner line, newsletter or publication name, mark).
- **`visual-moves.md`** formats list the LinkedIn and Substack image sizes, and the carousel rules match the six-slide set.

## 0.15.0 · 2026-10-22

The idea leads every picture, and the person always knows what they're doing and why.

- **A visual kit, not templates.** The Figma master now has a Kit page (the twelve marks plus the accent marker as components bound to the Style variables, each with its meaning in its description, and starter frames at 4:5, square and 1500x1800) and a Plays page (one 2x2 drawn five ways). The 17 moves stay as "Moves (examples)": worked examples of how the parts go together, not forms. Start here was rewritten to say so.
- **`fmt-post-visual` and the designer** build from the kit: visual philosophy finds the idea's shape first, the moves library supplies a proven way to draw it or the marks build a new one, and an example is only a starting copy when its layout already fits, changed until it carries this idea (the count of cells, steps or bars comes from the idea). The old line that called visual philosophy only "when no move fits" is gone. `docs/spec.md` records why: consistency comes from the kit and the design system, the layout from the idea.
- **`setup-figma`** connects "the visual kit"; the phrase is "set up my Figma". `apply-brand.js` and `footer-name.js` use the new page names.
- **Every stage, explained.** `setup-start` holds one table: for each setup stage, what happens, why it's there, what the person has at the end, how long, and what they lose if they skip it, plus a paragraph on skipping the interviews. Every setup skill opens with its row and closes with what changed and what's next. `CLAUDE.md` rule 7 makes the same true for every task.
- **`docs/quick-start.md`** says why for each day-one step, what skipping it costs, why the interviews matter, and a section on what happens if you skip them. `YOUR-STUDIO.md` says the same in two sentences.

## 0.14.0 · 2026-10-22

Quick wins first. A person gets things they can use on day one, before any interview, and the interviews later make all of it theirs.

- **The new setup order.** Intake, then the quick wins (template library, dashboard, first post), then the interviews, the strategy, "make it yours", the first piece through the crew, and `/check`. `setup-start` conducts it with two new stages ("quick wins" and "make it yours"); a quick win can be skipped. `scripts/build-instance.py` starts every instance at "quick wins", lists them in `canon/setup-progress.md` and in a new "Start here" section of `YOUR-STUDIO.md`. `strategy-brand` hands over to "make it yours"; `setup-check.sh` treats the new stages as early.
- **`docs/quick-start.md`.** The road in plain words for the person: what to do on day one, what works before the interviews and what waits for them, the interviews, what comes after, the week once set up.
- **The Figma template library master** (`figma_master` in the manifest). A Start here page; V1 to V17 at 1080x1350, each with a note on its job and the shape of idea it needs; a seven-frame carousel set; a field guide at 1500x1800; a plate in two versions; a Brand page. Every fill and stroke is bound to a "Style" collection with two modes (Neutral, which never changes, and Brand), and all type uses seven text styles, so a brand goes on in one step.
- **`setup-figma`.** The person duplicates the master with one click; the skill connects the copy and, when they gave colors and fonts at intake, puts them on it with `references/apply-brand.js` (Brand mode, text styles, nearest font weight, contrast warnings) and their name in the footers. Tested on the master with a sample brand and reset.
- **`setup-first-post`.** One post from material the person already has, through the full LinkedIn chain, facts only from that material, a visual from their templates when Figma is connected. Writes a `quick_start: true` piece; the librarian counts its edits but never treats it as an orphan.
- **`setup-visual-identity`** ("make it yours"). After the strategy: keep and tune the brand they have, or build one with `craft-contradiction`; writes `canon/visual/design-system.md` from a new template, reruns `setup-figma` with it, draws their top two or three frameworks as signature visuals, and updates the dashboard and guide.
- **`setup-notion` without a token.** The connector route: the person duplicates the master and the studio finds and fills it through the Notion tools in Claude. `scripts/sync-notion.py --dump` prints the rows in the connector's shape; every role does the Notion half of the sync through the tools when `config/tools.md` says `route: connector`. The master's top page and Home were reordered (the pipeline board sits under Pipeline) and Home gained a "Your template library" callout.
- **The designer and `fmt-post-visual`** build from the person's template library: duplicate the move's template, judge it in the Neutral mode, style it by switching to the Brand mode. Without a design system, the Brand mode from intake is the look.
- Intake question 11 now says the template library and the dashboard come first.

## 0.13.0 · 2026-10-23

The dashboard, as the person's own app.

- **`docs/dashboard-app.md`**, the contract: six entities (Piece, Idea, Proposal, CanonEntry, WeeklyStat, StudioSettings), seven pages (Home, Pipeline, Body of work as the tree of knowledge, Idea bank, Your files, Numbers, How your studio works), the person-owned fields, and the rules: files are the truth, decisions come back through the producer, the app never changes a stage, IDs are the join. The master app lives in Base44 (`dashboard_master` in the manifest) in the Engraved Swirl style by default, with a person's colors and fonts overriding when set. The Notion template spec stays as a later mirror.
- **`scripts/sync-dashboard.py`.** Reads the files and pushes them to the person's app; reads their decisions (your decision, your answer) back as lines in `pieces/_decisions.md` for the producer, then clears them. Silent when no dashboard is connected. Every role runs it as its last step.
- **`setup-dashboard`.** Copies the master for a person, connects the sync, fills it, deploys, hands over the link. Intake no longer ties the dashboard to Notion; everyone gets one.
- **`scripts/save.sh`.** The end of every session commits the person's files and pushes when there's a remote. The person never types git.
- **`craft-human`:** signposts ("Here's why:") stay when the explanation follows at once and the person would say it out loud; one per piece at most.


## 0.12.0 · 2026-10-23

Setup in two phases. Phase 1 is facts and gives the person a studio that is already theirs before any interview; phase 2 is the interviews.

- **Intake** (`docs/intake-questions.md`, `templates/intake/answers.yaml`). Fourteen questions about facts, about ten minutes: who they are, what they want, where they publish and how many hours, their material and recordings, Notion and Figma, their look (assets, three references they like, three they can't stand), and anything the studio should know. Five are required. One question, one answer. The same questions run two ways and produce the same `config/intake.yaml`: as a form the person fills in before installing (Tally or similar), or inside Claude with "set up my studio" (`skills/setup-intake`).
- **`scripts/build-instance.py`.** Builds (or, with `--fill`, fills) a person's instance from the answers: their repo from the studio, `config/tools.md`, `canon/strategy/outcomes.md` in their words with hours under Capacity, `canon/visual/brand-assets.md`, `canon/setup-progress.md` with intake ticked, their uploads in `inbox/`, and `YOUR-STUDIO.md`: a one-page guide to their studio written for them, their words quoted, lists rendered as sentences or bullets. It never guesses: a blank stays blank and says so. Notion and Figma are recorded as wanted; the skills that build them come next. The script is the one source for those files' shape; the drifted templates and `config/tools.example.md` are gone.
- **`/start` is the setup conductor.** It says the road once (intake, then the interviews where the studio learns what they believe, reading what they've made first when it's in hand, then the strategy, then the first post; a few weeks to set up, about a year to work), sends a new person to "set up my studio", greets a person who came through the form by name and points at their guide, says nothing twice when intake just ran, and rewrites the setup section of `YOUR-STUDIO.md` at every stage. It says how material that isn't a text file gets in (paper photographed or typed, audio transcribed) instead of promising a read-back it can't do.
- **The brand tree reads intake.** It no longer asks what they do or what material they have; it reads intake back in two or three sentences, routes with a rule for when material and a clear answer both apply (material first, then their answer; a lot of material makes the read-back the whole first session), writes the rules in their intake notes as draft stop-list entries, reads the goal and the channels back instead of re-asking them, asks the target association from the vehicle's `known_for`, points the voice samples at `inbox/`, keeps an entry draft until all its fields are in, glosses a studio label once per session and then uses it bare, and sets the stage in `setup-progress.md` when a session ends.
- **Scripts.** `status.sh` prints the setup stage first and says "not started yet" instead of "missing" before the interview; it counts a file's own `status` only when the file has real content. `setup-check.sh` reads the stage and reports what the interview and the strategy haven't written yet as "not yet", not FAIL, so `/check` never reads as broken; the voice-rule check accepts the template's heading shape.
- Seventh and eighth studio tests: `tests/studio/intake-form-lena/` and `tests/studio/intake-claude-marco/`, each with the first run's notes that produced the fixes above.


## 0.11.1 · 2026-10-23

- **The full LinkedIn library.** `skills/fmt-linkedin-post/library/posts/<ID>.md` holds the full text of all 357 sorted posts (from Josué's two libraries: 256 from the Storied library, 101 from the swipe file), one file per ID with its tags in the frontmatter and the hook and body notes. The index CSV gains `Visual URL` and `Media` (text, image, carousel, infographic); 174 posts have the visual that ran with them. The moves and draft stages now read each example in full instead of the hook line plus a URL, and `fmt-post-visual` can pull real post-and-picture pairs by media type.


## 0.11.0 · 2026-10-23

The v1 candidate: the checks, the last setup stage, the spec brought level with the build, and the scope said plainly.

- **`scripts/check-mechanical.py`.** The checks a script can decide, run on every draft before the editor reads it: em dashes, "Not X. Y." pairs, reveal devices, "quietly", decoration adverbs, "expert", claims about what people in general think, a `## Post` section, a source map with rows, every ID resolving to the canon or the idea bank, every number in the post sourced. The writer runs it before handing off (step 6); the editor runs it first and a fail is a gate. IDs inside quotes and code spans aren't IDs; `2024 Q2` isn't Q2.
- **`setup-check`** (`/check`). The last setup stage. `scripts/setup-check.sh` checks the studio files, scripts, the manifest against `studio-source.md`, the person-owned folders, the minimum canon, the confirmed strategy, the channel files, the voice guide and that the canon has no em dashes; then the skill runs one test piece through the whole crew with the real canon to `reviewed`, never ships it, and sets the stage to `setup done`. `/start` gets a check stage.
- **`/update`** (`scripts/update-studio.sh`, from 0.10.1). A person's instance is its own repo carrying `studio-source.md`; the script replaces the studio-owned paths from `studio.manifest.yaml` and never touches canon, pieces, config, inbox or proposals. `--init <path>` makes a new instance.
- **Spec brought level.** `docs/spec.md` gains "As built, v1": the scope, what exists, a table of the decisions that changed the spec and why, and what from the spec isn't built. The crew table shows capture and the librarian as built.
- **Scope said plainly.** The README names what v1 covers (one person, their own instance in Claude Code, LinkedIn posts, files) and what it doesn't. `docs/install-in-claude.md` marks the Claude app path "not yet": the skills read each other and the canon by repo path.
- **Welcome path fixes.** From the sixth studio test, a fresh instance from `--init` taken through `/start` and the first interview session by a fictional person. `/start` explains the studio once and the brand tree skill no longer repeats it; it says "your files", not "canon", and every studio label comes with what it means for the person. `/start` asks two questions (the goal, and channels plus hours a week) and no longer asks about Notion or Figma until setup is done; the year-long horizon moves there too. The vehicle session refines the goal from `outcomes.md` instead of asking it again. `setup-brand-tree` gets the missing branch for material that exists but isn't in hand (route on what's here, plan extraction, take the story offered now), a session swap for POV-first people, the list of the 17 files step 5 creates and the three it doesn't, what "fill in what's known" means, a read-back step so a story told in full is confirmed in the same session, the permission question in nine words, a `from` field that waits for values, a Constraints section in `vehicle.md` for capacity, acknowledgement by restating instead of "Noted.", and an ending written for a repo. Templates lose their example blocks on creation, and `scripts/status.sh` skips placeholders and counts a file's frontmatter status once, so a person after session 1 sees the drafts they have and not fourteen. `config/tools.example.md` no longer carries its copying instruction into the person's copy.
- Sixth studio test: `tests/studio/welcome-tomas/`.


## 0.10.0 · 2026-10-23

The designer role. The crew is complete.

- **`role-designer`** (`/design`). For a piece that passed review and has a visual: runs `craft-visual-philosophy` to find the idea's structure (or says the idea is words and has no visual), runs `fmt-post-visual` for the format and the move with three options of different mechanics, writes every headline and label in the reader's words to pass the stand-alone test, builds in neutral and runs the six tests, applies the person's design system from `canon/visual/` (or stops at neutral and says the visual waits on `setup-visual-identity`), judges at feed size, sets `designed`. Words on a visual may only say what the piece says; numbers only from the source map. Untested until a design system exists to apply; the structure half runs today.


## 0.9.0 · 2026-10-23

The librarian and the producer's clerk, with the fixes from the librarian's first run. The loop the spec describes now closes: capture → strategist → writer → editor → producer → librarian → proposals → the person → the canon.

- **`role-librarian`** (`/librarian`, `/correct`). Part A, after a piece ships or weekly: diffs the final against the last draft and sorts every change (voice edit, repeat, contradiction, limit confirmed, definition); reads the evidence ledger; counts against the person's thresholds (a belief three times, a story twice, a voice edit twice where the person stating the rule counts as a mention, a contradiction once, an asked-for definition at once); writes proposals in the person's words with a dated evidence list and one question, never more than five open; sets `used_in` on material a final carries; rewrites the body-of-work index with orphans, dead ends and pieces shipped over a redo; and turns `studio-notes.md` into proposed skill fixes, marking done the ones that already landed. Part B is the correct entry point: what, the true version word for word, the source, the follow-up, and on the person's yes it makes the canon change as their hands.
- **`role-producer`** (`/review`). The clerk for the person's decisions at the two gates and on proposals and questions: records each in their words with the reason, sets the status, names the next actor, asks for the final as published, and logs `signal` lines when they say how a piece did. It never decides for them.
- **Templates.** `final.md`; `signal` lines in the piece log; a Note column in the index; a dated evidence list and `[librarian's wording]` marks in proposals; the ledger's kind list.
- Fifth studio test: `tests/studio/librarian-mara/`.


## 0.8.0 · 2026-10-22

Capture, the input side, with the fixes from its first test run.

- **`role-capture`** (`/capture`). Reads whatever the person dropped (text, or files in `inbox/`), splits it into one idea per entry with the raw text kept word for word (speaker labels kept, `[...]` where filler was cut), types each entry (story, POV, method, question, observation, proof, objection, outside), links it to any canon ID, marks what fits this quarter's branches, sets permission by source (calls anonymize, journals private, memos public unless anyone else appears), folds later captures of the same idea into the existing entry as `also:` items, and ends with a few lines for the person: counts, the permission questions, what went to proposals because they asked for it, and the one entry the strategist can use first.
- **The evidence ledger** (`canon/bank/evidence.md`). One line per mention of something the canon doesn't hold or holds in other words. Capture and the editor write lines; the librarian counts them and proposes. `proposals.md` is reserved for things the person has to answer, so `/status` stays honest. The one exception: when the person asks out loud for something to be written down, it goes straight to proposals.
- **Templates.** `ideas.md` gains `method` as a type, `also:` blocks, `wanted_now`, `who_said_it`, `note`; new `questions.md`, `evidence.md`, `inbox/README.md`. The content plan gains an input minimum (entries a week, derived from the cadence) that `strategy-brand` sets and capture reports against. The brand tree interview now creates `canon-index.md` and every bank file at setup, so the roles find them.
- `/status` reports entries captured in the last seven days and files waiting in `inbox/`.
- Fourth studio test: `tests/studio/capture-mara/`.


## 0.7.0 · 2026-10-22

The per-piece strategist, with the fixes from its first test run.

- **`role-strategist`** (`/brief`). Part A, weekly: the runway in weeks, candidates from the idea bank, the plan and the thin spots in the body of work, a kill list (doesn't trace to the thesis or fails the cohesion test, anti-association, needs a fact the canon lacks, topic-popular, two ideas, a repeat, private material), a ranking in five rules that stops at the first that separates, and `pieces/shortlist.md`. Part B, on the producer's pick: the piece folder and a brief whose Material lines are verbatim entry fields with IDs, a decided call to action, and the format plan from the moves stage with the card's name copied, examples that share move and structure, and WATCH FOR from the card. Interview answers go into the idea bank word for word. Two statuses when questions stay open: `briefed` (the writer can draft without a guess) and `blocked` (it can't). Items the canon names but doesn't fill go to a "Waiting on the person" section that `/status` surfaces, not to the kill list. With the person away, the strategist keeps briefing until the runway target is met.
- **Templates.** `pieces/index.md` (the body of work: every piece by branch, layer, state), `pieces/shortlist.md`, `canon/bank/ideas.md` (raw captures, I IDs), `templates/proposals.md`. The brief gains `channel` and `layer` in its frontmatter and a bracketed voice note where an entry's wording breaks the voice guide.
- Third studio test: `tests/studio/strategist-mara/`, three raw ideas with one trap. The writer-editor fixture's conditional call to action is fixed; it broke the strategist's own rule.


## 0.6.1 · 2026-10-22

The writer and editor roles, with the fixes from their first test run.

- **`role-writer`.** Drafts from an approved brief only, through the format skill's draft stage, with a short argument check (the writer-sized copylosophy pass) written into the draft, a source map that says for each line whether it's the person's quote kept or an interviewer's note restated, and a `## Post` section that holds only the post. Rules added from the run: what to do when a brief's format plan contradicts itself (pick the card the material carries, write a PLAN NOTE), when a brief line outruns its cited entry (use the entry, flag a brief defect), when a term the person uses has no canon definition (don't define it; write a proposal), when the brief hands over a conditional call to action (no-CTA post, CTA as CLOSE ALT, decision up). Strategy files in draft don't block a piece.
- **`role-editor`.** Judges in a fresh context in three layers: gates nothing can be scored around, a weighted score by branch (`references/scoring.md`), and a ranked report with one move. Rules added from the run: the invented-material gate has two grades (a new fact is a redo; a claim that stretches a confirmed entry is a fix), brief defects are a severity of their own that go to the producer, the hook is judged against the writer's PLAN NOTE card, the verdict mapping across the three scales is written down, each finding has one owner across the gates table, the format block and check-human. Both roles run as agents in Claude Code (`.claude/agents/writer.md`, `editor.md`).
- **check-human** and craft-human now agree on the pass rule (two patterns or fewer, none in more than two places). `scripts/check-human.py` measures a draft's `## Post` section alone. The editor's check-human run lives in the review; no separate file.
- **Library truth.** The sorted CSV holds each post's hook line, tags, notes and URL, not the full text. The moves and draft stages said otherwise in four places and now say what the file holds.
- Second studio test: `tests/studio/writer-editor-mara/`.
- `studio-notes.md` at the repo root: one line per place a skill made a run guess, from any role. The studio's own loop.


## 0.5.0 · 2026-10-21

Added the craft layer: the standards every format runs under.

- **`craft-copylosophy`, `craft-visual-philosophy`, `craft-contradiction`.** Josué's three methods, ported whole with a short "in the studio" header each: where their inputs come from in the canon, who calls them, where the output goes. Copylosophy runs in the writer before any piece that argues and in the editor as check 28 (a false premise is a redo). Visual philosophy runs before `fmt-post-visual` picks a move and writes `visual-brief.md` into the piece. Contradiction is the method behind `setup-visual-identity` (not yet built) and writes `canon/visual/contradiction-brief.md`.
- **`craft-human` and `check-human`.** The standard that sits under every voice guide: six patterns that mark text as machine-written (nobody in the room, every sentence weighs the same, ladders and triads, a landing line on every paragraph, no stance, every loop closed), a worked before-and-after, and what not to do (no planted mistakes). `check-human` marks the lines and gives pass or fix; `scripts/check-human.py` measures the counts and, with a Pangram key in `config/tools.md`, records the detector score as one more reading. The judge gets section F (check 29). The writing rules gain one clarification: stance words a talker uses stay; decoration adverbs go.
- The old LinkedIn writing skills and the format-type skills stay out of the studio on purpose; the moves library is the current truth about what works.


## 0.4.1 · 2026-10-21

Test run of `strategy-brand` on a fictional person, and the fixes it produced.

- The skill now says what gate 1 means (lived the reader's situation, or fixed their problem enough times to see a pattern), where gate 2 reads from (a new `reads` field on each audience segment, with its interview question), that one file per platform carries several jobs, that a wanted-but-not-live channel gets a `starts when` line, how to trim cadence to capacity (costs in `references/rules.md`), that pace and reach-versus-relationships are two different numbers, that one confirmed branch is enough, where proposals go (`proposals.md`), where the review goes (`canon/strategy/strategy-review.md`), to create `canon-index.md` if the interview didn't, and to carry `permission` into the channel files.
- Templates: `reads` on audience segments; `starts when`, the arithmetic and permission on channel files; the quarter as 13 weeks from start; first-run wording for the reputation gap and the reputation checks table.
- First studio test: `tests/studio/strategy-brand-mara/`, a complete fictional minimum canon plus the checks a run must pass, the first run's outputs and its notes on the skill.


## 0.4.0 · 2026-10-21

Added the strategy layer: the method and the skill that runs it.

- **`docs/strategy-method.md`.** How the studio gets from a confirmed canon to a personal branding strategy. Synthesized from 25 transcripts (Josué's Network Design Workshop and Personal Branding Model, Caleb Ralston, Alec Paul, Adam Robinson, Gal Aga, Josh Sanders and others), checked against the sources by a separate pass, and reviewed by Josué. One derivation in seven questions, five branches by goal (clients for a practice, pipeline for a company, an audience business, a career or capital, the reader isn't on the channel), per-branch defaults for mix, cadence and signals, and the studio's position on each place the sources disagree. Decisions: no archetypes (a character sheet instead), branch A has two paces (clients soon, body of work first) blended as one plan, cadence set per branch, anti-associations required, no paid promotion for now, a hybrid ghostwriting stance.
- **`strategy-brand`.** Runs the derivation once the minimum canon is confirmed, writes `brand-strategy.md` with reasons, one file per channel in `canon/strategy/channels/`, and the quarter's content plan, then shows the person each choice for a yes. Reruns each quarter from the signals.
- **Templates.** `brand-strategy.md` gains branch and pace, the character sheet, anti-associations, a channels table, a time horizon and open questions. New `strategy/channels/channel.md`. `content-plan.md` gains the weighting, stories in rotation, cadence by channel, signals and a last-quarter section.
- **Handoffs.** `setup-brand-tree` no longer drafts the content plan or decides channels; it hands to `strategy-brand`. Its interview records which channels the person uses and asks one capacity question. `/start` has a strategy stage between the brand tree and the first piece, and the welcome now says two things plainly: about a year before it works in a real way, and the studio drafts from the person's inputs while they make the calls. `fmt-linkedin-post` reads `canon/strategy/channels/linkedin.md` for the channel's job, mix and selling rule.


## 0.3.0 · 2026-10-21

Added the front door and the operating guide, so a new person can find their way without anyone in the room.

- **`setup-start`** (`/start`). On the first session it explains the studio in a few sentences, asks three questions (what they want in a year, where they publish, whether they use Notion or Figma) and writes `canon/strategy/outcomes.md`, `config/tools.md` and `canon/setup-progress.md`. Every session after that it reads the files, says where the person is in setup and gives one next step. It ends after one step and doesn't mention optional tools until the first piece has shipped. The spec's separate setup-welcome agent is folded into this skill; there wasn't enough to it to be its own.
- **`check-status`** (`/status`). The front door after setup: what's waiting on the person (briefs to approve, pieces to ship or kill, proposals to confirm, blocked pieces), what's moving, runway in weeks when a content plan exists, canon health, and one next step. `scripts/status.sh` prints the counts behind it.
- **`docs/operating-guide.md`.** One page: capture, decide, review; the daily, weekly and quarterly rhythm; what to say for each thing; where the person's files live; the two rules worth knowing.
- `.claude/skills/start` and `.claude/skills/status` make the two slash commands work in Claude Code. They point at the skills in `skills/`.

## 0.2.1 · 2026-10-21

Made the studio installable in the Claude app, not only in Claude Code.

- Added `scripts/make-skill-zips.sh`. It builds one zip per skill into `dist/skills/`, in the layout the app's "Upload a skill" button expects, and checks each zip before it reports it built.
- Added `docs/install-in-claude.md`: the two ways to run the studio (Claude Code with the whole repo, or the app with uploaded skills and a Project per person) and how to update after a new studio version.
- Added `.gitignore` for secrets, built zips and OS files.

The packager and the install steps were adapted from the Second Brain Factory repo. Nothing else from it was copied; the ideas worth keeping from it (folder-scoped rules, a `/recall` over the canon, a `/status` doctor, a correct skill that writes to `proposals.md`) are noted for the pieces they belong to.

## 0.2.0 · 2026-10-21

Fixed the five mismatches between the post chain, the brand tree interview and the spec.

- **Voice file.** The post chain now reads `canon/voice/voice-guide.md`, the file the interview writes. `voice-profile.md` is gone.
- **One brief.** `templates/piece/brief.md` now holds both halves: the spec's fields (parent ID, segment, desire, material with IDs, outcome, not saying, call to action, open questions) and a format plan that the format skill fills. For LinkedIn posts that's the hook move, structure, inside moves, close, examples and what to watch for. The moves stage writes into it instead of producing its own brief.
- **Canon first.** The moves stage reads the brief, the core summary, the linked canon entries and the idea bank before asking the person anything, and labels every piece of material with its source ID. It asks only about what's still missing, or about everything when no canon exists yet.
- **Names.** `content-studio` is now `fmt-linkedin-post` and `brand-tree-builder` is now `setup-brand-tree`. The visual stage and its library moved into their own skill, `fmt-post-visual`, because a post and its picture are asked for separately.
- **Goal.** The post chain's GOAL field is now PURPOSE: what this piece is for, taken from the brief or the content plan. The person's overall goal stays in `canon/vehicle/vehicle.md`.

The drafts and reviews from the post chain now save into the piece's folder as `draft-vN.md` and `review-vN.md`.

## 0.1.0 · 2026-10-21

First version of the repo.

- Added `docs/spec.md`, exported from the Content Studio Spec.
- Added `skills/brand-tree-builder`: the self-serve brand tree interview, with its references and 17 canon templates (including audience and content plan).
- Added `skills/content-studio`: the LinkedIn post chain (moves, draft, judge, visual stages) and its library (hook moves, body moves, visual moves, 357 sorted posts).
- Added the skeleton: `CLAUDE.md`, `README.md`, `studio.manifest.yaml`, piece templates in `templates/piece/`, and empty `canon/`, `pieces/`, `config/` and `tests/` folders.

Decisions in this version:

- The canon templates live inside `skills/brand-tree-builder/templates/` instead of a separate `canon-templates/` folder, so the interview skill works on its own and the templates exist in one place.
- `config/` is person-owned, because it holds one person's tool IDs.

Known gaps (fixed in 0.2.0): the voice file name, the two briefs, the post chain asking for material before reading the canon, and the naming prefixes.
