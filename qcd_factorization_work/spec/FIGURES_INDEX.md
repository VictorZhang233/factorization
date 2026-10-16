# FIGURES_INDEX — figures of 《QCD 因子化定理：严格证明、全阶论证与适用边界》

The spec synthesizer built this index on 2026-10-10. It binds together with `WRITER_SPEC.md` §7.

## 0. Rules

1. **One owner.** Every figure belongs to exactly one owning chapter (column "owner"). Only the owner includes the `figure` environment. Every other chapter refers to it with `\cref{fig:...}`, e.g. 「见\cref{fig:reduced-dis}」.
2. **Existing figures are copied verbatim.**
   - Copy the whole block from `%%% BEGIN fig:<name>` to `%%% END fig:<name>` out of the source file, including `\begin{figure}`, the caption and the label. Do not edit coordinates, styles or captions.
   - If you think a caption is wrong (convention, sign), keep it and report it under "figure issues" in your final report.
3. **tikz1 is final; tikz2 and tikz3 are being redone.**
   - `research/tikz1/figures1.tex` is final.
   - `research/tikz2/figures2.tex` and `research/tikz3/figures3.tex` are being redone. On 2026-10-10 at 13:49 both files contained all 16 of their labels and compiled without errors (`test_figures2.log`, `test_figures3.log`).
   - At writing time, copy the **then-current** block. If the file or block is missing or does not compile, use the placeholder protocol (rule 4) and list the label in your report.
4. **Placeholder protocol.** Insert the following, keeping the canonical label so that `\cref` works:
   ```latex
   \begin{figure}[htbp]\centering
   \fbox{\parbox{0.8\textwidth}{\centering\vspace{2cm}图待补：fig:<name>（见 FIGURES\_INDEX）\vspace{2cm}}}
   \caption{<the caption draft from this index>}\label{fig:<name>}
   \end{figure}
   ```
5. **New figures.**
   - Draw them in plain TikZ (or pgfplots for function plots) with the styles already defined in `common/preamble_fact.tex`. These include `fd`, `quark`, `gluon`, `photon`, `ghost`, `wilson`, `cut`, `hard blob`, `jet blob`, `jetB blob`, `soft blob`, `hadron blob`, `glauber`, `opvertex`, `scalar`, `longit` with `\longitmark`, `lcaxis`, `region`, `mom`, `vertex`, `blob` and `bound state`.
   - Do not load new packages or TikZ libraries beyond those in the preamble.
   - Wrap each new figure in `%%% BEGIN fig:<label>` / `%%% END fig:<label>` comments, so that the lead author can extract it.
   - Width at most `\textwidth`. Fonts: `\small` or the `fd` default. Colours as in the styles, light enough for greyscale print.
6. **Adapting agent snippets.** When a new figure is adapted from a research agent's snippet (column "start from"), do three things:
   - rename its label to the canonical one;
   - check its conventions against WRITER_SPEC §3 ($n_A,n_B$; arrows = fermion number; momentum arrows; $\pm i0$ statements in the caption);
   - render it and inspect the PNG (WRITER_SPEC §9).
7. **Renders to look at before writing.**
   - tikz1: `research/tikz1/png/`.
   - tikz2: `research/tikz2/render/`.
   - tikz3: `research/tikz3/png/`.
   - The test PDFs `test_figures{1,2,3}.pdf`.

**Counts.**
- Existing figures: **44** (tikz1 12, tikz2 16, tikz3 16).
- New required figures: **29** (audit: `fig:disall-seed`, `fig:disall-heavy`, `fig:dy-abelian-model` promoted from optional).
- New optional figures: **10**.
- Every chapter Ch1–Ch22 has at least two required figures, existing or new (table in §4).

---------------------------------------------------------------------------------------------------

## 1. Existing figures (44)

| # | label | source | owner | also referenced from | content (from caption) |
|---|---|---|---|---|---|
| 1 | `fig:parton-model` | tikz1 | Ch1 | Ch6, Ch7 | 部分子模型图像：静止系 vs 无穷动量系；时间膨胀 |
| 2 | `fig:dis-kinematics` | tikz1 | Ch6 | Ch9 | DIS 运动学 $\ell+A\to\ell'+X$ |
| 3 | `fig:handbag` | tikz1 | Ch1 | Ch6 | 部分子模型的手提包割图 |
| 4 | `fig:forward-compton` | tikz1 | Ch6 | — | 前向 Compton 振幅（$s$ 道与 $u$ 道） |
| 5 | `fig:omega-plane` | tikz1 | Ch6 | — | $\omega$ 复平面、割线与围道 |
| 6 | `fig:ope-schematic` | tikz1 | Ch6 | Ch21 | 光锥 OPE 示意 |
| 7 | `fig:pdf-operator` | tikz1 | Ch7 | Ch8 | 夸克分布的割图表示 |
| 8 | `fig:pdf-oneloop` | tikz1 | Ch7 | App G | PDF 单圈图（实辐射、Wilson 线、虚修正） |
| 9 | `fig:dglap-ladder` | tikz1 | Ch7 | Ch16 | LLA 梯形图 |
| 10 | `fig:splitting-vertices` | tikz1 | Ch7 | — | 四种 $1\to2$ 分裂 |
| 11 | `fig:dis-oneloop` | tikz1 | Ch6 (audit; was Ch9) | Ch9, App G | DIS 的 $O(\alpha_s)$ 图 |
| 12 | `fig:factorization-schematic` | tikz1 | Ch1 | Ch8, Ch11 | 强子—强子共线因子化示意 |
| 13 | `fig:landau-pinch` | tikz2 | Ch3 | App D | 复 $k^-$ 平面：端点、非钳夹、钳夹 |
| 14 | `fig:vertex-regions` | tikz2 | Ch3 | Ch4 | 单圈顶点的三个钳夹面 |
| 15 | `fig:coleman-norton` | tikz2 | Ch3 | App D | Coleman–Norton 时空图像 |
| 16 | `fig:reduced-ee` | tikz2 | Ch3 | Ch5, Ch14 | $e^+e^-$ 两喷注约化割图 |
| 17 | `fig:reduced-dis` | tikz2 | Ch3 (audit; was Ch9) | Ch9, App E | DIS 约化割图 |
| 18 | `fig:reduced-dy` | tikz2 | Ch3 (audit; was Ch11) | Ch11, Ch13 | DY 约化割图 |
| 19 | `fig:momentum-regions` | tikz2 | Ch3 | Ch13, Ch14 | $(\ln k^+,\ln k^-)$ 平面上的区域 |
| 20 | `fig:ward-identity` | tikz2 | Ch8 | App F | 图示 Ward 恒等式（K 胶子 → Wilson 线） |
| 21 | `fig:soft-eikonal` | tikz2 | Ch2 (audit; was Ch8) | Ch8 | 软胶子程函近似；出射/入射夸克 ↔ 未来/过去指向 Wilson 线 |
| 22 | `fig:ee-oneloop` | tikz2 | Ch5 | App G | $e^+e^-$ $O(\alpha_s)$：振幅图与 $\Pi$ 的两圈图及切割 |
| 23 | `fig:dy-oneloop` | tikz2 | Ch11 | App G | DY $O(\alpha_s)$ 部分子图 |
| 24 | `fig:glauber-exchange` | tikz2 | Ch11 | Ch17 | Glauber 交换：DY 旁观者 vs SIDIS/DIS |
| 25 | `fig:glauber-contour` | tikz2 | Ch8 | Ch11 | 复 $k^-$ 平面中的 Glauber 区分析 |
| 26 | `fig:sudakov-ff` | tikz2 | Ch4 | Ch3 (pointer only) | 离壳 Sudakov 形状因子的区域展开 |
| 27 | `fig:scet-wilson` | tikz2 | Ch14 | — | SCET 中的 $W_n$ 与 $Y_n$ |
| 28 | `fig:dijet-factorization` | tikz2 | Ch14 | Ch15 | 推力分布 $H\,J\otimes J\otimes S$ |
| 29 | `fig:tmd-staple` | tikz3 | Ch13 | Ch17, Ch21 | TMD 算符的订书钉形 Wilson 线 |
| 30 | `fig:tmd-soft-factor` | tikz3 | Ch13 | — | TMD 软因子的割图表示 |
| 31 | `fig:tmd-dy` | tikz3 | Ch13 | — | 小 $q_T$ DY 的约化割图与 TMD 因子化 |
| 32 | `fig:sidis-dy-links` | tikz3 | Ch13 | Ch20 | 单胶子交换决定 Wilson 线方向（SIDIS vs DY） |
| 33 | `fig:violation-cq` | tikz3 | Ch17 | — | Collins–Qiu 机制 |
| 34 | `fig:diffraction` | tikz3 | Ch17 | Ch10 (pointer only) | 衍射 DIS vs 强子—强子衍射 |
| 35 | `fig:pion-ff` | tikz3 | Ch18 | — | $\pi$ 形状因子领头阶硬散射 |
| 36 | `fig:dvcs-handbag` | tikz3 | Ch18 | — | DVCS 手提包图与交叉图 |
| 37 | `fig:meson-production` | tikz3 | Ch18 | — | 纵向光子介子产生 |
| 38 | `fig:nrqcd` | tikz3 | Ch19 | — | NRQCD 产生的因子化图像 |
| 39 | `fig:bfkl-ladder` | tikz3 | Ch16 | — | 小 $x$：割开的胶子梯形图（BFKL） |
| 40 | `fig:renormalon-chain` | tikz3 | Ch20 | — | 重整化子链图（大 $\beta_0$） |
| 41 | `fig:higher-twist` | tikz3 | Ch6 (audit; was Ch20) | Ch20 | DIS 强子张量的扭度展开 |
| 42 | `fig:twist3-ssa` | tikz3 | Ch20 | Ch13 (pointer only) | Qiu–Sterman 软胶子极点机制 |
| 43 | `fig:dps` | tikz3 | Ch17 | — | 双部分子散射（双 DY） |
| 44 | `fig:quasi-pdf` | tikz3 | Ch21 | — | 准 PDF 与光锥 PDF 的时空图 |

Notes on the existing figures:
- **Ownership = first use (audit).** A figure is owned by the first chapter that uses it, so that no chapter needs a figure printed later. The audit therefore moved `fig:reduced-dis`, `fig:reduced-dy` to Ch3 (where reduced diagrams are introduced), `fig:dis-oneloop`, `fig:higher-twist` to Ch6, and `fig:soft-eikonal` to Ch2. Remaining references to later figures (`fig:sudakov-ff` from Ch3, `fig:diffraction` from Ch10, `fig:twist3-ssa` from Ch13) are pointers only, never needed for the argument.
- **Ch14.** A writer of Ch14 who needs a reduced diagram refers back to `fig:reduced-ee`.
- **`fig:pdf-operator`.** Its caption writes $w=w^-n$ with $n\cdot v=v^+$ (Collins' $w_2=n_B$). This agrees with WRITER_SPEC §3.
- **`fig:sidis-dy-links`.** It uses $n$ with $n\cdot v=v^+$ ($=n_B$); acceptable as is.
- **Captions with $n,\bar n$ outside Ch14 (audit).** Captions are copied verbatim, but their $n$ does not always mean the same thing: in `fig:momentum-regions` (Ch3) and `fig:sudakov-ff` (Ch4) $n$ is the direction of hadron/jet $A$ (our $n_A$) and $\bar n$ is our $n_B$; in `fig:pdf-operator` (Ch7), `fig:tmd-staple` and `fig:sidis-dy-links` (Ch13) $n$ is the vector with $n\cdot v=v^+$, i.e. our $n_B$; in `fig:soft-eikonal` (Ch2) $n$ is the direction of the quark momentum $p$. The owning writer adds one sentence in the text at the first reference, e.g. 「（图中 $n$、$\bar n$ 即本书的 $n_A$、$n_B$）」, and lists it under "figure issues". If tikz2/tikz3 are still being redone, the lead author may ask the figure agents to switch these captions to $n_A,n_B$.

---------------------------------------------------------------------------------------------------

## 2. New figures — required (29; entries 1–26 plus 26a–26c added by the audit)

Format of each entry:
- label · owner (section) · type;
- **draw:** what to draw;
- **caption draft** (Chinese);
- **start from:** an agent snippet to adapt, if there is one.

### Ch1
1. **`fig:intro-dependency`** · Ch1 (`sec:intro-organisation`) · TikZ graph, full width, about 9 cm high.
   - **Draw:** a left-to-right dependency graph of the main canonical results. Use rounded-rectangle nodes, each holding the short Chinese name plus the label number placeholder `\cref{...}` (the writer may use short names only). The fill colour encodes the tag with the colours of `\tagR\tagA\tagP\tagC\tagV` (OliveGreen, RoyalBlue, BurntOrange, Plum, BrickRed; light fills).
   - **Columns:**
     1. tools: `thm:prelim-cutting-rules`, `thm:prelim-slavnov-taylor`, `prop:prelim-wilson-rules`, `thm:prelim-composite-renorm`;
     2. IR structure: `thm:ir-landau-momentum`, `prop:ir-power-counting`, `thm:ir-leading-regions`;
     3. rigorous core: `thm:ee-R-finite`, `thm:dis-ope`, `thm:dis-moments`, `thm:pdf-moments-local`, `thm:pdf-dglap`;
     4. machine: `thm:sudakov-factorization`, `lem:method-ward-multi`, `thm:method-subtraction`, `prop:method-glauber-deformation`, `thm:method-template`;
     5. processes: `thm:disall-factorization`, `thm:coll-sia`, `thm:dy-factorization`, `thm:tmd-factorization`, `thm:scet-thrust`;
     6. boundaries: `thm:break-tmd`, `prop:break-spacelike`, `conj:dy-coloured-final`.
   - **Edges:** arrows follow the critical paths of FINAL_OUTLINE §0.5. Draw the three "weakest links" with a thick red border.
   - **Caption draft:** 「本书主要结论的逻辑依赖。框的颜色表示严格性标签（绿 R、蓝 A、橙 P、紫 C、红 V），粗红框为决定全阶论证地位的三个薄弱环节。」

### Ch2
2. **`fig:prelim-feynman-rules`** · Ch2 (`sec:prelim-qcd`) · TikZ table of vertices, about 0.9\textwidth.
   - **Draw:** two rows of small diagrams, each with its rule typeset beneath (VF-CONV-3).
     - Top row, propagators: quark (arrow, $\frac{i\slashed p}{p^2+i0}$), gluon (coil, $\frac{-ig_{\mu\nu}\delta^{ab}}{k^2+i0}$, Feynman gauge), ghost (dotted with arrow, $\frac{i\delta^{ab}}{p^2+i0}$).
     - Bottom row, vertices: $q\bar qg$ ($ig\gamma^\mu t^a$), three-gluon (all momenta incoming, $gf^{abc}[\dots]$), ghost–gluon ($-gf^{abc}p^\mu$, $p$ the outgoing ghost), four-gluon (rule written in the text).
   - Use the `quark`, `gluon`, `ghost`, `vertex` and `mom` styles.
   - **Caption draft:** 「本书使用的 Feynman 规则（协变规范，$D_\mu=\partial_\mu-igA^a_\mu t^a$）。三胶子顶点的动量均为流入，鬼场顶点中的 $p$ 为流出鬼场的动量。」
3. **`fig:prelim-wilson-rules`** · Ch2 (`sec:prelim-wilson`) · TikZ.
   - **Draw:** two panels.
     - (a) Past-pointing line $W[0,-\infty n]$: a double line from the left edge to a point $0$ (open circle). Three gluons $k_1,k_2,k_3$ attach in order from $-\infty$. Show the eikonal propagators $\frac{i}{n\cdot(k_1+\dots+k_j)+i0}$ under the segments and the vertices $igt^an^\mu$.
     - (b) Future-pointing line $W[\infty n,0]$ with denominators $\frac{-i}{n\cdot(k_j+\dots+k_m)-i0}$.
   - The momentum arrow of $k$ points into the line (VF-CONV-9).
   - **Caption draft:** 「半无限 Wilson 线的动量空间规则（$k$ 流入 Wilson 线；颜色矩阵按路径排序，靠近终点者在左）。(a) 过去指向，(b) 未来指向。」
   - **Start from:** `research/c_wilson/tex/c_wilson_rules.tex` (`fig:cw-rules`).

### Ch4
4. **`fig:sudakov-hjjs`** · Ch4 (`sec:sudakov-factorization`) · TikZ.
   - **Draw:** the reduced diagram of the form factor $\gamma^*\to q\bar q$.
     - A hard blob $H$ at the centre, with the photon entering from the left.
     - Two jet blobs: $J_1$ (blue, along $n_A$, upper right) and $J_2$ (orange, along $n_B$, lower right).
     - A soft blob $S$ (green) between them, connected to both jets by gluons only.
     - Scalar-polarized collinear gluons from $J_i$ into $H$ drawn with `longit` and dots.
   - A second panel shows the factorized form $H\cdot J_1J_2/S$, with $J_i$ represented as matrix elements with a Wilson line (double line) along the opposite direction, and $S$ as two Wilson lines meeting at a cusp.
   - **Caption draft:** 「Sudakov 形状因子的领头区域与因子化 $F=H\,J_1J_2/S$：喷注函数中的 Wilson 线沿另一喷注方向，软函数是两条 Wilson 线的真空期望。」
5. **`fig:sudakov-cusp`** · Ch4 (`sec:sudakov-evolution`) · TikZ.
   - **Draw:** a Wilson-line cusp. Two straight double lines from a common point with time-like directions $v_1$, $v_2$ and the cusp angle $\beta$ marked ($\cosh\beta=v_1\cdot v_2$).
   - One-loop gluon exchange between the two lines (coil), plus the self-energy of each line (small arc).
   - An inset shows the light-like limit, where both lines approach the light cone $\beta\to\infty$.
   - **Caption draft:** 「Wilson 线尖点及其单圈修正；尖点反常维度在类光极限下线性依赖于 $\beta$，给出 $\Gamma_{\rm cusp}$。」
6. **`fig:sudakov-dipole`** · Ch4 (`sec:sudakov-multileg`) · TikZ.
   - **Draw:** a hard blob with four outgoing lines $1..4$ (quarks/gluons).
   - (a) Dipole terms: gluons between pairs $(i,j)$, drawn as soft arcs labelled $\mathbf T_i\cdot\mathbf T_j$.
   - (b) Three-loop connected web touching three or four legs (non-dipole), shown as a shaded web connecting legs 1, 2, 3 (4).
   - **Caption draft:** 「多腿振幅的红外结构：(a) 两圈以内由偶极子项（色关联 $\mathbf T_i\cdot\mathbf T_j$）给出；(b) 三圈起出现连接三条或四条外线的非偶极子 web。」

### Ch5
7. **`fig:ee-pi-plane`** · Ch5 (`sec:ee-higher`) · TikZ.
   - **Draw:** the complex $q^2$ plane.
     - The cut along $[0,\infty)$ (wavy or bold line).
     - The Euclidean point $q^2=-Q^2$ marked on the negative axis.
     - The circle $|z|=s$, traversed counter-clockwise from $s+i0$ to $s-i0$, with arrows (contour formula `prop:ee-contour`).
     - The two points $s\pm i\Delta$ (smearing, `prop:ee-smearing`).
     - Labels "PT 可靠（欧氏）" near the negative axis and "共振区" near small $s$.
   - **Caption draft:** 「流关联函数 $\Pi(q^2)$ 的解析结构：割线 $[0,\infty)$、欧氏点 $-Q^2$、围道公式的积分路径 $|z|=s$ 以及抹平所用的点 $s\pm i\Delta$。」

### Ch8
8. **`fig:method-flowchart`** · Ch8 (`sec:method-strategy`) · TikZ flowchart, full width.
   - **Draw:** six boxes in a vertical chain:
     1. 区域（Landau + 幂次计数）
     2. 近似（共线/软，$i0$）
     3. Grammer–Yennie 分解
     4. Ward 恒等式 → Wilson 线
     5. 减除 + 幺正性（末态相互作用、软因子）+ Glauber 围道变形
     6. 因子化形式
   - Side annotations link each box to the hypotheses (H1)–(H5) of `thm:method-template` and to the canonical lemmas.
   - Boxes whose current status is [A] are coloured blue; boxes that are [R] at the level used are green.
   - **Caption draft:** 「全阶因子化证明的六个步骤及其与模板定理假设 (H1)–(H5) 的对应。」
9. **`fig:method-kg`** · Ch8 (`sec:method-gy`) · TikZ.
   - **Draw:** a collinear gluon between the $A$-collinear blob and $H$.
     - Left: the full $g_{\mu\nu}$.
     - Middle: the K term, drawn as `longit` with a dot and an arrow showing $\frac{k_\mu n_{B\nu}}{n_B\cdot k-i0}$.
     - Right: the G term, labelled "$\ge\lambda$ 压低".
     - Below: the Ward identity turns the K term into a Wilson line along $n_B$.
   - **Caption draft:** 「Grammer–Yennie 分解：共线胶子的 K 部分经 Ward 恒等式化为 Wilson 线，G 部分幂次压低（例外：作为活动部分子的单个横向胶子）。」
   - **Start from:** `research/c_wilson/tex/c_wilson_gy.tex` (`fig:cw-kg`).
10. **`fig:method-nesting`** · Ch8 (`sec:method-regions`) · TikZ.
    - **Draw:** a Venn-like diagram in the space of loop momenta (abstract).
      - The hard region contains the collinear-$A$ and collinear-$B$ regions, which both contain the soft region (nested pinch surfaces $\pi_S\subset\pi_A,\pi_B$).
      - Arrows labelled $T_S$, $T_A$, $T_H$ represent the approximators.
      - The subtraction chain $C_A=T_A(1-T_S)$ is written alongside.
    - **Caption draft:** 「区域的偏序与减除：最小区域（软）先近似，较大区域的近似子作用于减去较小区域贡献后的被积函数。」

### Ch10
11. **`fig:coll-sia`** · Ch10 (`sec:coll-sia`) · TikZ.
    - **Draw:** $e^+e^-\to\gamma^*\to hX$ as a cut diagram.
      - The photon enters a hard blob.
      - A jet blob containing the observed hadron $h$ (momentum $p_h$, fraction $z$) crosses the cut.
      - The other jet and the soft blob cross the cut.
    - Label $d_{h/q}(z/y)$ next to the jet that fragments.
    - **Caption draft:** 「$e^+e^-\to hX$ 的领头区域：被观测强子所在的喷注给出碎裂函数，其余末态在割线求和中由幺正性相消。」
12. **`fig:coll-sidis`** · Ch10 (`sec:coll-sidis`) · TikZ.
    - **Draw:** collinear SIDIS. The target blob (PDF, along $+z$) connects to a hard part with the virtual photon, and the outgoing jet blob produces $h$ (FF).
    - Annotate $x$, $z$, $P_{hT}$ and the region "$P_{hT}\sim Q$（共线）" vs "$P_{hT}\ll Q$（TMD, 第~13~章）".
    - **Caption draft:** 「半单举 DIS：$P_{hT}\sim Q$ 时为共线因子化 PDF$\otimes$硬部分$\otimes$FF；$P_{hT}\ll Q$ 时需要 TMD 因子化。」
13. **`fig:coll-photoproduction`** · Ch10 (`sec:coll-photo`) · TikZ, two panels.
    - **Draw:**
      - (a) Direct: the photon couples directly to the hard scattering with a parton from the proton.
      - (b) Resolved: the photon first splits into a hadron-like blob (photon PDF) that supplies a parton to the hard scattering, so that the photon side has spectators.
    - **Caption draft:** 「光生过程：(a) 直接光子（单强子过程，[A]）；(b) 分辨光子（等效于强子—强子过程，[C]）。」

### Ch9 (added by the audit; formerly optional)
26a. **`fig:disall-seed`** · Ch9 (`sec:disall-regions`) · TikZ.
   - **Draw:** one target-collinear K-gluon (`longit` with a dot, momentum $k$ into the hard part) attached to the struck quark of the hard part $H$ in all possible ways; an arrow to the right-hand side, where the gluon is attached instead to a future-pointing Wilson line $W[\infty n_B,0]$ (double line, $-i0$ in its eikonal propagator) at the quark field.
   - **Caption draft:** 「DIS 中 PDF Wilson 线的种子：一个靶共线 K 胶子对硬部分的所有附着之和，经 Ward 恒等式化为沿 $n_B$ 的未来指向 Wilson 线 $W^{(1)}[\infty n_B,0]$ 的单胶子项（VF-WL-8）。」
   - **Start from:** `research/c_wilson/tex/c_wilson_eikonal_ward.tex` (`fig:cw-dis-seed`).
26b. **`fig:disall-heavy`** · Ch9 (`sec:disall-heavy`) · TikZ, two panels.
   - **Draw:** (a) $\gamma^*g\to Q\bar Q$ at LO with massive quark lines (thick); (b) the ACOT/CWZ subtraction term $f_{Q/g}\otimes(\gamma^*Q\to Q)$, drawn as the gluon splitting into a $Q\bar Q$ pair (blob labelled $f_{Q/g}$) followed by the LO heavy-quark scattering.
   - **Caption draft:** 「含重夸克质量的 DIS：(a) 领头阶光子—胶子融合 $\gamma^*g\to Q\bar Q$；(b) 变味方案中的减除项 $f_{Q/g}\otimes\hat\sigma(\gamma^*Q\to Q)$，在 $m\to0$ 时抵消 $\ln(Q^2/m^2)P_{qg}$。」

### Ch11 (added by the audit; formerly optional)
26c. **`fig:dy-abelian-model`** · Ch11 (`sec:dy-model`) · TikZ.
   - **Draw:** two eikonal spectator lines (one from each hadron, opposite directions) exchanging $n$ massive abelian bosons (wavy lines, the `glauber` style), summed into the phase $e^{i\chi(b)}$; on the right the two cut placements (before/after the exchange) whose sum cancels for observables inclusive in the spectators' relative transverse momentum.
   - **Caption draft:** 「阿贝尔模型中旁观者之间的 Glauber 交换：对 $n$ 次交换求和给出冲量参数空间的相位 $e^{i\chi(b)}$，$\chi(b)=-\frac{g_Ag_B}{2\pi}K_0(m|b|)$；对旁观者相对横动量单举的截面中 $|e^{i\chi}|^2=1$，相位相消（VF-DY-13，VF-GLA-3）。」
   - **Start from:** `research/c_dy/dy_oneloop.tex` (`fig:dy1l-glauber`).

### Ch12
14. **`fig:thr-kinematics`** · Ch12 (`sec:thr-refactorization`) · TikZ.
    - **Draw:** the partonic threshold in DY. Two incoming partons from $f_A$, $f_B$ produce $\gamma^*$ with $z=Q^2/\hat s\to1$; only soft radiation (green, energy $\sim Q(1-z)$) is allowed.
    - A second panel shows the refactorized hard coefficient as $H\times S_{\rm DY}(Q(1-z))$, with the soft function made of two past-pointing Wilson lines.
    - **Caption draft:** 「阈值极限 $z\to1$：末态只剩能量 $\sim Q(1-z)$ 的软辐射，硬系数重新因子化为 $H\cdot S$。」
15. **`fig:thr-mellin`** · Ch12 (`sec:thr-prescriptions`) · TikZ.
    - **Draw:** the complex $N$ plane.
      - The rightmost singularities of the PDF moments, on the real axis.
      - The branch point $N_L$ at which $\alpha_s(Q^2/\bar N^2)$ reaches the Landau pole (position schematic, no formula), labelled "Landau 支点".
      - The minimal-prescription contour, parallel to the imaginary axis, passing between the PDF singularities and the Landau-pole branch point and bending to the left at large $|{\rm Im}\,N|$.
    - **Caption draft:** 「Mellin 反演与 Landau 极点：最小处方的积分围道位于部分子分布的奇点与 Landau 支点之间。」

### Ch15
16. **`fig:jets-sw-cone`** · Ch15 (`sec:jets-irsafe`) · TikZ.
    - **Draw:** the Sterman–Weinberg configuration in the $e^+e^-$ c.m. frame.
      - Two back-to-back cones of half-angle $\delta$ (shaded).
      - Particles inside the cones (lines).
      - A soft particle outside with energy $<\epsilon\sqrt s$.
      - Annotate "能量份额 $\epsilon$ 相对于总能量 $\sqrt s$".
    - **Caption draft:** 「Sterman–Weinberg 两喷注定义：两个半张角 $\delta$ 的锥之外的总能量小于 $\epsilon\sqrt s$。」
    - **Start from:** `research/c_ee/ee_total.tex` (`fig:ee-sw`).
17. **`fig:jets-ngl`** · Ch15 (`sec:jets-ngl`) · TikZ.
    - **Draw:** the hemisphere picture. A thrust axis separates hemispheres L and R, and an energy veto is imposed only in R.
      - A harder gluon $k_1$ emitted into L.
      - It radiates a softer gluon $k_2$ into R (the non-global configuration), with strong energy ordering $\omega_2\ll\omega_1$.
      - Label "$O(\alpha_s^2)$: $C_FC_A$".
    - **Caption draft:** 「非全局对数的来源：未被测量区域中的较硬胶子向被否决区域辐射较软胶子；首项出现在 $O(\alpha_s^2)$，色因子 $C_FC_A$。」
18. **`fig:jets-gap`** · Ch15 (`sec:jets-sll`) · TikZ.
    - **Draw:** gaps between jets at a hadron collider in the rapidity–azimuth plane.
      - Two jets at $y_1$, $y_2$.
      - A central gap region (hatched) with a veto $E_T<Q_0$.
      - Incoming beams at $y\to\pm\infty$.
    - A small inset shows a Coulomb (Glauber) exchange between the incoming partons (dark red coil, `glauber` style) dressed by a soft emission.
    - **Caption draft:** 「强子对撞中的"喷注间隙"可观测量；初态有色部分子间的 Coulomb/Glauber 交换与软辐射不对易，产生超领头对数。」

### Ch16
19. **`fig:smallx-dipole`** · Ch16 (`sec:smallx-dipole`) · TikZ.
    - **Draw:** the dipole picture of DIS at small $x$.
      - The virtual photon splits into a $q\bar q$ dipole of transverse size $r=|x_0-x_1|$.
      - The dipole crosses a target shock wave (a vertical shaded slab with Wilson lines $V(x_0)$, $V^\dagger(x_1)$).
      - One step of BK evolution: the emission of a gluon at $x_2$ splits the dipole into $(x_0,x_2)$ and $(x_2,x_1)$.
      - Annotate the kernel $\frac{x_{01}^2}{x_{02}^2x_{12}^2}$.
    - **Caption draft:** 「偶极子图像与 BK 演化：$q\bar q$ 偶极子穿过靶的冲击波；软胶子发射把偶极子分裂为两个，给出 BK 方程的非线性项。」
20. **`fig:smallx-map`** · Ch16 (`sec:smallx-status`) · TikZ.
    - **Draw:** the $(\ln1/x,\ln Q^2)$ plane.
      - The DGLAP region (large $Q^2$) and the BFKL direction (large $\ln1/x$).
      - The saturation line $Q_s^2(x)$ (diagonal curve), with the saturated region below it labelled "饱和（[C]）".
      - The DLA overlap near the diagonal.
      - Short tags with the status: DGLAP [R] (PT), BFKL [A] (LL/NLL), $k_T$ factorization [P].
    - **Caption draft:** 「小 $x$ 物理的"地图"：DGLAP、BFKL、饱和区及各描述的严格性地位。」

### Ch19
21. **`fig:heavy-bdpi`** · Ch19 (`sec:heavy-bdpi`) · TikZ.
    - **Draw:** $\bar B^0\to D^+\pi^-$.
      - The weak vertex (four-quark operator, square).
      - The $B\to D$ transition (heavy lines $b\to c$, double lines `bound state` for mesons).
      - The emitted pion as a collinear $q\bar q$ pair (blue jet blob) with DA $\phi_\pi(x)$.
      - Soft gluons between the pion pair and the $B$–$D$ system cancel at leading power (colour transparency), indicated by a crossed gluon.
    - **Caption draft:** 「$B\to D\pi$ 的因子化：发射的 $\pi$ 为小色偶极子，软胶子在领头幂次退耦；振幅为 $F^{B\to D}(0)\otimes T\otimes\phi_\pi$。」
    - **Start from:** `research/c_scet/tex/c_scet_bdecays.tex` (`fig:b-dpi`).
22. **`fig:heavy-qcdf`** · Ch19 (`sec:heavy-qcdf`) · TikZ, two panels.
    - **Draw:**
      - (a) The vertex term $T^{\rm I}$: form factor $\times$ hard kernel $\times\phi_{M_2}$.
      - (b) Hard spectator scattering $T^{\rm II}$, with a hard-collinear gluon from the spectator in $B$ to the emitted meson: $\phi_B\otimes\phi_{M_1}\otimes\phi_{M_2}$.
      - A red marker on the endpoint region ($y\to0$) of $\phi_{M_1}$ indicates the divergence at twist 3 and in annihilation.
    - **Caption draft:** 「无粲 $B\to M_1M_2$ 的 QCD 因子化：(a) 顶点项，(b) 硬旁观者散射；红色标记扭度 3 与湮灭项中的端点发散。」
    - **Start from:** `research/c_scet/tex/c_scet_bdecays.tex` (`fig:qcdf`).

### Ch20
23. **`fig:power-borel-plane`** · Ch20 (`sec:power-renormalons`) · TikZ.
    - **Draw:** the Borel $u$ plane.
      - IR renormalon poles at $u=2,3,\dots$ (crosses on the positive real axis), with $u=1$ explicitly marked as **absent** for the Adler function (open circle with a note "无 $u=1$").
      - UV renormalons at $u=-1,-2,\dots$.
      - The Borel integration path along the positive axis, with the ambiguity from deforming above or below.
      - An annotation linking $u=2$ to $\langle\frac{\alpha_s}\pi G^2\rangle/Q^4$.
    - **Caption draft:** 「大 $\beta_0$ 近似下 Adler 函数的 Borel 平面：红外重整化子位于 $u=2,3,\dots$（无 $u=1$），对应于 OPE 中的凝聚项。」

### Ch21
24. **`fig:lattice-matching`** · Ch21 (`sec:lattice-matching`) · TikZ schematic.
    - **Draw:** two columns.
      - Left: the lattice (Euclidean) quantity: quasi-PDF/pseudo-ITD at $P^z$ and $z^2$, with a box for "非微扰重整化（线性发散）".
      - Right: the light-cone PDF $q(x,\mu)$.
      - A middle arrow "匹配 $C(x/y,\mu/yP^z)$" with a note "+ $O(\Lambda^2/(x^2(1-x)P_z^2))$".
      - Underneath, "依赖于类空 OPE（[A]）".
    - **Caption draft:** 「LaMET/短距离因子化的结构：格点可计算的等时关联函数经微扰匹配与光锥 PDF 相联系，误差为幂次修正。」

### Ch22
25. **`fig:summary-status-map`** · Ch22 (`sec:summary-master`) · TikZ grid, full width.
    - **Draw:** a grid with rows = process classes and columns = levels ({微扰论严格 [R], 全阶论证 [A], 部分 [P], 猜想 [C], 破坏 [V]}).
      - Rows: $e^+e^-$ total, DIS moments, DIS $x$-space, SIA/SIDIS, DY/colour singlet, $pp\to$ jets, threshold, TMD (DY/SIDIS), TMD $h_1h_2\to h_3h_4$, SCET event shapes, small $x$, diffraction, DPS, exclusive, $B$ decays, NRQCD, power corrections, lattice.
      - Each cell contains a filled circle where the main result sits, using the tag colours.
      - The rows must agree with `tab:summary-master`.
    - **Caption draft:** 「各类过程中因子化陈述的地位一览（与表~\ref{tab:summary-master} 一致）。」
26. **`fig:summary-hypotheses`** · Ch22 (`sec:summary-hypotheses`) · TikZ bipartite graph.
    - **Draw:**
      - Left column: the hypotheses (H1)–(H5) and MA0–MA4.
      - Right column: the main [A] theorems (`thm:disall-factorization`, `thm:coll-sia`, `thm:dy-factorization`, `thm:tmd-factorization`, `thm:scet-thrust`, `thm:break-ddis`, `thm:break-double-dy`, `thm:excl-dvcs`, `thm:heavy-bdpi`).
      - Edges show which hypothesis each theorem needs; edges to the bottleneck hypothesis are thick red.
    - **Caption draft:** 「主要全阶论证所依赖的假设与元假设；粗红线为各定理的瓶颈。」

---------------------------------------------------------------------------------------------------

## 3. New figures — optional (10)

Draw these if the page budget allows; otherwise omit them without replacement.

| label | owner | draw | start from |
|---|---|---|---|
| `fig:prelim-lightcone` | Ch2 | $(z,t)$ diagram with light-cone axes $x^\pm$, a boosted hadron world-band and the components $v^\pm$; under a boost $v^\pm\to e^{\pm\eta}v^\pm$ | — |
| `fig:ir-landau-simplex` | Ch3 | Feynman-parameter simplex of the one-loop vertex with the Landau set (two edges, soft corner) highlighted | `research/c_regions/landau.tex` (`fig:landau-simplex`) |
| `fig:pdf-gluon-operator` | Ch7 | cut-diagram representation of the gluon PDF: $G^{+j}$ vertices with the adjoint Wilson line (double line, adjoint marking) | adapt `fig:pdf-operator` |
| `fig:pdf-ff-cut` | Ch7 | cut diagram of the fragmentation function: the parton emerges from the vacuum, the hadron $h$ and $X$ cross the cut, with future-pointing Wilson lines | — |
| `fig:coll-transversity` | Ch10 | helicity-flip structure: transversity couples chiral-odd to chiral-odd (DY $h_1\otimes\bar h_1$, SIDIS $h_1\otimes H_1^\perp$); absent in inclusive DIS | — |
| `fig:tmd-evolution` | Ch13 | $(\ln\mu,\ln\sqrt\zeta)$ plane: evolution paths from $(\mu_b,\mu_b^2)$ to $(Q,Q^2)$, first in $\zeta$ at fixed $\mu$ (CS kernel $\tilde K$), then in $\mu$ (anomalous dimension $\gamma_F$); path independence | — |
| `fig:scet-modes` | Ch14 | modes in the $(\ln\bar n\!\cdot\!p,\ln n\!\cdot\!p)$ plane with constant-virtuality lines; hard, collinear, (u)soft and Glauber points (VF-SCET-1) | `research/c_scet/tex/c_scet_scet.tex` (`fig:scet-modes`) |
| `fig:break-spacelike` | Ch17 | space-like collinear limit: incoming parton 2 and outgoing parton 3 become collinear; Coulomb phases with the other coloured partons ($\mathbf T_2\cdot\mathbf T_j$) indicated | — |
| `fig:excl-erbl` | Ch18 | the four one-loop ERBL graphs (exchange, two Wilson-line graphs, self-energy) with momentum fractions $x,y$ | `research/c_exclusive/tex/c_exclusive_da_erbl.tex` (`fig:cex-erbl-graphs`) |
| `fig:excl-endpoint` | Ch18 | pgfplots: ratio of LO $F_\pi$ for the CZ DA vs the asymptotic DA, and endpoint contributions as a function of a cut $x>x_0$ | `research/c_exclusive/tex/c_exclusive_formfactors.tex` (`fig:cex-endpoint`) |

**Further agent figures** that a writer may use instead of drawing anew. They must be relabelled to a `fig:<key>-<name>` label and reported:
- `research/c_ee/ee_total.tex`: `fig:ee-lo`, `fig:ee-nlo`, `fig:ee-2l`. `fig:ee-oneloop` (tikz2) already covers these.
- `research/c_regions/powercounting.tex`: `fig:pc-ee`, `fig:pc-dis`, `fig:pc-dy`, `fig:pc-leading`, `fig:pc-modes`. App E may adapt one of them as `fig:appE-degree`.
- `research/c_scet/tex`: `fig:thrust-HJJS`, `fig:thrust-oneloop`, `fig:usoft-decoupling`, `fig:nrqcd-decay`, `fig:nqs-nnlo`.
- `research/c_exclusive/tex`: `fig:cex-da-def`, `fig:cex-pionff-lo`, `fig:cex-tff`, `fig:cex-dvcs-handbag`, `fig:cex-meson`.
- `research/c_dis/dis_oneloop.tex`: `fig:dis1l-diagrams`. `research/c_dy/dy_oneloop.tex`: `fig:dy1l-diagrams`. `research/c_pdf/tex/c_pdf_oneloop.tex`: `fig:cpdf-oneloop`.

---------------------------------------------------------------------------------------------------

## 4. Figures per chapter (summary)

| unit | existing (owned) | new required | new optional | total required |
|---|---|---|---|---|
| Ch1 | parton-model, handbag, factorization-schematic | intro-dependency | — | 4 |
| Ch2 | soft-eikonal | prelim-feynman-rules, prelim-wilson-rules | prelim-lightcone | 3 |
| Ch3 | landau-pinch, vertex-regions, coleman-norton, reduced-ee, reduced-dis, reduced-dy, momentum-regions | — | ir-landau-simplex | 7 |
| Ch4 | sudakov-ff | sudakov-hjjs, sudakov-cusp, sudakov-dipole | — | 4 |
| Ch5 | ee-oneloop | ee-pi-plane | — | 2 |
| Ch6 | dis-kinematics, forward-compton, omega-plane, ope-schematic, dis-oneloop, higher-twist | — | — | 6 |
| Ch7 | pdf-operator, pdf-oneloop, dglap-ladder, splitting-vertices | — | pdf-gluon-operator, pdf-ff-cut | 4 |
| Ch8 | ward-identity, glauber-contour | method-flowchart, method-kg, method-nesting | — | 5 |
| Ch9 | — (refers back to reduced-dis, dis-oneloop) | disall-seed, disall-heavy | — | 2 |
| Ch10 | — | coll-sia, coll-sidis, coll-photoproduction | coll-transversity | 3 |
| Ch11 | dy-oneloop, glauber-exchange | dy-abelian-model | — | 3 |
| Ch12 | — | thr-kinematics, thr-mellin | — | 2 |
| Ch13 | tmd-staple, tmd-soft-factor, tmd-dy, sidis-dy-links | — | tmd-evolution | 4 |
| Ch14 | scet-wilson, dijet-factorization | — | scet-modes | 2 |
| Ch15 | — | jets-sw-cone, jets-ngl, jets-gap | — | 3 |
| Ch16 | bfkl-ladder | smallx-dipole, smallx-map | — | 3 |
| Ch17 | violation-cq, diffraction, dps | — | break-spacelike | 3 |
| Ch18 | pion-ff, dvcs-handbag, meson-production | — | excl-erbl, excl-endpoint | 3 |
| Ch19 | nrqcd | heavy-bdpi, heavy-qcdf | — | 3 |
| Ch20 | renormalon-chain, twist3-ssa | power-borel-plane | — | 3 |
| Ch21 | quasi-pdf | lattice-matching | — | 2 |
| Ch22 | — | summary-status-map, summary-hypotheses | — | 2 |
| App A–L | — | — | (App E may adapt `fig:pc-*`) | 0 |
| **total** | **44** | **29** | **10** | **73** |

---------------------------------------------------------------------------------------------------

## CHANGELOG

**2026-10-10 — spec audit (auditor agent).**
1. **Ownership = first use.** `fig:reduced-dis`, `fig:reduced-dy` moved Ch9/Ch11 → Ch3; `fig:dis-oneloop` Ch9 → Ch6; `fig:higher-twist` Ch20 → Ch6; `fig:soft-eikonal` Ch8 → Ch2. Reason: rule (c) of the audit, no chapter may need a figure printed in a later chapter. The remaining later-figure references are marked "pointer only".
2. **Promoted to required:** `fig:disall-seed`, `fig:disall-heavy` (Ch9 would otherwise own no figure), `fig:dy-abelian-model` (Ch11's main worked model). Full drawing descriptions and caption drafts added in §2 (entries 26a–26c). Counts: 44 existing + 29 required new + 10 optional.
3. **Caption conventions:** the meaning of $n,\bar n$ in five existing captions documented (§1 notes), with the conversion sentence the owning writer must add.
4. All 44 existing labels were re-checked in the current `figures{1,2,3}.tex` (tikz1 12:42, tikz2 13:00, tikz3 13:49): all present, 12+16+16 `%%% BEGIN` blocks. Every chapter Ch1–Ch22 still has at least two required figures (§4).

