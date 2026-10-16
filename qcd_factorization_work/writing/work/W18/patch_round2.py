# -*- coding: utf-8 -*-
# Second compression round for Ch15 (wording only; statements, [R] proof steps, \uses, status content and boxes kept).
import sys, os
P = sys.argv[1]
def sub(fn, old, new, count=1):
    path = os.path.join(P, fn)
    t = open(path, encoding='utf-8').read()
    assert t.count(old) >= 1, (fn, old[:60])
    t = t.replace(old, new, count)
    open(path, 'w', encoding='utf-8').write(t)

# ---------------- p0: conventions paragraph
sub('p0_intro.tex',
    "Dirac 投影算符 $P_n\\equiv\\frac{\\sla n\\bar{\\sla n}}{4}$、$P_{\\bar n}\\equiv\\frac{\\bar{\\sla n}\\sla n}{4}$ 满足 $P_n^2=P_n$、$P_n+P_{\\bar n}=1$、$P_nP_{\\bar n}=0$、$\\sla nP_n=0$、$\\gamma^0P_n^\\dagger\\gamma^0=P_{\\bar n}$（由 $\\sla n^2=\\bar{\\sla n}^2=0$、$\\sla n\\bar{\\sla n}+\\bar{\\sla n}\\sla n=4$），$\\gamma_\\perp^\\mu$ 与 $\\sla n$、$\\bar{\\sla n}$ 反对易，从而与 $P_n$、$P_{\\bar n}$ 对易。",
    "投影算符 $P_n\\equiv\\frac{\\sla n\\bar{\\sla n}}{4}$、$P_{\\bar n}\\equiv\\frac{\\bar{\\sla n}\\sla n}{4}$ 满足 $P_n^2=P_n$、$P_n+P_{\\bar n}=1$、$P_nP_{\\bar n}=0$、$\\sla nP_n=0$、$\\gamma^0P_n^\\dagger\\gamma^0=P_{\\bar n}$，并与 $\\gamma_\\perp^\\mu$ 对易。")
sub('p0_intro.tex',
    "SCET 的全阶陈述依赖三条前提，它们与图形方法的三处困难一一对应：模式完备对应区域完备与幂次计数（\\cref{asm:appN-envelope}），零箱减除的自洽对应减除的组合学（\\cref{asm:appN-collins}），Glauber 拉氏量与快度正规子对应 Glauber 区的围道变形（附录~O）。精确的表述见本章最后的\\cref{rem:scet-assumptions}。因此 SCET 证明并不比 Collins 的图形证明更严格；二者互补。",
    "SCET 的全阶陈述依赖三条前提，与图形方法的三处困难一一对应：模式完备对应区域完备与幂次计数（\\cref{asm:appN-envelope}），零箱减除的自洽对应减除的组合学（\\cref{asm:appN-collins}），Glauber 拉氏量与快度正规子对应 Glauber 区的围道变形（附录~O）；见\\cref{rem:scet-assumptions}。因此 SCET 证明并不比 Collins 的图形证明更严格，二者互补。")

# ---------------- p1: scaling proof and interactions paragraph
sub('p1_modes.tex',
    "共线胶子在一般协变规范中的传播子 $\\frac{-\\ii}{k^2}[g^{\\mu\\nu}-(1-\\xi_g)\\frac{k^\\mu k^\\nu}{k^2}]$（\\cref{def:prelim-feynman-rules}）的第二项给出 $A_n^\\mu A_n^\\nu\\sim\\lambda^4\\cdot k^\\mu k^\\nu/\\lambda^4$，即 $A_n^\\mu$ 各分量与 $k^\\mu$ 的相应分量同阶；第一项给出 $\\langle\\bar n\\cdot A_n\\,\\bar n\\cdot A_n\\rangle\\propto\\bar n^2=0$、$\\langle n\\cdot A_n\\,\\bar n\\cdot A_n\\rangle\\sim\\lambda^2$、$\\langle A_{n\\perp}A_{n\\perp}\\rangle\\sim\\lambda^2$，与 $(1,\\lambda^2,\\lambda)$ 相容。",
    "共线胶子的协变规范传播子 $\\frac{-\\ii}{k^2}[g^{\\mu\\nu}-(1-\\xi_g)\\frac{k^\\mu k^\\nu}{k^2}]$（\\cref{def:prelim-feynman-rules}）的第二项给出 $A_n^\\mu A_n^\\nu\\sim k^\\mu k^\\nu$，即 $A_n^\\mu$ 与 $k^\\mu$ 逐分量同阶；第一项给出 $\\langle\\bar n\\cdot A_n\\,\\bar n\\cdot A_n\\rangle\\propto\\bar n^2=0$、$\\langle n\\cdot A_n\\,\\bar n\\cdot A_n\\rangle\\sim\\langle A_{n\\perp}A_{n\\perp}\\rangle\\sim\\lambda^2$，与之相容。")
sub('p1_modes.tex',
    "吸收超软动量后 $(p+k)^2=p^2+\\bar n\\cdot p\\,n\\cdot k+\\order{\\lambda^3Q^2}$ 仍是共线的，且只出现 $n\\cdot k$；吸收软动量后 $(p+k)^2\\simeq\\bar n\\cdot p\\,n\\cdot k\\sim\\lambda Q^2$ 是硬共线的（\\cref{sec:scet-scet2}）；与 $\\bar n$ 共线动量结合得 $\\sim Q^2$（\\cref{prop:scet-wilson}）；交换 Glauber 动量 $q$ 时两个共线扇区都保持在壳，$|n\\cdot q\\,\\bar n\\cdot q|\\ll\\bm q_{\\mathrm T}^2$，交换在 $x^\\pm$ 上是瞬时的势（\\cref{sec:scet-glauber}）。",
    "吸收超软动量后 $(p+k)^2=p^2+\\bar n\\cdot p\\,n\\cdot k+\\order{\\lambda^3Q^2}$ 仍是共线的且只含 $n\\cdot k$；吸收软动量后 $(p+k)^2\\simeq\\bar n\\cdot p\\,n\\cdot k\\sim\\lambda Q^2$ 是硬共线的；与 $\\bar n$ 共线动量结合得 $\\sim Q^2$；交换 Glauber 动量时两个共线扇区都保持在壳，交换是瞬时的势。")

# ---------------- p3: shorten direct verification and remark
sub('p3_decoupling.tex',
    "也可直接验证：$\\ii\\bar n\\cdot\\partial$、$\\ii\\partial_\\perp$ 与 $Y_n$ 对易，由 (a) 得 $Y_n^\\dagger(\\ii\\mathcal D^\\mu+gA_n^\\mu)Y_n=\\ii\\mathcal D^\\mu_{(0)}+gA_n^{(0)\\mu}$（$\\ii\\mathcal D_{(0)}$ 不含超软场），且 $W_n[Y_nA^{(0)}Y_n^\\dagger]=Y_nW_n[A^{(0)}]Y_n^\\dagger$（$Y_n$ 沿 $\\bar n$ 为常数）。若规范固定项用 $\\ii\\partial$，$[\\ii\\partial,Y_nA^{(0)}Y_n^\\dagger]$ 不按共轭变换（条件 (2)）；若鬼场不重定义，鬼场项留下与 $n\\cdot A_{us}$ 的耦合（条件 (1)）；只有当 $Y_n$ 只依赖于 $\\bar n\\cdot x$ 时它才与 $\\ii\\bar n\\cdot\\partial$、$\\ii\\partial_\\perp$ 对易（条件 (5)）。",
    "（直接验证同样可行：$Y_n^\\dagger(\\ii\\mathcal D^\\mu+gA_n^\\mu)Y_n=\\ii\\mathcal D^\\mu_{(0)}+gA_n^{(0)\\mu}$，$W_n[Y_nA^{(0)}Y_n^\\dagger]=Y_nW_n[A^{(0)}]Y_n^\\dagger$。）条件 (1)(2) 是\\cref{prop:scet-gauge}(b) 的超软不变性所需：用 $\\ii\\partial$ 的规范固定项或不重定义的鬼场会留下与 $n\\cdot A_{us}$ 的耦合；条件 (5) 保证 $Y_n$ 是超软变换并与 $\\ii\\bar n\\cdot\\partial$、$\\ii\\partial_\\perp$ 对易。")
sub('p3_decoupling.tex',
    "对拉氏量恒等式与单圈推力这一差别无关紧要：虚图无标度，实辐射有 $n\\cdot k,\\bar n\\cdot k>0$；$e^+e^-$、DIS 与 Drell--Yan 的半球软函数在微扰论中直到 $\\order{\\as^2}$ 都相等，尽管个别振幅的虚部符号不同\\cite{Kang:2015moa}。此处 $\\lambda^2Q$ 的模式是超软的，不是 SCET$_{\\rm II}$ 意义下的软；",
    "对单圈推力这一差别无关紧要（虚图无标度，实辐射有 $n\\cdot k,\\bar n\\cdot k>0$）；$e^+e^-$、DIS 与 Drell--Yan 的半球软函数直到 $\\order{\\as^2}$ 都相等，尽管个别振幅的虚部符号不同\\cite{Kang:2015moa}。此处 $\\lambda^2Q$ 的模式是超软的；")
sub('p3_decoupling.tex',
    "于是 $\\ii n\\cdot\\partial Y_n=-g\\,t^an\\cdot\\epsilon\\,\\ee^{-\\ii k\\cdot x}+\\order{g^2}$ 恰与 $g\\,n\\cdot A_{us}$ 相消：$\\mathcal L^{(0)}_{\\xi\\xi}[Y_n\\xi^{(0)}_n]$ 中 $\\order{g}$ 的超软耦合消失。振幅层次：",
    "$\\ii n\\cdot\\partial Y_n=-g\\,t^an\\cdot\\epsilon\\,\\ee^{-\\ii k\\cdot x}+\\order{g^2}$ 恰与 $g\\,n\\cdot A_{us}$ 相消，故 $\\order{g}$ 的超软耦合消失。振幅层次：")
print('round2 ok')
