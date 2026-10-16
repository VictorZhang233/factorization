"""Audit fixes v2.3.1, part b: status sentences of two register entries (applied after apply_audit_v231.py).

Usage:  python3 -I apply_audit_v231b.py SPECDIR
Exact-match replacements (each must match exactly once). The register tables of FINAL_OUTLINE_v2 §08 and
ASSUMPTIONS.md §1 receive the identical replacement, so that they stay identical (AUDIT_v2_patch.md §3).
"""
import sys, os

SP = sys.argv[1]
FO, AS = 'FINAL_OUTLINE_v2.md', 'ASSUMPTIONS.md'
EDITS = []

# asm:appM-forward: X3 Cor. F.2 needs (A3), (Eε) (through Thm B) and JL; OSWI only gives an alternative route
# to the gluon point omega = 0 (X3 Lemma F.8); it is not an input of the reduction.
ROW_OLD = "`cor:appM-forward-ope` reduces it to (A3), (Eε), the Joglekar–Lee triangularity and `asm:appM-oswi`;"
ROW_NEW = ("`cor:appM-forward-ope` reduces it to (A3), (Eε) and the Joglekar–Lee triangularity (the gluon point "
           "$\\omega=0$ also follows from `asm:appM-oswi` via `lem:appM-gluon-regularity`, without "
           "`thm:appM-brst-reduction`);")
EDITS += [(FO, ROW_OLD, ROW_NEW), (AS, ROW_OLD, ROW_NEW)]
EDITS.append((FO, "reduces `asm:appM-forward` to (A3), (Eε), the Joglekar–Lee triangularity and, for gluons, `asm:appM-oswi`;",
                  "reduces `asm:appM-forward` to (A3), (Eε) and the Joglekar–Lee triangularity (for gluons at $\\omega=0$ alternatively `asm:appM-oswi`, `lem:appM-gluon-regularity`);"))
EDITS.append((AS, "把本假设化归为 (A3)、(Eε)、Joglekar–Lee 三角性与胶子的 `asm:appM-oswi`——化归而非解除",
                  "把本假设化归为 (A3)、(Eε) 与 Joglekar–Lee 三角性（胶子在 $\\omega=0$ 处的正则性也可由 `asm:appM-oswi` 经 `lem:appM-gluon-regularity` 得到，不经 `thm:appM-brst-reduction`）——化归而非解除"))
EDITS.append((AS, "((A3), (Eε), the Joglekar–Lee triangularity, `asm:appM-oswi`); Ch25 OP-A5.",
                  "((A3), (Eε), the Joglekar–Lee triangularity); Ch25 OP-A5."))

# asm:appN-lce: X2 Cor. A.5 note -- Lemma A.2 cannot replace (LCE) (for a single-signed density (IL2) is the
# integrability that the corollary concludes); Lemma A.2 also needs (IL1)-(IL3), not only (FR).
LCE_OLD = "[A]: proved for each graph by `lem:appN-identification` once (FR) is checked; open as a statement for all graphs"
LCE_NEW = ("[A]: the standard equivalence of light-front (light-cone-ordered) and covariant perturbation theory, not "
           "proved at the rigour of App N; `lem:appN-identification` cannot replace it (for a single-signed density "
           "its hypothesis (IL2) is the integrability that `cor:appN-cs3-fibered` concludes); proved directly for the "
           "Collins terms of the one-loop triangle and for the one-rung ladder")
EDITS += [(FO, LCE_OLD, LCE_NEW), (AS, LCE_OLD, LCE_NEW)]
EDITS.append((AS, "[A]：对每个检验了 (FR) 的图由 `lem:appN-identification` 证明；作为对所有图的陈述开放（光前微扰论与协变微扰论的等价）。",
                  "[A]：光前（光锥序）微扰论与协变微扰论的标准等价，未在 App N 的严格度下证明；`lem:appN-identification` 不能代替它（对定号密度，其前提 (IL2) 正是 `cor:appN-cs3-fibered` 要得出的可积性；它还需要 (IL1)、(IL3)）；对单圈离壳三角图的四个减除项与单梯级梯形图已直接证明（`prop:appN-triangle-cs`(b)、`prop:appN-phi36-dis`(c)）。"))
EDITS.append((AS, "- **文献：** `Ligterink:1994tm`, `Schoonderwoerd:1998qj`, `Schoonderwoerd:1998iy` (equivalence of light-front and covariant perturbation theory).",
                  "- **文献：** `Chang:1973qi`, `Ligterink:1994tm`, `Schoonderwoerd:1998qj`, `Schoonderwoerd:1998iy` (equivalence of light-front and covariant perturbation theory); `Collins:2018aqt` (where the elementary light-front derivation fails)."))

APPEND = [(AS, """
**2026-10-11 — revision v2.3.1 (audit of the verify patch; `AUDIT_v2_patch.md`).** Status sentences corrected, tags unchanged: `asm:appM-forward` (the reduction of `cor:appM-forward-ope` needs (A3), (Eε) and the Joglekar–Lee triangularity; `asm:appM-oswi` is only an alternative route to the gluon point $\\omega=0$); `asm:appN-lce` (`lem:appN-identification` cannot replace it; literature completed). §1 kept identical to FINAL_OUTLINE_v2 §08.
""")]


def main():
    texts = {}
    for fn, old, new in EDITS:
        texts.setdefault(fn, open(os.path.join(SP, fn), encoding='utf-8').read())
        n = texts[fn].count(old)
        if n != 1:
            raise SystemExit('ABORT: %s: %d matches for %r' % (fn, n, old[:90]))
        texts[fn] = texts[fn].replace(old, new)
    for fn, add in APPEND:
        texts.setdefault(fn, open(os.path.join(SP, fn), encoding='utf-8').read())
        texts[fn] = texts[fn].rstrip('\n') + '\n' + add
    for fn, t in texts.items():
        open(os.path.join(SP, fn), 'w', encoding='utf-8').write(t)
        print('written', fn)
    print('%d edits' % len(EDITS))


if __name__ == '__main__':
    main()
