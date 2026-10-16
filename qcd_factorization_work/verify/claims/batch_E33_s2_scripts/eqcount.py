# Count displayed-equation numbers in a LaTeX source (equation, align, eqnarray, gather, multline;
# rows ended by \\ inside multi-row environments; \nonumber/\notag and starred forms skipped;
# split/aligned/subequations handled approximately).  Prints number, labels and a snippet.
# usage: python3 -I eqcount.py file.tex [pattern ...]   (only rows matching a pattern are printed if given)
import re, sys
src = open(sys.argv[1], encoding='utf-8', errors='replace').read()
pats = sys.argv[2:]
src = re.sub(r'(?<!\\)%.*', '', src)
body = src[src.find('\\begin{document}'):]
# appendix resets are not handled; report section headers so the reader can see where we are
tok = re.compile(r'\\begin\{(equation|align|eqnarray|gather|multline)(\*?)\}(.*?)\\end\{\1\2\}|\\(section|appendix)\b[^\n]*', re.S)
n = 0
for m in tok.finditer(body):
    if m.group(4):
        print('   ##', m.group(0)[:90]); continue
    env, star, inner = m.group(1), m.group(2), m.group(3)
    if star: continue
    if env in ('equation', 'multline'):
        if '\\nonumber' in inner or '\\notag' in inner: continue
        n += 1; rows = [inner]
        labs = re.findall(r'\\label\{([^}]*)\}', inner)
        txt = ' '.join(inner.split())
        if not pats or any(p in txt for p in pats) or any(p in ' '.join(labs) for p in pats):
            print(f"({n}) {labs} {txt[:150]}")
    else:
        # strip inner aligned/split blocks so their \\ do not count
        inner2 = re.sub(r'\\begin\{(aligned|split|array|cases|pmatrix|matrix|bmatrix)\}.*?\\end\{\1\}', ' BLOCK ', inner, flags=re.S)
        for r in re.split(r'\\\\', inner2):
            if not r.strip() or '\\nonumber' in r or '\\notag' in r: continue
            n += 1
            labs = re.findall(r'\\label\{([^}]*)\}', r)
            txt = ' '.join(r.split())
            if not pats or any(p in txt for p in pats) or any(p in ' '.join(labs) for p in pats):
                print(f"({n}) {labs} {txt[:150]}")
