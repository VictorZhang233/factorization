# Verification batch N25–N29: stage 2 (second, independent verifier)

Date: 2026-10-11. Stance: skeptical. I did not rely on stage 1 (`batch_N25_s1.md`). I read it only after my own checks, to list where we agree or differ.

Method for each claim:
1. Re-run the project scripts named in the recipe.
2. Re-derive every statement with my own code, using methods chosen to differ from both the project and stage 1.
3. Read every cited source myself. arXiv sources and PDFs, plus the published versions where these are open access via SCOAP3, were downloaded fresh into the scratchpad and treated as untrusted data.
4. Check all texkeys on INSPIRE.

Scripts and logs are in `verify/claims/batch_N25_s2_scripts/`. Run each with `python3 -I <script>`. Project re-runs are in `rerun/`.

| script | checks | result |
|---|---|---|
| `n25_s2.py` | Glauber toy, plus trap | 36/36 PASS |
| `n26_s2.py` | eikonal identity vs regulator | 21/21 PASS |
| `n27_s2.py` | LaMET kernels as Fourier transforms | 49/49 PASS (≈1.5 min) |
| `n28_s2.py` | OTHERS transcriptions | 26/26 PASS |
| `n29_s2.py` | YZLIU cross-checks | 24/24 PASS |

**Project re-runs.** All reproduce:
- `research/c_dy/glauber_toy.py`: 25/25.
- `plus_trap.py`: c = 1.75.
- `research/c_wilson/scripts/s2_eikonal_identity.py`: 44/44.
- `frontier/lamet/scripts/s2_ft_testfunctions.py`: 44/0. Its 20 MS-bar/ratio comparisons have |diff| from 1.85e−12 to 7.93e−9.
- `frontier/others/scripts/` s2 10/10, s3 3/3, s4 8/8, s5 5/5.
- `frontier/yzliu/scripts/check_HL_and_C1.py`: identity 0; (C.1) agrees for n = 2, 3, 4.
- `check_gammaC2.py`: 0 and 0.
- `check_GN_ineq.py`: maximum ratios 0.99876 … 0.999997.
- `crossref_check.py`: needs the arguments `../yzliu.bib ../YZLIU.md`; it then runs.

## Summary

| id | verdict | already known? | what must change before printing |
|---|---|---|---|
| N25 | **confirmed for the corrected statement only** | yes: Collins 2011 §14.3, §14.4.1 item 5; the eikonal phase is classical | **The plus-trap formula exactly as written in the claim is FALSE.** The correct formula is (1+z²)𝒟₁ = [(1+z²)ln(1−z)/(1−z)]₊ + (7/4)δ(1−z), as in c_dy §3.10. "Cancels after the k_T integral" must say *relative* spectator k_T. |
| N26 | **confirmed** | yes: Echevarria–Scimemi–Vladimirov, PRD 93 (2016) 054004 [Echevarria:2015byo], eqs. (5)–(6) and text | "only with the adiabatic regulator" → "exactly when the cumulative regulators are additive (e.g. e^{−ε\|t\|} on every field)". |
| N27 | **confirmed** | yes: IJJSZ derived (65)/(68)/(70) from (62) by this very transform (their eq. (34), text after (69); (70) "starting with eq. (65) and using eq. (37) together with eq. (59)") | Accuracy is 1.9e−12 – 7.9e−9 (project), not "1e−9 to 1e−12". The momentum RGE is Ji:2020ect (RMP 93 (2021) 035005) eq. (32), **not** Ji:2020brr. |
| N28 | **confirmed** (5/5 transcriptions) | yes (transcriptions) | (i) "first term" → first **super-leading** (n = 1) term. (iii) Equality with Frixione (4.189) holds at leading power only; the αm²x²(1−x)/(πμ²) term is a power correction; Frixione is single-author. LN equation numbers: JHEP 04 (2020) 033 numbers them **(2.1), (2.3)** (arXiv: (1), (3)). CRS sign-structure numbers: negative on (0.264, 1) at μ = 0.8 GeV, not "[0.28, 0.98]". |
| N29 | **confirmed** (all items) | yes (cross-checks of published formulas) | N_m = C_Fe^{5/6}/π is Liu–Su eq. **(2.50)**; (2.52) holds the conjectured values. JLS: arXiv v1 and JHEP 08 (2023) 037 number §3–4 differently: γ̃_J explicit is arXiv (3.13) = JHEP (3.12); J_f^(1) is arXiv (4.10) = JHEP (4.11); H^(1) is arXiv (4.11) = JHEP (4.12). (A.x), (4.2), (5.11), (5.12) are the same in both. |

---------------------------------------------------------------------------------------------------------

## N25 — abelian DY Glauber toy; plus trap

### (a) χ(b) = −(g_Ag_B/2π)K₀(m|b|)
- **Kernel.** Vertices (ig_A)(ig_B), v_A·v_B = 1, and the Feynman-gauge propagator −ig_{μν}/(k²−m²+i0) at k⁺ = k⁻ = 0. Together they give the kernel −ig_Ag_B/(k_T²+m²) (sympy, n25 (2b)).
- **Measure.** The light-front Jacobian is 1, so d⁴k = dk⁺dk⁻d²k_T (n25 (2a)).
- **Fourier transform.** ∫d²k/(2π)² e^{ik·b}/(k²+m²) = K₀(mb)/2π. I checked it by a **Hankel transform** with `mpmath.quadosc`, a method different from the Schwinger parametrisation of stage 1 and the 2D `quadosc` of the project. It agrees to 30 digits at 3 points.
- **Sign, physical cross-check.** χ equals the **classical eikonal phase** −∫dz V(√(b²+z²)) of the repulsive Yukawa potential V = g_Ag_B e^{−mr}/(4πr). Vector exchange between like charges is repulsive. It agrees to 30 digits.

### (b) S–S exchange: trapped, and cancels after integration over the relative spectator k_T
- **Trapped k⁻ integral.** I evaluated it with an exact **partial-fraction closed form**, valid at any finite ε: ∫dk/((αk+β)(γk+δ)) = −iπ(sgn α − sgn γ)/(αδ−βγ) for Im β, Im δ > 0. The closed form was also checked against quadrature. It gives F(k₁)/(2p'⁺_A), i.e. the spectator goes on shell. When both poles lie on the same side the result is exactly 0.
- **k⁺ integral with the exact boson propagator.** I used contours deformed by compact C¹ bumps (n25 (3h)):
  - The value equals the Glauber-scale residue with the boson propagator → −1/K², up to 0.4–0.6 %, i.e. O(λ²).
  - Lifting **or** lowering the contour by iλ over |Re k⁺| < 3λ changes the value by O(1).
  - The contour is therefore trapped between s_B (LHP) and b (UHP), both at |k⁺| ~ λ².
- **Cancellation.** This was checked by direct-space 1D quadrature, without FFT:
  - At O(g²), ∫2Re M₀*M₁ = 2e−16, while ∫|·| = 0.63.
  - At O(g⁴), the cut sum is 2e−16.
  - Reason: the exchange kernel is −i × (a real symmetric kernel), so the cancellation needs the integration over the spectators' **relative** momentum.

### (c) Active–spectator exchange: not trapped in k⁺; I_as = 2πiθ(−k⁻)/(2p_b⁻K² + 2k⁻c_b)
- **Exact formula.** The partial-fraction form gives I_as **exactly at finite ε**: −iπ(sgn α − sgn γ)/(αδ−βγ) with α = 2p_b⁻, β = c_b+iε, γ = 2k⁻, δ = −K²+iε. Hence the formula, with θ(−k⁻) from sgn α − sgn γ ∈ {0, 2} (n25 (3e), 8 cases).
- **Contour tests.**
  - Lifting the contour by iλ over the Glauber region leaves the value unchanged to 1e−26.
  - Passing above the boson pole at k⁺ = −K²/(2|k⁻|) ≈ −1.08 gives 0.
  - So the integral is the boson-pole residue at |k⁺| ~ Q, which is A-collinear.
- **Eikonal replacement.** I_eik/I_as − 1 = k⁻c_b/(p_b⁻K²) exactly (−3.1e−3 for λ = 0.1).
- **Past-pointing identification.**
  - ∫_{−∞}^0 dλ e^{−iλn·k+ηλ} = i/(n·k+iη): this is the past-pointing line with k flowing in.
  - The future-pointing line gives −i/(n·k−iη).
  - So the +i0 of the active parton b selects W[0,−∞n_B], the line in f_{q/A}.

### (d) Plus trap: the claim text is false as written
- **Correct identity.** In the product convention g𝒟_k = g(1)𝒟_k + (g−g(1))ln^k(1−z)/(1−z), symbolically:
  g𝒟₁ − [g ln(1−z)/(1−z)]₊ = h(1)·∫₀¹(g−g(1))ln(1−z)/(1−z)dz.
  For g = 1+z² this is −∫₀¹(1+z)ln(1−z)dz = **7/4** (four test functions, 20 digits).
- **Consequence.** The δ coefficient C_F(2π²/3−8) of Δ_qq̄ becomes C_F(2π²/3−1) when the plus is put on the whole term.
- **Literal text.** "(1+z²)𝒟₁ vs [(1+z²)/(1−z)]₊ differ by (7/4)δ(1−z)" is **false**. The difference divided by h(1) is 14.33, −4.50, 3.35, −5.38 for four test functions, so it is not a multiple of δ.
- **Where the error sits.** Only the claim register's transcription is wrong; it drops the ln(1−z). The source is right: c_dy DERIVATION §3.10 item 1 and `plus_trap.py`.

### Literature (read)
- **Collins 2011, ch. 14** (open-access reissue, DOI 10.1017/9781009401845.014, pp. 540–572, read in full for §14.3–14.4):
  - §14.3 "Glauber region example": spectator ladder exchange; k± integrals closed on the final-state spectator poles, eqs. (14.11)–(14.13); "Cancellation after sum over cuts", (14.14)–(14.16).
  - §14.3.3: "to get a Glauber pinch … one must have an exchange attached to both the spectator parts"; "the cancellation applies only to the inclusive cross section".
  - §14.3.4: a gluon from the ladder to an active parton "attaches at a place which does not give a Glauber pinch. Therefore we can deform the integration out of the region".
  - §14.4.1 item 5: "the eikonal denominators correspond to past-pointing Wilson lines".
  - Attribution confirmed.
- **Bodwin 1985.** Bodwin, PRD 31 (1985) 2616; erratum PRD 34 (1986) 3932; INSPIRE Bodwin:1984hc; abstract read. It treats spectator interactions with one- and two-loop examples and all orders. Collins §14.4 says CSS 1988 "supersedes" it. Cite it as the original treatment only.

**Verdict: confirmed, for the corrected statement.** Not new.

---------------------------------------------------------------------------------------------------------

## N26 — eikonal identity at finite regulator

Exact symbolic checks:
- **m = 2, 3** (sympy `cancel`):
  - The adiabatic version, with the j-th cumulative denominator carrying +ijε, is exact for both past- and future-pointing lines.
  - Unequal per-gluon dampings with cumulative sums are **also exact**.
  - A uniform +iε is not exact; its defect is O(ε), with a ratio of 10.000 when ε goes from 1e−3 to 1e−4.
- **m = 4, 5**: exact Gaussian-rational arithmetic.
- **m = 2 uniform defect**, explicitly: −iε/[(a₁+iε)(a₂+iε)(a₁+a₂+iε)].

**Necessity.**
- For arbitrary subset shifts η(S) at m = 2, the defect is −i(η₁+η₂−η₁₂)/[(a₁+iη₁)(a₂+iη₂)(a₁+a₂+iη₁₂)]. The identity is exact iff the shifts are additive.
- At m = 3, additive shifts are exact and a non-additive triple shift fails.

**Interpretation.**
- The ordered integral with damping e^{ελ} on **each** field equals the adiabatic product (by hand, and by 2D quadrature).
- Damping only at the farthest attachment, e^{ελ_min}, gives exactly the uniform prescription. That is not a product of single-field factors, hence not a regulator of the Wilson-line operator.

**Distributional limit.** I give an exact closed form, which is new relative to stage 1, which used numerics only.
- The pairing of the uniform m = 2 defect with 1/((1+a₁²)(1+a₂²)) is **π²ε/((1+ε)²(2+ε))**, by residues.
- It was cross-checked by 2D quadrature on contours shifted to Im a = ½ (relative deviation ~2e−10).
- It is nonzero at every finite ε and → 0 like (π²/2)ε.

**Literature: the content is known.** Echevarria, Scimemi, Vladimirov, PRD 93 (2016) 054004, arXiv:1511.05590 [Echevarria:2015byo]:
- Eq. (5) defines the operator-level δ-regulator e^{−δσ} on Wilson lines.
- Eq. (6) gives the cumulative eikonal propagators 1/((k₁⁺−iδ)(k₂⁺−2iδ)…(k_n⁺−niδ)).
- The text says the original prescription ("setting the i0 … finite") "breaks the non-abelian exponentiation property"; "naive δ-regularization (with i0 directly replaced by iδ) … violates exponentiation properties … already … at NNLO, where terms with color factors C_F² arise in the exponent".
- The abelian part of exponentiation is the eikonal identity.

**Verdict: confirmed (precise form below).** Not new.

---------------------------------------------------------------------------------------------------------

## N27 — one-loop LaMET kernels as Fourier transforms

### Transcription
I read IJJSZ (arXiv:1801.03917v2 **and** the published PRD 98 (2018) 056004 via SCOAP3). The equation numbers are identical:
- FT relation: (34).
- FT[ln ζ²]: (59).
- Coordinate kernel: (62), with ΔC_{γ^z} in (63).
- Kernel with δ's at ±∞: (65).
- MS-bar kernel: (68), with γ^z in (69).
- Ratio kernel: (70), with γ^z in (71).

LAMET §4.6(a),(c) reproduces them exactly. Using ℓ_p = ln(μ²/4p_z²): −ln(μ²/y²P_z²) + ln(4ξ(1−ξ)) = −ℓ_p + ln(ξ(1−ξ)).

### Independent verification
Two methods, different from both the project's s2 (Gaussian test functions in ζ-space) and stage 1:
- **(P1) Pointwise in ξ ≠ 1.**
  - Use C(ξ) = ℓ_pA(ξ) + B(ξ) − (A ∗ [1/|u|])(ξ), with 𝒞 = A·L_z + B and FT[ln ζ²] = −2γ_Eδ − [1/|u|]_reg; the γ_E cancels against the 2γ_E in L_z.
  - I evaluated this with Hadamard finite parts in all three regions (ξ > 1, 0 < ξ < 1, ξ < 0), for both schemes, both Γ and two ℓ_p.
  - Maximum deviation from the printed functions: **7e−21** (36 checks).
  - The identity FT[ln ζ²] itself was also checked with Gaussians (≤1e−15).
- **(P2) Pointwise in ζ.** This fixes the δ(1−ξ) coefficients and the plus prescriptions, which P1 cannot see.
  - I computed ⟨C_printed, e^{−iξζ}⟩ with all plus prescriptions on the three domains.
  - The 1/ξ tails were done exactly via E₁ functions; the large-|ξ| subtracted parts via exact rational series and generalized E_k functions.
  - This was compared with G(ζ) = ∫dα 𝒞(α, L(ζ))e^{−iαζ} for ζ = 0.3, 1, 2.5, 7.
  - MS-bar and ratio, γ^0 and γ^z: maximum deviation **5e−22** (16 checks).
  - Negative control: changing the δ coefficient 5/2 → 2.51 is detected at 1.6e−2.
- **Consequence.** The δ-functions at ξ = ±∞ that IJJSZ dropped do not contribute for test functions that decay at infinity.
- **Accuracy figure.** The claim's "1e−9 to 1e−12" refers to the project's Gaussian pairings. Those are actually **1.9e−12 – 7.9e−9**, so the largest is ≈1e−8.

### Momentum RGE
- With dℓ_p/d ln p_z = −2, only the [g]₊ term on [0,1] and the δ term depend on ℓ_p. This gives
  P^z dC^MS/dP^z = 2a{[(1+ξ²)/(1−ξ)]₊ − (3/2)δ(1−ξ)} = (α_sC_F/π)[…] (sympy).
- This is **RMP eq. (32)** (arXiv:2004.03543v2; read).
- The plus there is the whole-term plus. RMP itself writes the MS-bar quasi-PDF and q^(1) with [·]^{[0,1]}_{+(1)}, so eq. (32) is consistent within RMP's conventions.
- RMP derives eq. (32) with a transverse-momentum cutoff.
- In the ratio scheme the −(3/2)δ is absent.
- **Attribution.** This is [Ji:2020ect]. [Ji:2020brr] (the hybrid scheme, NPB 964 (2021) 115311; source grepped) only cites [Ji:2020ect] for "momentum evolution". The LAMET source itself cites [Ji:2020ect] correctly; only the claim's literature list is wrong.

### Other attributions
- **Ratio kernel.** It agrees with Radyushkin, PRD 98 (2018) 014019 [Radyushkin:2018cvn], eq. (17) (inverse relation, "in agreement with" IJJSZ). This was read in arXiv and the published version, both numbered (17).
- **Radyushkin:2017cyf** (PRD 96 (2017) 034025) introduced the reduced ITD and the ratio idea.

**Verdict: confirmed (with corrected accuracy and attribution).** Not new.

---------------------------------------------------------------------------------------------------------

## N28 — OTHERS checked transcriptions

### (i) BNS, PRL 127 (2021) 212002
Read in arXiv and the published version (SCOAP3); the numbers are the same: eqs. (14), (18), (19), (21).
- **Tower sum.** From eq. (14) and the singlet eq. (19) with J₂ = J₄₃/2 = ΔY, only r = 0 contributes. Then Σ_n σ̂_n = −σ̂_B(4C_F/3π)α_s³L³ΔY ₂F₂(1,1;2,5/2;−w), w = N_cα_sL²/π. Exact sympy, term by term, n = 0..15.
- **First super-leading term.** n = 1 gives **+(4/(15π²))C_FN_cα_s⁴L⁵ΔYσ̂_B**.
- **n = 0 term.** It is −(4C_F/3π)α_s³L³ΔYσ̂_B, single-logarithmic, and is the first term of BNS's sum. So "first term" in the claim must read "first super-leading term".
- **Asymptotics.** The Mellin–Barnes double pole gives ₂F₂ = (3/2)(ln w − ψ(3/2))/w + …. It was checked against `mpmath.hyp2f2`:
  - relative deviation 5.5e−6 at w = 1e4 and 2.7e−10 at w = 1e8;
  - w·₂F₂/ln w = 1.49703 at w = 1e8.

### (ii) Liu–Neubert, JHEP 04 (2020) 033
- **Identity.** L̂²Σ n!/(2n+2)!(−C_Fα_sL̂²/2π)ⁿ = (L̂²/2)₂F₂(1,1;3/2,2;−C_Fα_sL̂²/8π). Exact term by term to n = 20, plus a numerical resummation check.
- **Low orders.** n = 0, 1 give L̂²/2 and (C_Fα_s/4π)(−L̂⁴/12), the leading logs of their NLO amplitude.
- **Equation numbers.**
  - arXiv:1912.08818 (article class) numbers them **(1), (3)**.
  - The **published JHEP version numbers them (2.1), (2.3)** (read via SCOAP3).
  - CLAIMS/OTHERS cite "JHEP 04 (2020) 033, eqs. (1),(3)", which mixes the journal reference with arXiv numbering. Fix before printing.

### (iii) LUXqed (PRL 117 (2016) 242002, arXiv eq. (6)) vs Frixione (JHEP 11 (2019) 158, eq. (4.189))
- **Sources read.** LUXqed arXiv v3, eq. (6). Frixione arXiv v2 and the published version, both (4.189), with Γ = Γ^[0] + (α/2π)Γ^[1] and K = 0 in MS-bar. Frixione is single-author (INSPIRE).
- **Point-like limit of LUXqed** (sympy, fixed α). With G_E = G_M = 1, F₂ = δ(1−x/z), F_L = (4m²/Q²)δ(1−x/z):
  xf_γ = (α/2π)[1+(1−x)²][ln(μ²/m²) − 2ln x − 1] + αm²x²(1−x)/(πμ²).
- **Comparison.** Its leading-power part is exactly x·(α/2π)Γ^[1]_{γ/e} of (4.189). The last term is an m²/μ² power correction that is absent from (4.189).
- **Shifts.** Dropping F_L shifts the result by (α/2π)4(1−x) at leading power. Dropping the MS-bar conversion term shifts it by (α/2π)x².
- **Independent derivation (new).** Light-cone wave-function computation in DR.
  - Integrand: [P^{(d)}(x)k² + x³m²]/(k²+x²m²)², with P^{(d)} = (1+(1−x)²)/x − εx.
  - It gives pole P_{γe}/ε and MS-bar finite part (1+(1−x)²)/x[ln(μ²/m²) − 2ln x − 1], i.e. (4.189). The −εx/ε cancels the +x of the mass term.
  - The x³m² term reproduces the exact Budnev EPA flux at leading power.

### (iv) CRS, PRD 105 (2022) 076010, eqs. (55)–(59)
Read in arXiv and the published version; the numbers are the same.
- **Dirac trace.** With numerical γ matrices: (1/4)Tr[γ⁺(k̸+m_q)(P̸+M)(k̸+m_q)] = P⁺[k_T²+(m_q+ξM)²] on the scalar mass shell.
- **Kinematics.** k²−m_q² = −(k_T²+Δ)/(1−ξ), so the integrand is (1−ξ)[k_T²+(m_q+ξM)²]/(k_T²+Δ)², eq. (58).
- **DR expansion.** 1/ε + ln(μ²/Δ) − 1 + c/Δ, i.e. eqs. (55) and (57).
- **Sign structure.** With m_q = 0.3, M = 1.0, m_s = 1.5 GeV (root finding):
  - The MS-bar pdf is negative **exactly on (0.2640, 1)** at μ = 0.8 GeV, and on (0.5674, 1) at 1.2 GeV.
  - The bracket at ξ = 1 is negative for μ < μ* = m_s exp{[1−(m_q+M)²/m_s²]/2} = 1.699 GeV.
  - It is positive for all ξ at 2.5 GeV.
  - **OTHERS §7's "negative for ξ ∈ [0.28, 0.98] at μ = 0.8 GeV" is a coarse-grid artefact.** It should read (0.264, 1).

### (v) BK
- **Eigenvalue.** I evaluated χ(γ) with the **2D complex Beta function**, I(a,b) = Γ(a)Γ(b)Γ(1−a−b)/(Γ(1−a)Γ(1−b)Γ(a+b)), with analytic regularisation (r₁²r₂²)^δ, δ → 0. This differs from the direct quadrature used by the project and stage 1. Result: χ = 2ψ(1)−ψ(γ)−ψ(1−γ) for γ = 0.15, 0.3, 0.5, 0.7 (≤4e−9), and χ(½) = 4ln2.
- **Source.** Balitsky–Chirilli, PRD 77 (2008) 014019 [Balitsky:2007feb], arXiv eq. (108), first line, gives this LO eigenvalue integral.
- **Minor typo.** Their arXiv text prints "2φ(1)" for 2ψ(1).

**Verdict: confirmed (with the clarifications above).** These are transcriptions, not new results. All texkeys resolve on INSPIRE: Becher:2021zkk, Liu:2019oav, Manohar:2016nzj, Frixione:2019lga, Collins:2021vke, Balitsky:2007feb.

---------------------------------------------------------------------------------------------------------

## N29 — YZLIU derived cross-checks

### (i) H decomposition
- C⁺C⁻ = 1 + (α_sC_F/2π)(−2 + π²/12 − L_z²/2 + L_z). This is JLS H^(1): arXiv (4.11), JHEP **(4.12)**.
- It equals ESZ C^(1) = −L²+2L−4+π²/6: PRD 99 (2019) 034505 eq. (25), read.
- (C^±)² = H^±_LFWF of JLS (4.2) at O(α_s). Its phase is (α_sC_F/2)(1−L_z).
- 𝒢^(1) = (α_sC_F/π)(1−L_z).
- All of this is a one-loop statement.

### (ii) c_H and the two-loop anomalous dimension
- **c_H.** The closed form is JLS (5.11) verbatim. Numerically it is 0.072518 C_F² − 0.084043 C_FC_A + 0.145307 C_Fn_fT_F, matching (5.12).
- **n_f parts.** The n_f part of c_H equals Liu–Su (2.42); that of γ̃_H^(2) equals (2.41) (large β₀).
- **γ̃_H^(2).** (A.11) with (A.2)–(A.5) gives exactly (A.13), using (α_s/4π)² → α_s² units. (A.6) was reproduced.

### (iii) γ̃_J^(2)
- γ̃_J^(2) = 2γ_HL − 2γ_s from (A.4), (A.5) via (A.10) gives C_FC_A(−1396/27 + 23π²/9 + 20ζ₃) + C_Fn_f(232/27 − 2π²/9). This is printed explicitly in JLS: arXiv **(3.13)**, JHEP **(3.12)**.
- It equals −γ₁ of Jain–Scimemi–Stewart, PRD 77 (2008) 094008 (bHQET jet function; source read). At one loop, −α_sC_F/π = −γ₀(α_s/4π) with γ₀ = 4C_F.

### (iv) N_m
- **Residue.** From Liu–Su (2.46), the residue at u = ½ is (μ/p^z)C_Fe^{5/6}/(2π), which is (2.47).
- **Normalisation.** With r_n = N_mβ₀ⁿn! this gives **N_m = C_Fe^{5/6}/π = 0.976564, eq. (2.50)**. Arithmetic and published numbering were checked. (2.52) contains the *conjectured* values beyond large β₀: 0.622 … 0.524.
- **Independent check.** In the large-β₀ static self-energy δm = (C_F/π)∫₀^μ dk α_V(k), with α_V(k) = α/(1+β₀α(ln(k/μ) − 5/6)), the coefficients tend to (C_Fe^{5/6}/π)β₀ⁿn!μ (ratio 1 at n = 30). So N_m is the pole-mass/linear-divergence normalisation.

### (v) The 𝒟 relations
- S_I = S₂/(S₁S₁) = e^{−𝒟} with JLL (20)–(21), read in arXiv and NPB 955 (2020) 115054, same numbers.
- This gives 𝒟 = 2𝒟₁ − 𝒟₂, so **𝒟₁ = (𝒟 + 𝒟₂)/2**. JLL state "2𝒟₁ − 𝒟₂ = 𝒟" in the text after (21).

### (vi)–(viii) Further items
- **(C.1) of Liu, JHEP 09 (2024) 030.** I checked it through its **middle (ω) representation**, i ∫dω/π sin(cω)Π1/(iω−E_k) = Σ_k e^{−cE_k}Π_{j≠k}(E_k−E_j)^{−1}. This was done with `quadosc` for n = 2, 3, 4 (≤1e−12). Stage 1 used finite-η E-integration instead.
- **GN inequalities (4.2)–(4.5) of Liu, JHEP 09 (2024) 093** (same numbering in arXiv and published):
  - (4.4) and (4.5) are proved **factor by factor** from |Γ(x+iy)/Γ(x)|² = Π_n[1 + y²/(x+n)²]^{−1}. The required inequalities are |n−l+c| ≤ n+1+2l−c and n+2l+2+2c ≤ 2(n+1+2l+c), true for 0 < c < ½.
  - For (4.2) and (4.3) I ran an adversarial grid plus Nelder–Mead search (l ≤ 8, |y| ≤ 1000, λ ≥ 0.01). The maxima were 0.98947 and 0.9999999899. Both equal 1 at λ = 0 and decrease there, since Re(a/b) > 0. For (4.3) the supremum 1 is approached only as |y| → ∞ (40-digit check at |y| = 1e4, 1e6). No violation was found.
- **One-loop threshold.** The IJJSZ kernel gives (2/(1−y))(L_z + ln(1−y) − 1) for 0 < y < 1 and 2ln(y−1)/(y−1) for y > 1. This equals the JLS J_f^(1) at power (1−y)^{−1}: arXiv (4.10), JHEP **(4.11)**.

**Verdict: confirmed (equation numbers as above).** These are cross-checks, not new. Texkeys Ji:2023pba, Liu:2023onm (JHEP 02 (2024) 204), Liu:2023pjb, Liu:2024omb, Ebert:2018gzl, Ji:2019sxk and Jain:2008gb all resolve on INSPIRE.

---------------------------------------------------------------------------------------------------------

## Agreement with stage 1
I agree with all five stage-1 verdicts and with their required corrections:
- N25: the plus-trap transcription.
- N27: the accuracy figure and the Ji:2020ect attribution.
- N28: "first super-leading term", leading-power equality, single-author Frixione.
- N29: (2.50) vs (2.52).

New in stage 2:
1. N26 is **in the literature**: Echevarria–Scimemi–Vladimirov 2016, eqs. (5)–(6). There is also an exact closed form for the distributional limit.
2. Published-vs-arXiv equation numbering:
   - **Liu–Neubert**: JHEP (2.1), (2.3) vs arXiv (1), (3).
   - **JLS**: JHEP (3.12)/(4.11)/(4.12) vs arXiv (3.13)/(4.10)/(4.11).
   - IJJSZ, BNS, CRS, Frixione, Liu–Su, Liu 2024a/b, JLL and Radyushkin 2018 have the same numbers in both.
   - Not checked against the published version (not open access): LUXqed (6), RMP (32), ESV (5)–(6). Cite those with arXiv numbering.
3. The CRS negativity interval at μ = 0.8 GeV is (0.264, 1), not [0.28, 0.98].
4. N27 is verified pointwise, to 1e−21, in both ξ and ζ.
5. I_as has an exact finite-ε closed form; the trapping and non-trapping were demonstrated by explicit contour deformations.
6. The LUXqed/Frixione comparison is cross-checked by an independent DR light-cone wave-function derivation; the BK eigenvalue by the complex Beta function.
