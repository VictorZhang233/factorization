# -*- coding: utf-8 -*-
# Second trimming pass on Ch08 parts: prose only (no statements, proofs of [R] statements, \uses, status paragraphs, boxes).
import os, glob
here = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'parts')
files = sorted(glob.glob(os.path.join(here, 'ch08_p*.tex')))
texts = {f: open(f, encoding='utf-8').read() for f in files}

def rep(old, new):
    hits = [f for f in files if old in texts[f]]
    if len(hits) != 1:
        raise SystemExit('match count %d for: %s' % (len(hits), old[:70]))
    f = hits[0]
    if texts[f].count(old) != 1:
        raise SystemExit('multiple in file for: %s' % old[:70])
    texts[f] = texts[f].replace(old, new)

# 1. chapter intro
rep(r"""这一次序本身是严格性的要求：若把 PDF 定义为“DIS 中乘在系数函数前面的量”，普适性就成了定义而不是定理。用本书的标签表述：规范与推动不变性、自由场值（\cref{prop:pdf-invariance}）和 Wilson 线顶点的矩恒等式（\cref{lem:pdf-wilson-moments}）由算符定义直接推出（\tagR，$R_{\mathrm{def}}$）；微扰论中的支撑、PDF 的矩等于扭度 2 定域算符矩阵元、由算符重整化得到的 DGLAP 方程、领头阶核、由算符定义算出的单圈 $P_{qq}$、纯维数正规化中的部分子分布、定域算符的单圈反常维度与求和规则在重整化微扰论中严格（\tagR，$R_{\mathrm{PT}}$），推广到强子态另需\cref{asm:intro-wightman}、\cref{asm:intro-composite}；DIS 结构函数扭度 2 部分的 $x$ 空间因子化以 OPE 为前提而严格（\tagR，$R_{\mathrm{OPE}}$）；强子态的支撑与全阶的类时演化只有全阶论证（\tagA）；$\MSbar$ PDF 在某一非微扰标度以上的正定性是猜想（\tagC），而“在所有标度上非负”是错的。矩关系的全阶证明见\cref{app:appL}，所用的矩问题引理见\cref{app:appK}。""",
r"""这一次序本身是严格性的要求：若把 PDF 定义为“DIS 中乘在系数函数前面的量”，普适性就成了定义而不是定理。各结论的严格性等级见下面的方框；推广到强子态的结论另需\cref{asm:intro-wightman}、\cref{asm:intro-composite}。矩关系的全阶证明见\cref{app:appL}，所用的矩问题引理见\cref{app:appK}。""")

# 2. composition law paragraph (also removes a printed VF identifier)
rep(r"""其中用了合成律 $W[w,0]=W[w,\infty n_B]W[\infty n_B,0]$（VF-CONV-9）。由合成律与回溯律也有 $W[w,0]=W[w,-\infty n_B]W[-\infty n_B,0]$：对共线 PDF，Wilson 线伸向未来还是过去无关紧要，对横动量依赖分布则不然（\cref{rem:pdf-gauge-residual}）。""",
r"""其中用了合成律 $W[w,0]=W[w,\infty n_B]W[\infty n_B,0]$；同样 $W[w,0]=W[w,-\infty n_B]W[-\infty n_B,0]$，故对共线 PDF，Wilson 线伸向未来还是过去无关紧要（对横动量依赖分布则不然，\cref{rem:pdf-gauge-residual}）。""")

# 3. gluon interpretation
rep(r"""在 $A^+=0$ 规范中 $G^{+j}=\partial^+A^j$，算符 $\propto(k^+)^2A^jA^j$，因子 $1/(\xi P^+)=1/k^+$ 恰把它变成“胶子数”（与标量场的数密度 $\propto k^+|\phi|^2$ 同形）。一般规范中胶子密度来自组合 $k^+A^j-k^jA^+$，即 Grammer--Yennie 分解中胶子作为活动部分子时领头的 G 部分（比较\cref{prop:ir-super-leading}与第~9~章的\cref{prop:method-gy-suppression}）；$A^+=0$ 规范的陷阱在规范不变的写法里对应于 Wilson 线方向的选择（\cref{rem:pdf-gauge-residual}）。""",
r"""在 $A^+=0$ 规范中 $G^{+j}=\partial^+A^j$，因子 $1/(\xi P^+)=1/k^+$ 把算符 $\propto(k^+)^2A^jA^j$ 变成“胶子数”（与标量场的数密度 $\propto k^+|\phi|^2$ 同形）；一般规范中的组合 $k^+A^j-k^jA^+$ 即 Grammer--Yennie 分解中领头的 G 部分（比较\cref{prop:ir-super-leading}与第~9~章的\cref{prop:method-gy-suppression}）。""")

# 4. free-field example
rep(r"""给出 $\frac12\delta(\xi p^+-p^+)\cdot2p^+=\delta(1-\xi)$；反夸克靶的负号来自费米统计而非旋量（改用\cref{def:pdf-antiquark}中电荷共轭场的定义，直接得 $f^{(0)}_{\bar q/\bar q}=\delta(1-\xi)$）；胶子靶的两项落在 $\xi=\pm1$，$\xi f^{(0)}_{g/g}$ 是偶分布。各自由分布的矩为 $1$、$(-1)^n$、$1+(-1)^n$；而定域算符在同样的态中给出 $\langle p|\bar\psi\gamma^+(\ii\partial^+)^{n-1}\psi|p\rangle=2(p^+)^n$，反夸克 $-\bar v\gamma^+v(-p^+)^{n-1}=(-1)^n2(p^+)^n$，胶子 $\sum_j\langle k|G^{+j}(\ii\partial^+)^{n-2}G^{+j}|k\rangle=[1+(-1)^n](k^+)^n$——除以 $2(p^+)^n$ 后与矩逐一相等，这是\cref{thm:pdf-moments-local}在自由场上的特例；自由胶子的 $\int_0^1x\,g=1$ 即动量求和规则（\cref{prop:pdf-sum-rules}）。""",
r"""给出 $\frac12\delta(\xi p^+-p^+)\cdot2p^+=\delta(1-\xi)$；反夸克靶的负号来自费米统计而非旋量（用\cref{def:pdf-antiquark}中电荷共轭场的定义直接得 $f^{(0)}_{\bar q/\bar q}=\delta(1-\xi)$）。各自由分布的矩为 $1$、$(-1)^n$、$1+(-1)^n$；定域算符在同样的态中给出 $\langle p|\bar\psi\gamma^+(\ii\partial^+)^{n-1}\psi|p\rangle=2(p^+)^n$，反夸克 $-\bar v\gamma^+v(-p^+)^{n-1}=(-1)^n2(p^+)^n$，胶子 $\sum_j\langle k|G^{+j}(\ii\partial^+)^{n-2}G^{+j}|k\rangle=[1+(-1)^n](k^+)^n$——除以 $2(p^+)^n$ 后与矩逐一相等，这是\cref{thm:pdf-moments-local}在自由场上的特例；自由胶子的 $\int_0^1x\,g=1$ 即动量求和规则（\cref{prop:pdf-sum-rules}）。""")

# 5. Jaffe remark
rep(r"""$\mathcal A$ 是部分子—靶前向振幅（含其各种割法）。""", r"""$\mathcal A$ 是部分子—靶前向振幅。""")
rep(r"""Jaffe 的观察是：当 $\xi>1$ 时，与 $k^-$ 相关的中间态（靶取走一个部分子后的剩余部分）总加号动量 $(1-\xi)p^+$ 为负（$\xi<-1$ 时交换夸克与反夸克的角色），完成其余回路动量的减号分量积分后，$\mathcal A$ 作为 $k^-$ 的函数的奇点全在实轴同一侧；被积函数在 $|k^-|\to\infty$ 时足够快地衰减，向另一侧闭合围道即得零""",
r"""当 $\xi>1$ 时，靶取走一个部分子后的中间态总加号动量 $(1-\xi)p^+$ 为负（$\xi<-1$ 时交换夸克与反夸克的角色），完成其余回路的减号分量积分后，$\mathcal A$ 作为 $k^-$ 的函数的奇点全在实轴同一侧；被积函数在 $|k^-|\to\infty$ 时足够快地衰减，向另一侧闭合围道即得零""")
rep(r"""微扰论中它与\cref{thm:pdf-support-pt}等价：两者都是“中间态加号动量非负”的不同表述。""",
r"""微扰论中它与\cref{thm:pdf-support-pt}等价，两者都表述“中间态加号动量非负”。""")

# 6. interpretation section intro
rep(r"""算符定义的直观含义来自光锥规范 $A^+=0$：此时 $W[w,0]=1$，好分量的光前量子化把\cref{eq:pdf-fq}变成产生、湮灭算符的期望值。这一读法只是启发式的，它恰恰是“$\MSbar$ PDF 是概率、故为正”这一误解的来源。

""", r"""算符定义的直观读法来自光锥规范 $A^+=0$（此时 $W[w,0]=1$）；它只是启发式的，并且正是“$\MSbar$ PDF 是概率、故为正”这一误解的来源。

""")

# 7. gauge-residual remark
rep(r"""相应地，传播子分子在 $k^+=0$ 的奇异性需要处方（主值、$k^+\pm\ii0$、Mandelstam--Leibbrandt 等），每种处方等价于对 $\bm A_{\mathrm T}$ 在 $x^-=\pm\infty$ 的一种边界条件。共线 PDF 的 Wilson 线是横向位置相同的\emph{有限}类光线段，$W[w,0]=W[w,\pm\infty n_B]W[\pm\infty n_B,0]$，连接两条半无限线的无穷远横向连接是平凡的，故结果与处方无关；横动量依赖分布的订书钉形 Wilson 线两端横向位置不同，无穷远横向连接依赖于边界条件（第~14~章）。最后，常见论证“用规范变换把 $W$ 变成 $1$”中的 $U(x)=W[\infty n_B,x]$ 是依赖于场的算符而非整体规范变换；结论之所以仍成立，是因为它只用到 $W[w,\infty n_B]W[\infty n_B,0]=W[w,0]$。""",
r"""相应地，传播子在 $k^+=0$ 的奇异性需要处方（主值、$k^+\pm\ii0$、Mandelstam--Leibbrandt 等），每种处方等价于对 $\bm A_{\mathrm T}$ 在 $x^-=\pm\infty$ 的一种边界条件。共线 PDF 的 Wilson 线是横向位置相同的\emph{有限}类光线段，$W[w,0]=W[w,\pm\infty n_B]W[\pm\infty n_B,0]$，无穷远横向连接平凡，故结果与处方无关；横动量依赖分布的订书钉形 Wilson 线两端横向位置不同，结果依赖于边界条件（第~14~章）。常见论证“用规范变换把 $W$ 变成 $1$”中的 $U(x)=W[\infty n_B,x]$ 是依赖于场的算符而非整体规范变换；结论仍成立，只因它用到的仅是合成律。""")

# 8. moments section intro
rep(r"""把它与本章的定义联系起来的桥梁是“PDF 的 $n$ 阶矩 $=A^{(n)}$”。这在两个层次上成立：对裸算符，它是光线算符在 $w^-=0$ 处的 Taylor 展开；对重整化的量，它要求 PDF 重整化核的矩恰为定域算符的重整化常数。""",
r"""与本章定义的桥梁是“PDF 的 $n$ 阶矩 $=A^{(n)}$”：对裸算符，它是光线算符在 $w^-=0$ 处的 Taylor 展开；对重整化的量，它要求 PDF 重整化核的矩恰为定域算符的重整化常数。""")

# 9. three remarks after the moment theorem
rep(r"""(iii) 本定理之后，\cref{thm:dis-moments}中的 $A^{(n)}_i$ 就是本章 PDF 的矩；对强子态，矩关系本身是\cref{asm:intro-composite}(C3) 的一部分——微扰论中它是定理，非微扰地它是假设。""",
r"""(iii) 本定理之后，\cref{thm:dis-moments}中的 $A^{(n)}_i$ 就是本章 PDF 的矩；对强子态，矩关系是\cref{asm:intro-composite}(C3) 的一部分。""")

# 10. ladder paragraph (the caption carries the details)
rep(r"""\cref{eq:pdf-dglap}的物理图像见\cref{fig:dglap-ladder}：在物理规范中，领头对数来自横动量强序的梯形图，每级分裂贡献 $\frac{\as}{2\pi}\int\frac{\dd k_{\mathrm T}^2}{k_{\mathrm T}^2}P(z_i)$，$n$ 级强序积分的体积为 $\frac1{n!}(\ln\frac{Q^2}{\mu_0^2})^n$，连同虚修正对 $n$ 求和即得固定耦合下领头阶 DGLAP 的解。这只是图像，定理是\cref{thm:pdf-dglap}。""",
r"""\cref{eq:pdf-dglap}的物理图像见\cref{fig:dglap-ladder}：在物理规范中，领头对数来自横动量强序的梯形图。这只是图像，定理是\cref{thm:pdf-dglap}。""")

# 11. paragraph after the LO-kernel proof
rep(r"""$\delta$ 项也可直接由虚图得到，两条路一致：$qq$ 道见\cref{prop:pdf-pqq-operator}（$\frac32=2-\frac12$，$2$ 来自 Wilson 线图、$-\frac12$ 来自夸克场重整化），$gg$ 道的 $\frac{\beta_0}2$ 在\cref{prop:pdf-local-anomalous}中来自 $\delta Z_3$ 与算符—胶子图之和；上面用到的两条守恒律在单圈也在那里逐图验证（$N=1$ 时 $\Gamma_{qq}=0$，$N=2$ 时两列之和为零）。例如领头阶非单态，MVV 的""",
r"""$\delta$ 项也可直接由虚图得到，两条路一致：$qq$ 道见\cref{prop:pdf-pqq-operator}（$\frac32=2-\frac12$），$gg$ 道的 $\frac{\beta_0}2$ 见\cref{prop:pdf-local-anomalous}。领头阶非单态时，MVV 的""")
rep(r"""都等于本书的 $\gamma_{qq}(N)$ 乘以 (e) 中的因子；""", r"""都等于 $\gamma_{qq}(N)$ 乘以 (e) 中的因子；""")

# 12. one-loop section intro
rep(r"""本节在 Feynman 规范下直接由\cref{eq:pdf-fq}算出夸克中夸克分布的单圈值。与光锥规范的计算相比，这里 Wilson 线显式出现，规范不变性逐步可见，每个图的紫外极点可以单独读出。""",
r"""本节在 Feynman 规范下直接由\cref{eq:pdf-fq}算出夸克中夸克分布的单圈值；Wilson 线显式出现，每个图的紫外极点可以单独读出。""")

# 13. one-loop example
rep(r"""按\cref{fig:pdf-oneloop}逐图：R1 给出 $A_\varepsilon(1-\varepsilon)^2(1-\xi)\xi^{-\varepsilon}$（极点 $1-\xi$），R2 与 V1 给出 $A_\varepsilon[\frac{2\xi^{1-\varepsilon}}{1-\xi}]_+$（极点 $[\frac{2\xi}{1-\xi}]_+$），V2 给出 $-A_\varepsilon\frac{1-\varepsilon}{2-\varepsilon}\delta(1-\xi)$（极点 $-\frac12\delta$），(d) 为零。$\delta$ 项的来源一目了然：$\frac32=2-\frac12$，$2$ 来自把 R2 与 V1 的组合改写为标准形式，$-\frac12$ 来自夸克场重整化，梯形图不含 $\delta$ 项。""",
r"""按\cref{fig:pdf-oneloop}逐图：R1 给出 $A_\varepsilon(1-\varepsilon)^2(1-\xi)\xi^{-\varepsilon}$，R2 与 V1 给出 $A_\varepsilon[\frac{2\xi^{1-\varepsilon}}{1-\xi}]_+$，V2 给出 $-A_\varepsilon\frac{1-\varepsilon}{2-\varepsilon}\delta(1-\xi)$，(d) 为零；$\delta$ 项 $\frac32=2-\frac12$ 中，$2$ 来自把 R2 与 V1 的组合改写为标准形式，$-\frac12$ 来自夸克场重整化，梯形图不含 $\delta$ 项。""")
rep(r"""正是 DGLAP 所要求的 $\mu$ 依赖。重整化结果的夸克数检验：""", r"""正是 DGLAP 所要求的 $\mu$ 依赖。夸克数检验：""")
rep(r"""有限部分依赖于红外正规化（纯维数正规化下为零，\cref{prop:pdf-partonic-dr}）；只有紫外极点与 $\ln\mu^2$ 的系数与正规化无关。""",
r"""有限部分依赖于红外正规化（纯维数正规化下为零，\cref{prop:pdf-partonic-dr}），只有紫外极点与 $\ln\mu^2$ 的系数与正规化无关。""")

# 14. quark-in-gluon example
rep(r"""无质量夸克的纯维数正规化中裸分布为零（无标度），$\MSbar$ 分布是纯红外极点 $-\frac{\as}{2\pi}\frac1\varepsilon P_{qg}$。为看清极化平均约定的作用，给夸克质量 $m$。$A^+=0$ 规范的直接计算""",
r"""无质量夸克的纯维数正规化中 $\MSbar$ 分布是纯红外极点 $-\frac{\as}{2\pi}\frac1\varepsilon P_{qg}$。为看清极化平均约定的作用，给夸克质量 $m$，$A^+=0$ 规范的直接计算""")
rep(r"""$\MSbar$ 重整化后 $f^{(1)}_{Q/g}=\frac{\as}{2\pi}P_{qg}(z)\ln\frac{\mu^2}{m^2}$，没有常数项。若把胶子极化平均改为 $\frac12$，结果乘以 $\frac{D-2}{2}=1-\varepsilon$，$\MSbar$ 分布变为 $\frac{\as}{2\pi}P_{qg}[\ln\frac{\mu^2}{m^2}-1]$：极化平均约定确是 $\MSbar$ 方案的一部分（\cref{def:pdf-gluon}）。顺带注意，$\mu<m$ 时这个 $\MSbar$ 重夸克分布是负的：$\MSbar$ 分布不必为正，在微扰论中就有初等的例子（\cref{conj:pdf-positivity}）。""",
r"""$\MSbar$ 重整化后 $f^{(1)}_{Q/g}=\frac{\as}{2\pi}P_{qg}(z)\ln\frac{\mu^2}{m^2}$，没有常数项；若把胶子极化平均改为 $\frac12$，结果乘以 $\frac{D-2}{2}=1-\varepsilon$，$\MSbar$ 分布变为 $\frac{\as}{2\pi}P_{qg}[\ln\frac{\mu^2}{m^2}-1]$：极化平均约定是 $\MSbar$ 方案的一部分（\cref{def:pdf-gluon}）。$\mu<m$ 时这个 $\MSbar$ 重夸克分布是负的：$\MSbar$ 分布不必为正，微扰论中就有初等的例子（\cref{conj:pdf-positivity}）。""")

# 15. DIS section intro
rep(r"""两者加上矩问题的唯一性（\cref{app:appK}），就得到结构函数扭度 2 部分在 $x$ 空间的因子化。它是严格的，但只到所陈述的程度：被控制的是扭度 2 部分，余项只在矩的意义下是 $\order{1/Q^2}$。""",
r"""加上矩问题的唯一性（\cref{app:appK}），就得到结构函数扭度 2 部分在 $x$ 空间的因子化；被控制的只是扭度 2 部分，余项只在矩的意义下是 $\order{1/Q^2}$。""")

# 16. DIS proof: remove the printed VF identifier
rep(r"""（VF-DIS-6；胶子道的因子 $2$ 来自每味的夸克与反夸克）""", r"""（胶子道的因子 $2$ 来自每味的夸克与反夸克）""")

# 17. after the DIS theorem
rep(r"""由 DGLAP（\cref{thm:pdf-dglap}）可验证 $\partial F_2^{\mathrm{tw2}}/\partial\ln\mu^2=\order{\as^2}$：每味 $q+\bar q$ 以 $P_{qq}$ 与 $2P_{qg}$ 演化，恰被 $\partial L/\partial\ln\mu^2=-1$ 的项抵消。""",
r"""由\cref{thm:pdf-dglap}可验证 $\partial F_2^{\mathrm{tw2}}/\partial\ln\mu^2=\order{\as^2}$（与 $\partial L/\partial\ln\mu^2=-1$ 的项抵消）。""")

# 18. schemes remark
rep(r"""DIS 方案是合法的方案选择；但若把 PDF \emph{定义}为“$F_2$ 中的那个量”，其他过程中的普适性就成了定义而非定理——这正是本章先给出算符定义的原因。""",
r"""DIS 方案是合法的方案选择；但若把 PDF \emph{定义}为“$F_2$ 中的那个量”，其他过程中的普适性就成了定义而非定理。""")

# 19. FF section intro
rep(r"""碎裂函数描述一个高能部分子产生动量份额为 $z$ 的强子 $h$ 的“数密度”。其算符定义与 PDF 平行，但有两处本质差别：被观测的强子在\emph{末态}，对其余末态 $X$ 的求和夹在两个场之间；以及由此带来的参考系与归一问题。""",
r"""碎裂函数描述高能部分子产生动量份额为 $z$ 的强子 $h$ 的“数密度”。其算符定义与 PDF 平行，但被观测的强子在\emph{末态}，对其余末态 $X$ 的求和夹在两个场之间，并由此带来参考系与归一问题。""")

# 20. verification note inside the local-anomalous proof becomes a comment
rep(r"""两列之和为零。各图的值对 $N=1,\dots,14$ 用两种独立方法核对过：显式 $4\times4$ Dirac 矩阵与平面波顶点，以及 $D$ 维迹与 Feynman 参数的符号计算。""",
r"""两列之和为零。
% (graph values cross-checked for N=1..14 with explicit 4x4 Dirac matrices and with D-dim traces; writing/work/W09/v9_local_ops.py)""")

# 21. chapter summary
rep(r"""PDF 的矩是扭度 2 定域算符的矩阵元，其重整化核的矩恰为定域算符的重整化常数（全阶证明只用定域算符的重整化理论，\cref{app:appL}）；DGLAP 由算符重整化得出，领头阶核可由光锥规范的实辐射或 Feynman 规范中带 Wilson 线的逐图计算得到，后者与定域算符的单圈计算逐图对应；求和规则来自守恒流；""",
r"""PDF 的矩是扭度 2 定域算符的矩阵元，其重整化核的矩恰为定域算符的重整化常数（\cref{app:appL}）；DGLAP 由算符重整化得出，Feynman 规范中带 Wilson 线的单圈计算与定域算符的单圈计算逐图对应；求和规则来自守恒流；""")

for f in files:
    open(f, 'w', encoding='utf-8').write(texts[f])
print('trim2 ok')
