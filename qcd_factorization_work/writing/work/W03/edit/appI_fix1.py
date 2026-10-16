# -*- coding: utf-8 -*-
p = 'chapters/appI_gamma5.tex'
s = open(p, encoding='utf-8').read()
old = "在 $D=4-2\\varepsilon$ 维中，$\\gamma_5$ 不可能同时与全部 $\\gamma^\\mu$ 反对易、又满足四维的迹公式 $\\Tr(\\gamma^\\mu\\gamma^\\nu\\gamma^\\rho\\gamma^\\sigma\\gamma_5)=-4\\ii\\epsilon^{\\mu\\nu\\rho\\sigma}$（\\cref{def:prelim-gamma5}）。"
new = "在 $D=4-2\\varepsilon$ 维中，$\\gamma_5$ 不可能既与全部 $\\gamma^\\mu$ 反对易、又满足四维的迹公式（\\cref{def:prelim-gamma5}）。"
assert old in s
s = s.replace(old, new)
open(p, 'w', encoding='utf-8').write(s)
print('ok')
