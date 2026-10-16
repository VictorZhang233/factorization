# Verification batch N10, N11, N12, N15, N16, N17 (stage 2, independent second verifier)

Date: 2026-10-11. Default stance: skeptical. I did not rely on the stage-1 verdicts and used a different method for each claim wherever possible.
The stage-1 reports are `batch_N07_s1.md` (§5 N10, §6 N11, §7 N12) and `batch_N13_s1.md` (§4 N15, §5 N16, §6 N17).
Sources of the claims: `frontier/lamet/LAMET.md` §4.1, §4.5, §7.2–7.3, §14; `refdoc/REFDOC_ANALYSIS.md` S30, §3 D24/C11, ERR-m23/m25; the reference text
`refdoc/refdoc.txt` (Ex C.27, pp. 101–102; App D.1 (D.1)–(D.2); Ex D.47 (D.26)–(D.33); (D.5)–(D.6), Lemma D.25, (D.17)); `research/c_glauber/DERIVATION.md` §2.4–2.5.

## 0. Method, sources, scripts

**Own scripts** (run with `python3 -I`, numpy 2.0.2, sympy 1.14, mpmath 1.3), in `verify/claims/batch_N10_s2_scripts/`, each with a `.log`:

| script | claim | method | result |
|---|---|---|---|
| `n10_prolate.py` | N10 | Lorentzian model at complex x; exact majorant test; prolate **differential operator** in the Legendre basis + eigenvalue of the finite Fourier transform read from F_c P_k = 2i^k j_k(cx) at x = 0 (no sinc-kernel quadrature); Landau–Widom plunge-slope test up to c = 1600 | 27/27 PASS |
| `n11_graph.py` | N11 | mechanical audit of the §4.5 table (grade monotonicity, [C]-input propagation) | PASS (see §3) |
| `n12_parametric.py` | N12 | **covariant Cheng–Wu/Schwinger parametrization**: every term of r = Γ − Σ_R C_RΓ is 1/(D_g X₁X₂) and lives on the same quadrant (α,β) ∈ [0,∞)²; kinematics, (b) by sympy, exact I, d = 4 remainder as one 2D integral, closed form, expansions | 24/24 PASS |
| `n12_finite_eps.py`, `n12_CH_largeeps.py`, `n12_CS_eps07.py` | N12 (a) | the four subtraction integrals at finite ε as absolutely convergent parametric integrals of the pointwise-combined integrands (no scaleless-integral convention), tail map a = y^(−1/ε), cancellation-free arithmetic | ε = 0.15, 0.3, 0.45: all ≤ 1e-12; ε = 0.7 limited to 1e-10 by the 2D rule; C_S to 1e-31 at ε ≤ 0.9 with endpoint maps (§4) |
| `n15_angular.py` | N15 | exact 4D angular average + 40–70-digit radial integration; cross-check with the Feynman-parameter form; region poset of the two-loop vertex | 20/20 PASS |
| `n16_collins.py`, `n16_sameside.py` | N16 | own residue derivation of C07 eq. (10) from its first line; same-side structure of eq. (11); F, G by Hankel (K₀) transforms and by an angular-integrated k-space convolution; Bessel-free Parseval identity; Cauchy–Schwarz scan | 29/29 + 6/6 PASS |
| `n17_colour.py` | N17 | explicit SU(N) generators from a **random** orthonormal basis (Gram–Schmidt), explicit colour-singlet hadrons, antitriplet spectator vertex −t^{aT}, same-side and opposite-side, U(1) control | 26/26 PASS |

**Literature, downloaded independently** (arXiv e-print sources, each into its own scratch directory, read as text; where equation numbers matter the
source was compiled with `latex -no-shell-escape` in a scratch build directory and the numbers read from the `.aux` file):
Collins arXiv:0708.4410v1 (eq:I1 = **(10)**, eq:I2 = **(11)**, p. 7); Rogers–Mulders arXiv:1001.2977 (eq:I1/I2 = **(27)/(28)**, eq:loopzero = (33),
eq:colorfact = **(34)**, eq:same/opp = (35)/(36)); J. Zhou arXiv:2610.11258 (eq:ratio = **(1)**); Ji arXiv:2408.03378; Ji–Liu–Su arXiv:2601.12189;
JZZ arXiv:1706.08962; IMQY arXiv:1707.03107; GJS arXiv:1707.07152; IJJSZ arXiv:1801.03917; Radyushkin arXiv:1705.01488; Usyukina–Davydychev
hep-ph/9307327; Monahan–Neumann arXiv:2609.40205; Chen et al. arXiv:2505.14619; Dutrieux et al. arXiv:2504.17706, 2506.24037; Xiong et al. arXiv:2506.16689.
The INSPIRE API was used for all bibliographic data (all journal data in the claims agree: NPB 1007 (2024) 116670; PRL 120 (2018) 112001;
PRD 96 (2017) 094019; PRL 121 (2018) 022004; PRD 98 (2018) 056004; PRD 81 (2010) 094006; PLB 298 (1993) 363–370) and for full-text searches.

**Project scripts named in the recipes**, re-run from copies (`batch_N10_s2_scripts/rerun/`, wrapper adds the site-packages path):
`s5_lemmas.py` 12/12 PASS, `s7_fourier.py` 14/14 PASS, `triangle_remainder.py` ALL CHECKS PASS, `check_remainder_d4.py` gives int remainder (d=4) = −0.0173434339581,
`tmd_breaking_abelian.py` 31/31 PASS, `colour_factors.py` 32/32 PASS. `check1.py` (R5) **crashes** with the installed SciPy ("Infinity inputs cannot be
used with break points"). It uses the same angular-average formula as my `n15_angular.py`, in double precision. My verdicts rest on my own scripts.

## 1. Summary

| id | verdict | what must change before printing | already in the literature? |
|---|---|---|---|
| N10 | **confirmed** | Present Lemma 7.2 and Prop. 7.4 as classical harmonic analysis applied to LaMET, and cite Monahan–Neumann 2026 for this application. "About 2λ_L/π recoverable modes" is an interpretation: the precise facts are trace = 2λ_L/π and #{eig > ½} = 3, 6, 10, 16. Say that the Prop. 7.3 majorant grows ∝ P^z. | **Yes.** Lemma 7.2 is Paley–Wiener type; Prop. 7.4 is Slepian–Pollak / Landau–Widom. Both are applied to quasi-PDFs, with the same numbers (width m/P^z; ≈ 2ν_max/π ≈ 6 numbers at ν_max ≈ 10), in Monahan & Neumann, arXiv:2609.40205 (Sept. 2026). The qualitative analyticity is in Ji 2024 (NPB 1007, §"PDF and GPD singularities"). Not printed elsewhere: the explicit majorant of Prop. 7.3 and the counts 3, 6, 10, 16 (both elementary). |
| N11 | **confirmed with two qualifiers** | (i) "Non-perturbative content isolated in (H3)–(H5)" holds for Thm 4.3(ii) in MS-bar (and hybrid, as graded). Ratio/RI-MOM momentum-space matching needs a further non-perturbative input (node N13 [C]), so Remark 4.5.3 ("all [C] grades in §4 come from three sources") is contradicted by the table's own N13 row. (ii) N4 = [A] is a judgment and must be printed as one: IJJSZ call the QCD OPE "widely assumed", and no Zimmermann-level proof exists. | Organizational; no precedent in this form. Every attribution checked is accurate (quotes in §3). |
| N12 | **confirmed** | None. Optionally print the closed form ∫r = [4Li₂(−σ) + σ²(ln²σ + π²/3)]/(Q̃²(1−σ²)), σ = m²/Q̃². | Φ⁽¹⁾ is Usyukina–Davydychev 1993; the same function is printed in UD hep-ph/9307327. No prior statement of this Collins remainder was found. |
| N15 | **confirmed** | Print −κπ²/(2q⁴) + O(κm²q⁻⁶ln q). The next term is κ(m²/q⁶)[−2π²ln(q²/m²) + 7π²/2]. Demonstrate the F3 lesson with the one-loop comparison: a_S = 1/27 against the exact O(λ²) of N12. The two-loop "true" remainder has not been computed. | The reference's own example; elementary. |
| N16 | **confirmed** | State that the proof uses I₁ = 𝒩F(k_T)². The factor Π_j(k_T²+m_q²) in the printed second line of C07 eq. (10) is a misprint. State the result as sign(I₁(0)+I₂(0)) = −sign 𝒩 = −sign[g₂(g₂+g₁)]. | No published proof found: INSPIRE full text of the 93 citing records searched for "Cauchy-Schwarz", "Schwarz inequality", "Parseval", "I_1(0)". |
| N17 | **confirmed** (not new) | Drop "c_glauber's own". Cite RM 2010 eq. (34) for the crossed colour factor and the argument, and Zhou 2026 eq. (1) for R = 1 + 4/(N_c²−1). | **Yes**: Rogers–Mulders PRD 81 (2010) 094006, eq. (34); J. Zhou, arXiv:2610.11258 (8 Oct 2026), eq. (1). |

---

## 2. N10 — Fourier-step theorems (LAMET §7.2)

**Lemma 7.2 (proof check).** For x = x_R + i x_I, |e^{−ixλ}| = e^{x_Iλ}. The integrand of q̃(x) = ∫dλ/(2π) e^{−ixλ} h̃ is therefore bounded by
A(1+|λ|)^k e^{(|x_I| − m/P^z)|λ|}, which is integrable uniformly on |x_I| ≤ m/P^z − ε. So q̃ is holomorphic there: either by Morera + Fubini, or by
differentiating under the integral sign with dominated convergence. The proof is correct.
The width is sharp. For h̃ = A e^{−m|λ|/P}e^{ix₀λ} the transform is the Lorentzian (A/π)w/(w² + (x−x₀)²), w = m/P, with poles at x₀ ± iw.
My numerical transform equals it at x = 0.1, 0.7+0.05i and −0.4−0.225i to ≤ 1e-21. The partial integrals diverge for |Im x| = 1.2w, and |q̃| grows like 1/δ at
x₀ + iw(1−δ). The (1+|λ|)² prefactor leaves the strip unchanged.

**Prop. 7.3.** For real x, |∫_{|λ|>λ_L}dλ/(2π) e^{−ixλ}h̃| ≤ 2∫_{λ_L}^∞ A e^{−mλ/P^z}dλ/(2π) = (AP^z/(πm))e^{−mz_L}. This is correct. The bound is **attained** at
x = 0 for a positive tail (numerically to 1e-15), so as a majorant it cannot be improved. It grows linearly in P^z.
With ħc = 0.1973269804 GeV fm: e^{−0.5·1/ħc} = **0.0793517** and e^{−0.5·1.5/ħc} = **0.0223529**, i.e. 0.079 and 0.022 as claimed.

**Prop. 7.4 (new method).** The prolate operator L_c = −(d/dx)(1−x²)(d/dx) + c²x² commutes with the time–frequency-limiting operator K. I diagonalized
it exactly in the normalized Legendre basis (pentadiagonal; even and odd blocks). For each prolate ψ_n = Σβ_k P̄_k, the eigenvalue μ_n of
F_c f = ∫₋₁¹e^{icxt}f(t)dt follows from F_cP_k = 2i^k j_k(cx) at x = 0: μ_n = √2β₀/ψ_n(0) for even n, and the analogue with ψ_n′(0) for odd n.
Then λ_n = (c/2π)|μ_n|². No quadrature of the sinc kernel is involved.

| λ_L = c | λ_n around the plunge | #{eig > ½} | 2c/π | Σλ_n |
|---|---|---|---|---|
| 5 | λ₁…λ₄ = 0.9799, 0.7999, 0.3436, 0.0560 | **3** | 3.183 | 3.1830988618 (= 2c/π to 1e-13) |
| 10 | λ₄…λ₇ = 0.9745, 0.8251, 0.4402, 0.1123 | **6** | 6.366 | 6.3661977237 |
| 15 | λ₈…λ₁₁ = 0.8537, 0.5190, 0.1692, 0.0302 | **10** | 9.549 | 9.5492965855 |
| 25 | λ₁₄…λ₁₇ = 0.9021, 0.6513, 0.2917, 0.0755 | **16** | 15.915 | 15.9154943092 |

Further checks:
* Sanity check against a sinc-kernel Gauss–Legendre Nyström matrix (c = 10, n < 14): agreement to 1.8e-14.
* Classical values: λ₀(c=1) = 0.5725817806 and λ₀(c=4) = 0.9958854904 (Slepian–Pollak: 0.5726, 0.99589).
* Landau–Widom coefficient 1/π². In the plunge region, ln(1/λ_n − 1) is linear in n. Its slope times ln(κc)/π² rises toward 1 from below for κ = 1
  (0.628 → 0.792 for c = 25…1600) and falls toward 1 from above for κ = 4π (1.122 → 1.064). This is consistent with N(α) = 2c/π + π⁻²ln((1−α)/α)ln c + o(ln c).
* The integer counts N(α) − 2c/π for α = 1e-2, 1e-4, 1e-8 are also consistent, within integer noise.

The claim's numbers are right. "Recoverable modes" is the standard interpretation of the eigenvalues near 1, not a theorem.

**Literature.**
* Ji 2024 (arXiv:2408.03378 = NPB 1007 (2024) 116670, §"PDF and GPD singularities"): "momentum distribution f̃(y,P^z) is analytic in whole range of y
  at finite P^z including y=1 … Since the correlation function in coordinate space z has finite support (decays exponentially at large z) due to
  confinement, the momentum distribution is analytical at both y=0 or y=1". LAMET's attribution "makes precise the statement of [Ji:2024oka]" is
  accurate. (CLAIMS.md's "Ji–Liu–Su" is wrong. Ji–Liu–Su 2026, arXiv:2601.12189, give the decay and an oscillation-aware FT error, |h̃(z_L)|/(π|y|) at
  large P^z, but no strip statement.)
* **Monahan & Neumann, arXiv:2609.40205** (Sept. 2026), §"Matching" → "The region |x|>1" (found here; not in stage 1). They write: "the number of independent numbers the data
  can determine on [−1,1], about 2/Δx = 2ν_max/π [Slepian:1961, Landau:1980] … typical values z_max ≈ 1 fm and P^z ≈ 2 GeV give ν_max ≈ 10 and about six
  numbers". They also write: "Such a decay [e^{−mz} = e^{−mν/P^z}] means … continued to complex x, it has no singularities within a distance m/P^z of the real axis
  [Paley:1934]", and "higher precision of the data adds resolved numbers only logarithmically [Landau:1980]". This is Lemma 7.2 and Prop. 7.4 in substance.
* Xiong et al., EPJC 85 (2025) 1409: "exponentially decaying correlators correspond to analytic momentum distributions" (qualitative).
* Classical: Paley–Wiener, AMS Colloq. Publ. 19 (1934); Slepian–Pollak, Bell Syst. Tech. J. 40 (1961) 43; Landau–Widom, J. Math. Anal. Appl. 77 (1980) 469.
* INSPIRE full-text searches (prolate/Slepian/Paley–Wiener/Landau–Widom with Ioffe time / quasi-PDF / parton) return only Monahan–Neumann.

**Verdict N10: confirmed**, with the literature as stated. It is not a new result in substance. Only the explicit majorant of Prop. 7.3 and the exact counts
3, 6, 10, 16 are not printed elsewhere, and both are elementary.

## 3. N11 — Lean-style dependency graph (LAMET §4.5)

**Mechanical audit** (`n11_graph.py`). Rule: grade(node) ≤ min(grades of parents, grade of the implication), with [R] > [A] > [P] > [C].
* All 14 rows are consistent. N11 = Lemma 5.2 is "[R] (cond.)", i.e. conditional on (H4).
* The [C] inputs of N12 = Thm 4.3(ii) are exactly {(H3), (H4) non-perturbative part, (H5)}.
* N13 for the ratio/RI-MOM schemes needs a further [C] input: perturbativity of Z′_X at large z, i.e. the hadronic zero-momentum matrix element or the
  RI/MOM vertex at all z. That input lies outside (H3)–(H5).
* Hence Remark 4.5.3 ("All [C] grades in §4 come from three sources") must be restricted to the MS-bar (and hybrid) formulation.

**Attributions (read in the arXiv sources).**
* **N1 [A].** JZZ (1706.08962): "In analogy to heavy-quark effective theory (HQET), we argue that this theory is renormalizable to all orders in
  perturbation theory". Also: "the above arguments are valid independent of whether the heavy quark field in the HQET Lagrangian is defined by a timelike or
  spacelike vector", with the BRST proof taken from Bagan et al. 1993 (HQET). So "BRST argument as for HQET, asserted for space-like n" is accurate.
  JZZ's conclusion says "we have shown"; the body says "argue".
* **N3 [A].**
  * IMQY (1707.03107): "we prove … that quasi-PDFs in coordinate-space can be multiplicatively renormalized". They add the caveats "We only concentrated on
    overall divergences but not on subdivergences, because subdivergences can be taken care by forest subtraction" and "The change of divergence
    indexes discussed here are only for superficial divergence".
  * GJS (1707.07152) use the auxiliary field on the lattice, citing Craigie–Dorn and Dorn 1986.
  * Two independent sketched all-order arguments justify [A].
* **N4 [A], no Zimmermann-level proof.** IJJSZ (1801.03917): "the OPE has been proven for scalar field theory to all orders in perturbation theory
  [Brandt; Wilson–Zimmermann; Zimmermann], and is widely assumed to hold for any renormalizable quantum field theory including QCD. By introducing
  auxiliary fields in place of the Wilson line [Dorn 1986], the correlator … is known to be equivalent to a product of local renormalizable operators of
  this type."
  By the monograph's own taxonomy ([C] = "widely used but not proven"), [A] is a judgment. It is defensible through Remark 4.5.1: the reduction to local
  operators of the auxiliary theory is standard, the gaps (anisotropic power counting, det(in·D)) are technical, and the 2–3-loop checks agree.
  The printed text must say that it is a judgment.
* **N5 [R] in PT.**
  * IJJSZ: "For arbitrary finite z, the pseudo-PDF only has support in −1 ≤ x ≤ 1 [Radyushkin 1983, 2016]".
  * Radyushkin 2017 (1705.01488): "It can be shown … that, for all contributing Feynman diagrams, [it] has the −1 ≤ x ≤ 1 support".
  * Radyushkin 1983 (PLB 131, 179) is not on arXiv and was not read.

**Verdict N11: confirmed, with the two qualifiers above.** The result is organizational.

## 4. N12 — exact Collins remainder of the off-shell triangle

Setting: the reference's (D.1)–(D.2) and (D.26), read in `refdoc.txt`:
* denominators D_g = −k², D₁ = m² + 2Pk⁻ − (m²/P)k⁺ − k², D₂ = m² + 2P′k⁺ − (m²/P′)k⁻ − k²;
* e_i, h_i, t_i as in (D.2);
* C_S = 1/(D_g e₁e₂), C_{C1} = (1/(D_g h₂))(1/D₁ − 1/e₁), C_{C2} likewise, C_H = (1/D_g)(1/t₁ − 1/h₁)(1/t₂ − 1/h₂);
* measure μ^{2ε}d^dk/(iπ^{d/2}).

**Kinematics** (sympy): p₁² = p₂² = −m² and Q² = −(p₁+p₂)² = (Q̃²+m²)²/Q̃². D₁ and D₂ follow from −(p₁−k)² and −(p₂+k)².

**Method (different from stage 1's k⁻ residues).** Write every term as 1/(D_g X₁X₂), with X₁ ∈ {D₁, e₁, t₁, h₁} and X₂ ∈ {D₂, e₂, t₂, h₂}.
* Parametrize with 1/(D_gX₁X₂) = 2∫₀^∞dα dβ (D_g + αX₁ + βX₂)⁻³. This gives −c k² + 2v·k + K.
* After the covariant shift, each term is μ^{2ε}Γ(1+ε)∫dα dβ c^{−1+2ε}N^{−1−ε}, with N = 2v⁺v⁻ + cK.
* sympy table: Γ: c = 1+α+β, N = αβQ² + (α+β)m²; C_S: c = 1, N = αβQ̃² + (α+β)m²; (D₁,h₂): c = 1+α, N = α(βQ̃² + m²); (e₁,h₂): c = 1, same N;
  (t₁,t₂): c = 1+α+β, N = αβQ̃²; (h₁,t₂), (t₁,h₂), (h₁,h₂): c = 1+β, 1+α, 1, N = αβQ̃².
* All terms live on the same quadrant, so the combined integrands are pointwise sums.

**(a) Analytic.**
* C_S: ∫∫(αβQ̃² + (α+β)m²)^{−1−ε} = Q̃⁻²(Q̃²/m⁴)^εΓ(ε)Γ(1−ε)/ε, giving **Q̃⁻²(μ²Q̃²/m⁴)^ε𝓑**.
* C_{C1}: the integrand factorizes. ∫dβ(βQ̃²+m²)^{−1−ε} = m^{−2ε}/(εQ̃²), and ∫dα α^{−1−ε}[(1+α)^{−1+2ε} − 1] = B(−ε,1−ε), absolutely convergent for 0<ε<1.
  This gives **−Q̃⁻²(μ²/m²)^ε𝒜**.
* C_H: (αβ)^{−1−ε}[(1+α+β)^{−1+2ε} − (1+α)^{−1+2ε} − (1+β)^{−1+2ε} + 1], absolutely convergent, with value Γ(−ε)²/Γ(1−2ε). This gives **Q̃⁻²(μ²/Q̃²)^ε𝒜**.

**(a) Numerical**, with no scaleless-integral convention: direct 2D quadrature of the combined integrands, with a tail map and cancellation-free
expm1/log1p brackets (`n12_finite_eps.log`, `n12_CH_largeeps.log`, `n12_CS_eps07.log`).
* All four terms agree with the closed forms to ≤ 1e-12 at ε = 0.15, 0.3 and 0.45 (P, P′, m² = 0.8, 1.3, 0.02); C_{C2} = C_{C1}.
* C_H at ε = 0.45 agrees to 4e-25 (40 digits).
* At ε = 0.7, C_{C1} and C_H agree to ≤ 7e-11 and C_S to 2e-10. This is the limit of the 2D tensor-product rule there, caused by the a^{−ε} endpoint and a
  boundary layer in the tail.
* With endpoint-regularizing maps, C_S agrees to 1e-31 at ε = 0.45, 0.7 and 0.9.
* At the second point (2.0, 0.35, 0.3), ε = 0.25, the sum agrees to 1e-12.

**(b)** sympy: the ε⁻² and ε⁻¹ coefficients vanish, and the finite part is (ℓ_Q − ℓ_m)² + π²/3 = **ln²(Q̃²/m²) + π²/3**.

**(c) Remainder.**
* My Feynman-parameter derivation gives Q²I = ∫₀¹du ln(u(1−u)/t)/(u(1−u) − t). It equals the UD Φ⁽¹⁾(t,t) to < 1e-25.
* The Γ density on the quadrant integrates to I = 11.934692603409 (1e-12).
* The **d = 4 remainder as a single parametric integral** ∫∫ρ(α,β) = **−0.01734343395808**, against I − (D.32) = −0.01734343395809 (Δ = 2e-15). ρ·αβ → 0 at every corner, so ρ is integrable.
* Closed form: with σ = m²/Q̃², √(1−4t) = (1−σ)/(1+σ) and ρ_UD t = σ, we get ∫r = [4Li₂(−σ) + σ²(ln²σ + π²/3)]/(Q̃²(1−σ²)) (agreement to 1e-22).
* sympy expansion:
  * Q²I = L² + π²/3 + t(2L² − 4L − 4 + 2π²/3) + t²(6L² − 14L − 11 + 2π²) + …
  * Q²∫r = **−4t + t²(L² − 15 + π²/3)** + t³(6L² − 4L − 490/9 + 2π²) + …, with no logarithm at NLP.
  * The numerical residual at t = 1e-5 over t³L² is 5.39, approaching 6.
* Value: **−0.0173434339581** at m² = 0.02, P = 0.8, P′ = 1.3 (also reproduced by the re-run `check_remainder_d4.py`).

**Literature.**
* UD's Φ⁽¹⁾ formula, (iπ²/p₃²)Φ⁽¹⁾, Φ⁽¹⁾ = λ⁻¹{2(Li₂(−ρx)+Li₂(−ρy)) + ln(ρx)ln(ρy) + ln(y/x)ln((1+ρy)/(1+ρx)) + π²/3}, is read in
  UD hep-ph/9307327 (Phys. At. Nucl. 56 (1993) 1553), which cites UD PLB 298 (1993) 363. PLB 298 is not on arXiv (INSPIRE abstract: "Exact results for
  diagrams up to the two-loop level are obtained in terms of polylogarithms"). The formula is in any case verified numerically.
* Collins 2011 ch. 10 is "Factorization and subtractions" (§10.3 Sudakov form factor, §10.4 region approximator, §10.5 one-loop Sudakov form factor;
  Cambridge front matter).
* INSPIRE full-text searches for this remainder found nothing.

**Verdict N12: confirmed.**

## 5. N15 — reference Ex C.27 sharpened; F3 lesson

**Ex C.27** (read in `refdoc.txt`, p. 102): "κ∫d⁴k[Δ(q−k) − Δ(q)]Δ(k)³ = O(q⁻⁴ln q²)", with Euclidean Δ = 1/(k²+m²) and ∫d⁴kΔ³ = π²/(2m²).

**Method.**
* The exact 4D angular average ⟨Δ(q−k)⟩_{S³} = 2/(A + √(A² − 4q²k²)), A = q²+k²+m², is checked against direct S³ quadrature to 1e-30.
* The radial integral is done in cancellation-free form, at 40 digits (70 digits for the NLP).
* Cross-checked against the Feynman-parameter form at q = 0.7, 3, 10 to 1e-25.
* Mean-value property ⟨1/(q−k)²⟩ = 1/max(q²,k²), i.e. 1/x² harmonic in R⁴: checked to 1e-25.
* Analytically, the region k > q gives π²∫_{q²}^∞du(u⁻³ − q⁻²u⁻²) = −π²/(2q⁴), m-independent and without log.
* The region k ~ m gives ⟨Δ(q−k)⟩ − Δ(q) ≈ −um²/q⁶, i.e. O(m²q⁻⁶ln q).

**Results.**
* q⁴I = −5.46482 (q/m = 10), −4.94952 (100), −4.9350404 (10³), −4.93480549 (10⁴), −4.934802201 (10⁶) → −π²/2 = −4.934802201.
* The same limit holds for m = 0.5 and 2.
* q⁶[I + π²/(2q⁴)]/m² = −2π²ln(q²/m²) + 34.5436154 (7π²/2 = 34.5436154). The slope is −19.73920886, against −2π² = −19.73920880.
* |q⁴I| decreases to π²/2, so there is no ln q at leading power. The reference's bound is true but not sharp.

**F3** (reference rule after (D.6): β_R = 3^{h(R)−h*}, h* = 1 + max_{R≠R_max}h(R); (D.17): a_R = β_R/3).
* Line modes of the 9 regions of Fig. 63 (k₁ inner, k₂ outer; lines k₁, k₂, p₁−k₂, p₁−k₂−k₁, p₂+k₂, p₂+k₂+k₁) with the order S < C_i < H give
  12 covering relations.
* They reproduce the reference's meets (C₁,C₁)∧(H,S) = (C₁,S), (H,C₁)∧(H,C₂) = (H,S), (C₁,C₁)∧(C₂,C₂) = (S,S).
* h(S,S) = 0 and h* = 4, so β_(S,S) = 1/81 and **a = 1/243**.
* One loop: β_S = 1/9 and β_C = 1/3 (as in the reference), so a_S = 1/27.
* The exact one-loop remainder (N12) is O(λ²) (relative O(λ²/L²)). This demonstrates "far from sharp" at one loop. No two-loop remainder has been computed, so the
  two-loop comparison in CLAIMS.md ("against the true O(λ²L²)") is an expectation, not a result.

**Verdict N15: confirmed.**

## 6. N16 — Cauchy–Schwarz proof of I₁(0)+I₂(0) < 0 (Collins 2007)

**Source.** C07 eq. (10) (= eq:I1), second line: λ²g₁²g₂(g₂+g₁)x(1−x)/(256π⁷)∫d²l₁d²l₂ **Π_j (k_T²+m_q²)**/((l_j²+m_g²)[(k_T−l_j)²+m_q²]).
Eq. (11): I₂ = −[same]∫1/((l₁²+m_g²)(l₂²+m_g²)[(k−l₁−l₂)²+m_q²](k_T²+m_q²)). Collins writes: "with a certain amount of effort, it can be proved
analytically that I₁(0)+I₂(0) < 0". No proof is given.

**Own derivation from the first line of (10).**
* At l^+ = 0 and M = 0, the l⁻ integral of [(k−l)²−m_q²+i0]⁻¹[(p−k+l)²−m_q²+i0]⁻¹ = **2πi/(2p⁺A_j)**, A_j = (k_T−l_jT)²+m_q², independent of k⁻.
  This holds by residues (sympy) and by quadrature at ε = 1e-6. The conjugate side gives the complex conjugate.
* Assembling the constants (sympy): xp⁺·[2(1−x)p⁺]²·(2π)²·2π/(2(1−x)p⁺)·(2π)²/(4p⁺²)/(2π)¹² = x(1−x)/(256π⁷), so 𝒩 = λ²g₁²g₂(g₂+g₁)x(1−x)/(256π⁷).
  No factor (k_T²+m_q²) arises: **I₁ = 𝒩F(k_T)²**.
* Dimensions: the first line has M⁻², while the printed second line has M⁺².
* RM eq. (27), the massless non-abelian analogue ("the same result as in Ref. [Collins:2007jp]"), has no such factor.
* With the printed factor, k F²(k²+m_q²)² grows (1.1e4, 3.9e5, 8.3e6 at k = 10, 10², 10³), so ∫d²k I₁ would diverge. That contradicts C07's own statement.

**Same-side structure (eq. (11)), derived** (`n16_sameside.py`).
* The two spectator orderings sum to ∫du[(Pu+c₁+i0)⁻¹ + (P(v⁻−u)+c₂+i0)⁻¹] = −2πi/P, independent of c₁, c₂, v⁻ (analytic, and numerically at ε = 1e-3, 1e-5).
* The remaining v⁻ integral is the opposite-side one, 2πi/(2p⁺A_v).
* The conjugate tree propagator is k² − m_q² = −(k_T²+m_q²)/(1−x).
* Magnitudes: same side (2π)²(1−x)²/(A_v(k_T²+m_q²)), opposite side (2π)²(1−x)²/(A₁A₂). The prefactor 𝒩 is the same, and the structure is G/(k_T²+m_q²).
* The overall minus sign of (11) is then fixed by C07's stated k_T-integrated cancellation, verified below.

**F, G, Parseval, Cauchy–Schwarz** ((m_g, m_q) = (0.5, 1)).
* F: closed form = Hankel 2π∫b db J₀K₀(m_gb)K₀(m_qb) = Feynman form, to 1e-15.
* G: Hankel (2π)²∫b db J₀K₀(m_gb)²K₀(m_qb) = angular-integrated convolution 2π∫q dq F_gg(q)/√((k²+q²+m_q²)²−4k²q²), to 1e-12.
  G(0) = 54.7287077109, G(0.8) = 51.1837488651.
* Parseval: ∫d²kF² = 493.154149319128. The Bessel-free identity ∫d²k G/(k²+m_q²) = ∫d²q F_gg(q)F_qq(q) gives 493.154149319128, and the b-space value
  (2π)³∫b db K₀²K₀² is the same. At (1.7, 0.4): 302.5398199927, three ways. Hence ∫d²k_T(I₁+I₂) = 0.
* Measure: dμ = d²b/(2π)²·2πK₀(m_qb) gives ∫dμ = 1/m_q² (1e-18), F(0) = ∫dμ 2πK₀(m_gb) = π ln(m_g²/m_q²)/(m_g²−m_q²) = 5.80689624, and G(0) = ∫dμ(2πK₀)².
* Cauchy–Schwarz: F(0)² = 33.720 < G(0)/m_q² = 54.729. It is strict because K₀(m_gb) is not constant.
* Scan over m_g/m_q = 0.01 … 60 and m_q/m_g = 0.05, 0.003: always < 0, with relative gap between −0.037 (m_g/m_q = 0.01; it approaches saturation as m_g → 0) and −0.9999.
* Point values of (I₁+I₂)/𝒩: −21.008664, −17.726681, −7.1894964, −0.70082836, +0.37679619, +0.089029285 at k_T = 0, 0.3, 0.8, 1.5, 3, 6.
  These agree with the claimed −21.0, −17.7, −7.19, −0.70, +0.38, +0.089.
* Sign: I₁(0)+I₂(0) = 𝒩[F(0)² − G(0)/m_q²], so it is negative iff 𝒩 > 0, i.e. g₂(g₂+g₁) > 0. Collins's "< 0" presupposes this.

**Literature.** INSPIRE lists 93 citing records (recid 759565). Full-text searches for "Cauchy-Schwarz", "Schwarz inequality", "Parseval" and "I_1(0)" among them
return nothing. "Bessel" returns 10 unrelated TMD papers. No published proof found.

**Verdict N16: confirmed** (with the I₁ = 𝒩F² reading and the sign statement made explicit).

## 7. N17 — entanglement test

**Own computation** (`n17_colour.py`).
* Generators come from random Hermitian traceless matrices, Gram–Schmidt orthonormalized in Tr(t^at^b) = δ^{ab}/2. Completeness was checked.
* Hadrons are ψ = δ_{is}/√N, quark ⊗ antitriplet spectator, with spectator vertex −t^{aT}. The hard exchange is colour neutral (1→3 and 2→4 colour lines).
* The gluon from spectator 1 attaches to X ∈ {3, 4, 2}, the one from spectator 2 to Y ∈ {4, 3, 1}, with t^a in fermion-flow order.

Relative to tree, for N = 2, 3, 4, 5:
* Single gluon: C₁(3) = C₂(4) = −C_F; C₁(4) = C₁(2) = C₂(3) = C₂(1) = 0.
* Two gluons: C(3,4) = C_F². Each crossed attachment (X ∈ {4,2}, Y ∈ {3,1}) gives T_F²(N²−1)/N². Mixed attachments (3,3), (3,1), (4,4), (2,4) give 0.
* Σ = C_F² + 4T_F²(N²−1)/N² = C_F²[1 + 4/(N²−1)]. The factorized product is (ΣC₁)(ΣC₂) = C_F².
* SU(3): **24/9 vs 16/9** (ratio 3/2). The results are identical for gluons on the same side and on opposite sides of the cut.
* U(1): the two-gluon weights are products of single-exchange charges, so the sum equals the product.

**Premise.** The pole parts of eikonal attachments to incoming and outgoing quark lines are equal. This is checked in C07 eq. (2) and in RM eqs. (35)/(36):
the sums of the eikonal pairs are −4π²δ(l₁⁺)δ(l₂⁻) (same side) and +4π²δδ (opposite side).

**Literature (read in the sources).**
* RM eq. (34): "all graphs of the type shown in Fig. [violating] include the non-zero color factor Tr_C[t^at^b]Tr_C[t^bt^a] = T_F²(N_c²−1)". Generalized
  factorization predicts 0 for this class (eq. (33)).
* Zhou (arXiv:2610.11258, eq. (1)) obtains R = 1 + 4/(N_c²−1) from a full twist-3 calculation in the RM double-Sivers model: "crossed attachments contribute an extra term equal to
  4/(N_c²−1) times that coefficient"; uncrossed colour N_c²C_F², crossed Σ_{a,b}Tr(t^at^b)Tr(t^bt^a) = (N_c²−1)/4.
* The c_glauber test is RM's argument in attachment-sum form, and its ratio is Zhou's R.

**Verdict N17: confirmed (already in the literature).** Drop "c_glauber's own".

## 8. Items for the authors
1. LAMET §7.2–7.3 and §14 item 10:
   * Cite Monahan–Neumann arXiv:2609.40205 (§"The region |x|>1") for the strip width m/P^z and the ≈ 2ν_max/π count.
   * Mark Lemma 7.2 and Prop. 7.4 as classical (Paley–Wiener; Slepian–Pollak; Landau–Widom).
   * State that the Prop. 7.3 majorant grows ∝ P^z.
   * Correct CLAIMS.md's "Ji–Liu–Su" to "Ji 2024".
2. LAMET Remark 4.5.3: add N13 (ratio/RI-MOM, [C]) as a further non-perturbative input, and print N4 = [A] as an explicit judgment (IJJSZ: "widely assumed").
3. N12: the closed form ∫r = [4Li₂(−σ) + σ²(ln²σ + π²/3)]/(Q̃²(1−σ²)) may be printed.
4. N15: give the F3 lesson with the one-loop comparison (a_S = 1/27 vs the exact O(λ²)); do not claim a two-loop "true O(λ²L²)".
5. N16: print I₁ = 𝒩F² explicitly with a footnote on the misprint in C07 eq. (10), and give the sign as −sign[g₂(g₂+g₁)].
6. N17: replace "ours" by citations of RM eq. (34) and Zhou eq. (1).
