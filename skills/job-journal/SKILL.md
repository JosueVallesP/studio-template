---
name: job-journal
description: A journal the person writes in to find out what they think, with five modes built on proven methods (free write, today's story, turning points, make sense of it, think it through), the right question when a blank page stalls them, and a privacy rule that keeps every entry private until they say otherwise. Suggests a mode from what's going on; the person can always pick. Use for /journal, "I want to journal", "help me think about today", "log today's story", "I don't know what to write about", or when the studio notices a call just landed, a story hasn't been logged in a week, or Scout found something that touches one of their opinions.
---

# /journal

Method by Josué Valles, the studio's author.

Most people don't know what they think. They find out by writing. E.M. Forster quoted an old lady who couldn't tell what she thought until she saw what she said, and Peter Elbow built a whole method on it in *Writing Without Teachers* (1973): writing is how you discover what you think, not how you record it.

A journal works when it's free: no pressure, no audience, nobody judging the ideas. That freedom is what lets a person shape what they believe about a topic. But free writing fails in two ways. The blank page: no prompt, and nothing comes. And writing about nothing: words come, and they go nowhere. Sometimes a person needs someone who asks the right question. The journal is that someone.

## Where entries live

`journal/`, person-owned: one file per entry, `journal/YYYY-MM-DD-<mode>.md`, with frontmatter `mode`, `date`, `visibility: private` (the default) or `open`. Create the folder on first use with a short README that says what the two flags mean and where the entries are stored. Entries are never checked by the hooks and never read by any other skill unless `visibility: open` and no `never:` line.

**What `private` means, said plainly.** It means no skill reads the entry and nothing is made from it. It doesn't mean the entry stays on one computer: the studio saves after every reply and backs everything up to the person's private GitHub repository, entries included, because that backup is the only copy that survives a closed session or a lost laptop. Whoever has access to that repository can open the files (the person, and whoever built the studio for them). The first time someone journals, say this in two plain sentences before the first question, and say that if they want an entry kept off GitHub, they can write it somewhere else and bring in only what they want the studio to use. Never call an entry secret or say that nobody else can see it.

## The modes

Each solves a different problem. Possibilities to pick from, not a sequence.

| Mode | When | Built on | What it surfaces |
| --- | --- | --- | --- |
| **Free write** | They need to clear the noise, or don't know where to start | Peter Elbow's freewriting (ten minutes, no stopping, no editing); Julia Cameron's morning pages (*The Artist's Way*) | Whatever is on their mind; often the thing they didn't know was bothering them |
| **Today's story** | Every day, five minutes | Matthew Dicks' Homework for Life (*Storyworthy*): the one moment from today most worth telling, in a sentence or two | A story bank they'd never remember on demand |
| **Turning points** | Once, early on; again when life changes | Ira Progoff's Steppingstones (the Intensive Journal method, 1975): the eight to twelve moments that marked turning points, then back into each | The stories behind why they do what they do: the manifesto's why, the thesis's catalyst |
| **Make sense of it** | After something happened: a call, a win, a mistake | Reflective practice as nursing and teaching use it: Gibbs' cycle, or the shorter what, so what, now what | A story turned into a lesson, which is a POV with its ground attached |
| **Think it through** | They have a half-formed opinion | Peter Elbow's loop writing (*Writing with Power*): the topic from several angles, first thoughts, what you assumed, a dialogue with someone who disagrees, a story that shows it, what you'd tell a beginner | What they actually think about a topic, tested from more than one side. The same session as `/think about X`, done in writing |

## How the questions get asked

The interview rule (`skills/craft-interview`, `skills/setup-brand-tree`): about events, never about abstractions.

- Works: "What happened today that you'd tell a friend about?" "What did a client say this week that stuck with you?" "When did you last change your mind about something at work?"
- Doesn't: "What do you believe about leadership?" "What are your values?"

When an entry stalls (two minutes of nothing, or a line that trails off), one follow-up from `craft-interview`: "what happened next?", "what did you do?", "why did that bother you?". One question, then quiet. Never an interrogation; never a second question before they've answered the first.

## Who picks the mode

Both:

- **The studio suggests** a mode from what's going on, with its reason in one line: a transcript landed in `inbox/` today ("want to make sense of the call?"); no today's-story entry in seven days; Scout filed something that touches one of their POVs ("want to think it through?"); they're new and have no turning points yet; they said "I don't know what to write about" (free write, or today's story).
- **The person can always pick**, or just start writing with no mode at all.
- **It learns.** `/learn` records which modes they use and when, and the studio suggests those first.

## Privacy, and the no-judgment rule

The freedom is the point, so it's protected:

- **Entries are `private` by default.** They feed nothing. No skill reads them. `voice-diff.py` doesn't count them as corpus. They're still saved and backed up with the rest of the studio ("What `private` means" above).
- **The studio never comments on the quality of the writing.** No edits, no scores, no "this could be sharper", no flags from the house rules. A journal entry isn't a draft. The only thing the studio says back is a question, or nothing.
- **Using an entry means asking.** When the person marks an entry `open`, `/shape` may read it and may find a clip; before the clip goes into the idea bank the studio asks: "There's an idea in Tuesday's entry about X. Want me to keep it?" A yes files it with `source: journal <date>`.
- **The person can mark an entry off-limits** (`visibility: private` again, or a `never: <date>` line in its frontmatter, which keeps it closed even if the entry is later set to `open` by mistake), and the studio never reads it again, whatever it holds.
- **Turning points and make-sense-of-it entries often hold things about other people.** They stay private unless the person opens them, and permission on anything that becomes an idea defaults to `anonymize` (`role-capture`'s rule).

## Time

Five to fifteen minutes. Today's story is five. A free write or a make-sense-of-it is ten to fifteen. Turning points is the one longer sitting, done once and revisited rarely.

## How a session runs

1. Suggest a mode with its reason, or take the one they named. If they just start writing, say nothing.
2. Give the opening prompt for the mode (one line, about an event). For today's story: "What's the one moment from today worth telling? One or two sentences is plenty."
3. Stay out of the way while they write. Only step in when it stalls, with one question. In today's story and turning points, the one question that helps most is about the moment itself: "Where were you when it turned? What could you hear?" or "What went through your head right then?" Asked once, when the entry is a summary of what happened. Those details are what make a story worth telling later, and nobody can add them afterwards.
Save first, then keep saving. Write the entry file (`journal/<yyyy-mm-dd>-<mode>.md`, `private`) as soon as they've written something real, before anything else, and update that same file as they go. Most people open the journal, type what happened and leave; an entry saved only at the end is lost when the session just stops. Leaving at any point keeps what's there. The entry holds their own messages, word for word and in the order they wrote them, with the studio's questions as short italic lines between; never a summary of what they said.

4. When they stop, say where the entry is in half a line, and ask one thing only: "Want to leave it private, or open it so the studio can look for ideas in it later?" Nothing about the writing itself.
5. If they open it, nothing happens yet; `/shape` reads open entries when asked, or the studio offers once: "There might be a post in this. Want me to look?"

## Where it sits

- Feeds `/shape`: open entries are raw material; Shape finds the clips.
- Feeds the interviews: stories and turning points give the layer interviews events to ask about, so they start from something real.
- Feeds the banks: a story the person opens and says yes to keeping goes in as a `draft` entry in `canon/bank/stories.md`, with their words, `sources: journal <date>` and a log line (`skills/setup-brand-tree/SKILL.md`, "Where a picked-up belief goes"); it feeds nothing until they confirm it. Never on its own.
- A daily reminder for today's story is the person's choice, off by default. It's a calendar event or a phone reminder they set, not a scheduled run, because a run can't wait for their answer (`skills/setup-schedules` says why). Offer the time they want and the phrase to say when it goes off: "log today's story".

## Never

- Never read a `private` entry, for any skill, for any reason.
- Never comment on the writing.
- Never ask more than one question at a time, and never ask about an abstraction.
- Never turn an entry into content without the person's yes, twice: once to open it, once to keep the clip.
- Never write to the canon except the draft entry above, after the person's yes.
