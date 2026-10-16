# -*- coding: utf-8 -*-
p = 'parts/ch03_p6.tex'
s = open(p, encoding='utf-8').read()
i = s.index('\\paragraph{本章小结}')
j = s.index('\\begin{table}')
new = r"""\paragraph{本章小结}
沿 $z$ 轴的推动把光锥分量乘以 $\ee^{\pm\eta}$、把好/坏旋量分量乘以 $\ee^{\pm\eta/2}$（\cref{lem:prelim-boost}），这是幂次计数的出发点。Wilson 线是规范协变的平行移动算符（\cref{prop:prelim-wilson-covariance}），其动量空间规则由一条统一规则给出，未来与过去指向的线相差 $2\pi\ii\,\delta(n\cdot k)$（\cref{prop:prelim-wilson-rules}）；程函恒等式在绝热正规化下精确成立（\cref{lem:prelim-eikonal-identity}），并把高能部分子与软胶子的耦合等同于 Wilson 线（\cref{ex:prelim-eikonal-two}）。维数正规化的每个极点都要标明来源，无标度积分为零（\cref{lem:prelim-scaleless,ex:prelim-scaleless}）。加号分布与 $(1-z)^{-1-a\varepsilon}$ 的展开组织了单圈实辐射（\cref{lem:prelim-plus-expansion}），Mellin 变换把卷积化为乘积（\cref{lem:prelim-mellin}），矩只把 $x$ 空间的对象确定为分布（\cref{rem:prelim-moment-tools}）。切割规则、物理幺正性与光学定理（\cref{thm:prelim-cutting-rules,prop:prelim-unitarity,prop:prelim-optical}）把截面与前向振幅的虚部联系起来；无质量维数正规化中的割图规则是全阶论证（\cref{rem:prelim-cutting-dr}，\tagA）。

\paragraph{这些工具在后文的用途}
光锥坐标与推动引理用于第~4~章的区域标度与幂次计数（\cref{def:ir-scalings}、\cref{prop:ir-power-counting}）。Wilson 线出现在部分子分布的定义（\cref{def:pdf-quark}）、尖点反常维度（\cref{def:sudakov-cusp}）、共线与软近似（\cref{def:method-collinear-approx}、\cref{def:method-soft-approx}）、多胶子 Ward 恒等式（\cref{lem:method-ward-multi}）与 TMD 的定义（\cref{def:tmd-unsub}）中。维数正规化的记账用于\cref{prop:sudakov-oneloop}与\cref{prop:pdf-partonic-dr}，$\gamma_5$ 的约定用于\cref{thm:dis-bjorken}与\cref{thm:coll-g1-moments}。加号分布与 Mellin 变换用于分裂函数（\cref{prop:pdf-lo-kernels}）、次领头阶系数函数（\cref{prop:disall-nlo}、\cref{prop:dy-nlo}）与阈值区（\cref{prop:thr-oneloop}）；矩问题的工具用于\cref{cor:dis-weak-xspace}、\cref{rem:dis-nonuniform}与\cref{rem:pdf-ns-plusminus}。割图与光学定理是\cref{thm:ee-R-finite}、\cref{prop:dis-dispersion}、\cref{prop:method-fsi}与\cref{lem:method-soft-unitarity}的基础，其光锥形式在附录~O 中证明。

"""
s = s[:i] + new + s[j:]
# compact table: footnotesize, fewer rows
s = s.replace("\\small\n\\renewcommand{\\arraystretch}{1.12}", "\\footnotesize\n\\renewcommand{\\arraystretch}{1.05}")
for row in ["$y$ & 快度 $\\frac12\\ln(k^+/k^-)$ & \\cref{def:prelim-lightfront} \\\\\n",
            "$\\tilde A(k)$ & 胶子场的 Fourier 分量，$k$ 流入 Wilson 线 & \\cref{def:prelim-wilson} \\\\\n",
            "$\\delta^+(p^2-m^2)$ & 割线的在壳条件 $\\theta(p^0)\\delta(p^2-m^2)$ & \\cref{def:prelim-cut} \\\\\n"]:
    assert row in s, row
    s = s.replace(row, "")
s = s.replace("$v^\\pm$，$\\mathbf v_{\\mathrm T}$ & 光锥分量 $(v^0\\pm v^3)/\\sqrt2$，横向分量 $(v^1,v^2)$ & \\cref{def:prelim-lightfront} \\\\",
              "$v^\\pm$，$\\mathbf v_{\\mathrm T}$，$y$ & 光锥分量 $(v^0\\pm v^3)/\\sqrt2$，横向分量，快度 $\\frac12\\ln(k^+/k^-)$ & \\cref{def:prelim-lightfront} \\\\")
s = s.replace("$W^{(A)}_{ab}$ & 伴随表示的 Wilson 线 $2\\Tr[t^aWt^bW^\\dagger]$ & \\cref{def:prelim-wilson} \\\\",
              "$W^{(A)}_{ab}$，$\\tilde A(k)$ & 伴随 Wilson 线 $2\\Tr[t^aWt^bW^\\dagger]$；胶子场的 Fourier 分量（$k$ 流入） & \\cref{def:prelim-wilson} \\\\")
open(p, 'w', encoding='utf-8').write(s)
print('p6 ok')
