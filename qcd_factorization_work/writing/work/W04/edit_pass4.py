# -*- coding: utf-8 -*-
# Pass 4 (writer W04): checker fixes.
#  - Ch4: prop:ir-glauber-trapping self-contained (no notation borrowed from ex:ir-vertex);
#         thm:ir-regions-euclid wording (C8b).
#  - App D: no cross-unit equation labels (WRITER_SPEC_v2 Sec. 5.4): restate the two Landau systems locally.
import os
ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..', '..'))

def fix(path, a, b, count=1):
    fn = os.path.join(ROOT, path)
    s = open(fn, encoding='utf-8').read()
    assert s.count(a) >= 1, (path, a[:70])
    if count == 'all':
        s = s.replace(a, b)
    else:
        s = s.replace(a, b, count)
    open(fn, 'w', encoding='utf-8').write(s)

P5 = 'writing/work/W04/parts/ch04_p5_glauber.tex'
fix(P5, "(a)~单圈无质量顶点（一条 $A$ 共线外线、一条 $B$ 共线外线，\\cref{ex:ir-vertex}的记号）在 Glauber 区没有钳夹点。",
    "(a)~单圈无质量顶点 $\\gamma^*(q)\\to q(p_1)\\bar q(p_2)$（$p_1=(p_1^+,0,\\mathbf 0_T)$，$p_2=(0,p_2^-,\\mathbf 0_T)$，"
    "分母 $D_0=k^2=2k^+k^--k_T^2$、$D_1=(p_1-k)^2=-2(p_1^+-k^+)k^--k_T^2$、$D_2=(p_2+k)^2=2k^+(p_2^-+k^-)-k_T^2$，各带 $+\\ii0$）"
    "在 Glauber 区没有钳夹点。")
fix(P5, "(a)~由\\cref{ex:ir-vertex}的分母，$D_0=0$ 与 $D_2=0$ 的 $k^-$ 根",
    "(a)~$D_0=0$ 与 $D_2=0$ 的 $k^-$ 根")

P7 = 'writing/work/W04/parts/ch04_p7_regions.tex'
fix(P7, "区域展开与已被证明的子图展开（渐近展开的子图形式）逐项一致",
    "区域展开与已有严格证明的子图展开（渐近展开的子图形式）逐项一致")

D = 'chapters/appD_landau.tex'
# restate the Landau systems in the introduction of App D
fix(D, "记号同\\cref{sec:ir-landau}：第 $j$ 条线的动量 $q_j=\\sum_l\\eta_{jl}k_l+r_j$，$D_j=q_j^2-m_j^2$，分母为 $D_j+\\ii0$。",
    "记号同\\cref{sec:ir-landau}：第 $j$ 条线的动量 $q_j=\\sum_l\\eta_{jl}k_l+r_j$，$D_j=q_j^2-m_j^2$，分母为 $D_j+\\ii0$；"
    "$\\mathcal D(\\alpha,k)=\\sum_j\\alpha_j(m_j^2-q_j^2)=-\\sum_{l,l'}A_{ll'}k_l\\cdot k_{l'}-2\\sum_lB_l\\cdot k_l+C$，"
    "$\\mathcal U$、$\\mathcal F$ 与驻点 $k_c(\\alpha)$ 如\\cref{def:ir-landau-setup}。为便于引用，把两组 Landau 方程重述如下：动量形式（$k$ 实，"
    "$\\alpha\\in\\mathbb R^N_{\\ge0}\\setminus\\{0\\}$）\n"
    "\\begin{equation}\\label{eq:appD-Lk}\n"
    "\\alpha_jD_j(k)=0\\quad(j=1,\\dots,N),\\qquad \\sum_j\\alpha_j\\eta_{jl}q_j^\\mu(k)=0\\quad(l=1,\\dots,L);\n"
    "\\end{equation}\n"
    "参数形式（$\\alpha$ 属于闭单形 $\\bar\\Delta$）\n"
    "\\begin{equation}\\label{eq:appD-La}\n"
    "\\mathcal F(\\alpha,p)=0,\\qquad \\alpha_j\\,\\partial_j\\mathcal F(\\alpha,p)=0\\quad(j=1,\\dots,N).\n"
    "\\end{equation}")
fix(D, "这正是\\cref{eq:ir-landau-k}。", "这正是\\cref{eq:appD-Lk}。")
fix(D, "\\paragraph{\\cref{eq:ir-param}的推导。}", "\\paragraph{参数表示（\\cref{def:ir-landau-setup}）的推导。}")
fix(D, "即\\cref{eq:ir-param}。被积函数的总次数", "即\\cref{def:ir-landau-setup}中的参数表示。被积函数的总次数")
fix(D, "由\\cref{eq:ir-quadform}，", "由\\cref{def:ir-landau-setup}中 $\\mathcal D$ 的形式，")
fix(D, "此即\\cref{eq:ir-envelope}。", "此即\\cref{lem:ir-envelope}的两个恒等式。")
fix(D, "($\\Rightarrow$)~若 $\\alpha$ 满足\\cref{eq:ir-landau-alpha}，则", "($\\Rightarrow$)~若 $\\alpha$ 满足\\cref{eq:appD-La}，则")
fix(D, "故 $(k_c,\\alpha)$ 满足\\cref{eq:ir-landau-k}。($\\Leftarrow$)~若 $(k,\\alpha)$ 满足\\cref{eq:ir-landau-k}，则",
    "故 $(k_c,\\alpha)$ 满足\\cref{eq:appD-Lk}。($\\Leftarrow$)~若 $(k,\\alpha)$ 满足\\cref{eq:appD-Lk}，则")
fix(D, "这是\\cref{eq:ir-landau-alpha}的解。按假设", "这是\\cref{eq:appD-La}的解。按假设")
fix(D, "即\\cref{eq:ir-landau-alpha}；再由\\cref{lem:ir-envelope}化为动量形式。", "即\\cref{eq:appD-La}；再由\\cref{lem:ir-envelope}化为动量形式\\cref{eq:appD-Lk}。")
fix(D, "设 $(k_0,\\alpha)$ 满足 $\\alpha_j\\ge0$ 的\\cref{eq:ir-landau-k}，", "设 $(k_0,\\alpha)$ 满足 $\\alpha_j\\ge0$ 的\\cref{eq:appD-Lk}，")
print('pass 4 done')
