"""Count numbered equations in a LaTeX file (equation, eqnarray, align) and
print the equation number of each \\label found inside them.
Usage: python3 -I eqcount.py file.tex [label ...]
Reads the file as data only."""
import re, sys
path = sys.argv[1]
want = set(sys.argv[2:])
txt = open(path, encoding='latin-1').read()
# strip comments (unescaped %)
lines = []
for ln in txt.split('\n'):
    out = []; i = 0
    while i < len(ln):
        if ln[i] == '\\' and i + 1 < len(ln):
            out.append(ln[i:i+2]); i += 2; continue
        if ln[i] == '%':
            break
        out.append(ln[i]); i += 1
    lines.append(''.join(out))
txt = '\n'.join(l for l in lines if not l.lstrip().startswith(('\\newcommand','\\def','\\renewcommand')))
# (macro-definition lines are dropped above so that \newcommand{\bea}{\begin{eqnarray}} is not counted)
# appendix equations are renumbered A1, A2, ... by revtex; numbers printed here are global counts
env_re = re.compile(r'\\begin\{(equation|eqnarray|align|eqnarray\*|equation\*|align\*)\}(.*?)\\end\{\1\}', re.S)
n = 0
results = {}
for m in env_re.finditer(txt):
    env, body = m.group(1), m.group(2)
    if env.endswith('*'):
        continue
    if env == 'equation':
        n += 1
        for lab in re.findall(r'\\label\{([^}]*)\}', body):
            results[lab] = n
        continue
    # split rows at \\ (not \\\\ inside?)
    rows = re.split(r'\\\\(?:\[[^\]]*\])?', body)
    for r in rows:
        if r.strip() == '':
            # an empty trailing row still gets a number in eqnarray if \\ at end; ignore empty
            continue
        if re.search(r'\\nonumber|\\nn\b|\\notag', r):
            # LaTeX steps the equation counter before the row is typeset, so a
            # label on an unnumbered eqnarray row refers to the next printed number
            for lab in re.findall(r'\\label\{([^}]*)\}', r):
                results[lab] = n + 1
            continue
        n += 1
        for lab in re.findall(r'\\label\{([^}]*)\}', r):
            results[lab] = n
for lab in (want or results):
    print(lab, results.get(lab))
print('total numbered equations:', n)
