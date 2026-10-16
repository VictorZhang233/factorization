# -*- coding: utf-8 -*-
import sys
fn = sys.argv[1]
t = open(fn, encoding='utf-8').read()

i = t.index('快度正规子有三类：'); j = t.index('\\begin{proposition}[快度发散的处理与等价性')
t = t[:i] + (
    "快度正规子有三类：Collins 的非类光 Wilson 线（\\cref{def:tmd-collins}）；Chiu--Jain--Neill--Rothstein（CJNR）的 $\\eta$ 正规子与快度重整化群\\cite{ChiuEtAl2012a,ChiuEtAl2012b}，在软 Wilson 线的每个顶点插入 $w\\,|2k^z/\\nu|^{-\\eta/2}$、在共线 Wilson 线的每个顶点插入 $w\\,|\\bar n\\cdot k/\\nu|^{-\\eta}$；Becher--Neubert 的解析正规子与“共线反常”\\cite{BecherNeubert2011}。例如在 $\\eta$ 正规子下 $|2k^z|=2k_T|\\sinh y|$，\\cref{eq:scet-rapdiv}中的快度积分变为 "
    "$\\int\\dd y\\,|2\\sinh y|^{-\\eta}=2^{-\\eta}\\Gamma(\\tfrac\\eta2)\\Gamma(\\tfrac12-\\tfrac\\eta2)/\\sqrt\\pi=\\tfrac2\\eta+\\order{\\eta}$：软辐射在正、负快度两侧都被截断，这是 CJNR 在软线中取 $\\eta/2$ 的原因\\cite{ChiuEtAl2012a}。% w18_s5 (A2, A3)\n\n"
) + t[j:]

i = t.index('\\begin{proofsketch}'); j = t.index('\\end{proofsketch}', i)
t = t[:i] + (
    "\\begin{proofsketch}\n"
    "(1) 每种方案中束流函数与软函数的快度发散在乘积中相消（CJNR：$\\tilde\\gamma^S_\\nu+2\\tilde\\gamma^B_\\nu=0$\\cite{ChiuEtAl2012b}；Becher--Neubert：$Q^2$ 依赖被完整地指数化\\cite{BecherNeubert2011}；Collins：\\cref{def:tmd-collins}中的平方根组合）。"
    "(2) 固定 $b_T$ 时 $b$ 空间截面 $H\\tilde f_A\\tilde f_B$ 对 $\\ln Q^2$ 的导数是物理量：在 Collins 方案中取 $\\zeta_A=\\zeta_B=Q^2$，它等于 $\\partial\\ln H/\\partial\\ln Q^2+\\tilde K$（\\cref{prop:tmd-evolution}）；在 $\\eta$ 方案中 $\\tilde f=\\tilde B\\sqrt{\\tilde S}$，$\\tilde B$ 只通过 $\\nu/\\omega$ 依赖于大光锥动量 $\\omega$，故 $\\partial\\ln\\tilde f/\\partial\\ln\\omega=-\\tilde\\gamma^B_\\nu=\\frac12\\tilde\\gamma^S_\\nu$，而 $\\zeta\\propto\\omega^2$；在另两种方案中乘积分别正比于 $(Q^2)^{-F_{q\\bar q}}$ 与 $(Q^2)^{-2D}$。硬函数相同时比较即得\\cref{eq:scet-kernels}；RG 一致性给出 $\\frac{\\dd\\tilde K}{\\dd\\ln\\mu}=-2\\Gamma_{\\rm cusp}$、$\\frac{\\dd F_{q\\bar q}}{\\dd\\ln\\mu}=2\\Gamma_{\\rm cusp}$、$\\frac{\\dd D}{\\dd\\ln\\mu}=\\Gamma_{\\rm cusp}$。"
    "(3) 单圈核对：$\\tilde K=-\\frac{\\as C_F}\\pi L_b$（第~14~章）；CJNR 的 $p_T$ 空间结果 $\\nu\\frac{\\dd}{\\dd\\nu}S^{(1)}=\\frac{4\\as C}{\\pi}\\mathcal L_0$（$C$ 为 Wilson 线的 Casimir，$\\mathcal L_0=\\frac1{2\\pi}[1/\\bm p^2]_+$ 在 $|\\bm p|<\\mu$ 内减除）\\cite{ChiuEtAl2012b}经 $\\int\\dd^2p\\,\\ee^{\\ii\\bm p\\cdot\\bm b}\\mathcal L_0=\\int_0^\\infty\\frac{\\dd p}p[J_0(pb)-\\theta(\\mu-p)]=-\\frac12L_b$ 给出 $\\tilde\\gamma^S_\\nu=-\\frac{2\\as C_F}{\\pi}L_b$；$F_{q\\bar q}=\\frac{C_F\\as}\\pi L_\\perp$（$L_\\perp=L_b$）\\cite{BecherNeubert2011}；$D=\\frac{\\as}{4\\pi}2C_FL_T$（$L_T=L_b$）\\cite{EchevarriaIdilbiScimemi2012}。四者满足\\cref{eq:scet-kernels}。% w18_s5 (B, C)\n"
    "完整论证见\\cite{Collins:2017oxh,ChiuEtAl2012b,BecherNeubert2011,EchevarriaIdilbiScimemi2012}。\n"
) + t[j:]

i = t.index('\\paragraph{地位与缺口}')
t = t[:i] + (
    "\\paragraph{地位与缺口}\n"
    "\\cref{prop:scet-rapidity-rg}是全阶论证（[A]）。据文献\\cite{Collins:2017oxh}摘要，它推导了 CSS 原始表述、Collins 表述与若干 SCET 表述之间的联系，并以 $\\order{\\as^2}$、$\\order{\\as^3}$ 的已知结果核对；没有对所有阶、对非微扰函数同时成立的等价性证明。最弱的一步是 (a) 的“等价”本身：单个束流函数与软函数依赖于正规子，只有组合是物理的——快度发散标志着一个真实的附加因子化变量（$\\zeta$ 或 $\\nu$），而不是正规子的人为产物；这是方案之间的等价性问题，不涉及幂次误差。每一种方案都以 TMD 因子化（\\cref{thm:tmd-factorization}，[A]）为前提，其瓶颈是\\cref{asm:appN-tmd}与 Glauber 区（\\cref{asm:appO-mixing}）；TMD 算符的多重可重整性在文献中被论证而未被证明\\cite[第~13~章]{Collins2011}。升级途径：在一个固定方案中把\\cref{asm:appN-tmd}(T3) 证明到所有阶，并给出方案之间的有限重定义。\n"
)
open(fn, 'w', encoding='utf-8').write(t)
print('ok', len(t))
