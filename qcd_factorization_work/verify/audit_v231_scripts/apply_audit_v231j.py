"""Audit fixes v2.3.1, part j: App Q cross-references of E12 and E29 (after parts a-i).

Usage:  python3 -I apply_audit_v231j.py SPECDIR
The Ch19 note on `Guo:2021ibg` said "not an App Q row" and the Ch6 verification paragraph "E29 is history only (no App Q
row)", while App Q prints both as author corrections in `tab:appQ-errata-b` (rows Q.18 = E12, Q.20 = E29), as do
WRITER_SPEC_v2 §6.13, VERIFIED_FORMULAS_v2 (VF-EE-10) and REFS_NOTES_v2 §3.5 (verify/claims/batch_E07_s1.md,
batch_E07_s2.md for E12; batch_E25_s1.md, batch_E26_s2.md for E29).
"""
import sys, os

SP = sys.argv[1]
FO = 'FINAL_OUTLINE_v2.md'
EDITS = [
    ("corrected by the authors in `Guo:2023pqw` §II — cite where used, not an App Q row).",
     "corrected by the authors in `Guo:2023pqw` §II — cite where used; it is listed among the author corrections of App Q, `tab:appQ-errata-b` (row Q.18, E12), not in `tab:appQ-errata`)."),
    ("— the earlier GKL value was corrected (history only, E29) —",
     "— the earlier GKL value was corrected (history only here; listed among the author corrections of App Q, `tab:appQ-errata-b`, row Q.20, E29) —"),
    ("A09 (OPE status wording as verified); E29 is history only (no App Q row).",
     "A09 (OPE status wording as verified); E29 confirmed as an author correction: a history sentence in this chapter and row Q.20 of `tab:appQ-errata-b` (App Q)."),
    ("10. Checks re-run: `checks/check_final_outline_v2.py` E1–E14, W1–W2 OK;",
     "10. App Q cross-references: the notes \"not an App Q row\" (E12, Ch19) and \"no App Q row\" (E29, Ch6) contradicted `tab:appQ-errata-b` (rows Q.18, Q.20); corrected.\n"
     "11. Checks re-run: `checks/check_final_outline_v2.py` E1–E14, W1–W2 OK;"),
]


def main():
    p = os.path.join(SP, FO)
    t = open(p, encoding='utf-8').read()
    for old, new in EDITS:
        if t.count(old) != 1:
            raise SystemExit('ABORT: %s: %d matches for %r' % (FO, t.count(old), old[:80]))
        t = t.replace(old, new)
    open(p, 'w', encoding='utf-8').write(t)
    print('%d edits' % len(EDITS))


if __name__ == '__main__':
    main()
