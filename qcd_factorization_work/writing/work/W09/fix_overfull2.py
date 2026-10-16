# -*- coding: utf-8 -*-
import os
here = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'parts')
p = os.path.join(here, 'ch08_p3.tex')
s = open(p, encoding='utf-8').read()
a = r"""\gamma_{qq}=C_F\Big[\frac32+\frac{1}{N(N+1)}-2S_1(N)\Big],\qquad \gamma_{qg}=T_F\frac{N^2+N+2}{N(N+1)(N+2)},\qquad \gamma_{gq}=C_F\frac{N^2+N+2}{(N-1)N(N+1)},\\
\gamma_{gg}=2C_A\Big[\frac{1}{N(N-1)}+\frac{1}{(N+1)(N+2)}-S_1(N)\Big]+\frac{\beta_0}{2};"""
b = r"""\gamma_{qq}=C_F\Big[\frac32+\frac{1}{N(N+1)}-2S_1(N)\Big],\qquad \gamma_{qg}=T_F\frac{N^2+N+2}{N(N+1)(N+2)},\\
\gamma_{gq}=C_F\frac{N^2+N+2}{(N-1)N(N+1)},\qquad \gamma_{gg}=2C_A\Big[\frac{1}{N(N-1)}+\frac{1}{(N+1)(N+2)}-S_1(N)\Big]+\frac{\beta_0}{2};"""
assert a in s
s = s.replace(a, b)
open(p, 'w', encoding='utf-8').write(s)
print('ok')
