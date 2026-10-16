# Final claim verdicts (two-stage verification for errata and new results)
Status legend: confirmed = confirmed by both independent verifiers (errata/new results) or by the stage-1 verifier (other kinds); disputed = stage-2 verifier did not confirm; refuted / unresolved as stated.

## E01 — erratum — **confirmed**

**Claim:** Hybrid-scheme one-loop kernel printed as C_hyb = C_ratio + (3a/2)[−1/|1−ξ|_+ + 2Si((1−ξ)λ_S)/(π(1−ξ))], with 1/|u|_+ = lim_{β→0}[θ(|u|−β)/|u| + 2δ(u)ln β] (a = α_sC_F/2π, λ_S = z_S p^z). This gives ∫dξ C_hyb = 1 + 3a ln(λ_S e^{γ_E}), about 10% at λ_S ≈ 1, and violates vector-current conservation. Correct: the whole bracket is a plus distribution on ℝ (as in Su et al. 2023).

**Printable version:** Ji et al., NPB 964 (2021) 115311, eqs. (33)–(34) (arXiv:2008.03886, eq. hybridm2), repeated in RMP 93 (2021) 035005 (arXiv:2004.03543v2, eqs. (120)–(121)), print C_hybrid(ξ) = C_ratio(ξ) + (3a/2)[−1/|1−ξ|_+ + 2Si((1−ξ)λ_S)/(π(1−ξ))]. Here 1/|1−ξ|_+ ≡ lim_{β→0+}[θ(|1−ξ|−β)/|1−ξ| + 2δ(1−ξ)lnβ], a = α_sC_F/2π and λ_S = z_S p^z.

This is not the Fourier transform of their own coordinate kernel, eq. (30), which is C_ratio + (3a/2)δ(1−α)ln(z²/z_S²)θ(|z|−z_S). It exceeds that transform by 3a ln(λ_S e^{γ_E})δ(1−ξ). Hence ∫dξ C_hybrid = 1 + 3a ln(λ_S e^{γ_E}), about 0.09–0.11 at λ_S = 1, which violates quark-number (vector-current) conservation.

The correct one-loop kernel is C_hybrid = C_ratio + (3a/2)[−1/|1−ξ| + 2Si((1−ξ)λ_S)/(π(1−ξ))]^{[−∞,∞]}_{+(1)}, with λ_S = z_S|p^z|. That is, the printed form minus 3a ln(λ_S e^{γ_E})δ(1−ξ). This form appears in Chou–Chen, PRD 106 (2022) 014507, eq. (35), and in Su et al., NPB 991 (2023) 116201, eq. (A.14).

**Literature check:** Yes, so this is not a new result. Chou & Chen, PRD 106 (2022) 014507 (arXiv:2204.08343), eq. (35), give the plus-on-ℝ kernel with |y|. The text after their eq. (37) says quark-number conservation is violated in Ji et al.'s expression, and notes the y vs |y| difference. Su et al., NPB 991 (2023) 116201, eq. (A.14), print the corrected form and cite Chou–Chen. INSPIRE: none of the 35 papers citing Ji:2020brr before July 2022 printed the kernel. Chou–Chen (April 2022) is therefore the first published correction found.

## E02 — erratum — **confirmed**

**Claim:** Quasi-TMD factorization is printed with e^{K ln(ζ_z/ζ)} and the ratio (ζ_z1/ζ_z2)^K, inconsistent with 2ζ∂_ζ ln f = K. Correct: f̃√S_I = H(ζ_z/μ²)e^{½K ln(ζ_z/ζ)}f^TMD; ratio (ζ_z1/ζ_z2)^{K/2} = (P_1^z/P_2^z)^K (ESZ form); LFWF: ψ̃^±√S_r = e^{½ln((∓ζ_z−i0)/ζ)K}H^±ψ^±. At one loop (a = α_sC_F/2π), f̃^(1) = a[−½L_b² + L_b(5/2−L_z) − 3/2 − ½L_z² + L_z] and S_r^(1) = K^(1) = −2aL_b; the printed form leaves a residual L_b(L_z − L_ζ).

**Printable version:** Several papers print the quasi-TMD factorization without the factor ½ in the Collins–Soper exponent:
- PLB 811 (2020) 135946, eq. (22): f̃√S_r = H e^{K ln(ζ_z/ζ)} f^TMD.
- RMP 93 (2021) 035005 (arXiv:2004.03543v2): eq. (209), f^TMD = H e^{−ln(ζ_z/ζ)K} f̃ S_r^{1/2}, and eq. (210), the ratio with (ζ_z1/ζ_z2)^K.
- APPB 53 (2022) 4-A2: eqs. (53) and (75).
- arXiv:2106.05310v1: eqs. (49), (51), (73).

This contradicts the CS equation 2ζ∂_ζ ln f^TMD = K printed in the same papers.

The correct form is f̃√S_r = H(ζ_z/μ²) e^{½K ln(ζ_z/ζ)} f^TMD. This is APPB eq. (52), ESZ PRD 99 (2019) 034505 eq. (24), and ESSZ JHEP 04 (2022) 178. The ratio is f̃(ζ_z1)/f̃(ζ_z2) = [H(ζ_z1)/H(ζ_z2)](ζ_z1/ζ_z2)^{K/2}, where (ζ_z1/ζ_z2)^{K/2} = (P_1^z/P_2^z)^K at fixed x (ESZ eq. (27)).

At one loop (a = α_sC_F/2π):
- f̃^(1) = a[−½L_b² + L_b(5/2−L_z) − 3/2 − ½L_z² + L_z].
- S_r^(1) = K^(1) = −2aL_b.
- The printed exponent leaves the b-dependent residual aL_b(L_z−L_ζ).

The published PRD 105 (2022) 076014 is correct: its eqs. (49), (51), (74) have the ½, and footnote 1 notes the omission elsewhere.

For the LFWF, consistency with PRD 105's one-loop eqs. (63), (69), (72), (75), (76) requires ψ̃^±√S_r = H^± e^{½ln((∓ζ_z+i0)/ζ)K} ψ^±, as written by Liu–Su JHEP 2024, 204. The printed '−i0' is inconsistent for ψ^+.

**Literature check:** Yes, partly by the original authors. PRD 105 (2022) 076014, footnote 1, states that the ½ is missing in the RMP and in NPB 955. The correct ½ form was already in ESZ PRD 99 (2019) 034505, eqs. (24) and (27), and in ESSZ JHEP 04 (2022) 178. Liu's own APPB eq. (52) is also correct. The LFWF '+i0' prescription appears without comment in Liu–Su, JHEP 2024, 204 (arXiv:2311.06907). I found no explicit published note that the '−i0' in PRD 105 eqs. (49)/(74) is a typo.

## E03 — erratum — **confirmed**

**Claim:** BVZ eq. (cR): R^∥_Q and R^⊥_Q omit q(x)ln(1−x) relative to their own correct eqs. (t4-Qparallel),(t4-Qperp): Q^∥ = q + (κΛ²/(x²P_z²)){∫_{|x|}^1(dy/y)y²/[1−y]_+ q(x/y) + q − |x|q′}, with the [0,1] plus distribution. The printed form is off by ~30% (∥) and ~24% (⊥) at x = 0.5. The asymptotic Λ²/(x²(1−x)P_z²) is unaffected.

**Printable version:** Braun–Vladimirov–Zhang, PRD 99 (2019) 014013, eqs. (63)–(64) (arXiv eq. cR, for x > 0) print:
- R^∥_Q = (x̄/q){∫_x^1 dy/(1−y)[yq(x/y)−q(x)] + q − xq'};
- R^⊥_Q = (x̄/q){∫_x^1 dy/(1−y)[y(2y−1)q(x/y)−q(x)] + 2q − xq'}.

Both omit q(x)ln(1−x) inside the braces, relative to their own eqs. (61)–(62) with the [0,1] plus distribution of eq. (55).

Those equations are the correct second derivatives. For x > 0: Q^∥ = q + (κΛ²/(x²P_z²)){∫_x^1(dy/y) y²/[1−y]_+ q(x/y) + q − xq'}, and similarly for ⊥ (for general x the last term is −x q'(x)). Correct: R_Q^{∥,⊥} = R_Q^{∥,⊥}(printed) + (1−x)ln(1−x).

For BVZ's model (60), q = x^{−1/2}(1−x)³, at x = 0.5 the printed R is 31.6% (∥) and 24.0% (⊥) too large; the size depends on the model. The endpoint behaviour Λ²/(x²(1−x)P_z²) is unaffected.

**Literature check:** I did not find the omission of q ln(1−x) in eq. (64) reported anywhere. I searched INSPIRE full text of BVZ citers for 'typo', 'misprint' and 'ln(1-x)'. A different typo in eq. (61), '−|x|q'' instead of '−xq'' for x < 0, was noted by Liu & Chen, PRD 104 (2021) 094501 (arXiv:2010.06623), in a footnote. Their momentum-space eq. (Qrenorm), written with ∫_0^1, implicitly contains q ln(1−|x|).

## E04 — erratum — **confirmed**

**Claim:** IJJSZ use P exp(−ig∫A^+) for the light-cone link and P exp(−ig∫A^z) for the space-like link. Since A^z = −A_z, these correspond to opposite signs of g in D_μ. Internal inconsistency, harmless at O(g²).

**Printable version:** IJJSZ, PRD 98 (2018) 056004, define the light-cone link as U(ξ⁻,0) = Pexp(−ig∫_0^{ξ⁻}dη⁻A⁺) (eq. 2) and the space-like link as U(z,0) = Pexp(−ig∫_0^z dz′A^z) (eq. 5).

Along x⁻, dx^μA_μ = dη⁻A⁺; along ẑ, dx^μA_μ = −dz′A^z. Gauge covariance therefore requires D_μ = ∂_μ + igA_μ for eq. (2) but D_μ = ∂_μ − igA_μ for eq. (5). The paper's vertex −igT^aγ^μ (eq. 41) corresponds to D = ∂ + igA, so eq. (5) should read Pexp(+ig∫dz′A^z).

The explicit one-loop sail integrands of eq. (41) correspond to the consistent link, so the published one-loop results are unaffected. The relative sign of the link and vertex couplings does matter at O(g²), since flipping the sails changes the result.

**Literature check:** Not found. I searched INSPIRE full text of papers citing IJJSZ for 'typo', 'misprint', 'sign of the coupling' and 'opposite sign'. None reports the inconsistency between eqs. (2) and (5).

## E05 — erratum — **confirmed**

**Claim:** JZZ: 'no lower-dimension operator can mix' is correct but incomplete. For chirally non-symmetric lattice fermions there is same-dimension mixing: O^R_Γ = Z_φ²e^{−m|z|}O_{Γ′}, Γ′ = Γ + r sgn(z){n̸,Γ} + r²n̸Γn̸. There is none for Γ = γ^t.

**Printable version:** JZZ, PRL 120 (2018) 112001, state that 'there is no lower-dimension operator that can mix' with the nonlocal quark bilinear on the lattice. This is correct but incomplete.

For chirally non-symmetric lattice fermions (e.g. Wilson-type), the operator mixes at O(a⁰) with the same-dimension structure {n̸,Γ}: O^R_Γ(z) = Z_φ²e^{−m|z|}O_{Γ′}(z), with Γ′ = Γ + r_mix sgn(z){n̸,Γ} + r_mix²n̸Γn̸, where r_mix = O(g²). Sources: Green–Jansen–Steffens, PRL 121 (2018) 022004, eqs. (5)–(6); one-loop: Constantinou–Panagopoulos, PRD 96 (2017) 054506; symmetry analysis: Chen et al., CPC 43 (2019) 103101.

For Γ = γ^t with n along z, {n̸,γ^t} = 0 and n̸γ^tn̸ ∝ γ^t. So there is no O(a⁰) mixing, only a rescaling. O(a) mixing with dimension-4 operators remains for every Γ.

**Literature check:** The physics is in the literature: Constantinou & Panagopoulos 2017 (one loop), Chen et al., CPC 43 (2019) 103101 (arXiv:1710.01089, symmetry analysis), Green–Jansen–Steffens 2018 (master formula), and the RMP 2021. Only the editorial remark that JZZ's sentence is correct but incomplete is ours.

## E06 — erratum — **confirmed**

**Claim:** Ji 2013's matching q̃ = ∫_x^1(dy/y)Z(x/y, μ/P^z)q(y) is superseded by ∫(dy/|y|)C(x/y, μ/(|y|P^z))f(y). Using P^z instead of |y|P^z errs at O(α_s) by terms ∝ ln|y| P_qq⊗f [V].

**Printable version:** Ji 2013 (PRL 110, 262002; arXiv:1305.1539, eq. 11) writes q̃(x,μ²,P^z) = ∫_x^1(dy/y)Z(x/y, μ/P^z)q(y,μ²). This is superseded by q̃(x,P^z) = ∫_{−1}^{1}(dy/|y|)C(x/y, μ_R/μ, μ/(|y|P^z))q(y,μ) (IJJSZ, PRD 98 (2018) 056004, eq. 27), which follows exactly from coordinate-space factorization by the substitution λ′ = yλ.

Using the hadron momentum P^z instead of the parton momentum |y|P^z changes the one-loop MS-bar kernel (IJJSZ eq. 68) by C(ξ,μ/P^z) − C(ξ,μ/(|y|P^z)) = −(α_sC_F/π)ln|y|(1+ξ²)/(1−ξ)_+ θ(0<ξ<1). This equals −(α_s/π)ln|y|[P_qq(ξ) − (3/2)C_Fδ(1−ξ)]; in the ratio scheme it is −(α_s/π)ln|y|P_qq(ξ). This is an O(α_s) error.

The early range ∫_x^1 also omits the |y| < |x| and y < 0 contributions. The early form is graded [V].

**Literature check:** Yes, this is not new. IJJSZ, PRD 98 (2018) 056004, state explicitly (Introduction, and the text after eq. 27) that the matching coefficient depends on p^z = |y|P^z, not the choice p^z = P^z used in the early papers [Ji 2013, Ji 2014, Xiong et al. 2013]. Before that, Ji–Schäfer–Xiong–Zhang, PRD 92 (2015) 014039 (arXiv:1506.00248), wrote for quasi-GPDs that 'p^z shall be replaced by yP^z'.

## E07 — erratum — **confirmed**

**Claim:** Literature errors reported by others. (i) Alexandrou et al. 2015 TMC formula does not conserve particle number (Chen et al. 2016). (ii) Bent Euclidean soft functions (Ji:2014hxa, Ebert:2019okf) carry the cusp at Euclidean angle π/2 and are wrong from two loops (Ji–Liu–Liu 2020; ESSZ). (iii) Jia et al. 2024 correct an earlier 't Hooft-model quasi-PDF expression. (iv) Xiong et al. 2014 cutoff matching has a Λ_UV/((1−y)²P^z) linear divergence.

**Printable version:** (i) The quasi-PDF target-mass formula of Alexandrou et al., PRD 92 (2015) 014502, eq. (11), q~(x) = q~0(xi)/(1+mu xi^2) with xi = 2x/(1+sqrt(1+4mu x^2)) and mu = M^2/(4Pz^2), is not the inverse of their eq. (4), a~_n = K_n a~_n^(0) with K_n = sum_j C(n-j,j) mu^j.
- It gives int dx x^(n-1) q~ = int dxi xi^(n-1) q~0(xi)/(1-mu xi^2)^(n+1), so already int q~ = int q~0 + 2 mu <xi^2> + O(mu^2): particle number is not conserved.
- The exact inversion is Chen et al., NPB 911 (2016) 246, App. B, eq. (61): q~(x) = [(f+/2) q(2x/f+) - (f-/2) q(-2x/f-)]/sqrt(1+4c), with f+- = sqrt(1+4c) +- 1 and c = M^2/(4Pz^2). Its moments are K_n <x^(n-1)>_q exactly (eq. (62)), and Chen et al. note that the earlier result does not conserve quark number.

(ii) The Euclidean 'bent' soft subtractions of Ji-Sun-Xiong-Yuan, PRD 91 (2015) 074009, eqs. (3)-(4), and Ebert-Stewart-Zhao, JHEP 09 (2019) 037, eq. (4.26), contain only cusps between orthogonal space-like directions, i.e. Euclidean angle pi/2.
- Their anomalous dimension is governed by Gamma_cusp(pi/2). This equals the large-hyperbolic-angle constant gamma_HH at one loop (-as CF/pi) but not at two loops.
- In units of (as/pi)^2: Gamma2(pi/2) = CF CA(pi^2/24 - 49/36) + (5/9) CF TF nf, while gamma_HH2 = CF CA(-49/36 + pi^2/12 - z3/2) + (5/9) CF TF nf. The difference is CF CA(z3/2 - pi^2/24), about 0.190 CF CA.
- These factors depend only on mu*b, so the mismatch produces a wrong ln(mu^2 b^2) term at O(as^2), which no b-independent kernel can absorb. The construction therefore fails from two loops.
- This was argued by Ji-Liu-Liu, NPB 955 (2020) 115054 (also PLB 811 (2020) 135946), and reported by Ebert-Schindler-Stewart-Zhao, JHEP 04 (2022) 178.

(iii) Jia-Mo-Xiong-Yu, PRD 109 (2024) 014042 (Sec. VII, eqs. (83)-(87), App. C), correct their own 't Hooft-model quasi-PDF of PRD 98 (2018) 054011.
- That expression missed an O(Nc^0) piece for flavour-neutral mesons, from O~_{1/2} and the next-to-leading Fock component. The piece vanishes as P -> infinity.
- They state that the same piece was also missed in Ma-Ji (2021) and Ji-Liu-Zahed (2019).

(iv) The transverse-momentum-cutoff one-loop quasi-PDF and matching of Xiong-Ji-Zhang-Zhao, PRD 90 (2014) 014051, eqs. (7), (8), (14)-(16), contain (as CF/2pi) Lambda/((1-y)^2 P^z), where Lambda is their cutoff mu.
- This is the linear divergence of the Wilson-line self-energy, delta m = as CF Lambda/2, which the authors kept in the matching.
- As stated in the RMP, the Lambda/P^z term spoils the 1/Pz^2 power counting, so a scheme without it is required.

**Literature check:** Yes, by construction: these are errors reported in the literature.
- (i) Chen et al., NPB 911 (2016) 246, App. B, and the main text after eq. (24).
- (ii) Ji-Liu-Liu, NPB 955 (2020) 115054 and PLB 811 (2020) 135946; reported by ESSZ, JHEP 04 (2022) 178, section 2. The explicit pi/2 identification and the two-loop mismatch value CF CA(z3/2 - pi^2/24)(as/pi)^2 are not printed there; they come from Kidonakis 2009 and GHKM 2016 evaluated here.
- (iii) Self-correction by Jia et al., PRD 109 (2024) 014042.
- (iv) Flagged by Xiong et al. themselves, and by the RMP 2021 (arXiv:2004.03543v2, Sec. II.B), which has overlapping authors.

## E08 — erratum — **confirmed**

**Claim:** APPB eq. (81) and PRD 105 eq. (72) give Γ_S^(2) with the wrong sign relative to their own Γ_S^(1) = +α_sC_F/π (there Γ_S = −γ_HH). Correct: Γ_S^(2) = (α_s²/π²)C_F[C_A(49/36 − π²/12 + ζ_3/2) − (5/18)n_f], where γ_HH = −α_sC_F/π + (α_s²/π²)C_F[C_A(−49/36 + π²/12 − ζ_3/2) + (5/9)T_Fn_f] is the constant in Γ_cusp(θ) → θΓ_cusp + γ_HH. The RMP and JHEP 2023 eq. (A.6) are correct.

**Printable version:** Gamma_S^(2) has the wrong overall sign relative to the papers' own conventions in two places:
- Liu, Acta Phys. Pol. B 53 (2022) 4-A2: the display defining Gamma_S^(2) directly below eq. (81).
- Ji-Liu, PRD 105 (2022) 076014: eq. (73) (eq. (72) of arXiv:2106.05310v1).
Both print Gamma_S^(2) = (as^2/pi^2)[CF CA(-49/36 + pi^2/12 - z3/2) + (5/18) CF nf].

In those papers mu^2 dlnS_I/dmu^2 = -Gamma_S and Gamma_S^(1) = +as CF/pi (APPB (77)-(80); PRD 105 (47), (48), (70)-(72)). Hence Gamma_S = -gamma_HH.

Correct value: Gamma_S^(2) = -gamma_HH^(2) = (as^2/pi^2) CF [CA(49/36 - pi^2/12 + z3/2) - (5/9) TF nf].

Here gamma_HH(as) = -as CF/pi + (as/pi)^2 CF [CA(-49/36 + pi^2/12 - z3/2) + (5/9) TF nf] + O(as^3) is the constant in Gamma_cusp(as,theta) -> theta Gamma_cusp(as) + gamma_HH(as). This refers to a single cusp, d/dln mu, with Gamma_cusp(as,theta) = (as CF/pi)(theta coth theta - 1) + O(as^2). It equals mu^2 dlnS_I/dmu^2.

The RMP value (arXiv:2004.03543v2, display after eq. (208), Gamma_S^(2) = -gamma_HH^(2)) and JHEP 08 (2023) 037 eq. (A.6) (2 gamma_HL - gamma_s = gamma_HH) are correct.

**Literature check:** Not as an erratum: INSPIRE records no erratum.
- JHEP 08 (2023) 037 (A.6) gives the correct gamma_HH^(2), but asserts that it agrees with the earlier formulas, citing RMP, PLB 811 and PRD 105.
- The RMP's Gamma_S^(2) has the correct sign for its stated Gamma_S^(1).

## E09 — erratum — **confirmed**

**Claim:** RMP eqs. (205)-(206) print d ln S_r/d ln μ² = +Γ_S. This contradicts Γ_S^(1) = +α_sC_F/π and S_r^(1) = −(α_sC_F/π)L_b. Correct: μ²d ln S_r/dμ² = −Γ_S = γ_HH.

**Printable version:** Ji et al., Rev. Mod. Phys. 93 (2021) 035005, eqs. (205)-(206) (numbering of arXiv:2004.03543v2 = accepted manuscript) contradict the paper's own eqs. (203), (204), (207) and its statements Gamma_S^(1) = as CF/pi and Gamma_S^(2) = -(as^2/pi^2)[CF CA(-49/36 + pi^2/12 - z3/2) + (5/18) CF nf]:
- (205) prints mu^2 dlnS_r/dmu^2 = Gamma_S.
- (206) prints mu^2 dlnS_DY/dmu^2 = -(Y+Y')Gamma_cusp - Gamma_S.

Those equations imply S_r^(1) = -(as CF/pi)L_b. Consistently with them and with (208), the RGEs must read:
- mu^2 dlnS_r/dmu^2 = -Gamma_S;
- mu^2 dlnS_DY/dmu^2 = -(Y+Y')Gamma_cusp + Gamma_S.

Convention-independent statement: mu^2 dlnS_r/dmu^2 = gamma_HH(as) = -as CF/pi + (as/pi)^2 CF [CA(-49/36 + pi^2/12 - z3/2) + (5/9) TF nf] + O(as^3).

**Literature check:** Not found in the literature.
- APPB (77)-(78) and PRD 105 (47)-(48) use the consistent relative sign.
- PLB 811 (20) is consistent with its own convention Gamma_S = gamma_HH.

## E10 — erratum — **confirmed**

**Claim:** PLB 811 eq. (26), γ_C^(2), is incorrect: it differs by −2γ_HH^(2) + C_Fn_f/(24π²); the C_F² term agrees. Correct (JHEP 2023 (A.13), dα/d ln μ = −β_0α², β_0 = 11C_A/(6π) − n_f/(3π)): γ̃_H^(1) = −C_F/π, γ̃_H^(2) = (1188ζ_3 − 99π² − 1108)/(432π²)C_FC_A − (36ζ_3 + 6 − 7π²)/(12π²)C_F² + (1/24 + 10/(27π²))C_Fn_f.

**Printable version:** Ji-Liu-Liu, PLB 811 (2020) 135946, eq. (26) and the values below it, gives gamma_C^(2) = (a1 CF CA + a2 CF^2 + a3 CF nf)/(16 pi^2), with a1 = 60 z3 - 19pi^2/3 + 68/27, a2 = -48 z3 + 28pi^2/3 - 8, a3 = 2pi^2/3 - 62/27. This is incorrect.
- It differs from the correct value by -2 gamma_HH^(2) + CF nf/(24 pi^2) = -CF[CA(12pi^2 - 196 - 72 z3) + 37 nf]/(72 pi^2).
- The CF^2 term agrees.

Correct value. With mu dlnH/dmu = Gamma_cusp ln(zeta_z/mu^2) + gamma_C and gamma_C = sum_n gamma_C^(n) as^n:
- gamma_C^(1) = -CF/pi;
- gamma_C^(2) = (1188 z3 - 99pi^2 - 1108)/(432 pi^2) CF CA - (36 z3 + 6 - 7pi^2)/(12 pi^2) CF^2 + (1/24 + 10/(27 pi^2)) CF nf, for TF = 1/2.
- This is JHEP 08 (2023) 037, eqs. (A.12)-(A.13).
- Equivalently gamma_C = 2(gamma' - gamma~_J) = gamma_V + 2 gamma_F + gamma_HH.
- Numerically, for nf = 4: 0.1034, versus 0.7494 in PLB.
- The coefficients do not depend on the beta-function convention.

**Literature check:** Not as an erratum: there is no erratum to PLB 811.
- The correct value appears in Ji-Liu-Su, JHEP 08 (2023) 037 (A.13). That paper nevertheless says gamma_C 'is known to two-loop' and cites PLB 811 and PRD 105, without noting the discrepancy.
- del Rio-Vladimirov, PRD 108 (2023) 114009, computed the NNLO quasi-TMD coefficient directly and state agreement with Ji-Liu-Su.
- The value also follows from Bell 2009 (gamma') together with Broadhurst-Grozin 1995 (gamma~_J).

## E11 — erratum — **confirmed**

**Claim:** The two-loop L_b² coefficient of ln S_I, printed as α_s²β_0C_F/(2π) with β_0 = −(1/2π)(11C_A/3 − 4N_fT_F/3), is a factor 2 too large, and the single-log sign in APPB (81) is wrong. Correct: ln S_I = −(α_sC_F/π)L_b + α_s²[−(C_Fβ_0/(8π²))L_b² + γ̂_HH L_b + c_2], with β_0 = 11C_A/3 − (4/3)T_Fn_f and γ̂_HH = (C_F/π²)[C_A(−49/36 + π²/12 − ζ_3/2) + (5/9)T_Fn_f].

**Printable version:** Correct two-loop structure. With mu^2 das/dmu^2 = -beta0 as^2/(4pi) and beta0 = 11CA/3 - (4/3)TF nf, the RGE mu^2 dlnS_I/dmu^2 = gamma_HH(as(mu)) fixes:
- ln S_I = -(as CF/pi) L_b + as^2 [-(CF beta0/(8pi^2)) L_b^2 + gammahat_HH L_b + c2] + O(as^3);
- L_b = ln(mu^2 b^2/b0^2);
- gammahat_HH = (CF/pi^2)[CA(-49/36 + pi^2/12 - z3/2) + (5/9) TF nf].

The printed L_b^2 coefficient is twice the correct value in two places:
- Liu, APPB 53 (2022) 4-A2, eq. (81): +as^2 (beta0 CF/2pi) L_b^2 in ln S_I.
- RMP 93 (2021) 035005, eq. (208) of arXiv:2004.03543v2: -(as^2 beta0 CF/2pi) L_b^2 in D = -ln S_r.
Both use beta0 = -(11CA/3 - 4NF TF/3)/(2pi). In that convention the correct coefficient in ln S_I is as^2 beta0 CF/(4pi).

Single-log term.
- In APPB (81) the single-log term evaluates to -gammahat_HH as^2 L_b instead of +gammahat_HH as^2 L_b, because of the wrong-sign Gamma_S^(2) (see E08).
- In RMP (208) the single log is correct.

**Literature check:** Not found in the literature.

## E12 — erratum — **confirmed**

**Claim:** Guo–Ji–Liu 2021 eq. (16): the gluon GPD has a spurious ½ that propagates to eqs. (24)-(26). Corrected in Guo–Ji–Liu–Yang 2023 eqs. (1),(5): F_g = (1/(P̄^+)²)∫(dλ/2π)e^{iλx}⟨P′|F^{a+i}(−λn/2)F^{a+}_i(λn/2)|P⟩, |G|² = (4/ξ⁴){(1 − t/(4M_N²))E_2² − 2E_2(H_2+E_2) + (1−ξ²)(H_2+E_2)²}, a factor 4 relative to 2021.

**Printable version:** Guo-Ji-Liu, PRD 103 (2021) 096010, eq. (16) defines F_g with a colour trace, Tr{F^{+i}F^+_i} = (1/2) sum_a F^{a+i}F^{a+}_i. This is half the standard gluon GPD of Diehl, Phys. Rept. 388 (2003) 41, eq. (18), for which H^g(x,0,0) = x g(x).
- It is inconsistent with the paper's own moment relations, eqs. (21)-(23) and (32).
- It is also inconsistent with the amplitude, eqs. (13)-(14) and (17). With the standard F_g these reproduce the classic LO high-energy result of Ryskin et al., Z. Phys. C 76 (1997) 231, eq. (2); with the 1/2 they give one quarter of it.

The spurious 1/2 enters through eq. (24) into eq. (26), and into the polarized eqs. (58)-(59). Eq. (25) is unaffected.

The authors corrected it in Guo-Ji-Liu-Yang, PRD 108 (2023) 034003, Sec. II, leaving eqs. (13) and (17) unchanged:
- eq. (1): F_g = (1/(P^+)^2) int (dlambda/2pi) e^{i lambda x} <P'| F^{a+i}(-lambda n/2) F^{a}_i^{+}(lambda n/2) |P>, with colour summed and the contraction meaning sum_{i=1,2} F^{a+i}F^{a+i};
- eq. (5): |G|^2 = (4/xi^4){(1 - t/(4M_N^2)) E_2^2 - 2E_2(H_2+E_2) + (1-xi^2)(H_2+E_2)^2}, averaged over proton spin. This is a factor 4 relative to eq. (26) of 2021.

**Literature check:** Yes: the authors corrected it themselves in Guo-Ji-Liu-Yang, PRD 108 (2023) 034003, Sec. II, eqs. (1) and (5), which also extends the factor 4 to the polarized eqs. (58)-(59).

## E13 — erratum — **confirmed**

**Claim:** APPB App. F cites the 'edge of the wedge' theorem for the complex Lorentz covariance of Wightman functions; the theorem used is Bargmann–Hall–Wightman. Terminology only; Liu 2024 is correct.

**Printable version:** Liu (APPB 53 (2022) 4-A2, App. F) invokes the 'edge of the wedge' theorem for the covariance of the analytically continued Wightman functions under proper complex Lorentz transformations on the extended tube. That property is the Bargmann-Hall-Wightman theorem (Hall-Wightman 1957; Streater-Wightman Thm. 2-11). It requires only the spectral condition (tube analyticity, temperedness) and real Lorentz covariance; it needs neither locality nor positivity. The edge-of-the-wedge theorem glues holomorphic functions whose boundary values coincide on a real edge. Together with locality it combines the permuted Wightman functions, and that is where App. F's 'causality' input belongs: the re-ordering of the W_DY points. The conclusion (F.6) is unaffected; the issue is terminology only. The complex Lorentz map is Λ(t,z) = (iz,it), a boost with rapidity iπ/2 and det = +1 (Liu, JHEP 09 (2024) 030, eq. (3.25)), not (it,iz). Liu 2024 states the covariance correctly.

**Literature check:** Terminology note only. No published erratum to APPB 2022 exists. Liu himself phrases it correctly in Liu:2023pjb (JHEP 09 (2024) 030, §2.1, eq. (3.25)) and uses edge of the wedge correctly in Ji:2026vir (arXiv:2601.12189 §5.1).

## E14 — erratum — **confirmed**

**Claim:** Coleman–Norton 1965 assume that a momentum-space pinch is equivalent to a Feynman-parameter pinch. This fails for massless graphs: the one-loop self-energy at p² = 0 has a collinear momentum pinch, but F = −p²α_1α_2 ≡ 0, so there is no parameter pinch. Eikonal parameter pinches are independent, and there is a zero-eigenvalue gap in the massive case. Print: proof [V], result true.

**Printable version:** Coleman and Norton (Nuovo Cim. 38 (1965) 438) derive the physical-region singularity criterion from the pure Feynman-parameter representation. As Collins observed (arXiv:2007.04085, §IV, App. D), their proof tacitly assumes that the momentum-space contour is pinched if and only if the parameter contour is. Their trapping argument (A = ½E_ijη_iη_j) also requires every eigenvalue of E_ij to be non-zero.
- Massless graphs. The tacit assumption fails. The one-loop massless self-energy has, at p² = 0, a line of collinear momentum-space pinches k = αp, 0 ≤ α ≤ 1. In the parametric form, F = -p²α₁α₂ is p² times a p-independent function of α. The α-integrand therefore has no pinch, and the collinear singularity resides entirely in the prefactor (-p²)^{n/2-2}. At p² = 0, F and all its α-derivatives vanish identically, so the CN quadratic form is totally degenerate.
- Linear denominators (non-relativistic or Wilson-line/eikonal). The parametric form is pathological. In Collins' example the ω-integral equals -4iπm δ(α-½)/(2Em-2k²+2pk-p²), localized at α = ½ whether or not the momentum integral is pinched. The momentum integral is pinched only at E = p²/4m.
- Massive theories. The argument fails at zero-eigenvalue points, which CN call very exceptional and which remain unresolved.
Status: CN's proof is [V] for the massless and linear-denominator cases, with a gap at exceptional massive points. The result is proven by Collins 2020, Thm. 'main.contour' (unrefereed; denominators at most quadratic, plus a sign condition): a physical-region trap exists iff there is a Landau point with λ_j ≥ 0, i.e. iff there is a classical Coleman-Norton process. The literal statement 'singularity iff classical process' is false for massless graphs: the massless bubble is pinched at k = 0 and k = p for every p but is singular only at p² = 0.

**Literature check:** Yes, this is not a new result of ours. Collins:2020euz (arXiv:2007.04085, unrefereed) §I, §IV ('Evidently Coleman and Norton have assumed...'), App. D.1-D.2. Related: T. Kawai, RIMS Kokyuroku 856 (1994) 107, on the massless Coleman-Norton picture.

## E15 — erratum — **confirmed**

**Claim:** ELOP 1966 §2.1 is heuristic. The 'normal' deformation is undefined without a metric. Non-zero first-order shifts are assumed, which is false: anomalous deformations exist, e.g. for 1/(E − p²/2m + iε). Condition (2.1.19b) lacks λ_j ≥ 0. 'Landau condition ⇒ singularity' is false, the condition being only necessary [V]. Collins 2011 §5.4.3: there is no complete published proof.

**Printable version:** (i) The Landau derivation in ELOP (1966) §2.1 is avowedly heuristic.
- p. 48: 'We shall be content with plausibility arguments'. Collins 2011 §5.4.3 and Collins 2020 §I quote the fuller sentence, which begins 'A proper proof needs the use of topology'.
- p. 50: a rigorous treatment 'requires homology theory', with a reference to Fotiadi-Froissart-Lascoux-Pham (1964, unpublished; 'see also Topology 4, 159 (1965)').
- Its multidimensional argument distorts the contour 'in the direction of the normal to S_r'.
Collins (arXiv:2007.04085 §IV) objects on three points:
- A normal is not canonically defined: the gradient is a dual vector, and the allowed deformation directions form an open half-space.
- The tacit assumption that avoiding a singularity requires a non-zero first-order shift is unjustified.
- Condition (2.1.19b) has no positivity constraint λ_j ≥ 0. It is the correct general necessary condition for complex singularity surfaces, but it is not sufficient for a physical-region pinch.
(ii) That assumption is false in two or more real dimensions; it is true in one dimension (Collins App. B.2). Collins App. B.1 gives anomalous singularity-avoiding deformations for i/(E-p²/2m+iε), namely (η,ξ) = (|E_R|+2|p_R|, m) and (p_R+p_R²/2m-E_R, m) [V].
(iii) The Landau condition with λ_j ≥ 0 is necessary and sufficient for a trap of the contour (Collins 2020, Thm. main.contour, unrefereed) and necessary for a singularity. It is not sufficient for a singularity of the integral [V]. Counterexamples: Collins App. A (power singularity cancelled by a numerator); App. D.1 (massless bubble, pinched for all p, singular only at p² = 0).
(iv) Collins (2011, §5.4.3, p. 110) states that he found no published explicit and complete proof that the Landau equations are both necessary and sufficient for a pinch singular surface, and that textbook treatments are incomplete. Do not add that the FFLP work was never published: ELOP itself cites Fotiadi et al., Topology 4 (1965) 159.

**Literature check:** Yes, not new. Collins:2011zzd §5.4.3 (p. 110; quotes ELOP p. 48). Collins:2020euz §I, §IV (ELOP paragraph), Apps. A, B.1, B.2. ELOP p. 50 and bibliography p. 280 themselves point to the homological treatment (FFLP 1964 unpublished; Topology 4 (1965) 159).

## E16 — erratum — **confirmed**

**Claim:** BFH 2026: one-jettiness in colour-singlet + jet production has coherence-violating logs. dσ^CVL ≃ Σ_a𝒜_a(α_s/π)⁴(−iπ)²(1/480)ln⁶(1/τ_1), with 𝒜_q = (8/3)N_c²T_R⁴f^q_Af^g_Bσ_qg and 𝒜_g = −(32/3)N_c²T_R⁴f^g_Af^q_Bσ_gq; α_s^nL^{2n−2} terms are expected. This contradicts the claim of Alioli et al. 2024 that τ_1 in V+jet is free of NGLs/SLLs. Single group; [V] at LL-CVL level.

**Printable version:** Banfi, Forshaw and Holguin (PRL 136 (2026) 221901, arXiv:2511.11799) show that the one-jettiness distribution in colour-singlet + jet production contains coherence-violating (super-super-leading) logarithms. The leading term is α_s⁴L⁶ relative to Born, L = ln(1/τ1). Their computation is for the qg → qZ channel, with the cumulant in τ1 taken differential in the Born variables, at fixed α_s and with PDFs at μ_F = τ1 Q:
dσ1^CVL/(dx_a dx_b dB) ≈ Σ_{a=q,g} A_a (α_s/π)⁴ (-iπ)² (1/480) ln⁶(1/τ1),
with A_q = (8/3)N_c²T_R⁴ f^q_A f^g_B σ^(0)_qg(B) and A_g = -(32/3)N_c²T_R⁴ f^g_A f^q_B σ^(0)_gq(B). They expect α_s^n L^{2n-2} terms for n ≥ 4, so the standard form σ exp[-(α_s/2π)L²(2C_F+C_A)][g0 + α_s g1 + ...] cannot hold. This contradicts the statement of Alioli et al. (PRD 109 (2024) 094009) that one-jettiness for colour-singlet + jet production 'does not suffer from superleading or nonglobal logarithms', specifically its super-leading part. That statement underlies N³LL resummation and N-jettiness slicing. The result is confirmed for the qg → q channel by Becher, Hager, Neubert and Schwienbacher (PRL 137 (2026) 121902) in a SCET framework with Glauber and new modes. Grade [V]: an explicit leading-log CVL computation, established by two groups using different methods.

**Literature check:** Yes. Banfi:2025mra (PRL 136 (2026) 221901) is itself the source, independently confirmed by Becher:2026kbr (Becher-Hager-Neubert-Schwienbacher, 'Factorization beyond Coherence', PRL 137 (2026) 121902, arXiv:2603.12383). The claim's 'single group' is outdated.

## E17 — erratum — **confirmed**

**Claim:** Aybat–Rogers 2011 eq. (3), ζ_F = 2M_p²x²e^{2(y_P−y_s)}, is twice the standard ζ = 2(xP^+)²e^{−2y_n}. It contradicts their own √(ζ_Fζ_D) ≈ Q², and their (A10),(A11),(B1) agree with ours only without the factor 2. A misprint; do not copy.

**Printable version:** Aybat and Rogers (PRD 83 (2011) 114042, arXiv:1101.5057v2) print ζ_F = 2M_p²x²e^{2(y_P-y_s)} in eq. (3) and ζ_D = 2(M_H²/z²)e^{2(y_s-y_h)} in eq. (4). In their light-cone convention V^± = (V⁰±V^z)/√2, M²e^{2y_P} = 2(P⁺)². Both printed values are therefore twice the standard ones: ζ_F = M_p²x²e^{2(y_P-y_s)} = 2(xP⁺)²e^{-2y_s} and ζ_D = (M_h²/z²)e^{2(y_s-y_h)} = 2(P_h⁻/z)²e^{2y_s}. These are the normalizations of Collins-Rogers 2013 and of Aybat-Collins-Qiu-Rogers 2012. With the printed forms √(ζ_Fζ_D) = 2Q², which contradicts:
- the authors' own statement √(ζ_Fζ_D) ≈ Q² and their choice √ζ_F = √ζ_D = Q;
- RG invariance of H·F·D, given their (B1) γ_F = γ_D = (α_s C_F/π)(3/2 - ln ζ/μ²) and their one-loop hard factor (arXiv:1107.3973).
Their one-loop results (A11) and (B1) agree with the standard Collins-scheme expressions only for the factor-free ζ. (A10) is ζ-independent. The factor 2 is a misprint; do not copy eqs. (3),(4).

**Literature check:** Implicitly corrected, but no explicit erratum exists. The same authors use the factor-free normalization in Aybat:2011ge (PRD 85 (2012) 034043, eqs. (zetaF),(zetaD)) and state ζ₁ζ₂ = Q⁴ in Aybat:2011vb (arXiv:1107.3973). Collins:2012uy (PRD 87 (2013) 034018) eqs. (zeta.A),(zeta.B) also use the standard form.

## E18 — erratum — **confirmed**

**Claim:** Collins arXiv:0708.4410v1 eq. (10) has a spurious numerator Π_j(k_T² + m_q²), inconsistent with its first line, eq. (11), dimensions and ∫d²k_T(I_1+I_2) = 0. Consistent form: I_1 = 𝒩F², I_2 = −𝒩G/(k_T² + m_q²), 𝒩 = λ²g_1²g_2(g_2+g_1)x(1−x)/(256π⁷).

**Printable version:** In Collins, arXiv:0708.4410v1 (unpublished), the second line of eq. (10) contains a spurious numerator ∏_{j=1,2}(k_T²+m_q²). Consistency with the first line of (10), with eq. (11), with dimensional analysis (a TMD density has dimension M⁻²) and with the stated ∫d²k_T(I₁+I₂) = 0 requires:
- I₁(k_T) = 𝒩 F(k_T)², with F(k_T) = ∫d²l_T / [(l_T²+m_g²)((k_T-l_T)²+m_q²)];
- I₂(k_T) = -𝒩 G(k_T)/(k_T²+m_q²), as printed, with G(k_T) = ∫d²l_{1T} d²l_{2T} / [(l_{1T}²+m_g²)(l_{2T}²+m_g²)((k_T-l_{1T}-l_{2T})²+m_q²)];
- 𝒩 = λ²g₁²g₂(g₂+g₁)x(1-x)/(256π⁷).
With these forms, ∫d²k_T(I₁+I₂) = 0 holds exactly, so collinear factorization survives. Meanwhile I₁(0)+I₂(0) = 𝒩[F(0)² - G(0)/m_q²] < 0, for example -21.0𝒩 at (m_g,m_q) = (0.5,1). The first line of (10) also lacks squares in '(k-l_j)-m_q²' and '(p-k+l_j)-m_q²', and carries +iε on the conjugate side of the cut.

**Literature check:** Not recorded anywhere. The paper is an unpublished preprint with only arXiv v1 (INSPIRE Collins:2007jp, no journal version), and I found no erratum.

## E19 — erratum — **confirmed**

**Claim:** WITHDRAWN, do not print. An earlier c_glauber draft claimed a sign misprint in an equation of Collins 2011; it could not be verified and was withdrawn.

**Printable version:** Print no erratum of Collins, Foundations of Perturbative QCD (2011), on our own authority; the withdrawn c_glauber claim is not printed. Corrections of the book are cited only as the author's own errata ('Errata and updates for Foundations of Perturbative QCD', J. Collins, 22 May 2026, Sec. 3): Fig. 7.10 and eqs. (11.4)-(11.6) (E27). If the N19 material is used, also eq. (14.30), p. 559, whose correct form is −i∏_f 1/(P_A^−−k_A^−−Σ_{j>f}l_j^−−D_f−i0) + i∏_f 1/(P_A^−−k_A^−−Σ_{j>f}l_j^−−D_f+i0).

**Literature check:** Yes, for every Collins-2011 correction our material uses: the author's errata list (version 22 May 2026, Sec. 3 'Corrections and updates relative to published paperback edition of November 2013') contains Fig. 7.10, eqs. (11.4)-(11.6) and eq. (14.30). The withdrawn draft named no recorded equation.

## E20 — erratum — **confirmed**

**Claim:** Ji PRL 1997 (arXiv v1) eq. (15): the second denominator 'x + ξ_Ji/2 + iε' must have −iε (Feynman propagator; ξ_Ji = 2ξ). LO: T^{μν} = g⊥^{μν}Σe_q²∫F^q[1/(x−ξ+i0) + 1/(x+ξ−i0)] − iε⊥^{μν}Σe_q²∫F̃^q[1/(x−ξ+i0) − 1/(x+ξ−i0)]. The published version was not checked; VGG eq. (38) has −iε.

**Printable version:** In arXiv:hep-ph/9603249v1 (preprint of X. Ji, PRL 78 (1997) 610), eq. (15), the second denominator in both brackets (vector and axial) is printed 1/(x+ξ_Ji/2+iε). It must be 1/(x+ξ_Ji/2−iε): u-channel Feynman propagator, required by analyticity and by Im T^11 = 2πF_1 ∝ q+q̄ in the forward limit. Here ξ_Ji = 2ξ.
Corrected LO result:
T^{μν} = g_⊥^{μν} Σ_q e_q^2 ∫dx F^q [1/(x−ξ+i0) + 1/(x+ξ−i0)] − iε_⊥^{μν} Σ_q e_q^2 ∫dx F̃^q [1/(x−ξ+i0) − 1/(x+ξ−i0)].
Conventions (must be printed with it): T^{μν} = i∫d^4z e^{iq'·z}<P'|T J^μ(z)J^ν(0)|P>; γ5 = iγ^0γ^1γ^2γ^3; ε^{0123} = +1; ε_⊥^{μν} = ε^{μνρσ} n̄_ρ n_σ with n̄ along the hadron and n̄·n = 1; F^q = (2P̄^+)^{-1}[H ū'γ^+u + E ū'iσ^{+α}Δ_α u/(2M)]; F̃^q = (2P̄^+)^{-1}[H̃ ū'γ^+γ5 u + Ẽ Δ^+ ū'γ5 u/(2M)].
Ji's PRD 55 (1997) 7114, eq. (4), and VGG, PRD 60 (1999) 094017, eq. (38), have −iε. The published PRL text was not accessible; attribute the misprint to the arXiv v1, not to the journal page.

**Literature check:** The correct −iε is in Ji's own PRD 55 (1997) 7114 (hep-ph/9609381 v1 and v3, eq. (4) of v3), in VGG 1999 eq. (38), and in standard reviews. No erratum record on INSPIRE. No remark on the PRL/preprint iε was found: INSPIRE full-text 'refersto ∧ prescription ∧ (misprint ∨ typo)' gave 17 hits; the DVCS-era ones concern other misprints, and Diehl's review has no such remark.

## E21 — erratum — **confirmed**

**Claim:** Mankiewicz–Piller 2000 say in the text that the WW twist-3 integrands behave as '12/τ and 9/τ'. Their eq. (10), with eqs. (3)-(5) and φ_∥ = 6ττ̄, gives 12/τ and 6/τ (in general 8g^v(0)/τ and 4g^v(0)/τ). Internally inconsistent; do not quote 9/τ.

**Printable version:** In Mankiewicz–Piller, PRD 61 (2000) 074013 [arXiv:hep-ph/9905287], the text after eq. (10) states that for φ_∥ = 6ττ̄ the integrands of eq. (10) behave as 12/τ and 9/τ. Eq. (10) together with eqs. (3)-(5), as printed, gives 12/τ and 6/τ; for a general DA, 8g^v(0)/τ and 4g^v(0)/τ, with g^v(0) = ½∫_0^1 du φ_∥(u)/u. The paper is internally inconsistent, and '9/τ' must not be quoted. Likewise, MP's inference 'I_1/I_2 close to one', which rests on 12:9, should not be quoted: eq. (10) gives 2:1 for every DA. Both integrals diverge logarithmically in any case.

**Literature check:** Not found. INSPIRE has no erratum record. Full-text search 'refersto MP ∧ (9/τ ∨ 12/τ ∨ misprint ∨ typo)' gave 2 unrelated hits. Diehl's review (Phys. Rept. 388 (2003) 41) says MP and Anikin–Teryaev agree but quotes no coefficients.

## E22 — erratum — **refuted**

**Claim:** Attributed: Collins–Diehl 2000 state that an NLO calculation claiming a non-zero leading-twist γ*_T → V_T amplitude omitted necessary collinear subtractions. The amplitude vanishes to all orders by chirality/helicity.

**Printable version:** 

**Literature check:** Yes. Hoodbhoy, PRD 65 (2002) 077501 [hep-ph/0108214], explicitly acknowledges the omission pointed out by Collins-Diehl and confirms the vanishing at one loop. Diehl, Phys. Rept. 388 (2003) 41 [hep-ph/0307382] summarizes: zero at LO (MPW 1998), NLO (Hoodbhoy 2002) and to all orders (DGP 1999; CD 2000).

## E23 — erratum — **confirmed**

**Claim:** Becher–Schwartz 2008 App. A prints Γ_1 = 4C_F[C_A(67/9 − π²/3) − (20/9)C_FT_Fn_f]; the inner C_F is spurious. Correct: Γ_1 = 4C_F[(67/9 − π²/3)C_A − (20/9)T_Fn_f], with Γ_cusp = Σ(α_s/4π)^{n+1}Γ_n.

**Printable version:** Becher–Schwartz, JHEP 07 (2008) 034, eq. (A.10) (p. 29; also arXiv:0803.0342 v1, v2, App. A), print Γ_1 = 4C_F[C_A(67/9 − π²/3) − (20/9)C_F T_F n_f]; the C_F multiplying T_F n_f inside the bracket is spurious. The correct value, with Γ_cusp = Σ_n (α_s/4π)^{n+1} Γ_n, is Γ_1 = 4C_F[(67/9 − π²/3)C_A − (20/9)T_F n_f], equal to 36.8436 for n_f = 5 (Korchemsky–Radyushkin, NPB 283 (1987) 342; e.g. Moch–Vermaseren–Vogt, NPB 688 (2004) 101, eq. (3.11)).

**Literature check:** The correct value is standard: KR 1987 (attributed; not read directly), MVV 2004 eq. (3.11), Becher–Neubert 2009, and BNP 2006 (BS's own ref.). The misprint itself was not found reported: no INSPIRE erratum; of 68 broad full-text hits (refersto BS ∧ cusp ∧ misprint/typo/erratum), 7 were scanned here and 7 others by stage 1, and none mentions it.

## E24 — erratum — **confirmed**

**Claim:** The Becher–Schwartz jet function J(p²) = (1/n̄·p)(1/π)Im[i∫e^{−ipx}⟨0|T{χ̄_n(x)(n̸̄/2)χ_n(0)}|0⟩] = δ(p²) + …, read literally (fermionic T sign, Dirac and colour traces), gives −2N_cδ(p²). A factor −(1/2N_c)tr is implicit; use the explicitly normalized cut definition.

**Printable version:** Becher–Schwartz, JHEP 07 (2008) 034, eq. (2.6) [arXiv:0803.0342], define J(p²) = (n̄·p)^{-1}π^{-1} Im[i∫d^4x e^{−ipx} <0|T{χ̄_n(x)(n̸̄/2)χ_n(0)}|0>] = δ(p²) + O(α_s). Read literally (a scalar operator summed over Dirac and colour indices, with fermionic T-ordering), the free field gives −2N_c δ(p²), so a factor −1/(2N_c) is implicit. The monograph uses the explicitly normalized cut definition Σ_X (2π)^D δ^D(p−p_X) <0|χ_n|X><X|χ̄_n|0> = 2π (n̸/2) n̄·p J(p²) 𝟙_c, which gives J^(0) = δ(p²). Equivalently one may use Becher–Neubert, PLB 637 (2006) 251, eqs. (3) and (6).

**Literature check:** The properly normalized operator definition is in Becher–Neubert 2006 (hep-ph/0603140, eqs. (3), (6)), cited by BS as ref. [23]. The implicit normalization of BS eq. (2.6) was not found reported: no INSPIRE erratum, and none of the 7 full-text hits is relevant.

## E25 — erratum — **confirmed**

**Claim:** BPS 2002: 'the first two terms of (Lcg) are invariant under collinear gauge transformations' is false for the ghost term. Correct: the field-strength term is collinear and usoft invariant; the gauge-fixing and ghost terms are usoft covariant and BRST invariant.

**Printable version:** Bauer–Pirjol–Stewart, PRD 65 (2002) 054022 [arXiv:hep-ph/0109045], state after eq. (24) that its first two terms, the field-strength and ghost terms, are invariant under collinear gauge transformations. For the ghost term 2tr{c̄[i𝒟_μ,[i𝒟^μ+gA^μ_{n,q},c]]} this is false: the outer commutator [i𝒟_μ, ·] is not collinear covariant, and the variation is non-zero both for adjoint and for inert ghosts. Correct statement: the field-strength term is invariant under collinear and usoft gauge transformations. The gauge-fixing term and the ghost term are each invariant under usoft gauge transformations (c, c̄ → V_us c V_us†; the usoft field acts as a background), but neither is collinear-gauge invariant. Their sum, not each term separately, is BRST invariant, and so is the full L_c^(g). Usoft invariance and BRST invariance are what the decoupling proof needs.

**Literature check:** No published correction found: INSPIRE has no erratum record for PRD 65 054022. Full-text search 'refersto BPS ∧ ghost ∧ collinear gauge ∧ (not invariant ∨ misprint ∨ incorrect)' gave 11 hits; 4 were scanned and none concerns this sentence. The underlying facts are standard background-field/BRST properties; BPS themselves note that eq. (24) equals the background-field action with A_us as the background.

## E26 — erratum — **confirmed**

**Claim:** BBNS 2001 / BN 2003: 'X_H = ln(m_M/Λ_h) ≈ 2.4' must read m_B (ln(5.28/0.5) = 2.36). In BN 2003's notation V refers to the emitted M_2; do not mix it with BBNS's πK labels.

**Printable version:** BBNS, NPB 606 (2001) 245, text after eq. (71): 'default value X_H=ln(m_M/Lambda_h)≈2.4' must read X_H=ln(m_B/Lambda_h)≈2.4. BN, NPB 675 (2003) 333, text after eq. (63): 'default value X_A=ln(m_M/Lambda_h)≈2.4' must read X_A=ln(m_B/Lambda_h)≈2.4; X_H is treated 'similarly'. Here ln(5.28 GeV/0.5 GeV)=2.36, consistent with their parametrization X=(1+rho e^{i phi}) ln(m_B/Lambda_h), Lambda_h=0.5 GeV, and with BBNS's other statements. Remark: in BN's general notation, eq. (35), V_i(M_2) refers to the emitted meson M_2; M_1 receives the spectator. BBNS eq. (46) is the pi K special case of the same convention (a_1, a_4 with V_K; a_2, a_3, a_9 with V_pi). Verified against the arXiv texts; journal typesetting not seen.

**Literature check:** No published erratum: INSPIRE lists none for either paper. The correct value ln(m_B/Lambda_h)≈2.4 is printed elsewhere in BBNS 2001 itself.

## E27 — erratum — **confirmed**

**Claim:** Collins 2011: use Fig. 7.10 (Wilson-line vertices −ig_0n^μt left of the cut, +ig_0n^μt right) and eqs. (11.4)-(11.6), p. 402 (upper and lower indices interchanged), as corrected in the author's errata. Collinear K_μν = k_μw_2ν/(k·w_2 − i0) (DIS, future-pointing). Collins uses D = ∂ + igA (eq. (2.2)), so g_Collins = −g.

**Printable version:** Collins, Foundations of Perturbative QCD (CUP 2011; same pages in the 2013 printing and the 2023 OA reissue) must be used with the author's errata (version of 22 May 2026, Sec. 3).
(i) Fig. 7.10, p. 236: the gluon-pdf Wilson-line vertex right of the cut is -g0 n^mu f_{k alpha j}, not +g0 n^mu f_{k alpha j} (also -g0 Z3^{1/2} n^mu f_{k alpha j} for renormalized fields). The left vertex is +g0 n^mu f_{k alpha j}, with (T_alpha)_kj=i f_{k alpha j}. The quark-pdf vertices, -i g0 n^mu (t_alpha)_kj left and +i g0 n^mu (t_alpha)_kj right, were printed correctly.
(ii) Eqs. (11.4)-(11.6), p. 402, with upper and lower indices interchanged: H.C=H^{mu1..muN} prod g_{mu_j nu_j} C^{nu1..nuN}, g=K+G, K_{mu nu}=k_mu w2_nu/(k.w2 - i0), w2=(0,1,0_T), k flowing into H. This is the future-pointing (DIS) prescription.
(iii) Collins uses D=d+i g0 t A (eq. (2.2); vertex -ig t gamma, Fig. 3.1), so g_Collins=-g in our convention and his Wilson lines are P exp(-i g0 ∫ n.A) (eq. (13.40)).

**Literature check:** Yes: J. Collins, 'Errata and updates for Foundations of Perturbative QCD' (22 May 2026), Sec. 3, https://www.cantab.net/users/johncollins/qcdbook/qcd-errata.pdf. The g-sign convention is stated in the book itself (eq. (2.2), Fig. 3.1, caption of Fig. 7.10).

## E28 — erratum — **confirmed**

**Claim:** Sterman–Weinberg: σ_2j = σ_0{1 − (C_Fα_s/π)[4ln δ ln 2ε + 3ln δ + π²/3 − 5/2]}, with ε the fraction of the total energy. The common form '4ln δ ln ε' holds only for ε a fraction of the beam energy; otherwise it is off by 4ln2|ln δ|C_Fα_s/π. At (ε,δ) = (1e−6, 0.003): numerical −288.2811, ln 2ε form −288.2812, ln ε form −304.39.

**Printable version:** In Sterman-Weinberg's definition (all but a fraction eps of the total c.m. energy sqrt(s) inside some pair of opposite cones of half-angle delta, free axis), the O(alpha_s) result for eps ≲ delta << 1 is
sigma_2j = sigma_0 {1 - (C_F alpha_s/pi)[4 ln delta ln(2eps) + 3 ln delta + pi^2/3 - 5/2]} + O(eps, delta^2 logs),
with sigma_0 the Born cross section. The form with 4 ln delta ln eps is correct only if eps is defined as a fraction of the beam energy sqrt(s)/2 (as in Becher-Neubert-Rothen-Shao 2016, eq. (1), with beta, c0=10-4pi^2/3). Mixing the conventions shifts sigma_2j/sigma_0 by 4 ln2 |ln delta| C_F alpha_s/pi. Numerically, at (eps, delta)=(1e-6, 0.003): exact c2j=-288.2811, ln 2eps form -288.2812, ln eps form -304.39. Print this as a convention remark, not as an erratum of SW 1977.

**Literature check:** Yes. ln 2eps with total-energy eps: Nandi-Wada PRD 21 (1980) 76, eq. (23); Chay-Ellis PRD 55 (1997) 2728, eq. (11); Ali-Kramer EPJH 36 (2011) 245; Sapeta PPNP 89 (2016) 1 (f3 with -7/4); Cheung-Luke-Zuberi PRD 81 (2010) 094017 (ln 2beta). Beam-energy form with ln beta and c0=10-4pi^2/3: Becher-Neubert-Rothen-Shao PRL 116 (2016) 192001, eq. (1). The numerical comparison is our own.

## E29 — erratum — **confirmed**

**Claim:** The GKL 1988 O(α_s³) R-ratio was later corrected. Corrected a³ coefficient (MS-bar, μ² = s, a = α_s/π): −6.63694 − 1.20013n_f − 0.00518n_f² − 1.2395η, with η = (Σe_q)²/(3Σe_q²) and singlet coefficient 55/72 − (5/3)ζ_3. Status in source: recalled, verify.

**Printable version:** The O(alpha_s^3) coefficient of R(s) of Gorishny-Kataev-Larin, PLB 212 (1988) 238, was incorrect. It was corrected by Surguladze-Samuel, PRL 66 (1991) 560 [Erratum ibid. 2416], and by Gorishny-Kataev-Larin, PLB 259 (1991) 144. The corrected result (SU(3), MS-bar, mu^2=s, a=alpha_s(s)/pi), with R=3 Sum e_q^2 [1+a+r2 a^2+r3 a^3]:
r3 = -6.63694 - 1.20013 nf - 0.00518 nf^2 - 1.2395 eta, eta=(Sum e_q)^2/(3 Sum e_q^2).
The singlet (light-by-light) term is (Sum e_q)^2 (55/72 - (5/3)zeta3) a^3 = -1.2395 (Sum e_q)^2 a^3. For nf=5 the coefficient is -12.805.

**Literature check:** Yes: GKL PLB 259 (1991) 144; Surguladze-Samuel PRL 66 (1991) 560 [Erratum 2416]; Surguladze-Samuel RMP 68 (1996) 259, eqs. (Ranalytic1) and (Rnumerical); Chetyrkin-Kuehn-Kwiatkowski Phys. Rept. 277 (1996) 189; Baikov-Chetyrkin-Kuehn PRL 101 (2008) 012002; PDG 2025 QCD review, eq. (9.9b).

## E30 — erratum — **confirmed**

**Claim:** Collins 1993's argument that T invariance forbids the Sivers function is invalidated by the Wilson line (Collins 2002, after BHS 2002): f_1T^⊥,SIDIS = −f_1T^⊥,DY, and likewise h_1^⊥.

**Printable version:** Collins (NPB 396 (1993) 161, appendix) argued from PT invariance that the Sivers function vanishes. The argument ignored the Wilson line in the gauge-invariant operator, as the paper itself notes, and is therefore invalid. Correctly, PT maps future-pointing staples to past-pointing ones, giving
P(x,k_T,S_T)|future = P(x,k_T,-S_T)|past and f1T^perp(x,k_T)|SIDIS = -f1T^perp(x,k_T)|DY
(Collins, PLB 536 (2002) 43, eqs. (2)-(3), following Brodsky-Hwang-Schmidt, PLB 530 (2002) 99). Likewise the Boer-Mulders function: h1^perp|SIDIS = -h1^perp|DY (explicitly Boer-Mulders-Pijlman NPB 667 (2003) 201; Boer-Brodsky-Hwang PRD 67 (2003) 054003; Collins 2011 §13.17.2). All T-even TMDs are the same in both processes. This holds given TMD factorization with future-pointing (SIDIS) and past-pointing (DY) staples.

**Literature check:** Yes: Collins PLB 536 (2002) 43, eqs. (2)-(3); Brodsky-Hwang-Schmidt PLB 530 (2002) 99; Boer-Mulders-Pijlman NPB 667 (2003) 201; Boer-Brodsky-Hwang PRD 67 (2003) 054003; Collins, Foundations of Perturbative QCD (2011), §13.17, eq. (13.124), pp. 534-536.

## E31 — erratum — **confirmed**

**Claim:** Collins 2011 §14.4 p. 553 follows CSS 1988 'with some important improvements and with correction of errors'; CSS 1988 supersedes Bodwin 1985 and CSS 1985.

**Printable version:** Collins (Foundations of Perturbative QCD, 2011, §14.4, p. 553) states that his treatment of the Glauber region follows Collins-Soper-Sterman, NPB 308 (1988) 833, 'but with some important improvements and with correction of errors', and that CSS 1988 'supersedes earlier work (Bodwin, 1985 [PRD 31, 2616]; Collins, Soper, and Sterman, 1985a [NPB 261, 104])'. Print this attributed to Collins. Collins does not specify the errors, so the monograph must not list or characterize them or imply they were checked. Improvements that may be named: the commutator argument (p. 558), the extension to TMDs (p. 560), and the soft-factor cancellation via T invariance (pp. 560-561).

**Literature check:** The statement is Collins 2011, p. 553 (verbatim). No published identification of the specific errors of CSS 1988 was found.

## E32 — erratum — **refuted**

**Claim:** A 'commonly quoted variant' of C^{q,(1)}_{2,n} (α_s/4π units), with 2/(n+1) + 1/n² instead of 4/(n+1) + 2/n², fails the Adler n = 1 check. Correct: C_F[2S_1² − 2S_2 + 3S_1 − 2S_1/(n(n+1)) + 3/n + 4/(n+1) + 2/n² − 9], which vanishes at n = 1. The source of the variant is unspecified.

**Printable version:** 

**Literature check:** The correct formula and its n=1 (Adler) check are in Bardeen–Buras–Duke–Muta, PRD 18 (1978) 3998, eqs. (3.9), (4.7), (4.10). Also Buras, RMP 52 (1980) 199, eq. (2.96); Vermaseren–Vogt–Moch, NPB 724 (2005) 3, eq. (A.3); Blümlein–Marquard–Schneider–Schönwald, arXiv:2208.14325. The variant was not found in print.

## E33 — erratum — **confirmed**

**Claim:** Errata exist but their content was not examined for: Bodwin 1985; Collins–Soper 1981; Collins 1998; BBL 1995; Becher–Neubert 2009; Henneaux 1993; Ebert–Gao–Stewart 2022; Rodini–Vladimirov 2022; KPS 2016; Cougoulic et al. 2022; Dixon et al. 2020; Forshaw–Holguin 2021; Becher et al. 2016; Bertone et al. 2020; Diehl–Ostermeier–Schäfer 2012; Kramer–Lampe 1987; Penin 2015; Floratos et al. Use the corrected equations.

**Printable version:** Cite each paper with its erratum and use only corrected formulas and conclusions.

The 18 papers and their errata:
- Bodwin PRD 31 (1985) 2616 [PRD 34 (1986) 3932]
- Collins-Soper NPB 193 (1981) 381 [NPB 213 (1983) 545]
- Collins PRD 57 (1998) 3051 [PRD 61 (2000) 019902]
- Bodwin-Braaten-Lepage PRD 51 (1995) 1125 [PRD 55 (1997) 5853]
- Becher-Neubert PRL 102 (2009) 162001 [PRL 111 (2013) 199905]
- Henneaux PLB 313 (1993) 35 [PLB 316 (1993) 633]
- Ebert-Gao-Stewart JHEP 06 (2022) 007 [JHEP 07 (2023) 096]
- Rodini-Vladimirov JHEP 08 (2022) 031 [JHEP 12 (2022) 048]
- Kovchegov-Pitonyak-Sievert JHEP 01 (2016) 072 [JHEP 10 (2016) 148]
- Cougoulic-Kovchegov-Tarasov-Tawabutr JHEP 07 (2022) 095 [JHEP 09 (2024) 052]
- Dixon-Herrmann-Yan-Zhu JHEP 05 (2020) 135 [JHEP 06 (2024) 143]
- Forshaw-Holguin JHEP 12 (2021) 084 [JHEP 04 (2024) 097]
- Becher-Neubert-Rothen-Shao JHEP 11 (2016) 019 [JHEP 05 (2017) 154]
- Bertone-Cacciari-Frixione-Stagnitto JHEP 03 (2020) 135 [JHEP 08 (2022) 108]
- Diehl-Ostermeier-Schafer JHEP 03 (2012) 089 [JHEP 03 (2016) 001]
- Kramer-Lampe ZPC 34 (1987) 497 [ZPC 42 (1989) 504]
- Penin PLB 745 (2015) 69 [PLB 751 (2015) 596; PLB 771 (2017) 633]
- Floratos-Ross-Sachrajda NPB 129 (1977) 66 [NPB 139 (1978) 545]
Also add these errata, present in our material: Erdogan PRD 89 (2014) 085016 [PRD 90 (2014) 089902]; Surguladze-Samuel PRL 66 (1991) 560 [ibid. 2416]; Buffing-Diehl-Kasemets JHEP 01 (2018) 044 [JHEP 07 (2021) 046].

Corrected content that matters for us:
(a) DHYZ. The two-loop soft-collinear tripole term still breaks strict collinear factorization at amplitude level (corrected (4.27): 15 zeta4, -i pi^3/6 log v). At cross-section level these terms cancel for pure QCD (corrected (4.30): first line zero, second line cancels after summing over colours). Never cite DHYZ as evidence of cross-section-level violation.
(b) Penin 2015. After the 2017 corrigendum the power-suppressed form factor f(x) = -3F1^(1) peaks at 0.8816 (x = 2.609) and then decays exponentially. Do not quote the original enhancement.
(c) Becher-Neubert 2009. The dipole formula is eq. (7). The erratum adds -(i f^{abc}/32eps) Sum_(i,j,k) T_i^a T_j^b T_k^c (gamma0^i/C_i - gamma0^j/C_j) ln(-s_ij/-s_jk) ln(-s_ki/-s_ij) to eq. (12).
(d) BNRS. Use the corrected signs of V_m and R_m in (5.11) and the factor 1/n! in (5.17). §2 is unchanged.
(e) Forshaw-Holguin. No coherence-violating logarithms in the vector-sum pT of W/Z/H. The scalar-sum pT may have alpha_s^5 L^2 (ln w)^4.
(f) BBL. Spin-flip Fock states have probability ~v^3. Error estimates are O(v^3 Gamma) in (3.1), (4.1), (4.3) and O(v^3 sigma) in (6.8), (6.9). Typo fixes: (3.19a,b), (5.4), (5.5) coefficient 4/(N_c^2-1), (A16) and (A25) alpha_s(2M).
(g) Collins 1998. Figs. 1 and 5 corrected: extra target-collinear final-state lines.
(h) Bertone (C.18)-(C.20) x2!,2!,3!. Ebert-Gao-Stewart: factors of 2 and complex C^(1). Rodini-Vladimirov 2022: signs and factors (-i). DOS: listed fixes. KPS: corrected large-Nc kernels. CKTT: intermediate signs only.
(i) Bodwin 1986, Collins-Soper 1983, Henneaux 1993, Kramer-Lampe 1989, FRS 1978: contents not examined. Quote no formula from them unchecked.

**Literature check:** These are the published errata. INSPIRE records were verified. Published texts read: JHEP 06(2024)143, 04(2024)097, 05(2017)154, 08(2022)108, 07(2023)096, 12(2022)048, 10(2016)148, 09(2024)052, 03(2016)001; PLB 751 (2015) 596 and PLB 771 (2017) 633. Also read: BBL erratum.tex (hep-ph/9407339v2), arXiv 0901.0722 v1-v3 and hep-ph/9709499 v1-v2.

## E34 — erratum — **disputed:refuted**

**Claim:** Reported disagreements. (i) LMNW 2021 predict the three-loop h→γγ logs O(α_bα_s²L^k), k = 6..3, disagreeing with earlier conventional predictions. (ii) Rodini–Vladimirov 2024 report 'several differences with earlier derivations'. (iii) Balitsky–Chirilli 2008: NLO BK agrees with NLO BFKL up to an α_s²ζ(3) term. (iv) Borden–Kovchegov intercept 3.66074√(α_sN_c/2π) vs BER's 3.66394, with Δγ_GG differing from four loops (open).

**Printable version:** (i) Liu–Mecaj–Neubert–Wang (JHEP 01 (2021) 077) predict the logarithms O(alpha_b alpha_s^2 L^k), k=6,5,4,3, L=ln(-M_h^2/m_b^2), of the three-loop b-loop h->gamma gamma amplitude. These agree with the numerical computation of Czakon–Niggetiedt and with the analytic n_f terms. For the subleading logarithms (k=5 at three loops; the NLL series alpha alpha_s^n L^(2n+1)) they disagree with the predictions of Akhoury–Wang–Yakovlev (2001) and Anastasiou–Penin (2020). (ii) Rodini–Vladimirov (PRD 110 (2024) 034009) report 'several differences with earlier derivations', attributed to the kinematics of quark-gluon interference terms. (iii) Balitsky–Chirilli (PRD 77 (2008) 014019): the forward limit of the NLO BK kernel agrees with NLO BFKL up to a term proportional to alpha_s^2 zeta(3) times the dipole, which they attribute to different longitudinal cutoffs. Later work by the same authors reports that the 'composite conformal dipole' kernel agrees with NLO BFKL (PRD 88 (2013) 111501, N=4 SYM context). (iv) Borden–Kovchegov (PRD 108 (2023) 014001) find alpha_h=(4/3^(1/3)) sqrt(Re[(-9+i sqrt111)^(1/3)]) sqrt(alpha_s N_c/2pi) ≈ 3.66074 sqrt(alpha_s N_c/2pi). Their resummed Delta gamma_GG = 4abar/omega+8abar^2/omega^3+56abar^3/omega^5+496abar^4/omega^7+... agrees with fixed order through three loops. The pure-glue BER result (Bartels–Ermolaev–Ryskin, Z. Phys. C72 (1996) 627) gives 504 abar^4/omega^7 at four loops and an intercept sqrt((17+sqrt97)/2) sqrt(alpha_s N_c/2pi) ≈ 3.66394 sqrt(alpha_s N_c/2pi). BER themselves quote 3.66; the analytic value is from Kovchegov–Pitonyak–Sievert 2017. Open problem, no verdict.

**Literature check:** All four items are the papers' own statements. The (iii) mismatch was withdrawn by its authors in Balitsky & Chirilli, Nucl. Phys. B 822 (2009) 45 [arXiv:0903.5326], Sec. 6 'In QCD'. BER references: Z. Phys. C70 (1996) 273 [hep-ph/9507271] and Z. Phys. C72 (1996) 627 [hep-ph/9603204]. The 2026 status is from Borden-Kovchegov PRD 113 (2026) 034002.

## E35 — erratum — **confirmed**

**Claim:** CRS 2022: the CFH 2020 argument for NLO MS-bar positivity fails at 'bare PDFs are positive'. Yukawa counterexample: f = a_λ(1−ξ)[ln(μ²/Δ) − 1 + (m_q+ξm_p)²/Δ], Δ = ξm_s² + (1−ξ)m_q² − ξ(1−ξ)m_p², negative at low μ (ξ ∈ [0.28, 0.98] at μ = 0.8 GeV for masses 0.3/1.0/1.5 GeV; μ_* = 1.70 GeV). 'Positive for all μ' is [V]; positivity above a scale is [P] (CFGH: Q² ≳ 5 GeV²).

**Printable version:** Collins-Rogers-Sato (PRD 105 (2022) 076010, Sec. VI) show that the Candido-Forte-Hekhorn argument (JHEP 11 (2020) 129) for positivity of NLO MS-bar PDFs fails at the step 'bare PDFs are positive' (CFH §2 after eq. (2.2), used in §3.1). The UV-divergent contributions are positive for n < 4 but turn negative after continuation to n > 4 (eps < 0), the regime CFH need for the collinear subtraction.

Counterexample (CRS eqs. (55)-(57)): Yukawa model with a_lambda = lambda^2/16pi^2,
  f_{q/p}(xi;mu) = a_lambda (1-xi)[ln(mu^2/Delta) - 1 + (m_q + xi m_p)^2/Delta],
  Delta = xi m_s^2 + (1-xi) m_q^2 - xi(1-xi) m_p^2.
For m_q, m_p, m_s = 0.3, 1.0, 1.5 GeV, f < 0 exactly for xi in (0.264, 1) at mu = 0.8 GeV. In general f < 0 for mu below a threshold mu0(xi) that increases from m_q (xi -> 0) to mu* = m_s exp{[1-(m_q+m_p)^2/m_s^2]/2} = 1.699 GeV (xi -> 1). So f > 0 for all xi iff mu >= mu*.

Grades: 'MS-bar PDFs are positive for all mu' is [V]. Positivity above some scale is [P]: CFGH (EPJC 84 (2024) 335) agree that PDFs turn negative at low enough, non-perturbative scales, and estimate positivity 'very conservatively' for Q^2 >~ 5 GeV^2.

**Literature check:** Collins, Rogers & Sato, Phys. Rev. D 105 (2022) 076010 [arXiv:2111.01170], abstract, Sec. VI, eqs. (55)-(59), Sec. VIII A-B. Candido, Forte & Hekhorn, JHEP 11 (2020) 129, §2 (after eq. (2.2)) and §3.1.1-3.1.2. Candido, Forte, Giani & Hekhorn, Eur. Phys. J. C 84 (2024) 335 [arXiv:2308.00025]. The corrected interval (0.264, 1) is our own evaluation of CRS eq. (55).

## E36 — erratum — **confirmed**

**Claim:** Two claims of factorization violation by spectator–spectator Glauber exchange are contradicted, for pure Glauber ladders and IR-safe single-scale observables, by the all-order cancellation of SYZ 2018 ('disproves previous claims'): Gaunt 2014 (two S–S Glauber gluons spoil CSS for E_T) and RS 2016 §11.1 (spoiled from O(α_s⁴)). Disputed; the claims survive for multi-differential observables. Zeng 2015's counterexample lies outside SYZ's scope.

**Printable version:** Gaunt (JHEP 07 (2014) 110) found that the CSS cancellation argument for Glauber gluons breaks down at the level of two spectator-spectator Glauber gluons for hadronic E_T. He suggested leading-power factorization failure for E_T and other MPI-sensitive observables (beam thrust, transverse thrust).

Rothstein-Stewart (JHEP 08 (2016) 025, §11.1) state that, when the measurement constrains Delta p_perp ~ Q*, S-S Glauber exchange spoils the factorization of the collinear initial-state radiation starting at O(alpha_s^4), for beam thrust, transverse thrust, E_T and any observable constraining Delta p_perp.

Schwartz-Yan-Zhu (PRD 97 (2018) 096017) give an all-order argument [A], using CSS q_T factorization and scale invariance of the 2->2 amplitude. It shows that for pure Glauber ladder graphs all amplitude-level factorization-violating effects cancel at cross-section level for any IR-safe single-scale observable, which 'disproves' the pure-Glauber claims. A leading violation then requires soft emission off the Glauber rungs (Lipatov vertex). This later result is unrebutted and adopted in later work.

SYZ's argument 'does not apply to doubly-differential observables'. There Rothstein-Stewart's general Delta p_perp mechanism is not contradicted, and Zeng's model (JHEP 10 (2015) 189: non-zero leading-power longitudinal-spin asymmetry from S-S Glauber exchange in DY with beam thrust) is outside SYZ's scope ([V] in the model). Standard factorization for MPI-sensitive observables remains [C].

**Literature check:** These are the papers' own claims. Gaunt:2014ska abstract and conclusions. Rothstein:2016bsq §11.1, eq. (11.13) and the paragraph after it. Schwartz:2018obd abstract, introduction, §3.2 and scope sentence. Zeng:2015iba abstract. Later adoption of SYZ: Chien-Rahn-Shao arXiv:2205.05104; Bijl-Niedenzu-Waalewijn arXiv:2307.02521.

## N01 — new_result — **confirmed**

**Claim:** prop:dy-eikonal-twogluon, marked 「本书新结果（待文献核查）」. Two infinite time-like Wilson lines (rapidity difference Y) exchange two gluons of mass m with exact propagators; a = k_T² + m², b = (K−k)_T² + m². J_box = (2π/(ab))(π + iY), J_cross = −2πiY/(ab). With X = T_A·T_B, c_box = X² and c_cross = X² + (C_A/2)X, the sum is (2π/(ab))[πX² − iY(C_A/2)X]. Hence p_opp = −iY/π, Re p_opp = 0, V†V = 1 + O(χ³), and real cuts start at O(g⁶). Other O(g⁴) graphs and non-eikonal spectators are not covered.

**Printable version:** Print without the marker 「本书新结果（待文献核查）」, citing Meggiolaro 1997 and Giordano-Meggiolaro 2006.

Setup: two infinite time-like Wilson lines (rapidity difference Y, generators T_A and T_B, X = T_A.T_B) exchange two gluons of mass m with exact Feynman-gauge propagators, at fixed transverse momenta. Let a = k_T^2 + m^2 and b = (K-k)_T^2 + m^2. The longitudinal integrals are J_box = (2pi/(ab))(pi + iY) (ladder, same ordering on both lines) and J_cross = -2pi iY/(ab). The colour factors are c_box = X^2 and c_cross = X^2 + (C_A/2)X, so J_box c_box + J_cross c_cross = (2pi/(ab))[pi X^2 - iY(C_A/2)X].

The X^2 term is the abelian exponentiation term (1/2)(i chi)^2 X^2. The C_A term is i x real x Hermitian: the one-loop reggeization phase, whose Y -> inf limit is the classic one-loop gluon trajectory. Hence p_opp = -iY/pi, Re p_opp = 0, and V^dag V = 1 + O(chi^3); the strict-instantaneous-window residual is an artefact of that truncation.

Real cuts start at O(g^6): single (and O(g^2) double) emission from straight infinite time-like lines vanishes.

Including the other O(g^4) eikonal graphs (Meggiolaro 1997 eqs. (3.28)-(3.34): a real multiple of the tree, F^(2)(t) real for t < 0), unitarity holds at O(g^4) for the complete eikonal amplitude. Non-eikonal spectators and active partons are not covered.

Cite M97 (3.23)-(3.26), (3.34), (3.36) and GM06 (4.24); avoid M97 (3.35) and GM06 (4.15)-(4.21), (4.27), whose signs are misprinted.

**Literature check:** Yes. E. Meggiolaro, Z. Phys. C 76 (1997) 523 [hep-th/9602104], §3, eqs. (3.23)-(3.26), with the other O(g^4) graphs in (3.28)-(3.34) and the Regge limit in (3.36). Graph by graph: M. Giordano & E. Meggiolaro, Phys. Rev. D 74 (2006) 016003 [hep-ph/0602143], eq. (4.24). The high-energy limit is classic (Cheng-Wu; Lipatov, as cited by M97). Related structure: Korchemskaya & Korchemsky, NPB 437 (1995) 127. Rothstein-Stewart §9 (crossed Glauber boxes vanish with their eta regulator) is consistent.

## N02 — new_result — **confirmed**

**Claim:** OTHERS Prop 1.2 [R]: Collins' geometric Thm 3 (arXiv:2007.04085) is Gordan's alternative (1873). Either ∃w with D_j(w) > 0 ∀j, or Σλ_jD_j = 0 with λ_j ≥ 0 not all zero. Constructive proof: w = min-norm point of conv{D_j} gives D_j(w) ≥ |w|². Checked on 400 instances (226 of type I, 174 of type II). Prior notice in the literature unchecked.

**Printable version:** Remark (Collins' Thm 3 = Gordan's alternative), graded [R]. Let D_1,...,D_N be dual vectors on a finite-dimensional real vector space V. Exactly one of the following holds:
(I) there is a v in V with D_j(v) > 0 for all j (a good contour-deformation direction);
(II) there are lambda_j >= 0, not all zero, with Sum_j lambda_j D_j = 0 (a Landau point).
This is Gordan's theorem of the alternative (P. Gordan, Math. Ann. 6 (1873) 23-28), and it is exactly Collins' geometric Theorem 3 in arXiv:2007.04085 (proved there in Secs. V-VII).

Constructive proof: choose an inner product (identifying V* with V) and let w be the minimum-norm point of conv{D_j}. If w = 0, the convex weights give (II). Otherwise v = w satisfies D_j(w) >= |w|^2 > 0 for all j. This explicit, tight margin can serve as a deformation recipe, and |w| = max_{|v|<=1} min_j D_j(v). (II) excludes (I), since Sum lambda_j D_j(v) would be positive.

Present as a short remark, not as a significant new result. The analytic part (Collins' Thm 2, anomalous deformations) remains Collins' own.

**Literature check:** Gordan's theorem (1873) and the min-norm/projection proof are classical (convex analysis and optimization texts). No published identification of Collins' Thm 3 (arXiv:2007.04085) with Gordan's theorem was found: INSPIRE full-text searches, the sources of 2407.13738, 2407.17158, 2603.05444, 2204.02988, and stage 1's grep of all 39 citers. The closest related use is Farkas' lemma for graph orientations in arXiv:2609.18668. The underlying dual-cone fact is standard in microlocal analysis, so the identification is elementary.

## N03 — new_result — **confirmed**

**Claim:** OTHERS Cor 1.3 [R]†: the Coleman–Norton picture in momentum space, including massless and eikonal lines. A point is trapped iff there are λ_j ≥ 0, not all zero, on on-shell lines, with Σ_jη_jLλ_jΔ_j = 0 for every loop L (Δ_j = k_j or n_j). It follows from Collins Thm 1 under sign condition (8.15).

**Printable version:** Corollary (of Collins, arXiv:2007.04085, Thm 1) [R]†.

Setting: an integral over real loop momenta l_L, with every denominator written as (A_j + i0). Each A_j is one of:
- k_j^2 - m_j^2 (m_j >= 0);
- n_j.k_j (eikonal; the vector n_j is fixed by this +i0 convention, so 1/(n.k - i0) means n_j = -n);
- a light-front-approximated denominator.
Here k_j = sum_L eta_jL l_L + external.

Statement: the contour is trapped at a real point iff there exist lambda_j >= 0, not all zero, with lambda_j = 0 unless A_j = 0, such that sum_j eta_jL lambda_j Delta_j^mu = 0 for every loop L. Here Delta_j = k_j for propagators and Delta_j = n_j for eikonal lines.

Equivalently (Coleman-Norton), there are vertex positions with x_head(j) - x_tail(j) = lambda_j Delta_j. This is a classical process: massless lines move on light-like paths, eikonal lines move along n_j, and off-shell lines shrink to points.

Scope and limits:
- Soft massless lines (k_j = 0) always satisfy the condition, with zero displacement.
- The corollary asserts only that such a picture exists. It does not determine which vanishing denominators actually trap, nor the pinch surfaces of approximated graphs.
- Integrals with conjugated (-i0) propagators, i.e. cut graphs, are not covered without a separate argument.

**Literature check:** Not new in substance. It is a one-line specialization of Collins arXiv:2007.04085 Thm 1, which explicitly covers Wilson lines (statement of Thm 1; Sec. VIII B), combined with the classic Coleman-Norton closure (Nuovo Cim. 38 (1965) 438). That closure is textbook as a necessary condition, e.g. the review arXiv:2112.07099 (Agarwal-Magnea-Signorile-Signorile), section 'The Coleman-Norton physical picture'. Among the citers of Collins 2020 that deal with Landau or Coleman-Norton questions (eight sources grepped), none prints this iff-corollary with eikonal lines. Present it as a remark, not as a new theorem.

## N04 — new_result — **confirmed**

**Claim:** OTHERS Prop 8.1 [A]: moment reduction of the BRST classification for the bilocal ψ̄γ^+Wψ, under (H1) Joglekar–Lee/Henneaux, (H2) support in [−1,1], (H3) generating function of local operators. Then O^R = Z_OO⊗O in physical matrix elements, with ∫z^{N−1}Z_OO = Z^(N)_tw2, and EOM/BRST-exact operators drop out; uniqueness by Müntz–Szász. This closes the renormalization part of Collins 2011 §11.3.2; the multilocal step remains [C].

**Printable version:** Proposition [A] (moment reduction; prior art, not 'this work').

Operators: O_q(w^-) = psibar(w) gamma^+ W[w,0] psi(0), and the gluon analogue.

Hypotheses:
- (H1) Joglekar-Lee/Henneaux for the local twist-2 operators: [O_N] = Z_N O_N^bare + (BRST-exact) + (EOM), with triangular mixing.
- (H2) At each order, the forward matrix elements in the states considered are distributions supported in [-1,1].
- (H3) The bare bilocal operator is the generating function of the bare local operators.
- (H4) In each C-parity sector (a quark-gluon matrix for the singlet) there is a distribution Z_OO on [0,1] whose Mellin moments are the Z_N of that sector. Equivalently, there is a single kernel on [-1,1] for O_q with int_{-1}^{1} z^{N-1} Z = Z_N. This holds order by order in perturbation theory; at one loop the kernel is built from [(1+z^2)/(1-z)]_+.

Conclusion: in matrix elements between hadronic (BRST-invariant) states, or with operators inserted at non-zero momentum, O^R = Z_OO (x) O_bare is finite. It equals the generating function of the renormalized gauge-invariant local operators, and BRST/EOM admixtures drop out. This is Collins 2011 §11.4 eq. (11.20), restricted to physical matrix elements.

Uniqueness: Z_OO is unique on (0,1]. Within a parity sector this follows from Muentz-Szasz, up to distributions at z = 0; on [-1,1] with all N it follows from compact support alone.

Caveats:
- For forward on-shell partonic matrix elements in dimensional regularization, BRST and EOM operators need not drop out.
- The classification of general multilocal operators in the factorization step (Collins §11.3.2) remains [C].

**Literature check:** Yes. Braun-Manashov-Moch-Strohmaier, JHEP 02 (2019) 191 (arXiv:1901.06172), read:
- eq. (2.4): light-ray operators as generating functions of the local operators;
- eq. (2.6): 'Renormalized LROs are defined by the same expression with bare local operators replaced by the renormalized ones';
- eq. (3.1): the Joglekar-Lee decomposition into gauge-invariant, BRST and EOM parts;
- eq. (3.2): the gauge-invariant light-ray operator as the generating function of the gauge-invariant parts.
This is the general off-forward version, and the idea goes back to Balitsky-Braun 1989.

Collins 2011 §11.4 (pp. 411-412) asserts the triangular form (11.20) 'for the same reasons as with the local operators used in the OPE (Collins, 1984, p. 318)'.

The zero-momentum caveat is in BMMS arXiv:1810.04993 ('Conformal symmetry of QCD in d dimensions').

## N05 — new_result — **confirmed**

**Claim:** One-loop quasi-PDF in the unphysical regions from our own Feynman rules (a = α_sC_F/2π). Vertex a∫(1−y)/|ξ−y|; sail (a/(1−ξ))∫(ξ+y)/|ξ−y|; tadpole −a/|1−ξ|. Sum for ξ > 1: a[((1+ξ²)/(1−ξ))ln(ξ/(ξ−1)) + 1]; for ξ < 0: a[−((1+ξ²)/(1−ξ))ln(−ξ/(1−ξ)) − 1]. Agrees with IJJSZ App. B.

**Printable version:** One loop, with a = alpha_s C_F/(2 pi), Gamma = gamma^0, Feynman gauge, CONTEXT conventions, on-shell massless quark target, xi outside [0,1]:
- vertex graph: a int_0^1 dy (1-y)/|xi-y|;
- the two sail graphs together: (a/(1-xi)) int_0^1 dy (xi+y)/|xi-y|;
- Wilson-line self-energy (tadpole), in dimensional regularization: -a/|1-xi|. With a 3-D momentum cutoff it is +2a Lambda/(pi(1-xi)^2 p^z) - a/|1-xi|, i.e. linearly divergent. The vertex and sail graphs are finite in d = 4.

Sum:
- xi > 1: a[((1+xi^2)/(1-xi)) ln(xi/(xi-1)) + 1];
- xi < 0: a[-((1+xi^2)/(1-xi)) ln(-xi/(1-xi)) - 1];
- tail: -3a/(2|xi|).

This is an independent re-derivation of IJJSZ App. B eqs. (B1)-(B3) at eps = 0, and of the eps -> 0 limit of IJJSZ eq. (1loopquasi).

**Literature check:** Yes. Izubuchi-Ji-Jin-Stewart-Zhao, PRD 98 (2018) 056004 (arXiv:1801.03917): App. B eqs. (B1)-(B3) give the three graphs (at eps = 0 they are exactly the claimed expressions), and eq. (1loopquasi) gives the sum. Present it as an independent re-derivation, not as a new result.

## N06 — new_result — **confirmed**

**Claim:** One-loop threshold factorization of the LaMET kernel verified to |λ| = 1e5, including the phase sign. H_threshold = H_quasi-TMD at one loop. The summed one-loop anomalous dimensions, Γ_cusp[ln(λ²e^{2γ_E}) − iπ sgn z] plus non-cusp terms, are μ-independent.

**Printable version:** Take the one-loop MS-bar gamma^t coordinate-space kernel (IJJSZ). Conventions: lambda = P.z = -P^z z, l_z = ln(-z^2 mu^2 e^{2gamma_E}/4), L_z = ln(4p_z^2/mu^2), so that l_z + L_z = ln(lambda^2 e^{2gamma_E}).

Large-|lambda| limit (verified analytically, and numerically to |lambda| = 1e5 for both signs of lambda; residual 2.7e-4 at 1e5):
e^{-i lambda} h(lambda) = 1 + a[H^(1) + J^(1) + i pi sgn(z)(L_z - 1)] + O(ln^2|lambda|/|lambda|),
with H^(1) = -2 + pi^2/12 - L_z^2/2 + L_z and J^(1) = l_z^2/2 + l_z + pi^2/12 + 2.

This is the one-loop content of the Ji-Liu-Su threshold factorization C = H |p^z| J_f, and H^(1) equals the one-loop quasi-TMD hard kernel.

One-loop anomalous dimensions:
- d lnH/d ln mu = Gamma_cusp L_z + gamma_H;
- d ln J/d ln mu = Gamma_cusp l_z - gamma_J;
- the phase contributes -i pi Gamma_cusp sgn z;
- Gamma_cusp = alpha_s C_F/pi and gamma_H = gamma_J = -alpha_s C_F/pi.
Their sum, Gamma_cusp[ln(lambda^2 e^{2gamma_E}) - i pi sgn z], has no explicit mu dependence and equals the threshold limit of the kernel RGE. The non-cusp terms cancel at one loop.

**Literature check:** Yes. Ji-Liu-Su, JHEP 08 (2023) 037 (arXiv:2305.04416): eqs. (hardoneloop), (jetoneloop), (JetoneloopIM) and the RGEs (resulttildegammaJ, RGEH). The text after (hardoneloop) states both that H and J_f reproduce the one-loop quasi-PDF at power (1-y)^-1 and that H agrees with the quasi-TMDPDF/LFWF hard kernel. H^(1) is also Ebert-Stewart-Zhao arXiv:1901.03685 eq. (C_nlo) and Ji-Liu-Liu arXiv:1911.03840 (c_1). Present it as an independent cross-check.

## N07 — new_result — **confirmed**

**Claim:** Exact TMC for Γ = γ^0 (c = M²/(4P_z²)). K^⊥_N = Σ_i binom(N−i,i)((N−2i)/N)c^i = K_N − (2c/N)dK_N/dc; q̃_{γ0} = q̃_{γz} − 2c∫_0^1(dy/y)∂_c q̃_{γz}(x/y). K^⊥_1 = K^⊥_2 = 1, K^⊥_3 = 1 + 2c/3, K^⊥_4 = 1 + 3c/2. At O(c) this agrees with BVZ; TMC commutes with matching.

**Printable version:** Leading-twist target-mass correction for Gamma = gamma^0, with c = M^2/(4P_z^2) and the normalization P^z/P^0.

Moments: <x^{N-1}> of q_M^{gamma0} = Kperp_N a_N, with
Kperp_N = sum_i C(N-i,i)((N-2i)/N) c^i = K_N - (2c/N) dK_N/dc, where K_N = sum_i C(N-i,i) c^i is the gamma^z factor (Chen et al. 2016).
Explicit values: Kperp_1 = Kperp_2 = 1, so there is no TMC for the normalization or for <x>; Kperp_3 = 1 + 2c/3; Kperp_4 = 1 + 3c/2.

x space: q_M^{gamma0}(x) = q_M^{gamma z}(x) - 2c int_0^1 (dy/y) d_c q_M^{gamma z}(x/y). This is the same transformation as Chen et al.'s helicity TMC (App. B, with Delta q -> q).

At O(c): q - c(xq' + 3q) + 2c int_{|x|}^1 (dy/y) q(x/y), which is BVZ's (target-perp).

Relation to matching: to all orders in alpha_s at leading twist, q_Gamma = C_Gamma (x) q_M^Gamma, i.e. the massless kernel acts on the TMC-transformed PDF. The TMC does not literally commute with the momentum-space matching; that fails at O(alpha_s c). The gamma^0/gamma^z x-space identity relates the TMC-transformed tree-level distributions, not the full one-loop quasi-PDFs.

**Literature check:** Partly.
- Chen-Cohen-Ji-Lin-Zhang, NPB 911 (2016) 246 (arXiv:1603.06664): the helicity ratio Kbar_n = sum((n-i)/n) C(n-i-1,i) c^i (eq. Knbar) is identical to Kperp_n, and the helicity x-space solution in App. B is pointwise identical to the gamma^0 formula.
- The O(c) result is BVZ arXiv:1810.00048 eq. (target-perp), which BVZ say agrees with Chen et al.
- The exact P^z-independence of the first two gamma^0 moments is in Bhattacharya-Cocuzza-Metz, PRD 102 (2020) 054021 (arXiv:1903.05721).
- The all-order result follows from the Balitsky-Braun identity that BVZ quote.
- Not found in print: the explicit identification as the unpolarized gamma^0 TMC, and the d_c representation.

## N08 — new_result — **confirmed**

**Claim:** LaMET Lemma 5.2: FT[z²Λ²r(λ)] = +(Λ²/P_z²)ρ″(x), with endpoint factors a(a−1)/x² and b(b−1)/(1−x)². Cor 5.3: if ρ_4/q ~ (1−x)^δ, the correction is Λ²/((1−x)^{2−δ}P_z²); δ = 1 gives BVZ, δ = 0 the RMP rule. The P = 0 normalization adds −¼x̄x²q″/q to R^∥ (−5/12 for ⊥).

**Printable version:** Lemma [R] (elementary). Let rho be a distribution supported in [-1,1], r(lambda) = int dalpha e^{i alpha lambda} rho(alpha), and z^2 = -lambda^2/P_z^2 at fixed P^z. Then int dlambda/(2pi) e^{-ix lambda} z^2 Lambda^2 r(lambda) = +(Lambda^2/P_z^2) rho''(x), as distributions. If rho ~ x^a as x -> 0 and ~ (1-x)^b as x -> 1, then rho''/rho -> a(a-1)/x^2 and b(b-1)/(1-x)^2 respectively.

Corollary. If q ~ (1-x)^b and rho_4/q -> C(1-x)^delta with b+delta not 0 or 1, the relative power correction is (Lambda^2/P_z^2) C (b+delta)(b+delta-1)(1-x)^{delta-2}(1+o(1)).
- delta = 1 is the BVZ renormalon model (C = 1/(b+1), R -> b): Lambda^2/((1-x)P_z^2).
- delta = 0 is the RMP counting: Lambda^2/((1-x)^2 P_z^2).
- The endpoint behaviour of the true rho_4 is unknown ([C]).

Normalization to the P = 0 matrix element replaces k by [k]_+ = k - delta(1-alpha) int k, with int k = 1/4 (parallel) and 5/12 (perp). This adds -(1/4) xbar x^2 q''/q (respectively -(5/12)) to R (BVZ eq. (bR)), an effect proportional to 1/(1-x)^2 (delta = 0).

**Literature check:** Partly.
- The P = 0 normalization terms -1/4 and -5/12 and the 1/(1-x)^2 enhancement are BVZ arXiv:1810.00048 eq. (bR), with the sentence 'enhanced as 1/(1-x)^2 at x -> 1'.
- The Fourier identity is used implicitly in BVZ (t4-qITD) -> (t4-Qparallel).
- RMP arXiv:2004.03543 states both counting rules: eq. (fact_0), and later BVZ's 1/(1-y).
- The unified endpoint-dichotomy phrasing is not printed elsewhere, but it is an elementary reformulation.

## N09 — new_result — **refuted**

**Claim:** LaMET Props 4.4-4.5. Tails: C^MS → −3a/(2|ξ|) and C^ratio → ∓4a/(3ξ²). So the MS-bar quasi-PDF has no zeroth moment, while the ratio scheme has ∫q̃ = 1 with a log-divergent first moment. The MS-bar convolution converges iff ∫_0|f| < ∞; ratio/hybrid needs ∫_0|yf| < ∞, so a sea ~ y^{−1−δ} makes MS-bar ill-defined.

**Printable version:** 

**Literature check:** The tails follow directly from IJJSZ, PRD 98 (2018) 056004 [arXiv:1801.03917], eqs. (quasi-matching)/(quasi-matching-alt). IJJSZ note g_i ~ 1/xi^2 inside the plus functions and state that the MS-bar matching 'is valid for any PDF that behaves as f(y) ~ y^{-1+a} with a > 0'. The hybrid kernel, with lambda_S = z_S p^z (parton momentum), is Ji et al., NPB 964 (2021) 115311 [arXiv:2008.03886], eq. (hybridm2). No published statement of the (erroneous) hybrid/Regge-sea conclusions was found.

## N10 — new_result — **confirmed**

**Claim:** LaMET Lemma 7.2: decay e^{−m|z|} implies analyticity in |Im x| < m/P^z. Prop 7.3: the truncation error is ≤ (AP^z/(πm))e^{−mz_L}, with e^{−mz_L} = 0.079 (1 fm) and 0.022 (1.5 fm) at m = 0.5 GeV. Prop 7.4: about 2λ_L/π recoverable modes; the number of eigenvalues > ½ is 3, 6, 10, 16 for λ_L = 5, 10, 15, 25.

**Printable version:** Lemma 7.2 (Paley–Wiener-type, applied to LaMET). If |h̃(λ,−λ²/P_z²)| ≤ A(1+|λ|)^k e^{−m|λ|/P^z} for all real λ, then q̃(x,P^z) = ∫dλ/(2π) e^{−ixλ}h̃ extends holomorphically to the strip |Im x| < m/P^z. The width is sharp: for e^{−m|λ|/P^z}, q̃ is a Lorentzian with poles at ±im/P^z. In particular q̃ is real-analytic at x = 0, ±1 at finite P^z.

Prop. 7.3. If |h̃| ≤ A e^{−m|λ|/P^z} for |λ| > λ_L, then for real x
|q̃(x) − ∫_{|λ|≤λ_L}dλ/(2π) e^{−ixλ}h̃| ≤ (AP^z/(πm)) e^{−mz_L}, with z_L = λ_L/P^z.
The bound is attained for a positive tail at x = 0 and grows ∝ P^z. For m = 0.5 GeV, e^{−mz_L} = 0.0794 (z_L = 1 fm) and 0.0224 (z_L = 1.5 fm).

Prop. 7.4 (classical; Slepian–Pollak, Landau–Widom). The operator (Kf)(x) = ∫_{−1}^1 [sin λ_L(x−y)/(π(x−y))] f(y)dy on L²[−1,1] has eigenvalues in (0,1) and trace 2λ_L/π. The count satisfies N(α) = 2λ_L/π + π^{−2} ln((1−α)/α) ln λ_L + o(ln λ_L). The number of eigenvalues above 1/2 is 3, 6, 10, 16 for λ_L = 5, 10, 15, 25. 'About 2λ_L/π recoverable modes' is the standard interpretation of these facts, not a theorem.

**Literature check:** Yes, in substance.
- Lemma 7.2 is a classical Paley–Wiener-type theorem (Paley–Wiener, AMS Colloq. Publ. 19, 1934).
- Prop. 7.4 is classical: Slepian–Pollak, Bell Syst. Tech. J. 40 (1961) 43; Landau–Widom, J. Math. Anal. Appl. 77 (1980) 469.
- Both are applied to LaMET quasi-PDFs in Monahan & Neumann, arXiv:2609.40205 (Sept 2026), §'The region |x|>1'. They write that the distribution 'has no singularities within a distance m/P^z of the real axis [Paley:1934]', and that the data determine 'about 2ν_max/π [Slepian:1961, Landau:1980] ... ν_max ≈ 10 and about six numbers'.
- Qualitative analyticity at y = 0, 1: Ji, NPB 1007 (2024) 116670 (arXiv:2408.03378); Xiong et al., EPJC 85 (2025) 1409.
- Not printed elsewhere, but elementary: the explicit majorant of Prop. 7.3 and the exact counts 3, 6, 10, 16.

## N11 — new_result — **confirmed**

**Claim:** Lean-style dependency graph of the LaMET matching theorem (N0-N13). Non-perturbative content is isolated in (H3)-(H5). Grades: N1 (space-like auxiliary field) [A]; N3 multiplicative renormalizability [A]; N4 space-like OPE [A], with no Zimmermann-level proof; N5 support [R].

**Printable version:** The §4.5 table of LAMET is a consistent dependency graph: no node is graded above its weakest parent or its implication.

For the MS-bar form of the hadronic matching theorem Thm 4.3(ii) (and the hybrid scheme, as graded), the non-perturbative inputs are exactly (H3), the non-perturbative part of (H4), and (H5). Momentum-space matching in the ratio or RI/MOM scheme needs one more non-perturbative input: perturbativity of Z'_X at all relevant z (node N13, [C]).

Grades:
- N1 [A]: JZZ argue all-order renormalizability of QCD plus a space-like auxiliary static field by analogy with the HQET BRST proof.
- N3 [A]: multiplicative renormalizability of O_Γ(z), via the JZZ/GJS auxiliary-field route and IMQY's power counting of overall divergences.
- N4 [A], stated as a judgment: the space-like OPE is 'widely assumed' for QCD (IJJSZ), and no Zimmermann-level proof exists for the non-covariant auxiliary-field theory.
- N5 [R] in perturbation theory: support in [−1,1] for every Feynman diagram.

**Literature check:** Not in this form; the result is organizational. Sources of the individual grades, all checked as accurate:
- Ji–Zhang–Zhao, PRL 120 (2018) 112001 [1706.08962]
- Ishikawa–Ma–Qiu–Yoshida, PRD 96 (2017) 094019 [1707.03107]
- Green–Jansen–Steffens, PRL 121 (2018) 022004 [1707.07152]
- Izubuchi–Ji–Jin–Stewart–Zhao, PRD 98 (2018) 056004 [1801.03917]
- Radyushkin, PLB 131 (1983) 179 (not read) and arXiv:1705.01488

## N12 — new_result — **confirmed**

**Claim:** prop:appN-triangle-exact (sharpened). Off-shell one-loop triangle with Q̃² = 2PP′ and Q² = (Q̃² + m²)²/Q̃²; the subtraction terms sum to Q̃^{−2}[ln²(Q̃²/m²) + π²/3]. Exact remainder: ∫r = −4m²/Q⁴ + (m⁴/Q⁶)(L² − 15 + π²/3) + O(m⁶Q^{−8}L²), with no NLP log; here Q²I = L² + π²/3 + t(2L² − 4L − 4 + 2π²/3). ∫r = −0.0173434339581 at m² = 0.02, P = 0.8, P′ = 1.3.

**Printable version:** Setting: scalar off-shell triangle with massless internal lines; p1 = (P, −m²/(2P), 0_T), p2 = (m²/(2P′), −P′, 0_T); Q̃² = 2PP′; Q² = −(p1+p2)² = (Q̃²+m²)²/Q̃²; measure μ^{2ε}d^dk/(iπ^{d/2}); the reference's approximators (D.26).

(a) The subtraction terms are absolutely convergent for 0<ε<1:
- ∫C_HΓ = Q̃^{−2}(μ²/Q̃²)^ε𝒜
- ∫C_{C1}Γ = ∫C_{C2}Γ = −Q̃^{−2}(μ²/m²)^ε𝒜
- ∫C_SΓ = Q̃^{−2}(μ²Q̃²/m⁴)^ε𝓑
with 𝒜 = Γ(1+ε)Γ(1−ε)²/(ε²Γ(1−2ε)) and 𝓑 = Γ(1+ε)²Γ(1−ε)/ε².

(b) Σ_R∫C_RΓ → Q̃^{−2}[ln²(Q̃²/m²) + π²/3] as ε → 0.

(c) With I = Φ^{(1)}(t,t)/Q² (Usyukina–Davydychev), t = m²/Q², L = ln(Q²/m²), σ = m²/Q̃²:
∫r = I − Σ_R = [4Li₂(−σ) + σ²(ln²σ + π²/3)]/(Q̃²(1−σ²)) = −4m²/Q⁴ + (m⁴/Q⁶)(L² − 15 + π²/3) + O(m⁶Q^{−8}L²).
There is no logarithm at NLP. Also Q²I = L² + π²/3 + t(2L² − 4L − 4 + 2π²/3) + O(t²L²); the NLP logarithms of I are reproduced by the subtraction terms through Q̃² ≠ Q².

Numerically ∫r = −0.0173434339581 at m² = 0.02, P = 0.8, P′ = 1.3.

**Literature check:** Partly.
- Φ^{(1)} is Usyukina–Davydychev, PLB 298 (1993) 363; the same function is printed in UD hep-ph/9307327.
- Collins, Foundations of Perturbative QCD (2011), ch. 10 'Factorization and subtractions', §10.3–10.5 (Sudakov form factor), is the framework.
- The explicit subtraction values for the reference's approximators, the closed-form remainder and its expansion were not found in INSPIRE full-text searches. The result is elementary but appears unpublished; it is the reference's Ex. D.47 sharpened.

## N13 — new_result — **refuted**

**Claim:** lem:appO-joint-localization (sharpened) replaces Ass E.33(c1). Equal-time limit of N single-pole Glauber insertions: weights w_π = Π_jz_j/Π_mΣ_{l≥m}z_{π(l)}, with z_j = k_Tj²/(2k_j^+), for same-side poles (0/1 otherwise); N = 2 gives w_12 = z_1/(z_1+z_2). Non-analytic at k_j^+ = 0.

**Printable version:** 

**Literature check:** Partly.
- The lower-half-plane N-insertion formula is printed in the reference document itself (p. 196; not citable).
- sum_pi w_pi = 1 is the classical eikonal (shuffle) identity.
- The LCOPT precedent, Aybat–Sterman, PLB 671 (2009) 46–50 (arXiv:0811.0246), is verified: the paper uses light-cone-ordered perturbation theory. It does not contain the weights.
- No published source with the upper-half-plane or mixed-sign cases was found (search not exhaustive).

## N14 — new_result — **unresolved**

**Claim:** Further 'surpass' items of the reference analysis: (i) Ass E.18(iii) provable (lem:appJ-cut-hermiticity, standard); (ii) a side-independent window construction for E14 (to check); (iii) an attempt to discharge Ass C.24 via Anikin–Zav'yalov / Zav'yalov 1990 plus uniqueness Thm C.25(iii); (iv) App O supplies input D.27 (X1).

**Printable version:** 

**Literature check:** (i) is standard:
- Veltman, Physica 29 (1963) 186–207 (largest-time equation);
- 't Hooft–Veltman, Diagrammar, CERN-73-09 (1973);
- Kugo–Ojima, Prog. Theor. Phys. Suppl. 66 (1979) 1–130.

(iii) Anikin–Zav'yalov, Ann. Phys. 116 (1978) 135 (scope unverified). Related works:
- Karchev, NPB 211 (1983) 55 (QCD light-cone expansion);
- Zav'yalov–Polivanov, Ukr. Math. J. 44 (1992) (massless theories);
- Keller–Kopper, CMP 153 (1993) 245 (massive phi^4_4, flow equations).

## N15 — new_result — **confirmed**

**Claim:** Sharpened reference Ex C.27: the combination equals −κπ²/(2q⁴) + O(m²q^{−6}ln q), with no log and an m-independent leading term (4D harmonicity), against 'O(q^{−4}ln q²)'. F3 lesson: per-order region exponents (e.g. 1/243 for the two-loop (S,S) region) can be far from sharp.

**Printable version:** In Euclidean space with Δ(k) = 1/(k²+m²):
κ∫d⁴k[Δ(q−k) − Δ(q)]Δ(k)³ = −κπ²/(2q⁴) + κ(m²/q⁶)[−2π² ln(q²/m²) + 7π²/2] + O(κm⁴q^{−8} ln² q).
The leading term is independent of m and has no logarithm; this follows from the 4D mean-value property ⟨1/(q−k)²⟩_{S³} = 1/max(q²,k²). The reference's O(q^{−4} ln q²) is a non-sharp bound.

F3: with the reference's rule β_R = 3^{h(R)−h*}, a_R = β_R/3, the two-loop planar vertex (9 leading regions, h* = 4) gives a_(S,S) = 1/243, and the one-loop triangle gives a_S = 1/27. The exact one-loop Collins remainder is O(λ²) (relative O(λ²/L²)), so per-order region exponents can be far from sharp. The two-loop true remainder has not been computed.

**Literature check:** No external source is needed. This is the reference document's own Ex. C.27 (pp. 101–102), sharpened by an elementary asymptotic evaluation. The region rule is the reference's own (text after (D.6); (D.17)).

## N16 — new_result — **confirmed**

**Claim:** c_glauber's own proof of Collins 2007's unproven I_1(0) + I_2(0) < 0. With dμ = d²b/(2π)²·2πK_0(m_qb), Cauchy–Schwarz gives F(0)² < G(0)/m_q². Also ∫d²k_T(I_1+I_2) = 0 by Parseval, with F(k) = (π/√Λ)ln((s+√Λ)/(s−√Λ)). (I_1+I_2)/𝒩 = −21.0 … +0.089 for k_T = 0 … 6.

**Printable version:** In Collins's scalar model (arXiv:0708.4410v1, eqs. (10)–(11)):
I₁(k_T) = 𝒩F(k_T)² and I₂(k_T) = −𝒩G(k_T)/(k_T²+m_q²), with 𝒩 = λ²g₁²g₂(g₂+g₁)x(1−x)/(256π⁷).
- F(k) = ∫d²l/((l²+m_g²)((k−l)²+m_q²)) = (π/√Λ) ln((s+√Λ)/(s−√Λ)), where s = k²+m_g²+m_q² and Λ = s²−4m_g²m_q².
- G(k) = ∫d²l₁d²l₂/((l₁²+m_g²)(l₂²+m_g²)((k−l₁−l₂)²+m_q²)).
- The factor Π_j(k_T²+m_q²) in the printed second line of eq. (10) is a misprint.

In b-space, F̃ = (2π)²K₀(m_g b)K₀(m_q b) and G̃ = (2π)³K₀(m_g b)²K₀(m_q b). Hence ∫d²k_T(I₁+I₂) = 0 by Parseval.

Take the positive measure dμ = d²b/(2π)²·2πK₀(m_q b). Then ∫dμ = 1/m_q², F(0) = ∫dμ 2πK₀(m_g b) and G(0) = ∫dμ[2πK₀(m_g b)]². Cauchy–Schwarz gives F(0)² < G(0)/m_q² strictly, so sign(I₁(0)+I₂(0)) = −sign 𝒩 = −sign[g₂(g₂+g₁)]. This is negative in Collins's case g₂(g₂+g₁) > 0.

For (m_g, m_q) = (0.5, 1), (I₁+I₂)/𝒩 = −21.01, −17.73, −7.19, −0.70, +0.38, +0.089 at k_T = 0, 0.3, 0.8, 1.5, 3, 6.

**Literature check:** No published proof was found: I searched the INSPIRE full text of the 93 records citing Collins:2007jp for 'Cauchy-Schwarz', 'Schwarz inequality', 'Parseval' and 'I_1(0)', with no hits. The proof is elementary.
Ingredients: Collins arXiv:0708.4410 eqs. (10)–(11); Rogers–Mulders PRD 81 (2010) 094006, eqs. (27)–(28), the massless non-abelian analogue, which corroborates the corrected eq. (10).

## N17 — new_result — **confirmed**

**Claim:** Entanglement test: Σ_{X,Y}C(X,Y) = C_F² + 4T_F²(N²−1)/N², whereas the factorized prediction is C_F². For SU(3) this is 24/9 vs 16/9; the abelian case factorizes.

**Printable version:** Setting: the Rogers–Mulders double-Sivers model, with a colour-neutral hard exchange and colour-singlet hadrons each made of a fundamental quark and an antitriplet spectator. Assume equal pole coefficients for eikonal attachments to incoming and outgoing quark lines.

Then the double-pole colour weight relative to tree is
Σ_{X∈{3,4,2}, Y∈{4,3,1}} C(X,Y) = C_F² + 4T_F²(N²−1)/N² = C_F²[1 + 4/(N²−1)].
The same holds with the two gluons on the same side or on opposite sides of the cut. The pieces are: C(3,4) = C_F²; each of the four crossed attachments (X∈{4,2}, Y∈{3,1}) contributes T_F²(N²−1)/N²; mixed attachments vanish.

Any formula with a separate Wilson-line structure per hadron predicts (Σ_X C₁(X))(Σ_Y C₂(Y)) = C_F². For SU(3) this is 24/9 vs 16/9. For U(1) the two-gluon weights factorize.

This is Rogers–Mulders' argument (eq. (34)) in attachment-sum form, and the ratio is Zhou's R = 1 + 4/(N_c²−1).

**Literature check:** Yes.
- Rogers–Mulders, PRD 81 (2010) 094006 [arXiv:1001.2977]: crossed-class colour factor Tr_C[t^at^b]Tr_C[t^bt^a] = T_F²(N_c²−1) in eq. (34), against the generalized-factorization prediction 0 (eq. (33)).
- J. Zhou, arXiv:2610.11258 (8 Oct 2026), eq. (1): R = 1 + 4/(N_c²−1), with uncrossed colour N_c²C_F² and crossed colour (N_c²−1)/4.

## N18 — new_result — **confirmed**

**Claim:** With the pole rule P = −T_a − 2T_b, the gluonic-pole strength is C_G = 1 + 2⟨T_a·T_b⟩/C_F. Channels: (N²−5)/(N²−1), −(N²+3)/(N²−1), −(N²−3)/(N²−1), (N²+1)/(N²−1). QVY graph ratios: −2/(N²−1), −1/(N²−1), (N²−2)/(N²−1). Exact agreement with BBMP and QVY.

**Printable version:** Let a (from the polarized hadron) and b be the incoming partons of the hard process. An eikonal attachment of the spectator gluon has the same pole part -i pi delta(l^+) g t^a on incoming and outgoing quark lines (Collins-Qiu 2007 eqs. (4.1)-(4.3); Collins 2007 eq. (2)). Hence the gluonic-pole parts sum to the colour operator P = sum_out T_j - sum_{in, j != a} T_j = -T_a - 2T_b (Catani-Seymour charges, colour conservation). Normalised to SIDIS, the gluonic-pole strength is C_G = <(-T_a).P>/C_F = 1 + 2<T_a.T_b>/C_F (SIDIS +1, DY -1). Exactly in N: qq tt* and uu*: (N^2-5)/(N^2-1) [<T_a.T_b> = -1/N]; qq tu*: -(N^2+3)/(N^2-1) [-(N^2+1)/(2N)]; q qbar tt*: -(N^2-3)/(N^2-1) [-(N^2-2)/(2N)]; q qbar -> q' qbar' ss* and q qbar -> q qbar st*: (N^2+1)/(N^2-1) [1/(2N)]. For SU(3) these are 1/2, -3/2, -3/4, 5/4, equal to BBMP 2005 Table I and eqs. (B5),(B6). Graph by graph for the t-channel diagram (1) of QVY 2007 Fig. 8: C_I/C_u = -2/(N^2-1), C_F1/C_u = -1/(N^2-1) (jet on the polarized quark's line), C_F2/C_u = (N^2-2)/(N^2-1) (SU(3): -1/4, -1/8, 7/8). All entries of QVY Table I and eqs. (25)-(28) are reproduced exactly in N.

**Literature check:** The channel values are in Bacchetta-Bomhof-Mulders-Pijlman, PRD 72 (2005) 034030, hep-ph/0505268, Table I, eqs. (B5),(B6), and in Qiu-Vogelsang-Yuan, PRD 76 (2007) 074029, arXiv:0706.1196, Table I, eqs. (25)-(28). The attachment rule in Wilson-line form (links stuck at each external parton, future-pointing for outgoing and past-pointing for incoming) is in Buffing-Mulders, JHEP 07 (2011) 065, arXiv:1105.4804. Ratcliffe-Teryaev, hep-ph/0703293, state qualitatively that the colour factor is set by the colour charge of the parton in the ISI/FSI; their -1/(2N_c) and N_c/2 equal <-T_a.T_X>. I did not find the compact closed form 1 + 2<T_a.T_b>/C_F stated explicitly. I checked an INSPIRE full-text search ('gluonic pole' and 'color charge', 15 hits screened), Liu-Ringer-Vogelsang-Yuan arXiv:2008.03666 (which uses QVY's C's) and Zhou arXiv:2610.11258. The search was not exhaustive.

## N19 — new_result — **confirmed**

**Claim:** Further c_glauber results: (i) an exact finite-ε cut-sum telescoping identity; (ii) ladder/crossed colour L = c², X = c² + (C_A/2)c for any representations; (iii) V = −ie_Ae_B/(k_T² + m_g²), χ(b) = −e_Ae_BK_0(m_gb)/(2π); (iv) singlet→octet leakage coefficient C_F/(2N) = 2/9.

**Printable version:** (i) For every N and every eps > 0: sum_{c=1}^N [prod_{f>c}(a_f - i eps)^{-1}] * 2eps/(a_c^2+eps^2) * [prod_{f<c}(a_f + i eps)^{-1}] = i prod_f (a_f + i eps)^{-1} - i prod_f (a_f - i eps)^{-1}. For a_f = E - d_f, the integral of dE/(2pi) gives 1 for N = 1 and 0 for N >= 2. This is the eps-regulated form of Collins 2011 eqs. (14.29)-(14.30); (14.30) is printed there with the overall sign reversed. (ii) For two gluons exchanged between lines in arbitrary representations, with c = T1.T2: ladder L = c^2, crossed ladder X = c^2 + (C_A/2) c. A Glauber phase does not commute with other soft exchanges: [T_A.T_B, T_A.T_j] = i f^{abc} T_A^c T_B^a T_j^b != 0. (iii) The abelian spectator-spectator Glauber exchange is M^(1)(p_A',p_B') = int d^2k_T/(2pi)^2 V(k_T) M^(0)(p_A'-k_T, p_B'+k_T), with V = -i e_A e_B/(k_T^2+m_g^2). Equivalently Mtilde^(1)(b) = i chi(b) Mtilde^(0)(b) with chi(b) = -e_A e_B K0(m_g b)/(2pi). (iv) Dipole toy: for U = exp(i d T_q.T_B) (B fundamental, colour averaged), 1 - P_singlet = ((N^2-1)/N^2) sin^2(d/2) = (C_F/(2N)) d^2 + O(d^4), with coefficient 2/9 for SU(3). For U = exp(i(chi1 T_q + chi2 T_qbar).T_B) the singlet-to-octet leakage is (chi1-chi2)^2 C_F/(2N) to second order in the phases.

**Literature check:** (i) This is Collins, Foundations of Perturbative QCD (2011), Sec. 14.4.3, eqs. (14.29)-(14.30), p. 559 of the OA reissue, at i0. As printed, (14.30) has the overall sign reversed. (ii) It is a standard one-line Lie-algebra identity (the box versus crossed-box colour difference of non-abelian exponentiation). Rothstein-Stewart 2016 (arXiv:1601.04695) note only that the box and crossbox colour factors differ (stage-1 reading). (iii) It is the standard eikonal phase; Rothstein-Stewart 2016 Sec. 9 has the gluon-mass form (stage-1 reading). (iv) It is a toy model; I found no earlier source. Novelty is not claimed.

## N20 — new_result — **confirmed**

**Claim:** New one-loop illustration. With space-like regulator lines V^SIDIS = (V^DY)*. With time-like lines Re V^DY − V^SIDIS = (α_sC_F/4π)·2π², since the past-pointing path-ordered operator is anti-time-ordered. So the PT/Sivers-sign argument fails for time-like lines at finite rapidity; the remainder's Fourier transform is 2π²/(Λ_Bb_T).

**Printable version:** Consider the one-loop vertex graph of the unsubtracted TMD for a massless on-shell quark p with a non-light-like Wilson line n (Feynman gauge, pure DR). Let V^time = -(alpha_s C_F/4pi)(pi mu^2 |n^2|/(p.n)^2)^eps Gamma(1-eps)Gamma(1+2eps)(1-eps)/((1-2eps)eps^2), which is real. Then V_SIDIS^time = V^time, V_DY^time = e^{2pi i eps} V^time, V_SIDIS^space = e^{-i pi eps} V^time and V_DY^space = e^{+i pi eps} V^time. Hence for space-like lines V_SIDIS = (V_DY)* exactly. For time-like lines Re V_DY - V_SIDIS = (alpha_s C_F/4pi)[2pi^2 + O(eps)] and Im V_DY = (alpha_s C_F/4pi)(-2pi/eps + ...), a Coulomb phase. The reason is that a past-pointing time-like path-ordered Wilson line is anti-time-ordered, whereas the Feynman rules (and the factorization derivation) give the time-ordered product. So at finite rapidity the PT image of the SIDIS TMD is not the DY TMD that enters factorization, and the Sivers-sign (PT) argument fails for time-like lines. For space-like (Collins) lines path and time ordering coincide. All these terms are proportional to |n^2|^eps and vanish when the light-like limit is taken first (Re eps > 0). For the real graphs, the remainder D(kappa) = ln(1+kappa^2) + 2kappa arctan(1/kappa), kappa = k_T/Lambda_B, has 2D Fourier transform 4pi int_0^inf sin(s) arcsinh(s/z)/s^2 ds = 2pi^2/z + O(e^{-z}) with z = Lambda_B b_T, so it vanishes as Lambda_B -> infinity at fixed b_T. This supports the space-like choice of Collins 2011 (Sec. 10.6.4, pp. 349-350; Sec. 10.11.1, p. 381; order of limits Sec. 10.8.2; cf. Exercise 13.8, p. 538) and of Aybat-Rogers 2011, following Collins-Metz 2004.

**Literature check:** The mechanism is stated qualitatively in the literature: space-like lines make path ordering compatible with time ordering and are needed for universality. See Collins-Metz, PRL 93 (2004) 252001; Collins 2011 Sec. 10.6.4 (pp. 349-350; time-like vectors possible 'if one gave up the argument about universality ... need further investigation') and Sec. 10.11.1 (p. 381); Aybat-Rogers 2011. Collins 2011 Exercise 13.8 (p. 538) poses exactly the question of whether time-like lines cause problems. I did not find the explicit one-loop phase relations (e^{2pi i eps}, e^{+-i pi eps}) or the 2pi^2 difference in the sources read; the search was not exhaustive. Ji-Ma-Yuan 2004 use time-like vectors but discuss only the soft factor.

## N21 — new_result — **confirmed**

**Claim:** Exact ILS soft fractions (c = μ_0²/Q²): R_as = c[5c − 2(c+2)ln c − 4]; R_CZ = c[456c³ + 352c² − 675c − 132 − (144c³ + 768c² + 450c + 36)ln c]. For μ_0² = 1 GeV²: 0.87, 0.62, 0.15 at Q² = 4, 10, 100 GeV² (CZ 0.98, 0.90, 0.48).

**Printable version:** Let R(c), with c = mu_0^2/Q^2 <= 1, be the fraction of the LO u-line integral int int phi(x)phi(y)/(xbar ybar) that comes from the region xbar ybar Q^2 < mu_0^2. For the asymptotic DA phi = 6x xbar, R_as(c) = c[5c - 2(c+2) ln c - 4]. For the CZ DA phi = 30 x xbar (2x-1)^2, R_CZ(c) = c[456c^3 + 352c^2 - 675c - 132 - (144c^3 + 768c^2 + 450c + 36) ln c]. In both cases R(1) = 1 and R increases monotonically, with R_as ~ 4c ln(1/c) and R_CZ ~ 36c ln(1/c) as c -> 0. For mu_0^2 = 1 GeV^2, R_as = 0.87, 0.62, 0.15 and R_CZ = 0.98, 0.90, 0.48 at Q^2 = 4, 10, 100 GeV^2. Isgur and Llewellyn Smith's fraction function is f(eps) = 1 - R(eps); for the asymptotic DA, f(1/150) = 0.892. The concept is ILS's (NPB 317 (1989) 526). The closed forms are derived here, and their novelty is not asserted because ILS 1989 could not be checked.

**Literature check:** The concept is Isgur-Llewellyn Smith's fraction function. Yeh, hep-ph/0107192, Sec. IV, attributes it to ILS PRL 52 (1984) 1080 and NPB 317 (1989) 526 and quotes '90% for eps = 1/150' for the asymptotic DA, which our formula reproduces (0.892). Stage 1 found no fraction function in the 1984 preprint, which points to ILS 1989 (possibly also ILS PLB 217 (1989) 535). I found no closed form in Yeh 2001 or Brodsky-Ji-Pang-Robertson hep-ph/9705221. The ILS 1989 papers were not accessible, so the novelty of the closed forms cannot be established.

## N22 — new_result — **refuted**

**Claim:** X_A model prescription dependence: cutting x < 1−δ and y > δ instead of the BN rule shifts A_3^i by −21.6 at X_A = 13.8; it is a model, not a theorem. Re-derived: A_1^i ≈ A_2^i ≈ πα_s[18(X_A − 4 + π²/3) + 2r_χ²X_A²]; A_3^i ≈ 6πα_s(r_χ^{M1} − r_χ^{M2})(X_A² − 2X_A + π²/3).

**Printable version:** 

**Literature check:** The formulas are BN 2003 (hep-ph/0308039) eq. (XAmodel) and BBNS 2001 (hep-ph/0104110) eq. (XAdef). The model dependence is stated by both papers: BN 2003, 'The treatment of weak annihilation is model-dependent in the QCD factorization approach'; BBNS 2001, 'taking the same value of X_A for all annihilation terms is a crude model'. I did not find the specific -pi^2 regulator shift in the literature.

## N23 — new_result — **confirmed**

**Claim:** Own proofs of classical facts (novelty not claimed). c_pdf Thm 7.2 (even moments plus Hausdorff), Cor 7.3, Prop 7.5, Prop 7.7 (replaces Carlson), and the L² Müntz distance (π/sinh(√3π) = 0.02722). The Gegenbauer eigenfunction proof. REVIEW counterexamples: sin(Q²x), δ′(x), (1 − cos πn)/2.

**Printable version:** Own proofs of classical facts (novelty not claimed). (Thm 7.2) If x^{2k0} g is in L^1(0,1) and int x^{2k} g = 0 for all k >= k0, then g = 0 a.e. The proof uses h(t) = (1/2) t^{k0-1/2} g(sqrt t) and Hausdorff/Weierstrass uniqueness. (Cor 7.3) a_N = int_0^1 x^{N-1}[q + (-1)^N qbar]: even moments with N >= N1 determine q + qbar and g, odd moments determine q - qbar, and even moments alone do not separate q from qbar. (Prop 7.5) P = r + a[1/(1-x)]_+ + b delta(1-x) with |r| <= C/x is fixed by its even moments, using Mellin[1/(1-x)]_+ = -(psi(N)+gamma_E). (Prop 7.7) A function holomorphic and polynomially bounded in Re z > sigma0 that vanishes on an arithmetic progression is identically zero (Cayley map, Jensen, Blaschke condition). (Mueller) dist_{L^2(0,1)}(x^lambda, span{x^{lambda_k}}) = (2lambda+1)^{-1/2} prod |lambda - lambda_k|/(lambda + lambda_k + 1). In particular dist(x, span{x^{k^2+1}: k >= 1}) = (1/sqrt3) prod_{k>=1} k^2/(k^2+3) = pi/sinh(sqrt3 pi) = 0.02723 (0.0272282). (ERBL) V_0 is self-adjoint for <f,g> = int fg/(x xbar) and maps x xbar P_k into x xbar P_k for all k (the x^{k+1} coefficients +-(1/(k+2) - 1/2) cancel). Hence the eigenfunctions are x xbar C_n^{3/2}(2x-1) with eigenvalues v_n = C_F[-1/2 + 1/((n+1)(n+2)) - 2 sum_{j=2}^{n+1} 1/j] = int z^n P_qq. (Counterexamples) Moments of sin(Q^2 x) are O(1/Q^2) uniformly in n while sup|sin(Q^2 x)| = 1. delta'(x) has all even moments zero. From even integers alone the Carlson type bound halves to < pi/2, and the sharp counterexample is sin(pi n/2) (type pi/2). The function (1 - cos pi n)/2 vanishes on even n but has type pi, so it is not the right example for the pi/2 threshold.

**Literature check:** All items are classical. Hausdorff (1921/23) uniqueness via Weierstrass; the Mueller-Szasz theorem and the Cauchy-determinant distance formula; the Blaschke condition via Jensen (e.g. Rudin, Real and Complex Analysis, ch. 15). Carlson's theorem: Titchmarsh, Theory of Functions Sec. 5.81, and Boas, Entire Functions Th. 9.2.1, both cited for it by Waldschmidt, arXiv:2002.01223 (verified in the source). The Gegenbauer eigenfunctions of ERBL are due to Efremov-Radyushkin and Lepage-Brodsky (1979/80); I did not re-read these. The REVIEW counterexamples are elementary.

## N24 — new_result — **confirmed**

**Claim:** thm:ee-R-finite [R, R_PT]. Euclidean finiteness plus Laurent coefficients that are polynomials in L and vanish for real L, hence identically. The DR cut-sum identification is [A]. Exact-in-ε cutting identity: 2(D−1)s Im Π^(1)_bare = ρ_V + ρ_R. Π_MS = N_ce²/(12π²)[5/3 − L + (α_s/π)(3C_F/4)(55/12 − 4ζ_3 − L)].

**Printable version:** Theorem ([R], given the cited Euclidean-finiteness inputs). In massless QCD, at each order in alpha_s(mu), the MS-bar renormalised vector correlator has the form Pi_MS(q^2; eps) = sum_k [Laurent series in eps] (Q^2/mu^2)^{-k eps} + q-independent pure poles, with Q^2 = -q^2 - i0. Its Laurent coefficients are therefore polynomials in L = ln(-q^2/mu^2). Euclidean finiteness of the renormalised correlator gives the inputs: Poggio-Quinn 1976; Breitenlohner-Maison II (CMP 52 (1977) 55) for massless theories whose interaction terms all have IR degree >= 4, a condition met by massless QCD in covariant gauges including Faddeev-Popov ghosts. This forces all negative-order coefficients to vanish identically. Hence Pi_MS(s+i0) has a finite limit as eps -> 0, and R = 12 pi Im Pi_MS(s+i0) is IR finite to all orders. The identification with the DR sum over partonic cuts is [A]. Exactly in eps: 2(D-1) s Im Pi^(1)_bare(s+i0) = rho_V + rho_R, term by term, where Pi^(1)_bare = N_c e_q^2 C_F g0^2 (Q^2)^{-2eps}/(4pi)^D [r1 G(1,1)^2 + r2 G(1,1)G(1+eps,1)] with r1 = -4(1-eps)(2-eps+2eps^2)/(eps(3-2eps)) and r2 = 16(1-eps)(1-2eps)(2-2eps+eps^2)/(eps(3-2eps)(2-3eps)); the G(1,1)^2 term equals the virtual (two-parton) cut and the G(1,1)G(1+eps,1) term the real (three-parton) cut. In MS-bar, Pi_MS = (N_c sum_q e_q^2/(12 pi^2))[5/3 - L + (alpha_s/pi)(3C_F/4)(55/12 - 4 zeta3 - L)] + O(alpha_s^2), with e_q in units of e. Hence R = N_c sum e_q^2 [1 + (3C_F/4) alpha_s/pi].

**Literature check:** The route is the corollary of Poggio-Quinn, PRD 14 (1976) 578: physical discontinuities are IR finite. The rigorous inputs are Lowenstein-Zimmermann CMP 44 (1975) 73, Lowenstein CMP 47 (1976) 53, and Breitenlohner-Maison CMP 52 (1977) 11, 39, 55 (BM II read here). The two-loop d-dimensional photon self-energy is standard: Grozin, hep-ph/0508242 (stage-1 reading); Chetyrkin-Tkachov IBP. The MS-bar constant 55/12 - 4 zeta3 is standard; I did not re-read a primary source and derived it independently here. The exact-in-eps cutting check is unitarity in DR (Cutkosky, Veltman, 't Hooft-Veltman); the explicit term-by-term O(g^2) form was not found stated elsewhere, and novelty is not claimed.

## N25 — new_result — **confirmed**

**Claim:** Abelian DY Glauber toy: χ(b) = −(g_Ag_B/2π)K_0(m|b|); S–S exchange is trapped and cancels after the k_T integral. The active–spectator exchange is not trapped in k^+ and equals the A-collinear term with a past-pointing line [P]: I_as = 2πiθ(−k^-)/(2p_b^-K² + 2k^-c_b). Plus trap: (1+z²)𝒟_1 vs [(1+z²)/(1−z)]_+ differ by (7/4)δ(1−z).

**Printable version:** Abelian toy model of Drell-Yan: a massive vector boson (mass m, Feynman gauge) and charged scalar partons/spectators, at leading power in lambda; grade [P].

(G-i) For infinite light-like eikonal spectators, the spectator-spectator exchanges exponentiate exactly to e^{i chi(b)}, with chi(b) = -(g_A g_B/2 pi) K_0(m|b|). chi is real; b is the spectators' relative transverse separation; self-energies vanish because v^2 = 0.

(G-ii) For any cross section inclusive in the spectators' RELATIVE transverse momentum, the phase cancels: order by order between the cut positions (i chi - i chi = 0; chi^2 - chi^2/2 - chi^2/2 = 0; ...) and to all orders (|e^{i chi}| = 1). The relative-k_T distribution itself is changed.

(G-iii) For finite-energy spectators at one loop, the k+ (and k-) contour of the spectator-spectator exchange is trapped in the Glauber region, between the s_B pole (lower half-plane) and the b pole (upper half-plane), both at |k+| ~ lambda^2 Q. It cannot be removed by contour deformation.

(G-iv) At one loop, the exchange between the B-active parton b and the A-spectator is not trapped in k+:
 I_as(k-) = int dk+ [(2p_b^- k^+ + c_b + i0)(2k^+k^- - K^2 + i0)]^{-1} = 2 pi i theta(-k^-)/(2 p_b^- K^2 + 2 k^- c_b), with K^2 = k_T^2 + m^2.
- The integral is saturated by the boson pole at k^+ = -K^2/(2|k^-|), i.e. |k^+| ~ Q.
- Replacing b by the eikonal line 1/(2p_b^- k^+ + i0) changes it by the relative amount k^- c_b/(p_b^- K^2) = O(lambda^2).
- The +i0 is the Feynman rule i/(n_B.k + i0) of the past-pointing Wilson line W[0,-inf n_B] in f_{q/A}. At leading power the exchange is therefore an A-collinear contribution to the A-PDF with a past-pointing line.

Plus-prescription remark. Use D_k = [ln^k(1-z)/(1-z)]_+ and the product convention g D_k = g(1) D_k + (g - g(1)) ln^k(1-z)/(1-z). Then
 (1+z^2) D_1 = [(1+z^2) ln(1-z)/(1-z)]_+ + (7/4) delta(1-z), because -int_0^1 (1+z) ln(1-z) dz = 7/4.
Hence 4C_F(1+z^2)D_1 + C_F(2pi^2/3 - 8) delta(1-z) = 4C_F[(1+z^2)ln(1-z)/(1-z)]_+ + C_F(2pi^2/3 - 1) delta(1-z).
(The version without the logarithm, '[(1+z^2)/(1-z)]_+', is false.)

**Literature check:** Yes; novelty is correctly not claimed.
- J. Collins, Foundations of Perturbative QCD (2011; open-access reissue 2023, DOI 10.1017/9781009401845): §14.3 (Glauber region example: k± integrals closed on final-state spectator poles, eqs. (14.11)-(14.13); cancellation after the sum over cuts, eqs. (14.14)-(14.16), valid only for the inclusive cross section).
- Same book: §14.3.3 (a Glauber pinch needs an exchange attached to both spectator parts) and §14.3.4 (an attachment to an active parton gives no Glauber pinch, so the contour can be deformed out).
- Same book: §14.4.1 item 5 (in DY the eikonal denominators are past-pointing Wilson lines).
- G. Bodwin, PRD 31 (1985) 2616 [Bodwin:1984hc], all-order spectator treatment; superseded, per Collins, by Collins-Soper-Sterman, NPB 308 (1988) 833.
- chi(b) is the classical eikonal phase -int V dz of a Yukawa potential.
- The plus-prescription identity is an elementary distribution identity.

## N26 — new_result — **confirmed**

**Claim:** The eikonal identity for Wilson lines is exact at finite ε only with the adiabatic regulator e^{−ε|t|}, not with a uniform +iε. Novelty not claimed.

**Printable version:** Abelian (or colour-symmetrised) eikonal identity:
 sum_{pi in S_m} prod_{j=1}^m i/(n.(k_{pi(1)}+...+k_{pi(j)}) + i eta_{pi,j}) = prod_j i/(n.k_j + i eps_j).
At finite regulator this holds exactly if and only if each cumulative regulator eta_{pi,j} is the sum of the regulators of the gluons absorbed so far (additivity).

Damping every field insertion on a semi-infinite Wilson line by e^{-eps|t|} (adiabatic switching; t = affine distance from the finite end) realises this with eta = j eps (past-pointing) and (m-j+1) eps (future-pointing). The identity is then exact at finite eps; unequal dampings eps_k per gluon also work.

With a uniform +i eps in every eikonal denominator (as from eikonalised Feynman propagators, or the naive delta-regulator) the identity fails at O(eps). For m = 2 the defect is
 -i eps/[(a1 + i eps)(a2 + i eps)(a1 + a2 + i eps)], with a_j = n.k_j.
It vanishes only as a distribution when eps -> 0; for example, its pairing with 1/((1+a1^2)(1+a2^2)) equals pi^2 eps/((1+eps)^2(2+eps)). The uniform prescription is equivalent to damping only the farthest attachment, which is not a regulator of the Wilson-line operator. Novelty not claimed.

**Literature check:** Yes. M. G. Echevarria, I. Scimemi, A. Vladimirov, PRD 93 (2016) 054004, arXiv:1511.05590 [Echevarria:2015byo], eqs. (5)-(6) and the accompanying text: the operator-level regulator e^{-delta sigma} gives cumulative denominators 1/((k1^+ - i delta)(k2^+ - 2i delta)...(kn^+ - n i delta)) and preserves exponentiation, while the naive delta-regularization (i0 replaced by i delta in every eikonal propagator) violates exponentiation (C_F^2 terms in the exponent at NNLO). The abelian eikonal identity itself, proved by splitting the product of line integrals into simplices, is classical.

## N27 — new_result — **confirmed**

**Claim:** Distributional verification that the one-loop MS-bar and ratio quasi-PDF kernels are the Fourier transforms of the coordinate kernels, for both γ^0 and γ^z (1e−9 to 1e−12). Ji's momentum-RGE −(3/2)δ follows from the MS-bar kernel.

**Printable version:** The one-loop momentum-space quasi-PDF matching kernels of Izubuchi-Ji-Jin-Stewart-Zhao (arXiv:1801.03917 = PRD 98 (2018) 056004), in the MS-bar scheme (eqs. (68), (69)) and in the ratio scheme (eqs. (70), (71)), with the delta-functions at xi = ±inf dropped, are exactly the Fourier transforms (their eq. (34)) of the coordinate-space kernel C(alpha, z^2 mu^2) of eqs. (62), (63) and of C - delta(1-alpha) C_0, respectively, for both Gamma = gamma^0 and gamma^z.

This holds as distributions on test functions that decay at infinity, including test functions that do not vanish at xi = 1 and decay only like a power. The key identity is FT[ln zeta^2] = -2 gamma_E delta(u) - [1/|u|]_reg (their eq. (59), up to delta-functions at ±inf).

Numerical verification:
- Project script: 20 Gaussian test-function pairings agree to 1.9e-12 - 7.9e-9.
- Independent stage-2 checks agree pointwise in zeta (<C, e^{-i xi zeta}> vs the coordinate side) to 5e-22, and pointwise in xi != 1 to 7e-21.

Consequence: with ell_p = ln(mu^2/4p_z^2),
 P^z dC^MS/dP^z = (alpha_s C_F/pi)[((1+xi^2)/(1-xi))_+ - (3/2) delta(1-xi)].
This is the momentum RGE of Ji, Liu, Liu, Zhang, Zhao, Rev. Mod. Phys. 93 (2021) 035005 [Ji:2020ect], eq. (32) (derived there with a transverse-momentum cutoff). In the ratio scheme the -(3/2) delta term is absent. This is a numerical confirmation, not a new result.

**Literature check:** Yes. Izubuchi, Ji, Jin, Stewart, Zhao, PRD 98 (2018) 056004 [Izubuchi:2018srq]: the momentum kernels (65), (68), (70) were derived from the coordinate kernel (62) by this Fourier transform (eq. (34); text after (69); eq. (70) obtained from (65) using eqs. (37), (59)). Ratio kernel also in Radyushkin, PRD 98 (2018) 014019 [Radyushkin:2018cvn], eq. (17); the reduced-ITD concept is from Radyushkin:2017cyf. The momentum RGE is Ji et al., RMP 93 (2021) 035005 [Ji:2020ect], eq. (32), not Ji:2020brr.

## N28 — new_result — **confirmed**

**Claim:** OTHERS checked transcriptions (not novel). BNS SLL tower: ₂F₂(1,1;2,5/2;−w), first term (4/(15π²))C_FN_cα_s⁴L⁵ΔYσ̂_B. LDL series: (L̂²/2)₂F₂(1,1;3/2,2;−C_Fα_sL̂²/(8π)). LUXqed point-like limit = Frixione eq. (4.189), xf_γ = (α/2π)[1+(1−x)²][ln(μ²/m²) − 2ln x − 1] + αm²x²(1−x)/(πμ²). CRS Yukawa PDF. BK eigenvalue χ(½) = 4ln 2.

**Printable version:** Checked transcriptions (not new results):

(i) Becher-Neubert-Shao, PRL 127 (2021) 212002, eqs. (14), (19), (21). For singlet exchange in forward kinematics (J_2 = J_43/2 = DeltaY), sum_n sigma_n^SLL = -sigma_B (4C_F/3pi) alpha_s^3 L^3 DeltaY 2F2(1,1;2,5/2;-w), with w = N_c alpha_s L^2/pi. The first super-leading (four-loop, n = 1) term is +(4/(15 pi^2)) C_F N_c alpha_s^4 L^5 DeltaY sigma_B; the n = 0 term is single-logarithmic. Asymptotically 2F2 ~ (3/2)(ln w - psi(3/2))/w.

(ii) Liu-Neubert, JHEP 04 (2020) 033, eq. (2.3) [arXiv:1912.08818 eq. (3)]: M_0 Lhat^2 sum_n n!/(2n+2)! (-C_F alpha_s Lhat^2/2pi)^n = M_0 (Lhat^2/2) 2F2(1,1;3/2,2;-C_F alpha_s Lhat^2/(8pi)). Its n = 0, 1 terms Lhat^2/2 and (C_F alpha_s/4pi)(-Lhat^4/12) are the leading logarithms of the NLO amplitude, JHEP eq. (2.1) [arXiv eq. (1)].

(iii) The LUXqed formula, Manohar-Nason-Salam-Zanderighi PRL 117 (2016) 242002 eq. (6), evaluated for a point-like Dirac fermion of mass m (G_E = G_M = 1, fixed alpha) gives
 x f_gamma = (alpha/2pi)[1+(1-x)^2][ln(mu^2/m^2) - 2 ln x - 1] + alpha m^2 x^2 (1-x)/(pi mu^2).
Its leading-power part equals x (alpha/2pi) Gamma^[1]_{gamma/e}(x, mu^2) of S. Frixione, JHEP 11 (2019) 158, eq. (4.189), in MS-bar (K_{gamma e} = 0). Dropping F_L would shift it by (alpha/2pi) 4(1-x), and dropping the MS-bar conversion term by (alpha/2pi) x^2.

(iv) Collins-Rogers-Sato, PRD 105 (2022) 076010, eqs. (55)-(59): in the Yukawa model
 f_{q/p}(xi; mu) = a_lambda(mu)(1-xi)[ln(mu^2/Delta) - 1 + (m_q + xi m_p)^2/Delta] + O(a_lambda^2),
 Delta = xi m_s^2 + (1-xi) m_q^2 - xi(1-xi) m_p^2.
For each xi it is negative at small mu and positive at large mu. For m_q = 0.3, m_p = 1.0, m_s = 1.5 GeV it is negative on (0.264, 1) at mu = 0.8 GeV and positive for all xi at mu = 2.5 GeV; the xi -> 1 sign change is at mu* = m_s exp{[1 - (m_q+m_p)^2/m_s^2]/2} = 1.70 GeV.

(v) The linearised LO BK kernel acting on (r^2)^gamma has eigenvalue alpha_bar chi(gamma), chi = 2psi(1) - psi(gamma) - psi(1-gamma), so chi(1/2) = 4 ln 2.

**Literature check:** Yes, these are transcriptions:
- Becher:2021zkk, PRL 127 (2021) 212002, eqs. (14), (19), (21).
- Liu:2019oav, JHEP 04 (2020) 033, eqs. (2.1), (2.3) (arXiv eqs. (1), (3)); LDL series originally from Kotsky-Yakovlev and Akhoury-Wang-Yakovlev.
- Manohar:2016nzj, PRL 117 (2016) 242002, eq. (6).
- Frixione:2019lga, JHEP 11 (2019) 158, eq. (4.189) (single author).
- Collins:2021vke, PRD 105 (2022) 076010, eqs. (55)-(59).
- Balitsky:2007feb, PRD 77 (2008) 014019, arXiv eq. (108); chi(1/2) = 4 ln 2 is the classic LO BFKL intercept.

## N29 — new_result — **confirmed**

**Claim:** YZLIU derived cross-checks (not claimed novel). H = C_HL^+C_HL^- with C_HL^± = 1 + (α_sC_F/8π)(−4 − 5π²/6 + 2L_± − L_±²). c_H ≈ 0.0725C_F² − 0.0840C_FC_A + 0.1453C_Fn_fT_F (closed form in CLAIMS.md). γ̃_J^(2) = C_FC_A(−1396/27 + 23π²/9 + 20ζ_3) + C_Fn_f(232/27 − 2π²/9), in (α_s/4π)². N_m = C_Fe^{5/6}/π ≈ 0.977. 𝒟_1 = (𝒟 + 𝒟_2)/2.

**Printable version:** Cross-checks of published formulas of the Liu programme (not claimed novel):

(i) At O(alpha_s), H = C_HL^+ C_HL^-, with C_HL^± = 1 + (alpha_s C_F/8pi)(-4 - 5pi^2/6 + 2L_± - L_±^2) and L_± = L_z ± i pi. Hence H = 1 + (alpha_s C_F/2pi)(-2 + pi^2/12 - L_z^2/2 + L_z) [Ji-Liu-Su, JHEP 08 (2023) 037, eq. (4.12) = arXiv:2305.04416 eq. (4.11)], which equals the Ebert-Stewart-Zhao form (alpha_s C_F/4pi)(-L^2 + 2L - 4 + pi^2/6). Also (C_HL^±)^2 = H^±_LFWF (JLS eq. (4.2)) and G^(1) = (alpha_s C_F/pi)(1 - ln(zeta_z/mu^2)).

(ii) The constant in ln H at O(alpha_s^2), with c_H in units of alpha_s^2 (JLS eq. (5.11)):
 c_H = (241 zeta3/(144pi^2) + 11pi^2/320 - 559/1728 - 971/(324pi^2)) C_F C_A + (-45 zeta3 - 2pi^4 + 30pi^2 - 30)/(24pi^2) C_F^2 + (36 zeta3 + 51pi^2 + 1312)/(1296pi^2) C_F n_f T_F
 = 0.0725 C_F^2 - 0.0840 C_F C_A + 0.1453 C_F n_f T_F (eq. (5.12)).
Its n_f part agrees with the large-beta0 result of Liu-Su, JHEP 02 (2024) 204, eq. (2.42).

(iii) In units of (alpha_s/4pi)^2, gamma~_J^(2) = 2gamma_HL - 2gamma_s = C_F C_A(-1396/27 + 23pi^2/9 + 20 zeta3) + C_F n_f(232/27 - 2pi^2/9). This follows from JLS (A.4), (A.5), (A.10); it is printed in JHEP eq. (3.12) [arXiv eq. (3.13)] and equals -gamma_1 of Jain-Scimemi-Stewart, PRD 77 (2008) 094008.

(iv) In the large-beta0 limit, N_m = C_F e^{5/6}/pi = 0.977 (Liu-Su eq. (2.50)). This is the pole-mass/linear-divergence renormalon normalisation; the values beyond large beta0 in Liu-Su eq. (2.52) are conjectural.

(v) From S_I = S_2/(S_1 S_1) = e^{-D} (Ji-Liu-Liu, NPB 955 (2020) 115054, eqs. (19)-(21)): D = 2D_1 - D_2, i.e. D_1 = (D + D_2)/2.

**Literature check:** Yes, these are cross-checks of published formulas:
- Ji:2023pba, JHEP 08 (2023) 037: (4.2), (4.12) [arXiv (4.11)], (3.12) [arXiv (3.13)], (5.11), (5.12), (A.1)-(A.13).
- Liu:2023onm, JHEP 02 (2024) 204: (2.41), (2.42), (2.46), (2.47), (2.50); (2.52) contains only the conjectured values.
- Ji:2019sxk, NPB 955 (2020) 115054: text after eq. (21).
- Ebert:2018gzl, PRD 99 (2019) 034505, eq. (25).
- Jain:2008gb, PRD 77 (2008) 094008 (gamma_1).
- Liu:2023pjb, JHEP 09 (2024) 030, eq. (C.1).
- Liu:2024omb, JHEP 09 (2024) 093, eqs. (4.2)-(4.5).

## R-S1 — correction_of_reference_doc — **confirmed**

**Claim:** Reference pp. 57-61, 85 and App E: the claim that the non-abelian two-Glauber exchange leaves a residual −¼C_Aχ²T_A·T_B (basis of the B′ grade for DY) is false. The exact eikonal box and crossed box give Re p_opp = 0, so the residual −½C_Aχ²(Re p_opp)X vanishes. The C_A term is the one-loop reggeization phase, and V†V = 1 + O(χ³) without real emission (see N01). (E.51) on p. 217 confirms ¼C_A; reader R4's −1/8 is a slip.

**Printable version:** In the reference's own eikonal-spectator model (Lemma 9.2 / Lemma E.48(d), elastic kinematics K^+- = 0), its residual is an artefact of the strict instantaneous Glauber approximation with independent symmetric cut-offs in k^+ and k^-. That regularization gives equal ordering weights, p_opp = 1/2, and the residual V^dag V - 1 = -1/4 C_A chi^2 T_A.T_B ((E.51), p. 217, arithmetically correct; reader R4's -1/8 C_A chi^2 X is the amplitude-level deviation, not this residual).

The same box and crossed box, evaluated exactly, give a different result. Take two infinite time-like Wilson lines with rapidity difference Y, exact gluon propagators of mass m, fixed transverse momenta, a = k_T^2 + m^2 and b = (K-k)_T^2 + m^2, and the normalization J_sigma = Int dx_A dx_B [i/(x_A+i0)][i/(sigma x_B+i0)]/((k_par^2 - a + i0)(k_par^2 - b + i0)). Then J_box = (2 pi/(ab))(pi + iY) and J_cross = -2 pi i Y/(ab). Hence p_opp = J_cross/(J_box + J_cross) = -iY/pi, Re p_opp = 0, and the residual -1/2 C_A chi^2 (Re p_opp) X of (E.36) vanishes.

In b space the two-exchange amplitude is A2 = 1/2(-i chi)^2 X^2 + i(C_A Y/(4 pi)) chi^2 X. Its C_A term is anti-Hermitian: it is the one-loop reggeization of the exchanged gluon (Regge trajectory omega(t) Y), not a unitarity violation. So (1 + A1 + A2)^dag (1 + A1 + A2) = 1 + O(chi^3) within these graphs. No real emission is needed: for straight infinite lines, real cuts first appear at O(g^6), and the remaining O(g^4) virtual graphs are a real multiple of the tree.

The reference's statements are therefore false in its own model: that the residual 'does not cancel within these graphs', that it can only cancel with Glauber-soft mixing and real emission, and that within G0 it 'should not be expected to vanish'. The cancellation for non-eikonal spectators and active partons (Ass. E.33(c) in general), together with E.34 and E.44, remains open.

**Literature check:** Yes, the computation is known:
- Meggiolaro, Z. Phys. C 76 (1997) 523 [hep-th/9602104], eq. (3.26): for ladder plus cross, the G1 = X coefficient is i(N_c g^4/4pi) I(t) chi coth^2 chi and the G2 = X^2 coefficient is -1/2 g^4 I(t) coth^2 chi, which is exactly p_opp = -i chi/pi. His eq. (3.36) gives the Regge form (2s/t)[1 - alpha(t) ln s], and eqs. (3.28)-(3.34) give the other O(g^4) graphs as a real multiple of the tree.
- Giordano-Meggiolaro, PRD 74 (2006) 016003, eq. (4.24), give the same graph by graph.
- Rothstein-Stewart, JHEP 08 (2016) 025, sec. 9, eqs. (9.1), (9.18), (9.19): with their rapidity regulator the crossed Glauber rungs vanish and the boxes exponentiate to e^{i phi} with Hermitian phi. That is regulator-dependent but also unitary. Their sec. 7.2 obtains reggeization from rapidity renormalization.
- Caron-Huot, JHEP 05 (2015) 093, treats reggeization in the eikonal approach.

Only the remark that the uncitable reference's strict-window residual is a truncation artefact is ours.

## R-S2 — correction_of_reference_doc — **confirmed**

**Claim:** Reference p. 74: η_bT_b + η_cT_c + η_dT_d reduces to −η_bT_a, which would predict no Sivers flip. Correct, with all-outgoing charges: the Glauber part is ∝ T_b − T_c − T_d = T_a + 2T_b; SIDIS gives +T_a, DY −T_a; P = −T_a − 2T_b.

**Printable version:** On p. 74 the reference writes the Glauber part of a spectator gluon's eikonal coupling to partons j in {b, c, d} as -i pi Sum_j eta_j T_j delta(n_j.k), with eta = +1 for initial and -1 for final partons, and uses in = out colour conservation T_a + T_b = T_c + T_d. With eta_c = eta_d = -eta_b this reduces to -eta_b T_a. That bookkeeping would make the phase absorbable into a Wilson line for parton a (no TMD-factorization breaking) and would give the same sign in SIDIS and DY (no Sivers sign flip).

The error is the dropped relative minus sign of final-state eikonal factors. For k flowing into line j, incoming lines give +T_j/(n.k + i0) and outgoing lines give -T_j/(n.k - i0). So in the in = out convention the delta-parts of initial and final lines have the same sign, and the pole part is P = -(T_b + T_c + T_d) = -T_a - 2T_b (coefficient of +i pi delta). Equivalently, with all-outgoing charges (Sum_j T_j = 0; initial lines 1/(n.k + i0), final lines 1/(n.k - i0)) the Glauber part is proportional to T_b - T_c - T_d = T_a + 2T_b. This is irreducible.

SIDIS gives +T_a and DY gives -T_a, which is the Sivers sign flip. The abelian analogue reproduces Collins-Qiu's i pi(g1 + 2g2) delta(l^+), eqs. (4.1)-(4.3). The gluonic-pole strength is C_G = 1 + 2<T_a.T_b>/C_F.

**Literature check:** The correct physics is known:
- Collins-Qiu, PRD 75 (2007) 114014, eqs. (4.1)-(4.3): i pi(g1 + 2g2) delta(l^+).
- The Sivers sign flip: Collins, PLB 536 (2002) 43.
- Gluonic-pole colour factors: Bacchetta-Bomhof-Mulders-Pijlman 2005; Qiu-Vogelsang-Yuan 2007.

The correction of the (uncitable) reference document is ours.

## R-S3 — correction_of_reference_doc — **confirmed**

**Claim:** Reference p. 198, Ass E.33(c1) (a fixed localization order) is generically false. The equal-time limit is w_12O_2O_1 + w_21O_1O_2, w_12 = z_1/(z_1+z_2), so a fixed order errs by w_21[O_1,O_2] = O(1). Replace by the ordering-weight lemma (N13).

**Printable version:** Ass. E.33(c1) of the reference (p. 198) is generically false. It postulates a fixed localization order for non-commuting equal-time insertions on one spectator parton such that per-graph weak equivalence (E.35) holds.

As the reference's own analysis (pp. 195-196) shows, joint localization of two insertions is a weighted sum, w12 O2O1 + w21 O1O2. When the external factors have single poles z_j = kT_j^2/(2k_j^+) in the same half-plane, w12 = z1/(z1+z2) = k2^+ kT1^2/(k1^+ kT2^2 + k2^+ kT1^2), the weight of O2O1 (O2 later). The weights are 0 and 1 when k1^+ k2^+ < 0. For N insertions, the time order pi(1) < ... < pi(N) has weight prod_j z_j / prod_{m=1}^N Sum_{l>=m} z_pi(l), and the weights sum to 1.

A fixed order O2O1 therefore errs by w21[O1,O2], which is O(1). The weight w21 ranges over (0,1) as k1^+/k2^+ varies, and for two SS lines on one pair of spectators the colour of the commutator term is proportional to C_A T_A.T_B.

(c1) should be replaced by an ordering-weight lemma, with weights that are piecewise and non-analytic at k_j^+ = 0. Only the complete-set statement (c2) should be kept as an assumption.

**Literature check:** The weight formula is elementary: ordered integrals of exponentials, i.e. sequential energy denominators as in time-ordered perturbation theory. It is also stated in the reference itself (pp. 195-196). I know of no published treatment of the correction of (c1); the reference is not citable.

## R-S4 — correction_of_reference_doc — **confirmed**

**Claim:** Reference pp. 19, 22: the super-leading configurations (n_F,n_T) = (0,0) (p_J = −2) and (0,1) (p_J = −1) are omitted. They cancel in gauge-invariant sums (CSS 1989 §8.6) [A], and their remainders build F^{+j}.

**Printable version:** By the reference's power-counting formula (3.8), p_J = n_F + n_T + 2n_- - c_J, with c_J = 2 for the DIS forward amplitude, the configurations (n_F, n_T) = (0,0) (p_J = -2) and (0,1) (p_J = -1) are super-leading. Consequently, 'all other combinations are suppressed by at least lambda' (Cor 3.8, p. 19) and 'p(R) >= 0' (Thm 3.12, p. 22) are false as power-counting statements.

The reference dismisses (0,0) in one sentence, without remainder analysis, and never mentions (0,1). (0,1) is not removed by rotational symmetry: J^{j+...} proportional to k_T^j, combined with the O(lambda) k_T-dependence of H, is leading.

These configurations cancel only in gauge-invariant sums, by Ward identities and colour neutrality (CSS 1989 sec. 8.6) [A]. Their O(lambda) and O(lambda^2) remainders are leading and build the field strength F^{+j} = d^+A^j - d^jA^+ + .... For a single active gluon, k.H = 0 and the G term proportional to k^+A^j - k^jA^+ is leading. So 'n_T transverse gluons' is not a gauge-invariant bookkeeping in the gluon channel.

**Literature check:** Yes, the physics is known:
- Collins-Soper-Sterman, Adv. Ser. Direct. HEP 5 (1989) 1 [hep-ph/0409313], sec. 8.6 (Feynman-gauge power counting holds only for gauge-invariant sets; individual graphs are more divergent) and sec. 8.1 (field strengths).
- The F^{+j} form of the gluon distribution: Collins-Soper, NPB 194 (1982) 445; Collins 2011, Foundations of perturbative QCD.

The correction of the reference is ours.

## R-M1 — correction_of_reference_doc — **confirmed**

**Claim:** p. 15: 'no Euclidean pinch' is false, because zero-momentum massless lines solve Landau. They are IR convergent (degree A + ½A_q ≥ 2).

**Printable version:** Cor 3.4 of the reference ('no pinch in the Euclidean region', p. 15) is false as stated, and its proof errs in requiring the lines adjacent to a zero-momentum line to be on shell.

For any external kinematics, a massless line carrying zero momentum (alpha_j > 0, all other alpha = 0, adjacent lines off shell) solves the Landau equations (3.2). In parameter space, the three simplex corners of the triangle (3.3), with F = m^2 a0(a1+a2) + Q^2 a1 a2, are solutions for all m^2 and Q^2.

In the Euclidean non-exceptional region these zero-momentum configurations are the only Landau solutions; with massive lines F > 0 and there are none. They are IR convergent by power counting. The IR degree of a soft subgraph is omega = 4L_S - 2N_g - N_q + V_3 = A + 1/2 A_q >= 2, where A is the number of soft-line attachments to the hard part and A_q the number of those that are quarks. Hence the Feynman integral is still analytic there (Lowenstein-Zimmermann).

**Literature check:** Yes:
- Collins, arXiv:2007.04085, App. D.1: pinches at zero-momentum massless lines exist for all external p, without a singularity of the integral.
- Lowenstein-Zimmermann, Commun. Math. Phys. 44 (1975) 73-86: IR power-counting convergence for massless propagators.

The correction of the reference is ours.

## R-M2 — correction_of_reference_doc — **confirmed**

**Claim:** pp. 16-17, Prop 3.5: the kinematics is not Euclidean and π²/3 is omitted. Correct: Q²I = L² + π²/3 + t(2L² − 4L − 4 + 2π²/3), t = m²/Q², L = ln(Q²/m²) [P].

**Printable version:** The kinematics of the reference's (3.3), p1^2 = p2^2 = -m^2 and (p1+p2)^2 = -Q^2 with Q >> m, is not realizable with real Euclidean momenta, which would force Q^2 <= 4m^2. It is a spacelike Minkowski configuration with all invariants negative, and its collinear regions exist only because of the Minkowski signature.

Prop 3.5 gives only Q^2 I = ln^2(Q^2/m^2) + O(ln^0) and does not determine the constant. Exactly, Q^2 I = Phi^(1)(t,t) (Usyukina-Davydychev), and
Q^2 I = L^2 + pi^2/3 + t(2L^2 - 4L - 4 + 2pi^2/3) + O(t^2 L^2), with t = m^2/Q^2 and L = ln(Q^2/m^2).
The next term is t^2(6L^2 - 14L - 11 + 2pi^2).

The sum of the hard, two collinear and soft region integrals in dimensional regularization reproduces L^2 + pi^2/3 at leading power. This is verified at one loop [P].

**Literature check:** Yes:
- The closed form: Usyukina-Davydychev, PLB 298 (1993) 363 (Phi^(1)).
- The leading-power constant pi^2/3 also appears in the reference's own App. D (D.32) and Table 5.
- The method of regions for the off-shell Sudakov form factor is a standard example (Smirnov, Applied Asymptotic Expansions).

The NLP coefficient is a direct expansion of the known closed form. The correction of the reference is ours.

## R-M3 — correction_of_reference_doc — **confirmed**

**Claim:** pp. 14-15: parameter-space and momentum-space pinch theorems are conflated (they differ for massless graphs), and second-type singularities are ignored. Give two theorems with two proofs.

**Printable version:** The reference's Thm 3.1 (pp. 14-15, proved in App. A with Feynman parameters) gives a necessary condition for singularities of I(p) in the external momenta. The same text uses its conditions (3.2) as the criterion for momentum-space trapping, i.e. pinch surfaces and reduced diagrams. These are distinct theorems with distinct proofs. For massless graphs a momentum-space pinch need not be a parameter-space pinch: the one-loop massless self-energy has a collinear momentum pinch at p^2 = 0 with no pinch in the pure parameter integral, and it has zero-momentum pinches for all p (Collins 2020, App. D.1).

The statement 'endpoints do not occur; infinity is a UV problem' also ignores second-type singularities (U = 0, pinch at infinity). These are not UV divergences.

One should state and prove separately:
(A) the alpha-space analyticity theorem: singularities of I(p) lie on the first-type Landau varieties of the graph and its reduced graphs, or on second-type varieties;
(B) the momentum-space trapping criterion: at fixed p the contour is trapped at a real point iff a Landau point exists for the first derivatives of the vanishing denominators. This is Collins 2020, Thms 1-3, a Gordan-type alternative, and it is valid also with Wilson-line denominators.

**Literature check:** Yes:
- Collins, arXiv:2007.04085 (2020), Theorems 1-3 and App. D.1.
- Second-type singularities: Fairlie, Landshoff, Nuttall, Polkinghorne (1962); Eden, Landshoff, Olive, Polkinghorne, The Analytic S-Matrix.

The correction of the reference is ours.

## R-M4 — correction_of_reference_doc — **confirmed**

**Claim:** p. 11, Fig 4: the Wilson-line rules are ambiguous. Correct: vertex igt^av^μ; past line Π i/(n·(k_1+…+k_j) + i0); future line Π (−i)/(n·(k_j+…+k_m) − i0).

**Printable version:** The Wilson-line rules of the reference's Fig. 4 (p. 11) are ambiguous and inconsistent with its own definition (2.7). Fig. 4 says 'vertex igv^mu t^a, propagator i/(v.k +- i0), + = future, - = past'. It gives no momentum routing, does not distinguish W from W^dag, and gives no multi-gluon partial sums.

From (2.7), W_v^(+-)(x) = W[x, x +- inf v]. For a gluon momentum k flowing into the line, the one-gluon rule is igv^mu t^a x i/(v.k - i0) for the future line and igv^mu t^a x i/(v.k + i0) for the past line, the opposite of Fig. 4's assignment. Fig. 4's own last row (incoming quark absorbing k: -g p^mu/(p.k + i0) = igp^mu t^a x i/(p.k + i0)) puts +i0 on a past-type line.

Correct rules, with D = d - igA, W[b,a] = P exp(ig Int_a^b dz.A), gluon momenta k_j flowing into the line and numbered along the path orientation, and colour matrices path-ordered with later points on the left. Each vertex is ig t^{a_j} n^{mu_j}.
- Past line W[0,-inf n]: prod_{j=1}^m i/(n.(k_1+...+k_j) + i0).
- Future line W[inf n,0]: prod_{j=1}^m (-i)/(n.(k_j+...+k_m) - i0).
Equivalently: propagator i/(n.l + i0), with l the momentum along the path orientation.

**Literature check:** Yes, these are the standard eikonal Feynman rules: e.g. Collins 2011, Foundations of perturbative QCD, Fig. 7.10 as corrected in the author's errata, with the opposite sign convention for g. The correction of the reference is ours.

## R-M5 — correction_of_reference_doc — **confirmed**

**Claim:** pp. 23-25: the K-projection lacks an i0. Correct: DIS K_μν = k_μw_2ν/(k·w_2 − i0) (future); DY +i0 (past).

**Printable version:** The collinear K-projection of the reference ((3.10), used in Thm 3.14), K^mu_nu = khat^mu nbar_nu/(nbar.k), carries no i0. The pure-gauge argument of Thm 3.14 cannot supply it: it yields +i0 (a past-pointing line) only because U in (3.14) is based at -infinity, which Rem 3.15 admits is arbitrary.

With k flowing from the collinear subgraph into H, the i0 is inherited from the propagators that the eikonal factors replace:
- DIS, where the K gluons end on the final-state struck quark: K_mu nu = k_mu w_2nu/(k.w_2 - i0), with w_2 projecting onto k^+. This is a future-pointing Wilson line (Collins 2011, eq. (11.6), as listed in his errata).
- Drell-Yan, where they end on the incoming parton from the other hadron: +i0, a past-pointing line. The direction is established only after the Glauber contour analysis.

For collinear PDFs the choice is immaterial after the k^+ integral; for TMDs and for the Glauber analysis it is essential.

**Literature check:** Yes: Collins, Foundations of perturbative QCD (CUP 2011; OA reissue doi:10.1017/9781009401845), eq. (11.6), as reproduced in the author's errata of 22 May 2026 (p. 402 item, where only the index placement is corrected): K = k w_2/(k.w_2 - i0), with k_j flowing into H. The past-pointing DY lines are in Collins 2011, ch. 14. The correction of the reference is ours.

## R-M6 — correction_of_reference_doc — **confirmed**

**Claim:** pp. 23-25, Thm 3.14 is overclaimed: the abelian/tree identity is [R], the all-order non-abelian statement [A].

**Printable version:** Thm 3.14 of the reference (pp. 23-25) is stated for a general colour-singlet hard subgraph H with n longitudinal collinear gluons. It is proven there only for H built of quark lines with colour-singlet vertices (tree level), by the telescoping identity (3.15). For H with internal gluon lines, the required Slavnov-Taylor (ghost) step is cited, not proven; the reference's own App. D keeps the Ward identity for modified integrands as an assumption (Ass. D.37). Gluon-initiated H is not covered by its statement.

Grade: the abelian / tree-level identity is [R]; the all-order non-abelian statement is [A].

**Literature check:** Graph-by-graph Ward identities for collinear gluons exist in sketched all-order form: Collins-Soper-Sterman 1989 sec. 9 [hep-ph/0409313]; Collins 2011, ch. 11. No complete published all-order non-abelian proof was identified; hence [A]. The grading correction of the reference is ours.

## R-M7 — correction_of_reference_doc — **confirmed**

**Claim:** p. 26: the soft factor contains a literal '⋯'. Define the operators precisely, with the inherited i0 (future for e⁺e⁻/DIS, past for DY).

**Printable version:** The soft factor (3.16) of the reference (p. 26), S = (1/N_c)<0|Tr W_nbar^dag W_n ... W_n^dag W_nbar|0>, contains a literal '...'. It leaves unspecified the positions of the lines, the time ordering (T vs anti-T), the sum over soft final states, and whether the lines point to the future or the past. The 'identical proof' of Cor 3.17 also ignores that the base point of the soft lines, the hard vertex, is physical.

The soft factor should be defined as a cut matrix element of path-ordered Wilson lines emanating from the hard vertex, S(k_tot) = Sum_{X_s} <0|(T prod_i W_{v_i})^dag|X_s><X_s|T prod_i W_{v_i}|0> delta^4(k_tot - p_{X_s}), as in the reference's own (8.2) and (E.48). The i0 of each line is inherited from the replaced jet propagators: future-pointing for final-state jets (e+e- annihilation, SIDIS), past-pointing for Drell-Yan.

**Literature check:** Yes, these are standard definitions:
- the reference's own (8.2) and (E.48);
- Collins, Foundations of perturbative QCD (2011), chs. 13-14 (future-pointing lines for e+e-/SIDIS, past-pointing for DY);
- Aybat-Rogers, PRD 83 (2011) 114042 (future SIDIS vs past DY lines).

The correction of the reference is ours.

## R-M8 — correction_of_reference_doc — **confirmed**

**Claim:** pp. 1, 7, 84: meson electroproduction factorizes for longitudinal photons only; γ*_T has endpoint divergences.

**Printable version:** The Collins–Frankfurt–Strikman theorem (PRD 56 (1997) 2982) proves leading-power factorization of hard exclusive meson electroproduction only for longitudinally polarized virtual photons (σ_L). For transverse photons the amplitude is suppressed by 1/Q, endpoint (soft-parton) regions are not power suppressed, and collinear factorization fails, with divergent endpoint integrals at twist 3 (Mankiewicz–Piller 2000). In the reference the qualifier is missing only on p. 1 (abstract) and p. 7 (Def. 1.1); p. 84 (Table 1) and Thm. 11.4 already say γ*_L.

**Literature check:** Yes: Collins–Frankfurt–Strikman, PRD 56 (1997) 2982 [Collins:1996fb], Sec. II and the section on transversely polarized photons; Mankiewicz–Piller, PRD 61 (2000) 074013 [Mankiewicz:1999tt].

## R-M9 — correction_of_reference_doc — **confirmed**

**Claim:** Quarkonium decay is graded A*; it should be [A]: Minkowskian, needs local duality.

**Printable version:** NRQCD factorization of inclusive annihilation decays of heavy quarkonium (Bodwin–Braaten–Lepage) holds as an all-order perturbative argument given in sketch form, with matching cutoff dependence of f_n(Λ) and ⟨O_n⟩_Λ: grade [A]. The decay rate is a Minkowskian quantity at the fixed scale 2M_Q, and energy smearing as in e+e- is unavailable (BBL §II.E). A non-perturbative statement therefore requires local quark–hadron duality, which is not among the Euclidean OPE/dispersion assumptions. It is not 'as rigorous as the OPE' (the reference's A*).

**Literature check:** Yes, the duality/smearing caveat is stated by BBL themselves: PRD 51 (1995) 1125 [Bodwin:1994jh], §II.E (erratum PRD 55 (1997) 5853 irrelevant here).

## R-M10 — correction_of_reference_doc — **confirmed**

**Claim:** pp. 36-37: one P_qq for all n is wrong beyond LO. P^±_NS differ: ∫P^{V(1)}_qq̄ = 0.71931C_F(C_F − C_A/2).

**Printable version:** Beyond LO the OPE anomalous dimensions of even-n (C-even) and odd-n (C-odd) twist-2 quark operators are moments of different kernels: P^±_NS = P^V_qq ± P^V_qq̄. At NLO, P^+ - P^- = 2P^{V(1)}_qq̄ with ∫_0^1 P^{V(1)}_qq̄ dx = (13/4 - 3ζ_2 + 2ζ_3) C_F(C_F - C_A/2) = 0.71931 C_F(C_F - C_A/2), normalization P = Σ_n (α_s/2π)^{n+1} P^(n); this is 2.87725 C_F(C_F - C_A/2) in a_s = α_s/4π. Even-n RG ⟺ DGLAP for the C-even set (q+q̄, g); odd-n ⟺ DGLAP for C-odd non-singlet q - q̄ with P^- (for the total valence, P^v_ns = P^- + P^s_ns from NNLO), with separate analytic continuations. A single P_qq for all n, as in reference Prop. 5.4, is valid only at LO.

**Literature check:** Yes: Curci–Furmanski–Petronzio, NPB 175 (1980) 27 [Curci:1980uw]; Moch–Vermaseren–Vogt, NPB 688 (2004) 101 [Moch:2004pa], eqs. (2.4), (4.6), (4.7). The numerical first moment follows from these; not new.

## R-M11 — correction_of_reference_doc — **confirmed**

**Claim:** p. 41: the two-rung ladder misses the all-hard region R_0; three regions are needed.

**Printable version:** For the two-rung ladder graph of the DIS forward amplitude the leading regions are R2 < R1 < R_H (both rungs collinear; only the lower rung collinear; all hard). The all-hard region R_H carries the two-loop hard coefficient, C_HΓ = ΔH0ΔK2K1(k1,p̂). Without it, Γ - Σ_R C_RΓ = C_HΓ + r is not power suppressed and the subtraction formula (6.4) is false. The reference's Fig. 24 lists only two regions, contradicting its own Ex. D.48.

**Literature check:** The region structure is standard (Collins, Foundations of pQCD, ch. 10, where the sum over regions includes the hard region) and appears in the reference's own Ex. D.48. The statement concerns the reference only.

## R-M12 — correction_of_reference_doc — **confirmed**

**Claim:** 'Combinatorics complete' is overclaimed: the regrouping into T̂⊗f is an input (Ass D.37).

**Printable version:** In the reference the combinatorial regrouping of the subtracted region terms into hard coefficient ⊗ parton distribution is not a completed proof but an input. For DIS it relies on the commutativity/absorption properties (Com)(Abs) of the approximators (reference Prop. D.42, Thm. D.46; (Com) is exact only with an adapted momentum routing). For the other processes it relies on the assumed product structure of Ward identities on approximated integrands (Ass. D.37 (W1)(W2), general-order proof not written). The statement '§6 fully executes the five steps; the combinatorial part is complete' (p. 39) therefore overclaims and must be replaced by an explicitly labelled assumption.

**Literature check:** Statement about the reference document only; supported by the reference's own App. D (Prop. D.42, Ass. D.37, Thm. D.46, Note D.24).

## R-M13 — correction_of_reference_doc — **confirmed**

**Claim:** p. 29: that the DR cut sum equals 12π Im Π is not shown. Use thm:ee-R-finite plus cor:ee-cuts [A] (N24).

**Printable version:** R(s) = 12π Im Π(s+i0) is IR finite at every order. The renormalized Euclidean Π is IR finite (Poggio–Quinn 1976; Lowenstein–Zimmermann; Breitenlohner–Maison), its ε-Laurent coefficients are polynomials in L = ln(Q²/μ²) whose pole parts vanish for all real L and hence identically, and so analytic continuation commutes with ε→0 ([R] in perturbation theory). The equality of R with the sum over D-dimensional partonic cuts (including ghosts and counterterms) follows from the cutting rules and unitarity and is graded [A]. The reference proves the first statement but only asserts the second.

**Literature check:** Yes for the finiteness route: Poggio–Quinn, PRD 14 (1976) 578 (theorem plus corollary on physical discontinuities). The cutting rules/unitarity are standard ('t Hooft–Veltman); a fully rigorous massless-DR treatment with ghosts is not available in one source.

## R-M14 — correction_of_reference_doc — **confirmed**

**Claim:** p. 47: the one-loop PDF check is incomplete (rapidity cancellation in [2ξ/(1−ξ)]_+, self-energy −½δ). Use prop:pdf-pqq-operator.

**Printable version:** The one-loop operator computation of f_{q/q} in Feynman gauge (massless on-shell quark, gluon-mass IR regulator) has these graph-by-graph UV-pole coefficients, in units (α_s/2π)C_F/ε. The ladder gives (1-ξ). The Wilson-line real graph and the virtual Wilson-line graph combine into [2ξ/(1-ξ)]_+; their ξ→1 (k⁺→0) endpoint divergence is regulated neither by DR nor by the gluon mass and cancels only in this combination. The external-leg self-energy gives -½δ(1-ξ) (δZ₂). The sum is P_qq/C_F = [(1+ξ²)/(1-ξ)]_+, and quark number holds exactly in ε. The MS-bar result is f^(1) = (α_s/2π){P_qq ln(μ²/m²) + C_F[-(1-ξ)(2+ln ξ) - [2ξ ln ξ/(1-ξ)]_+ + ¼δ(1-ξ)]}, with ∫_0^1 f^(1) = 0. The reference's Prop. 7.1 instead fixes the δ term by the sum rule.

**Literature check:** Standard one-loop computation (e.g. Collins, Foundations of pQCD, ch. 9, graph-by-graph). The specific gluon-mass finite part was re-derived here and agrees with research/c_pdf §3.5; it is regulator dependent and not a physical result.

## R-M15 — correction_of_reference_doc — **refuted**

**Claim:** p. 64, step (iv): with identical arguments the formula is rapidity divergent. Correct: f̃^unsub_A(y_{P_A}−y_B)f̃^unsub_B(y_A−y_{P_B})S̃(y_A,y_B)/[S̃(+∞,y_B)S̃(y_A,−∞)].

**Printable version:** 

**Literature check:** The correct identity f̃_A f̃_B = f̃^unsub_A(y_{P_A}-y_B) f̃^unsub_B(y_A-y_{P_B})/S̃(y_A,y_B) (any y_n; limit y_A→+∞, y_B→-∞ finite by equal slopes) is Collins, Foundations of pQCD, eq. (13.106) and surrounding text; it is also the reference's own Lemma D.38. If an editorial remark is wanted, print this identity, or equivalently ff·S̃(+∞,-∞)/[S̃(+∞,y_B)S̃(y_A,-∞)] with the ±∞ cancelling among the soft factors, instead of the ERR-M15 formula.

## R-M16 — correction_of_reference_doc — **confirmed**

**Claim:** W+Y 'uniformly O((Λ/Q)^a)' needs modified cutoffs near q_T ~ Q and q_T ~ Λ.

**Printable version:** In the standard CSS W+Y construction the error estimate O((m/Q)^c) holds only for m ≲ q_T ≲ Q. Uniform validity down to q_T → 0 requires suppressing Y at q_T ≲ m (a low-q_T cutoff X(q_T/λ); precursor: CSS 1985 Q_T^min). Validity at q_T ≳ Q requires modifying W (small-b cutoff b_c = √(b_T² + b_0²/(C_5Q)²)), as in Collins–Gamberg–Prokudin–Rogers–Sato–Wang, PRD 94 (2016) 034014. The unqualified claim 'W+Y is uniformly O((Λ/Q)^a)' must be qualified accordingly.

**Literature check:** Yes: J. Collins, L. Gamberg, A. Prokudin, T.C. Rogers, N. Sato, B. Wang, PRD 94 (2016) 034014, arXiv:1605.00671 [INSPIRE Collins:2016hqq] (verified; not yet in our bib).

## R-M17 — correction_of_reference_doc — **confirmed**

**Claim:** p. 71: the transverse-photon failure is a log divergence, since g_⊥^(v)(0) = ½∫φ_∥/u ≠ 0, plus double poles; the leading-twist γ*_T → V_T amplitude vanishes.

**Printable version:** For transversely polarized photons the leading-twist γ*_T → V_T hard-scattering amplitude vanishes to all orders, by angular-momentum and chirality conservation (Diehl–Gousset–Pire 1999, valid for any photon polarization; all-order proof completed by Collins–Diehl 2000). At twist 3, in the Wandzura–Wilczek approximation, the meson-side endpoint integrals diverge logarithmically, because the twist-3 DA g_⊥^(v)(u→0) = ½∫_0^1 du φ_∥(u)/u ≠ 0 (3/2 for φ_∥ = 6uū). This persists for any φ_∥ with ∫φ_∥/u ≠ 0, including endpoint-suppressed ones. In addition, the GPD convolution contains double poles (ξ∓x-i0)^{-2}, which produce further IR singularities, e.g. for the asymptotic singlet quark GPD (Mankiewicz–Piller 2000). Collinear factorization therefore fails for γ*_T.

**Literature check:** Yes: Mankiewicz–Piller, PRD 61 (2000) 074013 [Mankiewicz:1999tt]; Diehl–Gousset–Pire, PRD 59 (1999) 034023 [Diehl:1998pd]; Collins–Diehl, PRD 61 (2000) 114015 [INSPIRE Collins:1999un].

## R-M18 — correction_of_reference_doc — **confirmed**

**Claim:** p. 74: the CQ model is abelian. RM is a double-Sivers counterexample with Tr[t^at^b]Tr[t^bt^a] = T_F²(N_c²−1), against a prediction of 0. Collins 2007 is not cited.

**Printable version:** Collins–Qiu (PRD 75 (2007) 114014) disprove standard k_T factorization for pp → h1h2X in an abelian spectator model (massive gluon, couplings g1 ≠ g2). Rogers–Mulders (PRD 81 (2010) 094006) disprove generalized TMD factorization (arbitrary process-dependent Wilson lines per hadron) in an SU(N_c) spectator model with a colour-neutral hard exchange. Their counterexample is the anomalous two-gluon contribution (one gluon from each hadron's spectator) to a double-Sivers asymmetry, with colour factor Tr[t^at^b]Tr[t^bt^a] = T_F²(N_c²-1) ≠ 0, whereas generalized factorization with colour-traced Wilson loops predicts 0 (Tr[t^a] = 0). It is not a 'difference ∝ [t^a,t^b]'. Collins 2007 (arXiv:0708.4410) showed the failure of standard k_T factorization for the unpolarized cross section at two-gluon exchange; the reference does not cite it.

**Literature check:** Yes: Collins–Qiu PRD 75 (2007) 114014 [Collins:2007nk], Sec. II; Rogers–Mulders PRD 81 (2010) 094006 [Rogers:2010dm], eq. for the colour factor and its discussion of the abelian case; Collins arXiv:0708.4410 [Collins:2007jp].

## R-M19 — correction_of_reference_doc — **confirmed**

**Claim:** p. 76: the NQS Wilson lines are necessary at NNLO (uncancelled poles ∝ α_s²v²/ε), not inconsequential.

**Printable version:** Nayak–Qiu–Sterman (PLB 613 (2005) 45; PRD 72 (2005) 114012) analysed the NNLO (two-loop, eikonal) transition of a QQ̄ pair from colour octet to colour singlet in g → H fragmentation. They find a non-cancelling infrared pole Σ^(2) = α_s²(4/3ε)[(P·q)²/P⁴ − q²/P²]. In the pair rest frame this is α_s² v²/(12ε) + O(v⁴), with v the relative velocity, so the pole is NNLO and of relative order v².

The conventional octet production operators χ†K_nψ a_H†a_H ψ†K'_nχ do not reproduce this pole. Their gauge-completed version, with adjoint Wilson lines to infinity, generates it exactly. The Wilson lines are therefore necessary for NNLO factorization and do change the result.

The pole coefficient does not depend on the Wilson-line direction. The matching holds to all orders in v at NNLO (NQS PRD 74 (2006) 074007), still with the gauge-completed operators. Beyond NNLO, absent special cancellations, further non-local operators may be needed.

**Literature check:** Yes. NQS PLB 613 (2005) 45 [hep-ph/0501235] (abstract, eqs. (gn),(gn1)); NQS PRD 72 (2005) 114012 [hep-ph/0509021] (abstract, §5 'Summary of results', eq. (IIIdivergence)); NQS PRD 74 (2006) 074007 [hep-ph/0608066].

## R-M20 — correction_of_reference_doc — **refuted**

**Claim:** p. 73: the two-loop phase cancellation claim is wrong. CdFR find a Hermitian P^(2) for ≥ 5 partons; FSS: violation from three loops in pure QCD; GHMMS: cancels up to NNLO.

**Printable version:** 

**Literature check:** Yes. CdFR JHEP 07 (2012) 026 (abstract; §6.2 eqs. (mp1two), (p22part), (wd2til), (wd2til4), (2partcorrcan), (wd2til5); §6.4); FSS JHEP 11 (2012) 066 (abstract, §5, §6); Henn–Ma–Xu–Yan–Zhang–Zhu PRD 112 (2025) 076003 [2406.14604]; GHMMS JHEP 01 (2025) 090 [2408.03019], Introduction.

## R-M21 — correction_of_reference_doc — **confirmed**

**Claim:** BBNS status understated: LP argued to all orders; SCET LP derivations exist (Chay–Kim; BPRS); heavy-to-light form-factor factorization is LP theorem-level.

**Printable version:** BBNS (PRL 83 (1999) 1914; NPB 591 (2000) 313; NPB 606 (2001) 245) state the leading-power QCD factorization formula for B → M1M2 as valid to all orders in α_s. They compute the kernels at O(α_s). For the heavy–light case B → Dπ they give an explicit two-loop infrared analysis, which they say is not an all-order proof. Endpoint divergences appear only in power-suppressed terms (annihilation, chirally enhanced twist 3).

SCET derivations of leading-power factorization for B into two light mesons, to all orders in α_s, exist: Chay–Kim, NPB 680 (2004) 302 [hep-ph/0301262]; Bauer–Pirjol–Rothstein–Stewart, PRD 70 (2004) 054015. The latter argue that cc̄ ('charming') penguins could give long-distance effects at leading power.

For B → π form factors, the leading-power decomposition F_i = C_i ξ_π + φ_B⋆T_i⋆φ_π has been derived to all orders in SCET (BPS PRD 67 (2003) 071502; Beneke–Feldmann NPB 685 (2004) 249). Here ξ_π is a universal soft-overlap function that cannot be factorized further; written as a convolution it would be endpoint divergent.

Grading: the form-factor statement is [A]. QCD factorization for B → ππ at leading power is at least [P] with all-order arguments, not 'O(α_s) only'.

**Literature check:** Yes. BBNS NPB 591 (2000) 313 §2.2, §5; BBNS NPB 606 (2001) 245; Chay–Kim NPB 680 (2004) 302; BPRS PRD 70 (2004) 054015; BPS PRD 67 (2003) 071502; Beneke–Feldmann NPB 685 (2004) 249.

## R-M22 — correction_of_reference_doc — **confirmed**

**Claim:** p. 76, Conj 12.5 is not BBL's. At p_T ≫ m_Q there is LP + NLP fragmentation factorization (KQS 2012, KMQS 2014, FLMR 2012), then NRQCD.

**Printable version:** Conjecture 12.5 of the reference ('p_T ≫ m_Q or √s ≫ m_Q, leading velocity power') is not BBL's conjecture.

BBL (PRD 51 (1995) 1125, §VI.A) propose σ(H) = Σ_n F_n/M^{d_n−4}⟨0|O_n^H|0⟩. It applies to inclusive production in processes with momentum transfer Q² ≳ M², is organized in powers of v (all orders in v, finitely many matrix elements at each order), and is argued to hold to all orders in α_s. For hadron collisions BBL assume Glauber cancellation and absorption of collinear singularities into PDFs.

For p_T ≫ m_Q the established structure has two steps. First, perturbative QCD factorizes the cross section into leading-power single-parton fragmentation (∝ p_T⁻⁴) plus next-to-leading-power QQ̄-pair (double-parton) fragmentation, suppressed by m_Q²/p_T², with mixing evolution (Kang–Qiu–Sterman PRL 108 (2012) 102002; Kang–Ma–Qiu–Sterman PRD 90 (2014) 034006; in SCET, Fleming–Leibovich–Mehen–Rothstein PRD 86 (2012) 094012). Second, the input fragmentation functions at μ₀ ≳ 2m_Q are factorized with NRQCD. This second step remains a conjecture, tested at NNLO with gauge-completed octet operators (NQS).

**Literature check:** Yes. BBL PRD 51 (1995) 1125 §VI.A (erratum PRD 55 (1997) 5853); KQS PRL 108 (2012) 102002; KMQS PRD 90 (2014) 034006; FLMR PRD 86 (2012) 094012.

## R-M23 — correction_of_reference_doc — **confirmed**

**Claim:** Gap observables should be graded [C], not D (evidence for factorization restoration).

**Printable version:** For gap-between-jets and other non-global pp observables:
- Strict (amplitude-level) collinear factorization for space-like splittings is violated [V] (CdFR 2012).
- Super-leading logarithms exist at fixed order: the tower α_s^n L^{n+1}, n ≥ 4, starts at α_s⁴L⁵ relative to Born (Forshaw–Kyrieleis–Seymour JHEP 08 (2006) 059). They have been resummed (Becher–Neubert–Shao PRL 127 (2021) 212002; BNSS JHEP 12 (2023) 116).
- PDF factorization of the gap cross section is open [C]. Becher–Hager–Jaskiewicz–Neubert–Schwienbacher (PRL 134 (2025) 061901) identify three-loop active–active Glauber contributions that make the cross section consistent with PDF factorization below the veto scale at leading-log accuracy; they state this is not a proof.

The grade 'proven violated' (D) for these observables is therefore incorrect.

**Literature check:** Yes. Becher–Hager–Jaskiewicz–Neubert–Schwienbacher PRL 134 (2025) 061901 [2408.10308]; FKS JHEP 08 (2006) 059; Becher–Neubert–Shao PRL 127 (2021) 212002; BNSS JHEP 12 (2023) 116.

## R-M24 — correction_of_reference_doc — **confirmed**

**Claim:** Alien (EOM) operators vanish only off-forward or with IR-regulated legs, not 'including forward'.

**Printable version:** The vanishing of alien-operator matrix elements between on-shell partonic states is proved only for non-zero momentum transfer or IR-regulated external legs (off-shell or massive). The LSZ/Schwinger–Dyson argument for EOM operators and the BRST-Ward-identity argument for BRST-exact operators both require IR singularities weaker than the inverse-propagator zeros. That requirement can fail at zero momentum transfer with on-shell massless gluons.

Collins–Scalise (PRD 50 (1994) 4117) showed by explicit one-loop calculation that the BRST-exact gauge-variant part of the energy–momentum tensor has a non-vanishing on-shell gluon matrix element at zero momentum transfer. The reason is a 1/p² IR singularity, present only at zero momentum transfer, that cancels the inverse ghost propagator. This underlies the apparently non-triangular mixing found by Hamberg–van Neerven (NPB 379 (1992) 143). For EOM operators the forward on-shell massless case is likewise not covered by the standard proof.

Grade: proved off-forward / IR-regulated, not 'including forward'. Modern off-shell computations include the alien counterterms explicitly (Falcioni–Herzog JHEP 05 (2022) 177; Gehrmann–von Manteuffel–Yang JHEP 04 (2023) 041).

**Literature check:** Yes. Collins–Scalise PRD 50 (1994) 4117 [hep-ph/9403231] (abstract, §1, §4.4, §5); Hamberg–van Neerven NPB 379 (1992) 143; Falcioni–Herzog JHEP 05 (2022) 177; Gehrmann–von Manteuffel–Yang JHEP 04 (2023) 041.

## R-M25 — correction_of_reference_doc — **confirmed**

**Claim:** p. 118, Ass C.56 (W2) (isolated nucleon) is false in the chiral limit and for m_u ≠ m_d/QED. Lemma C.64 needs only spec ⊂ {p² ≥ M²}.

**Printable version:** Assumption C.56 (W2) of the reference requires the baryon-number-1 spectrum to lie in {p² = M²} ∪ {p² ≥ M₁²} with M₁ > M, the nucleon being the lowest, isolated mass. This fails in three cases:
- Chiral limit: m_π = 0, so the Nπ continuum starts at s = M² and no M₁ > M exists.
- Isospin breaking (m_u ≠ m_d and/or QED): p and n are two distinct discrete levels below the lowest Nπ threshold (M_n − M_p ≈ 1.3 MeV ≪ m_π). (W2) then cannot hold for a neutron target; it holds literally only for the lightest nucleon.
- Dynamical QED: the massless photon removes isolation in every sector.

Lemma C.64 (the dispersion relation) uses only spec ⊂ {p² ≥ M²}. It should be imposed in the superselection sector of the target's conserved flavour quantum numbers, which is the sector J|P⟩ populates since J is flavour diagonal. This bound holds in all the cases above. Isolation is needed only to construct one-particle and asymptotic states by standard Haag–Ruelle theory. Massive light quarks must be assumed explicitly and reconciled with the massless MS-bar coefficients.

**Literature check:** Elementary. Standard facts: the chiral-limit Nπ threshold; PDG masses; Haag–Ruelle requires an isolated mass eigenvalue (e.g. Dybalski LMP 72 (2005) 27). This is a correction of the reference only.

## R-M26 — correction_of_reference_doc — **confirmed**

**Claim:** 'No verbatim proof' of the OPE remainder (Ass C.24) was claimed without checking Anikin–Zav'yalov 1978, Zav'yalov 1990, Joglekar 1977 or Hollands 2008.

**Printable version:** The reference asserts that there is 'no verbatim proof in the literature' of two things: the momentum-space ('frozen-q') OPE remainder estimate (hence its Ass. C.24), and the BRST statements for the full gauge-variant operator basis (hence (B1)(B2)). It does not discuss directly relevant literature:
- Anikin–Zav'yalov, Ann. Phys. 116 (1978) 135. This is the reference's own [116], cited only for the light-cone expansion. It derives short-distance and light-cone expansions of T-products of currents to arbitrary order of perturbation theory.
- Zav'yalov, Renormalized Quantum Field Theory (Kluwer 1990).
- Joglekar, Ann. Phys. 108 (1977) 233 and 109 (1977) 210: the OPE of gauge-invariant currents in non-abelian gauge theory and the gauge-variant operators in it.
- Hollands, RMP 20 (2008) 1033: in perturbative pure Yang–Mills, the OPE closes on gauge-invariant operators in the BRST-cohomology sense.

Whether these works discharge Ass. C.24 (via the uniqueness result Thm C.25(iii)) or (B1)(B2) for QCD has not been established. The theory class and remainder form of Anikin–Zav'yalov/Zav'yalov are unverified; Joglekar is known here only from abstracts; Hollands covers pure YM with a position-space algebraic OPE. C.24 and (B1)(B2) remain stated assumptions until their scope is checked.

**Literature check:** The omission concerns the reference only. The relevant works exist (bibliographic data verified on INSPIRE): Anikin–Zav'yalov Ann. Phys. 116 (1978) 135; Joglekar Ann. Phys. 108 (1977) 233 and 109 (1977) 210; Hollands RMP 20 (2008) 1033 [0705.3340]; Zav'yalov, Renormalized QFT (Kluwer 1990). Whether they contain C.24 is unverified.

## R-M27 — correction_of_reference_doc — **confirmed**

**Claim:** Self-energies of space-like regulator lines are non-integrable (a 1/sinh² double pole), not an 'indispensable finite term'.

**Printable version:** For the space-like rapidity-regulator lines n_A(y_A) = (1, −e^{−2y_A}, 0_T), the Wilson-line self-energy graphs are neither finite nor indispensable.

For a real gluon of rapidity y, n_A·k = −√2 k_T e^{−y_A} sinh(y − y_A) vanishes inside the phase space. The cut (real-gluon) self-energy carries n_A²/[(n_A·k+i0)(n_A·k−i0)] = −1/(k_T² sinh²(y−y_A)). This is a pinched double pole: the rapidity integral is non-integrable, a divergence proportional to the length of the line. The virtual self-energies are scaleless.

Any self-energy factor exp σ(y) per line cancels identically in Collins' combination f̃_A = f̃_A^unsub(y_B)·√(S̃(y_A,y_n)/(S̃(y_A,y_B)S̃(y_n,y_B))). These graphs must therefore be excluded ('No S.I.', Aybat–Rogers PRD 83 (2011) 114042), or defined by one convention used consistently in f̃^unsub and S̃. For time-like lines they are finite and still cancel.

**Literature check:** Yes. Aybat–Rogers PRD 83 (2011) 114042 [1101.5057] (eq. (soft): Wilson-line self-interactions 'very badly divergent', excluded, cancel in the final definitions); project research/c_tmd/DERIVATION.md §3.2–3.6.

## R-M28 — correction_of_reference_doc — **confirmed**

**Claim:** MS-bar is not a finite renormalization of BPHZ in non-abelian theories: non-invariant counterterms are needed.

**Printable version:** In non-abelian gauge theories the passage from BPHZ(L) forest-formula renormalization to DR+MS-bar is not a finite renormalization in the sense of finite redefinitions of couplings and fields.

BPHZ(L) momentum-space Taylor subtractions break the Slavnov–Taylor identities, whether made at zero momentum with auxiliary masses or at Euclidean subtraction points. By the quantum action principle the breaking is local and, absent anomalies, it is removed by finite non-invariant counterterms (algebraic renormalization: Becchi–Rouet–Stora; Piguet–Sorella LNP m28 (1995); explicitly for BPHZL, Kraus Ann. Phys. 262 (1998) 155; Grassi–Hurth–Steinhauser Ann. Phys. 288 (2001) 197). DR+MS-bar respects the identities in vector-like QCD (Breitenlohner–Maison CMP 52 (1977) 11). The two schemes therefore differ by finite local counterterms that necessarily include non-invariant ones.

As a consequence, graphical Ward identities hold exactly only for DR (MS-bar) graphs. With BPHZ(L) they hold only up to local terms. The reference does not reconcile (U1) with its Ward-identity inputs (W1) (Ass. D.37) and (Z2) (Ass. D.43).

**Literature check:** Yes. Algebraic renormalization: Piguet–Sorella, Algebraic Renormalization, LNP m28 (1995); Kraus Ann. Phys. 262 (1998) 155 [hep-th/9709154] eq. (defren); Grassi–Hurth–Steinhauser Ann. Phys. 288 (2001) 197 [hep-ph/9907426] §1; Breitenlohner–Maison CMP 52 (1977) 11 (action principle in DR).

## R-M29 — correction_of_reference_doc — **confirmed**

**Claim:** pp. 223-226: (H1)(H2) for rewritten forms carry Glauber-specific content (Prop E.46); count them as Glauber-specific inputs.

**Printable version:** The reference undercounts the Glauber-specific open inputs of its Drell–Yan proof. It says the App. D inputs are unrelated to the Glauber region (Table 8 caption), and that the Glauber-specific residue is only Ass. E.33(c), E.44(a)–(d) and E.33(a)(b) (p. 226).

Its own Prop. E.46, Note E.11(5) and Prop. D.32, however, assign three Glauber-related checks to (H1)(H2) for the r_R-rewritten and spectator-family-summed integrands, which is the form Ass. D.14 takes in Drell–Yan:
- that the localized spectator terms plus (1−T_R) errors reproduce the distributional external-endpoint contributions at n·K_i = 0. The reference calls this 'the Glauber problem in a single cut graph'. It fixes the past-pointing Wilson-line prescription, which is substantive for TMDs.
- that SA/AS localized spectator endpoints are allocated correctly between region R and the soft limit of R′.
- that SS lines satisfy (H1) after the family sum, since it fails graph by graph.

These forms do not exist in DIS or e⁺e⁻→hX. These instances of (H1)(H2), together with the fibre-integral envelope Ass. E.34 (needed only for the Glauber-window rewriting), must be counted as Drell–Yan/Glauber-specific open inputs.

**Literature check:** Not applicable. This is a statement about the reference's internal bookkeeping (its Prop. E.46(a)(c), Note E.11(5), Prop. D.32, Table 8, p. 226).

## R-M30 — correction_of_reference_doc — **confirmed**

**Claim:** p. 229: Gaunt 2014 is cited without the SYZ 2018 rebuttal; the issue is contested (E36). Note: NNLO DY agreement does not test the Glauber cancellation.

**Printable version:** Reference p. 229 (Rem. E.55) cites Gaunt (JHEP 07 (2014) 110) as showing that the CSS Glauber-cancellation argument fails at the level of two spectator-spectator Glauber gluons for hadronic E_T. It does not mention that Schwartz-Yan-Zhu (PRD 97 (2018) 096017, the reference's own [137], cited only in a generic list on p. 230) contest the pure-Glauber part. SYZ argue to all orders (explicit two-loop check plus a scale-invariance argument) that pure Glauber ladder graphs cancel at cross-section level for every IR-safe single-scale observable (including E_T and beam thrust). The leading factorization violation then requires at least one soft emission off the Glauber rungs (Lipatov vertex, i.e. Glauber-soft mixing). Their argument excludes doubly differential observables. Gaunt's result is a failure of the CSS argument together with a suggestion of leading-power factorization failure. Zeng (JHEP 10 (2015) 189) gives an explicit counterexample in QCD with scalar quarks: a non-zero leading-power double longitudinal-spin asymmetry of the doubly differential beam thrust from S-S Glauber exchange, contradicting any factorization with decoupled collinear sectors; this lies outside SYZ's scope. Standard factorization for single-scale MPI-sensitive observables is therefore [C], not established either way. Note (not a reference error): fixed-order partonic DY contains no hadron spectators. At NNLO there is no spectator-spectator configuration at all; at N3LO there is only a single, abelian-like exchange between two radiated partons. Partonic finiteness after mass factorization therefore tests the leading-power cancellation for coloured massless partonic states, not the hadron-spectator Glauber cancellation. Agreement with data is evidence for factorization as a whole, not a test of this step.

**Literature check:** Yes: Schwartz-Yan-Zhu PRD 97 (2018) 096017 (arXiv:1801.01138) rebut the pure-Glauber claims; Gaunt JHEP 07 (2014) 110 (arXiv:1405.2080); Zeng JHEP 10 (2015) 189 (arXiv:1507.01652); Rothstein-Stewart JHEP 08 (2016) 025 sec. 11.1. The remark about the reference's citation practice is ours.

## R-M31 — correction_of_reference_doc — **confirmed**

**Claim:** p. 228, Rem E.54(b) ignores −2l_T·k_T ~ Qλ. The pinch is Glauber relative to (n_A,w_1); the conclusion survives.

**Printable version:** Reference p. 228, Rem. E.54(b): the argument '2l.k contains 2l^+k^- with l^+ ~ Q, so J_1 depends on k^- at the scale lambda^2' ignores the term -2l_T.k_T ~ lambda Q^2 for a central jet. For a generic DY-Glauber momentum k ~ (lambda^2, lambda^2, lambda)Q this term dominates (2l.k ~ lambda Q^2). The J_1 line is then off shell by O(lambda Q^2), its k^- dependence is only a relative O(lambda) effect, and that region is power suppressed. The leading pinch region is Glauber relative to the pair (n_A, w_1): k.n_A ~ k.w_1 ~ lambda^2 Q with the remaining components ~ lambda Q, i.e. w_1^- k^+ - w_1T.k_T = O(lambda^2 Q); on the slice k^+ <~ lambda^2 Q this means k_T nearly orthogonal to w_1T. There 2l.k ~ lambda^2 Q^2 and J_1 depends on k^- (through w_1^+ k^-) at the same scale lambda^2 as J_A. The premise of Lemma E.28 therefore fails, and the conclusion of Rem. E.54(b) survives.

**Literature check:** Not applicable: this is a statement about the reference document, based on standard Glauber power counting for the dipole (n_A, w_1).

## R-M32 — correction_of_reference_doc — **confirmed**

**Claim:** The App E method (hybrid LCPT, deformation mismatch, unitarity) is Aybat–Sterman 2009, which is uncited; DGOPS 2016 is not compared. The phrase 'Glauber 相消的方法是 Collins (2011) 首创' is forbidden.

**Printable version:** App E of the reference applies light-cone-ordered perturbation theory (x+ ordering for the A-collinear subgraph, x- for the B-collinear one, soft gluons as external lines). Initial-state energy denominators have soft-momentum poles on one side and final-state ones on the other, so the Glauber pinch of a single cut graph appears as an initial/final mismatch of deformation directions. This mismatch is removed by summing over cuts (unitarity), after which the soft momenta are deformed and Wilson lines obtained. This is the light-cone-ordered method of Collins-Soper-Sterman (NPB 308 (1988) 833, reviewed in Collins 2011 ch. 14), which the reference credits (p. 165). It is cast in the 'hybrid' formulation of Aybat-Sterman (PLB 671 (2009) 46, arXiv:0811.0246): LCOPT for the collinear remainder with the soft (eikonal-field) gluons as external sources; 'the Glauber pinch ... is replaced in the hybrid form by a mismatch between the directions of the deformations for initial and final states'; the causal identity; phases cancel after the inclusive sum. The reference never cites Aybat-Sterman. Diehl-Gaunt-Ostermeier-Plossl-Schafer (JHEP 01 (2016) 076) re-derive and clarify the LCPT sum-over-cuts argument for single Drell-Yan (sec. 4.3.1) and extend it to double DY. The reference cites them ([61]) only for the double-DY extension (sec. 12.6, Rem. E.57) and does not compare their single-DY treatment with App E. Our text must credit CSS 1988/Collins 2011 for the method, and Aybat-Sterman 2009 and DGOPS 2016 as precedents for its LCPT/hybrid formulation. It must not say that the method originates with Aybat-Sterman. It must not use the phrase 'Glauber 相消的方法是 Collins (2011) 首创的光锥序处理', which is wrong because the LCOPT treatment goes back to CSS 1988.

**Literature check:** Yes: Aybat-Sterman PLB 671 (2009) 46; Diehl et al. JHEP 01 (2016) 076 (sec. 4.3.1, which attributes the LCPT technique to CSS NPB 308 (1988) 833 and Collins 2011). The remark that the reference omits Aybat-Sterman is ours.

## R-m01 — correction_of_reference_doc — **confirmed**

**Claim:** m1-m5. The hard point is not a Landau solution. U(+∞) is field dependent. The original GY K is symmetric (b_k k_μk_ν). Bare-PDF positivity is formal. (1.1) notation and grade mixing.

**Printable version:** Minor corrections to the reference.
(m1) p. 16: in the Landau analysis of the off-shell Sudakov triangle, the 'hard point (alpha_k = 0, all lines off shell)' is not a Landau solution but the absence of a pinch. The soft-quark configurations k = p1 and k = -p2 (zero-momentum quark line) are Landau solutions, namely the endpoints of C1 and C2; they are power suppressed (by m^2/Q^2) and enter only at NLP.
(m2) p. 25, Rem. 3.15: U(+inf) = P exp(ig int_{-inf}^{inf} A) is a field-dependent operator, not a constant colour matrix or global gauge transformation. Independence of the collinear PDF from the boundary condition follows from W[w,inf] W[inf,0] = W[w,0].
(m3) p. 23: the K-part K^{mu nu} = n^mu k^nu/(n.k) is not the original Grammer-Yennie K-photon, which is the symmetric b_k(p_f,p_i) k_mu k_nu. The one-sided form with an i0 prescription is the adaptation used in the Collins-Soper-Sterman approach (Collins 2011 ch. 10).
(m4) pp. 13-14, Prop. 2.4: positivity of the unrenormalized PDF is formal, since the bare operator is UV divergent. The light-cone-gauge proof inherits the 1/k^+ ambiguity raised in Rem. 2.3. The light-cone anticommutator term at w_T = 0 is the divergent constant delta(w^-) delta^2(0). The support of the renormalized PDF is not addressed; it follows from a gauge-invariant state sum and the support of the renormalization kernel.
(m5) pp. 6, 7, 11: (1.1) writes an absolute remainder O((Lambda/Q)^p) although item (c) states a relative one; sigma-hat_ij(xi_A, xi_B, ...) is schematic; nu = P.q clashes with the Lorentz index nu (p. 11); grade C mixes finite-order checks ([P]) with conjectures ([C]).

**Literature check:** Grammer-Yennie PRD 8 (1973) 4332 (symmetric K-photon; checked through Sen-Indumathi-Choudhury arXiv:1812.06468); one-sided form in Collins, Foundations of perturbative QCD (2011) ch. 10, as followed by Diehl et al. JHEP 01 (2016) 076. The rest are statements about the reference only.

## R-m06 — correction_of_reference_doc — **confirmed**

**Claim:** m6-m12. T_2 vertex roles; non-standard duality example; α_s^n[ln^{2n−1}(1−z)/(1−z)]_+ ↔ ln^{2n}N; τ conflict; missing colour projection (1/N_c)TrH TrJ; degree max(1,n); finite parts quoted, not derived.

**Printable version:** Minor corrections to the reference.
(m6) p. 34, Ex. 5.2: in the tree handbag the T_2 structure (P^mu P^nu) comes from the kslash term of the propagator numerator: the gamma-index of the twist-2 operator is one of the vertex gammas, and kslash supplies the derivatives. The qslash term feeds only T_1 (g^mu nu) and the gauge terms (q^mu ...).
(m7) p. 32: the duality-violation example e^{-c sqrt(s)/Lambda} sin(...) is non-standard. Instanton-type (finite-distance) mechanisms give power-damped oscillations s^{-kappa/2} sin(sqrt(s) rho); resonance models at large finite N_c give exponentially damped oscillations in s, of the form e^{-delta - gamma s} sin(alpha + beta s) (Shifman hep-ph/0009131).
(m8) p. 49, Rem. 7.5: at order alpha_s^n the threshold logarithms are alpha_s^n [ln^{2n-1}(1-z)/(1-z)]_+, which correspond to alpha_s^n ln^{2n} N in Mellin space, since M_N[(ln^k(1-z)/(1-z))_+] ~ (-1)^{k+1} ln^{k+1}(N e^gE)/(k+1). They are not 'alpha_s^n ln^{2n-1}(1-z)'.
(m9) tau denotes Q^2/s on p. 12 but Q^2/s-hat on p. 49.
(m10) pp. 39-40: for a colour-singlet target the colour projection Tr_c[H J] = (1/N_c) Tr_c H Tr_c J must be included alongside the Dirac projection.
(m11) p. 29: a_n has degree n-1 only for n >= 1 (a_0 is a constant); the n-th coefficient of Pi has degree max(1, n) in L.
(m12) p. 49, Prop. 7.4: the finite parts c_q, C_2,g are quoted, not derived, and the 1/(D-2) gluon polarization average, the DIS scheme and F_L are not mentioned.

**Literature check:** Shifman, 'Quark-hadron duality', At the Frontier of Particle Physics vol. 3 (WS 2001) 1447 (hep-ph/0009131); Mellin asymptotics and MS-bar coefficient functions are textbook results. The corrections themselves concern the reference only.

## R-m13 — correction_of_reference_doc — **confirmed**

**Claim:** m13-m16. Fig 34 gauge dependence (Feynman gauge: t|M_e|² → −80, t·2Re → +33.6). PT bilinear, ε_T^{12} = +1. Remainder O((Λ²/Q⁴)ln(Q²/Λ²)). Small-b remainder O((b_Tm)²), not O(b_TΛ) (also OUR-5).

**Printable version:** Minor corrections to the reference.
(m13) p. 56, Fig. 34: the statement that the collinear (1/t) singularity of q g -> gamma* q comes from the square of graph (e) is gauge dependent. In Feynman gauge (gluon polarization sum -g), with t = (k - p_2)^2 -> 0 and z = Q^2/s-hat, t|M_e|^2 -> -8 s-hat and t 2Re(M_d M_e*) -> +16 s-hat z(1-z), so the interference also has the 1/t pole. Only the sum, -8 s-hat [z^2 + (1-z)^2] proportional to P_qg, is physical (couplings, colour and spin average stripped; at s-hat = 10, Q^2 = 3 the values are -80 and +33.6). Only in a light-cone (axial) gauge does the pole come from |M_e|^2 alone.
(m14) p. 67: under the antiunitary PT, psibar(w) gamma^mu psi(0) -> +psibar(-w) gamma^mu psi(0) directly, with no Hermitian conjugation needed. The colour matrices go to t^{a*} = t^{aT}, which reverses the path ordering. For a hadron along +z the Trento definition f = f_1 - f_1T^perp (P-hat x k_T).S/M requires eps_T^{12} = +1 in (10.9). This is not the Trento eps_perp of the SIDIS frame, which has eps_perp^{12} = -1.
(m15) pp. 68-69: by the reference's own endpoint-area estimate (area ~ (Lambda^2/Q^2) ln(Q^2/Lambda^2)), the remainder in (11.2) is O((Lambda^2/Q^4) ln(Q^2/Lambda^2)), not O(Lambda^2/Q^4).
(small-b) p. 66, Cor. 10.5: for unpolarized leading-twist TMDs the small-b matching onto collinear PDFs has power corrections O((b_T m)^2), up to logarithms (more precisely ~ x b_T^2 Lambda^2 for TMD PDFs and b_T^2 Lambda^2/z for TMD FFs), not O(b_T Lambda). The same correction applies to our own spec (OUR-5).

**Literature check:** Gauge dependence of the collinear pole is textbook (axial-gauge collinear factorization). Trento conventions: Bacchetta et al. PRD 70 (2004) 117504. Small-b power corrections ~ b^2: Scimemi-Vladimirov JHEP 03 (2017) 002 (arXiv:1609.06047); Moos-Vladimirov JHEP 12 (2020) 145 (arXiv:2008.01744). The errata of the reference are ours.

## R-m17 — correction_of_reference_doc — **confirmed**

**Claim:** m17-m22. T_coll = T_2; SCET lines fixed by external states, and the λ²Q mode is ultrasoft; Prop 14.1 unproven (large-N O(N) σ-model case); twist parity holds only for symmetric operators; invariant cross section needed; bibliography misattributions and missing refs.

**Printable version:** Minor corrections to the reference.
(m17) p. 73, (12.2): the colour operator in the one-loop space-like splitting amplitude is -2 sum_{j non-collinear} T_2.T_j f(eps; z_2 - i0 s_j2), where T_2 is the colour charge of the collinear parton whose momentum fraction can be negative (Catani-de Florian-Rodrigo, JHEP 07 (2012) 026). With only three coloured partons it reduces to a c-number by colour conservation; genuine colour correlations require at least four coloured partons.
(m18) pp. 77-78: in SCET_I the direction (i0 prescription) of the ultrasoft Wilson line is fixed by the external states already at leading order: past-pointing for incoming and future-pointing for outgoing collinear quarks (Chay-Kim-Kim-Lee, PRD 71 (2005) 056001). The lambda^2 Q mode is ultrasoft, not soft.
(m19) p. 81: Prop. 14.1 is only argued. The explicit proof that IR renormalons cancel against the ambiguities of higher-dimension terms in the OPE exists for the two-dimensional O(N) sigma model at large N (David, NPB 209 (1982) 433; NPB 234 (1984) 237; at NLO in 1/N, Beneke-Braun-Kivel, PLB 443 (1998) 308).
(m20) p. 83: 'twist parity = chirality' holds for symmetric traceless operators, as Lemma C.43 states; it fails, e.g., for the twist-2 chiral-odd transversity operator.
(m21) p. 72, (12.1): sigma-hat_{ab->c} must be the invariant E_c dsigma-hat/d^3p_c; the factor 1/z^2 is the Jacobian.
(m22) Bibliography: errata omitted for [34] (NPB 644 (2002) 403) and [59] (PRD 55 (1997) 5853); minor title deviations in [27], [53], [56]. Relevant works are missing: Collins 2007 (arXiv:0708.4410), Aybat-Sterman 2009, Mitov-Sterman 2012, Becher et al. 2025, Kang-Qiu-Sterman 2012, Nayak-Qiu-Sterman PLB 2005, BBNS 2000, Nachtmann 1973. The content misattributions of [53] and [60] are treated in R-M18 and R-M19.

**Literature check:** Catani-de Florian-Rodrigo JHEP 07 (2012) 026; Chay-Kim-Kim-Lee PRD 71 (2005) 056001; David NPB 209 (1982) 433; Beneke-Braun-Kivel PLB 443 (1998) 308. The corrections concern the reference only.

## R-m23 — correction_of_reference_doc — **confirmed**

**Claim:** m23-m25. Ex C.27 sharpened (N15); App C details; D.20 misinvoked. The Table 5 fit should be t(2L² − 4L − 4 + 2π²/3), and Table 5 does not test the remainder (N12). The C_S integral is a Beta function.

**Printable version:** Minor corrections to the reference.
(m23) pp. 101-102, Ex. C.27: the reduced combination is kappa int d^4k [Delta(q-k) - Delta(q)] Delta(k)^3 = -kappa pi^2/(2q^4) + O(m^2 q^-6 ln q). It has no logarithm at O(q^-4), and its leading term is m-independent, by 4D harmonicity; the reference states only O(q^-4 ln q^2).
(m24) App. C: Cor. C.18 needs the additive extension of omega to disconnected subgraphs, since Def. C.5 covers only connected ones. Besides Thm. C.8, the perturbative proofs also use Zimmermann's compatibility of canonical momentum routing [78], whose use for frozen-q AB parts deserves a lemma. The one-dimensional edge-of-the-wedge step in Lemma C.64 needs the same Q^2-smearing argument used for positivity. In Thm. C.66(i) the bound ||gamma(alpha)|| <= C alpha requires rescaling the dimensionful mass-mixing entries.
(m25) App. D: Lemma D.20 (soft-momentum deformation) is invoked unnecessarily in the proof of Prop. D.28(a), since the DIS unphysical region has no soft approximations. The exact next-to-leading power of the off-shell triangle is Q^2 I = L^2 + pi^2/3 + t(2L^2 - 4L - 4 + 2pi^2/3) + O(t^2 L^2), with t = m^2/Q^2 and L = ln(Q^2/m^2); the fit '2 lambda^2 L^2 - 3.9 lambda^2 L' of Table 5 approximates it. Table 5 compares I with L^2 + pi^2/3 written in Q^2, not with (D.32) written in Q~^2 = 2PP', so it does not test the Collins remainder. That remainder is I - (D.32) = -4m^2/Q^4 + (m^4/Q^6)(L^2 - 15 + pi^2/3) + ..., with no logarithm at NLP. The C_S k^+ integral is a Beta function, Gamma(eps) Gamma(1-eps) (m^2)^-eps (2P')^(eps-1), not J(eps). Typo '假设假设' on pp. 128 and 146. (Not to be printed: the claim that Fig. 55 has cubic vertices outside the model is false, since Yukawa vertices are dimension-4 monomials of the stated model; the Lemma D.23(iii) edge case is unverified.)

**Literature check:** The exact triangle is classical (Usyukina-Davydychev one-loop Phi^(1)); the sharpened remainder and NLP coefficients are the explicit results N12 and N15 of our material, reproduced here numerically. The corrections concern the reference only.

## R-m26 — correction_of_reference_doc — **confirmed**

**Claim:** m26-m27. E.28(iii) fixable via LHP closure; vertex sign +ig; (E.30) absolute; Rem E.49(2): compensating +¼C_Aχ²X; σ missing in Im(n·K); w_12 also depends on k_T1²/k_T2².

**Printable version:** Minor corrections to App. E of the reference.
(i) The proof of Lemma E.28(iii) uses derivative bounds on E near real-axis poles that do not follow from (J1)(J2). It is repaired by closing the contour in the lower half plane: int dk/2pi E R_down = -i sum_i r_i E(z_i), where E = J^fi + iJ_+/(k - i lambda_J) is analytic in the closed LHP and satisfies |E(z)| <= 2M lambda_J/|z|^2 there. With |z_i| >= 2Lambda this gives O(M lambda_J ||R||/Lambda).
(ii) With the reference's own covariant derivative D_mu = d_mu - igA_mu, the leading couplings on p. 195 are +ig J_A^{+a}, +ig J_B^{-a}, not -ig. V_G is unaffected, because two vertices enter.
(iii) The error in (E.30) must be stated as absolute, O(M lambda_J |R(0)|/Lambda) with M >= |J_pm| the constant of (J2), not as a relative error with respect to R(0) J_A(0).
(iv) In Rem. E.49(2) the residual of (E.51) is -(1/4) C_A chi^2 X. The contribution that the complete graph set must supply, if Assumption E.33(c) holds, is therefore +(1/4) C_A chi^2 X.
(v) On the deformed contour, Im(n.K) = t sigma sum_a f_a (sigma = +1 amplitude, -1 conjugate), so sigma Im(n.K) = t sum_a f_a >= 0; the printed formula omits sigma.
(vi) The two-insertion ordering weight w_12 = z_1/(z_1+z_2), z_j = k_Tj^2/(2k_j^+), depends on k_T1^2/k_T2^2 as well as on the k_j^+.

**Literature check:** Not applicable: these are statements about the reference document. The ordering-weight formula itself is the lemma N13 of our material.

## R-OUR1 — correction_of_reference_doc — **confirmed**

**Claim:** INTERNAL: errors in our own spec (the reference is correct here). OUR-1: the FF prefactor in the hadron frame is z^{1−2ε}/(4N_c), not 1/(4N_cz) (Jacobian d^{2−2ε}p_hT = z^{2−2ε}d^{2−2ε}k_T). OUR-2: subtraction conditions (CS1)-(CS3), not termwise induction. OUR-3: hadronic OPE only on |ω| ≤ √3M/Q. OUR-4: two-component deformation along e_G = n_B − n_A.

**Printable version:** Corrections of our own specification (the reference is correct on these points).
(OUR-1) The collinear fragmentation function defined in the hadron frame (p_hT = 0, w = (0^+, w^-, 0_T)) carries the prefactor z^{1-2eps}/(4N_c) = z^{d-3}/(4N_c) (Collins-Soper 1982; Collins 2011 ch. 12). The prefactor 1/(4N_c z) belongs to the parton frame, together with an explicit integral over d^{2-2eps} p_hT; the two are related by d^{2-2eps} p_hT = z^{2-2eps} d^{2-2eps} k_T. With the correct prefactor the O(alpha_s) quark-to-quark FF is (alpha_s/2pi) C_F (1+z^2)/(1-z) dl_T^2/l_T^2; with 1/(4N_c z) in the hadron frame it would be z^{-2} times this, an error the delta(1-z) free-quark check cannot detect.
(OUR-2) Collins' subtraction theorem must be stated as a conditional theorem under subtraction-level conditions (our (CS1)-(CS3)). A termwise induction is impossible, because single approximants and chain terms are not absolutely integrable (e.g. T_C1 Gamma converges only for eps < 0 at the rapidity end and only for eps > 0 in the UV; the scaleless T_C1 T_S Gamma for no eps), and the suppression holds only for grouped expressions.
(OUR-3) For a hadron target the Euclidean OPE gives information only on a shrinking segment of the imaginary omega axis. In the rest frame, Euclidean q gives omega = 2iMq_4/Q^2, so |omega| <= 2M/Q, and |omega| <= sqrt(3) M/Q with the restriction |q-vector| >= Q/2 needed for a non-degenerate T_2 projection. 'Insert and compare coefficients' treats a formal series as convergent; moments must be obtained via fixed-n Taylor coefficients, positivity and finite-subtraction dispersion relations.
(OUR-4) Leaving the Glauber region requires the simultaneous deformation of both light-cone components along e_G = n_B - n_A (Im k^+ = -sigma kappa |k_T|, Im k^- = +sigma kappa |k_T|), giving |k^+||k^-| >= kappa^2 k_T^2 with Re k^2 < 0. Deforming only k^- (to |k^-| ~ |k_T|) leaves |k^+ k^-| ~ lambda^3 << k_T^2 and only makes one side's soft approximation valid; one component alone is limited by the soft line's own pole at k^- ~ k_T^2/(2|k^+|).

**Literature check:** Yes, as standard material: FF normalization in Collins-Soper NPB 194 (1982) 445 and Collins 2011 ch. 12 (also the reference's (2.13)); the failure of termwise subtraction arguments, the Euclidean segment (C.31) and the two-component deformation (E.42) are in the reference document (not citable).

## R-OUR2 — correction_of_reference_doc — **confirmed**

**Claim:** INTERNAL: OUR-5, small-b remainder O((b_Tm)²) (verify). OUR-6: real-ω remainder bounds do not control the discontinuity. OUR-7: Shifman2000 booktitle 'At the Frontier of Particle Physics' vol. 3, pp. 1447-1494. OUR-8: exceptional forward momenta need separate tags.

**Printable version:** Corrections of our own specification.
(OUR-5) The small-b matching of unpolarized leading-twist TMDs onto collinear PDFs has remainder O((b_T m)^2), up to logarithms, not O(b_T m). Rotational invariance allows no term odd in b_T for an unpolarized target, and renormalon and twist analyses give leading corrections ~ b_T^2 (scaling as x b_T^2 Lambda^2 for TMD PDFs; Scimemi-Vladimirov JHEP 03 (2017) 002, Moos-Vladimirov JHEP 12 (2020) 145).
(OUR-6) Remainder bounds valid on a real segment of omega in the unphysical region do not, by themselves, control the discontinuity (the physical structure function) pointwise. One needs either bounds uniform on a complex domain (giving moments by Cauchy estimates) or a direct physical-region (cut-diagram) argument.
(OUR-7) The bibliographic entry is: M. Shifman, 'Quark-hadron duality', in At the Frontier of Particle Physics: Handbook of QCD, ed. M. Shifman (World Scientific, Singapore 2001), vol. 3, pp. 1447-1494 [hep-ph/0009131], not the proceedings of the 8th International Symposium on Heavy Flavor Physics, where only the underlying talk was given.
(OUR-8) The forward on-shell partonic statements of the DIS OPE are at exceptional (and non-Euclidean) momenta and are not covered by the Euclidean non-exceptional OPE theorem; they need separate sub-statements with their own rigor tags (dimensional regularization of the IR, partonic matching).

**Literature check:** Yes: Scimemi-Vladimirov JHEP 03 (2017) 002 and Moos-Vladimirov JHEP 12 (2020) 145 for OUR-5; INSPIRE and arXiv records of hep-ph/0009131 for OUR-7; the non-exceptional-momentum condition is standard (Zimmermann; Lowenstein-Zimmermann). OUR-6 is also stated in the reference's Prop. D.28(b).

## A01 — attribution — **confirmed**

**Claim:** LAMET.md cites NPB 964 (2021) 115311 as 'Ji, Liu, Liu, Zhang, Zhao et al.'. The INSPIRE authors are X. Ji, Yizhuang Liu, A. Schäfer, W. Wang, Y.-B. Yang, J.-H. Zhang, Y. Zhao; the cited list is that of the RMP.

**Printable version:** The hybrid-renormalization paper NPB 964 (2021) 115311 [Ji:2020brr, arXiv:2008.03886] is by X. Ji, Y. (Yizhuang) Liu, A. Schäfer, W. Wang, Y.-B. Yang, J.-H. Zhang and Y. Zhao. LAMET.md line 89 must cite it as 'Ji, Liu, Schäfer, Wang, Yang, Zhang, Zhao, NPB 964 (2021) 115311'.

The string 'Ji, Liu, Liu, Zhang, Zhao' is the complete author list of the LaMET review RMP 93 (2021) 035005 [Ji:2020ect]. PLB 811 (2020) 135946 [Ji:2019ewn] is by X. Ji, Yizhuang Liu and Yu-Sheng Liu, so LAMET line 101 is correct.

**Literature check:** Bibliographic metadata: INSPIRE records Ji:2020brr, Ji:2020ect, Ji:2019ewn; Crossref DOIs 10.1016/j.nuclphysb.2021.115311, 10.1103/RevModPhys.93.035005, 10.1016/j.physletb.2020.135946; arXiv API.

## A02 — attribution — **confirmed**

**Claim:** Yizhuang Liu: INSPIRE 1981577, BAI Y.Liu.90, ORCID 0000-0002-0897-1165; 73 items by BAI, 72 by name search. BSc USTC 2012; PhD Stony Brook 2018 (Zahed); TDLI; Regensburg; Jagiellonian since 2021; habilitation 2023 [H1]-[H7]. The Chinese name is UNVERIFIED (do not print). Our files conflict: LAMET line 9 uses 刘义壮, YZLIU line 857 and FINAL_OUTLINE line 137 use 刘一壮. No personal identifiers.

**Printable version:** Yizhuang Liu is INSPIRE author 1981577 (BAI Y.Liu.90; ORCID 0000-0002-0897-1165). The BAI search gives 73 INSPIRE literature records (July 2014 – Sept 2026). The quoted name search a "Liu, Yizhuang" gives 72; the BAI adds the APPB lecture notes, whose author string is 'Liu, Y.'.

Career (habilitation summary, Jagiellonian University BIP, Aug 2023):
- B.Sc. USTC 2012;
- Ph.D. SUNY Stony Brook 2018 (advisor I. Zahed);
- postdoc at TDLI Shanghai 2018–2020 and at Regensburg 2020–2021;
- at the Jagiellonian University since 2021 (postdoctoral internship, then adiunkt).

His 2023 habilitation application rests on [H1]–[H7] = Ji:2021znw, Ji:2020brr, LatticeParton:2020uhz, Ji:2020ect, Ji:2019ewn, Ji:2019sxk, Ji:2023pba.

No authoritative Chinese rendering of his name was found. None may be printed: delete 刘义壮 (LAMET.md l. 9) and 刘一壮 (YZLIU.md l. 857; FINAL_OUTLINE.md l. 137).

**Literature check:** INSPIRE author record 1981577 and literature search 'a Y.Liu.90'; ORCID 0000-0002-0897-1165; habilitation documents 'Yizhuang Liu_opis_kariery_zawodowej' and 'wykaz osiągnięć' on habilitacje.bip.uj.edu.pl.

## A03 — attribution — **confirmed**

**Claim:** Liu-programme 'first' claims: time-independent soft factor (A1); continuation framework and Table 2 (A3); S_I and 𝒟 = 2𝒟_1 − 𝒟_2 (A5); time-ordering argument (A6); quasi-TMD matching and power counting (B1); threshold factorization (C2); convergent twist expansion in 2D GN, λ ∈ iℝ≥0 only (D1); 2D results the only all-power case (LAMET §11). LPC 2020 'first lattice CS kernel' conflicts with Shanahan–Wagman–Zhao arXiv:2003.06063 (earlier).

**Printable version:** Priority statements that may be printed (each 'to our knowledge, INSPIRE searches Oct 2026'):

(A1) Ji–Liu–Liu [Ji:2019sxk] first represented the Collins off-light-cone soft factor as a time-independent matrix element, a form factor of a fast heavy-quark pair. The earlier bent Euclidean soft functions [Ji:2014hxa, Ebert:2019okf] reproduce only the one-loop logarithms (JLL's argument).

(A3) Liu [Liu:2022nnk] gave a systematic analytic-continuation classification of off-light-cone TMD soft functions, including the universality classes of Table 2. Analyticity of the cusp anomalous dimension in the cusp angle goes back to Korchemsky–Radyushkin 1987. Do not print 'first' without 'to our knowledge'.

(A5) The intrinsic soft function S_I = e^{−𝒟}, with 𝒟 = 2𝒟1 − 𝒟2, was introduced by JLL as an operator-defined, rapidity-scheme-independent and Euclidean-computable object. An undetermined non-perturbative soft mismatch factor g^S_q had been introduced earlier by Ebert–Stewart–Zhao (PRD 99 (2019) 034505).

(A6) Liu [Liu:2023pjb] gave the first explicit all-order argument (conditional on DR coordinate-space analyticity) that the DY soft factor in the exponential regulator is time-ordering insensitive and equals a single-time-ordered form factor.

(B1) Ji–Liu–Liu (PLB 811) first matched a quasi-TMD to the scheme-independent TMDPDF with a Euclidean-computable soft factor. The single-line power counting is APPB eqs. (54)–(68).

(C2) Ji–Liu–Su (JHEP 08 (2023) 037) first derived the threshold factorization C → H·J of the momentum-space quasi-PDF matching kernel and its RG resummation. Earlier, Gao–Lee–Mukherjee–Shugert–Zhao (PRD 103 (2021) 094504) explained the origin of the threshold logarithms and resummed those of the pseudo-PDF/short-distance coefficient at NLL.

(D1) Liu (JHEP 09 (2024) 093) gives the first exactly worked marginal 2D theory (U(N) Gross–Neveu, O(1/N)) in which the Bjorken-limit twist expansion of a forward matrix element is derived to all powers and shown to converge pointwise for imaginary Ioffe time λ ∈ iℝ≥0 (F2, F3 'similar'). The all-power, convergent OPE of a vacuum correlator was obtained earlier in the O(N) σ model by Beneke–Braun–Kivel (PLB 443 (1998) 308).

(LAMET §11) Restrict the 'only all-power case' sentence accordingly (O(1/N), forward matrix elements).

(I.5) LPC 2020 [LatticeParton:2020uhz] performed the first lattice calculation of S_I. The first lattice determination of the CS kernel is Shanahan–Wagman–Zhao [Shanahan:2020zxr] (quenched; arXiv March 2020).

**Literature check:** The novelty statements are the authors' own:
- JLL NPB 955 (2020) 115054 (introduction);
- LPC PRL 125 (2020) 192001 ('first lattice QCD calculation of the intrinsic soft function');
- SWZ PRD 102 (2020) 014511 ('first exploratory determination of the CS kernel');
- Liu JHEP 09 (2024) 093 §1.

Precedents to cite:
- Gao et al. PRD 103 (2021) 094504;
- Ebert–Stewart–Zhao PRD 99 (2019) 034505 (g^S_q);
- Korchemsky–Radyushkin NPB 283 (1987) 342;
- Beneke–Braun–Kivel PLB 443 (1998) 308;
- Mariño–Miravitllas SciPost Phys. 18 (2025) 101.

## A04 — attribution — **refuted**

**Claim:** Liu proof status: APPB self-assessment ('typical rigorous standards' except analyticity); PLB is a 'sketch'; ESSZ 2022 is an independent all-order proof, VS 2020 one-loop SCET; the renormalization proofs are not Liu's; CS 1981 detail beyond one loop 'not presented'; Vladimirov 'the open question'; pinch poles go back to Collins 2008 and Ji:2018hvs; ultrasoft loop order should not be pinned; N_m conjecture (2.52) [C]; DY = SIDIS [P].

**Printable version:** 

**Literature check:** Liu, Acta Phys. Polon. B 53 (2022) 4-A2: §6, §4.4 and Ref. [47] = Collins, Int. J. Mod. Phys. Conf. Ser. 4 (2011) 85. PLB 811 (2020) 135946. Vladimirov–Schäfer PRD 101 (2020) 074517. Ebert et al. JHEP 04 (2022) 178. Vladimirov JHEP 04 (2018) 045, p. 32. Collins PoS LC2008 028. Ji et al. PRD 99 (2019) 114006. Liu–Su JHEP 02 (2024) 204, eq. (2.52). Liu JHEP 09 (2024) 030 and 093.

## A05 — attribution — **confirmed**

**Claim:** LaMET attributions: Ji–Liu–Su 2026 decay theorem after Fredenhagen 1985; IJJSZ (OPE) vs Ma–Qiu (published 2018) routes; RMP proof only for free-quark states; Ji 2014 asserted without proof; JZZ space-like extension asserted; IMQY superficial counting; BCK 2020 space-like = time-like ADs; Radyushkin 1983 support (recalled); JLS fitted c_a, c_H, with H confirmed by dRV; Avkhadiev 2024 'first such determination'.

**Printable version:** (i) Exponential decay of space-like correlators follows from locality and a spectral gap (Ji–Liu–Su 2026, §5). It uses the conformal-mapping/Jensen technique of Fredenhagen's cluster theorem (CMP 97 (1985) 461). The underlying spectral representation is proven to all orders in φ³/φ⁴ perturbation theory. For QCD the result is [A]/[C].

(ii) The quasi-PDF matching theorem has two proof routes:
- the coordinate-space OPE (Izubuchi–Ji–Jin–Stewart–Zhao 2018), assuming the OPE that is 'widely assumed' for QCD;
- collinear factorization (Ma–Qiu, arXiv 2014, PRD 98 (2018) 074021).
The RMP states that the proof covers only perturbative free-quark states. Ji 2014 asserted, without proof, that the factorization can be proved order by order as in the renormalization program.

(iii) Multiplicative renormalizability:
- Ji–Zhang–Zhao 2018 (auxiliary heavy field; the space-like extension of the HQET/BRST argument is asserted);
- Green–Jansen–Steffens 2018;
- Ishikawa–Ma–Qiu–Yoshida 2017 (superficial degree counting, not a full BPHZ analysis).
Braun–Chetyrkin–Kniehl 2020 argue that the space-like and time-like renormalization factors coincide to all orders, and compute them to three loops (quark) and two loops (gluon).

(iv) Support property: Radyushkin, PLB 131 (1983) 179, by parametric representation.

(v) Ji–Liu–Su 2023 extracted the two constants c_a and c_H by comparing their threshold factorization with the exact NNLO kernel (41 singular terms). c_H = 0.0725 C_F² − 0.0840 C_F C_A + 0.1453 C_F n_f T_F. Their H agrees with del Río–Vladimirov.

(vi) Avkhadiev–Shanahan–Wagman–Zhao 2024 call their lattice CS-kernel result 'the first such determination with systematic control of quark mass, operator mixing, and discretization effects'.

**Literature check:** Ji–Liu–Su arXiv:2601.12189 §5. Fredenhagen CMP 97 (1985) 461. Izubuchi et al. PRD 98 (2018) 056004. Ma–Qiu PRD 98 (2018) 074021. Ji Sci. China 57 (2014) 1407. RMP 93 (2021) 035005 §III. Ji–Zhang–Zhao PRL 120 (2018) 112001. Ishikawa et al. PRD 96 (2017) 094019. Braun et al. JHEP 07 (2020) 161. Radyushkin PLB 131 (1983) 179. Ji–Liu–Su JHEP 08 (2023) 037. Avkhadiev et al. PRL 132 (2024) 231901.

## A06 — attribution — **refuted**

**Claim:** Literature-absence claims: no Zimmermann-level OPE for Wilson-line operators; no quasi-TMD Glauber analysis; no N³LO kernel; no refutation of the Rossi–Testa resolution; the RS ℒ_G proof never appeared; no BBNS refactorization; no all-order twist-3 SSA proof; no QCD-with-quarks flow-equation OPE proof (not verified); no multilocal BRST proof; Gordan precedent unchecked. Unrefereed: Collins 2020, FH 2016, BSS 2026, Gamberg 2022, Bodwin 2025.

**Printable version:** 

**Literature check:** Contradicting literature: Cheng et al. PRL 134 (2025) 251902 [arXiv:2410.05141]; Ji et al. JHEP 03 (2025) 045; Rossi–Testa PRD 98 (2018) 054028 and PoS Confinement2018 092; Karpie et al. JHEP 11 (2018) 178; Radyushkin PLB 788 (2019) 380.

Supporting literature: Diehl et al. JHEP 01 (2016) 076; Rein et al. PRL 135 (2025) 251901; Keller–Kopper PLB 273 (1991); Efremov–Guida–Kopper J. Math. Phys. 58 (2017); Fröb–Holland–Hollands J. Math. Phys. 57 (2016) 122301.

## A07 — attribution — **confirmed**

**Claim:** GPDs at x = ±ξ: Braun 2024 finds first-power corrections; Su et al. 2026 find no leading-twist soft contribution and continuous GPDs. The two are not strictly contradictory; with Braun 2023 twist-3 the status is [C].

**Printable version:** Braun–Koller–Schoenleber (PRD 109 (2024) 074510; renormalon analysis) find that at x = ±ξ the non-perturbative corrections to quasi-GPDs are suppressed by only the first power of the hard scale. These corrections come from soft momenta and are unrelated to the UV renormalon of the Wilson line; the limits x → ±ξ and P → ∞ do not commute.

Su–Ji–Liu–Zhang (arXiv:2609.20545) show that the one-loop logarithms of the would-be soft scale 2|x±ξ|P^z come multiplied by |x±ξ|, so there is no leading-twist soft contribution. Reanalysing four lattice data sets with full one-loop matching and the regulator ordering ε2 ≪ |ε1| → 0, they obtain GPDs that are continuous at x = ±ξ, with discontinuous derivatives.

The two results are not contradictory: no leading-twist soft term, versus a first-power correction. Neither paper criticises the other. Together with the logarithmically enhanced, discontinuous kinematic twist-3 terms of Braun (JHEP 10 (2023) 134), computability at x = ±ξ beyond leading power is [C].

**Literature check:** Braun–Koller–Schoenleber PRD 109 (2024) 074510; Su–Ji–Liu–Zhang arXiv:2609.20545; Braun JHEP 10 (2023) 134.

## A08 — attribution — **confirmed**

**Claim:** Collins 2020 exists as v1 only, unpublished (as is Mühlbauer 2020). OTHERS grades it [R]†, which FINAL_OUTLINE §0.9 item 4 does not adopt.

**Printable version:** Collins, 'A new and complete proof of the Landau condition for pinch singularities of Feynman graphs and other integrals' (arXiv:2007.04085), exists only as v1 (8 July 2020, 39 pp.) with no journal publication as of 2026-10-10. The same holds for Mühlbauer, 'Momentum Space Landau Equations Via Isotopy Techniques' (arXiv:2011.10368, v1).

Collins' Theorem 1 is proven only for denominators at most quadratic and obeying the sign condition (8.15). He regards these restrictions as needed only by his method.

OTHERS grades Theorem 1 [R]† (with (8.15)) and [C] without. FINAL_OUTLINE §0.9 item 4 does not adopt the [R]† grade (decision D3), so the monograph cites the work as an unrefereed preprint.

**Literature check:** arXiv:2007.04085v1 and arXiv:2011.10368v1. INSPIRE Collins:2020euz and Muhlbauer:2020kut (no publication_info). Crossref (no journal record).

## A09 — attribution — **confirmed**

**Claim:** OPE rigour. Zimmermann: scalar theory; QCD is 'proved the same way' (Collins 1984 §12.8) or 'widely assumed' (IJJSZ). Hollands 2008: pure YM only. Fröb–Holland 1603.08012 (unpublished): BRST closure fails with chiral fermions in non-real representations. Convergence: φ⁴_4 only (HK 2012 eq. (7); HHK 2016). Anikin–Zav'yalov theory class unverified.

**Printable version:** (1) Zimmermann proved the OPE in renormalized perturbation theory for scalar field theory. For gauge theories Collins (Renormalization, §12.8) asserts that it 'is proved in a gauge theory the same way as in any other theory'; IJJSZ 2018 say it is 'widely assumed' for QCD.

(2) Hollands (Rev. Math. Phys. 20 (2008) 1033) constructs perturbative pure Yang–Mills theory on globally hyperbolic spacetimes; the OPE closes on gauge-invariant operators. Matter fields are only discussed (§5.1: possible anomalies with chiral fermions).

(3) Fröb–Holland (arXiv:1603.08012, unpublished) prove OPE existence for massless renormalizable theories (Thm 1). They prove BRST Ward identities for the OPE coefficients if H^{1,4}_{E(4)}(s|d) = 0 (Thm 2). This holds for pure YM but not, for instance, with chiral fermions in non-real representations; their bounds are proven for pure YM only, hence [R]†.

(4) Convergence of the OPE at finite distance is proven only for φ⁴₄ at fixed loop order: massive in Hollands–Kopper, CMP 313 (2012) 257, eq. (7); massless in Holland–Hollands–Kopper, CMP 342 (2016) 385.

(5) The theory class covered by Anikin–Zav'yalov (Ann. Phys. 116 (1978) 135) is unverified.

**Literature check:** Zimmermann Ann. Phys. 77 (1973) 570. Collins, Renormalization (CUP 1984; OA 2023, DOI 10.1017/9781009401807) §12.8. Izubuchi et al. PRD 98 (2018) 056004. Hollands Rev. Math. Phys. 20 (2008) 1033. Fröb–Holland arXiv:1603.08012. Fröb–Holland–Hollands J. Math. Phys. 57 (2016) 122301. Hollands–Kopper CMP 313 (2012) 257. Holland–Hollands–Kopper CMP 342 (2016) 385. Anikin–Zav'yalov Ann. Phys. 116 (1978) 135.

## A10 — attribution — **confirmed**

**Claim:** Method of regions: rigorous in Euclidean limits (Smirnov 1990); Jantzen 2011 has a gap; SSS 2019 partial proofs; 'regions = facets' [V] (GHJM 2024); BHJNS found a Glauber region missed by codes. The off-shell Sudakov example is BBF 2015 §2.2 (massive exchange: Jantzen §6), not Beneke–Smirnov 1998.

**Printable version:** Method of regions — status.

(1) Rigorous for Euclidean large-momentum and large-mass limits (Smirnov, CMP 134 (1990) 109).

(2) Jantzen (JHEP 12 (2011) 076) gives a general derivation conditional on commuting expansions and on the convergence and exchangeability of the series summations: identity [R] conditionally, applicability [P].

(3) Semenova–Smirnov–Smirnov (EPJC 79 (2019) 136) prove the facet prescription at leading order for each essential facet, and to all orders when a single facet contributes (positive polynomials). The general case is [C].

(4) Gardi–Herzog–Jones–Ma–Schlenk (JHEP 07 (2023) 197) relate regions of the on-shell expansion to Landau solutions and facets and prove commutativity for a class of regions. In Minkowski kinematics 'regions = lower facets' fails ([V]): new regions from dissected polytopes are needed from three loops (Gardi–Herzog–Jones–Ma, JHEP 08 (2024) 127). Becher–Hager–Jaskiewicz–Neubert–Schwienbacher (PRL 134 (2025) 061901) found a hidden three-loop active–active Glauber region that the automated finder Asy2.1 missed.

(5) The off-shell Sudakov regions example should be cited from Becher–Broggio–Ferroglia (LNP 896, 2015) §2.2, with the massive-exchange version in BBF §2.3 and Jantzen §6. It is not in Beneke–Smirnov 1998, who introduced the method for the threshold expansion.

**Literature check:** Smirnov CMP 134 (1990) 109. Jantzen JHEP 12 (2011) 076. Semenova–Smirnov–Smirnov EPJC 79 (2019) 136. Gardi et al. JHEP 07 (2023) 197 and JHEP 08 (2024) 127. Becher et al. PRL 134 (2025) 061901. Beneke–Smirnov NPB 522 (1998) 321. Becher–Broggio–Ferroglia Lect. Notes Phys. 896 (2015) §2.2–2.3.

## A11 — attribution — **refuted**

**Claim:** Glauber attributions: replace 'Cheng–Wu' by Aybat–Sterman eq. (14) and RS eqs. (9.1), (9.18)-(9.19), (11.12)-(11.13). RS is not a full proof ('far from a proof … even abelian'). RS makes no e⁺e⁻ statement. Usoft decoupling does not remove Glauber (RS §5.1). A–A Glauber = soft zero-bin.

**Printable version:** 

**Literature check:** Aybat–Sterman PLB 671 (2009) 46, eq. (14). Rothstein–Stewart JHEP 08 (2016) 025: §4, §5.1, §9.3, §10.1–10.3 with Fig. 29, §11.1, §12. Collins, Foundations of Perturbative QCD (CUP 2011; OA 2023), §14.4.5.

## A12 — attribution — **confirmed**

**Claim:** The dipole formula fails at three loops (Almelid–Duhr–Gardi 2016, abstract level); Caron-Huot rules it out from four loops. Graded [V] beyond two loops.

**Printable version:** For massless multi-leg amplitudes, the dipole formula (Becher-Neubert, PRL 102 (2009) 162001; Gardi-Magnea, JHEP 03 (2009) 079) gives the complete soft anomalous dimension through two loops (Aybat-Dixon-Sterman, PRD 74 (2006) 074004). At three loops there is a non-vanishing correction:
Delta_n^(3) = 16 f^{abe} f^{cde} [ sum T_i^a T_j^b T_k^c T_l^d F(rho_ikjl, rho_iljk) + perms - C sum {T_i^a, T_i^d} T_j^b T_k^c ],
with C = zeta5 + 2 zeta2 zeta3 and F a single-valued polylogarithm of weight five (Almelid-Duhr-Gardi, PRL 117 (2016) 172002, eqs. (7), (13), (14)).
- The correction is a constant for three coloured partons.
- For four or more partons it depends on conformal cross ratios.
- It preserves strict collinear factorization (eq. (17)).
This was confirmed independently by Henn-Mistlberger, PRL 117 (2016) 171601. Earlier, Caron-Huot (JHEP 05 (2015) 093, section 4.3, eq. (4.28)) found from BFKL dynamics in the Regge limit a non-dipole four-loop term, which 'appears to rule out the dipole conjecture starting from four loops'.
Grade: dipole formula beyond two loops [V].

**Literature check:** Yes. The result is entirely in the cited literature: ADG 2016, cross-checked by Henn-Mistlberger 2016; Caron-Huot 2015, section 4.3.

## A13 — attribution — **confirmed**

**Claim:** Collins 2011 (OA reissue, DOI 10.1017/9781009401845, not a new edition) quotes: §5.4.3 p. 110; §11.3.2 pp. 407-410 (BRST gap); §14.4 p. 553; §14.4.8 pp. 561-562; §14.6 pp. 569-570; §14.7 pp. 570-571 (NQS 'notable exception'); §15.9 p. 580. Hazards: D = ∂ + igA (eq. (2.2)); Fourier sign e^{+ik·b} (eq. (13.35)).

**Printable version:** Collins, Foundations of Perturbative QCD (CUP 2011). It was reissued Open Access in 2023, unrevised (edition 1), under DOI 10.1017/9781009401845. Likewise Renormalization (CUP 1984; OA reissue 2023, DOI 10.1017/9781009401807).
Verified locations:
- section 5.4.3, p. 110: no published complete proof of the Landau-equation results. It quotes ELOP p. 48, 'A proper proof needs the use of topology; ... We shall be content with plausibility arguments'. See Exercise 5.3, p. 159.
- section 11.3.2, pp. 407-410: the BRST classification is assumed for non-local operators (verbatim gap on p. 410). Triangular mixing (11.20) is on p. 412.
- section 14.4, p. 553: follows CSS 1988 'with some important improvements and with correction of errors'.
- section 14.4.7, p. 561: BBL phases 'get moved into the parton densities'.
- section 14.4.8, pp. 561-562: 'Issues remaining'.
- section 14.6, pp. 569-570: factorization guarantees only leading-power IR cancellation. 'One can imagine' terms of the form m^2/Q^2 x 1/eps (eq. 14.42). Keeping incoming heavy-quark masses in the hard scattering 'is a bad idea'.
- section 14.7, pp. 570-571: 'relative lack of detailed proofs'. The NQS 2005 work is a 'notable exception'; the printed sentence contains the typo 'One of notable notable exception', so quote only the fragment or mark [sic]. TMD factorization for hadron-hadron to dihadron 'appear[s] to fail' (Collins-Qiu 2007; Rogers-Mulders 2010).
- section 15.9, p. 580: 'I have not been able to penetrate the SCET literature to properly understand its rationale'.
Transcription hazards:
- Collins uses D = d + igA (eq. 2.2), so g_Collins = -g_ours. His Wilson line is P exp(-ig int n.A) (eq. 13.40).
- His TMD Fourier transform uses e^{+ik_T.b_T} (eq. 13.35a,b), with a normalization different from CS 1982.

**Literature check:** Not a new result; these are attribution and location checks of Collins 2011, and every location and quote has been confirmed in the book itself.

## A14 — attribution — **confirmed**

**Claim:** History: BBL 1981/1989 initial-state interactions; Bodwin 1985; LRS two-loop; BFT 1989; DFT 1980 / Di'Lieto 1981 (disagree on intermediate results) / Andrási on Bloch–Nordsieck failure, power-suppressed (FGT 1984; CCM 1986; CSS 1989 §10.2: m⁴/s²); BRS 1984; Frye 2019 (KLN); CSS 1986 'conjecture'; e⁺e⁻ first in TMD (TMD Handbook).

**Printable version:** Initial-state interactions:
- BBL 1981 (PRL 47, 1799): initial-state interactions 'violate the usual QCD factorization predictions ... in leading twist'.
- BBL 1989 (PRD 39, 3287): such interactions 'can invalidate the parton-model (factorized) form ... unless the beam energy is greater than a scale that grows with the length of the target'.
Factorization program and its checks:
- Bodwin 1985 (PRD 31, 2616; Erratum PRD 34, 3932) gives one- and two-loop examples and an all-order program.
- Two-loop spectator cancellations: Lindsay-Ross-Sachrajda (PLB 117 (1982) 105; NPB 214 (1983) 61).
- Eikonal-meson model: Brandt-Frenkel-Taylor (NPB 312 (1989) 589).
Bloch-Nordsieck failure for coloured initial states:
- Doria-Frenkel-Taylor (NPB 168 (1980) 93).
- Confirmed by Di'Lieto-Gendron-Halliday-Sachrajda (NPB 183 (1981) 223). They agree on the non-cancellation but disagree with several intermediate results, so the agreement is 'fortuitous'.
- Confirmed also by Andrasi et al. (NPB 182 (1981) 104).
- The non-cancelling terms are power suppressed: FGT (NPB 233 (1984) 307), to O(g^4) and argued to all orders; CCM (NPB 264 (1986) 588), 'higher twist type'.
- CSS 1989, section 10.2: relative order m^4/s^2 at two loops in DY.
- Basu-Ramalho-Sterman (NPB 244 (1984) 221): in a scalar-quark model at one loop, factorization holds at m^2/s and fails at m^4/s^2.
Other statements:
- KLN: a one-sided (initial or final) sum suffices. Finiteness generically/often requires forward scattering and interference with disconnected diagrams (Frye et al., PRD 99 (2019) 056015).
- CSS 1986 (NPB 263, 37) call heavy-quark production factorization a 'conjecture' requiring an all-order analysis.
- According to the TMD Handbook (arXiv:2304.03302, section 2.11.4), e+e- -> h1 h2 X was the first process with proven TMD factorization (Collins-Soper, NPB 193 (1981) 381; Erratum NPB 213 (1983) 545).

**Literature check:** Yes. All statements are attributions to the cited papers, and they have been verified in those papers' abstracts or texts.

## A15 — attribution — **confirmed**

**Claim:** Recalled DIS/DY attributions: DFLM 1988 (DIS-scheme gluon), AEM 1979 (DIS scheme), AM 1978 (F_L), BBDM (not opened), FP 1982, ESW (4.80). AEM worked in the DIS scheme, so the MS-bar Δ_qq̄ attribution needs care. First full O(α_s²) DY: HvNM 1991.

**Printable version:** DIS scheme:
- The DIS scheme for quark densities goes back to Altarelli-Ellis-Martinelli, NPB 143 (1978) 521 [Erratum NPB 146 (1978) 544] and NPB 157 (1979) 461.
- Fixing the DIS-scheme gluon by the momentum sum rule for all moments is the convention first introduced by Diemoz-Ferroni-Longo-Martinelli, ZPC 39 (1988) 21 (see Klasen-Kramer, PLB 386 (1996) 384).
Longitudinal structure function:
- The O(alpha_s) coefficient C_L^q = 2C_F z is first in Zee-Wilczek-Treiman, PRD 10 (1974) 2881 (moments; see also Calvo 1977; Nanopoulos-Ross 1975; Hinchliffe-Llewellyn Smith 1977).
- The x-space formula F_L = (alpha_s/4pi) x^2 int dz/z^3 [(16/3)F_2 + 8 sum e_q^2 (1-x/z) z g] is the Altarelli-Martinelli equation (PLB 76 (1978) 89).
BBDM:
- Bardeen-Buras-Duke-Muta, PRD 18 (1978) 3998, eq. (3.9): the MS coefficient B_2n. With the gamma0~(ln 4pi - gammaE) term removed, B_2n = 2 C^q_{2,N}(MS-bar, alpha_s/2pi normalization), exactly.
- Their eq. (3.8) gives C_L. Their eq. (4.12) gives the Bjorken sum rule int_0^1 dx [F1^{nubar p} - F1^{nu p}] = 1 - 8/((33-2f) ln(Q^2/Lambda^2)), i.e. 1 - (2/3) alpha_s/pi.
Drell-Yan:
- AEM worked with DIS-scheme densities. The MS-bar form of the DY coefficient appears later, e.g. in Furmanski-Petronzio, ZPC 11 (1982) 293 ('common factorization scheme').
- The first complete O(alpha_s^2) DY calculation is Hamberg-van Neerven-Matsuura, NPB 359 (1991) 343 [Erratum NPB 644 (2002) 403].
- Cite ESW only without an equation number unless it is checked.

**Literature check:** Yes, all of these are literature attributions. The ZWT priority is visible in BBDM's own citation (refs. 11-14) and in H1 2008. The DFLM gluon convention is attributed to DFLM by Klasen-Kramer 1996. The HvNM erratum is on INSPIRE.

## A16 — attribution — **confirmed**

**Claim:** e⁺e⁻: Poggio–Quinn give a physics-level proof; rigorous versions are LZ 1975, Lowenstein 1976, BM 1977 (BM II gauge scope to verify). r_2 = 1.9857 − 0.1153n_f (CKT 1979; Dine–Sapirstein 1979; Celmaster–Gonsalves 1980); general-group a² coefficient; ESW H(ε) unverified.

**Printable version:** Poggio-Quinn (PRD 14 (1976) 578) give a simple, physics-level proof: Green functions at non-exceptional Euclidean momenta in any renormalizable (not super-renormalizable) theory with massless particles are IR finite, and so are physical discontinuities.
The rigorous perturbative framework:
- Lowenstein-Zimmermann's IR power-counting theorem (CMP 44 (1975) 73) and Lowenstein's convergence theorems (CMP 47 (1976) 53).
- Breitenlohner-Maison's dimensional renormalization for massless theories: CMP 52 (1977) 39 (no super-renormalizable couplings) and CMP 52 (1977) 55 (mixed masses, IR degree >= 4).
- For gauge theories, BM II only names QED and Yang-Mills with vector-like fermions as examples. The absence of IR counterterms rests on the assumption that the Ward/Slavnov-Taylor identities are respected by dimensional regularization; ghosts are not discussed.
The O(alpha_s^2) coefficient of R_e+e- in MS-bar at mu^2 = s is
r_2 = -(3/32)C_F^2 + C_F C_A(123/32 - (11/4)zeta3) + C_F T_F n_f(zeta3 - 11/8) = 1.9857 - 0.1153 n_f.
References for r_2:
- Chetyrkin-Kataev-Tkachov, PLB 85 (1979) 277.
- Dine-Sapirstein, PRL 43 (1979) 668: 1.98 - 0.115 N_f in MS-bar.
- Celmaster-Gonsalves, PRL 44 (1980) 560: computed in the MOM scheme and agreeing with the former two.
- General group: Baikov-Chetyrkin-Kuhn, PRL 104 (2010) 132004.

**Literature check:** Yes, all attributions are standard. The r_2 general-group formula is printed in Baikov-Chetyrkin-Kuhn 2010. The limited gauge scope of BM II is visible directly in the paper.

## A17 — attribution — **confirmed**

**Claim:** c_pdf: Carlson locations Titchmarsh §5.81 and Boas Thm 9.2.1; refs from memory (CS 1982, AP, CFP, Catani–Seymour, Jaffe, Joglekar–Lee, ESW); MVV γ_ns^(0) normalization (factor 2).

**Printable version:** Carlson's theorem (F. Carlson, Uppsala thesis, 1914).
- Weaker form, Titchmarsh, The Theory of Functions, 2nd ed. (1939), section 5.81: if f is regular and O(e^{k|z|}) with k < pi for Re z >= 0 and f(n) = 0 for n = 0,1,2,..., then f is identically zero.
- Sharper form, with finite type in the half-plane and type < pi on the imaginary axis: Boas, Entire Functions (1954), Thm 9.2.1. This location is as cited by Waldschmidt, arXiv:2002.01223.
Standard references (bibliographic data verified on INSPIRE):
- Collins-Soper, NPB 194 (1982) 445.
- Altarelli-Parisi, NPB 126 (1977) 298.
- Gross-Wilczek, PRD 8 (1973) 3633 and PRD 9 (1974) 980.
- Georgi-Politzer, PRD 9 (1974) 416.
- Curci-Furmanski-Petronzio, NPB 175 (1980) 27.
- Catani-Seymour, NPB 485 (1997) 291 [Erratum NPB 510 (1998) 503].
- Jaffe, NPB 229 (1983) 205.
- Joglekar-Lee, Ann. Phys. 97 (1976) 160.
MVV convention: MVV (NPB 688 (2004) 101) expand in a_s = alpha_s/4pi with gamma = -int x^{N-1} P (eq. 2.7), and give gamma_ns^(0) = C_F[2(S1(N-1) + S1(N+1)) - 3] (eq. 3.4). This equals -2 x our gamma_qq(N) in the alpha_s/2pi normalization. MVV note that older literature includes an extra factor 2 in (2.7).

**Literature check:** Yes, these are bibliographic and location checks. The Titchmarsh location has been verified in the book itself; Boas only via Waldschmidt.

## A18 — attribution — **confirmed**

**Claim:** c_wilson: the GY original is symmetric and the one-sided form is Collins' (known via 1812.06468; original not seen). Combridge–Kripfganz–Ranft 1977; ESW Tab 7.1 / PS §6.1 numbers to verify; Weinberg 1965 B516; Collins page numbers to check.

**Printable version:** Grammer-Yennie decomposition:
- Grammer-Yennie (PRD 8 (1973) 4332) split the photon propagator/polarization sum into a G part and a K part. The K part is proportional to k_mu k_nu, i.e. pure gauge ('resembles a gauge transformation'). Its coefficient is built from the adjacent charged-line propagators, and all IR divergences sit in the K part.
- The one-sided form K_{mu nu} = k_mu w_nu/(k.w -/+ i0), with fixed auxiliary vector w, approximated momenta and a specified i0, is the generalization used by Collins (2011: section 5.5.6, p. 118; section 10.6, p. 345; section 11.9.3, p. 421; eqs. (11.4)-(11.6), p. 402). Collins states that it differs from GY's K term.
- The k <-> -k symmetrized coefficient b_k found in later papers (Indumathi 1998; Sen-Indumathi-Choudhury 2018) is described there as a modification of GY's original. Do not present it as GY's formula.
Other items:
- The spin- and colour-averaged tree result for qqbar -> gg is |M|^2/g^4 = (32/27)(t^2+u^2)/(tu) - (8/3)(t^2+u^2)/s^2 (Combridge-Kripfganz-Ranft, PLB 70 (1977) 234; PDG RPP eq. (51.9)).
- The soft-photon theorem location is Weinberg, Phys. Rev. 140 (1965) B516.

**Literature check:** Yes. The adaptation is stated by Collins himself (2011, pp. 118, 345, 421). The qqbar->gg formula is standard (CKR 1977; PDG). The caveat about the symmetrized b_k comes from Indumathi 1998, footnote 1.

## A19 — attribution — **confirmed**

**Claim:** TMD/Sivers: Ji–Yuan 2002 and BJY 2003 transverse links. The spectator Sivers function matches BCR 2008 (SivBM2-s-pl) with e_qe_s = −e_c². Lensing (Burkardt; Lu–Schmidt). u-quark Sivers sign recalled. T-odd FF universality (Collins–Metz; Meissner–Metz).

**Printable version:** Transverse gauge links at light-cone infinity are needed for gauge-invariant TMDs in light-cone gauge (Ji-Yuan, PLB 543 (2002) 66; Belitsky-Ji-Yuan, NPB 656 (2003) 165).
Scalar-diquark spectator model at one-gluon exchange:
f_1T^perp,SIDIS(x, k_T) = g^2 e_q e_s M(m + xM)(1 - x) / [4 (2pi)^4 k_T^2 (k_T^2 + L^2)] x ln((k_T^2 + L^2)/L^2) = -f_1T^perp,DY,
with L^2 = x lambda^2 + (1-x) m^2 - x(1-x) M^2.
- This agrees with Bacchetta-Conti-Radici, PRD 78 (2008) 074010, eq. (SivBM2-s-pl), for e_q e_s = -e_c^2 and e_c^2 -> 4pi C_F alpha_s. It is negative (Trento convention) for attractive final-state interactions.
Other statements:
- The sign correlation with the anomalous magnetic moment ('chromodynamic lensing'): Burkardt, PRD 66 (2002) 114005 and NPA 735 (2004) 185. Diquark-model kappa relations: Burkardt-Hwang, PRD 69 (2004) 074032; Lu-Schmidt, PRD 75 (2007) 073008; generalized by BCR 2008, eq. (Sivers-kappa).
- Phenomenologically f_1T^perp u (SIDIS, Trento) is negative and f_1T^perp d positive (BCR 2008 comparison with fits; Bury-Prokudin-Vladimirov, JHEP 05 (2021) 151, where the u function may change sign at large x).
- TMD fragmentation functions, including T-odd ones, are universal: Collins-Metz, PRL 93 (2004) 252001; Meissner-Metz, PRL 102 (2009) 172003.

**Literature check:** Yes. Everything is in the cited literature; the spectator formula is BCR 2008, eq. (SivBM2-s-pl). The only correction is bibliographic: the lensing/kappa references must be cited precisely.

## A20 — attribution — **confirmed**

**Claim:** Blueprint corrections: CdFR show no cancellation; DDIS has an r^- pinch and escapes via r^+ (Collins 1998 §III D); RM is double-Sivers; first SLL σ = −σ_0(2α_s/π)⁴ln⁵(Q/Q_0)π²Y(3N²−4)/480 (FKS, quoted); BNS: 2→0 from five loops, 'contrary to earlier statements'; CDF 'O(10)' via arXiv:1206.3955; H1 direct-photoproduction tension.

**Printable version:** (1) Catani-de Florian-Rodrigo (JHEP 07 (2012) 026) do not demonstrate a cancellation.
- The one-loop squared collinear factor P^(1) is strictly factorized. The two-loop P^(2) is not, and its factorization-breaking operator contributes only for n >= 5 QCD partons.
- This 'may invalidate the factorization theorem of mass singularities starting at the N3LO' unless other subprocesses cancel it.
- Forshaw-Seymour-Siodmok (JHEP 11 (2012) 066): in pure QCD the two-loop effect vanishes and violation is expected at three loops (two loops only with electroweak phases).
- Guan et al. (JHEP 01 (2025) 090): the effects appear to cancel in pure-QCD cross sections up to NNLO.
(2) In diffractive DIS the soft-gluon r^- contour is trapped at the target subgraph, which contains both initial- and final-state poles. Collins' proof (PRD 57 (1998) 3051, section III D) instead deforms r^+.
(3) Rogers-Mulders (PRD 81 (2010) 094006) give an explicit violation of generalized TMD factorization for a double transverse-spin (double-Sivers) asymmetry in a non-abelian spectator model. The unpolarized case is only indicated (Fig. 11). In the abelian model the two-gluon terms violate standard but not generalized TMD factorization.
(4) Super-leading logarithms in gaps-between-jets qq->qq (gap width Y):
- The lowest SLL appears at O(alpha_s^4) relative to the Born.
- Forshaw-Kyrieleis-Seymour (JHEP 08 (2006) 059, eq. (3.24)) give -sigma0 (2 alpha_s/pi)^4 ln^5(Q/Q0) pi^2 Y (3N^2-4)/480 for an out-of-gap gluon on one side (y > 0).
- Summing both sides gives -sigma0 (2 alpha_s/pi)^4 ln^5(Q/Q0) pi^2 Y (3N^2-4)/240 (FKS, JHEP 09 (2008) 128, eq. (2.22); Keates-Seymour, JHEP 04 (2009) 040, eq. (3.2)).
- Becher-Neubert-Shao (PRL 127 (2021) 212002) resum the tower alpha_s^{n+3} L^{2n+3}. They show that SLLs arise for 2->1 processes from four loops and for 2->0 processes (e.g. qqbar -> V with a jet veto; also relevant to Higgs production with a jet veto) from five loops. Earlier literature had stated that two coloured final-state partons are required.
(5) CDF's own summary (PRD 86 (2012) 032009) describes the Run I diffractive-dijet result as a breakdown of factorization by a suppression 'by a factor of O(10)' relative to HERA DDIS densities.
(6) H1 (EPJC 51 (2007) 549) find a suppression of about 0.5 for both direct and resolved diffractive photoproduction. ZEUS data are less suppressed (Klasen-Kramer, MPLA 23 (2008) 1885: global factors 0.42 for H1 vs 0.71 for ZEUS). Collins' proof would cover direct photoproduction, so this is an open tension.

**Literature check:** Yes. All items are in the cited papers. The factor-2 (one-sided versus two-sided) clarification of the FKS 2006 coefficient is stated by FKS themselves in JHEP 09 (2008) 128, eq. (2.22), and used by Keates-Seymour 2009.

## A21 — attribution — **confirmed**

**Claim:** Exclusive processes: PRL 84 (2000) 2589 is about decuplets; the pion-pole reference is FPPS PRD 60 (1999) 014010. LO factorization by LB, ER, DM, FJ; NLO kernel FGOC NPB 186 (1981) 429 and others; LB normalization recalled; soft overlap 1/Q⁴ quoted, not derived.

**Printable version:** PRL 84 (2000) 2589 (Frankfurt-Polyakov-Strikman-Vanderhaeghen) concerns decuplet baryons. The reference for hard exclusive pseudoscalar-meson production and the pion pole in the isovector Etilde (required by PCAC) is Frankfurt-Pobylitsa-Polyakov-Strikman, PRD 60 (1999) 014010.
Pion form factor:
- Leading-power factorization: Lepage-Brodsky (PLB 87 (1979) 359; PRD 22 (1980) 2157), Efremov-Radyushkin (PLB 94 (1980) 245), Duncan-Mueller (PLB 90 (1980) 159; PRD 21 (1980) 1636). Farrar-Jackson (PRL 43 (1979) 246) gave the normalized asymptotic behaviour.
- NLO hard-scattering corrections: Field-Gupta-Otto-Chang, NPB 186 (1981) 429; Dittes-Radyushkin, Sov. J. Nucl. Phys. 34 (1981) 293; Braaten-Tse, PRD 35 (1987) 2255; Melic-Nizic-Passek, PRD 60 (1999) 074004.
- Lepage-Brodsky normalize the DA as int_0^1 dx phi_LB = f_pi/(2 sqrt N_c) with f_pi ~ 93 MeV (PRD 22 (1980) 2157, eq. (2.24a); <0|J_W^mu|pi+> = sqrt2 f_pi p^mu). This equals F_pi/(2 sqrt N_c) when f_pi ~ 130 MeV is used.
- The soft (end-point) contribution is formally suppressed, entering at O(1/Q^4) (see Braun-Khodjamirian-Maul, PRD 61 (2000) 073004, eq. (25)). Isgur-Llewellyn Smith argued that it dominates at accessible Q^2.
Other items:
- Ji's sum rule: J^q = (1/2)[A^q(0) + B^q(0)] (PRL 78 (1997) 610, eq. (13)).
- DVCS factorization: Collins-Freund, PRD 59 (1999) 074009 (arXiv v2 with improved endpoint treatment).

**Literature check:** Yes, all of these are attributions verified in the cited papers. The 1/Q^4 citation is redirected to BKM 2000, which states the scaling explicitly.

## A22 — attribution — **confirmed**

**Claim:** SCET: PRD 66 054005 is power counting; the endpoint paper is PRD 67 071502. The BPS RPI footnote refers to Bauer–Stewart 2001, not MMPS 2002. BBNS–BPRS dispute: no verdict. BBL: D = ∂ + igA flips c_2-c_4, and M is the pole mass.

**Printable version:** Reference corrections:
- Phys. Rev. D 66 (2002) 054005 is Bauer-Pirjol-Stewart, 'Power counting in the soft-collinear effective theory'.
- The endpoint-singularity paper is Bauer-Pirjol-Stewart, 'Factorization and endpoint singularities in heavy to light decays', PRD 67 (2003) 071502.
Reparameterization footnote: in Bauer-Pirjol-Stewart, PRD 65 (2002) 054022, the footnote 'this global reparameterization invariance fixes the collinear action, except for the way in which i n.D appears' refers to the x-independent collinear transformations of Bauer-Stewart, PLB 516 (2001) 134. It does not refer to the Lorentz reparameterization invariance of Manohar-Mehen-Pirjol-Stewart, PLB 539 (2002) 59.
Charming penguins: the dispute is documented by the Beneke-Buchalla-Neubert-Sachrajda comment (PRD 72 (2005) 098501) and the Bauer-Pirjol-Rothstein-Stewart reply (PRD 72 (2005) 098502). It is reported here without a verdict.
NRQCD (Bodwin-Braaten-Lepage, PRD 51 (1995) 1125 [Erratum PRD 55 (1997) 5853]):
- BBL use D^mu = d^mu + i g A^mu. Transcribed to D = d - igA, the bilinear terms with explicit gE and gB (coefficients c2, c3, c4) change sign.
- In Gamma = sum 2 Im f_n / M^{d_n - 4} <O_n>, M is the heavy-quark (perturbative pole) mass, not the quarkonium mass.
- Decays: BBL sections II.F-G. Production: section VI.A.

**Literature check:** Yes. These are bibliographic and attribution checks; the footnote and conventions have been verified in the source texts.

## A23 — attribution — **confirmed**

**Claim:** REVIEW §11 'verify' list (21 items): Anikin–Zav'yalov; LZ NPB 86; Frye; Gaunt; Aybat–Sterman; FSS; CSS 1986; Collins 1998; DFT/Di'Lieto; Beneke–Braun 1995; BNRS/BNS; MP 2000; EMSS 2022; BVZ; Korchemsky–Sterman; Shifman; Graudenz; page data; FF z^{1−2ε}; gluon average; Collins chapters.

**Printable version:** Status of the REVIEW §11 items:
(1) Anikin–Zav'yalov, Ann. Phys. 116 (1978) 135–166: short-distance and light-cone expansions of T-products of currents are derived 'in the framework of the arbitrary order of the perturbation theory' (abstract). The class of theories covered is OPEN. Do not cite it as a QCD proof.
(2) Lowenstein–Zimmermann, NPB 86 (1975) 77–103: BPHZL scheme for the massless A^4 model, applied to the Goldstone and pre-Higgs models. The pre-Higgs model is an abelian massive-vector model (LZW, PRD 10 (1974) 2500). It does NOT cover gauge-fixed QCD.
(3) Frye et al., PRD 99 (2019) 056015: a sum over initial OR final states suffices. IR finiteness often needs forward scattering and the interference of disconnected with connected diagrams.
(4) Gaunt, JHEP 07 (2014) 110: shown, the CSS Glauber argument fails at two spectator–spectator Glauber gluons for hadronic E_T. Only suggested: leading-power factorization fails for E_T and for MPI-sensitive observables (beam thrust, transverse thrust). Disputed by SYZ 2018 (claim E36).
(5) Aybat–Sterman, PLB 671 (2009) 46–50: an outline, not a proof. It treats weighted transition probabilities with an incoming parton plus an incoming Wilson line; IR-safe weights may select jets or heavy coloured particles. The Glauber phases cancel only after inclusive final-state sums, and only if radiation at energies ~m^2/Q is summed inclusively in all directions. A single transverse scale is assumed, and key steps are deferred to a paper that never appeared.
(6) Forshaw–Seymour–Siódmok, JHEP 11 (2012) 066: for non-inclusive observables, pure-QCD collinear factorization is violated at three loops. Beyond QCD it can fail at two loops.
(7) Collins–Soper–Sterman, NPB 263 (1986) 37–60: heavy-particle production is argued only from low-order graphs and called a 'conjecture'. Grade [C].
(8) Collins, PRD 58 (1998) 094002: 'The power-suppressed corrections to the factorization formula are uniformly suppressed by a power of Λ/Q, independently of the size of heavy quark masses, M, relative to Q.'
(9) Doria–Frenkel–Taylor, NPB 168 (1980) 93, and Di'Lieto–Gendron–Halliday–Sachrajda, NPB 183 (1981) 223: two-loop non-cancellation for massive, colour-averaged initial quarks. The power statement is not in these papers. CSS 1989 review §10.2: the non-cancelling divergences in DY appear at the level m^4/s^2, and the cancellation holds at leading power. Frenkel–Gatheral–Taylor, NPB 233 (1984) 307: finite to O(g^4) except for power-suppressed terms.
(10) Beneke–Braun, NPB 454 (1995) 253: the leading renormalon of the resummed DY cross section cancels. Higher-twist corrections are expected at Λ^2/(Q^2(1−z)^2) for Q(1−z) > Λ. This is evidence, not a proof.
(11) BNRS JHEP 11 (2016) 019 [Erratum JHEP 05 (2017) 154]; BNS PRL 127 (2021) 212002.
(12) Mankiewicz–Piller, PRD 61 (2000) 074013.
(13) Ebert–Michel–Stewart–Sun, JHEP 07 (2022) 129.
(14) Braun–Vladimirov–Zhang, PRD 99 (2019) 014013.
(15) Korchemsky–Sterman, NPB 555 (1999) 335–351: shape functions organize the 1/(eQ)^n power corrections.
(16) Shifman, 'Quark–hadron duality', in Handbook of QCD vol. 3 (World Scientific 2001) 1447–1494.
(17) Graudenz, NPB 432 (1994) 351–376: NLO SIDIS with fracture functions.
(18) Page ranges: Li–Sterman NPB 381 (1992) 129–140; Soffer PRL 74 (1995) 1292–1294; Labastida–Sterman NPB 254 (1985) 425–440; Kodaira NPB 165 (1980) 129–140; Christ–Lee Phys. Rev. 143 (1966) 1310–1321.
(19) Collins 2011, eqs. (12.38) and (12.40): the integrated FF carries z^{n−3} = z^{1−2ε}; explicit in eq. (12.73).
(20) The standard MS-bar C_g = T_F[(z^2+(1−z)^2) ln((1−z)/z) − 1 + 8z(1−z)] (BBDM; MVV eq. (4.4)) corresponds to averaging the gluon over D−2 = 2(1−ε) polarizations. A 1/2 average adds T_F[z^2+(1−z)^2]. C_L^g is unchanged, and the shift cancels in Δ_qg − C_g.
(21) Collins chapters cited as ch. 5, 12, 13 and 14 are correct. The QCD DIS proof (B10) is ch. 8–11 (§§11.3, 11.9), not ch. 8–10.

**Literature check:** Anikin:1978tj (abstract); Lowenstein:1974qt; Lowenstein:1974wu (PRD 10 (1974) 2500, model classification); Frye:2018xjj §8; Gaunt:2014ska; Aybat:2008ct; Forshaw:2012bi; Collins:1985gm; Collins:1998rz; Doria:1980ak; DiLieto:1980nkq; Frenkel:1983di; CSS review hep-ph/0409313 §10.2; Beneke:1995pq; Becher:2016mmh; Becher:2021zkk; Mankiewicz:1999tt; Ebert:2022cku; Braun:2018brg; Korchemsky:1999kt; Shifman:2000jv; Graudenz:1994dq; Collins 2011 (DOI 10.1017/9781009401845) eqs. (12.38), (12.40), (12.73), §§11.3, 11.9; Vermaseren–Vogt–Moch hep-ph/0504242 eq. (4.4); BBDM PRD 18 (1978) 3998.

## A24 — attribution — **confirmed**

**Claim:** Misconception-box attributions: Collins 1993 vs 2002; Collins–Metz / Meissner–Metz; Ji–Yuan / BJY; Lam–Tung violated at O(α_s²); DFT / Di'Lieto; 't Hooft-model scaling (CCG, Einhorn; recalled); Burkardt–Koike δ(x) (recalled); CFP P^±.

**Printable version:** (1) Collins, NPB 396 (1993) 161–182, Appendix, argued that time-reversal invariance forbids the Sivers asymmetry. After Brodsky–Hwang–Schmidt, PLB 530 (2002) 99, Collins, PLB 536 (2002) 43, showed that the Wilson line invalidates that argument; T-reversal instead implies the sign reversal between SIDIS and DY.
(2) T-odd fragmentation functions are universal between SIDIS and e+e−. This is argued by Collins–Metz, PRL 93 (2004) 252001, and further supported by Meissner–Metz, PRL 102 (2009) 172003, who show that the partonic pole matrix elements vanish.
(3) The transverse gauge link at light-cone infinity: Ji–Yuan, PLB 543 (2002) 66; Belitsky–Ji–Yuan, NPB 656 (2003) 165.
(4) The Lam–Tung relation (PRD 21 (1980) 2712) has no O(α_s) correction. It is violated at O(α_s^2), i.e. at NLO for q_T ≠ 0, but only mildly: Mirkes, NPB 387 (1992) 3; Mirkes–Ohnemus, PRD 51 (1995) 4891; see Lambertsen–Vogelsang, PRD 93 (2016) 114013.
(5) Doria–Frenkel–Taylor, NPB 168 (1980) 93–110, and Di'Lieto–Gendron–Halliday–Sachrajda, NPB 183 (1981) 223–250: Bloch–Nordsieck cancellation fails at two loops for massive, colour-averaged initial quarks.
(6) In the 't Hooft model, exact Bjorken scaling in DIS, with the parton model reproduced exactly by the sum over hadronic states, is due to Einhorn, PRD 14 (1976) 3451–3471. Its published title is 'Confinement, form factors, and deep-inelastic scattering in two-dimensional quantum chromodynamics'. It builds on Callan–Coote–Gross, PRD 13 (1976) 1649–1669, who constructed the current amplitudes, showed asymptotic freedom and treated the vacuum polarization.
(7) Burkardt–Koike, NPB 632 (2002) 311–329: at O(α_s) on a massive quark target there are δ(x) terms in h_L and in e(x), but none in g_T.
(8) P^+_NS − P^−_NS starts at NLO with colour factor C_F(C_F − C_A/2), as in MVV eq. (4.7). The x-space kernels are from Curci–Furmanski–Petronzio, NPB 175 (1980) 27–92; the moments from Floratos–Ross–Sachrajda 1977 and González-Arroyo–López–Ynduráin 1979.
(9) NMC, PRL 66 (1991) 2712: S_G = 0.240 ± 0.016, below 1/3. In the quark-parton model S_G = 1/3 + (2/3)∫(ū − d̄), so 1/3 requires ū = d̄.
(10) Christ–Lee, Phys. Rev. 143 (1966) 1310–1321 (abstract level).

**Literature check:** Collins:1992kk (Appendix); Collins:2002kn; Brodsky:2002cx; Collins:2004nx; Meissner:2008yf; Ji:2002aa; Belitsky:2002sm; Lam:1980uc; Mirkes:1992hu; Mirkes–Ohnemus PRD 51 (1995) 4891; Lambertsen:2016wgj §1; Doria:1980ak; DiLieto:1980nkq; Callan:1975ps; Einhorn:1976uz; Mondejar–Pineda 0901.3113; Burkardt:2001iy; Curci:1980uw; Floratos:1977au; MVV hep-ph/0403192 eq. (4.7); NewMuon:1991hlj; NewMuon:1993oys; Gottfried:1967kk; Christ:1966zz.

## A25 — attribution — **confirmed**

**Claim:** NQS gauge completion [P]; Bodwin et al. 2020 two-loop universality, differing from NQS in some respects; η_c tension (BHK vs Han et al. / Zhang et al.); EW Bloch–Nordsieck violation (CCC 2000); BERV 2019 non-factorizable EW; DGOPS double DY; EGS conditional on Glauber; Gamberg preprint.

**Printable version:** NRQCD production. NQS (PLB 613 (2005) 45; PRD 72 (2005) 114012; PRD 74 (2006) 074007) find NNLO infrared poles in gluon fragmentation that conventional octet operators do not match. Operators with Wilson lines restore factorization at NNLO: first to O(v^2), then, for the octet→singlet transition, to all orders in v. At higher orders, 'in the absence of special cancellations', further non-local operators may be needed [P]. Bodwin–Chung–Ee–Kim–Lee (PRD 101 (2020) 096011) did a covariant two-loop calculation. They find the IR divergences independent of the Wilson-line direction. Their results differ in some respects from NQS, and they identified the sources of some of these differences. Both calculations are consistent with NRQCD factorization, but the underlying principle is unknown [P].
η_c. Butenschoen–He–Kniehl (PRL 114 (2015) 092004) say η_c data challenge NRQCD factorization. Han et al. (PRL 114 (2015) 092005) and Zhang et al. (PRL 114 (2015) 092006) find the data consistent with NRQCD.
Electroweak. Ciafaloni–Ciafaloni–Comelli (PRL 84 (2000) 4810): electroweak double logs violate Bloch–Nordsieck for non-singlet initial states [V]. Baumgart–Erdoğan–Rothstein–Vaidya (PRD 100 (2019) 096008): leading-power non-factorizable electroweak corrections, starting at α_s^2 α_W^2 log^4(Q^2/M_W^2), for observables that measure weak charge [V], as computed there.
DPS and NLP TMDs. Diehl–Gaunt–Ostermeier–Plößl–Schäfer (JHEP 01 (2016) 076): Glauber cancellation for double DY at all orders, both integrated and q_T-differential [A]. Ebert–Gao–Stewart (JHEP 06 (2022) 007 [Erratum 07 (2023) 096]): conditional on a Glauber assumption [A](cond.). Gamberg–Kang–Shao–Terry–Zhao, arXiv:2211.13209: unrefereed as of 2026-10-10 (†).

**Literature check:** Nayak:2005rw; Nayak:2005rt; Nayak:2006fm; Bodwin:2019bpf; Butenschoen:2014dra; Han:2014jya; Zhang:2014ybe; Ciafaloni:2000df; Baumgart:2018ntv; Diehl:2015bca; Ebert:2021jhy; Gamberg:2022lju (arXiv v2, no journal-ref).

## A26 — attribution — **confirmed**

**Claim:** Grade conflicts: OTHERS QCD OPE [R] and Collins [R]† vs FINAL_OUTLINE §0.9 item 4; YZLIU [R]-level vs LAMET [A] for renormalizability; LAMET [R]_2L with fitted constants vs [P]; the reference's B′ for DY rests on the R-S1 residual.

**Printable version:** There were five grade conflicts; the binding resolutions in spec_v2 are:
(1) The perturbative OPE for QCD with quarks is [A], not '[R] via classical results'. Collins 2020 Theorem 1 is [A] because its proof exists only in a preprint, not [R]†.
(2) Multiplicative renormalizability of space-like Wilson-line quark bilinears (prop:lattice-renormalizability) is [A], not [R]. The space-like extension of the auxiliary-field/BRST proof is asserted, and the diagrammatic proof counts only superficial degrees.
(3) Threshold factorization of the quasi-PDF kernel is [A]. Its NNLO check, 41 singular terms with two constants c_a and c_H extracted from the comparison, is [P], not [R]_2L. Only c_H is cross-checked independently, by del Río–Vladimirov 2023.
(4) Gordan's alternative (lem:appD-gordan) stays an untagged mathematical lemma. The constructive min-norm proof (lem:front-min-norm) is added in Ch24.
(5) The reference document's B′ grade for DY rested mainly on the two-Glauber residual, which is an artefact of strict truncation (R-S1/N01). DY factorization is therefore [A], with the open App. O assumptions named.

**Literature check:** Internal files: frontier/others/OTHERS.md §1.2, §1.7, §2.7; frontier/yzliu/YZLIU.md §3.C2, §3.E2; frontier/lamet/LAMET.md §0.2 row 18, §3.2, §4.5, §6.1; spec/FINAL_OUTLINE.md §0.9 item 4; spec_v2/FINAL_OUTLINE_v2.md §0.8 (D3, MD14), Ch22 prop:lattice-renormalizability, Ch23 thm:yzliu-threshold and prop:yzliu-threshold-nnlo; spec_v2/REFS_NOTES_v2.md rule A26; refdoc/REFDOC_ANALYSIS.md §0 item 1, ERR-S1, line 1051; verify/claims/batch_N01_s1.md (N01, N02). Literature behind (5): Meggiolaro 1997, per batch_N01_s1.

## A27 — attribution — **confirmed**

**Claim:** Sivers sign: COMPASS 2017/2024 consistent; STAR χ² 7.4/6 vs 19.6/6 (small evolution assumed); BPV 2021 cannot exclude the same sign; EKT tension. BMP 2009 disagree with Kang–Qiu twist-3 evolution; sign mismatch addressed by JAM 2020. Collins 1998: remainders uniform in m/Q.

**Printable version:** Sivers sign change: consistent with the data, not decisive.
- COMPASS 2017 (PRL 119 (2017) 112002): the sign is consistent with the reversal 'within the experimental uncertainties'.
- COMPASS final 2015+2018 data (PRL 133 (2024) 071902): 'consistent with the fundamental QCD prediction of a sign change'.
- STAR (PRL 116 (2016) 132301), 2011 data with 25 pb^-1: a fit to the W± asymmetries in the Kang–Qiu model without TMD evolution gives χ²/ndf = 7.4/6 with the sign change and 19.6/6 without. This favours the sign change only 'if TMD evolution effects are small'.
- Bury–Prokudin–Vladimirov (PRL 126 (2021) 112002): a fit without the sign change shows DY–SIDIS tensions, yet has χ²/N_pt = 1.0 and 'cannot exclude the same sign'. The sign of the sea-quark Sivers function is central.
- Echevarria–Kang–Terry (JHEP 01 (2021) 126): tension with the RHIC W/Z data.
Twist-3 evolution:
- Braun–Manashov–Pirnay (PRD 80 (2009) 114002 [Erratum PRD 86 (2012) 119902]) disagreed with Kang–Qiu (PRD 79 (2009) 016003). The results were reconciled in Kang–Qiu, PLB 713 (2012) 273; see also Schäfer–Zhou, PRD 85 (2012) 117501.
- Kang–Qiu–Vogelsang–Yuan (PRD 83 (2011) 094001) found a sign mismatch between the Sivers function and the twist-3 function T_F. The JAM 2020 global analysis (PRD 102 (2020) 054002) 'further indicates a resolution'. In that fit the Collins-type term dominates A_N.
Heavy quarks: Collins (PRD 58 (1998) 094002) states that 'The power-suppressed corrections … are uniformly suppressed by a power of Λ/Q, independently of the size of heavy quark masses, M, relative to Q.'

**Literature check:** COMPASS:2017jbv; COMPASS:2023vqt; STAR:2015vmv (text and Fig. 4); Bury:2020vhj (p. 4); Echevarria:2020hpy; Braun:2009mi (+ erratum PRD 86 (2012) 119902); Kang:2008ey; Kang:2012em (PLB 713 (2012) 273); Schafer:2012ra (PRD 85 (2012) 117501); Kang:2011hk; Cammarota:2020qcw (§1); Collins:1998rz.

## A28 — attribution — **confirmed**

**Claim:** NLP endpoint factorization: endpoint divergences generic [R] (LN 2020; BBJV 2020); h→γγ theorem [A], with refactorization conditions 'proven' within SCET (LMNW §3); threshold DY bare d-dimensional [P]; LL resummation [A]; BSS 2026 [A]† (preprint).

**Printable version:** Endpoint divergences:
- Endpoint-divergent convolutions occur at NLP. In explicit examples, MS-bar renormalization of the individual functions does not remove them: h→γγ (Liu–Neubert, JHEP 04 (2020) 033) and threshold DY (BBJV, JHEP 07 (2020) 078). This is [R] in the sense of explicit examples.
h→γγ via a b-quark loop:
- The renormalized endpoint-factorized theorem holds to all orders [A] (LN 2020; Liu–Mecaj–Neubert–Wang, JHEP 01 (2021) 077).
- Its two D-dimensional refactorization conditions were verified at NLO and conjectured in LN 2020 (§5.2). LMNW prove them with SCET methods: the first in §3.1 (eq. (3.5)), the second in §3.2 (eqs. (3.12)–(3.14), via the discontinuity of the soft function). The theorem therefore rests on SCET's own assumptions.
Other processes:
- gg→h via light quarks in the RBS scheme: [A] (Liu–Neubert–Schnubel–Wang, JHEP 06 (2023) 183).
- Threshold DY at NLP: the bare d-dimensional factorization fails if d→4 is taken before the convolution [P] (BBJV 2020).
- LL resummation at NLP for DY (JHEP 03 (2019) 043), gg→H (JHEP 01 (2020) 094), off-diagonal DIS (JHEP 10 (2020) 196) and 'gluon thrust' (JHEP 07 (2022) 144): [A] at LL only.
- NLP DIS and PDF factorization (Beneke–Schnubel–Szafron, arXiv:2608.25502 v1, unrefereed): the threshold PDF becomes a two-scale object at NLP. LL resummation is done both in MS-bar and in an endpoint scheme, with the relation between the schemes given to double-log accuracy [A]†.
Critiques:
- Bodwin et al. examine individual ingredients: PRD 104 (2021) 016010; PRD 104 (2021) 116025; PRD 109 (2024) 056020; arXiv:2512.11647 (unrefereed).

**Literature check:** Liu:2019oav §5.2 eqs. (54)–(55); Liu:2020wbn §3.1 eq. (3.5), §3.2 eqs. (3.12)–(3.14), §7; Liu:2022ajh; Beneke:2019oqx; Beneke:2018gvs; Beneke:2019mua; Beneke:2020ibj; Beneke:2022obx; Beneke:2026miy (arXiv v1, §7); Bodwin:2021cpx; Bodwin:2021epw; Bodwin:2023asf; Bodwin:2025zzi (arXiv v3).
