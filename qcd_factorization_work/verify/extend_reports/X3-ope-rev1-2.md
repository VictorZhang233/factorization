# X3-ope-rev1-2

(extracted verbatim from the workflow journal; structured output of the agent)

## overall

fixable_issues

## per_result

### [per_result 1]
[PROCESS — read first] REPORT.md does not exist. The X3 agent did try to write it, at 2026-10-10T22:40Z, and the harness blocked the write: 'Subagents should return findings as text, not write report files'. I watched for the file from 23:15 to 23:35 and it never appeared. The full report survives only as the X3 agent's StructuredOutput: summary §0–§10, 26 results and 11 open items, in workflow wf_52f29317-58b, agent a924e58162fd27409. I reviewed that final text in full, and also the 24k-character blocked draft. Two process consequences. (a) The draft's status table still lists 'Prop A.6: Ass. C.24 follows from Smirnov + uniqueness [R-cited], new observation'. The final text retracts this as circular (Remark A.6), so the saved REPORT.md must be built from the final StructuredOutput. (b) The same harness rule applies to me, so I did not write review_r1_2.md; this structured output is the review. My independent check scripts and logs are saved as data in .../verify/extend/X3-ope/review_r1_2_scripts/ (rv2_*.py plus logs/). Answer to the user's question ('is it running normally?'): the workflow runs, but every 'write REPORT.md / review .md' step silently fails. Unless the orchestrator saves the StructuredOutputs, later steps point at files that do not exist. This also explains why X1 and X2 have no REPORT.md. Reproducibility: all four X3 scripts (f1, f2, h1, e1) were re-run and reproduce their logs bit-identically.

### [per_result 2]
Thm A (Euclidean OPE for J J, full MS-bar basis). Verdict: GAP. It is graded honestly, but it does not qualify for PASS of slot X3b. (A1) and (A3) rest on three papers read only at abstract or author-review level: Smirnov CMP 134 (1990) 109 (title checked on INSPIRE: 'Asymptotic expansions in limits of large momenta and masses'), Gorishny NPB 319 (1989) 633, and Llewellyn Smith–de Vries NPB 296 (1988) 991. [R-cited] is therefore the right grade. The [R, R_PT] (cited) tag requires checked theorem locations and hypotheses: uniformity in direction and on compact non-exceptional p-sets, the operator form with ghosts and gauge-variant operators, and finiteness of C^bare Z^-1. The report's own open item O1 says this is not done. (A2) and (A5) are correct, but they presuppose (A3) finiteness and (A1); their grade should read '[R] given A1, A3', not plain [R]. (A4) with Lemma A.3 is correct.

### [per_result 3]
Lemma A.3 (linear independence of operator Green functions). CORRECT. The proof is an induction in g^2 at fixed epsilon, using injectivity of the tree vertex polynomials of a monomial basis and separation of distinct homogeneity degrees |q|^(2-d-2k*eps).

### [per_result 4]
Remark A.6 (CLAIMS R-M26 is circular). CORRECT and important. I re-derived the circularity. G^T = sum C' G_N[O] + R' with R' small (cited theorem), and G^T = sum C~ G_N[O] + N~_a (exact identity). Uniqueness (a) applied to sum (C~ - C') G = R' - N~_a needs the smallness of N~_a, which is asm:appM-remainder itself. So the planned X3a route in spec_v2/OUTLINE_appMNOPQ.md ('by lem:appM-uniqueness(a) ... hence asm:appM-remainder holds') is circular: X3a FAILS as planned and the fallback applies. One possible way to close it, which the X3 author should examine: in the massive model N~_a is over-subtracted at p=0. Comparing p-derivatives at p=0 of the two representations would give the identification lemma (O3), provided the cited remainder R' comes with q-uniform bounds on its p-derivatives at p=0.

### [per_result 5]
Thm B (BRST / gauge-invariant reduction). Verdict: GAP. The logic is sound but the result is conditional, and the novelty is unverified. I checked steps 1–6. s J = 0. DR-WI combines the spectator-outside terms into -/+ sum C_O <(sO)Phi>. The merged coefficients C^{s phi}(q;p_k) are polynomial in p_k (E_eps). The SD contact terms of <(O' C(q;-i d) dS/dphi)(0) Phi> reproduce them leg by leg, with the same p_k and signs (delta(0)=0). Lemma A.3 at fixed epsilon then gives sum C_O sO = +/- E, an element of the EOM ideal. So sX_d lies in the EOM ideal, not sX_d = 0. This is a genuine correction of the reference's Prop C.44 and of the spec's prop:dis-ope-gi plan, which claim X_d is classically BRST-closed and thereby drop the merged terms. The final conclusion (GI + s-exact + EOM) survives through the on-shell cohomology. Problems. (i) The grade should be [R-cond: E_eps, LBC]. E_eps, the expansion with one composite spectator, lies within K2 only at [R-cited] level (O1). LBC must be the on-shell cohomology for the gauge-fixed s, which is cited and not proved. (ii) 'New proof' is not established: Joglekar 1977 I/II, Hollands 2008 and Fröb–Holland 2016 were read only at abstract level. (iii) Reword the critique of (B1). In DR, <T J sPhi> = 0 exactly, so the total contact term of (B1) is trivially polynomial. What fails is the implicit omission, in (B2)/C.44's proof, of the merged OPE terms, which carry logs and are EOM operators. Slot outcome: X3d PARTIAL. asm:appM-brst-ope can be replaced by the weaker input E_eps plus cited LBC, and the prop:dis-ope-gi proof plan must be corrected.

### [per_result 6]
Thm I (= A + B + twist classification). Consistent with its inputs, at [R-cited]. It does not support upgrading prop:dis-ope-euclid or prop:dis-ope-gi beyond [A] until O1 is done (decision D3 stands).

### [per_result 7]
Lemma F.0 (forward Symanzik structure F = Q^2(F0 + omega F1)). CORRECT. I recomputed U, F0 and F1 independently with the network / matrix-tree method: U = prod(x) det L_red(1/x) and F/U = P^T L_red^-1 P. The result is identical to my own forest enumeration on 60 random graphs and on every explicit topology. Domination is trivial, since |c_p| <= 1 <= |c_q| whenever c_q is nonzero. f1's random tests of C1 and C4 therefore add nothing beyond this lemma.

### [per_result 8]
Lemma F.1 (Newton-polytope domination). CORRECT. Points checked: (a) The coefficients c_m(1 + lambda theta_m), |theta_m| <= 1, lie in the sector |arg| <= arcsin r. This is exactly the 'open strongly convex cone' hypothesis of Schultka arXiv:1806.01086 Thm 3.1, which I read in §3. Because mon(F1) is contained in mon(G0), d_rho(F1) >= d_rho(G0), so the λ=0 convergence condition implies that of every Taylor term. (b) sum |binom(-c,n)| r^n <= (1-r)^-|c| gives dominated convergence. (c) On Kaneko–Ueda cubes the monomial map is injective, so monomial-wise domination survives and Re f_{sigma,lambda} >= (1-r) f_{sigma,0} >= c0 > 0. The Taylor identity for each n then extends by uniqueness of meromorphic continuation.

### [per_result 9]
Thm F (forward on-shell DR amplitude: cut-plane holomorphy, Taylor series = naive expansion). Verdict: CORRECT given (F-DR), but GAP as stated. (i) (F-DR) is asserted to 'hold unless scaleless' without proof, yet Cor F.2 uses it for every graph at every order. It is checked only on 21 + 34 graphs. (ii) As formulated (the DR line a=(1,...,1) only) it is too weak for the Tarasov-reduced tensor integrals, which have raised powers a_e >= 1 and dimension D+2k, and for the Taylor terms. What is needed: no D-independent polar hyperplane meets {a_e > 0}. (iii) A proof I supply (rv2_matroid.py, rv2_facets_d0*.py). supp(U+F0) equals the set of complements of spanning trees of Gamma+ = Gamma + {virtual edge J1J2}, with the virtual coordinate dropped. I verified this on all 21 f1 graphs and 226/226 random graphs. Hence Newt(U+F0) is affinely isomorphic to the base polytope of the cographic matroid M*(Gamma+), which has two consequences. dim = |E+| - #components, so the polytope is full-dimensional iff Gamma+ is 2-connected and loopless; my block criterion agrees with exact rank on 1500/1500 random graphs. Edmonds' description B = {x >= 0, x(S) <= r*(S), x(E+) = L+1} lists every facet: coordinate (d=0), -1_S (d = -r*(S) < 0), 1_{E minus S} (d = L+1-r*(S) > 0), and -1 (d = -(L+1)). So the only D-independent poles are a_e in -N0, and DR is admissible for all positive powers. Numerically, every d=0 facet is a coordinate facet in 21/21 f1 graphs and in 185/185 + 68/68 random full-dimensional graphs, each facet verified exactly. The printed normals match the r* formulas, e.g. (1,0,0,0,1,1,1) has d=1 for the planar ladder. With this lemma Thm F becomes unconditional for amputated graphs with Gamma+ 2-connected; all others are scaleless (F3). (iv) Wording: 'contracted with p-independent tensors' should read 'contracted with tensors polynomial in p or homogeneous of degree 0'. That covers p-slash spin sums, physical gluon sums (pn+np)/(p.n), and the p_mu p_nu of the T2 projector. For p^2=0 the projector has P^2 = omega^2 Q^2/4, a harmless exact 1/omega^3 division. In DR the D-dimensional projector T2 = nu[(D-1)PPT - P^2 gT]/((D-2)(P^2)^2) must be used. (v) An independent two-loop test that X3 did not do (rv2_ladder2.py): the planar forward ladder with all seven powers free. The exact on-shell amplitude is computed by turning the inner light-like triangle into an Euler superposition of propagators ((k+tp)^2)^-A; the outer triangle then sits at argument -t*omega. Its omega^n coefficients equal the nested naive tensor terms identically in (a1..a7, D) for n=0..5 (sympy ratio = 1), and numerically to 1e-11–1e-13 at 4 random points. I re-derived the triangle closed form by my own Feynman-parameter quadrature. Novelty: this is the 'method of projectors' (Gorishny–Larin–Tkachov PLB 124 (1983) 217; Larin et al. NPB 492 (1997) 338, eqs. 29–32). The latter says the method 'implicitly involves a considerable rearrangement of IR and UV divergences' and gives no proof. Semenova–Smirnov–Smirnov EPJC 79 (2019) 136 prove expansion by regions only at leading order, or with one essential facet, for positive coefficients, and only as an asymptotic expansion. I found no rigorous convergent-Taylor proof, so 'new rigorous proof of a folklore statement' is plausible. A dedicated check of Tkachov 1992–97, Chetyrkin arXiv:1701.08627 and Smirnov's books is needed before any 「本书新结果」 marker.

### [per_result 10]
Cor F.2 (forward partonic OPE at every order). CORRECT given Thm F, (A3), Thm B and K3; grade [R-cited]. I checked the key steps. The forward graphs are exactly the AI two-leg hard graphs: a non-AI graph has a bridge of Gamma/(J1=J2) carrying 0 or ±p. Hence sum over Gamma of naive(Gamma) = sum C^bare_O V_O(p,-p) is literally the combinatorial definition of C^bare in (A3). On-shell loop matrix elements are scaleless. Aliens have zero tree matrix elements and mix only into aliens. My earlier worry, that the naive terms must be identified with C~ Z^-1, is resolved by (A3) at cited level. Required changes: the hypothesis list must include (F-DR), or the matroid lemma. For the slots, asm:appM-forward is not discharged to [R]; it is reduced to (A3) of prop:dis-ope-euclid. Under D3, prop:dis-ope-forward therefore stays [A], with its bottleneck now A3 + E_eps instead of asm:appM-forward. Equivalently it is [R, R_cond: A3, E_eps].

### [per_result 11]
Cor F.3 (perturbative cut-plane analyticity, discontinuity, moments). OVERGRADED: GAP. (a) Holomorphy on the cut plane: [R]; it follows from F1. (b) 'Disc = 4 pi i F2^(j) [R]' needs the cutting rules for the DR-continued amplitude, i.e. the identification of the discontinuity with cut diagrams. The report's own K10 grades exactly this cut identification as [A], which is inconsistent. It should be [A] unless F2^(j) is simply defined as Disc/(4 pi i). (c) 'At one loop it holds for all n >= 1 [R] (c_dis)' is unsupported. research/c_dis/DERIVATION.md §11 checks only N <= 8 (ope_check_N8.log), and N <= 6 for the MS-bar coefficients. Slot X3c (all N at one loop) is therefore NOT delivered.

### [per_result 12]
Examples F.3/F.4. CORRECT. f2 reproduces bit-identically. The triangle 2F1 closed form was re-derived by my own 2-d quadrature in the convergent region. F.4's ln(Q^2/P^2)+2 follows from integral of ln[t(1-t)] = -2. At a_i=1 the omega^n pole is -1/((n+1) eps), as in the f2 log. Minor: f2 (B) agrees with the quadrature only to 1.2e-5 at its second point (endpoint singularity (1-y)^-0.8). Report this as quadrature accuracy.

### [per_result 13]
Remark F.5 (zero-momentum twist-2 insertions IR finite by Breitenlohner–Maison II). Graded [A], which is fine. But 'answers the open question of Rem C.37' overstates an unchecked application of BM II to an exceptional (zero-momentum) insertion. Reword to 'indicates'.

### [per_result 14]
Lemma 4.10 (the hadronic step needs exactly the segment approximation SA). CORRECT as a logical statement.

### [per_result 15]
Lemmas 5.1–5.2 (Euclidean segment; standard non-perturbative OPE implies SA). CORRECT. I re-derived the geometry: nu = iMq4, P^2 = M^2 qvec^2/Q^2 >= M^2/4, |omega| <= sqrt3 M/Q. Analytically |Pi_2| <= 20 Q/M (h1 finds 6.06 numerically). The size of each term, nu b_j ~ (M/Q)^(t-2+2b) omega^(r-1-2b), follows from dimensional analysis. The odd part of an eps-approximation of an odd function is again an eps-approximation. The case analysis (trace terms M^2/Q^2; twist 3 with chiral suppression mM/Q^2; twist >= 4) is consistent.

### [per_result 16]
Lemmas 5.3–5.5 (Markov, Jensen, boundary values). CORRECT. Markov: |c_k| <= |Re c_k| + |Im c_k| <= 2 max|coef T_D|, and sum |coef T_D| = |T_D(i)| <= (1+sqrt2)^D. Jensen: J(y) is the Green function of [-2,2] (w -> i(w-1/w) maps the unit circle onto the segment), so J >= 0. The subharmonic mean on radius-2 circles then gives |f| <= C(3+|z|)^A, and Cauchy's estimates finish the proof. 5.5(a): a bump with |chi^(j)| <~ R^-j gives nu([R,2R]) <~ R^(A+1).

### [per_result 17]
Prop 5.6 (dispersion relation from W1–W3). CORRECT at [R-cond: W], with one sketch-level step. Checked: crossing (A(z) = R^T(-z)) makes T2 odd. S1 and S2 are even in s, hence functions of s^2. I derived the slice inequality in closed form: w2^2 - (Im s)^2 = 2 w2^2 Q^2/(B + sqrt(A^2 + 4 w1^2 w2^2)), with A = w1^2 - w2^2 + Q^2 and B = |w|^2 + Q^2; numerically exact. The removable point q = (iQ, 0) gives T2 = Q^4 (b + a/Q^2)/nu. W = 0 for |omega| < 1 by the spectral condition in H_T. The bound |1 - x^2 omega^2| >= (Im omega)^2/|omega|^2 is proved: for x >= 1/|omega| use |1 ± z| >= |Im z|; for x < 1/|omega| minimise over r <= 1 (numerically the minimum ratio is 1.0008). The condition n0 > A+1 by dyadic summation is correct and sharper than the spec's n0 > A+2. The entire-function argument (Lemma 5.4, then H(iy)/(iy)^(n0-1) -> 0) is correct. Sketch-level: restricting the 4D distributional identities and positivity to every fixed-Q^2 slice via the 'primitive representation'. One must show that the K-fold w-primitives of T2(w, Q^2) are jointly continuous up to the boundary, for example from joint holomorphy in (w, Q^2) and the Q-uniform Vladimirov exponents.

### [per_result 18]
Thm 5.7 (fixed-n Taylor coefficients). CORRECT. The tail is <= 2 t_n0 r_Q^(N-1) for r_Q <= 1/sqrt2. Markov then applies on I_Q. The bootstrap gives t_n0 = O(ln^k Q), because 2c r_Q^(N-n0) <= 1/2. Hence |t_n - pi_n| = O((M/Q)^(N-1-n)) = O(M^2/Q^2) for N >= n+3, and the result holds for every even n >= 2.

### [per_result 19]
Prop 5.8 (low moments iff growth condition G). CORRECT. The descending identity is verified algebraically. Sufficiency uses monotone convergence; necessity uses dominated convergence. The remark that a fixed pole c*omega is invisible in F2 is right.

### [per_result 20]
Thm 5.9 + Thm M (hadron-level DIS moment theorem). CORRECT as conditional statements. The remark that twist-2 MS-bar RG has no mass mixing is correct for the symmetric spin-n sector, since there are no twist-1 operators. This is a re-proof and refinement of the reference/spec structure, not a literature novelty.

### [per_result 21]
E1 (Källén–Lehmann; one subtraction iff D finite at one point). CORRECT. V1 excludes massless spin-0 states coupling to J.

### [per_result 22]
E2 (Adler-function asymptotics, no 1/Q^2 term in the chiral limit). CORRECT as a conditional statement.

### [per_result 23]
E3 (Euclidean moments M_k). CORRECT. The recursion M_{k+1} = M_k - (Q^2/k) dM_k/dQ^2 is re-derived. The H_{k-1} b0 d1 term is verified. The explicit 'derivative bounds' hypothesis is what licenses term-by-term differentiation. b0 = beta0/4 for a = alpha_s/pi, consistent with CONTEXT.

### [per_result 24]
E4 (exact duality-violation counterexample). CORRECT. Differentiating integral of t sin t/(t^2+b^2) dt = (pi/2) e^-b with respect to b gives (pi/2) e^-b/b. Hence D = R0[1 + kappa (pi/2)(Q/Lambda) e^(-Q/Lambda)]. The conclusion is even stronger than stated: the model satisfies a sectorial OPE for every fixed theta0 > 0, since Re sqrt(Q^2) >= |Q| sin(theta0/2). 'Known in spirit' is correct (Shifman; Blok–Shifman–Zhang).

### [per_result 25]
E5 (Karamata Tauberian theorem: Cesàro mean of R tends to R0). The PROOF is CORRECT: Karamata as u -> 0, the monotone-density step with lambda -> 1, then Karamata again. The novelty claim 'new in this context' should be dropped; the argument is classical. Tauberian remainders from power-law Euclidean errors are only logarithmic in general, consistent with O9.

### [per_result 26]
E6 (PQW smearing). CORRECT. The exact identity 12 pi Im Pi(s+i Delta) = (1/2pi) integral of D(|s+iDelta| e^{i phi}) dphi over |phi| <= pi - theta is re-derived from dPi = -D dQ^2/(12 pi^2 Q^2). Graded [R-cond: V2'], which is fine. Not new (Poggio–Quinn–Weinberg 1976).

### [per_result 27]
Verification log (f1, f2, h1, e1). Reproduced. f1's numerical C2/C3 evidence is now superseded by the matroid-base-polytope lemma. h1's identities are all re-derived analytically: projector, removable point, slice inequality, dispersion normalization 4 pi i, descending identity.

## required_fixes

### [required_fixes 1]
Orchestrator: save REPORT.md for X3 from the X3 agent's final StructuredOutput (summary + results + open, workflow wf_52f29317-58b, agent a924e58162fd27409), not from the blocked 24k draft. The draft still contains the retracted 'Prop A.6: C.24 follows via uniqueness [R-cited]'. Do the same for X1/X2 and for review outputs. Subagent .md writes are blocked by the harness, so steps that point to REPORT.md / review_r1_*.md files currently read nothing.

### [required_fixes 2]
Thm F / Cor F.2: replace the unproved hypothesis (F-DR, 'true unless scaleless') with a lemma. Newt(U+F0) is affinely isomorphic to the base polytope of the cographic matroid of Gamma+ = Gamma + {J1J2}; its support is the set of complements of spanning trees of Gamma+ with the virtual coordinate dropped. Consequences: full-dimensional iff Gamma+ is 2-connected and loopless; by Edmonds' description every facet has normal e_e (d=0), -1_S (d = -r*(S)), 1_{E minus S} (d = L+1-r*(S)) or -1. So the only D-independent poles are a_e in -N0, and DR is admissible for all positive powers, which covers the Tarasov raised powers and the Taylor terms. Evidence: review_r1_2_scripts/rv2_matroid.py and rv2_facets_d0*.py. Add this lemma, or (F-DR) in the strengthened form, to the hypothesis list of Cor F.2.

### [required_fixes 3]
Thm F wording: 'contracted with p-independent tensors' must become 'contracted with tensors polynomial in p or homogeneous of degree 0 in p' (p-slash spin sums, physical gluon sums, p_mu p_nu in the T2 projector). For partonic T2 in DR state the D-dimensional projector nu[(D-1)PPT - P^2 gT]/((D-2)(P^2)^2), and note that the exact 1/omega^3 from P^2 = omega^2 Q^2/4 is harmless.

### [required_fixes 4]
Cor F.3: downgrade 'Disc = 4 pi i F2^(j)' to [A] (cutting rules in DR; this matches the report's own K10), or state that F2^(j) is defined as Disc/(4 pi i). Delete '[R] at one loop for all n >= 1 (c_dis)': c_dis covers only N <= 8 (N <= 6 for MS-bar coefficients). Record slot X3c as NOT delivered, or supply an all-N one-loop proof including the unsubtracted dispersion relation at one loop.

### [required_fixes 5]
Slot decisions to record in the verify patch. X3a: FAIL as planned (circular, per Remark A.6); keep asm:appM-remainder, list O3 (identification lemma), and optionally try comparing p-derivatives at p=0. X3b: not PASS ([R-cited] from abstracts; full texts of Smirnov 1990 / Gorishny 1989 / LS–dV 1988 needed, O1); prop:dis-ope-euclid stays [A] under D3. X3d: PARTIAL, replacing asm:appM-brst-ope by E_eps + LBC. X3e: PASS candidate for Thm F after the matroid lemma, pending a second independent confirmation. Cor F.2 then reduces asm:appM-forward to A3 + E_eps, so prop:dis-ope-forward stays [A] under D3, or becomes [R, R_cond: A3, E_eps].

### [required_fixes 6]
Thm B: regrade as [R-cond: E_eps, LBC (on-shell cohomology for gauge-fixed s, cited)]. Change the spec's prop:dis-ope-gi proof plan from 'X_d classically BRST closed' to 'sX_d lies in the EOM ideal'. Reword the critique of (B1): in DR <T J sPhi> = 0 exactly, so the defect is the omission of the merged OPE terms (log-carrying EOM operators) in (B2)/C.44, not the polynomiality of the total contact term. Withhold 'new proof' until Joglekar 1977 I/II, Hollands 2008 and Fröb–Holland 1603.08012 have been read in full.

### [required_fixes 7]
Thm A: state that (A2) and (A5) are [R] given (A1) and (A3) (finiteness of C^bare Z^-1), not unconditionally [R].

### [required_fixes 8]
Prop 5.6: make the slice-restriction step explicit. Prove that K-fold w-primitives of T2(w, Q^2) have boundary values jointly continuous in (Re w, Q^2), e.g. from joint holomorphy of the slice parametrisation in (w, Q^2) plus the Q-uniform Vladimirov exponents, so that the 4D identities and positivity hold on every fixed-Q^2 slice and not only for almost every Q^2.

### [required_fixes 9]
Remark F.5: change 'answers the open question of Rem C.37' to 'indicates (at [A]; BM II hypotheses for zero-momentum composite insertions not checked)'.

### [required_fixes 10]
Novelty markers: no 「本书新结果」 for Thm F, Thm B, E5 or Lemma F.0 without a dedicated literature check. Thm F: Tkachov 1992–97, Chetyrkin arXiv:1701.08627, Smirnov 1991/2002 books; Larin et al. NPB 492 (1997) 338 shows the method is used without proof. Thm F should cite Gorishny–Larin–Tkachov 1983, Larin et al. 1994/1997, Semenova–Smirnov–Smirnov EPJC 79 (2019) 136, Jantzen JHEP 12 (2011) 076, Schultka 1806.01086 and Berkesch–Forsgård–Passare 2014. Drop E5's 'new in this context' (classical Tauberian argument). Suggested wording for Thm F: 「本书给出的严格证明（该方法在文献中作为 method of projectors 使用）」.

### [required_fixes 11]
Minor: in f2 (B) state that the second test point agrees with the quadrature only to 1.2e-5 (endpoint singularity), or improve that quadrature. In f1, note that C1 and C4 hold identically by Lemma F.0 (|c_p| <= 1 <= |c_q|), so the random tests of them carry no extra evidence.
