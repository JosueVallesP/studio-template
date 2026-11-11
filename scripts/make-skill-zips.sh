#!/usr/bin/env bash
# Builds one zip per skill in skills/, ready for "Upload a skill" in the Claude app.
# Each zip opens to <skill-name>/SKILL.md, which is the layout the uploader expects.
#
# Usage:
#   bash scripts/make-skill-zips.sh            # all skills
#   bash scripts/make-skill-zips.sh fmt-linkedin-post setup-brand-tree
#
# Output goes to dist/skills/. That folder is ignored by git.

set -euo pipefail

REPO_ROOT="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
SRC="$REPO_ROOT/skills"
OUT="$REPO_ROOT/dist/skills"

for tool in zip unzip; do
  if ! command -v "$tool" >/dev/null 2>&1; then
    echo "Stopped: $tool is not installed." >&2
    exit 1
  fi
done

if [ "$#" -gt 0 ]; then
  names=("$@")
else
  names=()
  for dir in "$SRC"/*/; do
    names+=("$(basename "$dir")")
  done
fi

# The Claude app turns away a skill whose description is over 1024 characters; stop before building one.
python3 -I "$REPO_ROOT/scripts/check-descriptions.py" >/dev/null || { python3 -I "$REPO_ROOT/scripts/check-descriptions.py" | grep FAIL >&2; echo "Stopped: shorten those descriptions first." >&2; exit 1; }

mkdir -p "$OUT"

for name in "${names[@]}"; do
  if [ ! -f "$SRC/$name/SKILL.md" ]; then
    echo "Stopped: skills/$name/SKILL.md does not exist." >&2
    exit 1
  fi
  rm -f "$OUT/$name.zip"
  (cd "$SRC" && zip -r -q "$OUT/$name.zip" "$name" -x "$name/.*" -x "*/.DS_Store")

  # Check the zip opens to name/SKILL.md and holds nothing outside that folder.
  entries="$(unzip -Z1 "$OUT/$name.zip")"
  if ! printf '%s\n' "$entries" | grep -Fxq "$name/SKILL.md"; then
    echo "Stopped: $name.zip does not contain $name/SKILL.md." >&2
    exit 1
  fi
  if printf '%s\n' "$entries" | grep -v "^$name/" | grep -q .; then
    echo "Stopped: $name.zip contains a path outside $name/." >&2
    exit 1
  fi
  echo "built dist/skills/$name.zip"
done
