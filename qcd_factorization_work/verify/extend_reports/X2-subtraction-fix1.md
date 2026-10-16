# X2-subtraction-fix1

(extracted verbatim from the workflow journal; structured output of the agent)

## summary

RUN STATUS. Answer to the relayed question 「在正常运行吗」: 不完全正常, not normal at this step. The computations run normally. The X2 run finished with 41 scripts and logs. This fix round ran 11 new scripts (scripts/r1_*.py, logs/r1_*), and all of them completed. The deliverables of this stage, however, do not exist on disk. verify/extend/X2-subtraction/REPORT.md was never written: the harness refuses report files written by subagents ('Subagents should return findings as text, not write report files'). Neither review_r1_1.md nor review_r1_2.md exists either, for the same reason; the two reviews reached me only inside the workflow's computed task text. This fix round is again a subagent. I therefore could not write REPORT.md and did not try to work around the block. The COMPLETE REVISED REPORT is this structured output: this summary, 28 results and 14 open items. The last result, [X2-REVISIONS], is the REVISIONS section. Required action, which no subagent can take: the orchestrator or main session must write REPORT.md verbatim from these fields and persist both reviews. The workflow script should pass structured outputs to reviewers and fixers directly. X1 and X3 have the same problem; their REPORT.md files are missing too. Files written in this round: 11 scripts and 15 logs/archives under verify/extend/X2-subtraction/{scripts,logs}. Two round-0 docstrings were also marked (t18 retracted, t15c invalid). No report file was written.

TOPIC. App. D proves its precise subtraction theorem (Thm D.10) only under several hypotheses: (H1)–(H3), which are our (CS1)–(CS3); (A1)–(A4); and D.14/D.27/D.37/D.43. X2 verifies these hypotheses for explicit graphs and infinite classes, in a fibered form (light-cone residues). EVERY statement is a scalar-model statement: (M1) a φ³-type off-shell Sudakov vertex in d=4−2ε; (M2) φ³₆ DIS in the unphysical region; (M3) an abelian massive photon. None of them is a QCD statement.

WHAT THIS REVISION CHANGES. Every valid reviewer item is addressed; the item-by-item list is in [X2-REVISIONS].
(1) WITHDRAWN: the space-like 'genuine pinch'. This affects old Prop 3.14, Err(e), summary item 7 and O8.
- The Landau analysis finds no pinch. k ∝ n_A is incompatible with k²=M²>0. For {G,h1Y,h2Y} the Gram determinant is −16P²P'²(1−e^{−4Y})² ≠ 0.
- On the real base, the fibered density has a simple pole with a definite i0. The integral along a base contour deformed into Im k⁺>0 equals the η→0 value: both are 63.01377+142.80054i.
- Space-like vectors, as used in Collins §10.6.4, remain admissible for virtual graphs. Only the real-base (CS3^φ) fails. 'Extends E1' is deleted.
(2) REPLACED: the two-loop asymptotics.
- In DR, the 9 single-approximator patterns are exactly homogeneous of degree 0. The 40 composite patterns are scaleless. This is a symbolic check.
- Hence Σ_R∫C_R=P(L̃) is a polynomial, and ∫r=Φ^(2)/Q⁴−P.
- If P=LP, then ∫r=−λ²(L̃⁴/2+π²L̃²+12+7π⁴/30)+O(λ⁴L̃⁴).
- The exact values are −7.0507, −4.5967, −2.5705 and −1.2817, and they agree with QMC.
- The fits '−4.7m²L³' and 'averaged norm ~m²L^{2.6–3}' are withdrawn. Every remainder norm is ≥½λ²L̃⁴(1+o(1)).
- The QMC errors were re-assessed with 16 independent randomizations; they are indicative only.
(3) REPAIRED: all one-loop DIS graphs. Old Prop 3.12(ii) was wrong because those graphs are UV divergent.
- The graph list is now complete: 2 ladders, 4 vertex corrections, 2 hard self-energies, 4 J–φ mixing graphs and 1 t-channel graph. Tadpoles vanish.
- Renormalization is integrand-level BPHZ with plus-matched subtraction points, and T_H∘R=R∘T_H.
- Proven: (CS1)_H ≤ Cλ²L for the vertex corrections and ≤ Cλ² for the self-energies.
- Numerically, the renormalized norms are ≈(0.46L+3.1)m² and 0.871m². The unrenormalized remainder grows like ln Λ at O(m²).
(4) DOWNGRADED: DIS ladders of every length (Thm 5.1), from [R] to [P].
- New: a complete proof for n=1 (Prop 5.1', [R, R_PT]), with leading coefficient c₁(x)=4∫ξ^{1/2}(1−ξ)^{3/2}(1−ξ/x)^{−2}dξ. At x=2, c₁=1.262984.
- New: an analytic proof of Lemma 5.3.
- The general-n induction remains a sketch with five identified gaps.
(5) REFORMULATED: Thm 2.6. The claim '(A1) disappears' is replaced by two explicit hypotheses:
- (AR), existence of the residue representation;
- (ID), identification of fibered and covariant values. Lemma 2.7 proves (ID) by Fubini at finite η plus domination; it also excludes zero modes.
- For the triangle, the fibered values of C_S, C_C1, C_C2 and C_H equal the covariant Feynman-parameter values to within 4·10⁻⁷.
- (A1)(b) is kept for Prop D.16. The scope is restricted: Glauber-pinched processes are excluded. The error type is renamed E-N^φ. The grade is [R, R_cond].
(6) STRENGTHENED: the certificates.
- The recession check is corrected; the round-0 cone_rays missed interior directions of half-plane cones.
- An exact primal–dual optimal pair is now asserted before the face-dimension bound is used.
- Frozen variables are treated as coefficients.
- Triangle, natural cover θ=2: all items are λ² at ε=0. The worst item is λ^{8/5}=λ^{2−4ε₀} at ε₀=1/10 (exact). All recession slopes are ≤−1/2 at ε=0 and ≤−9/20 at ε₀=1/10. 58 certificates are archived.
- Bubble class: all 330 remainder cells and all items were re-certified, with exponents ≥2 at ε=0 and ≥1.6 at ε₀.
- The sliver and part-III items are covered by a single-shell structure.
- The hybrid regularization is now stated, and C_j grows at least like j!.
(7) RE-LABELLED: the corrections to App. D.
- Lemma D.23(iii) is confirmed: the literal convention fails in exactly 4 cases (scripted), and soft-first is sufficient.
- Def D.5/Lesson (d) is a sharpening, not an error.
- Def D.9 on the real contour is a remark.
- The Def D.21 'pinch' is withdrawn.
(8) ATTRIBUTIONS and GRADES.
- The angle averaging p=1→2 is Collins §10.7.3.
- Rapidity divergences and non-light-like lines are Collins §10.5–10.6 and Collins–Hautmann, PLB 472 (2000) 129.
- The inductive structure is Collins Theorems 1R–4 (§10.7.5–10.7.6).
- The tropical bounds are Borinsky, AIHPD 10 (2023) 635, Thms 8.A/8.B.
- The region and polytope literature is now cited. All bibliographic data were checked on INSPIRE.
- [R, ca] becomes [R, R_PT] (computer-assisted, scripts archived). Conditional statements are [R, R_cond]. The names (CS1)–(CS3) are used.
(9) SLOTS.
- X2a (prop:appN-triangle-cs): DELIVERED in the fibered form, uniformly in ε∈(0,1/10].
- X2b (thm:appN-oneloop): NOT delivered. Only the equal-virtuality triangle is covered, so the fallback stays.
- X2c (prop:appN-ladder-cs): NOT delivered. There is only a scalar φ³₆ analogue, proven for n=1.
- X2d (rem:appN-abs-edge): OPEN.

MAIN RESULTS AFTER REVISION:
- Fibered subtraction theorem [R, R_cond].
- Identification lemma [R].
- Tropical certificate lemma [R].
- LCPT positivity [R, R_PT]: scalar, spacelike/unphysical, no tadpoles, no q⁺=0 subloops.
- Triangle:
  - densities [R, R_PT];
  - sliver ζ₂/Q̃² at ε=0 [R];
  - (CS1)–(CS3) at the sharp exponent λ²L² [R, R_PT, computer-assisted];
  - remainder norm ≤Cλ²L² rigorous, ≈λ²(4L̃−0.69) numerical [P].
- Bubble class, each fixed j, hybrid model [R, R_PT, computer-assisted].
- All one-loop DIS graphs of (M2) [R, R_PT].
- One-rung ladder [R, R_PT].
- Ladders of all n [P].
- Massive photon, exact light-like remainder [R, R_PT]; the (CS3) failure is known.
- Two-loop algebra [R].
- Two-loop exact integrated remainder [R, R_cond].
- All-order conditional Sudakov theorem [R, R_cond].

NOT VERIFIED:
- gauge numerators;
- crossed and non-planar two-loop graphs;
- two-loop graphs with UV subdivergences;
- the two-loop (CS1)–(CS3) bounds (numerical only);
- admissibility and identification of Collins terms at all orders;
- DIS ladders with n≥2;
- cut (physical) processes;
- slots X2b, X2c and X2d.

## results

### [results 1]
[X2-Setup] MODELS, CONVENTIONS, GRADES.
(M1) Sudakov model, d=4−2ε.
- Fields: complex 'quark' ψ and real 'gluon' φ, with vertex gψ*ψφ and current J=ψ*ψ.
- External momenta: p1=(P,−m²/2P,0_T) and p2=(m²/2P',−P',0_T) in (+,−,T) components, both incoming, with p_i²=−m².
- Q̃²=2PP', Q²=−(p1+p2)²=(Q̃²+m²)²/Q̃², λ²=m²/Q̃², L=L̃=ln(Q̃²/m²).
- One-loop graphs: the triangle (φ exchange) and the J–φ mixing graph (a ψ loop between J and a φ of momentum q=p1+p2). External self-energies are amputated; tadpoles vanish in massless DR.
(M2) DIS model, d=6−2ε, with the same fields.
- Target ψ with p=(p⁺,−m²/2p⁺,0_T). J is inserted twice (forward amplitude).
- Frame q⁺=0, q=(0,q⁻,q_T), Q²=q_T², x=Q²/(2p·q)≥x₀>1 (unphysical region, no cuts), λ²=m²/Q², c_x=1−1/x.
(M3) Abelian massive photon, d=4−2ε.
- On-shell massless legs p1=(P,0,0_T) and p2=(0,−P',0_T); exchanged boson of mass M; λ²=M²/Q², Q²=2PP' (space-like q).
Conventions.
- Measure ∫d^dk/(iπ^{d/2}) per loop; propagators 1/(−l²−i0); units Q̃=1 (M1) and Q=1 (M2, M3); the scripts mostly use P=P'=1/√2.
- Collins terms: C_RΓ=T_R(Γ−Σ_{R'<R}C_R'Γ), X_R0=Γ−Σ_{R<R0}C_RΓ, r=Γ−Σ_RC_RΓ, with the regions and approximators of App. D (Defs D.3, D.18, D.19). The soft-first convention is used at two loops.
- Names: (CS1)–(CS3) are App. D's (H1)–(H3); the fibered versions are (CS1^φ)–(CS3^φ).
Grades follow WRITER_SPEC v2.2 §4.3.
- [R, R_PT]: rigorous for the stated graphs at the stated order, with no unproven input. 'Computer-assisted' means the only non-elementary inequalities are LP optima, certified by exact rational primal–dual pairs; the scripts are archived.
- [R, R_cond]: complete proof from the listed premises.
- [P]: finite subclass or numerical evidence.
Error type E-N^φ: the integral-norm bound ∫_A|ρ_F|dμ_B≤Cλ^aL^K on the fibered base, with the fiber integrated exactly, uniformly in ε∈(0,ε₀]. It is not E-F in the spec's sense.
No QCD claim is made anywhere.

### [results 2]
[X2-Thm2.6] FIBERED SUBTRACTION THEOREM (an implication).
Setting.
- V is the space of finite sums of products Π_j(a_j(b)+Σ_iβ_ji(b)k_i⁻−i0w_j)^{−e_j}, times measurement functions of the base b=(k_i⁺,k_iT).
- Every propagator and eikonal factor is jointly affine in the minus components. The scalar approximators, which zero light-cone coordinates and the IR regulator, preserve V.
- Fibered density: ρ_F(b)=Π_i(iπ^{d/2})^{−1}∫dk_1⁻…dk_ℓ⁻F, evaluated by iterated residues (lcpt.py). Optionally, a compact group of transverse rotations is added to the fiber.
Hypotheses.
- (AR) Admissibility of every F∈{Γ, C_RΓ}: at a.e. b and at every stage, the integrand has degree ≤−2 in the current k_i⁻ and only simple poles (one may close on a side with simple poles only).
- (ID) For Γ and every C_RΓ, ∫_Bρ_F equals the covariant DR value I_F (Lemma 2.7).
- A finite measurable cover {U_R} of B, whose non-maximal members are bounded in every UV direction.
- (CS1^φ)_{R0}: ∫_{U_R0}|ρ_{(1−T_R0)X_R0}|dμ_B≤Cλ^aL^K.
- (CS2^φ)_{R0}: the same bound for C_RΓ, for every R≰R0. Both are uniform in ε∈[0,ε₀] with a>0.
- (CS3^φ): ρ_Γ∈L¹(B) uniformly in ε∈[0,ε₀], and ρ_{C_RΓ}∈L¹(B) for each ε∈(0,ε₀].
Statement. Uniformly in ε∈(0,ε₀]:
- ∫_B|ρ_Γ−Σ_Rρ_{C_RΓ}|dμ_B≤C'λ^aL^K;
- |I_Γ−Σ_RI_{C_RΓ}|≤C'λ^aL^K.
Proof.
- Residue sums are linear, so identity (D.10), r=(1−T_R0)X_R0−Σ_{R≰R0}C_RΓ, holds for the densities a.e. on U_R0.
- The triangle inequality and the finiteness of the cover give the norm bound.
- (CS3^φ) and (ID) make ∫ρ_r=I_Γ−ΣI_{C_R}.
Grade [R, R_cond] (premises (AR), (ID), (CS1^φ)–(CS3^φ)). Error type E-N^φ. It implies the integrated statement; it is not comparable with E-N on a deformed 4D contour.
NEW as a formulation; the proof is that of Thm D.10.
What it replaces.
- (A1)(a) of Ass. D.7 assumes, but App. D does not construct, a 4D contour deformation compatible with all subtraction terms. It is replaced by (AR)+(ID), which can be checked graph by graph.
- (A1)(b) is still needed for Prop D.16 (removing ε).
Scope. Only integrands whose fibered densities are absolutely integrable on the real base, e.g. (M1) and (M2) at x>1. The theorem does NOT cover:
- processes with Glauber pinches (cut graphs with initial- and final-state spectator interactions, O7);
- real-base fibrations with poles (space-like rapidity regulators, Prop 3.14).
Remarks.
(a) Literal (H3) of Def D.9 on the REAL contour fails already for Γ: there is a ln(1/η) divergence across light cones. This is a remark, not an App. D error, because App. D works on a deformed contour Ω (Def D.2, Ass. D.7(A1)).
(b) [Confirmed sharpening] Non-maximal U_R must be UV-bounded. For example, ∫_{U_C1∩{k⁺>P}}|ρ_{C_C2}|=∫_P^∞dx∫_0^{2sx}dκκ^{−ε}/(Pe₂(e₂+κ))≈s^{1−ε}P^{−ε}/ε, which is not uniform in ε for the unbounded U_R of Def D.5.
(c) The fibration is part of the statement: adding transverse azimuths to the fiber turns first-order full norms into second-order ones. This mechanism is Collins 2011 §10.7.3: 'these commonly vanish after an integral over angle. Then the actual error is one power better: p = 2' (text checked in the open-access edition, doi:10.1017/9781009401845). It is quantified here in X2-Num-2loop and X2-Prop5.1'.

### [results 3]
[X2-Lem2.7] IDENTIFICATION OF FIBERED AND COVARIANT VALUES. NEW in this round.
Let F∈V, and denote by F_η the integrand with every i0 replaced by iηw_j.
Hypotheses.
- (I1) For ε in a nonempty open interval E⊂(0,ε₀] and every η>0, ∫d^dk|F_η|<∞.
- (I2) G∈L¹(B,dμ_ε) for ε∈E, where G is the sum of the moduli of the η=0 residue terms selected by the algorithm.
Statement. For ε∈E, ∫_Bρ_Fdμ_ε=lim_{η→0}∫d^dkF_η, the covariant DR value with the stated i0. The identity extends by analytic continuation wherever both sides are analytic.
Proof.
- Fubini holds at finite η.
- After a pole is substituted, the real part of a_g−(β_g/β_f)(a_f−iηw_f)−iηw_g equals its value at η=0. Hence every factor satisfies |·_η|≥|·_0|.
- The pole classification, sign(w/β), does not depend on η. Hence |ρ_{F,η}|≤G.
- ρ_{F,η}→ρ_F a.e., and dominated convergence gives the result.
Consequence: under (I1)–(I2) no zero-mode (k_i⁺=0) contribution can arise. At finite η the set {k_i⁺=0} is null, and (I2) excludes δ-like concentration as η→0.
Grade [R]. NEW (elementary).
If the covariant decomposition contains scaleless pieces, the DR value is defined by analytic continuation and the identification must be checked. Example: C_C1=T₁+T₂ with T₂=−1/((−k²)(m²+2n₁·k)(2n₂·k)), which is scaleless.
Check for the triangle (r1_triangle_covariant.py). The covariant Feynman-parameter values, with n₁·k=Pk⁻ and n₂·k=P'k⁺, are:
- ∫C_S=Γ(ε)²Γ(1−ε)(μ²Q̃²/m⁴)^ε/Q̃², from a convergent parameter integral;
- ∫C_C1=∫C_C2=Γ(1+ε)Γ(−ε)Γ(1−ε)/(εΓ(1−2ε))·(μ²/m²)^ε/Q̃², with T₂=0;
- ∫C_H=Γ(1+ε)Γ(1−ε)²/(ε²Γ(1−2ε))·(μ²/Q̃²)^ε/Q̃², the massless on-shell triangle plus scaleless terms.
They equal the fibered values (sliver included) to:
- relative 7.5·10⁻⁸ to 4.0·10⁻⁷ at P=0.8, P'=1.3, m²=0.1, ε=0.3;
- relative 1.5 to 8.6·10⁻⁵ at P=P'=1/√2, m²=0.01, ε=0.2, limited by UV truncation.
This cross-checks refdoc/work_R6/check_triangle_numerics.py independently.
For the approximated terms of general graphs, (I1)–(I2) are NOT proven (open item O11).

### [results 4]
[X2-Lem2.8] TROPICAL (LP) CERTIFICATE LEMMA.
Setting.
- f=N/Π_kD_k in local coordinates y_i=e^{LX_i}, with m²=e^{−L} and L=ln(1/λ²).
- N is a real polynomial in (y,m²). Its coefficients may depend on 'frozen' variables confined to compact intervals in (0,∞), so they are bounded.
- Each D_k is comparable on the cell to a positive-coefficient polynomial g_k. The constants are explicit: at most 2^{deg} per factor for the frozen ranges [1/2,1] and [1,2], and at most (15/7)^{deg} on the sliver.
- ψ_a(X)=⟨a+w,X⟩−a_m−Σ_kmax_{b∈supp g_k}(⟨b,X⟩−b_m).
- U is a polyhedron (the cell, in normalized log coordinates; the LP is solved on the log-coordinate superset of the cell).
Hypothesis: every ψ_a has a bounded argmax face F_a on U. Equivalently (proved here), ψ_inf(r)<0 for every r∈rec(U)∖{0}. Proof of the equivalence: for concave ψ the difference quotient is non-increasing. If ψ_inf(r)≥0 for some r, then x*+tr lies in F_a for all t; conversely, an unbounded F_a gives ψ_inf=0 along its recession direction.
Statement: ∫_U|f|Πy^{w−1}dy≤CL^dλ^{−2φ*}, with φ*=max_amax_Uψ_a and d=max dim F_a. With polynomial weights (1+|X|)^j, which log insertions require, the L-power rises to L^{d+j}.
Proof.
- Borinsky, arXiv:2008.12310 = AIHPD 10 (2023) 635. Thm 8.A gives |p|≤(Σ|c_ℓ|)p^tr. Thm 8.B gives the lower bound; for positive coefficients it is trivial, with C=min c_ℓ. Both statements were checked in the PDF.
- A Hoffman-type error bound for polyhedral convex functions gives max ψ−ψ≥c·dist(X,F_a).
- A Laplace estimate finishes the proof.
Uniformity in ε.
- ψ_a is affine in ε (weight w_κ=1−ε), so the LP value is convex in ε and the endpoints fix the exponent.
- Uniform constants follow from κ^{−ε}≤1+κ^{−ε₀} for ε∈[0,ε₀]: the certificates at ε=0 and at ε=ε₀ together bound the integral.
Implementation, corrected in this round (r1_lptools.py).
- (i) Exact rational dual y AND primal x with c·x=b·y; strong duality is asserted before the face-dimension bound dim F≤(n+K)−rank(A_S) is used. Round 0 used only weak duality, and complementary slackness was unjustified.
- (ii) The recession check splits the 2D recession cone into its four closed-quadrant pieces, which are pointed, and maximizes the concave piecewise-linear ψ_inf at the endpoints and tie points. Round 0's recession.cone_rays missed interior directions of half-plane cones: cone_rays([([-1,0],0)])=[(0,1),(0,−1)]. Consequences: the true maximum for 'r u>1' is −1/2, not −1, and r_I and r_II had never been checked. An LP cross-check in any dimension is included.
- (iii) Frozen variables are never substituted into numerators; the support is computed with them as coefficients.
Grade [R] for the lemma.
Novelty: the ingredients are known: the tropical approximation (Borinsky); polytope and region methods (Jantzen JHEP 12 (2011) 076; Semenova–Smirnov–Smirnov EPJC 79 (2019) 136; Gardi–Herzog–Jones–Ma–Schlenk JHEP 07 (2023) 197; Ma JHEP 05 (2020) 012; Ma JHEP 09 (2024) 197; Arkani-Hamed–Hillman–Mizera PRD 105 (2022) 125013). Their use to certify Collins' integral norms (CS1)–(CS3) is, as far as INSPIRE searches show, new.

### [results 5]
[X2-Lem2.10/Cor2.11] LIGHT-CONE POSITIVITY (scalar cubic models, massless internal lines).
Hypotheses.
- G is a connected graph of (M1) or (M2) without tadpoles.
- In case (b), every loop of G also carries target plus momentum. This excludes the J–φ mixing bubbles and the t-channel graph, whose q⁺=0 loops are pure zero modes in this frame.
- Kinematics: (a) as in (M1); (b) as in (M2) with x>1.
Statement.
- For a.e. b, ρ_G is a finite sum over x⁺-orderings of terms Π_lines(2l⁺)^{−1}Π_states(E_st−Σl_T²/2l⁺)^{−1}, times a positive constant.
- Every energy denominator is strictly negative.
- All orderings have the same number of states: 2ℓ for the vertex (V=2ℓ+1) and 2ℓ+1 for DIS (V=2ℓ+2).
- Hence ρ_G has a definite sign, and ∫_B|ρ_G|=|I_G|.
Bounds.
- (a) The current vertex is last. E_st∈{p1⁻,p2⁻,p1⁻+p2⁻}, so |E_st−Σ|≥m²/2P.
- (b) Before the photon absorption and after the emission, E_st=p⁻ and |·|≥m²/2p⁺. After the absorption the state carries total plus momentum p⁺ and transverse momentum q_T. Convexity gives Σl_T²/2l⁺≥Q²/2p⁺, hence |E_st−Σ|≥(m²+Q²(1−1/x))/2p⁺. This replaces round 0's weaker form ξ(m²+Q²(1−1/x))/2p⁺. The variant (m²+Q²(1/ξ−1/x))/2p⁺ proposed in review r1_2 does not hold when spectators carry transverse momentum; already the n=1 ladder state has minimum m²+Q²(1−1/x).
Proof: light-cone ordered PT (Chang–Yan PRD 7 (1973) 1147; Ligterink–Bakker PRD 52 (1995) 5954). Zero modes are absent because every loop has ≥2 propagators depending on its k⁻ and carries nonzero plus momentum.
Corollary 2.11: (CS3^φ) holds for Γ, uniformly in ε∈[0,ε₀], for every UV-finite graph that satisfies the hypotheses.
- In (M1), with d=4 and ω=4−E−V, these are all graphs without one-loop two-point subgraphs (ψ and φ self-energies, J–φ mixing) and without tadpoles.
- In (M2), with d=6 and ω=6−2E, these include every DIS ladder.
Grade [R, R_PT], given the standard LCPT input. Verified numerically at one and two loops (t1, t9).
Novelty is modest: negativity of LCPT energy denominators below threshold is classical, and is equivalent to positivity of the Symanzik F polynomial for space-like invariants. Its use for (CS3^φ) is new.

### [results 6]
[X2-Lem2.12] ONE-DIMENSIONAL REDUCTION OF RUNG KERNELS (d=6).
Setup: the parent has (v,K); the child has fraction z and transverse momentum k; v'=zv+|k−zK|²/(1−z); κ=1/(π²(1−z)v'²).
Statement: for every F≥0, ∫d⁴kκF(v')=(1−z)∫_{zv}^∞dt(t−zv)F(t)/t²≤(1−z)∫_{zv}^∞dtF(t)/t. The projected parent (v=0, K=0) gives (1−z)∫_0^∞dtF(t)/t.
Proof: set l=k−zK; then d⁴l=π²|l|²d|l|² and |l|²=(1−z)(t−zv).
In d=6−2ε the reduction reads c_ε(1−z)^{1−ε}∫(t−zv)^{1−ε}F(t)/t²dt.
Grade [R]. Elementary; new only as a tool. Independently re-derived by both reviews.

### [results 7]
[X2-Prop3.1] ONE-LOOP OFF-SHELL TRIANGLE (M1): FIBERED DENSITIES.
Notation: x=k⁺, κ=k_T², u=x/P, e₂=m²+2P'x, h₂=2P'x, A=xm²(1−u)+Pκ, B=xm²+Pκ, a=m²/P', w=2x+a.
Densities:
- ρ_Γ=1/(AD̂₂) with D̂₂=e₂[1+m²/Q̃²+κ/(Q̃²(1−u))]+κ, for 0<x<P;
- ρ_CS=1/(Be₂) for x>0;
- ρ_CC1=xm²/(Q̃²AB) for 0<x<P, and −1/(h₂B) for x>P;
- ρ_CC2=−1/(Pe₂(e₂+κ)) for x>0, and w/(P[(a−w)P'w+aκ](P'w+κ)) on the sliver −a/2<x<0;
- ρ_CH=−x/(P(h₂+κ)(h₂(P−x)+Pκ)) for 0<x<P, and 1/(P(h₂+κ)h₂) for x>P;
- on the sliver, ρ_Γ=2/(wD_gD₁) at k⁻=P'+κ/w.
Normalization: μ^{2ε}∫d^dk/(iπ^{d/2})F=(μ^{2ε}/Γ(1−ε))∫dxdκκ^{−ε}ρ_F.
Checks:
- symbolic residues (t1);
- the engine at 2000 points, maximum deviation 3·10⁻¹⁰ (t7);
- direct k⁻ integration at η=10⁻⁷ (R6);
- ∫ρ_Γ=Φ^(1)(t,t)/Q² (Usyukina–Davydychev);
- new in this round: the four fibered Collins-term values equal the covariant DR values (Lemma 2.7).
(CS3^φ): ρ_Γ≥0, finite uniformly in ε. Each ρ_{C_R} lies in L¹ exactly for 0<ε<1: the UV needs ε>0 and the endpoint x→P needs ε<1.
Grade [R, R_PT]. The closed forms are known (App. D Ex. D.47 / R6); this is an independent verification.

### [results 8]
[X2-Prop3.2] THE NEGATIVE-k⁺ SLIVER OF THE TRIANGLE.
The region is −m²/2P'<k⁺<0: the B-collinear gluon carries negative plus momentum. The statements hold AT ε=0 and in the routing and fibration of Prop 3.1, where the loop momentum is the gluon momentum and the base is (k⁺,k_T).
Statements.
- ∫_sliver ρ_CC2=ζ₂/Q̃² EXACTLY, to all orders in m. Indeed ∫dκρ_CC2=ln(a/(a−w))/(PP'w), and ∫_0^a(dw/2)(…)=Li₂(1)/(2PP').
- ∫_sliver ρ_Γ=ζ₂/Q̃²+O(m²/Q̃⁴). This is half of the π²/3 in (D.32).
- ∫_sliver r=−2m²/Q̃⁴+o(m²): two negative terms contribute −m²/Q̃⁴ each, which is half of the total −4m²/Q̃⁴.
For ε>0 the weight κ^{−ε} changes these values. In another routing or fibration the sliver is not a separate base region: the split among base regions depends on the fibration, while the values ∫C_R do not.
Grade [R] (analytic).
Numerics:
- ∫ρ_Γ(sliver)=1.644934 at λ²=10⁻⁶;
- the sliver remainder is −1.99979λ² at λ²=10⁻⁴ and −2.00000λ² at λ²=10⁻⁶ (t2b; independently reproduced by review r1_2);
- exact LP certificates of the sliver at λ² for ε=0 and at λ^{9/5} for ε₀=1/10, with recession slopes −1/2 (r1_triangle_recert.py).
NEW (elementary).

### [results 9]
[X2-Thm3.3] TRIANGLE (M1): (CS1^φ)–(CS3^φ) AT THE SHARP EXPONENT ON THE NATURAL COVER.
Cover (Q̃=1, P=P'=1/√2, u=k⁺/P, κ=k_T², s=λ²):
- U_S={0<u≤s, κ≤us};
- U_C1={s<u≤1, κ≤us}∪{1<u≤2, κ≤s};
- U_C2={0<u≤s, us<κ≤u}∪sliver;
- U_H is the complement. It contains every UV direction and, at s=λ², the interior of the Sudakov diamond (k~λ).
Statement.
(i) At ε=0, every (CS1)/(CS2) item is ≤Cλ²L^{≤2}. The items are:
- on U_S: (1−T_S)Γ, C_C1, C_C2, C_H (C_H is λ⁴);
- on U_C1: (1−T_C1)X_C1, C_C2, C_H;
- on U_C2: (1−T_C2)X_C2, C_C1, C_H;
- on U_H: r.
(ii) For ε∈(0,1/10], every item is ≤C(λ²L²+λ^{8/5}), uniformly in ε. The exact certificates at ε₀=1/10 give exponents 8/5 or 9/5, and uniformity follows from κ^{−ε}≤1+κ^{−ε₀}.
(iii) (CS3^φ) holds as in Prop 3.1.
Hence, by Thm 2.6 and Lemma 2.7: ∫|ρ_r|≤Cλ²L² at ε=0, and |I_Γ−Σ_RI_{C_R}|≤C(λ²L²+λ^{8/5}) on (0,1/10].
Evidence, all re-run in this round with r1_triangle_recert.py:
- exact primal–dual optimal pairs, with strong duality asserted;
- the corrected recession check on every unbounded cell; the maximum slope is −1/2 at ε=0 and −9/20 at ε₀;
- frozen variables treated as coefficients;
- comparability constants ≤2^{deg} per denominator factor (cell I: v∈[1/2,1]; cell II: u∈[1/2,1]; cell III: u∈[1,2]); on the sliver, γ∈[0.7,1.5] gives ≤(15/7)^{deg};
- the global remainder cells r_I, r_II and r_III and the sliver A/B certified at λ² with slopes −1/2;
- 58 certificates (cells, exact dual vectors, primal points) archived in logs/r1_triangle_certificates.json.
At θ=2 the (CS1)_H item coincides with the global remainder certificate: there the cover adds nothing beyond the direct r-bound.
L-power: rigorously L^{≤2}, from the exact face bound. The float LP gives L⁰–L¹.
Cover family s=λ^θ, θ∈(0,2].
- The certified exponent is θ (exact for θ=1, 3/2, 19/10, 2).
- Lower bound: ∫_{U_S}ρ_CC1≥s·min(s,m²)/(4m²)=s/4.
- Numerically, A/s→1 for θ<2 and →1/2 at θ=2.
- The (CS1)_C1 norm is ≈(θ/2)sL for θ<2. At θ=2 it is 1.36, 1.41, 1.43, 1.44 sL for λ²=10⁻⁴…10⁻¹⁰, still slowly increasing (r1_theta2_lower.py).
Relation to App. D. The neighbourhoods λ^β, 0<β<1, β_S<β_C of Def D.5/Lemma D.25 are sufficient-condition choices for the general envelope argument (lem:method-local-accuracy needs t_R≫s_R in (GA3)(iii)). For the triangle they are unnecessary and cost powers; natural-scale covers give the sharp exponent when the grouped objects are computed explicitly. This is a SHARPENING, not an error correction.
Grade [R, R_PT], computer-assisted.
NEW: integral-norm verification of (CS1)–(CS3) for this graph. Delivers slot X2a in the fibered form.

### [results 10]
[X2-Thm3.5/Prop3.6] TRIANGLE REMAINDER: NORM VERSUS INTEGRAL.
Rigorous: ∫|ρ_r|≤Cλ²L² at ε=0 [R, R_PT, computer-assisted, Thm 3.3].
Numerical [P]:
- ∫|ρ_r|=c(λ)λ²L, with c=3.53, 3.79, 3.89, 3.93, 3.95, 3.96, 3.962 for λ²=10⁻²…10⁻⁸ (t2b; reproduced by review r1_2 with an independent integrator);
- 91.41525λ² at λ²=10⁻¹⁰ (review r1_1);
- hence ∫|ρ_r|≈λ²(4L̃−c'), with c'→0.69. This is one log more than the integrated remainder.
Sign structure:
- soft box −1.04L, C1 strip −0.54L, k⁺>P strip +0.95L, hard part +0.48L (t2c);
- the monomial majorant is sharp to a factor 1.1–1.3 (t3).
Exact integrated remainder (known; REFDOC N12, reproduced). In units Q̃=1, ρt=m² holds exactly, so:
- ∫r=Φ^(1)(t,t)/Q²−(L̃²+π²/3)=4Li₂(−m²)/(1−m⁴)+(L̃²+π²/3)m⁴/(1−m⁴)=−4λ²+O(λ⁴L̃²);
- equivalently, in Q units: −4m²/Q⁴+(m⁴/Q⁶)(L_Q²−15+π²/3)+O(m⁶L²/Q⁸).
The fibered integral matches UD to 10⁻¹¹ (t2b).
Table 5 of the reference tests the leading power of the exact integral in Q, not the Collins remainder in Q̃ (ERR-m25).

### [results 11]
[X2-Thm3.9] INFINITE CLASS I: RENORMALIZED BUBBLE CHAINS (log insertions) IN THE HYBRID MODEL.
Model (hybrid scheme).
- (M1), with the φ propagator replaced by the MS-bar-renormalized n-bubble chain AT ε=0: Γ^(j)=ln^j(D_g/μ²)/(D_gD₁D₂), j≤n, μ=Q̃.
- The insertion sits inside the d-dimensional outer integral: a d=4−2ε outer measure with a fixed 4D insertion. The true d-dimensional renormalized chain is (−k²)^{−nε} times poles, not ln^j.
Lemma 3.7 [R in the hybrid model].
- The insertion is a fixed function of k². The approximators act only on lines 1 and 2 and on the external momenta. So C_RΓ^(j)=ln^j(D_g)·C_RΓ pointwise in 4D, and the region set is that of the triangle.
- That this reproduces the leading regions of the full (j+1)-loop graph is a MODEL ASSUMPTION, not proven here. Heuristic: the massless bubble Π(k²) is non-analytic only at k²=0, so the bubble lines follow the mode of k or are hard. The hard part is removed by integrand-level renormalization of the bubble subgraphs (Ass. D.41 (U1)/(U2)), which commutes with T_R because the counterterms are polynomial in k and k is not approximated.
Four-shell representation, for 0<u<1, with v=1−u and P=P'=1/√2.
- ρ_r^(j)=Σ_sl_s^jT_s over the shells s=D,e,t,h.
- R_D=(um²v+κ)/v, R_e=um²+κ, R_t=κ/v, R_h=κ.
- T_D=(v/D_G−1/u)/(um²v+κ), T_e=m²/(u(m²+u)(um²+κ)), T_t=1/(u(uv+κ)), T_h=1/((m²+u)(m²+u+κ))−1/(u(u+κ)).
- The k⁻ contour closes away from the ln D_g cut in every range: upward on the line-1 shells for 0<u<1; only the e and h shells contribute for u>1; downward on the D₂ pole on the sliver, where the cut lies in the upper half plane.
Lemma 3.8 (rectangle rule, exact).
- l_D−l_e−l_t+l_h=δ=ln(A/B), with |δ|≤min(u²m²/(um²v+κ), CL(1+|X|)).
- a=l_e−l_h∈[0,min(um²/κ,CL)] and b=ln(1/v)∈[0,min(u/v,CL)].
- ρ^(j)=l_h^jρ_r^(0)+Σ_{n≥1}C(j,n)l_h^{j−n}[a^n(T_D+T_e)+b^n(T_D+T_t)+((a+b+δ)^n−a^n−b^n)T_D].
Single-shell structure (new in this round).
- On the sliver, Γ^(j) and C_C2^(j) are both residues at the D₂ pole. So ρ_r^(j)=l_sl^jρ_r^(0) exactly, with l_sl=ln D_g evaluated at the D₂ pole. C_S, C_C1 and C_H vanish there.
- For 1<u≤2 every Collins term lies on a single shell: C_S and C_C1 on e, C_C2 and C_H on h, and Γ=0. So the part-III items of U_C1 are l_e^j or l_h^j times the j=0 items.
Theorem. On the natural cover of Thm 3.3, for each fixed j, every (CS1)/(CS2) item and ∫|ρ_r^(j)| satisfy:
- ≤C_jλ²L^{j+2} at ε=0;
- ≤C_j(λ²+λ^{8/5})L^{j+2} uniformly for ε∈(0,1/10].
(CS3^φ) holds for 0<ε<1 in the hybrid sense: the logs do not affect convergence, but individual C_R need ε>0.
Evidence (r1_bubble_recert.py: exact primal–dual pairs, corrected recession check).
- Remainder, 0<u<1, 270 cells: minimum exponent 2 at ε=0 and 1.6 at ε₀=1/10. At ε₀, piece P3 needs the trivial alternative |δ|≤CL(1+|X|) in 9 deep cells (v≲λ², κ≲λ⁴…λ⁸). Worst recession slopes −1/2 and −9/20. The corner {v≤λ⁶, κ≤λ⁸} is bounded shell by shell (each |T_s|≤λ⁸ there).
- Remainder, u>1, 60 cells: minimum exponent 2 at ε=0 and 1.8 at ε₀; slopes −1/2 and −11/20.
- Items on U_S, U_C1 (s<u≤1) and U_C2 (u>0): minimum exponent 2 at ε=0 and 1.6 at ε₀; slopes −1/2 and −9/20.
- Sliver and part III: the triangle certificates times the log weights |l|^j≤(CL(1+|X|))^j, using Lemma 2.8 with polynomial weights.
Growth in j. C_j grows at least factorially.
- The u>1 part alone has remainder norm ≈2m²j! at fixed m². This comes from the UV tail ∫_1^∞(lnκ)^jκ^{−2}dκ=j! (review r1_1: norm/(m²j!)→2.0 for j=8, 10, 12 at m²=10⁻²).
- So C_j≳2j!/L₀^{j+2}, and nothing can be said about the summed chain (renormalon).
Numerics [P] (t5): ∫r^(j)≈−4λ²(−L)^j. At λ²=10⁻¹⁰ the norms are 3.97λ²L (j=0), 4.84λ²L² (j=1) and 6.58λ²L³ (j=2).
The round-0 script t15c ('resolved by exact vertex enumeration') is invalid, because those LPs are unbounded. Its docstring is now marked, and it is not part of any proof.
Grade [R, R_PT] for each fixed j in the hybrid model, computer-assisted. NEW.

### [results 12]
[X2-Prop3.12] ALL ONE-LOOP GRAPHS OF THE DIS FORWARD AMPLITUDE IN (M2).
Round 0's part (ii) was wrong: it claimed '(H3) trivial' for UV-divergent graphs. This item is repaired.
Complete list, for current vertex Jψ*ψ and coupling gψ*ψφ:
- (i) 2 ladders: rung φ(p−k), spine ψ(k) twice, hard line ψ(k±q).
- (ii) 4 vertex corrections: φ exchanged between the target line and the hard line, at J_in or J_out, in the s or u channel.
- (iii) 2 hard-line self-energies.
- (iv) 4 J–φ mixing graphs: a ψ loop between one current and a φ of momentum q, which is absorbed by the target line.
- (v) 1 t-channel graph: a ψ loop carrying both currents, coupled to the target by a φ of zero momentum. It is ∝1/t at t=0 and independent of x, so it is excluded from the forward amplitude. In QCD the analogues of (iv) and (v) vanish by colour (Tr t^a=0).
- Tadpoles vanish in massless DR, and external self-energies are amputated. Graphs (iv) and (v) were missing in round 0.
Statements.
(i) The collinear region is leading. Covered by Prop 5.1' (the u channel is analogous, with A'=1+ξ/x≥1) [R, R_PT].
(ii),(iii) These graphs are UV divergent: ω=0 for the vertex and ω=2 for the self-energy. The unrenormalized (1−T_H)Γ=S(P)[f(m²)−f(0)]+[S(P)−S(P̂)]f(0) diverges at O(m²): ∫_{|l|<Λ}|ρ|=25.4, 43.8, 62.2 m² for Λ=10², 10⁴, 10⁶ at m²=10⁻³.
Renormalization: integrand-level BPHZ (Ass. D.41), with subtraction points that match the plus components.
- Vertex: subtract the same graph at a fixed space-like point (p₀,q₀) with p₀⁺=p⁺, q₀⁺=0 and fixed invariants p₀²=−μ², q₀²=−Q₀² and (p₀+q₀)². The integrated counterterm is a constant times the tree vertex. Because the fibered supports agree, the subtraction improves the UV pointwise, to ρ~|l|^{−6}.
- Self-energy: after the shift l→l−zP_T the density is (1/π²)/(|l|²+z(1−z)s), with s=−P². Subtract its first-order Taylor polynomial in s at s₀. This is a Taylor expansion in P⁻ at fixed P⁺ and P_T, with integrated counterterm Σ(s₀)+(s−s₀)Σ'(s₀). The result is g(s)=(c−c₀)²/(π²(a+c)(a+c₀)²), with c=z(1−z)s.
- Commutation: T_H acts only on p (p→p̂, p̂⁺=p⁺, P_T unchanged), and the subtraction point does not depend on p. Hence T_H∘R=R∘T_H.
Theorem. Write f(m²)=1/(π²(1−z)vH), with v=zm²+|l|²/(1−z), H=A+v+2l·q and A=1−z/x.
- The renormalized vertex graph satisfies (1−T_H)RΓ=S(P)[f(m²)−f(0)]+[S(P)−S(P̂)][f(0)−f₀], and ∫|ρ|≤C(x)λ²L.
- The self-energy graph satisfies ∫|g(s)/s²−g(ŝ)/ŝ²|≤C(x)λ², with ŝ=s−m²=Q²(1−1/x).
- (CS3^φ) holds uniformly in ε, and R={H} suffices.
Proof (vertex).
- From v₀H₀−vH=−zm²(v₀+H): |f(m²)−f(0)|≤zm²/(|l|²HH₀)+zm²/(v|l|²H₀).
- The first term integrates to O(zm²). The second integrates to O(zm²(1−z)[L+ln(1/(z(1−z)))]), using v≥max(zm²,|l|²/(1−z)).
- H and H₀ are ≥zc_x, and the endpoint z→0 is integrable.
- |S(P)−S(P̂)|≤m²/(sŝ), and f(0)−f₀∈L¹ (UV |l|^{−6}, IR |l|^{−2}).
Proof (self-energy): |∂_sg| integrates to ≤Cz(1−z)(|s−s₀|/s₀+(s−s₀)²/(ss₀)), and g(ŝ)∈L¹.
(iv) These graphs depend on the target only through S(p+q). Their q-bubble has q⁺=0 and is a pure zero mode in this frame, so it is treated as a renormalized insertion Π_R(q²). The remainder is exactly [S(P)−S(P̂)]D(q)Π_R(q²)=O(λ²) [R].
Numerics (r1_dis_Honly.py; x=2, μ²=1, x₀=2):
- the renormalized vertex norm is 5.18, 6.32, 7.38, 8.43, 9.48, 10.53 m² for m²=10⁻²…10⁻⁷, i.e. ≈(0.46L+3.1)m², with definite sign and independent of the cutoff;
- the self-energy norm is 0.835 m² at m²=10⁻² and 0.871 m² for m²≤10⁻⁴.
Grade [R, R_PT]. NEW.

### [results 13]
[X2-Thm3.13] ABELIAN MASSIVE PHOTON (M3) WITH LIGHT-LIKE APPROXIMATORS.
Per-line semilattice: T_S maps (t1,t2)→(h1,h2); T_C1 maps t2→h2; T_C2 maps t1→h1; T_H maps G=M²−k² to g0=−k².
Exact forms:
- C_S=1/(Gh1h2);
- C_C1=(1/(Gh2))(1/t1−1/h1);
- C_C2=(1/(Gh1))(1/t2−1/h2);
- C_H=(1/g0)(1/t1−1/h1)(1/t2−1/h2);
- r=(1/G−1/g0)δ1δ2=−M²g0/(Gt1h1t2h2).
Fibered form, P=P'=1/√2:
- ρ_r=(M²/u)[(1−u)/((M²(1−u)+κ)(u(1−u)+κ))−1/((M²+κ)(u+κ))] for 0<u<1;
- ρ_r=−M²/(u(M²+κ)(u+κ)) for u>1.
The κ-integral of the 0<u<1 bracket vanishes identically: both terms equal ln(u/M²)/(u−M²).
Consequences:
- ∫r=−M²∫_1^∞du·ln(u/M²)/(u(u−M²))=−λ²(L+1)−λ⁴(L/2+1/4)+O(λ⁶L), exactly. This is consistent with Jantzen's closed form.
- Numerics: −5.6246…−14.8084λ², against −(L+1)=−5.605…−14.816. The Jantzen offset 1.7·10⁻⁴, constant in M², is a κ-cutoff tail.
- The norm is ≈λ²(3.0L−0.85) [P].
(CS3) fails for C_S, C_C1 and C_C2 at every ε. These are rapidity divergences: ρ_CS has constant density per unit ln k⁺, and ρ_CC1=−1/(2PP'(M²+κ)k⁺) for k⁺>P. So Thm D.10 does not apply, although r is integrable and O(λ²L).
KNOWN (attributed). The rapidity divergences of light-like Wilson lines with a massive gluon, and their cure by non-light-like lines, are in:
- Collins 2011 §10.5 (the one-loop Sudakov form factor with gluon mass; §10.5.6: 'the integral has a rapidity divergence') and §10.6.4;
- Collins–Hautmann, PLB 472 (2000) 129 [hep-ph/9908467];
- the same graph with analytic regulators: Jantzen, JHEP 12 (2011) 076, §6;
- rapidity regulators: Chiu–Jain–Neill–Rothstein, PRL 108 (2012) 151601; Becher–Neubert, EPJC 71 (2011) 1665.
NEW only:
- the exact light-like remainder formula;
- the remark that the remainder bound holds without (CS3), while factorization into separately defined factors needs (CS3).
Grade: exact formula [R, R_PT]; norm [P].

### [results 14]
[X2-Prop3.14] RAPIDITY-REGULATED SOFT APPROXIMATORS IN (M3): TIME-LIKE VERSUS SPACE-LIKE.
Rewritten. The round-0 claim of a 'genuine pinch' for space-like vectors is WITHDRAWN.
Time-like vectors: h1Y=2P(k⁻+e^{−2Y}k⁺) and h2Y=2P'(k⁺+e^{−2Y}k⁻).
- The eikonal and photon poles never collide on the real base.
- The rapidity integral converges: 545.458 at Y=3 and 1090.909 at Y=6, linear in Y. (CS3^φ) holds for ε>0.
- For Y≥L/2 (e^{−2Y}≤λ²) the remainder equals the light-like value within O(λ²), with norm ≈2.9λ²L. At Y=L/4 the regulator error ~e^{−2Y}=λ dominates (t16b) [P].
Space-like vectors, as in Def D.21 and in Collins §10.6.4: h1Y=2P(k⁻−e^{−2Y}k⁺)−i0 and h2Y=2P'(k⁺−e^{−2Y}k⁻)−i0. The i0's are inherited from the light-like limits of the propagators in this kinematics.
(a) No pinch [R].
- For {G,h1Y}, the Landau condition −2α_Gk+α₁n_A=0 forces k∝n_A. Then k²∝n_A²=−8P²e^{−2Y}<0, which is incompatible with G=0 (k²=M²>0).
- For {G,h1Y,h2Y}, (α₁,α₂) must lie in the kernel of the Gram matrix of (n_A,n_B). Its determinant is −16P²P'²(1−e^{−4Y})²≠0, so k=0 and G=M²≠0.
- There is no Landau singularity at finite k (symbolic check, r1_spacelike.py).
(b) On the real base the fibered density has a simple pole with a definite i0.
- For x=k⁺>0, ρ_CS=1/(P(M²+κ−2e^{−2Y}x²−i0)·2P'x(1−e^{−4Y})); the engine and the closed form agree.
- The pole sits at x₀=√((M²+κ)e^{2Y}/2), displaced to x₀−i0. It is integrable as a distribution and is removed by deforming x into Im x>0. The k⁻ residue formula continues analytically, and the only colliding pair is h1Y–G.
- Numerically, at M²=10⁻³, Y=3, κ=0.01: ∫|ρ| over [x₀/2,2x₀] diverges like 2|Res|ln(1/d), giving 392, 811, 1230, 1648 for cut-outs d=10⁻²…10⁻⁸.
- At finite η the integral takes the values 61.720+142.673i (η=10⁻⁴), 63.0008+142.7994i (10⁻⁶) and 63.01364+142.80053i (10⁻⁸). These converge to PV−iπRes=63.01377+142.80054i, which equals the integral along a semicircle in Im x>0, 63.01377+142.80054i.
(c) What fails is only absolute integrability on the REAL fibered base, i.e. (CS3^φ) in this fibration. This is a limitation of the real-base method, not of space-like Wilson lines.
- Remedies: a complex deformation of the base k⁺; a different fibration (for instance integrating κ first, after which only a weak branch point remains); or time-like vectors.
- Space-like vectors remain admissible for virtual graphs: Collins applies the approximants on contours deformed out of the Glauber region (§10.6.4).
- The round-0 claim 'extends E1/ERR-M27' is deleted. E1 concerns real emission, where the k·n=0 singularities for space-like n lie in the physical region (Collins §10.6.4, last paragraph).
Grade: (a) and (b) [R] (analytic, with a numerical check); the time-like window [P]. NEW (elementary).

### [results 15]
[X2-Thm4.1/Prop4.2] TWO-LOOP PLANAR SUDAKOV VERTEX (M1): EXACT ALGEBRA.
Setup.
- Lines: g1=k1, g2=k2, a1=p1−k2, a2=p1−k1−k2, b1=p2+k2, b2=p2+k1+k2.
- 9 regions: HH, HC1, HC2, C1C1, C2C2, HS, C1S, C2S, SS.
- Approximators are coordinate-zeroing sets on (k1±,k1T,k2±,k2T,M), where M is the IR regulator.
- Soft-first convention: a jet line that carries soft momentum enters H with its soft-approximated momentum, so soft momenta drop out of H. This is the requirement in Collins §10.6.6 that the hard factor not depend on soft momenta.
Verified exactly (t8):
- the 12-edge Hasse diagram;
- meet closure;
- (Com);
- (Abs) for all 9 incomparable pairs;
- chain recursion = product formula (50 zeroing patterns).
Prop 4.2. The literal convention of App. D is: Def D.18, H sees π± of the exact jet momentum; Def D.19, soft momenta are approximated only inside jet factors.
- Its zeroing sets differ from soft-first in four entries: HS a2 {k2−,k2T,M}; HS b2 {k2+,k2T,M}; C1S b2 {k1−,k1T,k2+,k2T,M}; C2S a2 {k1+,k1T,k2−,k2T,M}.
- With it, (Abs) fails in exactly 4 cases. On a2, the meet zeroes k2⁺ but neither region does: (C1C1,HS) with meet C1S, and (C1C1,C2S) with meet SS. On b2, the same happens for k2⁻: (C2C2,HS) with meet C2S, and (C2C2,C1S) with meet SS.
- Scripted in r1_abs_naive.py; confirmed independently by both reviews.
Wording: soft-first is SUFFICIENT for (Abs) here, and the literal convention fails. Necessity is not claimed.
This corrects Lemma D.23(iii) ('always true for per-line meets'). It is a different edge case of the same lemma than R6 E5.
NOT settled: slot X2d (rem:appN-abs-edge: a soft line with both ends at hard vertices, gluon polarizations) is a different configuration and remains open.
Grade [R] (exact). NEW as an explicit check.

### [results 16]
[X2-Thm4.3] TWO-LOOP PLANAR VERTEX (M1, P=P'=1/√2, Q̃=1): EXACT INTEGRATED REMAINDER. NEW in this round.
(i) [R, exact symbolic check, r1_twoloop_exact.py] Homogeneity and scalelessness.
- Among the 49 non-trivial zeroing patterns of r=Π_R(1−T_R)Γ (soft-first), the 9 single-approximator terms T_RΓ are exactly homogeneous. The scaling acts on the loop-momentum components with weight(m²)=1, and the total degree is 0 at ε=0.
- Hence ∫T_RΓ=c_R(ε)(m²)^{−k_Rε}, with k_R=0 (HH), 1 (HC1, HC2), 2 (C1C1, C2C2, HS), 3 (C1S, C2S) and 4 (SS).
- The other 40 patterns (composites) are homogeneous along a one-parameter family. That family includes an m²-independent rescaling with nonzero ε-weight, so these patterns are scaleless and vanish in DR (standard convention).
- Hence, in DR, Σ_R∫C_RΓ=Σ_R∫T_RΓ: Collins' integrated subtraction terms coincide with the expansion-by-regions contributions, and the overlap terms are scaleless (cf. Jantzen 2011 on overlap and zero-bin contributions).
(ii) [R, R_cond; premise: ∫Γ and ∫r are finite at ε=0, so the ε-poles cancel]
- Σ_R∫C_RΓ=P(L̃), a polynomial of degree ≤4 in L̃=ln(Q̃²/m²).
- ∫r=Φ^(2)(t,t)/Q⁴−P(L̃).
- ∫Γ=Φ^(2)/Q⁴=(1+m²)[12Li₄(−m²)+L̃⁴/4+π²L̃²/2+7π⁴/60]/((1−m²)(1+m²)⁴). This is the UD formula; for Q̃=1, ρt=m² exactly.
(iii) [R, R_cond; premise: ∫r→0 as m→0, i.e. the subtraction theorem at this order (numerically supported), or equivalently the leading-power expansion by regions of Φ^(2) with this region set]
- P=LP=L̃⁴/4+π²L̃²/2+7π⁴/60. Hence, exactly, ∫r=−λ²(L̃⁴/2+π²L̃²+12+7π⁴/30)+O(λ⁴L̃⁴).
- Values: −7.050661, −4.596744, −2.570489, −1.281728, −0.446917, −0.0201338 at m²=0.04, 0.01, 0.0025, 6.25·10⁻⁴, 10⁻⁴, 10⁻⁶.
- Ratio to the NLP formula: 0.924, 0.980, 0.995, 0.9988, 0.9998, 0.999998.
- ∫r/(m²L̃³) runs −5.29, −4.71, −4.78, −5.11, −5.72, −7.64, −9.75 down to m²=10⁻⁸. The round-0 fit '−4.7m²L³' was pre-asymptotic.
Consequence.
- Every norm of the remainder, in particular the azimuth-averaged one, is ≥|∫r|≥½λ²L̃⁴(1+o(1)).
- If P≠LP, the remainder would not even vanish.
- Either way, the round-0 claim 'averaged norm ~m²L^{2.6–3}' is asymptotically false.
Evidence for (iii): the QMC values of ∫r agree with the exact values within 0.05–2.4σ.
- n18 run: −7.036±0.22, −4.593±0.08, −2.386±0.24, −1.319±0.084.
- This round, 16 randomizations: −6.963±0.18, −5.125±0.22, −2.583±0.082, −1.300±0.11.
NEW: the identity and the NLP coefficient.

### [results 17]
[X2-Num-2loop] TWO-LOOP PLANAR VERTEX: DOUBLE-RESIDUE (LCPT) DENSITIES AND REMAINDER NORMS. Grade [P] (numerical).
Engine: lcpt.py with 6 factors and 2 minus components; order and weight independence to 5·10⁻¹⁰ (t9).
Validation of ∫ρ_Γ against Φ^(2)(t,t)/Q⁴ (exact: 82.282, 223.863, 508.102, 1019.383 at m²=0.04…6.25·10⁻⁴):
- n18 run: 82.41±2.0, 222.4±1.1, 513.8±6.5, 1016.8±4.6.
- This round (r1_twoloop_qmc.py; 16 independently scrambled Sobol sequences, 2^17 points per sub-box, seeds disjoint from t12): 81.66±0.55, 239.1±12, 505.9±1.8, 1020.2±5.2, with pulls −1.1, +1.3, −1.2, +0.2.
- The n16 run of t12 under-covers: pulls −2.5 and −1.9 for ∫Γ, and −4.6 for ∫r at 6.25·10⁻⁴.
Error analysis.
- The integrands have integrable singularities, so the QMC sample distribution is heavy-tailed.
- Standard errors over randomizations are indicative only: one of the eight pulls in the 16-randomization run is 2.4σ.
- Exact values are taken from the closed forms (Thm 4.3).
Remainder norms.
- Full light-cone norm: 20.12±0.13, 14.58±0.19, 9.44±0.11, 5.96±0.11, i.e. ≈31.3, 31.7, 31.5, 32.3 λL. This is first order, from angle-odd projection errors such as 2k1T·k2T when a collinear momentum enters a hard loop. Indicative only; the mechanism is Collins §10.7.3.
- Norm with the relative azimuth averaged in the fiber: 11.3, 7.0, 3.46, 1.88 (t14). Consistent with the exact lower bound |∫r|=7.05, 4.60, 2.57, 1.28. Asymptotically ≥½λ²L̃⁴(1+o(1)) (Thm 4.3).
The fitted rates '31λL', 'm²L^{2.6–3}' and '−4.7m²L³' are withdrawn as determinations; the last two are asymptotically wrong.

### [results 18]
[X2-Lem5.2] DIS LADDERS IN (M2): POSITIVE LIGHT-CONE REPRESENTATION AND EXACT COLLINS STRUCTURE.
Setup: the n-rung forward ladder L_n=∫Π_jd⁶k_j/(iπ³)·H₀(k_n)Π_jS(k_j)²R(k_{j−1}−k_j), with k₀=p, in the frame q⁺=0 with x>1.
Statements.
(a) Support: the iterated k⁻ integrals vanish unless 0<k_n⁺<…<k_1⁺<p⁺.
(b) Rungs on shell. On the support, close each k_j⁻ contour (top-down, j=n,…,1) on the side of the single rung pole. This gives ρ_c=Π_i[π^{−2}(1−z_i)^{−1}(v_i^(c))^{−2}]H^(c_{n+1}), where:
- c∈{0,1}^{n+1}; c_i=1 means the parent of level i is projected, and c_{n+1}=1 means the hard factor is projected;
- v_i=z_i(1−c_i)v_{i−1}+|k_iT−(1−c_i)z_ik_{i−1,T}|²/(1−z_i), with v₀=m²;
- H^(0)=1/(A+v_n+2k_nT·q_T), H^(1)=1/A, A=1−ξ_n/x.
(c) Invariants: v≥ξm²+|K|²/(1−ξ) for unprojected chains, and v≥|K|²/(1−ξ) for all chains (Cauchy–Schwarz with weights z(1−ξ) and 1−z). Hence H^(0)>0.
(d) The approximators T_{R_j} (project s_j in factor j+1; T_{R_0}=T_H: p→p̂) commute, because π(s) depends only on ξ. Hence r=Σ_c(−1)^{|c|}ρ_c=U_0(s₀), where U_n(s)=h(s)−h(πs) and U_{j−1}(s)=κ(s→s')U_j(s')−κ(πs→s'₀)U_j(s'₀).
Pole-side argument, written out in this round.
- At level j the rung factor R(k_{j−1}−k_j) has its simple pole in the upper half plane iff k_{j−1}⁺>k_j⁺.
- The spine double pole S(k_j)² and the hard factor have coefficient −2k_j⁺<0 and i0-weight 1, so their poles lie in the lower half plane for k_j⁺>0.
- After the rung pole is substituted, the propagated spine and hard factors keep coefficient −2k_j⁺ in k_{j−1}⁻ and acquire i0-weight k_{j−1}⁺/(k_{j−1}⁺−k_j⁺)>0. So they stay in the lower half plane, and on the ordered support the rung pole is the only upper pole at every level.
- All other sign patterns vanish by light-cone ordered PT (Chang–Yan 1973): the integral is nonzero only if the plus momenta admit an x⁺-ordering with positive plus momentum on every line. For example, k_n⁺<0<k_{n−1}⁺−k_n⁺ would force the cycle left rung vertex < right rung vertex < right photon vertex < left photon vertex < left rung vertex.
Validation:
- n=1: the fibered value equals the covariant Feynman-parameter value to 10⁻¹³ (t6);
- n=2: the structure was checked numerically (t11).
Grade [R, R_PT], given the standard LCPT input. The structure is known (App. D Ex. D.48 for n=2) and is made precise here; NEW as stated.

### [results 19]
[X2-Lem5.3] HARD-FACTOR LEMMA. The analytic proof replaces the sampling check of round 0.
Setup:
- a parent state (ξ,K,v) with 0<ξ≤1 and v≥|K|²/(1−ξ);
- a child (z,l)∈(0,1)×R⁴, with k=l+zK and v'=zv+|l|²/(1−z);
- d=A(zξ)+v'+2k·q, with A(y)=1−y/x, |q|=1 and c_x=1−1/x;
- d̄=A(zξ)+zv+|l|²/(1−z)+2zK·q.
Statement.
- (i) d≥zξc_x>0 in every direction of l.
- (ii) ⟨1/d⟩_{l̂∈S³}=2/(d̄+√(d̄²−4|l|²))≤2/d̄≤2/(1−z+zξc_x+|l|²/(1−z)).
- (iii) ⟨1/d²⟩_{S³}≤(2/d̄²)(1+(d̄/(zξc_x))^{1/2}).
- (iv) ∫_0^1(1−z)⟨1/d⟩dz≤2, uniformly in ξ.
Proof.
- (i) By Cauchy–Schwarz with weights z(1−ξ) and 1−z, the child invariant v'≥|k|²/(1−zξ) holds. Then min_r(r²/(1−zξ)−2r)=−(1−zξ) gives the bound.
- (ii) Use ∫_0^πsin²θdθ/(a+bcosθ)=π(a−√(a²−b²))/b², with a=d̄>|b|=2|l| by (i). The bound on d̄ follows from v−2|K|≥−(1−ξ).
- (iii) Differentiate (ii) with respect to a, and use a²−b²≥a·d_min.
- (iv) Use (1−z)/(1−z+zξc_x)≤1.
The closed-form S³ average was checked by quadrature to 12 digits (r1_ladder1_analytic.py). t19 remains as a cross-check: its ratio to the bound is ≤0.5.
Grade [R]. NEW (elementary).

### [results 20]
[X2-Prop5.1'] ONE-RUNG DIS LADDER: COMPLETE PROOF. NEW in this round. Hypotheses: (M2), x≥x₀>1, Q=1, λ=m≤c_x/8.
Notation:
- ρ_r(z,k)=κ₁(h₁−ĥ)−κ₀(h₀−ĥ);
- κ₁=1/(π²(1−z)v'²) with v'=zm²+|k|²/(1−z);
- κ₀ is the same with v'₀=|k|²/(1−z);
- h₁=1/(A+v'+2k·q), h₀=1/(A+v'₀+2k·q), ĥ=1/A, A=1−z/x.
Claims.
(a) ∫dzd⁴k|ρ_r|≤C(x)λ.
(b) On the cover U_{R1}={v'≤λ²}, U_H=complement, all items are ≤C(x)λ.
(c) (CS3^φ): ρ_Γ=κ₁h₁≥0 is integrable uniformly in ε (UV ~|k|^{−6}). ρ_{C_R1}=κ₁ĥ and ρ_{C_H}=κ₀(h₀−ĥ) are integrable for ε>0 only (logarithmic UV divergence).
(d) ∫|ρ_r|=c₁(x)λ+o(λ), with c₁(x)=4∫_0^1dξξ^{1/2}(1−ξ)^{3/2}/(1−ξ/x)². This comes from the angle-odd term −2k·q[κ₁−κ₀]/A², using ⟨|cosθ|⟩_{S³}=4/(3π) and ∫_0^∞(2y+1)y^{−1/2}(1+y)^{−2}dy=3π/2.
- Values: c₁(2)=1.262984, c₁(1.3)=1.936673, c₁(5)=0.924158.
- Numerics (t6b): 1.26329 at m²=10⁻⁷, agreeing to within 3·10⁻⁴, the size of the angular-quadrature error. This leading coefficient was first derived in review r1_1 and is re-derived here.
For ε∈(0,ε₀] the bounds hold with λ^{1−2ε₀}, uniformly (κ^{−ε}≤1+κ^{−ε₀}).
Proof of (a). Let δ=zm²=v'−v'₀.
- Positivity: for |k|≤c_x/4, A+v−2|k|≥c_x/2 for every v≥0. For all k, A+v'₀+2k·q≥zc_x.
Region B={v'₀≤δ}, where |k|≤m/2 and |h−ĥ|≤(8/(7c_x²))(v+2|k|). With t=v'₀ and d⁴k=π²(1−z)²tdt:
- ∫_Bκ₁|h₁−ĥ|≤c(1−z)[δ+(4/5)√((1−z)δ)];
- ∫_Bκ₀|h₀−ĥ|≤c(1−z)[δ+4√((1−z)δ)].
Region A={v'₀>δ}: ρ_r=(κ₁−κ₀)(h₁−ĥ)+κ₀(h₁−h₀), with |κ₁−κ₀|≤2δ/(π²(1−z)v'₀³) and |h₁−h₀|=δh₁h₀≤δh₀².
- On |k|≤c_x/4: |h−ĥ|≤(2/c_x²)(v+2|k|) and h₀≤2/c_x. The contribution is ≤C[√δ+δ(L+ln(1/(z(1−z))))].
- On |k|>c_x/4: the κ's depend only on |k|, so average over the direction of k. Lemma 5.3 gives ⟨h₁⟩≤2/(c_x+t) and ⟨h₀²⟩≤(2/d̄²)(1+(d̄/(zc_x))^{1/2}), with d̄≥c_x+t. The contribution is ≤C(δ+δz^{−1/2}).
- Integrating over z gives ∫|ρ_r|≤C(x)m.
Proof of (b).
- (CS1)_{R1}=κ₁(h₁−ĥ), with |k|≤λ and |h₁−ĥ|≤c(λ²+2λ). It is ≤3cλ(1−z)ln(1/z).
- (CS2)_{R1} is C_H on U_{R1}, ≤c(1−z)(λ²+4√(1−z)λ).
- (CS1)_H is r on U_H, bounded by (a).
Grade [R, R_PT]. NEW (elementary).

### [results 21]
[X2-Thm5.1] INFINITE CLASS II: DIS LADDERS OF EVERY LENGTH n. DOWNGRADED from [R] to [P].
Claim: for every n, (CS1^φ)–(CS3^φ) hold on the cover N_{R_j}={v_i≤λ², |k_iT|²/(1−z_i)≤λ² for i≤j}, U_{R_j}=N_{R_j}∖N_{R_{j+1}}, with items ≤C_nλΛ^n. Moreover ∫|ρ_r|≤C_nλ(1+L)^n at ε=0.
Status.
- PROVEN for n=1 (Prop 5.1').
- n=2 is numerical (t11): the full norm is 2.63, 3.26, 3.90, 4.54, 5.19 λ for m²=10⁻²…10⁻⁶, i.e. ≈(1.3+0.27L)λ. With the q-azimuth averaged it is 0.83–0.88λ (rung cross terms keep first order). With both azimuths averaged it is second order: 0.93, 1.51, 2.22, 3.06, 4.07 m².
- General n: proof sketch only.
Strategy. Induction on N_j(s)=‖U_j(s;·)‖_{L¹}, and on D_j(s,s̃)=‖U_j(s)−U_j(s̃)‖ for equal (ξ,K). The recursions are:
- (R1) N_j≤∫_A|Δκ|N_{j+1}+∫_Aκ₀D_{j+1}, plus the undifferenced bound on region B;
- (R2) D_j≤∫|κ(s)−κ(s̃)|N_{j+1}+∫κ(s̃)D_{j+1}. The projected parts cancel, since πs=πs̃.
Exact region-A constants, for |k|≥8√v:
- |v'−v'₀|≤(17/8)z√v|k|/(1−z);
- v'/v'₀∈[47/64,81/64];
- |Δκ|≤9z(√v/|k|)κ₀.
All k-integrals reduce to 1D integrals by Lemma 2.12.
Gaps in the round-0 outline, identified in this round:
- (g1) (P1) cannot hold pointwise at the top level j=n. h(s) is unbounded as ξ→0, and A+v+2K·q≥ξc_x is sharp. The induction must start at j=n−1, using the direction-averaged Lemma 5.3.
- (g2) On region B the projected kernel κ₀~(1−z)/|k|⁴ is not integrable at k=0 against an O(1) factor. The undifferenced form κ(s)|U(Φ(s))|+κ₀|U(Φ(πs))| must be used, with N_{j+1}(Φ(πs))=O(√v'₀).
- (g3) The Lipschitz bound (P2) at j=n−1 involves ⟨h²⟩, which carries the factor (d̄/d_min)^{1/2} with d_min≥zξc_x. A weight ξ^{−1/2} must be carried through the induction; it stays integrable through ξ_j=z_jξ_{j−1}.
- (g4) For large v the bounds grow like powers of Λ(v)=1+|ln v| (two-sided logarithm).
- (g5) ε-uniformity in d=6−2ε, with weights (t−zv)^{1−ε}, is not addressed.
Scope.
- This is a φ³₆ scalar statement only. It does NOT deliver slot X2c: prop:appN-ladder-cs is the fermion two-rung ladder with Dirac projections.
- The bounds hold only at real x≥x₀>1, not with the complex-ω uniformity that prop:disall-two-routes(b) needs.
Prior art:
- the OPE proof of moment factorization in the unphysical region (Ch5);
- Curci–Furmanski–Petronzio, NPB 175 (1980) 27 (ladder mass-singularity factorization);
- Collins' inductive Theorems 1R–4 (§10.7.5–10.7.6).
Conjecture [P]: the angle-averaged norm is O(λ²L^{b_n}).

### [results 22]
[X2-Prop5.4] TWO-ELEMENT CHAINS ('single collinear subgraph').
Setting: Γ=H(k)J(k,p), with regions {A<H}. T_A acts only on H (H(k)→H(πk)); T_H acts only on J (J→J̃).
Identities:
- C_A=H(πk)J;
- C_H=ΔH·J̃;
- r=ΔH·ΔJ.
Hence:
- (CS1)_A ⟺ ∫_{U_A}|ΔH·J| is small;
- (CS2)_A ⟺ ∫_{U_A}|ΔH·J̃| is small;
- (CS1)_H ⟺ ∫_{U_H}|ΔH·ΔJ| is small;
- (CS3) ⟺ integrability of HJ (uniformly), of H(πk)J and of ΔH·J̃ (for ε>0).
Grade [R] (algebra). This is the n=1 case of the ladder structure. The structure is known (App. D Ex. D.48) and is made precise here.

### [results 23]
[X2-Thm6.1] SUDAKOV FORM FACTOR TO ALL ORDERS: PRECISE CONDITIONAL THEOREM (scalar model M1).
Setting.
- (M1) at fixed order N, with integrand-level renormalization (Ass. D.41 (U1)(U2)) of all UV-divergent subgraphs: the one-loop ψ and φ self-energies and the J–φ mixing bubbles. Tadpoles vanish in massless DR.
- Regions: the meet closure of the leading regions. Approximators: soft-first.
Premises: (AR) and (ID) (Lemma 2.7) for all terms; (F1), a cover with (CS1^φ) and (CS2^φ) at exponent a>0; (CS3^φ).
Conclusion: Σ_ΓΣ_R∫C_RΓ=F^(N)+O(λ^aL^K), and each term is absolutely convergent for ε>0. The UV poles cancel in the sum (Prop D.16 under (A1)(b)).
Gauge theories would additionally need D.37 (Ward product structure) and the P_A/K-gluon approximators, for which (Abs) may fail through transverse couplings.
Grade [R, R_cond].
Status of the premises.
VERIFIED here:
- (CS3^φ) for Γ at all orders, for UV-finite graphs without tadpoles (Cor 2.11) [R, R_PT];
- (F1) at N=1 for all graphs: the triangle (sharp λ²L² at ε=0; λ^{8/5} uniformly on (0,1/10]), and the J–φ mixing graph (H only, a tree times the renormalized insertion; remainder Π_R(q²)D(q)−Π_R(q̂²)D(q̂)=O(λ²)) [R, R_PT];
- (AR)+(ID) for all terms at N=1 (exact identification, Lemma 2.7);
- (F1) for the bubble-chain class in the hybrid model, for each fixed j: λ²L^{j+2}, with C_j≳j!. These are not all N in any summed sense;
- (Com), (Abs) (soft-first) and the product formula for the N=2 planar ladder [R];
- the exact integrated N=2 planar remainder [R, R_cond].
NOT VERIFIED:
- (AR)+(ID) of the Collins terms at all orders. Eikonal factors lose their k⁻ dependence, so zero modes must be excluded. At two loops only the decay of the 50 patterns was checked pointwise by the engine, and 40 composite patterns are scaleless (open items O11, O4).
- (F1) for the crossed two-loop vertex, for two-loop graphs with UV subdivergences (ψ self-energy and vertex subgraphs; BPHZ vs MS-bar and the Ward identities, ERR-M28), for the J–φ class beyond one loop, and for general N≥2. Goal (ii), 'all two-loop graphs', is NOT met.
- (CS1)–(CS3) bounds at N=2 (numerical only).
- Gauge numerators; Ward identities on approximated integrands; the (Abs) edge case X2d.
Positioning.
- For space-like kinematics the Symanzik F polynomial is positive. The integrated leading-power region expansion is therefore covered, or plausibly covered, by the literature on asymptotic expansions: Bergère–de Calan–Malbouisson, CMP 62 (1978) 137; Jantzen 2011; Semenova–Smirnov–Smirnov 2019; Poldaru, arXiv:2607.26291 (expansion by regions from the Mellin transform for positive-coefficient polynomials); Gardi–Herzog–Jones–Ma–Schlenk 2023 (on-shell expansion; multiple on-shell expansions commute for Sudakov regions).
- What is genuinely open is identifying that expansion with Collins' nested subtraction terms and operator definitions, together with integral-norm bounds. At two loops Thm 4.3 shows the integrated identification explicitly.
- The inductive structure is Collins Theorems 1R–4 (§10.7.5–10.7.6).

### [results 24]
[X2-Err] CORRECTIONS AND SHARPENINGS RELATIVE TO APP. D, as re-labelled after review.
(a) CONFIRMED correction of Lemma D.23(iii). (Abs) is not automatic for per-line meets: with the literal convention it fails in exactly 4 cases of the two-loop planar vertex, while soft-first suffices (Prop 4.2).
(b) SHARPENING, not an error (Def D.5/Lesson (d)).
- The λ^β, β<1 neighbourhoods are sufficient-condition choices for the general envelope argument.
- Natural-scale covers suffice where the grouped objects are computed explicitly, and give the sharp exponent: λ²L² for the triangle, versus the λ^{β/3}-type exponents of Lemma D.25.
- Fat neighbourhoods remain the device of the general argument.
(c) REMARK (Def D.9). (H3) on the real contour fails already for Γ. App. D works on a deformed contour Ω (Def D.2, Ass. D.7(A1)). The fibered form replaces that unconstructed deformation by checkable hypotheses (AR)+(ID).
(d) CONFIRMED sharpening. In the fibered form, non-maximal U_R must be UV-bounded, because individual subtraction terms carry UV logarithms that are not uniform in ε: ∫_{U_C1∩{k⁺>P}}|ρ_CC2|≈s^{1−ε}P^{−ε}/ε.
(e) WITHDRAWN: the space-like rapidity vectors of Def D.21 do not pinch (Prop 3.14).
(f) CONFIRMED, absent from the reference (Ex. D.47).
- The integral norm of the remainder is ≈λ²(4L̃−0.69), one log more than |∫r|=4λ².
- At ε=0 the sliver carries ζ₂/Q̃² of the integral and −2λ² of the remainder.
(g) CONFIRMED. (H3) is not necessary for the remainder bound (massive photon), but it is necessary for factorization into separately defined factors. The rapidity-divergence mechanism itself is known (Collins §10.5; Collins–Hautmann 2000).

### [results 25]
[X2-Err-own] RETRACTION OF AN INTERMEDIATE CLAIM OF ROUND 0 (for the record).
Round 0 at first expected the exponent 1 of the 2×2 cover to be optimal, i.e. that 'Thm D.10 necessarily loses one power'. This is false: θ=2 is optimal and gives λ²L² (Thm 3.3). The data show B(θ)=(θ/2)sL(1+o(1)) for θ<2, never λ²L/s, and ≈1.44sL at θ=2.
The sentence 'exponent 1 (theta=1) is optimal' in the t18 docstring is now marked RETRACTED inside the script.
The truncated round-0 draft still contains the claim (§0 item 3 and status-table row 3.4). It must not be used: REPORT.md must be written from this output.

### [results 26]
[X2-Est] ERROR ESTIMATES WITH EXPLICIT POWERS.
All at ε=0 unless stated. For ε∈(0,ε₀] the one-loop exponents decrease by at most 4ε₀, certified exactly at ε₀=1/10.
Triangle (M1):
- all items ≤Cλ²L² on the natural cover; the fat cover s=λ^θ gives Θ(λ^θL);
- remainder norm ≤Cλ²L² rigorously, ≈λ²(4L̃−0.69) numerically;
- signed ∫r=−4λ²+O(λ⁴L̃²), exact formula in Thm 3.5.
Bubble class (hybrid model):
- items and remainder ≤C_jλ²L^{j+2}, with C_j≳2j!/L₀^{j+2};
- numerically, norm ≈c_jλ²L^{j+1} and signed ≈−4λ²(−L)^j.
DIS (M2):
- one-rung remainder ≤Cλ rigorously, and =c₁(x)λ+o(λ) with c₁(2)=1.262984; items ≤Cλ;
- n=2 full norm ≈(1.3+0.27L)λ, numerically;
- the all-n bound C_nλ(1+L)^n is conjectural [P];
- one-loop H-only graphs after renormalization: vertex ≤Cλ²L (numerically ≈(0.46L+3.1)λ²); self-energy ≤Cλ² (≈0.871λ²); J–φ graphs O(λ²) exactly.
Massive photon (M3):
- light-like: ∫r=−λ²(L+1)−λ⁴(L/2+1/4)+O(λ⁶L) exactly, with norm ≈λ²(3.0L−0.85);
- time-like regulated: equal to the light-like value for Y≥L/2, with error ~e^{−2Y} otherwise.
Two-loop planar vertex:
- ∫r=−λ²(L̃⁴/2+π²L̃²+12+7π⁴/30)+O(λ⁴L̃⁴) [R, R_cond];
- every remainder norm is ≥½λ²L̃⁴(1+o(1));
- full norm ≈31–32λL (indicative [P]).

### [results 27]
[X2-Slots] MAPPING TO THE SPEC SLOTS (spec_v2/OUTLINE_appMNOPQ.md).
X2a, prop:appN-triangle-cs: DELIVERED in the fibered (k⁻-residue) form.
- Content: (CS1)–(CS3) for the one-loop off-shell triangle, with explicit exponents, uniformly in ε∈(0,1/10] (Thm 3.3 + Lemma 2.7).
- Grade [R, R_PT], computer-assisted.
- The status sentence of prop:appN-triangle-exact may change as planned.
X2b, thm:appN-oneloop: NOT DELIVERED.
- Only the equal-virtuality triangle p1²=p2² (plus the H-only J–φ mixing graph) is covered.
- Unequal or hierarchical virtualities, massive internal lines and gauge numerators are not covered.
- The fallback (deletion) stays.
X2c, prop:appN-ladder-cs: NOT DELIVERED.
- prop:appN-ladder is the fermion two-rung ladder with Dirac projections.
- X2 gives only the scalar φ³₆ analogue, proven for n=1 and numerical for n=2.
- The fallback stays.
X2d, rem:appN-abs-edge: OPEN.
- Prop 4.2 is a different issue, about conventions.
- The configuration of the remark (a soft line with both ends at hard vertices, gluon polarizations) has not been checked.

### [results 28]
[X2-REVISIONS] REVISIONS, FIX ROUND 1. Source: reviews r1_1 and r1_2 as relayed in the computed task; the files review_r1_1.md and review_r1_2.md do not exist.
P0 Process (r1_1 PROCESS, r1_2 F0). A subagent cannot fix this. REPORT.md must be written by the orchestrator from this output, and the reviews must be persisted. X1 and X3 have the same problem.
1 Space-like regulators (r1_1 R12, R19(e), O8; r1_2 F1).
- The 'genuine pinch' is withdrawn.
- Prop 3.14 is rewritten, with the Landau analysis and the deformation check (r1_spacelike.py).
- Err(e) is withdrawn and O8 is rewritten.
- 'Extends E1' is deleted, and the grade '[R] (pinch analysis)' is dropped.
2 Two-loop asymptotics (r1_1 R14, R21; r1_2 Num-2loop, F10).
- New Thm 4.3: the homogeneity and scalelessness check, the exact identity and the NLP formula (r1_twoloop_exact.py).
- The fitted rates are withdrawn, and the averaged-norm lower bound is added.
- The QMC was re-run with 16 randomizations (r1_twoloop_qmc.py), and the error statement is now honest.
3 One-loop DIS H-only graphs (r1_1 R10(ii); r1_2 F2). Prop 3.12 is rewritten:
- the complete graph list, including the J–φ mixing and t-channel graphs that round 0 missed;
- integrand-level BPHZ with plus-matched subtraction points, and T_H∘R=R∘T_H;
- proven (CS1)_H bounds, with '(H3) trivial' deleted;
- numerics in r1_dis_Honly.py.
4 DIS ladders of all n (r1_1 R16; r1_2 Thm5.1, F4).
- Thm 5.1 is downgraded to [P].
- A complete n=1 proof is added (Prop 5.1').
- Lemma 5.3 is proven analytically; r1_ladder1_analytic.py checks the closed form and c₁(x).
- The gaps g1–g5 of the general induction are listed.
- Scope: φ³₆ only; X2c is not delivered; there is no complex-ω uniformity.
- Prior art is positioned.
5 Thm 2.6 (r1_1 R1; r1_2 Thm2.6, F6).
- '(A1) disappears' is replaced by (AR) and (ID).
- New Lemma 2.7, with the triangle check (r1_triangle_covariant.py).
- (A1)(b) is kept for Prop D.16.
- The scope is restricted, E-F is renamed E-N^φ, and the grade is [R, R_cond].
- Caveat (a) is reclassified as a remark; caveat (c) is attributed to Collins §10.7.3.
6 Certificates (r1_1 R2, R7(b),(f); r1_2 Lem2.8, Thm3.3, F5).
- r1_lptools.py: the corrected recession check, exact primal–dual optimality, frozen variables as coefficients, and an LP cross-check.
- r1_triangle_recert.py: θ=2 and θ=1 covers, the global remainder cells and the sliver, at ε=0 and ε₀=1/10; archived in logs/r1_triangle_certificates.json.
- Comparability constants are listed; uniform constants come from κ^{−ε}≤1+κ^{−ε₀}.
7 Wording of Thm 3.3 (r1_1 R7(c),(d),(e), R19(b),(c); r1_2 F7).
- The corrections of Def D.5/Lesson (d) are re-labelled as sharpenings.
- (θ/2)sL is restricted to θ<2; at θ=2 the value is ≈1.44sL (r1_theta2_lower.py).
- It is stated that (CS1)_H is the global remainder certificate at θ=2.
- R19(c) is a remark.
8 Bubble class (r1_1 R9; r1_2 Thm3.9, F3).
- The sliver and part-III items are covered by the single-shell structure.
- Exact ε₀ runs (r1_bubble_recert.py), with the trivial alternative added for P3.
- The hybrid regularization and the factorial growth of C_j are stated.
- The Lemma 3.7 argument is written, and its model assumption is made explicit.
- t15c is marked invalid.
9 Prop 4.2 (r1_1 R13; r1_2 Thm4.1, F11).
- 'Necessary' is replaced by 'sufficient; the literal convention fails in exactly 4 cases'.
- Scripted in r1_abs_naive.py; R6 E5 is cited; X2d is stated as open.
10 Thm 6.1 (r1_1 R18; r1_2 Thm6.1, F8).
- Admissibility and identification at all orders are moved to 'unproven'.
- The crossed and subdivergent two-loop graphs are listed as unverified, and goal (ii) as not met.
- The N=1 graph list is corrected to include the J–φ graph.
- Positioning against the literature is added; O1 and O10 are reworded.
11 Attributions (r1_1 SUMMARY; r1_2 F8). Added: Collins §10.7.3, §10.5–10.6 and Theorems 1R–4; Collins–Hautmann; Borinsky Thms 8.A/8.B; Jantzen 2011; Semenova–Smirnov–Smirnov 2019; Gardi–Herzog–Jones–Ma–Schlenk 2023; Ma 2020 and 2024; Arkani-Hamed–Hillman–Mizera 2022; Bergère–de Calan–Malbouisson 1978; Poldaru 2026; Curci–Furmanski–Petronzio 1980; Chang–Yan 1973; Ligterink–Bakker 1995; Chiu–Jain–Neill–Rothstein 2012; Becher–Neubert 2011. All bibliographic data were checked on INSPIRE. The NEW labels are narrowed.
12 Grades and names (r1_2 F9). [R, ca] becomes [R, R_PT], computer-assisted. Conditional statements are [R, R_cond]. (CS1)–(CS3) are used. The retracted text is marked in the t18 docstring.
13 Prop 3.2 (r1_1 R6). 'At ε=0' and the dependence on fibration and routing are added.
14 Lemma 2.10 (r1_1 R3; r1_2 Lem2.10).
- Scope: no tadpoles; for DIS, no q⁺=0 subloops.
- Bound (b) becomes (m²+Q²(1−1/x))/2p⁺.
- The novelty is stated as modest.
- NOT adopted: the variant with 1/ξ from r1_2, which is invalid when spectators carry transverse momentum.
15 Thm 3.13 (r1_1 R11; r1_2 Thm3.13). The (CS3) failure is attributed; only the exact remainder is new.
16 Thm 3.5 (r1_1 R8). The exact NLP in Q̃ units and the norm fit λ²(4L̃−c') are added.
17 Lemma 5.2 (r1_1 R15). The pole-side argument is written out.
18 X2-Est, X2-Err, the summary and the open list are updated. New open items: O11 (AR)/(ID) at all orders; O12 ladders with n≥2; O13 bubble chains beyond the hybrid model; O14 slots X2b and X2d.

## open

### [open 1]
O1, central: App. D Ass. D.14 in fibered form.
- What is open is NOT the integrated leading-power region expansion. For space-like kinematics with positive Symanzik polynomials, that expansion is covered by the expansion-by-regions literature: Bergère–de Calan–Malbouisson 1978; Jantzen 2011; Semenova–Smirnov–Smirnov 2019; Poldaru 2026; Gardi–Herzog–Jones–Ma–Schlenk 2023.
- What is open: identifying that expansion with Collins' nested subtraction terms and operator definitions, together with the integral-norm bounds (CS1^φ)/(CS2^φ) for general graphs.
- The only inductive mechanism found here is the chain structure plus the 1D rung-kernel reduction, which covers ladders; its proof is complete only for n=1.
- The LP method needs explicit densities, i.e. finite sets of graphs.
- Overlapping regions, several jets with soft subgraphs, and non-planar topologies have no proof.

### [open 2]
O2: Gauge theories.
- No one-loop QCD vertex or box with Dirac numerators and the P_A=g_T+n⊗n̄ / K-gluon projections has been certified.
- Also open: instantaneous terms in LCPT for numerators with k⁻; failure of (Abs) for transverse polarizations of direction-flipping lines (Lemma D.23(iii)); Ward identities on approximated integrands (D.37 W1/W2).

### [open 3]
O3: Two loops beyond the planar ladder and the bubble insertion.
- The crossed ladder.
- Quark self-energy and vertex subgraphs: their UV subdivergences need integrand-level renormalization (U1)/(U2), and BPHZ versus MS-bar breaks the Ward identities (ERR-M28).
- The J–φ mixing class beyond one loop.
- Goal (ii), 'all two-loop graphs', is not met.

### [open 4]
O4: Two-loop planar vertex.
- A rigorous (CS1)–(CS3) proof is missing. The 5D densities contain Gram factors such as |k1T+k2T|², so Lemma 2.8 must be extended to Gram-positive factors or to angle-averaged fibrations.
- (CS3^φ) for the individual C_R must also be checked. 40 composite zeroing patterns are scaleless (Thm 4.3), so their fibered integrals cannot converge separately; only the combinations inside each C_R can.
- Present evidence is numerical.

### [open 5]
O5: Sharp second-order norms with angle-averaged fibrations.
- DIS ladders of all n: conjecture O(λ²L^{b_n}), supported by n=1 and n=2.
- Two-loop vertex: the averaged norm is now known to be ≥½λ²L̃⁴(1+o(1)), and the conjecture is that it is Θ(λ²L̃⁴).

### [open 6]
O6: Uniformity in ε for multi-loop transverse integrals in d=4−2ε (Gram-determinant weights). This is handled exactly only at one loop, where the exponent loss is ≤4ε₀ and is certified at ε₀=1/10.

### [open 7]
O7: Physical (cut) processes.
- The cut-sum representation (Ass. D.27) is untouched.
- Light-cone positivity holds only in space-like or unphysical kinematics.
- Physical DIS, e+e-, DY and TMD need the cut-summed integrand and certificates of their own. Glauber-pinched processes lie outside the scope of Thm 2.6.

### [open 8]
O8 (rewritten): Rapidity regulators.
- Needed: a TMD-type subtraction with proven (CS1)–(CS3).
- Time-like vectors work at one loop, with window Y≥L/2.
- For space-like vectors (Def D.21, Collins §10.6.4) there is NO pinch (Prop 3.14). What is needed is a version of the fibered method on a complex-deformed base k⁺, or another fibration, for which (CS3^φ) can be verified. A cancellation of pinch contributions is not what is needed.

### [open 9]
O9: Massive-photon (abelian) class beyond one loop. Not addressed: ladders and bubbles with a massive photon combined with Collins subtraction with time-like regulators, and abelian exponentiation.

### [open 10]
O10 (reworded): The all-order Sudakov theorem (Thm 6.1) rests on O1 and O11.
- Exponentiation, the product structure (D.37) and multiplicative renormalization (D.43) are not addressed.
- At fixed order in (M1), the integrated statement Σ∫C_R=LP+O(λ^a) is plausibly covered by the expansion-by-regions literature, as shown explicitly at two loops in Thm 4.3. The integral-norm bounds are not covered.

### [open 11]
O11 (new): Admissibility (AR) and identification (ID) of all Collins terms at all orders.
- What is needed is a zero-mode-free light-cone representation for approximated integrands. Eikonal factors lose their k⁻ dependence, so δ(k⁺) contributions must be excluded, e.g. via (I1)–(I2) of Lemma 2.7.
- Checked so far: the one-loop triangle (exact identification with the covariant values) and the (M2) one-loop graphs.
- Two loops: the decay was checked pointwise by the engine; the identification was not.

### [open 12]
O12 (new): DIS ladders with n≥2.
- Complete the induction of Thm 5.1, closing gaps g1–g5: top-level start with direction averaging, the region-B undifferenced bounds, the ξ^{−1/2} weight, two-sided logarithms, and ε-uniformity.
- The complex-ω uniformity needed by prop:disall-two-routes(b).
- The fermion ladder with Dirac projections (slot X2c).

### [open 13]
O13 (new): Bubble chains.
- The summed chain is open: C_j≳j! (a renormalon).
- So is the full (j+1)-loop graph beyond the hybrid model: the regions of the bubble loop momenta, and integrand-level renormalization of the bubble subgraphs together with the outer subtraction.

### [open 14]
O14 (new): Spec slots.
- X2b: unequal or hierarchical virtualities, massive internal lines and gauge numerators in the one-loop Sudakov class; the fallback stays.
- X2d: the (Abs) edge case of rem:appN-abs-edge, i.e. a soft line with both ends at hard vertices and gluon polarizations. It has not been checked whether such an assignment arises as a meet of leading regions.

## files

### [files 1]
/Users/hao-cheng/Desktop/theorem proof/qcd_factorization_work/verify/extend/X2-subtraction/REPORT.md (does NOT exist; to be written by the orchestrator from this output)

### [files 2]
/Users/hao-cheng/Desktop/theorem proof/qcd_factorization_work/verify/extend/X2-subtraction/scripts/r1_lptools.py

### [files 3]
/Users/hao-cheng/Desktop/theorem proof/qcd_factorization_work/verify/extend/X2-subtraction/scripts/r1_triangle_recert.py

### [files 4]
/Users/hao-cheng/Desktop/theorem proof/qcd_factorization_work/verify/extend/X2-subtraction/logs/r1_triangle_recert.log

### [files 5]
/Users/hao-cheng/Desktop/theorem proof/qcd_factorization_work/verify/extend/X2-subtraction/logs/r1_triangle_certificates.json

### [files 6]
/Users/hao-cheng/Desktop/theorem proof/qcd_factorization_work/verify/extend/X2-subtraction/scripts/r1_triangle_covariant.py

### [files 7]
/Users/hao-cheng/Desktop/theorem proof/qcd_factorization_work/verify/extend/X2-subtraction/logs/r1_triangle_covariant.log

### [files 8]
/Users/hao-cheng/Desktop/theorem proof/qcd_factorization_work/verify/extend/X2-subtraction/scripts/r1_theta2_lower.py

### [files 9]
/Users/hao-cheng/Desktop/theorem proof/qcd_factorization_work/verify/extend/X2-subtraction/logs/r1_theta2_lower.log

### [files 10]
/Users/hao-cheng/Desktop/theorem proof/qcd_factorization_work/verify/extend/X2-subtraction/scripts/r1_bubble_recert.py

### [files 11]
/Users/hao-cheng/Desktop/theorem proof/qcd_factorization_work/verify/extend/X2-subtraction/logs/r1_bubble_recert_items.log

### [files 12]
/Users/hao-cheng/Desktop/theorem proof/qcd_factorization_work/verify/extend/X2-subtraction/logs/r1_bubble_recert_remainder.log

### [files 13]
/Users/hao-cheng/Desktop/theorem proof/qcd_factorization_work/verify/extend/X2-subtraction/logs/r1_bubble_recert_small_eps0.1_v2.log

### [files 14]
/Users/hao-cheng/Desktop/theorem proof/qcd_factorization_work/verify/extend/X2-subtraction/scripts/r1_twoloop_exact.py

### [files 15]
/Users/hao-cheng/Desktop/theorem proof/qcd_factorization_work/verify/extend/X2-subtraction/logs/r1_twoloop_exact.log

### [files 16]
/Users/hao-cheng/Desktop/theorem proof/qcd_factorization_work/verify/extend/X2-subtraction/scripts/r1_twoloop_qmc.py

### [files 17]
/Users/hao-cheng/Desktop/theorem proof/qcd_factorization_work/verify/extend/X2-subtraction/logs/r1_twoloop_qmc.log

### [files 18]
/Users/hao-cheng/Desktop/theorem proof/qcd_factorization_work/verify/extend/X2-subtraction/scripts/r1_spacelike.py

### [files 19]
/Users/hao-cheng/Desktop/theorem proof/qcd_factorization_work/verify/extend/X2-subtraction/logs/r1_spacelike.log

### [files 20]
/Users/hao-cheng/Desktop/theorem proof/qcd_factorization_work/verify/extend/X2-subtraction/scripts/r1_dis_Honly.py

### [files 21]
/Users/hao-cheng/Desktop/theorem proof/qcd_factorization_work/verify/extend/X2-subtraction/logs/r1_dis_Honly.log

### [files 22]
/Users/hao-cheng/Desktop/theorem proof/qcd_factorization_work/verify/extend/X2-subtraction/scripts/r1_abs_naive.py

### [files 23]
/Users/hao-cheng/Desktop/theorem proof/qcd_factorization_work/verify/extend/X2-subtraction/logs/r1_abs_naive.log

### [files 24]
/Users/hao-cheng/Desktop/theorem proof/qcd_factorization_work/verify/extend/X2-subtraction/scripts/r1_ladder1_analytic.py

### [files 25]
/Users/hao-cheng/Desktop/theorem proof/qcd_factorization_work/verify/extend/X2-subtraction/logs/r1_ladder1_analytic.log

### [files 26]
/Users/hao-cheng/Desktop/theorem proof/qcd_factorization_work/verify/extend/X2-subtraction/scripts/t18_cover_optimality.py (docstring: retracted claim marked)

### [files 27]
/Users/hao-cheng/Desktop/theorem proof/qcd_factorization_work/verify/extend/X2-subtraction/scripts/t15c_resolve_failures.py (docstring: marked invalid, not part of any proof)

### [files 28]
/Users/hao-cheng/Desktop/theorem proof/qcd_factorization_work/verify/extend/X2-subtraction/scripts/ (round-0 scripts still used: lcpt.py, tropical.py, exact_verify.py, t1, t2b, t2c, t3, t4, t4x, t4y, t4z, t5, t6, t6b, t7, t8, t9, t10, t11, t12, t13, t14, t15, t15b, t15d, t15f, t16, t16b, t17, t17x, t17y; superseded: recession.py, t15e, t4w, t19)

### [files 29]
/private/tmp/claude-501/-Users-hao-cheng-Desktop-theorem-proof/c211c739-758d-4b40-bbac-67f4e1a65da4/scratchpad/rev_x2/X2_structured_output.json (round-0 report content, recovered by review r1_2)
