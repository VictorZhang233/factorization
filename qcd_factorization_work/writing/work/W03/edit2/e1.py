# -*- coding: utf-8 -*-
# W03 resume session: clarity/precision edits of Ch3 parts (run from writing/work/W03)
def load(p): return open(p, encoding='utf-8').read()
def save(p, s): open(p, 'w', encoding='utf-8').write(s)
def rep(s, old, new):
    assert s.count(old) == 1, ('not unique/missing', old[:80])
    return s.replace(old, new)

# ---------------- p2: Wilson lines ----------------
p = 'parts/ch03_p2.tex'; s = load(p)
old = r"""(b) 中反路径序的断言可由无穷小变换 $U=1+\ii\theta$ 验证：$\delta A_\mu=\ii[\theta,A_\mu]+\frac1g\partial_\mu\theta$，对\cref{eq:prelim-W-ode}作变分并分部积分，路径序给出 $\delta W=\ii(\theta(b)W-W\theta(a))$，两个对易子项相消；反路径序（$\dd V/\dd s=\ii g\,V\dot z\cdot A$）则给出 $\delta V=\ii(V\theta(b)-\theta(a)V)+2g\int_0^1\dd s\,V(0,s)[\dot z\cdot A,\theta]V(s,1)$，末项一般不为零。反路径序指数是耦合符号相反的约定 $D=\partial+\ii gA$ 下的协变 Wilson 线（Collins~\cite{Collins2011}的约定，换算时令 $g\to-g$）。"""
new = r"""(b) 中关于反路径序的断言可由无穷小变换 $U=1+\ii\theta$（$\delta A_\mu=\ii[\theta,A_\mu]+\frac1g\partial_\mu\theta$）看出：对\cref{eq:prelim-W-ode}作变分，路径序给出 $\delta W=\ii[\theta(b)W-W\theta(a)]$，对易子项恰好相消；反路径序（较早的点在左，$\dd V/\dd s=\ii g\,V\,\dot z\cdot A$）则给出 $\delta V=\ii[V\theta(b)-\theta(a)V]+2g\int_0^1\dd s\,V(0,s)[\dot z\cdot A,\theta]V(s,1)$，末项一般不为零。反路径序指数 $\bar P\exp(\ii g\int_a^b\dd z\cdot A)$ 恰是约定 $D=\partial+\ii gA$（Collins~\cite{Collins2011}的约定，其 Wilson 线为 $P\exp(-\ii g\int\dd z\cdot A)$）下沿反向路径（由 $b$ 到 $a$）的 Wilson 线，在那个约定下按 $U(a)\cdots U^\dagger(b)$ 变换；引用 Collins 的公式时令 $g\to-g$。"""
s = rep(s, old, new)

old = r"""\item 除伸向无穷远的一段外，每一段一个程函传播子 $\ii/(v\cdot\ell+\ii0)$，$\ell$ 是沿路径取向流动的动量，由各连接点的动量守恒与"伸向无穷远的一段 $\ell=0$"确定（连到有限端点的一段携带流入的总动量）；"""
new = r"""\item 除伸向无穷远的一段外，每一段一个程函传播子 $\ii/(v\cdot\ell+\ii0)$，$\ell$ 是沿路径取向流动的动量，由各连接点的动量守恒与"伸向无穷远的一段 $\ell=0$"确定（连到有限端点的一段把流入的总动量带到有限端点）；"""
s = rep(s, old, new)

old = r"""例如两个胶子时 $W^{(2)}-\frac12(W^{(1)})^2$ 只含 $[T_2,T_1]$ 乘以 $E(1,2)-E(2,1)$（$E(r,s)$ 为先连接 $r$ 后连接 $s$ 的程函传播子之积），这由\cref{eq:prelim-eikonal}把 $E(1)E(2)$ 写成 $E(1,2)+E(2,1)$ 即得。"""
new = r"""例如两个胶子（颜色矩阵 $T_j\equiv t^{a_j}$；$E(r,s)$ 为先连接 $r$、后连接 $s$ 的程函传播子之积，$E(j)$ 为单胶子因子）时，$W^{(2)}$ 中的相应项为 $T_2T_1E(1,2)+T_1T_2E(2,1)$，$\frac12(W^{(1)})^2$ 中为 $\frac12\{T_1,T_2\}E(1)E(2)$；用\cref{eq:prelim-eikonal}把 $E(1)E(2)$ 写成 $E(1,2)+E(2,1)$，二者之差为 $\frac12[T_2,T_1]\,[E(1,2)-E(2,1)]$，只含对易子。"""
s = rep(s, old, new)

old = r"""程函近似的相对误差是 $O(\lambda)$（$k$ 整体缩小为 $\lambda$ 倍），但系数正比于 $1/|p\cdot k|$：在 $p\cdot k\to0$ 而 $k^2\ne0$ 的 Glauber 区近似失效。"""
new = r"""程函近似略去了 $k^2$ 与 $\sla k\gamma^\mu$，要求 $|k^2|\ll|p\cdot k|$：对软标度 $k\sim\lambda Q$（各分量同阶），相对误差是 $O(\lambda)$；在 Glauber 区（$|k^+k^-|\ll\mathbf k_{\mathrm T}^2$），对沿 $+z$ 的 $p$ 有 $2p\cdot k\approx2p^+k^-$，而 $|k^2|\approx\mathbf k_{\mathrm T}^2$ 可以与之同阶，近似失效。"""
s = rep(s, old, new)
save(p, s)

# ---------------- p3: DR conventions ----------------
p = 'parts/ch03_p3.tex'; s = load(p)
old = r"""(b) 的理由：$D$ 维中横向极化有 $D-2$ 个；若对 $2$ 个极化平均，胶子道部分子截面乘以 $1-\varepsilon$，与共线极点 $-\frac2\varepsilon P_{qg}$ 相乘留下有限项 $2P_{qg}$，即上述平移。"""
new = r"""(b) 的理由：$D$ 维中横向极化有 $D-2$ 个；若改为对 $2$ 个极化平均，胶子道部分子截面整体乘以 $1-\varepsilon$，每个共线极点 $-\frac1\varepsilon P_{qg}$（单位 $\frac{\as}{2\pi}$）因而多出有限项 $+P_{qg}$。DIS 的 $\gamma^*g$ 道中夸克与反夸克各给出一个这样的极点，部分子结构函数为 $\hat F_2^g/(ze_q^2)=\frac{\as}{2\pi}\big[-\frac2\varepsilon P_{qg}+2C_2^g+O(\varepsilon)\big]$（$\mu=Q$），故 $C_2^g\to C_2^g+P_{qg}$；Drell--Yan 的 $qg$ 道只有一个这样的极点，故 $\Delta_{qg}\to\Delta_{qg}+P_{qg}$。"""
s = rep(s, old, new)
save(p, s)

# ---------------- p4: moment tools, classical citations ----------------
p = 'parts/ch03_p4.tex'; s = load(p)
old = r"""\item \emph{Hausdorff 唯一性}：$[0,1]$ 上全部矩为零的有限带号 Borel 测度为零"""
new = r"""\item \emph{Hausdorff 唯一性}~\cite{Hausdorff1923}：$[0,1]$ 上全部矩为零的有限带号 Borel 测度为零"""
s = rep(s, old, new)
old = r"""\item \emph{延拓的唯一性}：Carlson 定理（\cref{thm:appK-carlson}）——"""
new = r"""\item \emph{延拓的唯一性}：Carlson 定理（\cref{thm:appK-carlson}；Carlson~\cite{Carlson1914}，证明见\cite[第~5.81~节]{Titchmarsh1939}）——"""
s = rep(s, old, new)
old = r"""\item \emph{Müntz--Szász 定理}：对"""
new = r"""\item \emph{Müntz--Szász 定理}~\cite{Muntz1914,Szasz1916}：对"""
s = rep(s, old, new)
save(p, s)

# ---------------- p5: cuts ----------------
p = 'parts/ch03_p5.tex'; s = load(p)
old = r"""把割胶子的极化换成其动量时振幅剩下鬼场振幅（树图形式 $k_{1\mu}\mathcal A^{\mu\nu}_{ab}"""
new = r"""把割胶子的极化换成其动量时振幅剩下鬼场振幅（树图形式，$Q=k_1+k_2$：$k_{1\mu}\mathcal A^{\mu\nu}_{ab}"""
s = rep(s, old, new)
save(p, s)
print('e1 applied')
