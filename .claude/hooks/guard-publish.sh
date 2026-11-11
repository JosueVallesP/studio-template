#!/usr/bin/env bash
# PreToolUse hook on the publishing connectors: booking, posting, moving or cancelling asks first.
# See guard-publish.py.
cd "${CLAUDE_PROJECT_DIR:-.}" 2>/dev/null
exec python3 -I "$(dirname "${BASH_SOURCE[0]}")/guard-publish.py"
