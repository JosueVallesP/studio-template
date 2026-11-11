# Bank format

The tense bank is one markdown file, `bank/tenses.md`, owned by the person like the rest of `bank/`. Both the person and the studio read it, so keep it plain.

## Rules

- **Only what the person said.** Every line comes from their answers, their files or a draft they wrote. No inferences, and no polishing their story into something it wasn't. Keep their wording; when an answer was a half-thought and they took a sharper version, keep both, the raw words first (`CLAUDE.md` rule 3).
- **Say where it came from.** Each bridge names its source: `/three-tenses <date>`, a file in `material/`, or a piece ID.
- **Date everything.** Each bridge gets the date it was added. Each Future end gets its own date, because that's the part that goes stale.
- **One bridge per thread.** If a new answer extends an existing bridge, update that bridge instead of adding a duplicate.
- **Mark ideas, don't delete them.** When the person picks an idea it becomes an idea bank entry and gets `picked <date>, I<n>`; when it ships, the piece goes under Posted. A used idea can come back later from another angle.
- **Edit in place.** Use small edits rather than rewriting the whole file, so nothing the person added by hand gets lost.

## Structure

```markdown
---
doc: tenses
layer: bank
owner: <person's name>
---
# Tense bank

Last updated: <date>

## Snapshot
- Then: <one line on who they were, in their words>
- Now: <one line on who they are>
- Future: <one line on who they're becoming>

## People

### <short name for the bridge>
Added: <date> · source: <where it came from>
- Then: <the moment, with specifics>
- Now: <what it looks like today>
- Future (<date>): <where it's heading, and the next step>

Ideas:
- [Then/Now] <the point the post would make> | first line: "<plain first line>"
- [Now/Future] <the point> | first line: "<plain first line>"

## Tools
...

## Process
...

## Projects
...

## Beliefs
...

## Loose ends
- [Then] <topic> | <a story that hasn't connected to anything yet> (<date>)
- [Future] <topic> | <a plan with no past or present link yet> (<date>)

## Posted
- <date> | <bridge name> | <overlap> | <piece ID or first line>
```

## The snapshot

The three-line snapshot at the top is the person's brand in its simplest form: where they came from, where they are, where they're going. Fill it after the first few bridges, in their words. A good snapshot reads like one sentence split in three ("Ex-lawyer, now building my writing career, growing my newsletter to 100,000 readers"). Update it when the Future line changes. When the canon has a core summary (`canon/core-summary.md`) and the snapshot says something it doesn't, that's a proposal of kind `seen`, not an edit.

## Idea lines

Each idea is one line with three parts:

1. The overlap tag: `[Then/Now]`, `[Now/Future]`, or now and then a single tense.
2. The point the post would make, in a plain sentence.
3. A first line, written the way the person would say it. It's a starting point for `/post`, not a finished hook.
