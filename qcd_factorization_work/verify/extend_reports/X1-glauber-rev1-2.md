# X1-glauber-rev1-2

(extracted verbatim from the workflow journal; structured output of the agent)

## overall

fixable_issues

## per_result

### [per_result 1]
PROCESS / INPUT — wrong (workflow defect, not author math). verify/extend/X1-glauber/REPORT.md does not exist: the harness refused the author's report-file write, and the workflow never saved the author's StructuredOutput to disk. X2-subtraction and X3-ope have no REPORT.md either. I reviewed the author's result exactly as recorded in the workflow journal (~/.claude/projects/-Users-hao-cheng-Desktop-theorem-proof/c211c739-.../subagents/workflows/wf_52f29317-58b/journal.jsonl, line 41, agent ad274be466e27b0fa). It is byte-identical to reviewer 1's copy. Under the same subagent policy I did not write review_r1_2.md: this structured output is the review, and the parent must save it. My independent scripts and logs are in verify/extend/X1-glauber/review_r1_2_scripts/ and review_r1_2_logs/.

### [per_result 2]
DEFS — gap (minor). (i) Def 3.2 sets J_sigma = sum_t c_t i^N. With gap factors i/(A+K) and with L3's normalisation (J_A = i/d0 in the scalar model), the consistent definition is J_sigma = sum_t c_t, with no i^N. Used literally, the stated version flips the sign for N=2. (ii) Hypothesis (R) is argued, not proven; it should be listed as an assumption. (iii) (NF_X) is not a mild condition. In the model, alpha_1 > 0 exactly when s_T·k_2T > k_2T^2/2, so NF fails on an O(1) fraction of the spectator transverse-momentum integration domain. This limits every pointwise result that assumes NF.

### [per_result 3]
L1 [R] — correct. Independent check: a brute-force 2-D quadrature at finite eta = 0.35, with single- and double-state gaps and external poles in mixed half-planes, agrees with L1(a) to about 1e-7 (review_r1_2_logs/l1_bruteforce.log). A separate time-space derivation reproduces the N=2 weights in all four sectors FF, BB, BF, FB (regweights.log). Novelty is overstated. The N-order race formula is already in the reference (App E.4.4). The identity sum_sigma w_sigma = 1 is the standard eikonal identity and should be cited. What is new: the half-plane sector-selection rule, exactness at finite eta, and the error bound. 'Replaces E.33(c1)' holds only as an exact identity at fixed k^+, not as a per-graph jet-local rewriting (that fails, by P4).

### [per_result 4]
L2 [R] — correct. Continuity with a kink at a single hyperplane k_e^+ = 0 and discontinuity at the origin are right, and the result legitimately corrects the wording of ERR-S3.

### [per_result 5]
T1 [R_cond] — correct, but adds essentially nothing beyond the reference's E.35 and E.31(iii) (abelian or non-coincident cases). Non-abelian coincident insertions on one spectator that commute form an essentially empty class. Present T1 as a uniform re-derivation, not as a new result.

### [per_result 6]
P1 [R_cond] — essentially correct, with a gap in (b). The bound sum_{l in S} Delta_l^2 <= (sum_m |k_Tm|)^2 needs each SS momentum to be carried by at most one line of each state. That is true for time-monotone routings, such as the scalar model, but a general standard-flow path can cross a time slice several times. Fix: multiply the last term of nu-hat by the maximal number of lines per state. The report should also state that Theta-hat changes the map r_R and enlarges the soft-angle region K_R, which feeds E.44(c).

### [per_result 7]
L3 [R] — correct. My independent localized derivation and the author's test_twoexch_parts2 log both confirm it; the residual differences scale as O(eta).

### [per_result 8]
L4 — (a)–(c) correct; (d) wrong as stated. Each X_e = T_i·T_j is real symmetric in a real tensor basis, because complex conjugation acts on every SU(3) irrep by the same automorphism T^a -> s_a T^a; I checked s_a s_b s_c = -1 for every nonzero f^{abc}. Hence [X1,X2] is real antisymmetric, and Tr(rho [X1,X2]) = 0 for every real colour density matrix. Example: the valence baryon–antibaryon spectator state (eps·eps) gives exactly 0 (colour_halfcoinc.log). A non-zero value requires relative phases between different colour-singlet couplings. The quoted '0.38' is a basis-dependent off-diagonal element; the operator norm on the singlet space is 0.433 for (3b,3b,3b;8) and 0.707 for the other cases. Also, check_halfcoinc_singlets.py crashed (LinAlgError) before finishing; the report does not mention this.

### [per_result 9]
L5 [R] — correct. The Stokes argument on the swept boundary pieces (du_e = 0) is valid and the arcs at 0 and at infinity vanish. NF_B is essential. Contour-angle independence is confirmed: the author's real-contour and rotated methods agree, and my runs at theta = pi/8, pi/4, 3pi/8 agree to 8 digits.

### [per_result 10]
L6 [R] — correct. The ray identity is elementary; I re-derived it, including the -pi*Res/k_p pole term.

### [per_result 11]
T2 [R_cond] — mathematically correct within the two-time model (Lemma E.19 jets, exact connecting propagators). Independent check: my leading-power code, using the author's chi(k^+) regulator, gives Re p_opp = 0.046, 1.8e-3 and 3.8e-5 for K_c/lambda_B = 1e2, 1e4, 1e6. The result is unchanged by an extra analytic cut-off on the A-side k^- integrals provided K·K_c >> k_T^2 (t2_regulator.log). The physical scope is overclaimed. (i) The result is pointwise and holds only where NF_A and NF_B both hold. T2' still needs NF_B, and the case where both fail is open (O2), so nothing is established for the cross section integrated over spectator momenta. (ii) The cancellation comes from the near-mass-shell region |k^+ k^-| ~ k_T^2, which lies outside the Glauber window. Analytic cut-offs that remove that region (K·K_c << k_T^2) give p_opp -> 0.4994, the strict-window value (t2_nearshell.log). So T2 verifies the version of E.33(c2) restricted to G_0 (window plus adjacent near-shell region); it does not show that E.33(c2) is unnecessary. (iii) Without a regulator, the -1/2 in Step 4 is generated at k^+ ~ a/lambda_A, the A-collinear end where E.19(a) is invalid — the same status as the end poles — so the physical claim rests on G7. 'Refutes the reference' should be replaced by 'extends ERR-S1 to LCOPT jets'. Prior art: BFT 1989 already showed the two-loop fully coincident cancellation for eikonal spectators.

### [per_result 12]
T2' — (a) correct for a regulator on k^+ only, given NF_B. (b) The end-pole formula is correct: I re-derived Res(rho_12)/k_p = -a1 alpha1/(a1 alpha1 + a2 |d10|), and the apole numerics (0.2520 against 0.2517) agree. Convergence is slow, like lambda^{1/2}: Re p_opp = 0.028 at lambda = 1e-3. The stated 'mechanism' — a universal -1/4 from each analytic rapidity end — is bookkeeping on the rotated contour and is false in general: analytic cut-offs on both k^± that exclude the near-shell region give no -1/2 at all.

### [per_result 13]
P2 — the result (p_opp = 1/2 in the strict window) is correct and already known. The diagnosis is wrong. The cause is the strict propagator -1/k_T^2, which removes the near-shell region and with it the sign(k^+) sector selection (rho~(0) = 0). Non-analyticity of the cut-off is not the cause: analytic cut-offs give the same 1/2. The reference's own Rem. E.32 and E.49(2) already give the correct diagnosis, so the novelty claim must be withdrawn.

### [per_result 14]
P3 — correct and known in substance: standard Cutkosky two-particle unitarity for distinguishable massive lines, as in ERR-S1.

### [per_result 15]
T3 — the calculation is correct for the unregulated two-time model, but the physics conclusion is wrong or unsupported. My independent leading-power evaluation gives W12 = 0.5 - 0.03056i (author: 0.5 - 0.03069i at lambda = 3e-3) and, for the B-asymmetric set, 0.5 + 0.04682i (author: +0.04679i); Re W12 = 1/2 is exact. Objections: (a) Im W12 comes from |k^+| ~ lambda_B, where the A-side ordering is decided at |k^-| ~ k_T^2/lambda_B ~ Q. That is the B-collinear end, where E.19(b) fails and the commutator part has 1/k^- tails that are not power suppressed. An analytic cut-off chi(k^-) = K^2/(k^2+K^2) on the A-side k^- integrals gives Im W12 = -0.0306, -0.0204, -0.0050, -0.0006, -0.00006 for K = infinity, 1, 0.1, 0.01, 0.001 times k_T^2/lambda_B (t3_regulator.log; independent of contour angle). The residual is therefore power suppressed for any lambda_A << K << Q. By the report's own G7 reasoning it is a collinear-end matching question, not a violation. (b) Its colour factor vanishes for every real colour state (see L4). (c) The family is incomplete. Coincident SA patterns (lines i–j_e and i–b) carry T_b = -sum_j T_j on a colour-singlet hadron B, which is how LRS obtained the two-loop cancellation for a baryon target; these patterns are ignored, so 'only Y graphs can compensate' is unjustified. (d) The result conflicts with the all-order CSS/Collins/DGOPS-2016 argument, which works graph by graph and has no ordering weights, and no error in that argument is identified. LRS NPB 222 (1983) is mischaracterised as having 'at most one spectator per hadron': it treats baryon targets. Withdraw the [V] grade; at most a [P] statement about the unregulated model.

### [per_result 16]
P4 [R] — the conclusion (per-graph weak equivalence with jet-local data fails) is fine. The illustration is imprecise: base and apole do not have 'the same window data', since d0 and nu_A differ. The argument should rest on the O(1) constants fixed by data outside the window.

### [per_result 17]
P5 [A] — plausible and standard: unitarity at three-particle cuts needs the Lipatov vertex, as in BFKL. 'Needed' is relative to the bookkeeping by SS families, not an absolute statement about QCD.

### [per_result 18]
L7 [R] — correct and elementary (affine k^- dependence, distance to the zero >= 2Λ_j). It is a valid reduction of E.33(a).

### [per_result 19]
P6 — qualitative diagnosis with no theorem statement or proof, so the grade [R] is inappropriate. Downgrade to [P] or a remark.

### [per_result 20]
REG — overclaims. G5 is called 'not needed' for fully coincident pairs at O(g^4), which ignores the NF_B requirement, the open case O2 and G7. G5(i) (half-coincident from O(g^4)) is unsupported, by T3 above. G7 is stated for k^+ only; it must be symmetric in k^+ and k^-, and the symmetric version also removes the T3 residual. The register never compares with the CSS/DGOPS graph-by-graph route.

### [per_result 21]
EX / verification — the numerics are reproducible and agree with mine. However, checks_C2_C3_C4.log ends with 'SOME CHECK FAILED' (C3e/C3f, which test the Re-based residual formula). According to the halfcoinc.py docstring that formula was the author's original prediction, not 'deliberately mis-specified'. check_halfcoinc_singlets.py aborted. Script docstrings cite outdated theorem labels (T4, T5). The real-contour code is invalid for the apole and both sets, as the report itself acknowledges.

### [per_result 22]
NOVELTY — the search was limited (titles only). Checked on INSPIRE: Lindsay–Ross–Sachrajda 1982/83 (PLB 117, 105; NPB 214, 61; NPB 222, 189), Brandt–Frenkel–Taylor 1989 (NPB 312, 589), Bodwin 1985, Bodwin–Brodsky–Lepage 1981, Collins–Soper–Sterman 1988 (NPB 308, 833), DGOPS 2016 (JHEP 01 (2016) 076, §4), Liu–Ma arXiv:0802.2973, Gaunt 2014 (arXiv:1405.2080), Ángeles-Martínez–Forshaw–Seymour 2015. Genuinely new: the sector rule and error bound in L1, L2, the P1 construction, the role of L6, T2 for LCOPT jets, and the T2'(b) formula. Not new: the race formula and eikonal identity, T1, P2, P3, and P5 in substance.

## required_fixes

### [required_fixes 1]
WORKFLOW (this is the answer to the user's question '在正常运行吗' / 'is it running normally?'): only partly. The X1, X2 and X3 author reports exist only as StructuredOutputs in journal.jsonl; the harness refuses report-file writes by subagents and the workflow script never writes them to disk. The parent must save each author result as verify/extend/X*/REPORT.md and each review StructuredOutput (including this one) as review_r1_*.md. Otherwise the review and repair stages read missing files.

### [required_fixes 2]
T3: withdraw the [V] grade and the sentences 'genuinely needed already at O(g^4)' and 'Any compensation must carry the three-gluon colour structure'. Restate T3 as a property of the unregulated two-time model. Add: the residual is generated at |k^-| ~ k_T^2/|k^+| ~ Q (B-collinear end); it is power suppressed with any analytic k^- cut-off lambda_A << K << Q (numbers in review_r1_2_logs/t3_regulator.log); its colour factor Tr(rho[X1,X2]) vanishes for real colour states; and the SA-coincident patterns together with colour conservation (the LRS mechanism) were not included. Reformulate O1 accordingly.

### [required_fixes 3]
L4(d): replace 'does not vanish once a fourth spectator is present' by the reality statement: zero for any real colour density matrix (all valence configurations), non-zero only through relative phases between distinct singlet couplings. Quote basis-independent operator norms (0.433 and 0.707) instead of the basis-dependent '0.38'.

### [required_fixes 4]
T2 / T2' / summary item (4) / REG G5: state the scope precisely. The result is pointwise on NF_A ∧ NF_B; T2' needs NF_B; the both-fail case (an O(1) part of spectator phase space) is open (O2), so nothing is claimed for the spectator-integrated cross section. Say explicitly that the cancellation comes from the near-mass-shell region |k^+ k^-| ~ k_T^2: T2 verifies the G_0-restricted form of E.33(c2), not its dispensability. Replace 'refutes the reference' by 'extends ERR-S1 to LCOPT jets'. Cite BFT 1989 for the eikonal two-loop result.

### [required_fixes 5]
P2 and the T2' 'mechanism' paragraph: remove the 'non-analytic truncation' diagnosis and the 'universal -1/4 per analytic end' claim. Use the near-shell explanation (the reference's Rem. E.32/E.49(2)); analytic cut-offs that exclude the near-shell region also give p_opp = 1/2 (review_r1_2_logs/t2_nearshell.log).

### [required_fixes 6]
G7: make it symmetric (analytic regulators on both k^+ and k^-, with K_c^+ K_c^- >> k_T^2 so that the near-shell region is kept) and apply the same rule to T2 and T3. Then move T3 out of G5(i).

### [required_fixes 7]
Add a section comparing the localization framework with the CSS/Collins/DGOPS-2016 graph-by-graph argument (sum over cuts of each forward graph, contour deformation using the exact gluon pole, colour factors constant per graph, so no ordering weights). Either identify a gap in that argument or present all 'E.33(c)-type assumption needed' statements as relative to the framework.

### [required_fixes 8]
Def 3.2: J_sigma = sum_t c_t, removing the stray i^N. List (R) as an assumption. Quantify the NF restriction (e.g. alpha_1 > 0 exactly when s_T·k_2T > k_2T^2/2).

### [required_fixes 9]
P1: add the multiplicity factor (maximal number of lines per state carrying SS momentum) to nu-hat, or require time-monotone routings. State the consequence for r_R and K_R.

### [required_fixes 10]
L1: cite the eikonal identity for sum w = 1 and the reference's App E.4.4 N-order formula. Limit the novelty claim to the half-plane sector rule, finite-eta exactness and the error bound.

### [required_fixes 11]
T1: re-label as a uniform re-derivation of the reference's E.35/E.31(iii). P6: downgrade to [P] or a remark. P4: replace 'same window data' with an argument through constants fixed outside the window.

### [required_fixes 12]
Verification log: report honestly that checks_C2_C3_C4.log ends with 'SOME CHECK FAILED' (C3e/C3f use the author's original Re-based formula) and that check_halfcoinc_singlets.py aborted; fix and re-run it. Update stale theorem labels in the script docstrings. Keep the real-contour code out of the apole and both sets.

### [required_fixes 13]
Literature (O8): correct the description of LRS (NPB 222 (1983) 189 treats meson and baryon targets, and the cancellation needs a colour-singlet target). Engage DGOPS 2016 §4, CSS 1988 and Collins 2011 §14.4 before attaching any 'new' or [V] markers.
