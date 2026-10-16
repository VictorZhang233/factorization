#!/usr/bin/env python3
r"""blueprint_gen.py -- generator of the formal blueprint, Appendix P (FINAL_OUTLINE_v2 App P §P.2-§P.7).

    python3 -I blueprint_gen.py --root <book dir> --master master.tex [--aux master.aux]
            --outline spec_v2/FINAL_OUTLINE_v2.md --register spec_v2/ASSUMPTIONS.md --out build/appP
            [--level 0..3] [--final] [--stub] [--date YYYY-MM-DD]

Inputs: the \input order of the master driver (unit files of WRITER_SPEC_v2 §1.1; units that are not present are
skipped), the unit files, the .aux file (hyperref \newlabel form; printed numbers and pages), the label registry and
master-table rows of FINAL_OUTLINE_v2 (§08, §09; the master table is read from ch25_summary.tex when it is present),
and the assumption register (ASSUMPTIONS.md §1).

Outputs (all in --out): appP_register.tex, appP_status.tex, appP_uses.tex, appP_graph_a.tex ... appP_graph_h.tex,
appP_checks.tex, blueprint.json, appP_report.txt.  With --stub only placeholders that define the labels are written
(first LaTeX pass); blueprint.json and appP_report.txt are written in both modes.

Checks C-P1 ... C-P17 of §P.7 (plus C-P0: source parsing).  Exit code 0 if no finding of severity E, 1 otherwise;
--final turns C-P13 into an error.  Budget levels 0-3 (§P.7 "Budget control").  Deterministic output.
"""
import os, re, sys, json, math, argparse, itertools, collections, datetime
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import booklib as B

VERSION = '1.0'
TOOL = 'blueprint\\_gen.py'

CHECKS = collections.OrderedDict([
    ('C-P0', '源文件解析（环境、标题、标签）'),
    ('C-P1', '依赖、前提与非微扰地位中的标签均有定义；\\texttt{\\string\\uses} 的格式'),
    ('C-P2', '规范标签由登记的所属单元写出，且与登记表一致'),
    ('C-P3', '无前向依赖'),
    ('C-P4', '无依赖环'),
    ('C-P5', '等级传递：标签不高于前提的内容等级'),
    ('C-P6', '正面陈述不依赖 [V] 陈述'),
    ('C-P7', '[R] 的限定语逐字一致且彼此相容'),
    ('C-P8', '$R_{\\mathrm{cond}}$ 的前提句完整'),
    ('C-P9', '每条编号假设至少被使用一次'),
    ('C-P10', '「被使用于」与计算的直接使用者一致'),
    ('C-P11', '主表各行的标签存在且严格性标签一致'),
    ('C-P12', '无重复标签'),
    ('C-P13', '无待核实标记与已撤回的标签'),
    ('C-P14', '主表“瓶颈”列包含计算的瓶颈'),
    ('C-P15', '强子层面陈述的非微扰地位行'),
    ('C-P16', '「地位与缺口」段落存在并点名瓶颈'),
    ('C-P17', '具名缺口被点名'),
])
SEV_ORDER = {'E': 0, 'W': 1, 'I': 2}


# ============================================================================================== findings
class Findings(object):
    def __init__(self):
        self.items = []

    def add(self, check, sev, msg, zh=None, label=None, unit=None, file=None, line=None):
        self.items.append(dict(check=check, sev=sev, msg=msg, zh=zh or '', label=label, unit=unit, file=file, line=line))

    def of(self, check, sev=None):
        return [f for f in self.items if f['check'] == check and (sev is None or f['sev'] == sev)]

    def count(self, sev):
        return sum(1 for f in self.items if f['sev'] == sev)

    def sorted_items(self):
        def k(f):
            return (list(CHECKS).index(f['check']), SEV_ORDER[f['sev']], B.UNIT_INDEX.get(f['unit'], 99),
                    f['file'] or '', f['line'] or 0, f['label'] or '', f['msg'])
        return sorted(self.items, key=k)


def Lz(label):
    """Label typeset in tt with break points after ':' and '-' (for table cells and finding texts); a segment longer
    than 18 characters also gets a break point every 12 characters."""
    parts = []
    for p in re.findall(r'[^:\-]+[:\-]?|[:\-]', label):
        while len(p) > 18:
            parts.append(p[:12])
            p = p[12:]
        parts.append(p)
    return '\\bpLab{%s}' % '\\bpBrk '.join('\\detokenize{%s}' % p for p in parts if p)


# ============================================================================================== master table
def parse_master_tex(U):
    """Rows of tab:summary-master in ch25_summary.tex (several table floats; header row with 规范标签/瓶颈)."""
    s = U.text
    start, end = 0, len(s)
    secs = [(o, l, k, t, lab) for (o, l, k, t, lab) in U.sections if k.startswith('section')]
    for i, (o, l, k, t, lab) in enumerate(secs):
        if lab == 'sec:summary-master' or ('主表' in t and start == 0):
            start = o
            end = secs[i + 1][0] if i + 1 < len(secs) else len(s)
            break
    rows = []
    scope = s[start:end]
    for m in re.finditer(r'\\begin\s*\{(tabular\*?|tabularx|longtable|tabulary)\}', scope):
        name = m.group(1)
        j = m.end()
        nargs = 2 if name in ('tabular*', 'tabularx', 'tabulary') else 1
        while j < len(scope) and scope[j] in ' \n\t':
            j += 1
        if j < len(scope) and scope[j] == '[':
            j = scope.find(']', j) + 1
        for _ in range(nargs):
            while j < len(scope) and scope[j] in ' \n\t':
                j += 1
            if j < len(scope) and scope[j] == '{':
                j = B.match_brace(scope, j) + 1
        e = scope.find('\\end{%s}' % name, j)
        if e < 0:
            continue
        body = scope[j:e]
        header = None
        for raw in re.split(r'\\\\(?:\s*\[[^\]]*\])?', body):
            row = re.sub(r'\\(?:toprule|midrule|bottomrule|hline|endhead|endfirsthead|endfoot|endlastfoot|addlinespace)'
                         r'(?:\[[^\]]*\])?', ' ', raw)
            row = re.sub(r'\\cmidrule\s*(?:\([^)]*\))?\s*\{[^}]*\}', ' ', row)
            cells = [c.strip() for c in B.split_top(row, '&')]
            if len(cells) < 3:
                continue
            if any('规范标签' in c for c in cells):
                header = {}
                for i, c in enumerate(cells):
                    cc = re.sub(r'\\[A-Za-z]+\s*', '', c)
                    if '规范标签' in cc:
                        header['label'] = i
                    elif '瓶颈' in cc:
                        header['bottleneck'] = i
                    elif '非微扰' in cc:
                        header['np'] = i
                    elif cc.strip() in ('标签', '严格性', '等级', '严格性标签'):
                        header['tag'] = i
                continue
            if header and 'label' in header and header['label'] < len(cells):
                labs = B.LABEL_TOKEN.findall(cells[header['label']])
            else:
                labs = B.LABEL_TOKEN.findall(row)
            labs = [x for x in labs if not x.startswith('asm:')] or labs
            if not labs:
                continue
            lab = labs[0]
            tcell = cells[header['tag']] if header and 'tag' in header and header['tag'] < len(cells) else row
            tags = B.TAGMAC_RE.findall(tcell)
            tag = tags[0] if tags else None
            if tag is None:
                mt = re.search(r'\[\s*([RAPCV])\s*[,\]]', tcell)
                tag = mt.group(1) if mt else None
            qm = B.QUAL_DETECT.search(tcell) or re.search(r'R_(PT|def|OPE|cond)', tcell)
            qual = {'PT': 'R_PT', 'def': 'R_def', 'OPE': 'R_OPE', 'cond': 'R_cond'}[qm.group(1)] if (qm and tag == 'R') else None
            bcell = cells[header['bottleneck']] if header and 'bottleneck' in header and header['bottleneck'] < len(cells) else ''
            npcell = cells[header['np']] if header and 'np' in header and header['np'] < len(cells) else ''
            rid = re.match(r'^\s*([IVX]+\.\d+)', cells[0])
            rows.append(dict(row=rid.group(1) if rid else '', label=lab, tag=tag, qual=qual,
                             np=re.sub(r'\s+', ' ', npcell), bottleneck_labels=B.dedupe(B.LABEL_TOKEN.findall(bcell)),
                             bottleneck_text=re.sub(r'\s+', ' ', bcell), star=('★' in cells[-1] or '\\star' in cells[-1]),
                             source='ch25', line=U.line(start + m.start())))
    return rows


def master_rows(book):
    for U in book.units:
        if U.uid == 'Ch25':
            rows = parse_master_tex(U)
            if rows:
                return rows, 'ch25_summary.tex'
    return list(book.registry.master), 'FINAL_OUTLINE_v2 §09 (ch25_summary.tex %s)' % (
        'without a parsable tab:summary-master' if 'Ch25' in book.present else 'not present')


# ============================================================================================== checks
def run_checks(book, master, F, final=False):
    R = book.registry
    reg = book.register
    stmts = book.stmts
    present = set(book.present)
    withdrawn = set(R.withdrawn.values())
    canon = set(R.owner) | set(R.asm) | set(reg)

    def undefined_kind(p):
        """'withdrawn' | 'absent' (canonical, owner unit not present) | 'missing' (canonical, owner present) |
        'unknown'"""
        if p in withdrawn:
            return 'withdrawn'
        if p in canon:
            u = book.unit_of(p)
            return 'missing' if u in present else 'absent'
        return 'unknown'

    # ---------------------------------------------------------------- C-P0 parsing
    for U in book.units:
        for (env, ln) in U.unlabelled:
            F.add('C-P0', 'W', 'unlabelled %s environment (not in the dependency graph)' % env,
                  zh='%s 第 %d 行：无标签的 %s 环境' % (B.tex_escape(U.file), ln, env), unit=U.uid, file=U.file, line=ln)
    for l, st in stmts.items():
        if len(st.tags) > 1:
            F.add('C-P0', 'E', 'more than one tag macro in the title (%s)' % ', '.join(st.tags),
                  zh='%s：标题中有多个标签' % Lz(l), label=l, unit=st.unit, file=st.file, line=st.line)
        if st.title_warn:
            F.add('C-P0', 'W', st.title_warn, zh='%s：可选标题的方括号' % Lz(l), label=l, unit=st.unit, file=st.file, line=st.line)
        if st.label_line_delta is not None and st.label_line_delta > 2:
            F.add('C-P0', 'W', '\\label is not within the first three lines of the environment',
                  zh='%s：\\texttt{\\string\\label} 不在环境的前三行' % Lz(l), label=l, unit=st.unit, file=st.file, line=st.line)
        if B.label_prefix(l) != st.type and B.label_prefix(l) in B.STMT_PFX:
            F.add('C-P0', 'W', 'label prefix %s does not match the environment %s' % (B.label_prefix(l), st.env),
                  zh='%s：标签前缀与环境 %s 不符' % (Lz(l), st.env), label=l, unit=st.unit, file=st.file, line=st.line)

    # ---------------------------------------------------------------- C-P1 labels used are defined; \uses format
    for l, st in stmts.items():
        for field, lst in (('\\uses', st.uses), ('premise sentence', st.premises), ('非微扰地位 line', st.np_labels)):
            for p in lst:
                if field == '\\uses' and not B.is_stmt_label(p):
                    F.add('C-P1', 'E', '\\uses contains the non-statement label %s' % p,
                          zh='%s：\\texttt{\\string\\uses} 含非陈述标签 %s' % (Lz(l), Lz(p)), label=l, unit=st.unit,
                          file=st.file, line=st.line)
                    continue
                if p in stmts:
                    continue
                k = undefined_kind(p)
                if k == 'withdrawn':
                    continue      # C-P13
                if k == 'absent':
                    F.add('C-P1', 'I', '%s names %s of a unit not yet present (%s)' % (field, p, book.unit_of(p)),
                          zh='%s：%s 所在单元尚未写入' % (Lz(l), Lz(p)), label=l, unit=st.unit, file=st.file, line=st.line)
                elif k == 'missing':
                    F.add('C-P1', 'E', '%s names %s, canonical but not defined by its owner %s' % (field, p, book.unit_of(p)),
                          zh='%s：%s 未在所属单元中定义' % (Lz(l), Lz(p)), label=l, unit=st.unit, file=st.file, line=st.line)
                else:
                    F.add('C-P1', 'E', '%s names the unknown label %s (not in the registry)' % (field, p),
                          zh='%s：未知标签 %s' % (Lz(l), Lz(p)), label=l, unit=st.unit, file=st.file, line=st.line)
        if st.type in B.NEEDS_USES and st.uses_count == 0 and not st.uses_none:
            F.add('C-P1', 'E', 'no \\uses line and no "% uses: none"',
                  zh='%s：缺少 \\texttt{\\string\\uses}' % Lz(l), label=l, unit=st.unit, file=st.file, line=st.line)
        if st.uses_count > 1:
            F.add('C-P1', 'E', '%d \\uses lines (exactly one is allowed)' % st.uses_count,
                  zh='%s：多于一个 \\texttt{\\string\\uses}' % Lz(l), label=l, unit=st.unit, file=st.file, line=st.line)
        if st.type in ('rem', 'ex') and st.tag and st.uses_count == 0 and not st.uses_none:
            F.add('C-P1', 'W', 'tagged %s without \\uses' % st.env, zh='%s：带标签的%s缺少 \\texttt{\\string\\uses}'
                  % (Lz(l), B.TYPE_ZH[st.type]), label=l, unit=st.unit, file=st.file, line=st.line)
        if st.uses_none and st.uses_count:
            F.add('C-P1', 'W', 'both \\uses and "% uses: none"', zh='%s：同时有 \\texttt{\\string\\uses} 与 uses: none' % Lz(l),
                  label=l, unit=st.unit, file=st.file, line=st.line)

    # ---------------------------------------------------------------- C-P2 ownership / registry
    absent_count = collections.Counter()
    for lab, defs in sorted(book.dups.items()):
        own = R.owner.get(lab)
        if lab in B.GENERATED_LABELS:
            continue
        for (u, f, ln) in defs:
            if own and u != own:
                F.add('C-P2', 'E', '%s defined in %s, registry owner %s' % (lab, u, own),
                      zh='%s 由 %s 定义，登记的所属单元为 %s' % (Lz(lab), B.unit_short(u), B.unit_short(own)), label=lab,
                      unit=u, file=f, line=ln)
    for (u, lab, typ, tag, q, math_, title) in R.rows:
        if lab in B.GENERATED_LABELS:
            continue
        if lab in book.dups:
            continue
        if u in present:
            F.add('C-P2', 'E', 'canonical label %s of %s is not defined' % (lab, u),
                  zh='规范标签 %s（%s）缺失' % (Lz(lab), B.unit_short(u)), label=lab, unit=u, file=B.UNIT_FILE.get(u))
        else:
            absent_count[u] += 1
    for lab, a in list(reg.items()) + [(k, v) for k, v in R.asm.items() if k not in reg]:
        if lab in stmts:
            continue
        u = a.get('owner')
        if u in present:
            F.add('C-P2', 'E', 'registered assumption %s is not defined by its owner %s' % (lab, u),
                  zh='登记的假设 %s 未写出' % Lz(lab), label=lab, unit=u)
        else:
            absent_count[u] += 1
    if absent_count:
        F.add('C-P2', 'I', '%d canonical labels belong to %d units that are not present yet (%s)' % (
            sum(absent_count.values()), len(absent_count), ', '.join(sorted(absent_count, key=lambda x: B.UNIT_INDEX.get(x, 99)))),
            zh='%d 个规范标签属于尚未写入的 %d 个单元' % (sum(absent_count.values()), len(absent_count)))
    for l, st in stmts.items():
        if st.type == 'asm':
            rt = (reg.get(l) or R.asm.get(l) or {}).get('tag', 'n/a')
            if rt != 'n/a' and rt != st.tag:
                sev = 'E' if (st.tag and (rt is None or B.RANK[st.tag] > B.RANK[rt])) else 'W'
                F.add('C-P2', sev, 'assumption tag [%s] differs from the register [%s]' % (st.tag or '-', rt or '-'),
                      zh='%s：假设标签 [%s] 与登记表 [%s] 不同' % (Lz(l), st.tag or '无', rt or '无'), label=l, unit=st.unit,
                      file=st.file, line=st.line)
            continue
        if l not in R.info:
            continue
        rt, rq, rm = R.tag_of(l)
        if (st.tag, st.qualifier if st.tag == 'R' else None) == (rt, rq):
            continue
        if st.tag == 'R' and st.qualifier is None and rt == 'R':
            continue      # missing qualifier: C-P7
        if rt is None and st.tag is not None:
            sev, what = 'E', 'tag added'
        elif st.tag is None and rt is not None:
            sev, what = 'E', 'tag missing'
        else:
            r1 = B.RANK.get(st.tag, 0) + (0.5 if st.qualifier in ('R_PT', 'R_def') else (0.3 if st.qualifier == 'R_OPE' else 0))
            r0 = B.RANK.get(rt, 0) + (0.5 if rq in ('R_PT', 'R_def') else (0.3 if rq == 'R_OPE' else 0))
            if st.tag == 'V' or rt == 'V':
                sev, what = 'E', 'tag changed'
            elif r1 > r0:
                sev, what = 'E', 'strengthened'
            elif r1 < r0:
                sev, what = 'W', 'weakened (justify in the report)'
            else:
                sev, what = 'W', 'qualifier changed'
        fmt = lambda t, q: (t or '-') + ((', ' + q) if q else '')
        F.add('C-P2', sev, 'tag [%s] vs registry [%s]: %s' % (fmt(st.tag, st.qualifier if st.tag == 'R' else None), fmt(rt, rq), what),
              zh='%s：[%s] 与登记表 [%s] 不同' % (Lz(l), B.tex_escape(fmt(st.tag, st.qualifier if st.tag == 'R' else None)),
                                             B.tex_escape(fmt(rt, rq))), label=l, unit=st.unit, file=st.file, line=st.line)

    # ---------------------------------------------------------------- C-P3 forward dependencies
    to_app = 0
    for l, st in stmts.items():
        su = st.unit
        for p in st.uses:
            if not B.is_stmt_label(p):
                continue
            pu = book.unit_of(p)
            if pu is None:
                continue
            if pu == su:
                if p in stmts and book.order[p] > book.order[l]:
                    F.add('C-P3', 'E', 'uses %s, defined later in the same unit' % p,
                          zh='%s 使用同一单元中后出现的 %s' % (Lz(l), Lz(p)), label=l, unit=su, file=st.file, line=st.line)
                continue
            if B.is_appendix(su):
                continue
            if B.is_appendix(pu):
                to_app += 1
                continue
            if B.UNIT_INDEX[pu] > B.UNIT_INDEX[su]:
                F.add('C-P3', 'E', 'forward dependency: uses %s of the later unit %s' % (p, pu),
                      zh='%s 使用后面%s的 %s' % (Lz(l), B.unit_name(pu), Lz(p)), label=l, unit=su, file=st.file, line=st.line)
    if to_app:
        F.add('C-P3', 'I', '%d chapter -> appendix edges (allowed)' % to_app, zh='章到附录的依赖 %d 条（允许）' % to_app)
    # hidden forward dependencies through appendix statements (WRITER_SPEC_v2 §4.5 item 5)
    for l, st in stmts.items():
        if not B.is_chapter(st.unit):
            continue
        k = B.UNIT_INDEX[st.unit]
        seen, stack, hits = set(), [p for p in st.uses if p in stmts and B.is_appendix(stmts[p].unit)], []
        while stack:
            a = stack.pop()
            if a in seen:
                continue
            seen.add(a)
            for q in stmts[a].uses:
                if q not in stmts:
                    continue
                qu = stmts[q].unit
                if B.is_appendix(qu):
                    stack.append(q)
                elif B.is_chapter(qu) and B.UNIT_INDEX[qu] > k:
                    hits.append((a, q))
        for (a, q) in sorted(set(hits)):
            F.add('C-P3', 'W', 'hidden forward dependency: through %s it reaches %s of the later unit %s' % (a, q, stmts[q].unit),
                  zh='%s 经 %s 间接依赖后面的 %s' % (Lz(l), Lz(a), Lz(q)), label=l, unit=st.unit, file=st.file, line=st.line)

    # ---------------------------------------------------------------- C-P4 cycles (Tarjan)
    sys.setrecursionlimit(max(10000, 4 * len(stmts) + 100))
    index, low, onst, stack, comps, cnt = {}, {}, set(), [], [], [0]

    def strong(v):
        index[v] = low[v] = cnt[0]
        cnt[0] += 1
        stack.append(v)
        onst.add(v)
        for w in stmts[v].uses:
            if w not in stmts:
                continue
            if w not in index:
                strong(w)
                low[v] = min(low[v], low[w])
            elif w in onst:
                low[v] = min(low[v], index[w])
        if low[v] == index[v]:
            comp = []
            while True:
                w = stack.pop()
                onst.discard(w)
                comp.append(w)
                if w == v:
                    break
            if len(comp) > 1 or v in stmts[v].uses:
                comps.append(sorted(comp, key=book.sort_key))
    for v in stmts:
        if v not in index:
            strong(v)
    for comp in sorted(comps, key=lambda c: book.sort_key(c[0])):
        st = stmts[comp[0]]
        F.add('C-P4', 'E', 'dependency cycle: ' + ' -> '.join(comp),
              zh='依赖环：' + '、'.join(Lz(x) for x in comp[:4]) + ('……' if len(comp) > 4 else ''), label=comp[0],
              unit=st.unit, file=st.file, line=st.line)

    # ---------------------------------------------------------------- C-P5 .. C-P8 grades and qualifiers
    allowed = {'R_def': ('R_def',), 'R_PT': ('R_def', 'R_PT'), 'R_OPE': ('R_def', 'R_PT', 'R_OPE')}
    conv_asm = set()
    for l, st in stmts.items():
        t, q = st.tag, st.qualifier
        if st.type == 'asm' or t is None:
            continue
        reg_note = lambda frm: '（按登记表）' if frm else ''
        if t == 'R' and st.qual_problem:
            F.add('C-P7', 'E', st.qual_problem, zh='%s：限定语句不合规定' % Lz(l), label=l, unit=st.unit, file=st.file, line=st.line)
        for p in st.uses:
            if not B.is_stmt_label(p):
                continue
            pt, pq, frm = book.tagq(p)
            if p not in stmts and not frm:
                continue
            if p not in stmts and p not in R.info and p not in reg and p not in R.asm:
                continue
            ptype = B.label_prefix(p)
            if ptype == 'asm':
                if p in B.GLOBAL_ASM or t == 'V':
                    continue
                if pt is None:
                    conv_asm.add(p)
                    continue
                if t == 'R' and q == 'R_cond':
                    continue
                if B.RANK[t] > B.RANK[pt]:
                    F.add('C-P5', 'E', '[%s] statement uses the assumption %s [%s]%s' % (t, p, pt, ' (registry)' if frm else ''),
                          zh='%s [%s] 使用假设 %s [%s]%s' % (Lz(l), t, Lz(p), pt, reg_note(frm)), label=l, unit=st.unit,
                          file=st.file, line=st.line)
                continue
            if pt is None:
                continue
            if pt == 'V':
                if t != 'V' and st.type not in ('rem', 'ex'):
                    F.add('C-P6', 'E', 'positive statement uses the [V] statement %s' % p,
                          zh='%s 使用 [V] 陈述 %s' % (Lz(l), Lz(p)), label=l, unit=st.unit, file=st.file, line=st.line)
                continue
            if t == 'V':
                continue
            if t == 'R':
                if q == 'R_cond':
                    continue          # C-P8
                if q == 'R_OPE' and p in B.OPE_PREMISES:
                    continue
                if pt != 'R':
                    F.add('C-P5', 'E', '[R, %s] uses %s [%s]%s' % (q, p, pt, ' (registry)' if frm else ''),
                          zh='%s [R] 使用 %s [%s]%s' % (Lz(l), Lz(p), pt, reg_note(frm)), label=l, unit=st.unit,
                          file=st.file, line=st.line)
                    continue
                if q is None:
                    continue          # reported above
                if pq == 'R_cond':
                    c = book.content(p)
                    pst = stmts.get(p)
                    glob = pst is not None and all((x in B.GLOBAL_ASM) or (x in stmts and stmts[x].tag == 'R')
                                                   for x in pst.premises)
                    if c != 'R' or not glob or q == 'R_def':
                        F.add('C-P7', 'E', '[R, %s] uses the R_cond statement %s (content %s, global-only premises %s)' % (
                            q, p, c, glob), zh='%s [R, %s] 使用 $R_{\\mathrm{cond}}$ 陈述 %s（内容等级 %s）' % (
                            Lz(l), B.QUAL_SHORT[q], Lz(p), c), label=l, unit=st.unit, file=st.file, line=st.line)
                    else:
                        need = [x for x in pst.premises if x in B.GLOBAL_ASM and x not in st.np_labels]
                        if need:
                            F.add('C-P15', 'E', 'uses the global-only R_cond %s; its 非微扰地位 line must name %s' % (
                                p, ', '.join(need)), zh='%s 的非微扰地位行须列出 %s' % (Lz(l), '、'.join(Lz(x) for x in need)),
                                label=l, unit=st.unit, file=st.file, line=st.line)
                    continue
                if pq is None and not frm and p in stmts:
                    continue          # premise without qualifier: reported at the premise
                if pq not in allowed.get(q, ()):
                    F.add('C-P7', 'E', '[R, %s] uses %s [R, %s]%s' % (q, p, pq, ' (registry)' if frm else ''),
                          zh='%s [R, %s] 使用 %s [R, %s]%s' % (Lz(l), B.QUAL_SHORT[q], Lz(p), B.QUAL_SHORT.get(pq, '?'),
                                                         reg_note(frm)), label=l, unit=st.unit, file=st.file, line=st.line)
                continue
            # t in A, P, C
            if pt == 'R':
                c = book.content(p) if pq == 'R_cond' else ('A' if pq == 'R_OPE' else 'R')
            else:
                c = pt
            if B.RANK[t] > B.RANK[c]:
                F.add('C-P5', 'E', '[%s] statement uses %s (content grade %s)%s' % (t, p, c, ' (registry)' if frm else ''),
                      zh='%s [%s] 使用 %s（内容等级 %s）%s' % (Lz(l), t, Lz(p), c, reg_note(frm)), label=l, unit=st.unit,
                      file=st.file, line=st.line)
    for p in sorted(conv_asm, key=book.sort_key):
        F.add('C-P7', 'I', 'convention assumption %s (no tag) is used; allowed everywhere' % p,
              zh='约定性假设 %s（无标签）被使用' % Lz(p), label=p)
    # C-P8
    for l, st in stmts.items():
        if not (st.tag == 'R' and st.qualifier == 'R_cond'):
            continue
        loc = dict(label=l, unit=st.unit, file=st.file, line=st.line)
        if st.premise_status == 'none':
            F.add('C-P8', 'E', 'R_cond without the premise sentence 「前提：…」', zh='%s：缺少前提句' % Lz(l), **loc)
            continue
        if st.premise_status == 'late':
            F.add('C-P8', 'E', 'the premise sentence is not among the first two sentences', zh='%s：前提句不在前两句' % Lz(l), **loc)
        prem = set(st.premises)
        for p in st.uses:
            if not B.is_stmt_label(p):
                continue
            if B.label_prefix(p) == 'asm':
                if p not in prem:
                    F.add('C-P8', 'E', 'assumption %s in \\uses but not in the premise sentence' % p,
                          zh='%s：假设 %s 不在前提句中' % (Lz(l), Lz(p)), **loc)
                continue
            pt, pq, frm = book.tagq(p)
            if pt is None:
                continue
            c = book.content(p) if pt == 'R' and pq == 'R_cond' else ('A' if (pt == 'R' and pq == 'R_OPE') else pt)
            if c is not None and c != 'R' and p not in prem:
                # WRITER_SPEC_v2 §4.3 rule 1 (rank 2) demands every non-[R] statement (E); App P C-P8 also every
                # premise with content grade below [R], which for an [R]-tagged R_cond/R_OPE premise is a warning
                sev = 'W' if pt == 'R' else 'E'
                F.add('C-P8', sev, 'premise %s (%s, content %s) in \\uses but not in the premise sentence' % (
                    p, pt + ((', ' + pq) if pq else ''), c), zh='%s：前提 %s（%s）不在前提句中' % (Lz(l), Lz(p), c), **loc)
            if pt == 'R' and pq == 'R_OPE' and 'thm:dis-ope' not in prem:
                F.add('C-P8', 'E', 'uses the R_OPE statement %s without thm:dis-ope in the premise sentence' % p,
                      zh='%s：使用 $R_{\\mathrm{OPE}}$ 陈述 %s，前提句须列出 \\bpLab{thm:dis-ope}' % (Lz(l), Lz(p)), **loc)
        for p in st.premises:
            if p not in st.uses:
                F.add('C-P8', 'E', 'premise %s is not in \\uses' % p, zh='%s：前提 %s 不在 \\texttt{\\string\\uses} 中' % (Lz(l), Lz(p)), **loc)

    # ---------------------------------------------------------------- C-P9 assumptions used
    for l, st in stmts.items():
        if st.type == 'asm' and not book.users.get(l):
            F.add('C-P9', 'E', 'assumption used by no statement', zh='假设 %s 未被任何陈述使用' % Lz(l), label=l, unit=st.unit,
                  file=st.file, line=st.line)

    # ---------------------------------------------------------------- C-P10 「被使用于」
    for l, st in stmts.items():
        if st.type != 'asm':
            continue
        comp = set(book.users.get(l, []))
        loc = dict(label=l, unit=st.unit, file=st.file, line=st.line)

        def judge(listed, what):
            listed = set(listed)
            miss = sorted(comp - listed, key=book.sort_key)
            extra = sorted([x for x in listed - comp if book.unit_of(x) in present], key=book.sort_key)
            if miss or extra:
                F.add('C-P10', 'W', '%s differs from the computed users: missing %s; extra %s' % (
                    what, ', '.join(miss) or '-', ', '.join(extra) or '-'),
                    zh='%s：%s缺 %d、多 %d' % (Lz(l), '正文' if what.startswith('tex') else '登记表', len(miss), len(extra)), **loc)
        if st.asm_used_by is None:
            F.add('C-P10', 'W', 'no 「被使用于：」 field', zh='%s：缺少「被使用于」' % Lz(l), **loc)
        else:
            judge(st.asm_used_by, 'tex field 「被使用于」')
        r = reg.get(l) or R.asm.get(l)
        if r is not None:
            judge(r['users'], 'ASSUMPTIONS.md "used by"')

    # ---------------------------------------------------------------- C-P11 master rows
    for r in master:
        lab = r['label']
        loc = dict(label=lab, unit='Ch25' if r.get('source') == 'ch25' else None,
                   file='ch25_summary.tex' if r.get('source') == 'ch25' else None, line=r.get('line'))
        if lab not in stmts:
            k = undefined_kind(lab)
            if k == 'absent':
                F.add('C-P11', 'I', 'master row %s: %s belongs to a unit not yet present' % (r['row'], lab),
                      zh='主表 %s：%s 所在单元尚未写入' % (r['row'], Lz(lab)), **loc)
            else:
                F.add('C-P11', 'E', 'master row %s names %s, which is not defined (%s)' % (r['row'], lab, k),
                      zh='主表 %s：%s 未定义' % (r['row'], Lz(lab)), **loc)
            continue
        st = stmts[lab]
        if r['tag'] is None:
            F.add('C-P11', 'E', 'master row %s prints no tag' % r['row'], zh='主表 %s：未印标签' % r['row'], **loc)
            continue
        if (r['tag'], r['qual'] if r['tag'] == 'R' else None) != (st.tag, st.qualifier if st.tag == 'R' else None):
            F.add('C-P11', 'E', 'master row %s prints [%s%s], the statement is [%s%s]' % (
                r['row'], r['tag'], (', ' + r['qual']) if r['qual'] else '', st.tag or '-',
                (', ' + st.qualifier) if (st.tag == 'R' and st.qualifier) else ''),
                zh='主表 %s：%s 的标签与正文不同' % (r['row'], Lz(lab)), **loc)

    # ---------------------------------------------------------------- C-P12 duplicates
    for lab, defs in sorted(book.dups.items()):
        if len(defs) > 1:
            u0, f0, l0 = defs[0]
            F.add('C-P12', 'E', 'label defined %d times: %s' % (len(defs), '; '.join('%s:%d' % (f, ln) for (u, f, ln) in defs)),
                  zh='%s 定义了 %d 次' % (Lz(lab), len(defs)), label=lab, unit=u0, file=f0, line=l0)
        if lab in B.GENERATED_LABELS:
            u0, f0, l0 = defs[0]
            F.add('C-P12', 'E', '%s is generated by blueprint_gen.py and must not be defined in a unit' % lab,
                  zh='%s 由生成程序定义，单元中不应再定义' % Lz(lab), label=lab, unit=u0, file=f0, line=l0)

    # ---------------------------------------------------------------- C-P13 pending markers, withdrawn labels
    sev13 = 'E' if final else 'W'
    for U in book.units:
        for (pos, ln, kind, val) in U.markers:
            if kind == 'pending':
                F.add('C-P13', sev13, 'pending-verification comment: %s' % val, zh='%s 第 %d 行：待核实注释' % (
                    B.tex_escape(U.file), ln), unit=U.uid, file=U.file, line=ln)
        for m in re.finditer(r'PENDING-VERIFY', U.text):
            ln = U.line(m.start())
            F.add('C-P13', sev13, 'printed pending-verification marker', zh='%s 第 %d 行：印出的待核实标记' % (
                B.tex_escape(U.file), ln), unit=U.uid, file=U.file, line=ln)
        for (lab, cmd, off, ln) in U.refs:
            if lab in withdrawn:
                F.add('C-P13', sev13, 'reference to the withdrawn slot label %s' % lab, zh='%s 第 %d 行：引用已撤回的标签 %s' % (
                    B.tex_escape(U.file), ln, Lz(lab)), label=lab, unit=U.uid, file=U.file, line=ln)
        for (lab, off, ln) in U.labels:
            if lab in withdrawn:
                F.add('C-P13', sev13, 'definition of the withdrawn slot label %s' % lab, zh='定义了已撤回的标签 %s' % Lz(lab),
                      label=lab, unit=U.uid, file=U.file, line=ln)

    # ---------------------------------------------------------------- C-P14 bottleneck column
    for r in master:
        lab = r['label']
        if lab not in stmts:
            continue
        b = set(book.bottleneck(lab))
        ml = set(x for x in r['bottleneck_labels'] if B.is_stmt_label(x))
        miss = sorted(b - ml, key=book.sort_key)
        extra = sorted(ml - b, key=book.sort_key)
        if miss or extra:
            F.add('C-P14', 'W', 'master row %s: bottleneck column misses %s; lists in addition %s' % (
                r['row'], ', '.join(miss) or '-', ', '.join(extra) or '-'),
                zh='主表 %s（%s）：缺 %d、多 %d' % (r['row'], Lz(lab), len(miss), len(extra)), label=lab,
                unit='Ch25' if r.get('source') == 'ch25' else None)

    # ---------------------------------------------------------------- C-P15 non-perturbative lines
    mrow = {r['label']: r for r in master}
    for l, st in stmts.items():
        if st.type in ('def', 'asm', 'ex') or (st.tag is None and st.type != 'rem'):
            continue
        if st.type == 'rem' and st.tag is None:
            continue
        loc = dict(label=l, unit=st.unit, file=st.file, line=st.line)
        G = book.closure(l)[1]
        if st.np_line:
            bad = [x for x in st.np_labels if x not in B.GLOBAL_ASM]
            if bad:
                F.add('C-P15', 'E', '非微扰地位 line names non-global labels: %s' % ', '.join(bad),
                      zh='%s：非微扰地位行含非全局标签 %s' % (Lz(l), '、'.join(Lz(x) for x in bad)), **loc)
            missing = sorted(set(G) - set(st.np_labels), key=book.sort_key)
            if missing:
                F.add('C-P15', 'E', '非微扰地位 line misses global assumptions of the closure: %s' % ', '.join(missing),
                      zh='%s：非微扰地位行缺 %s' % (Lz(l), '、'.join(Lz(x) for x in missing)), **loc)
            continue
        r = mrow.get(l)
        npc = (r or {}).get('np', '') or ''
        hadron_master = bool(r) and npc.strip() not in ('', '—', '-', '–') and '部分子' not in npc
        if hadron_master:
            F.add('C-P15', 'E', 'hadron-level statement (master table: %s) without 非微扰地位 line' % npc,
                  zh='%s：强子层面陈述缺非微扰地位行' % Lz(l), **loc)
        elif G and not st.partonic:
            F.add('C-P15', 'W', 'the closure contains global assumptions (%s) but there is no 非微扰地位 line' % ', '.join(
                sorted(G, key=book.sort_key)), zh='%s：闭包含全局假设而无非微扰地位行' % Lz(l), **loc)
        elif not st.partonic and st.type in ('thm', 'prop', 'lem', 'cor', 'conj'):
            F.add('C-P15', 'W', 'neither a 非微扰地位 line nor the partonic remark (classification heuristic)',
                  zh='%s：既无非微扰地位行也无“只涉及部分子态”说明' % Lz(l), **loc)
    for l, st in stmts.items():
        if st.qualifier == 'R_cond' and st.tag == 'R':
            g_uses = [p for p in st.uses if p in B.GLOBAL_ASM and p not in st.premises]
            if g_uses and st.premise_status != 'none':
                pass   # reported by C-P8 (every assumption in \uses must be in the premise sentence)

    # ---------------------------------------------------------------- C-P16 status paragraphs
    for l, st in stmts.items():
        if st.type == 'asm' or st.tag not in ('A', 'P', 'C', 'V'):
            continue
        loc = dict(label=l, unit=st.unit, file=st.file, line=st.line)
        if not st.status_paragraph:
            F.add('C-P16', 'E', '[%s] statement without 「地位与缺口」 paragraph' % st.tag,
                  zh='%s [%s]：缺「地位与缺口」' % (Lz(l), st.tag), **loc)
            continue
        if st.status_where == 'late':
            F.add('C-P16', 'W', '「地位与缺口」 does not follow the environment (and its proof) immediately',
                  zh='%s：「地位与缺口」未紧随环境' % Lz(l), **loc)
        elif st.status_where == 'inside':
            F.add('C-P16', 'I', '「地位与缺口」 is inside the environment', zh='%s：「地位与缺口」在环境内部' % Lz(l), **loc)
        b = book.bottleneck(l)
        if b and not (set(b) & set(st.status_labels)):
            F.add('C-P16', 'W', '「地位与缺口」 names none of the bottleneck labels %s' % ', '.join(b),
                  zh='%s：「地位与缺口」未点名瓶颈（%s 等）' % (Lz(l), Lz(b[0])), **loc)

    # ---------------------------------------------------------------- C-P17 named gaps
    for gap, trig in B.NAMED_GAPS.items():
        for l, st in stmts.items():
            if st.tag not in ('A', 'P', 'C', 'V') or st.type == 'asm':
                continue
            S = book.closure(l)[2]
            if not (trig in S or l == trig):
                continue
            named = gap in st.status_labels or any(gap in stmts[p].status_labels for p in st.uses if p in stmts)
            if not named:
                F.add('C-P17', 'W', 'closure contains %s; 「地位与缺口」 does not name the named gap %s' % (trig, gap),
                      zh='%s：未点名具名缺口 %s' % (Lz(l), Lz(gap)), label=l, unit=st.unit, file=st.file, line=st.line)


def named_gap_state(book, l):
    """For tab:appP-uses: [(gap, named?)] for the named gaps that apply to l."""
    out = []
    st = book.stmts.get(l)
    if st is None:
        return out
    for gap, trig in B.NAMED_GAPS.items():
        S = book.closure(l)[2]
        if trig in S or l == trig or gap in book.closure(l)[0]:
            if st.tag == 'R' and st.qualifier == 'R_cond':
                out.append((gap, 'premise' if gap in st.premises else False))
            else:
                named = gap in (st.status_labels or []) or any(gap in (book.stmts[p].status_labels or [])
                                                              for p in st.uses if p in book.stmts)
                out.append((gap, named))
    return out


# ============================================================================================== LaTeX helpers
HEADER_MACROS = r'''\providecommand{\bpNum}[1]{\hyperref[#1]{\ref*{#1}}}%
\providecommand{\bpNumA}[1]{\hyperref[#1]{\textcolor{orange!65!black}{\ref*{#1}}}}%
\providecommand{\bpPage}[1]{\pageref*{#1}}%
\providecommand{\bpLab}[1]{{\ttfamily #1}}%
\providecommand{\bpBrk}{\allowbreak}%
\providecommand{\bpT}[2]{\facttagbox[#1]{\scriptsize #2}}%
\providecommand{\bpU}[1]{{\color{gray!70!black}#1}}%
'''


def tex_header(meta, what):
    return ('%% %s -- generated by writing/tools/blueprint_gen.py %s (level %s) on %s from sources %s; do not edit\n'
            % (what, VERSION, meta['level'], meta['date'], meta['rev'])) + HEADER_MACROS


def num(book, l):
    if l in book.stmts:
        return ('\\bpNumA{%s}' if B.label_prefix(l) == 'asm' else '\\bpNum{%s}') % l
    return '\\bpU{%s}' % Lz(l)


AUXNUM = {}          # label -> printed number from the .aux (filled in main(); used by nums_compact)


def nums_compact(book, labels):
    """Chapter-grouped list of printed numbers, every number hyperlinked: '1.9--13；7.2, 19, 22；N.6'.
    Numbers come from the .aux; labels without a known number fall back to \\bpNum (resolved by LaTeX)."""
    labels = sorted(B.dedupe(labels), key=book.sort_key)
    if not labels:
        return '—'
    groups, other = [], []
    for l in labels:
        n = AUXNUM.get(l, '')
        m = re.match(r'^([A-Z]|\d+)\.(\d+)$', n)
        if l not in book.stmts or not m:
            other.append(num(book, l))
            continue
        pre, k = m.group(1), int(m.group(2))
        if groups and groups[-1][0] == pre:
            groups[-1][1].append((k, l))
        else:
            groups.append((pre, [(k, l)]))

    def link(l, txt):
        return ('\\hyperref[%s]{\\textcolor{orange!65!black}{%s}}' if B.label_prefix(l) == 'asm' else '\\hyperref[%s]{%s}') % (l, txt)
    out = []
    for pre, items in groups:
        items.sort()
        runs, cur = [], [items[0]]
        for it in items[1:]:
            if it[0] == cur[-1][0] + 1:
                cur.append(it)
            else:
                runs.append(cur)
                cur = [it]
        runs.append(cur)
        parts = []
        for j, r in enumerate(runs):
            first = ('%s.%d' % (pre, r[0][0])) if j == 0 else str(r[0][0])
            if len(r) >= 3:
                parts.append(link(r[0][1], first) + '--' + link(r[-1][1], str(r[-1][0])))
            else:
                parts.append(', \\bpBrk '.join([link(r[0][1], first)] + [link(x[1], str(x[0])) for x in r[1:]]))
        out.append(', \\bpBrk '.join(parts))
    return '；\\bpBrk '.join(out + other)


def nums_l(book, labels, level, limit=None):
    """Number list for table cells: compact chapter-grouped form at level >= 2, plain list otherwise."""
    if level >= 2 and AUXNUM:
        return nums_compact(book, labels)
    return nums(book, labels, limit=limit)


def nums(book, labels, sep='，', limit=None):
    """Printed numbers (hyperlinks) of labels in book order; with limit, at most that many followed by 「等共 k 条」."""
    labels = sorted(B.dedupe(labels), key=book.sort_key)
    if not labels:
        return '—'
    shown = labels if (limit is None or len(labels) <= limit) else labels[:limit]
    s = (sep + '\\bpBrk ').join(num(book, x) for x in shown)
    if len(shown) < len(labels):
        s += '等共 %d 条' % len(labels)
    return s


def tag_full(t, q):
    if t is None:
        return '—'
    s = '\\tag%s' % t
    if t == 'R' and q:
        s += '\\,{\\scriptsize %s}' % B.QUAL_TEX[q]
    return s


def tag_compact(t, q=None, content=None):
    """Compact tag box (the preamble's \\facttagbox with the tag colour): 'R PT', 'A', 'R cond:C' ..."""
    if t is None:
        return '—'
    txt = t + (('\\,' + B.QUAL_SHORT[q]) if (t == 'R' and q) else '')
    if content and content != t and t == 'R' and q == 'R_cond':
        txt += '\\,{:}\\,%s' % content
    return '\\bpT{%s}{%s}' % (B.TAG_COLOUR[t], txt)


def colspec(widths, sep_col=None):
    """longtable column specification: widths are fractions of (\\textwidth - 2(n-1)\\tabcolsep); a column whose
    width is None is an empty separator column."""
    n = len(widths)
    tot = sum(w for w in widths if w)
    cols = []
    for w in widths:
        if not w:
            cols.append('@{\\hspace{2.5mm}}c@{\\hspace{2.5mm}}')
            continue
        k = int(1000 * w / tot)          # floor: the columns never add up to more than the text width
        cols.append('>{\\raggedright\\arraybackslash}p{\\dimexpr(\\textwidth-%d\\tabcolsep-%s)*%d/1000\\relax}'
                    % (2 * (n - 1), '5mm' if None in widths else '0mm', k))
    return '@{}' + ''.join(cols) + '@{}'


def longtable(caption, label, header_cells, rows, widths, font, cont_caption=None, tabcolsep='2.5pt'):
    n = len(header_cells)
    hdr = ' & '.join(('\\textbf{%s}' % h) if h else '' for h in header_cells) + ' \\\\'
    out = ['\\begingroup%s\\setlength{\\tabcolsep}{%s}\\renewcommand{\\arraystretch}{1.06}' % (font, tabcolsep),
           '\\begin{longtable}{%s}' % colspec(widths),
           '\\caption{%s}\\label{%s}\\\\' % (caption, label),
           '\\toprule', hdr, '\\midrule', '\\endfirsthead',
           '\\caption[]{%s}\\\\' % (cont_caption or (caption + '（续）')),
           '\\toprule', hdr, '\\midrule', '\\endhead',
           '\\midrule', '\\multicolumn{%d}{r@{}}{\\footnotesize（续下页）}\\\\' % n, '\\endfoot',
           '\\bottomrule', '\\endlastfoot']
    out += rows
    out += ['\\end{longtable}', '\\endgroup']
    return '\n'.join(out)


def cref_or(book, label, text):
    """\\cref{label} if the label is defined in the sources, otherwise plain text (partial books)."""
    return ('\\cref{%s}' % label) if label in book.dups else text


def section_head(book, title, label, F):
    if label in book.dups:
        F.add('C-P12', 'W', 'section label %s is already defined in a unit file: generated heading omitted' % label,
              zh='%s 已由单元定义，生成的节标题省略' % Lz(label), label=label)
        return '%% heading omitted: %s is defined in a unit file\n' % label
    return '\\section{%s}\\label{%s}\n' % (title, label)


# ============================================================================================== register
def asm_rows_in_order(book):
    """Assumptions in book order of the owners; within an owner in source order (register order if absent)."""
    reg = book.register if book.register else book.registry.asm
    labs = list(dict.fromkeys([l for l, st in book.stmts.items() if st.type == 'asm'] + list(reg) + list(book.registry.asm)))
    regl = list(reg)

    def k(l):
        st = book.stmts.get(l)
        u = st.unit if st else (reg.get(l, {}) or book.registry.asm.get(l, {})).get('owner')
        return (B.UNIT_INDEX.get(u, 99), 0 if st else 1, book.order.get(l, 0), regl.index(l) if l in reg else 999, l)
    return sorted(labs, key=k)


INNER = re.compile(r'\(([A-Z][A-Za-z]{0,3}\d?[a-z]?\'?′?)\)')


def inner_items(content):
    """Inner item names of an assumption, compressed: (W1)--(W4)."""
    names = B.dedupe(INNER.findall(content or ''))
    names = [n for n in names if re.match(r'^[A-Z]{1,4}\d', n) or n in ('ADJ', 'REAL', 'LCE', 'SR', 'UL', 'MR')]
    if not names:
        return ''
    groups, cur = [], [names[0]]
    for a in names[1:]:
        pa = re.match(r'^([A-Z]+)(\d+)$', cur[-1])
        pb = re.match(r'^([A-Z]+)(\d+)$', a)
        if pa and pb and pa.group(1) == pb.group(1) and int(pb.group(2)) == int(pa.group(2)) + 1:
            cur.append(a)
        else:
            groups.append(cur)
            cur = [a]
    groups.append(cur)
    out = []
    for g in groups:
        out.append('(%s)' % g[0] if len(g) == 1 else ('(%s)(%s)' % (g[0], g[1]) if len(g) == 2 else '(%s)--(%s)' % (g[0], g[-1])))
    return ''.join(out)


def text_unicode_safe(t):
    """Greek letters etc. outside $...$ written in math mode (the Latin Modern text fonts lack them)."""
    segs = t.split('$')
    for i in range(0, len(segs), 2):
        segs[i] = ''.join(B.UNI_TEX.get(c, c) if c in B.UNI_TEX and c not in '–—' else c for c in segs[i])
    return '$'.join(segs)


STATUS_ZH = {'A': '文献有全阶论证，未作为精确陈述证明', 'P': '仅在特例、有限阶或模型中证明', 'C': '无全阶论证', None: '约定'}


def write_register(book, meta, F, level):
    reg = book.register if book.register else book.registry.asm
    rows = []
    for l in asm_rows_in_order(book):
        st = book.stmts.get(l)
        r = reg.get(l) or book.registry.asm.get(l) or {}
        u = st.unit if st else r.get('owner')
        tag = st.tag if st else r.get('tag')
        title = text_unicode_safe(st.title_text) if (st and st.title_text) else B.tex_escape(r.get('title', ''))
        if st and not B.tex_safe_fragment(title):
            title = B.tex_escape(r.get('title', ''))
        items = inner_items(r.get('content', ''))
        content = title + ((' ' + items) if items and items not in title else '')
        flags = []
        if l in B.GLOBAL_ASM:
            flags.append('全局非微扰假设')
        if l in B.NAMED_GAPS:
            flags.append('具名缺口')
        status = None
        if st and st.asm_status_text and len(st.asm_status_text) <= 60 and B.tex_safe_fragment(st.asm_status_text):
            status = st.asm_status_text
        if status is None:
            status = STATUS_ZH.get(tag, '')
        flags = [f for f in flags if f not in status]
        if flags:
            status = '；'.join(flags) + '。' + status
        upg = None
        if st and st.asm_upgrade_text and len(st.asm_upgrade_text) <= 60 and B.tex_safe_fragment(st.asm_upgrade_text):
            upg = st.asm_upgrade_text
        if upg is None:
            upg = '见该假设的「解除途径」' if st else '（单元尚未写入）'
        users = book.users.get(l, [])
        first = (num(book, l) + '\\newline ' + Lz(l)) if st else Lz(l)
        tagcell = (tag_full(tag, None) if level == 0 else tag_compact(tag)) if tag else '无'
        rows.append('%s & %s & %s & %s & %s & %s & %s \\\\' % (first, ('\\mbox{%s}' % B.unit_name(u)) if u else '—', content, tagcell, status,
                                                               nums_l(book, users, level), upg))
    font = '\\footnotesize' if level == 0 else '\\scriptsize'
    out = [tex_header(meta, 'appP_register.tex'),
           section_head(book, '假设登记表', 'sec:appP-register', F),
           '本表由各单元的 \\texttt{assumption} 环境与假设登记表自动生成，按所属单元的书序排列；“被使用于”一列由各陈述的 '
           '\\texttt{\\string\\uses} 数据计算（直接使用者的编号），与环境中「被使用于」字段的比较见检查 C-P10。',
           longtable('编号假设登记表（由 \\texttt{assumption} 环境生成）', 'tab:appP-register',
                     ['编号／标签', '单元', '内容', '标签', '地位', '被使用于', '解除途径'], rows,
                     [2.3, 1.3, 2.35, 1.95 if level == 0 else 0.75, 2.05, 3.6 if level == 0 else 4.55, 1.8], font)]
    return '\n'.join(out) + '\n'


# ============================================================================================== status table
def status_rows(book, level):
    return [l for l, st in book.stmts.items() if not (level >= 1 and st.type in ('def', 'rem', 'ex'))]


def write_status(book, meta, F, level):
    canon = set(book.registry.owner) | set(book.registry.asm) | set(book.register)
    labs = status_rows(book, level)

    def grade_cells(l):
        st = book.stmts[l]
        c = book.content(l)
        if st.type in ('def', 'rem', 'ex') and not st.tag:
            return '—', '—'
        if st.tag is None:
            return '数学', tag_compact(c)
        return tag_compact(st.tag, st.qualifier), tag_compact(c)

    def common(l):
        st = book.stmts[l]
        prem = [p for p in st.uses if B.label_prefix(p) != 'def']
        mark = '' if l in canon else '$^\\dagger$'
        err = B.ERRTYPE_TEX.get(st.errtype, st.errtype) if st.errtype else '—'
        return st, prem, mark, err
    intro = ('本表按书序列出%s陈述（$^\\dagger$ 为作者增加的非规范标签），给出标签与限定、按%s'
             '计算的内容等级 $c(S)$、直接前提（定义不列；假设以橙色编号列出）、最弱一步的误差类型（取自环境中的 '
             '\\texttt{\\%% errtype:} 注释）与页码。编号均为超链接。'
             % ('全部规范' if level == 0 else '除定义、注与例之外的全部规范',
                cref_or(book, 'def:appP-content-grade', '内容等级的定义'))) + (
                 '前提的编号按章合并：“7.2, 19--22”即 7.2、7.19 至 7.22。' if level >= 2 else '')
    if level <= 1:
        rows = []
        for l in labs:
            st, prem, mark, err = common(l)
            t, cg = grade_cells(l)
            rows.append(' & '.join([num(book, l) + mark, '{\\scriptsize %s}' % Lz(l), B.TYPE_ZH[st.type], t, cg,
                                    nums_l(book, prem, level), err, '\\bpPage{%s}' % l]) + ' \\\\')
        widths = [1.0, 3.95, 0.7, 1.55, 0.85, 4.65, 0.75, 0.6] if level == 0 else [0.95, 3.85, 0.65, 1.5, 0.8, 5.1, 0.7, 0.55]
        table = longtable('全部规范陈述的状态表', 'tab:appP-status',
                          ['编号', '标签', '类型', '标签与限定', '$c(S)$', '前提', '误差', '页'], rows, widths,
                          '\\footnotesize' if level == 0 else '\\scriptsize')
    else:
        half = []
        for l in labs:
            st, prem, mark, err = common(l)
            c = book.content(l)
            if st.tag is None:
                g = '数学' if st.type not in ('def', 'rem', 'ex') else '—'
            else:
                g = tag_compact(st.tag, st.qualifier, c)
            half.append([num(book, l) + mark, Lz(l.split(':', 1)[1]), g, nums_l(book, prem, level), err, '\\bpPage{%s}' % l])
        rows = []
        for i in range(0, len(half), 2):
            a = half[i]
            b = half[i + 1] if i + 1 < len(half) else [''] * 6
            rows.append(' & '.join(a) + ' & & ' + ' & '.join(b) + ' \\\\')
        w = [0.75, 2.75, 1.55, 1.5, 0.6, 0.45]
        hdrh = ['编号', '标签（无前缀）', '等级', '前提', '误差', '页']
        table = longtable('全部规范陈述的状态表（两栏排列）', 'tab:appP-status', hdrh + [''] + hdrh, rows,
                          w + [None] + w, '\\scriptsize', tabcolsep='1.5pt')
    out = [tex_header(meta, 'appP_status.tex'), section_head(book, '全部陈述的状态表', 'sec:appP-status', F), intro, table]
    return '\n'.join(out) + '\n'


# ============================================================================================== uses table
def uses_rows(book, master, level):
    rows = []
    seen = set()
    for r in master:
        if r['label'] in book.stmts and r['label'] not in seen:
            rows.append((r['row'], r['label'], r))
            seen.add(r['label'])
    if level <= 2:
        for l, st in book.stmts.items():
            if st.unit in ('AppM', 'AppN', 'AppO') and st.type == 'thm' and st.tag == 'R' and st.qualifier == 'R_cond' and l not in seen:
                rows.append(('', l, None))
                seen.add(l)
    return rows


def write_uses(book, master, meta, F, level):
    font = '\\footnotesize' if level == 0 else '\\scriptsize'
    lim = None
    body, trivial = [], []
    for rid, l, r in uses_rows(book, master, level):
        st = book.stmts[l]
        A, G, S, O = book.closure(l)
        b = book.bottleneck(l)
        mb = [x for x in (r['bottleneck_labels'] if r else []) if B.is_stmt_label(x)]
        cons = '—' if r is None else ('是' if set(b) == set(mb) else '否')
        gaps = named_gap_state(book, l)
        gtxt = '；'.join('%s%s' % (num(book, g), '（前提）' if n == 'premise' else ('（已点名）' if n else '（未点名）'))
                        for g, n in gaps) or '—'
        if level >= 2 and r is not None and not A and not G and not b and not mb and not gaps:
            trivial.append(l)
            continue
        ma = sorted(set(B.GLOBAL_MA[g] for g in G))
        mas = '、\\allowbreak '.join(x.replace('+', '+\\allowbreak ') for x in ma)
        if level >= 2:
            gcell = mas or '—'
            first = ((rid + '\\hspace{0.4em}\\allowbreak ') if rid else '') + num(book, l)
            mcell = ('同左' if (r and cons == '是' and b) else (nums_l(book, mb, level) if r else '—'))
        else:
            gcell = (nums(book, G) + ('（%s）' % mas if ma else '')) if G else '—'
            first = ((rid + '\\enspace ') if rid else '') + num(book, l) + '\\newline {\\scriptsize %s}' % Lz(l)
            mcell = nums(book, mb) if r else '—'
        body.append(' & '.join([first, tag_compact(st.tag, st.qualifier), tag_compact(book.content(l)),
                                nums_l(book, A, level, lim), gcell, nums_l(book, b, level, lim), mcell, cons, gtxt]) + ' \\\\')
    intro = ('每行给出一条主表陈述（%s）%s的依赖闭包：闭包沿 \\texttt{\\string\\uses} 计算，经过 '
             '$R_{\\mathrm{cond}}$ 陈述时沿其前提句；$R_{\\mathrm{OPE}}$ 陈述的 OPE 前提作为具名前提，不再展开。'
             '“瓶颈（计算）”为闭包中等级最低的技术性假设（若最低等级只由不含技术性假设的陈述达到，则为该陈述）%s。'
             % (cref_or(book, 'tab:summary-master', '第~25~章的总表'),
                '及附录~M--O 的 $R_{\\mathrm{cond}}$ 定理' if level <= 2 else '',
                '；编号按章合并（如“N.6, 8, 21”即 N.6、N.8、N.21），全局假设只列总称，“同左”表示总表的瓶颈与计算结果相同，'
                '陈述的标签见\\cref{tab:appP-status}' if level >= 2 else ''))
    table = longtable('主要定理的依赖闭包与瓶颈', 'tab:appP-uses',
                      ['陈述', '标签', '$c(S)$', '闭包中的技术性假设', '全局假设', '瓶颈（计算）', '瓶颈（总表）', '一致', '具名缺口'],
                      body, [2.8, 1.35, 0.85, 3.0, 1.75, 1.85, 1.85, 0.65, 1.35] if level <= 1 else
                      [1.85, 1.35, 0.85, 3.9, 1.5, 2.25, 1.9, 0.65, 1.3], font)
    out = [tex_header(meta, 'appP_uses.tex'), section_head(book, '主要定理的依赖闭包与瓶颈', 'sec:appP-uses', F), intro, table]
    if trivial:
        out.append('另有 %d 条主表陈述的依赖闭包中既无技术性假设也无全局假设，总表的“瓶颈”列亦为空（一致）：%s。'
                   % (len(trivial), nums(book, trivial, '、')))
    return '\n'.join(out) + '\n'


# ============================================================================================== checks table
def write_checks(book, meta, F, level):
    lines = [tex_header(meta, 'appP_checks.tex'), section_head(book, '一致性检查', 'sec:appP-checks', F)]
    cap = ('一致性检查的结果（生成程序 %s 版本 %s，日期 %s，源文件修订 \\texttt{%s}，压缩级别 %d；'
           'E 为错误，W 为警告，I 为信息）' % (TOOL, VERSION, meta['date'], meta['rev'], level))
    allpass = all(not F.of(c, 'E') and not F.of(c, 'W') for c in CHECKS)
    if level >= 3 and allpass:
        lines.append('全部一致性检查 C-P1--C-P17 均通过（%s）。\\refstepcounter{table}\\label{tab:appP-checks}' % cap)
    else:
        rows = []
        for c, desc in CHECKS.items():
            e, w, i = len(F.of(c, 'E')), len(F.of(c, 'W')), len(F.of(c, 'I'))
            res = '通过' if not (e or w) else ''
            parts = []
            if e:
                parts.append('E\\,%d' % e)
            if w:
                parts.append('W\\,%d' % w)
            if i:
                parts.append('I\\,%d' % i)
            res = (res + ('（' if res else '') + '，'.join(parts) + ('）' if res else '')) if parts else res
            ex = [f['zh'] for f in F.sorted_items() if f['check'] == c and f['sev'] in ('E', 'W')][:3]
            if not ex:
                ex = [f['zh'] for f in F.sorted_items() if f['check'] == c][:1]
            rows.append('\\mbox{%s} & %s & %s & %s \\\\' % (c, desc, res, '；\\newline '.join(x for x in ex if x) or '—'))
        lines.append(longtable(cap, 'tab:appP-checks', ['检查', '内容', '结果', '前三条发现'], rows, [1.15, 4.1, 1.7, 9.0],
                               '\\footnotesize' if level == 0 else '\\scriptsize', '一致性检查的结果（续）'))
        lines.append('完整的发现清单（按单元分组）见生成程序的报告文件 \\texttt{appP\\_report.txt}。')
    lines.append('\\FloatBarrier\\label{appP:end}')
    return '\n'.join(lines) + '\n'


# ============================================================================================== graphs
PT = 2.54 / 72.27
CHW = 0.525 * 6.0 * PT          # \tiny (6 pt) Latin Modern Mono character width, cm
CJKW = 6.0 * PT
LINEH = 7.0 * PT


def split_label(t, L):
    if len(t) <= L:
        return [t]
    seg = re.findall(r'[^-]+-?', t)
    n = len(seg)
    for k in range(2, n + 1):
        best = None
        for cuts in itertools.combinations(range(1, n), k - 1):
            parts, prev = [], 0
            for c in list(cuts) + [n]:
                parts.append(''.join(seg[prev:c]))
                prev = c
            m = max(len(x) for x in parts)
            if m <= L and (best is None or m < best[0]):
                best = (m, parts)
        if best:
            return best[1]
    return seg


def text_width(s):
    w = 0.0
    for ch in s:
        w += CJKW if ord(ch) > 0x2e80 else CHW
    return w


class GNode(object):
    def __init__(self, nid, kind, unit, label=None, text=None, members=None, order=None):
        self.id, self.kind, self.unit, self.label = nid, kind, unit, label
        self.text = text or []
        self.members = members or []
        self.order = order
        self.w = self.h = 0.0
        self.col = 0
        self.x = self.y = 0.0


def node_style(book, l):
    st = book.stmts[l]
    if st.type == 'asm':
        return 'bp asm'
    if st.type == 'conj':
        return 'bp conj'
    if st.type == 'def':
        return 'bp def'
    if st.tag == 'V':
        return 'bp V'
    if st.tag is None:
        return 'bp math'
    s = 'bp %s' % st.tag
    if st.tag == 'R' and st.qualifier == 'R_cond':
        s += ',bp cond'
    return s


class GraphBuilder(object):
    def __init__(self, book, master):
        self.book = book
        self.master = master
        self.mlab = [r['label'] for r in master if r['label'] in book.stmts]
        self.mstar = set(r['label'] for r in master if r['star'] and r['label'] in book.stmts)
        self.mrow = {r['label']: r for r in master}
        self.neck = set()
        for r in master:
            for b in r['bottleneck_labels']:
                if b.startswith('asm:'):
                    self.neck.add(b)
        self._anc = {}

    def graded(self, l):
        st = self.book.stmts.get(l)
        return st is not None and st.type not in ('def', 'rem', 'ex')

    def ancestors(self, l, _stack=None):
        if l in self._anc:
            return self._anc[l]
        _stack = _stack if _stack is not None else set()
        if l in _stack:
            return frozenset()
        _stack.add(l)
        res = set()
        st = self.book.stmts.get(l)
        if st is not None:
            for p in st.uses:
                if p in self.book.stmts:
                    res.add(p)
                    res |= self.ancestors(p, _stack)
        _stack.discard(l)
        res = frozenset(res)
        self._anc[l] = res
        return res

    # ---------------------------------------------------------------- selection
    def users_within(self, sel):
        S = self.book.stmts
        sset = set(sel)
        cnt = collections.Counter()
        for v in sel:
            for p in S[v].uses:
                if p in sset:
                    cnt[p] += 1
        return cnt

    def select(self, group, maxnodes):
        """Returns (selected, folded, units_in, main).  Skeleton (a): quotas -- the bottleneck assumptions of the
        starred master rows (<= 16, most used first), the R_cond theorems of App M-O (<= 6), then the starred master
        statements (theorems and conjectures first), then other master theorems; folded statements are not drawn
        (counted in the caption).  Per part (b-g) and h: FINAL_OUTLINE_v2 App P §P.7 node selection and fold rule."""
        bk = self.book
        S = bk.stmts
        if group == 'a':
            rc = [l for l, st in S.items() if st.unit in ('AppM', 'AppN', 'AppO') and st.type == 'thm'
                  and st.tag == 'R' and st.qualifier == 'R_cond']
            star = [l for l in self.mlab if l in self.mstar]
            starneck = collections.Counter()
            for l in star:
                for x in self.mrow[l]['bottleneck_labels']:
                    if x in S and S[x].type == 'asm':
                        starneck[x] += 1
                for x in bk.closure(l)[0]:
                    if x in S:
                        starneck[x] += 0
            asm_sel = sorted([a for a in starneck if starneck[a] > 0], key=lambda a: (-starneck[a], bk.sort_key(a)))[:16]
            reach = collections.Counter()
            for l in star:
                anc = self.ancestors(l)
                for r in rc:
                    if r in anc:
                        reach[r] += 1
            rc_sel = sorted(rc, key=lambda r: (-reach[r], bk.sort_key(r)))[:6]
            room = maxnodes - len(asm_sel) - len(rc_sel)
            cand = B.dedupe(star + [l for l in self.mlab if S[l].type in ('thm', 'conj')])
            used = self.users_within(cand)
            cand.sort(key=lambda l: (0 if l in self.mstar else 1, 0 if S[l].type in ('thm', 'conj') else 1,
                                     -used[l], bk.sort_key(l)))
            sel = B.dedupe(asm_sel + rc_sel + [l for l in cand if l not in asm_sel and l not in rc_sel][:max(0, room)])
            pool = set(self.mlab) | set(rc) | set(l for l, st in S.items() if st.type == 'asm')
            folded = sorted(pool - set(sel), key=bk.sort_key)
            return sorted(sel, key=bk.sort_key), folded, None, sel
        title, units = B.GRAPH_GROUPS[group]
        units_in = set(units)
        if group == 'h':
            main = [l for l, st in S.items() if st.unit in units_in and st.type != 'asm' and self.graded(l)
                    and any(B.is_chapter(S[u].unit) for u in bk.users.get(l, []) if u in S)]
        else:
            main = [l for l, st in S.items() if st.unit in units_in and (l in self.mrow or st.type == 'thm')]
        prem = []
        for m in main:
            for p in S[m].uses:
                if p in S and S[p].unit in units_in and S[p].type != 'asm' and self.graded(p) and p not in main:
                    prem.append(p)
        prem = B.dedupe(sorted(prem, key=bk.sort_key))
        asms = []
        for m in main:
            for p in list(S[m].uses) + list(S[m].premises):
                if p in S and S[p].type == 'asm':
                    asms.append(p)
        asms = B.dedupe(sorted(asms, key=bk.sort_key))
        sel = sorted(B.dedupe(main + prem + asms), key=bk.sort_key)
        mainset = set(main)

        def prio(l):
            st = S[l]
            if l in self.mstar:
                return 6
            if l in self.mrow:
                return 5
            if st.type == 'asm' and l in self.neck:
                return 4.5
            if l in mainset:
                return 4
            if st.type == 'asm':
                return 3
            return 1
        used = self.users_within(sel)

        def n_stubs(cur, fold):
            keys = set(('fold', S[f].unit) for f in fold)
            for v in cur:
                for p in S[v].uses:
                    if p in S and self.graded(p) and S[p].unit not in units_in and S[p].type != 'asm':
                        keys.add(('ext', S[p].unit))
            return len(keys)
        cur = list(sel)
        order = sorted(cur, key=lambda l: (prio(l), used[l], -bk.order.get(l, 0)))
        folded, k = [], 0
        while len(cur) + n_stubs(cur, folded) > maxnodes and k < len(order):
            v = order[k]
            k += 1
            cur.remove(v)
            folded.append(v)
        return cur, folded, units_in, main

    # ---------------------------------------------------------------- graph
    def build(self, group, maxnodes, L):
        bk = self.book
        S = bk.stmts
        cur, folded, units_in, main = self.select(group, maxnodes)
        nodes = collections.OrderedDict()
        for k, l in enumerate(sorted(cur, key=bk.sort_key)):
            st = S[l]
            txt = split_label(l.split(':', 1)[1], min(L, 10) if st.type == 'conj' else L)
            nodes[l] = GNode('n%d' % (k + 1), node_style(bk, l), st.unit, label=l, text=txt, order=bk.sort_key(l))
        stubs = collections.OrderedDict()
        if group != 'a':
            for f in folded:
                stubs.setdefault(('fold', S[f].unit), []).append(f)
            for v in cur:
                for p in S[v].uses:
                    if p in S and self.graded(p) and S[p].unit not in units_in and S[p].type != 'asm' and p not in cur:
                        stubs.setdefault(('ext', S[p].unit), []).append(p)
        k0 = len(nodes)
        for i, (key, mem) in enumerate(sorted(stubs.items(), key=lambda kv: (B.UNIT_INDEX.get(kv[0][1], 99), kv[0][0]))):
            kind, u = key
            mem = B.dedupe(mem)
            text = ['+%d' % len(mem)] if kind == 'fold' else [B.unit_name(u, tilde=False)]
            nodes[key] = GNode('n%d' % (k0 + i + 1), 'bp fold' if kind == 'fold' else 'bp stub', u, text=text, members=mem,
                               order=(B.UNIT_INDEX.get(u, 99), -1 if kind == 'ext' else 0, 0, ''))
        real = [l for l in nodes if isinstance(l, str)]
        anc = {l: self.ancestors(l) for l in real}
        rel = set()
        for v in real:
            for u in real:
                if u != v and u in anc[v]:
                    rel.add((u, v))
        edges = set()
        for (u, v) in rel:
            if any((u, w) in rel and (w, v) in rel for w in real if w != u and w != v):
                if not (S[u].type == 'asm' and bk.is_rcond(v) and u in S[v].uses):
                    continue
            edges.add((u, v))
        for key, g in nodes.items():
            if isinstance(key, str):
                continue
            for v in real:
                for m in g.members:
                    if m in anc[v] or m in S[v].uses:
                        if any(w in anc[v] and m in anc[w] for w in real if w != v):
                            continue
                        edges.add((key, v))
                        break
        red = set()
        for t in real:
            r = self.mrow.get(t)
            if r and S[t].tag == 'A':
                for b in r['bottleneck_labels']:
                    if b in nodes and isinstance(b, str):
                        red.add((b, t))
                        edges.add((b, t))
        return nodes, edges, red, folded, main

    # ---------------------------------------------------------------- layout
    def layout(self, nodes, edges, group_of, kcap, sep=0.25):
        """Layers left -> right by group (unit, or part for the skeleton) in book order; inside a group up to kcap
        sub-columns by longest-path depth; consecutive stub-only groups share one column.  Vertical order: book
        order, then barycentre sweeps; coordinates: isotonic placement towards the neighbours' mean."""
        bk = self.book
        ids = list(nodes)
        for key, g in nodes.items():
            w = max(text_width(t) for t in g.text) + (3.0 + 0.45) * PT
            h = max(0.40, len(g.text) * LINEH + (2 * 1.1 + 0.45 + 1.6) * PT)
            if g.kind == 'bp conj':
                w, h = w * 1.42 + 0.04, h * 1.30
            if g.kind == 'bp V':
                w, h = w + 0.05, h + 0.05
            g.w, g.h = w * 1.04, h
        gnodes = collections.OrderedDict()
        for key in sorted(ids, key=lambda k: nodes[k].order):
            gnodes.setdefault(group_of(nodes[key].unit), []).append(key)
        groups = sorted(gnodes, key=lambda gk: gk[0])
        depth = {k: 0 for k in ids}
        for _ in range(60):
            changed = False
            for (a, b) in edges:
                if isinstance(a, str) and isinstance(b, str) and group_of(nodes[a].unit) == group_of(nodes[b].unit):
                    if bk.sort_key(a) < bk.sort_key(b) and depth[b] < depth[a] + 1:
                        depth[b] = depth[a] + 1
                        changed = True
            if not changed:
                break
        cols, colmembers, stubrun = [], [], []

        def flush():
            if stubrun:
                cols.append((tuple(gk for gk, _ in stubrun), 0, True))
                colmembers.append([k for _, ks in stubrun for k in ks])
                stubrun[:] = []
        for gk in groups:
            ks = gnodes[gk]
            if all(not isinstance(k, str) for k in ks):
                stubrun.append((gk, ks))
                continue
            flush()
            dk = {k: (min(depth[k], kcap - 1) if isinstance(k, str) else 0) for k in ks}
            for d in range(max(dk.values()) + 1):
                mem = [k for k in ks if dk[k] == d]
                if mem:
                    cols.append(((gk,), d, False))
                    colmembers.append(mem)
        flush()
        col_of = {}
        for c, mem in enumerate(colmembers):
            for k in mem:
                col_of[k] = c
                nodes[k].col = c
        nb = collections.defaultdict(set)
        for (a, b) in edges:
            nb[a].add(b)
            nb[b].add(a)
        pos = {}
        for c, mem in enumerate(colmembers):
            mem.sort(key=lambda k: nodes[k].order)
            for i, k in enumerate(mem):
                pos[k] = i - (len(mem) - 1) / 2.0

        def sweep(forward):
            rng = range(len(colmembers)) if forward else range(len(colmembers) - 1, -1, -1)
            for c in rng:
                mem = colmembers[c]

                def bary(k):
                    ns = [n for n in nb[k] if (col_of[n] < c if forward else col_of[n] > c)]
                    return sum(pos[n] for n in ns) / len(ns) if ns else pos[k]
                mem.sort(key=lambda k: (bary(k), nodes[k].order))
                for i, k in enumerate(mem):
                    pos[k] = i - (len(mem) - 1) / 2.0
        for _ in range(4):
            sweep(True)
            sweep(False)
        z = {}
        for c, mem in enumerate(colmembers):
            acc = 0.0
            for i, k in enumerate(mem):
                if i:
                    acc += (nodes[mem[i - 1]].h + nodes[k].h) / 2 + sep
                z[k] = acc
            for k in mem:
                z[k] -= acc / 2

        def place(mem, desired):
            offs = [0.0]
            for i in range(1, len(mem)):
                offs.append(offs[-1] + (nodes[mem[i - 1]].h + nodes[mem[i]].h) / 2 + sep)
            blocks = []
            for i in range(len(mem)):
                blocks.append([desired[i] - offs[i], 1])
                while len(blocks) > 1 and blocks[-2][0] / blocks[-2][1] > blocks[-1][0] / blocks[-1][1]:
                    s2, c2 = blocks.pop()
                    blocks[-1][0] += s2
                    blocks[-1][1] += c2
            u = []
            for s1, c1 in blocks:
                u += [s1 / c1] * c1
            return [u[i] + offs[i] for i in range(len(mem))]
        for it in range(8):
            rng = list(range(len(colmembers)))
            if it % 2:
                rng.reverse()
            for c in rng:
                mem = colmembers[c]
                des = []
                for k in mem:
                    ns = [z[n] for n in nb[k] if col_of[n] != c]
                    des.append(sum(ns) / len(ns) if ns else z[k])
                for k, v in zip(mem, place(mem, des)):
                    z[k] = v
        widths = [max(nodes[k].w for k in mem) for mem in colmembers]
        xs = [0.0]
        for c in range(1, len(colmembers)):
            same = (not cols[c][2]) and (not cols[c - 1][2]) and cols[c][0] == cols[c - 1][0]
            xs.append(xs[-1] + widths[c - 1] / 2 + (0.14 if same else 0.30) + widths[c] / 2)
        top = max(-z[k] + nodes[k].h / 2 for k in ids)
        bot = min(-z[k] - nodes[k].h / 2 for k in ids)
        shift = (top + bot) / 2
        for k in ids:
            nodes[k].x = round(xs[col_of[k]], 3)
            nodes[k].y = round(-z[k] - shift, 3)
        return dict(cols=cols, colmembers=colmembers, xs=xs, widths=widths,
                    left=min(nodes[k].x - nodes[k].w / 2 for k in ids), right=max(nodes[k].x + nodes[k].w / 2 for k in ids),
                    top=max(nodes[k].y + nodes[k].h / 2 for k in ids), bot=min(nodes[k].y - nodes[k].h / 2 for k in ids))

    # ---------------------------------------------------------------- TikZ
    def tikz(self, nodes, edges, red, lay, group_label):
        out = []
        w = out.append
        heads = collections.OrderedDict()
        for c, (gks, d, stub) in enumerate(lay['cols']):
            if not stub:
                heads.setdefault(gks[0], []).append(c)
        top = lay['top']
        for gk, cs in heads.items():
            x = (lay['xs'][cs[0]] + lay['xs'][cs[-1]]) / 2
            w('\\node[bp unit] at (%.3f,%.3f) {%s};' % (x, top + 0.32, group_label(gk)))
        for c in range(1, len(lay['cols'])):
            if lay['cols'][c][0] != lay['cols'][c - 1][0] or lay['cols'][c][2] != lay['cols'][c - 1][2]:
                xsep = (lay['xs'][c] - lay['widths'][c] / 2 + lay['xs'][c - 1] + lay['widths'][c - 1] / 2) / 2
                w('\\draw[bp sep] (%.3f,%.3f) -- (%.3f,%.3f);' % (xsep, top + 0.18, xsep, lay['bot'] - 0.05))
        for key, g in nodes.items():
            txt = '\\\\'.join('\\detokenize{%s}' % t if g.label else t for t in g.text)
            w('\\node[%s] (%s) at (%.3f,%.3f) {%s};' % (g.kind, g.id, g.x, g.y, txt))
        w('\\begin{scope}[on background layer]')

        def ekey(e):
            a, b = e
            return ((e in red), str(nodes[a].order), str(nodes[b].order))
        for (a, b) in sorted(edges, key=ekey):
            ga, gb = nodes[a], nodes[b]
            if (a, b) in red:
                style = 'bp neck'
            elif not isinstance(a, str):
                style = 'bp stubuse'
            elif self.book.stmts[a].type == 'asm' and self.book.is_rcond(b):
                style = 'bp asmuse'
            else:
                style = 'bp use'
            if abs(ga.col - gb.col) > 2 and (a, b) not in red:
                style += ',bp long'
            if ga.col == gb.col:
                w('\\draw[%s] (%s) to[bend left=35] (%s);' % (style, ga.id, gb.id))
            else:
                w('\\draw[%s] (%s) -- (%s);' % (style, ga.id, gb.id))
        w('\\end{scope}')
        return out


def part_group(u):
    """Skeleton layers: parts (Ch1-5, Ch6-8, ..., App A-L, App M-O, App P-Q)."""
    p = B.UNIT_PART.get(u)
    if isinstance(p, int):
        return (p, p)
    if p == 'S':
        return (8, 'S')
    if u in ('AppM', 'AppN', 'AppO'):
        return (10, 'MO')
    if u in ('AppP', 'AppQ'):
        return (11, 'PQ')
    if B.is_appendix(u):
        return (9, 'AL')
    return (0, 'front')


PART_LABEL = {1: '第~1--5~章', 2: '第~6--8~章', 3: '第~9--13~章', 4: '第~14--18~章', 5: '第~19--20~章', 6: '第~21~章',
              7: '第~22--24~章', 'S': '第~25~章', 'AL': '附录~A--L', 'MO': '附录~M--O', 'PQ': '附录~P--Q', 'front': '前言'}


def unit_group(u):
    return (B.UNIT_INDEX.get(u, 99), u)


TIKZ_STYLES = r'''\begin{tikzpicture}[
  bp node/.style={draw,line width=0.45pt,rounded corners=1pt,font=\tiny\ttfamily,align=center,
                  inner xsep=1.5pt,inner ysep=1.1pt,minimum height=4mm},
  bp R/.style={bp node,fill=OliveGreen!15,draw=OliveGreen!60!black},
  bp A/.style={bp node,fill=RoyalBlue!15,draw=RoyalBlue!60!black},
  bp P/.style={bp node,fill=BurntOrange!15,draw=BurntOrange!70!black},
  bp C/.style={bp node,fill=Plum!15,draw=Plum!70!black},
  bp V/.style={bp node,fill=BrickRed!15,draw=BrickRed!70!black,double,double distance=0.6pt},
  bp cond/.style={dash pattern=on 1.6pt off 1pt},
  bp math/.style={bp node,fill=white,draw=black!60},
  bp def/.style={bp node,fill=white,draw=black!45,line width=0.3pt,rounded corners=0pt},
  bp conj/.style={bp node,ellipse,inner xsep=0pt,inner ysep=0pt,fill=Plum!15,draw=Plum!70!black},
  bp asm/.style={bp node,fill=orange!8,draw=orange!65!black,dash pattern=on 2pt off 1.2pt},
  bp stub/.style={bp node,font=\tiny,fill=gray!12,draw=gray!55,text=black!70},
  bp fold/.style={bp node,font=\tiny,fill=white,draw=gray!55,dash pattern=on 1pt off 1pt,text=black!70},
  bp unit/.style={font=\scriptsize,text=black!70,inner sep=1pt},
  bp sep/.style={draw=gray!40,line width=0.4pt,dash pattern=on 1pt off 1.5pt},
  bp key/.style={font=\scriptsize,anchor=west,inner sep=0pt},
  bp use/.style={draw=gray!60,line width=0.5pt,-{Stealth[length=2.6pt,width=2.2pt]}},
  bp stubuse/.style={draw=gray!45,line width=0.45pt,dash pattern=on 1.2pt off 1pt,-{Stealth[length=2.6pt,width=2.2pt]}},
  bp asmuse/.style={draw=orange!65!black,line width=0.5pt,dash pattern=on 2pt off 1.2pt,-{Stealth[length=2.6pt,width=2.2pt]}},
  bp neck/.style={draw=red!60!black,line width=1.1pt,-{Stealth[length=3.6pt,width=3.2pt]}},
  bp long/.style={opacity=0.5}]'''

LEGEND = r'''  \begin{scope}[shift={(%(x).3f,%(y).3f)}]
    \node[bp R,anchor=west,minimum width=4.5mm] (k1) at (0,0) {R};
    \node[bp R,bp cond,anchor=west,minimum width=4.5mm,right=0.8mm of k1] (k2) {R};
    \node[bp A,anchor=west,minimum width=4.5mm,right=0.8mm of k2] (k3) {A};
    \node[bp P,anchor=west,minimum width=4.5mm,right=0.8mm of k3] (k4) {P};
    \node[bp C,anchor=west,minimum width=4.5mm,right=0.8mm of k4] (k5) {C};
    \node[bp V,anchor=west,minimum width=4.5mm,right=0.8mm of k5] (k6) {V};
    \node[bp key,right=1.2mm of k6] (t1) {严格性标签（虚线框为 $R_{\rm cond}$）};
    \node[bp conj,anchor=west,minimum width=7mm,minimum height=3.4mm,right=2.5mm of t1] (k7) {};
    \node[bp key,right=1mm of k7] (t2) {猜想};
    \node[bp asm,anchor=west,minimum width=4.5mm,right=2.5mm of t2] (k8) {};
    \node[bp key,right=1mm of k8] (t3) {编号假设};
    \node[bp math,anchor=west,minimum width=4.5mm,right=2.5mm of t3] (k9) {};
    \node[bp key,right=1mm of k9] (t4) {纯数学};
    \node[bp stub,anchor=west,minimum width=4.5mm,right=2.5mm of t4] (k10) {};
    \node[bp key,right=1mm of k10] (t5) {其他单元};
    \node[bp fold,anchor=west,minimum width=4.5mm,right=2.5mm of t5] (k11) {$+k$};
    \node[bp key,right=1mm of k11] {折叠};
    \draw[bp use] (0,-0.42) -- ++(6mm,0) coordinate (e1);
    \node[bp key] (u1) at ($(e1)+(1.2mm,0)$) {依赖（前提指向陈述）};
    \draw[bp asmuse] ($(u1.east)+(2.5mm,0)$) -- ++(6mm,0) coordinate (e2);
    \node[bp key] (u2) at ($(e2)+(1.2mm,0)$) {编号假设 $\to R_{\rm cond}$};
    \draw[bp neck] ($(u2.east)+(2.5mm,0)$) -- ++(6mm,0) coordinate (e3);
    \node[bp key] (u3) at ($(e3)+(1.2mm,0)$) {瓶颈依赖（主表）};
    \draw[bp use,bp long] ($(u3.east)+(2.5mm,0)$) -- ++(6mm,0) coordinate (e4);
    \node[bp key] (u4) at ($(e4)+(1.2mm,0)$) {跨两列以上};
    \draw[bp stubuse] ($(u4.east)+(2.5mm,0)$) -- ++(6mm,0) coordinate (e5);
    \node[bp key] at ($(e5)+(1.2mm,0)$) {来自其他单元};
  \end{scope}'''
LEGEND_W, LEGEND_H = 15.2, 0.75

CAPTION_TAIL = ('框的颜色为严格性标签，虚线框为 $R_{\\rm cond}$ 条件定理，橙色虚线框为编号假设，椭圆为猜想，双线框为 [V]，白色框为纯数学%s。'
                '边由前提指向陈述，是可达关系在所画节点上的传递约化（经由未画出陈述的依赖也画成一条边）；'
                '橙色虚线边为编号假设到 $R_{\\rm cond}$ 陈述的依赖，粗红线为决定全阶论证地位的瓶颈依赖（取自主表“瓶颈”列），半透明线跨越两列以上。')
STUB_NOTE = ('；灰色框代表%s之外的单元（该单元中被直接使用的陈述合并为一个节点），虚线白框“$+k$”为按折叠规则省略的 $k$ 个次要陈述')

# (sub-column cap, characters per label line), in order of preference
GRAPH_CONFIGS = [(3, 12), (3, 10), (2, 12), (2, 10), (3, 8), (2, 8), (1, 12), (1, 10), (1, 8)]


def graph_file(gb, group, level, meta, report, pre=''):
    maxn = 60 if level < 2 else 40
    half = (level >= 2 and group != 'a')
    hmax = 9.6 if half else 20.5
    group_of = part_group if group == 'a' else unit_group
    group_label = (lambda gk: PART_LABEL.get(gk[1], str(gk[1]))) if group == 'a' else (lambda gk: B.unit_name(gk[1]))
    best = None
    built = {}
    for (kcap, L) in GRAPH_CONFIGS:
        if L not in built:
            built[L] = gb.build(group, maxn, L)
        nodes, edges, red, folded, main = built[L]
        if not nodes:
            break
        lay = gb.layout(nodes, edges, group_of, kcap)
        W = max(lay['right'] - lay['left'], LEGEND_W)
        H = lay['top'] - lay['bot'] + 0.55 + LEGEND_H + 0.2
        fits_plain = W <= 15.9 and H <= hmax
        fits_rot = (not half) and H <= 15.9 and W <= 20.8
        cand = dict(kcap=kcap, L=L, nodes=nodes, edges=edges, red=red, folded=folded, main=main, lay=lay, W=W, H=H,
                    rot=(not fits_plain) and fits_rot, ok=fits_plain or fits_rot)
        if cand['ok']:
            best = cand
            break
        s_plain = min(15.9 / W, hmax / H)
        s_rot = 0 if half else min(20.8 / W, 15.9 / H)
        cand['scale'] = max(s_plain, s_rot)
        cand['rot'] = s_rot > s_plain
        if best is None or cand['scale'] > best.get('scale', 0) + 1e-9:
            best = cand
    label = 'fig:appP-dependency' + ('' if group == 'a' else '-' + group)
    head = tex_header(meta, 'appP_graph_%s.tex' % group)
    if best is None:
        report.append('graph %s: no nodes' % group)
        body = ('\\begin{figure}[htbp]\\centering\\fbox{\\parbox{0.8\\textwidth}{\\centering\\vspace{1cm}（本部分尚无可画的陈述）'
                '\\vspace{1cm}}}\\caption{%s}\\label{%s}\\end{figure}' % (graph_caption(group, 0, 0, 0), label))
        return head + pre + body + '\n', dict(group=group, nodes=0)
    nodes, lay = best['nodes'], best['lay']
    lines = gb.tikz(nodes, best['edges'], best['red'], lay, group_label)
    legend = LEGEND % dict(x=lay['left'], y=lay['bot'] - 0.55)
    pic = TIKZ_STYLES + '\n' + '\n'.join('  ' + x for x in lines) + '\n' + legend + '\n\\end{tikzpicture}'
    nreal = sum(1 for k in nodes if isinstance(k, str))
    nstub = len(nodes) - nreal
    scale = best.get('scale') if not best['ok'] else None
    if best['rot']:
        inner = '\\rotatebox{90}{%s}' % (('\\resizebox{%.3fcm}{!}{%s}' % (best['W'] * scale, pic)) if scale else pic)
        place = 'p'
    else:
        inner = ('\\resizebox{%.3fcm}{!}{%s}' % (best['W'] * scale, pic)) if scale else pic
        place = 'tbp' if half else ('p' if best['H'] > 12 else 'tbp')
    cap = graph_caption(group, nreal, nstub, len(best['folded']))
    body = '\\begin{figure}[%s]\n\\centering\n%s\n\\caption{%s}\\label{%s}\n\\end{figure}' % (place, inner, cap, label)
    info = dict(group=group, nodes=nreal, stubs=nstub, folded=len(best['folded']), edges=len(best['edges']),
                red=len(best['red']), width_cm=round(best['W'], 2), height_cm=round(best['H'], 2), rotated=bool(best['rot']),
                scale=round(scale, 3) if scale else 1.0, label_chars=best['L'], subcolumns=best['kcap'])
    report.append('graph %s: %d nodes + %d stubs (%d folded), %d edges (%d red), %.1f x %.1f cm, rotated %s, scale %s, '
                  'sub-columns <= %d, label lines <= %d chars' % (group, nreal, nstub, len(best['folded']), len(best['edges']),
                                                                 len(best['red']), best['W'], best['H'], best['rot'],
                                                                 info['scale'], best['kcap'], best['L']))
    return head + pre + body + '\n', info


def graph_caption(group, nreal, nstub, nfold):
    if group == 'a':
        head = ('本书主要陈述的依赖图（骨架；由各环境中的 \\texttt{\\string\\uses} 自动生成）：总表中的主要陈述、它们的瓶颈假设与附录~M--O 的 '
                '$R_{\\rm cond}$ 定理（%d 个节点%s；按书序自左向右分层，每层为一部分，层内按依赖深度分列；其余各图每层为一个单元）。'
                % (nreal, '，另有 %d 个陈述按折叠规则未画出' % nfold if nfold else ''))
        return head + CAPTION_TAIL % ''
    title, units = B.GRAPH_GROUPS[group]
    tail = ('图例与画法同\\cref{fig:appP-dependency}；灰色框代表%s之外的单元，“$+k$”为按折叠规则省略的 $k$ 个次要陈述。'
            % ('附录~M--O' if group == 'h' else '本部分'))
    if group == 'h':
        return ('%s中被各章陈述使用的陈述及其编号假设的依赖图（%d 个陈述节点、%d 个汇总节点）。' % (title, nreal, nstub)) + tail
    return ('%s主要定理的依赖图：总表中的陈述与本部分的全部定理、它们在本部分内的直接前提及所用的编号假设（%d 个陈述节点、%d 个汇总节点）。'
            % (title, nreal, nstub)) + tail


# ============================================================================================== stub mode
def write_stubs(out, meta, book, F):
    files = {}
    note = '（本节由 blueprint\\_gen.py 生成；此为第一遍编译的占位。）'
    files['appP_register.tex'] = (tex_header(meta, 'appP_register.tex (stub)') + section_head(book, '假设登记表', 'sec:appP-register', F)
                                  + note + '\\refstepcounter{table}\\label{tab:appP-register}\n')
    files['appP_status.tex'] = (tex_header(meta, 'appP_status.tex (stub)') + section_head(book, '全部陈述的状态表', 'sec:appP-status', F)
                                + note + '\\refstepcounter{table}\\label{tab:appP-status}\n')
    files['appP_uses.tex'] = (tex_header(meta, 'appP_uses.tex (stub)') + section_head(book, '主要定理的依赖闭包与瓶颈', 'sec:appP-uses', F)
                              + note + '\\refstepcounter{table}\\label{tab:appP-uses}\n')
    files['appP_graph_a.tex'] = (tex_header(meta, 'appP_graph_a.tex (stub)') + section_head(book, '依赖图', 'sec:appP-graphs', F)
                                 + note + '\\refstepcounter{figure}\\label{fig:appP-dependency}\n')
    for g in 'bcdefgh':
        files['appP_graph_%s.tex' % g] = (tex_header(meta, 'appP_graph_%s.tex (stub)' % g)
                                          + '\\refstepcounter{figure}\\label{fig:appP-dependency-%s}\n' % g)
    files['appP_checks.tex'] = (tex_header(meta, 'appP_checks.tex (stub)') + section_head(book, '一致性检查', 'sec:appP-checks', F)
                                + note + '\\refstepcounter{table}\\label{tab:appP-checks}\n\\FloatBarrier\\label{appP:end}\n')
    for n, t in files.items():
        write(os.path.join(out, n), t)


def write(path, text):
    with open(path, 'w', encoding='utf-8') as f:
        f.write(text)


# ============================================================================================== json / report
def blueprint_json(book, master, aux, F, meta, graphs):
    nodes = []
    for l, st in book.stmts.items():
        A, G, S, O = book.closure(l)
        n = aux.get(l, ('', '', '', ''))
        nodes.append(dict(label=l, type=st.type, unit=st.unit, unit_index=B.UNIT_INDEX[st.unit], file=st.file, line=st.line,
                          section=st.section, title=st.title_text, tag=st.tag, qualifier=st.qualifier,
                          premises=st.premises, uses=st.uses, np_line=st.np_labels if st.np_line else None,
                          partonic=st.partonic, status_paragraph=st.status_paragraph, status_labels=st.status_labels,
                          errtype=st.errtype, pending=st.pending, number=n[0], page=n[1],
                          content_grade=book.content(l), tech_closure=sorted(A, key=book.sort_key),
                          global_closure=sorted(G, key=book.sort_key), bottleneck=book.bottleneck(l),
                          used_by=book.users.get(l, []), canonical=(l in book.registry.info or l in book.register)))
    edges = [[p, l] for l, st in book.stmts.items() for p in st.uses if p in book.stmts]
    return dict(meta=meta, nodes=nodes, edges=edges, master=[dict((k, v) for k, v in r.items()) for r in master],
                findings=F.sorted_items(), graphs=graphs,
                counts=dict(statements=len(book.stmts), edges=len(edges), units=book.present,
                            E=F.count('E'), W=F.count('W'), I=F.count('I')))


def report_text(book, F, meta, extra):
    out = []
    w = out.append
    w('App P generator report -- blueprint_gen.py %s (level %s, %s mode) -- %s -- sources %s' % (
        VERSION, meta['level'], 'stub' if meta['stub'] else 'full', meta['date'], meta['rev']))
    w('units present (%d): %s' % (len(book.present), ' '.join(book.present)))
    missing = [u for u in B.UNITS if u not in book.present]
    w('units not present (%d): %s' % (len(missing), ' '.join(missing)))
    w('statements: %d   \\uses edges: %d   master-table source: %s' % (
        len(book.stmts), sum(len(st.uses) for st in book.stmts.values()), meta['master_source']))
    c = collections.Counter((st.tag or '-') + ('/' + st.qualifier if st.tag == 'R' and st.qualifier else '') for st in book.stmts.values())
    w('tags: ' + ', '.join('%s %d' % (k, v) for k, v in sorted(c.items())))
    for x in extra:
        w(x)
    w('findings: E %d, W %d, I %d' % (F.count('E'), F.count('W'), F.count('I')))
    w('')
    w('== summary per check')
    for ck, desc in CHECKS.items():
        w('%-6s E %4d  W %4d  I %4d   %s' % (ck, len(F.of(ck, 'E')), len(F.of(ck, 'W')), len(F.of(ck, 'I')),
                                           re.sub(r'\\[a-zA-Z]+\{?|[{}$]', '', desc)))
    w('')
    w('== findings per check')
    for ck in CHECKS:
        items = [f for f in F.sorted_items() if f['check'] == ck]
        if not items:
            continue
        w('-- %s (%d)' % (ck, len(items)))
        for f in items:
            loc = ('%s:%s' % (f['file'], f['line'])) if f['file'] else (f['unit'] or '')
            w('  [%s] %-34s %-28s %s' % (f['sev'], f['label'] or '', loc, f['msg']))
    w('')
    w('== findings per unit (for return to the writers)')
    byu = collections.defaultdict(list)
    for f in F.sorted_items():
        byu[f['unit'] or '(book)'].append(f)
    for u in sorted(byu, key=lambda x: B.UNIT_INDEX.get(x, 99)):
        items = sorted(byu[u], key=lambda f: (f['line'] or 0, f['check']))
        e = sum(1 for f in items if f['sev'] == 'E')
        wn = sum(1 for f in items if f['sev'] == 'W')
        w('-- %s  (E %d, W %d, I %d)' % (u, e, wn, len(items) - e - wn))
        for f in items:
            w('  %s:%s [%s %s] %s %s' % (f['file'] or '', f['line'] or '', f['check'], f['sev'], f['label'] or '', f['msg']))
    return '\n'.join(out) + '\n'


# ============================================================================================== main
def appP_pages(aux):
    """(pages of App P, how) from the .aux: page(app:appQ) - page(app:appP), else page(appP:end) - page(app:appP) + 1."""
    def pg(l):
        v = aux.get(l)
        if not v:
            return None
        try:
            return int(v[1])
        except ValueError:
            return None
    a = pg('app:appP')
    if a is None:
        return None, 'app:appP not in the aux'
    q = pg('app:appQ')
    if q is not None:
        return q - a, 'page(app:appQ) - page(app:appP)'
    e = pg('appP:end')
    if e is not None:
        return e - a + 1, 'page(appP:end) - page(app:appP) + 1'
    return None, 'no end label'


def main():
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument('--root', default=None, help='directory against which the master\'s \\input paths are resolved '
                    '(default: the directory of --master)')
    ap.add_argument('--master', required=True)
    ap.add_argument('--aux', default=None)
    ap.add_argument('--outline', required=True)
    ap.add_argument('--register', required=True)
    ap.add_argument('--out', required=True)
    ap.add_argument('--level', type=int, default=0, choices=[0, 1, 2, 3])
    ap.add_argument('--final', action='store_true')
    ap.add_argument('--stub', action='store_true')
    ap.add_argument('--date', default=None)
    a = ap.parse_args()
    master_path = a.master if os.path.isabs(a.master) or a.root is None else os.path.join(a.root, a.master)
    if not os.path.exists(master_path) and os.path.exists(a.master):
        master_path = a.master
    root = a.root or os.path.dirname(os.path.abspath(master_path))
    aux_path = a.aux
    if aux_path and not os.path.isabs(aux_path) and not os.path.exists(aux_path) and a.root:
        aux_path = os.path.join(a.root, aux_path)
    inputs = B.read_master_inputs(master_path, root)
    unit_paths = [(u, p) for (u, p, ex) in inputs if ex]
    registry = B.read_outline(a.outline)
    register = B.read_register(a.register)
    book = B.load_book(unit_paths, registry, register)
    aux = B.parse_aux(aux_path) if aux_path else {}
    AUXNUM.clear()
    AUXNUM.update((k, v[0]) for k, v in aux.items())
    srcs = [p for (u, p) in unit_paths]
    if a.date:
        date = a.date
    else:
        mt = [os.path.getmtime(p) for p in srcs + [a.outline, a.register] if os.path.exists(p)]
        date = datetime.date.fromtimestamp(max(mt)).isoformat() if mt else datetime.date.today().isoformat()
    master, msrc = master_rows(book)
    meta = dict(version=VERSION, level=a.level, date=date, rev=B.sources_revision(srcs + [a.outline, a.register]),
                stub=a.stub, final=a.final, master_source=msrc, aux=bool(aux))
    F = Findings()
    run_checks(book, master, F, final=a.final)
    os.makedirs(a.out, exist_ok=True)
    extra = []
    pages, how = appP_pages(aux) if aux else (None, 'no aux')
    extra.append('App P pages in the aux: %s (%s)' % (pages if pages is not None else 'n/a', how))
    graphs = []
    if a.stub:
        write_stubs(a.out, meta, book, F)
    else:
        write(os.path.join(a.out, 'appP_register.tex'), write_register(book, meta, F, a.level))
        write(os.path.join(a.out, 'appP_status.tex'), write_status(book, meta, F, a.level))
        write(os.path.join(a.out, 'appP_uses.tex'), write_uses(book, master, meta, F, a.level))
        gb = GraphBuilder(book, master)
        gpre = section_head(book, '依赖图', 'sec:appP-graphs', F) + (
            '本节的图由 \\texttt{\\string\\uses} 数据自动生成：\\cref{fig:appP-dependency}为全书骨架，其余各图依次给出各部分的主要定理'
            '（每图至多 %d 个节点，超出时按折叠规则省略使用者最少的次要前提）。\n' % (60 if a.level < 2 else 40))
        for g in 'abcdefgh':
            txt, info = graph_file(gb, g, a.level, meta, extra, gpre if g == 'a' else '')
            graphs.append(info)
            write(os.path.join(a.out, 'appP_graph_%s.tex' % g), txt)
        write(os.path.join(a.out, 'appP_checks.tex'), write_checks(book, meta, F, a.level))
    js = blueprint_json(book, master, aux, F, meta, graphs)
    with open(os.path.join(a.out, 'blueprint.json'), 'w', encoding='utf-8') as f:
        json.dump(js, f, ensure_ascii=False, indent=1, sort_keys=True)
    write(os.path.join(a.out, 'appP_report.txt'), report_text(book, F, meta, extra))
    print('blueprint_gen %s: %d units, %d statements, level %d%s; findings E %d, W %d, I %d; App P pages (aux): %s -> %s' % (
        VERSION, len(book.present), len(book.stmts), a.level, ' (stub)' if a.stub else '', F.count('E'), F.count('W'),
        F.count('I'), pages if pages is not None else 'n/a', a.out))
    sys.exit(1 if F.count('E') else 0)


if __name__ == '__main__':
    main()
