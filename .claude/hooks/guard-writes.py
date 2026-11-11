# PreToolUse hook on Write and Edit: each crew agent writes only its own files (CLAUDE.md rule 6,
# enforced). The main session is never limited. The lists below are the whole permission table and
# the one place it's written down; docs and other files point here rather than copy it.
import json, sys, os, fnmatch
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from guard_common import agent_of, root_of
try:
    d = json.load(sys.stdin)
except Exception:
    sys.exit(0)
agent = agent_of(d)
path = (d.get("tool_input") or {}).get("file_path") or (d.get("tool_input") or {}).get("path") or ""
if not agent or not path:
    sys.exit(0)                      # main session, or not a file write: nothing to guard
root = root_of(d)
ap = os.path.abspath(os.path.join(root, path))
if not ap.startswith(root + os.sep):
    sys.exit(0)                      # scratch outside the repo is fine
rel = os.path.relpath(ap, root).replace(os.sep, "/")

common = ["studio-notes.md", "proposals.md", "pieces/*/log.md"]
allowed = {
    # canon/bank/stories.md and proof.md: capture adds `also:` blocks to an existing entry there, nothing else.
    "capture":    ["bank/ideas.md", "bank/credibility.md", "bank/questions.md", "bank/evidence.md",
                   "canon/bank/stories.md", "canon/bank/proof.md", "inbox/*", "inbox/**"],
    "writer":     ["pieces/*/draft-*.md", "pieces/*/brief.md"],
    "judge":      ["pieces/*/review-*.md", "pieces/*/brief.md"],
    "librarian":  ["bank/evidence.md", "bank/ideas.md", "bank/credibility.md", "pieces/index.md",
                   "pieces/librarian-last-run.md", "pieces/*/brief.md"],
}
if agent not in allowed:
    sys.exit(0)                      # an agent the studio doesn't know (the person's own); don't guess
ok = any(fnmatch.fnmatch(rel, p) for p in allowed[agent] + common)
if ok:
    sys.exit(0)
reason = (f"The {agent} doesn't write {rel}. Its files are: " + ", ".join(allowed[agent] + common) +
          ". If the piece needs this change, write it to proposals.md or the piece's log.md and say so; "
          "the person or the producer makes it (CLAUDE.md rule 6).")
print(json.dumps({"hookSpecificOutput": {"hookEventName": "PreToolUse",
                  "permissionDecision": "deny", "permissionDecisionReason": reason}}))
sys.exit(0)
