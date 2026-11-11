#!/usr/bin/env bash
# Builds the public template: an empty instance of the studio that a person copies to start.
# Run it from the content-studio folder after shipping a version:
#   bash scripts/make-template.sh https://github.com/JosueVallesP/studio-template
# It builds the instance in a temp folder with update-studio.sh --init, writes the person-facing
# README (docs/getting-started.md), and force-pushes it as the template's main branch. The template
# has no history worth keeping: it is the studio at one version, nothing else.
set -euo pipefail
STUDIO="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
TEMPLATE_URL="${1:?the git URL of the template repo}"
TMP="$(mktemp -d)"; trap 'rm -rf "$TMP"' EXIT
OUT="$TMP/instance"
STUDIO_URL="$TEMPLATE_URL" bash "$STUDIO/scripts/update-studio.sh" "$STUDIO" --init "$OUT" >/dev/null
cp "$STUDIO/docs/getting-started.md" "$OUT/README.md"
version="$(grep -m1 '^version:' "$STUDIO/studio.manifest.yaml" | awk '{print $2}')"
cd "$OUT"
git init -q -b main
git add -A
git -c user.name="Content Studio" -c user.email="studio@local" commit -q -m "Content studio template $version"
git remote add origin "$TEMPLATE_URL"
git push -q --force origin main
echo "Template $version pushed to $TEMPLATE_URL"
