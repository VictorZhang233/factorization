r"""Writer QA script for spec v2 (WRITER_SPEC_v2 Sec. 9).  Run in your test directory:

    python3 -I check_unit_v2.py UNIT.tex UNITID [FINAL_OUTLINE_v2.md]

UNITID is the registry heading of your unit: Ch01 ... Ch25, AppA ... AppQ, or front.
The script reads the label registry of FINAL_OUTLINE_v2.md: headings '### ChNN' / '### AppX' / '### front' /
'### Assumptions', followed by table rows whose first cell is a backticked label.  The owner of a canonical label
is the unit under whose heading it is listed (NOT its prefix: moved labels keep their old key, WRITER_SPEC_v2 Sec. 5).

Checks (each prints OK or a list of problems):
 C1 canonical labels owned by this unit that are missing in the file;
 C2 labels defined in the file that the registry assigns to another unit;
 C3 external references (\cref, \ref, \uses) that are not canonical;
 C4 \uses lists: only statement labels (def thm lem prop cor conj rem ex asm); no sec/eq/fig/tab/ch/app;
    no label of a later chapter; no label defined later in the same file;
 C5 the statement labels \cref'd inside a statement environment and its proof that are missing from its \uses
    (to be justified as pointers in the report), and \uses entries never mentioned in the proof (informational);
 C6 every \tagR environment opens with exactly one of the four qualifier sentences; R_cond is followed by the
    premise sentence; every \tagA/\tagP/\tagC/\tagV environment is followed by a 地位与缺口 paragraph;
 C7 every def/asm/lem/prop/thm/cor/conj environment has a \uses{...} or the comment '% uses: none';
 C8 (a) printed planning markers ([PENDING-VERIFY], 待文献核查) -- must be absent (the comment '% PENDING-VERIFY: ...'
    of WRITER_SPEC_v2 Sec. 6.12 is allowed); (b) phrases that are over-claims unless qualified (Sec. 4.11, 6.9), each
    shown with its context: rephrase, or justify the occurrence in the report.
 (spec v2.1: C5 ignores the field 「被使用于：…」 of assumption environments, which lists reverse dependencies.)
"""
import re, sys

STMT = ('def', 'thm', 'lem', 'prop', 'cor', 'conj', 'rem', 'ex', 'asm')
ENV2PFX = {'definition': 'def', 'theorem': 'thm', 'lemma': 'lem', 'proposition': 'prop', 'corollary': 'cor',
           'conjecture': 'conj', 'remark': 'rem', 'example': 'ex', 'assumption': 'asm'}
ORDER = ['front'] + ['Ch%02d' % i for i in range(1, 26)] + ['App' + c for c in 'ABCDEFGHIJKLMNOPQ']
QUAL = {
    'R_PT': '（$R_{\\mathrm{PT}}$：在重整化微扰论中对红外正规化的部分子态严格。）',
    'R_def': '（$R_{\\mathrm{def}}$：由算符定义直接推出。）',
    'R_OPE_long': '（$R_{\\mathrm{OPE}}$：以 OPE 为前提而严格。QCD 中含夸克的微扰 OPE 是全阶论证（\\cref{thm:dis-ope}），严格证明只对标量理论与纯 Yang--Mills 的规范不变算符给出；对强子态还须非微扰 OPE（\\cref{asm:intro-np-ope}）。）',
    'R_OPE_short': '（$R_{\\mathrm{OPE}}$：以 OPE 为前提。）',
    'R_cond': '（$R_{\\mathrm{cond}}$：在所列编号假设之下证明完整；结论的地位不高于其中最弱的假设。）',
}
FORBIDDEN = ['严格证明了', '已被证明', '软因子等于 1', '格点检验了因子化', 'Glauber 胶子在单举截面中总是相消',
             '[PENDING-VERIFY]', '待文献核查', '偶极子公式对所有阶精确']

def main():
    fn, unit = sys.argv[1], sys.argv[2]
    outline = sys.argv[3] if len(sys.argv) > 3 else 'FINAL_OUTLINE_v2.md'
    t = open(fn, encoding='utf-8').read().replace('\u2013', '--')
    o = open(outline, encoding='utf-8').read()
    owner = {}
    cur = None
    for line in o.split('\n'):
        m = re.match(r'^###\s+(Ch\d\d|App[A-Q]|front|Assumptions)\b', line)
        if m:
            cur = m.group(1); continue
        if line.startswith('## ') or line.startswith('# '):
            cur = None if not line.startswith('## 08') else cur
        m = re.match(r'^\|\s*`((?:def|thm|lem|prop|cor|conj|rem|ex|asm|sec|fig|tab):[A-Za-z0-9\-]+)`', line)
        if m and cur:
            lab = m.group(1)
            if cur == 'Assumptions':
                key = re.match(r'asm:([A-Za-z0-9]+)-', lab)
                owner.setdefault(lab, 'asm-register')
            else:
                owner[lab] = cur
    canon = set(re.findall(r'`((?:def|thm|lem|prop|cor|conj|rem|ex|asm|sec|fig|tab):[A-Za-z0-9\-]+)`', o))
    labs = re.findall(r'\\label\{([^}]+)\}', t)
    labpos = {}
    for m in re.finditer(r'\\label\{([^}]+)\}', t):
        labpos.setdefault(m.group(1), m.start())
    mine = sorted(l for l, u in owner.items() if u == unit)
    print('C1 canonical labels of this unit missing:', [l for l in mine if l not in labpos and not l.startswith(('fig:', 'tab:'))] or 'OK')
    print('C1b canonical fig/tab labels of this unit missing:', [l for l in mine if l not in labpos and l.startswith(('fig:', 'tab:'))] or 'OK')
    wrong = sorted(l for l in labpos if owner.get(l) not in (None, unit, 'asm-register'))
    print('C2 labels defined here but owned by another unit:', ['%s (owner %s)' % (l, owner[l]) for l in wrong] or 'OK')
    refs = set()
    for m in re.finditer(r'\\(?:c?ref|Cref|cref\*|uses|eqref)\{([^}]+)\}', t):
        for r in m.group(1).split(','):
            refs.add(r.strip())
    ext = sorted(r for r in refs if r not in labpos)
    print('C3 external refs not canonical:', [r for r in ext if r not in canon] or 'OK')
    print('   external refs (list them in your report):', ext)
    uidx = ORDER.index(unit) if unit in ORDER else None
    probs = []
    for m in re.finditer(r'\\uses\{([^}]+)\}', t):
        for r in [x.strip() for x in m.group(1).split(',')]:
            pfx = r.split(':')[0]
            if pfx not in STMT:
                probs.append('%s: not a statement label' % r); continue
            if r in labpos and labpos[r] > m.start():
                probs.append('%s: defined later in this file (forward use)' % r)
            ou = owner.get(r)
            if ou in ORDER and uidx is not None and ou.startswith('Ch') and unit.startswith('Ch') and ORDER.index(ou) > uidx:
                probs.append('%s: label of a later chapter (%s)' % (r, ou))
    print('C4 \\uses problems:', probs or 'OK')
    # statement blocks
    envs = re.finditer(r'\\begin\{(definition|theorem|lemma|proposition|corollary|conjecture|remark|example|assumption)\}(\[[^\]]*(?:\[[^\]]*\][^\]]*)*\])?(.*?)\\end\{\1\}', t, re.S)
    c5, c6, c7 = [], [], []
    for m in envs:
        env, title, body = m.group(1), m.group(2) or '', m.group(3)
        lab = re.search(r'\\label\{([^}]+)\}', body)
        lab = lab.group(1) if lab else '(unlabelled %s at char %d)' % (env, m.start())
        after = t[m.end():m.end() + 6000]
        pm = re.match(r'\s*\\begin\{(proof|proofsketch)\}(.*?)\\end\{\1\}', after, re.S)
        proof = pm.group(2) if pm else ''
        uses = set()
        for u in re.findall(r'\\uses\{([^}]+)\}', body):
            uses |= set(x.strip() for x in u.split(','))
        crefd = set()
        body_noq = body
        for q in QUAL.values():
            body_noq = body_noq.replace(q, '')   # crefs inside the qualifier sentences are pointers
        if env == 'assumption' and '被使用于' in body_noq:
            # the field 「被使用于：…」 lists REVERSE dependencies (WRITER_SPEC_v2 Sec. 4.4 item 3): not part of \uses
            a = body_noq.index('被使用于')
            b = body_noq.find('解除途径', a)
            body_noq = body_noq[:a] + (body_noq[b:] if b >= 0 else '')
        for u in re.findall(r'\\c?ref\{([^}]+)\}', body_noq + proof):
            crefd |= set(x.strip() for x in u.split(',') if x.strip().split(':')[0] in STMT)
        crefd.discard(lab)
        miss = sorted(crefd - uses)
        if env in ('definition', 'theorem', 'lemma', 'proposition', 'corollary', 'conjecture', 'assumption'):
            if not uses and '% uses: none' not in body:
                c7.append(lab)
            if miss:
                c5.append('%s: cref\'d but not in \\uses: %s' % (lab, ', '.join(miss)))
        if '\\tagR' in title:
            first = re.sub(r'^\s*(\\label\{[^}]+\}\s*)*', '', body).lstrip()
            if not any(first.startswith(q) for q in QUAL.values()):
                c6.append('%s: [R] without a verbatim qualifier as first sentence' % lab)
            elif first.startswith(QUAL['R_cond']):
                rest = first[len(QUAL['R_cond']):].lstrip()
                if not rest.startswith('前提：'):
                    c6.append('%s: R_cond without the premise sentence 「前提：…」' % lab)
        if any(x in title for x in ('\\tagA', '\\tagP', '\\tagC', '\\tagV')):
            window = body[-1500:] + after[:4000]
            if '地位与缺口' not in window:
                c6.append('%s: no 地位与缺口 paragraph' % lab)
    print('C5 cref/uses mismatches (justify as pointers or fix):', c5 or 'OK')
    print('C6 tag/qualifier problems:', c6 or 'OK')
    print('C7 statements without \\uses or "% uses: none":', c7 or 'OK')
    markers = [w for w in ('[PENDING-VERIFY]', 'PENDING-VERIFY]', '待文献核查') if w in t.replace('% PENDING-VERIFY:', '')]
    hits = []
    for w in FORBIDDEN:
        if w in ('[PENDING-VERIFY]', '待文献核查'):
            continue
        for m in re.finditer(re.escape(w), t):
            hits.append('%s ... %s' % (w, t[max(0, m.start() - 25):m.end() + 15].replace('\n', ' ')))
    print('C8a printed planning markers (must be absent; the comment form % PENDING-VERIFY: is allowed):', markers or 'OK')
    print('C8b phrases to justify in context (WRITER_SPEC_v2 Sec. 4.11, 6.9):', hits or 'OK')

if __name__ == '__main__':
    main()
