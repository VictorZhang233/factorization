r"""Extract statement data (label, type, tag, qualifier, unit, \uses, premises) from spec_v2/FINAL_OUTLINE_v2.md.

    python3 -I outline_data.py <FINAL_OUTLINE_v2.md> <out.json>

The parser is the one of spec_v2/checks/check_final_outline_v2.py (copied verbatim: parse(), registry(), norm_tag()),
so that the figure data agree with the integrator's checker.  Standard library only.
"""
import sys, re, json, collections

TYPEWORD = {'定义': 'def', '假设': 'asm', '定理': 'thm', '引理': 'lem', '命题': 'prop', '推论': 'cor', '猜想': 'conj', '注': 'rem', '例': 'ex'}
STMT = ('def', 'asm', 'thm', 'lem', 'prop', 'cor', 'conj', 'rem', 'ex')
UNITS = ['front'] + ['Ch%02d' % i for i in range(1, 26)] + ['App' + c for c in 'ABCDEFGHIJKLMNOPQ']
HDR = re.compile(r'^(?P<ind>\s*)(?:[*-]|\d+\.)\s+\*\*(?P<pv>\[PENDING-VERIFY[^\]]*\]\s*)?(?P<type>定义|假设|定理|引理|命题|推论|猜想|注|例)\s+'
                 r'`(?P<label>(?:def|asm|thm|lem|prop|cor|conj|rem|ex):[A-Za-z0-9\-]+)`\s*—\s*(?P<title>.+?)\*\*(?P<rest>.*)$')
TAGRE = re.compile(r'\[(R, R_PT|R, R_def|R, R_OPE|R, R_cond|A|P|C|V|\\tag[RAPCV])\]')
LAB = re.compile(r'(?<![A-Za-z])(?:def|asm|thm|lem|prop|cor|conj|rem|ex):[A-Za-z0-9][A-Za-z0-9\-]*[A-Za-z0-9]')


def unit_of_heading(line):
    m = re.match(r'^## (Front matter|Chapter (\d+)|Appendix ([A-Q]))\b', line)
    if not m:
        return None
    if m.group(1).startswith('Front'):
        return 'front'
    return 'Ch%02d' % int(m.group(2)) if m.group(2) else 'App' + m.group(3)


def norm_tag(rest):
    head = rest[:220]
    m = TAGRE.search(head)
    pn = [p for p in (head.find('(no tag'), head.find('(数学'), head.find('（数学')) if p >= 0]
    pn = min(pn) if pn else 10 ** 9
    if m and m.start() < pn:
        t = m.group(1)
        if t.startswith('\\tag'):
            return t[-1], None
        return ('R', t[3:]) if t.startswith('R, ') else (t, None)
    if pn < 10 ** 9:
        return None, ('math' if '数学' in head[pn:pn + 6] else None)
    return None, None


def parse(text):
    lines = text.split('\n')
    out, unit, stop, cur = [], None, False, None

    def close(i):
        nonlocal cur
        if cur is not None:
            cur['body'] = '\n'.join(lines[cur['line'] - 1:i])
            out.append(cur)
            cur = None
    for i, line in enumerate(lines):
        if re.match(r'^#{1,2} (0[89]|1[0-9])\b', line) or line.startswith('# Part VII annexes') or re.match(r'^## (F[1-6]|CHANGELOG)', line):
            close(i); stop = True; unit = None; continue
        u = unit_of_heading(line)
        if u:
            close(i); unit, stop = u, False; continue
        if line.startswith('# ') or line.startswith('## '):
            close(i)
            if line.startswith('# '):
                unit = None
            continue
        if line.startswith('#'):
            close(i); continue
        if stop or unit is None:
            continue
        m = HDR.match(line)
        if m:
            close(i)
            tag, qual = norm_tag(m.group('rest'))
            lab = m.group('label')
            cur = dict(label=lab, type=m.group('type'), pfx=lab.split(':')[0], title=m.group('title').strip(), tag=tag,
                       qual=qual, unit=unit, line=i + 1, indent=len(m.group('ind')), reserved=bool(m.group('pv')))
            continue
        if cur is not None and line.strip() and len(line) - len(line.lstrip()) <= cur['indent']:
            close(i)
    close(len(lines))
    for s in out:
        b = s['body']
        uu = re.findall(r'\\uses\{([^}]*)\}', b)
        s['uses'] = list(dict.fromkeys(x.strip() for x in uu[0].split(',') if x.strip())) if uu else []
        pm = re.search(r'前提[：:]\s*(.*?)(?:。|$)', b, re.S)
        s['premise'] = list(dict.fromkeys(LAB.findall(pm.group(1)))) if pm else []
        del s['body']
    return out


def registry(text):
    owner, rows, asm = {}, [], {}
    cur, in08 = None, False
    for line in text.split('\n'):
        if re.match(r'^#{1,2} ', line):
            in08 = bool(re.match(r'^#{1,2} 08\b', line)); cur = None; continue
        m = re.match(r'^###\s+(Ch\d\d|App[A-Q]|front|Assumptions)\b', line)
        if m:
            cur = m.group(1); continue
        if line.startswith('### '):
            cur = None; continue
        m = re.match(r'^\|\s*`((?:def|thm|lem|prop|cor|conj|rem|ex|asm|sec|fig|tab):[A-Za-z0-9\-]+)`\s*\|(.*)$', line)
        if m and cur and in08:
            cells = [c.strip() for c in m.group(2).split('|')]
            if cur == 'Assumptions':
                asm[m.group(1)] = cells
            else:
                owner[m.group(1)] = cur
                rows.append((cur, m.group(1), cells))
    return owner, rows, asm


def master_rows(text):
    """Rows of the master table (Sec. 09): (row id, label, tag cell, bottleneck cell)."""
    out, in09 = [], False
    for line in text.split('\n'):
        if re.match(r'^#{1,2} ', line):
            in09 = bool(re.match(r'^#{1,2} 09\b', line)); continue
        if not in09 or not line.startswith('|'):
            continue
        cells = [c.strip() for c in line.strip().strip('|').split('|')]
        if len(cells) < 8 or not re.match(r'^[IV]+\.\d+', cells[0]):
            continue
        m = re.search(r'`([a-z]+:[A-Za-z0-9\-]+)`', cells[5])
        if m:
            out.append(dict(row=cells[0], label=m.group(1), tag=cells[3], np=cells[4], bottleneck=cells[6], star=cells[-1]))
    return out


def main():
    text = open(sys.argv[1], encoding='utf-8').read()
    st = parse(text)
    owner, rows, asm = registry(text)
    regrows = [dict(unit=u, label=l, cells=c) for (u, l, c) in rows]
    data = dict(statements=st, registry=regrows, assumptions={k: v for k, v in asm.items()}, master=master_rows(text))
    json.dump(data, open(sys.argv[2], 'w', encoding='utf-8'), ensure_ascii=False, indent=1)
    cnt = collections.Counter(s['unit'] for s in st)
    print('statements:', len(st), ' registry rows:', len(regrows), ' assumptions:', len(asm), ' master rows:', len(data['master']))
    print(' '.join('%s:%d' % (u, cnt[u]) for u in UNITS if cnt[u]))


if __name__ == '__main__':
    main()
