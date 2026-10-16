# Verification batch N07–N12 (stage 1, independent verifier)

Date: 2026-10-10. Default stance: skeptical. Claims N07–N11 come from `frontier/lamet/LAMET.md` (§4.5, §4.6(d), §5.1–5.3, §7.2–7.3, §14 items 7–11);
N12 comes from `refdoc/REFDOC_ANALYSIS.md` (S30, §3 D24, ERR-m25) and the reference document's Ex. D.47.

## 0. Method and sources

* **Primary literature was re-downloaded independently** (arXiv e-print sources, latest versions, into a scratch folder; read as text only; not the copies in
  `frontier/lamet/papers/`):
  1810.00048 (BVZ), 1603.06664 (Chen–Cohen–Ji–Lin–Zhang), 1801.03917 (IJJSZ), 2008.03886 (Ji et al., hybrid), 2004.03543 (RMP), 2408.03378 (Ji 2024),
  2601.12189 (Ji–Liu–Su 2026), 1706.08962 (JZZ), 1707.07152 (GJS), 1707.03107 (IMQY), 1705.01488 (Radyushkin 2017), 1702.01726 (Radyushkin, TMC),
  1803.04393 (LP3 2018), 1902.00587 (ETMC 2019), 2005.12015 (Fan et al. 2020), 2007.06590 (Gao et al. 2020), 2011.14971 (Lin et al. 2020),
  2408.13486 (Han et al. 2024), 2606.09732 (Braun–Jiang 2026), 2608.29042 (Shi et al. 2026).
* INSPIRE API: bibliographic data of every cited key (all match the claims: NPB 911 (2016) 246; PRD 99 (2019) 014013; PRD 96 (2017) 034025;
  PRD 98 (2018) 056004; NPB 964 (2021) 115311; RMP 93 (2021) 035005; PRD 96 (2017) 094019; PRL 120 (2018) 112001; PRL 121 (2018) 022004;
  NPB 1007 (2024) 116670; PLB 298 (1993) 363), plus title/abstract/full-text searches for prior results (listed per claim).
* My own scripts (run with `python3 -I`), in `verify/claims/batch_N07_s1_scripts/`:
  `n07_tmc.py` (40/40), `n08_fourier_lemma.py` (11/11), `n09_tails.py` (12/12), `n10_fourier.py` (20/20), `n10_landau_widom.py`,
  `n12_triangle.py` (23/23). Logs `*.log` next to them.
* Project scripts named in the recipes, re-run: `frontier/lamet/scripts/s6_tmc.py` 40/40 PASS, `s5_lemmas.py` 12/12, `s1_kernels.py` 51/51,
  `s7_fourier.py` 14/14; `refdoc/work_SYN/triangle_remainder.py` ALL CHECKS PASS (it lacks the site-packages path line; run through a wrapper that adds it);
  `refdoc/work_R6/check_remainder_d4.py` reproduces −0.0173434339581 (log: `batch_N07_s1_scripts/rerun_check_remainder_d4.log`).
  Note: these project checks share code paths with the claims; my verdicts rest on the independent scripts above.

Notation: a = α_s C_F/(2π); c = M²/(4P_z²); z² is the Minkowski 4-vector square (z² = −λ²/P_z² < 0 for z along e_z).

## 1. Summary

| id | verdict | what must change before printing | already in the literature? |
|---|---|---|---|
| N07 | **confirmed** | Replace "TMC commutes with matching" by the precise formula q̃_Γ = C_Γ ⊗ q_M^Γ (same kernel; TMC applied to the PDF first). The reverse order differs at O(α_s c). The x-space identity relates the TMC-transformed (tree-level) distributions. Drop or qualify "new closed form". | **Partly.** K⊥_N is identical to Chen et al. 2016's helicity ratio K̄_n (NPB 911, App. B, eq. (Knbar)); our γ⁰ closed form equals their helicity x-space formula pointwise (Δq → q). The identification for unpolarized γ⁰ is not in the literature I found; O(c) is BVZ (target-perp). |
| N08 | **confirmed** | Attribute the P = 0 normalization terms (−¼ and −5/12, and the 1/(1−x)² enhancement) to BVZ eqs. (65)–(66) [label (bR)]; they are not new. Lemma 5.2 is elementary (used implicitly in BVZ's (t4-Qparallel)). | **Yes** for the normalization part (BVZ 2018). The general Lemma/Corollary phrasing appears new but is elementary. |
| N09 | **refuted** (as stated) | Tails and Prop. 4.4 are right. Prop. 4.5 is wrong for the hybrid kernel and its conclusion on Regge-like sea quarks is wrong. See the corrected statement. | Tails follow directly from IJJSZ's printed kernels. IJJSZ state the MS-bar validity condition f ~ y^{−1+a}, a > 0. |
| N10 | **confirmed** | Label Lemma 7.2 as a Paley–Wiener-type classical fact applied to the quasi-PDF. "Recoverable modes" should read "eigenvalues close to 1 (trace = 2λ_L/π)". | Classical mathematics (Paley–Wiener; Slepian–Landau–Pollak; Landau–Widom). Ji 2024 (NPB 1007, §"PDF and GPD singularities") states the qualitative analyticity. |
| N11 | **confirmed**, with two qualifiers | "Non-perturbative content isolated in (H3)–(H5)" holds for the MS-bar/hybrid formulation. Ratio/RI-MOM momentum-space matching carries its own [C] (node N13). IJJSZ call the OPE "widely assumed", so the printed text should say that N4 = [A] is a judgment. | Organizational. Attributions checked: JZZ, GJS, IMQY, IJJSZ, Radyushkin 1983. No Zimmermann-level OPE proof found. |
| N12 | **confirmed** | None of substance. Optionally print the exact closed form ∫r = [4Li₂(−σ) + σ²(ln²σ + π²/3)]/(Q̃²(1−σ²)), σ = m²/Q̃². | The small-t expansion of Φ⁽¹⁾ is elementary. The statement about this Collins remainder (reference approximators) was not found in the literature. Φ⁽¹⁾: Usyukina–Davydychev PLB 298 (1993) 363 (checked at abstract level; the formula is verified numerically). |

## 2. N07 — exact target-mass correction for Γ = γ⁰

### 2.1 Independent derivation of K⊥_N
* The twist-2 matrix element ⟨P|O^{μ1…μN}|P⟩ = 2a_N(P^{μ1}⋯P^{μN} − traces). Contracting the traceless symmetric tensor T with z^N gives a polynomial f_N(z) that is
  **harmonic** (□_z f_N = N(N−1)·trace = 0). I constructed f_N = Σ_k β_k (P²z²)^k (P·z)^{N−2k}, β_0 = 1, by imposing □_z f_N = 0 (sympy, N ≤ 6).
  This does not use the Chebyshev/Gegenbauer closed form.
* γ^z: K_N = f_N/(P·z)^N at z = z e_z. γ⁰: u_{μ1}z_{μ2}⋯z_{μN}T^{μ1…μN} = (1/N) u·∂_z f_N with u = e_t (u·z = 0). Normalized by P⁰(P·z)^{N−1}, as in h̃ = ⟨O_Γ⟩/(2P^Γ).
  Result (`n07_tmc.py`): K_N = Σ_i C(N−i,i) c^i and **K⊥_N = Σ_i C(N−i,i)(N−2i)/N c^i** for N = 1…6.
  K⊥_1 = K⊥_2 = 1, K⊥_3 = 1 + 2c/3, K⊥_4 = 1 + 3c/2, K⊥_5 = 1 + 12c/5 + 3c²/5, K⊥_6 = 1 + 10c/3 + 2c². By hand: K⊥_3 = 1 + C(2,1)(1/3)c and K⊥_4 = 1 + C(3,1)(2/4)c + C(2,2)·0·c².
* Identity K⊥_N = K_N − (2c/N) dK_N/dc: exact (sympy) for N = 1…30. It follows from Σ_i i C(N−i,i)c^i = c K_N′.
* Physical cross-checks. N = 1: the conserved current ⟨ψ̄γ⁰ψ⟩ = 2P⁰ has no correction. N = 2: the T^{0z} trace term ∝ g^{0z} = 0. γ^z: T^{zz} gives 1 + c.

### 2.2 x-space formula
* The operator A[g](x) = ∫₀¹ (dy/y) g(x/y) = ∫_x^{±∞} (dt/t) g(t) divides the N-th moment by N. Hence the RHS of q̃_{γ0} = q̃_{γz} − 2c A[∂_c q̃_{γz}] has moments K⊥_N a_N.
  Both sides have compact support, so moments determine them.
* Numerical check with a test function that has both quark and antiquark parts (c = 0.15): moments n = 1…5 reproduce K⊥_n to 10 digits.
* **Literature finding (important).** Chen et al. 2016 (arXiv:1603.06664 = NPB 911 (2016) 246), polPDFs.tex eq. (Knbar), give the *helicity* (γ^zγ₅) moment ratio
  K̄_n = Σ_i ((n−i)/n) C(n−i−1, i) c^i. This is identical to K⊥_n: C(n−i,i)(n−2i)/n = C(n−i−1,i)(n−i)/n. The reason is that S·∂_P acting on the traceless tensor gives the same
  K_n − (2c/n)K_n′ as u·∂_z, because S·P = 0 and u·z = 0.
  Their App. B (tmc_appendix.tex) solves it in x-space:
  Δq̃(x) = (1/(1+4c))[(f₊/2)Δq(2x/f₊) + (f₋/2)Δq(−2x/f₋)] − ∫_{±∞}^x (dy/y)(2c/(1+4c)^{3/2})[Δq(2y/f₊) + Δq(−2y/f₋)].
  With Δq → q this equals our γ⁰ formula **pointwise** (7 points, both signs of x, agreement to 1e-10). Its moments also give K⊥_n.
  So the transformation itself is already in print. What is new in our text is (i) that it is the unpolarized **γ⁰** TMC and (ii) the compact representation via ∂_c q̃_{γz}.
* Search for the γ⁰ identification: INSPIRE (title/abstract "target mass", papers citing Chen:2016utp with "mass correction" and "all orders" in the full text, 17 hits examined)
  and the papers listed in §0.
  - Lattice papers using γ^t/γ⁰ cite only Chen et al. for the TMC: LP3 2018 (1803.04393), ETMC 2019 (1902.00587), Lin et al. 2020 (2011.14971).
    Fan et al. 2020 (2005.12015, eq. (targetmass)) explicitly apply the γ^z formula to γ_t data.
  - Gao et al. 2020 (2007.06590, App. "Leading twist target mass correction") use the scalar factor Σ C(n−k,k)c^k for γ_t. Their z² coefficient is −m²⟨x²⟩/8; K⊥_3 implies −m²⟨x²⟩/12.
    (I did not examine their analysis further.)
  - RMP 2021 says "TMC have been computed to all orders … in [Chen:2016utp, Radyushkin:2017ffo]". Those papers treat γ^z, the polarized cases, and a scalar model, not unpolarized γ⁰.
  - BVZ note that the all-order leading-twist projection of the exponential is in Balitsky–Braun 1989. Combined with BVZ's derivative identity, this would yield the γ⁰ result. Not checked (not on arXiv).
  - Braun–Jiang 2026 (2606.09732) and Shi et al. 2026 (2608.29042) work at O(m²) or for γ^z-type structures (quasi-GPDs, baryon quasi-DAs).

### 2.3 O(c) versus BVZ
* BVZ (arXiv:1810.00048 source; by my count of the source these are eqs. (27) and (29)).
  (target-parallel): Q^∥ = q + ¼(m²v²/(pv)²)[xq′ + q].
  (target-perp): Q^⊥ = q + ¼(m²v²/(pv)²)[xq′ + 3q] − ½(m²v²/(pv)²)θ(|x|<1)∫_{|x|}^1 (dy/y) q(x/y).
  With v² = −1 and (pv)² = P_z², ¼m²v²/(pv)² = −c. These are exactly q − c(xq′ + q) and q − c(xq′ + 3q) + 2c∫_{|x|}^1 (dy/y) q(x/y).
* From our formula: A[∂_c q̃_{γz}]|_{c=0} = A[−(xq′ + q)] = q(x) − ∫_x^1 dt q(t)/t (using q(1) = 0). This reproduces the BVZ γ⁰ result (sympy; `n07_tmc.py`).
  Moment check: 1 + c(N−3+2/N) = 1 + c(N−1)(N−2)/N. BVZ's own pseudo-PDF TMC (target-pPDF), built from I^⊥, also gives 1 + c(N−1)(N−2)/N. This is an independent consistency check of K⊥.

### 2.4 "TMC commutes with matching" (Prop. 5.1(d))
* With the OPE (H2), h̃_Γ(λ,z²) = Σ_n C_n(z²μ²)((iλ)^n/n!) K^Γ_{n+1}(c) a_{n+1} with c independent of λ at fixed P^z.
  For γ^z the extra z^α structure multiplies a_{n+2}K_{n+2}, so the same K for the same moment. Hence q̃_Γ = C_Γ ⊗ q_M^Γ by the steps of Thm 4.2. **Correct.**
* Literal commutation is false. For a dilatation D_s q(x) = s q(x/s), substituting y = sy′ gives exactly
  C ⊗_{P^z} D_s q = D_s(C ⊗_{sP^z} q).
  The momentum-space kernels depend on ln(μ²/(4y²P_z²)), and s₊ = f₊/2 = 1 + c + O(c²). So TMC[C ⊗ q] − C ⊗ TMC[q] = 2a c [(1+ξ²)/(1−ξ)]₊ ⊗ q + O(a c², a² c) ≠ 0.
  Print the precise formula, not the slogan.
* The identity q̃_{γ0} = q̃_{γz} − 2c A[∂_c q̃_{γz}] is between the TMC-transformed tree-level distributions (q_M^{γ0} versus q_M^{γz}). It does not relate the full quasi-PDFs: the one-loop kernels differ by 2a(1−ξ).

### 2.5 Verdict N07
Confirmed (all formulas verified independently). The novelty must be qualified (Chen et al. 2016, helicity) and the "commutes" wording fixed.

## 3. N08 — Fourier lemma and endpoint dichotomy

* **Lemma 5.2.** λ²e^{−ixλ} = −∂_x²e^{−ixλ} and z² = −λ²/P_z², so FT[z²Λ²r] = −(Λ²/P_z²)FT[λ²r] = +(Λ²/P_z²)ρ″. Correct as distributions.
  Numerical test with ρ = (1−α²)⁶ (r(λ) in closed form, λ ≤ 200) at x = 0, 0.35, 0.7: FT[λ²r] = −ρ″ to 1e-8 (`n08_fourier_lemma.py`).
  The sign convention agrees with BVZ (t4-qITD) → (t4-Qparallel): BVZ write −κv²Λ²/(pv)² (d/dx)², which equals +κΛ²/P_z² (d/dx)².
  So BVZ use this identity implicitly.
* **Endpoint factors:** ρ ~ x^a gives ρ″/ρ → a(a−1)/x², and ρ ~ (1−x)^b gives b(b−1)/(1−x)². Checked with sympy.
* **Cor. 5.3:** for ρ₄ = q(1−x)^δ with q ~ (1−x)^b, ρ₄″/q → (b+δ)(b+δ−1)(1−x)^{δ−2} (sympy, δ = 0, ½, 1). Correct as an implication.
  *δ = 1 ↔ BVZ:* in BVZ's renormalon model ρ₄(x) = ∫_x^1 (dy/y)(y + ȳ ln ȳ) q(x/y) ~ (1−x)^{b+1}. The numerical local exponent of ρ₄/q at x → 1 is 0.9996.
  This matches BVZ's conclusion O(Λ²/(x²(1−x)P_z²)).
  *δ = 0 ↔ RMP:* RMP eq. (fact_0) states O(Λ²/((1−y)P^z)²), "suppressed by … the spectator momentum (1−y)P^z [Ji:2020brr]". Read in the arXiv source of 2004.03543.
* **P = 0 normalization.** ∫₀¹(α + ᾱ ln ᾱ) = ¼ and ∫₀¹(α + ᾱ ln ᾱ + αᾱ) = 5/12 (sympy). [k]₊ = k − ¼δ(ᾱ) gives the extra term −¼q″, hence ΔR^∥ = −¼ x̄x²q″/q (and −5/12 for ⊥) in BVZ's normalization (cR).
  **This is printed in BVZ**: arXiv:1810.00048 eq. (bR), eqs. (65)–(66) by my count. They give R̄^∥_Q = R^∥_Q − ¼(x̄x²/q)q″ and R̄^⊥_Q = R^⊥_Q − (5/12)(x̄x²/q)q″,
  with the sentence "the additional terms are proportional to the second derivative of the quark PDF and thus enhanced as 1/(1−x)² at x → 1."
  BVZ therefore already exhibit both the 1/(1−x) (unnormalized) and the 1/(1−x)² (P = 0-normalized) behaviours.
  Our dichotomy is a clean reformulation, not a new phenomenon.
* **Verdict N08: confirmed.** Attribute the normalization statement to BVZ. Present Lemma 5.2/Cor. 5.3 as an elementary reformulation that makes BVZ's observation general.
  The endpoint behaviour of ρ₄ itself stays [C], as the source says.

## 4. N09 — moments and convolution domain of the one-loop quasi-PDF

### 4.1 What is right
* The kernels as printed in IJJSZ (arXiv:1801.03917 eqs. (quasi-matching), (quasi-matching-alt); read in the source) agree with LAMET §4.6(c).
* **Tails** (sympy series, `n09_tails.py`), with w = 1/|ξ|:
  C^MS → −3w/2 ∓ 17w²/6 − 43w³/12 at ξ → ±∞;
  C^ratio → ∓4w²/3 − 25w³/12.
  So C^MS → −3a/(2|ξ|) and C^ratio → ∓4a/(3ξ²): **confirmed.**
  An independent coordinate-space route gives the same result. The 1/|ξ| tail comes from (3a/2)ln λ² δ(1−α), whose FT is −1/|ξ−1|. The ratio tail is a∫₀¹αB(α)dα = −4a/3.
* **Prop. 4.4:** q̃^MS(x) → −(3a/(2|x|))∫f at large |x|, so there is no zeroth moment when ∫f ≠ 0. In the ratio scheme ∫q̃ = ∫f.
  With the antiquark part f(y<0) = −q̄(|y|), the tail reads q̃^ratio → −(4a/3) sgn(x)(⟨y⟩_q + ⟨y⟩_q̄)/x². The first moment then diverges logarithmically. **Confirmed.**
* **Prop. 4.5, MS-bar and ratio parts:** near y → 0 the MS-bar integrand is −(3a/(2|x|))f(y)(1 + O(y)). Lebesgue convergence therefore holds iff ∫_{|y|<ε}|f| < ∞ (true).
  For the ratio kernel the integrand is O(|y f(y)|) (true). Numerically, for f = 1/y at x = 0.3: MS-bar partial integrals grow with slope −5.0001 per unit ln(1/ε) (prediction −3/(2x) = −5); ratio converges.
  IJJSZ already state the MS-bar condition: "valid for any PDF that behaves as lim_{y→0} f(y) ~ y^{−1+a} with a > 0".

### 4.2 What is wrong
1. **Hybrid kernel.** In C_hyb = C_ratio + (3a/2)[−1/|1−ξ| + 2Si((1−ξ)λ_S)/(π(1−ξ))], the parameter is λ_S = z_S p^z = z_S|y|P^z (parton momentum).
   Ji et al. 2008.03886 eq. (hybridm2): "λ_S = z_S p^z with p^z = xP^z being the parton momentum", in their swapped notation.
   As y → 0, ξ = x/y → ∞ but (1−ξ)λ_S → −x z_S P^z stays finite. The 1/u² decay of the bracket used in LAMET (§3.7, "decays like −2cos(uλ_S)/(πλ_S u²)") holds only at **fixed** λ_S.
   In the convolution the hybrid term behaves as (3a/(2|x|))[(2/π)Si(|x|z_SP^z) − 1] f(y). Equivalently, in hadron variables it is ∫dy f(y) G(x−y), with G(x−y) → G(x) ≠ 0 as y → 0.
   Numerically, for f = 1/y, x = 0.3, z_SP^z = 3: slope −2.26110 versus predicted −2.26104 (logarithmic divergence).
   **So the hybrid scheme has the same small-y requirement as MS-bar.** The coefficient 1 − (2/π)Si(|x|z_SP^z) is only suppressed (0.40, −0.18, −0.056, 0.0026 at |x|z_SP^z = 1, 3, 10, 30) and vanishes only at isolated points.
2. **"A Regge-like sea ~ y^{−1−δ} makes the MS-bar quasi-PDF ill-defined; only ratio/hybrid are meaningful."** The quark quasi-PDF always contains the antiquark at y < 0, and the leading tail −3a/(2|ξ|) is **even** in ξ.
   The y → 0± contributions therefore combine into −(3a/(2|x|))(q − q̄) + O(y(q+q̄)). This is absolutely integrable whenever the valence q − q̄ and y(q + q̄) are integrable at small y,
   i.e. for Regge-like sea with δ < 1. This is the same condition under which the light-cone ITD itself exists.
   Numerically, for a C-even sea q = q̄ = y^{−1.3}: the MS-bar, hybrid and ratio combined integrals all converge, with differences shrinking exactly as ε^{0.7}.
   The quark-only MS-bar partial integral alone diverges (−2070 at ε = 1e-7).
   The statement about gluons is not supported either: gluon matching uses different kernels (and x g(x)), which were not analyzed.

### 4.3 Verdict N09
**Refuted as stated.** The precise statement that can be printed is given in the structured output and below:
> At O(α_s), C^MS(ξ) → −3a/(2|ξ|) and C^ratio(ξ) → ∓4a/(3ξ²) for ξ → ±∞ (IJJSZ kernels). Hence q̃^MS ~ −(3a/(2|x|))∫f has no zeroth moment when ∫f ≠ 0, and
> ∫q̃^ratio = ∫f with q̃^ratio ~ −(4a/3) sgn(x)⟨y⟩_{q+q̄}/x², so the first moment diverges logarithmically.
> Near y = 0 the integrand of ∫dy/|y| C(x/y) f(y) is −(3a/(2|x|)) f(y)(1+O(y)) for MS-bar, (3a/(2|x|))[(2/π)Si(|x|z_SP^z) − 1] f(y)(1+O(y)) for the hybrid scheme
> (λ_S = z_S|y|P^z), and O(|y f(y)|) for the ratio scheme. So MS-bar and hybrid converge absolutely iff ∫_{|y|<ε}|f| < ∞, while the ratio scheme needs only ∫|y f| < ∞.
> For physical quark distributions (antiquarks at y < 0) the O(1) terms combine into (q − q̄). Hence all three schemes give finite quark quasi-PDFs when q − q̄ and y(q + q̄) are integrable at small y,
> including Regge-like sea with δ < 1.

## 5. N10 — Fourier-step theorems

* **Lemma 7.2.** For x = x_R + i x_I, |e^{−ixλ}| = e^{x_I λ}. The integrand is bounded by A(1+|λ|)^k e^{(|x_I| − m/P^z)|λ|}, uniformly integrable on |x_I| ≤ m/P^z − ε, so the function is holomorphic (Morera/Fubini).
  The width is sharp: the FT of e^{−m|λ|/P} is the Lorentzian (1/π)(m/P)/((m/P)² + x²) with poles at ±im/P (numerical check to 1e-20). **Correct.**
  This is the classical Paley–Wiener-type statement. **Attribution checked:** Ji 2024 (arXiv:2408.03378, NPB 1007 (2024) 116670, §"PDF and GPD singularities") says the momentum distribution
  "is analytic in whole range of y at finite P^z … Since the correlation function in coordinate space z has finite support (decays exponentially at large z) due to confinement".
  Lemma 7.2 is the precise form of this statement.
  CLAIMS.md says "making a statement of Ji–Liu–Su precise". This should read Ji 2024 (single author), as LAMET §7.2 has it.
  Ji–Liu–Su 2026 (2601.12189) prove the decay and estimate FT errors, but I found no momentum-space strip-analyticity statement there.
* **Prop. 7.3.** |∫_{|λ|>λ_L}| ≤ 2∫_{λ_L}^∞ A e^{−mλ/P^z} dλ/(2π) = (AP^z/(πm)) e^{−m z_L}. **Correct** (also tested numerically).
  ħc = 0.1973269804 GeV fm gives e^{−m z_L} = **0.0794** (1 fm) and **0.0224** (1.5 fm) at m = 0.5 GeV. **Correct.**
  Remark: Ji–Liu–Su 2026 (2601.12189, §"FT precision") give a different, oscillation-aware large-P^z estimate (|h̃(z_L)|/(π|y|)). Prop. 7.3 is the cruder, rigorous majorant.
  It grows with P^z, which should be said when it is printed.
* **Prop. 7.4.** Eigenvalues of (Kf)(x) = ∫_{−1}^1 sin(λ_L(x−y))/(π(x−y)) f(y)dy were computed two ways:
  Gauss–Legendre Nyström (160 and 320 nodes) and an independent Legendre-basis matrix K_mn = √((2m+1)(2n+1)) (−1)^{(m−n)/2} (2/π)∫₀^c j_m j_n dk. The two agree to ≤ 7e-14.
  #{eig > ½} = **3, 6, 10, 16** for λ_L = 5, 10, 15, 25. The trace equals 2λ_L/π exactly (3.183, 6.366, 9.549, 15.915).
  The Landau–Widom log coefficient (1/π²)ln((1−α)/α) is consistent numerically (c = 50…800: measured slopes 0.55 versus 0.47 for α = 1e-2 and 0.91 versus 0.93 for α = 1e-4, within integer-count noise).
  Note: the kernel's normalization (band λ_L, interval [−1,1]) matches the ITD/pseudo-PDF problem.
* **Verdict N10: confirmed.** Present Lemma 7.2 and Prop. 7.4 as classical results applied to LaMET, not as new mathematics. "Recoverable modes" is an interpretation of the eigenvalue count.

## 6. N11 — Lean-style dependency graph

Audit of the §4.5 table against the cited proofs:
* **Monotonicity:** no node is graded above its weakest parent. N3 [A] ← N2 [A] ← N1 [A] ← N0 [R]; N6 [A] ← N4 [A], N5 [R]; N7, N9 [A]; N12 [C] ← (H3), (H5) [C]; N13 [A]/[C].
* **N1 [A]:** JZZ (1706.08962) write "In analogy to HQET, we argue that this theory is renormalizable to all orders". They also write "the above arguments are valid independent of whether the heavy quark field … is defined by a timelike or spacelike vector".
  The BRST proof cited is Bagan et al. 1993 (HQET). The quote in LAMET is accurate, and "asserted for space-like n" is a fair description.
  The RMP (2004.03543) calls the JZZ/GJS argument "the first rigorous proof". Our [A] is more conservative than the RMP's wording; this is defensible, but the printed text should say so.
* **N3 [A]:** two independent all-order arguments. IMQY (1707.03107) state: "We only concentrated on overall divergences but not on subdivergences, because subdivergences can be taken care by forest subtraction …
  The change of divergence indexes … are only for superficial divergence." This matches LAMET's caveat (ii). GJS (1707.07152) use the auxiliary field on the lattice, citing Craigie–Dorn and Dorn.
* **N4 [A], no Zimmermann-level proof:** IJJSZ (1801.03917, §OPE) write "the OPE has been proven for scalar field theory to all orders … and is widely assumed to hold for any renormalizable quantum field theory including QCD.
  By introducing auxiliary fields … equivalent to a product of local renormalizable operators". INSPIRE title and abstract searches ("operator product expansion" with quasi / Wilson line / Ioffe / proof) find no proof beyond IJJSZ's own argument.
  Caveat: by the monograph's own taxonomy ([C] = "widely used but not proven"), grading N4 as [A] rather than [C] is a judgment. Remark 4.5.1 supports it (the reduction to local operators of the auxiliary theory, explicit 2–3-loop agreement).
  The judgment should be stated, together with IJJSZ's "widely assumed".
* **N5 [R] in PT:** IJJSZ and Radyushkin 2017 (1705.01488) both state the [−1,1] support "for all contributing Feynman diagrams", citing Radyushkin, PLB 131 (1983) 179, and PLB 767 (2017) 314.
  I did not read the 1983 paper (not on arXiv).
* **"Non-perturbative content isolated in (H3)–(H5)":** true for Thm 4.3(ii) in MS-bar and hybrid. But node N13 (Prop. 3.3) is [C] for ratio and RI/MOM momentum-space matching, because the scheme conversion Z′_X(z) is non-perturbative at large z.
  This is a further non-perturbative input not listed among (H3)–(H5) (Remark 4.5.3 overlooks it). The sentence needs the qualifier "in the MS-bar/hybrid formulation".
* **Verdict N11: confirmed with the two qualifiers.** It is organizational and has no literature precedent in this form.

## 7. N12 — exact Collins remainder of the off-shell triangle

* **Kinematics:** p₁² = p₂² = −m². With Q̃² = 2PP′, (p₁+p₂)² = −2m² − Q̃² − m⁴/Q̃², so Q² = (Q̃² + m²)²/Q̃². Derived by hand.
* **Exact integral.** My Feynman-parameter derivation gives Q²I = ∫_simplex [t x₁(1−x₁) + x₂x₃]^{−1} = ∫₀¹ du ln(u(1−u)/t)/(u(1−u) − t).
  It equals the Usyukina–Davydychev Φ⁽¹⁾(t,t) to < 1e-30 (t = 0.2 … 1e-6). The general-(x,y) UD formula also equals a direct 2D Feynman-parameter integral at x = 0.1, y = 0.03 (1e-18).
  So the formula is right whatever the attribution. The attribution is UD, PLB 298 (1993) 363, checked at abstract level ("exact results for diagrams up to the two-loop level … in terms of polylogarithms").
* **(a) Subtraction terms.** The approximators, read in the reference text (Ex. D.47, (D.26)), are C_SΓ = 1/(D_g e₁e₂), C_{C1}Γ = (1/(D_g h₂))(1/D₁ − 1/e₁), C_{C2}Γ analogous, and C_HΓ = D_g/(t₁h₁t₂h₂).
  I derived the k⁻ residues independently (pole positions for each k⁺ range) and did the K- and k⁺-integrals analytically.
  The results are ∫C_S = Q̃^{−2}(μ²Q̃²/m⁴)^ε Γ(ε)²Γ(1−ε), ∫C_{C1} = Q̃^{−2}(μ²/m²)^ε Γ(ε)J(ε) with J = B(−ε,1−ε), and ∫C_H = −Q̃^{−2}(μ²/Q̃²)^ε Γ(ε)J(ε).
  Since Γ(ε)Γ(−ε) = −Γ(1+ε)Γ(1−ε)/ε², these equal Q̃^{−2}(μ²Q̃²/m⁴)^ε𝓑, −Q̃^{−2}(μ²/m²)^ε𝒜 and Q̃^{−2}(μ²/Q̃²)^ε𝒜. **(a) confirmed.**
  An mpmath 2D quadrature at ε = 0.3 agrees to 2e-8 relative.
* **(b)** With ln(𝒜ε²) = −γε − ζ₂ε²/2 and ln(𝓑ε²) = −γε + 3ζ₂ε²/2, the poles cancel (1−2+1 = 0; ℓ_Q − 2ℓ_m + (2ℓ_m − ℓ_Q) = 0). The finite part is (ℓ_m − ℓ_Q)² + 2ζ₂ = ln²(Q̃²/m²) + π²/3 (sympy). **Confirmed.**
* **d = 4 remainder.** My own residue densities integrated in d = 4 give ∫ρ_Γ = 11.9346926034091 = I. The remainder ∫(ρ_Γ − Σρ_R) = **−0.0173434339580862** = I − (D.32). **Confirmed.**
* **(c) Exact closed form (new sharpening found here).** With σ = m²/Q̃², t = σ/(1+σ)², √(1−4t) = (1−σ)/(1+σ) and ρt = σ:
  **∫r = [4Li₂(−σ) + σ²(ln²σ + π²/3)] / (Q̃²(1−σ²))**
  This agrees with Φ⁽¹⁾/Q² − (D.32) to 30 digits at the R6 point and at t = 1e-2, 1e-4, 1e-7.
  Expansion (sympy): Q²∫r = −4t + t²(L² − 15 + π²/3) + t³(6L² − 4L − 490/9 + 2π²) + …, so **no logarithm at NLP**.
  Q²I = L² + π²/3 + t(2L² − 4L − 4 + 2π²/3) + t²(6L² − 14L − 11 + 2π²) + O(t³L²); the residual at t = 1e-9 is 7.6e-24. **Confirmed.**
* **Literature:** the small-t expansion of Φ⁽¹⁾ is elementary. The statement concerns the reference's specific Collins approximators and is not claimed to be new ("sharpened"). I found nothing printing it.
  INSPIRE: "off-shell Sudakov" returns only Belitsky et al. 2022 (N = 4), which is unrelated.
* **Verdict N12: confirmed.**

## 8. Items for the authors (LAMET.md / REFDOC)
1. LAMET §5.1(b) and §14 item 7: cite Chen et al. 2016 App. B (helicity K̄_n and its x-space solution) as the same transformation. Replace "TMC commutes with matching" by q̃_Γ = C_Γ ⊗ q_M^Γ.
2. LAMET §5.3 and §14 item 8: the −¼ / −5/12 normalization terms and the 1/(1−x)² remark are BVZ eqs. (65)–(66) (label (bR)).
3. LAMET §4.6(d) Prop. 4.5 and §14 item 9: correct the hybrid statement and the Regge-sea conclusion (§4.3 above). §3.7's "1/u² decay" holds only at fixed λ_S.
4. LAMET Remark 4.5.3: add N13 (ratio/RI-MOM, [C]) as a further non-perturbative input.
5. N12: optionally print the closed form of §7.
