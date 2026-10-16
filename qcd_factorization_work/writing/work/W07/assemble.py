"""Assemble chapters/ch07_dis.tex from parts/*.tex (in the order of ORDER), replacing each line
'%%INSERT fig:<label>' by the verbatim block '%%% BEGIN fig:<label>' ... '%%% END fig:<label>' of
writing/packs/W07/figblocks.tex (LA-10: figure blocks are copied verbatim)."""
import os, re, sys
here = os.path.dirname(os.path.abspath(__file__))
root = os.path.abspath(os.path.join(here, '..', '..', '..'))
figsrc = os.path.join(root, 'writing', 'packs', 'W07', 'figblocks.tex')
ORDER = ['p00_intro', 'p01_kinematics', 'p02_compton', 'p03a_ope', 'p03b_ope', 'p04_np', 'p05_moments_rg',
         'p06_wilson', 'p07_xspace', 'p08_ht_pol', 'p09_summary']
blocks = {}
txt = open(figsrc, encoding='utf-8').read()
for m in re.finditer(r'(%%% BEGIN (fig:[\w\-]+)\n.*?%%% END \2\n)', txt, re.S):
    blocks[m.group(2)] = m.group(1)
out, used = [], []
for name in ORDER:
    p = os.path.join(here, 'parts', name + '.tex')
    if not os.path.exists(p):
        print('missing part (skipped):', name); continue
    for line in open(p, encoding='utf-8'):
        m = re.match(r'^%%INSERT (fig:[\w\-]+)\s*$', line)
        if m:
            lab = m.group(1)
            if lab not in blocks:
                sys.exit('no figure block for ' + lab)
            out.append(blocks[lab]); used.append(lab)
        else:
            out.append(line)
    out.append('\n')
target = sys.argv[1] if len(sys.argv) > 1 else os.path.join(root, 'chapters', 'ch07_dis.tex')
open(target, 'w', encoding='utf-8').write(''.join(out).rstrip('\n') + '\n')
print('wrote', target, '; figures inserted:', used, '; unused blocks:', sorted(set(blocks) - set(used)))
