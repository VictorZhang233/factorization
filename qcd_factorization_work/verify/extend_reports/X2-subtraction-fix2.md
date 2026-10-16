# X2-subtraction-fix2

(extracted verbatim from the workflow journal; structured output of the agent)

## summary

RUN STATUS. Answer to the relayed question 「在正常运行吗」: 不完全正常 (not fully normal). The workflow is running, and every computation in this fix round (round 2) finished normally. It produced 8 new scripts and 10 new logs or archives under verify/extend/X2-subtraction/{scripts,logs}, listed in 'files'.\nThe stage's deliverable still does not exist on disk. verify/extend/X2-subtraction/REPORT.md was not written: the harness refuses report files written by subagents, and this fix round is again a subagent. review_r1_*.md and review_r2_*.md do not exist either. I did not try to work around the block.\nThe COMPLETE REVISED REPORT is this structured output: this summary, 29 results and 15 open items. The last result, [X2-REVISIONS], is the REVISIONS section; it covers round 2 item by item and keeps the round-1 list.\nRequired action, which no subagent can take: the orchestrator or main session must\n- write REPORT.md verbatim from this output (journal.jsonl of workflow wf_52f29317-58b, agent aa54636b3bf3d0143, label X2-subtraction-fix2);\n- persist the four reviews: journal lines 74 and 70 (round 1) and lines 115 and 110 (round 2);\n- pass structured outputs directly to later stages.\nThe blocked round-0 draft and its scratch copies contain retracted text and must not be used.\n\nTOPIC (unchanged). App. D proves its precise subtraction theorem (Thm D.10) under hypotheses (H1)–(H3), which are our (CS1)–(CS3), together with (A1)–(A4) and D.14/D.27/D.37/D.43. X2 verifies these hypotheses in a fibered (light-cone residue) form, for explicit graphs and infinite classes of three scalar models:\n- (M1) an off-shell Sudakov vertex in φ³-type theory, d=4−2ε;\n- (M2) DIS in φ³₆, in the unphysical region;\n- (M3) an abelian massive photon.\nNo statement is made about QCD.\n\nWHAT ROUND 2 CHANGES. Every item of both reviews is addressed; the details are in [X2-REVISIONS].\n(1) IDENTIFICATION REPAIRED. Lemma 2.7 is now restricted to products of pure denominators.\n- It does not apply to the composite Collins terms. For C_C1, the moduli of its two residue pieces integrate to 462.7, 1644.8, 4614.2 and 12073 for cut-offs 10⁻⁴…10⁻¹⁶ at ε=0.1, so (I2) fails. C_H carries a numerator, which the lemma excludes.\n- (I1) is verified for no term and is now an explicit assumption wherever the lemma is used.\n- NEW Prop 3.1′: all four triangle Collins terms are identified EXACTLY.\n  - Fibered side: the κ-integral is done in closed form, leaving Beta integrals.\n  - Covariant side: the WHOLE integrand is Feynman-parametrized; every parameter integral converges absolutely for 0<ε<1.\n  - sympy confirms the two sides are equal.\n- The round-1 wording 'massless triangle plus scaleless terms' is withdrawn: 1/(D_g h1 h2) is boost invariant, and DR does not regulate it.\n- For Γ itself, fibered = covariant numerically to 3·10⁻¹⁷ (ε=0.3) and 3·10⁻²¹ (ε=0.1).\n- The integrated corollary of Thm 3.3 is now [R, R_cond], with the single premise (ID)_Γ.\n- New for the one-rung ladder: C_R1 is identified exactly; C_H agrees numerically to 4·10⁻¹⁷–3·10⁻¹³.\n(2) PROP 3.14 CORRECTED. With the stated i0's, the real-base density has THREE simple poles:\n- x=0, of the form c/(x−i0), above the axis;\n- −x₀′+i0, above (ρ_CS≠0 for x<0);\n- x₀−i0, below.\nWithdrawn: 'the only colliding pair is h1Y–G'; 'deform x into Im x>0'; 'integrate κ first'; and the attribution of these i0's to Collins (10.68), which treats the time-like form factor. These i0's are compatible with the symmetric Glauber deformation of (M3); Collins' sign pattern obstructs it. There is still no 4D pinch.\n(3) THM 4.3 CORRECTED.\n- The family dimensions 1, 2, 3, 4 occur 18, 15, 6 and 1 times.\n- 22 composite patterns have exact ε-independent (rapidity-type) invariances, so 'scaleless ⇒ 0 in DR' does not apply to them.\n- With independent analytic powers on the six lines, all 40 composites acquire a nonzero weight (exact check).\n- (ii) is restated as ∫Γ−∫r=Σ_{9 singles}∫T_RΓ. Both (ii) and (iii) are [R, R_cond], with explicit premises (Reg) and (F).\n- The norm lower bound additionally needs (ID) for r.\n- The result is relabelled a worked example of the zero-bin/overlap mechanism (Manohar–Stewart 2007; Idilbi–Mehen 2007; Jantzen 2011).\n(4) CERTIFICATES.\n- The face-dimension bound now uses S⁺={exact y_i>0}.\n- The 546 triangle certificates are clean.\n- The bubble class was re-run and fully archived: 70,373 exact certificates, no zero duals, no bound changed, all exponents reproduced.\n(5) PROP 5.1′(d) PROVEN: ∫|ρ_r|=c₁(x)λ+O(λ²L). The odd part integrates to exactly c₁λ, and numerically ∫|rest|≈0.37–0.49λ²L. The ε-uniformity claim is downgraded to a sketch.\n(6) THM 2.6: the unused hypothesis 'non-maximal U_R UV-bounded' is removed; it is now Remark (b). Graphs with q⁺=0 subloops are added to the scope exclusions.\n(7) POSITIONING.\n- Ma, JHEP 05 (2020) 012 is now cited correctly, as an IR forest formula with pairwise cancellation of singularities.\n- Added: Erdoğan–Sterman 2015, Feige–Schwartz 2014, Anastasiou–Sterman 2019, and Ellis–Georgi–Machacek–Politzer–Ross 1979.\n- The 'genuinely open' claim is narrowed.\n(8) WORDING fixes in Thm 3.9, Prop 3.2, Prop 3.12 and Cor 2.11.\n\nMAIN RESULTS AFTER ROUND 2:\n- Fibered subtraction theorem [R, R_cond].\n- Identification lemma for pure denominators [R].\n- Tropical certificate lemma [R].\n- LCPT sign lemma [R]; Cor 2.11 [R, R_cond] (LCPT–covariant equivalence as input), direct for the triangle and the ladder.\n- Triangle:\n  - densities [R, R_PT];\n  - exact Collins-term identification [R];\n  - (CS1)–(CS3) at λ²L² [R, R_PT, computer-assisted];\n  - integrated corollary [R, R_cond].\n- Bubble class [R, R_PT, archived].\n- One-loop DIS graphs [R, R_PT].\n- One-rung ladder (a)–(d) [R, R_PT]; C_R1 identification [R].\n- Ladders of all n [P].\n- Massive photon [R, R_PT].\n- Space-like regulators: pole structure [R].\n- Two-loop algebra [R] and scaling structure [R].\n- Two-loop integrated remainder [R, R_cond].\n- All-order conditional theorem [R, R_cond].\nNOT VERIFIED:\n- gauge numerators;\n- crossed, non-planar and UV-subdivergent two-loop graphs;\n- the two-loop (CS1)–(CS3) bounds and (Reg)/(ID) at two loops;\n- (I1);\n- identification of Collins terms beyond the triangle and the one-rung ladder;\n- ladders with n≥2;\n- cut (physical) processes;\n- slots X2b, X2c and X2d.

## results

### [results 1]
[X2-Setup] MODELS, CONVENTIONS, GRADES. Unchanged except the additions marked ROUND 2.
(M1) Sudakov model, d=4−2ε.
- Fields: complex 'quark' ψ and real 'gluon' φ; vertex gψ*ψφ; current J=ψ*ψ.
- External momenta: p1=(P,−m²/2P,0_T) and p2=(m²/2P′,−P′,0_T) in (+,−,T) components, both incoming, with p_i²=−m².
- Q̃²=2PP′, Q²=(Q̃²+m²)²/Q̃², λ²=m²/Q̃², L=L̃=ln(Q̃²/m²).
- One-loop graphs: the triangle and the J–φ mixing graph. External self-energies are amputated; tadpoles vanish in massless DR.
(M2) DIS model, d=6−2ε, with the same fields.
- Target ψ with p=(p⁺,−m²/2p⁺,0_T); J inserted twice (forward amplitude).
- Frame q⁺=0, q=(0,q⁻,q_T), Q²=q_T², x=Q²/(2p·q)≥x₀>1 (unphysical region), λ²=m²/Q², c_x=1−1/x.
(M3) Abelian massive photon, d=4−2ε: massless on-shell legs p1=(P,0,0_T) and p2=(0,−P′,0_T); boson mass M; λ²=M²/Q², Q²=2PP′.
Conventions.
- Measure ∫d^dk/(iπ^{d/2}) per loop; propagators 1/(−l²−i0); units Q̃=1 (M1) and Q=1 (M2, M3); the scripts mostly use P=P′=1/√2.
- Collins terms: C_RΓ=T_R(Γ−Σ_{R′<R}C_{R′}Γ), X_{R0}=Γ−Σ_{R<R0}C_RΓ, r=Γ−Σ_RC_RΓ (App. D Defs D.3, D.18, D.19). The soft-first convention is used at two loops.
- Names: (CS1)–(CS3) are App. D's (H1)–(H3); the fibered versions are (CS1^φ)–(CS3^φ).
ROUND 2 additions.
(i) Covariant value. Let F be built from quadratic propagators, linear (eikonal) factors and a polynomial numerator. Its covariant DR value I_F=μ^{2ε}∫d^dk/(iπ^{d/2})F is DEFINED by the Feynman/Schwinger-parameter representation of the WHOLE integrand (shift, Wick rotation, standard l-integrals), continued analytically in ε. 'DR linearity' means splitting a sum into pieces with disjoint convergence domains and adding the separately continued values. It is the standard convention and is used only where stated (Thm 4.3).
(ii) Fibered value I^fib_F=∫_Bρ_F dμ_ε. The one-loop normalizations are:
- (M1): (μ^{2ε}/Γ(1−ε))∫dk⁺dκκ^{−ε}ρ_F, with κ=|k_T|²;
- (M2), rung on shell: (1/Γ(2−ε))∫dξ/(1−ξ)∫dt t^{1−ε}(…), with S^{3−2ε} averages.
(iii) Auxiliary analytic regularization: independent complex powers 1+δ_l on the lines.
Grades follow WRITER_SPEC v2.2 §4.3.
- [R, R_PT]: rigorous for the stated graphs at the stated order, with no unproven input. 'Computer-assisted' means the only non-elementary inequalities are LP optima, certified by exact rational primal–dual pairs; scripts and certificates are archived.
- [R, R_cond]: complete proof from the listed premises.
- [P]: finite subclass or numerical evidence.
Error type E-N^φ: ∫_A|ρ_F|dμ_B≤Cλ^aL^K on the fibered base, with the fiber integrated exactly, uniformly in ε∈(0,ε₀].
No QCD claim is made anywhere.

### [results 2]
[X2-Thm2.6] FIBERED SUBTRACTION THEOREM (an implication). REVISED in round 2: an unused hypothesis is removed and the scope is extended (review r2_1; review r2_2 scope).
Setting.
- V is the space of finite sums of products Π_j(a_j(b)+Σ_iβ_ji(b)k_i⁻−i0w_j)^{−e_j}, times measurement functions of the base b=(k_i⁺,k_iT).
- Every propagator and eikonal factor is jointly affine in the minus components. The scalar approximators, which zero light-cone coordinates and the IR regulator, preserve V.
- Fibered density: ρ_F(b)=Π_i(iπ^{d/2})^{−1}∫dk_1⁻…dk_ℓ⁻F, evaluated by iterated residues (lcpt.py).
Hypotheses.
- (AR) Admissibility of every F∈{Γ, C_RΓ}: at a.e. b and at every stage, degree ≤−2 in the current k_i⁻ and simple poles only on one closing side.
- (ID) For Γ and every C_RΓ, ∫_Bρ_F=I_F, the covariant value of [X2-Setup].
- A finite measurable cover {U_R} of B. No boundedness is required. Round 1 also required the non-maximal U_R to be UV-bounded; the proof never used that, and the cover of Thm 3.3 violates it.
- (CS1^φ)_{R0}: ∫_{U_{R0}}|ρ_{(1−T_{R0})X_{R0}}|≤Cλ^aL^K.
- (CS2^φ)_{R0}: the same bound for C_RΓ, for every R≰R0. Both are uniform in ε∈[0,ε₀] with a>0.
- (CS3^φ): ρ_Γ∈L¹(B) uniformly in ε∈[0,ε₀], and ρ_{C_RΓ}∈L¹(B) for each ε∈(0,ε₀].
Statement. Uniformly in ε∈(0,ε₀]:
- ∫_B|ρ_Γ−Σ_Rρ_{C_RΓ}|≤C′λ^aL^K;
- |I_Γ−Σ_RI_{C_RΓ}|≤C′λ^aL^K.
Proof.
- Residue sums are linear, so identity (D.10), r=(1−T_{R0})X_{R0}−Σ_{R≰R0}C_RΓ, holds for the densities a.e. on U_{R0}. Both round-2 reviews re-derived it.
- The triangle inequality on the finite cover gives the norm bound.
- (CS3^φ) and (ID) give ∫ρ_r=I_Γ−ΣI_{C_R}.
Grade [R, R_cond] (premises (AR), (ID), (CS1^φ)–(CS3^φ)). Error type E-N^φ. It implies the integrated statement and is not comparable with E-N on a deformed 4D contour.
What it replaces.
- (A1)(a) of Ass. D.7 assumes an unconstructed 4D contour deformation compatible with all subtraction terms. It is replaced by (AR)+(ID), which can be checked graph by graph.
- (A1)(b) is still needed for Prop D.16.
Scope (extended). The theorem needs fibered densities that are absolutely integrable on the real base, e.g. (M1), and (M2) at x>1. NOT covered:
- Glauber-pinched processes (O7);
- real-base fibrations with poles (space-like rapidity regulators, Prop 3.14);
- graphs with q⁺=0 subloops. These are pure zero modes in this frame and violate (AR); examples are the J–φ mixing and t-channel graphs of (M2), Prop 3.12(iv),(v), which are treated outside the fibered framework.
Prior art for nested (forest) subtractions on general graphs, at the level of pinch surfaces:
- Collins 2011 Ch. 10 (Theorems 1R–4);
- Erdoğan–Sterman, PRD 91 (2015) 065033;
- Ma, JHEP 05 (2020) 012 (IR forest formula for wide-angle amplitudes; the singularities of its subtraction terms cancel pairwise).
What Thm 2.6 adds is the integral-norm (power-suppression) form on a real fibered base. NEW as a formulation; the proof is that of Thm D.10.
Remarks.
(a) Literal (H3) of Def D.9 on the REAL contour fails already for Γ: there is a ln(1/η) divergence across light cones. This is a remark, not an App. D error, because App. D works on a deformed contour Ω.
(b) [Sharpening; the round-1 hypothesis becomes this remark] For (CS2^φ) to hold uniformly in ε, the non-maximal U_R should be UV-bounded or carry items that decay fast enough.
- Example: ∫_{U_C1∩{k⁺>P}}|ρ_CC2|=∫_P^∞dx∫_0^{2sx}dκκ^{−ε}/(Pe₂(e₂+κ))≈s^{1−ε}P^{−ε}/ε, which is not uniform in ε for the unbounded U_R of Def D.5.
- The cover of Thm 3.3 puts the unbounded sliver {−m²/2P′<k⁺<0}×{κ>0} in U_C2. This is harmless, because the sliver items decay like κ^{−2}.
(c) The fibration is part of the statement. Adding transverse azimuths to the fiber turns first-order full norms into second-order ones. This is Collins 2011 §10.7.3: 'these commonly vanish after an integral over angle. Then the actual error is one power better: p = 2'. It is quantified in X2-Num-2loop and Prop 5.1′.

### [results 3]
[X2-Lem2.7] IDENTIFICATION OF FIBERED AND COVARIANT VALUES FOR PURE-DENOMINATOR PRODUCTS. REVISED in round 2: the scope is restricted and the applications are corrected (review r2_1 (ID); review r2_2 F3).
Setting: F=Π_j D_j^{−e_j} is a single product with every e_j≥1, i.e. no numerator factors and i0 only in denominators. F_η denotes F with every i0 replaced by iηw_j.
Hypotheses.
- (I1) For ε in a nonempty open interval E⊂(0,ε₀] and every η>0, ∫d^dk|F_η|<∞.
- (I2) G∈L¹(B,dμ_ε) for ε∈E, where G is the sum of the moduli of the η=0 residue terms selected by the algorithm.
Statement: for ε∈E, ∫_Bρ_Fdμ_ε=lim_{η→0}∫d^dkF_η. The identity extends by analytic continuation wherever both sides are analytic.
Proof.
- Fubini holds at finite η, by (I1).
- After a pole is substituted, every remaining factor is a denominator with Re(·_η)=Re(·_0), so |·_η|≥|·_0|.
- The closing side, sign(w/β), does not depend on η. Hence |ρ_{F,η}|≤G.
- ρ_{F,η}→ρ_F a.e., and dominated convergence gives the result.
Under (I1)–(I2) no zero-mode (k_i⁺=0) contribution can arise.
Grade [R]. NEW (elementary).
Scope after round 2.
(1) The lemma does NOT cover the composite Collins terms.
- C_C1=T₁+T₂: the η=0 pieces are 1/(Ah₂) and −1/(Bh₂), each ~1/(x(xm²+Pκ)) at the soft end. At P=P′=1/√2, m²=0.01, ε=0.1 their moduli integrate over x>δ to 462.72, 1644.85, 4614.22 and 12072.96 for δ=10⁻⁴, 10⁻⁸, 10⁻¹², 10⁻¹⁶, growing like δ^{−ε}/ε (r2_triangle_identification.py, PART E).
- C_C2 and C_H have the same defect. Written as one product, C_H=D_g/(t₁h₁t₂h₂) has the numerator D_g, for which |N_η|≥|N_0| fails.
- The one-rung ladder's C_H=κ₀(h₀−ĥ) also violates (I2), because ∫κ₀ĥ∝∫dt t^{−1−ε}.
- These terms are identified by direct computation instead: the triangle in Prop 3.1′, the ladder in Prop 5.1′(e).
(2) (I1) is NOT verified for any term in this report; it is an explicit assumption wherever the lemma is used. For the triangle's Γ it is plausible for 0<ε<1 by Minkowski power counting at fixed η: the worst regions, the two-dimensional cones {k²=0, p_i·k=0}, contribute ∫R^{−1−2ε}ln²R dR. It fails logarithmically at ε=0. Not proven.
(3) Where the lemma is applied (Γ of the triangle and of the one-rung ladder), (I2) holds.
- There is one residue term per base point, and ρ_Γ≥0.
- ∫ρ_Γ<∞ is checked directly. For the triangle, the κ-integral is explicit and leaves (Q̃²/(Q̃²+m²))∫_0^1du ln(1/u+Q̃²/m²)/(m²(1−u)+Q̃²u), plus an explicit sliver term. For ε>0, use κ^{−ε}≤1+κ^{−ε₀}.
- Hence (ID)_Γ ⇐ (I1).
(4) Numerical evidence for (ID)_Γ (r2_triangle_identification.py, PART F):
- triangle, P=0.8, P′=1.3, m²=0.1, ε=0.3: fibered = covariant = 15.5610705037585, relative 3·10⁻¹⁷;
- triangle, P=P′=1/√2, m²=0.01, ε=0.1: 40.3386417978396, relative 3·10⁻²¹;
- triangle at ε=0: 10⁻¹¹ (t2b);
- ladder: 10⁻¹³ (t6).
An independent standard input is the LCPT–covariant equivalence for scalar graphs (Chang–Yan, PRD 7 (1973) 1147; Ligterink–Bakker, PRD 52 (1995) 5954). There, covariant diagrams defined by Feynman rules are split into light-cone time-ordered diagrams by k⁻ contour integration, and zero modes occur only in loops whose plus momentum is constant along the loop. It is not proven at the rigour of this report.
(5) WITHDRAWN round-1 statements, replaced as indicated: 'Lemma 2.7 gives (ID) for all terms at N=1'; 'by Thm 2.6 and Lemma 2.7' (Thm 3.3, slot X2a); and 'checked: the (M2) one-loop graphs' (O11).

### [results 4]
[X2-Lem2.8] TROPICAL (LP) CERTIFICATE LEMMA. The implementation is repaired in round 2; the lemma itself is unchanged.
Setting.
- f=N/Π_kD_k in local coordinates y_i=e^{LX_i}, with m²=e^{−L} and L=ln(1/λ²).
- N is a real polynomial in (y,m²). Its coefficients may depend on 'frozen' variables confined to compact intervals in (0,∞).
- Each D_k is comparable on the cell to a positive-coefficient polynomial g_k. The constants are at most 2^{deg} per factor for the frozen ranges [1/2,1] and [1,2], and at most (15/7)^{deg} on the sliver.
- ψ_a(X)=⟨a+w,X⟩−a_m−Σ_k max_{b∈supp g_k}(⟨b,X⟩−b_m); U is a polyhedron.
Hypothesis: every ψ_a has a bounded argmax face F_a on U. Equivalently (proved), ψ_inf(r)<0 for every r∈rec(U)∖{0}.
Statement: ∫_U|f|Πy^{w−1}dy≤CL^dλ^{−2φ*}, where φ*=max_a max_Uψ_a and d=max dim F_a≤dim U. With weights (1+L|X|)^j, which log insertions require, the power is L^{d+j}.
Proof.
- Borinsky, AIHPD 10 (2023) 635 [2008.12310], Thms 8.A/8.B.
- A Hoffman-type error bound, then a Laplace estimate.
- Uniformity in ε: ψ_a is affine in ε (weight 1−ε), and κ^{−ε}≤1+κ^{−ε₀} combines the certificates at ε=0 and ε₀.
Implementation (r1_lptools.py):
- (i) exact rational dual and primal with c·x=b·y; strong duality is asserted before the face bound is used;
- (ii) exact 2D recession check on closed-quadrant pieces;
- (iii) frozen variables treated as coefficients.
ROUND 2 (review r2_2 F4): the bound dim F≤(n+K)−rank(A_{S⁺}) now uses S⁺={i: exact y_i>0}, the only constraints complementary slackness forces tight. Round 1 used the floating support S, which can understate the dimension when the exact dual vanishes on part of S (fixed in r2_lptools.py).
- Triangle: all 546 archived monomial certificates have y_i>0 on S (r2_cert_audit.py). Their face bounds are 0, 1 and 2 for 251, 207 and 88 certificates.
- Bubble class: re-run with r2_lptools and archived (Thm 3.9). No zero dual entry, and no bound changed.
- Every cell used here is 2-dimensional, so the stated L-powers (L^{≤2}, L^{j+2}) are the trivial bound d≤2 and never depended on the defect.
- The recession check for n≥3 is floating-point only and is not used in any proof.
Grade [R].
Novelty. The ingredients are known:
- Borinsky;
- polytope and region methods: Jantzen, JHEP 12 (2011) 076; Semenova–Smirnov–Smirnov, EPJC 79 (2019) 136; Gardi–Herzog–Jones–Ma–Schlenk, JHEP 07 (2023) 197; Ma, JHEP 09 (2024) 197; Arkani-Hamed–Hillman–Mizera, PRD 105 (2022) 125013.
Their use to certify Collins' integral norms appears to be new; both round-2 reviews repeated the INSPIRE searches. Ma, JHEP 05 (2020) 012 is a forest-formula paper; round 1 misfiled it here, and it is now cited under Thm 2.6 and Thm 6.1.

### [results 5]
[X2-Lem2.10/Cor2.11] LIGHT-CONE POSITIVITY (scalar cubic models, massless internal lines). REVISED in round 2: the input of Cor 2.11 is made explicit (review r2_1).
Hypotheses.
- G is a connected graph of (M1) or (M2) without tadpoles.
- In case (b), every loop carries target plus momentum. This excludes the J–φ mixing and t-channel graphs.
- Kinematics: (a) as in (M1); (b) as in (M2) with x>1.
Lemma 2.10 (residue algebra).
- For a.e. b, the fibered density equals a finite sum over x⁺-orderings of Π_lines(2l⁺)^{−1}Π_states(E_st−Σl_T²/2l⁺)^{−1}, times a positive constant.
- Every energy denominator is strictly negative.
- All orderings have the same number of states: 2ℓ for the vertex (V=2ℓ+1) and 2ℓ+1 for DIS (V=2ℓ+2).
- Hence ρ_G has a definite sign.
Bounds:
- (a) |E_st−Σ|≥m²/2P;
- (b) after the absorption, |E_st−Σ|≥(m²+Q²(1−1/x))/2p⁺. The 1/ξ variant proposed in review r1_2 does not hold when spectators carry transverse momentum.
Corollary 2.11: (CS3^φ) holds for Γ, uniformly in ε∈[0,ε₀], for every UV-finite graph that satisfies the hypotheses.
- In (M1), with ω=4−E−V: graphs without one-loop two-point subgraphs and without tadpoles.
- In (M2), with ω=6−2E: every DIS ladder.
Proof.
- By the sign, ∫|ρ_Γ|=|∫ρ_Γ|.
- ∫ρ_Γ=I_Γ<∞ by the LCPT–covariant equivalence (Chang–Yan 1973; Ligterink–Bakker 1995). This is an INPUT, with its hypotheses:
  - scalar vertices, so no instantaneous terms;
  - every loop with non-constant plus momentum, so no zero modes;
  - k⁻ integrands of degree ≤−2.
Lemma 2.7 cannot replace this input: for a single-signed density, (I2) is exactly ∫|ρ_Γ|<∞, i.e. the claim itself. For the triangle and the one-rung ladder, ∫ρ_Γ<∞ is checked by explicit integration, so there the corollary is unconditional.
Grade:
- Lemma 2.10 [R];
- Cor 2.11 [R, R_cond] (premise: the LCPT–covariant equivalence);
- [R] for the triangle and the one-rung ladder.
Verified numerically at one and two loops (t1, t9). Novelty is modest: negativity of LCPT energy denominators below threshold is classical, and is equivalent to positivity of the Symanzik F polynomial. Its use for (CS3^φ) is new.

### [results 6]
[X2-Lem2.12] ONE-DIMENSIONAL REDUCTION OF RUNG KERNELS (d=6). Unchanged.
Setup: the parent has (v,K); the child has fraction z and transverse momentum k; v′=zv+|k−zK|²/(1−z); κ=1/(π²(1−z)v′²).
Statement: for every F≥0,
- ∫d⁴kκF(v′)=(1−z)∫_{zv}^∞dt(t−zv)F(t)/t²≤(1−z)∫_{zv}^∞dtF(t)/t;
- for the projected parent (v=0, K=0): (1−z)∫_0^∞dtF(t)/t.
Proof: set l=k−zK; then d⁴l=π²|l|²d|l|² and |l|²=(1−z)(t−zv).
In d=6−2ε the reduction carries the factors (1−z)^{1−ε} and (t−zv)^{1−ε}. With the measure d^dk/(iπ^{d/2}), the rung-on-shell fibered measure is (1/Γ(2−ε))∫dξ/(1−ξ)∫dt t^{1−ε}(…)/v² (Prop 5.1′(e)).
Grade [R]. Elementary; new only as a tool. Re-derived by all four reviews.

### [results 7]
[X2-Prop3.1] ONE-LOOP OFF-SHELL TRIANGLE (M1): FIBERED DENSITIES. The identification has moved to Prop 3.1′.
Notation: x=k⁺, κ=k_T², u=x/P, e₂=m²+2P′x, h₂=2P′x, A=xm²(1−u)+Pκ, B=xm²+Pκ, a=m²/P′, w=2x+a.
Densities:
- ρ_Γ=1/(AD̂₂) for 0<x<P, with D̂₂=e₂[1+m²/Q̃²+κ/(Q̃²(1−u))]+κ; on the sliver, ρ_Γ=2/(wD_gD₁) at k⁻=P′+κ/w;
- ρ_CS=1/(Be₂) for x>0;
- ρ_CC1=xm²/(Q̃²AB) for 0<x<P, and −1/(h₂B) for x>P;
- ρ_CC2=−1/(Pe₂(e₂+κ)) for x>0, and w/(P[(a−w)P′w+aκ](P′w+κ)) on the sliver −a/2<x<0;
- ρ_CH=−x/(P(h₂+κ)(h₂(P−x)+Pκ)) for 0<x<P, and 1/(P(h₂+κ)h₂) for x>P.
Normalization: μ^{2ε}∫d^dk/(iπ^{d/2})F=(μ^{2ε}/Γ(1−ε))∫dxdκκ^{−ε}ρ_F.
Checks:
- symbolic residues (t1);
- the engine at 2000 points, maximum deviation 3·10⁻¹⁰ (t7);
- direct k⁻ integration (R6);
- ∫ρ_Γ=Φ^(1)(t,t)/Q² (Usyukina–Davydychev);
- own residue code of review r2_2, maximum deviation 3.5·10⁻²¹.
(CS3^φ): ρ_Γ≥0 and is finite uniformly in ε. Each ρ_{C_R} lies in L¹ exactly for 0<ε<1; every part has a definite sign, and its absolute integral is the closed form of Prop 3.1′.
Grade [R, R_PT]. The closed forms are known (App. D Ex. D.47 / R6); this is an independent verification.

### [results 8]
[X2-Prop3.1′] EXACT IDENTIFICATION OF THE TRIANGLE'S COLLINS TERMS. NEW in round 2 (reviews r2_1 and r2_2 F3). It replaces the round-1 numerical check (relative 4·10⁻⁷) and the appeal to Lemma 2.7.
Statement: for 0<ε<1 and all P,P′,m²>0 (μ=1), fibered value = covariant value = the following closed forms.
- C_S: Γ(ε)²Γ(1−ε)(Q̃²/m⁴)^ε/Q̃².
- C_C1 and C_C2: Γ(ε)Γ(−ε)Γ(1−ε)/Γ(1−2ε)·(m²)^{−ε}/Q̃²=−Γ(1+ε)Γ(1−ε)²/(ε²Γ(1−2ε))·(m²)^{−ε}/Q̃².
- C_H: Γ(1+ε)Γ(1−ε)²/(ε²Γ(1−2ε))·(Q̃²)^{−ε}/Q̃².
As in round 1, Σ_R∫C_R→L̃²+π²/3.
Proof, fibered side.
- κ-integrals: K1(α)=∫_0^∞dκκ^{−ε}/(κ+α)=gα^{−ε} and K2(α,β)=g(α^{−ε}−β^{−ε})/(β−α), with g=Γ(ε)Γ(1−ε).
- Each density part has the form c/((κ+α)(κ+β)) or c/(κ+α), with (α,β):
  - C_S: (xm²/P, −);
  - C_C1: (xm²/P, xm²(1−u)/P) for 0<x<P, and (xm²/P, −) for x>P;
  - C_C2: (e₂, −) for x>0, and (m²u, m²u(1−u)) on the sliver in u=w/a;
  - C_H: (h₂, h₂(1−u)) for 0<x<P, and (h₂, −) for x>P.
- The remaining x-integrals are:
  - J0=∫_0^1du u^{−1−ε}[(1−u)^{−ε}−1]=B(−ε,1−ε)+1/ε. The integral converges for ε<1 and equals the analytic continuation of the split form;
  - J1=∫_1^∞u^{−1−ε}du=1/ε;
  - J2=∫_0^∞s^{−ε}/(1+s)ds=g.
- Assembly:
  - C_C1=(g/Γ(1−ε))(m²)^{−ε}(J0−J1)/Q̃²; the x>P part cancels the 1/ε of J0;
  - C_C2: the sliver supplies J0 and the x>0 part −1/ε;
  - C_H=(g/Γ(1−ε))(Q̃²)^{−1−ε}(J1−J0).
Proof, covariant side (whole integrand).
- C_S=1/(D_ge₁e₂): Δ=λ₁λ₂Q̃²+m²(λ₁+λ₂).
- C_C1=(e₁−t₁)/(D_gh₂t₁e₁), with e₁−t₁=(m²/P)k⁺+k². Use 6∫dxdλ₁dλ₂[xt₁+(1−x)D_g+λ₁h₂+λ₂e₁]^{−4}. Then Δ=(x+λ₂)(m²(1−x)+Q̃²λ₁), and the even part of the numerator after the shift is l²+Δ. The l-integral gives Γ(1+ε)(2ε−1)Δ^{−1−ε}; then x^{−ε}/ε, (m²(1−x))^{−ε}/(εQ̃²) and B(1−ε,1−ε).
- C_C2: exchange 1↔2.
- C_H=D_g/(t̂₁h₁t̂₂h₂): Δ=Q̃²(x+λ₁)(1−x+λ₂), numerator −l²−Δ, l-integral Γ(1+ε)(1−2ε)Δ^{−1−ε}, then B(1−ε,1−ε)/ε².
- All parameter integrals converge absolutely for 0<ε<1. No scaleless-term convention is used.
Checks (r2_triangle_identification.py).
- PARTS A–C (sympy): the Δ's and numerator reductions are asserted symbolically, and the equality of both sides with the closed forms is checked with gammasimp.
- PART D, direct 2D fibered quadrature WITHOUT the κ-formula: relative 1.3·10⁻⁷ to 9.3·10⁻⁷ at P=0.8, P′=1.3, m²=0.1, ε=0.3, and 3·10⁻⁶ to 2.6·10⁻⁵ at P=P′=1/√2, m²=0.01, ε=0.2.
- PART D, the parametric integrals BEFORE the λ-integrations: 4·10⁻⁶ to 9·10⁻⁶.
Remark (review r2_2 (c)). The covariant decomposition C_H=[massless on-shell triangle]−1/(D_gt̂₁h₂)−1/(D_gh₁t̂₂)+1/(D_gh₁h₂) contains 1/(D_gh₁h₂). That term is exactly boost invariant with zero ε-weight, so DR does not regulate it; only the whole C_H has a value. WITHDRAWN: the round-1 wording 'massless on-shell triangle plus scaleless terms'. Likewise, the split C_C1=T₁+T₂ with T₂ DR-scaleless is no longer used.
Grade [R] (analytic; computer algebra and numerics serve as checks). NEW (elementary).

### [results 9]
[X2-Prop3.2] THE NEGATIVE-k⁺ SLIVER OF THE TRIANGLE. Unchanged except the recession-slope wording (review r2_2 F7).
The region is −m²/2P′<k⁺<0, at ε=0, in the routing and fibration of Prop 3.1.
Statements.
- ∫_sliverρ_CC2=ζ₂/Q̃² EXACTLY, to all orders in m. Indeed ∫dκρ_CC2=ln(a/(a−w))/(PP′w), and the w-integral gives Li₂(1)/(2PP′).
- ∫_sliverρ_Γ=ζ₂/Q̃²+O(m²/Q̃⁴), which is half of the π²/3 in (D.32).
- ∫_sliver r=−2m²/Q̃⁴+o(m²), half of the total −4m²/Q̃⁴.
For ε>0 the weight κ^{−ε} changes these values. In another routing or fibration the sliver is not a separate base region.
Numerics:
- ∫ρ_Γ(sliver)=1.644934 at λ²=10⁻⁶;
- the sliver remainder is −1.99979λ² at λ²=10⁻⁴ and −2.00000λ² at λ²=10⁻⁶ (t2b; reproduced by review r1_2).
Exact LP certificates of the sliver give λ² at ε=0 and λ^{9/5} at ε₀=1/10. The recession slopes are −1/2 at ε=0 and −9/20 at ε₀ (r1_triangle_recert.log); round 1 wrote −1/2 for both.
Grade [R] (analytic). NEW (elementary).

### [results 10]
[X2-Thm3.3] TRIANGLE (M1): (CS1^φ)–(CS3^φ) AT THE SHARP EXPONENT ON THE NATURAL COVER. REVISED in round 2: the integrated corollary (review r2_1 GAP; review r2_2).
Cover (Q̃=1, P=P′=1/√2, u=k⁺/P, κ=k_T², s=λ²):
- U_S={0<u≤s, κ≤us};
- U_C1={s<u≤1, κ≤us}∪{1<u≤2, κ≤s};
- U_C2={0<u≤s, us<κ≤u}∪sliver. The sliver part is unbounded in κ, which the revised Thm 2.6 allows; its items decay like κ^{−2};
- U_H is the complement.
Statement.
(i) At ε=0, every (CS1)/(CS2) item is ≤Cλ²L^{≤2}. The items are:
- on U_S: (1−T_S)Γ, C_C1, C_C2, C_H (C_H is λ⁴);
- on U_C1: (1−T_C1)X_C1, C_C2, C_H;
- on U_C2: (1−T_C2)X_C2, C_C1, C_H;
- on U_H: r.
(ii) For ε∈(0,1/10], every item is ≤C(λ²L²+λ^{8/5}), uniformly. The exact certificates at ε₀ give 8/5 or 9/5, and uniformity follows from κ^{−ε}≤1+κ^{−ε₀}.
(iii) (CS3^φ) holds as in Prop 3.1.
Fibered conclusion (Thm 2.6 norm part, no (ID) needed): ∫|ρ_r|≤Cλ²L² at ε=0, and ≤C(λ²L²+λ^{8/5}) on (0,1/10].
Integrated corollary (ROUND 2).
- (ID) for the four Collins terms holds exactly (Prop 3.1′).
- Given (ID)_Γ: |I_Γ−Σ_RI_{C_R}|≤C(λ²L²+λ^{8/5}) on (0,1/10].
- The single premise (ID)_Γ follows from Lemma 2.7 under (I1), and is verified numerically to 3·10⁻¹⁷ and 3·10⁻²¹ (ε=0.3, 0.1).
- WITHDRAWN: the round-1 justification 'by Thm 2.6 and Lemma 2.7'.
Evidence.
- Exact primal–dual optimal pairs.
- The corrected recession check; the maximum slope is −1/2 at ε=0 and −9/20 at ε₀.
- Frozen variables treated as coefficients, with comparability constants ≤2^{deg}, and ≤(15/7)^{deg} on the sliver.
- r_I, r_II, r_III and sliver A/B certified at λ².
- 58 certificates archived (r1_triangle_certificates.json). All 546 monomial certificates have exact y_i>0 on S (r2_cert_audit.py), so the S⁺ repair changes nothing.
- At θ=2, (CS1)_H coincides with the global remainder certificate.
L-power: L^{≤2}, which is trivial for 2D cells. The exact face bounds are 0, 1 and 2 for 251, 207 and 88 monomial certificates.
Cover family s=λ^θ.
- The certified exponent is θ (exact for θ=1, 3/2, 19/10 and 2).
- Lower bound: ∫_{U_S}ρ_CC1≥s/4.
- The (CS1)_C1 norm is ≈(θ/2)sL for θ<2. At θ=2 it is 1.36, 1.41, 1.43, 1.44 sL for λ²=10⁻⁴…10⁻¹⁰ (r1_theta2_lower.py).
Relation to App. D: natural-scale covers sharpen Def D.5/Lemma D.25. This is a sharpening, not an error correction.
Grade:
- fibered statements [R, R_PT], computer-assisted;
- integrated corollary [R, R_cond] (premise (ID)_Γ).
NEW: integral-norm verification of (CS1)–(CS3) for this graph. It delivers slot X2a in the fibered form.

### [results 11]
[X2-Thm3.5/Prop3.6] TRIANGLE REMAINDER: NORM VERSUS INTEGRAL. Unchanged.
Rigorous: ∫|ρ_r|≤Cλ²L² at ε=0 [R, R_PT, computer-assisted; Thm 3.3].
Numerical [P]:
- ∫|ρ_r|=c(λ)λ²L with c=3.53, 3.79, 3.89, 3.93, 3.95, 3.96, 3.962 for λ²=10⁻²…10⁻⁸ (t2b; reproduced by review r1_2);
- 91.41525λ² at λ²=10⁻¹⁰ (review r1_1);
- hence ∫|ρ_r|≈λ²(4L̃−c′) with c′→0.69: one log more than the integrated remainder.
Sign structure: soft box −1.04L, C1 strip −0.54L, k⁺>P strip +0.95L, hard part +0.48L (t2c). The monomial majorant is sharp to a factor 1.1–1.3 (t3).
Exact integrated remainder (known; REFDOC N12, reproduced). In units Q̃=1, ρt=m² holds exactly, so:
- ∫r=Φ^(1)(t,t)/Q²−(L̃²+π²/3)=4Li₂(−m²)/(1−m⁴)+(L̃²+π²/3)m⁴/(1−m⁴)=−4λ²+O(λ⁴L̃²);
- equivalently, in Q units: −4m²/Q⁴+(m⁴/Q⁶)(L_Q²−15+π²/3)+O(m⁶L²/Q⁸). Review r2_2 finds the residual ≈5m⁶L².
The fibered integral matches UD to 10⁻¹¹ (t2b). Round 2: the subtracted L̃²+π²/3 is the sum of the covariant C_R values, which are now identified exactly with the fibered ones (Prop 3.1′). Table 5 of the reference tests the leading power of the exact integral in Q, not the Collins remainder in Q̃ (ERR-m25).

### [results 12]
[X2-Thm3.9] INFINITE CLASS I: RENORMALIZED BUBBLE CHAINS (log insertions) IN THE HYBRID MODEL. REVISED in round 2: certificates archived, defect check done, corner wording fixed (review r2_2 F4; review r2_1).
Model (hybrid scheme).
- (M1), with the φ propagator replaced by the MS-bar-renormalized n-bubble chain at ε=0: Γ^(j)=ln^j(D_g/μ²)/(D_gD₁D₂), j≤n, μ=Q̃.
- The outer measure is d=4−2ε, with a fixed 4D insertion. The true d-dimensional renormalized chain is (−k²)^{−nε} times poles, not ln^j.
Lemma 3.7 [R in the hybrid model]: C_RΓ^(j)=ln^j(D_g)·C_RΓ pointwise, with the region set of the triangle. That this reproduces the leading regions of the full (j+1)-loop graph is a MODEL ASSUMPTION.
Four-shell representation, 0<u<1, v=1−u:
- ρ_r^(j)=Σ_s l_s^jT_s over the shells s=D,e,t,h;
- T_D=(v/D_G−1/u)/(um²v+κ), T_e=m²/(u(m²+u)(um²+κ)), T_t=1/(u(uv+κ)), T_h=1/((m²+u)(m²+u+κ))−1/(u(u+κ)).
Lemma 3.8 (rectangle rule, exact):
- l_D−l_e−l_t+l_h=δ=ln(A/B), with |δ|≤min(u²m²/(um²v+κ), CL(1+|X|));
- a∈[0,min(um²/κ,CL)] and b=ln(1/v)∈[0,min(u/v,CL)].
Single-shell structure:
- on the sliver, ρ_r^(j)=l_sl^jρ_r^(0) exactly;
- for 1<u≤2, C_S and C_C1 lie on the e shell, C_C2 and C_H on the h shell, and Γ=0.
Theorem. On the natural cover of Thm 3.3, for each fixed j, every (CS1)/(CS2) item and ∫|ρ_r^(j)| satisfy:
- ≤C_jλ²L^{j+2} at ε=0;
- ≤C_j(λ²+λ^{8/5})L^{j+2} uniformly for ε∈(0,1/10].
(CS3^φ) holds for 0<ε<1 in the hybrid sense.
Evidence (ROUND 2).
- Re-run with r2_lptools.py (face bound over S⁺) and FULLY ARCHIVED: r2_bubble_recert.py → logs/r2_bubble_certificates_items_big_small_eps0_1o10.json.gz.
- The archive holds 2986 piece records (cell, piece, chosen alternative, exponent, slope, comparability) and 70,373 exact monomial certificates (monomial, value, dual vector, primal point, S⁺, face bounds).
- Remainder 0<u<1, 270 cells: minimum exponent 2 at ε=0 and 1.6 at ε₀=1/10, with worst slopes −1/2 and −9/20. At ε₀, piece P3 uses the trivial alternative |δ|≤CL(1+|X|) in 9 deep cells.
- Remainder u>1, 60 cells: 2 and 1.8, slopes −1/2 and −11/20.
- Items on U_S, U_C1 (s<u≤1) and U_C2: 2 and 1.6.
- No exact zero dual entry on S; the repair changed no face bound; the maximal L-power bound used is 2. All of this is identical to round 1.
- The corner {v≤λ⁶, κ≤λ⁸} is bounded shell by shell: ∫_corner|T_s|≤Cλ^{a_s}L^k with exact exponents a_D=8, a_e=14, a_t=8, a_h=16 (t15f). Round 1 wrote 'each |T_s|≤λ⁸'.
- Sliver and part III: the triangle certificates times |l|^j≤(C(1+L|X|))^j.
Growth in j: C_j≳2j!/L₀^{j+2}. The u>1 UV tail gives ∫_1^∞(lnκ)^jκ^{−2}dκ=j!. Nothing can be said about the summed chain (renormalon).
Numerics [P] (t5): ∫r^(j)≈−4λ²(−L)^j. At λ²=10⁻¹⁰ the norms are 3.97λ²L (j=0), 4.84λ²L² (j=1) and 6.58λ²L³ (j=2).
t15c is invalid (its LPs are unbounded) and is not part of any proof.
Grade [R, R_PT] for each fixed j in the hybrid model, computer-assisted, with certificates archived. NEW.

### [results 13]
[X2-Prop3.12] ALL ONE-LOOP GRAPHS OF THE DIS FORWARD AMPLITUDE IN (M2). Wording REVISED in round 2 (review r2_1; review r2_2 F7).
Complete list, for current vertex Jψ*ψ and coupling gψ*ψφ:
- (i) 2 ladders;
- (ii) 4 vertex corrections;
- (iii) 2 hard-line self-energies;
- (iv) 4 J–φ mixing graphs;
- (v) 1 t-channel graph.
Tadpoles vanish, and external self-energies are amputated.
ROUND 2 wording.
- Graph (v) is ∝1/t at t=0, i.e. infinite in the forward limit. It is independent of x and has no discontinuity in ω. The forward amplitude is therefore DEFINED modulo x-independent terms: the observable is the x-dependent part, equivalently the discontinuity. This removes (v).
- Graphs (iv) and (v) contain q⁺=0 loops, which are pure zero modes in this frame. They violate (AR) and are treated outside the fibered framework; for (iv) the loop is a renormalized insertion Π_R(q²).
- In QCD the analogues of (iv) and (v) vanish by colour.
Statements (unchanged).
- (i) The collinear region is leading (Prop 5.1′).
- (ii) and (iii) are UV divergent (ω=0 and ω=2). Unrenormalized, ∫|ρ| at O(m²) grows with the cutoff Λ (25.4, 43.8, 62.2 m² for Λ=10², 10⁴, 10⁶). They are renormalized with integrand-level BPHZ and plus-matched subtraction points, and T_H∘R=R∘T_H.
Theorem.
- Vertex: (1−T_H)RΓ=S(P)[f(m²)−f(0)]+[S(P)−S(P̂)][f(0)−f₀], with ∫|ρ|≤C(x)λ²L.
- Self-energy: ∫|g(s)/s²−g(ŝ)/ŝ²|≤C(x)λ².
- (CS3^φ) holds uniformly in ε, and R={H} suffices.
The proofs are as in round 1: v₀H₀−vH=−zm²(v₀+H); H,H₀≥zc_x; |S(P)−S(P̂)|≤m²/(sŝ); g(s)=(c−c₀)²/(π²(a+c)(a+c₀)²). Review r2_2 reproduced the self-energy norm 0.87123m² analytically from Σ_R(s)=(1/6)[s ln(s/s₀)−s+s₀].
- (iv): the remainder [S(P)−S(P̂)]D(q)Π_R(q²)=O(λ²) [R].
Numerics (r1_dis_Honly.py): the vertex norm is ≈(0.46L+3.1)m², and the self-energy norm 0.871m².
Grade: (i)–(iii) [R, R_PT]; (iv) [R], outside the fibered framework. NEW.

### [results 14]
[X2-Thm3.13] ABELIAN MASSIVE PHOTON (M3) WITH LIGHT-LIKE APPROXIMATORS. Unchanged.
Per-line semilattice: T_S maps (t1,t2)→(h1,h2); T_C1 maps t2→h2; T_C2 maps t1→h1; T_H maps G=M²−k² to g0=−k².
Exact forms:
- C_S=1/(Gh1h2);
- C_C1=(1/(Gh2))(1/t1−1/h1);
- C_C2=(1/(Gh1))(1/t2−1/h2);
- C_H=(1/g0)(1/t1−1/h1)(1/t2−1/h2);
- r=−M²g0/(Gt1h1t2h2).
Fibered form, P=P′=1/√2:
- ρ_r=(M²/u)[(1−u)/((M²(1−u)+κ)(u(1−u)+κ))−1/((M²+κ)(u+κ))] for 0<u<1;
- ρ_r=−M²/(u(M²+κ)(u+κ)) for u>1.
The κ-integral of the 0<u<1 bracket vanishes identically.
Consequences:
- ∫r=−λ²(L+1)−λ⁴(L/2+1/4)+O(λ⁶L), exactly;
- the norm is ≈λ²(3.0L−0.85) [P].
(CS3) fails for C_S, C_C1 and C_C2 at every ε: these are rapidity divergences. So Thm D.10 does not apply, although r is integrable and O(λ²L).
KNOWN (attributed):
- Collins 2011 §10.5–10.6;
- Collins–Hautmann, PLB 472 (2000) 129;
- Jantzen, JHEP 12 (2011) 076 §6;
- Chiu–Jain–Neill–Rothstein, PRL 108 (2012) 151601;
- Becher–Neubert, EPJC 71 (2011) 1665.
NEW only: the exact light-like remainder formula, and the remark that the remainder bound holds without (CS3), while factorization into separately defined factors needs (CS3).
Grade: exact formula [R, R_PT]; norm [P].

### [results 15]
[X2-Prop3.14] RAPIDITY-REGULATED SOFT APPROXIMATORS IN (M3): TIME-LIKE VERSUS SPACE-LIKE. REVISED again in round 2: parts (b) and (c) are corrected (review r2_1).
Time-like vectors: h1Y=2P(k⁻+e^{−2Y}k⁺) and h2Y=2P′(k⁺+e^{−2Y}k⁻).
- The eikonal and photon poles never collide on the real base.
- The rapidity integral converges (545.458 at Y=3, 1090.909 at Y=6), and (CS3^φ) holds for ε>0.
- For Y≥L/2 the remainder equals the light-like value within O(λ²), with norm ≈2.9λ²L [P].
Space-like vectors, with the i0's of t16/r1_spacelike: h1Y=2P(k⁻−ek⁺)−i0 and h2Y=2P′(k⁺−ek⁻)−i0, with e=e^{−2Y} and S=M²+κ.
(a) No pinch of the 4D integral [R] (unchanged).
- {G,h1Y}: k∝n_A is incompatible with k²=M²>0.
- {G,h1Y,h2Y}: the Gram determinant is −16P²P′²(1−e^{−4Y})²≠0.
- {h1Y,h2Y}: the gradients are independent.
(b) Real-base pole structure [R] (corrected; r2_spacelike_poles.py).
- x=k⁺>0, closing on the h1Y pole: ρ_CS=1/(P(S−2ex²−i0)(2P′x(1−e²)−i0)).
- x<0, closing on the h2Y pole: ρ_CS=1/(P′(S−2x²/e−i0)(2Px(1−e²)−i0)). This is nonzero; round 1 gave only x>0 and dropped the i0 of the 1/x factor.
There are three simple real-base poles.
(1) x=0: c/(x−i0) from both sides, with c=1/(2PP′S(1−e²)). At M²=10⁻³, Y=3, κ=0.01, x·ρ→90.9096494773 from both sides.
- Origin: as x→0, the h1Y pole (k⁻=ex+i0) and the h2Y pole (k⁻=x/e−i0) close in on k⁻=0 from opposite sides.
- This is a pinch of the fiber contour, not of the 4D integral, because h1Y=0 and h2Y=0 intersect transversally.
(2) x=−x₀′+i0, with x₀′=√(Se^{−2Y}/2) (G–h2Y collision); residue −1/(4PP′S(1−e²)).
(3) x=x₀−i0, with x₀=√(Se^{2Y}/2) (G–h1Y collision); same residue.
Numerical checks.
- At η=10⁻⁷ (t16 weights), the continued densities have poles at +5.89·10⁻⁸i, −0.0036923+4.66·10⁻⁸i and 1.4895833−2.37·10⁻⁵i. These are exact roots of the residue denominators.
- On intervals isolating each pole, the real-axis integrals at η=10⁻⁶, 10⁻⁸, 10⁻¹⁰ converge to PV+iπRes for x=0 and −x₀′, and to PV−iπRes for x₀, to 10⁻⁸.
Consequences.
- The real-base integral exists as a distribution (PV±iπδ at each pole).
- The singular parts can be integrated along small semicircles passing BELOW 0 and −x₀′ and ABOVE x₀.
- There is no global deformation of the base into one half plane.
- WITHDRAWN from round 1: 'the only colliding pair is h1Y–G'; 'removed by deforming x into Im x>0'; and the remedy 'integrate κ first; only a weak branch point remains'. The last fails because ∫dκκ^{−ε}c(κ) is a nonzero constant for ε>0, so a pole at x=0 survives.
- The round-1 check near x₀ (63.01377+142.80054i on [x₀/2,2x₀]) stands as a local statement.
(c) The i0 assignment and its attribution [R for the compatibility statements].
- These i0's are inherited from the light-like eikonals h1=2Pk⁻−i0 and h2=2P′k⁺−i0.
- They are compatible with the symmetric deformation that takes (M3) out of the Glauber region, k±→k±−iδ: the t1 pole in k⁻ and the t2 pole in k⁺ lie in the upper half planes, and along the deformation Im h1Y=−2P(1−e)δ and Im h2Y=−2P′(1−e)δ keep the sign of −i0.
- They are NOT the i0's of Collins (10.68). That equation concerns the time-like form factor, with deformation (10.67), k⁺→k⁺+iδ and k⁻→k⁻−iδ. Collins fixes the signs for universality by also requiring compatibility with the asymmetric deformation (10.69): 'the relative signs between the i0s and the k⁺ terms … all be the same'.
- WITHDRAWN: the attribution 'as in Collins §10.6.4'.
- Transplanting Collins' sign pattern to (M3) (h2Y→+i0) gives ρ_CS=0 for x<0, no pole at x=0, and both remaining poles, x₀′ and x₀, at −i0, so the base becomes deformable into Im x>0. But in (M3) this assignment obstructs the symmetric Glauber deformation: Im h2Y=−2P′(1−e)δ against +i0.
- Which assignment gives universal soft factors in space-like form-factor kinematics is not settled here.
In both assignments, what fails is only absolute integrability on the real fibered base, i.e. (CS3^φ) in this fibration. Time-like vectors have no real-base poles. Space-like vectors remain admissible for virtual graphs with contour-deformed approximants.
Grade: (a), (b) and (c) [R] (analytic, checked numerically); the time-like window [P]. NEW (elementary).

### [results 16]
[X2-Thm4.1/Prop4.2] TWO-LOOP PLANAR SUDAKOV VERTEX (M1): EXACT ALGEBRA. Unchanged.
Setup.
- Lines: g1=k1, g2=k2, a1=p1−k2, a2=p1−k1−k2, b1=p2+k2, b2=p2+k1+k2.
- 9 regions: HH, HC1, HC2, C1C1, C2C2, HS, C1S, C2S, SS.
- Approximators are coordinate-zeroing sets.
- Soft-first convention: this is Collins §10.6.6, 'the requirement that the hard factor does not depend on the soft momenta'.
Verified exactly (t8):
- the 12-edge Hasse diagram;
- meet closure;
- (Com);
- (Abs) for all 9 incomparable pairs;
- chain recursion = product formula (50 zeroing patterns).
Prop 4.2: the literal convention of App. D differs from soft-first in four entries. With it, (Abs) fails in exactly 4 cases (r1_abs_naive.py; confirmed by all reviews):
- on a2 the meet zeroes k2⁺ but neither region does: (C1C1,HS) and (C1C1,C2S);
- on b2 the same for k2⁻: (C2C2,HS) and (C2C2,C1S).
Soft-first is SUFFICIENT; necessity is not claimed. This corrects Lemma D.23(iii) (text verified by review r2_1). Slot X2d remains open.
Grade [R] (exact). NEW as an explicit check.

### [results 17]
[X2-Thm4.3] TWO-LOOP PLANAR VERTEX (M1, P=P′=1/√2, Q̃=1): SCALING STRUCTURE AND INTEGRATED REMAINDER. REVISED in round 2 (review r2_2 F1, F2, F6; review r2_1).
(i) [R, exact symbolic; r1_twoloop_exact.py, r2_twoloop_regulator.py] Scaling structure of the 50 zeroing patterns of r=Π_R(1−T_R)Γ (soft-first).
Definitions: the weights act on (k1±,|k1T|,k2±,|k2T|), with weight(m²)=μ. K is the space of m²-independent scalings (μ=0) under which every line factor is homogeneous; D0 is the degree of integrand×measure at ε=0.
Results.
- Γ itself is not homogeneous.
- The 9 singles T_RΓ (coefficient −1 in r) have K=0, i.e. a unique scaling, with D0=0 and m²-exponent −k_Rε: k_R=0 (HH), 1 (HC1, HC2), 2 (C1C1, C2C2, HS), 3 (C1S, C2S), 4 (SS).
- The 40 composites have D0=0 on the whole family, and dim K=1, 2, 3, 4 for 18, 15, 6 and 1 patterns.
- Every composite has a direction of nonzero ε-weight.
- The 22 composites with dim K≥2 also contain a subspace K0 of exact, ε-INDEPENDENT invariances (rapidity type), with dim K0=1, 2, 3 for 15, 6 and 1 patterns.
- Example: the boost (0,0,0,−1,1,0) of k2 in the pattern a1→2Pk2⁻, b1→2P′k2⁺, with k2 absent from a2 and b2. Its k2-subintegral is ∫d^dk2/(k2²·2Pk2⁻·2P′k2⁺).
- These 22 integrals are not defined in DR alone, so 'scaleless ⇒ 0 in DR' does not apply to them.
With independent analytic powers 1+δ_l on the six lines:
- the weight map K→(ε,δ_g1,…,δ_b2) is injective for all 40 composites (for example, the boost above gets weight δ_b1−δ_a1);
- so each composite is exactly homogeneous under a scaling of nonzero weight, and vanishes in DR + generic analytic regularization by the standard convention;
- the singles acquire m²-exponents −k_Rε−ℓ_R(δ) (e.g. ℓ_HC1=δ_a1+δ_g2).
WITHDRAWN: 'the other 40 patterns are homogeneous along a one-parameter family … scaleless and vanish in DR (standard convention)'.
(ii) [R, R_cond] Premises.
- (Reg)(a) The analytically regularized pattern integrals are meromorphic in (ε,δ). This is standard for quadratic propagators (Speer, J. Math. Phys. 9 (1968) 1404) and not proven here for the eikonal-type factors.
- (Reg)(b) The nine singles ∫T_RΓ and the nine Collins terms ∫C_RΓ are analytic at δ=0 for ε in a punctured neighbourhood of 0. That is, DR alone regulates them: the rapidity-type divergences of the composites cancel inside each C_R, as 1/(D_gh₁h₂) does inside C_H at one loop (Prop 3.1′).
- (F) ∫Γ and ∫r are finite at ε=0.
Then, by DR linearity over analytically continued pieces:
- ∫Γ−∫r=Σ_R∫C_RΓ=Σ_{9 singles}∫T_RΓ=Σ_Rc_R(ε)(m²)^{−k_Rε};
- by (F), this is a polynomial P(L̃) of degree ≤4;
- ∫r=Φ^(2)(t,t)/Q⁴−P(L̃);
- ∫Γ=Φ^(2)/Q⁴=(1+m²)[12Li₄(−m²)+L̃⁴/4+π²L̃²/2+7π⁴/60]/((1−m²)(1+m²)⁴) (Usyukina–Davydychev, PLB 298 (1993) 363 and PLB 305 (1993) 136; ρt=m²). ∫Γ is analytic at δ=0, since the off-shell vertex is UV and IR finite.
(iii) [R, R_cond] Additional premise: ∫r→0 as m→0, i.e. the subtraction theorem at this order (numerically supported). Then:
- P=LP=L̃⁴/4+π²L̃²/2+7π⁴/60;
- ∫r=−λ²(L̃⁴/2+π²L̃²+12+7π⁴/30)+O(λ⁴L̃⁴);
- values: −7.050661, −4.596744, −2.570489, −1.281728, −0.446917 and −0.0201338 for m²=0.04…10⁻⁶;
- ratio to the NLP formula: 0.924…0.999998.
Norms (premise added; review r2_2 F2).
- Every fibered norm is ≥|∫_Bρ_r|.
- Identifying ∫_Bρ_r with the covariant ∫r is (ID) for r at two loops, which is a PREMISE (O11). The QMC agreement supports it: within 0.05–2.4σ; n18 gives −7.036±0.22, −4.593±0.08, −2.386±0.24, −1.319±0.084.
- Under (ID)_r, (Reg), (F) and (iii): every norm is ≥½λ²L̃⁴(1+o(1)).
Labels (reviews r2_1, r2_2 F6).
- The identity Σ∫C_R=Σ∫T_R is the standard zero-bin/overlap mechanism: Manohar–Stewart, PRD 76 (2007) 074002; Idilbi–Mehen, PRD 75 (2007) 114017; Jantzen 2011.
- Here it is a worked example for Collins' nested subtractions at two loops, with the regulator requirement made explicit.
- The NLP coefficient is an elementary expansion of the Usyukina–Davydychev closed form.
NEW only as a worked example.

### [results 18]
[X2-Num-2loop] TWO-LOOP PLANAR VERTEX: DOUBLE-RESIDUE (LCPT) DENSITIES AND REMAINDER NORMS. Grade [P] (numerical). Unchanged apart from the round-2 note.
Engine: lcpt.py; order and weight independence to 5·10⁻¹⁰ (t9).
Validation of ∫ρ_Γ against Φ^(2)/Q⁴ (exact: 82.282, 223.863, 508.102, 1019.383):
- n18 run: 82.41±2.0, 222.4±1.1, 513.8±6.5, 1016.8±4.6;
- 16 randomizations: 81.66±0.55, 239.1±12, 505.9±1.8, 1020.2±5.2;
- n16 under-covers.
Errors are indicative only.
Remainder norms:
- full norm ≈31.3, 31.7, 31.5, 32.3 λL (first order; Collins §10.7.3);
- azimuth-averaged norm 11.3, 7.0, 3.46, 1.88 (t14).
The fits are withdrawn (round 1).
Round 2 note: these are fibered integrals. Their agreement with the exact covariant values tests (ID) for Γ and r at two loops, jointly with the premises of Thm 4.3.

### [results 19]
[X2-Lem5.2] DIS LADDERS IN (M2): POSITIVE LIGHT-CONE REPRESENTATION AND EXACT COLLINS STRUCTURE. Unchanged.
Statements.
- (a) Support: 0<k_n⁺<…<k_1⁺<p⁺.
- (b) Rungs on shell: ρ_c=Π_i[π^{−2}(1−z_i)^{−1}(v_i^(c))^{−2}]H^(c_{n+1}).
- (c) Invariants: v≥|K|²/(1−ξ) (Cauchy–Schwarz with weights z(1−ξ) and 1−z), so H^(0)>0.
- (d) The approximators commute, and r=U_0(s₀).
Pole sides:
- the rung pole is upper iff k_{j−1}⁺>k_j⁺;
- the spine and hard poles are lower;
- the propagated weight k_{j−1}⁺/(k_{j−1}⁺−k_j⁺) is positive.
Validation:
- n=1: fibered = covariant to 10⁻¹³ (t6);
- n=2: checked numerically (t11).
Grade [R, R_PT], given the standard LCPT input. Known structure (App. D Ex. D.48), made precise.

### [results 20]
[X2-Lem5.3] HARD-FACTOR LEMMA. Unchanged.
Statements:
- (i) d≥zξc_x;
- (ii) ⟨1/d⟩_{S³}=2/(d̄+√(d̄²−4|l|²))≤2/(1−z+zξc_x+|l|²/(1−z));
- (iii) ⟨1/d²⟩_{S³}≤(2/d̄²)(1+(d̄/(zξc_x))^{1/2});
- (iv) ∫_0^1(1−z)⟨1/d⟩dz≤2, uniformly in ξ.
Grade [R]. NEW (elementary).
For d=6−2ε the S³ averages become S^{3−2ε} averages: ⟨1/(a+bcosθ)⟩=2/(a+r)·₂F₁(1,ε;2−ε;(a−r)/(a+r)), with r=√(a²−b²). This was checked against direct quadrature in r2_ladder1_identification.py. The ε>0 analogues of (ii)–(iv) are not proven.

### [results 21]
[X2-Prop5.1′] ONE-RUNG DIS LADDER: COMPLETE PROOF AT ε=0. REVISED in round 2:
- (d) is proven with an explicit error;
- (e) identification is new;
- ε-uniformity is downgraded to a sketch (reviews r2_1 and r2_2 F7).
Hypotheses: (M2), x≥x₀>1, Q=1, λ=m≤c_x/8.
Notation:
- ρ_r=κ₁(h₁−ĥ)−κ₀(h₀−ĥ), with rung kernels κ₁=1/(π²(1−z)v′²), v′=zm²+|k|²/(1−z), and κ₀ the same with v′₀=|k|²/(1−z);
- h₁=1/(A+v′+2k·q), h₀=1/(A+v′₀+2k·q), ĥ=1/A, A=1−z/x, δ=zm²;
- k∈R⁴ is the transverse momentum, with d⁴k=π²(1−z)²t dt and t=v′₀.
Claims.
(a) ∫|ρ_r|≤C(x)λ.
(b) On U_{R1}={v′≤λ²}, with U_H the complement, all items are ≤C(x)λ.
(c) (CS3^φ) holds as in round 1.
(d) ∫|ρ_r|=c₁(x)λ+O(λ²L), with c₁(x)=4∫_0^1dξξ^{1/2}(1−ξ)^{3/2}/(1−ξ/x)². Values: c₁(2)=1.262984, c₁(1.3)=1.936673, c₁(5)=0.924158. The coefficient was first derived in review r1_1.
(e) [NEW] Identification of the Collins terms.
Proofs of (a) and (b): unchanged from round 1. Review r2_1 re-derived every inequality.
Proof of (d) (NEW). Write ρ_r=odd+rest, with odd:=−2k·q(κ₁−κ₀)/A².
(i) The odd part.
- κ₁−κ₀ depends only on |k| and is negative.
- ∫d⁴k|k||κ₁−κ₀|=(1−z)^{3/2}∫_0^∞t^{3/2}(t^{−2}−(t+δ)^{−2})dt=(1−z)^{3/2}δ^{1/2}·3π/2, EXACTLY.
- With ⟨|cosθ|⟩_{S³}=4/(3π), this gives ∫|odd|=c₁(x)λ exactly.
(ii) The rest on |k|≤c_x/4.
- There A+s≥c_x/2, and the exact identity h−ĥ=−s/A²+R₂(s), R₂(s)=s²/(A²(A+s)), gives rest=−E1+E2.
- E1=−δ/(π²(1−z)A²v′v′₀). It integrates to ≤C(1−z)δ(1+ln(1/((1−z)δ))).
- E2=κ₁R₂(s₁)−κ₀R₂(s₀). On region A use (κ₁−κ₀)R₂(s₁)+κ₀(R₂(s₁)−R₂(s₀)), with |R₂(s₁)−R₂(s₀)|≤Cδ(v′₀+δ+2|k|). On region B use direct bounds. Altogether ≤Cδ(1+L+ln(1/(z(1−z)))).
(iii) On |k|>c_x/4: ∫|ρ_r|≤C(δ+δz^{−1/2}) and ∫|odd|≤C(1−z)^{3/2}δ/c_x.
Integrating over z: ∫|rest|≤C(x)λ²L, hence |∫|ρ_r|−c₁λ|≤C(x)λ²L.
Numerics (r2_ladder1_even.py, x=2):
- ∫|odd|/λ=1.262937…1.262979;
- ∫|rest|/(λ²L)=0.491, 0.431, 0.401, 0.383, 0.371;
- (∫|ρ_r|−c₁λ)/(λ²L)=−0.076…−0.024, for m²=10⁻²…10⁻⁶;
- consistent with t6b.
(e) In d=6−2ε, with the fibered measure (1/Γ(2−ε))∫dξ/(1−ξ)∫dt t^{1−ε}(…)/v²:
- C_R1=S²R(p−k)Ĥ, with Ĥ=1/(Q²−2q⁻k⁺). Fibered = covariant = Γ(ε)∫_0^1dξ(1−ξ)^{1−ε}(ξm²)^{−ε}/(Q²(1−ξ/x)), EXACTLY [R]. Numerically to 10⁻²¹–10⁻²²: 11.27248142379893 at m²=0.01, ε=0.1, and 27.06758503548673 at m²=0.001, ε=0.3.
- C_H=S²R(p̂−k)(k²+2k·q_⊥)H₀Ĥ, as a whole: −Γ(ε)Q^{−2−2ε}∫_simplex[x₃(x₁+x₂c_x)]^{−ε}/(1−x₂/x)+2Γ(1+ε)Q^{−2−2ε}∫_simplex x₁x₃^{−ε}(x₁+x₂c_x)^{−1−ε}/(1−x₂/x).
- This equals the fibered value numerically to 3.9·10⁻¹⁷, 4.2·10⁻¹⁵ and 3.4·10⁻¹³ at ε=0.1, 0.2, 0.3: −6.58496209517625, −3.57272130934841, −2.60783786095414 [P] (r2_ladder1_identification.py).
ε∈(0,ε₀] — a SKETCH, downgraded in round 2.
- In d=6−2ε, the transverse measure carries (|k|²)^{−ε}.
- Lemma 2.12 brings the factors (1−z)^{1−ε} and (t−zv)^{1−ε}.
- The S³ averages become S^{3−2ε} averages.
- The region |k|~m gives the exponent 1−2ε.
- Uniform constants would follow from (|k|²)^{−ε}≤1+(|k|²)^{−ε₀}.
- The estimates are not written out. Round 1 wrote κ^{−ε}≤1+κ^{−ε₀}, which clashed with the rung kernel κ; corrected.
Grade:
- (a)–(d) at ε=0 [R, R_PT];
- (e): C_R1 [R], C_H [P];
- ε-uniformity [P].
NEW (elementary).

### [results 22]
[X2-Thm5.1] INFINITE CLASS II: DIS LADDERS OF EVERY LENGTH n. Grade [P] (downgraded in round 1).
Claim: for every n, (CS1^φ)–(CS3^φ) hold on the nested cover, with items ≤C_nλΛ^n, and ∫|ρ_r|≤C_nλ(1+L)^n at ε=0.
Status.
- n=1: PROVEN (Prop 5.1′), now including the leading coefficient and the identification.
- n=2: numerical (t11). The full norm is ≈(1.3+0.27L)λ; with both azimuths averaged it is second order, 0.93…4.07m².
- General n: proof sketch, with gaps g1–g5.
Scope: φ³₆ only. It does not deliver slot X2c, and there is no complex-ω uniformity.
Prior art:
- the OPE proof (Ch5);
- ladder mass-singularity factorization: Ellis–Georgi–Machacek–Politzer–Ross, NPB 152 (1979) 285 (added in round 2), and Curci–Furmanski–Petronzio, NPB 175 (1980) 27;
- Collins' Theorems 1R–4.
Conjecture [P]: the angle-averaged norm is O(λ²L^{b_n}).

### [results 23]
[X2-Prop5.4] TWO-ELEMENT CHAINS ('single collinear subgraph'). Unchanged.
Setting: Γ=H(k)J(k,p), with regions {A<H}.
Identities:
- C_A=H(πk)J;
- C_H=ΔH·J̃;
- r=ΔH·ΔJ.
Hence each of (CS1)–(CS3) is equivalent to a smallness or integrability statement about these products.
Grade [R] (algebra). Known (App. D Ex. D.48); made precise here.

### [results 24]
[X2-Thm6.1] SUDAKOV FORM FACTOR TO ALL ORDERS: PRECISE CONDITIONAL THEOREM (scalar model M1). REVISED in round 2: the status list and the positioning.
Setting.
- (M1) at fixed order N, with integrand-level renormalization of all UV-divergent subgraphs.
- Regions: the meet closure of the leading regions. Approximators: soft-first.
Premises: (AR) and (ID) for all terms; (F1), a cover with (CS1^φ),(CS2^φ) at exponent a>0; (CS3^φ).
Conclusion:
- Σ_ΓΣ_R∫C_RΓ=F^(N)+O(λ^aL^K);
- each term is absolutely convergent for ε>0;
- the UV poles cancel in the sum (Prop D.16 under (A1)(b)).
Gauge theories would additionally need D.37 and the P_A/K-gluon approximators.
Grade [R, R_cond].
Status of the premises (corrected).
VERIFIED:
- (CS3^φ) for Γ at all orders, for UV-finite graphs without tadpoles, given the LCPT–covariant equivalence (Cor 2.11); direct for the triangle.
- (F1) at N=1 for all graphs: the triangle (λ²L² at ε=0, λ^{8/5} on (0,1/10]) and the J–φ graph [R, R_PT].
- (AR) for all N=1 terms.
- (ID) at N=1: exact for the four triangle Collins terms (Prop 3.1′), by direct computation and NOT by Lemma 2.7 as round 1 claimed. For Γ it holds under (I1), and numerically to 3·10⁻¹⁷. The J–φ graph is an explicit renormalized insertion.
- (F1) for the bubble-chain class (hybrid model, each fixed j; certificates archived).
- (Com), (Abs) and the product formula at N=2 [R].
- The two-loop scaling structure [R, exact].
- The integrated N=2 planar remainder [R, R_cond]; it inherits the premises (Reg) and (F) of Thm 4.3.
NOT VERIFIED:
- (I1);
- (AR)+(ID) of the Collins terms at N≥2: 22 composites carry rapidity-type invariances, and neither the C_R nor r is identified;
- (F1) for the crossed vertex, for UV-subdivergent graphs, for the J–φ class beyond one loop, and for general N≥2; goal (ii) is NOT met;
- the N=2 (CS1)–(CS3) bounds (numerical only);
- gauge numerators, Ward identities, and X2d.
Positioning (rewritten; reviews r2_1, r2_2 F5). Nested (forest) subtractions for general graphs exist at the level of pinch surfaces:
- Collins 2011 Ch. 10;
- Erdoğan–Sterman, PRD 91 (2015) 065033;
- Ma, JHEP 05 (2020) 012 [1910.11304]: a BPHZ-like IR forest formula for wide-angle massless amplitudes with any number of external momenta; it proves that all singularities of its subtraction terms cancel pairwise, and gives a factorized form;
- Feige–Schwartz, PRD 90 (2014) 105020 (all-order hard–soft–collinear factorization);
- Anastasiou–Sterman, JHEP 07 (2019) 056 (local two-loop IR counterterms).
The integrated leading-power region expansion is covered by the expansion-by-regions literature: Bergère–de Calan–Malbouisson 1978; Jantzen 2011; Semenova–Smirnov–Smirnov 2019; Poldaru, arXiv:2607.26291; Gardi–Herzog–Jones–Ma–Schlenk 2023.
NARROWED: what remains open is the off-shell, integrand-level version for general graphs. It consists of integral-norm bounds with explicit power suppression, uniform in ε, together with the identification of fibered and covariant values. X2 supplies these for the listed graphs.
WITHDRAWN: the round-1 phrase 'genuinely open'.

### [results 25]
[X2-Err] CORRECTIONS AND SHARPENINGS RELATIVE TO APP. D.
(a) CONFIRMED correction of Lemma D.23(iii) (Prop 4.2).
(b) SHARPENING (Def D.5): natural-scale covers give the sharp exponent.
(c) REMARK (Def D.9): (H3) fails on the real contour. The fibered form replaces the deformation by (AR)+(ID).
(d) CONFIRMED sharpening, now Remark (b) of Thm 2.6 and no longer a hypothesis.
(e) WITHDRAWN (round 1): the space-like vectors of Def D.21 produce no 4D pinch. Round 2 completes the replacement analysis (Prop 3.14):
- three real-base poles with definite sides;
- no global base deformation;
- an i0 assignment compatible with the Glauber deformation of (M3).
(f) CONFIRMED: ∫|ρ_r|≈λ²(4L̃−0.69), and the sliver carries ζ₂/Q̃² and −2λ².
(g) CONFIRMED: (H3) is not necessary for the remainder bound, but it is for factorization; the mechanism is known.

### [results 26]
[X2-Err-own] RETRACTION OF AN INTERMEDIATE CLAIM OF ROUND 0 (for the record).
- Round 0 expected the exponent 1 of the 2×2 cover to be optimal. This is false: θ=2 is optimal and gives λ²L².
- The claim is marked RETRACTED in the t18 docstring.
- The truncated round-0 draft and the scratch copies X2_REPORT_attempted.md and X2_REPORT_orig.md still contain it.
- REPORT.md must be written from THIS round-2 output only.

### [results 27]
[X2-Est] ERROR ESTIMATES WITH EXPLICIT POWERS. All at ε=0 unless stated. For ε∈(0,ε₀] the one-loop exponents decrease by at most 4ε₀, certified at ε₀=1/10.
Triangle (M1):
- items ≤Cλ²L²;
- fibered remainder norm ≤Cλ²L² [R, R_PT], ≈λ²(4L̃−0.69) [P];
- integrated: |I_Γ−ΣI_{C_R}|≤C(λ²L²+λ^{8/5}) [R, R_cond: (ID)_Γ];
- signed ∫r=−4λ²+O(λ⁴L̃²).
Bubble class: ≤C_jλ²L^{j+2}, with C_j≳2j!/L₀^{j+2}.
DIS (M2):
- one-rung ∫|ρ_r|=c₁(x)λ+O(λ²L) [R] (numerically |∫|ρ_r|−c₁λ|≤0.08λ²L);
- n=2 ≈(1.3+0.27L)λ [P];
- H-only graphs: vertex ≤Cλ²L, self-energy ≤Cλ², J–φ O(λ²).
Massive photon (M3): ∫r=−λ²(L+1)−λ⁴(L/2+1/4)+O(λ⁶L).
Two-loop:
- ∫r=−λ²(L̃⁴/2+π²L̃²+12+7π⁴/30)+O(λ⁴L̃⁴) [R, R_cond: (Reg), (F), ∫r→0];
- every norm ≥½λ²L̃⁴(1+o(1)) [additionally (ID)_r];
- full norm ≈31–32λL [P].

### [results 28]
[X2-Slots] MAPPING TO THE SPEC SLOTS (spec_v2/OUTLINE_appMNOPQ.md).
X2a, prop:appN-triangle-cs: DELIVERED.
- Fibered form (Thm 3.3) [R, R_PT, computer-assisted].
- Integrated form [R, R_cond], with the single premise (ID)_Γ. The Collins terms are identified exactly (Prop 3.1′). WITHDRAWN: the round-1 reference to Lemma 2.7.
X2b, thm:appN-oneloop: NOT DELIVERED. Only equal virtualities and the J–φ graph are covered; the fallback stays.
X2c, prop:appN-ladder-cs: NOT DELIVERED. There is only the scalar φ³₆ analogue: n=1 proven, including C_R1 (exact) and C_H (numerical); n=2 numerical. The fallback stays.
X2d, rem:appN-abs-edge: OPEN.

### [results 29]
[X2-REVISIONS]
REVISIONS, FIX ROUND 2. Sources: review r2_1 (journal line 115, agent a51dcb1cf908d4110) and review r2_2 (line 110, agent a03989ecad817d7ee), relayed in the computed task. The files review_r2_*.md do not exist.
P0 Process (r2_1 PROCESS; r2_2 F0). The blocker is unchanged: this output is the report. REPORT.md must be written from it, not from fix-1 and not from the blocked draft, and the reviews must be persisted.
1 Identification at N=1 (r2_1; r2_2 F3).
- Lemma 2.7 is restricted to pure denominators.
- The (I2) failure for composite C_R is shown (PART E).
- (I1) is stated as an assumption.
- New Prop 3.1′: exact closed-form identification (r2_triangle_identification.py).
- The wording 'massless triangle plus scaleless terms' is withdrawn.
- Corrected accordingly: the corollary of Thm 3.3, X2a, Thm 6.1 and O11.
- New: the (ID)_Γ check at ε>0 (PART F), and identification of the ladder's C_R1 (exact) and C_H (numerical) (r2_ladder1_identification.py).
2 Prop 3.14 (r2_1).
- The three poles and their sides are given; the x<0 density is added; the i0 of 1/x is restored.
- Withdrawn: the 'only colliding pair' claim, 'deform into Im x>0', and 'integrate κ first'.
- The Collins (10.68) attribution is corrected (r2_spacelike_poles.py).
- The summary item and O8 are updated.
3 Thm 4.3 (r2_2 F1, F2, F6; r2_1).
- Family dimensions corrected; the 22 rapidity-type composites identified.
- Injectivity of the analytic-regulator weight map shown (r2_twoloop_regulator.py).
- (ii) restated; (Reg) and (F) made explicit; (ID)_r added as a premise for the norm bound.
- DR linearity stated.
- Relabelled as a worked example.
4 Certificates (r2_2 F4).
- S⁺ rank in r2_lptools.py.
- Triangle archive audited (r2_cert_audit.py).
- Bubble class re-run and archived (r2_bubble_recert.py).
5 Positioning (r2_1; r2_2 F5): Ma 2020 described correctly; Erdoğan–Sterman, Feige–Schwartz and Anastasiou–Sterman added; the 'genuinely open' claim narrowed.
6 Thm 2.6 (r2_1; r2_2): the unused hypothesis becomes Remark (b); q⁺=0 subloops added to the exclusions.
7 Prop 5.1′ (r2_1; r2_2 F7):
- (d) proven (r2_ladder1_even.py);
- notation fixed;
- S^{3−2ε} averages stated;
- ε-uniformity marked as a sketch.
8 Minor wording:
- Thm 3.9 corner exponents;
- Prop 3.2 slopes;
- Prop 3.12 (iv),(v);
- Cor 2.11 LCPT input;
- EGMPR 1979 cited;
- O4 extended.
9 Not changed, confirmed correct by both reviews: Setup, Lem 2.12, Thm 3.5/3.6, Thm 3.13, Thm 4.1/4.2, Num-2loop, Lem 5.2, Lem 5.3, Prop 5.4, Err (a)–(d),(f),(g).
REVISIONS, FIX ROUND 1 (kept; reviews r1_1, r1_2):
- Space-like pinch withdrawn.
- Two-loop Thm 4.3 introduced; fits withdrawn; QMC re-run.
- Prop 3.12 rewritten.
- Thm 5.1 downgraded to [P]; Prop 5.1′ and Lemma 5.3 analytic.
- Thm 2.6: (AR)/(ID) introduced, with E-N^φ.
- Certificates corrected and archived.
- Sharpenings relabelled.
- Bubble-class single-shell structure.
- Prop 4.2: 'sufficient' wording.
- Thm 6.1 positioning.
- Attributions added.
- Grades R_PT/R_cond adopted.
- Prop 3.2 at ε=0.
- Lemma 2.10 bound (b).
- Thm 3.13 attributed.
- Thm 3.5 NLP.
- Lemma 5.2 pole sides.
- Est, Err and open lists updated.

## open

### [open 1]
O1, central (narrowed in round 2): App. D Ass. D.14 in fibered form.
- The integrated leading-power region expansion is covered by the expansion-by-regions literature.
- Nested forest subtractions with pairwise cancellation of singularities, at the pinch-surface level for on-shell wide-angle amplitudes, are Ma 2020 (with Collins 2011, Erdoğan–Sterman 2015, Feige–Schwartz 2014).
- Open:
  - the off-shell, integrand-level integral-norm bounds (CS1^φ)/(CS2^φ) with explicit exponents for general graphs;
  - (AR)/(ID) of the Collins terms.
- The only inductive mechanism found covers ladders and is complete only for n=1.

### [open 2]
O2: Gauge theories.
- No one-loop QCD vertex or box with Dirac numerators and the P_A/K projections has been certified.
- Also open:
  - instantaneous LCPT terms;
  - (Abs) for transverse polarizations;
  - Ward identities on approximated integrands.

### [open 3]
O3: Two loops beyond the planar ladder.
- the crossed ladder;
- UV subdivergences (ERR-M28);
- the J–φ class.
Goal (ii) is not met.

### [open 4]
O4 (extended in round 2): Two-loop planar vertex.
- A rigorous (CS1)–(CS3) proof is missing (Gram factors).
- 22 of the 40 composite patterns carry exact ε-independent (rapidity-type) invariances. Any check of (CS3^φ) for an individual C_R must show that they cancel inside that C_R, as 1/(D_gh₁h₂) does inside C_H at one loop. Otherwise (CS3^φ) fails, as in (M3).
- This is equivalent to premise (Reg)(b) of Thm 4.3.
- The present evidence is numerical.

### [open 5]
O5: Sharp second-order norms with angle-averaged fibrations.
- DIS ladders: conjecture O(λ²L^{b_n}).
- Two-loop vertex: the averaged norm is ≥½λ²L̃⁴ under (ID)_r; conjecture Θ(λ²L̃⁴).

### [open 6]
O6: Uniformity in ε.
- Multi-loop transverse integrals (Gram weights) remain open.
- The ε-uniformity of the one-rung ladder is only sketched (S^{3−2ε} averages, (1−z)^{1−ε} factors).

### [open 7]
O7: Physical (cut) processes.
- The cut-sum representation (Ass. D.27) is untouched.
- Glauber-pinched processes lie outside the scope of Thm 2.6.

### [open 8]
O8 (rewritten in round 2): Rapidity regulators.
- Time-like vectors work at one loop for Y≥L/2.
- Space-like vectors, with the inherited i0's:
  - no 4D pinch;
  - three real-base poles (0 and −x₀′ above, x₀ below);
  - no global base deformation.
- Needed:
  - a fibered method on a locally deformed base, or another fibration in which (CS3^φ) can be verified;
  - a decision on the i0 assignment for universal soft factors in space-like form-factor kinematics (Collins' pattern obstructs the Glauber deformation of (M3)).

### [open 9]
O9: Massive-photon class beyond one loop.

### [open 10]
O10: The all-order theorem (Thm 6.1) rests on O1 and O11, together with the positioning of Thm 6.1.
- Exponentiation, D.37 and D.43 are not addressed.
- At fixed order the integrated statement is covered by expansion by regions; the integral-norm bounds are not.

### [open 11]
O11 (corrected in round 2): (AR)/(ID) of all Collins terms.
- Identified EXACTLY: the four triangle Collins terms (Prop 3.1′) and the one-rung ladder's C_R1 (Prop 5.1′(e)).
- Identified NUMERICALLY:
  - triangle Γ: 3·10⁻¹⁷ (ε=0.3), 3·10⁻²¹ (ε=0.1);
  - ladder Γ: 10⁻¹³;
  - ladder C_H: 3.9·10⁻¹⁷–3.4·10⁻¹³.
- Lemma 2.7 needs (I1), which is unverified, and fails for composite C_R through (I2).
- Needed: a grouped-residue version of Lemma 2.7 with a dominator for the group, or a rigorous LCPT–covariant equivalence for approximated integrands with eikonal factors and numerators.
- At two loops neither the C_R nor r is identified.

### [open 12]
O12: DIS ladders with n≥2.
- close gaps g1–g5;
- complex-ω uniformity;
- the fermion ladder (slot X2c).

### [open 13]
O13: Bubble chains.
- The summed chain is open: C_j≳j! (a renormalon).
- So is the full graph beyond the hybrid model.

### [open 14]
O14: Spec slots X2b and X2d.
- X2b: unequal virtualities, massive lines and gauge numerators.
- X2d: the (Abs) edge case.

### [open 15]
O15 (new in round 2): (I1), or a proof of (ID)_Γ that avoids it.
- For the triangle, after the κ-integral the 0<x<P part of the fibered Γ equals Γ(1+ε)(Q̃²/(Q̃²+m²))∫_0^1du∫_0^1dy(1−u)^{−ε}[m²(1−y+yu)+(1−y)Q̃²u]^{−1−ε} (checked to 1.6·10⁻¹⁷), plus an explicit sliver term.
- So (ID)_Γ is an identity between explicit two-dimensional parametric integrals. A change of variables proving it would make the integrated corollary of Thm 3.3 unconditional.
- (I1) itself is expected for 0<ε<1 and fails logarithmically at ε=0.

## files

### [files 1]
/Users/hao-cheng/Desktop/theorem proof/qcd_factorization_work/verify/extend/X2-subtraction/REPORT.md (does NOT exist; the orchestrator must write it verbatim from this output)

### [files 2]
/Users/hao-cheng/Desktop/theorem proof/qcd_factorization_work/verify/extend/X2-subtraction/scripts/r2_triangle_identification.py

### [files 3]
/Users/hao-cheng/Desktop/theorem proof/qcd_factorization_work/verify/extend/X2-subtraction/logs/r2_triangle_identification.log

### [files 4]
/Users/hao-cheng/Desktop/theorem proof/qcd_factorization_work/verify/extend/X2-subtraction/scripts/r2_spacelike_poles.py

### [files 5]
/Users/hao-cheng/Desktop/theorem proof/qcd_factorization_work/verify/extend/X2-subtraction/logs/r2_spacelike_poles.log

### [files 6]
/Users/hao-cheng/Desktop/theorem proof/qcd_factorization_work/verify/extend/X2-subtraction/scripts/r2_twoloop_regulator.py

### [files 7]
/Users/hao-cheng/Desktop/theorem proof/qcd_factorization_work/verify/extend/X2-subtraction/logs/r2_twoloop_regulator.log

### [files 8]
/Users/hao-cheng/Desktop/theorem proof/qcd_factorization_work/verify/extend/X2-subtraction/logs/r2_twoloop_regulator.json

### [files 9]
/Users/hao-cheng/Desktop/theorem proof/qcd_factorization_work/verify/extend/X2-subtraction/scripts/r2_lptools.py

### [files 10]
/Users/hao-cheng/Desktop/theorem proof/qcd_factorization_work/verify/extend/X2-subtraction/scripts/r2_bubble_recert.py

### [files 11]
/Users/hao-cheng/Desktop/theorem proof/qcd_factorization_work/verify/extend/X2-subtraction/logs/r2_bubble_recert.log

### [files 12]
/Users/hao-cheng/Desktop/theorem proof/qcd_factorization_work/verify/extend/X2-subtraction/logs/r2_bubble_recert_items_big_small_eps0_1o10.json

### [files 13]
/Users/hao-cheng/Desktop/theorem proof/qcd_factorization_work/verify/extend/X2-subtraction/logs/r2_bubble_certificates_items_big_small_eps0_1o10.json.gz

### [files 14]
/Users/hao-cheng/Desktop/theorem proof/qcd_factorization_work/verify/extend/X2-subtraction/scripts/r2_cert_audit.py

### [files 15]
/Users/hao-cheng/Desktop/theorem proof/qcd_factorization_work/verify/extend/X2-subtraction/logs/r2_cert_audit.log

### [files 16]
/Users/hao-cheng/Desktop/theorem proof/qcd_factorization_work/verify/extend/X2-subtraction/scripts/r2_ladder1_even.py

### [files 17]
/Users/hao-cheng/Desktop/theorem proof/qcd_factorization_work/verify/extend/X2-subtraction/logs/r2_ladder1_even.log

### [files 18]
/Users/hao-cheng/Desktop/theorem proof/qcd_factorization_work/verify/extend/X2-subtraction/scripts/r2_ladder1_identification.py

### [files 19]
/Users/hao-cheng/Desktop/theorem proof/qcd_factorization_work/verify/extend/X2-subtraction/logs/r2_ladder1_identification.log

### [files 20]
/Users/hao-cheng/Desktop/theorem proof/qcd_factorization_work/verify/extend/X2-subtraction/scripts/ (round-0/1 scripts still used: lcpt.py, r1_*.py, t1–t19 as listed in round 1)

### [files 21]
/Users/hao-cheng/.claude/projects/-Users-hao-cheng-Desktop-theorem-proof/c211c739-758d-4b40-bbac-67f4e1a65da4/subagents/workflows/wf_52f29317-58b/journal.jsonl (source of the reviews: lines 70, 74 for round 1 and 110, 115 for round 2; this output belongs to agent aa54636b3bf3d0143)
