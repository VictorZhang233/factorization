# -*- coding: utf-8 -*-
import sys
fn = sys.argv[1]
t = open(fn, encoding='utf-8').read()

old = "$\\sigma_0=\\frac{4\\pi\\alpha^2}{s}N_c\\sum_qe_q^2\\cdot\\frac13$ 为 Born 截面。"
new = "$\\sigma_0=\\frac{4\\pi\\alpha^2}{3s}N_c\\sum_qe_q^2$ 为 Born 截面。"
assert old in t; t = t.replace(old, new)

i = t.index('\\begin{proofsketch}'); j = t.index('\\end{proofsketch}', i)
t = t[:i] + (
    "\\begin{proofsketch}\n"
    "% errtype: E-S\n"
    "(1)~\\emph{硬匹配。}在 $\\order{\\lambda^0}$，$\\bar\\psi\\gamma^\\mu\\psi\\to C_V[\\bar\\chi_n\\gamma_\\perp^\\mu\\chi_{\\bar n}+(n\\leftrightarrow\\bar n)]$：算符形式在树图层次由\\cref{prop:scet-wilson}给出，共线规范不变性（\\cref{prop:scet-gauge}）使它在各阶只以 $\\chi_n$、$\\chi_{\\bar n}$ 出现；$C_V$ 由在壳形状因子确定（\\cref{prop:scet-hard-matching}）。"
    "(2)~\\emph{超软退耦。}由\\cref{thm:scet-decoupling}与\\cref{eq:scet-JY}，流化为 $C_V\\bar\\chi^{(0)}_nY_n^\\dagger\\gamma_\\perp^\\mu Y_{\\bar n}\\chi^{(0)}_{\\bar n}$，$\\mathcal L^{(0)}$ 分解为互不作用的 $n$、$\\bar n$、超软三部分，态空间相应地分解为 $|X_n\\rangle|X_{\\bar n}\\rangle|X_{us}\\rangle$。"
    "(3)~\\emph{测量。}由\\cref{eq:scet-taudecomp}，领头幂次的 $\\tau$ 是三部分之和；共线粒子总在其喷注所在的半球。"
    "(4)~\\emph{求和。}对末态求和、对色指标缩并：喷注矩阵元正比于 $\\mathbb 1_{\\rm c}$，色单态流使软矩阵元以 $\\frac1{N_c}\\Trc$ 出现，轻子张量与 $\\gamma_\\perp^\\mu$ 的迹给出 $\\sigma_0$，即得\\cref{eq:scet-thrust-fact}。"
    "(5)~\\emph{零箱。}推力的零箱积分无标度（\\cref{def:scet-zero-bin}(c)），减除后的喷注函数等于未减除的，不与 $S_T$ 重复计数。"
    "(6)~\\emph{Glauber。}所有共线粒子都是出射的，喷注线吸收软动量时的极点位于同一半平面（\\cref{lem:coll-final-poles}），围道可以离开 Glauber 区（\\cref{prop:method-glauber-deformation}(a)），不需要 Glauber 算符。"
    "(7)~\\emph{区域。}硬、两个共线与超软模式正是测量 $\\tau$ 时 $e^+e^-\\to$ 强子的领头区域（\\cref{thm:ir-leading-regions}，以 $\\lambda^2\\sim\\tau$ 计数）。"
    "完整论证见\\cite{Bauer:2003di,Fleming:2007qr,Schwartz:2007ib,Fleming:2007xt,BecherSchwartz2008,Bauer:2008dt}。\n"
) + t[j:]

i = t.index('\\paragraph{地位与缺口}'); j = t.index('\\Cref{fig:dijet-factorization}')
t = t[:i] + (
    "\\paragraph{地位与缺口}\n"
    "\\cref{thm:scet-thrust}在以硬、两个共线、超软为模式的 SCET 内对所有阶成立（[A]）。最弱的一步是模式完备，即\\cref{asm:intro-bridge}(Br1) 与积分形式的幂次计数\\cref{asm:appN-envelope}：(7) 只给出 E-S 型的标度陈述，余项 $\\order{\\tau}$ 不是对所有阶一致的积分界。$e^+e^-$ 中没有 Glauber 钳夹，依据是围道变形论证（\\cref{prop:method-glauber-deformation,lem:coll-final-poles}）；Rothstein--Stewart 只可作为一般机制引用：迭代的 Glauber 交换要么给出相位，要么可以吸收进软或共线 Wilson 线的方向，“因而在单举截面中相消”\\cite{RothsteinStewart2016}。在 Collins 减除的语言中，推力的减除结构是\\cref{prop:appN-thrust}（[R, $R_{\\mathrm{cond}}$]），其前提\\cref{asm:appN-collins}、\\cref{asm:appN-cutsum}、\\cref{asm:appN-ward-product}决定了图形路线的 [A]；图形路线中 Ward 恒等式那一步还牵涉第~9~章所命名的缺口（\\cref{asm:appN-brst-nonlocal}，[C]），SCET 路线以有效理论的规范对称性代替那一步。当 $Q\\tau\\sim\\Lambda$ 时软函数成为非微扰的形状函数\\cite{Korchemsky:1994is,Korchemsky:1999kt,Bauer:2003di}；在尾部，主要的强子化效应是分布的平移 $\\propto\\Lambda/Q$，作为在事件形状之间普适的陈述它属于 [C]（第~21~章）。文献：\\cite{Bauer:2003di,Lee:2006nr,Fleming:2007qr,Schwartz:2007ib,Fleming:2007xt,BecherSchwartz2008,Bauer:2008dt}。升级途径：对 $e^+e^-$ 事件形状把\\cref{asm:appN-envelope,asm:appN-collins}在所有阶以积分范数形式证明。\n\n"
) + t[j:]
open(fn, 'w', encoding='utf-8').write(t)
print('ok', len(t))
