# -*- coding: utf-8 -*-
def load(p): return open(p, encoding='utf-8').read()
def save(p, s): open(p, 'w', encoding='utf-8').write(s)
def rep(s, old, new):
    assert old in s, old[:90]
    return s.replace(old, new)
p = 'parts/ch03_p2.tex'; s = load(p)
s = rep(s, "\\uses{def:prelim-wilson,prop:qcd-covariance}", "\\uses{def:prelim-qcd,def:prelim-wilson,prop:qcd-covariance}")
s = rep(s, "特别地，取 $a_j=n\\cdot k_j+\\ii\\epsilon$（$\\epsilon>0$），左边第 $j$ 个分母为 $n\\cdot(k_{\\pi(1)}+\\dots+k_{\\pi(j)})+\\ii j\\epsilon$：带绝热正规化（\\cref{def:prelim-wilson}(b)）的阿贝尔程函恒等式在有限 $\\epsilon$ 下严格成立。",
        "特别地，取 $a_j=n\\cdot k_j+\\ii\\epsilon$（$\\epsilon>0$），左边第 $j$ 个分母为 $n\\cdot(k_{\\pi(1)}+\\dots+k_{\\pi(j)})+\\ii j\\epsilon$：带绝热正规化的阿贝尔程函恒等式在有限 $\\epsilon$ 下严格成立。")
s = rep(s, "由\\cref{prop:prelim-wilson-rules}证明中的逐次积分，每个单纯形贡献",
        "与\\cref{eq:prelim-past}的推导相同的逐次积分表明，每个单纯形贡献")
save(p, s)
p = 'parts/ch03_p3.tex'; s = load(p)
s = rep(s, "$D$ 维相空间以及 $S_\\varepsilon$ 约定的影响见\\cref{sec:appC-msbar}，$\\gamma_5$ 见\\cref{def:prelim-gamma5}。",
        "$D$ 维相空间以及 $S_\\varepsilon$ 约定的影响见\\cref{sec:appC-msbar}，$\\gamma_5$ 的约定见本节末。")
save(p, s)
print('ok')
