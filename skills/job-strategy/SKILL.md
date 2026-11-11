---
name: job-strategy
description: >-
  A person's content strategy from one command, in one sitting: what to be known for, who to, on which channels, in what shape, how often, and why. Reads their material and asks the few questions the method needs, instead of waiting for the full interviews and a confirmed canon. Writes the same strategy files strategy-brand writes, as drafts the interviews later sharpen. Use for /strategy, "build my strategy", "what should I post and how often", "my content strategy", and to revise the strategy later.
---

# /strategy

The strategy is the part of the studio that decides what the content is for. Without it, every post is a guess. `strategy-brand` builds it from a confirmed canon, after the interviews, and that's the best version. But a person shouldn't have to do hours of interviews to get a strategy they can act on this week. This skill builds a first one in one sitting, from their material and a short conversation, writes it to the same files, and marks it as what it is: a draft the interviews sharpen.

The method is the same. Read `docs/strategy-method.md` sections 2 to 7 once, and keep `skills/strategy-brand/references/routes.md` and `references/rules.md` open. What changes is where the inputs come from.

## Two modes

- **The canon is confirmed** (the minimum in `canon/progress.md` is ticked): run `skills/strategy-brand` as written. It has everything it needs and the IDs to cite. This skill adds nothing.
- **The canon is thin or empty**: run the short version below. Everything the method needs comes from `material/`, the intake, and the person, in the chat.

Say which mode you're in, in one line, before starting.

## The short version

### What you read first

- `material/` and `inbox/` (run `python3 scripts/inbox-to-text.py` first): their posts, essays, transcripts. You're reading for four things: what they keep coming back to (the branches), what they've done for whom and with what result (the proof), the opinions they state that others would push back on (the POVs), and how they talk (the voice).
- `canon/strategy/outcomes.md` and `config/intake.yaml`, if the intake ran: the goal, where they publish, the hours.
- `canon/vehicle/vehicle.md` and whatever else in `canon/` is confirmed. Draft entries count only if the person confirms them now.
- `config/tools.md` for the channels they use.

Write down, before asking anything, what the material already answers. Then ask only about the gaps.

### What you ask

In the chat, one question at a time, in plain words, with what you already found stated first so they correct it rather than start from nothing. One question is one thing the person has to decide. The method needs these answers; the material usually gives about half.

1. **The goal.** What should the content lead to, a year from now? (Clients for a practice, pipeline for a company, buyers for a course or a book, a role or investors, or something else.) This picks the route.
2. **The reader.** Who is the one person this is for: title, company size and stage, situation.
3. **The three gates**, one at a time: Have you been in this reader's situation, or done the thing they want done, for people like them, enough times to see a pattern? Then: where does this reader read? Then: will they pay for what you offer, and who sends them to you?
4. **Known for.** When a client recommends you to someone, what do they say you do? In their words. If the material shows something different from what they say, show both and ask which is true.
5. **Never paired with.** Ask about an event: "Tell me about a time a reader or a lead came to you for the wrong thing. What had they read or heard that made them think you did that?" Or: "When did you last see someone in your field post something you'd never want your name next to?" The anti-associations come from the answers.
6. **What you've done.** The two or three results, cases or stories with a number or a name that prove the "known for". Point to the ones you found in the material and ask for what's missing.
7. **Your opinions about your field.** Show the ones found in the material first, each with the lines it came from. Then, for more, ask about an event, never for the opinion itself: "What's the last thing you had to un-teach a client?" or "Tell me about a project that went well for a reason you didn't expect." (`skills/setup-brand-tree/interviews/povs.md` has the rest.)
8. **Capacity and team.** Hours a week, who else touches the content, which channels they already have.

If the intake ran, the goal, the reader and capacity are mostly answered; confirm them in one line each.

The goal decides everything after it, so it gets the most care. Ask it the way `skills/craft-interview` says: know what they want before recommending anything (move 1); if the goal is a round number or a far date ("10k followers", "a year"), ask what it's for and what would change when they hit it (move 4); turn a hedged answer into a plain number and do the arithmetic against their hours and cadence (move 3); if they're torn between two routes, show both taken all the way and ask which comes first (move 7). This applies to a goal the intake already wrote too: confirming it in one line is enough when it's specific, and a round goal gets one move-4 question before you build on it. Stay inside the question budget.

### What you decide

Then work through the method's seven questions by following `skills/strategy-brand` steps 1 to 7 as written; that skill is the one place the method's steps live, so read it rather than working from a summary here. Write each answer with its reason. Where a step cites a canon ID this canon doesn't have, cite the material or the chat instead (see "What you write"). Two differences on the short version: a failed first gate (step 3) stops the strategy, and you say that the content can't carry a claim the person hasn't earned, and what would earn it; and a step that needs a confirmed entry the canon doesn't have yet works from what the person confirmed in this chat, marked as such.

### What you write

The same files `strategy-brand` writes, from the same templates in `skills/setup-brand-tree/templates/strategy/`, so the writer, the strategist and `/status` read them the same way:

- `canon/strategy/brand-strategy.md`, `status: draft`, with `source: /strategy, <date>` in the frontmatter.
- `canon/strategy/channels/<channel>.md`, one per channel with a job.
- `canon/strategy/content-plan.md`, this quarter.
- `canon/strategy/strategy-review.md`: the one-page summary for the person.

Where the template asks for a canon ID the canon doesn't have, cite the material (`material/talk-2025.md: "..."`) or `said in /strategy, <date>`. Where the person stated a belief, a story or a result in the chat, write it as a draft entry in the canon file, in their words, so the interviews confirm it later rather than ask again. The route is in `skills/setup-brand-tree/SKILL.md`, "Where a picked-up belief goes". Never mark it confirmed here.

### Show it and get the yes

Show `strategy-review.md`: the route and pace in a sentence, the target association and anti-associations, the character sheet, each channel's job and cadence in one line, the mix, the selling rule, the signals, the open questions. Every line with its reason in a few words, in plain words as `strategy-brand` step 8 says. Ask them to confirm, change or reject each part. The files stay `status: draft` (the interviews haven't confirmed the canon underneath), but add `person_confirmed: <date>` to the frontmatter of `brand-strategy.md` and `content-plan.md` (and of each channel file they said yes to) once they've said yes. A strategy counts as in use when its frontmatter has `person_confirmed:` or `status: confirmed`; this is the one definition (`skills/setup-start`, step 3). From then on `/post`, `/essay` and `/brief` read the strategy as the person's. When the minimum canon is confirmed later, `/start` offers `strategy-brand` to check this plan against it and set `status: confirmed`.

End with what the interviews add, in one line: the strategy now rests on what they told you in an hour; the brand tree checks it against what they actually believe and have done, and that's where it stops being a draft. Then the one next step in their words.

## Revising later

Each quarter, or when the signals say a choice was wrong, run again from "What you decide" step 6 with the shipped pieces and the signals in hand. Rewrite the content plan; touch the brand strategy only where the signals say so.

## Never

- Never invent a story, a number, a client, a belief or a quote. Every claim about the person cites the material, the canon or what they said in this chat.
- Never bend what they believe to fit the audience or the goal. If the goal needs a reputation their work can't support yet, say so.
- Never propose a wide, topic-popular content line to someone on route-clients or route-pipeline as a way to grow.
- Never propose paid promotion.
- Never set a cadence above what they said they can hold.
- Never mark a strategy section `confirmed`; only `strategy-brand`, after the interviews, does that. `person_confirmed` is the mark this skill leaves.
- Never write facts about the person into this skill.

## Studio notes

When this skill made you guess, write one line per guess to `studio-notes.md`.
