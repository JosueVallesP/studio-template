#!/usr/bin/env bash
# Hands a client's studio over to them: the repo moves to their own GitHub account, the seller
# keeps no access to it, and from then on the client pulls new versions themselves with /update.
#
#   bash scripts/hand-over.sh <owner/repo> <their-github-username> [options]
#
# What it does, in order:
#   1. Makes sure the template (the repo that holds only the studio's code, no one's files) is at
#      this studio's version, and rebuilds it with make-template.sh when it's older.
#   2. Points the studio at the template: studio-source.md says "- studio: <template URL>" instead of
#      "managed", and config/tools.md records the repo's new URL. Commits and pushes that.
#   3. Gives them read access to the template when it's private, so /update can fetch from it.
#   4. Takes the repo off the update job's list (the content-studio-instance topic), since the job
#      can't reach a repo it doesn't own.
#   5. Asks GitHub to transfer the repo to them. GitHub emails them; the repo moves when they accept.
#      Once it has moved, the seller has no access at all: not as owner, not as collaborator.
#
# Options:
#   --template URL   the template repo (default: $STUDIO_TEMPLATE_URL, or github.com/JosueVallesP/studio-template)
#   --dry-run        say what would happen and change nothing
#
# make-client.sh --hand-over runs this right after it builds a new studio. For a studio that
# already exists, run it on its own. Needs git and the GitHub CLI (gh), logged in as the repo's owner.
set -euo pipefail

STUDIO="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
REPO="${1:?give the studio repo as owner/name}"; shift
USER_GH="${1:?give their GitHub username}"; shift
USER_GH="${USER_GH#@}"
TEMPLATE_URL="${STUDIO_TEMPLATE_URL:-https://github.com/JosueVallesP/studio-template}"
DRY=0
while [ $# -gt 0 ]; do
  case "$1" in
    --template) TEMPLATE_URL="$2"; shift 2;;
    --dry-run) DRY=1; shift;;
    *) echo "unknown option: $1" >&2; exit 2;;
  esac
done
TEMPLATE_URL="${TEMPLATE_URL%.git}"
TEMPLATE="$(printf '%s' "$TEMPLATE_URL" | sed -E 's#^https://github.com/##')"
NAME="${REPO#*/}"
NEW_URL="https://github.com/$USER_GH/$NAME"
do_it() { if [ "$DRY" = 1 ]; then echo "   (dry run) $*"; else "$@"; fi; }

command -v gh >/dev/null 2>&1 && gh auth status >/dev/null 2>&1 || { echo "The GitHub CLI isn't installed or logged in. Run 'gh auth login' first." >&2; exit 1; }
gh api "users/$USER_GH" --jq .login >/dev/null 2>&1 || { echo "GitHub has no user called $USER_GH. Check the username." >&2; exit 1; }
gh repo view "$REPO" >/dev/null 2>&1 || { echo "Can't see $REPO from this login." >&2; exit 1; }
if gh repo view "$USER_GH/$NAME" >/dev/null 2>&1; then
  echo "$USER_GH already has a repo called $NAME, so GitHub would refuse the transfer. Rename one of them first." >&2; exit 1
fi

echo "1. Checking the template ($TEMPLATE) is at this studio's version"
want="$(grep -m1 '^version:' "$STUDIO/studio.manifest.yaml" | awk '{print $2}')"
have="$(gh api -H 'Accept: application/vnd.github.raw' "repos/$TEMPLATE/contents/studio.manifest.yaml" 2>/dev/null | grep -m1 '^version:' | awk '{print $2}' || true)"
if [ "$have" = "$want" ]; then
  echo "   the template is at $want"
else
  echo "   the template is at ${have:-nothing yet}, the studio at $want: rebuilding the template"
  do_it bash "$STUDIO/scripts/make-template.sh" "$TEMPLATE_URL"
fi

echo "2. Pointing the studio at the template"
WORK="$(mktemp -d)"; trap 'rm -rf "$WORK"' EXIT
gh repo clone "$REPO" "$WORK/studio" -- -q --depth 1
cd "$WORK/studio"
[ -f studio-source.md ] || { echo "$REPO has no studio-source.md, so it isn't a studio. Nothing changed." >&2; exit 1; }
sed -i.bak -E "s#^- studio:.*#- studio: $TEMPLATE_URL#" studio-source.md && rm -f studio-source.md.bak
[ -f config/tools.md ] && { sed -i.bak -E "s#^- url: .*#- url: $NEW_URL#" config/tools.md && rm -f config/tools.md.bak; }
git add -A
if git diff --cached --quiet; then
  echo "   already pointed at the template"
else
  git -c user.name="Content Studio" -c user.email="studio@local" commit -q -m "Hand over to $USER_GH: new versions come from the template with /update"
  do_it git push -q
  echo "   studio-source.md now says: studio: $TEMPLATE_URL"
fi
cd - >/dev/null

echo "3. Read access to the template"
if [ "$(gh api "repos/$TEMPLATE" --jq .private)" = "true" ]; then
  do_it gh api -X PUT "repos/$TEMPLATE/collaborators/$USER_GH" -f permission=pull >/dev/null
  echo "   invited $USER_GH to read $TEMPLATE (it holds only the studio's code)"
else
  echo "   the template is public, nothing to do"
fi

echo "4. Taking it off the update job's list"
do_it gh repo edit "$REPO" --remove-topic content-studio-instance >/dev/null 2>&1 || true
if grep -qx "$REPO" "$STUDIO/.github/ops/update-include.txt" 2>/dev/null; then
  echo "   $REPO is in .github/ops/update-include.txt: take that line out"
fi

echo "5. Transferring $REPO to $USER_GH"
do_it gh api -X POST "repos/$REPO/transfer" -f new_owner="$USER_GH" >/dev/null

cat <<EOT

Done. What $USER_GH does next (GitHub emails them both):
  1. Accept the transfer of $NAME. GitHub lets the request expire after a day; if it does, run this again.
  2. Accept the invite to read the template, if one came. That's what /update fetches from.
  3. In the Claude app, Code, Cloud: when they pick the studio, GitHub asks them to let Claude see their
     repos. They allow it for $NAME (and the template). Then /start, or /update whenever they want the latest version.

Once they accept, the repo lives at $NEW_URL and you have no access to it.
Check it any time: gh repo view $USER_GH/$NAME should say it can't find it.
EOT
