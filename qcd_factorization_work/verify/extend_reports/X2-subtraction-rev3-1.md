# X2-subtraction-rev3-1

(extracted verbatim from the workflow journal; structured output of the agent)

## overall

fixable_issues

## per_result

### [per_result 1]
RUN STATUS (answer to 「在正常运行吗」): 在运行，但不完全正常. The workflow is running. Fix round 2 (agent aa54636b3bf3d0143) finished at 05:12, both round-3 reviewers started, and every script I ran finished normally. What is not normal: verify/extend/X2-subtraction/ still holds only logs/ and scripts/. REPORT.md does not exist; the directory mtime (Oct 10 17:45) shows it was never created. No review_r1_*/review_r2_* files exist either. So I reviewed the complete revised report as it actually exists: the fix-2 StructuredOutput, journal.jsonl line 122 of workflow wf_52f29317-58b (summary, 29 results, 15 open items). I checked it against reviews r2_1 (line 115) and r2_2 (line 110). The harness instructions forbid subagents to write report .md files, so review_r3_1.md was NOT written; this StructuredOutput is the review. My check scripts and logs are in /Users/hao-cheng/Desktop/theorem proof/qcd_factorization_work/verify/extend/X2-subtraction/review_r3_1_scripts/ (r3_numbers, r3_ladder_CH, r3_M1_infrared, r3_bubble_archive, each .py with its .log).

### [per_result 2]
[X2-Setup] CORRECT as conventions; it is consistent with the scripts I used (fibered normalization, covariant whole-integrand definition, rho t = m^2 at Qt = 1). HIDDEN ASSUMPTION: (M1) is a massless SUPER-renormalizable model ([g] = mass^1 in d = 4). Its off-shell vertex is IR-finite at fixed m only for restricted graph classes: one loop and the planar ladder, but not, e.g., graphs with phi self-energy insertions (see Cor 2.11 and Thm 6.1). The Setup must state the IR-finite graph class to which (M1) statements apply.

### [per_result 3]
[X2-Thm2.6] CORRECT as an implication. I re-derived r = (1-T_R0)X_R0 - sum_{R not<= R0} C_R at integrand level; linearity of residue sums plus the triangle inequality on the finite cover give the norm bound, and (CS3phi)+(ID) give the integrated bound. Removing the UV-boundedness hypothesis is fine because the proof never used it. Remark (b): the order of the example re-derives as ~(2s)^(1-eps) P^(-1-eps)/(2 eps(1-eps)). Scope: 'absolutely integrable ... e.g. (M1)' must read 'IR-finite graphs of (M1)', because generic (M1) graphs beyond one loop have non-integrable densities (Cor 2.11 below).

### [per_result 4]
[X2-Lem2.7] CORRECT for pure-denominator products. After a pole substitution the real parts do not depend on eta and the imaginary parts are eta times real coefficients, so |D_eta| >= |D_0|; the closing side is eta-independent; dominated convergence follows. The scope restriction is right. The (I2)-failure numbers 462.7 -> 12073 grow like delta^-eps: successive ratios 3.55, 2.81, 2.62 tend to 10^0.4 = 2.51. MINOR: (1) the proof uses simple-pole residue formulas, so the (AR)-type hypothesis (simple poles on the closing side, non-degenerate closing sides at finite eta) must be stated in the lemma itself. (2) The conclusion is lim_{eta->0} int d^dk F_eta, while (ID) uses the parametric value I_F of [X2-Setup]; the standard step 'Feynman-parametrize at finite eta, then eta -> 0' should be written or cited.

### [per_result 5]
[X2-Lem2.8] CORRECT as a lemma, and the S+ repair is right. I audited the round-2 bubble archive independently (r3_bubble_archive.py). It has 2986 piece records and 70,373 certificates, all 'ok'; exponent = -2 max(value) in every record; S+ equals the exact dual support in every certificate; no face-dimension bound changed; every primal point satisfies the archived cell constraints exactly. The minimum exponents are 2 at eps=0 and 8/5 at eps0 (items and 0<u<1), 9/5 for u>1 at eps0, and 8 and 36/5 for the corner, as claimed. CAVEAT: neither archive (triangle or bubble) stores the LP rows, right-hand sides or objective beyond the cell constraints, so optimality cannot be re-verified independently of r1/r2_lptools.py. The archive is not self-contained. Novelty: my INSPIRE searches found no prior LP/tropical certification of Collins norms (fulltext 'Collins subtraction' with tropical / 'Newton polytope' / 'linear programming': 0 hits). Belitsky-Smirnov PRD 113 (2026) 036022 §4 do use Newton polytopes and tropical geometry, but to evaluate region integrals of the same off-shell form factor; this related use should be cited.

### [per_result 6]
[X2-Lem2.10/Cor2.11] Lemma 2.10 CORRECT. Cor 2.11 is WRONG as stated for (M1). Counterexample (three loops): insert the two-loop 'kite' phi self-energy (psi loop with an internal phi chord) into the exchanged phi of the triangle. It has no one-loop two-point subgraph and no tadpole, and omega < 0 for every subgraph, so it is 'UV-finite' in the report's sense. Pi_2(k^2) = K(eps)(-k^2)^(-1-2eps) with K(0) = 6 zeta(3) x couplings > 0, so the graph is c x (triangle with phi power nu = 3+2eps). Lemma 2.10 gives rho >= 0, and near k -> 0 rho ~ 1/(2P m^2 (kappa + x m^2/P)^3), so int rho = +infinity for every eps in [0,eps0]. Its DR value is nevertheless FINITE at eps = 0: the corner of the parametric integral gives the pole at eps = -1/3, not at 0. Hence 'int|rho| = |int rho| = I_Gamma < infinity' fails even granting the LCPT-covariant equivalence. General criterion: in (M1) a soft subgraph has omega_IR = n_a - V_S (n_a = endpoints on non-soft lines, V_S = all-soft vertices). It is divergent if <= 0: any phi self-energy insertion, or a psi box coupled to four soft phi's (four loops, omega_IR = 0, no self-energy at all). The parametric criterion for the triangle with phi power nu is convergence iff nu < d/2 = 2-eps. Numerically (r3_M1_infrared.py), the corner integral converges for nu = 1 (24.7706), grows by ln(100)/m^4 = 46,052 per step for nu = 2, ~ln^2 for nu = 2 with the renormalized log, and ~1/delta for nu = 3. The (M2) clause is fine: in phi^3_6, omega_IR = 2 n_a > 0. This is the IR catastrophe of massless super-renormalizable models (Jackiw-Templeton, PRD 23 (1981) 2291, verified on INSPIRE).

### [per_result 7]
[X2-Lem2.12] CORRECT (d^4l = pi^2|l|^2 d|l|^2 with |l|^2 = (1-z)(t-zv); the d = 6-2eps form re-derived). The rung-on-shell fibered measure (1/Gamma(2-eps)) int dxi/(1-xi) int dt t^(1-eps)(...)/v^2 was re-derived from the R-pole residue 1/(p+(1-xi)) and S = 1/v at that pole.

### [per_result 8]
[X2-Prop3.1] CORRECT. I verified analytically the kappa- and x-integrals of all density parts, and the pole sides: all poles lie on one side for x < -a/2 and for x > P where stated; one residue per base point for Gamma; rho_Gamma > 0 on the sliver. Minor wording: 'its absolute integral is the closed form of Prop 3.1'' is inaccurate, because the absolute integrals involve J0+J1 where the signed ones involve J0-J1. Say 'is given by the same Beta integrals'.

### [per_result 9]
[X2-Prop3.1'] CORRECT; both sides independently re-derived. Fibered side: K1 = g alpha^-eps, K2 = g(alpha^-eps - beta^-eps)/(beta-alpha), J0 = B(-eps,1-eps)+1/eps, J1 = 1/eps, J2 = g; the assembly gives exactly the four closed forms. Covariant side: Delta_C1 = (x+l2)(m^2(1-x)+Qt^2 l1) with even numerator l^2+Delta and l-integral Gamma(1+eps)(2eps-1)Delta^(-1-eps); Delta_H = Qt^2(x+l1)(1-x+l2) with numerator -l^2-Delta and Gamma(1+eps)(1-2eps); Delta_S = Qt^2 l1 l2 + m^2(l1+l2). The values agree. Numerically: C_S = 27.6979046621097, C_C = -7.26621198785426, C_H = 2.92340552583143 at (0.8,1.3,0.1,0.3); sum C_R -> Lt^2+pi^2/3, checked at eps = 1e-6..1e-10 (24.4974606 at m^2 = 1e-2). POSITIONING GAP: the four closed forms are exactly the method-of-regions values of the off-shell triangle (h, c1, c2, us): T11^h = Gamma(-eps)^2 Gamma(1+eps)/Gamma(1-2eps), T11^c = Gamma(-eps)^2 Gamma(eps)/(2Gamma(-2eps)), T11^us = Gamma(1-eps)Gamma(eps)^2 (Belitsky-Smirnov PRD 113 (2026) 036022 App. A.1; Belitsky-Bork-Smirnov JHEP 05 (2025) 237). 'NEW (elementary)' can only refer to the fibered-side identification.

### [per_result 10]
[X2-Prop3.2] CORRECT (re-derived: int dkappa rho_CC2 = ln(a/(a-w))/(PP'w), then (1/2PP')int_0^1 -ln(1-u)/u = zeta2/Qt^2 exactly).

### [per_result 11]
[X2-Thm3.3] CORRECT as a computer-assisted fibered statement. The integrated corollary is now correctly [R, R_cond]: Prop 3.1' supplies (ID) for the four C_R exactly for 0<eps<1, and (ID)_Gamma is the single honest premise. uniformity on (0,1/10] follows from the uniform fibered norm bound and |I_Gamma - sum I_CR| <= int|rho_r|. No new defect found.

### [per_result 12]
[X2-Thm3.5/Prop3.6] CORRECT. Recomputed independently: int r = [4Li2(-m^2)+(Lt^2+pi^2/3)m^4]/(1-m^4), equal to Phi1/Q^2 - (Lt^2+pi^2/3) to 1e-35. The Q-unit residual (Q^2 int r - expansion)/(m_Q^6 L_Q^2) = 4.72, 5.16, 5.39 for m^2 = 1e-3, 1e-4, 1e-5, consistent with r2_2's '~5 m^6 L^2'.

### [per_result 13]
[X2-Thm3.9] WRONG LABEL / MODEL MISIDENTIFICATION; the mathematics for the stated integrand family stands. The report says '(M1), with the phi propagator replaced by the MS-bar-renormalized n-bubble chain at eps=0: Gamma^(j) = ln^j(D_g/mu^2)/(D_g D1 D2)'. This is false for (M1). In d=4, B0 is dimensionless and [g^2] = mass^2, so Pi_R(k^2) = (g^2/16pi^2)(c - ln(-k^2/mu^2)) carries NO factor k^2. The renormalized n-bubble chain is therefore g^(2n)(c - ln)^n / D_g^(n+1), not ln^j/D_g. By the criterion above (nu >= 2 > d/2 - eps) every such (M1) graph is IR divergent at fixed m, so (CS3phi) FAILS for the true chains. The structure ln^j(k^2)/k^2 belongs to renormalizable theories with Pi proportional to k^2 (phi^3_6, or the transverse gauge self-energy: the QCD-like large-beta0 chain). Also false for (M1): 'the true d-dimensional renormalized chain is (-k^2)^(-n eps) times poles' (a factor g^(2n)(-k^2)^(-n) is missing) and the renormalon interpretation. The certificate archive is internally consistent (see Lem 2.8), so the bounds hold for the log-weighted triangle family Gamma^(j). They do not concern any graph class of (M1).

### [per_result 14]
[X2-Prop3.12] CORRECT. The (iv)/(v) wording repairs are adequate. Analogues vanish in QCD (Tr t^a = 0). phi^3_6 has no soft IR problem (omega_IR = 2n_a), so the (M1) defect above does not affect (M2).

### [per_result 15]
[X2-Thm3.13] CORRECT and properly attributed; the rapidity-divergence failure of (CS3) is known.

### [per_result 16]
[X2-Prop3.14] CORRECT as rewritten. I re-derived both densities from the k- residues: for x>0, closing on h1Y gives 1/(P(S-2ex^2-i0)(2P'x(1-e^2)-i0)); for x<0, closing downward on h2Y gives 1/(P'(S-2x^2/e-i0)(2Px(1-e^2)-i0)). The three poles and their sides are as stated, with c = 1/(2PP'S(1-e^2)) = 90.9096494773 and residues -1/(4PP'S(1-e^2)) = -45.4548247386 at x0 = 1.48958328542 and -x0' = -0.00369230781107. The transplanted Collins assignment indeed gives rho = 0 for x<0, no x=0 pole, and both poles at -i0. I checked the attribution against the Collins text (§10.6.4, eqs. (10.67)-(10.69)); it is accurate: the symmetric deformation k+ -> k+ + i delta, k- -> k- - i delta is for the time-like case, and the requirement that 'the relative signs between the i0s and the k+ terms in (10.68) all be the same' comes from (10.69). Minor: 'compatible with k+- -> k+- - i delta' holds only locally in the Glauber region, because Im G = 2 delta(k+ + k-) can have the wrong sign elsewhere. Say that the deformation is local.

### [per_result 17]
[X2-Thm4.1/Prop4.2] CORRECT (confirmed by all previous reviews; the 4 (Abs) failures under the literal convention and the Lemma D.23(iii) text were verified by r2_1/r2_2). No new issue.

### [per_result 18]
[X2-Thm4.3] (i) CORRECT: the log reproduces dim K {1:18, 2:15, 3:6, 4:1}, dim K0 {0:18, 1:15, 2:6, 3:1}, 22 rapidity-type composites and an injective weight map; r2_2's independent code agrees. (ii)/(iii) CORRECT as conditional statements. I recomputed int r = -7.0506612, -4.5967436, -2.5704893, -1.2817277, -0.44691728, -0.020133844 and ratios to the NLP formula 0.92448 ... 0.999998. The m^2 list is 0.04, 0.01, 0.0025, 6.25e-4, 1e-4, 1e-6, not '0.04...1e-6'. POSITIONING GAP (significant): Smirnov-Rakhmetov, Theor. Math. Phys. 120 (1999) 870 [hep-ph/9812529], Sec. 2, treat exactly this diagram: the massless planar two-loop vertex with p_i^2 = -mu^2 and Q^2 -> infinity. They list the same nine regions (h-h, 1c-h, 2c-h, 1c-1c, 2c-2c, us-h, us-1c, us-2c, us-us), evaluate all nine region integrals and show the poles cancel to (Q^2)^2 F -> L^4/4 + pi^2 L^2/2 + 7pi^4/60, i.e. X2's P(L). Their prescription (c) sets scaleless integrals to zero 'even if not regulated within DR'. Belitsky-Smirnov 2026 App. A.2 give the nine integrals to O(eps^2). I checked that X2's singles T_HS and T_SS coincide with SR's (us-h), eq. (6), and (us-us), eq. (5); the m^2 exponents -k_R eps match all nine. Consequences: (a) 'NEW only as a worked example' is overstated; what is new is the Collins composite/zero-bin structure, the regulator analysis of the 22 composites and the NLP coefficient. (b) (Reg)(b) for the singles, (F) for int r and premise (iii) can be discharged by citing these explicit evaluations, once the nine singles are identified with SR's region integrals. (c) 'P is a polynomial of degree <= 4' needs pole order <= 4 of c_R(eps); this follows from those values but must be stated.

### [per_result 19]
[X2-Num-2loop] CORRECT as [P]. The exact Phi2/Q^4 values are re-verified independently: 82.28243299, 223.8634185, 508.1019667 and 1019.382822 for m^2 = 0.04, 0.01, 0.0025, 6.25e-4.

### [per_result 20]
[X2-Lem5.2] CORRECT (pole sides and the Cauchy-Schwarz invariant were re-checked by previous reviews; no new issue).

### [per_result 21]
[X2-Lem5.3] CORRECT; the eps>0 analogues are honestly marked unproven.

### [per_result 22]
[X2-Prop5.1'] (a)-(c) CORRECT. (d) CORRECT, re-derived: int d^4k|k||kappa1-kappa0| = (1-z)^(3/2) delta^(1/2) x [B(1/2,3/2) + 2B(3/2,1/2)] = (1-z)^(3/2) delta^(1/2)(3pi/2); <|cos theta|>_S3 = 4/(3pi); |int|a+b| - int|a|| <= int|b|. Splitting E1 and E2 at t ~ delta gives O(delta(1+L+ln(1/(z(1-z))))); the tails are O(m^2); hence O(lambda^2 L). c1(2) = 1.262983875, c1(1.3) = 1.936673074, c1(5) = 0.9241577558 confirmed. (e) C_R1 CORRECT [R]: fibered int dt t^(1-eps)/v^2 = (1-xi)^(2-eps)(xi m^2)^(-eps)Gamma(2-eps)Gamma(eps); covariant via Feynman/Cheng-Wu with the shift by lam*n (n^2 = 0, so Delta = y(1-y)m^2 + lam Q^2(1-(1-y)/x)); both give the stated formula. C_H: my independent covariant derivation, in a different parametric form (r3_ladder_CH.py), agrees with the report's fibered value to 3.1e-16 (eps=0.1), 4.2e-15 (0.2) and 3.4e-13 (0.3). The larger deviations come from the t >= e^-40 cut in CH_fibered: the neglected part is ~e^(-40(1-eps)) = 1.3e-14 and 6.9e-13, contrary to the script comment '< 1e-15'. This is not a mismatch; [P] is honest and C_H is a good candidate for an exact proof.

### [per_result 23]
[X2-Thm5.1] Grade [P] appropriate; gaps g1-g5 are real; (M2) is unaffected by the (M1) IR problem.

### [per_result 24]
[X2-Prop5.4] CORRECT (algebra).

### [per_result 25]
[X2-Thm6.1] The implication is CORRECT, but its (M1) setting is DEFECTIVE and the status list is partly FALSE. (a) Thm 6.1 includes 'integrand-level renormalization of all UV-divergent subgraphs', so at N=2 the triangle with the renormalized phi bubble on the exchanged phi is part of F^(2). Its integrand is ~ ln(k^2)/(k^4 D1 D2) near k = 0, a ln^2 IR divergence at fixed m; in DR the bare and counterterm parts have nu = 2+eps and 2, which violate nu < 2-eps. So (CS3phi) FAILS, F^(2) of (M1) is itself not finite, and the 'to all orders' statement is vacuous for the full form factor at N >= 2 unless restricted. (b) 'VERIFIED: (CS3phi) for Gamma at all orders, for UV-finite graphs' is false (three-loop kite counterexample above). (c) '(F1) for the bubble-chain class' is not about any (M1) graph class (Thm 3.9). (d) POSITIONING: missing are Smirnov-Rakhmetov 1999 and Belitsky-Bork-Smirnov JHEP 05 (2025) 237 [2409.05945]. Also missing is Belitsky-Smirnov PRD 113 (2026) 036022 [2505.22595], on exactly the off-shell scalar integrals of (M1): hard factorization holds to three loops, but ultrasoft-collinear factorization is violated (two-loop O(eps) obstruction z1 = Gamma(1+2eps)/Gamma(1+eps)^2, irreparable at three loops; the c-us region integrals are not products). This bears directly on O1/O10 and on any upgrade of the subtraction theorem to a factorization theorem in off-shell kinematics. Note also that X2's C1S/C2S approximators keep the entangling term 2(P-k1+)k2-.

### [per_result 26]
[X2-Err] (a)-(g) acceptable as labelled; nothing new.

### [per_result 27]
[X2-Err-own] CORRECT.

### [per_result 28]
[X2-Est] CORRECT where re-checked: two-loop NLP, one-loop expansions, c1 and the (M3) series. The bubble-class entry inherits the Thm 3.9 relabelling; the two-loop entries inherit the Thm 4.3 premises (some dischargeable by citation, see above).

### [per_result 29]
[X2-Slots] Consistent with spec_v2/OUTLINE_appMNOPQ.md. X2a is delivered in fibered form [R, R_PT, computer-assisted]; the spec's 'hence thm:appN-subtraction holds for the triangle' holds only as [R, R_cond] (premise (ID)_Gamma), as the report says. X2b, X2c and X2d are correctly not delivered.

### [per_result 30]
[X2-REVISIONS] ACCURATE: every r2_1 and r2_2 required fix is addressed. The bubble archive was produced as requested, but without LP data (see Lem 2.8).

### [per_result 31]
[OPEN ITEMS] O1-O15 are honest, but O3 ('UV subdivergences' at two loops) and O13 ('the full graph beyond the hybrid model') are not open in (M1): those graphs are IR divergent at fixed m, so (CS3phi) fails. O1 and O10 need the Belitsky-Smirnov positioning. O15 is a good suggestion. Citations newly added in round 2 were verified on INSPIRE: Erdogan-Sterman PRD 91 065033; Feige-Schwartz PRD 90 105020; Anastasiou-Sterman JHEP 07 (2019) 056; EGMPR NPB 152 285; Manohar-Stewart PRD 76 074002; Idilbi-Mehen PRD 75 114017; Speer JMP 9 1404; Chang-Yan PRD 7 1147; Ligterink-Bakker PRD 52 5954; Usyukina-Davydychev PLB 298 363 and 305 136; Ma JHEP 05 (2020) 012; Jantzen JHEP 12 (2011) 076.

## required_fixes

### [required_fixes 1]
[PROCESS, blocking] The orchestrator or main session must write verify/extend/X2-subtraction/REPORT.md verbatim from the fix-2 StructuredOutput (journal.jsonl line 122, agent aa54636b3bf3d0143). It must also persist reviews r1_2 (line 70), r1_1 (line 74), r2_2 (line 110), r2_1 (line 115) and this review. Subagents may not write report .md files, so review_r3_1.md was not written; my scripts and logs are in verify/extend/X2-subtraction/review_r3_1_scripts/.

### [required_fixes 2]
[Cor 2.11 / Thm 6.1, (M1) IR finiteness, substantive] (M1) is massless and super-renormalizable. Add an explicit IR-finiteness hypothesis to Cor 2.11, e.g. the soft criterion n_a(S) > V_S(S) for every soft subgraph S, equivalently convergence at all soft corners. Delete the claim for 'every UV-finite graph' of (M1), citing the three-loop counterexample: the triangle with the UV-finite kite self-energy on the exchanged phi has rho >= 0 and int rho = infinity, while its DR value is finite. In Thm 6.1 either restrict the sum over Gamma to an explicitly IR-finite graph class, or change the model. State that the full (M1) F^(N) is IR divergent at fixed m for N >= 2: the renormalized phi self-energy insertion gives int d^4k ln k^2/k^4. Delete 'VERIFIED: (CS3phi) for Gamma at all orders'. Update [X2-Setup], the scope of Thm 2.6, O3 and O13. Cite Jackiw-Templeton, PRD 23 (1981) 2291.

### [required_fixes 3]
[Thm 3.9, substantive] Withdraw the identification of Gamma^(j) = ln^j(D_g/mu^2)/(D_g D1 D2) with the MS-bar-renormalized bubble chain of (M1). In (M1) the j-bubble chain is g^(2j)(c - ln)^j/D_g^(j+1) and is IR divergent. Withdraw also 'the true d-dimensional chain is (-k^2)^(-n eps) times poles' and the renormalon reading for (M1). Relabel the class, e.g. as 'log-weighted triangle family, modelling the large-beta0 chain of a theory with Pi proportional to k^2 (phi^3_6 or gauge theories); not a graph class of (M1)'. Remove '(F1) for the bubble-chain class' from Thm 6.1's (M1) status list, and adjust the summary ('Bubble class [R, R_PT, archived]'), X2-Est and O13.

### [required_fixes 4]
[Positioning / novelty, substantive] Cite Smirnov-Rakhmetov, Theor. Math. Phys. 120 (1999) 870 [hep-ph/9812529]: same diagram, same nine regions, all region integrals, and the LP sum L^4/4 + pi^2 L^2/2 + 7pi^4/60. Cite also Belitsky-Bork-Smirnov, JHEP 05 (2025) 237 [2409.05945] and Belitsky-Smirnov, PRD 113 (2026) 036022 [2505.22595]: same off-shell scalar integrals, region values at one and two loops, and ultrasoft-collinear factorization violation. Place these in Prop 3.1' (its closed forms are the known region values; 'NEW' only for the fibered identification), in Thm 4.3 (reduce 'worked example' novelty to the composite/zero-bin regulator analysis and the NLP coefficient) and in Thm 6.1, O1 and O10. Discuss that for off-shell kinematics the c-us region integrals are non-product, so the subtraction theorem does not extend naively to a factorized form.

### [required_fixes 5]
[Thm 4.3, upgrade] Identify X2's nine singles T_R Gamma with the SR / Belitsky-Smirnov region integrals; I checked T_HS = (us-h) and T_SS = (us-us), and all m^2 exponents. Then use their explicit DR-regulated values to discharge (Reg)(b) for the singles, (F) for int r and premise (iii). State the pole-order <= 4 input behind 'P is a polynomial of degree <= 4'. Give the m^2 values explicitly: 0.04, 0.01, 0.0025, 6.25e-4, 1e-4, 1e-6.

### [required_fixes 6]
[Lemma 2.7, minor] Add the simple-pole / non-degenerate-closing-side hypothesis that the residue-domination step uses. Add, or cite, the step showing that lim_{eta->0} int d^dk F_eta equals the parametric value I_F used in (ID): Feynman parametrization at finite eta, then eta -> 0.

### [required_fixes 7]
[Prop 5.1'(e), minor] The CH_fibered comment 'neglected part O(e^-40(1-eps)) < 1e-15' is false for eps >= 0.2: it is 1.3e-14 at 0.2 and 6.9e-13 at 0.3, and this explains the reported deviations. Move the cut, or correct the comment and the stated precision. Optionally upgrade C_H to an exact identification. An independent covariant form agreeing to 3e-16 at eps=0.1 is: C_H = Gamma(1+eps)Q^(-2-2eps) int_simplex x1[(2eps-2)a^(-eps)/(eps b) + x3 a^(-1-eps)/b - a^(-eps)/(eps b^2)], with a = x3(x1 + x2 c_x) and b = 1 - x2/x.

### [required_fixes 8]
[Certificates, minor] Make the archives self-contained: for every piece, store the LP rows, right-hand sides and objective, or the polynomial supports and comparability data. Then 'computer-assisted [R]' can be re-verified exactly without r1/r2_lptools.py. My consistency audit of the bubble archive passed, but it cannot check optimality.

### [required_fixes 9]
[Wording, minor] Prop 3.1: the absolute integrals of the C_R parts are given by J0+J1-type Beta integrals, not by 'the closed form of Prop 3.1''. Prop 3.14(c): say the symmetric deformation is local to the Glauber region (Im G = 2 delta(k+ + k-)).
