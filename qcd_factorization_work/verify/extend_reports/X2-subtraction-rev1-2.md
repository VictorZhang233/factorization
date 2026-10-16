# X2-subtraction-rev1-2

(extracted verbatim from the workflow journal; structured output of the agent)

## overall

fixable_issues

## per_result

### [per_result 1]
PROCESS (this answers your question '在正常运行吗' / 'is it running normally?'): not at this step. The file /Users/hao-cheng/Desktop/theorem proof/qcd_factorization_work/verify/extend/X2-subtraction/REPORT.md does not exist. The X1-glauber and X3-ope reports are missing too. I polled for 30 minutes (23:14 to 23:44 EDT) and none appeared. Cause, read from the extender transcript ~/.claude/projects/-Users-hao-cheng-Desktop-theorem-proof/c211c739-758d-4b40-bbac-67f4e1a65da4/subagents/workflows/wf_52f29317-58b/agent-ad47b382e8e1e17ed.jsonl: at 2026-10-10T23:34Z the extender tried to Write REPORT.md and was refused with '<\tool_use_error>Subagents should return findings as text, not write report files<\/tool_use_error>'. It then returned the report in its StructuredOutput (21 results and 10 open items). The workflow script factorization-verify-and-extend-wf_52f29317-58b.js (function extend()) never writes that output to disk; it launches the reviewers against the missing file anyway. All six round-1 reviewers therefore point at nonexistent files, and the fix rounds will hit the same block. I reviewed the recovered content instead: the StructuredOutput, plus a truncated draft that covers only §0 to §2.5 (23.8k characters). Copies are in /private/tmp/claude-501/-Users-hao-cheng-Desktop-theorem-proof/c211c739-758d-4b40-bbac-67f4e1a65da4/scratchpad/rev_x2/ as X2_structured_output.json and X2_REPORT_attempted.md. The draft is stale: its §0 item 3 and status-table row 3.4 still say exponent 1 is optimal, a claim the extender later retracted. For the same policy reason I did not write review_r1_2.md. This StructuredOutput is the review.

### [per_result 2]
X2-Thm2.6 (fibered subtraction theorem), verdict: CORRECT as a formal statement, with a GAP. The proof is valid: residue sums are linear, identity (D.10) holds fiberwise, and summing over a finite cover with the triangle inequality gives the bound. It is only a reformulation, however. The gap: the theorem bounds I_Gamma minus the sum of the base integrals of rho_{C_R}, and those base integrals are taken as the definition of the subtraction-term values. A lemma is needed to identify them with the 4D dimensionally regulated values in which each denominator keeps its own i0, since those are the values that become operator matrix elements. The lemma would use Fubini at finite eta and d=4-2eps, then dominated convergence as eta goes to 0. Alternatively the values must be declared fibered and checked against the covariant ones; this check exists for the triangle in prop:appN-triangle-exact(b),(e). The error type is called 'E-F', but in the spec E-F means a bound pointwise in the remaining variables. This is an L1 norm on the base, so it needs a new label such as E-N^phi. Caveat (a) is right: literal (H3) on the real contour fails already for Gamma, with a ln(1/eta) divergence. But our spec already uses a deformed contour Omega (def:appN-integrand), so this corrects the reference document, not our spec.

### [per_result 3]
X2-Lem2.8 (tropical LP certificate), verdict: CORRECT, with a TOOLING GAP. I checked the citation: Borinsky arXiv:2008.12310 Thm 8.A/8.B say what is claimed. The proof works because, for a concave piecewise-linear psi_a, a bounded argmax face forces strictly negative slopes in every recession direction of U; superlevel sets are then bounded and the Laplace estimate holds. The exact pipeline does not certify face boundedness. It relies on recession.py, and recession.cone_rays is wrong for half-plane cones: cone_rays([([-1,0],0)]) returns [(0,1),(0,-1)], so no interior direction is ever tested. For the cell 'r u>1' (t4w) the script reports slope -1, but sampling the full cone gives a true maximum of -1/2 at direction (1,1)/sqrt2. Cells r_I and r_II are not checked at all; their true maxima are -1/2. All values are still negative, so the bounds hold, but the certificate as coded is incomplete. On uniformity in eps: convexity of the LP value fixes the exponent. Uniform constants follow from kappa^{-eps} <= 1 + kappa^{-eps0}, which should be written down.

### [per_result 4]
X2-Lem2.10/Cor2.11 (light-cone positivity), verdict: CORRECT. I re-derived it. In (a) every energy denominator is at most E_st, which is negative. In (b) one gets |E_st - sum| >= (m^2 + Q^2(1/xi - 1/x))/(2p^+); the stated bound carries an extra factor xi, so it is weaker but still valid. Citations checked on INSPIRE: Chang–Yan PRD 7 (1973) 1147 and Ligterink–Bakker PRD 52 (1995) 5954. The technique is standard and equivalent to positivity of the Symanzik F polynomial when all invariants are spacelike, so it is new only as an application. 'Without self-energy subgraphs' should also exclude tadpoles.

### [per_result 5]
X2-Lem2.12 (1D rung-kernel reduction), verdict: CORRECT. I re-derived it: d^4 l = pi^2 |l|^2 d|l|^2 and |l|^2 = (1-z)(t - zv). The result is trivial.

### [per_result 6]
X2-Prop3.1 (triangle fibered densities), verdict: CORRECT. I re-derived all five densities independently, taking residues propagator by propagator with C_H expanded into four 1/Dg terms (scratchpad dens_check.py). The ratio to the normalized forms in t4 is exactly 1 for 0<u<1 and for u>1, and Gamma vanishes for u>1. I also checked the normalization factor (mu^{2eps}/Gamma(1-eps)) kappa^{-eps}. (H3) holding for C_R when 0<eps<1 is correct.

### [per_result 7]
X2-Prop3.2 (negative-k+ sliver), verdict: CORRECT. Analytically, the kappa integral of rho_{C_C2} is ln(a/(a-w))/(PP'w), and the w integral then gives Li2(1)/(2PP') = zeta2/Qt^2 exactly. My independent quadrature (scratchpad norm_fast3.py) gives the integral of rho_Gamma over the sliver as 1.642936, 1.644734, 1.644914, 1.644932, and the integral of r over the sliver as -1.99786, -1.99979, -1.99998, -2.00000 times lambda^2, for lambda^2 = 1e-3 to 1e-6. The observation is new but elementary.

### [per_result 8]
X2-Thm3.3 (triangle CS1/CS2 at the sharp exponent, natural cover theta=2), verdict: CORRECT in substance, with MINOR GAPS. (i) The certificates for eps0 > 0 were run only for theta=1 (t4). I ran the theta=2 cover at eps=0.1 and 0.2 with the floating LP of t4 (scratchpad theta2_eps.py). The worst exponents are lambda^1.6 and lambda^1.2, i.e. 2 - 4eps, which matches the claim. These runs still need exact duals and must be added to the evidence. (ii) The half-plane recession bug described for Lem 2.8 affects 'r u>1'. (iii) Direct numerics (scratchpad cs_check.py) confirm the certified exponents. At theta=1: (CS1)_S scales as lambda L, C_C1 on U_S as lambda, H on U_S as lambda^2. At theta=2: G-S, C_C1 and C_C2 on U_S scale as lambda^2, H as lambda^4, and (CS1)_C2 as lambda^2 L. The lower bound 'integral of C_C1 over U_S >= s/4' is correct.

### [per_result 9]
X2-Thm3.5/Prop3.6 (triangle remainder: norm versus integral), verdict: CORRECT. My independent computation uses the closed rational form of r, separate v and sliver parametrizations, and Gauss-Legendre panels in log variables. It reproduces the exact Usyukina–Davydychev remainder to within 6e-15 relative. It gives the L1 norm of rho_r as 26.1926, 35.8384, 45.2419, 54.5289 times lambda^2 for lambda^2 = 1e-3 to 1e-6, i.e. 3.79 to 3.95 lambda^2 L; this matches t2b. The rigorous bound lambda^2 L^2 follows from Thm 3.3.

### [per_result 10]
X2-Thm3.9 (bubble-chain / log-insertion class), verdict: GAP. (a) The item certificates (t17, t17x, t17y) cover only U_S, U_C1 for 0<u<1 (regions I and II) and U_C2 for u>0. Nothing is certified on U_C1 for 1<u<=2, and nothing on the sliver inside U_C2 for j>=1, where only t5 numerics exist. So 'all items on the natural cover of Thm 3.3' is not proven. (b) Every bubble LP was run at eps=0 (weights [1,1]), so uniformity in eps is not certified. (c) The model puts a 4D-renormalized ln^j(D_g) insertion inside a d-dimensional measure. (H3) for C_R^(j) holds only in that mixed sense and fails at eps=0; this must be stated. (d) t15c claims its unbounded LPs were 'resolved by exact vertex enumeration'. That is logically invalid, because vertex maxima ignore recession directions, and the exponents it prints (-2, -4, -6) are not suppressions anyway. The final chain t15d/t15e/t15f does not use it, but it must be removed. The rectangle rule (Lemma 3.8) and the bounds on |delta|, a and b check out.

### [per_result 11]
X2-Prop3.12 (all one-loop DIS graphs in phi^3_6), verdict: WRONG in part (ii). In d=6 the photon-vertex corrections are log UV divergent and the hard-line self-energy is quadratically divergent, so '(H3) trivial' is false: Gamma is not in L1 uniformly in eps. The remainder (1-T_H)Gamma is also UV divergent at O(m^2) unless the subgraphs are renormalized at integrand level (asm:appN-uv). For the self-energy, in the q^+=0 frame, T_H shifts l^2 by exactly -m^2, giving an m^2 ln Lambda log term and an O(Lambda^2 m^2) term. For the vertex correction, the constant c/eps multiplies S(p+q) - S(p^+q), which is O(m^2). So the bound ∫|(1-T_H)Γ| <= C lambda^2 L must be re-derived for renormalized integrands. Part (i), the ladders, follows from Thm 5.1.

### [per_result 12]
X2-Thm3.13 (massive photon, light-like approximators), verdict: CORRECT. I checked r = (1/G - 1/g0) delta1 delta2 = -M^2 g0/(G t1 h1 t2 h2) using the per-line semilattice. The kappa integral of the 0<u<1 bracket vanishes identically, since both terms equal ln(u/M^2)/(u - M^2). Expanding -M^2 times the integral from 1 to infinity of ln(u/M^2)/(u(u-M^2)) gives -M^2(L+1) - M^4(L/2+1/4), as claimed. The (H3) failure is the known rapidity divergence and must be cited: Jantzen arXiv:1111.2589 §6, which treats the same graph with analytic regulators; Chiu–Jain–Neill–Rothstein PRL 108 (2012); Becher–Neubert EPJC 71 (2011). What is new is only the exact light-like remainder formula.

### [per_result 13]
X2-Prop3.14 (time-like versus space-like rapidity regulators), verdict: WRONG as stated. There is no Landau pinch. At a common zero of G = M^2 - k^2 and h1Y = 2P(k^- - e^{-2Y}k^+), with n_A spacelike, the gradients (-2k^-, -2k^+, 2k_T) and 2P(-e^{-2Y}, 1, 0) can never be antiparallel. That would need k_T = 0 and k^- = -e^{-2Y}k^+, which contradicts h1Y = 0 and makes k^2 < 0, not M^2. The two singular surfaces therefore cross transversally, and the 4D integral stays finite, with at most an absorptive part from the delta(G) delta(n_A.k) term. The k^- contour is trapped only at fixed base points. This produces a simple pole 1/(k^+ - k0^+ ± i0) in the fibered density, which is integrable as a distribution and avoidable by deforming the base contour. What genuinely fails is absolute integrability, i.e. (H3^phi) in this particular fibration. So the following must be rewritten as a limitation of the fibered method: 'genuine pinch of the soft subtraction term', 'extends E1/ERR-M27', and open item O8's 'prove that the pinch contributions cancel'. The time-like analysis and the window numerics Y >= L/2 are fine as [P].

### [per_result 14]
X2-Thm4.1/Prop4.2 (two-loop planar vertex algebra), verdict: CORRECT. t8 checks the soft-first convention exactly. The naive-convention failures are not scripted. I checked two by hand. For (C1C1,HS) the meet is C1S, and on line a2 k2^+ lies in Z_C1S but not in Z_C1C1 ∪ Z_HS^naive. For (C1C1,C2S) the meet is SS, and line a2 fails the same way. The soft-first convention matches Collins' treatment of the Sudakov form factor. This does NOT settle slot X2d, which is about the configuration in rem:appN-abs-edge: a soft line between hard vertices, with gluon polarizations.

### [per_result 15]
X2-Num-2loop, verdict: correctly graded [P]. The quasi-Monte Carlo error bars are unreliable at low sampling. In the t12 n16 run the integral of Gamma is 72.7±3.9 against an exact value of 82.3 (2.5 sigma), and 200.5±12 against 223.9 (2 sigma). Fitted rates such as 31 lambda L, m^2 L^{2.6-3} and -4.7 m^2 L^3 come from four points with 1–5% errors. They are not determinations and should be printed only as indicative.

### [per_result 16]
X2-Lem5.2 (DIS ladders: positive light-cone representation), verdict: PLAUSIBLE but not fully reviewable, because the written §5 is missing. The pieces summarized are standard: top-down pole-side induction, on-shell rungs, and (Com) because the approximators act on distinct factors.

### [per_result 17]
X2-Thm5.1 (DIS ladders, all n, graded [R]), verdict: GAP. The available text does not support [R]. The induction (P1)/(P2), with its case split and constants 64, 3 and 19, is only summarized. Lemma 5.3 is backed only by a numerical check (t19), although an analytic proof is immediate: the S^3 average of 1/(a + b cos θ) equals 2/(a + sqrt(a^2 - b^2)), which is at most 2/a. The model is phi^3_6, not the fermion ladder with Dirac projections of prop:appN-ladder, so slot X2c is not delivered. The bounds hold only at real x >= x0 > 1. That does not give the complex-omega uniformity that prop:disall-two-routes(b) needs. The prior art has to be positioned: the operator-product-expansion proof of moment factorization in the unphysical region (Ch5) and the Curci–Furmanski–Petronzio NPB 175 (1980) mass-singularity factorization.

### [per_result 18]
X2-Prop5.4 (two-element chains), verdict: CORRECT. It is algebra only.

### [per_result 19]
X2-Thm6.1 (all-order conditional Sudakov theorem), verdict: CORRECT as a conditional statement, with a GAP in positioning. Its 'verified' list inherits the gaps of 3.9 and 3.12. Prior art is missing. Bergère–de Calan–Malbouisson CMP 62 (1978) prove asymptotic expansions by multiple Mellin transforms. Also relevant: Semenova–Smirnov–Smirnov arXiv:1809.04325, Poldaru arXiv:2607.26291 (expansion by regions for integrals of positive polynomials), Jantzen arXiv:1111.2589, and Gardi–Herzog–Jones–Ma arXiv:2211.14845 (multiple on-shell expansions commute for Sudakov regions). All invariants are spacelike in model (M1), and in (M2) in the unphysical region, so F is positive and these methods plausibly already give the integrated leading-power region expansion. What is genuinely open is identifying that expansion with Collins' nested subtraction terms and operator definitions, together with integral-norm bounds. O1 and O10 should be reworded accordingly.

### [per_result 20]
X2-Err (corrections to App. D). (a) CORRECT. (b) OVER-GENERALIZED: the fat neighbourhoods of def:method-neighbourhoods and lem:appN-beta are a device for the general envelope argument (lem:method-local-accuracy needs t_R much larger than s_R in (GA3)(iii)). The triangle shows natural covers suffice only when the grouped objects are computed explicitly. (c) Correct for the literal real contour, but it does not correct our spec. (d) CORRECT. (e) WRONG; see Prop 3.14. (f) CORRECT. (g) CORRECT.

### [per_result 21]
X2-Err-own (retraction), verdict: CORRECT and honest. The truncated draft still contains the retracted text in §0 item 3 and status-table row 3.4 and must be purged.

### [per_result 22]
X2-Est (error estimates), verdict: a summary that inherits the issues above. Mapping to the spec slots: X2a is delivered in fibered form ([R] with computer-assisted certificates, after the fixes listed). X2b is NOT delivered in its planned generality: only equal virtualities p1^2 = p2^2 are covered, with no unequal or hierarchical virtualities, no massive internal lines and no gauge numerators, so the fallback stays. X2c is delivered only as a scalar phi^3_6 analogue. X2d remains open. Novelty: none of my INSPIRE searches found prior integral-norm verification of Collins' (CS1)–(CS3). The new content is narrow, though: LP certificates for those specific subtraction conditions. The techniques themselves are known: tropical bounds (Borinsky 2020; Arkani-Hamed–Hillman–Mizera arXiv:2202.12296), light-cone-ordered perturbation theory positivity, and overlap (zero-bin) structure (Jantzen 2011).

## required_fixes

### [required_fixes 1]
F0 (process, blocking): get the extender's StructuredOutput onto disk as REPORT.md. The extender cannot do it itself: the harness refuses subagent report writes. The orchestrator or main session must write REPORT.md, or the script must pass the content inline to reviewers and fixers. Use the final StructuredOutput, not the stale truncated draft. Do the same for X1 and X3. As things stand, every review and fix round works on a missing file and the fixer's write will be refused again.

### [required_fixes 2]
F1: Rewrite Prop 3.14, X2-Err(e) and O8. Space-like regulators produce no Landau pinch: the singular surfaces G=0 and n_A.k=0 cross transversally and the 4D value is finite. The fibered density is not absolutely integrable, so (H3^phi) fails in this fibration only. Remedies are a complex base deformation, a different fibration, or time-like regulators. Drop 'extends E1/ERR-M27'.

### [required_fixes 3]
F2: Prop 3.12(ii). Treat the UV divergences in phi^3_6: log divergent photon vertices and a quadratically divergent hard-line self-energy. Use integrand-level renormalization (asm:appN-uv, (U1)/(U2)). Re-derive (H1)_H for the renormalized integrand, because the unrenormalized (1-T_H)Γ carries O(m^2 ln Λ) and O(m^2 Λ^2) divergences. Delete '(H3) trivial'.

### [required_fixes 4]
F3: Thm 3.9 (bubble class). Certify the sliver for j>=1. Either certify U_C1 for 1<u<=2, or move that set into U_H, where the 60 u>1 remainder cells already cover it. Add exact certificates at eps0 > 0. State the mixed model precisely (4D-renormalized ln^j insertion inside a d-dimensional measure) and what (H3) means for it. Delete t15c's invalid 'resolved by vertex enumeration' and document the corner cell, which t15f handles.

### [required_fixes 5]
F4: Thm 5.1. Write out the full proof: the (P1)/(P2) induction with every constant, and an analytic proof of Lemma 5.3 via the closed form 2/(a + sqrt(a^2 - b^2)) for the S^3 average. Until that is done, grade it as a sketch or [P]. State that it covers phi^3_6 only, does not fill slot X2c (prop:appN-ladder-cs), and does not give the complex-omega uniformity that prop:disall-two-routes needs.

### [required_fixes 6]
F5: Thm 3.3. Add exact certificates for the theta=2 cover at eps0; my floating run gives lambda^1.6 at eps=0.1. Fix recession.cone_rays for half-plane and full-plane cones, by splitting them into quadrants or maximising over the cone cross-section with an LP, then re-run on r_I, r_II and r_III. Add the argument for uniform constants via kappa^{-eps} <= 1 + kappa^{-eps0}. Note that a bounded argmax face of a concave psi already implies negative recession slopes.

### [required_fixes 7]
F6: Thm 2.6. Either add a lemma identifying fibered subtraction-term values with the 4D dimensionally regulated values (Fubini at finite eta, then eta to 0 by dominated convergence), or declare the values fibered and verify them against the covariant values wherever they are used. Rename the error type: the bound is not E-F as the spec defines it.

### [required_fixes 8]
F7: Restrict X2-Err(b). Natural covers suffice where grouped objects are computed explicitly. Fat neighbourhoods remain the device of the general envelope argument.

### [required_fixes 9]
F8: Literature and novelty. Cite and position against: Jantzen arXiv:1111.2589 (especially §6), Bergère–de Calan–Malbouisson CMP 62 (1978), Semenova–Smirnov–Smirnov arXiv:1809.04325, Poldaru arXiv:2607.26291, Gardi–Herzog–Jones–Ma arXiv:2211.14845, Curci–Furmanski–Petronzio NPB 175 (1980), Chang–Yan PRD 7 (1973), Ligterink–Bakker PRD 52 (1995), Chiu–Jain–Neill–Rothstein PRL 108 (2012), Becher–Neubert EPJC 71 (2011), Borinsky arXiv:2008.12310 and Arkani-Hamed–Hillman–Mizera arXiv:2202.12296. Narrow the 'NEW' labels to integral-norm verification of Collins' specific subtraction conditions. Reword Thm 6.1, O1 and O10 to say which part is already covered by the rigorous theory of asymptotic expansions for positive parametric integrals.

### [required_fixes 10]
F9: Map '[R, ca]' onto the monograph's grades: [R, R_PT], with 'computer-assisted' stated in the 地位 field and the scripts archived. Use the names (CS1)–(CS3), not (H1)–(H3). Purge the retracted 'exponent 1 optimal / loses a full power' text from the draft.

### [required_fixes 11]
F10: Two-loop numerics. Give an honest error analysis, since the quasi-Monte Carlo error bars undercover at low sampling. Present fitted L-powers and coefficients as indicative only.

### [required_fixes 12]
F11: Slot X2d. State explicitly that the configuration in rem:appN-abs-edge (a soft line with both ends at hard vertices, gluon polarizations) is unresolved. Prop 4.2 is a separate convention issue. Add a script for the four naive-convention (Abs) failures.

### [required_fixes 13]
F12: Slot X2b. State that only the equal-virtuality triangle is covered. Unequal or hierarchical virtualities, massive internal lines and gauge numerators are not, so thm:appN-oneloop keeps its fallback.
