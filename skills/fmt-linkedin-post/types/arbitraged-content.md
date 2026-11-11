# Type: arbitraged content

A post that borrows the attention someone else's material already has (a story, a person, an event, a book, a podcast, a memo, a quote, a named law) and uses it to carry the person's own idea. The name comes from financial arbitrage, which profits from a price gap between two markets: here the gap is in attention. A famous name, a dramatic event or a counterintuitive case has attention built in; the post attaches the person's idea to it and makes the connection feel like it could only go one way. The post chain reads this file at the moves stage (step 3g, once the shape is set) and follows it through the draft and judge stages, as an add-on to the cards; it isn't a procedure of its own. Method by Josué Valles, built from 18 annotated posts.

## What it's for

Reach, and a point of view people remember because it arrived inside something they already wanted to read. The borrowed material is the vehicle and the person's idea is where it goes. The type covers the cases where the person has a source and needs the idea it carries said well, and the cases where the person has an idea and needs a source to carry it (step 1).

## Where it sits in the library

- **Hook moves:** 2 (here's the actual document) for a memo, a quote set, a rule list or a book passage; 13 (the reframe) for a named law or concept anchored in a case (card 13 already holds Conway's law, L121); 12 (the numbered promise) on top of 2 for a book distilled into principles; 10 (news, plus a take) when the borrowed event is this week's; 9 (the line someone said) when one public line opens the post. 3 (someone notable did something odd) is where the story-led sources start, and those route to `borrowed-story` (see the next section).
- **Structures:** S2 (the explained list) for a memo, a book or an event distilled into points with the person's gloss on each; S4 (the argument) for a concept anchored in a case; S3 (the story arc) for a source told alongside the person's own story; S7 (the body is the hook) for the shortest signal boost.
- **Inside moves:** M8 (the subject's own words), M9 (the meaning line, which is where the bridge lives), M6 (the analogy) when a concept needs something physical, M2 (the turn), M1 (the context block, kept short).
- **Inventory slots:** BORROWED or DOCUMENT for the source, plus the OPINION it carries. NEWS when the source is recent. STORY when the person's own experience runs alongside the source. Without an OPINION of the person's, the source is a book report and the post fails the swap test.

What this file adds to cards 2 and 13: the two modes, the routing between idea-led and story-led sources, the five parts with the bridge as the joint, the lesson swap test, and the line between the source's words and the person's.

## When it fits, and when it doesn't

It fits when the person has an idea of their own and a real source that carries it. The boundary that matters most is with `borrowed-story`, because both build a post on something the person didn't make.

**Arbitraged content and borrowed story, and how to route.** Borrowed story is a true story about a real person, company, campaign or moment, told so it proves the person's claim: the post's spine is the story's arc (a decision, a life, a case), and the craft is in binding that one narrated case to the claim. Arbitraged content is wider in what it borrows and different in where the weight sits: the spine is the person's commentary on borrowed material, and the borrowed thing is often a body of ideas (a book, a memo, a set of quotes, a law, a lecture series, a workshop) rather than a sequence of events. So the route follows what the post would be built on:

| What's borrowed | Structure type (examples) | Route |
|---|---|---|
| A person's life or arc in order | Biography or timeline (#3, #16, #17) | `borrowed-story`, the chronicle path |
| One leader's decision and what came of it | Leadership case study (#18) | `borrowed-story`, decision and dividend |
| A brand's stunt or campaign | Brand case study (#12) | `borrowed-story`, annotated case or decision and dividend |
| A short observation about one person's habit | Personal observation (#4, #5) | `borrowed-story`; read its step 1 failure tell first |
| One sentence someone said, which is the whole payload | Quote anchor with a single line | `borrowed-story`, quote delivery |
| A memo, a letter, a rule list or a set of quotes, reproduced and annotated | Quote or memo anchor (#1, #10) | this file |
| A book's or a program's ideas, distilled | Book distillation (#2, #11) | this file, with `power-listicle` for the list craft |
| A named law, idea or philosophy, anchored in a case | Concept plus story (#7, #13, #14, #15) | this file |
| A free resource worth pointing at | Signal boost (#6) | this file; `simple-listicle` if there are three or more |
| What was taught at an event the person attended | Event or workshop recap (#9) | this file, with the adjacent witness rules from `borrowed-story` |
| A source told side by side with the person's own experience | Personal plus source parallel (#8) | this file, with `owned-story` for the person's half |

When a piece routed here still narrates a real event inside it (the case under a concept, the origin of a memo, the moment a law was named), the story part follows `borrowed-story`'s steps 1, 2 and 4 and its gate. When Mode B (step 1) turns up a single story, the piece goes to `borrowed-story` from that point.

The other boundaries:

- **Newsjacking.** The source is news, the timing is the point and the post's job is the take on what just happened: `newsjacking`. A parallel post that uses this week's news as the source (#8) stays here only when the person's own story is the larger half.
- **Op-ed.** The post is the person's argument and the source is one piece of evidence among several: `op-ed`. The sign is that the borrowed material could be cut to one sentence without the post losing its spine.
- **Power listicle.** A book distilled into numbered propositions uses `power-listicle` for the count, the item headline and the item test. This file adds the attribution rule (step 4) and the demand that the person's commentary, not the book's summary, is what each item carries.
- **No idea.** The person has a source and nothing it made them think. Ask what it made them think, or offer it as a `/scout` find for later.

## Facts and sources

Everything about the borrowed material (a name, a date, a figure, a quote, a title, a price, what a book says, what a speaker said, how a law got its name) is `borrowed: verify` in the source map, with its source named on the row: a link, a book with the page, an episode with its date and time, the memo itself. The idea it carries comes from the person: a canon POV or belief, an idea bank entry, `material/`, or what they said today, cited like any fact about the person under `CLAUDE.md` rule 1. Their parallel story (#8) and their experience of following a program (#11) are facts about them, never filled in.

Any factual claim about a real person or event runs the gate in `borrowed-story.md`, section "The verification gate" (the three tiers, the seven ways it goes wrong, the two checks and the two cautions). This file doesn't have a gate of its own. The source skill asked the writer to "verify it or soften the language"; the gate is the studio's version of that, and it wins.

Two notes on the sources this type uses:

- **An event the person attended.** What a speaker said comes from the person's notes or recording, cited as the file. Quote marks only around words the notes hold exactly; the rest is paraphrase and attributed. That's borrowed story's adjacent witness path, and the safest material in this type.
- **The examples file is craft, never fact.** Several of its source posts drew defects when the borrowed-story corpus checked them (the Ogilvy castle hook, the Carnegie two-hours claim). Take the construction; never reuse a figure or a line from it.

## Step 1. Which mode, and what's the idea

The person comes in one of two ways:

- **Mode A: they have a source.** A story, a quote, a book, a podcast, a person, an event. Find out what idea they want it to carry. If it isn't clear from the material or the canon, ask: "What did this make you think?"
- **Mode B: they have an idea.** A lesson, an opinion, an insight. The writer finds a source that carries it (step 3).

In either mode, the person's idea is the destination. If neither the session nor the files give one, there's no post yet.

## Step 2. Pick the structure type

Use the routing table above. The source's guidance on depth for each kind that stays here:

- **Quote or memo anchor.** Reproduce the artifact, then comment. The artifact gives the reader something concrete and shareable; the commentary can be short (three sentences in #1) and still does the arbitrage. Hook move 2's rule holds: quote it, never paraphrase it.
- **Book or program distillation.** Distill the source into principles with the person's commentary on each. The person adds their own examples and says the idea in their reader's language; the best line in #2 is the writer's, not the book's. When the person followed the program (#11), what happened to them is the post's proof, and it needs their account.
- **Concept plus story.** State the idea, ground every abstract claim at once in a concrete case, give the idea a phrase that sticks (#7 "you ship your org chart"), and end with something the reader can do or test against (#13 hands over a litmus question, #14 a "try this"). The commentary often runs longer than the source's own words (#15); that's the arbitrage working.
- **Signal boost.** Point to a remarkable resource with brief context. The lightest form. Under the studio's rules it still needs the person's reason (H7): what they took from it or why their reader needs it. One line of praise and a link fails the swap test.
- **Event recap.** What it cost or what made it rare goes in the hook (#9's price tag), then the takeaways, each with something specific enough to use.
- **Personal plus source parallel.** Alternate the source's beats with the person's own, so each beat of theirs answers one of the source's. The person's half carries the weight and follows `owned-story`.

## Step 3. Find the source (Mode B)

The writer uses `/scout`, which files each find as an outside entry with its source (`CLAUDE.md` rule 8). By default, one quick search for one strong source; when the person asks for depth, search several angles and bring two or three candidates, each with a one-line pitch: the hook, why it fits the idea, and the angle the post would take. The person picks.

What to look for:

1. **Stories, not definitions.** A person, an event, a brand, a moment. "Leadership" is a topic; "Alan Mulally taking over Ford in 2006" is a story.
2. **Drama and specificity.** Amounts, timelines, turning points, quotes. An abstract idea needs a concrete moment to hang on.
3. **Facts that can be checked.** Run the gate on the core claims of every candidate before offering it. If something can't be verified, say so in the pitch.
4. **Sources the reader hasn't seen a hundred times,** or a fresh angle on a well-known one. Borrowed story's second caution explains why: the pool of business anecdotes is small and copied, errors included.

## Step 4. Draft the five parts

Every piece has five parts. The order and the weight change with the material; all five are present.

### The hook

The first one to three lines stop the scroll, and they have to work before "see more". The hook borrows from the source: a startling fact, a specific number, a dramatic moment, a name people know. What works is specificity ("a $363.2 million advertising empire" against "a huge advertising company"), tension the reader needs to close, and concrete details (names, dates, amounts, places) that say this is a real story. Hooks fail when they're abstract or about the writer ("I've been thinking a lot about leadership lately"); house rule H23 already bans the rhetorical-question opener. The hook is also the riskiest sentence: borrowed story's "The hook is the riskiest sentence" applies here, and a cause word joining two facts is the part to check.

### The story

Unpack the source, and only as much of it as the lesson needs. Three ways this part goes wrong:

- **Retelling without a point of view.** Every detail serves the lesson. A fact that doesn't connect to it gets cut.
- **Too much context.** The reader doesn't need the full encyclopedia entry. Pick the details that make the strongest bridge.
- **Losing the reader's trust.** Arbitraged content lives or dies on the credibility of the source. Nothing gets embellished; the gate decides what's stated flat.

### The bridge

The pivot from their material to the person's point. Often one line, and it reframes everything the reader just took in, the moment a lens clicks into focus. Two of the source's best: "Ogilvy didn't become the best despite being a chef, a spy, and a farmer. He became the best because of it." and "Some people start late because they're behind. Others start late because they're finally whole."

The source asks for a bridge that sounds like a proverb and is quotable on its own. The studio's rules narrow that: the bridge is a full sentence that says how the source produces the idea (borrowed story's mechanism test), which is M9's job. A bridge built as a "Not X. Y." pair or an "isn't X, it's Y" reversal fails H17, whatever it holds; a line made to be admired fails H1. Quotable is what a clear bridge turns out to be, and never the target. The source's ban on bridge clichés stands: "and the rest is history", "little did he know", "fast forward to today". A bridge should only fit this piece.

### The lesson

The person's idea, and the reason the post exists. It can be a direct takeaway with a clear "so what", a set of principles drawn from the source with the person's commentary on each, a call to examine something in the reader's own work ("Pull up your org chart."), or the person's own reflection connecting the source to their life or work.

**The lesson swap test.** If a different lesson could replace this one and the piece still works, the bridge isn't doing its job. The story and the lesson should feel made for each other. This is the same failure borrowed story's substitution test catches from the other side.

**Keep the source's words and the person's apart.** The reader should always be able to tell which line came from the source and which is the person's. In #2 the reframe is the writer's and sits after the book's principle; in #10 the writer follows each Meditations quote with a plain business version. Credit the source's ideas to the source; never put the person's line in the source's mouth or the source's line in the person's.

**Put the person in the post.** One sentence of the person's reading turns everything after it into their view instead of a claim about the subject (borrowed story's "Put the person in the post"; judge check 17).

### The close

The last one to three lines. The source names four: a question that invites a response, a provocative restatement, a call to action, and a short line that ends the piece. The studio narrows these too. The provocative restatement and the short last line are both C1 (the restated principle), the most used close in the library and the weakest; prefer C2 (the question back, aimed at the reader's own experience), C3 (the small instruction, as in #13 and #14) or C6 (no close). A close earns its place when it carries a noun from the source (borrowed story's BS7 test).

### What to avoid

- **Moralizing.** Show something and let the lesson land. A line telling the reader what to feel ("and that's why we should all be more grateful") kills the piece.
- **Fake profundity.** A simple lesson stays simple. "There are no real rules, so make rules that work for you" (#5) does more than a paragraph that dresses it up.
- **Disconnected sources.** If the source doesn't lead to the lesson, find a better source. Don't force the joint.
- **Hagiography.** Don't make the source a saint. The strongest pieces keep the complexity: Ogilvy thrown out of Oxford, Parsons living with PTSD, Mikitani leaving a prestigious bank job. Those details are facts too, so they come from a source and pass the gate like any other; a flaw added for texture is as invented as a virtue.

### Length

The source gives 1,200 to 1,500 words as the LinkedIn maximum. LinkedIn caps a post at 3,000 characters, roughly 450 to 500 words, so the platform is the ceiling. Inside it, length follows the material: #5 is five sentences, the concept piece (#7) is the longest in the set, and an emotional story earns its length (#17). For anything story-led, borrowed story's length data applies.

## Checks the judge adds

On top of the stage's checks, each a FAIL with the line quoted:

- **AC1. Route.** The post's spine isn't a single narrated story of a real person or company. If it is, the piece belongs to `borrowed-story` and BS1 to BS8 apply in full. Any narrated event inside a post routed here runs BS1, BS5 and BS6.
- **AC2. The gate.** Every proper noun, date, figure, title and quote about the source has a `borrowed: verify` row with a named source, or is hedged and marked `source: not found`, as `borrowed-story.md` "The verification gate" sets out. Graded as "Outside example unverified" in the gates table in `skills/role-editor`.
- **AC3. The idea is the person's.** The lesson traces to a canon entry, an idea bank entry, `material/` or `said today`. A lesson with no source row is invented (check 18).
- **AC4. The lesson swap test.** A different lesson can't replace this one without the piece breaking.
- **AC5. The bridge** says how the source produces the idea, in a full sentence. No H17 pair, no bridge cliché.
- **AC6. Commentary outweighs summary.** Every borrowed principle, quote or point has the person's line on it, and every detail in the story part serves the lesson.
- **AC7. Attribution.** Each line is plainly the source's or the person's, and the source is credited for its ideas.
- **AC8. The ceiling.** The lesson claims no more than the source supports: no "proved", law or ranking on one case (BS3), no moral the material doesn't carry.
- **AC9. Hagiography.** The source isn't presented as flawless when the material holds its complexity, and any flaw shown has a source.

## Things that look like rules and aren't

Dividers between the source and the lesson, bold on a key phrase, numbered lists, arrow sub-points, emoji, profanity, italics for a mantra, a labelled "TAKEAWAY", the register (playful for Heinz, raw for Van Der Beek, reflective for Bradbury). They vary across the eighteen examples with the material, and the source says to format only when a visual element earns its place. The house rules still apply to all of them, and the source's own voice notes that clash with them lose: em dashes for asides (H16), stacked one-word sentences for drum beats (H4, H29), and cutting "really", "just" and "actually" on sight (H19 keeps the stance words a talker uses).

## Examples

Eighteen annotated posts, sorted into the ten structure types, are in `arbitraged-content/examples.md`. Read the ones for the structure type before drafting, as calibration for construction and depth. For a story-led source, read `borrowed-story/exemplars.md` instead.
