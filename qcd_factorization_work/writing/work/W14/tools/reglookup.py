r"""W14 helper: look up owner/type/tag/title of labels in the FINAL_OUTLINE_v2 registry (section 08).
Usage: python3 -I reglookup.py OUTLINE file1.tex [file2.tex ...]   -> all \cref/\uses/\ref labels of the files
       python3 -I reglookup.py OUTLINE -l lab1 lab2 ...              -> the given labels
"""
import re, sys
outline = sys.argv[1]
o = open(outline, encoding='utf-8').read()
reg = {}
cur = None
in08 = False
for line in o.split('\n'):
    if line.startswith('## 08'):
        in08 = True; continue
    if in08 and line.startswith('## ') and not line.startswith('## 08'):
        in08 = False
    if not in08:
        continue
    m = re.match(r'^###\s+(Ch\d\d|App[A-Q]|front|Assumptions)\b', line)
    if m:
        cur = m.group(1); continue
    m = re.match(r'^\|\s*`([a-z]+:[A-Za-z0-9\-]+)`\s*\|([^|]*)\|([^|]*)\|([^|]*)\|', line)
    if m and cur:
        reg.setdefault(m.group(1), (cur, m.group(2).strip(), m.group(3).strip(), m.group(4).strip()))
args = sys.argv[2:]
if args and args[0] == '-l':
    labs = args[1:]
else:
    labs = set()
    defined = set()
    for fn in args:
        t = open(fn, encoding='utf-8').read()
        for mm in re.finditer(r'\\(?:c?ref|Cref|uses)\{([^}]+)\}', t):
            for r in mm.group(1).split(','):
                labs.add(r.strip())
        defined |= set(re.findall(r'\\label\{([^}]+)\}', t))
    labs = sorted(l for l in labs if l not in defined and not l.startswith('eq:'))
for l in labs:
    print('%-45s %s' % (l, reg.get(l, 'NOT IN REGISTRY')))
