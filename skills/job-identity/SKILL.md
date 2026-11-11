---
name: job-identity
description: >-
  A person's visual identity from one command, built on the genius of contradiction: the two opposite sides of them that are already true, whose collision produces what they want to be known for. Takes its facts from the strategy, the material and a short conversation instead of waiting for a confirmed canon; writes the contradiction brief and the design system, and applies them to the Figma visual kit. Use for /identity, "build my look", "my visual identity", "make it look like me", "genius of contradiction".
---

# /identity

`setup-visual-identity` builds a person's look after the interviews and the strategy, from the canon. This skill builds it from what's there now: the strategy if `/strategy` or `strategy-brand` wrote one, the person's material, and a short conversation. The method is the same (`skills/craft-contradiction`, with `skills/craft-visual-philosophy` for the marks); only the inputs move.

## Two modes

- **The strategy is confirmed and the canon holds the values and stories:** run `skills/setup-visual-identity` as written.
- **Otherwise:** the short version below. Say which, in one line.

## The short version

### Get the facts

`craft-contradiction` step 1 needs: what the brand is, who it's for, where it came from, what it wants to be known for, and what it must never be paired with. Read first:

- `canon/strategy/brand-strategy.md` if `/strategy` wrote one: the target association, the anti-associations, the character sheet. Use them as written.
- `material/`: how they write and what they keep coming back to; the sides of them that show up on the page.
- `canon/visual/brand-assets.md` or the intake: what exists visually today (logo, colors, fonts), and whether they want to keep it or build from scratch.

Then ask only for what's missing, in plain words, one question at a time. The method's own questions in step 1 are the list; most people need three or four of them. Ask also what they can't stand looking like, and which brands they sit next to (the room the look has to stand out in).

### Run the method

Steps 2 to 8 of `skills/craft-contradiction`, as written: the associations, the tensions that are already true, the collision test, the ratio, the visual codes for each side, where they clash, the test. Don't invent a side. A contradiction that isn't true of the person is decoration, and the test in step 8 catches it when the person says "that's not me".

Write the Contradiction Brief. Then run `skills/craft-visual-philosophy` on the brief's central idea to find the identity's one mark or mechanic, the thing every visual carries.

### Write it down and apply it

- The Contradiction Brief, saved where `craft-contradiction` says ("In the studio"), and `canon/visual/design-system.md` from `skills/setup-visual-identity/templates/design-system.md`, `status: draft` with `source: /identity, <date>`. Type, color, the marks, the ratio, what the style never does.
- Before applying anything, show the design system and ask for the yes on it. A yes in this session confirms it (`CLAUDE.md` rule 2): set `status: confirmed` and add `confirmed in /identity <date>` to its log. `setup-figma` applies only a confirmed design system, so without the yes the kit stays as it is and the design system waits as a draft.
- When Figma is connected (`config/tools.md`) and the design system is confirmed: apply it to the person's visual kit as `setup-visual-identity` says (the Style variables' Brand mode, the plates, the placements). Show three frames from the kit in the new look before touching the rest, and get the yes.
- When Figma isn't connected: show the brief and the design system, say the kit is where it gets applied, and point to `setup-figma`.

### Show it

The contradiction in one sentence ("you're a tax lawyer who writes like a stand-up comic, and the look is a ledger with one line out of place"), the two sides and their codes, the ratio, and three frames. Ask what's true and what isn't; the person's "that's not me" is the method's test, not an objection to argue with. Then the next step in their words: `/visual` for the first picture in the new look.

## Never

- Never invent a side of the person. Both sides come from the strategy, the material or what they said.
- Never build the look from taste alone. The contradiction is the reason for every choice, and the brief says so.
- Never overwrite a look the person said they want to keep; tune it, and say what you changed and why.
- Never write facts about the person into this skill.

## Studio notes

When this skill made you guess, write one line per guess to `studio-notes.md`.
