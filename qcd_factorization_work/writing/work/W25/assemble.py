#!/usr/bin/env python3
"""Assemble chapters/ch22_lamet.tex from parts/p*.tex; '%%% FIGBLOCK fig:X' lines are replaced verbatim by the
figure block of writing/packs/W25/figblocks.tex (LA-10) or, for the optional Ch22 figures that are not in the pack,
by the identical block of figures/figset_D.tex (the figure source listed in figures/FIGURES_STATUS.md)."""
import os, re, sys, glob
here = os.path.dirname(os.path.abspath(__file__))
root = os.path.abspath(os.path.join(here, '..', '..', '..'))
packs = open(os.path.join(root, 'writing', 'packs', 'W25', 'figblocks.tex'), encoding='utf-8').read()
figD = open(os.path.join(root, 'figures', 'figset_D.tex'), encoding='utf-8').read()
def block(src, lab):
    beg = '%%% BEGIN ' + lab + '\n'
    end = '%%% END ' + lab
    a = src.find(beg)
    if a < 0: return None
    b = src.index(end, a) + len(end)
    return src[a:b]
out = []
for p in sorted(glob.glob(os.path.join(here, 'parts', 'p[0-9][0-9]_*.tex'))):
    txt = open(p, encoding='utf-8').read()
    def rep(m):
        lab = m.group(1)
        b = block(packs, lab) or block(figD, lab)
        if b is None: sys.exit('missing figure block ' + lab)
        return b
    txt = re.sub(r'^%%% FIGBLOCK (fig:[A-Za-z0-9\-]+)\s*$', rep, txt, flags=re.M)
    out.append(txt.rstrip('\n') + '\n')
target = os.path.join(root, 'chapters', 'ch22_lamet.tex')
open(target, 'w', encoding='utf-8').write('\n'.join(out))
print('wrote', target, sum(len(t) for t in out), 'chars from', len(out), 'parts')
