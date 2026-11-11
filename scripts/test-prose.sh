#!/usr/bin/env bash
# Reruns the house-rule tests: every file in tests/prose/fail must fail check-prose, every file in
# tests/prose/pass must pass (flags allowed), and voice-diff must flag the studio's drafts in
# tests/prose/drift against the corpus in tests/prose/corpus. Run after any change to the rules,
# the scripts, or a skill that writes. Exit 1 on the first broken expectation.
cd "$(dirname "$0")/.." || exit 1
if [ ! -d tests/prose/fail ] && [ ! -d tests/prose/pass ]; then
  echo "test-prose: no test set here (tests/prose/ is missing); nothing to run"; exit 0
fi
ok=0; bad=0
for f in tests/prose/fail/*.md; do
  [ -e "$f" ] || continue
  if python3 -I scripts/check-prose.py "$f" >/dev/null 2>&1; then echo "SHOULD FAIL but passed: $f"; bad=$((bad+1)); else ok=$((ok+1)); fi
done
for f in tests/prose/pass/*.md; do
  [ -e "$f" ] || continue
  if python3 -I scripts/check-prose.py "$f" >/dev/null 2>&1; then ok=$((ok+1)); else echo "SHOULD PASS but failed: $f"; python3 -I scripts/check-prose.py "$f" | grep -A12 FAILS; bad=$((bad+1)); fi
done
for f in tests/prose/reply-fail/*.md; do
  [ -e "$f" ] || continue
  if python3 -I scripts/check-prose.py "$f" --mode reply >/dev/null 2>&1; then echo "REPLY SHOULD FAIL but passed: $f"; bad=$((bad+1)); else ok=$((ok+1)); fi
done
for f in tests/prose/drift/*.md; do
  [ -e "$f" ] || continue
  if python3 -I scripts/voice-diff.py "$f" --corpus tests/prose/corpus >/dev/null 2>&1; then echo "SHOULD DRIFT but didn't: $f"; bad=$((bad+1)); else ok=$((ok+1)); fi
done
echo "test-prose: $ok ok, $bad broken"
[ "$bad" -eq 0 ]
