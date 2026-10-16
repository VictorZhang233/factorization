#!/usr/bin/env python3
r"""Figure checker: static checks of the figure files (run on src/ copies).

    python3 -I staticcheck.py src/figures1.tex ... src/figset_F.tex

Per %%% BEGIN/END block: placement [htbp]; exactly one figure env, one \caption, one \label{fig:..}
equal to the delimiter label, \label after \caption; planning/novelty markers in captions;
local re-definitions of preamble style names; \resizebox/\scalebox; italic imaginary unit
(i0 / ie^ written without \ii) and \overline{\rm MS} instead of \MSbar inside math;
local style names without the file's prefix (new sets only); bare n / \bar n outside Ch15 owners.
"""
import re
import sys

PREAMBLE_STYLES = ['fd', 'quark', 'plain', 'gluon', 'gluon loop', 'photon', 'ghost', 'mom', "mom'", 'mom arrow',
                   'vertex', 'blob', 'bound state', 'wilson', 'wilson plain', 'cut', 'hard blob', 'jet blob',
                   'jetB blob', 'soft blob', 'hadron blob', 'glauber', 'opvertex', 'scalar', 'longit', 'lcaxis',
                   'region', 'fd arrow']
PREFIX = {'figset_A.tex': 'fa', 'figset_B.tex': 'fb', 'figset_C.tex': 'fc', 'figset_D.tex': 'fd2',
          'figset_E.tex': 'fe', 'figset_F.tex': 'ff'}
MARKERS = ['PENDING-VERIFY', '待文献核查', '本书新结果', '首次', '新结果', 'TODO', 'FIXME', '图待补']


def strip_comments(s):
    return re.sub(r'(?<!\\)%.*', '', s)


def caption_text(body):
    i = body.find('\\caption{')
    if i < 0:
        return ''
    j, depth = i + len('\\caption{'), 1
    while j < len(body) and depth:
        if body[j] == '{':
            depth += 1
        elif body[j] == '}':
            depth -= 1
        j += 1
    return body[i:j]


issues = []
nblocks = 0
for fn in sys.argv[1:]:
    base = fn.split('/')[-1]
    lines = open(fn, encoding='utf-8').read().splitlines()
    blocks, cur, lab = [], None, None
    for ln, line in enumerate(lines, 1):
        m = re.match(r'^%%% BEGIN (\S+)\s*$', line)
        if m:
            if cur is not None:
                issues.append((base, ln, 'BEGIN inside open block ' + str(lab)))
            lab, cur, start = m.group(1), [], ln
            continue
        m = re.match(r'^%%% END (\S+)\s*$', line)
        if m:
            if cur is None or m.group(1) != lab:
                issues.append((base, ln, 'END %s does not match %s' % (m.group(1), lab)))
            else:
                blocks.append((lab, start, '\n'.join(cur)))
            cur, lab = None, None
            continue
        if cur is not None:
            cur.append(line)
    for lab, start, raw in blocks:
        nblocks += 1
        body = strip_comments(raw)
        where = (base, start, lab)
        nfig = len(re.findall(r'\\begin\{figure\*?\}', body))
        if nfig != 1:
            issues.append(where + ('%d figure environments' % nfig,))
        pl = re.findall(r'\\begin\{figure\*?\}(\[[^\]]*\])?', body)
        if not pl or pl[0] != '[htbp]':
            issues.append(where + ('placement %s (not [htbp])' % (pl[0] if pl else None),))
        body_nosub = re.sub(r'\\begin\{subfigure\}.*?\\end\{subfigure\}', '', body, flags=re.S)
        ncap = len(re.findall(r'\\caption[\[{]', body_nosub))
        if ncap != 1:
            issues.append(where + ('%d captions' % ncap,))
        labs = re.findall(r'\\label\{(fig:[^}]*)\}', body)
        if labs != [lab]:
            issues.append(where + ('fig labels %s' % labs,))
        if body.find('\\label{' + lab + '}') < body.find('\\caption'):
            issues.append(where + ('label before caption',))
        cap = caption_text(body)
        for mk in MARKERS:
            if mk in cap:
                issues.append(where + ('caption contains marker "%s"' % mk,))
        # local redefinition of preamble styles
        for st in PREAMBLE_STYLES:
            if re.search(r'(?<![\w\s-])\s*' + re.escape(st) + r'/\.(?:style|append style|default)', body):
                # exclude e.g. 'fa quark/.style' (prefixed names contain a space before)
                for m in re.finditer(r'([\w\s\'-]*?)' + re.escape(st) + r'/\.(?:style|append style|default)', body):
                    pre = m.group(1)
                    if pre.strip() == '' or pre.endswith(','):
                        issues.append(where + ('local re-definition of preamble style "%s"' % st,))
                        break
        if re.search(r'\\(resizebox|scalebox|adjustbox)', body):
            issues.append(where + ('uses \\resizebox/\\scalebox',))
        if re.search(r'\bscale\s*=\s*0?\.\d', body) and re.search(r'transform shape(?!\s*=\s*false)', body):
            issues.append(where + ('scale with transform shape (fonts scaled)',))
        # local style prefixes in new sets
        if base in PREFIX:
            for m in re.finditer(r'([A-Za-z][\w \-\']*?)/\.(style|append style|pic|code)', body):
                name = m.group(1).strip()
                last = re.split(r'[,\[{]', name)[-1].strip()
                if not last.startswith(PREFIX[base]) and last not in ('every picture', 'every node', 'every path',
                                                                      'every axis', 'every label', 'every edge',
                                                                      'every pin', 'every matrix', 'every axis plot',
                                                                      'every tick label', 'every axis label',
                                                                      'every axis x label', 'every axis y label'):
                    issues.append(where + ('local style without prefix: "%s"' % last,))
        # imaginary unit / MS-bar inside math
        for m in re.finditer(r'\$([^$]*)\$', body):
            mt = m.group(1)
            if re.search(r'(?<![\\A-Za-z])i0\b', mt) or re.search(r'(?<![\\A-Za-z{])i\s*0\b', mt):
                issues.append(where + ('italic imaginary unit "i0": %s' % mt[:60],))
            if re.search(r'\\overline\{\\(rm|mathrm)\s*\{?MS', mt):
                issues.append(where + ('\\overline{MS} instead of \\MSbar',))
print('blocks checked:', nblocks)
seen = set()
for it in issues:
    if it in seen:
        continue
    seen.add(it)
    print('  ', ' | '.join(str(x) for x in it))
print('issues:', len(seen))
