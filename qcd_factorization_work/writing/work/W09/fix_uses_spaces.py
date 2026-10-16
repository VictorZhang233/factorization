# -*- coding: utf-8 -*-
import re, os, glob
here = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'parts')
pat = re.compile(r'\\(uses|cref|Cref|crefrange|labelcref)\{([^{}]*)\}')
tot = 0
for p in sorted(glob.glob(os.path.join(here, '*.tex'))):
    s = open(p, encoding='utf-8').read()
    def rep(m):
        global tot
        inner = m.group(2)
        new = re.sub(r'\s*,\s*', ',', inner.strip())
        if new != inner:
            tot += 1
        return '\\%s{%s}' % (m.group(1), new)
    s2 = pat.sub(rep, s)
    if s2 != s:
        open(p, 'w', encoding='utf-8').write(s2)
        print('fixed', os.path.basename(p))
print('replacements', tot)
