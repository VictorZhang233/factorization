# -*- coding: utf-8 -*-
# W03 resume session, round 2: precision edits + float placement of fig:soft-eikonal (run from writing/work/W03)
def load(p): return open(p, encoding='utf-8').read()
def save(p, s): open(p, 'w', encoding='utf-8').write(s)
def rep(s, old, new):
    assert s.count(old) == 1, ('not unique/missing', old[:80])
    return s.replace(old, new)

p = 'parts/ch03_p2.tex'; s = load(p)
# E2-1: define V(s1,s2) in the reversed-ordering remark
s = rep(s, r"""则给出 $\delta V=\ii[V\theta(b)-\theta(a)V]+2g\int_0^1\dd s\,V(0,s)[\dot z\cdot A,\theta]V(s,1)$，末项一般不为零。""",
        r"""则给出 $\delta V=\ii[V\theta(b)-\theta(a)V]+2g\int_0^1\dd s\,V(0,s)[\dot z\cdot A,\theta]V(s,1)$（$V(s_1,s_2)$ 为 $[s_1,s_2]$ 段上的反路径序指数，$\theta$ 取在 $z(s)$ 处），末项一般不为零。""")
# E2-2: rapidity-divergence sentence
s = rep(s, r"""维数正规化控制不了这一端点：在共线分布中它在固定纵向动量分数时于实、虚修正之间相消，形成加号分布（第~8~章）；在固定横动量的分布中不相消，成为快度发散，需要快度正规子与软因子（第~14~章）。""",
        r"""维数正规化控制不了这一端点：在对横动量积分的共线分布中，实辐射在 $\xi\to1$ 处的同一发散与之相消，二者合成加号分布（第~8~章）；在固定横动量的分布中，虚修正只在 $\mathbf k_{\mathrm T}=0$ 处有贡献，相消不再发生，发散成为快度发散，需要快度正规子与软因子（第~14~章）。""")
# E2-7: move the figure block before the m=2 example (the block itself is unchanged, LA-10)
i = s.index('%%% BEGIN fig:soft-eikonal'); j = s.index('%%% END fig:soft-eikonal') + len('%%% END fig:soft-eikonal')
block = s[i:j]
s = s[:i] + s[j:]
s = s.replace('\n\n\n', '\n\n')
k = s.index(r'\begin{example}[$m=2$ 的程函恒等式与入射夸克传播子的程函极限]')
s = s[:k] + block + '\n\n' + s[k:]
save(p, s)

p = 'parts/ch03_p3.tex'; s = load(p)
s = rep(s, r"""弄错它们的来源是共线减除中符号错误的经典来源（本节末的常见误解）。""",
        r"""弄错它们的来源是共线减除中符号错误的经典来源（见\cref{sec:prelim-cuts}末的“常见误解”）。""")
save(p, s)

p = 'parts/ch03_p4.tex'; s = load(p)
s = rep(s, r"""这是一切单圈实辐射的结构：软极点 $-\frac{1}{2\varepsilon}\delta(1-z)$ 与虚修正的 $\delta(1-z)$ 极点相消，留下 $\mathcal D_k$ 与正规函数""",
        r"""这是一切单圈实辐射的结构：软极点 $-\frac{1}{2\varepsilon}\delta(1-z)$ 与虚修正中 $\delta(1-z)$ 的软极点相消，剩下的共线极点由部分子分布吸收，有限部分由 $\mathcal D_k$ 与正规函数组成""")
save(p, s)

p = 'parts/ch03_p5.tex'; s = load(p)
s = rep(s, r"""且逐项成立：双圈图中 $G(1,1)^2$ 一项对应虚修正（两部分子割），""",
        r"""其中 $\rho_V$、$\rho_R$ 分别是两部分子割（含虚修正）与三部分子割（实辐射）的谱函数；等式逐项成立：双圈图中 $G(1,1)^2$ 一项对应虚修正（两部分子割），""")
save(p, s)

p = 'parts/ch03_p6.tex'; s = load(p)
s = rep(s, r"""\caption{第~3~章记号速查}""", r"""\caption{本章记号速查}""")
save(p, s)
print('e2 applied')
