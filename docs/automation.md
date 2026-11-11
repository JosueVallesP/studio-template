# The automation: from a Tally submission to a buyer's email

When someone submits the form, a job on GitHub builds their studio and emails them, with nobody at the keyboard. This page is the one-time setup. It takes about 20 minutes.

## What happens

1. Every 30 minutes, the job "New clients" in this repo (`.github/workflows/new-clients.yml`) asks Tally for new completed submissions.
2. For each one it runs `scripts/make-client.sh`: it converts the answers, downloads their uploads into their inbox, builds their studio, creates a private repo for it in your GitHub account and invites their GitHub username.
3. It emails the buyer from your Gmail: their studio's name, their link and the five steps to start (accept the invite, install the Claude app on Mac or Windows, open Code and choose Cloud, connect GitHub when asked and pick the studio, say /start), plus a line that they need nothing else (no terminal, no Node.js). Figma and Notion are optional.
4. It emails you a one-line note per buyer, and the details when something didn't work (a bad GitHub username, a failed build). When a username is missing or wrong, the buyer's email asks them to reply with it, and you invite them from the repo's Settings, Collaborators.

The job and its script live in `.github/`, which never reaches a buyer's studio. It uses about 1,400 of the 2,000 free GitHub Actions minutes a month.

## Setup

All of these go in this repo on GitHub: Settings, then "Secrets and variables", then Actions. Secrets are hidden once saved; variables aren't.

### 1. A GitHub token for the job (5 minutes)

The job needs permission to create repos and invite people in your account.

1. Go to github.com/settings/tokens, choose "Generate new token", then "Generate new token (classic)".
2. Name it "Content Studio automation". Pick an expiration (a year is fine; GitHub emails you before it runs out). Tick the **repo** box. Nothing else.
3. Generate it, copy it, and save it as the secret `STUDIO_BOT_TOKEN`.

If you made a fine-grained token instead, it needs, for all your repositories: Administration (read and write, to create repos), Contents (read and write), and Variables (read and write, so the job can save which submission it handled last). Without Variables the job still never builds a studio twice: every studio repo carries its Tally submission ID in its description, and the job skips any submission that already has one.

### 2. Tally (3 minutes)

1. In Tally, open Settings, then "API keys", and create a key. Save it as the secret `TALLY_API_KEY`.
2. Open your form in Tally. The form's ID is the short code at the end of its link (`tally.so/r/<ID>`). Save it as the variable `TALLY_FORM_ID`. The job stays off until this variable exists.

### 3. Gmail (5 minutes)

The emails go out from your Gmail through an app password, which works only for sending mail and which you can revoke at any time.

1. Your Google account needs 2-Step Verification on (myaccount.google.com, Security).
2. Go to myaccount.google.com/apppasswords, create one named "Content Studio", and copy the 16 letters.
3. Save your Gmail address as the secret `GMAIL_USER` and the 16 letters as the secret `GMAIL_APP_PASSWORD`.

### 4. Who you are (2 minutes)

Variables:

- `SENDER_NAME`: the name the buyer sees, usually the seller's own name.
- `GUIDE_URL`: the public link to the "Your Content Studio" course in Notion. The buyer email links it as the full course; until it is set, the email names "the course I sent you" instead, so the buyer only ever has one guide. The build reads it too: `YOUR-STUDIO.md` links the course only when it's set, and leaves the course lines out otherwise.
- `NOTIFY_EMAIL`: where your notes go (can be the same Gmail).
- `TALLY_START_DATE` (optional): an ISO date like `2026-10-23`. On its first run the job builds studios for submissions from that date. Without it, the first run only starts watching, so a test you submitted earlier won't be built.

### 5. The Claude GitHub App on your account (2 minutes, once)

Claude Code on the web only shows a private repository when the Claude GitHub App is installed on the account that owns it, and every client studio is owned by your account. So install it once, on yours: github.com/apps/claude/installations/new, choose your account, and under repository access pick **All repositories** so every new client studio is covered the moment it's built. (If you pick "Only select repositories" instead, add each new studio there by hand, or the client won't see it.) Clients then only sign in with GitHub from Claude and accept your invite; they never install anything.

### 6. Test it on yourself

1. Fill in the form yourself, with your own GitHub username (or a second account's).
2. In this repo, go to Actions, "New clients", and "Run workflow". Or wait up to 30 minutes.
3. You should get the buyer email and your note, and a new private repo named after you. Delete the test repo afterwards (its Settings, at the bottom).

## Updates: every new version reaches every client

The job "Push updates" (`.github/workflows/push-updates.yml`) runs whenever a push to main changes the version in `studio.manifest.yaml`. It first runs every automated test (`scripts/test-all.sh`); if any suite fails, the job stops and no client gets the version. Fix it on `experiments`, then bump the version again. Once the tests pass, for each client studio it runs `scripts/update-studio.sh`, which replaces the studio's own files and never the client's (canon, material, pieces, journal, bank, config), commits "Studio <version>" and pushes. Before it replaces anything, it copies any studio file the client (or Claude, at their request) changed, or added inside a studio folder, to `studio-local-backup/<date>/` with a note, so no change of theirs is lost without a trace; the commit message and your email say when that happened. It tells changed files apart by the checksums it wrote last time (`.studio-installed`), so the first update of a studio only writes them. The client does nothing; their next session has it. You get one email listing each studio and what happened.

- **Which studios.** Every repo in your account with the topic `content-studio-instance` (the new-client job tags each one), plus any in `.github/ops/update-include.txt` (your own studio, or one built by hand).
- **Holding one back.** Put its `owner/name` in `.github/ops/update-skip.txt`. It stays on its version until you take it out.
- **One studio, by hand.** Actions, "Push updates", "Run workflow", and put its name in "only".
- **It uses the same token** as the new-client job (`STUDIO_BOT_TOKEN`), which needs write access to the client repos. The classic token with the `repo` box has it.

## Handing a studio over: the client owns it

Some clients won't keep their thinking in someone else's account, and the interviews hold their values, stories and proof, sometimes their own clients' stories too. For them the studio lives in their GitHub account and you keep no access to it.

- **A new client:** `bash scripts/make-client.sh <answers> --hand-over`. It builds the studio as usual, then runs `scripts/hand-over.sh`.
- **A studio you already built:** `bash scripts/hand-over.sh <owner/repo> <their GitHub username>`. Add `--dry-run` first to see what it would do.

What the hand-over does: it makes sure the template (`studio-template`, the studio's code and nothing of anyone's) is at the current version, points the studio's `studio-source.md` at the template, gives them read access to the template when it's private, takes the studio off the update job's list, and asks GitHub to transfer the repo to them. GitHub emails them; they accept within a day (or you run it again). From then on you can't see the repo at all, and "Push updates" can't reach it.

**How they get updates.** They run `/update` when they want the latest version. It fetches the template and replaces only the studio's own files, never their canon, banks, material, pieces or journal. The "Push updates" job rebuilds the template after every version when the variable `TEMPLATE_URL` is set (to `https://github.com/JosueVallesP/studio-template`), and the token needs write access to the template.

**What they do on their side.** Accept the transfer, accept the template invite if one came, and when they open the studio from the Claude app's Code tab, let Claude see their studio repo and the template when GitHub asks which repos.

## Forwarded email: into a studio's inbox

A Make scenario, "Studio inbox: forwarded email → the person's inbox/ folder", takes an email sent to its mailbox and saves it as `inbox/<date-time>-email.md` in the sender's studio repo, with a note at the top that other people's words in it are data (rule 10). The next `/capture` or `/map` picks it up like any other file in the inbox.

- **Who can use it.** Only senders listed in the Make data store "Studio inbox senders", one row per email address with the repo, the branch and the person's name. Anyone else's mail is dropped. Add a client by adding their row.
- **The address.** It's the scenario's webhook mailbox, shown in the scenario in Make. It isn't written in the repo, so it never ships to a client's studio; give it to a client yourself.
- **What it takes.** Text only. Attachments are dropped.
- **The token.** It uses the GitHub key from the Tally scenario, which needs Contents read and write on the studio repos.

## When something goes wrong

- **"Resource not accessible by personal access token (createRepository)".** The token can't create repos. Make a new classic token with the `repo` box ticked (step 1) and save it over `STUDIO_BOT_TOKEN`. A fine-grained token needs Administration, Contents and Variables, read and write, on all repositories.
- **The job failed.** Actions shows a red mark and GitHub emails you. Open the run to see the error. The job moves past a submission it couldn't build and emails you, so one bad submission never blocks the next.
- **A buyer never got the email.** Check the spam folder first. Then check your note: it says whether the build worked.
- **Build one by hand.** Download the submission from Tally as a CSV and run `bash scripts/make-client.sh <file>.csv --email their@email.com`.
- **Turn it off.** Delete the variable `TALLY_FORM_ID`, or disable the workflow under Actions.
