# -*- coding: utf-8 -*-
# W03 resume session, round 3 (run from writing/work/W03)
def load(p): return open(p, encoding='utf-8').read()
def save(p, s): open(p, 'w', encoding='utf-8').write(s)
def rep(s, old, new):
    assert s.count(old) == 1, ('not unique/missing', old[:80])
    return s.replace(old, new)
p = 'parts/ch03_p2.tex'; s = load(p)
s = rep(s, r"""实辐射在 $\xi\to1$ 处的同一发散与之相消""", r"""实辐射在纵向动量分数 $\xi\to1$ 处的同一发散与之相消""")
save(p, s)
p = '../../../chapters/appI_gamma5.tex'; s = load(p)
old = r"""经过 $Z_5^{\mathrm{ns}}$ 的有限重整化之后，非单态流的结果"""
new = r"""极化分裂函数的两圈计算正是这样做的：Mertig 与 van Neerven~\cite[第~3~节]{MertigVanNeerven1996}按（与 HVBM 等价的）'t Hooft--Veltman 处方计算算符矩阵元，再乘以有限重整化常数 $1+\frac{g^2}{16\pi^2}z_{qq}$，$z_{qq}(x)=-8C_F(1-x)$，以消除 $\gamma_5$ 处方的非物理效应，并把这一步推广到高自旋的非单态与单态算符（Vogelsang~\cite{Vogelsang1996}的独立重新计算与其结果一致）。$z_{qq}$ 的一阶矩 $-8C_F\int_0^1(1-x)\,\dd x=-4C_F$ 正是\cref{eq:appI-Z5}中的系数。% MvN hep-ph/9506451 Sec. 3 (below eq. (3.60)); first-moment cross-check of VF-POL-1

经过 $Z_5^{\mathrm{ns}}$ 的有限重整化之后，非单态流的结果"""
s = rep(s, old, new)
save(p, s)
print('e3 applied')
