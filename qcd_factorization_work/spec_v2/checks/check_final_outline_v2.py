r"""Integrator's checker for spec_v2/FINAL_OUTLINE_v2.md (spec v2.2).  Python 3 standard library only.

    python3 -I check_final_outline_v2.py SPECDIR [OUTLINE.md]

SPECDIR must contain FINAL_OUTLINE_v2.md (or the file given), FIGURES_INDEX_v2.md, refs_merged_v2.bib, ASSUMPTIONS.md.
Checks (each prints OK or the findings; exit code 1 if any check of severity E fails):
 E1  statement entries parse; labels unique; type word = prefix
 E2  label key = owner key (exceptions: moved v1 `prelim` labels of Ch2, v1 `lattice` labels of Ch22)
 E3  every \uses target is a statement label, is defined, and is not a reserved [PENDING-VERIFY] slot
 E4  no forward dependency (chapter -> later chapter; same unit -> later entry; appendix -> later entry of the same appendix)
 E5  no dependency cycle (Tarjan SCC over all \uses edges)
 E6  grade propagation (WRITER_SPEC_v2 v2.2 Sec. 4.6) and qualifier compatibility; [V] never a premise of a positive claim
 E7  R_cond: premise sentence present; premises in \uses; assumptions and non-[R] premises of \uses in the premise sentence
 E8  every [A]/[P]/[C]/[V] statement (not asm) has a status paragraph; every [R] has a qualifier
 E9  assumptions: every asm entry is in the register table '### Assumptions' with the same tag, and is used by >= 1 statement
 E10 registry (Sec. 08) = entries: every entry registered under its unit with its tag; every registry statement row has an entry
 E11 required figures of FIGURES_INDEX_v2 Sec. 5 are registry rows of their owner; every fig label in the outline is known
 E12 citation-like tokens (`Key2011`, `Name:2019abc`) are keys of refs_merged_v2.bib
 E13 unit budgets present; total = 487
 E14 master-table rows (Sec. 09): label exists, tag equals the entry's tag
 W1  labels mentioned anywhere but not defined (wildcards, reserved slots and the retired labels of decisions D10, D11 excluded)
 W2  hidden forward dependencies: a chapter statement reaching, through appendix statements, a statement of a later chapter
     (allowed by WRITER_SPEC_v2 Sec. 4.5 item 5 only for the exceptions listed in FINAL_OUTLINE_v2 Sec. 0.5)
"""
import sys, os, re, collections

TYPEWORD = {'定义': 'def', '假设': 'asm', '定理': 'thm', '引理': 'lem', '命题': 'prop', '推论': 'cor', '猜想': 'conj', '注': 'rem', '例': 'ex'}
STMT = ('def', 'asm', 'thm', 'lem', 'prop', 'cor', 'conj', 'rem', 'ex')
UNITS = ['front'] + ['Ch%02d' % i for i in range(1, 26)] + ['App' + c for c in 'ABCDEFGHIJKLMNOPQ']
UIDX = {u: i for i, u in enumerate(UNITS)}
UNITKEY = {'front': 'front', 'Ch01': 'intro', 'Ch02': 'qcd', 'Ch03': 'prelim', 'Ch04': 'ir', 'Ch05': 'sudakov', 'Ch06': 'ee',
           'Ch07': 'dis', 'Ch08': 'pdf', 'Ch09': 'method', 'Ch10': 'disall', 'Ch11': 'coll', 'Ch12': 'dy', 'Ch13': 'thr',
           'Ch14': 'tmd', 'Ch15': 'scet', 'Ch16': 'jets', 'Ch17': 'smallx', 'Ch18': 'break', 'Ch19': 'excl', 'Ch20': 'heavy',
           'Ch21': 'power', 'Ch22': 'lamet', 'Ch23': 'yzliu', 'Ch24': 'front', 'Ch25': 'summary'}
for c in 'ABCDEFGHIJKLMNOPQ':
    UNITKEY['App' + c] = 'app' + c
MOVED_CH2 = {'def:prelim-qcd', 'def:prelim-feynman-rules', 'def:prelim-brst', 'lem:prelim-brst-nilpotent', 'thm:prelim-slavnov-taylor',
             'def:prelim-msbar', 'prop:prelim-beta', 'prop:prelim-rg', 'thm:prelim-composite-renorm'}
GLOBAL = {'asm:intro-wightman', 'asm:intro-composite', 'asm:intro-np-ope', 'asm:intro-af-coeff', 'asm:intro-growth', 'asm:intro-bridge'}
OPE = {'thm:dis-ope', 'prop:dis-ope-euclid', 'prop:dis-ope-gi', 'prop:dis-ope-forward'}
RANK = {'R': 4, 'A': 3, 'P': 2, 'C': 1, 'V': 0}
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
        s['n_uses'] = len(uu)
        s['uses_none'] = 'uses: none' in b
        pm = re.search(r'前提[：:]\s*(.*?)(?:。|$)', b, re.S)
        s['premise'] = list(dict.fromkeys(LAB.findall(pm.group(1)))) if pm else []
        s['status'] = ('地位与缺口' in b) or ('Status and gap' in b) or ('*Status' in b) or ('status and gap' in b.lower())
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

def main():
    sp = sys.argv[1]
    fn = sys.argv[2] if len(sys.argv) > 2 else os.path.join(sp, 'FINAL_OUTLINE_v2.md')
    text = open(fn, encoding='utf-8').read()
    ST = parse(text)
    res = collections.OrderedDict()
    def P(k, msg):
        res.setdefault(k, []).append(msg)
    for k in ['E1', 'E2', 'E3', 'E4', 'E5', 'E6', 'E7', 'E8', 'E9', 'E10', 'E11', 'E12', 'E13', 'E14', 'W1', 'W2']:
        res[k] = []
    by = collections.defaultdict(list)
    for s in ST:
        by[s['label']].append(s)
    D = {l: v[0] for l, v in by.items()}
    order = {s['label']: k for k, s in enumerate(ST)}
    for l, v in by.items():
        if len(v) > 1:
            P('E1', '%s defined %d times (lines %s)' % (l, len(v), ', '.join(str(x['line']) for x in v)))
    for s in ST:
        if TYPEWORD[s['type']] != s['pfx']:
            P('E1', '%s: type word %s vs prefix' % (s['label'], s['type']))
        key = s['label'].split(':')[1].split('-')[0]
        if key != UNITKEY[s['unit']] and not (s['unit'] == 'Ch02' and s['label'] in MOVED_CH2) and not (s['unit'] == 'Ch22' and key == 'lattice'):
            P('E2', '%s (unit %s, key %s)' % (s['label'], s['unit'], key))
    owner, rows, asmrow = registry(text)
    asmtag = {}
    for l, cells in asmrow.items():
        t = cells[1] if len(cells) > 1 else ''
        asmtag[l] = {'[A]': 'A', '[C]': 'C', '[P]': 'P'}.get(t.strip(), None)
    def tagof(l):
        s = D.get(l)
        if s is None:
            return None
        return asmtag.get(l, s['tag']) if s['pfx'] == 'asm' else s['tag']
    # E3/E4
    edges = collections.defaultdict(set)
    for s in ST:
        if s['reserved']:
            continue
        if s['pfx'] in ('def', 'asm', 'thm', 'lem', 'prop', 'cor', 'conj') and not s['uses'] and not s['uses_none']:
            P('E3', '%s: no \\uses and no "% uses: none"' % s['label'])
        if s['n_uses'] > 1:
            P('E3', '%s: %d \\uses lines' % (s['label'], s['n_uses']))
        for u in s['uses']:
            if u.split(':')[0] not in STMT:
                P('E3', '%s uses non-statement %s' % (s['label'], u)); continue
            if u not in D:
                P('E3', '%s uses undefined %s' % (s['label'], u)); continue
            if D[u]['reserved']:
                P('E3', '%s uses reserved slot %s' % (s['label'], u))
            edges[s['label']].add(u)
            su, tu = s['unit'], D[u]['unit']
            if su.startswith('App'):
                if tu == su and order[u] > order[s['label']]:
                    P('E4', '%s (%s) uses later %s' % (s['label'], su, u))
                continue
            if tu.startswith('App'):
                continue
            if UIDX[tu] > UIDX[su]:
                P('E4', '%s (%s) uses %s of later %s' % (s['label'], su, u, tu))
            elif tu == su and order[u] > order[s['label']]:
                P('E4', '%s (%s) uses later %s' % (s['label'], su, u))
    # E5 Tarjan
    sys.setrecursionlimit(100000)
    idx, low, onst, st, comps = {}, {}, set(), [], []
    counter = [0]
    def strong(v):
        idx[v] = low[v] = counter[0]; counter[0] += 1; st.append(v); onst.add(v)
        for w in edges.get(v, ()):
            if w not in idx:
                strong(w); low[v] = min(low[v], low[w])
            elif w in onst:
                low[v] = min(low[v], idx[w])
        if low[v] == idx[v]:
            comp = []
            while True:
                w = st.pop(); onst.discard(w); comp.append(w)
                if w == v:
                    break
            if len(comp) > 1 or v in edges.get(v, ()):
                comps.append(comp)
    for v in list(D):
        if v not in idx:
            strong(v)
    for c in comps:
        P('E5', 'cycle: ' + ' -> '.join(sorted(c)))
    # E6/E7 grade propagation
    memo = {}
    def content(l, stack=()):
        if l in memo:
            return memo[l]
        s = D.get(l)
        if s is None or l in stack:
            return 'R'
        if s['pfx'] == 'asm':
            g = 'R' if l in GLOBAL else (asmtag.get(l) or 'R')
        elif s['tag'] is None:
            g = 'R'
        elif s['tag'] == 'R' and s['qual'] == 'R_cond':
            g = 'R'
            for p in set(s['premise']) | set(s['uses']):
                if p in GLOBAL or p not in D:
                    continue
                if D[p]['pfx'] == 'asm':
                    pt = asmtag.get(p) or 'R'
                elif D[p]['tag'] == 'R' and D[p]['qual'] == 'R_OPE':
                    pt = 'A'
                else:
                    pt = content(p, stack + (l,))
                if pt != 'V' and RANK[pt] < RANK[g]:
                    g = pt
        elif s['tag'] == 'R' and s['qual'] == 'R_OPE':
            g = 'A'
        else:
            g = s['tag']
        memo[l] = g
        return g
    for s in ST:
        if s['reserved'] or s['tag'] is None or s['pfx'] == 'asm':
            continue
        t, q = s['tag'], s['qual']
        if t == 'R' and q is None:
            P('E8', '%s: [R] without qualifier' % s['label'])
        for u in s['uses']:
            if u not in D:
                continue
            us = D[u]
            if us['pfx'] == 'asm':
                if u in GLOBAL or t == 'V':
                    continue
                at = asmtag.get(u)
                if at is None:
                    continue
                if t == 'R' and q == 'R_cond':
                    if u not in s['premise']:
                        P('E7', '%s: asm %s in \\uses but not in the premise sentence' % (s['label'], u))
                    continue
                if RANK[t] > RANK[at]:
                    P('E6', '%s [%s] uses %s [%s]' % (s['label'], t + (',' + q if q else ''), u, at))
                continue
            ut, uq = us['tag'], us['qual']
            if ut is None:
                continue
            if ut == 'V':
                if t != 'V':
                    P('E6', '%s [%s] uses [V] %s' % (s['label'], t, u))
                continue
            if t == 'V':
                continue
            if t == 'R':
                if q == 'R_cond':
                    if ut != 'R' and u not in s['premise']:
                        P('E7', '%s: non-[R] %s [%s] not in the premise sentence' % (s['label'], u, ut))
                    if ut == 'R' and uq == 'R_OPE' and 'thm:dis-ope' not in s['premise']:
                        P('E7', '%s uses R_OPE %s without thm:dis-ope in the premise sentence' % (s['label'], u))
                    continue
                if q == 'R_OPE' and u in OPE:
                    continue
                if ut != 'R':
                    P('E6', '%s [R,%s] uses %s [%s]' % (s['label'], q, u, ut)); continue
                allowed = {'R_def': {'R_def'}, 'R_PT': {'R_def', 'R_PT'}, 'R_OPE': {'R_def', 'R_PT', 'R_OPE'}}.get(q, set())
                if uq == 'R_cond':
                    glob = all((p in GLOBAL) or (p in D and D[p]['tag'] == 'R') for p in D[u]['premise'])
                    if content(u) != 'R' or not glob:
                        P('E6', '%s [R,%s] uses R_cond %s (content %s, global-only %s)' % (s['label'], q, u, content(u), glob))
                    continue
                if uq not in allowed:
                    P('E6', '%s [R,%s] uses %s [R,%s]' % (s['label'], q, u, uq))
                continue
            if ut == 'R':
                c = content(u) if uq == 'R_cond' else ('A' if uq == 'R_OPE' else 'R')
                if RANK[t] > RANK[c]:
                    P('E6', '%s [%s] uses %s (content %s)' % (s['label'], t, u, c))
                continue
            if RANK[t] > RANK[ut]:
                P('E6', '%s [%s] uses %s [%s]' % (s['label'], t, u, ut))
    for s in ST:
        if s['tag'] == 'R' and s['qual'] == 'R_cond' and not s['reserved']:
            if not s['premise']:
                P('E7', '%s: R_cond without premise sentence' % s['label'])
            for p in s['premise']:
                if p not in s['uses']:
                    P('E7', '%s: premise %s not in \\uses' % (s['label'], p))
        if s['tag'] in ('A', 'P', 'C', 'V') and s['pfx'] != 'asm' and not s['reserved'] and not s['status']:
            P('E8', '%s [%s] without status paragraph (line %d)' % (s['label'], s['tag'], s['line']))
    # E9 assumptions
    asm_def = {l for l in D if l.startswith('asm:')}
    used = collections.Counter(u for s in ST for u in s['uses'])
    for l in sorted(asm_def):
        if l not in asmrow:
            P('E9', '%s not in the register table' % l)
        elif (asmtag.get(l) or None) != D[l]['tag']:
            P('E9', '%s: entry tag %s vs register %s' % (l, D[l]['tag'], asmtag.get(l)))
        if not used[l]:
            P('E9', '%s used by no statement' % l)
    for l in asmrow:
        if l not in asm_def:
            P('E9', 'register row %s has no entry' % l)
    # E10 registry
    for s in ST:
        if s['reserved']:
            if s['label'] in owner:
                P('E10', 'reserved slot %s registered' % s['label'])
            continue
        if owner.get(s['label']) != s['unit']:
            P('E10', '%s: entry in %s, registry %s' % (s['label'], s['unit'], owner.get(s['label'])))
    for u, l, cells in rows:
        if l.split(':')[0] in STMT and l not in D:
            P('E10', 'registry row %s (%s) has no entry' % (l, u))
        if l in D and D[l]['pfx'] != 'asm':
            t = cells[1] if len(cells) > 1 else ''
            m = re.search(r'\[(R, R_PT|R, R_def|R, R_OPE|R, R_cond|A|P|C|V)\]', t)
            rt = (('R', m.group(1)[3:]) if m.group(1).startswith('R, ') else (m.group(1), None)) if m else (None, None)
            et = (D[l]['tag'], D[l]['qual'] if D[l]['tag'] == 'R' else None)
            if rt != et and not (rt[0] is None and et[0] is None):
                P('E10', 'registry tag of %s: %s vs entry %s' % (l, t, et))
    # E11 figures
    fi = open(os.path.join(sp, 'FIGURES_INDEX_v2.md'), encoding='utf-8').read()
    s5 = fi[fi.index('## 5. Figures per unit'):]
    s5 = s5[:s5.index('## CHANGELOG')] if '## CHANGELOG' in s5 else s5
    req, opt = {}, {}
    for line in s5.split('\n'):
        m = re.match(r'^\|\s*(Ch\d+|App [A-Q](?:–[A-Q])?)\s*\|(.*)\|\s*(\d+)\s*\|\s*$', line)
        if not m:
            continue
        u = m.group(1)
        u = ('Ch%02d' % int(u[2:])) if u.startswith('Ch') else ('App' + u.split()[1][0] if '–' not in u else 'AppA-L')
        cells = [c.strip() for c in m.group(2).split('|')]
        for i, c in enumerate(cells):
            for name in re.findall(r'([a-zA-Z][a-zA-Z0-9\-]+)', re.sub(r'\(.*?\)', '', c)):
                (opt if i == len(cells) - 1 else req)['fig:' + name] = u
    regfig = {l: u for l, u in owner.items() if l.startswith('fig:')}
    for l, u in req.items():
        if u == 'AppA-L':
            continue
        if regfig.get(l) != u:
            P('E11', 'required %s (owner %s) registered under %s' % (l, u, regfig.get(l)))
    for l, u in regfig.items():
        if l not in req:
            P('E11', 'registry fig %s (%s) is not a required figure of FIGURES_INDEX_v2 Sec. 5' % (l, u))
    known_snippet = re.findall(r'`(fig:[A-Za-z0-9\-]+)`', fi)
    for l in sorted(set(re.findall(r'(?<![A-Za-z])fig:[A-Za-z0-9][A-Za-z0-9\-]*[A-Za-z0-9]', text))):
        if l not in req and l not in opt and l not in known_snippet:
            P('E11', 'fig label %s unknown to FIGURES_INDEX_v2' % l)
    # E12 citations
    bib = open(os.path.join(sp, 'refs_merged_v2.bib'), encoding='utf-8').read()
    keys = set(re.findall(r'@\w+\{([^,\s]+),', bib))
    for t in sorted(set(re.findall(r'`([A-Za-z][A-Za-z0-9:\-_\.\'+]*?)`', text))):
        if re.match(r'^(def|asm|thm|lem|prop|cor|conj|rem|ex|sec|tab|fig|ch|app|eq):', t) or re.search(r'\.(tex|md|py|bib|log|tsv)$', t):
            continue
        if (re.match(r'^[A-Za-z][A-Za-z\-\']*:?\d{4}[a-z]{0,4}$', t) or re.match(r'^[A-Za-z\-]+:\d{4}[A-Za-z]{2,4}$', t)) and t not in keys:
            P('E12', 'citation key not in bib: %s' % t)
    # E13 budgets
    bud = {}
    for m in re.finditer(r'^## (Front matter|Chapter (\d+)|Appendix ([A-Q]))[^\n]*\n+(.*?)$', text, re.M):
        u = 'front' if m.group(1).startswith('Front') else ('Ch%02d' % int(m.group(2)) if m.group(2) else 'App' + m.group(3))
        b = re.search(r'\*\*(\d+(?:\.\d+)?) pp\*\*', m.group(4)) or re.search(r'\((\d+) pp', m.group(0))
        if b:
            bud[u] = float(b.group(1))
    for u in UNITS:
        if u not in bud:
            P('E13', 'no budget for %s' % u)
    tot = sum(bud.values())
    if abs(tot - 487) > 0.01:
        P('E13', 'total budget %.1f != 487' % tot)
    # E14 master rows (Sec. 09)
    if '\n## 09 ' in text:
        sec9 = text[text.index('\n## 09 '):]
        nxt = re.search(r'\n## (1[0-9]|CHANGELOG)', sec9)
        sec9 = sec9[:nxt.start()] if nxt else sec9
        n = 0
        for line in sec9.split('\n'):
            m = re.match(r'^\| ([IVX]+\.\d+) \|', line)
            if not m:
                continue
            n += 1
            cells = [c.strip() for c in line.strip().strip('|').split('|')]
            labs = LAB.findall(cells[5]) if len(cells) > 5 else []
            if not labs:
                P('E14', '%s: no label' % m.group(1)); continue
            l = labs[0]
            if l not in D:
                P('E14', '%s: %s undefined' % (m.group(1), l)); continue
            mt = re.search(r'\[(R, R_PT|R, R_def|R, R_OPE|R, R_cond|A|P|C|V)\]', cells[3])
            rt = (('R', mt.group(1)[3:]) if mt.group(1).startswith('R, ') else (mt.group(1), None)) if mt else (None, None)
            et = (D[l]['tag'], D[l]['qual'] if D[l]['tag'] == 'R' else None)
            if rt != et:
                P('E14', '%s %s: row tag %s vs entry %s' % (m.group(1), l, cells[3], et))
        res.setdefault('info', []).append('master-table rows checked: %d' % n)
    else:
        P('E14', 'no Sec. 09 master-table rows')
    # W1
    RETIRED = {'lem:appO-past-unitarity', 'rem:prelim-bphz-brst'}
    for l in sorted(set(LAB.findall(text))):
        if l not in D and '-' in l.split(':')[1] and l not in RETIRED:
            P('W1', l)
    # W2 hidden forward dependencies through appendices
    for s in ST:
        if s['reserved'] or not s['unit'].startswith('Ch'):
            continue
        k = UIDX[s['unit']]
        seen, stack, hits = set(), [(u, (u,)) for u in s['uses']], []
        while stack:
            v, path = stack.pop()
            if v in seen or v not in D:
                continue
            seen.add(v)
            vu = D[v]['unit']
            if vu.startswith('Ch') and UIDX[vu] > k:
                hits.append((v, path)); continue
            for w in D[v]['uses']:
                stack.append((w, path + (w,)))
        for v, path in hits[:1]:
            P('W2', '%s (%s) -> %s (%s) via %s%s' % (s['label'], s['unit'], v, D[v]['unit'], ' > '.join(path[:-1]), ' (+%d more)' % (len(hits) - 1) if len(hits) > 1 else ''))
    # report
    fail = False
    tags = collections.Counter((s['tag'] or ('math' if s['qual'] == 'math' else '-')) + ((',' + s['qual']) if s['tag'] == 'R' else '')
                               for s in ST if not s['reserved'])
    print('FINAL_OUTLINE_v2 check: %d entries (%d reserved), %d units with entries, %d registry rows, %d register rows'
          % (len(ST), sum(s['reserved'] for s in ST), len({s['unit'] for s in ST}), len(rows), len(asmrow)))
    print('tags:', dict(sorted(tags.items())))
    for k, v in res.items():
        if k == 'info':
            for x in v:
                print('info:', x)
            continue
        print('%s: %s' % (k, 'OK' if not v else '%d finding(s)' % len(v)))
        for x in v[:200]:
            print('    ', x)
        if v and k.startswith('E'):
            fail = True
    sys.exit(1 if fail else 0)

if __name__ == '__main__':
    main()
