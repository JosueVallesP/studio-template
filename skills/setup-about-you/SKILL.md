---
name: setup-about-you
description: >-
  One page about the person, written from their own material and their intake answers, that they can paste into any AI (Claude, ChatGPT, Gemini, whatever they use) so it stops starting from zero. Nothing in it is invented; every line comes from what they said or wrote, and what the studio read rather than confirmed is marked as such. Rewritten on request as the canon grows. Use for /about, "write my one-pager", "the page about me", "something I can paste into ChatGPT", and offered once by /start at the end of setup.
---

# About you, on one page

Every AI a person uses starts from zero about them. This page fixes that on day one: who they are, what they do and for whom, what they keep saying, how they sound, what they're working toward, and what never to say about them. It's portable on purpose: plain text, no studio terms, pasted at the top of any conversation anywhere. For a person who never does the interviews, it's the most useful thing the studio makes. For one who does, it gets sharper every time it's rewritten from what the interviews confirmed. The interviews don't read it.

## What it reads

`config/intake.yaml` (the facts: name, what they do, where they publish, the goal, hours), `canon/strategy/outcomes.md`, everything in `material/` and `inbox/` (run `python3 scripts/inbox-to-text.py` first), `bank/map/map.json` if it exists (or `canon/readback.md` in an older studio), and the canon's confirmed entries if any exist (then the page is written from those first and the material second). The page can be made with intake alone; it's thin, and it says so.

## What's on the page

In this order, in plain words, under these headings, each kept to a few lines. Leave a heading out rather than pad it.

1. **Who I am.** Name, what they do, for whom, where they're based if they said. One or two sentences, from intake.
2. **What I'm working toward.** The year-from-now goal in their words, and what they publish and where. From intake and `outcomes.md`.
3. **What I keep saying.** Three to six beliefs, each in one sentence, each with the person's own line under it in quotes. When the map exists, take them from its claims, the spine first, with the quotes it gives, and say which ones the person confirmed in its review. Otherwise read them from the material with the map's threshold (`skills/job-map/references/reading.md`): a belief the person has stated in two separate pieces, or once as a rule with a reason. Marked at the top of the section: "Read from my own writing; not all confirmed yet." After the interviews, only confirmed POVs go here and the mark comes off.
4. **How I talk.** Three to five short lines quoted from their own writing that sound most like them, and two or three plain rules the material shows (short sentences, no jargon, says "clients" not "customers"). No rule the material doesn't show.
5. **What I've done.** Two to four results, cases or stories with a number or a name, from the material, one line each. Only what's there; a page with none says "add two results you're proud of".
6. **Never.** Words they don't use, things they refuse to be paired with, claims they'd never make, from the material and intake. Short.
7. **How to work with me.** Two or three lines for the AI reading this page: ask before assuming, keep my words, don't make up stories or numbers about me, and (if the material shows it) the language to write in.

Then, under a line, the paste block: the same page as one plain-text block with no headings beyond bold lines, no markdown tables, no IDs, no file names, ready to paste into any assistant. The studio terms (canon, brand tree, POV) never appear on the page.

## Procedure

1. Read the inputs. Keep a scratch list: for each candidate line, where it came from (file and quoted words, or `intake`).
2. Write `canon/about-you.md`: the seven sections, then the paste block. Every line in sections 3 to 6 traces to a quote or an intake field; a line you can't trace is cut. Mark section 3 as read-not-confirmed unless the canon is confirmed.
3. Show the person the page in the chat, then ask one question: "Anything here that's wrong, or that you'd never say?" Fix what they say, in their words (CLAUDE.md rule 3 for a half-formed correction). Don't ask them to confirm every line; the interviews do that.
4. Say in two lines what it's for: paste it at the top of any AI conversation and the AI stops starting from zero; the studio rewrites it as it learns more ("/about" any time). Write one line in the log of `canon/setup-progress.md` if the file exists.
5. On a later `/about`: reread the inputs including the confirmed canon, rewrite the page, show a short diff in words ("three beliefs are confirmed now; two new results; the voice rules come from your voice guide"), and ask the same one question.

## Rules

- Nothing invented. Every line in sections 3 to 6 traces to the person's words. Section 7 is the studio's, and it's the same for everyone except the language line.
- Beliefs the studio read but the person hasn't confirmed are marked as such, every time, until confirmed. Never present a read belief as a confirmed one.
- No studio words on the page. It leaves the studio; it has to make sense in ChatGPT.
- One page. If the material would fill three, the page holds the strongest; the canon holds the rest.
- This page never feeds the writer by itself; the writer reads the canon and the material. The page is for the person and for other AIs.
- `canon/about-you.md` is person-owned. An update never touches it.

## Studio notes

When this skill made you guess, write one line per guess to `studio-notes.md`: the date, the skill, what was unclear.
