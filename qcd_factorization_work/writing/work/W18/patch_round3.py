# -*- coding: utf-8 -*-
# Third compression round for Ch15 (wording; no statement, [R]-proof step, \uses, status content or box removed).
import sys, os
P = sys.argv[1]
def sub(fn, old, new):
    path = os.path.join(P, fn)
    t = open(path, encoding='utf-8').read()
    assert old in t, (fn, old[:70])
    t = t.replace(old, new, 1)
    open(path, 'w', encoding='utf-8').write(t)

# ---------------- p4
sub('p4_scet2.tex',
    "(b) 当红外发散也用维数正规化时，零箱减除与“除以软 Wilson 线矩阵元”的软减除等价；这一点在夸克形状因子与 $x_B\\to1$ 的 DIS 中、并在两圈阿贝尔虚修正中被显式检验\\cite{IdilbiMehen2007}；两种形式中消除重复计数的比较见\\cite{Lee:2006nr}。只有当零箱减除在每个共线因子中自洽地实施时，重复计数才被避免。",
    "(b) 红外发散也用维数正规化时，零箱减除与“除以软 Wilson 线矩阵元”的软减除等价，这在夸克形状因子、$x_B\\to1$ 的 DIS 与两圈阿贝尔虚修正中被显式检验\\cite{IdilbiMehen2007}（两种形式的比较亦见\\cite{Lee:2006nr}）；只有当零箱减除在每个共线因子中自洽地实施时，重复计数才被避免。")
sub('p4_scet2.tex',
    "对一个软胶子，精确的发射振幅与程函因子 $-n\\cdot\\epsilon^*/n\\cdot k$ 之差（对夸克自旋求和后）的相对大小在一个代表性运动学点上为 $0.81$、$0.081$、$0.0081$（$\\lambda=10^{-1},10^{-2},10^{-3}$），按 $\\lambda$ 的一次方减小；具体数值依赖于所选的点，标度行为不依赖。% w18_s5 (H); c_scet quotes 0.78, 0.077, 0.0077 for a single spinor at the same point\n软胶子若出现在拉氏量中与共线场耦合，就会把共线粒子推到硬共线虚度，因此在 SCET$_{\\rm II}$ 中它们只能出现在算符的 $S_n$ 里。",
    "对一个软胶子，精确发射振幅与程函因子 $-n\\cdot\\epsilon^*/n\\cdot k$ 之差（对夸克自旋求和）的相对大小在一个代表性运动学点上为 $0.81$、$0.081$、$0.0081$（$\\lambda=10^{-1},10^{-2},10^{-3}$），按 $\\lambda$ 的一次方减小。% w18_s5 (H); c_scet quotes 0.78, 0.077, 0.0077 for a single spinor at the same point\n软—共线耦合若出现在拉氏量中，就会把共线粒子推到硬共线虚度，故软胶子只能出现在算符的 $S_n$ 里。")

# ---------------- p5
sub('p5_glauber.tex',
    "标准的 SCET$_{\\rm I}$、SCET$_{\\rm II}$ 拉氏量里没有 Glauber 模式。Bauer--Lange--Ovanesyan 找到一类旁观者相互作用的例子，在其中必须为了自洽而引入 Glauber 胶子\\cite{Bauer:2010cc}；Rothstein--Stewart 构造了领头幂次的 Glauber 算符\\cite{RothsteinStewart2016}。在图形方法中，Glauber 区是 Drell--Yan 因子化最困难的一步（第~9~章\\cref{prop:method-glauber-deformation}，附录~O）；本节说明它在有效理论中的形态。",
    "标准的 SCET$_{\\rm I}$、SCET$_{\\rm II}$ 拉氏量里没有 Glauber 模式。Bauer--Lange--Ovanesyan 找到一类旁观者相互作用的例子，在其中为了自洽必须引入 Glauber 胶子\\cite{Bauer:2010cc}；Rothstein--Stewart 构造了领头幂次的 Glauber 算符\\cite{RothsteinStewart2016}。在图形方法中 Glauber 区是 Drell--Yan 因子化最困难的一步（\\cref{prop:method-glauber-deformation}，附录~O）。")
sub('p5_glauber.tex',
    "(1) \\emph{树图匹配。}把 QCD 中 $t$ 道单胶子交换的前向散射图投影到领头幂次：对 $n$ 共线夸克 $\\bar u_n\\gamma^\\mu u_n=n^\\mu\\,\\bar u_n\\frac{\\bar{\\sla n}}{2}u_n+\\order{\\lambda}$，对 $\\bar n$ 共线夸克同理；Glauber 动量 $q\\sim(\\lambda^2,\\lambda^2,\\lambda)$ 使 $q^2=n\\cdot q\\,\\bar n\\cdot q-\\bm q_{\\mathrm T}^2=-\\bm q_{\\mathrm T}^2[1+\\order{\\lambda^2}]$，故",
    "(1) \\emph{树图匹配。}$t$ 道单胶子交换的前向散射在领头幂次中，$\\bar u_n\\gamma^\\mu u_n=n^\\mu\\,\\bar u_n\\frac{\\bar{\\sla n}}{2}u_n+\\order{\\lambda}$（$\\bar n$ 共线夸克同理），而 Glauber 动量使 $q^2=-\\bm q_{\\mathrm T}^2[1+\\order{\\lambda^2}]$，故")

# ---------------- p6
sub('p6_thrust.tex',
    "推力是 SCET$_{\\rm I}$ 因子化的原型：观测量对红外安全（\\cref{def:ir-safe}），末态只有出射的共线粒子，因而 Glauber 区不构成障碍；因子化定理在 SCET 中可以写到所有阶（[A]），而它的每一个单圈成分都可以独立计算并与全 QCD 比较（[R]，\\cref{sec:scet-rg}）。",
    "推力是 SCET$_{\\rm I}$ 因子化的原型：观测量红外安全（\\cref{def:ir-safe}），末态只有出射的共线粒子，Glauber 区不构成障碍；因子化定理在 SCET 中可写到所有阶（[A]），其单圈成分可独立计算并与全 QCD 比较（[R]，\\cref{sec:scet-rg}）。")
sub('p6_thrust.tex',
    "喷注函数必须用归一化明确的定义\\cref{eq:scet-Jdef}：\\cite[式~(2.6)]{BecherSchwartz2008}的写法 $J=\\frac{1}{\\bar n\\cdot p}\\frac1\\pi\\Imag[\\ii\\int\\dd^4x\\,\\ee^{-\\ii px}\\langle0|\\mathrm T\\{\\bar\\chi_n(x)\\frac{\\bar{\\sla n}}2\\chi_n(0)\\}|0\\rangle]$ 若按字面计算（费米子编时的符号、对 Dirac 与色指标求迹），自由场给出 $-2N_c\\,\\delta(p^2)$，即其中隐含因子 $-\\frac1{2N_c}\\Tr$；与\\cref{eq:scet-Jdef}等价、归一化明确的定义见\\cite[式~(3)、(6)]{Becher:2006qw}。",
    "喷注函数须用归一化明确的定义\\cref{eq:scet-Jdef}：\\cite[式~(2.6)]{BecherSchwartz2008}的写法 $J=\\frac{1}{\\bar n\\cdot p}\\frac1\\pi\\Imag[\\ii\\int\\dd^4x\\,\\ee^{-\\ii px}\\langle0|\\mathrm T\\{\\bar\\chi_n(x)\\frac{\\bar{\\sla n}}2\\chi_n(0)\\}|0\\rangle]$ 按字面计算（费米子编时符号、对 Dirac 与色指标求迹）对自由场给出 $-2N_c\\,\\delta(p^2)$，即隐含因子 $-\\frac1{2N_c}\\Tr$；等价而归一化明确的定义见\\cite[式~(3)、(6)]{Becher:2006qw}。")

# ---------------- p7
sub('p7_rg.tex',
    "(a) 单圈实辐射末态为 $q(k_1)g(k_2)$，$p=k_1+k_2$，$x\\equiv\\bar n\\cdot k_2/\\bar n\\cdot p$。胶子可由共线夸克线发射（\\cref{prop:scet-lagrangian}，对共线场在树图层次精确，故可用 QCD 顶角与传播子再投影）或由 $W_n$ 发射（\\cref{prop:scet-wilson}的单胶子规则）：",
    "(a) 实辐射末态为 $q(k_1)g(k_2)$，$p=k_1+k_2$，$x\\equiv\\bar n\\cdot k_2/\\bar n\\cdot p$。胶子由共线夸克线发射（\\cref{prop:scet-lagrangian}：对共线场在树图层次精确，可用 QCD 顶角与传播子再投影）或由 $W_n$ 发射（\\cref{prop:scet-wilson}）：")
sub('p7_rg.tex',
    "方括号是 $D$ 维劈裂函数 $P_{gq}(x)/C_F$；色因子为 $\\Trc(t^at^a)=C_FN_c$。$D$ 维两体相空间为",
    "方括号是 $D$ 维劈裂函数 $P_{gq}(x)/C_F$，色因子为 $\\Trc(t^at^a)=C_FN_c$。$D$ 维两体相空间为")
sub('p7_rg.tex',
    "(c) 由定义 $L_J=L_Q+\\ln s$、$L_S=\\frac12L_Q+\\ln s$，故 $2L_Q-4L_J+4L_S=0$ 恒成立；其余是\\cref{eq:scet-RGE}的线性组合。单圈：$\\gamma^H_0-2\\gamma^J_0=-6C_F+6C_F=0$，与 (b) 的直接计算一致；并且",
    "(c) 由 $L_J=L_Q+\\ln s$、$L_S=\\frac12L_Q+\\ln s$，$2L_Q-4L_J+4L_S=0$ 恒成立，其余是\\cref{eq:scet-RGE}的线性组合。单圈 $\\gamma^H_0-2\\gamma^J_0=-6C_F+6C_F=0$，与 (b) 一致；并且")
sub('p7_rg.tex',
    "LL 重求和在微扰论中的地位因此是全阶论证，而不是严格证明。Laplace 空间与 $\\tau$ 空间累积分布的 LL 函数相同，从 NLL 起才不同；$\\lambda\\to\\frac12$ 处的奇点对应软标度 $\\mu_s=Q/(\\nu\\ee^{\\gamma_E})$ 降到 $\\Lambda$，微扰重求和在此失效。与 CTTW 的比较：CTTW 的 $\\beta_0=(11C_A-2n_f)/(12\\pi)$ 即此处的 $b$；Becher--Schwartz 报告其 RG 结果在 $\\order{\\as^3}$ 以内的 NLL 对数系数与 CTTW 完全一致，并把重求和推进到 N$^3$LL\\cite{BecherSchwartz2008}。升级途径与\\cref{thm:scet-thrust}相同。",
    "LL 重求和在微扰论中的地位因此是全阶论证，而不是严格证明。Laplace 空间与 $\\tau$ 空间累积分布的 LL 函数相同，从 NLL 起才不同；$\\lambda\\to\\frac12$ 处的奇点对应软标度 $\\mu_s=Q/(\\nu\\ee^{\\gamma_E})$ 降到 $\\Lambda$，微扰重求和在此失效。CTTW 的 $\\beta_0=(11C_A-2n_f)/(12\\pi)$ 即此处的 $b$；Becher--Schwartz 报告其 RG 结果在 $\\order{\\as^3}$ 以内的 NLL 对数系数与 CTTW 完全一致\\cite{BecherSchwartz2008}。升级途径与\\cref{thm:scet-thrust}相同。")

# ---------------- p8
sub('p8_status.tex',
    "\\par\n\\textbf{“Rothstein--Stewart 的 Glauber 拉氏量证明了 Drell--Yan 等强子对撞过程的因子化。”}不对：作者明确说旁观者相位的相消单独来看“远不是因子化的证明”，完整的 SCET 证明尚未发表（\\cref{prop:scet-glauber-operators}）。",
    "")
sub('p8_status.tex',
    "SCET 把领头区域写成场，把区域近似写成多极展开后的拉氏量，把 Ward 恒等式写成共线规范不变性。在树图层次，积掉 $\\phi_{\\bar n}$ 与离壳模式是精确的，$W_n$ 由程函因子按次序求和得到；领头阶拉氏量具有共线与超软规范对称性，BPS 场重定义使超软胶子在领头幂次只出现在算符的 $Y_n$ 中（[R]）。SCET$_{\\rm II}$ 中软 Wilson 线由积掉硬共线模式产生，快度发散的三种处理给出等价的 TMD 因子化（[A]）。Glauber 模式由 Rothstein--Stewart 的算符描述，与附录~O 的光锥序证明一一对应，但其相消在强子对撞中没有完整证明（[A]）。推力分布的因子化是 [A]，其单圈因子、RG 一致性与对全 QCD 奇异项的再现是 [R]，LL 指数作为 QCD 陈述继承 [A]。",
    "在树图层次，积掉 $\\phi_{\\bar n}$ 与离壳模式是精确的，$W_n$ 由程函因子按次序求和得到；领头阶拉氏量的规范对称性与 BPS 场重定义使超软胶子只出现在算符的 $Y_n$ 中（[R]）。SCET$_{\\rm II}$ 的快度发散有三种等价的处理，Glauber 模式由 Rothstein--Stewart 的算符描述而其相消没有完整证明（[A]）。推力分布的因子化是 [A]，其单圈因子、RG 一致性与对全 QCD 奇异项的再现是 [R]，LL 指数作为 QCD 陈述继承 [A]。")
print('round3 ok')
