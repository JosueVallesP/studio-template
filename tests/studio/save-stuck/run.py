#!/usr/bin/env python3
"""The save stops when git was left halfway (a rebase or merge cut off, an unsettled clash, a file
still holding conflict markers), and saves normally once it's sorted. Throwaway repos in a temp folder.
Usage: python3 -I tests/studio/save-stuck/run.py"""
import os, shutil, subprocess, sys, tempfile
REPO = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "..", ".."))
ok = True
def check(name, cond, extra=""):
    global ok
    print(("ok   " if cond else "FAIL ") + name + ("" if cond else f"\n     {extra}"))
    ok = ok and cond
def git(t, *a): return subprocess.run(["git", "-c", "user.name=t", "-c", "user.email=t@t", *a], cwd=t, capture_output=True, text=True)
def fresh():
    t = tempfile.mkdtemp()
    os.makedirs(os.path.join(t, "scripts"))
    for f in ("save.sh", "scan-secrets.py"):
        shutil.copy(os.path.join(REPO, "scripts", f), os.path.join(t, "scripts", f))
    open(os.path.join(t, "studio-source.md"), "w").write("- version: test\n")
    open(os.path.join(t, "note.md"), "w").write("one\n")
    git(t, "init", "-q", "-b", "main"); git(t, "add", "-A"); git(t, "commit", "-qm", "start")
    return t
def save(t): return subprocess.run(["bash", "scripts/save.sh"], cwd=t, capture_output=True, text=True)
def commits(t): return len(git(t, "log", "--oneline").stdout.strip().splitlines())
def note(t):
    p = os.path.join(t, ".claude", ".save-failed")
    return open(p).read() if os.path.exists(p) else ""

t = fresh()
open(os.path.join(t, "note.md"), "w").write("<<<<<<< HEAD\nmine\n=======\ntheirs\n>>>>>>> abc123\n")
save(t)
check("conflict markers in a file stop the save", commits(t) == 1)
check("the note names the file in plain words", "note.md" in note(t) and "clash" in note(t), note(t))
open(os.path.join(t, "note.md"), "w").write("mine and theirs, settled\n")
save(t)
check("once settled, the save goes through", commits(t) == 2)
shutil.rmtree(t)

t = fresh()
os.makedirs(os.path.join(t, ".git", "rebase-merge"))
open(os.path.join(t, "note.md"), "w").write("two\n")
save(t)
check("an open rebase stops the save", commits(t) == 1 and "cut off" in note(t), note(t))
shutil.rmtree(t)

t = fresh()
git(t, "checkout", "-qb", "other"); open(os.path.join(t, "note.md"), "w").write("other\n"); git(t, "commit", "-qam", "o")
git(t, "checkout", "-q", "main"); open(os.path.join(t, "note.md"), "w").write("main\n"); git(t, "commit", "-qam", "m")
git(t, "merge", "other")
save(t)
check("an unsettled merge stops the save", commits(t) == 3 and "merge" in note(t) or "clash" in note(t), note(t))
shutil.rmtree(t)

t = fresh()
open(os.path.join(t, "essay.md"), "w").write("A line of equals signs below is just a heading underline.\nTitle\n=======\n")
save(t)
check("a heading underline isn't a clash", commits(t) == 2, note(t))
shutil.rmtree(t)

print("all passed" if ok else "some failed")
sys.exit(0 if ok else 1)
