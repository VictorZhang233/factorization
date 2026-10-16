"""Audit fixes v2.3.1, part e: precise credit for E02 (App Q row Q.11; inclusion rule 3).

Usage:  python3 -I apply_audit_v231e.py SPECDIR
PRD 105 (2022) 076014, footnote 1, notes the missing 1/2 for its refs. [22] (the RMP, `JiEtAl2021`) and [23]
(NPB 955; possibly a mis-citation, no explicit CS-exponent formula there) -- not for PLB 811 eq. (22) (`Ji:2019ewn`)
or APPB eqs. (53), (75) (`Liu:2022nnk`) (verify/claims/batch_E01_s1.md §3, batch_E01_s2.md §3).
"""
import sys, os

SP = sys.argv[1]
EDITS = [
    ('FINAL_OUTLINE_v2.md',
     "| **noted by the authors** in the journal version of `Ji:2021znw` (PRD 105 (2022) 076014, footnote 1), which is correct; correct form also `Ebert:2022fmh` and `Liu:2022nnk` eq. (52) |",
     "| for `JiEtAl2021` **noted by the authors** in the journal version of `Ji:2021znw` (PRD 105 (2022) 076014, footnote 1, which also names NPB 955; that journal version is correct); not noted for `Ji:2019ewn` eq. (22) or `Liu:2022nnk` eqs. (53), (75); correct form earlier in `EbertStewartZhao2019` eqs. (24), (27), also `Ebert:2022fmh` and `Liu:2022nnk` eq. (52) |"),
    ('FINAL_OUTLINE_v2.md',
     "Credit: the first published correction of E01 is `Chou:2022drv`; E02 was noted by the authors themselves (PRD 105 (2022) 076014, footnote 1).",
     "Credit: the first published correction of E01 is `Chou:2022drv`; for the RMP, E02 was noted by the authors themselves (PRD 105 (2022) 076014, footnote 1); the correct exponent was printed earlier by `EbertStewartZhao2019`."),
    ('WRITER_SPEC_v2.md',
     "E02 was noted by the authors themselves (PRD 105 (2022) 076014, footnote 1), whose journal version of `Ji:2021znw` is correct.",
     "E02 was noted for the RMP by the authors themselves (PRD 105 (2022) 076014, footnote 1), whose journal version of `Ji:2021znw` is correct (not noted for `Ji:2019ewn` eq. (22) or `Liu:2022nnk` eqs. (53), (75)); the correct exponent is earlier in `EbertStewartZhao2019`."),
    ('WRITER_SPEC_v2.md',
     "(App Q row Q.11; noted by the authors in PRD 105 (2022) 076014, footnote 1)",
     "(App Q row Q.11; for the RMP noted by the authors in PRD 105 (2022) 076014, footnote 1)"),
]


def main():
    for fn, old, new in EDITS:
        p = os.path.join(SP, fn)
        t = open(p, encoding='utf-8').read()
        if t.count(old) != 1:
            raise SystemExit('ABORT: %s: %d matches for %r' % (fn, t.count(old), old[:80]))
        open(p, 'w', encoding='utf-8').write(t.replace(old, new))
    print('%d edits' % len(EDITS))


if __name__ == '__main__':
    main()
