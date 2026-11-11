---
name: job-recall
description: Finds what a person has said, written or shipped about a topic, across their material, their canon, their idea bank and their pieces, and hands it back in their own words with where each line came from. Use for /recall, "what have I said about X", "did I ever write about X", "find my story about X", "what do I believe about X".
---

# /recall

A body of material is only useful if you can find things in it. This skill answers one question: what has this person already said about X? It reads, quotes and cites. It doesn't write a post, doesn't interpret, and doesn't fill gaps.

## Where it looks

In this order, and all of them:

1. `material/`: their posts, essays, transcripts, stories, notes. The biggest source and usually the richest.
2. `canon/`: confirmed and draft entries (POVs, stories, proof, thesis, branches, values), each with its ID and status.
3. `bank/ideas.md`: captured entries from `/capture`, and `bank/credibility.md`: their results, clients and what people said about them.
4. `pieces/*/final.md` and the latest `draft-vN.md` of each piece: what shipped and what's in progress.
5. `inbox/` and `inbox/done/`: what came in and hasn't been sorted, or was.
6. `proposals.md`: what the crew thinks they said, waiting for their yes.
7. `journal/`: only entries whose frontmatter says `visibility: open` and that carry no `never:` line. A `private` entry is never opened, not even to search it (`skills/job-journal`).

Search with `grep -ril` for the topic and its obvious variants (singular and plural, the verb and the noun, the Spanish and English word when the material mixes languages), then read the matching passages, not just the matching lines. People rarely use the studio's word for their own subject ("pricing" may be "what I ask for", "fees" or "rates"), so also search their own terms for it: the vocabulary in `canon/voice/voice-guide.md`, the claim's other versions in `bank/map/map.json` when the map exists, and any term the canon entries on the topic use. A thin result doesn't prove they never said it.

## What it gives back

Grouped by where it came from, newest first within each group:

```
What you've said about <topic>

From your material (<n> places)
- <file> (<date if known>): "<the passage, in their words, trimmed to the part about the topic>"

In your canon
- <ID> · <kind> · <status>: "<the entry's quote or claim>"

Captured, not yet used
- <I ID> (<date>): "<quote>"

Shipped or in progress
- <piece ID> (<status>, <date>): "<the line or paragraph>"

Proposed, waiting on you
- <proposal heading>: "<proposal>"

You've said you no longer hold this
- <file or map claim> (<date>, dropped <date>): "<the passage>"
```

A passage that says a view the map marks `held before` (`bank/map/map.json`, a claim the person told the studio they've moved on from) goes under the last group, never with the rest, so they can see what they used to think without it reading as what they think now.

Leave out a group that has nothing in it. If nothing anywhere mentions the topic, say so in one line that names the words you searched ("Nothing under pricing, fees, rates or what I charge"), so they can give you theirs, and stop; don't offer what they might think. What the passages add up to is `/think`'s job, not this one's.

## Rules

- Quote; don't paraphrase. The point is their words.
- Every line carries its source. A passage with no file or ID isn't recalled; it's invented.
- Never write to any file. This is a read.
- Private material stays private. A private journal entry is never read, so it never shows up here. An open journal entry, or a bank line marked `permission: private` or `anonymize`, is shown to the person (it's theirs) with that flag beside it, so they don't put it in a post by mistake.

## Studio notes

When this skill made you guess, write one line per guess to `studio-notes.md`.
