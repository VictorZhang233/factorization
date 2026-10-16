# -*- coding: utf-8 -*-
import os
here = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'parts')
def edit(fn, pairs):
    p = os.path.join(here, fn)
    s = open(p, encoding='utf-8').read()
    for a, b in pairs:
        if a not in s:
            raise SystemExit('NOT FOUND in %s: %s' % (fn, a[:80]))
        s = s.replace(a, b)
    open(p, 'w', encoding='utf-8').write(s)

edit('ch08_p3.tex', [
(r"""\begin{equation}\label{eq:pdf-ioffe}
M_q(w^-)\equiv\langle P|O_q(w^-)|P\rangle_{\mathrm c}=2P^+\!\int\!\dd\xi\,\ee^{\ii\xi P^+w^-}f_q(\xi),\qquad
M_g(w^-)\equiv\langle P|O_g(w^-)|P\rangle_{\mathrm c}=(P^+)^2\!\int\!\dd\xi\,\ee^{\ii\xi P^+w^-}\xi f_g(\xi).
\end{equation}""",
r"""\begin{equation}\label{eq:pdf-ioffe}
\begin{gathered}
M_q(w^-)\equiv\langle P|O_q(w^-)|P\rangle_{\mathrm c}=2P^+\!\int\!\dd\xi\,\ee^{\ii\xi P^+w^-}f_q(\xi),\\
M_g(w^-)\equiv\langle P|O_g(w^-)|P\rangle_{\mathrm c}=(P^+)^2\!\int\!\dd\xi\,\ee^{\ii\xi P^+w^-}\xi f_g(\xi).
\end{gathered}
\end{equation}"""),
(r"""\begin{equation}\label{eq:pdf-Pij}
\begin{gathered}
P_{qq}=C_F\Big[\frac{1+z^2}{1-z}\Big]_+=C_F\Big[\frac{1+z^2}{(1-z)_+}+\frac32\delta(1-z)\Big],\qquad P_{qg}=T_F\big[z^2+(1-z)^2\big],\qquad P_{gq}=C_F\frac{1+(1-z)^2}{z},\\
P_{gg}=2C_A\Big[\frac{z}{(1-z)_+}+\frac{1-z}{z}+z(1-z)\Big]+\frac{\beta_0}{2}\delta(1-z),
\end{gathered}
\end{equation}""",
r"""\begin{equation}\label{eq:pdf-Pij}
\begin{gathered}
P_{qq}=C_F\Big[\frac{1+z^2}{1-z}\Big]_+=C_F\Big[\frac{1+z^2}{(1-z)_+}+\frac32\delta(1-z)\Big],\qquad P_{qg}=T_F\big[z^2+(1-z)^2\big],\\
P_{gq}=C_F\frac{1+(1-z)^2}{z},\qquad P_{gg}=2C_A\Big[\frac{z}{(1-z)_+}+\frac{1-z}{z}+z(1-z)\Big]+\frac{\beta_0}{2}\delta(1-z),
\end{gathered}
\end{equation}"""),
(r"""\begin{equation}\label{eq:pdf-gammas}
\begin{gathered}
\gamma_{qq}=C_F\Big[\frac32+\frac{1}{N(N+1)}-2S_1(N)\Big],\quad \gamma_{qg}=T_F\frac{N^2+N+2}{N(N+1)(N+2)},\quad \gamma_{gq}=C_F\frac{N^2+N+2}{(N-1)N(N+1)},\\
\gamma_{gg}=2C_A\Big[\frac{1}{N(N-1)}+\frac{1}{(N+1)(N+2)}-S_1(N)\Big]+\frac{\beta_0}{2};
\end{gathered}
\end{equation}""",
r"""\begin{equation}\label{eq:pdf-gammas}
\begin{gathered}
\gamma_{qq}=C_F\Big[\frac32+\frac{1}{N(N+1)}-2S_1(N)\Big],\qquad \gamma_{qg}=T_F\frac{N^2+N+2}{N(N+1)(N+2)},\qquad \gamma_{gq}=C_F\frac{N^2+N+2}{(N-1)N(N+1)},\\
\gamma_{gg}=2C_A\Big[\frac{1}{N(N-1)}+\frac{1}{(N+1)(N+2)}-S_1(N)\Big]+\frac{\beta_0}{2};
\end{gathered}
\end{equation}"""),
])

edit('ch08_p6.tex', [
(r"""\begin{equation}\label{eq:pdf-ff}
d_{h/q}(z)=\frac{z^{1-2\varepsilon}}{4N_c}\sum_X\int\frac{\dd w^-}{2\pi}\,\ee^{\ii k^+w^-}\Trc\TrD\Big[\gamma^+\langle0|W[\infty n_B,w]\psi(w)|hX\rangle\langle hX|\bar\psi(0)W[0,\infty n_B]|0\rangle\Big],
\end{equation}""",
r"""\begin{equation}\label{eq:pdf-ff}
\begin{aligned}
d_{h/q}(z)=\frac{z^{1-2\varepsilon}}{4N_c}\sum_X\int\frac{\dd w^-}{2\pi}\,\ee^{\ii k^+w^-}\Trc\TrD\Big[&\gamma^+\langle0|W[\infty n_B,w]\psi(w)|hX\rangle\\
&\times\langle hX|\bar\psi(0)W[0,\infty n_B]|0\rangle\Big],
\end{aligned}
\end{equation}"""),
(r"""\begin{equation}\label{eq:pdf-ffg}
d_{h/g}(z)=\frac{z^{1-2\varepsilon}}{(D-2)(N_c^2-1)k^+}\sum_X\int\frac{\dd w^-}{2\pi}\ee^{\ii k^+w^-}\sum_{j,a}\langle0|W^{(A)}_{ab}[\infty n_B,w]G^{+j}_b(w)|hX\rangle\langle hX|G^{+j}_c(0)W^{(A)}_{ca}[0,\infty n_B]|0\rangle,
\end{equation}""",
r"""\begin{equation}\label{eq:pdf-ffg}
\begin{aligned}
d_{h/g}(z)=\frac{z^{1-2\varepsilon}}{(D-2)(N_c^2-1)k^+}\sum_X\int\frac{\dd w^-}{2\pi}\ee^{\ii k^+w^-}\sum_{j,a}&\langle0|W^{(A)}_{ab}[\infty n_B,w]G^{+j}_b(w)|hX\rangle\\
&\times\langle hX|G^{+j}_c(0)W^{(A)}_{ca}[0,\infty n_B]|0\rangle,
\end{aligned}
\end{equation}"""),
(r"""\begin{equation}\label{eq:pdf-helicity}
\Delta f_{q/H}(\xi)=\int\frac{\dd w^-}{4\pi}\ee^{-\ii\xi P^+w^-}\langle P,+|\bar\psi(w)\gamma^+\gamma_5W[w,0]\psi(0)|P,+\rangle_{\mathrm c},\quad \Delta q(x)=\Delta f_q(x),\ \ \Delta\bar q(x)=+\Delta f_q(-x),
\end{equation}
$\gamma_5=""",
r"""\begin{equation}\label{eq:pdf-helicity}
\Delta f_{q/H}(\xi)=\int\frac{\dd w^-}{4\pi}\ee^{-\ii\xi P^+w^-}\langle P,+|\bar\psi(w)\gamma^+\gamma_5W[w,0]\psi(0)|P,+\rangle_{\mathrm c},
\end{equation}
$x>0$ 时 $\Delta q(x)=\Delta f_q(x)$，$\Delta\bar q(x)=+\Delta f_q(-x)$；$\gamma_5="""),
])
print('ok')
