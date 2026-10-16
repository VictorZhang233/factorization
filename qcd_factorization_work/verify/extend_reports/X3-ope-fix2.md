# X3-ope-fix2

(extracted verbatim from the workflow journal; structured output of the agent)

## summary

**Status (answer to 在正常运行吗): 在运行，但不完全正常 (running, not fully normal).**
- Workflow wf_52f29317-58b is active. X1 and X2 are in review round 3 (journal lines 123–127). X3 is in fix round 2: this run, agent a316f5dc20a66707d, journal line 121.
- `verify/extend/X{1,2,3}/REPORT.md` still do not exist. Of the round-2 reviews only `X1-glauber/review_r2_1.md` is on disk.
- The X3 texts exist only in `journal.jsonl` of the workflow: fix round 1 at line 112, review r2-2 at line 119, review r2-1 at line 120.
- **What the parent should do.** Subagents must not write report files, so this StructuredOutput is the complete revised X3 report. Save it verbatim as `verify/extend/X3-ope/REPORT.md`, and save journal lines 120 and 119 as `review_r2_1.md` and `review_r2_2.md`.
- A temporary working copy of this text is `scratchpad/x3fix3/draft_report_rev2.txt` (session scratchpad, not a project file).
- Two new scripts (f5, f6) were written. All eight X3 scripts reproduce their logs; f1–f4, h1 and e1 are byte-identical on re-run (2026-10-11).

# X3 (revised after review round 2): OPE in massless QCD; DIS and e⁺e⁻ moments at hadron level

**Conventions.** As in CONTEXT.md: metric (+,−,−,−), $D=4-2\varepsilon$, $\overline{\rm MS}$, $Q^2=-q^2$, $\nu=P\cdot q$, $\omega=2\nu/Q^2=1/x$, $a=\alpha_s/\pi$.

**Grades** (WRITER_SPEC_v2 §4.3):
- [R, R_PT]: complete proof here, perturbative, per graph or per order.
- [R, R_def]: algebra and definitions only.
- [R]: mathematics with a complete proof.
- [R, R_cond: X]: complete proof given the numbered premises X. The content grade is that of the weakest premise.
- [A]: all-order argument whose cited key step was not verified at theorem level.
- [C]: open.

**Citations.** "Checked" means I read the theorem in the full text. "Abstract" means I did not. "Not read" means I could not obtain the text.

**Scripts** live in `verify/extend/X3-ope/scripts/`, with logs in `logs/`:
- f1: graph polynomials (its sampling part is superseded by f3).
- f2: the exact one-loop forward triangle.
- f3: Lemma F.6, with exact facet checks.
- f4: Lemma F.7.
- h1: hadronic lemmas.
- e1: e⁺e⁻.
- **f5 (new):** Grassmann check of the DR-SD signs.
- **f6 (new):** the D-dimensional evanescent structure.

The reviewers' checks are in `review_r1_1_checks/`, `review_r1_2_scripts/`, `review_r2_1_checks/` and `review_r2_2_scripts/`.

## 0. Executive summary

**(i) Theorem I = A + B, overall [A].** This is the strongest OPE statement for massless QCD with quarks. It holds at every order of DR+$\overline{\rm MS}$ perturbation theory in covariant gauges $\xi_R$ near 1; Feynman gauge is $\xi_R=1$.
- **Expansion (A1).** The remainder is $O(|q|^{1-a}\ln^k)$ at Euclidean non-exceptional momenta.
- **Coefficient form (A2).** $|q|^{2-d_O}$ times a polynomial in $L$.
- **Renormalization (A3).** $C^{\rm bare}Z^{-1}$.
- **(A1)–(A3)** hold in the full D-dimensional $\overline{\rm MS}$ basis.
- **Uniqueness (A4) and the RG equation (A5)** hold in every sector satisfying (NE), which has no evanescent operators. **New in this round:** (A5) carries the gauge-parameter term $\beta_\xi\partial_\xi$. Without that term it holds for the GI block in Feynman gauge (Cor. A.5, [A]).
- **Theorem B.** $sX_d\in\mathcal E$, hence $X_d$ = GI + $s$-exact + EOM.
- **Twist 2.** Only $O^{(n)}_q,O^{(n)}_g$ appear.

**Why Theorem A stays [A].** Its inputs (A1), (A3) and E_ε are cited, and the checked sources do not cover them as used here (K2).

**Theorem B.** Grade [R, R_cond: E_ε] for the bare statements, [R, R_cond: E_ε, K3] for the renormalized ones; content [A]. Two repairs this round:
- the DR-SD sign is corrected (f5);
- the use of LBC at non-integer D is justified (Remark B.1).

**(ii) Forward kinematics.**
- **Theorem F, [R, R_PT] per graph.** It is the rigorous proof of the *analytic step* of the method of projectors: the on-shell forward DR amplitude is holomorphic on the cut ω-plane and equals its convergent naive Taylor series for $|\omega|<1$.
- **Lemma F.6** is known in substance (Schultka §4 and others); here it is re-derived in matroid form.
- **The identification with $\overline{\rm MS}$ coefficients** is Cor. F.2, [A].
- **Gluon regularity at ω=0** is [A], via Cor. F.2 or via the new Lemma F.8 (conditional on the on-shell Ward identity).

**(iii) Theorem M** (hadron level) is unchanged. The slice step of Prop. 5.6 now rests on the new Lemma 5.5(c).

**(iv) e⁺e⁻, E1–E6:** unchanged.

**Slot outcomes.**

| slot | outcome |
|---|---|
| X3a | **Not delivered (open).** Replaces "FAILS as planned". (1) Uniqueness alone is circular (Remark A.6). (2) The designated sources (Anikin–Zav'yalov 1976 and 1978; Zav'yalov 1979/1990; Llewellyn Smith–de Vries 1988) could not be obtained and are unread. Secondary sources describe them as position-space short-distance expansions of Zimmermann type (K2). (3) **New Lemma A.7** [R, R_cond: CT-p]: matching at p=0 removes the circularity. Any momentum-space theorem with p-derivative bounds at p=0 in the massive model discharges asm:appM-remainder per order. asm:appM-remainder stays [A], and CLAIMS A09(5) stays open. |
| X3b | **Not passed** (unchanged). prop:dis-ope-euclid stays [A]; D3 unchanged. |
| X3c | **Not delivered.** c_dis covers N≤8. |
| X3d | **Partial.** QCD: asm:appM-brst-ope is replaced by E_ε + LBC + K3 (Theorem B, content [A]). Pure YM: Hollands 2008 §4.1.3 is located but not verified. |
| X3e | **PASS**, as a per-graph statement: Theorem F with Lemmas F.6 and F.7, [R, R_PT]. Both round-2 reviewers confirmed it. **Do not** apply the planned rule "asm:appM-forward 已解除". Via Cor. F.2 ([A]) asm:appM-forward is only reduced to (A3) + E_ε + Theorem B + K3, so prop:dis-ope-forward stays [A]. |

## 1. Setup

**D1. Theory.** SU($N_c$) with $n_f$ massless Dirac quarks.
- **Gauge fixing.** $s(\bar c(\partial A+\xi_0B/2))$ with B off-shell.
- **Gauge-parameter renormalization.** $\xi_0=Z_3\xi_R$; Feynman gauge means $\xi_R(\mu)=1$.
- **Running of $\xi_R$.** $\beta_\xi\equiv\mu\,d\xi_R/d\mu=-2\gamma_3\xi_R$, with $\gamma_3=\frac12\mu\,d\ln Z_3/d\mu$. At one loop $\beta_\xi=\frac{\alpha_s}{2\pi}\xi_R[(\frac{13}{6}-\frac{\xi_R}{2})C_A-\frac43T_Fn_f]$. At $\xi_R=1$ and SU(3) this is $\frac{\alpha_s}{2\pi}(5-\frac23n_f)\neq0$.
- **BRST.** $sA=Dc$, $s\psi=igc\psi$, $sc=-\frac g2[c,c]$, $s\bar c=B$, $sB=0$.
- **Canonical dimensions in D dimensions.** $[A]=[c]=[\bar c]=1-\varepsilon$, $[\psi]=\frac32-\varepsilon$, $[B]=2-\varepsilon$, $[g_0]=\varepsilon$, $[J]=3-2\varepsilon$, $[\mathcal J(q)]=2-2\varepsilon$.
- **Dimension of a monomial.** A monomial with 4D dimension $d^{(4)}$, $n_\phi$ elementary fields and $n_g$ explicit factors of $g_0$ has $d(\varepsilon)=d^{(4)}-\varepsilon(n_\phi-n_g)$. The map s raises $d^{(4)}$ by 1 and preserves $n_\phi-n_g$, so it raises $d(\varepsilon)$ by exactly 1.

**D2. Scheme.** DR (with analytic regulators where stated) and $\overline{\rm MS}$.
- Renormalized operators: $[O]=Z_{OO'}O'_{\rm bare}$.
- There is no $\gamma_5$, so DR is exactly BRST-invariant.
- The operator basis is D-dimensional: formal tensor and Clifford algebra, Dirac structures $\gamma^{[\mu_1\dots\mu_r]}$ of every rank $r$, including evanescent ones.

**D3. Operator classes.**
- GI: colour-singlet polynomials in $F,\psi,\bar\psi,D$.
- BRST-exact: $s\Lambda$.
- EOM: the ideal $\mathcal E$ generated by the $\partial^\alpha\delta S/\delta\phi$, for $\phi\in\{A,\psi,\bar\psi,c,\bar c,B\}$.
- Aliens: BRST-exact plus EOM.

**D4.** $\mathcal J^{\mu\nu}(q)=i\int d^Dx\,e^{iqx}TJ^\mu(x)J^\nu(0)$.

**D5.** Non-exceptional: no proper partial sum of the external momenta vanishes.

**D6.** $T^{\mu\nu}=-\tilde g^{\mu\nu}T_1+\hat P^\mu\hat P^\nu T_2/\nu$, with $T_2=\sum_{n\,\rm even}t_n\omega^{n-1}$ and $M_2^{(n)}=\int_0^1x^{n-2}F_2$. For a free quark, $T_2=4e_q^2\omega/(1-\omega^2)$.

**D7.** $O^{(n)}_{q,g}$ are symmetric and traceless, with $\langle P|O_i|P\rangle=2A_i(PP\cdots-{\rm tr})$.

**D8.** $\mathcal I_Q=\{iy:|y|\le\sqrt3M/Q\}$.

**D9.** Naive Taylor term: replace $p\to\lambda p$ and expand the integrand in λ.

**D10.** Lee–Pomeransky form $\int\alpha^{a-1}\mathcal G^{-D/2}$ with $\mathcal G=\mathcal U+\mathcal F$. By Tarasov, tensor integrals become scalar ones with shifted D and powers.

**D11. Condition (NE).** A finite sector $\mathcal S$ of basis operators satisfies (NE) if, at D=4 (4-dimensional external momenta and polarizations), the map $(c_O)_{O\in\mathcal S}\mapsto\sum_Oc_O\cdot V^{(4)}_O$ is injective. Here the $c_O$ are constant tensors contracted into the free indices of O, and $V^{(4)}_O$ are the tree-level vertex polynomials.
- By the second fundamental theorem for O(4), the only identities that hold at D=4 but not at formal D come from antisymmetrizing five or more index slots, either $\gamma^{[r\ge5]}=0$ or Gram/Schouten relations. So (NE) holds whenever no such antisymmetrization can be formed in the sector.
- **Where (NE) holds.**
  - The symmetric traceless twist-2 operators, for every n.
  - The $(\mu\nu)$-symmetric part of the $J^\mu J^\nu$ OPE for $d_O\le5$. A Dirac structure of rank $\ge5$ needs five distinct index carriers. In the symmetric channel these are at most one of μ, ν, then q, then derivative or field-strength indices, which forces $d_O\ge6$.
- **Where (NE) fails.**
  - The $(\mu\nu)$-antisymmetric part at $d_O=5$, already at tree level. The quark line with the two currents and one soft gluon has rank-5 part $2\gamma^{[\nu l\alpha q\mu]}/q^4$, so the operator $\bar\psi\gamma^{[\nu\sigma\alpha\rho\mu]}q_\rho F_{\sigma\alpha}\psi$ appears (f6).
  - The four-quark sector at $d_O=6$, where the $\Gamma^{(5)}\otimes\Gamma^{(5)}$ contraction is $-D(D-1)(D-2)(D-3)(D-4)$ (rv22_algebra (E)).

**Assumption register.**
- **E_ε** [A]. The DR large-q expansion at fixed small generic ε, for every bare $\xi_0$, for $\langle\mathcal J\Phi\rangle$ and for $\langle\mathcal J\,Z(p_Z)\Phi\rangle$ with one composite spectator $Z=s\phi$:
  $$\langle\mathcal JZ\Phi\rangle=\sum C_O\langle OZ\Phi\rangle+\sum C^Z_{O'}(q;p_Z)\langle O'\Phi\rangle+\mathcal R'.$$
  - The $C_O$ are the same as without Z.
  - $C^Z$ is polynomial in $p_Z$; it comes from the hard subgraphs that contain the Z vertex ("merged" terms).
  - All coefficients are graded-homogeneous.
  - E_ε has the scope status of K2.
- **DR-WI, DR-SD.** Exact identities of bare DR Green functions (Theorem B).
- **LBC.** K6 together with Remark B.1.
- **K3.** Joglekar–Lee triangularity, and the ξ-independence of $\gamma_{GG}$.
- **KO.** Kugo–Ojima.
- **New this round:**
  - **CT-p**: used only in Lemma A.7.
  - **OS-WI**: used only in Lemma F.8.
  - **GP**: used only in Cor. A.5.
- **Hadronic DIS:** W1–W3, N1, N1-std, N2, N3, G, Φ (§5).
- **e⁺e⁻:** V1–V3, V2′ (§6).

## 2. Literature (what was verified)

**K1. IR finiteness** (abstracts):
- Lowenstein–Zimmermann CMP 44 (1975) 73;
- Lowenstein CMP 47 (1976) 53;
- Breitenlohner–Maison CMP 52 (1977) 11, 39, 55: massless theories with all vertices of IR degree ≥4, which covers Feynman-gauge QCD;
- Poggio–Quinn PRD 14 (1976) 578.

**K2. The DR/$\overline{\rm MS}$ OPE, and the X3a sources.**
- **Smirnov, CMP 134 (1990) 109 (checked; `x3fix/dl_smirnov/s90.txt`).**
  - The Theorem on p. 117 proves the remainder estimate of (3.7) as a distribution in ξ and as a function of non-exceptional Euclidean small momenta, for λ near 0 (analytic regularization).
  - The DR function form is only asserted: "may easily be maintained", p. 118.
  - §6 gives the operator form. Ghosts, gauge-variant bases and composite spectators are not treated.
  - On p. 110 Smirnov places LS–dV [26] among the works whose expansions "have not been analytically justified" and in which "there is no explicit infrared (IR) finiteness".
- **Chetyrkin, arXiv:1701.08627 (checked).**
  - Thms 7 and 8 are stated, with proofs "given elsewhere".
  - §6: [80] = LS–dV "deals with a very particular case …, namely with the short distance expansion of a product of two composite operators".
  - The "rigorous proof" of (5.18) is credited to [53, 54] (Smirnov 1988, 1990), "along the lines of refs. [7, 9, 25, 82]", that is Zimmermann, Zav'yalov's book and AZ TMF 27.
- **Designated X3a sources: not read** (closed access).
  - Anikin–Zav'yalov, TMF 27 (1976) 425–430 [doi 10.1007/BF01028628].
  - Anikin–Zav'yalov, Ann. Phys. 116 (1978) 135–166 [doi 10.1016/0003-4916(78)90007-6]. The INSPIRE abstract reads: "Short-distance and light-cone expansions for T-ordered products of currents are derived in the framework of the arbitrary order of the perturbation theory".
  - Zav'yalov, *Renormalized Feynman diagrams* (Nauka 1979) = *Renormalized Quantum Field Theory* (Kluwer 1990).
  - Llewellyn Smith–de Vries, NPB 296 (1988) 991–1006 [OXFORD-TP-45/87]. INSPIRE abstract: the OPE "is proved for minimally subtracted operators using an extension of a simplified version of Zimmermann's momentum subtraction proof".
  - Anikin–Zav'yalov–Karchev, TMF 44 (1980) 291 and 46 (1981) 3, and Anikin–Bordag–Zav'yalov, TMF 56 (1983) 163 ("Infrared divergences … in massless theories I–III").
  - Access: OpenAlex lists no open-access copy; Springer and Elsevier require a login; mathnet.ru refuses connections and CERN CDS blocks automated access from this environment.
- **Secondary descriptions of these sources (checked).**
  - Smirnov p. 110: Zimmermann and AZ give the coordinate-space Wilson expansion (1.2), $TJ_1(x+\rho\xi_1)J_2(x+\rho\xi_2)=\sum C_i(\rho\xi_1,\rho\xi_2)[O_i](x)$. Its coefficients are Green functions of composite operators that "depend on it nontrivially", so the expansion is not one in powers and logarithms.
  - Keller–Kopper, CMP 153 (1993) 245, p. 246: "the short distance expansion of a product of two arbitrary Zimmermann normal products … was proven by Anikin and Zavialov [7] by using BPH techniques (a more accessible presentation … in [8])", where [8] is Zav'yalov's book. Their own Theorem 11 is a position-space statement in massive Euclidean $\phi^4_4$, $R_A(y)=o(|y|^{A-D^{(1)}-D^{(2)}})$.
  - Tkachov, hep-th/9612037, footnote 14: the light-cone OPE of [74] = AZ 1978 is "BPHZ-type" and studied "in coordinate representation".
  - **Consequence.** A position-space remainder bound does not imply the pointwise momentum-space bound C.24; cor:appM-coordinate goes the other way. Whether AZ or Zav'yalov prove the frozen-q momentum-space estimate, for example as an intermediate step, is unknown.
- **Gorishny, NPB 319 (1989) 633:** not obtained.
- **Conclusion:** (A1), (A3) and E_ε remain [A].

**K3. Renormalization of GI operators** (abstracts):
- Joglekar–Lee, Ann. Phys. 97 (1976) 160: GI operators mix into GI + aliens, and aliens mix only into aliens.
- Kluberg-Stern–Zuber, PRD 12 (1975) 467, 482, 3159: renormalization of GI operators; ξ-independence of $\gamma_{GG}$.
- Henneaux, PLB 313 (1993) 35.
- Collins–Scalise, PRD 50 (1994) 4117.
- BBH §8.6 (checked) supplies the cohomological part, "class I operators give a basis of $H^{0,*}(s,\Omega)$", and credits Joglekar–Lee and Henneaux 1993.

**K4. Joglekar 1977** (abstracts): Ann. Phys. 108 (1977) 233 and 109 (1977) 210.

**K5. Pure Yang–Mills.**
- Hollands, RMP 20 (2008) 1033, §4.1.3 (checked); different framework, construction not verified.
- Fröb–Holland, arXiv:1603.08012.
- FHH, JMP 57 (2016) 122301.

**K6. LBC (checked).**
- BBH, Phys. Rep. 338 (2000) 439: Thm 7.1, Lemma 8.1, §8.3, §8.6, §2.6–2.7. The text is formulated in n-dimensional spacetime, "in any number of spacetime dimensions" (abstract, §1).
- Henneaux, PLB 367 (1996) 163, §3: the gauge-fixed Koszul differential is acyclic on local functions, not on local functionals.
- BHHS, PLB 492 (2000) 376, Appendix.
- **Together they give:** if X is a ghost-number-0 local polynomial with $sX\in\mathcal E$, then $X=\sum c_jO^{GI}_j+s\Lambda+E$ with $E\in\mathcal E$, all terms of the dimension and type of X.

**K7.** Hollands–Kopper, CMP 313 (2012) 257; Holland–Hollands–Kopper, CMP 342 (2016) 385.

**K8. Euler–Mellin integrals and Feynman polytopes.**
- **Schultka, arXiv:1806.01086 (checked).**
  - §3: Thm 3.1 (convergence), Thm 3.6 = BFP 2.4 (continuation; coefficients in an open strongly convex cone), Cor 3.8.
  - §4:
    - Def 4.3: generic euclidean kinematics;
    - Thm 4.15: the Feynman polytope Newt($\psi\Phi$) is a generalized permutahedron;
    - Prop 4.17: irreducible iff s-irreducible;
    - Cor 4.18: facet presentation by subgraphs;
    - Prop 4.29: convergence domain, nonempty iff s-irreducible;
    - Rem 4.30: Speer, AIHP A 23 (1975) 1, for 1VI graphs;
    - Prop 4.31: graphs that are not s-irreducible give 0;
    - Thm 4.32: $I_G=\omega_G\prod\Gamma(\tilde\omega_\gamma)J_G$ with $J_G$ entire.
- **Other polytope results.**
  - Borinsky, AIHPD 10 (2023) 635, Thm 32 (crediting Schultka Thm 4.15 and Brown).
  - Arkani-Hamed–Hillman–Mizera, PRD 105 (2022) 125013: facet presentations of $\mathcal U_G,\mathcal F_G$ for general kinematics.
  - Tellander–Helmer, CMP 399 (2023) 1021: the proof of Thm 3.1 identifies Newt($\mathcal U$) as the cographic matroid polytope; Lemma 3.3 gives a flag matroid polytope.
  - Walther, LMP 112 (2022) 120, Lemma 3.3: momentous 2-forests form a matroid.
- Feichtner–Sturmfels, math/0411260 (checked): Prop 2.3 (flat inequalities) and Prop 2.4 ($\dim P_M=|E|-c(M)$).
- Nilsson–Passare 2013; Berkesch–Forsgård–Passare 2014; Kaneko–Ueda 2010.

**K9. Tools.**
- Vladimirov §25–26.
- Reed–Simon II, Thm IX.16.
- Hörmander, ALPDO I §3.1, Thm 3.1.15; it is extended to curved approaches in Lemma 5.5(c), proved here.
- Feller II; Korevaar; Borwein–Erdélyi.

**K10.** c_ee Thm 5.1: Euclidean steps [R]; cut identification [A].

**K11.** c_pdf §5 and §7.

**K12. Evanescent operators** (abstracts): Dugan–Grinstein, PLB 256 (1991) 239; Herrlich–Nierste, NPB 455 (1995) 39.

## 3. Part I: Euclidean perturbative OPE

### Lemma A.3 (linear independence) [R, R_PT]

**Hypothesis.** For all strings Φ and all p in an open non-exceptional set, at each order,
$$\sum_Oc_O(q)\tilde G_{O;\Phi}(p)=O(|q|^\varrho\ln^k).$$

**Conclusions.**
- **(a) Fixed generic ε, D-dimensional basis, bare functions.** $c_O=O(|q|^\varrho\ln^k)$. Graded-homogeneous $c_O$ of degrees $>\varrho$ vanish identically.
- **(b) D=4, renormalized functions.** The same holds in every sector satisfying (NE).

**Proof.** Induction in $g^2$.
1. At tree level only operators whose fields match Φ contribute, through their vertex polynomials.
2. Distinct monomials have linearly independent vertex polynomials. This holds for formal D, and at D=4 it is exactly (NE).
3. Lower orders are handled by induction. Distinct powers $|q|^{\kappa-2j\varepsilon}$ separate the orders. ∎

**Without (NE),** step 2 fails at D=4, because evanescent operators have vanishing 4D tree vertices; (b) is then not claimed. The lemma is known in spirit (reference Lemma C.30).

### Theorem A (Euclidean OPE for $J^\mu J^\nu$ in covariant gauges)

**Hypotheses.**
- D1–D2, with $\xi\equiv\xi_R$ in a compact interval $\Xi\ni1$;
- fixed order r in $\alpha_s(\mu)$;
- integer $a\ge2$;
- the D-dimensional $\overline{\rm MS}$ basis.

**Claims.**
- **(A1) Expansion.** $\tilde G^T_{JJ;\Phi}-\sum_{d_O\le a}C_O(q;\mu,\xi)\tilde G_{[O];\Phi}=O(|q|^{1-a}\ln^k)$, uniformly in direction, on compact non-exceptional p-sets, and in $\xi\in\Xi$.
- **(A2) Coefficient form.** $C_O=|q|^{2-d_O}\times$ a polynomial of degree ≤ r in $L=\ln(q^2/\mu^2)$, whose coefficients are polynomials in ξ.
- **(A3) Renormalization.** $C^{\overline{\rm MS}}=C^{\rm bare}Z^{-1}$. Here $C^{\rm bare}$ is the sum over hard (AI) subgraphs of their DR Taylor coefficients.
- **(A4) Uniqueness.** In every sector satisfying (NE), the coefficients are unique.
- **(A5) RG equation.** In every such sector,
  $$(\mu\partial_\mu+\beta\partial_\alpha+\beta_\xi\partial_\xi)C_i=\sum_jC_j\gamma_{ji}(\alpha,\xi).$$

**Proof.**
- **(A1), (A3).** Apply K2 graph by graph and in operator form for each fixed ξ, and substitute $O_{\rm bare}=Z^{-1}[O]$. IR finiteness of $\tilde G_{[O]}$ follows from K1.
  - Uniformity in ξ: at fixed order the remainder is a polynomial in ξ of bounded degree. Lagrange interpolation at finitely many values of ξ bounds every coefficient.
- **(A2).** At fixed ε the k-loop hard part, in bare $(g_0,\xi_0)$, is exactly homogeneous of degree $2-d_O-2k\varepsilon$.
  - Substitute the coupling renormalization, the gauge-parameter renormalization **$\xi_0=Z_3\xi$**, and $Z^{-1}$.
  - This gives $|q|^{2-d_O}\sum_kc_k(\varepsilon,\xi)(\mu^2/q^2)^{k\varepsilon}$, with poles of order ≤ r.
  - Finiteness forces a polynomial of degree ≤ r in L.
- **(A4).** Lemma A.3(b).
- **(A5).**
  1. Let $\mathcal D=\mu\partial_\mu+\beta\partial_\alpha+\beta_\xi\partial_\xi+\sum_{\rm legs}\gamma_\phi$. This is the total μ-derivative at fixed bare $(g_0,\xi_0)$.
  2. Then $\mathcal D\tilde G^T=0$, because J is not renormalized, and $\mathcal D\tilde G_{[O_i]}=-\sum_j\gamma_{ij}\tilde G_{[O_j]}$.
  3. Applying $\mathcal D$ to (A1) gives $\sum_i(\hat{\mathcal D}C_i-\sum_jC_j\gamma_{ji})\tilde G_{[O_i]}=-\mathcal D\mathcal R$, with $\hat{\mathcal D}=\mu\partial_\mu+\beta\partial_\alpha+\beta_\xi\partial_\xi$.
  4. At fixed order, $\mathcal R$ is a polynomial in $\ln\mu$ and in ξ. Lagrange interpolation in both variables gives $\mathcal D\mathcal R=O(|q|^{1-a}\ln^k)$.
  5. The bracket has the structure (A2), so it vanishes by (A4).
  6. **Vacuum correlator.** The identity operator appears, with an inhomogeneous RG term from the additive renormalization of $\langle JJ\rangle$; E2–E3 therefore use the Adler function. ∎

**Why the ξ term is needed (correction of round 1).**
- Green functions with elementary legs depend on ξ already at one loop; the massless quark self-energy is ∝ ξ.
- $\beta_\xi(\alpha,1)\neq0$ (D1).
- So round 1's equation without $\beta_\xi\partial_\xi$ was not proved, and for ξ-dependent (alien) coefficients it is false in general.
- In Landau gauge $\beta_\xi=0$.

**Grade.**
- (A1), (A3): [A], cited (checked) for Smirnov 1990, with the scope limits of K2.
- (A2): [R, R_cond: A1, A3].
- (A4), (A5): [R, R_cond: A1, A3], restricted to (NE).
- Overall: [A]. The assembly is mine; the content is standard.

### Corollary A.5 (GI block in Feynman gauge) [R, R_cond: A1, A3, K3, GP]; content [A]

**Setting.** A sector satisfying (NE).

**Premises.**
- (K3) Aliens do not mix into GI operators: $\gamma_{AG}=0$.
- (GP) $\partial_\xi C^{GI}=0$ and $\partial_\xi\gamma_{GG}=0$.

**Claim.** At $\xi=1$,
$$(\mu\partial_\mu+\beta\partial_\alpha)C^{GI}_i=\sum_{j\in GI}C^{GI}_j(\gamma_{GG})_{ji}.$$

**Proof.** Take i ∈ GI in (A5). The alien terms drop because $\gamma_{AG}=0$, and the ξ term drops by (GP). ∎

**Status of (GP).**
- $\gamma_{GG}$: K3 (Kluberg-Stern–Zuber, Joglekar–Lee; abstracts).
- $C^{GI}$ for the twist-2 coefficients $C^{(n)}_{2,i}$, the only ones used downstream (through N2 in Thm 5.9): (GP) follows from three inputs.
  - Cor. F.2(a), which holds for every ξ near 1.
  - The ξ-independence of $T^{(j)}_2$. This is an on-shell amplitude with physical polarizations and DR LSZ factor 1; the standard BRST argument makes it [A].
  - The ξ-independence of $A^{(n)}_{i/j}=\sum Z_{GG}\cdot$tree (K3). Since $A^{(n)}=1+O(\alpha_s)$ is invertible, the coefficients follow.
- Other GI coefficients: [A] (Joglekar 1977 I, abstract).

### Remark A.6 (logic; corrects CLAIMS R-M26)

- **The claim.** R-M26 says that, by uniqueness, any proven momentum-space OPE discharges Ass. C.24.
- **Why it is circular.** lem:appM-uniqueness(a), applied to $\sum(\tilde C-C')G=\mathcal R'-\tilde N_a$, needs $\tilde N_a$ small, and that is C.24.
- **The DR route** needs no C.24.
- **The withdrawn draft claim** "C.24 follows from Smirnov + uniqueness" stays withdrawn.
- **The way out is Lemma A.7.** The slot verdict is now "not delivered (open)".

### Lemma A.7 (matching at p=0) [R, R_cond: CT-p]

**Setting.**
- The massive Euclidean model of spec §M.2 (reference App C.2): scalars and Dirac fermions with dimension-4 monomial interactions, so all couplings are dimensionless; BPHZ.
- The exact identity (reference C.22) in connected amputated Green functions: $\tilde G^T=\sum_{d_O\le a}\tilde C_O\tilde G_{N[O]}+\tilde N_a$.

**Premise (CT-p).**
- There are p-independent $C'_O(q;m)$ such that $\mathcal R':=\tilde G^T-\sum C'_O\tilde G_{N[O]}$ satisfies the following.
- Let $\mathcal H'_a$ be the span of the functions obtained from $\mathcal R'$ by finitely many $\partial/\partial p_j^\nu$, multiplications by $p_{j\mu}$ and applications of $m\partial_m$.
- Every $h\in\mathcal H'_a$ obeys $|h(q;p)|\le K_h|q|^{D-1-a}(\ln|q|)^k$ for $|q|\ge2$, at each order, uniformly in $\hat q$ and for p in compact sets **containing p = 0**.

**Conclusion.**
- asm:appM-remainder (= reference Ass. C.24) holds in per-order form.
- The per-order form suffices for thm:appM-scaling (ii)–(iv) and cor:appM-coordinate. Their proofs, reference Lemmas C.29 and C.30 (read), use only homogeneity in (q,p,m), O(4) covariance, and order-by-order linear independence. All three hold for the order-r sum.

**Proof.**
1. **Over-subtraction at p=0.** For every connected amputated graph Γ, $\partial^\alpha_p\tilde N_{a,\Gamma}(q;0)=0$ for $|\alpha|\le a-\sum_{E(\Gamma)}d_e$.
   - Let $\gamma_0$ be the maximal AB part, i.e. the bridgeless component of $\Gamma\cup\ell_x$ that contains $\ell_x$, with $\ell_x$ removed.
   - Every other part of Γ hangs off $\gamma_0$ through one bridge b.
   - A hanging tree without external legs has a 1PI leaf block with one external line. BPHZ subtracts it at its only allowed momentum, 0, so it vanishes.
   - A hanging tree with one external leg is an external-leg insertion, which is amputated.
   - So every hanging tree has at least two external legs, of total dimension $\ge2>d_b$.
   - Hence $\delta_a(\gamma_0)=a-\sum_{E(\gamma_0)}d_e\ge a-\sum_{E(\Gamma)}d_e$.
   - By reference Def C.21(b), $\gamma_0$ is subtracted by $(1-t_p^{\delta_a(\gamma_0)})$ in its external momenta, which are linear in p and vanish at p=0.
   - The other factors are smooth in p.
2. **Normalization matrix.** Let $M_{(E,\alpha),O}=\partial^\alpha_p\tilde G^E_{N[O]}(0)$, with rows $\sum_Ed_e+|\alpha|\le a$ and columns $d_O\le a$.
   - At order 0 only the vertex $V^E_O$ contributes. It is homogeneous of degree $d_O-\sum_Ed_e$.
   - So $M^{(0)}$ is block diagonal by dimension, with injective blocks, because a monomial is fixed by its vertex.
   - Choose rows such that $M^{(0)}_{\rm sq}$ is square and invertible.
   - $M_{\rm sq}=M^{(0)}_{\rm sq}+O(g)$ is then invertible as a formal power series, with q-independent entries.
3. **Matching.** We have $\sum_O(\tilde C_O-C'_O)\tilde G^E_{N[O]}=\mathcal R'-\tilde N_a$.
   - Take $\partial^\alpha_p$ at p=0 on the chosen rows. By step 1 the $\tilde N_a$ term drops.
   - So $\Delta C=M_{\rm sq}^{-1}(\partial\mathcal R'|_{p=0})_{\rm sq}$. At each order this is a finite, q-independent combination, hence $O(|q|^{D-1-a}\ln^k)$ by (CT-p).
   - The same holds for $(m\partial_m)^j\Delta C$: differentiate the identity; $m\partial_mM$ is q-independent.
4. **Conclusion.** $\tilde N_a=\mathcal R'-\sum\Delta C\,\tilde G_{N[O]}$. Every element of $\mathcal H_a$ is a combination of elements of $\mathcal H'_a$ and of $(m\partial_m)^i\Delta C$ times bounded smooth functions of p. ∎

**Status.**
- (CT-p) is not verified in the literature (K2).
- The lemma removes the circularity: the remainder is controlled at p=0 by the cited theorem, not by C.24.
- Position-space theorems (Keller–Kopper Thm 11; AZ as described) do not supply (CT-p).
- Proof here, following review r2-1's suggestion; no novelty claimed.

### Theorem B (BRST reduction of the OPE coefficients)

**Premises.** Bare DR at fixed generic small ε, **any bare $\xi_0$**, B off-shell, no $\gamma_5$, D-dimensional algebra.
- **(DR-WI)** $sJ=0$. For local monomials at non-exceptional momenta, exactly,
  $$\sum_i(-1)^{|X_1|+\dots+|X_{i-1}|}\langle TX_1\cdots(sX_i)\cdots X_n\rangle=0.$$
  This holds because the regularized action and measure are BRST-invariant ('t Hooft–Veltman; Breitenlohner–Maison).
- **(DR-SD), corrected.** With $\tilde\Phi=\prod_k\int d^Dx_ke^{ip_kx_k}\phi_k(x_k)$,
  $$\langle T(Y\cdot\partial^\alpha\delta_LS/\delta\phi)(y)\tilde\Phi\rangle=i\sum_{k:\phi_k=\phi}\epsilon_k(ip_k)^\alpha e^{ip_ky}\langle TY(y)\tilde\Phi_{\hat k}\rangle,\qquad \epsilon_k=(-1)^{|\phi|(|\phi_1|+\dots+|\phi_{k-1}|)}.$$
  - Derivation: $\int\mathcal D\phi\,\frac{\delta_L}{\delta\phi(y)}[Y\tilde\Phi e^{iS}]=0$ with the graded Leibniz rule. The factor $(-1)^{|\phi||Y|}$ occurs in both surviving terms and cancels.
  - The $\delta^{(D)}(0)$ terms vanish in DR.
  - Round 1 had $|Y|$ inside $\epsilon_k$. f5 confirms the corrected rule: 400/400 Grassmann tests pass, while the round-1 sign fails 18 tests.
- **(E_ε)** As in the register; [A].
- **(LBC)** K6 with Remark B.1.

**Conclusions.**
- **(B-i)** For every d ≤ a: $sX_d\in\mathcal E$, where $X_d=\sum_{d_O=d}C_OO$ (bare, D-dimensional).
- **(B-ii)** $X_d$ = GI + $s$-exact + EOM.
- **(B-iii)** With K3: $X_d=\sum c'_j[O^{GI}_j]$ + aliens, with $c'=cZ_{GG}^{-1}$ finite, and the $\overline{\rm MS}$ coefficients of "rest" operators vanish.
- **(B-iv)** Between physical states only GI operators survive. At twist 2 these are $O_q^{(n)},O_g^{(n)}$ (reference Lemma C.42).

**Proof.**
1. **Ward identity.** $sJ=0$ and DR-WI give $\sum_k\epsilon'_k\langle\mathcal J\phi_1\cdots(s\phi_k)\cdots\phi_n\rangle=0$, with $\epsilon'_k=(-1)^{\sum_{l<k}|\phi_l|}$.
2. **Non-merged parts.** Insert E_ε, with $Z=s\phi_k$ at $p_k$. Because O is bosonic, DR-WI turns the non-merged parts into $-\sum_OC_O\langle(sO)\Phi\rangle$.
3. **Merged parts.**
   - Moving $Z_k$ (parity $|\phi_k|+1$) next to $\mathcal J$ costs $(-1)^{(|\phi_k|+1)\sum_{l<k}|\phi_l|}$. Combined with $\epsilon'_k$ this gives exactly $\epsilon_k$ of DR-SD.
   - $C^{s\phi_k}$ depends on k only through the field type and $p_k$.
   - DR-SD therefore gives $M_\Phi=\langle\mathbb E(q)\Phi\rangle$, with
     $$\mathbb E(q)=-i\sum_\phi\sum_{O'}O'\cdot C^{s\phi}_{O'}(q;-i\partial)\,\delta_LS/\delta\phi.$$
   - Round 1's extra factor $(-1)^{|\phi||O'|}$ is dropped; it equals +1 anyway, because $|O'|=|\phi|+1$.
4. **Combined identity.** $\langle[-\sum C_O\,sO+\mathbb E(q)]\Phi\rangle=O(|q|^{1-a}\ln^k)$ for every Φ.
5. **Degree matching** in D-dimensional dimensions.
   - Write the bracket as $\sum_YK_Y(q)Y$ over a monomial basis of ghost number 1.
   - The order-$g_0^m$ part of $K_Y$ is $\propto|q|^{3-d^{(4)}_Y+\varepsilon c_{Y,m}}$, with $c_{Y,m}=n_{\phi,Y}-n_{g,Y}-2-m$. This follows from $[\mathcal J]=2-2\varepsilon$, $[s]=1$ and $[g_0]=\varepsilon$.
   - For merged terms with $Y=O'\partial^\alpha\delta S/\delta\phi$ this matches the dimension $d_\phi-1-d_{O'}-|\alpha|$ of the $p^\alpha$ coefficient of $C^{s\phi}_{O'}$.
   - Truncate at $d_O\le a$ and merged terms with $d^{(4)}_Y\le a+1$. Lemma A.3(a) (generic ε, so distinct exponents) gives $K_Y=O(|q|^{1-a}\ln^k)$.
   - The exponent exceeds $1-a$ for small $|\varepsilon|$, so $K_Y\equiv0$.
   - Hence $\sum_{d_O=d}C_O\,sO=\mathbb E_{d+1}\in\mathcal E$.
6. **LBC.** Apply LBC (Remark B.1) to each loop-order coefficient.
7. **Physical states.** EOM operators vanish on shell, and $\langle s\Lambda\rangle$ vanishes between physical states (KO). For partons at tree level this is direct. ∎

**Grade.**
- (B-i), (B-ii): [R, R_cond: E_ε].
- (B-iii): [R, R_cond: E_ε, K3]. K3 is abstract-level; BBH §8.6, checked, covers only its cohomological part.
- (B-iv): additionally KO.
- Content grade: [A].
- **Gauge convention.** B holds identically in $\xi_0$ at each order in $g_0$. It may therefore be used with $\xi_0=Z_3\xi_R$, $\xi_R=1$, as in Theorem A.
- **Novelty: not claimed.** Joglekar 1977 II treats the question at physicist's level (abstract).

**Correction to the reference's Prop C.44 (reworded).**
- C.44 is a valid conditional statement given (B1) and (B2) as formulated.
- The error is Rem C.45's claim that (B2) is "the direct generalization of Thm C.35" to Green functions with composite external legs.
- The direct generalization is E_ε. Its expansion of $\langle T\tilde T\phi_1\cdots(s\phi_k)\cdots\phi_n\rangle$ contains merged terms, namely hard subgraphs containing the non-linear vertex $s\phi_k$.
- (B2), as used in C.44's proof, omits them, so it is a stronger and unjustified hypothesis.
- With E_ε the same argument gives $sX_d\in\mathcal E$ instead of $sX_d=0$; LBC then restores the physical conclusion.
- The second identity of (B1) is trivially true in DR, because its left side vanishes (step 1).
- Round-1 withdrawals stand: the claim that the (B1) contact terms are false or log-carrying, and the novelty claim.

### Remark B.1 (LBC at formal D) [R, given K6 and classical invariant theory]

Theorem B applies LBC at non-integer D to formal-D local polynomials. Their indices are contracted with g ($g^\mu_\mu=D$) and with $\hat q$, and their Dirac structures are $\gamma^{[\mu_1\dots\mu_r]}$ of every rank, evanescent ones included.

Let $V^g$ be the finite-dimensional ℚ-space of such expressions of given 4D dimension, ghost number g and tensor type. Set
$$K=\{X\in V^0:sX\in\mathcal E\},\qquad L=GI\cap V^0+s(V^{-1})+\mathcal E\cap V^0.$$

1. **K and L are ℚ-subspaces, with L ⊂ K.**
   - s, the generators $\delta S/\delta\phi$ and the GI class are D-independent formal expressions.
   - D enters the formal algebra only through contractions $g^\mu_\mu$ and $\gamma^\mu\cdots\gamma_\mu$, which neither s nor products $Y\cdot\partial^\alpha\delta S/\delta\phi$ create when Y is written in the antisymmetrized basis.
2. **Specialization to integer dimension.** Take an integer $n\ge n_0$, where $n_0$ exceeds the number of index slots in $V$.
   - Specialization $D\to n$ is injective on V: by the second fundamental theorem for O(n), and because $\gamma^{[r]}$ for r ≤ n are independent.
   - By Pin(n)-averaging (s, $\mathcal E$ and GI are equivariant) and the first fundamental theorem ($\mathrm{Hom}(S,S)\cong Cl(n)$), every covariant element of the n-dimensional $\mathcal E$, GI or $s(\cdot)$ of this type is a specialization of an element of V.
3. **Integer-dimension LBC.** BBH (formulated in any spacetime dimension n), Henneaux 1996 and BHHS give LBC in dimension n. So $K(n)=L(n)$, and by step 2, $K=L$.
4. **Conclusion.** $X_d\in K\otimes\mathbb C$, with coefficients depending on $q^2$ and ε. Hence $X_d\in L\otimes\mathbb C$.
   - Canonical dimensions shift uniformly (D1), and s and $\mathcal E$ are homogeneous. So the three parts can be taken of the dimension and tensor type of $X_d$. ∎

### Theorem I = A + B + twist classification [A]

Statement as in §0(i).

**Gap analysis: four routes.**
1. **DR + Theorem B.** Complete modulo (A1), (A3) and E_ε at theorem level (O1), and K3.
2. **BPHZL.** Convergence is known (K1). A C.24-type remainder estimate is not contained in the sources I read. The designated sources are unread (O3), so their content is open.
3. **Flow equations (FHH/FH).** Rigorous for pure YM. QCD with Dirac fermions is open (O2).
4. **Hollands 2008.** Pure YM only, in the Epstein–Glaser framework.

**Missing for QCD with quarks:** theorem-level (A1), (A3) and E_ε for a gauge theory with ghosts and a composite spectator, plus K3 at full-text level.

## 4. Part II: from Euclidean to forward kinematics

### Lemma F.0 (forward 2-forest structure) [R, R_PT]; elementary

**Setting.** A connected graph with incoming p at $P_1$, $-p$ at $P_2$, q at $J_1$ and $-q$ at $J_2$, where $J_1\ne J_2$; and $p^2=0$.

**Statement.**
$$\mathcal F=Q^2(\hat F_0+\omega\hat F_1),\qquad \hat F_0=\sum_{T:c_q\ne0}\alpha^{E\setminus T},\qquad \hat F_1=-\sum_Tc_pc_q\alpha^{E\setminus T},\qquad c_p,c_q\in\{0,\pm1\}.$$
Hence ${\rm mon}(\hat F_1)\subset{\rm mon}(\hat F_0)$ and $|{\rm coef}|\le1$.

**Proof.** $-s_T=Q^2(c_q^2-c_pc_q\omega)$. ∎

### Lemma F.1 (Newton-polytope domination) [R]; proof here, tools standard

**Setting.** $\mathcal G_\lambda=\mathcal U+\hat F_0+\lambda\hat F_1$ with dominated $\hat F_1$; P = Newt($\mathcal U+\hat F_0$) full-dimensional; $|\lambda|\le r<1$.

**Claims.**
- **(a)** The integral and all Taylor-term integrals converge on a common open set.
- **(b)** $I(\lambda)=\sum\lambda^nI_n$.
- **(c)** The candidate poles do not depend on λ, and $\frac1{n!}\partial^n_\lambda I|_0=I_n$ after continuation.

**Proof.**
- (a) The coefficients lie in $|\arg|\le\arcsin r$ (Schultka Thm 3.1), and $s+m\in c\,{\rm int}P+nP\subset(c+n){\rm int}P$.
- (b) Use $\sum|\binom{-c}{n}|r^n\le(1-r)^{-|c|}$ and Tonelli–Fubini.
- (c) On Kaneko–Ueda cubes, $\mathcal G_\lambda=x^{m_\sigma}(f_{\sigma,0}+\lambda f_{\sigma,1})$ with ${\rm Re}(f_{\sigma,0}+\lambda f_{\sigma,1})\ge(1-r)f_{\sigma,0}>0$. Conclude by Gel'fand–Shilov continuation and the identity theorem. ∎

### Lemma F.6 (matroid form of Newt($\mathcal U+\hat F_0$); DR admissibility) [R]

**Status: known in substance; re-derived here in matroid form for the Lee–Pomeransky polytope.**

**Setting.** $G_0=G+e_q$, where $e_q$ joins $J_1$ and $J_2$. G has N lines and L loops.

**Claims.**
- **(a) Support.** $\hat F_0=\mathcal U(G/\{J_1{=}J_2\})$ and $\mathcal U(G_0)=x_q\mathcal U(G)+\hat F_0$. Hence ${\rm Newt}(\mathcal U+\hat F_0)\cong P(M^*(G_0))$, the base polytope of the cographic matroid, via the projection that drops $x_q$.
- **(b) Dimension.** $\dim=N+1-c(M(G_0))$. It is full iff $G_0$ is loopless and 2-connected.
- **(c) Facets.** Every facet has primitive inward normal u and $d_u=\min\langle u,\cdot\rangle$ of one of four types:
  - $e_e$, with d = 0;
  - $-\mathbb 1$, with d = $-(L+1)$;
  - $-\mathbb 1_F$, with d = $-r^*(F)\le-1$;
  - $\mathbb 1_{E\setminus F'}$, with d = $L+1-r^*(F'\cup e_q)\ge1$.

  So $d_u=0$ only for coordinate facets.
- **(d) DR admissibility.** For all powers with ${\rm Re}\,a_e>0$, polynomial numerators, dimension shifts, naive Taylor terms, and every $\omega\in\mathcal C$, the only D-independent candidate poles are $a_e\in-\mathbb N_0$.

**Proof** (unchanged from round 1).
- Deletion–contraction gives (a).
- Feichtner–Sturmfels Prop 2.4 gives (b), with Whitney's theorem.
- Feichtner–Sturmfels Prop 2.3 gives (c): every facet is cut out by one of the defining inequalities, mapped through the projection.
- For (d), use Schultka Thm 3.6 = BFP 2.4. Its coefficient cone condition holds for every $\omega\in\mathcal C$, because $1=((1+\omega)+(1-\omega))/2$. The poles lie on $\langle u_F,s\rangle-c\,d_F+d_F(\cdot)\in-\mathbb N_0$, and these depend on D unless $u_F=e_e$. ∎

**Attribution** (new; reviews r2-1 and r2-2).
- (a) is standard deletion–contraction. Compare the proof of Tellander–Helmer Thm 3.1 (Newt($\mathcal U$) is the cographic matroid polytope) and Walther Lemma 3.3 (momentous 2-forests form a matroid).
- (b)–(d) and (F3) are known. $\hat F_0$ is the second Symanzik polynomial of G with external vertices $\{J_1,J_2\}$ carrying ±q only, which is generic euclidean in the sense of Schultka Def 4.3. Then:
  - Thm 4.15, Prop 4.17 and Cor 4.18 give the facet presentation of Newt($\mathcal U\hat F_0$), and full dimension iff s-irreducible, which is equivalent to $G_0$ loopless and 2-connected;
  - Prop 4.29 gives the convergence domain (Speer 1975, Rem 4.30);
  - Thm 4.32 gives $I_G=\omega_G\prod\Gamma(\tilde\omega_\gamma)J_G$ with $J_G$ entire;
  - Prop 4.31 gives the vanishing of graphs that are not s-irreducible;
  - see also Borinsky Thm 32 and Arkani-Hamed–Hillman–Mizera.
- **The book's contribution** is only the application to the on-shell forward amplitude through the domination of Lemmas F.0–F.1.
- Lemma F.6 is dropped from any 本书新结果 candidacy.

**Checks.**
- f3: 21 explicit topologies and 1028 random multigraphs, exact, 0 failures.
- Reviewers: r1 116/116; r2 45/45; rv2_matroid 226/226; rv2_facets_d0 185 + 68; rv22_numeric (H): 9 explicit graphs and 360 random graphs by brute-force facet enumeration without qhull or matroid theory.

### Theorem F (forward on-shell DR amplitude) [R, R_PT] per graph

**Setting.** Γ is a connected graph of the amputated forward amplitude of a massless on-shell parton j ($p^2=0$) with the two currents.

**Exclusions.**
- **(i) Bridges carrying ±p.** These are external-leg corrections, removed by amputation. The on-shell self-energy is scaleless, so LSZ = 1.
- **(ii) Bridges carrying exactly 0.** By fermion and ghost number such a bridge is a gluon line. The side not containing the target legs (the current side, or a vacuum side) carries a single adjoint index, and its other insertions are colour singlets. It is therefore zero by colour invariance, graph by graph; **no target averaging is needed.**

**Definition.** The parametric (Lee–Pomeransky/Speer-type), analytically regularized integral at $p^2=0$.
- For real $|\omega|<1$ and $Q^2>0$ all coefficients of $\mathcal G_\omega$ are positive (Lemma F.0). The Minkowski parametric form carries $(\mathcal F-i0)$, and $\mathcal F>0$ on the orthant, so **the $i0$ is immaterial** and the integral equals the Feynman-$i\epsilon$ momentum integral.
- For other ω the integral is defined by the continuation in (F1).

**Components.** Any tensor component contracted with tensors polynomial in p. $\nu^{-k}$ prefactors are treated in Lemmas F.7 and F.8.

**Claims.**
- **(F1)** For $\omega\in\mathcal C=\mathbb C\setminus((-\infty,-1]\cup[1,\infty))$ the integral converges on an ω-independent open set, continues meromorphically with ω-independent candidate poles, and is holomorphic in ω. Every DR Laurent coefficient is holomorphic on $\mathcal C$.
- **(F2)** For $|\omega|<1$ each Laurent coefficient equals $\sum_n\omega^nI^{[k]}_n$, the series of naive Taylor terms, absolutely and locally uniformly convergent.
- **(F3)** If $G_0$ is not loopless and 2-connected, both sides are scaleless and hence zero.

**Proof** (unchanged).
- Tarasov reduction, then Lemma F.0.
- For ${\rm Im}\,\omega\ne0$ the coefficients $\{1,1\pm\omega\}$ lie in an open half-plane. Newt is unchanged, so Schultka Thm 3.1 applies, and Kaneko–Ueda cubes give joint holomorphy.
- (F2): Lemma F.1, plus the pointwise equality of parametric and naive momentum-space Taylor terms (Schwinger + Gaussian). Restrict to DR by Lemma F.6(d).
- (F3): degenerate Newt are invariant under a scaling $t^u$, and so are the Taylor terms. ∎

**Status (narrowed).**
- Theorem F is the book's rigorous proof (本书给出的严格证明) of the **analytic step** of the method of projectors: per graph, the on-shell forward DR amplitude is holomorphic on $\mathcal C$ and equals its convergent naive Taylor series in p for $|\omega|<1$.
- The literature uses this step without proof: Gorishny–Larin–Tkachov PLB 124 (1983) 217; Gorishny–Larin NPB 283 (1987) 452; Larin–van Ritbergen–Vermaseren NPB 427 (1994) 41; Larin–Nogueira–van Ritbergen–Vermaseren NPB 492 (1997) 338.
- The "rearrangement of IR and UV divergences" of LNvRV, i.e. the identification with $\overline{\rm MS}$ coefficient functions, is Cor. F.2 and stays [A].
- Related rigorous work, not covering this case: Semenova–Smirnov–Smirnov 2019; Jantzen 2011.
- A 本书新结果 marker needs the WRITER_SPEC §6.5 second check: Tkachov 1992–97; Smirnov's books; Nilsson–Passare/BFP; Schultka §4; Borinsky; AHM; Tellander–Helmer; Walther.
- Independent tests: r2-1's one-loop box with all powers free (rv21_box: Taylor terms agree to 3e-27; series = integral at four complex ω; holomorphic off the disk).

### Lemma F.7 (projection onto $T_2$ in D dimensions) [R, R_PT]

**Setting.** T is the sum of forward graphs at fixed order and Laurent order, after the target spin sum.
- Quark: average with $\frac12\not p$.
- Gluon: average with $d_{ab}/(D-2)$, where $d_{ab}=-g_{ab}+(p_aq_b+q_ap_b)/\nu-q^2p_ap_b/\nu^2$. This tensor satisfies $d\cdot p=d\cdot q=0$, has trace $2-D$, and has degree 0 in p.

**(a) Projector.** T is transverse and lies in ${\rm span}\{g,pp,pq,qp,qq\}$. Then
$$T_2=\frac{Q^4[(D-1)S_1-(\nu^2/Q^2)S_2]}{(D-2)\nu^3},\qquad S_1=ppT,\quad S_2=gT$$
(f4 a; rv22 (A)).

**(b) Quark target (proof replaced).**
- By the first fundamental theorem (formal D; no ε-tensor without $\gamma_5$), the n-th naive term $T_n$ is a polynomial tensor of degree n in p, built from g, q and p.
- With $p^2=0$:
  $$T_n=a\nu^ng+b\nu^{n-2}pp+c\nu^{n-1}pq+c'\nu^{n-1}qp+e\nu^nqq,$$
  where a, b, c, c′, e depend on $q^2$ only, and polynomiality forces b = 0 for n < 2.
- By D6, $T_2=\nu\times$(coefficient of $p^\mu p^\nu$). So the n-th term of $T_2$ is $b\nu^{n-1}$: zero for n ≤ 1, and O(ν) for n ≥ 2.
- Hence the $\omega^{-3},\dots,\omega^0$ terms of the projector formula cancel for every n. f4 b (n ≤ 8) and rv22 (B) (n ≤ 4) are consistency checks.
- Conclusion: $T_2$ is holomorphic on $\mathcal C$, odd, and O(ω), and its Taylor series is the naive series.

**(c) Gluon target.**
- $T=H_0+H_1/\nu+H_2/\nu^2$, with Theorem F applying to each $H_k$.
- So $T_{1,2}$ are meromorphic on $\mathcal C$, holomorphic on $\mathcal C\setminus\{0\}$, and have the termwise naive Laurent expansion.
- Regularity at 0: Cor. F.2 ([A]) or Lemma F.8 ([R, R_cond: OS-WI]).
- f4 c: at tree level $T_2=4\omega/(1-\omega^2)$ and $T_1=2\omega^2/(1-\omega^2)$, independent of D. ∎

### Corollary F.2 (forward partonic OPE at every order) [A]

**Premises.** Theorem F and Lemmas F.6–F.7; (A3); Theorem B; K3; the twist classification.

**(a)** At every order and Laurent order, for $|\omega|<1$: $T^{\mu\nu}_j=\sum_OC^{\mu\nu}_O\langle j|[O]|j\rangle$, with only twist-2 GI operators and $A^{(n)}_{i/j}=\sum Z\cdot$tree. In particular
$$T^{(j)}_2=4\sum_{n\,\rm even}\omega^{n-1}\sum_iC^{(n)}_{2,i}A^{(n)}_{i/j}$$
(for gluons, $T_2^{(g)}$ is regular at 0).

**(b)** For every N there are C, k such that, for all Euclidean q with **$|q|\ge4p^0$**, uniformly in direction,
$$\Big|T^{\mu\nu}_j-\sum_{d_O\le N}C^{\mu\nu}_O\langle j|[O]|j\rangle\Big|\le C|q|^{1-N}(1+\ln|q|)^k.$$

**Proof.**
1. **Graphs.** The forward graphs are exactly the AI two-leg hard graphs: a bridge of $G_0$ carries 0 or ±p.
2. **Naive terms.** By Theorem F and Lemma F.7 the naive terms sum to $\sum_OC^{\rm bare}_OV_O(p,-p)$, contracted with the spin tensor. Bare on-shell matrix elements equal trees, because loops are scaleless.
3. **Renormalization.** $C^{\rm bare}=C^{\overline{\rm MS}}Z$. Theorem B and K3 give that "rest" coefficients vanish, GI operators mix into GI + aliens, and aliens mix only into aliens.
4. **Aliens (reconciled with CLAIMS R-M24).** Their contributions vanish here because of three facts:
   - p² = 0 exactly in DR, so all loop matrix elements are scaleless and $\langle[O_A]\rangle=Z_{AA}\cdot$tree;
   - the **physical** average $d_{ab}$ makes the contracted alien tree vertices vanish (EOM vertices are ∝ $p^2$ or $p_a$; B legs are ∝ $p_a$; $d_{ab}p^b=0$; there are no external ghosts) — with $-g_{ab}$ they would not vanish;
   - K3.

   This is not a claim about off-forward, off-shell or IR-regulated matrix elements, where aliens do contribute (Hamberg–van Neerven; Collins–Scalise; Falcioni–Herzog). Evanescent operators do not contribute either: the spin-averaged forward tree matrix elements of $\gamma^{[r\ge2]}$ structures built from p alone vanish.
5. **GI two-gluon vertices** are transverse in each leg, so $d_{ab}V^{ab}_O=-g_{ab}V^{ab}_O$ is polynomial; Lemma F.7(b) then gives gluon regularity at 0.
6. **Twist.** With $p^2=0$ only twist 2 survives, with finite coefficients by (A3).
7. **The bound (b), with sharpened constants** (rv22 (G)).
   - $|\nu|\le p^0|q|$, so $|\omega|\le2p^0/|q|\le\frac12$.
   - $|\hat P|^2_E=2(p^0)^2-|\nu|^2/Q^2\le2(p^0)^2$.
   - Cauchy estimates on $|\omega|=3/4$ give tails $O(\ln^K|\omega|^{N-1})$ for $T_1$ and $O(\ln^K|\omega|^{\max(N-3,0)})$ for $T_2/\omega$.
   - With $T=-\tilde gT_1+2\hat P\hat P(T_2/\omega)/Q^2$ this gives $|q|^{1-N}$. ∎

**Status.** asm:appM-forward is **reduced** to (A3) + E_ε + Theorem B + K3, not discharged; prop:dis-ope-forward stays [A]. One-loop instances: c_dis, $N\le8$.

### Lemma F.8 (gluon regularity from the on-shell Ward identity) [R, R_cond: OS-WI]; content [A]; new

**Premise (OS-WI).** At each order and Laurent order, the amputated forward DR amplitude $M^{\mu\nu}_{ab}(p,q)$ of an on-shell gluon (incoming a, outgoing b, $p^2=0$) satisfies
$$p^aM_{ab}\varepsilon^b=0=\varepsilon^aM_{ab}p^b\quad\text{for every }\varepsilon\text{ with }\varepsilon\cdot p=0.$$

**Claim.** The naive terms of $d^{ab}M_{ab}$ are polynomial in p. Hence $T^{(g)}_2$ is holomorphic on $\mathcal C$, regular at ω=0, and its Taylor series is the naive series. Theorem B is not needed.

**Proof.**
1. Apply OS-WI at $\lambda p$ and expand by (F2). This gives $p^aM_{n,ab}\varepsilon^b=0$ for each naive term.
2. For fixed μν, the vector $V^{\mu\nu}_b:=p^aM^{\mu\nu}_{n,ab}$ annihilates $p^\perp$, so it is ∝ $p_b$.
   - By the first fundamental theorem, V is a combination of the independent structures built from g, p, q, with coefficients polynomial in ν and $q^2$.
   - Being ∝ $p_b$ means $V^{\mu\nu}_b=\alpha^{\mu\nu}_np_b$, with $\alpha_n$ a polynomial tensor.
   - Likewise $M^{\mu\nu}_{n,ab}p^b=\alpha'^{\mu\nu}_np_a$.
3. With $p^2=0$: $d^{ab}M_{n,ab}=-g^{ab}M_{n,ab}+\alpha_n+\alpha'_n$, which is polynomial and transverse. Lemma F.7(b) applies. ∎

**Status of OS-WI.** It is the standard on-shell BRST identity: the longitudinal state is BRST-exact, states with $\varepsilon\cdot p=0$ are BRST-closed, and J is BRST-invariant. Deriving it from DR-WI needs either the $p^2\to0$ limit of the Slavnov–Taylor identity or an integrand-level graphical proof (compare Example F.4 for non-uniform limits). Neither is verified here, so it is [A]. Gluon regularity thus has two independent [A] supports.

### Corollary F.3 (perturbative cut-plane structure)

- **(a)** The Laurent coefficients of the partonic $T^{(j)}_2$ are holomorphic on $\mathcal C$:
  - quarks: [R, R_PT] (Lemma F.7(b));
  - gluons on $\mathcal C\setminus\{0\}$: [R, R_PT];
  - gluons at ω=0: **[A]** (Cor. F.2, or Lemma F.8 with OS-WI).
- **(b)** [A]: ${\rm Disc}\,T_2^{(j)}=4\pi iF_2^{(j)}(1/\omega)$, by DR cutting rules for Laurent coefficients; it becomes a definition if $F_2$ is defined as Disc/($4\pi i$).
- **(c)** [A]: the moment identity for even $n>A+1$ needs fixed-order growth bounds (O4).
- c_dis verifies the moment identity at one loop for N ≤ 8 (exact in ε).
- **WITHDRAWN** (round 1): one loop for all n. X3c is not delivered.

### Example F.3 (one-loop triangle) [R, R_PT]

- $I=\frac{\Gamma(a-\frac D2)}{\prod\Gamma(a_i)}(Q^2)^{\frac D2-a}B(\frac D2-a_2,\frac D2-a_1-a_3)B(a_1,a_3)\,{}_2F_1(a-\frac D2,a_1;a_1+a_3;\omega)$.
- The $\omega^n$ coefficient equals the naive term identically in $(a_i,D)$ (f2).
- At $a_i=1$ each term has the pole $-1/((n+1)\varepsilon)$.
- f2 quadrature point 2 agrees to $1.2\times10^{-5}$; the exact-y evaluation agrees to $10^{-12}$.

### Example F.4 (non-uniformity) [R, R_PT]

$Q^2I=\ln(Q^2/P^2)+2+O(P^2\ln)$ for $p^2=-P^2$, while the on-shell DR value is a pure pole.

### Remark F.5 [A]

- Zero-momentum insertions of $O^{(n)}$, n ≥ 2, into $p^2<0$ two-point functions are expected to be IR finite by Breitenlohner–Maison II.
- The hypotheses of BM II for this situation were not checked (O10).
- This indicates, but does not settle, the reference's Rem C.37.

### Lemma 4.10 (logic)

- Beyond W1–W3 the hadronic step uses only the segment approximation N1 on $\mathcal I_Q$.
- No perturbative statement implies N1.
- M > 0 removes the exceptional-momentum obstruction.

## 5. Part III: hadron-level DIS

All statements are unchanged except Lemma 5.5(c), which is new, and step 6′(ii) of Prop. 5.6, which uses it.

### Assumptions

- **W1.** Wightman framework. $J^\mu$ is hermitian, local, covariant, conserved and tempered; parity holds.
- **W2** (corrects ERR-M25). A stable spin-½ target of mass M, in the superselection sector of its flavour numbers, with ${\rm spec}\subset\{p^2=M^2\}\cup\{p^2\ge M_1^2\}$, $M_1>M$, which needs $m_\pi>0$. Only ${\rm spec}\subset\{p^2\ge M^2\}$ is used.
- **W3.** The spin-averaged connected forward commutator is tempered and has a retarded part R with:
  - support in $\bar V_+$ and $R-A=C$;
  - crossing $A^{\mu\nu}(z)=R^{\nu\mu}(-z)$;
  - covariance, parity and $q_\mu\tilde R^{\mu\nu}=0$;
  - freedom up to polynomials in q.
- **N1** (segment approximation, for a given even n). There are $N\ge\max(n+3,n_0+2)$ and constants $Q_0,K,k$ such that for $Q\ge Q_0$ some odd $P_N=\sum_{m\le N-2,\ \rm even}\pi_m\omega^{m-1}$ satisfies:
  - (a) $\sup_{\mathcal I_Q}|T_2-P_N|\le K(M/Q)^{N-2}\ln^kQ$;
  - (b) $|\pi_m|\le K\ln^kQ$;
  - (c) $\pi_n=4\sum_iC^{(n)}_{2,i}A^{(n)}_i+O((M^2+mM)Q^{-2}\ln^k)$.
- **N1-std** (standard non-perturbative OPE). On Euclidean q, $T=\sum_{d_j\le N}\tilde C_j\langle P|O_j|P\rangle+O(|q|^{1-N}\ln^k)$, with:
  - covariant coefficients bounded by $K|q|^{2-d_j}\ln^k$;
  - finitely many operators in each dimension;
  - twist ≥ 2, and twist 2 spanned by $O_q,O_g$;
  - odd-twist coefficients ≤ $Km|q|^{1-d}\ln^k$.
- **N2.** Twist-2 RG with $\gamma^{(n)}$ asymptotic to $\overline{\rm MS}$, $\beta=-b\alpha^2(1+o(1))$ with b > 0, and coefficients asymptotic to $\overline{\rm MS}$ perturbation theory.
- **N3.** PDFs exist.
- **G.** $\lim_{y\to\infty}T_2(iy)/(iy)=0$.
- **Φ.** x-space measures with the twist-2 moments exist.

### Lemmas

- **Lemma 5.1 [R, R_def].** $\hat P^2=M^2\mathbf q^2/Q^2\ge M^2/4$, and $\omega=2iMq^4/Q^2$ covers $\mathcal I_Q$ (h1 c).
- **Lemma 5.2 [R, R_cond: N1-std].** N1-std implies the segment approximation for all N.
  - Transversalize with $\Pi=g-qq/q^2$. Then $|\Pi_2|\le CQ/M$ on $\mathcal I_Q$.
  - Corrections: twist 2 is leading; trace terms are $M^2/Q^2$; chirally suppressed twist 3 is $mM/Q^2$; twist ≥ 4 is $M^2/Q^2$.
  - Without chiral suppression the error is O(M/Q).
  - This re-proves reference Lemma C.47.
- **Lemma 5.3 (Markov) [R].** For odd h of degree ≤ $D_g$: $|h_k|r^k\le2(1+\sqrt2)^{D_g}\sup_{|y|\le r}|h(iy)|$.
- **Lemma 5.4 (Jensen) [R].** If f is entire with $|f|\le C(1+|z|)^A|{\rm Im}\,z|^{-B}$, then f is a polynomial of degree ≤ A.
- **Lemma 5.5 [R].**
  - **(a)** Let f be holomorphic on $0<{\rm Im}\,z<1$ with $|f|\le C(1+|z|)^A({\rm Im}\,z)^{-B}$. Then the boundary value obeys $|\langle f(\cdot+i0),\chi\rangle|\le C'\sum_{j\le\lceil B\rceil+1}\int(1+|x|)^A|\chi^{(j)}|$, and a positive jump measure has $\nu([R,2R])\le CR^{A+1}$.
  - **(b)** One-dimensional distributional edge of the wedge, via K-fold primitives.
  - **(c) New: boundary values along curved approaches.**
    - *Setting.* $X\subset\mathbb R^m$ open; $\Gamma\ne\mathbb R^m$ an open convex cone; f holomorphic on $X+i(\Gamma\cap B_\gamma)$ with $|f(x+iy)|\le C|y|^{-N}$; $f_0$ its boundary value (Hörmander Thm 3.1.15).
    - *Approach maps.* Let $\Gamma'$ be a closed cone with $\Gamma'\setminus0\subset\Gamma$, and $X'\Subset X$. Let $\Theta_\eta:X'\to\mathbb C^m$, $0<\eta\le\eta_0$, be smooth, with ${\rm Im}\,\Theta_\eta\in(\Gamma'\setminus0)\cap B_{\gamma/2}$ and $\Theta_\eta\to{\rm id}$ in $C^\infty(X')$.
    - *Claim.* $\int f(\Theta_\eta(x))\varphi(x)\,dx\to\langle f_0,\varphi\rangle$ for every $\varphi\in C^\infty_0(X')$.
    - *Proof.*
      1. Fix $Y\in\Gamma$ small. Taylor's formula for $s\mapsto f(z+isY)$ at s = 1 gives $f=\sum_{k\le N}\frac{(-i)^k}{k!}L^kf_Y+L^{N+1}H$, where $L=Y\cdot\partial_z$, $f_Y=f(\cdot+iY)$ and $H(z)=\frac{(-i)^{N+1}}{N!}\int_0^1s^Nf(z+isY)\,ds$.
      2. $f_Y$ is holomorphic near $\bar X'$.
      3. H is continuous up to the edge on $\Gamma'$. Since Γ lies in an open half-space $\{\langle n,\cdot\rangle>0\}$, we have $|y+sY|\ge cs$, so $s^N|f|$ is bounded and dominated convergence applies.
      4. For holomorphic H, $(L^{N+1}H)\circ\Theta_\eta=(a_\eta\cdot\partial_x)^{N+1}(H\circ\Theta_\eta)$ with $a_\eta=(D\Theta_\eta)^{-1}Y\to Y$ in $C^\infty$.
      5. Integrate by parts and use the uniform continuity of H. The limit is $\sum_kc_k\int(L^kf_Y)\varphi+\int H_0\,((Y\cdot\partial)^{N+1})^t\varphi$, which does not depend on Θ.
      6. Choosing $\Theta_\eta=x+i\eta Y'$ identifies the limit with $f_0$. ∎

### Prop 5.6 (dispersion relation) [R, R_cond: W1–W3]

**Claims.**
- (a) $T_2(\omega,Q^2)$ is holomorphic and odd on $\mathcal C$.
- (b) $|T_2|\le C_Q(1+|\omega|)^A|{\rm Im}\,\omega|^{-B}$, with A, B independent of Q.
- (c) ${\rm Disc}\,T_2=4\pi i\nu_Q$, where $\nu_Q=F_2(1/\omega)d\omega\ge0$ on $[1,\infty)$, for **every** $Q^2$.
- (d) For even $n_0>A+1$,
  $$T_2=\sum_{n<n_0}t_n\omega^{n-1}+4\omega^{n_0-1}\int_{(0,1]}\frac{x^{n_0-2}F_2\,dx}{1-x^2\omega^2},$$
  so $t_n=4M_2^{(n)}$ for $n\ge n_0$.

**Proof.**
1. **Tubes.** $T=i\tilde R$ on the forward tube, with Vladimirov bounds.
2. **Oddness.** Crossing makes $T_2$ odd.
3. **Slice holomorphy.** $S_1,S_2$ are even in s on the slice $q=(w,0,0,s)$. The root with ${\rm Re}\,s>0$ of $s^2=w^2+Q^2$ has $|{\rm Im}\,s|<{\rm Im}\,w$.
4. **The point w = iQ is removable** (h1 d).
5. **Bounds.** From the slice inequality, $A=a+2b+2$ and $B=b$ (h1 e).
6. **Jump.** $i(\tilde R-\tilde A)=4\pi iW$, and $W=0$ for $|\omega|<1$ by W2.

6′. **Slice restriction.**
- **Local wedge.** For complex $Q^2$ near $Q_0^2>0$, the domain $|{\rm Im}\,s|<{\rm Im}\,w$ contains a wedge $\mathcal W=U+i(\Gamma'\cap B_\gamma)$ in the coordinates $(w,Q^2)$. Its cone contains the directions (1,0) and (1,−2x). To first order the condition reads $|\eta_Q+2x\eta_w|<2\sqrt{x^2+Q^2}\,\eta_w$, and the second-order terms are dominated on compact subcones (rv22 (W)).
- **Bound.** $|F|\le C|{\rm Im}|^{-B}$ there.
- **(i) Slice boundary values.** A K-fold primitive in w with K > B gives $F(\cdot+i0,Q^2)$ for every $Q^2$, weakly continuous in $Q^2$; and $\int dQ^2\langle F(\cdot+i\eta,Q^2),\psi\rangle\to\int dQ^2\langle F(\cdot+i0,Q^2),\psi\rangle$.
- **(ii) Identification with the 4D boundary value (repaired).** Pair the 4D boundary value $\lim_{\eta\to0}i\tilde R(q+i\eta e_0)$ with $\varphi\in C^\infty_0$ supported away from $\mathbf q=0$. Average over SO(3) and substitute $(q^0,|\mathbf q|)\mapsto(x,s)=(q^0,|\mathbf q|^2-(q^0)^2)$, with Jacobian $2|\mathbf q|$. This gives $\iint\psi(x,s)F(\Theta_\eta(x,s))$, with $\Theta_\eta(x,s)=(x+i\eta,\ s+\eta^2-2ix\eta)\to{\rm id}$ in $C^\infty$ and ${\rm Im}\,\Theta_\eta=\eta(1,-2x)\in\Gamma'$. By Lemma 5.5(c) the limit is the wedge boundary value $F_0$, which by (i) disintegrates into the slice boundary values.
- **(iii) Every slice.** By weak continuity, positivity and support hold for every $Q^2$; $D_{Q^2}=4\pi i\nu_Q$ (fixes E9). Lemma 5.5(b) then gives holomorphy on $\mathcal C$.

7. **Positivity.** $F_1\ge0$ and $F_2\ge\nu F_1/\hat P^2\ge0$.
8. **Growth.** $\nu_Q([R,2R])\le CR^{A+1}$, so $n_0>A+1$ suffices.
9. **Dispersion relation.** $H=T_2-\sum_{n<n_0}t_n\omega^{n-1}-D_{n_0}$ has no jump. Lemma 5.4 makes it a polynomial, and $H=O(\omega^{n_0-1})$ forces $H=0$. ∎

This re-proves reference Lemma C.64 with fixes; the explicit $n_0$ is new.

### Results

- **Theorem 5.7 [R, R_cond: W, N1].** For every even n ≥ 2, $t_n=4\sum_iC^{(n)}_{2,i}A^{(n)}_i+O((M^2+mM)Q^{-2}\ln^kQ)$.
  - Proof: the positivity tail is ≤ $2t_{n_0}r_Q^{N-1}$; apply Markov on $\mathcal I_Q$; bootstrap $t_{n_0}=O(\ln^k)$; use $(M/Q)^{N-1-n}\le(M/Q)^2$.
  - This re-proves reference Thm C.50 with a minimal hypothesis.
- **Prop 5.8 [R, R_cond: W].** Given (d) with $n_0\ge4$: $t_n=4M_2^{(n)}$ for all even $2\le n<n_0$ iff G holds.
  - Proof by descending induction, with $T_2(iy)/(iy)=\sum_{n<k-2}t_n(iy)^{n-2}+(iy)^{k-4}[t_{k-2}-4\int x^{k-4}F_2\frac{x^2y^2}{1+x^2y^2}]$.
  - A fixed pole cω is invisible in $F_2$.
- **Theorem 5.9 [R, R_cond: N2].** $C^{(n)}_{2,i}(Q^2/\mu^2,\alpha_s(\mu))=\sum_jC^{(n)}_{2,j}(1,\alpha_s(Q))[\mathcal P\exp(-\int_\mu^Q\frac{d\mu'}{\mu'}\gamma^{(n)})]_{ji}$.
  - The perturbative counterpart is Cor. A.5 (twist-2 GI block).
- **Theorem M [R, R_cond].** This refines reference Thm C.66.
  - (i) [W, N1] $t_n=4\sum CA+O((M^2+mM)Q^{-2}\ln^k)$ for every even n.
  - (ii) [W] $t_n=4M_2^{(n)}$ for $n\ge n_0$.
  - (iii) [+G] All even n ≥ 2, including the momentum sum rule; G is necessary.
  - (iv) [+N2] The RG-improved coefficients are asymptotic to perturbation theory.
  - (v) [+Φ] Weak x-space convergence.

## 6. Part IV: e⁺e⁻ and the Adler function (unchanged)

**Assumptions.**
- V1: W1 in the vacuum sector.
- V2: the non-perturbative OPE for D(Q²), with derivative bounds.
- V3: identity coefficient ≍ $R_0\sum d_ka^k$.
- V2′: V2 on a sector.

**Results.**
- **E1 [R, R_cond: V1].** Källén–Lehmann representation. The following are equivalent: one subtraction suffices; D is finite at one point.
- **E2 [R, R_cond: V1–V3].** $D=R_0[1+\sum d_ka^k]+O(a^{K+1})+O(m^2/Q^2)+O(\Lambda^4Q^{-4}\ln^k)$. There is no $1/Q^2$ term.
- **E3 [R, R_cond: V1–V3 + derivative bounds].** With $M_{k+1}=M_k-\frac{Q^2}{k}\frac{dM_k}{dQ^2}$: $M_k=R_0[1+d_1a+(d_2+H_{k-1}b_0d_1)a^2+O(a^3)]$, $b_0=\beta_0/4$ (e1 c, c′).
- **E4 [R, R_def].** $R=R_0[1+\kappa\sin(\sqrt s/\Lambda)]$ gives $D=R_0[1+\kappa\frac\pi2\frac Q\Lambda e^{-Q/\Lambda}]$. Known in spirit (Shifman; Blok–Shifman–Zhang).
- **E5 [R, R_cond: V1 + leading term].** Karamata Tauberian theorem; classical, no novelty claimed.
- **E6 [R, R_cond: V2′].** Poggio–Quinn–Weinberg contour average; known.

## 7. Verification log

All scripts were re-run on 2026-10-11.
- **f1–f4, h1, e1:** byte-identical with the stored logs. Reviewer r2-1 found the same at 04:53 (`rerun_x3_scripts.log`).
- **f5 (new).** Grassmann model (12 odd generators, exact rationals). The corrected DR-SD rule passes 400/400 tests; the round-1 rule with $|Y|$ fails 18 (all of them odd-Y cases with non-zero right side).
- **f6 (new).** Explicit Clifford matrices.
  - $\gamma^{[a_1..a_5]}\equiv0$ in D=4, and nonzero in D=5 and 6.
  - The tree-level hard part (s- plus u-channel) has rank-5 part exactly $2\gamma^{[\nu l\alpha q\mu]}$, to $9\times10^{-16}$. The k-terms cancel.
  - The $(\mu\nu)$-symmetric part has no rank-5 component.
  - With 4-dimensional kinematics the rank-5 part vanishes.
- **Reviewer checks used.**
  - rv21_box: one-loop forward box, all powers free; naive Taylor terms vs parametric terms agree to 3e-27; series = integral at four complex ω (≤ 4e-15; high precision for 0.8i); holomorphic at 1.5+0.7i, −2+0.5i and 2.5i.
  - rv22_algebra: (A)–(E), including the evanescent contraction $-D(D-1)(D-2)(D-3)(D-4)$.
  - rv22_numeric: (F) half-plane property; (G) constants; (W) wedge; (H) brute-force facets.
- **c_dis:** one loop, N ≤ 8, exact in ε.

## 8. Changes relative to the reference's App C and to CLAIMS

1. **Ass. C.24.** Not needed in the DR route. CLAIMS R-M26's "uniqueness discharges C.24" is circular (Remark A.6). The correct statement is Lemma A.7: a momentum-space theorem with p-derivative bounds at p=0 discharges C.24. A09(5) stays open, because the theory class of AZ is unverified.
2. **Prop C.44.** C.44 is valid as a conditional statement. Rem C.45 is wrong in calling (B2) the direct generalization of Thm C.35. With E_ε, $sX_d\in\mathcal E$ (Theorem B), and asm:appM-brst-ope is replaced by E_ε + LBC + K3.
3. **C.54(a), forward remainder.** Reduced to (A3) + E_ε + B + K3 (Cor. F.2). Theorem F is [R, R_PT].
4. **CLAIMS R-M24.** Consistent with Cor. F.2 step 4, which uses the physical polarization sum and exact on-shell DR.
5. **Rem C.37:** [A], pending O10.
6. **Hadronic part:** W2 (ERR-M25); E9 fixed (Lemma 5.5(c)); E10 avoided; $n_0$ explicit; the $\hat P=0$ point.
7. **C.58** replaced by N1. **Rem C.62** extended to E1–E6.
8. **RG equation of the coefficients** (spec prop:dis-ope-rg, derived from uniqueness). Needs the $\beta_\xi\partial_\xi$ term, or restriction to the GI block (Cor. A.5), together with (NE).

## 9. Spec patch instructions (for the spec_v2 update)

1. **X3a.** Delete the label prop:appM-remainder-discharge (not delivered). asm:appM-remainder stays [A].
   - New 地位 text: "uniqueness alone is circular; any momentum-space theorem with the (CT-p) bounds discharges it (Lemma A.7); the designated sources (Anikin–Zav'yalov 1976/1978, Zav'yalov 1979/1990, LS–dV 1988) were not examined (closed access); secondary sources describe them as position-space expansions".
   - Lemma A.7 may be printed in §M.4 as [R, R_cond].
2. **X3e.** Insert thm:appM-forward-expansion [R, R_PT] as the per-graph statement (Theorem F with Lemmas F.6 and F.7).
   - Do NOT set asm:appM-forward to 已解除. Its status line reads "reduced to (A3)+E_ε+Theorem B+K3 (Cor. F.2, [A])".
   - prop:dis-ope-forward stays [A].
   - Wording: "rigorous proof of the analytic step of the method of projectors".
3. **prop:dis-ope-gi.** Change the plan from "$X_d$ classically BRST closed" to "$sX_d\in\mathcal E$ (Theorem B) + LBC". Replace asm:appM-brst-ope by E_ε + LBC + K3.
4. **prop:dis-ope-rg.** Add $\beta_\xi\partial_\xi$, or restrict to the GI block under K3 + GP; add (NE).
5. **lem:appM-uniqueness(b), prop:dis-ope-euclid.** Add the (NE) caveat for D=4 uniqueness. Twist 2 is unaffected.
6. **Markers.** No 本书新结果 for Lemma F.6. Theorem F: "本书给出的严格证明" with the narrowed wording; 本书新结果 only after the §6.5 second check (list in §4).
7. **rem:appM-forward-aliens / ERR-M24.** Consistent with Cor. F.2 step 4.

## 10. Open problems

See the `open` list: O1–O13 updated, plus new items O14 (OS-WI) and O15 (GP).

## 11. Key references

- **K1–K12:** as listed in §2.
- **Also cited:**
  - forward-expansion literature: Gorishny–Larin 1987; Larin–van Ritbergen–Vermaseren 1994; Larin–Nogueira–van Ritbergen–Vermaseren 1997; Moch–Vermaseren–Vogt NPB 724 (2005) 3; Semenova–Smirnov–Smirnov EPJC 79 (2019) 136; Jantzen JHEP 12 (2011) 076;
  - Hamberg–van Neerven NPB 379 (1992) 143; Falcioni–Herzog JHEP 05 (2022) 177;
  - Kugo–Ojima 1979; 't Hooft–Veltman 1972; Poggio–Quinn–Weinberg 1976;
  - Lee–Pomeransky JHEP 11 (2013) 165; Tarasov PRD 54 (1996) 6479.

## 12. REVISIONS

### Fix round 2 (2026-10-11), responding to review_r2_1 (journal line 120) and review_r2_2 (journal line 119)

**Theorem A.**
- **R2-1 (r2-1, required).** (A5) used $\mathcal D\tilde G^T=0$ without the gauge-parameter term, which is wrong because $\beta_\xi(\alpha,1)\ne0$. Fixed in two ways:
  - Theorem A is now stated in covariant gauges ξ near 1, with $\beta_\xi\partial_\xi$ in (A5);
  - new Cor. A.5 gives the GI-block RG equation in Feynman gauge under K3 + GP, with GP derived for twist 2 from Cor. F.2 ([A]).

  The round-1 claim of (A5) without the ξ term for the full basis is **WITHDRAWN**. Also, $\xi_0=Z_3\xi_R$ is added to (A2).
- **R2-2 (r2-2, required).** Evanescent operators.
  - Lemma A.3 is split into (a), at generic ε, and (b), at D=4 under (NE).
  - (A4) and (A5) are restricted to (NE) sectors (D11).
  - **Partial disagreement with r2-2:** (NE) does not hold for all of $d_O\le5$. The $(\mu\nu)$-antisymmetric channel has a tree-level evanescent operator at $d_O=5$ (f6). It holds for the symmetric channel at $d_O\le5$ and for twist 2. DIS is unaffected.

**Slot X3a.**
- **R2-3 (r2-1, r2-2, required).** "FAILS as planned" becomes "not delivered (open)".
  - The designated sources were searched for: INSPIRE, OpenAlex, Springer, Elsevier, mathnet.ru and CDS. They are unobtainable and recorded as unread, with DOIs.
  - Secondary descriptions were read and quoted: Smirnov p. 110; Keller–Kopper p. 246; Tkachov footnote 14; Chetyrkin §6.
  - New Lemma A.7 closes the logical gap under (CT-p) (r2-1's suggestion, with a proof of the over-subtraction at p=0 for 1PR graphs).
  - The gap-analysis line on BPHZL is qualified. K2 now lists Anikin–Zav'yalov 1976/1978 and Anikin–(Karchev/Bordag)–Zav'yalov I–III. A09(5) stays open.

**Lemma F.6 and Theorem F.**
- **R2-4 (both, required).** Lemma F.6 is attributed to Schultka §4 (Def 4.3, Thm 4.15, Prop 4.17, Cor 4.18, Prop 4.29, Rem 4.30/Speer, Prop 4.31, Thm 4.32), Borinsky Thm 32, AHM, Tellander–Helmer and Walther, all checked in the downloaded texts. It is now marked "known; re-derived in matroid form" and dropped from novelty candidacy.
- **R2-5 (r2-2, required).** Theorem F's status is narrowed to the analytic step; the IR/UV rearrangement is Cor. F.2, [A]. The §6.5 check list is extended.

**Theorem B.**
- **R2-6 (r2-1 (i), r2-2 (ii), required).** New Remark B.1 justifies LBC at formal D, including evanescent structures, and D1 gives the ε-shifted dimensions. Step 5 is redone with D-dimensional dimensions.
- **R2-7 (r2-1 (ii)).** K3 added to R_cond for (B-iii).
- **R2-8 (r2-1 (iii)).** The C.44 critique is reworded: C.44 is valid as a conditional statement, and the error is in Rem C.45.
- **R2-9 (r2-1 (iv)).** Gauge convention: B holds for every $\xi_0$, used with $\xi_0=Z_3\xi_R$, $\xi_R=1$.
- **R2-10 (r2-2 item 5).** DR-SD sign corrected: $\epsilon_k$ without $|Y|$. The factor $(-1)^{|\phi||O'|}$ in $\mathbb E$ is dropped (it is ≡ 1; r2-1). f5 confirms.

**Corollaries F.2, F.3 and Lemmas F.7, F.8.**
- **R2-11 (r2-1, required).** Cor. F.3(a) tag split: quarks [R, R_PT]; gluons at ω=0 [A].
- **R2-12 (r2-2 item 9, optional).** The upgrade is taken as **conditional**: new Lemma F.8 [R, R_cond: OS-WI]. OS-WI itself is not proved at theorem level, so gluon regularity stays [A] and is not upgraded to [R, R_PT].
- **R2-13 (r2-2 item 6).** Lemma F.7(b): general-n proof replaces "the general case is the same linear algebra".
- **R2-14 (r2-2 item 3).** Cor. F.2 step 4 reconciled with R-M24. The spec patch records the X3e PASS as per-graph only and blocks the rule "asm:appM-forward 已解除".

**Prop 5.6.**
- **R2-15 (both, required).** Step 6′(ii) now uses the new Lemma 5.5(c) (boundary values along curved, x-dependent approaches; full proof) instead of Hörmander Thm 3.1.15 alone.

**Wording.**
- **R2-16 (r2-2 item 8).**
  - Lemma F.1(c): $x^{m_\sigma}(f_{\sigma,0}+\lambda f_{\sigma,1})$.
  - "Wick rotation" replaced by the $(\mathcal F-i0)$ remark.
  - Exclusion (ii) holds without target averaging.
  - Cor. F.2(b) constants sharpened: $|\omega|\le2p^0/|q|$, $|\hat P|_E\le\sqrt2p^0$, $|q|\ge4p^0$.

**Pipeline.**
- **R2-17 (both, O13).** This StructuredOutput is the complete report; the parent must save it and the two reviews. New scripts f5 and f6; logs in `logs/`.

**Rejected:** none. **Partially disagreed:** R2-2 (the scope of (NE)) and R2-12 (only a conditional upgrade).

### Fix round 1 (2026-10-11, summary)

- **Grades.** "[R-cited]" abolished. Theorem A [A]; Theorem B [R, R_cond: E_ε]; Cor. F.2 [A].
- **Literature.** Smirnov 1990 and Chetyrkin 1701.08627 read.
- **Proof repairs.**
  - (A5) argument completed (polynomial ln μ dependence, Lagrange interpolation, vacuum term).
  - Theorem B rewritten: exact LBC citations, merged terms, degree matching.
  - (F-DR) proven as Lemma F.6.
  - Spin sums handled by Lemma F.7.
  - Cor. F.2 bound derived by Cauchy estimates.
  - Prop 5.6 step 6′ made explicit.
- **Withdrawn:**
  - draft "C.24 from Smirnov + uniqueness";
  - "(B1) contact terms false/log-carrying";
  - Theorem B novelty;
  - one-loop all-n [R];
  - E5 novelty.
- **Scripts.** f1, f2, e1 documentation fixes; new f3, f4.

## results

### [results 1]
SLOTS (fix round 2). X3a: not delivered (open). The uniqueness-only route is circular (Remark A.6). The designated sources (Anikin-Zav'yalov 1976 and 1978, Zav'yalov 1979/1990, Llewellyn Smith-de Vries 1988) could not be obtained and are unread. The new conditional Lemma A.7 reduces asm:appM-remainder to a momentum-space theorem with p-derivative bounds at p=0 (CT-p); asm:appM-remainder stays [A]. X3b: not passed. X3c: not delivered. X3d: partial (QCD: E_eps + LBC + K3; pure YM not verified). X3e: PASS as a per-graph statement (Theorem F with Lemmas F.6 and F.7, [R, R_PT]), confirmed by both round-2 reviewers. Do NOT apply the rule 'asm:appM-forward 已解除'; asm:appM-forward is only reduced to A3 + E_eps + Theorem B + K3 via Cor F.2 [A], and prop:dis-ope-forward stays [A].

### [results 2]
lem:X3-A3 (linear independence). (a) At fixed generic eps in the D-dimensional basis: if sum_O c_O G_[O];Phi = O(|q|^rho ln^k) for all Phi, then c_O = O(|q|^rho ln^k), and graded-homogeneous c_O of degree > rho vanish. (b) The same at D=4 for renormalized functions, but only in sectors satisfying (NE) (no evanescent operators). Grade [R, R_PT]. Known in spirit (reference Lemma C.30).

### [results 3]
thm:X3-A (Euclidean OPE for J J; covariant gauge with xi near 1, Feynman gauge = xi_R = 1; DR + MS-bar; fixed order). (A1) remainder O(|q|^{1-a} ln^k), uniformly in direction and in xi. (A2) C_O = |q|^{2-d_O} times a polynomial in L whose coefficients are polynomial in xi; the proof includes xi_0 = Z_3 xi_R. (A3) C^MS = C^bare Z^{-1}. (A4) uniqueness and (A5) the RG equation (mu d_mu + beta d_alpha + beta_xi d_xi) C_i = sum_j C_j gamma_ji, both only in (NE) sectors. Grades: (A1), (A3) [A] (Smirnov CMP 134 checked, with scope limits); (A2), (A4), (A5) [R, R_cond: A1, A3]; overall [A]. WITHDRAWN: the round-1 (A5) without beta_xi d_xi, since beta_xi(alpha,1) = (alpha_s/2pi)(5 - 2n_f/3) is nonzero for SU(3).

### [results 4]
cor:X3-A5 (GI-block RG equation in Feynman gauge). In (NE) sectors, given K3 (gamma_AG = 0) and GP (C^GI and gamma_GG independent of xi): (mu d_mu + beta d_alpha) C^GI = C^GI gamma_GG at xi = 1. Grade [R, R_cond: A1, A3, K3, GP]; content [A]. For twist-2 coefficients GP follows from Cor F.2, the BRST gauge independence of on-shell physical amplitudes, and K3, all at grade [A]. Standard fact, stated here precisely.

### [results 5]
rem:X3-A6 (logic). CLAIMS R-M26 (uniqueness discharges Ass. C.24) is circular, because lem:appM-uniqueness(a) needs the frozen-q remainder to be small, which is C.24 itself. The DR route needs no C.24. Correct as stated.

### [results 6]
lem:X3-A7 (matching at p=0). Setting: the massive Euclidean model of spec §M.2, BPHZ. Suppose a momentum-space expansion G^T = sum C'_O G_N[O] + R' holds, with |h| <= K|q|^{D-1-a} ln^k for every h in the span of p-derivatives, p-multiplications and m d_m of R', uniformly in direction and for p in compact sets containing p = 0 (premise CT-p). Then asm:appM-remainder (Ass. C.24) holds per order, which suffices for thm:appM-scaling and cor:appM-coordinate. Proof: the frozen-q normal product is over-subtracted at p=0, including for 1PR graphs, and the normalization matrix is invertible. Grade [R, R_cond: CT-p]; CT-p is unverified. Proof here, following review r2-1; no novelty claimed.

### [results 7]
thm:X3-B (BRST reduction). Premises: DR-WI; DR-SD with corrected sign eps_k = (-1)^{|phi| sum_{l<k}|phi_l|} (checked by f5); E_eps for any bare xi_0; LBC (BBH/Henneaux/BHHS plus Remark B.1). Conclusion: sX_d lies in the EOM ideal, so X_d = GI + s-exact + EOM; with K3, the renormalized-basis form holds and the rest coefficients vanish; between physical states only GI operators survive, and at twist 2 only O_q, O_g. Grades: [R, R_cond: E_eps] for the bare statements, [R, R_cond: E_eps, K3] for the renormalized ones; content [A]. Novelty not claimed (Joglekar 1977 II). Correction to the reference: C.44 is valid as a conditional statement; the error is Rem C.45, whose (B2) omits the merged terms and so is not the direct generalization.

### [results 8]
rem:X3-B1 (LBC at formal D). K = {X : sX in E} equals GI + im s + E on formal-D covariant local polynomials, evanescent Dirac structures included. K and L are Q-subspaces; specialization to integer n >= n0 is injective (second fundamental theorem for O(n)); Pin(n) averaging plus the first fundamental theorem; integer-n LBC (BBH, valid in any dimension). Grade [R], given K6 and classical invariant theory. New argument for a standard step.

### [results 9]
thm:X3-I = A + B + twist classification (GI OPE for massless QCD with quarks). Grade [A].

### [results 10]
lem:X3-F0 (forward 2-forest structure). F = Q^2(F0 + omega F1), with mon(F1) contained in mon(F0) and |coef| <= 1. Grade [R, R_PT]. Elementary.

### [results 11]
lem:X3-F1 (Newton-polytope domination). The integral and all Taylor-term integrals converge on a common open set; I(lambda) = sum lambda^n I_n; candidate poles do not depend on lambda. Grade [R]. Proof here; tools standard (Schultka, BFP, Kaneko-Ueda).

### [results 12]
lem:X3-F6 (matroid form of Newt(U+F0); DR admissibility). Newt(U+F0) is the base polytope of the cographic matroid of G0 = G + e_q. It is full-dimensional iff G0 is loopless and 2-connected. Four facet types; d_u = 0 only for coordinate facets; DR is admissible for every omega in the cut plane. Grade [R]. KNOWN in substance: Schultka 1806.01086 §4 (Def 4.3, Thm 4.15, Prop 4.17, Cor 4.18, Prop 4.29, Rem 4.30/Speer 1975, Prop 4.31, Thm 4.32); Borinsky AIHPD 10 (2023) 635 Thm 32; Arkani-Hamed-Hillman-Mizera PRD 105 (2022) 125013; Tellander-Helmer CMP 399 (2023) 1021; Walther LMP 112 (2022) 120. Re-derived here in matroid form; no novelty.

### [results 13]
thm:X3-F = thm:appM-forward-expansion (forward on-shell DR amplitude, per graph). Setting: amputated forward amplitude of an on-shell massless parton; bridges carrying +-p are amputated; zero-momentum bridges vanish by colour without target averaging; parametric DR definition, where the (F - i0) prescription is immaterial. Claims: (F1) the Laurent coefficients are holomorphic on the cut plane; (F2) for |omega| < 1 they equal the convergent naive Taylor series; (F3) degenerate graphs vanish. Grade [R, R_PT] per graph. Status: the rigorous proof of the analytic step of the method of projectors (GLT 1983, GL 1987, LvRV 1994, LNvRV 1997). The identification with MS-bar coefficients is Cor F.2, [A]. Wording '本书给出的严格证明' is allowed; '本书新结果' waits for the §6.5 second check.

### [results 14]
lem:X3-F7 (T2 projection in D dimensions). T2 = Q^4[(D-1)S1 - (nu^2/Q^2)S2]/((D-2)nu^3) for transverse T. Quark target: the n-th naive term of T2 is b nu^{n-1}, which is zero for n <= 1, for every n (first fundamental theorem). So T2 is holomorphic on the cut plane and its Taylor series equals the naive series. Gluon target: meromorphic, holomorphic away from 0. Grade [R, R_PT].

### [results 15]
cor:X3-F2 (forward partonic OPE). T_j = sum C_O <j|[O]|j> for |omega| < 1, with only twist-2 GI operators and A = Z x tree. Bound: C|q|^{1-N} ln^k for |q| >= 4 p0, uniformly in direction, with sharpened constants |omega| <= 2p0/|q| and |Phat|_E <= sqrt2 p0. The alien step is reconciled with CLAIMS R-M24 (exact on-shell DR, physical polarization sum, K3). Grade [A], inheriting A3, Theorem B and K3.

### [results 16]
lem:X3-F8 (gluon regularity from the on-shell Ward identity). If p^a M_ab eps^b = 0 = eps^a M_ab p^b for every eps with eps.p = 0 (premise OS-WI), then the naive terms of d^ab M_ab are polynomial and T2^(g) is regular at omega = 0, without using Theorem B. Grade [R, R_cond: OS-WI]; OS-WI itself is [A]. New: the conditional form of review r2-2's suggested upgrade.

### [results 17]
cor:X3-F3 (partonic cut-plane structure). (a) Quarks [R, R_PT]; gluons on C minus {0} [R, R_PT], and at omega = 0 [A] (via Cor F.2 or Lemma F.8). (b) Disc T2 = 4 pi i F2: [A]. (c) Moments for even n > A+1: [A]. Withdrawn in round 1: the one-loop all-n claim.

### [results 18]
ex:X3-F3/F4 (one-loop checks). Forward triangle in closed form: the omega^n coefficient equals the naive term identically in (a_i, D), each term has the pole -1/((n+1)eps), and the off-shell limit is non-uniform. Grade [R, R_PT] at one loop (f2).

### [results 19]
rem:X3-F5 (zero-momentum insertions). Expected to be IR finite by Breitenlohner-Maison II; hypotheses not checked (O10). Grade [A].

### [results 20]
lem:X3-4.10 (the hadronic step needs only N1). Logic.

### [results 21]
lem:X3-5.1..5.5. Phat^2 >= M^2/4: [R, R_def]. N1-std implies the segment approximation: [R, R_cond]. Markov, Jensen and boundary-value lemmas: [R], known. NEW 5.5(c): boundary values along curved, x-dependent approaches equal the wedge boundary value; full proof extending Hormander Thm 3.1.15.

### [results 22]
prop:X3-5.6 (dispersion relation from W1-W3). T2 is holomorphic and odd on the cut plane, with Q-independent bounds. Disc = 4 pi i nu_Q >= 0 for every Q^2; the slice identification now uses Lemma 5.5(c). n0-subtracted relation, with t_n = 4 M2^(n) for n >= n0 > A+1. Grade [R, R_cond: W1-W3]. Re-proof of reference Lemma C.64 with fixes.

### [results 23]
thm:X3-M with Thm 5.7, Prop 5.8, Thm 5.9 (hadron-level DIS moments). (i) [W, N1] t_n = 4 sum C A + O((M^2+mM)Q^{-2} ln^k). (ii) [W] t_n = 4 M2^(n) for n >= n0. (iii) [+G] all even n; G is necessary. (iv) [+N2] RG-improved coefficients are asymptotic to perturbation theory. (v) [+Phi] weak x-space convergence. Grade [R, R_cond]. Refines reference Thm C.66; unchanged.

### [results 24]
E1-E6 (e+e-). Kallen-Lehmann and one subtraction [R, R_cond: V1]; Adler-function asymptotics with no 1/Q^2 term [R, R_cond: V1-V3]; Euclidean moments M_k [R, R_cond]; exact duality-violation counterexample [R, R_def]; Karamata Tauberian theorem [R, R_cond]; PQW smearing [R, R_cond: V2']. All known; unchanged.

### [results 25]
def:X3-NE (evanescent condition). (NE) holds for twist-2 symmetric traceless operators at every n, and for the (mu nu)-symmetric part when d_O <= 5. It fails at d_O = 5 in the (mu nu)-antisymmetric part (tree-level operator psibar gamma^[5] q F psi, shown by f6) and at d_O = 6 in the four-quark sector (rv22). Grade [R, R_def].

### [results 26]
VERIF. f1-f4, h1 and e1 re-run on 2026-10-11 and byte-identical. New f5: Grassmann check of the DR-SD signs; the corrected rule passes 400/400, the round-1 rule fails 18. New f6: rank-5 structure 2 gamma^[nu l alpha q mu]; its symmetric part and its 4D value are zero. Reviewer checks rv21_box, rv22_algebra and rv22_numeric were also used.

## open

### [open 1]
O1 (partly done). Smirnov 1990 has been read. Remaining: Gorishny 1989, Smirnov's 1991 book, and theorem-level proofs of the DR function form, direction uniformity, ghosts and E_eps. These would make A1, A3, Theorem B and Cor F.2 [R].

### [open 2]
O2. Flow-equation (FHH-type) existence and bounds for Yang-Mills with Dirac fermions, as an independent route to Theorem I.

### [open 3]
O3 (X3a, updated). Obtain and read Anikin-Zav'yalov TMF 27 (1976) 425 [10.1007/BF01028628], Ann. Phys. 116 (1978) 135 [10.1016/0003-4916(78)90007-6], Zav'yalov 1979/1990 (Wilson-expansion chapter), and Llewellyn Smith-de Vries NPB 296 (1988) 991. Record theory class, momentum or position space, uniformity, and p-derivative bounds at p=0. If they prove (CT-p) or the frozen-q momentum-space bound, Lemma A.7 or direct citation discharges asm:appM-remainder. CLAIMS A09(5) stays open.

### [open 4]
O4. Fixed-order polynomial growth bounds in omega for the partonic forward amplitude: the moment identity for all n, and absence of fixed poles.

### [open 5]
O4' (X3c). One-loop all-N forward identity.

### [open 6]
O5. Non-perturbative: construct 4D QCD and derive N1.

### [open 7]
O6. Derive the growth condition G (no real fixed pole c omega).

### [open 8]
O7. Convergence of the OPE for YM/QCD at fixed order.

### [open 9]
O8. Polarized structure functions: gamma5 breaks exact DR BRST invariance; this channel also has the antisymmetric evanescent operator. Theorem B must be extended.

### [open 10]
O9. Local duality and pointwise R(s); Tauberian remainder theorems.

### [open 11]
O10. Check the Breitenlohner-Maison II hypotheses for zero-momentum composite insertions (Remark F.5).

### [open 12]
O11. Renormalon / OPE-basis ambiguity (reference Prop C.68, Rem C.69).

### [open 13]
O12. Novelty checks before any 本书新结果 marker. Theorem F: Tkachov 1992-97, Smirnov's books, Nilsson-Passare/BFP, Schultka §4, Borinsky, AHM, Tellander-Helmer, Walther. Theorem B: full texts of Joglekar 1977 I/II and Collins 1984 §12.8. Pure-YM X3d: verify Hollands' construction.

### [open 14]
O13 (pipeline). The orchestrator must persist StructuredOutputs as REPORT.md and review files: X3 fix1 at journal line 112, rev2-2 at line 119, rev2-1 at line 120, and this fix2. Same for X1 and X2.

### [open 15]
O14 (new). Prove OS-WI, the on-shell BRST Ward identity for amputated forward DR amplitudes at p^2 = 0, at theorem level (integrand-level graphical proof, or a controlled p^2 -> 0 limit of Slavnov-Taylor identities). Lemma F.8 would then make gluon regularity at omega = 0 [R, R_PT].

### [open 16]
O15 (new). GP: xi-independence of all GI coefficients and of gamma_GG at theorem level (full texts of Kluberg-Stern-Zuber, Joglekar-Lee, Joglekar 1977 I). Also an evanescent prescription for (A4)/(A5) outside (NE) sectors (Dugan-Grinstein; Herrlich-Nierste).

## files

### [files 1]
/Users/hao-cheng/Desktop/theorem proof/qcd_factorization_work/verify/extend/X3-ope/REPORT.md (intended destination; NOT written by this subagent - parent should save this StructuredOutput summary there)

### [files 2]
/Users/hao-cheng/Desktop/theorem proof/qcd_factorization_work/verify/extend/X3-ope/scripts/f5_sd_signs.py

### [files 3]
/Users/hao-cheng/Desktop/theorem proof/qcd_factorization_work/verify/extend/X3-ope/scripts/f6_evanescent_tree.py

### [files 4]
/Users/hao-cheng/Desktop/theorem proof/qcd_factorization_work/verify/extend/X3-ope/logs/f5_sd_signs.log

### [files 5]
/Users/hao-cheng/Desktop/theorem proof/qcd_factorization_work/verify/extend/X3-ope/logs/f6_evanescent_tree.log

### [files 6]
/Users/hao-cheng/Desktop/theorem proof/qcd_factorization_work/verify/extend/X3-ope/scripts/ (f1-f4, h1, e1; re-run, logs byte-identical)

### [files 7]
/Users/hao-cheng/Desktop/theorem proof/qcd_factorization_work/verify/extend/X3-ope/review_r2_1_checks/ and review_r2_2_scripts/ (reviewer checks used)

### [files 8]
/private/tmp/claude-501/-Users-hao-cheng-Desktop-theorem-proof/c211c739-758d-4b40-bbac-67f4e1a65da4/scratchpad/x3fix3/draft_report_rev2.txt (temporary working copy of this report)

### [files 9]
/private/tmp/claude-501/-Users-hao-cheng-Desktop-theorem-proof/c211c739-758d-4b40-bbac-67f4e1a65da4/scratchpad/x3fix3/dl_kk/kk.txt (Keller-Kopper CMP 153 text)

### [files 10]
/private/tmp/claude-501/-Users-hao-cheng-Desktop-theorem-proof/c211c739-758d-4b40-bbac-67f4e1a65da4/scratchpad/x3fix3/dl_tk/tk.txt (Tkachov hep-th/9612037 text)

### [files 11]
/private/tmp/claude-501/-Users-hao-cheng-Desktop-theorem-proof/c211c739-758d-4b40-bbac-67f4e1a65da4/scratchpad/x3fix3/inspire/ (INSPIRE/OpenAlex queries for the X3a sources)
