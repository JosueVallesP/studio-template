#!/usr/bin/env python3
"""Looks for passwords, API keys and tokens in what's about to be saved, before the save pushes it to
GitHub. The save runs after every reply and pushes on its own, and the people the studio is for can't
scrub a key out of git history, so a key-shaped string stops the save instead.

Usage: python3 -I scripts/scan-secrets.py            # the staged changes (save.sh runs it this way)
       python3 -I scripts/scan-secrets.py --text FILE # one file, for the tests
Prints one line per file with the kind of key found, never the key itself. Exit 1 when anything is found.
Only lines being added are read; a key already in history isn't this script's job.
"""
import re, subprocess, sys

PATTERNS = [
    ("an OpenAI or Anthropic-style API key", re.compile(r"\bsk-(?:ant-|proj-)?[A-Za-z0-9_\-]{20,}")),
    ("a Slack token", re.compile(r"\bxox[abprs]-[A-Za-z0-9\-]{10,}")),
    ("a GitHub token", re.compile(r"\b(?:gh[pousr]_[A-Za-z0-9]{30,}|github_pat_[A-Za-z0-9_]{30,})")),
    ("an AWS access key", re.compile(r"\bAKIA[0-9A-Z]{16}\b")),
    ("a private key", re.compile(r"-----BEGIN (?:[A-Z]+ )*PRIVATE KEY-----")),
    ("a signed token (JWT)", re.compile(r"\beyJ[A-Za-z0-9_\-]{10,}\.eyJ[A-Za-z0-9_\-]{10,}\.[A-Za-z0-9_\-]{10,}")),
    ("a Notion token", re.compile(r"\b(?:ntn_[A-Za-z0-9]{30,}|secret_[A-Za-z0-9]{40,})")),
    ("a Google API key", re.compile(r"\bAIza[0-9A-Za-z_\-]{35}\b")),
    ("a Stripe key", re.compile(r"\b(?:sk|rk)_live_[0-9A-Za-z]{20,}")),
    ("a key set in a file", re.compile(r"(?i)\b[A-Z0-9_]*(?:API_KEY|SECRET|TOKEN|PASSWORD)\s*=\s*['\"]?[A-Za-z0-9_\-\.]{16,}")),
]

def scan(lines_by_file):
    found = {}
    for f, lines in lines_by_file.items():
        for line in lines:
            for kind, rx in PATTERNS:
                if rx.search(line):
                    found.setdefault(f, set()).add(kind)
    return found

def staged():
    out = subprocess.run(["git", "diff", "--cached", "-U0", "--no-color", "--no-ext-diff"],
                         capture_output=True, text=True, errors="replace").stdout
    by, cur = {}, None
    for line in out.splitlines():
        if line.startswith("+++ "):
            cur = line[6:] if line.startswith("+++ b/") else None
        elif cur and line.startswith("+") and not line.startswith("+++"):
            by.setdefault(cur, []).append(line[1:])
    return by

def main():
    if "--text" in sys.argv:
        f = sys.argv[sys.argv.index("--text") + 1]
        by = {f: open(f, encoding="utf-8", errors="replace").read().splitlines()}
    else:
        by = staged()
    found = scan(by)
    for f, kinds in sorted(found.items()):
        print(f"{f}: looks like {', '.join(sorted(kinds))}")
    sys.exit(1 if found else 0)

if __name__ == "__main__":
    main()
