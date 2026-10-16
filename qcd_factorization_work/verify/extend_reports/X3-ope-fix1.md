# X3-ope-fix1

(extracted verbatim from the workflow journal; structured output of the agent)

## summary

**Status (answer to 在正常运行吗).** Only partly normal.
- The workflow is running. It resumed at 03:21 after the account session limit. X1 and X2 are in review round 2; X3 is in fix round 1 (this run).
- **Problem 1: report files are never written.** The harness forbids subagents to write report files. So `verify/extend/X{1,2,3}/REPORT.md` and every `review_r*_k.md` do not exist. Reports and reviews survive only as StructuredOutputs in the workflow journal (`~/.claude/projects/-Users-hao-cheng-Desktop-theorem-proof/c211c739-…/subagents/workflows/wf_52f29317-58b/journal.jsonl`).
- **What the parent should do.** This summary is the complete revised X3 report. Save it verbatim as `verify/extend/X3-ope/REPORT.md`: the round-2 reviewers will look for that file.
- **Problem 2: the first X3 fix agent died.** Agent a6200862df9da8ea1 finished its scripts, then hit "Output token limit hit" while emitting its final output, then hit the session limit. This rerun (aa6e04ae9a9fda375) reused and re-checked its scripts and downloads, and wrote the revisions below.
- All six X3 scripts reproduce their logs byte for byte.

# X3 (revised after review round 1): OPE in massless QCD; DIS and e⁺e⁻ moments at hadron level

Conventions are those of CONTEXT.md: metric (+,−,−,−), $D=4-2\varepsilon$, $\overline{\rm MS}$, $Q^2=-q^2$, $\nu=P\cdot q$, $\omega=2\nu/Q^2=1/x$, $a=\alpha_s/\pi$.

**Grades** (monograph tags, WRITER_SPEC_v2 §4.3):
- [R, R_PT]: complete proof here, perturbative, per graph or per order.
- [R, R_def]: algebra and definitions.
- [R]: pure mathematics with a complete proof.
- [R, R_cond: X]: complete proof given the numbered premises X. Its content grade is that of the weakest premise.
- [A]: all-order argument whose cited key step was not verified at theorem level.
- [C]: open.

How citations are qualified:
- "cited (checked)": I located the theorem in the full text and recorded its hypotheses.
- "cited (abstract)": I did not check the full text.
- The first version's tag "[R-cited]" is abolished (see REVISIONS).

**Scripts** (`verify/extend/X3-ope/scripts/` → `logs/`):
- f1: graph polynomials. Its sampling part is superseded by f3.
- f2: exact one-loop forward triangle.
- f3: matroid lemma F.6, with exact facet verification.
- f4: D-dimensional T₂ projector and Laurent cancellation (Lemma F.7).
- h1: hadronic lemmas.
- e1: e⁺e⁻ checks.
- Also used: `research/c_dis` logs ope_check_N6, ope_check_N8.
- The reviewers' independent checks are in `review_r1_1_checks/` and `review_r1_2_scripts/`.

## 0. Executive summary

**(i) The strongest OPE statement for massless QCD with quarks is Theorem I = A + B, overall grade [A].** It holds at every order of DR+$\overline{\rm MS}$ perturbation theory in Feynman gauge:
- **Expansion.** The large-$q$ expansion of $\langle T J J\,\Phi\rangle$ at Euclidean non-exceptional momenta has remainder $O(|q|^{1-a}\ln^k)$.
- **Coefficients.** They are unique, equal to $|q|^{2-d_O}$ times a polynomial in $\ln(q^2/\mu^2)$, equal to $C^{\rm bare}Z^{-1}$, and obey the RG equation.
- **Gauge structure.** $X_d$ is GI + $s$-exact + EOM.
- **Twist 2.** Only $O_q^{(n)}$ and $O_g^{(n)}$ appear.

**Why Theorem A stays [A].** Its key inputs (A1) and (A3) are cited, and the checked sources do not cover them as used here:
- **Smirnov CMP 134 (1990) 109, now read in full.** Its theorem proves the remainder estimate as a distribution, in analytic regularization. The function form at Euclidean momenta in DR is only asserted ("may easily be maintained"). The operator form of its §6 is derived from that theorem. Ghosts and gauge-variant bases are not treated.
- **Chetyrkin arXiv:1701.08627 (= MPI-PTh 13/91).** Thms 7–8 are stated with proofs "given elsewhere".
- **Gorishny NPB 319 (1989) 633 and Llewellyn Smith–de Vries NPB 296 (1988) 991.** I could not obtain them.

**Theorem B is [R, R_cond: E_ε], with content grade [A].** It reduces the BRST/GI reduction to:
- E_ε, the expansion with one composite spectator;
- exact DR identities;
- the cited local BRST cohomology, now located: BBH Phys. Rep. 338 §8.6 with Lemma 8.1 and Thm 7.1, Henneaux PLB 367 (1996) 163, and Barnich–Henneaux–Hurth–Skenderis PLB 492 (2000) 376, App.

I do not claim novelty for Theorem B: Joglekar, Ann. Phys. 109 (1977) 210, treats the same question at physicist's level (abstract checked).

**(ii) Euclidean versus forward kinematics.**
- **Theorem F, [R, R_PT] per graph, now unconditional.** The forward on-shell DR amplitude is holomorphic in the cut $\omega$-plane and equals its naive Taylor series in $p$. The former hypothesis (F-DR) is now proven (Lemma F.6, matroid base polytope), and projections onto $T_2$ are handled by Lemma F.7.
- **Corollary F.2, [A] (inherits A and B).** It gives the forward partonic OPE at every order. It reduces asm:appM-forward to (A3) + E_ε, with an explicit Cauchy-estimate remainder bound.
- **Hadronic side.** It needs exactly the segment approximation N1. There is no exceptional-momentum obstruction because $M>0$.

**(iii) Theorem M** (hadron-level DIS moments): unchanged, [R, R_cond: W, N1 (+N2, G, Φ)].

**(iv) e⁺e⁻, E1–E6:** unchanged. E5's novelty claim is dropped.

**Slot outcomes.**

| slot | outcome |
|---|---|
| X3a: discharge asm:appM-remainder by uniqueness | **FAILS** as planned. The argument is circular (Remark A.6). asm:appM-remainder stays [A] (open item O3). |
| X3b: prop:dis-ope-euclid → [R, R_PT] | **Not passed.** It stays [A] and D3 is unchanged (K2 below). |
| X3c: one-loop all-$N$ forward identity | **Not delivered.** The "[R] at one loop for all $n$" claim is withdrawn. c_dis covers $N\le 8$. |
| X3d: asm:appM-brst-ope | **Partial.** QCD: reduced to E_ε plus cited LBC by Theorem B, [R, R_cond: E_ε], content [A]. Pure YM: the Hollands 2008 §4.1.3 statement is located, but it lives in a different framework and was not verified. The proof plan of prop:dis-ope-gi must change from "$X_d$ classically BRST closed" to "$sX_d\in\mathcal E$". |
| X3e: thm:appM-forward-expansion | **PASS**, subject to round-2 confirmation. Theorem F with Lemmas F.6 and F.7, [R, R_PT] per graph. prop:dis-ope-forward stays [A]; its bottleneck is now A3 + E_ε instead of asm:appM-forward. |

## 1. Setup

- **D1.** SU($N_c$), $n_f$ massless Dirac quarks.
  - Gauge fixing $s(\bar c(\partial A+\xi B/2))$ at $\xi=1$, with $B$ kept off-shell.
  - $sA=Dc$, $s\psi=igc\psi$, $sc=-\frac g2[c,c]$, $s\bar c=B$, $sB=0$, $s^2=0$.
  - $[A]=[c]=[\bar c]=1$, $[\psi]=3/2$, $[B]=2$.
- **D2.** DR (with analytic regulators where stated) and $\overline{\rm MS}$, $[O]=Z_{OO'}O'_{\rm bare}$. There is no $\gamma_5$, so DR is exactly BRST-invariant.
- **D3.** Operator classes:
  - GI: colour-singlet polynomials in $F,\psi,\bar\psi,D$;
  - BRST-exact: $s\Lambda$;
  - EOM: the ideal $\mathcal E$ generated by $\delta S/\delta\phi$ for all $\phi\in\{A,\psi,\bar\psi,c,\bar c,B\}$ and their derivatives;
  - aliens = BRST-exact + EOM.
- **D4.** $\mathcal J^{\mu\nu}(q)=i\int d^Dx\,e^{iqx}TJ^\mu(x)J^\nu(0)$; it "counts as dimension 2".
- **D5.** Non-exceptional: no proper partial sum of the external momenta vanishes. Forward matrix elements are exceptional.
- **D6.** $T^{\mu\nu}=-\tilde g^{\mu\nu}T_1+\hat P^\mu\hat P^\nu T_2/\nu$ and $W^{\mu\nu}=-\tilde gF_1+\hat P\hat PF_2/\nu$, with $T_2=\sum_{n\,\rm even}t_n\omega^{n-1}$ and $M_2^{(n)}=\int_0^1x^{n-2}F_2$ (elastic point included). Free quark: $T_2=4e_q^2\omega/(1-\omega^2)$.
- **D7.** $O_q^{(n)},O_g^{(n)}$ symmetric traceless, $\langle P|O_i|P\rangle=2A_i(PP\cdots-{\rm tr})$.
- **D8.** $\mathcal I_Q=\{iy:|y|\le r_Q=\sqrt3M/Q\}$.
- **D9.** Naive Taylor expansion: $p\to\lambda p$, expand the integrand in λ.
- **D10.** Lee–Pomeransky representation $I\propto\int_{\mathbb R^N_+}\alpha^{a-1}\mathcal G^{-D/2}$ with $\mathcal G=\mathcal U+\mathcal F$. By Tarasov (1996), tensor integrals are scalar integrals in $D+2k$ dimensions with powers $a_e+\nu_e$, times polynomial tensors.

**Assumption register.**
- **E_ε** [A]. The DR large-$q$ expansion at fixed small generic ε for $\langle\mathcal J\Phi\rangle$ and for $\langle\mathcal J\,Z(p_Z)\Phi\rangle$, with one composite spectator $Z=s\phi$:
  $$\langle\mathcal J Z\Phi\rangle=\sum C_O\langle OZ\Phi\rangle+\sum C^Z_{O'}(q;p_Z)\langle O'\Phi\rangle+\mathcal R'.$$
  - The $C_O$ are the same as without $Z$.
  - $C^Z$ is polynomial in $p_Z$; it comes from hard subgraphs containing the $Z$ vertex.
  - All coefficients are graded-homogeneous.
  - This is K2 applied to graphs with a composite vertex, so it has the scope status of K2.
- **DR-WI, DR-SD.** Exact identities of bare DR Green functions (stated in Theorem B).
- **LBC.** Cited (checked), K6.
- **K3.** Joglekar–Lee triangularity.
- **Hadronic DIS:** W1–W3, N1, N1-std, N2, N3, G, Φ (§5).
- **e⁺e⁻:** V1–V3, V2′ (§6).

## 2. Literature (what was verified)

**K1. IR finiteness** (cited, abstract):
- Lowenstein–Zimmermann CMP 44 (1975) 73;
- Lowenstein CMP 47 (1976) 53;
- Breitenlohner–Maison CMP 52 (1977) 11, 39, 55: massless theories whose interactions all have IR degree Ω≥4. QCD in Feynman gauge has only Ω=4 vertices.
- Poggio–Quinn PRD 14 (1976) 578.

**K2. The DR/$\overline{\rm MS}$ OPE.**
- **Smirnov CMP 134 (1990) 109: full text read** (scratchpad copy `x3fix/dl_smirnov/s90.txt`).
  - §2: DR and analytic regularization defined through the α-representation, at non-exceptional Euclidean momenta, with MS subtraction.
  - §3: the diagrammatic expansion (3.4)–(3.7), a sum over asymptotically irreducible (AI) subgraphs via Zimmermann identities.
  - **The Theorem (p. 117)** states the required ρ-power estimate for the remainder of (3.7):
    - as a tempered distribution in ξ, and as a function of non-exceptional Euclidean small momenta;
    - for the analytic regularization parameter λ near 0.
    - The paper adds that "the corresponding estimate for Feynman integrals considered at non-exceptional momenta" "may easily be maintained". This is not written out.
  - §4: explicit finiteness via $R^*$ (Chetyrkin's equivalence, brief version).
  - §5: proof by α-parameters and sectors.
  - §6: operator expansions (6.10), and (6.11) in an arbitrary basis via MS $Z$-matrices. They "follow immediately" from the diagram theorem. Gauge theories are mentioned only in connection with the choice of basis.
  - **Not covered explicitly:**
    - uniformity in direction on compact $p$-sets;
    - the function form in DR at fixed ε;
    - ghosts and gauge-variant bases;
    - composite spectators (E_ε).
- **Chetyrkin arXiv:1701.08627 (= MPI-PTh 13/91), §5.** Thm 7 (form of the DR expansion) and Thm 8 (rearrangement over AI spinneys) are stated, with proofs "given elsewhere". The $R$ and $R^*$ forms are derived from them.
- **Gorishny 1989 and Llewellyn Smith–de Vries 1988:** not obtained (abstracts only).
- **Conclusion:** (A1), (A3) and E_ε remain [A].

**K3. Renormalization of GI operators** (abstracts):
- Joglekar–Lee Ann. Phys. 97 (1976) 160. A FNAL preprint exists: Pub-75-050-T.
- Kluberg-Stern–Zuber PRD 12 (1975) 467, 482, 3159. These treat the renormalization of GI operators, not the OPE.
- Henneaux PLB 313 (1993) 35.
- Collins–Scalise PRD 50 (1994) 4117.

**K4. Joglekar 1977** (abstracts; full texts not obtained):
- Ann. Phys. 108 (1977) 233, COO-2220-82: which local functionals have η-independent physical matrix elements.
- Ann. Phys. 109 (1977) 210, COO-2220-89: the OPE of two GI currents. Physical matrix elements of the gauge-variant operators "either vanish or cannot be isolated". This is the content of Theorem B at physicist's level.

**K5. Pure Yang–Mills.**
- **Hollands RMP 20 (2008) 1033 = arXiv:0705.3340v4, §4.1.3 (read).**
  - Statement: for $\hat s$-closed ghost-number-0 operators, the OPE coefficients vanish unless the operators on the right are $\hat s$-closed, and $\hat s$-exact if one factor is exact.
  - Framework: semisimple $G$ without abelian factors, no matter; Epstein–Glaser; the position-space OPE of Hollands CMP 273 (2007) 1.
  - The underlying construction of the interacting BRST charge was not verified.
- **Fröb–Holland arXiv:1603.08012:** a preprint; Thm 2 holds under $H^{1,4}_{E(4)}(\hat s|d)=0$.
- **FHH JMP 57 (2016) 122301.**

**K6. LBC (checked).**
- **BBH Phys. Rep. 338 (2000) 439 [hep-th/0002245]:**
  - Thm 7.1: $H^g(s)\simeq H^g_0(\gamma,H(\delta))$ on local forms;
  - Lemma 8.1 and §8.3: matter with first-order field equations, which includes Dirac quarks;
  - §8.6: at ghost number 0, the class-I gauge-invariant operators form a basis of $H^{0,*}(s,\Omega)$ (the setting of §8.4 covers $G={\rm SU}(N_c)$);
  - §2.6–2.7: the antighost/auxiliary pairs $(\bar c,B)$ are contractible, and the gauge-fixed cohomology is related in its refs [26, 136].
- **Henneaux PLB 367 (1996) 163 [hep-th/9510116], §3:** the gauge-fixed Koszul differential is acyclic in positive antifield number on local functions. The reconstruction theorems therefore hold for local functions; they fail for local functionals.
- **BHHS PLB 492 (2000) 376 [hep-th/9910201], Appendix:** for V = local functions, $H^g(s,V)\simeq H^g_0(\gamma_g,H(\delta_g,V))$ in gauge-fixed form.
- **Together these give LBC as used here:** if $X$ is a ghost-number-0 local polynomial with $sX\in\mathcal E$, then $X=\sum c_jO^{GI}_j+s\Lambda+E$ with $E\in\mathcal E$. The terms can be taken of the dimension and Lorentz type of $X$, because $s$ and $\mathcal E$ are homogeneous.

**K7.** Hollands–Kopper CMP 313 (2012) 257; Holland–Hollands–Kopper CMP 342 (2016) 385.

**K8. Euler–Mellin integrals and matroid polytopes.**
- Schultka arXiv:1806.01086 §3 (read):
  - Thm 3.1: absolute convergence iff ${\rm Re}\langle s,u_\rho\rangle>{\rm Re}\,c\,d_\rho$ for all facet normals, for coefficients in an open strongly convex cone and a full-dimensional polytope; no convergence otherwise.
  - Thm 3.6 = BFP Thm 2.4: continuation of the form $\Phi\prod_{\rm facets}\Gamma(\langle u_F,s\rangle-c\,d_F)$ with Φ entire.
  - Cor 3.8: Kaneko–Ueda cubes.
- Nilsson–Passare 2013; Berkesch–Forsgård–Passare Michigan Math. J. 63 (2014) 101; Kaneko–Ueda CPC 181 (2010) 1352.
- Feichtner–Sturmfels arXiv:math/0411260 (read):
  - Prop 2.3: $P_M=\{x\in\Delta:\ x(F)\le{\rm rank}(F)\ \forall$ flats $F\}$, with $\Delta=\{x\ge0,\ x(E)=r\}$;
  - Prop 2.4: $\dim P_M=|E|-c(M)$.

**K9. Tools:** Vladimirov (1979) §25–26; Reed–Simon II Thm IX.16; Hörmander ALPDO I §3.1 (Thm 3.1.15, boundary values in wedges); Feller II XIII.5; Korevaar 2004; Borwein–Erdélyi (Markov).

**K10.** c_ee Thm 5.1: Euclidean steps [R], cut identification [A].

**K11.** c_pdf §5 and §7.

## 3. Part I: Euclidean perturbative OPE

**Lemma A.3 (linear independence) [R, R_PT].**
- *Hypothesis.* $\sum_Oc_O(q)\tilde G_{[O];\Phi}(p)=O(|q|^\varrho\ln^k)$ for all strings Φ and all $p$ in an open non-exceptional set, at each order.
- *Conclusion.* $c_O=O(|q|^\varrho\ln^k)$. If moreover the $c_O$ are graded-homogeneous of degrees $>\varrho$, then $c_O\equiv0$. This holds also at fixed generic ε, where the loop-order-$j$ piece scales like $|q|^{\kappa-2j\varepsilon}$.

*Proof.* Induction in $g^2$.
1. At tree level, only operators whose fields match Φ contribute, through the vertex polynomial $V_O(p)$. The map from monomials to symmetrized polynomials is injective.
2. Lower orders are handled by induction.
3. Separate the distinct powers of $|q|$. ∎

(Known in spirit; reference Lemma C.30.)

**Theorem A (Euclidean OPE for $J^\mu J^\nu$, full $\overline{\rm MS}$ basis).** Hypotheses: D1–D2, fixed order $r$, integer $a\ge2$.
- **(A1)** $\tilde G^T_{JJ;\Phi}-\sum_{d_O\le a}C_O(q;\mu)\tilde G_{[O];\Phi}=O(|q|^{1-a}\ln^k|q|)$, uniformly in direction and on compact non-exceptional $p$-sets.
- **(A2)** $C_O=|q|^{2-d_O}\times$ a polynomial of degree $\le r$ in $\ln(q^2/\mu^2)$.
- **(A3)** $C^{\overline{\rm MS}}=C^{\rm bare}Z^{-1}$. Here $C^{\rm bare}$ is the sum over hard (AI) subgraphs of their DR Taylor coefficients, and it is finite after multiplying by $Z^{-1}$.
- **(A4)** Uniqueness.
- **(A5)** $(\mu\partial_\mu+\beta\partial_\alpha)C_i=\sum_jC_j\gamma_{ji}$.

*Proof.*
- **(A1), (A3).** Apply K2 graph by graph and in operator form (Smirnov 1990 §§3–6). Substitute $O_{\rm bare}=Z^{-1}[O]$. IR finiteness of $\tilde G_{[O]}$ follows from K1.
- **(A2).** At fixed ε a $k$-loop hard part is exactly homogeneous of degree $2-d_O-2k\varepsilon$. After coupling renormalization and $Z^{-1}$ one gets $|q|^{2-d_O}\sum_kc_k(\varepsilon)(\mu^2/q^2)^{k\varepsilon}$ with poles of order $\le r$. Finiteness forces a polynomial of degree $\le r$ in $L$.
- **(A4).** The difference of two solutions is $|q|^{2-d_O}P(L)=O(|q|^{1-a}\ln^k)$ by Lemma A.3, so $P=0$.
- **(A5) (argument completed).**
  - Let $\mathcal D=\mu\partial_\mu+\beta\partial_\alpha+\sum_{\rm legs}\gamma_\phi$. Then $\mathcal D\tilde G^T=0$ and $\mathcal D\tilde G_{[O_i]}=-\sum_j\gamma_{ij}\tilde G_{[O_j]}$.
  - Applying $\mathcal D$ to (A1) gives $\sum_i(\mathcal DC_i-\sum_jC_j\gamma_{ji})\tilde G_{[O_i]}=-\mathcal D\mathcal R$.
  - At each order in $\alpha_s(\mu)$, $\mathcal R$ is a polynomial of degree $\le K$ in $\ln\mu$ ($\overline{\rm MS}$).
  - Use (A1) at $K+1$ fixed values of μ. Lagrange interpolation bounds every coefficient of this polynomial by the same $O(|q|^{1-a}\ln^k)$. Hence $\mathcal D\mathcal R=O(|q|^{1-a}\ln^k)$ uniformly for μ in compacts; the $\beta\partial_\alpha$ term is treated order by order.
  - The bracket has the structure (A2), so it vanishes by (A4).
  - **Vacuum correlator** (Φ = ∅, Part IV): the identity operator appears, and its coefficient obeys an RG equation with an inhomogeneous term from the additive renormalization of $\langle JJ\rangle$. E2–E3 therefore use the RG-invariant Adler function. ∎

*Grade.*
- (A1), (A3): [A], cited (checked) for Smirnov 1990 with the scope limits listed in K2; the remaining sources are unchecked.
- (A2), (A4), (A5): [R, R_cond: (A1), (A3)].
- Theorem A overall: [A].
- The content is standard; only the assembly is mine. The reference's Thm C.35 cites the same sources.

**Remark A.6 (correction to CLAIMS R-M26; logic).**
- R-M26 claims that, by uniqueness, any proven momentum-space OPE discharges Ass. C.24. This is **circular**.
- The reason: lem:appM-uniqueness(a), applied to $\sum(\tilde C-C')G=\mathcal R'-\tilde N_a$, needs $\tilde N_a$ (the frozen-$q$ remainder) to be small, and that is C.24 itself.
- The DR route needs no C.24. For the frozen-$q$ BPHZ construction an identification lemma is required (O3).
- **Slot X3a therefore fails as planned.** The blocked first draft's statement "Prop A.6: C.24 follows from Smirnov + uniqueness" is **withdrawn**; it must not enter the spec.

**Theorem B (BRST reduction of the OPE coefficients).**

*Premises* (bare DR at fixed generic small ε, Feynman gauge, $B$ off-shell, no $\gamma_5$):
- **(DR-WI)** $sJ^\mu=0$. For local monomials $X_i$ at non-exceptional momenta,
  $$\sum_i(-1)^{|X_1|+\dots+|X_{i-1}|}\langle TX_1\cdots(sX_i)\cdots X_n\rangle=0$$
  exactly. This holds because the regularized action and measure are BRST-invariant ('t Hooft–Veltman 1972; Breitenlohner–Maison 1977).
- **(DR-SD)** With $\tilde\Phi=\prod_k\int d^Dx_k\,e^{ip_kx_k}\phi_k(x_k)$:
  $$\langle T(Y\cdot\partial^\alpha\delta_LS/\delta\phi)(y)\,\tilde\Phi\rangle=i\sum_{k:\phi_k=\phi}\epsilon_k\,(ip_k)^\alpha e^{ip_ky}\langle TY(y)\tilde\Phi_{\hat k}\rangle,\qquad \epsilon_k=(-1)^{|\phi|(|Y|+|\phi_1|+\dots+|\phi_{k-1}|)}.$$
  It follows from $\int\mathcal D\phi\,\frac{\delta_L}{\delta\phi(y)}[Y\Phi e^{iS}]=0$. The $\delta^{(D)}(0)$ terms vanish in DR.
- **(E_ε)** As in the assumption register; [A].
- **(LBC)** As in K6; cited (checked).

*Conclusion.*
- For every $d\le a$: $sX_d\in\mathcal E$, where $X_d=\sum_{d_O=d}C_OO$.
- Hence $X_d$ = GI + $s$-exact + EOM.
- With K3, $X_d=\sum c'_j[O_j^{GI}]$ + aliens, with $c'=cZ_{GG}^{-1}$ finite.
- The $\overline{\rm MS}$ coefficients of "rest" operators vanish.
- Between physical states only GI operators survive. At twist 2 these are $O_q^{(n)},O_g^{(n)}$ (reference Lemma C.42).

*Proof.*
1. **Ward identity.** $sJ=0$ and DR-WI give $\sum_k\epsilon'_k\langle\mathcal J\phi_1\cdots(s\phi_k)\cdots\phi_n\rangle=0$, with $\epsilon'_k=(-1)^{|\phi_1|+\dots+|\phi_{k-1}|}$.
2. **Non-merged parts.** Insert E_ε (with $Z=s\phi_k$ at $p_k$). Since $O$ is bosonic of ghost number 0, DR-WI turns the non-merged parts into $\sum_OC_O\sum_k\epsilon'_k\langle O\cdots s\phi_k\cdots\rangle=-\sum_OC_O\langle(sO)\Phi\rangle$.
3. **Merged parts.** They give $M_\Phi=\sum_k\pm\sum_{O'}C^{s\phi_k}_{O'}(q;p_k)\langle O'\Phi_{\hat k}\rangle$.
   - Moving $Z_k$ (parity $|\phi_k|+1$) next to $\mathcal J$ costs $(-1)^{(|\phi_k|+1)(|\phi_1|+\dots+|\phi_{k-1}|)}$. Combined with $\epsilon'_k$, the $k$-dependent sign is $(-1)^{|\phi_k|\sum_{l<k}|\phi_l|}$. This is $\epsilon_k$ of DR-SD up to the $k$-independent factor $(-1)^{|\phi||O'|}$.
   - $C^{s\phi_k}$ depends on $k$ only through the field type and $p_k$, and $C(q;-i\partial_y)e^{ipy}=C(q;p)e^{ipy}$.
   - Therefore DR-SD gives $M_\Phi=\langle\mathbb E(q)\Phi\rangle$ for the EOM operator
     $$\mathbb E(q)=-i\sum_\phi\sum_{O'}(-1)^{|\phi||O'|}\,O'\cdot C^{s\phi}_{O'}(q;-i\partial)\,\delta_LS/\delta\phi,$$
     where $-i\partial$ acts on the EOM factor.
4. **Combined identity.** $\langle[-\sum_OC_O\,sO+\mathbb E(q)]\Phi\rangle=O(|q|^{1-a}\ln^k)$ for every Φ.
5. **Degree matching.**
   - Write $-\sum C_O\,sO+\mathbb E=\sum_YK_Y(q)Y$ over a monomial basis $\{Y\}$ of ghost number 1.
   - Since $\mathcal J$ counts as dimension 2 and $s$ raises dimension by 1, $K_Y$ is graded-homogeneous: its loop-order-$j$ part is $\propto|q|^{3-d_Y-2j\varepsilon}$.
   - Truncate consistently: all $O$ with $d_O\le a$, and all merged terms with $d_Y\le a+1$.
   - Lemma A.3 at fixed ε (the powers $|q|^{-2j\varepsilon}$ are distinct for generic ε) gives $K_Y=O(|q|^{1-a}\ln^k)$.
   - Since $3-d_Y-2j\varepsilon>1-a$ for $d_Y\le a+1$ and small $|\varepsilon|$, $K_Y\equiv0$.
   - Hence $\sum_{d_O=d}C_O\,sO=\mathbb E_{d+1}\in\mathcal E$ for each $d\le a$.
6. **LBC.** Apply LBC to each loop-order coefficient (q-dependent c-number tensors times operators): $X_d$ = GI + $s\Lambda$ + $E$.
7. **Physical states.** EOM operators vanish on shell. $\langle s\Lambda\rangle$ vanishes between physical states (Kugo–Ojima). For partons at tree level this is direct: $B$ legs give $p\cdot\varepsilon=0$, and there are no ghosts. ∎

*Grade and status.*
- **Grade:** [R, R_cond: E_ε], with premises DR-WI and DR-SD (standard) and LBC (cited, checked). Content grade [A].
- **Novelty:** not claimed (K4: Joglekar 1977 II treats the same question at physicist's level). The literature check is incomplete (Joglekar I/II and Collins 1984 §12.8 full texts not obtained).
- **Correction to the reference's Prop C.44.**
  - The second identity of (B1), $\langle T\tilde T\,s\Phi\rangle$ = polynomial, is trivially true in DR, because the left side vanishes (step 1).
  - The defect is in (B2) and the proof of C.44. They expand $\langle T\tilde T\phi_1\cdots(s\phi_k)\cdots\phi_n\rangle$ with only the terms $C_O\langle O\cdots\rangle$, and omit the merged terms (hard subgraphs that contain the nonlinear vertex $s\phi_k$).
  - With the merged terms included, the proof yields $sX_d\in\mathcal E$, not "$sX_d=0$ classically". The latter is not established, and the physical conclusion survives through LBC.
  - The spec's prop:dis-ope-gi plan must be corrected accordingly. asm:appM-brst-ope can be replaced by E_ε + LBC.
- **WITHDRAWN:** the first version's claim that the polynomial contact terms of (B1) are "in general false" and carry logarithms. I make no claim about the $q$-dependence of $C^{s\phi}$ beyond graded homogeneity, and Theorem B does not need one.

**Theorem I = Theorem A + Theorem B + twist classification. [A].** The statement is that of §0(i).

**Gap analysis: four routes.**
1. **DR + Theorem B.** Complete modulo (A1), (A3) and E_ε at theorem level (O1).
2. **BPHZL.** Convergence is known (K1), but there is no C.24-type remainder estimate.
3. **Flow equations (FHH/FH).** Rigorous for pure YM. QCD needs FHH with Dirac fermions (O2); the anomaly condition already holds by parity.
4. **Hollands 2008.** Pure YM only, in the Epstein–Glaser framework.

**What is exactly missing for QCD with quarks:** theorem-level verification of (A1), (A3) and E_ε for a gauge theory with ghosts and a composite spectator.

## 4. Part II: from Euclidean to forward kinematics

**Lemma F.0 (forward 2-forest structure) [R, R_PT]; elementary, no novelty claimed.**
- *Setting.* A connected graph with incoming $p$ at $P_1$, $-p$ at $P_2$, $q$ at $J_1$, $-q$ at $J_2$ ($J_1\ne J_2$; other vertices may coincide), and $p^2=0$.
- *Statement.*
  $$\mathcal F=Q^2(\hat F_0+\omega\hat F_1),\qquad \hat F_0=\sum_{T:\,c_q\ne0}\alpha^{E\setminus T},\qquad \hat F_1=-\sum_Tc_pc_q\,\alpha^{E\setminus T},\qquad c_p,c_q\in\{0,\pm1\}.$$
  Hence ${\rm mon}(\hat F_1)\subset{\rm mon}(\hat F_0)$, with $|{\rm coef}|\le1$.
- *Proof.* $-s=Q^2(c_q^2-c_pc_q\omega)$, and a monomial determines its 2-forest. ∎

f1's random tests (C1), (C4) hold identically by this lemma and add no evidence.

**Lemma F.1 (Newton-polytope domination) [R]; proof here, tools standard.**
- *Setting.* $\mathcal G_\lambda=\mathcal U+\hat F_0+\lambda\hat F_1$, where $\mathcal U,\hat F_0$ have positive coefficients, ${\rm mon}(\hat F_1)\subset{\rm mon}(\hat F_0)$ and $|{\rm coef}_1|\le{\rm coef}_0$. Let $g$ be polynomial, $P={\rm Newt}(\mathcal U+\hat F_0)$ full-dimensional, and $|\lambda|\le r<1$.
- **(a)** $I(\lambda)=\int\alpha^{s-1}g\,\mathcal G_\lambda^{-c}$ and all Taylor-term integrals $I_n$ (numerator $g\hat F_1^n$, exponent $c+n$) converge absolutely on a common nonempty open set Λ.
- **(b)** $I(\lambda)=\sum\lambda^nI_n$ on Λ.
- **(c)** The meromorphic continuations have λ-independent candidate polar hyperplanes. $I$ is holomorphic in λ, and $\frac1{n!}\partial^n_\lambda I|_0=I_n$.

*Proof.*
- (a) The coefficients $c_m(1+\lambda\theta_m)$ lie in $|\arg|\le\arcsin r$, and Newt is unchanged; apply Schultka Thm 3.1. For the Taylor terms, $s+m\in c\,{\rm int}P+nP\subset(c+n){\rm int}P$.
- (b) $\sum|\binom{-c}{n}|r^n\le(1-r)^{-|c|}$ and $|\hat F_1|\le\hat F_0\le\mathcal G_0$; then Tonelli–Fubini.
- (c) On Kaneko–Ueda cubes, $\mathcal G_\lambda=x^{m_\sigma}f_{\sigma,\lambda}$ with $f_{\sigma,1}$ polynomial and ${\rm Re}\,f_{\sigma,\lambda}\ge(1-r)f_{\sigma,0}>0$. Gel'fand–Shilov continuation and the identity theorem finish the proof. ∎

**Lemma F.6 (matroid structure of ${\rm Newt}(\mathcal U+\hat F_0)$; discharge of (F-DR)) [R].** New in this report (not in the first version); the tools are standard.
- *Setting.* $G$ as in Lemma F.0, with $N$ lines and $L$ loops. Let $G_0=G+e_q$, where $e_q$ is a virtual line $J_1J_2$, and $E_0=E\cup\{e_q\}$.

- **(a) Support.**
  - $\hat F_0=\mathcal U(G/\{J_1{=}J_2\})$. By deletion–contraction on $e_q$, $\mathcal U(G_0)=x_q\,\mathcal U(G)+\mathcal U(G/\{J_1{=}J_2\})$. All coefficients of $\mathcal U$ and $\hat F_0$ equal 1.
  - Hence ${\rm supp}(\mathcal U+\hat F_0)=\pi(\mathfrak B)$, where $\mathfrak B$ is the set of indicator vectors of the bases of the cographic matroid $M^*(G_0)$ (complements of spanning trees), and π drops $x_q$.
  - π is an affine bijection from the hyperplane $x(E_0)=L+1$ onto $\mathbb R^N$, with inverse $x_q=L+1-\sum_Ex_e$.
  - So ${\rm Newt}(\mathcal U+\hat F_0)\cong P(M^*(G_0))$.
- **(b) Dimension.** $\dim=N+1-c(M(G_0))$ (Feichtner–Sturmfels Prop 2.4; $c(M^*)=c(M)$). So Newt is full-dimensional iff $M(G_0)$ is connected, i.e. iff $G_0$ is loopless and 2-connected (Whitney).
- **(c) Facets.** If Newt is full-dimensional, every facet has primitive inward normal $u$ and $d_u=\min\langle u,\cdot\rangle$ of one of four types:
  - $u=e_e$, with $d_u=0$ (coordinate facet);
  - $u=-\mathbb 1$, with $d_u=-(L+1)$ (from $x_q\ge0$);
  - $u=-\mathbb 1_F$, where $F$ is a flat of $M^*(G_0)$ with $e_q\notin F$, with $d_u=-r^*(F)\le-1$ (since $G_0$ has no bridges);
  - $u=\mathbb 1_{E\setminus F'}$, where $F'\cup\{e_q\}$ is a proper flat, with $d_u=L+1-r^*(F'\cup\{e_q\})\ge1$.

  This follows from FS Prop 2.3 ($P_M=\{x\ge0,\ x(E_0)=L+1,\ x(F)\le r^*(F)\}$, with $r^*(E_0)=L+1$) and the fact that every facet of a polyhedron is cut out by one of its defining inequalities, mapped through π. **In particular $d_u=0$ only for coordinate facets.**
- **(d) Strong (F-DR).** Take any graph with full-dimensional Newt, any line powers with ${\rm Re}\,a_e>0$, any polynomial numerator, and any dimension shift $D\to D+2k$ (Tarasov). Then:
  - every naive Taylor term $I_n$, and the amplitude $I(\omega)$ for every ω in the cut plane $\mathcal C$, is a meromorphic function of $D$ with isolated poles;
  - the only $D$-independent candidate polar hyperplanes are $a_e\in-\mathbb N_0$, which never meet ${\rm Re}\,a_e>0$.

*Proof of (d).* Use Schultka Thm 3.6 (= BFP Thm 2.4), which holds under Schultka's standing assumption (§3) that the coefficients lie in an open strongly convex cone. This assumption holds for $\mathcal G_\omega$ for every $\omega\in\mathcal C$: for real $|\omega|<1$ all coefficients are positive, and for ${\rm Im}\,\omega\ne0$ the coefficients $\{1,1\pm\omega\}$ lie in an open half-plane.
1. **Form of the continuation.**
   $$\int\alpha^{s-1}g\,\mathcal G_\omega^{-c}=\Phi(s,c)\prod_F\Gamma\big(\langle u_F,s\rangle-c\,d_F+d_F(g)\big),$$
   with Φ entire. The product runs over the facets $F$ of the common polytope $P$.
2. **Taylor terms.** The same holds for every Taylor term $I_n$: replace $g$ by $g\hat F_1^n$, $c$ by $c+n$, and use $\mathcal G_0$.
3. **Only coordinate facets are $D$-independent.** The candidate poles lie on $\langle u_F,s\rangle-c\,d_F+d_F(\cdot)\in-\mathbb N_0$. With $c=D/2$, by (c) these depend on $D$ unless $u_F=e_e$. On a coordinate facet the condition reads $a_e+d_{e}(\cdot)\in-\mathbb N_0$ with $d_e(\cdot)\ge0$, which is impossible for ${\rm Re}\,a_e>0$.
4. **Consistency.** These continuations agree with the continuation in ω of Theorem F (F1), because both continue the same absolutely convergent integral. ∎

*Checks.*
- f3 verifies exactly, on the 21 explicit QCD topologies and on 1028 random multigraphs (129 of them full-dimensional), with 0 failures:
  - the identities in (a);
  - the support bijection;
  - the dimension formula and its criterion;
  - that every facet is of matroid type with the stated $d_u$, using exact integer normals and exact tight-set rank;
  - that $d_u=0$ only for coordinate facets.
- The reviewers' independent checks agree: r1 (116/116 graphs), r2 (45/45), rv2_matroid (226/226), rv2_facets_d0* (185 + 68 graphs).
- *Supersedes* the sampling classification of degenerate graphs in f1.

**Theorem F (forward on-shell DR amplitude) [R, R_PT] per graph.**

*Setting.* Let Γ be a connected graph of the amputated forward amplitude of a massless on-shell parton $j$ ($p^2=0$) with the two currents.

*Exclusions:*
- **(i) Bridges carrying ±p.** These graphs are external-leg corrections. They are excluded by amputation; the on-shell massless self-energy is scaleless, so the LSZ factor is 1 in DR.
- **(ii) Bridges carrying exactly 0.** The target-side part is then a subgraph with a single adjoint index (only a gluon line can carry it, by fermion and ghost number). After colour averaging over the target it is an invariant tensor with one adjoint index, which is zero ($\mathrm{Tr}\,t^a=0$, $f^{abb}=0$).

*Definition.* The DR amplitude is the parametric (Lee–Pomeransky/Speer-type), analytically regularized integral at $p^2=0$.
- For real $|\omega|<1$ and $Q^2>0$, all coefficients of $\mathcal G_\omega$ are positive, by Lemma F.0. There it coincides with the Feynman-$i\epsilon$ momentum integral: $\mathcal F>0$ on the positive orthant, so Wick rotation is legitimate.
- For other ω it is defined by the continuation in (F1).

*Components.* Any tensor component contracted with tensors polynomial in $p$. Finite combinations with $\nu^{-k}$ prefactors (projectors, physical gluon polarization sums) are treated in Lemma F.7.

*Claims.*
- **(F1)** For ω in $\mathcal C=\mathbb C\setminus((-\infty,-1]\cup[1,\infty))$, the regularized integral converges on an ω-independent nonempty open set. It continues meromorphically with ω-independent candidate poles and is holomorphic in ω. Every DR Laurent coefficient is holomorphic on $\mathcal C$.
- **(F2)** For $|\omega|<1$, each Laurent coefficient equals $\sum_n\omega^nI_n^{[k]}$, where $I_n$ is the DR integral of the $n$-th naive Taylor term. The series converges absolutely and locally uniformly.
- **(F3)** If Newt is not full-dimensional ($G_0$ not 2-connected or not loopless), both sides are scaleless and hence zero.
- (F-DR), formerly a hypothesis, is Lemma F.6(d).

*Proof.*
- Tarasov reduction gives LP integrals with prefactors polynomial in $\lambda p$.
- By Lemma F.0, $\mathcal G_\omega=\mathcal U+Q^2(\hat F_0+\omega\hat F_1)$.
- For ${\rm Im}\,\omega\ne0$ the coefficients $\{1,1\pm\omega\}$ lie in an open half-plane; for real $|\omega|<1$ they are positive. So Newt is unchanged and Schultka Thm 3.1 applies.
- Joint holomorphy follows from Kaneko–Ueda cubes on compact subsets of $\mathcal C$.
- (F2): rescale λ and apply Lemma F.1. The parametric Taylor terms equal the parametric forms of the naive momentum-space terms pointwise in α (Schwinger + Gaussian). Restrict to DR by Lemma F.6(d).
- (F3): a degenerate Newt is invariant under a scaling $t^u$, and so are the Taylor terms, because ${\rm mon}\hat F_1\subset{\rm mon}\hat F_0$. ∎

*Status.* This is the book's rigorous proof (本书给出的严格证明) of the method of projectors, which the literature uses without proof:
- Gorishny–Larin–Tkachov PLB 124 (1983) 217;
- Gorishny–Larin NPB 283 (1987) 452;
- Larin–van Ritbergen–Vermaseren NPB 427 (1994) 41;
- Larin–Nogueira–van Ritbergen–Vermaseren NPB 492 (1997) 338, around Eq. (29), which says the method "implicitly involves a considerable rearrangement of infrared and ultraviolet divergences".

Related rigorous work, none of which covers this case:
- Semenova–Smirnov–Smirnov EPJC 79 (2019) 136: positive coefficients, asymptotic expansions only;
- Jantzen JHEP 12 (2011) 076;
- Schultka 2018; BFP 2014.

A 「本书新结果」 marker still requires the second literature check of WRITER_SPEC_v2 §6.5: Tkachov 1992–97 and Smirnov's books. (Chetyrkin 1701.08627 §5 was checked: it treats Euclidean large-momentum/mass limits only.)

**Lemma F.7 (projection onto $T_2$ in D dimensions) [R, R_PT].**
- *Setting.* $T^{\mu\nu}$ is the sum of forward graphs at fixed order and Laurent order, after the target spin sum.
  - Quark: $\frac12\not p$, polynomial in $p$.
  - Gluon: average with $d_{ab}(p,q)/(D-2)$, where $d_{ab}=-g_{ab}+(p_aq_b+q_ap_b)/\nu-q^2p_ap_b/\nu^2$. This tensor satisfies $d\cdot p=d\cdot q=0$, has trace $-(D-2)$, and is homogeneous of degree 0 in $p$ (f4 d).
- **(a) Projector.** $T$ lies in ${\rm span}\{g,pp,pq,qp,qq\}$ (no $\gamma_5$, parity). It is transverse, $q_\mu T^{\mu\nu}=T^{\mu\nu}q_\nu=0$: this is the abelian Ward identity of the EM current with amputated on-shell partons, exact in DR. For such tensors
  $$T_2=\nu B=\frac{Q^4\,[(D-1)S_1-(\nu^2/Q^2)S_2]}{(D-2)\,\nu^3},\qquad S_1=p_\mu p_\nu T^{\mu\nu},\quad S_2=g_{\mu\nu}T^{\mu\nu}$$
  (f4 a). In $D=4$ this is $Q^4(3S_1-(\nu^2/Q^2)S_2)/(2\nu^3)$. Equivalently, $\nu[(D-1)\hat P\hat PT-\hat P^2gT]/((D-2)(\hat P^2)^2)$ with $\hat P^2=\omega^2Q^2/4$.
- **(b) Quark target.** Theorem F applies to $S_1,S_2$, so they are holomorphic on $\mathcal C$ and equal their naive series.
  - The $n$-th naive term of $T$ is a transverse covariant tensor that is a homogeneous polynomial of degree $n$ in $p$. Transversality of each term follows from $q_\mu T^{\mu\nu}(\lambda p)=0$ for all small λ.
  - For such tensors the projector gives $\beta_n\nu^{n-1}$, with $\beta_n=0$ for $n<2$ (f4 b, $n\le8$, symbolic in $D$; the general case is the same linear algebra).
  - Hence the $\omega^{-3},\dots,\omega^0$ terms of the projector formula cancel identically. $T_2$ is holomorphic on $\mathcal C$, odd, $O(\omega)$, and its Taylor series is the naive series.
- **(c) Gluon target.** $T=H_0+H_1/\nu+H_2/\nu^2$, where each $H_k$ is $M^{\mu\nu,ab}$ contracted with $p$-polynomial tensors, and Theorem F applies to each $H_k$.
  - Hence $T_1,T_2$ are meromorphic on $\mathcal C$ and holomorphic on $\mathcal C\setminus\{0\}$, with at most a finite-order pole at ω=0.
  - Their Laurent expansions at 0 are the termwise naive expansions.
  - Regularity at 0 is proven in Corollary F.2.
- f4 (c) checks the tree level in $D$ dimensions: $T_2=4\omega/(1-\omega^2)$ and $T_1=2\omega^2/(1-\omega^2)$, independently of $D$, and transverse. ∎

**Corollary F.2 (forward partonic OPE at every order) [A]** (inherits A3 and Theorem B).
- *Premises.* Theorem F, Lemmas F.6–F.7 [R, R_PT]; Theorem A (A3) [A]; Theorem B [A]; K3; twist classification.
- **(a)** At every order in $\alpha_s(\mu)$ and every Laurent order, for $|\omega|<1$ (absolutely convergent):
  $$T^{\mu\nu}_j=\sum_OC^{\mu\nu}_O(q;\mu)\langle j(p)|[O]_\mu|j(p)\rangle.$$
  - Only twist-2 GI operators contribute.
  - $A^{(n)}_{i/j}=\sum Z\cdot{\rm tree}$ = tree + pure poles.
  - In particular $T_2^{(j)}=4\sum_{n\,\rm even}\omega^{n-1}\sum_iC^{(n)}_{2,i}A^{(n)}_{i/j}$, including gluons ($T_2^{(g)}$ is regular at ω=0).
- **(b) The asm:appM-forward bound, derived.** For every $N$ there are $C,k$ such that, for all Euclidean $q$ with $|q|\ge4\sqrt2\,p^0$, uniformly in the direction (not only when $2p\cdot\hat q$ is imaginary),
  $$\Big|T^{\mu\nu}_j-\sum_{d_O\le N}C^{\mu\nu}_O\langle j|[O]|j\rangle\Big|\le C|q|^{1-N}(1+\ln|q|)^k.$$

*Proof.*
1. **Graphs.** The forward graphs are exactly the AI two-leg hard graphs: a non-AI graph has a bridge carrying 0 or ±p, which is excluded by Theorem F (i), (ii).
2. **Naive terms.** By Theorem F (and Lemma F.7 for the spin sums), the sum of naive terms is $\sum_OC^{\rm bare}_OV_O(p,-p)$, contracted with the spin-sum tensor. On-shell loop matrix elements are scaleless, so the bare matrix elements equal the trees.
3. **Renormalization.** $C^{\rm bare}=C^{\overline{\rm MS}}Z$. Theorem B and K3 give $C^{\overline{\rm MS}}_{\rm rest}=0$. Joglekar–Lee: GI mixes only into GI + aliens, and aliens mix only into aliens.
4. **Aliens.** Their contracted tree vertices vanish:
   - EOM vertices are ∝ $p^2$ or $p_a$;
   - BRST-exact vertices have $B$ legs ∝ $p_a$, and $d_{ab}p^b=0$;
   - there are no external ghosts.
5. **GI operators and gluon regularity.** The two-gluon tree vertices of GI operators are built from linearized field strengths, so they are transverse in each leg. The gauge terms of $d$ drop out, and $d_{ab}V^{ab}_O=-g_{ab}V^{ab}_O$ is polynomial in $p$. So every naive term of $T_j$, gluons included, is a polynomial transverse tensor, and Lemma F.7(b) gives regularity of $T_2^{(g)}$ at 0.
6. **Twist.** With $p^2=0$, only twist 2 contributes, and the coefficients are finite by (A3).
7. **The bound (b).**
   - $|\omega|\le2|p\cdot q|/|q|^2\le2\sqrt2p^0/|q|\le\frac12$.
   - At fixed order, $T_{1,2}=\sum_{k\le K}\ln^k(Q^2/\mu^2)\tau_k(\omega)$ with $\tau_k$ holomorphic on $|\omega|<1$. Cauchy on $|\omega|=3/4$ bounds the $\omega^m$ coefficient by $\max_{|\omega|=3/4}|\tau_k|(4/3)^m$.
   - The spin-$n$ operator contributes $\omega^n$ to $T_1$ and $\omega^{n-1}$ to $T_2$, and $d_O\le N$ means $n\le N-2$. So the tails are $O(\ln^K|q|\cdot|\omega|^{N-1})$ for $T_1$, and $O(\ln^K|q|\cdot|\omega|^{N-3})$ for $T_2/\omega$.
   - $T^{\mu\nu}=-\tilde gT_1+2\hat P\hat P(T_2/\omega)/Q^2$ with $|\hat P|\le3p^0$. This gives $|q|^{1-N}$. ∎

*Status.*
- asm:appM-forward is **reduced** to (A3) + E_ε, not discharged; prop:dis-ope-forward stays [A].
- One-loop instance (c_dis ope_check, exact in ε): $N\le8$ for quarks, even $N\le8$ for gluons; MS-bar coefficients (ope_wilson) for $N\le6$.

**Corollary F.3 (perturbative cut-plane structure).**
- **(a) [R, R_PT].** Each Laurent coefficient of the partonic $T_2^{(j)}$ is holomorphic on $\mathcal C$. Quarks: Lemma F.7(b). Gluons: on $\mathcal C\setminus\{0\}$, and on $\mathcal C$ given Corollary F.2.
- **(b) [A].** ${\rm Disc}\,T_2^{(j)}=4\pi iF_2^{(j)}(1/\omega)$, with $F_2^{(j)}$ the cut-diagram structure function. This needs the DR cutting rules for Laurent coefficients, including the distributions at $x=1$, which is the status of K10's cut identification. If $F_2^{(j)}$ is defined as ${\rm Disc}/(4\pi i)$, (b) becomes a definition.
- **(c) [A].** $t_n=4\int x^{n-2}F_2^{(j)}$ for even $n>A+1$ needs fixed-order growth bounds (O4).
- c_dis verifies $t_N=4\int x^{N-2}F_2$ at one loop for $N\le8$ by computing both sides independently; this is [R, R_PT] for those $N$ only.
- **WITHDRAWN:** "at one loop it holds for all $n\ge1$ [R]". Slot X3c is not delivered (O4′).

**Example F.3 (one-loop triangle) [R, R_PT].**
- Lines $k$ ($a_3$), $k+q$ ($a_2$), $k-p$ ($a_1$):
  $$I=\frac{\Gamma(a-\frac D2)}{\prod\Gamma(a_i)}(Q^2)^{\frac D2-a}B(\tfrac D2-a_2,\tfrac D2-a_1-a_3)\,B(a_1,a_3)\;{}_2F_1(a-\tfrac D2,a_1;a_1+a_3;\omega).$$
- The $\omega^n$ coefficient equals the naive term identically in $(a_i,D)$ (sympy ratio = 1).
- Quadrature at three real points: one point agrees only to $1.2\times10^{-5}$, because of the endpoint singularity $(1-y)^{-0.8}$ (tolerance $2\times10^{-5}$). An exact-$y$ evaluation agrees to $10^{-12}$. Complex points: review r3.
- At $a_i=1$: each term has the pole $-1/((n+1)\varepsilon)$.

**Example F.4 (non-uniformity) [R, R_PT].**
- With $p^2=-P^2$, ω=0, $D=4$: $Q^2I=\ln(Q^2/P^2)+2+O(P^2\ln)$.
- So the off-shell matrix element diverges as $P^2\to0$, while the hard coefficient is unchanged. The on-shell DR value is the pure pole $-c_\Gamma(Q^2)^{-1-\varepsilon}/\varepsilon$. Theorem F avoids the limit.

**Remark F.5 [A] (reworded).**
- Zero-momentum insertions of $O^{(n)}$, $n\ge2$ (IR degree $n+2\ge4$), into 2-point functions at $p^2<0$ are expected to be IR finite to all orders by BM II.
- The hypotheses of BM II for composite insertions at exceptional momenta were not checked (O10).
- This indicates, but does not settle, the open question of the reference's Rem C.37 in DR.

**Lemma 4.10 (hadronic side; logic).**
- Beyond W1–W3, the hadron-level theorem uses only the segment approximation SA = N1 on $\mathcal I_Q$.
- No perturbative statement implies SA, which concerns non-perturbative target states.
- There is no exceptional-momentum obstruction ($M>0$).
- Corollary F.2 is the perturbative counterpart: the IR poles of $A_{i/j}$ play the role of the non-perturbative matrix elements.

## 5. Part III: hadron-level DIS (essentially unchanged; one proof step made explicit)

**Assumptions.**
- **W1.** Wightman framework: Hilbert space, positive-energy representation, unique vacuum. $J^\mu$ is hermitian, local, covariant, conserved and tempered. Parity holds.
- **W2 (corrects ERR-M25).** The target is a stable spin-½ particle of mass $M$ in the superselection sector $\mathcal H_T$ of its flavour numbers, with ${\rm spec}(P)|_{\mathcal H_T}\subset\{p^2=M^2\}\cup\{p^2\ge M_1^2\}$, $M_1>M$. This needs $m_\pi>0$. Only ${\rm spec}\subset\{p^2\ge M^2\}$ is used.
- **W3.** The spin-averaged connected forward commutator is tempered. It has a retarded part $R$ with:
  - support in $\bar V_+$ and $R-A=C$;
  - crossing $A^{\mu\nu}(z)=R^{\nu\mu}(-z)$;
  - covariance and parity;
  - $q_\mu\tilde R^{\mu\nu}=0$.
  - Freedom: polynomials in $q$.
- **N1 (segment approximation SA, for a given even $n$).** There are $N\ge\max(n+3,n_0+2)$ and constants $Q_0,K,k$ such that for $Q\ge Q_0$ some odd $P_N=\sum_{m\le N-2,\ \rm even}\pi_m\omega^{m-1}$ satisfies:
  - (a) $\sup_{\mathcal I_Q}|T_2-P_N|\le K(M/Q)^{N-2}\ln^kQ$;
  - (b) $|\pi_m|\le K\ln^kQ$;
  - (c) $\pi_n=4\sum_iC^{(n)}_{2,i}A^{(n)}_i+O((M^2+mM)Q^{-2}\ln^k)$.
- **N1-std (standard non-perturbative OPE).** On Euclidean $q$, $T=\sum_{d_j\le N}\tilde C_j\langle P|O_j|P\rangle+O(|q|^{1-N}\ln^k)$, where:
  - the coefficients are covariant with $|\tilde C_j|\le K|q|^{2-d_j}\ln^k$;
  - finitely many operators appear up to each dimension;
  - twist ≥ 2, and twist 2 is spanned by $O_q,O_g$;
  - odd-twist coefficients are $\le Km|q|^{1-d}\ln^k$ (chiral suppression).
- **N2.** Twist-2 RG with $\gamma^{(n)}$ asymptotic to $\overline{\rm MS}$, $\beta=-b\alpha^2(1+o(1))$ with $b>0$, and $C^{(n)}_{2,i}(1,\alpha_s(Q))$ asymptotic to $\overline{\rm MS}$ perturbation theory.
- **N3.** PDFs exist.
- **G.** $\lim_{y\to\infty}T_2(iy)/(iy)=0$.
- **Φ.** $x$-space measures with the twist-2 moments exist.

**Lemma 5.1 [R, R_def].** $\hat P^2=M^2\mathbf q^2/Q^2\ge M^2/4$, and $\omega=2iMq^4/Q^2$ covers $\mathcal I_Q$ (h1 c).

**Lemma 5.2 [R, R_cond: N1-std].** N1-std implies SA for all $N$.
- Transversalize with $\Pi=g-qq/q^2$.
- Write $T_2=\sum_j\nu b_j+\Pi_2(\Pi\mathcal R_N\Pi)$, where $\Pi_2=\nu(3PP-\hat P^2g)/(2(\hat P^2)^2)$ and $|\Pi_2|\le CQ/M$ on $\mathcal I_Q$ (h1: 6.06).
- $\nu b_j$ has size $(M/Q)^{t-2+2b}\omega^{r-1-2b}$.
- Contributions:
  - twist 2: the leading term;
  - trace terms: $M^2/Q^2$;
  - twist 3 with chiral suppression: $mM/Q^2$;
  - twist ≥ 4: $M^2/Q^2$.
- Without chiral suppression the error is $O(M/Q)$.

**Lemma 5.3 (Markov) [R].** For odd $h$ of degree $\le D_g$: $|h_k|r^k\le2(1+\sqrt2)^{D_g}\sup_{|y|\le r}|h(iy)|$ (h1 h).

**Lemma 5.4 (Jensen) [R].** If $f$ is entire and $|f|\le C(1+|z|)^A|{\rm Im}\,z|^{-B}$, then $f$ is a polynomial of degree $\le A$.
- Subharmonic averages over circles of radius 2.
- $J(y)=\frac1{2\pi}\int\log|y+2\sin\theta|=\log\max(1,|w_\pm|)\ge0$.

**Lemma 5.5 [R].**
- **(a)** Let $f$ be holomorphic on $0<{\rm Im}\,z<1$ with $|f|\le C(1+|z|)^A({\rm Im}\,z)^{-B}$. Then $|\langle f(\cdot+i0),\chi\rangle|\le C'\sum_{j\le\lceil B\rceil+1}\int(1+|x|)^A|\chi^{(j)}|$ (almost-analytic extension). A positive jump measure therefore has $\nu([R,2R])\le CR^{A+1}$.
- **(b)** One-dimensional distributional edge of the wedge, via $K$-fold primitives (Hörmander §3.1).

**Prop 5.6 (dispersion relation) [R, R_cond: W1–W3].**
- (a) $T_2(\omega,Q^2)$ is holomorphic and odd on $\mathcal C$.
- (b) $|T_2|\le C_Q(1+|\omega|)^A|{\rm Im}\,\omega|^{-B}$, with $A,B$ independent of $Q$.
- (c) ${\rm Disc}\,T_2=4\pi i\nu_Q$, where $\nu_Q=F_2(1/\omega)d\omega\ge0$ on $[1,\infty)$, for **every** $Q^2$.
- (d) For even $n_0>A+1$:
  $$T_2=\sum_{n<n_0}t_n\omega^{n-1}+4\omega^{n_0-1}\int_{(0,1]}\frac{x^{n_0-2}F_2\,dx}{1-x^2\omega^2},$$
  so $t_n=4M_2^{(n)}$ for $n\ge n_0$.

*Proof.*
1. **Tubes.** $T=i\tilde R$ on the forward tube and $i\tilde A$ on the backward tube, with Vladimirov bounds.
2. **Oddness.** Crossing makes $T_2$ odd.
3. **Slice holomorphy.**
   - $S_1=PPT$ and $S_2=gT$ are SO(3)-invariant. On the slice $q=(w,0,0,s)$ they are even in $s$, hence holomorphic in $(w,s^2)$.
   - The root with ${\rm Re}\,s>0$ of $s^2=w^2+Q^2$ satisfies $|{\rm Im}\,s|<{\rm Im}\,w$.
   - So $T_2$ is holomorphic for ${\rm Im}\,w>0$, except possibly at $w=iQ$.
4. **The point $w=iQ$ is removable:** $T_2=Q^4(b+a/Q^2)/\nu$ (h1 d).
5. **Bounds.**
   - Slice inequality: ${\rm Im}\,w-|{\rm Im}\,s|\ge{\rm Im}\,w\,Q^2/(2(|w|^2+Q^2))$ (h1 e).
   - This gives $A=a+2b+2$ and $B=b$.
6. **Jump.** $i(\tilde R-\tilde A)=4\pi iW$, and $W=0$ for $|\omega|<1$ by W2.
6′. **Slice restriction (made explicit; this replaces the earlier sketch "continuity of primitives").**
   - **Local wedge.** Fix $Q_0^2>0$ and a compact interval of ${\rm Re}\,w$. For complex $Q^2$ near $Q_0^2$, the condition $|{\rm Im}\,s|<{\rm Im}\,w$ reads, to first order, $|\eta_Q+2x\eta_w|<2\sqrt{x^2+Q^2}\,\eta_w$, with $\eta_w={\rm Im}\,w$ and $\eta_Q={\rm Im}\,Q^2$. So $F(w,Q^2):=T_2(q(w,Q^2))$ is jointly holomorphic on a local wedge $\mathcal W\subset\mathbb C^2$ over the edge $\{(x,Q^2)\}$. Its cone Γ is open, convex, and contains:
     - the direction (1,0) (fixed $Q^2$);
     - the direction $(1,-2x)$: the 4D approach ${\rm Im}\,q=(\eta,0,0,0)$, which in these coordinates is the curve $(x+i\eta,\ Q^2+\eta^2-2ix\eta)$.
   - **Uniform bound.** On compact subcones $|F|\le C|{\rm Im}\,z|^{-B}$, by Vladimirov and step 5.
   - **(i) Slice boundary values.** Let $G$ be a $K$-fold primitive in $w$ with $K>B$. Then $|\partial_\eta G(x+i\eta,Q^2)|\le C\eta^{K-1-B}$ uniformly, so $G(\cdot+i0,\cdot)$ is jointly continuous. Hence $F(\cdot+i0,Q^2)=\partial_x^KG$ exists for every $Q^2$ and is weakly continuous in $Q^2$.
   - **(ii) Identification with the 4D boundary value.** By the same uniformity, $\int dQ^2\langle F(\cdot+i0,Q^2),\varphi(\cdot,Q^2)\rangle=\lim_{\eta\to0}\iint F(x+i\eta,Q^2)\varphi$. This is the 2D boundary value from $\mathcal W$, which is independent of the approach inside Γ (Hörmander Thm 3.1.15). It therefore equals the pull-back of the SO(3)-averaged 4D boundary value $i\tilde R$ under the real-analytic change of variables $(q^0,|\mathbf q|)\mapsto(w,Q^2)$, whose Jacobian $2|\mathbf q|$ is nonzero.
   - **(iii) Every slice.** The 4D jump disintegrates as $\int dQ^2\,D_{Q^2}$, with $D_{Q^2}$ the slice jump, weakly continuous in $Q^2$. The 4D jump is positive for ν>0 and vanishes for $|\omega|<1$. By continuity these two properties hold for every $Q^2$, not just almost every $Q^2$, and $D_{Q^2}$ is a positive measure, $=4\pi i\nu_Q$ (fixes E9). Lemma 5.5(b) then gives holomorphy on $\mathcal C$.
7. **Positivity:** $F_1\ge0$ and $F_2\ge\nu F_1/\hat P^2\ge0$, slice by slice.
8. **Growth.** Lemma 5.5(a) gives $\nu_Q([R,2R])\le C_QR^{A+1}$, so $\int x^{n_0-2}F_2<\infty$ for $n_0>A+1$. (This is sharper than the spec's $n_0>A+2$.)
9. **Dispersion relation.**
   - Let $H=T_2-\sum_{n<n_0}t_n\omega^{n-1}-D_{n_0}$. It has no jump.
   - $|1-x^2\omega^2|\ge({\rm Im}\,\omega)^2/|\omega|^2$, so Lemma 5.4 makes $H$ a polynomial.
   - $H=O(\omega^{n_0-1})$ at 0, and $H(iy)/(iy)^{n_0-1}\to0$. Hence $H\equiv0$. ∎

This is a re-proof of reference Lemma C.64 with fixes; the explicit $n_0$ is new.

**Theorem 5.7 [R, R_cond: W, N1].** $t_n=4\sum_iC^{(n)}_{2,i}A^{(n)}_i+O((M^2+mM)Q^{-2}\ln^kQ)$ for every even $n\ge2$.

*Proof.*
1. The positivity tail is $\le2t_{n_0}r_Q^{N-1}$.
2. Apply Markov on $\mathcal I_Q$.
3. Bootstrap: $t_{n_0}=O(\ln^kQ)$.
4. $(M/Q)^{N-1-n}\le(M/Q)^2$. ∎

This is a re-proof of reference Thm C.50 with a minimal hypothesis.

**Prop 5.8 [R, R_cond: W].** Given (d) with $n_0\ge4$: [$t_n=4M_2^{(n)}$ for all even $2\le n<n_0$] holds iff G holds.
- Proof: descending induction with the identity
  $$T_2(iy)/(iy)=\sum_{n<k-2}t_n(iy)^{n-2}+(iy)^{k-4}\Big[t_{k-2}-4\int x^{k-4}F_2\frac{x^2y^2}{1+x^2y^2}\Big].$$
  h1(g) checks only the integrand identity; the limits are argued in the text.
- Regge behaviour is neither necessary nor sufficient: a fixed pole $c\omega$ is invisible in $F_2$.

**Theorem 5.9 [R, R_cond: N2].**
$$C^{(n)}_{2,i}(Q^2/\mu^2,\alpha_s(\mu))=\sum_jC^{(n)}_{2,j}(1,\alpha_s(Q))\Big[\mathcal P\exp\Big(-\int_\mu^Q\frac{d\mu'}{\mu'}\gamma^{(n)}\Big)\Big]_{ji}.$$
Twist-2 $\overline{\rm MS}$ RG is mass-independent and has no lower-dimension mixing at rank $n$, so E10 does not arise.

**Theorem M (hadron-level DIS moments) [R, R_cond].** This refines reference Thm C.66.
- (i) [W, N1] $t_n=4\sum CA+O((M^2+mM)Q^{-2}\ln^k)$ for every even $n$.
- (ii) [W] $t_n=4M_2^{(n)}$ for even $n\ge n_0$.
- (iii) [+G] All even $n\ge2$, including the momentum sum rule. G is necessary.
- (iv) [+N2] The RG-improved coefficients are asymptotic to perturbation theory.
- (v) [+Φ] Weak $x$-space convergence.

## 6. Part IV: e⁺e⁻ and the Adler function

**Assumptions.**
- **V1:** W1 in the vacuum sector; no massless spin-0 state couples to $J$.
- **V2:** the non-perturbative OPE for $D(Q^2)$, with remainder $O(Q^{-N})$ and derivative bounds.
- **V3:** the identity coefficient is asymptotic to $R_0\sum d_ka^k$.
- **V2′:** V2 on the sector $|\arg Q^2|\le\pi-\theta_0$.

**E1 [R, R_cond: V1].** Källén–Lehmann: $\hat W=2\pi\theta(q^0)(qq-q^2g)\rho$ with $\rho\ge0$. The following are equivalent:
- $\int\rho/(1+s)^2<\infty$;
- $D=Q^2\int R/(s+Q^2)^2<\infty$ at one (hence every) $Q^2$;
- Π satisfies a once-subtracted dispersion relation.

**E2 [R, R_cond: V1–V3].** $D=R_0[1+\sum_{k\le K}d_ka^k]+O(a^{K+1})+O(m^2/Q^2)+O(\Lambda^4Q^{-4}\ln^k)$. There is no $1/Q^2$ term in the chiral limit.

**E3 [R, R_cond: V1–V3 + derivative bounds].** $M_k=kQ^{2k}\int R/(s+Q^2)^{k+1}$ satisfies $M_1=D$ and $M_{k+1}=M_k-\frac{Q^2}k\frac{dM_k}{dQ^2}$. Hence $M_k=R_0[1+d_1a+(d_2+H_{k-1}b_0d_1)a^2+O(a^3)]$ with $b_0=\beta_0/4$.
- e1(c): the formula for $k\le6$;
- e1(c′): the recursion checked against the definition for $R=s^{1/3}$, $k=1,2,3$.

**E4 [R, R_def] (exact counterexample).** For $|\kappa|<1$, $R=R_0[1+\kappa\sin(\sqrt s/\Lambda)]$ gives exactly $D=R_0[1+\kappa\frac\pi2\frac Q\Lambda e^{-Q/\Lambda}]$. So the Euclidean OPE plus positivity fixes neither pointwise $R$ nor $R$ smeared over a fixed width. Known in spirit (Shifman; Blok–Shifman–Zhang).

**E5 [R, R_cond: V1 + leading term]; classical Karamata method, no novelty claimed.** If $R\ge0$ and $D\to R_0$, then $\frac1s\int_0^sR\to R_0$. The proof is Karamata, then a monotone-density step, then Karamata again. No rate in general.

**E6 [R, R_cond: V2′]; known (Poggio–Quinn–Weinberg 1976).**
$$\bar R_\Delta(s)=12\pi\,{\rm Im}\,\Pi(s+i\Delta)=\frac1{2\pi}\int_{-(\pi-\theta)}^{\pi-\theta}D(|s+i\Delta|e^{i\phi})\,d\phi.$$
- Proportional smearing is asymptotic to perturbation theory.
- Fixed width needs local duality (E4).

Perturbative e⁺e⁻: c_ee Thm 5.1 (K10).

## 7. Verification log

All six scripts were re-run on 2026-10-11 and reproduce their stored logs byte for byte.

- **f1.** Explicit topologies and random graphs. Documentation fixes:
  - (C1) and (C4) are identities (Lemma F.0);
  - the sampling of (C2), (C3) and the classification of degenerate graphs are heuristic and superseded by f3;
  - the class "±p bridge" is relabelled as an external-leg correction, excluded by amputation.
- **f2.** Exact ratio = 1.
  - The docstring is corrected: real parameter points, not complex.
  - Quadrature point 2 deviates by $1.23\times10^{-5}$ (tolerance $2\times10^{-5}$, endpoint singularity). The exact-$y$ check agrees to $10^{-12}$.
  - Off-shell asymptotics confirmed.
- **f3 (new).** Lemma F.6, exact checks:
  - 21/21 explicit graphs pass;
  - 1028 random multigraphs (129 full-dimensional) pass, with 0 failures.
- **f4 (new).** Lemma F.7:
  - transversality solution and D-dimensional projector;
  - no negative powers of ν for transverse homogeneous tensors of degree $n\le8$;
  - D-dimensional tree level: $T_2=4\omega/(1-\omega^2)$, $T_1=2\omega^2/(1-\omega^2)$;
  - gluon projector: $d\cdot p=d\cdot q=0$, trace $2-D$, degree 0.
- **h1.** Unchanged. (g) is only the integrand identity.
- **e1.** (c′) now checks the recursion against the definition and the closed form for $R=s^{1/3}$.
- **c_dis.** One-loop Taylor coefficients equal the cut moments exactly in ε, for $N\le8$.

## 8. Changes relative to the reference's App C and to CLAIMS

1. **Ass. C.24.** Not needed in the DR route. R-M26's uniqueness discharge is circular.
2. **Prop C.44.**
   - The (B1) identity for $\langle T\tilde T s\Phi\rangle$ holds trivially in DR.
   - The proof omits the merged terms. Corrected conclusion: $sX_d\in\mathcal E$ (Theorem B), conditional on E_ε.
   - asm:appM-brst-ope is to be replaced by E_ε + LBC.
3. **C.54(a), forward remainder.** Reduced to (A3) + E_ε (Theorem F, Lemmas F.6–F.7, Corollary F.2). Theorem F itself is [R, R_PT].
4. **Rem C.37, zero-momentum IR question.** Indicated by BM II, [A], pending O10.
5. **Hadronic part.**
   - W2 corrected (ERR-M25).
   - The slice edge of the wedge is now a full proof (E9).
   - E10 avoided.
   - $n_0$ made explicit.
   - The $\hat P=0$ point treated rigorously.
6. **C.58** replaced by the weaker N1.
7. **Rem C.62** extended to E1–E6.

## 9. Open problems

See the `open` list.

## 10. Key references

- **K1:** Lowenstein–Zimmermann 1975; Lowenstein 1976; Breitenlohner–Maison 1977 I–III; Poggio–Quinn 1976.
- **K2:** Smirnov CMP 134 (1990) 109 (read); Chetyrkin arXiv:1701.08627; Smirnov 1991 (book); Smirnov hep-th/9412063; Gorishny NPB 319 (1989) 633; Llewellyn Smith–de Vries NPB 296 (1988) 991; Gorishny–Larin–Tkachov PLB 124 (1983) 217.
- **K3, K4:** Joglekar–Lee Ann. Phys. 97 (1976) 160; Joglekar Ann. Phys. 108 (1977) 233 and 109 (1977) 210; Kluberg-Stern–Zuber PRD 12 (1975) 467, 482, 3159; Henneaux PLB 313 (1993) 35; Collins–Scalise PRD 50 (1994) 4117.
- **K5:** Hollands RMP 20 (2008) 1033 (§4.1.3 read); Hollands CMP 273 (2007) 1; FHH JMP 57 (2016) 122301; Fröb–Holland arXiv:1603.08012.
- **K6:** Barnich–Brandt–Henneaux Phys. Rep. 338 (2000) 439; Henneaux PLB 367 (1996) 163; Barnich–Henneaux–Hurth–Skenderis PLB 492 (2000) 376.
- **K8:** Schultka arXiv:1806.01086; Nilsson–Passare 2013; Berkesch–Forsgård–Passare 2014; Kaneko–Ueda 2010; Feichtner–Sturmfels arXiv:math/0411260; Lee–Pomeransky JHEP 11 (2013) 165; Tarasov PRD 54 (1996) 6479.
- **Forward-expansion literature:** Gorishny–Larin NPB 283 (1987) 452; Larin–van Ritbergen–Vermaseren NPB 427 (1994) 41; Larin–Nogueira–van Ritbergen–Vermaseren NPB 492 (1997) 338; Moch–Vermaseren–Vogt NPB 724 (2005) 3; Semenova–Smirnov–Smirnov EPJC 79 (2019) 136; Jantzen JHEP 12 (2011) 076.
- **K9:** Vladimirov 1979; Reed–Simon II; Hörmander ALPDO I; Feller II; Korevaar 2004; Borwein–Erdélyi 1995.
- **Other:** Kugo–Ojima 1979; 't Hooft–Veltman 1972; Poggio–Quinn–Weinberg 1976.

## 11. REVISIONS (fix round 1, 2026-10-11, responding to review_r1_1 and review_r1_2)

**Process.**
- REPORT.md was never written, because the harness blocks subagent report files. This text is built from the author's **final** StructuredOutput, not the blocked draft.
- The draft's claim "Prop A.6: C.24 follows from Smirnov + uniqueness" is **withdrawn** (Remark A.6).
- The parent must save this summary as REPORT.md, and must persist review outputs.

**Grades.**
- **R1 (all reviewers).** The tag "[R-cited]" is abolished in favour of the monograph tags.
  - Theorem A overall [A]: (A1), (A3) [A]; (A2), (A4), (A5) [R, R_cond: A1, A3].
  - Theorem I: [A].
  - Corollary F.2: [A].
  - Theorem B: [R, R_cond: E_ε], content [A].
  - Slot outcomes are now stated explicitly (§0).
- **R2 (O1 partly done).**
  - Smirnov 1990 was read in full, and its theorem location and scope were recorded (K2). It does not make (A1), (A3) [R].
  - Chetyrkin 1701.08627 was checked: Thms 7–8 are unproven there.
  - Gorishny 1989 and LS–dV 1988 are still unread.

**Part I.**
- **R3 (Theorem A, (A5)).** Added: polynomial ln μ dependence, the Lagrange-interpolation argument, and the inhomogeneous identity term for the vacuum correlator.
- **R4 (Theorem B).** Repairs:
  - exact LBC citation (BBH §8.6, Lemma 8.1, Thm 7.1, §2.6–2.7; Henneaux 1996 §3; BHHS 2000 App.);
  - DR-SD written with factors of $i$ and Grassmann signs;
  - sign matching of the merged terms;
  - degree matching (step 5) written out;
  - E_ε placed in the register.

  Withdrawals and corrections:
  - **WITHDRAWN:** "(B1)'s polynomial contact terms are in general false and carry logs". The (B1) identity is trivially true in DR; the gap is the omission of the merged terms in (B2) and C.44, now stated correctly.
  - **WITHDRAWN:** "new proof". Novelty is not claimed (Joglekar 1977 II, abstract).
  - Stated precisely: the reference's conclusion "$sX_d=0$ classically" is not established by its proof; Theorem B gives $sX_d\in\mathcal E$, which suffices.

**Part II.**
- **R5 (Theorem F, (F-DR)).** The hypothesis is replaced by **Lemma F.6**, which is proven: matroid base polytope, facet classification, and the strong form for all powers, dimension shifts, Taylor terms and all ω ∈ $\mathcal C$, via Schultka Thm 3.6 = BFP Thm 2.4 (whose coefficient condition holds for every ω ∈ $\mathcal C$). Checked by f3 and by both reviewers' scripts.
- **R6 (Theorem F, spin sums).** "Spin sums are polynomial in $p$" was false for gluons and for the $T_2$ projector. Replaced by **Lemma F.7** (D-dimensional projector, Laurent cancellation; gluon case meromorphic, with regularity in Corollary F.2).
- **R7 (Theorem F, statement).** Added:
  - the parametric definition and its equality with the iε integral for real $|\omega|<1$;
  - the colour argument for zero-momentum bridges;
  - the LSZ/amputation remark.
- **R8 (Corollary F.2).** The asm:appM-forward remainder bound is derived by Cauchy estimates, uniformly in all Euclidean directions. asm:appM-forward is recorded as reduced, not discharged.
- **R9 (Corollary F.3).**
  - "Disc = 4πi F₂" downgraded to [A] (or read as a definition).
  - **WITHDRAWN:** "[R] at one loop for all $n\ge1$ (c_dis)".
  - X3c is not delivered.
- **R10 (Remark F.5).** "Answers Rem C.37" is replaced by "indicates, [A], pending O10".
- **R11 (novelty markers).**
  - Theorem F, Lemmas F.1 and F.6: "the book's rigorous proof of the method of projectors", with the literature cited. The marker is pending the §6.5 second check.
  - Lemma F.0: elementary.
  - E5: classical; "new in this context" **withdrawn**.

**Part III.**
- **R12 (Prop 5.6).** The slice-restriction step is now a full argument (step 6′): local wedge in $(w,Q^2)$, uniform primitives, independence of the approach direction, disintegration with weak continuity. So positivity and support hold for every $Q^2$.

**Scripts.**
- **R13.** f1 docstring (identities, heuristic part, amputation label); f2 docstring and tolerance; e1(c′) completed; new f3 and f4.

**Rejected or unchanged items.**
- None of the reviewers' points was rejected.
- **Not done:**
  - an all-$N$ one-loop proof (X3c): optional, recorded as O4′;
  - an explicit one-loop example of log-carrying merged coefficients: no longer needed, since the claim was withdrawn.

## results

### [results 1]
SLOTS (fix round 1): X3a FAILS as planned (uniqueness discharge of asm:appM-remainder is circular, Remark A.6; stays [A]); X3b NOT passed (prop:dis-ope-euclid stays [A], D3 unchanged; Smirnov 1990 read: theorem proven for distributional remainder in analytic regularization, function form in DR only asserted); X3c NOT delivered (one-loop all-n claim withdrawn); X3d PARTIAL (QCD: asm:appM-brst-ope reduced to E_eps + cited LBC by Thm B, content [A]; pure YM: Hollands 2008 §4.1.3 located, different framework, not verified); X3e PASS pending round-2 confirmation (Thm F + Lemmas F.6, F.7, [R, R_PT]); prop:dis-ope-forward stays [A] (bottleneck A3 + E_eps).

### [results 2]
Lemma A.3 [linear independence of operator Green functions]: if sum_O c_O(q) G_[O];Phi(p) = O(|q|^rho ln^k) for all Phi, p (open non-exceptional set), each order, then c_O = O(|q|^rho ln^k); graded-homogeneous c_O of degree > rho vanish; also at fixed generic eps. [R, R_PT]. Known in spirit (ref. Lemma C.30).

### [results 3]
Thm A [Euclidean OPE for J J, full MS-bar basis; DR+MS-bar, Feynman gauge, fixed order]: (A1) remainder O(|q|^{1-a} ln^k) uniformly; (A2) C_O = |q|^{2-d_O} x polynomial in ln(q^2/mu^2); (A3) C^MS = C^bare Z^{-1}; (A4) uniqueness; (A5) RG (argument now includes ln-mu polynomiality + Lagrange interpolation; inhomogeneous identity term for vacuum correlator). Grade [A] overall: (A1),(A3) [A] (Smirnov CMP 134 (1990) 109 Theorem p.117 + §6, scope limits recorded; Chetyrkin 1701.08627 Thms 7-8 proofs deferred; Gorishny 1989, LS-dV 1988 unread); (A2),(A4),(A5) [R, R_cond: A1, A3]. Content standard; assembly ours.

### [results 4]
Remark A.6 [logic]: CLAIMS R-M26 (any proven OPE discharges Ass. C.24 by uniqueness) is circular: lem:appM-uniqueness(a) needs the frozen-q remainder small, i.e. C.24. DR route needs no C.24; frozen-q route needs an identification lemma (O3). Draft claim 'Prop A.6: C.24 follows' withdrawn.

### [results 5]
Thm B [BRST reduction of OPE coefficients]: premises DR-WI, DR-SD (exact bare DR identities, signs and factors of i stated), E_eps (expansion with one composite spectator s(phi), same C_O, merged C^{s phi}(q;p) polynomial in p), LBC (BBH Phys.Rep.338 §8.6 + Lemma 8.1 + Thm 7.1 + §2.6-2.7; Henneaux PLB 367 (1996) 163 §3; BHHS PLB 492 (2000) 376 App.). Conclusion: sum_{d_O=d} C_O sO = E_{d+1} in EOM ideal (merged terms = Green functions of the EOM operator E(q) = -i sum (+-) O' C^{s phi}(q;-i d) dS/dphi); hence X_d = GI + s-exact + EOM; with Joglekar-Lee only GI survive between physical states, twist 2 = O_q, O_g. Grade [R, R_cond: E_eps], content [A]. Novelty NOT claimed (Joglekar Ann.Phys. 109 (1977) 210). Corrects the proof of ref. Prop C.44 (omitted merged terms; conclusion sX_d in EOM ideal, not sX_d = 0); withdraws first-version claim that (B1) contact terms are false/log-carrying.

### [results 6]
Thm I = A + B + twist classification [GI OPE for massless QCD with quarks]. [A].

### [results 7]
Lemma F.0 [forward 2-forest structure]: F = Q^2 (F0 + omega F1), c_p, c_q in {0,+-1}; mon(F1) subset mon(F0), |coef| <= 1; F0 = F-polynomial at p = 0. [R, R_PT]. Elementary; no novelty claimed.

### [results 8]
Lemma F.1 [Newton-polytope domination]: G_lambda = U + F0 + lambda F1 with F1 dominated by F0, Newt full-dimensional, |lambda| <= r < 1: integral and all Taylor-term integrals converge on a common open set; I(lambda) = sum lambda^n I_n; continuation with lambda-independent candidate poles; Taylor identity after continuation. [R]. Proof here; tools standard (Schultka Thms 3.1, 3.6; BFP 2.4; Kaneko-Ueda).

### [results 9]
Lemma F.6 [matroid structure, discharge of (F-DR)] (new in this revision): with G0 = G + {J1J2}: F0 = U(G/{J1=J2}), U(G0) = x_q U(G) + U(G/{J1=J2}); Newt(U+F0) is affinely isomorphic to the base polytope of the cographic matroid M*(G0); dim = N+1-c(M(G0)) (Feichtner-Sturmfels Prop 2.4), full iff G0 loopless and 2-connected; facets (FS Prop 2.3): e_e (d=0), -1 (d=-(L+1)), -1_F (d=-r*(F)<0), 1_{E\F'} (d=L+1-r*>0); hence d=0 only for coordinate facets and DR is admissible for all positive powers, dimension shifts, Taylor terms and all omega in the cut plane (Schultka Thm 3.6 = BFP Thm 2.4; its coefficient condition holds for every omega in C). [R]. Tools standard, application ours. Checked exactly by f3 (21 + 1028 graphs) and by both reviewers.

### [results 10]
Thm F [forward on-shell DR amplitude]: for amputated forward graphs of an on-shell massless parton (bridges with +-p excluded by amputation, LSZ = 1; zero-momentum bridges vanish by colour averaging), DR amplitude defined parametrically (= Feynman i-epsilon integral for real |omega| < 1), components contracted with p-polynomial tensors: (F1) every Laurent coefficient holomorphic in C = complex plane minus (-inf,-1] and [1,inf); (F2) for |omega| < 1 equals the naive Taylor series in p (method of projectors), absolutely convergent; (F3) degenerate graphs scaleless. (F-DR) now a theorem (Lemma F.6). [R, R_PT] per graph. Status: 本书给出的严格证明（该方法在文献中作为 method of projectors 使用）: GLT PLB 124 (1983) 217, Gorishny-Larin NPB 283 (1987) 452, LvRV NPB 427 (1994) 41, LNvRV NPB 492 (1997) 338 (Eq. 29 remark); SSS EPJC 79 (2019) 136 does not cover it; 本书新结果 marker pending second literature check (Tkachov, Smirnov books).

### [results 11]
Lemma F.7 [projection onto T2 in D dimensions]: transverse T in span{g,pp,pq,qp,qq}; T2 = Q^4[(D-1) S1 - (nu^2/Q^2) S2]/((D-2) nu^3), S1 = ppT, S2 = gT; quark target: T2 holomorphic on C, Taylor = naive (omega^{-3..0} terms cancel; n-th naive term gives beta_n nu^{n-1}, beta_n = 0 for n < 2); gluon target (physical average d_ab(p,q), degree 0): meromorphic on C with possible pole only at 0, naive Laurent expansion termwise. [R, R_PT]. Checked by f4.

### [results 12]
Cor F.2 [forward partonic OPE at every order]: T^{mu nu}_j = sum_O C^{mu nu}_O <j|[O]|j> for |omega| < 1, only twist-2 GI operators, A_{i/j} = Z x tree; T2^(j) = 4 sum_{n even} omega^{n-1} sum_i C^(n)_{2,i} A^(n)_{i/j} incl. gluons (regular at 0); explicit asm:appM-forward bound |T - sum_{d_O<=N}| <= C |q|^{1-N} (1+ln|q|)^k for |q| >= 4 sqrt2 p0, uniformly in all Euclidean directions (Cauchy estimates). [A] (inherits Thm A (A3) and Thm B). asm:appM-forward reduced to A3 + E_eps, not discharged.

### [results 13]
Cor F.3 [perturbative cut-plane structure]: (a) Laurent coefficients of partonic T2 holomorphic on C [R, R_PT]; (b) Disc T2 = 4 pi i F2 (cut diagrams) [A] (DR cutting rules; or a definition); (c) moments for even n > A+1 [A] (O4). c_dis verifies one loop N <= 8 exactly in eps [R, R_PT for those N]. Withdrawn: one-loop all-n claim; X3c not delivered.

### [results 14]
Examples F.3/F.4 [explicit one-loop checks]: forward triangle with general powers = Gamma-prefactor x B x B x 2F1(a-D/2, a1; a1+a3; omega); omega^n coefficient = naive term identically in (a_i, D); each term at a_i = 1 has pole -1/((n+1) eps); off-shell leg: Q^2 I = ln(Q^2/P^2) + 2 + O(P^2 log) (non-uniformity). [R, R_PT] (one loop). f2 (point 2 quadrature 1.2e-5, flagged).

### [results 15]
Remark F.5 [zero-momentum insertions]: twist-2 O^(n), n >= 2 (IR degree n+2 >= 4) inserted at zero momentum into p^2 < 0 two-point functions expected IR finite by Breitenlohner-Maison II; hypotheses for exceptional composite insertions unchecked (O10); indicates, does not settle, ref. Rem C.37. [A].

### [results 16]
Lemma 4.10 [what the hadronic step needs]: beyond W1-W3 only the segment approximation N1 on I_Q = {iy: |y| <= sqrt3 M/Q}; no perturbative statement implies it; M > 0 removes exceptional-momentum obstruction. Logic.

### [results 17]
Lemmas 5.1-5.2: Phat^2 = M^2 qvec^2/Q^2 >= M^2/4, I_Q covered [R, R_def]; N1-std (with chiral suppression) implies SA for all N with pi_n = 4 sum C A + O((M^2+mM)/Q^2 ln^k) [R, R_cond: N1-std]. Re-proof of ref. Lemma C.47.

### [results 18]
Lemmas 5.3-5.5 [Markov, Jensen, boundary values]: |h_k| r^k <= 2(1+sqrt2)^D sup |h|; entire f with |f| <= C(1+|z|)^A |Im z|^{-B} is a polynomial of degree <= A; boundary-value estimate, nu([R,2R]) <= C R^{A+1}; 1-d edge of the wedge. [R]. Known; full proofs.

### [results 19]
Prop 5.6 [dispersion relation from W1-W3]: T2 holomorphic odd on C; |T2| <= C_Q (1+|omega|)^A |Im omega|^{-B} (A,B Q-independent); Disc T2 = 4 pi i nu_Q, nu_Q >= 0 for EVERY Q^2 (slice restriction now proven: local wedge in (w,Q^2), uniform K-fold primitives, direction independence, weakly continuous disintegration); n0-subtracted relation for even n0 > A+1, t_n = 4 M2^(n) for n >= n0. [R, R_cond: W1-W3]. Re-proof of ref. Lemma C.64 with fixes (W2/ERR-M25, removable point, E9, explicit n0).

### [results 20]
Thm 5.7 [fixed-n Taylor coefficients]: under Prop 5.6 and N1 for one N >= max(n+3, n0+2): t_n = 4 sum_i C^(n)_{2,i} A^(n)_i + O((M^2+mM)/Q^2 ln^k Q) for every even n >= 2. [R, R_cond: W, N1]. Re-proof of ref. Thm C.50, minimal hypothesis.

### [results 21]
Prop 5.8 [low moments iff growth]: given the n0-subtracted relation (n0 >= 4), t_n = 4 int x^{n-2} F2 for all even 2 <= n < n0 (incl. momentum sum rule) iff lim T2(iy)/(iy) = 0; fixed pole c omega invisible in F2. [R, R_cond: W]. Ref. Rem C.65 re-proved.

### [results 22]
Thm 5.9 + Thm M [hadron-level DIS moments]: (i) [W,N1] t_n = 4 sum C A + O((M^2+mM)Q^{-2} ln^k) every even n; (ii) [W] t_n = 4 M2^(n), n >= n0; (iii) [+G] all even n >= 2, G necessary; (iv) [+N2] RG-improved coefficients asymptotic to PT (no mass mixing, E10 avoided); (v) [+Phi] weak x-space convergence. [R, R_cond]. Refinement of ref. Thm C.66.

### [results 23]
E1 [Kallen-Lehmann; one subtraction iff D finite at one point] [R, R_cond: V1]. Known; precise form.

### [results 24]
E2 [Adler function asymptotics; no 1/Q^2 term in chiral limit] [R, R_cond: V1-V3]. Known (ref. Rem C.62).

### [results 25]
E3 [Euclidean moments M_k = R0[1 + d1 a + (d2 + H_{k-1} b0 d1) a^2 + O(a^3)], recursion M_{k+1} = M_k - (Q^2/k) dM_k/dQ^2] [R, R_cond: V1-V3 + derivative bounds]. Presentation ours; e1 (c), (c').

### [results 26]
E4 [exact duality-violation counterexample: R = R0[1 + kappa sin(sqrt s/Lambda)] gives D = R0[1 + kappa (pi/2)(Q/Lambda) e^{-Q/Lambda}]] [R, R_def]. Known in spirit (Shifman; Blok-Shifman-Zhang).

### [results 27]
E5 [Tauberian: R >= 0 and D -> R0 imply Cesaro mean of R -> R0] [R, R_cond: V1 + leading term]. Classical Karamata method; novelty claim withdrawn.

### [results 28]
E6 [PQW smearing: 12 pi Im Pi(s+i Delta) = contour average of D; proportional smearing asymptotic to PT; fixed width needs local duality] [R, R_cond: V2']. Known (Poggio-Quinn-Weinberg 1976).

### [results 29]
VERIF: f1, f2, f3 (new), f4 (new), h1, e1 re-run 2026-10-11, all logs reproduced byte for byte; f3: Lemma F.6 exact on 21 explicit + 1028 random graphs, 0 failures; f4: projector/Laurent/tree-level/gluon-projector checks; c_dis one-loop N <= 8 exact in eps.

## open

### [open 1]
O1 (partly done): Smirnov CMP 134 (1990) read (Theorem p.117: distributional remainder, analytic regularization; function form in DR asserted; §6 operator form; no ghosts/gauge-variant bases/composite spectators). Remaining: Gorishny NPB 319 (1989) 633, Llewellyn Smith-de Vries NPB 296 (1988) 991, Smirnov 1991 book; establish at theorem level the DR function form at fixed eps, direction uniformity, ghosts, and E_eps; then Thm A (A1, A3), Thm B and Cor F.2 become [R].

### [open 2]
O2: FHH-type flow-equation existence, bounds and BRST Ward identities for Yang-Mills with Dirac fermions (independent route to Thm I).

### [open 3]
O3: Identification lemma for the reference's frozen-q BPHZ coefficients (discharges Ass. C.24; uniqueness alone is circular). Suggested route (review r1-2): compare p-derivatives at p = 0 of the over-subtracted frozen-q representation and of the cited expansion in a massive model; needs q-uniform bounds on p-derivatives of the cited remainder at p = 0.

### [open 4]
O4: Fixed-order polynomial growth bounds in omega for the partonic forward amplitude at all orders (moment identity for all n, absence of fixed poles).

### [open 5]
O4' (slot X3c): one-loop all-N forward identity: exact-in-eps one-loop forward amplitude as 2F1 combinations, large-|omega| bound at fixed eps, Disc = cut diagrams at one loop (incl. delta(1-x)), contour argument, continuation in eps.

### [open 6]
O5: Non-perturbative: construct 4D QCD; derive N1 (e.g. Bostelmann phase-space condition plus single-particle uniformity).

### [open 7]
O6: Derive the growth condition G (absence of a real fixed pole c omega) from axioms or Regge theory.

### [open 8]
O7: Convergence (not only asymptoticity) of the OPE for YM/QCD at fixed order (as Hollands-Kopper for phi^4_4).

### [open 9]
O8: Polarized structure functions: gamma5 breaks exact DR BRST invariance; extend Thm B (Larin scheme, finite counterterms).

### [open 10]
O9: Local duality and pointwise R(s); Tauberian remainder theorems.

### [open 11]
O10: Check Breitenlohner-Maison II hypotheses for zero-momentum composite insertions (Remark F.5); remainder estimates at exceptional momenta.

### [open 12]
O11: Renormalon/OPE-basis ambiguity (ref. Prop C.68, Rem C.69) unchanged.

### [open 13]
O12: Novelty checks before any 本书新结果 marker: Thm F / Lemmas F.1, F.6 (Tkachov 1992-97; Smirnov 1991/2002/2012 books; WRITER_SPEC_v2 §6.5 second check); Thm B (full texts of Joglekar 1977 I/II, Collins 1984 §12.8). Pure-YM X3d: verify Hollands 2008 construction behind §4.1.3 and relate its position-space OPE to the DR momentum-space coefficients.

### [open 14]
O13 (pipeline, orchestrator): persist every agent's StructuredOutput as the REPORT.md / review_r*_k.md files the workflow refers to (subagent .md writes are blocked), or pass the texts inline; same for X1, X2.

## files

### [files 1]
/Users/hao-cheng/Desktop/theorem proof/qcd_factorization_work/verify/extend/X3-ope/scripts/f1_forward_graphs.py

### [files 2]
/Users/hao-cheng/Desktop/theorem proof/qcd_factorization_work/verify/extend/X3-ope/scripts/f2_triangle.py

### [files 3]
/Users/hao-cheng/Desktop/theorem proof/qcd_factorization_work/verify/extend/X3-ope/scripts/f3_matroid_lemma.py

### [files 4]
/Users/hao-cheng/Desktop/theorem proof/qcd_factorization_work/verify/extend/X3-ope/scripts/f4_projector_laurent.py

### [files 5]
/Users/hao-cheng/Desktop/theorem proof/qcd_factorization_work/verify/extend/X3-ope/scripts/h1_hadronic_checks.py

### [files 6]
/Users/hao-cheng/Desktop/theorem proof/qcd_factorization_work/verify/extend/X3-ope/scripts/e1_ee_checks.py

### [files 7]
/Users/hao-cheng/Desktop/theorem proof/qcd_factorization_work/verify/extend/X3-ope/logs/f1_forward_graphs.log

### [files 8]
/Users/hao-cheng/Desktop/theorem proof/qcd_factorization_work/verify/extend/X3-ope/logs/f2_triangle.log

### [files 9]
/Users/hao-cheng/Desktop/theorem proof/qcd_factorization_work/verify/extend/X3-ope/logs/f3_matroid_lemma.log

### [files 10]
/Users/hao-cheng/Desktop/theorem proof/qcd_factorization_work/verify/extend/X3-ope/logs/f4_projector_laurent.log

### [files 11]
/Users/hao-cheng/Desktop/theorem proof/qcd_factorization_work/verify/extend/X3-ope/logs/h1_hadronic_checks.log

### [files 12]
/Users/hao-cheng/Desktop/theorem proof/qcd_factorization_work/verify/extend/X3-ope/logs/e1_ee_checks.log

### [files 13]
/Users/hao-cheng/Desktop/theorem proof/qcd_factorization_work/verify/extend/X3-ope/review_r1_1_checks/

### [files 14]
/Users/hao-cheng/Desktop/theorem proof/qcd_factorization_work/verify/extend/X3-ope/review_r1_2_scripts/

### [files 15]
/Users/hao-cheng/.claude/projects/-Users-hao-cheng-Desktop-theorem-proof/c211c739-758d-4b40-bbac-67f4e1a65da4/subagents/workflows/wf_52f29317-58b/journal.jsonl

### [files 16]
/private/tmp/claude-501/-Users-hao-cheng-Desktop-theorem-proof/c211c739-758d-4b40-bbac-67f4e1a65da4/scratchpad/x3fix2/ (draft pieces of this report, identical to the summary; rerun logs)

### [files 17]
/private/tmp/claude-501/-Users-hao-cheng-Desktop-theorem-proof/c211c739-758d-4b40-bbac-67f4e1a65da4/scratchpad/x3fix/dl_smirnov/s90.txt

### [files 18]
/private/tmp/claude-501/-Users-hao-cheng-Desktop-theorem-proof/c211c739-758d-4b40-bbac-67f4e1a65da4/scratchpad/x3fix/dl_chetyrkin/ch.txt

### [files 19]
/private/tmp/claude-501/-Users-hao-cheng-Desktop-theorem-proof/c211c739-758d-4b40-bbac-67f4e1a65da4/scratchpad/x3fix/dl_bbh/bbh.txt

### [files 20]
/private/tmp/claude-501/-Users-hao-cheng-Desktop-theorem-proof/c211c739-758d-4b40-bbac-67f4e1a65da4/scratchpad/x3fix/dl_henneaux/h96.txt

### [files 21]
/private/tmp/claude-501/-Users-hao-cheng-Desktop-theorem-proof/c211c739-758d-4b40-bbac-67f4e1a65da4/scratchpad/x3fix/dl_henneaux/bhhs.txt

### [files 22]
/private/tmp/claude-501/-Users-hao-cheng-Desktop-theorem-proof/c211c739-758d-4b40-bbac-67f4e1a65da4/scratchpad/dl/0705.3340/paper.txt

### [files 23]
/private/tmp/claude-501/-Users-hao-cheng-Desktop-theorem-proof/c211c739-758d-4b40-bbac-67f4e1a65da4/scratchpad/dl_schultka/sch.txt

### [files 24]
/private/tmp/claude-501/-Users-hao-cheng-Desktop-theorem-proof/c211c739-758d-4b40-bbac-67f4e1a65da4/scratchpad/x3rev/dl_fs/fs.txt

### [files 25]
/private/tmp/claude-501/-Users-hao-cheng-Desktop-theorem-proof/c211c739-758d-4b40-bbac-67f4e1a65da4/scratchpad/x3rev/author/author_summary.md
