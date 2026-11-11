#!/usr/bin/env python3
"""Moves one processed inbox file to inbox/done/, with today's date in front of its name.

  python3 scripts/inbox-done.py inbox/<file>

The file lands at inbox/done/<YYYY-MM-DD>_<name> (the folder is made when it doesn't exist) and the
script prints the new path. It refuses a path outside inbox/, a file already in inbox/done/, and a
name that's already taken there. Run from the instance root; capture runs it once per file it has
turned into idea bank entries.
"""
import os, shutil, sys
from datetime import date

def main():
    if len(sys.argv) != 2 or sys.argv[1] in ("-h", "--help"):
        print(__doc__); sys.exit(2)
    root = os.path.abspath(os.getcwd())
    inbox = os.path.join(root, "inbox")
    done = os.path.join(inbox, "done")
    src = os.path.realpath(os.path.join(root, sys.argv[1]))
    if not src.startswith(os.path.realpath(inbox) + os.sep):
        print(f"refused: {sys.argv[1]} is not inside inbox/", file=sys.stderr); sys.exit(1)
    if src.startswith(os.path.realpath(done) + os.sep):
        print(f"refused: {sys.argv[1]} is already in inbox/done/", file=sys.stderr); sys.exit(1)
    if not os.path.isfile(src):
        print(f"refused: {sys.argv[1]} is not a file", file=sys.stderr); sys.exit(1)
    os.makedirs(done, exist_ok=True)
    dst = os.path.join(done, f"{date.today().isoformat()}_{os.path.basename(src)}")
    if os.path.exists(dst):
        print(f"refused: {os.path.relpath(dst, root)} already exists", file=sys.stderr); sys.exit(1)
    shutil.move(src, dst)
    print(os.path.relpath(dst, root))

if __name__ == "__main__":
    main()
