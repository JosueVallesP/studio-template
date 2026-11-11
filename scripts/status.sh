#!/usr/bin/env bash
# Prints the mechanical facts behind /status: studio version, canon counts by file,
# pieces by state, and open proposals. It reads files and counts; it judges nothing.
# Run from the repo root: bash scripts/status.sh

set -uo pipefail
cd "$(dirname "${BASH_SOURCE[0]}")/.."

echo "STUDIO"
version="$(grep -m1 '^version:' studio.manifest.yaml 2>/dev/null | awk '{print $2}')"
echo "  version: ${version:-unknown}"

echo "SETUP"
if [ -f canon/setup-progress.md ]; then
  echo "  stage: $(grep -m1 '^stage:' canon/setup-progress.md | cut -d' ' -f2-)"
  grep -q '^brand_tree: skipped' canon/setup-progress.md && echo "  interviews: skipped (job commands); routes like setup done"
  [ -f config/intake.yaml ] && echo "  intake: done ($(grep -m1 '^built_by:' config/intake.yaml | awk '{print $2}' | tr -d '"'))"
else
  echo "  not started: no canon/setup-progress.md (say /start)"
fi

echo "CANON"
if [ ! -f canon/progress.md ]; then
  echo "  brand tree not started yet; the interview creates these files"
else
  # count_status FILE STATUS-REGEX: counts entries (a heading plus its "status:" line), skipping the
  # frontmatter and template placeholders: an entry whose heading still holds "<", or whose every
  # field line still holds "<...>", was never filled in.
  count_status() {
    awk -v rx="$2" '
      function flush() { if (seen && st != "" && heading !~ /</ && (fields == 0 || filled > 0)) { entries++; if (st ~ rx) n++ } }
      /^##+ / { flush(); heading=$0; seen=1; st=""; fields=0; filled=0; next }
      /^status: / { if (seen) st=$0; else fm=$0; next }
      /^[a-z_]+: / { if (seen) { fields++; if ($0 !~ /<[^>]*>/) { filled++; anyfilled=1 } } }
      /^(- |[A-Z"])/ { if ($0 !~ /<[^>]*>/ && $0 !~ /^- \[ \]/) anyfilled=1 }
      END { flush(); if (entries == 0 && anyfilled && fm ~ rx) n++; print n+0 }' "$1"
  }
  for f in person/values.md person/behaviors.md person/povs.md person/philosophy.md person/thesis.md \
           person/branches.md person/stop-list.md bank/stories.md bank/proof.md vehicle/vehicle.md \
           strategy/brand-strategy.md strategy/audience.md strategy/content-plan.md voice/voice-guide.md; do
    if [ -f "canon/$f" ]; then
      c="$(count_status "canon/$f" '^status: confirmed')"
      d="$(count_status "canon/$f" '^status: (draft)')"
      r="$(count_status "canon/$f" '^status: retired')"
      echo "  $f: confirmed=$c draft=$d retired=$r"
    elif [ "$f" = strategy/content-plan.md ]; then
      echo "  $f: not yet written (strategy-brand writes it)"
    else
      echo "  $f: missing"
    fi
  done
  if [ -f canon/progress.md ]; then
    total="$(grep -cE '^- \[[ x]\]' canon/progress.md)"
    done_="$(grep -c '^- \[x\]' canon/progress.md)"
    echo "  minimum canon: $done_ of $total items checked"
    next="$(sed -n '/^## Next session/,/^## /p' canon/progress.md | grep -m1 '^- ')"
    echo "  next session: ${next#- }"
  fi
fi

echo "INPUT"
if [ -f bank/ideas.md ]; then
  week_ago="$(date -d '7 days ago' +%Y-%m-%d 2>/dev/null || date -v-7d +%Y-%m-%d)"
  n="$(grep -E '^date: [0-9]{4}-[0-9]{2}-[0-9]{2}' bank/ideas.md | awk -v w="$week_ago" '{if ($2 >= w) c++} END {print c+0}')"
  echo "  idea bank entries captured in the last 7 days: $n"
  echo "  ready entries: $(awk '/^##+ /{h=$0} /^status: ready/{if (h !~ /</) n++} END{print n+0}' bank/ideas.md)"
  # The garden: seeds by stage, and stage moves waiting for the person's yes (the idea bank template defines both)
  # Ready to harvest: the top of the last list, and its date (skills/role-strategist)
  if [ -f pieces/shortlist.md ]; then
    echo "  ready to harvest (list of $(grep -m1 '^week:' pieces/shortlist.md | awk '{print $2}')):"
    awk '/^## Candidates/{f=1; next} /^## /{f=0} f && /^[0-9]+\. /' pieces/shortlist.md | head -3 | sed 's/^/    /'
  fi
  stages="$(awk '/^##+ /{h=$0} /^stage: /{if (h !~ /</) c[$2]++} END{for (s in c) printf "%s %d, ", s, c[s]}' bank/ideas.md)"
  [ -n "$stages" ] && echo "  seeds by stage: ${stages%, }"
  # The latest weekly tending run: one line per idea it tended (skills/job-scout, "The tending run")
  last_tend="$(ls sessions/tending-*.md 2>/dev/null | sort | tail -1)"
  if [ -n "$last_tend" ]; then
    echo "  last tending run: ${last_tend#sessions/tending-}" | sed 's/\.md$//'
    grep -E '^- ' "$last_tend" | sed 's/^- /    new: /'
  fi
  awk '/^##+ /{h=$0; sub(/^##+ /,"",h)} /^next_stage: [a-z]/{if (h !~ /</) {sub(/^next_stage: /,""); print "  stage move waiting for a yes: " h " -> " $0}}' bank/ideas.md
else
  echo "  no idea bank yet"
fi
if [ -f bank/credibility.md ]; then
  week_ago="${week_ago:-$(date -d '7 days ago' +%Y-%m-%d 2>/dev/null || date -v-7d +%Y-%m-%d)}"
  n="$(awk -v w="$week_ago" '/^log: [0-9]{4}-[0-9]{2}-[0-9]{2}/{if ($2 >= w) c++} END {print c+0}' bank/credibility.md)"
  echo "  credibility bank entries captured in the last 7 days: $n"
  echo "  credibility entries ready: $(awk '/^##+ /{h=$0} /^status: ready/{if (h !~ /</) n++} END{print n+0}' bank/credibility.md)"
  if [ -f canon/person/povs.md ]; then
    bare=""
    for p in $(awk '/^## P[0-9]+/{id=$2} /^status: confirmed/{if (id) print id; id=""}' canon/person/povs.md); do
      grep -qE "^backs:.*\b$p\b" bank/credibility.md || bare="$bare $p"
    done
    [ -n "$bare" ] && echo "  confirmed views with nothing in the credibility bank behind them:$bare"
  fi
else
  echo "  no credibility bank yet"
fi
[ -d inbox ] && echo "  inbox files waiting: $(find inbox -maxdepth 1 -type f ! -name README.md | wc -l)"

echo "PIECES"
found=0
for b in pieces/*/brief.md; do
  [ -f "$b" ] || continue
  found=1
  s="$(grep -m1 '^status:' "$b" | awk '{print $2}')"
  sch="$(grep -m1 '^scheduled:' "$b" | awk '{print $2}')"
  case "$sch" in [0-9][0-9][0-9][0-9]-*) sch=" · scheduled $sch";; *) sch="";; esac
  dir="$(dirname "$b")"
  grep -q '^path:[[:space:]]*direct' "$b" && kind=" · direct" || kind=""
  # the verdict of the latest review (highest version number), when there is one
  rv="$(ls "$dir"/review-v*.md 2>/dev/null | sort -V | tail -n1)"
  v=""; [ -n "$rv" ] && v="$(grep -m1 '^verdict:' "$rv" | awk '{print $2}')"
  case "$v" in pass|revise|redo) v=" · verdict $v";; *) v="";; esac
  # reviewed but never shown: the person hasn't seen it yet (CLAUDE.md rule 9)
  [ -n "$rv" ] && [ "$s" = drafted ] && v="$v · review ready, not shown yet"
  # a review is of one exact draft: when the draft's hash no longer matches, the verdict doesn't cover it
  if [ -n "$rv" ]; then
    want="$(grep -m1 '^draft_sha256:' "$rv" | awk '{print $2}')"
    case "$want" in [0-9a-f][0-9a-f][0-9a-f][0-9a-f]*)
      dn="$(grep -m1 '^draft:' "$rv" | awk '{print $2}')"
      [ -z "$dn" ] && dn="draft-v$(grep -m1 '^draft_version:' "$rv" | awk '{print $2}').md"
      if [ -f "$dir/$dn" ]; then
        have="$(sha256sum "$dir/$dn" 2>/dev/null | awk '{print $1}')"
        [ -n "$have" ] && [ "$have" != "$want" ] && v="$v · $dn edited after its review"
      fi;;
    esac
  fi
  echo "  $(basename "$dir"): ${s:-no status}$kind$v$sch"
done
[ "$found" = 0 ] && echo "  none yet"

echo "PROPOSALS"
if [ -f proposals.md ]; then
  # a proposal is a "## " heading plus its fields; only a block whose status line says open counts
  echo "  open: $(awk '/^## /{h=$0; next} /^status:[ \t]*open([ \t]|$)/{if (h != "" && h !~ /</) n++; h=""} END{print n+0}' proposals.md)"
else
  echo "  none"
fi

echo "TOOLS"
if [ -f config/tools.md ]; then
  awk '/^## /{section=$2} /^- (connected|channels):/{sub(/^- /,""); print "  " section ": " $0}' config/tools.md
else
  echo "  config/tools.md not created yet"
fi
