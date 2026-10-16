# Verification batch E13–E18 (stage 1, independent verifier)

Date: 2026-10-10. Default stance: skeptical. Claims E13–E18 of `verify/CLAIMS.md` (sources: `frontier/yzliu/YZLIU.md` §3.A3, §4.1 E6;
`frontier/others/OTHERS.md` §1.2–1.7, §4.6–4.7; `research/c_regions/DERIVATION.md` §1.3; `research/c_tmd/DERIVATION.md` §1 item 4;
`research/c_glauber/DERIVATION.md` §2.4; `spec/VERIFIED_FORMULAS.md` VF-TMD-9, VF-GLA-8).

## 0. Method and sources

* **Primary literature was downloaded independently** and read as text (untrusted data; nothing executed from it):
  * Liu, APPB 53 (2022) 4-A2, journal PDF from actaphys.uj.edu.pl (89 pp.; App. F on pp. 4-A2.79–80; page 80 also rendered as an image to check the formulas).
  * Liu, arXiv:2312.05957v6 (= JHEP 09 (2024) 030); Ji–Liu–Su arXiv:2601.12189v1; Hollands arXiv:gr-qc/0212028 (cites Streater–Wightman theorem numbers).
  * Hall & Wightman, Mat.-Fys. Medd. Dan. Vid. Selsk. 31 no. 5 (1957), scanned PDF from the Danish academy archive (original statement of the theorem behind BHW).
  * D. Ruelle, book review of Streater–Wightman, Bull. Amer. Math. Soc. 71 (1965) 130–133, doi:10.1090/S0002-9904-1965-11247-2 (scanned pages read as images). This is how I checked what Streater–Wightman ch. 2 contains: **the book itself was not accessible** (archive.org copy is lending-only).
  * Wikipedia "Edge-of-the-wedge theorem" (raw wikitext), section "Application to quantum field theory".
  * Collins arXiv:2007.04085v1, **LaTeX source** (§I, §IV "Literature review", §VIII.E "Case of one denominator", §IX, Apps. A, B.1, B.2, D.1, D.2).
  * Collins, *Foundations of Perturbative QCD*, ch. 5, open-access reissue (Cambridge 2023, doi:10.1017/9781009401845; chapter PDF pp. 87–160); §5.4.3 on p. 110.
  * Banfi–Forshaw–Holguin arXiv:2511.11799v1 source (the only arXiv version; APS abstract identical); Alioli et al. arXiv:2312.06496v1 source (only version);
    Becher–Hager–Neubert–Schwienbacher arXiv:2603.12383v1 source (= PRL 137 (2026) 121902).
  * Aybat–Rogers arXiv:1101.5057v1 and v2 sources and the v2 PDF (equation numbers checked in the PDF); Collins–Rogers arXiv:1210.2100v2 (source and PDF);
    Aybat–Collins–Qiu–Rogers arXiv:1110.6428v3 (source "as-published" and PDF).
  * Collins arXiv:0708.4410v1 source and PDF (page 7 rendered as an image).
* **Not accessible:** Coleman–Norton, Nuovo Cim. 38 (1965) 438 (Springer paywall; only the abstract was read, via INSPIRE and Springer);
  Eden–Landshoff–Olive–Polkinghorne (ELOP) 1966 (lending-only on archive.org; Google Books rate-limited); Streater–Wightman (see above).
  Where a claim concerns those texts, I say explicitly that the check is second-hand.
* INSPIRE API: publication data, texkeys, citing papers of arXiv:2511.11799 (16 citations, read titles; the relevant one, arXiv:2603.12383, read in full).
* **My own scripts**, copied to `verify/claims/batch_E13_s1_scripts/` (run with `python3 -I`): `e14_check.py`, `e15_check.py`, `e16_colour.py`,
  `e16_integral.py`, `e17_check.py`, `e18_check.py` (output saved as `e18_check.out.txt`).
  Project scripts named in the recipes were re-run from scratch copies: `research/c_regions/landau_oneloop.py` (**23/23 PASS**, both L3f checks PASS),
  `research/c_tmd/scripts/one_loop_tmd.py` (all PASS), `research/c_glauber/scripts/tmd_breaking_abelian.py` (**31/31 PASS**, A4f PASS).

## 1. Summary

| id | verdict | what must change before printing | already in the literature? |
|---|---|---|---|
| E13 | **confirmed** | Say what the edge-of-the-wedge theorem does (gluing different operator orderings by locality). Also: APPB writes the complex Lorentz map as "Λ(t,z) → (it,iz)", which is not a Lorentz transformation. The correct map is (t,z) ↦ (iz,it), as in Liu 2024 eq. (3.25). YZLIU.md line 262 copied the wrong form. | Terminology note. No published correction found (Liu 2024 simply uses the right wording). |
| E14 | **confirmed** (diagnosis second-hand for the CN text itself) | Reword "F ≡ 0, so there is no parameter pinch". "Eikonal" → "linear denominators" (Collins' explicit example is non-relativistic). "Result true" = the *pinch* criterion and classical picture, not CN's literal "singularity iff classical process". CN's proof is fine for massive graphs apart from the zero-eigenvalue cases CN themselves excluded. | Yes: this is Collins arXiv:2007.04085 §I, §IV, App. D (unrefereed). Not a new observation of ours. |
| E15 | **confirmed** (the ELOP-text items second-hand, via Collins) | Attribute the ELOP-specific points to Collins 2020 §I/§IV. Do not quote ELOP (2.1.19b) verbatim without checking the book. (2.1.19b) is the general complex Landau condition: necessary, and correct as such, but not sufficient for physical-region pinches. Anomalous deformations exist only in ≥ 2 dimensions. The Collins 2011 statement holds "as of 2011". | Yes: Collins 2011 §5.4.3; Collins 2020 §IV, Apps. A, B. |
| E16 | **confirmed** | Remove "single group": BHNS (PRL 137 (2026) 121902) independently confirm the qg→q result. Alioli et al. are contradicted on the *super-leading* part of their sentence only; NGLs are not addressed. dσ is the cumulant in τ₁, differential in Born variables, with fixed α_s. | Yes: BFH 2026 itself, confirmed by BHNS 2026. |
| E17 | **confirmed** | Add: the same factor 2 is in their eq. (4) for ζ_D. (A10) is ζ-independent, so cite (A11),(B1). The same authors use the correct normalization in ACQR, PRD 85 (2012) 034043, eqs. (2),(3). | Implicitly corrected by the authors in ACQR 2012 and Collins–Rogers 2013; no explicit erratum. |
| E18 | **confirmed** | None for the main point. Optional: the first line of the same equation also lacks two squares, and puts +iε instead of −iε on the conjugate side of the cut; read literally, that flips the overall sign. | Not recorded anywhere (unpublished preprint, v1 only). |

---

## 2. E13 — APPB App. F: "edge of the wedge" should be Bargmann–Hall–Wightman

**Published text (Liu, APPB 53 (2022) 4-A2, App. F, p. 4-A2.80, checked on the rendered page):**
> "Then both Wightman functions are in their analytic region, and all arguments relate with each other through the complex Lorentz transform Λ(t, z) → (it, iz)) since Λ(−iv, −iv′) = (n, n′). Then one needs to use the “edge of the wedge” theorem. This theorem states that the Wightman functions in their analytic region called the “extend tube” transform under complex Lorentz transform in a covariant way. In fact, the extended tube is constructed exactly through complex-Lorentz transforms from the tubes. Given the theorem, we have [(F.6)] … Note that the theorems mentioned above only rely on the tempered nature of the Wightman functions, causality (for the “edge of the wedge” theorem), and support property, but do not require any positivity …"

**What the two theorems state (read, not recalled):**
* Hall & Wightman 1957, Theorem I and its outline (Lemma 1): if f is analytic in the tube (Im z_j in the future cone) and invariant under the orthochronous Lorentz group, "then (Lemma 1) it also satisfies (1) when Λ is an arbitrary complex Lorentz transformation … if Λz₁,…,Λz_n lies outside the future tube, (1) defines a single valued analytic continuation of the function f originally given. We shall refer to the set of points Λz₁,…,Λz_n, for Λ ∈ Ω, and z₁,…,z_n in the tube, as the extended tube." The authors also stress that the results "are valid in both local and non-local field theory", so no causality is needed.
* Ruelle's 1965 review of Streater–Wightman, describing ch. 2 ("some mathematical tools"): "One is a theorem (Bargmann, Hall, and Wightman) asserting that if a function is analytic in a certain tube (the 'forward' tube) of C^{4n} and transforms covariantly under the Lorentz group, it is the restriction of a function analytic in a larger domain of C^{4n} (the 'extended' tube) and covariant under the complex Lorentz group. Another specific tool is the 'edge of the wedge' theorem. This is a nontrivial generalization to several variables of Painlevé's theorem on couples of analytic functions having the same boundary values on the real axis."
* Hollands (gr-qc/0212028), Lemma 5.2: continuation to the extended tube under the one-parameter group of complex (t,z) boosts, "compare [Streater–Wightman, thm. 2.11]". Separately, the "edge-of-the-wedge theorem (see e.g. [Streater–Wightman, thm. 2.17])" is used for vanishing boundary values. The theorem numbers are Hollands' citations; I could not check them in the book.
* Wikipedia, edge-of-the-wedge theorem, QFT section: the permuted Wightman functions are glued by the edge-of-the-wedge theorem "(with the edge given by the set of totally spacelike points) … The equality of the boundary values on the edge … follows from the locality axiom".

**Conclusion.** The property invoked in App. F — continuation to the extended tube and covariance under proper complex Lorentz transformations — is precisely the BHW theorem. It needs only the spectral condition (tube analyticity) and real Lorentz covariance, and no locality. For the longitudinal-boost invariance assumed in App. F, the elementary one-parameter version suffices (Hollands Lemma 5.2).

The edge-of-the-wedge theorem plus locality is what makes the analytic functions of different operator orderings one function on the permuted extended tube. App. F needs that step implicitly ("This is possible since W_DY is insensitive to time-ordering"), which explains the mention of "causality". So the misattribution is terminological, and the derivation of (F.6) stands.

**Liu 2024 (arXiv:2312.05957v6 = JHEP 09 (2024) 030), §2.1:**
> "the analytic Wightman functions are covariant under proper complex Lorentz transforms (complex-valued Lorentz transforms with determinants equal to 1) … One can show that for any permutation P, the analytic Wightman function W_P obtained this way is still single-valued … without using the local commutativity, one obtains n! analytic functions W_P … given the local commutativity, all these n! analytic functions can be combined together as a single analytic function."

This is correct, names neither theorem, and does not misattribute. The word "wedge" does not occur in Liu 2024.

**Ji–Liu–Su 2026 (arXiv:2601.12189v1) §5.1:** "Because of locality … the two functions have identical boundary values on this edge, which means G_>(w,z⃗) and G_<(w,z⃗) can be combined into a single analytic function based on the Edge-of-the-wedge theorem." This is the correct use, so the full-statement reference in CLAIMS.md is accurate.

**Additional finding (affects our files).** APPB writes the map as "Λ(t,z) → (it, iz)". Read literally, this sends t²−z² to −(t²−z²), so it is not a Lorentz map. The map with the stated property Λ(−iv) = n is (t,z) ↦ (iz, it):
* matrix [[0,i],[i,0]], with Λᵀ diag(1,−1) Λ = diag(1,−1) and det = 1 (checked);
* a boost with rapidity iπ/2;
* written exactly this way in Liu 2024 eq. (3.25), with Λ(−iλn) = λn and Λ(−iλn̄) = −λn̄.

YZLIU.md §3.A3 (line 262) copies "Λ(t,z)=(it,iz)". Fix it before printing.

---

## 3. E14 — Coleman–Norton 1965: momentum-space vs parameter-space pinch

**Collins 2020 (arXiv:2007.04085v1, source) states the diagnosis verbatim:**
* §I: "They apply a Feynman parameter representation and then perform the momentum integrals. Their proof is applied to the integral over Feynman parameters, with its single denominator. There is an unstated assumption that there is a pinch in the original momentum-space integral if and only if there is a pinch in the parameter integral. But in the massless case that implication simply fails, and it fails in the simplest graph, a one-loop self energy."
* Footnote 4 (on the classical-process derivation): "In a theory with no massless particles, this part of the proof is correct."
* §IV: "The authors then state that it is easy to show that the contour is trapped, but only if none of eigenvalues of E_ij is zero … The proof does indeed fail when zero eigenvalues exist. It is not at all clear whether the failure can be remedied … That cases of zero eigenvalues arise in massive theories in reality is mentioned; they occur only at 'very exceptional points' … [Eden 1961] appears not to contain a clear statement of whether such singularities can occur in the physical region." And: "It is important to remember that it is not the result that breaks down, but the proof."
* §IX item 2: "Coleman and Norton's proof works in the massive case, but it becomes singular in the massless case".

**CN 1965 itself** (abstract only): "a Feynman amplitude has singularities on the physical boundary if and only if the relevant Feynman diagram can be interpreted as a picture of an energy- and momentum-conserving process … As a by-product of the proof, the Feynman parameter associated with an internal line is identified (within a proportionality factor) with the time the particle exists between collisions, divided by its mass." So the proof is parametric and its interpretation presupposes massive lines. The tacit-assumption diagnosis is Collins'; I could not read the CN text.

**Independent computations (`e14_check.py`):**
1. Massless bubble, Symanzik polynomials: U = α₁+α₂ and **F = −p²α₁α₂**. The Hessian of F in α is [[0,−p²],[−p²,0]], identically 0 at p² = 0 (all eigenvalues zero). The parametric Landau equations α_j∂F/∂α_j = −p²α₁α₂ = 0 give only the corners for p² ≠ 0 and hold *identically* at p² = 0.
2. Momentum-space Landau equations: λ₁k − λ₂(p−k) = 0 gives k = λ₂p/(λ₁+λ₂), with k² ∝ p² and (p−k)² ∝ p². So both lines are on shell only if p² = 0, and then k = xp with x ∈ [0,1] for λ ≥ 0: the collinear pinch line.
3. Mixed momentum-parameter form: the denominator at k = αp equals αp²(1−α), so interior solutions exist only at p² = 0 (Collins D.1 reproduced).
4. Pure-parameter form: Π = iΓ(ε)(−p²−i0)^{−ε}(4π)^{ε−2}·B(1−ε,1−ε). The α-integral is a p-independent constant (numerically 1.516964 = B(0.8,0.8) at ε = 0.2). The singularity at p² = 0 sits entirely in the prefactor, and no α-contour is ever pinched.
5. Collins App. D.2 (non-relativistic analogue):
   * ∫dω[(1−2α)ω+b]^{−2} = 0 exactly for α ≠ ½ (checked at α = 1/5, 2/5, 9/20);
   * ∫₀¹dα first, then ∫dω, gives −iπ/b, which reproduces Collins' coefficient −4iπm/(2Em−2k²+2pk−p²) δ(α−½);
   * the direct ω-integral equals −2πi/(E−A−B) numerically;
   * the momentum-space pinch is at k = p/2, E = p²/(4m).
   The same mechanism holds for any pair of denominators linear in the same component with opposite signs, e.g. an eikonal pair 1/(l⁺+i0)·1/(−l⁺+i0).
6. Re-run of `research/c_regions/landau_oneloop.py`: 23/23 PASS. L3f: "only the two corners" for p² ≠ 0, and "F vanishes identically (every point is a solution)" at p² = 0.

**Precision issues in the claim as worded:**
* (a) "F ≡ 0, so there is no parameter pinch" is a non sequitur. F ≡ 0 means the parametric Landau equations are satisfied *everywhere* (and the CN quadratic form is totally degenerate), not that they fail. The correct statement: F = p²·(−α₁α₂) with a p-independent α-dependence, so the α-contour is never pinched and the collinear singularity resides in the prefactor (−p²)^{−ε}. At p² = 0 the parametric representation degenerates (Collins: "there is no pinch correspond[ing] to the collinear singularity. Instead the singularity of the integral at p²=0 is in the prefactor only").
* (b) Collins' explicit example for linear denominators is non-relativistic. He says the same applies to Wilson lines, and the mechanism is the same (item 5).
* (c) "Result true" must mean: physical-region **pinch** ⟺ Landau point with λ_j ≥ 0 ⟺ classical process (Collins Thm. 1, hypotheses (a),(b); [R]† since unrefereed). CN's literal "singularity iff classical process" is *not* an "iff" in massless theories. Collins App. D.1: the massless bubble is pinched at k = 0 and k = p for every p, yet Π is non-singular for p² ≠ 0.
* (d) For massive graphs the CN proof is accepted by Collins, except at zero-eigenvalue points. CN themselves exclude those as "very exceptional", and Collins (§VIII.E) notes an "obscure reference" to them on CN p. 441. So "proof [V]" applies to the massless extension that pQCD actually uses. The massive case has an acknowledged, unresolved exceptional set.

---

## 4. E15 — ELOP §2.1 and textbook Landau-analysis errors

**Read directly:**
* Collins 2011 (OA reissue) §5.4.3, p. 110: "A devil's advocate would search for a proof in the literature that the Landau equations are both necessary and sufficient for a PSS, and would be rewarded by not finding a published explicit and complete proof. Textbook treatments, when examined closely, are incomplete. For example, in … Eden et al. (1966), we read (p. 48): 'A proper proof needs the use of topology; … We shall be content with plausibility arguments.' The reference given for a real proof is an unpublished paper, by Fotiadi, Froissart, Lascoux, and Pham …"
* Collins 2020 §I repeats the ELOP p. 48 quote ("proper proof needs the use of topology", "be content with plausibility arguments").
* Collins 2020 §IV (ELOP paragraph) makes four points:
  * the contour should be distorted "in the direction of the normal" — "an unambiguous 'normal' to a surface only makes sense in a Euclidean space", whereas the allowed directions form a half-space;
  * ELOP "appear to assume as so obvious as not to need a proof that for a contour deformation to avoid a singularity surface it must give a nonzero first order shift … But this definitely not the case";
  * "(2.1.19b) … lacks the positivity constraint needed for the kind of 'physical region' pinch we consider … their version of the condition is trivially satisfied whenever the number of singularity surfaces is larger than the dimension of the integration space, as the authors do indeed observe";
  * "The positivity conditions do appear in the ELOP treatment for physical region pinches/singularities, but only when they consider Feynman graphs in a Feynman parametric representation."

**Reproduced (`e15_check.py`):**
* Anomalous deformations for 1/(E−p²/2m+iε), with D = (1,−p/m):
  * #1, (η,ξ) = (|E_R|+2|p_R|, m): Im = λ(|E_R|+2|p_R|−p_R) ≥ 0, zero only at the origin, where Re = λ²m/2 > 0. The first-order shift vanishes at the origin.
  * #2, (η,ξ) = (p_R+p_R²/2m−E_R, m): on Re = 0, Im = λ³m/2 > 0 exactly (sympy). The first-order shift vanishes on the *whole* singular surface (numerically 0 at 9 sample points).
  * Grid scan of |E_R|,|p_R| ≤ 2 for λ = 10⁻³…1: the distance to the forbidden set stays positive for #1 and #2. The constant tangent deformation (0,m) crosses the singularity (distance 0). So the anomalous deformations need position-dependent v, exactly as Collins says.
  * Collins App. B.2 shows that in **one** dimension a strictly positive first-order shift *is* necessary. So the statement is "false in ≥ 2 dimensions".
* Trap without singularity (App. A): I(Q/m) = m²Q∫dk/[(k−m+iε)(k−iε)²(k+Q−iε)] = −2πiQ/(Q+m) (residue at k = m; numerically confirmed). The contour is trapped at k → 0 as m → 0, yet I is regular at m = 0. A genuine Feynman-graph example is App. D.1 (bubble pinched at zero-momentum lines for all p, singular only at p² = 0). So "Landau condition ⇒ singularity" is [V]; the condition is necessary only.
* Minor: Collins 2020 eq. (den) prints "iλ(η−ξp_Rm)" for iλ(η−ξp_R/m). The subsequent formulas use the correct form.

**Caveat.** ELOP pp. 47–48 and eq. (2.1.19) could not be inspected. The p. 48 disclaimer is quoted identically in two Collins texts, so I accept it. The "normal", first-order-shift and (2.1.19b) points are Collins' reading.

Collins' remark that ELOP observe their condition to be trivially satisfied with more surfaces than dimensions only makes sense for a sign-unconstrained linear dependence. That supports his reading. Note that for general (complex, non-physical-region) singularities a condition without positivity is the *correct necessary* condition. What it lacks is sufficiency for physical-region pinches, which needs λ_j ≥ 0 (Collins Defs. 6–7, Thm. 1).

---

## 5. E16 — One-jettiness has coherence-violating logarithms (contra Alioli et al. 2024)

**BFH (arXiv:2511.11799v1 = PRL 136 (2026) 221901, doi:10.1103/flv7-ksvf).** Final equation:
"dσ₁^CVL/(dx_a dx_b dℬ) ≈ Σ_{a=q,g} A_a (α_s/π)⁴ (−iπ)² (1/480) (ln 1/τ₁)⁶", with
A_q = (8/3)N_c²T_R⁴ f^q_A f^g_B σ⁽⁰⁾_qg(ℬ) and A_g = −(32/3)N_c²T_R⁴ f^g_A f^q_B σ⁽⁰⁾_gq(ℬ), PDFs at τ₁Q and fixed α_s. The paper also states: "We expect this behaviour to extended to higher orders as α_s^n L^{2n−2} for n≥4." The exponentiated form of their eq. (2) is said to fail.

**Alioli et al. (arXiv:2312.06496v1 = PRD 109 (2024) 094009), Introduction:** "The one-jettiness variable is a suitable event shape for colour singlet (L) + jet production which does not suffer from superleading or nonglobal logarithms."

**Reproduced:**
* **1/480** (`e16_integral.py`): with l = ln(k_T/τ₁Q), t = ln(1/θ), u(k) ⇔ t > l and L₂ = l² (μ_F = τ₁Q), the integral is 2∫₀^{L/2}dl l⁴(L−2l) = **L⁶/480** exactly. Using tan(θ/2) ≈ θ/2 in u(k) changes only L⁵ and lower terms.
* **Colour factors** (`e16_colour.py`), by explicit SU(N) colour-space algebra. I built the 4-parton state t_a|M_Born⟩ (Catani–Seymour charge conventions; colour conservation checked to 10⁻¹⁶; t_a² = C_F resp. C_A) and computed ⟨(1/3)[T_s²,[T_s²,T_ad²]]⟩/⟨M|M⟩ with T_ad² = Σ_{i<j,(ij)≠(ad)} T_i·T_j. Result: **A_q/σ = 0.6667, 1.5000, 2.6667** and **A_g/σ = −2.6667, −6.0000, −10.6667** for N = 2, 3, 4. These equal (8/3)N²T_R⁴ and −(32/3)N²T_R⁴ exactly.
* BCH: the (iπ)² term of V†V is (1/3)[b,[b,a]], matching BFH. Their displayed single-commutator term has the opposite sign to mine, but it drops out under the trace.
* **Independent confirmation:** Becher, Hager, Neubert, Schwienbacher, "Factorization beyond Coherence", arXiv:2603.12383 = **PRL 137 (2026) 121902** (doi:10.1103/q3m4-bcpl). They work in SCET with Glauber modes and new momentum modes. The iterated scale integral gives ln⁶(Q/ω)/46080, reproduced: L′⁶/720 with L′ = ½ln(Q/ω). Quote: "For the qg→q channel, expression (CVL1jet) confirms the corresponding result obtained in [Banfi:2025mra]", with leading CVLs ∼ α_s^{2+n} ln^{2+2n} (n ≥ 2), starting at five loops for 0-jettiness. They also write: "Our findings imply that most existing factorization formulas for global LHC observables must be revised." The BHNS acknowledgements thank Banfi for triggering the project, but the method and authors are independent.

**Corrections to the claim:** drop "single group". Alioli et al.'s sentence is contradicted in its super-leading part; non-global logs are not at issue. The grade [V] for "τ₁ free of SLLs" is now supported by two groups with different methods.

---

## 6. E17 — Aybat–Rogers 2011: spurious factor 2 in ζ

**Published (arXiv:1101.5057v2 = PRD 83 (2011) 114042; identical in v1):**
* eq. (3): ζ_F = 2M_p²x²e^{2(y_P−y_s)};
* eq. (4): ζ_D = 2(M_H²/z²)e^{2(y_s−y_h)}.
They state: "Together, Eqs. (3, 4) give √(ζ_Fζ_D) ≈ Q²" and later "Since √(ζ_Fζ_D) ≈ Q², we will … use √ζ_F = √ζ_D = Q". Their light-cone convention is V^± = (V⁰±V^z)/√2 (Sec. III).

**Correct:** ζ_F = M_p²x²e^{2(y_P−y_s)} = 2(xP⁺)²e^{−2y_s} and ζ_D = (M_H²/z²)e^{2(y_s−y_h)} = 2(P_h⁻/z)²e^{2y_s}, so that √(ζ_Fζ_D) = Q².

**Checks (`e17_check.py`):**
* M²e^{2y_P} = 2(P⁺)² and M_h²e^{−2y_h} = 2(P_h⁻)², exactly in their convention.
* With Q² = 2xP⁺P_h⁻/z: their (3),(4) give √(ζ_Fζ_D)/Q² = **2**; the corrected forms give **1**.
* RG consistency: with their (B1) γ_F = (α_sC_F/π)(3/2 − ln ζ/μ²), γ_D = γ_F at O(α_s) (their App. B), and the standard one-loop hard factor (γ_H = −(α_sC_F/π)(3 − 2ln Q²/μ²)), the sum γ_H + γ_F + γ_D = (α_sC_F/π) ln[Q⁴/(ζ_Fζ_D)]. It vanishes iff ζ_Fζ_D = Q⁴; with the printed normalization it equals −ln 4. So (B1) and (A11), whose ζ-dependent δ(1−x) term is −L_b ln(ζ_F/μ²), are consistent only with the unprinted normalization.
* (A10) (C̃ for q in g) is ζ-independent and should not be listed.
* The **same authors** (with Collins, Qiu) write ζ_F = M_P²x²e^{2(y_P−y_s)} and ζ_D = (M_h²/z²)e^{2(y_s−y_h)}, "They obey √(ζ_Fζ_D) = Q² up to power-suppressed corrections, and have been normalized to correspond to CSS's definitions" (ACQR, arXiv:1110.6428v3 = PRD 85 (2012) 034043, eqs. (2),(3)).
* Collins–Rogers (arXiv:1210.2100v2 = PRD 87 (2013) 034018) eqs. (4),(5): ζ_A = 2(x_Ap_A⁺)²e^{−2y_n}, ζ_B = 2(x_Bp_B⁻)²e^{2y_n}, ζ_Aζ_B = Q⁴.
* Re-run of `research/c_tmd/scripts/one_loop_tmd.py`: the δ(1−x) coefficient of the Collins TMD at k_T ≠ 0 is −2y_n − ln k_T² + 2ln p⁺ + ln 2 = ln(ζ/k_T²) with ζ = 2(p⁺)²e^{−2y_n}; also γ_F = a(3 − 2l_ζ), K̃ = −(α_sC_F/π)L_b. All PASS.

INSPIRE texkey of the paper is Aybat:2011zv; CLAIMS.md uses "AybatRogers2011".

---

## 7. E18 — Collins arXiv:0708.4410v1 eq. (10): spurious numerator

**Published (eq. (10), second line; page 7 rendered):**
I₁(k_T) = λ²g₁²g₂(g₂+g₁)x(1−x)/(256π⁷) ∫d²l_{1T}d²l_{2T} ∏_{j=1,2} (k_T²+m_q²)/[(l_{jT}²+m_g²)((k_T−l_{jT})²+m_q²)].

Eq. (11): I₂(k_T) = −λ²g₁²g₂(g₂+g₁)x(1−x)/(256π⁷) ∫d²l_{1T}d²l_{2T} 1/[(l_{1T}²+m_g²)(l_{2T}²+m_g²)((k_T−l_{1T}−l_{2T})²+m_q²)(k_T²+m_q²)].

Text after (11): "Integrating I₁(k_T)+I₂(k_T) over all k_T gives zero … it can be proved analytically that I₁(0)+I₂(0) < 0." The paper has no journal version (INSPIRE: Collins:2007jp).

**Correct:** I₁ = 𝒩F(k_T)² with F(k) = ∫d²l/[(l²+m_g²)((k−l)²+m_q²)]. I₂ = −𝒩G(k_T)/(k_T²+m_q²) as printed, with G(k) = ∫d²l₁d²l₂/[(l₁²+m_g²)(l₂²+m_g²)((k−l₁−l₂)²+m_q²)] and 𝒩 = λ²g₁²g₂(g₂+g₁)x(1−x)/(256π⁷).

**Checks (`e18_check.py`, output saved):**
* **Derivation from the first line of (10).**
  * At l_j⁺ = 0 the l_j⁻ integral is ∫du/[(−2xp⁺u−A+i0)(2(1−x)p⁺u−A+i0)] = πi/(p⁺A), with A = (k_T−l_T)²+m_q² (residue; numerically confirmed). On the complex-conjugate side of the cut it is −πi/(p⁺A).
  * The k⁻ δ-function gives 2π/(2(1−x)p⁺).
  * Each gluon gives 2(1−x)p⁺·(−1/(l_T²+m_g²))·(±πi/(p⁺A)).
  * Collecting all constants gives **I₁ = 𝒩F²** with the correct conjugation (+i0 left, −i0 right of the cut). Taking the printed "+iε" literally on both sides gives −𝒩F². Either way **no factor (k_T²+m_q²)** arises, and the normalization 1/(256π⁷)·x(1−x) is reproduced exactly.
* **Dimensions** (λ has mass dimension 1 for the scalar cubic coupling): the first line of (10), the corrected second line and eq. (11) all have M⁻², as a TMD density must. The printed second line has M². Counting only the integrals, the comparison is M⁰ vs M⁻⁴, as in CLAIMS.md.
* **Cancellation**, with (m_g,m_q) = (0.5,1):
  * ∫d²k F² = 493.154149319 = ∫d²k G/(k²+m_q²) = (2π)³∫b K₀(m_gb)²K₀(m_qb)²db, so ∫d²k(I₁+I₂)/𝒩 = 5×10⁻¹¹.
  * Analytically: shifting k → k−l₁ and l_j → −l_j maps one integrand onto the other.
  * With the printed numerator, ∫_{k<K}d²k(k²+m_q²)²F² = 2.4×10⁵, 1.0×10⁸, 2.3×10¹⁰ for K = 10, 100, 1000, so the stated cancellation is impossible.
* **Sign:** I₁(0)+I₂(0) = −21.01𝒩 < 0, consistent with Collins' remark.
* Re-run of `research/c_glauber/scripts/tmd_breaking_abelian.py`: 31/31 PASS (A4a–A4f).
* Further misprints in the first line of (10): "(k−l₁)−m_q²" and "(p−k+l₁)−m_q²" lack squares, and the conjugate-side propagators carry +iε. None of these affect the corrected final form.
