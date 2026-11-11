#!/usr/bin/env python3
"""The house rules on the studio's own replies (skills/craft-house-rules, Part 2). Two modes, one file.

  stop    (Stop hook) Read the reply the studio just finished from the transcript and run
          scripts/check-prose.py --mode reply on it. A script-level fail (an em dash, a filler opener,
          machine vocabulary, process narration) sends the reply back once to be said again plainly
          ({"decision": "block"}). On the second pass (stop_hook_active) the reply stands, so nothing
          loops, and the breaks are saved to .claude/.reply-check.json for the next turn instead. Flags
          never block; they're saved as notes.
  prompt  (UserPromptSubmit hook) If the last reply left breaks or notes behind, put a short line in front
          of Claude before it answers, then clear them. Never blocks.

Never crashes: on any error it exits 0 and the reply goes out as written.
"""
import json, os, subprocess, sys

MODE = sys.argv[1] if len(sys.argv) > 1 else "stop"

def read_input():
    try: return json.loads(sys.stdin.read() or "{}")
    except Exception: return {}

def state_path(root): return os.path.join(root, ".claude", ".reply-check.json")

def load_state(root):
    try: return json.load(open(state_path(root), encoding="utf-8"))
    except Exception: return {}

def save_state(root, st):
    try:
        os.makedirs(os.path.dirname(state_path(root)), exist_ok=True)
        json.dump(st, open(state_path(root), "w", encoding="utf-8"))
    except Exception: pass

def last_reply(path):
    """Every assistant text block since the last real user message (tool results are user records too)."""
    texts = []
    try: lines = open(path, encoding="utf-8").read().splitlines()
    except Exception: return ""
    for line in lines:
        try: rec = json.loads(line)
        except Exception: continue
        msg = rec.get("message") or {}
        role = msg.get("role") or rec.get("type")
        content = msg.get("content")
        if role == "user":
            is_tool_result = isinstance(content, list) and content and all(isinstance(c, dict) and c.get("type") == "tool_result" for c in content)
            if not is_tool_result: texts = []
        elif role == "assistant":
            if isinstance(content, str): texts.append(content)
            elif isinstance(content, list): texts += [c.get("text", "") for c in content if isinstance(c, dict) and c.get("type") == "text"]
    return "\n\n".join(t for t in texts if t)

def main():
    d = read_input()
    root = os.path.abspath(d.get("cwd") or os.environ.get("CLAUDE_PROJECT_DIR") or ".")

    if MODE == "prompt":
        st = load_state(root)
        pending = st.pop("pending", None)
        if pending:
            save_state(root, st)
            msg = ("Your last reply broke house rules a script can see (skills/craft-house-rules). Don't apologize or repeat it; "
                   "write this reply and the rest without them:\n- " + "\n- ".join(pending))
            print(json.dumps({"hookSpecificOutput": {"hookEventName": "UserPromptSubmit", "additionalContext": msg}}))
        sys.exit(0)

    path = d.get("transcript_path")
    if not path or not os.path.exists(path): sys.exit(0)
    text = last_reply(path)
    if len(text.split()) < 12: sys.exit(0)
    script = os.path.join(root, "scripts", "check-prose.py")
    if not os.path.exists(script): sys.exit(0)
    cmd = [sys.executable, "-I", script, "--stdin", "--mode", "reply", "--json"]
    voice = os.path.join(root, "canon", "voice", "voice-guide.md")
    if os.path.exists(voice): cmd += ["--voice", voice]
    try:
        r = subprocess.run(cmd, input=text, capture_output=True, text=True, timeout=25, cwd=root)
        report = json.loads(r.stdout or "{}")
    except Exception:
        sys.exit(0)
    fails, flags = report.get("fails", []), report.get("flags", [])
    if not fails and not flags: sys.exit(0)
    items = [f"{f['rule']} {f['what']}" for f in fails[:8]] + [f"{f['rule']} (likely) {f['what']}" for f in flags[:4]]

    if fails and not d.get("stop_hook_active"):
        reason = ("House rules (skills/craft-house-rules): the reply breaks " + str(len(fails)) + " script rule(s). "
                  "Say the same thing again without them, plainly, then stop. " + " || ".join(items[:8]))
        print(json.dumps({"decision": "block", "reason": reason}))
        sys.exit(0)

    st = load_state(root)
    sid = d.get("session_id") or "unknown"
    if st.get("session") != sid: st = {"session": sid, "counts": {}, "noted": []}
    st["pending"] = items
    is_master = os.path.exists(os.path.join(root, "studio.manifest.yaml")) and not os.path.exists(os.path.join(root, "studio-source.md"))
    for f in fails:
        rule = f["rule"]
        st["counts"][rule] = st["counts"].get(rule, 0) + 1
        if st["counts"][rule] == 2 and rule not in st["noted"] and not is_master:
            st["noted"].append(rule)
            try:
                with open(os.path.join(root, "studio-notes.md"), "a", encoding="utf-8") as fh:
                    fh.write(f"\n- reply check: house rule {rule} broke twice in one session in the studio's own replies\n")
            except Exception: pass
    save_state(root, st)
    sys.exit(0)

if __name__ == "__main__":
    main()
