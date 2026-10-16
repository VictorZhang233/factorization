#!/usr/bin/env python3
"""Assemble chapters/ch21_power.tex from writing/work/W24/parts/p*.tex.
Figure markers %%FIG:<name>%% are replaced by the verbatim figure blocks parts/<name>.tex
(copied from writing/packs/W24/figblocks.tex, identical to the figure sources; LA-10)."""
import os, re, sys
here = os.path.dirname(os.path.abspath(__file__))
parts = os.path.join(here, 'parts')
order = ['p0_intro.tex', 'p1_twist4.tex', 'p2_twist3.tex', 'p3_nlp.tex', 'p4_opebasis.tex',
         'p5_renormalons.tex', 'p6_np.tex']
out = []
for fn in order:
    s = open(os.path.join(parts, fn), encoding='utf-8').read()
    def repl(m):
        blk = open(os.path.join(parts, m.group(1) + '.tex'), encoding='utf-8').read().rstrip('\n')
        return blk
    s, n = re.subn(r'%%FIG:([A-Za-z0-9_]+)%%', repl, s)
    out.append(s.rstrip('\n') + '\n')
text = '\n'.join(out)
dest = os.path.join(here, '..', '..', '..', 'chapters', 'ch21_power.tex')
open(dest, 'w', encoding='utf-8').write(text)
print('written', os.path.normpath(dest), len(text), 'chars;', text.count('%%% BEGIN fig:'), 'figure blocks')
assert '%%FIG:' not in text
