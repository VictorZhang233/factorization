"""Assemble ../figset_D.tex from blocks/, then split it into split/<label>.tex
(one file per figure) and check every '%%% BEGIN <label>' / '%%% END <label>'
block: exactly one figure environment, one \\caption, exactly one fig: label
equal to the delimiter label, and every local style 'fd2 ...' used in a block
declared in that block.  Writes split/order.txt and a list of external
\\cref / \\cite targets (split/extern.txt) for the test document."""
import re, sys, os, glob
here = os.path.dirname(os.path.abspath(__file__))
blocks = sorted(glob.glob(os.path.join(here, 'blocks', '[0-9][0-9]_*.tex')))
out = os.path.join(here, '..', 'figset_D.tex')
with open(out, 'w', encoding='utf-8') as f:
    for i, b in enumerate(blocks):
        txt = open(b, encoding='utf-8').read().rstrip('\n') + '\n'
        if i: f.write('\n')
        f.write(txt)
src = open(out, encoding='utf-8').read().splitlines()
blk, cur, label = [], None, None
for ln, line in enumerate(src, 1):
    m = re.match(r'^%%% BEGIN (\S+)\s*$', line)
    if m:
        if cur is not None: sys.exit(f'line {ln}: BEGIN inside open block {label}')
        label, cur = m.group(1), []; continue
    m = re.match(r'^%%% END (\S+)\s*$', line)
    if m:
        if cur is None or m.group(1) != label: sys.exit(f'line {ln}: END {m.group(1)} does not match {label}')
        blk.append((label, cur)); cur = None; label = None; continue
    if cur is not None: cur.append(line)
    elif line.strip() and not line.startswith('%'):
        sys.exit(f'line {ln}: non-comment text outside any block: {line[:60]}')
if cur is not None: sys.exit(f'unterminated block {label}')
os.makedirs(os.path.join(here, 'split'), exist_ok=True)
order, bad, labels_all, cites_all = [], 0, set(), set()
for label, lines in blk:
    body = '\n'.join(lines)
    nb = body.count(r'\begin{figure}'); ne = body.count(r'\end{figure}')
    labs = re.findall(r'\\label\{([^}]*)\}', body)
    figlabs = [l for l in labs if l.startswith('fig:')]
    ncap = body.count(r'\caption{')
    used = set(re.findall(r'fd2 [a-z][a-z0-9 ]*?(?=[/,=\]\}\)])', body))
    declared = set(re.findall(r'(fd2 [a-z][a-z0-9 ]*?)/\.(?:style|pic|default|code)', body))
    undeclared = sorted(u for u in used if u.strip() not in {d.strip() for d in declared})
    refs = set()
    for grp in re.findall(r'\\[cC]ref\{([^}]*)\}', body):
        refs.update(x.strip() for x in grp.split(','))
    for grp in re.findall(r'\\ref\{([^}]*)\}', body):
        refs.update(x.strip() for x in grp.split(','))
    cites = set()
    for grp in re.findall(r'\\cite(?:\[[^\]]*\])?\{([^}]*)\}', body):
        cites.update(x.strip() for x in grp.split(','))
    labels_all |= refs; cites_all |= cites
    ok = (nb == 1 and ne == 1 and figlabs == [label] and ncap == 1 and not undeclared)
    bad += (not ok)
    print(f'{label:32s} fig={nb}/{ne} cap={ncap} labels={labs} '
          f'{"UNDECLARED: " + str(undeclared) if undeclared else ""} {"OK" if ok else "PROBLEM"}')
    fn = label.replace(':', '_') + '.tex'
    open(os.path.join(here, 'split', fn), 'w', encoding='utf-8').write(body + '\n')
    order.append(fn)
open(os.path.join(here, 'split', 'order.txt'), 'w').write('\n'.join(order) + '\n')
own = {l for l, _ in blk}
ext = sorted(l for l in labels_all if l not in own)
open(os.path.join(here, 'split', 'extern.txt'), 'w').write('\n'.join(ext) + '\n')
open(os.path.join(here, 'split', 'cites.txt'), 'w').write('\n'.join(sorted(cites_all)) + '\n')
print(len(blk), 'blocks;', bad, 'problems; external refs:', ', '.join(ext), '; cites:', ', '.join(sorted(cites_all)))
