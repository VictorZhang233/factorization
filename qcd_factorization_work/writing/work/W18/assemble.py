# Assemble chapters/ch15_scet.tex from writing/work/W18/parts/*.tex:
#  - splice the figure blocks verbatim from writing/packs/W18/figblocks.tex (LA-10);
#  - normalize label lists in \uses{...}, \cref{...}, \Cref{...} (cleveref does not strip blanks after commas).
import re, sys, os
root = sys.argv[1]
W = os.path.join(root, 'writing/work/W18/parts/')
parts = ['p0_intro.tex', 'p1_modes.tex', 'p2_lagrangian.tex', 'p3_decoupling.tex', 'p4_scet2.tex',
         'p5_glauber.tex', 'p6_thrust.tex', 'p7_rg.tex', 'p8_status.tex']
txt = ''.join(open(W + p, encoding='utf-8').read().rstrip('\n') + '\n\n' for p in parts)
fb = open(os.path.join(root, 'writing/packs/W18/figblocks.tex'), encoding='utf-8').read()
def block(name):
    return re.search(r'(%%% BEGIN ' + re.escape(name) + r'\n.*?%%% END ' + re.escape(name) + r')\n', fb, re.S).group(1)
for name in ('fig:scet-wilson', 'fig:dijet-factorization'):
    pat = re.compile(r'%%% BEGIN ' + re.escape(name) + r'\n.*?%%% END ' + re.escape(name), re.S)
    assert len(pat.findall(txt)) == 1, name
    b = block(name)
    txt = pat.sub(lambda m: b, txt)
def norm(m):
    return m.group(1) + '{' + ','.join(x.strip() for x in m.group(2).split(',')) + '}'
txt = re.sub(r'(\\uses|\\cref|\\Cref)\{([^{}]*)\}', norm, txt)
for name in ('fig:scet-wilson', 'fig:dijet-factorization'):
    assert block(name) in txt, name
open(os.path.join(root, 'chapters/ch15_scet.tex'), 'w', encoding='utf-8').write(txt)
print('assembled', len(txt), 'chars')
