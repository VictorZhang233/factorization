import re, sys
outline = open(sys.argv[2], encoding='utf-8').read()
unit = open(sys.argv[1], encoding='utf-8').read()
# registry rows: | `label` | type | tag | title |
reg = {}
for m in re.finditer(r'^\|\s*`([a-zA-Z]+:[^`]+)`\s*\|\s*([^|]*)\|\s*([^|]*)\|', outline, re.M):
    lab, typ, tag = m.group(1), m.group(2).strip(), m.group(3).strip()
    reg.setdefault(lab, (typ, tag))
envs = 'definition|assumption|theorem|lemma|proposition|corollary|conjecture|example|remark'
pat = re.compile(r'\\begin\{(' + envs + r')\}(\[[^\n]*?\])?\\label\{([^}]+)\}(.*?)\\end\{\1\}', re.S)
for m in pat.finditer(unit):
    env, title, lab, body = m.group(1), m.group(2) or '', m.group(3), m.group(4)
    u = re.search(r'\\uses\{([^}]*)\}', body)
    uses = u.group(1).split(',') if u else []
    mytag = reg.get(lab, ('?', '?'))[1]
    print(f'== {lab}  [{mytag}]')
    for x in uses:
        x = x.strip()
        t = reg.get(x, ('NOT-IN-REGISTRY', ''))
        print(f'     {x:42s} {t[1]}')
