"""Generate the TikZ block fig:summary-status-map (figset_D, prefix fd2).

Every dot is one row of tab:summary-master (FINAL_OUTLINE_v2 section 09).
Filled dot: the row's tag column ([R] for R_PT/R_def/R_OPE).
Hollow dot: an R_cond row, drawn at its content grade (WRITER_SPEC_v2 4.6:
global asm:intro-* premises do not lower the content grade).
The tags are re-read from FINAL_OUTLINE_v2.md and checked against the
level given here."""
import re, sys, os

outline = sys.argv[1]
out = sys.argv[2]

txt = open(outline, encoding='utf-8').read().split('\n')
tags = {}
for l in txt:
    m = re.match(r'^\| ((?:I|II|III|IV|V|VII)\.\d+) \|.*?\| (\[[^\]]*\]) \|', l)
    if m and m.group(1) not in tags:
        tags[m.group(1)] = m.group(2)

# (label, master-row id list text, [(level, kind, id), ...]);
# kind: f = filled (tag), h = hollow (R_cond at content grade)
ROWS = [
 (r'$e^+e^-$ 总截面', 'II.1--7',
  [('R','f','II.1'),('R','f','II.2'),('R','f','II.4'),('A','f','II.3'),('A','f','II.5'),
   ('C','f','II.6'),('C','f','II.7')]),
 (r'DIS 矩、OPE 与极化求和规则', 'II.8--15, 17--19, 28, 29；III.21--24',
  [('R','f','II.17'),('R','f','II.18'),('R','f','II.28'),('R','f','III.21'),
   ('R','h','II.12'),('R','h','II.13'),('R','h','II.14'),('R','h','II.15'),
   ('A','f','II.8'),('A','f','II.9'),('A','f','II.10'),('A','f','II.11'),('A','f','II.19'),
   ('A','h','II.29'),('C','f','III.23'),('V','f','III.22'),('V','f','III.24')]),
 (r'DIS $x$ 空间', 'II.16, 25；III.10--15；VII.30',
  [('R','f','II.25'),('R','f','III.14'),('R','h','II.16'),
   ('A','f','III.13'),('A','f','III.15'),('A','f','VII.30'),
   ('A','h','III.10'),('A','h','III.11'),('C','h','III.12')]),
 (r'SIA、SIDIS 与光生', 'III.16--19',
  [('A','f','III.16'),('A','f','III.17'),('A','f','III.18'),('C','f','III.19')]),
 (r'DY 与色单态末态', 'III.25--30, 33, 34',
  [('R','f','III.27'),('A','f','III.26'),('A','f','III.29'),('A','f','III.30'),('A','f','III.33'),
   ('A','h','III.25'),('P','f','III.28'),('V','f','III.34')]),
 (r'$pp\to$ 喷注/强子（有色末态）', 'III.31, 32；IV.24--26',
  [('C','f','III.31'),('C','f','III.32'),('C','f','IV.25'),('V','f','IV.24'),('V','f','IV.26')]),
 (r'阈值重新因子化', 'III.35--37',
  [('A','f','III.35'),('A','f','III.36'),('P','f','III.37')]),
 (r'TMD：DY、SIDIS、$e^+e^-$', 'IV.1--9；VII.48',
  [('R','f','IV.2'),('R','f','IV.6'),('A','f','IV.3'),('A','f','IV.4'),('A','f','IV.5'),
   ('A','f','IV.7'),('A','f','IV.8'),('A','h','IV.1'),('P','f','IV.9'),('C','f','VII.48')]),
 (r'TMD：$h_1h_2\to H_1H_2X$', 'IV.22, 23',
  [('A','h','IV.22'),('V','f','IV.23')]),
 (r'SCET、事件形状与喷注', 'IV.10--17；VII.23--25',
  [('R','f','IV.10'),('A','f','IV.11'),('A','f','IV.12'),('A','f','IV.13'),('A','f','IV.15'),
   ('A','f','VII.23'),('P','f','IV.14'),('P','f','IV.16'),('P','f','VII.24'),('C','f','IV.17'),
   ('V','f','VII.25')]),
 (r'小 $x$', 'IV.18--21；VII.31',
  [('A','f','IV.18'),('A','f','IV.20'),('P','f','IV.19'),('C','f','IV.21'),('V','f','VII.31')]),
 (r'衍射', 'III.20；IV.28, 29',
  [('A','f','IV.28'),('V','f','III.20'),('V','f','IV.29')]),
 (r'双部分子散射与多重相互作用', 'IV.27, 30--32；VII.22, 46',
  [('A','f','IV.30'),('A','f','VII.22'),('C','f','IV.31'),('C','f','IV.32'),('C','f','VII.46'),
   ('V','f','IV.27')]),
 (r'硬遍举过程', 'V.1--8',
  [('A','f','V.2'),('A','f','V.3'),('A','f','V.5'),('A','f','V.6'),('A','h','V.1'),
   ('P','f','V.4'),('P','f','V.8'),('V','f','V.7')]),
 (r'$B$ 介子衰变', 'V.9--13',
  [('A','f','V.9'),('A','f','V.10'),('A','f','V.13'),('P','f','V.11'),('V','f','V.12')]),
 (r'重夸克偶素（NRQCD）', 'V.14--16',
  [('A','f','V.14'),('A','f','V.16'),('C','f','V.15')]),
 (r'幂次修正、NLP 与重整化子', 'V.17--24, 26；VII.26, 47',
  [('R','f','V.21'),('A','f','V.17'),('A','f','VII.26'),('P','f','V.18'),('P','f','V.20'),
   ('P','f','V.22'),('P','f','V.23'),('P','f','V.26'),('C','f','V.19'),('C','f','V.24'),
   ('C','f','VII.47')]),
 (r'格点与 LaMET（共线）', 'VII.1--9, 16, 17, 33--38, 40--42',
  [('R','f','VII.1'),('R','f','VII.6'),('R','f','VII.7'),
   ('A','f','VII.2'),('A','f','VII.3'),('A','f','VII.16'),('A','f','VII.34'),('A','f','VII.35'),
   ('A','f','VII.38'),('A','h','VII.5'),('A','h','VII.33'),('P','f','VII.17'),
   ('C','f','VII.4'),('C','f','VII.36'),('C','f','VII.40'),('C','f','VII.41'),('C','f','VII.42'),
   ('C','h','VII.8'),('C','h','VII.9'),('V','f','VII.37')]),
 (r'准 TMD 与软函数', 'VII.10--15, 39',
  [('A','f','VII.10'),('A','f','VII.11'),('A','f','VII.12'),('A','f','VII.13'),('A','f','VII.14'),
   ('A','f','VII.15'),('C','f','VII.39')]),
 (r'Landau 理论、区域与 OPE', 'I.10--12, 22, 23；V.25；VII.18--21, 43--45',
  [('R','f','I.10'),('R','f','I.11'),('R','f','I.12'),('R','f','I.22'),('R','f','V.25'),
   ('A','f','VII.18'),('A','h','VII.19'),('P','f','I.23'),('C','f','VII.20'),('C','f','VII.45'),
   ('V','f','VII.21'),('V','f','VII.43'),('V','f','VII.44')]),
]
# content grades of the R_cond rows (master-table bottleneck column; global
# asm:intro-* premises are not counted, WRITER_SPEC_v2 4.6 item 1, MD4)
CONTENT = {'II.12':'R','II.13':'R','II.14':'R','II.15':'R','II.16':'R','II.29':'A',
           'III.10':'A','III.11':'A','III.12':'C','III.25':'A','IV.1':'A','IV.22':'A','V.1':'A',
           'VII.5':'A','VII.33':'A','VII.8':'C','VII.9':'C','VII.19':'A'}
# footnote letters of the hollow clusters
NOTE = {('DIS 矩、OPE 与极化求和规则','R'):'a', ('DIS $x$ 空间','R'):'a',
        ('格点与 LaMET（共线）','C'):'b', ('DIS $x$ 空间','C'):'c'}
NOTE_DEFAULT_A = None

LEV = ['R','A','P','C','V']
COL = {'R':'OliveGreen','A':'RoyalBlue','P':'BurntOrange','C':'Plum','V':'BrickRed'}
GROUP_END = [7, 13, 17]        # thicker separators after these rows (1-based)

# ---- consistency checks against the outline ----
seen = set(); errs = 0
for name, ids, marks in ROWS:
    for lev, kind, rid in marks:
        if rid in seen:
            print('duplicate', rid); errs += 1
        seen.add(rid)
        t = tags.get(rid)
        if t is None:
            print('unknown row', rid); errs += 1; continue
        if kind == 'f':
            want = 'R' if t.startswith('[R') else t[1]
            if 'R_cond' in t:
                print('R_cond row drawn filled', rid); errs += 1
            if want != lev:
                print('tag mismatch', rid, t, lev); errs += 1
        else:
            if 'R_cond' not in t:
                print('hollow but not R_cond', rid, t); errs += 1
            if CONTENT[rid] != lev:
                print('content mismatch', rid, lev); errs += 1
allrows = set(tags)
print('drawn:', len(seen), 'of', len(allrows))
print('not drawn:', ' '.join(sorted(allrows - seen, key=lambda s: (s.split('.')[0], int(s.split('.')[1])))))
if errs:
    sys.exit('ERRORS: %d' % errs)

# ---- geometry (cm) ----
LW = 4.55           # label column (figure checker: 4.45 -> 4.55, the longest id string touched the rule)
CW = 2.28           # level column width (2.3 -> 2.28: total width unchanged, 15.95 cm)
RH = 0.72           # row height
R0 = 0.17           # first dot offset in a cell (figure checker: 0.21 -> 0.17)
DS = 0.222          # dot spacing (figure checker: 0.228 -> 0.222 so that the (a) note clears the column rule)
DR = 0.088          # dot radius
N = len(ROWS)
X0 = LW
W = LW + 5*CW
L = []
a = L.append
a(r'%%% BEGIN fig:summary-status-map')
a(r'\begin{figure}[htbp]')
a(r'\centering')
a(r'\begin{tikzpicture}[fd,x=1cm,y=1cm,')
a(r'  fd2 dot/.style={circle,fill=#1,draw=#1!70!black,line width=0.4pt,inner sep=0pt,minimum size=%.3fcm},' % (2*DR))
a(r'  fd2 hol/.style={circle,fill=white,draw=#1,line width=0.85pt,inner sep=0pt,minimum size=%.3fcm},' % (2*DR-0.01))
a(r'  fd2 row/.style={font=\footnotesize,anchor=west,inner sep=0pt},')
a(r'  fd2 ids/.style={font=\tiny,anchor=west,inner sep=0pt,text=gray!45!black},')
a(r'  fd2 fn/.style={font=\tiny,anchor=west,inner sep=0.5pt}]')
top = 0.0
# zebra background
for i in range(N):
    y1 = top - i*RH; y0 = y1 - RH
    if i % 2 == 1:
        a(r'  \fill[gray!7] (0,%.3f) rectangle (%.3f,%.3f);' % (y0, W, y1))
# column header
hy = top + 0.42
heads = {'R':r'\tagR','A':r'\tagA','P':r'\tagP','C':r'\tagC','V':r'\tagV'}
for j, lev in enumerate(LEV):
    a(r'  \node[inner sep=0pt] at (%.3f,%.3f) {%s};' % (X0 + (j+0.5)*CW, hy, heads[lev]))
a(r'  \node[font=\footnotesize\bfseries,anchor=west,inner sep=0pt] at (0,%.3f) {过程类};' % hy)
# horizontal rules
a(r'  \draw[gray!60,line width=0.6pt] (0,%.3f) -- (%.3f,%.3f);' % (top, W, top))
for g in GROUP_END:
    y = top - g*RH
    a(r'  \draw[gray!55,line width=0.6pt] (0,%.3f) -- (%.3f,%.3f);' % (y, W, y))
yb = top - N*RH
a(r'  \draw[gray!60,line width=0.6pt] (0,%.3f) -- (%.3f,%.3f);' % (yb, W, yb))
# vertical rules between level columns
for j in range(6):
    x = X0 + j*CW
    a(r'  \draw[gray!35,line width=0.4pt] (%.3f,%.3f) -- (%.3f,%.3f);' % (x, top+0.8 if j in (0,5) and False else top, x, yb))
# rows
for i, (name, ids, marks) in enumerate(ROWS):
    yc = top - (i+0.5)*RH
    a(r'  \node[fd2 row] at (0.06,%.3f) {%s};' % (yc+0.11, name))
    a(r'  \node[fd2 ids] at (0.06,%.3f) {%s};' % (yc-0.2, ids.replace(', ', ',\\,')))
    for lev in LEV:
        fs = [m for m in marks if m[0] == lev and m[1] == 'f']
        hs = [m for m in marks if m[0] == lev and m[1] == 'h']
        x = X0 + LEV.index(lev)*CW + R0
        for m in fs:
            a(r'  \node[fd2 dot=%s] at (%.3f,%.3f) {};  %% %s' % (COL[lev], x, yc, m[2])); x += DS
        if hs and fs: x += 0.06
        for m in hs:
            a(r'  \node[fd2 hol=%s] at (%.3f,%.3f) {};  %% %s' % (COL[lev], x, yc, m[2])); x += DS
        if hs:
            letter = NOTE.get((name, lev), NOTE_DEFAULT_A if lev == 'A' else '?')
            if letter:
                a(r'  \node[fd2 fn] at (%.3f,%.3f) {(%s)};' % (x - DS + DR + 0.03, yc + 0.09, letter))
# legend / notes
ly = yb - 0.42
a(r'  \node[fd2 dot=gray,anchor=center] at (0.15,%.3f) {};' % ly)
a(r'  \node[font=\footnotesize,anchor=west,inner sep=0pt] at (0.32,%.3f) {表~\ref{tab:summary-master} 中的一条陈述，画在其规范标签所在列（$R_{\mathrm{PT}}$、$R_{\mathrm{def}}$、$R_{\mathrm{OPE}}$ 均在 [R] 列）；颜色同标签};' % ly)
ly -= 0.42
a(r'  \node[fd2 hol=darkgray,anchor=center] at (0.15,%.3f) {};' % ly)
a(r'  \node[font=\footnotesize,anchor=west,inner sep=0pt] at (0.32,%.3f) {条件定理 $[\mathrm R,R_{\mathrm{cond}}]$，画在其内容等级所在列（全局假设 \texttt{asm:intro-*} 不降低内容等级）};' % ly)
ly -= 0.45
a(r'  \node[font=\footnotesize,anchor=north west,inner sep=0pt,align=left,text width=%.2fcm] at (0.06,%.3f) {%s};' % (W-0.1, ly+0.1,
  r'[A] 列中的空心圆：部分子层次的条件定理，前提为 [A] 级技术假设（\texttt{asm:appM-*}、\texttt{asm:appN-*}、\texttt{asm:appO-*}、\cref{asm:lamet-ope}）或 [A] 级定理。'
  r'(a)~前提只含全局非微扰假设，II.14、II.15 的瓶颈为 \cref{asm:intro-np-ope,asm:intro-growth}；\ '
  r'(b)~强子层次，瓶颈为 [C] 级假设：VII.8 为 \cref{asm:lamet-uniform,asm:lamet-twist4,asm:lamet-large-z}，VII.9 为 \cref{asm:lamet-gap}；\ '
  r'(c)~部分子层次的正规子路线，内容等级经由 \cref{asm:appN-ir-regulator} 为 [C]。'))
a(r'\end{tikzpicture}')
a(r'\caption{各类过程中因子化陈述的地位一览（与表~\ref{tab:summary-master} 一致）。每个圆点代表该表的一行：实心圆画在其规范标签所在的列，空心圆为条件定理 $[\mathrm R,R_{\mathrm{cond}}]$，画在其内容等级所在的列，[C] 列的空心圆是内容等级为 [C] 的条件定理（VII.8、VII.9 为强子层次的陈述），图下注明其瓶颈假设；左栏小字为归入该类的表行编号。'
  r'基础、方法与部分子分布性质的陈述（区块 I 的大部分、II.20--II.24、II.26、II.27、III.1--III.9、III.38）以及 VII.27--VII.29、VII.32 不属于某一过程类，未画出。'
  r'同一过程类往往同时含有不同等级的陈述：标签属于陈述，而不属于过程。}')
a(r'\label{fig:summary-status-map}')
a(r'\end{figure}')
a(r'%%% END fig:summary-status-map')
open(out, 'w', encoding='utf-8').write('\n'.join(L) + '\n')
print('written', out, 'dots:', len(seen))
