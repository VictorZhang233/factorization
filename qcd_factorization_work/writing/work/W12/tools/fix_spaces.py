import re, sys, glob, os
parts = sorted(glob.glob(os.path.join(sys.argv[1], 'p*.tex')))
pat = re.compile(r'\\(uses|cref|Cref|crefrange)\{([^{}]*)\}')
total = 0
for f in parts:
    s = open(f, encoding='utf-8').read()
    n = 0
    def rep(m):
        global total
        nonlocal_n[0] += 0
        inner = m.group(2)
        new = re.sub(r'\s*,\s*', ',', inner).strip()
        if new != inner:
            nonlocal_n[0] += 1
        return '\\' + m.group(1) + '{' + new + '}'
    nonlocal_n = [0]
    s2 = pat.sub(rep, s)
    if s2 != s:
        open(f, 'w', encoding='utf-8').write(s2)
    print(os.path.basename(f), nonlocal_n[0])
    total += nonlocal_n[0]
print('total fixed', total)
