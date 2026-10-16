"""Split ../figset_C.tex into one file per figure using the
'%%% BEGIN <label>' / '%%% END <label>' delimiters; check that the
delimiters are well formed, that each block holds exactly one figure
environment with exactly one fig: label equal to the delimiter label and one
caption, that the float specifier is [htbp], and that every fc style used in
a block is declared in it.  Writes split/<label with ':' -> '_'>.tex and
split/order.txt."""
import re, sys, os
here = os.path.dirname(os.path.abspath(__file__))
src = open(os.path.join(here, '..', 'figset_C.tex'), encoding='utf-8').read().splitlines()
blocks, cur, label = [], None, None
for ln, line in enumerate(src, 1):
    m = re.match(r'^%%% BEGIN (\S+)\s*$', line)
    if m:
        if cur is not None:
            sys.exit(f'line {ln}: BEGIN {m.group(1)} inside open block {label}')
        label, cur = m.group(1), [line]
        continue
    m = re.match(r'^%%% END (\S+)\s*$', line)
    if m:
        if cur is None or m.group(1) != label:
            sys.exit(f'line {ln}: END {m.group(1)} does not match open block {label}')
        cur.append(line)
        blocks.append((label, cur)); cur = None; label = None
        continue
    if cur is not None:
        cur.append(line)
    elif line.strip() and not line.startswith('%'):
        sys.exit(f'line {ln}: non-comment text outside any block: {line[:60]}')
if cur is not None:
    sys.exit(f'unterminated block {label}')
os.makedirs(os.path.join(here, 'split'), exist_ok=True)
order, bad = [], 0
for label, lines in blocks:
    body = '\n'.join(lines)
    nb = body.count(r'\begin{figure}[htbp]'); ne = body.count(r'\end{figure}')
    labs = re.findall(r'\\label\{([^}]*)\}', body)
    figlabs = [l for l in labs if l.startswith('fig:')]
    ncap = body.count(r'\caption{')
    used = set(re.findall(r'fc [a-zA-Z][a-zA-Z ]*?(?=[/,=\]\}])', body))
    declared = set(re.findall(r'(fc [a-zA-Z][a-zA-Z ]*?)/\.(?:style|pic|default)', body))
    undeclared = sorted(u for u in used if u.strip() not in {d.strip() for d in declared})
    ok = (nb == 1 and ne == 1 and figlabs == [label] and ncap == 1 and not undeclared)
    bad += (not ok)
    print(f'{label:28s} fig={nb}/{ne} cap={ncap} labels={labs} '
          f'{"undeclared fc styles: " + str(undeclared) if undeclared else ""} {"OK" if ok else "PROBLEM"}')
    fn = label.replace(':', '_') + '.tex'
    open(os.path.join(here, 'split', fn), 'w', encoding='utf-8').write(body + '\n')
    order.append(fn)
open(os.path.join(here, 'split', 'order.txt'), 'w').write('\n'.join(order) + '\n')
print(len(blocks), 'blocks;', bad, 'problems')
if bad:
    sys.exit(1)
