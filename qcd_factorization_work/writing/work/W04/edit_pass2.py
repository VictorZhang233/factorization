# -*- coding: utf-8 -*-
# Tightening pass 2 for Ch4 (writer W04): optional figure removed, extra example folded into text,
# boxes / summary / transitions condensed.  Statements, proofs, \uses and status paragraphs untouched.
import re

def load(fn):
    return open('parts/' + fn, encoding='utf-8').read()

def save(fn, s):
    open('parts/' + fn, 'w', encoding='utf-8').write(s)

def rep(s, a, b):
    assert a in s, a[:90]
    return s.replace(a, b)

def cut(s, start, end_marker, new, include_end=False):
    i = s.index(start)
    j = s.index(end_marker, i)
    if include_end:
        j += len(end_marker)
    return s[:i] + new + s[j:]

# ------------------------------------------------------------------ p0 intro: shorter first paragraph
s = load('ch04_p0_intro.tex')
i = s.index('本章研究因子化的一切图形证明共同的几何与分析基础')
j = s.index('\\begin{tcolorbox}')
s = s[:i] + ('本章研究因子化的一切图形证明共同的几何与分析基础：在圈动量空间的哪些地方，一个费曼积分会对长程物理'
             '（小虚度、软动量）敏感，这种敏感性有多强，它又如何在可观测量中相消或被吸收。在维数正规化的重整化微扰论中，'
             'Landau 条件的两种形式、Coleman--Norton 定理的代数形式、约化图的超表观红外发散度（一个标度陈述）、单圈 Glauber '
             '区的钳夹判据、QED 的 Bloch--Nordsieck 定理与欧氏极限下的区域方法有完整证明（\\tagR，$R_{\\mathrm{PT}}$；前四者的证明在'
             '\\cref{app:appD}与\\cref{app:appE}）。钳夹面与约化图的对应、超领头构型的相消、领头区域定理、KLN 定理与红外安全量的'
             '有限性只有全阶论证（\\tagA），共同的瓶颈是从标度陈述到嵌套区域上积分界的过渡。Landau 条件的充分性与闵氏运动学中的区域'
             '方法没有证明，有色初态的非阿贝尔 Bloch--Nordsieck 抵消则不成立。\n\n') + s[j:]
save('ch04_p0_intro.tex', s)

# ------------------------------------------------------------------ p1 Landau: drop optional figure, fold toy example
s = load('ch04_p1_landau.tex')
s = cut(s, '%%% BEGIN fig:ir-landau-simplex', '%%% END fig:ir-landau-simplex\n', '', include_end=True)
s = rep(s, '故解恰为三个角（\\cref{fig:ir-landau-simplex}(b)）：', '故解恰为三个角：')
i = s.index('\\begin{example}[一维中的钳夹与端点]')
j = s.index('由此得到原则：')
toy = ('一维的例子（$a,b$ 实，$\\epsilon>0$）：两个极点 $x=a-\\ii\\epsilon$、$x=-b+\\ii\\epsilon$ 分居实轴两侧时，在上半平面闭合得\n'
       '\\begin{equation}\\label{eq:ir-toy-pinch}\n'
       '\\int_{-\\infty}^{\\infty}\\frac{\\dd x}{(x-a+\\ii\\epsilon)(x+b-\\ii\\epsilon)}=-\\frac{2\\pi\\ii}{a+b-2\\ii\\epsilon} ,\n'
       '\\end{equation}\n'
       '$a+b\\to0$、$\\epsilon\\to0$ 时两极点从两侧相向趋近，围道被夹住，积分作为外部参数 $a+b$ 的函数出现极点'
       '（\\cref{fig:landau-pinch}(b)）；两个极点同侧时在另一侧闭合得零，围道总能推离实轴（图 (a)）；端点情形 '
       '$\\int_0^1\\dd x/(x-a+\\ii0)=\\ln\\frac{1-a}{a}-\\ii\\pi$ 在 $a\\to0^+$ 时对数发散（图 (c)）。三式均已数值核对。\n\n')
s = s[:i] + toy + s[j:]
s = rep(s, '一维的例子已经包含全部要点。\n\n', '')
save('ch04_p1_landau.tex', s)

# ------------------------------------------------------------------ p2 CN: condense the vertex illustration
s = load('ch04_p2_cn.tex')
i = s.index('\\cref{prop:ir-coleman-norton}把钳夹面翻译成经典的时空图像')
j = s.index('%%% BEGIN fig:coleman-norton')
s = s[:i] + ('\\cref{prop:ir-coleman-norton}把钳夹面翻译成经典的时空图像\\cite{ColemanNorton1965}（\\cref{fig:coleman-norton}）。'
             '以无质量顶点的共线钳夹为例：在 $k=xp_1$ 处胶子线 $k$ 与夸克线 $p_1-k$ 在壳且平行于 $p_1$，离壳的反夸克线收缩进光子顶点 $X$；'
             '圈方程给出 $\\alpha_0x=\\alpha_1(1-x)$，于是两条线的位移 $\\alpha_0xp_1$ 与 $\\alpha_1(1-x)p_1$ 相等\\cite[式~(58)]{Sterman:1995fz}：'
             '夸克与胶子在 $X$ 处产生，沿 $p_1$ 的光线同行，在 $Y_1=X+\\alpha_0xp_1$ 处同时到达并结合；$\\alpha\\ge0$ 要求物理区 $0\\le x\\le1$。\n\n') + s[j:]
save('ch04_p2_cn.tex', s)

# ------------------------------------------------------------------ p4 power: figure paragraph shorter; vertex example without simplex figure
s = load('ch04_p4_power.tex')
i = s.index('\\cref{fig:momentum-regions,fig:ir-mode-exponents}从两个角度画出这些标度。')
j = s.index('%%% BEGIN fig:momentum-regions')
s = s[:i] + ('\\cref{fig:momentum-regions,fig:ir-mode-exponents}从两个角度画出这些标度；前者沿用文献中常见的记号，图中的 $n$ 共线、'
             '$\\bar n$ 共线即本书的 $A$ 共线（沿 $n_A$）与 $B$ 共线（沿 $n_B$）。Glauber 模式在 $(\\ln k^+,\\ln k^-)$ 平面中与超软模式重合，'
             '只有加上横动量方向（后者）才能区分：它位于在壳平面 $c=\\frac12(a+b)$ 之下。\n\n') + s[j:]
s = rep(s, '\\cref{eq:ir-landau-alpha}给出 $\\alpha_1\\alpha_2=0$：Landau 集是两条闭棱（\\cref{fig:ir-landau-simplex}(a)）。',
        '\\cref{eq:ir-landau-alpha}给出 $\\alpha_1\\alpha_2=0$：Landau 集是单形的两条闭棱。')
save('ch04_p4_power.tex', s)

# ------------------------------------------------------------------ p6 cancellation: transitions shorter
s = load('ch04_p6_cancel.tex')
i = s.index('无质量理论中单个割图的钳夹面给出红外与共线发散。')
j = s.index('\\begin{theorem}[QED 中的 Bloch--Nordsieck 定理 \\tagR]')
s = s[:i] + ('单个割图的钳夹面给出红外与共线发散；物理截面必须使之相消，或把它们吸收进可测量的长程因子。下面依次讨论 QED 的 '
             'Bloch--Nordsieck 定理（对不可分辨的软光子求和）、KLN 定理（对简并态求和）、非阿贝尔理论中有色初态的反例，以及红外安全的概念。\n\n') + s[j:]
i = s.index('QED 的相消依赖于两件事：')
j = s.index('\\begin{theorem}[KLN 定理 \\tagA]')
s = s[:i] + ('QED 的相消依赖于软光子耦合只依赖外线的电荷与动量、且光子之间没有相互作用；非阿贝尔理论中后一点不再成立。\n\n') + s[j:]
save('ch04_p6_cancel.tex', s)

# ------------------------------------------------------------------ p7: closing paragraph, box, summary, uses condensed
s = load('ch04_p7_regions.tex')
i = s.index('区域方法最重要的实例是第~5~章的 Sudakov 形状因子')
j = s.index('%% ---------------------------------------------------------------------')
s = s[:i] + ('区域方法最重要的实例是第~5~章的 Sudakov 形状因子（\\cref{ex:sudakov-offshell}；有质量交换须用解析正规子，'
             '\\cref{ex:sudakov-massive}）；它与 Landau 分析、Newton 多面体的现代联系以及隐藏区域见\\cref{sec:front-landau}等。\n\n') + s[j:]
i = s.index('\\begin{tcolorbox}[enhanced,breakable,title=常见误解')
j = s.index('\\end{tcolorbox}', i) + len('\\end{tcolorbox}')
box = r"""\begin{tcolorbox}[enhanced,breakable,title=常见误解,fonttitle=\bfseries,
  colback=gray!3!white,colframe=gray!55!black,boxrule=0.6pt,arc=2pt,
  left=5pt,right=5pt,top=3pt,bottom=3pt,before skip=6pt,after skip=6pt]
\textbf{“欧氏区没有钳夹，所以欧氏 Green 函数红外有限。”}（M29）零动量无质量线总满足 Landau 方程；有限性来自幂次计数（\cref{rem:ir-euclid-corners}）。\par
\textbf{“Landau 方程给出奇异性。”}（M20，O12）只是必要条件；解可以无害，被钳住也不等于奇异；外部不变量的奇异性与固定外动量下的钳夹区域是两个问题（\cref{rem:ir-landau-status}）。\par
\textbf{“Coleman--Norton 图像说明这里没有奇异性。”}（C15）它只刻画物理区钳夹（\cref{sec:ir-coleman-norton}）。\par
\textbf{“KLN 定理解释了强子对撞截面为何有限。”}（M8）初态共线奇异性被因子化而非相消；有色初态的 Bloch--Nordsieck 相消会失效（\cref{prop:ir-bn-failure}）。\par
\textbf{“红外安全保证了因子化。”}（M9）它只处理末态奇异性（\cref{thm:ir-safe-finite}）。\par
\textbf{“区域方法是定理”“可以用它确定领头区域。”}（M19，O11，C5）只在欧氏极限下是定理；Minkowski 极限下无一般证明，侧面处方在三圈有反例；有质量交换才需要解析正规子；用它确定领头区域是循环论证（\cref{prop:ir-regions-minkowski}）。
\end{tcolorbox}"""
s = s[:i] + box + s[j:]
i = s.index('\\paragraph{本章小结。}')
j = s.index('\\paragraph{这些工具在后文的用途。}')
s = s[:i] + (r"""\paragraph{本章小结。}
长程敏感性只能出现在积分围道被钳住的地方。动量空间的 Landau 方程（带 $\alpha_j\ge0$）是钳夹的必要条件，参数形式的 Landau 条件控制外部不变量的解析性与红外有限性，二者都在重整化微扰论中严格成立，但在钳夹的层次上并不等价。Coleman--Norton 图像把钳夹面翻译为经典过程，给出硬--喷注--软的约化图（\tagA）；幂次计数给出其超表观度（严格的标度陈述），在 Feynman 规范中挑出每个喷注一个物理部分子加任意多个标量极化胶子、软线只以胶子附着于喷注的领头区域（\tagA），超领头构型只在规范不变的和中相消。Glauber 区在幂次计数上领头而程函近似失效：在顶点中未被钳住，在初、末态相互作用并存时被钳住。QED 的软光子发散在单举截面中相消；KLN 定理与红外安全给出末态相消的一般框架（\tagA），有色初态的非阿贝尔 Bloch--Nordsieck 相消不成立（\tagV）；区域方法只在欧氏极限下严格。从标度陈述到积分界的过渡（\cref{asm:appN-envelope}、\cref{asm:appN-separation}）是本章全部 \tagA 结论的共同瓶颈。

""") + s[j:]
i = s.index('\\paragraph{这些工具在后文的用途。}')
s = s[:i] + (r"""\paragraph{这些工具在后文的用途。}
第~5~章用钳夹面与区域分析 Sudakov 形状因子（\cref{sec:sudakov-regions}）；第~6~章的欧氏红外有限性与 $R(s)$ 的有限性（\cref{thm:ee-euclid-ir}、\cref{thm:ee-R-finite}）建立在\cref{rem:ir-euclid-corners}与红外幂次计数之上；第~9~章把领头区域、标量极化主导与 Glauber 形变发展为一般方法（\cref{def:method-regions}、\cref{prop:method-gy-suppression}、\cref{prop:method-glauber-deformation}），附录~N 给出其精确形式；第~10、12、14~章对 DIS、Drell--Yan（\cref{prop:dy-regions}）与 TMD 使用\cref{fig:reduced-dis,fig:reduced-dy}的约化图，附录~O 处理被钳住的 Glauber 区；第~16~章以\cref{def:ir-safe}为出发点（\cref{prop:jets-sw}）；第~24~章讨论 Landau 判据的完整证明（预印本）、Gordan 择一定理与隐藏区域（\cref{thm:front-collins-pinch}、\cref{prop:front-hidden-regions}）。
""")
save('ch04_p7_regions.tex', s)
print('pass 2 done')
