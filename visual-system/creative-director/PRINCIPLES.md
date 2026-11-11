# Principles

These are the ideas the whole repo rests on. When a skill, rule or persona seems to conflict with one of them, the principle wins and the file gets fixed.

## 1. The repo is the frame. A person is the framer.

Dan Shipper's essay "After Automation" (Every, May 21, 2026) makes a point this repo is built around: a model can climb any frame you give it, but it can't be the one who decides what the frame should be. He calls it "the frame is not the framer."

For us, the frame is everything in this repo: the interview, the rules, the reviewer personas, the brand folder. The framer is a person: Josué, or whoever runs the studio, plus the client whose brand it is. Concretely:

- **A person sits at both ends of every piece of work.** Kieran Klaassen at Every calls this the human sandwich: people are the bread on either end of the agent's work. A person starts it (intake, the visual brief) and a person finishes it (approving direction, promoting a piece to canon). The agent does the middle.
- **The agent never approves its own direction.** `cd-direction` proposes; a person signs off. `cd-learn` proposes rule changes; a person accepts them.
- **The canon is a person's call.** A piece goes into `canon/` only when a person says so. The agent can do the copying when asked, but the decision is never the agent's, because the canon is what "right" looks like for a brand.

## 2. Generic means visible sameness

The same essay defines slop as "visible sameness, repeated ad nauseam," and not any one tell. That matters for how we catch generic work:

- The generic detector asks "would this look at home in anyone's feed?" before it checks any list of tells.
- `taste/rules/generic-tells.md` is a starting list, and it goes stale. Every time models get better, yesterday's distinctive look becomes today's default. `cd-learn` refreshes it from real rejections.
- A brand can't be distinctive by borrowing someone else's distinctiveness. The reference library shows what a look signals; it never supplies the look.

## 3. Quality comes from the frame, so spend effort on the frame

The essay points out how much "smuggled intelligence" sits inside a good prompt: the human judgment that frames the task before the model starts. The same is true here. A thin brief gets a polished but interchangeable brand.

- `cd-intake` and `cd-direction` get the most care, the best model and the most time.
- When output is weak, fix the brief, the direction or a rule first. Don't add a tool.

## 4. Difference comes from the person's live situation

Models know the work that has already been done. A person knows what is true about them right now: what they believe, what they've built, what they're fighting for. That's the only reliable source of a brand nobody else has.

- Every side of a contradiction, every association and every visual code needs evidence from the person's own life or work. If there's no evidence, it's a costume.
- References a client likes are inputs to judge, not a style to copy.

## 5. Agent-native by default

From Every's [Agent-native Architectures](https://every.to/guides/agent-native) guide:

- **Parity.** Anything you can do to a brand (edit a rule, swap a reference, promote a piece, change the mode, archive it) the agent can do through the same files when you ask. The "Brand admin" table in `AGENTS.md` lists how.
- **Granularity.** The repo adds no tools of its own. Skills are prompts that combine file reads and writes with each connector's own tools. Judgment lives in prompts and rule files, never inside a tool.
- **Composability.** A new kind of piece (a one-sheet, a book cover, a booth) needs no new skill. `cd-make` reads the brand and picks a tool.
- **Emergent capability.** The test for every change: ask for something no skill was built for, and check the agent can still get there.
- **Improvement over time.** Every yes and no lands in `log.md`; `cd-learn` turns the ones that matter into lessons and rule edits.

## 6. The writing rules apply to everything

Every word this repo writes, to the studio owner, to a client, or onto a visual, follows `taste/rules/copy-on-visuals.md`. That includes interview questions, briefs, review findings and headlines. The rules apply to anything sold from this repo too.
