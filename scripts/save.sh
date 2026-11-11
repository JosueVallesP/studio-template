#!/usr/bin/env bash
# Saves the person's work: commits everything changed in the instance, writes one line per commit to
# sessions/log.md (date, time, the files in the commit), and pushes when a remote exists. The stop
# hook runs it after every reply, and /end runs it once with a message, so the person never types git.
#   bash scripts/save.sh ["commit message"]
# Silent and harmless when the folder isn't a git repo or nothing changed.
# A file over 50 MB is never committed (GitHub refuses it, and one such file would block every later
# push); it stays on disk, unstaged, and the save says so. When a save doesn't reach GitHub, it writes
# one line to .claude/.save-failed (gitignored); session-start.sh shows it at the next session, and the
# next save that does reach GitHub deletes it.
cd "$(dirname "${BASH_SOURCE[0]}")/.."
# In the studio's master repo (studio.manifest.yaml present, studio-source.md absent) it saves nothing:
# adding everything would sweep in work that isn't ready, and the push below would land the current
# branch on the master's main. Every instance carries studio-source.md, so instances still save.
if [ -f studio.manifest.yaml ] && [ ! -f studio-source.md ]; then
  echo "not saved: this is the studio's own repo, so nothing is committed or pushed on its own. Commit the files you mean by hand."
  exit 0
fi
git rev-parse --is-inside-work-tree >/dev/null 2>&1 || exit 0
marker=.claude/.save-failed
failed() { mkdir -p .claude; printf '%s · %s\n' "$(date '+%Y-%m-%d %H:%M')" "$1" > "$marker"; }
# A git step left half done (a rebase or merge cut off when the stop hook ran out of time, or a clash
# git couldn't settle) leaves files with conflict markers in them. Saving then would commit and push
# those files as they are, so the save stops instead, and the next session start says so in plain
# words. The fix is a git job; the person shouldn't have to do it.
gitdir="$(git rev-parse --git-dir 2>/dev/null)"
stuck=""
[ -d "$gitdir/rebase-merge" ] || [ -d "$gitdir/rebase-apply" ] && stuck="an update from GitHub was cut off halfway"
[ -z "$stuck" ] && [ -f "$gitdir/MERGE_HEAD" ] && stuck="a merge was left halfway"
[ -z "$stuck" ] && [ -n "$(git diff --name-only --diff-filter=U 2>/dev/null)" ] && stuck="two versions of a file clashed and weren't settled"
if [ -z "$stuck" ]; then
  clash="$(git ls-files -m -o --exclude-standard -z 2>/dev/null | python3 -I -c '
import sys, re
names = [n for n in sys.stdin.buffer.read().decode("utf-8", "replace").split("\0") if n]
hit = []
for n in names:
    try:
        t = open(n, encoding="utf-8", errors="replace").read(400000)
    except OSError:
        continue
    if re.search(r"^<{7} .*$\n(?:.*\n)*?^={7}$\n(?:.*\n)*?^>{7} ", t, re.M):
        hit.append(n)
print(" ".join(hit[:5]))')"
  [ -n "$clash" ] && stuck="these files still hold both sides of a clash: $clash"
fi
if [ -n "$stuck" ]; then
  failed "nothing was saved: $stuck. Ask Claude to sort out the git clash before anything else"
  echo "not saved: $stuck"
  exit 0
fi
git add -A >/dev/null 2>&1
# Unstage anything over 50 MB and name it.
big="$(git diff --cached --name-only -z --diff-filter=AM | python3 -I -c '
import os, sys
names = [n for n in sys.stdin.buffer.read().decode("utf-8", "replace").split("\0") if n]
print("\n".join(n for n in names if os.path.isfile(n) and os.path.getsize(n) > 50 * 1024 * 1024))')"
if [ -n "$big" ]; then
  while IFS= read -r f; do
    [ -n "$f" ] && { git reset -q -- "$f" >/dev/null 2>&1 || git rm -q --cached -- "$f" >/dev/null 2>&1; }
  done <<< "$big"
  failed "left out of the save because it's over 50 MB: $(echo "$big" | tr '\n' ' ')(move it out of the studio folder, or keep the text version only)"
  echo "not saved to GitHub (over 50 MB): $(echo "$big" | tr '\n' ' ')"
fi
if git diff --cached --quiet; then exit 0; fi
# A password, API key or token in what's about to be saved stops the save: once it's pushed, it stays in
# GitHub's history, and taking it out needs git surgery. Nothing is committed; the next session start
# tells the person which file and what kind of key, never the key itself (scripts/scan-secrets.py).
if [ -f scripts/scan-secrets.py ]; then
  keys="$(python3 -I scripts/scan-secrets.py 2>/dev/null)"
  if [ -n "$keys" ]; then
    git reset -q >/dev/null 2>&1
    failed "nothing was saved: something that looks like a password or key is in $(echo "$keys" | tr '\n' ' ' | sed 's/ *$//'). Move it into .env (or delete it), and change the key if it was ever shared"
    echo "not saved: something that looks like a password or key is in $(echo "$keys" | tr '\n' ' ')"
    exit 0
  fi
fi
# The files in this commit, read NUL-separated so names with spaces stay whole. The log file itself
# isn't listed as a change.
files="$(git diff --cached --name-only -z | python3 -I -c '
import sys
names = [n for n in sys.stdin.buffer.read().decode("utf-8", "replace").split("\0") if n and n != "sessions/log.md"]
print(" ".join(names[:20]) + (f" and {len(names) - 20} more" if len(names) > 20 else ""))')"
if [ -n "$files" ]; then
  mkdir -p sessions
  [ -f sessions/log.md ] || printf '# Sessions\n\nOne line per save: date, time, what changed. `/end` adds what was decided.\n\n' > sessions/log.md
  printf -- '- %s · changed: %s\n' "$(date '+%Y-%m-%d %H:%M')" "$files" >> sessions/log.md
  git add sessions/log.md >/dev/null 2>&1
fi
msg="${1:-Studio session $(date +%Y-%m-%d\ %H:%M)}"
git -c user.name="${GIT_AUTHOR_NAME:-Content Studio}" -c user.email="${GIT_AUTHOR_EMAIL:-studio@local}" commit -q -m "$msg" || exit 0
# Never push to the studio's own repo (the template a person cloned from, or the master): a fresh
# clone's origin is the template, and a person's files must never land there. setup-start renames
# that remote to "template"; this check holds even if it hasn't run yet.
studio_url="$(grep -m1 '^- studio:' studio-source.md 2>/dev/null | sed 's/^- studio: *//; s/\.git$//')"
origin_url="$(git remote get-url origin 2>/dev/null | sed 's/\.git$//')"
if [ -n "$origin_url" ] && [ "$origin_url" = "$studio_url" ]; then
  git remote rename origin template >/dev/null 2>&1
  echo "saved locally. This folder's origin was the studio template, so it was renamed to 'template' and nothing was pushed; say \"back up my studio\" to set up your own backup."
  exit 0
fi
if git remote get-url origin >/dev/null 2>&1; then
  # Always save to the repo's main branch, whatever branch this session is on. Claude Code on the web
  # gives each session its own branch; pushing only that branch would hide the work from the next
  # session, which starts from main. If main moved (an update, another session), rebase onto it first.
  default="$(git symbolic-ref -q --short refs/remotes/origin/HEAD 2>/dev/null | sed 's#^origin/##')"
  [ -n "$default" ] || default="$(git ls-remote --symref origin HEAD 2>/dev/null | sed -n 's#^ref: refs/heads/\([^[:space:]]*\).*#\1#p')"
  [ -n "$default" ] || default=main
  if git push -q origin "HEAD:$default" 2>/dev/null; then rm -f "$marker"
  elif git pull -q --rebase origin "$default" 2>/dev/null && git push -q origin "HEAD:$default" 2>/dev/null; then rm -f "$marker"
  else
    git rebase --abort >/dev/null 2>&1
    branch="$(git rev-parse --abbrev-ref HEAD 2>/dev/null)"
    if git push -q -u origin HEAD 2>/dev/null; then
      failed "the work went to the branch $branch on GitHub, not to $default (the two had changes that clash); the next session starts from $default and won't see it until they're merged"
    else
      failed "the save to GitHub failed (offline, no access, or a file GitHub refused); the work is committed on this computer only"
    fi
    echo "saved locally; the save to GitHub's $default branch failed (offline, no access, or a clash). It will go with the next save."
  fi
fi
# A file left out for size is shown at the next session too, so it isn't lost track of.
[ -n "$big" ] && failed "left out of the save because it's over 50 MB: $(echo "$big" | tr '\n' ' ')(move it out of the studio folder, or keep the text version only)"

echo "saved"
