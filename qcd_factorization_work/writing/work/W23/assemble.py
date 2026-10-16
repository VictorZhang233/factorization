# Assemble chapters/ch20_heavy.tex from the parts; figure blocks are inserted verbatim at the %%INSERT markers.
import os, re, sys
here = os.path.dirname(os.path.abspath(__file__))
parts = os.path.join(here, 'parts')
order = ['p0_head.tex', 'p1_bdpi.tex', 'p2_qcdf.tex', 'p3_inclusive.tex', 'p4_nrqcd.tex', 'p5_summary.tex']
out = []
for fn in order:
    t = open(os.path.join(parts, fn), encoding='utf-8').read()
    def ins(m):
        return open(os.path.join(parts, m.group(1)), encoding='utf-8').read().rstrip('\n')
    t = re.sub(r'(?m)^%%INSERT (\S+)\s*$', ins, t)
    out.append(t.rstrip('\n') + '\n')
txt = '\n'.join(out)
dest = os.path.join(here, '..', '..', '..', 'chapters', 'ch20_heavy.tex')
open(dest, 'w', encoding='utf-8').write(txt)
print('written', os.path.normpath(dest), len(txt), 'chars')
