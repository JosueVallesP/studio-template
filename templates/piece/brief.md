---
id: <yyyy-mm-dd-slug>
status: briefed
format: <format skill name, e.g. fmt-linkedin-post or fmt-substack-essay>
channel: <linkedin / newsletter / …, a file in canon/strategy/channels/; for format: craft-sales-copy, one of page / email / linkedin-dm / pamphlet>
visual: <yes / no; whether this piece gets a visual, from the channel file or the person; /visual reads it>
layer: <stories / POVs / branches / proof / thesis, the layer this piece fills in the content plan's mix>
parent: <ID of the branch, POV or value this grows from, when the canon has one; otherwise `none (direct)`>
seed: <the idea bank entry (I ID) this piece grows from; see the idea bank template for the seed record>
sources: <other canon IDs it draws on>
segment: <G ID>
desire: <D ID>
path: direct  (every piece since 0.90; `pipeline` on a piece from before it)
written_by: <blank when the studio drafts it; `the person` when the person wrote draft-v1 themselves and brought it to /refine: one draft under `## Post`, their lines marked `verbatim` with `supplied` in the source map, and the judge reads every line as theirs>
thinks_out_loud: no
adapted_from: <piece ID when /adapt made this from another piece; blank otherwise>
kind: <test / cornerstone; craft-refine decides how far the piece is pushed. Most posts are test; the manifesto, a key essay, a page or a talk are cornerstone. The person can change it with a word>
scheduled: <yyyy-mm-dd when the person has picked a day to publish; blank until then. /status shows the next seven days; /review sets it with "queue it for <day>">
---
# Brief

`/post`, `/essay` or a selling tool writes this as the stops go, and the format skill fills the format plan. The person's yes at each stop is the approval; there's no separate one. Every section answers a plain question, and the sources beside the answers let the judge check where each claim came from.

## The one idea
What should a reader be able to repeat to a friend?

<One sentence.>

## Fractal shape
- Claim: <…>
- Why it's true: <…, with its ID; or `writer: <the premise the writer will argue>` when the canon holds no why>
- Evidence: <idea bank or canon IDs; facts always need one>
- What it changes for the reader: <…>

## The reader
Who is this for, and what do they already feel?

- One real reader: <a person, not a segment: named, or described by what they do and what they believe now; where they came from (said today, a question, a client, the audience file)>
- Segment: <G ID and one line>
- Desire: <D ID>, with WILL "<quote>" and WON'T "<quote, confirmed only>"
- The problem they already feel, in their words: "<…>"

## Purpose
What is this piece for: trust, leads, reach, a point of view, recruiting, relationships?

<One line, from the content plan's layer mix, or the list of what's ready to harvest.>

## Material
What real material does it use? Nothing here may be invented.

**The scene rule.** The piece stands on at least one concrete thing: a scene of the person's (an S or R entry, a captured moment, a number) or a `borrowed: verify` case named here. The person's earlier sentences alone don't count.

- <SLOT> <source>: "<words>"

The source is a canon or bank ID, a file and quote (`material/<file>: "..."`), `said today`, or `borrowed: <source>`. `writer` is never a material line; the writer's own reasoning goes in the draft.

Kinds (slots): for `fmt-linkedin-post`, RESULT, METHOD, STORY, DOCUMENT, OPINION, PATTERN, BORROWED, NEWS, DATA, EXPERIMENT, ADMISSION, LINE, LAUNCH. For `fmt-substack-essay`, the same where they apply, plus IDEA, MODEL, CASE, SOURCE, TERM, CHANGED, OBJECTIONS, OCCASION.

## Outcome
What should the one real reader think, feel or do afterward? The job the piece has to get done; the judge reads the draft against it.

<…>

## Not saying
What does this piece leave out, to keep scope and nuance?

<…>

## Call to action
<C ID, or none.>

## Open questions
What would the person's answers improve? With status `briefed`, the writer can draft without them; with status `blocked`, nothing moves until they're answered.

<…>

## Format plan
Filled by the format skill named above. For `fmt-linkedin-post`:

```
GIVES           do, see, believe or direction, and at what level
READER NOW      what the reader believes or does about this today, and whether they'd push back
QUESTIONS       the reader's questions in order, numbered; each is one beat
SHAPE           code and name, from the questions; the runner-up if there was one
LENGTH          in plain words, from the beats; a guide, never a target
TYPE            the post type and its path, or none
TYPE NOTES      what the type's checks need on record, or none: the clock word and the shelf life it buys (newsjacking), the permission, what can be named and published (proof post), "lead capture" for a contents page (simple listicle)
HOOK MOVE       number and name, why it's available, how it opens this shape and what it buys
OPENING         the opening the person picked, as they saw it or rewrote it (direct path); otherwise none
SECONDARY MOVE  if any
PAIRING         common, or why this idea needs an uncommon pair
INSIDE MOVES    per beat, where a beat has one
CLOSE           which one, and why
EXAMPLES        IDs of the pulled posts, each hook line as the CSV holds it
WATCH FOR       the "how it fails" items this material is closest to tripping
```

For `fmt-substack-essay`:

```
IDEA            the one idea, one sentence, with its POV or branch ID, or on a direct piece the stage 1 point or the quoted line
READER NOW      what the reader believes or does about this today, and whether they'd push back
QUESTIONS       the reader's questions in order, numbered; each is a section or part of one
STRUCTURE       code and name, why it's available, the runner-up
TITLE MOVE      code and name, why it's available and what it buys
SUBTITLE JOB    code and name, what the title leaves unsure
OPENING MOVE    code and name; the promise the opening ends on
OPENING         the title and opening lines the person picked, or none
SECTIONS        numbered, each with the question it answers, its job and the material ID it uses
INSIDE MOVES    the ones the structure needs, plus the long-form holding moves
CLOSE           which one, and why
LENGTH          in plain words, from the sections; a guide, never a target
ACCESS          free, or paid with the paywall's place named
EXAMPLES        IDs of the pulled essays, each title as the CSV holds it
WATCH FOR       the "how it fails" items this material is closest to tripping
```
