# -*- coding: utf-8 -*-
import io
def load(p): return open(p, encoding='utf-8').read()
def save(p, s): open(p, 'w', encoding='utf-8').write(s)
def rep(s, old, new):
    assert old in s, old[:90]
    return s.replace(old, new)
# ---- p1: fold definition item (e) into the paragraph after
p = 'parts/ch03_p1.tex'; s = load(p)
s = rep(s, """\\par
(e) 第~15~章的 SCET 类光矢量 $n=(1,0,0,1)$、$\\bar n=(1,0,0,-1)$ 与 $n_A,n_B$ 的换算见\\cref{sec:appA-lightfront}。
% uses: none""", """% uses: none""")
s = rep(s, """$n_B$ 即 Collins~\\cite{Collins2011}的 $w_2$。""", """$n_B$ 即 Collins~\\cite{Collins2011}的 $w_2$；第~15~章 SCET 的 $n=(1,0,0,1)$、$\\bar n=(1,0,0,-1)$ 与 $n_A,n_B$ 的换算见\\cref{sec:appA-lightfront}。""")
save(p, s)
# ---- p2
p = 'parts/ch03_p2.tex'; s = load(p)
s = rep(s, """反路径序指数是耦合符号相反的约定 $D=\\partial+\\ii gA$ 下的协变 Wilson 线；Collins~\\cite{Collins2011}用的正是那种约定，换算时须令 $g\\to-g$。在随机光滑的 SU(2)、SU(3) 背景场中对离散化路径序指数的数值检验确认了 (b)、(c) 以及伴随线等于以 $(T^c)_{ab}=-\\ii f^{cab}$ 为生成元的路径序指数（误差只是离散化误差，反路径序的偏差为 $O(1)$）。""",
"""反路径序指数是耦合符号相反的约定 $D=\\partial+\\ii gA$ 下的协变 Wilson 线（Collins~\\cite{Collins2011}的约定，换算时令 $g\\to-g$）。在随机的 SU(2)、SU(3) 背景场中对离散化路径序指数的数值检验确认了 (b)、(c) 以及伴随线等于以 $(T^c)_{ab}=-\\ii f^{cab}$ 为生成元的路径序指数。""")
s = rep(s, """把 $k$ 整体缩小为 $\\lambda$ 倍时，程函近似的相对误差随 $\\lambda$ 线性下降（数值拟合斜率 $1.00$），但其系数正比于 $1/|p\\cdot k|$：在 $p\\cdot k\\to0$ 而 $k^2\\ne0$ 的 Glauber 区近似失效。""",
"""程函近似的相对误差是 $O(\\lambda)$（$k$ 整体缩小为 $\\lambda$ 倍），但系数正比于 $1/|p\\cdot k|$：在 $p\\cdot k\\to0$ 而 $k^2\\ne0$ 的 Glauber 区近似失效。""")
s = rep(s, """(i) $k^+\\to0$ 时 $(1-\\ee^{-\\ii k^+w^-})/k^+\\to\\ii w^-$：$k^+=0$ 处的极点是可去的，不需要任何 $\\ii0$。
(ii) 令 $w^-\\to+\\infty$ 并带阻尼 $\\ee^{-\\epsilon s}$：$\\int_0^\\infty\\dd s\\,\\ee^{-\\ii sk^+-\\epsilon s}=-\\ii/(k^+-\\ii\\epsilon)$，于是 $W^{(1)}\\to g\\,t^a\\tilde A^{a+}(k)/(k^+-\\ii0)=W^{(1)}[\\infty n_B,0]$，即\\cref{eq:prelim-one-gluon}的未来规则。
(iii) 令 $w^-\\to-\\infty$ 并带阻尼 $\\ee^{+\\epsilon s}$：$\\int_0^{-\\infty}\\dd s\\,\\ee^{-\\ii sk^++\\epsilon s}=-\\ii/(k^++\\ii\\epsilon)$，得 $g\\,t^a\\tilde A^{a+}(k)/(k^++\\ii0)=W^{(1)}[-\\infty n_B,0]$。""",
"""(i) $k^+\\to0$ 时 $(1-\\ee^{-\\ii k^+w^-})/k^+\\to\\ii w^-$：极点是可去的，不需要 $\\ii0$。
(ii)(iii) 令 $w^-\\to\\pm\\infty$ 并带阻尼 $\\ee^{\\mp\\epsilon s}$：$\\int_0^{\\pm\\infty}\\dd s\\,\\ee^{-\\ii sk^+\\mp\\epsilon s}=-\\ii/(k^+\\mp\\ii\\epsilon)$，于是 $W^{(1)}\\to g\\,t^a\\tilde A^{a+}(k)/(k^+\\mp\\ii0)$，分别是\\cref{eq:prelim-one-gluon}中 $W^{(1)}[\\pm\\infty n_B,0]$ 的规则。""")
save(p, s)
# ---- p4
p = 'parts/ch03_p4.tex'; s = load(p)
s = rep(s, """把\\cref{lem:prelim-mellin}用于\\cref{ex:prelim-plus}，可以对一般的 $N$ 核对\\cref{eq:prelim-ex-plus}：取 $h=z^{N-1}$，并利用 $\\int_0^1\\frac{z^{N-1}\\ln z}{1-z}\\dd z=-\\sum_{j\\ge0}\\frac1{(N+j)^2}=-\\big[\\zeta_2-S_2(N-1)\\big]$，得
\\[
B(N-\\varepsilon,-2\\varepsilon)=-\\frac1{2\\varepsilon}-S_1(N-1)-\\varepsilon\\big[S_1^2+2S_2-\\zeta_2\\big](N-1)+O(\\varepsilon^2),
\\]
与 $\\Gamma$ 函数闭式的展开逐阶一致（$N=1,2,3,5,8$ 已作符号验证）。大 $N$ 近似收敛较慢""",
"""用\\cref{lem:prelim-mellin}与 $\\int_0^1z^{N-1}\\frac{\\ln z}{1-z}\\dd z=-[\\zeta_2-S_2(N-1)]$，\\cref{ex:prelim-plus}对一般 $N$ 给出 $B(N-\\varepsilon,-2\\varepsilon)=-\\frac1{2\\varepsilon}-S_1(N-1)-\\varepsilon[S_1^2+2S_2-\\zeta_2](N-1)+O(\\varepsilon^2)$，与 $\\Gamma$ 函数闭式逐阶一致。大 $N$ 近似收敛较慢""")
s = rep(s, """\\item \\emph{延拓的唯一性}：Carlson 定理（\\cref{thm:appK-carlson}）——在 $\\Real z\\ge0$ 上全纯、指数型、沿虚轴增长慢于 $\\ee^{c|y|}$（$c<\\pi$）且在全部非负整数上为零的函数恒为零；常数 $\\pi$ 不可改进（$\\sin\\pi z$），只用偶数点时界减半为 $\\pi/2$（临界反例 $\\sin(\\pi z/2)$）。对矩而言更简单的版本已足够：在 $\\Real z>\\sigma_0$ 上全纯、多项式有界且在一个算术级数上为零的函数恒为零（\\cref{prop:appK-continuation}）。所以部分子分布与演化核的 Mellin 变换由偶数 $N$ 唯一地延拓，例如 $S_1(N)\\mapsto\\psi(N+1)+\\gamma_E$；加上 $c\\sin(\\pi N/2)$ 虽不改变偶数点的值，却违反增长条件。由偶数与由奇数 $N$ 出发的延拓一般是不同的函数（分别对应 $q+\\bar q$ 与 $q-\\bar q$）。""",
"""\\item \\emph{延拓的唯一性}：Carlson 定理（\\cref{thm:appK-carlson}）——在 $\\Real z\\ge0$ 上全纯、指数型、沿虚轴增长慢于 $\\ee^{c|y|}$（$c<\\pi$）且在全部非负整数上为零的函数恒为零（$\\pi$ 不可改进，反例 $\\sin\\pi z$；只用偶数点时界为 $\\pi/2$，反例 $\\sin(\\pi z/2)$）。对矩而言更简单的版本已足够：在 $\\Real z>\\sigma_0$ 上全纯、多项式有界且在一个算术级数上为零的函数恒为零（\\cref{prop:appK-continuation}）。所以 Mellin 变换由偶数 $N$ 唯一地延拓（例如 $S_1(N)\\mapsto\\psi(N+1)+\\gamma_E$；加上 $c\\sin(\\pi N/2)$ 违反增长条件），而由偶数与由奇数 $N$ 出发的延拓一般不同（分别对应 $q+\\bar q$ 与 $q-\\bar q$）。""")
save(p, s)
# ---- p5
p = 'parts/ch03_p5.tex'; s = load(p)
s = rep(s, """\\emph{虚部的两种算法。}(i) 在 $q^2=s+\\ii0$ 处 $L=\\ln(s/\\mu^2)-\\ii\\pi$，故 $\\Imag\\Pi_0^{\\MSbar}(s+\\ii0)=\\frac{N_ce_q^2}{12\\pi^2}\\,\\pi=\\frac{N_ce_q^2}{12\\pi}$，$R_0=12\\pi\\Imag\\Pi_0=N_ce_q^2$。(ii) 精确到 $\\varepsilon$：""",
"""\\emph{虚部的两种算法。}(i) $q^2=s+\\ii0$ 处 $L=\\ln(s/\\mu^2)-\\ii\\pi$，故 $\\Imag\\Pi_0^{\\MSbar}=\\frac{N_ce_q^2}{12\\pi}$，$R_0=12\\pi\\Imag\\Pi_0=N_ce_q^2$。(ii) 精确到 $\\varepsilon$：""")
save(p, s)
print('ok')
