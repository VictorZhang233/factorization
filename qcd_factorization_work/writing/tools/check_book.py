#!/usr/bin/env python3
r"""check_book.py -- whole-book consistency checker for the unit files (usable before integration).

    python3 -I check_book.py --chapters chapters --outline spec_v2/FINAL_OUTLINE_v2.md --register spec_v2/ASSUMPTIONS.md
            [--bib spec_v2/refs_merged_v2.bib] [--out build/check_book.txt] [--max 40]

Reads every unit file present in --chapters (file names of WRITER_SPEC_v2 §1.1; part prefaces such as
part7_preface.tex are scanned for references and markers only), the label registry and master rows of FINAL_OUTLINE_v2
and the assumption register.  Checks (E = error, W = warning, I = information):
  K1  duplicate labels (within a unit and across units)
  K2  references to labels that no present unit defines: canonical label of a unit not yet written (I, counted per
      unit) vs. canonical label missing although its owner is present (E) vs. unknown / withdrawn / foreign eq: label (E)
  K3  canonical labels missing in their (present) owner unit; canonical labels defined in another unit
  K4  \uses order violations (forward edges: chapter -> later chapter, same unit -> later statement) and cycles;
      hidden forward dependencies through appendix statements (W)
  K5  tags (and qualifiers) that differ from the registry (strengthened E; weakened / changed W) and assumption tags
      that differ from the register
  K6  [R] qualifier sentences: missing, not verbatim, not first, short R_OPE form before the long one
  K7  R_cond without the premise sentence, or not among the first two sentences
  K8  [A]/[P]/[C]/[V] statements without a 「地位与缺口」 paragraph (E), or not immediately after (W)
  K9  printed planning markers 「位置待核实」「待核实」「文献待补」「待文献核查」 PENDING TODO FIXME (E; in comments: I)
  K10 forbidden phrasing of WRITER_SPEC_v2 §4.11 next to [A] statements (「严格证明了」「已被证明」 inside or after an [A]
      environment, or within 60 characters of a \cref to an [A] statement: E); the other phrases of check_unit_v2.py
      C8b anywhere in printed text (W, to be justified in context)
  K11 mentions of the reference document (factorization_qcd, 参考文档, reference document, refdoc ...) (E; comments W)
  K12 label lists with spaces or line breaks in \cref/\uses (cleveref prints "??"; figsync --normalize-refs repairs the
      build copy) (E)
  K13 \uses format: missing \uses / "% uses: none" (E), several \uses (E), non-statement labels in \uses (E)
  K14 assumption environments without the fields 地位/文献/被使用于/解除途径 (W)
  K15 citation keys not in the bibliography (base file + chapters/*.bib-additions) (E)
  K16 figure-block delimiters (unbalanced or non-standard %%% BEGIN/END) (W)
  plus a per-unit summary table.  Output: plain text (--out, also printed).  Exit code 0 always (it is a report).
"""
import os, re, sys, glob, argparse, collections
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import booklib as B

MARKERS = ['位置待核实', '待核实', '文献待补', '待文献核查', 'PENDING', 'TODO', 'FIXME']
REFDOC = [r'factorization[_\\]*_?qcd', r'参考文档', r'参考文件', r'reference document', r'\brefdoc\b', r'REFDOC']
FORBIDDEN_A = ['严格证明了', '已被证明']
C8B = ['软因子等于 1', '格点检验了因子化', 'Glauber 胶子在单举截面中总是相消', '偶极子公式对所有阶精确',
       '本书新结果', '首次', '文献中未见', '独立确认', '尚待']
CHECKS = collections.OrderedDict([
    ('K1', 'duplicate labels'), ('K2', 'references to undefined labels'), ('K3', 'canonical labels missing / misplaced'),
    ('K4', '\\uses order and cycles'), ('K5', 'tags vs registry'), ('K6', '[R] qualifier sentences'),
    ('K7', 'R_cond premise sentences'), ('K8', '「地位与缺口」 paragraphs'), ('K9', 'printed planning markers'),
    ('K10', 'forbidden phrasing (§4.11) and phrases to justify'), ('K11', 'reference document mentioned'),
    ('K12', 'label lists with spaces (prints ??)'), ('K13', '\\uses format'), ('K14', 'assumption fields'),
    ('K15', 'citation keys not in the bibliography'), ('K16', 'figure-block delimiters')])


class Rep(object):
    def __init__(self):
        self.items = []

    def add(self, k, sev, unit, file, line, msg):
        self.items.append((k, sev, unit or '', file or '', line or 0, msg))


def bib_keys(base, chapters):
    keys = set()
    for p in [base] + sorted(glob.glob(os.path.join(chapters, '*.bib-additions'))):
        if p and os.path.exists(p):
            for m in re.finditer(r'@\s*[A-Za-z]+\s*[{(]\s*([^,\s]+)\s*,', B.read_text(p)):
                keys.add(m.group(1).lower())
    return keys


def main():
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument('--chapters', required=True)
    ap.add_argument('--outline', required=True)
    ap.add_argument('--register', required=True)
    ap.add_argument('--bib', default=None)
    ap.add_argument('--out', default=None)
    ap.add_argument('--max', type=int, default=40, help='maximum findings listed per check and unit in the detail part')
    a = ap.parse_args()
    R = B.read_outline(a.outline)
    reg = B.read_register(a.register)
    found, unknown = B.find_unit_files(a.chapters)
    bk = B.load_book(found, R, reg)
    present = set(bk.present)
    aux = []
    for f in sorted(unknown):
        p = os.path.join(a.chapters, f)
        U = B.parse_unit(p, 'front')        # parsed as a text file only (no unit semantics)
        U.uid = f
        aux.append(U)
    rp = Rep()
    S = bk.stmts
    withdrawn = set(R.withdrawn.values())
    canon = set(R.owner) | set(R.asm) | set(reg) | set(B.CHAPTER_LABEL.values()) | set(R.optional)
    defined = set(bk.dups)
    all_units = list(bk.units) + aux

    # K1 duplicates
    for lab, defs in sorted(bk.dups.items()):
        if len(defs) > 1:
            u, f, ln = defs[0]
            rp.add('K1', 'E', u, f, ln, '%s defined %d times: %s' % (lab, len(defs), '; '.join('%s:%d' % (x[1], x[2]) for x in defs)))
    for U in aux:
        for (lab, off, ln) in U.labels:
            rp.add('K1', 'W', U.uid, U.file, ln, 'label %s defined in a non-unit file (part preface)' % lab)
    # K2 references
    absent_refs = collections.defaultdict(set)
    for U in all_units:
        own = set(l for (l, o, ln) in U.labels)
        for (lab, cmd, off, ln) in U.refs:
            if lab in defined or lab in B.GENERATED_LABELS or '#' in lab:
                continue
            if lab in withdrawn:
                rp.add('K2', 'E', U.uid, U.file, ln, 'reference to the withdrawn slot label %s' % lab)
            elif lab.startswith('eq:') and lab not in own:
                rp.add('K2', 'E', U.uid, U.file, ln, 'reference to the equation label %s of another unit (equation labels '
                                                    'are unit-internal, WRITER_SPEC_v2 §5.4)' % lab)
            elif lab in canon:
                ow = bk.unit_of(lab)
                if ow in present:
                    rp.add('K2', 'E', U.uid, U.file, ln, 'canonical label %s is not defined although its owner %s is present'
                           % (lab, ow))
                else:
                    absent_refs[U.uid].add(lab)
            elif lab != lab.strip() or ' ' in lab:
                pass      # K12
            else:
                rp.add('K2', 'E', U.uid, U.file, ln, 'unknown label %s (not defined, not in the registry; %s)' % (lab, cmd))
    for u, labs in sorted(absent_refs.items(), key=lambda kv: B.UNIT_INDEX.get(kv[0], 99)):
        owners = collections.Counter(bk.unit_of(l) or '?' for l in labs)
        rp.add('K2', 'I', u, B.UNIT_FILE.get(u, u), 0, '%d canonical labels of units not yet written (%s)' % (
            len(labs), ', '.join('%s %d' % (k, v) for k, v in sorted(owners.items(), key=lambda kv: B.UNIT_INDEX.get(kv[0], 99)))))
    # K3 canonical labels missing / misplaced
    for (u, lab, typ, tag, q, math_, title) in R.rows:
        if u in present and lab not in defined and lab not in B.GENERATED_LABELS:
            rp.add('K3', 'E', u, B.UNIT_FILE[u], 0, 'canonical %s label %s (%s) is missing' % (typ, lab, title[:40]))
    for lab, a_ in reg.items():
        if a_.get('owner') in present and lab not in defined:
            rp.add('K3', 'E', a_['owner'], B.UNIT_FILE.get(a_['owner']), 0, 'registered assumption %s is missing' % lab)
    for lab, defs in sorted(bk.dups.items()):
        ow = R.owner.get(lab)
        for (u, f, ln) in defs:
            if ow and u != ow:
                rp.add('K3', 'E', u, f, ln, '%s is owned by %s (registry), defined here' % (lab, ow))
    for U in bk.units:
        if U.uid in B.CHAPTER_LABEL and U.chapter_label != B.CHAPTER_LABEL[U.uid]:
            rp.add('K3', 'E', U.uid, U.file, 1, 'chapter label is %s, expected %s' % (U.chapter_label, B.CHAPTER_LABEL[U.uid]))
    # K4 order, cycles
    for l, st in S.items():
        for p in st.uses:
            if not B.is_stmt_label(p):
                continue
            pu = bk.unit_of(p)
            if pu is None:
                continue
            if pu == st.unit:
                if p in S and bk.order[p] > bk.order[l]:
                    rp.add('K4', 'E', st.unit, st.file, st.line, '%s uses %s, defined later in the same unit' % (l, p))
            elif not B.is_appendix(st.unit) and not B.is_appendix(pu) and B.UNIT_INDEX[pu] > B.UNIT_INDEX[st.unit]:
                rp.add('K4', 'E', st.unit, st.file, st.line, '%s uses %s of the later unit %s' % (l, p, pu))
    for l, st in S.items():
        if not B.is_chapter(st.unit):
            continue
        k = B.UNIT_INDEX[st.unit]
        seen, stack = set(), [p for p in st.uses if p in S and B.is_appendix(S[p].unit)]
        while stack:
            x = stack.pop()
            if x in seen:
                continue
            seen.add(x)
            for q in S[x].uses:
                if q in S:
                    if B.is_appendix(S[q].unit):
                        stack.append(q)
                    elif B.is_chapter(S[q].unit) and B.UNIT_INDEX[S[q].unit] > k:
                        rp.add('K4', 'W', st.unit, st.file, st.line, 'hidden forward dependency: %s -> %s -> %s (%s)' % (
                            l, x, q, S[q].unit))
    sys.setrecursionlimit(max(10000, 4 * len(S) + 100))
    index, low, onst, stck, cnt = {}, {}, set(), [], [0]

    def strong(v):
        index[v] = low[v] = cnt[0]
        cnt[0] += 1
        stck.append(v)
        onst.add(v)
        for w_ in S[v].uses:
            if w_ in S:
                if w_ not in index:
                    strong(w_)
                    low[v] = min(low[v], low[w_])
                elif w_ in onst:
                    low[v] = min(low[v], index[w_])
        if low[v] == index[v]:
            comp = []
            while True:
                w_ = stck.pop()
                onst.discard(w_)
                comp.append(w_)
                if w_ == v:
                    break
            if len(comp) > 1 or v in S[v].uses:
                c = sorted(comp, key=bk.sort_key)
                st = S[c[0]]
                rp.add('K4', 'E', st.unit, st.file, st.line, 'dependency cycle: ' + ' -> '.join(c))
    for v in S:
        if v not in index:
            strong(v)
    # K5 tags vs registry
    for l, st in S.items():
        if st.type == 'asm':
            rt = (reg.get(l) or R.asm.get(l) or {}).get('tag', 'n/a')
            if rt != 'n/a' and rt != st.tag:
                strong_ = st.tag and (rt is None or B.RANK[st.tag] > B.RANK[rt])
                rp.add('K5', 'E' if strong_ else 'W', st.unit, st.file, st.line,
                       '%s: assumption tag [%s], register [%s]' % (l, st.tag or '-', rt or '-'))
            continue
        if l not in R.info:
            continue
        rt, rq, rm = R.tag_of(l)
        sq = st.qualifier if st.tag == 'R' else None
        if (st.tag, sq) == (rt, rq) or (st.tag == 'R' and sq is None and rt == 'R'):
            continue
        r1 = B.RANK.get(st.tag, -1) + (0.5 if sq in ('R_PT', 'R_def') else (0.3 if sq == 'R_OPE' else 0))
        r0 = B.RANK.get(rt, -1) + (0.5 if rq in ('R_PT', 'R_def') else (0.3 if rq == 'R_OPE' else 0))
        if st.tag is None or rt is None or 'V' in (st.tag, rt):
            sev, what = 'E', 'tag %s' % ('missing' if st.tag is None else ('added' if rt is None else 'changed'))
        elif r1 > r0:
            sev, what = 'E', 'strengthened (never allowed)'
        elif r1 < r0:
            sev, what = 'W', 'weakened (allowed with a justification in the report)'
        else:
            sev, what = 'W', 'qualifier changed'
        fmt = lambda t, q: (t or 'no tag') + ((', ' + q) if q else '')
        rp.add('K5', sev, st.unit, st.file, st.line, '%s: [%s] vs registry [%s] -- %s' % (l, fmt(st.tag, sq), fmt(rt, rq), what))
    # K6, K7, K8, K13, K14
    for l, st in S.items():
        if st.tag == 'R' and st.qual_problem:
            rp.add('K6', 'E', st.unit, st.file, st.line, '%s: %s' % (l, st.qual_problem))
        if st.tag == 'R' and st.qualifier == 'R_cond':
            if st.premise_status == 'none':
                rp.add('K7', 'E', st.unit, st.file, st.line, '%s: R_cond without the premise sentence 「前提：…」' % l)
            elif st.premise_status == 'late':
                rp.add('K7', 'E', st.unit, st.file, st.line, '%s: premise sentence not among the first two sentences' % l)
        if st.type != 'asm' and st.tag in ('A', 'P', 'C', 'V'):
            if not st.status_paragraph:
                rp.add('K8', 'E', st.unit, st.file, st.line, '%s [%s]: no 「地位与缺口」 paragraph' % (l, st.tag))
            elif st.status_where == 'late':
                rp.add('K8', 'W', st.unit, st.file, st.line, '%s [%s]: 「地位与缺口」 not immediately after the environment/proof'
                       % (l, st.tag))
        if st.type in B.NEEDS_USES and st.uses_count == 0 and not st.uses_none:
            rp.add('K13', 'E', st.unit, st.file, st.line, '%s: no \\uses and no "%% uses: none"' % l)
        if st.uses_count > 1:
            rp.add('K13', 'E', st.unit, st.file, st.line, '%s: %d \\uses lines' % (l, st.uses_count))
        bad = [p for p in st.uses if not B.is_stmt_label(p)]
        if bad:
            rp.add('K13', 'E', st.unit, st.file, st.line, '%s: non-statement labels in \\uses: %s' % (l, ', '.join(bad)))
        if st.type == 'asm':
            miss = [f for f in ('地位', '文献', '被使用于', '解除途径') if f not in (st.asm_fields or [])]
            if miss:
                rp.add('K14', 'W', st.unit, st.file, st.line, '%s: fields missing: %s' % (l, '、'.join(miss)))
    # K9, K10, K11, K12 (text scans)
    a_labels = set(l for l, st in S.items() if st.tag == 'A' and st.type != 'asm')
    a_labels |= set(l for l, i in R.info.items() if i['tag'] == 'A' and l not in S)
    for U in all_units:
        raw_lines = U.raw.split('\n')
        txt_lines = U.text.split('\n')
        # [A] regions: from an [A] environment to the next statement environment (env, proof, status paragraph)
        a_ranges = []
        ust = sorted(U.stmts, key=lambda s: s.line)
        for i, st in enumerate(ust):
            if st.tag == 'A' and st.type != 'asm':
                end = ust[i + 1].line - 1 if i + 1 < len(ust) else len(txt_lines)
                a_ranges.append((st.line, end, st.label))
        for ln, (raw, txt) in enumerate(zip(raw_lines, txt_lines), 1):
            com = raw[len(txt):] if len(raw) > len(txt) else ''
            for mk in MARKERS:
                if mk in txt:
                    if mk == '待核实' and '位置待核实' in txt:
                        continue
                    if mk == 'TODO' and re.search(r'TODO', txt) is None:
                        continue
                    rp.add('K9', 'E', U.uid, U.file, ln, 'printed planning marker 「%s」: %s' % (mk, txt.strip()[:80]))
                elif mk in com and mk != 'PENDING':
                    rp.add('K9', 'I', U.uid, U.file, ln, 'planning marker 「%s」 in a comment' % mk)
            for pat in REFDOC:
                if re.search(pat, txt, re.I):
                    rp.add('K11', 'E', U.uid, U.file, ln, 'mention of the reference document (%s): %s' % (pat, txt.strip()[:80]))
                elif re.search(pat, com, re.I):
                    rp.add('K11', 'W', U.uid, U.file, ln, 'mention of the reference document in a comment: %s' % com.strip()[:80])
            for ph in FORBIDDEN_A:
                for m in re.finditer(re.escape(ph), txt):
                    inA = [lab for (b, e, lab) in a_ranges if b <= ln <= e]
                    near = [x for x in B.labels_in(txt[max(0, m.start() - 60):m.end() + 60]) if x in a_labels]
                    if inA or near:
                        rp.add('K10', 'E', U.uid, U.file, ln, '「%s」 next to the [A] statement %s: %s' % (
                            ph, (inA or near)[0], txt[max(0, m.start() - 30):m.end() + 20].strip()))
                    else:
                        rp.add('K10', 'W', U.uid, U.file, ln, '「%s」 (justify: allowed only for [R]/[V] statements): %s' % (
                            ph, txt[max(0, m.start() - 30):m.end() + 20].strip()))
            for ph in C8B:
                for m in re.finditer(re.escape(ph), txt):
                    rp.add('K10', 'W', U.uid, U.file, ln, 'phrase 「%s」 to justify in context: %s' % (
                        ph, txt[max(0, m.start() - 30):m.end() + 20].strip()))
        for m in re.finditer(r'\\(cref|Cref|cpageref|Cpageref|labelcref|crefrange|Crefrange|uses)\*?\s*\{([^{}]*)\}', U.text):
            if re.search(r',\s|\s,|\n', m.group(2)) or (m.group(2) != m.group(2).strip()):
                rp.add('K12', 'E', U.uid, U.file, U.line(m.start()), '\\%s{%s}: spaces/line breaks in the label list (prints ??)'
                       % (m.group(1), re.sub(r'\s+', ' ', m.group(2))[:70]))
    # K15 citations
    keys = bib_keys(a.bib, a.chapters) if a.bib else None
    if keys is not None:
        for U in all_units:
            for (k, ln) in U.cites:
                if k.lower() not in keys:
                    rp.add('K15', 'E', U.uid, U.file, ln, 'citation key %s not in the bibliography (base + .bib-additions)' % k)
    # K16 figure delimiters
    for U in all_units:
        lines = U.raw.split('\n')
        openb = None
        for i, line in enumerate(lines, 1):
            m = re.match(r'^\s*(%{2,})\s*(BEGIN|END)\s+(fig:\S+)', line)
            if not m:
                continue
            if len(m.group(1)) != 3:
                rp.add('K16', 'W', U.uid, U.file, i, 'non-standard delimiter "%s %s %s"' % (m.group(1), m.group(2), m.group(3)))
            if m.group(2) == 'BEGIN':
                if openb:
                    rp.add('K16', 'W', U.uid, U.file, i, 'BEGIN %s inside the open block %s' % (m.group(3), openb))
                openb = m.group(3)
            else:
                if openb != m.group(3):
                    rp.add('K16', 'W', U.uid, U.file, i, 'END %s does not close %s' % (m.group(3), openb))
                openb = None
        if openb:
            rp.add('K16', 'W', U.uid, U.file, len(lines), 'block %s not closed' % openb)
    # ------------------------------------------------------------------ report
    out = []
    w = out.append
    w('check_book report -- %d unit file(s) in %s (+ %d other .tex: %s)' % (
        len(bk.units), a.chapters, len(aux), ', '.join(U.file for U in aux) or '-'))
    w('units present: %s' % ' '.join(bk.present))
    w('units missing: %s' % ' '.join(u for u in B.UNITS if u not in present))
    tot = collections.Counter(sev for (k, sev, u, f, ln, msg) in rp.items)
    w('findings: E %d, W %d, I %d' % (tot['E'], tot['W'], tot['I']))
    w('')
    w('== per check')
    for k, desc in CHECKS.items():
        c = collections.Counter(sev for (kk, sev, u, f, ln, msg) in rp.items if kk == k)
        w('%-4s E %4d  W %4d  I %4d   %s' % (k, c['E'], c['W'], c['I'], desc))
    w('')
    w('== per unit')
    w('%-6s %-24s %6s %5s %-40s %-22s %6s %5s %5s %5s' % ('unit', 'file', 'lines', 'stmts', 'types (def/asm/thm/lem/prop/cor/conj/ex/rem)',
                                                        'tags R/A/P/C/V', 'canon', 'miss', 'E', 'W'))
    for U in bk.units:
        c = collections.Counter(st.type for st in U.stmts)
        t = collections.Counter(st.tag for st in U.stmts if st.type != 'asm')
        rows = [r for r in R.rows if r[0] == U.uid and r[1] not in B.GENERATED_LABELS]
        miss = sum(1 for r in rows if r[1] not in defined)
        e = sum(1 for x in rp.items if x[2] == U.uid and x[1] == 'E')
        wn = sum(1 for x in rp.items if x[2] == U.uid and x[1] == 'W')
        types = '/'.join(str(c[p]) for p in ('def', 'asm', 'thm', 'lem', 'prop', 'cor', 'conj', 'ex', 'rem'))
        tags = '/'.join(str(t[x]) for x in 'RAPCV')
        w('%-6s %-24s %6d %5d %-40s %-22s %6d %5d %5d %5d' % (U.uid, U.file, U.raw.count('\n') + 1, len(U.stmts), types, tags,
                                                            len(rows), miss, e, wn))
    w('')
    w('== findings (by check, then unit; at most %d per check and unit)' % a.max)
    for k in CHECKS:
        items = sorted([x for x in rp.items if x[0] == k], key=lambda x: (B.UNIT_INDEX.get(x[2], 99), x[2], x[4], x[1]))
        if not items:
            continue
        w('-- %s %s (%d)' % (k, CHECKS[k], len(items)))
        per = collections.Counter()
        for (kk, sev, u, f, ln, msg) in items:
            per[u] += 1
            if per[u] > a.max:
                if per[u] == a.max + 1:
                    w('   ... more findings for %s omitted' % u)
                continue
            w('  [%s] %s:%s  %s' % (sev, f, ln if ln else '-', msg))
    txt = '\n'.join(out) + '\n'
    if a.out:
        os.makedirs(os.path.dirname(os.path.abspath(a.out)), exist_ok=True)
        with open(a.out, 'w', encoding='utf-8') as fh:
            fh.write(txt)
    sys.stdout.write('\n'.join(out[:30]) + '\n' + ('(full report: %s)\n' % a.out if a.out else ''))


if __name__ == '__main__':
    main()
