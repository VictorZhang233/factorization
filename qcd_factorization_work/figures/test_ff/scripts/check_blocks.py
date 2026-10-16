r"""Check the %%% BEGIN/END delimiters of a figure-set file: every BEGIN has a matching END with the same label,
no nesting, exactly one \begin{figure}[htbp] ... \end{figure} and exactly one \label{<same label>} per block,
labels unique; every line outside the blocks is a comment or blank.

    python3 -I check_blocks.py figset_F.tex
"""
import sys, re

lines = open(sys.argv[1], encoding='utf-8').read().split('\n')
err, cur, body, seen = [], None, [], []
for i, l in enumerate(lines, 1):
    m = re.match(r'^%%% BEGIN (\S+)\s*$', l)
    n = re.match(r'^%%% END (\S+)\s*$', l)
    if m:
        if cur:
            err.append('line %d: BEGIN %s inside %s' % (i, m.group(1), cur))
        cur, body = m.group(1), []
        continue
    if n:
        if n.group(1) != cur:
            err.append('line %d: END %s does not match %s' % (i, n.group(1), cur))
        else:
            b = '\n'.join(body)
            if b.count('\\begin{figure}[htbp]') != 1 or b.count('\\end{figure}') != 1:
                err.append('%s: needs exactly one figure environment with [htbp]' % cur)
            labs = re.findall(r'\\label\{(fig:[^}]*)\}', b)
            if labs != [cur]:
                err.append('%s: figure labels %s' % (cur, labs))
            if cur in seen:
                err.append('%s: duplicate block' % cur)
            seen.append(cur)
        cur = None
        continue
    if cur:
        body.append(l)
    elif l.strip() and not l.lstrip().startswith('%'):
        err.append('line %d: text outside blocks: %s' % (i, l[:60]))
if cur:
    err.append('unterminated block %s' % cur)
print('blocks:', len(seen))
for e in err:
    print('ERROR', e)
sys.exit(1 if err else 0)
