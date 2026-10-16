r"""booklib -- shared data and parsers for the integration tools of the monograph
《QCD 因子化定理：严格证明、全阶论证与适用边界》 (ctexbook + XeLaTeX).

Python 3 standard library only.  The tools import this module after inserting their own directory into
sys.path (they are run with `python3 -I`, which does not put the script directory on sys.path).

Contents
  * the unit table of WRITER_SPEC_v2 §1.1 (unit ids front, Ch01..Ch25, AppA..AppQ; keys; file names; parts);
  * constants of WRITER_SPEC_v2 §4 (environments, tags, the four verbatim qualifier sentences, global
    assumptions, OPE premises, named gaps) and of FINAL_OUTLINE_v2 App P (generated labels);
  * a LaTeX source parser for unit files (comment stripping with marker lines kept, statement environments
    with balanced optional titles, labels, references, \uses lists, qualifiers, premise sentences,
    non-perturbative lines, status paragraphs, sections, figure-block delimiters);
  * parsers for the label registry (FINAL_OUTLINE_v2 §08, format of checks/check_unit_v2.py), the master-table
    rows (§09), the withdrawn slot labels (§10), the assumption register (ASSUMPTIONS.md §1), the master
    driver's \input order and the hyperref .aux file;
  * the grade machinery of WRITER_SPEC_v2 §4.6 / FINAL_OUTLINE_v2 def:appP-content-grade (content grades,
    technical/global assumption closures, bottlenecks).
"""
import os, re, sys, json, bisect, hashlib, collections

LIB_VERSION = '1.0'

# --------------------------------------------------------------------------------------------- units
# (unit id, key, file, part)   part: 1..7 numbered parts, 'S' = summary (after Part VII), 'A' = appendix,
# None = front matter.  WRITER_SPEC_v2 §1.1 (binding) and FINAL_OUTLINE_v2 §0.1.
UNIT_TABLE = [
    ('front', None, 'front.tex', None),
    ('Ch01', 'intro', 'ch01_intro.tex', 1), ('Ch02', 'qcd', 'ch02_qcd.tex', 1),
    ('Ch03', 'prelim', 'ch03_prelim.tex', 1), ('Ch04', 'ir', 'ch04_ir.tex', 1),
    ('Ch05', 'sudakov', 'ch05_sudakov.tex', 1),
    ('Ch06', 'ee', 'ch06_ee.tex', 2), ('Ch07', 'dis', 'ch07_dis.tex', 2), ('Ch08', 'pdf', 'ch08_pdf.tex', 2),
    ('Ch09', 'method', 'ch09_method.tex', 3), ('Ch10', 'disall', 'ch10_disall.tex', 3),
    ('Ch11', 'coll', 'ch11_coll.tex', 3), ('Ch12', 'dy', 'ch12_dy.tex', 3), ('Ch13', 'thr', 'ch13_thr.tex', 3),
    ('Ch14', 'tmd', 'ch14_tmd.tex', 4), ('Ch15', 'scet', 'ch15_scet.tex', 4), ('Ch16', 'jets', 'ch16_jets.tex', 4),
    ('Ch17', 'smallx', 'ch17_smallx.tex', 4), ('Ch18', 'break', 'ch18_break.tex', 4),
    ('Ch19', 'excl', 'ch19_excl.tex', 5), ('Ch20', 'heavy', 'ch20_heavy.tex', 5),
    ('Ch21', 'power', 'ch21_power.tex', 6),
    ('Ch22', 'lamet', 'ch22_lamet.tex', 7), ('Ch23', 'yzliu', 'ch23_yzliu.tex', 7), ('Ch24', 'front', 'ch24_front.tex', 7),
    ('Ch25', 'summary', 'ch25_summary.tex', 'S'),
    ('AppA', 'appA', 'appA_lightfront.tex', 'A'), ('AppB', 'appB', 'appB_wilson.tex', 'A'),
    ('AppC', 'appC', 'appC_dimreg.tex', 'A'), ('AppD', 'appD', 'appD_landau.tex', 'A'),
    ('AppE', 'appE', 'appE_powercount.tex', 'A'), ('AppF', 'appF', 'appF_ward.tex', 'A'),
    ('AppG', 'appG', 'appG_oneloop.tex', 'A'), ('AppH', 'appH', 'appH_literature.tex', 'A'),
    ('AppI', 'appI', 'appI_gamma5.tex', 'A'), ('AppJ', 'appJ', 'appJ_brst.tex', 'A'),
    ('AppK', 'appK', 'appK_moments.tex', 'A'), ('AppL', 'appL', 'appL_lightray.tex', 'A'),
    ('AppM', 'appM', 'appM_ope.tex', 'A'), ('AppN', 'appN', 'appN_subtraction.tex', 'A'),
    ('AppO', 'appO', 'appO_glauber.tex', 'A'), ('AppP', 'appP', 'appP_blueprint.tex', 'A'),
    ('AppQ', 'appQ', 'appQ_errata.tex', 'A'),
]
UNITS = [u[0] for u in UNIT_TABLE]
UNIT_INDEX = {u: i for i, u in enumerate(UNITS)}
UNIT_KEY = {u[0]: u[1] for u in UNIT_TABLE}
UNIT_FILE = {u[0]: u[2] for u in UNIT_TABLE}
UNIT_PART = {u[0]: u[3] for u in UNIT_TABLE}
FILE_UNIT = {u[2]: u[0] for u in UNIT_TABLE}
# part prefaces written by unit writers (not units; no statements, no labels): input right after the part divider
PART_PREFACE_FILES = {7: ['part7_preface.tex']}
AUX_FILES = set(f for v in PART_PREFACE_FILES.values() for f in v)
PART_TITLE = {1: '基础', 2: '严格核心', 3: '共线因子化', 4: '共线之外', 5: '其他硬过程', 6: '极限', 7: '前沿进展'}
PART_FIRST = {1: 'Ch01', 2: 'Ch06', 3: 'Ch09', 4: 'Ch14', 5: 'Ch19', 6: 'Ch21', 7: 'Ch22'}
CN_NUM = {1: '一', 2: '二', 3: '三', 4: '四', 5: '五', 6: '六', 7: '七'}
# chapter / appendix labels (WRITER_SPEC_v2 §1.2: \label{ch:<key>} / \label{app:<key>}); not registry rows
CHAPTER_LABEL = {}
for _u, _k, _f, _p in UNIT_TABLE:
    if _u.startswith('Ch'):
        CHAPTER_LABEL[_u] = 'ch:' + _k
    elif _u.startswith('App'):
        CHAPTER_LABEL[_u] = 'app:' + _k
# App P graph groups (FINAL_OUTLINE_v2 App P §P.2-P.6 and FIGURES_INDEX_v2 §4.9 rule 1)
GRAPH_GROUPS = collections.OrderedDict([
    ('b', ('第一部分（第~1--5~章）', ['Ch%02d' % i for i in range(1, 6)])),
    ('c', ('第二部分（第~6--8~章）', ['Ch06', 'Ch07', 'Ch08'])),
    ('d', ('第三部分（第~9--13~章）', ['Ch%02d' % i for i in range(9, 14)])),
    ('e', ('第四部分（第~14--18~章）', ['Ch%02d' % i for i in range(14, 19)])),
    ('f', ('第五、六部分（第~19--21~章）', ['Ch19', 'Ch20', 'Ch21'])),
    ('g', ('第七部分（第~22--24~章）', ['Ch22', 'Ch23', 'Ch24'])),
    ('h', ('附录~M--O', ['AppM', 'AppN', 'AppO'])),
])


def unit_name(u, tilde=True):
    """Printed unit name: 第~7~章 / 附录~N / 前言."""
    sp = '~' if tilde else ' '
    if u == 'front':
        return '前言'
    if u.startswith('Ch'):
        return '第%s%d%s章' % (sp, int(u[2:]), sp)
    if u.startswith('App'):
        return '附录%s%s' % (sp, u[3:])
    return u


def unit_short(u):
    """Short unit name for narrow table cells (Ch7, App N)."""
    if u.startswith('Ch'):
        return 'Ch%d' % int(u[2:])
    if u.startswith('App'):
        return 'App %s' % u[3:]
    return u


def is_chapter(u):
    return u is not None and u.startswith('Ch')


def is_appendix(u):
    return u is not None and u.startswith('App')


# --------------------------------------------------------------------------------------------- spec constants
STMT_ENV = collections.OrderedDict([
    ('definition', 'def'), ('assumption', 'asm'), ('theorem', 'thm'), ('lemma', 'lem'), ('proposition', 'prop'),
    ('corollary', 'cor'), ('conjecture', 'conj'), ('example', 'ex'), ('remark', 'rem')])
STMT_PFX = ('def', 'asm', 'thm', 'lem', 'prop', 'cor', 'conj', 'rem', 'ex')
TYPE_ZH = {'def': '定义', 'asm': '假设', 'thm': '定理', 'lem': '引理', 'prop': '命题', 'cor': '推论', 'conj': '猜想',
           'ex': '例', 'rem': '注'}
NEEDS_USES = ('def', 'asm', 'thm', 'lem', 'prop', 'cor', 'conj')
TAGS = ('R', 'A', 'P', 'C', 'V')
RANK = {'R': 4, 'A': 3, 'P': 2, 'C': 1, 'V': 0}
TAG_COLOUR = {'R': 'OliveGreen', 'A': 'RoyalBlue', 'P': 'BurntOrange', 'C': 'Plum', 'V': 'BrickRed'}
TAG_ZH = {'R': '严格', 'A': '全阶论证', 'P': '部分', 'C': '猜想', 'V': '破坏'}
QUALS = ('R_PT', 'R_def', 'R_OPE', 'R_cond')
# WRITER_SPEC_v2 §4.3 -- the verbatim first sentences (compared after normalize_ws)
QUAL_TEXT = collections.OrderedDict([
    ('R_PT', '（$R_{\\mathrm{PT}}$：在重整化微扰论中对红外正规化的部分子态严格。）'),
    ('R_def', '（$R_{\\mathrm{def}}$：由算符定义直接推出。）'),
    ('R_OPE', '（$R_{\\mathrm{OPE}}$：以 OPE 为前提而严格。QCD 中含夸克的微扰 OPE 是全阶论证（\\cref{thm:dis-ope}），'
              '严格证明只对标量理论与纯 Yang--Mills 的规范不变算符给出；对强子态还须非微扰 OPE（\\cref{asm:intro-np-ope}）。）'),
    ('R_OPE_short', '（$R_{\\mathrm{OPE}}$：以 OPE 为前提。）'),
    ('R_cond', '（$R_{\\mathrm{cond}}$：在所列编号假设之下证明完整；结论的地位不高于其中最弱的假设。）'),
])
QUAL_TEX = {'R_PT': '$R_{\\mathrm{PT}}$', 'R_def': '$R_{\\mathrm{def}}$', 'R_OPE': '$R_{\\mathrm{OPE}}$',
            'R_cond': '$R_{\\mathrm{cond}}$'}
QUAL_SHORT = {'R_PT': 'PT', 'R_def': 'def', 'R_OPE': 'OPE', 'R_cond': 'cond'}
GLOBAL_ASM = ('asm:intro-wightman', 'asm:intro-composite', 'asm:intro-np-ope', 'asm:intro-af-coeff',
              'asm:intro-growth', 'asm:intro-bridge')
# umbrella names (ASSUMPTIONS.md §2; np-ope is listed under MA0 in the status lines)
GLOBAL_MA = {'asm:intro-wightman': 'MA0', 'asm:intro-composite': 'MA0', 'asm:intro-np-ope': 'MA0',
             'asm:intro-af-coeff': 'MA4', 'asm:intro-growth': 'MA3', 'asm:intro-bridge': 'MA1+MA2'}
OPE_PREMISES = ('thm:dis-ope', 'prop:dis-ope-euclid', 'prop:dis-ope-gi', 'prop:dis-ope-forward')
# named gaps (WRITER_SPEC_v2 §4.6 item 6, MD1, LA-1): gap -> statement whose closure triggers the naming duty
NAMED_GAPS = {'asm:appN-brst-nonlocal': 'lem:method-ward-multi'}
# labels produced by blueprint_gen.py (never written by a unit)
GENERATED_LABELS = ('sec:appP-register', 'sec:appP-status', 'sec:appP-uses', 'sec:appP-graphs', 'sec:appP-checks',
                    'tab:appP-register', 'tab:appP-status', 'tab:appP-uses', 'tab:appP-checks',
                    'fig:appP-dependency') + tuple('fig:appP-dependency-' + g for g in 'bcdefgh')
GENERATED_FIGS = tuple(l for l in GENERATED_LABELS if l.startswith('fig:'))
# withdrawn slot labels (FINAL_OUTLINE_v2 §10 names the slots only by ID; the labels are those of the superseded
# draft OUTLINE_appMNOPQ.md).  read_withdrawn() re-derives the list from the two files when they are available.
WITHDRAWN_FALLBACK = {
    'X1a': 'prop:appO-eikonal-allorders', 'X1b': 'prop:appO-g4-complete', 'X1d': 'prop:appO-compatibility-g0',
    'X1e': 'prop:appO-c2-twoloop', 'X2b': 'thm:appN-oneloop', 'X2c': 'prop:appN-ladder-cs',
    'X3a': 'prop:appM-remainder-discharge', 'X3b': 'prop:appM-ope-qcd-scope', 'X3c': 'prop:appM-forward-oneloop-alln',
    'X3d': 'prop:appM-brst-ope-ym'}
ERRTYPES = ('E-S', 'E-P', 'E-F', 'E-N', 'E-Nphi', 'E-W')
ERRTYPE_TEX = {'E-S': 'E-S', 'E-P': 'E-P', 'E-F': 'E-F', 'E-N': 'E-N', 'E-Nphi': 'E-N$^\\varphi$', 'E-W': 'E-W'}

LABEL_TOKEN = re.compile(r'(?<![A-Za-z@])(?:def|asm|thm|lem|prop|cor|conj|rem|ex):[A-Za-z0-9][A-Za-z0-9\-_]*[A-Za-z0-9]')
ANY_LABEL_TOKEN = re.compile(r'(?<![A-Za-z@])(?:def|asm|thm|lem|prop|cor|conj|rem|ex|sec|fig|tab|eq|ch|app):'
                             r'[A-Za-z0-9][A-Za-z0-9\-_]*[A-Za-z0-9]')


def label_prefix(l):
    return l.split(':', 1)[0] if ':' in l else ''


def is_stmt_label(l):
    return label_prefix(l) in STMT_PFX


# --------------------------------------------------------------------------------------------- text utilities
def read_text(path):
    with open(path, encoding='utf-8', errors='replace') as f:
        return f.read().replace('\r\n', '\n').replace('\r', '\n')


def comment_start(line):
    """Index of the first '%' that starts a TeX comment (preceded by an even number of backslashes), or None."""
    i = line.find('%')
    while i >= 0:
        k = i - 1
        n = 0
        while k >= 0 and line[k] == '\\':
            n += 1
            k -= 1
        if n % 2 == 0:
            return i
        i = line.find('%', i + 1)
    return None


MARK_USES_NONE = re.compile(r'^\s*uses\s*:\s*none\b', re.I)
MARK_ERRTYPE = re.compile(r'^\s*errtype\s*:\s*(E-?(?:Nphi|N\$?\^?\\?varphi\$?|S|P|F|N|W))', re.I)
MARK_PENDING = re.compile(r'PENDING[- ]?VERIFY', re.I)
MARK_FIG = re.compile(r'^%*\s*(BEGIN|END)\s+(fig:[^\s%]+)')


def norm_errtype(s):
    s = s.replace('$', '').replace('\\varphi', 'phi').replace('^', '')
    s = s.upper().replace('E-NPHI', 'E-Nphi').replace('ENPHI', 'E-Nphi')
    if not s.startswith('E-'):
        s = 'E-' + s[1:] if s.startswith('E') else s
    return s if s in ERRTYPES else None


def strip_comments(text):
    """Remove %-comments line by line (line structure kept, so offsets map to the same line numbers).
    Returns (stripped_text, markers) with markers = [(offset_in_stripped, line, kind, value)] for the marker lines
    '% uses: none', '% errtype: E-..', pending-verification comments and '%%% BEGIN/END fig:..' delimiters."""
    out, markers = [], []
    off = 0
    for ln, line in enumerate(text.split('\n'), 1):
        c = comment_start(line)
        if c is None:
            keep = line
        else:
            keep, com = line[:c], line[c + 1:]
            pos = off + len(keep)
            if MARK_USES_NONE.match(com):
                markers.append((pos, ln, 'uses_none', ''))
            m = MARK_ERRTYPE.match(com)
            if m:
                markers.append((pos, ln, 'errtype', norm_errtype(m.group(1)) or m.group(1)))
            if MARK_PENDING.search(com):
                markers.append((pos, ln, 'pending', com.strip()[:120]))
            m = MARK_FIG.match(com)
            if m:
                markers.append((pos, ln, 'fig' + m.group(1).lower(), m.group(2)))
        out.append(keep)
        off += len(keep) + 1
    return '\n'.join(out), markers


def line_starts(text):
    st = [0]
    for m in re.finditer('\n', text):
        st.append(m.end())
    return st


def offset_line(starts, off):
    return bisect.bisect_right(starts, off)


def match_brace(s, i, open_c='{', close_c='}'):
    """s[i] == open_c; index of the matching close_c (backslash escapes skipped), or -1."""
    depth = 0
    n = len(s)
    j = i
    while j < n:
        c = s[j]
        if c == '\\':
            j += 2
            continue
        if c == open_c:
            depth += 1
        elif c == close_c:
            depth -= 1
            if depth == 0:
                return j
        j += 1
    return -1


def split_top(s, sep):
    """Split s at sep characters that are at brace depth 0 (and not escaped)."""
    parts, depth, cur, j, n = [], 0, [], 0, len(s)
    while j < n:
        c = s[j]
        if c == '\\' and j + 1 < n:
            cur.append(s[j:j + 2])
            j += 2
            continue
        if c == '{':
            depth += 1
        elif c == '}':
            depth -= 1
        if c == sep and depth == 0:
            parts.append(''.join(cur))
            cur = []
        else:
            cur.append(c)
        j += 1
    parts.append(''.join(cur))
    return parts


def find_top(s, target, start=0):
    """First index >= start of the string target at brace depth 0 (relative to start), or -1."""
    depth, j, n, L = 0, start, len(s), len(target)
    while j < n:
        c = s[j]
        if c == '\\':
            j += 2
            continue
        if c == '{':
            depth += 1
        elif c == '}':
            depth -= 1
        elif depth <= 0 and s.startswith(target, j):
            return j
        j += 1
    return -1


def parse_optarg(s, i, maxlen=1500):
    """s[i] == '['.  Parse an optional argument.  Returns (content, end, warn) where end is the index after the
    closing ']' and warn is None or a message.  Primary parse: balanced brackets and braces (FINAL_OUTLINE_v2
    App P rule 3).  LaTeX itself (amsthm \@ythm ...[#4]) ends the argument at the first ']' at brace depth 0;
    if the two differ, the title contains an unbraced ']' and LaTeX cuts it short -- reported as a warning."""
    n = len(s)
    # LaTeX semantics
    depth, j, latex_end = 0, i + 1, -1
    while j < n and j - i < maxlen:
        c = s[j]
        if c == '\\':
            j += 2
            continue
        if c == '{':
            depth += 1
        elif c == '}':
            depth -= 1
        elif c == ']' and depth == 0:
            latex_end = j
            break
        j += 1
    # balanced brackets
    dc, db, j, bal_end = 0, 0, i, -1
    while j < n and j - i < maxlen:
        c = s[j]
        if c == '\\':
            j += 2
            continue
        if c == '{':
            dc += 1
        elif c == '}':
            dc -= 1
            if dc < 0:
                break
        elif dc == 0:
            if c == '[':
                db += 1
            elif c == ']':
                db -= 1
                if db == 0:
                    bal_end = j
                    break
        if c == '\n' and j + 1 < n and s[j + 1] == '\n':
            break
        j += 1
    warn = None
    if bal_end >= 0:
        if latex_end >= 0 and latex_end != bal_end:
            warn = ('optional title contains an unbraced "]": LaTeX ends the title at the first "]" '
                    '(wrap nested brackets in braces)')
        return s[i + 1:bal_end], bal_end + 1, warn
    if latex_end >= 0:
        return s[i + 1:latex_end], latex_end + 1, 'optional title: brackets not balanced (LaTeX semantics used)'
    return '', i, 'optional title: no closing "]"'


CJK_CHAR = '\u3000-\u303f\u3400-\u4dbf\u4e00-\u9fff\uff00-\uffef'
_RE_CJK_SP = re.compile('(?<=[%s]) (?=[%s])' % (CJK_CHAR, CJK_CHAR))


def normalize_ws(s):
    """Normalisation for the verbatim comparison of qualifier sentences: en dash -> '--', whitespace runs ->
    one space, no space between two CJK characters (xeCJK prints them identically), trimmed."""
    s = s.replace('\u2013', '--')
    s = re.sub(r'\s+', ' ', s)
    s = _RE_CJK_SP.sub('', s)
    return s.strip()


QUAL_NORM = collections.OrderedDict((k, normalize_ws(v)) for k, v in QUAL_TEXT.items())
QUAL_DETECT = re.compile(r'R_\{?\s*(?:\\(?:mathrm|rm|textrm|text|mathsf)\s*\{?\s*)?(PT|def|OPE|cond)\b')

LABEL_RE = re.compile(r'\\label\s*(?:\[[^\]]*\])?\s*\{([^{}]+)\}')
REF_RE = re.compile(r'\\(cref|Cref|cpageref|Cpageref|labelcref|namecref|nameCref|ref|pageref|eqref|autoref|nameref|vref|'
                    r'crefrange|Crefrange|uses)\*?\s*\{([^{}]*)\}')
HYPERREF_RE = re.compile(r'\\hyperref\s*\[([^\]]*)\]')
CITE_RE = re.compile(r'\\(?:cite|citep|citet|citealp|citeauthor|citeyear|nocite)\*?\s*(?:\[[^\]]*\]\s*){0,2}\{([^{}]*)\}')
SECT_RE = re.compile(r'\\(chapter|section|subsection|subsubsection)(\*?)\s*(?:\[[^\]]*\])?\s*\{')
ENV_BEGIN_RE = re.compile(r'\\begin\s*\{(' + '|'.join(STMT_ENV) + r')\}')
TAGMAC_RE = re.compile(r'\\tag([RAPCV])(?![A-Za-z])')
USES_RE = re.compile(r'\\uses\s*\{')
PARTONIC_RE = re.compile(r'[（(]\s*本[^（）()。]{0,40}?(?:只涉及|不涉及强子|仅涉及)')
STATUS_HEAD_RE = re.compile(r'^\s*(?:\\noindent\s*)?(?:\\paragraph\*?\s*\{\s*地位与缺口\s*[：:。.]?\s*\}'
                            r'|\\textbf\s*\{\s*地位与缺口\s*[：:。.]?\s*\}|\{\s*\\bfseries\s*地位与缺口\s*[：:。.]?\s*\}'
                            r'|地位与缺口\s*[：:])')
STATUS_STOP_RE = re.compile(r'\\(?:paragraph|section|subsection|subsubsection|chapter)\b|\\begin\s*\{(?:'
                            + '|'.join(STMT_ENV) + r'|proof|proofsketch)\}')
ASM_STATUS_RE = re.compile(r'(?<!非微扰)地位\s*[：:]')


def labels_in(s):
    """Labels referenced by \\cref/\\ref/... and \\uses commands inside s (comma lists), in order."""
    out = []
    for m in REF_RE.finditer(s):
        for x in m.group(2).split(','):
            x = x.strip()
            if x:
                out.append(x)
    for m in HYPERREF_RE.finditer(s):
        x = m.group(1).strip()
        if x:
            out.append(x)
    return out


def dedupe(seq):
    return list(dict.fromkeys(seq))


def sentence_end(s, start=0):
    """Index just after the first '。' at brace depth 0 (a directly following '）' is included), or len(s)."""
    j = find_top(s, '。', start)
    if j < 0:
        return len(s)
    j += 1
    if j < len(s) and s[j] in '）)':
        j += 1
    return j


# --------------------------------------------------------------------------------------------- unit parser
class Stmt(object):
    """One statement environment (definition ... remark) of a unit file."""
    FIELDS = ('label', 'env', 'type', 'unit', 'file', 'line', 'end_line', 'offset', 'section', 'title', 'title_text',
              'tags', 'tag', 'qualifier', 'qual_verbatim', 'qual_short', 'qual_problem', 'premises', 'premise_status',
              'uses', 'uses_count', 'uses_none', 'np_line', 'np_labels', 'partonic', 'status_paragraph',
              'status_where', 'status_labels', 'errtype', 'pending', 'label_line_delta', 'title_warn',
              'asm_fields', 'asm_used_by', 'asm_status_text', 'asm_upgrade_text', 'proof', 'body_labels')

    def __init__(self, **kw):
        for f in self.FIELDS:
            setattr(self, f, kw.get(f))

    def as_dict(self):
        return {f: getattr(self, f) for f in self.FIELDS}


class UnitData(object):
    def __init__(self, uid, path):
        self.uid = uid
        self.path = path
        self.file = os.path.basename(path)
        self.raw = ''
        self.text = ''
        self.starts = [0]
        self.markers = []
        self.labels = []        # (label, offset, line)
        self.refs = []          # (label, cmd, offset, line)
        self.cites = []         # (key, line)
        self.sections = []      # (offset, line, kind, title, label)
        self.stmts = []         # Stmt
        self.unlabelled = []    # (env, line)
        self.chapter_label = None
        self.chapter_title = None
        self.figblocks = []     # (label, begin_line, end_line)

    def line(self, off):
        return offset_line(self.starts, off)


def _clean_inline(s, limit=None):
    s = re.sub(r'\s+', ' ', s).strip()
    if limit and len(s) > limit:
        s = s[:limit]
    return s


def _first_field_sentence(body, head_re):
    """Text of the field introduced by head_re (e.g. 「地位：」) up to the first '。' at depth 0."""
    m = head_re.search(body)
    if not m:
        return None
    a = m.end()
    e = sentence_end(body, a)
    stop = re.search(r'(?:文献|被使用于|解除途径|地位)\s*[：:]', body[a:e])
    if stop:
        e = a + stop.start()
    return _clean_inline(body[a:e])


def parse_unit(path, uid, raw=None):
    """Parse one unit file.  All positions refer to the comment-stripped text (same line numbers as the file)."""
    U = UnitData(uid, path)
    U.raw = raw if raw is not None else read_text(path)
    U.text, U.markers = strip_comments(U.raw)
    s = U.text
    U.starts = line_starts(s)
    # figure blocks (from the raw delimiter lines)
    open_blocks = {}
    for (pos, ln, kind, val) in U.markers:
        if kind == 'figbegin':
            open_blocks.setdefault(val, []).append(ln)
        elif kind == 'figend':
            if open_blocks.get(val):
                U.figblocks.append((val, open_blocks[val].pop(0), ln))
            else:
                U.figblocks.append((val, None, ln))
    for val, lns in open_blocks.items():
        for ln in lns:
            U.figblocks.append((val, ln, None))
    # sections
    for m in SECT_RE.finditer(s):
        b = m.end() - 1
        e = match_brace(s, b)
        if e < 0:
            continue
        title = s[b + 1:e]
        lab = None
        nxt = SECT_RE.search(s, e)
        lim = min(len(s), e + 400, nxt.start() if nxt else len(s))
        lm = LABEL_RE.search(s, e, lim)
        if lm and s.count('\n', e, lm.start()) <= 3:
            lab = lm.group(1).strip()
        U.sections.append((m.start(), U.line(m.start()), m.group(1) + m.group(2), _clean_inline(title), lab))
        if m.group(1) == 'chapter' and U.chapter_label is None:
            U.chapter_label, U.chapter_title = lab, _clean_inline(title)
    # labels, references, citations
    for m in LABEL_RE.finditer(s):
        U.labels.append((m.group(1).strip(), m.start(), U.line(m.start())))
    for m in REF_RE.finditer(s):
        for x in m.group(2).split(','):
            x = x.strip()
            if x:
                U.refs.append((x, m.group(1), m.start(), U.line(m.start())))
    for m in HYPERREF_RE.finditer(s):
        x = m.group(1).strip()
        if x:
            U.refs.append((x, 'hyperref', m.start(), U.line(m.start())))
    for m in CITE_RE.finditer(s):
        for x in m.group(1).split(','):
            x = x.strip()
            if x:
                U.cites.append((x, U.line(m.start())))
    # statement environments
    envs = []
    for m in ENV_BEGIN_RE.finditer(s):
        name = m.group(1)
        depth = 1
        end = None
        for mm in re.finditer(r'\\(begin|end)\s*\{' + name + r'\}', s[m.end():]):
            if mm.group(1) == 'begin':
                depth += 1
            else:
                depth -= 1
                if depth == 0:
                    end = (m.end() + mm.start(), m.end() + mm.end())
                    break
        if end is None:
            end = (len(s), len(s))
        envs.append((m.start(), m.end(), end[0], end[1], name))
    qual_long_seen = False
    for (b0, b1, e0, e1, name) in envs:
        # title
        j = b1
        while j < len(s) and s[j] in ' \t':
            j += 1
        if j < len(s) and s[j] == '\n':
            k = j + 1
            while k < len(s) and s[k] in ' \t':
                k += 1
            if k < len(s) and s[k] == '[':
                j = k
        title, twarn, body_start = None, None, b1
        if j < len(s) and s[j] == '[':
            title, body_start, twarn = parse_optarg(s, j)
        # mask nested statement environments
        body = s[body_start:e0]
        for (c0, c1, d0, d1, n2) in envs:
            if c0 > body_start and d1 <= e0 and (c0, d1) != (b0, e1):
                a, z = c0 - body_start, d1 - body_start
                body = body[:a] + ' ' * (z - a) + body[z:]
        lm = LABEL_RE.search(body)
        line0 = U.line(b0)
        if not lm:
            U.unlabelled.append((name, line0))
            continue
        label = lm.group(1).strip()
        tags = TAGMAC_RE.findall(title or '')
        tag = tags[0] if tags else None
        pfx = STMT_ENV[name]
        st = Stmt(label=label, env=name, type=pfx, unit=uid, file=U.file, line=line0, end_line=U.line(e0), offset=b0,
                  title=title, title_text=_clean_inline(TAGMAC_RE.sub('', title or '')).strip(), tags=tags, tag=tag,
                  title_warn=twarn, label_line_delta=U.line(body_start + lm.start()) - line0)
        # section
        sec = None
        for (so, sl, kind, stitle, slab) in U.sections:
            if so < b0 and kind in ('section', 'subsection', 'section*', 'subsection*'):
                sec = slab or stitle
        st.section = sec
        # markers inside the environment
        st.uses_none = any(k == 'uses_none' and b0 <= p <= e1 for (p, l, k, v) in U.markers)
        ets = [v for (p, l, k, v) in U.markers if k == 'errtype' and b0 <= p <= e1]
        st.errtype = ets[0] if ets else None
        st.pending = any(k == 'pending' and b0 <= p <= e1 for (p, l, k, v) in U.markers)
        # \uses
        uses, cnt = [], 0
        for um in USES_RE.finditer(body):
            ob = um.end() - 1
            cb = match_brace(body, ob)
            if cb < 0:
                continue
            cnt += 1
            for x in body[ob + 1:cb].split(','):
                x = x.strip()
                if x:
                    uses.append(x)
        st.uses, st.uses_count = dedupe(uses), cnt
        # text after the label (for the qualifier and premise sentence)
        rest = body[:lm.start()] + body[lm.end():] if not body[:lm.start()].strip() else body
        rest = rest.lstrip()
        while True:
            m2 = re.match(r'(?:\\label\s*\{[^{}]*\}|\\leavevmode|\\hfill|\\mbox\{\})\s*', rest)
            if not m2:
                break
            rest = rest[m2.end():]
        st.qualifier, st.qual_verbatim, st.qual_short, st.qual_problem = None, False, False, None
        st.premises, st.premise_status = [], None
        nrest = normalize_ws(rest[:900])
        found = None
        for k, q in QUAL_NORM.items():
            if nrest.startswith(q):
                found = k
                break
        head = rest[:260]
        dq = QUAL_DETECT.search(head)
        if found:
            st.qualifier = 'R_OPE' if found == 'R_OPE_short' else found
            st.qual_verbatim = True
            st.qual_short = (found == 'R_OPE_short')
            if found == 'R_OPE':
                qual_long_seen = True
            elif found == 'R_OPE_short' and not qual_long_seen:
                st.qual_problem = 'short R_OPE form before the first long form in this unit'
        elif dq and (head.lstrip().startswith('（') or head.lstrip().startswith('(')) and dq.start() < 40:
            st.qualifier = {'PT': 'R_PT', 'def': 'R_def', 'OPE': 'R_OPE', 'cond': 'R_cond'}[dq.group(1)]
            st.qual_problem = 'qualifier sentence not verbatim (WRITER_SPEC_v2 §4.3)'
        elif dq:
            st.qualifier = {'PT': 'R_PT', 'def': 'R_def', 'OPE': 'R_OPE', 'cond': 'R_cond'}[dq.group(1)]
            st.qual_problem = 'qualifier is not the first sentence of the body'
        if st.qualifier is not None and tag != 'R':
            # a qualifier-like sentence in a non-[R] statement (composite statements carry it in an item)
            if tag is None or not st.qual_verbatim:
                st.qualifier, st.qual_problem = None, None
            else:
                st.qual_problem = 'qualifier sentence in a statement tagged [%s]' % tag
        if tag == 'R' and st.qualifier is None:
            st.qual_problem = '[R] without a qualifier sentence'
        # premise sentence (R_cond)
        if st.qualifier == 'R_cond':
            p_idx = find_top(rest, '前提')
            while p_idx >= 0 and not re.match(r'前提\s*[：:]', rest[p_idx:]):
                p_idx = find_top(rest, '前提', p_idx + 2)
            if p_idx < 0:
                st.premise_status = 'none'
            else:
                e1s = sentence_end(rest, 0)
                e2s = sentence_end(rest, e1s)
                pre = rest[e1s:p_idx]
                st.premise_status = 'ok' if (p_idx < e2s and not pre.strip()) or p_idx < e1s else 'late'
                pe = sentence_end(rest, p_idx)
                st.premises = dedupe(x for x in labels_in(rest[p_idx:pe]))
        # 非微扰地位 line, partonic remark
        npm = re.search(r'非微扰地位\s*[：:]', body)
        st.np_line = bool(npm)
        st.np_labels = dedupe(labels_in(body[npm.end():sentence_end(body, npm.end())])) if npm else []
        st.partonic = bool(PARTONIC_RE.search(body))
        st.body_labels = dedupe(x for x in labels_in(body) if x != label)
        # assumption fields
        if pfx == 'asm':
            st.asm_fields = [f for f in ('地位', '文献', '被使用于', '解除途径')
                             if (ASM_STATUS_RE.search(body) if f == '地位' else re.search(f + r'\s*[：:]', body))]
            ub = re.search(r'被使用于\s*[：:]', body)
            if ub:
                ue = re.search(r'解除途径\s*[：:]', body[ub.end():])
                seg = body[ub.end():ub.end() + ue.start()] if ue else body[ub.end():]
                seg = USES_RE.split(seg)[0]
                st.asm_used_by = dedupe(LABEL_TOKEN.findall(seg))
            else:
                st.asm_used_by = None
            st.asm_status_text = _first_field_sentence(body, ASM_STATUS_RE)
            st.asm_upgrade_text = _first_field_sentence(body, re.compile(r'解除途径\s*[：:]'))
        # proof and status paragraph
        after = e1
        st.proof = None
        while True:            # consecutive proof / proofsketch environments (and floats placed in between)
            pm = re.match(r'\s*\\begin\s*\{(proof|proofsketch|table\*?|figure\*?)\}', s[after:after + 4000])
            if not pm:
                break
            pname = pm.group(1)
            depth = 1
            pstart = after + pm.end()
            pend = None
            for mm in re.finditer(r'\\(begin|end)\s*\{' + pname + r'\}', s[pstart:]):
                if mm.group(1) == 'begin':
                    depth += 1
                else:
                    depth -= 1
                    if depth == 0:
                        pend = pstart + mm.end()
                        break
            if pname in ('proof', 'proofsketch'):
                st.proof = pname if st.proof is None else st.proof + '+' + pname
            if not pend:
                break
            after = pend
        st.status_paragraph, st.status_where, st.status_labels = False, None, []
        tail = s[after:after + 12000]
        hm = STATUS_HEAD_RE.match(tail)
        where = None
        if hm:
            where, a = 'after', hm.end()
        else:
            lim = 3000
            for sm in STATUS_STOP_RE.finditer(tail, 0, 3000):
                if STATUS_HEAD_RE.match(tail[sm.start():]) or re.match(r'\\begin\s*\{(?:proof|proofsketch)\}', tail[sm.start():]):
                    continue
                lim = sm.start()
                break
            win = tail[:lim]
            k = win.find('地位与缺口')
            if k >= 0:
                where, a = 'late', k + len('地位与缺口')
            else:
                k = body.rfind('地位与缺口')
                if k >= 0:
                    where = 'inside'
                    seg = body[k:]
                    st.status_labels = dedupe(labels_in(seg))
        if where in ('after', 'late'):
            stop = STATUS_STOP_RE.search(tail, a)
            seg = tail[a:stop.start() if stop else min(len(tail), a + 8000)]
            st.status_labels = dedupe(labels_in(seg))
        st.status_paragraph = where is not None
        st.status_where = where
        U.stmts.append(st)
    return U


# --------------------------------------------------------------------------------------------- spec files
def parse_tag_cell(cell):
    """'[R, R_PT]' -> ('R','R_PT',False); '[A]' -> ('A',None,False); '(数学，无标签)' -> (None,None,True);
    '(no tag)', '—', '' -> (None,None,False)."""
    c = (cell or '').strip()
    m = re.match(r'\[\s*R\s*,\s*(R_PT|R_def|R_OPE|R_cond)\s*\]', c)
    if m:
        return 'R', m.group(1), False
    m = re.match(r'\[\s*([RAPCV])\s*\]', c)
    if m:
        return m.group(1), None, False
    if '数学' in c:
        return None, None, True
    return None, None, False


def md_cells(line):
    """Cells of a markdown table row; '|' inside $...$ or `...` does not split."""
    s = line.strip()
    if s.startswith('|'):
        s = s[1:]
    if s.endswith('|'):
        s = s[:-1]
    cells, cur, inmath, intick = [], [], False, False
    i = 0
    while i < len(s):
        c = s[i]
        if c == '\\' and i + 1 < len(s):
            cur.append(s[i:i + 2])
            i += 2
            continue
        if c == '$' and not intick:
            inmath = not inmath
        elif c == '`':
            intick = not intick
        if c == '|' and not inmath and not intick:
            cells.append(''.join(cur).strip())
            cur = []
        else:
            cur.append(c)
        i += 1
    cells.append(''.join(cur).strip())
    return cells


class Registry(object):
    """Label registry (FINAL_OUTLINE_v2 §08), assumption register table, master rows (§09), withdrawn labels."""

    def __init__(self):
        self.owner = {}          # label -> unit id
        self.rows = []           # (unit, label, type, tag, qual, math, title)
        self.info = {}           # label -> dict(unit, type, tag, qual, math, title)
        self.asm = collections.OrderedDict()   # label -> dict(owner, tag, title, content, status, users, upgrade)
        self.master = []         # dict(row, label, tag, qual, np, bottleneck_labels, bottleneck_text, star, source)
        self.withdrawn = {}      # slot -> label
        self.optional = set()    # optional labels named below the registry tables
        self.optional_owner = {} # optional label -> unit heading under which it is named
        self.unit_titles = {}    # unit -> Chinese title (§0.1)

    def tag_of(self, label):
        i = self.info.get(label)
        if i is None:
            return None, None, False
        return i['tag'], i['qual'], i['math']


OWNER_MAP = {'Ch1': 'Ch01', 'AppM': 'AppM'}


def norm_owner(o):
    o = o.strip().replace('`', '')
    m = re.match(r'^Ch\s*0?(\d+)$', o)
    if m:
        return 'Ch%02d' % int(m.group(1))
    m = re.match(r'^App\s*([A-Q])$', o)
    if m:
        return 'App' + m.group(1)
    return o


def read_outline(path):
    """Parse FINAL_OUTLINE_v2.md: registry (§08), assumption register table, master rows (§09), withdrawn slot ids
    (§10), unit titles (§0.1)."""
    R = Registry()
    text = read_text(path)
    lines = text.split('\n')
    cur, in08, in09, in01 = None, False, False, False
    for line in lines:
        if re.match(r'^#{1,2} ', line):
            in08 = bool(re.match(r'^#{1,2} 08\b', line))
            in09 = bool(re.match(r'^#{1,2} 09\b', line))
            cur = None
            continue
        if line.startswith('### 0.1 '):
            in01 = True
            continue
        if line.startswith('### ') and in01:
            in01 = False
        if in01 and line.startswith('|'):
            c = md_cells(line)
            if len(c) >= 5:
                f = c[3].strip('` ')
                if f in FILE_UNIT:
                    R.unit_titles[FILE_UNIT[f]] = c[4]
        if in08:
            m = re.match(r'^###\s+(Ch\d\d|App[A-Q]|front|Assumptions)\b', line)
            if m:
                cur = m.group(1)
                continue
            if line.startswith('### '):
                cur = None
                continue
            if line.startswith('Optional') and cur:
                for l in re.findall(r'`((?:fig|tab):[A-Za-z0-9\-]+)`', line):
                    R.optional.add(l)
                    R.optional_owner[l] = cur
            m = re.match(r'^\|\s*`((?:def|thm|lem|prop|cor|conj|rem|ex|asm|sec|fig|tab):[A-Za-z0-9\-_]+)`\s*\|', line)
            if m and cur:
                lab = m.group(1)
                cells = md_cells(line)
                if cur == 'Assumptions':
                    tag, q, math = parse_tag_cell(cells[2] if len(cells) > 2 else '')
                    R.asm[lab] = dict(owner=norm_owner(cells[1]) if len(cells) > 1 else None, tag=tag,
                                      title=cells[3] if len(cells) > 3 else '', content=cells[4] if len(cells) > 4 else '',
                                      status=cells[5] if len(cells) > 5 else '',
                                      users=re.findall(r'`([a-z]+:[A-Za-z0-9\-_]+)`', cells[6]) if len(cells) > 6 else [],
                                      upgrade=cells[7] if len(cells) > 7 else '', source='outline')
                else:
                    tag, q, math = parse_tag_cell(cells[2] if len(cells) > 2 else '')
                    typ = cells[1] if len(cells) > 1 else label_prefix(lab)
                    title = cells[3] if len(cells) > 3 else ''
                    R.owner[lab] = cur
                    R.rows.append((cur, lab, typ, tag, q, math, title))
                    R.info[lab] = dict(unit=cur, type=typ, tag=tag, qual=q, math=math, title=title)
        if in09 and line.startswith('|'):
            cells = md_cells(line)
            if len(cells) >= 8 and re.match(r'^[IV]+\.\d+', cells[0]):
                m = re.search(r'`([a-z]+:[A-Za-z0-9\-_]+)`', cells[5])
                if m:
                    tag, q, math = parse_tag_cell(cells[3])
                    R.master.append(dict(row=cells[0], label=m.group(1), tag=tag, qual=q, np=cells[4],
                                         bottleneck_labels=re.findall(r'`([a-z]+:[A-Za-z0-9\-_]+)`', cells[6]),
                                         bottleneck_text=cells[6], star=('★' in cells[-1]), source='outline'))
    # withdrawn slot labels
    m = re.search(r'The labels reserved for the slots ([^.]*?) are \*\*withdrawn\*\*', text)
    ids = re.findall(r'X\d[a-z]', m.group(1)) if m else list(WITHDRAWN_FALLBACK)
    draft = os.path.join(os.path.dirname(path), 'OUTLINE_appMNOPQ.md')
    found = {}
    if os.path.exists(draft):
        for mm in re.finditer(r'\[PENDING-VERIFY (X\d[a-z])\]\s*\S+\s*`([a-z]+:[A-Za-z0-9\-]+)`', read_text(draft)):
            found.setdefault(mm.group(1), mm.group(2))
    for i in ids:
        lab = found.get(i) or WITHDRAWN_FALLBACK.get(i)
        if lab:
            R.withdrawn[i] = lab
    return R


def read_register(path):
    """ASSUMPTIONS.md §1 summary table -> OrderedDict label -> dict(owner, tag, title, content, status, users,
    upgrade)."""
    out = collections.OrderedDict()
    if not path or not os.path.exists(path):
        return out
    on = False
    for line in read_text(path).split('\n'):
        if line.startswith('## '):
            on = line.startswith('## 1.')
            continue
        if on and line.startswith('| `asm:'):
            c = md_cells(line)
            lab = c[0].strip('` ')
            tag, q, math = parse_tag_cell(c[2] if len(c) > 2 else '')
            out[lab] = dict(owner=norm_owner(c[1]) if len(c) > 1 else None, tag=tag, title=c[3] if len(c) > 3 else '',
                            content=c[4] if len(c) > 4 else '', status=c[5] if len(c) > 5 else '',
                            users=re.findall(r'`([a-z]+:[A-Za-z0-9\-_]+)`', c[6]) if len(c) > 6 else [],
                            upgrade=c[7] if len(c) > 7 else '', source='register')
    return out


def parse_aux(path, _seen=None):
    """hyperref-form \\newlabel{<label>}{{<number>}{<page>}{<title>}{<anchor>}{}} -> dict label -> (number, page,
    title, anchor); '@cref' duplicates ignored; \\@input{...aux} files followed."""
    out = {}
    if not path or not os.path.exists(path):
        return out
    _seen = _seen or set()
    ap = os.path.abspath(path)
    if ap in _seen:
        return out
    _seen.add(ap)
    t = read_text(path)
    for m in re.finditer(r'\\newlabel\{', t):
        b = m.end() - 1
        e = match_brace(t, b)
        if e < 0:
            continue
        lab = t[b + 1:e]
        if lab.endswith('@cref'):
            continue
        if e + 1 >= len(t) or t[e + 1] != '{':
            continue
        e2 = match_brace(t, e + 1)
        if e2 < 0:
            continue
        inner = t[e + 2:e2]
        groups, j = [], 0
        while j < len(inner) and len(groups) < 5:
            if inner[j] == '{':
                k = match_brace(inner, j)
                if k < 0:
                    break
                groups.append(inner[j + 1:k])
                j = k + 1
            else:
                j += 1
        while len(groups) < 4:
            groups.append('')
        num = re.sub(r'\\relax\s*', '', groups[0]).strip()
        out[lab] = (num, groups[1].strip(), groups[2], groups[3])
    for m in re.finditer(r'\\@input\{([^}]+)\}', t):
        sub = os.path.join(os.path.dirname(path), m.group(1))
        out.update(parse_aux(sub, _seen))
    return out


def read_master_inputs(master_path, root=None):
    """Unit files in the order of the \\input/\\include commands of the master driver (comments ignored).
    Returns [(unit_id, absolute path, exists)] for files whose basename is a unit file of WRITER_SPEC_v2 §1.1."""
    root = root or os.path.dirname(os.path.abspath(master_path))
    txt, _ = strip_comments(read_text(master_path))
    out = []
    for m in re.finditer(r'\\(?:input|include)\s*\{([^}]+)\}', txt):
        rel = m.group(1).strip()
        p = rel if rel.endswith('.tex') else rel + '.tex'
        base = os.path.basename(p)
        if base not in FILE_UNIT:
            continue
        ap = p if os.path.isabs(p) else os.path.join(root, p)
        out.append((FILE_UNIT[base], os.path.abspath(ap), os.path.exists(ap)))
    return out


def find_unit_files(chapters_dir):
    """Unit files present in a chapters directory, in book order: [(unit id, path)]; plus unknown .tex files."""
    found, unknown = [], []
    if not os.path.isdir(chapters_dir):
        return found, unknown
    names = set(os.listdir(chapters_dir))
    for u in UNITS:
        if UNIT_FILE[u] in names:
            found.append((u, os.path.join(chapters_dir, UNIT_FILE[u])))
    for n in sorted(names):
        if n.endswith('.tex') and n not in FILE_UNIT:
            unknown.append(n)
    return found, unknown


# --------------------------------------------------------------------------------------------- book model
class Book(object):
    """All parsed units in book order, with the statement graph."""

    def __init__(self, units, registry=None, register=None):
        self.units = units                                 # [UnitData] in book order
        self.present = [U.uid for U in units]
        self.registry = registry or Registry()
        self.register = register or collections.OrderedDict()
        self.stmts = collections.OrderedDict()             # label -> Stmt (first definition, book order)
        self.dups = collections.defaultdict(list)          # label -> [(unit, file, line)] for every \label
        self.order = {}
        for U in units:
            for (lab, off, ln) in U.labels:
                self.dups[lab].append((U.uid, U.file, ln))
            for st in U.stmts:
                if st.label not in self.stmts:
                    self.stmts[st.label] = st
        for k, l in enumerate(self.stmts):
            self.order[l] = k
        self.users = collections.defaultdict(list)         # label -> direct users (via \uses), book order
        for l, st in self.stmts.items():
            for p in st.uses:
                self.users[p].append(l)
        self._content = {}
        self._clos = {}

    # -- unit of a label: the defining unit if defined, else the registry owner (for asm: also the register)
    def unit_of(self, label):
        st = self.stmts.get(label)
        if st is not None:
            return st.unit
        u = self.registry.owner.get(label) or self.registry.optional_owner.get(label)
        if u:
            return u
        for uu, cl in CHAPTER_LABEL.items():
            if cl == label:
                return uu
        a = self.register.get(label) or self.registry.asm.get(label)
        if a and a.get('owner'):
            return a['owner']
        if label_prefix(label) == 'asm':
            key = label.split(':', 1)[1].split('-')[0]
            for uu, kk in UNIT_KEY.items():
                if kk == key:
                    return uu
        return None

    def defined(self, label):
        return label in self.stmts

    def is_rcond(self, l):
        st = self.stmts.get(l)
        return st is not None and st.tag == 'R' and st.qualifier == 'R_cond'

    def asm_tag(self, l):
        st = self.stmts.get(l)
        if st is not None:
            return st.tag
        a = self.register.get(l) or self.registry.asm.get(l)
        return a['tag'] if a else None

    def tagq(self, l):
        """(tag, qualifier, from_registry) of a statement label (source if defined, registry otherwise)."""
        st = self.stmts.get(l)
        if st is not None:
            return st.tag, st.qualifier, False
        if label_prefix(l) == 'asm':
            return self.asm_tag(l), None, True
        t, q, m = self.registry.tag_of(l)
        return t, q, True

    # -- content grade (def:appP-content-grade)
    def content(self, l, _stack=None):
        if l in self._content:
            return self._content[l]
        _stack = _stack or set()
        st = self.stmts.get(l)
        if st is None:
            t, q, _ = self.tagq(l)
            if label_prefix(l) == 'asm':
                return 'R' if (l in GLOBAL_ASM or t is None) else t
            if t is None:
                return 'R'
            if t == 'R':
                return 'A' if q == 'R_OPE' else 'R'
            return t
        if l in _stack:
            return 'R'
        _stack = _stack | {l}
        if st.type == 'asm':
            g = 'R' if (l in GLOBAL_ASM or st.tag is None) else st.tag
        elif st.tag is None:
            g = 'R'
        elif st.tag == 'R':
            if st.qualifier == 'R_cond':
                # min over the premise sentence; [R]-tagged R_cond/R_OPE statements of \uses that are missing from it
                # are included as well (WRITER_SPEC_v2 §4.6 item 2: a user inherits the premises of an R_cond statement)
                g = 'R'
                for p in dedupe(list(st.premises) + [x for x in st.uses if label_prefix(x) != 'asm']):
                    if p in GLOBAL_ASM or not is_stmt_label(p):
                        continue
                    if label_prefix(p) == 'asm':
                        pt = self.asm_tag(p) or 'R'
                    else:
                        pst = self.stmts.get(p)
                        if pst is not None and pst.tag == 'R' and pst.qualifier == 'R_OPE':
                            pt = 'A'
                        else:
                            pt = self.content(p, _stack)
                    if pt != 'V' and RANK[pt] < RANK[g]:
                        g = pt
            elif st.qualifier == 'R_OPE':
                g = 'A'
            else:
                g = 'R'
        else:
            g = st.tag
        self._content[l] = g
        return g

    def followed(self, l):
        """Labels followed by the closures from l: the premise sentence for R_cond, \\uses otherwise."""
        st = self.stmts.get(l)
        if st is None:
            return []
        return st.premises if (st.tag == 'R' and st.qualifier == 'R_cond') else st.uses

    def closure(self, l, _stack=None):
        """(A, G, S, O): technical-assumption closure, global-assumption closure, statements reached, opaque OPE
        premises (for R_OPE statements the OPE premises are named premises and are not traversed)."""
        if l in self._clos:
            return self._clos[l]
        if _stack is None:
            _stack = set()
        A, G, S, O = set(), set(), set(), set()
        if l in _stack:              # dependency cycle (reported by C-P4): partial closure
            return A, G, S, O
        _stack.add(l)
        st = self.stmts.get(l)
        rope = st is not None and st.tag == 'R' and st.qualifier == 'R_OPE'
        for p in self.followed(l):
            if p in GLOBAL_ASM:
                G.add(p)
                continue
            if label_prefix(p) == 'asm':
                A.add(p)
                continue
            if rope and p in OPE_PREMISES:
                O.add(p)
                continue
            if p not in self.stmts:
                continue
            S.add(p)
            a, g, s2, o2 = self.closure(p, _stack)
            A |= a
            G |= g
            S |= s2
            O |= o2
        _stack.discard(l)
        res = (frozenset(A), frozenset(G), frozenset(S), frozenset(O))
        self._clos[l] = res
        return res

    def bottleneck(self, l):
        """B(S) (FINAL_OUTLINE_v2 App P data model): the technical assumptions of the closure with the minimal grade
        below [R]; statements of the closure whose own grade is below that of all their technical assumptions
        ('intrinsic', e.g. an assumption-free [P] statement, or an opaque OPE premise) compete on equal terms."""
        A, G, S, O = self.closure(l)
        ca, cs = {}, {}
        for a in A:
            c = 'R' if a in GLOBAL_ASM else (self.asm_tag(a) or 'R')
            if c != 'R' and c != 'V':
                ca[a] = c
        for p in sorted(S | O):
            cp = self.content(p)
            if cp in ('R', 'V'):
                continue
            if p in O:
                cs[p] = cp
                continue
            Ap = self.closure(p)[0]
            ga = [self.asm_tag(a) or 'R' for a in Ap if a not in GLOBAL_ASM]
            ga = [g for g in ga if g != 'V']
            if not ga or RANK[cp] < min(RANK[g] for g in ga):
                cs[p] = cp
        ma = min([RANK[c] for c in ca.values()] or [99])
        ms = min([RANK[c] for c in cs.values()] or [99])
        if ca and ma <= ms:
            pick = [x for x, c in ca.items() if RANK[c] == ma]
        elif cs:
            pick = [x for x, c in cs.items() if RANK[c] == ms]
        else:
            pick = []
        return sorted(pick, key=self.sort_key)

    def sort_key(self, l):
        """Book order for labels: defined ones by position, others by owner unit then name."""
        if l in self.order:
            st = self.stmts[l]
            return (UNIT_INDEX.get(st.unit, 99), 0, self.order[l], l)
        u = self.unit_of(l)
        return (UNIT_INDEX.get(u, 99) if u else 99, 1, 0, l)


def load_book(unit_paths, registry=None, register=None):
    units = []
    for uid, p in unit_paths:
        if os.path.exists(p):
            units.append(parse_unit(p, uid))
    units.sort(key=lambda U: UNIT_INDEX[U.uid])
    return Book(units, registry, register)


def sources_revision(paths):
    h = hashlib.sha1()
    for p in paths:
        if os.path.exists(p):
            h.update(os.path.basename(p).encode('utf-8'))
            with open(p, 'rb') as f:
                h.update(f.read())
    return h.hexdigest()[:10]


UNI_TEX = {'α': r'$\alpha$', 'β': r'$\beta$', 'γ': r'$\gamma$', 'δ': r'$\delta$', 'ε': r'$\varepsilon$', 'ζ': r'$\zeta$',
           'η': r'$\eta$', 'θ': r'$\theta$', 'κ': r'$\kappa$', 'λ': r'$\lambda$', 'μ': r'$\mu$', 'ν': r'$\nu$', 'π': r'$\pi$',
           'ρ': r'$\rho$', 'σ': r'$\sigma$', 'τ': r'$\tau$', 'φ': r'$\varphi$', 'χ': r'$\chi$', 'ψ': r'$\psi$', 'ω': r'$\omega$',
           'Γ': r'$\Gamma$', 'Δ': r'$\Delta$', 'Λ': r'$\Lambda$', 'Φ': r'$\Phi$', 'Ψ': r'$\Psi$', 'Ω': r'$\Omega$', 'Σ': r'$\Sigma$',
           '–': '--', '—': '---', '′': r"$'$", '×': r'$\times$', '≤': r'$\le$', '≥': r'$\ge$', '→': r'$\to$',
           '∞': r'$\infty$', '±': r'$\pm$', '·': r'$\cdot$', '∈': r'$\in$', '⇒': r'$\Rightarrow$', '≠': r'$\ne$'}


def tex_escape(s):
    """Escape plain text for LaTeX (used for prose fragments copied from markdown/spec files); Greek letters and a
    few symbols that the Latin Modern text fonts lack are written in math mode."""
    rep = {'\\': r'\textbackslash{}', '&': r'\&', '%': r'\%', '#': r'\#', '_': r'\_', '{': r'\{', '}': r'\}',
           '~': r'\textasciitilde{}', '^': r'\textasciicircum{}'}
    rep.update(UNI_TEX)
    return ''.join(rep.get(c, c) for c in s)


def tex_safe_fragment(s):
    """True if a LaTeX fragment copied from a unit file can be re-emitted inside a table cell."""
    if s is None:
        return False
    if s.count('$') % 2:
        return False
    depth = 0
    for i, c in enumerate(s):
        if c == '{' and (i == 0 or s[i - 1] != '\\'):
            depth += 1
        elif c == '}' and (i == 0 or s[i - 1] != '\\'):
            depth -= 1
            if depth < 0:
                return False
    if depth:
        return False
    if re.search(r'\\(?:begin|end|item|\\|par\b|footnote|label|section|caption)', s):
        return False
    if '&' in s.replace('\\&', ''):
        return False
    return True
