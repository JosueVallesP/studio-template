#!/usr/bin/env bash
# The install half of setup-check: is this instance complete and healthy? Prints one line per
# check, ok or FAIL, and exits 1 on any FAIL. The skill (skills/setup-check) runs this first, then
# the part a script can't do: one test piece through the whole crew.
#
# Run from the instance root: bash scripts/setup-check.sh

set -uo pipefail
cd "$(dirname "${BASH_SOURCE[0]}")/.."
fails=0
ok()   { echo "  ok    $1"; }
fail() { echo "  FAIL  $1"; fails=$((fails+1)); }
check_file() { [ -f "$1" ] && ok "$1" || fail "$1 missing"; }
check_dir()  { [ -d "$1" ] && ok "$1/" || fail "$1/ missing"; }

echo "STUDIO FILES"
for f in CLAUDE.md README.md studio.manifest.yaml templates/piece/brief.md templates/piece/draft.md templates/piece/review.md templates/piece/log.md templates/piece/final.md templates/piece/index.md templates/piece/shortlist.md templates/proposals.md templates/inbox/README.md templates/material/README.md docs/operating-guide.md docs/strategy-method.md; do check_file "$f"; done
# Every skill folder must hold its SKILL.md, and every skill CLAUDE.md routes to must exist.
for d in skills/*/; do s="$(basename "$d")"; [ -f "skills/$s/SKILL.md" ] && ok "skills/$s" || fail "skills/$s/SKILL.md missing"; done
for s in $(grep -o '`skills/[a-z0-9-]*' CLAUDE.md 2>/dev/null | sort -u | sed 's#^`skills/##'); do
  [ -f "skills/$s/SKILL.md" ] || fail "skills/$s/SKILL.md missing (CLAUDE.md routes to it)"
done
for a in capture writer librarian judge; do [ -f ".claude/agents/$a.md" ] && ok "agent $a" || fail "agent $a missing"; done
# The commands are the .claude/skills/ entries the manifest lists as the studio's.
for c in $(sed -n 's#^  - \.claude/skills/\([^/]*\)/$#\1#p' studio.manifest.yaml); do [ -f ".claude/skills/$c/SKILL.md" ] && ok "/$c" || fail "/$c missing"; done

echo "SCRIPTS"
for s in scripts/*.py scripts/*.sh; do check_file "$s"; done
if command -v python3 >/dev/null; then
  if python3 -c 'import sys; sys.exit(0 if sys.version_info >= (3, 8) else 1)' 2>/dev/null; then
    ok "python3 $(python3 --version 2>&1 | awk '{print $2}')"
  else
    fail "python3 $(python3 --version 2>&1 | awk '{print $2}') is too old: the scripts need 3.8 or newer"
  fi
else
  fail "python3 not found"
fi
python3 -c "import re,json,statistics" 2>/dev/null && ok "python modules" || fail "python modules"
bash scripts/status.sh >/dev/null 2>&1 && ok "status.sh runs" || fail "status.sh errors"

echo "MANIFEST"
v="$(grep -m1 '^version:' studio.manifest.yaml | awk '{print $2}')"
[ -n "$v" ] && ok "studio version $v" || fail "no version in manifest"
if [ -f studio-source.md ]; then
  sv="$(grep -m1 '^- version:' studio-source.md | awk '{print $3}')"
  [ "$sv" = "$v" ] && ok "studio-source.md matches ($sv)" || fail "studio-source.md says $sv, manifest says $v: run /update"
else
  ok "no studio-source.md (this is the studio repo itself, not an instance)"
fi
for p in canon bank pieces config inbox; do check_dir "$p"; done
grep -q "^  - canon/" studio.manifest.yaml && ok "canon/ is client-owned in the manifest" || fail "canon/ not listed as client-owned"

echo "PERSON"
stage=""
if [ -f canon/setup-progress.md ]; then
  stage="$(grep -m1 '^stage:' canon/setup-progress.md | cut -d' ' -f2-)"
  ok "setup-progress.md (stage: $stage)"
else
  fail "canon/setup-progress.md missing: intake hasn't run (say /start)"
fi
# Before the check stage, the canon and strategy checks below are expected to be incomplete.
# Report them as "not yet" and don't count them as failures, so /check never reads as broken.
early=0
case "$stage" in
  "quick wins"*|"brand tree"*|"strategy"*|"make it yours"*|"ready for a first piece"*|"first piece in progress"*|"") early=1 ;;   # the last two: older instances
esac
# Interviews skipped (stage "interviews-skipped", or a brand_tree: skipped line): the person works through
# the job commands, which need material, not the minimum canon. The canon checks become notes.
skipped=0
case "$stage" in "interviews-skipped"*|"interviews skipped"*) skipped=1 ;; esac
grep -q '^brand_tree: skipped' canon/setup-progress.md 2>/dev/null && [ ! -f canon/progress.md ] && skipped=1
soft() { if [ "$early" = 1 ] || [ "$skipped" = 1 ]; then echo "  not yet  $1"; else fail "$1"; fi; }
if [ "$skipped" = 1 ]; then
  if find material inbox -type f ! -name README.md 2>/dev/null | grep -q .; then ok "interviews skipped: material to write from is in material/ or inbox/"
  else echo "  note  interviews skipped and material/ and inbox/ are empty: the job commands need something of yours to write from"; fi
fi
if [ -f canon/progress.md ]; then
  total="$(grep -cE '^- \[[ x]\]' canon/progress.md)"; done_="$(grep -c '^- \[x\]' canon/progress.md)"
  [ "$done_" = "$total" ] && [ "$total" -gt 0 ] && ok "minimum canon complete ($done_/$total)" || soft "minimum canon $done_/$total"
else
  soft "canon/progress.md: the brand tree interview hasn't started"
fi
for f in config/intake.yaml YOUR-STUDIO.md canon/visual/brand-assets.md canon/strategy/outcomes.md config/tools.md proposals.md; do check_file "$f"; done
for f in canon/canon-index.md canon/core-summary.md bank/ideas.md bank/credibility.md bank/evidence.md; do [ -f "$f" ] && ok "$f" || soft "$f: written by the interview"; done
for f in canon/strategy/brand-strategy.md canon/strategy/content-plan.md; do
  # only the frontmatter's status counts; entries inside the file (segments, "Known for") carry their own status lines
  # "In use" is status: confirmed (strategy-brand) or a person_confirmed: line (/strategy), as setup-start reads it.
  if [ -f "$f" ]; then
    fm="$(awk 'NR==1&&/^---$/{f=1;next} f&&/^---$/{exit} f' "$f")"
    if printf '%s\n' "$fm" | grep -q '^status: confirmed'; then ok "$f confirmed"
    elif printf '%s\n' "$fm" | grep -q '^person_confirmed: *[0-9]'; then ok "$f in use (person_confirmed)"
    else soft "$f not confirmed yet"; fi
  else soft "$f: written by the strategy"; fi
done
ls canon/strategy/channels/*.md >/dev/null 2>&1 && ok "channel files: $(ls canon/strategy/channels/*.md | wc -l)" || soft "channel files: written by the strategy"
if [ -f canon/voice/voice-guide.md ]; then
  # Only the person's own rules count: a W rule whose status line says default is the studio's starting set.
  n="$(awk '/^(###? |- )W[0-9]+/{if(h&&st!~/^status: default/)n++; h=1; st=""; next} /^##? /{if(h&&st!~/^status: default/)n++; h=0; next} h&&/^status:/{st=$0} END{if(h&&st!~/^status: default/)n++; print n+0}' canon/voice/voice-guide.md)"
  [ "$n" -ge 3 ] && ok "voice guide has $n rules of the person's own" || soft "voice guide has $n rules of the person's own (needs 3 before the check; the default rules don't count)"
else soft "canon/voice/voice-guide.md: written by the interview"; fi

echo "KEYS"
# A connected tool's key must be in the environment (Claude Code on the web: the cloud environment's
# variables) or in .env (on a computer). A missing key is a warning, not a FAIL: the sync stays quiet without it.
has_key() { [ -n "${!1:-}" ] || grep -q "^$1=." .env 2>/dev/null; }
section_connected() { awk -v s="## $1" '$0==s{f=1;next} /^## /{f=0} f&&/^- connected: yes/{print "yes"}' config/tools.md 2>/dev/null | grep -q yes; }
route_token() { awk '$0=="## Notion"{f=1;next} /^## /{f=0} f&&/^- route: token/{print "yes"}' config/tools.md 2>/dev/null | grep -q yes; }
warned=0
if section_connected Notion && route_token && ! has_key NOTION_TOKEN; then echo "  warn  Notion is connected by token but NOTION_TOKEN isn't set (environment or .env)"; warned=1; fi
if section_connected Dashboard && ! has_key BASE44_API_KEY; then echo "  warn  the dashboard is connected but BASE44_API_KEY isn't set (environment or .env)"; warned=1; fi
if ! has_key PANGRAM_API_KEY; then echo "  warn  PANGRAM_API_KEY isn't set (environment or .env): the detector reading will say \"not run\""; warned=1; fi
[ "$warned" = 0 ] && ok "keys for the connected tools are set"

echo "ROUTING"
# Every studio command must be in CLAUDE.md's routing table, or a session won't know when to use it.
unrouted=""
for c in $(sed -n 's#^  - \.claude/skills/\([^/]*\)/$#\1#p' studio.manifest.yaml); do
  grep -q "/$c\b" CLAUDE.md || unrouted="$unrouted /$c"
done
[ -z "$unrouted" ] && ok "every command is in CLAUDE.md's routing table" || fail "not in CLAUDE.md's routing table:$unrouted"

echo "SIZE"
# Files the studio reads often, past the size where a session starts wading instead of reading.
# A warning, never a FAIL: /tidy moves what's stale to an archive and compacts the logs. The limits
# are starting defaults (bytes); a person with a big body of work will pass them sooner.
big=0
while read -r f limit; do
  [ -f "$f" ] || continue
  n=$(wc -c < "$f" | tr -d ' ')
  if [ "$n" -gt "$limit" ]; then echo "  warn  $f is $((n/1000)) KB (past $((limit/1000)) KB): say /tidy"; big=1; fi
done <<'EOF'
bank/ideas.md 120000
bank/credibility.md 80000
bank/evidence.md 80000
bank/questions.md 60000
proposals.md 60000
sessions/log.md 80000
studio-notes.md 40000
EOF
[ "$big" = 0 ] && ok "the banks and logs are a size the studio can read in one go"

echo "WRITING RULES IN THE CANON"
# the canon's own text should pass the mechanical checks too: no em dashes in the person's files.
# An em dash inside a quotation (the person's own words, kept as written) doesn't count; only the
# studio's prose around the quotes does. readback.md is all quotes and is skipped.
emdash_files="$(grep -rl $'—' canon/ 2>/dev/null | grep -v 'canon/readback.md' | while read -r f; do
  python3 - "$f" <<'PY'
import re,sys
f=sys.argv[1]; s=open(f,encoding='utf-8').read()
s=re.sub(r'"[^"\n]*"', '', s)            # straight quotes
s=re.sub(r'\u201c[^\u201d\n]*\u201d', '', s)  # curly quotes
s=re.sub(r'(?m)^>.*$', '', s)           # blockquotes
if '\u2014' in s: print(f)
PY
done | tr '\n' ' ')"
if [ -n "$emdash_files" ]; then fail "em dashes in the studio's own prose: $emdash_files"; else ok "no em dashes in canon/ outside the person's quotes"; fi

echo
if [ "$fails" = 0 ] && [ "$skipped" = 1 ]; then
  echo "setup-check: the install is fine. You skipped the interviews, so the check covers what the job commands need; the canon checks above are notes."
elif [ "$fails" = 0 ] && [ "$early" = 1 ]; then
  echo "setup-check: the install is fine. You're at \"$stage\"; the rest of the check runs once \"make it yours\" is done or skipped."
elif [ "$fails" = 0 ]; then
  echo "setup-check: all install checks pass. Now the test piece (skills/setup-check, step 2)."
else
  echo "setup-check: $fails FAIL. Fix these first."
fi
[ "$fails" = 0 ]
