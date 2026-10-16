# Verification batch N25–N29 (stage 1, independent verifier)

Date: 2026-10-10. Default stance: skeptical. All five claims are of kind `new_result`; none claims novelty.
For each claim I (i) re-ran the project scripts named in the recipe, (ii) re-derived or re-computed the statement myself with new code and, where possible, by a different route, and (iii) read the cited literature (arXiv sources and PDFs downloaded fresh into my scratch area and treated as untrusted text; equation numbers taken from the arXiv PDFs) and checked bibliographic data on INSPIRE.

## 0. Method and sources

**Project scripts re-run** (outputs in `verify/claims/batch_N25_s1_scripts/rerun/`). All reproduce exactly.
* `research/c_dy/plus_trap.py`: c = 1.75 = 7/4. `research/c_dy/glauber_toy.py`: 25/25 PASS.
* `research/c_wilson/scripts/s2_eikonal_identity.py`: 44/44 PASS.
* `frontier/lamet/scripts/s2_ft_testfunctions.py`: 44 PASS / 0 FAIL. Of these, 20 are the MS-bar/ratio comparisons (|diff| from 1.9e−12 to 7.9e−9) and 24 are hybrid-scheme checks.
* `frontier/others/scripts/s3_luxqed_pointlike.py` 3/3, `s4_resummed_series.py` 8/8, `s5_bk_kernel.py` 5/5, plus `s2_crs_yukawa_pdf.py` 10/10.
* `frontier/yzliu/scripts/check_HL_and_C1.py`: the one-loop identity gives 0, and (C.1) agrees to 12 digits for n = 2, 3, 4.
* `check_gammaC2.py`: (A.6) and (A.11)⇒(A.13) both give 0.
* `check_GN_ineq.py`: maximum ratios 0.99876, 0.9999991, 0.99998, 0.999997, all ≤ 1.

**My own scripts** are in `verify/claims/batch_N25_s1_scripts/`, with logs. Run them with `python3 -I`.
* `n25_glauber_plus.py` (18/18 PASS). χ(b) by Schwinger parametrisation. The sign is fixed symbolically from the Gaussian functional. All contour integrals are done on the real axis at finite Feynman ε with ε → 0 (no indented contours). Residue bookkeeping for shifted contours. Past/future Wilson-line rules. Plus trap with four test functions, plus a test of the literal claim text.
* `n26_eikonal.py` (7/7 PASS). Explicit numerical ordered multiple integrals of the damped abelian line for m = 2, 3. Necessity of additive regulators, symbolic for m = 2, 3. Distributional limit of the uniform-ε defect.
* `n27_lamet_ft.py` (63/63 PASS). Two routes, both different from the project's s2:
  * Method A works in ξ-space and needs no ζ integral: FT[ln ζ²] = −2γ_E δ − [1/|u|]_R is applied to the decomposition 𝒞 = A L + B.
  * Method B works in ζ-space, with closed-form Φ(ζ) (Bessel K) for Lorentzian and power-law test functions and a closed form for G(ζ) (Ein/E1 functions, small-ζ series).
  * The test functions include ones decaying only like |x|^−0.4 and |x|^−0.7. Momentum RGE checked symbolically.
* `n28_others.py` (17/17 PASS). BNS tower from their eqs. (14) and (19). LN identity to n = 15. LUXqed point-like limit derived symbolically. CRS integrand re-derived from the Dirac trace. BK eigenvalue by my own 2D quadrature.
* `n29_yzliu.py` (22/22 PASS). One-loop H decomposition. c_H numerics. Anomalous-dimension algebra, with γ_V and γ_J checked against Becher–Neubert–Pecjak (read). γ̃_J against Jain–Scimemi–Stewart (read). Liu–Su residue, and N_m by an independent large-β₀ static-self-energy computation. D-relations. (C.1) at finite η. 6000-point test of the GN inequalities and an analytic proof of (4.4)–(4.5).

**Literature read** (arXiv sources and PDFs):
* Collins, *Foundations of perturbative QCD*, ch. 14, pp. 540–572 (Cambridge open-access chapter PDF, DOI 10.1017/9781009401845.014).
* IJJSZ arXiv:1801.03917 (PRD 98 (2018) 056004).
* Ji et al., RMP arXiv:2004.03543 (RMP 93 (2021) 035005).
* Ji et al., hybrid scheme arXiv:2008.03886 (NPB 964 (2021) 115311).
* Radyushkin arXiv:1705.01488, 1710.08813, 1801.02427.
* Becher–Neubert–Shao arXiv:2107.01212.
* Liu–Neubert arXiv:1912.08818.
* Manohar–Nason–Salam–Zanderighi arXiv:1607.04266.
* Frixione arXiv:1909.03886.
* Collins–Rogers–Sato arXiv:2111.01170.
* Ji–Liu–Su arXiv:2305.04416.
* Liu–Su arXiv:2311.06907.
* Liu arXiv:2312.05957 and arXiv:2403.06787.
* Ebert–Stewart–Zhao arXiv:1811.00026.
* Ji–Liu–Liu arXiv:1910.11415.
* Jain–Scimemi–Stewart arXiv:0801.0743.
* Becher–Neubert–Pecjak hep-ph/0607228.
* Chay–Kim–Kim–Lee hep-ph/0412110.

**INSPIRE checks.** All texkeys in the five claims resolve to the stated papers: Becher:2021zkk, Liu:2019oav, Manohar:2016nzj, Frixione:2019lga, Collins:2021vke, Balitsky:2007feb, Ji:2023pba, Liu:2023onm, Liu:2023pjb, Liu:2024omb, Ebert:2018gzl, Izubuchi:2018srq, Ji:2019sxk, Collins:2011zzd and Bodwin:1984hc. There are two exceptions:
* Ji:2020brr is the hybrid-scheme paper, not the source of the momentum RGE (see N27).
* Frixione:2019lga has a single author, not "Frixione et al.".

## 1. Summary

| id | verdict | new? | what must change before printing |
|---|---|---|---|
| N25 | **confirmed, after correction of a formula** | No. Collins 2011 §14.3 (Glauber region example: S–S pinch, cancellation after the sum over cuts, no pinch at the active-parton end) and §14.4.1 item 5 (DY eikonal lines are past-pointing); eikonal phase classical. | **The plus-trap formula in the claim text is mis-transcribed and false as written.** It must read (1+z²)𝒟₁ = [(1+z²)ln(1−z)/(1−z)]₊ + (7/4)δ(1−z). (c_dy §3.10, VF-DY-12 and FINAL_OUTLINE all have it right; only CLAIMS.md and the task text drop the ln(1−z).) "First term" vs "cancels after the k_T integral" wording: see §2.5. |
| N26 | **confirmed** | No; elementary (abelian exponentiation with a damping on each insertion). | Precise form: the identity is exact at finite regulator **iff** the cumulative regulators are additive. With equal per-gluon damping this means "j-th denominator carries ijε", i.e. the adiabatic e^{−ε\|s\|}. A uniform iε, which is what eikonalised Feynman propagators give, fails at O(ε). |
| N27 | **confirmed** | No. It is a numerical confirmation of the Fourier relation that IJJSZ themselves used to derive eqs. (65)/(68)/(70) from (62). | (a) The momentum RGE with −(3/2)δ is RMP eq. (32), [Ji:2020ect], **not** [Ji:2020brr]. (b) Accuracy is 2e−12 to 8e−9 (project) and ≤7e−8 (mine, including slowly decaying test functions), not "1e−9 to 1e−12". (c) Add Radyushkin PRD 98 (2018) 014019 eq. (17) for the ratio kernel. |
| N28 | **confirmed** (all five transcriptions) | No (transcriptions). | (i) "First term" means the first **super-leading** term (n = 1); the n = 0 term is single-logarithmic. (iii) The LUXqed result equals Frixione (4.189) only at leading power; the αm²x²(1−x)/(πμ²) term is a power correction beyond both. Frixione is single-author. |
| N29 | **confirmed** (all items) | No (cross-checks of published formulas). | (iii) is printed explicitly as JLS eq. (3.13) and equals −γ₁ of JSS 2008. (iv) N_m = C_Fe^{5/6}/π is Liu–Su eq. (2.50); eq. (2.52) holds the conjectured beyond-large-β₀ values. (i) holds at O(α_s) only. |

## 2. N25 — abelian DY Glauber toy; plus trap

### 2.1 χ(b) (G-i)
For a free abelian field, ⟨T e^{i∫J·A}⟩ = exp(−½∫∫J D J). The cross term, with v_A=(1⁺,0⁻,0_T), v_B=(0⁺,1⁻,0_T), v_A·v_B=1 and the Feynman propagator −ig_{μν}/(k²−m²+i0), is
−g_Ag_B∫d⁴k/(2π)⁴ (−i)/(k²−m²+i0) e^{−ik·b}(2π)²δ(k⁺)δ(k⁻) = −i g_Ag_B ∫d²k_T/(2π)² e^{ik_T·b}/(k_T²+m²).
* Hence χ(b) = −(g_Ag_B/2π)K₀(m|b|) (symbolic check, n25 (1b)).
* The 2D Fourier transform was checked independently by Schwinger parametrisation (max relative deviation 7.8e−17).
* Self-energies ∝ v² = 0.
* The one-loop momentum-space kernel was re-derived. The k⁻ integral at finite ε converges linearly in ε to the residue value: rel. dev. 6.1e−3, 6.1e−4, 6.1e−5 for ε = 1e−4, 1e−5, 1e−6. The trapped pair s_A (UHP), a (LHP) closes on s_A. Assembly gives −ig_Ag_B/(k_T²+m²). ✓

### 2.2 S–S trapping and cancellation (G-ii, G-iii)
* **Trapping.** At fixed k⁻ the k⁺ poles of s_B (κ_s−i0) and b (κ_b+i0) lie at |k⁺| ~ λ² on opposite sides. On the real axis at finite ε the value equals the Glauber-scale residue: value/residue = 1.000000000. The boson-pole residue is O(λ²) relative (7.9e−3 for λ = 0.1).
* Shifting the contour by ±iλ/3 changes the value by exactly the crossed residues, including the far boson pole when it is swept. The bookkeeping holds to 2.1e−7 at ε = 1e−9 and to 2.1e−5 at ε = 1e−7, i.e. linearly in ε. So the contour cannot leave the Glauber region: it is pinched. ✓
* **Cancellation.** In the toy, the S–S exchange shifts only the spectators' relative momentum. The cut sums Σ_j (iχ)^j(−iχ)^{n−j}/(j!(n−j)!) vanish, and |e^{iχ}|² = 1 by Parseval (project G3/G5, re-run). ✓

### 2.3 Active–spectator exchange (G-iv)
* **Formula.** I_as(k⁻) = ∫dk⁺[(2p_b⁻k⁺+c_b+i0)(2k⁺k⁻−K²+i0)]⁻¹ = 2πiθ(−k⁻)/(2p_b⁻K²+2k⁻c_b). Confirmed by:
  * a sympy residue (only the boson pole is in the UHP, and only for k⁻ < 0);
  * real-axis finite-ε integration: 242.3320i vs 242.3320i at k⁻ = −0.006; 243.9125i vs 243.9125i at k⁻ = −0.02; 0 for k⁻ > 0.
* **Saturation.** The integral is saturated by the boson pole at k⁺ = K²/(2k⁻) ≈ −1.08, i.e. |k⁺| ~ Q, the A-collinear region.
* **Eikonal replacement.** Replacing b by the eikonal line 1/(2p_b⁻k⁺+i0) changes the result by |k⁻c_b/(p_b⁻K²)| = 2.8e−3 = O(λ²).
* **Past-pointing identification.** With k flowing into b, the eikonal propagator is i/(n_B·k+i0). That is the Feynman rule of the past-pointing line W[0,−∞n_B]: ∫_{−∞}^0 dλ e^{−i(n·k)λ+ηλ} = i/(n·k+iη). A future-pointing line would give −i/(n·k−i0).
* This agrees with Collins §14.4.1 item 5 ("the eikonal denominators correspond to past-pointing Wilson lines", Drell–Yan) and §14.3.4 (a gluon attached to an active parton "does not give a Glauber pinch. Therefore we can deform the integration out of the region"). ✓

### 2.4 Plus trap — transcription error
* **Correct statement.** In the product convention g𝒟_k = g(1)𝒟_k + (g−g(1))ln^k(1−z)/(1−z):
  (1+z²)𝒟₁ − [(1+z²)ln(1−z)/(1−z)]₊ = −∫₀¹(1+z)ln(1−z)dz · δ(1−z) = (7/4)δ(1−z).
  This was checked symbolically and with four test functions, giving exactly 7/4. Hence 4C_F(1+z²)𝒟₁ vs the whole-term plus differ by 7C_Fδ(1−z): δ coefficient C_F(2π²/3−8) ↔ C_F(2π²/3−1). ✓
* **As written in the claim** ("(1+z²)𝒟₁ vs [(1+z²)/(1−z)]₊ differ by (7/4)δ(1−z)") the statement is **false**. The difference is not a multiple of δ(1−z): its ratio to h(1) is 14.33, −1.5, 1.92, 2.52 for four test functions. The source files are correct: c_dy DERIVATION §3.10 item 1, spec VERIFIED_FORMULAS(_v2) VF-DY-12 and FINAL_OUTLINE(_v2). The error is confined to CLAIMS.md N25 and the condensed task text.

### 2.5 Literature, novelty, wording
* **Collins 2011 §14.3** (pp. 545–552) has the "Glauber region example": a spectator–spectator exchange in a DY model, the k± integrals closing on final-state spectator poles, cancellation after the sum over cuts (14.11)–(14.16), and "to get a Glauber pinch … one must have an exchange attached to both the spectator parts" (§14.3.3).
* **Collins §14.4** gives the general proof following CSS 1988 (NPB 308, 833), which "supersedes earlier work (Bodwin, 1985; Collins, Soper, and Sterman, 1985a)". I could not read Bodwin, PRD 31 (1985) 2616 [Erratum PRD 34 (1986) 3932] directly; it is cited correctly as the original treatment.
* Explicit one-loop spectator analyses also exist: Bodwin–Brodsky–Lepage, PRL 47 (1981) 1799, and Collins–Soper–Sterman, PLB 109 (1982) 388.
* **Wording.** "Cancels after the k_T integral" must say: after integrating over the spectators' *relative* transverse momentum (the total, −q_T, is untouched). Grade [P] (model, one loop) is appropriate.

## 3. N26 — eikonal identity and the regulator

* **Direct construction (n26 (1)).** I numerically integrated the ordered multiple integrals of the abelian line W[0,−∞n] with damping e^{εs} (s<0) on every attached field, for m = 2 (three parameter sets) and m = 3, and summed over orderings. The sum equals Π_j i/(a_j+iε) and the cumulative formula with +ijε, with |diff| ≤ 2e−12.
* **Uniform prescription.** The cumulative formula with a uniform +iε differs by 0.14–0.67. It equals the ordered integral damped only by the farthest attachment, e^{ε s_min}, which is not a product of single-field factors (diff 1.8e−12).
* **Necessity (n26 (2)).** For general cumulative shifts a_S → a_S + iη(S):
  * at m = 2 the defect is i(η₁+η₂−η₁₂)/[(a₁+iη₁)(a₂+iη₂)(a₁+a₂+iη₁₂)], so the identity holds for all real a iff η₁₂ = η₁+η₂;
  * at m = 3, additive shifts are exact and a non-additive triple shift breaks the identity.
  * With equal per-gluon shifts, "j-th denominator carries ijε" is therefore necessary and sufficient. With unequal per-gluon dampings, any additive set works.
  * Uniform η gives the defect +iε/[(a₁+iε)(a₂+iε)(a₁+a₂+iε)] (−iε/[…] with the propagator factors i included, as in c_wilson §3.1).
* **Distributional limit (n26 (3)).** Paired with a smooth 2D test function, the m = 2 uniform defect is 0.966, 0.628, 0.360, 0.193 for ε = 0.2, 0.1, 0.05, 0.025. It tends to 0, so the identity holds only distributionally as ε → 0. ✓
* **Physics.** Eikonalised Feynman propagators i/(2p·K+iε₀) carry a uniform ε₀, which does not scale with the number of absorbed gluons. The uniform convention is common in print, e.g. Chay–Kim–Kim–Lee, PRD 71 (2005) 056001, eq. for Y, where the identity is used only as ε → 0.
* **Verdict.** Confirmed. The claim's "only" is correct within the class of regulators with equal damping per insertion; for a general statement use the additivity criterion. Not new.

## 4. N27 — LaMET one-loop kernels as Fourier transforms

* **Transcription.** LAMET §4.6(a),(c) reproduces IJJSZ exactly (arXiv numbering):
  * coordinate kernel: eq. (62), with ΔC_{γ^z} = 2a(1−α) from eq. (63);
  * MS-bar momentum kernel: eq. (68), which is eq. (65) with the δ-functions at ξ=±∞ dropped and [3/(2ξ)]_{+(∞)} → 3/(2ξ);
  * ratio kernel: eq. (70); γ^z additions: eqs. (69), (71);
  * FT of ln ζ²: eq. (59).
  The ratio kernel also agrees with Radyushkin PRD 98 (2018) 014019, eq. (17), "in agreement with a recent result" of IJJSZ.
* **Method A** (ξ-space; 48 comparisons): 2 schemes × 2 Γ × 6 test functions × 2 values of ℓ. Agreement is within 2e−10–4.4e−9 for Gaussians (including one centred at x = 1) and Lorentzians, and within 2.6–7.3e−8 for φ = (1+((x−0.5)/0.8)²)^{−0.35} (tail |x|^{−0.7}).
* **Method B** (ζ-space with closed-form Φ; 12 comparisons): agreement within 3.9e−10–3.6e−9 (Lorentzian), 5.4–7.3e−8 (|x|^{−0.7}) and 7.5e−12–2e−9 (|x|^{−0.4}).
  * A first version of Method B lost precision through catastrophic cancellation at small ζ. With power series for |ζ| < 1 all comparisons pass; the old discrepancies were numerical.
  * Since the slowly decaying test functions agree, the δ-functions at ±∞ dropped by IJJSZ do not contribute for test functions vanishing like any power at infinity. This is consistent with IJJSZ's argument for PDFs ~ y^{−1+a}, a > 0.
* **Momentum RGE.** With ℓ_p = ln(μ²/4p_z²), dℓ_p/dlnP^z = −2. Only the 0<ξ<1 term and the δ term depend on ℓ_p, which gives
  P^z dC^{MS}/dP^z = 2a[((1+ξ²)/(1−ξ))₊ − (3/2)δ(1−ξ)] = (α_sC_F/π)[…]. This is exactly RMP 2004.03543 eq. (32).
  * In the ratio scheme the −(3/2)δ is absent.
  * RMP eq. (32) was derived with a transverse-momentum cutoff. There, the P^z-dependence of the linearly divergent Λ_UV/((1−y)²P^z) terms of RMP (unpolvertex) is not shown, so in MS-bar the statement is cleaner.
  * **Attribution:** the momentum RGE is in [Ji:2020ect], RMP 93 (2021) 035005, eq. (32). [Ji:2020brr] (2008.03886, hybrid scheme) contains no momentum RGE (grep of the source).
* **Novelty.** IJJSZ derived the momentum kernels from the coordinate kernel by exactly this Fourier transform: "C and 𝒞 … automatically satisfy the relation" (text after eq. (69)). The claim is an independent numerical confirmation, not a new result.

## 5. N28 — OTHERS checked transcriptions

* **(i) BNS (PRL 127 (2021) 212002).**
  * From eq. (14) (σ̂_n^SLL) and eq. (19) (C_rn^(S)) with J₂ = J₄₃/2 = ΔY, only r = 0 contributes. Term by term for n = 0..12 this gives −σ̂_B(4C_F/3π)α_s³L³ΔY ₂F₂(1,1;2,5/2;−w), w = N_cα_sL²/π, which is their eq. (21).
  * The general-n identity also follows by hand from (5/2)_n = (2n+4)!/(3·4^{n+1}(n+2)!).
  * n = 0 gives −σ̂_B(4C_F/3π)α_s³L³ΔY, which is single-logarithmic. The first SLL is n = 1: σ̂_B(4/(15π²))C_FN_cα_s⁴L⁵ΔY.
  * Asymptotics (Mellin–Barnes double pole): ₂F₂ = (3/2)(ln w − ψ(3/2))/w + …, with relative deviation 2.7e−10 at w = 1e8, where w·₂F₂/ln w = 1.4970. ✓
* **(ii) Liu–Neubert (JHEP 04 (2020) 033).**
  * Eq. (3) (read) holds exactly: 2n!/(2n+2)! = 4^{−n}/((n+1)(3/2)_n), checked for n ≤ 15 and in general by hand.
  * The n = 0, 1 terms L̂²/2 and (C_Fα_s/4π)(−L̂⁴/12) are the leading logs of eq. (1) (read). ✓
* **(iii) LUXqed eq. (6) (read)** on a point-like Dirac target, with the elastic δ at z = x counted fully, gives exactly xf_γ = (α/2π)[1+(1−x)²][ln(μ²/m²) − 2lnx − 1] + αm²x²(1−x)/(πμ²) (symbolic).
  * Frixione (1909.03886) eq. (4.189) (read; Γ = Γ^[0] + (α/2π)Γ^[1], K_γe = 0 in MS-bar) is the leading-power part.
  * Without F_L: +(α/2π)4(1−x) (exact difference (α/π)(1−x)(2 − 2m²x²/μ²)). Without the MS-bar conversion term: +(α/2π)x². ✓
* **(iv) CRS (PRD 105 (2022) 076010)**, eqs. (55)–(59) (read).
  * I re-derived the integrand from the Feynman rules: (1/4)Tr[γ⁺(k̸+m_q)(P̸+M)(k̸+m_q)] = P⁺[k_T²+(m_q+ξM)²] on the scalar mass shell, and k²−m_q² = −(k_T²+Δ)/(1−ξ), giving a_λ(1−ξ)∫dk_T²[k_T²+(m_q+ξM)²]/[k_T²+Δ]².
  * The DR expansion 1/e + [−lnΔ − 1 + c/Δ] gives (55).
  * Sign structure: negative for ξ ∈ [0.27, 0.99] at μ = 0.8 GeV, positive for all ξ at μ = 2.5 GeV. ✓
* **(v) BK.** My own 2D quadrature of the dipole kernel on (r²)^γ gives χ(γ) = 2ψ(1)−ψ(γ)−ψ(1−γ) for γ = 0.3, 0.5, 0.7 (to < 1e−6), and χ(½) = 4ln2 exactly. Balitsky–Chirilli PRD 77 (2008) 014019 is a fine general reference; the χ(½) = 4ln2 intercept is classic BFKL. ✓

## 6. N29 — YZLIU cross-checks

* **(i) One-loop H.**
  * C_HL^+C_HL^- = 1 + (α_sC_F/2π)(−2+π²/12−L_z²/2+L_z). This equals JLS eq. (4.11), ESZ eq. (kernels_nlo) [C^{(1)} = −L²+2L−4+π²/6, read] and APPB.
  * (C_HL^±)² = JLS eq. (4.2), with phase (α_sC_F/2)(1−L_z).
  * 𝒢^(1) = 2∂_{L_z}H^(1) = (α_sC_F/π)(1−L_z). ✓
* **(ii) c_H.**
  * The closed form is JLS eq. (5.11) verbatim (read). Numerically it is 0.072518C_F² − 0.084043C_FC_A + 0.145307C_Fn_fT_F, matching eq. (5.12).
  * Its n_f part with T_F = ½ equals the independent large-β₀ result of Liu–Su eq. (2.42).
  * (A.11) with (A.2)–(A.5) reproduces (A.13). The n_f part of γ̃_H^(2) equals Liu–Su eq. (2.41). ✓
* **(iii) γ̃_J^(2).** 2γ_HL − 2γ_s from JLS (A.5), (A.4) gives C_FC_A(−1396/27+23π²/9+20ζ₃) + C_Fn_f(232/27−2π²/9), in (α_s/4π)².
  * This is printed as JLS eq. (3.13). It equals −γ₁ of the bHQET jet function in Jain–Scimemi–Stewart, PRD 77 (2008) 094008 (read: γ₁ = [1396/27 − 23π²/9 − 20ζ₃]C_FC_A + [2π²/9 − 232/27]C_Fn_f).
  * Inputs cross-checked: JLS (A.3) γ_V = BNP γ₁^V (read), and γ_V/2 − γ_s/2 = BNP γ₁^J (read), which independently confirms (A.4). ✓
* **(iv) N_m.**
  * From Liu–Su eq. (2.46), the residue at u = ½ is (μ/p^z)C_Fe^{5/6}/(2π), which is their eq. (2.47).
  * With B(u) = Σ(t^n/n!)c_n, u = β₀t/2, and the factor 2 for the pair (their eq. (2.48)), this gives r_n = N_mβ₀^n n! with N_m = C_Fe^{5/6}/π = 0.976564, their eq. (2.50).
  * Independent check: the large-β₀ static self-energy δm = (C_F/π)∫₀^μ dk α_V(k), α_V = α/(1+β₀α(ln(k/μ)−5/6)), has coefficients whose ratio to (C_Fe^{5/6}/π)β₀^n n! μ tends to 1 (1 − 1.6e−9 at n = 10, 1 − O(1e−17) at n = 20). So N_m is indeed the large-β₀ pole-mass/linear-divergence normalisation.
  * The claim cites (2.52); that equation lists the *conjectured* beyond-large-β₀ values 0.622…0.524. ✓
* **(v) D-relations.** S_I = S₂/(S₁S₁) = e^{−𝒟} (Ji–Liu–Liu 2019, eq. (SSS) and the text below it: "2𝒟₁ − 𝒟₂ = 𝒟"; read) gives 𝒟₁ = (𝒟+𝒟₂)/2, trivially. ✓
* **(vi)–(viii)**, from CLAIMS.md:
  * (C.1) of Liu 2312.05957 (read) was verified by direct finite-η E-integration (η = 1e−6, rel. dev. 4e−7, 1.2e−6, 4.5e−6 for n = 2, 3, 4, consistent with O(η) corrections) and holds analytically: the difference of products is 2πiΣ_kδ(E−E_k)Π_{j≠k}(E_k−E_j)^{−1}.
  * GN inequalities (4.2)–(4.5) of 2403.06787 (read; same ranges): maximum ratios over 6000 random points ≤ 1. (4.4) and (4.5) are proved termwise from the Weierstrass product.
  * One-loop threshold: the IJJSZ kernel gives (α_sC_F/2π)·2/(1−y)·(L_z+ln(1−y)−1) for y<1 and 2ln(y−1)/(y−1) for y>1, which equals JLS (4.10). ✓

## 7. Reproduction
`cd "…/verify/claims/batch_N25_s1_scripts"` then `python3 -I n25_glauber_plus.py` (≈12 s), `n26_eikonal.py` (≈22 s), `n27_lamet_ft.py` (≈6 s), `n28_others.py` (≈9 s), `n29_yzliu.py` (≈13 s). Logs: `*.log`. Project re-runs: `rerun/`.
