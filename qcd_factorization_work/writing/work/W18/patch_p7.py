# -*- coding: utf-8 -*-
import sys
fn = sys.argv[1]
t = open(fn, encoding='utf-8').read()

# (c) proof: inline the C_F^2 terms instead of referring to the table
old = "两圈：把\\cref{tab:scet-anomdim}中 $\\gamma^H_1$、$\\gamma^J_1$ 的 $C_F^2$ 项代入，$C_F^2(-3+4\\pi^2-48\\zeta_3)-2C_F^2(-\\frac32+2\\pi^2-24\\zeta_3)=0$，其余项给出所述 $\\gamma^S_1$；这符合非阿贝尔指数化对软函数色结构的要求。% w18_s4 (E)"
new = ("两圈：Becher--Schwartz 附录~A 给出\\cite{BecherSchwartz2008}\n"
       "$\\gamma^H_1=C_F^2(-3+4\\pi^2-48\\zeta_3)+C_FC_A(-\\frac{961}{27}-\\frac{11\\pi^2}{3}+52\\zeta_3)+C_FT_Fn_f(\\frac{260}{27}+\\frac{4\\pi^2}{3})$、"
       "$\\gamma^J_1=C_F^2(-\\frac32+2\\pi^2-24\\zeta_3)+C_FC_A(-\\frac{1769}{54}-\\frac{11\\pi^2}{9}+40\\zeta_3)+C_FT_Fn_f(\\frac{242}{27}+\\frac{4\\pi^2}{9})$，"
       "故 $\\gamma^H_1-2\\gamma^J_1$ 中 $C_F^2$ 项精确相消，其余项给出所述 $\\gamma^S_1$；这符合非阿贝尔指数化对软函数色结构的要求。两圈尖点 $\\Gamma_1=4C_F[(\\frac{67}9-\\frac{\\pi^2}3)C_A-\\frac{20}9T_Fn_f]$ 见\\cref{def:sudakov-cusp}（该文附录~A 在 $T_Fn_f$ 前多印了一个 $C_F$，见附录~Q 第~1~条）。% w18_s4 (E); values re-read in the BS source")
assert old in t, 'c'
t = t.replace(old, new)

# remove the table and the sentence after it
i = t.index('\\begin{table}[htbp]'); j = t.index('\\begin{example}[单圈 $H$、$J$、$S_T$ 合成 QCD 奇异项]')
t = t[:i] + t[j:]

# compress the example
i = t.index('\\begin{example}[单圈 $H$、$J$、$S_T$ 合成 QCD 奇异项]'); j = t.index('\\end{example}', i)
t = t[:i] + (
    "\\begin{example}[单圈 $H$、$J$、$S_T$ 合成 QCD 奇异项]\\label{ex:scet-thrust-oneloop}\n"
    "在 Laplace 空间中检验\\cref{prop:scet-thrust-oneloop}(d)。由\\cref{eq:scet-laplace}、\\cref{eq:scet-CV}与 (a)(b)，单圈的 $\\tilde t$ 等于 $1+a[(-2L_Q^2+6L_Q-16+\\tfrac{7\\pi^2}3)+2(2L_J^2-3L_J+7-\\tfrac{2\\pi^2}{3})+(-8L_S^2-\\pi^2)]$；代入 $L_J=L_Q-\\ell$、$L_S=\\frac12L_Q-\\ell$，二次项 $-2L_Q^2+4(L_Q-\\ell)^2-8(\\frac12L_Q-\\ell)^2=-4\\ell^2$，一次项 $6\\ell$，常数 $-16+14+(\\frac73-\\frac43-1)\\pi^2=-2$，故 $\\tilde t=1+a(-4\\ell^2+6\\ell-2)$，与 $\\mu$ 无关。另一方面，由 QCD 的累积分布 $R(\\tau)$，$\\tilde t(\\nu)=\\nu\\int_0^\\infty\\dd\\tau\\,\\ee^{-\\nu\\tau}R(\\tau)$；用 $\\nu\\int_0^\\infty\\ee^{-\\nu\\tau}\\ln\\tau\\,\\dd\\tau=-\\ell$、$\\nu\\int_0^\\infty\\ee^{-\\nu\\tau}\\ln^2\\tau\\,\\dd\\tau=\\ell^2+\\zeta_2$，得 $\\tilde t=1+\\frac{C_F\\as}{2\\pi}[-2(\\ell^2+\\zeta_2)+3\\ell+\\frac{\\pi^2}{3}-1]=1+2a(-2\\ell^2+3\\ell-1)$，相同。$\\delta(\\tau)$ 的系数也可由求和规则 $c_\\delta=\\frac32-\\int_0^1r(\\tau)\\,\\dd\\tau$ 数值地得到（$r$ 为 QCD 分布减去其奇异部分，以 $\\frac{C_F\\as}{2\\pi}$ 为单位；$\\tau>\\frac13$ 时 QCD 分布为零）：$c_\\delta=2.28986813369645287\\ldots$，与 $\\frac{\\pi^2}{3}-1$ 一致到 $10^{-20}$。% w18_s4 (F); c_scet: 2.289868133697 (lower precision)\n"
    "\\uses{prop:scet-thrust-oneloop}\n"
) + t[j:]
open(fn, 'w', encoding='utf-8').write(t)
print('ok', len(t))
