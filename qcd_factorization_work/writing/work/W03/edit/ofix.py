# -*- coding: utf-8 -*-
def load(p): return open(p, encoding='utf-8').read()
def save(p, s): open(p, 'w', encoding='utf-8').write(s)
def rep(s, old, new):
    assert old in s, old[:90]
    return s.replace(old, new)
p = 'parts/ch03_p2.tex'; s = load(p)
s = rep(s, """所以同一条类光线上的两点之间，$W[w,0]=W[w,\\infty n_B]W[\\infty n_B,0]=W[w,-\\infty n_B]W[-\\infty n_B,0]$：伸向未来还是过去无关紧要。""",
"""所以对同一条类光线上的两点，伸向未来还是过去无关紧要：
\\[
W[w,0]=W[w,\\infty n_B]\\,W[\\infty n_B,0]=W[w,-\\infty n_B]\\,W[-\\infty n_B,0].
\\]""")
save(p, s)
p = 'parts/ch03_p5.tex'; s = load(p)
s = rep(s, """在 $O(g^2)$ 处，对流关联函数，这一恒等式已精确到 $\\varepsilon$ 的一切阶验证：$2(D-1)s\\,\\Imag\\Pi^{(1)}_{\\mathrm{bare}}(s+\\ii0)=\\rho_V+\\rho_R$，且逐项成立——双圈图中 $G(1,1)^2$ 一项对应虚修正（两部分子割），$G(1,1)G(1+\\varepsilon,1)$ 一项对应实辐射（三部分子割）（\\cref{prop:ee-cutting-exact}，第~6~章）。% VF-EE-8""",
"""在 $O(g^2)$ 处，对流关联函数，这一恒等式已精确到 $\\varepsilon$ 的一切阶验证：
\\[
2(D-1)\\,s\\,\\Imag\\Pi^{(1)}_{\\mathrm{bare}}(s+\\ii0)=\\rho_V+\\rho_R , % VF-EE-8
\\]
且逐项成立：双圈图中 $G(1,1)^2$ 一项对应虚修正（两部分子割），$G(1,1)G(1+\\varepsilon,1)$ 一项对应实辐射（三部分子割）（\\cref{prop:ee-cutting-exact}，第~6~章）。""")
save(p, s)
print('ok')
