---
name: job-end
description: Closes a working session in two minutes. Writes what got made, what the person decided and what's waiting to sessions/log.md, runs /learn's list of choices to keep, offers to save a routine as a recipe when one has shown up in three sessions, and saves. Use for /end, "I'm done for today", "let's wrap up", "close the session".
---

# /end

The studio saves files on its own (a hook commits after every reply and writes a line to `sessions/log.md` saying which files changed). What it can't write on its own is what the session meant: what you decided, what you'd do differently, what's waiting on you. This skill writes that down, so next session starts from it instead of from zero, and so the librarian can count it.

## Procedure

1. **Say the session back in three lines**, in plain words, and ask if that's right:
   - Made: the pieces, canon entries, visuals or strategy files that changed this session (read the day's lines in `sessions/log.md` and `git log --since="<today> 00:00" --stat`; the hook commits after every reply, so the day's work is in the commits, not in the working tree).
   - Decided: the choices the person made out loud (a move picked, a line cut, a proposal answered, a direction set).
   - Waiting: what the person said they'd do, and what the studio needs from them (a scene for a brief, a yes on a proposal, a file for the inbox).
2. **Run `skills/job-learn`** on the session: the voice rules, vocabulary, facts, samples and rewrites worth keeping, each with a yes or no. Rewrite pairs are written without asking, as that skill says.
   Then run `python3 scripts/rewrites.py tally --since <today>` and say its first line as it prints, when there were rewrites today: "3 rewrites, 7 changes: 4 broke a rule the reviews missed, 2 are new, 1 was about the piece only." The first number says whether the checks catch what the person catches; the second says whether they're still teaching the studio something new. Over a few weeks the first should fall toward zero. No rewrites, no line.
3. **Offer a recipe, when a routine has shown up.** Follow `skills/job-recipes`, "Offering a recipe": if the same chain of commands, with the same choices, ran in three separate sessions (today's included), offer to save it as one command. At most one offer; nothing when no chain qualifies, and nothing when nobody is there to answer. Requests about how a studio skill works go to `studio-notes.md`, never into the skill.
4. **Write the session entry** to `sessions/log.md` under a `## <date>` heading: the three lines from step 1 as the person corrected them, then one line per item `/learn` kept and where it went, then the tally line if there was one, then one `ran:` line, then the recipe line if step 3 offered one (`recipe saved: <name>` or `recipe declined: <the chain>`). Keep it to twelve lines. The hook's own "changed:" lines stay where they are.
   The `ran:` line lists the commands the session chained, in order, each with the person's choices in a few of their words: `ran: /sources (pull Thursday client call) → /shape → /post (short, skip visual)`. A recipe run is written as `ran: /<recipe name>`. A session that ran one command or none writes `ran: /<command>` or nothing. This line is what step 3 counts next time, so write what happened, not a tidier version.
5. **Say what's next in one line**, from the waiting list: the first thing to do when they come back.
   **Sync Notion on the connector route.** If `config/tools.md` says `route: connector` under Notion and this session changed pieces, ideas, proposals or the canon, run the sync in `skills/setup-notion` ("Keeping it in sync"): `python3 scripts/sync-notion.py --dump`, apply it through the Notion tools, then read the person's decisions and answers back into `pieces/_decisions.md`. The token route needs nothing here; the stop hook syncs it.
6. **Save with a message:** `bash scripts/save.sh "Session <date>: <three words>"`, the three words naming what the session was about. The stop hook would save anyway; doing it here gives the commit a name the person can find, with the session entry in it. In the studio's own repo (no `studio-source.md`) the script saves nothing and says so; commit the session entry and the files `/learn` wrote by hand, on the current branch, and push nothing.

## Rules

- Never write a decision the person didn't make. "Waiting" lists what they said, not what the studio wants.
- Never skip step 2 by writing the lessons yourself; `/learn` asks for the yes.
- Never save a recipe without the person's yes on what will be saved, and never offer one the log says they declined.
- An empty session ("nothing decided, nothing waiting") is a fine entry. One line.
- `sessions/` belongs to the person; an update never touches it.
