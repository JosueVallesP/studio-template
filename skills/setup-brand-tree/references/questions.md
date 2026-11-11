# Question bank

The person layer (values, behaviors, POVs, philosophy, thesis) has its questions in its own session file under `../interviews/`. This file holds the questions for the other layers and the follow-ups that work after any answer. Every question here exists to fill a field in `fields.md`. If a question fills no field you still need, skip it.

How to use this file:

- When you have a draft entry, show it and ask if it's true before using a cold question.
- Ask one question at a time.
- Pick the follow-up that fills the field you're missing. If every field is there, restate and move on.
- Don't read questions out in order. Choose the one that fits where the conversation is.
- Reword questions to fit the person's field and how they talk.

## Questions to never ask

These ask for an abstraction about the person, and people answer them with a plausible, polished line that tells the studio nothing:

- "What are your values?"
- "What do you believe that most of your peers would argue with?"
- "What's true about your field that most people in it miss?"
- "What does your field get wrong?"
- "What makes you unique?"
- "What's your brand?"
- "What do you stand for?"
- "What's your philosophy?" or "What's your thesis?"
- "How would you describe your voice?"

Ask about what happened instead: choices, refusals, moments something worked or failed, things they had to un-teach. The studio finds the abstraction and hands it back.

---

## Values, behaviors, POVs, philosophy, thesis

In their session files: `../interviews/values.md`, `behaviors.md`, `povs.md`, `philosophy.md`, `thesis.md`.

## Branches

- "What do you find yourself explaining over and over? When did you last explain it, and to whom?"
- "Think of the last time you walked a client or a colleague through how you do something. What were the steps you took them through? Even if you've never named them."
- "Walk me through how you'd solve [a problem they mentioned] step by step."

For each branch:

- "What problem does it solve?"
- "What are the parts or steps? How does one lead to the next?" When they've never written it down and the steps don't come, guess instead: "Most people in your field would do it like this: <the usual steps>. Where do you do it differently?" A "yes, that's it" is the field's normal practice and isn't their branch; every "no, not really" is theirs, and that's where to dig. If you don't know what's normal in their field, say so and ask them what most people do, never invent a baseline.
- "Where did it come from? What happened that made you see it?"
- "Where doesn't it work?"
- "If you drew it, what would it look like?"
- "Is this something new you put together, something others in your field do but don't talk about, or a known method you've given your own name?" (mechanism)
- "Which of your audience's wants does this answer?" (desires)
- "What words do you use for each part? What words should nobody swap in?"

## Stop list

- "Tell me about a time you saw someone in your field post something and thought you'd never say that. What was it?"
- "Tell me about a time you started to write or say something in public and stopped yourself. What was the topic?"
- "When did you last hear someone in your field make a claim and think you'd never say that to a client? What was the claim?"
- "Are there names, clients or companies you'll never mention?"
- "What words make you cringe when you see them in your field?"
- "What have you stopped talking about? When did you last catch yourself about to say it?"

## Stories

Ask for stories inside every other layer. When someone gives you a story, first put them back in it, then get the parts.

**Back in the moment** (before the parts, once per story worth telling in public). A story told from memory comes out as the summary they've given before; the details a reader believes come back when they're in the scene again. Since the writer may never add a detail of what it looked or felt like, or what they thought at the time, the interview is the only place those come from.

- "Take me to the moment it turned. Where were you? Who was in the room?"
- "What could you see or hear right then?"
- "What went through your head at that moment, before you said anything?"
- "Tell me the small things too, even the ones that seem not to matter."

Don't ask them to imagine it from someone else's view; that move makes people fill in what they never saw. Write what they give into `scene` and `thought_then`, word for word.

**The parts:**

- "When was that, roughly?"
- "Who was involved?"
- "What did they say? What did you say?"
- "What happened after?"
- "Were you there for that part, or did someone tell you?" (`told`)
- "Is this one you've told a lot, on stage or to clients?" A story told for years has drifted toward its best version; for the facts that matter (what was said, a number, a date), ask whether there's a record: an email, a note, a slide.
- "Can I use that one with names, without names, or not at all?"

Then read back the `what` and `result` lines and the permission in one breath, and ask if that's right. A story told in full and read back once is confirmed in the same session as the entry it supports; a story told once and never read back stays draft. Don't let a story wait a session for want of a read-back.

## Proof

- "What results have clients gotten? Do you have numbers?"
- "Can I use that result in public? With their name or without?"

Never round a number up or fill a gap with a guess.

## Vehicle

Start with the goal, then the business.

- Read back the year-from-now answer in `strategy/outcomes.md` and ask: "Still true? What would you change?" Then: "Be specific. What does it look like when it has happened?" (goal). Don't ask the year-from-now question again from scratch.
- "What would you need to be known for so that happens?" (known_for)
- "What would you need to do to be known for that?" (do)
- "What would you need to learn to do those things?" (learn)
- "Does the business have a name?" Only if `config/intake.yaml` has no `business`.
- "What do you sell right now? Walk me through each offer."
- "Who is each one for, and what do they get?"
- "Which offers are open, which are on a waitlist, and which are closed?" (availability)
- "What do you want to sell more of over the next three months?"
- "How does your business prove what you believe?"
- "What should someone do after reading your content? What exact words do you use to invite them?"

## Brand strategy

- "Tell me about your last three clients. How did each one find you, and how did they describe the problem when you first talked?"
- "Of the people you've worked with, which two or three would you clone if you could? What was it about each one?"
- "How would one of them describe their problem, in their words?"
- "What do they already believe about your field before they meet you?"
- "Who sends you clients? Peers, connectors, people in nearby fields?"
- "Tell me about a client or a project you'd turn down if it came again. What happened?"
- Read back `known_for` from `vehicle/vehicle.md` and ask: "Is that the first thing you want people to think of when they hear your name, or is it something else?" (target association). Don't ask it from scratch; the vehicle session already asked what they need to be known for.
- "What do you think they actually think of today?" (then suggest they ask three clients or peers and bring back their exact words for the reputation check)
- Read back the channels from `config/intake.yaml` (`publishes_on`, `wants_to_start`) and ask only "Still right?" (Don't decide their jobs or cadence; `strategy-brand` does that.)
- "When someone likes a piece of yours, what should they do next?"

For segment words, ask for real phrases: "What's something a client actually said to you before you worked together?"

## Audience

The audience layer runs through `/understand` (`skills/job-understand`): research from what readers say in their own words, written as drafts into `strategy/audience.md` for the person's yes. Offer it first, in one sentence on what it gives them. The six questions below are the fallback, only when the person won't run the research or has no sources for it. Ask them one at a time, for each segment. Keep answers short and specific; 150 sharp words beat 2,000 vague ones.

1. "In general, who is your market? Name the roles, the work they do and the outcome they care about."
2. "Is there a narrower group inside it that's most ready for what you do? What do they already believe, and what have they already tried?"
3. "What problems do they have, and how does failing at them make them feel? What do they want to feel instead?"
4. "Think of the last time one of them pushed back on something you suggested. What did they say, and what did it tell you about what they believe?"
5. "How much do they know about their problem when they first meet you? Do they see it at all, know it but not the fix, know fixes exist, or already know you?"
6. "Where does this reader actually read and talk? LinkedIn, a newsletter, a forum, a community, nowhere online? How do you know?" (Fills the `reads` field; the strategy needs it to pick the primary channel.)

What the person offers, its benefits and how it changes people come from the thesis, branches and vehicle, so don't ask again.

Then ask for raw material:

- "Can you share sales call recordings or transcripts, intake forms, or client emails where people describe their problem?"
- "Where does this group talk online? Forums, groups, review sites?"

After the research, for each desire:

- "Score this from 1 to 10 on how badly they want it, how often it comes up, and how many of them share it." (Ask before showing any AI scores.)
- "Write what they'd say about this out loud, then what they'd never admit." (Ask before showing drafted WILL and WON'T statements.)
- "Has a client ever said or shown something like this WON'T statement? Who, and when?"

## Content plan

Not asked here. `strategy-brand` derives the content plan from the confirmed canon once the minimum is in place. The one interview question the strategy depends on is capacity, because the strategy trims cadence to it. Intake asks it (`hours_per_week`) and the build records it in `strategy/outcomes.md` under Capacity. If that line is empty when you reach the vehicle session, ask it there: "How many hours a week can you give this, honestly, when business is busy?" and record it in `vehicle/vehicle.md` under Constraints.

## Voice

Voice comes from material, not from questions. Your jobs here:

- Ask for samples. If their material is in `material/` or `inbox/`: "Pick three to five from what you sent that sound most like you, and one or two that don't." Otherwise: "Share three to five pieces you wrote that sound most like you, and one or two that don't."
- Ask about each: "What makes this one sound like you?" and "What's wrong with that one?"
- Ask for words: "Are there phrases you use a lot? Words you'd never use?"
- Draft a few rules from their answers and samples, show each rule with a before and after example, and ask if it's right. Their rules take the next free W number after the ten defaults. Show the default rules (W1 to W10) too, one line each: a default they say yes to becomes `status: confirmed`; a default their samples contradict gets their rule beside it and is marked `status: retired` once they say yes.

---

## Follow-ups (use after any answer)

Three moves earn their place on almost any answer:

- Ask what changed: "What do you think changed that made it work?" This brings out the process.
- Ask whether it works for everyone: "Would that work for anyone, or was it specific to that case?" This fills a POV's `condition` (a branch's `limits`).
- Ask what someone else should do: "If someone wanted the same result, what's the biggest thing they should focus on?" This fills what the thesis `implies`.

Others:

- "Give me a specific example."
- "When was the last time that happened?"
- "What did it cost you?"
- "What did you do instead?"
- "Who would disagree with that?"
- "Where doesn't that apply?"
- "What else was on the table then? What did you weigh?"
- "Say more about that."
- "What happened next?"
