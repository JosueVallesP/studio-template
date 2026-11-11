#!/usr/bin/env bash
# Makes a person's studio from their Tally submission (or an answers file), in one command:
# converts the answers, builds their instance, puts it in git, creates a private GitHub repo,
# invites them, and pushes the first version. After this, every session they run saves and
# backs itself up (scripts/save.sh).
#
#   bash scripts/make-client.sh <tally-export.csv | tally-webhook.json | answers.yaml> [options]
#
# Options:
#   --row N           which CSV submission (1 = first; default: the last one)
#   --email ADDRESS   pick the CSV submission with this email instead
#   --name SLUG       folder and repo name (default: built from their name, e.g. ana-ruiz-studio)
#   --dir PATH        where studios live on this computer (default: ~/Studios)
#   --owner OWNER     GitHub user or organization that owns the repo (default: whoever gh is logged in as)
#   --no-github       build and commit locally, don't create a repo or invite anyone
#   --hand-over       the studio goes to their own GitHub account instead of yours: build it, then
#                     scripts/hand-over.sh transfers it to them (you keep no access) and they pull new
#                     versions with /update. Needs their GitHub username in the answers.
#   --description TEXT  the repo's description on GitHub (the automation puts the Tally submission ID here)
#   --result FILE     also write the outcome as key=value lines (name, email, github, slug, folder, url, invited)
#                     for automation (.github/ops/new-clients.py reads it)
#
# Needs: python3, git, and for the GitHub part the GitHub CLI (gh) logged in once with `gh auth login`.
set -euo pipefail

STUDIO="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
SRC="${1:?give the Tally export (.csv or .json) or an answers .yaml file}"; shift
DESC=""; ROW=""; EMAIL=""; SLUG=""; DIR="${HOME}/Studios"; OWNER=""; GITHUB=1; RESULT=""; HANDOVER=0
while [ $# -gt 0 ]; do
  case "$1" in
    --row) ROW="$2"; shift 2;;
    --email) EMAIL="$2"; shift 2;;
    --name) SLUG="$2"; shift 2;;
    --dir) DIR="$2"; shift 2;;
    --owner) OWNER="$2"; shift 2;;
    --description) DESC="$2"; shift 2;;
    --no-github) GITHUB=0; shift;;
    --hand-over) HANDOVER=1; shift;;
    --result) RESULT="$(cd "$(dirname "$2")" && pwd)/$(basename "$2")"; shift 2;;
    *) echo "unknown option: $1" >&2; exit 2;;
  esac
done

WORK="$(mktemp -d)"; trap 'rm -rf "$WORK"' EXIT
ANSWERS="$WORK/answers.yaml"; UPLOADS="$WORK/uploads"; mkdir -p "$UPLOADS"

echo "1. Reading the answers"
case "$SRC" in
  *.csv|*.CSV|*.json|*.JSON)
    args=("$SRC" --out "$ANSWERS" --uploads "$UPLOADS")
    [ -n "$ROW" ] && args+=(--row "$ROW")
    [ -n "$EMAIL" ] && args+=(--email "$EMAIL")
    python3 "$STUDIO/scripts/tally-to-answers.py" "${args[@]}";;
  *) cp "$SRC" "$ANSWERS";;
esac

field() { grep -m1 "^$1:" "$ANSWERS" | sed -E "s/^$1:[[:space:]]*//; s/^\"(.*)\"$/\1/"; }
PERSON="$(field name)"; GH_USER="$(field github | sed 's/^@//')"
[ -n "$PERSON" ] || { echo "The answers have no name; can't name the studio." >&2; exit 1; }
if [ -z "$SLUG" ]; then
  SLUG="$(printf '%s' "$PERSON" | iconv -f utf-8 -t ascii//TRANSLIT 2>/dev/null || printf '%s' "$PERSON")"
  SLUG="$(printf '%s' "$SLUG" | tr '[:upper:]' '[:lower:]' | sed -E 's/[^a-z0-9]+/-/g; s/^-|-$//g')-studio"
fi
HAVE_GH=0
if [ "$GITHUB" = 1 ] && command -v gh >/dev/null 2>&1 && gh auth status >/dev/null 2>&1; then
  HAVE_GH=1
  [ -n "$OWNER" ] || OWNER="$(gh api user --jq .login)"
  # Two buyers with the same name get ana-ruiz-studio and ana-ruiz-studio-2.
  base="$SLUG"; n=2
  while gh repo view "$OWNER/$SLUG" >/dev/null 2>&1 || [ -e "$DIR/$SLUG" ]; do SLUG="$base-$n"; n=$((n+1)); done
fi
OUT="$DIR/$SLUG"
[ -e "$OUT" ] && { echo "$OUT already exists. Pick another --name, or move it first." >&2; exit 1; }

echo "2. Building $PERSON's studio in $OUT"
mkdir -p "$DIR"
python3 "$STUDIO/scripts/build-instance.py" "$ANSWERS" --studio "$STUDIO" --out "$OUT" --inbox "$UPLOADS" | sed 's/^/   /'

cd "$OUT"
echo "   Turning their uploads into text the studio can read"
python3 scripts/inbox-to-text.py | sed 's/^/   /'

echo "3. Putting it in git"
git init -q -b main
git add -A
git -c user.name="Content Studio" -c user.email="studio@local" commit -q -m "Studio for $PERSON, built from their intake"

URL=""; INVITED="no"
if [ "$GITHUB" = 1 ]; then
  if [ "$HAVE_GH" != 1 ]; then
    echo "   GitHub CLI isn't installed or logged in; skipping the repo. Run 'gh auth login', then:"
    echo "   cd \"$OUT\" && gh repo create $SLUG --private --source . --push"
  else
    echo "4. Creating the private repo $OWNER/$SLUG"
    if ! gh repo create "$OWNER/$SLUG" --private --source . --push ${DESC:+--description "$DESC"} >/dev/null; then
      echo "   GitHub refused to create the repo. If it says \"Resource not accessible by personal access token\", the token can't create repos: see docs/automation.md, step 1." >&2
      exit 1
    fi
    # Tag it so the update job (.github/workflows/push-updates.yml) finds it and pushes each new version.
    gh repo edit "$OWNER/$SLUG" --add-topic content-studio-instance >/dev/null 2>&1 || echo "   (couldn't tag the repo; add it to .github/ops/update-include.txt so it gets updates)"
    URL="https://github.com/$OWNER/$SLUG"
    sed -i.bak -E "s#^- url: not yet.*#- url: $URL#" config/tools.md && rm -f config/tools.md.bak
    git add -A && git -c user.name="Content Studio" -c user.email="studio@local" commit -q -m "Record the repo URL" && git push -q
    if [ "$HANDOVER" = 1 ]; then
      if [ -n "$GH_USER" ]; then
        echo "5. Handing it over to $GH_USER"
        bash "$STUDIO/scripts/hand-over.sh" "$OWNER/$SLUG" "$GH_USER" | sed 's/^/   /' && INVITED="handed-over" \
          || { INVITED="failed"; echo "   The hand-over didn't finish. Fix what it says, then run: bash scripts/hand-over.sh $OWNER/$SLUG <their username>"; }
      else
        INVITED="failed"; echo "   No GitHub username in their answers, so it can't be handed over yet. Get it, then run: bash scripts/hand-over.sh $OWNER/$SLUG <their username>"
      fi
    elif [ -n "$GH_USER" ]; then
      gh api -X PUT "repos/$OWNER/$SLUG/collaborators/$GH_USER" -f permission=push >/dev/null \
        && { INVITED="yes"; echo "   Invited $GH_USER. They accept the invite from their email or github.com/notifications."; } \
        || { INVITED="failed"; echo "   Couldn't invite $GH_USER. Check the username and invite them from the repo's Settings, Collaborators."; }
    else
      echo "   No GitHub username in their answers. Invite them from the repo's Settings, Collaborators."
    fi
  fi
fi

if [ -n "$RESULT" ]; then
  { echo "name=$PERSON"; echo "email=$(field email)"; echo "github=$GH_USER"; echo "slug=$SLUG"; echo "folder=$OUT"; echo "url=$URL"; echo "invited=$INVITED"; } > "$RESULT"
fi

echo
echo "Done: $PERSON's studio."
echo "  Folder: $OUT"
[ -n "$URL" ] && echo "  Repo:   $URL"
echo "  Send them docs/getting-started.md (it's in their repo too) and say: in the Claude app's Code tab, pick Cloud and this studio, then say /start."
