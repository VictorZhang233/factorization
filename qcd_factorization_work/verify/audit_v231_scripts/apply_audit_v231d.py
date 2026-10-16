"""Audit fixes v2.3.1, part d: header revisions, a changelog item and the writer QA script (after parts a-c).

Usage:  python3 -I apply_audit_v231d.py SPECDIR
"""
import sys, os

SP = sys.argv[1]
EDITS = [
    ('WRITER_SPEC_v2.md',
     "and to **revision v2.3** by the verify patch (2026-10-11; all verification outcomes applied — see CHANGELOG)",
     "to **revision v2.3** by the verify patch (2026-10-11; all verification outcomes applied — see CHANGELOG), and to **revision v2.3.1** by the audit of that patch (`AUDIT_v2_patch.md`)"),
    ('WRITER_SPEC_v2.md', "- `refs_merged_v2.bib` (1003 entries), `key_aliases_v2.tsv`",
     "- `refs_merged_v2.bib` (1051 entries since v2.3), `key_aliases_v2.tsv`"),
    ('WRITER_SPEC_v2.md',
     "4. §6.12: verification bookkeeping is never printed (exceptions: App Q's 核实 column, the novelty wording of §6.5).\n",
     "4. §6.12: verification bookkeeping is never printed (exceptions: App Q's 核实 column, the novelty wording of §6.5).\n"
     "5. QA (§10): `checks/check_unit_v2.py` C8a now also flags the retired comment form `% PENDING-VERIFY:`; C8b additionally shows 「本书新结果」「首次」「文献中未见」 (allowed only for `prop:appN-triangle-cs`(a)) and printed bookkeeping (「独立确认」「尚待」) for justification.\n"),
    ('VERIFIED_FORMULAS_v2.md',
     "(current revision **v2.1**, same day: VF-EXC-14, VF-FRO-17, pending register keyed to `verify/CLAIMS.md` — see CHANGELOG)",
     "(revision v2.1, same day: VF-EXC-14, VF-FRO-17, pending register keyed to `verify/CLAIMS.md`; current revision **v2.3.1**: verify patch v2.3 and its audit — see CHANGELOG)"),
    ('checks/check_unit_v2.py',
     " C8 (a) printed planning markers ([PENDING-VERIFY], 待文献核查) -- must be absent (the comment '% PENDING-VERIFY: ...'\n",
     " C8 (a) planning markers ([PENDING-VERIFY], 待文献核查, and since spec v2.3 also the retired comment form '% PENDING-VERIFY: ...')\n    -- must be absent (audit v2.3.1; the original wording follows) (the comment '% PENDING-VERIFY: ...'\n"),
    ('checks/check_unit_v2.py',
     "FORBIDDEN = ['严格证明了', '已被证明', '软因子等于 1', '格点检验了因子化', 'Glauber 胶子在单举截面中总是相消',\n             '[PENDING-VERIFY]', '待文献核查', '偶极子公式对所有阶精确']",
     "FORBIDDEN = ['严格证明了', '已被证明', '软因子等于 1', '格点检验了因子化', 'Glauber 胶子在单举截面中总是相消',\n             '[PENDING-VERIFY]', '待文献核查', '偶极子公式对所有阶精确',\n             # audit v2.3.1: novelty words (allowed only for prop:appN-triangle-cs(a), WRITER_SPEC_v2 Sec. 6.5) and\n             # printed verification bookkeeping (WRITER_SPEC_v2 Sec. 6.12)\n             '本书新结果', '首次', '文献中未见', '独立确认', '尚待']"),
    ('checks/check_unit_v2.py',
     "    markers = [w for w in ('[PENDING-VERIFY]', 'PENDING-VERIFY]', '待文献核查') if w in t.replace('% PENDING-VERIFY:', '')]",
     "    markers = [w for w in ('[PENDING-VERIFY]', 'PENDING-VERIFY', '待文献核查') if w in t]  # v2.3.1: comment form retired too"),
    ('checks/check_unit_v2.py',
     "    print('C8a printed planning markers (must be absent; the comment form % PENDING-VERIFY: is allowed):', markers or 'OK')",
     "    print('C8a planning markers (must be absent, including the retired comment form % PENDING-VERIFY:):', markers or 'OK')"),
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
