# The intake questionnaire

The questions the intake asks: only what day one needs, which is delivering the studio, writing a first post from their own material and putting their brand on the visual kit. They collect facts, not beliefs. Everything else is asked later, in the interviews and the strategy, where the studio can follow up and push back (the form spec, `docs/tally-form.md`, lists where each one went). Ten questions, about five to ten minutes. This page is the one place the count is stated.

Question 7 has a follow-up about ghostwritten pieces; it counts as part of 7.

The questions live in two places, and both produce the same file, `config/intake.yaml` (template in `templates/intake/answers.yaml`). The two differ in small ways: the form doesn't ask question 9 (a blank tool answer counts as wanted), and the intake inside Claude skips question 8.

- **Outside Claude**, as a form (Tally or similar) the person fills in before they install anything. The answers come back as a file, `scripts/tally-to-answers.py` turns it into the answers file, and `scripts/build-instance.py` builds their instance from it: their repo, their settings, their outcomes, their brand assets and their one-page guide. Their Figma kit comes later, from `setup-figma`. The first time they open Claude Code, the studio is already theirs.
- **Inside Claude**, as `skills/setup-intake`, for someone who installed the bare studio from GitHub. It asks the same questions one at a time, writes the same file, and runs the same build.

Each question names its field. Keep the field names when you build the form; the script reads them. One question, one answer: no question asks two things.

## About you

1. **Your name, as you'd like it to appear.** `name`
2. **Your email.** Where the studio's emails go: its link and the steps to start. `email`
3. **What do you do, and who do you do it for?** Two or three sentences, the way you'd say it to someone at a dinner. `what_you_do`

## Your content

4. **A year from now, what do you want to have happened because of this content?** Clients, a book, a job, a reputation for something specific. A rough answer is fine; the vehicle session comes back to it. `goal`

The studio writes LinkedIn posts and Substack essays. Say so before the next question, and that they can pick both: the strategy works out which one leads, with them, after the interviews.

5. **LinkedIn and Substack: where are you with each?** For each one: posting there now, want to start, or not for now. (A newsletter somewhere else, like Beehiiv or Kit, counts as Substack "now".) Written as `publishes_on` (the ones they're on now) and `wants_to_start`.
6. **About how many hours a week can you give this when work is busy?** Including the time to read and approve drafts. 1 to 2, 3 to 5, 6 to 10, or more than 10. `hours_per_week`

## Your material

The studio reads what they've already written or said before it asks them anything, and it reads files, not links. The first post comes from it. Say all three before the next question.

7. **What have you already written or said that you can send the studio?** Say how it gets there before they answer, as `docs/handing-things-over.md` says for where the studio runs: paste text into the chat, attach a file to the message (the studio files it in their inbox, a folder in their studio where anything they hand over waits until it's read), or, on the form, upload it. Posts, essays, a book chapter, course notes, transcripts of calls or talks. Tell them how: LinkedIn posts: copy their best 15 to 30 into one document with the date above each (a Shares.csv from LinkedIn's data archive works too, when their archive has one, and its Comments.csv brings in their comments on other people's posts, which show the positions they take); a Substack archive: the publication's Settings, Exports, "Create new export" (the studio keeps only the posts, never the subscriber list); transcripts from Zoom, Otter, Fathom, Descript or YouTube. PDF, Word, text, CSV, HTML or ZIP all work; `scripts/inbox-to-text.py` turns them into text. Audio and video need a transcript first. Name what's coming in `material`.

   Then one more question, asked plainly: **Did anyone else write any of these for you, like an agency, a ghostwriter or someone on your team? Which ones?** Say why in one line: the studio learns how they write from their own pieces, and a piece someone else wrote would teach it the wrong voice. Many people had help, and it's fine. Write the answer on the matching `material` line, after a colon ("LinkedIn posts: 2019 to 2022 written by an agency"). Each file they name gets this first line when it's filed: `<!-- studio: written for them, not by them -->`. The map still reads those pieces for what the person approved, and the voice work and voiceprint skip them. When they can't say which posts, write what they know ("posts before 2023") and mark only the files that clearly fit.

## Your tools

8. **Your GitHub username.** The studio lives in a private GitHub repo, and the username is how they get access to it. Skipped when the intake runs inside the studio, since they're already in it. `github`
9. **Do you use Notion, Figma, both or neither?** Notion holds the dashboard and Figma holds the visual kit. Both are optional; without them the studio works in files and `/status`. Written as `notion: yes` or `no` and `figma: yes` or `no`.

## Your brand

10. **Do you already have a logo, brand colors or fonts?** Ask for the font names and the colors (hex codes like #1A2B3C if they have them, plain names if not), and for the logo as a file: inside Claude, they attach it to the message and the studio files it; on the form, they upload it. Say what it's for in plain words: the visual kit is the set of templates in Figma for the pictures in their posts, and their brand goes on it today (leave Figma out if they don't use it). If they don't have any, they say so: after the interviews, the studio builds a look from what it learns about them. The worked example of this question, said well, is in `docs/handing-things-over.md`. `logo`, `colors`, `fonts`

## Notes for building the form

- Required: name, email, what you do, the goal, LinkedIn and Substack, hours, and the GitHub username on the form. Everything else can be blank. A blank tool answer counts as wanted, so the quick win offers it and the person can skip it there. A blank stays blank in the instance; the script never fills a gap with a guess.
- File uploads (logo, fonts, material exports, transcripts) go into the instance's `inbox/` with the original names, so `/capture` and the brand tree extraction find them. Material on paper: photograph it or type it, and it goes in the same place.
- Lists (channels, material, colors) are one item per line; the script splits on lines. In a list item, keep the name first and any note after a colon ("LinkedIn: 3k followers", "#0B3D2E: dark green"); the script shows the name alone where a sentence needs it and the whole line where there's room.
- `scripts/tally-to-answers.py` turns the form's export into `config/intake.yaml` before the build (`docs/tally-form.md` says how to build the form so it can). The YAML is the contract, not the form.
