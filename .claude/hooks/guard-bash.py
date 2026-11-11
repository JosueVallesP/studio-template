# PreToolUse hook on Bash: limits what a crew agent may run. Each role gets a short list of the
# studio's own scripts, plus read-only git (status, diff, log, show, ls-files), ls, wc, date, pwd and
# `mkdir -p pieces/...`. Nothing else runs. A command may chain allowed parts with && || ; or |, but
# any redirect (> or <), command substitution ($( or a backtick), newline or a lone & (a background
# job) is denied outright, so an allowed command can't be used to write a file or run something
# hidden. An output flag (--out, --targets, --log) may only name a path under pieces/ or bank/voiceprint/.
# The detector call (check-human.py --detector) is allowed for the judge only (the
# producer, in the main session, makes the call on the final). voiceprint.py is theirs and the
# librarian's, and never the writer's: the pass that wrote a draft doesn't measure it (rule 4).
# The main session (the person present) and an agent the studio doesn't know are not limited to a list;
# they only meet the short list of commands that destroy work (DESTRUCTIVE below), which asks first.
# A subagent call with no agent_type is treated as the main session; guard_common.py notes it once in studio-notes.md.
import json, sys, os, re
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from guard_common import agent_of, CREW
try:
    d = json.load(sys.stdin)
except Exception:
    sys.exit(0)
agent = agent_of(d)
cmd = ((d.get("tool_input") or {}).get("command") or "").strip()

# Outside the crew (the main session, or an agent the studio doesn't know), a short list of commands
# that destroy work asks first. The stop hook saves and pushes after every reply, so a deleted folder
# or a rewritten history reaches GitHub before anyone notices, and the people the studio is for can't
# dig it back out of git. "ask" shows the app's own approval prompt; nothing here denies outright.
# The studio's own scripts (update-studio.sh deletes inside the script) pass, since only the command
# text is read. Deleting inside a temp folder passes too.
DESTRUCTIVE = [
    (r"(?:^|[\s;&|(])rm\s+(?:-[a-zA-Z]*[rR][a-zA-Z]*|--recursive)\b", "deletes a folder and everything in it"),
    (r"(?:^|[\s;&|(])git\s+reset\s+(?:\S+\s+)*--hard\b", "throws away changes that haven't been saved"),
    (r"(?:^|[\s;&|(])git\s+push\b(?=[^;&|]*\s(?:--force(?:-with-lease)?|-f)\b)", "rewrites the history on GitHub, which can lose saved work"),
    (r"(?:^|[\s;&|(])git\s+clean\b(?=[^;&|]*\s-[a-zA-Z]*f)", "deletes files git isn't tracking"),
    (r"(?:^|[\s;&|(])git\s+(?:checkout|restore)\s+(?:\S+\s+)*(?:--\s+)?\.(?:\s|$)", "throws away every change in the folder"),
    (r"(?:^|[\s;&|(])git\s+branch\s+(?:\S+\s+)*-D\b", "deletes a branch even if its work isn't merged"),
]
TEMP_ONLY = re.compile(r"^\s*rm\s+-[a-zA-Z]+\s+(?:(?:/tmp/|\$TMPDIR/?|\"?\$TMP\"?/?)\S*\s*)+$")

if agent not in CREW:
    if cmd and not TEMP_ONLY.match(cmd):
        for rx, what in DESTRUCTIVE:
            if re.search(rx, cmd):
                print(json.dumps({"hookSpecificOutput": {"hookEventName": "PreToolUse",
                    "permissionDecision": "ask",
                    "permissionDecisionReason": f"This command {what}, and the studio saves to GitHub after every reply. "
                        "Say in plain words what it will remove and why, and run it only on the person's yes."}}))
                sys.exit(0)
    sys.exit(0)
if not cmd:
    sys.exit(0)

def deny(reason):
    print(json.dumps({"hookSpecificOutput": {"hookEventName": "PreToolUse",
                      "permissionDecision": "deny", "permissionDecisionReason": reason}}))
    sys.exit(0)

if re.search(r"[<>`\n\r]|\$\(", cmd) or re.search(r"(?<!&)&(?!&)", cmd):
    deny(f"The {agent} can't use redirects (> or <), $( ), backticks, newlines or a lone & in a command. "
         "Write files with the Write tool, and run one studio script at a time.")

# The dashboard syncs aren't listed: the stop hook runs them after every reply, so no agent needs to.
scripts = {
    "writer":     ["packet", "rewrites", "self-check", "check-mechanical", "check-human", "check-prose", "voice-diff", "check-stitch"],
    "judge":      ["self-check", "check-mechanical", "check-human", "check-prose", "voice-diff", "check-stitch", "voiceprint"],
    "capture":    ["inbox-to-text", "inbox-done"],
    "librarian":  ["rewrites", "check-human", "status", "voiceprint", "check-proposals"],
}
detector_ok = {"judge"}
ext = {"status": "sh"}           # every other script is .py

def script_ok(part):
    m = re.match(r"^(?:(?:python3|python)\s+(?:-I\s+)?scripts/([\w\-]+)\.py|bash\s+scripts/([\w\-]+)\.sh)(?:\s|$)", part)
    if not m:
        return False
    name = m.group(1) or m.group(2)
    kind = "py" if m.group(1) else "sh"
    if name not in scripts[agent] or ext.get(name, "py") != kind:
        return False
    words = part.split()
    if name == "check-human" and "--detector" in words and agent not in detector_ok:
        return False
    # A flag that names a file to write (voiceprint.py's --out, --targets, --log) may only point inside
    # pieces/ or bank/voiceprint/; an empty --log '' (skip the log) is fine.
    for i, w in enumerate(words):
        flag, eq, val = w.partition("=")
        if flag in OUTPUT_FLAGS:
            target = val if eq else (words[i + 1] if i + 1 < len(words) else "")
            target = target.strip("'\"")
            if target and (".." in target or not re.match(r"^(pieces|bank/voiceprint)/", target)):
                return False
    return True

OUTPUT_FLAGS = {"--out", "--targets", "--log"}

other = [
    r"^git\s+(status|diff|log|show|ls-files)(?!.*\s--output)(\s|$)",   # --output would write a file
    r"^(ls|wc|date|pwd)(\s|$)",
    r"^mkdir\s+-p\s+pieces/(?!.*\.\.)[\w./\-]*$",                      # no .. out of pieces/
]
parts = [p for p in re.split(r"\s*(?:&&|\|\||;|\|)\s*", cmd) if p]
if all(script_ok(p) or any(re.match(rx, p) for rx in other) for p in parts):
    sys.exit(0)
names = ", ".join(f"scripts/{n}.{ext.get(n, 'py')}" for n in scripts[agent])
extra = " (check-human without --detector; the judge makes that one call)" if agent == "writer" else ""
names = f"{names}{extra}, " if names else ""
deny(f"The {agent} runs only {names}read-only git (status, diff, log, show, ls-files), ls, wc, date, pwd "
     "and mkdir -p pieces/. Reading and editing files is done with the Read, Grep and Write tools. If a step truly needs "
     "another command, write it to studio-notes.md and stop; the person runs it.")
