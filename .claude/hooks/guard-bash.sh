#!/usr/bin/env bash
# PreToolUse hook on Bash: each crew agent runs its own short list of studio scripts and read-only
# git only; the main session is asked first before a command that destroys work. See guard-bash.py for the lists.
cd "${CLAUDE_PROJECT_DIR:-.}" 2>/dev/null
exec python3 -I "$(dirname "${BASH_SOURCE[0]}")/guard-bash.py"
