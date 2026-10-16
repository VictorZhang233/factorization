# -*- coding: utf-8 -*-
def load(p): return open(p, encoding='utf-8').read()
def save(p, s): open(p, 'w', encoding='utf-8').write(s)
def rep(s, old, new):
    assert old in s, old[:90]
    return s.replace(old, new)
p = 'parts/ch03_p2.tex'; s = load(p)
i = s.index("非阿贝尔情形中，\\cref{eq:prelim-eikonal}只适用于颜色对称化的部分；两个胶子时")
j = s.index("\\begin{example}[$m=2$ 的程函恒等式")
s = s[:i] + """非阿贝尔情形中颜色按路径排序，\\cref{eq:prelim-eikonal}只适用于颜色对称化的部分；反对称部分由对易子 $[t^b,t^a]=\\ii f^{bac}t^c$ 组成，即携带总动量的伴随"网"。例如两个胶子时 $W^{(2)}-\\frac12(W^{(1)})^2$ 只含 $[T_2,T_1]$ 乘以 $E(1,2)-E(2,1)$（$E(r,s)$ 为先连接 $r$ 后连接 $s$ 的程函传播子之积），这由\\cref{eq:prelim-eikonal}把 $E(1)E(2)$ 写成 $E(1,2)+E(2,1)$ 即得。% VF-WL-3
以网表述的全阶非阿贝尔指数化是全阶论证（\\cref{prop:appB-webs}；Gatheral~\\cite{Gatheral1983}，Frenkel 与 Taylor~\\cite{FrenkelTaylor1984}）。

""" + s[j:]
s = rep(s, """(c) 两个软胶子依次（先 $k_1$ 后 $k_2$）被吸收时，重复 (b) 两次得 $\\frac{-g\\,p^{\\mu_2}}{p\\cdot(k_1+k_2)+\\ii0}\\frac{-g\\,p^{\\mu_1}}{p\\cdot k_1+\\ii0}t^{a_2}t^{a_1}u(p)$，正是\\cref{eq:prelim-past}中这一次序的项。对两种次序求和：颜色对易时由 (a) 得到两个独立单胶子因子之积；对 QCD 的色矩阵得到路径序的 $W^{(2)}$，它不是乘积。""",
"""(c) 两个软胶子依次（先 $k_1$ 后 $k_2$）被吸收时，重复 (b) 两次得\\cref{eq:prelim-past}中这一次序的项 $\\frac{-g\\,p^{\\mu_2}}{p\\cdot(k_1+k_2)+\\ii0}\\frac{-g\\,p^{\\mu_1}}{p\\cdot k_1+\\ii0}t^{a_2}t^{a_1}u(p)$；对两种次序求和，颜色对易时由 (a) 得到单胶子因子之积，QCD 中则得到路径序的 $W^{(2)}$。""")
save(p, s)
p = 'parts/ch03_p5.tex'; s = load(p)
s = rep(s, """(1) 坐标空间。把每个顶点标记为"无圈"或"有圈"：无圈顶点用通常的顶点因子，有圈顶点用其复共轭；两端无圈的线用 $\\Delta_F(x-y)$，两端有圈的用 $\\Delta_F^*(x-y)$，无圈的 $x$ 与有圈的 $y$ 之间用正频函数 $\\Delta^+(y-x)$。由 $\\Delta_F(x)=\\theta(x^0)\\Delta^+(x)+\\theta(-x^0)\\Delta^+(-x)$ 与 $\\Delta_F^*(x)=\\theta(x^0)\\Delta^+(-x)+\\theta(-x^0)\\Delta^+(x)$，若 $x_i$ 是时间最大的顶点，与它相连的线在 $x_i$ 改变标记时都不变，只有顶点因子变号（实耦合）；故对 $x_i$ 的两种标记求和为零，而每个时间排序都有时间最大的顶点，所以全部 $2^n$ 种标记之和为零。""",
"""(1) 坐标空间：把每个顶点标记为"无圈"或"有圈"（有圈顶点用复共轭的顶点因子），两端无圈的线用 $\\Delta_F(x-y)$，两端有圈的用 $\\Delta_F^*(x-y)$，无圈的 $x$ 与有圈的 $y$ 之间用正频函数 $\\Delta^+(y-x)$。由 $\\Delta_F(x)=\\theta(x^0)\\Delta^+(x)+\\theta(-x^0)\\Delta^+(-x)$，若 $x_i$ 是时间最大的顶点，与它相连的线在 $x_i$ 改变标记时都不变而顶点因子变号；故全部 $2^n$ 种标记之和为零。""")
s = rep(s, """(1) 对在壳胶子取类光的 $\\bar k=(k^0,-\\mathbf k)$，则 $-g_{\\mu\\nu}=\\sum_{\\lambda=1,2}\\epsilon^{(\\lambda)}_\\mu\\epsilon^{(\\lambda)*}_\\nu-\\frac{k_\\mu\\bar k_\\nu+\\bar k_\\mu k_\\nu}{k\\cdot\\bar k}$。(2) 由 Slavnov--Taylor 恒等式（\\cref{thm:prelim-slavnov-taylor}），把割胶子的极化换成其动量时，振幅剩下的正是鬼场振幅；树图形式为 $k_{1\\mu}\\mathcal A^{\\mu\\nu}_{ab}=\\frac{g^2f^{abc}}{Q^2}(k_2^2g^{\\nu\\sigma}-k_2^\\nu k_2^\\sigma)J_{c\\sigma}$，$J_c^\\sigma=\\bar v(p_2)\\gamma^\\sigma t^cu(p_1)$，另一胶子为物理极化时为零。于是 (1) 中第二项化为鬼场振幅之积，与鬼场割线相消。""",
"""(1) 对在壳胶子取类光的 $\\bar k=(k^0,-\\mathbf k)$，$-g_{\\mu\\nu}=\\sum_{\\lambda=1,2}\\epsilon^{(\\lambda)}_\\mu\\epsilon^{(\\lambda)*}_\\nu-\\frac{k_\\mu\\bar k_\\nu+\\bar k_\\mu k_\\nu}{k\\cdot\\bar k}$。(2) 由 Slavnov--Taylor 恒等式（\\cref{thm:prelim-slavnov-taylor}），把割胶子的极化换成其动量时振幅剩下鬼场振幅（树图形式 $k_{1\\mu}\\mathcal A^{\\mu\\nu}_{ab}=\\frac{g^2f^{abc}}{Q^2}(k_2^2g^{\\nu\\sigma}-k_2^\\nu k_2^\\sigma)\\bar v(p_2)\\gamma_\\sigma t^cu(p_1)$，另一胶子为物理极化时为零），于是 (1) 中第二项与鬼场割线相消。""")
save(p, s)
print('ok')
