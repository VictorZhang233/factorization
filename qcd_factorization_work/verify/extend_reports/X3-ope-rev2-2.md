# X3-ope-rev2-2

(extracted verbatim from the workflow journal; structured output of the agent)

## overall

fixable_issues

## per_result

### [per_result 1]
[0] PROCESS / STATUS (answer to 在正常运行吗): only partly normal. Workflow wf_52f29317-58b is running: this reviewer (a845cd28620d1f2f3, X3-ope-rev2-2) and X3-ope-rev2-1 started about 04:03, and X2-subtraction-fix2 is running. But verify/extend/X3-ope/REPORT.md still does not exist: the harness blocks subagent report files, and the orchestrator has not saved the fix agent's output. I reviewed the revised report from the workflow journal (entry 111, agent aa6e04ae9a9fda375, 'X3-ope-fix1': summary, 29 results, 14 open items; extracted to scratchpad/x3rev2_2/X3_REPORT_rev1.md), together with the two round-1 reviews (entries 71, 75). For the same harness rule I did not write review_r2_2.md; this StructuredOutput is the review. I re-ran all six X3 scripts (f1, f2, f3, f4, h1, e1) and each reproduces its stored log byte for byte. My own independent checks are verify/extend/X3-ope/review_r2_2_scripts/rv22_algebra.py and rv22_numeric.py, with logs/; all of them pass.

### [per_result 2]
[1] SLOT OUTCOMES (result 0). X3b 'not passed', X3c 'not delivered' and X3d 'partial': CORRECT. X3e (thm:appM-forward-expansion): PASS CONFIRMED by this round-2 reviewer. Theorem F with Lemmas F.6 and F.7 is a complete per-graph [R, R_PT] proof (items 9-11). This holds only as the per-graph statement: the spec's planned consequence 'hence asm:appM-forward at every order' and the decision rule 'If PASS: asm:appM-forward 已解除' do NOT follow, because asm:appM-forward is only reduced to (A3) + E_eps + Theorem B (Cor F.2 is [A]). The report states this correctly; the spec patch must not apply the planned rule mechanically. X3a 'FAILS as planned': GAP. The circularity argument is right, but the sources the slot exists to check were never read (item 4).

### [per_result 3]
[2] Lemma A.3 (linear independence): CORRECT at fixed generic eps, where every D-dimensional monomial has a non-zero tree vertex, and CORRECT for a 4-dimensional basis. GAP at D = 4 in DR, which is how it is used in (A4). DR generates evanescent operators, for example four-quark operators built from Gamma^(5) (x) Gamma^(5). Their tree vertices are proportional to (D-4): the contraction is -D(D-1)(D-2)(D-3)(D-4), verified with explicit Clifford matrices in D = 4, 5, 6, 7 (rv22_algebra (E)). For them the tree-level injectivity step fails. Irrelevant for twist 2.

### [per_result 4]
[3] Theorem A: the overall grade [A] is honest. (A2) is CORRECT (a finite limit of sum_k c_k(eps)(mu^2/q^2)^{k eps} is a log-polynomial of degree <= r). The (A5) completion is CORRECT: polynomial dependence on ln mu plus Lagrange interpolation, with the inhomogeneous identity-operator term for Phi = empty. GAP in (A4), and hence in (A5), which uses (A4), for the stated 'full MS-bar basis'. From dimension 6 on, starting at two loops in the four-quark sector, the DR basis contains evanescent operators [E]. Their renormalized Green functions start at one loop, so coefficients can be traded between [E] and physical operators: uniqueness fails without an evanescent prescription (finite renormalization a la Dugan-Grinstein / Herrlich-Nierste) or a restriction of the sector. The K2 citations are quoted accurately; I checked them in the downloaded texts. Smirnov CMP 134: the Theorem on p.117 (remainder as a distribution in xi and as a function at non-exceptional Euclidean q, lambda near 0) and the 'may easily maintain' sentence on p.118. Chetyrkin 1701.08627: Thm 7 'given elsewhere', Thm 8 'will be published elsewhere'.

### [per_result 5]
[4] Remark A.6: the logic is CORRECT. I re-derived it: sum(C~ - C')G = R' - N~_a needs N~_a small, which is C.24 itself. But the conclusion that X3a fails and only an identification lemma (O3) can help is PREMATURE. Smirnov CMP 134 p.110, in the X3 author's own scratch copy x3fix/dl_smirnov/s90.txt, says that Zimmermann and Anikin-Zav'yalov [TMF 27 (1976) 425; Ann. Phys. 116 (1978) 135; Zav'yalov, Renormalized Feynman diagrams 1979 / Kluwer 1990] write the Wilson coefficients as Green functions of composite operators whose coefficients 'depend on [rho] nontrivially', so the expansion is not in powers and logs. That is exactly the Zimmermann/frozen-q type of the reference's C~^(a)_O (cf. Ex. C.27). If those works prove the momentum-space remainder bound, C.24 is discharged directly, with no uniqueness or identification step. Llewellyn Smith-de Vries NPB 296 (1988) 991 (abstract: 'extension of a simplified version of Zimmermann's momentum subtraction proof') is another candidate. The X3 report and both round-1 reviews never mention Anikin-Zav'yalov, although R-M26 and A09(5) ('theory class UNVERIFIED') demand it. I could not obtain the texts either (mathnet.ru is unreachable; Springer requires login). The gap-analysis line 'BPHZL ... no C.24-type remainder estimate' is unsupported for the same reason.

### [per_result 6]
[5] Theorem B (BRST reduction): CORRECT as [R, R_cond: E_eps], content grade [A]. No novelty is claimed, which is right. Checked: step 1 (sJ = 0 with DR-WI). Step 2: the non-merged parts give -sum C_O <sO Phi>. Merged terms come only from the non-linear parts of s phi; the linear parts dc and B carry the small momentum and cannot sit in a hard subgraph. Step 3: DR-SD gives <E(q) Phi> with E in the EOM ideal. Step 5: at each order in g0 the coefficient is exactly homogeneous with exponent 3 - d_Y + O(eps) > 1 - a for d_Y <= a+1. Step 6: I checked the LBC citations in the downloaded texts: BBH Thm 7.1 (eq. 7.5), Lemma 8.1 and §8.6 ('class I operators give a basis of H^{0,*}(s,Omega)'); Henneaux hep-th/9510116 (the gauge-fixed Koszul-Tate differential is acyclic on local functions, not on functionals); BHHS hep-th/9910201. The diagnosis of the reference's Prop C.44 matches refdoc R5: the reference keeps only polynomial contact terms pi_Y and concludes sX_d = 0. Minor (i), DR-SD sign: from int D phi delta_L/delta phi(y)[Y Phi e^{iS}] = 0 with the graded Leibniz rule, the factor (-1)^{|phi||Y|} appears in both surviving terms and cancels. So eps_k = (-1)^{|phi| sum_{l<k} |phi_l|}, without |Y|, and the factor (-1)^{|phi||O'|} in E(q) should be dropped. Harmless, because it does not depend on k. Minor (ii): LBC is applied at fixed eps to D-dimensional polynomials; say that it is used in the formal-D tensor algebra (the BBH argument does not depend on the dimension), and link this to the evanescent remark.

### [per_result 7]
[6] Theorem I = A + B + twist classification, graded [A]: CORRECT.

### [per_result 8]
[7] Lemma F.0: CORRECT (-s_T = Q^2(c_q^2 - c_p c_q omega)). It is elementary.

### [per_result 9]
[8] Lemma F.1: CORRECT; I re-derived it. The coefficients lie in the sector |arg| <= arcsin r, and s+m lies in c intP + nP, which is inside (c+n) intP. For the n-th Taylor term the candidate poles are <u,a> - (D/2) d_u + d_u(g) + n delta_u in -N0, with delta_u = d_u(F1) - d_u >= 0. This is a subset of the n = 0 progression, so the candidate poles do not depend on lambda. Wording nit in (c): write G_lambda = x^{m_sigma}(f_{sigma,0} + lambda f_{sigma,1}).

### [per_result 10]
[9] Lemma F.6 (matroid base polytope; discharge of F-DR): CORRECT. Checked logically: deletion-contraction on e_q, the affine bijection pi, Feichtner-Sturmfels Prop 2.3 and 2.4 (read in the text), the four normal types, and d_u = 0 only for e_e. Schultka Thm 3.6 requires the coefficients to lie in an open strongly convex polyhedral cone (read in the text); this holds for every omega in the cut plane. Also checked by an independent brute-force facet enumeration with exact integer verification, using neither qhull nor matroid theory (rv22_numeric (H)): 9 explicit graphs, 2 of them not 2-connected, and 360 random multigraphs with loops and multi-edges, 176 of them full-dimensional. In all of them full-dimensionality holds iff G0 is loopless and 2-connected, every facet normal is a 0/±1 vector of one of the four sign types, and d_u = 0 only for coordinate facets. NOVELTY: known in substance. Schultka 1806.01086 §4 covers Euclidean non-exceptional kinematics, which includes the p = 0 propagator-type integral U + F0: Thm 4.15 (generalized-permutahedron facet presentation), Prop 4.17, Cor 4.18, Prop 4.29 (convergence domain in analytic/DR regularization), and Rem 4.30, which credits Speer 1975. The matroid structure of the U and F supports is in Tellander-Helmer CMP 2023 (proof of Thm 3.1, Lemma 3.3) and Walther LMP 2022. Facet descriptions are in Borinsky AIHPD 2023 Thm 32 and Arkani-Hamed-Hillman-Mizera PRD 2022. The report cites only Schultka §3.

### [per_result 11]
[10] Theorem F (forward on-shell DR amplitude): CORRECT, [R, R_PT] per graph; the cited theorems were checked. (F1): for every omega in the cut plane the coefficient set {1, 1±omega} lies in an open half-plane, including |Re omega| > 1 with Im omega != 0, and the property fails on the cuts. Re-derived: 1 = ((1+omega)+(1-omega))/2 lies in the cone spanned by 1+omega and 1-omega, whose opening angle is below pi; also checked on a grid (rv22_numeric (F)). (F2) follows from Lemma F.1 and a contour argument in D. (F3): I re-derived the block-cut-tree argument; every branch outside the q-block carries net momentum 0 or ±p, so it depends only on p^2 = 0. Exclusion (ii) holds graph by graph without target averaging: the side of a zero-momentum bridge that does not contain the target, or the tadpole side, has a single adjoint index. Wording: replace 'Wick rotation is legitimate' by: the Minkowski parametric form has (F - i0), and F > 0 on the orthant for real |omega| < 1, so the i0 is immaterial. The status must be narrowed. Theorem F proves the analytic step of the method of projectors: the on-shell DR amplitude equals its convergent naive Taylor series. The IR/UV 'rearrangement' that LNvRV mention, i.e. the identification with MS-bar coefficient functions, is Cor F.2 and stays [A]. NOVELTY: I found no prior proof of the analytic step. INSPIRE full-text 'method of projectors' gives 48 records, of which 14 also match 'proof'; none contains such a proof. GLT 1983, GL 1987 and Gorishny 1989 are Euclidean large-momentum expansions (abstracts). The key inputs (holomorphy of Euler-Mellin integrals in the coefficients per Nilsson-Passare/BFP, and Schultka) are standard. So '本书给出的严格证明' is justified; '本书新结果' only after an extended §6.5 literature check.

### [per_result 12]
[11] Lemma F.7 (T2 projection in D dimensions): CORRECT. (a): I re-derived the projector from a general tensor with left and right transversality (rv22_algebra (A)). (b): the remark 'the general case is the same linear algebra' is unnecessary. Since T2 = beta_n nu^{n-1}, only n = 0 and n = 1 can give a non-positive power of nu. Hand proof: for n = 0, T is proportional to Q^2 g + qq, so (D-1)S1 - (nu^2/Q^2)S2 = 0. For n = 1, transversality kills the pq and qp terms and forces T = a nu g~, so T2 = 0. Verified symbolically for the most general transverse polynomial tensor, n <= 4 (rv22_algebra (B)). (c) is correct. At tree level T2 is independent of D and equals the report's 4w/(1-w^2) up to the overall sign convention of T (C). The d_ab properties are confirmed (D).

### [per_result 13]
[12] Corollary F.2 (forward partonic OPE): the logic is CORRECT and the grade [A] is correct. The forward graphs are exactly the AI graphs, because a bridge of G0 = G + e_q carries 0 or ±p. Step 3 follows from Joglekar-Lee. (b): the constants are valid and can be sharpened to |omega| <= 2p0/|q| and |Phat|_E <= sqrt2 p0 (rv22_numeric (G)); the Cauchy-tail powers are correct. Step 4 (aliens) is correct in DR, because the d_ab-contracted tree vertices vanish and all on-shell loops vanish. It should cross-reference CLAIMS R-M24 (the forward on-shell alien caveat) and state that the physical polarization sum is essential. Suggested upgrade: gluon regularity at omega = 0 can be proved without Theorem B. The exact on-shell BRST Ward identity gives p_a M_n^{ab} eps_b = 0 for every eps with eps·p = 0 (longitudinal states are both BRST-closed and BRST-exact). Hence p_a M_n^{ab} = alpha_n p^b with alpha_n = (q·V_n)/nu a polynomial, so d_ab M_n^{ab} = -g_ab M_n^{ab} + 2 alpha_n is polynomial and Lemma F.7(b) applies. This would make Lemma F.7(c) and Cor F.3(a) [R, R_PT] for gluons.

### [per_result 14]
[13] Corollary F.3: CORRECT as now graded. (a) is [R] for quarks; for gluons it is via F.2 [A] unless the Ward-identity route above is added. (b) and (c) are [A]. The withdrawal of the one-loop all-n claim is right.

### [per_result 15]
[14] Examples F.3 and F.4: CORRECT. f2 reproduces its log. I checked analytically that F = Q^2 x2 (x3 + (1-omega) x1) and that each term has the pole -1/((n+1) eps) at a_i = 1.

### [per_result 16]
[15] Remark F.5: the grade [A] and the wording 'indicates, pending O10' are appropriate.

### [per_result 17]
[16] Lemma 4.10: CORRECT as a logical statement.

### [per_result 18]
[17] Lemmas 5.1-5.5: CORRECT. For 5.1 I re-derived that Phat^2 >= M^2/4 iff |omega| <= sqrt3 M/Q.

### [per_result 19]
[18] Prop 5.6 (dispersion relation): CORRECT; step 6' closes the round-1 gap. Checked: the first-order local wedge is |eta_Q + 2x eta_w| < 2 sqrt(x^2+Q^2) eta_w, and the exact 4D approach (x+i eta, Q^2+eta^2-2ix eta) gives Im s = 0, so it lies inside (rv22_numeric (W)). Disintegration with weak continuity then gives positivity and support on every slice. The normalization in (d) checks: a free quark gives 4w/(1-w^2). Minor: in (w, Q^2) the 4D approach is a curved approach whose direction depends on x, while Hörmander Thm 3.1.15 is stated for straight approaches. One line is needed: either continuity of the K-fold primitive on the closure of the local wedge in compact subcones, or invariance of boundary values under the real-analytic change of variables (w, Q^2) <-> (q0, |q|^2).

### [per_result 20]
[19] Theorem 5.7, Prop 5.8, Theorem 5.9 and Theorem M: CORRECT as conditional statements; unchanged since round 1, and the round-1 checks stand.

### [per_result 21]
[20] E1-E6: CORRECT. I re-derived the E3 recursion and its H_{k-1} b0 d1 term (b0 = beta0/4), and the E4 integral D = R0[1 + kappa (pi/2)(Q/Lambda) e^{-Q/Lambda}].

### [per_result 22]
[21] Verification log: CORRECT. All six scripts reproduce their logs byte for byte. f3 is a genuine check (qhull facets, then exact integer verification), not a circular one. The documentation fixes requested in round 1 are present in f1, f2 and e1.

## required_fixes

### [required_fixes 1]
1. Slot X3a, Remark A.6, O3 and gap analysis. Record X3a as 'not delivered': the uniqueness route is circular (Remark A.6, correct), and the direct route was not examined. Read, or explicitly list as unread, Anikin-Zav'yalov TMF 27 (1976) 425 [doi 10.1007/BF01028628] and Ann. Phys. 116 (1978) 135, Zav'yalov 1979/1990 (chapter on Wilson expansions), and Llewellyn Smith-de Vries NPB 296 (1988) 991. By Smirnov CMP 134 p.110 these use Zimmermann-type coefficients with rho-dependence, the same type as the reference's C~^(a)_O. A momentum-space remainder theorem there would discharge C.24 with no identification lemma. Put this first in O3, keep CLAIMS A09(5) open, and remove or qualify 'BPHZL ... no C.24-type remainder estimate'.

### [required_fixes 2]
2. Theorem A (A4)/(A5) and Lemma A.3 at D = 4; the same caveat applies to the spec's lem:appM-uniqueness(b) and prop:dis-ope-euclid. Add the evanescent-operator hypothesis. In DR, from dimension 6 on, starting at two loops in the four-quark sector, the basis contains operators whose tree vertices are O(D-4) (Gamma^(5)(x)Gamma^(5): contraction -D(D-1)(D-2)(D-3)(D-4), rv22_algebra (E)). Uniqueness then fails. Either state (A1)-(A5) for a 4-dimensional basis with a fixed evanescent prescription, or restrict (A4)/(A5) to sectors without evanescent operators (twist 2; dimension <= 5), and note that the DIS and twist-2 results are unaffected. Also state that LBC in Theorem B is used in the formal-D tensor algebra.

### [required_fixes 3]
3. Spec patch for X3e. Record PASS for thm:appM-forward-expansion only as the per-graph statement (Theorem F + Lemmas F.6, F.7, [R, R_PT]). Do NOT apply the planned rule 'asm:appM-forward 已解除': asm:appM-forward is reduced to (A3) + E_eps (+ Theorem B), Cor F.2 is [A], and prop:dis-ope-forward stays [A]. Reconcile Cor F.2 step 4 with CLAIMS R-M24: the aliens drop because the d_ab-contracted tree vertices vanish and DR on-shell loops are zero; this needs the physical polarization sum.

### [required_fixes 4]
4. Novelty labels. Lemma F.6 is known in substance: Schultka 1806.01086 §4 (Thm 4.15, Prop 4.17, Cor 4.18, Prop 4.29, Rem 4.30 crediting Speer 1975); Tellander-Helmer CMP 2023 (Lemma 3.3); Walther LMP 2022; Borinsky AIHPD 2023 Thm 32; Arkani-Hamed-Hillman-Mizera PRD 2022. Cite these, change 'tools standard, application ours' to 'known; re-derived in matroid form for the Lee-Pomeransky polytope', and drop Lemma F.6 from any 本书新结果 candidacy. Add these works, plus Nilsson-Passare / BFP (holomorphy in the coefficients), to the WRITER_SPEC §6.5 second check for Theorem F. Narrow Theorem F's status to 'rigorous proof of the analytic step of the method of projectors (the on-shell forward DR amplitude equals its convergent naive Taylor series, |omega| < 1)'. The IR/UV rearrangement, i.e. the identification with MS-bar coefficient functions, is Cor F.2 and stays [A].

### [required_fixes 5]
5. Theorem B, DR-SD signs. With the left derivative and the graded Leibniz rule, eps_k = (-1)^{|phi| sum_{l<k} |phi_l|}, without |Y|. Drop (-1)^{|phi||O'|} from E(q), or state the ordering convention that produces it. The conclusion is unaffected.

### [required_fixes 6]
6. Lemma F.7(b). Replace '(f4 b, n <= 8; the general case is the same linear algebra)' by the observation that only n = 0 and n = 1 can give non-positive powers of nu. Add the three-line proof: for n = 0, T is proportional to Q^2 g + qq; for n = 1, transversality forces T = a nu g~. Both give T2 = 0.

### [required_fixes 7]
7. Prop 5.6 step 6'(ii). The 4D approach is curved, with an x-dependent tangent (1,-2x) in (w, Q^2). Justify the identification beyond Hörmander Thm 3.1.15, either by continuity of the K-fold primitive on the closed local wedge in compact subcones, or by invariance of distributional boundary values under the real-analytic change of variables (w, Q^2) <-> (q0, |q|^2).

### [required_fixes 8]
8. Wording. Lemma F.1(c): write G_lambda = x^{m_sigma}(f_{sigma,0} + lambda f_{sigma,1}). Theorem F definition: replace 'Wick rotation is legitimate' by 'the (F - i0) prescription is immaterial since F > 0 on the orthant'. Exclusion (ii): one side of a zero-momentum bridge has a single adjoint index, so the graph vanishes without target averaging. Cor F.2(b): the constants are valid; optionally sharpen them to |omega| <= 2p0/|q| and |Phat|_E <= sqrt2 p0.

### [required_fixes 9]
9. Optional upgrade. Prove gluon regularity at omega = 0 (Lemma F.7(c), Cor F.3(a)) from the exact on-shell BRST Ward identity. It gives p_a M_n^{ab} = alpha_n p^b with alpha_n polynomial, so d_ab M_n^{ab} = -g_ab M_n^{ab} + 2 alpha_n is polynomial. Gluon regularity would then be [R, R_PT] without Theorem B.

### [required_fixes 10]
10. Pipeline (orchestrator). REPORT.md still does not exist. Save the revised report from journal entry 111 (agent aa6e04ae9a9fda375) as verify/extend/X3-ope/REPORT.md. Save this review and X3-ope-rev2-1 from their StructuredOutputs; subagents cannot write report files. Evidence for this review is in verify/extend/X3-ope/review_r2_2_scripts/ (rv22_algebra.py, rv22_numeric.py, logs/).
