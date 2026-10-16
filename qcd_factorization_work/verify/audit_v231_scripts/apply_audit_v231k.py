"""Audit fixes v2.3.1, part k: status note of prop:appM-zero-momentum-insertion (after parts a-j).

Usage:  python3 -I apply_audit_v231k.py SPECDIR
v2.3 printed as a fact that "the epsilon of Breitenlohner:1976te is the damping regulator of that construction, not the
dimension shift of DR". No verification record supports this; the X3 final report (verify/extend_reports/
X3-ope_final.md §2, "Checked: Breitenlohner-Maison II ... Thm 1") reads Thm 1 as a statement about the dimensionally
renormalized amplitude, and states that BM I and Lowenstein-Zimmermann were not read (its last table). The grade [A]
stays: the reviewed grade of X3 Remark F.5 was [A] (rev1-1, rev2-1, rev2-2, rev3-1), and its upgrade to [R, R_PT] in
the final round (W19) has no independent confirmation. Only the unverified sentence is replaced by the open point.
"""
import sys, os

SP = sys.argv[1]
FO = 'FINAL_OUTLINE_v2.md'
EDITS = [
    ("It settles, for off-shell forward two-point functions, the question left open in `rem:appM-exceptional`.",
     "Given the identification named in the status note, it settles, for off-shell forward two-point functions, the question left open in `rem:appM-exceptional`."),
    ("**地位与缺口.** [A]: the $\\varepsilon$ of `Breitenlohner:1976te` is the damping regulator of that construction, not the dimension shift of DR, and the identification of its limit with the dimensionally regularized $\\overline{\\rm MS}$ insertion used here rests on the relation between that paper and `Breitenlohner:1975hg`, which the verification did not check; upgrade path to [R, R_PT]: that identification written out, plus a second independent confirmation.",
     "**地位与缺口.** [A]: `Breitenlohner:1976te` Thm 1 applies (all vertices of IR degree $\\ge4$, fields of IR dimension $\\ge1$) and gives the $\\varepsilon\\to0$ limit as a tempered distribution; that this limit, in the framework set up in `Breitenlohner:1975hg`, is the dimensionally regularized $\\overline{\\rm MS}$ insertion used here has not been checked against that paper; upgrade path to [R, R_PT]: this identification written out and independently confirmed. (Writer's note, not printed: X3 Remark F.5 proposes [R, R_PT]; that grade was set in X3's final round without an independent confirmation, the reviewed grade is [A]; the v2.3 sentence calling the $\\varepsilon$ of `Breitenlohner:1976te` a damping regulator is not supported by the verification records and is not printed.)"),
    ("11. Checks re-run: `checks/check_final_outline_v2.py` E1–E14, W1–W2 OK;",
     "11. `prop:appM-zero-momentum-insertion` status note: the unverified sentence on the $\\varepsilon$ of `Breitenlohner:1976te` (\"damping regulator\") replaced by the open identification, and the claim that it 'settles' `rem:appM-exceptional` made conditional on it; grade [A] kept (reviewed grade of X3 Remark F.5).\n"
     "12. Checks re-run: `checks/check_final_outline_v2.py` E1–E14, W1–W2 OK;"),
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
