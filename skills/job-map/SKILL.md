---
name: job-map
description: >-
  Reads a person's whole body of work (posts, essays, talks, a book, call transcripts, memos and notes, public and private) and maps how their ideas connect: the claims they make, the stories and frameworks that carry them, and the links between them. Hands back the findings a person can't see from inside their own work (their spine, one idea said many ways, unmade connections, gaps, tensions, dropped ideas, how their thinking changed, what they say in private and never publish), drawn as a tree they open in any browser, then a 20-minute review of the strongest ten. Leaves draft entries for the interviews. Use for /map, "map my ideas", "read my material", "read-back", "what do I already believe", "how do my ideas connect", "update my map", and as the first step after intake.
---

# The map

A person with years of work can't see its shape. They're too close to it, and nobody has read all of it in one sitting, including them. The studio can. This skill reads everything they've made and said, finds the claims in it and how they connect, and shows them what they haven't noticed: the few ideas everything else hangs from, the same idea said seven ways, two ideas that make a third, the places they assert and never argue, what they tell clients and never publish.

The studio is for people with a lot of material, so this is the first real thing it does for them. It has to pass one test: every finding makes the person say "I hadn't seen that", or "yes, and here's what I actually meant". A map that tells them their topics has failed.

Seeing is putting things already in the files side by side; inventing is adding what isn't there (`CLAUDE.md` rule 8). Every finding quotes the lines it rests on, and nothing on the map is true about the person until they say so.

## Where things are

- **Reads:** `material/`, `inbox/` (run `python3 scripts/inbox-to-text.py` first; a file it marks as a summary, or one marked as written for them, is read as `references/reading.md` says, never for their words), `config/intake.yaml` (`what_you_do`, `goal`, `notes`), and the canon and banks if they exist (so a confirmed entry isn't raised as news, and a `no` is never raised again). Never `journal/`.
- **The reading rules and the drafts:** `references/reading.md`. Read it before you read a file.
- **The data file and what's checked:** `references/map-data.md`. Read it before you write the map.
- **The kinds of finding:** `skills/job-think`, "What it looks for" (kinds 1 to 13). That list is the one definition.
- **Writes:** `bank/map/map.json` (the one source), then `python3 scripts/map-render.py` builds `bank/map/findings.md` (the page), `bank/map/map.html` (the tree, opens in any browser, works offline; a View switch turns the same map into an orbit they can drag around, with the spine in the middle) and `bank/map/map.canvas` (the same map for Obsidian). Draft entries in the canon files, as `references/reading.md` says.

## Tell them what and why

Before reading, one short paragraph (rule 7; the words for setup are in `skills/setup-start`): the studio reads everything they've handed over, public and private, and maps how their ideas connect; they'll get the strongest findings and a picture of the whole; it takes none of their time while it reads (a large body of work takes a while), then a 20-minute review where they say what's true. Say that private material (calls, memos) shows on their map, marked private, and never goes into a post without their yes.

## Working in the background

A large body of work is read in parallel, a bundle per reader (below). Readers run in the background so the person can do something else.

- **Say nothing about the readers while they work.** No counts, no "three of the four are back". The person hears about the map once, when it's done.
- **Never cut into a guided flow** (`CLAUDE.md` rule 9). If the intake, an interview, a journal session or `/think about` is going when the map finishes, say nothing until it ends, then one line: "Your map is ready: want to see the strongest findings?" If the session ends first, it shows at the start of the next one.
- When the person is waiting for the map and nothing else is going on, say so in one line when it starts ("Reading your 40 transcripts and 120 posts; this takes about N minutes") and then nothing until it's done.

## Procedure

### 1. Before reading

Run the converter on `inbox/`. If `config/tools.md` shows a calls, talks or reading source connected (`skills/setup-sources`), offer once to pull the calls or books the person says hold their best thinking; their pick, not a sweep. Then list every file with its kind, rough date, length, and its mark, `public` or `private` (`references/reading.md`). If a map already exists, this is an update: go to "Updating the map".

If the material is thin (a handful of posts and nothing else), say so before reading: the map needs a body of work to find patterns, and with this much it will find a few claims and little else. Ask for more (the ways in: `docs/handing-things-over.md`), or run it anyway if they'd rather.

### 2. Read, piece by piece

Read every file end to end, under the rules in `references/reading.md`. Past about forty thousand words, split the files into bundles of roughly that size and give each to a reader (the Agent tool, in the background), each with these instructions and `references/reading.md`; with fewer, read it yourself. Every reader returns, per piece:

- **Claims:** sentences someone could disagree with, each with the line it came from, word for word, and `outright` or `implied`. The test for a claim: could a thoughtful person in their field disagree? "Clients matter" fails; "pick clients for who they are and the price follows" passes. A topic ("pricing", "LinkedIn") is never a claim; find what they claim about it, or drop it.
- **Stories:** events with a time and people, or cases they teach with (marked `teaching`).
- **Terms:** frameworks, models, coined words, with credit when it's someone else's.
- **Who they cite:** authors, people, books, as a line under the piece (not nodes; they show who the person argues with and from).

And, once for the whole bundle, the files it didn't read to the end, with where it stopped. Those go on the source list as `read in part`, and the hand-back names them.

### 3. Merge

Put the claims from every piece side by side and merge the ones that say the same thing into one claim with all its versions, each with its quote and source. Keep the versions: one idea in many words is a finding (kind 1). Two claims that sound alike but differ in a condition stay two claims with a `tension` or `supports` link; don't flatten a real distinction.

Then count each claim in **separate pieces** (a post and its essay version are one), note the first and last date, and whether it ever comes with a reason or a story.

### 4. Link

Draw the links (`references/map-data.md` lists the kinds), each with the pieces that show it. Most come from inside one piece (a story told to prove a claim, a reason given for it). The valuable ones cross pieces: two claims from different years that one supports, a story from a call that carries a claim from an essay. A link the person never made is the studio's reading; it shows on the map as seen, not as theirs.

### 5. Find the spine and the roots

The spine is the three to five claims the others hang from: most supported by other claims, most carried by stories, in the most separate pieces over the longest span. Weigh evidence, not repetition: a line they repeat forty times may be a habit, and a claim stated twice with a story behind each may be the core.

For each spine claim, write one root question: what someone would have to care about, or what would have had to happen to them, to hold it. Write it as a question about an event, the way the interviews ask (`skills/craft-interview`): "What did it cost you the first time you picked a client for who they were?" Never "your value is X". Values are few, rarely change, and come out in the interviews; the root questions are where those start.

### 6. Find, test and rank the findings

Go through kinds 1 to 13 in `skills/job-think` against the claims, stories and links. For each candidate:

- **It quotes its evidence.** At least two quotes with their sources (a dropped idea, one). A conclusion the quotes don't carry is cut.
- **It's news.** Cut it if the person has already said it themselves (a connection they wrote, a spine they named in their About line), if it's a confirmed canon entry, or if an earlier map or `/think` session recorded a `no` to it.
- **It's specific.** "Your work is about trust" is a topic. "Every story you tell about a client who stayed starts with you turning work down" is a finding.
- **It ends in something to do:** a post (an unmade connection, a dropped idea, a story that could carry a claim), a question for the interviews (a gap, a tension, how the thinking changed, a root), or a yes or no (the spine, one idea in many words, a private claim).
- **No praise, no verdict on the work.** The map is a mirror. "Remarkably coherent" says nothing; say what connects to what.

Rank by how much of the work a finding explains and how unlikely the person is to have seen it. Mark the top ten `review: true`. Keep the rest in the file; the page lists them under the ten. Fewer than ten true findings is fine; never pad to ten.

### 7. Write and build

Write `bank/map/map.json` as `references/map-data.md` says, then run `python3 scripts/map-render.py` from the studio's folder. It checks the file, then builds the page, the tree and the canvas. When it refuses, fix what it names and run it again. The titles, the `what` lines and the tightened claims are prose the person reads: the house rules apply (`skills/craft-house-rules`), and their quotes are never touched.

### 8. Leave the drafts

Write the draft entries for the interviews as `references/reading.md` says ("The drafts it leaves"), put each draft's canon ID on its node (`canon`), and run the build again.

### 9. Hand back

In the chat, short:

1. What was read, in their terms ("your 120 posts, 14 essays and 40 client calls"), with the public and private split and the `left_out` line if there is one.
2. The three strongest findings, each in a sentence or two with one quote. Not the whole map.
3. The map itself: publish `bank/map/map.html` with the Artifact tool when it's in the session, so they get a private link; otherwise send the file (SendUserFile) or, on a Local install, say it opens by double-clicking it in their studio folder, under `bank/map`. Say in one line what they're looking at: the questions at the roots, the claims on the branches, the pieces as leaves, the findings beside it. Mention once that "View: orbit" shows the same map in 3D, for anyone who'd rather turn it around than read it top to bottom.
4. The next step: "The review takes about 20 minutes: we go through the ten strongest, and you say what's true. Want to do it now?" A yes runs the review below.

Then stop.

## The review

Twenty minutes, the ten findings marked `review`, one at a time, strongest first. When the brand tree hasn't started, this is its first session (`skills/setup-brand-tree`, step 2), and confirming follows that skill's rules.

For each finding: say it in a sentence or two, quote the lines, ask its question. Then:

- **Yes:** record `status: yes`. If the finding names a belief, story or method whose draft entry has every required field from the person (`skills/setup-brand-tree/references/fields.md`), confirm it by the brand tree's rules for a draft shown with its quotes; otherwise it stays `draft` with "agreed in the map review <date>" in its log. An unmade connection, a dropped idea or a story that could carry a claim goes to the idea bank as a `ready` entry of type `observation`, with its sources in `links`. A private claim they'd say in public: write that on its node (`ok_to_publish: <date>`).
- **No:** record `status: no` and their reason in `answer`. No later run raises it again unless new evidence appears.
- **Renamed or corrected:** keep their words raw in `answer`, offer a sharper version beside it if it's a half-thought (`CLAUDE.md` rule 3), and record what they keep. A renamed claim takes their wording as its `text`.
- **"I don't think that anymore":** on a change-of-mind finding or a tension, when they hold only one side now, the other claim becomes `held before` with the date and their reason as they said it, and a `replaced_by` link to the one they hold (`references/map-data.md`). Offer a draft stop-list entry for the old view in their words. From then on nothing quotes it as what they think now: the packet lists it for the writer, the mechanical check fails a post that says it as theirs, and `/recall` shows it apart.
- **Not sure:** record it; it stays open, and the interviews come back to it.

When their answer opens something, follow it with at most three questions (`skills/craft-interview`, moves 5 and 6), then move on: the review isn't the interview. After the ten, run the build again so the page and the tree show the answers, update `canon/progress.md` with the next session (the brand tree layer the answers point to, or the root question that got the strongest answer), and say in two lines what changed and what's next.

## Updating the map

"Update my map", or new material since the map's `updated` date (`/start`, `/status` and `/coach` can offer it in one line when a lot has arrived). Read only the new files. Add their claims to the existing nodes as new versions where they say the same thing, add new nodes where they don't, redraw the links they touch, and look again for findings. Keep every status and answer; a new finding gets `new: true`. Never rebuild from scratch: the person's answers live in the file. Hand back what's new in two or three lines, then the build.

## Private material in pieces

A claim or story whose versions are all private, or a draft entry with `privacy: private`, feeds a piece only after the person says it can, in the session or on the map (`ok_to_publish`). The client's side of a call never does; their words are a reader speaking (`skills/job-understand`). Names of clients follow the permission defaults in `skills/role-capture`, step 7.

## Never

- Never invent a claim, a link or a quote. If it can't be quoted, it isn't on the map.
- Never write a value. Roots are questions.
- Never treat a quoted author, a client's words or an AI's polished rewrite as the person.
- Never mark anything confirmed outside the review, and there only by the brand tree's rules.
- Never narrate the readers' progress, and never cut into a guided flow with the result.
- Never rebuild a map over the person's answers.
- Never write facts about a person into this skill.

## Studio notes

When this skill made you guess, write one line per guess to `studio-notes.md`: the date, the skill, what was unclear.
