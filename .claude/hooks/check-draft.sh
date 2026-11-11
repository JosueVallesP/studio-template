#!/usr/bin/env bash
# PostToolUse hook on Write and Edit. Any person-facing file (finals, briefs, proposals, canon drafts)
# gets scripts/check-prose.py, the house rules a script can see. The person's own words are skipped:
# material/, inbox/, journal/, bank/ (the idea bank and rewrites included) and canon/bank/; check-draft.py
# has the list. When a piece's draft file is written, run the mechanical checks on it. check-mechanical's fails go back as fails to fix; check-human's flags go back in a
# separate paragraph as evidence for the editor, not fails. The writer's skill says to run them; this
# makes sure a draft that fails never reaches the editor unseen. Drafts under tests/ are skipped. The
# detector is never called here (one paid call per piece, made by the judge).
cd "${CLAUDE_PROJECT_DIR:-.}" 2>/dev/null
exec python3 -I "$(dirname "${BASH_SOURCE[0]}")/check-draft.py"
