#!/usr/bin/env bash
# Stop and UserPromptSubmit hook: the house rules on the studio's own replies (see check-reply.py).
# "stop" checks the reply that just ended and sends it back once if a script rule broke; "prompt" puts
# any leftover note in front of Claude before it answers. Runs in the master repo and in every instance.
cd "${CLAUDE_PROJECT_DIR:-.}" 2>/dev/null
exec python3 -I "$(dirname "${BASH_SOURCE[0]}")/check-reply.py" "${1:-stop}"
