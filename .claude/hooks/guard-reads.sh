#!/usr/bin/env bash
# PreToolUse hook on Read, Grep and Glob: keeps every crew agent out of bank/swipe/, the full text of
# other people's posts the person saved to read. The rule and its reason live in guard-reads.py.
cd "${CLAUDE_PROJECT_DIR:-.}" 2>/dev/null
exec python3 -I "$(dirname "${BASH_SOURCE[0]}")/guard-reads.py"
