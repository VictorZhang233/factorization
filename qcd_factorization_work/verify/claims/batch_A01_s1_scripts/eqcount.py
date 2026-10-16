# Rough LaTeX equation counter (JHEP-style numbering per section): reports the equation number at given line numbers.
# Usage: python3 -I eqcount.py file.tex line1 [line2 ...]
import re, sys
src = open(sys.argv[1], encoding='utf-8', errors='replace').read().split('\n')
targets = set(int(a) for a in sys.argv[2:])
sec = 0; eq = 0; in_env = None; app = False; appidx = 0
cur_rows = []
def strip_comments(l):
    return re.sub(r'(?<!\\)%.*', '', l)
for i, raw in enumerate(src, 1):
    l = strip_comments(raw)
    if re.search(r'\\appendix', l): app = True; sec = 0
    m = re.search(r'\\section\*?\{', l)
    if m and not re.search(r'\\section\*', l):
        sec += 1; eq = 0
    if in_env is None:
        m = re.search(r'\\begin\{(equation|align|eqnarray|gather|multline)\}', l)
        if m:
            in_env = m.group(1); body = l[m.end():]; rowtxt = body
            cur_rows = []
            if re.search(r'\\end\{' + in_env + r'\}', body):
                # single-line env
                txt = body.split('\\end{' + in_env + '}')[0]
                rows = re.split(r'\\\\', txt) if in_env != 'equation' else [txt]
                for r in rows:
                    if '\\nonumber' not in r and '\\notag' not in r: eq += 1
                in_env = None
            continue
    else:
        if re.search(r'\\end\{' + in_env + r'\}', l):
            rowtxt += '\n' + l.split('\\end{' + in_env + '}')[0]
            if in_env in ('equation', 'multline'):
                rows = [rowtxt]
            else:
                rows = re.split(r'\\\\', rowtxt)
            for r in rows:
                if r.strip() == '': continue
                if '\\nonumber' not in r and '\\notag' not in r: eq += 1
            if i >= min(targets, default=10**9) - 40:
                pass
            in_env = None
            label = re.findall(r'\\label\{([^}]*)\}', rowtxt)
            for t in list(targets):
                if t <= i and t >= i - rowtxt.count('\n') - 1:
                    tag = (chr(ord('A') + sec - 1) if app else str(sec))
                    print(f'line {t}: equation ({tag}.{eq}) [env ends at {i}] labels={label}')
                    targets.discard(t)
        else:
            rowtxt += '\n' + l
