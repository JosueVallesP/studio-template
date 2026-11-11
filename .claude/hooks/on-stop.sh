#!/usr/bin/env bash
# Stop hook: when Claude finishes a reply, save the work. Runs scripts/save.sh first, which commits,
# appends one line to sessions/log.md (date, time, the files in the commit) and pushes, so a slow
# dashboard can't use up the hook's time before the save. Then it mirrors to the dashboards when
# they're connected. Silent when nothing changed. Never blocks; always exits 0. A save that didn't
# reach GitHub leaves .claude/.save-failed, which session-start.sh shows at the next session.
# In the studio's master repo (studio.manifest.yaml present, studio-source.md absent) it does nothing,
# so the master never commits or pushes on its own.
cd "${CLAUDE_PROJECT_DIR:-.}" 2>/dev/null || exit 0
[ -f studio.manifest.yaml ] && [ ! -f studio-source.md ] && exit 0
git rev-parse --is-inside-work-tree >/dev/null 2>&1 || exit 0
[ "$(git status --porcelain -z 2>/dev/null | head -c1 | wc -c)" -eq 0 ] && exit 0
bash scripts/save.sh >/dev/null 2>&1 || true
# Each sync gets at most 50 seconds where `timeout` exists (macOS has none by default; then it runs as is).
limit=""; command -v timeout >/dev/null 2>&1 && limit="timeout 50"
# A sync that isn't set up exits quietly with 0. One that fails leaves a line in .claude/.sync-failed-<name>
# (gitignored) with the reason, and session-start.sh tells the person at the next session, the same way it
# reports a save that didn't reach GitHub; the next sync that works deletes the line. Without it a dashboard
# that stopped updating would keep showing old stages and old "waiting on you" lists as if they were current.
run_sync() {
  name="$1"; marker=".claude/.sync-failed-$name"
  out="$(STUDIO_QUIET=1 $limit python3 "scripts/sync-$name.py" 2>&1)"; code=$?
  if [ "$code" -eq 0 ]; then rm -f "$marker"; return; fi
  if [ "$code" -eq 124 ]; then why="took longer than 50 seconds and was stopped"
  else why="$(printf '%s\n' "$out" | grep -v '^\s*$' | tail -n 1 | cut -c1-240)"; fi
  mkdir -p .claude; printf '%s · %s\n' "$(date '+%Y-%m-%d %H:%M')" "${why:-stopped with no message}" > "$marker"
}
run_sync dashboard
run_sync notion
exit 0
