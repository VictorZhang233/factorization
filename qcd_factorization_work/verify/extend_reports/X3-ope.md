# X3-ope

(extracted verbatim from the workflow journal; structured output of the agent)

## summary

Yes, the workflow step ran normally. This X3-ope agent finished its task, but the harness blocked writing `verify/extend/X3-ope/REPORT.md` (subagents may not write report `.md` files). The full report is given below so the parent can save it. All checks pass.

# X3: OPE in massless QCD, and DIS / e⁺e⁻ moments at hadron level

Conventions follow `CONTEXT.md`: metric (+,−,−,−), $D=4-2\varepsilon$, $\overline{\rm MS}$, $Q^2=-q^2$, $\nu=P\cdot q$, $\omega=2\nu/Q^2=1/x$, $a=\alpha_s/\pi$.

| Grade | Meaning |
|---|---|
| [R] | Complete proof here, or a rigorous theorem whose scope I checked. |
| [R-cited] | Rigorous in the cited source, but I read only the abstract and the author's own later summary. |
| [R-cond: X] | Rigorous given the numbered assumptions X. |
| [A] | All-order argument standard in the literature, but parts exist only as sketches. |
| [C] | Open. |

**Scripts and logs** (all checks pass):
- `scripts/f1_forward_graphs.py`: graph polynomials and Newton polytopes.
- `scripts/f2_triangle.py`: exact one-loop forward triangle.
- `scripts/h1_hadronic_checks.py`: the hadronic lemmas.
- `scripts/e1_ee_checks.py`: e⁺e⁻ / Adler-function checks.
- `research/c_dis` logs `ope_check_N6`, `ope_check_N8`: one-loop DIS check, exact in ε.

## 0. Executive summary

### (i) The strongest OPE statement for massless QCD with quarks

The strongest statement is **Theorem I = Theorem A + Theorem B**, at every order of DR+$\overline{\rm MS}$ perturbation theory (Feynman gauge).
- **Expansion.** The T-product of two EM currents, in Green functions of elementary fields at Euclidean non-exceptional momenta, has a large-$q$ expansion in $\overline{\rm MS}$ local operators. The remainder is $O(|q|^{1-a}\ln^k|q|)$.
- **Coefficients.** They are unique, equal to $|q|^{2-d_O}$ times a polynomial in $\ln(q^2/\mu^2)$, given by $C^{\rm bare}Z^{-1}$, and obey the RG equation.
- **Gauge structure.** The dimension-$d$ part $X_d$ is GI + BRST-exact + EOM.
- **Physical matrix elements.** The twist-2 part involves only $O_q^{(n)}$ and $O_g^{(n)}$.

How it is assembled:
- **Theorem A** rests on the graph-by-graph large-momentum expansion of dimensionally regularized and $\overline{\rm MS}$-renormalized amplitudes and its operator form: Smirnov CMP 134 (1990) 109, Gorishny NPB 319 (1989) 633, Llewellyn Smith–de Vries NPB 296 (1988) 991. This is [R-cited]: I verified the abstracts and Smirnov's own review (hep-th/9412063), not the full texts.
- **The missing step for QCD with quarks** is the BRST/GI reduction of the OPE coefficients. Before this report it existed only at physicist's level (Joglekar 1977) or for pure Yang–Mills in other frameworks (Hollands 2008; Fröb–Holland 2016, a preprint).
- **Theorem B closes that step.** It uses the exact BRST invariance of DR for vector-like QCD, plus one observation: the merged contact terms produced by the composite BRST variations $s\phi$ are always Green functions of EOM operators. It needs no assumption (B1) and no polynomiality of contact terms.
- **What Theorem B still relies on:** the DR expansion with one composite spectator ($E_\varepsilon$, within the scope of K2), the exact DR Ward and Schwinger–Dyson identities, and local BRST cohomology.
- **Flow-equation route (FHH/FH).** It would also give the result. The cohomological condition $H^{1,4}_{E(4)}(\hat s|d)=0$ holds for vector-like QCD by parity. What is missing there is the FHH-type existence-with-bounds theorem for Yang–Mills with Dirac fermions.

### (ii) Euclidean versus forward kinematics

**Partonic.** Moments need forward, on-shell matrix elements. These are exceptional kinematics, and the Euclidean remainder is not uniform there (Example F.4: matrix elements diverge like $\ln p^2$).
- The estimate needed is the reference's forward remainder, Prop. C.54(a).
- **This is proven in DR to all orders** (Theorem F and Corollary F.2).
- The key fact is about the forward Symanzik polynomial: $F=Q^2(\hat F_0+\omega\hat F_1)$, where every monomial of $\hat F_1$ is a monomial of $\hat F_0$ with coefficient of modulus no larger.
- By Newton-polytope (Euler–Mellin) theory, each Laurent coefficient is holomorphic in the cut $\omega$-plane, and its Taylor series equals the naive Taylor expansion in $p$ (no other regions).
- Hence $T_2^{(j)}=4\sum_{n\ \rm even}\omega^{n-1}\sum_iC^{(n)}_{2,i}A^{(n)}_{i/j}$ at every order, with the Euclidean $\overline{\rm MS}$ coefficients.

**Hadronic.** There is no exceptional-momentum problem, because $M>0$. What is needed is exactly the non-perturbative OPE on the Euclidean segment $|\omega|\le\sqrt3M/Q$ (assumption N1, "SA"). It cannot be derived with present mathematics.

### (iii) Hadron-level DIS moment theorem (Theorem M)

Assumptions:
- **W1–W3:** Wightman framework, with a corrected spectral condition, plus a covariant conserved retarded part of the forward matrix element.
- **N1:** the segment approximation, the minimal form of the non-perturbative OPE.
- **N2:** RG plus asymptotic freedom of the twist-2 coefficients; needed only to compare with perturbation theory.
- **G:** a growth condition; needed only for $n<n_0$.
- **N3, Φ:** optional.

Conclusions:
- Every even Taylor coefficient obeys $t_n=4\sum_iC^{(n)}_{2,i}A^{(n)}_i+O\big((M^2+mM)Q^{-2}\ln^kQ\big)$.
- The moment identity $t_n=4\int x^{n-2}F_2$ holds for even $n\ge n_0$, with $n_0$ = the smallest even integer $>A+1$. $A$ is a $Q$-independent Wightman temperedness exponent.
- G is necessary and sufficient for the moments with $2\le n<n_0$, including the momentum sum rule.

### (iv) e⁺e⁻ and the Adler function (E1–E6)

- **E1 [R]:** Källén–Lehmann; one subtraction suffices iff $D<\infty$ at one point.
- **E2 [R-cond]:** $D$ equals its PT series up to $O(m^2/Q^2,\Lambda^4/Q^4)$, with no $1/Q^2$ term.
- **E3 [R-cond]:** Euclidean moments $M_k=R_0[1+d_1a+(d_2+H_{k-1}b_0d_1)a^2+O(a^3)]$.
- **E4 [R]:** exact counterexample. $R=R_0[1+\kappa\sin(\sqrt s/\Lambda)]$ gives $D=R_0[1+\kappa\frac\pi2\frac Q\Lambda e^{-Q/\Lambda}]$. So the Euclidean OPE plus positivity cannot fix $R(s)$ pointwise, nor $R$ smeared over a fixed width.
- **E5 [R-cond]:** Karamata Tauberian theorem: $\frac1s\int_0^sR\to R_0$ follows from $D\to R_0$ and $R\ge0$.
- **E6 [R-cond]:** PQW smearing with width $\Delta\propto s$ follows from an OPE on a sector. Fixed width needs local duality.

## 1. Setup

- **D1.** SU($N_c$) gauge group, $n_f$ massless Dirac quarks. Gauge fixing $s(\bar c(\partial A+\xi B/2))$. BRST: $sA=Dc$, $s\psi=igc\psi$, $sc=-\frac g2[c,c]$, $s\bar c=B$, $sB=0$, $s^2=0$. Dimensions $[A]=[c]=[\bar c]=1$, $[\psi]=3/2$, $[B]=2$.
- **D2.** DR (plus analytic regulators where stated) with $\overline{\rm MS}$; $[O]=Z_{OO'}O'_{\rm bare}$. There is no $\gamma_5$ (vector-like theory, EM current, unpolarized operators), so DR is exactly BRST-invariant.
- **D3.** Operator classes:
  - GI: colour-singlet polynomials in $F$, $\psi$, $\bar\psi$ and $D$;
  - BRST-exact: $s\Lambda$;
  - EOM: the ideal $\mathcal E$ generated by $\delta S/\delta\phi$ and its derivatives;
  - aliens = BRST-exact + EOM.
- **D4.** $\mathcal J^{\mu\nu}(q)=i\int d^Dx\,e^{iqx}TJ^\mu(x)J^\nu(0)$ and $D\equiv d_J+d_J-4=2$. $\tilde G^T_{JJ;\Phi}$ denotes Green functions of $\mathcal J$ with a string $\Phi$ of elementary fields; $\tilde G_{[O];\Phi}$ has the operator $O$ at momentum $-\sum p$.
- **D5.** Non-exceptional means no proper partial sum of $(p_1..p_n,-\sum p)$ vanishes. Forward matrix elements are exceptional.
- **D6.** $T^{\mu\nu}=i\int e^{iqz}\langle P|TJ^\mu J^\nu|P\rangle_c=-\tilde g^{\mu\nu}T_1+\hat P\hat P\,T_2/\nu$ and $W^{\mu\nu}=\frac1{4\pi}\int e^{iqz}\langle P|[J,J]|P\rangle_c=-\tilde gF_1+\hat P\hat PF_2/\nu$. $T_2=\sum_{n\ \rm even}t_n\omega^{n-1}$ and $M^{(n)}_2=\int_0^1x^{n-2}F_2$, including the elastic point. Free quark: $T_2=4e_q^2\omega/(1-\omega^2)$, ${\rm Disc}\,T_2=4\pi iF_2$.
- **D7.** $O_q^{(n)}=\mathcal S\bar\psi\gamma iD\cdots iD\psi-$tr and $O_g^{(n)}=\mathcal S F\,iD\cdots iD\,F-$tr. $\langle P|O_i|P\rangle=2A_i(PP\cdots-{\rm tr})$, and $t_n=4\sum C^{(n)}_{2,i}A^{(n)}_i+\dots$
- **D8.** Euclidean segment: $\mathcal I_Q=\{iy:|y|\le r_Q=\sqrt3M/Q\}$.
- **D9.** Naive Taylor expansion: rescale $p\to\lambda p$, so $\omega\to\lambda\omega$, and expand the integrand in $\lambda$.
- **D10.** Lee–Pomeransky representation:
  $$I=\frac{\Gamma(D/2)}{\Gamma((L+1)D/2-|a|)\prod_l\Gamma(a_l)}\int_{\mathbb R^N_+}\alpha^{a-1}\,\mathcal G^{-D/2},\qquad \mathcal G=\mathcal U+\mathcal F.$$
  Tensor integrals are sums of scalar integrals with raised powers in shifted dimensions, times polynomial tensors (Tarasov 1996).

**Assumption register.**
- **Inputs to Part I:**
  - E_ε: the DR expansion with at most one composite spectator.
  - DR-WI: exact BRST Ward identities.
  - DR-SD: Schwinger–Dyson identities; δ(0)=0 in DR.
  - LBC: local BRST cohomology.
  - K3: Joglekar–Lee.
- **Hadronic DIS:** W1–W3, N1, N1-std, N2, N3, G, Φ (§5).
- **e⁺e⁻:** V1–V3 and V2′ (§6).

## 2. Literature (what I verified)

**K1. IR finiteness.**
- Lowenstein–Zimmermann CMP 44 (1975) 73 (IR power counting); Lowenstein CMP 47 (1976) 53 (BPHZL convergence).
- Breitenlohner–Maison CMP 52 (1977) 11, 39, 55: DR Green functions of massless theories with all interaction terms of IR degree Ω≥4 exist to all orders, and the action principle holds. QCD in Feynman gauge has only Ω=4 vertices.
- Poggio–Quinn PRD 14 (1976) 578: IR finiteness at non-exceptional momenta.
- Checked: abstracts.

**K2. The DR / $\overline{\rm MS}$ OPE.**
- (a) Smirnov CMP 134 (1990) 109, abstract: "Asymptotic expansions of renormalized Feynman amplitudes in limits of large momenta and/or masses are proved … operator expansions … for … time-ordered products are presented". Book: Birkhäuser 1991.
  - Hypotheses, from his review hep-th/9412063 (read in full) and hep-ph/9708423: off-shell, non-exceptional momenta; large momenta Euclidean or spacelike.
  - The bare formula $F_\Gamma\sim\sum_\gamma F_{\Gamma/\gamma}\circ\mathcal TF_\gamma$ is "justified in [Smirnov 1990]".
  - The renormalized form is "proved in [1990; Chetyrkin MPI preprint 1991]"; the $R^*$-finite form is proved in the Chetyrkin preprint.
  - Full text not accessible (bot protection). [R-cited]
- (b) Gorishny 1989, abstract: a method for expanding $\overline{\rm MS}$ Green functions in large Euclidean momenta in terms of $\overline{\rm MS}$ operators; the coefficients are IR-finite.
- (c) Llewellyn Smith–de Vries 1988: "OPE is proved for minimally subtracted operators".
- (d) Chetyrkin TMF 75, 76 (1988); Gorishny–Larin–Tkachov PLB 124 (1983) 217 (method of projectors).
- All of these are graph-by-graph or combinatorial; gauge symmetry plays no role in them.

**K3. Renormalization of GI operators.**
- Kluberg-Stern–Zuber PRD 12 (1975) 467, 482.
- Joglekar–Lee Ann. Phys. 97 (1976) 160 (abstract checked): BRST-exact basis, closure under renormalization, decoupling.
- Henneaux PLB 313 (1993) 35.
- Collins–Scalise PRD 50 (1994) 4117 (§1–2 read): the Hamberg–van Neerven problem arises from off-shell gluon states taken on shell at zero momentum transfer.

**K4.** Joglekar Ann. Phys. 108 (1977) 233 and 109 (1977) 210 (abstracts): non-abelian theories with fermions. In the OPE of GI currents, the physical matrix elements of gauge-variant operators "vanish or cannot be isolated". Physicist's level.

**K5. Pure Yang–Mills.**
- Hollands RMP 20 (2008) 1033 (abstract): "OPE closes on the space of gauge invariant operators".
- FHH JMP 57 (2016) 122301: rigorous bounds and Ward identities.
- Fröb–Holland arXiv:1603.08012 (read §1.1, §8):
  - Thm 1: the OPE exists for "arbitrary massless superficially renormalisable theory".
  - Thm 2: a BRST Ward identity for the OPE coefficients, if $H^{1,4}_{E(4)}(\hat s|d)=0$.
  - §8: extension to other gauge theories needs FHH-type Ward identities.

**K6.** Barnich–Brandt–Henneaux Phys. Rep. 338 (2000) 439 and NPB 455 (1995) 357.
- For semisimple groups the anomaly candidates are only the parity-odd, matter-independent forms.
- At ghost number 0, $H(s)$ modulo EOM consists of the GI polynomials (cohomology on local functions).

**K7.** Hollands–Kopper CMP 313 (2012) 257 and Holland–Hollands–Kopper CMP 342 (2016) 385: OPE convergence in φ⁴₄.

**K8. Euler–Mellin integrals** (Schultka arXiv:1806.01086 §3, read). Nilsson–Passare J. Geom. Anal. 23 (2013) 24; Berkesch–Forsgård–Passare Michigan Math. J. 63 (2014) 101; Kaneko–Ueda CPC 181 (2010) 1352.
- **Thm 3.1.** Let the coefficients lie in an open strongly convex cone, and let $P=\sum{\rm Newt}(f_i)$ be full-dimensional. Then the Mellin transform converges absolutely iff ${\rm Re}\langle s,u_\rho\rangle>{\rm Re}\,d_\rho(c)$ for every ray $\rho$ of the normal fan. This set is nonempty. If $P$ is not full-dimensional, it converges nowhere.
- **Thm 3.6 (= BFP 2.4).** Meromorphic continuation of the form $\Phi\prod_\rho\Gamma(\cdot)$ with $\Phi$ entire.
- **Cor 3.8 (Kaneko–Ueda).** A decomposition into cubes $[0,1]^N$ on which each polynomial is a monomial times a nonvanishing polynomial.

**K9. Tools.**
- Vladimirov (1979) §25–26 and Reed–Simon II Thm IX.16: tube holomorphy with $|\tilde f|\le C(1+|\zeta|)^a(1+\Delta^{-b})$.
- Hörmander ALPDO I §3.1: boundary values.
- Karamata: Feller II, XIII.5; Korevaar 2004.
- Markov coefficient inequality: Borwein–Erdélyi.

**K10.** `c_ee` Thm 5.1: $R^{(n)}$ is IR finite and equals $12\pi\,{\rm Im}\,\Pi^{(n)}(s+i0)$. Euclidean steps [R], cut identification [A].

**K11.** `c_pdf` §5: moments of the PDFs are local-operator matrix elements. §7: even moments determine $q+\bar q$ and $g$; Prop 7.7 covers continuation in $N$.

## 3. Part I: Euclidean perturbative OPE

**Lemma A.3 (linear independence).** Let $\{O\}$ be finitely many linearly independent monomials. Suppose
$$\sum_Oc_O(q)\,\tilde G_{[O];\Phi}(p)=O(|q|^\varrho\ln^k)$$
for all strings Φ and all $p$ in an open non-exceptional set, at each order. Then $c_O=O(|q|^\varrho\ln^k)$. If moreover $c_O$ is graded homogeneous with degrees $>\varrho$, then $c_O\equiv0$.

*Proof.* Expand $c_O=\sum_jg^{2j}c^{(j)}_O$.
- At order $g^0$, only $O$ whose fields match Φ contribute, through the tree vertex polynomial $V_O(p)$. The map from monomials to symmetrized polynomials is injective, so evaluating at finitely many $p$ gives $c^{(0)}=O(|q|^\varrho)$.
- At order $g^{2j}$ the terms $c^{(i)}G^{(l)}$ with $i<j$ are $O(|q|^\varrho)$ by induction, since $G^{(l)}$ does not depend on $q$. The same argument then applies to $c^{(j)}$.
- For graded-homogeneous $c$, separate the powers of $|q|$. ∎

**Theorem A (Euclidean OPE for $J^\mu J^\nu$, full basis).** Hypotheses: D1–D2 in Feynman gauge, fixed order $r$, integer $a\ge2$.
- (A1) $\tilde G^T_{JJ;\Phi}-\sum_{d_O\le a}C_O(q;\mu)\tilde G_{[O];\Phi}=O(|q|^{1-a}\ln^k|q|)$, uniformly in direction and on compact non-exceptional sets of $p$.
- (A2) $C_O=|q|^{2-d_O}\times$ a polynomial of degree $\le r$ in $\ln(q^2/\mu^2)$ (tensor in $\hat q$ and $g$).
- (A3) $C^{\overline{\rm MS}}=C^{\rm bare}Z^{-1}$. Here $C^{\rm bare}_O$ is the sum over hard subgraphs (containing both current vertices, 1PI after identifying them) of the DR Taylor coefficients in all small momenta.
- (A4) Uniqueness.
- (A5) $(\mu\partial_\mu+\beta\partial_\alpha)C_i=\sum_jC_j\gamma_{ji}$.

*Proof.*
- (A1),(A3): K2 applied to each graph; sum over graphs; substitute $O_{\rm bare}=Z^{-1}[O]$; $\overline{\rm MS}$ finiteness by K2; IR finiteness of $\tilde G_{[O]}$ by K1 (BM II, Ω=4).
- (A2): at fixed ε, a $k$-loop hard part is exactly homogeneous of degree $2-d_O-2k\varepsilon$ (Smirnov's eq. (5)). Expressing $g_0$ through $\alpha_s(\mu)$ and multiplying by $Z^{-1}$ gives $|q|^{2-d_O}\sum_kc_k(\varepsilon)(\mu^2/q^2)^{k\varepsilon}$, with poles of order $\le r$. Finiteness forces the limit to be a polynomial of degree $\le r$ in $L$.
- (A4): two solutions differ by $\Delta_O=|q|^{2-d_O}P(L)$ with $\Delta_O=O(|q|^{1-a}\ln^k)$ (Lemma A.3). So $|P(L)|\le K|q|^{-(a+1-d_O)}\ln^k\to0$, and the polynomial $P$ vanishes.
- (A5): $\sum_iC_i(\mu)[O_i]_\mu$ is μ-independent. Differentiating and using $\mu\,d[O_i]/d\mu=-\gamma_{ij}[O_j]$ shows the bracket is $O(\text{remainder})$. It has the log-polynomial structure, so it vanishes by (A4). ∎

Grade: (A1),(A3) [R-cited]; (A2),(A4),(A5) [R]. Assembly is new here; the reference's Thm C.35 cites the same sources.

**Remark A.6 (correction to CLAIMS R-M26).** R-M26 says that "by uniqueness, any proven momentum-space OPE would discharge Ass. C.24". This is circular, because the reference's uniqueness Thm C.25(iii) is itself proven *given* C.24: it subtracts two expansions that are both assumed to have small remainders.
- In the DR route no analogue of C.24 is needed; the remainder estimate is part of K2.
- For the reference's frozen-$q$ BPHZ construction, C.24 still needs an identification lemma: the frozen-$q$ coefficients must equal the K2 coefficients after scheme change, up to the remainder. This is open (O3).

**Theorem B (gauge-invariant reduction).** Inputs, all bare DR at fixed generic ε:
- (DR-WI) For local monomials $X_i$: $\sum_i\pm\langle TX_1\cdots(sX_i)\cdots\rangle=0$ exactly. Holds because the regularized action and measure are BRST-invariant ('t Hooft–Veltman 1972; BM 1977).
- (DR-SD) $\langle T(Y\,\partial^\alpha\frac{\delta S}{\delta\phi})(0)\,\Phi\rangle=i\sum_{k:\phi_k=\phi}\pm(\hat p_k)^\alpha\langle TY(0)\Phi_{\hat k}\rangle$, with the δ(0) terms equal to 0 in DR.
- ($E_\varepsilon$) For $\mathcal J(q)$ with Φ, and with one composite spectator $Z=s\phi$:
  $$\langle\mathcal J\Phi\rangle=\sum C_O\langle O\Phi\rangle+\mathcal R,\qquad \langle\mathcal J\,Z(p_Z)\Phi\rangle=\sum C_O\langle O\,Z\Phi\rangle+\sum C^Z_{O'}(q;p_Z)\langle O'\Phi\rangle+\mathcal R'.$$
  The coefficients $C_O$ are the same in both; $C^Z$ is polynomial in $p_Z$ (it comes from hard subgraphs containing the $Z$ vertex); all coefficients are graded-homogeneous. This is K2 graph by graph.
- (LBC) For ghost number 0: $sX\in\mathcal E$ implies $X=\sum c_jO^{GI}_j+s\Lambda+E$ with $E\in\mathcal E$ (K6).

Conclusion:
- For every dimension $d$ (and every hard-loop grade), $sX_d\in\mathcal E_{d+1}$ with $X_d=\sum_{d_O=d}C_OO$.
- Hence $X_d=$ GI + $s$-exact + EOM.
- With K3, $X_d=\sum c'_j[O^{GI}_j]+$aliens, with $c'=cZ_{GG}^{-1}$ finite.
- The $\overline{\rm MS}$ coefficients of "rest" operators vanish.
- Between physical states only GI operators survive. The twist-2 part involves only $O_q$ and $O_g$ (twist classification, ref. Lemma C.42).

*Proof.*
1. $sJ=0$, so DR-WI gives $\sum_k\pm\langle\mathcal J\,\phi_1\cdots(s\phi_k)\cdots\phi_n\rangle=0$.
2. Insert $E_\varepsilon$ into each term. The first sums combine by DR-WI into $\mp\sum_OC_O\langle(sO)\Phi\rangle$.
3. The merged terms equal $\sum_k\pm\sum_{O'}C^{s\phi_k}_{O'}(q;p_k)\langle O'\Phi_{\hat k}\rangle$. By DR-SD this is $\langle\mathbb E(q)\Phi\rangle$ for the EOM operator $\mathbb E=\sum_\phi\sum_{O'}O'\cdot C^{s\phi}_{O'}(q;-i\partial)\frac{\delta S}{\delta\phi}$, a q-dependent combination of EOM monomials. The SD contact term puts the operator at the point of leg $k$, which in momentum space absorbs $p_k$ — consistent with the merged term.
4. Hence $\langle[\mp\sum C_O\,sO+\mathbb E]\Phi\rangle=\text{remainder}$ for every Φ.
5. Lemma A.3 at fixed ε (graded homogeneity: $sO$ and the EOM terms pair with the same powers of $q$) gives $\sum C_O\,sO=\pm\mathbb E\in\mathcal E$, degree by degree.
6. Apply LBC.
7. Physical states: EOM operators vanish on shell; $\langle s\Lambda\rangle=0$ by Kugo–Ojima. For partons at tree level: $B$ legs give $p\cdot\varepsilon=0$, and ghost terms do not contribute. ∎

Grade: [R-cond: E_ε], with DR-WI, DR-SD and LBC cited. **New proof.**
- Compared with the reference's Prop C.44: (B1) is not needed. Its claim that the contact terms are polynomial in $q$ is in general false; they carry logarithms, but they are EOM operators.
- (B2) reduces to $E_\varepsilon$ with one spectator.

**Theorem I = A + B** (statement as in §0 (i)). Grade [R-cited].

**Gap analysis: four routes.**
1. **DR (Smirnov–Gorishny) + Theorem B.** Complete, modulo reading the K2 full texts (O1).
2. **BPHZL.** Convergence is available (K1). A remainder estimate (the analogue of C.24) is not. BRST needs finite counterterms (algebraic renormalization). More gaps.
3. **Flow equations (FHH/FH).** Rigorous for pure YM. For QCD the missing piece is FHH with Dirac fermions (O2). The anomaly condition holds by parity and K6. FH is a preprint.
4. **Hollands 2008.** Pure YM; matter is only discussed in §5.1.

**Exactly missing for QCD with quarks:** (a) a verbatim BRST-covariance theorem for the OPE coefficients, now closed by Theorem B; (b) full-text verification of the operator-level K2 for gauge theories with composite spectators.

## 4. Part II: from Euclidean to forward kinematics

**Lemma F.0 (forward 2-forest structure).** Take a connected graph with incoming $p$ at $P_1$, $-p$ at $P_2$, $q$ at $J_1$, $-q$ at $J_2$ (vertices may coincide), and $p^2=0$. Then
$$\mathcal F=Q^2(\hat F_0+\omega\hat F_1),\quad \hat F_0=\sum_{T:\,c_q\neq0}\alpha^{E\setminus T},\quad \hat F_1=-\sum_Tc_pc_q\,\alpha^{E\setminus T},$$
with $c_p,c_q\in\{0,\pm1\}$. In particular ${\rm mon}(\hat F_1)\subset{\rm mon}(\hat F_0)$ with $|\text{coef}|\le1$, and $\hat F_0$ is the $\mathcal F$-polynomial of the propagator-type graph at $p=0$.

*Proof.* A 2-forest component contains external momentum $c_pp+c_qq$. Then $-s=Q^2(c_q^2-c_pc_q\omega)$, using $p^2=0$ and $2p\cdot q=\omega Q^2$. A monomial determines its 2-forest. ∎

[R], new. Checked on 21 QCD forward topologies at 1–3 loops and 400 random graphs (f1).

**Lemma F.1 (Newton-polytope domination).** Let $\mathcal G_\lambda=\mathcal U+\hat F_0+\lambda\hat F_1$, with $\mathcal U,\hat F_0$ having positive coefficients, ${\rm mon}(\hat F_1)\subset{\rm mon}(\hat F_0)$ and $|\text{coef}_1|\le\text{coef}_0$. Let $g(\alpha,\lambda)$ be polynomial in λ, let $P={\rm Newt}(\mathcal U+\hat F_0)$ be full-dimensional, and $|\lambda|\le r<1$. Then:
- (a) $I(\lambda)=\int\alpha^{s-1}g\,\mathcal G_\lambda^{-c}$ and all Taylor-term integrals $I_n$ converge absolutely on a common nonempty open set Λ.
- (b) $I(\lambda)=\sum_n\lambda^nI_n$ on Λ, uniformly for $|\lambda|\le r$.
- (c) $I$ and $I_n$ continue meromorphically in $(s,c)$. The polar set consists of λ-independent hyperplanes, $I$ is holomorphic in λ, and $\frac1{n!}\partial^n_\lambda I|_0=I_n$ holds after continuation.

*Proof.*
- (a) The coefficients $c_m(1+\lambda\theta_m)$ lie in the sector $|\arg|\le\arcsin r$, and ${\rm Newt}(\mathcal G_\lambda)=P$ because no vertex coefficient vanishes. Schultka Thm 3.1 applies.
  - The $n$-th Taylor term has the form $\mathcal M$ with numerator $g\hat F_1^n$ and exponent $c+n$.
  - Its convergence condition differs from the λ=0 one by $n[d_\rho(\hat F_1)-d_\rho(\mathcal G_0)]\ge0$. So it holds on $\Lambda=\bigcap_j\Lambda(g_j)$.
  - Λ is nonempty because $P({\rm Re}\,c)$ scales linearly in Re c and the numerator shifts are finitely many.
- (b) $|\hat F_1|\le\hat F_0\le\mathcal G_0$ pointwise, so $\mathcal G_\lambda^{-c}=\mathcal G_0^{-c}\sum_n\binom{-c}{n}(\lambda\hat F_1/\mathcal G_0)^n$. Since $\sum_n|\binom{-c}{n}|r^n\le(1-r)^{-|c|}$, the series is dominated by $(1-r)^{-|c|}\sum_j|g_j|\,\mathcal G_0^{-{\rm Re}\,c}$. Tonelli and Fubini then give the termwise expansion.
- (c) Kaneko–Ueda cubes (Schultka Cor 3.8):
  - On each cube, $\mathcal G_\lambda=x^{m_\sigma}f_{\sigma,\lambda}$ with $f_{\sigma,\lambda}=f_{\sigma,0}+\lambda f_{\sigma,1}$. Here $f_{\sigma,1}$ is a polynomial, because every monomial of $\hat F_1$ is a monomial of $\hat F_0$.
  - ${\rm Re}\,f_{\sigma,\lambda}\ge(1-r)f_{\sigma,0}\ge c_0>0$ on $[0,1]^N$.
  - Gel'fand–Shilov Taylor subtraction in each $x_j$ then gives a continuation with poles at $A_j(s,c)\in-\mathbb N_0$ ($A_j$ affine and λ-independent) and residues holomorphic in λ.
  - Both sides of the Taylor identity are meromorphic and agree on Λ, so they agree everywhere. ∎

[R], new; it uses K8.

**Theorem F (forward on-shell DR amplitude).** Let Γ be any graph of the amputated forward amplitude of a massless parton $j$ plus two currents (amputated: no external-leg corrections). Lines carrying exactly 0 vanish by colour; graphs with lines carrying exactly ±p are external-leg corrections. Consider any tensor component contracted with $p$-independent tensors (spin sums are polynomial in $p$). Assume (F-DR): the $p=0$ propagator-type integrals are DR-admissible, i.e. no $D$-independent polar hyperplane contains the DR line. This holds unless they are scaleless; verified for all listed graphs (f1 C3).
- **(F1)** For ω in the cut plane $\mathcal C=\mathbb C\setminus((-\infty,-1]\cup[1,\infty))$: the analytically regularized integral converges on an ω-independent nonempty open set, continues meromorphically with ω-independent poles, and is holomorphic in ω. So every DR Laurent coefficient is holomorphic on $\mathcal C$.
- **(F2)** For $|\omega|<1$, each Laurent coefficient equals $\sum_n\omega^nI^{[k]}_n$, where $I_n$ is the DR integral of the $n$-th naive Taylor term. The series converges absolutely, locally uniformly.
- **(F3)** If ${\rm Newt}(\mathcal U+\hat F_0)$ is not full-dimensional, both sides are scaleless (zero in DR).

*Proof.*
- Tarasov reduction gives LP integrals with prefactors polynomial in λp.
- Lemma F.0 gives $\mathcal G_\omega=\mathcal U+Q^2(\hat F_0+\omega\hat F_1)$.
- For ω outside the real axis, $\{1,1\pm\omega\}$ lie on a line through 1 that misses 0. They are therefore in an open half-plane, as is the Newton polytope's coefficient set; for real $|\omega|<1$ they are all positive. Then Newt is unchanged and Schultka Thm 3.1 applies.
- Joint holomorphy: Kaneko–Ueda cubes on compact subsets of $\mathcal C$, with $|f_\sigma|$ bounded below.
- (F2): rescale λ and apply Lemma F.1. The parametric Taylor terms equal the parametric representations of the naive momentum-space terms pointwise in α (Schwinger + Gaussian, with the λ-derivative under the Gaussian integral). Then restrict to the DR line.
- (F3): a degenerate Newt is invariant under a 1-parameter scaling $t^u$, so the DR value is 0 for both sides. ∎

[R], **new rigorous proof** of the folklore "method of projectors" statement (Gorishny–Larin–Tkachov 1983; Larin–van Ritbergen–Vermaseren 1994; MVV 2005).

**Corollary F.2 (forward partonic OPE at every order).** Hypotheses: Theorem A (A3, finiteness), Theorem B, K3, twist classification, and Theorem F. Statement: at every order in $\alpha_s(\mu)$ and every Laurent order in ε, for $|\omega|<1$,
$$T_2^{(j)}=4\sum_{n\ \rm even}\omega^{n-1}\sum_iC^{(n)}_{2,i}(Q^2/\mu^2,\alpha_s)\,A^{(n)}_{i/j},$$
where $C$ are the finite Euclidean $\overline{\rm MS}$ coefficients and $A^{(n)}_{i/j}=\sum Z\cdot$tree $=$ tree + pure poles. Hence Prop C.54(a) holds, and (C.36) holds without its hypotheses (a) and (c).

*Proof.*
1. Forward graphs are exactly the AI 2-leg hard graphs. Non-AI graphs carry 0 or ±p and are excluded.
2. By Theorem F, the forward amplitude equals $\sum_\Gamma$(naive Taylor) $=\sum_OC^{\rm bare}_OV_O(p,-p)$, i.e. bare coefficients times on-shell bare matrix elements, which equal the tree values since loops are scaleless.
3. Substitute $C^{\rm bare}=C^{\overline{\rm MS}}Z$. By Theorem B and K3, $C^{\overline{\rm MS}}_{\rm rest}=0$.
4. Aliens have $A=0$: EOM operators vanish on shell, $B$ legs give $p\cdot\varepsilon$, ghosts do not appear, and aliens mix only into aliens.
5. GI operators with $p^2=0$ contribute to $T_2$ only at twist 2 (the matrix element is built from $p$ only, so $d-2=r$).
6. Finiteness of $C$ follows from Theorem A. ∎

[R-cited], via Thm A. **New**: it closes the reference's Rem C.37 / C.54(a) gap in DR. One-loop instance: c_dis `ope_check` N≤8, exact in ε, and `ope_wilson` N≤6.

**Corollary F.3.** At each order the partonic $T_2^{(j)}$ Laurent coefficients are holomorphic on $\mathcal C$ with ${\rm Disc}=4\pi iF_2^{(j)}$ [R]. The moment identity $t_n=4\int x^{n-2}F_2^{(j)}$ for even $n>A+1$ needs fixed-order polynomial growth bounds; this is [A] (O4). At one loop it holds for all $n\ge1$ [R] (c_dis).

**Example F.3 (exact one-loop triangle).** Lines $k$ ($a_3$), $k+q$ ($a_2$), $k-p$ ($a_1$), with $p^2=0$:
$$I=\frac{\Gamma(a-\frac D2)}{\prod\Gamma(a_i)}(Q^2)^{\frac D2-a}\,B\!\left(\tfrac D2-a_2,\tfrac D2-a_1-a_3\right)B(a_1,a_3)\;{}_2F_1\!\left(a-\tfrac D2,a_1;a_1+a_3;\omega\right).$$
- The $\omega^n$ coefficient equals the naive term $\frac{(a_1)_n}{n!}A(n,0)$ identically in $(a_i,D)$ (sympy ratio = 1).
- Numerical agreement with a direct Feynman-parameter integral.
- At $a_i=1$: each $\omega^n$ term carries an IR pole, $-\frac1{(n+1)\varepsilon}+\dots$ (f2).

**Example F.4 (non-uniformity).** With an off-shell leg $p^2=-P^2$ and ω=0, in $D=4$: $Q^2I=\ln(Q^2/P^2)+2+O(P^2\ln)$. Numerically checked at $P^2/Q^2=10^{-2},10^{-4},10^{-6}$. The hard coefficient is unchanged, but the matrix element diverges as $P^2\to0$. In DR on shell it becomes the pure pole $-c_\Gamma(Q^2)^{-1-\varepsilon}/\varepsilon$. So no limiting argument from the off-shell OPE works; Theorem F avoids the limit.

**Remark F.5.** Zero-momentum insertions of $O^{(n)}$ with $n\ge2$ (Ω=$n+2\ge4$) into 2-point functions at $p^2<0$ are first-order perturbations of IR degree ≥4. They are therefore IR finite to all orders by BM II [A]. This answers the open question of Rem C.37, in DR.

**Lemma 4.10 (hadronic side).** The only information about $T_2$, beyond W1–W3, that the hadron-level theorem uses is the segment approximation SA (N1) on $\mathcal I_Q$. No perturbative statement implies it, because it concerns non-perturbative target states. There is no exceptional-momentum obstruction (M>0, W2). Corollary F.2 is its perturbative counterpart: the IR poles of $A_{i/j}$ play the role of the NP matrix elements. [R] (logic).

## 5. Part III: hadron-level DIS

**Assumptions.**
- **W1.** Wightman framework: Hilbert space, positive-energy unitary representation of the Poincaré group, unique vacuum. $J^\mu$ is hermitian, local, covariant, conserved and tempered. Parity holds, with $J$ a polar vector.
- **W2 (corrects ERR-M25).** The target is a stable spin-½ particle of mass $M$ in the superselection sector $\mathcal H_T$ of its conserved flavour numbers, with ${\rm spec}(P)|_{\mathcal H_T}\subset\{p^2=M^2\}\cup\{p^2\ge M_1^2\}$, $M_1>M$. This requires physical light-quark masses ($m_\pi>0$). Only ${\rm spec}\subset\{p^2\ge M^2\}$ enters the analysis.
- **W3.** The spin-averaged connected forward commutator $C^{\mu\nu}(z)$ is tempered, and it has a retarded part $R$ with:
  - support in $\bar V_+$, $R-A=C$, crossing $A^{\mu\nu}(z)=R^{\nu\mu}(-z)$;
  - covariance under the little group, symmetry, parity-even;
  - conservation, $q_\mu\tilde R^{\mu\nu}=0$.
  - Freedom: $\sum c_\alpha\partial^\alpha\delta$ (polynomial in $q$).
- **N1 (segment approximation SA, for a given even n).** There are $N\ge\max(n+3,n_0+2)$ and $Q_0,K,k$ such that for $Q\ge Q_0$ some odd polynomial $P_N=\sum_{m\le N-2,\ \rm even}\pi_m\omega^{m-1}$ satisfies:
  - (a) $\sup_{\mathcal I_Q}|T_2-P_N|\le K(M/Q)^{N-2}\ln^kQ$;
  - (b) $|\pi_m|\le K\ln^kQ$;
  - (c) $\pi_n=4\sum_iC^{(n)}_{2,i}A^{(n)}_i+O\big((M^2+mM)Q^{-2}\ln^k\big)$.
- **N1-std (standard NP OPE).** On the Euclidean set $E_Q$, $T=\sum_{d_j\le N}\tilde C_j\langle P|O_j|P\rangle+O(|q|^{1-N}\ln^k)$, where:
  - the coefficients are covariant (built from $q$, $g$; no ε by parity) and bounded, $|\tilde C_j|\le K|q|^{2-d_j}\ln^k$;
  - finitely many operators appear up to each dimension;
  - twist ≥2, and the twist-2 symmetric traceless part is spanned by $O_q,O_g$;
  - chiral suppression: odd-twist coefficients are $\le Km|q|^{1-d}\ln^k$.
- **N2.** Twist-2 RG with $\gamma^{(n)}$ asymptotic to $\overline{\rm MS}$, $\beta=-b\alpha^2(1+o(1))$ with $b>0$, and $C^{(n)}_{2,i}(1,\alpha_s(Q))$ asymptotic to $\overline{\rm MS}$ PT.
- **N3.** PDFs exist, with moments $A^{(n)}_i$.
- **G.** $\lim_{y\to\infty}T_2(iy)/(iy)=0$.
- **Φ.** $x$-space measures with the twist-2 moments exist.

**Lemma 5.1 (Euclidean segment).** $\hat P^2=M^2\mathbf q^2/Q^2\ge M^2/4$ and $\omega=2iMq^4/Q^2$ covers $\mathcal I_Q$. [R] (h1 c)

**Lemma 5.2 (N1-std ⇒ SA for all N).**
- Transversalize with $\Pi=g-qq/q^2$, which is bounded at Euclidean points.
- Then $\Pi X_j\Pi=A_j\tilde g+b_j\hat P\hat P$, where $b_j$ is the $PP$-coefficient of the explicit tensor $X_j=\tilde C_j\langle O_j\rangle$.
- $T_2=\sum_j\nu b_j+\Pi_2(\Pi R_N\Pi)$ with $\Pi_2=\nu(3PP-\hat P^2g)/(2(\hat P^2)^2)$, which satisfies $|\Pi_2|\le CQ/M$ on $\mathcal I_Q$ (h1 b, i).
- $\nu b_j$ is a polynomial of degree $\le r_j-1$ and parity $(-1)^{r_j-1}$, with size $(M/Q)^{t-2+2b}\omega^{r-1-2b}$ (twist $t$).
- Twist 2 with $b=0$ gives the leading coefficients; trace terms give $M^2/Q^2$; twist 3 with chiral suppression gives $mM/Q^2$; twist ≥4 gives $\le M^2/Q^2$.
- Define $P_N$ as the odd part. [R-cond: N1-std]. Without chiral suppression the error is $O(M/Q)$.

**Lemma 5.3 (Markov).** For an odd polynomial of degree $\le D_g$: $|h_k|r^k\le c_{D_g}\sup_{|y|\le r}|h(iy)|$, with $c\le2\max|{\rm coef}\,T_{D_g}|\le2(1+\sqrt2)^{D_g}$. [R] (sharp via Chebyshev; h1 h)

**Lemma 5.4 (Jensen).** If $f$ is entire and $|f|\le C(1+|z|)^A|{\rm Im}\,z|^{-B}$, then $f$ is a polynomial of degree $\le A$.

*Proof.* Subharmonicity on circles of radius 2 gives $\log|f(z)|\le\log C+A\log(3+|z|)-BJ({\rm Im}\,z)$, where $J(y)=\frac1{2\pi}\int\log|y+2\sin\theta|=\log\max(1,|w_\pm|)\ge0$ (Jensen applied to $w^2+iyw-1$). Then use Cauchy estimates. [R] (h1 a)

**Lemma 5.5 (boundary values).**
- (a) Let $f$ be holomorphic for $0<{\rm Im}\,z<1$ with $|f|\le C(1+|z|)^A({\rm Im}\,z)^{-B}$. Then $|\langle f(\cdot+i0),\chi\rangle|\le C'\sum_{j\le\lceil B\rceil+1}\int(1+|x|)^A|\chi^{(j)}|$. This uses the almost-analytic extension $\tilde\chi=\rho(y)\sum_{j\le K}\chi^{(j)}(iy)^j/j!$, with $\bar\partial\tilde\chi=\frac12\rho\,\chi^{(K+1)}(iy)^K/K!+(\rho'$-terms$)$, and Stokes. Consequently a positive jump measure has $\nu([R,2R])\le CR^{A+1}$.
- (b) One-dimensional distributional edge of the wedge: take $K$-fold primitives, which have continuous boundary values; they differ by a polynomial; apply Painlevé. [R] (Hörmander §3.1)

**Prop 5.6 (dispersion relation from W).** Under W1–W3:
- (a) $T_2(\omega,Q^2)$ is holomorphic on $\mathcal C$ and odd;
- (b) $|T_2|\le C_Q(1+|\omega|)^A|{\rm Im}\,\omega|^{-B}$ with $A,B$ independent of $Q$;
- (c) ${\rm Disc}\,T_2=4\pi i\nu_Q$, where $\nu_Q(d\omega)=F_2(1/\omega)d\omega\ge0$ on $[1,\infty)$, elastic point included;
- (d) for even $n_0>A+1$: $T_2=\sum_{n<n_0}t_n\omega^{n-1}+4\omega^{n_0-1}\int_{(0,1]}\frac{x^{n_0-2}F_2\,dx}{1-x^2\omega^2}$, so $t_n=4M^{(n)}_2$ for $n\ge n_0$.

*Proof.*
1. $T=i\tilde R$ on the forward tube $T_+$ and $T=i\tilde A$ on $T_-$, with Vladimirov bounds.
2. Crossing gives $T^{\nu\mu}(q)=T^{\mu\nu}(-q)$, hence $T_2$ is odd.
3. $S_1=PPT$ and $S_2=gT$ are SO(3)-invariant. On the slice $(w,0,0,s)$ they are even in $s$, hence holomorphic in $(w,s^2)$. Along $s^2=w^2+Q^2$ the root with Re s>0 satisfies $|{\rm Im}\,s|<{\rm Im}\,w$. So $T_2=\nu(3s_1-\hat P^2s_2)/(2(\hat P^2)^2)$ is holomorphic on the upper half-plane except possibly at $w=iQ$.
4. At $w=iQ$: the local covariant decomposition $T^{ij}=a\delta+bqq$, $T^{0i}=cq$, $T^{00}=e$, with $a,b,c,e$ holomorphic, together with transversality, gives $T_2=Q^4(b+a/Q^2)/\nu$. This is regular (h1 d). [Fixes the $\hat P=0$ point.]
5. Bounds: ${\rm Im}\,w-|{\rm Im}\,s|\ge{\rm Im}\,w\,Q^2/(2(|w|^2+Q^2))$ (h1 e); $|\hat P^2|\ge M^2/2$ away from $iQ$; maximum principle near $iQ$. This gives $A=a+2b+2$, $B=b$.
6. Jump: $i(\tilde R-\tilde A)=4\pi iW$. $W=0$ for $|\omega|<1$ by the spectral condition in $\mathcal H_T$. The slice boundary values depend continuously on $Q^2$ (primitive representation), so the 4D identities hold slice by slice. [Fixes E9.] Then Lemma 5.5(b) gives holomorphy on $\mathcal C$.
7. Positivity: $W$ is a positive matrix measure for ν>0. Contracting with $\hat P\hat P$ and with transverse vectors gives $F_1\ge0$ and $F_2\ge\nu F_1/\hat P^2\ge0$, slice by slice.
8. Growth: Lemma 5.5(a) gives $\nu_Q([R,2R])\le C_QR^{A+1}$, so $\int x^{n_0-2}F_2<\infty$ for $n_0>A+1$.
9. Dispersion: $H=T_2-\sum_{n<n_0}t_n\omega^{n-1}-D_{n_0}$ has no jump. Using $|1-x^2\omega^2|\ge({\rm Im}\,\omega)^2/|\omega|^2$, $|D|\le C|\omega|^{n_0+1}({\rm Im}\,\omega)^{-2}$, so Lemma 5.4 makes $H$ a polynomial. $H=O(\omega^{n_0-1})$ at 0, and $H(iy)/(iy)^{n_0-1}\to0$ because $T_2(iy)=O(y^A)$ and $D(iy)/(iy)^{n_0-1}=4\int x^{n_0-2}F_2/(1+x^2y^2)\to0$ by dominated convergence. Hence $H\equiv0$. ∎

[R-cond: W]. Re-proof with fixes; the explicit $n_0$ is new.

**Theorem 5.7 (fixed $n$).** Hypotheses: Prop 5.6 and N1 for $n$. Conclusion: $t_n=4\sum_iC^{(n)}_{2,i}A^{(n)}_i+O\big((M^2+mM)Q^{-2}\ln^kQ\big)$ for every even $n\ge2$.

*Proof.*
1. For $n'\ge n_0$, $0\le t_{n'}\le t_{n_0}$, so the tail on $\mathcal I_Q$ is $\le2t_{n_0}r_Q^{N-1}$.
2. $h=\sum_{n'\le N-2}(t_{n'}-\pi_{n'})\omega^{n'-1}$ satisfies $\sup_{\mathcal I_Q}|h|\le\varepsilon_N+2t_{n_0}r_Q^{N-1}$. Markov (Lemma 5.3) then gives $|t_{n'}-\pi_{n'}|\le c(\varepsilon_N+2t_{n_0}r_Q^{N-1})r_Q^{1-n'}$.
3. Bootstrap at $n'=n_0$: $t_{n_0}\le2|\pi_{n_0}|+2c\varepsilon_Nr_Q^{1-n_0}=O(\ln^kQ)$.
4. Hence $|t_n-\pi_n|=O((M/Q)^{N-1-n}\ln^k)=O(M^2/Q^2\ln^k)$. Combine with N1(c). ∎

[R-cond: W, N1]. No sum over spins is needed. The minimal hypothesis is new.

**Prop 5.8 (low moments).** Suppose (d) holds with some $n_0\ge4$. Then [$t_n=4M^{(n)}_2$ for all even $2\le n<n_0$] iff G.

*Proof.* (⇐) by descending induction. The order-$k$ relation gives
$$\frac{T_2(iy)}{iy}=\sum_{n<k-2}t_n(iy)^{n-2}+(iy)^{k-4}\Big[t_{k-2}-4\int x^{k-4}F_2\frac{x^2y^2}{1+x^2y^2}\Big]$$
(integrand identity, h1 g). G forces the bracket to tend to 0, so $\int x^{k-4}F_2=t_{k-2}/4<\infty$, and the order-$(k-2)$ relation follows. (⇒) $T_2(iy)/(iy)=4\int F_2/(1+x^2y^2)\to0$. ∎

[R-cond: W]. Regge behaviour is neither necessary nor sufficient: a fixed pole $c\omega$ is invisible in $F_2$.

**Theorem 5.9 (RG and asymptotic freedom).** Under N2:
$$C^{(n)}_{2,i}(Q^2/\mu^2,\alpha_s(\mu))=\sum_jC^{(n)}_{2,j}(1,\alpha_s(Q))\Big[\mathcal P\exp\Big(-\int_\mu^Q\frac{d\mu'}{\mu'}\gamma^{(n)}\Big)\Big]_{ji},$$
with $C(1,\alpha_s(Q))$ asymptotic to $\overline{\rm MS}$. Twist-2 $\overline{\rm MS}$ RG is mass-independent and has no lower-dimension mixing at rank $n$, so E10 does not arise. [R-cond: N2]

**Theorem M (hadron-level DIS moments).**
- (i) [W, N1] $t_n=4\sum CA+O\big((M^2+mM)Q^{-2}\ln^k\big)$ for every even $n$.
- (ii) [W] $t_n=4M^{(n)}_2$ for even $n\ge n_0$, hence $M^{(n)}_2=\sum CA+O(\cdot)$.
- (iii) [+G] (ii) for all even $n\ge2$, including the momentum sum rule; G is necessary.
- (iv) [+N2] the RG-improved coefficients are asymptotic to PT.
- (v) [+Φ] weak $x$-space convergence (ref. Cor C.52; uniqueness from c_pdf Thm 7.2).

## 6. Part IV: e⁺e⁻ and the Adler function

- **V1:** W1 in the vacuum sector; no massless spin-0 state couples to $J$ (C-parity).
- **V2:** the NP OPE for $D(Q^2)$ with remainder $O(Q^{-N})$ and derivative bounds.
- **V3:** the identity coefficient is asymptotic to $R_0\sum d_ka^k$.
- **V2′:** V2 uniformly on the sector $|\arg Q^2|\le\pi-\theta_0$.

**E1.** Källén–Lehmann: $\hat W=2\pi\theta(q^0)(qq-q^2g)\rho(q^2)$ with $\rho\ge0$ a tempered measure (contract with $\varepsilon\perp q$). Defining $D=Q^2\int R/(s+Q^2)^2$ with $R=12\pi^2\rho$, the following are equivalent: $\int\rho/(1+s)^2<\infty$; $D<\infty$ at some (hence every) $Q^2$; $\Pi$ is given by a once-subtracted relation. $D$ is then holomorphic off $(-\infty,0]$ and positive. [R]

**E2.** $D=R_0\big[1+\sum_{k\le K}d_ka^k\big]+O(a^{K+1})+O(m^2/Q^2)+O(\Lambda^4Q^{-4}\ln^k)$. There is no GI dimension-2 scalar in the chiral limit. [R-cond: V1–V3]

**E3.** $M_k=kQ^{2k}\int R/(s+Q^2)^{k+1}$ satisfies $M_1=D$, $M_{k+1}=M_k-\frac{Q^2}k\frac{dM_k}{dQ^2}$, and therefore $M_k=R_0[1+d_1a+(d_2+H_{k-1}b_0d_1)a^2+O(a^3)]$, with $Q^2\,da/dQ^2=-b_0a^2$ and $b_0=\beta_0/4$. [R-cond: V1–V3 + derivative bounds] (e1 c)

**E4 (exact counterexample).** For $|\kappa|<1$, $R=R_0[1+\kappa\sin(\sqrt s/\Lambda)]$ is positive and gives $D=R_0[1+\kappa\frac\pi2\frac Q\Lambda e^{-Q/\Lambda}]$. This follows from $\int_0^\infty\frac{2t\sin t}{(t^2+b^2)^2}dt=\frac\pi2\frac{e^{-b}}b$. So $R$ has no limit, while the Euclidean asymptotics agree with the constant model to all orders. Fixed-width smearing (width ≪ the local period $\sim4\pi\sqrt s\Lambda$) also fails to converge. [R] (e1 a, b)

**E5 (Tauberian).** If $R\ge0$ and $D\to R_0$, then $\frac1s\int_0^sR\to R_0$.

*Proof.* $D/Q^2=\int_0^\infty e^{-uQ^2}uL(u)\,du$ with $L(u)=\int e^{-us}R$. Karamata gives $\int_0^uvL\sim R_0u$. Since $L$ is monotone, $uL(u)\to R_0$ (squeeze with λ→1). Karamata applied to $L$ then gives $\sigma(s)\sim R_0s$. ∎

[R-cond: V1 + leading term]. New in this context; the method is classical. In the E4 model the rate is $O(\Lambda/\sqrt s)$ (e1 d).

**E6 (PQW smearing).**
$$\bar R_\Delta(s)=12\pi\,{\rm Im}\,\Pi(s+i\Delta)=\frac1{2\pi}\int_{-(\pi-\theta)}^{\pi-\theta}D\big(|s+i\Delta|e^{i\phi}\big)\,d\phi,\qquad\theta=\arctan(\Delta/s).$$
- With $\Delta=s\tan\theta$ and V2′, this equals $R_0[(1-\theta/\pi)+\dots]$ plus PT corrections (e1 e).
- With Δ fixed, the arc approaches the cut. That needs local duality, which E4 shows is independent of the Euclidean OPE.
- Grade [R-cond: V2′].

**Perturbative e⁺e⁻:** cite c_ee Thm 5.1 (K10).

## 7. Verification log

- **f1**:
  - all 21 QCD forward topologies (1L box, vertex and self-energy graphs; gluon boxes; 2L ladders, crossed, vertex, 3-gluon, singlet; 3L ladders) satisfy domination, full dimensionality and DR admissibility;
  - of 400 random graphs, 400/400 satisfy domination, and all 34 full-dimensional ones are DR-admissible;
  - every degenerate graph is explained by one of: a self-loop, a zero-momentum bridge, a ±p bridge, a scaleless cut-vertex block, or no q-flow.
- **f2**: exact ratio = 1; numerical agreement at three parameter points; pole structure as stated; off-shell asymptotics confirmed.
- **h1**: Jensen; projector; segment bounds; removable point; slice inequality (0 violations in 50 000); subtracted dispersion relations agree to $10^{-26}$; jump ratio $1.0000015$; descending identity; Markov; projector norm $\le6.1\,Q/M$.
- **e1**: (a)–(e) all agree.
- **c_dis**: one-loop OPE vs cut moments, N≤8, exact in ε.

## 8. Changes relative to the reference's App C and to CLAIMS

1. Ass. C.24 is not needed in the DR route. R-M26's uniqueness argument for discharging it is circular.
2. (B1) is unnecessary, and its polynomial contact terms are in general false; the contact terms are EOM operators (Theorem B).
3. C.54(a) is proven in DR (Theorem F, Corollary F.2).
4. The zero-momentum IR question of Rem C.37 is settled by BM II (Remark F.5, [A]).
5. W2 corrected (ERR-M25); slice edge of the wedge fixed (E9); E10 avoided; $n_0$ made explicit; $\hat P=0$ point treated rigorously.
6. C.58 replaced by the weaker segment approximation N1.
7. Rem C.62 extended to E1–E6, including the duality results E4–E5.

## 9. Open problems

See the `open` list.

## 10. Key references

- K1: Lowenstein–Zimmermann 1975; Lowenstein 1976; Breitenlohner–Maison 1977 I–III; Poggio–Quinn 1976.
- K2: Smirnov CMP 134 (1990) 109; Smirnov, Birkhäuser 1991; Smirnov hep-th/9412063; Gorishny NPB 319 (1989) 633; Llewellyn Smith–de Vries NPB 296 (1988) 991; Chetyrkin TMF 75/76 (1988); Gorishny–Larin–Tkachov PLB 124 (1983) 217.
- K3, K4: Joglekar–Lee 1976; Joglekar 1977 I, II; Kluberg-Stern–Zuber 1975; Henneaux 1993; Collins–Scalise PRD 50 (1994) 4117.
- K5: Hollands RMP 20 (2008) 1033; FHH JMP 57 (2016) 122301; Fröb–Holland arXiv:1603.08012.
- K6: BBH Phys. Rep. 338 (2000) 439; BBH NPB 455 (1995) 357.
- K8: Schultka arXiv:1806.01086; Nilsson–Passare 2013; BFP 2014; Kaneko–Ueda 2010; Lee–Pomeransky JHEP 11 (2013) 165; Tarasov PRD 54 (1996) 6479.
- K9: Vladimirov 1979; Reed–Simon II; Hörmander I; Feller II; Korevaar 2004; Borwein–Erdélyi 1995.
- Other: Larin–van Ritbergen–Vermaseren NPB 427 (1994) 41; MVV NPB 724 (2005) 3; Kugo–Ojima 1979; 't Hooft–Veltman NPB 50 (1972) 318.

## results

### [results 1]
Thm A [Euclidean OPE for J^mu J^nu in massless QCD, full MS-bar basis]. Hypotheses: SU(N_c), n_f massless Dirac quarks; DR+MS-bar; Feynman gauge; fixed order r; Euclidean non-exceptional momenta. Claims: (A1) remainder O(|q|^{1-a} ln^k); (A2) coefficients = |q|^{2-d_O} x polynomial of degree <= r in ln(q^2/mu^2); (A3) C^MS = C^bare Z^{-1}; (A4) uniqueness (log-polynomial lemma); (A5) RG equation. Grade: [R-cited] for A1, A3 (Smirnov CMP 134 (1990) 109; Gorishny NPB 319 (1989) 633; Llewellyn Smith-de Vries NPB 296 (1988) 991; full texts not read; IR finiteness from Breitenlohner-Maison CMP 52 (1977)); [R] for A2, A4, A5 (proofs given). Status: assembly new; content standard.

### [results 2]
Lemma A.3 [linear independence of operator Green functions]. If sum_O c_O(q) G_[O];Phi(p) = O(|q|^rho ln^k) for all strings Phi and all p in an open non-exceptional set, at each order, then c_O = O(|q|^rho ln^k). Graded-homogeneous c_O of degree > rho vanish identically. Proof: induction on the order, using injectivity of tree-level vertex polynomials. Grade [R]. Known in spirit (reference Lemma C.30); here also at fixed epsilon.

### [results 3]
Remark A.6 [correction to CLAIMS R-M26]. The claim that uniqueness (ref. Thm C.25(iii)) lets any proven momentum-space OPE discharge Ass. C.24 is circular, because C.25(iii) is itself proven under C.24. The DR route needs no C.24. For the reference's frozen-q BPHZ construction, C.24 still requires an open identification lemma for its coefficients. Grade [R] (logic). New.

### [results 4]
Thm B [gauge-invariant (BRST) reduction of the OPE]. Inputs: (DR-WI) exact BRST Ward identities of bare DR Green functions with composite insertions (vector-like QCD, no gamma5); (DR-SD) Schwinger-Dyson identities; (E_eps) DR large-momentum expansion with at most one composite spectator s(phi), with the same coefficients C_O as without it plus merged coefficients C^{s phi}_{O'}(q;p) polynomial in p; (LBC) local BRST cohomology at ghost number 0 modulo EOM (Barnich-Brandt-Henneaux 2000). Conclusion: s X_d lies in the EOM ideal, hence X_d = GI + BRST-exact + EOM. With Joglekar-Lee, the MS-bar coefficients of non-GI, non-alien operators vanish and the GI coefficients c Z_GG^{-1} are finite; only O_q^(n), O_g^(n) survive in physical twist-2 matrix elements. Key step: the merged terms equal Green functions of the EOM operator E(q) = sum O' C^{s phi}(q;-i d) dS/dphi. Grade [R-cond: E_eps] with cited WI, SD, LBC. New proof: removes the reference's assumption (B1) and its claim that contact terms are polynomial in q; reduces (B2) to E_eps.

### [results 5]
Thm I [combined GI OPE for massless QCD with quarks] = Thm A + Thm B + twist-2 classification (ref. Lemma C.42). Grade [R-cited]. The step missing in the literature (BRST covariance of the OPE coefficients, available before only at physicist level in Joglekar Ann. Phys. 108/109 (1977), or for pure YM in Hollands RMP 20 (2008) 1033 and Frob-Holland arXiv:1603.08012) is closed here, conditional on E_eps. Alternative flow-equation route: the cohomological condition H^{1,4}_{E(4)}(s|d) = 0 holds for vector-like QCD by parity (BBH); what is missing is FHH-type bounds for YM with Dirac fermions.

### [results 6]
Lemma F.0 [forward Symanzik structure]. For any connected graph with external p, -p (p^2 = 0) and q, -q: F = Q^2 (F0hat + omega F1hat). Every monomial of F1hat is a monomial of F0hat with |coefficient| <= coefficient in F0hat. F0hat is the F-polynomial of the propagator-type graph at p = 0. Proof: 2-forest invariants -s = Q^2 (c_q^2 - c_p c_q omega). Grade [R]. New. Checked on 21 QCD topologies at 1-3 loops and 400 random graphs (f1).

### [results 7]
Lemma F.1 [Newton-polytope domination]. Let G_lambda = U + F0 + lambda F1 with positive U, F0, F1's monomials among F0's, |coef F1| <= coef F0, Newt(U+F0) full-dimensional, |lambda| <= r < 1. Then: the Mellin/LP integral and all its lambda-Taylor-term integrals converge absolutely on a common nonempty open set; I(lambda) = sum_n lambda^n I_n there; the meromorphic continuation in (exponents, D) has lambda-independent poles; the Taylor identity holds after continuation. Proof: Schultka Thm 3.1 (strongly convex cone); dominated binomial series with sum |binom(-c,n)| r^n <= (1-r)^{-|c|}; Kaneko-Ueda sector cubes with Re f_sigma >= (1-r) f_sigma,0 > 0; Gel'fand-Shilov continuation. Grade [R]. New.

### [results 8]
Thm F [forward on-shell DR amplitude: no regions beyond the hard one]. Hypotheses: amputated forward graph of a massless on-shell parton (p^2 = 0) with two currents; no lines carrying fixed momentum 0 or +-p; (F-DR) the p = 0 propagator-type integrals are DR-admissible (true unless scaleless). Claims: (F1) every DR Laurent coefficient is holomorphic in the cut plane C minus (-inf,-1] and [1,inf); (F2) for |omega| < 1 its Taylor series is exactly the naive Taylor expansion of the integrand in p (method of projectors), absolutely convergent; (F3) if Newt(U+F0hat) is degenerate, both sides are scaleless (zero). Grade [R]. New rigorous proof of a folklore statement used in Gorishny-Larin-Tkachov PLB 124 (1983) 217 and Larin-van Ritbergen-Vermaseren NPB 427 (1994) 41. Verified exactly at one loop (f2; c_dis ope_check N <= 8, exact in epsilon).

### [results 9]
Cor F.2 [forward partonic OPE at every order]. Hypotheses: Thm A (finite C^MS = C^bare Z^{-1}), Thm B, Joglekar-Lee triangularity, twist classification, Thm F. Claim: T2^(j)(omega) = 4 sum_{n even} omega^{n-1} sum_i C^(n)_{2,i}(Q^2/mu^2, alpha_s) A^(n)_{i/j}, at every order in alpha_s and every Laurent order in epsilon, for |omega| < 1. C are the Euclidean MS-bar coefficients; A = Z x tree (tree + pure IR poles). Consequence: the reference's Prop C.54(a) (forward remainder) is proven in DR, and (C.36) holds without its assumptions (a) and (c). Grade [R-cited] (via Thm A). New: closes the forward-kinematics gap of reference Rem C.37.

### [results 10]
Cor F.3 [perturbative cut-plane analyticity]. Each Laurent coefficient of the partonic T2^(j) is holomorphic in the cut omega-plane, with discontinuity 4 pi i F2^(j). Grade [R]. The moment identity t_n = 4 int x^{n-2} F2^(j) for even n > A+1 at all orders is [A] (needs fixed-order growth bounds); at one loop it is [R] for all n >= 1 (c_dis).

### [results 11]
Example F.3/F.4 [explicit checks]. One-loop forward triangle with general powers: I = Gamma(a-D/2)/prod Gamma(a_i) (Q^2)^{D/2-a} B(D/2-a2, D/2-a1-a3) B(a1,a3) 2F1(a-D/2, a1; a1+a3; omega); its omega^n coefficients equal the naive Taylor terms identically (sympy ratio = 1); each term at a_i = 1 has an IR pole. Off-shell leg p^2 = -P^2, omega = 0, D = 4: Q^2 I = ln(Q^2/P^2) + 2 + O(P^2 log), so the off-shell matrix element diverges as P^2 -> 0 while the hard coefficient is unchanged (no uniform limit). Grade [R]. Verified in f2.

### [results 12]
Remark F.5 [zero-momentum insertions, off-shell forward]. Zero-momentum insertions of twist-2 O^(n), n >= 2 (IR degree n+2 >= 4), into 2-point functions with p^2 < 0 are IR finite to all orders in DR, by Breitenlohner-Maison II (all interactions of IR degree >= 4). Grade [A] (hypotheses of BM II not checked in full text). New observation; answers the open question in reference Rem C.37.

### [results 13]
Lemma 4.10 [what the hadronic forward step needs]. Beyond the Wightman structure W1-W3, the hadron-level theorem uses only the segment approximation SA (N1) on I_Q = {i y : |y| <= sqrt3 M/Q}. No perturbative statement implies SA, because it concerns non-perturbative target states. The hadron mass removes the exceptional-momentum obstruction. Cor F.2 is the perturbative counterpart. Grade [R] (logic). Sharpened relative to the reference.

### [results 14]
Lemma 5.1-5.2 [Euclidean segment; standard NP OPE implies SA]. Lemma 5.1: rest-frame Euclidean q with |qvec| >= Q/2 gives Phat^2 = M^2 qvec^2/Q^2 >= M^2/4 and omega in I_Q; all of I_Q is attained. Lemma 5.2: covariance, coefficient bounds, twist >= 2, twist-2 spanned by O_q, O_g, and chiral suppression give an odd polynomial P_N with sup_{I_Q} |T2 - P_N| <= K (M/Q)^{N-2} ln^k and pi_n = 4 sum C A + O((M^2+mM)/Q^2 ln^k). Proof via transversalization and the PP-coefficient functional; the projector norm is <= C Q/M on I_Q. Grade [R] / [R-cond]. Re-proof of reference Lemma C.47.

### [results 15]
Lemma 5.3-5.5 [analytic tools]. 5.3 (Markov): odd polynomials of degree D_g satisfy |h_k| r^k <= c sup_{|y|<=r} |h(iy)|, with c <= 2 (1+sqrt2)^{D_g}, sharp via Chebyshev. 5.4 (Jensen): an entire f with |f| <= C (1+|z|)^A |Im z|^{-B} is a polynomial of degree <= A (circle averages; J(y) = log max(1, |w_+-|) >= 0). 5.5: boundary-value estimate via almost-analytic extension, giving nu([R,2R]) <= C R^{A+1} for a positive jump; distributional 1-d edge of the wedge. Grade [R]. Known; full proofs given.

### [results 16]
Prop 5.6 [dispersion relation from Wightman axioms]. Hypotheses: W1 (Wightman for J), W2 (target spectral condition in its flavour superselection sector; corrects reference ERR-M25), W3 (tempered forward commutator with covariant, symmetric, conserved, crossing-symmetric retarded part). Claims: T2 is holomorphic and odd in the cut omega-plane; |T2| <= C_Q (1+|omega|)^A |Im omega|^{-B} with A, B independent of Q; Disc T2 = 4 pi i nu_Q with nu_Q = F2(1/omega) d omega >= 0; for even n0 > A+1 the n0-subtracted dispersion relation holds, so t_n = 4 int x^{n-2} F2 for n >= n0. Grade [R-cond: W]. Re-proof of reference Lemma C.64 with fixes: rigorous removable point at Phat = 0; slice edge of the wedge via continuity in Q^2 (E9); explicit n0.

### [results 17]
Thm 5.7 [fixed-n Taylor coefficients]. Hypotheses: Prop 5.6 plus the segment approximation N1 for one N >= max(n+3, n0+2). Claim: t_n = 4 sum_i C^(n)_{2,i} A^(n)_i + O((M^2+mM)/Q^2 ln^k Q) for every even n >= 2. Proof: positivity tail 0 <= t_{n'} <= t_{n0}; Markov on I_Q; bootstrap t_{n0} = O(ln^k Q). No sum over spins. Grade [R-cond: W, N1]. Re-proof of reference Thm C.50 with a minimal hypothesis.

### [results 18]
Prop 5.8 [low moments iff growth]. Given the n0-subtracted relation with n0 >= 4: t_n = 4 int x^{n-2} F2 for all even 2 <= n < n0 (including the momentum sum rule) iff lim_{y->inf} T2(iy)/(iy) = 0. Proof: descending induction with an exact integrand identity. Regge behaviour is neither necessary nor sufficient; a fixed-pole term c omega is invisible in F2. Grade [R-cond: W]. Reference Rem C.65, re-proved.

### [results 19]
Thm 5.9 + Thm M [hadron-level DIS moment theorem]. Assumptions: W1-W3; N1 (segment approximation, the minimal NP OPE; implied by the standard OPE with chiral suppression); N2 (twist-2 RG and asymptotic freedom: coefficients at mu = Q asymptotic to MS-bar series); G (growth, only for n < n0); N3, Phi optional. Claims: (i) t_n = 4 sum C A + O((M^2+mM)/Q^2 ln^k) for every even n; (ii) M_2^(n) = sum C A + O(...) for even n >= n0, n0 explicit and Q-independent; (iii) with G, for all even n >= 2, and G is necessary; (iv) with N2, C(Q^2/mu^2) = sum_j C_j(1, alpha_s(Q)) [P exp(-int gamma)]_{ji}, asymptotic to PT (twist-2 RG is mass-independent, so the reference's mass-mixing norm issue E10 does not arise); (v) with Phi, weak x-space convergence. Grade [R-cond]. Refinement of reference Thm C.66.

### [results 20]
E1 [Kallen-Lehmann; one subtraction]. From W1 in the vacuum sector, with no massless spin-0 state coupling to J: hat W = 2 pi theta(q0) (qq - q^2 g) rho(q^2), rho >= 0 tempered. The following are equivalent: int rho/(1+s)^2 < inf; D(Q^2) = Q^2 int R/(s+Q^2)^2 is finite at one (hence every) Q^2; Pi admits a once-subtracted dispersion relation. Grade [R]. Known; precise form.

### [results 21]
E2 [Adler-function asymptotics]. Under V1-V3 (NP vacuum OPE; identity coefficient asymptotic to MS-bar): D(Q^2) = R0 [1 + sum_{k<=K} d_k a^k] + O(a^{K+1}) + O(m^2/Q^2) + O(Lambda^4/Q^4 ln^k); no 1/Q^2 term in the chiral limit (no GI dimension-2 scalar). Grade [R-cond: V]. Known (reference Rem C.62), precise statement.

### [results 22]
E3 [Euclidean moments of R]. M_k = k Q^{2k} int R/(s+Q^2)^{k+1} satisfy M_1 = D and M_{k+1} = M_k - (Q^2/k) dM_k/dQ^2. Hence M_k = R0 [1 + d1 a + (d2 + H_{k-1} b0 d1) a^2 + O(a^3)], with H_m the harmonic numbers and Q^2 da/dQ^2 = -b0 a^2 - ... Grade [R-cond: V + derivative bounds]. New presentation; verified symbolically for k <= 6 (e1).

### [results 23]
E4 [exact duality-violation counterexample]. R = R0 [1 + kappa sin(sqrt(s)/Lambda)], |kappa| < 1, is positive and gives exactly D(Q^2) = R0 [1 + kappa (pi/2)(Q/Lambda) e^{-Q/Lambda}], from int_0^inf 2t sin t/(t^2+b^2)^2 dt = (pi/2) e^{-b}/b. So the Euclidean OPE (to all power and log orders) plus positivity cannot determine R(s) pointwise, nor R smeared over a fixed width. Grade [R]. Explicit construction; known in spirit (duality violations); verified numerically (e1).

### [results 24]
E5 [Tauberian theorem for R(s)]. If R >= 0 and D(Q^2) -> R0 (the leading OPE term), then (1/s) int_0^s R -> R0. Proof: write D/Q^2 as the Laplace transform of u L(u), L(u) = int e^{-us} R; apply Karamata twice, with a monotone-density step in between. Grade [R-cond: V1 + leading term]. New in this context; method classical. In the E4 model the rate is O(Lambda/sqrt s).

### [results 25]
E6 [PQW smearing]. Rbar_Delta(s) = 12 pi Im Pi(s + i Delta) = (1/2pi) int_{-(pi-theta)}^{pi-theta} D(|s+i Delta| e^{i phi}) d phi, theta = arctan(Delta/s). With a sectorial OPE (V2'), proportional smearing Delta = s tan(theta) is asymptotic to PT, with leading term R0 (1 - theta/pi). Fixed-width smearing needs the OPE arbitrarily close to the cut (local duality), which E4 shows is independent. Grade [R-cond: V2']. Known in spirit (Poggio-Quinn-Weinberg); precise form; verified (e1).

### [results 26]
VERIF [verification log]. All checks pass. f1: 21 QCD forward topologies (1-3 loops) satisfy domination, full dimensionality and DR admissibility; 400/400 random graphs satisfy domination; every degenerate graph is explained (self-loop, zero-momentum bridge, +-p bridge, scaleless cut-vertex block, no q-flow). f2: exact hypergeometric vs naive Taylor terms; off-shell asymptotics. h1: Jensen; T2 projector; segment bounds; removable point; slice inequality; dispersion relations agree to 1e-26; jump normalization; descending identity; Markov; projector norm. e1: E3, E4, E5, E6 checks. c_dis: one-loop OPE vs cut moments, N <= 8, exact in epsilon.

## open

### [open 1]
O1: Read the full texts of Smirnov CMP 134 (1990) 109, Smirnov's 1991 book, Gorishny NPB 319 (1989) 633 and Llewellyn Smith-de Vries NPB 296 (1988) 991. Confirm that the operator-form DR/MS-bar large-momentum expansion covers gauge theories with ghosts and Green functions with one composite spectator (E_eps), with finite MS-bar coefficients C^bare Z^{-1}. This would make Thm A and Thm B fully [R].

### [open 2]
O2: Extend Frob-Holland-Hollands (JMP 57 (2016) 122301) to Yang-Mills with Dirac fermions: flow-equation existence, bounds and BRST Ward identities. This would give an independent rigorous route to the OPE and its BRST covariance for QCD (Frob-Holland Thms 1-2); the cohomological condition already holds by parity.

### [open 3]
O3: Identification lemma for the reference's frozen-q BPHZ coefficients: show they equal the coefficients of a proven OPE (after scheme change) up to the remainder. This would discharge Ass. C.24; uniqueness alone is circular.

### [open 4]
O4: Fixed-order polynomial growth bounds in omega for the partonic forward amplitude, which would give the moment identification for all n at all orders; also prove the absence of fixed poles (n = 2) at all orders.

### [open 5]
O5: Non-perturbative: construct 4D QCD; derive the segment approximation N1 (for example from Bostelmann's phase-space condition plus uniformity for single-particle states).

### [open 6]
O6: Derive the growth condition G (no real fixed-pole term c omega in T2) from axioms or Regge theory; it is equivalent to the low-moment sum rules, including the momentum sum rule.

### [open 7]
O7: Prove convergence (not only asymptoticity) of the OPE for Yang-Mills or QCD at fixed order, as Hollands-Kopper did for phi^4_4.

### [open 8]
O8: Polarized structure functions: gamma5 in DR breaks exact BRST invariance and the simple Ward identity; extend Thm B (e.g. Larin scheme with finite counterterms).

### [open 9]
O9: Local duality and pointwise R(s): quantify duality violations; obtain Tauberian remainder theorems strong enough to recover the alpha_s correction in the Cesaro mean of R.

### [open 10]
O10: OPE remainder estimates at exceptional (off-shell forward) momenta in BPHZL or DR; and check the hypotheses of Breitenlohner-Maison II for zero-momentum composite insertions (Remark F.5).

### [open 11]
O11: Renormalon / OPE-basis ambiguity: status of renormalon absorption into condensates (reference Prop C.68, Rem C.69) is unchanged.

## files

### [files 1]
/Users/hao-cheng/Desktop/theorem proof/qcd_factorization_work/verify/extend/X3-ope/scripts/f1_forward_graphs.py

### [files 2]
/Users/hao-cheng/Desktop/theorem proof/qcd_factorization_work/verify/extend/X3-ope/logs/f1_forward_graphs.log

### [files 3]
/Users/hao-cheng/Desktop/theorem proof/qcd_factorization_work/verify/extend/X3-ope/scripts/f2_triangle.py

### [files 4]
/Users/hao-cheng/Desktop/theorem proof/qcd_factorization_work/verify/extend/X3-ope/logs/f2_triangle.log

### [files 5]
/Users/hao-cheng/Desktop/theorem proof/qcd_factorization_work/verify/extend/X3-ope/scripts/h1_hadronic_checks.py

### [files 6]
/Users/hao-cheng/Desktop/theorem proof/qcd_factorization_work/verify/extend/X3-ope/logs/h1_hadronic_checks.log

### [files 7]
/Users/hao-cheng/Desktop/theorem proof/qcd_factorization_work/verify/extend/X3-ope/scripts/e1_ee_checks.py

### [files 8]
/Users/hao-cheng/Desktop/theorem proof/qcd_factorization_work/verify/extend/X3-ope/logs/e1_ee_checks.log

### [files 9]
/Users/hao-cheng/Desktop/theorem proof/qcd_factorization_work/research/c_dis/logs/ope_check_N8.log

### [files 10]
/Users/hao-cheng/Desktop/theorem proof/qcd_factorization_work/research/c_dis/logs/ope_check_N6.log

### [files 11]
/Users/hao-cheng/Desktop/theorem proof/qcd_factorization_work/research/c_dis/logs/ope_wilson_N6.log
