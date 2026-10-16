# ASSUMPTIONS — 全书编号假设登记表 / The global assumption register (spec v2)

**Status (revision v2.3, verify patch of 2026-10-11; merged revision v2.2).** v2.3 applies the outcomes of the verification workflow (`verify/CLAIM_VERDICTS.md`; proof extensions X1–X3, `verify/extend_reports/`): six new entries (`asm:appM-oswi`, `asm:appN-lce`, `asm:appN-analytic-reg`, `asm:appO-adjacent-swap`, `asm:appO-real-jets`, `asm:appO-collinear-ends`), the rewordings of `asm:appM-brst-ope`, `asm:appO-mixing`, `asm:appO-envelope`, `asm:appO-deformation`, the status and upgrade fields of the entries touched by X1–X3, and §1 regenerated (47 entries; FINAL_OUTLINE_v2 decision MD19). Earlier status: This register was merged with `FINAL_OUTLINE_v2.md` by the spec-v2 integrator (2026-10-10): §1 is identical to the `### Assumptions` table of FINAL_OUTLINE_v2 §08 (users computed from the final `\uses` data); the **binding texts** are the owners' entries (merge decision MD18): Ch1 entries of FINAL_OUTLINE_v2 for `asm:intro-*` (reproduced in §3.1), the entries below for App M/N/O (§3.2–§3.4, together with the App M/N/O entries of FINAL_OUTLINE_v2), and the Part VII annex §F1 of FINAL_OUTLINE_v2 for the frontier entries (reproduced verbatim in §3.5–§3.7). Merge decisions affecting this file: MD1 (`asm:appN-brst-nonlocal` → `\tagC`, named gap), MD2 ((Z2) split kept), MD3 (technical App M/N/O entries `\tagA`), MD13 (`asm:front-scet-modes` stays with Ch24), MD15 (inner names), MD18. Original status line of the draft: binding spec-v2 register of every numbered assumption (`assumption` environment, `asm:` label) of 《QCD 因子化定理：严格证明、全阶论证与适用边界》, drafted 2026-10-10 by the spec-v2 new-appendices drafter. Companion of `spec_v2/OUTLINE_appMNOPQ.md`; merged by the synthesizer into `FINAL_OUTLINE_v2.md` (§1 below is the `### Assumptions` registry block). Ch1 prints the short register `tab:intro-assumptions` from §1; App P prints the generated register `tab:appP-register` from the `assumption` environments and checks it against this file (check C-P10).

**Sources.** `refdoc/REFDOC_ANALYSIS.md` §5.2–§5.3 (the 25-entry register, S5–S8), §2 (ERR-M25, M27–M29, S3); `spec_v2/WRITER_SPEC_v2.md` §4.3–§4.9 (v2.1: tag mapping of assumptions, grade propagation, inner item names), §5.6 (definition ownership); `research/critic/REVIEW.md` §12 (MA0–MA4); the frontier reports `frontier/lamet/LAMET.md`, `frontier/yzliu/YZLIU.md`, `frontier/others/OTHERS.md` (§8.3: multilocal BRST classification); `spec_v2/OUTLINE_appMNOPQ.md` (App M/N/O entries, users); the working drafts of the core outline (Ch1–Ch21, Ch25) and of the frontier outline (Ch22–Ch24) as of 2026-10-10 18:30, from which the users of the global and frontier entries and the names and tags of the 14 frontier entries are taken (the owner outlines govern the wording of their entries; this register copies the summary).

**What this file contains.** §00 rules and decisions; §1 the summary table (47 entries); §2 the MA0–MA4 dictionary; §3 the full entries, grouped by owner (statement with inner items, status, literature, users, upgrade path, `\uses`); §4 inner item names and renames; §5 grade-propagation consequences (bottlenecks of the main theorems; [C]/[P] entries and their users; inconsistencies found in the working drafts); §6 hypotheses deliberately **not** registered; §7 changes relative to the 25-entry register of REFDOC §5.3; §8 open decisions for the lead author; CHANGELOG.

---------------------------------------------------------------------------------------------------

## 00. Rules

### 00.1 What is registered and how it is written

1. **Registered** are exactly the hypotheses that act as formal premises of statements of the book (premises in an $R_{\rm cond}$ premise sentence, or hypotheses shared by several statements) and are not proven in the book. Local hypothesis lists inside one statement (e.g. (CS1)–(CS3) as hypotheses of `thm:appN-subtraction`, (Com)(Abs) of `prop:method-product`, (ET1)(ET2) of `lem:appO-equal-time`) and the weakest *step* of an [A] proof sketch are not registered (§6).
2. **Owner and label.** Each entry is owned by one unit; the key in the label is the owner's key (`asm:intro-*` Ch1; `asm:appM-*`, `asm:appN-*`, `asm:appO-*`; `asm:lamet-*` Ch22; `asm:yzliu-*` Ch23; `asm:front-*` Ch24). Only the owner states it; other units cite it (`\cref`, `\uses`) and may paraphrase it in one sentence (WRITER_SPEC_v2 §4.4 item 5).
3. **Environment** (WRITER_SPEC_v2 §4.4 item 3): `\begin{assumption}[<中文标题> \tag?]\label{asm:…}`; body fields in this order: statement (precise, with formulas, inner items); 「地位：」; 「文献：」; 「被使用于：」 (reverse dependencies, copied from this register; never in the assumption's own `\uses`); 「解除途径：」; last line `\uses{…}` (definitions it refers to, and earlier assumptions whose objects it uses) or `% uses: none` — never an empty `\uses{}`.
4. **Global vs technical** (WRITER_SPEC_v2 §4.4 item 7). The six `asm:intro-*` entries are *global non-perturbative* assumptions: they appear in the 「非微扰地位：」 line of hadron-level statements and as premises of explicitly non-perturbative $R_{\rm cond}$ theorems, and they do not lower the (perturbative) tags of ordinary statements. All other entries are *technical* and enter the grade propagation (WRITER_SPEC_v2 §4.6).

### 00.2 Tag policy (WRITER_SPEC_v2 §4.4 item 2, spec v2.1)

| tag | criterion for an assumption | entries |
|---|---|---|
| `\tagA` | the assumed claim is covered by an all-order argument of the literature (CSS, Bodwin, Collins 2011, Sterman; OPE literature), although not proven as the precise statement given here | all `asm:appM-*`; all `asm:appN-*` except `asm:appN-values`, `asm:appN-ir-regulator` and `asm:appN-brst-nonlocal`; all `asm:appO-*` except `asm:appO-adjacent-swap`, `asm:appO-real-jets`; `asm:lamet-aux-renorm`, `asm:lamet-ope`, `asm:lamet-staple`, `asm:lamet-soft-rapidity`, `asm:lamet-order-limits`; `asm:yzliu-wightman-pt`; `asm:front-scet-modes` |
| `\tagP` | proven only in special cases, at finite order or in models; no all-order argument for the general claim | `asm:yzliu-lightcone-uniform`; `asm:appO-adjacent-swap`, `asm:appO-real-jets` (v2.3: proven in the scalar spectator model, argued for QCD jets; they enter only the QCD transfer of the App O model theorems, which are [P]) |
| `\tagC` | no all-order argument exists | the six `asm:intro-*` (global; excluded from propagation for ordinary statements); `asm:appN-ir-regulator`; `asm:appN-brst-nonlocal` (MD1: a **named gap** — premise only of `thm:appN-structure`; named, not used, by the chapter [A] statements whose literature grade contains it); `asm:lamet-uniform`, `asm:lamet-twist4`, `asm:lamet-large-z`, `asm:lamet-gap`; `asm:yzliu-heavy-pair`; `asm:front-mor-complete` |
| no tag | a convention or a choice | `asm:appN-values` |

The word "open" in a status field means "not proven as stated" and is compatible with `\tagA`. A `\tagC` technical entry is never a premise of an [A] statement (checked on FINAL_OUTLINE_v2 by `checks/check_final_outline_v2.py`, E6). **Named gaps** (MD1; WRITER_SPEC_v2 v2.2 §4.6 item 6): a `\tagC` entry that formalizes an explicitly assumed step of the standard literature argument is named in the 「地位与缺口」 paragraphs of the [A] statements whose literature grade contains that step, without being their `\uses` premise.

### 00.3 Decisions taken in this register (relative to REFDOC §5.3)

1. **(Z2) split off** as `asm:appN-ir-regulator` (`\tagC`: no on-shell gluon regulator preserving the Ward identities is known). It is used only by the regulator route `thm:disall-renorm-compat` (content grade [C]); the [A] process theorems use the DR route `asm:appN-multren`(Z1)(Z3), where (Z3)(ii) states DR mass factorization (finite $\hat{\mathsf H}^{\rm bare}Z$), verified at fixed orders.
2. **New entry `asm:appN-brst-nonlocal`** (`\tagA`): the BRST classification of the multilocal light-ray operators that Collins 2011 §11.3.2 assumes. **Lead-author decision required**: frontier/others §8.3 assesses the general multilocal case as [C]; with `\tagC` the grade propagation would force `lem:method-ward-multi` and every process theorem to [C], contrary to the binding master-table tags. The entry makes explicit what the [A] tag of `lem:method-ward-multi` already contains. **Resolved at the merge (MD1):** tag `\tagC` (no all-order argument exists; same claim as `conj:front-brst-multilocal` [C]); premise only of `thm:appN-structure` (content grade [C]); a named gap of `lem:method-ward-multi`, `thm:method-template` and the Feynman-gauge process theorems (named in their status paragraphs, not a `\uses` premise). The lead author may instead make it a premise (all these statements become [C]).
3. **`asm:appO-mixing`(c1) deleted** (a fixed localization order is false per graph); replaced by `lem:appO-joint-localization`; its consequence (non-analytic ordering weights for coincident SA/AS insertions) added to `asm:appO-deformation`(d).
4. **Frontier entries**: the 14 names, tags and inner item names of the frontier outline (working draft) are adopted (no clash with the core and appendix names). The candidate names considered earlier from the frontier reports (a separate decay assumption, a quasi-TMD power-counting assumption, a rapidity IR-control assumption, a Jantzen-regions assumption) are **not** registered: the decay theorem uses `asm:lamet-gap`; (QT1)–(QT7) and the Jantzen conditions are local lists; Liu's assumed IR-control step is the named weakest step of an [A] sketch (§6).
5. **Verify patch v2.3 (2026-10-11).** Six new entries (`asm:appM-oswi`, `asm:appN-lce`, `asm:appN-analytic-reg`, `asm:appO-adjacent-swap`, `asm:appO-real-jets`, `asm:appO-collinear-ends`); `asm:appM-brst-ope`: (B1) retired, (B2) ≡ (Eε); `asm:appO-mixing`: (a) replaced by (a′) (pre-integration localization, `lem:appO-preintegration-localization`); `asm:appO-envelope`: imposed on side-summed families for coincident connections; `asm:appO-deformation`(c)(d) reworded (window-edge terms vanish with side-independent windows). No tag of an existing entry changed. Lead-author confirmation requested (FINAL_OUTLINE_v2 MD19).

---------------------------------------------------------------------------------------------------

## 1. Summary table

### Assumptions

| label | owner | tag | 中文标题 | content (one line) | status | used by (direct, computed) | upgrade path |
|---|---|---|---|---|---|---|---|
| `asm:intro-wightman` | Ch1 | [C] | QCD 的 Wightman 结构 | (W1) Wightman QCD with gauge-invariant composites, conserved Hermitian $j^\mu$, parity; (W2) spectral condition in the superselection sector of the target's flavour numbers, isolated mass shell for Haag–Ruelle states, massive light quarks; (W3) tempered forward matrix elements; (W4) covariant retarded extension, $q_\mu\tilde R^{\mu\nu}=0$ | open (4D QCD not constructed) | `asm:intro-composite`, `asm:intro-np-ope`, `asm:intro-growth`, `def:intro-MA`, `prop:prelim-optical`, `prop:ee-R-ImPi`, `prop:ee-analytic`, `prop:ee-smearing`, `prop:dis-W-structure`, `prop:dis-ope-rg`, `prop:dis-dispersion-np`, `thm:dis-fixed-n`, `thm:dis-moments-np`, `cor:dis-weak-xspace`, `thm:dis-moments`, `prop:dis-twist4`, `prop:dis-tmc`, `thm:dis-bjorken`, `prop:pdf-invariance`, `prop:pdf-support-hadron`, `thm:pdf-moments-local`, `thm:pdf-dis-xspace`, `prop:pdf-sum-rules`, `prop:pdf-timelike-dglap`, `prop:coll-photon-sf`, `prop:coll-luxqed`, `thm:coll-g1-moments`, `prop:coll-transversity-evolution`, `thm:tmd-sivers-sign`, `prop:excl-erbl`, `prop:excl-polynomiality`, `thm:heavy-inclusive-b`, `thm:lamet-exp-decay`, `lem:appM-forward-tube`, `lem:appM-positivity` | construct QCD; or prove (W1)–(W4) for the continuum limit of lattice QCD |
| `asm:intro-composite` | Ch1 | [C] | 规范不变复合算符与光线算符的存在与重整化群 | gauge-invariant composite families graded by dimension; twist 2 = $O_q^{(n)},O_g^{(n)}$; operator RG with triangular mixing; $\beta,\gamma$ asymptotic to PT; light-ray operators exist between hadron states with moments $A_i^{(n)}$ | open | `asm:intro-np-ope`, `def:intro-MA`, `prop:dis-ope-rg`, `thm:dis-moments-np`, `cor:dis-weak-xspace`, `thm:dis-moments`, `prop:dis-twist4`, `prop:dis-tmc`, `thm:dis-bjorken`, `prop:pdf-invariance`, `prop:pdf-support-hadron`, `thm:pdf-moments-local`, `thm:pdf-dglap`, `thm:pdf-dis-xspace`, `prop:pdf-sum-rules`, `prop:pdf-timelike-dglap`, `prop:coll-photon-sf`, `prop:coll-luxqed`, `thm:coll-g1-moments`, `prop:coll-transversity-evolution`, `prop:tmd-small-b`, `thm:tmd-sivers-sign`, `prop:excl-erbl`, `prop:excl-polynomiality`, `thm:heavy-inclusive-b`, `lem:appM-norm-bound` | as above |
| `asm:intro-np-ope` | Ch1 | [C] | 非微扰算符乘积展开 | (O1) direction-uniform Euclidean OPE to every finite level $N$ between the vacuum and hadron states, remainder $O(\vert q\vert^{2-N-\delta}\ln^k\vert q\vert)$ with bounds on all $q$-derivatives, Lorentz-covariant coefficients; (O2) odd-twist coefficients $\propto m_q/\vert q\vert$ | open, widely assumed; vacuum part `conj:ee-np-ope` [C]; asymptotic only (renormalons, instantons) | `asm:intro-af-coeff`, `def:intro-MA`, `lem:dis-ope-segment`, `thm:dis-fixed-n`, `thm:dis-moments-np`, `cor:dis-weak-xspace`, `thm:dis-moments`, `prop:dis-twist4`, `prop:dis-tmc`, `thm:dis-bjorken`, `thm:pdf-dis-xspace`, `prop:coll-photon-sf`, `thm:coll-g1-moments` | a non-perturbative definition of the OPE (OP-A3) |
| `asm:intro-af-coeff` | Ch1 | [C] | 系数的渐近自由行为 | at $\mu=\vert q\vert$ the OPE coefficients are asymptotic to their $\overline{\rm MS}$ series: $\tilde C_i(q;\vert q\vert)=\vert q\vert^{2-d_i}[\sum_{k\le K}c_{i,k}(\hat q)\alpha_s(\vert q\vert)^k+O(\alpha_s^{K+1})]$; light-quark masses as higher-dimension terms | open; compatible with renormalons and instantons | `def:intro-MA`, `thm:dis-moments-np`, `cor:dis-weak-xspace`, `thm:dis-moments`, `prop:dis-twist4`, `prop:dis-tmc`, `thm:dis-bjorken`, `thm:pdf-dis-xspace`, `prop:coll-photon-sf`, `thm:coll-g1-moments`, `thm:heavy-inclusive-b`, `lem:appM-norm-bound` | as for `asm:intro-np-ope` (OP-A3) |
| `asm:intro-growth` | Ch1 | [C] | 前向振幅的增长条件 | $\lim_{y\to\infty}T_2(iy,Q^2)/(iy)=0$ | open; ⇔ low-moment sum rules incl. momentum sum rule (`prop:dis-low-moments`); true at computed orders | `def:intro-MA`, `thm:dis-moments-np`, `thm:dis-moments`, `thm:dis-bjorken`, `thm:pdf-dis-xspace` | non-perturbative proof or fixed-pole counterexample |
| `asm:intro-bridge` | Ch1 | [C] | 从部分子微扰论到强子的桥接假设 | partonic leading regions are the only hadronic leading regions; all $\Lambda$-sensitivity in hadronic matrix elements of the same operators; remainder $O((\Lambda/Q)^p)$ asymptotically | open (= MA1 + MA2, asymptotic part of MA4) | `def:intro-MA`, `thm:method-template`, `thm:disall-factorization`, `thm:disall-heavy`, `prop:disall-nuclear`, `thm:coll-sia`, `thm:coll-sidis`, `thm:coll-direct-photo`, `thm:dy-factorization`, `thm:dy-colour-singlet`, `thm:dy-polarized`, `thm:dy-higher-twist`, `thm:tmd-factorization`, `prop:tmd-small-b`, `cor:tmd-sivers-observable`, `prop:tmd-collins-universality`, `thm:scet-thrust`, `thm:jets-ngl-factorization`, `thm:break-ddis`, `thm:break-double-dy`, `thm:excl-pion-ff`, `thm:excl-transition`, `thm:excl-dvcs`, `thm:excl-meson-L`, `thm:heavy-bdpi`, `prop:heavy-btopi-ff`, `prop:heavy-qcdf-lp`, `thm:heavy-inclusive-b`, `thm:heavy-nrqcd-decay`, `prop:heavy-quarkonium-fragmentation`, `prop:power-dis-twist4-x` | non-perturbative control; solvable models |
| `asm:appM-remainder` | AppM | [A] | 冻结 $q$ 双局域正规乘积的动量空间余项估计 | massive Euclidean model, each order: every $h\in\mathcal H_{a,\Gamma}$ (derivatives, multiplications by $p$ and $m\partial_m$ of the frozen-$q$ normal product $\tilde N_{a,\Gamma}$) obeys $\vert h\vert\le K_h\vert q\vert^{D-1-a}(\ln\vert q\vert)^k$, uniformly in $q/\vert q\vert$ | open in the stated form; reduced to the zero-momentum matching estimate (CTp), `rem:appM-remainder-reduction` (slot X3a not delivered: the uniqueness route is circular) | `thm:appM-scaling`, `cor:appM-coordinate` | prove (CTp) by sector estimates, or a momentum-space OPE theorem whose scope is verified |
| `asm:appM-forward` | AppM | [A] | 前向在壳无质量部分子矩阵元的 OPE 余项 | massless QCD, DR, on-shell parton target: $T^{\mu\nu}_j-\sum_{d_O\le N}\tilde C^{\mu\nu}_O\langle p\vert[O]\vert p\rangle=O(\vert q\vert^{1-N}\ln^k\vert q\vert)$ at each order, uniformly in the Euclidean direction | open; per graph the forward expansion is proved (`thm:appM-forward-expansion`); `cor:appM-forward-ope` reduces it to (A3), (Eε), the Joglekar–Lee triangularity and `asm:appM-oswi`; one loop exact in $\varepsilon$ for $N\le8$ (VF-DIS-13) | `prop:dis-ope-forward` | discharge the inputs of `cor:appM-forward-ope` (OP-A5) |
| `asm:appM-brst-ope` | AppM | [A] | OPE 的 BRST 结构：带一个复合旁观者的欧氏展开 (Eε) | (B2) ≡ (Eε): in bare DR at generic $\varepsilon$, the large-$q$ expansion with one composite spectator $Z=s\phi$ holds with the coefficients of the expansion without $Z$ plus merged coefficients $C^Z_{O'}$ polynomial in $p_Z$; (B1) retired | open; slot X3d partial: the reduction to gauge-invariant operators is proved under (Eε) (`thm:appM-brst-reduction`); Joglekar read at abstract level, Hollands' QCD scope not verified | `prop:dis-ope-gi`, `thm:appM-brst-reduction` | prove (Eε) (graph-by-graph DR expansion with one composite spectator) |
| `asm:appM-oswi` | AppM | [A] | 前向在壳胶子振幅的 Ward 恒等式 | $p^aM_{ab}\varepsilon^b=0=\varepsilon^aM_{ab}p^b$ for the amputated forward on-shell gluon Compton amplitude at each order in DR, for all $\varepsilon\cdot p=0$ (incl. $\varepsilon=p$); equivalently $p^aM_{ab}\propto p_b$ | [A] (BRST Ward identity of the forward amplitude; the zero-momentum subtleties of `rem:appM-forward-aliens` are the reason it is stated separately) | `lem:appM-gluon-regularity` | a proof of the forward on-shell Ward identity at all orders |
| `asm:appN-contour` | AppN | [A] | (GA1) 围道 | contour $\Omega$ homotopic to real space crossing no singularity of $\Gamma$ or any $C_R\Gamma$; each $\int_\Omega C_R\Gamma$ meromorphic near $\varepsilon=0$ | open in general; holds when all poles are one-sided (`lem:method-i0-compat`); DY: one-sided form from App O | `cor:method-removing-eps`, `thm:method-subtraction`, `prop:disall-two-routes`, `thm:disall-renorm-compat`, `thm:appN-subtraction`, `prop:appN-sia`, `thm:appN-structure` | general deformation theorem (Collins 2020 geometry + Glauber, Ch24) |
| `asm:appN-envelope` | AppN | [A] | (GA3) 幂次计数包络 | envelopes $\Phi_{R_0}$ on $U_{R_0}$ with $\int\Phi_{R_0}\le CL^K$ dominating every partially approximated integrand; uniform integrability at $\Vert k\Vert\ge1$; pointwise boost bound $\vert f_i-T_{R_0}f_i\vert\le C(s_{R_0}/t_{R_0})g_i$ | open (never written in integral form at all orders); fibered version for the scalar models (`thm:appN-fibered-subtraction`) | `lem:method-local-accuracy`, `thm:method-template`, `prop:disall-two-routes`, `thm:disall-factorization`, `rem:appE-actual-bound`, `lem:appN-error-table`, `prop:appN-sia`, `thm:appN-structure`, `prop:appO-one-sided`, `thm:appO-main`, `cor:appO-interface`, `prop:appO-tmd` | an integral version of the Sterman–Collins power counting (sector decomposition per region) |
| `asm:appN-separation` | AppN | [A] | (GA4) 分离性 | virtuality $\ge c\,t_R^2$ on $\mathsf H_R$ lines; $\vert l^+\vert\ge c\,t_R$ on jet lines changed by $T_R$; for soft momenta $\vert k^+k^-\vert\ge c\,\mathbf k_T^2$ and $\vert\tilde D\vert\ge c(\vert p^+\vert\vert k^-\vert+v_A(p))$ | open in general; verified in the one-loop triangle; the exponent 2 in (i) is an independent (Łojasiewicz-type) assumption | `lem:method-local-accuracy`, `thm:method-template`, `prop:disall-two-routes`, `thm:disall-factorization`, `lem:appN-error-table`, `prop:appN-sia`, `prop:appN-tmd-window`, `thm:appN-structure`, `prop:appO-one-sided`, `thm:appO-main`, `cor:appO-interface`, `prop:appO-tmd` | Łojasiewicz inequalities for the Landau varieties of leading regions plus a deformation theorem (App O for the Glauber part) |
| `asm:appN-lce` | AppN | [A] | 光锥序表示与协变值的等同（LCE） | for graphs of the scalar models (M1), (M2) satisfying the hypotheses of `lem:appN-lc-positivity` and (IRF), the fibered value equals the covariant value, $\int_B\rho_G\,d\mu_\varepsilon=I_G$ | [A]: proved for each graph by `lem:appN-identification` once (FR) is checked; open as a statement for all graphs | `cor:appN-cs3-fibered` | a general proof of (FI) for the scalar models (light-front perturbation theory) |
| `asm:appN-values` | AppN | — | 发散链项的取值规则 | linear value rule for divergent chain terms compatible with the convergent subtraction terms (V1); scaleless = 0 (V2) | convention; verified in the triangle | `thm:method-template`, `prop:appN-thrust-zerobin`, `prop:appN-thrust`, `thm:appN-structure`, `prop:appN-triangle-exact`, `prop:appN-twoloop-remainder` | — (convention) |
| `asm:appN-collins` | AppN | [A] | 一般图的 Collins 条件 | (CS1)–(CS3) for every leading-power integrand of the process, incl. multi-direction processes and non-adapted routing | [A]-level (Collins 2011 ch. 10); complete for the one-loop off-shell triangle (`prop:appN-triangle-cs`, slot X2a); fibered framework `thm:appN-fibered-subtraction`; slots X2b, X2c not delivered | `thm:method-subtraction`, `thm:method-template`, `prop:disall-two-routes`, `prop:disall-h5`, `thm:disall-factorization`, `thm:dy-factorization`, `thm:tmd-factorization`, `prop:excl-soft-cancel`, `thm:excl-meson-L`, `prop:appN-sia`, `prop:appN-thrust`, `prop:appN-dy`, `prop:appN-tmd-window`, `thm:appN-structure` | grouped power counting under (Com)(Abs); the fibered programme `rem:appN-fibered-allorders` |
| `asm:appN-ward-product` | AppN | [A] | Ward 恒等式的乘积结构与减除的重组 | (WI1) Ward identities apply to integrands already modified by other approximators and give hard ⊗ collinear ⊗ soft; (WI2) regrouping of subtractions by order | [A] (content of `lem:method-ward-multi` + combinatorics); abelian and $n\le2$ tree level [R] | `thm:method-template`, `prop:disall-factorized-subtraction`, `thm:disall-factorization`, `prop:tmd-zero-bin-soft`, `prop:excl-soft-cancel`, `prop:appN-sia`, `prop:appN-thrust`, `prop:appN-dy`, `thm:appN-structure`, `prop:appO-past-wilson`, `thm:appO-main`, `cor:appO-interface`, `prop:appO-tmd` | inductive Ward proof for approximated integrands (App F) |
| `asm:appN-brst-nonlocal` | AppN | [C] | 多定域光线算符的 BRST 分类 | BRST-invariant multilocal light-ray operators of the K-gluon expansion are gauge invariant modulo BRST-exact and EOM operators, which drop out of physical matrix elements | assumed by Collins 2011 §11.3.2; no all-order argument (= `conj:front-brst-multilocal`, [C]); bilocal PDF operators: moment reduction (`prop:front-brst-bilocal`, N04); **named gap** of the chapter [A] statements (MD1) | `thm:appN-structure` | multilocal BRST cohomology (Ch24 programme) |
| `asm:appN-cutsum` | AppN | [A] | 割图求和的公共表示 | (CU1) common LCOPT domain and integrand for each forward graph; (CU2) approximators act on it, (GA)/(CS) hold for it; (CU3) event-shape density condition | open in general; (CU1) provided by App O for DY-type graphs under `asm:appO-lcopt` | `prop:method-fsi`, `thm:method-template`, `prop:disall-two-routes`, `thm:disall-factorization`, `thm:dy-factorization`, `prop:appN-sia`, `prop:appN-thrust`, `prop:appN-dy`, `prop:appN-tmd-window`, `thm:appN-structure` | LCOPT theorem for general graphs (`asm:appO-lcopt`) |
| `asm:appN-uv` | AppN | [A] | 被积函数层次的紫外重整化 | (U1) integrand-level UV renormalization (DR+$R$ operation, or BPHZ(L) plus the finite non-invariant counterterms restoring Slavnov–Taylor identities); (U2) $T_R$ commutes with the UV subtractions up to harmless finite local terms | partly proven (linear substitutions; Euclidean points) | `thm:method-subtraction`, `thm:method-template`, `prop:disall-factorized-subtraction`, `thm:disall-factorization`, `thm:appN-structure` | full proof of (U2) for all approximators |
| `asm:appN-multren` | AppN | [A] | 共线因子的乘法重整化（维数正规化路线） | (Z1) moment-space multiplicative renormalization of collinear factors (theorem for on-shell twist-2 local operators; input for FFs); (Z3)(i) DR on-shell massless partonic targets give the same $\hat{\mathsf H}^{\rm bare}$, (ii) $\hat{\mathsf H}^{\rm bare}Z$ finite (DR mass factorization) | (Z1) theorem for PDFs; (Z3) [A], verified at NNLO/N3LO | `prop:pdf-timelike-dglap`, `thm:method-template`, `thm:disall-renorm-compat`, `prop:disall-h5`, `thm:disall-factorization`, `thm:coll-sia`, `asm:appN-ir-regulator`, `thm:appN-structure` | (Z1) for FFs; (Z3)(ii) from (Z1)+(Z2) via `thm:disall-renorm-compat` |
| `asm:appN-ir-regulator` | AppN | [C] | 保持 Ward 恒等式的部分子靶红外正规化 | (Z2) partonic targets with an IR regulator preserving the Ward identities, with finite invertible renormalized partonic PDFs | genuine input: quark targets (massive quarks) only; gluon targets only off shell with alien counterterms (MD2) | `thm:disall-renorm-compat` | construct such a regulator or the off-shell route with aliens |
| `asm:appN-tmd` | AppN | [A] | TMD 输入 | (T1) $k_T$ tails in the rapidity window; (T2) asymptotic linearity of $\ln\tilde S$, $\ln\tilde f^{\rm unsub}$ with equal slope; (T3) $b$-space multiplicative renormalization; (T4) $y_B\to-\infty$ under the integral | one loop verified (c_tmd); all orders [A] | `prop:tmd-zero-bin-soft`, `thm:tmd-factorization`, `prop:tmd-evolution`, `prop:appN-tmd-window`, `thm:appN-structure` | all-order proofs of (T2) (CS equation) and (T1) |
| `asm:appN-endpoint` | AppN | [A] | 端点条件 | (E1) endpoint integrability of meson-jet subgraphs; (E2) hard kernel at most $1/x$, $1/\bar x$; (E3) endpoint region suppressed | true for finite Gegenbauer truncations; assumption for non-perturbative DAs | `prop:excl-soft-cancel`, `thm:excl-pion-ff`, `thm:excl-meson-L`, `thm:appN-structure` | endpoint behaviour of partonic DAs at all orders |
| `asm:appN-analytic-reg` | AppN | [A] | 两圈图样积分的辅助解析正规化 | (RA1) the analytically regularized pattern integrals of the two-loop planar vertex are meromorphic in $(\varepsilon,\delta)$; (RA2) the nine single-approximator integrals are regular at $\delta=0$ for small $\varepsilon\ne0$ with their DR values as limits | [A]: analytic renormalization covers quadratic propagators, not the eikonal-type linear factors | `prop:appN-twoloop-remainder` | meromorphy for linear (eikonal) factors |
| `asm:appO-lcopt` | AppO | [A] | 光锥序微扰论的适用性 | (i) no zero modes or endpoint contributions at $l^+=0$ at leading power; minus-component truncation can be dropped; (ii) instantaneous-loop values reproducing the covariant minus integrals | open; partial results in the light-front literature (`Schoonderwoerd:1998qj`, `Schoonderwoerd:1998iy`); Hermiticity of the cut rules: `lem:appJ-cut-hermiticity` (corrected in v2.3) | `prop:method-fsi`, `lem:dy-fsi`, `thm:dy-factorization`, `prop:break-measurement`, `lem:appO-hard-locality`, `lem:appO-unitarity`, `prop:appO-ss-localize`, `lem:appO-side-independent-windows`, `prop:appO-ss-cancel`, `prop:appO-twoexch-spectator`, `prop:appO-one-sided`, `thm:appO-main`, `cor:appO-interface`, `prop:appO-tmd` | equivalence of LCOPT and covariant PT incl. renormalization |
| `asm:appO-adjacent-swap` | AppO | [P] | 相邻交换对称性（ADJ） | (ADJ) of `def:appO-sectors` for the leading-power cut-summed LCOPT jet factors of QCD graphs with two spectator insertions | proved in the scalar spectator model; argued, not proved, for spin-summed QCD jets; enters only the QCD transfer of the model theorems | `prop:appO-twoexch-spectator`, `prop:appO-pergraph-weights`, `prop:appO-halfcoinc-sensitivity` | a proof for leading-power LCOPT jets |
| `asm:appO-real-jets` | AppO | [P] | 旁观者喷注函数的实性（REAL） | (REAL) of `def:appO-sectors`: every colour-stripped jet function is a fixed phase times a rational function with real coefficients | proved in the scalar spectator model; argued for spin-summed QCD jets; enters only the QCD transfer of the model theorems | `prop:appO-twoexch-spectator`, `prop:appO-pergraph-weights`, `prop:appO-halfcoinc-sensitivity` | a proof for leading-power LCOPT jets |
| `asm:appO-collinear-ends` | AppO | [A] | 共线端点的匹配 | with two-sided analytic rapidity regulators on the SS windows, the $A$- and $B$-collinear ends (and the cut contributions located there) are reproduced by collinear factorization with no leftover Hermitian $C_AX$ (fully coincident) or $[X_1,X_2]$ (half-coincident) term | open; relocates, not removes, the content of `asm:appO-mixing`(c) for coincident $O(g^4)$ patterns; the half-coincident part is proved in the model with a $k^-$ regulator alone (`prop:appO-halfcoinc-sensitivity`); not a premise of `thm:appO-main` | `prop:appO-twoexch-spectator`, `prop:appO-twoexch-regulated`, `prop:appO-halfcoinc-sensitivity` | compute the cut direct-line contributions or prove their suppression (`rem:appO-cut-ss`) |
| `asm:appO-envelope` | AppO | [A] | 纤维积分误差的可积包络 | envelope $\hat\Phi_R$ for all fibre-integration errors of the equal-time rewriting, uniform in $\varepsilon$ and $\eta_0$; boundary layers; for coincident connections imposed on side-summed families | open; Glauber specific; the per-graph version cannot hold within the class of `prop:appO-pergraph-weights` | `prop:method-glauber-deformation`, `prop:dy-deformation`, `thm:dy-factorization`, `asm:appO-mixing`, `prop:appO-one-sided`, `thm:appO-main`, `cor:appO-interface`, `prop:appO-tmd` | fibre version of the integral power counting |
| `asm:appO-mixing` | AppO | [A] | Glauber–软混合与重合连接的完整图集相消 | (a′) pre-integration localization with envelope bounds (incl. $\sum_\sigma\vert w_\sigma\vert$ and the exceptional sets $E_j$); (b) cut compatibility of $S$; (c) for coincident connections the complete graph set gives $\mathcal W'^\dagger\mathcal W=1+O(\lambda^a)$ weakly | (a′)(b) automatic for $\mathcal G_0$; (c) holds for two-gluon exchange between eikonal lines at $O(g^4)$ (`prop:dy-eikonal-twogluon`); model evidence for the uncut lines of composite spectators (`prop:appO-twoexch-spectator`, slot X1f partial); cut direct lines, $O(g^6)$ (`prop:appO-g6-ladder`) open | `prop:method-glauber-deformation`, `prop:dy-deformation`, `thm:dy-factorization`, `lem:tmd-glauber`, `thm:tmd-factorization`, `prop:appO-one-sided`, `thm:appO-main`, `cor:appO-interface`, `prop:appO-tmd` | all-order unitarity argument for the complete graph set incl. cut direct lines; the matching `asm:appO-collinear-ends` |
| `asm:appO-deformation` | AppO | [A] | 一般构型、相容性、软角区与 H-发射端点 | (a) deformation targets for general configurations; (b) compatibility with the region set algebra; (c) (CS1)(CS2) on the soft-angle region incl. the out-of-window parts and wee-line endpoints of the side-independent windows; (d) H-emission endpoints and coincident SA/AS insertions | (a) proved for $\mathcal G_0$ and graded configurations; window-edge terms vanish identically (`lem:appO-side-independent-windows`, slot X1c); (b)(c)(d) open, needed even for abelian $\mathcal G_0$ (slot X1d not delivered) | `prop:method-glauber-deformation`, `prop:dy-deformation`, `thm:dy-factorization`, `lem:tmd-glauber`, `prop:appN-dy`, `thm:appO-main`, `cor:appO-interface`, `prop:appO-tmd` | soft-scale treatment of spectator couplings; analyticity of the ordering weights near $k^+=0$ |
| `asm:appO-rewritten-cs` | AppO | [A] | 改写形式与族求和形式的 Collins 条件 | (CS1)(CS2) for rewritten and family-summed forms, incl. the matching at $n\cdot K_i=0$ (Wilson-line prescription) and the allocation of SA/AS endpoints | open; Glauber specific; harmless for collinear PDFs, substantive for TMD | `prop:method-glauber-deformation`, `prop:dy-deformation`, `thm:dy-factorization`, `lem:tmd-glauber`, `thm:tmd-factorization`, `prop:appN-dy`, `prop:appO-past-wilson`, `thm:appO-main`, `cor:appO-interface`, `prop:appO-tmd` | one- and two-loop checks of the past-pointing prescription; general proof |
| `asm:lamet-aux-renorm` | Ch22 | [A] | 含类空辅助静态色源的 QCD 的可重整性 | (AX1) an auxiliary colour-triplet spinless Grassmann field $Q$ along $\hat n=\hat e_z$ turns Wilson-line operators into products of local composites; (AX2) the extended theory is renormalizable BRST-invariantly with $Z_Q$, $Z_1^{QQg}$ (tied to $Z_g$) and $\delta m$ only; (AX3) the $Q$ determinant is constant in DR | [A] (auxiliary-field method; all-order arguments in the LaMET literature) | `prop:lattice-renormalizability`, `asm:lamet-ope`, `asm:lamet-gap`, `conj:lamet-decay-qcd`, `asm:lamet-staple`, `thm:yzliu-soft-hqet` | complete algebraic renormalization of the extended theory |
| `asm:lamet-ope` | Ch22 | [A] | 类空 Wilson 线算符的短距离 OPE（重整化微扰论） | (OP1) leading-twist light-ray OPE of $O^R_{\gamma^\alpha}(z,\mu)$ as $z^2\to0$ at fixed $\lambda$, twist-2 coefficients $C_n$, $C'_n$; (OP2) for massless on-shell partonic states the leading-twist expression holds for all $z$ order by order | [A] | `thm:lamet-coordinate`, `thm:lamet-parton-momentum`, `prop:lamet-tmc`, `prop:lamet-sdf`, `thm:lamet-quasi-gpd` | perturbative OPE theorem for Wilson-line operators (cf. App M) |
| `asm:lamet-gap` | Ch22 | [C] | 谱隙与边界值正则性 | (GP1) isolated external one-particle state, other contributing states at least $\Delta m$ above; (GP2) Fredenhagen-type boundary-value regularity in complex time; (GP3) QCD: non-perturbative reduction to QCD + static source with a gap $\Lambda_X$ above the static threshold | open | `thm:lamet-exp-decay`, `conj:lamet-decay-qcd` | non-perturbative spectral information |
| `asm:lamet-uniform` | Ch22 | [C] | 扭度展开对 Ioffe 时间的一致性 | (UI-a) coordinate form: twist-2 remainder of the hadronic ITD bounded by $K(-z^2)\Lambda^2(1+\vert\ln(-z^2\mu^2)\vert)^k$ uniformly in $\lambda$; (UI-b) ray form: along $z^2=-\lambda^2/P_z^2$ the remainder beyond twist 4 has Fourier transform $o(P_z^{-2})$ at fixed $x$ | open | `thm:lamet-hadronic` | non-perturbative control of the twist expansion |
| `asm:lamet-twist4` | Ch22 | [C] | 领头幂次修正的结构（扭度 4） | (TW1) $O(z^2)$ term $z^2\Lambda^2\int d\alpha\,e^{i\alpha\lambda}\rho_4(\alpha,z^2)$, $\rho_4$ supported in $[-1,1]$; (TW2) at most logarithmic $z^2$ dependence | open | `asm:lamet-large-z`, `thm:lamet-hadronic` | twist-4 OPE for hadron states |
| `asm:lamet-large-z` | Ch22 | [C] | 大距离区域的控制 | (LZ1) the region $\vert\lambda\vert>z_0P^z$ contributes $o(1)$ to the Fourier transform of $\tilde h-\tilde h_{\rm tw2}$ at fixed $x\in(0,1)$; (LZ2) the same with $\tilde h-\tilde h_{\rm tw2}-\tilde h_{\rm tw4}$ is $o(P_z^{-2})$ | open; `thm:lamet-exp-decay` gives decay under `asm:lamet-gap` but no usable constants | `thm:lamet-hadronic` | quantitative exponential decay of hadronic matrix elements with constants uniform in $P^z$ |
| `asm:lamet-staple` | Ch22 | [A] | 订书钉形类空 Wilson 线算符的重整化与 $L\to\infty$ 极限 | (ST1) staple$/\sqrt{Z_E}$ multiplicatively renormalizable with end-point factors only; (ST2) $L\to\infty$ exists order by order; (ST3) on the lattice $\sqrt{Z_E}$ plus the short-distance matrix element removes all UV divergences | [A] | `def:lamet-quasi-tmd`, `thm:lamet-quasi-tmd`, `prop:yzliu-qtmd-powercount` | all-order proof (auxiliary-field method) |
| `asm:lamet-soft-rapidity` | Ch22 | [A] | 离光锥软函数的大快度结构 | (SR) $\ln S=(Y+Y')\tilde K+\mathcal D+O(e^{-(Y+Y')})$ | [A] | `def:lamet-reduced-soft`, `thm:lamet-quasi-tmd` | rapidity-divergence factorization at all orders (Ch23) |
| `asm:lamet-order-limits` | Ch22 | [A] | 极限次序 | (OL1) $\varepsilon\to0$ commutes with $L\to\infty$ and with the off-light-cone regulator limit for $\Omega/\sqrt S$; (OL2) large-rapidity vs Collins scheme differ by a UV factor $C_q$ | [A]; one loop verified | `thm:lamet-quasi-tmd` | all-order proof |
| `asm:yzliu-heavy-pair` | Ch23 | [C] | 静态色单态 $Q\bar Q$ 对的谱假设 | (HP1) isolated colour-singlet static-pair ground state with residual energy $\gamma^{-1}V(\vec b_\perp)$, gapped continuum; (HP2) non-zero boost-invariant overlap; (HP3) self-energies and pair evolution cancel against $\sqrt{ZZ}$ (LSZ-type amputation) | open | `cor:yzliu-soft-form-factor` | non-perturbative static-pair spectroscopy |
| `asm:yzliu-wightman-pt` | Ch23 | [A] | 维数正规化微扰论中的 Wightman 结构 | (WP1) order by order in linear covariant gauges with DR at $\varepsilon\ne0$ gluon/ghost Wightman functions satisfy spectral condition and locality (Kugo–Ojima), hence BHW analyticity; (WP2) null separations on one light-like line are scaleless | [A] | `thm:yzliu-analyticity`, `thm:yzliu-time-ordering`, `conj:yzliu-complex-wilson`, `thm:yzliu-jet-continuation` | proof within the covariant operator formalism |
| `asm:yzliu-lightcone-uniform` | Ch23 | [P] | 光锥极限对 ${\rm Im}\,\theta$ 的一致性 | (UL) the light-cone limit $Y\to\infty$ of single-time-ordered soft functions is uniform in ${\rm Im}\,\theta\in[-\pi,\pi]$ | verified at fixed orders | `prop:yzliu-universality-classes` | all-order uniformity |
| `asm:front-mor-complete` | Ch24 | [C] | 区域集合的完备性 | (MR) the listed regions (essential facets, or the regions found after dissecting the polytope), each expanded and integrated over the whole domain, reproduce the asymptotic expansion to all orders — no hidden regions, no non-scaleless overlaps beyond `lem:front-jantzen` | proven for Euclidean limits and the one-facet case; open in Minkowski kinematics (facet recipe fails from three loops) | `prop:front-commuting` | `conj:front-mor-minkowski`; an algorithm guaranteed to find all regions with a completeness proof |
| `asm:front-scet-modes` | Ch24 | [A] | SCET 的模式完备性与 Glauber 模式的缺席 | (SM1) the listed hard, (anti-)hard-collinear, collinear, soft and soft-quark modes reproduce all regions at the stated power; (SM2) Glauber modes do not contribute at that power (colour-neutral final states, $e^+e^-$; partonic coefficient functions only) | [A]: the standard SCET assumption, covered by the region analyses of the processes considered; completeness checked case by case | `thm:front-hgg`, `prop:front-ggh`, `prop:front-nlp-ll`, `prop:front-nlp-dis`, `prop:front-sidis-nlp` | a region analysis (pinch analysis and power counting, Ch4, Ch9) of each process at the stated power with the Glauber region treated explicitly |

Total: **47** entries (6 global; 4 App M; 15 App N; 8 App O; 9 Ch22; 3 Ch23; 2 Ch24). Tags: [A] 29, [C] 14, [P] 3, — 1. (Identical to FINAL_OUTLINE_v2 §08 `### Assumptions`; "used by" = direct `\uses` users computed from FINAL_OUTLINE_v2 after the verify patch v2.3.)

---------------------------------------------------------------------------------------------------

## 2. MA0–MA4 dictionary (Ch1 `def:intro-MA`)

| umbrella | content (critic §12) | register entries |
|---|---|---|
| MA0 存在性 | QCD exists as a quantum field theory with the required composite operators | `asm:intro-wightman`, `asm:intro-composite` |
| MA1 区域完备性 | the partonic leading regions are complete for hadronic states | `asm:intro-bridge` (with MA2) |
| MA2 幂次计数的传递 | power suppression transfers from partonic to hadronic states | `asm:intro-bridge` (with MA1) |
| MA3 解析性与高能行为 | analyticity of forward amplitudes and their high-energy behaviour | analyticity is now a theorem under MA0 (`prop:dis-dispersion-np`); the genuine remainder is `asm:intro-growth` |
| MA4 渐近性 | perturbative series are asymptotic to the non-perturbative quantities | `asm:intro-af-coeff`, and the asymptotic part of `asm:intro-bridge` |

The non-perturbative OPE `asm:intro-np-ope` is listed under MA0 in the 「非微扰地位」 lines of OPE-based statements (it presupposes MA0 and adds the expansion). The technical entries (`asm:appM-*`, `asm:appN-*`, `asm:appO-*`, frontier entries) are not umbrella-mapped: they concern perturbation theory or hadron-level frontier hypotheses and are cited by label.

---------------------------------------------------------------------------------------------------

## 3. Full entries

Format of each entry: heading with label, Chinese title, tag; then 所属 (owner, class), 陈述 (exact content with inner items), 地位, 文献 (with locations; 「位置待核实」 where the location is not documented; 「文献待补」 where no bib key exists), 被使用于 (direct users in the working drafts of 2026-10-10; the merge recomputes them and App P checks them, C-P10), 解除途径, `\uses`. Users written in *italics* are additions that the merge must make to the owners' `\uses` lists.

### 3.1 Owner Ch1 `intro` — global non-perturbative assumptions

#### `asm:intro-wightman` — QCD 的 Wightman 结构 [\tagC] (global)
- **所属：** Ch1 `sec:intro-tags`; technical commentary (which axiom is used where) in App M §M.8. Global (not in the grade propagation of ordinary statements).
- **Binding text** (FINAL_OUTLINE_v2 Ch1 entry, reproduced verbatim; the 「被使用于」 field there lists the direct `\uses` users computed at the merge):
    - **陈述.** (W1) QCD with $n_f$ quark flavours of positive masses exists as a Wightman theory: a Hilbert space with positive metric, a strongly continuous unitary representation of the Poincaré group, a unique invariant vacuum $|0\rangle$, and local gauge-invariant composite fields — in particular the conserved hermitian electromagnetic current $j^\mu$ and the operators of `asm:intro-composite` — as operator-valued tempered distributions satisfying locality; parity is a symmetry. (W2) Spectral condition: the joint spectrum of $P^\mu$ lies in the closed forward cone; **in the superselection sector of the target's conserved flavour quantum numbers** the spectrum lies in $\{p^2\ge M^2,p^0>0\}$, $M$ the target mass, and for Haag–Ruelle one-particle states $M$ is an isolated eigenvalue of the mass operator in that sector (isolation is used only for the existence of the asymptotic target state). (W3) The connected forward matrix elements $\langle P|j^\mu(x)j^\nu(0)|P\rangle$ are tempered distributions in $x$. (W4) A covariant retarded extension $\tilde R^{\mu\nu}(q)$ of the commutator exists with $q_\mu\tilde R^{\mu\nu}=0$; its polynomial (contact-term) ambiguity affects only finitely many low Taylor coefficients $t_n$ of the forward amplitude. Massive light quarks are part of the assumption; the reconciliation with massless $\overline{\rm MS}$ coefficients is part of `asm:intro-af-coeff`.
    - **地位：** open — 4D QCD has not been constructed (the existence of 4D Yang–Mills with a mass gap is a Clay Millennium problem); widely assumed; (W2) as stated here corrects the spectral condition "nucleon isolated below the $N\pi$ continuum", which is false in the chiral limit and for $m_u\ne m_d$ (ERR-M25). **文献：** `Streater:1989vi`, `Jost:1965yxu`, `Haag:1958vt`; technical commentary (which axiom is used where) in App M §M.8. **被使用于：** direct `\uses` users (computed at the merge): `asm:intro-composite`, `asm:intro-np-ope`, `asm:intro-growth`, `prop:prelim-optical`, `prop:ee-R-ImPi`, `prop:ee-analytic`, `prop:ee-smearing`, `prop:dis-W-structure`, `prop:dis-ope-rg`, `prop:dis-dispersion-np`, `thm:dis-fixed-n`, `thm:dis-moments-np`, `cor:dis-weak-xspace`, `thm:dis-moments`, `prop:dis-twist4`, `prop:dis-tmc`, `thm:dis-bjorken`, `prop:pdf-invariance`, `prop:pdf-support-hadron`, `thm:pdf-moments-local`, `thm:pdf-dis-xspace`, `prop:pdf-sum-rules`, `prop:pdf-timelike-dglap`, `prop:coll-photon-sf`, `prop:coll-luxqed`, `thm:coll-g1-moments`, `prop:coll-transversity-evolution`, `thm:tmd-sivers-sign`, `prop:excl-erbl`, `prop:excl-polynomiality`, `thm:heavy-inclusive-b`, `thm:lamet-exp-decay`, `lem:appM-forward-tube`, `lem:appM-positivity`; in addition every hadron-level statement whose 「非微扰地位」 line names it (`def:intro-MA` refers to all six global entries). **解除途径：** construction of QCD (constructive field theory); in the meantime: lattice QCD as non-perturbative evidence (not proof).
    - `% uses: none`

#### `asm:intro-composite` — 规范不变复合算符与光线算符的存在与重整化群 [\tagC] (global)
- **所属：** Ch1 `sec:intro-tags`; technical commentary (which axiom is used where) in App M §M.8. Global (not in the grade propagation of ordinary statements).
- **Binding text** (FINAL_OUTLINE_v2 Ch1 entry, reproduced verbatim; the 「被使用于」 field there lists the direct `\uses` users computed at the merge):
    - **陈述.** (C1) Gauge-invariant local composite operators exist as Wightman fields (in the sense of `asm:intro-wightman`) and are organized in finite families graded by mass dimension; after renormalization they obey RG equations with triangular mixing (an operator mixes only with operators of equal or lower dimension), with $\beta$ and anomalous-dimension matrices asymptotic to their perturbative series. (C2) The spin-$n$ twist-2 sector with non-zero spin-averaged forward matrix elements is spanned by the quark operators $O_q^{(n)}$ (one per flavour) and the gluon operator $O_g^{(n)}$ (even $n$) of the perturbative classification (forward pointers: `def:dis-twist`, `lem:dis-twist-classification`). (C3) The PDF light-ray operators (Wilson-line bilocals of `def:pdf-lightray`, forward pointer) exist between hadron states as tempered distributions in $w^-$, and their moments are the reduced matrix elements $A_i^{(n)}$ of the local twist-2 operators.
    - **地位：** open (presupposes `asm:intro-wightman`); in PT, (C1)–(C3) are theorems (`thm:prelim-composite-renorm`, `thm:pdf-moments-local`). **文献：** `Joglekar:1976eb`, `Joglekar:1976pe`, `Hollands:2007zg` (PT/pure YM). **被使用于：** direct `\uses` users (computed at the merge): `asm:intro-np-ope`, `prop:dis-ope-rg`, `thm:dis-moments-np`, `cor:dis-weak-xspace`, `thm:dis-moments`, `prop:dis-twist4`, `prop:dis-tmc`, `thm:dis-bjorken`, `prop:pdf-invariance`, `prop:pdf-support-hadron`, `thm:pdf-moments-local`, `thm:pdf-dglap`, `thm:pdf-dis-xspace`, `prop:pdf-sum-rules`, `prop:pdf-timelike-dglap`, `prop:coll-photon-sf`, `prop:coll-luxqed`, `thm:coll-g1-moments`, `prop:coll-transversity-evolution`, `prop:tmd-small-b`, `thm:tmd-sivers-sign`, `prop:excl-erbl`, `prop:excl-polynomiality`, `thm:heavy-inclusive-b`, `lem:appM-norm-bound`; in addition every hadron-level statement whose 「非微扰地位」 line names it (`def:intro-MA` refers to all six global entries). **解除途径：** as for `asm:intro-wightman`.
    - `\uses{asm:intro-wightman}`

#### `asm:intro-np-ope` — 非微扰算符乘积展开 [\tagC] (global)
- **所属：** Ch1 `sec:intro-tags`; technical commentary (which axiom is used where) in App M §M.8. Global (not in the grade propagation of ordinary statements).
- **Binding text** (FINAL_OUTLINE_v2 Ch1 entry, reproduced verbatim; the 「被使用于」 field there lists the direct `\uses` users computed at the merge):
    - **陈述.** (O1) For the T-product of two currents, the Euclidean OPE holds between the vacuum and between the hadron states of `asm:intro-wightman`, to every finite level $N$ in the operator dimension: $\tilde T^{\mu\nu}(q)-\sum_{d_j\le N}\tilde C^{\mu\nu}_j(q;\mu)\langle O_j\rangle=O(|q|^{2-N-\delta}\ln^k|q|)$, with remainder bounds uniform in the direction of $q$ and with bounds on all $q$-derivatives; the coefficients are Lorentz covariant. (O2) Odd-twist (chiral-odd) coefficients are suppressed by a light-quark mass ($\propto m_q/|q|$).
    - **地位：** open, widely assumed; its vacuum part is `conj:ee-np-ope` [C] (forward pointer); compatible with renormalons and instantons only as an asymptotic statement (`asm:intro-af-coeff`). **文献：** `Wilson1969`, `ShifmanVainshteinZakharov1979a`, `Novikov:1984rf`; AQFT approach `Bostelmann:2005rr`. **被使用于：** direct `\uses` users (computed at the merge): `asm:intro-af-coeff`, `lem:dis-ope-segment`, `thm:dis-fixed-n`, `thm:dis-moments-np`, `cor:dis-weak-xspace`, `thm:dis-moments`, `prop:dis-twist4`, `prop:dis-tmc`, `thm:dis-bjorken`, `thm:pdf-dis-xspace`, `prop:coll-photon-sf`, `thm:coll-g1-moments`; in addition every hadron-level statement whose 「非微扰地位」 line names it (`def:intro-MA` refers to all six global entries). **解除途径：** a non-perturbative definition of the OPE in QCD (Ch25 open problem OP-A3).
    - `\uses{asm:intro-wightman, asm:intro-composite}`

#### `asm:intro-af-coeff` — 系数的渐近自由行为 [\tagC] (global)
- **所属：** Ch1 `sec:intro-tags`; technical commentary (which axiom is used where) in App M §M.8. Global (not in the grade propagation of ordinary statements).
- **Binding text** (FINAL_OUTLINE_v2 Ch1 entry, reproduced verbatim; the 「被使用于」 field there lists the direct `\uses` users computed at the merge):
    - **陈述.** At $\mu=|q|$ the OPE coefficients of `asm:intro-np-ope` are asymptotic to their $\overline{\rm MS}$ perturbative series: for every $K$, $\tilde C_i(q;|q|)=|q|^{2-d_i}\big[\sum_{k\le K}c_{i,k}(\hat q)\,\alpha_s(|q|)^k+O(\alpha_s(|q|)^{K+1})\big]$, with $c_{i,k}$ the perturbative coefficients (forward pointers `prop:dis-ope-euclid`, `prop:dis-c-oneloop`); light-quark-mass corrections are included as higher-dimension terms.
    - **地位：** open; compatible with IR renormalons and with instanton effects $e^{-2\pi/\alpha_s}=(\Lambda/Q)^{\beta_0}$ (both beyond every power of $\alpha_s$). **文献：** `Mueller1985`, `Beneke1999`. **被使用于：** direct `\uses` users (computed at the merge): `thm:dis-moments-np`, `cor:dis-weak-xspace`, `thm:dis-moments`, `prop:dis-twist4`, `prop:dis-tmc`, `thm:dis-bjorken`, `thm:pdf-dis-xspace`, `prop:coll-photon-sf`, `thm:coll-g1-moments`, `thm:heavy-inclusive-b`, `lem:appM-norm-bound`; in addition every hadron-level statement whose 「非微扰地位」 line names it (`def:intro-MA` refers to all six global entries). **解除途径：** as for `asm:intro-np-ope`.
    - `\uses{asm:intro-np-ope}`

#### `asm:intro-growth` — 前向振幅的增长条件 [\tagC] (global)
- **所属：** Ch1 `sec:intro-tags`; technical commentary (which axiom is used where) in App M §M.8. Global (not in the grade propagation of ordinary statements).
- **Binding text** (FINAL_OUTLINE_v2 Ch1 entry, reproduced verbatim; the 「被使用于」 field there lists the direct `\uses` users computed at the merge):
    - **陈述.** For each fixed $Q^2$, the invariant forward Compton amplitude of a hadron target satisfies $\lim_{y\to\infty}T_2(iy,Q^2)/(iy)=0$ (normalization of `def:dis-compton`, forward pointer).
    - **地位：** open; holds at every computed fixed order in PT; it is **equivalent** to the validity of the low-moment sum rules (in particular the momentum sum rule) for the hadronic structure function and to the absence of a real fixed-pole term $c\,\omega$ (forward pointer `prop:dis-low-moments`); Regge behaviour of $F_2$ is neither necessary nor sufficient. **文献：** fixed poles: `conj:coll-bc` context (`BurkhardtCottingham1970`). **被使用于：** direct `\uses` users (computed at the merge): `thm:dis-moments-np`, `thm:dis-moments`, `thm:dis-bjorken`, `thm:pdf-dis-xspace`; in addition every hadron-level statement whose 「非微扰地位」 line names it (`def:intro-MA` refers to all six global entries). **解除途径：** a bound on the high-energy behaviour of the forward amplitude from first principles (Ch25 open problem OP-A4).
    - `\uses{asm:intro-wightman}`

#### `asm:intro-bridge` — 从部分子微扰论到强子的桥接假设 [\tagC] (global)
- **所属：** Ch1 `sec:intro-tags`; technical commentary (which axiom is used where) in App M §M.8. Global (not in the grade propagation of ordinary statements).
- **Binding text** (FINAL_OUTLINE_v2 Ch1 entry, reproduced verbatim; the 「被使用于」 field there lists the direct `\uses` users computed at the merge):
    - **陈述.** (Br1) *Region completeness:* the leading-power regions found in PT for IR-regulated partonic states are the only leading-power regions in QCD with hadron states; confinement modifies only the IR-sensitive factors and creates no new leading region. (Br2) *Power-counting transfer:* all $\Lambda$-sensitivity of a hadronic cross section covered by a factorization theorem sits in the hadronic matrix elements of the same operators (PDFs, FFs, TMDs, DAs, soft factors) that appear in the partonic theorem. (Br3) *Asymptoticity:* the remainder is $O((\Lambda/Q)^p)$ for some $p>0$ as an asymptotic statement; perturbative series are asymptotic and renormalon ambiguities are of the order of power corrections, so "exact up to power corrections" has meaning only once the power-correction term is defined.
    - **地位：** open; supported by phenomenology, lattice consistency and renormalon analyses; the value of $p$ is not fixed by the perturbative proofs except for OPE-accessible quantities. **文献：** `CollinsSoperSterman1989`, `Collins2011` (ch. 14 discussion), `Beneke1999`. **被使用于：** direct `\uses` users (computed at the merge): `thm:method-template`, `thm:disall-factorization`, `thm:disall-heavy`, `prop:disall-nuclear`, `thm:coll-sia`, `thm:coll-sidis`, `thm:coll-direct-photo`, `thm:dy-factorization`, `thm:dy-colour-singlet`, `thm:dy-polarized`, `thm:dy-higher-twist`, `thm:tmd-factorization`, `prop:tmd-small-b`, `cor:tmd-sivers-observable`, `prop:tmd-collins-universality`, `thm:scet-thrust`, `thm:jets-ngl-factorization`, `thm:break-ddis`, `thm:break-double-dy`, `thm:excl-pion-ff`, `thm:excl-transition`, `thm:excl-dvcs`, `thm:excl-meson-L`, `thm:heavy-bdpi`, `prop:heavy-btopi-ff`, `prop:heavy-qcdf-lp`, `thm:heavy-inclusive-b`, `thm:heavy-nrqcd-decay`, `prop:heavy-quarkonium-fragmentation`, `prop:power-dis-twist4-x`; in addition every hadron-level statement whose 「非微扰地位」 line names it (`def:intro-MA` refers to all six global entries). **解除途径：** non-perturbative control of QCD (Ch25 open problem OP-A1).
    - `\uses{def:intro-factorization}`

### 3.2 Owner App M

#### `asm:appM-remainder` — 冻结 $q$ 双局域正规乘积的动量空间余项估计 [\tagA]
- **所属：** App M §M.4 (`sec:appM-remainder`). Technical.
- **陈述：** Massive four-dimensional Euclidean model of §M.2 (scalars and Dirac fermions, dimension-4 monomial interactions), at each order. Let $\tilde N_{a,\Gamma}(q;p)$ be the contribution of the graph $\Gamma$ to the frozen-$q$ bilocal normal product $\tilde N_a$ of `def:appM-normal-product` ($a\in D+\mathbb Z_{\ge0}$, $D=d_A+d_B-4$), and $\mathcal H_{a,\Gamma}$ the linear span of the functions obtained from $\tilde N_{a,\Gamma}$ by finitely many derivatives $\partial/\partial p_j^\nu$, multiplications by $p_{j\mu}$ and applications of $m\,\partial_m$. There is an integer $k$ such that every $h\in\mathcal H_{a,\Gamma}$ obeys $|h(q;p)|\le K_h|q|^{D-1-a}(\ln|q|)^k$ for $|q|\ge2$, uniformly in $q/|q|$ and for $p$ in compact sets.
- **地位：** 在所述形式下开放（v2.3）：验证扩展的槽位 X3a 未交付——经由 `lem:appM-uniqueness` 从已发表的动量空间 OPE 定理推出本假设的路线是循环的（唯一性论证本身要用到余项估计），所引文献的适用范围亦未核实；本假设已化归为零动量匹配估计 (CTp)（`rem:appM-remainder-reduction`）；维数正规化路线（`prop:dis-ope-euclid` 的 (A1)–(A4)）不需要本假设。
- **文献：** `Anikin:1978tj`, `Zavyalov:1990kv` (momentum-space OPE; scope not verified), `Zimmermann1973`, `Smirnov:1990rz`, `Smirnov2002`, `Bergere:1977wz` (asymptotic expansions of Feynman amplitudes).
- **被使用于：** `thm:appM-scaling`, `cor:appM-coordinate` (direct `\uses` users in FINAL_OUTLINE_v2, computed at the merge).
- **解除途径：** a proof of the zero-momentum matching estimate (CTp) by sector (Weinberg-type) estimates; or a momentum-space OPE theorem whose theory class and remainder form are verified to cover the frozen-$q$ form (slot X3a not delivered).
- `\uses{def:appM-normal-product}`

#### `asm:appM-brst-ope` — OPE 的 BRST 结构：带一个复合旁观者的欧氏展开 (Eε) [\tagA]
- **所属：** App M §M.6 (`sec:appM-brst`). Technical. (Reworded in v2.3 after the X3 verification; the label is kept.)
- **陈述：** Massless QCD in bare dimensional regularization at fixed generic $\varepsilon$ (any gauge parameter $\xi_0$, $B$ off shell, no $\gamma_5$, $D$-dimensional algebra). **(B2) ≡ (Eε):** for one composite spectator $Z=s\phi$ ($\phi$ an elementary field) and products $\Phi$ of elementary fields, the large-$q$ expansion $\langle\mathcal J(q)\,Z\,\Phi\rangle=\sum_{d_O\le a}C_O\langle O\,Z\,\Phi\rangle+\sum_{O'}C^Z_{O'}(q;p_Z)\langle O'\,\Phi\rangle+\mathcal R'$ holds, with the coefficients $C_O$ of the expansion without $Z$ (`prop:dis-ope-euclid`), **merged coefficients** $C^Z_{O'}$ (hard subgraphs containing the $Z$ vertex) polynomial in $p_Z$, all coefficients graded-homogeneous, and $\mathcal R'=O(|q|^{1-a}\ln^k|q|)$. **(B1)** is retired (the name is not reused): its Ward identities hold exactly in DR and its contact-term clause is not needed. The earlier form of (B2), without merged terms, is not the correct generalization of the Euclidean expansion: the merged terms turn $sX_d=0$ into $sX_d\in\mathcal E$ (`thm:appM-brst-reduction`).
- **地位：** 开放（v2.3）：槽位 X3d 部分完成——在 (Eε) 下，物理矩阵元只需规范不变算符这一化归已证明（`thm:appM-brst-reduction`，[R, R_cond]；形式上的定域 BRST 上同调 `lem:appM-lbc-formal`）；(Eε) 本身是带一个复合旁观者的逐图维数正规化欧氏展开，未证明。Joglekar 1977 只在摘要层次读过；Hollands 2008 与 Fröb–Holland 2016（预印本）覆盖纯 Yang–Mills，其对含夸克 QCD 的适用范围未核实（S63-3）。
- **文献：** `Joglekar:1976eb`, `Joglekar:1976pe` (abstract level), `Joglekar:1975nu`, `Kluberg-Stern:1975ebk`, `Henneaux:1995ex`, `Barnich:1999cy` (gauge-fixed BRST cohomology), `Hollands:2007zg`, `Frob:2016mzv` (预印本), `Piguet:1995er`.
- **被使用于：** `prop:dis-ope-gi`, `thm:appM-brst-reduction` (direct `\uses` users in FINAL_OUTLINE_v2, computed after the verify patch).
- **解除途径：** a proof of (Eε) (graph-by-graph DR expansion with one composite spectator, merged hard subgraphs); for pure Yang–Mills a comparison with Hollands' position-space OPE.
- `\uses{def:appM-alien}`

#### `asm:appM-forward` — 前向在壳无质量部分子矩阵元的 OPE 余项 [\tagA]
- **所属：** App M §M.5 (`sec:appM-massless`). Technical.
- **陈述：** Massless QCD, DR (statements for the Laurent coefficients in $\varepsilon$), on-shell parton target $j$ ($p^2=0$, physical polarizations, spin averaged), Euclidean direction $\hat q$ with $2p\cdot\hat q$ purely imaginary: at each order $T^{\mu\nu}_j-\sum_{d_O\le N}\tilde C^{\mu\nu}_O(q;\mu)\langle p|[O]_\mu|p\rangle=O(|q|^{1-N}\ln^k|q|)$, uniformly in the direction (forward on-shell momenta are exceptional, so `prop:dis-ope-euclid` does not apply).
- **地位：** 开放（v2.3）：逐图的前向在壳展开定理已证明（`thm:appM-forward-expansion`，[R, R_PT]；槽位 X3e 逐图通过）；`cor:appM-forward-ope`（[A]）把本假设化归为 (A3)、(Eε)、Joglekar–Lee 三角性与胶子的 `asm:appM-oswi`——化归而非解除；在 $O(\alpha_s)$ 对 $N\le8$ 精确到 $\varepsilon$ 验证（`ex:appM-forward-oneloop`, VF-DIS-13）；槽位 X3c 未交付（被 X3e 取代）。
- **文献：** `ChristHasslacherMueller1972`, `BrandtPreparata1971`, `Anikin:1978tj` (momentum-space form); `Collins:1994ee`, `Hamberg:1991qt` (forward on-shell subtleties).
- **被使用于：** `prop:dis-ope-forward` (direct `\uses` users in FINAL_OUTLINE_v2, computed at the merge).
- **解除途径：** discharge the inputs of `cor:appM-forward-ope` ((A3), (Eε), the Joglekar–Lee triangularity, `asm:appM-oswi`); Ch25 OP-A5.
- `\uses{def:dis-compton}`

#### `asm:appM-oswi` — 前向在壳胶子振幅的 Ward 恒等式 [\tagA]
- **所属：** App M §M.7 (`sec:appM-forward`). Technical. New in v2.3 (X3 verification).
- **陈述：** For the amputated forward on-shell gluon Compton amplitude $M_{ab}$ at each order in DR, $p^aM_{ab}\varepsilon^b=0=\varepsilon^aM_{ab}p^b$ for all $\varepsilon$ with $\varepsilon\cdot p=0$ (including $\varepsilon=p$); equivalently $p^aM_{ab}\propto p_b$ (the BRST form, the ghost amplitude being inside the proportionality factor).
- **地位：** [A]：前向振幅的 BRST Ward 恒等式；单独陈述，是因为零动量转移与在壳无质量胶子的红外微妙之处（`rem:appM-forward-aliens`，R-M24）使标准证明不能直接套用。
- **文献：** `KugoOjima1979`, `Collins:1994ee` (forward on-shell subtleties).
- **被使用于：** `lem:appM-gluon-regularity` (direct `\uses` users in FINAL_OUTLINE_v2, computed after the verify patch).
- **解除途径：** a proof of the forward on-shell Ward identity at all orders (BRST with on-shell IR control).
- `\uses{def:dis-compton, def:prelim-brst}`

### 3.3 Owner App N

#### `asm:appN-contour` — (GA1) 围道 [\tagA]
- **所属：** App N §N.2. Technical.
- **陈述：** There is a contour $\Omega$ (a complex deformation of real loop-momentum space, equal to it as $\|k\|\to\infty$) such that (a) for $\Gamma$ and every subtraction term $C_R\Gamma$ the homotopy from real space to $\Omega$ crosses no singularity, so the $\Omega$-integral (when it exists) equals the real-space integral defined with each denominator's own $i0$ (as $i\eta$, $\eta\to0^+$); (b) each $\int_\Omega C_R\Gamma\,d\mu$, defined for $\varepsilon\in(0,\varepsilon_0]$ by (CS3), continues to a meromorphic function near $\varepsilon=0$.
- **地位：** 一般情形开放；当所有相关极点在同一半平面时成立（`lem:method-i0-compat`；$e^+e^-$ 与 DIS：`lem:coll-final-poles`）；DY 单个割图不成立，由 App O 以单侧形式提供（`cor:appO-interface`）。
- **文献：** `Collins2011` §5.5–§5.6 (contour deformation; 位置待核实), `Collins:2020euz` (geometry of deformations, 预印本).
- **被使用于：** `cor:method-removing-eps`, `thm:method-subtraction`, `prop:disall-two-routes`, `thm:disall-renorm-compat`, `thm:appN-subtraction`, `prop:appN-sia`, `thm:appN-structure` (direct `\uses` users in FINAL_OUTLINE_v2, computed at the merge).
- **解除途径：** a general deformation theorem for leading regions including the Glauber region (Ch24 programme; App O for colour-singlet DY).
- `\uses{def:appN-integrand, def:method-subtraction}`

#### `asm:appN-envelope` — (GA3) 幂次计数包络 [\tagA]
- **所属：** App N §N.2. Technical.
- **陈述：** For every $R_0\in\mathcal R$ there is $\Phi_{R_0}\ge0$ on $U_{R_0}$ with $\int_{U_{R_0}}\Phi_{R_0}d\mu\le CL^K$ uniformly in $\varepsilon$, such that (i) every partially approximated integrand of the telescoping sum of `lem:method-telescoping` (each factor taken exact, approximated by $T_{R_0}$, or as the envelope of rows 3, 4, 6 of `tab:method-errors`) is $\le C\Phi_{R_0}$ on $U_{R_0}\cap\{\|k\|\le1\}$; (ii) on $U_{R_0}\cap\{\|k\|\ge1\}$ every term of the telescoping sum is uniformly integrable with integral $\le C\lambda^aL^K$; (iii) (pointwise boost bound) on $U_{R_0}\cap\{\|k\|\le1\}$, for rows 3, 4, 6: $|f_i-T_{R_0}f_i|\le C(s_{R_0}/t_{R_0})\,g_i$.
- **地位：** 开放：Sterman 与 Collins 幂次计数的积分形式，从未在所有阶以积分形式写出；(iii) 是 boost 论证的逐点形式（它本身只给出标度）。
- **文献：** `Sterman1978a`, `LibbySterman1978a`, `Collins2011` ch. 5.
- **被使用于：** `lem:method-local-accuracy`, `thm:method-template`, `prop:disall-two-routes`, `thm:disall-factorization`, `rem:appE-actual-bound`, `lem:appN-error-table`, `prop:appN-sia`, `thm:appN-structure`, `prop:appO-one-sided`, `thm:appO-main`, `cor:appO-interface`, `prop:appO-tmd` (direct `\uses` users in FINAL_OUTLINE_v2, computed at the merge).
- **解除途径：** an integral version of the Sterman–Collins power counting (sector decomposition per region).
- `\uses{def:method-neighbourhoods, def:method-collinear-approx, def:method-soft-approx}`

#### `asm:appN-separation` — (GA4) 分离性 [\tagA]
- **所属：** App N §N.2. Technical.
- **陈述：** With $t_R=\lambda^{\beta_<(R)}$: on $U_R$ (i) every line of $\mathsf H_R$ has $|l^2-M_l^2|\ge c\,t_R^2$; (ii) every jet line changed by $T_R$ has $|l^+|\ge c\,t_R$ ($B$: $|l^-|$), the region set containing the endpoint assignments that make such lines soft; (iii) for every soft momentum $k$ of $R$ and every $A$-jet line $l=p+k$ it flows through: $|k^+k^-|\ge c\,\mathbf k_T^2$ and $|\tilde D|\ge c(|p^+||k^-|+v_A(p))$, $v_A(p)=|p^+p^-|+\mathbf p_T^2$, $\tilde D=p^2-M_l^2+2p^+k^-+i0$ ($B$ jets with $+\leftrightarrow-$).
- **地位：** 一般情形开放；在单圈三角图中验证；(i) 中的指数 2 是独立假设（Łojasiewicz 型）；(iii) 的第一部分即修正后的无 Glauber 条件 $|k^+k^-|\gtrsim\mathbf k_T^2$（取代常见的"$\kappa\sim|\mathbf k_T|$"说法）。
- **文献：** `Collins2011` §5.5, §10.4 (位置待核实).
- **被使用于：** `lem:method-local-accuracy`, `thm:method-template`, `prop:disall-two-routes`, `thm:disall-factorization`, `lem:appN-error-table`, `prop:appN-sia`, `prop:appN-tmd-window`, `thm:appN-structure`, `prop:appO-one-sided`, `thm:appO-main`, `cor:appO-interface`, `prop:appO-tmd` (direct `\uses` users in FINAL_OUTLINE_v2, computed at the merge).
- **解除途径：** Łojasiewicz inequalities for the Landau varieties of leading regions plus a deformation theorem (App O for the Glauber part).
- `\uses{def:method-neighbourhoods, def:ir-glauber}`

#### `asm:appN-collins` — 一般图的 Collins 条件 [\tagA]
- **所属：** App N §N.3. Technical.
- **陈述：** For every leading-power integrand $\Gamma$ of the process (a single graph, or a family of graphs with a common routing), including multi-direction processes and non-adapted routing, with its meet-closed region set $\mathcal R$ (containing the endpoint assignments required by `asm:appN-separation`): (CS1)$_{R_0}$ and (CS2)$_{R_0}$ of `def:method-collins-conditions` hold for every $R_0\in\mathcal R$, and (CS3) holds.
- **地位：** [A] 层次：Collins 2011 第 10 章断言之（在该章的严格程度下对 Sudakov 形状因子完整：标度陈述）；可证部分：极小 $R_0$ 的 (CS1)（`lem:method-local-accuracy`）、(Com)(Abs) 下化为分组幂次计数（`prop:method-product`）；单圈离壳三角图已完整证明（`prop:appN-triangle-cs`，槽位 X2a；纤维化积分范数 E-N$^\varphi$，`thm:appN-fibered-subtraction`）；一般单圈图与两级梯形图未交付（槽位 X2b、X2c；部分证据 `prop:appN-phi36-dis`、`prop:appN-massive-photon`、`prop:appN-twoloop-remainder`）；障碍：逐项条件为假（`prop:appN-ladder`(c)）、(Abs) 的失效（`rem:method-abs-failure`）、非适配动量分配（`rem:appN-routing`）。CSS 1989 §10.1："there is as yet in the literature no complete and systematic subtraction procedure in QCD … even in the case of deeply inelastic scattering"。
- **文献：** `Collins2011` ch. 10; `CollinsSoperSterman1989` §10.1.
- **被使用于：** `thm:method-subtraction`, `thm:method-template`, `prop:disall-two-routes`, `prop:disall-h5`, `thm:disall-factorization`, `thm:dy-factorization`, `thm:tmd-factorization`, `prop:excl-soft-cancel`, `thm:excl-meson-L`, `prop:appN-sia`, `prop:appN-thrust`, `prop:appN-dy`, `prop:appN-tmd-window`, `thm:appN-structure` (direct `\uses` users in FINAL_OUTLINE_v2, computed at the merge).
- **解除途径：** grouped power counting under (Com)(Abs) at all orders; the fibered programme of `rem:appN-fibered-allorders` (F.1–F.4).
- `\uses{def:method-collins-conditions, def:appN-meet-closed}`

#### `asm:appN-values` — 发散链项的取值规则 [no tag: convention]
- **所属：** App N §N.3. Convention (no grade).
- **陈述：** There is a linear rule $T_c\Gamma\mapsto\langle T_c\Gamma\rangle$ (e.g. raise every denominator changed by an approximator to the power $1+\delta$, continue in $(\varepsilon,\delta)$, then $\delta\to0$) with **(V1)** $\sum_{c:\max c=R}(-1)^{|c|-1}\langle T_c\Gamma\rangle=\int_\Omega C_R\Gamma\,d\mu$ and **(V2)** scaleless chain terms have value zero.
- **地位：** 约定；在单圈三角图中验证（(V1) 由 Feynman 参数延拓，`prop:appN-triangle-exact`(e)）；只用于把减除项的值与区域方法的逐项值等同，不进入任何严格估计。
- **文献：** `Collins2011` §10.8 (zero bins; 位置待核实), `Smirnov2002`.
- **被使用于：** `thm:method-template`, `prop:appN-thrust-zerobin`, `prop:appN-thrust`, `thm:appN-structure`, `prop:appN-triangle-exact`, `prop:appN-twoloop-remainder` (direct `\uses` users in FINAL_OUTLINE_v2, computed at the merge).
- **解除途径：** — (a choice; App P lists it as information, check C-P7).
- `\uses{def:method-subtraction, prop:method-chains}`

#### `asm:appN-cutsum` — 割图求和的公共表示 [\tagA]
- **所属：** App N §N.5. Technical.
- **陈述：** $\sigma[M]=\sum_G\sum_{\mathcal C}\int\Gamma_{G,\mathcal C}M$. **(CU1)** For each forward graph $G$ there are a common domain $\Omega_G$ (light-cone-ordered: minus components integrated by residues for uncut and by $\delta$ functions for cut lines, leaving the plus and transverse components) and an integrand $F_G$ with $\sum_{\mathcal C}\int\Gamma_{G,\mathcal C}M=\int_{\Omega_G}F_G\,d\mu_G$. **(CU2)** The approximators induce linear maps on $F_G$ commuting with the cut sum, and (GA1)–(GA4), (CS1)–(CS3) hold for $F_G$ ($\lambda$ possibly a measured variable). **(CU3)** (event shapes) for all $R$ and $s\in(0,1)$: $\int_{U_R\cap\{|\tau_R-\tau|\le s\tau\}}|F_G|\,d\mu_G\le C\,s\,L^K$.
- **地位：** 一般情形开放；(CU1) 对 DY 型图由 App O 在 `asm:appO-lcopt` 之下提供（`lem:appO-lcopt`, `lem:appO-hard-locality`）。
- **文献：** `Collins2011` §12.8, §14.3 (位置待核实); `Sterman:1995fz`.
- **被使用于：** `prop:method-fsi`, `thm:method-template`, `prop:disall-two-routes`, `thm:disall-factorization`, `thm:dy-factorization`, `prop:appN-sia`, `prop:appN-thrust`, `prop:appN-dy`, `prop:appN-tmd-window`, `thm:appN-structure` (direct `\uses` users in FINAL_OUTLINE_v2, computed at the merge).
- **解除途径：** an LCOPT theorem for general graphs (= discharge of `asm:appO-lcopt`) plus (CU2)(CU3) for the measured quantities.
- `\uses{def:appN-integrand, def:prelim-cut}`

#### `asm:appN-ward-product` — Ward 恒等式的乘积结构与减除的重组 [\tagA]
- **所属：** App N §N.4. Technical.
- **陈述：** At fixed order, after summing all graphs and all attachments of longitudinal and soft gluons: **(WI1)** each chain term's approximated integrand factorizes by the Ward identities (`lem:method-ward-multi`, `prop:method-collinear-wilson`, `prop:method-soft-wilson`) into hard ⊗ collinear matrix elements with Wilson lines ⊗ soft matrix element, and the Ward identities apply equally to integrands already modified by other approximators; **(WI2)** grouped by the order of the $A$-collinear part, $\sum_{\rm graphs,R}C_R\Gamma$ reorganizes into the products used in `prop:tmd-zero-bin-soft`(b) and `thm:appN-structure`.
- **地位：** [A]（`lem:method-ward-multi` 的内容加组合学）；阿贝尔情形与 $n\le2$ 树图 [R]。
- **文献：** `Collins2011` §10.8–§11.3 (位置待核实), `CollinsSoperSterman1989` §5.
- **被使用于：** `thm:method-template`, `prop:disall-factorized-subtraction`, `thm:disall-factorization`, `prop:tmd-zero-bin-soft`, `prop:excl-soft-cancel`, `prop:appN-sia`, `prop:appN-thrust`, `prop:appN-dy`, `thm:appN-structure`, `prop:appO-past-wilson`, `thm:appO-main`, `cor:appO-interface`, `prop:appO-tmd` (direct `\uses` users in FINAL_OUTLINE_v2, computed at the merge).
- **解除途径：** the inductive Ward argument for approximated integrands (App F `prop:appF-induction`) made complete.
- `\uses{lem:method-ward-multi, prop:method-collinear-wilson, prop:method-soft-wilson, def:method-subtraction}`

#### `asm:appN-brst-nonlocal` — 多定域光线算符的 BRST 分类 [\tagC] (named gap; MD1)
- **所属：** App N §N.4. Technical. New entry (§00.3 item 2).
- **陈述：** The BRST-invariant multilocal light-ray operators that appear in the leading-region expansion of Green functions with longitudinal (K) gluon attachments are, modulo BRST-exact operators (class A) and equation-of-motion operators (class B), gauge invariant; classes A and B have vanishing matrix elements between physical states and vanishing insertions into Green functions of gauge-invariant operators at separated points.
- **地位：** Collins 2011 §11.3.2 明确假定（"I will assume the result is true"）；局域算符情形是 Joglekar–Lee 定理（`prop:appJ-local-operators`）；双局域 PDF 算符的矩约化（Ch24 的结果）覆盖重整化部分；多定域情形开放，前沿报告评为 [C]。**合并决定 MD1：** 以 `\tagC` 登记（没有全阶论证；与 `conj:front-brst-multilocal`〔C〕是同一主张）；它只是 `thm:appN-structure` 的前提（该定理的内容等级因此为 [C]）；对 `lem:method-ward-multi`、`thm:method-template` 及各费曼规范过程定理，它是在「地位与缺口」中点名的具名缺口，而不是 `\uses` 前提（WRITER_SPEC_v2 v2.2 §4.6 第 6 条）。
- **文献：** `Collins2011` §11.3.2 (p. 410); `Joglekar:1975nu`, `Joglekar:1976eb`; `Henneaux:1993jn`, `Barnich:2000zw`.
- **被使用于：** `thm:appN-structure` (direct `\uses` users in FINAL_OUTLINE_v2, computed at the merge).
- **解除途径：** multilocal BRST cohomology for light-ray operators (the Ch24 programme on the non-local BRST gap; pointer).
- `\uses{def:appM-alien, prop:appJ-local-operators}`

#### `asm:appN-uv` — 被积函数层次的紫外重整化 [\tagA]
- **所属：** App N §N.5. Technical.
- **陈述：** **(U1)** $\Gamma$ is renormalized at the integrand level — by DR + $\overline{\rm MS}$ with the subtraction of UV subdivergences organized as local integrand counterterms ($R$ operation in DR), or by Zimmermann's forest formula with BPHZ(L) Taylor subtractions **supplemented by the finite non-invariant counterterms that restore the Slavnov–Taylor identities** — so that $\Gamma$ is a single function on $\Omega$ with $\int|\Gamma|$ uniformly bounded near $\varepsilon=0$; graphical Ward identities hold exactly for DR graphs; **(U2)** for every $R$ and every renormalization part $\gamma$, $T_R$ and $t_\gamma$ commute up to polynomials in the external momenta of $\gamma$ that give no leading contribution in the power counting of $T_R$.
- **地位：** 部分证明（线性动量替换；欧氏点）。修正了"BPHZ 与 $\overline{\rm MS}$ 只差有限重整化"的说法。
- **文献：** `Zimmermann1969`, `Breitenlohner:1975hg`, `Breitenlohner:1976te`, `Piguet:1995er`, `Chetyrkin:1982zq`.
- **被使用于：** `thm:method-subtraction`, `thm:method-template`, `prop:disall-factorized-subtraction`, `thm:disall-factorization`, `thm:appN-structure` (direct `\uses` users in FINAL_OUTLINE_v2, computed at the merge).
- **解除途径：** a proof of (U2) for all approximators (projections and eikonalization) at all orders.
- `\uses{def:appN-integrand, thm:prelim-composite-renorm}`

#### `asm:appN-multren` — 共线因子的乘法重整化（维数正规化路线） [\tagA]
- **所属：** App N §N.5. Technical.
- **陈述：** **(Z1)** In moment space the bare collinear factor renormalizes multiplicatively, $f_N^{\rm bare}=Z_Nf_N^{\rm ren}$ (matrix in parton species, $Z_N$ a pure $\overline{\rm MS}$ pole series, independent of the target). **(Z3)** (DR route) For on-shell massless partonic targets with DR as the only IR regulator: (i) the factorization identity holds with the same $\hat{\mathsf H}^{\rm bare}$ as for hadron targets (bare partonic PDFs scaleless, $f^{\rm bare}_{\cdot/j}=\delta$); (ii) $C\equiv\hat{\mathsf H}^{\rm bare}Z$ has no pole at $\varepsilon=0$ (DR mass factorization: the IR poles of the DR partonic forward amplitude are those of $Z^{-1}$). (The item (Z2) of the earlier formulation is the separate entry `asm:appN-ir-regulator`.)
- **地位：** (Z1) 对 PDF 是定理（壳上规范不变局域扭度 2 算符，`thm:prelim-composite-renorm`、`prop:appJ-local-operators`、`thm:pdf-moments-local`），对碎裂函数是独立输入（`rem:pdf-ff-multren`）；(Z3) [A]，(ii) 在 NNLO/N3LO 系数函数的有限性中被验证；在 (Z2) 之下 (Z3)(ii) 由 (Z1)、(Z3)(i) 推出（`thm:disall-renorm-compat`）。
- **文献：** `Collins2011` §8.5, §10.7 (位置待核实); `Collins1984`.
- **被使用于：** `prop:pdf-timelike-dglap`, `thm:method-template`, `thm:disall-renorm-compat`, `prop:disall-h5`, `thm:disall-factorization`, `thm:coll-sia`, `asm:appN-ir-regulator`, `thm:appN-structure` (direct `\uses` users in FINAL_OUTLINE_v2, computed at the merge).
- **解除途径：** (Z1) for FFs (a time-like operator definition with multiplicative renormalization); (Z3)(ii) via (Z2).
- `\uses{thm:pdf-moments-local, prop:pdf-partonic-dr}`

#### `asm:appN-ir-regulator` — 保持 Ward 恒等式的部分子靶红外正规化 [\tagC]
- **所属：** App N §N.5. Technical. Split off from the earlier (Z2) (§00.3 item 1).
- **陈述：** **(Z2)** There exist partonic targets $j$ with an IR regularization (parameter $\lambda$) preserving the Ward identities used in `prop:disall-factorized-subtraction`, such that `prop:disall-two-routes`(a)(b) hold and $f^{\rm ren}_{N,\cdot/j}$ is finite at $\varepsilon=0$ and invertible order by order (as a matrix in parton species).
- **地位：** 真正的输入：离壳外部部分子与 (Z1) 的在壳性矛盾（离壳 PDF 规范相关；BRST/EOM 混合）；胶子质量破坏非阿贝尔 Ward 恒等式；在壳有质量夸克只正规化夸克靶，而矩阵可逆性需要胶子靶；没有已知的保持 Ward 恒等式且正规化在壳胶子共线发散的正规化。部分实现：非单态（夸克）靶；胶子靶只能离壳并加外来抵消项（代价是把 (Z1) 换成离壳形式）。
- **文献：** `Collins:1994ee`, `Hamberg:1991qt`, `Falcioni:2022fdm`, `Gehrmann:2023ksf`.
- **被使用于：** `thm:disall-renorm-compat` (direct `\uses` users in FINAL_OUTLINE_v2, computed at the merge).
- **解除途径：** construct such a regulator, or carry out the off-shell route with alien operators at all orders.
- `\uses{asm:appN-multren}`

#### `asm:appN-tmd` — TMD 输入 [\tagA]
- **所属：** App N §N.5. Technical.
- **陈述：** For SIDIS, $e^+e^-\to h_1h_2X$ and DY in the TMD region ($y_A=-y_B=Y$, approximators `def:appN-tmd-approx`): **(T1)** tails — constants $a>0$, $c_1\ge c_0>1+2a$, $J$ such that for $c_0L\le Y\le c_1L$, on every $U_R$ and on the subset where some soft or collinear line has $|\mathbf k_T|\le\lambda^{1+a}$, the integral norm of integrand minus approximants is $O(\lambda^aL^KY^J)$, and the constants of (CS1)(CS2) grow at most like $Y^J$; **(T2)** asymptotic linearity in $b$ space — $\ln\tilde S(y_1,y_2)=a_S+(y_1-y_2)\tilde K+O(e^{-(y_1-y_2)})$, $\ln\tilde f_A^{\rm unsub}(y_B)=\alpha_A-y_B\tilde K+O(e^{y_B-y_{P_A}})$ with the same slope $\tilde K$; **(T3)** $b$-space multiplicative renormalization $\tilde f^{\rm bare}=Z_{\rm TMD}(\mu,\zeta)\tilde f^{\rm ren}$, soft-factor renormalization by the cusp anomalous dimension; **(T4)** in the combination divided by the soft factor, $y_B\to-\infty$ ($y_A\to+\infty$) can be taken under the integral.
- **地位：** 单圈验证（c_tmd：$Y\coth Y$、斜率相等、$\sigma$ 与 $y_B$ 相消；VF-TMD-1, VF-TMD-8）；所有阶 [A]。类空正规子线的自能需约定（VF-REF-19）。
- **文献：** `Collins2011` ch. 13 (位置待核实), `CollinsSoperSterman1985a`, `AybatRogers2011`.
- **被使用于：** `prop:tmd-zero-bin-soft`, `thm:tmd-factorization`, `prop:tmd-evolution`, `prop:appN-tmd-window`, `thm:appN-structure` (direct `\uses` users in FINAL_OUTLINE_v2, computed at the merge).
- **解除途径：** all-order proofs of (T2) (the CS equation from the operator definitions) and of the tail estimate (T1).
- `\uses{def:appN-tmd-approx, def:tmd-unsub, def:tmd-soft}`

#### `asm:appN-endpoint` — 端点条件 [\tagA]
- **所属：** App N §N.6. Technical.
- **陈述：** For every graph of the pion form factor (and of the meson side of $\gamma_L^*$ meson production), at each order: **(E1)** integrating the meson-jet subgraph over its internal loop momenta at fixed fraction $x$ (with absolute values), $|J|(x)$ satisfies $\int_0^t|J|(x)dx+\int_{1-t}^1|J|(x)dx\le C\,t\,L^K$ for $0<t<1$; **(E2)** the hard kernel is at most $1/x$, $1/\bar x$ singular at the endpoints; **(E3)** $\int_\Omega|C_{R_{\rm end}}\Gamma|\,d\mu\le C\lambda^aL^K$ and $C_R\Gamma\in\mathfrak S(U_{R_{\rm end}})$ for every $R>R_{\rm end}$.
- **地位：** 对有限 Gegenbauer 截断成立；对非微扰 DA 是假设；对横向光子与扭度 3 不成立（`prop:excl-soft-cancel`(c)）。
- **文献：** `LepageBrodsky1980`, `EfremovRadyushkin1980` (keys as in the core outline), `CollinsDiehl2000`, `Mankiewicz:1999tt`.
- **被使用于：** `prop:excl-soft-cancel`, `thm:excl-pion-ff`, `thm:excl-meson-L`, `thm:appN-structure` (direct `\uses` users in FINAL_OUTLINE_v2, computed at the merge).
- **解除途径：** the endpoint behaviour of partonic DAs at all orders (Sudakov suppression of endpoint regions).
- `\uses{def:appN-excl-approx, def:method-collins-conditions}`

#### `asm:appN-lce` — 光锥序表示与协变值的等同（LCE） [\tagA]
- **所属：** App N §N.7 (fibered framework). Technical. New in v2.3 (X2 verification).
- **陈述：** For every graph $G$ of the scalar models (M1), (M2) that satisfies the hypotheses of `lem:appN-lc-positivity` and the infrared-finiteness condition (IRF) — its (renormalized) parametric integral converges absolutely for every $\varepsilon\in[0,\varepsilon_0]$ —, the fibered value equals the covariant value: $\int_B\rho_G\,d\mu_\varepsilon=I_G$ (condition (FI) of `def:appN-fibered`).
- **地位：** [A]：对每个检验了 (FR) 的图由 `lem:appN-identification` 证明；作为对所有图的陈述开放（光前微扰论与协变微扰论的等价）。
- **文献：** `Ligterink:1994tm`, `Schoonderwoerd:1998qj`, `Schoonderwoerd:1998iy` (equivalence of light-front and covariant perturbation theory).
- **被使用于：** `cor:appN-cs3-fibered` (direct `\uses` users in FINAL_OUTLINE_v2, computed after the verify patch).
- **解除途径：** a general proof of (FI) for the scalar models.
- `\uses{def:appN-fibered, lem:appN-lc-positivity}`

#### `asm:appN-analytic-reg` — 两圈图样积分的辅助解析正规化 [\tagA]
- **所属：** App N §N.7 (two-loop planar vertex). Technical. New in v2.3 (X2 verification).
- **陈述：** Two-loop planar vertex of (M1), each line raised to an independent power $1+\delta_l$. **(RA1)** the analytically regularized pattern integrals are meromorphic in $(\varepsilon,\delta)$; **(RA2)** the nine single-approximator integrals $\int T_R\Gamma$ are regular at $\delta=0$ for $\varepsilon$ in a punctured neighbourhood of 0, and their $\delta\to0$ limits are their dimensionally regularized values.
- **地位：** [A]：解析重整化对二次传播子证明了 (RA1)，但不覆盖程函型线性因子。
- **文献：** `Smirnov2002` (analytic regularization of Feynman integrals).
- **被使用于：** `prop:appN-twoloop-remainder` (direct `\uses` users in FINAL_OUTLINE_v2, computed after the verify patch).
- **解除途径：** meromorphy of analytically regularized integrals with linear (eikonal-type) factors.
- `\uses{prop:appN-twoloop-algebra}`

### 3.4 Owner App O

#### `asm:appO-lcopt` — 光锥序微扰论的适用性 [\tagA]
- **所属：** App O §O.2 (`sec:appO-lcopt`). Technical.
- **陈述：** For a DY leading region $R$ and $J=J_A$ (likewise $J_B$), with $V_H$, $V_H^\dagger$ and the cut: **(i)** (zero modes, endpoints, truncation) on $U_R$, in the integral norm, the regularized Feynman integral of $J$ equals, up to $O(\lambda^a)$, the iterated integral "all internal minus components over $\mathbb R$ at fixed plus and transverse components (`lem:appO-lcopt`, `lem:appO-numerators`), then plus and transverse components over $\{l^+\ne0\}$"; distributions concentrated at $l^+=0$ and endpoint contributions of plus integrals are absent at leading power; the minus-component restriction of `def:method-neighbourhoods` can be dropped (removed tail $O(\lambda_J/\lambda^\beta)$). **(ii)** (instantaneous loops) there is an assignment of the one-dimensional integrals of `lem:appO-numerators`(v) (depending only on plus and transverse components; distributions at $l^+=0$ allowed) for which the minus integral equals the expansion of `lem:appO-numerators`.
- **地位：** 开放；光前文献中有部分结果（好分量流的零模不贡献；具体图中光前与协变微扰论的等价）；早先表述中的第 (iii) 项（割图规则的 Hermite 性）由 `lem:appJ-cut-hermiticity` 给出（v2.3 修正其陈述：最大时间圈规则下对每个实系数顶点、含鬼场顶点成立；逐顶点的"物理 $\mathcal M^*$"读法对鬼场不成立，只在对鬼圈两种走向求和后一致），不再是假设。无论 (ii) 的取值如何，它们都与所有负分量能量无关，故所有极点论证与之无关。
- **文献：** `Kogut:1969xa`, `Chang:1973qi`, `Brodsky:1997de` (zero modes, Z-graphs), `Ligterink:1994tm` (equivalence; minus integrals), `Collins:2018aqt` (light-front vacuum), `Schoonderwoerd:1998qj`, `Schoonderwoerd:1998iy` (covariant vs light-front perturbation theory).
- **被使用于：** `prop:method-fsi`, `lem:dy-fsi`, `thm:dy-factorization`, `prop:break-measurement`, `lem:appO-hard-locality`, `lem:appO-unitarity`, `prop:appO-ss-localize`, `lem:appO-side-independent-windows`, `prop:appO-ss-cancel`, `prop:appO-twoexch-spectator`, `prop:appO-one-sided`, `thm:appO-main`, `cor:appO-interface`, `prop:appO-tmd` (direct `\uses` users in FINAL_OUTLINE_v2, computed at the merge).
- **解除途径：** a theorem on the equivalence of light-cone-ordered and covariant perturbation theory including UV renormalization and zero modes at all orders.
- `\uses{lem:appO-lcopt, lem:appO-numerators, def:method-neighbourhoods}`

#### `asm:appO-envelope` — 纤维积分误差的可积包络 [\tagA]
- **所属：** App O §O.6 (`sec:appO-rewriting`). Technical; Glauber specific.
- **陈述：** For each leading region $R$ there is $\hat\Phi_R\ge0$ on $U_R$, independent of the localized soft components, with $\int_{U_R}\hat\Phi_R\,d\hat\mu\le CL^K$ uniformly in $\varepsilon\in(0,\varepsilon_0]$ and in the $i0$ regulator $\eta_0$, such that for $\Gamma$ and every chain term $T_c\Gamma$: (i) the fibre-integration error of each unit localization (the SS localization of `prop:appO-ss-localize`, the remainder of `lem:appO-equal-time`(iii), the remainder of `lem:appO-joint-localization`(b), truncation terms at fibre endpoints), with the other $i0$ replaced by $i\eta_0$, is bounded pointwise by $C\lambda^a\hat\Phi_R$; (ii) on boundary layers of relative width $\lambda^a$ — including fibre endpoints set by neighbourhoods $N_{R'}$ with $\beta_{R'}>\beta_R$ — $\int\hat\Phi_R\le C\lambda^aL^K$. **For coincident connections the bounds are imposed on side-summed families** (v2.3: within the class of `prop:appO-pergraph-weights` the per-graph version cannot hold; for graph-generated jets the per-graph question is open).
- **地位：** 开放；(GA3) 的纤维积分版本，必须处理其余变量中残留的夹挤；在任何阶都未证明；在 DIS 与 $e^+e^-$ 中不需要；对重合连接只能对按侧求和的族成立（`prop:appO-pergraph-weights`）。
- **文献：** — (formulated here; cf. `Collins2011` §14.4.8 for the remaining issues).
- **被使用于：** `prop:method-glauber-deformation`, `prop:dy-deformation`, `thm:dy-factorization`, `asm:appO-mixing`, `prop:appO-one-sided`, `thm:appO-main`, `cor:appO-interface`, `prop:appO-tmd` (direct `\uses` users in FINAL_OUTLINE_v2, computed at the merge).
- **解除途径：** the fibre version of the integral power counting.
- `\uses{def:appO-rewriting, def:appO-windows}`

#### `asm:appO-mixing` — Glauber–软混合与重合连接的完整图集相消 [\tagA]
- **所属：** App O §O.6 (statement placed after `asm:appO-envelope`). Technical; Glauber specific.
- **陈述：** $\Gamma$ a DY forward graph, $R$ a leading region, windows as in `def:appO-windows`, $\hat\Phi_R$ as in `asm:appO-envelope`. **(a′)** (pre-integration localization with envelope bounds; replaces the earlier half-plane splitting clause (a), v2.3) localization is performed before the integration over the internal loops of $S$, pointwise outside the exceptional sets $E_j$ of `lem:appO-preintegration-localization`; assumed: envelope bounds $C\lambda^aL^K$ (i) for the $S$-loop integral of the absolute localization error, including the factor $\sum_\sigma|w_\sigma(p)|$ when there are several insertions, and (ii) for the unlocalized integrand on the $E_j$ — these bounds also justify the Fubini interchange; same for $J_B$. **(b)** (cut compatibility of $S$) after the localization of (a′) the cut sum of $J_A\otimes J_B\otimes S$ takes the closed-time-path form of `lem:appO-unitarity` with $S$'s fields as $\langle0|\bar{\rm T}\{\cdots\}{\rm T}\{\cdots\}|0\rangle$, and the $\tau=0$ insertions with both ends on spectators (also through $S$) assemble into operators on $\mathcal H_A\otimes\mathcal H_B\otimes\mathcal H_S$. **(c)** (complete graph set) for the set $\mathfrak G$ of all forward graphs of the given order with the given $J_A$, $J_B$ (closed under adding soft three- and four-gluon vertices between Glauber and soft lines, including real soft emission through Lipatov-type vertices), summed over all coincident connections and side assignments, combining the window with the adjacent near-on-shell soft region of $U_R$ (including real emission), the contribution after the integration map $\mathfrak P$ is $O(\lambda^aL^K)$ in the weak sense of `def:appO-weak-equivalence`; equivalently $\mathcal W'^\dagger\mathcal W=1+O(\lambda^a)$ on spectator states at $\tau=0$. (The per-graph fixed-order clause (c1) of the earlier formulation is deleted; joint localization is `lem:appO-joint-localization`.)
- **地位：** (a′)(b) 对 $\mathcal G_0$ 自动成立（只有连接线自身的极点；$S$ 为空）；(c) 在阿贝尔理论与只有非重合连接的阶成立（`prop:appO-ss-cancel`），对程函线之间的双胶子交换在 $O(g^4)$ 成立（`prop:dy-eikonal-twogluon`）；对复合旁观者，在全局两时模型中全重合 $O(g^4)$ 族的未割线部分逐点相消（`prop:appO-twoexch-spectator`，模型定理，作为 QCD 陈述为 [P]；槽位 X1f 部分完成）；被割的直接线（`rem:appO-cut-ss`）、共线端点处的半重合模式、$O(g^6)$（`prop:appO-g6-ladder`，直接线梯形图类在幺正性下不封闭）与重合 SA/AS 插入开放；槽位 X1a、X1b、X1e 未交付。证据（非证明）：Lindsay–Ross–Sachrajda 两圈旁观者相消、Brandt–Frenkel–Taylor 程函介子模型、Rothstein–Stewart 的正规化给出共同时序、Schwartz–Yan–Zhu（纯 Glauber 梯形图对单尺度可观测量相消）。
- **文献：** `CollinsSoperSterman1988`, `Collins2011` §14.3–§14.4 (outline), `AybatSterman2009`, `RothsteinStewart2016`, `Lindsay:1982pu`, `Lindsay:1983ny`, `Lindsay:1983dt`, `Brandt:1988xt`, `Schwartz:2018obd`, `Meggiolaro:1996hf`.
- **被使用于：** `prop:method-glauber-deformation`, `prop:dy-deformation`, `thm:dy-factorization`, `lem:tmd-glauber`, `thm:tmd-factorization`, `prop:appO-one-sided`, `thm:appO-main`, `cor:appO-interface`, `prop:appO-tmd` (direct `\uses` users in FINAL_OUTLINE_v2, computed after the verify patch).
- **解除途径：** an all-order unitarity argument for the complete graph set including the cut direct lines and the Lipatov-vertex graphs; the matching `asm:appO-collinear-ends` for the coincident $O(g^4)$ patterns.
- `\uses{def:appO-windows, def:appO-family, def:appO-weak-equivalence, asm:appO-envelope, lem:appO-unitarity, lem:appO-equal-time, lem:appO-preintegration-localization}`

#### `asm:appO-deformation` — 一般构型、相容性、软角区与 H-发射端点 [\tagA]
- **所属：** App O §O.7 (`sec:appO-deformation`). Technical; Glauber specific.
- **陈述：** For any $\Gamma$, $R$, $F=\tilde F_{\Gamma,R}$: **(a)** a deformation target (`def:appO-target`(a)–(c)) exists, given on each two-leg-type component by a Glauber flow (two separately conserved flows on localized legs, the localized component's imaginary part at most half the carrier width) plus internal deformations of $S$, with the sign condition of `lem:appO-no-crossing`(a), $|q_e^+||q_e^-|\ge cq_{Te}^2$ on legs, no denominator of $S$ crossed, and single-leg-type components moved in the component their jet does not see; **(b)** the target is compatible with $\mathfrak B$ (`def:appO-target`(d)); **(c)** on the soft-angle region — including the out-of-window parts of the side-independent windows and the wee-line endpoint region of `lem:appO-side-independent-windows`(c); the window-edge terms themselves vanish identically (v2.3) —, (CS1)$_R$ and (CS2)$_R$ hold for the rewritten forms: $\int_{h_1(U_R)}\big(1-\prod_u\Theta'_u\big)\big(|\mathfrak r_R(1-T_R)X_R[F_\Gamma]|+\sum_{R'\not\le R}|\mathfrak r_RC_{R'}F_\Gamma|\big)d\mu_\Omega\le C\lambda^aL^K$; **(d)** for regions with H-emission endpoints and for coincident SA/AS insertions (ordering weights continuous but not analytic at $k^+=0$, `lem:appO-joint-localization`(d); the dominant region $|k^+_{\rm SA}|\sim\lambda_B$, `rem:appO-h-emission`), a weakly equivalent rewriting exists in which each uncut soft momentum appears in each jet only in denominators of one orientation or only in carriers, with a deformation target such that `prop:appO-eikonal` and `prop:appO-past-wilson` hold.
- **地位：** (a) 对 $\mathcal G_0$ 与分级构型已证（`prop:appO-target`）；窗口边缘项在与侧无关的窗口下恒为零（`lem:appO-side-independent-windows`，槽位 X1c 通过）；开放：近壳携流线（两个相近软动量之差）导致 (GC2) 失效、(GC3) 失效、两类被排除的分量；**(b)(c)(d) 即使对阿贝尔 $\mathcal G_0$ 也需要**（槽位 X1d 未交付）——在截面层次 DY 的 Glauber 相消没有任何部分是无条件的。(c) 包括真正软尺度 $\lambda^2(1,1,1)$ 的旁观者耦合（领头幂次）与窗口外部分、wee 线端点区。
- **文献：** `CollinsSoperSterman1988`, `Collins2011` §14.4.8, `AybatSterman2009`.
- **被使用于：** `prop:method-glauber-deformation`, `prop:dy-deformation`, `thm:dy-factorization`, `lem:tmd-glauber`, `prop:appN-dy`, `thm:appO-main`, `cor:appO-interface`, `prop:appO-tmd` (direct `\uses` users in FINAL_OUTLINE_v2, computed at the merge).
- **解除途径：** compatibility for $\mathcal G_0$ with a window-adapted set algebra; a soft-scale treatment of spectator couplings; a common treatment of H-emission endpoints and coincident SA/AS insertions (analyticity of the ordering weights in the dominant region).
- `\uses{def:appO-target, def:appO-rewriting, def:appO-graded, prop:appO-ss-cancel, lem:appO-side-independent-windows}`

#### `asm:appO-rewritten-cs` — 改写形式与族求和形式的 Collins 条件 [\tagA]
- **所属：** App O §O.8 (`sec:appO-wilson`). Technical; Glauber specific (split off from the generic (CS) input).
- **陈述：** (CS1)$_R$ and (CS2)$_R$ of `def:method-collins-conditions` hold for the rewritten forms $\mathfrak r_R(\cdot)$ and for the family-summed forms $\sum_{\mathfrak F}\mathfrak P[\cdot]$ on $h_1^{(R)}(U_R)$, including (i) the term-by-term matching of the localized spectator terms (plus the $(1-T_R)$ errors) with the external-endpoint distributions at $n_A\cdot K_i=0$ that fixes the Wilson-line prescription (past pointing), and (ii) the allocation of localized SA/AS endpoints between the region $R$ and the $A$-collinear region $R'$ (the $A$-end Glauber recoil is not reproduced by $T_R$; the overlap is the zero bin).
- **地位：** 开放；Glauber 特有（DIS 与 $e^+e^-$ 中不存在）；对共线 PDF 无害（Wilson 线方向无关），对 TMD 是实质性的（订书钉方向、Sivers 符号）。
- **文献：** `Collins2002`, `Collins2011` §14.4, `CollinsSoperSterman1988`.
- **被使用于：** `prop:method-glauber-deformation`, `prop:dy-deformation`, `thm:dy-factorization`, `lem:tmd-glauber`, `thm:tmd-factorization`, `prop:appN-dy`, `prop:appO-past-wilson`, `thm:appO-main`, `cor:appO-interface`, `prop:appO-tmd` (direct `\uses` users in FINAL_OUTLINE_v2, computed at the merge).
- **解除途径：** one- and two-loop checks of the past-pointing prescription for DY and of the future-pointing one for SIDIS (Ch14 material), then a general proof.
- `\uses{def:method-collins-conditions, def:appO-rewriting, def:appO-family}`

#### `asm:appO-adjacent-swap` — 相邻交换对称性（ADJ） [\tagP]
- **所属：** App O §O.5 (model theorems). Technical. New in v2.3 (X1 verification).
- **陈述：** Every leading-power cut-summed LCOPT jet factor $J_X$ ($X=A,B$) of QCD graphs with two amplitude-side insertions on spectator partons satisfies (ADJ) of `def:appO-sectors`: two sectors of one jet that differ only by the order of two adjacent operations among (insertion 1, insertion 2, $V_H$) have their terms with a single-state gap between the two operations in bijection, with equal coefficients and equal other gap functions.
- **地位：** [P]：在标量旁观者模型（`ex:dy-spectator-lcopt`）中精确成立；对自旋求和的领头幂次 LCOPT 喷注只有论证，没有证明。只进入 App O 模型定理的 QCD 转移（这些定理作为 QCD 陈述为 [P]），不是 `thm:appO-main` 或 `thm:dy-factorization` 的前提。
- **文献：** — (formulated here; `verify/extend_reports/X1-glauber_final.md`).
- **被使用于：** `prop:appO-twoexch-spectator`, `prop:appO-pergraph-weights`, `prop:appO-halfcoinc-sensitivity` (direct `\uses` users in FINAL_OUTLINE_v2, computed after the verify patch).
- **解除途径：** a proof for leading-power cut-summed LCOPT jets (numerator structure of `lem:appO-numerators`).
- `\uses{def:appO-sectors}`

#### `asm:appO-real-jets` — 旁观者喷注函数的实性（REAL） [\tagP]
- **所属：** App O §O.5 (model theorems). Technical. New in v2.3 (X1 verification).
- **陈述：** (REAL) of `def:appO-sectors` holds for the leading-power cut-summed LCOPT jet factors of QCD graphs with spectator insertions: every colour-stripped jet function is a fixed phase times a rational function with real coefficients.
- **地位：** [P]：在标量旁观者模型中精确成立；对自旋求和的 QCD 喷注只有论证；只进入模型定理的 QCD 转移。
- **文献：** — (formulated here; `verify/extend_reports/X1-glauber_final.md`).
- **被使用于：** `prop:appO-twoexch-spectator`, `prop:appO-pergraph-weights`, `prop:appO-halfcoinc-sensitivity` (direct `\uses` users in FINAL_OUTLINE_v2, computed after the verify patch).
- **解除途径：** a proof for leading-power cut-summed LCOPT jets.
- `\uses{def:appO-sectors}`

#### `asm:appO-collinear-ends` — 共线端点的匹配 [\tagA]
- **所属：** App O §O.5 (model theorems). Technical; Glauber specific. New in v2.3 (X1 verification).
- **陈述：** The SS windows carry the two-sided analytic rapidity regulators of `def:appO-regulator-class`(c); the complements — the $A$-collinear end ($|k^+|\gtrsim K^+$) and the $B$-collinear end ($|k^-|\gtrsim K^-$), together with the cut contributions located there — are assigned to the collinear regions, where collinear factorization (Wilson lines and subtraction terms) reproduces them with no leftover Hermitian $C_AX$ term (fully coincident pattern) and no leftover $[X_1,X_2]$ term (half-coincident pattern).
- **地位：** 开放，[A]：它把 `asm:appO-mixing`(c) 对重合 $O(g^4)$ 模式的内容**转移**而非消去；半重合部分在模型中只用 $k^-$ 正规子即已证明（`prop:appO-halfcoinc-sensitivity`）；被割的直接线贡献在共线端点处未被计算（`rem:appO-cut-ss`）。不是 `thm:appO-main` 或 `thm:dy-factorization` 的前提；`Zhou:2017his` 可读作其 EFT 形式（我们不接受其关键步骤为证明）。
- **文献：** `Zhou:2017his`, `Liu:2008cc`, `RothsteinStewart2016`, `Collins2011` §14.4.
- **被使用于：** `prop:appO-twoexch-spectator`, `prop:appO-twoexch-regulated`, `prop:appO-halfcoinc-sensitivity` (direct `\uses` users in FINAL_OUTLINE_v2, computed after the verify patch).
- **解除途径：** compute the cut direct-line contributions at the collinear ends or prove their suppression with the two-sided regulators (`rem:appO-cut-ss`); then the matching itself.
- `\uses{def:appO-regulator-class, def:appO-glob-model}`

### 3.5 Owner Ch22 `lamet` (reproduced verbatim from FINAL_OUTLINE_v2 Part VII annex §F1.1, the owner's binding text)

#### `asm:lamet-aux-renorm` — 含类空辅助静态色源的 QCD 的可重整性 [\tagA]
- **所属：** Ch22 `sec:lamet-renorm`. Technical.
- 陈述：(AX1)–(AX3) of the Ch22 entry (auxiliary colour-triplet spinless Grassmann field $Q$ along $\hat n=\hat e_z$; renormalizability of the extended theory with $Z_Q$, $Z_1^{QQg}$ (tied to $Z_g$) and $\delta m$ only, BRST-invariantly; constant $Q$ determinant in DR).
- 地位：[A]-level — asserted in `Ji:2017oey` (the space-like extension of the HQET renormalizability argument is stated, not written), supported by the lattice auxiliary-field construction of `Green:2017xeu` and the coordinate-space degree counting of `Ishikawa:2017faj` (superficial degrees and "bookkeeping forests", not a BPHZ proof); explicit checks: two loops `Ji:2015jwa`, three-loop anomalous dimension `Braun:2020ymy`, heavy–light current to three loops `Chetyrkin:2003vi`. Decision D3 / A26: the multiplicative renormalizability of space-like Wilson-line operators is [A] in this book.
- 文献：`Ji:2017oey`, `Green:2017xeu`, `Ishikawa:2017faj`, `Dorn:1986dt`, `Dotsenko:1979wb`, `Braun:2020ymy`, `Chetyrkin:2003vi`.
- 被使用于：`prop:lattice-renormalizability`, `asm:lamet-ope`, `asm:lamet-gap`, `conj:lamet-decay-qcd`, `asm:lamet-staple`, `thm:yzliu-soft-hqet` (direct `\uses` users in FINAL_OUTLINE_v2, computed at the merge).
- 解除途径：a written BRST-invariant renormalization proof of QCD + space-like static source (Zimmermann/BPHZ with the anisotropic power counting of the propagator $\theta(x^z)\delta(x^0)\delta^2(x_\perp)$, or flow equations in the style of `Frob:2015uqy`), including the treatment of $\det(i\hat n\cdot D)$ and of $\delta(0)$-type terms.
- `\uses{def:prelim-qcd, def:prelim-brst, def:prelim-wilson}`.

#### `asm:lamet-ope` — 类空 Wilson 线算符的短距离 OPE（重整化微扰论） [\tagA]
- **所属：** Ch22 `sec:lattice-matching`. Technical.
- 陈述：(OP1) the leading-twist light-ray OPE of the renormalized operator $O^R_{\gamma^\alpha}(z,\mu)$ as $z^2\to0$ at fixed $\lambda$, with traceless symmetric twist-2 quark and gluon operators and coefficients $C_n$, $C'_n$; (OP2) for massless on-shell partonic states the leading-twist expression holds for all $z$ order by order.
- 地位：[A] — argued by `IzubuchiEtAl2018` (read) from the auxiliary-field localization (the non-local operator becomes a product of local operators of the extended theory) plus the standard OPE; no Zimmermann-level theorem for Wilson-line operators is known — wording 「据我们截至 2026 年 10 月的文献检索，尚未见……」 (A06). The remark under `tab:lamet-dependency` lists what a proof needs.
- 文献：`IzubuchiEtAl2018` §II, `Radyushkin2017`, `Braun:2007wv`, `Ji:2017oey`.
- 被使用于：`thm:lamet-coordinate`, `thm:lamet-parton-momentum`, `prop:lamet-tmc`, `prop:lamet-sdf`, `thm:lamet-quasi-gpd` (direct `\uses` users in FINAL_OUTLINE_v2, computed at the merge).
- 解除途径：Zimmermann's forest formula for the extended theory with the anisotropic power counting; or a flow-equation OPE theorem (cf. `Frob:2016mzv`) extended to theories with a static auxiliary field.
- `\uses{prop:lattice-renormalizability, asm:lamet-aux-renorm, def:dis-twist}`.

#### `asm:lamet-uniform` — 扭度展开对 Ioffe 时间的一致性 [\tagC]
- **所属：** Ch22 `sec:lamet-power`. Technical.
- 陈述：(UI-a) coordinate form — the twist-2 remainder of the hadronic ITD is bounded by $K(-z^2)\Lambda^2(1+|\ln(-z^2\mu^2)|)^k$ uniformly in $\lambda$ for $0<-z^2\le z_0^2$; (UI-b) ray form — along $z^2=-\lambda^2/P_z^2$, $|\lambda|\le z_0P^z$, the remainder beyond twist 4 has Fourier transform $o(P_z^{-2})$ at fixed $x\in(0,1)$.
- 地位：[C] — no all-order argument; evidence from the renormalon model (`prop:lamet-bvz`) and from solvable models; Liu's Gross–Neveu theorem covers only imaginary Ioffe time (`thm:yzliu-gn-convergence`, Ch23). The frontier report's hypothesis was reformulated (writer note in the Ch22 entry): a pointwise bound of type (UI-a) does not give a $P^z$-suppressed Fourier transform.
- 文献：`IzubuchiEtAl2018`, `Braun:2018brg`, `JiEtAl2021`.
- 被使用于：`thm:lamet-hadronic` (direct `\uses` users in FINAL_OUTLINE_v2, computed at the merge).
- 解除途径：a non-perturbative OPE with remainder bounds uniform in $\lambda$ (cf. `asm:intro-np-ope`); as a first step a model proof at real Ioffe time.
- `\uses{thm:lamet-coordinate, prop:lamet-tmc}`.

#### `asm:lamet-twist4` — 领头幂次修正的结构（扭度 4） [\tagC]
- **所属：** Ch22 `sec:lamet-power`. Technical.
- 陈述：(TW1) $\tilde h_{\rm tw4}=z^2\Lambda^2\int_{-1}^1d\alpha\,e^{i\alpha\lambda}\rho_4(\alpha,z^2)$ with $\rho_4$ supported in $[-1,1]$, smooth inside; (TW2) at most logarithmic $z^2$ dependence of $\rho_4$.
- 地位：[C] — the form is suggested by the twist-4 OPE in perturbation theory (support as in `prop:lamet-support`), the hadronic structure is assumed.
- 文献：`Braun:2018brg`, `Radyushkin2017`, `JiEtAl2021`.
- 被使用于：`asm:lamet-large-z`, `thm:lamet-hadronic` (direct `\uses` users in FINAL_OUTLINE_v2, computed at the merge).
- 解除途径：a twist-4 OPE for hadron matrix elements with control of the $z^2$ dependence (non-perturbative OPE).
- `\uses{prop:lamet-support, cor:lamet-entire}`.

#### `asm:lamet-large-z` — 大距离区域的控制 [\tagC]
- **所属：** Ch22 `sec:lamet-power`. Technical.
- 陈述：(LZ1) the region $|\lambda|>z_0P^z$ contributes $o(1)$ to the Fourier transform of $\tilde h-\tilde h_{\rm tw2}$ at fixed $x\in(0,1)$; (LZ2) the same with $\tilde h-\tilde h_{\rm tw2}-\tilde h_{\rm tw4}$ is $o(P_z^{-2})$.
- 地位：[C] — requires large-distance control of hadronic Wilson-line correlators with constants uniform in $P^z$; `thm:lamet-exp-decay` gives decay under `asm:lamet-gap` but no usable constants; `conj:lamet-decay-qcd`.
- 文献：`Ji:2026vir` (预印本), `JiEtAl2021`, `Gao:2021dbh`.
- 被使用于：`thm:lamet-hadronic` (direct `\uses` users in FINAL_OUTLINE_v2, computed at the merge).
- 解除途径：quantitative exponential decay of hadronic matrix elements with constants uniform in $P^z$.
- `\uses{thm:lamet-coordinate, asm:lamet-twist4}`.

#### `asm:lamet-gap` — 谱隙与边界值正则性 [\tagC]
- **所属：** Ch22 `sec:lamet-fourier`. Technical.
- 陈述：(GP1) isolated one-particle external state, other contributing states at least $\Delta m$ above it; (GP2) Fredenhagen-type regularity of the boundary values of the ordered two-point functions in complex time; (GP3) QCD application: non-perturbative reduction of the Wilson-line operator to local operators of QCD + static source and a gap $\Lambda_X$ above the static threshold.
- 地位：[C] for QCD — (GP1), (GP2) are standard axiomatic hypotheses for the channel considered; (GP3) needs confinement in the heavy–light sector and a non-perturbative version of `asm:lamet-aux-renorm`; lattice values ($\Lambda_X\approx0.5$ GeV) are evidence only.
- 文献：`Ji:2026vir` §5 (预印本, read), `Fredenhagen:1984bz`.
- 被使用于：`thm:lamet-exp-decay`, `conj:lamet-decay-qcd` (direct `\uses` users in FINAL_OUTLINE_v2, computed at the merge).
- 解除途径：(GP1), (GP2) in a constructive or axiomatic setting for the channel; (GP3) requires control of confinement — beyond present methods.
- `\uses{asm:lamet-aux-renorm}`.

#### `asm:lamet-staple` — 订书钉形类空 Wilson 线算符的重整化与 $L\to\infty$ 极限 [\tagA]
- **所属：** Ch22 `sec:lattice-tmd`. Technical.
- 陈述：(ST1) multiplicative renormalizability of the staple operator divided by $\sqrt{Z_E}$ with end-point factors only; (ST2) existence of $L\to\infty$ order by order (pinch poles cancel against $\sqrt{Z_E}$; ultrasoft modes cancel after resummation of dipole self-interactions); (ST3) on the lattice $\sqrt{Z_E}$ plus the short-distance matrix element removes all UV divergences; same-dimension mixing as in `prop:lattice-renormalizability`(b).
- 地位：[A]-level — argued to all orders (Ch23 `prop:yzliu-pinch-ultrasoft` gives the all-order argument for (ST2), itself [A] with the ultrasoft cancellation argued, not proven); explicit one-loop checks; lattice renormalization studies.
- 文献：`Ji:2019ewn`, `Liu:2022nnk` §§3–4, `Ebert:2022fmh`, `Ebert:2019tvc`, `Constantinou:2019vyb`, `Alexandrou:2023ucc`; history `Collins:2008ht`, `Ji:2018hvs` (A04).
- 被使用于：`def:lamet-quasi-tmd`, `thm:lamet-quasi-tmd`, `prop:yzliu-qtmd-powercount` (direct `\uses` users in FINAL_OUTLINE_v2, computed at the merge).
- 解除途径：the auxiliary-field renormalization proof (as for `asm:lamet-aux-renorm`) for staples with cusps, plus an all-order treatment of ultrasoft and "ultra-ultrasoft" modes.
- `\uses{asm:lamet-aux-renorm, def:prelim-wilson}`.

#### `asm:lamet-soft-rapidity` — 离光锥软函数的大快度结构 [\tagA]
- **所属：** Ch22 `sec:lattice-tmd`. Technical.
- 陈述：(SR) $\ln S(b_\perp,\mu,Y,Y')=(Y+Y')\tilde K(b_\perp,\mu)+\mathcal D(b_\perp,\mu)+O(e^{-(Y+Y')})$ with $\tilde K$ the Collins–Soper kernel.
- 地位：[A]-level — the all-order argument is Ch23 `prop:yzliu-rapidity-linear` (complete except an explicitly assumed IR step of the rapidity slicing); claimed in `CollinsSoper1981`; conformal-map renormalization theorem for light-like regulators (`Vladimirov:2017ksc`; Ch24 `prop:front-rapidity-renorm`); explicit three-loop soft functions (`Li:2016axz`).
- 文献：`Ji:2019sxk`, `Liu:2022nnk` App. E, `CollinsSoper1981`, `Vladimirov:2017ksc`, `Li:2016axz`.
- 被使用于：`def:lamet-reduced-soft`, `thm:lamet-quasi-tmd` (direct `\uses` users in FINAL_OUTLINE_v2, computed at the merge).
- 解除途径：a proof of the IR-control step of the rapidity-slicing argument (Ch23).
- `\uses{def:lamet-soft-offlc, prop:tmd-evolution}`.

#### `asm:lamet-order-limits` — 极限次序 [\tagA]
- **所属：** Ch22 `sec:lattice-tmd`. Technical.
- 陈述：(OL1) $\varepsilon\to0$ commutes with $L\to\infty$ and with the off-light-cone rapidity regulator limit for $\Omega/\sqrt S$; (OL2) the large-rapidity and Collins schemes differ only in the order of $\varepsilon\to0$ and $y_B\to-\infty$, a UV effect absorbed into $C_q(\sqrt{\zeta_{\rm LR}}/2,\mu)$.
- 地位：[A] — argued to all orders by `Ebert:2022fmh` ((OL1) verified at one loop; (OL2) by asymptotic freedom), not a diagram-by-diagram proof.
- 文献：`Ebert:2022fmh` (read).
- 被使用于：`thm:lamet-quasi-tmd` (direct `\uses` users in FINAL_OUTLINE_v2, computed at the merge).
- 解除途径：a diagrammatic proof of (OL1) beyond one loop and of (OL2).
- `\uses{def:lamet-quasi-tmd, def:tmd-collins}`.

### 3.6 Owner Ch23 `yzliu` (reproduced verbatim from FINAL_OUTLINE_v2 Part VII annex §F1.2)

#### `asm:yzliu-heavy-pair` — 静态色单态 $Q\bar Q$ 对的谱假设 [\tagC]
- **所属：** Ch23 `sec:yzliu-soft`. Technical.
- 陈述：(HP1) isolated colour-singlet ground state of the static pair at fixed $\vec b_\perp$ with residual energy $\gamma^{-1}V(\vec b_\perp)$, gapped continuum; (HP2) non-zero, boost-invariant overlap of the pair interpolating field; (HP3) Wilson-line self-energies and the pair time evolution cancel against $\sqrt{ZZ}$ (LSZ-type amputation; perturbatively `lem:yzliu-partial-exp`).
- 地位：[C] — non-perturbative spectral assumptions; (HP1) is supported by lattice static potentials (evidence).
- 文献：`Ji:2019sxk` (read), `Liu:2022nnk` §4.1–4.2, App. A.
- 被使用于：`cor:yzliu-soft-form-factor` (direct `\uses` users in FINAL_OUTLINE_v2, computed at the merge).
- 解除途径：(HP1) from a gap in the static colour-singlet sector (confinement); (HP2), (HP3) from an LSZ-type construction for static sources in non-perturbative HQET.
- `\uses{def:lamet-soft-offlc}`.

#### `asm:yzliu-wightman-pt` — 维数正规化微扰论中的 Wightman 结构 [\tagA]
- **所属：** Ch23 `sec:yzliu-analyticity`. Technical.
- 陈述：(WP1) order by order, in linear covariant gauges and DR at generic $\varepsilon\ne0$, gluon and ghost Wightman functions satisfy the spectral condition and local commutativity, so that their coordinate-space representations are boundary values of functions holomorphic in the (permuted extended) tubes, covariant under proper complex Lorentz transformations; (WP2) null separations on the same light-like line give scaleless contributions, so $\eta\to0^+$ may be taken at integrand level.
- 地位：[A]-level — formally a consequence of the covariant operator formalism (`KugoOjima1979`) and of the Bargmann–Hall–Wightman theorem (`Streater:1989vi`), used by Liu ("the author believes in it", `Liu:2023pjb` §4 item 2); not proven as a precise statement for DR at generic $\varepsilon$ (indefinite metric, gauge-dependent Green functions). It is the bottleneck of `thm:yzliu-analyticity`, `thm:yzliu-time-ordering`, `thm:yzliu-jet-continuation`.
- 文献：`Liu:2022nnk` App. F, `Liu:2023pjb` §2 and App. B, `Ji:2023pba` App. C.2, `KugoOjima1979`, `Streater:1989vi`.
- 被使用于：`thm:yzliu-analyticity`, `thm:yzliu-time-ordering`, `conj:yzliu-complex-wilson`, `thm:yzliu-jet-continuation` (direct `\uses` users in FINAL_OUTLINE_v2, computed at the merge).
- 解除途径：a proof that the DR parametric representations of all gluon/ghost Wightman functions with numerators are boundary values of holomorphic functions in the permuted extended tubes — e.g. by extending the positivity of $P_{ij}(\alpha)$ (`lem:yzliu-matrix-tree`) and the below-threshold argument of `thm:yzliu-time-ordering` to all graphs.
- `\uses{def:prelim-qcd, def:prelim-brst}`.

#### `asm:yzliu-lightcone-uniform` — 光锥极限对 ${\rm Im}\,\theta$ 的一致性 [\tagP]
- **所属：** Ch23 `sec:yzliu-rapidity`. Technical.
- 陈述：(UL) the light-cone limit $Y\to\infty$ of the single-time-ordered soft functions is uniform in ${\rm Im}\,\theta\in[-\pi,\pi]$.
- 地位：[P] — verified perturbatively for ${\rm Im}\,\theta\in\{0,\pm\frac\pi2,\pm\pi\}$ only.
- 文献：`Liu:2022nnk` §4.5–4.7, §6.
- 被使用于：`prop:yzliu-universality-classes` (direct `\uses` users in FINAL_OUTLINE_v2, computed at the merge).
- 解除途径：a uniform bound on the $O(e^{-\theta})$ remainder in the strip at each order.
- `\uses{def:yzliu-hyperbolic-angle, thm:yzliu-analyticity}`.

### 3.7 Owner Ch24 `front` (reproduced verbatim from FINAL_OUTLINE_v2 Part VII annex §F1.3; the provisional v2.1 texts are replaced — note that (SM2) of `asm:front-scet-modes` is "Glauber modes do not contribute at the stated power", not the v2.1 wording)

#### `asm:front-mor-complete` — 区域集合的完备性 [\tagC]
- **所属：** Ch24 `sec:front-regions`. Technical.
- 陈述：(MR) for the expansion considered, the listed regions (essential facets, or the regions found after dissecting the polytope), each expanded and integrated over the whole domain, reproduce the asymptotic expansion to all orders — no hidden regions, no non-scaleless overlap contributions beyond those of `lem:front-jantzen`.
- 地位：[C] — proven for Euclidean limits (`thm:ir-regions-euclid`) and for the one-facet case (`prop:front-lp-facets`); the facet recipe fails in Minkowski kinematics from three loops (`prop:front-hidden-regions`); no general argument.
- 文献：`Semenova:2018cwy`, `Gardi:2022khw` §6, `Gardi:2024axt`, `Jantzen2011`.
- 被使用于：`prop:front-commuting` (direct `\uses` users in FINAL_OUTLINE_v2, computed at the merge).
- 解除途径：`conj:front-mor-minkowski`; an algorithm guaranteed to find all regions (dissecting the polytope) with a completeness proof.
- `\uses{def:front-facets, def:ir-regions}`.

#### `asm:front-scet-modes` — SCET 的模式完备性与 Glauber 模式的缺席 [\tagA]
- **所属：** Ch24 `sec:front-nlp`. Technical.
- 陈述：(SM1) the listed hard, (anti-)hard-collinear, collinear, soft and soft-quark modes reproduce all regions at the stated power (zero-bin subtractions consistent); (SM2) Glauber modes do not contribute at that power (automatic for decays into colour-neutral states and for $e^+e^-$; for partonic coefficient functions of processes with incoming partons the statement concerns the partonic cross section only).
- 地位：[A] — the standard SCET assumption (critic C6, M18), covered by the region analyses of the processes considered; `prop:front-hidden-regions` shows that completeness has to be checked case by case. Ownership note (§F5 item 11): it may move to Ch15 if the lead author wants `thm:scet-thrust` to cite it.
- 文献：`Liu:2019oav`, `Liu:2020wbn`, `Beneke:2022obx`, `RothsteinStewart2016`.
- 被使用于：`thm:front-hgg`, `prop:front-ggh`, `prop:front-nlp-ll`, `prop:front-nlp-dis`, `prop:front-sidis-nlp` (direct `\uses` users in FINAL_OUTLINE_v2, computed at the merge).
- 解除途径：a region analysis (pinch analysis and power counting, Ch4, Ch9) of each process at the stated power with the Glauber region treated explicitly.
- `\uses{def:scet-modes}`.

---------------------------------------------------------------------------------------------------

## 4. Inner item names (scoped) and renames

Inner items are always cited together with their assumption (「\cref{asm:appN-tmd}(T2)」). Names are unique across the book.

| assumption | inner items | note |
|---|---|---|
| `asm:intro-wightman` | (W1)–(W4) | binding (WRITER_SPEC_v2 §4.4 item 4) |
| `asm:intro-np-ope` | (O1)(O2) | owner's names (FINAL_OUTLINE_v2 Ch1); the parts of "the OPE holds" in App M are (OPE1)–(OPE5) (MD15) |
| `asm:intro-composite` | (C1)–(C3) | owner's names |
| `asm:intro-bridge` | (Br1)–(Br3) | owner's names |
| `asm:appM-brst-ope` | (B2) ≡ (Eε) | v2.3: (B1) retired (the name is not reused); (B2) renamed (Eε) in App M |
| `asm:appM-oswi` | — | v2.3 |
| `asm:appN-contour`, `def:appN-meet-closed`, `asm:appN-envelope`, `asm:appN-separation` | (GA1), (GA2), (GA3), (GA4) | binding; (GA2) is a definition |
| `asm:appN-values` | (V1)(V2) | renamed from the reference's (D1)(D2) |
| `asm:appN-cutsum` | (CU1)–(CU3) | renamed from (X1)–(X3) (clash with the verify extensions X1–X3) |
| `asm:appN-ward-product` | (WI1)(WI2) | renamed from (W1)(W2) (clash with Wightman) and not (WP1)(WP2) (used by `asm:yzliu-wightman-pt`) |
| `asm:appN-uv` | (U1)(U2) | — |
| `asm:appN-multren` | (Z1), (Z3)(i)(ii) | binding names; (Z2) moved to `asm:appN-ir-regulator` |
| `asm:appN-ir-regulator` | (Z2) | — |
| `asm:appN-tmd` | (T1)–(T4) | binding |
| `asm:appN-endpoint` | (E1)–(E3) | binding (not the error types E-S…E-W) |
| `asm:appO-lcopt` | (i)(ii) | (iii) proved in App J |
| `asm:appO-mixing` | (a′)(b)(c) | (c1) deleted; (a) replaced by (a′) in v2.3 |
| `asm:appO-adjacent-swap`, `asm:appO-real-jets` | (ADJ), (REAL) | v2.3; the names belong to `def:appO-sectors` together with (SEC), (EQ) |
| `asm:appO-collinear-ends` | — | v2.3 |
| `asm:appN-lce`, `asm:appN-analytic-reg` | (LCE); (RA1)(RA2) | v2.3 |
| `asm:appO-deformation` | (a)–(d) | — |
| `asm:appO-rewritten-cs` | (i)(ii) | — |
| `asm:lamet-aux-renorm` | (AX1)–(AX3) | Ch22 owner entry |
| `asm:lamet-ope` | (OP1)(OP2) | frontier outline; replaces the LaMET report's (H2) |
| `asm:lamet-uniform` | (UI) ((UI-a), …) | frontier outline; replaces (H3) |
| `asm:lamet-twist4` | (TW1)(TW2) | replaces (H4) |
| `asm:lamet-large-z` | (LZ1)(LZ2) | replaces (H5) |
| `asm:lamet-gap` | (GP1)–(GP3) | replaces the decay hypotheses of the report |
| `asm:lamet-staple` | (ST1)–(ST3) | — |
| `asm:lamet-soft-rapidity` | (SR) | — |
| `asm:lamet-order-limits` | (OL1)(OL2) | — |
| `asm:yzliu-heavy-pair` | (HP1)–(HP3) | — |
| `asm:yzliu-wightman-pt` | (WP1)(WP2) | replaces parts of Liu's (H)/(T) lists |
| `asm:yzliu-lightcone-uniform` | (UL) | — |
| `asm:front-mor-complete` | (MR) | — |
| `asm:front-scet-modes` | (SM1)(SM2) | — |

Other scoped names (not assumptions): (CS1)–(CS3) (`def:method-collins-conditions`), (H1)–(H5) (`thm:method-template`), (CSS-1)–(CSS-6), (O-1)–(O-8), (Gla-a)–(Gla-c) (WRITER_SPEC_v2 §4.4 item 4), (Ctr) (`lem:appM-chain-expansion`; the reference's "(H)"), (ET1)(ET2) (`lem:appO-equal-time`; not (J1)(J2), which the frontier outline uses locally for Jantzen's conditions), (GC1)–(GC3) (`def:appO-graded`; the reference's (S1)–(S3)), (h1)(h2) (`prop:appN-dy`), (OPE1)–(OPE5) (App M §M.1, meaning of "the OPE holds"; renamed at the merge, MD15), (QT1)–(QT7), (PS1)–(PS3), (J1)–(J4) (local lists of the frontier outline), (Φ) (`cor:dis-weak-xspace`), MA0–MA4 (umbrella names). **v2.3 local names** (not assumptions; clash-free): (Pr1)–(Pr5), (NE) (`def:appM-blocks`, `lem:appM-ne`), (CTp) (`rem:appM-remainder-reduction`), (A1)–(A4) (`prop:dis-ope-euclid`), (FR), (FI) (`def:appN-fibered`), (IL1)–(IL3), (IRF), (COV) (App N fibered framework), (M1), (M2) (App N scalar models), (SEC), (EQ) (`def:appO-sectors`), F.1–F.4 (`rem:appN-fibered-allorders`). The LaMET report's (H1) is not an assumption: it is the proposition `prop:lattice-renormalizability` (under `asm:lamet-aux-renorm`).

---------------------------------------------------------------------------------------------------

## 5. Grade-propagation consequences

### 5.1 Bottlenecks of the main theorems (for the 瓶颈 column of `tab:summary-master` and for App P `tab:appP-uses`)

| statement (tag) | technical assumptions in the dependency closure (direct and through App N/O) | global (MA) | weakest |
|---|---|---|---|
| `thm:method-subtraction` [A] | `asm:appN-collins`, `asm:appN-uv`; through `thm:appN-subtraction`: `asm:appN-contour`; through `lem:method-local-accuracy`: `asm:appN-envelope`, `asm:appN-separation` | — | all \tagA (bottleneck `asm:appN-collins`) |
| `thm:method-template` [A] | the above + `asm:appN-ward-product`; named gap `asm:appN-brst-nonlocal` ([C]; named, not a premise; MD1) | `asm:intro-bridge` | \tagA (named gap [C]) |
| `thm:appN-structure` [R, R_cond] | all `asm:appN-*` of its premise sentence incl. `asm:appN-brst-nonlocal` | — | content [C] (through the named gap) |
| `thm:disall-factorization` [A] | `asm:appN-collins`, `asm:appN-cutsum`, `asm:appN-separation`, `asm:appN-envelope`, `asm:appN-ward-product`, `asm:appN-uv`, `asm:appN-multren`(Z1)(Z3) | `asm:intro-bridge` | \tagA |
| `thm:coll-sia` [A], `thm:coll-sidis` [A] | `asm:appN-multren` ((Z1) for FFs), `asm:appN-cutsum`, `asm:appN-collins` | `asm:intro-bridge` | \tagA |
| `thm:dy-factorization` [A] | `asm:appO-lcopt`, `asm:appO-envelope`, `asm:appO-mixing`, `asm:appO-deformation`, `asm:appO-rewritten-cs`, `asm:appN-collins`, `asm:appN-cutsum`, `asm:appN-ward-product`, `asm:appN-envelope`, `asm:appN-separation` | `asm:intro-bridge` | \tagA (status paragraph names the `asm:appO-*` items: "B′") |
| `thm:tmd-factorization` [A] | `asm:appN-tmd`, `asm:appN-ward-product`, `asm:appN-collins`, `asm:appN-cutsum`; DY: + `asm:appO-*` (via `prop:appO-tmd`) | `asm:intro-bridge` | \tagA |
| `thm:scet-thrust` [A] | `asm:appN-collins`, `asm:appN-cutsum` ((CU3)), `asm:appN-values` (convention) | `asm:intro-bridge` | \tagA |
| `thm:excl-pion-ff` [A], `thm:excl-meson-L` [A] | `asm:appN-endpoint`, `asm:appN-collins`, `asm:appN-ward-product` | `asm:intro-bridge` | \tagA |
| `prop:dis-ope-gi` [A] | `asm:appM-brst-ope` | — | \tagA |
| `prop:dis-ope-forward` [A] | `asm:appM-forward` (+ `prop:dis-ope-gi`) | — | \tagA |
| `thm:appM-scaling` [R, R_cond] | `asm:appM-remainder` | — | content [A] |
| `thm:dis-moments-np` [R, R_cond] | — | `asm:intro-wightman`, `asm:intro-composite`, `asm:intro-np-ope`, `asm:intro-af-coeff` (+ `asm:intro-growth` for all $n$) | content [C] (non-perturbative theorem) |
| `thm:disall-renorm-compat` [R, R_cond] | `asm:appN-multren`(Z1)(Z3)(i), `asm:appN-ir-regulator`, `asm:appN-contour` | — | content [C] — **must not be used by [A] statements** |
| `thm:lamet-quasi-tmd` [A] | `asm:lamet-staple`, `asm:lamet-soft-rapidity`, `asm:lamet-order-limits` | `asm:intro-composite`, `asm:intro-bridge` | \tagA |
| `thm:lamet-hadronic` [R, R_cond] | `asm:lamet-uniform`, `asm:lamet-twist4`, `asm:lamet-large-z` | `asm:intro-wightman`, `asm:intro-composite` | content [C] |
| `thm:lamet-exp-decay` [R, R_cond] | `asm:lamet-gap` | `asm:intro-wightman` | content [C] (non-perturbative) |

### 5.2 Entries tagged \tagC or \tagP and their users (state of FINAL_OUTLINE_v2)

- `asm:appN-brst-nonlocal` [C] → only `thm:appN-structure` (content [C]); named gap of `lem:method-ward-multi`, `thm:method-template` and the Feynman-gauge process theorems (MD1).

- `asm:appN-ir-regulator` [C] → only `thm:disall-renorm-compat` (content [C]); the [A] theorems use (Z3)(ii).
- `asm:lamet-uniform`, `asm:lamet-twist4`, `asm:lamet-large-z` [C] → `thm:lamet-hadronic` (R_cond, content [C]); `conj:lamet-principle` [C] cites them in its status (pointer).
- `asm:lamet-gap` [C] → `thm:lamet-exp-decay` (R_cond, non-perturbative), `conj:lamet-decay-qcd` [C]. (`prop:yzliu-decay-extensions` no longer uses it: restricted to the scalar-model statement by the frontier outline — resolved.)
- `asm:yzliu-heavy-pair` [C] → `cor:yzliu-soft-form-factor` [R, R_cond] (content [C]); `thm:yzliu-soft-hqet` [A] no longer uses it (resolved by the frontier outline).
- `asm:yzliu-lightcone-uniform` [P] → `prop:yzliu-universality-classes` [P] (consistent).
- `asm:appO-adjacent-swap`, `asm:appO-real-jets` [P] (v2.3) → only the App O model theorems `prop:appO-twoexch-spectator`, `prop:appO-pergraph-weights`, `prop:appO-halfcoinc-sensitivity` (all [P]); no [A] statement uses them.
- `asm:front-mor-complete` [C] → `prop:front-commuting` [R, R_cond] (content [C]; fallback [C], not [A], MD14).
- The six global `asm:intro-*` [C] do not lower ordinary statements; R_cond statements listing them have content grade [C] and are explicitly non-perturbative.

### 5.3 Inconsistencies found in the working drafts — all resolved in FINAL_OUTLINE_v2 (items 1–4, 6, 8 by the merge patches P2–P7, P9; item 5 by the core drafter; item 7 by the frontier drafter; see `AUDIT_v2.md` §2)

1. Core: `thm:disall-renorm-compat` lists only `asm:appN-multren`; with the split it must list `asm:appN-ir-regulator` and must not appear in the `\uses` of [A] statements (the core draft's `thm:disall-factorization` does not use it — consistent).
2. Core: `lem:tmd-sqrt-identity` [R, R_def] lists `asm:appN-tmd` in `\uses`; only its second item uses (T2) — either split the item (composite rule, WRITER_SPEC_v2 §4.3 rule 3) or remove the assumption from the `\uses` of the R_def statement.
3. Core: `prop:pdf-timelike-dglap` [R, R_PT] lists `asm:appN-multren`; (Z1) for FFs is an [A]-level input, so the statement must be [A] or $R_{\rm cond}$ (qualifier rule, App P C-P7).
4. Core: `prop:excl-soft-cancel` premise sentence lacks `asm:appN-ward-product` (its step (i) uses (WI1)).
5. Core: the global entries are written with `\uses{}`; WRITER_SPEC_v2 §4.5 item 1 requires `% uses: none`.
6. Core: `lem:method-ward-multi` must add `asm:appN-brst-nonlocal` (if the lead author keeps the entry). — **Not done by decision MD1** (named gap instead of a premise).
7. Frontier: items in §5.2 (`prop:yzliu-decay-extensions`, `thm:yzliu-soft-hqet`).
8. Proof-delivery `\uses` additions for chapter statements proved in App M/N/O are listed in the proof-delivery tables of `OUTLINE_appMNOPQ.md` (e.g. `lem:appM-uniqueness` for `prop:dis-ope-euclid`, `prop:dis-ope-rg`; `lem:appN-absorption` for `prop:tmd-zero-bin-soft`; `def:appO-orientation` for `lem:dy-poles-orientation`).

---------------------------------------------------------------------------------------------------

## 6. Hypotheses deliberately not registered

| hypothesis | where | why not registered |
|---|---|---|
| (CS1)–(CS3) | hypotheses of `thm:appN-subtraction`; defined in `def:method-collins-conditions` | hypotheses of a conditional theorem; the assumed version is `asm:appN-collins` |
| (Com)(Abs), meet closure | `prop:method-product`, `def:appN-meet-closed` | hypotheses of an identity / a choice |
| (Ctr) | `lem:appM-chain-expansion` | combinatorial condition verified in the applications |
| (ET1)(ET2) | `lem:appO-equal-time` | hypotheses of a mathematical lemma, verified in LCOPT (`lem:appO-insertion-values`) |
| (GC1)–(GC3) | `def:appO-graded` | definition of a class of configurations |
| (h1)(h2) | `prop:appN-dy` | (h1) is part of `asm:appN-cutsum`(CU2), (h2) is `asm:appO-rewritten-cs` |
| (H1)–(H5) | `thm:method-template` | template hypotheses verified process by process |
| (Φ) | `cor:dis-weak-xspace` | existence of measures with given moments: a hypothesis of a corollary |
| (O1)–(O5) | App M §M.1 | names of the parts of "the OPE holds", each proved or assumed elsewhere |
| LaMET (H1) | Ch22 | it is the proposition `prop:lattice-renormalizability` |
| Liu's assumed IR-control step of the rapidity-slicing argument | Ch23 | the weakest step of an [A] sketch is named in the 「地位与缺口」 paragraph (registering it would make the [A] statement [C]) |
| (QT1)–(QT7), (PS1)–(PS3), (J1)–(J4) | Ch23, Ch24 | local hypothesis lists of single statements |
| MA0–MA4 | Ch1 `def:intro-MA` | umbrella names; the register entries are the precise forms |

---------------------------------------------------------------------------------------------------

## 7. Changes relative to the 25-entry register of REFDOC §5.3

1. 25 → 41 entries: + `asm:appN-ir-regulator` (split from `asm:appN-multren`(Z2)), + `asm:appN-brst-nonlocal` (explicit), + 14 frontier entries (Ch22: 9, Ch23: 3, Ch24: 2), with the names of the frontier outline.
2. `asm:appN-multren`: (Z3) split into (i) (same $\hat{\mathsf H}^{\rm bare}$) and (ii) (DR mass factorization), which is what the [A] process theorems use.
3. `asm:appO-mixing`: (c1) deleted (false per graph) and replaced by `lem:appO-joint-localization`; status updated with `prop:dy-eikonal-twogluon` ($O(g^4)$ eikonal case holds).
4. `asm:appO-deformation`(d): extended to coincident SA/AS insertions (non-analytic ordering weights).
5. `asm:appO-envelope`(ii): boundary layers from neighbourhoods with $\beta_{R'}>\beta_R$ included.
6. `asm:appO-lcopt`: item (iii) (Hermiticity of cut rules) removed — proved in App J (`lem:appJ-cut-hermiticity`).
7. Tags assigned per WRITER_SPEC_v2 v2.1 §4.4 item 2 (the REFDOC register gave status sentences only); "open" no longer mapped to `\tagC`.
8. Inner items renamed as in §4 ((CU), (V), (WI), (GC), (ET), (Ctr)).
9. Users ("被使用于") recomputed from the working drafts.

---------------------------------------------------------------------------------------------------

## 8. Open decisions for the lead author (v2.1) — taken provisionally at the merge (FINAL_OUTLINE_v2 §0.8)

1. **`asm:appN-brst-nonlocal`**: keep as a `\tagA` entry (making explicit what the [A] tag of `lem:method-ward-multi` contains) or tag `\tagC` as the frontier report assesses the multilocal case — the latter turns every process theorem into [C] by grade propagation.
2. **(Z2) split**: keep `asm:appN-ir-regulator` (`\tagC`) with the regulator route `thm:disall-renorm-compat` at content grade [C] and the DR route (Z3)(ii) for the [A] theorems (this register's choice), or re-merge (Z2) into `asm:appN-multren` (`\tagA`) as in REFDOC §5.3.
3. **`\tagA` for the technical App M/N/O entries** (§00.2): binding only if the master-table tags [A] of the process theorems are kept; otherwise those theorems drop.
4. **Frontier entries**: confirm the adoption of the frontier outline's 14 names and tags; resolve the two grade inconsistencies of §5.2 (`prop:yzliu-decay-extensions`, `thm:yzliu-soft-hqet`); write the two Ch24 entries (provisional here).
5. **Global entries**: confirm `\tagC` for the six `asm:intro-*` (no effect on ordinary statements; content grade [C] for the explicitly non-perturbative R_cond theorems).

**Merge (v2.2):** item 1 → MD1 (`\tagC`, named gap; **confirmation requested**); item 2 → MD2 (split kept; `thm:disall-renorm-compat` premises completed, `prop:disall-h5` re-routed); item 3 → MD3 (`\tagA` kept, consistent with the master-table [A] tags); item 4 → frontier names and tags adopted, both inconsistencies resolved by the frontier outline, the two Ch24 entries now copied from the owner (§3.7), `asm:front-scet-modes` stays with Ch24 (MD13); item 5 → `\tagC` kept.

---------------------------------------------------------------------------------------------------

## CHANGELOG

**2026-10-10 — drafted (spec-v2 new-appendices drafter).**
1. Global register of 41 entries with owner, tag, exact content (inner items), status, literature, direct users, upgrade path and `\uses`; summary table in the `check_unit_v2.py` registry format (`### Assumptions`).
2. Started from the 25 entries of REFDOC §5.3, MA0–MA4 (critic §12) and the frontier hypotheses; frontier names, tags and inner items adopted from the frontier outline's working draft (no clash with core/appendix names); two Ch24 entries provisional.
3. Decisions §00.3 (split of (Z2); explicit `asm:appN-brst-nonlocal`; deletion of `asm:appO-mixing`(c1)); renames §4; grade-propagation consequences and draft inconsistencies §5; open decisions §8.

**2026-10-10 (merge) — revision v2.2 (spec-v2 integrator).**
1. Merged with `FINAL_OUTLINE_v2.md`: §1 regenerated (identical to its `### Assumptions` table; users computed from the final `\uses` data; owners' titles); §3.1 reproduces the binding Ch1 texts; §3.5–§3.7 reproduce the owner texts of the frontier annex §F1 (the provisional Ch24 texts of v2.1 are replaced); every 「被使用于」 field of §3.2–§3.7 recomputed.
2. `asm:appN-brst-nonlocal` → `\tagC`, named gap (MD1); §00.2, §00.3, §5.1, §5.2 updated. Totals: 25 `\tagA`, 1 `\tagP`, 14 `\tagC` (6 global), 1 untagged.
3. Inner names: `asm:intro-np-ope` (O1)(O2), `asm:intro-composite` (C1)–(C3), `asm:intro-bridge` (Br1)–(Br3) are the owner's; App M's parts of "the OPE holds" are (OPE1)–(OPE5) (MD15).
4. §5.3 marked resolved; §8 records the provisional merge decisions.

**2026-10-11 — revision v2.3 (spec patcher, verify patch).**
1. Six new entries (§3.2–§3.4): `asm:appM-oswi`, `asm:appN-lce`, `asm:appN-analytic-reg`, `asm:appO-collinear-ends` (`\tagA`), `asm:appO-adjacent-swap`, `asm:appO-real-jets` (`\tagP`); totals 29 `\tagA`, 3 `\tagP`, 14 `\tagC` (6 global), 1 untagged = 47.
2. Rewordings after X1–X3: `asm:appM-brst-ope` ((B1) retired, (B2) ≡ (Eε); new title), `asm:appO-mixing` ((a) → (a′), status), `asm:appO-envelope` (side-summed families for coincident connections), `asm:appO-deformation` ((c), (d), status); status and upgrade fields of `asm:appM-remainder`, `asm:appM-forward`, `asm:appN-collins`, `asm:appO-lcopt` updated (slot outcomes of FINAL_OUTLINE_v2 §00.4); 「文献待补」 replaced by `Bergere:1977wz`, `Schoonderwoerd:1998qj`, `Schoonderwoerd:1998iy`.
3. §1 regenerated (identical to FINAL_OUTLINE_v2 §08 `### Assumptions`; the seven rows whose math cells were broken by unescaped `|` rebuilt with `\vert`; users recomputed); every 「被使用于」 field recomputed from the final `\uses` data; §00.2, §00.3 item 5, §4, §5.2 updated. Lead-author confirmation requested (FINAL_OUTLINE_v2 MD19).

