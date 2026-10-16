# Verification batch E13–E18 (stage 2, second independent verifier)

Date: 2026-10-11. Stance: skeptical. I did not rely on the stage-1 report (`batch_E13_s1.md`). Every primary text quoted below
was downloaded again into a fresh scratch directory and read by me as text (untrusted data; nothing executed from it).
Where possible I used a different method or a different source from stage 1. These differences are listed per claim.

Scripts (all mine, run with `python3 -I`; copies and outputs are in `verify/claims/batch_E13_s2_scripts/`):
`e13_lorentz_map.py` (PASS), `e14_s2.py` (20/20 PASS), `e15_s2.py` (6/6 PASS) + `e15_conv.py`, `e15_conv2.py` (grid-convergence studies),
`e16_colour_s2.py` (PASS, N = 2…6), `e16_integral_s2.py` (PASS), `e17_s2.py` (8/8 PASS), `e18_s2.py` (9/9 PASS).
I also re-ran the project scripts named in the recipes from scratch copies: `research/c_regions/landau_oneloop.py` gave **23/23 PASS** (both L3f checks PASS).
`research/c_tmd/scripts/one_loop_tmd.py` gave **all PASS**. `research/c_glauber/scripts/tmd_breaking_abelian.py` gave **31/31 PASS** (A4f PASS).

## 1. Summary

| id | verdict | what must be printed / corrected | already in the literature? |
|---|---|---|---|
| E13 | **confirmed** | App. F of APPB 2022 calls a BHW statement "edge of the wedge". The derivation of (F.6) is unaffected. Also: App. F's map "Λ(t,z) → (it,iz)" is not a Lorentz map. The correct map is (t,z) ↦ (iz,it) (Liu 2024 eq. (3.25)). YZLIU.md line 262 copied the wrong map. | Terminology note only; no erratum published. Liu himself uses both theorems correctly in 2024/2026. |
| E14 | **confirmed** (with rewording) | Attribute the diagnosis to Collins 2020. Replace "F ≡ 0, so there is no parameter pinch" by the precise statement. Say "linear (e.g. eikonal/non-relativistic) denominators". "Result true" = pinch ⇔ Landau point (λ ≥ 0) ⇔ classical process, **not** "singularity ⇔ classical process". | Yes: Collins arXiv:2007.04085 §I, §IV, App. D (unrefereed). Also Kawai 1994 for the massless CN picture. |
| E15 | **confirmed** (with corrections) | The ELOP p. 48/50 statements were now checked directly in ELOP (Google Books snippets). The (2.1.19b) content is still Collins' reading. Write "in ≥ 2 dimensions" for anomalous deformations. Do **not** repeat Collins' remark that the FFLP paper "is still unpublished": ELOP's own bibliography adds "See also Fotiadi et al., Topology 4, 159 (1965)". | Yes: Collins 2011 §5.4.3; Collins 2020 §I, §IV, Apps. A, B. |
| E16 | **confirmed**; "single group" must be dropped | Two groups now agree: Becher–Hager–Neubert–Schwienbacher, PRL 137 (2026) 121902, confirm the qg→q result. Alioli et al. are contradicted on the super-leading part; NGLs are not at issue. BFH's displayed single-commutator BCH term has a sign slip, which is harmless. | Yes: BFH 2026 itself, confirmed by BHNS 2026. |
| E17 | **confirmed** | The factor 2 is also in eq. (4) (ζ_D). (A10) is ζ-independent, so the test rests on (A11),(B1). Cite INSPIRE key Aybat:2011zv. | Implicitly corrected by the same authors (ACQR PRD 85 (2012) 034043; proceedings arXiv:1107.3973) and by Collins–Rogers 2013. No explicit erratum. |
| E18 | **confirmed** | None for the main point. First-line typos as noted (missing squares; +iε on the conjugate side flips the overall sign if read literally). | Not recorded anywhere (unpublished preprint, v1 only). |

---

## 2. E13 — APPB App. F: "edge of the wedge" is really Bargmann–Hall–Wightman

**Read directly.** Liu, APPB 53 (2022) 4-A2, journal PDF (actaphys.uj.edu.pl), App. F "Alternative proof of S = S_DY", p. 4-A2.80:
> "Then both Wightman functions are in their analytic region, and all arguments relate with each other through the complex
> Lorentz transform Λ(t, z) → (it, iz)) since Λ(−iv, −iv′) = (n, n′). Then one needs to use the 'edge of the wedge' theorem. This
> theorem states that the Wightman functions in their analytic region called the 'extend tube' transform under complex Lorentz
> transform in a covariant way. In fact, the extended tube is constructed exactly through complex-Lorentz transforms from the
> tubes. Given the theorem, we have [(F.6)] … Note that the theorems mentioned above only rely on the tempered nature of the
> Wightman functions, causality (for the 'edge of the wedge' theorem), and support property, but do not require any positivity".

Earlier in the same paragraph: "Now we choose the same N + M points from the contour of W_DY, but according to the z-ordering.
This is possible since W_DY is insensitive to time-ordering."

**Statements of the two theorems (sources different from stage 1):**
* **BHW.** A. S. Wightman, "The spin-statistics connection" (Electron. J. Diff. Eqns. Conf. 04 (2000), pp. 210–211), describes it in his own words. F_n is analytic in the forward tube and invariant under L↑₊. It "can be extended by analytic continuation to points of the form Λζ₁,…,Λζ_{n−1}, where Λ is an arbitrary proper complex Lorentz transformation; the set of all such points form the extended tube. The BHW Theorem (1957) says that, so extended, F_n is analytic and single-valued … and is invariant under L₊(C)". For tensor and spinor fields, invariance becomes the covariant transformation law. The inputs are tube analyticity (spectral condition, temperedness) and real Lorentz covariance; **locality is not used**.
* **Streater–Wightman numbering** (the book itself is not accessible: archive.org lending only, Google Books quota exhausted). arXiv:2105.07487 (an independent citing paper, App. A) refers to "the Bargmann-Hall-Wightman theorem (Theorem 2-11 and its Lemma of [Streater–Wightman])".
* **Edge of the wedge.** Hollands–Sanders, arXiv:1702.04924, App. A, Theorem 19: F₁ is holomorphic on U+iC, F₂ on U−iC, and their distributional boundary values on the real open set U coincide. Then there is a holomorphic F on a complex neighbourhood of U extending both. This is a gluing theorem; it says nothing about Lorentz covariance. In Wightman theory it enters, together with locality, to combine permuted Wightman functions. arXiv:2102.02433 §2 describes that use. Ji–Liu–Su arXiv:2601.12189v1 §5.1 (caption of the w-plane figure) uses it the same way: "Because of locality … the two functions have identical boundary values on this edge, which means G_>(w,z⃗) and G_<(w,z⃗) can be combined into a single analytic function based on the Edge-of-the-wedge theorem."

**Liu 2024 (arXiv:2312.05957v6 = JHEP 09 (2024) 030, source read).** §2.1: "the analytic Wightman functions are covariant under proper complex Lorentz transforms (complex-valued Lorentz transforms with determinants equal to 1) and are symmetric or anti-symmetric under permutations". Further: "without using the local commutativity, one obtains n! analytic functions 𝒲_P … given the local commutativity, all these n! analytic functions can be combined together as a single analytic function." Neither theorem is named, and both statements are correct. The word "wedge" does not occur.

**Assessment.** The property App. F needs and states, covariance of the continued Wightman functions on the extended tube under L₊(C), is the BHW theorem. The locality ("causality") input that App. F attributes to that theorem is really needed elsewhere: in the step "W_DY is insensitive to time-ordering", where the W_DY points are re-ordered at (totally space-like, Jost-type) real points. So the error is in the naming and in where "causality" is placed. The chain BHW + locality supports (F.6), so the claim "terminology only" is correct.

**Side issue (`e13_lorentz_map.py`, PASS).** As a 2×2 map on (t,z), "Λ(t,z) → (it,iz)" has ΛᵀgΛ = −g and det = −1. It is not a Lorentz map, and it sends −iv to v rather than to n. The map (t,z) ↦ (iz,it) has ΛᵀgΛ = g and det = +1, and sends −iλn ↦ λn and −iλn̄ ↦ −λn̄. This is Liu 2024 eq. (3.25), with (3.26)–(3.27); I checked the equation number in the v6 PDF. `frontier/yzliu/YZLIU.md` line 262 copies the wrong form and must be fixed before printing.

**Verdict: confirmed.** Different from stage 1: I used Wightman's own description of BHW, a different citing paper for S-W Thm 2-11, and the Hollands–Sanders statement of the edge-of-the-wedge theorem. Stage 1 used Ruelle's review, Hall–Wightman 1957, Hollands gr-qc/0212028 and Wikipedia.

---

## 3. E14 — Coleman–Norton 1965: momentum-space vs parameter-space pinch

**Read directly: Collins arXiv:2007.04085v1, LaTeX source** (the only version; INSPIRE Collins:2020euz; no journal publication).
* §IV ("Literature review", CN paragraph): "To provide an actual proof of necessity and sufficiency, Coleman and Norton perform the momentum integrals analytically, and work with an integral solely over the parameters". They expand to "A = ½ Σ E_ij η_i η_j", and "it is easy to show that the contour is trapped, but only if none of eigenvalues of E_ij is zero … The proof does indeed fail when zero eigenvalues exist. It is not at all clear whether the failure can be remedied". Further: "That cases of zero eigenvalues arise in massive theories in reality is mentioned; they occur only at 'very exceptional points' … Considerable further work is apparently needed".
* Massless case: "in the parameter integral there is no pinch that corresponds to the collinear pinch in momentum space". For linear denominators: "the pure parameter integral has a pinch independently of whether there is a pinch in the momentum integral".
* "Evidently Coleman and Norton have assumed that a pinch in momentum space occurs if and only if a corresponding pinch occurs in parameter space … The examples just mentioned show that the implication is not even correct, in general, even if it works in the case of standard massive Feynman graphs." And: "It is important to remember that it is not the result that breaks down, but the proof." Here "the result" refers to the sentence just before: "a pinch configuration corresponds to a situation with classical particles propagating".
* App. D.1 (massless self-energy): in momentum space there are pinches at k = 0 and k = p for every p, and at p² = 0 a line of collinear pinches k = αp, 0 ≤ α ≤ 1. In the pure-parameter form Π = iΓ(2−n/2)(p²)^{n/2−2}(4π)^{−n/2}∫dα[α(1−α)+iε]^{n/2−2}: "there is no pinch correspond[ing] to the collinear singularity. Instead the singularity of the integral at p²=0 is in the prefactor only."
* App. D.2: for the non-relativistic bubble, ∫dω[(1−2α)ω + Eα − (k² − 2αpk + αp²)/2m + iε]^{−2} = −4iπm δ(α−½)/(2Em − 2k² + 2pk − p² + iε). The momentum-space pinch is only at E = p²/4m, (ω,k) = ½(E,p). The section is introduced as applying "with non-relativistic theories or with Wilson lines".
* Thm "main.contour": trap ⇔ Landau point (λ_j ≥ 0, not all zero). This holds under restrictions (a) denominators at most quadratic, and (b) a sign condition.

**CN 1965 itself is not accessible.** Springer is closed access (Semantic Scholar/OpenAlex: "closed"); CERN CDS and Springer block automated clients. Only the abstract (INSPIRE) was read: "As a by-product of the proof, the Feynman parameter associated with an internal line is identified … with the time the particle exists between collisions, divided by its mass." This confirms the parametric route and the massive setting. The tacit-assumption diagnosis is Collins', so it must be attributed to him. An independent remark: T. Kawai, RIMS Kôkyûroku 856 (1994) 107, "Microlocal analysis of massless singularities". He writes that the CN picture "becomes somewhat obscure when massless particles are relevant", because SS(1/(k²+i0)) contains the component {k = 0, w arbitrary}, which is not the m→0 limit of the massive one. This is consistent with Collins' k = 0 pinch.

**Independent computations (`e14_s2.py`, 20/20 PASS; different from stage 1).**
1. I derived the bubble's parametric denominator by completing the square in k (general masses). The result is k_c = α₂p/U and D(k_c) = −F/U with F = U(α₁m₁²+α₂m₂²) − α₁α₂p². For massless lines F = −p²α₁α₂, which vanishes identically at p² = 0.
2. CN quadratic form on the simplex. At the massive threshold p² = (m₁+m₂)² the critical point is x* = m₂/(m₁+m₂), with D(x*) = 0 and E = D″ = 2(m₁+m₂)² ≠ 0, so the form is nondegenerate. In the massless case D = −s x(1−x). At s = 0, D, D′ and D″ all vanish identically, so all eigenvalues are zero. For s ≠ 0 the only stationary point is x = ½, where D = −s/4 ≠ 0, so there is no interior Landau point.
3. Momentum space, light-cone components. At p² = 0, k = xp solves the Landau equations with (λ₁,λ₂) = (1−x, x) for every x. For p² ≠ 0 the only solutions with both lines on shell have λ₁ = λ₂ = 0. Trap test at k = 0.3p: the gradients are anti-parallel with positive weights, and 2×10⁵ random directions give no v with v·∇A₁ > 0 and v·∇A₂ > 0. At k = 0, A₁ = 0 and ∇A₁ = 0 for every p, which is the single-denominator pinch of Collins D.1.
4. App. D.2 by a different route from stage 1: a symmetric cutoff in ω. I find ∫_{−Λ}^{Λ}dω(aω+B)^{−2} = 2Λ/(B²−a²Λ²). For fixed α ≠ ½ this tends to 0. As a distribution in α its weight tends to −iπ/B(½) (checked for three complex B), which equals Collins' −4iπm/(2Em−2k²+2pk−p²). Solving the Landau equations gives the momentum pinch only at E = p²/4m, (ω,k) = (p²/8m, p/2), λ₁ = λ₂. The identity E − k²/2m − (p−k)²/2m = (E − p²/4m) − (k−p/2)²/m shows the square-root branch point at E = p²/4m.

**Precision issues in the claim wording.**
* (a) "F = −p²α₁α₂ ≡ 0, so there is no parameter pinch" is a loose inference. At p² = 0, F ≡ 0 means the parametric Landau conditions hold everywhere: the CN form is totally degenerate, not absent. What is true, and should be printed, is the following. F = p²·(p-independent function of α), so the α-integrand has no pinch for any p. The collinear singularity at p² = 0 sits in the prefactor (−p²)^{n/2−2}.
* (b) "Eikonal" should read "denominators linear in a momentum component, e.g. non-relativistic propagators or Wilson-line (eikonal) denominators". Collins' explicit example is non-relativistic.
* (c) "Result true" must be stated as: physical-region trap ⇔ Landau point with λ_j ≥ 0 ⇔ classical (Coleman–Norton) process. This is proven in Collins 2020 Thm main.contour (unrefereed; restrictions (a),(b)). CN's literal "singularity ⇔ classical process" is **not** true in massless theories: the massless bubble is pinched at k = 0 and k = p for every p but is singular only at p² = 0 (Collins D.1).
* (d) For massive graphs CN's argument is incomplete only at zero-eigenvalue points, which CN called "very exceptional" and which Collins leaves unresolved. "Proof [V]" therefore refers to the massless and linear-denominator cases, plus a gap at exceptional massive points.

**Verdict: confirmed** in the precise form below. Attribution to CN's text is via Collins and the CN abstract.

---

## 4. E15 — ELOP §2.1 and textbook Landau-analysis errors

**Read directly in ELOP for the first time** (CUP 2002 reprint of the 1966 book, Google Books "search within volume" snippets, volume id VWTnlTyjwjMC, page numbers as printed):
* p. 48: "… be content with plausibility arguments. (a) Usually, when a singularity surface S_r advances on H a distortion of H away from S_r, in the direction of the normal to S_r, will keep H out of the way and so will avoid the singularity …"
* p. 48: "… distorted away from its original real location, much as the simple contour C was distorted for the case of the single integration variable. When the possibility of this distortion ceases, so that H becomes trapped, we are liable to …"
* p. 49: "Since the normals to the S_r represent directions in which the hypercontour cannot move …"; "… (2.1.19) are plausible is to consider the comparison function … (2.1.20)".
* p. 50: "… rigorous treatment requires homology theory and for this we refer to the paper by Fotiadi, Froissart, Lascoux & Pham (1964). 2.2 The Landau equations …"
* Bibliography p. 280: "FOTIADI, D., FROISSART, M., LASCOUX, J. & PHAM, F. (1964). (Unpublished). See also FOTIADI et al. Topology, 4, 159 (1965)." Crossref confirms D. Fotiadi, M. Froissart, J. Lascoux, F. Pham, "Applications of an isotopy theorem", Topology 4 (1965) 159–191, doi:10.1016/0040-9383(65)90063-7. I did not read its content.
* I could **not** see the text of (2.1.19a,b) (Google rate limit). That item stays second-hand, via Collins.

**Read directly: Collins 2011** (open-access reissue, Cambridge Core, ch. 5 PDF; page header "110"), §5.4.3:
> "A devil's advocate would search for a proof in the literature that the Landau equations are both necessary and sufficient for
> a PSS, and would be rewarded by not finding a published explicit and complete proof. Textbook treatments, when examined closely,
> are incomplete. For example, in … Eden et al. (1966), we read (p. 48): 'A proper proof needs the use of topology; … We shall be
> content with plausibility arguments.' The reference given for a real proof is an unpublished paper, by Fotiadi, Froissart,
> Lascoux, and Pham; the paper, as far as I can find out, is still unpublished forty years later."

**Read directly: Collins 2020** §IV, ELOP paragraph. It makes four points:
* the "normal" is not unambiguous (the allowed directions form a half-space, and a normal needs a Euclidean structure);
* the tacit assumption that avoiding a singularity needs a non-zero first-order shift is "definitely not the case";
* "(2.1.19b) … lacks the positivity constraint needed for the kind of 'physical region' pinch … While the more general version is appropriate for pinches outside the physical region, further conditions are needed";
* positivity appears in ELOP only in the Feynman-parameter treatment.

Apps. A, B.1 and B.2 were read in source.

**Independent test of the anomalous deformations (`e15_s2.py`, 6/6 PASS; method different from stage 1's distance scan).** I used multidimensional Cauchy invariance. Take I = ∫dE dp i f(E,p)/(E − p²/2m + iε) with f = e^{−(E²+p²)} entire. Deform (E,p) → (E_R,p_R) + iλχ(η,ξ), where χ is a Gaussian bump and the full complex Jacobian is included. An allowed deformation must leave I unchanged; one that crosses the pole changes I.
* ε = 0.1. Undeformed: I = 4.50137595 − 0.95512198i. anom2, (η,ξ) = (p_R + p_R²/2m − E_R, m): identical to all printed digits. anom1, (η,ξ) = (|E_R|+2|p_R|, m): agrees to 2×10⁻⁵ at h = 0.004, with error ∝ h² on the midpoint grid (7.9e-5, 2.0e-5, 5.0e-6 for h = 0.008, 0.004, 0.002). With |·| smoothed it agrees to 10⁻¹⁵. The constant tangent deformation (0, m) gives 1.085 + 6.661i: it crosses the singularity.
* ε = 0 on the deformed contours versus the ε→0⁺ limit (computed with the natural shift E → E + 0.5i): anom2 differs by 1.0e-5, 8.6e-7, 1.35e-7 and anom1 by 2.1e-5, 5.2e-6, 1.3e-6 for h = 0.004, 0.002, 0.001, so both converge (`e15_conv2.out.txt`). The tangent deformation is off by 9.4. The undeformed integral approaches the limit linearly in ε (0.26 at ε = 0.05, 0.106 at ε = 0.02).
* Symbolic check, including the bump c > 0. For anom2, Re = 0 at E_R = p_R²/2m − λ²c²m/2, where Im = (λ³c³m + 2ε)/2 > 0. For anom1, Im = λc(|E_R| + 2|p_R| − p_R) + ε ≥ λc(|E_R|+|p_R|) + ε. So the first-order shift vanishes (at the origin for anom1, on the whole surface for anom2), yet no singularity is met.
* Collins App. B.2 (read): in one dimension a strictly positive first-order shift *is* necessary. Hence the false textbook assumption is false **in ≥ 2 dimensions**.
* Collins' typo: in his eq. (den) "iλ(η−ξp_Rm)" should read iλ(η−ξp_R/m); the formulas that follow use the correct form.

**"Landau condition ⇒ singularity" [V].** App. A: I(Q/m) = m²Q∫dk/[(k−m+iε)(k−iε)²(k+Q−iε)] = −2πi/(1+m/Q). The contour is trapped as m→0, but the function is regular; Collins calls this example "entirely trivial", a numerator cancellation. The physically relevant example is D.1, the massless bubble, which is pinched for all p but singular only at p² = 0 (reproduced in `e14_s2.py` (c)). The Landau condition is necessary for a singularity: no trap means the contour can be deformed away. It is necessary and sufficient for a trap (Collins Thm main.contour, unrefereed).

**Corrections and caveats for printing.**
* State the ELOP points as "ELOP p. 48: 'be content with plausibility arguments'; 'in the direction of the normal to S_r'" (now verified in ELOP). The positivity point about (2.1.19b) must be attributed to Collins 2020 §IV. Note that (2.1.19b), without a sign constraint, is the correct general necessary condition for complex singularity surfaces; it is not sufficient for a physical-region trap.
* "Collins 2011 §5.4.3: there is no complete published proof" is an accurate **attribution** (necessary and sufficient for a PSS). Collins' remark that FFLP "is still unpublished forty years later" should **not** be repeated: ELOP's bibliography itself points to FFLP, Topology 4 (1965) 159. Whether that paper, Pham 1967, or the later isotopy work (Mühlbauer arXiv:2011.10368, unpublished per INSPIRE) settles the physical-region statement was not checked. Collins 2020 now claims a complete proof (arXiv only).

**Verdict: confirmed**, with the corrections above.

---

## 5. E16 — One-jettiness has coherence-violating logarithms (contra Alioli et al. 2024)

**Read directly.** BFH arXiv:2511.11799v1 source (only version; INSPIRE Banfi:2025mra = PRL 136 (2026) 221901, doi:10.1103/flv7-ksvf):
* Abstract: τ₁ "suffers from super-leading logarithms starting at order α_s⁴ ln(1/τ₁)⁶ relative to the Born level".
* Introduction: "According to [Alioli:2023rxx], one-jettiness … is free from both non-global and super-leading logarithms … In this letter we show that this is not the case".
* The calculation is for qg → qZ, with μ_F = τ₁Q and fixed α_s. Final equation: dσ₁^CVL/(dx_a dx_b dℬ) ≈ Σ_{a=q,g} A_a (α_s/π)⁴(−iπ)²(1/480)(ln 1/τ₁)⁶, with A_q = (8/3)N_c²T_R⁴ f^q_A f^g_B σ⁽⁰⁾_qg(ℬ) and A_g = −(32/3)N_c²T_R⁴ f^g_A f^q_B σ⁽⁰⁾_gq(ℬ).
* Higher orders: "We expect this behaviour to extended to higher orders as α_s^n L^{2n−2} for n≥4". The exponentiated form of their eq. (2) fails.
* Alioli et al. arXiv:2312.06496v1 (only version; Alioli:2023rxx = PRD 109 (2024) 094009), Introduction: "The one-jettiness variable is a suitable event shape for colour singlet (L) + jet production which does not suffer from superleading or nonglobal logarithms."

**Independent checks (methods different from stage 1).**
* **Colour factors** (`e16_colour_s2.py`). I used a matrix-free SU(N) implementation with all-outgoing conventions, N = 2…6 (stage 1: N = 2, 3, 4). It computes R_a = ⟨ψ|⅓[T_s²,[T_s²,T_ad²]]|ψ⟩/⟨M|M⟩, ψ = T_a^d M, in two ways. One is directly. The other uses a shortcut I derived from Uψ = C_aψ, where U = (T_a+T_d)²: R_a = −⅓⟨T_s²ψ|(C_a − U)|T_s²ψ⟩/⟨M|M⟩. Results: R_q = 0.6667, 1.5000, 2.6667, 4.1667, 6.0000 = N²/6 = (8/3)N²T_R⁴ exactly. R_g = −2.6667, −6, −10.6667, −16.6667, −24 = −(32/3)N²T_R⁴ exactly. The two routes agree. The shortcut also shows sign(A_q) > 0, since U ≥ C_F on 3⊗8, while A_g can be negative, since 8⊗8 contains the singlet.
* **1/480** (`e16_integral_s2.py`). I used the *exact* BFH boundaries: u(k) = Θ(τ₁ − (k_T/Q)tan(θ/2)), θ ∈ [k_T/Q, 1], L₂ = ln²(k_T/τ₁Q). I evaluated the integral numerically for L = 20…200 (mpmath) and fitted a degree-6 polynomial. The L⁶ coefficient is 0.0020833333 = 1/480 to 10 digits, and the L⁵ coefficient is 6 ln2/480, from tan(θ/2) ≈ θ/2. The leading-log form 2∫₀^{L/2}ℓ⁴(L−2ℓ)dℓ = L⁶/480 holds exactly.
* **BCH.** Finite differences on random Hermitian matrices give the O(ab²) term of V†V, V = exp(aS_ad + ibS_s), as −⅓ab²[S_s,[S_s,S_ad]] = ⅓a(ib)²[S_s,[S_s,S_ad]]. This is BFH's third term, with ib = −iπ(α_s/π)ln(k_T/μ_F). The O(ab) term is +i ab[S_ad,S_s], so BFH's displayed second term has the opposite sign (stage 1 noted the same). It vanishes under the trace with the real-symmetric density matrix, so the result is unaffected.
* **Independent confirmation, read in source.** Becher–Hager–Neubert–Schwienbacher, arXiv:2603.12383v1 = **PRL 137 (2026) 121902** (Becher:2026kbr, doi:10.1103/q3m4-bcpl). They use SCET with Glauber and new soft/ultra-collinear modes: "For the qg→q channel, expression (CVL1jet) confirms the corresponding result obtained in [Banfi:2025mra]", with leading CVLs dσ/dω ∼ α_s^{2+n}ln^{2+2n}(Q/ω), n ≥ 2, the same tower as α_s^nL^{2n−2}, n ≥ 4. Their iterated integral: with L′ = ln(ω_c/ω) = ½ln(Q/ω), ∫(L′−x₁)x₁⁴/24 = L′⁶/720, so the result is ln⁶(Q/ω)/46080 as printed. The authors and method are independent; they thank Banfi for "triggering this project". INSPIRE lists 16 citing papers of BFH, and none disputes the result.

**Corrections.** Drop "single group": the result is now confirmed by two groups with two methods. The contradiction with Alioli et al. concerns the super-leading part of their sentence, and non-global logarithms are not at issue. The result is a cumulant in τ₁, differential in the Born variables, at fixed α_s, for the qg → qZ channel.

**Verdict: confirmed** (with "single group" replaced by the BHNS confirmation).

---

## 6. E17 — Aybat–Rogers 2011: spurious factor 2 in ζ_F (and ζ_D)

**Read directly.** arXiv:1101.5057v2 source and PDF (Aybat:2011zv = PRD 83 (2011) 114042); v1 is identical on this point.
* (3) ζ_F = 2M_p²x²e^{2(y_P−y_s)}; (4) ζ_D = 2(M_H²/z²)e^{2(y_s−y_h)}; convention (5): V^± = (V⁰±V^z)/√2, V² = 2V⁺V⁻ − V_T².
* Text: "Together, Eqs. (3, 4) give √(ζ_Fζ_D) ≈ Q²" and "Since √(ζ_Fζ_D) ≈ Q², we will … use √ζ_F = √ζ_D = Q".
* (A10): C̃_{j′/g} = (α_sT_f/2π)(2[1−2x(1−x)][ln(2/(b_Tμ)) − γ_E] + 2x(1−x)). This is **ζ-independent**.
* (A11): the δ(1−x) term is (α_sC_F/2π)[−½(ln b_T²μ² − 2(ln2−γ_E))² − (ln b_T²μ² − 2(ln2−γ_E)) ln(ζ_F/μ²)] = (α_sC_F/2π)[−½L_b² − L_b ln(ζ_F/μ²)], with L_b = ln(μ²b_T²/b₀²).
* (B1): γ_F = α_s(C_F/π)(3/2 − ln(ζ_F/μ²)).

**Other sources read.**
* Aybat–Collins–Qiu–Rogers, arXiv:1110.6428v3 "as published" (Aybat:2011ge = PRD 85 (2012) 034043), eqs. (zetaF),(zetaD): ζ_F = M_P²x²e^{2(y_P−y_s)} and ζ_D = (M_h²/z²)e^{2(y_s−y_h)}. "They obey √(ζ_Fζ_D) = Q² up to power-suppressed corrections, and have been normalized to correspond to CSS's definitions". γ_F is identical to (B1).
* Aybat–Rogers proceedings arXiv:1107.3973 (Aybat:2011vb): "ζ₁ζ₂ = Q⁴". It also gives the one-loop SIDIS hard factor |H|² = 1 + (C_Fα_s/π)[(3/2)ln(Q²/μ²) − ½ln²(Q²/μ²) − 4].
* Collins–Rogers arXiv:1210.2100v2 (Collins:2012uy = PRD 87 (2013) 034018), eqs. (zeta.A),(zeta.B): ζ_A = 2(x_Ap_A⁺)²e^{−2y_n}, ζ_B = 2(x_Bp_B⁻)²e^{2y_n}, ζ_Aζ_B = Q⁴.

**Independent checks (`e17_s2.py`, 8/8 PASS).**
1. Kinematics in their convention: M²e^{2y_P} = 2(P⁺)² and M_h²e^{−2y_h} = 2(P_h⁻)². With Q² = 2xP⁺P_h⁻/z (hadron frame), the printed (3),(4) give √(ζ_Fζ_D) = **2Q²**, while the factor-free forms give Q². The factor-free ζ_F equals 2(xP⁺)²e^{−2y_s} (Collins–Rogers form).
2. RG invariance using the **authors' own** hard factor (1107.3973), which differs from stage 1's use of the standard one. It gives γ_H = (α_sC_F/π)(2 ln(Q²/μ²) − 3), and with (B1), γ_H + γ_F + γ_D = (α_sC_F/π) ln(Q⁴/(ζ_Fζ_D)). This vanishes iff ζ_Fζ_D = Q⁴; with the printed normalization it is −(α_sC_F/π) ln 4.
3. Independent derivation of the normalization. The Collins soft-factor ratio √(S(+∞,y_s)/(S(+∞,−∞)S(y_s,−∞))) removes real gluons with rapidity below y_s, since the Y_± cancel. With y_l = ln(√2 l⁺/l_T), the cut is (1−x) > k_Te^{y_s}/(√2p⁺). The δ(1−x) coefficient is then 2ln(1/δ₀) = ln(ζ/k_T²) with ζ = **2(p⁺)²e^{−2y_s}**. This matches the project's `one_loop_tmd.py` result (re-run: PASS) and the factor-free ζ_F, consistent with the standard (A11) form.

**Corrections.** The factor 2 also sits in eq. (4) for ζ_D. Cite (A11),(B1), not (A10), which cannot detect the normalization. The bibliography key should be Aybat:2011zv. The statement "a misprint; do not copy" is justified: the paper's own text, its √ζ = Q choice, the same authors' 2011 proceedings and 2012 PRD, and RG invariance all require the factor-free form.

**Verdict: confirmed.**

---

## 7. E18 — Collins arXiv:0708.4410v1 eq. (10): spurious numerator

**Read directly.** Source (`2loop.tex`, labels eq:I1, eq:I2) and v1 PDF. The equation numbers (10) and (11) were checked in the PDF text. INSPIRE Collins:2007jp has no publication information; there is only v1.
* Second line of (10): I₁(k_T) = λ²g₁²g₂(g₂+g₁)x(1−x)/(256π⁷) ∫d²l_{1T}d²l_{2T} ∏_{j=1,2}(k_T²+m_q²)/[(l_{jT}²+m_g²)((k_T−l_{jT})²+m_q²)].
* (11): I₂(k_T) = −(same)∫d²l_{1T}d²l_{2T} 1/[(l_{1T}²+m_g²)(l_{2T}²+m_g²)((k_T−l_{1T}−l_{2T})²+m_q²)(k_T²+m_q²)].
* Text: "Integrating I₁(k_T)+I₂(k_T) over all k_T gives zero … it can be proved analytically that I₁(0)+I₂(0) < 0."

**Independent checks (`e18_s2.py`, 9/9 PASS).**
1. **Dimensions** (λ has mass dimension 1, g is dimensionless). First line of (10): M⁻². Corrected second line: M⁻². (11): M⁻², the dimension of a TMD density. The printed second line has M⁺².
2. **Reduction of the first line** (symbolic). At l_j⁺ = 0, with the spectator on shell, the l_j⁻ integral has its D₁ pole in the upper half-plane. The residue is 1/(2p⁺A_j), so the integral is iπ/(p⁺A_j) with A_j = (k_T−l_{jT})²+m_q². It is **independent of B = k_T²+m_q²**. B cancels identically; I confirmed this numerically: 0.0018 + 2.05333i against 2.05333i. Collecting all factors, with −iε on the conjugate side of the cut, gives exactly x(1−x)/(256π⁷)·F(k_T)², with no (k_T²+m_q²) factor.
3. **Cancellation**, by momentum-space quadrature (a different method from the position-space Bessel route of stage 1 and of the project script). F(k) is the closed-form Feynman-parameter bubble, checked against Gauss–Legendre. G(k) = ∫d²l F(|k−l|)/(l²+m_g²) is computed by split radial and angular quadrature. At (m_g,m_q) = (0.5,1): ∫d²k F² = 493.154149562 and ∫d²k G/(k²+m_q²) = 493.154149607 (relative difference 9×10⁻¹¹), so ∫d²k(I₁+I₂) = 0 for the corrected I₁. This agrees with the project's b-space value 493.15414932. Analytic reason: shift k → k − l₁ and l₁ → −l₁.
4. With the printed numerator, ∫_{k<K}d²k(k²+m_q²)²F² = 2.43e5, 9.96e7, 2.28e10 for K = 10, 100, 1000. It diverges, so the stated cancellation is impossible.
5. I₁(0)+I₂(0) = 𝒩[F(0)² − G(0)/m_q²] = 𝒩(33.720 − 54.729) = −21.009𝒩 < 0. It is also negative for (m_g,m_q) = (0.2,2), (1,1), (2,0.3), consistent with Collins' remark.

**Extra misprints in the first line**, which do not affect the corrected form:
* "(k−l_j)−m_q²" and "(p−k+l_j)−m_q²" lack squares.
* The conjugate-side propagators carry +iε. Read literally, that turns F² into −F².

**Verdict: confirmed.** Not recorded in the literature.

---

## 8. Precise statements recommended for printing

* **E13.** "Liu (APPB 53 (2022) 4-A2, App. F) invokes the 'edge of the wedge' theorem for the covariance of the analytically continued Wightman functions under proper complex Lorentz transformations on the extended tube. That statement is the Bargmann–Hall–Wightman theorem (Hall–Wightman 1957; Streater–Wightman Thm. 2-11). It needs only the spectral condition and real Lorentz covariance: no locality, no positivity. The edge-of-the-wedge theorem glues holomorphic functions with coinciding boundary values on a real edge; with locality it combines the permuted Wightman functions. That is where App. F's 'causality' input (re-ordering the W_DY points) belongs. The conclusion (F.6) stands. The complex Lorentz map is Λ(t,z) = (iz,it) (Liu, JHEP 09 (2024) 030, eq. (3.25)), not (it,iz). Liu 2024 states the covariance correctly."
* **E14.** "Coleman and Norton (Nuovo Cim. 38 (1965) 438) obtain the physical-region criterion from the pure Feynman-parameter representation. As Collins (arXiv:2007.04085, §IV, App. D) points out, the proof tacitly assumes that the momentum-space contour is pinched iff the parameter contour is. Its trapping argument (A = ½E_ijη_iη_j) also needs all eigenvalues of E_ij to be non-zero.
  - The assumption fails for massless graphs. The one-loop massless self-energy has, at p² = 0, a line of collinear momentum-space pinches k = αp, 0 ≤ α ≤ 1. In the parametric form, however, F = −p²α₁α₂ is p² times a p-independent function. So the α-integrand has no pinch, and the collinear singularity sits entirely in the prefactor (−p²)^{n/2−2}. At p² = 0, F and all its α-derivatives vanish identically: the CN quadratic form is totally degenerate.
  - For denominators linear in a momentum component (non-relativistic or Wilson-line denominators) the parametric form is pathological. In Collins' example the ω-integral equals −4iπm δ(α−½)/(2Em−2k²+2pk−p²), localized at α = ½ whether or not the momentum integral is pinched. The momentum integral is pinched only at E = p²/4m.
  - In massive theories the argument fails at zero-eigenvalue points, which CN call 'very exceptional'; Collins regards this as unresolved.
  - Grade: CN's proof [V] (massless and linear-denominator cases; gap at exceptional massive points). The result 'physical-region trap ⇔ Landau point with λ_j ≥ 0 ⇔ classical Coleman–Norton process' is proven in Collins 2020, Thm. main.contour (unrefereed; denominators at most quadratic plus a sign condition). The literal 'singularity ⇔ classical process' is false for massless graphs: the massless bubble is pinched at k = 0 and k = p for every p but is singular only at p² = 0."
* **E15.**
  - (i) ELOP (1966) §2.1 is avowedly heuristic. P. 48 says 'We shall be content with plausibility arguments' (the fuller sentence 'A proper proof needs the use of topology; …' is quoted by Collins 2011 §5.4.3 and Collins 2020 §I). P. 50 says 'a rigorous treatment requires homology theory', citing Fotiadi–Froissart–Lascoux–Pham (1964, unpublished; 'see also Topology 4, 159 (1965)'). ELOP distorts the contour 'in the direction of the normal to S_r'. Collins 2020 §IV objects to three points. A normal is not canonical: the gradient is a dual vector, and the allowed directions form an open half-space. ELOP tacitly assumes that avoiding a singularity needs a non-zero first-order shift. And (2.1.19b), a correct general necessary condition for complex singularity surfaces, lacks the positivity λ_j ≥ 0 that characterizes physical-region traps.
  - (ii) The assumption 'a singularity-avoiding deformation must have a strictly positive first-order shift' is false in ≥ 2 real dimensions (true in one dimension; Collins App. B.2). Collins App. B.1 gives anomalous deformations for i/(E−p²/2m+iε): (η,ξ) = (|E_R|+2|p_R|, m) and (η,ξ) = (p_R+p_R²/2m−E_R, m) [V].
  - (iii) With λ_j ≥ 0, the Landau condition is necessary and sufficient for a trap (Collins 2020 Thm. main.contour, unrefereed) and necessary for a singularity. It is not sufficient for a singularity of the integral [V]. Examples: Collins App. A (power singularity cancelled by a numerator) and App. D.1 (massless bubble, pinched for all p, singular only at p² = 0).
  - (iv) Collins (2011, §5.4.3, p. 110) states that he found no published explicit and complete proof that the Landau equations are necessary and sufficient for a pinch singular surface, and that textbook treatments are incomplete." Do **not** add that the FFLP paper was never published (see §4).
* **E16.** "Banfi, Forshaw and Holguin (PRL 136 (2026) 221901, arXiv:2511.11799) show that the one-jettiness cumulant in colour-singlet + jet production contains coherence-violating (super-leading) logarithms from α_s⁴L⁶ relative to Born. They work in the qg → qZ channel at fixed α_s with PDFs at μ_F = τ₁Q.
  - Result: dσ₁^CVL/(dx_a dx_b dℬ) ≈ Σ_{a=q,g} A_a(α_s/π)⁴(−iπ)²(1/480)ln⁶(1/τ₁), with A_q = (8/3)N_c²T_R⁴ f^q_A f^g_B σ⁽⁰⁾_qg and A_g = −(32/3)N_c²T_R⁴ f^g_A f^q_B σ⁽⁰⁾_gq. They expect α_s^nL^{2n−2} terms (n ≥ 4) at higher orders, so the standard exponentiated form fails.
  - This contradicts the statement of Alioli et al. (PRD 109 (2024) 094009) that one-jettiness 'does not suffer from superleading or nonglobal logarithms', specifically its super-leading part.
  - Becher, Hager, Neubert and Schwienbacher (PRL 137 (2026) 121902) independently confirm the qg → q result in SCET with Glauber modes. Grade [V], two groups."
* **E17.** "Aybat and Rogers (PRD 83 (2011) 114042) print ζ_F = 2M_p²x²e^{2(y_P−y_s)} in eq. (3) and ζ_D = 2(M_H²/z²)e^{2(y_s−y_h)} in eq. (4). In their convention V^± = (V⁰±V^z)/√2 these equal twice the standard values, ζ_F = M_p²x²e^{2(y_P−y_s)} = 2(xP⁺)²e^{−2y_s} and ζ_D = (M_h²/z²)e^{2(y_s−y_h)} = 2(P_h⁻/z)²e^{2y_s}.
  - The printed forms give √(ζ_Fζ_D) = 2Q². This contradicts their own '√(ζ_Fζ_D) ≈ Q²', their choice √ζ_F = √ζ_D = Q, RG invariance with their (B1) and their own hard factor, and the same authors' PRD 85 (2012) 034043.
  - Their (A11) and (B1) coincide with the standard Collins-scheme one-loop results only for the factor-free ζ. The factor 2 is a misprint; do not copy."
* **E18.** "In Collins, arXiv:0708.4410v1, the second line of eq. (10) has a spurious numerator ∏_j(k_T²+m_q²). The first line of (10), eq. (11), dimensional analysis, and the stated ∫d²k_T(I₁+I₂) = 0 all require
  - I₁(k_T) = 𝒩F(k_T)², with F(k_T) = ∫d²l_T/[(l_T²+m_g²)((k_T−l_T)²+m_q²)];
  - I₂(k_T) = −𝒩G(k_T)/(k_T²+m_q²), with G(k_T) = ∫d²l₁d²l₂/[(l₁²+m_g²)(l₂²+m_g²)((k_T−l₁−l₂)²+m_q²)];
  - 𝒩 = λ²g₁²g₂(g₂+g₁)x(1−x)/(256π⁷).

  With these forms the k_T integral of I₁+I₂ vanishes exactly, while I₁(0)+I₂(0) < 0 (e.g. −21.0𝒩 at (m_g,m_q) = (0.5,1)). The first line of (10) also lacks two squares and carries +iε on the conjugate side of the cut."
