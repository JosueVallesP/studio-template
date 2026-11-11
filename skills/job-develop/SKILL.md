---
name: job-develop
description: >-
  Works one idea through until it can carry many pieces. Takes a seed the person planted (an idea bank entry, a thought they hand over, a question) and writes an idea sheet: the question under it, the claim, when it holds and when it doesn't, real cases, and what a reader leaves with, in the shape the idea has. Says what is the person's and what the studio proposed, and names the pieces the idea asks for. Drafts nothing. Use for /develop, "develop this idea", "help me think this idea through on paper", "what is this idea made of", "what pieces can this idea become".
---

# /develop

Method by Josué Valles, the studio's author.

An idea and a piece are different things. An idea is a question worked through until there is something to say about it: a claim, what it is made of, when it holds, what shows it, and what a reader can do with it. A piece is one way to show that idea, or one part of it. One developed idea carries many pieces: the long one that holds all of it, a post on one case, a post on the claim alone, a picture of how the parts fit.

A pitch with no developed idea under it leaves the person with nothing to write from. They read "a post about why raises don't make people feel freer" and don't know where to start. The sheet is what they start from.

## Where it sits

- `role-capture` plants the seed in the person's words. `/shape` finds ideas that already sit in raw material and says what form each wants. `/think about` is a conversation that helps the person say what they think. Develop comes after any of them: it takes one idea and does the thinking on paper, so there is a sheet to react to.
- Develop hands to `/essay` and `/post`, which build one piece at a time with the person, and to `/visual`.
- Develop never drafts a piece and never plants an idea. The seed is the person's. The thinking the studio adds is marked as the studio's until the person takes it.

## What it takes

- An idea bank ID, a thought the person hands over in the chat, or a question.
- With nothing given: the entries in `bank/ideas.md` at stage `growing` or `sprouting`, newest first. Name the top three in a line each and let the person pick.

## What it reads

- The seed and its record in `bank/ideas.md`.
- `canon/`: the POVs, the thesis and the stories that touch the idea. With no canon, what the person has said and `material/`.
- What the person has already put out on the subject: shipped pieces in `pieces/`, and published posts and essays in `material/`.
- `skills/craft-house-rules` for the writing, and `CLAUDE.md` rules 1, 6 and 8 for what is theirs and what is proposed.

## Procedure

1. **Say the question back.** Every idea starts as a question about how something works in the reader's life. Put the seed as that question, in one line, with one line on why you read it that way. Wait for a yes or a change. This is the only stop before the sheet.

2. **Check what they've already said.** Read what they've published and confirmed on the subject. If the idea argues against something of theirs, say so before writing anything, quote both sides, and let them choose: they've changed their mind (it goes to `proposals.md` as a contradiction, `CLAUDE.md` rule 6), or the idea is left. A clash found after the sheet is written costs the whole sheet.

3. **Work the idea.** Ask of it, in turn: what it is, what it is made of, what would prove it, what argues against it, how a reader will take it, and what it is for. These are the studio's working questions. The person never sees their names and is never asked them. They see the answers.

4. **Write the sheet, in the shape the idea has.** A developed idea has no fixed layout. It is developed when the sheet answers four things:
   - What is the claim, in one or two sentences?
   - When does it hold, and when does it not?
   - What real case shows it?
   - What does the reader leave with?

   Ideas have different shapes and the sheet takes the shape of the one it holds: one thing split into its parts, a test for telling two things apart, two things people treat as one, a cause people get backwards, a trade where both sides cost something, a change that happens in stages. These are examples. If two sheets in a row come out with the same headings, the second one was forced. The ending varies as well: a question the reader can ask, a single line, a picture, or nothing.

5. **Cases.** The person's own cases come first, each from their files with its source (`CLAUDE.md` rule 1). An outside case is a real one with its source named, marked `borrowed: verify`. No invented case, and no case stretched to cover a part it doesn't show. A part with no case is left as a gap.

6. **Close with whose is what.** This is the one fixed part of every sheet:
   - **Theirs:** each fact and view, with the canon ID or the file it came from.
   - **Proposed:** every part the studio added (a split into parts, a test, a reading of one of their stories). It stays proposed until they take it.
   - **To check:** outside facts not yet verified.
   - **To ask:** what only they can supply, such as a story they haven't told.

7. **Show it and let them react.** Put the sheet in the chat. They accept, change or reject each proposed part. Don't follow the sheet with a list of open questions (`skills/craft-house-rules`, S3); the "to ask" items wait for when they matter.

8. **Name the pieces the idea asks for.** Only those, each in one sentence saying what that piece would say. The long piece comes first. Each post is built fresh from the sheet by `/post`; none is cut out of the long piece. For a LinkedIn post, match it to an idea brief (`skills/fmt-linkedin-post/library/idea-briefs.md`) and hold the brief's "What you need" list against what's on file: a post whose brief needs something the person hasn't said waits for them, and the sheet says which. For each piece, say in a few words what its visual is for (show the person, set a feeling, show the idea, hold many facts) or that it has none. The same six forms listed under every idea is a sign nobody looked.

## What it writes

- `bank/sheets/<short-name>.md`: the sheet, with `status: proposed` at the top, then `accepted` once the person has gone through the proposed parts, or `dropped` with the reason in one line.
- In the seed's record in `bank/ideas.md`: one dated line under what fed it (`developed: bank/sheets/<short-name>.md`). An objection the sheet found goes in the seed's `pushback` as `open`.
- A part the person takes that states a belief, a method or a model of theirs goes in as a `draft` entry in its canon or bank file, as `skills/setup-brand-tree` says under "Where a picked-up belief goes". Nothing else touches the canon.
- One line in `sessions/log.md`: `<date> · develop · <short-name>`.

## What it says to the person

The sheet itself, then one line on what is theirs and what is proposed, then the pieces. Under 150 words around the sheet. End with the one thing they can react to: "Does this hold as you'd say it, or is a part off?"

## Never

- Never draft a piece. `/essay` and `/post` draft.
- Never take an idea from their past posts and hand it back as new. Past posts say what they think and supply facts and stories.
- Never show the names of the working questions.
- Never use a fixed set of headings.
- Never write a proposed part as if they had said it.
- Never invent a case, a number or a story.
- Never write to the canon beyond a `draft` entry they said yes to.

## Studio notes

Where this skill made a run guess (a shape that was hard to name, a part with no case), one line in `studio-notes.md`.
