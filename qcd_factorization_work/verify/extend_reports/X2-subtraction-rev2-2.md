# X2-subtraction-rev2-2

(extracted verbatim from the workflow journal; structured output of the agent)

## overall

fixable_issues

## per_result

### [per_result 1]
PROCESS — answer to the relayed question 「在正常运行吗」: 在运行，但不完全正常 (it is running, but not fully normally). (1) The four extension computations run normally. However, verify/extend/X2-subtraction/REPORT.md, review_r1_1.md and review_r1_2.md still do not exist; the directory holds only logs/ and scripts/. The harness refuses report files written by subagents, and the workflow script never writes the structured outputs to disk. (2) What I reviewed is the current revised report, i.e. the fix-round-1 StructuredOutput: journal.jsonl line 97, agent a3b63d44b69bba4fe, a summary plus 28 results and 14 open items. I extracted it myself from ~/.claude/projects/-Users-hao-cheng-Desktop-theorem-proof/c211c739-758d-4b40-bbac-67f4e1a65da4/subagents/workflows/wf_52f29317-58b/journal.jsonl and did not use the sibling reviewer's reconstruction. I cross-checked it against the round-0 output (line 38, agent ad47b382e8e1e17ed), the blocked round-0 draft (it covers §0–§2.5 only and is stale) and the two round-1 reviews (lines 74 and 70). Copies are in /private/tmp/claude-501/-Users-hao-cheng-Desktop-theorem-proof/c211c739-758d-4b40-bbac-67f4e1a65da4/scratchpad/x2r2_2/. (3) The first round-2 X2 reviewers (agents a42cd3e182277b640 and a31f06205f284fcbd, started at journal lines 98–99) have no recorded result, and their transcripts stop at 02:40. This run relaunched the same keys at 03:21. (4) For the same policy reason, review_r2_2.md was NOT written. This StructuredOutput is the review and must be written to disk by the orchestrator. My check scripts are in .../scratchpad/x2r2_2/chk/: c1_cert_audit.py, c2_scaling_family.py, c3_triangle.py, c4_eps_items.py.

### [per_result 2]
[X2-Setup] CORRECT. The models (M1)–(M3), the conventions and the grade mapping are consistent with WRITER_SPEC. The statement 'No QCD claim is made anywhere' is respected throughout.

### [per_result 3]
[X2-Thm2.6, fibered subtraction theorem] CORRECT as an implication with premises (AR), (ID) and (CS1φ)–(CS3φ). I re-derived the pointwise identity r=(1−T_R0)X_R0−Σ_{R≰R0}C_R; the triangle inequality on a finite cover and linearity of residue sums then give the norm bound, and (CS3φ)+(ID) give the integrated statement. The grade [R, R_cond] and the new error label E-N^φ are appropriate. Minor scope point: besides Glauber pinches and space-like real-base poles, graphs containing q⁺=0 subloops (pure zero modes, Prop 3.12(iv)) also lie outside (AR). The scope paragraph should say so, because those graphs are treated outside the fibered framework.

### [per_result 4]
[X2-Lem2.7, identification] PROOF GAP; the conclusion is fine where it is actually used. (a) The domination step argues that after a pole substitution every factor satisfies |·_η| ≥ |·_0|, so that |ρ_{F,η}| ≤ G. This works for denominators only. 𝒱 explicitly allows e_j<0, and the lemma is invoked for C_H=D_g/(t1 h1 t2 h2), whose numerator is D_g. For a numerator factor the inequality goes the wrong way, so |ρ_{F,η}| ≤ G does not follow. Either restrict the lemma to e_j ≥ 0 (no i0 in numerators) or supply a dominator for the η-dependent numerator. (b) The triangle 'check' is purely numerical: relative agreement 7.5e-8 to 4e-7, and 1.5e-5 to 8.6e-5 at P=P'=1/√2. Hypotheses (I1) and (I2) were not verified for the triangle's Collins terms. Exact identification is nevertheless easy, and I derived it in closed form from the Prop 3.1 densities (normalization μ^{2ε}/Γ(1−ε), measure dx dκ κ^{−ε}): ∫C_S=Γ(ε)²Γ(1−ε)(μ²Q̃²/m⁴)^ε/Q̃². ∫C_C1=Γ(ε)Γ(−ε)Γ(1−ε)(μ²/m²)^ε/(Γ(1−2ε)Q̃²), where the x>P part −Γ(1−ε)Γ(ε)(m²)^{−ε}/(εQ̃²) cancels the +1/ε of B(−ε,1−ε). ∫C_C2 equals ∫C_C1 only because the sliver contributes Γ(1−ε)Γ(ε)(m²)^{−ε}[Γ(−ε)Γ(1−ε)/Γ(1−2ε)+1/ε]/Q̃². ∫C_H=Γ(1+ε)Γ(1−ε)²(μ²/Q̃²)^ε/(ε²Γ(1−2ε)Q̃²). sympy confirms that these equal the stated covariant values identically and that Σ_R∫C_R → L̃²+π²/3 as ε→0. So (ID) at N=1 is exact, but by direct computation, not via Lemma 2.7. (c) The wording 'massless on-shell triangle plus scaleless terms' is imprecise: the term 1/(D_g h1 h2) in the covariant decomposition of C_H is boost invariant, so dimensional regularization does not regulate it (see Thm 4.3). Only the combination C_H has a well-defined value.

### [per_result 5]
[X2-Lem2.8, tropical certificate lemma] CORRECT. I checked the Borinsky citation on INSPIRE: AIHPD 10 (2023) 635. The weak-sharp-minimum bound and the Laplace estimate are valid, and so is the equivalence between a bounded argmax and negative recession slopes. Audit of r1_lptools.py: the exact primal–dual optimality check and the 2D recession check (quadrant pieces, endpoints plus tie points, exact) are logically correct. LATENT DEFECT: when the exact dual has free parameters, _certify first sets them to 0 but still computes rank(A_S) over the whole floating support S. Complementary slackness forces tightness only where y_i>0, so the face dimension, and hence the L-power, could be understated. My audit of all 546 archived triangle monomial certificates (r1_triangle_certificates.json) found no exact zero dual entry, so the triangle L-powers are valid. The bubble certificates were not archived and cannot be audited. The recession check for n≥3 is floating-point only; it is not used in any proof here.

### [per_result 6]
[X2-Lem2.10/Cor2.11, light-cone positivity] CORRECT. I re-derived the following. With V=2ℓ+1 vertices for the vertex graph and 2ℓ+2 for DIS, every ordering has 2ℓ and 2ℓ+1 states respectively. Every energy denominator is negative, including the crossed ordering (emission before absorption), where the bound improves to (m²+Q²(1+1/x))/2p⁺. The convexity bound uses the total plus momentum p⁺. The rejection of review r1_2's 1/ξ variant is right. The UV-finiteness criteria ω=4−E−V in (M1) and ω=6−2E in (M2) are correct, and all subgraphs of a ladder have E≥4.

### [per_result 7]
[X2-Lem2.12] CORRECT (trivial). Re-derived via d⁴l=π²|l|²d|l|² and |l|²=(1−z)(t−zv).

### [per_result 8]
[X2-Prop3.1, triangle densities] CORRECT. I wrote my own residue code from the 4D definitions (D_g, D1, D2, e_i, h_i, t_i with C_S, C_C1, C_C2 and C_H=D_g/(t1h1t2h2)); C_H=(1/D_g)(1/t1−1/h1)(1/t2−1/h2) was re-derived. It reproduces the t4 tables F/Fbig, which every LP certificate uses, to a maximum relative deviation of 3.5e-21 (300 random points × 5 terms, both 0<u<1 and u>1). It reproduces the sliver numerator and denominators of r1_triangle_recert to 1e-22. ρ_CS, ρ_CC1 and ρ_CH vanish identically on the sliver, as claimed.

### [per_result 9]
[X2-Prop3.2, sliver] CORRECT at ε=0. Re-derived: ∫dκ ρ_CC2=ln(a/(a−w))/(PP'w), and then ∫_0^a dw/2 gives Li₂(1)/(2PP')=ζ₂/Q̃², independent of m. Minor: 'recession slopes −1/2' holds at ε=0. At ε₀=1/10 the log shows −9/20.

### [per_result 10]
[X2-Thm3.3, triangle at the sharp exponent] CORRECT as a fibered, computer-assisted statement, with one small GAP in the integrated corollary. Evidence: the densities and the LP logic were audited as above; the cell constraints (S, C1 parts I/II/III, C2 and the sliver), the item list and the supersets are correct; and all items are present ((1−T_C2)X_C2 on the sliver equals r there). Independent direct numerical integration (c4_eps_items.py, λ²=1e-4…1e-10): (H1)_S and (H2)_S C_C1 scale exactly as λ^2.000 at ε=0 and λ^1.600 at ε=1/10. (H1)_C2 and the 0<u<1 remainder have local exponents 1.81→1.90, i.e. λ²L, at ε=0 and approach 1.6 at ε₀. All of this matches the certified λ², λ²L^{≤2} and λ^{8/5}. GAP: '|I_Γ−Σ I_{C_R}| ≤ … by Thm 2.6 and Lemma 2.7' relies on Lemma 2.7, whose hypotheses were not checked. Replace that step by the closed-form identification given above.

### [per_result 11]
[X2-Thm3.5/Prop3.6] CORRECT. Independently confirmed: ∫r=[4Li₂(−m²)+(L̃²+π²/3)m⁴]/(1−m⁴) against Φ^(1)/Q² (the ρt=m² identity was checked algebraically). The Q-unit expansion −4m²/Q⁴+(m⁴/Q⁶)(L_Q²−15+π²/3) leaves a residual of about 5 m⁶L² for m²=1e-3…1e-5, which is consistent with O(m⁶L²).

### [per_result 12]
[X2-Thm3.9, bubble chains, hybrid model] CORRECT as a fixed-j, hybrid-model, computer-assisted statement, with the model assumption of Lemma 3.7 stated honestly. Checks: the rectangle rule was re-derived (A/B=(um²v+κ)/(um²+κ), |δ| ≤ u²m²/(um²v+κ), and the trivial alternative |δ| ≤ ln(1/v)). The single-shell claims were verified by pole analysis: on the sliver, Γ and C_C2 both close downward on the D₂ pole, with the ln D_g cut above the axis; for 1<u≤2, C_S and C_C1 sit on the e shell, C_C2 and C_H on the h shell, and Γ=0. The logs confirm 330 cells with minimum exponent 2 at ε=0 and 1.6 at ε₀. Caveat: the bubble certificates were not archived, so the latent face-bound defect cannot be excluded for the L-powers L^{j+2}. The λ-exponents are unaffected.

### [per_result 13]
[X2-Prop3.12, one-loop DIS graphs] CORRECT after the repair. Checks: (i) The graph list (2+4+2+4+1=13 graphs at O(g²)) is complete. (ii) T_H∘R=R∘T_H holds, and the BPHZ counterterm does not drop out of (1−T_H)R because it multiplies S(P). (iii) The vertex algebra v₀H₀−vH=−zm²(v₀+H) and H ≥ zc_x are correct. (iv) The self-energy subtraction gives g=(c−c₀)²/((a+c)(a+c₀)²). I derived Σ_R(s)=(1/6)[s ln(s/s₀)−s+s₀] and |d/ds(Σ_R/s²)|=0.87123 at s=1/2, s₀=1, which reproduces the logged self-energy norm 0.87123 m² analytically. Minor points: the graphs in (iv) violate (AR) (q⁺=0 zero modes) and are treated outside the fibered framework, which should be said explicitly. Graph (v) is infinite (∝1/t at t=0), so 'excluded from the forward amplitude' must be stated as a definition: the observable is the x-dependent part (or the discontinuity).

### [per_result 14]
[X2-Thm3.13, massive photon] CORRECT. I re-derived ∫r=−M²Σ_k M^{2k}[1/(1+k)²+L/(1+k)]=−λ²(L+1)−λ⁴(L/2+1/4)+…. The (CS3) failure is properly attributed (Collins §10.5–10.6; Collins–Hautmann PLB 472 (2000) 129, verified on INSPIRE).

### [per_result 15]
[X2-Prop3.14, space-like vs time-like] CORRECT as rewritten. I re-derived: k∝n_A is incompatible with k²=M²>0; the Gram determinant is −16P²P'²(1−e^{−4Y})²; the pole sits at x₀=√((M²+κ)e^{2Y}/2) and is displaced to x₀−i0; and the result equals PV−iπ·Res, which equals the integral along the upward-deformed contour. The withdrawal of the 'genuine pinch' is correct.

### [per_result 16]
[X2-Thm4.1/Prop4.2, two-loop algebra] CORRECT. Against R6's definition of (Abs), Z_{R∧R'} ⊆ Z_R ∪ Z_R', I re-derived the literal-convention failure on line a2: Z_C1S(a2) contains k2⁺, while Z_C1C1(a2)=∅ and Z_HS^lit(a2)={k2⁻,k2T,M}, because Def. D.18 lets H see π₊(p1−k2). The soft-first convention works. The 'sufficient, not necessary' wording is right.

### [per_result 17]
[X2-Thm4.3, two-loop exact integrated remainder] GAP in (i); the downstream claims are overgraded. I re-implemented the homogeneity analysis independently (c2_scaling_family.py). It reproduces 1 non-homogeneous pattern (Γ), 9 singles with a unique scaling (k_R=0,1,1,2,2,2,3,3,4) and D0=0 for all 50 patterns. But the claim that the 40 composites are 'homogeneous along a one-parameter family' is FALSE for 22 of them: the family dimensions are 1 (18 patterns), 2 (15), 3 (6) and 4 (1). Each of the 22 patterns with dimension ≥2 contains a nonzero m²-independent rescaling with ZERO ε-weight, i.e. an exact, ε-independent invariance that dimensional regularization does not regulate (a rapidity-type divergence). Explicit example: the coefficient −1 pattern with a1→2Pk2⁻, b1→2P'k2⁺ and k2 absent from a2 and b2. It is invariant under the k2 boost (0,0,0,2,−2,0), and its subintegral is ∫d^dk2/(k2²·2Pk2⁻·2P'k2⁺). For these 22 patterns 'scaleless ⇒ 0 in DR (standard convention)' does not follow from DR; their vanishing needs an auxiliary regulator, e.g. independent analytic powers on the D₁- and D₂-type lines, which give the boost direction weight δ_a1−δ_b1. One must also show that the 9 singles are regular, and ∫Γ and ∫r continuous, as the regulator is removed. So (i) is not an '[R, exact symbolic check]', and (ii) needs this premise; the cleanest form of (ii) is ∫Γ−∫r=Σ_{9 singles}∫T_RΓ. The final NLP formula is very likely right: I re-derived the expansion of the UD closed form to −λ²(L̃⁴/2+π²L̃²+12+7π⁴/30), and the QMC values agree. Further gaps: 'every remainder norm ≥ |∫r|' equates the fibered ∫ρ_r with the covariant ∫r, i.e. it uses (ID) for r at two loops, which O11 lists as unverified. That must be added as a premise. 'NEW' is overstated: the identity is the standard overlap/zero-bin scalelessness statement (modulo the gap above), and the NLP coefficient is an elementary expansion of a known closed form.

### [per_result 18]
[X2-Num-2loop] CORRECT as [P]. I recomputed the pulls from the logs: for ∫Γ −1.13, +1.27, −1.22, +0.16; for ∫r +0.49, −2.40, −0.15, −0.17. The full-norm ratios 31.25, 31.66, 31.5 and 32.3 λL are reproduced. The withdrawn fits are correctly labelled.

### [per_result 19]
[X2-Lem5.2, DIS ladder structure] CORRECT. Propagation of the invariant by Cauchy–Schwarz (weights z(1−ξ) and 1−z, summing to 1−zξ) was re-derived, giving v ≥ |K|²/(1−ξ) for all chains and H^(0)>0. The pole-side argument is now written out and is sound.

### [per_result 20]
[X2-Lem5.3, hard-factor lemma] CORRECT. Re-derived: ⟨1/(a+b cosθ)⟩_{S³}=2/(a+√(a²−b²)); (i) d ≥ zξc_x; the bound d̄ ≥ 1−z+zξc_x+|l|²/(1−z); (iii) from −dφ/da together with a²−b² ≥ a·d_min; and (iv).

### [per_result 21]
[X2-Prop5.1', one-rung ladder] CORRECT at ε=0. I checked every inequality of (a): the region-B bounds (|h−ĥ| ≤ (8/7c_x²)(v+2|k|) with |k| ≤ m/2 ≤ c_x/16, giving δ+(4/5)√((1−z)δ) and δ+4√((1−z)δ)), the region-A decomposition with |κ₁−κ₀| ≤ 2δ/(π²(1−z)t³) and |h₁−h₀|=δh₁h₀, and the direction-averaged |k|>c_x/4 bounds via Lemma 5.3. I also checked (b) and (c), and (d): the derivation of c₁ via ⟨|cosθ|⟩=4/(3π) and ∫(2y+1)y^{−1/2}(1+y)^{−2}dy=3π/2, with c₁(2)=1.262983875, c₁(1.3)=1.936673 and c₁(5)=0.924158 (recomputed). Minor: the sentence 'for ε∈(0,ε₀] the bounds hold with λ^{1−2ε₀}' is asserted rather than proved; it must handle the (1−z)^{1−ε} and (t−zv)^{1−ε} factors of Lemma 2.12's ε-form. My (CS2)_{R1} bound c(1−z)[(1−z)m²+4(1−z)m] is slightly sharper than the stated one; this is harmless.

### [per_result 22]
[X2-Thm5.1, ladders of all n] Correctly DOWNGRADED to [P]. Gaps g1–g5 and the scope (φ³₆ only, no complex-ω uniformity, slot X2c not delivered) are stated honestly.

### [per_result 23]
[X2-Prop5.4] CORRECT (algebra: C_A=H(πk)J, C_H=ΔH·J̃, r=ΔH·ΔJ).

### [per_result 24]
[X2-Thm6.1, all-order conditional theorem] CORRECT as a conditional statement. The status table needs corrections. (a) '(AR)+(ID) for all terms at N=1 (exact identification, Lemma 2.7)': the identification is exact, but by the closed forms above, not by Lemma 2.7. (b) 'Exact integrated N=2 planar remainder [R, R_cond]' inherits the regulator gap of Thm 4.3(i). (c) POSITIONING is incomplete. Ma, JHEP 05 (2020) 012 [arXiv:1910.11304] is 'A Forest Formula to Subtract Infrared Singularities in Amplitudes for Wide-angle Scattering': a BPHZ-like forest formula built on Collins' Sudakov analysis and Erdoğan–Sterman, with a proof that the singularities of its subtraction terms cancel pairwise. The report cites it only as 'polytope and region' literature, which misdescribes it. Also missing: Feige–Schwartz, PRD 90 (2014) 105020 [1403.6472] (all-order hard-soft-collinear factorization of amplitudes) and Erdoğan–Sterman, PRD 91 (2015) 065033 [1411.4588]. Consequently, the claim in Thm 6.1, O1 and O10 that identifying the region expansion with nested subtraction terms is 'genuinely open' must be narrowed: it is open for the off-shell (M1)/(M2) integrand-level integral-norm version, not for on-shell amplitudes at the level of pairwise cancellation.

### [per_result 25]
[X2-Err] (a) CONFIRMED (independent hand check). (b) Sharpening, not an error: correct. (c) Remark: correct. (d) CONFIRMED (s^{1−ε}P^{−ε}/ε re-derived). (e) The withdrawal is correct. (f) CONFIRMED. (g) Correct.

### [per_result 26]
[X2-Err-own] CORRECT. Note that the retracted 'exponent 1 is optimal' text still exists in the blocked draft and in scratch copies (scratchpad rev_x2/X2_REPORT_attempted.md and x2r2_1/X2_REPORT_orig.md). REPORT.md must be written from the fix-1 output only.

### [per_result 27]
[X2-Est] CORRECT, except that the two-loop line inherits the Thm 4.3 gap. The bubble entry C_j ≳ 2j!/L₀^{j+2} is consistent with the reported UV-tail numerics.

### [per_result 28]
[X2-Slots] CORRECT. X2a is delivered in fibered form; once the identification is done in closed form, its integrated version is also rigorous. X2b, X2c and X2d are correctly marked not delivered or open.

### [per_result 29]
[X2-REVISIONS] ACCURATE. Every round-1 item I traced (r1_1 R1–R21 and F0–F12; r1_2 F0–F12) is addressed, with one exception: the requirement to archive the exact certificates is met for the triangle but NOT for the bubble class (only summary logs/JSON).

### [per_result 30]
OPEN ITEMS O1–O14: reasonable and honest. O4 should add that 22 of the 40 composite two-loop patterns carry ε-independent (rapidity-type) invariances. Any check of (CS3φ) for an individual two-loop C_R must therefore show that they cancel inside that C_R, as happens at one loop for 1/(D_g h1 h2) inside C_H; otherwise (CS3φ) fails, as in the massive-photon case. O1 and O10 need the positioning in the Thm 6.1 entry.

### [per_result 31]
NOVELTY: INSPIRE full-text and title searches ('Collins subtraction'+tropical, subtraction+'integral norm', 'Newton polytope'+factorization, tropical+factorization, and others) found no prior LP/tropical certification of Collins-type subtraction conditions, so the narrowed novelty claim stands. Citations verified on INSPIRE: Borinsky AIHPD 10 (2023) 635; Poldaru arXiv:2607.26291 exists ('Expansion by Regions Derivation from the Mellin Transform', unpublished); Gardi–Herzog–Jones–Ma–Schlenk JHEP 07 (2023) 197; Arkani-Hamed–Hillman–Mizera PRD 105 (2022) 125013; Jantzen JHEP 12 (2011) 076; Semenova–Smirnov–Smirnov EPJC 79 (2019) 136; Ma JHEP 09 (2024) 197 = 2312.14012; Ligterink–Bakker PRD 52 (1995) 5954; Collins–Hautmann PLB 472 (2000) 129. Ma JHEP 05 (2020) 012 = 1910.11304 is the forest-formula paper discussed above.

## required_fixes

### [required_fixes 1]
F0 (process, blocking). The orchestrator or main session must write verify/extend/X2-subtraction/REPORT.md verbatim from the fix-round-1 StructuredOutput (journal.jsonl line 97, agent a3b63d44b69bba4fe). It must also persist review_r1_1 (line 74), review_r1_2 (line 70) and this review. Change the workflow so that reviewers and fixers receive the structured outputs directly, because subagents cannot write report .md files. Never use the stale truncated draft.

### [required_fixes 2]
F1 (Thm 4.3(i)). Replace 'the 40 composites are homogeneous along a one-parameter family' by the correct statement: the family dimensions are 1 (18), 2 (15), 3 (6) and 4 (1). State that the 22 patterns with dimension ≥2 carry an exact ε-independent invariance (example: the k2 boost (0,0,0,2,−2,0) of the pattern a1→2Pk2⁻, b1→2P'k2⁺, which contains ∫d^dk2/(k2²k2⁺k2⁻)). For these patterns 'scaleless ⇒ 0 in DR' does not hold. Then either introduce an auxiliary analytic regulator (e.g. independent propagator powers), prove that all 40 composites vanish under it, that the 9 singles are regular at zero regulator, and that ∫Γ and ∫r are continuous as the regulator is removed; or downgrade (i) to [R, R_cond] with that premise. Restate (ii) as ∫Γ−∫r=Σ_{9 singles}∫T_RΓ. Apply the same correction to the one-loop wording 'massless triangle plus scaleless terms', since 1/(D_g h1 h2) is boost invariant.

### [required_fixes 3]
F2 (Thm 4.3 consequence). 'Every remainder norm ≥ |∫r| ≥ ½λ²L̃⁴(1+o(1))' requires the fibered ∫ρ_r to equal the covariant ∫r at two loops, i.e. (ID) for r, which O11 lists as unverified. Add (ID) for r as a premise (currently supported by the QMC agreement) or prove it.

### [required_fixes 4]
F3 (Lemma 2.7 and its uses). Repair the domination step for numerator factors (e_j<0; ρ_CH has D_g in the numerator): restrict the lemma to e_j ≥ 0 with no i0 in numerators, or give an explicit η-uniform dominator. Replace the numerical triangle check by the closed-form identification: ∫C_S=Γ(ε)²Γ(1−ε)(μ²Q̃²/m⁴)^ε/Q̃²; ∫C_C1=∫C_C2=Γ(ε)Γ(−ε)Γ(1−ε)(μ²/m²)^ε/(Γ(1−2ε)Q̃²), where the sliver term Γ(1−ε)Γ(ε)(m²)^{−ε}[Γ(−ε)Γ(1−ε)/Γ(1−2ε)+1/ε]/Q̃² is needed for C_C2; ∫C_H=Γ(1+ε)Γ(1−ε)²(μ²/Q̃²)^ε/(ε²Γ(1−2ε)Q̃²); Σ_R∫C_R → L̃²+π²/3. Update the integrated corollary of Thm 3.3 and the N=1 row of Thm 6.1 so that they rest on this computation, not on Lemma 2.7.

### [required_fixes 5]
F4 (certificate tooling). In r1_lptools._certify, compute the face-dimension rank over S⁺={i: exact y_i>0}, or assert y_i>0 on S, before using dim F ≤ (n+K)−rank. Re-run the bubble-class certificates and archive them (cells, exact duals, primal points), as was done for the triangle; the triangle archive passes this audit (no zero duals among 546 certificates). Note that the n≥3 recession check is floating-point only.

### [required_fixes 6]
F5 (positioning and literature). In Thm 6.1, O1, O10 and the novelty paragraph of Lemma 2.8: describe Ma, JHEP 05 (2020) 012 [1910.11304] correctly, as a BPHZ-like IR forest formula for wide-angle amplitudes with pairwise cancellation of the singularities of its subtraction terms. Add Feige–Schwartz, PRD 90 (2014) 105020 [1403.6472] and Erdoğan–Sterman, PRD 91 (2015) 065033 [1411.4588]. Narrow the 'genuinely open' claim to the off-shell, integrand-level, integral-norm version of the identification.

### [required_fixes 7]
F6 (novelty labels). Relabel Thm 4.3 from 'NEW' to an explicit check: the identity is the standard overlap/zero-bin scalelessness statement (subject to F1), and the NLP coefficient is an elementary expansion of the Usyukina–Davydychev closed form.

### [required_fixes 8]
F7 (minor wording). Prop 3.2: the recession slopes are −1/2 at ε=0 and −9/20 at ε₀=1/10. Prop 3.12: say that graphs (iv) lie outside (AR) and are handled outside the fibered framework, and that graph (v) is infinite at t=0, so the observable is defined as the x-dependent part. Prop 5.1': prove the λ^{1−2ε₀} ε-uniformity sentence or mark it as a sketch. O4: add the 22 rapidity-type composites and the resulting requirement that (CS3φ) for an individual two-loop C_R shows their cancellation inside that C_R.
