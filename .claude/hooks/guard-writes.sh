#!/usr/bin/env bash
# PreToolUse hook on Write and Edit: the crew's permissions, enforced instead of asked for.
# Rule 6 in CLAUDE.md says nobody but the person changes the canon, and the spec gives each role a
# write list. Skills say this; this script makes it so. It reads the tool call from stdin and denies
# a crew agent any write outside its list. The main session (the person is in the room) is never
# blocked, because setup, /learn and /review write the canon with the person present.
# Each role's list is in guard-writes.py, the one source; it isn't repeated here.
# A subagent call with no agent_type isn't guarded; guard_common.py notes it once in studio-notes.md.
cd "${CLAUDE_PROJECT_DIR:-.}" 2>/dev/null
exec python3 -I "$(dirname "${BASH_SOURCE[0]}")/guard-writes.py"
