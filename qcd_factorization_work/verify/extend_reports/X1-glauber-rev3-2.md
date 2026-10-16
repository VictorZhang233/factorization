# X1-glauber-rev3-2

(extracted verbatim from the workflow journal; structured output of the agent)

## overall

fixable_issues

## per_result

### [per_result 1]
运行状态（回答“在正常运行吗”）：工作流在运行，但不完全正常。按 journal（wf_52f29317-58b/journal.jsonl），X1 和 X2 都在最后一轮（第 3 轮）审稿（第 123–127 行），X3 在第二轮修订（第 121 行）。仍未解决的问题是结果没有存盘：(1) verify/extend/X1-glauber/REPORT.md 从来不在盘上。按作者在第 42 行的自述，harness 拒绝了它写报告文件。review_r1_1.md、review_r1_2.md、review_r2_2.md 也不存在，X2、X3 同样没有 REPORT.md。(2) 所以本审稿审阅的是 X1-glauber-fix2（agent aff8996e9d3974c62）的结构化输出，即 journal 第 125 行：results[0..26] 加 open O1–O12。(3) 按“子代理不写报告类 .md 文件”的规则，我没有写 review_r3_2.md。本结构化输出就是审稿意见，需要父会话存盘。(4) 脚本在 round === 3 之后直接 break，X1 不会再有修订轮。下面 required_fixes 中的各项只能在修补 spec 时由父会话处理。我的独立检查脚本和日志在 /Users/hao-cheng/Desktop/theorem proof/qcd_factorization_work/verify/extend/X1-glauber/review_r3_2_scripts/ 及其 logs/ 子目录。总评：数学主体（L1/L1′/L8/T2/T2′/P2/T3(e)/P4）经独立推导和独立代码验证是正确的。剩下的是若干可修复的错误或缺口：P4(b) 中关于 (Sp′) 的一句说法错误；P5 的缺陷恒等式写错；T2 少一个小量条件；REG 误读了登记规则；ERR-S1b 的表述需要修正。

### [per_result 2]
DEFS — CORRECT, with one register problem (see REG). I re-derived alpha_1 = (2 s_T.k_2T - k_2T^2)/(2 x_s P^+). I checked the class-X example: in the closed quadrant, |chi-1| <= |k|/K_c and |chi| <= K_c/|k|, because |1+k/K_c| >= max(1, |k|/K_c) for Re k >= 0. (Sp') is plausible for LCOPT time-ordered graphs: swapping two adjacent special vertices with no internal vertex between them gives another LCOPT graph with the same other intermediate states. At leading power the good-component couplings are equal. (Sp') is exact in the scalar model, and my independent jet generator implements it.

### [per_result 3]
L1 [R] — CORRECT as corrected. (b1) The closed-quadrant lemma is proved correctly: pairwise Re(z_i conj z_j) >= 0 in a cone of opening pi/2, so |sum z|^2 >= sum|z|^2 >= |z_m|^2. Independent test (r3_quadrant_P2.py): 20000 random groups with both cone edges occupied give max|w| = 0.9999992. The condition is sharp: for opening pi/2+0.3, z = (1, 0.3 e^{i(pi/2+0.3)}) gives |w| = 1.047. (b2) holds: a same-ray (Glauber) group gives sum|w| = 1 exactly. The novelty restriction is accurate.

### [per_result 4]
L1' [R] — CORRECT. The corrected bound carries sum_sigma|w_sigma(p)|. I re-derived the Lorentzian weights u_z = K^2/(z^2+K^2), u_+ = z/(2(z-iK)), u_- = z/(2(z+iK)) by partial fractions. The sum rule holds to 3e-16, and c_U = 1.6485 is reproduced (r3_T3e_constants.log).

### [per_result 5]
L2 [R] — CORRECT (unchanged). I re-derived the (+,+) weight z1/(z1+z2) = a1 k2/(a1 k2 + a2 k1) by closing the k^- contour on the eikonal J_A^[12] = Jcal 2pi delta(k1+k2) i/(k1+i0) times the two gluon factors.

### [per_result 6]
T1 — CORRECT as a re-derivation of Props E.35/E.31(iii). The round-2 error-route note (line-by-line E.28(iii) for commuting insertions, instead of L1'(b)) is legitimate.

### [per_result 7]
P1 [R_cond] — CORRECT as revised. The x_min >= c hypothesis, the endpoint region assigned to E.44(c), the use of E.19(a) and cut-independence are all stated. The price, an enlarged G6(c), is stated honestly.

### [per_result 8]
L3 [R] — CORRECT (unchanged).

### [per_result 9]
L4 [R] — CORRECT. (b): with c_e real, the coefficient of X1X2 is c1c2(1 - W21 - W12*) = 2i c1c2 Im W12, and that of X2X1 is its negative (re-derived). (d1): I re-derived f^{abc}T^a_j1 T^b_j2 (T^c_j1 + T^c_j2) = 0; the two terms are -/+ (iC_A/2) T_j1.T_j2. (d3) scope is now right. CONTEXT verified in arXiv:1112.4405: eqs. (186)-(190) give Delta^(2) proportional to f_abc T1 T2 T3, vanishing for n = 4 by colour conservation and first contributing at n = 5.

### [per_result 10]
L5 [R] — CORRECT; the proof is now complete. Checked: (1) the radial (Euler) identity and kappa.n = 0 on the half-axes. (2) The arcs, after the R^2 measure: generic R^-3, strip R^-2 ln R, axis bands lambda R^-2, all better than the stated R^-1 ln R. (3) At fixed eta > 0 no gap factor vanishes for any t in [0, pi/2], since that would need y > 0 and y < 0 at once. The bounds are therefore uniform in t, with eta-dependent constants. (4) The eta -> 0 bound |A + i(eta-y)| >= <y>/sqrt5 for eta <= mu, by the case split |y| <= 2mu versus |y| > 2mu.

### [per_result 11]
L6 [R] — CORRECT (unchanged; Cauchy's theorem with [rho - (1+k)^-1]/k).

### [per_result 12]
L8 [R] (NEW) — CORRECT, independently re-derived and tested. Re-derived: (a), and the pi/4 inequality |A+K| >= max(|A|,|y|)/sqrt2, which reduces to (t - 1/sqrt2)^2 >= 0. The eikonal sector sum -1/(p1P) + 1/(p1p2) - 1/(Pp2) = 0. The strip algebra: BB minus g/kappa2 = phi2 i(P+A)/((A+p1)p2), the FF remainder is iA'/((A'-p2)p2), and (-Jcal_BB + Jcal_BF)/(p1p2) cancels by (Sp). (e): the integral of g dP/2pi equals Jcal from the UHP poles of the FF gaps, since multi-state gaps have zero residue sum. The counterclockwise rotation sweeps the 1st and 3rd quadrants while the poles sit in the 2nd and 4th under NF, giving -i Jcal. (f): orientation d^2p = -d^2kappa. Independent numerics (r3_L8_check.py) use my own jet generator: set-dependent gap functions with unit single-state coefficients and random 2- and 3-state terms, mu/lambda from 1e-3 to 0.6, 200 jets x 300 points. Max lhs/bound: (b) 0.357, generic 384M 0.044, axis band 9Mflat 0.065, (c) 400Mflat 0.0083, (d) 16Mflat 0.033, (e) 0.216. int g/2pi = -1.000000i and int S/(2pi)^2 = -1.00000 to -1.00002 for 5 jets. Minor arithmetic slip in (c), axis band: the multi-state second-gap pieces of BB and BF sum to at most (16/9 + 1) = 2.78 Mflat lambda/(R^2<r1>), not 2. The final constant 9 still holds (total about 8.2).

### [per_result 13]
T2 [R_cond, model] — CORRECT as a model theorem, with three small hypothesis/explicitness gaps. I re-derived Steps 0-7: the normalization; the S/T/O partition; T_+ lies in (-,+) with the exact sector 1V2; the main term -(i/2pi) int_K^inf rho12 dkappa/kappa. The asymmetric strip in (kappa_P, kappa_2) coordinates, kappa_P in (-kappa2/3, kappa2/4), is covered by P6 (tail |U| > kappa2/4) and P7 (sliver). The E1-E8 constants agree with L8(g): 24/pi^2; 825/pi^2 = 6600/8 divided by pi^2; 1600/pi^2; 43/pi^2 = 2x86/(4pi^2); 16/pi^2; 4/pi. L6 gives exactly -pi/2 per mixed sector. The v-term is purely imaginary (v real and odd, the square symmetric, D(-kappa) = conj D(kappa)), and the (1+L) factor is right. GAPS: (i) the last step needs delta_Y <= 1/2, i.e. C_N eps^{1/2}(1+L_B)^2 <= 1/2. This is NOT implied by eps <= eps_0 = min(1/16, a_min^2/(4a1a2)): 2E2 alone is about 167 mflat_B eps^{1/2}(1+L_B). (ii) C_T needs the constant C_c in |X| <= |Re X| + L/pi + C_c, but Step 7 gives only +O(1). It can be bounded with L8 (int|g| <= C Mflat(1+ln(lambda_B/mu_B)); the R <= 4lambda_B part <= 12 Mflat ln^2(1+16lambda_B/mu_B)), so C_T also depends on ln(lambda_B/mu_B). (iii) 'Im p_opp = -(1/pi)ln(1/eps) + c + O(eps^{1/2}...)' asserts convergence of the O(1) remainders to a constant at that rate without derivation. It is true for fixed jet shapes as a grows, by the same tail estimates; state that scaling and derive the rate, or weaken to +O(1). Prior art: the restriction to Lindsay 1984 and BFT 1989 is now right. Their INSPIRE abstracts confirm meson+meson and a two-'meson' eikonal model, whereas LRS treat quark + hadron.

### [per_result 14]
T2' — (a) CORRECT. The stated rate follows from O(lambda_B/K + K/K_c + lambda_A K/a + (K_c lambda_A/a)^2) with K = (lambda_B K_c)^{1/2}; it is a mild over-estimate of the last two terms. rho~ = rho chi_+(k) chi_-(-k) is holomorphic in the first quadrant (chi_- continues into the third quadrant) and real on k > 0, and the pole residues are multiplied by O((K_c lambda_A/a)^2). (b) CORRECT, but the clause 'jet B's poles give the same by symmetry' can only mean the mirror statement under NF_A (k^- rotation), because L5 needs NF_B; dropping NF on both jets is O2. (c) [P] is consistent with P2(b). Remark: G7 for the half-coincident family is proved only with the k^- regulator alone (T3(e)). Adding the class-X k^+ factor should change W12 by O(a/(K^+K^-)) by the same estimates. This is not certified; it deserves one sentence.

### [per_result 15]
P2 [R] — CORRECT, independently verified (r3_quadrant_P2.py). w12 = 1/2 + i delta, with delta the PV integral, follows from J^[12]_eik = Jcal 2pi delta(k1+k2) i/(k1+i0). The sharp-window formula delta = ln(min(K2,K1')/min(K1,K2'))/(2pi) matches direct PV integrals on 4 window sets. The identity p_opp = 1/2 + 2 delta_A delta_B holds with the W(12,21)+W(21,12) convention. The 97/105 example for (1,3;4,1/2) is reproduced three ways: exact UHP residues (poles i/2 and i); the L1' regulator-pole race (u_init = K2/(K1+K2), u_fin = K1/(K1+K2); race weights 4/5, 1, 0, 6/7); and the PV integral 0.9238094.

### [per_result 16]
P3 — CORRECT (unchanged).

### [per_result 17]
T3 — CORRECT as restated, and (e) is now a genuine proposition. Verified independently (r3_T3e_constants.py, 2x10^5 random points on the pi/4 rays): c_U = 1.6485; sup|v_K| = 0.5000; sup |v_K|/(|x1|+|x2|) for |x_e| <= 1/4 is 0.2500; |v_K - (x1-x2)/4| <= 0.0441(|x1|+|x2|)^2; |v_K| <= min(1/2, 8KR/a_min) with max ratio 1.0000. The strict-Glauber limit gives v_K -> 0 and the gluon-pole limit gives the race weight. The closed-quadrant placement of {z_e, -iK} and {z_e, +iK} on the pi/4 rays is right. The interpretive sentence 'not determined by the integrand on any window |k^-| <= K' says more than the proven bound: the Lorentzian changes the in-window integrand by a relative O(k^2/K^2), not by zero. (d)'s colour note (the model's own DY colour factor vanishes) is correct.

### [per_result 18]
P4 [R_cond] — (a) and (c) CORRECT; the result of (b) is CORRECT, but one stated reason is FALSE. The added term s c2 [i/(A1+k1)][i/(A2+k1)][i/(A'-k2)] in sector 1V2 DOES have a single-state gap: the final gap between V_H and insertion 2. So 'leaves ... (Sp') (no single-state gap) unchanged' is false if (Sp') is imposed on J_A. (Sp') for the adjacent pair (V_H, 2) would require a partner s c2 [i/(A1+k1)][i/(A2+k1)][i/(B+k1+k2)] in sector 12V. This is harmless for T2, whose hypotheses impose (Sp') on J_B only. Adding the partner changes W(12,21) only by O(lambda_A K/a + lambda_B/K): BB never reaches the strip, in S it is a multi-state localization error, and in O it is bounded like E3. The J_B perturbation of (c) has only two-state gaps and does preserve (Sp'). The numbers match fix_r2_logs/p4_regulated_B.log: -0.028724i (G7), and -0.030829i against the predicted -0.030858i (unregulated); BB-sector shifts are <= 1e-5.

### [per_result 19]
P5 [A] — the conclusion is ACCEPTABLE, but the round-2 identity is WRONG as stated. A three-particle cut of a class-C graph cuts a rung whose two ends lie on line A on one side and line B on the other. Class C therefore yields only the interference int dPhi3 [(A_A)^dag A_B + h.c.], not int dPhi3 (A^lines)^dag A^lines. The self terms, where the gluon is emitted and absorbed by one line, lie outside C, as the report's own next sentence concedes. Kinematic check (r3_P5_cut_structure.py, eikonal currents, Feynman gauge): cross/full = 2.9-3.5 at Y = 0.5, 1.005-1.12 at Y = 3, and 1.000001 at Y = 8. In Feynman gauge the self terms are negative, and D_C is gauge dependent because class C is not gauge invariant. With the common colour factor f^{a1 a2 b} T_A^{a1} T_B^{a2} of the eikonal line vertex, D_C = int C^dag C * 2 vA.vB/((vA.k)(vB.k)) >= 0. So 'PSD' and 'D_C != 0' survive in Feynman gauge in the eikonal approximation, but the stated reason ('a sum of B^dag B terms') does not apply to an interference term.

### [per_result 20]
L7 [R] — CORRECT as corrected.

### [per_result 21]
Remark P6 — appropriate as an ungraded remark.

### [per_result 22]
REG — the asm mapping is verified in spec_v2/ASSUMPTIONS.md (appO-lcopt, appO-envelope, appO-mixing (a)-(c), appO-deformation (a)-(d), appO-rewritten-cs; collinear-ends is correctly marked as proposed). ERROR: 'Local hypotheses of single statements are NOT registered (ASSUMPTIONS.md rule 1): (H_glob); (J); (Sp); (Sp'); (R); NF' misreads rule 00.1-1. That rule registers exactly the unproven hypotheses that are R_cond premises OR are shared by several statements. (Sp') is used by L8, L5, T2 and T3, and (R) by T2, T3 and P4; both are unproven, shared R_cond premises and must be registered or proved. Admissible alternatives with precedent in register §6: (H_glob) as a model definition, as (GC1)-(GC3) are a class definition; NF as the definition of the domain of pointwise statements; (J) and (Sp) as hypotheses of a lemma verified in LCOPT, as (ET1)(ET2). Also, 'G5(ii) needed ... (shown, P5)' overstates an [A] result: it should read 'argued [A]'. The G7 relocation statement is correct.

### [per_result 23]
CMP — ACCURATE, with two precision points checked in arXiv:1708.01743v2. (i) The caveat 'should not be viewed as strict proofs' (pp. 22, 29) qualifies their graphical Section VI only. Their operator-level argument is presented as a proof ('It is proved...' in the abstract and Sec. VII), so the report's non-acceptance rests on its own assessment of the single-evolution-parameter step and should be worded that way. (ii) Eqs. (66)-(70) do rewrite both ends of an A+_G line as delta(n_f+.y) (verified). But A-_G is treated afterwards with a second time-like direction n_f- (eqs. (85)-(86)), so 'one unitary operator U_{+G}' covers the A+_G sector only.

### [per_result 24]
TMD [C] — APPROPRIATE. Verified in arXiv:2201.10901: S = 0.8 is fixed from NA10 nu at E_pi = 194 GeV and reused for E615 and COMPASS, and the quoted phrase 'is not fully inclusive in kinematics' is genuine. The Collins-Qiu abstract does contrast with Drell-Yan. Boer et al. (abstract, §4, App. A) support the 'SA/AS patterns, imaginary parts, no conflict' reading: the surviving entangled diagrams (i)-(iii) have gluons on both spectators coupling to the other hadron's active line, and diagrams (iv),(v) cancel after the cut sum.

### [per_result 25]
EX — ACCURATE. The fix_r2 logs contain exactly the quoted numbers (l1_bound_quadrant, p2_window_shape, l8_bounds, p4_regulated_B, t3e_sensitivity).

### [per_result 26]
LIT — CORRECT. Bibliographic data for all round-2 additions verified on INSPIRE (r3_inspire_refs.log), including Sterman-Erdogan EPJ ST 235 (2026) 1493 = arXiv:2502.14230 ('Coordinate light-cone-ordered perturbation theory'). Novelty searches found no prior statement of T2 for general LCOPT jets, T3, P1, P2(b), P4 or L8 (r3_inspire_novelty*.log, r3_inspire_citers.log). They covered title searches (Glauber with spectator, Glauber with Drell-Yan, 'spectator interactions') and the Glauber/spectator citers of DGOPS, Aybat-Sterman and Rothstein-Stewart. Optional related work for O3/O4: Forshaw-Holguin-Pathak, PRD 104 (2021) L091501 [2108.13439], and Pathak, JHEP 06 (2022) 118 [2108.13440], on ordering Glauber loops against soft emissions and the role of the Lipatov vertex. As a contrast (a trapped Glauber pinch): Nabeebaccus et al., PRD 111 (2025) L091502 [2409.16067].

### [per_result 27]
ERRATA ERR-S1b — VALID in substance; the framing needs one correction. The three quoted sentences exist in refdoc.txt (Rem E.32 around lines 11801-11810, the E.33 status paragraph at line 11862, Rem E.49(2) at line 13014). But the same Rem E.32 states that with exact propagators the orderings are correlated, that the correlation comes from the near-shell points |k+k-| ~ kT^2, and that the strict window loses it. Rem E.49(2) attributes the missing -1/4 C_A chi^2 X to the PV part near 2k+k- = kT^2 AND to three-gluon-vertex real/virtual graphs. ERR-S1b should say that the reference identified the near-shell mechanism. The actual error is its expectation (E.33 status: 'even for G0 it is an assumption about the complete set G') that this is insufficient within G0. T2 shows that the near-shell part of the direct lines alone supplies the full -1/4 C_A chi^2 X for this pattern at O(g^4), so the three-gluon-vertex graphs must have zero net Hermitian C_A X part (not computed).

### [per_result 28]
REVISIONS / OPEN — every round-2 required fix of both reviewers has been addressed, except the process item, which is outside a subagent's remit. O1-O12 are stated honestly.

## required_fixes

### [required_fixes 1]
PROCESS (parent session; round 3 is the last round, so nothing else will apply these fixes). Write journal line 125 (X1-glauber-fix2 result) as verify/extend/X1-glauber/REPORT.md. Save lines 80, 78 and 111 as review_r1_1.md, review_r1_2.md and review_r2_2.md, and the two rev3 results as review_r3_1.md and review_r3_2.md. Do the same for X2 and X3, and add a check to extend() that saves the returned text whenever REPORT.md is missing. Apply the fixes below while patching the spec.

### [required_fixes 2]
P4(b): the claim that the added 1V2 term leaves '(Sp') (no single-state gap)' unchanged is false. Its final gap i/(A'-k2) is single-state, so (Sp') for the adjacent pair (V_H,2) would need a partner s c2[i/(A1+k1)][i/(A2+k1)][i/(B+k1+k2)] in sector 12V. Either state that the class in P4 and in REG-G2 imposes (Sp') on J_B only (which is all T2 needs), or add the partner and note that it shifts W(12,21) only by O(lambda_A K/a + lambda_B/K).

### [required_fixes 3]
P5: replace 'D_C = int dPhi3 (A^lines)^dag A^lines' by the interference form D_C = int dPhi3 [(A_A)^dag A_B + h.c.] (cut rungs join A and B). Note that class C is not gauge invariant, so D_C is gauge dependent. PSD holds in Feynman gauge in the eikonal approximation because D_C = int C^dag C * 2vA.vB/((vA.k)(vB.k)); equality with |A^lines|^2 holds only for light-like lines or in the Regge limit. Remove 'sum of B^dag B terms' as the reason.

### [required_fixes 4]
T2: (i) add to the hypotheses the smallness condition delta_Y <= 1/2, i.e. C_N eps^{1/2}(1+L_B)^2 <= 1/2; eps <= eps_0 does not imply it. (ii) Write the constant C_c of Step 7, or state that C_T also depends on ln(lambda_B/mu_B) through int|g| and the R <= 4lambda_B square. (iii) Either derive the error term in 'Im p_opp = -(1/pi)ln(1/eps) + c + O(...)' under an explicit scaling (fixed jet shapes, a growing), or weaken it to -(1/pi)ln(1/eps) + O(1).

### [required_fixes 5]
REG: under ASSUMPTIONS.md rule 00.1-1, register (Sp') and (R), or prove them; they are unproven R_cond premises shared by L8/L5/T2/T3 and T2/T3/P4. Recast (H_glob) as a model definition, NF as the domain definition of pointwise statements, and (J), (Sp) as lemma hypotheses verified in LCOPT, following the §6 precedents (GC1)-(GC3) and (ET1)(ET2). Change 'G5(ii) ... (shown, P5)' to 'argued [A]'.

### [required_fixes 6]
ERRATA ERR-S1b: acknowledge that Rem E.32 and Rem E.49(2) already attribute the ordering correlation, and part of the missing -1/4 C_A chi^2 X, to the near-shell PV region of the direct lines. Locate the reference's error precisely: it expected this to be insufficient within G0 and the three-gluon-vertex graphs to be needed (E.33 status paragraph). T2 shows that the near-shell part of the direct lines supplies the whole term for this pattern at O(g^4).

### [required_fixes 7]
CMP (Zhou-Yan-Zhang-Li): say that the 'not strict proofs' caveat applies to their graphical Section VI, while the operator-level argument is presented as a proof; the report's non-acceptance is its own assessment of the single-evolution-parameter step. Also note that A-_G is treated with a second direction n_f- (eqs. 85-86), so U_{+G} covers the A+_G sector only.

### [required_fixes 8]
T2'(b): restate 'jet B's poles give the same by symmetry' as the mirror statement under NF_A (k^- rotation); the case with NF dropped on both jets stays O2. T2'(c)/REG: add a sentence that the half-coincident G7 claim is proved with the k^- regulator alone. Including the class-X k^+ factor is expected to cost O(a/(K^+K^-)); this is not proved.

### [required_fixes 9]
T3(e): soften the interpretive sentence 'not determined by the integrand on any window |k^-| <= K'. The proven statement is that any in-window Lorentzian suppression of |k^-| >~ K removes the O(1) part, up to the bound C_e[...]. The Lorentzian also changes the in-window integrand, by a relative O(k^2/K^2).

### [required_fixes 10]
L8(c), axis band: correct the intermediate constant for the multi-state second-gap pieces from 2 to 16/9 + 1 (about 2.78) Mflat lambda/(R^2<r1>). The final constant 9 is unaffected (total about 8.2).

### [required_fixes 11]
Spec integration (WRITER_SPEC_v2 §4.3): give every [R] item exactly one qualifier. The L-lemmas and P2 are pure mathematics (R_PT-type). T1, P1, T2, T3(a)-(c),(e) and P4(b) are R_cond, with premise sentences naming only registered labels; the physical readings of T2 and T3 stay [P].

### [required_fixes 12]
LIT (optional): cite Forshaw-Holguin-Pathak PRD 104 (2021) L091501 and Pathak JHEP 06 (2022) 118 for O3/O4 (ordering of Glauber/Coulomb loops against soft emissions, the Lipatov vertex), and Nabeebaccus et al. PRD 111 (2025) L091502 as a contrast (a trapped Glauber pinch in an exclusive process).
