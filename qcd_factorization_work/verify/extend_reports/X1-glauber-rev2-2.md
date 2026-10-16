# X1-glauber-rev2-2

(extracted verbatim from the workflow journal; structured output of the agent)

## overall

fixable_issues

## per_result

### [per_result 1]
状态（回答“在正常运行吗”）：工作流在运行，但仍有一处不正常，即结果没有存盘。X1 第一轮修订已完成，第二轮审稿正在进行。按 journal，X1-glauber-rev2-2 先在第 103 行启动，中断后又在第 109 行重启。英文详述：verify/extend/X1-glauber/REPORT.md 仍然不存在，review_r1_1.md 和 review_r1_2.md 也不存在。修订者建议在 extend() 里加的存盘检查也还没有加。我审阅的是 fix-round-1 的结构化输出，即 wf_52f29317-58b/journal.jsonl 第 101 行的修订报告。它与 scratchpad 中 x1rev2_1/fix1_SO.json 的副本逐字节相同，且自称取代原作者结果（第 42 行）。两份第一轮审稿意见在第 80 行和第 78 行。按 harness 的“子代理不写报告类 .md 文件”规则，我没有写 review_r2_2.md，本结构化输出就是审稿意见，需要父会话存盘。独立检查脚本和日志在 verify/extend/X1-glauber/review_r2_2_scripts/，含 chkA–chkE 的 .py 与 logs/。

### [per_result 2]
DEFS — CORRECT with minor wording issues. (H_glob), (R) and NF are now explicit hypotheses. I re-derived the NF quantification: alpha_1 = (2 s_T.k_2T - k_2T^2)/(2 x_s P^+), so alpha_1 > 0 exactly when s_T.k_2T > k_2T^2/2. The corrected Def 3.2 agrees with Jcal_A = i/d_0. A sympy check (chkD) confirms that the covariant scalar-model J_A^[12] equals the sum of the three LCOPT sector terms, each carrying the common factor i/d_0. The remark that ordering information is 'generated at the gluon poles' depends on how the integral is represented (see the T3(e) entry).

### [per_result 3]
L1 [R] — (a) and (c) CORRECT, (b) has a GAP as stated. (a) holds also for complex poles at finite eta: in chkA, direct quadrature matches the formula to 1e-12 at eta = 0.05. (c) is the eikonal identity, and the race interpretation is right. (b): the first inequality, |J^(sigma)(z) - lead| <= N 2^{N+1} M_sigma (lambda_J/kappa) prod|K_l|^{-1}, is right; I re-derived the telescoping step and the lambda_J^{-d_t} normalisation. The 'Hence' step is not: multiplying by prod(-/+ i r_e) gives a relative error N 2^{N+1} M (lambda_J/kappa) * Sum_sigma |w_sigma(z)|. The stated O(N 2^{N+1} max M lambda_J/kappa) silently assumes Sum|w_sigma| <= 1, and the lemma allows arbitrary complex z. Counterexample (chkA): N = 2, both insertions final, z = (1-0.01i, -0.99-0.01i), A_1 = A_2 = -0.005, kappa = 0.0224. The actual relative error is 8.86, against a stated bound of 3.58; with the factor |w| = 44.7 included the bound is 160 and holds. This is harmless for the Glauber application: real same-sign poles give w_sigma in [0,1] and Sum = 1. If each group's poles lie in one closed quadrant, then |w_sigma| <= 1. Either condition, or the factor itself, must be stated. The novelty restriction is correct; the race formula is in App E.4.4, which I checked in refdoc.txt.

### [per_result 4]
L1' [R] — (a) and (c) CORRECT, (b) has the SAME GAP as L1(b). I re-derived the example weights analytically: u_z = K^2/(z^2+K^2), u_+ = z/(2(z-iK)), u_- = z/(2(z+iK)), and they sum to 1. The bound in (b) should read |Err| <= N 2^{N+1} max M (lambda_J/kappa) Sum_(p) prod_e |rho_{e,p}/p| Sum_sigma |w_sigma(p)|. The stated prod ||R_e|| needs Sum_sigma |w_sigma(p)| <= 1. For the Lorentzian example, each group's poles lie in a closed quadrant, so |w_sigma| <= 1 and Sum <= n_F! n_B!; this only changes the constant. For the arbitrary soft-line poles of L7 the factor can be large.

### [per_result 5]
L2 [R] — CORRECT. I re-derived: continuity across a single hyperplane k_e^+ = 0 under (Sp), with e moving next to V_H in the same colour position from both sides; the kink in (c); and the discontinuity at the origin. The claim to correct ERR-S3's wording is accurate; I checked the ERR-S3 text in REFDOC_ANALYSIS ('non-analytic at k_j^+=0 exactly like c_j = theta(k_j^+)'). The physical caveat is appropriate.

### [per_result 6]
T1 [R_cond] — CORRECT and correctly relabelled as a re-derivation. The hypotheses of Prop E.35 in refdoc.txt are 'abelian, or at most one localizable insertion per spectator per side; otherwise E.33(c1)'. So the content is the reference's E.35/E.31(iii). The only new element is the route via L1.

### [per_result 7]
P1 [R_cond] — CORRECT. I re-derived E(l) <= 2E^(0)(l) + Delta_l^2/l^+ from (a+b)^2 <= 2a^2 + 2b^2, with l^+ unchanged under E.19(a). I also checked the single-state bounds |A_D| <= max(P^-, Sum_S E) and |A'_D| <= max(E_cut, Sum_S E), and the multiplicity n_A. Minor gap: the family identity is applied after the (R1) cut sum, so nu-hat must also be independent of the cut position. The parenthetical '(each spectator line counted once on each side of the cut, cut lines once)' reads as cut-dependent. It should be stated as a sum over the lines of the forward graph, which is cut-independent.

### [per_result 8]
L3 [R] — CORRECT. I checked the prefactor: in quadrant (-,+), prod(-i sgn(k_e^+) r_e) = -1/(4k^2), so F_A^[12](-k,k) = -J^(1V2)(z_1,z_2)/(4k^2). The incompatibility rules and the holomorphy domains (UHP for k^+ > 0, LHP for k^+ < 0) are right.

### [per_result 9]
L4 [R] — (a)-(d) CORRECT. I re-derived (b) by hand: R = 2i chi_1 chi_2 Im W_12 [X_1,X_2], using W_12 + W_21 = 1 and conjugate insertions on the left. My independent colour code (chkC) builds its own real adjoint basis from 3 x 3bar matrix units. It reproduces: [X_1,X_2] = i f T_i T_j1 T_j2; X_e real symmetric and [X_1,X_2] real antisymmetric; (d1) with kappa_i = 1 (A-rem = qbar) and 1/2 (diquark), to <= 1.7e-16 on random complex DY states; exact vanishing when B-rem = {j1,j2}, including A-rem = q q g, where the 3bar multiplicity space has dim 2 and K_i is a matrix; and the operator norms 0.4330, 0.2165, 0.3536. (d2) holds only in a weight (tensor-product) basis; in the standard adjoint basis all signs are -1. The report's phrase 'common real weight basis' is adequate. Novelty of the form is fine; the colour-singlet mechanism is credited to LRS, whose abstract (NPB 222) I verified.

### [per_result 10]
L5 [R] — CORRECT, with the proof still a sketch. I checked: in the swept region, Im z_e = -a_e sin t/(2x_e), so each quadrant piece stays in its holomorphy domain. J_B's initial factors A - e^{it}X never vanish for t in (0,pi) and are consistent with i0 because A < 0. The final factors A' + e^{it}X are consistent with i0 iff A' < 0, which is NF_B. The t = pi correction is right. The arc and strip estimates are only asserted.

### [per_result 11]
L6 [R] — CORRECT. I re-derived it by Cauchy's theorem with f = [rho - (1+k)^{-1}]/k on the quadrant: Im int dkappa/kappa (1+i kappa)^{-1} = -pi/2, and the axis-pole term is -pi Sum Res/k_p.

### [per_result 12]
T2 [R_cond] — the MODEL STATEMENT IS SUPPORTED, but the PROOF IS INCOMPLETE and one physical sentence is misleading. Independently re-derived: Step 3, p_opp^in = -(1/2Jcal_B) int S_B(-i kappa) + (1/Jcal_B) int v Delta_B(-i kappa), with v real and odd and the v-term imaginary by (R); int S_B(-i kappa) = -Jcal_B. Step 4's coefficient, p_opp^out = -(i/2pi) int_K^inf (dkappa/kappa)[varrho_12 + varrho_21], using int g_B(-iU) dU/2pi = -i Jcal_B, which comes from the counterclockwise rotation, the only one consistent with i0 under NF_B. For the scalar model, rho_12 = a1 a2/[(2k d10 - a1)(2k alpha1 - a2)] (sympy, chkD) is real-analytic in the first quadrant under NF_A, with rho(0) = 1, so L6 gives exactly -pi/2. The quoted numbers match the logs (base Re p_opp 0.0123470862, 0.0003447618; N/N0 -> 1). GAPS: (i) Steps 3-4 assert without proof: the off-strip decay O(lambda_B/|u|^3) of each colour-ordered J_B (the leading 1/|u|^2 cancels in the sector sum, which I checked for single-state gaps but which must be shown for (J)-class jets with multi-state gaps); the O(lambda_B/|p_2|) strip corrections; and the O(lambda_B/K) tail of S_B. For [R_cond] these must be written out with constants. (ii) Physical reading: under (H_glob), NF and G7, T2 contradicts Rem E.32's explicit statement that 'within G_0 the O(chi^2) residual should not be expected to vanish', which I verified in refdoc.txt. 'Sharpens' understates this; it should say so plainly, while keeping 'E.33(c2) not refuted'. The supporting unitarity argument (the crossed box has no s-channel cut; ERR-S1 gives p_opp = -iY/pi) is sound. The novelty restriction is correct: the Lindsay 1984 and BFT 1989 INSPIRE abstracts confirm cancellation in the sum of all two-loop diagrams.

### [per_result 13]
T2' — (a) CORRECT for class-X k^+ regulators. (b) CORRECT: the end-pole formula Res(rho_12)/k_p = -a1 alpha1/(a1 alpha1 + a2|d10|) is verified symbolically (chkD), and apole 0.2520 vs 0.2517 matches the log. Two wording gaps. First, 'these terms are artefacts of (H_glob)' rests on the massive-spectator argument (s.k = 0 is impossible). For massless QCD partons, s.k = 0 occurs for collinear k, so the end poles are genuine A-collinear configurations: they belong to the collinear region under G7 rather than being artefacts. Second, '(a) ... the real part does not [depend on the end]' must be qualified by K^+K^- >> k_T^2: T2'(c) itself shows Re p_opp -> 1/2 when an A-side k^- regulator cuts below a/K^+. (c) [P]: the numbers match regulator_indep_B.log and t2_nearshell.log. The SUMMARY's '-> 1/2 otherwise' holds only for even or line-identical regulators (see P2), and at K^+K^-/a = 1 the value is 0.149, i.e. a crossover rather than 1/2.

### [per_result 14]
P2 — the RESULT is CORRECT (this is E.48(d)); the DIAGNOSIS is INCOMPLETE. In chkB, with the strict propagator and independent sharp truncations [-K1,K2], the weights are 1/2 +/- (i/2pi) ln(K2/K1) (numerically exact). Then p_opp = 1/2 + 2 delta_A delta_B, which ranges over [0,1]: p_opp = 0 for opposite windows with ln(K2/K1) = +/- pi, and p_opp = 1 for equal ones. Smooth even (Lorentzian) cut-offs give exactly 1/2, even with line-dependent scales. Non-even, line-dependent smooth cut-offs give other values, e.g. 0.924. So 'smooth analytic two-sided cut-offs that exclude the near-shell region give the same 1/2' holds only for even or line-identical regulators. The accurate diagnosis: excluding the near-shell region decorrelates the two jets' orderings and leaves a value set by the regulator's shape, which is E.48(d)'s 'property of the regularization'. 1/2 is the symmetric-regulator value.

### [per_result 15]
P3 — CORRECT and known. The crossed box has no s-channel cut: each side reduces to a single on-shell emission from a massive line. The three-line Remark is properly marked uncertified (O9).

### [per_result 16]
T3 — (a)-(c) CORRECT, and the numbers in (d) and (f) match the logs: halfcoinc.log 0.49787981-0.03662858i etc.; halfcoinc_sym.log symmetric -0.0000283i, B-asym +0.04679i, a-asym -0.02120i; regulator_indep_A.log vs t3_regulator.log agree to >= 4 digits. (e) is a GRADE ERROR. That Im W_12 'is generated at |k^-| ~ a/lambda_B' depends on the representation: the same integral can be evaluated by closing on J_A's poles or on rotated contours. The meaningful content is the sensitivity statement of (f): a regulator that suppresses |k^-| >~ K, with K << a/lambda_B, drives Im W_12 to O(K lambda_B/a). That is numerical [P], not [R_cond]. Also, 'the weights are values of the external factors at k^- = z_e' is imprecise: they are J_A's equal-time asymptotics evaluated at the gluon-pole positions. (g) is CORRECT. It also implies that T3's own model (B -> b + s1 + s2, so B-rem = {j1,j2}) has a vanishing DY colour factor; (d) should say so. In (i), LRS's configuration has AS-type insertions (no A-spectator); the mechanism is analogous, as phrased.

### [per_result 17]
P4 [R_cond] — CORRECT within the class (J), (Sp), (R). I recomputed independently (chkE): int dk/k rho2 = -0.38629436112 (= 1 - 2 ln 2 for set 1), -0.376196716824 and 0.49648105127, giving dW/s = +0.06148i, +0.05987i, -0.07902i. The rotation to the real axis is valid because the poles of rho2, at a1/(2A1), a1/(2A2) and a2/(2A'), are negative. GAP: the perturbing two-state term is not shown to come from any graph (O10). So the CONSEQUENCE 'no per-graph rewriting ... can satisfy (E.35)', and REG-G2's '(the per-graph version is false, P4)', must be stated for that class, not for physical LCOPT jets.

### [per_result 18]
P5 [A] — ACCEPTABLE. The line part of the Lipatov vertex and the abelian vanishing for straight lines are standard. REG-G5(ii)'s 'needed for every non-abelian coincident pattern from O(g^6) on' generalises from the fully coincident two-line ladder class. It should read 'shown for that class, expected for the others'.

### [per_result 19]
L7 [R] — (a) CORRECT: the affine zero lies at distance >= 2 Lambda_j, |l^2 - m^2| >= 1/2 |l^2(0) - m^2| on the disc, and the bound 2^{n_j} follows. (b) has a GAP for several insertions: it inherits the missing Sum_sigma|w_sigma(p)| factor of L1'(b), and soft-line poles in one group can have opposite real parts, so the factor is unbounded in general. For one insertion, via E.28(iii), it is fine. Replacing E.33(a) by the assumption G3' is honest.

### [per_result 20]
Remark P6 — APPROPRIATE as an ungraded remark.

### [per_result 21]
REG — CONSISTENT with the revised results. I checked that the two-sided G7 window is non-empty: a << K^+K^- << a/epsilon. With K^+ >> lambda_B, the half-coincident suppression (K^- << a/lambda_B) and the fully coincident cancellation (K^+K^- >> a) hold together, matching the T2'(c) entries for K^+ = 1e4 lambda_B, which lie in G7 range. Fixes needed: the P4 qualification under G2, and the wording of G5(ii) (see above).

### [per_result 22]
CMP — ACCURATE. I read DGOPS §4 myself (arXiv:1510.08696). Steps 1-6 match the report; step 3 contains 'It would be desirable to have a formal proof that this is always possible'. §4.3.1, eqs. (4.18)-(4.20), is the light-cone Cutkosky identity, and §4.3.4 proves that R is independent of the partition V. DGOPS step 6 explicitly states that failures of the approximations in larger regions are removed by subtraction terms, which supports the CMP reading of T3's B-collinear-end residual. The CSS review §8.4 sentence about deforming kappa^+- to |kappa^+-| ~ |k_T| is verified. Bibliographic error: arXiv:1510.08696 exists only as v1 (the v2 URL returns 404; the abs page lists only [v1]). The cited §4 = pp. 38-52 is correct for v1.

### [per_result 23]
TMD [C] — the GRADE IS APPROPRIATE. Literature is missing for item (iii) (staple direction and T-odd TMDs): Collins, PLB 536 (2002) 43, and Collins & Metz, PRL 93 (2004) 252001; both verified on INSPIRE. A dissenting phenomenological line, which claims non-cancelling Glauber phases in pion-induced Drell-Yan within k_T factorisation, should be cited and discussed: Chang & Li, PLB 726 (2013) 262; Li, PRD 106 (2022) 014029.

### [per_result 24]
EX — the LOG ACCOUNT IS NOW ACCURATE. Spot checks against the logs: brute force W(12,12) = 0.135732, 0.117983, 0.110479, 0.107262; base 0.0123470862 and 0.0003447618; apole 0.2625709, 0.2535667, 0.2520385; the half-coincident, symmetric and asymmetric sets; T3(f); T2'(c); the colour norms; P4. checks_C2_C3_C4.log and check_halfcoinc_singlets_v2.log both end with ALL PASS. The account of method I's defect, and the cross-check of the alt set against altswap, are sound.

### [per_result 25]
LIT — I verified the bibliographic data on INSPIRE for: BBL 1981; LRS PLB 117, NPB 214, NPB 222; Nelson 1983; Lindsay 1984; Bodwin 1985 with its erratum; CSS 1985, 1988 and the review; Brandt 1989; BFT 1989; Liu-Ma; Gaunt 2014; Angeles-Martinez-Forshaw-Seymour 2015; DGOPS 2016; Rothstein-Stewart 2016; Schwartz-Yan-Zhu 2018; Del Duca; Sterman-Erdogan (EPJ ST 235 (2026) 1493). The descriptions agree with the abstracts. MISSING: Aybat & Sterman, PLB 671 (2009) 46, arXiv:0811.0246, which gives an all-order argument for the cancellation of Glauber gluons and divergent phases with initial-state partons; it is relevant to CMP and to the novelty claims. The TMD references above are also missing. Novelty is now restricted appropriately: INSPIRE title searches (Glauber + Drell-Yan since 2015) found nothing that pre-empts the App-E-framework statements.

### [per_result 26]
REVISIONS / OPEN — every round-1 item is addressed at least nominally. The stated departures are justified: lambda_J^{-d_t} is the dimensionally correct normalisation, and rejecting 'sharp truncation' as the cause is right, although P2's symmetric-shape dependence must be added. New open items to add: (O11) the regulator-shape dependence of the residual once the near-shell region is excluded; and the bound fix in L1(b), L1'(b) and L7(b). The process item (persistence) remains unresolved.

## required_fixes

### [required_fixes 1]
PROCESS: the parent session must write three files: journal line 101 (the fix-round-1 result) as verify/extend/X1-glauber/REPORT.md; lines 80 and 78 as review_r1_1.md and review_r1_2.md; and this structured output as review_r2_2.md. It must also add the persistence check to extend(), for X2 and X3 as well. Until then every reviewer is pointed at a missing file.

### [required_fixes 2]
L1(b), L1'(b), L7(b): put the factor Sum_sigma |w_sigma(z)| into the relative-error bound, or add a hypothesis. Either: each group's poles lie in one closed quadrant, giving |w_sigma| <= 1 and Sum <= n_F! n_B!; or: poles are real and of the same sign within each group (the Glauber case), giving Sum = 1. Then restate the Glauber corollary. Counterexample to the current statement: chkA.log, case (ii).

### [required_fixes 3]
P2, plus the SUMMARY and T2'(c) phrase '-> 1/2 otherwise': replace the diagnosis with the regulator-shape statement. Once the near-shell region is excluded, p_opp depends on the regulator: 1/2 for even or line-identical cut-offs; 1/2 + 2 delta_A delta_B in [0,1] for sharp asymmetric windows, with delta = ln(K2/K1)/2pi; other real values for non-even, line-dependent smooth cut-offs (chkB.log). Describe K^+K^- ~ k_T^2 as a crossover.

### [required_fixes 4]
T3(e): downgrade to a remark, or restate as a sensitivity proposition with proof (modifying the integrand at |k^-| >~ K changes W_12 by O(1)). Replace 'values of the external factors at k^- = z_e' with 'J_A's equal-time asymptotics at the gluon-pole positions'. In (d), state that the model's own DY colour factor vanishes (B-rem = {j1,j2}, by L4(d1)).

### [required_fixes 5]
T2'(a): qualify 'the real part does not [depend on the end]' by K^+K^- >> k_T^2. T2'(b): replace 'artefacts of (H_glob)' with 'artefacts for massive spectators; for massless partons they are genuine A-collinear configurations, assigned to the collinear region by G7'.

### [required_fixes 6]
T2, T3(b), L5: write out the omitted estimates with explicit constants: off-strip decay of each colour-ordered J_B for (J)-class jets with multi-state gaps; the O(lambda_B/|p_2|) strip corrections and their dkappa/kappa integral; the S_B tail; the arc estimates. Otherwise label these items [A] (within App E's framework, sketched and numerically confirmed) until the proofs exist.

### [required_fixes 7]
T2 physical reading: state plainly that, under (H_glob), NF and G7, T2 contradicts Rem E.32's statement that the G_0 residual should not be expected to vanish. Keep the statement that E.33(c2) is not refuted, and cite the on-shell unitarity argument (P3, ERR-S1) as the consistency check.

### [required_fixes 8]
P4 and REG-G2: qualify the per-graph consequence as holding within the class (J), (Sp), (R); for graph-generated jets it is open (O10).

### [required_fixes 9]
P1: state explicitly that J_A^0, and hence nu-hat, is a sum over the lines of the forward graph and therefore independent of the cut position, which the (R1)-then-(R2) order requires.

### [required_fixes 10]
CMP and LIT: correct arXiv:1510.08696v2 to v1. Add Aybat & Sterman, PLB 671 (2009) 46 (arXiv:0811.0246). In TMD, add Collins PLB 536 (2002) 43 and Collins & Metz PRL 93 (2004) 252001, and discuss the dissenting Chang & Li PLB 726 (2013) 262 and Li PRD 106 (2022) 014029 (Glauber phases in pion-induced DY).

### [required_fixes 11]
REG-G5(ii): change 'needed for every non-abelian coincident pattern from O(g^6) on' to 'shown for the fully coincident two-line ladder class (P5), expected for the other coincident patterns'.

### [required_fixes 12]
OPEN: add O11, the regulator-shape dependence of the residual once the near-shell region is excluded. Record the L1(b), L1'(b), L7(b) bound correction in REVISIONS.
