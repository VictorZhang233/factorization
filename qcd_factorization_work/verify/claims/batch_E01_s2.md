# Verification batch E01–E06 (stage 2, second independent verifier)

Date: 2026-10-11. Stance: skeptical; the stage-1 report (`batch_E01_s1.md`) was read only after my own reading/derivations and was
not used as a source. Notation: a = α_s C_F/(2π).

## 0. Method and sources

* **Fresh downloads** (new scratch directories, read as text only; Python run with `-I`; nothing executed from download dirs):
  * arXiv e-prints (latest versions, version history checked on the abs pages): 2008.03886 (v2), 2004.03543 (**v2 is the latest**;
    there is no v3), 2209.01236 (v1, v2), 2204.08343 (v4), 1911.03840 (v2), 2106.05310 (v1, only version), 1811.00026, 2201.08401,
    1810.00048, 1801.03917, 1706.08962, 1707.07152, 1705.11193 (v4), 1305.1539, 1710.01089, 1910.11415, 2010.06623, 2311.06907 (v3),
    1506.00248, plus some citing papers (2112.02208, 2103.02965, 2011.09788, 2201.09173, 2206.04084, 2102.01101, 2112.07519,
    2008.12474, 2011.14971, 2609.40205, 2401.08012, 2004.14831).
  * arXiv PDFs: RMP v2 (2004.03543v2, for equation numbers) and 2106.05310v1.
  * **Journal versions** (SCOAP3 repository API, `repo.scoap3.org/api/records/?doi=`; equations checked on rendered pages where it
    mattered): NPB 964 (2021) 115311; NPB 991 (2023) 116201; PRD 106 (2022) 014507; PLB 811 (2020) 135946; PRD 105 (2022) 076014;
    PRD 99 (2019) 014013; PRD 99 (2019) 034505; PRD 98 (2018) 056004; PRL 120 (2018) 112001; PRL 121 (2018) 022004;
    APPB 53 (2022) 4-A2 (journal site PDF).
  * Not accessible: RMP 93 (2021) 035005 journal PDF (APS returns 403; not in SCOAP3) → arXiv v2 used; PRL 110 (2013) 262002 → arXiv;
    PRD 96 (2017) 054506 → arXiv v4.
* INSPIRE API: publication data; citing-paper lists; full-text searches (`refersto:recid:… and fulltext:"typo"/"misprint"/…`).
* My scripts (copied to `verify/claims/batch_E01_s2_scripts/`, run with `python3 -I`): `e01_lorentz.py`, `e01_plusR3.py`,
  `e02_qtmd_1loop.py`, `e02_lfwf_i0.py`, `e03_bvz.py`, `e03_exact_eval2.py`, `e03_negx.py`, `e06_check.py` (+ `scoap3_get.py`, `show_inspire.py`).
* Project scripts named in the recipes were re-run: `frontier/lamet/scripts/s2_ft_testfunctions.py` **44 PASS / 0 FAIL**
  (agreement 2·10⁻¹² … 2·10⁻¹⁰), `frontier/lamet/scripts/s4_tmd_bvz.py` **20 PASS / 0 FAIL**, `frontier/yzliu/scripts/check_qtmd_1loop.py`
  (c = ½ residual 0; c = 1 residual L_b(L_z − L_ζ)).
* Methods deliberately different from stage 1: Lorentzian test functions with closed-form (E₁) pairings (E01); explicit i0 bookkeeping
  in the LFWF one-loop check and a cross-source one-loop check with ESZ inputs (E02); closed-form analytic derivation of x²F″ plus exact
  sympy integration for polynomial PDFs and direct numerical differentiation (E03); my own derivation of the sail link vertex and of
  the UV-pole count from IJJSZ eq. (43) (E04); a toy smooth coordinate kernel to test the parton-momentum change of variables (E06).

## 1. Summary

| id | verdict | what must change before printing | in the literature? |
|---|---|---|---|
| E01 | **confirmed** | Not new: first published by Chou & Chen 2022. Su et al. eq. is **(A.14)** (arXiv label `eq:hybridkernelNLO`), not "(C1 hybrid)". Write λ_S = z_S\|p^z\|. RMP numbers are arXiv **v2** eqs. (120)–(121). | **Yes**: Chou–Chen PRD 106 (2022) 014507 eq. (35) + remark after eq. (37); Su et al. NPB 991 (2023) eq. (A.14). |
| E02 | **confirmed (core: missing ½)**, with two corrections | (i) Remove the published **PRD 105 (2022) 076014** from the erratum list: it has the ½ in eqs. (49), (51), (74) and footnote 1; only arXiv:2106.05310v1 eqs. (49), (51), (73) lack it. (ii) **New finding**: the LFWF formula in the claim copies the printed i0 "(∓ζ_z − i0)", which for ψ⁺ is inconsistent with PRD 105's own one-loop eqs. (63), (69), (72), (75), (76); consistency requires (∓ζ_z **+** i0), as printed later by Liu–Su JHEP 2024, 204. | Yes (by the authors): PRD 105 fn. 1; correct forms ESZ 2019 eqs. (24),(27); ESSZ 2022; APPB eq. (52) itself. |
| E03 | **confirmed** (x > 0) | Journal eq. numbers (55), (60)–(64). The 31.6 %/24.0 % refer to BVZ model (60). For general x the braces need "−x q′(x)" (BVZ's "−\|x\|q′" is wrong for x < 0; Liu–Chen 2021). | The (64) omission: not found. |
| E04 | **confirmed**, sharper reason | Eq. (5) is the inconsistent one (vertex −igT^aγ^μ ⇒ D = ∂ + igA ⇒ link should be P exp(+ig∫dz′A^z)). "Harmless" because IJJSZ's eq. (41) integrands use the consistent link, **not** because O(g²) is sign-insensitive (sail diagrams flip; UV coefficient 3/2 → −1/2). | Not found. |
| E05 | **confirmed** | Add "at O(a⁰)" (O(a) mixing with dimension-4 operators exists for all Γ, even with chiral fermions). | Physics: CP 2017, Chen et al. CPC 2019, GJS 2018 (RMP 2021). Remark on JZZ's sentence is editorial. |
| E06 | **confirmed** | Precise O(α_s) difference: C(μ/P^z) − C(μ/(\|y\|P^z)) = −(α_sC_F/π) ln\|y\| (1+ξ²)/(1−ξ)₊ θ(0<ξ<1) = −(α_s/π) ln\|y\|[P_qq − (3/2)C_Fδ(1−ξ)] (MS-bar, IJJSZ eq. (68)); ratio scheme: −(α_s/π) ln\|y\| P_qq. Range ∫_x^1 also incomplete. | **Yes**: IJJSZ 2018 (text after eq. (27)); Ji–Schäfer–Xiong–Zhang PRD 92 (2015) 014039 (quasi-GPDs). |

## 2. E01 — hybrid-scheme kernel

### 2.1 Printed (journal NPB 964 (2021) 115311, page 12 rendered; identical in arXiv source label `eq:hybridm2`)
* eq. (30): 𝒞_hybrid(α, z²μ², z²/z_S²) = 𝒞_ratio(α, z²μ²) + δ(1−α)(α_sC_F/2π)(3/2) ln(z²/z_S²) θ(|z| − z_S).
* eq. (32): Z^MS_ratio = 1 − a[(3/2) ln(z²μ²/(4e^{−2γ_E})) + 5/2].
* eq. (33): C_hybrid(ξ, μ²/(p^z)², z_S²μ²) = C_ratio(ξ, μ²/(p^z)²) + (α_sC_F/2π)(3/2)[ −1/|1−ξ|₊ + 2Si((1−ξ)λ_S)/(π(1−ξ)) ],
  "ξ = y/x, λ_S = z_S p^z with p^z = xP^z being the parton momentum".
* eq. (34): 1/|1−ξ|₊ ≡ lim_{β→0⁺}[ θ(|1−ξ|−β)/|1−ξ| + 2δ(1−ξ) ln β ].
* RMP (arXiv 2004.03543 **v2**, PDF): the same formula as eqs. **(120)–(121)** (label `eq:hybridm2`). Journal RMP not accessible.

### 2.2 Independent derivation (Lorentzian test functions, closed forms)
Let u = 1−ξ, g(λ) = ln(λ²/λ_S²) θ(|λ| − λ_S) (the coordinate correction at fixed parton momentum, λ = z p^z; θ(|z|−z_S) ⇒ λ_S = z_S|p^z|),
G(u) = ∫dλ/(2π) e^{iuλ} g(λ). The extra kernel is (3a/2) G(1−ξ).
* u ≠ 0 (Fubini form, ln(λ/λ_S) = ∫_{λ_S}^λ dt/t, Abel regularization): G(u) = −(2/(πu))∫_{λ_S}^∞ sin(ut)/t dt = −1/|u| + 2Si(uλ_S)/(πu).
  Numerical check with e^{−ε|λ|}, ε = 10⁻⁸: agreement ~10⁻⁷ at 9 points (ε-limited).
* g is continuous, vanishes for |λ| < λ_S (so no δ-terms at ξ = ±∞ and no δ′), grows like ln|λ|; hence the exact distribution is the
  regularized −1/|u| + 2Si(uλ_S)/(πu) plus c δ(u), with c fixed by ⟨G,1⟩ = g(0) = 0.
* Test function φ_R(u) = R²/(R²+u²), Φ_R(λ) = πR e^{−R|λ|}:
  exact ⟨G, φ_R⟩ = (R/2)∫ g e^{−R|λ|} dλ = **2E₁(λ_S R)** (closed form; checked against direct quadrature to 15 digits).
  Printed prescription: ⟨1/|u|₊, φ_R⟩ = **2 ln R** exactly, and (4/π)∫_0^∞ Si(λ_S u)/(u(1+u²/R²)) du = **2[E₁(λ_S R) + ln(λ_S R) + γ_E]**
  (from d/da ∫Si(au)/(u(1+u²)) = (π/2)(1−e^{−a})/a). Hence printed pairing = 2E₁(λ_S R) + 2 ln(λ_S e^{γ_E}), i.e.
  **printed − exact = 2 ln(λ_S e^{γ_E}) φ_R(0) for every R** (units 3a/2). R → ∞: ∫G_exact = 0, ∫G_printed = 2 ln(λ_S e^{γ_E}).
* Shifted Lorentzians φ(u) = R²/(R²+(u−u₀)²) (exact pairing 2R Re[E₁((R−iu₀)λ_S)/(R−iu₀)]), 6 cases with λ_S ∈ {0.2, 0.5, 1, 2, 3.7}:
  (printed − exact)/(2 ln(λ_S e^{γ_E})φ(0)) = 1 within 3·10⁻⁹…2·10⁻⁸; plus-on-ℝ pairing − exact = 4·10⁻¹³…2·10⁻⁸ (truncation-limited).
* Direct ∫_{−U}^{U} of the printed bracket with U = 10⁴: equals 2 ln(λ_S e^{γ_E}) to 5·10⁻⁸ (λ_S = 0.5, 1, 2).
* Therefore printed C_hyb = exact + 3a ln(λ_S e^{γ_E}) δ(1−ξ), ∫dξ C_hyb = 1 + 3a ln(λ_S e^{γ_E}) (∫C_ratio = 1).
  At λ_S = 1: 3aγ_E = 0.110 (α_s = 0.3), 0.092 (α_s = 0.25) — "about 10 %" is right. The sign follows ln(λ_S e^{γ_E}).
* Vector-current conservation: h_hyb(z = 0) = h_ratio(0) = 1 ⇒ ∫dx q̃ = ∫dy q requires ∫dξ C = 1; violated by the printed form.
* Project script `s2_ft_testfunctions.py` (Gaussian test functions): 44/44 PASS.

### 2.3 Corrected form and its literature
* **Chou & Chen, PRD 106 (2022) 014507** (journal read): eq. (35) C^{hybrid-ratio}_{γ^t} = C^ratio + (3α_sC_F/4π)(−1/|1−ξ| + 2Si((1−ξ)|y|z_sP^z)/(π(1−ξ)))^{[−∞,∞]}_{+(1)};
  eq. (37) quotes Ji et al.'s term; text: "In addition to the difference between y and |y| in the argument of the Si function, quark number
  conservation is violated in the expression of (37) but is preserved in (35)." (arXiv v4 labels (28), (33).)
* **Su et al., NPB 991 (2023) 116201** (journal read): **eq. (A.14)** prints the same plus-on-ℝ form with Si[(1−ξ)|y|z_sP_z], citing [63] = Chou–Chen.
  No equation labelled "C1 hybrid" exists in either arXiv version or the journal.
* INSPIRE: the 35 papers citing Ji:2020brr before 2022-07 were listed; sources of the candidates (2112.02208, 2103.02965, 2011.09788,
  2201.09173, 2206.04084, 2102.01101, …) contain no momentum-space Si kernel; Gao et al. 2112.02208 use C⁻¹(x/y, μ/(yP^z), |y|λ_S) but do not print it.
  So Chou–Chen (April 2022) is the first published correction found.

### 2.4 Verdict
**Confirmed** as an erratum of NPB 964 eqs. (33)–(34) and RMP (arXiv v2) eqs. (120)–(121). The correction is already published (Chou–Chen 2022);
LAMET.md §14 item 1 must not call it a new result. Also λ_S must be z_S|p^z| (Si is odd).

## 3. E02 — Collins–Soper exponent in quasi-TMD / quasi-LFWF factorization

### 3.1 What is printed (read)
| source | version | printed | own consistency relations in the same source |
|---|---|---|---|
| Ji–Liu–Liu PLB 811 (2020) 135946 | journal (pp. 3–4 rendered) | eq. (22): f̃√S_r = H(ζ_z/μ²) e^{K ln(ζ_z/ζ)} f^TMD; text "exp[ln(ζ_z/ζ)K] is required" | eq. (7) 2ζ d ln f^TMD/dζ = K; eq. (12) 2ζ_z d ln f̃/dζ_z = K + G; eq. (13) K^(1) = −(α_sC_F/π)L_b; eq. (21) S^(1) = a[2−2(Y+Y′)]L_b; text "comparing (22) and (12), 2 d ln H/d ln ζ_z = G" (true only with ½) |
| RMP 93 (2021) 035005 | arXiv v2 | eq. (209): f^TMD = H e^{−ln(ζ_z/ζ)K} f̃ S_r^{1/2}; eq. (210): f̃(ζ_{z,1})/f̃(ζ_{z,2}) = [H(ζ_{z,2})/H(ζ_{z,1})](ζ_{z,1}/ζ_{z,2})^K | eq. (184) CS eq.; TMD evolution eq. with exp[½K ln(ζ/ζ₀)]; eq. (201) P^z d ln f̃/dP^z = K + 𝒢; eq. (212) 2ζ_z d ln H⁻¹/dζ_z = 𝒢 and eq. (213) h^(1) = a(−2+π²/12−L_z²/2+L_z) — both consistent only with ½ |
| Y. Liu APPB 53 (2022) 4-A2 | journal (pp. 21, 22, 32 rendered) | eq. (52) **correct** (e^{½ln(ζ_z/ζ)K}); eq. (53) ratio (ζ_{z,1}/ζ_{z,2})^{K}; eq. (75) e^{K ln(ζ_z/ζ)}; text "exp[ln(ζ_z/ζ)K] is required" | eq. (22) CS eq. ("S_I" = intrinsic soft function = S_r) |
| Ji–Liu PRD 105 (2022) 076014 | **journal** (pp. 12–16 rendered) | eq. (49) ψ̃^±_N√S_rN = **e^{½ ln((∓ζ_z−i0)/ζ)K_N}** H^±_N ψ^±_N; eq. (51) K_N = [**½** ln(ζ_z/ζ′_z)]⁻¹ ln(…); eq. (74) (N = 1) with **½**; **footnote 1**: "In front of the Collins Soper Kernel K_N there is a factor ½, which is missing in Refs. [22,23]" ([22] = RMP 93 035005, [23] = NPB 955 115054) | eq. (35) CS eq.; eq. (73) is Γ_S^(2) |
| same | arXiv 2106.05310v1 (PDF) | eqs. (49), (51), (73) **without** ½ | — |
| ESZ PRD 99 (2019) 034505 | journal | eq. (24) exp[½γ_ζ ln((2xP^z)²/ζ)]; eq. (27) γ_ζ = ln[…]/ln(P₁^z/P₂^z) | — |
| ESSZ JHEP 04 (2022) 178 | arXiv | eqs. `oldfact`, `factorization_statement`: exp[½γ_ζ ln(…)] | — |

NPB 955 (2020) 115054 (arXiv source) contains no explicit CS-exponent matching formula; footnote 1's reference [23] may be a mis-citation (not decidable).

### 3.2 All-order argument
LHS f̃√S_r is ζ-independent; with 2ζ∂_ζ ln f^TMD = K, ∂_{ln ζ} ln[H e^{cK ln(ζ_z/ζ)} f^TMD] = (½ − c)K ⇒ c = ½.
From the P^z side: 2ζ_z∂_{ζ_z}[ln H + cK ln ζ_z] = K + G ⇒ 2 d ln H/d ln ζ_z = G + (1 − 2c)K; H is b_⊥-independent ⇒ c = ½
(which is exactly the constraint the PLB states and RMP eq. (212) prints). Ratio at fixed x: (ζ_{z,1}/ζ_{z,2})^{K/2} = (P₁^z/P₂^z)^K.

### 3.3 One-loop checks (`e02_qtmd_1loop.py`)
* RMP inputs: K^(1) = S_r^(1) = −2aL_b (from eq. (207) with S_DY = e^{(Y+Y′)K+𝒟}, S_r = e^{−𝒟}); residual of
  f̃^(1) + ½S_r^(1) − [h^(1) + cK^(1)(L_z−L_ζ) + f^(1)] = **aL_b(L_z − L_ζ)(2c − 1)** ⇒ c = ½; with c = 1: **aL_b(L_z − L_ζ)**.
  2∂_{L_ζ}f^(1) = −2aL_b = K ✓; 2∂_{L_z}f̃^(1) = K + G with G^(1) = 2a(1 − L_z) ✓ (PLB eq. (14)).
* Cross-source: ESZ one-loop C^(1) = (α_sC_F/4π)(−L_z²+2L_z−4+π²/6) and g^S = 1 + aL_b (ESZ eqs. (25)–(26)) combined **with ½**
  reproduce RMP eq. (200) exactly: f̃^(1) = a[−½L_b² + L_b(5/2 − L_z) − 3/2 − ½L_z² + L_z].
* ESZ ratio estimator returns γ_ζ^(1) = −2aL_b = K^(1).

### 3.4 LFWF — including imaginary parts (`e02_lfwf_i0.py`; new relative to stage 1)
Inputs from journal PRD 105: eq. (63) ψ^± ⊃ aL_b(3/2 + ln(μ²/(±√(ζζ̄) − i0))); eq. (69) ψ̃^± ⊃ aL_b[5/2 + ln(μ²/(−√(ζ_zζ̄_z) ± i0))] + L_b-free terms;
eq. (72) S_r1^(1) = −2aL_b; eq. (60) K = −2aL_b; eq. (76) h^±(1) = α_s{c₁ + (C_F/4π)[ℓ_± + ℓ̄_± − ½(ℓ_±² + ℓ̄_±²)]}, ℓ_± = ln((−ζ_z ± i0)/μ²);
ζ_z/ζ = ζ̄_z/ζ̄. (I also re-derived eq. (63) from eqs. (54), (58), (59), (62): ψ⁺ has no iπL_b term, ψ⁻ has +iπaL_b.)
* Lower sign (ψ⁻): with c = ½ the full residual (including constants and imaginary parts, H from eq. (76)) is **0**.
* Upper sign (ψ⁺): with the printed exponent ½K ln((−ζ_z − i0)/ζ) the residual is **−2iπ aL_b** (b-dependent, cannot be in H);
  with ½K ln((−ζ_z + i0)/ζ) it is **0**. Equivalently, PRD 105's own H-RGE eq. (75) (±i0) agrees with "+i0" and not with "−i0".
* Liu–Su, JHEP 2024, 204 (arXiv:2311.06907v3, eq. `quai_fac_1`) print Ψ̃^± S_r^{1/2} = H^± e^{½ ln((∓ζ_z + i0)/ζ)K} Ψ^±, i.e. the consistent "+i0".
* Hence the claim's LFWF formula "ψ̃^±√S_r = e^{½ln((∓ζ_z−i0)/ζ)K}H^±ψ^±" has the right ½ but the wrong i0 for ψ⁺ (relative to the
  paper's own one-loop results). It must not be printed as "verified" in that form.

### 3.5 Verdict
**Confirmed** for PLB 811 eq. (22), RMP (arXiv v2) eqs. (209)–(210) [and, per the authors' footnote, the published RMP], APPB 53 eqs. (53), (75):
published formulas wrong, ½-corrected forms right. **Not** an erratum of the published PRD 105 (only of arXiv v1). LFWF i0 must read (∓ζ_z + i0).
Not new: the authors flag the missing ½ in PRD 105 fn. 1; correct forms in ESZ 2019, ESSZ 2022, APPB eq. (52).

## 4. E03 — Braun–Vladimirov–Zhang eq. (cR)

### 4.1 Printed (journal PRD 99 (2019) 014013, p. 9 rendered; same as arXiv)
eq. (55) [f(α)]₊ = f(α) − δ(ᾱ)∫_0^1 dβ f(β); eq. (60) q = x^{−1/2}(1−x)³; eq. (61) Q^∥ = q − (κv²Λ²/(pv)²)(d/dx)²∫_{|x|}^1(dy/y)(y+ȳlnȳ)q(x/y)
= q − (κv²Λ²/(x²(pv)²)){∫_{|x|}^1 (dy/y) y²/[1−y]₊ q(x/y) + q − |x|q′}; eq. (62) analogous (kernel +yȳ, braces [y²/[1−y]₊ − 2y²], +2q);
eqs. (63)–(64) "assuming x > 0": Q = q{1 − v²Λ²/(x²x̄(pv)²) R_Q}, R^∥_Q = (x̄/q){∫_x^1 dy/(1−y)[yq(x/y) − q] + q − xq′},
R^⊥_Q = (x̄/q){∫_x^1 dy/(1−y)[y(2y−1)q(x/y) − q] + 2q − xq′}. (−κv²/(pv)² = +κ/P_z² for v² = −1, so the claim's "q + κΛ²/(x²P_z²){…}" is the same.)

### 4.2 Independent analytic derivation (x > 0, q(1) = 0)
F(x) = ∫_x^1 (dy/y) k(y) q(x/y), k = y + ȳ ln ȳ, k(1) = 1, k′(y) = −ln(1−y). Then F′ = −(q + G)/x with G = ∫_x^1 dy ln(1−y) q(x/y), and
integrating xG′ by parts with a cutoff 1−ε (the ln ε terms cancel):
**x²F″ = ∫_x^1 dy [y q(x/y) − q(x)]/(1−y) + q(x) ln(1−x) + q(x) − x q′(x).**
For ⊥, the extra kernel y − y² adds x²(∫_x^1 dy(1−y)q(x/y))″ = q(x) − 2∫_x^1 dy y q(x/y), reproducing eq. (62).
Since ∫_0^1 dy [h(y) − h(1)]/(1−y) with h = y q(x/y)θ(y > x) equals ∫_x^1 dy [yq(x/y) − q(x)]/(1−y) + q(x) ln(1−x), eqs. (61)–(62) with the
[0,1] plus distribution are exactly x²F″, and (64) **drops q(x) ln(1−x)** in both braces: **R_printed − R_correct = −(1−x) ln(1−x)**.

### 4.3 Checks
* Exact (sympy closed-form F; branch artifacts removed) for q = x(1−x)³, x²(1−x)², (1−x)⁴, x³(1−x) at x = 0.3, 0.6, ∥ and ⊥:
  x²F″ = [0,1]-plus braces to ~10⁻¹⁵; x²F″ − (64)-braces = q ln(1−x) to ~10⁻¹⁵ (`e03_exact_eval2.py`).
* BVZ model (60), direct numerical second derivative (mpmath, 30 digits; `e03_bvz.py`):

| x | R^∥ correct | R^∥ printed | excess | R^⊥ correct | R^⊥ printed | excess | −x̄ ln x̄ |
|---|---|---|---|---|---|---|---|
| 0.2 | 0.468715 | 0.64723 | +38.1 % | 0.826486 | 1.00500 | +21.6 % | 0.178515 |
| 0.5 | 1.09528 | 1.44185 | **+31.6 %** | 1.44624 | 1.79282 | **+24.0 %** | 0.346574 |
| 0.8 | 2.02726 | 2.34915 | +15.9 % | 2.20595 | 2.52784 | +14.6 % | 0.321888 |

  (x²F″ equals the [0,1]-plus braces to 12 digits in all six cases.) The percentages are model-dependent; the absolute shift is universal.
* x < 0 (`e03_negx.py`): x²F″ equals the braces with **−x q′(x)**, not −|x|q′(x) (x = −0.3: 0.03902 vs −0.2562). Already noted by
  Liu–Chen, PRD 104 (2021) 094501, footnote (arXiv:2010.06623v3: "…should be a typo of Ref. [BVZ]"); their eq. (Qrenorm), written with ∫_0^1,
  contains q ln(1−|x|) implicitly.
* Endpoints: −x̄ ln x̄ → 0 at x → 0, 1; R_correct → const as x → 1 (s4: 1.99, 2.99 for (1−x)², (1−x)³) ⇒ Λ²/(x²(1−x)P_z²) unaffected.
* Project `s4_tmd_bvz.py`: 20/20.
* Literature: INSPIRE full-text search among BVZ citers ("typo": Liu–Chen 2021, Monahan 2026 (unrelated typo), TMD Handbook; "misprint": none;
  "ln(1-x)": 11 papers, none discussing (64)). The (64) omission was not found reported.

### 4.4 Verdict
**Confirmed** (x > 0): published (64) is wrong, (61)–(62) with the [0,1] plus distribution (55) are right.

## 5. E04 — sign of g in IJJSZ Wilson lines

* Printed (journal PRD 98 (2018) 056004, pp. 2, 7 rendered = arXiv): eq. (2) U(ξ⁻,0) = P exp(−ig∫_0^{ξ⁻}dη⁻A⁺(η⁻)); eq. (5) U(z,0) = P exp(−ig∫_0^z dz′A^z(z′));
  both enter ψ̄(endpoint) Γ U(endpoint,0) ψ(0); eq. (41) vertex (−igT^aγ^μ) and sail link factor (igT^aγ⁰)(e^{−ip^zz} − e^{−ik^zz})/(i(p^z−k^z))δ^{μz}.
* Gauge covariance (derived): for D = ∂ + isgA, A′ = UAU† + (i/(sg))(∂U)U†, the covariant link is W[b,a] = P exp(−isg∫_a^b dx^μA_μ).
  Along x⁻ (x⁺ = 0): dx^μA_μ = dx⁻A₋ = dη⁻A⁺ ⇒ eq. (2) ⇔ s = +1. Along ẑ: dx^μA_μ = dz′A₃ = −dz′A^z ⇒ eq. (5) = P exp(+ig∫dx·A) ⇔ s = −1.
  Vertex −igγ^μ ⇔ ℒ_int = −gψ̄A̸ψ ⇔ s = +1. So **eq. (5) is inconsistent with eq. (2) and with the paper's own vertex**.
* Sail link vertex (my derivation, position-space Feynman rules, ψ(y)|p⟩ = u e^{−ip·y}, q = p − k, (p−k)·e = −(p^z−k^z)):
  link term (−is_Lg)T^a e^μ ∫_0^z dz′ e^{i(p^z−k^z)z′} × e^{−ip^zz} = (+is_Lg)(e^{−ip^zz} − e^{−ik^zz})/(i(p^z−k^z)). Eq. (41) has (+ig): **s_L = +1 = s**,
  i.e. the computation used the consistent link P exp(−ig∫dx·A) = P exp(+ig∫dz′A^z), not eq. (5) as printed.
* O(g²) sensitivity: from IJJSZ eq. (43), the UV-pole coefficients (×a e^{−iζ}/ε_UV) are sail +1, tadpole +1, wave function −½ ⇒ 3/2 (the
  heavy-light anomalous dimension). Flipping the sail sign gives −1/2 and also destroys the collinear-pole matching to the PDF. The relative sign
  therefore matters at O(g²); the inconsistency is harmless only because the actual integrands are consistent.
* Literature: no report found (INSPIRE full-text searches among IJJSZ citers: "typo", "misprint", "sign of the coupling", "opposite sign").
* **Verdict: confirmed**, with the sharper justification.

## 6. E05 — JZZ and same-dimension lattice mixing

* JZZ PRL 120 (2018) 112001 (journal = arXiv): "Although lattice regularization breaks Lorentz symmetry and introduces operator mixing, it is not a
  concern for O(z₂,z₁) because there is no lower-dimension operator that can mix with it in lattice QCD"; then O_R = Z_j̄⁻¹Z_j⁻¹e^{δm̄|z|}ψ̄ΓLψ with Γ unchanged.
* GJS PRL 121 (2018) 022004 (journal, p. 2 rendered): eq. (5) φ_R = Z_φ(φ + r_mix n̸φ); eq. (6) O^R_Γ = Z_φ²e^{−m|ξ|}O_{Γ′}, Γ′ = Γ + r_mix sgn(ξ){n̸,Γ} + r_mix²n̸Γn̸;
  "In the continuum, this mixing is excluded by chiral symmetry … commonly used lattice regularizations break chiral symmetry"; "Since r_mix is O(g²),
  this is the same pattern at one-loop order as in Ref. [14]" (= Constantinou–Panagopoulos).
* Constantinou–Panagopoulos (arXiv v4): lattice one-loop term ∝ (Γγ_μ + γ_μΓ) "indicates mixing between operators of equal dimension, which is finite";
  pairs {S,V₁}, {A₂,T₃₄}, {A₃,T₄₂}, {A₄,T₂₃}; "For the operators P, V_ν (ν≠μ), A_μ, T_μν (ν≠μ) … only a multiplicative renormalization is required."
* Chen et al., CPC 43 (2019) 103101 (arXiv:1710.01089): dimension-3 mixing 1 ↔ γ₃ and iγ_iγ₅ ↔ ε_ijkσ_jk if chiral symmetry is broken; dimension-3 ↔
  dimension-4 mixing at O(a) "cannot be avoided even if chiral symmetry is preserved".
* Γ = γ^t, n = ẑ: {γ^z,γ^t} = 0 and γ^zγ^tγ^z ∝ γ^t (Euclidean γ₃γ₄γ₃ = −γ₄) ⇒ Γ′ = (1 − r_mix²)γ₄: no new Dirac structure at O(a⁰).
* JZZ's literal sentence is true (no lower-dimension mixing); its multiplicative formula with Γ unchanged is incomplete for chirally non-symmetric fermions.
* **Verdict: confirmed**, add "at O(a⁰)". The physics is in the literature; only the remark on JZZ's sentence is ours.

## 7. E06 — Ji 2013 matching with the hadron momentum

* Ji, arXiv:1305.1539 eqs. (11)–(12) (journal PRL 110 (2013) 262002 not accessed): q(x,μ²,P^z) = ∫_x^1 (dy/y) Z(x/y, μ/P^z) q(y,μ²),
  Z^(1) = T(x)(μ/P^z) + P(x) ln(P^z/μ) (transverse-cutoff μ).
* IJJSZ journal: eq. (6) (generic p^z), eq. (27) q̃(x, μ/P^z) = ∫_{−1}^{1} (dy/|y|) C(x/y, μ/(|y|P^z)) q(y,μ), followed by "This differs from the choice
  p^z = P^z which had been conjectured and used in the early papers on the quasi-PDF [21,22,24]" ([21] = Ji 2013); Introduction: "In the quasi-generalized
  parton distribution analysis in [38] it was observed that one should take p^z = |y|P^z". Ji–Schäfer–Xiong–Zhang PRD 92 (2015) 014039 (arXiv source):
  "p^z shall be replaced by yP^z with P^z being the averaged longitudinal momentum of the external hadrons." ✓
* Change of variables λ′ = yλ (exact; orientation flip for y < 0 gives 1/|y|): the kernel depends on λ′²μ²/(y²P_z²), i.e. on μ/(|y|P^z).
  Toy test (`e06_check.py`, 𝒞 = δ(1−α)e^{−z²μ²}, PDF with antiquark part): direct FT = convolution with C(x/y, μ/(|y|P^z)) to 12 digits at x = 0.3, 0.6, −0.2;
  the P^z version differs by O(1) (e.g. 0.0553 vs 0.1267 at x = 0.3).
* O(α_s) size (IJJSZ eq. (68), MS-bar, μ enters via −(1+ξ²)/(1−ξ) ln(μ²/(y²P_z²)) inside [·]^{[0,1]}_{+(1)} and (3/2)δ(1−ξ) ln(μ²/(4y²P_z²))):
  C(ξ, μ/P^z) − C(ξ, μ/(|y|P^z)) = −2a ln|y| {[(1+ξ²)/(1−ξ)]₊ − (3/2)δ(1−ξ)} = −(α_sC_F/π) ln|y| (1+ξ²)/(1−ξ)₊ θ(0<ξ<1)
  = −(α_s/π) ln|y| [P_qq(ξ) − (3/2)C_F δ(1−ξ)] (identity ∫_0^1[(1+t²)−2]/(1−t)dt = −3/2 checked). Ratio scheme (IJJSZ eq. (70)): −(α_s/π) ln|y| P_qq(ξ).
  So "∝ ln|y| P_qq ⊗ f" is right up to the δ-term in MS-bar. The early range ∫_x^1 also misses ξ > 1 (|y| < |x|) and y < 0.
* **Verdict: confirmed**; already in the literature (IJJSZ 2018; JSXZ 2015).

## 8. Required edits (for the spec patch)
1. LAMET §0.3 item 1, §3.7 Prop. 3.4, §14 item 1: credit **Chou & Chen PRD 106 (2022) 014507 eq. (35)** (remark after eq. (37)); Su et al. **eq. (A.14)**;
   λ_S = z_S|p^z|; RMP numbers = arXiv v2 eqs. (120)–(121); journal NPB 964 eqs. (30), (33), (34). Remove "new result".
2. LAMET §0.3 item 2, §10.2, §14 item 2; YZLIU §4.1 E1: drop PRD 105 (journal) from the erratum list (only arXiv:2106.05310v1 eqs. (49), (51), (73));
   cite PRD 105 fn. 1; **LFWF exponent must be e^{½ ln((∓ζ_z + i0)/ζ)K}** (Liu–Su JHEP 2024, 204), not "(∓ζ_z − i0)"; RMP eqs. (209)–(210) are arXiv v2 numbers.
3. LAMET §0.3 item 3, §5.3, §14 item 3: journal eqs. (55), (60)–(64); percentages refer to model (60); use "−x q′(x)" for general x (or restrict to x > 0) and cite Liu–Chen 2021 for that typo.
4. LAMET §0.3 item 4: eq. (5) is the inconsistent one; results unaffected because eq. (41) uses the consistent link; the relative sign does matter at O(g²).
5. LAMET §0.3 item 5, §3.5: add "at O(a⁰)"; note O(a) dimension-4 mixing (Chen et al. 2019).
6. LAMET §0.3 item 6, §4.1 Thm 4.2: give the precise ΔC above; cite IJJSZ eq. (27) and JSXZ 2015.
