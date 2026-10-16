# Verification batch N01–N06 (stage 1, independent verifier)

Date: 2026-10-10. Default stance: skeptical. All six claims are of kind `new_result`.
For each claim I (i) re-derived or re-computed the statement myself, by a route different from the project scripts where possible, (ii) re-ran the project scripts named in the recipe, and (iii) searched the literature (INSPIRE API, arXiv sources and PDFs read directly) to see whether the result is already known.

## 0. Method and sources

* Project scripts re-run, all reproduced exactly:
  * `refdoc/work_R3/scripts/eikonal_box.py`, `eikonal_box_check.py`, `eikonal_box_closedform.py`. Maximum relative deviation from the closed form: 4.67e−16.
  * `frontier/others/scripts/s1_landau_gordan.py`: 10/10 PASS, 226 type-I and 174 type-II instances, worst margin deficit −1.07e−14.
  * `frontier/lamet/scripts/s1_kernels.py`: 51/51 PASS. `s3_threshold.py`: 9/9 PASS. `s4_tmd_bvz.py`: 20/20 PASS.
* My own scripts are in `verify/claims/batch_N01_s1_scripts/`, with logs. Run them with `python3 -I`.
  * `n01_eikonal.py`: N01 by a different route. Exact k⁻ residues at finite ε, a numerical k⁺ integral, then ε→0. Also the explicit SU(3) colour algebra for 3⊗3, 3⊗3̄, 8⊗3 and 8⊗8.
  * `n02_n03_checks.py`: N02 with Wolfe's minimum-norm-point algorithm (independent of the project's SLSQP), 600 random and degenerate instances. N03: the equivalence of the loop equations with vertex positions on 600 random graphs, plus an eikonal toy model for the orientation question.
  * `n05_diagrams.py`: N05 vertex and sail diagrams from first principles. CONTEXT Feynman rules, Γ = γ⁰, Feynman gauge, k⁰ by residues, k_T numerically, d = 4.
  * `n06_threshold.py`: N06 in two ways. (a) The exact λ→∞ asymptotics of the one-loop coordinate kernel, symbolically. (b) Numerical evaluation for |λ| ≤ 1e5 from special functions and a contour-rotated tail, both signs of λ computed directly.
  * `grep_citers.sh`: downloads arXiv sources and greps them for Gordan, Farkas, Stiemke, Motzkin and "theorem(s) of the alternative".
* Literature read from arXiv sources and PDFs, downloaded fresh into my scratch area and treated as untrusted text.
  * Collins arXiv:2007.04085 (source and PDF, v1, the only version).
  * Collins, *Foundations of perturbative QCD*, ch. 11, pp. 398–425. Cambridge open-access reissue, DOI 10.1017/9781009401845.
  * Meggiolaro hep-th/9602104 (Z. Phys. C 76 (1997) 523), hep-th/9702186, hep-th/9506043, hep-th/9709045.
  * Giordano–Meggiolaro hep-ph/0602143 (PRD 74 (2006) 016003).
  * Korchemsky hep-ph/9311294 (PLB 325 (1994) 459). Korchemskaya–Korchemsky hep-ph/9409446 (NPB 437 (1995) 127).
  * Rothstein–Stewart 1601.04695 (JHEP 08 (2016) 025).
  * IJJSZ 1801.03917 (PRD 98 (2018) 056004). Stewart–Zhao 1709.04933. Ji–Liu–Su 2305.04416 (JHEP 08 (2023) 037). Ji–Liu–Liu 1911.03840.
  * Braun–Manashov–Moch–Strohmaier 1901.06172 (JHEP 02 (2019) 191) and 1810.04993 (PLB 793 (2019) 78).
  * All 39 INSPIRE citers of Collins 2007.04085, plus 2512.12763, 2407.13738, 2204.02988, 0812.3686, 1203.0291, 1211.0509, 1912.09291, 2212.06661, 2009.07854 and 1010.2350, for the Gordan question.
* Bibliographic data checked on INSPIRE and Crossref:
  * Gordan, Math. Ann. 6 (1873) 23–28, DOI 10.1007/BF01442864.
  * Henneaux PLB 313 (1993) 35, Erratum PLB 316 (1993) 633.
  * Joglekar–Lee, Ann. Phys. 97 (1976) 160.
  * Meggiolaro 1997, DOI 10.1007/s002880050575.
  * Giordano–Meggiolaro 2006, DOI 10.1103/PhysRevD.74.016003.

## 1. Summary

| id | verdict | is it new? | what must change before printing |
|---|---|---|---|
| N01 | **confirmed (computation)**; **novelty refuted** | **No.** Meggiolaro, Z. Phys. C 76 (1997) 523, §3, eqs. (3.23)–(3.26) and (3.28)–(3.36) (arXiv numbering). Each graph separately: Giordano–Meggiolaro, PRD 74 (2006) 016003, eq. (4.24) (arXiv numbering). | **Drop the marker 「本书新结果（待文献核查）」.** Cite Meggiolaro 1997 and GM 2006 (4.24). The "other O(g⁴) graphs" are not just argued: Meggiolaro computed them. Do not cite GM (4.15)/(4.20) or M97 (3.35), which carry a sign misprint (§2.6). |
| N02 | **confirmed** | The theorem is Gordan's (1873) and the min-norm proof is textbook. The identification with Collins' Thm 3 was not found in print. | State "exactly one of"; say that an inner product identifies V* with V. Present it as a short remark, not as a significant result. |
| N03 | **confirmed** (inherits the † of Collins Thm 1) | Not new in substance. It is a one-line specialization of Collins' Thm 1, which Collins states covers Wilson lines. The classical-picture step is Coleman–Norton's own. | Fix the orientation convention: denominators must read (n_j·k_j + i0). The trapped side of k ∥ n flips with the sign. Say that soft lines get zero displacement and that the corollary does not determine which denominators trap. |
| N04 | **confirmed** as a conditional [A] argument, with caveats | **No.** Braun–Manashov–Moch–Strohmaier, JHEP 02 (2019) 191, eqs. (2.4), (2.6), (3.1)–(3.2), in the more general off-forward form. The idea goes back to the light-ray operator literature (Balitsky–Braun 1989). | (i) "Physical matrix elements" must exclude forward on-shell massless partonic matrix elements in DR, where BRST/EOM operators do not drop out: Hamberg–van Neerven 1992; Collins–Scalise 1994; BMMS PLB 793 (2019) 78. (ii) The Collins passage that uses the classification for renormalization is §11.4, eq. (11.20), pp. 411–412. (iii) The existence of Z_OO as a distribution needs an argument. (iv) The Müntz–Szász uniqueness is up to distributions at z = 0. |
| N05 | **confirmed** | **No.** These are exactly IJJSZ App. B, eqs. (B1)–(B3) at ε = 0. The sums are IJJSZ eq. (quasi-matching) and Stewart–Zhao 2017, h₀(x>1), h₀(x<0). | Call it an independent re-derivation, not a new result. The tadpole is finite only in DR. With a cutoff it is linearly divergent, so "all integrals finite in d = 4" is wrong for the tadpole. |
| N06 | **confirmed** | **No.** Ji–Liu–Su 2023, eqs. (3.9), (3.11), (3.13), (4.1)–(4.11). The text after (4.11) states both the one-loop reproduction and H_thr = H_quasi-TMD. H^(1) is also Ji–Liu–Liu 2020. | Call it a numerical cross-check. State the convention for the phase sign. At one loop the non-cusp terms cancel (γ̃_H = γ̃_J = −α_sC_F/π). |

## 2. N01 — two-gluon exchange between infinite time-like Wilson lines

### 2.1 Claim (as given)
Lines v_A, v_B with rapidity difference Y. Gluons have mass m. a = k_T² + m², b = (K−k)_T² + m². The claim is J_box = (2π/(ab))(π+iY) and J_cross = −2πiY/(ab). With X = T_A·T_B, c_box = X² and c_cross = X² + (C_A/2)X, so that J_box c_box + J_cross c_cross = (2π/(ab))[πX² − iY(C_A/2)X]. It follows that p_opp = −iY/π, Re p_opp = 0, V†V = 1 + O(χ³), and real cuts start at O(g⁶).

### 2.2 Independent analytic derivation (light-cone residues)
Write v_A^± = e^{±Y/2}/√2 and v_B^± = e^{∓Y/2}/√2, so v_A·v_B = cosh Y. The infinite lines produce δ(v_A·K)δ(v_B·K), hence K^± = 0. The project normalization (eikonal_box.py) is
J = ∫dx_A dx_B [i/(x_A+i0)][i/(σx_B+i0)] g, with x_A = v_A·k, x_B = v_B·k, σ = −1 for the box and +1 for the crossed graph. The measure is dx_A dx_B = sinh Y dk⁺dk⁻ and g = [(2k⁺k⁻−a+i0)(2k⁺k⁻−b+i0)]⁻¹.

* **Box.** At fixed k⁺ ≠ 0 the k⁻ poles are as follows.
  * Line A: k⁻ = −e^{−Y}k⁺ − i0, in the lower half plane.
  * Line B: k⁻ = −e^{Y}k⁺ + i0, in the upper half plane.
  * The two gluon poles, k⁻ = (a−i0)/(2k⁺), lie in the upper half plane only for k⁺ < 0.

  Close the contour upward for k⁺ > 0, picking up only B, and downward for k⁺ < 0, picking up only A. Keeping ε finite, both cases give
  ∫dk⁻(…) = (2πi/sinh Y) ĝ(k⁺)/(k⁺ − i0′).
  Here ĝ = G₊(k⁺) for k⁺ > 0 and G₋(|k⁺|) for k⁺ < 0, with G_±(κ) = [(2e^{±Y}κ²+a)(2e^{±Y}κ²+b)]⁻¹. Both branches tend to 1/(ab) as k⁺ → 0. The −i0′ comes from D_A evaluated at the B pole, −√2e^{Y/2}sinh Y k⁺ + iε(1+e^Y). It is the trace of the 2D pinch of the two eikonal poles at k⁺ = k⁻ = 0.

  Frullani's integral gives PV∫ĝ/k = ∫₀^∞(G₊−G₋)dκ/κ = (1/(2ab))ln(e^{−Y}/e^{Y}) = −Y/(ab). Hence ∫∫(…) = (2πi/sinh Y)(iπ − Y)/(ab). Multiplying by the factor i·i·sinh Y = −sinh Y gives **J_box = (2π/(ab))(π + iY)**.
* **Crossed graph.** Both eikonal poles now lie in the lower half plane, so there is no pinch and no δ(k⁺) term. For k⁺ > 0 every pole is in the lower half plane and the integral vanishes. For k⁺ < 0 the two eikonal residues give, after k⁺ → −κ, (2πi/sinh Y)∫₀^∞(G₋−G₊)dκ/κ = 2πiY/(ab sinh Y). Hence **J_cross = −2πiY/(ab)**, and Re J_cross = 0 exactly.
* **Abelian check.** J_box + J_cross = 2π²/(ab). This equals (−2πiδ)(−iπδ) from the eikonal identity, as it must.

### 2.3 Independent numerics, a different route (`n01_eikonal.py`)
Exact k⁻ residues at finite ε, then a numerical k⁺ integral, for ε = 1e−3 … 1e−6. The deviation is linear in ε. Examples:
* Re J_cross = 8.06e−3, 8.06e−4, 8.06e−5, 8.06e−6 → 0.
* Re J_box → 2π²/(ab).
* Relative deviation at ε = 1e−6: 3.3e−6, 6.9e−6 and 2.1e−5 for (a,b,Y) = (1,2.5,1), (0.7,0.3,3), (2,0.1,0.4).

This confirms the closed forms independently of the project's PV-plus-δ decomposition.

### 2.4 Colour, normalization, unitarity
* **Colour.** Path ordering puts the later attachment on the left. With the same ordering on both lines, c_box = T_A^bT_A^a T_B^bT_B^a = X². With opposite orderings, c_cross = X² + (C_A/2)X. Checked with explicit SU(3) matrices for 3⊗3, 3⊗3̄, 8⊗3 and 8⊗8. All deviations are below 5e−16.
* **Normalization.** With all factors restored ((ig)⁴, (v_A·v_B)², −i per propagator, and V(b) = 1 + (1/sinh Y)∫d²K/(2π)² e^{iK·b}M(K)):
  V(b) = 1 + iχX − ½χ²X² + i(C_A Y/(4π))χ²X + …, with χ = −g² coth Y K₀(mb)/(2π).
  Then V†V = 1 + O(χ³) ✓. For straight infinite time-like lines the one-gluon real emission is ∝ δ(v·k) = 0 on shell, so inelastic channels enter at |O(g³)|² = O(g⁶) ✓.
* **Physical sign.** In momentum space the C_A term equals M_tree·ωY with ω = −g²C_A(K²+m²)/(16π³)∫d²k/(ab) < 0 as Y → ∞. This is the standard negative one-loop gluon trajectory, so the sign is physical.
* **The parameter p_opp.** The reference document's (E.36) reads M^(2) = ½(−iχ)²[X² + p_opp(C_A/2)X], with residual −½C_Aχ²(Re p_opp)X. Hence p_opp = J_cross/(J_box+J_cross) = −iY/π and Re p_opp = 0 ✓. Read in `refdoc/refdoc.txt`, lines 12160–12200.

### 2.5 Literature check — **the result is known**
* **Meggiolaro, Z. Phys. C 76 (1997) 523 [hep-th/9602104], §3 "The case of QCD at order O(g_R⁴)".**
  * Setting: two infinite time-like Wilson lines at hyperbolic angle χ, with W = P exp[−ig∫₋∞^∞ A·(p/m)dτ]. Fixed transverse momentum transfer through ∫d²z e^{iq·z}. Gluon mass λ as IR regulator. Feynman gauge.
  * He computes the ladder (Fig. 2(b)) and cross (Fig. 2(c)) graphs, eq. (3.23), with colour factors G₂ = (T^aT^b)⊗(T^aT^b) = X² and (T^aT^b)⊗(T^bT^a) = G₂ + (N_c/2)G₁, eq. (3.25).
  * Eq. (3.26): **M^(G₁) = i(N_c g⁴/4π) I(t) χ coth²χ** and **M^(G₂) = −½ g⁴ I(t) coth²χ**, with I(t) = ∫d²k/(2π)² [(k²+λ²)((q−k)²+λ²)]⁻¹. He states these hold "for every real value of χ".
  * The remaining O(g⁴) graphs are computed too. The three-gluon graphs vanish, M_(2,1) = M_(1,2) = 0 (eq. (3.32)). The (3,1)+(1,3) graphs and the gluon self-energy give a real constant times the tree, (2N_cB − F^(2)(t)) (eqs. (3.28)–(3.34)).
  * His Regge limit, eq. (3.36), is (2s/t)[1 − ᾱ ln s] with ᾱ = (N_cg²/4π)q²I > 0.
* **Giordano–Meggiolaro, PRD 74 (2006) 016003 [hep-ph/0602143], eq. (4.24).** They restate Meggiolaro's result graph by graph: **M^(b) = i(g⁴/2π)I(t)(iπ−|χ|)coth²χ** and **M^(c) = i(g⁴/2π)I(t)|χ|coth²χ**, so that M^(b)+M^(c) = −½g⁴I coth²χ.
* **Comparison.** Restore N01's omitted factors: cosh²Y/sinh Y from (v_A·v_B)² and the measure, 1/sinh Y in V(b), (−i)² for the propagators, and ∫d²k/(2π)⁴. N01's J_box and J_cross then become −(g⁴/2π)I coth²Y(π+iY) and +i(g⁴/2π)I Y coth²Y. These are **identical, sign and normalization included, to M^(b) and M^(c)** with χ = Y. In particular p_opp = M^(c)/(M^(b)+M^(c)) = −iχ/π.
* Related earlier work, in renormalization-group language:
  * Korchemsky PLB 325 (1994) 459 and Korchemskaya–Korchemsky NPB 437 (1995) 127 contain the same (iπ−γ)coth γ versus γ coth γ structure: KK95 eqs. (F1)–(F2) with F₂(γ) = −F₁(iπ−γ), and the one-loop cross anomalous-dimension matrix with entries −(iπ/N)coth γ and N(γ coth γ − 1).
  * The Y → ∞ limit is classical high-energy perturbation theory (Cheng–Wu; Lipatov), which Meggiolaro cites.
* **The Rothstein–Stewart attribution in rem:dy-common-ordering is correct.** RS 2016 §9, text before eq. (9.1) and referring to §5.2.1: "all diagrams with crossed Glauber rungs vanish with our rapidity regulator". Eq. (9.1) defines the Hermitian colour phase φ(b⊥), and eqs. (9.18)–(9.19) give the exponentiation G̃ = e^{iφ}.

### 2.6 Side observation: a sign misprint in the sources (relevant to citation)
* M97 eq. (3.35) and GM06 eqs. (4.15)/(4.20) (also (4.16), (4.21), (4.27)) print the G₁ bracket as [1 − g²(F^(2) + 2N_cB/(4π)² + (N_c/4π)tIχ coth χ)]. This is inconsistent with their own eqs. (3.26)/(3.34)/(4.24) and with (3.36).
* The bracket follows from (3.34) on removing 2Z_W^(2). It must read [1 + g²(−F^(2) + 2N_cB/(4π)² + (N_c/4π)tIχ coth χ)].
* Taken literally, the printed form would give (2s/t)[1 + ᾱ ln s], that is, the wrong sign of the trajectory.
* GM06's crossing and analytic-continuation conclusions are insensitive to this sign. **Cite (3.26), (3.34), (3.36) and GM06 (4.24), not (3.35)/(4.15)/(4.20).**

### 2.7 Verdict N01
* The computation and the conclusions (a)–(c) are **correct**, re-derived analytically and numerically by an independent route.
* It is **not a new result**: Meggiolaro 1997 §3 and GM 2006 eq. (4.24). The marker 「本书新结果（待文献核查）」 must not be printed.
* What remains our own is only the remark that the reference document's strict-window residual is a truncation artefact. The reference document is uncitable (S62), so it cannot be printed as a priority claim anyway.
* The "not shown: other O(g⁴) graphs" can be upgraded by citing M97 eqs. (3.28)–(3.34). The extra graphs give a real multiple of the tree, so V†V = 1 + O(g⁶) for the complete eikonal amplitude at O(g⁴). This needs F^(2)(t) real for t < 0, which holds.

## 3. N02 — Collins' Thm 3 = Gordan's alternative

* **Collins' text, arXiv:2007.04085 v1.**
  * Thm 3 (`thm:main.geom`, p. 9): "Let V be a real vector space, and let (D₁,…,D_N) be dual vectors on V. Then, there is a direction v for which D_j(v) > 0 for all j, if and only if there is no Landau point for the D_j."
  * The Landau point is Def. 6: λ_j ≥ 0, at least one positive, Σλ_jD_j = 0.
  * The geometric proof is Secs. V–VII, pp. 13–24 of 39, so "about 12 pp." is correct.
  * Footnote 6, p. 2: "Undoubtedly the second part of the proof is closely related to the mathematical subjects of which an account is given in books by Gallier … But I have not yet found the result that is needed …" ✓
* **Gordan 1873** (Crossref verified): for real A, exactly one of (i) ∃x: Ax > 0, (ii) ∃y ≥ 0, y ≠ 0: Aᵀy = 0. With rows D_j, Collins' Thm 3 is this statement verbatim ✓.
* **Min-norm proof.** Fix an inner product, and let w be the unique minimum-norm point of K = conv{D_j}, which is compact and convex. For u ∈ K and t ∈ (0,1], |w+t(u−w)|² ≥ |w|². Dividing by t and letting t → 0⁺ gives ⟨w,u−w⟩ ≥ 0, so D_j(w♯) ≥ |w|². If w = 0, the convex weights give a Landau point. Exclusivity is immediate. The proof is correct and standard (projection onto a convex set).
* **Numerics.**
  * Project script reproduced: 226/174, worst deficit −1.1e−14.
  * Own check with Wolfe's exact minimum-norm-point algorithm and an LP: 600 instances including zero vectors, duplicates and N > d. Result: 238 type I, 362 type II, 0 inconsistencies, worst relative margin −2.4e−12.
* **Literature.** No explicit identification of Collins' Thm 3 with Gordan's theorem was found.
  * Full-source grep of all 39 INSPIRE citers of 2007.04085 and 10 further Landau/contour-deformation papers (§0) for Gordan, Farkas, Stiemke, Motzkin and "theorem(s) of the alternative". The only hits are unrelated: a Farkas variant for acyclic vector configurations in Klausen's thesis 2302.13184, and "Clebsch–Gordan" in 2112.07099.
  * INSPIRE fulltext queries ("Gordan theorem" & Landau; "theorem of the alternative" & Landau; Farkas & pinch) returned no relevant paper. One near miss: 2609.18668 uses Farkas' lemma for graph orientations, not for Collins' theorem.
* **Verdict: confirmed.** Mathematically correct. The theorem and proof are classical. The identification appears unpublished but is elementary.

## 4. N03 — momentum-space Coleman–Norton picture including massless and eikonal lines

* **Derivation.** Collins Thm 1 states: trapped at w_S ⇔ there is a Landau point for {∂A_j(w_S)}, over the denominators vanishing at w_S. Its hypotheses are (a) denominators at most quadratic and (b) the same-sign condition, which is eq. (8.15) on p. 27 of the PDF. Thm 1 is on p. 9.
  * For a propagator, ∂(k_j²−m_j²)/∂ℓ_L^μ = 2η_{jL}k_{jμ}. For an eikonal denominator, ∂(n_j·k_j)/∂ℓ_L^μ = η_{jL}n_{jμ}.
  * Hence Σλ_jD_j = 0 is exactly Σ_jη_{jL}λ_jΔ_j = 0 for every L, with the factor 2 absorbed into λ ✓.
  * Collins himself states in Thm 1 that (8.15) "is obeyed for the denominators encountered in Feynman graphs, including cases with Wilson lines" and verifies it in Sec. VIII B.
  * Relevant on-shell lines: massive lines have v̂² ≤ 0, and massless lines with k ≠ 0 have v̂ spacelike or null. Lines with k = 0 are not "relevant". Eikonal lines have E = 0.
* **Coleman–Norton equivalence.** The loop equations hold if and only if there are vertex positions x_v with x_head − x_tail = λ_jΔ_j. This is the orthogonality of the cycle and cut spaces. Checked on 600 random graph instances.
* **Caveats to print.**
  1. Orientation. The statement holds only if every eikonal denominator is written as (n_j·k_j + i0). For 1/(n·k − i0) one has Δ_j = −n_j. Toy model (gluon k, Wilson line n·k+i0 with n light-like, massless quark p−k): k = αn is trapped for α < 0 and not trapped for α > 0 (`n02_n03_checks.py`).
  2. A zero-momentum massless line has D_j = 0. It is therefore always "trapped" and gets zero displacement λ_j·0. The corollary gives only the *existence* of a classical picture for some Landau point. It does not say which denominators trap. That is Collins' open item 2 and the issue raised by Ma, which Collins' conclusion item 3 lists as missing for QCD. OTHERS §1.5 already says this.
* **Literature.** The momentum-space Landau equations with Wilson lines and the classical interpretation are standard (Landau 1959; Coleman–Norton 1965; Collins 2011). Collins 2020 explicitly includes Wilson lines in Thm 1. The corollary is a direct specialization with no new mathematics.
* **Verdict: confirmed**, at [R]† inherited from Collins Thm 1, with the orientation convention made explicit. Not new in substance.

## 5. N04 — moment reduction of the BRST classification for the bilocal PDF operator

* **Collins' text** (OA reissue, ch. 11).
  * The gap is stated on p. 410 in §11.3.2 for "the non-local operators we use in factorization". Verbatim quote verified.
  * The renormalization use is in §11.4, pp. 411–412: "For the same reasons as with the local operators … the renormalization matrix has a triangular form (11.20) … In physical matrix elements, only the operators O are non-zero … we can therefore replace (11.20) by O = Z_OO O_(0)."
  * Prop 8.1 therefore addresses the **§11.4 (11.20)** use of the classification, not the factorization-step gap of §11.3.2. The claim should cite §11.4 (pp. 411–412).
* **Logic** (checked step by step).
  * (H3): the moments of the bare bilocal matrix element are the bare local twist-2 matrix elements.
  * (H1): ⟨O_N^R⟩ = Z_N⟨O_N⟩ + (class A, B, and total derivatives), and these drop out in physical forward matrix elements.
  * Define Z_OO by its moments. Then Z_OO ⊗ f^bare has finite moments for all N.
  * (H2): at each order, the coefficient of each 1/ε^k is a compactly supported distribution with vanishing moments, hence zero.
  * The argument is valid given its premises.
* **Caveats.**
  1. **Physical matrix elements.** For forward (zero-momentum-insertion) on-shell massless partonic matrix elements in DR, BRST/EOM ("alien") operators do *not* drop out (Hamberg–van Neerven 1992; Collins–Scalise 1994). BMMS PLB 793 (2019) 78 (arXiv:1810.04993), text after their eqs. (12)–(13): "theorems on the renormalization of gauge invariant operators directly apply to matrix elements with the operators inserted at nonzero momentum … [with] operators inserted at zero momentum … physical matrix elements of gauge variant operators do not vanish". So H2/H3 "at each order in physical states" must mean genuinely physical states, or IR-safe and nonzero-momentum kinematics.
  2. **Existence** of Z_OO as a distribution with moments Z^(N) is not implied by H1–H3. It follows from the perturbative structure, since the inverse Mellin transforms of the anomalous dimensions are the splitting kernels, or from applying H2 to the renormalized operator. It should be stated.
  3. **Uniqueness.** On [−1,1] all integer moments are available, so compact support (Paley–Wiener, Weierstrass) suffices. For parity-split kernels on [0,1], Müntz–Szász (Σ1/λ = ∞ for odd or for even exponents) gives uniqueness only up to distributions supported at z = 0. For example, δ(z) is invisible to the odd exponents 1, 3, 5, …. Such terms are irrelevant for convolutions at x > 0, but the statement should say so.
* **Literature: not new.**
  * Braun–Manashov–Moch–Strohmaier, JHEP 02 (2019) 191, eq. (2.4): light-ray operators as generating functions of local operators, which is (H3).
  * Same paper, eq. (2.6): "Renormalized LROs are defined by the same expression with bare local operators replaced by the renormalized ones."
  * Same paper, eqs. (3.1)–(3.2): the Joglekar–Lee decomposition of each renormalized local operator into gauge-invariant, BRST and EOM parts, and the gauge-invariant renormalized light-ray operator as the generating function of the gauge-invariant parts.
  * This is the moment reduction, in the off-forward setting. The generating-function view of light-ray operators is classical (Balitsky–Braun 1989; Müller et al. 1994).
* **Verdict: confirmed** as an [A]-grade conditional statement with the caveats above. It cannot be labelled "this work".

## 6. N05 — one-loop quasi-PDF in the unphysical regions

* **Sums.** With L = ln(ξ/(ξ−1)), for ξ > 1 the sum is a[1 − (ξ−1)L + (2ξL−1)/(1−ξ) + 1/(1−ξ)] = a[((1+ξ²)/(1−ξ))L + 1]. For ξ < 0 it is a[−((1+ξ²)/(1−ξ))ln(−ξ/(1−ξ)) − 1]. Both ✓, by hand and with sympy; `s1` gives 51/51.
* **First-principles diagrams** (`n05_diagrams.py`, CONTEXT conventions: vertex +igγ^μ, W = P exp(ig∫dz·A), Γ = γ⁰, Feynman gauge).
  * Vertex numerator: N_v = −8(p·k)k⁰ + 4p⁰k².
  * Sail numerator, both sails equal: N_s = ½Tr[p̸γ⁰k̸(ẑ·γ)] = −2(p⁰k^z + p^zk⁰). The link factor is g ẑ^μ(e^{−ik^z z} − e^{−ip^z z})/(p^z−k^z).
  * k⁰ is done by exact residues and k_T numerically. At 7 points ξ ∈ {1.5, 2, 3.7, 8, −0.4, −1, −3.3}, the vertex equals a∫₀¹(1−y)/|ξ−y| and the sail equals (a/(1−ξ))∫₀¹(ξ+y)/|ξ−y|. Maximum relative deviation 2.4e−16, independent of p^z.
  * A first attempt got the sail sign wrong through a trace slip: γ³ = e̸ with e_μ = δ_μ³, so e^μ = −δ^{μ3}. After checking the trace with explicit Dirac matrices the sign agrees.
  * Tadpole, in DR: at ξ ≠ 1 one gets i g²C_F p^z/(p_z²(1−ξ)²)·(2π)⁻⁴∫dl⁰d^{d−2}l_⊥(l²+i0)⁻¹|_{l^z=(1−ξ)p^z}. The integral equals 2iπ²|1−ξ|p^z at d → 4, which gives −a/|1−ξ| ✓.
  * With a transverse cutoff the same integral is linearly divergent. So the tadpole is finite only in DR, and LAMET.md's phrase "all integrals finite in d = 4" is inaccurate for the tadpole.
* **IJJSZ App. B (read).**
  * Vertex + w.fn., eq. (B1): (1−ε)∫₀¹dy(1−y)|x−y|^{−1−2ε}Γ(ε+½)/√π + δ-terms.
  * Sail, eq. (B2): ∫₀¹dy (x+y)/(1−x) |x−y|^{−1−2ε}Γ(ε+½)/√π + δ-terms.
  * Tadpole, eq. (B3): −(1−2ε)⁻¹|1−x|^{−1−2ε}Γ(ε+½)/√π + δ-terms.
  * At ε = 0 and x ∉ [0,1] these are exactly the three claimed expressions ✓.
  * Stewart–Zhao, PRD 97 (2018) 054512, h₀(x): (1+x²)/(1−x) ln(x/(x−1)) + 1 for x > 1 and (1+x²)/(1−x) ln((x−1)/x) − 1 for x < 0 ✓.
* **Verdict: confirmed.** Not new: it is an independent re-derivation of IJJSZ App. B.

## 7. N06 — one-loop threshold factorization; H_thr = H_qTMD

* **Exact asymptotics** (`n06_threshold.py`, sympy). Input is the one-loop γ^t coordinate kernel, checked term by term against IJJSZ eq. (1loopiofferen): the h(ζ) term is the transform of the plus distribution, the 4iζe^{−iζ}₃F₃ term is the transform of −[4ln(1−α)/(1−α)]₊, and 2(1−iζ−e^{−iζ})/ζ² is the transform of 2(1−α).
  * With Λ = ln|λ| + γ_E, the λ→∞ limit of e^{iλ}G̃(λ) is exactly H^(1) + J̃^(1) + iπ sgn(λ)(L_z−1).
  * Here H^(1) = −2 + π²/12 − L_z²/2 + L_z, J̃^(1) = l_z²/2 + l_z + π²/12 + 2, and l_z = 2Λ − L_z.
  * Real part: (l_z+1)(l_z+L_z) − (l_z+L_z)²/2 + π²/6 = H^(1) + J̃^(1) ✓. Imaginary part: π(2Λ − l_z − 1) = π(L_z − 1) ✓.
* **Numerics.**
  * Ci/Si plus an exponentially convergent contour-rotated tail, at 30 digits.
  * At |λ| = 1e2, 1e3, 1e4, 1e5 and L_z ∈ {0, 1.3, −0.8}, both signs of λ computed directly: residual |d| = 0.31, 0.041, 2.4e−3, 2.7e−4. Im d flips sign with λ.
  * This reproduces s3's numbers to all printed digits. Representations cross-checked against direct quadrature to 1e−29.
* **Phase-sign convention.** The tree is e^{−iλ} with λ = z p^z (z the position of ψ̄), and C(y) = ∫dλ/(2π) e^{−iλ(1−y)}[e^{iλ}G̃]. This is the same Fourier convention as JLS eq. (3.19). The odd term (L_z−1)P(1/(1−y)) must then appear in momentum space, and it does: the IJJSZ kernel gives 2(L_z−1)/(1−ξ) for ξ → 1⁻ and 0 for ξ → 1⁺. So the sign is fixed physically.
* **Anomalous dimensions, one loop, in units of a = α_sC_F/2π.** d ln H/d ln μ = 2L_z − 2 (Γ_cusp = 2a, γ̃_H = −2a). d ln J̃/d ln μ = 2l_z + 2 (γ̃_J = −2a). The phase gives −2iπ = −iπΓ_cusp. The sum is Γ_cusp[ln(λ²e^{2γ_E}) − iπ sgn λ], μ-independent at fixed λ. The non-cusp terms cancel at one loop. This agrees with the threshold limit of the exact kernel RGE dC/d ln μ² = a[3/2 δ − B].
* **Universality.** JLS eq. (4.11): H = 1 + (α_sC_F/2π)(−2 + π²/12 − L_z²/2 + L_z). Ji–Liu–Liu 2020, ln H^(1) = α_s[c₁ + (C_F/2π)(L_z − L_z²/2)] with c₁ = (C_F/2π)(−2+π²/12) ✓. `s4` gives the same H^(1) from the quasi-TMD ingredients.
* **Literature: not new.** JLS 2023, text after eq. (4.11): "the above hard kernel together with the jet function J_f completely reproduces the one-loop quasi-PDF in MS scheme … at power (1−y)⁻¹ … Moreover, the hard kernel completely agrees with the hard kernel for quasi-TMDPDF/quasi-LFWF factorization". The RGEs are eqs. (3.11), (4.4) and §6.
* **Verdict: confirmed** as a numerical cross-check of JLS 2023.

## 8. Reproduction
`cd verify/claims/batch_N01_s1_scripts && for f in n01_eikonal n02_n03_checks n05_diagrams n06_threshold; do python3 -I $f.py; done`. Logs are in `*.log` in the same folder. Run time is under 2 min in total.
