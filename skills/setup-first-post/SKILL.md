---
name: setup-first-post
description: The quick-win post during setup. Before any interview, turns what the person already has (an old post, a talk, a call transcript, a voice memo, notes) into a strong LinkedIn post, so they see what the studio does before they give it hours of interviews. Runs /post (skills/job-post) with the setup framing and records the result in setup-progress. Use when /start reaches the first-post quick win, or when someone says "write a post from this" or "try it on this" during setup.
---

# The first post, from what they already have

The point is a real post on day one, from their own material. The post itself is made by `skills/job-post`; read that file and run it. This file adds only what setup needs around it.

## Tell them what and why

Before any step that needs the person, say what's about to happen and why (CLAUDE.md rule 7; the words for setup are in `skills/setup-start`).

## What's different from a plain /post

- **The piece folder** is `pieces/<yyyy-mm-dd>-first-post/`, with `quick_start: true` as well as `path: direct` in the brief's frontmatter.
- **The material** is whatever is in `inbox/` and `material/` (run `python3 scripts/inbox-to-text.py` first). If both are empty, ask for one thing: "Paste or drop in something you've already made: a post, a talk, notes from a call. The rougher the better."
- **Purpose and reader** come from `canon/strategy/outcomes.md` and `config/intake.yaml` when the intake ran; otherwise ask once, as `job-post` says.
- **The judge** is the `judge` agent with `templates/piece/review-direct.md`, as for any direct piece, run in the foreground. The first post runs inside `/start`, so the setup step after it waits until the post is shown, and the post never lands in the middle of the next step's questions (`CLAUDE.md` rule 9).
- **Questions in the moves step:** the moves stage's budget, plus any fact the post can't be written without. This is the quick version; the plan `/post` shows before drafting (the idea, its shape, the opening) is usually the one question worth asking.
- **The picture:** when Figma is connected, run `skills/job-visual` on the passed draft and show it. Without Figma, describe the picture in two lines and say the visual kit arrives with the Figma quick win.
- **When you show it,** the third of the three lines is what the interviews add: the studio will know what they believe and how they talk, so it stops guessing from one file.

## After the post

In `canon/setup-progress.md`, write `- [x] First post from their own material: drafted <date>, waiting on their call` (it becomes `shipped <date>` when the producer records the ship), and set `first_post_reminders: 0` in the frontmatter.

## Rules

Everything in `skills/job-post` holds: facts only from the material, the stages and the three contexts, no writing to `canon/`, one post per run.

## Studio notes

When this skill made you guess, write one line per guess to `studio-notes.md`.
