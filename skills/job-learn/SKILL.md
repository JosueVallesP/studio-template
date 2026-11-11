---
name: job-learn
description: At the end of a session, lists the choices the person made in it (a voice rule, a banned word, a structure they liked or rejected, a fact they corrected, a belief they stated) and asks yes or no to each; the yeses go where the studio will read them next time (the voice guide, the canon files as drafts or confirmed entries, the piece's log). Use for /learn, "save what we decided", "remember this for next time", at the end of a working session.
---

# /learn

Every session makes choices: "cut the question at the end", "I'd never say 'leverage'", "that's not my opinion, this is", "I liked the story-first opening". Without a step that saves them, the next session starts from zero and the person edits the same things again. This skill is that step. It runs at the end of a session, lists what it saw, and lets the person keep or drop each item.

## What it reads

The session itself: the person's edits to drafts, their corrections, their reactions to options, the things they said about themselves that no file holds yet. Then the files those would land in, so it doesn't propose what's already there:

- `canon/voice/voice-guide.md` (rules W, vocabulary, approved and rejected samples).
- `proposals.md` (what's already proposed on the entries the session touched).
- The canon entry the item would change, if any.

## What counts as a lesson

Five kinds. Anything else is session chatter and stays out.

1. **A voice rule.** How they write or won't write, specific enough to check: "no rhetorical questions as closes", "say 'clients' not 'customers'". Goes to the voice guide as a W rule with a before and after line taken from this session. If the move also sits in a rewrite pair as a `new` line, change that line's tag to the new rule's W number, in every pair that has it; that closes the lesson in the pair, so the writer's slots go to moves no rule holds yet.
2. **A vocabulary item.** A phrase they use, a term they coined, a word they'd never use. Goes to the voice guide's vocabulary.
3. **A fact about them.** A belief they stated, a story they told, a result they named. It follows `skills/setup-brand-tree/SKILL.md`, "Where a picked-up belief goes": a new one becomes an entry in its canon file, in their words, with `quote`, `sources` and a log line. Their yes here confirms it only when its required fields are present; otherwise it stays `draft` with "agreed in /learn <date>" in the log. A correction to a confirmed entry works the way `/correct` does (`skills/role-librarian` part B): the list shows the entry as it reads now and their words beside it, and their yes on that item is the person changing the canon in the session, so make the change, add a `log` line (`<date> changed by the person via /learn: <was> → <now>`), and close any open proposal on that entry as `accepted <date>`. Nothing goes to `proposals.md` and nobody asks a second time.
4. **A sample.** A post or passage they approved as sounding like them, or rejected. Goes to the voice guide's approved or rejected samples with one line on why.
5. **A rewrite.** The person took a draft and handed back their own version of it. This one needs no yes and no threshold: write the pair to `bank/rewrites/<piece id>.md` (named by the piece, so the producer finds it on ship; if a file there already names this piece in its `piece:` line, add to that one) from `skills/setup-brand-tree/templates/bank-working/rewrites-template.md` the moment it happens (the draft's `## Post`, their version, what changed in three to six quoted lines, each ending with its rule tag as the template sets out: the H or W number of a rule the draft broke, `new` for a move no rule covers, or `piece` for a change about this piece only). Write the detector reading on their version as "not run": `/learn` never calls the detector, and the producer's call on the shipped final covers it (`CLAUDE.md`'s detector paragraph). The writer reads the last ten pairs before every draft (the default in `skills/role-writer`), so this is the fastest way the studio starts writing like them.

## How the person works

Beside the choices about writing, `/learn` keeps one short section in `config/working.md` (person-owned; create it on first use) on how this person uses the studio: which commands they reach for and which they never touch, the journal modes they use, when they work (a session a week, or every morning), what they skip and why, and how much they want said back to them. `/coach` and `/status` read it to suggest less and the right things; the writer reads nothing from it. One line per fact, dated, replaced when it changes, never a guess: only what the session showed or the person said.

## Procedure

1. Write any rewrite pairs first (kind 5; they don't wait for the list). Then go back through the session and list every other candidate, one line each, in the person's words where they exist: what the lesson is, the kind, where it would go, and the moment it came from ("when you cut the last line of the pricing post").
2. Drop anything already in the files, and anything that was about this piece only (a fix to one line isn't a rule unless they said it should be).
3. Show the list, numbered, and ask them to say which to keep: "all", numbers, or "none". Don't save anything before they answer.
4. Write each kept item where its kind says, in the file's own format (a W rule has a before, an after and a source; a canon entry has an ID, a quote and a log line). Add a dated log line to each file touched.
5. Say what was saved and where, in one line per item.

If the session made no choices worth keeping, say that in one line. An empty `/learn` is a fine result; a padded one teaches the studio things the person never said.

## Rules

- Nothing is saved without a yes on that item.
- The person's wording stays as written. A rule they stated in their words isn't reworded to sound like a rule.
- Never save a lesson the person didn't make: your own judgment about their writing isn't theirs.
- Never write a fact about the person into a skill. Facts go to the canon or the voice guide.

## Studio notes

When this skill made you guess, write one line per guess to `studio-notes.md`.
