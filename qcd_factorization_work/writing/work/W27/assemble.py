#!/usr/bin/env python3
"""Assemble chapters/ch24_front.tex from parts/p*.tex; insert the figure blocks verbatim from
writing/packs/W27/figblocks.tex (LA-10) at the markers %%FIGBLOCK <label>%%."""
import os, re, glob, sys
W = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.abspath(os.path.join(W, '..', '..', '..'))
fb = open(os.path.join(ROOT, 'writing', 'packs', 'W27', 'figblocks.tex'), encoding='utf-8').read()
blocks = {}
for m in re.finditer(r'(%%% BEGIN (fig:[A-Za-z0-9\-]+)\n.*?%%% END \2)', fb, re.S):
    blocks[m.group(2)] = m.group(1)
parts = sorted(glob.glob(os.path.join(W, 'parts', 'p[0-9][0-9]_*.tex')))
out = []
used = set()
for p in parts:
    t = open(p, encoding='utf-8').read()
    def rep(m):
        lab = m.group(1); used.add(lab)
        return blocks[lab]
    t = re.sub(r'%%FIGBLOCK (fig:[A-Za-z0-9\-]+)%%', rep, t)
    out.append(t.rstrip('\n') + '\n')
txt = '\n'.join(out)
dest = sys.argv[1] if len(sys.argv) > 1 else os.path.join(ROOT, 'chapters', 'ch24_front.tex')
open(dest, 'w', encoding='utf-8').write(txt)
print('parts:', [os.path.basename(p) for p in parts])
print('figure blocks inserted:', sorted(used), ' available:', sorted(blocks))
