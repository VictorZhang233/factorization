"""Audit fixes v2.3.1, part i: version references and headers (after parts a-h).

Usage:  python3 -I apply_audit_v231i.py SPECDIR
The headers still named ASSUMPTIONS.md revision v2.3 (it now has a v2.3.1 entry), REFS_NOTES_v2 "current revision
v2.1 ... 1003 entries" (1051 since v2.3) and FIGURES_INDEX_v2 revision v2.2 (it has a v2.3 entry); the §0.8 heading
pointed to AUDIT_v2.md also for MD19. FIGURES_INDEX_v2 gets a v2.3.1 entry (regenerate from the v2.3.1 outline; the
pre-patch generator inputs under figures/ contain withdrawn slot labels).
"""
import sys, os

SP = sys.argv[1]
EDITS = [
    ('FINAL_OUTLINE_v2.md',
     "with the fixes and decisions listed in §0.8 and in `AUDIT_v2.md`. **The three outline drafts",
     "with the fixes and decisions listed in §0.8 and in `AUDIT_v2.md`; the verify patch v2.3 and its audit are recorded in MD19, the CHANGELOG and `AUDIT_v2_patch.md`. **The three outline drafts"),
    ('FINAL_OUTLINE_v2.md',
     "`WRITER_SPEC_v2.md` (revision v2.3.1), `ASSUMPTIONS.md` (revision v2.3), ",
     "`WRITER_SPEC_v2.md` (revision v2.3.1), `ASSUMPTIONS.md` (revision v2.3.1), "),
    ('FINAL_OUTLINE_v2.md',
     "### 0.8 Integrator (merge) decisions MD1–MD19 (binding unless the lead author overrides; justification in `AUDIT_v2.md`)",
     "### 0.8 Integrator (merge) decisions MD1–MD19 (binding unless the lead author overrides; justification in `AUDIT_v2.md`, for MD19 in `AUDIT_v2_patch.md`)"),
    ('FINAL_OUTLINE_v2.md',
     "9. Checks re-run: `checks/check_final_outline_v2.py` E1–E14, W1–W2 OK; `checks/keys_check.py`, `checks/figures_check.py` PASS; `checks/check_unit_v2.py` C8 updated (WRITER_SPEC_v2 CHANGELOG v2.3.1 items 5, 7).\n",
     "9. Version references: header (`ASSUMPTIONS.md` revision v2.3.1; `AUDIT_v2_patch.md`) and §0.8 heading; headers of `ASSUMPTIONS.md`, REFS_NOTES_v2 (current revision, 1051 entries) and FIGURES_INDEX_v2 (v2.3, v2.3.1).\n"
     "10. Checks re-run: `checks/check_final_outline_v2.py` E1–E14, W1–W2 OK; `checks/keys_check.py`, `checks/figures_check.py` PASS; `checks/check_unit_v2.py` C8 updated (WRITER_SPEC_v2 CHANGELOG v2.3.1 items 5, 7).\n"),
    ('WRITER_SPEC_v2.md',
     "the full register is `ASSUMPTIONS.md` (revision v2.3; binding texts",
     "the full register is `ASSUMPTIONS.md` (revision v2.3.1; binding texts"),
    ('WRITER_SPEC_v2.md',
     "7. §6.5 item 3: priority statements about cited works in the verified wording (Ch23: `Ji:2019sxk`, `Liu:2023pjb`; A03) are attributions and may contain 「首次」.\n",
     "7. §6.5 item 3: priority statements about cited works in the verified wording (Ch23: `Ji:2019sxk`, `Liu:2023pjb`; A03) are attributions and may contain 「首次」.\n"
     "8. Header: `ASSUMPTIONS.md` revision v2.3.1.\n"),
    ('ASSUMPTIONS.md',
     "**Status (revision v2.3, verify patch of 2026-10-11; merged revision v2.2).**",
     "**Status (revision v2.3.1, audit of the verify patch: two status sentences corrected, see CHANGELOG; revision v2.3, verify patch of 2026-10-11; merged revision v2.2).**"),
    ('ASSUMPTIONS.md',
     "§1 kept identical to FINAL_OUTLINE_v2 §08.",
     "§1 kept identical to FINAL_OUTLINE_v2 §08; header status line updated."),
    ('REFS_NOTES_v2.md',
     "(current revision **v2.1**, same day: 1003 entries, attribution rules A01–A28, App Q sources E01–E36 — see CHANGELOG)",
     "(revision v2.1, same day: 1003 entries, attribution rules A01–A28, App Q sources E01–E36; current revision **v2.3.1**: the verify patch v2.3 with 48 additions, 1051 entries, and its audit — see CHANGELOG)"),
    ('REFS_NOTES_v2.md',
     "Row A03 (I.5): the LPC priority sentence finalized (A03 confirmed). No key changed.",
     "Row A03 (I.5): the LPC priority sentence finalized (A03 confirmed); header revision updated. No key changed."),
    ('FIGURES_INDEX_v2.md',
     "**revision v2.2** by the spec-v2 integrator (merge with FINAL_OUTLINE_v2: App P generated per-part graphs, optional `fig:lamet-dependency`, confirmed section labels — see CHANGELOG).",
     "**revision v2.2** by the spec-v2 integrator (merge with FINAL_OUTLINE_v2: App P generated per-part graphs, optional `fig:lamet-dependency`, confirmed section labels), **revision v2.3** by the verify patch and **revision v2.3.1** by its audit (2026-10-11) — see CHANGELOG."),
]
APPEND = ('FIGURES_INDEX_v2.md',
          "**2026-10-11 — v2.3.1 (audit of the verify patch; `AUDIT_v2_patch.md`).**\n"
          "1. Header revision.\n"
          "2. The generated figures of v2.3 item 3 are regenerated from the v2.3.1 outline (cells of nine master rows of §09 rewritten; labels, tags and `\\uses` unchanged). The generator inputs `figures/test_fa/uses.json` and `figures/test_ff/scripts/outline.json` predate the verify patch and contain withdrawn slot labels: rebuild them from FINAL_OUTLINE_v2, never reuse them.\n")


def main():
    for fn, old, new in EDITS:
        p = os.path.join(SP, fn)
        t = open(p, encoding='utf-8').read()
        if t.count(old) != 1:
            raise SystemExit('ABORT: %s: %d matches for %r' % (fn, t.count(old), old[:80]))
        open(p, 'w', encoding='utf-8').write(t.replace(old, new))
    fn, block = APPEND
    p = os.path.join(SP, fn)
    t = open(p, encoding='utf-8').read()
    if '— v2.3.1 (audit of the verify patch' in t:
        raise SystemExit('ABORT: %s already has the v2.3.1 entry' % fn)
    open(p, 'w', encoding='utf-8').write(t.rstrip('\n') + '\n\n' + block)
    print('%d edits + 1 append' % len(EDITS))


if __name__ == '__main__':
    main()
