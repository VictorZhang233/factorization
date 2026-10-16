# -*- coding: utf-8 -*-
# condense the Glauber section part (writer W04 tightening pass)
fn = 'parts/ch04_p5_glauber.tex'
s = open(fn, encoding='utf-8').read()

def cut(start, end_marker, new):
    global s
    i = s.index(start)
    j = s.index(end_marker, i)
    s = s[:i] + new + s[j:]

cut("软与超软区的幂次计数之所以简单", "\\begin{definition}[Glauber 区]",
    "软与超软区的计数之所以简单，是因为程函近似在那里成立：软动量流过共线线时，分母只通过一个光锥分量感知它。有一个领头区域不满足这一点。\n\n")

cut("Glauber 区的幂次计数与软、超软区相同：", "\\begin{proposition}[单圈 Glauber 区的钳夹判据 \\tagR]",
    "Glauber 区的幂次计数与软、超软区相同：在 $A$ 线与 $B$ 线之间交换一个胶子，Glauber 标度给出测度 $\\lambda^6$、"
    "胶子传播子 $\\lambda^{-2}$、两条线的分母各 $\\lambda^{-2}$，合计 $\\lambda^0$（软与超软标度分别给出 $\\lambda^{4-2-1-1}$ 与 "
    "$\\lambda^{8-4-2-2}$）。区别只在程函近似是否成立，所以关键在于 Glauber 区是否被钳住：若否，可把围道移到程函近似成立之处；"
    "若是，就必须另行处理。\n\n")

cut("(a)~由\\cref{ex:ir-vertex}的分母，", "(b)~被积函数在",
    "(a)~由\\cref{ex:ir-vertex}的分母，$D_0=0$ 与 $D_2=0$ 的 $k^-$ 根 $(k_T^2-\\ii0)/(2k^+)$、$-p_2^-+(k_T^2-\\ii0)/(2k^+)$ "
    "都是 $O(Q)$，$D_1=0$ 的根 $\\simeq-k_T^2/(2p_1^+)+\\ii0$ 为 $O(\\lambda^2Q)$（数值拟合指数 $0$、$0$、$2$）。所以窗口内只有 "
    "$D_1$ 的极点，$k^-$ 围道可以向下半平面推离它直到 $|k^-|\\sim k_T\\ll Q$；对 $k^+$ 同理只有 $D_2$ 的极点。这与"
    "\\cref{thm:ir-landau-momentum}一致：Glauber 区中 $D_0\\simeq-k_T^2\\ne0$，在壳线至多是 $D_1$、$D_2$，而 $u_1\\simeq-2p_1$ "
    "与 $u_2\\simeq2p_2$ 不能以非负系数相消，没有 Landau 点。\n")

i = s.index("(a) 的结论与 CSS 综述中对顶点 Glauber 区的分析一致")
new = (
    "(a) 与 CSS 综述对顶点 Glauber 区的分析一致：每个光锥变量只出现在一个分母里，积分不被钳住，可以形变到 $|k^\\pm|\\sim k_T$"
    "\\cite[第~8.4~节，式~(137)--(138)]{CollinsSoperSterman1989}。注意两个分量都要形变：只把 $k^-$ 推到 $|k^-|\\sim k_T$ "
    "而保持 $k^+\\sim\\lambda^2Q$，仍有 $|k^+k^-|\\sim\\lambda^3Q^2\\ll k_T^2$，并未离开 Glauber 区（误解 M31）；一般图中两个分量须沿 "
    "$e_G=n_B-n_A$ 协调形变（第~9~章的\\cref{rem:method-two-component}与\\cref{prop:method-glauber-deformation}）。(b) 是 Drell--Yan "
    "中初态与末态旁观者相互作用的情形：同一共线子图中携带 Glauber 动量的线既有在硬散射之前的、又有在其后的，Glauber 区被钳住，"
    "程函近似不能使用，必须借助对末态割线的求和（幺正性）另证其相消——这在第~9、12~章与附录~O 中完成。在光锥序微扰论中，"
    "Glauber 钳夹还可以出现在不同项之间（项间钳夹），它阻碍 Ward 恒等式的直接使用，这也是 Glauber 区必须在割图求和的层次上"
    "处理的原因之一。\n")
s = s[:i] + new
open(fn, 'w', encoding='utf-8').write(s)
print('ok', len(s))
