---
name: setup-libraries
description: Shows a person the libraries their studio came with, one of the quick wins before the interviews. The LinkedIn library (real posts sorted by the job each hook and body does), the Substack library (real essays sorted the same way) and the visual moves (proven ways to draw an idea, drawn in their Figma kit). It doesn't recite the libraries; it picks the few moves their own material can carry today, shows each with a real example, and tells them how the studio uses the rest. Use when someone says "/libraries", "show me the libraries", "what's in the library", "what did I get", or when it is the next quick win in /start.
---

# Show the libraries

Every studio ships with the same three libraries. They live in the studio's own folders, so every person has them from the first day and gets each new version with the next update:

- **LinkedIn library**, `skills/fmt-linkedin-post/library/`: 57 idea briefs (`idea-briefs.md`, `briefs/`), each naming the idea under a group of posts and what a person needs to write their own; the posts themselves (`posts/`), every post sorted by its hook move, structure and close (`content-moves-sorted.csv`), and the move cards (`hook-moves.md`, `body-moves.md`).
- **Substack library**, `skills/fmt-substack-essay/library/`: the essays (`essays/`), every essay sorted by its title, subtitle and opening moves (`essays-sorted.csv`), and the move cards (`hook-moves.md`, `body-moves.md`).
- **Visual moves**, `skills/fmt-post-visual/library/visual-moves.md`: the proven ways to draw an idea, each drawn once on the Moves page of their Figma kit.

A move is the job a piece does for the reader, not a sentence to fill in. That is the one idea the person should leave with: the studio doesn't hand them templates, it reads what they have and picks the move that material can carry.

## Tell them what and why

Before you start, say it in plain words (CLAUDE.md rule 7): "Your studio came with three libraries: real LinkedIn posts, real Substack essays and proven ways to draw an idea, all sorted by the job each one does for the reader. I'll show you the few that fit what you already have, so you can see what the studio builds with. About ten minutes, and you don't have to do anything."

## What you need

- `config/tools.md`: which channels they publish on, and whether Figma is connected (`library file`).
- What you know about them so far: `config/intake.yaml`, `material/`, `inbox/`, and `canon/` if anything is confirmed.
- The three libraries above.

## Procedure

1. **Count, don't remember.** Count the posts in `posts/`, the essays in `essays/`, and the move cards in each moves file (each card is a `## ` heading with a number). Say the counts. Never quote a number from this file or from memory; the libraries grow.
2. **Pick for them.** Read their material and intake. For each hook move, read "What it needs" and check whether they have that raw material today (a result with numbers, a long practice, a story with a turn, a strong opinion, a client case). Keep the three moves their material can carry best. If their material is thin, pick the moves that need the least (an opinion, a lesson from their work) and say so. Never show a move as theirs when they don't have what it needs.
3. **LinkedIn**, if they publish there. For each of the three moves, in a few lines: the move's name and its job in plain words; one real opening from the library with its ID, short enough to read at a glance; and one sentence naming the thing in their own material that could carry it ("your 40 client audits are the proof this one needs"). Then one body move that fits the same material, the same way.
4. **Substack**, if they publish there. Two moves the same way: one title or opening move, one body move, each with a real essay from the library (its title and author) and what in their material fits it.
5. **Visual moves.** Pick two or three moves that fit ideas in their material (a before and after, steps in order, two things that overlap). If Figma is connected, take a screenshot of each on the Moves page of their copy, in the Brand mode when their brand is applied. A kit duplicated before late October 2026 may lack moves V18 to V22; when one you picked isn't on their Moves page, say it's on the master kit and that a fresh duplicate carries it. If it isn't, describe each in one line and say "set up my Figma" puts them in front of them. Say once that the studio starts from the idea's shape and draws from the parts, so the drawings are examples, not forms.
6. **How they use it.** In three short lines: they never have to open these folders, because `/post`, `/essay` and `/visual` pick the move from what they hand over; they can ask "show me posts that open like this", "which moves fit this material" or "/teardown" on any post they like, and new moves they find can be added; and the folders are there if they're curious (name them in plain words, not paths).
7. **Close.** Offer the next quick win in one line, the first post, and say it will use one of the moves you just showed them. Tick `- [x] The libraries: done <date>` in `canon/setup-progress.md`, and add a dated line to its log.

## Rules

- Show a handful, never the whole library. The point is "this is what the studio builds with, and here's what fits you", not a catalogue.
- Every example is a real one from the library, with its ID. Never write a new example and present it as from the library.
- Never say a move suits them for a reason they didn't give you. The fit comes from their material, quoted or named.
- The libraries belong to the studio. Never add a person's facts to them; their own posts go in `material/`.
- Never write facts about a person into this skill.

## Studio notes

When this skill made you guess, write one line per guess to `studio-notes.md`.
