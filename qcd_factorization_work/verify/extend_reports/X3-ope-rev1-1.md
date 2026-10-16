# X3-ope-rev1-1

(extracted verbatim from the workflow journal; structured output of the agent)

## overall

fixable_issues

## per_result

### [per_result 1]
STATUS AND PROVENANCE. Answer to the relayed question (在正常运行吗): not fully normal. verify/extend/X3-ope/REPORT.md does not exist. The X3 author's transcript is ~/.claude/projects/-Users-hao-cheng-Desktop-theorem-proof/c211c739-758d-4b40-bbac-67f4e1a65da4/subagents/workflows/wf_52f29317-58b/agent-a924e58162fd27409.jsonl. The author tried to Write REPORT.md at 2026-10-10T22:40:21Z. The harness rejected it with 'Subagents should return findings as text, not write report files'. The author then returned the full report (about 44.5 KB) in StructuredOutput.summary at 22:49:44Z. The workflow script's extend() launches reviewers without checking that REPORT.md exists. The same rule will also block review_r*_k.md and the fixer's edits to REPORT.md. X1-glauber and X2-subtraction have no REPORT.md either. I reviewed the author's StructuredOutput (summary, results and open lists); it is byte-identical to reviewer #2's recovered copy. Extracted copies are in /private/tmp/claude-501/-Users-hao-cheng-Desktop-theorem-proof/c211c739-758d-4b40-bbac-67f4e1a65da4/scratchpad/x3rev/author/. The blocked draft there is truncated after section 2. I did not write review_r1_1.md, for the same harness reason; this structured output is the review. My independent check scripts and logs are in verify/extend/X3-ope/review_r1_1_checks/ (r1, r2, r3). All four X3 scripts reproduce their stored logs byte for byte.

### [per_result 2]
Lemma A.3 (linear independence): CORRECT. The proof is a standard induction on the order, using injectivity of tree-level vertex polynomials, and it holds for connected amputated Green functions at non-exceptional momenta. Total-derivative operators stay independent because the operator momentum is nonzero. Vanishing of graded-homogeneous coefficients at fixed eps is fine: each loop order j carries a single power |q|^(2-d-2j eps).

### [per_result 3]
Theorem A (Euclidean OPE in the full MS-bar basis): PARTLY CORRECT; THE GRADE IS TOO HIGH. (A2), (A4) and (A5) follow correctly from (A1) and (A3). A finite limit of sum_k c_k(eps) exp(-k eps L) is a polynomial of degree <= r in L; uniqueness follows from the log-polynomial lemma; RG follows from uniqueness. (A5) needs two unstated points. First, the remainder bound must hold for mu in compacts with polynomial ln mu dependence, so that mu d/dmu of the O(.) term is again O(.). Second, for Phi non-empty there is no inhomogeneous identity-operator term; such a term exists for the vacuum correlator used in Part IV. (A1) and (A3) rest on Smirnov CMP 134 (1990) 109, Gorishny NPB 319 (1989) 633 and Llewellyn Smith-de Vries NPB 296 (1988) 991. These were checked only at the level of abstracts and Smirnov's review (author's own open item O1). '[R-cited]' is not a monograph grade. Under the tag rules, an unverified scope means [A]. So Theorem A is [A] overall; (A2), (A4) and (A5) are rigorous implications of (A1) and (A3).

### [per_result 4]
Remark A.6 (the uniqueness discharge of Ass. C.24 in CLAIMS R-M26 is circular): CORRECT. lem:appM-uniqueness(a) needs sum_O DeltaC_O G_O = O(remainder). That requires the frozen-q remainder N_a to be small, which is C.24 itself. An identification lemma (open item O3) would be needed instead. Consequence: slot X3a FAILS, and asm:appM-remainder stays tagA (fallback). The blocked draft's section 0.2 claimed the opposite ('Prop A.6: C.24 follows from Smirnov + scheme change + uniqueness, new observation'). The final text retracts this, and the draft claim must not enter the spec.

### [per_result 5]
Theorem B (BRST / gauge-invariant reduction via exact DR Ward and Schwinger-Dyson identities): THE ARGUMENT IS SOUND GIVEN ITS INPUTS; THERE ARE GRADE AND NOVELTY GAPS. I checked steps 1-7:
- sJ = 0 together with the exact bare DR Ward identity (no gamma5, B kept off-shell).
- The 'soft' sums combine to -/+ sum_O C_O <(sO) Phi>.
- The merged terms sum_k +/- C^{s phi_k}(q; p_k) <O' Phi_khat> equal <E(q) Phi> for the EOM operator E = sum O' C^{s phi}(q; -i d) dS/dphi. This uses DR-SD with delta(0) = 0, and holds because C^{s phi} depends on k only through the field type and p_k.
- Lemma A.3 at fixed eps gives sum_O C_O sO = +/- E, degree by degree.
- Local cohomology (weak gamma-cohomology at ghost number 0), then EOM and Kugo-Ojima vanishing.
Gaps:
(i) E_eps (expansion with one composite spectator, the same C_O, and C^Z polynomial in p_Z) is taken from K2, whose scope is unverified (O1). The grade is therefore [A], or [R-cond: E_eps] with E_eps stated in the assumption register.
(ii) LBC must cite the exact theorem (which result of BBH Phys. Rep. 338 covers quarks and the trivial pairs (cbar, B)).
(iii) The claim that the reference's (B1) polynomial contact terms are 'in general false' needs an explicit one-loop example showing ln q^2 in C^{s phi}.
(iv) 'New proof' needs a literature check. INSPIRE shows Joglekar Ann. Phys. 108 and 109 (1977) are application-specific and physicist-level; Collins, Renormalization section 12.8 and Kluberg-Stern-Zuber PRD 12 (1975) are still to be checked.
(v) Write out the degree matching in step 5.

### [per_result 6]
Theorem I (= A + B): THE GRADE IS TOO HIGH. It is [A], not [R-cited]. Slot X3b does NOT pass: prop:dis-ope-euclid stays [A] and decision D3 is unchanged. Slot X3d is not verified. Its pure Yang-Mills part rests on Hollands RMP 20 (2008) 1033 (abstract only) and Froeb-Holland arXiv:1603.08012v2, which has no journal reference on INSPIRE or arXiv. The QCD part via Theorem B is [R-cond: E_eps], roughly [A]. asm:appM-brst-ope can be labelled 'reduced to E_eps', not discharged.

### [per_result 7]
Lemma F.0 (forward 2-forest structure F = Q^2 (F0 + omega F1), F1 dominated by F0): CORRECT, and trivial. The coefficient is -s = Q^2 (c_q^2 - c_p c_q omega) with c_p, c_q in {0, +-1}, and a monomial determines its 2-forest. Independent check: I recomputed the supports by deletion-contraction, using F0/Q^2 = U(G/{J1=J2}). They agree with f1 on all 21 topologies, and every coefficient of U and F0 equals 1. Calling a one-line observation 'new' is an overstatement.

### [per_result 8]
Lemma F.1 (Newton-polytope domination): CORRECT; I re-derived it.
(a) For |lambda| <= r < 1 the coefficients c_m (1 + lambda theta_m) lie in |arg| <= arcsin r, so the Newton polytope P is unchanged. The numerator monomials of the n-th Taylor term lie in n Newt(F1), which is inside nP. Hence s + m lies in c int(P) + nP, which is inside (c+n) int(P), so one domain Lambda works for every n.
(b) sum_n |binom(-c,n)| r^n <= (1-r)^(-|c|) and |F1| <= F0 <= G0 together justify Fubini.
(c) On Kaneko-Ueda cubes, F1 = x^{m_sigma} f_{sigma,1} with f_{sigma,1} a polynomial and |f_{sigma,1}| <= f_{sigma,0}. So Re f_{sigma,lambda} >= (1-r) f_{sigma,0} > 0, Gel'fand-Shilov gives lambda-independent poles, and the identity theorem finishes the proof.

### [per_result 9]
Theorem F (the forward on-shell DR amplitude equals its naive Taylor series in p; holomorphic in the cut omega-plane): CORRECT AS STATED, per graph and given the hypothesis (F-DR). Four gaps, all fixable.
(i) (F-DR) is assumed, checked on 21 topologies and 34 random graphs, yet Corollary F.2 uses it at every order. It is in fact a theorem (proof in required fix 3). Newt(U + F0) is full-dimensional iff G0 = G + {J1J2} is loopless and 2-connected. When it is, the only facets with d_u = 0 are coordinate facets, so DR is admissible for every non-degenerate graph, including Tarasov-shifted integrals. My checks: the full-dimensionality criterion held on 116/116 random graphs; the coordinate-facet property held on all 10 random full-dimensional graphs, 45/45 targeted 2-connected graphs and all 21 explicit graphs (scripts r1, r2).
(ii) 'Spin sums are polynomial in p' is false for gluon targets with physical polarizations: the projector -g + (pq+qp)/(p.q) - pp q^2/(p.q)^2 has 1/omega^k terms. The F2/FL projection also has them: at p^2 = 0, T2 = Q^4 (3 ppT - (nu^2/Q^2) gT) / (2 nu^3). The theorem must be applied to components contracted with tensors polynomial in p, followed by Laurent-series algebra and analyticity of T2 at omega = 0.
(iii) The definition must be stated: the parametric (Speer-type) DR integral at p^2 = 0. It equals the Feynman-i-epsilon Minkowski integral for real |omega| < 1, where all coefficients are positive, and is then continued in omega.
(iv) 'Lines carrying exactly 0 vanish by colour' needs its reason: there is no invariant tensor with a single adjoint index (colour-averaged target). Self-loops and scaleless blocks are covered by (F3).
Novelty: INSPIRE, arXiv and web searches found no prior rigorous proof. Larin-Nogueira-van Ritbergen-Vermaseren, NPB 492 (1997) 338, around Eq. (29), say the projection method 'implicitly involves a considerable rearrangement of infrared and ultraviolet divergences'. Mark this as the book's rigorous proof of the standard projection method (Gorishnii-Larin-Tkachov PLB 124 (1983) 217; Gorishnii-Larin NPB 283 (1987) 452). Semenova-Smirnov-Smirnov EPJC 79 (2019) 136 treat positive-coefficient two-scale limits, not this mixed-sign F1. Slot X3e: PASS after fixes (i)-(iv).

### [per_result 10]
Corollary F.2 (forward partonic OPE at every order): THE LOGIC IS CORRECT; THE GRADE IS [A]. Each step checks:
- The forward graphs are exactly the asymptotically irreducible 2-leg hard graphs, because non-AI bridges carry 0 or +-p.
- Theorem F gives sum of naive terms = sum_O C^bare_O V_O(p,-p); all loops are scaleless, so the matrix elements are tree-level.
- C^bare = C^MS Z.
- Aliens drop out by Joglekar-Lee triangularity, and their tree-level elements vanish (EOM on shell; p.eps = 0 for B legs; no ghosts).
- p^2 = 0 forces twist 2.
Gaps: the result inherits the grade of Theorems A and B ([A]) and needs (F-DR) for all graphs (fix 3). The asm:appM-forward form (remainder O(|q|^(1-N) ln^k), uniform in Euclidean directions with 2p.qhat imaginary) should be derived explicitly by Cauchy estimates on |omega| <= 1/2. Net effect: asm:appM-forward is reduced to Theorems A and B, not discharged at [R]. prop:dis-ope-forward stays [A], as the spec anticipated.

### [per_result 11]
Corollary F.3: HOLOMORPHY IS CORRECT; TWO CLAIMS ARE OVER-GRADED. Holomorphy on the cut plane is [R]: for omega off the real axis the coefficients {1, 1 +- omega} lie in an open half-plane, and for real |omega| < 1 they are positive. 'Disc = 4 pi i F2 [R]' identifies the discontinuity with the cut diagrams, i.e. it is the DR cutting rules for Laurent coefficients, including the distributions at x = 1. The report does not prove this, and the spec grades the analogous e+e- cut identification [A] (K10), so this should be [A]. 'At one loop it holds for all n >= 1 [R] (c_dis)' is unsupported. c_dis checks only N = 1..8 for quarks and even N <= 8 for gluons (logs/ope_check_N8.log), and itself assumes the dispersion relation. Slot X3c (one-loop all-N Mellin-moment identity) is therefore NOT delivered.

### [per_result 12]
Examples F.3/F.4: CORRECT. I re-derived the 2F1 formula, using F = Q^2 x2 (x3 + (1-omega) x1). Taylor coefficients obtained by a Cauchy integral match the naive tensor terms to 1e-29 at complex (a_i, D) for n = 0, 1, 3, 7. A direct quadrature at a complex point matches the exact formula to 1e-9 (script r3). At a_i = 1 each term has the pole -1/((n+1) eps). F.4 holds with 'omega = 0' meaning (p+q)^2 = q^2 off shell, and Q^2 I approaches ln(Q^2/P^2) + 2 as stated. Minor points: the f2 docstring says 'random complex parameters' but the script uses real ones, and point 2 of f2(B) has an unflagged quadrature deviation of 1.2e-5.

### [per_result 13]
Remark F.5 (zero-momentum twist-2 insertions are IR finite by Breitenlohner-Maison II, Omega = n+2 >= 4): grade [A] is appropriate and the claim is plausible from IR power counting. 'Answers the open question of Rem C.37' is overstated until BM II's hypotheses for composite insertions at exceptional momenta are checked (author's open item O10).

### [per_result 14]
Lemma 4.10 (only the segment approximation is needed at hadron level): CORRECT as a logical statement.

### [per_result 15]
Lemmas 5.1-5.5: CORRECT.
- 5.1: Phat^2 = M^2 qvec^2 / Q^2 >= M^2/4 and |omega| <= sqrt(3) M/Q (re-derived).
- 5.3: V. A. Markov plus sum |coefficients of T_n| = |T_n(i)| <= (1+sqrt 2)^n (checked for n <= 21); the factor 2 covers complex coefficients.
- 5.4: subharmonic averaging over circles of radius 2, with J(y) = log max(1, |w+-|) >= 0 (Jensen applied to w^2 + i y w - 1), gives |f| <= C (3+|z|)^A. Correct and elegant.
- 5.5(a): nu([R,2R]) <= C R^(A+1), so the integral of x^(n0-2) F2 is finite iff n0 > A+1 (re-derived; sharper than the spec's n0 > A+2).

### [per_result 16]
Prop 5.6 (dispersion relation from W1-W3): CORRECT IN STRUCTURE. Step 9 checks: |1 - x^2 omega^2| >= (Im omega)^2 / |omega|^2 for all x in (0,1] (minimum-distance argument). H is entire by the one-dimensional edge of the wedge, a polynomial by Lemma 5.4, O(omega^(n0-1)) at 0, and H(iy)/(iy)^(n0-1) tends to 0; hence H = 0. Steps 3-7 are correct:
- the SO(3)-even slice functions are holomorphic in (w, s^2);
- the point w = iQ is removable because T2 = Q^4 (b + a/Q^2)/nu;
- the slice inequality Im w - |Im s| >= Im w Q^2 / (2(|w|^2 + Q^2)) is proved in closed form;
- positivity gives F2 >= nu F1 / Phat^2.
The restriction to fixed-Q^2 slices via continuity of primitives is plausible but only sketched.

### [per_result 17]
Theorem 5.7 (fixed-n Taylor coefficients): CORRECT. The positivity tail is <= 2 t_n0 r_Q^(N-1); Markov's inequality applies on the segment; the bootstrap gives t_n0 = O(ln^k Q) for N >= n0+2; and (M/Q)^(N-1-n) <= (M/Q)^2 for N >= n+3.

### [per_result 18]
Prop 5.8 (low moments iff the growth condition G): CORRECT. In the descending induction the bracket tends to 0 because the lower terms are O(y^(k-6)), and the (k-2)-subtracted relation then follows algebraically. The fixed-pole remark is correct.

### [per_result 19]
Theorem 5.9 and Theorem M: CORRECT as [R-cond: W, N1 (+N2, G, Phi)], and consistent with the spec's thm:dis-moments-np. The remark that E10 is avoided holds, since mass-independent MS-bar twist-2 RG has no lower-dimension mixing at rank n.

### [per_result 20]
E1-E6 (e+e- and the Adler function): CORRECT.
- E3: the recursion and the H_(k-1) coefficient were verified; b0 = beta0/4 in the CONTEXT conventions.
- E4: the integral is the b-derivative of the integral of t sin t/(t^2 + b^2), which equals (pi/2) e^(-b).
- E5: the Karamata, monotone-density, Karamata chain is correct; it needs R >= 0 and gives no rate in general.
- E6: the contour formula was re-derived from D(-q^2) = -12 pi^2 q^2 Pi'(q^2).
The grades are appropriate.

### [per_result 21]
Scripts f1, f2, h1, e1: all reproduce their logs byte for byte. Remaining issues:
- f1's checks (C1) and (C4) are tautological: the F0 coefficient is c_q^2 and the F1 coefficient is -c_p c_q.
- f1's random-graph 'classification of degenerate graphs' is heuristic, not a proof; the matroid criterion supersedes it.
- The class 'bridge carrying +-p' is an on-shell external propagator, excluded by amputation (the LSZ factor is 1 in massless DR); it is not a scaleless integral.
- h1(g) checks only the integrand identity.
- e1(c') computes M_k for R = s^(1/3) but checks nothing.

## required_fixes

### [required_fixes 1]
1. PIPELINE (orchestrator / parent). Save the author's StructuredOutput.summary verbatim to verify/extend/X3-ope/REPORT.md. Source: transcript agent-a924e58162fd27409.jsonl, StructuredOutput call at 2026-10-10T22:49:44Z, or the scratchpad copy x3rev/author/author_summary.md, with the results and open lists appended. Change the workflow so reviewers and fixers receive the report text inline, or so the parent persists every agent's output. Under the current harness rule no subagent can write REPORT.md or review_r*_k.md, so the fix rounds cannot update REPORT.md. X1 and X2 have the same problem.

### [required_fixes 2]
2. GRADES. Replace '[R-cited]' with monograph tags: Theorem A (A1),(A3), Theorem I and Corollary F.2 become [A] until open item O1 is done (read the full texts and record theorem numbers and hypotheses). State the slot outcomes explicitly:
- X3a FAILS (Remark A.6);
- X3b does not pass (prop:dis-ope-euclid stays [A]);
- X3c is not delivered;
- X3d is not verified for pure Yang-Mills and is [R-cond: E_eps] (about [A]) for QCD;
- X3e PASSES once fixes 3-5 are made.

### [required_fixes 3]
3. Add a lemma that discharges (F-DR) for ALL forward graphs, with this proof.
(a) F0 = Q^2 U(G/{J1=J2}) and, by deletion-contraction, U(G0) = x_q U(G) + U(G/{J1=J2}), where G0 = G + {J1J2}. So supp(U + F0) is the image of supp U(G0) (the bases of the cographic matroid M*(G0)) under the affine bijection x_q = L+1 - sum x_E.
(b) Feichtner-Sturmfels arXiv:math/0411260, Prop 2.4: dim P(M) = |E| - c(M). So the polytope is full-dimensional iff M(G0) is connected, i.e. iff G0 is loopless and 2-connected (Whitney).
(c) Prop 2.3 (with Prop 2.6 for flacets): every facet is x_e >= 0 or sum_{e in F} x_e <= r*(F) for a flat F. Mapped to R^N:
- x_e >= 0 gives u = e_e, d = 0;
- x_q >= 0 gives u = -1, d = -(L+1);
- a flat F not containing q gives u = -1_F, d = -r*(F), nonzero because G0 has no bridges;
- a flat F containing q gives u = 1_{E\F}, d = L+1 - r*(F) > 0.
So d_u = 0 only for coordinate facets, where <u,1> = 1. The poles a_e in -N0 never meet a_e >= 1, which also covers Tarasov shifts (D+2k, a+nu). Degenerate graphs are then handled by the scaling argument of (F3). This replaces the random-sampling classification; independent checks are in review_r1_1_checks/ (r1: 116/116 random graphs; r2: 45/45 targeted graphs).

### [required_fixes 4]
4. Theorem F hypothesis on spin sums: 'spin sums are polynomial in p' is false for gluon targets, whose physical projector has 1/(p.q)^k terms. The F2/FL projectors also have 1/nu^k terms (at p^2 = 0, T2 = Q^4 (3 ppT - (nu^2/Q^2) gT) / (2 nu^3)). Apply Theorem F to components contracted with tensors polynomial in p (for example ppT and gT, and the tensor components before polarization projection). Then show that the Taylor coefficients of T2 are the corresponding finite Laurent combinations, with negative powers cancelling by analyticity of T^{mu nu}. For gluons beyond one loop, use the physical projector or explicit ghost subtraction.

### [required_fixes 5]
5. Theorem F statement: (a) define the DR forward amplitude as the parametric (Speer-type) integral at p^2 = 0, and show it equals the Feynman-i-epsilon momentum integral for real |omega| < 1 (all coefficients positive) before continuing in omega; (b) give the colour argument for zero-momentum gluon bridges (no invariant tensor with one adjoint index for a colour-averaged target); (c) add the LSZ remark that external-leg corrections are excluded by amputation and that the on-shell Z = 1 in massless DR.

### [required_fixes 6]
6. Corollary F.2: derive the asm:appM-forward remainder bound, uniform in Euclidean directions, from the exact series via Cauchy estimates. Grade it [A] (inherited from Theorems A and B). Record asm:appM-forward as 'reduced to Theorems A and B', not discharged, and keep prop:dis-ope-forward at [A].

### [required_fixes 7]
7. Corollary F.3: downgrade 'Disc T2 = 4 pi i F2' to [A], or prove the DR cutting rules for Laurent coefficients including the distributions at x = 1. Delete 'at one loop it holds for all n >= 1 [R] (c_dis)', because c_dis covers only N <= 8 and assumes the dispersion relation. Alternatively, prove it for all N (one-loop large-|omega| bounds plus a count of subtractions); that would deliver slot X3c.

### [required_fixes 8]
8. Theorem B:
- cite the exact local BRST cohomology theorem used (including quarks and the trivial pairs (cbar, B));
- write out the degree matching in step 5 and the factors of i and signs in DR-SD;
- give an explicit one-loop example showing that the merged coefficients carry ln q^2, to support the claim that (B1) polynomiality is false;
- check novelty against the full texts of Joglekar 1977, Collins 1984 section 12.8 and Kluberg-Stern-Zuber 1975;
- put E_eps in the assumption register and grade the theorem [R-cond: E_eps].

### [required_fixes 9]
9. Remark F.5: replace 'answers the open question of Rem C.37' with 'expected from BM II; [A] pending O10'.

### [required_fixes 10]
10. Novelty markers:
- Theorem F and Lemma F.1: 'the book's rigorous proof' of the standard projection method, citing GLT PLB 124 (1983) 217, Gorishnii-Larin NPB 283 (1987) 452, and LNRV NPB 492 (1997) 338 around Eq. (29);
- Lemma F.0: elementary, not new;
- E5: classical method.
Any 本书新结果 marker still needs a second literature check (WRITER_SPEC_v2 section 6.5).

### [required_fixes 11]
11. Theorem A (A5): add the argument that the remainder is uniform in mu with polynomial ln mu dependence, so that it can be differentiated in mu. Note the inhomogeneous identity-operator term in the RG for the vacuum correlator (Part IV).

### [required_fixes 12]
12. Minor script and documentation fixes:
- f2 docstring: the parameters are real, not complex; report a tolerance for f2(B) (point 2 deviates by 1.2e-5);
- complete or delete e1(c');
- state that f1's (C1) and (C4) are identities;
- relabel the '+-p bridge' class as 'external-leg correction, excluded by amputation'.
