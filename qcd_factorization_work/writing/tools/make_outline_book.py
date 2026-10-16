#!/usr/bin/env python3
r"""Generate a SYNTHETIC full-size test book from spec_v2/FINAL_OUTLINE_v2.md (test fixture only; never written into
chapters/).  Every canonical statement of the outline becomes an environment with its title, tag, verbatim qualifier,
premise sentence (R_cond), 非微扰地位 line or partonic remark, `% errtype:` comment, \uses list and (for [A]/[P]/[C]/[V])
a 「地位与缺口」 paragraph naming the labels of the outline's status item; sections come from the registry;
ch25_summary.tex carries the master table (§09) as several table floats; front.tex carries tab:front-notation.
The statement bodies are placeholders.  Used to test the integration tools (make_master, blueprint_gen, build.sh)
at the real scale (~900 statements, 47 assumptions, 203 master rows).

    python3 -I make_outline_book.py --outline spec_v2/FINAL_OUTLINE_v2.md --out build/test_outline/chapters
            [--units Ch01,Ch07,...] [--omit Ch05,...]
"""
import os, re, sys, argparse, collections
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import booklib as B

HDR = re.compile(r'^(?P<ind>\s*)(?:[*-]|\d+\.)\s+\*\*(?P<pv>\[PENDING-VERIFY[^\]]*\]\s*)?(?P<type>定义|假设|定理|引理|命题|推论|猜想|注|例)\s+'
                 r'`(?P<label>(?:def|asm|thm|lem|prop|cor|conj|rem|ex):[A-Za-z0-9\-]+)`\s*—\s*(?P<title>.+?)\*\*(?P<rest>.*)$')
TAGRE = re.compile(r'\[(R, R_PT|R, R_def|R, R_OPE|R, R_cond|A|P|C|V|\\tag[RAPCV])\]')
LAB = re.compile(r'(?<![A-Za-z])(?:def|asm|thm|lem|prop|cor|conj|rem|ex):[A-Za-z0-9][A-Za-z0-9\-]*[A-Za-z0-9]')
ENV = {'def': 'definition', 'asm': 'assumption', 'thm': 'theorem', 'lem': 'lemma', 'prop': 'proposition',
       'cor': 'corollary', 'conj': 'conjecture', 'ex': 'example', 'rem': 'remark'}


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
    return None, None


def parse(text):
    """Statement entries of the outline (parser of spec_v2/checks/check_final_outline_v2.py, extended)."""
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
        s['uses_none'] = 'uses: none' in b
        pm = re.search(r'前提[：:]\s*(.*?)(?:。|$)', b, re.S)
        s['premise'] = list(dict.fromkeys(LAB.findall(pm.group(1)))) if pm else []
        np_ = [l for l in b.split('\n') if '非微扰地位' in l]
        s['np'] = list(dict.fromkeys(LAB.findall(np_[0]))) if np_ else []
        s['partonic'] = bool(re.search(r'只涉及部分子|不涉及强子|只涉及模型|只涉及算符', b))
        st = [l for l in b.split('\n') if ('地位与缺口' in l or 'Status and gap' in l or '*Status' in l)]
        s['status_labels'] = list(dict.fromkeys(x for l in st for x in LAB.findall(l)))
        em = re.search(r'(?:Error type|误差类型|errtype)[^\n]{0,40}?(E-(?:S|P|F|N|W))(\$\^\\varphi\$|phi)?', b)
        s['errtype'] = (em.group(1) + ('phi' if em.group(2) else '')) if em else None
        del s['body']
    return out


def clean_title(t):
    t = t.replace('`', '').replace('**', '').strip()
    t = re.sub(r'\s+', ' ', t)
    # unbalanced $ or braces would break the test build
    if t.count('$') % 2 or t.count('{') != t.count('}'):
        t = re.sub(r'[${}]', '', t)
    return t


def lab_cref(labels):
    return '、'.join('\\cref{%s}' % l for l in labels)


def main():
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument('--outline', required=True)
    ap.add_argument('--out', required=True)
    ap.add_argument('--units', default='')
    ap.add_argument('--omit', default='')
    a = ap.parse_args()
    text = B.read_text(a.outline)
    R = B.read_outline(a.outline)
    st = [s for s in parse(text) if not s['reserved']]
    by = collections.defaultdict(list)
    for s in st:
        by[s['unit']].append(s)
    want = [u for u in B.UNITS if (not a.units or u in a.units.split(',')) and u not in a.omit.split(',')]
    os.makedirs(a.out, exist_ok=True)
    secs = collections.defaultdict(list)
    for (u, l, typ, tag, q, math, title) in R.rows:
        if l.startswith('sec:') and l not in B.GENERATED_LABELS:
            secs[u].append(l)
    total = 0
    for u in want:
        L = []
        w = L.append
        w('%% SYNTHETIC TEST UNIT generated by writing/tools/make_outline_book.py from FINAL_OUTLINE_v2 -- not book text')
        title = clean_title(R.unit_titles.get(u, u))
        if u == 'front':
            w('\\chapter*{摘要}\\addcontentsline{toc}{chapter}{摘要}')
            w('本书为测试用的合成文本（由提纲自动生成）。')
            w('\\chapter*{记号与约定}\\addcontentsline{toc}{chapter}{记号与约定}')
            w('\\begin{table}[htbp]\\centering\\caption{记号（测试）}\\label{tab:front-notation}')
            w('\\begin{tabular}{ll}\\toprule 记号 & 含义\\\\\\midrule $v^\\pm$ & 光锥分量\\\\\\bottomrule\\end{tabular}\\end{table}')
            open(os.path.join(a.out, B.UNIT_FILE[u]), 'w', encoding='utf-8').write('\n'.join(L) + '\n')
            continue
        w('\\chapter{%s}\\label{%s}' % (title, B.CHAPTER_LABEL[u]))
        w('本单元为测试用的合成文本（由 FINAL\\_OUTLINE\\_v2 自动生成），陈述内容从略。')
        S = by.get(u, [])
        sl = secs.get(u, []) or ['sec:%s-synthetic' % B.UNIT_KEY[u]]
        per = max(1, -(-len(S) // len(sl)))
        ope_long = False
        for k, s in enumerate(S):
            if k % per == 0 and k // per < len(sl):
                w('')
                w('\\section{第 %d 节（测试）}\\label{%s}' % (k // per + 1, sl[k // per]))
            env = ENV[s['pfx']]
            tagm = (' \\tag%s' % s['tag']) if s['tag'] else ''
            if s['pfx'] == 'asm':
                ra = R.asm.get(s['label'])
                t = ra['tag'] if ra else None
                tagm = (' \\tag%s' % t) if t else ''
            w('')
            w('\\begin{%s}[%s%s]\\label{%s}' % (env, clean_title(s['title']), tagm, s['label']))
            if s['tag'] == 'R':
                q = s['qual'] or 'R_PT'
                if q == 'R_OPE':
                    w(B.QUAL_TEXT['R_OPE_short'] if ope_long else B.QUAL_TEXT['R_OPE'])
                    ope_long = True
                else:
                    w(B.QUAL_TEXT[q])
                if q == 'R_cond':
                    w('前提：%s。' % (lab_cref(s['premise']) if s['premise'] else '（提纲未列）'))
            w('（测试用合成陈述：内容从略。）')
            if s['np']:
                w('非微扰地位：%s。' % lab_cref(s['np']))
            elif s['partonic']:
                w('（本命题只涉及部分子态。）')
            if s['pfx'] == 'asm':
                ra = R.asm.get(s['label'], {})
                w('地位：测试状态句。')
                w('文献：测试。')
                if ra.get('users'):
                    w('被使用于：%s。' % lab_cref(ra['users']))
                w('解除途径：测试解除途径。')
            if s['errtype']:
                w('%% errtype: %s' % s['errtype'])
            if s['uses']:
                w('\\uses{%s}' % ', '.join(s['uses']))
            else:
                w('% uses: none')
            w('\\end{%s}' % env)
            if s['tag'] == 'A':
                w('\\begin{proofsketch}测试。\\end{proofsketch}')
            if s['tag'] in ('A', 'P', 'C', 'V') and s['pfx'] != 'asm':
                lab = [x for x in s['status_labels'] if x != s['label']]
                w('\\paragraph{地位与缺口}测试：%s。' % (('本陈述的地位由' + lab_cref(lab) + '决定') if lab else '见文献'))
            total += 1
        if u == 'Ch25':
            w('')
            rows = R.master
            chunk = 40
            for c0 in range(0, len(rows), chunk):
                part = rows[c0:c0 + chunk]
                first = (c0 == 0)
                w('\\begin{table}[htbp]\\centering\\scriptsize')
                w('\\caption{全书主要结论总表%s}\\label{tab:summary-master%s}' % ('' if first else '（续）', '' if first else '-%s' % 'bcdefghij'[c0 // chunk - 1]))
                w('\\begin{tabular}{@{}lllp{2.4cm}p{6cm}l@{}}\\toprule')
                w('\\# & 标签 & 非微扰 & 规范标签 & 瓶颈假设 & ★\\\\\\midrule')
                for r in part:
                    tg = '\\tag%s' % r['tag'] if r['tag'] else '—'
                    if r['qual']:
                        tg += ' %s' % B.QUAL_TEX[r['qual']]
                    labcell = ('\\texttt{\\detokenize{%s}}' % r['label']) if first else ('\\cref{%s}' % r['label'])
                    bn = lab_cref(r['bottleneck_labels']) if r['bottleneck_labels'] else '—'
                    npc = re.sub(r'[`$\\{}]', '', r['np'])[:20]
                    w('%s & %s & %s & %s & %s & %s\\\\' % (r['row'], tg, npc, labcell, bn, '★' if r['star'] else ''))
                w('\\bottomrule\\end{tabular}\\end{table}')
        open(os.path.join(a.out, B.UNIT_FILE[u]), 'w', encoding='utf-8').write('\n'.join(L) + '\n')
    print('units written: %d, statements: %d -> %s' % (len(want), total, a.out))


if __name__ == '__main__':
    main()
