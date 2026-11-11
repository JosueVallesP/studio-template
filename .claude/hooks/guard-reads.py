# PreToolUse hook on Read, Grep and Glob: no crew agent reads the full text of other people's posts.
# bank/swipe/ holds whole pieces the person saved to read for inspiration. The crew (the writer above
# all) works from bank/swipe-file.md instead, which keeps the moves and one short quote, so there are no
# sentences to borrow (job-teardown, "Learn the move, never copy the piece"). The main session, with the
# person present, reads bank/swipe/ when the person asks to see a piece. A Grep or Glob aimed at bank/
# or the whole repo still runs; one aimed at bank/swipe/ is denied.
import json, sys, os
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from guard_common import agent_of, root_of, CREW
try:
    d = json.load(sys.stdin)
except Exception:
    sys.exit(0)
agent = agent_of(d)
if agent not in CREW:
    sys.exit(0)                      # main session, or an agent the studio doesn't know
ti = d.get("tool_input") or {}
root = root_of(d)
targets = [ti.get("file_path") or "", ti.get("path") or "", ti.get("pattern") or "", ti.get("glob") or ""]

def hits_swipe(t):
    if not t:
        return False
    t = t.replace(os.sep, "/")
    if os.path.isabs(t):
        t = os.path.relpath(os.path.abspath(t), root).replace(os.sep, "/")
    t = t.lstrip("./")
    return t == "bank/swipe" or t.startswith("bank/swipe/") or "/bank/swipe/" in t or t.startswith("swipe/")

# Grep's pattern is text to search for, not a path; only its path and glob point at files.
checked = targets if d.get("tool_name") != "Grep" else [targets[1], targets[3]]
if any(hits_swipe(t) for t in checked):
    reason = (f"The {agent} doesn't read bank/swipe/: those are other people's whole posts, kept for the person "
              "to read. Use the moves in bank/swipe-file.md, never the piece's sentences.")
    print(json.dumps({"hookSpecificOutput": {"hookEventName": "PreToolUse",
                      "permissionDecision": "deny", "permissionDecisionReason": reason}}))
sys.exit(0)
