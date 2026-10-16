# Final independent review of X2-subtraction_final.md

(persisted verbatim from workflow wf_4e25ac9b-92f; overall verdict: **fixable_issues**)

## Per-result verdicts

### [1]
[0] INPUTS AND METHOD.
- Reviewed the on-disk file /Users/hao-cheng/Desktop/theorem proof/qcd_factorization_work/verify/extend_reports/X2-subtraction_final.md (1961 lines). It exists, and its content matches the backup text in the task. All six reviews (rev1-1 … rev3-2) are persisted.
- My independent checks use my own code; none imports X2 code. They are in /Users/hao-cheng/Desktop/theorem proof/qcd_factorization_work/verify/extend/X2-subtraction/review_final_scripts/: chk_B3.py, chk_C4e.py, chk_C4e3b.py, chk_misc.py and chk_coverage.py, each with its .log, plus re-run logs of r3_archive_verify.py (rerun_r3_archive_verify_{triangle,bubble}.log).
- Literature read in full text: Smirnov–Rakhmetov hep-ph/9812529 and Belitsky–Smirnov arXiv:2505.22595.
- INSPIRE records checked for 2505.22595, 2409.05945, 2607.26291 and 1801.03960.

### [2]
[1] §1 SETTING: CORRECT. I re-derived the normalizations.
- (M1): μ^{2ε}∫d^dk/(iπ^{d/2}) = (1/(iπΓ(1−ε)))∫dx dκ κ^{−ε}∫dk⁻. Hence ρ = 2·Res at the D_1 pole (0<x<P) and ρ = −2·Res at the D_2 pole (sliver).
- (M2): the R-pole residue gives the measure (1/Γ(2−ε))∫dξ/(1−ξ)∫dt t^{1−ε}⟨1/(A+v+2k·q)⟩/v², with S = v at the pole.
- The (M1) caveat of §1.1 is correct.

### [3]
[2] §2 REGISTER: CONSISTENT, with two loose points.
- (IRF) is defined as absolute convergence of the parametric integral on [0,ε_0]. Thm F.1 admits UV-divergent J–φ insertions, and for those graphs this fails at ε = 0 unless (IRF) is stated for the renormalized integrand.
- The register calls (FIN2) 'discharged'. That holds only given (RA1), (RA2) and (V2) (Thm E.3(v)).

### [4]
[3] Thm A.1: CORRECT.
- I re-derived (A.1), the constant C′ = |𝓡|(1+|𝓡|)C, and (FR) for (1−T)X by linearity. The asymptotics of Remark (b) also re-derive.
- Slip: 'All three round-2 reviewers re-derived (A.1)'. Only two round-2 reviews exist (rev2-1, rev2-2); r3_1 and r3_2 also re-derived it.

### [5]
[4] Lemma A.2: CORRECT with (FR)_η, (IL1), (IL2) and (IL3).
- After each pole substitution the real parts do not depend on η, so |g_η| ≥ |g_0|; the closing sides do not depend on η either.
- Scope (3) is right: Q² = (Q̃²+m²)²/Q̃² > 4m² cannot be realized by purely spatial p_1, p_2, since |p_1+p_2| ≤ 2m. So the triangle never lies in the Euclidean region.

### [6]
[5] Lemma A.3: (a) and (b) CORRECT; the verifier of (c) has two unstated limitations.
- (a): both directions re-checked, via ψ(x+tr) ≥ ψ(x)+tψ_inf(r) and the eventual slope. (b): the L-power equals the face dimension once the L^n Jacobian is included.
- (c), r3_archive_verify.py imports only sympy and the standard library. Its exact checks are y≥0, Aᵀy=c, b·y+const=value, Ax≤b, c·x+const=value, S⁺, rank, face bound, exponent, L-power and the 2D recession slope. Together these form a complete LP-optimality certificate.
- My re-run, 0 failures, minimal exponents as stated:
  - triangle: 58 records, 546 certificates, 58 closed forms;
  - bubble: 2986 records, 70,373 certificates, 2938 closed forms, plus 48 item records checked at the LP level only.
- Face-bound counts: triangle {0:251, 1:207, 2:88}; bubble {0:60012, 1:9839, 2:522}.
- Limitation (i): the closed-form identity test is an exact evaluation at 3 random rational points. It is a randomized test, not a symbolic proof.
- Limitation (ii): cell coverage of each U_R and of the base is not checked. I checked it myself.
  - Triangle, by inspection: the archived cells equal the cover of Thm B.5 (U_S: X_u≤−1, X_κ−X_u≤−1; U_{C_1} cells I/II/III; U_{C_2}; remainder cells I/II/u>1; sliver A/B), and every LP cell contains the actual cell.
  - Bubble, by sampling: 20,000 points per region and per ε in normalized log coordinates, 0 uncovered (regions I, II∖corner, corner, u>1).
  - The u∈(1,2] part of U_{C_1} and the sliver are covered by the triangle certificates times |l|^j, as Thm B.8 states.

### [7]
[6] Lemma A.4: unchanged since rounds 1–3. The word 'analogous to' has been applied.

### [8]
[7] Cor A.5: CORRECT as [R, R_cond: (IRF),(LCE)].
- The endpoint bound is valid because ε enters only through exponents affine in ε: the integrand is exp(εA+B), which is convex in ε.
- Round 2 stated an (M2) clause, 'every DIS ladder', conditional on (LCE). The final text downgrades it to '(IRF) expected'.
- The downgrade is defensible: IR finiteness of (M2) is only power-counted (OQ16). But it contradicts r3_2 fix 2 ('keep the (M2) clause unchanged') and is not recorded in §17.

### [9]
[8] Prop A.6: (a), (b), (d) CORRECT; (c) contains an error.
- (a), correct. The kite is the massless two-loop master with its chord across the ψ loop, so it has no one-loop two-point subgraph. Σ_2 = K(ε)(−k²)^{−1−2ε}, with K(0) = 6ζ(3) times couplings, and ν = 3+2ε.
  - The corner integral ∫r^{d/2−ν−1}dr converges only for ε < −1/3. Since Γ(3+3ε) is finite, the DR value is finite at ε = 0.
  - I re-derived the effective density: D_g at the D_1 pole is A/(P−x), giving (P−x)^{2+2ε}/(A^{3+2ε}D̂_2).
  - The numbers match r3_M1_infrared.log, but the report does not state the δ grid (10⁻³, 10⁻⁵, 10⁻⁷) or the parameters (m² = 0.01, P = P′ = 1/√2) of the proxy.
  - The refutation needs only the divergence of the positive parametric integral. The 'effective fibered density' step integrates the kite subgraph covariantly first, which is an LCE-type step; the text should say so.
- (b), correct: ν = 2+ε and 2. The increments 46,020 and 46,051 match ln(100)/m⁴ = 46,052.
- (c): the formula ω = n_a − V_S and all seven table entries re-derive correctly.
  - ERROR: 'a hard or counterterm two-point insertion on a soft line … lowers ω by 4' is wrong. With V_2 two-valent insertions, 2I_S = 3V_S+2V_2+n_a and L_S = I_S−V_S−V_2, so ω = n_a−V_S−2V_2: each insertion lowers ω by 2 (triangle: +2 → 0).
  - This is exactly the logarithmic ν = 2 case of (b), and r3_M1_infrared.log (a) shows the corner integrand r^{−1−ε}. With '4' the counterterm graph would be power divergent, which contradicts (b).
- (d), correct: ω = 2n_a, also with insertions ∝k².

### [10]
[9] Lemmas A.7, A.8, A.9: CORRECT.
- A.7 re-derived.
- A.8: the coefficient of ε^{−s} gives Σ_k k^n c_{k,−N} = 0 for 0 ≤ n ≤ N−1. The Vandermonde determinant on nodes 0..4 is 288.
- A.9: both continuations re-derived.

### [11]
[10] Prop B.1: CORRECT.
- I re-derived the residues from the propagators at general P, P′ with sympy.
- main = 1/(AD̂_2), and sliver = 2/(wD_gD_1) at k⁻ = P′+κ/w. Both hold identically.

### [12]
[11] Prop B.2: CORRECT.
- The closed forms re-check, and the ε→0 sum is L̃²+π²/3 (sympy series).
- The positioning is accurate. Our C_H, C_{C_i} and C_S equal Belitsky–Smirnov (A.1)–(A.3) up to e^{εγ_E}: Γ(−ε)²Γ(1+ε)/Γ(1−2ε), Γ(−ε)²Γ(ε)/(2Γ(−2ε)) and Γ(1−ε)Γ(ε)².

### [13]
[12] Prop B.3: CONFIRMED. This review is one independent confirmation.
- By hand:
  - main map: Jacobian (1−u)/(1+τ), x_g = (1−u)(1−z), F = (1−u)[m²(u+(1−u)z)+zu];
  - sliver map: Jacobian τs/(1+τ), x_g = s(1−v), F = τs[1−s(1−v)+τv(1−s)], and x_1 < τx_2 ⟺ s < 1;
  - the Feynman-parameter κ-integrals of both parts.
- Numerically, with my own residues and my own simplex quadrature:
  - (P,P′,m²,ε) = (0.8,1.3,0.1,0.3): main 13.396394159814183728 on both sides (rel 5·10⁻²⁵); sliver 2.164676343944342866 (rel 3·10⁻²²);
  - (0.5,0.9,0.02,−0.4): main 5.0789343503040503353 (rel 3·10⁻²⁶); sliver 0.3265132115884442963 (rel 1·10⁻²⁶).
- Novelty: for Γ this is an explicit instance of the known LF/LCPT–covariant equivalence for scalar graphs (Ligterink–Bakker 1995; Chang–Yan 1973, already cited under (LCE)). The sliver is the non-valence k⁺<0 ordering. Prop B.3 is a self-contained derivation, not a new identification.

### [14]
[13] Prop B.4: CONFIRMED numerically with my own code at ε = 0.
- ∫_sl ρ_{C_{C_2}} − ζ_2 = 4·10⁻³¹ at m² = 10⁻³ and 10⁻⁵.
- ∫_sl ρ_Γ − ζ_2 = −2.0·10⁻³ and −2.0·10⁻⁵.
- ∫_sl r/m² = −1.99786 and −1.99998.

### [15]
[14] Thm B.5: CORRECT as [R, R_PT], computer-assisted.
- The archive re-verifies, and its cells match the cover.
- The ε-uniformity argument is valid: κ^{−ε} ≤ 1+κ^{−ε_0}, and the LP value is convex in ε.
- Minor: '∫_{U_S}ρ_{C_{C_1}} ≥ s/4 since A,B ≤ 2um²' holds only at θ = 2. For θ < 2 one has A,B ≤ 2us, which gives ≥ λ²/4; that is what the optimality conclusion needs.
- A stronger, cover-independent argument is available. Σ items ≥ ∫|ρ_r| ≥ |∫ρ_r| = |∫r| = 4λ²(1+o(1)), by Prop B.7 with (FI) from Props B.2–B.3. So no cover at all beats exponent 2.

### [16]
[15] Cor B.6: the implication is CORRECT.
- With Prop B.3 confirmed here, Cor B.6 is mathematically [R, R_PT], computer-assisted.
- The spec's PASS rule requires two independent confirmations (see required fixes). So one more confirmation of Prop B.3 is needed before Cor B.6 is printed without its premise.

### [17]
[16] Prop B.7: CORRECT.
- With ρt = m² and λ = (1−m²)/(1+m²), Φ^(1)(t,t)/Q² = [4Li_2(−m²)+L̃²+π²/3]/(1−m⁴).
- The result carries no [rev]/[new-final] flag, contrary to §0's rule that every result carries one.

### [18]
[17] Thm B.8: CORRECT after the relabelling.
- The (M1) chain ∝ g^{2j}(−k²)^{−1−j(1+ε)}×(poles) checks by dimension counting.
- Lemma B.8.1 is correct.
- The four-shell identity re-checks symbolically in my verifier re-run (both ranges True).
- The archive and its coverage pass.
- ∫_1^∞(ln κ)^jκ^{−2}dκ = j! is correct.

### [19]
[18] Props C.1 and C.6, Lemma C.3, Prop C.4(a)–(d), Claim C.5: carried over faithfully from fix 1.
- I compared the texts: regions A/B are defined and gaps g1–g5 are listed.
- c_1(2), c_1(1.3), c_1(5) = 1.2629839, 1.9366731, 0.92415776, as stated.
- Re-derived: ∫σ^{3/2}(σ⁻²−(σ+δ)⁻²)dσ = 3πδ^{1/2}/2 and ⟨|cosθ|⟩_{S³} = 4/(3π).
- Both S^{3−2ε} average forms agree with direct quadrature (for example 1.04300240082267 by all three routes).
- The grade 'at ε = 0' of (a)–(d) is honest. But the summaries call the ladder 'proved completely' without saying 'at ε = 0'.

### [20]
[19] Lemma C.2: the new three-case pole-side proof reaches the correct conclusion.
- Step 1 is imprecise. A factor propagated from level l > j depends on k_j⁻ with coefficient −2k_l⁺, not −2k_j⁺.
- The sign is the same on the ordered support, so the conclusion stands. Fix 1 had it right: 'coefficient −2k_j⁺ in k_{j−1}⁻'.

### [21]
[20] Prop C.4(e1): CONFIRMED. This review is one independent confirmation.
- Re-derived by hand: the measure step, the Feynman parameter (Δ = (1−ξ)[ξm²+(1−y)ξc+y(1−y)(1−ξ)]), the covariant F = x_2(x_1+x_3)m²+x_3(x_1+x_2c), and the map to the simplex (Jacobian 1−ξ).
- Numerically: m² = 0.01, ε = 0.1 gives 4.68929374814784151 on both sides (rel 4·10⁻²⁶); m² = 0.05, ε = 0.25 gives 4.852772726725455 (rel 1·10⁻²⁴).
- The fibered value in the r3 log was quadrature-limited (rel 2.8·10⁻¹³).
- Novelty: an instance of (LCE), as for Prop B.3.

### [22]
[21] Prop C.4(e2): CORRECT. The t-integral is a Beta integral.

### [23]
[22] Prop C.4(e3): the fibered closed form is CONFIRMED. This review is one independent confirmation.
- My own 2D quadrature, with the t^{−1−ε} tail done analytically:
  - x = 2: ε = 0.1, 0.2, 0.3 give −6.5849620951762479309, −3.5727213093484249996, −2.607837860955034437 (rel 4·10⁻²⁵, 1·10⁻²⁵, 6·10⁻²⁶);
  - x = 1.3, ε = 0.15: −5.5948279175487600717 (rel 3·10⁻²⁶);
  - the fibered T_HΓ at ε = −0.3 and −0.6 equals the continued closed form (rel 3·10⁻¹² and 5·10⁻¹⁵).
- Steps 2–4 re-derived by hand: Δ = (1−y)(1−ξ)(ξc+y(1−ξ)), T(ε), dβdγ = s ds dy, and the factorization to B(−ε,2−ε)∫y′(c+y′(1−c))^{−1−ε}dy′.
- Minor (i): step 1's 'the constants are uniform' needs ₂F₁(1/2,1;2−ε;z) to stay bounded as z → 1, which holds only for ε < 1/2.
  - Here z_max = (1−ξ)/(1−ξ/x) → 1 as ξ → 0. For 1/2 ≤ ε < 1 the constant grows like ξ^{1/2−ε}, which is still integrable; alternatively extend by analyticity.
  - Verified: ₂F₁ tends to 3.49 at ε = 0.3 and is unbounded at ε = 0.6.
- Minor (ii): 'simplex identity to 10⁻¹³–10⁻³¹' overstates the agreement. The log shows T(square) and T(simplex) agreeing only to 5.6·10⁻¹¹ at ε = −0.3.
- The [P] grade for the whole-integrand parametric value is honest.

### [24]
[23] Thm D.1 and Prop D.2.
- Thm D.1 CONFIRMED numerically:
  - the κ-integral of the 0<u<1 bracket vanishes (−9·10⁻³³ at u = 0.37);
  - ∫r minus −λ²(L+1)−λ⁴(L/2+1/4), divided by M⁶L, is ≈ −0.35 and −0.34 at M² = 10⁻³ and 10⁻⁶, consistent with the stated O(λ⁶L).
- Prop D.2 is unchanged (re-derived by r3_1 and r3_2), and the round-3 wording fixes are applied.

### [25]
[24] Thm E.1, Prop E.2 and Thm E.3(i): unchanged, and the counts are consistent.
- 9 singles + 40 composites + identity = 50 patterns.
- 18+15+6+1 = 40 composites, and 15+6+1 = 22 rapidity-type composites.

### [26]
[25] Thm E.3(ii): CONFIRMED against the Smirnov–Rakhmetov full text.
- SR eq. (2) reads p_1 = p̃_1+(m²/Q²)p̃_2, p_2 = p̃_2+(m²/Q²)p̃_1, with 2p̃_1·p̃_2 = Q². So SR's Q² is exactly our Q̃², and our p_1 and −p_2 are SR's eq. (2) with m²_SR = −m².
- SR define 1c by k⁺ ~ Q with k^± = k⁰ ± k¹, which is collinear to p̃_2. The region dictionary and the routing (k,l) = (k_2,k_1+k_2) are therefore correct.
- The six integrands encoded in r3_twoloop_regions.py coincide factor by factor with SR eqs. (3), (5), (6), (7), (8), (9).
- B_0 (for example k_1 = (l⁺, l⁻−k⁻, l_T)) is a k-dependent translation of l, as stated.
- SR's own 'Q² ≡ −q²' is inconsistent with their eq. (2) at O(m²). The report correctly uses eq. (2).

### [27]
[26] Thm E.3(iii): CORRECT as [R, R_cond: (RA1),(RA2),(V2)]. (RA2) was not discharged.
- r3_1 fix 5 asked for (RA2) to be discharged. It was not, and §17 does not say so.
- A discharge route exists. SR's straight-contour Mellin–Barnes representations (eq. (8): 3Re ε < c < min(Re ε, 0) for Re ε < 0) indicate that each single converges absolutely in pure DR on an open ε-domain. With (RA1) and uniqueness of analytic continuation, that would give (RA2) for the singles.

### [28]
[27] Thm E.3(iv): CORRECT.
- The summation of SR's printed values is consistent: e^{−γ_Eε} per loop is restored for eqs. (5)–(7) to match eqs. (4) and (10), and the deviation is O(ε).
- Wording: 'they introduce one only for the non-planar diagram of their Limit 2' is inaccurate. SR state that the planar diagram in Limit 2 also needs analytic regularization (their ref. [7]).
- What matters here is correct: no regulator is used for this diagram in Limit 1.

### [29]
[28] Thm E.3(v) and (vi).
- (v) CONFIRMED. A sympy series of the UD form gives the NLP coefficient −(L̃⁴/2+π²L̃²+7π⁴/30+12). The grid values and their ratios (0.92448 … 0.999998) match.
- (vi): the logic is correct, but it is graded '[R]'. It assumes (FIN2) together with (RA1), (RA2) and (V2) from (iii), which are needed to reduce ΣC_R to singles with exponents −k_Rε. It should be graded [R, R_cond].

### [30]
[29] §7.4: the [P] grade is honest, and the norm statements are correct as conditional statements.

### [31]
[30] Thm F.1: CORRECT as an implication.
- The restriction to (IRF) classes and Remark F.2 are adequate.
- The N = 1 status list over-attributes. It lists (FR) and (CS3^φ) '(Prop B.1)' for 'all graphs of (M1), i.e. the triangle and the J–φ graph', but Prop B.1 covers only the triangle.
- The J–φ graph is in fact handled as an explicit renormalized insertion, with remainder Π_R(q²)D(q) − Π_R(q̂²)D(q̂) = O(λ²). It does not go through (FR), (FI) and (CS3^φ).

### [32]
[31] Remarks F.3–F.4: VERIFIED in the Belitsky–Smirnov full text.
- The quote is in their §2: '…has the status of experimental mathematics. However, up to now, there are no known examples where it is found to fail.'
- Eq. (6.18) is the entangling term [(k2−p1)²+2k1·(k2−p1)]^{−1}.
- Eq. (6.22): T21^{c1-us} = (1/4)z_1T11^cT11^us with z_1 = Γ(1+2ε)/Γ²(1+ε). Twisting works at two loops and fails at three.
- App. A.2 gives the two-loop region values to O(ε²); §4 uses tropical geometry and Newton polytopes.
- INSPIRE confirms PRD 113 (2026) 036022, JHEP 05 (2025) 237 [2409.05945], Poldaru 2607.26291, and Collins 1801.03960 with the titles as cited.

### [33]
[32] §9–§11: dictionary fine apart from one overstatement; PASS statement wrong.
- '(V2) enters only Thm E.3 and Prop C.4(e3)' is too strong. The statement '(V1) verified for the triangle' itself uses (V2) for the zero-bin chain terms (for example T_{C_1}T_SΓ, scaleless with weight −ε), and an analytic regulator for the zero-weight term 1/(D_gh_1h_2). What Props B.2–B.3 prove is (FI).
- §11's statement of the PASS rule is wrong (see the required fixes).
- X2a in fibered form (Thm B.5) meets PASS: r2_2, r3_1 and r3_2 confirmed it, and so does this review.
- X2b, X2c and X2d are correctly reported as not delivered.

### [34]
[33] §12 novelty ledger: mostly honest, with three problems.
- Item 4 counts Prop B.3, and item 6 counts Prop C.4(e1), as new. Both are instances of the known LF–covariant equivalence.
- Item 8 (Prop A.6(a)) refutes this report's own round-2 claim. It is not a result for the monograph.
- Item 3's 'optimal λ-exponent' should say 'within the cover family', or use the cover-independent argument of [14].

### [35]
[34] §13–§17: ledgers complete, OQ list consistent; three gaps.
- OQ1 still lacks the Belitsky–Smirnov positioning requested by r3_1 (per_result 31 and fix 4). OQ10 is covered through OQ17.
- §17 does not mention that (RA2) was not discharged (r3_1 fix 5).
- §17 does not mention the change to the (M2) clause of Cor A.5 (r3_2 fix 2).

### [36]
[35] LEDGER OF ROUND-3 REQUIRED FIXES.
- Review r3_1:
  - 1 done: the report is complete and the reviews are persisted.
  - 2 and 3 done.
  - 4 done, except OQ1.
  - 5 PARTIAL: (FIN2), premise (iii), the pole-order input and the m² grid are done; (Reg)(b), now (RA2), is kept without explanation.
  - 6 done: (FR)_η and (IL3).
  - 7 done: C_H exact on the fibered side, closed form added, precision corrected.
  - 8 done: self-contained archives and an independent verifier, with the coverage and randomized-test caveats of [5].
  - 9 done.
- Review r3_2:
  - 1 done: every fix-1 proof is carried over, checked against the fix-1 text.
  - 2 done, but the (M2) clause was changed rather than kept.
  - 3 done (OQ16).
  - 4 and 5 done.
  - 6 done: closed form, numbers labelled, measure dz d⁴k stated.
  - 7 done: m² grid, Vandermonde sentence, LP data, 'analogous to', Collins 2018, Jackiw–Templeton.

## Required fixes (binding for the appendix writer)

### Fix 1
[Prop A.6(c), error] Replace 'lowers ω by 4' with 'lowers ω by 2'.
- State the formula ω_IR = n_a − V_S − 2V_2, where V_2 counts two-valent (constant) insertions.
- This is consistent with (b) and r3_M1_infrared.log: ν = 2 is logarithmic, with corner integrand r^{−1−ε}.

### Fix 2
[§0 and §11, PASS rule] The spec requires TWO independent confirmations recorded in verify/, plus a literature check for any novelty claim (OUTLINE_appMNOPQ §00.4; WRITER_SPEC_v2 §6.5 item 2.2). The report says one; correct both places.
- This final review is one independent confirmation of:
  - Prop B.3;
  - Prop C.4(e1), and the fibered closed form in C.4(e3);
  - Prop A.6(a),(b), after fix 1;
  - Lemmas A.8 and A.9;
  - Thm E.3(ii) and (iv)–(vi), after the Thm E.3 fixes below;
  - the r3 archive verification.
- Cor B.6 stays [R, R_cond: (FI)_Γ] in print until a second independent confirmation of Prop B.3 is recorded.

### Fix 3
[Novelty: §12 items 4, 6, 8; Props B.3 and C.4(e1)] Present the fibered = covariant identity for Γ of the triangle and of the one-rung ladder as an explicit, self-contained derivation.
- It is an instance of the known LF/LCPT–covariant equivalence for scalar graphs (Ligterink–Bakker 1995; Chang–Yan 1973), and the sliver is the non-valence k⁺<0 ordering. Under WRITER_SPEC §6.5 item 2.3 it is printed as 「本书给出的推导」.
- Keep novelty only for the fibered identification of the Collins terms that contain zero-bins (Prop B.2, Prop C.4(e3)), and for its use to remove the premise of Cor B.6.
- Remove item 8 (Prop A.6(a)) from the novelty ledger; it is the correction W19.

### Fix 4
[Thm E.3] Four corrections.
- (a) Either discharge (RA2) for the nine singles, or explain in (iii) and in §17 why SR's pure-DR values do not discharge it (r3_1 fix 5). Route: show that each single converges absolutely in pure DR on an open ε-domain (SR's α/MB representations with straight contours, e.g. eq. (8) for Re ε < 0), then use (RA1) and uniqueness of analytic continuation.
- (b) Regrade (vi) as [R, R_cond: (RA1),(RA2),(V2),(FIN2)].
- (c) Correct 'they introduce one only for the non-planar diagram of their Limit 2'. SR also use analytic regularization for the planar diagram in Limit 2 (their ref. [7]); none is needed for Limit 1.
- (d) In the §2 register, write '(FIN2) discharged given (RA1), (RA2), (V2)'.

### Fix 5
[Thm F.1 status; (IRF) in §2] Two corrections.
- At N = 1, list (FR), (FI) and (CS3^φ) (Props B.1–B.3) for the triangle only. State that the J–φ graph is handled exactly, as a renormalized insertion outside the fibered framework, with remainder O(λ²).
- Define (IRF) for the renormalized integrand, or exclude UV faces. Thm F.1 admits UV-divergent J–φ insertions, whose bare parametric integrals diverge at ε = 0.

### Fix 6
[Summaries of the one-rung ladder: §0 item 3, §11 X2c, §12 item 6, Claim C.5 status] Two wording changes.
- Replace 'proved completely' with 'proved at ε = 0 (d = 6); ε-uniformity only sketched (Prop C.4(e4) [P])'.
- Replace 'exact identification of … C_H' with 'C_H identified with its DR-linearity value under (V2); whole-integrand parametric value [P]'.

### Fix 7
[Prop C.4(e3)] Two corrections.
- (a) Qualify step 1. The ξ-uniform constants hold only for ε < 1/2. For 1/2 ≤ ε < 1, ₂F₁(1/2,1;2−ε;z) diverges as z → (1−ξ)/(1−ξ/x) → 1 (ξ → 0), so the constants grow like ξ^{1/2−ε}. That is still integrable; alternatively extend by analyticity.
- (b) Correct 'simplex identity to 10⁻¹³–10⁻³¹'. The log shows only 5.6·10⁻¹¹ at ε = −0.3.

### Fix 8
[Lemma A.3(c), and 'computer-assisted' in §1.5] State the verifier's two limitations, and preferably remove them.
- The closed-form check in r3_archive_verify.py is an exact-arithmetic evaluation at 3 random rational points, i.e. a randomized identity test. Replace it with an exact symbolic test, e.g. sympy.cancel(num/den − c·expected) == 0.
- Coverage of each U_R and of the base by the archived cells is not machine-checked; add a coverage check. review_final_scripts/chk_coverage.py does this by sampling and found 0 uncovered points.

### Fix 9
[Minor wording and precision]
- Thm B.5: for θ < 2 the lower bound is ≥ λ²/4 (from A,B ≤ 2us), not s/4. Optionally add the cover-independent optimality argument: Σ items ≥ |∫r| = 4λ²(1+o(1)).
- Prop A.6(a): state δ = 10⁻³, 10⁻⁵, 10⁻⁷, m² = 0.01 and P = P′ = 1/√2 for the proxy numbers. Say that the refutation needs only the divergence of the positive parametric integral.
- Lemma C.2 step 1: a factor propagated from level l has coefficient −2k_l⁺.
- §3: replace 'All three round-2 reviewers' with 'reviewers r2_1, r2_2, r3_1 and r3_2'.
- §9: (V2) also enters the (V1) statement for the triangle, through the zero-bin chain terms and the analytic regulator for 1/(D_gh_1h_2). Props B.2–B.3 prove (FI).
- Add a [rev] flag to Prop B.7 and to Thm E.3(iii).
- OQ1: add the Belitsky–Smirnov positioning.
- §17: record the deliberate downgrade of the round-2 (M2) clause in Cor A.5 (a deviation from r3_2 fix 2), and the decision on (RA2).
