"""Audit fixes v2.3.1, part c: banners on superseded records (applied after parts a and b).

Usage:  python3 -I apply_audit_v231c.py SPECDIR
The three outline drafts still contain the pre-patch [PENDING-VERIFY] markers, planning tags and the withdrawn slot
labels; AUDIT_v2.md still contains the pre-patch go/no-go table. Both are records, not inputs; the banners make this
explicit (AUDIT_v2_patch.md §2, check P1).
"""
import sys, os

SP = sys.argv[1]
OLD_DRAFT = ("this file is kept unchanged below as the drafter's record.\n")
NEW_DRAFT = ("this file is kept unchanged below as the drafter's record.\n"
             ">\n"
             "> **VOID MARKERS (2026-10-11, audit v2.3.1).** The `[PENDING-VERIFY]` markers, planning tags, reserved slot "
             "labels and candidate texts below were resolved by the verify patch v2.3 in `FINAL_OUTLINE_v2.md` "
             "(§0.10, §00.4, §10); the undelivered slot labels are withdrawn and must not be used. Nothing in this file "
             "may be copied into a unit.\n")

AUDIT_OLD = "# AUDIT_v2 — integration and adversarial audit of spec v2\n"
AUDIT_NEW = ("# AUDIT_v2 — integration and adversarial audit of spec v2\n\n"
             "> **SUPERSEDED IN PART (2026-10-11).** The verify patch v2.3 resolved the pending items of this audit; "
             "its audit is `AUDIT_v2_patch.md`, whose go/no-go table (§5) replaces §6 below. The merge decisions MD1–MD18 "
             "and the defect log of §3–§4 remain valid as records.\n")


def rep(fn, old, new):
    p = os.path.join(SP, fn)
    t = open(p, encoding='utf-8').read()
    if t.count(old) != 1:
        raise SystemExit('ABORT: %s: %d matches' % (fn, t.count(old)))
    open(p, 'w', encoding='utf-8').write(t.replace(old, new))
    print('written', fn)


for fn in ('OUTLINE_core.md', 'OUTLINE_appMNOPQ.md', 'OUTLINE_frontier.md'):
    rep(fn, OLD_DRAFT, NEW_DRAFT)
rep('AUDIT_v2.md', AUDIT_OLD, AUDIT_NEW)
