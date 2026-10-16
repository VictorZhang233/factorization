# Final independent review of X1-glauber_final.md

(persisted verbatim from workflow wf_4e25ac9b-92f; overall verdict: **fixable_issues**)

## Per-result verdicts

### [1]
STATUS. The file verify/extend_reports/X1-glauber_final.md (1860 lines) has the same content as the backup text in the task. Every final-round script and log it cites exists (verify/extend/X1-glauber/final_scripts/, final_logs/), and the logs contain the quoted numbers. My independent checks are in verify/extend/X1-glauber/final_review_scripts/, with logs in final_review_logs/: fr_p5_lipatov, fr_l4_colour, fr_t3e_vK, fr_t2_A4, fr_endpole_L6, fr_t2_constants_arith. VERDICT: the mathematical core (L1, L1', L3, L5, L6, L8, T2(a), P2(b), P4(b), T3(b)) is correct, and every rev3-1/rev3-2 required fix was applied. What remains: (i) a new error introduced by the P5 fix; (ii) a missing pointwise/integrated qualifier in ERR-S1b; (iii) grade-system inconsistencies with WRITER_SPEC_v2; (iv) informal hypotheses in several [R] items other than T2; (v) two inequalities in the T3(e) proof that are only sampled numerically, not proved; (vi) minor numeric and wording slips.

### [2]
DEFS D1-D8: correct. Checks: alpha_1 = (2 s_T.k_2T - k_2T^2)/(2 x_s P^+) re-derived; the class-X example bounds re-derived. The L1' Lorentzian weights u_z = K^2/(z^2+K^2) and u_+- = z/(2(z -+ iK)) were re-derived by partial fractions, with sum 1. The scalar-model sector form is consistent with rho_12 = a1a2/((a1-2 d10 k)(a2-2 alpha1 k)). The D3 status is honest: (ADJ) and (REAL) are argued, not proved; the LCOPT argument for (ADJ) with good-component couplings is sound. The paraphrase of asm:appO-mixing(c) in §1.2 matches ASSUMPTIONS.md §3.4.

### [3]
L1 [R]: correct; Steps 1-5 re-derived. Step 1: Weinberg count of d+1 decaying factors on a d-dimensional subspace. Step 2: sector selection, residues -i r_e (final) and +i r_e (initial). Step 3: telescoping bound N 2^N, multi-state terms 2^{N+1}, prefactor identity prod(-r_e/z_e) prod z/prod K. Step 4: closed-quadrant lemma via Re(z_i conj z_j) >= 0. Minor slip: in the quoted round-2 counterexample z = (1-0.01i, -0.99-0.01i), Sum_sigma |w_sigma| = (|z1|+|z2|)/|z1+z2| = 89.0. The quoted 44.7 is max|w_sigma|, the factor that enters the corrected bound 160 in fix_r2_logs/l1_bound_quadrant.log.

### [4]
L1' [R]: correct (multilinearity; Sum_p(-rho/p) = R_e(0); closed-quadrant placement on the theta-contour for theta in [0, pi/2]). c_U = 1.64853 reproduced. It is a numerical supremum of an explicit one-dimensional function. A provable crude bound exists: |u_+-| <= 1/sqrt2 and |u_z| <= 1 give c_U <= 1+sqrt2.

### [5]
L2, L3, L7: correct. L3 mixed-quadrant prefactor: (i r1)(-i r2) = 1/(4k1^+k2^+), giving F_A^[12](-k,k) = -J^(1V2)/(4k^2). The half-plane holomorphy agrees with L5. L7 is now correctly a pre-integration lemma, with (a') as the honest replacement for asm:appO-mixing(a).

### [6]
L5 [R]: correct; Step 1 re-derived. A zero of a J_B initial factor needs e^{it}X in the second quadrant; a zero of a final factor needs the fourth quadrant on N_B and the third off N_B. The swept set covers the first and third quadrants, so N_B is necessary and sufficient. F_A gap factors have Im >= eta. Weakening the hypotheses to (SEC) + N_B is correct (§16 item 43).

### [7]
L6 [R]: correct. Re-derived, and checked numerically on the scalar rho_12 (fr_endpole_L6.log). Base set: integral = -1.5707963268 = -pi/2. Apole set, with an axis pole: +0.0108144325 = -pi/2 - pi Res/k_p.

### [8]
L8 [R]: correct; (a)-(h) re-derived. Generic constant: 384 sqrt(17/16) = 395.8 <= 400. Axis band, with the corrected 25/9 piece: total 4/3 + 25/9 + 25/9 + 1.13 = 8.02 <= 9. (e): only the FF single-state UHP poles contribute, multi-state gaps have zero residue sum, and the rotation sweeps quadrants 1 and 3 while the poles sit in quadrants 2 and 4 on N. (g): 4M^flat l^2 per sector (12 for f_pi); 3200; strip 256/3 <= 86; 2*3200 + 2*86 = 6572 <= 6600. The inequality Int_X^inf ln(1+cR) R^-2 dR <= (1+ln(1+cX))/X was verified: the extra term c ln(1+1/(cX)) <= 1/X.

### [9]
L4 [R, R_def]: correct. Independent implementation (fr_l4_colour.log; Gell-Mann basis, random complex psi). (d1) holds to 1e-16, with K_i = 1 for A-rem = qbar and 1/2 for a diquark. The four quoted norms 0.4330, 0.2165, 0.3536, 0.7071 are reproduced and are identical for every (i, j1, j2); each DY singlet space is 2-dimensional. (d2): the sign pattern s_a s_b s_c = -1 holds for every nonzero f^{abc}. (b): the X1X2 coefficient c1c2(1 - W21 - W12*) = 2i c1c2 Im W12 re-derived. The CdFR precision fix was applied.

### [10]
T1 [R, R_cond: lcopt]: correct as a re-derivation, with the error route for multi-pole factors. §13 overstates it as 'not needed (T1, unconditionally)': T1 is R_cond and its integrated form needs asm:appO-envelope.

### [11]
P1 [R, R_cond: lcopt]: correct. (b) re-derived: E(l) <= 2E^(0)(l) + Delta_l^2/l^+; a state contains one segment per line of J_A^0 and at most n_A SS-carrying lines; E_cut is bounded the same way. The F8 fix (x_min is a momentum fraction) was applied. Weakening the planned [R, R_PT] to R_cond is justified.

### [12]
T2(a) model theorem: correct; Steps 0-8 re-derived and the arithmetic checked (fr_t2_constants_arith.log). V_S is purely imaginary. L6 gives -pi/2 per mixed sector, so Re p_out = -1/2 + O(E8). The E1-E8 coefficients follow from L8(g): 24/pi^2, 825/pi^2, 1600/pi^2, 43/pi^2, 16/pi^2, 4/pi, and E5 via eps(1+2L)^2 <= 11.12 eps^{1/2}. delta_Y = 2E1+2E2+2E3+E4; C_N contains 3243 and C_E contains 1667; 2E2 = 167.2 m^flat_B eps^{1/2}(1+L_B). The |V_S| and |p_out| bounds, C_X1 and C_X0 are right. The imaginary parts -(i/pi) ln(K/(4 lambda_B)) - (i/pi) ln(kappa'/K) add to -L/pi - (1/pi) ln(a_min/(8a)). sup over eps of eps^{1/2}(1+L_B)^2 equals (1+l_B)^2/4 <= 3 + l_B^2. Int|g| <= 4M^flat(1+l_B) holds for lambda/mu >= 1. (A4) tested on 3000 random multi-state jets: maximum ratio 0.04 (fr_t2_A4.log). (ADJ) is correctly needed only for J_B: it controls the strip and axis-band tails of f_pi. NOTES: (1) the constants also depend on ln(a_max/a_min) (through C_IX and R_out), and on n_bar_A (lambda_A/mu_A)^2 through c_rho. (2) C_I still contains E_tot inside C_IX. (3) With all jet constants m = 1, C_N is about 500, so hypothesis (v) needs eps <~ 1e-11. The numerical tests run at eps = 1e-3 to 1e-5, so they probe the statement, not the proven bound. (4) The numerics summary slightly misquotes review_r3_1_logs/t2_general.log: over two decades Re p_opp falls like eps^0.63 (pair 2), eps^0.70 (pair 1), eps^0.73 (pair 0) and eps^0.78 (base); the first-decade Im slopes are 0.680, 0.696, 0.717. The physical reading is correctly restricted to uncut lines, conditional on asm:appO-collinear-ends and OPEN-13.

### [13]
T2(b), T3 transfer [R, R_cond with proposed premises †]: the implication is correct. Content grade [P] is honest. The items cannot be printed as R_cond until the † entries are registered; A.4 says so.

### [14]
T2' (a) [R]: proof structure correct. L5 holds with class X. L6 applies to rho~ = rho_12 chi_+(k) chi_-(-k), and the axis-pole residues are suppressed by (K_c lambda_A/a)^2. The AM-GM step lambda_A K/a <= (eps + K_c lambda_A/a)/2 holds with K = (lambda_B K_c)^{1/2}. The observed rates 0.103, 0.054, 0.028 match lambda^{1/2}. However the hypotheses are informal ('<<', 'up to logarithms'). There is also a constant slip: |chi1 chi2 - 1| <= 3R/K_c given |chi| <= 2, not 2R/K_c. (b) [R]: residue formula re-derived, -a1 alpha1/(a1 alpha1 + a2|d10|). Predictions recomputed from the parameters in scripts/twoexch_rotated_fast.py (fr_endpole_L6.log): apole 0.2517 (alpha1 = 1.35 > 0; alpha0 = 0.5625 is correctly irrelevant), alt 0.0483 (mirror formula, B alpha2 = 0.518 > 0), base 0. These match the quoted numerics. The F9 mirror restatement was applied. (c) [P]: consistent with P2.

### [15]
P2: correct. (b) re-derived: w12 = 1/2 + i delta from the three-sector identity J^[12]_eik = J 2pi delta(q1+q2) i/(q1+i0); p_opp = 1/2 + 2 delta_A delta_B; delta^(p) = -delta^(k+). Sharp-window delta = ln(min(K2,K1')/min(K1,K2'))/(2pi) re-derived. The F7 orientation fix was applied, with an exact check (final_logs/p2_orientation.log: 97/105, 43/455, 1/2, 7/72).

### [16]
P3 [R, R_PT] at O(g^4): correct (graph-by-graph Cutkosky; at O(g^4) the crossed box has no s-channel cut and three-particle cuts would need a forbidden on-shell emission). The three-line remark is correctly marked as uncertified (OPEN-9).

### [17]
P4: (a) and (b) correct. rho_2 re-derived from the n1=2, n2=1 term: c_t(2ik) = 2 s c~_2 k. It is holomorphic in Re k > 0 and has fixed sign -sgn(c~_2/J_A) on k > 0, so delta W(12,21) is purely imaginary and nonzero whenever c~_2 != 0. The F2 fix was applied correctly: the class imposes (ADJ) on J_B only, and the effect of the 12V partner is power-level (difference -1.8e-5 - 6.95e-5 i at lambda = 0.01 in review_r3_1_logs/t2_general.log). delta p_opp is purely imaginary because the 1V2 perturbation does not touch the 2V1 sector. (c) [P] honest; the all-initial sector selection is correctly labelled observed, not proved.

### [18]
T3: (a) and (g) [R, R_def] correct. (b) correct: f_B(-kappa) = e^{2i phi} conj(f_B(kappa)) with v real and odd gives an imaginary integral; f_B is S-type through (ADJ) for adjacent insertions on different partons. (c) correct. (e): proof structure re-derived. The L1' closed quadrants on the pi/4 rays and |e_K| <= 32 c_U^2 m_A lambda_A max(1/K, 2R/a_min) follow from N 2^{N+1} = 16 and Sum|w| <= 2. The splits at X_K = a_min/(16K) and at a_min/(2K) are right, and the F5 boost-invariance correction is right. GAPS: step (3) asserts |v_K| <= (|x1|+|x2|)/4 for |x_e| <= 1/4 and |v_K| <= 1/2 without proof. My sampling (fr_t3e_vK.log, 2e5 points) gives suprema of exactly 0.250000 and 0.500000, so the inequalities are sharp but only numerical. My one-dimensional PV representation of v_K agrees with the pole sum to 4e-8 and could support a proof. The hypotheses 'of the type (iv), (v) of T2' and 'lambda_A << K << a/lambda_B' are informal. The (d), (e') and (f) numbers match final_logs/t3f_recompute.log, and the colour note (the model's own colour factor vanishes) is correct.

### [19]
P5 [A]: the identity D_C = Int dPhi3 [A_A^dag A_B + h.c.] is correct. Every cut rung joins A to B; cuts with a non-interacting line on one side are kinematically forbidden for on-shell massive or time-like lines. ERROR introduced by the round-3 fix: (ii) claims a 'common factor 1/q_T^2', but radiation from A carries the exchange propagator 1/q2^2 (transfer to B) and radiation from B carries 1/q1^2, with q1 + q2 = k. So (iii)'s 'k.(J_A+J_B) = 1 - 1 = 0, |A_A+A_B|^2 gauge invariant' is false in general. Verified in fr_p5_lipatov.log: the line-part current violation reaches 99%, and |L_A+L_B|^2 differs between Feynman and light-cone gauge by factors up to 3.9e3. Adding the three-gluon term with a fixed relative sign of -1 conserves the current to 3e-15 and makes |J|^2 gauge independent to 1e-11. (iii) therefore contradicts P5's own conclusion that the three-gluon term is needed. Feynman-gauge positivity survives: interference = 2 C^dag C (vA.vB)^3/((vA.k)(vB.k) q1^2 q2^2) > 0. The conclusions D_C != 0 and D_C gauge dependent stand. final_scripts/p5_interference.py builds in equal normalization, so its gauge-invariance check is circular.

### [20]
Remark P6 and Remark C: appropriately ungraded. Remark C(ii) is plausible. I re-derived the delta(p1) part: i/k1^- x 1/(2k1^+) at k1^- = a1/(2k1^+) gives i/a1, which is finite, so the estimate O(N0) at the B-collinear end follows. OPEN-13 is honest.

### [21]
CMP §10: the F10 (Zhou et al.) fixes were applied: the Sec. VI caveat, the n_f^- sector, and 'our own assessment'. 'DGOPS step 3/step 6' refers to DGOPS's own six-step list (verified by rev2-2), not to the report's items 1-4. Say so.

### [22]
TMD [C]: appropriate; the Chang-Li/Li assessment is fair and honest about the perturbative scope.

### [23]
ERR-S1b: the quotations are verbatim in refdoc/refdoc.txt (Rem E.32 tail about lines 11801-11816, the E.33 status paragraph at 11862, Rem E.49(2) at 13014). The reframing was applied correctly: the reference already names the near-shell mechanism, and its error is the expectation that this mechanism is insufficient. REMAINING: the 'What stays' bullet and T2 'Relation to the reference' say the reference is 'contradicted for the uncut-line part' without the pointwise qualifier. Off N_A the unregulated uncut side sum leaves the end-pole term of T2'(b) (0.2517 for apole). The spectator-integrated statement, which is what the reference's remark concerns, is therefore not established; it is OPEN-2. Separately, the status '[R, R_cond]' has no premise list and does not match T2(a)'s grade.

### [24]
REG §2/§13: the recast follows the §6 precedents and is acceptable. (ADJ) and (REAL) are class definitions for the mathematical statements, proposed as asm:appO-adjacent-swap/real-jets (tag P) for the QCD transfer; M_glob is a model definition; N_X is a domain definition. 'G5(ii) argued [A]' was applied. ISSUES: (1) asm:appO-collinear-ends lacks the 被使用于 and 解除途径 fields, and its relation to thm:appO-main/thm:dy-factorization is unstated. (2) The fully coincident §13 bullet does not separate the proven k^+-only result (T2'(a)) from the two-sided numerics [P] (T2'(c)). (3) Grade system: [R, R_PT] is applied to pure-mathematics lemmas and model theorems, against WRITER_SPEC §4.1 and §4.3, and §18 and A.4 disagree.

### [25]
EX/LIT: the quoted log numbers match the logs. final_scripts/t2_constants.py part (2) re-tabulates earlier logged values without saying so; they match logs/twoexch_rotated_fast2.log, logs/twoexch_exact2_0.003_base.log and review_r3_1_logs/t2_general.log. Novelty claims are restricted and honest, with no markers before OPEN-8. Lindsay 1984 and BFT 1989 are correctly cited as prior art (INSPIRE abstracts in r3_inspire_refs.log). Barcaro et al. confirmed on INSPIRE: 'Collinear Factorization Violation and Reggeization', DESY-26-091, SLAC-PUB-260713. No log of that check is stored.

### [26]
REQUIRED-FIX AUDIT. rev3-1: F1 applied (§0.3, §1.2, T2 reading, T2'(c), T3(j), Remark C, §12, §13, OPEN-13). F2, F3, F4 (hypothesis (v), explicit C_N/C_T/C_I, Im part weakened to O(1)), F5, F7, F8, F9, F10, F11 and F12 applied. F6 applied for registration/recast and 'argued [A]', but the qualifier choice conflicts with WRITER_SPEC (see fixes). F13 was handled by the parent through extend_reports/. rev3-2: items 2-10 and 12 applied. Item 11 is partly applied: T2, T3 and P4 are graded as [R, R_PT] model theorems plus a transfer item with unregistered † premises, not as R_cond with registered premises. This is defensible but undeclared. The P5 fix (F3/item 3) introduced a new inaccuracy (common propagator, gauge invariance).

## Required fixes (binding for the appendix writer)

### Fix 1
P5 (§9 (ii), (iii), Verification bullet 1, §14.5, §16 item 31). (a) Replace 'the common factor 1/q_T^2'. Radiation from line A carries the exchange propagator 1/q2^2 and radiation from line B carries 1/q1^2, with q1 + q2 = k, v_A.q1 = 0 and v_B.q2 = 0. (b) Delete the claim that |A_A+A_B|^2 is gauge invariant because k.(J_A+J_B) = 0. In fact k.(A_A+A_B) is proportional to C (vA.vB)(1/q2^2 - 1/q1^2), which is nonzero. Current conservation and gauge independence need the three-gluon-vertex (central Lipatov) term; the line parts alone suffice only in the limit q1^2 = q2^2 (|k_T| << |q_T|). (c) Keep the positivity statement in the form 2 C^dag C (vA.vB)^3/((vA.k)(vB.k) q1^2 q2^2) > 0, and state the comparison with Int|A_A+A_B|^2 in Feynman gauge. (d) Replace the circular check in final_scripts/p5_interference.py, which assumes equal normalization, by one that includes the propagators and the three-gluon term, as in final_review_scripts/fr_p5_lipatov.py. Conclusions and grade [A] are unchanged.

### Fix 2
ERR-S1b (§12 'What stays', T2 'Relation to the reference', §0.2 row). Qualify 'contradicted for the uncut-line part' as: pointwise on N_A ∩ N_B in the unregulated M_glob, or on N_B with the in-window class-X k^+ regulator (T2'(a)). Add that off N_A the unregulated uncut side sum keeps the nonzero end-pole term of T2'(b) (e.g. Re p_opp -> 0.2517 for the apole set). The spectator-integrated statement, which the reference's remark concerns, therefore holds only under asm:appO-collinear-ends, and only where at least one NF holds; the rest is OPEN-2. Replace the status '[R, R_cond]', which has no premise list, by 'T2(a) (model, pointwise) + [P] (T2'(c))', or list the premises.

### Fix 3
Grade system (WRITER_SPEC_v2 §4.1, §4.3; rev3-1 F6, last clause; rev3-2 item 11). (a) Drop the self-declared rule '[R, R_PT] = pure mathematics about defined classes'. Pure mathematics carries no tag, and the outline itself marks lem:appO-equal-time, lem:appO-cut-position and lem:appO-carrier as (数学). Mark L6, L2 and the abstract-class lemmas L5 and L8 as (数学). Keep [R, R_PT] for statements about LCOPT jet factors or Feynman integrals (L1 as the revision of lem:appO-joint-localization, L1', L3, L7, P3). (b) Model theorems T2(a), T2'(a),(b), T3(b),(c),(e), P4(a),(b): §0.2/§18 print [R, R_PT] (model), while A.4 says both 'print grades as in §18' and 'print [P] for model theorems'. Choose one convention and apply it in §0.2, §18, A.2 and A.4: either slot X1f's planned '[R, R_PT] (at O(g^4), in M_glob; first sentence states it)' or §4.3 item 4's [P]. (c) Make §0.2's T3(a) [R, R_def], as in the body and §18. (d) Record the departure from rev3-2 item 11: the transfer items have unregistered † premises and stay PENDING-VERIFY.

### Fix 4
Explicit hypotheses in the remaining [R] items, as round 3 required for T2. T2'(a) ('lambda_B << K_c << a/lambda_A', 'up to logarithms'), T2'(b) ('+O(power)'), T3(b),(e) ('smallness conditions of the type (iv), (v)', 'lambda_A << K << a/lambda_B') and P4(a),(b) ('o(1)') need explicit conditions and logarithmic factors. For example, for T3(e): K >= 2 lambda_A, a_min/(16K) >= 4 lambda_B, eps <= eps_0, and |N(K)/N_0 - 1| <= 1/2 with its explicit bound. For T2'(a): 4 lambda_B <= (lambda_B K_c)^{1/2} <= K_c <= a_min/(2 lambda_A) and the analogue of (v). Otherwise present these items as asymptotic statements with proof sketches. Also correct |chi1 chi2 - 1| <= 2R/K_c to 3R/K_c (given |chi| <= 2).

### Fix 5
T3(e) proof, step (3). The inequalities |v_K| <= (|x1|+|x2|)/4 for |x_e| <= 1/4 and |v_K| <= 1/2 are stated without proof and are only sampled numerically. Both are sharp: the suprema are exactly 0.25 and 0.5, so there is no slack. Prove them, for example from the explicit pole sum or from the one-dimensional representation v_K = (i/2pi) PV Int rho1(k) rho2(-k) dk/k with rho_e(k) = z_e K^2/((z_e - k)(k^2+K^2)). Alternatively use provable substitutes: |v_K| <= c_U^2 + 1/2 (race weights have modulus <= 1 in closed quadrants) and an analytic O(|x|) bound near x = 0; only C_e changes. Likewise c_U = 1.6485 is a numerical supremum; quote the analytic bound c_U <= 1 + sqrt2 or derive the maximum.

### Fix 6
Register and §13 consistency. (a) The fully coincident bullet 'not needed, given asm:appO-collinear-ends ... (T2'(a),(c))' should say, like the half-coincident bullet, that it is proved with the class-X k^+ regulator alone (T2'(a)). The two-sided version is numerics [P] for one jet pair (T2'(c): Lorentzian regulators, jet A localized). (b) Give asm:appO-collinear-ends its 被使用于 and 解除途径 fields. State that it is not proposed as a premise of thm:appO-main or thm:dy-factorization, which keep asm:appO-mixing(c) with tag A. If it replaced mixing(c) and were tagged P, grade propagation (§4.6) would lower thm:dy-factorization to [P], contradicting 'thm:dy-factorization stays [A]'. (c) Drop 'unconditionally' from the T1 bullet of §13.

### Fix 7
Minor accuracy and disclosure. (a) T2(a): the constants are polynomials also in ln(a_max/a_min), and C_E depends on n_bar_A (lambda_A/mu_A)^2 through c_rho; say so. Replace E_tot inside C_IX by C_E(3 + l_B^2) when forming C_I. Write out the derivation of c_rho in (A4); a random test gives maximum ratio 0.04. Add one sentence that with the proven constants (m's = 1, C_N about 500) hypothesis (v) needs eps <~ 1e-11. (b) Correct the T2 numerics for non-factorized pairs to the decay exponents 0.63, 0.70, 0.73 and the first-decade Im slopes 0.680-0.717 (review_r3_1_logs/t2_general.log). (c) L1 verification: in the round-2 counterexample Sum|w| = 89.0; the quoted 44.7 is max|w_sigma|. (d) §10: say that 'DGOPS step 3/step 6' refers to DGOPS's own step list. (e) Disclose that final_scripts/t2_constants.py part (2) re-tabulates logged values, and store a log of the Barcaro et al. INSPIRE check (DESY-26-091, SLAC-PUB-260713; confirmed).
