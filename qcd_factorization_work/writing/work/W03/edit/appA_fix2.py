# -*- coding: utf-8 -*-
p = 'chapters/appA_lightfront.tex'
s = open(p, encoding='utf-8').read()
def rep(old, new):
    global s
    assert old in s, old[:80]
    s = s.replace(old, new)
rep("$\\langle\\mathcal D_1,z^{N-1}\\rangle=-\\sum_{j=0}^{N-2}\\int_0^1z^j\\ln(1-z)=\\sum_{m=1}^{N-1}\\frac{S_1(m)}m$，再用",
    "$\\langle\\mathcal D_1,z^{N-1}\\rangle=-\\sum_{j=0}^{N-2}\\int_0^1z^j\\ln(1-z)$，由第二式等于 $\\sum_{m=1}^{N-1}S_1(m)/m$，再用")
rep("例如 $\\int_0^1z^{N-1}[z^2+(1-z)^2]=\\frac2{N+2}-\\frac2{N+1}+\\frac1N=\\frac{N^2+N+2}{N(N+1)(N+2)}$。",
    "例如 $\\int_0^1z^{N-1}[z^2+(1-z)^2]=\\frac2{N+2}-\\frac2{N+1}+\\frac1N$。")
open(p, 'w', encoding='utf-8').write(s)
print('ok')
