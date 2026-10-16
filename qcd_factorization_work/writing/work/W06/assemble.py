r"""assemble.py -- writer W06: concatenate the parts into chapters/ch06_ee.tex and chapters/appC_dimreg.tex;
lines '%%FIG:<name>%%' are replaced by the verbatim figure block parts/<name>.tex (copied from packs/W06/figblocks.tex)."""
import os, re
here = os.path.dirname(os.path.abspath(__file__))
root = os.path.abspath(os.path.join(here, '..', '..', '..'))
parts = os.path.join(here, 'parts')


def expand(fn):
    out = []
    for line in open(os.path.join(parts, fn), encoding='utf-8'):
        m = re.match(r'^%%FIG:([A-Za-z0-9_]+)%%\s*$', line)
        if m:
            out.append(open(os.path.join(parts, m.group(1) + '.tex'), encoding='utf-8').read())
        else:
            out.append(line)
    return ''.join(out)


ch = ''.join(expand(f) + '\n' for f in ['p0_intro.tex', 'p1_R.tex', 'p2_analytic.tex', 'p3_euclid.tex', 'p4_theorem.tex',
                                         'p5_oneloop.tex', 'p6_higher.tex', 'p7_ope.tex', 'p8_duality.tex'])
open(os.path.join(root, 'chapters', 'ch06_ee.tex'), 'w', encoding='utf-8').write(ch.rstrip('\n') + '\n')
ap = expand('c_all.tex')
open(os.path.join(root, 'chapters', 'appC_dimreg.tex'), 'w', encoding='utf-8').write(ap.rstrip('\n') + '\n')
print('written', len(ch.splitlines()), 'and', len(ap.splitlines()), 'lines')
