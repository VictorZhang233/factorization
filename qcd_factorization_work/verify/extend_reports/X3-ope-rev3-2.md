# X3-ope-rev3-2

(extracted verbatim from the workflow journal; structured output of the agent)

## overall

fixable_issues

## per_result

### [per_result 1]
[0] PROCESS / STATUS (answer to the relayed question 在正常运行吗). 在运行，但不完全正常 (running, not fully normal). Workflow wf_52f29317-58b is active, and X1, X2 and X3 are all in review round 3 (journal lines 123-130). I am agent ab95205b675842721 (X3-ope-rev3-2, line 130); X3-ope-rev3-1 runs in parallel (line 129). Three problems persist. (a) /Users/hao-cheng/Desktop/theorem proof/qcd_factorization_work/verify/extend/X3-ope/REPORT.md still does not exist. (b) No X3 review_r*.md exists; across X1-X3 only X1-glauber/review_r2_1.md is on disk. (c) Each review therefore has to be rebuilt from the journal. What I reviewed: the fix-round-2 StructuredOutput (agent a316f5dc20a66707d), which is line 128 of /Users/hao-cheng/.claude/projects/-Users-hao-cheng-Desktop-theorem-proof/c211c739-758d-4b40-bbac-67f4e1a65da4/subagents/workflows/wf_52f29317-58b/journal.jsonl. I extracted it to scratchpad/x3rev3_2/j/line128.txt and read it together with the two round-2 reviews (lines 119 and 120). Under the subagent rule against report .md files I did not write review_r3_2.md: this StructuredOutput is the review, and the orchestrator must save it and save line 128 as REPORT.md. Reproducibility: all eight X3 scripts (f1-f6, h1, e1) reproduce their logs byte for byte (review_r3_2_scripts/logs/rerun_x3_scripts.log). My independent checks are in /Users/hao-cheng/Desktop/theorem proof/qcd_factorization_work/verify/extend/X3-ope/review_r3_2_scripts/ (rv32_triangle.py, rv32_misc.py, rv32_bv.py); all pass, logs in logs/.

### [per_result 2]
[1] SLOT OUTCOMES: CORRECT. X3a ('not delivered (open)'): honest. The uniqueness-only route is circular, the designated sources are listed as unread with DOIs, and the new Lemma A.7 is correct (item 8). One addition is needed for O3, see item 21. X3b, X3c, X3d: I agree. X3e (PASS as a per-graph statement): confirmed again; my independent triangle check passes (item 13). It is right that the spec patch must not apply the rule 'asm:appM-forward 已解除'.

### [per_result 3]
[2] D1 (gauge-parameter running and D-dimensional dimensions): CORRECT. From xi_0 = Z_3 xi_R with the one-loop MS-bar Z_3 I re-derived beta_xi = (alpha_s/2pi) xi_R [(13/6 - xi_R/2) C_A - (4/3) T_F n_f] (rv32_misc (a)). At xi_R = 1 and SU(3) it equals (alpha_s/2pi)(5 - 2n_f/3), which is nonzero for every integer n_f. With d(eps) = d4 - eps(n_phi - n_g), s raises the dimension by exactly 1 for every generator (rv32_misc (b)). The canonical dimensions [J] = 3-2eps and [calJ(q)] = 2-2eps are right.

### [per_result 4]
[3] D11 (condition NE): CORRECT as statements. Tag: these are lemmas, not definitions. Counting, re-derived: a rank-5 Dirac structure needs five distinct index carriers among e_mu, e_nu, q and the internal index slots of O. If both e_mu and e_nu sit in one antisymmetrizer, the term is antisymmetric in mu nu. With only one of them plus q, three internal slots are needed, which costs dimension >= 3, so d_O >= 6 in the symmetric channel. Gram minors need ten slots, more than are available at d_O <= 5. Tree-level example, re-derived by hand: the s- and u-channel hard parts each give gamma^[nu l alpha q mu]/q^4, the k-terms cancel pairwise, and the total 2 gamma^[nu l alpha q mu]/q^4 is antisymmetric in mu nu. f6 agrees. Twist 2 has no evanescent operator, because all derivative indices are symmetric-traceless free indices. The grade [R, R_def] (results[24]) understates what these are: lemmas resting on the O(4) second fundamental theorem plus gamma^[5] = 0. How (NE) is used in (A4) is a gap (item 5).

### [per_result 5]
[4] Lemma A.3. (a), at fixed generic eps in the D-dimensional basis: CORRECT. (b), at D = 4 in (NE) sectors: CORRECT only if the hypothesis is a relation over the operators of the sector S alone. If the sum runs over the whole basis, step 2 (tree-level injectivity) fails for evanescent operators of other sectors. Their coefficients are then never fixed, and the induction step 'lower orders handled by induction' breaks, because their renormalized D = 4 Green functions enter the order-r equation (item 5).

### [per_result 6]
[5] Theorem A. (A1) and (A3) as [A], and (A2) with xi_0 = Z_3 xi now included: CORRECT. The beta_xi d_xi correction answers r2-1 correctly.
(A4): GAP. Uniqueness starts from sum over ALL O of DeltaC_O G_[O] = O(|q|^{1-a} ln^k), and this sum contains evanescent operators of other sectors at the same dimension. An example is the four-quark Gamma^(5) x Gamma^(5) operators at d_O = 6, which D11 itself lists; that is the dimension of the n = 4 twist-2 operators. Their 4D tree vertices vanish, so their DeltaC are never fixed, while their renormalized D = 4 Green functions are nonzero from one loop on. The report never shows that these contributions cannot land on the sector's tree structures. Exact separations do exist: the split into mu nu symmetric and antisymmetric parts, and the split by dimension (|q|-homogeneity). So (A4) is proved for the symmetric channel at d_O <= 5, but not for twist 2 with n >= 4. Hence 'DIS is unaffected' (R2-2) is true in substance but not proved by the argument given.
(A5): CORRECT as restricted, but the route through (A4) is unnecessary and is what imports the (NE) restriction. By (A3), C^MS = C^bare Z^{-1}, and C^bare depends only on (q, g0, xi0, eps). Hence (mu d_mu + beta(alpha,eps) d_alpha + beta_xi d_xi) C^MS = C^MS gamma with gamma = -(mu dZ/dmu) Z^{-1}, exactly at fixed eps and for every operator of the full D-dimensional basis. The limit eps -> 0 then gives (A5) at grade [R, R_cond: A3], without (NE).

### [per_result 7]
[6] Corollary A.5 (GI-block RG equation in Feynman gauge): CORRECT given K3 and GP, and not circular, since Cor F.2 does not use (A5). The twist-2 derivation of GP (Cor F.2(a) for xi near 1, BRST xi-independence of on-shell physical T2, K3 for A = sum of Z_GG times tree, and invertibility of A) is a sound [A] argument. Minor: d_xi gamma_GG = 0 is not used in the xi = 1 equation; only d_xi C^GI = 0 is.

### [per_result 8]
[7] Remark A.6 (circularity of CLAIMS R-M26): CORRECT.

### [per_result 9]
[8] Lemma A.7 (matching at p = 0, new): CORRECT. I checked it against the reference text (scratchpad r2rev1/refdoc.txt, lines 5690-5930 and 6095-6230). Def C.21(b) subtracts every AB part, 1PI or not, with t_p^{delta_a}, delta_a = a - sum_E d_e, and q frozen. Identity C.22 uses minimal normal products. Ass. C.24 is stated per graph. Lemmas C.29-C.30 use only homogeneity, O(4) covariance and order-wise independence, so the per-order form suffices, as the report claims. Step 1, re-derived: for every AB part sigma, sigma plus l_x lies in the 2-edge-connected component of l_x, so sigma is contained in gamma_0. The remaining renormalization parts are 1PI and cannot contain a bridge. Hence R_Gamma = (product over hanging trees) x (1 - t^{delta_a(gamma_0)}) Rbar_gamma0. Bridge momenta are linear in p, tadpole leaves vanish, and sum over E(gamma_0) of d_e <= sum over E(Gamma) of d_e. Steps 2-4: correct. M_sq is invertible as a formal series with q-independent entries, and m d_m is handled. In effect the lemma shows that C.24 is equivalent to the existence of any p-independent expansion with CT-p bounds. 'No novelty claimed' is right: Zimmermann normal products are classically fixed by zero-momentum normalization conditions.

### [per_result 10]
[9] Theorem B (BRST reduction): CORRECT given its premises (E_eps, LBC, K3, KO), at the stated grades.
DR-SD sign, re-derived from the integral of D phi delta_L/delta phi(y)[Y Phi~ e^{iS}] = 0: the factor (-1)^{|phi||Y|} multiplies both surviving terms and cancels, and -1/i = i. This gives eps_k = (-1)^{|phi| sum_{l<k} |phi_l|}, as now stated. f5 is a genuine exact Berezin test with interaction, and it covers the only parity case where the two rules differ (odd phi, odd Y).
Step-3 sign composition eps'_k (-1)^{(|phi_k|+1) sum_{l<k} |phi_l|} = eps_k: checked for every parity string with n <= 6 (rv32_misc (d)).
Step-5 degree matching, checked symbolically: [K_Y] = d_phi - 1 - d_O' - |alpha| for Y = O' d^alpha dS/dphi, and the exponent is 3 - d4_Y + eps(n_phi - n_g - 2 - m) (rv32_misc (c)).
Step 6 has a presentational gap; see item 10.

### [per_result 11]
[10] Remark B.1 (LBC at formal D) and Theorem B step 6: GAP (minor; the conclusions survive).
(i) s, dS/dphi and the GI class depend on g0 (sA = dc - i g0 [A,c]). 'Apply LBC to each loop-order coefficient' is valid only if 'loop order' means the homogeneous component of weight w = n_phi - n_g, with g0 counted in both coefficients and operators. That component is exactly the eps-exponent class of step 5 and is preserved by s and the EOM ideal (D1), but the text never says so.
(ii) 'Finite-dimensional Q-space V^g' requires that weight grading with g0 treated as a formal parameter. Alternatively, rescale phi -> phi/g0 (ghosts and B likewise); then s, the EOM ideal and GI are g0-independent and S = g0^{-2} S~.
(iii) (B-iii) needs the GI coefficients to be power series in g0. LBC at fixed g0 does not give this, but the rescaling does: a weight-w GI monomial in F, psi, D has polynomial g0-dependence.
(iv) Step 2 needs n even. For odd n, gamma^[1..n] is central in an irreducible spinor representation and gamma^[r] is proportional to gamma^[n-r], so 'gamma^[r], r <= n, independent' fails.
Citations: BBH ('in any number of spacetime dimensions'; abstract checked), Henneaux 1996 and BHHS are adequate.

### [per_result 12]
[11] Theorem I (= A + B + twist classification), grade [A]: I agree; the four-route gap analysis is accurate.

### [per_result 13]
[12] Lemmas F.0, F.1 and F.6: CORRECT. Re-derived: F.0 (-s_T = Q^2 (c_q^2 - c_p c_q omega)); F.6(a) by deletion-contraction; the four facet types under x_q = L+1 - sum of x_e; and d_u = 0 only for coordinate facets, since the cographic matroid of a bridgeless G0 is loopless. The F.6 attribution to Schultka section 4, Borinsky, Arkani-Hamed-Hillman-Mizera, Tellander-Helmer and Walther is now adequate.

### [per_result 14]
[13] Theorem F with Examples F.3 and F.4: CORRECT, [R, R_PT] per graph. Independent check (rv32_triangle), by a route different from f2:
(A) naive terms from one Feynman parameter and the shift k = l - xq; at p^2 = 0 only (-2x nu)^n survives. They equal the omega^n coefficients of the 2F1 closed form identically in (a_i, D) (sympy ratio = 1).
(B) direct 2-d simplex quadrature, in a parametrization different from f2's, equals the closed form at six complex omega. Four of them lie outside the unit disk (1.5+0.7i, -2+0.5i, 3i, 2.5-0.2i); relative deviation <= 1.1e-10. This confirms holomorphy on the cut plane.
(C) the naive series reproduces the closed form to 1e-21 at three complex omega with |omega| < 1.
(D) at a_i = 1 the leading pole of the n-th term is -1/((n+1) eps) for n <= 4.
I also re-derived the closed form analytically via Euler's integral for 2F1.

### [per_result 15]
[14] Lemma F.7 (T2 projector in D dimensions): CORRECT.
(a) re-verified numerically in D = 7 (rv32_misc (e)).
(b) the general-n proof is right. Hand check: transversality forces c = c' = b/Q^2 and a = eQ^2 - b/Q^2, and then the projector returns exactly b nu^{n-1}. Two lines are missing: that each naive term T_n is transverse (lambda-expansion of q_mu T^{mu nu}(lambda p) = 0, licensed by Theorem F), and that oddness in omega needs crossing of the summed graphs.
EDITORIAL ERROR: the line 'f4 c: at tree level T2 = 4w/(1-w^2) and T1 = 2w^2/(1-w^2)' sits under (c) 'Gluon target'. But f4(c) is the tree-level QUARK handbag (f4 docstring, line 13), and a gluon has no tree-level coupling to the photon.

### [per_result 16]
[15] Corollary F.2 (forward partonic OPE): CORRECT as [A].
(b): the constants check on 2000 random points: |nu| <= p0|q|_E and |Phat|_E^2 = 2p0^2 - |nu|^2/Q^2 (rv32_misc (g)).
Step 4, the evanescent sentence: GAP in justification. 'Spin-averaged forward tree matrix elements of gamma^[r>=2] structures vanish' is not enough, because in MS-bar an evanescent operator can mix into physical operators of its own type, so <j|[E]|j> = sum_Q Z_EQ tree_Q. The conclusion still holds for another reason: no twist-2 operator is evanescent, mixing preserves Lorentz type and dimension, and forward on-shell massless tree matrix elements of operators with twist > 2 vanish (p^2 = 0, pslash u = 0).

### [per_result 17]
[16] Lemma F.8 (gluon regularity from OS-WI, new, conditional): CORRECT. The step-3 identity d^ab M_ab = -g^ab M_ab + alpha + alpha' is verified numerically for tensors built to satisfy OS-WI (rv32_misc (f)). OS-WI as formulated (every eps with eps.p = 0, including eps = p) is equivalent to p^a M_ab proportional to p_b. That is the standard BRST form, with the ghost amplitude inside the proportionality factor, so it is the right premise; the grade [R, R_cond: OS-WI] with content [A] is honest. Suggested one-line addition: -g^ab M_ab is transverse in mu nu because the EM Ward identity has no contact terms when the external gluons are EM-neutral.

### [per_result 18]
[17] Corollary F.3, Remark F.5 and Lemma 4.10: CORRECT as tagged. F.3(a) is now split: quarks [R, R_PT]; gluons at omega = 0 [A].

### [per_result 19]
[18] Lemmas 5.1-5.5, including the new 5.5(c): CORRECT.
5.1: P^2 = M^2|q|^2/Q^2 and omega = 2iMq4/Q^2, checked numerically (rv32_misc (h)).
5.5(c), every step checked: the Taylor formula at s = 1 with remainder L^{N+1}H; the bound |y + sY| >= cs, which holds because Gamma lies in an open half-space; the chain rule (L^{N+1}H) o Theta = (a.d_x)^{N+1}(H o Theta) with a = (DTheta)^{-1} Y; integration by parts; uniform continuity of H.
Numerical test (rv32_bv): a 1-d curved approach (x-dependent speed plus a real distortion), and the exact 2-d geometry of Prop 5.6 (Theta = (x+i eta, s+eta^2-2ix eta), with an x-dependent direction), both converge to the predicted wedge boundary value with error O(eta): 1.4e-4 at eta = 1e-4, and 4.1e-3 at eta = 2e-3.
NOVELTY: the label 'NEW' is not substantiated. The argument is Hoermander's proof of Thm 3.1.15 run through a change of variables.

### [per_result 20]
[19] Prop 5.6 (dispersion relation from W1-W3): CORRECT; step 6'(ii) is now rigorous via 5.5(c). Two precision points. (1) The test functions must be supported in the spacelike region s = |qvec|^2 - q0^2 > 0, where the local wedge is established. (2) The local cone varies with x, so 5.5(c) must be applied on small patches (partition of unity), each with a fixed closed subcone containing all directions (1,-2x) of the patch.

### [per_result 21]
[20] Theorem 5.7, Prop 5.8, Theorem 5.9, Theorem M and E1-E6: unchanged since round 2; I agree with the earlier verifications. The RG solution in Thm 5.9 has the correct sign given the convention (A5).

### [per_result 22]
[21] LITERATURE: quotes verified in the full texts.
- Smirnov CMP 134: p. 110 (s90.txt lines 50-74; Smirnov's [26] is LS-dV); pp. 117-118 (lines 470-486: the remainder is a tempered distribution in xi and a function at non-exceptional Euclidean momenta; 'may easily maintain'). He mentions gauge theories only for the choice of basis (line 1253).
- Chetyrkin arXiv:1701.08627 (downloaded): 'given elsewhere' (l.1612), 'published elsewhere' (l.1637), '[80] ... very particular case ... product of two composite operators' (l.1943-1946); the rigorous proof is credited to [53,54] 'along the lines of' [7,9,25,82] = Zimmermann Brandeis 1970, Zimmermann AP 77, Zav'yalov, Anikin-Zav'yalov TMF 27.
- Keller-Kopper p. 246 and Tkachov footnote 14: verified.
- BBH abstract: verified.
Missing source: the reference's own App C status table calls C.24 the momentum-space, frozen-q form of Zimmermann's coordinate-space theorem and cites Zimmermann's sector method [18, 78]. Zimmermann, Ann. Phys. 77 (1973) 570 (reprinted Lect. Notes Phys. 558 (2000) 278) is therefore the first source to read for O3, but it is absent from K2 and O3.

### [per_result 23]
[22] NOVELTY: no overclaims except Lemma 5.5(c) ('NEW'). INSPIRE fulltext searches found nothing that pre-empts Theorem F's analytic step, Remark B.1 or Lemma F.8: 'BRST cohomology' + evanescent + dimensional regularization + gauge-invariant operators (10 hits, none relevant); 'method of projectors' since 2024 (9 hits); 'forward Compton amplitude' + 'naive Taylor' since 2023 (0 hits). The markers stay as the report proposes: 本书给出的严格证明 for Theorem F, no novelty for Lemma F.6, Theorem B or Lemma A.7.

### [per_result 24]
[23] VERIFICATION LOG: REPRODUCED. All eight X3 scripts re-run byte-identically (SHA prefixes in review_r3_2_scripts/logs/rerun_x3_scripts.log). f5 and f6 are genuine checks, and f6 agrees with my hand derivation.

## required_fixes

### [required_fixes 1]
1. (A4), Lemma A.3(b), D11, section 0 and R2-2. Define a 'sector' as a set of operators of one dimension that can be isolated from the OPE identity by exact projections, and claim D=4 uniqueness only for such sectors. Cases: (a) the mu nu-symmetric channel at d_O <= 5 is covered by the exact symmetry split plus the dimension split; (b) for twist 2 at every n, add an exact projection onto q-hat spherical harmonics, legitimate because (A1) is uniform in direction. The mu nu-trace part of a spin-j coefficient has harmonic degree <= j, and the traceless part <= j+2. So the degree-n (trace) and degree-(n+2) (traceless) harmonics see only operators of dimension n+2 with spin >= n. Check (NE) for that projected set, which also contains gauge-variant low-twist monomials of the D-dimensional basis. Otherwise, add a Dugan-Grinstein-type non-contamination premise ([A], K12) and grade accordingly. Replace 'DIS is unaffected' with a pointer to whichever argument is used.

### [required_fixes 2]
2. (A5), Cor A.5 and spec patch item 4. Replace the proof of (A5) by the direct derivation from (A3): C^bare is mu-independent at fixed (g0, xi0, eps), so (mu d_mu + beta(alpha,eps) d_alpha + beta_xi d_xi) C^MS = C^MS gamma with gamma = -(mu dZ/dmu) Z^{-1}; then let eps -> 0. This holds for every operator of the D-dimensional MS-bar basis. Drop the (NE) restriction from (A5) and from spec patch item 4, and grade (A5) [R, R_cond: A3]. Cor A.5 then needs only K3 and d_xi C^GI = 0; remove d_xi gamma_GG = 0 from GP, or note that it is not used at xi = 1.

### [required_fixes 3]
3. Theorem B step 6 and Remark B.1. (i) State that the 'loop-order coefficients' are the homogeneous components of weight w = n_phi - n_g (g0 counted in coefficients and operators), i.e. the eps-exponent classes of step 5, and that s and the EOM ideal preserve this weight. (ii) Treat g0 as a formal parameter in V^g together with the weight grading (needed for finite dimensionality), or rescale phi -> phi/g0 for all fields so that s, the EOM ideal and GI are g0-independent and S = g0^{-2} S~. (iii) Use the rescaling to show that the GI coefficients in (B-ii)/(B-iii) are power series in g0. (iv) Require n even in Remark B.1 step 2.

### [required_fixes 4]
4. Cor F.2 step 4. Replace the evanescent sentence: in MS-bar, <j|[E]|j> = sum_Q Z_EQ tree_Q, so a vanishing tree for E itself is not sufficient. Use instead the argument that no twist-2 operator is evanescent, that mixing preserves Lorentz type and dimension, and that forward on-shell massless tree matrix elements of operators with twist > 2 vanish.

### [required_fixes 5]
5. Lemma F.7. Move the line 'f4 c: tree level T2 = 4w/(1-w^2), T1 = 2w^2/(1-w^2)' from (c) 'Gluon target' to (b) 'Quark target': f4(c) is the quark handbag. Add one line stating that each naive term T_n is transverse, by the lambda-expansion of q_mu T^{mu nu}(lambda p) = 0 licensed by Theorem F, and that oddness in omega uses crossing of the summed graphs.

### [required_fixes 6]
6. Lemma 5.5(c) (results[20], section 5) and Prop 5.6. Replace 'NEW' by 'proved here (routine extension of the proof of Hoermander Thm 3.1.15)', with no 本书新结果 marker unless a literature check supports it. In Prop 5.6 step 6'(ii), restrict the test functions to the spacelike region s > 0, and state the partition of unity over patches, each with a fixed closed subcone containing the approach directions (1,-2x) of the patch.

### [required_fixes 7]
7. K2 and O3. Put Zimmermann, Ann. Phys. 77 (1973) 570 (reprinted Lect. Notes Phys. 558 (2000) 278), together with the Brandeis 1970 lectures, first on the reading list for X3a. The reference's own status table calls C.24 the momentum-space, frozen-q form of Zimmermann's coordinate-space theorem. Also record that Smirnov's theorem is a mixed statement: a distribution in the coordinate variables xi and a function of the non-exceptional momenta.

### [required_fixes 8]
8. D11 and results[24]. Re-tag the scope statements of (NE) (twist 2 for every n; symmetric channel at d_O <= 5; the evanescent counterexamples) as lemmas with grade [R], citing the O(4) second fundamental theorem and the relation gamma^[5] = 0 in Cl(4), rather than [R, R_def].

### [required_fixes 9]
9. Pipeline (O13), for the orchestrator. Save journal.jsonl line 128 (agent a316f5dc20a66707d, X3-ope-fix2) as verify/extend/X3-ope/REPORT.md, and save this StructuredOutput (agent ab95205b675842721, X3-ope-rev3-2) as verify/extend/X3-ope/review_r3_2.md. Subagents do not write report files. My evidence is in verify/extend/X3-ope/review_r3_2_scripts/ (rv32_triangle.py, rv32_misc.py, rv32_bv.py, logs/ including rerun_x3_scripts.log).
