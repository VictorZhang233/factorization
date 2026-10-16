# Verification batch R-M30 – R-OUR2 (stage 1, independent verifier)

Date: 2026-10-10. Default stance: skeptical. All eleven claims are of kind `correction_of_reference_doc`
(sources: `refdoc/REFDOC_ANALYSIS.md` ERR-M30 … ERR-M32, ERR-m1 … ERR-m27, §2.4 OUR-1 … OUR-8; full statements in
`verify/CLAIMS.md` §5). Criterion: a correction is confirmed only if the physics (or attribution) statement our monograph
would print is correct. Where a claim bundles several sub-items, every sub-item was checked. Sub-items that turned out
wrong or that I could not verify are listed explicitly and are excluded from the printable statement.

## 0. Method and sources

* **Reference document.** I read it through the page-split text `refdoc/refdoc.txt` (form feed = PDF page; printed
  page = PDF page), using `batch_R-M30_s1_scripts/page.py`. Pages read: 6–7, 11–17, 23–25, 28–29, 32, 34, 39–40, 48–49,
  55–58, 62, 66–69, 72–73, 77–78, 81, 83, 88, 91–92, 97, 101–102, 110, 112, 121, 123, 128–129, 139–141, 145, 155–158,
  162–165, 176–181, 192–195, 208, 213, 215, 217–218, 227–238 (bibliography). Page 92 (Fig. 55) was rendered with
  `pdftoppm` and inspected as an image.
* **Primary literature** (arXiv e-print sources downloaded into fresh scratch directories, read as text; bibliographic
  data checked with the INSPIRE API and arXiv abstract pages):
  * Aybat–Sterman, arXiv:0811.0246 = PLB 671 (2009) 46 [AS2009] (full text, 4 pp.)
  * Diehl–Gaunt–Ostermeier–Plößl–Schäfer, arXiv:1510.08696 = JHEP 01 (2016) 076 [DGOPS] (§4, summary)
  * Gaunt, arXiv:1405.2080 = JHEP 07 (2014) 110; Schwartz–Yan–Zhu, arXiv:1801.01138v2 = PRD 97 (2018) 096017 [SYZ];
    Zeng, arXiv:1507.01652 = JHEP 10 (2015) 189; INSPIRE list of the 36 papers citing SYZ; Barcaro et al. arXiv:2607.14259
  * Sen–Indumathi–Choudhury, arXiv:1812.06468 (reproduces the Grammer–Yennie K/G split, PRD 8 (1973) 4332, not itself seen)
  * Shifman, hep-ph/0009131 (full text; INSPIRE and arXiv records)
  * Bacchetta–D'Alesio–Diehl–Miller, hep-ph/0410050 = PRD 70 (2004) 117504 (Trento conventions)
  * Catani–de Florian–Rodrigo, arXiv:1112.4405 = JHEP 07 (2012) 026 [CdFR]
  * Chay–Kim–Kim–Lee, hep-ph/0412110 = PRD 71 (2005) 056001 [CKKL]
  * Scimemi–Vladimirov, arXiv:1609.06047 = JHEP 03 (2017) 002; Moos–Vladimirov, arXiv:2008.01744 = JHEP 12 (2020) 145
  * Collins–Soper–Sterman review, hep-ph/0409313 (GY passage)
  * INSPIRE abstracts: David NPB 209 (1982) 433 and NPB 234 (1984) 237; Beneke–Braun–Kivel PLB 443 (1998) 308 (arXiv abstract)
* **Scripts** in `verify/claims/batch_R-M30_s1_scripts/` (run with `python3 -I`; output in the `.log` next to each):
  * `rm31_kinematics.py` — R-M31: central-jet denominators for DY-Glauber and (n_A,w_1)-Glauber momenta, scaling fits.
  * `rm06_checks.py` — R-m06: handbag traces (m6), Mellin moments of plus distributions (m8), RG degrees (m11).
  * `rm13_checks.py` — R-m13: qg→γ*q in Feynman and light-cone gauge (m13), PT on bilinears and the sign of ε_T^{12} (m14),
    endpoint area (m15).
  * `rm23_checks.py` — R-m23: exact off-shell triangle, Table 5, Collins remainder, N12 point, Ex. C.27, C_S Beta function.
  * `rm26_checks.py` — R-m26: LHP closure for Lemma E.28(iii), absolute vs relative error in (E.30), (E.51) colour algebra,
    ordering weights.
  * `rour1_ff.py` — OUR-1: explicit O(α_s) quark→quark fragmentation function in the hadron frame.
  * `rour2_checks.py` — OUR-3 segment bound, OUR-4 one- vs two-component deformation, OUR-5 invariants, OUR-6 example.
  * `refdoc/work_R8/check_kinematics.py` (the recipe for R-M31) was read and re-run (ALL PASS), but it does **not**
    test Rem. E.54(b) (its items K1–K11 concern other statements); R-M31 was therefore checked with `rm31_kinematics.py`.

## 1. Summary

| id | verdict | what must change before printing | literature |
|---|---|---|---|
| R-M30 | **confirmed**, wording refined | Gaunt is cited on p. 229 for the E_T breakdown; SYZ ([137]) appears only in a generic list on p. 230. Print Gaunt as "argument fails / suggestion", SYZ as contradicting only the pure-Glauber part. Do not print "MPI-sensitive observables remain non-factorizing": keep [C]. NNLO note: no S–S configuration exists in partonic DY at NNLO; first single S–S exchange between radiated partons at N³LO. | Gaunt 2014; SYZ 2018; Zeng 2015 |
| R-M31 | **confirmed** | Write the dropped term as −2l_T·k_T ∼ λQ². For a generic DY-Glauber k it dominates (2l·k ∼ λQ²), so J_1's k⁻ dependence is a relative O(λ) effect. The leading pinch region is Glauber relative to (n_A,w_1). "k_T ⊥ w_{1T}" describes only the slice k⁺ ≲ λ²Q; in general w_1⁻k⁺ − w_{1T}·k_T = O(λ²Q). | statement about the reference only |
| R-M32 | **confirmed with a corrected attribution** | Do **not** print "the App E method is Aybat–Sterman's". The LCOPT/sum-over-cuts/deformation method is CSS 1988 (reviewed in Collins 2011 ch. 14), which the reference credits (p. 165). AS2009 says so itself, and so does DGOPS. AS2009 is an uncited precedent for the "hybrid form" and for the "pinch ↔ mismatch of deformation directions" formulation. DGOPS **is** cited ([61], §12.6, Rem. E.57), but only for double DY; its single-DY LCPT argument (§4.3.1) is not compared. The forbidden phrase is rightly forbidden; the reference does not use it. | AS2009; DGOPS 2016; CSS 1988 (via AS2009/DGOPS) |
| R-m01 | **confirmed** | Locator: the ν = P·q clash is on p. 11 (after (2.9)), grade C on p. 7. m1: the soft-quark points k = p_1, −p_2 are the endpoints of C_1, C_2 and are power suppressed by m²/Q². m3: the original GY was seen only via 1812.06468. | GY 1973 (via Sen et al. 2019); Collins 2011/DGOPS for the one-sided form |
| R-m06 | **confirmed** | none (m8: Mellin asymptotics verified; m6: trace decomposition verified) | Shifman 2000 (§"three regimes", eq. (monone)) |
| R-m13 | **confirmed** | Print the analytic limits (t|M_e|² → −8ŝ, t·2Re → 16ŝz(1−z), sum −8ŝ[z²+(1−z)²]); −80/+33.6 hold only at ŝ = 10, Q² = 3 with couplings, colour and spin average stripped. ε_T^{12} = +1 is the hadron-along-+z value implied by Trento's definition. Trento's own ε_⊥^{12} = −1 is a different tensor in the SIDIS frame. m15 is an internal-consistency correction. | Trento 2004; Scimemi–Vladimirov 2017; Moos–Vladimirov 2020 |
| R-m17 | **confirmed** | m19: the proven case is David 1982 (large-N O(N) σ-model, "we prove that renormalons cancel"), with BBK 1998 at NLO in 1/N. m20: Lemma C.43 itself is restricted to symmetric traceless operators; only the p. 83 summary drops the qualifier. m22: the [60] title nit could not be confirmed (INSPIRE shows the arXiv title); keep only verified items. | CdFR 2012 eq. (ic12gen), §3-parton case; CKKL 2005; David 1982; BBK 1998 |
| R-m23 | **confirmed except two sub-items** | **Drop** "Fig. 55 has cubic vertices outside the stated model". The model includes spinors, and the Yukawa vertex ψ̄ψφ is a dimension-4 monomial; both graphs of Fig. 55 are valid Yukawa graphs. Lemma D.23(iii) edge case: not verified (REFDOC itself says "plausible"); do not print. | Usyukina–Davydychev (closed form); exact numerics here |
| R-m26 | **confirmed** | E.28(iii): the bound in the closed LHP is \|E(z)\| ≤ 2Mλ_J/\|z\|². The reference's 3Mλ_J/k² is weaker but valid. The vertex-sign slip has no effect on V_G (two vertices). | statement about the reference only |
| R-OUR1 | **confirmed** | OUR-3: the bound is √3M/Q under the reference's restriction \|**q**\| ≥ Q/2 ((C.31)), and 2M/Q in general. | Collins–Soper 1982; Collins 2011 ch. 12 (prefactor, via the reference's (2.13)) |
| R-OUR2 | **confirmed** | OUR-5: O((b_T m)²) up to logarithms (more precisely ∝ x b_T²Λ² for TMD PDFs, b_T²Λ²/z for TMD FFs, Scimemi–Vladimirov). | Scimemi–Vladimirov 2017; Moos–Vladimirov 2020; INSPIRE/arXiv for Shifman 2000 |

---

## 2. R-M30 — Gaunt cited without the SYZ rebuttal; NNLO DY does not test the spectator Glauber cancellation

**Reference.**
* p. 229, Rem. E.55: "Gaunt [136] 指出，对强子末态横能量 E_T 这类可观测量，CSS 论证在旁观者之间交换两条 Glauber 胶子的层次上失效，并把这一失效与多部分子相互作用联系起来。"
* [137] = SYZ (PRD 97 (2018) 096017) is in the bibliography (p. 238). It is cited only once, at the end of Rem. E.56 (p. 230): "关于 Glauber 相位与因子化破坏之间关系的进一步讨论见 [54, 55, 137]". The rebuttal is never attached to the Gaunt sentence.
* p. 227 (Rem. E.53(1)) already states that the explicit two- and three-loop DY coefficient functions test the cancellation for coloured massless partonic initial states, not the spectator Glauber cancellation. So the "NNLO note" is indeed not a reference error.

**Literature (read).**
* Gaunt 2014, abstract: "the classic CSS argument for the cancellation of Glauber gluons breaks down at the level of two Glauber gluons exchanged between the spectators … we *suggest* that this failure … corresponds to a failure of the 'standard' factorisation formula … MPI sensitive observables … beam thrust … transverse thrust."
* SYZ 2018, abstract: "for pure Glauber ladder graphs, all amplitude-level factorization violating effects completely cancel at cross section level for any single-scale observable (such as hadronic transverse energy or beam thrust). This result disproves previous claims that these pure Glauber graphs are factorization-violating … The leading factorization-violating effects therefore come from graphs with at least one soft gluon, involving the Lipatov vertex."
  * Introduction: "Our argument does not apply to doubly-differential observables, like those studied in [Zeng]."
  * Explicit two-loop check, then an all-orders argument via scale invariance (§3, conclusions).
* Zeng 2015: the observable is the doubly-differential beam thrust (τ_R, τ_L) in γγ → Φ + X, in QCD with scalar quarks. The double longitudinal spin asymmetry is (1.58 ± 0.02) C_F²α_s² relative to LO, non-zero at leading power, and comes from two spectator–spectator Glauber gluons (one on each side of the cut). This contradicts any factorization with decoupled collinear sectors ("generalized factorization").
* INSPIRE: 36 papers cite SYZ. None rebuts it. Barcaro et al. 2026 (2607.14259) list Gaunt 2014, Zeng 2015 and SYZ 2018 together among works where violation "has been established", without discussing the conflict. My reading agrees with the earlier E36 verification (`batch_E31_s1.md` §7).

**NNLO/N³LO note (refined).** The note concerns fixed-order *partonic* DY, which has no hadronic (colour-singlet, bound-state) spectators. The spectators of a partonic "hadron" are radiated collinear partons. My order counting:
* NNLO has no spectator–spectator configuration at all. That needs a radiated parton from each beam (RR) plus a loop.
* RV at NNLO contains only spectator(A)–active(B) exchanges, which are deformable on one side.
* The first S–S Glauber exchange between radiated partons is a single gluon in RRV at N³LO. It is abelian-like: a phase that cancels between the two cuts after the relative-momentum integral.
* Multiple non-abelian S–S exchanges first appear beyond N³LO.

So partonic fixed-order finiteness tests the leading-power cancellation for coloured massless partonic states to that order, not the hadron-spectator cancellation. Agreement with data is evidence for factorization as a whole, not a test of this step.

**Verdict: confirmed.** "Contested" is accurate in the sense of E36: no published rebuttal of SYZ exists, and Gaunt's later listing does not engage with SYZ. The REFDOC phrase "MPI-sensitive observables remain non-factorizing (Zeng 2015 explicit counterexample)" overstates the case. Zeng's counterexample is doubly differential and polarized, i.e. outside SYZ's scope. For single-scale MPI-sensitive observables, violation is expected through Glauber–soft (Lipatov) graphs but has not been demonstrated: grade [C].

## 3. R-M31 — Rem. E.54(b) ignores −2l_T·k_T

**Reference, p. 228 (b):** "(l+k)² − m² = l² − m² + 2l·k + k²，而 2l·k 含 2l⁺k⁻，l⁺ ∼ Q（w_1 不平行于 n̄）。所以 J_1 在与 J_A 的分母相同的尺度 λ² 上依赖于 k⁻，引理 E.28 的前提不成立。"

**Independent check (`rm31_kinematics.py`).** Set Q = 1. The central jet w_1 has rapidity 0.3. A J_1 line is l = E w_1 + O(λ) + O(λ²), with l² ∼ λ². Fits over λ = 10⁻² … 10⁻⁴ give:

| region of k | 2l·k | 2l⁺k⁻ | ratio |
|---|---|---|---|
| generic DY-Glauber, k = (λ², λ², λ) with k_T in a generic direction | ∼ λ^0.999 (dominated by 2l_T·k_T) | ∼ λ^2.002 | ∼ λ |
| Glauber relative to (n_A, w_1): k·n_A ∼ k·w_1 ∼ λ², rest ∼ λ | ∼ λ^1.996 | ∼ λ^2.002 | ≈ 0.46, constant |

* In the generic region the J_1 line is pushed off shell by O(λ) ≫ λ². Its dependence on k⁻ is then a relative O(λ) effect, and the region is power suppressed by one power of λ (volume λ⁶ × propagators λ⁻²·λ⁻²·λ⁻¹ = λ). Only a fraction ∼ λ of the DY-Glauber volume keeps |w_1·k| ≲ λ² (Monte Carlo: 1.7λ).
* In the (n_A,w_1)-Glauber region the count is λ⁶ × λ⁻⁶ = λ⁰, i.e. leading, and J_1 depends on k⁻ at scale λ² through w_1⁺k⁻. The conclusion of (b) therefore survives.
* Precision: in this region the DY light-cone component k⁺ can be ∼ λ, compensated by w_{1T}·k_T. The REFDOC description "k_T nearly orthogonal to w_{1T}" holds on the slice k⁺ ≲ λ²Q. The general condition is w_1⁻k⁺ − w_{1T}·k_T = O(λ²Q).
* The dropped term is ∼ λQ², not "Qλ".

**Verdict: confirmed.**

## 4. R-M32 — attribution of the App E method; DGOPS; the forbidden phrase

**Reference.**
* The method (pp. 162–165, 176–181, 192–195): x⁺-ordered LCOPT for J_A and x⁻-ordered LCOPT for J_B, with the soft momenta as external injections. Initial-state energy denominators contain +k⁻ and final-state ones −k⁻ (Lemma E.22), so the pinch is an "initial–final" pinch (Def. E.4). The sum over cuts with maximal-time pairing cancels FSI (Lemmas E.24, E.26). Simultaneous deformation of the soft momenta then gives Wilson lines.
* Credits (p. 165): "本附录的论证沿用 Collins–Soper–Sterman [135, 3, 4]、Bodwin [6] 与 Collins 专著 [1] 第 14 章的思路；光锥排序微扰论的规则取自 Kogut–Soper [131] 与 Brodsky–Pauli–Pinsky [132] …".
* Aybat–Sterman is cited nowhere: no "Aybat" in the text, and no PLB 671 in the bibliography [1]–[145].
* DGOPS **is** cited as [61], in §12.6 (p. ~75, double DY, grade B′) and in Rem. E.57 (p. 230: "Diehl、Gaunt 等 [61] 把 CSS 的 Glauber 相消论证推广到这一过程。用我们的步骤来看：…").
* The phrase 「Glauber 相消的方法是 Collins (2011) 首创的光锥序处理」 does not occur in the reference. It is a writer rule in our `spec_v2/WRITER_SPEC_v2.md:559`.

**AS2009 (full text read).**
* "In Ref. [CSS 1988] the remainder functions R were treated in light cone-ordered perturbation theory (LCOPT) … the cancellation of final state interactions is manifest after the integral over p_N⁺."
* AS2009's own step is the "hybrid form": LCOPT for the reduced remainder, with the low-q⁻ "eikonal field" as an external source at fixed q⁺, their eq. (Mj).
* They find poles only in the UHP for initial-state and only in the LHP for final-state insertions. Then: "The Glauber 'pinch' of covariant perturbation theory is then replaced in the hybrid form by a mismatch between the directions of the deformations for initial and final states."
* Further ingredients: the "causal identity" (their eq. (causal)); Wilson lines W_- for the spectators; phases that cancel after the inclusive sum; the explicit abelian phase (their eq. (Mj2)).
* AS2009 has one jet plus an incoming Wilson line β. Its "hybrid" means covariant eikonal field + LCOPT remainder, not "x⁺ for one jet, x⁻ for the other".

**DGOPS (§4 read).**
* "We make use of the same techniques that were used to demonstrate the all-order cancellation of Glauber gluons in the single Drell-Yan process [CSS 1988, Collins 2011] -- in particular, we use the light-front ordered version of QCD perturbation theory (LCPT)."
* §4.3.1 "Single Drell-Yan" re-derives the sum-over-cuts argument: LCPT in x⁺ for the collinear factor A, soft lines treated as external lines, all poles of A in the lower half plane after the sum over cuts. Steps for B are done "with the roles of plus and minus momenta interchanged".
* Summary: the all-order proof "makes use of light-cone perturbation theory and generalises the corresponding proof for the single Drell-Yan process in [CSS 1988, Collins 2011]".
* DGOPS do not cite AS2009.

**Verdict: confirmed with a corrected attribution.** Each part of the claim:
* AS2009 really contains the hybrid form, the deformation-mismatch formulation, and FSI/phase cancellation by unitarity. It is not cited by the reference. Confirmed.
* The phrase "the App E method *is* Aybat–Sterman 2009" over-attributes. By AS2009's and DGOPS's own statements, the LCOPT treatment with FSI cancellation after the cut sum goes back to CSS 1988 (reviewed in Collins 2011 ch. 14), and the reference credits those works. The two-sided form (x⁺ for A, x⁻ for B) appears explicitly in DGOPS.
* "DGOPS not compared" is true only for its single-DY LCPT argument. The reference cites DGOPS and maps its double-DY extension onto App E's steps (Rem. E.57).
* The forbidden phrase is correctly forbidden: the LCOPT treatment predates Collins 2011 (CSS 1988). Caveat: CSS 1988 and Collins 2011 were not read directly; their content is taken from AS2009's and DGOPS's statements.

## 5. R-m01 — m1–m5 (pp. 6–25)

* **m1 (p. 16).** The list reads "硬点（α_k = 0，所有线离壳）；C1；C2；S". If all lines are off shell, Landau condition (i) forces every α_j = 0, which is excluded. So the "hard point" is the absence of a pinch, not a solution. The soft-quark configurations k = p_1 (line p_1 − k at zero momentum) and k = −p_2 do solve the Landau equations (only α_2 ≠ 0, resp. α_3 ≠ 0). They are the endpoints x = 1 of C_1 = {k = x p_1}, resp. of C_2. My power counting gives a soft-quark region ∼ λ² relative to the leading term, so these points matter only at NLP. Confirmed (minor).
* **m2 (p. 25, Rem. 3.15).** The text says U(+∞) is "一个常数色矩阵，即一个整体规范变换". But U(+∞) = P exp(ig∫_{−∞}^{∞}A(z⁻)dz⁻) depends on the gluon field. The conclusion still holds, as the remark itself says, through U(w⁻)U†(0) = W[w⁻,0]. Confirmed.
* **m3 (p. 23).** The reference calls K^{μν} = n^μk^ν/(n·k) "Grammer–Yennie 分解 [15] 的'K 部分'". GY's K-photon, as reproduced by Sen–Indumathi–Choudhury (arXiv:1812.06468, sec. 3.1), is symmetric: b_k(p_f,p_i)k_μk_ν, with b_k = ½[(2p_f−k)·(2p_i−k)/(((p_f−k)²−m²)((p_i−k)²−m²)) + (k↔−k)]. The one-sided form with i0 is the adaptation used in the Collins–Soper–Sterman approach: DGOPS's (GY-collin), (GY-soft) follow Collins 2011. The CSS review says only that its methods are "motivated by" GY. Confirmed; the original PRD 8 (1973) 4332 was not seen directly.
* **m4 (pp. 13–14, Prop. 2.4).** The proof claims "对未重整化的分布，f_{q/A} ≥ 0". The bare matrix element is UV divergent, so this positivity is formal. The proof uses A⁺ = 0 gauge, whose 1/k⁺ prescription problem is raised in Rem. 2.3. The anticommutator term ∝ δ(w⁻) at w_T = 0 is the divergent constant δ²(0) (the reference: "由正规排序去掉"). Support of the renormalized PDF is not addressed. Confirmed.
* **m5.** (1.1) on p. 6 writes an absolute remainder "+O((Λ/Q)^p)", although item (c) says relative. σ̂_ij(ξ_A, ξ_B, …) is schematic. The ν = P·q clash appears on **p. 11** ("对 ν = P·q > 0", right after W^{μν} with index ν). Grade C on p. 7 mixes "低阶验证" ([P]-type content) with "猜想" ([C]). Confirmed; locator correction p. 11.

## 6. R-m06 — m6–m12 (pp. 12–49)

* **m6 (p. 34, Ex. 5.2)** (`rm06_checks.py`). Take k = ξP massless.
  * ½Tr[k̸γ^μk̸γ^ν] = 2ξ²P^μP^ν exactly: the T_2 structure comes only from k̸.
  * ½Tr[k̸γ^μq̸γ^ν] = ξ(P^μq^ν + q^μP^ν) − ξP·q g^{μν}: only T_1 and gauge terms.
  * The symmetric part of γ^μk̸γ^ν is k^μγ^ν + k^νγ^μ − g^{μν}k̸. So for T_2 the operator index γ^{μ1} is a vertex γ and k̸ supplies the derivative.
  * The reference's "q̸ 与外顶点的 γ 矩阵组合给出 γ^{μ1}" is wrong for T_2. Confirmed.
* **m7 (p. 32).** The reference's example "e^{−c√s/Λ} sin(…)" is not one of the standard forms. Shifman (hep-ph/0009131) lists three regimes:
  * (i) finite-distance (instanton) singularities: s^{−κ/2} sin(√s), power damped;
  * (ii) N_c = ∞: s^{−η/2} sin(s);
  * (iii) large finite N_c: exp(−αs) sin(s), with the resonance model giving 2exp(−2πsB/(σ²N_c))cos(2πs/σ²).

  That is the e^{−δ−γs}sin(α+βs) form. Confirmed.
* **m8 (p. 49).** M_N[(ln^k(1−z)/(1−z))_+] / [(−1)^{k+1}ln^{k+1}(N̄)/(k+1)] → 1 (k=1: 1.017 at N = 10⁴; k=3: 1.115). The k = 1 harmonic-sum form agrees to 15 digits. A plain ln^k(1−z) moment behaves like (−1)^k ln^k N/N. So α_s^n[ln^{2n−1}(1−z)/(1−z)]_+ ↔ α_s^n ln^{2n}N. Confirmed.
* **m9.** τ = Q²/s on p. 12 (hadronic) and τ = Q²/ŝ on p. 49 (partonic). Confirmed.
* **m10 (pp. 39–40).** Only the Dirac projection ¼Tr[Hγ⁻]Tr[γ⁺J] is written; no colour average appears. For a colour-singlet target, J_{ij} = δ_{ij}Tr_cJ/N_c, so Tr_c[HJ] = (1/N_c)Tr_cH Tr_cJ is needed. Confirmed.
* **m11 (p. 29).** Solving the RG order by order (sympy, through α_s⁵): deg a_0 = 0, deg a_n = n − 1 for n ≥ 1, deg Π_n = max(1, n). Confirmed.
* **m12 (p. 49).** "有限部分的完整计算是标准的 [30, 31, 33]，结果为 c_q": the finite parts are quoted. The printed c_q and C_{2,g} agree with the standard MS-bar forms (C_F[…−(9/2+π²/3)δ(1−z)], T_F[(z²+(1−z)²)ln((1−z)/z) − 1 + 8z(1−z)]). The 1/(D−2) gluon average, the DIS scheme and F_L are not mentioned. Confirmed.

## 7. R-m13 — m13–m16 (pp. 53–71) and OUR-5

* **m13 (p. 56, Fig. 34)** (`rm13_checks.py`, independent code). Kinematics ŝ = 10, Q² = 3 (z = 0.3); couplings, colour and the 1/4 average stripped.
  * Feynman gauge: t|M_e|² → −80.000 = −8ŝ; t·2Re(M_dM_e*) → +33.598 → 16ŝz(1−z) = 33.6; total → −46.40 = −8ŝ[z²+(1−z)²] (∝ P_qg).
  * Light-cone gauge (n ∥ p_1): t·2Re → −0.0039 → 0 and t|M_e|² → −46.398, so the whole pole sits in |M_e|².
  * The totals in the two gauges agree with −8(s/t + t/s + 2uQ²/(st)).

  Confirmed. Print the analytic forms, not −80/+33.6.
* **m14 (p. 67).** With M = −γ¹γ³γ⁰ (Peskin–Schroeder P and T, either order), M†γ⁰*γ^{μ*}M = +γ⁰γ^μ for all μ. So Vψ̄(w)γ^μψ(0)V⁻¹ = +ψ̄(−w)γ^μψ(0) without Hermitian conjugation; the axial bilinear changes sign. Colour bookkeeping: under antiunitary V, t^a → t^{a*} = t^{aT}, which reverses the path ordering; the reference hides this in "适当的色共轭约定下".
  * ε_T: with ε^{0123} = +1 and the hadron along +z, Trento's −f_{1T}^⊥ε^{μνρσ}P_μk_νS_ρn_σ/(M P·n) equals −f_{1T}^⊥(P̂×k_T)·S/M = −f_{1T}^⊥(k¹S² − k²S¹)/M. So (10.9) needs ε_T^{12} = +1 (checked numerically).
  * Caution: the Trento paper's own ε_⊥^{12} = −1 refers to ε_⊥^{ρσ} = ε^{μνρσ}P_μq_ν/(…) in the frame with the photon along +z. That is a different tensor and frame; reproduced −1.000000.

  Confirmed.
* **m15 (pp. 68–69).** (11.2) has remainder O(Λ²/Q⁴). The reference's own Fig. 44 caption says the endpoint region (area ∼ (Λ²/Q²)ln(Q²/Λ²)) is suppressed "by Λ²/Q² (up to a log)". Check: the exact area of {x̄ȳ ≤ r} is r(1 + ln(1/r)), agreeing to 6 digits. So by the reference's own estimate the remainder is O((Λ²/Q⁴)ln(Q²/Λ²)). Confirmed as an internal-consistency correction.
* **Small-b remainder (p. 66, Cor. 10.5: "+O(b_TΛ)") and OUR-5.**
  * Symmetry: for unpolarized f_1 (P_T = n_T = 0, b = (0⁺, b⁻, b_T)), every invariant depends on b_T only through b_T² (`rour2_checks.py`). An O(b_T) term would need a transverse vector (S_T, P_T, n_T).
  * Literature: Scimemi–Vladimirov JHEP 03 (2017) 002 — "the leading power corrections are ∼ b²"; an exponential ansatz "would imply the corrections ∼ √b² to the small-b OPE, that cannot appear without extra scaling parameter". Their eq. for F carries + O(b⁴) after the b² term, which scales as x b² (PDF) and b²/z (FF).
  * Moos–Vladimirov JHEP 12 (2020) 145: twist-2/3 contributions come with (M²b²)^n.

  Confirmed: O((b_Tm)²) up to logarithms.
* Spot checks of the other m16 items (CLAIMS full text; not in the batch statement):
  * "χ(b) as written is IR divergent": confirmed, ∫d²k e^{ik·b}/k² diverges logarithmically; App E's (E.32) adds the window Θ.
  * "(9.3) omits (2π)² / conflates total and relative momenta": consistent on reading but normalization dependent.
  * "Rem. 9.6 'no Glauber region in DIS' holds only for unphysical ω": **not an error**. Rem. 9.6 (p. 62) already says "前向振幅 T^{μν} 在非物理区没有末态，因此 Glauber 区根本不出现" and treats the physical region by unitarity. Do not print this item.
  * The f_π and Fig. 46 items were not re-verified.

## 8. R-m17 — m17–m22 (pp. 72–83, 231–238)

* **m17 (p. 73, (12.2)).** CdFR's eq. (ic12gen) fixes z_1 > 0 and contains "−2Σ_{j≥3} **T**_2·**T**_j f(ε; z_2 − i0 s_{j2})". So "T_coll" must be **T**_2, the collinear parton whose momentum fraction can be negative. For n = 3 QCD partons the operator reduces to −(1/ε)(C_12 + C_2 − C_1)f(…), "proportional to the unit matrix in colour space" (CdFR §"n = 3"). For n ≥ 4, initial-state splittings "necessarily involve colour correlations". Confirmed.
* **m18 (pp. 77–78).**
  * The reference itself says the direction is fixed by the external states. The imprecise part is "正确的处方 … 在拉氏量层次上看不出来".
  * CKKL (PRD 71 (2005) 056001, §2): in SCET_I the soft Wilson line is obtained by attaching usoft gluons to collinear fields in the eikonal approximation. Incoming quark: Y from −∞ to x; outgoing quark: Ỹ† from x to ∞. Matching and LO rules fix the direction.
  * The reference calls A_s at λ²Q "软", whereas in SCET_I it is ultrasoft; the reference itself notes this in (3.7).

  Confirmed (wording).
* **m19 (p. 81).** Prop. 14.1 is followed by "论证" and ends "只是论证而非证明". The proven case:
  * David, NPB 209 (1982) 433, INSPIRE abstract: in the 1/N expansion of the 2D O(N) σ-model, "We prove that renormalons cancel between the different terms of the operator expansion".
  * David NPB 234 (1984) 237 (the reference's [114]).
  * Beneke–Braun–Kivel PLB 443 (1998) 308: OPE of the self-energy at NLO in 1/N, no extra power corrections.
  * NSVZ was not re-read.

  Confirmed.
* **m20 (p. 83).** The summary says "扭度的奇偶性等于手征性，被完整证明" without qualification. Lemma C.43 (p. 110) is stated for operators "属于对称无迹秩 j 表示". The transversity operator ψ̄σ^{μν}γ_5D…ψ (twist 2, chiral-odd, mixed symmetry) violates the unqualified rule. Confirmed.
* **m21 (p. 72, (12.1)).** With E_h dσ/d³p_h and dz/z², σ̂_{ab→c} must be E_c dσ̂/d³p_c, since d³p_h/E_h = z²d³p_c/E_c. Confirmed.
* **m22 (bibliography; INSPIRE and arXiv).** Each item:
  * [27]: published "An Analytic Calculation …" ✓.
  * [34]: Erratum NPB 644 (2002) 403 omitted ✓.
  * [53]: title paraphrased ✓.
  * [56]: the arXiv title ends with "?" ✓ (INSPIRE strips it).
  * [59]: Erratum PRD 55 (1997) 5853 omitted ✓.
  * [60]: claimed "arXiv title" — not confirmable; INSPIRE lists the same title. Do not print.
  * Missing references: Collins 2007, AS2009, Mitov–Sterman PRD 86 (2012) 114038, Becher et al. 2025, KQS 2012, NQS PLB 2005, BBNS 2000 and Nachtmann 1973 are all absent from [1]–[145] ✓.
  * The misattributions of [53]/[60] are the separate claims R-M18/R-M19.

## 9. R-m23 — m23–m25 (pp. 91–158)

* **m23 (pp. 101–102, Ex. C.27)** (`rm23_checks.py`). I(q) = ∫d⁴k[Δ(q−k) − Δ(q)]Δ(k)³ with m = 1 gives q⁴I = −5.4648 (q = 10), −4.94952 (100), −4.935040 (1000), −4.934833 (3000), tending to −π²/2 = −4.934802.
  * The correction behaves like c·m²q⁻⁶ln q with c ≈ −39.5 ≈ −4π².
  * No q⁻⁴ln q term: by 4D harmonicity, the angular average of 1/(q−k)² equals 1/q² for |k| < |q|.
  * The unreduced piece is π²/(2m²q²), as the reference says.

  Confirmed (= N15's value).
* **m24 (App C details).** Each sub-item:
  * **Fig. 55 "cubic vertices outside the stated model" — refuted.** The model (p. 91) is "有质量的标量场（量纲 1）与旋量场（量纲 3/2），相互作用为量纲 4 的单项式", and ψ̄ψφ has dimension 4. Fig. 55 (rendered p. 92) uses undistinguished lines. (a) is a fermion loop with two fermion self-energies; (b) is a fermion loop with a scalar rung. Every cubic vertex is a Yukawa vertex.
  * Cor. C.18: Def. C.5 defines ω only for connected γ, while γ(S′) may be disconnected; the proof uses (C.4) additively. Confirmed (minor).
  * "唯一外部输入是定理 C.8" (p. 88): Def. C.7 (p. 92) also invokes Zimmermann's canonical routing compatibility [78]. Confirmed (over-statement).
  * Lemma C.64 (p. 121): edge-of-the-wedge is applied on a 1D slice after a 4D support statement, while the Q²-smearing justification appears only for positivity. Plausible; one sentence is missing.
  * Thm. C.66(i) (p. 123): ‖γ(α)‖ ≤ Cα is applied with dimensionful mass-mixing entries (γ_ij ≠ 0 only for d_j ≤ d_i). Rescaling is needed. Plausible.
* **m25.**
  * (i) Prop. D.28(a) proof (p. 145) invokes "引理 D.20(a) 的符号条件". Lemma D.20 concerns deformation of soft momenta, while in the DIS unphysical region "只连到靶喷注上的软线留在 J 中，不作近似". Confirmed (misinvoked).
  * (ii) Table 5 reproduced to all printed digits from Q²I = ∫dt du[λ²(1−t)+tu(1−u)]⁻¹, a Feynman-parameter form I re-derived. Diff − t(2L²−4L−4+2π²/3) = 3.9·10⁻⁶ (t = 10⁻⁴), 9.6·10⁻¹⁰ (10⁻⁶), 2.9·10⁻¹⁷ (10⁻¹⁰). The reference's fit "2λ²L²−3.9λ²L" gives 9.7058·10⁻⁸ against the exact 9.7086·10⁻⁸.
  * (iii) The Collins remainder against (D.32) in Q̃², with Q² = (Q̃²+m²)²/Q̃²: Q⁴r/m² = −3.8972, −3.9638, −3.99268, …, −3.9999967 for Q²/m² = 10², 10³, 10⁴, …, 10⁸. [Q⁴r/m² + 4]/(t(L² − 15 + π²/3)) → 1. So r = −4m²/Q⁴ + (m⁴/Q⁶)(L² − 15 + π²/3) + …, with no NLP logarithm. Table 5 therefore compares I with L² + π²/3 in Q² and mostly measures the Q̃² → Q² conversion. N12's number reproduced: ∫r = −0.01734343395809.
  * (iv) C_S: ∫₀^∞dk k^{−ε}/(m² + 2P′k) = (m²)^{−ε}(2P′)^{ε−1}Γ(ε)Γ(1−ε), a Beta function (6.4328272057014 vs J(ε) = −2.532). It reproduces (D.31)'s B(ε) to 14 digits. Confirmed.
  * Typo "假设假设" on pp. 128 and 146 ✓.
  * Lemma D.23(iii) "edge case": not verified (REFDOC: "plausible"). Excluded.

**Verdict: confirmed for everything except the Fig. 55 sub-item (wrong) and the D.23(iii) edge case (unverified), which must not be printed.**

## 10. R-m26 — m26–m27 (App E)

* **E.28(iii) (pp. 192–193).** The proof's near-pole step needs |E′| on the real axis. (J1)(J2) give analyticity of J^fi only in Im k < 0, so that step is not justified by the stated hypotheses. The fix: E = J^fi + iJ_+/(k − iλ_J) is analytic in the closed LHP and O(k⁻²), so closing in the LHP gives ∫dk/2π E R_↓ = −iΣr_iE(z_i). Numerically, −0.4155964052−0.0263677035i on both sides (`rm26_checks.py`). Bound: for Im z ≤ 0, |z − iλ_J| ≥ |z|, hence |E(z)| ≤ Mλ_J/|z|² + |J_+|λ_J/|z|² ≤ 2Mλ_J/|z|² (sample maximum 1.007·Mλ_J/|z|²). With |z_i| ≥ 2Λ this gives O(Mλ_J‖R‖/Λ). Confirmed.
* **Vertex sign (p. 195).** "J_A 的领头耦合是 −igJ_A^{+a}" contradicts the reference's D_μ = ∂_μ − igA_μ (2.5) and its Fig. 4 (vertex +igγ^μt^a). The correct sign is +ig. The slip has no effect on V_G, since (±ig)² = −g². Confirmed.
* **(E.30) (p. 194).** It is stated as a relative error R(0)J_A(0)[1+e_j]. Lemma E.28(iii) gives an absolute error O(Mλ_J‖R‖/Λ), with M ≥ |J_±| possibly ≫ |J(0)|. Counterexample (J(0) = 10⁻³, M ∼ 50, λ_J/Λ = 0.02): relative error 374, while the absolute bound holds. Confirmed.
* **Rem. E.49(2) (p. 218).** (E.51) is (1+A_1+A_2)†(1+A_1+A_2) = 1 − ¼C_Aχ²X + O(χ³). Σ_{ab}{T^a,T^b}{T′^a,T′^b} = 4X² + C_AX was verified for F⊗F, F⊗F̄ and F⊗A in SU(3). The missing contribution is therefore +¼C_Aχ²X, while the text says "缺少的 −¼C_Aχ²X". Confirmed.
* **σ in Im(n·K) (pp. 208, 213).** The deformation has Im q_a⁻ = tσf_a, so Im(n·K) = tσΣf_a and σIm(n·K) = tΣf_a ≥ 0. The text writes "Im(n·K) = tΣf_a … 与 σ 同号", which is consistent only with σ included. Confirmed.
* **w_12 (p. 195).** w_12 = z_1/(z_1+z_2) with z_j = k_{Tj}²/(2k_j⁺). The reference says it depends on k_j⁺; it also depends on k_{T1}²/k_{T2}² (at fixed k⁺: 0.667 → 0.889 when k_{T1}² goes 1 → 4).
  * Checks: P(insertion 1 earlier) = z_1/(z_1+z_2), by Monte Carlo and by an exact complex-pole integral. The N = 3 weights sum to 1.

  Confirmed.

## 11. R-OUR1 — OUR-1 … OUR-4 (our spec; the reference is right)

* **OUR-1** (`rour1_ff.py`). Hadron frame (p_T = 0), light-cone gauge, X = one gluon.
  * The trace is T = Tr[γ⁺k̸γ^νp̸γ^μk̸]d_{νμ} = 8p⁺l_T²(1+z²)/(1−z)² exactly (6 points), with k² = l_T²z/(1−z).
  * With the prefactor z^{1−2ε}/(4N_c) (z in 4D), d(z) per d²l_T equals the target (α_s/2π)C_F(1+z²)/((1−z)l_T²)·(1/π) to 10⁻¹⁵.
  * With 1/(4N_c z), the result is exactly 1/z² (25, 4, 1.5625) times larger.
  * Jacobian: d^{2−2ε}p_{hT} = z^{2−2ε}d^{2−2ε}k_T. The reference's (2.13) itself uses z^{d−3}/(4N_c).

  Confirmed.
* **OUR-2.** The reference's Ex. D.1(c) shows that single chain terms are not in L¹. Power counting: T_{C1}Γ needs ε < 0 at the rapidity end k = (a²κ⁺, κ⁻, aκ_T) and ε > 0 in the UV direction. The scaleless T_{C1}T_SΓ ∝ ∫₀^∞dσ σ^{−1−ε} diverges for every ε. A termwise induction is therefore impossible; the theorem must be conditional on subtraction-level properties. Confirmed.
* **OUR-3.** Rest frame, Euclidean q = (iq⁴, **q**): ω = 2iMq⁴/Q² is purely imaginary with |ω| ≤ 2M/Q. Under (C.31)'s restriction |**q**| ≥ Q/2 (P̂² ≥ M²/4), |ω| ≤ √3M/Q. Scan: 0.18800 = 2M/Q and 0.16281 = √3M/Q. Confirmed with this precision. The reference also calls (5.6) "形式级数" (p. 34).
* **OUR-4.**
  * For Glauber k = (λ², λ², λ), deforming only k⁻ by iκ|k_T| gives |k⁺k⁻|/k_T² ≈ 2λ (∼λ³ absolute), so k stays in G_δ.
  * The simultaneous deformation along e_G = n̄ − n = n_B − n_A gives |k⁺||k⁻| ≥ κ²k_T² and Re k² ≈ −0.82k_T² < 0.
  * Agrees with the reference's (E.42), Rem. E.13 and Lemma D.20(b) (one component: |k⁻| limited by the soft pole at k_T²/(2|k⁺|)).

  Confirmed.

## 12. R-OUR2 — OUR-5 … OUR-8

* **OUR-5:** see §7 (symmetry argument plus Scimemi–Vladimirov 2017 and Moos–Vladimirov 2020). Confirmed: O((b_Tm)²) up to logs.
* **OUR-6.** The reference's Prop. D.28(b) itself says real-ω bounds give no derivative bounds. Example: r(ω) = π⁻¹∫₁²sin(K(ω′−1))/(ω′−ω)dω′. On |ω| ≤ 0.8, max|r| = 0.150, 0.0136, 0.00144 for K = 10, 100, 1000, while max|Im r(ω+i0)| on [1,2] stays 1. Real-segment (or disc) bounds do not control the discontinuity pointwise. Confirmed.
* **OUR-7.** The arXiv comments say the paper was "Based on the talks delivered at the VIII-th International Symposium on Heavy Flavor Physics, Southampton … and … 'Gribov-70' … To be published in the Boris Ioffe Festschrift 'At the Frontier of Particle Physics/Handbook of QCD', Ed. M. Shifman (World Scientific, Singapore, 2001)".
  * INSPIRE: parent record "At the frontier of particle physics. Handbook of QCD. Vol. 1-3" (WS 2001), vol. 3, pp. 1447–1494, DOI 10.1142/9789812810458_0032.
  * The Southampton proceedings (PoS hf8) list only a talk "Quark-Hadron Duality: the 't Hooft Model and Beyond" with no full text.

  Confirmed.
* **OUR-8.** The forward on-shell partonic matrix element ⟨p|TJJ|p⟩ (p² = 0) has the partial sum p + (−p) = 0, so the external momenta are exceptional and also non-Euclidean. It lies outside the Euclidean non-exceptional OPE theorems; the reference itself notes the IR-divergent zero-momentum Taylor coefficients (p. 101). Confirmed.
