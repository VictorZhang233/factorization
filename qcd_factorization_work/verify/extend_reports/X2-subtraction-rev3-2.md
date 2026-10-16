# X2-subtraction-rev3-2

(extracted verbatim from the workflow journal; structured output of the agent)

## overall

fixable_issues

## per_result

### [per_result 1]
[0] RUN STATUS（回答「在正常运行吗」）: 在运行，但不完全正常 (running, but not fully normal). Workflow wf_52f29317-58b is running. X2-subtraction-fix2 (agent aa54636b3bf3d0143) finished at about 05:12; its result is journal.jsonl line 122 (1-based). X2-subtraction-rev3-1 (a1e6a339abd0d5c94) and this review, rev3-2 (a9d8f3708ecf49f68), started at 05:12, and X3-ope-fix2 was still active. (1) The input file verify/extend/X2-subtraction/REPORT.md does NOT exist: the directory holds only logs/ and scripts/, and no review_r*.md files exist either. I reviewed the fix-round-2 StructuredOutput, extracted verbatim from ~/.claude/projects/-Users-hao-cheng-Desktop-theorem-proof/c211c739-758d-4b40-bbac-67f4e1a65da4/subagents/workflows/wf_52f29317-58b/journal.jsonl. The copy is /private/tmp/claude-501/-Users-hao-cheng-Desktop-theorem-proof/c211c739-758d-4b40-bbac-67f4e1a65da4/scratchpad/x2rev3_2/fix2_readable.md; the earlier rounds (orig, rev1_*, fix1, rev2_*) are extracted to the same directory. (2) I did NOT write review_r3_2.md: subagents are not allowed to write report or review .md files. This StructuredOutput is the review, and the orchestrator must write it to disk. (3) My independent check scripts are in .../scratchpad/x2rev3_2/chk/: c1_triangle_id.py, c2_ladder.py, c3_ladder_CH_dr.py, c4_archive_audit.py, c5_twoloop_vals.py, c6_O15.py, c7_M1_IR.py.

### [per_result 2]
[1] X2-Setup: CORRECT, with one caveat. I re-derived the normalisation (1/Γ(1−ε))∫dx dκ κ^{−ε} ρ from the 4D residue: πi·π^{1−ε}/(iπ^{2−ε}Γ(1−ε)). Defining I_F by parametrising the whole integrand is a consistent convention. For C_H it reproduces the analytic-regulator / DR-linearity value, which is the massless on-shell triangle. Caveat: the model (M1) itself (massless φ³ in d=4, coupling of mass dimension 1) is IR divergent beyond one loop for some graphs; see [5] and [24]. The Setup should say that (M1) is used at one loop and for IR-finite graph classes only.

### [per_result 3]
[2] X2-Thm2.6: CORRECT as an implication from (AR), (ID) and (CS1φ)–(CS3φ). I re-derived (D.10): r=(1−T_R0)X_R0−Σ_{R≰R0}C_R pointwise, with linearity of the fibre integrals under (AR). Removing the unused UV-boundedness hypothesis makes the theorem consistent with the cover of Thm 3.3. The scope sentence ('absolutely integrable ... e.g. (M1)') is too broad: (M1) graphs with self-energy insertions on lines that can go soft have ρ_Γ∉L¹ (see [5]). They must be added to the scope exclusions.

### [per_result 4]
[3] X2-Lem2.7: CORRECT as a lemma for products of pure denominators. The domination uses Re(·_η)=Re(·_0) after each pole substitution, and the closing sides do not depend on η. I reproduced the (I2) failure for C_C1 independently: 462.7177, 1644.848, 4614.224 and 12072.96 for δ=1e-4, 1e-8, 1e-12, 1e-16 at ε=0.1, growing like (δ^{−ε}−1)/ε. Minor GAP: the lemma concludes ∫_Bρ_F=lim_{η→0}∫d^dk F_η, a limit of absolutely convergent Minkowski integrals, but (ID) is equality with the parametric value I_F of Setup (i). The bridge lim_{η→0}∫F_η=I_F is never stated: exponentiate at finite η, exchange the integrals, do the Gaussian l-integral, then let η→0. The statement '(ID)_Γ ⇐ (I1)' needs this step, so it must be listed as part of (I1) or cited as a standard fact. My Minkowski power counting agrees with the stated plausibility of (I1): the cones {k²=0, p_i·k=0} contribute ∫R^{−1−2ε}ln²R dR.

### [per_result 5]
[4] X2-Lem2.8 and r2_lptools: CORRECT; the S⁺ repair is logically right. Data-only audit of the bubble archive (c4_archive_audit.py), all as reported:
- 2986 records and 70,373 certificates;
- every dual entry is >0, and S⁺ equals the support of y;
- the S⁺ repair changes no dimension bound; the maximum bound is 2;
- c·x+const equals the stated value for every certificate;
- every primal X satisfies the stored cell constraints;
- every record exponent equals −2·max(value);
- minimum exponents: 2 and 8/5 (items and 0<u<1), 2 and 9/5 (u>1), 8 and 36/5 (corner).
Triangle archive: 546 certificates, no zero duals, face bounds {0:251, 1:207, 2:88}, as reported; the exponent-1 records belong to the θ=1 family only. Limitations: (i) the archive does not store the denominator supports or the LP rows, so dual feasibility (A_Sᵀy=c and b·y) cannot be re-checked from the archive alone; (ii) the fix-2 text writes 'Equivalently (proved)' but drops the proof that a bounded argmax face is equivalent to ψ_inf<0 on rec(U)∖0, which fix 1 contained. The equivalence is true; I checked it via ψ(x+tr)≥ψ(x)+tψ_inf(r).

### [per_result 6]
[5] X2-Lem2.10/Cor2.11: Lemma 2.10 is CORRECT. Cor 2.11 is WRONG as stated for (M1).
- The flaw: the proof step '∫ρ_Γ=I_Γ<∞ by the LCPT–covariant equivalence' takes UV finiteness for finiteness. Massless (M1) is super-renormalizable. Self-energy insertions on internal lines that can go soft make it IR divergent at off-shell external momenta (Jackiw–Templeton, PRD 23 (1981) 2291). The LCPT input does not supply IR finiteness.
- Counterexample satisfying every stated hypothesis (UV finite, no one-loop two-point subgraph, no tadpole, loop plus momenta not constant): the three-loop triangle whose gluon line carries the massless two-loop 'kite' self-energy, i.e. a ψ loop with an internal φ rung. The kite is UV finite (ω=−2) and Σ₂(k²)=c·6ζ₃·g⁴/(−k²). The k-integrand is c/((−k²)³D₁D₂) with D₁D₂→m⁴, so I_Γ has a power IR divergence. In parametric form this is Δ^{−3−3ε}, still divergent for ε near 0. By the corollary's own sign-plus-equivalence argument, ∫|ρ_Γ|=∞, so (CS3φ) fails.
- Numerics (c7_M1_IR.py) — fibred norm ∫_{x>δ} for δ = 1e-3, 1e-5, 1e-7:
  - triangle: 21.83, 22.82, 22.83 (converges);
  - proxy 1/(D_g²D₁D₂): 20203, 64422, 110003 (grows like ln(1/δ));
  - proxy 1/(D_g³D₁D₂): 2.46e8, 3.47e10, 3.50e12 (grows like 1/δ).
- The (M2) clause (φ³₆ ladders) is unaffected.

### [per_result 7]
[6] X2-Lem2.12: CORRECT (unchanged; re-derived in earlier rounds).

### [per_result 8]
[7] X2-Prop3.1: CORRECT. From the 4D propagators I re-derived:
- the pole sides;
- D̂₂=e₂[1+m²/Q̃²+κ/(Q̃²(1−u))]+κ;
- the sliver density ρ_Γ=2/(wD_gD₁);
- ρ_CC1=xm²/(Q̃²AB) for 0<x<P;
- ρ_CC2, including the cancellation of 1/κ for x>0;
- ρ_CH, from the t̂₂ pole for 0<x<P and the h₁ pole for x>P.
C_H=D_g/(t̂₁h₁t̂₂h₂) follows from T_H(Γ−C_S−C_C1−C_C2) because h_i−t̂_i=−D_g.

### [per_result 9]
[8] X2-Prop3.1′: CORRECT. I re-derived both sides by hand.
- Fibred side: the K1/K2 κ-integrals; J0=B(−ε,1−ε)+1/ε; J1=1/ε; assembly as stated, including the sliver for C_C2.
- Covariant side: Δ=λ₁λ₂Q̃²+m²(λ₁+λ₂) for C_S; Δ=(x+λ₂)(m²(1−x)+Q̃²λ₁) with even numerator part l²+Δ, giving Γ(1+ε)(2ε−1)Δ^{−1−ε}; Δ=Q̃²(x+λ₁)(1−x+λ₂) with numerator −l²−Δ, giving Γ(1+ε)(1−2ε)Δ^{−1−ε}. Every parameter integral converges absolutely for 0<ε<1.
- My own 2D quadrature without the κ-formula (c1_triangle_id.py) agrees to 3e-11–1e-9 at (P,P′,m²,ε)=(0.8,1.3,0.1,0.3) and to ≤5e-7 at (1/√2,1/√2,0.01,0.2).
- Σ_R C_R → L̃²+π²/3 (24.49746 against 24.49746 at m²=0.01).
- The remark that 1/(D_gh₁h₂) is boost invariant and not DR-regulated is right.

### [per_result 10]
[9] X2-Prop3.2: CORRECT. ∫dκ ρ_CC2=ln(a/(a−w))/(PP′w), and the w-integral gives Li₂(1)/(2PP′)=ζ₂/Q̃² (re-derived).

### [per_result 11]
[10] X2-Thm3.3: CORRECT as a fibred, computer-assisted statement. The integrated corollary is correctly graded [R, R_cond] with the single premise (ID)_Γ.
- I re-derived the lower bound ∫_{U_S}ρ_CC1≥s/4 (on U_S both A and B are ≤2um²).
- I confirmed (ID)_Γ numerically with my own Feynman-simplex value: 15.5610705037585 (rel. 3e-17), and 70.4057347500423 at (1/√2,1/√2,0.01,ε=0.2) (rel. 3e-28).
- I reproduced the O15 parametric form of the 0<x<P part (13.3963941598142, rel. 2.8e-17) and found fibred = covariant at (0.5,0.9,0.02,0.15) to 4e-29.
So the premise is certainly true; only its proof is missing.

### [per_result 12]
[11] X2-Thm3.5/Prop3.6: CORRECT. I re-derived ρt=m² and ∫r=4Li₂(−m²)/(1−m⁴)+(L̃²+π²/3)m⁴/(1−m⁴). The ratio ∫r/(−4m²) is 0.93636, 0.99777 and 0.99995 at m²=1e-2, 1e-4 and 1e-6.

### [per_result 13]
[12] X2-Thm3.9: The certified statement is CORRECT for the stated integrand class Γ^(j)=ln^j(D_g/μ²)/(D_gD₁D₂). The archive audit is in [4]. All shells are line-1 poles in the upper half plane, where ln D_g is real, consistent with the four-shell representation.
But the MODEL IDENTIFICATION is WRONG.
- In (M1), [g]=1. The ψ-loop self-energy is Σ_R(k²)∝g²[ln(−k²/μ²)+c]: dimension 2, not proportional to k².
- The MS-bar renormalised j-bubble chain of (M1) is therefore ∝g^{2j}[ln(D_g/μ²)+c]^j/D_g^{j+1}, not ln^j(D_g)/D_g.
- That chain is IR divergent in the soft region for j≥1: ln² for j=1, a power divergence for j≥2 (see [5] and [24]).
- 'The true d-dimensional renormalized chain is (−k²)^{−nε} times poles' is also wrong for (M1): it is (−k²)^{−n(1+ε)} times poles.
The certified class is the chain of a theory with a dimensionless coupling (gauge-theory-like vacuum polarisation, or φ³₆) grafted onto the (M1) triangle. The renormalon remark belongs to that analogy.

### [per_result 14]
[13] X2-Prop3.12: CORRECT (statements unchanged). The QCD colour remark is right: a single gluon attached to a colour-singlet current loop gives Tr t^a=0. But fix 2 says 'The proofs are as in round 1', so the proofs must be carried over into the final report.

### [per_result 15]
[14] X2-Thm3.13: CORRECT. r=−M²g₀/(Gt₁h₁t₂h₂) re-derived from h_i−t_i=−g₀ and g₀−G=−M².

### [per_result 16]
[15] X2-Prop3.14: CORRECT as rewritten.
(b) I re-derived the densities and poles by hand:
- for x>0, the h1Y residue gives ρ_CS=1/(P(S−2ex²−i0)(2P′x(1−e²)−i0));
- for x<0, the h2Y pole (k⁻=x/e−i0) is the only lower pole, giving ρ_CS=1/(P′(S−2x²/e−i0)(2Px(1−e²)−i0));
- c=1/(2PP′S(1−e²)) from both sides (90.90965 at M²=1e-3, Y=3, κ=0.01);
- residue −1/(4PP′S(1−e²)) at both −x₀′+i0 and x₀−i0, with x₀′=0.0036923 and x₀=1.48958;
- the r2_spacelike_poles.log values agree.
(c) I checked the text of Collins Ch. 10 §10.6.4, eqs. (10.67)–(10.69), in the open-access copy. (10.68) concerns the time-like form factor with k⁺→k⁺+iδ, k⁻→k⁻−iδ, and the quoted sentence is verbatim.
- The inherited −i0's are compatible with k±→k±−iδ in (M3): Im h1Y=−2P(1−e)δ and Im h2Y=−2P′(1−e)δ, with the t1 and t2 poles in the upper half planes.
- With Collins' pattern (h2Y→+i0) I also re-derived ρ_CS=0 for x<0, no pole at x=0, and poles at +x₀′−i0 and x₀−i0.

### [per_result 17]
[16] X2-Thm4.1/Prop4.2: CORRECT (unchanged; confirmed by both earlier rounds).

### [per_result 18]
[17] X2-Thm4.3: CORRECT as graded.
- I checked the logic of r2_twoloop_regulator.py (monomial weights of the line factors, K, K0, injectivity of Φ); the log gives the stated counts 18/15/6/1 and 22.
- (ii): deg P≤4 indeed follows from (F), because the singles carry only five distinct exponents k_R∈{0,…,4}: by a Vandermonde argument, the grouped pole coefficients of order ≥5 vanish. This deserves one sentence.
- I recomputed the values from the Usyukina–Davydychev (UD) closed form: −7.050661, −4.596744, −2.570489, −1.281728, −0.446917 and −0.0201338 at m²=0.04, 0.01, 0.0025, 0.000625, 1e-4 and 1e-6. The NLP ratios are 0.92448…0.999998.
- The text's 'm²=0.04…10⁻⁶' hides this non-uniform grid and should list it.

### [per_result 19]
[18] X2-Num-2loop: CORRECT as [P]. I recomputed the UD values 82.282433, 223.86342, 508.10197 and 1019.3828 at m²=0.04, 0.01, 0.0025 and 0.000625.

### [per_result 20]
[19] X2-Lem5.2: CORRECT (unchanged; verified in rounds 1–2). The fix-2 text is abbreviated (706 against 2323 characters in fix 1). The pole-side argument and the proof of the invariants must be carried over.

### [per_result 21]
[20] X2-Lem5.3: CORRECT (unchanged). Fix 2 omits the proofs, which must be carried over from fix 1.

### [per_result 22]
[21] X2-Prop5.1′:
(a)–(c) CORRECT (round-2 re-derivations). Fix 2 says 'unchanged from round 1', so the proofs must be carried over.
(d) CORRECT. I re-derived ∫t^{3/2}(t⁻²−(t+δ)⁻²)dt=3πδ^{1/2}/2 (=3B(1/2,3/2)) and ⟨|cosθ|⟩_{S³}=4/(3π). c₁(2)=1.262983875, c₁(1.3)=1.936673074, c₁(5)=0.9241577558. The E1 bound C(1−z)δ(1+ln(1/((1−z)δ))) checks. Two presentation gaps: (d)(ii) uses 'region A/B', which only fix 1 defines (A={v′₀>δ}, B={v′₀≤δ}); and c₁ depends on the measure dz d⁴k, which should be stated.
(e) C_R1 is CORRECT. I re-derived both sides independently:
- covariant: 2∫αdα·3∫dλ·Γ(1+ε)/6·Δ^{−1−ε}, with Δ=α(1−α)m²+λQ²(1−(1−α)/x);
- fibred: the rung-pole residue and ∫K^{1−ε}(K+a)⁻²dK=a^{−ε}Γ(2−ε)Γ(ε);
- both give Γ(ε)∫(1−ξ)^{1−ε}(ξm²)^{−ε}/(Q²(1−ξ/x)), and 11.27248142379893 and 27.06758503548673 at x=2 are reproduced.
C_H as [P] is correct. New observation: the whole-integrand value equals the DR-linearity value T_HΓ, because T_H C_R1 is scaleless with ε-weight −ε. This gives the closed form C_H=Γ(1+ε)Γ(−ε)Γ(2−ε)/Γ(2−2ε)·Q^{−2−2ε}∫₀¹y(y+(1−y)c_x)^{−1−ε}dy = −6.58496209517625, −3.57272130934842, −2.60783786095503 at ε=0.1, 0.2, 0.3 (x=2). The printed ε=0.3 value −2.60783786095414 is the fibred one.

### [per_result 23]
[22] X2-Thm5.1: CORRECT as [P]. But fix 2 (and O12) refers to 'gaps g1–g5' without listing them; the list exists only in fix 1, so the reference dangles.

### [per_result 24]
[23] X2-Prop5.4: CORRECT (algebra).

### [per_result 25]
[24] X2-Thm6.1: CORRECT as an implication, but one status item is WRONG and the status list is incomplete.
- 'VERIFIED: (CS3φ) for Γ at all orders, for UV-finite graphs without tadpoles' is false in (M1); see [5].
- From N=2 on, the graphs the theorem sums over include IR-divergent ones. Example: the triangle with the renormalised one-loop ψ-bubble on the gluon line, integrand ∝[ln(D_g/μ²)+c]/(D_g²D₁D₂), D₁D₂→m⁴. It has a ln² IR divergence at ε=0 and an IR pole in DR. Self-energy insertions on a soft quark line behave the same way.
- Hence F^(N) is itself IR divergent for N≥2, and for these graphs the premise (CS3φ) is FALSE, not merely unverified.
- The N≥2 content of Thm 6.1 in (M1) is therefore vacuous unless the graph class is restricted (e.g. no self-energy insertions on lines that can be soft) or the model is changed.
- This must be stated in Thm 6.1, in the summary item 'All-order conditional theorem', in O3/O10, and as a new open item. The positioning paragraph is fine.

### [per_result 26]
[25] X2-Err (a)–(g): CORRECT, as confirmed in round 2.

### [per_result 27]
[26] X2-Err-own: CORRECT.

### [per_result 28]
[27] X2-Est: CORRECT. I recomputed the one- and two-loop numbers and the DIS c₁ values. The bubble line should use the relabelled class (see [12]).

### [per_result 29]
[28] X2-Slots: CORRECT. X2a is delivered in fibred form and as [R, R_cond]; X2b and X2c are not delivered; X2d is open.

### [per_result 30]
[29] X2-REVISIONS: ACCURATE — I traced every item: rev2_1 [1]–[6] and rev2_2 F1–F7 are all addressed. INACCURATE claim: 'The COMPLETE REVISED REPORT is this structured output'.
- Fix 2 abbreviates items it marks unchanged, relative to fix 1: Prop 3.12 3458→1887 characters, Lem 5.2 2323→706, Lem 5.3 1077→497, Thm 5.1 2437→837, plus Thm 3.13 and the proof in Lemma 2.8.
- It defers proofs to 'round 1' while instructing that REPORT.md be written from fix 2 only.
- Following that instruction literally would produce an incomplete report with dangling references.

### [per_result 31]
[30] OPEN items: reasonable and honest. I verified O15 numerically (see [10]). Missing: an item on IR finiteness in (M1) beyond one loop (restricted graph class or a different model for Thm 6.1).

### [per_result 32]
[31] NOVELTY: my INSPIRE searches found no prior LP or tropical certification of Collins' (CS1)–(CS3) and no fibred integral-norm subtraction theorem, so the narrowed novelty labels stand.
- Queries: title 'light-cone ordered'; fulltext 'integral norm'+subtraction+factorization; 'linear programming'+'power counting'+pinch; 'Collins subtraction'+tropical; title tropical+(factorization|Sudakov|regions); 'forest formula'+infrared; fulltext Collins+subtraction+'Newton polytope'+certificate.
- Recent hits, none overlapping: Erdoğan–Sterman 2502.14230 (coordinate LCOPT review), Gardi 2609.29442 (Hidden Region Finder), Belitsky–Smirnov 2508.14298.
- Suggested citations: Collins arXiv:1801.03960 (when the elementary derivation of the light-front rules fails; zero modes), next to Chang–Yan and Ligterink–Bakker for the LCPT input; Jackiw–Templeton PRD 23 (1981) 2291 for the (M1) IR problem.

## required_fixes

### [required_fixes 1]
PROCESS (blocking; only the orchestrator can do it):
- Write REPORT.md from the fix-2 output (journal.jsonl line 122, agent aa54636b3bf3d0143) PLUS the full fix-1 text (line 97, agent a3b63d44b69bba4fe) for every item fix 2 marks 'unchanged' or 'as in round 1'. Do not write it from fix 2 alone. That includes: the proofs of Prop 5.1′(a)–(c) and the definitions of regions A/B; the list of gaps g1–g5 in Thm 5.1/O12; the proofs of Prop 3.12, Lemma 5.2 and Lemma 5.3; the proof of the recession equivalence in Lemma 2.8; the details of Thm 3.13 and Num-2loop.
- Persist reviews r1_1, r1_2, r2_1 and r2_2, and this review r3_2 (journal entry of agent a9d8f3708ecf49f68). I did not write review_r3_2.md because subagents may not write report files.

### [required_fixes 2]
Cor 2.11 (WRONG as stated for (M1)): add an IR-finiteness hypothesis, for example 'no self-energy insertion of any loop order on an internal line that can become soft', or simply 'I_Γ finite'. Replace '∫ρ_Γ=I_Γ<∞ by the LCPT–covariant equivalence' with '=I_Γ, finite by hypothesis'. Record the counterexample: the triangle with the massless two-loop kite self-energy on the gluon line, whose k-integrand is c/((−k²)³D₁D₂) and is power IR divergent. Keep the (M2) clause unchanged.

### [required_fixes 3]
Thm 6.1 (and the summary, Setup, the scope of Thm 2.6, O3/O10, and a new O16): state that massless (M1) is super-renormalizable and IR divergent beyond one loop for graphs with self-energy insertions on lines that can go soft (Jackiw–Templeton 1981). Example: the renormalised one-loop ψ-bubble on the gluon line of the triangle gives a ln² IR divergence at ε=0. Delete or restrict 'VERIFIED: (CS3φ) for Γ at all orders'. Say that for these graphs (CS3φ) is false, F^(N) is IR divergent for N≥2, and the theorem is vacuous. Then either restrict the all-order statement to an IR-finite graph class or change the model.

### [required_fixes 4]
Thm 3.9 (and the summary, Est, O13): relabel Γ^(j)=ln^j(D_g/μ²)/(D_gD₁D₂) as a log-insertion class that mimics the bubble chain of a theory with a dimensionless coupling (gauge-theory-like), grafted onto the (M1) triangle. Delete 'MS-bar-renormalized n-bubble chain' of (M1): in (M1) that chain is ∝g^{2j}[ln(D_g/μ²)+c]^j/D_g^{j+1} and is IR divergent for j≥1. Correct 'the true d-dimensional chain is (−k²)^{−nε} times poles' to (−k²)^{−n(1+ε)} for (M1). The certificates themselves are unaffected.

### [required_fixes 5]
Lemma 2.7: state explicitly the step lim_{η→0}∫d^dk F_η = I_F, where I_F is the parametric value of Setup (i), either as part of (I1) or as a cited standard fact. '(ID)_Γ ⇐ (I1)' depends on it.

### [required_fixes 6]
Prop 5.1′(e): add the closed form C_H=Γ(1+ε)Γ(−ε)Γ(2−ε)/Γ(2−2ε)·Q^{−2−2ε}∫₀¹y(y+(1−y)c_x)^{−1−ε}dy. It equals the whole-integrand value (it is the DR-linearity value T_HΓ, since T_H C_R1 is scaleless with ε-weight −ε) and could upgrade C_H to exact once the fibred side is evaluated. Label the printed numbers as fibred or covariant. In (d), state the measure dz d⁴k on which c₁ depends.

### [required_fixes 7]
Minor:
- List the m² grid of Thm 4.3 explicitly (0.04, 0.01, 0.0025, 0.000625, 1e-4, 1e-6).
- Add the one-line Vandermonde argument that deg P≤4 follows from (F).
- Store the LP rows (denominator supports) in the bubble archive so that dual feasibility can be re-checked from data alone.
- In Lemma 2.10, change 'equivalent to positivity of the Symanzik F polynomial' to 'analogous to'.
- Cite Collins arXiv:1801.03960 beside Chang–Yan and Ligterink–Bakker, and Jackiw–Templeton PRD 23 (1981) 2291.
