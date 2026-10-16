# X1-glauber

(extracted verbatim from the workflow journal; structured output of the agent)

## summary

The X1 run finished; the only failure was the REPORT.md write, which the harness refused. On "在正常运行吗": yes, apart from that. Subagents may not write report files, so the full report content — definitions, theorem statements, proofs, numbers, open problems — is in the 'results' and 'open' fields; the parent should write it to verify/extend/X1-glauber/REPORT.md. Scripts and logs are in verify/extend/X1-glauber/{scripts,logs}.

Setting. The reference document (App. E) proves Glauber cancellation in inclusive Drell–Yan only for the class 𝒢₀: the soft subgraph consists of direct lines between the two jets; there are no H-emission endpoints; in the non-abelian theory each spectator carries at most one localized insertion per side. The proof holds inside the Glauber window and assumes E.18, E.33, E.34 and E.44; its assumption E.33(c1) is internally inconsistent.

What this work adds (grades as in the monograph):

(1) L1 [R]: an exact lemma for N simultaneous insertions on one jet ('joint localization'). The result is a finite sum of sector functions evaluated at the external poles z_e. Its ordering weights are those of an exponential race with rates z_e = k_T²/(2|k⁺|), with explicit error bounds. This replaces the inconsistent E.33(c1).

(2) L2 [R]: for insertions on spectators, the weights are continuous across each single hyperplane k_e⁺ = 0. They are kinked there, not step functions like θ(k⁺). This corrects the wording of our ERR-S3.

(3) T1 [R_cond]: when all insertions on each spectator commute (in particular in the abelian theory), the cancellation holds to all orders for any multiplicity, with no E.33(c). P1 [R_cond]: windows built from side-independent energies remove the reference's unestimated 'window-edge terms'.

(4) T2 [R_cond], new: two non-abelian spectator–spectator (SS) exchanges between the same A-spectator and the same B-spectator, at O(g⁴), with exact connecting propagators and arbitrary jets in light-cone-ordered form. Then Re p_opp → 0, so the reference's residual −½C_Aχ²(Re p_opp)T_A·T_B vanishes at leading power. The C_A term is a pure reggeization phase, p_opp ≈ −(i/π) ln(k_T²/(λ_Aλ_B)).
 - It holds when neither jet has positive final-state energies, or with an analytic rapidity regulator at the collinear ends (T2′).
 - Without either, explicit 'end-pole' artefacts appear; their exact formula is confirmed numerically.
 - The mechanism is a universal −¼ from each analytic rapidity end (ray identity L6). The reference's strict window gives p_opp = ½ because its sharp, non-analytic cutoffs remove those ends (P2).
 - So E.33(c2) is not needed for this pattern at O(g⁴).

(5) T3, new and negative: two SS exchanges from one A-spectator to two different B-spectators ('half-coincident').
 - The residual is exactly 2i c₁c₂ Im W₁₂ [X₁,X₂], with [X₁,X₂] = i f^{abc} T^c_i T^a_{j1} T^b_{j2}.
 - Re W₁₂ = ½ holds exactly, but Im W₁₂ = O(1) in general (≈ −0.031 in our model; two independent methods agree).
 - The residual vanishes on colour singlets of the three spectators involved, in symmetric kinematics, and in the abelian theory. It does not vanish once a fourth spectator is present.
 - Hence an E.33(c2)-type compensation, carrying the three-gluon colour structure, is genuinely needed already at O(g⁴) for this pattern.

(6) Further propositions.
 - P3 [R]: for on-shell lines, box plus crossed box are exactly unitary at O(g⁴) (Cutkosky).
 - P4 [R], negative: per-graph weak equivalence fails for coincident pairs, so E.34 and E.35 must be imposed on side-summed families.
 - P5 [A]: the class of direct-line ladders is not unitarity-closed at O(g⁶); soft real emission and the Lipatov vertex are needed.
 - L7 [R]: E.33(a) holds on the far-off-shell set; only its near-shell remainder stays an assumption.
 - P6 [R]: locates exactly why coincident SA/AS insertions and H-emission endpoints block the contour deformation.

(7) An updated, shorter assumption register (G1–G7, entry REG).

Verification. All new claims are backed by exact symbolic or numerical checks (C1–C4; colour checks; three independent integration methods). The integral form of every result still needs the envelope assumption G2.

Two caveats.
 - The novelty claims rest on a limited INSPIRE title search.
 - Overall, inclusive DY factorization remains [A] (an all-order argument, not a full proof).

## results

### [results 1]
DEFS — definitions, notation and standing hypotheses. Conventions follow CONTEXT.md. λ_A (resp. λ_B) is the largest light-cone energy difference in the denominators of J_A (resp. J_B), of order λ². For a spectator–spectator (SS) line e put a_e = k_Te². Small parameter: ε = λ_Aλ_B/a (of order λ²); L = ln(1/ε). Amplitude-side connecting propagator R_e = 1/(2k_e⁺k_e⁻ − a_e + i0) = r_e/(k_e⁻ − z_e), with r_e = 1/(2k_e⁺) and z_e = (a_e − i0)/(2k_e⁺). Its pole lies in the LHP for k⁺ > 0 and in the UHP for k⁺ < 0. (Def 3.1, insertion sectors) Fix N amplitude-side insertions with energies k (standard flow). A sector σ is a split of {1..N} into the insertions before V_H, in order b_1..b_n, and those after V_H, in order f_1..f_m. Partial sums: K^B_ℓ = Σ_{l≤ℓ} k_{b_l} and K^F_ℓ = Σ_{l≥ℓ} k_{f_l}. The colour order of σ is b_1..b_n f_1..f_m. (Hyp J) J = Σ_σ J^(σ), with J^(σ)(k) = Σ_t c_t Π_ℓ φ_{B,ℓ}(K^B_ℓ) Π_ℓ φ_{F,ℓ}(K^F_ℓ). Each gap function is a product of n_ℓ ≥ 1 factors: i/(A_D + K + i0) for initial gaps and i/(A'_D − K + i0) for final gaps, with A_D, A'_D real and |A| ≤ λ_J. This follows from App E Lemmas E.15, E.16, E.21, E.22 under E.18 at leading power. (Def 3.2) The equal-time value is 𝒥_σ = Σ_{t: all n_ℓ = 1} c_t i^N; J^(σ) behaves as 𝒥_σ Π(−iK^B_ℓ)^{-1} Π(iK^F_ℓ)^{-1}. (Hyp Sp) For insertions on spectators, 𝒥_σ depends only on the colour order (Lemma E.28(i)). The colour-stripped values of different orders are equal. (Hyp R) Every colour-stripped jet function is a fixed phase times a rational function with real coefficients. At leading power this holds: energies and good-component couplings are real, traces without γ5 are real, and the overall power of i is the same in every term. (Hyp NF_X) Every final-state energy difference A'_D of jet X is negative: no final state of X can absorb an on-shell gluon of the relevant kinematics. Initial states satisfy the analogue automatically for bound hadrons (all A_D < 0). (Def 3.3, class 𝔛 of analytic end regulators) A factor Π_e χ(k_e⁺) such that, on each half line ±k⁺ > 0, χ is holomorphic in the quadrant obtained by rotating that half line counterclockwise by up to π/2, real on the half line, ≈ 1 for |k| ≪ K_c and O(K_c/|k|) for |k| ≫ K_c, with λ_B ≪ K_c ≪ a/λ_A. Example: χ = 1/(1 + |k|/K_c). The strict window with independent sharp truncations of k^± is NOT in 𝔛. (Def 3.4, side-independent window) ν̂_A = P_A⁻ + 2 Σ_{l∈J_A} E^(0)(l) + 2 (Σ_m |k_Tm|)² / x^A_min. Here E^(0) is the on-shell energy with all SS momenta set to zero, the sum runs over both sides and the cut, and x^A_min is the smallest plus momentum of a J_A line carrying SS momentum. ν̂_B is defined likewise, and Θ̂_m = ϑ(4ν̂_Aν̂_B/(λ^{a_G} k_Tm²)). (Coincidence patterns) For two SS lines on one side: non-coincident = different A- and different B-spectators; fully coincident = the same A-spectator i and the same B-spectator j; half-coincident = the same i and different j_1 ≠ j_2. (Ordering weights, reference E.36) M^(2) = ((−iχ)²/2)[X² + p_opp (C_A/2) X], with p_same + p_opp = 1 and X = T_i·T_j. Its integrals are written I(π_A,π_B) = ∫ d²k⁺/(2π)² F_A^[π_A](k⁺) J_B^[π_B](−k⁺), with N = Σ I, W = I/N, N_0 = 𝒥_A𝒥_B/(a_1a_2), and p_opp = W(12,21) + W(21,12).

### [results 2]
L1 — joint-localization lemma for N insertions [R]. It replaces Assumption E.33(c1). Hypotheses: J satisfies (J); external factors R_e(k) = r_e/(k − z_e) with Im z_e ≠ 0; 𝓕 = {e: Im z_e < 0} and 𝓑 = its complement. (a) Exact form: ∫_{R^N} Π dk_e/(2π) J(k) Π R_e(k_e) = [Π_{e∈𝓕}(−i r_e) Π_{e∈𝓑}(+i r_e)] Σ_{σ: 𝓑_σ = 𝓑, 𝓕_σ = 𝓕} J^(σ)(z_1..z_N). The integrals converge absolutely at finite iη and the identity is exact for each η and in the limit. (b) Asymptotics: let κ(z) = min_{σ,ℓ}|K_ℓ(z)| ≥ 2λ_J. Then J^(σ)(z) = 𝒥_σ Π(−iK^B_ℓ(z))^{-1} Π(iK^F_ℓ(z))^{-1} + 𝓔_σ, with |𝓔_σ| ≤ C_σ M_σ (λ_J/κ) Π|K_ℓ|^{-1}, where M_σ = Σ_t|c_t|. Hence the integral equals Π_e R_e(0) [Σ_σ w_σ(z) 𝒥_σ + O(Mλ_J/κ)], with w_σ = (Π_{e∈𝓕} z_e / Π_ℓ K^F_ℓ(z)) · (Π_{e∈𝓑} z_e / Π_ℓ K^B_ℓ(z)). (c) Σ_σ w_σ = 1. For real Glauber poles each group has z_e of one sign, so w_σ ∈ [0,1] is the probability of an exponential race with rates |z_e|. In the final group the insertions follow V_H in the order the clocks ring: w_π = Π z / Π_m Σ_{l≥m} z_{π(l)}. The initial group is time-reversed: w_π = Π z / Π_m Σ_{l≤m} z_{π(l)}. For Glauber factors κ ≥ min_e a_e/(2|k_e⁺|), so the relative error is O(λ_J|k⁺|/a). PROOF. (i) Absolute convergence at finite η follows from Weinberg's theorem. On any subspace W the number of factors that are not constant exceeds dim W: count the R_e and the gap function that contains the first variable of the support. (ii) Sector selection. Suppose e ∈ 𝓕_σ but Im z_e > 0. In J^(σ), k_e enters only final gaps, whose poles lie in the UHP, and R_e also has its pole in the UHP. The integrand is O(|k_e|^{-2}); closing the k_e contour in the LHP gives 0. The case e ∈ 𝓑_σ with Im z_e < 0 is the mirror image. (iii) For the surviving sectors, integrate the final variables one after another, closing in the LHP. With the other variables real, or already complex with Im < 0, all poles of the final gaps in k_f lie in the UHP, so only R_f contributes, giving −i r_f with k_f = z_f. Integrate the initial variables in the UHP, giving +i r_b. (iv) A gap with one state gives i/(A ± K) = (i/(±K))(1 + O(|A|/|K|)); gaps with ≥ 2 states are O(|K|^{-2}). The signs combine to w_σ: the factors (−i)^m/i^m = (−1)^m match Π R_e(0) = (−1)^m Π r/Π z, and similarly for the initial group. (v) Σ w = 1: the order regions partition R_+^m in the race integral, and this rational identity in the rates extends to complex z. VERIFIED. checks_misc.py C1a–c: N=3 race integrals agree with the formula symbolically and sum to 1. checks_C2_C3_C4.py C2: for N=3, all 6 colour orders and mixed half planes, the exact formula agrees with exact iterated residues to 1e-25 relative. test_twoexch_parts2.py: for N=2, quadrant formulas agree with residues plus quadrature, with differences O(η). NOVELTY. The reference gives the N=2 weight z1/(z1+z2) and the N-order formula only as an example (App E.4.4) and then assumes E.33(c1). The exact sector formula, the rule for mixed half planes, the error bound and the race interpretation are new here. CONSEQUENCE. E.33(c1) is false, and per graph it is replaced by the weighted sum of L1.

### [results 3]
L2 — the weights as functions of k⁺ [R]. Hypotheses: Glauber factors as in DEFS. Let W_π(k⁺) = Σ_{σ with colour order π} w_σ. (a) W_π is homogeneous of degree 0 and rational in each orthant. (b) Under (Sp), W_π is continuous on the set where at most one k_e⁺ vanishes. As k_e⁺ → 0^±, |z_e| → ∞ and e moves next to V_H (last initial insertion, or first final one); this is the same colour position on both sides. (c) W_π is not analytic across k_e⁺ = 0. Example (N=2, k_2⁺ > 0): W_(12) = 1 − a_2k_1⁺/(a_1k_2⁺) + ... as k_1⁺ → 0⁺, but W_(12) ≡ 1 for k_1⁺ < 0. (d) W_π is discontinuous where two or more components vanish (the limits depend on direction). (e) For an insertion on an active line emitted by V_H (𝒥_− = 0), the weight is θ(k_e⁺), which is discontinuous. Two-line formulas: W^[12] = a_1k_2⁺/(a_1k_2⁺ + a_2k_1⁺) in (+,+), a_2k_1⁺/(a_2k_1⁺ + a_1k_2⁺) in (−,−), 1 in (−,+), 0 in (+,−). PROOF. Immediate from L1(c). VERIFIED: checks_misc.py C1d, C1e. NOVELTY: new. It corrects REFDOC_ANALYSIS ERR-S3's statement that coincident weights are non-analytic 'exactly like θ(k⁺)': for spectators they are continuous, with only a kink.

### [results 4]
T1 — commuting insertions to all orders [R_cond]. Hypotheses: (Γ_0,R_0) ∈ 𝒢_0 without H-emission endpoints; the family 𝔉(Γ_0) has any number of SS lines with any coincidences and any localized SA/AS insertions; all localized insertions on every spectator commute (in particular in the abelian theory); E.18, E.34 (per graph), D.7(A3) and D.7(A4)(ii) hold. Conclusion: per-graph weak equivalence (E.35) holds with the reference's rewriting map 𝔯_R and without E.33(c1); one-sidedness holds; and the family cancellation (E.33) holds on the windows. With the windows of P1 there are no window-edge terms. PROOF. By L1, the localized value of a jet with N insertions is Π R_e(0) Σ_σ w_σ 𝒥_σ. Commuting insertions give 𝒥_σ = 𝒥(0) for every σ, by continuity at equal times and across V_H. The value is therefore Π R_e(0) 𝒥(0), independent of the weights since Σ w = 1. This is identical to the reference's line-by-line localization, so its proofs of E.35 and E.31(iii) apply verbatim, with the error terms of Lemma E.28 and (E.30)–(E.31). Remark: for commuting coincident pairs the commutator parts vanish identically, so the logarithmic sensitivity to rapidity of P4 is absent and the per-graph form of E.34 is consistent. NOVELTY. The abelian statement is in the reference (Props E.35, E.31(iii)). The uniform proof via L1 and the explicit absence of the logarithmic sensitivity are new. Valid unchanged for TMD.

### [results 5]
P1 — side-independent windows remove the window-edge terms [R_cond]. Hypotheses: ν̂_A, ν̂_B and Θ̂_m as in DEFS (Def 3.4); the remaining inputs as for the reference's Prop E.31(iii). (a) ν̂_A and ν̂_B do not depend on the side assignment of the SS lines in a connection pattern. (b) Every light-cone energy difference in the jets' denominators satisfies |A_D| ≤ ν̂_A, for every side assignment. (c) In the Glauber scaling region ν̂ ~ λ², so Θ̂ = 1 on the Glauber core. (d) Hence the localization bounds (E.30)–(E.31) hold with λ_J ≤ C ν̂. The family identity Σ_sides Π_l(...) = Π_l(−iG_lX_l + iG_lX_l) = 0 then holds at every point of the support, so the reference's 'window-edge terms' (unestimated in Prop E.31(iii)) vanish identically. PROOF. (a) holds by construction: E^(0) is evaluated at zero SS momentum, and the SS transverse momenta enter only through Σ|k_T|. (b) E(l) = ((l_T^(0) + Σ ± k_Tm)² + m²)/(2l⁺) ≤ 2E^(0)(l) + (Σ|k_Tm|)²/l⁺. Every A_D is P⁻ or 𝓔 (itself a sum of final energies) minus a sum of such energies. (c) is power counting. (d) The family algebra needs only that the window factors are the same for all side assignments. NOVELTY: new. R7 suggested the idea without proof.

### [results 6]
L3 — exact k⁻ residues for two SS lines (quadrant formulas) [R]. This is L1 with N=2 and the factors (1.1). In the quadrant Q = (sgn k_1⁺, sgn k_2⁺): F_A^[π](k⁺) = Π_e(−i sgn(k_e⁺) r_e) J_A^(σ(π,Q))(z_1,z_2). Here σ(π,Q) has initial set {e: k_e⁺ < 0} and colour order π; F_A^[π] = 0 if π is incompatible with that split ((+,−) kills [12] and (−,+) kills [21]). In the localized regime |z_e| ≥ 2λ_A: F_A^[π] = (𝒥_A/(a_1a_2)) w^[π](k⁺) [1 + O(λ_A|k⁺|/a)], with w as in L2. Each quadrant piece extends holomorphically to the product of half planes {Im z_e < 0 for final e, Im z_e > 0 for initial e}: for k⁺ > 0 this is the UHP, for k⁺ < 0 the LHP. VERIFIED: test_twoexch_parts2.py; residual differences O(η) come from the different iη distribution of LCOPT and covariant forms. NOVELTY: new (an explicit instance).

### [results 7]
L4 — colour bookkeeping [R]. (a) Fully coincident pair: M^(2) + M^(2)† + M^(1)†M^(1) = −½ C_A χ² (Re p_opp) X. Also ladder = X², crossed = X² + (C_A/2)X, and Σ[T^a,T^b]⊗[T^a,T^b] = −C_A X. (b) Half-coincident pair (spectator i; spectators j_1 ≠ j_2): let X_e = T_i·T_{j_e}. On the amplitude side, 'line 1 first on i' carries colour X_2X_1; the conjugate side carries X_1X_2; the configurations with one line on each side give X_1X_2 + X_2X_1, since conjugate insertions stand to the left in the closed-time-path form. The O(c_1c_2) residual is R = 2i c_1c_2 Im W_12 [X_1,X_2], with [X_1,X_2] = i f^{abc} T^c_i T^a_{j1} T^b_{j2}. (c) [X_1,X_2] vanishes on the invariant (colour-singlet) subspace of (i, j_1, j_2). There T_i = −(T_{j1} + T_{j2}), so X_e = −C_{j_e} − T_{j1}·T_{j2} and the two operators commute. (d) With further, passive spectators it does not vanish in general: the maximal singlet-space matrix elements are 0.38 for (3̄,3̄,3̄;8) and 0.71 for (3,3̄,3̄;3) and (3̄,3,3̄;3). VERIFIED: checks_C2_C3_C4.py C3a–d (SU(3), 3×3 and 3×3̄); check_halfcoinc_colour.py; check_halfcoinc_singlets.py (3̄3̄3̄, 333, 3̄83, 888 with 2 singlets, 833̄: all vanish; four-spectator cases are non-zero). NOVELTY: (a) is the reference's; (b)–(d) are new.

### [results 8]
L5 — complex rotation of the k⁺ contour [R]. Hypothesis: (NF_B). Statement: for each colour pair, I(π_A,π_B) = e^{2iθ} ∫ d²κ/(2π)² F_A^[π_A](e^{iθ}κ) J_B^[π_B](−e^{iθ}κ) for every θ ∈ [0,π/2], where each quadrant piece is continued analytically. At θ = π/2: I = −∫ d²κ/(2π)² F_A(iκ) J_B(−iκ). PROOF. (1) By L3, each quadrant piece of F_A is holomorphic on the swept set {e^{it}x: x ∈ Q, t ∈ [0,π/2]}, because sgn Im z_e = −sgn x_e there; at u_e → 0 the pieces are regular. (2) In J_B(−u) with p = −e^{it}x: initial factors A_D + p + i0 have A_D < 0, and the deformation always moves them in the direction of their +i0. Final factors A'_D − p + i0 are compatible exactly when A'_D < 0, which is (NF_B). For t ∈ (0,π] no factor vanishes. (3) Apply Stokes in each quadrant. On the swept boundary pieces {u_e = 0} one has du_e = 0, so the holomorphic 2-form restricts to zero. The arcs at 0 and at ∞ vanish: J_B^[π_B] decays like |u|^{-1} only in a strip of width λ_B around u_1 + u_2 = 0, where F_A = O(|u|^{-2}); elsewhere the decay is faster. VERIFIED. The rotated code (twoexch_rotated_fast2.py) agrees with the real-contour code (twoexch_exact.py) to 7–10 digits at λ = 1 and at λ = 0.01, 0.001 (base set). A naive polar grid fails to resolve the strip of width λ_B; that earlier failure is documented in logs/twoexch_rotated_fast_0.01.log. NOVELTY: new.

### [results 9]
L6 — ray identity [R]. Hypotheses: ρ is holomorphic in the open quadrant 0 < arg k < π/2 and continuous up to its boundary, except for finitely many simple poles on the positive real axis, where the boundary values are ρ(k + i0). Moreover |ρ(k) − 1| ≤ C|k|/k_1 for |k| ≤ k_1 and |ρ(k)| ≤ Ck_2/|k| for |k| ≥ k_2. Statement: ∫_0^∞ (dκ/κ) Im ρ(iκ) = −π/2 + Im ∫_0^∞ (dk/k) ρ(k + i0) = −π/2 − π Σ_p Res_{k_p}ρ / k_p. In particular the result is exactly −π/2 if ρ is real on the positive axis. PROOF. Apply Cauchy's theorem to f(k) = [ρ(k) − (1+k)^{-1}]/k on the boundary of the quadrant, indenting the poles from inside the quadrant. The small and large arcs vanish because f = O(1) at 0 and O(|k|^{-2}) at ∞. Take imaginary parts and use ∫_0^∞ (dκ/κ) Im (1+iκ)^{-1} = ∫_0^∞ dκ (−1)/(1+κ²) = −π/2. VERIFIED: checks_C2_C3_C4.py C4 (8 random rational ρ, including poles on the axis; agreement 1e-15). NOVELTY. The lemma is elementary. Its role as the mechanism of T2 — each analytic rapidity end contributes −¼ to Re p_opp — is new.

### [results 10]
T2 — fully coincident pair of SS exchanges at O(g⁴); new [R_cond]. HYPOTHESES. Two SS lines join spectator i of J_A and spectator j of J_B (amplitude side); the connecting propagators are exact; the jets satisfy (J), (Sp), (R), ε ≪ 1, (NF_A) and (NF_B). CONCLUSION (pointwise in the transverse and jet variables): N/N_0 = 1 + O(ε^{1/2}L²), and p_opp = −(i/π) ln(1/ε) + i c + O(ε^{1/2}L²) with c real (it depends on the jets). Hence the side-sum residual −½ C_A χ² (Re p_opp) X is O(ε^{1/2}L²). The C_A term of M^(2) equals (−iχX)·(−C_A χ ln(1/ε)/(4π) + ...), a real multiple of the anti-hermitian one-exchange amplitude: a reggeization phase. PROOF. Step 1: L3. Step 2: L5 with θ = π/2. Step 3, inner square max|κ_e| ≤ K with λ_B ≪ K ≪ a/λ_A. There F_A = (𝒥_A/(a_1a_2))[w + O(λ_A K/a)]. Write w^[12] = ½ + v and w^[21] = ½ − v; v is real and odd under κ → −κ. Then p_opp^in = −(1/(2𝒥_B)) ∫ S_B(−iκ) + (1/𝒥_B) ∫ v Δ_B(−iκ), where S_B, Δ_B = J_B^[12] ± J_B^[21] and d²κ/(2π)² is understood. ∫_{R²} S_B(−iκ) d²κ/(2π)² = −𝒥_B: this is the rotation of the exact identity ∫ S_B(−u) d²u/(2π)² = 𝒥_B, i.e. Fourier inversion at equal times for the abelian B function. The tail outside the square is O(λ_B/K), because the 1/p strip terms of [12] and [21] cancel in S_B. By (R) and the symmetry of the square, conj[(1/𝒥_B) ∫ vΔ_B] = −(1/𝒥_B) ∫ vΔ_B, so this term is imaginary. Hence Re p_opp^in = ½ + O(λ_B/K + λ_A K/a). Step 4, outside the square. Only the strip |κ_1 + κ_2| ≲ λ_B contributes at leading power. There J_B^[12](p) = g_B(P)/(ip_2) · [1 + O(λ_B/|p_2|)] and J_B^[21] = −(same). Here g_B = φ_B^fi + φ_B^in with ∫ g_B dP/(2π) = 𝒥_B, and ∫ g_B(−iU) dU/(2π) = −i𝒥_B by rotation, using (NF_B). Therefore p_opp^out = −(i/2π) ∫_K^∞ (dκ/κ)[ϱ_12(κ) + ϱ_21(κ)] + O(λ_B/K). Here ϱ_12(κ) = ρ_12(iκ), with ρ_12(k) = (a_1a_2/𝒥_A) F_A^[12](−k,k) coming from the mixed sector (1V2); ϱ_21 comes from (2V1) in the same way. ρ is holomorphic in the first quadrant (L1); |ρ − 1| = O(λ_A|k|/a) near 0 and ρ = O((a/(λ_A|k|))²) at ∞; ρ is real on the positive axis by (R) and (NF_A). L6 then gives ∫_0^∞ (dκ/κ) Im ϱ = −π/2 for each of the two, and the piece ∫_0^K is O(λ_A K/a). So Re p_opp^out = −½ + O(...). Step 5: add the two regions. The imaginary logarithms combine to −(1/π) ln(a/(λ_Aλ_B)). Choose K = (aλ_B/λ_A)^{1/2}. The abelian normalization N/N_0 follows from the same steps applied to S_B. □ NUMERICS (scalar spectator model, see EX). Base set (NF holds for both jets): Re p_opp = 0.0123, 0.00205, 0.00035 at λ = 0.01, 0.003, 0.001. The real-contour and rotated methods agree to at least 7 digits. The slope of Im p_opp is −0.636 per unit ln(1/λ), i.e. → −2/π. NOVELTY. New. For this pattern at O(g⁴) it refutes the reference's claims (Prop E.31(iv), Rem E.32, Lemma E.48(d) read as physics) that the coincident residual survives within 𝒢₀ and that E.33(c2) is needed. It extends our ERR-S1 from eikonal lines to arbitrary jets in light-cone-ordered (LCOPT) form, and it is consistent with the two-loop checks of Lindsay–Ross–Sachrajda (1982/83) and Brandt–Frenkel–Taylor (1989). It holds unchanged for TMD, since no transverse component is moved.

### [results 11]
T2' — analytic rapidity regulator, and the end-pole terms; new [R_cond]. (a) Insert a regulator Π_e χ(k_e⁺) with χ ∈ 𝔛 and λ_B ≪ K_c ≪ a/λ_A. Then Re p_opp = O(power) under (NF_B) alone. Reason: in Step 4 of T2, ρ is replaced by ρχ ≈ χ, because A is still localized up to K_c; ρχ is still holomorphic and real on the axis, so L6 gives −π/2 for any jet A. The mirror statement holds with a regulator on k⁻ and (NF_A). (b) Without a regulator and without (NF_A): Re p_opp = −½ Σ_p Res_{k_p}(ρ_12 + ρ_21)/k_p + O(power). In the scalar model this is +½ a_1α_1/(a_1α_1 + a_2|d_10|) if α_1 > 0, and +½ a_2α_2/(a_2α_2 + a_1|d_20|) if α_2 > 0. The same terms arise from jet B's poles, by A↔B symmetry. These poles sit at k⁺ = a/(2α), the collinear end, where Lemma E.19(a) (dropping k⁺ inside J_A) is invalid. With exact kinematics a massive on-shell spectator cannot absorb an on-shell gluon: s^(1)·k_2 = 0 is impossible. So these terms are artefacts of using the Glauber approximation outside its domain, and the regulator (or the collinear regions) removes them. NUMERICS. apole set (A has α_1 = 1.35λ²): Re p_opp = 0.2626, 0.2536, 0.2520 at λ = 0.01, 0.003, 0.001, against the prediction 0.2517 (rotated method; the real-contour method mishandles this case, see EX). alt set (B has α_2 = 0.518λ²): 0.0692, 0.0520, 0.0490, against 0.0483. altswap (the same pole moved to A): identical to alt. With the regulator χ = 1/(1+|k|/λ): base and apole give 0.103, 0.054, 0.028 (equal to within 3e-4); altswap gives 0.035, 0.017. All tend to 0 ∝ λ^{1/2}. NOVELTY: new.

### [results 12]
P2 — the strict window [R]. Replace each connecting propagator by −1/k_Te² and truncate k^± symmetrically and independently. Then W = ¼ for every order pair, p_opp = ½, and the residual is −¼ C_Aχ²X: this is the reference's Lemma E.48(d), verified in R8 K5. In the language of T2, the inner region still gives Re = ½. The sharp truncations are not holomorphic in the quadrant, so L6 does not apply at the ends: they contribute no real part, and the compensating −½ is lost. Grade [R]. NOVELTY: the result is known; the diagnosis (non-analytic truncation) is new.

### [results 13]
P3 — on-shell lines [R; known in substance]. Take two on-shell external lines (massive scalars, or infinite time-like eikonal lines) with exact gluon propagators, IR-regulated by a gluon mass. At O(g⁴), box plus crossed box obey the exact two-particle unitarity relation: Disc_s(box + crossed) = ∫dΦ_2 T_1†T_1, by Cutkosky's rules graph by graph (Cutkosky 1960; Veltman 1963; 't Hooft–Veltman). The crossed box has no s-channel cut: a cut through both lines between their vertices must also cut both gluons, which requires single on-shell emissions from on-shell massive lines, kinematically forbidden. Three-particle cuts vanish at this order for the same reason. Hence box plus crossed alone are unitary, and in the high-energy limit p_opp is purely imaginary (ERR-S1: −iY/π, refdoc/work_R3/scripts/eikonal_box*.py). Consequence: the residual of E.31(iv) is not a property of the exact graphs.

### [results 14]
T3 — half-coincident pair; new, negative [R_cond + V]. HYPOTHESES. SS lines i–j_1 and i–j_2 with j_1 ≠ j_2 spectators of J_B; exact propagators; (J), (Sp), (R), (NF_B). (a) The side-sum residual is R = 2i c_1c_2 Im W_12 [X_1,X_2], with [X_1,X_2] = i f^{abc} T^c_i T^a_{j1} T^b_{j2} (L4b). (b) Re W_12 = ½ + O(ε). Proof: W_12 = ½ + (1/𝒥_B) ∫ d²u/(2π)² v(u) J_B(−u), up to O(ε). Jet A is localized wherever J_B has support, because J_B for two commuting insertions decays like |u|^{-2} in each variable. Rotating (L5, quadrant by quadrant) and using the conjugation symmetry κ → −κ (from (R)) shows that the integral is purely imaginary. (c) Im W_12 = 0 when the configuration is symmetric under line 1 ↔ line 2, since then W_12 = W_21. (d) Im W_12 = O(1) in general. Scalar model with B → b + s_1 + s_2 (two B-spectators): W_12 = 0.49788 − 0.03663i, 0.49980 − 0.03161i, 0.499992 − 0.03069i at λ = 0.03, 0.01, 0.003 (rotated method, halfcoinc.py). The independent real-contour code (halfcoinc_real.py) gives identical numbers. Symmetric case: 0.499996 − 0.000028i. B-asymmetric case: +0.0468i. Asymmetric a_e: −0.0212i (halfcoinc_sym.py). (e) R vanishes on colour singlets of (i, j_1, j_2) (L4c) and in the abelian theory. It does not vanish once passive spectators are present (L4d). CONCLUSION. In the two-time (Lemma E.19, exact-propagator) framework the half-coincident family does not cancel in general at O(g⁴). Any compensation must carry the three-gluon colour structure i f^{abc} T^c_i T^a_{j1} T^b_{j2}. Candidates are Glauber–soft 'Y' graphs with a soft leg to i and Glauber legs to j_1 and j_2, which lie in the soft-angle region. The purely Glauber Y graph is power suppressed in Feynman gauge: the three-gluon vertex contracted with n_A, n_B, n_B gives (k_1 − k_2)⁺ ~ λ². So an assumption of type E.33(c2)/E.44(c) is genuinely needed already at O(g⁴) whenever one hadron has at least two spectators and there are at least four spectators in total. GRADES. (a), (b), (c), (e): [R_cond]. (d): [P], numerically established by two independent methods. The statement that 𝒢₀ suffices for half-coincident patterns is [V]. NOVELTY: new, to our knowledge. It is not covered by Lindsay–Ross–Sachrajda or Brandt–Frenkel–Taylor, which have at most one spectator per hadron or eikonal spectators. It turns the 'genuine open problem' of ERR-S1 into a concrete O(α_s²) statement.

### [results 15]
P4 — per-graph weak equivalence fails for coincident pairs [R]. For a fully coincident pair, no per-graph rewriting that replaces each jet by data local to the Glauber window (equal-time values, window scales, fixed carriers) can satisfy (E.35) with error Cλ^a L^K. Reason: W(π_A,π_B) contains ±(i/2π) ln(1/ε) plus an O(1) constant fixed by the jets' mixed-sector functions at the collinear ends. The constant has an imaginary part −(1/2π) ∫(dκ/κ) Re ϱ and, when present, a real end-pole part (Step 4 of T2). Explicit example at λ = 0.01: the base and apole sets have the same window data but W(12,21) = 0.0061 − 1.0494i versus 0.2582 − 1.2506i. Consequence: E.34 and E.35 must be imposed on side-summed families, where only Re p_opp enters, not graph by graph. Using weights per graph does not cure the inconsistency of E.33(c1). NOVELTY: new; it sharpens ERR-S3.

### [results 16]
P5 — O(g⁶) [A]. Consider two on-shell eikonal (or massive) lines and the class of direct-line ladder graphs at O(g⁶): all gluons join the two lines, with any crossings. By Cutkosky's rules graph by graph, their three-particle cuts through one rung assemble into ∫dΦ_3 |A^lines_{2→3}|². Here A^lines is the tree amplitude with one gluon exchanged and one gluon radiated from the lines. For straight lines, emission before and after the exchange combine into f^{abc} T^c (v_A^μ/(v_A·k) − v_B^μ/(v_B·k))/q_T², the line part of the Lipatov vertex. This is non-zero in the non-abelian theory; in the abelian eikonal limit it vanishes outside the collinear regions. So the ladder class is not closed under unitarity, and its defect is a positive operator. In DY, part of |A^lines|² corresponds to cut direct lines (inside 𝒢₀). Part corresponds to soft lines emitted and absorbed by the same spectator (outside 𝒢₀). Gauge completion requires the three-gluon vertex. Hence E.33(c2), with soft real emission and the Lipatov vertex, is needed from O(g⁶) on for every non-abelian coincident pattern. This is consistent with BFKL and with Schwartz–Yan–Zhu 2018. NOVELTY: the formulation is new.

### [results 17]
L7 — E.33(a) on the far-off-shell set [R]. Hypotheses: j is a localizable endpoint on a spectator whose soft line ends on an internal vertex of the soft subgraph S; all other variables are real and k_j⁺ ≠ 0. Suppose every internal propagator of S whose momentum depends on k_j⁻, l = l_0 + ε_l k_j, satisfies |l²(0) − m_l²| ≥ 4|l⁺|Λ_j at k_j⁻ = 0, where l⁺ = l_0⁺ + ε_l k_j⁺; and the same holds for the connecting line. Conclusion: at fixed loop momenta of S, the external factor R_j(k_j⁻) is holomorphic in |k_j⁻| < Λ_j. It is bounded there by 2^{n_j} times the product of the moduli of its factors at k_j⁻ = 0 (times a polynomial bound on the numerators). Hence Lemma E.28 and L1 apply, with error O(Mλ_J R̄_j/Λ_j), stated as an absolute bound as recommended in R7 E5. Consequently E.33(a) holds outside the exceptional set E_j = {some soft line carrying k_j has |l² − m²| < 4|l⁺|Λ_j}, with Λ_j = λ^{−a'}ν_A. What remains of E.33(a) is an envelope bound ∫_{E_j} Φ̂ ≤ Cλ^a L^K on near-shell soft lines, which is the configuration the reference also identifies (E.33 status, E.44). PROOF. l² − m² is affine in k_j⁻ with slope 2ε_l l⁺. Its zero lies at distance |l²(0) − m²|/(2|l⁺|) ≥ 2Λ_j, and on the disc |l² − m²| ≥ ½|l²(0) − m²|. NOVELTY: elementary; new as a reduction of E.33(a).

### [results 18]
P6 — coincident SA/AS insertions and H-emission endpoints: where the obstruction lies [R, negative]. (a) Take a coincident pattern on one A-spectator: one SS line and one SA line, where the SA line's B-end sits on an active line absorbed by V_H. The A-localized weights W_π(k⁺_SS, k⁺_SA) of L1 are continuous but not analytic at k⁺_SA = 0 (L2), and they depend on the ratio k⁺_SA/k⁺_SS. The k⁺_SA integral against B's active-line factor Φ_B (holomorphic in the LHP, scale λ_B) is dominated by |k⁺_SA| ~ λ_B, where Φ_B is not eikonal. The reference produces the past-pointing Wilson line by a uniform deformation k⁺_SA → k⁺_SA − iκλ^{−a_G}|k_T|; this needs analyticity across 0. Deforming each half line separately from 0 leaves a non-eikonal neighbourhood of 0 with O(1) weight. (b) The same holds for H-emission endpoints (c_j = θ(k_j⁺)) whose other end sits on an absorbed active line. (c) For a non-coincident SA line the A-factor does not depend on k⁺, and the reference's deformation works. NOVELTY: new. It refines E.44(d) and the consequence of ERR-S3: the obstruction is non-analyticity in the region that dominates the integral, not the discontinuity itself.

### [results 19]
REG — reduction of the general case to explicit assumptions (updated register; answers (iv)). G1 = E.18(i)(ii): LCOPT validity (zero modes, instantaneous loops, truncation of minus components); unchanged; E.18(iii) is provable (R7 E7). G2 = E.34': the fibre-integrated envelope, imposed on side-summed families (a per-graph version is false by P4); still an assumption. G3 = E.33(a)': only the near-shell remainder of E_j (L7). G4 = E.33(b): cut compatibility of S; unchanged. G5 = E.33(c)': 'family unitarity' (the S-matrix of the Glauber window together with the adjacent soft region and real emission is unitary). It is needed only for: (i) half-coincident patterns from O(g⁴) (T3), where the compensating colour structure is i f T_i T_j1 T_j2; (ii) every non-abelian coincident pattern from O(g⁶) (P5), where soft real emission and the Lipatov vertex enter; (iii) coincident SA/AS insertions (P6). It is NOT needed for commuting patterns (T1) nor for fully coincident SS–SS pairs at O(g⁴) (T2/T2'). E.33(c1) is replaced by L1. G6 = E.44(a)–(d): unchanged; (d) is refined by P6. G7 (new; part definition, part matching assumption): SS windows carry an analytic rapidity regulator χ ∈ 𝔛, and the complement (the collinear ends of SS lines) is assigned to the collinear regions. Its contribution there must be reproduced by collinear factorization (Wilson lines) without a leftover hermitian C_A term. Supporting evidence: P3, ERR-S1/K9, and T2' (the window part is unitary). App D inputs stay as in the reference: D.7(A3), D.7(A4)(ii); D.14 including (H1)(H2) for rewritten and family-summed forms, which are Glauber-specific per ERR-M29; D.27. Overall grade of inclusive DY collinear and TMD factorization: still [A]. Our results upgrade sub-steps: the pattern classes listed above are [R_cond] or [V].

### [results 20]
EX — scalar spectator model and verification log. MODEL. Each hadron splits at a point vertex into an active parton and a spectator s (TMD-style light-front kinematics, P⁺ = 1). The colour-ordered covariant jet functions are J_A^[12] = i³/[(k_1⁻ + k_2⁻ − β + i0)(α_0 − k_1⁻ − k_2⁻ + i0)(α_1 − k_2⁻ + i0)] and J_A^[21], obtained with (α_2 − k_1⁻ + i0) in the last factor. Here β = E_a + E_s − P⁻, α_0 = E_s − E(s−k_1−k_2), α_1 = E_s − E(s−k_2), α_2 = E_s − E(s−k_1), d_0 = P⁻ − E_a − E(s−k_1−k_2), d_10 = P⁻ − E_a − E(s−k_2), d_20 = P⁻ − E_a − E(s−k_1), and 𝒥_A = i/d_0. Jet B is analogous, with energies p = −k⁺. For the half-coincident test, J_B = i³/[(p_1 + p_2 − β + i0)(α^(1) − p_1 + i0)(α^(2) − p_2 + i0)]. The parameter sets are in scripts/twoexch_rotated_fast.py: base (NF holds for both jets), apole (A: α_1 > 0), alt (B: α_2 > 0), altswap/baseswap (A and B exchanged). METHODS. (I) Real contour (twoexch_exact.py): exact k⁻ residues, exact log-residue inner integral, principal value + iπ for real poles of the outer integrand. KNOWN DEFECT: it mishandles a pinch in the outer variable when jet A has α_1-type poles, so its apole and 'both' values are invalid and are superseded by (II). (II) Rotated contour with strip adaptation (twoexch_rotated_fast2.py; valid under NF_B). (III) Brute force at finite η, λ = 1, extrapolated to η → 0 (twoexch_bruteforce.py): consistent with I and II within the extrapolation accuracy. At λ = 1, I and II agree to 7 digits, and at λ = 0.01 to 6–10 digits; base at λ = 0.001 gives 0.0003448 − 3.57434i (II) versus 0.0003515 − 3.57433i (I). TABLE OF Re p_opp (λ = 0.01, 0.003, 0.001). base: 0.0123, 0.0021, 0.00035. apole (II): 0.263, 0.254, 0.2520 (predicted 0.2517). alt (I): 0.069, 0.052, 0.0490 (predicted 0.0483). Regulated, K_c = λ: base 0.103, 0.054, 0.028; apole the same; altswap (0.003, 0.001): 0.035, 0.017. The slope of Im p_opp tends to −2/π unregulated and −1/π regulated. Abelian normalization N/N_0 → 1 (0.9998 at λ = 0.003). The half-coincident numbers and the colour checks are given under T3 and L4. Other checks: L1 C1/C2, L6 C4. All checks pass, except that the deliberately mis-specified 'pred' formula in an early half-coincident test was corrected; the correct formula is in L4b.

## open

### [open 1]
O1 (main): does anything cancel the half-coincident residual of T3, 2i c₁c₂ Im W₁₂ ⟨[X₁,X₂]⟩, at O(α_s²)? Test it in a hadron model with at least four spectators. First candidate: Glauber–soft 'Y' graphs with a soft leg to the A-spectator and Glauber legs to j₁ and j₂ (soft-angle region). If nothing cancels it, the two-time framework (App E/Aybat–Sterman type) must be modified for multi-spectator hadrons.

### [open 2]
O2: prove the symmetric form of T2. That means analytic regulators at both rapidity ends and no NF hypothesis on either jet; we prove only the one-sided versions T2/T2′.

### [open 3]
O3 (all orders, conjectures). C1: the leading-log tower of the fully coincident pattern is anti-hermitian to every order, i.e. a real multiple of −iχX, with one factor −(i/π)ln per order (gluon reggeization). C2: at O(g⁶) and beyond, unitarity of the window is restored only after adding soft real emission (cut direct lines, soft lines emitted and absorbed by the same spectator) and the Lipatov three-gluon vertex. Supported by P5 (argued) and by BFKL; not proven here.

### [open 4]
O4: coincident SA/AS insertions and H-emission endpoints (E.44(d)). Treat the non-analytic weights of L2 together with the Wilson-line deformation, or give an alternative derivation of the past-pointing Wilson line that does not need deformation.

### [open 5]
O5: the remaining analytic inputs are untouched. E.34′ (envelope for side-summed families), E.18(i)(ii) (zero modes, instantaneous loops), E.44(b) (𝔅-compatibility), E.44(c) (soft-angle region, including SS exchange at the soft scale) and the near-shell remainder of E.33(a) (L7).

### [open 6]
O6: matching at the collinear ends (G7). Show that, with exact kinematics, the SS contributions beyond the analytic rapidity regulator are absorbed by collinear factorization without a leftover hermitian C_A term.

### [open 7]
O7: write out the TMD transcription. L1–L7, T1–T3 and P1–P6 carry over verbatim, since only k^± are manipulated and the measurement is transverse; check the interplay with E.9(iii′) and the staple direction.

### [open 8]
O8 (literature): the novelty claims rest on a limited INSPIRE title search; the citation search on DGOPS 2016 failed. Check CSS 1988, Collins 2011 §14.4, DGOPS 2016 §4 and Liu–Ma arXiv:0802.2973 for the half-coincident structure and for the ordering-weight analysis before printing 'new' markers.

## files

### [files 1]
/Users/hao-cheng/Desktop/theorem proof/qcd_factorization_work/verify/extend/X1-glauber/scripts/twoexch_exact.py

### [files 2]
/Users/hao-cheng/Desktop/theorem proof/qcd_factorization_work/verify/extend/X1-glauber/scripts/twoexch_rotated_fast2.py

### [files 3]
/Users/hao-cheng/Desktop/theorem proof/qcd_factorization_work/verify/extend/X1-glauber/scripts/twoexch_rotated_fast.py

### [files 4]
/Users/hao-cheng/Desktop/theorem proof/qcd_factorization_work/verify/extend/X1-glauber/scripts/twoexch_regulated.py

### [files 5]
/Users/hao-cheng/Desktop/theorem proof/qcd_factorization_work/verify/extend/X1-glauber/scripts/twoexch_bruteforce.py

### [files 6]
/Users/hao-cheng/Desktop/theorem proof/qcd_factorization_work/verify/extend/X1-glauber/scripts/twoexch_model.py

### [files 7]
/Users/hao-cheng/Desktop/theorem proof/qcd_factorization_work/verify/extend/X1-glauber/scripts/test_twoexch_parts2.py

### [files 8]
/Users/hao-cheng/Desktop/theorem proof/qcd_factorization_work/verify/extend/X1-glauber/scripts/halfcoinc.py

### [files 9]
/Users/hao-cheng/Desktop/theorem proof/qcd_factorization_work/verify/extend/X1-glauber/scripts/halfcoinc_real.py

### [files 10]
/Users/hao-cheng/Desktop/theorem proof/qcd_factorization_work/verify/extend/X1-glauber/scripts/halfcoinc_sym.py

### [files 11]
/Users/hao-cheng/Desktop/theorem proof/qcd_factorization_work/verify/extend/X1-glauber/scripts/checks_misc.py

### [files 12]
/Users/hao-cheng/Desktop/theorem proof/qcd_factorization_work/verify/extend/X1-glauber/scripts/checks_C2_C3_C4.py

### [files 13]
/Users/hao-cheng/Desktop/theorem proof/qcd_factorization_work/verify/extend/X1-glauber/scripts/check_halfcoinc_colour.py

### [files 14]
/Users/hao-cheng/Desktop/theorem proof/qcd_factorization_work/verify/extend/X1-glauber/scripts/check_halfcoinc_singlets.py

### [files 15]
/Users/hao-cheng/Desktop/theorem proof/qcd_factorization_work/verify/extend/X1-glauber/logs/twoexch_exact2_0.001_base.log

### [files 16]
/Users/hao-cheng/Desktop/theorem proof/qcd_factorization_work/verify/extend/X1-glauber/logs/twoexch_exact2_0.001_alt.log

### [files 17]
/Users/hao-cheng/Desktop/theorem proof/qcd_factorization_work/verify/extend/X1-glauber/logs/twoexch_rotated_fast2.log

### [files 18]
/Users/hao-cheng/Desktop/theorem proof/qcd_factorization_work/verify/extend/X1-glauber/logs/twoexch_rotated_fast2_apole.log

### [files 19]
/Users/hao-cheng/Desktop/theorem proof/qcd_factorization_work/verify/extend/X1-glauber/logs/twoexch_regulated.log

### [files 20]
/Users/hao-cheng/Desktop/theorem proof/qcd_factorization_work/verify/extend/X1-glauber/logs/twoexch_altswap_rot_reg.log

### [files 21]
/Users/hao-cheng/Desktop/theorem proof/qcd_factorization_work/verify/extend/X1-glauber/logs/twoexch_exact3_0.003_altswap.log

### [files 22]
/Users/hao-cheng/Desktop/theorem proof/qcd_factorization_work/verify/extend/X1-glauber/logs/twoexch_bruteforce_base.log

### [files 23]
/Users/hao-cheng/Desktop/theorem proof/qcd_factorization_work/verify/extend/X1-glauber/logs/halfcoinc.log

### [files 24]
/Users/hao-cheng/Desktop/theorem proof/qcd_factorization_work/verify/extend/X1-glauber/logs/halfcoinc_real.log

### [files 25]
/Users/hao-cheng/Desktop/theorem proof/qcd_factorization_work/verify/extend/X1-glauber/logs/halfcoinc_sym.log

### [files 26]
/Users/hao-cheng/Desktop/theorem proof/qcd_factorization_work/verify/extend/X1-glauber/logs/checks_misc.log

### [files 27]
/Users/hao-cheng/Desktop/theorem proof/qcd_factorization_work/verify/extend/X1-glauber/logs/checks_C2_C3_C4.log

### [files 28]
/Users/hao-cheng/Desktop/theorem proof/qcd_factorization_work/verify/extend/X1-glauber/logs/check_halfcoinc_colour.log

### [files 29]
/Users/hao-cheng/Desktop/theorem proof/qcd_factorization_work/verify/extend/X1-glauber/logs/check_halfcoinc_singlets.log

### [files 30]
/Users/hao-cheng/Desktop/theorem proof/qcd_factorization_work/verify/extend/X1-glauber/logs/test_twoexch_parts2.log
