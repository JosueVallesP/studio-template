#!/usr/bin/env bash
# SessionStart hook: puts the studio's state in front of Claude before the first prompt, so nobody
# has to ask "where are we". Prints the facts behind /status (counts, states, open proposals), what's
# in inbox/, and the last session line. Reads files and counts; judges nothing.
cd "${CLAUDE_PROJECT_DIR:-$(dirname "${BASH_SOURCE[0]}")/../..}" || exit 0

# Start from the latest saved work: earlier sessions and studio updates land on the main branch.
# Fast-forward only, silent, never touches uncommitted work.
if git rev-parse --is-inside-work-tree >/dev/null 2>&1 && git remote get-url origin >/dev/null 2>&1; then
  d="$(git symbolic-ref -q --short refs/remotes/origin/HEAD 2>/dev/null | sed 's#^origin/##')"; [ -n "$d" ] || d=main
  git fetch -q origin "$d" 2>/dev/null && git merge -q --ff-only "origin/$d" >/dev/null 2>&1
fi

# First visit: a person's studio (studio-source.md present) whose setup-progress has no "welcomed:"
# line yet. Claude can't speak before the person does, so this asks the first reply, whatever they
# typed, to open with the welcome in docs/welcome.md. The studio's master repo never sees it.
if [ -f studio-source.md ] && [ -f docs/welcome.md ] && ! grep -q '^welcomed:' canon/setup-progress.md 2>/dev/null; then
  echo "=== FIRST VISIT ==="
  echo "This person hasn't been welcomed yet. Your first reply in this session, whatever they typed (even \"hi\"),"
  echo "opens with the welcome in docs/welcome.md: read it and say it as written, with only the changes its"
  echo "top note allows (their name and step 1 done if config/intake.yaml exists; drop a tool they don't use)."
  echo "If they asked something, answer it after the welcome in the same reply. Then, if canon/setup-progress.md"
  echo "exists, add \"welcomed: $(date +%Y-%m-%d)\" to its frontmatter so it shows once. If it doesn't exist yet,"
  echo "setup-intake adds the line when it creates the file; until then the welcome shows each session."
  echo
fi

echo "=== STUDIO STATE ($(date '+%Y-%m-%d %A')) ==="
# The last save didn't reach GitHub (scripts/save.sh writes this line and deletes it after a save that does).
if [ -s .claude/.save-failed ]; then
  echo "SAVE: the last save didn't reach GitHub: $(head -n 1 .claude/.save-failed)"
  echo "  Tell the person in one line near the start of your first reply, in plain words, and offer to sort it out."
fi
# A dashboard sync that failed (on-stop.sh writes the line; the next sync that works deletes it).
for f in .claude/.sync-failed-dashboard .claude/.sync-failed-notion; do
  [ -s "$f" ] || continue
  which="dashboard app"; [ "$f" = .claude/.sync-failed-notion ] && which="Notion dashboard"
  echo "SYNC: the $which didn't update after the last reply: $(head -n 1 "$f")"
  echo "  Tell the person in one line near the start of your first reply that their $which may be out of date, and offer to sort it out (skills/setup-notion or skills/setup-dashboard, the sync step)."
done
# A new studio version arrived since the last check (pushed into a built-for-you studio, or /update):
# run the install check once and show only what needs the person. The version checked is kept in
# sessions/, which the save commits, so a Cloud session that starts from a fresh copy still knows.
if [ -f studio-source.md ] && [ -f scripts/setup-check.sh ]; then
  cur="$(grep -m1 '^- version:' studio-source.md | awk '{print $3}')"
  last="$(cat sessions/.checked-version 2>/dev/null)"
  # The first session ever (nothing checked yet) or one before the intake has run only records the
  # version: setup has its own check (/check) and a half-built studio would read as broken.
  if [ -n "$cur" ] && { [ -z "$last" ] || [ ! -f canon/setup-progress.md ]; }; then
    mkdir -p sessions && printf '%s\n' "$cur" > sessions/.checked-version
  elif [ -n "$cur" ] && [ "$cur" != "$last" ]; then
    probs="$(bash scripts/setup-check.sh 2>/dev/null | grep -E '^  (FAIL|warn) ' | grep -v 'API_KEY\|NOTION_TOKEN' | head -10)"
    mkdir -p sessions && printf '%s\n' "$cur" > sessions/.checked-version
    if [ -n "$probs" ]; then
      echo "AFTER UPDATE ($last -> $cur): the studio checked itself and found:"
      printf '%s\n' "$probs"
      echo "  After the person's first message is handled, and never inside a guided flow, tell them in one line"
      echo "  per problem what it means and what fixes it, in plain words (no file paths unless they ask), and offer"
      echo "  to make the safe fixes: running /tidy, or the step a FAIL line names. Never change their canon, material"
      echo "  or pieces to make a check pass."
    else
      echo "AFTER UPDATE ($last -> $cur): the studio checked itself; nothing needs the person."
    fi
  fi
fi

if [ -x scripts/status.sh ] || [ -f scripts/status.sh ]; then
  bash scripts/status.sh 2>/dev/null | head -60
fi

# Where the studio runs decides how the person hands over files (docs/handing-things-over.md).
if [ "${CLAUDE_CODE_REMOTE:-}" = "true" ]; then
  echo "WORKSPACE: cloud (the person's studio folders aren't on their computer: files come in through the chat or GitHub's upload page, never a folder they open; see docs/handing-things-over.md)"
else
  echo "WORKSPACE: local (their studio is a folder on their computer; inbox is a folder inside it they can open; see docs/handing-things-over.md)"
fi

if [ -d inbox ]; then
  n=$(find inbox -maxdepth 1 -type f ! -name 'README.md' 2>/dev/null | wc -l | tr -d ' ')
  if [ "$n" -gt 0 ]; then echo "INBOX: $n file(s) waiting for /capture"; fi
fi

# Drafts a librarian run (often a scheduled one, nobody present) listed for the canon and nobody has added yet.
# One entry is a ### heading or a top-level "- " line under "## Drafts to add"; "added <date>" marks one done.
if [ -f pieces/librarian-last-run.md ]; then
  n=$(awk 'function flush() { if (h && !a) c++; h=0; a=0 }
           /^## / {flush(); f=($0 ~ /^## Drafts to add/); next}
           f && /^### / {flush(); h=1; a=($0 ~ /added [0-9]/); next}
           f && /^- / && !h {if ($0 !~ /added [0-9]/) c++; next}
           f && h && /added [0-9]/ {a=1}
           END {flush(); print c+0}' pieces/librarian-last-run.md)
  if [ "$n" -gt 0 ]; then echo "LIBRARIAN: $n draft(s) from the librarian waiting to be added (say /status)"; fi
fi

if [ -f sessions/log.md ]; then
  echo "LAST SESSION:"
  tail -n 4 sessions/log.md | sed 's/^/  /'
fi

if bash scripts/status.sh 2>/dev/null | grep -q 'review ready, not shown yet'; then
  echo "READY TO SHOW: a piece above has its review but the person hasn't seen it. Show it after the person's first"
  echo "message is handled, in one line with an offer, and never in the middle of a guided flow (CLAUDE.md rule 9)."
fi
echo "Say /status for the full picture, /coach for what to do, /end before you leave."
exit 0
