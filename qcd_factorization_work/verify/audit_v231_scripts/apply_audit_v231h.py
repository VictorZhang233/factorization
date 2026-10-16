"""Audit fixes v2.3.1, part h (after parts a-g).

Usage:  python3 -I apply_audit_v231h.py SPECDIR
1. thm:ee-euclid-ir status note: the BM II hypotheses with their limits as recorded in verify/claims/batch_N18_s2.md
   §7.4 (claim N24: FP ghosts not discussed explicitly by BM; distributional existence theorem; pointwise statement
   from Poggio-Quinn, BPHZL from Lowenstein-Zimmermann; the two-point function suffices by its (Q^2)^{-k eps}
   structure); the bookkeeping clause "carried out in the verification (N24)" is removed.
2. Priority statements about cited works (Ch23, claim A03 items A1, A6) may contain 「首次」: WRITER_SPEC_v2 §6.5
   item 3, its CHANGELOG item 5, and the comment of checks/check_unit_v2.py (the checker only shows the word, C8b).
3. CHANGELOG bookkeeping (script list; items 8, 9 of FINAL_OUTLINE_v2; item 7 of WRITER_SPEC_v2).
"""
import sys, os

SP = sys.argv[1]
EDITS = [
    ('FINAL_OUTLINE_v2.md',
     "地位注: the explicit check that the Breitenlohner–Maison hypotheses are spelled out for non-abelian gauge fields with FP ghosts in covariant gauges was carried out in the verification (N24): all interaction terms of massless QCD in covariant gauges, ghost terms included, have IR degree $\\ge4$, as `Breitenlohner:1976te` requires; the gauge-invariant current correlator is gauge independent (`prop:qcd-xi-independence`).",
     "地位注: the hypothesis of `Breitenlohner:1976te` (every interaction term of IR degree $\\ge4$) holds for massless QCD in covariant gauges, ghost terms included (IR dimension $\\frac32$ for quarks, $1$ for gluons and ghosts, $+1$ per derivative); BM name Yang–Mills fields with vector-like fermions among their examples but do not discuss Faddeev–Popov ghosts explicitly, and their existence theorem is a statement about distributions — the pointwise statement at non-exceptional momenta is that of `PoggioQuinn1976` (for BPHZL subtractions `LowensteinZimmermann1975`), and for the current two-point function the distributional statement suffices because of its explicit $(Q^2)^{-k\\varepsilon}$ structure; the gauge-invariant current correlator is gauge independent (`prop:qcd-xi-independence`)."),
    ('FINAL_OUTLINE_v2.md',
     "Script `verify/audit_v231_scripts/apply_audit_v231.py` (exact-match edits on the v2.3 files; backup `verify/audit_v231_backup/`).",
     "Scripts `verify/audit_v231_scripts/apply_audit_v231.py` and `apply_audit_v231b.py`–`apply_audit_v231h.py` (exact-match edits on the v2.3 files, run in order by `apply_all_v231.py`; backup `verify/audit_v231_backup/`)."),
    ('FINAL_OUTLINE_v2.md',
     "8. Checks re-run: `checks/check_final_outline_v2.py` E1–E14, W1–W2 OK; `checks/keys_check.py`, `checks/figures_check.py` PASS; `checks/check_unit_v2.py` C8 updated (WRITER_SPEC_v2 CHANGELOG v2.3.1 item 5).\n",
     "8. `thm:ee-euclid-ir` 地位注: the Breitenlohner–Maison hypotheses with their limits (ghosts not discussed explicitly by BM; distributional existence theorem; pointwise statement from `PoggioQuinn1976`, BPHZL `LowensteinZimmermann1975`); the bookkeeping clause removed.\n"
     "9. Checks re-run: `checks/check_final_outline_v2.py` E1–E14, W1–W2 OK; `checks/keys_check.py`, `checks/figures_check.py` PASS; `checks/check_unit_v2.py` C8 updated (WRITER_SPEC_v2 CHANGELOG v2.3.1 items 5, 7).\n"),
    ('WRITER_SPEC_v2.md',
     "the only printed marker is 「本书新结果（据我们截至 2026 年 10 月的文献检索…）」 on `prop:appN-triangle-cs`(a).\n",
     "the only printed marker is 「本书新结果（据我们截至 2026 年 10 月的文献检索…）」 on `prop:appN-triangle-cs`(a). Priority statements about cited works in the verified wording of FINAL_OUTLINE_v2 (Ch23: `Ji:2019sxk` and `Liu:2023pjb`, each introduced by 「据我们所知」; claim A03) are attributions, not claims of novelty of this book, and may contain 「首次」.\n"),
    ('WRITER_SPEC_v2.md',
     "C8b additionally shows 「本书新结果」「首次」「文献中未见」 (allowed only for `prop:appN-triangle-cs`(a))",
     "C8b additionally shows 「本书新结果」「首次」「文献中未见」 (the novelty words only for `prop:appN-triangle-cs`(a); 「首次」 also in the two verified priority statements of Ch23, §6.5 item 3)"),
    ('WRITER_SPEC_v2.md',
     "6. §6.13, §3 row 43: the E02 credit is limited to the RMP (PRD 105 footnote 1); not noted for `Ji:2019ewn` or `Liu:2022nnk`.\n",
     "6. §6.13, §3 row 43: the E02 credit is limited to the RMP (PRD 105 footnote 1); not noted for `Ji:2019ewn` or `Liu:2022nnk`.\n"
     "7. §6.5 item 3: priority statements about cited works in the verified wording (Ch23: `Ji:2019sxk`, `Liu:2023pjb`; A03) are attributions and may contain 「首次」.\n"),
    ('checks/check_unit_v2.py',
     "             # audit v2.3.1: novelty words (allowed only for prop:appN-triangle-cs(a), WRITER_SPEC_v2 Sec. 6.5) and\n",
     "             # audit v2.3.1: novelty words (only for prop:appN-triangle-cs(a); '首次' also in the two verified priority\n"
     "             # statements of Ch23 about cited works, WRITER_SPEC_v2 Sec. 6.5 item 3) and\n"),
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
