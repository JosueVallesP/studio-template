#!/usr/bin/env python3
"""Runs the house-rules test set: each case in cases.json must fail, flag or pass as its `expect` says,
under the same check the scripts and hooks use (scripts/studio_checks.house_check).
Usage, from anywhere: python3 tests/studio/house-rules/run.py"""
import json, os, sys
HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, os.path.join(HERE, "..", "..", "..", "scripts"))
import studio_checks as sc
ok = bad = 0
for c in json.load(open(os.path.join(HERE, "cases.json"), encoding="utf-8")):
    fails, flags = sc.house_check(c["text"], reply=c.get("reply", False), allow=set(c.get("allow", [])))
    got = "fail" if fails else "flag" if flags else "pass"
    rule_ok = True
    if c["expect"] in ("fail", "flag") and c.get("rule"):
        rule_ok = any(r.startswith(c["rule"]) for r, _, _ in (fails if c["expect"] == "fail" else flags))
    if c["expect"] == "pass" and got == "flag" and not c.get("strict"):
        got = "pass"          # a flag is a note for the judge, not a fail; "pass" means no fails
    if got == c["expect"] and rule_ok:
        ok += 1; print(f"ok   {c['id']} ({got})")
    else:
        bad += 1; print(f"FAIL {c['id']}: expected {c['expect']} {c.get('rule','')}, got {got} {fails or flags}")
print(f"{ok} passed, {bad} failed")
sys.exit(1 if bad else 0)
