---
doc: ideas
layer: bank
version: 1
owner: <person's name>
---
# Idea bank

Raw captures, word for word. Capture writes them; the strategist reads the `ready` ones; the writer may use only what a brief cites. Summaries never replace the raw text.

Statuses: `raw` (captured, something missing) / `shaped` (`/shape` wrote the card and it waits for the person's yes; `/tidy` never archives it) / `ready` / `used` / `archived` / `merged into I<n>`. Only `ready` and `used` feed a piece. Status answers one question: can this feed a piece today?

Every entry the person planted (every type but `outside`) is also a seed, with a record of how it's growing. Outside entries are food for seeds, not seeds: they get no stage, and each names the seeds it feeds in `links`.

Stages, which the studio proposes and the person confirms (`next_stage` holds a proposal until they answer):

- `seed`: planted, not yet said in a sentence the person has confirmed.
- `sprouting`: the person has confirmed what it says (a translated line, a card, the point a piece makes). The studio brings the first wind here (below).
- `growing`: it has met pushback the person answered, or been fed something that holds up.
- `bearing`: it has shipped in at least one piece. It stays in the garden and can bear again.
- `resting`: the person chose to leave it for now. Nothing tends it, nothing archives it, until they wake it.
- `cut`: the person decided it doesn't hold. `/tidy` moves it to the archive, never deletes it.

**The first wind.** When a seed moves to `sprouting` with the person there, the studio asks it one real objection in the same moment, so an idea meets pushback when it's young instead of first meeting it inside a draft. One question, in plain words: the strongest case against the idea, and how would they answer it? Where the objection comes from, in this order: one a real person raised, from their files (a reader's question in `questions.md`, an `objection` entry, a client's pushback in a call); otherwise the strongest one the studio can build, said as the other side would say it (steelman it so its holders would agree with the wording), and named as the studio's, never put in a real person's mouth. Their answer goes in `pushback` in their words. "I don't know yet" is a fine answer: the line stays `open`, and `/scout I<n>` can look for a real opponent later. They can skip it; say once that the idea then meets its first objection in a draft or the weekly tending run. Never more than one objection per sprouting, and never during a guided flow that hasn't finished (`CLAUDE.md` rule 9): then it waits until the flow ends.

## I1 · <short title>
status: ready
raw: "<the capture, word for word: the transcript passage, the memo, the note>"
source: <call with <role>, 2026-10-14 / voice memo / interview <date> / forwarded email>
date: <date captured>
type: <story / POV / method / question / observation / objection / outside>; a result, a client, something said about the person and the rest of what builds trust go to `credibility.md`, paired here when the passage is both
links: <B, P, V IDs it belongs to, or none yet>
wanted_now: <yes when it fits one of this quarter's branches in the content plan>
who_said_it: <the person, or the role of whoever said it on a call: a client, a reader; never a name>
note: <optional one-line summary beside the raw text, never instead of it>
strength: <strong / maybe>
permission: <public / anonymize / private>
expires: <for outside material: use-by date>
also:
  - <date> · <source> · "<a later capture of the same idea, word for word>"
shape:
  gives: <do / see / believe / direction; written by /shape>
  level: <tactic / practice / principle / strategy>
  form: <the form it tends toward>
  move: <divide / contrast / reveal / transfer / name, and why>
  fails: <chain steps it fails, each with the question that fixes it; or none>
  translated: "<the idea said for the reader; waiting for the person's yes>"
  reader_belief: "<what the reader currently does or believes that this cuts against>"
stage: seed
next_stage: <a proposed stage and why, in one line, waiting for the person's yes; blank when nothing is proposed>
fed:
  - <I ID of an outside entry, or a canon story or proof ID> · <case / evidence / someone's idea it builds on / historical texture / story> · <one line on what it adds>
pushback:
  - <date> · <where it came from: a reader, a client, /scout I<n>, /shape, the judge, /think about> · "<the objection>" · <answer: "the person's words", or open>
fruit:
  - <piece ID> · <drafted / shipped <date>> · <one line on how it did, when anything came back>
became: <the POV, branch or method ID it grew into in the canon, or none yet>
tended: <the date the weekly tending run last brought this seed something; blank until then>
log: <date> captured
