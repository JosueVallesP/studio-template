---
name: setup-figma
description: Gives a person their own visual kit in Figma, one of the quick wins before the interviews. They duplicate the studio's master kit with one click; this skill connects their copy, puts their brand on it when they already have one (colors into the Brand mode, fonts into the text styles, their name in the footers), and hands over the link. After the interviews, setup-visual-identity runs the brand step again with the identity built from their files. Use when someone says "set up my Figma", "set up my visual kit", "set up my templates", or when config/tools.md says Figma is wanted and not connected.
---

# Set up the visual kit in Figma

The visual kit is a duplicate of the master (`figma_master` and `figma_template_link` in `studio.manifest.yaml`). It is not a set of forms to fill in. The studio decides every picture from the idea first (`skills/craft-visual-philosophy`, then `skills/fmt-post-visual`), and the kit is what it builds with:

- **Kit**: the twelve marks from the moves library as components (dot, line, bar, box, circle, arrow, curve, field, figure, panel, label, symbol) plus the accent marker, and starter frames at 4:5, square and 1500x1800.
- **Moves (examples)**: the 22 moves and nineteen variants drawn once each, with a note under each on the job it does and the shape of idea it needs. They show how the parts go together; a picture for a real idea changes them or builds something new.
- **Plays**: one move drawn five ways, because most of the variety comes from plays, not from new layouts.
- **Carousel**: a six-slide set (cover, point, point, diagram, statement, end) in 4:5 and square, with page numbers, a progress bar and safe-area guides, exported as one PDF.
- **Field guide and plate**: the bigger single-frame formats.
- **LinkedIn placements** and **Substack placements**: every place their look shows up beyond posts, at the right size, with each platform's crop notes and a Guides layer to hide before export. LinkedIn: profile photo, profile banner, infographic portrait and square, newsletter or article cover, newsletter logo, link preview, company page logo and cover. Substack: publication logo, wordmark, welcome page cover, post featured image, email header banner, in-post image.
- **Brand**: swatches, type and the logo slot.

Every color is a variable in the "Style" collection and every piece of type uses one of seven text styles. Two modes: **Neutral** (black lines on white, one accent), where every picture is judged before the look can flatter it, and **Brand** (the person's look). Neutral never changes. Brand starts as a copy of Neutral.

You don't build a kit per person. A change to the kit is a change to the master, for everyone.

## What you need

- The Figma tools in this session (the person connected Figma in Claude's settings, under Connectors). To check, load them if they're listed but not loaded, and call Figma's `whoami`; a tool that is only named, or a call that fails, means not connected. When it isn't: write `- [ ] Visual kit in Figma: waiting on Connectors` in `canon/setup-progress.md`, say the one step in one sentence ("Connect Figma in Claude's settings, under Connectors, then say 'set up my Figma'"), say the studio describes pictures in words until then, and name the next quick win in one line.
- `config/tools.md`, section Figma.
- The brand, from `canon/visual/design-system.md` when it exists and is confirmed (a design system the person said yes to in this session counts: `/identity` marks it confirmed before handing over), otherwise `canon/visual/brand-assets.md` (intake). The files in `inbox/` named there (logo, brand guide).
- `references/apply-brand.js` and `references/footer-name.js` in this folder.

## Tell them what and why

Check the connection first ("What you need"). If Figma isn't connected, skip the promise and go straight to the one step. Otherwise: Before any step that needs the person, say what's about to happen and why (CLAUDE.md rule 7; the words for setup are in `skills/setup-start`).

## Procedure

1. **Check.** Read `config/tools.md`, Figma. If `wanted: no`, stop. If `library file` is set and `connected: yes`, skip to step 4 (this is a re-run, usually from `setup-visual-identity`).
2. **The person's one step.** Send them the link and say: open it, click the file name at the top, choose "Duplicate", then send back the link of the copy (it lands in their drafts; they can rename it). One message.
3. **Connect the copy.** Take the file key from their link. Read its pages and confirm these are there: Start here, Kit, Moves (examples), Plays, Carousel, Field guide and plate, LinkedIn placements, Substack placements, Brand; and that the "Style" collection has the Neutral and Brand modes. If not, it isn't a copy of the master; say so. Write to `config/tools.md` under Figma: `connected: yes`, `library file: <key>`, `file url: <their link>`.
4. **Their brand, if they have one.** Read the brand file. Decide which of their colors plays which role:
   - `paper`: the background. Their light neutral, or white.
   - `ink`: text and filled marks. Their dark neutral, or near-black.
   - `accent`: the one thing to look at. Their strongest brand color.
   - `accent-2`: only if the brand has a second color that is meant to be used.
   - Leave `line`, `muted` and `panel` empty unless the brand names them; the script derives them.
   Fonts: the heading font and the body font, by the family name Figma uses. One font in the brand means it goes in both. Never invent a color or a font they didn't give; an empty role keeps its neutral value.
   Tell the person the mapping in two lines ("your green is the accent, your cream is the background, Playfair for headlines, Source Sans for the rest") and run it. They can change it after they see it; changing it is a rerun of this step.
   Fill `BRAND` in `references/apply-brand.js` and run it on their file. It writes the Brand mode, swaps the fonts on the seven text styles, shows the Brand mode on every page with pictures on it and returns a report. If they gave a name, run `references/footer-name.js` once per page that says "Your name" (Moves (examples), Carousel, Field guide and plate, LinkedIn placements, Substack placements), one call per page. Leave the other placeholder lines (the banner line, the publication name) as they are: they need words the person hasn't confirmed yet, and `setup-visual-identity` fills them after the interviews.
   Read the report's warnings out plainly: a font Figma doesn't have (it has to be installed on their computer, or they pick a Google font close to it), text that won't read on the background, an accent too faint to see. Don't fix them silently.
   **If they have no brand,** skip this step. The kit stays neutral, which is a good place to start. Say that after the interviews the studio can build a look with them from what it learns (`setup-visual-identity`) and apply it here the same way.
5. **The logo.** If a logo file is in `inbox/` and it's an image, put it in the "Logo (paste yours here)" frame on the Brand page. Otherwise tell them that's where it goes.
6. **Show it.** Take a screenshot at feed size of three things in their look: the 2x2 from Moves, the carousel cover, and the LinkedIn profile banner (for the channels they use: the Substack featured image instead when Substack is their main channel). Ask one question: does this look like you? A no goes back to step 4 with what they said.
7. **Hand over**, in three lines: the link; that the Start here page explains the kit and every move has a note on what it's for; that they don't pick a template, they ask "what should the picture be for this post?" and the studio finds the idea's shape and offers three ways to draw it. Write the link into the "Your visual kit" row of `YOUR-STUDIO.md` and, if Notion is connected, into the "Your visual kit" callout on their Notion Home. In `config/tools.md` set `brand applied: yes (<date>, from brand-assets)` or `brand applied: no (neutral)`. Tick the Figma item in `canon/setup-progress.md` in the format `setup-start` sets: `- [x] Visual kit in Figma: done <date>`.

## Rules

- Never edit the Neutral mode in a person's copy.
- Never rename a page, a component, a text style or a variable; the designer and the scripts find them by name.
- Never add to the kit here. New marks and new moves go into the master and reach people through their next duplicate. Pictures for pieces get built on a "Pieces" page in the person's file.
- Never write facts about a person into this skill.

## Studio notes

When this skill made you guess, write one line per guess to `studio-notes.md`.
