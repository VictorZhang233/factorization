"""Split figures1.tex into one file per figure using the
'%%% BEGIN <label>' / '%%% END <label>' delimiters, check that the
delimiters are well formed and that each block holds exactly one figure
environment with exactly one \\label equal to the delimiter label.
Writes split/<label-with-colon-replaced>.tex and split/order.txt."""
import re, sys, os
here = os.path.dirname(os.path.abspath(__file__))
src = open(os.path.join(here, 'figures1.tex'), encoding='utf-8').read().splitlines()
blocks, cur, label = [], None, None
for ln, line in enumerate(src, 1):
    m = re.match(r'^%%% BEGIN (\S+)\s*$', line)
    if m:
        if cur is not None:
            sys.exit(f'line {ln}: BEGIN {m.group(1)} inside open block {label}')
        label, cur = m.group(1), []
        continue
    m = re.match(r'^%%% END (\S+)\s*$', line)
    if m:
        if cur is None or m.group(1) != label:
            sys.exit(f'line {ln}: END {m.group(1)} does not match open block {label}')
        blocks.append((label, cur)); cur = None; label = None
        continue
    if cur is not None:
        cur.append(line)
if cur is not None:
    sys.exit(f'unterminated block {label}')
os.makedirs(os.path.join(here, 'split'), exist_ok=True)
order = []
for label, lines in blocks:
    body = '\n'.join(lines)
    nb = body.count(r'\begin{figure}'); ne = body.count(r'\end{figure}')
    labs = re.findall(r'\\label\{([^}]*)\}', body)
    figlabs = [l for l in labs if l.startswith('fig:')]
    ok = (nb == 1 and ne == 1 and figlabs == [label])
    print(f'{label:28s} figure-envs={nb}/{ne} labels={labs} {"OK" if ok else "PROBLEM"}')
    fn = label.replace(':', '_') + '.tex'
    open(os.path.join(here, 'split', fn), 'w', encoding='utf-8').write(body + '\n')
    order.append(fn)
open(os.path.join(here, 'split', 'order.txt'), 'w').write('\n'.join(order) + '\n')
print(len(blocks), 'blocks')
