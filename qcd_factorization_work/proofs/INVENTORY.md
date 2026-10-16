# Proof-completion inventory (generated from FINAL_OUTLINE_v2 by writing/tools/proof_inventory.py)


## front — Front matter — `front.tex` (6 pp; written by the Ch1 writer)


## Ch01 — Chapter 1 — 引言：部分子图像、因子化的含义与严格性分级 / Introduction: the parton picture, what factorization asserts, and levels of rigour

- [C] `asm:intro-wightman` (假设, tag C) — QCD 的 Wightman 结构
- [C] `asm:intro-composite` (假设, tag C) — 规范不变复合算符与光线算符的存在与重整化群
- [C] `asm:intro-np-ope` (假设, tag C) — 非微扰算符乘积展开
- [C] `asm:intro-af-coeff` (假设, tag C) — 系数的渐近自由行为
- [C] `asm:intro-growth` (假设, tag C) — 前向振幅的增长条件
- [C] `asm:intro-bridge` (假设, tag C) — 从部分子微扰论到强子的桥接假设

## Ch02 — Chapter 2 — QCD 基础——从规范不变性到渐近自由 / QCD basics: from gauge invariance to asymptotic freedom

Box:
- 本章给出完整推导的：`thm:qcd-gauge-invariance`（[R, R_def]）；`prop:qcd-covariance`（[R, R_def]）；`lem:prelim-brst-nilpotent`（[R, R_def]，细节见附录 J）；`prop:qcd-brst-cohomology`（[R, R_def]）；`prop:qcd-superficial-degree`（[R, R_def]）；单圈 $Z$ 因子与 $\beta_0$（`ex:qcd-gluon-self-energy`、`ex:qcd-quark-self-energy-vertex`、`ex:qcd-beta0-four-ways`，`prop:prelim-beta` 的 $\beta_0$ 部分 [R, R_PT]）；`prop:qcd-rge`（[R, R_PT]，以可重整性为前提的完整推导）；`prop:prelim-rg`（[R, R_PT]）；`thm:qcd-asymptotic-freedom`（[R, R_PT]）；`prop:qcd-soft-collinear-limits`（[R, R_PT]，树图）。
- 本章只陈述、留待后文或文献的：`thm:qcd-renormalizability`、`lem:qcd-st-regularized`、`prop:qcd-st-relations`（全阶部分）、`thm:prelim-slavnov-taylor`、`prop:qcd-xi-independence`、`thm:prelim-composite-renorm`（[R, R_PT]，证明概要 + 完整证明的文献）；$\beta_1,\beta_2$（文献值）；红外定理（第~4~章：`thm:ir-bn-qed`、`thm:ir-kln`、`prop:ir-bn-failure`、`thm:ir-safe-finite`）；QCD 的非微扰存在性（`asm:intro-wightman`，[C]）；Gribov 复本、禁闭（不在本书范围）。

- [R-sketch] `thm:qcd-gauge-invariance` (定理, tag R, R_def) — 经典 QCD 拉氏量的规范不变性与唯一性
- [R-sketch] `lem:qcd-st-regularized` (引理, tag R, R_PT) — 维数正规化理论的 Slavnov–Taylor 恒等式
- [R-sketch] `thm:qcd-renormalizability` (定理, tag R, R_PT) — QCD 的可重整性
- [R-sketch] `prop:qcd-st-relations` (命题, tag R, R_PT) — 重整化常数间的 Slavnov–Taylor 关系
- [R-sketch] `thm:prelim-slavnov-taylor` (定理, tag R, R_PT) — Slavnov–Taylor 恒等式（因子化所用形式）
- [R-sketch] `prop:qcd-xi-independence` (命题, tag R, R_PT) — 物理量的规范参数无关性
- [R-sketch] `thm:prelim-composite-renorm` (定理, tag R, R_PT) — 规范不变复合算符的重整化（Joglekar–Lee）

## Ch03 — Chapter 3 — 因子化的数学与场论工具 / Mathematical and field-theoretic tools of factorization

Box:
- 证明了：`lem:prelim-boost`（[R, R_def]）；`prop:prelim-wilson-covariance`、`prop:prelim-wilson-rules`（[R, R_def]，证明见附录 B）；`lem:prelim-eikonal-identity`、`lem:prelim-scaleless`、`lem:prelim-plus-expansion`、`lem:prelim-mellin`（数学）；`thm:prelim-cutting-rules`（[R, R_PT]，有质量或已正规化的图）；`prop:prelim-unitarity`（[R, R_PT]）；`prop:prelim-optical`（[R, R_def]，强子态需 `asm:intro-wightman`）。
- 给出全阶论证：`rem:prelim-cutting-dr`（[A]：无质量维数正规化中含鬼场的割图规则）。
- 没有证明：带插入的光锥割线位置恒等式与闭时路幺正性（附录 O，`lem:appO-cut-position`、`lem:appO-unitarity`）；单个割图不满足幺正性（只有对割线求和才行）。

- [R-sketch] `thm:prelim-cutting-rules` (定理, tag R, R_PT) — 切割规则
- [R-sketch] `prop:prelim-unitarity` (命题, tag R, R_PT) — 物理幺正性与鬼场割线
- [A] `rem:prelim-cutting-dr` (注, tag A) — 无质量维数正规化中的割图规则

## Ch04 — Chapter 4 — 费曼积分的红外结构：钳夹、幂次计数与红外安全 / Infrared structure of Feynman integrals: pinches, power counting, IR safety

Box:
- 证明了：`thm:ir-landau-alpha`、`thm:ir-landau-momentum`（[R, R_PT]，必要性；附录 D）；`prop:ir-coleman-norton`（[R, R_PT]，代数形式）；`prop:ir-power-counting`（[R, R_PT]，超表观度，E-S；附录 E）；`prop:ir-glauber-trapping`（[R, R_PT]，单圈）；`thm:ir-bn-qed`（[R, R_PT]）；`thm:ir-regions-euclid`（[R, R_PT]）。
- 给出全阶论证：`prop:ir-pinch-classification`、`prop:ir-super-leading`、`thm:ir-leading-regions`、`thm:ir-kln`、`thm:ir-safe-finite`（[A]；瓶颈：嵌套区域与积分形式的幂次计数 `asm:appN-envelope`、`asm:appN-separation`）。
- 没有证明：Landau 条件的充分性与整体围道形变（`rem:ir-landau-status`；第~24~章的预印本结果）；闵氏区域方法（`prop:ir-regions-minkowski`，[P]；“区域 = Newton 多面体下表面”在三圈有反例）；非阿贝尔 Bloch–Nordsieck 抵消（`prop:ir-bn-failure`，[V]）。

- [A] `rem:ir-landau-status` (注, tag A) — Landau 条件的充分性与整体形变
- [A] `prop:ir-pinch-classification` (命题, tag A) — 钳夹面与约化图
- [A] `prop:ir-super-leading` (命题, tag A) — 超领头构型及其相消
- [A] `thm:ir-leading-regions` (定理, tag A) — 领头区域
- [R-sketch] `thm:ir-bn-qed` (定理, tag R, R_PT) — QED 中的 Bloch–Nordsieck 定理
- [A] `thm:ir-kln` (定理, tag A) — KLN 定理
- [V] `prop:ir-bn-failure` (命题, tag V) — 有色初态时非阿贝尔 Bloch–Nordsieck 抵消的失效
- [A] `thm:ir-safe-finite` (定理, tag A) — 红外安全可观测量的有限性
- [P] `prop:ir-regions-minkowski` (命题, tag P) — Minkowski 极限下区域方法的地位

## Ch05 — Chapter 5 — Sudakov 形状因子与振幅的红外结构 / The Sudakov form factor and the infrared structure of amplitudes

Box:
- 证明了：`prop:sudakov-oneloop`（[R, R_PT]，精确到 $\varepsilon$ 的所有阶）；`prop:sudakov-coulomb`（[R, R_PT]，单圈）；`prop:sudakov-kg` 与 `prop:sudakov-webs` 的单圈/$O(g^2)$ 内容（[R]）。
- 给出全阶论证：`thm:sudakov-factorization`（[A]；减除在 Collins 2011 第 10 章中对此例完整）、`prop:sudakov-kg`、`cor:sudakov-exponentiation`、`prop:sudakov-webs`、`thm:sudakov-ir-poles`、`prop:sudakov-amplitude-factorization`（[A]）。
- 没有证明：偶极子公式作为全阶公式（`prop:sudakov-dipole-violation`，[V]）；类空严格共线因子化（`rem:sudakov-spacelike`，[V]，见第~18~章）。

- [A] `thm:sudakov-factorization` (定理, tag A) — Sudakov 形状因子的全阶因子化
- [A] `prop:sudakov-kg` (命题, tag A) — $K+G$ 演化方程
- [A] `cor:sudakov-exponentiation` (推论, tag A) — 指数化与解析延拓
- [A] `prop:sudakov-webs` (命题, tag A) — 非阿贝尔指数化（webs）
- [A] `thm:sudakov-ir-poles` (定理, tag A) — 无质量多腿振幅红外极点的因子化
- [V] `prop:sudakov-dipole-violation` (命题, tag V) — 偶极子公式作为全阶精确公式的失效
- [A] `prop:sudakov-amplitude-factorization` (命题, tag A) — 振幅的硬—软—共线因子化（出射或阈值运动学）
- [V] `rem:sudakov-spacelike` (注, tag V) — 类空共线极限预览

## Ch06 — Chapter 6 — 严格核心 I：$e^+e^-$ 湮灭总截面 / Rigorous core I: the $e^+e^-$ total cross section

Box:
- 证明了：`thm:ee-R-finite`、`thm:ee-euclid-ir`、`lem:ee-single-scale`、`prop:ee-adler-rg`、`prop:ee-oneloop`、`prop:ee-twoloop`、`prop:ee-cutting-exact`、`cor:ee-R-alphas`（[R, R_PT]）；`prop:ee-R-ImPi`、`prop:ee-analytic`、`prop:ee-adler-dispersion`、`prop:ee-contour`、`prop:ee-smearing`（[R, R_def]；强子态需 `asm:intro-wightman`）。
- 给出全阶论证：`cor:ee-cuts`（[A]：无质量维数正规化割图规则）；`thm:ee-ope`（[A]：含夸克 QCD 的 OPE）。
- 没有证明：非微扰 OPE 与凝聚（`conj:ee-np-ope`，[C]；`asm:intro-np-ope`）；夸克—强子对偶（`conj:ee-duality`，[C]）；在复 $q^2$ 处使用 OPE（`rem:ee-complex-ope`）。

- [R-sketch] `thm:ee-euclid-ir` (定理, tag R, R_PT) — 欧氏红外有限性
- [R-sketch] `prop:ee-twoloop` (命题, tag R, R_PT) — 欧氏两圈关联函数
- [A] `cor:ee-cuts` (推论, tag A) — 与部分子末态求和的等同；KLN
- [A] `thm:ee-ope` (定理, tag A) — 流关联函数的欧氏 OPE
- [C] `conj:ee-np-ope` (猜想, tag C) — 非微扰 OPE 与凝聚
- [C] `conj:ee-duality` (猜想, tag C) — 夸克—强子对偶

## Ch07 — Chapter 7 — 严格核心 II：深度非弹散射与算符乘积展开 / Rigorous core II: DIS and the operator product expansion

Box:
- 证明了：`prop:dis-W-structure`、`lem:dis-euclid-segment`、`lem:dis-twist-classification`、`lem:dis-twist-chirality`、`prop:dis-low-moments`（[R, R_def]）；`prop:dis-compton-analytic`、`prop:dis-dispersion`、`lem:dis-tree-ope`、`prop:dis-chiral-suppression`、`prop:dis-c-oneloop`（[R, R_PT]）；`thm:dis-moments`、`prop:dis-wilson-partons`、`prop:dis-ope-rg`、`cor:dis-scaling`、`prop:dis-twist4`、`prop:dis-tmc`、`thm:dis-bjorken`（[R, R_OPE]）；`prop:dis-dispersion-np`（[R, R_cond]，前提 `asm:intro-wightman`）、`lem:dis-ope-segment`（前提 `asm:intro-np-ope`）、`thm:dis-fixed-n`、`thm:dis-moments-np`、`cor:dis-weak-xspace`（[R, R_cond]，前提 `asm:intro-*`）。
- 给出全阶论证：`thm:dis-ope` 及其三个子陈述 `prop:dis-ope-euclid`、`prop:dis-ope-gi`、`prop:dis-ope-forward`（[A]；瓶颈 `asm:appM-brst-ope`、`asm:appM-forward`）；`prop:dis-light-cone`（[A]）。
- 没有证明：含夸克 QCD 的 OPE 的严格证明；非微扰 OPE（`asm:intro-np-ope`）；低阶矩（含动量求和规则）所需的增长条件（`asm:intro-growth`）；$x$ 空间逐点的 $O(1/Q^2)$（`rem:dis-nonuniform`）。

- [A] `prop:dis-ope-euclid` (命题, tag A) — 欧氏非例外动量下 Green 函数的逐图渐近展开
- [A] `prop:dis-ope-gi` (命题, tag A) — 物理矩阵元只需规范不变算符
- [A] `prop:dis-ope-forward` (命题, tag A) — 前向在壳部分子矩阵元
- [A] `thm:dis-ope` (定理, tag A) — 重整化微扰论中的欧氏 OPE
- [A] `prop:dis-light-cone` (命题, tag A) — 光锥展开
- [R-sketch] `prop:dis-twist4` (命题, tag R, R_OPE) — 扭度 4 修正的算符结构
- [R-sketch] `prop:dis-tmc` (命题, tag R, R_OPE) — 靶质量修正

## Ch08 — Chapter 8 — 严格核心 III：部分子分布与碎裂函数的算符定义 / Rigorous core III: operator definitions of PDFs and FFs

Box:
- 证明了：`prop:pdf-invariance`、`lem:pdf-wilson-moments`（[R, R_def]）；`thm:pdf-support-pt`、`thm:pdf-moments-local`、`thm:pdf-dglap`、`prop:pdf-lo-kernels`、`prop:pdf-pqq-operator`、`prop:pdf-partonic-dr`、`prop:pdf-local-anomalous`、`prop:pdf-sum-rules`（[R, R_PT]；强子版本需 `asm:intro-composite`）；`thm:pdf-dis-xspace`（[R, R_OPE]）；`prop:pdf-timelike-dglap` 的单圈内容（[R, R_PT]）。
- 给出全阶论证：`prop:pdf-support-hadron`（[A]）；`prop:pdf-timelike-dglap`（[A]：碎裂函数的乘法可重整性是独立输入，`asm:appN-multren`(Z1)）。
- 没有证明：$\overline{\rm MS}$ PDF 在某一非微扰标度以上的正定性（`conj:pdf-positivity`，[C]；在所有标度上非负是错的）；数密度诠释（启发式，`rem:pdf-number-density`）；非定域算符的 BRST 分类（第~24~章讨论其矩约化）。

- [R-sketch] `thm:pdf-support-pt` (定理, tag R, R_PT) — 支撑（微扰论）
- [A] `prop:pdf-support-hadron` (命题, tag A) — 支撑（强子态）
- [C] `conj:pdf-positivity` (猜想, tag C) — $\overline{\rm MS}$ PDF 的正定性
- [A] `prop:pdf-timelike-dglap` (命题, tag A) — 类时 DGLAP 演化

## Ch09 — Chapter 9 — 全阶因子化证明的一般方法 / The general method of all-order factorization proofs

Box:
- 证明了：`lem:method-ward-elementary`、`lem:method-ward-abelian`、`prop:method-ward-one`、`prop:method-ward-tree`、`lem:method-i0-compat`、`prop:method-glauber-oneloop`、`ex:method-naive-induction`（[R, R_PT]）；`lem:method-soft-unitarity`（[R, R_def]）；`prop:method-scale-scheme`（[R, R_PT]）；数学引理 `lem:method-meets`、`lem:method-covering`、`lem:method-telescoping`、`lem:method-gy`、`prop:method-chains`、`lem:method-pairing`、`prop:method-product`、`lem:method-no-pole`；条件定理 `lem:method-local-accuracy`（前提 `asm:appN-envelope`、`asm:appN-separation`）、`cor:method-removing-eps`（前提 `asm:appN-contour`）、`thm:appN-subtraction`（附录 N）。
- 给出全阶论证：`lem:method-collinear-accuracy`、`lem:method-soft-accuracy`、`prop:method-gy-suppression`、`lem:method-ward-multi`（瓶颈 `asm:appN-ward-product`）、`prop:method-collinear-wilson`、`prop:method-soft-wilson`、`thm:method-subtraction`（瓶颈 `asm:appN-collins`）、`prop:method-fsi`（`asm:appN-cutsum`、`asm:appO-lcopt`）、`prop:method-glauber-deformation`（`asm:appO-deformation`）、`thm:method-template`（[A]）。
- 没有证明：积分范数意义下的全阶幂次计数（`asm:appN-envelope`、`asm:appN-separation`）；含鬼场的非阿贝尔多胶子 Ward 恒等式与非定域算符的 BRST 分类；Glauber 区的一般情形（`asm:appO-*`）；单个链项的可积性（一般不成立，`ex:method-naive-induction`）。

- [A] `lem:method-collinear-accuracy` (引理, tag A) — 共线近似的精度
- [A] `lem:method-soft-accuracy` (引理, tag A) — 软近似的精度
- [A] `prop:method-gy-suppression` (命题, tag A) — G 部分的幂次压低
- [A] `lem:method-ward-multi` (引理, tag A) — 多个 K 胶子的 Ward 恒等式与 Wilson 线
- [A] `prop:method-collinear-wilson` (命题, tag A) — 共线 Wilson 线与 PDF
- [A] `prop:method-soft-wilson` (命题, tag A) — 软 Wilson 线
- [A] `thm:method-subtraction` (定理, tag A) — 减除定理
- [A] `prop:method-fsi` (命题, tag A) — 末态相互作用的幺正性相消
- [A] `prop:method-glauber-deformation` (命题, tag A) — Glauber 区的围道变形判据
- [A] `thm:method-template` (定理, tag A) — 因子化模板定理

## Ch10 — Chapter 10 — DIS 的全阶动量空间证明、重夸克与核靶 / DIS to all orders in momentum space; heavy quarks; nuclear targets

Box:
- 证明了：`prop:disall-nlo`、`prop:disall-scale`、`prop:disall-dis-scheme`（[R, R_PT]）；`cor:disall-consistency`（[R, R_OPE]）；`prop:disall-two-routes`、`prop:disall-factorized-subtraction`、`thm:disall-renorm-compat`（[R, R_cond]；前提 `asm:appN-collins`、`asm:appN-cutsum`、`asm:appN-ward-product`、`asm:appN-uv`、`asm:appN-multren`）。
- 给出全阶论证：`thm:disall-factorization`（[A]；瓶颈 `asm:appN-collins`、`asm:appN-ward-product`、`asm:appN-cutsum`）、`prop:disall-regions`、`lem:disall-fsi`、`prop:disall-h2`、`prop:disall-h3h4`、`prop:disall-h5`、`thm:disall-heavy`、`prop:disall-nuclear`（[A]）。
- 没有证明：$x\to1$ 处的一致性（阈值区）；非定域算符的 BRST 分类（`lem:method-ward-multi`）；积分范数形式的减除估计（`asm:appN-collins`）。

- [A] `lem:disall-fsi` (引理, tag A) — 末态喷注的非钳夹性
- [A] `prop:disall-regions` (命题, tag A) — DIS 的领头区域
- [A] `prop:disall-h2` (命题, tag A) — (H2) 的验证
- [A] `prop:disall-h3h4` (命题, tag A) — (H3)(H4) 平凡成立
- [A] `prop:disall-h5` (命题, tag A) — (H5) 的验证
- [A] `thm:disall-factorization` (定理, tag A) — DIS 共线因子化（动量空间，$x$ 空间逐点）
- [A] `thm:disall-heavy` (定理, tag A) — 含重夸克质量的因子化（Collins 1998）
- [A] `prop:disall-nuclear` (命题, tag A) — 核靶上的 DIS

## Ch11 — Chapter 11 — 其他共线过程：单举湮灭、SIDIS、光生、极化与横度 / Other collinear processes: SIA, SIDIS, photoproduction, polarized processes, transversity

Box:
- 证明了：`lem:coll-final-poles`（[R, R_PT]）；`prop:coll-anomaly-scheme`、`prop:coll-soffer`（[R, R_PT]，后者为 LO 演化的保持性）；`prop:coll-transversity-evolution`（[R, R_def]）；`thm:coll-g1-moments`、`prop:coll-photon-sf`（[R, R_OPE]）。
- 给出全阶论证：`lem:coll-unobserved-jet`、`prop:coll-sia-regions`、`thm:coll-sia`（另需 FF 乘法可重整性 `asm:appN-multren`(Z1)）、`thm:coll-sidis`、`thm:coll-direct-photo`、`prop:coll-luxqed`（[A]）。
- 没有证明：分辨光生（`conj:coll-resolved-photo`，[C]）；Burkhardt–Cottingham（`conj:coll-bc`，[C]）；衍射光生的标准因子化（`prop:coll-diffractive-photo`，[V]，实验）；Ellis–Jaffe、Wandzura–Wilczek（[V]）。

- [A] `lem:coll-unobserved-jet` (引理, tag A) — 未观测喷注与软辐射的幺正性相消
- [A] `prop:coll-sia-regions` (命题, tag A) — SIA 的领头区域
- [A] `thm:coll-sia` (定理, tag A) — $e^+e^-\to hX$ 的因子化
- [A] `thm:coll-sidis` (定理, tag A) — 共线 SIDIS 的因子化
- [A] `thm:coll-direct-photo` (定理, tag A) — 直接光生与光子结构函数
- [C] `conj:coll-resolved-photo` (猜想, tag C) — 分辨光生
- [V] `prop:coll-diffractive-photo` (命题, tag V) — 衍射光生中的因子化破坏
- [A] `prop:coll-luxqed` (命题, tag A) — 质子的光子分布
- [V] `prop:coll-ellis-jaffe` (命题, tag V) — Ellis–Jaffe 求和规则作为预言
- [C] `conj:coll-bc` (猜想, tag C) — Burkhardt–Cottingham 求和规则
- [V] `prop:coll-ww` (命题, tag V) — Wandzura–Wilczek 关系的一般失效

## Ch12 — Chapter 12 — Drell–Yan 过程与强子—强子碰撞 / Drell–Yan and hadron–hadron collisions

Box:
- 证明了：`prop:dy-born`、`prop:dy-glauber-pinch`、`lem:dy-poles-orientation`、`prop:dy-eikonal-twogluon`、`prop:dy-nlo`、`prop:dy-scale`（[R, R_PT]）；`prop:dy-universality`、`ex:dy-future-vs-past`（[R, R_def]）；`thm:appO-main`、`prop:appN-dy`（[R, R_cond]，附录 O、N）；`prop:dy-abelian-model`（[P]：阿贝尔程函模型中的完整证明）。
- 给出全阶论证：`prop:dy-regions`、`lem:dy-fsi`、`prop:dy-deformation`、`lem:dy-soft`、`thm:dy-factorization`、`thm:dy-colour-singlet`、`thm:dy-polarized`、`thm:dy-higher-twist`（[A]；瓶颈 `asm:appO-mixing`(c)、`asm:appO-deformation`(b)–(d)、`asm:appO-rewritten-cs`）。
- 没有证明：非程函（复合、相互作用）旁观者与活动部分子的 Glauber–软–共线混合（`asm:appO-mixing`(c)）；有色末态（`conj:dy-coloured-final`，[C]）；$1/Q^2$ 以外的幂次（`prop:dy-twist6-failure`，[V]）。

- [A] `prop:dy-regions` (命题, tag A) — DY 的领头区域
- [A] `lem:dy-fsi` (引理, tag A) — 旁观者末态相互作用的幺正性相消
- [A] `prop:dy-deformation` (命题, tag A) — 移除末态极点后的围道变形
- [A] `lem:dy-soft` (引理, tag A) — 软因子为 1
- [P] `prop:dy-abelian-model` (命题, tag P) — 阿贝尔模型中旁观者 Glauber 相位的相消
- [A] `thm:dy-factorization` (定理, tag A) — 单举 DY 的共线因子化
- [A] `thm:dy-colour-singlet` (定理, tag A) — 色单态末态
- [A] `thm:dy-polarized` (定理, tag A) — 极化 Drell–Yan
- [C] `conj:dy-coloured-final` (猜想, tag C) — 强子对撞中有色末态的共线因子化
- [C] `conj:dy-polarized-jets` (猜想, tag C) — 极化强子对撞中的 $A_{LL}$（喷注、$\pi^0$）
- [A] `thm:dy-higher-twist` (定理, tag A) — $1/Q^2$ 处的广义因子化
- [V] `prop:dy-twist6-failure` (命题, tag V) — 更高幂次的因子化失效

## Ch13 — Chapter 13 — 阈值重求和与重新因子化 / Threshold resummation and refactorization

Box:
- 证明了：`prop:thr-oneloop`（[R, R_PT]，单圈检验）。
- 给出全阶论证：`thm:thr-refactorization`、`prop:thr-dis`（[A]）。
- 没有证明：次领头幂次的一般阈值因子化（`prop:thr-nlp`，[P]）；Landau 极点处方（处方不是定理，`rem:thr-prescriptions`）。

- [A] `thm:thr-refactorization` (定理, tag A) — DY 阈值重新因子化与指数化
- [A] `prop:thr-dis` (命题, tag A) — DIS 的大 $x$ 重新因子化
- [P] `prop:thr-nlp` (命题, tag P) — 次领头幂次的阈值对数

## Ch14 — Chapter 14 — 横动量依赖（TMD）因子化 / TMD factorization

Box:
- 证明了：`lem:tmd-soft-oneloop`、`prop:tmd-evolution-oneloop`（[R, R_PT]，单圈）；`lem:tmd-sqrt-identity`、`thm:tmd-sivers-sign`（[R, R_def]）；`prop:tmd-zero-bin-soft`（[R, R_cond]，前提 `asm:appN-ward-product`、`asm:appN-tmd`；(a) 单圈无条件）。
- 给出全阶论证：`prop:tmd-regions`、`lem:tmd-glauber`、`prop:tmd-h1h5`、`thm:tmd-factorization`、`prop:tmd-evolution`、`prop:tmd-css`、`prop:tmd-small-b`、`cor:tmd-sivers-observable`、`prop:tmd-collins-universality`（[A]；瓶颈 `asm:appN-tmd`、`asm:appO-rewritten-cs`、`asm:appO-mixing`）。
- 没有证明：快度方案的全阶等价（只逐阶验证）；大 $b_T$ 区（非微扰）；$W+Y$ 在 $q_T\sim Q$ 与 $q_T\sim\Lambda$ 处的一致性（需修正的截断）；与扭度 3 的全阶匹配（`prop:tmd-twist3-matching`，[P]）。

- [A] `prop:tmd-regions` (命题, tag A) — 小 $q_T$ 的领头区域
- [A] `lem:tmd-glauber` (引理, tag A) — TMD DY、SIDIS、$e^+e^-$ 中的 Glauber 相消
- [A] `prop:tmd-h1h5` (命题, tag A) — 小 $q_T$ DY 对模板假设的验证
- [A] `thm:tmd-factorization` (定理, tag A) — Drell–Yan 的 TMD 因子化
- [A] `prop:tmd-evolution` (命题, tag A) — Collins–Soper 方程与重整化群方程
- [A] `prop:tmd-small-b` (命题, tag A) — 小 $b$ 展开
- [A] `prop:tmd-css` (命题, tag A) — CSS 解与非微扰输入
- [A] `cor:tmd-sivers-observable` (推论, tag A) — 可观测不对称的符号反转
- [A] `prop:tmd-collins-universality` (命题, tag A) — T-奇碎裂函数的普适性
- [P] `prop:tmd-twist3-matching` (命题, tag P) — 与扭度 3 共线因子化的匹配

## Ch15 — Chapter 15 — 有效场论方法：SCET / Effective-field-theory methods: soft-collinear effective theory

Box:
- 证明了：`prop:scet-scalings`、`prop:scet-gauge`、`thm:scet-decoupling`（[R, R_def]，作为 LO SCET 拉氏量的恒等式）；`prop:scet-lagrangian`、`prop:scet-wilson`、`prop:scet-scet2`、`prop:scet-hard-matching`、`prop:scet-thrust-oneloop`（[R, R_PT]）。
- 给出全阶论证：`prop:scet-rapidity-rg`、`prop:scet-glauber-operators`、`thm:scet-thrust`、`prop:scet-ll`（[A]；作为 QCD 陈述继承模式完备性 `asm:intro-bridge`、`asm:appN-envelope`）。
- 没有证明：模式完备性本身（即第~4~章的区域分析）；强子对撞中的 Glauber 相消（RS：远不是因子化的证明）；宣布的完整 SCET DY 证明（截至 2026 年 10 月未发表）。

- [A] `prop:scet-rapidity-rg` (命题, tag A) — 快度发散的处理与等价性
- [A] `prop:scet-glauber-operators` (命题, tag A) — Glauber 算符
- [A] `thm:scet-thrust` (定理, tag A) — 推力分布的因子化
- [A] `prop:scet-ll` (命题, tag A) — 领头对数指数

## Ch16 — Chapter 16 — 喷注、事件形状、非全局对数与超领头对数 / Jets, event shapes, non-global and super-leading logarithms

Box:
- 证明了：`prop:jets-sw`、`prop:jets-thrust-lo`、`prop:jets-ngl`（[R, R_PT]，固定阶）。
- 给出全阶论证：`cor:jets-ir-finite`、`thm:jets-bms`（LL，大 $N_c$）、`thm:jets-ngl-factorization`（[A]）。
- 没有证明：强子化修正的普适性（`conj:jets-hadronization`，[C]）；超出 LL 与有限 $N_c$ 的 NGL（`prop:jets-ngl-beyond`，[P]）；超领头对数的全阶结构与间隙截面的 PDF 因子化（`prop:jets-sll`，[P]；PDF 因子化 [C]）。

- [A] `cor:jets-ir-finite` (推论, tag A) — 红外安全喷注截面的有限性
- [C] `conj:jets-hadronization` (猜想, tag C) — 强子化修正的普适性
- [R-sketch] `prop:jets-ngl` (命题, tag R, R_PT) — 非全局对数的存在
- [A] `thm:jets-bms` (定理, tag A) — BMS 方程
- [P] `prop:jets-ngl-beyond` (命题, tag P) — 超出领头对数与有限 $N_c$
- [A] `thm:jets-ngl-factorization` (定理, tag A) — 喷注过程的有效场论因子化
- [P] `prop:jets-sll` (命题, tag P) — 超领头对数

## Ch17 — Chapter 17 — 小 $x$ 与高能因子化 / Small $x$ and high-energy factorization

Box:
- 证明了：（无新的 [R] 陈述；`ex:smallx-dla` 为固定耦合下的鞍点计算）。
- 给出全阶论证：`thm:smallx-bfkl`（LL/NLL）、`thm:smallx-bk`（LL，偶极子框架）（[A]）。
- 没有证明：$k_T$ 因子化的幂次修正控制（`prop:smallx-kt`，[P]）；饱和（`conj:smallx-saturation`，[C]）；与共线因子化的匹配。

- [A] `thm:smallx-bfkl` (定理, tag A) — BFKL 方程
- [P] `prop:smallx-kt` (命题, tag P) — $k_T$（高能）因子化
- [A] `thm:smallx-bk` (定理, tag A) — BK 方程与 JIMWLK
- [C] `conj:smallx-saturation` (猜想, tag C) — 饱和与色玻璃凝聚

## Ch18 — Chapter 18 — 因子化的破坏与非标准情形 / Breakdown of factorization and non-standard cases

Box:
- 证明了：`prop:break-colour`（[R, R_PT]）；`prop:break-measurement`（[R, R_cond]，前提 `asm:appO-lcopt`）。
- 给出全阶论证：`thm:break-ddis`、`thm:break-double-dy`（[A]）。
- 破坏（附证据类型）：`thm:break-tmd`（模型反例）、`prop:break-spacelike`（显式单圈计算，振幅层次）、`prop:break-fss`、`prop:break-jet-veto`（显式反例）、`prop:break-hh-diffraction`（实验）（[V]）。
- 没有证明：超出 NNLO 的质量奇异性因子化（`prop:break-mass-singularity`，[C]）；有色末态的 DPS 与“口袋公式”（[C]）。

- [V] `thm:break-tmd` (定理, tag V) — 强子—强子末态强子的 TMD 因子化不成立
- [V] `prop:break-spacelike` (命题, tag V) — 类空共线极限中严格共线因子化的失效
- [C] `prop:break-mass-singularity` (命题, tag C) — 超出 NNLO 的质量奇异性因子化
- [V] `prop:break-fss` (命题, tag V) — Coulomb 相位与软交换不对易导致的共线因子化破坏
- [V] `prop:break-jet-veto` (命题, tag V) — 对多重部分子相互作用敏感的观测量
- [A] `thm:break-ddis` (定理, tag A) — 衍射 DIS 的因子化
- [V] `prop:break-hh-diffraction` (命题, tag V) — 强子—强子硬衍射中的因子化破坏
- [A] `thm:break-double-dy` (定理, tag A) — 双 Drell–Yan 的因子化
- [C] `conj:break-dps-coloured` (猜想, tag C) — 有色末态的双部分子散射
- [C] `conj:break-pocket` (猜想, tag C) — "口袋公式" $\sigma_{\rm DPS}=\sigma_A\sigma_B/\sigma_{\rm eff}$

## Ch19 — Chapter 19 — 硬遍举过程 / Hard exclusive processes

Box:
- 证明了：`prop:excl-erbl`、`prop:excl-pion-lo`、`prop:excl-dvcs-lo`（[R, R_PT]）；`prop:excl-polynomiality`（[R, R_def]）；`prop:excl-soft-cancel`（[R, R_cond]，前提 `asm:appN-endpoint`、`asm:appN-collins`）。
- 给出全阶论证：`thm:excl-pion-ff`、`thm:excl-transition`、`thm:excl-dvcs`、`thm:excl-meson-L`（[A]）。
- 没有证明：端点区与软重叠的大小（`prop:excl-endpoint`，[P]）；横向光子的标准共线因子化（`prop:excl-meson-T`，[V]）；近阈重夸克偶素光生超出 LO（`prop:excl-near-threshold`，[P]）。

- [A] `thm:excl-pion-ff` (定理, tag A) — 介子电磁形状因子的因子化
- [A] `thm:excl-transition` (定理, tag A) — $\gamma^*\gamma\to\pi^0$ 形状因子
- [P] `prop:excl-endpoint` (命题, tag P) — 端点区域与软重叠
- [A] `thm:excl-dvcs` (定理, tag A) — DVCS 的因子化
- [A] `thm:excl-meson-L` (定理, tag A) — 纵向光子介子产生的因子化
- [V] `prop:excl-meson-T` (命题, tag V) — 横向光子：标准共线因子化失效
- [P] `prop:excl-near-threshold` (命题, tag P) — 近阈重夸克偶素光生（重夸克极限）

## Ch20 — Chapter 20 — 重夸克物理：$B$ 介子衰变与重夸克偶素 / Heavy-quark physics: $B$ decays and quarkonium

Box:
- 证明了：`prop:heavy-nrqcd-matching`（[R, R_PT]，单圈）。
- 给出全阶论证：`thm:heavy-bdpi`、`prop:heavy-btopi-ff`、`thm:heavy-inclusive-b`、`thm:heavy-nrqcd-decay`、`prop:heavy-quarkonium-fragmentation`（[A]）。
- 部分/猜想/破坏：`prop:heavy-qcdf-lp`（[P]）、`conj:heavy-nrqcd-production`（[C]）、`prop:heavy-qcdf-endpoint`（[V]）。

- [A] `thm:heavy-bdpi` (定理, tag A) — $B\to D\pi$ 的全阶因子化
- [A] `prop:heavy-btopi-ff` (命题, tag A) — 重到轻形状因子：软重叠与硬旁观者
- [P] `prop:heavy-qcdf-lp` (命题, tag P) — 无粲两体衰变的领头幂次 QCD 因子化
- [V] `prop:heavy-qcdf-endpoint` (命题, tag V) — 幂次修正中的端点发散
- [A] `thm:heavy-inclusive-b` (定理, tag A) — 单举 $B$ 衰变的重夸克展开
- [A] `thm:heavy-nrqcd-decay` (定理, tag A) — 衰变的 NRQCD 因子化
- [C] `conj:heavy-nrqcd-production` (猜想, tag C) — 产生的 NRQCD 因子化
- [A] `prop:heavy-quarkonium-fragmentation` (命题, tag A) — 大 $p_T$ 重夸克偶素产生

## Ch21 — Chapter 21 — 幂次修正、次领头幂次、重整化子与非微扰地位 / Power corrections, next-to-leading power, renormalons, non-perturbative status

Box:
- 证明了：`prop:power-next-to-soft`（[R, R_PT]，树图）；`prop:power-rearrangement`（[R, R_def]）；`thm:power-ope-convergence`（[R, R_PT]，$\varphi^4_4$）；`prop:power-adler-large-beta0`、`prop:power-thooft-model`（[P]：在大 $\beta_0$ 极限／二维大 $N_c$ 中完整证明）。
- 给出全阶论证：`prop:power-dis-twist4-x`（[A]，$x$ 空间）。
- 没有证明：一般的次领头幂次因子化（`prop:power-nlp-endpoint`，[P]）；强子—强子单自旋不对称的扭度 3 因子化（`conj:power-twist3-pp`，[C]）；红外重整化子与高扭度的一般对应（`conj:power-renormalon-ht`，[C]）；QCD 的构造（`rem:power-np-status`）。

- [A] `prop:power-dis-twist4-x` (命题, tag A) — DIS 扭度 4 修正的 $x$ 空间形式
- [P] `prop:power-twist3-sidis` (命题, tag P) — SIDIS 型过程中的扭度 3 共线因子化
- [C] `conj:power-twist3-pp` (猜想, tag C) — 强子—强子碰撞中单举强子单自旋不对称的扭度 3 因子化
- [P] `prop:power-nlp-endpoint` (命题, tag P) — 次领头幂次因子化与端点发散
- [P] `prop:power-adler-large-beta0` (命题, tag P) — 大 $\beta_0$ 极限下的 Adler 函数
- [P] `prop:power-renormalon-examples` (命题, tag P) — 若干过程中的重整化子与幂次修正
- [C] `conj:power-renormalon-ht` (猜想, tag C) — 红外重整化子与高扭度的一般对应
- [P] `prop:power-thooft-model` (命题, tag P) — 't Hooft 模型

## Ch22 — Chapter 22 — LaMET 与格点因子化：季向东等人的因子化证明 / LaMET and lattice factorization: the factorization proofs of Ji and collaborators

Box:
- 证明了：`prop:lamet-support`、`cor:lamet-entire`（[R, R_PT]）；`prop:lamet-oneloop`、`prop:lamet-tails`、`prop:lamet-twoloop`、`prop:lamet-hybrid-kernel`（[R, R_PT]，限于所述阶）；`thm:lamet-coordinate`（[R, R_cond]，前提 `prop:lattice-renormalizability`、`asm:lamet-ope`）、`thm:lamet-parton-momentum`（[R, R_cond]，前提 `thm:lamet-coordinate`）；`prop:lamet-tmc`（[R, R_cond]，前提 `asm:lamet-ope`）；`thm:lamet-hadronic`（[R, R_cond]，前提 `asm:lamet-uniform`、`asm:lamet-twist4`、`asm:lamet-large-z`）；`thm:lamet-exp-decay`（[R, R_cond]，前提 `asm:intro-wightman`、`asm:lamet-gap`）；`prop:lamet-sdf`（[R, R_cond]）；`lem:lamet-fourier`、`lem:lamet-strip`、`prop:lamet-truncation`、`prop:lamet-slepian`（数学）；`prop:lattice-moments`（[R, R_OPE]）。
- 给出全阶论证：`prop:lattice-renormalizability`（[A]；瓶颈 `asm:lamet-aux-renorm`）；`thm:lattice-lamet`、`prop:lamet-cfp`、`thm:lamet-lcs`、`prop:lamet-gluon-singlet`、`thm:lamet-quasi-gpd`（[A]；瓶颈 `asm:lamet-ope`）；`thm:lamet-quasi-tmd`、`prop:lattice-cs-kernel`、`prop:lamet-tmd-ratios`（[A]；瓶颈 `asm:lamet-order-limits`）；`cor:lamet-principle-pt`。
- 没有证明：LaMET 原理的非微扰形式（`conj:lamet-principle`，[C]）；强子层次匹配所需的 `asm:lamet-uniform`、`asm:lamet-twist4`、`asm:lamet-large-z`（[C]）；QCD 中 Wilson 线关联函数的指数衰减（`conj:lamet-decay-qcd`，[C]）；比值与 RI/MOM 方案在大 $|z|$ 处的动量空间匹配（`rem:lamet-ratio-large-z`，[C]）；GPD 在 $x=\pm\xi$ 的情形（第 23 章）。

- [C] `conj:lamet-principle` (猜想, tag C) — LaMET 原理（非微扰形式）
- [R-sketch] `prop:lamet-support` (命题, tag R, R_PT) — 准关联函数的支撑性质（逐图）
- [A] `asm:lamet-aux-renorm` (假设, tag A) — 含类空辅助静态色源的 QCD 的可重整性
- [A] `prop:lattice-renormalizability` (命题, tag A) — Wilson 线夸克双线性算符的乘法可重整性
- [A] `prop:lamet-ad-spacelike` (命题, tag A) — 类空与类时 Wilson 线算符的反常维度相同
- [P] `prop:lamet-lrr` (命题, tag P) — Wilson 线自能的线性重整子与领头重整子重求和
- [A] `prop:lamet-euclid-minkowski` (命题, tag A) — 欧氏格点矩阵元与 Minkowski 矩阵元的等同
- [R-sketch] `prop:lamet-oneloop` (命题, tag R, R_PT) — 准 PDF 匹配的单圈结果
- [P] `prop:lamet-polarized` (命题, tag P) — 极化、横度与扭度 3 准分布的匹配
- [A] `asm:lamet-ope` (假设, tag A) — 类空 Wilson 线算符的短距离 OPE（重整化微扰论）
- [V] `rem:lamet-early-form` (注, tag V) — 以强子动量为变量的早期匹配形式不成立
- [A] `prop:lamet-cfp` (命题, tag A) — 光锥规范下的共线减除路线（Ma–Qiu）
- [A] `thm:lamet-lcs` (定理, tag A) — “好的格点截面”的因子化（Ma–Qiu）
- [A] `thm:lattice-lamet` (定理, tag A) — LaMET 匹配定理（部分子态、领头幂次、全阶）
- [A] `prop:lamet-gluon-singlet` (命题, tag A) — 单态夸克与胶子准 PDF：带混合的匹配
- [A] `prop:lamet-scheme-validity` (命题, tag A) — 动量空间匹配在何种重整化方案中成立
- [C] `rem:lamet-ratio-large-z` (注, tag C) — 比值与 RI/MOM 方案在大 $|z|$ 处的动量空间匹配
- [C] `asm:lamet-gap` (假设, tag C) — 谱隙与边界值正则性
- [C] `conj:lamet-decay-qcd` (猜想, tag C) — QCD 准分布矩阵元的长程渐近形式
- [P] `prop:lamet-bvz` (命题, tag P) — 扭度 4 修正的重整子模型（大 $\beta_0$）
- [C] `asm:lamet-uniform` (假设, tag C) — 扭度展开对 Ioffe 时间的一致性
- [C] `asm:lamet-twist4` (假设, tag C) — 领头幂次修正的结构（扭度 4）
- [C] `asm:lamet-large-z` (假设, tag C) — 大距离区域的控制
- [C] `rem:lamet-inverse-problem` (注, tag C) — 逆问题之争：数学陈述与经验问题
- [A] `thm:lamet-quasi-gpd` (定理, tag A) — 准 GPD 与准 DA 的匹配
- [P] `prop:lamet-other-objects` (命题, tag P) — 其他准分布：重子与重介子 LCDA、$\Delta G$、双部分子分布
- [A] `asm:lamet-staple` (假设, tag A) — 订书钉形类空 Wilson 线算符的重整化与 $L\to\infty$ 极限
- [A] `asm:lamet-soft-rapidity` (假设, tag A) — 离光锥软函数的大快度结构
- [A] `asm:lamet-order-limits` (假设, tag A) — 极限次序
- [A] `thm:lamet-quasi-tmd` (定理, tag A) — 准 TMD 因子化
- [A] `prop:lattice-cs-kernel` (命题, tag A) — 格点 Collins–Soper 核
- [A] `prop:lamet-tmd-ratios` (命题, tag A) — 准 TMD 之比与 TMD 之比
- [A] `cor:lamet-principle-pt` (推论, tag A) — LaMET 原理的微扰内容

## Ch23 — Chapter 23 — Yizhuang Liu 的严格因子化研究 / The rigorous factorization research of Yizhuang Liu

Box:
- 证明了：`lem:yzliu-matrix-tree`、`lem:yzliu-final-state`（数学）；`prop:yzliu-sI-twoloop`、`prop:yzliu-gpd-oneloop`（[R, R_PT]，限于所述阶）；`cor:yzliu-soft-form-factor`（[R, R_cond]，前提 `asm:yzliu-heavy-pair`；内容等级 [C]）；在所述模型中：`thm:yzliu-gn-convergence`（作为 QCD 陈述为 [P]）。
- 给出全阶论证：`lem:yzliu-partial-exp`、`prop:yzliu-pinch-ultrasoft`、`thm:yzliu-soft-hqet`（[A]）；`thm:yzliu-analyticity`、`thm:yzliu-time-ordering`、`thm:yzliu-jet-continuation`（[A]；瓶颈 `asm:yzliu-wightman-pt`）；`prop:yzliu-rapidity-linear`、`thm:yzliu-intrinsic-soft`（[A]）；`prop:yzliu-qtmd-powercount`、`prop:yzliu-hard-kernel`、`prop:yzliu-lfwf`、`prop:yzliu-meson-ff`、`prop:yzliu-dy-quasi`、`prop:yzliu-sivers`、`thm:yzliu-threshold`、`prop:yzliu-ad-algebra`（[A]）。
- 没有证明：`asm:yzliu-wightman-pt` 作为数学命题；普适类的一般陈述（`prop:yzliu-universality-classes`，[P]，瓶颈 `asm:yzliu-lightcone-uniform`）；复时空 Wilson 圈猜想（`conj:yzliu-complex-wilson`，[C]）；大 $\beta_0$ 之外的重整子归一化与强子阈值渐近（`conj:yzliu-renormalon-norm`、`conj:yzliu-threshold-hadronic`，[C]）；GPD 在 $x=\pm\xi$（`conj:yzliu-gpd-xi`，[C]）；$e^+e^-$ 软因子的普适性。

- [A] `lem:yzliu-partial-exp` (引理, tag A) — 部分指数化引理
- [A] `prop:yzliu-pinch-ultrasoft` (命题, tag A) — 捏点奇点、超软模式与 $L\to\infty$ 极限
- [C] `asm:yzliu-heavy-pair` (假设, tag C) — 静态色单态 $Q\bar Q$ 对的谱假设
- [A] `thm:yzliu-soft-hqet` (定理, tag A) — 离光锥软函数是快速色源对的形状因子
- [A] `asm:yzliu-wightman-pt` (假设, tag A) — 维数正规化微扰论中的 Wightman 结构
- [A] `thm:yzliu-analyticity` (定理, tag A) — 软函数对复双曲角的解析性
- [A] `prop:yzliu-rapidity-linear` (命题, tag A) — 离光锥软函数中快度发散的因子化（线性性）
- [A] `thm:yzliu-intrinsic-soft` (定理, tag A) — 本征软函数：定义的等价、方案无关性与反常维度
- [P] `asm:yzliu-lightcone-uniform` (假设, tag P) — 光锥极限对 ${\rm Im}\,\theta$ 的一致性
- [P] `prop:yzliu-universality-classes` (命题, tag P) — 软函数的普适类
- [A] `thm:yzliu-time-ordering` (定理, tag A) — DY 形 TMD 软因子的时序无关性
- [P] `prop:yzliu-dy-sidis-exp` (命题, tag P) — 指数正规子下 DY 与 SIDIS 软因子相等
- [C] `conj:yzliu-complex-wilson` (猜想, tag C) — 复时空中的 Wilson 圈
- [A] `prop:yzliu-qtmd-powercount` (命题, tag A) — 准 TMD 因子化的 Collins 式证明：单线记号下的幂次计数
- [A] `prop:yzliu-hard-kernel` (命题, tag A) — 准 TMD 匹配核：RGE、重—轻分解与两圈结果
- [A] `prop:yzliu-lfwf` (命题, tag A) — 准光前波函数振幅的因子化
- [A] `prop:yzliu-meson-ff` (命题, tag A) — 大动量下的介子形状因子与 $S_I$ 的提取
- [A] `prop:yzliu-dy-quasi` (命题, tag A) — 以准 TMD 表示的小 $q_T$ Drell–Yan 截面
- [A] `prop:yzliu-sivers` (命题, tag A) — 由准 TMD 之比得到 Sivers 不对称
- [A] `thm:yzliu-jet-continuation` (定理, tag A) — 类空与类时重夸克喷注函数的解析延拓
- [A] `thm:yzliu-threshold` (定理, tag A) — 准 PDF 匹配核的阈值因子化（Ji–Liu–Su）
- [A] `prop:yzliu-ad-algebra` (命题, tag A) — 反常维度代数
- [P] `prop:yzliu-threshold-nnlo` (命题, tag P) — 阈值因子化的 NNLO 检验
- [P] `prop:yzliu-linear-renormalon` (命题, tag P) — 重—轻 Sudakov 核的线性红外重整子
- [C] `conj:yzliu-renormalon-norm` (猜想, tag C) — 线性重整子归一化的普适性
- [C] `conj:yzliu-threshold-hadronic` (猜想, tag C) — 强子夸克双线性矩阵元的阈值渐近
- [C] `conj:yzliu-gpd-xi` (猜想, tag C) — GPD 在 $x=\pm\xi$ 附近的 LaMET 可计算性
- [P] `thm:yzliu-gn-convergence` (定理, tag P) — 二维 $U(N)$ Gross–Neveu 模型中扭度展开的绝对收敛
- [P] `prop:yzliu-gn-structure` (命题, tag P) — Gross–Neveu 模型中扭度展开的结构：重整子相消与真空凝聚
- [P] `prop:yzliu-on-factorial` (命题, tag P) — 超可重整二维 $O(N)$ 模型：动量空间 OPE 的阶乘增强
- [P] `prop:yzliu-nlsm` (命题, tag P) — 二维非线性 $\sigma$ 模型：凝聚与跨级数
- [P] `prop:yzliu-2dqcd` (命题, tag P) — 二维大 $N_c$ QCD 中的准 PDF
- [P] `prop:yzliu-decay-extensions` (命题, tag P) — 标量场论中的谱表示与指数衰减（微扰论各阶）
- [A] `rem:yzliu-relation-css` (注, tag A) — 与 CSS、Collins 与 SCET 的关系

## Ch24 — Chapter 24 — 其他前沿严格结果 / Other rigorous frontier results

Box:
- 证明了：`lem:front-min-norm`、`lem:front-jantzen`（数学；后者在其局部假设 (J1)–(J4) 下）；`prop:front-lp-facets`、`prop:front-onshell-facets`（[R, R_PT]）；`cor:front-coleman-norton`（[R, R_cond]，前提 `thm:front-collins-pinch`）；`prop:front-commuting`（[R, R_cond]，前提 `asm:front-mor-complete`）；`prop:front-msbar-negative`(a)（单圈 Yukawa 模型，[R, R_PT]）。已知不成立（[V]）：`prop:front-anomalous`、`prop:front-landau-not-singular`、`prop:front-hidden-regions`、`prop:front-jettiness-cvl`、`prop:front-msbar-negative`、`prop:front-regge-pole`、`prop:front-ew-violation`。
- 给出全阶论证（[A]）：`prop:front-brst-bilocal`（规划标签 [A]；N04 通过——含循环性检查——后升为 [R, R_PT]，MD7）、`thm:front-collins-pinch`（证明仅见于预印本）、`prop:front-ir-forest`、`prop:front-coordinate-space`、`prop:front-glauber-bfkl`、`prop:front-syz`、`prop:front-heavy-fsi`、`prop:front-sll-all-orders`、`prop:front-sll-closed-form`、`thm:front-hgg`、`prop:front-ggh`、`prop:front-nlp-ll`、`prop:front-nlp-dis`（预印本）、`prop:front-tmd-nlp-operator`、`prop:front-sidis-nlp`、`prop:front-nlo-bk`、`prop:front-regge`、`prop:front-smallx-tmd`、`prop:front-smallx-helicity`、`prop:front-dps-scheme`、`prop:front-rapidity-renorm`、`prop:front-ngl`、`prop:front-jet-substructure`、`prop:front-lightray-ope`、`thm:front-luxqed`、`prop:front-lepton-pdf`、`prop:front-ew-pdf`。部分结果（[P]，有限阶、模型或子类）：`prop:front-local-ir`、`prop:front-ope-scalar`、`prop:front-ope-ym`、`prop:front-flow-renorm`、`prop:front-restoration`、`prop:front-nlp-threshold`、`prop:front-nlp-tmd-oneloop`、`prop:front-positivity-large-scale`、`prop:front-bk-collinear`、`prop:front-dpd-evolution`、`prop:front-nrqcd-ir`。
- 没有证明（[C]）：`conj:front-ope-convergence`、`conj:front-mor-minkowski`（及其前提形式 `asm:front-mor-complete`）、`conj:front-mpi-violation`、`conj:front-nlp-beyond-ll`、`conj:front-glauber-nlp`、`conj:front-brst-multilocal`。

- [V] `prop:front-anomalous` (命题, tag V) — "规避奇点需要严格正的一阶位移"不成立
- [A] `thm:front-collins-pinch` (定理, tag A) — 物理区钳夹判据（Collins 2020）
- [V] `prop:front-landau-not-singular` (命题, tag V) — Landau 条件只是奇点的必要条件
- [A] `prop:front-ir-forest` (命题, tag A) — 宽角振幅的红外森林公式（Ma 2020）
- [A] `prop:front-coordinate-space` (命题, tag A) — 振幅的全阶硬—软—共线因子化：坐标空间路线与算符路线
- [P] `prop:front-local-ir` (命题, tag P) — 被积函数层次的局域红外因子化
- [V] `rem:front-landau-algebraic` (注, tag V) — 代数几何的 Landau 分析与偶极子公式
- [P] `prop:front-ope-scalar` (命题, tag P) — 标量场论中 OPE 的收敛、结合律与弯曲时空
- [P] `prop:front-ope-ym` (命题, tag P) — 纯 Yang–Mills 理论中 OPE 在规范不变算符上闭合
- [P] `prop:front-flow-renorm` (命题, tag P) — 流方程（Wilson–Polchinski）重整化证明
- [C] `conj:front-ope-convergence` (猜想, tag C) — Yang–Mills 与 QCD 中 OPE 的收敛
- [A] `rem:front-ope-qcd-status` (注, tag A) — 对含夸克的 QCD，本书能断言什么
- [C] `asm:front-mor-complete` (假设, tag C) — 区域集合的完备性
- [V] `prop:front-hidden-regions` (命题, tag V) — "区域 = Newton 多面体的下表面"在 Minkowski 运动学中不成立
- [C] `conj:front-mor-minkowski` (猜想, tag C) — Minkowski 极限下区域方法的有效性
- [A] `prop:front-glauber-bfkl` (命题, tag A) — Glauber 有效理论：Regge 化、BFKL 与零箱减除
- [A] `prop:front-syz` (命题, tag A) — 纯 Glauber 梯形图在单标度红外安全观测量中的相消
- [C] `conj:front-mpi-violation` (猜想, tag C) — 对多重部分子相互作用敏感的观测量：标准因子化的破坏
- [A] `prop:front-heavy-fsi` (命题, tag A) — 重末态与旁观者之间的软末态相互作用
- [A] `rem:front-glauber-status` (注, tag A) — Glauber 现状与本书分级的后果
- [A] `prop:front-sll-all-orders` (命题, tag A) — 非全局 LHC 观测量的因子化与超领头对数的全阶重求和
- [A] `prop:front-sll-closed-form` (命题, tag A) — 超领头对数的塔与 $q\bar q$ 单态交换的闭式
- [P] `prop:front-restoration` (命题, tag P) — Glauber 胶子引起的"因子化恢复"
- [V] `prop:front-jettiness-cvl` (命题, tag V) — 1-jettiness 中的相干性破坏对数
- [A] `asm:front-scet-modes` (假设, tag A) — SCET 的模式完备性与 Glauber 模式的缺席
- [A] `thm:front-hgg` (定理, tag A) — $h\to\gamma\gamma$（$b$ 夸克圈）的重整化端点因子化定理
- [A] `prop:front-ggh` (命题, tag A) — 轻夸克诱导的 $gg\to h$ 与重因子化减除方案
- [P] `prop:front-nlp-threshold` (命题, tag P) — 次领头幂次阈值 Drell–Yan 的 $d$ 维因子化
- [A] `prop:front-nlp-ll` (命题, tag A) — 次领头幂次的领头对数重求和与端点因子化条件
- [A] `prop:front-nlp-dis` (命题, tag A) — 次领头幂次 DIS 与 PDF 因子化：阈值 PDF 的双标度结构
- [C] `conj:front-nlp-beyond-ll` (猜想, tag C) — 超出领头对数的次领头幂次端点因子化
- [C] `conj:front-glauber-nlp` (猜想, tag C) — 次领头幂次 TMD 过程中 Glauber 交换的相消
- [A] `prop:front-tmd-nlp-operator` (命题, tag A) — TMD 算符展开与运动学幂次修正
- [A] `prop:front-sidis-nlp` (命题, tag A) — SIDIS 方位角不对称的次领头幂次 SCET 因子化
- [P] `prop:front-nlp-tmd-oneloop` (命题, tag P) — 单圈次领头幂次系数函数与扭度 3 TMD 演化
- [V] `prop:front-msbar-negative` (命题, tag V) — $\overline{\rm MS}$ 部分子分布可以为负
- [P] `prop:front-positivity-large-scale` (命题, tag P) — 足够大标度上的正定性
- [A] `prop:front-brst-bilocal` (命题, tag A) — 双局域 PDF 算符 BRST 分类的矩约化
- [C] `conj:front-brst-multilocal` (猜想, tag C) — 多局域光线算符的 BRST 分类
- [A] `prop:front-nlo-bk` (命题, tag A) — NLO BK/JIMWLK 与三圈 BK 核
- [P] `prop:front-bk-collinear` (命题, tag P) — NLO BK 的不稳定性与共线重求和
- [A] `prop:front-regge` (命题, tag A) — 高能极限中的 Wilson 线方法、胶子 Regge 化与 Regge 极限的红外奇异部分
- [V] `prop:front-regge-pole` (命题, tag V) — 简单 Regge 极点因子化在 NNLL 失效
- [A] `prop:front-smallx-tmd` (命题, tag A) — 小 $x$ 的 TMD 与 Sudakov 对数
- [A] `prop:front-smallx-helicity` (命题, tag A) — 小 $x$ 螺旋度演化：截距与 BER 的分歧
- [A] `prop:front-dps-scheme` (命题, tag A) — 无重复计数的双部分子散射
- [A] `prop:front-rapidity-renorm` (命题, tag A) — 多部分子软因子快度发散的重整化定理
- [P] `prop:front-dpd-evolution` (命题, tag P) — 色关联 DPD 的演化与匹配
- [A] `prop:front-ngl` (命题, tag A) — 非全局对数：超出领头对数与测量驱动的因子化
- [A] `prop:front-jet-substructure` (命题, tag A) — 喷注子结构、修饰喷注与半单举喷注函数
- [A] `prop:front-lightray-ope` (命题, tag A) — 能量关联子的共线因子化与共形场论中的光线 OPE
- [P] `prop:front-nrqcd-ir` (命题, tag P) — NNLO 的红外极点与规范完备的八重态算符
- [A] `rem:front-quarkonium-alternatives` (注, tag A) — 唯象张力与替代方案
- [A] `thm:front-luxqed` (定理, tag A) — 由结构函数确定质子的光子 PDF（LUXqed）
- [A] `prop:front-lepton-pdf` (命题, tag A) — 轻子与电子的 PDF、QED 与混合演化核
- [A] `prop:front-ew-pdf` (命题, tag A) — 电弱 PDF 与 $Q\gg M_W$ 的电弱对数
- [V] `prop:front-ew-violation` (命题, tag V) — 电弱 Bloch–Nordsieck 抵消的失效与测量弱荷的观测量

## Ch25 — Chapter 25 — 总结：主表、依赖图与开放问题 / Summary: master table, dependency graph and open problems


## AppA — Appendix A — 光锥坐标、Dirac 代数、加号分布与 Mellin 变换 / Light-front coordinates, Dirac algebra, plus distributions, Mellin transforms


## AppB — Appendix B — Wilson 线：Feynman 规则、程函恒等式与尖点 / Wilson lines: Feynman rules, eikonal identities, cusp

- [A] `prop:appB-webs` (命题, tag A) — 非阿贝尔指数化

## AppC — Appendix C — 维数正规化积分与相空间 / Dimensional-regularization integrals and phase space


## AppD — Appendix D — Landau 方程与 Coleman–Norton 定理 / Landau equations and the Coleman–Norton theorem


## AppE — Appendix E — 幂次计数公式的推导 / Derivation of the power-counting formula

- [A] `rem:appE-actual-bound` (注, tag A) — 从超表观度到实际界

## AppF — Appendix F — 图形 Ward 恒等式 / Graphical Ward identities

- [A] `prop:appF-induction` (命题, tag A) — 多胶子情形的归纳论证

## AppG — Appendix G — 单圈与两圈计算细节 / Details of one- and two-loop calculations


## AppH — Appendix H — 文献导读 / Annotated bibliography


## AppI — Appendix I — 维数正规化中的 $\gamma_5$ / $\gamma_5$ in dimensional regularization


## AppJ — Appendix J — BRST 对称性与割图中的鬼场 / BRST symmetry and ghosts in cut diagrams

- [R-sketch] `prop:appJ-local-operators` (命题, tag R, R_PT) — 规范不变定域算符的重整化与混合
- [A] `rem:appJ-nonlocal` (注, tag A) — 非定域算符

## AppK — Appendix K — 矩问题与解析延拓引理 / Moment problems and continuation lemmas


## AppL — Appendix L — 光线算符与定域算符：矩关系的全阶证明 / Light-ray and local operators: all-order proof of the moment relation


## AppM — Appendix M — OPE：微扰证明、无质量 QCD、非微扰条件定理 / The OPE: perturbative proof, massless QCD, non-perturbative conditional theorems

Box:
- 证明了：`thm:appM-ope-identity`、`thm:appM-zimmermann-identity`、`cor:appM-reduction`、`lem:appM-integrability`（\tagR，$R_{\rm PT}$）；`lem:appM-uniqueness`（\tagR，$R_{\rm PT}$；无质量情形逐块，条件 (NE)，`lem:appM-ne`）；`thm:appM-scaling`、`cor:appM-coordinate`（\tagR，$R_{\rm cond}$，前提 `asm:appM-remainder`）；`lem:appM-alien-vanish`（\tagR，$R_{\rm PT}$）；`thm:appM-brst-reduction`（\tagR，$R_{\rm cond}$，前提 `asm:appM-brst-ope`，内容 [A]）；`thm:appM-forward-expansion`（\tagR，$R_{\rm PT}$，逐图：投影子方法的解析步骤）、`lem:appM-t2-projector`（$R_{\rm PT}$）、`lem:appM-gluon-regularity`（$R_{\rm cond}$，前提 `asm:appM-oswi`）；数学引理 `lem:appM-ne`、`lem:appM-lbc-formal`、`lem:appM-newton`、`lem:appM-matroid`、`lem:appM-curved-approach`；第 7 章 `lem:dis-twist-classification`、`lem:dis-twist-chirality`（$R_{\rm def}$）、`prop:dis-chiral-suppression`（$R_{\rm PT}$）、`prop:dis-ope-rg`（$R_{\rm OPE}$；直接由 (A3) 推出，含 $\beta_\xi\partial_\xi$）、`prop:dis-low-moments`（$R_{\rm def}$）的证明；`prop:dis-dispersion-np`、`lem:dis-ope-segment`、`thm:dis-fixed-n`、`thm:dis-moments-np`、`cor:dis-weak-xspace`（$R_{\rm cond}$，前提 `asm:intro-*`）的证明。
- 给出全阶论证：`prop:dis-ope-euclid`（\tagA，引用的欧氏渐近展开定理；`Smirnov:1990rz` 已核对，范围不足）、`prop:dis-ope-gi`（\tagA，瓶颈 `asm:appM-brst-ope` 的 (Eε)）、`prop:dis-ope-forward`（\tagA；经 `cor:appM-forward-ope` 化归为 (A3)+(Eε)+Joglekar–Lee，未解除 `asm:appM-forward`）、`cor:appM-forward-ope`、`cor:appM-cut-plane`、`prop:appM-zero-momentum-insertion`（\tagA）。
- 没有证明：冻结 $q$ 正规乘积的动量空间余项估计（`asm:appM-remainder`；化归为零动量匹配估计 (CTp)，`rem:appM-remainder-reduction`）；带复合旁观者的维数正规化欧氏展开（`asm:appM-brst-ope` 的 (Eε)）；前向在壳胶子 Ward 恒等式（`asm:appM-oswi`）；前向在壳部分子矩阵元的余项（`asm:appM-forward`，已化归、未解除）；纯 Yang–Mills 的 BRST 结论（未核实）；QCD 作为 Wightman 理论的存在与非微扰 OPE（`asm:intro-wightman`、`asm:intro-np-ope`）；$n<n_0$ 所需的增长条件（`asm:intro-growth`）；OPE 在有限距离的收敛（QCD 中为 \tagC）；重整子吸收（`conj:power-renormalon-ht`）。

- [A] `asm:appM-remainder` (假设, tag \tagA) — 冻结 $q$ 双局域正规乘积的动量空间余项估计
- [A] `rem:appM-exceptional` (注, tag A) — 例外动量与前向矩阵元
- [A] `prop:appM-zero-momentum-insertion` (命题, tag A) — 零动量扭度 2 算符插入在维数正规化中的存在性
- [A] `asm:appM-forward` (假设, tag \tagA) — 前向在壳无质量部分子矩阵元的 OPE 余项
- [A] `asm:appM-brst-ope` (假设, tag \tagA) — OPE 的 BRST 结构：带一个复合旁观者的欧氏展开 (Eε)
- [A] `cor:appM-forward-ope` (推论, tag A) — 每阶的前向在壳部分子 OPE
- [A] `asm:appM-oswi` (假设, tag \tagA) — 前向在壳胶子振幅的 Ward 恒等式
- [A] `cor:appM-cut-plane` (推论, tag A) — 部分子前向振幅在割平面上的全纯性、不连续性与矩
- [C] `rem:appM-supporting` (注, tag C) — 支持性的严格结果

## AppN — Appendix N — Collins 减除法的精确形式 / The precise form of Collins' subtraction method

Box:
- 证明了：`thm:appN-subtraction`（\tagR，$R_{\rm cond}$，前提 `asm:appN-contour`）；`thm:appN-fibered-subtraction`、`lem:appN-identification`、`lem:appN-lp-certificate`（数学：实纤维化底空间上的积分范数形式，可逐图检验的条件 (FR)(FI)）；`lem:appN-lc-positivity`（$R_{\rm PT}$）；`cor:appN-cs3-fibered`（$R_{\rm cond}$，前提 `asm:appN-lce`）；第 9 章 `lem:method-meets`、`lem:method-covering`、`prop:method-chains`、`lem:method-pairing`、`prop:method-product`、`lem:method-no-pole`、`lem:method-telescoping`（数学）、`lem:method-i0-compat`（$R_{\rm PT}$）、`lem:method-local-accuracy`、`cor:method-removing-eps`（$R_{\rm cond}$）的证明；`lem:appN-error-table`（$R_{\rm cond}$）；第 10 章 `prop:disall-two-routes`、`prop:disall-factorized-subtraction`、`thm:disall-renorm-compat`，第 14 章 `prop:tmd-zero-bin-soft`，第 19 章 `prop:excl-soft-cancel` 的证明（$R_{\rm cond}$）；`prop:appN-sia`、`prop:appN-thrust`、`prop:appN-dy`、`prop:appN-tmd-window`、`thm:appN-structure`（$R_{\rm cond}$）；`prop:appN-triangle-exact`、`prop:appN-ladder`（$R_{\rm PT}$）；`prop:appN-triangle-cs`（$R_{\rm PT}$，计算机辅助：单圈离壳三角图的纤维化 (CS1)–(CS3) 与积分减除定理）；`prop:appN-phi36-dis`、`prop:appN-massive-photon`、`prop:appN-twoloop-algebra`（$R_{\rm PT}$，标量模型）；`prop:appN-twoloop-remainder`（$R_{\rm cond}$，前提 `asm:appN-analytic-reg`、`asm:appN-values`）。
- 给出全阶论证（以编号假设的形式）：`asm:appN-collins`、`asm:appN-envelope`、`asm:appN-separation`、`asm:appN-contour`、`asm:appN-cutsum`、`asm:appN-ward-product`、`asm:appN-uv`、`asm:appN-multren`、`asm:appN-tmd`、`asm:appN-endpoint`、`asm:appN-lce`、`asm:appN-analytic-reg`（均为 \tagA）。
- 没有证明：一般图的 (CS1)–(CS3)（`asm:appN-collins`；纤维化形式只对单圈三角图与 $\varphi^3_6$ 单梯级梯形图完整验证，一般单圈 Sudakov 型图与 QCD 两级梯形图未完成）；变形四维围道上的一致积分界（对三角图已不需要）；规范理论的分子、Ward 恒等式与横向极化的 (Abs)；(Abs) 的边缘情形（`rem:appN-abs-edge`）；保持 Ward 恒等式、规范化在壳胶子靶的红外正规化（`asm:appN-ir-regulator`，\tagC）；多定域光线算符的 BRST 分类（`asm:appN-brst-nonlocal`，\tagC，具名缺口；故 `thm:appN-structure` 的内容等级为 [C]）；发散链项的取值是约定（`asm:appN-values`）。

- [A] `asm:appN-contour` (假设, tag \tagA) — (GA1) 围道
- [A] `asm:appN-envelope` (假设, tag \tagA) — (GA3) 幂次计数包络
- [A] `asm:appN-separation` (假设, tag \tagA) — (GA4) 分离性
- [A] `asm:appN-lce` (假设, tag \tagA) — 光锥序表示与协变值的等同（LCE）
- [A] `asm:appN-collins` (假设, tag \tagA) — 一般图的 Collins 条件
- [A] `asm:appN-ward-product` (假设, tag \tagA) — Ward 恒等式的乘积结构与减除的重组
- [C] `asm:appN-brst-nonlocal` (假设, tag \tagC) — 多定域光线算符的 BRST 分类
- [A] `asm:appN-cutsum` (假设, tag \tagA) — 割图求和的公共表示
- [A] `asm:appN-uv` (假设, tag \tagA) — 被积函数层次的紫外重整化
- [A] `asm:appN-multren` (假设, tag \tagA) — 共线因子的乘法重整化（维数正规化路线）
- [C] `asm:appN-ir-regulator` (假设, tag \tagC) — 保持 Ward 恒等式的部分子靶红外正规化
- [A] `asm:appN-tmd` (假设, tag \tagA) — TMD 输入
- [A] `asm:appN-endpoint` (假设, tag \tagA) — 端点条件
- [A] `asm:appN-analytic-reg` (假设, tag \tagA) — 两圈图样积分的辅助解析正规化

## AppO — Appendix O — 光锥排序微扰论与 Drell–Yan 的 Glauber 相消 / Light-cone-ordered perturbation theory and the Glauber cancellation in Drell–Yan

Box:
- 证明了：`lem:appO-lcopt`、`lem:appO-numerators`、`lem:appO-glauber-pc`、`lem:appO-insertion-values`、`lem:appO-joint-localization`（扇区规则、含 $\sum_\sigma|w_\sigma|$ 的误差界、权重的连续性与扭结）、`lem:appO-multipole-localization`、`lem:appO-quadrant-residues`、`lem:appO-preintegration-localization`、`lem:appO-no-crossing`、`prop:appO-target`、`prop:appO-eikonal`、`prop:appO-strict-window-shape`（\tagR，$R_{\rm PT}$）；`lem:appO-cut-position`、`lem:appO-equal-time`、`lem:appO-carrier`、`lem:appO-kplus-rotation`、`lem:appO-ray-identity`、`lem:appO-two-insertion-bounds`（数学）；`lem:appO-glauber-operator`、`lem:appO-halfcoinc-colour`（$R_{\rm def}$；指向过去的软因子的幺正性是第 9 章 `lem:method-soft-unitarity` 的过去指向情形）；`lem:appO-hard-locality`、`lem:appO-unitarity`、`prop:appO-ss-localize`、`lem:appO-side-independent-windows`、`prop:appO-ss-cancel`、`prop:appO-one-sided`、`thm:appO-main`、`cor:appO-interface`、`prop:appO-tmd`（$R_{\rm cond}$）；`lem:appO-orientation`（$R_{\rm PT}$；第 12 章 `lem:dy-poles-orientation` 即其陈述）；第 12 章 `prop:dy-eikonal-twogluon` 的证明（$R_{\rm PT}$）；全局两时模型中的模型定理 `prop:appO-twoexch-spectator`、`prop:appO-twoexch-regulated`、`prop:appO-halfcoinc-sensitivity`、`prop:appO-pergraph-weights`（模型内完整证明；作为 QCD 陈述为 [P]）。
- 给出全阶论证：`prop:appO-past-wilson`（\tagA：Wilson 线指向过去；逐项匹配归入 `asm:appO-rewritten-cs`）；`prop:appO-g6-ladder`（\tagA：$O(g^6)$ 直接线梯形图类在幺正性下不封闭）。
- 没有证明：LCOPT 的零模与瞬时圈（`asm:appO-lcopt`）；纤维积分误差的可积包络（`asm:appO-envelope`，对重合连接按侧求和族施加）；一般软子图与同一部分子上非对易插入的完整图集相消（`asm:appO-mixing`）；一般构型的形变、与区域集合代数的相容性、软角区、H-发射端点（`asm:appO-deformation`，(b)(c)(d) **即使对阿贝尔理论与 $\mathcal G_0$ 也需要**）；改写形式的 (CS1)(CS2)（`asm:appO-rewritten-cs`）；被割的直接 SS 线（实发射，`rem:appO-cut-ss`）；共线端点的匹配（`asm:appO-collinear-ends`）及 QCD 喷注的 (ADJ)(REAL)（`asm:appO-adjacent-swap`、`asm:appO-real-jets`；三者只进入模型定理的 QCD 转移，不是 `thm:appO-main` 的前提）。外态为色单态微扰模型；非微扰强子见 `asm:intro-bridge`。

- [A] `asm:appO-lcopt` (假设, tag \tagA) — 光锥序微扰论的适用性
- [P] `asm:appO-adjacent-swap` (假设, tag \tagP) — 相邻交换对称性（ADJ）
- [P] `asm:appO-real-jets` (假设, tag \tagP) — 旁观者喷注函数的实性（REAL）
- [A] `asm:appO-collinear-ends` (假设, tag \tagA) — 共线端点的匹配
- [P] `prop:appO-twoexch-spectator` (命题, tag P) — 全重合 SS 对的 $O(g^4)$ 侧求和（未割线）：全局两时模型中的相消
- [P] `prop:appO-twoexch-regulated` (命题, tag P) — 正规化版本、端点极点与双侧正规子
- [P] `prop:appO-pergraph-weights` (命题, tag P) — 全重合对的逐图次序权重不由窗口数据决定
- [P] `rem:appO-halfcoinc` (注, tag P) — 半重合对：无正规子的两时模型
- [P] `prop:appO-halfcoinc-sensitivity` (命题, tag P) — 半重合对：$W_{12}$ 的实部与对 $k^-$ 正规子的敏感性
- [A] `prop:appO-g6-ladder` (命题, tag A) — $O(g^6)$：直接线梯形图类在幺正性下不封闭
- [A] `asm:appO-envelope` (假设, tag \tagA) — 纤维积分误差的可积包络
- [A] `asm:appO-mixing` (假设, tag \tagA) — Glauber–软混合与重合连接的完整图集相消
- [A] `asm:appO-deformation` (假设, tag \tagA) — 一般构型、相容性、软角区与 H-发射端点
- [A] `asm:appO-rewritten-cs` (假设, tag \tagA) — 改写形式与族求和形式的 Collins 条件
- [A] `prop:appO-past-wilson` (命题, tag A) — Ward 恒等式与指向过去的 Wilson 线
- [C] `rem:appO-literature-comparison` (注, tag C) — 与其他全阶论证的比较；TMD 版本；有争议的提议

## AppP — Appendix P — 形式化蓝图：假设登记表、依赖图与状态表 / The formal blueprint: assumption register, dependency graphs and status table


## AppQ — Appendix Q — 经核实的文献勘误 / Verified literature errata

