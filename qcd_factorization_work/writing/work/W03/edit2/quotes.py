# replace ASCII double quotes in Chinese prose by curly quotes (pairwise per line); comments untouched
import re, sys
files = sys.argv[1:]
for p in files:
    lines = open(p, encoding='utf-8').read().split('\n')
    out = []; n = 0
    for ln in lines:
        if ln.lstrip().startswith('%') or '"' not in ln:
            out.append(ln); continue
        code = ln.split('%')[0] if '%' in ln and not '\\%' in ln else ln
        cnt = code.count('"')
        assert cnt % 2 == 0, (p, ln[:120])
        res = []; k = 0
        for ch in ln:
            if ch == '"':
                res.append('“' if k % 2 == 0 else '”'); k += 1; n += 1
            else:
                res.append(ch)
        out.append(''.join(res))
    open(p, 'w', encoding='utf-8').write('\n'.join(out))
    print(p, 'replaced', n)
