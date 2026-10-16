import os, sys, re
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import src
import regtable
TARGET = 'ASSUMPTIONS.md'
A = lambda n: src.ln(n, 'ASSUMPTIONS.md')

OUTLINE = src.TEXTS.get('FINAL_OUTLINE_v2.md')
USERS = regtable.users_map(OUTLINE)
def U(lab):
    us = USERS.get(lab, [])
    return ', '.join('`%s`' % u for u in us) if us else '—'

STATUS_OLD = '**Status (revision v2.2, merged).**'
STATUS_NEW = ('**Status (revision v2.3, verify patch of 2026-10-11; merged revision v2.2).** v2.3 applies the outcomes of the verification workflow '
              '(`verify/CLAIM_VERDICTS.md`; proof extensions X1–X3, `verify/extend_reports/`): six new entries (`asm:appM-oswi`, `asm:appN-lce`, '
              '`asm:appN-analytic-reg`, `asm:appO-adjacent-swap`, `asm:appO-real-jets`, `asm:appO-collinear-ends`), the rewordings of `asm:appM-brst-ope`, '
              '`asm:appO-mixing`, `asm:appO-envelope`, `asm:appO-deformation`, the status and upgrade fields of the entries touched by X1–X3, and §1 '
              'regenerated (47 entries; FINAL_OUTLINE_v2 decision MD19). Earlier status:')

REMAINDER_STATUS = r'''- **地位：** 在所述形式下开放（v2.3）：验证扩展的槽位 X3a 未交付——经由 `lem:appM-uniqueness` 从已发表的动量空间 OPE 定理推出本假设的路线是循环的（唯一性论证本身要用到余项估计），所引文献的适用范围亦未核实；本假设已化归为零动量匹配估计 (CTp)（`rem:appM-remainder-reduction`）；维数正规化路线（`prop:dis-ope-euclid` 的 (A1)–(A4)）不需要本假设。'''
REMAINDER_LIT = r'''- **文献：** `Anikin:1978tj`, `Zavyalov:1990kv` (momentum-space OPE; scope not verified), `Zimmermann1973`, `Smirnov:1990rz`, `Smirnov2002`, `Bergere:1977wz` (asymptotic expansions of Feynman amplitudes).'''
REMAINDER_UP = r'''- **解除途径：** a proof of the zero-momentum matching estimate (CTp) by sector (Weinberg-type) estimates; or a momentum-space OPE theorem whose theory class and remainder form are verified to cover the frozen-$q$ form (slot X3a not delivered).'''

BRST_ENTRY = r'''#### `asm:appM-brst-ope` — OPE 的 BRST 结构：带一个复合旁观者的欧氏展开 (Eε) [\tagA]
- **所属：** App M §M.6 (`sec:appM-brst`). Technical. (Reworded in v2.3 after the X3 verification; the label is kept.)
- **陈述：** Massless QCD in bare dimensional regularization at fixed generic $\varepsilon$ (any gauge parameter $\xi_0$, $B$ off shell, no $\gamma_5$, $D$-dimensional algebra). **(B2) ≡ (Eε):** for one composite spectator $Z=s\phi$ ($\phi$ an elementary field) and products $\Phi$ of elementary fields, the large-$q$ expansion $\langle\mathcal J(q)\,Z\,\Phi\rangle=\sum_{d_O\le a}C_O\langle O\,Z\,\Phi\rangle+\sum_{O'}C^Z_{O'}(q;p_Z)\langle O'\,\Phi\rangle+\mathcal R'$ holds, with the coefficients $C_O$ of the expansion without $Z$ (`prop:dis-ope-euclid`), **merged coefficients** $C^Z_{O'}$ (hard subgraphs containing the $Z$ vertex) polynomial in $p_Z$, all coefficients graded-homogeneous, and $\mathcal R'=O(|q|^{1-a}\ln^k|q|)$. **(B1)** is retired (the name is not reused): its Ward identities hold exactly in DR and its contact-term clause is not needed. The earlier form of (B2), without merged terms, is not the correct generalization of the Euclidean expansion: the merged terms turn $sX_d=0$ into $sX_d\in\mathcal E$ (`thm:appM-brst-reduction`).
- **地位：** 开放（v2.3）：槽位 X3d 部分完成——在 (Eε) 下，物理矩阵元只需规范不变算符这一化归已证明（`thm:appM-brst-reduction`，[R, R_cond]；形式上的定域 BRST 上同调 `lem:appM-lbc-formal`）；(Eε) 本身是带一个复合旁观者的逐图维数正规化欧氏展开，未证明。Joglekar 1977 只在摘要层次读过；Hollands 2008 与 Fröb–Holland 2016（预印本）覆盖纯 Yang–Mills，其对含夸克 QCD 的适用范围未核实（S63-3）。
- **文献：** `Joglekar:1976eb`, `Joglekar:1976pe` (abstract level), `Joglekar:1975nu`, `Kluberg-Stern:1975ebk`, `Henneaux:1995ex`, `Barnich:1999cy` (gauge-fixed BRST cohomology), `Hollands:2007zg`, `Frob:2016mzv` (预印本), `Piguet:1995er`.
- **被使用于：** %s (direct `\uses` users in FINAL_OUTLINE_v2, computed after the verify patch).
- **解除途径：** a proof of (Eε) (graph-by-graph DR expansion with one composite spectator, merged hard subgraphs); for pure Yang–Mills a comparison with Hollands' position-space OPE.
- `\uses{def:appM-alien}`
''' % U('asm:appM-brst-ope')

FORWARD_STATUS = r'''- **地位：** 开放（v2.3）：逐图的前向在壳展开定理已证明（`thm:appM-forward-expansion`，[R, R_PT]；槽位 X3e 逐图通过）；`cor:appM-forward-ope`（[A]）把本假设化归为 (A3)、(Eε)、Joglekar–Lee 三角性与胶子的 `asm:appM-oswi`——化归而非解除；在 $O(\alpha_s)$ 对 $N\le8$ 精确到 $\varepsilon$ 验证（`ex:appM-forward-oneloop`, VF-DIS-13）；槽位 X3c 未交付（被 X3e 取代）。'''
FORWARD_UP = r'''- **解除途径：** discharge the inputs of `cor:appM-forward-ope` ((A3), (Eε), the Joglekar–Lee triangularity, `asm:appM-oswi`); Ch25 OP-A5.'''

OSWI_ENTRY = r'''
#### `asm:appM-oswi` — 前向在壳胶子振幅的 Ward 恒等式 [\tagA]
- **所属：** App M §M.7 (`sec:appM-forward`). Technical. New in v2.3 (X3 verification).
- **陈述：** For the amputated forward on-shell gluon Compton amplitude $M_{ab}$ at each order in DR, $p^aM_{ab}\varepsilon^b=0=\varepsilon^aM_{ab}p^b$ for all $\varepsilon$ with $\varepsilon\cdot p=0$ (including $\varepsilon=p$); equivalently $p^aM_{ab}\propto p_b$ (the BRST form, the ghost amplitude being inside the proportionality factor).
- **地位：** [A]：前向振幅的 BRST Ward 恒等式；单独陈述，是因为零动量转移与在壳无质量胶子的红外微妙之处（`rem:appM-forward-aliens`，R-M24）使标准证明不能直接套用。
- **文献：** `KugoOjima1979`, `Collins:1994ee` (forward on-shell subtleties).
- **被使用于：** %s (direct `\uses` users in FINAL_OUTLINE_v2, computed after the verify patch).
- **解除途径：** a proof of the forward on-shell Ward identity at all orders (BRST with on-shell IR control).
- `\uses{def:dis-compton, def:prelim-brst}`
''' % U('asm:appM-oswi')

COLLINS_STATUS = r'''- **地位：** [A] 层次：Collins 2011 第 10 章断言之（在该章的严格程度下对 Sudakov 形状因子完整：标度陈述）；可证部分：极小 $R_0$ 的 (CS1)（`lem:method-local-accuracy`）、(Com)(Abs) 下化为分组幂次计数（`prop:method-product`）；单圈离壳三角图已完整证明（`prop:appN-triangle-cs`，槽位 X2a；纤维化积分范数 E-N$^\varphi$，`thm:appN-fibered-subtraction`）；一般单圈图与两级梯形图未交付（槽位 X2b、X2c；部分证据 `prop:appN-phi36-dis`、`prop:appN-massive-photon`、`prop:appN-twoloop-remainder`）；障碍：逐项条件为假（`prop:appN-ladder`(c)）、(Abs) 的失效（`rem:method-abs-failure`）、非适配动量分配（`rem:appN-routing`）。CSS 1989 §10.1："there is as yet in the literature no complete and systematic subtraction procedure in QCD … even in the case of deeply inelastic scattering"。'''
COLLINS_UP = r'''- **解除途径：** grouped power counting under (Com)(Abs) at all orders; the fibered programme of `rem:appN-fibered-allorders` (F.1–F.4).'''

LCE_ENTRY = r'''
#### `asm:appN-lce` — 光锥序表示与协变值的等同（LCE） [\tagA]
- **所属：** App N §N.7 (fibered framework). Technical. New in v2.3 (X2 verification).
- **陈述：** For every graph $G$ of the scalar models (M1), (M2) that satisfies the hypotheses of `lem:appN-lc-positivity` and the infrared-finiteness condition (IRF) — its (renormalized) parametric integral converges absolutely for every $\varepsilon\in[0,\varepsilon_0]$ —, the fibered value equals the covariant value: $\int_B\rho_G\,d\mu_\varepsilon=I_G$ (condition (FI) of `def:appN-fibered`).
- **地位：** [A]：对每个检验了 (FR) 的图由 `lem:appN-identification` 证明；作为对所有图的陈述开放（光前微扰论与协变微扰论的等价）。
- **文献：** `Ligterink:1994tm`, `Schoonderwoerd:1998qj`, `Schoonderwoerd:1998iy` (equivalence of light-front and covariant perturbation theory).
- **被使用于：** %s (direct `\uses` users in FINAL_OUTLINE_v2, computed after the verify patch).
- **解除途径：** a general proof of (FI) for the scalar models.
- `\uses{def:appN-fibered, lem:appN-lc-positivity}`
''' % U('asm:appN-lce')

AREG_ENTRY = r'''
#### `asm:appN-analytic-reg` — 两圈图样积分的辅助解析正规化 [\tagA]
- **所属：** App N §N.7 (two-loop planar vertex). Technical. New in v2.3 (X2 verification).
- **陈述：** Two-loop planar vertex of (M1), each line raised to an independent power $1+\delta_l$. **(RA1)** the analytically regularized pattern integrals are meromorphic in $(\varepsilon,\delta)$; **(RA2)** the nine single-approximator integrals $\int T_R\Gamma$ are regular at $\delta=0$ for $\varepsilon$ in a punctured neighbourhood of 0, and their $\delta\to0$ limits are their dimensionally regularized values.
- **地位：** [A]：解析重整化对二次传播子证明了 (RA1)，但不覆盖程函型线性因子。
- **文献：** `Smirnov2002` (analytic regularization of Feynman integrals).
- **被使用于：** %s (direct `\uses` users in FINAL_OUTLINE_v2, computed after the verify patch).
- **解除途径：** meromorphy of analytically regularized integrals with linear (eikonal-type) factors.
- `\uses{prop:appN-twoloop-algebra}`
''' % U('asm:appN-analytic-reg')

LCOPT_STATUS = r'''- **地位：** 开放；光前文献中有部分结果（好分量流的零模不贡献；具体图中光前与协变微扰论的等价）；早先表述中的第 (iii) 项（割图规则的 Hermite 性）由 `lem:appJ-cut-hermiticity` 给出（v2.3 修正其陈述：最大时间圈规则下对每个实系数顶点、含鬼场顶点成立；逐顶点的"物理 $\mathcal M^*$"读法对鬼场不成立，只在对鬼圈两种走向求和后一致），不再是假设。无论 (ii) 的取值如何，它们都与所有负分量能量无关，故所有极点论证与之无关。'''
LCOPT_LIT = r'''- **文献：** `Kogut:1969xa`, `Chang:1973qi`, `Brodsky:1997de` (zero modes, Z-graphs), `Ligterink:1994tm` (equivalence; minus integrals), `Collins:2018aqt` (light-front vacuum), `Schoonderwoerd:1998qj`, `Schoonderwoerd:1998iy` (covariant vs light-front perturbation theory).'''

ENV_STMT_ADD = r''' **For coincident connections the bounds are imposed on side-summed families** (v2.3: within the class of `prop:appO-pergraph-weights` the per-graph version cannot hold; for graph-generated jets the per-graph question is open).'''
ENV_STATUS = r'''- **地位：** 开放；(GA3) 的纤维积分版本，必须处理其余变量中残留的夹挤；在任何阶都未证明；在 DIS 与 $e^+e^-$ 中不需要；对重合连接只能对按侧求和的族成立（`prop:appO-pergraph-weights`）。'''

MIX_ENTRY = r'''#### `asm:appO-mixing` — Glauber–软混合与重合连接的完整图集相消 [\tagA]
- **所属：** App O §O.6 (statement placed after `asm:appO-envelope`). Technical; Glauber specific.
- **陈述：** $\Gamma$ a DY forward graph, $R$ a leading region, windows as in `def:appO-windows`, $\hat\Phi_R$ as in `asm:appO-envelope`. **(a′)** (pre-integration localization with envelope bounds; replaces the earlier half-plane splitting clause (a), v2.3) localization is performed before the integration over the internal loops of $S$, pointwise outside the exceptional sets $E_j$ of `lem:appO-preintegration-localization`; assumed: envelope bounds $C\lambda^aL^K$ (i) for the $S$-loop integral of the absolute localization error, including the factor $\sum_\sigma|w_\sigma(p)|$ when there are several insertions, and (ii) for the unlocalized integrand on the $E_j$ — these bounds also justify the Fubini interchange; same for $J_B$. **(b)** (cut compatibility of $S$) after the localization of (a′) the cut sum of $J_A\otimes J_B\otimes S$ takes the closed-time-path form of `lem:appO-unitarity` with $S$'s fields as $\langle0|\bar{\rm T}\{\cdots\}{\rm T}\{\cdots\}|0\rangle$, and the $\tau=0$ insertions with both ends on spectators (also through $S$) assemble into operators on $\mathcal H_A\otimes\mathcal H_B\otimes\mathcal H_S$. **(c)** (complete graph set) for the set $\mathfrak G$ of all forward graphs of the given order with the given $J_A$, $J_B$ (closed under adding soft three- and four-gluon vertices between Glauber and soft lines, including real soft emission through Lipatov-type vertices), summed over all coincident connections and side assignments, combining the window with the adjacent near-on-shell soft region of $U_R$ (including real emission), the contribution after the integration map $\mathfrak P$ is $O(\lambda^aL^K)$ in the weak sense of `def:appO-weak-equivalence`; equivalently $\mathcal W'^\dagger\mathcal W=1+O(\lambda^a)$ on spectator states at $\tau=0$. (The per-graph fixed-order clause (c1) of the earlier formulation is deleted; joint localization is `lem:appO-joint-localization`.)
- **地位：** (a′)(b) 对 $\mathcal G_0$ 自动成立（只有连接线自身的极点；$S$ 为空）；(c) 在阿贝尔理论与只有非重合连接的阶成立（`prop:appO-ss-cancel`），对程函线之间的双胶子交换在 $O(g^4)$ 成立（`prop:dy-eikonal-twogluon`）；对复合旁观者，在全局两时模型中全重合 $O(g^4)$ 族的未割线部分逐点相消（`prop:appO-twoexch-spectator`，模型定理，作为 QCD 陈述为 [P]；槽位 X1f 部分完成）；被割的直接线（`rem:appO-cut-ss`）、共线端点处的半重合模式、$O(g^6)$（`prop:appO-g6-ladder`，直接线梯形图类在幺正性下不封闭）与重合 SA/AS 插入开放；槽位 X1a、X1b、X1e 未交付。证据（非证明）：Lindsay–Ross–Sachrajda 两圈旁观者相消、Brandt–Frenkel–Taylor 程函介子模型、Rothstein–Stewart 的正规化给出共同时序、Schwartz–Yan–Zhu（纯 Glauber 梯形图对单尺度可观测量相消）。
- **文献：** `CollinsSoperSterman1988`, `Collins2011` §14.3–§14.4 (outline), `AybatSterman2009`, `RothsteinStewart2016`, `Lindsay:1982pu`, `Lindsay:1983ny`, `Lindsay:1983dt`, `Brandt:1988xt`, `Schwartz:2018obd`, `Meggiolaro:1996hf`.
- **被使用于：** %s (direct `\uses` users in FINAL_OUTLINE_v2, computed after the verify patch).
- **解除途径：** an all-order unitarity argument for the complete graph set including the cut direct lines and the Lipatov-vertex graphs; the matching `asm:appO-collinear-ends` for the coincident $O(g^4)$ patterns.
- `\uses{def:appO-windows, def:appO-family, def:appO-weak-equivalence, asm:appO-envelope, lem:appO-unitarity, lem:appO-equal-time, lem:appO-preintegration-localization}`
''' % U('asm:appO-mixing')

DEF_C_OLD = '**(c)** on the soft-angle region and for the window-edge terms of `prop:appO-ss-cancel`(iv), (CS1)$_R$ and (CS2)$_R$ hold'
DEF_C_NEW = '**(c)** on the soft-angle region — including the out-of-window parts of the side-independent windows and the wee-line endpoint region of `lem:appO-side-independent-windows`(c); the window-edge terms themselves vanish identically (v2.3) —, (CS1)$_R$ and (CS2)$_R$ hold'
DEF_D_OLD = '(non-analytic ordering weights, `lem:appO-joint-localization`(a))'
DEF_D_NEW = '(ordering weights continuous but not analytic at $k^+=0$, `lem:appO-joint-localization`(d); the dominant region $|k^+_{\\rm SA}|\\sim\\lambda_B$, `rem:appO-h-emission`)'
DEF_STATUS = r'''- **地位：** (a) 对 $\mathcal G_0$ 与分级构型已证（`prop:appO-target`）；窗口边缘项在与侧无关的窗口下恒为零（`lem:appO-side-independent-windows`，槽位 X1c 通过）；开放：近壳携流线（两个相近软动量之差）导致 (GC2) 失效、(GC3) 失效、两类被排除的分量；**(b)(c)(d) 即使对阿贝尔 $\mathcal G_0$ 也需要**（槽位 X1d 未交付）——在截面层次 DY 的 Glauber 相消没有任何部分是无条件的。(c) 包括真正软尺度 $\lambda^2(1,1,1)$ 的旁观者耦合（领头幂次）与窗口外部分、wee 线端点区。'''
DEF_UP = r'''- **解除途径：** compatibility for $\mathcal G_0$ with a window-adapted set algebra; a soft-scale treatment of spectator couplings; a common treatment of H-emission endpoints and coincident SA/AS insertions (analyticity of the ordering weights in the dominant region).'''

NEWO_ENTRIES = r'''
#### `asm:appO-adjacent-swap` — 相邻交换对称性（ADJ） [\tagP]
- **所属：** App O §O.5 (model theorems). Technical. New in v2.3 (X1 verification).
- **陈述：** Every leading-power cut-summed LCOPT jet factor $J_X$ ($X=A,B$) of QCD graphs with two amplitude-side insertions on spectator partons satisfies (ADJ) of `def:appO-sectors`: two sectors of one jet that differ only by the order of two adjacent operations among (insertion 1, insertion 2, $V_H$) have their terms with a single-state gap between the two operations in bijection, with equal coefficients and equal other gap functions.
- **地位：** [P]：在标量旁观者模型（`ex:dy-spectator-lcopt`）中精确成立；对自旋求和的领头幂次 LCOPT 喷注只有论证，没有证明。只进入 App O 模型定理的 QCD 转移（这些定理作为 QCD 陈述为 [P]），不是 `thm:appO-main` 或 `thm:dy-factorization` 的前提。
- **文献：** — (formulated here; `verify/extend_reports/X1-glauber_final.md`).
- **被使用于：** %s (direct `\uses` users in FINAL_OUTLINE_v2, computed after the verify patch).
- **解除途径：** a proof for leading-power cut-summed LCOPT jets (numerator structure of `lem:appO-numerators`).
- `\uses{def:appO-sectors}`

#### `asm:appO-real-jets` — 旁观者喷注函数的实性（REAL） [\tagP]
- **所属：** App O §O.5 (model theorems). Technical. New in v2.3 (X1 verification).
- **陈述：** (REAL) of `def:appO-sectors` holds for the leading-power cut-summed LCOPT jet factors of QCD graphs with spectator insertions: every colour-stripped jet function is a fixed phase times a rational function with real coefficients.
- **地位：** [P]：在标量旁观者模型中精确成立；对自旋求和的 QCD 喷注只有论证；只进入模型定理的 QCD 转移。
- **文献：** — (formulated here; `verify/extend_reports/X1-glauber_final.md`).
- **被使用于：** %s (direct `\uses` users in FINAL_OUTLINE_v2, computed after the verify patch).
- **解除途径：** a proof for leading-power cut-summed LCOPT jets.
- `\uses{def:appO-sectors}`

#### `asm:appO-collinear-ends` — 共线端点的匹配 [\tagA]
- **所属：** App O §O.5 (model theorems). Technical; Glauber specific. New in v2.3 (X1 verification).
- **陈述：** The SS windows carry the two-sided analytic rapidity regulators of `def:appO-regulator-class`(c); the complements — the $A$-collinear end ($|k^+|\gtrsim K^+$) and the $B$-collinear end ($|k^-|\gtrsim K^-$), together with the cut contributions located there — are assigned to the collinear regions, where collinear factorization (Wilson lines and subtraction terms) reproduces them with no leftover Hermitian $C_AX$ term (fully coincident pattern) and no leftover $[X_1,X_2]$ term (half-coincident pattern).
- **地位：** 开放，[A]：它把 `asm:appO-mixing`(c) 对重合 $O(g^4)$ 模式的内容**转移**而非消去；半重合部分在模型中只用 $k^-$ 正规子即已证明（`prop:appO-halfcoinc-sensitivity`）；被割的直接线贡献在共线端点处未被计算（`rem:appO-cut-ss`）。不是 `thm:appO-main` 或 `thm:dy-factorization` 的前提；`Zhou:2017his` 可读作其 EFT 形式（我们不接受其关键步骤为证明）。
- **文献：** `Zhou:2017his`, `Liu:2008cc`, `RothsteinStewart2016`, `Collins2011` §14.4.
- **被使用于：** %s (direct `\uses` users in FINAL_OUTLINE_v2, computed after the verify patch).
- **解除途径：** compute the cut direct-line contributions at the collinear ends or prove their suppression with the two-sided regulators (`rem:appO-cut-ss`); then the matching itself.
- `\uses{def:appO-regulator-class, def:appO-glob-model}`
''' % (U('asm:appO-adjacent-swap'), U('asm:appO-real-jets'), U('asm:appO-collinear-ends'))

INNER_ROWS_OLD = '| `asm:appM-brst-ope` | (B1)(B2) | binding |'
INNER_ROWS_NEW = '| `asm:appM-brst-ope` | (B2) ≡ (Eε) | v2.3: (B1) retired (the name is not reused); (B2) renamed (Eε) in App M |\n| `asm:appM-oswi` | — | v2.3 |'
INNER_MIX_OLD = '| `asm:appO-mixing` | (a)(b)(c) | (c1) deleted |'
INNER_MIX_NEW = '| `asm:appO-mixing` | (a′)(b)(c) | (c1) deleted; (a) replaced by (a′) in v2.3 |\n| `asm:appO-adjacent-swap`, `asm:appO-real-jets` | (ADJ), (REAL) | v2.3; the names belong to `def:appO-sectors` together with (SEC), (EQ) |\n| `asm:appO-collinear-ends` | — | v2.3 |\n| `asm:appN-lce`, `asm:appN-analytic-reg` | (LCE); (RA1)(RA2) | v2.3 |'
INNER_OTHER_ADD = ' **v2.3 local names** (not assumptions; clash-free): (Pr1)–(Pr5), (NE) (`def:appM-blocks`, `lem:appM-ne`), (CTp) (`rem:appM-remainder-reduction`), (A1)–(A4) (`prop:dis-ope-euclid`), (FR), (FI) (`def:appN-fibered`), (IL1)–(IL3), (IRF), (COV) (App N fibered framework), (M1), (M2) (App N scalar models), (SEC), (EQ) (`def:appO-sectors`), F.1–F.4 (`rem:appN-fibered-allorders`).'

S52_ADD = r'''- `asm:appO-adjacent-swap`, `asm:appO-real-jets` [P] (v2.3) → only the App O model theorems `prop:appO-twoexch-spectator`, `prop:appO-pergraph-weights`, `prop:appO-halfcoinc-sensitivity` (all [P]); no [A] statement uses them.
'''

CHANGELOG = r'''

**2026-10-11 — revision v2.3 (spec patcher, verify patch).**
1. Six new entries (§3.2–§3.4): `asm:appM-oswi`, `asm:appN-lce`, `asm:appN-analytic-reg`, `asm:appO-collinear-ends` (`\tagA`), `asm:appO-adjacent-swap`, `asm:appO-real-jets` (`\tagP`); totals 29 `\tagA`, 3 `\tagP`, 14 `\tagC` (6 global), 1 untagged = 47.
2. Rewordings after X1–X3: `asm:appM-brst-ope` ((B1) retired, (B2) ≡ (Eε); new title), `asm:appO-mixing` ((a) → (a′), status), `asm:appO-envelope` (side-summed families for coincident connections), `asm:appO-deformation` ((c), (d), status); status and upgrade fields of `asm:appM-remainder`, `asm:appM-forward`, `asm:appN-collins`, `asm:appO-lcopt` updated (slot outcomes of FINAL_OUTLINE_v2 §00.4); 「文献待补」 replaced by `Bergere:1977wz`, `Schoonderwoerd:1998qj`, `Schoonderwoerd:1998iy`.
3. §1 regenerated (identical to FINAL_OUTLINE_v2 §08 `### Assumptions`; the seven rows whose math cells were broken by unescaped `|` rebuilt with `\vert`; users recomputed); every 「被使用于」 field recomputed from the final `\uses` data; §00.2, §00.3 item 5, §4, §5.2 updated. Lead-author confirmation requested (FINAL_OUTLINE_v2 MD19).'''

OPS = [
 ('sub', STATUS_OLD, STATUS_NEW, STATUS_OLD),
 ('sub', '§1 the summary table (41 entries)', '§1 the summary table (47 entries)', '**What this file contains.**'),
 ('sub', 'all `asm:appO-*`; `asm:lamet-aux-renorm`', 'all `asm:appO-*` except `asm:appO-adjacent-swap`, `asm:appO-real-jets`; `asm:lamet-aux-renorm`', '| `\\tagA` | the assumed claim is covered'),
 ('sub', '| `asm:yzliu-lightcone-uniform` |', '| `asm:yzliu-lightcone-uniform`; `asm:appO-adjacent-swap`, `asm:appO-real-jets` (v2.3: proven in the scalar spectator model, argued for QCD jets; they enter only the QCD transfer of the App O model theorems, which are [P]) |', '| `\\tagP` | proven only in special cases'),
 ('rep', A(36) + '\n', A(36) + '\n5. **Verify patch v2.3 (2026-10-11).** Six new entries (`asm:appM-oswi`, `asm:appN-lce`, `asm:appN-analytic-reg`, `asm:appO-adjacent-swap`, `asm:appO-real-jets`, `asm:appO-collinear-ends`); `asm:appM-brst-ope`: (B1) retired, (B2) ≡ (Eε); `asm:appO-mixing`: (a) replaced by (a′) (pre-integration localization, `lem:appO-preintegration-localization`); `asm:appO-envelope`: imposed on side-summed families for coincident connections; `asm:appO-deformation`(c)(d) reworded (window-edge terms vanish with side-independent windows). No tag of an existing entry changed. Lead-author confirmation requested (FINAL_OUTLINE_v2 MD19).\n'),
 # --- §3.2
 ('rep', A(159) + '\n' + A(160) + '\n', REMAINDER_STATUS + '\n' + REMAINDER_LIT + '\n'),
 ('rep', A(162) + '\n', REMAINDER_UP + '\n'),
 ('range', '#### `asm:appM-brst-ope` — OPE 的 BRST 对称插入 [\\tagA]\n', '#### `asm:appM-forward` —', BRST_ENTRY + '\n', False),
 ('rep', A(177) + '\n', FORWARD_STATUS + '\n'),
 ('rep', A(180) + '\n' + A(181) + '\n', FORWARD_UP + '\n' + A(181) + '\n' + OSWI_ENTRY),
 # --- §3.3
 ('rep', A(215) + '\n', COLLINS_STATUS + '\n'),
 ('rep', A(218) + '\n', COLLINS_UP + '\n'),
 ('rep', A(300) + '\n', A(300) + '\n' + LCE_ENTRY + AREG_ENTRY),
 # --- §3.4
 ('rep', A(307) + '\n' + A(308) + '\n', LCOPT_STATUS + '\n' + LCOPT_LIT + '\n'),
 ('sub', '$\\int\\hat\\Phi_R\\le C\\lambda^aL^K$.', '$\\int\\hat\\Phi_R\\le C\\lambda^aL^K$.' + ENV_STMT_ADD, '- **陈述：** For each leading region $R$ there is $\\hat\\Phi_R\\ge0$ on $U_R$'),
 ('rep', A(316) + '\n', ENV_STATUS + '\n'),
 ('range', '#### `asm:appO-mixing` — Glauber–软混合与重合连接的完整图集相消 [\\tagA]\n', '#### `asm:appO-deformation` —', MIX_ENTRY + '\n', False),
 ('sub', DEF_C_OLD, DEF_C_NEW, '- **陈述：** For any $\\Gamma$, $R$, $F=\\tilde F_{\\Gamma,R}$:'),
 ('sub', DEF_D_OLD, DEF_D_NEW, '- **陈述：** For any $\\Gamma$, $R$, $F=\\tilde F_{\\Gamma,R}$:'),
 ('rep', A(334) + '\n', DEF_STATUS + '\n'),
 ('rep', A(337) + '\n' + A(338) + '\n', DEF_UP + '\n' + '- `\\uses{def:appO-target, def:appO-rewriting, def:appO-graded, prop:appO-ss-cancel, lem:appO-side-independent-windows}`\n'),
 ('rep', A(347) + '\n', A(347) + '\n' + NEWO_ENTRIES),
 # --- §4, §5.2
 ('rep', INNER_ROWS_OLD + '\n', INNER_ROWS_NEW + '\n'),
 ('rep', INNER_MIX_OLD + '\n', INNER_MIX_NEW + '\n'),
 ('sub', 'MA0–MA4 (umbrella names).', 'MA0–MA4 (umbrella names).' + INNER_OTHER_ADD, 'Other scoped names (not assumptions):'),
 ('rep', '- `asm:yzliu-lightcone-uniform` [P] → `prop:yzliu-universality-classes` [P] (consistent).\n', '- `asm:yzliu-lightcone-uniform` [P] → `prop:yzliu-universality-classes` [P] (consistent).\n' + S52_ADD),
 # --- §1 regenerated, users recomputed
 ('func', lambda t: _regen_table(t)),
 ('func', lambda t: regtable.update_users(t, USERS)[0]),
 ('rep', '4. §5.3 marked resolved; §8 records the provisional merge decisions.', '4. §5.3 marked resolved; §8 records the provisional merge decisions.' + CHANGELOG),
]

def _regen_table(t):
    table, total, rows = regtable.build(OUTLINE)
    lines = t.split('\n')
    h = next(i for i, l in enumerate(lines) if l.strip() == '### Assumptions')
    a = next(i for i in range(h, len(lines)) if lines[i].startswith('| label | owner |'))
    b = a
    while b < len(lines) and lines[b].startswith('|'):
        b += 1
    lines[a:b] = table.split('\n')
    tl = next(i for i in range(a, len(lines)) if lines[i].startswith('Total:'))
    lines[tl] = total + ' (Identical to FINAL_OUTLINE_v2 §08 `### Assumptions`; "used by" = direct `\\uses` users computed from FINAL_OUTLINE_v2 after the verify patch v2.3.)'
    return '\n'.join(lines)
