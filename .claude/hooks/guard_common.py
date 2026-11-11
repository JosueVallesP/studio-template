"""Shared by guard-writes.py and guard-bash.py: who is calling, and a visible note when a subagent
call arrives without an agent_type (the guards can't tell which role it is, so they don't apply)."""
import os
from datetime import date

CREW = {"capture", "writer", "judge", "librarian"}

def root_of(d):
    return os.path.abspath(d.get("cwd") or os.environ.get("CLAUDE_PROJECT_DIR") or ".")

def agent_of(d):
    """The crew role making the call, or "" for the main session. When the input has an agent_id
    but no agent_type, write one line to studio-notes.md, once per session, and return ""."""
    agent = (d.get("agent_type") or "").strip()
    if agent or not d.get("agent_id"):
        return agent
    try:
        root = root_of(d)
        marker = os.path.join(root, ".claude", ".guard-noted")
        session = str(d.get("session_id") or "")
        seen = open(marker, encoding="utf-8").read().split() if os.path.exists(marker) else []
        if session not in seen:
            os.makedirs(os.path.dirname(marker), exist_ok=True)
            with open(marker, "a", encoding="utf-8") as f:
                f.write(session + "\n")      # marker first, so a failed note is never written twice
            notes = os.path.join(root, "studio-notes.md")
            lead = ""
            if os.path.exists(notes) and os.path.getsize(notes):
                with open(notes, "rb") as f:
                    f.seek(-1, os.SEEK_END); lead = "" if f.read(1) == b"\n" else "\n"
            with open(notes, "a", encoding="utf-8") as f:
                f.write(f"{lead}- {date.today().isoformat()} · guard · subagent call with no agent_type; guards did not apply\n")
    except Exception:
        pass                         # a note that can't be written never blocks the call
    return ""
