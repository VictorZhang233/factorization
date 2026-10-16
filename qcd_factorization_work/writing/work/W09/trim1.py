# -*- coding: utf-8 -*-
"""Trimming pass 1 for ch08 parts (duplicated prose only; no proof steps removed)."""
import os
here = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'parts')

def edit(fn, pairs):
    p = os.path.join(here, fn)
    s = open(p, encoding='utf-8').read()
    for a, b in pairs:
        if a not in s:
            raise SystemExit('NOT FOUND in %s: %s' % (fn, a[:80]))
        s = s.replace(a, b)
    open(p, 'w', encoding='utf-8').write(s)

edit('ch08_p1.tex', [
("这一次序本身是严格性的要求：倘若把 PDF 定义为“DIS 中乘在系数函数前面的量”，普适性便不再是定理的结论，而成了定义的一部分。用本书的标签表述：",
 "这一次序本身是严格性的要求：若把 PDF 定义为“DIS 中乘在系数函数前面的量”，普适性就成了定义而不是定理。用本书的标签表述："),
("部分子模型的图像是：高速强子中部分子间的相互作用因时间膨胀而变慢，硬碰撞“看到”的是一组近似自由、各携带加号动量份额 $\\xi$ 的部分子，PDF 应是“份额为 $\\xi$ 的夸克数密度”。把它变成定义需要回答：用哪个场分量计数？如何保证规范不变？如何处理计数中的紫外发散？Collins 与 Soper 的回答",
 "部分子模型的图像是：高速强子中部分子间的相互作用因时间膨胀而变慢，硬碰撞“看到”的是一组近似自由、各带加号动量份额 $\\xi$ 的部分子。把“份额为 $\\xi$ 的夸克数密度”变成定义，Collins 与 Soper 的做法"),
("是：取好分量 $\\gamma^+\\psi$，用沿光锥的 Wilson 线把两点处的场连成规范不变的双局域算符，再在 $\\MSbar$ 中重整化。",
 "是：用好分量 $\\gamma^+\\psi$ 计数，用沿光锥的 Wilson 线保证规范不变，再在 $\\MSbar$ 中重整化计数中的紫外发散。"),
])

edit('ch08_p2.tex', [
("取 Dirac 表示，$p$ 沿 $+z$，$E=p^+/\\sqrt2$，螺旋度 $h$ 的旋量 $u(p,h)=\\sqrt E\\,(\\chi_h,2h\\chi_h)^{\\tp}$。由 $\\gamma^0\\gamma^+=(1+\\gamma^0\\gamma^3)/\\sqrt2$ 与 $\\gamma^0\\gamma^3=\\begin{pmatrix}0&\\sigma_3\\\\\\sigma_3&0\\end{pmatrix}$，$\\bar u\\gamma^+u=\\frac{1}{\\sqrt2}(u^\\dagger u+u^\\dagger\\gamma^0\\gamma^3u)=\\frac{E}{\\sqrt2}(2+2\\cdot(2h)^2)=2p^+$，与 $h$ 无关；$v$ 旋量同理。夸克靶在割图表示\\cref{eq:pdf-cut}中只有 $X=$ 真空一项，直接给出 $\\frac12\\delta(\\xi p^+-p^+)\\cdot2p^+=\\delta(1-\\xi)$。反夸克靶的负号来自费米统计而非旋量：改用电荷共轭场的定义（\\cref{def:pdf-antiquark}），$C\\bar u^{\\tp}$ 张成 $v$ 旋量，直接得 $f^{(0)}_{\\bar q/\\bar q}=\\delta(1-\\xi)$。胶子靶的两项分别落在 $\\xi=\\pm1$，因子 $1/\\xi$ 使其反号：$\\xi f^{(0)}_{g/g}=\\delta(1-\\xi)+\\delta(1+\\xi)$ 是偶分布。各自由分布的矩为",
 "Dirac 表示中，$p$ 沿 $+z$、$E=p^+/\\sqrt2$，螺旋度 $h$ 的旋量 $u=\\sqrt E(\\chi_h,2h\\chi_h)^{\\tp}$；由 $\\gamma^0\\gamma^+=(1+\\gamma^0\\gamma^3)/\\sqrt2$，$\\bar u\\gamma^+u=\\frac{E}{\\sqrt2}(2+2(2h)^2)=2p^+$，与 $h$ 无关。割图表示\\cref{eq:pdf-cut}中夸克靶只有 $X=$ 真空一项，给出 $\\frac12\\delta(\\xi p^+-p^+)\\cdot2p^+=\\delta(1-\\xi)$；反夸克靶的负号来自费米统计而非旋量（改用\\cref{def:pdf-antiquark}中电荷共轭场的定义，直接得 $f^{(0)}_{\\bar q/\\bar q}=\\delta(1-\\xi)$）；胶子靶的两项落在 $\\xi=\\pm1$，$\\xi f^{(0)}_{g/g}$ 是偶分布。各自由分布的矩为"),
("在 $A^+=0$ 规范中把好分量展开为 $\\psi_+(x)=\\int_{k^+>0}\\frac{\\dd k^+\\dd^2\\bm k_{\\mathrm T}}{(2\\pi)^32k^+}\\sum_s[b_s(k)u_+\\ee^{-\\ii k\\cdot x}+d^\\dagger_s(k)v_+\\ee^{\\ii k\\cdot x}]$，$\\{b,b^\\dagger\\}=(2\\pi)^32k^+\\delta^{(3)}$；用 $\\bar\\psi\\gamma^+\\psi=\\sqrt2\\psi_+^\\dagger\\psi_+$、$u_+^\\dagger u_+=\\sqrt2k^+$，对 $0<\\xi<1$ 得",
 "在 $A^+=0$ 规范中按光前产生、湮灭算符（$\\{b,b^\\dagger\\}=(2\\pi)^32k^+\\delta^{(3)}$）展开好分量，用 $\\bar\\psi\\gamma^+\\psi=\\sqrt2\\psi_+^\\dagger\\psi_+$、$u_+^\\dagger u_+=\\sqrt2k^+$，对 $0<\\xi<1$ 得"),
("$A^+=0$ 并未完全固定规范：保持它的变换满足 $\\partial^+U=0$，即与 $x^-$ 无关，作用在 $x^-=\\pm\\infty$ 处。相应地，传播子分子 $-g^{\\mu\\nu}+(k^\\mu n_B^\\nu+n_B^\\mu k^\\nu)/k^+$ 在 $k^+=0$ 的奇异性需要处方（主值、$k^+\\pm\\ii0$、Mandelstam--Leibbrandt 等），每种处方等价于对 $\\bm A_{\\mathrm T}$ 在 $x^-=\\pm\\infty$ 施加一种边界条件。",
 "$A^+=0$ 并未完全固定规范：保持它的变换与 $x^-$ 无关，作用在 $x^-=\\pm\\infty$ 处；相应地，传播子分子在 $k^+=0$ 的奇异性需要处方（主值、$k^+\\pm\\ii0$、Mandelstam--Leibbrandt 等），每种处方等价于对 $\\bm A_{\\mathrm T}$ 在 $x^-=\\pm\\infty$ 的一种边界条件。"),
])

edit('ch08_p4.tex', [
("按\\cref{fig:pdf-oneloop}逐图汇总：R1 积分后为 $A_\\varepsilon(1-\\varepsilon)^2(1-\\xi)\\xi^{-\\varepsilon}$，紫外极点 $1-\\xi$；R2 与 V1 积分后为 $A_\\varepsilon[\\frac{2\\xi^{1-\\varepsilon}}{1-\\xi}]_+$，极点 $[\\frac{2\\xi}{1-\\xi}]_+$；V2 为 $-A_\\varepsilon\\frac{1-\\varepsilon}{2-\\varepsilon}\\delta(1-\\xi)$，极点 $-\\frac12\\delta(1-\\xi)$；(d) 中的图为零（极点均以 $\\frac{\\as}{2\\pi}\\frac{C_F}\\varepsilon$ 为单位）。$\\delta$ 项的来源一目了然：",
 "按\\cref{fig:pdf-oneloop}逐图：R1 给出 $A_\\varepsilon(1-\\varepsilon)^2(1-\\xi)\\xi^{-\\varepsilon}$（极点 $1-\\xi$），R2 与 V1 给出 $A_\\varepsilon[\\frac{2\\xi^{1-\\varepsilon}}{1-\\xi}]_+$（极点 $[\\frac{2\\xi}{1-\\xi}]_+$），V2 给出 $-A_\\varepsilon\\frac{1-\\varepsilon}{2-\\varepsilon}\\delta(1-\\xi)$（极点 $-\\frac12\\delta$），(d) 为零。$\\delta$ 项的来源一目了然："),
("\\cref{eq:pdf-ren1}的有限部分依赖于红外正规化：纯维数正规化下它为零（\\cref{prop:pdf-partonic-dr}），离壳正规化下又不相同；只有紫外极点与 $\\ln\\mu^2$ 的系数与正规化无关。",
 "有限部分依赖于红外正规化（纯维数正规化下为零，\\cref{prop:pdf-partonic-dr}）；只有紫外极点与 $\\ln\\mu^2$ 的系数与正规化无关。"),
])

edit('ch08_p6.tex', [
("强子系由部分子系经横向推动得到，推动下部分子的横动量为 $\\bm k_{\\mathrm T}=-\\bm p_{h,\\mathrm T}/z$，故 $\\frac1z\\cdot z^{2-2\\varepsilon}=z^{1-2\\varepsilon}=z^{d-3}$（$d=4-2\\varepsilon$），即",
 "强子系由部分子系经横向推动得到，部分子的横动量为 $\\bm k_{\\mathrm T}=-\\bm p_{h,\\mathrm T}/z$，故 $\\frac1z\\cdot z^{2-2\\varepsilon}=z^{1-2\\varepsilon}=z^{d-3}$，即"),
("\\item 「PDF 由 DIS 定义。」——PDF 由算符定义（\\cref{def:pdf-quark}）；DIS 方案是合法的方案选择（\\cref{rem:pdf-schemes}），但用 $F_2$ 定义 PDF 会把其他过程中的普适性变成定义。",
 "\\item 「PDF 由 DIS 定义。」——PDF 由算符定义；用 $F_2$ 定义会把普适性变成定义（\\cref{rem:pdf-schemes}）。"),
("\\item 「PDF 是概率密度，故 $\\MSbar$ PDF 为正。」——数密度诠释只对裸的、紫外截断的光锥规范量成立（\\cref{rem:pdf-number-density}）；支撑与求和规则另有证明；$\\MSbar$ 正定性是猜想，在所有标度上非负是错的（\\cref{conj:pdf-positivity}）。",
 "\\item 「PDF 是概率密度，故 $\\MSbar$ PDF 为正。」——数密度只对裸的截断量成立（\\cref{rem:pdf-number-density}）；$\\MSbar$ 正定性是猜想，在所有标度上非负是错的（\\cref{conj:pdf-positivity}）。"),
("\\item 「光锥规范去掉了所有 Wilson 线，PDF 就是部分子数算符。」——剩余规范自由、$1/k^+$ 处方与无穷远横向连接仍在（\\cref{rem:pdf-gauge-residual}）。",
 "\\item 「光锥规范去掉了所有 Wilson 线。」——剩余规范自由、$1/k^+$ 处方与无穷远横向连接仍在（\\cref{rem:pdf-gauge-residual}）。"),
("\\item 「维数正规化中夸克中夸克分布是 $\\delta(1-x)$，什么也没发生。」——裸分布是；重整化后它是纯红外极点（\\cref{prop:pdf-partonic-dr}）。",
 "\\item 「维数正规化中 $f_{q/q}=\\delta(1-x)$，什么也没发生。」——裸分布是；重整化后它是纯红外极点（\\cref{prop:pdf-partonic-dr}）。"),
("\\item 「PDF 的支撑是 $0\\le\\xi\\le1$。」——按本书约定 $f_q$ 支撑在 $[-1,1]$，$\\xi<0$ 部分是反号的反夸克密度；重整化保持支撑，$\\xi=0$ 需要小心（\\cref{thm:pdf-support-pt}）。",
 "\\item 「PDF 的支撑是 $0\\le\\xi\\le1$。」——$f_q$ 支撑在 $[-1,1]$，$\\xi<0$ 部分是反号的反夸克密度（\\cref{thm:pdf-support-pt}）。"),
("本章在任何因子化定理之前，把 PDF 与碎裂函数定义为规范不变、经过重整化的算符矩阵元，并证明了：规范与推动不变性、自由场值与支撑（微扰论中严格，强子态有全阶论证）；PDF 的矩等于扭度 2 定域算符的矩阵元，且 PDF 重整化核的矩恰为定域算符的重整化常数，其全阶证明（\\cref{app:appL}）只用到定域算符的重整化理论；DGLAP 方程由算符重整化直接得出，领头阶核既可由光锥规范的实辐射、也可由 Feynman 规范中带 Wilson 线的逐图计算得到，后者与定域算符的单圈计算逐图对应；数与动量求和规则来自守恒流；DIS 结构函数扭度 2 部分的 $x$ 空间因子化以 OPE 为前提而严格，逐点的 $x$ 空间陈述属于第~10~章的全阶论证。碎裂函数的全阶演化需要独立的乘法可重整性输入；$\\MSbar$ PDF 的正定性只是猜想。第~9~章起，这些分布将作为因子化定理中的长距离因子出现。",
 "PDF 与碎裂函数在任何因子化定理之前就有了精确的算符定义。PDF 的矩是扭度 2 定域算符的矩阵元，其重整化核的矩恰为定域算符的重整化常数（全阶证明只用定域算符的重整化理论，\\cref{app:appL}）；DGLAP 由算符重整化得出，领头阶核可由光锥规范的实辐射或 Feynman 规范中带 Wilson 线的逐图计算得到，后者与定域算符的单圈计算逐图对应；求和规则来自守恒流；DIS 扭度 2 部分的 $x$ 空间因子化以 OPE 为前提而严格。碎裂函数的全阶演化需要独立的乘法可重整性输入，$\\MSbar$ PDF 的正定性只是猜想。第~9~章起，这些分布将作为因子化定理中的长距离因子出现。"),
])
print('ok')
