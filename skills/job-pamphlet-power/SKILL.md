---
name: job-pamphlet-power
description: Builds a very low-priced pamphlet (a short book, 40 to 60 pages, usually $3 to $10) that teaches the person's core method so well that some readers want to work with them, plus its sales page, its checkout offers and the emails after the purchase. Five stages - find the mechanism in the person's best client work, write the pamphlet in four sections, the sales page and the funnel, the follow-up emails and the path to the higher-priced work - each runnable alone. Copy runs three drafts and a judge in a fresh context; the mechanism, the terms and the offers go into the canon as draft entries for the person's yes. Use for /pamphlet-power, "pamphlet", "a $3 book", "authority pamphlet", "low-ticket front end", "self-liquidating offer", "mechanism", "what should my pamphlet be about", "pamphlet sales page".
---

# /pamphlet-power

Method by Josué Valles, the studio's author, built on the Pamphlet Power system from Taylor Welch's The Wealthy Consultant, whose own pamphlets and funnels are the cases in the reference files.

A pamphlet is a short book sold for a few dollars that teaches one method at the level of the idea, well enough that the reader understands something about their problem they didn't before. It sits between a free download and a paid product: the low price takes away the risk of buying, and the buyer is a customer, not a lead. Some of them, having seen how the person thinks, want help putting it into practice.

The pamphlet's job is to show what the person knows. It proves it through depth, through a way of seeing the problem that's theirs, and through being worth more than it costs. A pamphlet that's only helpful (tips, a checklist, a summary of what everyone says) gets read and forgotten. One that changes how the reader sees the problem gets passed on.

## Helpful and authoritative

This distinction drives the method:

| Someone helpful | Someone people see as the authority on it |
| --- | --- |
| Shares information and tactics | Has a method of their own and says where the usual advice goes wrong |
| Helps with problems people already know they have | Shows people a problem under the one they came in with |
| Competes on price and results | Sets the terms of the conversation, and can charge for it |
| Joins the conversation | Starts it |

Five things make the second: a method of the person's own, a name for it, the story of how they found it, the words they use for it, and the places it disagrees with their field. In the studio each of these comes from the person's files, never from the studio: the method from their branches and their best client work, the story from `canon/bank/stories.md`, the disagreements from their confirmed POVs and the peer landscape in `canon/strategy/audience.md`.

## What it reads

- `canon/person/thesis.md`, `branches.md`, `povs.md`: the person's method and where it disagrees with the usual advice. A POV that's `forming` or `exploring` feeds the pamphlet only with `thinks_out_loud: yes` in the brief (`CLAUDE.md` rule 2).
- `canon/bank/stories.md` and `proof.md`: the discovery story and the client results. Only these, or the person's words today, with the client's permission noted.
- `canon/strategy/audience.md`: the segment's desires, the struggling moment, what they've tried, the language bank, the peer landscape and the field's sophistication. The pamphlet's problem section and the sales page are built on it.
- `canon/vehicle/vehicle.md`: the higher-priced offers the pamphlet leads to, their prices and the calls to action. A draft offer is used only once the person confirms it in the session.
- `material/` and `inbox/`: what the person has already written about the method; their sentences come first (`craft-house-rules`, "Start from their words").
- When the canon is thin, say which interview or `/understand` pass would fill the gap before writing the pamphlet. Mechanism selection (stage 1) can run on material alone.

**How it relates.** `/shape` judges whether one idea can stand alone; stage 1 here finds the single method a whole pamphlet can carry, and uses `/shape`'s naming gate for its name. `/offer-designer` designs the higher-priced offers the pamphlet leads to, and the checkout offers here when they're more than a small add-on. `/pricing-tests` sets the prices of those offers. `/diagnosis-call` runs the call the pamphlet invites people to. `/adapt` turns a finished pamphlet into posts and essays. `/visual` makes the diagrams.

## The stages

Each stage runs alone. Ask where the person is and start there:

- "I need to work out what it should be about" → stage 1
- "I know my method, I need to write it" → stage 2
- "I have a pamphlet, I need the sales page and the funnel" → stage 3
- "I need the emails after someone buys" → stage 4
- "The whole thing" → stages 1 to 4 in order, with the person's yes between each

Before any stage, say what it does, why, what they'll have at the end and roughly how long, as `CLAUDE.md` rule 7 asks. Stage 1 is one session of about an hour; stage 2 is several sessions, one section at a time.

Gather, from the files first and then by asking: what they sell, who their best client is, their highest-priced offer and its price, whether they already teach a method, and what they've already written about it.

### Stage 1: Find the mechanism

`references/mechanism-selection.md`: the client success audit, the current state, desired state and gap, the five things a working mechanism has, the contrarian angle, the IMPACT scores and the four tests. Questions ask about clients and sessions that happened, never about the method in the abstract (`skills/craft-interview`).

Output: the mechanism brief in `pieces/<yyyy-mm-dd>-pamphlet-<slug>/mechanism.md`. The mechanism and its terms go in along the route in `skills/setup-brand-tree/SKILL.md`, "Where a picked-up belief goes". A mechanism that isn't in the canon yet becomes a `draft` branch entry in `canon/person/branches.md`, with the client stories it was found in as its sources and a log line naming the mechanism brief. One that changes a `confirmed` branch goes to `proposals.md` as `kind: change to B<n>`; one that connects several confirmed entries goes as `kind: seen`. A new term the person adopts goes on the "Terms they coined" line of `canon/voice/voice-guide.md` marked `draft`, with its plain definition and source.

### Stage 2: Write the pamphlet

`references/pamphlet-structure.md`: the four sections (credibility, the problem and the method, the shift in belief, what doing it takes and the next step), with the questions for each. The pamphlet is long, so it's written one section at a time, each through `skills/craft-sales-copy` with the copy kind `pamphlet section`: three drafts of the section, the judge in a fresh context, the person's read before the next section. The brief is `kind: cornerstone`; once all four sections pass, `/refine` can push the whole further.

Output: `pieces/<yyyy-mm-dd>-pamphlet-<slug>/` holds the brief, the drafts per section, the reviews, and `pamphlet.md` with the passed sections in order. Formatting it as a book (a PDF, a layout) is the person's choice of tool; the studio's diagrams come from `/visual`.

### Stage 3: The sales page and the funnel

`references/sales-funnel.md`: the funnel's shape, its prices, the eight parts of the sales page, the add-on at checkout, the offers after purchase, the fallbacks and the confirmation page. The sales page is one piece through `skills/craft-sales-copy` (copy kind `sales page`, `kind: cornerstone`), drafted part by part when it's long. The funnel map and its prices go in `pieces/<...>/funnel.md`; every new product and price on it is a `draft` `O` entry in `canon/vehicle/vehicle.md` (with `availability:` only when the person has said open, waitlist or closed) until the person says yes. A change to a `confirmed` offer, its price included, goes to `proposals.md` only, as `kind: change to O<n>`.

### Stage 4: The emails and the path up

`references/marketing-ascension.md`: testing with people who already know the person, ads if they use them, the emails after purchase, and the path from the pamphlet to the higher-priced work. Each email is its own piece through `skills/craft-sales-copy` (copy kind `nurture email`), with its own folder, three drafts and its own judge; the sequence plan in `pieces/<...>/emails.md` lists them in order.

## Principles

1. **The pamphlet shows what the person knows.** It proves it; being helpful isn't enough.
2. **Simple to understand, real work to do.** It teaches an idea the reader can grasp in one reading and use. What it takes to put the idea fully into practice is shown honestly, as it is. The studio never makes the method look harder than it is to sell help with it.
3. **It's worth its price on its own.** A reader who never buys anything else still got more than they paid for. This is the worth-it test from `/turning-prospects-into-collaborators`, applied to a book.
4. **Selling in the open.** The pamphlet says plainly that the person has higher-priced work and how to reach it (`skills/craft-sales-copy`, truth test 6).
5. **Every sentence earns the next.** The reader keeps reading because each line gives them something.
6. **The symptom isn't the problem.** Go one layer down: the reader's stated problem, then the cause under it, in the reader's words where the research has them.
7. **The four sections are the spine:** credibility, the problem and the method, the shift in belief, what it takes and the next step. What goes inside each follows the person's material.
8. **Page references on the sales page** make the content concrete: "the pricing table on page 23".
9. **Disagreement shows authority** when it's reasoned: the field's usual advice, the premise under it that fails, and what the person does instead (`skills/craft-copylosophy`).
10. **The buyer's experience comes before the revenue.** Long relationships beat short-term money every time.

## Words used here

| Term | What it means |
| --- | --- |
| Pamphlet | A short book, 40 to 60 pages (some run to 75), sold for a few dollars, that teaches one method and leads readers toward higher-priced work |
| Mechanism | The method at the centre of it, named, the person's own |
| Self-liquidating offer | A low-priced first product meant to pay for the cost of finding the buyer |
| Average order value | What a buyer spends on average across the whole funnel |
| Checkout add-on | A small extra product offered with a checkbox at checkout (the original calls it the bump) |
| One-time offer | An offer shown once, right after purchase (an upsell) |
| Contrarian angle | Where the person's method disagrees with the field's usual advice, with the reason |
| The gap | What's missing between where the reader is and where they want to be; where the mechanism lives |
| Self-selection | Two or three kinds of reader the pamphlet is for, so each can see themselves |
| IMPACT | Interest, market demand, personal authority, audience sophistication, competitive difference, transformation |

## Never

- Never invent a discovery story, a client result, a testimonial, a number, a credential or a price. Each comes from the canon, the material or the person today, and a client result notes the client's permission.
- Never use a fear, an urgency or a limit the research and the person's plans don't show (`skills/craft-sales-copy`).
- Never make the method look harder than it is to sell the next step.
- Never coin a term for a pattern that shows up fewer than three times in the person's material (`skills/job-shape`, the naming gate).
- Never confirm a mechanism, an offer or a price in the canon; they stay drafts until the person says yes.

## Studio notes

When this skill made you guess, write one line per guess to `studio-notes.md`.
