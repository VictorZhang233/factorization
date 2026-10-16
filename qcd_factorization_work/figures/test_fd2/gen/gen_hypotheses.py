"""Generate the TikZ block fig:summary-hypotheses (figset_D, prefix fd2).

Three columns: register entries (global, App M, App N) | main [A] and
R_cond theorems | register entries (App O, frontier).  Edges: thin grey =
direct dependency (the assumption is in the theorem's \\uses list or premise
sentence, = the tick marks of tab:summary-assumptions); thick red = the
theorem's bottleneck assumptions (master-table bottleneck column, or, for
R_cond theorems, the premises of lowest grade), drawn also when the
dependency runs through a statement used by the theorem.  Indirect
dependencies that are not bottlenecks are omitted (App P has them)."""
import sys

out = sys.argv[1]

ASM_TAG = {
 'intro-wightman':'C','intro-composite':'C','intro-np-ope':'C','intro-af-coeff':'C','intro-growth':'C',
 'intro-bridge':'C',
 'appM-remainder':'A','appM-brst-ope':'A','appM-forward':'A',
 'appN-contour':'A','appN-envelope':'A','appN-separation':'A','appN-values':'-','appN-collins':'A',
 'appN-ward-product':'A','appN-brst-nonlocal':'C','appN-cutsum':'A','appN-uv':'A','appN-multren':'A',
 'appN-ir-regulator':'C','appN-tmd':'A','appN-endpoint':'A',
 'appO-lcopt':'A','appO-envelope':'A','appO-mixing':'A','appO-deformation':'A','appO-rewritten-cs':'A',
 'lamet-aux-renorm':'A','lamet-ope':'A','lamet-gap':'C','lamet-uniform':'C','lamet-twist4':'C',
 'lamet-large-z':'C','lamet-staple':'A','lamet-soft-rapidity':'A','lamet-order-limits':'A',
 'yzliu-heavy-pair':'C','yzliu-wightman-pt':'A','yzliu-lightcone-uniform':'P',
 'front-mor-complete':'C','front-scet-modes':'A'}
assert len(ASM_TAG) == 41

LEFT = [('减除法（附录~N）', ['appN-contour','appN-envelope','appN-separation','appN-values','appN-collins',
                       'appN-ward-product','appN-brst-nonlocal','appN-cutsum','appN-uv','appN-multren',
                       'appN-ir-regulator','appN-tmd','appN-endpoint']),
        ('全局非微扰假设', ['intro-wightman','intro-composite','intro-np-ope','intro-af-coeff','intro-growth','intro-bridge']),
        ('OPE（附录~M）', ['appM-remainder','appM-brst-ope','appM-forward'])]
RIGHT = [('Glauber（附录~O）', ['appO-lcopt','appO-envelope','appO-mixing','appO-deformation','appO-rewritten-cs']),
         ('LaMET（第~22~章）', ['lamet-aux-renorm','lamet-ope','lamet-gap','lamet-uniform','lamet-twist4',
                         'lamet-large-z','lamet-staple','lamet-soft-rapidity','lamet-order-limits']),
         ('Liu（第~23~章）', ['yzliu-heavy-pair','yzliu-wightman-pt','yzliu-lightcone-uniform']),
         ('其他前沿（第~24~章）', ['front-mor-complete','front-scet-modes'])]

# theorems: (short label, full label, tag, R_cond content grade or None)
MID = [('共线因子化', [('scet-thrust','thm','A',None),('heavy-bdpi','thm','A',None),('excl-dvcs','thm','A',None),
                  ('excl-pion-ff','thm','A',None),('disall-factorization','thm','A',None),('coll-sia','thm','A',None),
                  ('break-ddis','thm','A',None),('appN-structure','thm','R','C'),('disall-renorm-compat','thm','R','C')]),
       ('Glauber 区与 DY 型过程', [('tmd-factorization','thm','A',None),('appO-main','thm','R','A'),
                  ('dy-factorization','thm','A',None),('break-double-dy','thm','A',None)]),
       ('前沿', [('lamet-coordinate','thm','R','A'),('lattice-lamet','thm','A',None),('lamet-hadronic','thm','R','C'),
               ('lamet-exp-decay','thm','R','C'),('lamet-quasi-tmd','thm','A',None),('yzliu-soft-form-factor','cor','R','C'),
               ('yzliu-analyticity','thm','A',None),('yzliu-time-ordering','thm','A',None),
               ('yzliu-universality-classes','prop','P',None),('front-commuting','prop','R','C'),('front-hgg','thm','A',None)]),
       ('OPE 与非微扰矩', [('dis-ope','thm','A',None),('dis-moments-np','thm','R','R')])]

N7 = ['appN-collins','appN-envelope','appN-separation','appN-cutsum','appN-ward-product','appN-uv','appN-multren']
DY7 = ['appO-mixing','appO-deformation','appO-rewritten-cs','appO-lcopt','appO-envelope','appN-collins','appN-cutsum']
E = {}   # theorem -> list of (asm, kind) kind d = direct grey, b = bottleneck red
def add(t, lst, k):
    E.setdefault(t, []).extend((a, k) for a in lst)
add('dis-moments-np', ['intro-wightman','intro-composite','intro-af-coeff'], 'd')
add('dis-moments-np', ['intro-np-ope','intro-growth'], 'b')
add('dis-ope', ['appM-remainder','appM-brst-ope','appM-forward'], 'b')
add('scet-thrust', ['intro-bridge','appN-envelope'], 'b')
add('heavy-bdpi', ['intro-bridge'], 'd')
add('excl-dvcs', ['intro-bridge'], 'd')
add('excl-pion-ff', ['intro-bridge','appN-collins'], 'd'); add('excl-pion-ff', ['appN-endpoint'], 'b')
for t in ['disall-factorization','coll-sia','break-ddis']:
    add(t, ['intro-bridge'], 'd'); add(t, N7, 'b')
add('appN-structure', ['appN-contour','appN-envelope','appN-separation','appN-collins','appN-uv','appN-multren',
                       'appN-ward-product','appN-cutsum','appN-values','appN-tmd','appN-endpoint'], 'd')
add('appN-structure', ['appN-brst-nonlocal'], 'b')
add('disall-renorm-compat', ['appN-multren','appN-contour'], 'd'); add('disall-renorm-compat', ['appN-ir-regulator'], 'b')
add('tmd-factorization', ['intro-bridge'], 'd')
add('tmd-factorization', ['appN-tmd','appN-collins','appO-rewritten-cs','appO-mixing'], 'b')
add('appO-main', ['appO-lcopt','appO-envelope','appN-envelope','appN-separation','appN-ward-product'], 'd')
add('appO-main', ['appO-mixing','appO-deformation','appO-rewritten-cs'], 'b')
for t in ['dy-factorization','break-double-dy']:
    add(t, ['intro-bridge'], 'd'); add(t, DY7, 'b')
add('lamet-coordinate', ['lamet-ope','lamet-aux-renorm'], 'b')
add('lattice-lamet', ['lamet-ope','lamet-aux-renorm'], 'b')
add('lamet-hadronic', ['lamet-uniform','lamet-twist4','lamet-large-z'], 'b')
add('lamet-exp-decay', ['intro-wightman'], 'd'); add('lamet-exp-decay', ['lamet-gap'], 'b')
add('lamet-quasi-tmd', ['lamet-soft-rapidity'], 'd'); add('lamet-quasi-tmd', ['lamet-staple','lamet-order-limits'], 'b')
add('yzliu-soft-form-factor', ['yzliu-heavy-pair'], 'b')
add('yzliu-analyticity', ['yzliu-wightman-pt'], 'b')
add('yzliu-time-ordering', ['yzliu-wightman-pt'], 'b')
add('yzliu-universality-classes', ['yzliu-lightcone-uniform'], 'b')
add('front-commuting', ['front-mor-complete'], 'b')
add('front-hgg', ['front-scet-modes'], 'b')

# ---- checks ----
mids = [t for _, g in MID for t, *_ in g]
used = set()
for t, lst in E.items():
    assert t in mids, t
    seen = set()
    for a, k in lst:
        assert a in ASM_TAG, a
        assert a not in seen, (t, a); seen.add(a); used.add(a)
side = [a for _, g in LEFT + RIGHT for a in g]
assert sorted(side) == sorted(ASM_TAG), set(ASM_TAG) ^ set(side)
missing = set(ASM_TAG) - used
assert not missing, missing
nd = sum(1 for l in E.values() for a, k in l if k == 'd'); nb = sum(1 for l in E.values() for a, k in l if k == 'b')
print('theorems', len(mids), 'edges', nd + nb, '(direct', nd, ', bottleneck', nb, ')')

# ---- layout ----
PITCH = 0.43; HEAD = 0.5; GAP = 0.3
XL, WL = 1.5, 3.0           # left column centre, node width
XM, WM = 7.95, 3.75         # middle
XR, WR = 14.25, 3.0         # right
def place_middle():
    y = 0.0; pos = {}; heads = []
    for name, g in MID:
        heads.append((name, y)); y -= HEAD
        for t, *_ in g:
            pos[t] = y; y -= PITCH
        y -= GAP
    return pos, heads
mpos, mheads = place_middle()
def targets(a):
    return [mpos[t] for t, l in E.items() for b, k in l if b == a]
def place_side(groups):
    """groups in the given order; each at the barycentre of its targets,
    overlaps removed by pushing down, then the whole column shifted by the
    mean displacement (least squares for a rigid shift)."""
    info = []
    for name, g in groups:
        g2 = sorted(g, key=lambda a: -sum(targets(a)) / len(targets(a)))
        h = HEAD + PITCH * (len(g2) - 1)
        bary = sum(sum(targets(a)) / len(targets(a)) for a in g2) / len(g2)
        info.append([name, g2, h, bary + h / 2])      # desired top
    tops = []; cursor = None
    for name, g2, h, d in info:
        t = d if cursor is None else min(d, cursor)
        tops.append(t); cursor = t - h - GAP - 0.25
    shift = sum(d - t for (n, g, h, d), t in zip(info, tops)) / len(tops)
    tops = [t + shift for t in tops]
    tops = [min(t, 0.0) for t in tops] if max(tops) > 0 else tops
    out_pos = {}; out_heads = []
    for (name, g2, h, d), top in zip(info, tops):
        out_heads.append((name, top)); y = top - HEAD
        for a in g2:
            out_pos[a] = y; y -= PITCH
    return out_pos, out_heads
lpos, lheads = place_side(LEFT)
rpos, rheads = place_side(RIGHT)

COL = {'R':'OliveGreen','A':'RoyalBlue','P':'BurntOrange','C':'Plum'}
L = []; a = L.append
a(r'%%% BEGIN fig:summary-hypotheses')
a(r'\begin{figure}[htbp]')
a(r'\centering')
a(r'\begin{tikzpicture}[fd,x=1cm,y=1cm,')
a(r'  fd2 asm/.style={draw=orange!65!black,dashed,fill=orange!8,rounded corners=1.5pt,line width=0.5pt,'
  r'minimum height=0.34cm,inner sep=1.5pt,font=\tiny\ttfamily,anchor=center},')
a(r'  fd2 thm/.style={draw=#1!65!black,fill=#1!15,rounded corners=1.5pt,line width=0.5pt,'
  r'minimum height=0.34cm,inner sep=1.5pt,font=\tiny\ttfamily,anchor=center},')
a(r'  fd2 rcond/.style={fd2 thm=OliveGreen,dashed},')
a(r'  fd2 tag/.style={font=\tiny\sffamily\bfseries,text=#1!75!black,inner sep=0.5pt},')
a(r'  fd2 head/.style={font=\scriptsize\bfseries,inner sep=1pt},')
a(r'  fd2 e/.style={draw=gray!60,line width=0.35pt,-{Stealth[length=2.6pt,width=2.2pt]}},')
a(r'  fd2 b/.style={draw=red!60!black,line width=1.0pt,opacity=0.75,-{Stealth[length=3.4pt,width=3pt]}}]')
# group frames and heads
def frame(x, w, top, n, name):
    yb = top - HEAD - PITCH * (n - 1) - 0.27
    a(r'  \draw[gray!45,line width=0.4pt,rounded corners=3pt,fill=gray!3] (%.3f,%.3f) rectangle (%.3f,%.3f);'
      % (x - w / 2 - 0.12, yb, x + w / 2 + 0.12, top + 0.2))
    a(r'  \node[fd2 head] at (%.3f,%.3f) {%s};' % (x, top - 0.02, name))
for (name, top), (_, g) in zip(lheads, LEFT): frame(XL, WL, top, len(g), name)
for (name, top), (_, g) in zip(rheads, RIGHT): frame(XR, WR, top, len(g), name)
for (name, top), (_, g) in zip(mheads, MID): frame(XM, WM, top, len(g), name)
# edges (grey first, red on top)
def edge(asm, t, k):
    yt = mpos[t]
    if asm in lpos:
        x0, y0 = XL + WL / 2 + 0.03, lpos[asm]; x1 = XM - WM / 2 - 0.02
        c0, c1 = x0 + 1.9, x1 - 1.9
    else:
        x0, y0 = XR - WR / 2 - 0.03, rpos[asm]; x1 = XM + WM / 2 + 0.02
        c0, c1 = x0 - 1.9, x1 + 1.9
    a(r'  \draw[fd2 %s] (%.3f,%.3f) .. controls (%.3f,%.3f) and (%.3f,%.3f) .. (%.3f,%.3f);'
      % ('e' if k == 'd' else 'b', x0, y0, c0, y0, c1, yt, x1, yt))
for kind in ('d', 'b'):
    for t in mids:
        for asm, k in E.get(t, []):
            if k == kind: edge(asm, t, k)
# nodes
for asm, y in list(lpos.items()) + list(rpos.items()):
    x, w = (XL, WL) if asm in lpos else (XR, WR)
    a(r'  \node[fd2 asm,minimum width=%.2fcm] at (%.3f,%.3f) {};' % (w, x, y))
    a(r'  \node[font=\tiny\ttfamily,anchor=west,inner sep=0pt] at (%.3f,%.3f) {%s};' % (x - w / 2 + 0.07, y, asm))
    tg = ASM_TAG[asm]
    if tg != '-':
        a(r'  \node[fd2 tag=%s,anchor=east] at (%.3f,%.3f) {%s};' % (COL[tg], x + w / 2 - 0.05, y, tg))
for name, g in MID:
    for t, typ, tag, cg in g:
        y = mpos[t]
        if cg:
            a(r'  \node[fd2 rcond,minimum width=%.2fcm] at (%.3f,%.3f) {};' % (WM, XM, y))
            a(r'  \node[fd2 tag=%s,anchor=east] at (%.3f,%.3f) {%s};' % (COL[cg], XM + WM / 2 - 0.05, y, cg))
        else:
            a(r'  \node[fd2 thm=%s,minimum width=%.2fcm] at (%.3f,%.3f) {};' % (COL[tag], WM, XM, y))
        txt = t if typ == 'thm' else r'{\color{gray!50!black}%s:}%s' % (typ, t)
        a(r'  \node[font=\tiny\ttfamily,anchor=west,inner sep=0pt] at (%.3f,%.3f) {%s};' % (XM - WM / 2 + 0.07, y, txt))
# legend
ymin = min(min(lpos.values()), min(rpos.values()), min(mpos.values())) - 0.75
a(r'  \node[fd2 asm,minimum width=0.9cm,font=\tiny] at (0.5,%.3f) {asm};' % ymin)
a(r'  \node[font=\scriptsize,anchor=west] at (1.0,%.3f) {编号假设（右端字母为其标签）};' % ymin)
a(r'  \node[fd2 thm=RoyalBlue,minimum width=0.75cm,font=\tiny] at (5.45,%.3f) {[A]};' % ymin)
a(r'  \node[fd2 thm=BurntOrange,minimum width=0.75cm,font=\tiny] at (6.3,%.3f) {[P]};' % ymin)
a(r'  \node[font=\scriptsize,anchor=west] at (6.75,%.3f) {定理（填色为其标签）};' % ymin)
a(r'  \node[fd2 rcond,minimum width=1.1cm,font=\tiny] at (10.25,%.3f) {$R_{\mathrm{cond}}$};' % ymin)
a(r'  \node[font=\scriptsize,anchor=west] at (10.85,%.3f) {条件定理（右端字母为内容等级）};' % ymin)
y2 = ymin - 0.45
a(r'  \draw[fd2 e] (0.05,%.3f) -- (0.95,%.3f);' % (y2, y2))
a(r'  \node[font=\scriptsize,anchor=west] at (1.0,%.3f) {直接依赖（\texttt{\string\uses} 或前提句）};' % y2)
a(r'  \draw[fd2 b] (5.1,%.3f) -- (6.0,%.3f);' % (y2, y2))
a(r'  \node[font=\scriptsize,anchor=west] at (6.05,%.3f) {瓶颈假设（可经由所用陈述进入）};' % y2)
a(r'\end{tikzpicture}')
a(r'\caption{主要全阶论证与条件定理所依赖的编号假设（节点为去掉类型前缀的规范标签；箭头由假设指向使用它的定理）。'
  r'细灰线为直接依赖（假设出现在该定理的 \texttt{\string\uses} 列表或前提句中，即表~\ref{tab:summary-assumptions} 中的 $\checkmark$）；'
  r'粗红线为该定理的瓶颈假设（总表~\ref{tab:summary-master} 的瓶颈栏；条件定理取前提中等级最低者），它们也可能经由所用的陈述进入；'
  r'不是瓶颈的间接依赖从略，完整的依赖闭包由 \texttt{\string\uses} 数据生成，见附录~P（\cref{fig:appP-dependency}）。'
  r'全局假设 \texttt{asm:intro-*} 不降低普通陈述的等级；\texttt{appN-brst-nonlocal} 是具名缺口，只作为 \texttt{thm:appN-structure} 的前提。}')
a(r'\label{fig:summary-hypotheses}')
a(r'\end{figure}')
a(r'%%% END fig:summary-hypotheses')
open(out, 'w', encoding='utf-8').write('\n'.join(L) + '\n')
print('written', out)
