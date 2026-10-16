# X1-glauber-rev2-1

(extracted verbatim from the workflow journal; structured output of the agent)

## overall

fixable_issues

## per_result

### [per_result 1]
PROCESS / INPUT — run status (relayed question 在正常运行吗): the workflow is running, but not fully normally. (1) verify/extend/X1-glauber/REPORT.md still does not exist; neither do review_r1_1.md, review_r1_2.md, or any REPORT.md for X2 or X3 (I searched the whole home directory). I therefore reviewed the current report as it was returned by agent X1-glauber-fix1 (a4cf5517baa9f46e2), which is recorded only in workflow journal line 101 (wf_52f29317-58b/journal.jsonl): summary, results[0..24] and open[0..9]. I also read the author's original result (line 42) and both round-1 reviews (lines 78 and 80). (2) X1 and X2 are in round-2 review and X3 is in fix round 1; all three were restarted at 03:21 after a session limit (the first rev2-1 attempt, a965df72c47e2cb4e, stopped at 02:40 without output). (3) Unlike earlier agents, I was able to write my review to disk: /Users/hao-cheng/Desktop/theorem proof/qcd_factorization_work/verify/extend/X1-glauber/review_r2_1.md. Scripts are in review_r2_1_scripts/, logs in review_r2_1_logs/.

### [per_result 2]
DEFS — CORRECT. (H_glob) is now an explicit hypothesis. The remark that ordering information is generated at the gluon poles k^- = a/(2k^+) agrees with my real-contour checks. Def 3.2 is consistent with the model: Jcal_A = i/d0 gives rho_12(0) = 1 (sympy). (R) is listed as an assumption. The NF formula alpha_1 = (2 s_T.k_2T - k_2T^2)/(2 x_s P^+) is verified with sympy. Minor: P1 implicitly uses E.19(a) to make l^+ independent of the SS momenta; say so.

### [per_result 3]
L1 [R] — CORRECT. I tested the corrected bound N 2^{N+1} M_sigma (lambda_J/kappa) prod|K_l|^{-1}, with M_sigma = sum_t |c_t| lambda_J^{-d_t}, on 20000 random sectors with multi-state gaps and complex z (kappa >= 2 lambda_J). The largest lhs/bound was 0.42, so the bound holds. The algebraic step 2^{N+d}(lJ/kappa)^d <= 2^{N+1} lJ/kappa is also checked. The novelty is now correctly restricted to the sector rule, finite-eta exactness and the error bound.

### [per_result 4]
L1' [R] — CORRECT. sympy reproduces the pole weights exactly (u_z = K^2/(z^2+K^2), u_+ = z/(2(z-iK)), u_- = z/(2(z+iK))) and the sum rule sum = 1. My independent real-contour runs with regulator poles validate its use (T3(f), T2'(c)).

### [per_result 5]
L2 [R] — CORRECT. I re-derived the two-line weights in all four quadrants and the continuity with a kink across a single k_e^+ = 0.

### [per_result 6]
T1 — CORRECT. It is properly relabelled as a re-derivation of the reference's E.35/E.31(iii).

### [per_result 7]
P1 [R_cond] — CORRECT AS REVISED, WITH A GAP (hidden assumption). (a), (b) and (d) re-derived; in particular E(l) <= 2E^(0)(l) + Delta_l^2/l^+ and the single-state bounds. The gap: (c), 'nu-hat ~ lambda^2 Q on the Glauber core', needs x^A_min and x^B_min bounded below by an O(1) fraction. Otherwise the term 2 n_A (sum|k_T|)^2/x_min is enhanced, and so is lambda_J <= C nu-hat, which degrades the localization error lambda_J/kappa. Separately, (b) silently uses E.19(a) (l^+ does not depend on the SS momenta).

### [per_result 8]
L3 [R] — CORRECT. My real-contour codes use exactly this quadrant structure and agree with the rotated results to about 1e-6.

### [per_result 9]
L4 — (a) CORRECT (sympy: -1/2 C_A chi^2 Re(p_opp) X). (b) GAP (convention): R = +2i c1 c2 Im W12 [X1,X2] holds only if M^(1)_e = -i c_e X_e with c_e real. With M^(1)_e = c_e X_e, c_e = -i chi_e, the sign is opposite (explicit-matrix check). c_e is never defined. (c), (d1), (d2) and the norms are CORRECT; I checked them with my own SU(3) code, using a randomly rotated real octet basis. (c) gives <= 5e-17 on the three-spectator singlet spaces. (d1) gives |lhs-rhs| <= 4e-16 on random complex DY states, including kappa_i = 1/2 with a further B-remnant parton, and exactly 0 when B-rem = {j1,j2}. (d2): P[X1,X2]P is real antisymmetric. The norms 0.4330, 0.2165, 0.3536 and 0.7071 hold for every (j1,j2) choice. Scope GAP in (d3) and T3(g): 'vanishes in the commonest DY configurations' is true only for valence (minimal-Fock) or real colour states. Generic multi-parton remnants with complex colour amplitudes are not covered, and I see no symmetry that makes the remnant-integrated residual vanish.

### [per_result 10]
L5 [R] — CORRECT. The t-range is fixed. Three independent real-contour computations (half-coincident W12 in two configurations, and the fully coincident regulated p_opp) reproduce the rotated-contour values to about 1e-6 without any rotation.

### [per_result 11]
L6 [R] — CORRECT. Re-derived by Cauchy's theorem applied to [rho-(1+k)^{-1}]/k on the quadrant; the -pi Res/k_p term is right.

### [per_result 12]
T2 [R_cond] — MATHEMATICALLY CORRECT; one citation is WRONG and one statement is mispositioned. I re-derived the key coefficients: int S_B(-i kappa) d^2kappa/(2pi)^2 = -Jcal_B (from d^2u = -d^2kappa); int g_B(-iU) dU/2pi = -i Jcal_B under NF_B; W^out(12,21) = -(i/2pi) int_K^inf dkappa/kappa varrho_12 (from J_B^[21] ~ -g_B/(i p_2) in the strip); and -1/4 per mixed sector from L6. (i) WRONG citation: the NOVELTY paragraph and LIT list LRS (PLB 117, NPB 214, NPB 222) among two-loop demonstrations of the fully coincident SS cancellation. LRS have no A-side spectator (the report's own T3 paragraph says so), so they contain no SS pattern; only Lindsay 1984 and BFT 1989 can. (ii) Positioning: the reference explicitly expects the opposite. Rem E.32 says 'in G_0 the O(chi^2) residual should not be expected to vanish', and the status paragraph of Assumption E.33 repeats it, with only the colour-structure coincidence as a reason. T2 together with T2'(c) contradicts that expectation for this pattern at O(g^4) (H_glob model, pointwise on NF, in-window regulators). The report should say so plainly (an errata item) instead of 'sharpens'. It should also contrast its 'three-gluon-vertex graphs not needed' remark with Boer et al., SciPost Phys. 3 (2017) 040, where in a two-gluon spectator model the three-gluon-vertex graphs are essential for the double-Boer-Mulders (T-odd) observable.

### [per_result 13]
T2' — (a) CORRECT, with a quantitative GAP. 'Re p_opp = O(power)' should state the rate the proof gives: O((lambda_B/K_c)^{1/2} + K_c lambda_A/a) up to logarithms, since the inner square needs K << K_c and the strip tail is O(lambda_B/K). This matches the observed lambda^{1/2} convergence (0.103, 0.054, 0.028). (b) CORRECT: sympy gives rho_12 = a1 a2/((a1 - 2 d10 k)(a2 - 2 alpha1 k)) and Res/k_p = -a1 alpha1/(a1 alpha1 + a2|d10|). The predicted values are apole 0.25172 and alt 0.04834, matching the report. Note that apole also has alpha_0 > 0; that pole sits in the both-final sector and contributes no end-pole term, which the report should say. (c) CORRECT as a [P] model statement, confirmed on the REAL contour at K^+ = 100 lambda_B, extrapolating delta -> 0. Without K^-: 0.0138825 - 1.5646509i (report 0.013880 - 1.564651i). At K^+K^-/a = 1000: 0.0137517 - 1.5504271i (report 0.013749 - 1.550427i). At 1: 0.1491170 - 0.2171151i (report 0.149117 - 0.217115i). At 1e-3: 0.4994934 (report 0.499493).

### [per_result 14]
P2 — CORRECT and known. The diagnosis is now right. I read the reference's Lemma E.48(d): w = 1/2 x 1/2 for all four order pairs.

### [per_result 15]
P3 — CORRECT and known in substance. The three-line remark is properly marked uncertified (O9).

### [per_result 16]
T3 — CORRECT AS RESTATED. A real-contour calculation (exact partial fractions for the inner integral, delta = 1e-3 to 1e-6, no rotation) gives the localized race value W12 -> 0.5000000 - 0.0305591i (report 0.5 - 0.030560i). For the B-asymmetric set it gives 0.5000000 + 0.0468158i (report +0.046818i). With the A-side k^- regulator, Im W12 = -0.0297491, -0.0203564, -0.0049989 and -0.00060104 for K = 10, 1, 0.1 and 0.01 x a/lambda_B (report -0.029750, -0.020357, -0.004999, -0.000601), and Re W12 = 1/2 to 2e-9. The location claim (e) is consistent with this. (g) has the scope gap noted under L4. The novelty paragraph is accurate.

### [per_result 17]
P4 [R_cond] — CORRECT, but needs refinements. sympy reproduces the closed forms: 1 - ln 4 = -0.38629436, -0.37619672, and (39/50) ln 6 - (13/10) ln 2 = 0.49648105, giving dW/s = +0.0614807i, +0.0598736i and -0.0790174i. rho2 has a fixed sign on (0, inf), so the shift is non-zero whenever ct2 != 0, not merely 'generically'. GAP in the CONSEQUENCE: as stated it holds for the unregulated H_glob integrand. With G7's in-window k^+ regulator the A-collinear-end dependence is cut off, and the per-graph obstruction rests only on the in-window J_B-shape dependence (the imaginary v Delta_B term). The report should say which version of E.35 is excluded.

### [per_result 18]
P5 [A] — ACCEPTABLE, with a GAP: 'its defect is a positive operator' is undefined. The Schwartz-Yan-Zhu description matches their abstract.

### [per_result 19]
L7 [R] — CORRECT and elementary. Recasting it as a pre-integration statement with G3' is the honest form.

### [per_result 20]
Remark P6 — ACCEPTABLE as an ungraded remark.

### [per_result 21]
REG — CONSISTENT with the results. Suggestion: state explicitly that G7 is a new matching assumption that relocates, rather than removes, the content of E.33(c2) for the coincident O(g^4) patterns. Map G1-G7, (H_glob), (R), (Sp), (J) and NF onto asm:appO-* labels; WRITER_SPEC_v2 requires premises to be named as asm labels for [R, R_cond] statements.

### [per_result 22]
CMP — CORRECT. I read DGOPS (arXiv:1510.08696): the step-3 sentence 'It would be desirable to have a formal proof that this is always possible...' and eqs. (4.18)-(4.20) (cut sum plus k^- integral gives 0 or 1) are as described. Minor GAP: the citation 'arXiv:1510.08696v2' is wrong, since arXiv has only v1 (published as JHEP 01 (2016) 076).

### [per_result 23]
TMD [C] — ACCEPTABLE. GAP: directly relevant references are missing. Boer-van Daal-Gaunt-Kasemets-Mulders, SciPost Phys. 3 (2017) 040, is a two-gluon spectator-model test of colour entanglement in which the Glauber region gives the whole dBM term and three-gluon graphs are essential. Buffing-Mulders, PRL 112 (2014) 092002, proposed the colour entanglement. Chang-Li, PLB 726 (2013) 262, and Li, PRD 106 (2022) 014029, claim observable Glauber phases in pion-induced DY.

### [per_result 24]
EX — CORRECT. The log account is now accurate: checks_C2_C3_C4.log ALL PASS, the _r0 log is kept as history, and check_halfcoinc_singlets_v2.log and colour_dy_check.log are ALL PASS.

### [per_result 25]
LIT — GAP (incompleteness). All 19 entries I checked on INSPIRE are bibliographically correct; I did not check Lipatov 1976 or KLF 1977. Missing and relevant: Doria-Frenkel-Taylor NPB 168 (1980) 93; Di'Lieto-Gendron-Halliday-Sachrajda NPB 183 (1981) 223; Andrasi et al. NPB 182 (1981) 104 (two-loop non-abelian Bloch-Nordsieck violation, the origin of the colour-singlet/spectator issue); Landshoff-Stirling ZPC 14 (1982) 251; Zhou-Yan-Zhang-Li, Commun. Theor. Phys. 74 (2022) 115202 / arXiv:1708.01743 (a SCET argument that SS Glauber exchanges cancel); Forshaw-Kyrieleis-Seymour JHEP 08 (2006) 059; Forshaw-Seymour-Siodmok JHEP 11 (2012) 066; Catani-de Florian-Rodrigo JHEP 07 (2012) 026 (non-commuting Coulomb/Glauber exchanges and the f T T T structure); Becher et al. PRL 134 (2025) 061901; Boer et al. 2017; Buffing-Mulders 2014. My INSPIRE searches found no prior statement of T2 for general LCOPT jets, of T3's configuration, of P1 or of P4, so the restricted novelty claims are plausible.

### [per_result 26]
REVISIONS — ACCURATE. Every round-1 item from journal lines 78 and 80 is addressed as described.

## required_fixes

### [required_fixes 1]
F1 (factual): remove LRS (PLB 117 (1982) 105; NPB 214 (1983) 61; NPB 222 (1983) 189) from the list of calculations that showed the fully coincident spectator-spectator cancellation, in both T2's NOVELTY and LIT. They have no A-side spectator. Keep Lindsay 1984 and BFT 1989, and describe LRS as covering active-spectator patterns.

### [required_fixes 2]
F2 (positioning): in T2's PHYSICAL READING, state explicitly what is contradicted. Within the H_glob model, pointwise on NF, at O(g^4), for the fully coincident SS pattern, the G_0-restricted E.33(c2) holds (T2 with T2'(c)). This contradicts the expectation stated in Rem E.32 ('in G_0 the O(chi^2) residual should not be expected to vanish') and in the status paragraph of Assumption E.33, whose colour-structure argument does not show non-cancellation. Add this as an errata item (App Q). Contrast the 'three-gluon-vertex graphs not needed' remark with Boer et al., SciPost Phys. 3 (2017) 040, which concerns a different, T-odd observable.

### [required_fixes 3]
F3: in L4(b), define c_e through M^(1)_e = -i c_e X_e with c_e real (the reference's -i chi X). Without this the sign of R = 2i c1 c2 Im W12 [X1,X2] is ambiguous.

### [required_fixes 4]
F4: in P1(c), add the hypothesis x^A_min, x^B_min >= c > 0, or assign the endpoint region (wee lines carrying SS momentum) to K_R / E.44(c). State that (b) uses the E.19(a) independence of l^+ from the SS momenta.

### [required_fixes 5]
F5: in T2'(a), replace 'Re p_opp = O(power)' by Re p_opp = O((lambda_B/K_c)^{1/2} + K_c lambda_A/a) up to logarithms, with the reason: the inner square needs K << K_c and the strip tail is O(lambda_B/K). In T2'(b), note that alpha_0 > 0 poles (as in the apole set) lie in the both-final sector and give no end-pole term.

### [required_fixes 6]
F6: in P4, replace 'generically non-zero' by 'non-zero whenever ct2 != 0' (rho2 has a fixed sign on (0, inf)). Qualify the CONSEQUENCE: as stated it holds for the unregulated H_glob integrand; with G7 regulators the obstruction rests on the in-window J_B-shape dependence. Say which version of E.35 (per graph, jet-local rewriting by D) is excluded.

### [required_fixes 7]
F7: in L4(d3) and T3(g), replace 'vanishes in the commonest DY colour configurations' by 'vanishes for valence (minimal-Fock) remnants and for real colour states'. State that generic multi-parton remnants with complex colour amplitudes are not covered, and add to O1 the open question of whether the remnant-integrated residual vanishes.

### [required_fixes 8]
F8: in P5, define the 'defect' (for example, Disc_s of the class minus the cuts that stay inside the class), or delete 'positive operator'.

### [required_fixes 9]
F9: in LIT and TMD, add Doria-Frenkel-Taylor 1980, Di'Lieto-Gendron-Halliday-Sachrajda 1981, Andrasi et al. 1981, Landshoff-Stirling 1982, Zhou-Yan-Zhang-Li (CTP 74 (2022) 115202), Forshaw-Kyrieleis-Seymour 2006, Forshaw-Seymour-Siodmok 2012, Catani-de Florian-Rodrigo 2012, Becher et al. PRL 134 (2025) 061901, Boer et al. SciPost Phys. 3 (2017) 040, Buffing-Mulders PRL 112 (2014) 092002, Chang-Li PLB 726 (2013) 262 and Li PRD 106 (2022) 014029. Compare the Zhou et al. EFT cancellation argument with CMP and REG, and assess the Chang-Li claims in the TMD section.

### [required_fixes 10]
F10: in CMP and LIT, DGOPS is arXiv:1510.08696 (only v1 exists); remove 'v2'.

### [required_fixes 11]
F11 (process; must be done by the parent session, since subagents cannot): write verify/extend/X1-glauber/REPORT.md from journal line 101 (agent a4cf5517baa9f46e2), write review_r1_1.md and review_r1_2.md from journal lines 80 and 78 (my review_r2_1.md is already on disk), do the same for X2 and X3, and add to the workflow's extend() a check that saves the returned text whenever REPORT.md is missing.
