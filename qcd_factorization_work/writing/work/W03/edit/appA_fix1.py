# -*- coding: utf-8 -*-
p = 'chapters/appA_lightfront.tex'
s = open(p, encoding='utf-8').read()
def rep(old, new):
    global s
    assert old in s, old[:80]
    s = s.replace(old, new)
rep("""(a) 对可积函数，$\\langle f\\otimes g,h\\rangle=\\int_0^1\\!\\dd\\xi\\int_0^1\\!\\dd y\\,f(\\xi)g(y)h(\\xi y)$（在 $\\int_0^1\\dd x\\,h(x)\\int_x^1\\frac{\\dd\\xi}\\xi f(\\xi)g(x/\\xi)$ 中代换 $y=x/\\xi$），这也是对分布的定义 $\\langle f(\\xi),\\langle g(y),h(\\xi y)\\rangle\\rangle$：对 $h\\in\\mathcal T_\\eta$ 与 $\\xi\\in[0,1]$，$y\\mapsto h(\\xi y)$ 在 $y=1$ 处一般不再 Hölder 连续于 $h(1)$，但 $\\mathcal D_k$ 只需要 $y\\mapsto h(\\xi y)$ 本身属于某个 $\\mathcal T_{\\eta'}$，对多项式与光滑的 $h$ 这总成立。取 $h(x)=x^{N-1}$，则 $h(\\xi y)=\\xi^{N-1}y^{N-1}$，二重配对分解为 $\\tilde f(N)\\tilde g(N)$。(b) 即\\cref{lem:appA-mellin-table}(a)。\\qed

例如 $\\mathcal D_0\\otimes\\mathcal D_0$ 的 Mellin 变换是 $S_1(N-1)^2$，它在 $x$ 空间中对应 $2\\mathcal D_1-\\zeta_2\\delta(1-z)-\\ln z/(1-z)$ 这类组合；在演化方程中，正是 Mellin 空间的乘法把卷积的迭代化为幂（第~8~章）。""",
"""(a) 对可积函数，在 $\\int_0^1\\dd x\\,h(x)\\int_x^1\\frac{\\dd\\xi}\\xi f(\\xi)g(x/\\xi)$ 中代换 $y=x/\\xi$ 得 $\\langle f\\otimes g,h\\rangle=\\int_0^1\\!\\dd\\xi\\int_0^1\\!\\dd y\\,f(\\xi)g(y)h(\\xi y)$；对分布，这就是定义 $\\langle f(\\xi),\\langle g(y),h(\\xi y)\\rangle\\rangle$，它对光滑的 $h$ 有定义（$y\\mapsto h(\\xi y)$ 光滑，内层配对作为 $\\xi$ 的函数又在 $\\xi=1$ 处 Hölder 连续）。取 $h(x)=x^{N-1}$，$h(\\xi y)=\\xi^{N-1}y^{N-1}$，二重配对分解为 $\\tilde f(N)\\tilde g(N)$。(b) 即\\cref{lem:appA-mellin-table}(a)。\\qed""")
rep("""(c)：逐项代入初等变换，并用 $S_k(N\\mp1)=S_k(N)\\mp N^{-k}$（$N-1$）与 $S_k(N+1)=S_k(N)+(N+1)^{-k}$；""",
"""(c)：逐项代入初等变换，并用 $S_k(N-1)=S_k(N)-N^{-k}$ 与 $S_k(N+1)=S_k(N)+(N+1)^{-k}$；""")
open(p, 'w', encoding='utf-8').write(s)
print('ok')
