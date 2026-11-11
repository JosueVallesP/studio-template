#!/usr/bin/env bash
# Runs every automated test the studio has, in one go: the house-rule test set (test-prose.sh), the
# hook guards, the rewrite pairs, the house-rule cases, the three-draft checks, the stitch check, the packet
# build, the dashboard syncs' config reader, the map build and the voiceprint check on the essay library. The update job
# runs this before it pushes a new version to any client, and stops when anything fails. A suite whose
# folder isn't here (an instance that doesn't carry it) is skipped and named, not failed.
# Usage, from anywhere: bash scripts/test-all.sh
cd "$(dirname "$0")/.." || exit 1
failed=()
skipped=()
run() {
  local name="$1"; shift
  local target="" a
  for a in "$@"; do case "$a" in tests/*|scripts/*) target="$a"; break;; esac; done
  if [ ! -e "$target" ]; then skipped+=("$name"); return; fi
  echo "######## $name"
  if "$@"; then echo; else failed+=("$name"); echo; fi
}
run "house-rule set"   bash scripts/test-prose.sh
run "hooks"            bash tests/studio/hooks/run.sh
run "rewrites"         python3 -I tests/studio/rewrites/run.py
run "house-rule cases" python3 -I tests/studio/house-rules/run.py
run "three drafts"     python3 -I tests/studio/drafts/run.py
run "stitch"           python3 -I tests/studio/stitch/run.py
run "packet"           python3 -I tests/studio/packet/run.py
run "sync config"      python3 -I tests/studio/sync-config/run.py
run "map"              python3 -I tests/studio/map/run.py
run "canon status"     python3 -I tests/studio/canon-status/run.py
run "receipts"         python3 -I tests/studio/receipts/run.py
run "review hash"      python3 -I tests/studio/review-hash/run.py
run "claims"           python3 -I tests/studio/claims/run.py
run "voice-diff"       python3 -I tests/studio/voice-diff/run.py
run "secrets"          python3 -I tests/studio/secrets/run.py
run "save stuck"       python3 -I tests/studio/save-stuck/run.py
run "inbox summary"    python3 -I tests/studio/inbox-summary/run.py
run "inbox chatgpt"    python3 -I tests/studio/inbox-summary/chatgpt_comments.py
run "descriptions"     python3 -I scripts/check-descriptions.py
run "voiceprint"       python3 -I tests/studio/voiceprint/validate.py --length 300 --check
run "voiceprint-above" python3 -I tests/studio/voiceprint/above_rate.py
run "voiceprint-own-rules" python3 -I tests/studio/voiceprint/own_rules.py
[ "${#skipped[@]}" -gt 0 ] && echo "test-all: no test set here for ${skipped[*]}; skipped"
if [ "${#failed[@]}" -gt 0 ]; then
  echo "test-all: FAILED (${failed[*]})"
  exit 1
fi
echo "test-all: every suite passed"
