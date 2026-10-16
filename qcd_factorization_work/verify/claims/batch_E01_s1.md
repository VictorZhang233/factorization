# Verification batch E01–E06 (stage 1, independent verifier)

Date: 2026-10-10. Default stance: skeptical. Claims E01–E06 come from `frontier/lamet/LAMET.md` §0.3, §3.5, §3.7, §4.1, §5.3, §10.2, §14
and `frontier/yzliu/YZLIU.md` §4.1 (E1).

## 0. Method and sources

* **Primary literature was re-downloaded independently** (not the copies in `frontier/lamet/papers/`). The downloads are untrusted data; they were read as text only.
  * arXiv e-prints (latest versions): 2008.03886, 2004.03543 (v3), 2209.01236, 1911.03840, 2106.05310 (v1, the only version), 1811.00026, 2201.08401,
    1810.00048, 1801.03917, 1706.08962, 1707.07152, 1305.1539, 1705.11193, 2204.08343, 1910.11415, 2010.06623, 2609.40205.
    The file sizes equal those of the project copies, so the project copies are the genuine latest versions.
  * **Journal versions** (open access, SCOAP3 repository PDFs): NPB 964 (2021) 115311; NPB 991 (2023) 116201; PLB 811 (2020) 135946;
    PRD 105 (2022) 076014; PRD 106 (2022) 014507; PRD 98 (2018) 056004; PRD 99 (2019) 014013; PRD 99 (2019) 034505;
    PRL 120 (2018) 112001; PRL 121 (2018) 022004; NPB 955 (2020) 115054. Also the APPB 53 (2022) 4-A2 PDF from the journal site.
  * The following were **not** accessible: the RMP 93 (2021) 035005 journal PDF (I used the arXiv v3 PDF, generated from the final arXiv source),
    PRL 110 (2013) 262002 (arXiv PDF used), PRD 96 (2017) 054506 (arXiv source used).
* INSPIRE API: publication data and erratum records (no erratum is recorded for any paper in this batch). INSPIRE full-text searches
  (`refersto:` + "typo", "misprint", "quark number conservation", "sign of g") to look for earlier reports.
* My own scripts, copied to `verify/claims/batch_E01_s1_scripts/` (run with `python3 -I`):
  `e01_hybrid.py`, `e02_qtmd.py`, `e03_bvz.py`, `e03_negx.py`, `e04_sign.py`, `e04_sign2.py`, `e06_parton_momentum.py`.
  The project scripts named in the recipes were also re-run: `frontier/lamet/scripts/s2_ft_testfunctions.py` (44/44 PASS),
  `frontier/lamet/scripts/s4_tmd_bvz.py` (20/20 PASS), `frontier/yzliu/scripts/check_qtmd_1loop.py` (all consistent).

Notation: a = α_s C_F/(2π).

## 1. Summary

| id | verdict | what must change before printing | already in the literature? |
|---|---|---|---|
| E01 | **confirmed** | Not a new result. Cite Chou–Chen 2022 as the first correction. Su et al. equation is (A.14), not "(C1 hybrid)". Use λ_S = z_S\|y\|P^z. | **Yes**: Chou & Chen, PRD 106 (2022) 014507, eq. (35) and the remark after eq. (37). |
| E02 | **confirmed, with one wrong citation** | The published PRD 105 (2022) 076014 is **correct** (it has the ½ and a footnote saying the ½ is missing elsewhere). Only arXiv:2106.05310v1 lacks it. Remove PRD 105 from the erratum list. | **Yes** (by the authors): PRD 105 (2022) 076014, footnote 1. The correct form was already in ESZ 2019 and ESSZ 2022. |
| E03 | **confirmed** (x > 0) | Journal eq. numbers: (61), (62), (63)–(64); plus definition (55). The 30%/24% figures hold for BVZ's model (60) and depend on the model. For x < 0 the term is −x q′(x), not −\|x\| q′(x). | The omission in (64) is not reported anywhere I found. A different typo in (61) (−\|x\|q′ → −xq′) is in Liu–Chen, PRD 104 (2021) 094501, fn. 1. |
| E04 | **confirmed**, needs a sharper reason | The relative sign of the link and vertex **does** matter at O(g²) (sail diagrams). It is "harmless" only because IJJSZ's actual integrands (eq. (41)) use the consistent link. | Not found. |
| E05 | **confirmed** | State "at O(a⁰)". For γ^t the r² term only rescales the operator. | The mixing itself: Constantinou–Panagopoulos 2017; Chen et al. 2017/19; GJS 2018. It is acknowledged in the RMP (2021). The remark about JZZ's sentence is ours. |
| E06 | **confirmed** | The exact O(α_s) difference is (α_sC_F/π) ln\|y\| (1+ξ²)/(1−ξ)_+ ⊗ f, which is (α_s/π) ln\|y\| [P_qq − (3/2)C_F δ(1−ξ)] ⊗ f. The early range ∫_x^1 is also too small. | **Yes**: IJJSZ PRD 98 (2018) 056004 says it explicitly; first seen for quasi-GPDs by Ji–Schäfer–Xiong–Zhang, PRD 92 (2015) 014039. |

## 2. E01 — hybrid-scheme kernel, δ-term

### 2.1 What is printed (read in the journal version)
NPB 964 (2021) 115311 (SCOAP3 PDF):
* eq. (30): 𝒞_hybrid(α, z²μ², z²/z_S²) = 𝒞_ratio(α, z²μ²) + δ(1−α) (α_sC_F/2π)(3/2) ln(z²/z_S²) θ(|z|−z_S);
* eq. (33): C_hybrid(ξ, μ²/(p^z)², z_S²μ²) = C_ratio(ξ, μ²/(p^z)²) + (α_sC_F/2π)(3/2)[ −1/|1−ξ|_+ + 2Si((1−ξ)λ_S)/(π(1−ξ)) ],
  with ξ = y/x, λ_S = z_S p^z, and p^z = xP^z "the parton momentum";
* eq. (34): 1/|1−ξ|_+ ≡ lim_{β→0⁺}[ θ(|1−ξ|−β)/|1−ξ| + 2δ(1−ξ) ln β ].

The arXiv source (2008.03886, label `eq:hybridm2`) is identical. The RMP (arXiv v3, labels `eq:hybridm2`) prints the same thing as eqs. (120)–(121).
I did not access the RMP journal PDF.

### 2.2 Independent derivation
With u = 1−ξ and λ = z p^z, the extra term is (3a/2) G(u), where G(u) = ∫dλ/(2π) e^{iuλ} g(λ) and g(λ) = ln(λ²/λ_S²) θ(|λ|−λ_S).
* For u ≠ 0, integrate by parts (Abel-regularized boundary term):
  G(u) = (2/π)∫_{λ_S}^∞ cos(uλ) ln(λ/λ_S) dλ = −1/|u| + 2Si(uλ_S)/(πu).
  For |u| → ∞ this decays like −2cos(uλ_S)/(πλ_S u²). Near u = 0 it behaves like −1/|u| + 2λ_S/π.
* g grows only logarithmically and is even. So the exact transform equals the pointwise function, regularized at u = 0, plus c δ(u). No δ′ or δ″ terms can appear.
* g is continuous at λ = 0 with g(0) = 0. Pairing G with φ(u/R), R → ∞, therefore gives ∫G du = g(0) = 0. So c is fixed by ∫G = 0.
  This is vector-current conservation: the hybrid correction vanishes at z = 0.
  Hence G_exact = [−1/|u| + 2Si(uλ_S)/(πu)]_+ on ℝ.
* With the printed prescription (34): ∫_{−U}^{U}(−1/|u|_+) du = −2 ln U, and (4/π)∫_0^{Uλ_S} Si(v)/v dv = 2ln(Uλ_S) + 2γ_E + o(1).
  The sum is 2 ln(λ_S e^{γ_E}). So the printed C_hybrid has ∫dξ C_hyb = 1 + 3a ln(λ_S e^{γ_E}) (using ∫C_ratio = 1).
  It equals the exact kernel plus 3a ln(λ_S e^{γ_E}) δ(1−ξ).

### 2.3 Numerical verification (`e01_hybrid.py`, mpmath, 30 digits)
* The asymptotics ∫_0^V Si(v)/v dv − (π/2)(ln V + γ_E) are 2.8e−3, 5.3e−5, −8.3e−7 and 3.1e−9 for V = 10, 10², 10³, 10⁴.
* There are 12 test cases: λ_S ∈ {0.5, 1, 2, 3.7}, each with three Gaussians φ(u) of different centre and width.
  For each I computed (i) the exact pairing ∫dλ/(2π) g(λ) φ̂(λ), (ii) the plus-on-ℝ pairing, and (iii) the printed pairing.
  (i) and (ii) agree to all 14 printed digits. Also (iii) − (i) = 2 ln(λ_S e^{γ_E}) φ(0) in units of 3a/2, with a ratio of 1.0000000000000 in all 12 cases.
  The sign of the error changes with λ_S: it is negative for λ_S = 0.5 because ln(0.5e^{γ_E}) < 0.
* Size: at λ_S = 1 the shift is 3aγ_E = 0.104 for a = 0.06 and 0.110 for α_s = 0.3. "About 10%" is correct.
* Re-run of `s2_ft_testfunctions.py`: 44 PASS, 0 FAIL.

### 2.4 The corrected form and its prior publication
* **Chou & Chen, PRD 106 (2022) 014507** (arXiv:2204.08343v4 eq. (28) = journal eq. (35)) print
  C^{hybrid-ratio} = C^{ratio} + (3α_sC_F/4π)[−1/|1−ξ| + 2Si((1−ξ)|y|z_sP^z)/(π(1−ξ))]^{[−∞,∞]}_{+(1)}.
  The journal text after eq. (36) says this "differs from the one of Ref. [63] [= Ji et al. 2021] in the last term …
  In addition to the difference between y and |y| in the argument of the Si function, quark number conservation is violated in the
  expression of (37) but is preserved in (35)."
* **Su et al., NPB 991 (2023) 116201**, journal eq. **(A.14)** (arXiv label `eq:hybridkernelNLO`), prints the same plus-on-ℝ form and cites Chou–Chen.
  The equation label "(C1 hybrid)" in our material does not exist.
* Extra point from Chou–Chen: the Si argument must contain |y| (or |p^z|). With a signed p^z = xP^z, the antiquark region gets the wrong sign, because Si is odd.
  My derivation agrees: θ(|z|−z_S) gives |λ_S|.

### 2.5 Verdict
**Confirmed** as an erratum of NPB 964 eqs. (33)–(34) and of the RMP (arXiv v3 eqs. (120)–(121)). The corrected version is right.
It is **already in the literature** (Chou–Chen 2022). LAMET.md §14 item 1 ("new result obtained in this work") and §0.3 item 1 must credit Chou–Chen.

## 3. E02 — Collins–Soper exponent in quasi-TMD factorization

### 3.1 What each paper prints (read)
| paper | version read | printed | own definitions in the same paper |
|---|---|---|---|
| Ji–Liu–Liu PLB 811 (2020) 135946 | journal | eq. (22): f̃√S_r = H e^{K ln(ζ_z/ζ)} f^TMD. The text also has "exp[ln(ζ_z/ζ)K] is required". | eq. (7): 2ζ d ln f^TMD/dζ = K; eq. (12): 2ζ_z d ln f̃/dζ_z = K + G; "comparing (22) and (12) … 2 d lnH/d lnζ_z = G" |
| Ji et al. RMP 93 (2021) 035005 | arXiv v3 | eq. (209): f^TMD = H e^{−ln(ζ_z/ζ)K} f̃ S_r^{1/2}; eq. (210): ratio (ζ_{z,1}/ζ_{z,2})^{K}. Item 2 of the text has exp[ln(ζ_z/ζ)K]. | eq. (184): 2ζ d ln f^TMD/dζ = K; eq. (201): P^z d ln f̃/dP^z = K + 𝒢; the text before (184) correctly gives f ∝ exp[−½K ln(μ²/ζ)] |
| Y. Liu APPB 53 (2022) 4-A2 | journal | eq. (52) has e^{½ ln(ζ_z/ζ)K} (**correct**). But eq. (53) has the ratio (ζ_{z,1}/ζ_{z,2})^{K}, eq. (75) has e^{K ln(ζ_z/ζ)}, and the text between (52) and (53) has exp[ln(ζ_z/ζ)K]. | eq. (22): 2ζ d ln f^TMD/dζ = K |
| Ji–Liu–Liu PRD 105 (2022) 076014 | **journal** | eq. (49): ψ̃_N√S_rN = **e^{½ ln((∓ζ_z−i0)/ζ)K_N}** H_N ψ_N; eq. (51): K_N = [½ ln(ζ_z/ζ′_z)]^{−1} ln(…); eq. (74) (N = 1) also has the **½**. **Footnote 1: "In front of the Collins Soper Kernel K_N there is a factor ½, which is missing in Refs. [22,23]"**, where [22] = RMP 93 035005 and [23] = NPB 955 115054. | eq. (35): 2ζ d ln ψ_N/dζ = K_N |
| same, arXiv:2106.05310 (v1, the only version) | arXiv | eqs. (49), (51), (73) lack the ½ | same |

* The claim's citation "PRD 105 (2022) 076014 eqs. (49),(51),(73)" is therefore **wrong for the journal version**.
  Those numbers and the missing ½ belong to the arXiv preprint only. In the journal the N = 1 formula is eq. (74), and eq. (73) is Γ_S^{(2)}.
* NPB 955 (2020) 115054 (journal, read) contains no formula with an explicit CS exponent of the form K ln(ζ_z/ζ). Footnote reference [23] may be a mis-citation; I cannot decide this.

### 3.2 All-order argument (independent of one-loop details)
The left side f̃√S_r does not depend on ζ. With 2ζ ∂_ζ ln f^TMD = K, the right side H e^{cK ln(ζ_z/ζ)} f^TMD has ∂_{ln ζ} ln(RHS) = (½ − c)K.
This vanishes only for c = ½.
Independently, ζ_z = (2xP^z)² gives P^z ∂_{P^z}(cK ln ζ_z) = 2cK. Agreement with P^z∂ ln f̃ = K + 𝒢 again requires c = ½.
With c = 1 one would need 2 d ln H/d ln ζ_z = G − K, which contradicts the perturbativity of H.
The ratio (ζ_{z1}/ζ_{z2})^{K/2} = (P_1^z/P_2^z)^K is the ESZ form: PRD 99 (2019) 034505, journal eqs. (24) and (27).

### 3.3 One-loop check (`e02_qtmd.py`, sympy; inputs are the RMP's own one-loop expressions)
* The inputs are f̃^{(1)} = a[−½L_b² + L_b(5/2 − L_z) − 3/2 − ½L_z² + L_z] (RMP eq. (200)) and f^{TMD(1)} = a[−½L_b² + (3/2 − L_ζ)L_b + ½ − π²/12] (eq. (185)).
  Also S_DY^{(1)} = a[2 − 2(Y+Y′)]L_b (eq. (207)), with S_DY = e^{(Y+Y′)K + 𝒟} and S_r = e^{−𝒟}.
* These give K^{(1)} = −2aL_b and S_r^{(1)} = −2aL_b.
* In f̃^{(1)} + ½S_r^{(1)} − H^{(1)} − cK^{(1)}(L_z − L_ζ) − f^{(1)}, the coefficients are L_bL_ζ: −a(2c−1) and L_b: aL_z(2c−1). Hence **c = ½**.
* Then H^{(1)} = a(−2 + π²/12 − L_z²/2 + L_z), which equals ESZ/ESSZ C_q^{(1)} and the PLB value c_1.
* With c = 1 the residual is **a L_b (L_z − L_ζ)**, as claimed.
* The ESZ ratio formula returns K^{(1)} = −2aL_b exactly.
* LFWF (N = 1, PRD 105 eqs. (69), (63), (72)), real parts: the L_b residual is aL_b(2c−1)(ℓ_z − ℓ_ζ). This vanishes only for c = ½.
* The project scripts give the same: `check_qtmd_1loop.py` and `s4_tmd_bvz.py` part A (6/6).

### 3.4 Verdict
**Confirmed** as an erratum of PLB 811 eq. (22), the RMP (arXiv v3 eqs. (209)–(210); the authors' footnote in PRD 105 confirms the published RMP lacks the ½), and APPB 53 eqs. (53) and (75).
**Not** an erratum of the published PRD 105 (2022) 076014, which is correct.
**Already noted in print by the original authors** (PRD 105, footnote 1). The correct form was published earlier by ESZ 2019 (eq. (24)) and later by ESSZ 2022 (eqs. "oldfact" and "factorization_statement").

## 4. E03 — Braun–Vladimirov–Zhang eq. (cR)

### 4.1 What is printed (PRD 99 (2019) 014013, journal)
* eq. (55): "[f(α)]_+ = f(α) − δ(ᾱ)∫_0^1 dβ f(β)" — the usual [0,1] definition.
* eq. (61) (= arXiv `t4-Qparallel`): Q^∥ = q − (κv²Λ²/(pv)²)(d/dx)² ∫_{|x|}^1 (dy/y)(y + ȳ ln ȳ) q(x/y)
  = q − (κv²Λ²/(x²(pv)²)){∫_{|x|}^1 (dy/y) y²/[1−y]_+ q(x/y) + q(x) − |x| q′(x)}.
* eq. (62) (= `t4-Qperp`) is the same with kernel y + ȳ ln ȳ + yȳ, braces {∫ (dy/y)[y²/[1−y]_+ − 2y²] q + 2q − |x|q′}.
* eqs. (63)–(64) (= `cR`), "assuming x > 0": Q^{∥(⊥)} = q{1 − v²Λ²/(x² x̄ (pv)²) R^{∥(⊥)}_Q}, with
  R^∥_Q = (x̄/q){∫_x^1 dy/(1−y)[y q(x/y) − q(x)] + q − x q′} and R^⊥_Q = (x̄/q){∫_x^1 dy/(1−y)[y(2y−1) q(x/y) − q(x)] + 2q − x q′}.
  (κ is dropped here, following BVZ's remark that one may set κ = 1.)

### 4.2 Independent proof
* Mellin space (exact, sympy for N = 1…8): N(N+1)K_∥(N) = N + 1 − H_{N+1}. This is the Mellin transform of {y²/[1−y]_+^{[0,1]} ⊗ q + q − x q′}.
  The ⊥ case is likewise exact.
* Rewriting the [0,1] plus distribution over [x,1]:
  ∫_x^1 (dy/y) y²/[1−y]_+ q(x/y) = ∫_x^1 dy [y q(x/y) − q(x)]/(1−y) + **q(x) ln(1−x)**.
  So (64) equals the correct second derivative minus x̄ ln x̄. That is, **R_printed − R_correct = −(1−x)ln(1−x)** for both ∥ and ⊥.
* Direct check (`e03_bvz.py`): numerical x²F″(x) agrees with the [0,1]-plus braces to 10⁻⁴⁰ for four model PDFs and x = 0.2, 0.5, 0.8, both ∥ and ⊥.
  It disagrees with the braces of (64).
* For BVZ's own model (60), q = x^{−1/2}(1−x)³, at x = 0.5: R^∥ is 1.0953 (correct) and 1.4419 (printed), +31.6%; R^⊥ is 1.4462 and 1.7928, +24.0%.
  This **matches the claim**. The size depends on the model: for x^{1/2}(1−x)³ it is +51% (∥) and +34% (⊥) at x = 0.5.
* Endpoints: −x̄ ln x̄ → 0 for x → 1 and x → 0, so BVZ's 1/(x²(1−x)) enhancement statement is unaffected.
* The project script `s4_tmd_bvz.py` part B gives 14/14.

### 4.3 Additional observation (not in the claim)
For x < 0, d²/dx² of the convolution gives "+ q(x) − x q′(x)", not "− |x| q′(x)". Numerically (`e03_negx.py`, antiquark model) at x = −0.3: x²F″ = −0.4764 = [−xq′ form]. The [−|x|q′] form gives +1.1455.
Liu & Chen, PRD 104 (2021) 094501, footnote 1, already call this a typo of eq. (61).
The claim's formula "… + q − |x|q′" is therefore correct only for x > 0. That is also the only region where the comparison with (64) is made.

### 4.4 Verdict
**Confirmed** (for x > 0): the published formula (64) is wrong and the corrected version (61)/(62) with the [0,1] plus distribution of (55) is right.
For printing, use journal eq. numbers (61), (62), (63)–(64), and state that the percentages are for model (60).
The omission was **not found** in the literature. The full-text search of citing papers found only the different typo noted by Liu–Chen.
Liu–Chen's momentum-space result (their eq. Qrenorm, with ∫_0^1) implicitly contains q ln(1−x).

## 5. E04 — sign of g in the IJJSZ Wilson lines

* Printed (PRD 98 (2018) 056004, journal = arXiv): eq. (2) U(ξ⁻,0) = P exp(−ig∫_0^{ξ⁻}dη⁻ A⁺(η⁻)); eq. (5) U(z,0) = P exp(−ig∫_0^z dz′ A^z(z′)).
  The vertex used in the one-loop integrands, eq. (41), is (−igT^aγ^μ). This means ℒ_int = −gψ̄A̸ψ, i.e. D_μ = ∂_μ + igA_μ.
* Gauge covariance (`e04_sign.py`): for D = ∂ + i s g A the invariant link is P exp(−i s g∫dx·A).
  Along x⁻, dx·A = dη⁻A⁺. So eq. (2) corresponds to s = +1.
  Along ẑ, dx·A = dz′A_3 = −dz′A^z. So eq. (5) equals P exp(+ig∫dx·A), which corresponds to s = −1.
  **The two links require opposite signs of g in D_μ, and eq. (5) is also inconsistent with the paper's own vertex.** The claim is confirmed.
* About "harmless at O(g²)": the sail diagrams are linear in the link coupling, so the relative sign matters at O(g²).
  With the consistent sign, the vertex + sail + tadpole decomposition gives the standard result a[(1+ξ²)/(1−ξ) ln(ξ/(ξ−1)) + 1] for ξ > 1 (tail −3a/(2ξ)).
  With the sail sign flipped, the result differs (tail +a/(2ξ)) (`e04_sign2.py`).
  I derived the sail term for the consistent convention (D = ∂ + igA, link P exp(−ig∫dx·A)).
  It equals IJJSZ's printed sail integrand in eq. (41), with link factor (igT^a)(e^{−ip^zz} − e^{−ik^zz})/(i(p^z−k^z))δ^{μz}, exactly.
  So their calculation used the consistent link, and only the printed definition (5) is off.
  "Harmless" is correct in the sense that **the results are unaffected**. It is not true that O(g²) is insensitive to the sign.
* **Verdict: confirmed** with the sharper justification. No earlier report was found.

## 6. E05 — JZZ and same-dimension lattice mixing

* JZZ, PRL 120 (2018) 112001 (journal = arXiv): "Although lattice regularization breaks Lorentz symmetry and introduces operator mixing, it is
  not a concern for O(z₂,z₁) because there is no lower-dimension operator that can mix with it in lattice QCD."
  The renormalized operator O_R = Z_j̄^{−1}Z_j^{−1}e^{δm̄|z|}ψ̄ΓLψ is then written with Γ unchanged.
* GJS, PRL 121 (2018) 022004, journal eqs. (5)–(6): φ_R = Z_φ(φ + r_mix n̸φ) and O^R_Γ = Z_φ²e^{−m|ξ|}O_{Γ′}, with Γ′ = Γ + r_mix sgn(ξ){n̸,Γ} + r_mix² n̸Γn̸.
  Quote: "In the continuum, this mixing is excluded by chiral symmetry … commonly used lattice regularizations break chiral symmetry".
  Also: "Since r_mix is O(g²), this is the same pattern at one-loop order as in Ref. [14] [Constantinou–Panagopoulos]."
* Constantinou–Panagopoulos, PRD 96 (2017) 054506 (arXiv source): the one-loop lattice term ∝ (Γγ_μ + γ_μΓ) "indicates mixing between operators of
  equal dimension, which is finite and appears in the lattice regularization". The mixing pairs are {S, V_1}, {A_2,T_34}, …
  The operators "P, V_ν (ν≠μ), A_μ, T_μν (ν≠μ)" need only multiplicative renormalization. In the DR calculation there is "no mixing between operators of equal or lower dimension".
* For Γ = γ^t with n along z, {n̸,γ^t} = 0. The r² term gives n̸γ_tn̸ = −γ_t (Euclidean), so Γ′ = (1−r²)γ_t: a rescaling, with no new Dirac structure.
  At O(a⁰) there is no mixing. The RMP (2021) states the same: "O_{γ^z}(z) can mix with the scalar operator O_1(z), whereas O_{γ^t}(z) does not."
* JZZ's literal statement (no *lower*-dimension mixing) is true, since only same-dimension mixing occurs. Its consequence, multiplicative renormalization with Γ unchanged on the lattice, is incomplete for chirally non-symmetric fermions.
* **Verdict: confirmed**; add "at O(a⁰)". The physics is in the literature (CP 2017, Chen et al. CPC 43 (2019) 103101 [arXiv:1710.01089], GJS 2018, RMP 2021). The comment on JZZ's sentence is an editorial remark.

## 7. E06 — Ji 2013 matching with the hadron momentum

* Ji, PRL 110 (2013) 262002 (arXiv eq. (11)): q(x,μ²,P^z) = ∫_x^1 (dy/y) Z(x/y, μ/P^z) q(y,μ²), with Z^{(1)} = T(x)(μ/P^z) + P(x) ln(P^z/μ) (eq. (12)).
* Change of variables (`e06_parton_momentum.py`, symbolic): inserting the coordinate factorization and substituting λ′ = yλ gives
  ∫dy/|y| f(y) ∫dλ′/(2π) e^{−i(x/y)λ′}∫dα e^{iαλ′} 𝒞(α, μ²λ′²/(yP^z)²). The kernel therefore depends on μ/(|y|P^z). This is exact.
* Size of the O(α_s) error. The MS-bar kernel depends on μ only through ℓ_p = ln(μ²/4p_z²), in the form a{−ℓ_p[(1+ξ²)/(1−ξ)]_+ + (3/2)ℓ_p δ(1−ξ)}.
  Replacing p^z = |y|P^z by P^z changes it by **ΔC = 2a ln|y| (1+ξ²)/(1−ξ)_+ = (α_s/π) ln|y| [P_qq(ξ) − (3/2)C_F δ(1−ξ)]**.
  This uses the identity [(1+ξ²)/(1−ξ)]_+ = (1+ξ²)/(1−ξ)_+ + (3/2)δ, checked numerically.
  For f = x^{−1/2}(1−x)³ and α_s = 0.3, Δq̃/f is 0.56, 0.42 and 0.28 at x = 0.3, 0.5 and 0.7. This agrees with IJJSZ's "important effect".
  The early form also restricts the range to y ∈ [x,1]. That drops the ξ > 1 and y < 0 contributions, which is a separate O(α_s) defect.
* IJJSZ (PRD 98 (2018) 056004, read) say this explicitly: "This differs from the choice p^z = P^z which had been conjectured and used in the early papers on the
  quasi-PDF [Ji:2013dva, Ji:2014gla, Xiong:2013bka]"; also "In the quasi-generalized parton distribution analysis in [Ji:2015qla] it was observed that one should take p^z = |y|P^z".
  Ji:2015qla is Ji, Schäfer, Xiong, Zhang, PRD 92 (2015) 014039, arXiv:1506.00248.
* **Verdict: confirmed**. The statement "∝ ln|y| P_qq ⊗ f" should be made precise as above. It is **already in the literature** (IJJSZ 2018), so it is not new.

## 8. Required edits to our material (for the spec patch)
1. LAMET §0.3 item 1, §3.7 Prop. 3.4 and §14 item 1: credit Chou & Chen PRD 106 (2022) 014507 eq. (35) as the first correction. Fix "Su et al. eq. (C1 hybrid)" to journal eq. (A.14). Write λ_S = z_S|y|P^z. The hybrid paper's authors are X. Ji, Yizhuang Liu, A. Schäfer, W. Wang, Y.-B. Yang, J.-H. Zhang, Y. Zhao (cf. A01).
2. LAMET §0.3 item 2, §10.2 and §14 item 2; YZLIU §4.1 E1: remove PRD 105 from the erratum list. State that its journal version is correct and that footnote 1 there acknowledges the missing ½ (for the RMP). Quote arXiv:2106.05310 only if the preprint is cited. It is not a new result of this work.
3. LAMET §0.3 item 3, §5.3 and §14 item 3: use journal eq. numbers (55), (61)–(64). Say that the 30%/24% figures are for model (60). Write "−x q′(x)" in place of "−|x| q′(x)" for general x, or restrict to x > 0, citing Liu–Chen 2021 for that typo.
4. LAMET §0.3 item 4: replace "harmless at the orders computed" by "IJJSZ's explicit one-loop integrands (eq. (41)) use the consistent link, so their results are unaffected; the relative sign does matter at O(g²)".
5. LAMET §0.3 item 6 and §4.1 Thm 4.2: the attribution [Izubuchi:2018srq] is correct. Also cite Ji–Schäfer–Xiong–Zhang 2015. Give the precise ΔC above.
