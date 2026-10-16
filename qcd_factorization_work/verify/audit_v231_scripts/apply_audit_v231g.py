"""Audit fixes v2.3.1, part g: CHANGELOG items for parts b, e, f (after parts a-f).

Usage:  python3 -I apply_audit_v231g.py SPECDIR
"""
import sys, os

SP = sys.argv[1]
EDITS = [
    ('FINAL_OUTLINE_v2.md',
     "5. Checks re-run: `checks/check_final_outline_v2.py` E1–E14, W1–W2 OK; `checks/keys_check.py`, `checks/figures_check.py` PASS.\n",
     "5. Register (§08 `### Assumptions`, identical in `ASSUMPTIONS.md` §1; tags unchanged): status of `asm:appM-forward` (`cor:appM-forward-ope` needs (A3), (Eε), Joglekar–Lee; `asm:appM-oswi` is only an alternative route to the gluon point) and of `asm:appN-lce` (`lem:appN-identification` cannot replace it); Ch25 OP-A5 likewise.\n"
     "6. App Q row Q.11 and the credit line: PRD 105 footnote 1 notes the missing ½ for the RMP only; not noted for `Ji:2019ewn` eq. (22) or `Liu:2022nnk` eqs. (53), (75); the correct exponent was printed earlier by `EbertStewartZhao2019`.\n"
     "7. §09: claim IDs, slot IDs and 「已证实」 removed from the cells of rows II.1, II.8, II.27, II.29, III.4, III.5, III.27, VII.28, VII.46 (these cells are transcribed into the printed tables); content, labels and tags unchanged.\n"
     "8. Checks re-run: `checks/check_final_outline_v2.py` E1–E14, W1–W2 OK; `checks/keys_check.py`, `checks/figures_check.py` PASS; `checks/check_unit_v2.py` C8 updated (WRITER_SPEC_v2 CHANGELOG v2.3.1 item 5).\n"),
    ('WRITER_SPEC_v2.md',
     "(「独立确认」「尚待」) for justification.\n",
     "(「独立确认」「尚待」) for justification.\n"
     "6. §6.13, §3 row 43: the E02 credit is limited to the RMP (PRD 105 footnote 1); not noted for `Ji:2019ewn` or `Liu:2022nnk`.\n"),
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
