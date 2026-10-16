# FIGURES_INDEX_v2 — figures of 《QCD 因子化定理：严格证明、全阶论证与适用边界》 (spec v2)

Drafted 2026-10-10 by the spec-v2 writer-spec/figures/bibliography drafter (revision v2.1, same day); **revision v2.2** by the spec-v2 integrator (merge with FINAL_OUTLINE_v2: App P generated per-part graphs, optional `fig:lamet-dependency`, confirmed section labels — see CHANGELOG). It **supersedes** `spec/FIGURES_INDEX.md` and binds together with `WRITER_SPEC_v2.md` §8. Chapter numbers are the v2 numbers (WRITER_SPEC_v2 §1.1); labels of existing figures are unchanged.

## 0. Rules

1. **One owner.** Every figure belongs to exactly one owner unit (column "owner"): the **first unit in reading order that uses it** (with the v2 order Ch1 … Ch25, then App A … Q). Only the owner includes the `figure` environment; every other unit refers to it with `\cref{fig:…}` (「见\cref{fig:reduced-dis}」). A later unit may refer back freely; a reference to a figure printed later is allowed only as a pointer, never as a step of an argument (marked "pointer only" below).
2. **Existing figures are copied verbatim.** Copy the whole block from `%%% BEGIN fig:<name>` to `%%% END fig:<name>` out of the source file, including `\begin{figure}`, the caption and the label. Do not edit coordinates, styles or captions. A caption that seems wrong is kept and reported under "figure issues".
3. **All three source files are final** (this replaces v1 rule 3): `research/tikz1/figures1.tex` (12 figures), `research/tikz2/figures2.tex` (16), `research/tikz3/figures3.tex` (16). On 2026-10-10 all 44 `%%% BEGIN/END` blocks were present and the test documents compiled without errors (`test_figures{1,2,3}.log`). Renders to look at before writing: `research/tikz1/png/`, `research/tikz2/render/`, `research/tikz3/png/`, and the PDFs `test_figures{1,2,3}.pdf`.
4. **Placeholder protocol** (keeps the canonical label so that `\cref` works):
   ```latex
   \begin{figure}[htbp]\centering
   \fbox{\parbox{0.8\textwidth}{\centering\vspace{2cm}图待补：fig:<name>（见 FIGURES\_INDEX\_v2）\vspace{2cm}}}
   \caption{<the caption draft from this index>}\label{fig:<name>}
   \end{figure}
   ```
5. **New figures.**
   - Plain TikZ (or pgfplots, `compat=1.17` is set in the preamble) with the styles of `common/preamble_fact.tex`: `fd`, `quark`, `gluon`, `gluon loop`, `photon`, `ghost`, `mom`, `mom'`, `vertex`, `blob`, `bound state`, `wilson`, `wilson plain`, `cut`, `hard blob`, `jet blob`, `jetB blob`, `soft blob`, `hadron blob`, `glauber`, `opvertex`, `scalar`, `longit` with `\longitmark`, `lcaxis`, `region`. Loaded TikZ libraries: decorations.pathmorphing, decorations.markings, arrows.meta, calc, positioning, shapes.geometric, patterns, backgrounds, fit. **Do not load new packages or libraries.**
   - Wrap each new figure in `%%% BEGIN fig:<label>` / `%%% END fig:<label>`.
   - Width at most `\textwidth`; fonts `\small` or the `fd` default (`\scriptsize` for tick labels); colours as in the styles, light enough for greyscale print.
   - **Numbers and formulas only from VERIFIED_FORMULAS_v2.** pgfplots curves are computed from the VF formula quoted in the entry (pgfplots expression) or drawn from the inline coordinate table given in the entry (computed by `spec_v2/checks/fig_data.py` / `vf_v2_checks.py`); no external data files.
   - Schematic figures say 「（示意）」 in the caption.
   - Captions: Chinese, self-contained, 1–4 sentences, stating the conventions that matter (directions of momenta and Wilson lines, $\pm i0$, which subgraph is which, the meaning of colours); VF IDs and citations may appear in captions.
6. **Adapting agent snippets** (column "start from"): rename the label to the canonical one; check conventions (WRITER_SPEC_v2 §3: $n_A,n_B$; arrows = fermion-number flow; momentum arrows separate; $\pm i0$ statements in the caption); render and inspect the PNG.
7. **Caption notation of existing figures.** Some existing captions use $n,\bar n$ outside Ch15 with different meanings (§1 notes). The owner adds one sentence in the text at the first reference, e.g. 「（图中 $n$、$\bar n$ 即本书的 $n_A$、$n_B$）」, and lists it under "figure issues".
8. **Status words in captions** must agree with the tags of FINAL_OUTLINE_v2 (e.g. 「全阶论证 [A]」). If a tag changes in the outline, the owner adjusts the caption of a *new* figure and reports the mismatch for an *existing* one.
9. **Captions and `verify/` claims (spec v2.1; final in v2.3).** A caption never contains a planning marker (the retired pending-verification marker, 「待文献核查」), a novelty claim (「本书新结果」「首次」) or an erratum statement about a paper; captions state the physics with the published source or the VF ID. The following figures touch claims of `verify/CLAIMS.md` (classes of WRITER_SPEC_v2 §6.5, §6.13) or the proof extensions X1–X3. The verify patch v2.3 has been applied: their owners **must re-check the caption** against the final outcome given in the last column (FINAL_OUTLINE_v2 §0.10, §00.4); generated figures that depend on the changed `\uses` data or master rows are regenerated (§5 note).

   | figure | claim | final outcome to check (v2.3) |
   |---|---|---|
   | `fig:dy-two-gluon-exchange` | N01 | confirmed but known (`Meggiolaro:1996hf`, `Giordano:2006vv`): no novelty wording anywhere; the caption may cite these sources |
   | `fig:appO-deformation`, `fig:appO-flowchart`, `fig:appO-cutsum`, `fig:appO-lcopt-term`, `fig:method-glauber-direction`, `fig:dy-pole-orientation`, `fig:break-measurement`; optional `fig:appO-windows`, `fig:appO-glauber-flow` | X1 | final App O statements: window-edge terms vanish with side-independent windows (`lem:appO-side-independent-windows`); `asm:appO-mixing` has clause (a′); the model theorems of §O.5 ([P]) and their assumptions `asm:appO-adjacent-swap`, `asm:appO-real-jets`, `asm:appO-collinear-ends` are side boxes of `fig:appO-flowchart`, never premises of `thm:appO-main`; ordering weights continuous with a kink |
   | `fig:method-hasse`, `fig:method-neighbourhoods`, `fig:method-sudakov-plane`, `fig:appN-triangle-regions`, `fig:appN-triangle-remainder` | X2; N12 | final App N statements: (CS1)–(CS3) for the triangle proved in the fibered norm (`prop:appN-triangle-cs`); the remainder is a sharpened explicit result, never "new" (the only novelty marker of the book, `prop:appN-triangle-cs`(a), is printed in the text, never in a caption) |
   | `fig:appM-dependency`, `fig:appM-forest`, `fig:appM-handbag-ab`, `fig:appM-euclid-forward`, `fig:dis-euclid-segment` | X3 | final App M statements: `asm:appM-brst-ope` is (Eε) ((B1) retired); new nodes `lem:appM-ne`, `thm:appM-brst-reduction`, `thm:appM-forward-expansion`, `cor:appM-forward-ope`, `asm:appM-oswi`; `asm:appM-remainder` feeds `thm:appM-scaling`, not `prop:dis-ope-euclid` |
   | `fig:front-gordan` | N02, A08 | N02 confirmed, no novelty claim; `Collins:2020euz` is a preprint |
   | `fig:lamet-hybrid` | E01 | confirmed: the caption gives $\int C_{\rm hyb}=1$ without commenting on the printed form (App Q row Q.8) |
   | `fig:yzliu-leading-region`, `fig:yzliu-soft-hqet` | E02, A03, A04 | E02 confirmed (correct CS exponent); priority words only in the text and only with 「据我们所知」 (A03); A04 corrections applied |
   | `fig:yzliu-complex-lorentz` | E13 | confirmed: the map is $\Lambda(t,z)=(iz,it)$; "edge of the wedge" is not used for the BHW step |
   | `fig:yzliu-threshold` | N06, A26 | confirmed: a check of the published factorization; two-loop agreement as "consistent with" (fitted constants) |
   | `fig:lamet-oneloop` | N05, N09 | N05 confirmed (cite `IzubuchiEtAl2018` App. B); no statement on the convolution domain beyond `prop:lamet-tails` as corrected (N09 refuted as stated) |
   | `fig:lamet-fourier` (optional) | N10 | confirmed, known in substance (also `Monahan:2026skv`): no novelty wording; the mode count cites `SlepianPollak1961`, `LandauWidom1980` |
   | `fig:front-yukawa-pdf` | E35 | confirmed: `CollinsRogersSato2022` model, $f<0$ for $\xi\in(0.264,1)$ at $\mu=0.8$ GeV, positive for all $\xi$ iff $\mu\ge1.699$ GeV; the dispute stays in the text |
   | `fig:jets-sw-cone` | E28 | confirmed as a convention remark: $\epsilon$ is the fraction of the total energy $\sqrt s$ |
   | `fig:excl-endpoint` (optional) | N21 | confirmed; novelty of the closed forms not asserted; cite the soft-region argument to `IsgurLlewellynSmith1984` |

**Counts (v2).**

| class | v1 | v2 |
|---|---|---|
| existing (tikz1–3) | 44 | 44 |
| v1 new figures, required | 29 | 30 (`fig:prelim-lightcone` promoted, refdoc S56) |
| v1 new figures, optional | 10 | 9 |
| refdoc S56 figures, required / optional | — | 17 / 5 |
| new v2 figures (Ch2, Ch22–Ch24, App M/N/O/P), required / optional | — | 22 / 11 |
| **total required (incl. existing)** | 73 | **120** (113 + the 7 generated per-part App P graphs, v2.2) |
| **total optional** | 10 | **26** (+ `fig:lamet-dependency`, v2.2) |

Every chapter Ch1–Ch25 owns at least two required figures, and each big appendix (M, N, O, P) at least one (§5).

---------------------------------------------------------------------------------------------------

## 1. Existing figures (44), re-assigned to v2 owners by first use

| # | label | source | v2 owner (v1 owner) | also referenced from | content (from caption) |
|---|---|---|---|---|---|
| 1 | `fig:parton-model` | tikz1 | Ch1 `intro` (Ch1) | Ch7, Ch8 | 部分子模型图像：静止系 vs 无穷动量系；时间膨胀 |
| 2 | `fig:dis-kinematics` | tikz1 | Ch7 `dis` (Ch6) | Ch10 | DIS 运动学 $\ell+A\to\ell'+X$ |
| 3 | `fig:handbag` | tikz1 | Ch1 (Ch1) | Ch7 | 部分子模型的手提包割图 |
| 4 | `fig:forward-compton` | tikz1 | Ch7 (Ch6) | App M | 前向 Compton 振幅（$s$ 道与 $u$ 道） |
| 5 | `fig:omega-plane` | tikz1 | Ch7 (Ch6) | App M | $\omega$ 复平面、割线与围道 |
| 6 | `fig:ope-schematic` | tikz1 | Ch7 (Ch6) | Ch22, App M | 光锥 OPE 示意 |
| 7 | `fig:pdf-operator` | tikz1 | Ch8 `pdf` (Ch7) | Ch9, Ch22 | 夸克分布的割图表示 |
| 8 | `fig:pdf-oneloop` | tikz1 | Ch8 (Ch7) | App G, Ch22 | PDF 单圈图（实辐射、Wilson 线、虚修正） |
| 9 | `fig:dglap-ladder` | tikz1 | Ch8 (Ch7) | Ch17 | LLA 梯形图 |
| 10 | `fig:splitting-vertices` | tikz1 | Ch8 (Ch7) | — | 四种 $1\to2$ 分裂 |
| 11 | `fig:dis-oneloop` | tikz1 | Ch7 (Ch6) | Ch10, App G | DIS 的 $O(\alpha_s)$ 图 |
| 12 | `fig:factorization-schematic` | tikz1 | Ch1 (Ch1) | Ch9, Ch12 | 强子—强子共线因子化示意 |
| 13 | `fig:landau-pinch` | tikz2 | Ch4 `ir` (Ch3) | App D, Ch24 | 复 $k^-$ 平面：端点、非钳夹、钳夹 |
| 14 | `fig:vertex-regions` | tikz2 | Ch4 (Ch3) | Ch5 | 单圈顶点的三个钳夹面 |
| 15 | `fig:coleman-norton` | tikz2 | Ch4 (Ch3) | App D, Ch24 | Coleman–Norton 时空图像 |
| 16 | `fig:reduced-ee` | tikz2 | Ch4 (Ch3) | Ch6, Ch15 | $e^+e^-$ 两喷注约化割图 |
| 17 | `fig:reduced-dis` | tikz2 | Ch4 (Ch3) | Ch10, App E | DIS 约化割图 |
| 18 | `fig:reduced-dy` | tikz2 | Ch4 (Ch3) | Ch12, Ch14 | DY 约化割图 |
| 19 | `fig:momentum-regions` | tikz2 | Ch4 (Ch3) | Ch9, Ch14, Ch15 | $(\ln k^+,\ln k^-)$ 平面上的区域 |
| 20 | `fig:ward-identity` | tikz2 | Ch9 `method` (Ch8) | App F | 图示 Ward 恒等式（K 胶子 → Wilson 线） |
| 21 | `fig:soft-eikonal` | tikz2 | **Ch3 `prelim`** (Ch2) | Ch9 | 软胶子程函近似；出射/入射夸克 ↔ 未来/过去指向 Wilson 线 |
| 22 | `fig:ee-oneloop` | tikz2 | Ch6 `ee` (Ch5) | App G; Ch2 (pointer only) | $e^+e^-$ $O(\alpha_s)$：振幅图与 $\Pi$ 的两圈图及切割 |
| 23 | `fig:dy-oneloop` | tikz2 | Ch12 `dy` (Ch11) | App G | DY $O(\alpha_s)$ 部分子图 |
| 24 | `fig:glauber-exchange` | tikz2 | Ch12 (Ch11) | Ch18, App O | Glauber 交换：DY 旁观者 vs SIDIS/DIS |
| 25 | `fig:glauber-contour` | tikz2 | Ch9 (Ch8) | Ch12, App O | 复 $k^-$ 平面中的 Glauber 区分析 |
| 26 | `fig:sudakov-ff` | tikz2 | Ch5 `sudakov` (Ch4) | Ch4 (pointer only) | 离壳 Sudakov 形状因子的区域展开 |
| 27 | `fig:scet-wilson` | tikz2 | Ch15 `scet` (Ch14) | — | SCET 中的 $W_n$ 与 $Y_n$ |
| 28 | `fig:dijet-factorization` | tikz2 | Ch15 (Ch14) | Ch16 | 推力分布 $H\,J\otimes J\otimes S$ |
| 29 | `fig:tmd-staple` | tikz3 | Ch14 `tmd` (Ch13) | Ch18, Ch22, Ch23 | TMD 算符的订书钉形 Wilson 线 |
| 30 | `fig:tmd-soft-factor` | tikz3 | Ch14 (Ch13) | Ch23 | TMD 软因子的割图表示 |
| 31 | `fig:tmd-dy` | tikz3 | Ch14 (Ch13) | — | 小 $q_T$ DY 的约化割图与 TMD 因子化 |
| 32 | `fig:sidis-dy-links` | tikz3 | Ch14 (Ch13) | Ch21 | 单胶子交换决定 Wilson 线方向（SIDIS vs DY） |
| 33 | `fig:violation-cq` | tikz3 | Ch18 `break` (Ch17) | App O | Collins–Qiu 机制 |
| 34 | `fig:diffraction` | tikz3 | Ch18 (Ch17) | Ch11 (pointer only) | 衍射 DIS vs 强子—强子衍射 |
| 35 | `fig:pion-ff` | tikz3 | Ch19 `excl` (Ch18) | — | $\pi$ 形状因子领头阶硬散射 |
| 36 | `fig:dvcs-handbag` | tikz3 | Ch19 (Ch18) | Ch22 | DVCS 手提包图与交叉图 |
| 37 | `fig:meson-production` | tikz3 | Ch19 (Ch18) | — | 纵向光子介子产生 |
| 38 | `fig:nrqcd` | tikz3 | Ch20 `heavy` (Ch19) | — | NRQCD 产生的因子化图像 |
| 39 | `fig:bfkl-ladder` | tikz3 | Ch17 `smallx` (Ch16) | — | 小 $x$：割开的胶子梯形图（BFKL） |
| 40 | `fig:renormalon-chain` | tikz3 | Ch21 `power` (Ch20) | Ch22 | 重整化子链图（大 $\beta_0$） |
| 41 | `fig:higher-twist` | tikz3 | Ch7 (Ch6) | Ch21 | DIS 强子张量的扭度展开 |
| 42 | `fig:twist3-ssa` | tikz3 | Ch21 (Ch20) | Ch14 (pointer only) | Qiu–Sterman 软胶子极点机制 |
| 43 | `fig:dps` | tikz3 | Ch18 (Ch17) | Ch24 | 双部分子散射（双 DY） |
| 44 | `fig:quasi-pdf` | tikz3 | **Ch22 `lamet`** (Ch21) | Ch23 | 准 PDF 与光锥 PDF 的时空图 |

Notes on the existing figures.
- **Owner changes caused by the v2 structure.** `fig:soft-eikonal` moves with the Wilson-line material to Ch3 `prelim` (Ch2 `qcd` does not use it; if the Ch2 writer wants to show it, it is a forward pointer). `fig:quasi-pdf` moves with the `lattice` material to Ch22. All other owners keep their v1 key; their chapter number is the v1 number + 1.
- **Captions with $n,\bar n$ outside Ch15.** In `fig:momentum-regions` (Ch4) and `fig:sudakov-ff` (Ch5), $n$ is the direction of hadron/jet $A$ (our $n_A$) and $\bar n$ is our $n_B$; in `fig:pdf-operator` (Ch8), `fig:tmd-staple` and `fig:sidis-dy-links` (Ch14), $n$ is the vector with $n\cdot v=v^+$, i.e. our $n_B$; in `fig:soft-eikonal` (Ch3), $n$ is the direction of the quark momentum $p$. The owner adds the conversion sentence (rule 7).
- **Caption pointers to later figures** (allowed as pointers): `fig:reduced-ee` → `fig:reduced-dis` (same unit); `fig:reduced-dis` (Ch4) → `fig:ward-identity` (Ch9); `fig:reduced-dy` (Ch4) → `fig:glauber-exchange` (Ch12); `fig:factorization-schematic` (Ch1) → `fig:pdf-operator` (Ch8).
- **`fig:tmd-staple`** shows **light-like** staples (Collins' TMD); the **space-like** staples of the quasi-TMD (Ch22–Ch23) are drawn in `fig:lamet-lattice-geometries` and `fig:yzliu-leading-region`; Ch22/Ch23 must say so when they refer to `fig:tmd-staple`.
- **`fig:quasi-pdf`** writes the quasi-PDF with $\int\frac{dz}{4\pi}e^{ixP^zz}$ and $\Gamma=\gamma^z$ or $\gamma^t$ "(归一化见正文)": consistent with WRITER_SPEC_v2 §3 row 41 ($N_\Gamma$ in the text).
- **`fig:glauber-exchange`, `fig:glauber-contour`** describe the obstruction (poles on both sides) and the cut-sum pre-step; their captions do not mention the two-component deformation — Ch9/Ch12 must add 「离开 Glauber 区须沿 $e_G$ 同时形变两个分量（\cref{fig:method-glauber-direction}）」 at the first reference (M31).
- **`fig:sidis-dy-links`** says the past-pointing line in DY arises from the initial-state interaction; at the first reference Ch14 adds that in a single cut graph the line is future-pointing and the past-pointing form appears only after the cut sum and one-sided rewriting (`ex:dy-future-vs-past`, M33).

---------------------------------------------------------------------------------------------------

## 2. v1 new figures, re-assigned (30 required + 9 optional)

Format: label · owner (section) · type; **draw**; **caption draft**; **start from** (agent snippet), if any. Section labels are those of FINAL_OUTLINE (v1 keys unchanged); where FINAL_OUTLINE_v2 renames a section, use its label.

### Ch1 `intro`
1. **`fig:intro-dependency`** · Ch1 (`sec:intro-organisation`) · TikZ graph, full width, ≈10 cm high. **Updated for v2.**
   - **Draw:** a left-to-right layered graph of the main canonical results; rounded-rectangle nodes with a short Chinese name (and optionally `\cref{…}`); fill colour = tag (OliveGreen, RoyalBlue, BurntOrange, Plum, BrickRed, light fills, as `\tagR`…`\tagV`); `[R, R_cond]` nodes have a dashed border. Assumption nodes (`asm:`) are small orange dashed boxes below the columns, connected by dashed orange edges to the R_cond statements that use them.
   - **Columns:** (1) tools (Ch2–Ch3): `thm:prelim-slavnov-taylor`, `prop:prelim-beta`, `thm:prelim-cutting-rules`, `prop:prelim-wilson-rules`, `thm:prelim-composite-renorm`; (2) IR structure (Ch4–Ch5): `thm:ir-landau-momentum`, `prop:ir-power-counting`, `thm:ir-leading-regions`, `thm:sudakov-factorization`; (3) rigorous core (Ch6–Ch8): `thm:ee-R-finite`, `thm:dis-ope`, `thm:dis-moments`, `thm:dis-moments-np`, `thm:pdf-moments-local`, `thm:pdf-dglap`; (4) machine (Ch9 + App N/O): `lem:method-ward-multi`, `thm:method-subtraction`, `thm:appN-subtraction`, `prop:method-glauber-deformation`, `thm:appO-main`, `thm:method-template`; (5) processes (Ch10–Ch15): `thm:disall-factorization`, `thm:coll-sia`, `thm:dy-factorization`, `thm:tmd-factorization`, `thm:scet-thrust`; (6) boundaries (Ch18): `thm:break-tmd`, `prop:break-spacelike`, `conj:dy-coloured-final`; (7) frontier (Ch22–Ch24): the LaMET matching theorem, the quasi-TMD factorization theorem, the time-ordering theorem, the physical-region pinch criterion (labels per FINAL_OUTLINE_v2).
   - **Assumption nodes:** `asm:intro-bridge`, `asm:intro-np-ope`, `asm:appN-collins`, `asm:appO-mixing`, `asm:appO-deformation`, `asm:appO-rewritten-cs` (the bottlenecks); thick red edges from them to the [A] process theorems.
   - **Caption draft:** 「本书主要结论的逻辑依赖。框的颜色表示严格性标签（绿 R、蓝 A、橙 P、紫 C、红 V），虚线框为 $R_{\rm cond}$ 条件定理；下方橙色虚线框为编号假设，粗红线标出决定各全阶论证地位的瓶颈假设。完整的依赖图见附录~P。」

### Ch2 `qcd`
2. **`fig:prelim-feynman-rules`** · Ch2 (`sec:prelim-qcd` or its v2 replacement) · TikZ table of vertices, ≈0.9\textwidth.
   - **Draw:** two rows of small diagrams with the rule typeset beneath (VF-CONV-3). Top row, propagators: quark (arrow, $\frac{i\slashed p}{p^2+i0}$), gluon (coil, $\frac{-ig_{\mu\nu}\delta^{ab}}{k^2+i0}$, Feynman gauge; general $\xi_g$ in the text), ghost (dotted with arrow, $\frac{i\delta^{ab}}{p^2+i0}$). Bottom row, vertices: $q\bar qg$ ($ig\gamma^\mu t^a$), three-gluon (all momenta incoming, $gf^{abc}[g^{\mu\nu}(k-p)^\rho+g^{\nu\rho}(p-q)^\mu+g^{\rho\mu}(q-k)^\nu]$), ghost–gluon ($-gf^{abc}p^\mu$, $p$ the outgoing ghost), four-gluon ($-ig^2[f^{abe}f^{cde}(g^{\mu\rho}g^{\nu\sigma}-g^{\mu\sigma}g^{\nu\rho})+\dots]$ written in the text, as Peskin–Schroeder).
   - Styles `quark`, `gluon`, `ghost`, `vertex`, `mom`.
   - **Caption draft:** 「本书使用的 Feynman 规则（协变规范，$D_\mu=\partial_\mu-igA^a_\mu t^a$；图中胶子传播子取 Feynman 规范 $\xi_g=1$）。三胶子顶点的动量均为流入，鬼场顶点中的 $p$ 为流出鬼场的动量。」

### Ch3 `prelim`
3. **`fig:prelim-wilson-rules`** · Ch3 (`sec:prelim-wilson`) · TikZ.
   - **Draw:** two panels. (a) Past-pointing line $W[0,-\infty n]$: a double line (`wilson`) from the left edge to the point $0$ (open circle); three gluons $k_1,k_2,k_3$ attach in order from $-\infty$; under the segments the eikonal propagators $\frac{i}{n\cdot(k_1+\dots+k_j)+i0}$, at the vertices $igt^an^\mu$. (b) Future-pointing line $W[\infty n,0]$ with denominators $\frac{-i}{n\cdot(k_j+\dots+k_m)-i0}$. Momentum arrows of $k$ point into the line (VF-CONV-9, VF-WL-1).
   - **Caption draft:** 「半无限 Wilson 线的动量空间规则（$k$ 流入 Wilson 线；颜色矩阵按路径排序，靠近终点者在左）。(a) 过去指向，(b) 未来指向。」
   - **Start from:** `research/c_wilson/tex/c_wilson_rules.tex` (`fig:cw-rules`).
4. **`fig:prelim-lightcone`** (promoted to required, refdoc S56) · Ch3 (`sec:prelim-lightfront`) · TikZ, two panels.
   - **Draw:** (a) the $(z,t)$ plane with `lcaxis` arrows for $z$ (horizontal) and $t$ (vertical); the light-cone axes $x^\pm=(t\pm z)/\sqrt2$ drawn as dashed diagonals labelled $x^+$, $x^-$; a boosted hadron world-band (light grey strip `hadron blob` fill) tilted towards the $x^+$ axis; an invariant hyperbola $t^2-z^2={\rm const}$ (dotted) with two points related by a boost of rapidity $\eta$ (arrow along the hyperbola). (b) The $(\ln v^+,\ln v^-)$ plane: a point $(\ln v^+,\ln v^-)$ and its image after the boost, $(\ln v^++\eta,\ln v^--\eta)$: the boost is a translation along the anti-diagonal; lines of constant $v^+v^-$ are anti-diagonals (slope $-1$), lines of constant rapidity $y=\frac12\ln(v^+/v^-)$ are diagonals.
   - **Caption draft:** 「光锥坐标与 Lorentz 推动。(a) $(z,t)$ 平面中的光锥轴 $x^\pm=(t\pm z)/\sqrt2$ 与沿 $+z$ 快速运动的强子世界带；推动沿不变双曲线移动点。(b) 对数光锥平面中，快度为 $\eta$ 的推动 $v^\pm\to e^{\pm\eta}v^\pm$ 是沿反对角线的平移，等 $v^+v^-$ 线为反对角线，等快度线为对角线。」

### Ch5 `sudakov`
5. **`fig:sudakov-hjjs`** · Ch5 (`sec:sudakov-factorization`) · TikZ.
   - **Draw:** the reduced diagram of the form factor $\gamma^*\to q\bar q$: a hard blob $H$ at the centre with the photon (wavy) entering from the left; two jet blobs $J_1$ (`jet blob`, along $n_A$, upper right) and $J_2$ (`jetB blob`, along $n_B$, lower right); a soft blob $S$ (`soft blob`) between them, connected to both jets by gluons only; scalar-polarized collinear gluons from $J_i$ into $H$ drawn with `longit` and `\longitmark`. A second panel: the factorized form $H\cdot J_1J_2/S$, with $J_i$ as matrix elements with a Wilson line (double line) along the opposite direction and $S$ as two Wilson lines meeting at a cusp.
   - **Caption draft:** 「Sudakov 形状因子的领头区域与因子化 $F=H\,J_1J_2/S$：喷注函数中的 Wilson 线沿另一喷注方向，软函数是两条 Wilson 线的真空期望。」
6. **`fig:sudakov-cusp`** · Ch5 (`sec:sudakov-evolution`) · TikZ.
   - **Draw:** two straight double lines from a common point with time-like directions $v_1,v_2$ and the cusp angle $\beta$ marked ($\cosh\beta=v_1\cdot v_2$); one-loop gluon exchange between the lines (coil) and the self-energy of each line (small arc). Inset: the light-like limit, both lines approaching the light cone, $\beta\to\infty$.
   - **Caption draft:** 「Wilson 线尖点及其单圈修正；包含两线自能的单圈尖点反常维度为 $\Gamma(\beta)=\frac{\alpha_sC_F}\pi(\beta\coth\beta-1)$，类光极限下线性依赖于 $\beta$，给出 $\Gamma_{\rm cusp}$（VF-CONV-23）。」
7. **`fig:sudakov-dipole`** · Ch5 (`sec:sudakov-multileg`) · TikZ.
   - **Draw:** a hard blob with four outgoing lines $1..4$. (a) Dipole terms: gluons between pairs $(i,j)$, drawn as soft arcs labelled $\mathbf T_i\cdot\mathbf T_j$. (b) A three-loop connected web touching three or four legs (non-dipole), shown as a shaded web connecting legs 1, 2, 3 (4).
   - **Caption draft:** 「多腿振幅的红外结构：(a) 两圈以内由偶极子项（色关联 $\mathbf T_i\cdot\mathbf T_j$）给出；(b) 三圈起出现连接三条或四条外线的非偶极子 web（偶极子公式超出两圈不成立，[V]）。」

### Ch6 `ee`
8. **`fig:ee-pi-plane`** · Ch6 (`sec:ee-higher`) · TikZ.
   - **Draw:** the complex $q^2$ plane: the cut along $[0,\infty)$ (bold zigzag); the Euclidean point $q^2=-Q^2$ on the negative axis; the circle $|z|=s$ traversed counter-clockwise from $s+i0$ to $s-i0$ with arrows (`prop:ee-contour`); the two points $s\pm i\Delta$ (`prop:ee-smearing`); labels 「PT 可靠（欧氏）」 near the negative axis and 「共振区」 near small $s$.
   - **Caption draft:** 「流关联函数 $\Pi(q^2)$ 的解析结构：割线 $[0,\infty)$、欧氏点 $-Q^2$、围道公式的积分路径 $|z|=s$ 以及抹平所用的点 $s\pm i\Delta$。在复 $q^2$ 处使用 OPE 是额外的假设（\cref{rem:ee-complex-ope}）。」

### Ch9 `method`
9. **`fig:method-flowchart`** · Ch9 (`sec:method-strategy`) · TikZ flowchart, full width. **Updated for v2.**
   - **Draw:** six boxes in a vertical chain: 1 区域（Landau + 幂次计数）; 2 近似（共线/软，$i0$）; 3 Grammer–Yennie 分解; 4 Ward 恒等式 → Wilson 线; 5 减除 + 幺正性（末态相互作用、软因子）+ Glauber 围道变形（沿 $e_G$ 同时形变）; 6 因子化形式. Side annotations link each box to (H1)–(H5) of `thm:method-template` and, per `tab:method-hypotheses`, to the `asm:` labels: (H1) ↔ `asm:appN-envelope`, `asm:appN-separation`; (H2) ↔ `asm:appN-ward-product`; (H3) ↔ `asm:appO-mixing`, `asm:appO-deformation`, `asm:appO-rewritten-cs`; (H4) ↔ `asm:appN-cutsum`, `asm:appO-lcopt`; (H5) ↔ `asm:appN-collins`, `asm:appN-values`, `asm:appN-uv`, `asm:appN-multren`. A right margin column names the precise appendix theorems: `thm:appN-subtraction` (box 5), `thm:appO-main` (box 5, DY). Box colours: blue for [A] content, green where the step is [R] at the level used; the precise R_cond implications are drawn as dashed borders.
   - **Caption draft:** 「全阶因子化证明的六个步骤、它们与模板定理假设 (H1)–(H5) 的对应以及精确形式中的编号假设（附录~N、O）。」
10. **`fig:method-kg`** · Ch9 (`sec:method-gy`) · TikZ.
    - **Draw:** a collinear gluon between the $A$-collinear blob and $H$: left the full $g_{\mu\nu}$; middle the K term (`longit` with a dot, arrow showing $\frac{k_\mu n_{B\nu}}{n_B\cdot k-i0}$); right the G term labelled 「$\ge\lambda$ 压低」; below, the Ward identity turns the K term into a Wilson line along $n_B$.
    - **Caption draft:** 「Grammer–Yennie 分解：共线胶子的 K 部分经 Ward 恒等式化为 Wilson 线，G 部分幂次压低（例外：作为活动部分子的单个横向胶子，其领头项组成 $G^{+j}$）。」
    - **Start from:** `research/c_wilson/tex/c_wilson_gy.tex` (`fig:cw-kg`).
11. **`fig:method-nesting`** · Ch9 (`sec:method-regions`) · TikZ.
    - **Draw:** a Venn-like diagram in the (abstract) space of loop momenta: the hard region contains the collinear-$A$ and collinear-$B$ regions, which both contain the soft region (nested pinch surfaces $\pi_S\subset\pi_A,\pi_B$); arrows labelled $T_S$, $T_A$, $T_H$; the chain $C_A=T_A(1-T_S)$ written alongside; a side note 「只有分组表达式被压低（\cref{ex:method-naive-induction}）」.
    - **Caption draft:** 「区域的偏序与减除：最小区域（软）先近似，较大区域的近似子作用于减去较小区域贡献后的被积函数；单个链项一般不可积，只有分组表达式满足 (CS1)–(CS3)。」

### Ch10 `disall`
12. **`fig:disall-seed`** · Ch10 (`sec:disall-regions`) · TikZ.
    - **Draw:** one target-collinear K-gluon (`longit` with a dot, momentum $k$ into the hard part) attached to the struck quark of $H$ in all possible ways; an arrow to the right-hand side, where the gluon is attached to a future-pointing Wilson line $W[\infty n_B,0]$ (double line, $-i0$ in its eikonal propagator) at the quark field.
    - **Caption draft:** 「DIS 中 PDF Wilson 线的种子：一个靶共线 K 胶子对硬部分的所有附着之和，经 Ward 恒等式化为沿 $n_B$ 的未来指向 Wilson 线 $W^{(1)}[\infty n_B,0]$ 的单胶子项（VF-WL-8）。」
    - **Start from:** `research/c_wilson/tex/c_wilson_eikonal_ward.tex` (`fig:cw-dis-seed`).
13. **`fig:disall-heavy`** · Ch10 (`sec:disall-heavy`) · TikZ, two panels.
    - **Draw:** (a) $\gamma^*g\to Q\bar Q$ at LO with massive quark lines (thick); (b) the ACOT/CWZ subtraction term $f_{Q/g}\otimes(\gamma^*Q\to Q)$, drawn as the gluon splitting into a $Q\bar Q$ pair (blob labelled $f_{Q/g}$) followed by LO heavy-quark scattering.
    - **Caption draft:** 「含重夸克质量的 DIS：(a) 领头阶光子—胶子融合 $\gamma^*g\to Q\bar Q$；(b) 变味方案中的减除项 $f_{Q/g}\otimes\hat\sigma(\gamma^*Q\to Q)$，在 $m\to0$ 时抵消 $\ln(Q^2/m^2)P_{qg}$。」

### Ch11 `coll`
14. **`fig:coll-sia`** · Ch11 (`sec:coll-sia`) · TikZ.
    - **Draw:** $e^+e^-\to\gamma^*\to hX$ as a cut diagram: the photon enters a hard blob; a jet blob containing the observed hadron $h$ (momentum $p_h$, fraction $z$) crosses the cut; the other jet and the soft blob cross the cut; label $d_{h/q}(z/y)$ next to the fragmenting jet.
    - **Caption draft:** 「$e^+e^-\to hX$ 的领头区域：被观测强子所在的喷注给出碎裂函数，其余末态在割线求和中由幺正性相消（\cref{lem:coll-unobserved-jet}）。」
15. **`fig:coll-sidis`** · Ch11 (`sec:coll-sidis`) · TikZ.
    - **Draw:** the target blob (PDF, along $+z$) connects to a hard part with the virtual photon; the outgoing jet blob produces $h$ (FF); annotate $x$, $z$, $P_{hT}$ and the regimes 「$P_{hT}\sim Q$（共线）」 vs 「$P_{hT}\ll Q$（TMD，第~14~章）」.
    - **Caption draft:** 「半单举 DIS：$P_{hT}\sim Q$ 时为共线因子化 PDF$\otimes$硬部分$\otimes$FF；$P_{hT}\ll Q$ 时需要 TMD 因子化。」
16. **`fig:coll-photoproduction`** · Ch11 (`sec:coll-photo`) · TikZ, two panels.
    - **Draw:** (a) direct: the photon couples directly to the hard scattering with a parton from the proton; (b) resolved: the photon first splits into a hadron-like blob (photon PDF) that supplies a parton, so that the photon side has spectators.
    - **Caption draft:** 「光生过程：(a) 直接光子（单强子过程，[A]）；(b) 分辨光子（等效于强子—强子过程，[C]）。」

### Ch12 `dy`
17. **`fig:dy-abelian-model`** · Ch12 (`sec:dy-model`) · TikZ.
    - **Draw:** two eikonal spectator lines (one from each hadron, opposite directions) exchanging $n$ massive abelian bosons (`glauber` style), summed into the phase $e^{i\chi(b)}$; on the right the two cut placements (before/after the exchange) whose sum cancels for observables inclusive in the spectators' relative transverse momentum.
    - **Caption draft:** 「阿贝尔模型中旁观者之间的 Glauber 交换：对 $n$ 次交换求和给出冲量参数空间的相位 $e^{i\chi(b)}$，$\chi(b)=-\frac{g_Ag_B}{2\pi}K_0(m|b|)$；对旁观者相对横动量单举的截面中 $|e^{i\chi}|^2=1$，相位相消（VF-DY-13，VF-GLA-3）。」
    - **Start from:** `research/c_dy/dy_oneloop.tex` (`fig:dy1l-glauber`).

### Ch13 `thr`
18. **`fig:thr-kinematics`** · Ch13 (`sec:thr-refactorization`) · TikZ.
    - **Draw:** two incoming partons from $f_A$, $f_B$ produce $\gamma^*$ with $z=Q^2/\hat s\to1$; only soft radiation (green, energy $\sim Q(1-z)$). Second panel: $H\times S_{\rm DY}(Q(1-z))$ with the soft function made of two past-pointing Wilson lines.
    - **Caption draft:** 「阈值极限 $z\to1$：末态只剩能量 $\sim Q(1-z)$ 的软辐射，硬系数重新因子化为 $H\cdot S$；阈值因子化嵌套在共线因子化之内，只在 $(1-z)$ 的领头幂次受外层控制。」
19. **`fig:thr-mellin`** · Ch13 (`sec:thr-prescriptions`) · TikZ.
    - **Draw:** the complex $N$ plane: the rightmost PDF singularities on the real axis; the Landau branch point $N_L$ (schematic) labelled 「Landau 支点」; the minimal-prescription contour parallel to the imaginary axis between them, bending to the left at large $|{\rm Im}\,N|$.
    - **Caption draft:** 「Mellin 反演与 Landau 极点：最小处方的积分围道位于部分子分布的奇点与 Landau 支点之间。」

### Ch16 `jets`
20. **`fig:jets-sw-cone`** · Ch16 (`sec:jets-irsafe`) · TikZ.
    - **Draw:** two back-to-back cones of half-angle $\delta$ (shaded); particles inside; a soft particle outside with energy $<\epsilon\sqrt s$; annotate 「能量份额 $\epsilon$ 相对于总能量 $\sqrt s$」.
    - **Caption draft:** 「Sterman–Weinberg 两喷注定义：两个半张角 $\delta$ 的锥之外的总能量小于 $\epsilon\sqrt s$（VF-EE-12）。」
    - **Start from:** `research/c_ee/ee_total.tex` (`fig:ee-sw`).
21. **`fig:jets-ngl`** · Ch16 (`sec:jets-ngl`) · TikZ.
    - **Draw:** hemispheres L and R separated by the thrust axis, energy veto only in R; a harder gluon $k_1$ into L radiates a softer gluon $k_2$ into R, $\omega_2\ll\omega_1$; label 「$O(\alpha_s^2)$：$C_FC_A$」.
    - **Caption draft:** 「非全局对数的来源：未被测量区域中的较硬胶子向被否决区域辐射较软胶子；首项出现在 $O(\alpha_s^2)$，色因子 $C_FC_A$。」
22. **`fig:jets-gap`** · Ch16 (`sec:jets-sll`) · TikZ.
    - **Draw:** rapidity–azimuth plane: two jets at $y_1,y_2$; a hatched central gap with veto $E_T<Q_0$; beams at $y\to\pm\infty$; inset: a Coulomb/Glauber exchange (`glauber`) between the incoming partons dressed by a soft emission.
    - **Caption draft:** 「强子对撞中的“喷注间隙”可观测量；初态有色部分子间的 Coulomb/Glauber 交换与软辐射不对易，产生超领头对数；间隙截面的 PDF 因子化仍是猜想（有恢复的证据，\cref{…}）。」

### Ch17 `smallx`
23. **`fig:smallx-dipole`** · Ch17 (`sec:smallx-dipole`) · TikZ.
    - **Draw:** the virtual photon splits into a $q\bar q$ dipole of size $r=|x_0-x_1|$; the dipole crosses a target shock wave (vertical shaded slab with Wilson lines $V(x_0)$, $V^\dagger(x_1)$); one step of BK evolution: emission of a gluon at $x_2$ splits the dipole into $(x_0,x_2)$, $(x_2,x_1)$; kernel $\frac{x_{01}^2}{x_{02}^2x_{12}^2}$.
    - **Caption draft:** 「偶极子图像与 BK 演化：$q\bar q$ 偶极子穿过靶的冲击波；软胶子发射把偶极子分裂为两个，给出 BK 方程的非线性项（VF-MISC-4）。」
24. **`fig:smallx-map`** · Ch17 (`sec:smallx-status`) · TikZ.
    - **Draw:** the $(\ln1/x,\ln Q^2)$ plane: DGLAP region, BFKL direction, saturation line $Q_s^2(x)$ with the saturated region below (「饱和（[C]）」), DLA overlap; status tags: DGLAP [R] (PT), BFKL [A] (LL/NLL), $k_T$ factorization [P].
    - **Caption draft:** 「小 $x$ 物理的“地图”：DGLAP、BFKL、饱和区及各描述的严格性地位（小 $x$ 结果是 Regge 展开中固定对数精度下的陈述）。」

### Ch20 `heavy`
25. **`fig:heavy-bdpi`** · Ch20 (`sec:heavy-bdpi`) · TikZ.
    - **Draw:** $\bar B^0\to D^+\pi^-$: weak vertex (square), $B\to D$ transition (heavy lines; `bound state` for mesons), the emitted pion as a collinear $q\bar q$ pair (blue `jet blob`) with DA $\phi_\pi(x)$; soft gluons between the pion pair and the $B$–$D$ system decoupling at leading power (crossed gluon).
    - **Caption draft:** 「$B\to D\pi$ 的因子化：发射的 $\pi$ 为小色偶极子，软胶子在领头幂次退耦；振幅为 $F^{B\to D}(0)\otimes T\otimes\phi_\pi$。」
    - **Start from:** `research/c_scet/tex/c_scet_bdecays.tex` (`fig:b-dpi`).
26. **`fig:heavy-qcdf`** · Ch20 (`sec:heavy-qcdf`) · TikZ, two panels.
    - **Draw:** (a) vertex term $T^{\rm I}$; (b) hard spectator scattering $T^{\rm II}$ with a hard-collinear gluon from the spectator to the emitted meson; red marker on the endpoint region ($y\to0$) of $\phi_{M_1}$.
    - **Caption draft:** 「无粲 $B\to M_1M_2$ 的 QCD 因子化：(a) 顶点项，(b) 硬旁观者散射；红色标记扭度 3 与湮灭项中的端点发散。」
    - **Start from:** `research/c_scet/tex/c_scet_bdecays.tex` (`fig:qcdf`).

### Ch21 `power`
27. **`fig:power-borel-plane`** · Ch21 (`sec:power-renormalons`) · TikZ.
    - **Draw:** Borel $u$ plane: IR renormalon poles at $u=2,3,\dots$ (crosses), $u=1$ marked as absent for the Adler function (open circle 「无 $u=1$」); UV renormalons at $u=-1,-2,\dots$; integration path along the positive axis with the ambiguity from deforming above or below; annotation linking $u=2$ to $\langle\frac{\alpha_s}\pi G^2\rangle/Q^4$.
    - **Caption draft:** 「大 $\beta_0$ 近似下 Adler 函数的 Borel 平面：红外重整化子位于 $u=2,3,\dots$（无 $u=1$），对应于 OPE 中的凝聚项。」

### Ch22 `lamet`
28. **`fig:lattice-matching`** · Ch22 (`sec:lattice-matching`, keep the v1 label) · TikZ schematic.
    - **Draw:** two columns: left the lattice (Euclidean) quantity — quasi-PDF/pseudo-ITD at $P^z$ and $z^2$, with a box 「非微扰重整化（线性发散；混合方案）」; right the light-cone PDF $q(x,\mu)$; a middle arrow 「匹配 $C(\frac xy,\frac{\mu}{|y|P^z})$」 with the note 「$+O\big(\frac{\Lambda^2}{x^2P_z^2},\frac{\Lambda^2}{(1-x)^{2-\delta}P_z^2}\big)$」; underneath 「微扰匹配：全阶论证 [A]；强子层次：依赖编号假设 [C]」.
    - **Caption draft:** 「LaMET/短距离因子化的结构：格点可计算的等时关联函数经微扰匹配与光锥 PDF 相联系（匹配核的宗量是部分子动量 $|y|P^z$），误差为幂次修正；微扰的匹配定理是全阶论证，强子层次的陈述依赖于编号假设（见正文）。」

### Ch25 `summary`
29. **`fig:summary-status-map`** · Ch25 (`sec:summary-master`) · TikZ grid, full width.
    - **Draw:** rows = process classes, columns = levels {微扰论严格 [R], 全阶论证 [A], 部分 [P], 猜想 [C], 破坏 [V]}. Rows: $e^+e^-$ total, DIS moments, DIS $x$-space, SIA/SIDIS, DY/colour singlet, $pp\to$ jets, threshold, TMD (DY/SIDIS), TMD $h_1h_2\to h_3h_4$, SCET event shapes, small $x$, diffraction, DPS, exclusive, $B$ decays, NRQCD, power corrections, lattice/LaMET (collinear), quasi-TMD/LaMET-TMD, frontier OPE/regions/Landau. Each cell has a filled circle where the main result sits (tag colours); two circles where the PT and the hadronic statements differ (the hadronic one hollow, labelled with its bottleneck `asm:`). The rows must agree with `tab:summary-master`.
    - **Caption draft:** 「各类过程中因子化陈述的地位一览（与表~\ref{tab:summary-master} 一致）；空心圆表示强子层次陈述及其瓶颈假设。」
30. **`fig:summary-hypotheses`** · Ch25 (`sec:summary-hypotheses`) · TikZ bipartite graph. **Updated for v2.**
    - **Draw:** left column: the register entries grouped in boxes — global (`asm:intro-*`), OPE (`asm:appM-*`), subtraction (`asm:appN-*`), Glauber (`asm:appO-*`), frontier (`asm:lamet-*`, `asm:yzliu-*`, `asm:front-*`); right column: the main [A] and R_cond theorems (`thm:disall-factorization`, `thm:coll-sia`, `thm:dy-factorization`, `thm:tmd-factorization`, `thm:scet-thrust`, `thm:break-ddis`, `thm:break-double-dy`, `thm:excl-dvcs`, `thm:heavy-bdpi`, `thm:dis-moments-np`, `thm:appO-main`, the LaMET matching and quasi-TMD theorems). Edges from the generated `\uses` data (App P); edges to the bottleneck assumption of each theorem thick red.
    - **Caption draft:** 「主要全阶论证与条件定理所依赖的编号假设；粗红线为各定理的瓶颈（由 `\uses` 数据生成，与附录~P 一致）。」

### Optional v1 figures (draw only if within the page budget)

| label | owner | draw | start from |
|---|---|---|---|
| `fig:ir-landau-simplex` | Ch4 | Feynman-parameter simplex of the one-loop vertex with the Landau set (two edges, soft corner) highlighted; for the off-shell triangle the solutions sit at the simplex corners (`rem:ir-euclid-corners`, VF-REF-17) | `research/c_regions/landau.tex` (`fig:landau-simplex`) |
| `fig:pdf-gluon-operator` | Ch8 | cut-diagram representation of the gluon PDF: $G^{+j}$ vertices with the adjoint Wilson line | adapt `fig:pdf-operator` |
| `fig:pdf-ff-cut` | Ch8 | cut diagram of the fragmentation function (hadron frame, future-pointing lines, prefactor $z^{1-2\varepsilon}/(4N_c)$) | — |
| `fig:coll-transversity` | Ch11 | helicity-flip structure: transversity couples chiral-odd to chiral-odd (DY $h_1\otimes\bar h_1$, SIDIS $h_1\otimes H_1^\perp$); absent in inclusive DIS | — |
| `fig:tmd-evolution` | Ch14 | $(\ln\mu,\ln\sqrt\zeta)$ plane: evolution paths from $(\mu_b,\mu_b^2)$ to $(Q,Q^2)$, first in $\zeta$ (CS kernel $\tilde K$), then in $\mu$ ($\gamma_F$); path independence | — |
| `fig:scet-modes` | Ch15 | modes in the $(\ln\bar n\cdot p,\ln n\cdot p)$ plane with constant-virtuality lines; hard, collinear, (u)soft and Glauber points (VF-SCET-1) | `research/c_scet/tex/c_scet_scet.tex` (`fig:scet-modes`) |
| `fig:break-spacelike` | Ch18 | space-like collinear limit: incoming parton 2 and outgoing parton 3 collinear; Coulomb phases $\mathbf T_2\cdot\mathbf T_j$ | — |
| `fig:excl-erbl` | Ch19 | the four one-loop ERBL graphs with momentum fractions $x,y$ | `research/c_exclusive/tex/c_exclusive_da_erbl.tex` (`fig:cex-erbl-graphs`) |
| `fig:excl-endpoint` | Ch19 | pgfplots: ratio of LO $F_\pi$ for the CZ vs asymptotic DA, and endpoint contributions vs a cut $x>x_0$; alternatively (spec v2.1) the soft fractions $R_{\rm as}(c)$, $R_{\rm CZ}(c)$ of VF-EXC-14 against $Q^2$ for $\mu_0^2=1$ GeV$^2$ (closed forms, pgfplots expressions; $R=0.87,0.62,0.15$ resp. $0.98,0.90,0.48$ at $Q^2=4,10,100$ GeV$^2$) | `research/c_exclusive/tex/c_exclusive_formfactors.tex` (`fig:cex-endpoint`) |

**Further agent figures** a writer may use instead of drawing anew (relabel to `fig:<key>-<name>`, report): `research/c_ee/ee_total.tex` (`fig:ee-lo`, `fig:ee-nlo`, `fig:ee-2l`); `research/c_regions/powercounting.tex` (`fig:pc-ee`, `fig:pc-dis`, `fig:pc-dy`, `fig:pc-leading`, `fig:pc-modes`; App E may adapt one as `fig:appE-degree`); `research/c_scet/tex` (`fig:thrust-HJJS`, `fig:thrust-oneloop`, `fig:usoft-decoupling`, `fig:nrqcd-decay`, `fig:nqs-nnlo`); `research/c_exclusive/tex` (`fig:cex-da-def`, `fig:cex-pionff-lo`, `fig:cex-tff`, `fig:cex-dvcs-handbag`, `fig:cex-meson`); `research/c_dis/dis_oneloop.tex` (`fig:dis1l-diagrams`); `research/c_dy/dy_oneloop.tex` (`fig:dy1l-diagrams`); `research/c_pdf/tex/c_pdf_oneloop.tex` (`fig:cpdf-oneloop`).

---------------------------------------------------------------------------------------------------

## 3. Figures from the reference-document analysis (refdoc S56): 17 required + 5 optional

The reference document's figure numbers are given only for orientation; **redraw, never copy** (WRITER_SPEC_v2 §6.10). Owners by first use in v2.

### Ch4 `ir`
S1. **`fig:ir-mode-exponents`** · Ch4 (`sec:ir-power`) · TikZ, 3D-perspective axes, ≈7 cm.
- **Draw:** the exponent space $(a,b,c)$ of $(k^+,k^-,k_T)\sim(\lambda^a,\lambda^b,\lambda^c)Q$, drawn with three `lcaxis` arrows ($a$ to the right, $b$ into the page at 30°, $c$ up). The on-shell plane $c=\frac{a+b}2$ as a light grey parallelogram. Points: H $(0,0,0)$; C$_A$ $(0,2,1)$; C$_B$ $(2,0,1)$; ultrasoft $(2,2,2)$; TMD-soft $(1,1,1)$ at the centre of the plane; all five on the plane (filled dots). Glauber $(2,2,1)$ **below** the plane (open red dot, `red!60!black`) with a vertical dashed line to the plane point $(2,2,2)$ and the label 「$k^2\approx-k_T^2$，离壳」.
- **Caption draft:** 「模式在指数空间 $(a,b,c)$ 中的位置（$(k^+,k^-,k_T)\sim(\lambda^a,\lambda^b,\lambda^c)Q$）：硬、两种共线、软与超软模式都在在壳平面 $c=\frac{a+b}2$ 上，Glauber 模式 $(2,2,1)$ 位于平面之下（以横动量为主，离壳）。本书的“超软”即 Libby–Sterman 的“软”。」

### Ch6 `ee`
S2. **`fig:ee-cutsum-disc`** · Ch6 (`sec:ee-higher`) · TikZ, two panels.
- **Draw:** (a) the $O(\alpha_s^2)$ classes of cuts of the two-loop current-correlator self-energy (three small diagrams: two-, three-, four-particle cuts drawn with `cut`), each labelled 「单类至多 $1/\varepsilon^4$ 极点」 (`poles up to $1/\epsilon^4$ per class`); a brace 「求和」 → 「有限」. (b) the forward function $J\otimes S$ in the complex $s$ plane: its discontinuity across the real axis equals the cut sum; the integration contour can be moved to a circle at distance $O(Q)$ from the real axis (arrow), where no pinch remains. Add the Furry remark as a note: 「单态 $(\sum e_q)^2$ 项自 $O(\alpha_s^3)$ 起」.
- **Caption draft:** 「对割图求和等于前向函数的不连续性：单类割图的红外极点（至多 $1/\varepsilon^4$）在求和中相消；前向函数的围道可移到距实轴 $O(Q)$ 处，从而只剩欧氏可计算的部分。」

### Ch7 `dis`
S3. **`fig:dis-euclid-segment`** · Ch7 (`sec:dis-moments` or the section of `lem:dis-euclid-segment`) · TikZ.
- **Draw:** the complex $\omega$ plane (`lcaxis`), cuts $(-\infty,-1]$ and $[1,\infty)$ (bold zigzag), the unit circle (dotted), and on the imaginary axis the short segment $\mathcal I_Q=\{iy:|y|\le\sqrt3M/Q\}$ (thick blue); an inset magnifier showing the scale $M/Q$; a small arrow 「$Q\to\infty$：线段缩向原点」. Label the region $|\omega|<1$ 「$T_2$ 解析（\cref{prop:dis-dispersion-np}）」.
- **Caption draft:** 「欧氏 OPE 只在虚轴上长度为 $O(M/Q)$ 的线段 $\mathcal I_Q$ 上提供信息（VF-REF-1）；由此得到固定 $n$ 的矩还需要 $F_2\ge0$ 与有限减除的色散关系（\cref{thm:dis-fixed-n}），而 $n<n_0$ 的低阶矩还需要增长条件。」

### Ch9 `method`
S4. **`fig:method-hasse`** · Ch9 (`sec:method-regions`) · TikZ (Ch5 refers to it as a pointer only).
- **Draw:** left: the two-loop planar vertex (inner gluon $k_1$, outer gluon $k_2$) between the photon vertex and two outgoing massless lines $p_1$, $p_2$. Right: the Hasse diagram of its nine leading regions $(R(k_1),R(k_2))$, bottom to top: $(S,S)$; $(C_1,S)$, $(C_2,S)$; $(C_1,C_1)$, $(H,S)$, $(C_2,C_2)$; $(H,C_1)$, $(H,C_2)$; top $(H,H)$. Covering edges (12, as verified): $(S,S)\to(C_1,S),(C_2,S)$; $(C_1,S)\to(C_1,C_1),(H,S)$; $(C_2,S)\to(C_2,C_2),(H,S)$; $(C_1,C_1)\to(H,C_1)$; $(H,S)\to(H,C_1),(H,C_2)$; $(C_2,C_2)\to(H,C_2)$; $(H,C_1)\to(H,H)$; $(H,C_2)\to(H,H)$. A vertical arrow 「钳夹集增大」. Mark the non-obvious relation $(C_1,C_1)<(H,C_1)$ with a small note.
- **Caption draft:** 「两圈平面顶点九个领头区域的 Hasse 图（区域为逐线模式指定，逐线交运算封闭），例如 $(C_1,C_1)\wedge(H,S)=(C_1,S)$、$(H,C_1)\wedge(H,C_2)=(H,S)$、$(C_1,C_1)\wedge(C_2,C_2)=(S,S)$。」
S5. **`fig:method-neighbourhoods`** · Ch9 (section of `def:method-neighbourhoods`) · TikZ, abstract.
- **Draw:** an abstract loop-momentum domain $\Omega$ (rounded rectangle); nested neighbourhoods drawn as tubes/balls around pinch sets: a small ball $N_S$ (radius $\lambda^{\beta_S}$) around $\pi_S$, two tubes $N_{C_1}$, $N_{C_2}$ (widths $\lambda^{\beta_C}$) around two lines $\pi_{C_1},\pi_{C_2}$ through $\pi_S$; the dominance sets $U_S=N_S$, $U_{C_i}=N_{C_i}\setminus N_S$, $U_H=\Omega\setminus(N_{C_1}\cup N_{C_2})$ in different light fills; a legend 「$\beta_R=3^{h(R)-h_*}$：较小区域的邻域较“胖”」 and the covering statement $\bigcup_RU_R=\Omega$.
- **Caption draft:** 「依赖于 $\lambda$ 的邻域 $N_R=\{\sigma_{R(j)}(l_j)\le\lambda^{\beta_R}\}$ 与支配集 $U_R=N_R\setminus\bigcup_{R'<R}N_{R'}$；它们覆盖整个积分域（\cref{lem:method-covering}）。」
S6. **`fig:method-sudakov-plane`** · Ch9 (`ex:method-sudakov-subtraction`) · TikZ.
- **Draw:** the $(\ln|k^+|,\ln|k^-|)$ plane (axes in units $\ln(1/\lambda)$) for the off-shell one-loop triangle: the on-shell line $k_T^2=2k^+k^-$ for $k_T\sim\lambda Q$ as an anti-diagonal; the regions as corners/patches: $C_1$ near $(0,-2)$, $C_2$ near $(-2,0)$, $S$ at $(-1,-1)$, $H$ at $(0,0)$; overlapping soft–collinear strips hatched; a note on the contour: 「软近似只在 ${\rm Re}\,k^-\sim k_T^2/(4k^+)$ 附近穿过实轴的围道上成立」.
- **Caption draft:** 「Sudakov 平面中单圈离壳三角图的区域与软—共线重叠；减除项在重叠区相消的方式由分组表达式决定（\cref{ex:method-sudakov-subtraction}）。」
S7. **`fig:method-coeff-minus-coll`** · Ch9 (`ex:method-dis-oneloop`) · TikZ.
- **Draw:** one-loop DIS cut graphs on the left (ISR², ISR–FSR interference, FSR² with `cut`), minus their collinear approximations on the right (the ladder graph of the PDF operator ↔ ISR²; the Wilson-line graphs ↔ ISR–FSR interference), with an equals sign to 「系数函数 $C^{(1)}$」; matching colours connect each cut graph with its approximation.
- **Caption draft:** 「单圈 DIS 系数函数 = 割图减去其共线近似：ISR 的平方对应 PDF 算符的梯形图，ISR–FSR 干涉对应 Wilson 线图（VF-DIS-6，VF-PDF-3）。」
S8. **`fig:method-glauber-direction`** · Ch9 (`sec:method-glauber`; App O §O.7 refers back) · TikZ, three panels.
- **Draw:** (a) complex $k^-$ plane: deforming only $k^-$ (arrow up by $\kappa$) leaves $|k^+k^-|\sim\lambda^3\ll k_T^2$: the point stays inside the Glauber wedge $G_\delta=\{|k^+k^-|\le\delta k_T^2\}$ (drawn as a hyperbolic shaded region near the axes in the real $(k^+,k^-)$ plane); (b) the soft line's own pole at $k^-\sim k_T^2/(2k^+)$ limits a one-component deformation to $\kappa\sim k_T^2/|k^+|$; (c) the simultaneous deformation along $e_G=n_B-n_A$ ($\mathrm{Im}\,k^->0$, $\mathrm{Im}\,k^+<0$ for an amplitude-side soft momentum into $J_A$) with amplitude $\sim|k_T|$ leaves $G_\delta$ and makes all denominators more time-like: $(l+it\sigma fe_G)^2-m^2=(l^2-m^2+2t^2f^2)+2it\sigma f(l^+-l^-)$.
- **Caption draft:** 「离开 Glauber 区需要沿 $e_G=n_B-n_A$ 同时形变两个光锥分量：只形变一个分量时动量仍留在 $G_\delta$ 中（且受软线自身极点限制），同时形变使所有分母更类时（VF-REF-7）。」

### Ch10 `disall`
S9. **`fig:disall-ladder-regions`** · Ch10 (`ex:disall-ladder`) · TikZ.
- **Draw:** the two-rung ladder of DIS (target at bottom, photon vertex on top, two rungs $k_1$ (upper) and $k_2$ (lower)); three nested region boxes $R_2<R_1<R_H$ (`region` style): $R_2$ = both rungs collinear, $R_1$ = upper rung hard, lower collinear, $R_H$ = all hard; to the right the grouped remainder $r=\Delta\mathsf H_0\,\Delta K_2\,\Delta K_1$ and the note 「单个链项 $T_H(1-T_2)\Gamma$ 在 $U_{R_2}$ 上不可积，分组是必要的」.
- **Caption draft:** 「两级梯形图的三个区域 $R_2<R_1<R_H$ 与分组余项 $r=\Delta\mathsf H_0\Delta K_2\Delta K_1$；包含全硬区域 $R_H$ 才能得到两圈系数函数。」

### Ch12 `dy`
S10. **`fig:dy-pole-orientation`** · Ch12 (`lem:dy-poles-orientation`) · TikZ.
- **Draw:** a cut DY graph in hybrid light-cone ordering: $J_A$ ordered in $x^+$ (horizontal time axis above), $J_B$ ordered in $x^-$ (below); the hard vertex $V_H$ at $\tau=0$; intermediate states before and after $V_H$ marked with vertical dotted lines and labelled with the sign of their $i0$ (「$+i0$」 before, 「$-i0$」 after); a soft gluon $k$ connecting $J_A$ lines in both orientations, with a small complex $k^-$ plane inset showing poles on both sides (Glauber pinch) vs one side.
- **Caption draft:** 「取向是光锥序中间态的性质：$J_A$ 在硬顶点之前与之后的中间态给出相反符号的 $i0$；软动量所经过的中间态取向一致时 $k^-$ 极点在同一半平面，否则形成 Glauber 钳夹（\cref{lem:dy-poles-orientation}）。」
S11. **`fig:dy-two-gluon-exchange`** · Ch12 (`prop:dy-eikonal-twogluon`; App O §O.8 refers back) · TikZ.
- **Draw:** two infinite time-like eikonal lines (double lines, rapidity difference $Y$) with (a) the box (two uncrossed gluons $k$, $K-k$) and (b) the crossed box; under each its longitudinal integral $J_{\rm box}=\frac{2\pi}{ab}(\pi+iY)$, $J_{\rm cross}=-\frac{2\pi iY}{ab}$ and colour factor $c_{\rm box}=X^2$, $c_{\rm cross}=X^2+\frac{C_A}2X$ ($X=\mathbf T_A\cdot\mathbf T_B$); on the right the sum $\frac{2\pi}{ab}[\pi X^2-iY\frac{C_A}2X]$ split into 「指数化项」 and 「Regge 相位」.
- **Caption draft:** 「两条程函线之间的双胶子交换：全部 $s$ 道权重在非交叉图中，交叉图只贡献单圈 Regge 相位 $\propto C_AY$；因而 ${\rm Re}\,p_{\rm opp}=0$，$O(g^4)$ 的幺正性没有残差（VF-REF-9）。」 *(v2.3: claim N01 confirmed but known — no novelty wording; the caption may cite `Meggiolaro:1996hf`, `Giordano:2006vv`; rule 9.)*

### App M
S12. **`fig:appM-dependency`** · App M (`sec:appM-overview`) · TikZ graph.
- **Draw:** nodes: `asm:intro-wightman`, `asm:intro-composite`, `asm:intro-np-ope`, `asm:intro-af-coeff`, `asm:intro-growth`, `asm:appM-remainder`, `asm:appM-brst-ope` ((Eε)), `asm:appM-forward`, `asm:appM-oswi` (orange dashed boxes, top row); statements `prop:dis-dispersion-np`, `lem:dis-euclid-segment`, `lem:dis-ope-segment`, `thm:dis-fixed-n`, `prop:dis-low-moments`, `thm:dis-moments-np`, `cor:dis-weak-xspace`, `prop:dis-ope-euclid`, `prop:dis-ope-gi`, `prop:dis-ope-forward`, `thm:dis-moments` (tag-coloured boxes, middle and bottom rows), and (v2.3) the App M statements `lem:appM-ne`, `thm:appM-brst-reduction`, `thm:appM-forward-expansion`, `cor:appM-forward-ope`, `thm:appM-scaling`; edges from the `\uses` lists (in v2.3 `asm:appM-remainder` feeds `thm:appM-scaling` only); R_cond edges dashed.
- **Caption draft:** 「DIS 矩定理对编号假设的依赖（由各陈述的依赖表生成）：微扰部分只依赖 OPE 的三个子陈述，非微扰的固定 $n$ 定理依赖 Wightman 公理与非微扰 OPE，$n<n_0$ 还依赖增长条件。」
S13. **`fig:appM-handbag-ab`** · App M (`sec:appM-chain`) · TikZ, two panels.
- **Draw:** (a) the handbag drawn as an "AB part": the subgraph containing both current vertices (hard, $A$) and the rest ($B$), with the external momentum $q$ frozen in $A$; (b) the same handbag drawn as a reduced graph (hard vertex + collinear lines). Labels: 「AB 部分（正规乘积的语言）」 vs 「约化图（区域的语言）」.
- **Caption draft:** 「手提包图的两种读法：作为正规乘积展开中的 AB 部分（冻结 $q$），与作为区域分析中的约化图。」

### App O
S14. **`fig:appO-flowchart`** · App O (`sec:appO-overview`) · TikZ flowchart.
- **Draw:** eight boxes (O-1) regions, domain and windows; (O-2) leading-power form in LCOPT; (O-3) cut sum and one-sided rewriting; (O-4) consistency of the subtraction terms with the rewriting; (O-5) deformation target; (O-6) eikonal approximation and past-pointing Wilson lines; (O-7) soft factor $=1$ and collinear factors; (O-8) interface with App N. The assumptions `asm:appO-lcopt`, `asm:appO-envelope`, `asm:appO-mixing`, `asm:appO-deformation`, `asm:appO-rewritten-cs` as dashed orange boxes attached to the steps that use them; the lemmas proved without assumptions as green tags (v2.3: `lem:appO-side-independent-windows` at (O-3), [R, R_cond]); (v2.3) a separate box "§O.5 model theorems ([P])" with the side boxes `asm:appO-adjacent-swap`, `asm:appO-real-jets` (\tagP) and `asm:appO-collinear-ends` (\tagA), connected to (O-3) by a dotted line only (evidence, not a premise of `thm:appO-main`).
- **Caption draft:** 「单举色单态 DY 中 Glauber 相消的条件证明的结构（步骤 (O-1)–(O-8)）；橙色虚线框为所用的编号假设。」
S15. **`fig:appO-lcopt-term`** · App O (`sec:appO-lcopt`) · TikZ.
- **Draw:** one LCOPT term: vertices ordered along the light-cone time $\tau=x^+$ (horizontal axis), lines between them; vertical dashed lines mark intermediate states, each labelled with its energy denominator $\frac{1}{P^-_{\rm in}-\sum_jk_j^-+i0}$; one instantaneous line (with a bar); the hard vertex $V_H$ at $\tau=0$ highlighted.
- **Caption draft:** 「一个光锥序微扰论项：顶点按光锥时间排序，每个中间态给出一个能量分母，瞬时线单独标出，硬顶点位于 $\tau=0$。」
S16. **`fig:appO-cutsum`** · App O (`sec:appO-unitarity`) · TikZ, two panels.
- **Draw:** (a) the light-cone cut-position identity: the sum over cut positions of a chain of $N$ intermediate states with insertions equals two boundary terms (VF-GLA-5 structure with at most two insertion terms); (b) the closed-time-path picture: forward branch $U(\tau,0)$ and backward branch $U^\dagger$ joined at the final time, with final-state interactions internal to one jet cancelling.
- **Caption draft:** 「割线位置恒等式（含插入）与闭时路形式：对割线位置求和后，同一喷注内部的末态相互作用精确相消（\cref{lem:appO-unitarity}）。」

### App P
S17. **`fig:appP-dependency`** · App P · generated. Template in §4.9.

### Optional (refdoc S56)

| label | owner | draw | caption draft |
|---|---|---|---|
| `fig:dis-twist-graphical` | Ch7 | twist ↔ extra partons: handbag (twist 2), one extra transverse gluon ($\times\lambda$), one extra quark pair ($\times\lambda^2$) | 「扭度与额外部分子：每多一条横向胶子压低 $\lambda$，每多一对夸克压低 $\lambda^2$。」 |
| `fig:appE-boost` | App E | the boost-and-dimension argument: a region's scaling obtained by boosting a soft configuration and counting dimensions | 「推动与量纲给出幂次。」 |
| `fig:tmd-rapidity-bars` | Ch14 | rapidity axis with $y_B<y_{P_B}<y_n<y_{P_A}<y_A$; bars for the coverage of $\tilde f^{\rm unsub}_A(y_B)$, $\tilde f^{\rm unsub}_B(y_A)$, $\tilde S(y_A,y_B)$ and the split at $y_n$ | 「快度覆盖与平方根构造（\cref{lem:tmd-sqrt-identity}）。」 |
| `fig:appO-glauber-flow` | App O | Glauber flows through a graph and graded configurations (rapidity-ordered groups of soft momenta) | 「Glauber 流与分级构型。」 |
| `fig:break-measurement` | Ch18 | measurement operators that commute ($1$, $e^{i\mathbf b\cdot\hat{\mathbf P}_T}$) or not ($\Pi_h$, $\Pi_{\rm gap}$) with the light-cone evolution | 「测量相容性判据（\cref{prop:break-measurement}）。」 |

---------------------------------------------------------------------------------------------------

## 4. New figures of spec v2 (22 required + 11 optional)

Section labels marked "(proposed)" follow the drafts of the frontier reports; use FINAL_OUTLINE_v2's labels if they differ.

### 4.1 Ch2 `qcd` (pedagogical; WRITER_SPEC_v2 §7 asks for ≥ 4 figures)

N1. **`fig:qcd-vacuum-polarization`** · Ch2 (renormalization section, `sec:qcd-renorm`) · TikZ, 0.95\textwidth × ≈5 cm, four panels (a)–(d) in one row.
- **Draw:** each panel a one-loop correction to the gluon propagator: external gluons (coils, `gluon`) with momentum $k$ entering on the left (colour $a$, index $\mu$) and leaving on the right ($b$, $\nu$); `vertex` dots at the attachments.
  - (a) quark loop: a circle made of two `quark` arcs (fermion arrows in the same rotational sense) between two quark–gluon vertices; label 「$\times n_f$」.
  - (b) gluon loop: a circle in `gluon loop` style between two three-gluon vertices; label 「对称因子 $\frac12$」.
  - (c) ghost loop: a circle of two `ghost` arcs (arrows in one rotational sense) between two ghost–gluon vertices; label 「闭合鬼场圈带 $-1$」.
  - (d) tadpole: a gluon loop attached at a single four-gluon vertex on the straight external gluon line; label 「维数正规化中为零」.
  - Under the row, centred: $\delta Z_3=\frac{\alpha_s}{4\pi\varepsilon}\Big[\frac53C_A-\frac43T_Fn_f\Big]$（Feynman 规范；一般规范 $(\frac{13}6-\frac{\xi_g}2)C_A$）, and an arrow to 「与 $\delta Z_2$、$\delta Z_{1F}$ 合成 $\delta Z_g=-\frac{\alpha_s}{4\pi\varepsilon}\frac{\beta_0}2$」.
- **Caption draft:** 「胶子传播子的单圈修正（Feynman 规范，外线动量 $k$）：(a) 夸克圈（对 $n_f$ 味求和），(b) 胶子圈，(c) 鬼场圈，(d) 四胶子顶点的蝌蚪图（无标度积分，维数正规化中为零）。(b)(c) 单独都不满足横向性，三者之和正比于 $k^2g^{\mu\nu}-k^\mu k^\nu$；紫外极点给出 $\delta Z_3$，与夸克场和顶点的重整化常数合成规范无关的 $\delta Z_g$ 与 $\beta_0=\frac{11}3C_A-\frac43T_Fn_f$（VF-PDF-14，VF-QCD-4）。」

N2. **`fig:qcd-running-coupling`** · Ch2 (running-coupling section, `sec:qcd-running`) · pgfplots, two panels. **Tested starter code** (compiles with the preamble; render checked):
```latex
%%% BEGIN fig:qcd-running-coupling
\begin{figure}[htbp]\centering
\begin{tikzpicture}
\begin{axis}[name=A,width=0.49\textwidth,height=5.6cm,xmode=log,xmin=5,xmax=1000,ymin=0.08,ymax=0.22,
  xlabel={$Q/\mathrm{GeV}$},ylabel={$\alpha_s(Q)$},legend style={font=\scriptsize,draw=none,fill=none,at={(0.97,0.97)},anchor=north east},
  tick label style={font=\scriptsize},label style={font=\small},title={\small (a)}]
\addplot[domain=5:1000,samples=120,thick,dashed,blue!60!black]{0.1180/(1+(23/3)*0.1180/(4*pi)*ln(x^2/91.19^2))};
\addlegendentry{单圈}
\addplot[domain=5:1000,samples=120,thick,red!60!black]{4*pi/((23/3)*ln(x^2/0.2262^2))*(1-(116/3)/(23/3)^2*ln(ln(x^2/0.2262^2))/ln(x^2/0.2262^2))};
\addlegendentry{两圈（截断式）}
\addplot[only marks,mark=*,mark size=1.6pt,error bars/.cd,y dir=both,y explicit] coordinates {(91.19,0.1180) +- (0,0.0009)};
\node[font=\scriptsize,anchor=south west] at (axis cs:100,0.121) {$\alpha_s(M_Z)=0.1180$};
\node[font=\scriptsize,anchor=south west] at (axis cs:6,0.085) {$n_f=5$};
\end{axis}
\begin{axis}[at={(A.east)},anchor=west,xshift=1.3cm,width=0.49\textwidth,height=5.6cm,xmin=1.6,xmax=6.95,ymin=4.5,ymax=12,
  xlabel={$\ln(Q/\mathrm{GeV})$},ylabel={$1/\alpha_s(Q)$},tick label style={font=\scriptsize},label style={font=\small},title={\small (b)}]
\addplot[domain=1.609:6.908,samples=2,thick,blue!60!black]{1/0.1180+(23/3)/(2*pi)*(x-ln(91.19))};
\draw[->,thin] (axis cs:3.2,7.6) -- (axis cs:4.2,7.6) -- (axis cs:4.2,8.82);
\node[font=\scriptsize,anchor=west] at (axis cs:4.25,8.1) {斜率 $\beta_0/(2\pi)=1.22$};
\node[font=\scriptsize,align=left,anchor=north west] at (axis cs:1.75,11.7) {渐近自由：\\$Q\to\infty$ 时 $\alpha_s\to0$};
\end{axis}
\end{tikzpicture}
\caption{<caption draft below>}\label{fig:qcd-running-coupling}
\end{figure}
%%% END fig:qcd-running-coupling
```
- Numbers (VF-QCD-7, checked in `checks/vf_v2_checks.log`): $n_f=5$, $\beta_0=23/3$, $\beta_1=116/3$; $\alpha_s(10\,{\rm GeV})=0.1731$ (one loop), $0.1779$ (exact two loop), $0.1783$ (truncated formula with $\Lambda^{(5)}=0.2262$ GeV); the truncated two-loop formula is within 0.55 % of the exact two-loop running on $5\le Q\le1000$ GeV.
- **Caption draft:** 「跑动耦合 $\alpha_s(Q)$（$n_f=5$，输入 PDG 2024 世界平均 $\alpha_s(M_Z)=0.1180\pm0.0009$\cite[式~(9.25)]{ParticleDataGroup:2024cfk}）。(a) 单圈与两圈（截断式，$\Lambda^{(5)}_{\overline{\rm MS}}=0.226$ GeV）跑动；(b) 单圈下 $1/\alpha_s$ 对 $\ln Q$ 为直线，斜率 $\beta_0/(2\pi)>0$：$Q$ 越大耦合越弱，这就是渐近自由。$Q<m_b$ 处须改变 $n_f$，图中未画出。」

N3. **`fig:qcd-antiscreening`** · Ch2 (asymptotic-freedom section, `sec:qcd-af`) · TikZ, two panels + small inset, schematic.
- **Draw:** (a) QED: a test charge (circle with 「$+$」) at the centre, surrounded by a ring of eight small virtual $e^+e^-$ dipoles (short segments with 「$-$」 end towards the centre, 「$+$」 end outward); an outward arrow 「$r$ 增大」 and the text 「有效电荷随 $r$ 增大而减小（屏蔽）」. (b) QCD: a colour charge (circle with 「$\mathbf T$」) surrounded by (i) quark–antiquark dipoles as in (a), labelled 「夸克对：屏蔽，$-\frac43T_Fn_f$」, and (ii) a cloud of short `gluon` coils radiating outward and carrying colour (small colour-charge dots at their ends), labelled 「胶子：色荷外移，反屏蔽，$+\frac{11}3C_A$」. Inset below (b): two schematic curves of the effective coupling versus distance $r$ (log scale, no numbers): QED rising towards small $r$, QCD falling towards small $r$; label 「示意」.
- **Caption draft:** 「屏蔽与反屏蔽的直观图像（示意）。(a) QED：真空中的虚电子—正电子对屏蔽电荷，有效耦合在远处变小；(b) QCD：夸克对同样屏蔽（$-\frac43T_Fn_f$），而带色的胶子把色荷“涂抹”到更大的区域，在短距离处看到的色荷变小（反屏蔽，$+\frac{11}3C_A$）。二者之和 $\beta_0>0$（SU(3) 中 $n_f\le16$）。这只是启发式图像：规范无关的推导见\cref{prop:prelim-beta}，把反屏蔽解释为胶子自旋的顺磁效应见\cite{Nielsen:1980sx}。」

N4. **`fig:qcd-ir-safety`** · Ch2 (IR section, `sec:qcd-ir`) · TikZ, three panels.
- **Draw:** (a) an outgoing massless quark line ($p$) emitting a gluon ($k$) at angle $\theta$; the internal propagator labelled $\frac{1}{(p+k)^2}=\frac{1}{2E_pE_k(1-\cos\theta)}$; two small arrows 「软：$E_k\to0$」, 「共线：$\theta\to0$」; the phase-space factor $\frac{dE_k}{E_k}\frac{d\theta^2}{\theta^2}$. (b) real–virtual cancellation: a small cut diagram with the gluon crossing the cut (`cut`) 「实发射：$+\frac{2}{\varepsilon^2}+\dots$」, plus a virtual vertex correction interfering with the Born 「虚修正：$-\frac{2}{\varepsilon^2}-\dots$」, equals 「$\frac34C_F\frac{\alpha_s}\pi$（有限）」 (VF-EE-6, VF-EE-11). (c) two final states, a two-parton state and a three-parton state obtained by adding a soft gluon or splitting one parton into two collinear ones; a box 「红外安全：$O_{n+1}\to O_n$」 (e.g. thrust, Sterman–Weinberg cross section) and a crossed-out box 「不安全：末态部分子数」.
- **Caption draft:** 「红外发散与红外安全（示意）。(a) 无质量夸克发射胶子：传播子在软（$E_k\to0$）与共线（$\theta\to0$）极限下发散；(b) 对足够单举的量，实发射与虚修正的发散相消（$e^+e^-$ 总截面，VF-EE-6）；(c) 红外安全可观测量在软发射与共线劈裂下取值不变，因而可以逐阶微扰计算（精确定义见\cref{def:ir-safe}）。」

Optional (Ch2):
- **`fig:qcd-gauge-orbit`** · TikZ: the space of gauge fields drawn as a plane; gauge orbits $\{A^U\}$ as curves; a gauge-fixing surface $F(A)=0$ crossing each orbit once (the Faddeev–Popov determinant = the Jacobian at the crossing), and a far region where it crosses an orbit twice, labelled 「Gribov 复本（微扰论中不出现）」. Caption: 「规范固定与 Faddeev–Popov 行列式（示意）：规范固定曲面与每条规范轨道相交一次，交点处的 Jacobian 给出鬼场。」
- **`fig:qcd-colour-flow`** · TikZ: double-line ('t Hooft) notation: a gluon as a quark–antiquark line pair; the Fierz identity $t^a_{ij}t^a_{kl}=\frac12(\delta_{il}\delta_{kj}-\frac1N\delta_{ij}\delta_{kl})$ drawn diagrammatically; the colour factors $C_F$ (quark self-energy) and $C_A$ (gluon loop) as two small diagrams. Caption: 「色流（双线）记号与 Fierz 恒等式；$C_F=\frac{N^2-1}{2N}$ 与 $C_A=N$ 的图示（VF-QCD-1）。」

### 4.2 Ch22 `lamet`

N5. **`fig:lamet-ioffe`** · Ch22 (`sec:lattice-quasi`, the v1 section label; the label `sec:lamet-objects` proposed in v2.1 is not used) · TikZ (or pgfplots), ≈0.8\textwidth × 6 cm.
- **Draw:** axes: horizontal Ioffe time $\lambda=P\cdot z$ (only $\lambda\ge0$ shown, $0\le\lambda\le16$), vertical $|z|$ in fm ($0\le|z|\le1.2$). Elements:
  - the $\lambda$ axis drawn bold and labelled 「光锥 ITD $I(\lambda)$（$z^2=0$）」;
  - three dashed rays through the origin, $|z|=0.1973\,\lambda/(P^z/{\rm GeV})$ fm for $P^z=1,2,3$ GeV, labelled 「准分布：固定 $P^z$」 and 「$P^z=1,2,3$ GeV」; an arrow along the family 「$P^z\to\infty$」 pointing towards the $\lambda$ axis;
  - three horizontal dotted lines $|z|=0.1,0.2,0.3$ fm labelled 「赝分布：固定 $z^2$」;
  - a light shaded band $|z|\le0.3$ fm labelled 「短距离因子化（SDF）」;
  - a lighter rectangle $|z|\le1$ fm, $\lambda\le15$ labelled 「格点数据区（示意）」.
- **Caption draft:** 「Ioffe 时间 $\lambda=P\cdot z$（$=-P^zz$）与间隔 $|z|$ 平面上的三种表示：光锥 ITD 位于 $z^2=0$；固定 $z^2$ 的水平线给出赝分布（对 $\lambda$ 作 Fourier 变换，支集 $[-1,1]$）；固定 $P^z$ 的射线 $|z|=|\lambda|/P^z$ 给出准分布（$z$ 与 $\lambda$ 同时变化），$P^z$ 增大时射线趋向光锥轴。短距离因子化只用阴影带内的数据，准分布的 Fourier 变换需要整条射线（长距离部分见正文）。」

N6. **`fig:lamet-oneloop`** · Ch22 (one-loop section, `sec:lamet-oneloop`) · TikZ, five small panels in one row (≈0.95\textwidth).
- **Draw:** in each panel the operator is a horizontal double line (`wilson plain`) between two `opvertex` nodes labelled $0$ and $z\hat e_z$ (axis note 「等时，沿 $\hat z$」); the incoming quark ($p$, `quark`) enters the vertex at $0$ from below-left and the outgoing quark leaves the vertex at $z$ to below-right (forward matrix element; no cut).
  - (a) vertex: a gluon (`gluon`) between the incoming and the outgoing quark lines below the operator;
  - (b) sail: a gluon from the incoming quark line to a point of the Wilson line;
  - (c) mirror sail: from the outgoing quark line to the Wilson line;
  - (d) Wilson-line self-energy: a gluon arc with both ends on the double line;
  - (e) quark self-energy on an external leg (drawn lighter, 「外线自能」).
  - Under (a), (b)+(c), (d) the unphysical-region contributions ($\xi>1$, VF-LAM-7): $a\int_0^1dy\frac{1-y}{|\xi-y|}$, $\frac a{1-\xi}\int_0^1dy\frac{\xi+y}{|\xi-y|}$, $-\frac a{|1-\xi|}$.
- **Caption draft:** 「准 PDF 的单圈图（Feynman 规范，在壳无质量夸克 $p=(p^z,0,0,p^z)$，$\Gamma=\gamma^0$）。双线为沿 $\hat z$ 的类空 Wilson 线 $W[z\hat e_z,0]$，$\otimes$ 为算符端点：(a) 顶点图，(b)(c) “帆”图，(d) Wilson 线自能，(e) 外线自能。非物理区 $\xi>1$ 中各图有限，其和为 $a[\frac{1+\xi^2}{1-\xi}\ln\frac{\xi}{\xi-1}+1]$（$a=\frac{\alpha_sC_F}{2\pi}$，VF-LAM-7）；维数正规化中 Wilson 线自能没有线性发散。」

N7. **`fig:lamet-hybrid`** · Ch22 (schemes section, `sec:lamet-schemes`) · TikZ, two panels, schematic.
- **Draw:** (a) a $|z|$ axis from $0$ to $1.2$ fm split at $z_S\approx0.2$–$0.3$ fm: left interval labelled 「比值方案：$\tilde h(\lambda,z^2)/\tilde h(0,z^2)$」, right interval 「Wilson 线质量减除：$e^{\delta m|z|}Z_{\rm hyb}$，$Z_{\rm hyb}$ 由 $z_S$ 处连续性确定」. (b) schematic curves of the conversion factor to $\overline{\rm MS}$ versus $|z|$: ratio/RI-MOM (rising like $\ln z^2$ and entering a grey band 「非微扰：$\alpha_s(1/|z|)$」 at large $|z|$), hybrid (equal to the ratio curve up to $z_S$, then flat); label 「示意」.
- **Caption draft:** 「混合重整化方案（示意）：$|z|\le z_S$ 用比值方案，紫外发散与 $e^{\delta m|z|}$ 在比值中相消；$|z|>z_S$ 只减去 Wilson 线的线性发散与对数因子，到 $\overline{\rm MS}$ 的换算因子在所有 $|z|$ 上都是微扰的，因此动量空间匹配成立。比值方案与 RI/MOM 方案在大 $|z|$ 处含 $\alpha_s(1/|z|)$，动量空间匹配没有依据。单圈混合核满足 $\int d\xi\,C_{\rm hyb}=1$（VF-LAM-10）。」

N8. **`fig:lamet-lattice-geometries`** · Ch22 (renormalization/lattice section, `sec:lamet-renorm`) · TikZ on a light grey lattice grid (spacing ≈0.35 cm, `gray!25`), three panels.
- **Draw:** (a) quasi-PDF operator: filled dot $\psi(0)$ at the origin, open dot $\bar\psi(z\hat e_z)$ at distance $z$ along the horizontal $\hat z$ axis, the chain of links between them as a double line; label $\bar\psi(z)\Gamma W[z,0]\psi(0)$. (b) quasi-TMD operator: $\psi(0)$ at the origin, $\bar\psi$ at $z\hat e_z+\vec b_\perp$ (vertical offset $b_\perp$); staple: from $0$ along $+\hat z$ to $L$, transverse link to $(L,b_\perp)$, back along $-\hat z$ to $(z,b_\perp)$; labels $L$, $b_\perp$, arrow 「$L\to\infty$」. (c) rectangular Wilson loop of size $2L\times b_\perp$ labelled $Z_E(2L,b_\perp)$.
- **Caption draft:** 「格点上的算符几何（等时面，晶格间距 $a$）：(a) 准 PDF 算符的直 Wilson 线；(b) 准 TMD 算符的订书钉形 Wilson 线（长 $L$，横向间隔 $b_\perp$）；(c) 矩形 Wilson 圈 $Z_E(2L,b_\perp)$，$\sqrt{Z_E}$ 除去订书钉的线性发散、尖点发散与捏点奇点，使 $L\to\infty$ 的极限存在。手征对称性不严格的格点费米子还引起同维混合 $\Gamma\to\Gamma'$（正文）。注意：这里的订书钉是类空的，与\cref{fig:tmd-staple}中的类光订书钉不同。」

Optional (Ch22):
- **`fig:lamet-fourier`** · pgfplots: $|\tilde h(\lambda)|=Ae^{-m\lambda/P^z}$ (log $y$) for $m=0.5$ GeV, $P^z=2$ GeV on $0\le\lambda\le20$; the data window $\lambda\le\lambda_L=z_LP^z$ with $z_L=1$ fm ($\lambda_L\approx10.1$) shaded; the truncated tail hatched with the bound $\frac{AP^z}{\pi m}e^{-mz_L}$, $e^{-mz_L}=0.079$; inset: the strip $|{\rm Im}\,x|<m/P^z$ in the complex $x$ plane. Caption: 「Fourier 变换的截断误差与解析带：在指数衰减假设下，准 PDF 在 $|{\rm Im}\,x|<m/P^z$ 中解析，截断误差不超过 $\frac{AP^z}{\pi m}e^{-mz_L}$；对现有的 $z_L$ 这一压低并不是参数上小的（VF-LAM-17）。」
- **`fig:lamet-dependency`** (proposed by the frontier outline, adopted at the merge; FINAL_OUTLINE_v2 Part VII annex §F4 item 1) · TikZ (`sec:lattice-matching`): the dependency graph of `tab:lamet-dependency` — nodes `asm:lamet-aux-renorm` → `prop:lattice-renormalizability` → `asm:lamet-ope` → `thm:lamet-coordinate` → `thm:lamet-parton-momentum` → `thm:lattice-lamet` → `thm:lamet-hadronic`, with `prop:lamet-support`, `cor:lamet-entire`, `prop:lamet-cfp`, `thm:lamet-lcs`, `prop:lamet-tmc`, `lem:lamet-fourier`, `asm:lamet-uniform`, `asm:lamet-twist4`, `asm:lamet-large-z`; styles of §4.9 rules 3–5 (fill by tag; assumptions dashed orange; R_cond dashed); may be generated with the App P generator restricted to Ch22. Caption draft: 「LaMET 匹配定理的依赖结构：箭头指向依赖者；颜色表示标签；红色节点是强子层次陈述的编号假设（见\cref{tab:lamet-dependency}）。」 Claim N11 (K5): a presentation, no novelty wording.
- **`fig:lamet-validity`** · TikZ: the $x$ axis $[0,1]$ with excluded strips $x\lesssim\Lambda/P^z$ and $1-x\lesssim\Lambda/P^z$; schematic relative power corrections $\Lambda^2/(x^2P_z^2)$ and $\Lambda^2/((1-x)^{2-\delta}P_z^2)$ ($\delta=0,1$ dashed/dotted); a bracket 「阈值重求和把大 $x$ 边界推到 $(1-x)P^z\gg\Lambda$」. Caption: 「LaMET 预言的适用范围（示意）：端点区要求 $2xP^z$ 与 $(1-x)P^z$ 都远大于 $\Lambda$；两种大 $x$ 计数规则对应扭度 4 分布的不同端点行为（VF-LAM-12）。」

### 4.3 Ch23 `yzliu`

N9. **`fig:yzliu-soft-hqet`** · Ch23 (soft-function section, `sec:yzliu-soft`) · TikZ, two panels.
- **Draw:** (a) in the $(z,t)$ plane plus a perspective transverse axis $b_\perp$: two staple-shaped Wilson loops built from time-like lines along $v=\gamma(1,\beta,\mathbf 0)$ (past, $t<0$) and $v'=\gamma'(1,-\beta',\mathbf 0)$ (future, $t>0$) at transverse positions $0$ and $b_\perp$, closed by transverse links at $\pm t$; a `T` ordering label; the denominator $\sqrt{Z(2t,b_\perp,Y)Z(2t',b_\perp,Y')}$ written beside. (b) HQET picture: two world-lines (colour sources $Q$ at $0$ and $\bar Q$ at $b_\perp$, `bound state` style for the pair) moving with $v$ for $t<0$, kicked at $t=0$ by the current $J$ (`opvertex` on each line) to $v'$; the states $|Q\bar Q,b_\perp\rangle_v$ and ${}_{v'}\langle Q\bar Q,b_\perp|$ labelled; a small inset with Euclidean time $\tau$ and $i\tilde v\cdot D_E=D_\tau-i\beta D_z$.
- **Caption draft:** 「离光锥 TMD 软函数作为快速色源对的形状因子：(a) 方向 $v$、$v'$（快度 $Y$、$Y'$）、横向间隔 $b_\perp$ 的两个订书钉形 Wilson 回路的时序真空期望，除以 $\sqrt{ZZ}$ 后取 $t,t'\to\infty$；(b) 等价的 HQET 图像：间隔 $b_\perp$ 的色单态静态 $Q\bar Q$ 对以速度 $v$ 运动，在 $t=0$ 被流 $J$ 踢到 $v'$，软函数是 ${}_{v'}\langle Q\bar Q,b_\perp|J|Q\bar Q,b_\perp\rangle_v$，因而有欧氏表示。大快度下 $\ln S=(Y+Y')\tilde K+\mathcal D+O(e^{-(Y+Y')})$，本征软函数 $S_I=e^{-\mathcal D}$（VF-YZL-2；全阶论证）。」

N10. **`fig:yzliu-leading-region`** · Ch23 (quasi-TMD section, `sec:yzliu-quasi-tmd`) · TikZ, two panels.
- **Draw:** (a) double-line notation: the collinear subgraph $C$ (`jet blob`, hadron $P$ along $\hat z$) at the bottom; two small hard blobs $H$ (`hard blob`) at the two quark–link junctions (positions $0$ and $\lambda\hat z/P^z+\vec b_\perp$); from each $H$ a space-like Wilson line runs along $+\hat z$ to $L$, closed by a transverse link (staple, double lines); a soft blob $S$ (`soft blob`) connected to the staple and to $C$ by soft gluons; several longitudinal collinear gluons from $C$ into each $H$ (`longit` with `\longitmark`); two collinear quark lines from $C$ into the two $H$. (b) single-line notation: the staple pair replaced by one thick dashed 「偶极线（量纲 $3/2$，自旋 $0$）」; the counting box $F(H)=-\frac72+2+\frac32=0$, $F(SC)\ge0$.
- **Caption draft:** 「准 TMD 的领头区域：(a) 双线记号——共线子图 $C$、位于两个夸克—规范线连接点的硬顶点 $H$、类空订书钉与软子图 $S$，$C$ 与 $H$ 间可有任意多条纵向共线胶子，$S$ 与 $C$ 间可有任意多条软胶子；(b) 单线记号——一对订书钉线合成一条量纲 $3/2$、自旋 $0$ 的偶极线。幂次计数 $F(H)=0$、$F(SC)\ge0$ 表明没有超领头区域，且硬动量不能在 $0$ 与 $b_\perp$ 之间传递，匹配中没有 $x$ 卷积（VF-YZL-8）。」

N11. **`fig:yzliu-theta-strip`** · Ch23 (analyticity section, `sec:yzliu-analyticity`) · TikZ.
- **Draw:** the complex $\theta$ plane: horizontal ${\rm Re}\,\theta$ (= $Y$), vertical ${\rm Im}\,\theta$ with ticks at $\pm\frac\pi2$, $\pm\pi$; the strip $-\pi\le{\rm Im}\,\theta\le\pi$ lightly shaded; at a fixed ${\rm Re}\,\theta=Y_0$ five marked points with short labels (from VF-YZL-4): $Y_0$ 「类空/类空，过去/过去；类时/类时，过去/未来」; $Y_0-i\pi$ 「类时/类时，过去/过去」; $Y_0+i\pi$ 「类空/类空，过去/未来」; $Y_0+\frac{i\pi}2$ 「类时/类空，过去/未来」; $Y_0-\frac{i\pi}2$ 「类时/类空，过去/过去」; an arrow to the right 「$Y\to\infty$：光锥极限（假设对 ${\rm Im}\,\theta$ 一致）」.
- **Caption draft:** 「离光锥软函数对双曲角的解析性：单一时序的减除软函数只通过 $\theta(v_1,v_2)$ 依赖于方向，是带形 $-\pi\le{\rm Im}\,\theta\le\pi$ 上同一解析函数的边界值；图中标出类空/类时、过去/未来指向的六种组合所对应的 $\theta$（VF-YZL-4）。由此在微扰论各阶 $S_{\rm DY}=S_{\rm FF}$（全阶论证；所需假设见正文）。」

N12. **`fig:yzliu-complex-lorentz`** · Ch23 (time-ordering section, `sec:yzliu-time-ordering`) · TikZ, two panels and a connecting arrow.
- **Draw:** left panel, real $(z,t)$ plane: two light-like directions $n$ and $\bar n$ (dashed diagonals) from the origin (Wilson lines $W_n(0)$, $W_{\bar n}(0)$ inside a `T` product) and the same pair at the shifted point $b_\perp-i\nu e_t$ (drawn as a parallel pair displaced, with a label 「虚时间位移 $-i\nu e_t$」, inside $\bar T$); title 「$S$：DY 形，指数正规子」. Right panel: the pair at $0$ and the pair at $b_\perp-\nu e_z$ (real space-like shift), all inside one `T`; title 「$S_t$：单一时序的类空形状因子」. Between the panels a thick arrow labelled $\Lambda(t,z)=(iz,it)$ with the dictionary $\Lambda(-i\lambda n)=\lambda n$, $\Lambda(-i\lambda\bar n)=-\lambda\bar n$, $\Lambda(-\nu e_z)=-i\nu e_t$. Below: the invariant lengths $x^2_{B,ij}=-\nu^2-b_\perp^2-\sqrt2i\nu(\lambda_i^L-\lambda_j^R)$ with the remark 「实部 $\le-b_\perp^2-\nu^2<0$：阈下、无割线」.
- **Caption draft:** 「时序无关性的解析延拓图像：指数正规子下的 DY 形软因子 $S$（左）与单一时序的类空形状因子 $S_t$（右）由复 Lorentz 变换 $\Lambda(t,z)=(iz,it)$ 相联系；所有不变间隔的实部都为负（阈下表示）。在维数正规化中胶子 Wightman 函数满足谱条件与局域对易性的假设下，微扰论各阶 $S=S_t$（全阶论证，VF-YZL-12）。」

N13. **`fig:yzliu-threshold`** · Ch23 (threshold section, `sec:yzliu-threshold`) · TikZ, two panels.
- **Draw:** (a) comparison: DIS at $x\to1$ — a narrow final-state jet and soft radiation between the jet and the target remnant. (b) quasi-PDF kernel at $\xi\to1$: a collinear quark (momentum $p^z$) enters and leaves the space-like Wilson line at the two junctions (hard vertices, scale $\zeta_z=4p_z^2$); semi-hard gluons (momenta $\sim|1-\xi|p^z$, drawn as soft-green coils) exchanged between the collinear quark line and the static link; a dashed box around the link and these gluons labelled 「类空喷注函数 $\tilde J$」; below, $C\to H(\frac{4p_z^2}{\mu^2})\,p^z\,J_f\big(\frac{(1-\xi)p^z}\mu,\frac{4p_z^2}{\mu^2}\big)$.
- **Caption draft:** 「阈值因子化的时空图像：(a) $x\to1$ 的 DIS；(b) $\xi\to1$ 的准 PDF 匹配核——共线夸克在类空 Wilson 线的两个连接点处发生硬相互作用（标度 $4p_z^2$），与静态规范线之间交换半硬胶子（标度 $|1-\xi|p^z$），后者组成带相位的类空喷注函数。$C=H\,p^zJ_f$ 在单圈精确成立、两圈与全部 41 个奇异项一致（VF-LAM-14，VF-YZL-9）。」

Optional (Ch23):
- **`fig:yzliu-borel`** · TikZ: the Borel $u$ plane of the heavy–light Sudakov kernel at large $\beta_0$; a pole at $u=\frac12$ marked 「只在虚部」; the normalization $N_m=C_Fe^{5/6}/\pi\approx0.977$; caption: 「重—轻 Sudakov 核的线性红外重整化子位于 $u=\frac12$，只出现在虚部（相位）中，与次领头幂次算符的紫外重整化子相消（大 $\beta_0$，部分结果）。」
- **`fig:yzliu-single-line`** · TikZ: single-line notation of a staple pair and the dipole 2PI decomposition (self-interaction webs vs operator–link 2PI vertices); caption: 「单线记号与偶极子 2PI 分解：自相互作用 web 指数化后被 $\sqrt{Z_E}$ 除去（部分指数化引理）。」

### 4.4 Ch24 `front`

N14. **`fig:front-gordan`** · Ch24 (Landau section, `sec:front-landau`) · TikZ, two panels in a 2D dual space.
- **Draw:** (a) three arrows $D_1,D_2,D_3$ from the origin whose convex hull (shaded triangle) does not contain $0$; the min-norm point $w$ of the hull (dot, with a dashed perpendicular from $0$); the open cone $\{v:D_j\cdot v>0\ \forall j\}$ lightly shaded with $w$ inside it; label 「$D_j\cdot w\ge|w|^2$：好方向」. (b) three arrows whose hull contains $0$; weights $\lambda_1,\lambda_2,\lambda_3\ge0$ with $\sum\lambda_jD_j=0$ indicated by a closed polygon of scaled arrows; label 「Landau 点：无好方向」.
- **Caption draft:** 「Gordan 二择一定理（1873）：对有限个对偶矢量 $D_j$，要么存在好方向 $v$（$D_j\cdot v>0$，可取凸包中范数最小的点 $w$，并有 $D_j\cdot w\ge|w|^2$），要么存在 Landau 点（$\lambda_j\ge0$ 不全为零、$\sum_j\lambda_jD_j=0$），二者恰有其一。在 Collins（2020，预印本）的符号条件下，积分围道在 $w_S$ 被钳住当且仅当存在 Landau 点（VF-FRO-1，VF-FRO-2）。」

N15. **`fig:front-regions-polytope`** · Ch24 (regions section, `sec:front-regions`) · TikZ, two panels, schematic.
- **Draw:** (a) a 2D projection of a Newton polytope (convex polygon) of the Lee–Pomeransky polynomial with all coefficients positive: vertices = exponents of the monomials; the lower facets (with inward normals pointing up, $r_{n+1}>0$) highlighted and labelled H, C$_1$, C$_2$, S; normals drawn as short arrows. (b) the Minkowski case: a monomial pair with opposite signs whose cancellation creates a pinch inside the parameter domain (a red cross inside the polygon); after "dissecting the polytope" along the singular locus a new lower facet appears (dashed), labelled 「隐藏区域（如 Glauber）」 and 「三圈非平面 $2\to2$」.
- **Caption draft:** 「区域方法的几何（示意）：(a) 当 $\mathcal U+\mathcal F$ 的系数全为正（欧氏型）时，区域对应 Newton 多面体的本质下表面，法向量给出各 Feynman 参数的标度；(b) Minkowski 运动学中异号项的相消在参数空间内部产生钳夹，标准的下表面算法漏掉相应区域，沿奇异轨迹剖分后出现新的面——“隐藏区域”\cite{Gardi:2024axt}。“区域 = 下表面”作为一般陈述在 Minkowski 运动学中不成立。」

N16. **`fig:front-endpoint`** · Ch24 (NLP section, `sec:front-nlp`) · TikZ, two panels.
- **Draw:** (a) $h\to\gamma\gamma$ via a $b$-quark loop: a scalar line (`scalar`) for $h$ entering a triangle of heavy quark lines (thick `quark`), two outgoing photons (`photon`) along $n_1$ and $n_2$; the $b$ line between the two photon vertices drawn green and labelled 「软夸克」, the other two lines blue/orange labelled 「$n_1$、$n_2$ 共线」. (b) the third term of the factorization theorem: $H_3$ (hard blob) × two radiative jet functions $J$ (`jet blob`, `jetB blob`) ⊗ the soft-quark function $S$ (`soft blob`), with the convolution variables $\ell_+$, $\ell_-$ and a red bracket at $\ell_\pm\to0$ 「端点发散」; a note 「重因子化条件 ⇒ 各项分别有限」.
- **Caption draft:** 「第一个完整的端点因子化定理：$h\to\gamma\gamma$ 的 $b$ 夸克圈（$\lambda=m_b/M_h$，次领头幂次振幅）。(a) 软夸克在两个光子共线扇区之间交换；(b) 第三项 $H_3\,J\otimes J\otimes S$ 在端点 $\ell_\pm\to0$ 发散，重因子化条件把端点发散在各项之间重新分配，给出各项分别有限的重整化定理，并再现领头双对数 ${}_2F_2(1,1;\frac32,2;-\frac{C_F\alpha_s}{8\pi}\hat L^2)$（全阶论证，VF-FRO-9）。」

N17. **`fig:front-yukawa-pdf`** · Ch24 (positivity section, `sec:front-positivity`) · pgfplots. **Tested starter code:**
```latex
%%% BEGIN fig:front-yukawa-pdf
\begin{figure}[htbp]\centering
\begin{tikzpicture}
\begin{axis}[width=0.62\textwidth,height=6cm,xmin=0,xmax=1,ymin=-0.6,ymax=3.6,xlabel={$\xi$},ylabel={$f^{\overline{\rm MS}}_{q/p}(\xi;\mu)/a_\lambda$},
  tick label style={font=\scriptsize},label style={font=\small},legend style={font=\scriptsize,draw=none,fill=none,at={(0.97,0.97)},anchor=north east}]
\addplot[domain=0.001:0.999,samples=200,thick,red!60!black]{(1-x)*(ln(0.8^2/(2.25*x+0.09*(1-x)-x*(1-x)))-1+(0.3+x)^2/(2.25*x+0.09*(1-x)-x*(1-x)))};
\addlegendentry{$\mu=0.8$ GeV}
\addplot[domain=0.001:0.999,samples=200,thick,dashed,orange!80!black]{(1-x)*(ln(1.2^2/(2.25*x+0.09*(1-x)-x*(1-x)))-1+(0.3+x)^2/(2.25*x+0.09*(1-x)-x*(1-x)))};
\addlegendentry{$\mu=1.2$ GeV}
\addplot[domain=0.001:0.999,samples=200,thick,dotted,blue!60!black]{(1-x)*(ln(2.5^2/(2.25*x+0.09*(1-x)-x*(1-x)))-1+(0.3+x)^2/(2.25*x+0.09*(1-x)-x*(1-x)))};
\addlegendentry{$\mu=2.5$ GeV}
\draw[gray,thin] (axis cs:0,0) -- (axis cs:1,0);
\draw[gray,densely dotted] (axis cs:0.264,-0.6) -- (axis cs:0.264,0.6) node[above,font=\scriptsize,black] {$0.264$};
\draw[gray,densely dotted] (axis cs:0.567,-0.6) -- (axis cs:0.567,0.35) node[above,font=\scriptsize,black] {$0.567$};
\end{axis}
\end{tikzpicture}
\caption{<caption draft below>}\label{fig:front-yukawa-pdf}
\end{figure}
%%% END fig:front-yukawa-pdf
```
- The expression is $f/a_\lambda=(1-\xi)[\ln\frac{\mu^2}{\Delta}-1+\frac{(m_q+\xi m_p)^2}{\Delta}]$, $\Delta=\xi m_s^2+(1-\xi)m_q^2-\xi(1-\xi)m_p^2$ with $m_q=0.3$, $m_p=1.0$, $m_s=1.5$ GeV (VF-FRO-10; sign changes checked in `checks/vf_v2_checks.log`).
- **Caption draft:** 「Yukawa 模型中单圈 $\overline{\rm MS}$ “夸克在核子中”的分布（$m_q=0.3$、$m_p=1.0$、$m_s=1.5$ GeV）\cite{CollinsRogersSato2022}：$\mu=0.8$ GeV 时 $\xi>0.264$ 处为负，$\mu=1.2$ GeV 时 $\xi>0.567$ 处为负，$\mu=2.5$ GeV 时处处为正。“$\overline{\rm MS}$ 分布在所有标度上非负”因而不成立；足够大标度上的正定性只有部分论证（\cref{conj:pdf-positivity}）。」

Optional (Ch24):
- **`fig:front-sll`** · TikZ: the iterated one-loop anomalous dimension with Glauber phases ($i\pi$) and soft emissions building the super-leading tower; a plot inset of ${}_2F_2(1,1;2,\frac52;-w)$ vs $w$ falling like $\frac32\ln w/w$ (VF-FRO-7). Caption: 「超领头对数的来源：Glauber 相位与软发射不对易；对 $q\bar q$ 单态交换的求和给出 ${}_2F_2(1,1;2,\frac52;-w)$，在大 $w$ 处只有幂次式衰减。」
- **`fig:front-dps-double-counting`** · TikZ: DPS vs SPS overlap at small transverse separation $y$; the cut-off function $\Phi(y\nu)$ and the subtraction $\sigma_{\rm sub}$ (VF-FRO-13). Caption: 「双部分子散射与单部分子散射在小 $y$ 处的重复计数及其减除：$\sigma=\sigma_{\rm SPS}+\sigma_{\rm DPS}-\sigma_{\rm sub}$。」

### 4.5 App M

N18. **`fig:appM-forest`** · App M (`sec:appM-bphz`) · TikZ, two panels.
- **Draw:** (a) a two-loop graph (e.g. the handbag with a vertex correction on one current vertex and a self-energy on the struck quark): three subgraphs marked with `region` boxes — $\gamma_1$ (the vertex loop), $\gamma_2\supset\gamma_1$ (the larger box containing $\gamma_1$ and the quark line), $\gamma_3$ (the self-energy, disjoint from $\gamma_2$); a legend 「森林：两两嵌套或不相交」 and the formula $R_\Gamma=\sum_F\prod_{\gamma\in F}(-t^{\delta(\gamma)}_\gamma)I_\Gamma$. (b) the frozen-$q$ bilocal normal product: two current vertices $j(x/2)$, $j(-x/2)$ (`opvertex`) with the large momentum $q$ flowing through a dashed box (the subgraph containing both currents) labelled 「对外动量（不对 $q$）作 Taylor 减除，次数 $\delta$」; a note 「减除次数须对顶点可加」.
- **Caption draft:** 「BPHZ 森林公式与正规乘积（示意）：(a) 森林由两两嵌套或不相交的紫外发散子图组成；(b) 冻结 $q$ 的双局域正规乘积中，含两个流顶点的子图只对外动量作 Taylor 减除。减除次数必须对顶点可加，否则可构造反例（正文）。」

N19. **`fig:appM-euclid-forward`** · App M (`sec:appM-massless`) · TikZ, two panels.
- **Draw:** (a) a 2D projection of Euclidean momentum space: the external momenta $p_1,p_2$ (short arrows) and the large $q$ (long arrow, direction $\hat q$); the exceptional set (partial sums of external momenta $=0$) drawn as thin dashed lines through the origin that the configuration avoids; a circular arc 「方向上一致」 around $\hat q$; the bound 「$O(|q|^{D-1-a}\ln^k|q|)$」. (b) the forward partonic configuration: a handbag-like graph with incoming $p$ and outgoing $p$ (same momentum, $p^2=0$), the sum of the incoming momenta of the two external partons $p+(-p)=0$ highlighted in red 「例外动量」 and the label 「需\cref{asm:appM-forward}」.
- **Caption draft:** 「欧氏非例外动量与前向在壳运动学：(a) 微扰 OPE 的定理形式适用于欧氏、非例外的外动量，$|q|\to\infty$ 时余项在方向上一致；(b) DIS 所需的前向在壳部分子矩阵元（入射与出射动量同为 $p$，$p^2=0$）是例外构型，欧氏定理不直接适用，其余项估计是编号假设（$O(\alpha_s)$ 已精确到 $\varepsilon$ 地检验至 $N\le8$，VF-DIS-13）。」

### 4.6 App N

N20. **`fig:appN-triangle-regions`** · App N (`sec:appN-examples`) · TikZ.
- **Draw:** the real $(k^+,k^-)$ plane at $k_T=0$ for the off-shell one-loop triangle ($p_1\approx P n_A$, $p_2\approx P'n_B$): the collinear pinch lines $\pi_{C_1}$ (segment of the $k^+$ axis, $0<k^+<P$) and $\pi_{C_2}$ (segment of the $k^-$ axis, $0<k^-<P'$) as thick lines; tubes $N_{C_1}$, $N_{C_2}$ of half-width $\lambda^{1/3}$ around them (light blue/orange fills); a disc $N_S$ of radius $\lambda^{1/9}$ around the origin (light green); labels $U_S=N_S$, $U_{C_i}=N_{C_i}\setminus N_S$, $U_H$ (rest). In each region a small box with the grouped expression that supplies the small factor: $U_S$: $(1-T_S)\Gamma$; $U_{C_1}$: $(1-T_{C_1})(\Gamma-C_S\Gamma)$ and $C_{C_2}\Gamma$ (CS2); $U_H$: $(1-T_H)X_H$. A note at the origin: 「软近似只在穿过 ${\rm Re}\,k^-\sim k_T^2/(4k^+)$ 的围道上成立」.
- **Caption draft:** 「单圈离壳三角图的区域与邻域（$k_T=0$ 截面，示意）：$\pi_{C_1}$、$\pi_{C_2}$ 为两条共线钳夹线，$\pi_S=\{0\}$；$N_{C_i}$ 为宽 $\lambda^{1/3}$ 的管，$N_S$ 为半径 $\lambda^{1/9}$ 的球。每个支配集 $U_R$ 上标出提供小因子的分组表达式，即 (CS1)(CS2) 在本例中的具体形式（\cref{def:method-collins-conditions}）。」

N21. **`fig:appN-triangle-remainder`** · App N (`sec:appN-examples`, with `prop:appN-triangle-exact`) · pgfplots. **Tested starter code** (inline coordinates from `checks/fig_data.py`, log in `checks/fig_data.log`):
```latex
%%% BEGIN fig:appN-triangle-remainder
\begin{figure}[htbp]\centering
\begin{tikzpicture}
\begin{axis}[name=A,width=0.48\textwidth,height=5.6cm,xmode=log,xmin=1e-5,xmax=0.2,ymin=-9,ymax=-3.4,
  xlabel={$t=m^2/Q^2$},ylabel={$Q^2\!\int r\,/\,t$},tick label style={font=\scriptsize},label style={font=\small},title={\small (a)},
  legend style={font=\scriptsize,draw=none,fill=none,at={(0.03,0.03)},anchor=south west}]
\addplot[only marks,mark=*,mark size=1.2pt] coordinates {(1.0e-5,-3.99879) (1.77828e-5,-3.99808) (3.16228e-5,-3.99697) (5.62341e-5,-3.99527) (0.0001,-3.99268) (0.000177828,-3.98881) (0.000316228,-3.98313) (0.000562341,-3.97501) (0.001,-3.96377) (0.00177828,-3.94895) (0.00316228,-3.93081) (0.00562341,-3.91148) (0.01,-3.89725) (0.0177828,-3.90336) (0.0316228,-3.96534) (0.0562341,-4.17112) (0.1,-4.7898) (0.15,-6.06052) (0.2,-8.80249)};
\addlegendentry{精确}
\addplot[domain=1e-5:0.2,samples=80,thick,dashed,red!60!black]{-4+x*(ln(1/x)^2-15+pi^2/3)};
\addlegendentry{$-4+t(L^2-15+\frac{\pi^2}3)$}
\end{axis}
\begin{axis}[at={(A.east)},anchor=west,xshift=1.7cm,width=0.48\textwidth,height=5.6cm,xmode=log,xmin=1e-5,xmax=0.2,ymin=0,ymax=235,
  xlabel={$t=m^2/Q^2$},ylabel={NLP 系数},tick label style={font=\scriptsize},label style={font=\small},title={\small (b)},
  legend style={font=\scriptsize,draw=none,fill=none,at={(0.97,0.97)},anchor=north east}]
\addplot[only marks,mark=*,mark size=1.2pt] coordinates {(1.0e-5,221.629) (1.77828e-5,198.089) (3.16228e-5,175.876) (5.62341e-5,154.992) (0.0001,135.438) (0.000177828,117.216) (0.000316228,100.33) (0.000562341,84.7839) (0.001,70.5819) (0.00177828,57.7299) (0.00316228,46.2333) (0.00562341,36.0952) (0.01,27.313) (0.0177828,19.8734) (0.0316228,13.745) (0.0562341,8.87051) (0.1,5.16015) (0.15,3.17897) (0.2,2.05715)};
\addlegendentry{精确 $(Q^2I-L^2-\frac{\pi^2}3)/t$}
\addplot[domain=1e-5:0.2,samples=80,thick,dashed,blue!60!black]{2*ln(1/x)^2-4*ln(1/x)-4+2*pi^2/3};
\addlegendentry{$2L^2-4L-4+\frac{2\pi^2}3$}
\end{axis}
\end{tikzpicture}
\caption{<caption draft below>}\label{fig:appN-triangle-remainder}
\end{figure}
%%% END fig:appN-triangle-remainder
```
- **Caption draft:** 「单圈离壳三角图的 Collins 减除（$t=m^2/Q^2$，$L=\ln(1/t)$）：(a) 精确余项 $Q^2\int r/t$ 趋于 $-4$，修正为 $t(L^2-15+\frac{\pi^2}3)$——余项在次领头幂次没有对数；(b) 原积分 $Q^2I$ 的次领头系数按 $2L^2-4L-4+\frac{2\pi^2}3$ 增长，这些对数完全由用精确运动学（$\tilde Q^2\neq Q^2$）写出的减除项再现（\cref{prop:appN-triangle-exact}，VF-REF-2，VF-REF-3）。」

Optional (App N):
- **`fig:appN-chain-pairing`** · TikZ: the nine-region poset of `fig:method-hasse` with a chosen $R_0=(C_1,C_1)$ highlighted, the incomparable regions split into $\mathcal I'$ (pinch sets meeting $\pi_{R_0}$, blue) and $\mathcal I''$ (not meeting, grey), and the meets $R\wedge R_0$ marked; caption: 「配对分解（\cref{lem:method-pairing}）在九区域偏序集上的例子。」

### 4.7 App O

N22. **`fig:appO-deformation`** · App O (`sec:appO-deformation`) · TikZ, three panels.
- **Draw:** (a) complex $k^-$ plane: after the one-sided rewriting all $J_A$ poles (crosses) lie in the lower half-plane; the contour (blue) is lifted to ${\rm Im}\,k^-=+\kappa|k_T|$ over the window; (b) complex $k^+$ plane: the $J_B$ poles in the upper half-plane; contour pushed to ${\rm Im}\,k^+=-\kappa|k_T|$ (so that ${\rm Im}\,k\propto e_G$); (c) the real $(k^+,k^-)$ plane with the Glauber wedge $G_\delta$ shaded; the deformed contour's projection leaves $G_\delta$, with the inequality 「$|k^+k^-|\ge\kappa^2k_T^2$ 于形变后围道」 and the constants 「$\kappa^2<1/(2KN_C^2)$，$c=\min(\kappa^2,\delta/2)$」; a note 「实围道上程函近似以 $O(1)$ 失效，形变后误差受 Grammer–Yennie 比值控制」.
- **Caption draft:** 「分级构型的同时形变（单侧改写之后）：$J_A$ 的 $k^-$ 极点全在下半平面、$J_B$ 的 $k^+$ 极点全在上半平面，故可沿 $e_G=n_B-n_A$ 以幅度 $\kappa|k_T|$ 同时形变两个分量，使动量离开 Glauber 区并在形变后的围道上获得程函近似的定量误差界（\cref{prop:appO-target}，\cref{prop:appO-eikonal}）。」 *(v2.3: X1 applied — the statements cited in the caption are unchanged; the owner re-checks the caption against the final App O statements, rule 9.)*

Optional (App O):
- **`fig:appO-windows`** · TikZ: a light-cone-time axis with window cores (bold intervals) and the entire carrier $\phi(x)=2\sqrt\pi e^{-x^2}$ (bell curve) used to smooth the window edges; the SA/AS split of an insertion near the hard vertex. Caption: 「窗口与整函数载体 $\phi(x)=2\sqrt\pi e^{-x^2}$：单侧改写只在弱等价意义下成立（E-W）。」

### 4.8 Ch25 `summary` (optional)
- **`fig:summary-chapter-dag`** · TikZ: chapter-level DAG (nodes = units, edges = the existence of `\uses` edges between their statements, generated), with the critical path FINAL_OUTLINE → App N → App O → Ch12/Ch14/Ch18 → Ch22–Ch24 highlighted. Caption: 「各章与附录之间的依赖（由 `\uses` 数据汇总）。」

### 4.9 App P — template of the generated `fig:appP-dependency`

The generator (integrator) emits plain TikZ; no graphviz. Rules:
1. **One label family, eight generated figures (spec v2.2, merge decision MD12):** `fig:appP-dependency` (the skeleton: the master-table statements, all `asm:` entries and the R_cond theorems of App M/N/O) and the per-part graphs `fig:appP-dependency-b` (Part I), `-c` (Part II), `-d` (Part III), `-e` (Part IV), `-f` (Parts V–VI), `-g` (Part VII), `-h` (the App M–O statements used by chapter statements). Per-part node selection = the **main theorems** of the part (master-table statements and all `thm:` labels of the part) with their direct premises inside the part and all assumptions they use; premises outside the part are collapsed into one grey stub per unit; **at most 60 nodes** per figure (fold rule of FINAL_OUTLINE_v2 App P §P.7). All eight are required, owned by App P and generated by the integrator. Each fits one page (landscape allowed via `\rotatebox{90}` inside the float, no new packages).
2. **Layout:** layers left→right by unit order (front, Ch1, …, Ch25, App A, …, App Q); inside a layer, vertical order by the barycentre of the predecessors (two sweeps); node separation ≥ 0.25 cm; long edges drawn as straight lines with `opacity=0.5`.
3. **Node style by type:** `thm`/`prop`/`lem`/`cor`: rectangle, rounded corners 1pt; `def`: rectangle without fill, thin border; `conj`: ellipse; `asm`: rectangle, dashed `orange!65!black` border, fill `orange!8`; `[V]` statements: rectangle with double border. **Fill by tag** (as the tag macros): `OliveGreen!15` (R), `RoyalBlue!15` (A), `BurntOrange!15` (P), `Plum!15` (C), `BrickRed!15` (V); R_cond nodes have a dashed border; pure-math lemmas white. Node text: `\tiny` short label (without prefix) — the full label in `tab:appP-status`.
4. **Edges:** `uses` edges solid `gray!60`, arrow `-{Stealth[length=2pt]}` pointing from premise to statement; edges from `asm:` premises to R_cond statements dashed `orange!65!black`; edges into the bottleneck assumptions of [A] process theorems thick `red!60!black` (from the master table's 瓶颈 column).
5. **Legend** (a small `matrix` of nodes in a corner): the five tag fills, the R_cond dashed border, the assumption node, the three edge styles.
6. **Caption draft:** 「本书规范陈述的依赖图（由各环境中的 `\uses` 自动生成）：框的颜色为严格性标签，虚线框为 $R_{\rm cond}$ 条件定理，橙色虚线框为编号假设，粗红线为决定全阶论证地位的瓶颈依赖。」

---------------------------------------------------------------------------------------------------

## 5. Figures per unit (v2 summary)

| unit | existing (owned) | v1-new required | S56 required | v2-new required | optional | total required |
|---|---|---|---|---|---|---|
| Ch1 | parton-model, handbag, factorization-schematic | intro-dependency | — | — | — | 4 |
| Ch2 | — | prelim-feynman-rules | — | qcd-vacuum-polarization, qcd-running-coupling, qcd-antiscreening, qcd-ir-safety | qcd-gauge-orbit, qcd-colour-flow | 5 |
| Ch3 | soft-eikonal | prelim-wilson-rules, prelim-lightcone | — | — | — | 3 |
| Ch4 | landau-pinch, vertex-regions, coleman-norton, reduced-ee, reduced-dis, reduced-dy, momentum-regions | — | ir-mode-exponents | — | ir-landau-simplex | 8 |
| Ch5 | sudakov-ff | sudakov-hjjs, sudakov-cusp, sudakov-dipole | — | — | — | 4 |
| Ch6 | ee-oneloop | ee-pi-plane | ee-cutsum-disc | — | — | 3 |
| Ch7 | dis-kinematics, forward-compton, omega-plane, ope-schematic, dis-oneloop, higher-twist | — | dis-euclid-segment | — | dis-twist-graphical | 7 |
| Ch8 | pdf-operator, pdf-oneloop, dglap-ladder, splitting-vertices | — | — | — | pdf-gluon-operator, pdf-ff-cut | 4 |
| Ch9 | ward-identity, glauber-contour | method-flowchart, method-kg, method-nesting | method-hasse, method-neighbourhoods, method-sudakov-plane, method-coeff-minus-coll, method-glauber-direction | — | — | 10 |
| Ch10 | — | disall-seed, disall-heavy | disall-ladder-regions | — | — | 3 |
| Ch11 | — | coll-sia, coll-sidis, coll-photoproduction | — | — | coll-transversity | 3 |
| Ch12 | dy-oneloop, glauber-exchange | dy-abelian-model | dy-pole-orientation, dy-two-gluon-exchange | — | — | 5 |
| Ch13 | — | thr-kinematics, thr-mellin | — | — | — | 2 |
| Ch14 | tmd-staple, tmd-soft-factor, tmd-dy, sidis-dy-links | — | — | — | tmd-evolution, tmd-rapidity-bars | 4 |
| Ch15 | scet-wilson, dijet-factorization | — | — | — | scet-modes | 2 |
| Ch16 | — | jets-sw-cone, jets-ngl, jets-gap | — | — | — | 3 |
| Ch17 | bfkl-ladder | smallx-dipole, smallx-map | — | — | — | 3 |
| Ch18 | violation-cq, diffraction, dps | — | — | — | break-spacelike, break-measurement | 3 |
| Ch19 | pion-ff, dvcs-handbag, meson-production | — | — | — | excl-erbl, excl-endpoint | 3 |
| Ch20 | nrqcd | heavy-bdpi, heavy-qcdf | — | — | — | 3 |
| Ch21 | renormalon-chain, twist3-ssa | power-borel-plane | — | — | — | 3 |
| Ch22 | quasi-pdf | lattice-matching | — | lamet-ioffe, lamet-oneloop, lamet-hybrid, lamet-lattice-geometries | lamet-fourier, lamet-validity, lamet-dependency | 6 |
| Ch23 | — | — | — | yzliu-soft-hqet, yzliu-leading-region, yzliu-theta-strip, yzliu-complex-lorentz, yzliu-threshold | yzliu-borel, yzliu-single-line | 5 |
| Ch24 | — | — | — | front-gordan, front-regions-polytope, front-endpoint, front-yukawa-pdf | front-sll, front-dps-double-counting | 4 |
| Ch25 | — | summary-status-map, summary-hypotheses | — | — | summary-chapter-dag | 2 |
| App A–L | — | — | — | — | appE-boost (App E may adapt `fig:pc-*`) | 0 |
| App M | — | — | appM-dependency, appM-handbag-ab | appM-forest, appM-euclid-forward | — | 4 |
| App N | — | — | — | appN-triangle-regions, appN-triangle-remainder | appN-chain-pairing | 2 |
| App O | — | — | appO-flowchart, appO-lcopt-term, appO-cutsum | appO-deformation | appO-glauber-flow, appO-windows | 4 |
| App P | — | — | appP-dependency (generated) | appP-dependency-b, appP-dependency-c, appP-dependency-d, appP-dependency-e, appP-dependency-f, appP-dependency-g, appP-dependency-h (generated) | — | 8 |
| App Q | — | — | — | — | — | 0 |
| **total** | **44** | **30** | **17** | **29** | **26** | **120** |

(v2.1: checked by `spec_v2/checks/figures_check.py`: 138 distinct labels (113 required + 25 optional). v2.2: 146 distinct labels (120 required incl. the 7 generated per-part App P graphs + 26 optional incl. `fig:lamet-dependency`), checked against the registry of FINAL_OUTLINE_v2 by `checks/check_final_outline_v2.py` (E11), each with exactly one owner; all 44 existing labels present in the source files; every chapter owns ≥ 2 required figures; App M, N, O, P own ≥ 1.)

---------------------------------------------------------------------------------------------------

## CHANGELOG

**2026-10-10 — v2 drafted (spec-v2 writer-spec/figures/bibliography drafter).**
1. All 44 existing figures re-assigned to v2 owners by first use (§1); owner changes: `fig:soft-eikonal` → Ch3, `fig:quasi-pdf` → Ch22; all other owners keep their key (chapter number +1). tikz2/tikz3 declared final (rule 3).
2. v1 new figures carried over with v2 owners (§2); `fig:prelim-lightcone` promoted to required (refdoc S56); `fig:intro-dependency`, `fig:method-flowchart`, `fig:summary-status-map`, `fig:summary-hypotheses` updated for the assumption register, App M/N/O and the frontier chapters.
3. The 22 figures of refdoc S56 added with full drawing descriptions (§3; 17 required, 5 optional), owners by first use in v2.
4. 33 new figures specified for Ch2, Ch22–Ch24, App M/N/O, Ch25 and the App P template (§4; 22 required, 11 optional); three pgfplots figures given as tested starter code (compiled with the preamble, renders inspected; numbers from `checks/vf_v2_checks.py` and `checks/fig_data.py`).
5. Counts and per-unit table (§5): 113 required, 25 optional; every chapter ≥ 2, every big appendix ≥ 1.

**2026-10-10 (later) — spec v2.1 (resumed writer-spec/figures/bibliography drafter).**
1. Planning markers removed from two caption drafts (`fig:dy-two-gluon-exchange`, `fig:appO-deformation`); the pending items are noted outside the caption text.
2. New rule 9 (§0): captions never carry planning markers, novelty claims or erratum statements; table of the figures whose captions touch claims of `verify/CLAIMS.md` (N01, N02, N05, N06, N10, N12, N21, E01, E02, E13, E28, E35, A03, A04, A08, A26) or the proof extensions X1–X3, with what the owner re-checks after the verify patch.
3. Optional `fig:excl-endpoint` may be drawn from the new VF-EXC-14 (Isgur–Llewellyn Smith soft fractions). Counts unchanged (113 required, 25 optional).

**2026-10-10 (merge) — spec v2.2 (spec-v2 integrator; FINAL_OUTLINE_v2).**
1. App P: the per-part dependency graphs `fig:appP-dependency-b` … `-h` are registered as required, generated figures owned by App P; §4.9 rule 1 now follows the App P generator specification (main theorems per part, at most 60 nodes; merge decision MD12) instead of "all statements of the part".
2. Ch22: the optional `fig:lamet-dependency` proposed by the frontier outline is adopted (§4.2).
3. Section assignments of N1–N17 confirmed against the registry of FINAL_OUTLINE_v2 ("proposed" dropped); N5 belongs to `sec:lattice-quasi` (the label `sec:lamet-objects` is not used).
4. Counts: 120 required, 26 optional (§0 table, §5). Every chapter still owns ≥ 2 required figures, every big appendix ≥ 1. No caption draft was changed.

**2026-10-11 — v2.3 (spec patcher; verify patch).**
1. Rule 9 final: the table now gives the outcome of every claim and slot (N01, N02, N05, N06, N09, N10, N12, N21, E01, E02, E13, E28, E35, A03, A04, A08, A26; X1–X3); `fig:break-measurement`, `fig:appM-handbag-ab` and the optional App O figures added to the re-check list.
2. S12 `fig:appM-dependency`: nodes `asm:appM-oswi`, `lem:appM-ne`, `thm:appM-brst-reduction`, `thm:appM-forward-expansion`, `cor:appM-forward-ope`, `thm:appM-scaling`; S14 `fig:appO-flowchart`: model-theorem box with side boxes (not premises of `thm:appO-main`); the pending notes of two caption drafts replaced by outcomes. No caption text and no count changed.
3. Generated figures to regenerate from the v2.3 outline (changed `\uses` data, register and master rows): `fig:intro-dependency`, `fig:summary-status-map`, `fig:summary-hypotheses`, `fig:appP-dependency` and `fig:appP-dependency-b` … `-h`, `fig:appM-dependency`, `fig:appO-flowchart`, optional `fig:lamet-dependency`.

