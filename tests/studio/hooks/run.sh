#!/usr/bin/env bash
# Feeds each *.json payload in this folder to the hook it names and compares the hook's decision
# with the payload's `expect:` field (allow, ask or deny). The hook is taken from the payload's `hook:`
# field, or from the file name's prefix (writes-... is guard-writes, bash-... is guard-bash, publish-... is guard-publish; reads- payloads name guard-reads).
# Each payload runs with its cwd set to an empty temp folder, so no hook can touch the repo.
# Usage, from anywhere: bash tests/studio/hooks/run.sh
set -uo pipefail
HERE="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
HOOKS="$(cd "$HERE/../../../.claude/hooks" && pwd)"
TMP="$(mktemp -d)"; trap 'rm -rf "$TMP"' EXIT
pass=0; fail=0
for f in "$HERE"/*.json; do
  name="$(basename "$f")"
  read -r hook expect payload < <(python3 -I - "$f" "$TMP" <<'PY'
import json, sys
d = json.load(open(sys.argv[1], encoding="utf-8"))
name = sys.argv[1].rsplit("/", 1)[-1]
hook = d.pop("hook", None) or ("guard-writes" if name.startswith("writes-") else "guard-bash" if name.startswith("bash-") else "guard-publish" if name.startswith("publish-") else "")
expect = d.pop("expect", "")
d["cwd"] = sys.argv[2]
print(hook, expect, json.dumps(d))
PY
)
  if [ -z "$hook" ] || [ ! -f "$HOOKS/$hook.py" ]; then
    echo "FAIL $name: no hook named (use a hook: field or a writes-/bash- prefix)"; fail=$((fail+1)); continue
  fi
  out="$(printf '%s' "$payload" | CLAUDE_PROJECT_DIR="$TMP" python3 -I "$HOOKS/$hook.py" 2>&1)"
  if printf '%s' "$out" | grep -q 'Traceback'; then
    echo "FAIL $name: the hook crashed"; echo "$out" | sed 's/^/     /'; fail=$((fail+1)); continue
  fi
  if printf '%s' "$out" | grep -q '"permissionDecision": "deny"'; then got=deny
  elif printf '%s' "$out" | grep -q '"permissionDecision": "ask"'; then got=ask; else got=allow; fi
  if [ "$got" = "$expect" ]; then
    echo "ok   $name ($got)"; pass=$((pass+1))
  else
    echo "FAIL $name: expected $expect, got $got"; [ -n "$out" ] && echo "     $out"; fail=$((fail+1))
  fi
done
echo "$pass passed, $fail failed"
[ "$fail" = 0 ]
