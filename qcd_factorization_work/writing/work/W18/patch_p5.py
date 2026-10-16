# -*- coding: utf-8 -*-
import sys
fn = sys.argv[1]
t = open(fn, encoding='utf-8').read()

i = t.index('\\paragraph{地位与缺口}'); j = t.index('\\begin{remark}[Glauber SCET 与光锥序证明的对照]')
t = t[:i] + (
    "\\paragraph{地位与缺口}\n"
    "算符的构造（(a)）是由匹配与幂次计数得到的全阶论证；(b)--(d) 是在单圈、两圈与梯形图求和中显式得到的，其对所有阶的推广被作者认为“非常可信”而没有证明\\cite[第~10~节]{RothsteinStewart2016}。作者明确指出旁观者相位的相消“taken alone it is far from a proof of factorization, even in the abelian case”（单独来看远不是因子化的证明，即使在阿贝尔情形）\\cite[第~11.1~节]{RothsteinStewart2016}，而 SCET 中完整的因子化证明需要证明 Glauber 拉氏量对硬散射没有贡献，将“在别处给出”\\cite[第~11~节]{RothsteinStewart2016}——据我们截至 2026 年 10 月的 INSPIRE 检索，尚未发表。因此最弱的一步是“$\\mathcal L_G$ 的效应在单举截面中相消”，它对应附录~O 的\\cref{asm:appO-mixing}(c) 与\\cref{asm:appO-deformation}；这是相消问题而不是幂次估计（作为幂次计数，(a) 只给出 E-S 型陈述）。对 $e^+e^-$ 的 $n$–$\\bar n$ 产生流只有单圈与两圈的显式证据\\cite[第~10~节]{RothsteinStewart2016}。在强子对撞中，Gaunt 发现对强子 $E_T$ 而言 CSS 的相消论证在两个旁观者 Glauber 胶子处失效\\cite{Gaunt2014}，Rothstein--Stewart 也认为当测量约束 $\\Delta p_\\perp$ 时旁观者交换从 $\\order{\\as^4}$ 起破坏因子化\\cite[第~11.1~节]{RothsteinStewart2016}；Schwartz--Yan--Zhu 对纯 Glauber 梯形图与任意红外安全的单标度观测量给出了全阶相消的论证，否定了这些论断中纯 Glauber 的部分，但不适用于多重微分的观测量\\cite{Schwartz:2018obd}（第~18、24~章，\\cref{prop:front-glauber-bfkl,prop:front-syz}）。升级途径：在有效理论中证明 $\\mathcal L_G$ 对单举观测量的贡献相消，即\\cref{thm:appO-main}去掉模型限制后的有效理论版本。\n\n"
) + t[j:]

i = t.index('最后一行的机制可以直接看到。'); j = t.index('\\end{remark}', i)
t = t[:i] + (
    "最后一行的机制如下。两条共线线交换两个 Glauber 胶子（圈动量 $k$）时，领头幂次的两个分母分别只含 $n\\cdot k=k^0-k^z$ 与 $\\bar n\\cdot k=k^0+k^z$：箱图中二者在复 $k^0$ 平面的零点分居实轴两侧，交叉箱图中位于同侧。正规子 $|2k^z|^{-\\eta}$ 只依赖于 $k^z$，因而可以先作 $k^0$ 积分：交叉箱图精确为零，箱图的 $k^z$ 积分只剩一个纯虚的 $\\delta$ 函数项（主值部分 $\\propto\\tan\\frac{\\pi\\eta}{2}\\to0$），即一个相位\\cite[第~5.2~节]{RothsteinStewart2016}。% w18_s5 (E1-E3)\n"
    "在附录~O 的语言中，这正是全部 $s$ 道权重落在非交叉次序上的“共同时序”，它是精确图给出的物理结果，而独立的对称截断给出 $p_{\\rm opp}=\\frac12$ 的截断假象（\\cref{rem:dy-common-ordering}）。\n"
) + t[j:]
open(fn, 'w', encoding='utf-8').write(t)
print('ok', len(t))
