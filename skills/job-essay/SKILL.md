---
name: job-essay
description: One Substack essay, end to end, from one command. Takes whatever the person hands over (or reads the idea bank and their material and offers the ideas they hold) and builds the essay with them in stops, as /post does: what they're saying, three to five titles and openings each tied to a structure, the section outline, then draft, judge and human check, without a brief approval, a strategist or a producer. Works on day one with no canon; uses the voice guide, the strategy and the canon when they exist. Use for /essay, "write an essay", "write a newsletter", "turn this into an essay".
---

# /essay

The same idea as `/post` (`skills/job-post`), for a Substack essay. Read `skills/job-post/SKILL.md` first; everything there about sources, voice, the stages (what you're saying, the openings, the outline, then draft and judge, each agreed before the next), the three contexts and the rules holds here. This file lists only what's different for an essay.

## What's different

- **The chain** is `skills/fmt-substack-essay` (moves, draft, judge) and its library. Read its `SKILL.md` and the stage files before running them.
- **An essay carries one idea**, and the idea has to be the person's. Where the canon has confirmed POVs or branches, the idea comes from one of them, or from the point the person agrees to in stage 1. Without a canon, the idea comes from what they hand over or from `material/`, and the point they agree to in stage 1 (or a quoted line from their sources) is enough for the moves stage: an opinion they've stated, a method they've used, a progression they've lived. When they say "/essay" alone, read `material/` and offer the three ideas it holds best, each in one sentence, and say which has the most material behind it.
- **Stage 1 goes deeper.** An essay carries a whole argument, so run copylosophy's writer pass in full with the person, the contrarian and provocation tests included whenever the idea pushes against common advice, and offer the scout for the best argument against as well as a case: an essay that never meets the strongest objection reads thin.
- **Stage 2 offers titles with openings.** Three to five options, each a title and the essay's first two or three lines, each tied to the structure it leads into, in plain words ("walks through your method step by step, with the two client cases as proof"; "an argument against the usual advice, answering the best objection"). The same rules as `/post`: only structures the idea and the material can carry, no invented material, your pick in one line. The essay moves stage (`skills/fmt-substack-essay/stages/moves.md`, steps 1 to 4, the reader's questions in step 1a included) runs first to know which are honest; when the studio offers the structures, the reader's questions decide which are on the table. Their pick sets the structure, the title move and the opening, and their words go in the plan's OPENING line. This is the one stop for the title and opening; the draft keeps the pick and sharpens it against the body, and drafts no new titles before the body exists.
- **Stage 3 shows the sections.** One line per section: the reader's question it answers, what it tells the reader and the scene or case it stands on, then the subtitle and the length as a guide. Their changes go into the plan's QUESTIONS and SECTIONS; then build the packet.
- **Material is heavier.** An essay needs more than a post: a scene or a case per section (the scene rule in `templates/piece/brief.md`), not one for the whole piece. In the moves stage, if the structure the idea asks for has sections the material can't fill, say which sections are empty and ask for them, or pick a structure whose required material lines are all present in the inventory (the gate list in the moves stage). Don't pad a section with the general point said twice.
- **The brief** sets `format: fmt-substack-essay`, `channel: substack` (or `newsletter`, whichever the strategy named), `path: direct`.
- **Source quotes:** the essay cap in `templates/piece/draft.md`.
- **Rewrites:** the writer reads `bank/rewrites/` the same way, with `python3 scripts/rewrites.py pick --format fmt-substack-essay`, which puts essay pairs first and post pairs after them. While the person has fewer than three pairs of their own, `pick` also lists default pairs (`skills/setup-brand-tree/templates/bank-working/rewrites-default/`, marked `default`): the writer reads only their "What changed" lines, as `skills/role-writer` step 1a says, and none of their phrases goes in the draft.
- **Section headers** inside the essay are `###`, so the check scripts read the whole `## Post` section.
- **The channel file** is `canon/strategy/channels/substack.md` (or `newsletter.md`) when it exists: access (free or paid, where the paywall goes), the plug rule, the sign-off.
- **The judge** runs `skills/fmt-substack-essay/stages/judge.md`, in the `judge` agent (in the foreground; if something else starts meanwhile, the essay waits its turn, `CLAUDE.md` rule 9), against the brief, the draft and the material. Same ladder: pass, revise, redo; one revision; then the person decides. The review is `templates/piece/review-direct.md`.
- **Length** comes from the format plan's LENGTH line, a guide and never a target: the essay is as long as its sections need. When the person wants it shorter or longer, that's a line in the brief, not a rewrite afterward.

## Show it

The essay as they'd paste it into Substack (title, subtitle, body), the judge's verdict word (pass, revise or redo) with any fail still open as one plain line, then two short lines: what in the material would make a second essay, and what the interviews add when the canon is empty. Then the decision that's theirs: post it and say `/review` and "ship it"; or say what to change; or "kill it". Offer `/visual` for the header image.

## Studio notes

When this skill made you guess, write one line per guess to `studio-notes.md`.
