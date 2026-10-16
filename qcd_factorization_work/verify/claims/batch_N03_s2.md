# Verification batch N03–N08 (stage 2, second independent verifier)

Date: 2026-10-11. All six claims are of kind `new_result`. The stage-1 verdicts (batch_N01_s1.md for N03–N06, batch_N07_s1.md for N07–N08) were **not** relied on: every formula was re-derived or re-computed by a route different from stage 1 and from the project scripts, and every literature statement used below was read in the source downloaded fresh into my scratch area (arXiv e-prints; Collins' book chapter 11 from the Cambridge open-access reissue).

## 0. Method, sources, reproduction

**Own scripts** (in `verify/claims/batch_N03_s2_scripts/`, run with `python3 -I`; logs `*.log` next to them):

| script | claim | result | method (differs from stage 1) |
|---|---|---|---|
| `n03_landau_cn.py` | N03 | 11/11 | exact rational cycle/cut-space ranks on 120 random multigraphs with random unimodular loop-basis changes; finite-difference gradients; LP Landau-point / good-direction tests for the eikonal orientation; sign-condition statistics |
| `n04_moment_reduction.py` | N04 | 9/9 | one-loop Mellin moments of the kernel derived symbolically; distributions at z=0 vs parity-restricted moments; Taylor/moment generating function |
| `n05_quasi_unphysical.py` | N05 | 45/45 | (A) own analytic Feynman-parameter reduction with symbolic 3-D master integrals; (B) **direct Wick rotation in the loop momentum, no Feynman parameters**, 2-D quadrature (valid for x>2, x<0); (C) Feynman-parameter numerics for 1<x<2; traces with explicit Dirac matrices; DR vs cutoff tadpole; ε→0 limit of IJJSZ eq. (1loopquasi) |
| `n06_threshold.py` | N06 | 40/40 | exact asymptotics from Γ(ε)(iλ)^(−ε) (symbolic); numerics with E1 and the ε-derivative of the lower incomplete gamma function (cross-checked against the ₃F₃ series and direct quadrature); RG algebra |
| `n07_tmc_components.py` | N07 | 32/32 | **explicit component construction of the symmetric traceless tensor** P^{μ1}…P^{μN} − traces in exact arithmetic (trace conditions solved directly; no Gegenbauer or harmonic-polynomial formula), then contraction for γ^z and γ^0; x-space checks against Chen et al.'s printed helicity formula; dilatation covariance of the kernel |
| `n08_fourier_dichotomy.py` | N08 | 20/20 | closed-form ₁F₁ transform of ρ = α⁴(1−α)⁵ and direct Fourier inversion; endpoint asymptotics of the BVZ renormalon kernels; normalization integrals |

**Project scripts re-run** (logs `rerun_project_*.log`): `others/scripts/s1_landau_gordan.py` 10/10; `lamet/scripts/s1_kernels.py` 51/51, `s3_threshold.py` 9/9, `s4_tmd_bvz.py` 20/20, `s5_lemmas.py` 12/12, `s6_tmc.py` 40/40. My verdicts rest on my own scripts, not on these.

**Literature read** (fresh downloads, read as text):
* Collins arXiv:2007.04085 (v1; INSPIRE recid 1805806, 39 citers, no journal version): Thm 1 (`thm:main.contour`), Thms 2–3, Defs 6–7, Sec. VIII B (sign condition, eq. `restrict` = (8.15)), Sec. IV, conclusions.
* Collins, *Foundations of perturbative QCD*, ch. 11 (OA reissue, doi 10.1017/9781009401845.011), pp. 409–412.
* Braun–Manashov–Moch–Strohmaier: arXiv:1901.06172 (JHEP 02 (2019) 191) §§2–3; arXiv:1810.04993 ("Conformal symmetry of QCD in d dimensions"), text after eq. (13).
* Moch–Vermaseren–Vogt hep-ph/0403192 (non-singlet three-loop splitting functions), §2.
* IJJSZ arXiv:1801.03917: App. B (eqs. (B1)–(B3)), eq. (1loopquasi), eq. (1loopiofferen).
* Ji–Liu–Su arXiv:2305.04416: §§2–4 (eqs. hardoneloop, jetoneloop, JetoneloopIM, RGEs, text after hardoneloop).
* Ebert–Stewart–Zhao arXiv:1901.03685, eq. (C_nlo); Ji–Liu–Liu arXiv:1911.03840, lines with ln H^(1) and c₁.
* Chen–Cohen–Ji–Lin–Zhang arXiv:1603.06664: corrections.tex (eq. Kn), polPDFs.tex (eq. Knbar), tmc_appendix.tex (App. B).
* Braun–Vladimirov–Zhang arXiv:1810.00048: eqs. (target-parallel), (target-perp), Balitsky–Braun identity, (t4-qITD), (t4-nqITD), (t4-Qparallel), (t4-Qperp), (cR), (bR).
* RMP Ji et al. arXiv:2004.03543: eq. (fact_0) and the later twist-4 paragraph.
* Radyushkin arXiv:1702.01726; Bhattacharya–Cocuzza–Metz arXiv:1903.05721 (PRD 102 (2020) 054021); Aslan–Tandogan arXiv:2605.12373; Monahan–Neumann arXiv:2609.40205; 2412.19862; Agarwal–Magnea–Signorile-Signorile arXiv:2112.07099 (§ Landau equations / Coleman–Norton); Mühlbauer arXiv:2011.10368; Ma arXiv:1910.11304; Gardi–Herzog–Jones 2211.14845; Ma 2312.14012, 2601.22144; Sterman–Venkata 2309.13023.
* INSPIRE: citers of Collins 2020 (39) and of Chen:2016utp (250; the 58 with "target mass" in the full text were screened by title, and the sources of the plausible ones grepped for their TMC statements).

## 1. Summary

| id | verdict | already in the literature? | what must change before printing |
|---|---|---|---|
| N03 | **confirmed** ([R]† inherited from the unpublished Collins Thm 1) | Not new in substance: one-line specialization of Collins 2020 Thm 1, which Collins states covers Wilson lines; the closure step is the classic Coleman–Norton algebra (textbook as a necessary condition, e.g. the review arXiv:2112.07099 by Agarwal–Magnea–Signorile-Signorile, § "The Coleman-Norton physical picture"). No paper found that prints the momentum-space iff with Wilson lines explicitly. | State that every denominator is written as (A_j + i0); then Δ_j = n_j for (n_j·k_j + i0) and Δ_j = −n_j for 1/(n·k − i0). Restrict to integrals of Collins' form (amplitude-level/uncut graphs; conjugated −i0 propagators are not covered by (8.15)). Say that soft massless lines (D_j = 0) give degenerate Landau points and that the corollary does not say which denominators trap (Collins' open items; Ma 2019). |
| N04 | **confirmed as a conditional [A] argument**, with corrections to the wording | **Not new**: BMMS JHEP 02 (2019) 191 eqs. (2.4), (2.6), (3.1), (3.2) (renormalized light-ray operators as generating functions of renormalized local ones; Joglekar–Lee decomposition carried over); idea from Balitsky–Braun 1989; Collins 2011 §11.4 asserts (11.20) "for the same reasons as with the local operators". | (i) Add the existence of the kernel as a hypothesis (or derive it order by order); (ii) "physical matrix elements" = hadronic (BRST-invariant) states or non-forward insertions: for forward on-shell partonic matrix elements in DR the BRST/EOM operators do **not** drop out (BMMS arXiv:1810.04993; Hamberg–van Neerven; Collins–Scalise); (iii) per-C-parity kernels on [0,1] (or one kernel on [−1,1]) — a single [0,1] kernel with "all N" is wrong beyond one loop; (iv) Müntz–Szász gives uniqueness only up to distributions at z = 0; (v) the renormalization use is Collins §11.4 eq. (11.20), pp. 411–412. |
| N05 | **confirmed** | **Not new**: IJJSZ App. B eqs. (B1)–(B3) at ε = 0, and the sums are IJJSZ eq. (1loopquasi) at ε → 0 (checked). | Present as an independent re-derivation. The tadpole is finite only in DR; with a 3-D cutoff it is +2aΛ/(π(1−ξ)²p^z) − a/|1−ξ| (LAMET §4.6(b) "all integrals finite in d = 4" is wrong for the tadpole). |
| N06 | **confirmed** | **Not new**: Ji–Liu–Su 2023 (eqs. hardoneloop, jetoneloop, JetoneloopIM and the text after hardoneloop) state both the one-loop reproduction and H_thr = H_quasi-TMD; H^(1) = ESZ 2019 eq. (C_nlo) = JLL 2020 c₁ + logs. | Call it an independent cross-check. Fix the phase convention (λ_ours = P·z = −P^z z, sgn z = −sgn λ_ours). At one loop the non-cusp terms cancel exactly. Harmonize L_z (LAMET uses L_z for ln(−z²μ²e^{2γ_E}/4) in §1.1 but for ln(4p_z²/μ²) in §6.1). |
| N07 | **confirmed** (all formulas); the slogan "TMC commutes with matching" must be replaced | **Partly**: K^⊥_N ≡ Chen et al. 2016's helicity ratio K̄_N (identical function), and their helicity x-space solution equals our γ^0 formula pointwise; O(c) is BVZ (target-perp), which BVZ already say agrees with Chen et al.; K^⊥_1 = K^⊥_2 = 1 is consistent with (and contained in) the exact, all-twist γ^0 sum rules of Bhattacharya–Cocuzza–Metz 2020 (first two moments P^z-independent). The explicit statement "exact unpolarized γ^0 TMC = K^⊥_N" and the ∂_c representation were not found in print. | Replace "commutes" by q̃_Γ = C_Γ ⊗ q_M^Γ (massless kernel applied to the TMC-transformed PDF); literal commutation fails at O(α_s c). The x-space identity relates the tree-level TMC-transformed distributions, not the full one-loop quasi-PDFs. Cite Chen et al. App. B and BCM 2020. |
| N08 | **confirmed** | **Partly**: Lemma 5.2 is elementary and used implicitly by BVZ in (t4-Qparallel); the −¼ and −5/12 normalization terms and the 1/(1−x)² remark are BVZ eq. (bR) verbatim; the RMP itself quotes both counting rules (eq. (fact_0) and, later, BVZ's 1/(1−y)). The reformulation as an endpoint dichotomy is new as phrasing only. | Attribute the normalization terms to BVZ (bR). In Cor. 5.3 say "generic exponents (b+δ ≠ 0, 1)" and keep the constant: ρ₄/q → C(1−x)^δ gives (Λ²/P_z²)C(b+δ)(b+δ−1)(1−x)^{δ−2}; in the BVZ model C = 1/(b+1), so R → b. |

## 2. N03 — Coleman–Norton picture in momentum space, including massless and eikonal lines

### 2.1 What Collins proves (read in arXiv:2007.04085)
* Integral form (2.4): ∫ d^dw B(w;z)/∏_j (A_j(w;z) + iε)^{n_j}, all A_j real-analytic, real external parameters, real initial contour ("physical region"; external momenta need not be on shell).
* **Thm 1** (`thm:main.contour`): at a real point w_S where a non-empty set of denominators vanishes, "the integration is trapped at w_S if and only if a Landau point exists for the first derivatives of those denominators that are zero", under (a) A_j at most quadratic, (b) the sign condition (8.15). Collins adds: "This condition is obeyed for the denominators encountered in Feynman graphs, including cases with Wilson lines. It also applies to the modified Feynman graphs obtained by applying the typical approximations used in deriving factorization." Thm 1 = Thm 3 (geometric) ∘ Thm 2 (contour deformations).
* **(8.15)** (eq. `restrict`): for the deformation direction v₀ at w_S, all non-zero v₀·E_j·v₀ over the "relevant" j (A_j = 0, D_j ≠ 0, D_j·v₀ = 0, α_j ≠ 0 in the Landau point) have the same sign. Sec. VIII B shows: k² − m² (+i0) gives v₀·E·v₀ = 2v̂² ≤ 0 (massive or massless with k ≠ 0); soft lines (D = 0) are not relevant; Wilson lines have E = 0; non-relativistic and light-front-approximated denominators have the same sign.
* Status: arXiv v1 only (INSPIRE record without publication info), so [R]† is the right grade.

### 2.2 Independent derivation of the corollary
* With w = (ℓ₁,…,ℓ_L) ∈ R^{4L} and k_j = Σ_L η_{jL}ℓ_L + (external): ∂(k_j² − m_j²)/∂ℓ_L^μ = 2η_{jL}k_{jμ}, ∂(n_j·k_j)/∂ℓ_L^μ = η_{jL}n_{jμ} (finite-difference check on random graphs, `n03` (1)). Hence Σ_jλ_jD_j = 0 as a dual vector on R^{4L} ⇔ Σ_j η_{jL}λ_jΔ_j^μ = 0 for every L and μ, with the factor 2 absorbed into λ_j ≥ 0. Thm 1 then gives "trapped ⇔ such λ exist, supported on the vanishing denominators". ✓
* Coleman–Norton closure: the columns η_{·L} form a basis of the cycle space; X ⊥ cycle space ⇔ X lies in the cut space ⇔ X_j = x_{head(j)} − x_{tail(j)} for vertex positions x_v. Verified with exact rational ranks on 120 random multigraphs, including random unimodular changes of loop basis (basis independence) (`n03` (2)). ✓
* Sign condition: random check of k·v = 0 ⇒ v² ≤ 0 for on-shell k of either energy sign, massive and massless (5000 samples); E = 0 for eikonal lines; v·E·v = −2v_T² ≤ 0 for light-front-approximated denominators (`n03` (4)). ✓

### 2.3 Caveats that the printed statement needs
1. **Orientation.** The corollary holds with Δ_j = n_j only if each eikonal denominator is written as (n_j·k_j + i0) with k_j along the line orientation. Toy check (gluon k, light-like Wilson line n, massless quark p−k off shell, k = βn): with (n·k + i0) there is a Landau point iff β < 0; with 1/(n·k − i0) = −1/(−n·k + i0) iff β > 0. In the non-trapped cases an explicit good direction exists (LP margin 0.8–1.0) (`n03` (3)). In Collins' integral form, where everything is A_j + iε, this is automatic; the monograph must say so.
2. **Scope.** (8.15) is guaranteed only when every quadratic denominator enters as (k² − m² + i0). A conjugated propagator rewritten as (−(k² − m²) + i0) has v·E·v ≥ 0, the opposite sign (`n03` (4)). Thm 1, and hence the corollary, therefore covers amplitude-level and uncut graphs (forward amplitudes, operator matrix elements) with Wilson lines and approximated denominators. It does not directly cover cut graphs; those must be treated side by side or through unitarity. The sentence in CLAIMS/OTHERS "(8.15) holds for all graphs used … checked in S1(c)" should be restricted accordingly; S1(c) tests only +i0 propagators.
3. **Degenerate Landau points.** A soft massless line (k_j = 0) has D_j = 0 and gives a Landau point by itself (`n03` (5)), so the classical picture can be degenerate. The corollary gives existence only. It does not say which denominators actually trap, nor anything about approximated graphs t_σA (Ma arXiv:1910.11304 §2.2: "the original Coleman–Norton interpretation does not necessarily apply for the entire graph"). Collins lists the massless CN picture among his open items for exactly this reason. OTHERS §1.5 already says this.

### 2.4 Literature
* The momentum-space Landau equations with the CN interpretation are textbook *as necessary conditions* (Feynman-parameter derivation), e.g. arXiv:2112.07099 §§ "The case of Feynman diagrams: the Landau equations" and "The Coleman–Norton physical picture". They are used routinely (Gardi–Herzog–Jones 2211.14845, Ma 2312.14012 and 2601.22144, Sterman–Venkata 2309.13023).
* Collins 2020 states that Thm 1 covers Wilson lines.
* I listed all 39 INSPIRE citers of Collins 2020 by title and grepped the sources of the eight that deal with Landau equations, regions or Coleman–Norton (2011.10368, 2211.14845, 2312.14012, 2601.22144, 2112.07099, 2309.13023, 2607.15126, 2609.29442). None writes the momentum-space iff with eikonal lines as a corollary of Thm 1; those that use the CN picture use it as the standard (necessary-condition) interpretation. Mühlbauer 2011.10368 treats singularities in external parameters by isotopy, without positivity or Wilson lines. INSPIRE full-text "Landau point" & eikonal returns only Collins 2020 and two papers unrelated to the corollary (hep-ph/0006255, hep-ph/0008309).
* **Verdict: confirmed.** The proof is correct. It inherits the † of Thm 1, with the orientation and scope qualifiers above. It is not new in substance and should be presented as a remark or corollary, not as a significant new theorem.

## 3. N04 — moment reduction of the BRST classification for the bilocal PDF operator

### 3.1 Logic check
1. (H3) together with forwardness: the moments of the bare bilocal matrix element are the bare local twist-2 matrix elements. The all-plus component of ψ̄γ^{μ1}D^{μ2}…D^{μN}ψ is automatically symmetric and its trace terms ∝ g^{++} vanish, so only total-derivative terms are dropped, and these vanish forward. ✓ Numerical illustration of "entire FT with moment Taylor coefficients" in `n04` (c).
2. (H1) gives ⟨O_N^R⟩ = Z_N⟨O_N^bare⟩ + ⟨A_N⟩ + ⟨B_N⟩. The last two vanish in physical (BRST-invariant, on-shell) states. ✓
3. Given a distribution Z_OO with moments Z_N, the convolution Z_OO ⊗ f^bare has finite moments. By (H2) each ε-pole coefficient is a compactly supported distribution with all moments zero, hence zero. ✓ So the renormalized bilocal equals Z_OO ⊗ bare, and it is the generating function of the renormalized gauge-invariant local operators. ✓ The logic is valid **given** the hypotheses plus the existence of Z_OO.

### 3.2 Corrections needed in the statement
* **Existence of Z_OO** is assumed ("define Z_OO through its moments"), not proven. A sequence of moments need not come from a distribution. At one loop it does: ∫₀¹z^{N−1}[(1+z²)/(1−z)]₊ = 3/2 + 1/(N(N+1)) − 2S₁(N) for all N, derived in `n04` (a). At higher orders it requires the anomalous dimensions to be Mellin moments of kernels, which is the light-ray-operator statement itself. It must be listed as a hypothesis (H4) or proved order by order.
* **Physical matrix elements.** BMMS arXiv:1810.04993, read: "the vanishing of physical matrix elements with BRST or EOM operators requires the on-shell limit with respect to their external momentum q … the limits q² → 0 and d → 4 do not commute. Therefore, theorems on the renormalization of gauge invariant operators … directly apply to matrix elements with the operators inserted at nonzero momentum … [two-point calculations] are typically realized with operators inserted at zero momentum. In this case, physical matrix elements of gauge variant operators do not vanish, the mixing matrix of operators is not triangular …". Forward partonic matrix elements in DR are therefore exactly the case where the conclusion fails. The statement must say hadronic (BRST-invariant) states, or non-forward/off-forward insertions. Collins (§11.4, read) likewise notes that beyond one loop off-shell renormalization needs the A and B operators (Hamberg–van Neerven 1992; Collins–Scalise 1994).
* **Parity sectors.** The displayed "∫₀¹dz z^{N−1}Z_OO(z) = Z^(N) for all N" cannot hold with one [0,1] kernel beyond one loop. P^v_{qq̄} is O(α_s²) (MVV hep-ph/0403192 §2, read), so γ_NS^+ ≠ γ_NS^−, and the odd moments of a [0,1] kernel fix its even moments (Müntz). The correct form is per C-parity sector, which the claim itself indicates, or one kernel on [−1,1] with ∫_{−1}^{1}z^{N−1}Z = Z^(N) (toy illustration `n04` (d)).
* **Uniqueness.** On [−1,1] with all integer moments, uniqueness follows from compact support (polynomials dense); Müntz is not needed. With only even or only odd powers on [0,1], uniqueness holds up to distributions supported at z = 0: δ(z) has zero odd moments and δ′(z) zero even moments (`n04` (b)). This is harmless for convolutions at x > 0, but "uniquely fixed" should read "uniquely fixed on (0,1]".
* **Where Collins uses it.** The gap is stated in §11.3.2, p. 410 (verbatim quote verified). The renormalization use is §11.4, eq. (11.20), pp. 411–412: "For the same reasons as with the local operators used in the OPE (Collins, 1984, p. 318), the renormalization matrix has a triangular form … In physical matrix elements, only the operators O are non-zero … O = Z_OO O_(0)." Prop. 8.1 justifies (11.20) in physical matrix elements, conditionally on H1–H4.

### 3.3 Literature
* BMMS JHEP 02 (2019) 191 (arXiv:1901.06172), read:
  * eq. (2.4): light-ray operators "can be viewed as the generating functions for local quark and gluon operators";
  * eq. (2.6): "Renormalized LROs are defined by the same expression with bare local operators replaced by the renormalized ones";
  * eq. (3.1): the Joglekar–Lee decomposition [O_{χ,nk}] = Ô + B + E;
  * eq. (3.2): Ô_χ(z₁,z₂) = Σ Ψ_{nk} Ô_{χ,nk}(0).
* This is the moment reduction, in the general off-forward setting. It goes back to Balitsky–Braun 1989.
* **Verdict: confirmed** as a correct conditional [A] argument with the corrections above. It is **not new** and must not be labelled "this work".

## 4. N05 — one-loop quasi-PDF in the unphysical regions

### 4.1 Own derivation (CONTEXT rules, Γ = γ⁰, Feynman gauge, massless on-shell quark p = (p^z,0,0,p^z))
* **Traces** (checked with explicit Dirac matrices):
  * vertex: N_v = ½Tr[p̸γ^μk̸γ⁰k̸γ_μ] = −8(p·k)k⁰ + 4p⁰k²;
  * sail 1 (ū γ⁰ k̸ γ³ u) and sail 2 (ū γ³ k̸ γ⁰ u): both 2(p⁰k^z + p^zk⁰).
* **Sail from the Wilson line.** W ≈ 1 + ig∫₀¹ds z·A(sz). The x ≠ 1 part of sail 1 is −ig²C_F∫d⁴k/(2π)⁴ [ūγ⁰k̸γ³u] e^{−ik^z z}/((p^z−k^z)k²(p−k)²). Sail 2 is identical, so the total is twice sail 1.
* **Analytic reduction** (Feynman parameters, l = k − (1−y)p, Wick rotation of l⁰, symmetric integration over the three Euclidean directions, symbolic masters):
  * vertex = a∫₀¹dy y/|x−1+y| = a∫₀¹(1−y)/|x−y|;
  * sails = (a/(1−x))∫₀¹(x+1−y)/|x−1+y| = (a/(1−x))∫₀¹(x+y)/|x−y|.
* **Tadpole.** At x ≠ 1, (ig²C_F/((1−x)²p^z))∫dq⁰d^{d−2}q_T/(2π)^d (q²+i0)^{−1}|_{q^z=(1−x)p^z}. In DR, ∫d^{3−2ε}q/(q²+M²) → −2π²M, giving −a/|1−x|. With a 3-D cutoff Λ the same integral gives +2aΛ/(π(1−x)²p^z) − a/|1−x| + O(1/Λ), checked numerically (slope 2/(π(1−x)²) reproduced at x = 1.5, 3, −0.7).
* **Numerics without Feynman parameters** (method B): Wick rotation k⁰ = ik₄ directly in the loop momentum is legitimate only where no pole of (p−k)² + i0 enters the first quadrant, i.e. x > 2 or x < 0 (for 0 < x < 2 such a pole exists when k_T² < x(2−x)). At x ∈ {2.5, 3.7, 8, −0.4, −1, −3.3}, the 2-D (k₄, k_T) quadrature reproduces both the vertex and the sail to better than 1e−7.
* **Method C** (Feynman-parameter numerics) at x ∈ {1.05, 1.5, 1.9, 2.5, −0.4}: agreement to 1e−8. The **sail sign** is thus fixed with CONTEXT's consistent conventions (D = ∂ − igA, W = P exp(+ig∫dz·A)). The opposite sign would also destroy the MS-bar tail −3a/(2|x|) of the sum, which is reproduced (|x| = 10³: −1.503, −1.497).
* **Sums.**
  * Numerically at 11 points, and symbolically: for x > 1, a[((1+x²)/(1−x))ln(x/(x−1)) + 1]; for x < 0, a[−((1+x²)/(1−x))ln(−x/(1−x)) − 1]. ✓
  * The ε → 0 limit of IJJSZ eq. (1loopquasi), where the 1/ε_IR bracket vanishes at ε = 0 for x ∉ [0,1], equals the claimed sums at x ∈ {1.5, 3, −0.5, −2} to 1e−12. ✓
* **IJJSZ App. B** (read): (B1) vertex + w.fn. = (α_sC_F/2π)(μ²/p_z²)^ε[(1−ε)∫₀¹dy(1−y)|x−y|^{−1−2ε}Γ(ε+½)/√π + δ-terms]; (B2) sail ∫₀¹dy (x+y)/((1−x)|x−y|^{1+2ε})·Γ(ε+½)/√π + δ-terms; (B3) tadpole −(1−2ε)^{−1}|1−x|^{−1−2ε}Γ(ε+½)/√π + δ-terms. At ε = 0 and x ∉ [0,1] these are exactly the three claimed expressions. ✓ (Their (B2)–(B3) carry (4πμ²/p_z²)^ε against (μ²/p_z²)^ε in (B1), an MS/MS-bar inconsistency that is irrelevant at x ≠ 1, ε = 0.)
* **Verdict: confirmed.** It is an independent re-derivation of IJJSZ App. B, not a new result. Printing note: only the vertex and the sail are finite in d = 4; the tadpole needs DR (or a δm-type subtraction).

## 5. N06 — one-loop threshold factorization; H_thr = H_quasi-TMD

### 5.1 Exact asymptotics (own derivation, `n06` (a))
* **Conventions.** λ = P·z = −P^z z, so sgn z = −sgn λ. h(λ) = ∫₀¹dα C(α,l)e^{iαλ}, with the γ^t kernel of IJJSZ. l = ln(−z²μ²e^{2γ_E}/4) (JLS l_z), L = ln(4p_z²/μ²) (JLS L_z), l + L = 2Λ, Λ = ln|λ| + γ_E.
* **Inputs.** From ∫₀¹β^{ε−1}(e^{−iβλ}−1) = Γ(ε)(iλ)^{−ε} − 1/ε + O(1/λ):
  * ∫₀¹(e^{−iβλ}−1)/β → −(ln(iλ)+γ_E);
  * ∫₀¹lnβ(e^{−iβλ}−1)/β → (ln(iλ)+γ_E)²/2 + π²/12.
* **Result.** These give, exactly (symbolic difference 0),
  **e^{−iλ}h(λ) → 1 + a[H^(1) + J̃^(1) + iπ sgn(z)(L−1)]**,
  with H^(1) = −2 + π²/12 − L²/2 + L and J̃^(1) = l²/2 + l + π²/12 + 2. This is JLS's eq. (hardoneloop) + eq. (jetoneloop) + eq. (JetoneloopIM).
* **Phase sign** fixed physically. The odd term iπ sgn(λ)(1−L) Fourier-transforms into a(L−1)P(1/(1−x)); combined with the even part (L−1)P(1/|1−x|) this gives 2a(L−1)/(1−x) only for x < 1. That matches the MS-bar kernel near ξ → 1⁻ and its absence at ξ → 1⁺ (IJJSZ eq. (quasi-matching)).

### 5.2 Numerics (different method from stage 1 and s3)
* **Method.** Exact one-loop e^{−iλ}h(λ) from E1(iλ) for the 1/β term and the ε-derivative of the lower incomplete gamma function for the lnβ/β term. That representation was cross-checked against the ₃F₃ series and direct quadrature at λ = 7.3, −12.1, 40 (agreement < 1e−15).
* **Results.**
  * At L ∈ {0, 1.3, −0.8} and λ = ±1e2, ±1e3, ±1e4, ±1e5 the residual is 0.311, 0.0414, 0.00241, 0.000272 (L = 0). It decays as ln²|λ|/|λ| (ratio test between 1e4 and 1e5).
  * Im of the residual flips sign with λ.
  * At |λ| = 1e5 and L = 1.3, Im = ∓0.9427 ≈ ∓0.3π, as claimed.
  * The numbers coincide with s3 and with the stage-1 values, obtained here by a different representation.

### 5.3 Anomalous dimensions and universality
* **Anomalous dimensions.**
  * d lnH/d lnμ = 2a(L−1) = Γ_cusp L + γ̃_H, with Γ_cusp = 2a = α_sC_F/π and γ̃_H = −2a.
  * d ln J̃/d lnμ = 2a(l+1) = Γ_cusp l − γ̃_J, with γ̃_J = −2a. JLS eq. (resulttildegammaJ) at one loop gives γ̃_J = −α_sC_F/π. ✓
  * The phase gives −iπΓ_cusp sgn z.
* **Sum.** Γ_cusp[ln(λ²e^{2γ_E}) − iπ sgn z], with no explicit μ; the non-cusp terms cancel exactly at one loop (γ̃_H − γ̃_J = 0). It equals the threshold limit of the kernel RGE dC/d lnμ² = a[3/2 δ − B] paired with e^{−i(1−α)λ} (symbolic). ✓
* **Universality.**
  * ESZ 2019 eq. (C_nlo) (read) gives C^TMD = 1 + (α_sC_F/4π)(−ln²(ζ/μ²) + 2ln(ζ/μ²) − 4 + π²/6), ζ = (2xP^z)².
  * JLL 2020 (read) gives ln H^(1) = α_s[c₁ + (C_F/2π)(L − L²/2)], c₁ = (C_F/2π)(−2 + π²/12).
  * Both equal H^(1). Re H^±_LFWF at one loop also equals H^(1). ✓
* **JLS text after eq. (hardoneloop)** (read): "the above hard kernel together with the jet function J_f completely reproduces the one-loop quasi-PDF in MS-bar scheme … at power (1−y)^{−1} … Moreover, the hard kernel completely agrees with the hard kernel for quasi-TMDPDF/quasi-LFWF factorization".
* **Verdict: confirmed.** It is an independent cross-check of JLS 2023, not a new result.

## 6. N07 — exact target-mass correction for γ⁰

### 6.1 Component-level derivation (`n07`)
* **Construction.** T^{μ1…μN} = Σ_k β_k Sym[g^{⊗k}⊗P^{⊗(N−2k)}] was built with the β_k fixed by imposing the trace conditions on all components (exact arithmetic, N ≤ 6). Then:
  * γ^z: T(z,…,z)/(P·z)^N gives K_N = 1, 1+c, 1+2c, 1+3c+c², 1+4c+3c², 1+5c+6c²+c³;
  * γ⁰: T(u,z,…,z)/(P⁰(P·z)^{N−1}), u = e_t, gives **K^⊥_N = 1, 1, 1+2c/3, 1+3c/2, 1+12c/5+3c²/5, 1+10c/3+2c²**.
* **Checks.**
  * These equal Σ_i C(N−i,i)((N−2i)/N)c^i. ✓
  * K^⊥ = K − (2c/N)dK/dc for N = 1…40. ✓
  * K^⊥_N ≡ Chen et al.'s helicity K̄_N = Σ_i((N−i)/N)C(N−i−1,i)c^i (polPDFs.tex eq. Knbar, read) for N = 1…40. The reason: S·P = 0 for helicity and u·z = 0 for γ⁰ produce the same derivative structure on T_N(P,z).

### 6.2 x-space
* q̃_{γ0} = q̃_{γz} − 2c∫₀¹(dy/y)∂_c q̃_{γz}(x/y) was evaluated with a test PDF that has quark and antiquark parts, c = 0.15. Its moments n = 1…5 equal K^⊥_n a_n to 1e−9. Note: the support of q̃_{γz} is [−f₊/2, f₊/2] when antiquarks are present.
* **Chen et al. App. B** (read), helicity solution Δq̃ = (1/(1+4c))[(f₊/2)Δq(2x/f₊) + (f₋/2)Δq(−2x/f₋)] − ∫_{±∞}^x (dy/y)(2c/(1+4c)^{3/2})[Δq(2y/f₊) + Δq(−2y/f₋)]. With Δq → q it equals our γ⁰ formula **pointwise** at 7 points, both signs of x (agreement ~1e−10). So the transformation is already in print, as the helicity TMC.
* **O(c).** K^⊥_n = 1 + c(n−1)(n−2)/n. These are exactly the moments of BVZ (target-perp) (read), q − c(xq′+3q) + 2c∫_{|x|}^1(dy/y)q(x/y), since ¼m²v²/(pv)² = −c. ✓ BVZ write: "The target mass corrections in Eqs. (target-parallel) and (target-perp) agree with those derived in Ref. [Chen:2016utp] when expanded to O(m²v²/(pv)²)". Since Chen et al. computed only γ^z (unpolarized) and the polarized cases, the ⊥ agreement is precisely the helicity identification at O(c).
* **K^⊥_1 = K^⊥_2 = 1.** Bhattacharya–Cocuzza–Metz PRD 102 (2020) 054021 (arXiv:1903.05721, read) give model-independent sum rules: ∫dx (1/δ₀) f_{1,Q(0)} = N, ∫dx x (1/δ₀) f_{1,Q(0)} = A^q(0) (P³-independent), and ∫dx x f_{1,Q(3)} = A^q(0) − (δ₀² − 1)C̄^q(0). These are consistent with K^⊥_1 = K^⊥_2 = 1 and K_2 = 1 + c plus a twist-4 C̄ term, with δ₀² − 1 = 4c. The no-correction statements are therefore known in exact (all-twist) form.
* **Literature search.**
  * Of the 58 citers of Chen:2016utp with "target mass" in the full text, the sources of the plausible ones were grepped for their TMC statements: 2609.40205 (states that TMCs are known to all orders only at tree level, from Chen et al.), 2605.12373 (model study of γ⁰ vs γ³), 2412.19862, 2011.14971, 2105.13313 and 2608.00251. No other paper gives the exact unpolarized γ⁰ TMC formula.
  * The all-order γ⁰ result also follows from the Balitsky–Braun identity Π[q̄γ_αq] = ∫₀¹dt ∂/∂v^α Π[q̄(tzv)v̸q(0)], quoted by BVZ, combined with the all-order ∥ projection.
  * Novelty is therefore limited to the explicit identification and the ∂_c representation.

### 6.3 "TMC commutes with matching"
* **The correct statement is LAMET Prop. 5.1(d), q̃_Γ = C_Γ ⊗ q_M^Γ** (massless kernel acting on the TMC-transformed PDF). This follows from the leading-twist OPE because c is λ-independent at fixed P^z. ✓
* **Literal commutation is false.** C ⊗_{P} D_s q = D_s(C ⊗_{sP} q) for D_s q(x) = q(x/s)/s. This was verified numerically with the P-dependent one-loop MS-bar piece (3.59298 = 3.59298). The naive commutator D_s(C⊗_P q) − C⊗_P D_s q is −0.131 at s = 1.08, x = 0.4: O(a ln s) ≠ 0. Because the γ^z TMC is a dilatation to O(c), TMC∘C ≠ C∘TMC at O(α_s c).
* The x-space identity of §6.2 holds for the tree-level TMC-transformed distributions only. The one-loop kernels for γ⁰ and γ^z differ by 2a(1−ξ).
* **Verdict: confirmed** (all formulas), with the wording fix and the attributions above.

## 7. N08 — Fourier lemma and endpoint dichotomy

* **Lemma 5.2.** λ²e^{−ixλ} = −∂_x²e^{−ixλ} and z² = −λ²/P_z² give FT[z²Λ²r] = +(Λ²/P_z²)ρ″ as distributions. ✓
  * Numerical test with ρ = α⁴(1−α)⁵, using r = B(5,6)₁F₁(5;11;iλ) in closed form (checked against quadrature to 1e−25) and direct inversion: FT[λ²r] = −ρ″ at x = 0.25, 0.5, 0.8 (|diff| ≤ 1.1e−6), and ≈ 0 at x = 1.3.
  * The sign agrees with BVZ: their −κv²Λ²/(pv)²(d/dx)² in (t4-Qparallel) equals +κΛ²/P_z²(d/dx)² with v² = −1. So BVZ already use the identity.
* **Endpoint factors.** ρ ~ x^a gives a(a−1)/x²; ρ ~ (1−x)^b gives b(b−1)/(1−x)² (symbolic). ✓
* **Cor. 5.3, checked on the BVZ renormalon model.** ρ₄ = ∫_x^1(dy/y)k(y)q(x/y), with k_∥ = y + ȳlnȳ and k_⊥ = k_∥ + yȳ.
  * The local exponent of ρ₄/q at x → 1 is 0.9995–0.9999 for b = 2, 3, 4.5 (δ = 1). ✓
  * (1−x)ρ₄″/q → b, i.e. the claimed (b+δ)(b+δ−1) times the constant C = 1/(b+1). This is consistent with s4's R_Q → b.
  * Small x: ρ₄/q → const, giving Λ²/(x²P_z²).
  * δ = 0 reproduces RMP eq. (fact_0) (read): O(Λ²/((1−y)P^z)²), "suppressed by … the spectator momentum (1−y)P^z". The RMP later quotes BVZ: "enhanced as 1/y² and 1/(1−y)". The two published rules are thus both in the RMP; Cor. 5.3 is a clean reformulation.
* **P = 0 normalization.**
  * ∫₀¹(y + ȳlnȳ) = 1/4 and ∫₀¹(y + ȳlnȳ + yȳ) = 5/12 (symbolic).
  * [k]₊ = k − ¼δ(ȳ) shifts R^∥ by −¼x̄x²q″/q, with relative correction −¼b(b−1)/(1−x)² (δ = 0).
  * BVZ eq. (bR) (read) gives R̄^∥ = R^∥ − ¼(x̄x²/q)q″ and R̄^⊥ = R^⊥ − (5/12)(x̄x²/q)q″, adding: "the additional terms are proportional to the second derivative of the quark PDF and thus enhanced as 1/(1−x)² at x → 1." ✓
* **Verdict: confirmed.**
  * The Lemma is elementary (implicit in BVZ).
  * The normalization statement is BVZ's.
  * The dichotomy is a correct implication for generic exponents (b+δ ≠ 0, 1), with the prefactor constant kept.
  * The endpoint behaviour of ρ₄ itself stays [C], as the source says.

## 8. Items for the authors (OTHERS.md / LAMET.md / spec)
1. **N03 (OTHERS §1.5).**
   * Add the +i0 convention: Δ_j = n_j for (n_j·k_j + i0).
   * Restrict to integrals in Collins' form (all denominators A_j + i0; conjugated propagators excluded).
   * Replace "this work" by "corollary of Collins 2020 Thm 1".
2. **N04 (OTHERS §8.3(b)).**
   * Add (H4), the existence of the kernel.
   * "Physical" = hadronic (BRST-invariant) states or non-forward insertions; cite BMMS 1810.04993 for the zero-momentum caveat.
   * Use per-parity kernels or one [−1,1] kernel.
   * Uniqueness on (0,1].
   * Cite Collins §11.4 (11.20) and BMMS JHEP 02 (2019) 191 eqs. (2.4), (2.6), (3.1)–(3.2) as prior art; drop "this report".
3. **N05 (LAMET §4.6(b)).** Delete "all integrals are finite in d = 4": the tadpole is linearly divergent with a cutoff (+2aΛ/(π(1−ξ)²p^z)). Present as a re-derivation of IJJSZ App. B.
4. **N06 (LAMET §6.1).** Harmonize the L_z notation, state the phase convention, and present as a cross-check of JLS 2023.
5. **N07 (LAMET §5.1, §14 item 7).**
   * Replace "TMC commutes with matching" by q̃_Γ = C_Γ ⊗ q_M^Γ.
   * Cite Chen et al. App. B (helicity K̄_N, the same transformation), BVZ (O(c), with their remark on Chen et al.), and Bhattacharya–Cocuzza–Metz 2020 (exact γ⁰ sum rules).
   * "New closed form" should read "identification and compact representation".
   * Side observation, not verified further: lattice analyses that apply the γ^z formula K_N to γ_t data (e.g. Fan et al. 2005.12015, as noted at stage 1) would be inconsistent with K^⊥_N.
6. **N08 (LAMET §5.2–5.3, §14 item 8).** Attribute the −¼/−5/12 terms and the 1/(1−x)² remark to BVZ eq. (bR). In Cor. 5.3 add "generic exponents" and keep the constant.
