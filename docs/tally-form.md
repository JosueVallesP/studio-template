# The Tally form

How to build the intake form in Tally so `scripts/tally-to-answers.py` can read it.

The form sits inside the Notion onboarding page, below the part that explains the accounts: GitHub, where the studio lives, is needed; Notion (for the dashboard) and Figma (for the visual kit) are optional. A free account is enough for each. The form doesn't ask about Notion or Figma: a blank answer counts as wanted, and each quick win offers its tool and lets the person skip it.

The form asks only what the studio needs on day one: what it takes to deliver the studio, write a first post from their own material and put their brand on the visual kit. Everything else waits for the interviews, where the studio can ask a follow-up, push back and hear the answer in the person's own words. Thirteen fields on four pages (the questions in `docs/intake-questions.md`, with some split into separate fields), about five to ten minutes, plus the time to find their files. "What moved to later" below says where every other question gets asked.

Nothing asks for what the studio can't use, and no help text promises what it can't do. Two limits shape the questions:

- **The studio writes for LinkedIn and Substack.** Those are the only channels with a format skill today, so the form asks about those two by name. Anywhere else they publish comes up in the strategy, as context.
- **The studio reads files, not links.** It can't open a LinkedIn profile, a Substack URL or a YouTube video. So the form asks for uploads, says how to export each one, and never asks for links.

## Rules for building it

- **Keep each title's start as written.** The converter finds each answer by the start of its title, the part shown in bold. You can change the rest of the title and all the help text.
- **Use the field type listed.**
- **Mark as required** only the fields marked required.
- **One page per section.** The sections below are the pages.

## Page 1: You

| # | Title (bold part must match) | Type | Required | Help text |
| --- | --- | --- | --- | --- |
| 1 | **Your name**, as you'd like it to appear | Short answer | Yes | |
| 2 | **Your email** | Email | Yes | Your studio's link and the steps to start arrive here. |
| 3 | **Your GitHub username** | Short answer | Yes | Your studio lives in a private GitHub repo that only you and we can see, and this is how you get access. Just the username, without the @. |
| 4 | **What do you do**, and who do you do it for? | Long answer | Yes | Two or three sentences, the way you'd say it to someone at a dinner. |

## Page 2: Your content

Put this text above question 6 (a Tally text block): "The studio writes LinkedIn posts and Substack essays. You can choose both. You don't need to decide which comes first: after the interviews, your strategy works that out with you."

| # | Title | Type | Required | Help text |
| --- | --- | --- | --- | --- |
| 5 | **A year from now**, what do you want to have happened because of this content? | Long answer | Yes | Clients, a book, a job, a reputation for something specific. A rough answer is fine: the interviews come back to it. |
| 6 | **LinkedIn:** where are you now? | Multiple choice: "I post there now" / "I want to start" / "Not for now" | Yes | |
| 7 | **Substack:** where are you now? | Multiple choice: "I have a newsletter there now" / "I want to start one" / "Not for now" | Yes | A newsletter somewhere else (Beehiiv, Kit, Ghost) counts as "I have a newsletter there now". |
| 8 | **About how many hours a week** can you give this when work is busy? | Multiple choice: "1 to 2" / "3 to 5" / "6 to 10" / "More than 10" | Yes | Including the time to read and approve drafts. |

## Page 3: What you've already made

Put this text at the top of the page: "The studio reads what you've already written or said before it asks you anything. Your first post comes from it, and the interviews start from your own words. It can only read files, so upload them here. You can skip this and send them to your studio in the chat later, but then your first post waits for them."

| # | Title | Type | Required | Help text |
| --- | --- | --- | --- | --- |
| 9 | **Upload what you've already written** | File upload (allow multiple) | No | Posts, essays, articles, a book chapter, course notes. PDF, Word, text or CSV files, up to 10 MB each. **LinkedIn posts:** copy your best 15 to 30 posts (the ones that sound most like you, not only the ones that did well) into one document, with the date above each, and upload it. **Substack:** in your publication's Settings, click Exports, then "Create new export"; Substack emails you when it's ready. Upload the ZIP. It also holds your subscriber list: the studio keeps only your posts and deletes the rest. |
| 10 | **Upload transcripts of you talking** | File upload (allow multiple) | No | Sales calls, podcast interviews, workshops, voice memos. These get your voice right better than polished writing does. Text transcripts only: Zoom, Otter, Fathom, Descript and YouTube all export one. |

## Page 4: Your brand, if you have one

Put this text at the top of the page: "If you already have a logo, colors or fonts, they go straight onto your visual kit today. If you don't, skip this page: after the interviews, the studio builds a look from what it learns about you."

| # | Title | Type | Required | Help text |
| --- | --- | --- | --- | --- |
| 11 | **Upload your logo** | File upload | No | |
| 12 | **Your brand colors** | Long answer | No | One per line, with the hex code if you know it ("#0B3D2E dark green"). |
| 13 | **Your brand fonts** | Long answer | No | One per line. |

## Settings

- **After submit:** a thank-you page saying what happens next: "Your studio is being built. Within the hour you'll get an email with your link and the steps to start. Meanwhile, accept the GitHub invite when it arrives, and make sure you can log in to Notion and Figma if you use them."
- **Notifications:** turn on the email to yourself for every new submission.
- **Payment,** if the form is also the checkout: Tally can take payments through Stripe on the free plan. Put the payment block on the last page. If people pay somewhere else first (Gumroad, Stripe link, Whop), send them to this form from the thank-you page there.

## What each answer feeds

| Answer | Where it goes in their studio | What reads it |
| --- | --- | --- |
| Name, what they do | `YOUR-STUDIO.md`, `config/intake.yaml` | Every greeting; the interviews read it back instead of asking again |
| Goal | `canon/strategy/outcomes.md` | The interviews (the vehicle session sharpens it) and `strategy-brand` |
| LinkedIn and Substack status | `canon/strategy/outcomes.md` (Channels), `config/tools.md` | The quick wins (which placements to show) and `strategy-brand` (which channel leads) |
| Hours | `canon/strategy/outcomes.md` (Capacity), `YOUR-STUDIO.md` | The guide's "your week", and `strategy-brand` trims the cadence to it |
| Uploads | `inbox/`, converted to text by `scripts/inbox-to-text.py` | The map, the first post, the interviews |
| Logo, colors, fonts | `canon/visual/brand-assets.md`, and the logo in `inbox/` | `setup-figma` puts them on the kit |

## What moved to later

These were on the form once. Each is asked where the studio can follow up on the answer, and nothing reads it before then.

| Question | Where it's asked now |
| --- | --- |
| How would you know it happened? | The vehicle session of the interviews ("What does it look like when it has happened?") |
| Business name | The vehicle session, with the offers |
| Anywhere else you publish, your links | `strategy-brand`, step 5, when it gives each channel its job |
| Does anyone else touch your content? | `strategy-brand`, step 6, with the cadence |
| What you've made that you can't upload | The interviews' intake step, when they ask for material |
| Looks they like and can't stand, the never word | `setup-visual-identity`, before it builds or tunes the look |
| A topic you won't touch, a client you'll never name, a word you hate | The stop list session of the interviews |
| Language | Not asked: the studio writes in the language of their material, and asks only if the material mixes languages |

The converter still reads the old questions, so an older form or a CSV from one still builds a studio.

## Getting a submission into a studio

The automation does it (`docs/automation.md`). By hand: download the submission from Tally as a CSV and run `bash scripts/make-client.sh <file>.csv --email their@email.com`.
