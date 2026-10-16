# check_figblocks.py (writer W04): every %%% BEGIN/END fig block in the W04 units must be byte-identical
# to the block of writing/packs/W04/figblocks.tex (LEAD_DECISIONS LA-10).
import re, sys, os
W = '/Users/hao-cheng/Desktop/theorem proof/qcd_factorization_work'
pat = re.compile(r'%%% BEGIN (fig:[^\n]+)\n(.*?)%%% END \1', re.S)
ref = {m.group(1).strip(): m.group(2) for m in pat.finditer(open(os.path.join(W, 'writing/packs/W04/figblocks.tex'), encoding='utf-8').read())}
ok = True
seen = set()
for f in ['chapters/ch04_ir.tex', 'chapters/appD_landau.tex', 'chapters/appE_powercount.tex']:
    t = open(os.path.join(W, f), encoding='utf-8').read()
    for m in pat.finditer(t):
        lab = m.group(1).strip(); seen.add(lab)
        if lab not in ref:
            print('NOT IN PACK:', lab, f); ok = False
        elif m.group(2) != ref[lab]:
            print('DIFFERS:', lab, f); ok = False
        else:
            print('identical:', lab, '(', f, ')')
for lab in ref:
    if lab not in seen:
        print('pack block not used:', lab)
print('ALL IDENTICAL' if ok else 'PROBLEMS FOUND')
