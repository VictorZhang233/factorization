"""Assemble the W10 unit files from the parts, substituting the verbatim figure blocks.

    python3 -I build_unit.py            -> writes chapters/ch09_method.tex and chapters/appF_ward.tex
                                           and copies them (with the common files) into writing/test/W10/
Figure blocks are copied verbatim from writing/packs/W10/figblocks.tex (LA-10); a part requests a block with a line
'%%FIG fig:label%%'.
"""
import os, re, shutil, sys
HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.abspath(os.path.join(HERE, '..', '..', '..'))
blocks_src = open(os.path.join(ROOT, 'writing', 'packs', 'W10', 'figblocks.tex'), encoding='utf-8').read()
BLOCKS = {lab: blk for blk, lab in re.findall(r'(%%% BEGIN (fig:[\w-]+)\n.*?%%% END \2\n)', blocks_src, re.S)}
UNITS = {
    'ch09_method.tex': ['ch09_p0_intro.tex', 'ch09_p1_strategy.tex', 'ch09_p2_regions.tex', 'ch09_p3_gy.tex',
                        'ch09_p4_ward.tex', 'ch09_p5_subtraction.tex', 'ch09_p6_unitarity.tex',
                        'ch09_p7_glauber.tex', 'ch09_p8_template.tex'],
    'appF_ward.tex': ['appF_p0.tex'],
}
used = set()
for unit, parts in UNITS.items():
    out = []
    for p in parts:
        fn = os.path.join(HERE, 'parts', p)
        if not os.path.exists(fn):
            print('  (missing part %s, skipped)' % p); continue
        txt = open(fn, encoding='utf-8').read()
        def sub(m):
            lab = m.group(1)
            if lab not in BLOCKS: sys.exit('unknown figure block ' + lab)
            used.add(lab)
            return BLOCKS[lab].rstrip('\n')
        txt = re.sub(r'^%%FIG (fig:[\w-]+)%%$', sub, txt, flags=re.M)
        out.append(txt.rstrip('\n') + '\n')
    dst = os.path.join(ROOT, 'chapters', unit)
    open(dst, 'w', encoding='utf-8').write('\n'.join(out))
    shutil.copy(dst, os.path.join(ROOT, 'writing', 'test', 'W10', unit))
    print('wrote', dst)
print('figure blocks used:', sorted(used))
print('figure blocks NOT used:', sorted(set(BLOCKS) - used))
for f, src in [('preamble_fact.tex', 'common/preamble_fact.tex'), ('refs_merged_v2.bib', 'spec_v2/refs_merged_v2.bib'),
               ('FINAL_OUTLINE_v2.md', 'spec_v2/FINAL_OUTLINE_v2.md'), ('check_unit_v2.py', 'spec_v2/checks/check_unit_v2.py')]:
    shutil.copy(os.path.join(ROOT, src), os.path.join(ROOT, 'writing', 'test', 'W10', f))
