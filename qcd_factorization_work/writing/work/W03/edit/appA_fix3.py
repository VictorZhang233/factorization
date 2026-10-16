# -*- coding: utf-8 -*-
p = 'chapters/appA_lightfront.tex'
s = open(p, encoding='utf-8').read()
def rep(old, new):
    global s
    assert old in s, old[:80]
    s = s.replace(old, new)
rep("(a) 第一式即 $\\langle\\mathcal D_0,z^{N-1}\\rangle$；$\\langle\\mathcal D_1,z^{N-1}\\rangle=-\\sum_{j=0}^{N-2}\\int_0^1z^j\\ln(1-z)$，由第二式等于 $\\sum_{m=1}^{N-1}S_1(m)/m$，再用 $(\\sum_{i\\le n}a_i)^2=2\\sum_{m\\le n}a_m\\sum_{i\\le m}a_i-\\sum_{i\\le n}a_i^2$（$a_i=1/i$）。",
    """(a) 第一式即 $\\langle\\mathcal D_0,z^{N-1}\\rangle$。由第二式，
\\[
\\langle\\mathcal D_1,z^{N-1}\\rangle=-\\sum_{j=0}^{N-2}\\int_0^1z^j\\ln(1-z)\\,\\dd z=\\sum_{m=1}^{N-1}\\frac{S_1(m)}m=\\frac12\\big[S_1^2+S_2\\big](N-1),
\\]
最后一步用 $(\\sum_{i\\le n}a_i)^2=2\\sum_{m\\le n}a_m\\sum_{i\\le m}a_i-\\sum_{i\\le n}a_i^2$（$a_i=1/i$）。""")
rep("两端都在 $\\Real N>0$ 上全纯且多项式有界，延拓唯一（\\cref{prop:appK-continuation}，指引）。",
    "两端都在 $\\Real N>0$ 上全纯且多项式有界，延拓唯一（附录~K）。")
rep("(a) 对 $\\eta>0$，$\\mathcal T_\\eta$ 是 $[0,1]$ 上满足 $|g(z)-g(1)|\\le C(1-z)^\\eta$ 的连续函数 $g$ 的空间。每个 $\\mathcal D_k$ 以及\\cref{lem:appA-plus-product}约定下的每个乘积 $g\\,\\mathcal D_k$（$g\\in\\mathcal T_\\eta$）都是 $\\mathcal T_\\eta$ 上的线性泛函；",
    "(a) 对 $\\eta>0$，$\\mathcal T_\\eta$ 是 $[0,1]$ 上满足 $|g(z)-g(1)|\\le C(1-z)^\\eta$ 的连续函数 $g$ 的空间。每个 $\\mathcal D_k$ 以及乘积约定下的每个乘积 $g\\,\\mathcal D_k$（$g\\in\\mathcal T_\\eta$）都是 $\\mathcal T_\\eta$ 上的线性泛函；")
rep("代回 $t=-a\\varepsilon$ 即\\cref{eq:prelim-plus-expansion}。", "代回 $t=-a\\varepsilon$ 即\\cref{lem:prelim-plus-expansion}中的展开式。")
open(p, 'w', encoding='utf-8').write(s)
print('ok')
