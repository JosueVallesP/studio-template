# Fields: what every entry needs

Use this file to check each answer. Every field has a short description of what it holds and, where answers often go wrong, a weak example and a strong one. If an answer looks more like the weak example, follow up before you write it down.

The examples here show the level of detail you're after. They are not answers to suggest. Never offer an example as if it were the person's own view.

## Fields every entry has

These go on every entry in every canon file:

- **id:** a short ID (V1, A3, P4, B2, X5, S17, R2). Never reuse or renumber IDs. A retired entry keeps its ID with `status: retired`.
- **status:** draft, confirmed or retired. What feeds content: `CLAUDE.md` rule 2.
- **quote:** the person's own words, verbatim, even if messy.
- **sources:** where it came from: "session 2" or a file name and date. An entry with no source stays draft.
- **log:** one dated line per change, for example `2026-10-21 confirmed`. A confirmed entry the person rechecked and kept gets `<date> still true` (see "Still true" below), so the last `confirmed` or `still true` line is the date it was last known to be true.

**Still true.** People change their minds, and a confirmed belief keeps feeding pieces until someone asks. So a confirmed values, behaviors, POVs, philosophy, thesis or stop-list entry whose last `confirmed` or `still true` line is more than six months old (a starting default) is due a check. `strategy-brand` asks about at most two due entries at each quarterly review, the ones cited most in shipped pieces first (`pieces/index.md`, the source maps). It asks about events, never "do you still believe this?" (`skills/craft-interview`): "Since <month>, has anything happened in your work that made this less true, or more true?" Then: kept as is, log `<date> still true`; changed, keep their raw words and offer a sharper version beside them (`CLAUDE.md` rule 3), and write the change to `proposals.md` as a proposal of kind `change to <ID>`, `proposed_by: still true`, for their yes; no longer true, the same kind proposing `status: retired`. Nothing changes in the canon until they say yes (rule 6). A "not sure" waits one more quarter, logged as `<date> asked, not sure`.

Entries point to each other by ID only. Never restate one entry inside another.

---

## Values (V1, V2, V3)

- **Is:** what wins when two good things conflict. A ranking, not a list of virtues. Keep the list to one to three (a starting default: only values that win a conflict are visible to a reader).
- **Isn't:** a virtue everyone claims, a preference, a goal.
- **Evidence:** a choice that cost them something real and that they'd make again; anger, because people get angry when a value is broken.
- **Gate:** at least one costly choice behind it, told as a story, and the person recognizes it as theirs. The session: `../interviews/values.md`.

Values rarely change. Treat them as something to find in the person's past choices, not something to choose.

| Field | What it holds |
| --- | --- |
| name | A short name |
| claim | One sentence in their own words |
| beats | The other good thing it wins over |
| cost | What it has cost them, with a real example |
| limit | Where it stops: the cost at which they'd choose the other way, in their words ("if it meant losing more than one client a year"). Optional; when it's empty, a piece never states the value as having no limit ("I'd never...") |
| story | A story ID where they chose it under pressure |
| rank | 1, 2 or 3 |

**claim**

- Weak: "I value quality."
- Strong: "I'd rather miss a deadline than send something I'm embarrassed by."

**beats**

The thing it beats has to be good too. "Quality over laziness" tells a reader nothing, because nobody values laziness.

- Weak: "Honesty over lying."
- Strong: "Honesty over keeping the client happy in the moment."

**cost**

- Weak: "It takes more time."
- Strong: "I lost a retainer last year because I told a client their launch plan wouldn't work and they didn't want to hear it."

**If the list grows past three:** test whether the extras are behaviors (things they do), POVs (opinions about the field) or preferences (things they like). Ask: "If these two values conflicted, which would win?" The one that loses is probably not a core value.

---

## Behaviors (A1, A2…)

- **Is:** a repeated act or refusal that follows from a value, specific enough that someone could film it. Refusals count, and often say more than actions.
- **Isn't:** a trait ("I'm curious"), a one-off event (that's a story).
- **Evidence:** "every time"; rules they keep that nobody asked for; habits a colleague would find odd.
- **Gate:** it's observable, it repeats, and it ties to a value. The session: `../interviews/behaviors.md`.

Behaviors prove the values are real, and they're the main source of story-based content.

| Field | What it holds |
| --- | --- |
| behavior | What they do or refuse to do, stated so someone could watch it happen |
| type | action or refusal |
| from | The value ID it comes from |
| proof | A story or result with specifics: who, when, what happened, the result |
| public | yes, anonymize or private |

**behavior**

- Weak: "I'm very thorough with clients."
- Strong: "I read every document a client sends before our first call, even when it's a hundred pages."

**refusal**

- Weak: "I don't do things I don't believe in."
- Strong: "I won't sign off on a plan I think will fail, even when the client is paying for my approval."

---

## POVs (P1, P2…)

- **Is:** a claim about how something in their field works or should work, in three parts: the claim, the ground (what they saw that made them believe it) and the condition (when it's true).
- **Isn't:** a value (a value is about what matters; a POV is about how things work), a hot take (no ground), a fact (no reasonable peer could reject it).
- **Evidence:** the ground is what makes it theirs. POVs show up in moments they watched something work or fail for a reason others didn't expect.
- **Gate:** all three parts present, and a reasonable peer could reject the claim. The session: `../interviews/povs.md`.

POVs are what make content distinct.

| Field | What it holds |
| --- | --- |
| claim | One sentence, specific enough that a peer could disagree |
| rejects | The common view it argues against |
| ground | What they saw that made them believe it, in their words: a moment, a case, a pattern across clients |
| evidence | Story IDs, proof IDs, cases or data behind the ground |
| condition | When it's true, and so when it isn't |
| confidence | firm, forming or exploring |
| from | The value IDs it comes from. Empty until values are found; for a POV-first start that's a later session, so don't ask "which value is that from?" of someone with no values written down |
| rank | Order of importance among their POVs |

**claim**

The test: could a smart, reasonable person in their field disagree? If not, it's a truism, not a POV.

- Weak: "Leaders should communicate clearly."
- Strong: "Founders should stop running weekly all-hands meetings once the company passes 50 people, because by then they turn into performances instead of decisions."

**rejects**

- Weak: "Bad advice."
- Strong: "The common advice that more face time with the founder always builds culture."

**condition**

Every POV has a place where it stops being true. If they can't name one, they haven't thought it through yet: the POV stays `draft`, with confidence `forming`.

- Weak: "It always applies."
- Strong: "This doesn't hold during a crisis, when people need to hear from the founder directly and often."

**confidence**

- firm: they'd defend it in public today
- forming: they believe it but are still working out the reasons or limits
- exploring: they're testing the idea

Older files may say `reasoning` for the ground and `limits` for the condition; read them as the same fields.

Confidence is separate from status. A forming or exploring POV feeds a piece only as `CLAUDE.md` rule 2 says (`thinks_out_loud: yes`), and never as settled.

---

## Philosophy (no IDs)

- **Is:** the model underneath that explains why their POVs belong together: the one picture of how their world works that those beliefs come from.
- **Isn't:** a list of POVs, a mission statement.
- **Evidence:** a premise several POVs share without saying it.
- **Gate:** it explains at least three confirmed POVs (listed in its `explains` line), and the person says it's the thread. Whether any confirmed POV contradicts it is checked for the layer's done test, not the gate. The session: `../interviews/philosophy.md`; nobody is asked for it directly.

Write it as one plain sentence plus a short paragraph (half a page at most) that shows how each POV follows from it, in their words where possible.

Test it with four lenses. They are tests, not boxes to fill. A gap under one lens is a flag to look at, not a failure.

| Lens | The check | If there's a gap, ask about an event |
| --- | --- | --- |
| What's true (ontology) | What does the thread say is true about their world? | Usually answered by the thread itself |
| How we know (epistemology) | What counts as proof for them? | "Tell me about the moment you first saw this was true." |
| How to read it (hermeneutics) | How do they think people should read what happens in their field? | "Tell me about a success story in your field everyone gets wrong. What did they miss?" |
| What it's for (teleology) | What's the work for? | "Tell me about a piece of work you're proudest of. What did it change for someone?" |

- Weak: "I believe in helping people grow and reach their potential."
- Strong: one sentence naming the premise their POVs share ("trust comes from what you're willing to give up"), then a paragraph showing how each POV follows from it, how they came to see it (years of client work, a pattern they saw again and again), how they think people should read the signals in the field, and what they think the work is ultimately for.

---

## Thesis (T)

- **Is:** the one claim the whole body of work exists to prove; where the person layer (values, POVs, philosophy) meets the goal (what they need to be known for).
- **Isn't:** a tagline, a mission. A mission says what they do. A thesis says what they claim is true.
- **Evidence:** every POV supports it or branches from it; proving it would take years of work.
- **Gate:** traces to the philosophy and the goal, has its catalyst, and the person would put their name on it. The session: `../interviews/thesis.md`; the studio drafts it, nobody is asked for it directly.

It's the filter: an idea that doesn't connect to the thesis doesn't get made.

| Field | What it holds |
| --- | --- |
| claim | One sentence |
| from | The philosophy it rests on, the POV IDs it holds together, and the goal it serves |
| catalyst | What they saw that others didn't, when, and why it made them act, with a story ID |
| for | Who it's for |
| changes | What it changes for them |
| implies | What people should do differently if it's true |
| falsifier | What would prove it wrong |
| branches | The branch IDs that hold it up (at least 2) |

**claim**

- Weak: "I help people build their personal brands."
  (That's a description of a job, not a claim.)
- Strong: "Small manufacturers lose more money to slow quoting than to high costs, and fixing the quote process is the fastest way to grow margin."

**catalyst**

A thesis without its origin is harder to believe and harder to write about.

- Weak: "I've always been passionate about this."
- Strong: "In 2019 I sat in on quoting for three shops in one month, and all three lost jobs they'd already won on price because their quotes took two weeks."

**falsifier**

If nothing could prove it wrong, it's too vague to guide content.

- Weak: "Nothing, it's just true."
- Strong: "If manufacturers who cut quote time to a day saw no change in win rate or margin, I'd be wrong."

---

## Branches (B1, B2…)

Core ideas and frameworks: the dense ideas and methods that need a long piece to explain. Usually 3 to 7, ranked.

| Field | What it holds |
| --- | --- |
| name | What they call it |
| problem | The problem it solves, in one sentence |
| parts | Its parts or steps, and how they relate |
| origin | A story ID for where it came from |
| limits | Where it doesn't apply |
| visual | Its natural visual form, if any: 2x2, sequence, layers, cycle, Venn |
| mechanism | new, claimed or renamed (see below) |
| desires | The desire IDs it answers |
| terms | Key terms with plain definitions |
| links | The thesis, POV IDs and published pieces it connects to |
| rank | Order of importance |

**terms** matters more than it looks. If the person calls something a "quote cycle", the writer must never swap in "sales process" or "pipeline". Define each term in one plain sentence.

**mechanism** says why a reader should believe this branch will work when other things haven't. Each type is fine; the person should just know which one they have.

- new: it connects things nobody connected before
- claimed: something everyone in the field does, which the person names and talks about first
- renamed: a known method with a new name and a new story around it

- Weak: "My process for content."
- Strong: a named framework with four parts, what each part is, how they lead into each other, and where the framework doesn't fit.

---

## Stop list (X1, X2…)

Topics they won't talk about, claims they won't make, names they won't mention and words they won't use. AI drifts most where nothing tells it what's missing on purpose.

| Field | What it holds |
| --- | --- |
| item | The topic, claim, name or word |
| type | topic, claim, name or word |
| why | A short reason, in their words |

- Weak: "Nothing negative."
- Strong: "I won't share client revenue numbers, even anonymized, because my clients trust me with them."

At least 5 entries (the minimum canon's default, in `templates/progress.md`).

---

## Stories (S1, S2…)

Stories feed every other layer. Every value needs at least one, and so does every top POV.

| Field | What it holds |
| --- | --- |
| title | A short label |
| raw | The story in their words, as told |
| who | Who was involved |
| when | Roughly when |
| what | What happened |
| result | How it turned out |
| scene | Optional. Where they were, who was there, what they saw or heard at the turn, in their words from the interview. The only place a piece may take sensory detail from |
| thought_then | Optional. What went through their head at that moment, as they reported it. A piece never adds a thought they didn't report |
| told | `first-hand` (they were there) or `heard` (someone told them). A `heard` story is told as heard, never as witnessed |
| links | The value, behavior, POV or branch IDs it supports |
| permission | public, anonymize or private. Ask it as "with names, without names, or not at all" |

- Weak: "I once had a client who didn't listen and it went badly."
- Strong: a story with a rough date, a description of the client (named only with permission), what was said, what the person did, and what happened after.

---

## Proof (R1, R2…)

Results and numbers. Never invent or round them up.

| Field | What it holds |
| --- | --- |
| result | What happened, with the number if there is one |
| who | Client or project (with permission) |
| when | Date |
| links | Offer or branch IDs |
| permission | public, anonymize or private |

---

## Vehicle (O1…, C1…)

The business that the thesis proves. This changes with the business, so it's reviewed quarterly and kept apart from the person layer.

**The goal comes first.** The person layer says what they can honestly be known for. The goal says what they need to be known for. Brand strategy works backward from the goal.

| Field | What it holds |
| --- | --- |
| goal | What they want to have happen, in their own words, with a rough date |
| by | A rough date for the goal |
| known_for | What they need to be known for so that it happens |
| do | What they need to do to be known for that |
| learn | What they need to learn to do those things |
| business | What the business is, in one paragraph |
| offers (O1…) | For each offer: name, who it's for, the outcome, how it works, price if public, link, `status` (draft, confirmed or retired, like every entry) and `availability` (open, waitlist or closed). A new offer, or a price on a draft offer, is a draft O entry; a change to a confirmed O entry is a proposal (`change to <O ID>`), never a direct edit |
| proves | How the vehicle proves the thesis |
| proof | Proof IDs |
| priorities | Current priorities and launches, with dates |
| goals | This quarter's goals (the next steps toward the goal) and which offer content should support |
| calls to action (C1…) | The approved calls to action, word for word |

**goal**

- Weak: "Grow my business."
- Strong: "By the end of next year, I want three manufacturers a quarter coming to me without outreach, so I can stop doing cold calls."

---

## Brand strategy (G1…)

Who the content is for, what the brand is known for, where it shows up, and how a reader gets from a piece to a conversation.

| Field | What it holds |
| --- | --- |
| segments (G1…) | For each: their situation, what they already believe, what they want, and the words they use for their problem |
| relationships | Ideal clients, plus peers and connectors who send clients |
| not for | Who it's not for |
| target association | The first thing people should think of when they hear the person's name, said the way a client would say it |
| known for | The thesis said the way a reader would say it, plus the ranked branches |
| reputation checks | What a few clients, peers and connectors actually think of first, in their words, with the date asked |
| anti-associations | What the person must never be paired with, each linked to the stop list; required |
| route and pace | The route (route-clients, route-pipeline, route-buyers, route-role, route-referrals), and for route-clients the pace (clients soon, body of work first or a split), with the reason; filled by `strategy-brand` |
| character sheet | Credibility position, enemy, two or three value types, purpose level; filled by `strategy-brand` |
| channels | Each channel, primary or secondary, its job and cadence, pointing at its file in `strategy/channels/`; filled by `strategy-brand` |
| path | What a reader does next after a piece, and where |
| time horizon | When to judge, when it should work in a real way, review dates; filled by `strategy-brand` |

**segment words** must be the segment's own words, not the person's.

- Weak: "They need help with brand positioning."
- Strong: "We win the jobs we bid on, but we lose half of them before we even get the quote out."

**target association**

It has to be something the person layer can support and the goal needs. See the two-directions test in `tests.md`.

- Weak: "A trusted leader in manufacturing."
- Strong: "The person who gets your quotes out in a day."

**reputation checks**

The gap between the target association and what people actually say is what the content isn't doing yet. Record people's exact words, not a summary.

---

## Audience (D1, D2…)

Content can't make people care about a thesis. It can only connect the thesis to something readers already want. This file holds what each segment already wants, one section per segment (G ID). The method adapts the research part of Eddie Shleyner's Transformational Sales Emails.

| Field | What it holds |
| --- | --- |
| awareness | unaware (doesn't see the problem), problem-aware, solution-aware, aware of the person, or ready to buy |
| reads | Where this reader actually reads and talks, and how that was checked; the strategy picks the primary channel from it |
| desires (D1…) | The broad wants the segment has before meeting the person, under 10 words each |
| scores | For each desire, 1 to 10 for urgency (how badly they want it), staying power (how often it comes up) and scope (how many share it), scored by the person first |
| will | For each desire, 3 statements they'd say out loud |
| wont | For each desire, 3 statements they'd never admit, tied to how they see themselves |
| wont_checked | For each WON'T, whether a real client has confirmed it, and how |
| emotional words | Words the segment actually uses, from the research |
| quotes | Real quotes behind each desire, each with its source |
| branches | The branch IDs that answer each desire |
| reasoning | What the segment believes that makes the behavior that isn't working seem reasonable to them (written by `/understand`) |
| tried | What they've already tried, in their words |
| struggling_moment | The specific moment they decide something has to change; quoted when a quote shows it (Moesta's Jobs to Be Done) |
| language_bank | The reader's exact phrases for their problems and goals, with sources; the writer draws openings from it |
| peer_landscape | The claims the field already makes to this reader, each with where it was seen and how worn it is (said everywhere / by a few / by one), and where the person's POVs cut against them |
| sophistication | low / mid / high: how many similar claims the reader has already heard; high means only a new mechanism or a fresh frame lands (Schwartz) |
| counts | Beside each finding: how many people and sources it repeats across. One mention is an anecdote, not a finding |

**desire**

A desire is something the segment already wants, not something the person wants for them.

- Weak: "Implement better quoting software." (That's the person's solution.)
- Strong: "Stop losing jobs we already won."

**will**

Close to the research. Often almost a direct quote.

- Weak: "They want efficiency."
- Strong: "Our quotes take too long and customers go elsewhere."

**wont**

The same desire, at the level of identity. Ask: if someone held the WILL statement as true about themselves, what would it say about how they see themselves?

- Weak: "They're frustrated."
- Strong: "I built this shop on doing things right, and I'm scared that being careful is now what's killing it."

A WON'T statement is a guess until a client confirms it. Never build content on an unconfirmed one. WILL and WON'T statements always belong to the same desire.

**sources**, ranked by how close they are to real buyers:

1. The person's own sales call recordings and transcripts
2. Intake forms, client emails, DMs and replies
3. Public comments, reviews, forum threads and Q&A sites where the segment talks

Articles and blog posts don't count. They're someone's opinion about the market, not the market's own words.

**The rule that keeps the brand honest:** the desire chooses the angle, and the canon chooses the claim. Never change a POV to fit what the audience wants.

---

## Content plan (no IDs)

The bridge between the canon, which stays stable, and weekly briefs. Rewritten every quarter.

| Field | What it holds |
| --- | --- |
| gap | The reputation gap now: target association against the latest reputation check |
| branches | This quarter's one or two branches, and why the goal needs them first |
| pairs | Each branch paired with the highest-scoring desires it answers |
| mix | The mix across layers of the tree, and why |

Each layer produces a different kind of content:

| Layer | Kind of content |
| --- | --- |
| Thesis and catalyst | The origin piece |
| Values and behaviors | Stories of choices and refusals |
| POVs | Opinions that name what they reject |
| Branches | Frameworks, methods, long essays |
| Proof and vehicle | Case studies, results, offers |
| Philosophy | Rare long pieces, the About page |

The mix follows the segment's stage of awareness:

- Unaware: stories and behaviors, opening with something true about who they are
- Problem-aware or solution-aware: lead with the desire, then POVs and branches
- Aware of the person: proof and case studies
- Ready to buy: the offer, with a reason to act now

---

## Voice (W1…)

How they sound. The interview's job here is mostly to collect material, because voice comes from how they really talk, not from how they describe it.

| Field | What it holds |
| --- | --- |
| rules (W1…) | Specific, checkable rules, each with a before and after example. W1 to W10 ship as defaults (`status: default`); the person's own rules take the next free W number; a default the person confirms becomes `status: confirmed` |
| vocabulary | Phrases they use, terms they coined, words they'd never use |
| approved samples | Pieces they wrote or approved, each with a line on why it sounds like them |
| rejected samples | Drafts they turned down, with the reason |
| register | How they sound different by channel, if they do |

Draft rules from transcripts and samples, then show them to the person with before and after examples. The first draft only needs a few rules. It grows as they edit future drafts.

- Weak rule: "Conversational tone."
- Strong rule: "Uses 'you' and talks to one reader. Before: 'Many professionals find that…' After: 'You've probably noticed…'"
