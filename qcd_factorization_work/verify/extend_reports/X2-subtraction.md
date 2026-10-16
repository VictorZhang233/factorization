# X2-subtraction

(extracted verbatim from the workflow journal; structured output of the agent)

## summary

RUN STATUS (answer to the relayed user question "在正常运行吗"): yes, the X2 subagent ran normally and completed. Every computation finished and was verified. One deviation: the Write tool refused to create verify/extend/X2-subtraction/REPORT.md ("subagents should return findings as text"). I did not work around that block, so the report content is given here in full (results + open). The orchestrator can write REPORT.md verbatim from these fields. All scripts and logs are in verify/extend/X2-subtraction/{scripts,logs}.

TOPIC. App. D proves its precise subtraction theorem (Thm D.10) only under (H1)-(H3) (= our CS1-CS3), (A1)-(A4) and D.14/D.27/D.37/D.43. Even for the one-loop triangle only "key points" are given. Here those hypotheses are actually verified for explicit graphs and for infinite classes, at sharp powers where possible.

MAIN RESULTS (details in `results`; "ca" = computer-assisted: LP optima re-verified exactly in rational arithmetic plus exact recession-slope checks):

(1) Fibered subtraction theorem [R, new formulation]. (H1)-(H3) are put on the light-cone base, with all minus components integrated exactly by residues. Thm D.10 holds verbatim, the 4D contour assumption (A1) disappears, and the Glauber region never appears.

(2) LP/tropical certificate lemma [R]. Integral-norm bounds for explicit fibered densities reduce to linear programs over Newton-polytope data (Borinsky's tropical approximation, Hoffman bound).

(3) One-loop off-shell Sudakov triangle, complete verification [R, ca]. On a 2x2 cover at the natural soft scale (s=lambda^2), every (H1)/(H2) item is <= C lambda^2 L^2, which is the sharp exponent. (H3) holds for 0<eps<1. Remainder norm <= C lambda^2 L^2 (numerically ~4 lambda^2 L, one log more than |int r| = 4m^2/Q^4).
- Correction to my own intermediate claim and to App. D's Lesson (d)/Def D.5: fat neighbourhoods are unnecessary and harmful. With s=lambda^theta the item int_{U_S} C_{C1} >= s/4, so the theorem's exponent is theta; theta=2 is optimal.
- The negative-k+ sliver carries exactly zeta_2/Qt^2 of the integral and -2m^2/Qt^4 of the remainder.

(4) Infinite class I: renormalized bubble chains (log insertions ln^j D_g, all j) [R, ca]. A new exact "rectangle rule" relates the gluon-virtuality logarithms on the four line-1 shells. With it, all items and the remainder are <= C_j lambda^2 L^{j+2}.

(5) Infinite class II: DIS ladders of every length n in phi^3_6 (off-shell target, unphysical region x>1) [R]. Ingredients: an exact positive light-cone representation, the exact product/difference structure of all Collins terms, and an L^1-Hoelder induction built on an exact 1D reduction of the rung kernel. Result: (H1)-(H3) hold for all n on an explicit cover, with full-norm remainder <= C_n lambda (1+L)^n. Numerically this first order is genuine (1.263 lambda for n=1); the azimuth-averaged norm is second order.

(6) All one-loop DIS graphs in phi^3_6 verified [R].

(7) Abelian massive photon (on-shell massless legs) [R].
- Light-like approximators: r = (1/G - 1/g0) delta1 delta2 exactly, and int r = -lambda^2(L+1) - lambda^4(L/2+1/4) + ... . Yet (H3) fails for C_S and C_C1/C_C2 for every eps (rapidity divergences). So Thm D.10 is inapplicable although its conclusion holds.
- Time-like rapidity regulators restore (H3), with window Y >= L/2.
- Space-like regulators (App. D Def D.21) pinch the virtual soft subtraction term.

(8) Two-loop planar Sudakov vertex. Exact algebra [R]: the 12-edge Hasse diagram, meet closure, (Com), and (Abs) only with a "soft-first" convention; with the naive one (Abs) fails in 4 explicit cases, correcting Lemma D.23(iii). Double-residue densities validated against Usyukina-Davydychev Phi^(2). Numerically [P]: remainder full light-cone norm ~31 lambda L (first order, from angle-odd hard-loop projection errors), azimuth-averaged norm second order, int r ~ -4.7 m^2 L^3.

(9) All orders. Precise conditional theorem for the Sudakov form factor, with a hypothesis-status table. Light-cone positivity, and hence (H3) for Gamma, is proven at all orders in the scalar model. General (H1)/(H2) remain the open [A] input.

Not verified: gauge-theory numerators (the one-loop QCD vertex with P_A/K-gluon projections), crossed and non-planar two-loop graphs, and two-loop graphs with UV subdivergences (quark self-energy and vertex subgraphs). These are listed as open.

## results

### [results 1]
[X2-Thm2.6] Fibered (light-cone) subtraction theorem. Setting: integrands in V = finite sums of products prod_j (a_j(b)+sum_i beta_ji(b) k_i^- - i0)^(-e_j) times measurement functions of the base b=(k_i^+,k_iT). Every Feynman propagator -(V)^2 = -2V^+V^- + V_T^2 is jointly affine in the minus components, and all approximators of Defs D.18/D.19 preserve V. Fibered density rho_F(b) = prod_i (i pi^{d/2})^{-1} int dk_1^- ... dk_l^- F, evaluated by residues (decay <= -2 in each variable), with infinitesimal imaginary parts tracked affinely (pole upper iff w/beta>0). Fibered conditions: (H1^phi)_R0: int_{U_R0}|rho_{(1-T_R0)X_R0}| <= C lambda^a L^K; (H2^phi)_R0: the same for C_R Gamma, R not<= R0; (H3^phi): rho_Gamma in L^1 uniformly in eps in [0,eps0], rho_{C_R Gamma} in L^1 for each eps in (0,eps0]. Statement: these imply int_B |rho_Gamma - sum_R rho_{C_R Gamma}| <= C lambda^a L^K and |I_Gamma - sum_R int rho_{C_R}| <= C lambda^a L^K. Grade [R]. NEW formulation; the proof is that of Thm D.10, since residue sums are linear and identity (D.10) holds fiberwise. Gains: no contour hypothesis (A1); the Glauber region is integrated exactly (Ex. D.47's (D.28) vanishing linearly at k+->0 is the fibered statement); error type E-F. Caveats proven here: (a) literal (H3) of Def D.9 on the real contour fails already for Gamma (log divergence across light cones); (b) non-maximal U_R must be UV-bounded, because individual subtraction terms carry UV logs not uniform in eps (triangle: int_{U_C1 cap k+>P}|rho_{C_C2}| ~ s/eps); (c) the fiber is part of the statement: adding transverse azimuths to the fiber changes first-order norms to second order (see X2-Num-2loop, X2-Num-DIS). Engine: scripts/lcpt.py, validated by t7_lcpt_validate.py (all 5 triangle densities at 2000 points, rel. dev <= 3e-10) and t9_twoloop_checks.py (order independence 5e-10, exact weight independence).

### [results 2]
[X2-Lem2.8] Tropical (LP) certificate lemma. Let f = N/prod_k D_k on local coordinates y_i=e^{L X_i}, m^2=e^{-L} (L=ln 1/lambda^2), with N real-coefficient and D_k comparable to positive polynomials g_k. psi_a(X) = <a+w,X> - a_m - sum_k max_{b in supp g_k}(<b,X>-b_m) for each monomial a of N. On a polyhedron U where every psi_a has bounded argmax face F_a: int |f| prod y^{w-1} dy <= C L^d lambda^{-2 phi*}, phi* = max_a max_U psi_a, d = max dim F_a. Proof: Borinsky arXiv:2008.12310 Thm 8.A/B (|N| <= sum|c_a| y^a; positive g_k >= min d_kb max monomial); concavity of psi_a plus Hoffman's bound on finitely many affine cells gives psi*-psi >= c dist(X,F_a); Laplace estimate. Grade [R]. Implementation: scripts/tropical.py (HiGHS LP per monomial); scripts/exact_verify.py reconstructs exact rational dual certificates (weak duality gives an exact upper bound; face dimension <= (n+K)-rank, exact); scripts/recession.py checks exactly that every psi_a has strictly negative asymptotic slope on all recession rays of unbounded cells (needed for convergence; a bounded LP alone is not enough). Uniformity in eps: weight w_kappa = 1-eps; the LP value is convex piecewise linear in eps, so the endpoints suffice; loss of at most lambda^{-4 eps0}.

### [results 3]
[X2-Lem2.10/Cor2.11] Light-cone positivity, all orders (scalar cubic theory, massless internal lines). (a) Sudakov kinematics (M1): p1=(P,-m^2/2P,0), p2=(m^2/2P',-P',0), both incoming, current outgoing at one vertex. (b) DIS forward amplitude (M2) in the frame q^+=0, x>1. Statement: rho_G(b) is a finite sum over x^+-orderings of terms prod(2l^+)^{-1} prod_states (E_st - sum l_T^2/2l^+)^{-1} with every energy denominator strictly negative. In (a) the current vertex is last (plus-momentum conservation), so E_st is in {p1^-, p2^-, p1^-+p2^-} < 0 and |denominator| >= m^2/2P. In (b) convexity gives sum l_T^2/2l^+ >= q_T^2/(2 xi p^+), so |denominator| >= xi (m^2+Q^2(1-1/x))/2p^+. All orderings have the same number of states (2l for the vertex, 2l+1 for DIS), so rho_G has a definite sign and int|rho_G| = |I_G|. Corollary: (H3^phi) for Gamma holds at all orders for UV-finite graphs (every (M1) graph without self-energy subgraphs; every DIS ladder). Grade [R], given the standard derivation of light-cone ordered PT from Feynman integrals (Chang-Yan, PRD 7 (1973) 1147; Ligterink-Bakker, PRD 52 (1995) 5954, hep-ph/9412315; no zero modes since every loop has >= 2 propagators depending on its k^-). Positivity verified numerically at one and two loops (t1, t9). NEW as a formulation and application.

### [results 4]
[X2-Lem2.12] One-dimensional reduction of rung kernels (d=6). Definitions: parent (v,K), child fraction z, child transverse momentum k, child virtuality v' = z v + |k - zK|^2/(1-z), kernel kappa = 1/(pi^2 (1-z) v'^2). Statement: for every F >= 0, int d^4k kappa F(v') = (1-z) int_{zv}^infty dt (t-zv) F(t)/t^2 <= (1-z) int dt F(t)/t; the projected parent (v=0,K=0) gives (1-z) int_0^infty dt F/t. Proof: l=k-zK, d^4l = pi^2 |l|^2 d|l|^2, |l|^2 = (1-z)(t-zv). Grade [R], NEW. The d=6-2eps version has (1-z)^{1-eps} c_eps int (t-zv)^{1-eps} F/t^2.

### [results 5]
[X2-Prop3.1] One-loop off-shell triangle: fibered densities (re-derived independently; agree with R6). Units and kinematics: k+=x, kappa=kT^2, u=x/P, Qt^2=2PP', e2=m^2+2P'x, h2=2P'x, A = x m^2(1-u) + P kappa, B = x m^2 + P kappa, a=m^2/P', w=2x+a. Densities: rho_Gamma = 1/(A Dhat2) with Dhat2 = e2[1+m^2/Qt^2+kappa/(Qt^2(1-u))] + kappa (0<x<P); rho_CS = 1/(B e2) (x>0); rho_CC1 = x m^2/(Qt^2 A B) (0<x<P), -1/(h2 B) (x>P); rho_CC2 = -1/(P e2 (e2+kappa)) (x>0), w/(P[(a-w)P'w + a kappa](P'w+kappa)) (sliver -a/2<x<0); rho_CH = -x/(P(h2+kappa)(h2(P-x)+P kappa)) (0<x<P), 1/(P(h2+kappa)h2) (x>P); rho_Gamma on the sliver = 2/(w Dg D1) at k^- = P'+kappa/w, Dg = [(a-w)P'w + a kappa]/w. Normalization: mu^{2eps} int d^dk/(i pi^{d/2}) F = (mu^{2eps}/Gamma(1-eps)) int dx dkappa kappa^{-eps} rho_F. Checks: symbolic residues = closed forms (t1); direct k^- integration at eta=1e-7; int rho_Gamma = Usyukina-Davydychev Phi^(1)(t,t)/Q^2. (H3^phi): rho_Gamma >= 0 and finite uniformly; each rho_{C_R} is in L^1 exactly for 0<eps<1 (UV at kappa,x->inf needs eps>0; the x->P endpoint needs eps<1). Grade [R]. Closed forms known (App. D Ex. D.47 / R6); independent verification here.

### [results 6]
[X2-Prop3.2] The negative-k+ sliver of the triangle (NEW). Region: -m^2/(2P') < k+ < 0, i.e. the B-collinear gluon carries negative plus momentum. Statements: int_sliver rho_CC2 = zeta_2/Qt^2 EXACTLY, to all orders in m (int dkappa rho_CC2 = ln(a/(a-w))/(PP'w), then int_0^a (dw/2)(...) = Li_2(1)/(2PP')). int_sliver rho_Gamma = zeta_2/Qt^2 + O(m^2/Qt^4), so half of the pi^2/3 in (D.32) comes from the sliver. int_sliver r = -2m^2/Qt^4 + o(m^2): r = -(2/(w Dg))(m^2(1-x/P)+Dg)/(D1 h1) has two negative terms, each integrating to -m^2/Qt^4. This is half of the total remainder -4m^2/Q^4. Grade [R] (analytic). Numerics: int rho_Gamma(sliver) = 1.644934 at lambda^2=1e-6; sliver remainder -1.99979, -2.00000 lambda^2 at lambda^2 = 1e-4, 1e-6 (t2b, t2c). Exact LP certificate of the sliver at lambda^2 (t4z: two sub-domains, 0 failures).

### [results 7]
[X2-Thm3.3] One-loop triangle: Collins conditions verified at the SHARP exponent (NEW). Cover in units Qt=1, u=k+/P, y=kappa/(2k+), s=lambda^2=m^2/Qt^2 (natural soft scale): U_S = {0<u<=s, y<=s}; U_C1 = {s<u<=2, y<=s}; U_C2 = {0<u<=s, s<y<=1} union the sliver; U_H = rest (all UV directions). Statement: every (H1)/(H2) item is <= C lambda^2 L^{<=2} at eps=0: (1-T_S)Gamma, C_C1, C_C2 on U_S (C_H: lambda^4); (1-T_C1)(1-T_S)Gamma, C_C2, C_H on U_C1; (1-T_C2)(1-T_S)Gamma, C_C1, C_H on U_C2; r on U_H. (H3^phi) as in Prop 3.1. Hence Thm 2.6 gives int|rho_r| <= C lambda^2 L^2. Grade [R, ca]. Evidence: 22 certificates, exact optima via rational duals, 0 failures (t4x, t4y); exact strictly negative recession slopes (<= -1/2) for all items (t4w); sliver separately (t4z). For eps in (0,eps0] the exponent loses at most 4 eps0 (LP at eps0=1/10 checked, t4). Family of covers s=lambda^theta, theta in (0,2]: int_{U_S} rho_CC1 >= s/4 (analytic; for kappa <= u m^2 one has rho~ >= 1/(4u m^2)), and numerically = s(1+o(1)). So the hypothesis exponent of a fat cover is theta (certified exactly: theta=1 -> lambda L; 3/2 -> lambda^{3/2}L; 19/10 -> lambda^{19/10}L; 2 -> lambda^2 L^2). Lesson, correcting App. D Lesson (d)/Def D.5: fat lambda^beta neighbourhoods (beta_S=1/9, beta_C=1/3) cost a power. The grouped forms (1-T_R0)X_R0 are small even where a single approximator fails (e.g. the measured (H1)_C1 norm is (theta/2)sL, with no lambda^2/s term). So covers at the natural scales give the sharp result.

### [results 8]
[X2-Thm3.5/Prop3.6] Triangle remainder: norm versus integral. Rigorous: int|rho_r| <= C lambda^2 L^2 [R, ca]. Numerical [P]: int|rho_r| = c(lambda) lambda^2 L with c = 3.53, 3.79, 3.89, 3.93, 3.95, 3.96, 3.962 for lambda^2 = 1e-2 ... 1e-8, i.e. -> 4 lambda^2 L. This is one log more than the signed remainder. Sign structure: soft box ~ -1.04L, C1 strip -0.54L, k+>P strip +0.95L, hard +0.48L (t2c). The monomial majorant is sharp to a factor 1.1-1.3 (t3). Exact remainder (KNOWN: REFDOC N12/synthesizer, reproduced): int r = -4m^2/Q^4 + (m^4/Q^6)(L_Q^2 - 15 + pi^2/3) + O(m^6 Q^-8 L^2), L_Q = ln(Q^2/m^2), Q^2 = (Qt^2+m^2)^2/Qt^2. The fibered integral matches UD to 1e-11 (t2b). Remark: Table 5 of the reference tests neither norm nor remainder (REFDOC ERR-m25).

### [results 9]
[X2-Thm3.9] Infinite class I: bubble chains / log insertions (NEW). Model (M1) with the gluon propagator replaced by the MS-bar-renormalized n-bubble chain at eps=0, i.e. Gamma^(j) = ln^j(Dg/mu^2)/(Dg D1 D2), j <= n, mu=Qt. Lemma 3.7 [R]: no T_R acts on the dressed gluon line; regions as for the triangle, bubble inside the gluon mode. So C_R Gamma^(j) = ln^j(Dg) C_R Gamma pointwise in 4D, while in the fiber the log is evaluated at the four line-1 shells D (exact), e (eikonal), t (massless), h (both). Shell virtualities (P=P'=1/sqrt2, v=1-u): R_D = (u m^2 v+kappa)/v, R_e = u m^2+kappa, R_t = kappa/v, R_h = kappa. rho_r^(j) = sum_s l_s^j T_s with T_D = (v/DG - 1/u)/(u m^2 v+kappa), T_e = m^2/(u(m^2+u)(u m^2+kappa)), T_t = 1/(u(uv+kappa)), T_h = 1/((m^2+u)(m^2+u+kappa)) - 1/(u(u+kappa)). Lemma 3.8 (rectangle rule, NEW, exact): l_D - l_e - l_t + l_h = delta = ln(A/B), |delta| <= u^2 m^2/(u m^2 v + kappa); a = l_e-l_h in [0, min(u m^2/kappa, CL)], b = l_t-l_h = ln(1/v) in [0, min(u/v, CL)]. Hence rho^(j) = sum_n C(j,n) l_h^{j-n}[a^n(T_D+T_e) + b^n(T_D+T_t) + ((a+b+delta)^n - a^n - b^n) T_D]. Theorem: on the natural cover of Thm 3.3, all (H1)/(H2) items are <= C_j lambda^2 L^{j+2} and int|rho_r^(j)| <= C_j lambda^2 L^{j+2}; (H3) as for the triangle. Grade [R, ca]. Evidence: 270 cells (0<u<1) + 60 cells (u>1), all at lambda^2, exact and strict (t15, t15b, t15d). Recession slopes <= -1/2 on 62 unbounded cells; the corner {v <= lambda^6, kappa <= lambda^8} is handled by separate shell bounds at lambda^8 (t15e, t15f). Items: t17y, exact and strict, min exponent 2. Naive groupings fail at lambda^{1-1.5}; the rectangle rule is essential. Numerics [P]: int r^(j) ~ -4 lambda^2 (-L)^j; norms 3.97 lambda^2 L (j=0), 4.84 lambda^2 L^2 (j=1), 6.58 lambda^2 L^3 (j=2) at lambda^2=1e-10 (t5).

### [results 10]
[X2-Prop3.12] All one-loop graphs of the DIS forward amplitude in phi^3_6 (NEW). Kinematics: unphysical region x >= x0 > 1, frame q^+=0, off-shell target p^2=-m^2. (i) Ladder (box), s and u channel: regions {A<H}; covered by Thm 5.1 with n=1. Rungs-on-shell representation L1 = (1/pi^2) int dxi d^4kT H0/((1-xi)v^2), v = xi m^2 + kT^2/(1-xi), H0 = 1/(Q^2(1-xi/x) + v + 2kT.qT); validated against the covariant Feynman-parameter value to 1e-13 (t6). (ii) Vertex corrections at the photon vertices and the hard-line self-energy: the collinear region is power-suppressed in phi^3_6 (only one spine propagator: d^4lT/v converges at m=0), so R={H} suffices. Then (H1)_H: int|(1-T_H)Gamma| <= C lambda^2 L, via |1/vbar - 1/vbar0| = m^2(1-z)/(vbar vbar0) and the 1D reduction; (H2) vacuous; (H3) trivial. Grade [R]. Numerics for the ladder [P]: full light-cone norm 1.228, 1.253, 1.260, 1.262, 1.263, 1.263 lambda (m^2 = 1e-2 ... 1e-7), first order with no log. Azimuth-averaged norm (0.34 + 0.125 L) m^2; signed (0.443 - 0.0437 L) m^2 (t6b).

### [results 11]
[X2-Thm3.13] Abelian massive-photon regulator, one loop, light-like approximators (NEW). Kinematics: p1=(P,0,0), p2=(0,-P',0), photon mass M, lambda^2 = M^2/Q^2, Q^2=2PP'. Per-line semilattice: T_S: (t1,t2) -> (h1,h2); T_C1: t2->h2; T_C2: t1->h1; T_H: G=M^2-k^2 -> g0=-k^2. Exactly: C_S = 1/(G h1 h2), C_C1 = (1/(G h2))(1/t1-1/h1), C_C2 = (1/(G h1))(1/t2-1/h2), C_H = (1/g0)(1/t1-1/h1)(1/t2-1/h2), r = (1/G-1/g0) delta1 delta2 = -M^2 g0/(G t1 h1 t2 h2). Fibered form (P=P'=1/sqrt2): rho_r = (M^2/u)[(1-u)/((M^2(1-u)+kappa)(u(1-u)+kappa)) - 1/((M^2+kappa)(u+kappa))] for 0<u<1, and -M^2/(u(M^2+kappa)(u+kappa)) for u>1. The kappa-integral of the first bracket vanishes identically, so the whole remainder integral sits at k+>P (outside supp Gamma). int r = -M^2 int_1^inf du ln(u/M^2)/(u(u-M^2)) = -lambda^2(L+1) - lambda^4(L/2+1/4) + O(lambda^6 L), exactly. Numerics: -5.6246, -7.9046, -10.2034, -12.5062, -14.8084 lambda^2 at lambda^2 = 1e-2..1e-6, versus -(L+1) = -5.605, ..., -14.816. Norm (2.83 -> 2.93) lambda^2 L, ~ 3 lambda^2 L - lambda^2 [P]. Exact Gamma reproduces Jantzen's formula (deviation 1.7e-4 = kappa-cutoff tail). Failure of (H3) [R]: rho_CS has constant density per unit ln k+ (rapidity divergence; the integral over |ln k+|<X grows exactly linearly), and rho_CC1 = -1/(2PP'(M^2+kappa)k+) for k+>P. So int dk+/k+ diverges for every eps: Thm D.10 is inapplicable although r is integrable and O(lambda^2 L). Lesson: (H3) is not needed for the remainder; it is needed only to split the sum into individually defined factors, which is exactly what factorization requires (t13).

### [results 12]
[X2-Prop3.14] Rapidity-regulated soft approximators: time-like versus space-like (NEW). Time-like: h1Y = 2P(k^- + e^{-2Y}k+), h2Y = 2P'(k+ + e^{-2Y}k^-). The eikonal pole -e^{-2Y}k+ (upper half plane) never meets the photon pole (M^2+kappa)/(2k+) (lower), so there is no pinch. The rapidity integral converges (545.458 at Y=3, 1090.909 at Y=6, linear in Y), and (H3) is restored for eps>0 (UV only). Remainder: for Y >= L/2 (e^{-2Y} <= lambda^2) it equals the light-like value within O(lambda^2), norm ~ 2.9 lambda^2 L. At Y = L/4 the regulator error ~ e^{-2Y} = lambda dominates (t16b; e.g. M^2=1e-3: int r = -7.75, -8.03, -7.92 lambda^2 at Y/L = 0.5, 1, 2, versus -(L+1) = -7.91). This is a sharp analogue of App. D's TMD window. Space-like (n_A spacelike, as in App. D Def D.21): h1Y = 2P(k^- - e^{-2Y}k+). The eikonal pole e^{-2Y}k+ + i0 and the photon pole (M^2+kappa)/(2k+) - i0 collide on 2e^{-2Y}(k+)^2 = M^2+kappa, a genuine pinch. rho_CS ~ 30.5/(k+/k0 - 1) near the surface (values +-3e3, 3e4, 3e5 at relative distances 1e-2, 1e-3, 1e-4), so it is not absolutely integrable. Grade [R] (pinch analysis), [P] (window numerics). This extends the reference erratum E1/ERR-M27 (spacelike self-energies) to single eikonal lines in virtual graphs.

### [results 13]
[X2-Thm4.1/Prop4.2] Two-loop planar Sudakov vertex: exact algebra. Lines: g1=k1, g2=k2, a1=p1-k2, a2=p1-k1-k2, b1=p2+k2, b2=p2+k1+k2. Regions: HH, HC1, HC2, C1C1, C2C2, HS, C1S, C2S, SS. Approximators are coordinate-zeroing sets on (k1+-,k1T,k2+-,k2T,M), with M = IR regulator (m^2, p1^-, p2^+). 'Soft-first' convention: a jet line carrying soft momentum enters H with its soft-approximated momentum, so soft momenta drop out of H entirely. Verified exactly [R]: the 12-edge Hasse diagram of App. D Fig. 63 (C1C1<HC1, C1S<C1C1, C1S<HS, C2C2<HC2, C2S<C2C2, C2S<HS, HC1<HH, HC2<HH, HS<HC1, HS<HC2, SS<C1S, SS<C2S); meet closure; (Com); (Abs) for all 9 incomparable pairs; the chain recursion C_R = T_R(Gamma - sum C_R') equals prod_R (1-T_R)Gamma (50 distinct zeroing patterns) (t8). Prop 4.2 (NEW correction of Lemma D.23(iii), 'always true for per-line meets'): with the naive convention (H sees pi_+ of the un-soft-approximated jet momentum, so k2^+ survives in H in region HS), (Abs) fails exactly for (C1C1,HS) and (C1C1,C2S) on line a2 [k2^+], and for (C2C2,HS) and (C2C2,C1S) on line b2 [k2^-]. The soft-first convention is necessary.

### [results 14]
[X2-Num-2loop] Two-loop planar vertex: double-residue (LCPT) densities and Collins remainder. Grade [P, numerical]; NEW. Engine lcpt.py with 6 factors and 2 minus components, order- and weight-independent. Supports: Gamma has k2+ in (-p2+,P) and K+ = k1+ + k2+ in (-p2+,P); approximated patterns extend to k+ -> infinity. Validation of int rho_Gamma against the exact Usyukina-Davydychev Phi^(2)(t,t)/Q^4 = -(6/lambda_K)[Li4(-1/(rho t)) - Li4(-rho t)]/Q^4: 82.41+-2.0 vs 82.28, 222.4+-1.1 vs 223.9, 513.8+-6.5 vs 508.1, 1016.8+-4.6 vs 1019.4 (P=P'=1/sqrt2, m^2 = 0.04, 0.01, 0.0025, 0.000625); 53.85+-0.66 vs 53.07 and 120.76+-1.4 vs 119.96 (P=0.8, P'=1.3) (t10, t12). This independently confirms both the LCPT representation and the L=2 UD formula at the ~1% level. Remainder (sum of 50 patterns), same m^2 values: full light-cone norm 20.2, 14.0, 9.57, 5.92, i.e. ~31 lambda L (first order, from angle-odd projection errors like 2 k1T.k2T when a collinear momentum enters a hard loop). Norm with the relative azimuth averaged in the fiber: 11.3, 7.0, 3.46, 1.88, second order (~ m^2 L^{2.6-3}). Signed int r: -6.9, -4.4, -2.6, -1.05, i.e. ~ -4.7 m^2 L^3 (t12, t14).

### [results 15]
[X2-Lem5.2] DIS ladders in phi^3_6: positive light-cone representation and exact Collins structure (NEW). Model and kinematics: n-rung forward ladder L_n = int prod_j d^6k_j/(i pi^3) H0(k_n) prod_j S(k_j)^2 R(k_{j-1}-k_j), k_0=p; q^+=0 frame, x>1. Statement: integrating k_n^-, ..., k_1^- top-down, all non-ordered plus-momentum configurations give zero (explicit pole-side induction), and on 0 < k_n^+ < ... < k_1^+ < p^+ only the rung poles contribute (rungs on shell). With c in {0,1}^{n+1} encoding projected rungs/hard factor: rho_c = prod_i [pi^{-2}(1-z_i)^{-1} (v_i^(c))^{-2}] H^(c_{n+1}), where v_i = z_i(1-c_i) v_{i-1} + |k_iT - (1-c_i) z_i k_{i-1,T}|^2/(1-z_i), v_0 = m^2, H^(0) = 1/(A + v_n + 2k_nT.qT), H^(1) = 1/A, A = 1 - xi_n/x. Invariant: every state has v >= xi m^2 + |K|^2/(1-xi) (convexity), hence H^(0) >= ... > 0. Approximators: T_{R_j}: k_j -> pi_+(k_j) in rung j+1 (or H0); T_H: p -> phat. They act on distinct factors, so (Com) holds and r = sum_c (-1)^{|c|} rho_c; (1-T_{R_j})X_{R_j} = [prod_{i<=j} kappa^(0)] U_j(s_j); C_{R_i} = [prod_{l<=i} kappa^(0)] kappa(pi s_i -> .) U_{i+1}(s'_{i+1,0}). The upper functionals U_j are defined recursively by U_{j-1}(s) = kappa(s->s')U_j(s') - kappa(pi s->s'_0)U_j(s'_0), U_n = h - hhat. Grade [R].

### [results 16]
[X2-Thm5.1] Infinite class II: DIS ladders of every length n (NEW). Setting as in Lem5.2, fibration = all minus components. Cover: N_{R_j} = {v_i <= lambda^2, w_i = |k_iT|^2/(1-z_i) <= lambda^2 for i<=j}, U_{R_j} = N_{R_j} minus N_{R_{j+1}}, U_{R_0} = complement of N_{R_1}. Statement: (H1)-(H3) hold for all n with every item <= C_n lambda (1+L)^n, and int|rho_r| <= C_n lambda(1+L)^n at eps=0. (H3): Gamma positive and UV-finite in d=6 (all subgraphs have degree -2); each C_{R_j} is in L^1 for eps>0 only (UV of the lower chain's last loop). Proof: induction on the norms N_j(s) = ||U_j(s;.)||_{L^1(upper)}, using (P1) N_j(s) <= C min(1,sqrt v) l(v)^{n-j} and (P2) ||U_j(s)-U_j(s~)||_1 <= C|v-v~| min(v,v~)^{-1/2} min(1,min^{-1/2}) l^{n-j-1} for equal (xi,K), with l(v) = 1 + ln+(1/v). Step: split the child momentum into (A) |k|^2 >= 64 v, where |v'-v'_0| <= 3z|k|sqrt v/(1-z), the kernel difference is <= 19 kappa_0 sqrt(v)/|k|, and the projected parts cancel in (P2) because pi s = pi s~; and (B) |k|^2 < 64 v, terms bounded separately. All integrals reduce to the 1D integrals of Lem 2.12. Hard-factor lemma (Lem 5.3): the S^3-average of 1/(A+v'+2k.q) over the child direction is <= 2/max(1-z, z xi(1-1/x)), integrable against (1-z) dz (numerical check t19: ratio <= 0.5). (H1)/(H2) then follow from (P1) with each lower level confined to the band [xi m^2, lambda^2]. Grade [R], complete proof outlined at the level of these explicit estimates. Numerics [P]: n=2 full norm 2.63, 3.26, 3.90, 4.54, 5.19 lambda (m^2 = 1e-2..1e-6), ~(1.3 + 0.27L) lambda; q-averaged 0.83-0.88 lambda (rung cross terms keep first order); both azimuths averaged 0.93, 1.51, 2.22, 3.06, 4.07 m^2 (second order); signed -0.65..-2.71 m^2 (t11). Conjecture: the angle-averaged norm is O(lambda^2 L^{b_n}) for all n.

### [results 17]
[X2-Prop5.4] Two-element chains ('single collinear subgraph'). Setting: Gamma = H(k) J(k,p), regions {A<H}, T_A acting only on H (H(k) -> H(pi_+ k)) and T_H only on J (J -> Jt). Identities: C_A = H(pi k) J, C_H = DeltaH Jt, r = DeltaH DeltaJ. (H1)_A <=> int_{U_A} |DeltaH J| small; (H2)_A <=> int_{U_A} |DeltaH Jt| small; (H1)_H <=> int_{U_H} |DeltaH DeltaJ| small; (H3) <=> integrability of HJ (uniform), H(pi k) J and DeltaH Jt (eps>0). Grade [R] (algebra); this is the n=1 case of Thm 5.1 and covers every one-loop DIS graph with a collinear region. Known structure (App. D Ex. D.48 for n=2), made precise.

### [results 18]
[X2-Thm6.1] Sudakov form factor to all orders: precise conditional theorem. Model (M1) at fixed order N; integrand-level renormalization only for self-energy subgraphs (Ass. D.41 (U1)(U2)); regions = meet closure of leading regions; soft-first approximators. Hypothesis (F1): a cover with (H1^phi),(H2^phi) at exponent a>0. Conclusion: sum_Gamma sum_R int C_R Gamma = F^(N) + O(lambda^a L^K), each term absolutely convergent for eps>0; UV poles cancel in the sum (Prop D.16 under (A1)(b)). Gauge theories need additionally D.37 (Ward product structure) and the P_A/K-gluon approximators (where (Abs) may fail by transverse couplings). Grade [R, R_cond]. Status of hypotheses. VERIFIED: (H3^phi) for Gamma at all orders for UV-finite graphs (Cor 2.11); admissibility of all Collins terms (affine-in-minus structure, decay per graph); (F1) at N=1 (all graphs, sharp exponent lambda^2 L^2); (F1) for the bubble-chain class at all N (lambda^2 L^{j+2}); (Com),(Abs), product formula for the N=2 planar ladder (exact; analytic remainder bounds only numerical [P]). NOT VERIFIED (open, [A] content of Collins' power counting): (F1) for crossed ladders and general N>=2 topologies; graphs with quark self-energy or vertex subgraphs (UV subdivergences; ERR-M28 BPHZ vs MS-bar); gauge numerators; Ward identities on approximated integrands.

### [results 19]
[X2-Err] Corrections and sharpenings to App. D found here (NEW; all verified). (a) Lemma D.23(iii): (Abs) is not automatic for per-line meets; it requires the soft-first convention (4 explicit failures in the two-loop planar vertex otherwise). (b) Def D.5/Lesson (d): fat lambda^beta neighbourhoods are not needed. At the natural scales the grouped Collins objects satisfy (H1),(H2) with the sharp exponent (triangle: lambda^2 L^2 instead of the lambda^{beta/3}-type exponents of Lemma D.25). (c) Def D.9 (H3) on the real contour fails already for Gamma; the fibered version is the meaningful one, and it removes (A1). (d) In fibered form, non-maximal U_R must be UV-bounded: individual subtraction terms have eps-non-uniform UV logarithms. (e) Def D.21's space-like rapidity vectors pinch the virtual soft subtraction term (Prop 3.14); time-like vectors do not. (f) Ex. D.47: the integral norm of the remainder is ~4 lambda^2 L, one log more than |int r|; the sliver -m^2/2P' < k+ < 0 carries zeta_2/Qt^2 of the integral and -2m^2/Qt^4 of the remainder (absent from the reference). (g) (H3) is not necessary for the remainder bound (massive photon), but it is necessary for factorization into separately defined factors.

### [results 20]
[X2-Err-own] Retraction of an intermediate claim of this run (for the record). I first expected that the 2x2-cover exponent 1 was optimal, i.e. that the theorem 'necessarily loses one power'. The exact theta-scan (t4y) and the lower-bound computation (t18: int_{U_S} C_C1 = s(1+o(1)), (H1)_C1 norm = (theta/2) s L) show the opposite: theta=2 (natural scale) is optimal and gives the sharp lambda^2 L^2. Only the version in X2-Thm3.3 is correct.

### [results 21]
[X2-Est] Error estimates with explicit powers (eps=0; for eps in (0,eps0] the exponents decrease by at most 4 eps0 at one loop). Triangle (M1): items <= C lambda^2 L^2 (natural cover); fat cover s=lambda^theta gives Theta(lambda^theta L); remainder norm <= C lambda^2 L^2 rigorous, ~4 lambda^2 L numerical; signed -4m^2/Q^4 + (m^4/Q^6)(L^2 - 15 + pi^2/3). Bubble class: items and remainder <= C_j lambda^2 L^{j+2}; numerical norm ~ c_j lambda^2 L^{j+1}, signed ~ -4 lambda^2 (-L)^j. DIS ladders (M2): items and full-norm remainder <= C_n lambda (1+L)^n; numerical full norm 1.263 lambda (n=1), (1.3+0.27L) lambda (n=2); angle-averaged second order. DIS one-loop H-only graphs: <= C lambda^2 L. Massive photon light-like: int r = -lambda^2(L+1) - lambda^4(L/2+1/4) + O(lambda^6 L) exact, norm ~ 3 lambda^2 L - lambda^2; time-like regulated: equals light-like for Y >= L/2, error ~ e^{-2Y} otherwise. Two-loop planar vertex: full norm ~31 lambda L, angle-averaged ~ m^2 L^{2.6-3}, signed ~ -4.7 m^2 L^3 [P].

## open

### [open 1]
O1 (central, = App. D Ass. D.14 in fibered form). (H1^phi)/(H2^phi) for general graphs. Here the only inductive mechanism found is the chain structure plus the exact 1D rung-kernel reduction (Lem 2.12), which covers ladders. Graphs with overlapping regions, several jets plus soft subgraphs, or non-planar topologies have no proof. The LP method needs explicit densities, i.e. finite sets of graphs.

### [open 2]
O2. Gauge theories: no one-loop QCD vertex or box with Dirac numerators and the P_A = g_T + n x nbar / K-gluon projections has been certified. Open in particular: instantaneous terms in LCPT for numerators with k^-; (Abs) failure for transverse polarizations of direction-flipping lines (Lemma D.23(iii)); Ward identities on approximated integrands (D.37 W1/W2).

### [open 3]
O3. Two loops beyond the planar ladder and the bubble insertion: crossed ladder (regions plausibly only {all-collinear, H} in phi^3_6, unproven); quark self-energy and vertex subgraphs (UV subdivergences need integrand-level renormalization (U1)/(U2), and BPHZ vs MS-bar breaks Ward identities, ERR-M28); the closed-loop current graph of (M1).

### [open 4]
O4. Two-loop planar vertex: a rigorous (H1)-(H3) proof. The 5D densities contain non-monomial Gram factors such as |k1T+k2T|^2, so Lemma 2.8 must be extended to Gram-positive factors or to angle-averaged fibrations. Present evidence is numerical only.

### [open 5]
O5. Sharp second-order norms with angle-averaged fibrations: for DIS ladders of all n (conjecture O(lambda^2 L^{b_n}), supported by n=1,2), and for the two-loop vertex (numerically ~ m^2 L^{2.6-3}).

### [open 6]
O6. Uniformity in eps for multi-loop transverse integrals in d=4-2eps (Gram-determinant weights). This is handled explicitly only at one loop (exponent loss <= 4 eps0) and remarked on for ladders.

### [open 7]
O7. Physical (cut) processes: the cut-sum representation (Ass. D.27) is untouched. Light-cone positivity (Lem 2.10) holds only in spacelike/unphysical kinematics. Physical DIS, e+e-, DY and TMD need the cut-summed integrand and its own certificates.

### [open 8]
O8. Rapidity regulators: TMD-type subtraction with proven (H1)-(H3). Time-like regulator vectors work at one loop (window Y >= L/2). For space-like vectors (App. D Def D.21) one must either prove that the pinch contributions cancel in the sum over regions, or replace them by time-like vectors.

### [open 9]
O9. Massive-photon (abelian) class beyond one loop: ladders and bubbles with a massive photon combined with Collins subtraction with time-like regulators, and abelian exponentiation, are not addressed.

### [open 10]
O10. The all-order Sudakov theorem (Thm 6.1) still rests on O1. Exponentiation and the product structure (D.37) and multiplicative renormalization (D.43) are not addressed here.

## files

### [files 1]
/Users/hao-cheng/Desktop/theorem proof/qcd_factorization_work/verify/extend/X2-subtraction/scripts/lcpt.py

### [files 2]
/Users/hao-cheng/Desktop/theorem proof/qcd_factorization_work/verify/extend/X2-subtraction/scripts/tropical.py

### [files 3]
/Users/hao-cheng/Desktop/theorem proof/qcd_factorization_work/verify/extend/X2-subtraction/scripts/exact_verify.py

### [files 4]
/Users/hao-cheng/Desktop/theorem proof/qcd_factorization_work/verify/extend/X2-subtraction/scripts/recession.py

### [files 5]
/Users/hao-cheng/Desktop/theorem proof/qcd_factorization_work/verify/extend/X2-subtraction/scripts/t1_triangle_densities.py

### [files 6]
/Users/hao-cheng/Desktop/theorem proof/qcd_factorization_work/verify/extend/X2-subtraction/scripts/t2b_norm_fast.py

### [files 7]
/Users/hao-cheng/Desktop/theorem proof/qcd_factorization_work/verify/extend/X2-subtraction/scripts/t2c_pieces.py

### [files 8]
/Users/hao-cheng/Desktop/theorem proof/qcd_factorization_work/verify/extend/X2-subtraction/scripts/t3_tropical_triangle.py

### [files 9]
/Users/hao-cheng/Desktop/theorem proof/qcd_factorization_work/verify/extend/X2-subtraction/scripts/t4_triangle_certificates.py

### [files 10]
/Users/hao-cheng/Desktop/theorem proof/qcd_factorization_work/verify/extend/X2-subtraction/scripts/t4x_triangle_exact.py

### [files 11]
/Users/hao-cheng/Desktop/theorem proof/qcd_factorization_work/verify/extend/X2-subtraction/scripts/t4y_theta_scan.py

### [files 12]
/Users/hao-cheng/Desktop/theorem proof/qcd_factorization_work/verify/extend/X2-subtraction/scripts/t4z_sliver_exact.py

### [files 13]
/Users/hao-cheng/Desktop/theorem proof/qcd_factorization_work/verify/extend/X2-subtraction/scripts/t4w_recession_theta2.py

### [files 14]
/Users/hao-cheng/Desktop/theorem proof/qcd_factorization_work/verify/extend/X2-subtraction/scripts/t5_bubble_numerics.py

### [files 15]
/Users/hao-cheng/Desktop/theorem proof/qcd_factorization_work/verify/extend/X2-subtraction/scripts/t15_bubble_certificate.py

### [files 16]
/Users/hao-cheng/Desktop/theorem proof/qcd_factorization_work/verify/extend/X2-subtraction/scripts/t15b_bubble_bigu_and_exact.py

### [files 17]
/Users/hao-cheng/Desktop/theorem proof/qcd_factorization_work/verify/extend/X2-subtraction/scripts/t15d_strict_select.py

### [files 18]
/Users/hao-cheng/Desktop/theorem proof/qcd_factorization_work/verify/extend/X2-subtraction/scripts/t15e_recession_check.py

### [files 19]
/Users/hao-cheng/Desktop/theorem proof/qcd_factorization_work/verify/extend/X2-subtraction/scripts/t15f_corner.py

### [files 20]
/Users/hao-cheng/Desktop/theorem proof/qcd_factorization_work/verify/extend/X2-subtraction/scripts/t17_bubble_H1H2.py

### [files 21]
/Users/hao-cheng/Desktop/theorem proof/qcd_factorization_work/verify/extend/X2-subtraction/scripts/t17y_bubble_H1H2_strict.py

### [files 22]
/Users/hao-cheng/Desktop/theorem proof/qcd_factorization_work/verify/extend/X2-subtraction/scripts/t6_dis_ladder1.py

### [files 23]
/Users/hao-cheng/Desktop/theorem proof/qcd_factorization_work/verify/extend/X2-subtraction/scripts/t6b_dis_ladder1_norms.py

### [files 24]
/Users/hao-cheng/Desktop/theorem proof/qcd_factorization_work/verify/extend/X2-subtraction/scripts/t11_dis_ladder2.py

### [files 25]
/Users/hao-cheng/Desktop/theorem proof/qcd_factorization_work/verify/extend/X2-subtraction/scripts/t19_hardfactor_check.py

### [files 26]
/Users/hao-cheng/Desktop/theorem proof/qcd_factorization_work/verify/extend/X2-subtraction/scripts/t13_massive_photon.py

### [files 27]
/Users/hao-cheng/Desktop/theorem proof/qcd_factorization_work/verify/extend/X2-subtraction/scripts/t16_massive_regulated.py

### [files 28]
/Users/hao-cheng/Desktop/theorem proof/qcd_factorization_work/verify/extend/X2-subtraction/scripts/t16b_regulated_grid.py

### [files 29]
/Users/hao-cheng/Desktop/theorem proof/qcd_factorization_work/verify/extend/X2-subtraction/scripts/t8_twoloop_algebra.py

### [files 30]
/Users/hao-cheng/Desktop/theorem proof/qcd_factorization_work/verify/extend/X2-subtraction/scripts/twoloop_dens.py

### [files 31]
/Users/hao-cheng/Desktop/theorem proof/qcd_factorization_work/verify/extend/X2-subtraction/scripts/twoloop_patterns.json

### [files 32]
/Users/hao-cheng/Desktop/theorem proof/qcd_factorization_work/verify/extend/X2-subtraction/scripts/t9_twoloop_checks.py

### [files 33]
/Users/hao-cheng/Desktop/theorem proof/qcd_factorization_work/verify/extend/X2-subtraction/scripts/t10_twoloop_integral.py

### [files 34]
/Users/hao-cheng/Desktop/theorem proof/qcd_factorization_work/verify/extend/X2-subtraction/scripts/t12_twoloop_remainder.py

### [files 35]
/Users/hao-cheng/Desktop/theorem proof/qcd_factorization_work/verify/extend/X2-subtraction/scripts/t14_twoloop_anglefiber.py

### [files 36]
/Users/hao-cheng/Desktop/theorem proof/qcd_factorization_work/verify/extend/X2-subtraction/scripts/t18_cover_optimality.py

### [files 37]
/Users/hao-cheng/Desktop/theorem proof/qcd_factorization_work/verify/extend/X2-subtraction/logs/
