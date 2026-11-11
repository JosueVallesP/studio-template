#!/usr/bin/env bash
# Updates an instance (a person's own repo) from the studio repo: replaces every studio-owned
# path listed in the studio's manifest and never touches a person-owned one.
#
# Usage, from inside the instance folder:
#   bash scripts/update-studio.sh                      (uses the URL in studio-source.md)
#   bash scripts/update-studio.sh https://github.com/you/studio-template
#   bash scripts/update-studio.sh /path/to/content-studio
#
# Or to create a new instance from the studio:
#   bash /path/to/content-studio/scripts/update-studio.sh /path/to/content-studio --init /path/to/new-instance
#
# It reads studio.manifest.yaml in the studio, deletes each studio_owned path in the instance and
# copies the studio's version in, then writes studio-source.md with the version it came from.
# Inside .claude/ the manifest names the studio's own files one by one, so anything else a person
# keeps there (their recipe shortcuts in .claude/skills/<name>/) survives. Everything under client_owned
# in the manifest is the person's and is never replaced; the missing client_owned folders are created,
# and a few starter files (README.md on --init, the folder READMEs, studio-notes.md, proposals.md) are
# added once. A file the last install put here (listed in .studio-installed) that the new manifest no
# longer lists as the studio's is moved to studio-local-backup/<date>/, never deleted.
# The stop hook commits the result; /update shows the diff first.

set -euo pipefail

# The studio can be a local folder, a git URL, or nothing (then the URL in studio-source.md is used).
SRC="${1:-}"
if [ -z "$SRC" ] && [ -f studio-source.md ]; then
  SRC="$(grep -m1 '^- studio:' studio-source.md | sed 's/^- studio: *//')"
fi
[ -n "$SRC" ] || { echo "Give the studio: a folder, a git URL, or run from an instance whose studio-source.md names one" >&2; exit 1; }
# "managed": this studio was built for the person, and new versions are pushed into their repo by the
# studio's update job (.github/ops/push-updates.py). There's nothing to pull from here.
if [ "$SRC" = managed ]; then
  echo "This studio is updated for you: each new version is pushed into your repo, and the next session has it. Nothing to run."
  exit 0
fi
TMP=""
case "$SRC" in
  https://*|http://*|file://*|git@*|ssh://*)
    TMP="$(mktemp -d)"
    echo "Fetching the studio from $SRC"
    git clone -q --depth 1 "$SRC" "$TMP/studio" || { echo "Couldn't fetch $SRC (offline, or this session can't see that repo: accept its invite, and let Claude see it from GitHub)" >&2; rm -rf "$TMP"; exit 1; }
    STUDIO="$TMP/studio"
    trap 'rm -rf "$TMP"' EXIT
    ;;
  *) STUDIO="$SRC" ;;
esac
INIT=0
if [ "${2:-}" = "--init" ]; then
  INSTANCE="${3:?path for the new instance}"
  INIT=1
  mkdir -p "$INSTANCE"
else
  INSTANCE="$(pwd)"
fi
[ -f "$STUDIO/studio.manifest.yaml" ] || { echo "No studio.manifest.yaml in $STUDIO" >&2; exit 1; }

version="$(grep -m1 '^version:' "$STUDIO/studio.manifest.yaml" | awk '{print $2}')"
owned="$(awk '/^studio_owned:/{f=1;next} /^client_owned:/{f=0} f && /^  - /{sub(/^  - /,""); print}' "$STUDIO/studio.manifest.yaml")"
client="$(awk '/^client_owned:/{f=1;next} /^[a-z_]+:/{f=0} f && /^  - /{sub(/^  - /,""); print}' "$STUDIO/studio.manifest.yaml")"
# under LIST PATH: true when PATH is one of LIST's entries, or inside one that ends in /.
under() { local e; while IFS= read -r e; do [ -n "$e" ] || continue
  case "$e" in */) case "$2" in "$e"*) return 0;; esac;; *) [ "$2" = "$e" ] && return 0;; esac; done <<< "$1"; return 1; }

echo "Updating $INSTANCE from studio $version"

# Keep the person's own edits. .studio-installed holds a checksum of every studio file the last
# update put here. A studio file whose checksum no longer matches (they or Claude changed it), or a
# file someone added inside a studio folder, is copied to studio-local-backup/<date>/ before it's
# replaced, with a note saying what happened. The first update of an instance has no checksums yet,
# so it only writes them; protection starts with the next one.
STAMP="$INSTANCE/.studio-installed"
BACKUP_DIR="studio-local-backup/$(date +%Y-%m-%d)"
kept=0
if [ "$INIT" = 0 ] && [ -f "$STAMP" ]; then
  for p in $owned; do
    [ "$p" = studio-source.md ] && continue
    [ -e "$INSTANCE/$p" ] || continue
    while IFS= read -r -d '' f; do
      rel="${f#$INSTANCE/}"
      now="$(sha256sum "$f" | awk '{print $1}')"
      was="$(awk -v r="$rel" '$2==r {print $1; exit}' "$STAMP")"
      if [ "$now" != "$was" ]; then
        mkdir -p "$INSTANCE/$BACKUP_DIR/$(dirname "$rel")"
        cp -p "$f" "$INSTANCE/$BACKUP_DIR/$rel"
        kept=$((kept+1))
      fi
    done < <(find "$INSTANCE/$p" -type f -print0)
  done
  if [ "$kept" -gt 0 ]; then
    cat > "$INSTANCE/$BACKUP_DIR/README.md" <<EOT
# Your changes to studio files, kept before the update to $version

The update on $(date +%Y-%m-%d) replaces the studio's own files with the new version. These $kept file(s)
had been changed here (by you, or by Claude at your request), or added inside a studio folder, so a copy of
each was kept here first, at the same path. Nothing of yours outside the studio's files was touched.

To keep a change, compare the copy here with the new file and say "bring back my change to <file>".
If you don't need them, this folder can go.
EOT
    echo "  kept $kept changed studio file(s) in $BACKUP_DIR"
  fi
fi

# Studio files that left the manifest: the last install put them here, the new version no longer has
# them as the studio's. Moved to the backup folder with the same relative path, never deleted, and
# never a person-owned path or anything the last install didn't list (a recipe shortcut, say).
moved=0
if [ "$INIT" = 0 ] && [ -f "$STAMP" ]; then
  while read -r _ rel; do
    [ -n "$rel" ] && [ -f "$INSTANCE/$rel" ] || continue
    under "$owned" "$rel" && continue
    under "$client" "$rel" && continue
    mkdir -p "$INSTANCE/$BACKUP_DIR/$(dirname "$rel")"
    mv "$INSTANCE/$rel" "$INSTANCE/$BACKUP_DIR/$rel"
    # The folders it leaves empty go too, up to the first one that still holds something.
    d="$(dirname "$rel")"
    while [ "$d" != "." ] && ! under "$client" "$d/" && rmdir "$INSTANCE/$d" 2>/dev/null; do d="$(dirname "$d")"; done
    echo "  moved $rel to $BACKUP_DIR (no longer part of the studio)"
    moved=$((moved+1))
  done < "$STAMP"
  if [ "$moved" -gt 0 ] && [ ! -e "$INSTANCE/$BACKUP_DIR/README.md" ]; then
    printf '# Studio files kept by the update to %s\n\nThe update on %s moved here the studio files the new version no longer has, at the same paths.\nNothing of yours was touched. If you don'"'"'t need them, this folder can go.\n' "$version" "$(date +%Y-%m-%d)" > "$INSTANCE/$BACKUP_DIR/README.md"
  fi
fi

for p in $owned; do
  [ "$p" = studio-source.md ] && continue      # written below, from the version just copied
  src="$STUDIO/$p"
  dst="$INSTANCE/$p"
  [ -e "$src" ] || { echo "  skip (not in studio): $p"; continue; }
  rm -rf "$dst"
  mkdir -p "$(dirname "$dst")"
  cp -r "$src" "$dst"
  echo "  replaced $p"
done

# Person-owned folders (every client_owned entry ending in /) exist in the instance, and are never
# touched if they do. bank/rewrites/ gets its README below.
for d in $(printf '%s\n' "$client" | grep '/$') bank/rewrites/; do
  case "$d" in studio-local-backup/) continue;; esac   # made only when an update keeps something
  mkdir -p "$INSTANCE/$d"
done
# README.md is the person's: written once on --init from the person-facing guide, never replaced.
if [ "$INIT" = 1 ] && [ ! -e "$INSTANCE/README.md" ] && [ -e "$STUDIO/docs/getting-started.md" ]; then
  cp "$STUDIO/docs/getting-started.md" "$INSTANCE/README.md"; echo "  added README.md (first time only)"
fi
[ -e "$INSTANCE/bank/rewrites/README.md" ] || { [ -e "$STUDIO/skills/setup-brand-tree/templates/bank-working/rewrites-README.md" ] && cp "$STUDIO/skills/setup-brand-tree/templates/bank-working/rewrites-README.md" "$INSTANCE/bank/rewrites/README.md"; }
for f in canon/README.md pieces/README.md; do
  [ -e "$INSTANCE/$f" ] || { [ -e "$STUDIO/$f" ] && cp "$STUDIO/$f" "$INSTANCE/$f" && echo "  added $f (first time only)"; }
done
[ -e "$INSTANCE/inbox/README.md" ] || cp "$STUDIO/templates/inbox/README.md" "$INSTANCE/inbox/README.md"
[ -e "$INSTANCE/material/README.md" ] || cp "$STUDIO/templates/material/README.md" "$INSTANCE/material/README.md"
# Run notes belong to the instance (the manifest lists them as person-owned); add the file once, never replace it.
[ -e "$INSTANCE/studio-notes.md" ] || { printf '# Studio notes\n\nOne line per place a skill made a run guess: date · skill · what was unclear. Feeds the next version of the studio.\n' > "$INSTANCE/studio-notes.md"; echo "  added studio-notes.md (first time only)"; }
[ -e "$INSTANCE/proposals.md" ] || cp "$STUDIO/templates/proposals.md" "$INSTANCE/proposals.md"

# Checksums of every studio file as installed, so the next update can tell what changed here.
: > "$STAMP"
for p in $owned; do
  [ "$p" = studio-source.md ] && continue
  [ -e "$INSTANCE/$p" ] || continue
  find "$INSTANCE/$p" -type f -print0 | while IFS= read -r -d '' f; do
    printf '%s %s\n' "$(sha256sum "$f" | awk '{print $1}')" "${f#$INSTANCE/}" >> "$STAMP"
  done
done

# Worked out here, not inside the heredoc: bash 3.2 (macOS) can't parse a case inside $( ) there.
studio_line="${STUDIO_URL:-}"
if [ -z "$studio_line" ]; then
  case "$SRC" in
    https://*|http://*|file://*|git@*|ssh://*) studio_line="$SRC" ;;
    *) studio_line="$(cd "$STUDIO" && git remote get-url origin 2>/dev/null || echo "$STUDIO")" ;;
  esac
fi

cat > "$INSTANCE/studio-source.md" <<EOT
# Studio source

This folder is one person's instance of the content studio. The studio-owned paths (listed in
studio.manifest.yaml) came from the studio repo and get replaced by \`scripts/update-studio.sh\`.
Everything else here is the person's and is never touched by an update.

- studio: $studio_line
- version: $version
- updated: $(date +%Y-%m-%d)
EOT
echo "Done. studio-source.md says $version. Review with git diff --stat."
