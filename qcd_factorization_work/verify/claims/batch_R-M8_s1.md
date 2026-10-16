# Verification batch R-M8 – R-M18 (stage 1, independent verifier)

Date: 2026-10-10. Default stance: skeptical. All eleven claims are of kind `correction_of_reference_doc` (source: `refdoc/REFDOC_ANALYSIS.md` ERR-M8 … ERR-M18).
Criterion applied: a correction is confirmed only if the physics statement our monograph would print is correct. Page locators of the reference are checked too, but the reference is not citable (REFDOC S62), so a wrong locator alone does not refute a claim. It is recorded as a precision note.

## 0. Method and sources

* **Reference document.** I read `factorization_qcd-2.pdf` through the page-split text `refdoc/refdoc.txt` (form-feed = PDF page; printed page numbers equal PDF page numbers). Pages read: 1, 6–8, 28–37, 39–48, 62–65, 70–75, 84, 136–137, 141, 149–160, 231–238 (bibliography). Pages 64 (200 dpi) and 84 (150 dpi) were also rendered with `pdftoppm` and inspected as images.
* **Primary literature.** Downloaded independently from arXiv (e-print sources, read as text only; latest versions). Bibliographic data were checked with the INSPIRE API.
  * Collins–Frankfurt–Strikman, hep-ph/9611433 v2 (Jul 1997) = PRD 56 (1997) 2982 [Collins:1996fb]
  * Bodwin–Braaten–Lepage, hep-ph/9407339 v2 + erratum file = PRD 51 (1995) 1125, Erratum PRD 55 (1997) 5853 [Bodwin:1994jh]
  * Moch–Vermaseren–Vogt, hep-ph/0403192 = NPB 688 (2004) 101 [Moch:2004pa], whose eqs. (4.6)–(4.7) reproduce Curci–Furmanski–Petronzio NPB 175 (1980) 27 [Curci:1980uw]
  * Collins–Gamberg–Prokudin–Rogers–Sato–Wang, arXiv:1605.00671 = PRD 94 (2016) 034014 [Collins:2016hqq]
  * Mankiewicz–Piller, hep-ph/9905287 = PRD 61 (2000) 074013 [Mankiewicz:1999tt]
  * Diehl–Gousset–Pire, hep-ph/9808479 = PRD 59 (1999) 034023 [Diehl:1998pd]
  * Collins–Diehl, hep-ph/9907498 = PRD 61 (2000) 114015 [Collins:1999un]
  * Collins–Qiu, arXiv:0705.2141 v2 = PRD 75 (2007) 114014 [Collins:2007nk]
  * Rogers–Mulders, arXiv:1001.2977 v2 = PRD 81 (2010) 094006 [Rogers:2010dm]
  * Collins, arXiv:0708.4410 ("2-soft-gluon exchange and factorization breaking", not published in a journal) [Collins:2007jp]
  * Poggio–Quinn, PRD 14 (1976) 578: INSPIRE abstract only
* **Scripts** in `verify/claims/batch_R-M8_s1_scripts/` (run with `python3 -I`; logs `*.log` next to them):
  * `rm10_pplusminus.py`: first moments of P^(1)± coded from MVV x-space formulas.
  * `rm14_oneloop_pdf.py`: one-loop quark-in-quark PDF with a gluon mass, every graph. Uses explicit 4×4 γ matrices, the l⁻ contour, the self-energy and the ε-expansion.
  * `rm15_tmd_softfactor.py`: soft-factor bookkeeping of the TMD product with the exact one-loop Y coth Y soft factor.
  * `rm17_rm18_checks.py`: Wandzura–Wilczek twist-3 DAs, the endpoint behaviour of the Mankiewicz–Piller integrals, and the SU(3) colour trace.
* **Project scripts re-run, as named in the recipes.** All pass:
  * `refdoc/work_R2/checks/check_Pplusminus.py`: output identical to its log.
  * `research/c_pdf/scripts/s2_oneloop_qq.py`: 29/29 PASS.
  * `research/c_pdf/scripts/s5b_gauge_independence.py`: 28/28 PASS.
  * `research/c_exclusive/scripts/s8_meson.py`: 11/11 PASS.
  * `research/c_tmd/scripts/soft_factor.py` was read. It checks the soft factor itself, not the step-(iv) identity.

## 1. Summary

| id | verdict | what must change before printing | already in the literature? |
|---|---|---|---|
| R-M8 | **confirmed** | Locator: p. 84 already says γ*_L (Table 1 row "DVCS、γ*_L p → M p"); the omission is only on p. 1 (abstract, item (ii)) and p. 7 (Def. 1.1, list of grade-B results). | Yes. CFS 1997 (σ_L only; endpoint contributions unsuppressed for γ*_T). Explicit divergences: Mankiewicz–Piller 2000. |
| R-M9 | **confirmed** | Cite BBL §II.E for the duality caveat ("smearing in the energy is not available to us in the case of quarkonium annihilation") and BBL §V for the all-order *sketch*. Locators: grade A on p. 7, A* on pp. 75, 84. | Yes. The caveat is stated by BBL themselves. |
| R-M10 | **confirmed** | Always state the normalisation: 0.71931 C_F(C_F−C_A/2) is for P = Σ(α_s/2π)^{n+1}P^(n). It is 2.87725 C_F(C_F−C_A/2) in the a_s = α_s/4π normalisation. Exact value: 13/4 − 3ζ₂ + 2ζ₃. Precision: from NNLO on, the total valence q−q̄ evolves with P^v_ns = P^− + P^s_ns. | Yes. CFP 1980; MVV 2004 eq. (4.7). |
| R-M11 | **confirmed** | None. R_0 = the reference's own R_H of Ex. D.48. | Region set as in Collins 2011 ch. 10 and the reference's Ex. D.48. |
| R-M12 | **confirmed, with a precision** | For DIS the regrouping input is Prop. D.42's (Com)(Abs), not Ass. D.37; D.37 (W1)(W2) is the input for the other processes (Thm. D.46). The overclaim proper is on p. 39. On p. 7 the phrase is attributed to the CSS standard and qualified at once. | Statement about the reference only. |
| R-M13 | **confirmed** | The finiteness route is Poggio–Quinn's corollary ("any physical discontinuity of Green's functions is also infrared finite"); it is not new. | Yes. Poggio–Quinn PRD 14 (1976) 578. |
| R-M14 | **confirmed** | Note that Ex. 10.1 (p. 63) *mentions* the real–virtual ξ→1 cancellation qualitatively, but Prop. 7.1 does not compute it. Our finite part is re-derived independently. | Standard. Collins 2011 ch. 9 computes the one-loop PDF graph by graph. |
| R-M15 | **refuted** | The proposed "correct" formula is not correct. By linearity of ln S̃ it is *identical* to the printed one. Either both are finite (reference's convention: ±∞ ≡ the regulators y_A, y_B; then the printed formula is exactly Lemma D.38) or both diverge (independent limits). Print f̃_A f̃_B = f̃^unsub_A(y_{P_A}−y_B) f̃^unsub_B(y_A−y_{P_B}) / S̃(y_A,y_B). | — |
| R-M16 | **confirmed** | Reference verified on INSPIRE; add it to the bib. The low-q_T cutoff has a precursor in CSS 1985's Q_T^min (CGPRSW say so). | Yes. CGPRSW PRD 94 (2016) 034014. |
| R-M17 | **confirmed, with precisions** | Say "in the Wandzura–Wilczek approximation" (M–P drop genuine qGq twist 3). The reference's "∫φ/z²" is imprecise rather than of the wrong degree, since it is also logarithmic. The real point is that the divergence persists for any φ_∥ with ∫φ_∥/u ≠ 0, including endpoint-suppressed φ_∥. The vanishing of the leading-twist γ*_T→V_T amplitude: DGP state it "for any spin state of the incoming virtual photon"; Collins–Diehl close the all-order loophole. | Yes. M–P 2000; DGP 1999; Collins–Diehl 2000. |
| R-M18 | **confirmed** | Locator: the "non-abelian model" sentence is in Thm. 12.3 on p. 73; the RM description is on p. 74. | Yes. CQ 2007 §II; RM 2010 eq. for the colour factor; Collins 2007. |

---

## 2. R-M8: meson electroproduction factorizes for longitudinal photons only

**Reference.**
* p. 1 (abstract, item (ii)) lists "硬遍举介子电产生" among the all-order (grade B) results. There is no photon-polarisation qualifier.
* p. 7 (Def. 1.1, list of grade-B results) says "硬遍举介子电产生（第 11 节）", also without a qualifier.
* p. 84 (Table 1) reads **"DVCS、γ*_L p → M p | GPD、分布振幅 | B"**. This was checked on the 150-dpi image: the subscript L is there. So p. 84 is *not* an instance of the omission.
* The body is correct. Thm. 11.4 (p. 70) is stated for γ*_L(q)+p → M+p′ and adds: "横向极化光子的振幅被压低 1/Q，且一般不能以同样的形式因子化（端点发散…）".

**Literature (CFS, arXiv v2 source, Sec. II).** "Indeed, we find we can derive a simple factorization theorem only for longitudinally polarized photons, since then the contributions from the endpoints z→0 and z→1 of the meson wave function are power suppressed … For transverse polarization, this suppression does not happen, and a more complicated theorem is needed." The section "Transversely polarized photons" adds:
* the γ*_T amplitude is suppressed by 1/Q;
* the endpoint (soft-quark) regions are leading for γ*_T;
* "the factorization theorem … does not hold … with a transverse photon, we must not only change the hard scattering factor but we must also put in more general objects for the non-perturbative factors".

Mankiewicz–Piller 2000 compute the twist-3 γ*_T → ρ_T amplitude explicitly and find divergent endpoint integrals (§12 below).

**Verdict: confirmed.** The physics statement is correct. Only pp. 1 and 7 carry the omission.

## 3. R-M9: inclusive quarkonium decay is [A], not "A*"

**Reference.**
* p. 7 puts inclusive quarkonium decay in grade A ("以 NRQCD 作为 QCD 的有效理论为前提——重夸克偶素的单举衰变").
* p. 75, heading "NRQCD 因子化（衰变为 A* 级…）". The text says the rate is ⟨H|Im T|H⟩ and "其严格程度与 OPE 相同（给定 NRQCD 作为 QCD 的有效理论；这就是表 1 中的 A*）". The non-perturbative statement is made conditional on "附录 C 中那一类关于非微扰 OPE 的假设".
* p. 84 (Table 1): "重夸克偶素衰变 | NRQCD 矩阵元 | A*".

**Literature (BBL).**
* §II.E "Space-Time Structure of Annihilation" localises the annihilation within 1/M, using KLN for final-state divergences. It then states: "The locality of the annihilation process is spoiled if the final-state gluons form a narrow resonance … In the case of e⁺e⁻ annihilation, one can deal with this problem by forming a suitable average of the cross section over the resonance region [PQW] … **This solution of smearing in the energy is not available to us in the case of quarkonium annihilation.** Fortunately, there are no known narrow glueball resonances …"
* This is exactly the local-duality caveat. The rate is evaluated at a fixed Minkowskian point (M_H, or 2M in the matching). No external variable can be smeared or continued to the Euclidean region, so a non-perturbative statement needs (local) quark–hadron duality.
* The reference itself (p. 32, §4.3) concedes that a pointwise R(s) needs "定域夸克–强子对偶", while the smeared R̄ does not. Its own App. C assumptions (Euclidean OPE, dispersion relations, Wightman axioms) therefore do not cover the decay rate.
* §V "Perturbative Factorization": "we *sketch* the connection … the aim is to demonstrate that, to all orders in perturbation theory, …". The argument uses topological factorisation, the controlling momentum, KLN, Taylor expansion in p and Fierz, with explicit checks through O(α_s³). This fits our grade [A].
* §III.E "Factorization-Scale Dependence": f_n(Λ) and ⟨O_n⟩_Λ depend on the NRQCD cutoff. This supports the parenthetical in ERR-M9.
* The 1997 erratum concerns velocity-scaling rules only and does not affect this.

**Verdict: confirmed.** Precise statement: NRQCD factorisation of inclusive quarkonium annihilation decays is [A] in perturbation theory (BBL's all-order argument, given in sketch form). Its non-perturbative validity requires local quark–hadron duality at the fixed scale 2M. Energy smearing (as in e⁺e⁻) is unavailable, as BBL state, so it is not "as rigorous as the OPE". (The recipe pointed to "BBL §V–VI"; the decisive text is in §II.E.)

## 4. R-M10: P^+_NS ≠ P^−_NS beyond LO

**Reference.**
* p. 34, (5.8): A_q^(n) = ∫_{−1}^{1} ξ^{n−1} f_q = ∫_0^1 ξ^{n−1}[f_q + (−1)^n f_q̄], with "i = q 遍历各味夸克，A_q^(n) 已包含反夸克的贡献".
* p. 36, Prop. 5.4: γ^(n)_ij = −2∫_0^1 z^{n−1} P_ij(z,α_s), stated as equivalent to DGLAP (5.10) for one set of kernels P_ij.
* p. 37 notes that odd n are needed for f_q − f_q̄ ("…其重整化同样定义了 γ^(n)"), but keeps one P_qq for both parities.

In the operator basis {q flavours, g}, the moment of DGLAP gives γ^(n)_qq = −2[M_n(P^V_qq) + (−1)^n M_n(P^V_qq̄)] + (sea terms). So one kernel for all n holds only if P^V_qq̄ = 0. That is true at LO and false at NLO.

**Independent computation (`rm10_pplusminus.py`).** I coded MVV's x-space P^(1)+_ns (their eq. (4.6), = CFP 1980) and P^(1)−_ns = P^(1)+_ns + 16C_F(C_F−C_A/2){p_qq(−x)[ζ₂ + 2H_{−1,0} − H_{0,0}] − 2(1−x) − (1+x)H_0} (their eq. (4.7)). The +-prescriptions and δ-terms are included explicitly.

* Quark-number check: ∫_0^1 P^(1)− = 0 separately for C_AC_F, C_F n_f and C_F² (to 10⁻³⁰). This validates the coding.
* ∫_0^1 P^(1)+ = 5.754492846 C_F² − 2.877246423 C_AC_F = 5.754492846 C_F(C_F−C_A/2) (MVV normalisation).
* Hence, with P^± = P^V_qq ± P^V_qq̄ (MVV eq. (2.4)) and P = Σ(α_s/2π)^{n+1}P^(n):
  **∫_0^1 P^{V(1)}_{qq̄} = (13/4 − 3ζ₂ + 2ζ₃) C_F(C_F−C_A/2) = 0.719311605774509 C_F(C_F−C_A/2)**.
  For SU(3) this is −0.159847.
* The MVV difference term equals the CFP/ESW form 2p_qq(−x)S₂(x) + 2(1+x)ln x + 4(1−x) pointwise (difference ~10⁻³⁰), using H_{−1,0} = ln x ln(1+x) + Li₂(−x).
* The project script `check_Pplusminus.py` gives the same 0.719311605774509.

**Verdict: confirmed.** Precision notes:
* Always quote the normalisation. The value is 4× larger (2.87725) for a_s = α_s/4π.
* "Odd n ⟺ q−q̄ with P^−" is exact for flavour non-singlet C-odd combinations. For the total valence Σ(q−q̄), MVV eq. (2.5) gives P^v_ns = P^− + P^s_ns, with P^s_ns ≠ 0 from NNLO.

## 5. R-M11: the two-rung ladder has three leading regions

**Reference.** The caption of Fig. 24 (p. 41) reads "两梯级梯形图及其两个领头区": R1 (k1 collinear, k2 hard) and R2 (both collinear). The text on p. 40 also gives only these two options. Thm. 6.3 (p. 42) states (6.4) Γ = Σ_R C_RΓ + O(λ^a L^K)×(leading). The reference's own Ex. D.48 (pp. 158–160) uses the chain **R2 < R1 < RH** ("RH：全硬") and the remainder r = (1−T_H)(1−T_1)(1−T_2)Γ = ΔH₀ΔK₂ΔK₁, with C_HΓ = ΔH₀ΔK₂K₁(k₁,p̂) giving "两圈硬系数".

**Check.** With only R1 and R2, the definitions C₂Γ = T₂Γ and C₁Γ = T₁(Γ−C₂Γ) = ΔH₀K₂(k₂,π⁺k₁)PK₁ give

Γ − C₂Γ − C₁Γ = ΔH₀ΔK₂K₁ = C_HΓ + r.

C_HΓ is not power suppressed: it is the O(α_s²) two-loop hard coefficient (unsuppressed in U_{R_H}), so (6.4) fails without R_H. No other region exists in the unphysical region. Thm. 3.12(a) leaves only "target jet + hard", and for the planar ladder the J–H separations are: below rung 1 (R_H), between the rungs (R1), and above rung 2 (R2). Any other separation cuts more than two lines or disconnects J from the target.

**Verdict: confirmed.** "R_0" in the claim is the reference's own R_H.

## 6. R-M12: "combinatorics complete" is overclaimed

**Reference.**
* p. 39 (§6 intro): "本节对 DIS 完整执行第 1.3 小节中的五个步骤 … 区域分析、Ward 恒等式与减除法的组合部分是完整的". It lists as conditions only Ass. D.7, D.14 (+ D.27, D.41, D.43).
* The regrouping Σ_{Γ,R}C_RΓ → Σ_i T̂_i ⊗ f_i is the first step of the proof of Thm. 6.6 (pp. 43–44). It takes three sentences ("按 J_R 中的图重新组合：对固定的'硬部分'…对固定的 J…于是 …").
* App. D shows the regrouping is conditional:
  * For DIS it is Prop. D.42, (D.23) Σ_graphs C_RΓ = Ĥ_R ⊗ J^bare_R, proven "设 (Com)(Abs) 成立".
  * (Com) holds exactly only for graphs with an adapted momentum routing; otherwise only up to loop-momentum shifts (p. 137, Note D.24). (Abs) holds exactly for DIS (p. 141).
  * For the other processes it is Ass. D.37 (W1)(W2), p. 149: "(W2) 在一般阶的证明…我们没有写出".
  * Thm. D.46 (p. 154) assumes "对 DIS 设命题 D.42 所用的 (Com)(Abs) 成立，对其余过程设假设 D.37 成立". Thm. 6.6 mentions (Com)(Abs) only inside the parenthesis about UV subdivergences.
* p. 7 (Def. 1.1) attributes the phrase to the CSS standard ("被视为完整的") and then qualifies it at once ("附录 D 表明，即使组合部分也需要精确化 … 假设 D.27、D.37与D.43").

**Verdict: confirmed.** Precise statement: the regrouping of the subtracted region terms into hard coefficient ⊗ PDF is an input, not a completed combinatorial proof. For DIS it rests on the commutativity/absorption properties (Com)(Abs) of the approximators (reference Prop. D.42 / Thm. D.46). For the other processes it rests on the product structure of the Ward identities on approximated integrands (Ass. D.37 (W1)(W2)). The overclaim proper is on p. 39; p. 7 is self-qualified.

## 7. R-M13: DR cut sum = 12π Im Π is not shown

**Reference.**
* p. 29, proof of Thm. 4.1(ii): Euclidean point → no pinches (Cor. 3.4) → IR finite; RG makes D polynomial in L; continue −Q² → s + i0. This concerns the uncut Π only.
* The coefficients (4.4) are "由显式计算得到 [25–27]", pointing to the cut graphs of Fig. 18.
* p. 31: "按 Cutkosky 规则，2 Im Π = Σ_C Π_C" is asserted without discussing ghosts, D-dimensional cutting rules or counterterm cuts. The proof of Prop. 4.2 is self-declared "概要性的".
* The identification of the DR sum over partonic cuts with 12π Im Π, and the interchange of ε→0 with the continuation for cut graphs, are therefore not shown.

**Our replacement.** For thm:ee-R-finite:
* Each Laurent coefficient in ε of the renormalised single-scale Π is a polynomial in L, because each term has the form (Q²/μ²)^{−jε} × (Laurent series).
* Euclidean IR finiteness (Poggio–Quinn: "all Green's functions for nonexceptional Euclidean momenta … are infrared finite") makes the pole coefficients vanish for all real L. Hence they vanish identically.
* So the continuation L → ln(s/μ²) − iπ commutes with ε → 0, and R is finite at every order.

The step is correct as mathematics. Poggio–Quinn already state the corollary "any physical discontinuity of Green's functions is also infrared finite", so the route is not new (consistent with N24, "novelty not claimed"). The identification with DR partonic cut sums is [A], since no source gives the massless DR cutting rules with ghosts in full rigour. That is an appropriate grade.

**Verdict: confirmed.**

## 8. R-M14: the one-loop PDF check of Prop. 7.1 is incomplete

**Reference (pp. 46–47).** Real graphs (7.2) are computed. Then: "虚修正给出 δ(1−ξ) 项，由夸克数守恒 ∫f = 1 确定", and in the proof "图 (e)…与外线自能 (f) 一起…它们的作用是把 1/(1−ξ) 变为加号分布并添加 (3/2)δ(1−ξ)：这由矢量流守恒…唯一确定".
* The virtual Wilson-line graph and the self-energy are never computed.
* Ex. 10.1 (p. 63) describes the real–virtual ξ→1 cancellation in words only.

**Independent computation (`rm14_oneloop_pdf.py`, all PASS).** Feynman gauge, massless on-shell quark target, gluon mass m, DR for the UV.
* Traces with explicit 4×4 γ matrices, D = 4 part (three random kinematic points):
  * ladder: ½Tr = 4p⁺l_T²(1−ξ)²/(l_T²+ξm²)²; in D dimensions the γ^νγ_ν contraction gives the factor (1−ε);
  * Wilson-line interference, both orderings: 8ξp⁺/(l_T²+ξm²);
  * k² = −(l_T²+ξm²)/(1−ξ).
* Normalisation g²/(2π)^{3−2ε}·π^{1−ε} = α_s/2π in MS-bar. Master integrals were checked symbolically and numerically.
* Real part: f_R = A_ε[(1−ε)²(1−ξ)ξ^{−ε} + 2ξ^{1−ε}/(1−ξ)], with A_ε = (α_sC_F/2π)e^{εγ_E}Γ(ε)(μ²/m²)^ε.
* Virtual Wilson-line graph:
  * The l⁻ integral was checked numerically against residues at finite iδ. Its δ→0 limit is iπ θ(0<l⁺<p⁺)/(p⁺(l_T²+xm²)).
  * Hence V₁+V₁† = −A_ε∫dx 2x^{1−ε}/(1−x) δ(1−ξ). This is exactly minus the Wilson-line real integrand.
  * The endpoint ξ→1 is regulated neither by DR nor by m. It cancels only in A_ε[2ξ^{1−ε}/(1−ξ)]_+.
* Self-energy: Σ_V(0) = −A_ε(1−ε)/(2−ε), so the two LSZ legs give (R−1)δ = −A_ε(1−ε)/(2−ε)δ.
* Graph-by-graph UV poles, in units (α_s/2π)C_F/ε: ladder (1−ξ); Wilson real+virtual [2ξ/(1−ξ)]_+; self-energy −½δ. The sum is [(1+ξ²)/(1−ξ)]_+ = P_qq/C_F.
* MS-bar finite part (the O(ε) term of A_ε drops out):
  f^(1) = (α_s/2π){P_qq ln(μ²/m²) + C_F[−(1−ξ)(2+ln ξ) − [2ξ ln ξ/(1−ξ)]_+ + ¼δ(1−ξ)]}, with ∫_0^1 f^(1) = 0.
  This was checked on four test functions. It agrees with c_pdf §3.5.
* Project scripts: s2 29/29 PASS; s5b (gauge-parameter independence, N = 2…8) 28/28 PASS.

**Verdict: confirmed.**

## 9. R-M15: step (iv) of the proof of Thm. 10.3 (REFUTED)

**Reference (p. 64, inspected at 200 dpi).** It prints f̃^unsub_A f̃^unsub_B S̃(+∞,−∞)/[S̃(+∞,−∞) S̃(+∞,−∞)] = f̃_A(ζ_A) f̃_B(ζ_B) "(在 y_n 无关的意义下)", and refers to Prop. D.36 / Lemma D.38 for the precise form.
* Lemma D.38 (p. 149) states the exact identity f̃_A f̃_B = f̃^unsub_A(y_B) f̃^unsub_B(y_A)/S̃(y_A,y_B) for any y_n, with f̃_A built from S̃(y_A,y_n)/[S̃(y_A,y_B)S̃(y_n,y_B)].
* Thm. D.46(d) says (10.4) is (D.22) "在 y_A → ∞、y_B → −∞ 的极限". In the reference's convention the "+∞" of (10.4) therefore *is* the regulator y_A of f̃^unsub_B, and "−∞" is y_B.

**Check.** Take ln S̃(y₁,y₂) = κ[Y coth Y − σ], the exact one-loop rapidity dependence (Y = y₁−y₂), and ln f̃^unsub_A = F_A + κ(y_{P_A}−y_B)+… with equal slope ((T2)). Script `rm15_tmd_softfactor.py`, plus the exact algebra with linear ln S̃ = a + κY, gives:
* **Collins product (10.4):** F_A + F_B − a + κ(y_{P_A} − y_{P_B}). This is finite.
* **Printed** S̃(+∞,−∞)/[S̃(+∞,−∞)S̃(+∞,−∞)], with ±∞ as independent cutoffs L_A, L_B: F_A + F_B − a + κ(y_{P_A}−y_{P_B}) + κ[(y_A−y_B) − (L_A−L_B)]. It diverges unless L_A−L_B = y_A−y_B.
* **ERR-M15 "correct"** S̃(y_A,y_B)/[S̃(+∞,y_B)S̃(y_A,−∞)]: *exactly the same expression*. Since S̃(+∞,y_B)S̃(y_A,−∞) = S̃(+∞,−∞)S̃(y_A,y_B) by linearity, the proposed form is ff/S̃(+∞,−∞), i.e. the printed form.
* **f̃^unsub_A f̃^unsub_B S̃(+∞,−∞)/[S̃(+∞,y_B) S̃(y_A,−∞)]**, and equally **f̃^unsub_A f̃^unsub_B/S̃(y_A,y_B)**: these equal the Collins product, finite and independent of the cutoffs.
* Numerically, with independent cutoffs (D = 5, 20): Collins, "corrected" and ff/S̃(y_A,y_B) all give −2.2660. Printed and ERR-M15 both give 1.434 and 12.534 respectively, drifting with D.
* With the cutoffs identified with y_A, y_B (the reference's convention), all five expressions give −2.2660.

**Conclusion.** "With identical arguments the formula is rapidity divergent" is false in the reference's convention: the printed display is then exactly Lemma D.38. In the other convention the printed formula diverges, but so does the proposed replacement, which is algebraically identical to it. The claim therefore cannot be printed. At most the display is notationally degenerate (regulators suppressed).

**What could be printed instead:** f̃_A f̃_B = lim_{y_A→+∞, y_B→−∞} f̃^unsub_A(x_A,b_T;y_{P_A}−y_B) f̃^unsub_B(x_B,b_T;y_A−y_{P_B}) / S̃(b_T;y_A,y_B). This is an exact identity for any y_n (Lemma D.38 / Collins 2011 (13.106)), and the limit exists by (T2). Equivalently, with independent ±∞: ff·S̃(+∞,−∞)/[S̃(+∞,y_B)S̃(y_A,−∞)].

## 10. R-M16: "W+Y uniformly O((Λ/Q)^a)" needs modified cutoffs

**Reference.** The box of Thm. 10.3 (p. 64) says "加上 Y 项后，误差对 q_T 一致地为 O((Λ_QCD/Q)^a)", without qualification. Its own conditional statement (same page) excludes "Y 项与 q_T ∼ Q 的区域".

**Literature.** INSPIRE confirms J. Collins, L. Gamberg, A. Prokudin, T.C. Rogers, N. Sato, B. Wang, "Relating Transverse Momentum Dependent and Collinear Factorization Theorems in a Generalized Formalism", PRD 94 (2016) 034014, arXiv:1605.00671 (132 citations). From the source:
* The original CSS W+Y "was designed with the aim to have a formalism that is valid to leading power in m/Q uniformly in q_T".
* The error estimates of the standard construction hold only for m ≲ q_T ≲ Q: "they must not be applied when q_T ≫ Q or q_T ≪ m".
* For q_T ≲ m they insert X(q_T/λ) into Y, "analogous to the introduction of a Q_T^min in [CSS 1985, eq. (2.8)]".
* For q_T ≳ Q, "not guaranteed to be well-described … We will correct this … with a modified W-term", namely b_c(b_T) = √(b_T² + b_0²/(C₅Q)²).
* Summary: "for the q_T ≳ Q and q_T ≲ m regions, the CSS W+Y formalism as it stands does not robustly revert to the FO or W terms alone".

**Verdict: confirmed.** Bib entry: Collins:2016hqq. Optionally mention the CSS 1985 Q_T^min precursor.

## 11. R-M17: the transverse-photon failure mechanism

**Reference (p. 71).** "对横向光子，领头扭度的硬核为零，下一阶出现 ∫dz φ(z)/z² 型的发散积分". In context φ is the meson (twist-2) DA, which for γ*_L enters as ∫φ/z.

**Literature.**
* **Mankiewicz–Piller (source read).** The WW relations are g^v(τ) = ½[∫_0^τ φ_∥/ū + ∫_τ^1 φ_∥/u] and g^a(τ) = 2[τ̄∫_0^τφ_∥/ū + τ∫_τ^1φ_∥/u]. Hence g^v(0) = ½σ_φ, with σ_φ = ∫φ_∥/u ≠ 0.
  * The γ*_⊥→ρ_⊥ amplitude contains I_1 = ∫dτ/τ(4g^v − 2Φ_∥/τ + g^a/(2ττ̄)) and I_2 = ∫dτ/τ(2g^v + g^a/(2ττ̄)). "Both … are divergent due to the behavior of the integrands at τ→0"; the singularities are "at least logarithmic".
  * "a modification of the end-point behavior of the twist-2 amplitude φ_∥ cannot cure the infrared divergence … direct consequence of the Ball–Braun relation".
  * The GPD part contains [1/(ξ−u−iε)² + 1/(ξ+u−iε)²]. For the asymptotic singlet quark GPD its real part "is infrared singular".
  * Genuine three-particle twist 3 "will not be considered".
* **Diehl–Gousset–Pire (source read).** The leading-twist contribution to V_T production vanishes "at leading power in 1/Q to all orders", by angular momentum and chirality conservation: the photon would have to transfer two units of J_z. They add: "the above derivation is valid for **any spin state of the incoming virtual photon**".
* **Collins–Diehl.** They close the loophole of Hoodbhoy–Lu (DR breaks chirality: an ε × 1/ε term). The collinear subtractions cancel it, and the coefficient vanishes to all orders.

**Independent numerics (`rm17_rm18_checks.py`; project s8_meson.py agrees).**
* φ_∥ = 6uū gives σ_φ = 3 and g^v(0) = 3/2; τ·integrand → 12 (I_1) and 6 (I_2). M–P print "12/τ and 9/τ"; the 9 looks like a misprint (separate claim E21).
* φ_∥ = 30u²ū² gives g^v(0) = 5/4; the limits are 10 and 5, so the integrals are still log divergent. By contrast ∫30z²(1−z)²/z²dz = 10 converges.

**Verdict: confirmed, with precisions.**
* Write "in the Wandzura–Wilczek approximation".
* The reference's "φ/z²" is imprecise, not of the wrong degree: it is also logarithmic for φ ∼ z, and terms Φ_∥/τ², g^a/τ² of that form do occur in I_1. Its defect is that it suggests endpoint-suppressed DAs would cure the divergence, which they do not.

## 12. R-M18: Collins–Qiu and Rogers–Mulders misreported; Collins 2007 not cited

**Reference.**
* p. 73, Thm. 12.3 "(Collins–Qiu 2007；Rogers–Mulders 2010)": "在一个具体的旁观者模型（带色旁观者的微扰非阿贝尔规范理论）中…".
* p. 74: "Rogers 与 Mulders … 色因子形如 Tr[t^at^b⋯t^at^b⋯]，与 … Tr[t^at^a⋯]Tr[t^bt^b⋯] 型结构不同，差别正比于 [t^a,t^b] ≠ 0；在阿贝尔理论中这个差别为零".
* Bibliography (pp. 231–238, 145 entries): Collins entries are [1]–[5], [36], [38], [42], [45], [52], [58], [63], [86], [108], [130], [135], [138]. None is arXiv:0708.4410.

**Literature.**
* **CQ §II (source):** "The gauge group is abelian." The model has a massive gluon and couplings g₁, g₂; non-factorisation follows from i π(g₁+2g₂). CQ show the failure of standard k_T factorisation.
* **RM (source):**
  * The gauge field is massless SU(N_c). The hard process is "exchange of a hypothetical new massive color-neutral U(1) gauge boson X".
  * The counterexample is "the anomalous two-gluon contribution to a double Sivers effect" (one gluon from each spectator).
  * "all graphs of the type shown in Fig. [violating] include the non-zero color factor Tr_C[t^at^b]Tr_C[t^bt^a] = T_F²(N_c²−1)".
  * The generalized formula with colour-traced Wilson loops gives no such term ("each includes a factor Tr_C[t^a] = 0"; "no corresponding factorization anomaly term").
  * In the abelian case "there is no obvious contradiction".
* **Collins 2007:** the extension to two-gluon exchange; "standard k_T-factorization fails for the unpolarized cross-section".
* **Computation:** Σ_ab Tr[t^at^b]Tr[t^bt^a] = 2.000000 = T_F²(N²−1) for SU(3), and Tr[t^a] = 0.

**Verdict: confirmed.** Locator note: the "non-abelian model" sentence is on p. 73.
