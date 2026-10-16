# X1-glauber-rev3-1

(extracted verbatim from the workflow journal; structured output of the agent)

## overall

fixable_issues

## per_result

### [per_result 1]
RUN STATUS (answer to 「在正常运行吗」): running, but not fully normally. Journal wf_52f29317-58b at 06:11 (133 lines): X1 is in round-3 review (rev3-2 finished at line 132; this is rev3-1, line 126); X2 has finished both round-3 reviews (lines 131, 133); X3 has finished fix 2 (line 128) and is in round-3 review (lines 129-130). Results are still not saved to disk: verify/extend/X1-glauber/REPORT.md, review_r1_1.md, review_r1_2.md and review_r2_2.md do not exist, and neither do the REPORT.md files of X2 and X3. I reviewed the X1-glauber-fix2 structured result (journal line 125). My review is written to verify/extend/X1-glauber/review_r3_1.md; scripts and logs are in review_r3_1_scripts/ and review_r3_1_logs/.

### [per_result 2]
DEFS — correct. The class-X example is right, and the scalar covariant J^[12] equals the sum of its three LCOPT sectors with c = i/d0. Hypotheses listed in DEFS but shared by several statements are registered premises (see REG).

### [per_result 3]
L1 [R] — correct as corrected. The telescoping bound N 2^{N+1} M_sigma (lam/kappa) prod|K_l|^-1 holds, including the multi-state step (2lam/kappa <= 1). The closed-quadrant lemma holds (pairwise Re z_i conj(z_j) >= 0), hence sum|w| <= nF! nB!. The Glauber case is unchanged.

### [per_result 4]
L1' [R] — correct. Example weights re-derived by partial fractions; sum rule holds; c_U = 1.64853 reproduced from scratch. The closed-quadrant placement holds for every theta in [0, pi/2]; theta <= pi/4 only avoids the pole collision at pi/2.

### [per_result 5]
L2, L3, L6 [R] — correct (unchanged). L6 re-derived by Cauchy with [rho - (1+k)^-1]/k.

### [per_result 6]
T1 — correct as a re-derivation of Props E.35/E.31(iii).

### [per_result 7]
P1 [R_cond] — correct. Notational gap: x^A_min is defined as min l^+ (a momentum), so 'x_min >= c' must read x_min >= c P_A^+ (or x must be a fraction). The proof of (b) is verified.

### [per_result 8]
L4 [R] — correct. (b) re-derived: the X1X2 coefficient is c1c2(1 - W21 - W12*) = 2i c1c2 Im W12. (c) re-derived: the two terms cancel on the (i, j1, j2) singlet. The CdFR context is verified in arXiv:1112.4405 eqs. (186)-(190): the operator is ∝ f T1T2T3 for n = 4 but its contribution to P^(2,R) vanishes by colour conservation, starting at n >= 5. (Precision: the operator itself does not vanish at n = 4.)

### [per_result 9]
L5 [R] — correct; the proof is now complete. Re-derived: the radial identity; kappa.n = 0 on the half-axes; no gap factor vanishes for t in [0, pi/2] at eta > 0; |A + i(eta - y)| >= <y>/sqrt5 for eta <= mu; the arc decay.

### [per_result 10]
L8 [R] (new) — correct and robust. My test on GENERAL non-factorized (Sp') jets (hexagon orbits, winding cycles, two-chains with multi-state shared gaps, isolated terms) gives max lhs/bound (b) 0.52, (c) 0.025, (d) 0.044, (e) 0.42 at theta = pi/2, and 0.46 / 0.008 / 0.012 / 0.09 at pi/4 with constants x8. g12 = g21 to 3e-12; int g and int S reproduce -i Jcal and -Jcal. A counter-test with (Sp') broken leaves the 1/kappa2 strip tails uncancelled, so (Sp') is necessary as stated. Minor: in (c) the axis-band intermediate constant is 16/9 + 1, not 2; the final constant 9 still holds.

### [per_result 11]
T2 [R_cond] — mathematically correct for the UNCUT side sum. Steps 0-7 re-derived (normalisation, S/T/O partition, E1-E8, K-choice conditions, imaginary v-term, L6 giving -1/2 per mixed sector). End-to-end numerics with my own integrator: it reproduces the scalar values (0.0123468, 0.0020501, 0.0003476 against 0.0123471, 0.0020476, 0.0003448), and for three NON-factorized jet pairs (one J_A violating (Sp')) Re p_opp -> 0 roughly ∝ eps^0.7, N/N0 -> 1, Im slope 0.72-0.73 per decade (theory 0.733). GAPS: (i) delta_Y <= 1/2 is used but not implied by eps <= eps_0; (ii) C_c is not explicit and brings ln(lam_B/mu_B) into C_T; (iii) the rate of the Im p_opp expansion is not derived. PHYSICAL READING OVERSTATED: G0 contains cut direct lines (Def. E.1(e) 「可以被割」) and E.33(c2) includes real emission (「含实发射」), but T2 omits cuts through the SS gluons. By power counting these are O(N0) in the unregulated H_glob model (from the collinear ends) and power suppressed only with two-sided G7 regulators. So 'the G0-restricted E.33(c2) HOLDS' is not established.

### [per_result 12]
T2' — (a) correct: rho~ is holomorphic and real; the end-pole residues are suppressed by (K_c lam_A/a)^2; the rate follows with K = (lam_B K_c)^1/2. (b) correct (residue re-derived), but 'jet B's poles give the same by symmetry' can only be the mirror statement under NF_A. (c) [P] is consistent; its real-part statement concerns uncut lines (see T2).

### [per_result 13]
P2 [R] — correct. Reproduced: the eikonal three-sector identity, the PV formula, the sharp-window delta, and 97/105 and 43/455 by exact residues. Gap: p_opp = 1/2 + 2 dA dB needs a fixed B-side orientation (with the opposite one it is 1/2 - 2 dA dB), and 'defined in the same way' does not fix it.

### [per_result 14]
P3 — correct (unchanged).

### [per_result 15]
T3 — (a)-(c) correct; (d) and (f) [P] reproduced earlier; (e) correct in substance. Verified from scratch: v_K linear term (x1 - x2)/4 in all quadrants, sup|v|/(|x1|+|x2|) = 0.25, sup|v| = 0.5, remainder 0.0441, c_U = 1.6485. WRONG TERM: the stated second term (lam_A/K)(1 + ln(1 + K/mu_B))^2 is not boost invariant (K is a k^- scale, mu_B a k^+ scale); the proof gives ln(1 + a_min/(K mu_B)). The interpretive sentence 'not determined by any window' says more than the bound proves. The cut-line scope issue of T2 applies to T3 as well.

### [per_result 16]
P4 [R_cond] — (a) and (c) correct; the result of (b) is correct but one stated reason is FALSE. The added 1V2 term has a single-state final gap, so (Sp') needs a partner in sector 12V; without it, J_A leaves the (Sp') class (my structural check: False). Adding the partner restores (Sp') and changes dW(12,21) only at power level (-7e-5 i and -1.6e-5 i against +0.0078i). The (b) shift formula is independently confirmed (+0.007838i predicted, +0.00785i computed).

### [per_result 17]
P5 [A] — conclusion acceptable; the identity is WRONG. A three-particle cut of a class-C graph cuts a rung with its two ends on opposite sides of the cut, so D_C = int dPhi3 [A_A^dag A_B + h.c.], not int |A^lines|^2. 'Sum of B^dag B terms' is therefore no reason for positivity. Positivity holds in Feynman gauge for eikonal lines through the common colour operator: C^dag C · 2vA.vB/((vA.k)(vB.k)). D_C is gauge dependent, and D_C != 0 survives.

### [per_result 18]
L7 [R] — correct as corrected.

### [per_result 19]
Remark P6 — acceptable as an ungraded remark.

### [per_result 20]
REG — the asm mapping is verified in spec_v2/ASSUMPTIONS.md. ERRORS: (i) it misreads register rule 00.1-1: (Sp'), (R), NF and (H_glob) are unproven R_cond premises shared by several statements, so they must be registered or recast (model or domain definitions, lemma hypotheses as in §6); (ii) the 'not needed, but conditionally' entries for coincident O(g^4) patterns ignore cut SS lines; (iii) 'G5(ii) (shown, P5)' should read 'argued [A]'. Each [R] also needs exactly one WRITER_SPEC qualifier.

### [per_result 21]
CMP — accurate on DGOPS and on Aybat-Sterman (eq. (10) 'holds for fixed color orderings'; the paper 'outline[s]' its argument; verified). For Zhou et al. (verified in v2): the 'not strict proofs' caveat applies only to the graphical Sec. VI, while the operator-level argument is presented as proved; A-_G is treated along a second direction n_f^- (eqs. (85)-(86)), so 'one unitary U_{+G}' covers the A+_G (all SS) sector only.

### [per_result 22]
TMD [C] — appropriate. The Chang-Li Nambu-Goldstone argument and Li 2022's k_T-factorization single-phase fit are confirmed from the abstracts.

### [per_result 23]
EX — accurate. t3e_sensitivity.py (iv) prints hard-coded round-1 values rather than recomputing them, and its ALL PASS criterion is weak.

### [per_result 24]
LIT — bibliographic data correct: 21 entries checked on INSPIRE, including Zhou et al.'s two unlinked records. Novelty: no prior statement of T2 (general LCOPT), T3, P1, P2(b), P4 or L8 was found. MISSING: Barcaro-Gao-Gaunt-Pathak, arXiv:2607.14259 (July 2026), on Glauber pinches and Reggeization in space-like collinear limits (context for L4 and the T2 reggeization remark; it pre-empts nothing).

### [per_result 25]
ERRATA ERR-S1b — valid in substance; the quotations are verbatim (refdoc lines 11816, 11862, 13014). Over-scoped: correction (ii) holds only for the uncut direct lines, since G0 and E.33(c2) include real-emission cuts. It should also acknowledge that Rem E.32 and E.49(2) already name the near-shell mechanism; the reference's actual error is the expectation that this mechanism is insufficient within G0.

### [per_result 26]
REVISIONS / OPEN — every round-2 item of both reviewers is addressed, and O1-O12 are honest. Add O13 (cut / real-emission contributions of the direct SS lines under two-sided G7) and extend O1/O6 accordingly.

## required_fixes

### [required_fixes 1]
F1 (scope). In T2, T2', T3, ERR-S1b and REG, state that the side sums contain only SS lines lying wholly on one side of the final-state cut (Def. E.30), whereas G0 (Def. E.1(e)) and E.33(c2) (「含实发射」) also contain cuts through the direct SS gluons. Restrict 'the G0-restricted E.33(c2) HOLDS' and ERR-S1b(ii) to the uncut lines. Then either add a lemma that the cut contributions are O(1) in the unregulated H_glob model (from the collinear ends) and O(lam_B K^-/a + lam_A K^+/a) with two-sided G7 regulators, or record this as a new open item O13.

### [required_fixes 2]
F2 (P4(b)). Delete '(Sp') (no single-state gap) unchanged'. Either add the 12V partner s c2 [i/(A1+k1)][i/(A2+k1)][i/(A''+k1+k2)] and state that it shifts W(12,21) only by O(lam_A K/a + lam_B/K) (verified numerically), or state that the class imposes (Sp') on J_B only.

### [required_fixes 3]
F3 (P5). Replace the identity by D_C = int dPhi3 [A_A^dag A_B + h.c.]. Justify positivity in Feynman gauge (eikonal lines) through the common colour operator, note that D_C is gauge dependent, and drop 'sum of B^dag B terms'.

### [required_fixes 4]
F4 (T2). Add the hypothesis delta_Y <= 1/2 (or build it into eps_0). Write C_c explicitly and state that C_T depends on ln(lam_B/mu_B). Either derive the rate in 'Im p_opp = -(1/pi) ln(1/eps) + c + O(...)' or weaken it to + O(1).

### [required_fixes 5]
F5 (T3(e)). In the second term of the bound replace ln(1 + K/mu_B) by ln(1 + a_min/(K mu_B)). Reduce the interpretive sentence to the proved sensitivity statement.

### [required_fixes 6]
F6 (REG). Under rule 00.1-1, register (Sp'), (R), NF and (H_glob), or recast them following the §6 precedents. Change 'G5(ii) (shown, P5)' to 'argued [A]'. Give each [R] statement exactly one WRITER_SPEC qualifier.

### [required_fixes 7]
F7 (P2). Fix the B-side orientation in the definition of delta_B, since the sign of the 2 dA dB term depends on it.

### [required_fixes 8]
F8 (P1). Write x^A_min >= c P_A^+, or define x as a momentum fraction.

### [required_fixes 9]
F9 (T2'(b)). Restate 'jet B's poles give the same by symmetry' as the mirror statement under NF_A; the case with NF dropped on both jets stays O2.

### [required_fixes 10]
F10 (CMP, Zhou et al.). Say that the caveat 'should not be viewed as strict proofs' applies to their graphical Sec. VI only, and that the A-_G sector is treated along a second direction n_f^- (eqs. 85-86).

### [required_fixes 11]
F11 (LIT). Add Barcaro-Gao-Gaunt-Pathak, arXiv:2607.14259 (2026).

### [required_fixes 12]
F12 (L8(c), minor). Correct the axis-band intermediate constant from 2 to 16/9 + 1; the final constant 9 is unaffected.

### [required_fixes 13]
F13 (process; parent session). Write journal line 125 as verify/extend/X1-glauber/REPORT.md. Save lines 80, 78, 111 and 132 as review_r1_1.md, review_r1_2.md, review_r2_2.md and review_r3_2.md (review_r3_1.md is written). Do the same for X2 and X3, and add to extend() a check that saves the returned text whenever REPORT.md is missing. Apply F1-F12 when patching the spec, since round 3 is the last.
