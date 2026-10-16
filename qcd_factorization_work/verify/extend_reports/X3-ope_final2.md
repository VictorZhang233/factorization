# X3 (final2): OPE in massless QCD; DIS and e⁺e⁻ moments at hadron level (Appendix M)

This report supersedes X3-ope.md, X3-ope-fix1.md, X3-ope-fix2.md and X3-ope_final.md, and is complete in itself. It applies:
- the six required fixes of the final independent review `verify/extend_reports/X3-ope-finalreview.md` (mapping in §13);
- `writing/LEAD_DECISIONS.md`: LA-2 (pure-mathematics lemmas carry no tag), LA-4 (the zero-momentum-insertion statement, Prop. F.5), LA-7 (unverified locations; K5 resolved);
- the novelty-wording rule of WRITER_SPEC_v2 §6.5 (class K4): our derivations or proofs of published or classical results are 「本书给出的推导／证明」, never novelty claims.

The round-3 dispositions are kept in §12. LA-5 (X1 exponents) does not concern this report: it prints no X1 exponent. LA-2's rule for model theorems ([P], with the model named in the first sentence) has no instance here either. E4 is an explicit mathematical identity used as an illustration (now untagged), and Examples F.3–F.4 are exact one-loop QCD graph computations, not model theorems. Every new or changed proof is listed in §14 for independent confirmation. Scripts and logs of this revision are in `verify/extend/X3-ope/final2_scripts/` and `verify/extend/X3-ope/final2_logs/`.

**Conventions** (CONTEXT.md): metric $(+,-,-,-)$, $D=4-2\varepsilon$, $\overline{\rm MS}$, $Q^2=-q^2$, $\nu=P\cdot q$, $\omega=2\nu/Q^2=1/x$, $a=\alpha_s/\pi$. In Euclidean statements, $|q|$ is the Euclidean norm and $\hat q=q/|q|$.
*Breitenlohner–Maison notation (Prop. F.5 only).* BM write $n$ for the dimension (here $D$) and $\varepsilon$ for the damping parameter (here $\eta>0$). The symbol $\eta$ never denotes the $\varepsilon$ of $D=4-2\varepsilon$, and the spin label $n$ of $O^{(n)}$ is not BM's $n$.

**Grades**
- **[R, R_PT]**: complete perturbative proof (per graph or per order). A cited theorem qualifies only if it was *checked*, i.e. its statement and hypotheses were read in full text.
- **[R, R_def]**: algebra and definitions.
- **[R, R_cond: X]**: complete proof given the premises X. The *content grade* is that of the weakest premise.
- **[A]**: all-order argument with an unverified cited step.
- **[C]**: open.
- **数学 (no tag)**: pure mathematics (WRITER_SPEC_v2 §4.1; LEAD_DECISIONS LA-2). Earlier versions tagged these lemmas "[R]".
- Examples carry no tag, as in the outline; their content is stated in words.
- *Abstract* means only the abstract was read; *unread* means the text was not obtained.

**Markers**
- 「本书给出的严格证明」: only Theorem F (outline `thm:appM-forward-expansion`). 「本书新结果」 is withheld (O12).
- 「本书给出的推导／证明」: our derivation or proof of a published or classical result, printed next to the source; never a novelty claim.
- No other novelty wording is used (W26).

## 0. Summary

1. **Theorem I = A + B + twist classification [A]: Euclidean OPE of $J^\mu J^\nu$ in massless QCD with quarks.** It holds at every order of DR+$\overline{\rm MS}$, in covariant gauges $\xi_R\in\Xi\ni1$. Its parts:
   - (A1) remainder $O(|q|^{1-a}\ln^k)$;
   - (A2) $C_O=|q|^{2-d_O}\times$ a polynomial in $L=\ln(q^2/\mu^2)$;
   - (A3) $C^{\overline{\rm MS}}=C^{\rm bare}Z^{-1}$;
   - (A4) uniqueness in every exact block satisfying (NE), including the twist-2 blocks for **all** $n$ (Lemma NE);
   - (A5) the RG equation with $\beta_\xi\partial_\xi$ in the **full** D-dimensional basis, [R, R_cond: A3];
   - (B) $sX_d\in\mathcal E$, hence $X_d$ = GI + $s$-exact + EOM;
   - twist 2 consists only of $O^{(n)}_{q,g}$.

   The overall grade is [A] because (A1), (A3) and Eε are cited (Smirnov 1990 was checked, but its scope falls short of these statements).
2. **Theorem F [R, R_PT] per graph.** This is the book's rigorous proof (本书给出的严格证明) of the *analytic step* of the method of projectors: each forward on-shell DR Laurent coefficient is holomorphic on the cut $\omega$-plane and equals its convergent naive Taylor series. The closest prior result is Semenova–Smirnov–Smirnov 2019, §7, Prop. 6 (positive coefficients, one essential facet, asymptotic expansion as $t\to0^+$). Theorem F adds sign-indefinite dominated terms, convergence for complex $|\omega|<1$, holomorphy of every Laurent coefficient on the cut plane, and the DR identification. The identification with $\overline{\rm MS}$ coefficients (Cor. F.2) is [A].
3. **Proposition F.5 (zero-momentum twist-2 insertions; outline `prop:appM-zero-momentum-insertion`).** For $n\ge2$ the zero-momentum insertion of $\int O^{(n)}$ into two-point functions exists at every order in DR, in the Breitenlohner–Maison framework: BM II Thm 1 applies, and the identification of BM II's subtraction $S=C+T(1-C)$ with minimal subtraction is written out (step 2). Proposed [R, R_PT]; the book prints [A] until the LA-4 confirmation. In DR it settles only the existence/IR-finiteness part of reference Rem. C.37.
4. **Theorem M [R, R_cond: W, SA (+RG, Grow, Meas)].** Hadron-level DIS moments; refines reference Thm C.66. Theorem 5.7 step 1 now uses the exact dispersion remainder; the conclusion is unchanged.
5. **E1–E6.** Conditional statements on the Adler function and smeared $R(s)$; known in substance.

**Slot outcomes**

| Slot | Outcome |
|---|---|
| X3a | **Not delivered (open).** Uniqueness alone is circular (Rem. A.6). Lemma A.7 [R, R_cond: CTp] reduces asm:appM-remainder to a momentum-space theorem with $p$-derivative bounds at $p=0$. The designated sources are unread, so asm:appM-remainder stays [A]. |
| X3b | **Not passed.** prop:dis-ope-euclid stays [A]. |
| X3c | **Not delivered.** c_dis covers only $N\le8$. |
| X3d | **Partial.** QCD: asm:appM-brst-ope is replaced by Eε + LBC + JL (Thm B, content [A]). Pure YM: Hollands 2008 §4.1.3 (now read, K5) argues, in the Epstein–Glaser framework, that the OPE of $\hat s$-closed fields closes on $\hat s$-closed fields; the transfer to the DR+$\overline{\rm MS}$ coefficients of Theorem A is not made. |
| X3e | **PASS per graph** (Thm F, Lemmas F.6, F.7). asm:appM-forward is only *reduced* (Cor. F.2 [A]). Do **not** apply "asm:appM-forward 已解除". |

## 1. Setup and assumption register

**D1. Theory and gauge fixing.**
- SU($N_c$) with $n_f$ massless Dirac quarks.
- Gauge fixing $s(\bar c(\partial\!\cdot\!A+\xi_0B/2))$, with $B$ off shell and $\xi_0=Z_3\xi_R$. Feynman gauge means $\xi_R=1$.
- $\beta_\xi=\mu\,d\xi_R/d\mu=-2\gamma_3\xi_R=\frac{\alpha_s}{2\pi}\xi_R[(\frac{13}6-\frac{\xi_R}2)C_A-\frac43T_Fn_f]+O(\alpha_s^2)$. At $\xi_R=1$ in SU(3) this is $\frac{\alpha_s}{2\pi}(5-\frac23n_f)\ne0$ (rv32_misc (a)).

**BRST and dimensions.**
- BRST transformations: $sA=Dc$, $s\psi=ig_0c\psi$, $sc=-\frac{g_0}2[c,c]$, $s\bar c=B$, $sB=0$.
- Canonical dimensions: $[A]=[c]=[\bar c]=1-\varepsilon$, $[\psi]=\frac32-\varepsilon$, $[B]=2-\varepsilon$, $[g_0]=\varepsilon$, $[\mathcal J(q)]=2-2\varepsilon$.
- A monomial with $n_\phi$ fields and $n_g$ explicit factors of $g_0$ has dimension $d(\varepsilon)=d^{(4)}-\varepsilon w$, with weight $w=n_\phi-n_g$. The BRST operator $s$ raises $d^{(4)}$ by 1 and preserves $w$.

**D2. Scheme.**
- DR, with analytic regulators where stated, and $\overline{\rm MS}$: $[O]=Z_{OO'}O'_{\rm bare}$.
- Green functions of $[O]$ are finite at non-exceptional momenta (Breitenlohner–Maison 1977; Collins 1984 ch. 6).
- There is no $\gamma_5$, so DR is exactly BRST-invariant.
- The basis is D-dimensional: formal tensors with $g^\mu_\mu=D$, and $\gamma^{[\mu_1..\mu_r]}$ of every rank.

**D3. Operator classes.**
- GI: colour-singlet polynomials in $F,\psi,\bar\psi,D$.
- BRST-exact: $s\Lambda$.
- EOM: the ideal $\mathcal E$ generated by $\partial^\alpha\delta S/\delta\phi$.
- Aliens: exact + EOM.
- Rest: a complement of GI ⊕ aliens.

**D4–D5.** $\mathcal J^{\mu\nu}(q)=i\int d^Dx\,e^{iqx}TJ^\mu(x)J^\nu(0)$. $\tilde G^T_{JJ;\Phi}$ and $\tilde G_{[O];\Phi}$ are connected amputated Green functions with a string $\Phi$ of elementary fields. A configuration is non-exceptional when no proper partial sum of the momenta vanishes.

**D6. Structure functions.**
- $T^{\mu\nu}=i\!\int\! e^{iqz}\langle P|TJ^\mu J^\nu|P\rangle_c=-\tilde g^{\mu\nu}T_1+\hat P^\mu\hat P^\nu T_2/\nu$ and $W^{\mu\nu}=\frac1{4\pi}\!\int\! e^{iqz}\langle P|[J^\mu,J^\nu]|P\rangle_c=-\tilde gF_1+\hat P\hat PF_2/\nu$, with $\tilde g=g-qq/q^2$ and $\hat P=P-(\nu/q^2)q$.
- Moments: $T_2=\sum_{n\,\rm even}t_n\omega^{n-1}$ and $M_2^{(n)}=\int_0^1x^{n-2}F_2$, elastic point included.
- Free quark: $T_2=4e_q^2\omega/(1-\omega^2)$.

**D7.** $O^{(n)}_q=\mathcal S\bar\psi\gamma^{\alpha_1}iD^{\alpha_2}\!\cdots iD^{\alpha_n}\psi-$tr and $O^{(n)}_g=\mathcal SF^{\alpha_1\rho}iD\cdots F_\rho{}^{\alpha_n}-$tr, with $\langle P|O^{(n)}_i|P\rangle=2A^{(n)}_i(P\cdots P-{\rm tr})$.

**D8.** $\mathcal I_Q=\{iy:|y|\le r_Q=\sqrt3M/Q\}$.

**D9.** Naive Taylor term: replace $p\to\lambda p$ and expand the integrand in $\lambda$.

**D10.** Lee–Pomeransky form $\int_{\mathbb R^N_+}\alpha^{a-1}(\mathcal U+\mathcal F)^{-D/2}$. Tarasov's relation turns tensor integrals into scalar ones in $D+2k$ dimensions with shifted powers.

**D11. (NE).** A finite set $\mathcal S$ satisfies (NE) if, at $D=4$, the map $(t_O)_{O\in\mathcal S}\mapsto\sum_Ot_O(V^{(4)}_O)$ is injective. Here $V^{(4)}_O$ are the 4D tree vertices and $t_O$ ranges over the constant equivariant contractions arising in $\mathcal S$ (Def. A.2). The scope of (NE) is Lemma NE (数学).

**Assumption register** (monograph prefix `asm:X3-`).

| Label | Content | Status |
|---|---|---|
| (A1), (A3) | DR/$\overline{\rm MS}$ large-$q$ expansion; $C^{\overline{\rm MS}}=C^{\rm bare}Z^{-1}$ | [A] (K2) |
| Eε | the same with one composite spectator $s\phi$, including merged terms (Thm B) | [A] (K2) |
| DR-WI, DR-SD | exact bare DR Ward and Schwinger–Dyson identities | standard |
| LBC | local BRST cohomology (K6, Lemma B.1) | cited, checked |
| JL | Joglekar–Lee triangularity; $\partial_\xi\gamma_{GG}=0$ | abstract (K3) |
| KO | $\langle s\Lambda\rangle=0$ between physical states | cited |
| CTp | $p$-derivative remainder bounds at $p=0$ (Lemma A.7) | open |
| OSWI | on-shell forward gluon Ward identity (Lemma F.8) | [A] |
| GP′ | $\partial_\xi C^{GI}_i\vert_{\xi=1}=0$ (Cor. A.5) | [A] |
| W1–W3, SA, NPOPE, RG, PDF, Grow, Meas | hadronic DIS (§5) | assumptions |
| V1, VOPE, VPT, VSec | e⁺e⁻ (§6) | assumptions |

Earlier names: SA = N1, NPOPE = N1-std, RG = N2, PDF = N3, Grow = G, Meas = Φ, VOPE = V2, VPT = V3, VSec = V2′, JL = "K3"; Lemma B.1 = Remark B.1 and Prop. F.5 = Remark F.5 of earlier versions.

## 2. Literature ledger

Copies of **all** checked texts are in `verify/extend/X3-ope/literature/`. This revision added: BM I, the BM action-principle paper, Feichtner–Sturmfels, Semenova–Smirnov–Smirnov 2019, Jantzen 2011, Nilsson–Passare, Berkesch–Forsgård–Passare, and Hollands 2008 (`hollands_RMP20_2008_0705.3340v4.txt`, text of arXiv:0705.3340v4).

**K1: IR finiteness and existence (Breitenlohner–Maison).**
- *Checked, full text:* **BM I** = Breitenlohner–Maison, CMP 52 (1977) 39 [`Breitenlohner:1975hg`]. It treats purely massless theories without super-renormalizable couplings.
  - α-representation with the damping factor; ε-Lemma p. 42, proved in App. B, whose closing Remark extends it to an extra factor $\varepsilon^k$, ${\rm Re}\,k>0$.
  - Prop. 1, p. 45: $\lim_{\varepsilon\to0}\mathcal T_{G,\varepsilon}(p,n)$ exists in $\mathcal S'$ near $n=4$, with poles at $n=4$ from UV subgraphs only.
  - §II.3, pp. 45–47: arbitrary external vertices are allowed, and internal vertices of dimension $\delta\ge4$, including non-renormalizable ones. Graphs with tadpoles vanish in the limit (p. 47).
  - §III, pp. 48–49: "If we denote by $\mathcal R_{G,\varepsilon}(p,n)$ the regular part of the Laurent series expansion of $\mathcal T_{G,\varepsilon}(p,n)$ around $n=4$ then $\mathcal R_G(p,n)=\lim\mathcal R_{G,\varepsilon}(p,n)$ resp. its value at $n=4$ is defined to be the dimensionally renormalized amplitude for $G$."
  - Theorem 1, p. 49: Green functions of arbitrary composite operators exist at every order as tempered distributions (BM: "distributions over $\mathcal S$"), and the counterterms are local with poles at $n=4$. From its proof: "ε, as we have used it, acts like a mass term. The counter terms necessary for renormalization (for ε > 0) are again of the strictly- or non-renormalizable type (δ ≥ 4), except when they are proportional to ε resp. ε²; in this case δ ≥ 2 resp. δ ≥ 0. The argument used for the contributions from tadpoles (end of Section II.3) applies also here and guarantees that such contributions vanish in the limit ε→0."
- *Checked, full text:* **BM II** = CMP 52 (1977) 55 [`Breitenlohner:1976te`].
  - §1, pp. 55–56. The damped α-integral (1.1) converges absolutely for $\varepsilon>0$ (and suitable ${\rm Re}\,n$; the inequality is garbled in the copy) and is meromorphic in $n$: "The limit ε→0 may or may not exist (in $\mathcal S'$), depending on whether there are IR-singularities or not." Purely massless theories "can be treated completely within the framework of dimensional renormalization, that is to say, the subtraction of pole terms in n−4 … is sufficient". The normalization conditions "are automatically satisfied as long as all particles are massless".
  - §2: IR degrees, $\Delta_\phi=(4+D)/2$ for a propagator $\sim|p|^D$ as $|p|\to0$. The requirement $\Delta_\phi\ge1$ for all fields excludes IR singularities of the free theory (the symbol is garbled in the copy; $\Delta\ge1$ is the value consistent with the massless scalar, $\Delta=1$, being admitted). Integrated interaction monomials with $\Delta\ge4$ suffice.
  - §3, pp. 61–63:
    - $S=C+T(1-C)$, with $C$ the singular part of the Laurent expansion at $n=4$ and $T$ the Taylor series at $p=0$ to order $\Omega_G-1$.
    - Prop. 1 and eq. (3.13): renormalization with $S=S_1+S_2$ equals the $S_1$-renormalization of reduced graphs with $S_2$-vertex parts. With $S_1=C$, $S_2=T(1-C)$, all terms are analytic at $n=4$ for $\varepsilon\ne0$.
    - IR degrees of vertex parts, (3.14): $\Delta^H_Y=4+\sum_{V_i\in H}(\Delta_i-4)$.
    - General propagators (3.15)–(3.16): a monomial numerator $M_\ell(p)$ of degree $r_\ell$ over $s^0_\ell$ massless and $s^m_\ell$ massive poles, with powers $w_\ell>0$. The IR degree $\frac12(4+r_\ell)-s^0_\ell$ follows from the definition $\Delta=(4+D)/2$; formula (3.16) itself is garbled in the copy.
    - α-representation (3.17) with $(p^2-z+i\varepsilon)$.
  - §5:
    - $\Omega_H=\omega_H+2s_H$, $s_H$ = number of massive denominators (p. 69).
    - ε-Lemma = Lemma 3 (pp. 67–68), including "$\lim_{\varepsilon\to0}\varepsilon^kf(q,\rho+2k,\varepsilon)=0$ for $k>0$".
    - Props. 2–3.
    - **Theorem 1** (p. 72): "For any connected Feynman graph G, satisfying $\Delta_i\ge4$ for all internal vertices, the renormalized amplitude $\mathcal R^S_{G,\varepsilon}(p,n)$ … is analytic at n = 4 and has a limit ε→0 (as distribution over $\mathcal S$) in some finite neighborhood of n = 4."
    - Tadpoles vanish (pp. 72–73). Theorem 2 (p. 73).
- *Checked:* BM, "Dimensional renormalization and the action principle", CMP 52 (1977) 11 [`BreitenlohnerMaison1977a`].
  - §II.1, pp. 12–16. The regularized integrand carries $\exp[-i\sum_\ell\alpha_\ell(m_\ell^2-i\varepsilon)]$, i.e. the Feynman $i\varepsilon$ kept finite, which in α-space is the damping factor $e^{-\varepsilon\sum\alpha_\ell}$. Eq. (3) on p. 13 is not legible in the copy; the factor is legible on p. 30 ("$\exp[-i(\alpha(m^2-i\varepsilon)+u^2/4\alpha)]$") and p. 36 ("$\sum\alpha_\ell(m_\ell^2-i\varepsilon)$").
  - p. 16: "For $\min\{m_\ell\}\ne0$ the limit ε→0 exists". p. 35: the dependence on ε enters only through $t_G\sqrt\varepsilon$, so ε has mass dimension 2.
  - §III.1, Theorem 1 (p. 22): the singular part of $\mathcal T_H$ (after its subdivergences) has poles of order $\le h_H$ and is a polynomial of degree $\omega_H$. The pole-subtracted amplitudes are analytic at $n=4$; "$\lim\mathcal R_{G,\varepsilon}(p,n)$ exists … This limit … is the renormalized amplitude."
- **What BM's ε is.** It is the damping parameter, i.e. the finite Feynman $i\varepsilon$, which "acts like a mass term" of mass dimension 2. It is not the dimensional regulator: BM's dimension is $n$. BM II Thm 1 gives, per graph, analyticity of $\mathcal R^S_{G,\varepsilon}$ at $n=4$ and a limit $\varepsilon\to0$ in $\mathcal S'(p)$ near $n=4$.
- **Covariant-gauge QCD qualifies** (BM II §§2–3):
  - IR degrees: $\Delta_A=\Delta_c=\Delta_{\bar c}=1$ and $\Delta_\psi=\frac32$. With $B$ off shell, $\langle AB\rangle\propto p/p^2$ and $\langle BB\rangle=0$, so $\Delta_B=2$.
  - The gluon propagator $-i[g-(1-\xi)pp/p^2]/p^2$ is of form (3.15): the term $g/p^2$ has $r=0,s^0=1$ and the term $pp/(p^2)^2$ has $r=2,s^0=2$, both of IR degree 1.
  - All QCD interaction monomials have $\Delta=4$.
- *Abstract only:* Lowenstein–Zimmermann (CMP 44, 73); Lowenstein (CMP 47, 53); Poggio–Quinn (PRD 14, 578).

**K2: DR/$\overline{\rm MS}$ OPE.**
- *Checked:* Smirnov, CMP 134 (1990) 109. The Theorem on p. 117 is a *mixed* statement: a distribution in the coordinate variables $\xi$ and a function of non-exceptional Euclidean momenta, in analytic regularization. The DR function form is only asserted ("one may easily maintain", p. 118). The operator form is in §6. Ghosts, gauge-variant bases and composite spectators are not treated.
- *Checked:* Chetyrkin, arXiv:1701.08627. Thms 7–8 are stated with proofs "given elsewhere".
- **Unread designated X3a sources:**
  - Anikin–Zav'yalov, TMF 27 (1976) 425 and Ann. Phys. 116 (1978) 135;
  - Zav'yalov 1979/1990;
  - Llewellyn Smith–de Vries, NPB 296 (1988) 991;
  - Anikin–(Karchev/Bordag)–Zav'yalov, TMF 44, 46, 56.
- **Unread, to be read first:**
  - Zimmermann, Ann. Phys. 77 (1973) 570 (= LNP 558 (2000) 278), and the Brandeis 1970 lectures;
  - Bergère–de Calan–Malbouisson, CMP 62 (1978) 137;
  - Bergère–Lam, CMP 39 (1974) 1;
  - Linhares–Malbouisson–Roditi, IJMPA 23 (2008) 1089, for the gauge-theory scope of (A1).
- *Checked secondary sources:* Smirnov p. 110, Keller–Kopper CMP 153 (1993) 246, and Tkachov hep-th/9612037 fn. 14 all describe the AZ/Zav'yalov results as position-space expansions. A position-space bound does not imply the momentum-space bound C.24.
- **Consequence:** (A1), (A3) and Eε remain [A].

**K3: renormalization of GI operators** (abstracts). Joglekar–Lee, Ann. Phys. 97 (1976) 160; Kluberg-Stern–Zuber, PRD 12 (1975) 467, 482, 3159; Henneaux, PLB 313 (1993) 35; Collins–Scalise, PRD 50 (1994) 4117.

**K4.** Joglekar, Ann. Phys. 108 (1977) 233 and 109 (1977) 210 (abstracts).

**K5: pure YM.**
- *Checked (location verified, LA-7):* Hollands, RMP 20 (2008) 1033 = arXiv:0705.3340 (v4), §4.1.3 "Operator product expansions and RG-flow", pp. 75–76 of v4. In the Epstein–Glaser framework on globally hyperbolic spacetimes (Minkowski included), pure YM: physical fields are classes $[Q_I,O_I]=0$ modulo $[Q_I,O'_I]$. With $[Q_I,O_I]=(\hat qO)_I$, $\hat q=\hat s+O(\hbar)$, "the OPE closes on gauge invariant operators": for $\hat s$-closed inputs of ghost number 0 the coefficients vanish unless the output is $\hat s$-closed of ghost number 0. If one input is $\hat s$-exact, only $\hat s$-exact outputs occur. The RG flow closes likewise.
- Fröb–Holland 1603.08012; FHH, JMP 57 (2016) 122301.

**K6: LBC** (checked). BBH, Phys. Rep. 338 (2000) 439 (Thm 7.1, Lemma 8.1, §§8.3, 8.6, 2.6–2.7; valid in any dimension); Henneaux, PLB 367 (1996) 163 §3; BHHS, PLB 492 (2000) 376, App.

**K7.** Hollands–Kopper, CMP 313 (2012) 257; Holland–Hollands–Kopper, CMP 342 (2016) 385.

**K8: polytope methods.**
- Schultka 1806.01086, §§3–4 (checked; copy).
- Berkesch–Forsgård–Passare, arXiv:1103.6273 (BFP; checked; copy). Def. 2.1 (completely non-vanishing); Thm 2.2: the Euler–Mellin integral converges on the tube over ${\rm int}(\tau\Delta_f)$. Thm 2.4: meromorphic continuation $\Phi\prod_k\Gamma(\langle\mu_k,s\rangle-\langle\nu_k,t\rangle)$, $\Phi$ entire, if $\Delta_f$ is full-dimensional.
- Nilsson–Passare, J. Geom. Anal. 23 (2013) 24, arXiv:1010.5060 [`NilssonPassare2013`] (checked; copy). Def. 1; Thm 1 (convergence on the tube over ${\rm int}\,\Delta_f$ for completely non-vanishing $f$); Thm 2 (meromorphic continuation with Gamma factors).
- Feichtner–Sturmfels, arXiv:math/0411260 (checked; **copy added in this revision**: `literature/feichtner_sturmfels_math0411260.txt`). Prop. 2.3 ($P_M=\{x\in\Delta:\sum_{i\in F}x_i\le{\rm rank}(F)\}$ over flats $F$); Prop. 2.4 ($\dim P_M=n-c(M)$); Prop. 2.6 (facet-defining flats).
  - Bibliography note: `refs_merged_v2.bib` dropped FS as "not verifiable on INSPIRE/Crossref", and the book cites `Schultka:2018nrs` for these facts. FS is verifiable on arXiv, so under LA-14 the App M writer may restore it.
- Borinsky, AIHPD 10 (2023) 635 Thm 32; Arkani-Hamed–Hillman–Mizera, PRD 105 (2022) 125013; Tellander–Helmer, CMP 399 (2023) 1021; Walther, LMP 112 (2022) 120; Kaneko–Ueda 2010; Speer 1975.

**K9: analysis and invariant theory.** Vladimirov §§25–26; Reed–Simon II Thm IX.16; Hörmander ALPDO I Thm 3.1.15; Feller II; Korevaar; Borwein–Erdélyi; Weyl's first and second fundamental theorems (FFT/SFT) for O($n$); Littlewood's GL→O restriction rule.

**K10.** c_ee Thm 5.1. **K11.** c_pdf §§5, 7. **K12.** Dugan–Grinstein, PLB 256 (1991) 239; Herrlich–Nierste, NPB 455 (1995) 39 (abstracts).

**Forward-expansion literature.**
- Gorishny–Larin–Tkachov, PLB 124 (1983) 217 (not checked);
- Gorishny–Larin, NPB 283 (1987) 452 (not checked);
- Larin–van Ritbergen–Vermaseren, NPB 427 (1994) 41 (not checked);
- LNvRV, NPB 492 (1997) 338 (§2 checked; copy);
- MVV, NPB 724 (2005) 3;
- Semenova–Smirnov–Smirnov, EPJC 79 (2019) 136, arXiv:1809.04325 [`Semenova:2018cwy`] (§§2–4 and §7 checked; copy). The setting is Lee–Pomeransky integrals with positive coefficients $c_w>0$. §3 recalls Speer's analytic-regularization definition of DR integrals at Euclidean momenta. §7, Prop. 6: with one essential facet the expansion by regions holds to all orders as $t\to+0$.
- Jantzen, JHEP 12 (2011) 076, arXiv:1111.2589 [`Jantzen2011`] (§§3, 7 checked; copy). §3, p. 17: "I cannot provide a rigorous proof for this convergence issue in the general case". §7: forward scattering of two light-like particles with $Q^2\gg\vec r_\perp^{\,2}$, with hard, collinear (1c, 2c), Glauber and collinear-plane regions (§7.1).
- Nilsson–Passare 2013 and BFP (see K8).

## 3. Part I: Euclidean perturbative OPE

**Lemma A.3 (linear independence) [R, R_PT].** Suppose that, at each order, $\sum_{O\in\mathcal S}c_O(q)\tilde G_{O;\Phi}(p)=O(|q|^\varrho\ln^k)$ for all $\Phi$ and all $p$ in an open non-exceptional set. Then:
- **(a)** At fixed generic $\varepsilon$, for bare functions with formal-D tree vertices: $c_O=O(|q|^\varrho\ln^k)$, and graded-homogeneous $c_O$ of degree $>\varrho$ vanish. The same holds coefficientwise in the Laurent expansion in $\varepsilon$.
- **(b)** At $D=4$, for renormalized functions, the same holds if $\mathcal S$ satisfies (NE). The sum must run over $\mathcal S$ **only**, i.e. after the exact projections of Def. A.2.

*Proof.* For an operator $O$ let $m(O)$ be the least number of elementary fields in a monomial of $O$.
1. **Organisation.** Fix the order in the coupling. The relation at this order is a finite sum of products of a coefficient (of that or a lower order) and a Green-function term.
   - Tree graphs of $O$ with legs $\Phi$ exist only if $|\Phi|\ge m(O)$.
   - For $|\Phi|=m(O)$ and matching field content, they are the vertex polynomial $V^\Phi_O(p)$.
   - For $|\Phi|>m(O)$, they also contain trees with internal propagators, built from lower monomials of $O$ and QCD vertices. These are non-polynomial in $p$ and enter at the **same** order as the vertices of operators with $m=|\Phi|$: each extra leg costs one coupling, whether it comes from a higher monomial of $O$ or from a QCD vertex.
2. **Induction over (order, number of legs), lexicographically.** Assume that all coefficients of lower order are $O(|q|^\varrho\ln^k)$, and so are the coefficients of the current order for every operator with $m(O)<m$. Take $\Phi$ with $|\Phi|=m$.
   - All terms except $\sum_{m(O)=m}c_OV^\Phi_O$ are then $O(|q|^\varrho\ln^k)$, because $\tilde G$ does not depend on $q$.
   - In particular the non-polynomial trees of the fewer-field operators enter with coefficients already fixed at lower leg number.
3. **Independence.** Hence $\sum_{m(O)=m}c_O(q)V^\Phi_O(p)=O(|q|^\varrho\ln^k)$ for all such $\Phi$ and all $p$ in an open set.
   - The vertex polynomials of distinct basis operators are linearly independent as formal-D tensors; this is how the D-dimensional basis is chosen. At $D=4$ this independence is exactly (NE).
   - Evaluating at finitely many points $p$, or taking finitely many $p$-derivatives, gives an invertible linear system. So $c_O=O(|q|^\varrho\ln^k)$ for $m(O)=m$.
4. **Homogeneous parts.** In (a), distinct powers $|q|^{\kappa-2j\varepsilon}$ (generic $\varepsilon$) separate the graded-homogeneous components. A component of degree $>\varrho$ that is $O(|q|^\varrho\ln^k)$ vanishes. Laurent coefficients in $\varepsilon$ are finite sums of $|q|^\kappa L^m$ and are treated the same way.
   - In (b), the order in $\alpha_s$ and the $L^m$-separation of (P4) play this role. Step 3 uses (NE) for $\mathcal S$, so the sum must run over $\mathcal S$ only, after the exact projections. ∎

This is known in spirit (reference Lemma C.30). Without (NE), step 3 fails: evanescent operators have vanishing 4D tree vertices but non-zero renormalized 4D Green functions.

**Definition A.2 (exact projections; blocks).** Let $\sum_{d_O\le a}\Delta C_O(q)\tilde G_{[O];\Phi}(p)=O(|q|^{1-a}\ln^k)$, uniformly in $\hat q\in S^3$, with each $\Delta C_O$ of form (A2). The following operations act on the coefficient side only:
- **(P1)** $(\mu\nu)$-(anti)symmetrization.
- **(P2)** $\mu\nu$ trace/traceless split.
- **(P3)** Projection onto spherical harmonics of degree $\ell$ in $\hat q$. This is legitimate because the remainder bound is uniform in $\hat q$.
- **(P4)** Separation of the terms $|q|^{2-d}L^m$, $d\le a$. Afterwards the relation holds *exactly*, with zero remainder.
- **(P5)** At $D=4$, projection of the output tensor (indices $\mu,\nu$ and the $\ell$ harmonic slots) onto an O(4)-isotypic type $\rho$. Since the $O$-term is $t_O(\tilde G_{[O]})$ with $t_O:W_O\to{\rm Out}$ equivariant, Schur's lemma gives $\Pi_\rho t_O=t_O\Pi^{W_O}_\rho$.

A **block** is the set of operators of dimension $d$ that survive (P1)–(P5). On a block the relation reads exactly $\sum_{O\in\mathcal S}\Pi_\rho t_O(\tilde G_{[O]})=0$. "Sector" in rounds 2–3 means a block or a union of blocks.

**Lemma NE (scope of (NE); outline `lem:appM-ne`) — 数学 (no tag).** By the second fundamental theorem (SFT) for O(4) and the basis $\{\gamma^{[r]}\}_{r\le4}$ of Cl(4), an identity that holds at $D=4$ but not at formal $D$ is spanned by terms containing an antisymmetrizer over $\ge5$ slots. Such an antisymmetrizer is either a Dirac rank $\ge5$ structure or a $\delta^{[a_1..a_5]}_{[b_1..b_5]}$ (Gram/Schouten). Each slot needs a distinct carrier: a free index, momentum or polarization.

- **(i) $(\mu\nu)$-symmetric channel, $d_O\le5$: (NE) holds.**
  - An antisymmetrized set contains at most one of $\mu,\nu$ and at most one $\hat q$.
  - The remaining carriers come from $O$: at most $d_O-3\le2$ derivative or gauge slots for quark bilinears. Dirac indices of $O$ can only be filled by $\mu,\nu,\hat q$ or by $O$'s own derivatives.
  - For $FF$ and $FDF$ the index slots are exhausted before a second five-element set exists.
  - Hence each set has $\le4$ carriers.

- **(ii) Twist-2 blocks $\mathcal B^\pm_n$, all $n\ge2$: (NE) holds.** These are the blocks with $d=n+2$ and $\rho=(\frac n2,\frac n2)^\pm$: rank-$n$ symmetric traceless tensors of either parity, with O(4) labels $[n]$ and its associate $[n,1,1]$.
  - **(α) Content.** $O\in\mathcal B^\pm_n$ requires $W_O\supset\rho$. The GL(4) content of $W_O$ has first row $\le y(O)$, the maximal number of mutually symmetrizable free slots. Littlewood restriction removes boxes and associates keep the first row, so $y(O)\ge n$.
  - **(β) Count.** Derivatives and gauge fields give $\le1$ slot each at cost 1. A quark bilinear gives $\le1$ slot of a symmetric set at cost 3. Ghosts and $B$ give none. With $b$ bilinears and slot-free cost $\kappa$, $n\le y\le(n+2-3b-\kappa)+b$, so $2b+\kappa\le2$.
    - Hence $b\le1$, and **no four-quark operator lies in $\mathcal B^\pm_n$**: four-quark contents have $y\le n-2$ (f7 (c)).
    - **For $b=1$:** $\kappa=0$. All $n-1$ derivative and gauge slots are free first-row slots, and exactly one Dirac index of the bilinear's structure $\gamma^{[r']}$ lies in the symmetric set. So no derivative, momentum or polarization factor is contracted with a Dirac index.
      - Every further Dirac index is a free index of $O$ outside the symmetric set. The equivariant contraction $t_O$ fills it with $\mu$, $\nu$ or $\hat q$, each at most once (antisymmetry). Hence **$r'\le4$**, and rank $\ge5$ structures cannot occur.
      - Chirality gives more: every open massless quark line with vector vertices carries an odd number of $\gamma$ matrices, so $r'$ is odd, $r'\in\{1,3\}$. This is **not** used below.
    - **For $b=0$:** bosonic monomials with $\kappa\le2$, e.g. $A\partial^nA$ or $\bar c\partial^nc$.
  - **(γ) Demand exceeds supply.**
    - *Projected relation.* After (P5) the relation is a linear relation among polynomials in the leg vectors (momenta $p_j$ and polarizations $\varepsilon_j$), the projection vector $z$ (null, degree $n$, the first-row output) and, for $[n,1,1]$, two antisymmetrized auxiliary vectors $w_1,w_2$ (degree 1 each). Its values lie in Cl($D$) through one Dirac structure $\gamma^{[r']}$ per monomial, with $r'=0$ for $b=0$. Since $\gamma^{[0]},\dots,\gamma^{[4]}$ are independent at $D=4$ and every generator below preserves the Dirac rank, the relation splits by $r'$.
    - *Generators of $D=4$-only relations* (preamble):
      - (G) a $5\times5$ Gram antisymmetrizer, with 5 upper and 5 lower vector slots;
      - (M$_r$) a mixed antisymmetrizer, with $r$ Dirac indices of $\gamma^{[r']}$ and $5-r$ vector slots above and 5 vector slots below, $1\le r\le\min(r',4)$;
      - (G5) $\gamma^{[5]}$ contracted with 5 vectors, possible only if $r'\ge5$.
    - *Demand.* Three facts fix the count.
      - $z$ occupies at most one slot of each antisymmetrized set and at most one Dirac index outside the antisymmetrizer (antisymmetry).
      - Every other copy of $z$ must be contracted with a non-$z$ vector ($z^2=0$).
      - Every Dirac index outside the antisymmetrizer needs a distinct vector.

      Let $Z_{\rm up},Z_{\rm low},Z_D\in\{0,1\}$ be the numbers of $z$'s in these three places. A term of type (G) ($r=0$) or (M$_r$) needs
      $$(10-r-Z_{\rm up}-Z_{\rm low})+(r'-r-Z_D)+(n-Z_{\rm up}-Z_{\rm low}-Z_D)=n+10+r'-2r-2(Z_{\rm up}+Z_{\rm low}+Z_D)$$
      non-$z$ vector occurrences.
      - The minimum over $r\le r'$ and the $Z$'s is **$n+6-r'$**. It is attained at $Z_{\rm up}=Z_{\rm low}=1$ with either $r=r',Z_D=0$ or $r=r'-1,Z_D=1$; for $r\le r'-2$ the demand is $\ge n+8-r'$.
      - For $b=0$ ($r'=0$) the minimum is $n+6$, the Gram count. Type (G5) needs $(5-Z)+(r'-5-Z_D)+(n-Z-Z_D)$ non-$z$ occurrences, where $Z+Z_D\le1$ because all these slots are Dirac indices of one $\gamma^{[r']}$; hence $\ge n+r'-2\ge n+3$.
      - For $b=1$, $r'\le4$ gives a demand $\ge n+2$: $n+5$ at $r'=1$, $n+3$ at $r'=3$, $n+2$ at $r'=4$.
    - *Supply.* The projected vertex contains at most $d-3b=n+2-3b$ momentum and polarization factors: one per derivative or gauge field, none for quark fields and ghosts. For $\mathcal B^-_n$ add $w_1,w_2$. So the supply is at most $n+4$ ($b=0$) and $n+1$ ($b=1$).
    - *Conclusion.* For $b=0$, $n+6>n+4$; for $b=1$, $n+6-r'\ge n+2>n+1$. No $D=4$-only relation exists, and (NE) holds in every $\mathcal B^\pm_n$, $n\ge2$. Only $r'\le4$ is used: even $r'=4$ gives $n+2>n+1$, so (γ) does not depend on the chirality argument. ∎
    - *Checks.*
      - `final2_scripts/fix4_ne_demand.py`, Part 1: exhaustive minimisation of the demand over $(r,Z_{\rm up},Z_{\rm low},Z_D)$ for $n=2..30$, $b\in\{0,1\}$, $r'\le4$, both parities. The minimum is $n+6-r'$ and always exceeds the supply.
      - Part 2 (numerical rank, with the final reviewer's evaluator `review_final_scripts/fr_ne_rank.py`): the threshold is sharp. With $r'=4$ a $D=4$-only relation appears with $n+2$ non-$z$ vectors (C5). With $r'=3$ one appears with $n+3$ non-$z$ vectors and none with $n+2$ (C8). With ranks 0..4 and supply $n+1$ (both parities) there is none (C7, C9). The control C6 (rank 4 with $n+1$ non-$z$ vectors) is vacuous: no monomial of that multidegree exists.
      - Final reviewer's `fr_ne_rank.py` and `fr_ne_rank_allr.py`: no $D=4$-only relation in any sector AA, AAA, AAAA, cc, ccA, BA, BAA, qq, qqA, qqAA of $\mathcal B^\pm_n$, $n=2..5$, Dirac ranks 0..4, with Gram and Dirac controls.
      - All rerun byte-identically (`final2_logs/rerun_all.log`).

- **(iii) Failures of (NE).**
  - The $(\mu\nu)$-antisymmetric channel at $d_O=5$, already at tree level: the rank-5 part $2\gamma^{[\nu l\alpha q\mu]}/q^4$ (f6; re-derived by r3-1 and r3-2).
  - Four-quark blocks at $d_O\ge6$: $\Gamma^{(5)}\cdot\Gamma_{(5)}=+D(D-1)(D-2)(D-3)(D-4)$ (f7 (a); the sign of rv22_algebra (E) is corrected).
  - There, $D=4$ uniqueness generally fails without an evanescent prescription (Dugan–Grinstein; Herrlich–Nierste).

### Theorem A (Euclidean OPE for $J^\mu J^\nu$, covariant gauges)

**Hypotheses.** D1–D2; $\xi\in\Xi$ compact with $1\in\Xi$; fixed order $r$; integer $a\ge2$; D-dimensional $\overline{\rm MS}$ basis.

- **(A1)** $\tilde G^T_{JJ;\Phi}-\sum_{d_O\le a}C_O(q;\mu,\xi)\tilde G_{[O];\Phi}=O(|q|^{1-a}\ln^k)$, uniformly in $\hat q$, on compact non-exceptional $p$-sets, and in $\xi$.
- **(A2)** $C_O=|q|^{2-d_O}\times$ a polynomial of degree $\le r$ in $L$, with covariant coefficients polynomial in $\xi$.
- **(A3)** $C^{\overline{\rm MS}}=C^{\rm bare}Z^{-1}$ is finite. Here $C^{\rm bare}_O$ is the sum over hard (AI) subgraphs containing both currents of their DR Taylor coefficients; it depends only on $(q,g_0,\xi_0,\varepsilon)$.
- **(A4)** In every block satisfying (NE), two families obeying (A1)–(A2) have equal projected coefficients. By Lemma NE this covers the symmetric channel at $d_O\le5$ and all $\mathcal B^\pm_n$. In particular the full twist-2 coefficients (all invariant functions $C^{(n)}_{L,i},C^{(n)}_{2,i}$, and the axial analogues) are unique.
- **(A5)** For **every** basis operator, evanescent ones included:
  $$(\mu\partial_\mu+\beta\partial_\alpha+\beta_\xi\partial_\xi)C_i=\sum_jC_j\gamma_{ji},\qquad\gamma=-(\hat{\mathcal D}Z)Z^{-1},$$
  where $\hat{\mathcal D}=\mu\partial_\mu+\beta(\alpha,\varepsilon)\partial_\alpha+\beta_\xi\partial_\xi$. For $\Phi=\varnothing$ the identity-operator coefficient obeys this with an inhomogeneous term.

*Proof.*

**(A1), (A3).** Apply K2 graph by graph and in operator form at each $\xi$; substitute $O_{\rm bare}=Z^{-1}[O]$. IR finiteness follows from K1.
- Uniformity in $\xi$: Lagrange interpolation, since the remainder is polynomial in $\xi$ at fixed order.
- For $\Phi\ne\varnothing$ no additive renormalization of $\tilde G^T$ is needed. Subgraphs containing both currents have superficial degree $2-E_A-E_c-\frac32E_\psi$, and the only degree-0 local terms ($g^{\mu\nu}AA$, $g^{\mu\nu}\bar cc$) violate the contact-free EM Ward identity for neutral legs.
- For $\Phi=\varnothing$ an additive counterterm is needed.

**(A2).** At fixed $\varepsilon$, the $k$-loop hard part is homogeneous of degree $2-d_O-2k\varepsilon$ in bare $(g_0,\xi_0)$. Substituting $g_0=\mu^\varepsilon Z_gg$, $\xi_0=Z_3\xi$ and $Z^{-1}$ gives $|q|^{2-d_O}\sum_kc_k(\varepsilon,\xi)(\mu^2/q^2)^{k\varepsilon}$, with poles of order $\le r$. A finite limit of this form is a polynomial in $L$.

**(A4).** Apply (P1)–(P5) to the difference of two expansions, then use Lemma A.3(b) for each $L^m$ coefficient. For $O^{(n)}_{q,g}$, $W_O=[n]$ is $\rho$-isotypic, so every harmonic component ($\ell\in\{n-2,n,n+2\}$) of $\Delta C_O$ lies in $\mathcal B^+_n$, and $\Delta C_O\equiv0$.

**(A5)** (direct; no uniqueness, no (NE)).
1. $\hat{\mathcal D}$ is the total $\mu$-derivative at fixed $(g_0,\xi_0)$, so $\hat{\mathcal D}C^{\rm bare}=0$.
2. Hence $\hat{\mathcal D}C^{\overline{\rm MS}}=C^{\rm bare}\hat{\mathcal D}Z^{-1}=-C^{\rm bare}Z^{-1}(\hat{\mathcal D}Z)Z^{-1}=C^{\overline{\rm MS}}\gamma$.
3. **$\gamma$ is finite.** In $\overline{\rm MS}$, $Z=1+\sum_{k\ge1}Z_k\varepsilon^{-k}$, $\beta(\alpha,\varepsilon)=-2\varepsilon\alpha+\beta(\alpha)$, and $\beta_\xi$ is $\varepsilon$-independent. So $\gamma=2\alpha\partial_\alpha Z_1+$(poles), with no positive powers of $\varepsilon$.
   - *Renormalized elementary legs.* Write $\phi_0=Z_\phi^{1/2}\phi$ and $\gamma_\phi:=\frac12\hat{\mathcal D}\ln Z_\phi$ (finite). Then $\tilde G_{[O_i];\Phi}=\prod_{\phi\in\Phi}Z_\phi^{1/2}\sum_jZ_{ij}\tilde G^{\rm bare}_{O_j;\Phi}$, since amputation with renormalized propagators gives $Z_\phi^{1/2}$ per leg.
   - With $\hat{\mathcal D}\tilde G^{\rm bare}=0$ this gives
     $$\sum_j\gamma_{ij}\tilde G_{[O_j];\Phi}=-\hat{\mathcal D}\tilde G_{[O_i];\Phi}+\Big(\sum_{\phi\in\Phi}\gamma_\phi\Big)\tilde G_{[O_i];\Phi}.$$
     The right side is finite (D2); the extra term is finite because $\gamma_\phi$ and $\tilde G_{[O_i];\Phi}$ are. The identity and the amputation factor are checked symbolically in `final2_scripts/fix6_rg_legs.py`, for a generic $3\times3$ $Z$ and two legs.
   - A highest pole $\gamma_K\varepsilon^{-K}\ne0$ ($K\ge1$) would force $\sum_j(\gamma_K)_{ij}\tilde G_{[O_j];\Phi}|_{\varepsilon^0}=0$ for all $\Phi$, contradicting Lemma A.3(a) in its formal-D Laurent form.
4. Let $\varepsilon\to0$. For $\Phi=\varnothing$ the counterterm adds the inhomogeneous term; E2–E3 therefore use the Adler function. ∎

The $\xi$ term is needed: elementary-leg Green functions depend on $\xi$ at one loop, and $\beta_\xi(\alpha,1)\ne0$.

**Grades.**
- (A1), (A3): [A] (cited; Smirnov checked, with the scope limits of K2).
- (A2), (A4): [R, R_cond: A1, A3].
- (A5): [R, R_cond: A3].
- Overall: [A].

**Corollary A.5 (GI-block RG equation at $\xi=1$) [R, R_cond: A3, Eε, JL, GP′]; content [A].** For $i\in$ GI,
$$(\mu\partial_\mu+\beta\partial_\alpha)C^{GI}_i=\sum_{j\in GI}C^{GI}_j(\gamma_{GG})_{ji}.$$
*Proof.* In (A5): rest coefficients vanish (Thm B(iii)); $\gamma_{\rm alien,GI}=0$ (JL); the $\beta_\xi$ term vanishes by GP′. ∎

GP′ for twist 2, at grade [A]:
- Cor. F.2(a) holds for all $\xi\in\Xi$.
- $T^{(j)}_2$ is $\xi$-independent: it is an on-shell physical amplitude with LSZ factor 1 (BRST argument).
- $A^{(n)}=\sum Z_{GG}\cdot$tree is $\xi$-independent, because $\overline{\rm MS}$ $Z_{GG}$ is fixed recursively by $\gamma_{GG}$, $\beta$ and $\beta_\xi\partial_\xi$, and $\partial_\xi\gamma_{GG}=0$ (JL); induction on the pole order.
- $A^{(n)}=1+O(\alpha_s)$ is invertible.

Other GI coefficients: [A] (Joglekar 1977 I).

**Remark A.6 (corrects CLAIMS R-M26).** "Uniqueness lets any proven momentum-space OPE discharge C.24" is circular: lem:appM-uniqueness(a), applied to $\sum(\tilde C-C')G=\mathcal R'-\tilde N_a$, needs $\tilde N_a$ small, which is C.24. The DR route needs no C.24.

**Lemma A.7 (matching at $p=0$) [R, R_cond: CTp]; content open.** (In the outline this content is the untagged remark `rem:appM-remainder-reduction`.)

*Setting.* The massive Euclidean BPHZ model of spec §M.2, with the exact identity (C.22) $\tilde G^T=\sum_{d_O\le a}\tilde C_O\tilde G_{N[O]}+\tilde N_a$.

*Premise CTp.* There are $p$-independent $C'_O$ with $\mathcal R'=\tilde G^T-\sum C'_O\tilde G_{N[O]}$ such that every element of the span generated from $\mathcal R'$ by $\partial_p$, multiplication by $p$, and $m\partial_m$ is $\le K|q|^{D-1-a}\ln^k|q|$, per order, uniformly in $\hat q$, for $p$ in compacts **containing 0**.

*Conclusion.* Ass. C.24 holds per order. This suffices for thm:appM-scaling (ii)–(iv) and cor:appM-coordinate (reference Lemmas C.29–C.30 use only homogeneity, O(4) covariance and order-wise independence).

*Proof.*
1. **Over-subtraction.** $\partial^\alpha_p\tilde N_{a,\Gamma}(q;0)=0$ for $|\alpha|\le a-\sum_{E(\Gamma)}d_e$.
   - The maximal AB part $\gamma_0$ (the bridgeless component of $\Gamma\cup\ell_x$ containing $\ell_x$) contains every AB part, and every renormalization part meeting it, so it is compatible with all forests.
   - Hanging trees: those without legs vanish (their leaf 1PI parts are subtracted at momentum 0); one-leg trees are amputated; trees with $\ge2$ legs have leg dimension $\ge2>d_b$.
   - So $\delta_a(\gamma_0)\ge a-\sum_Ed_e$, and $(1-t_p^{\delta_a})$ acts on momenta linear in $p$. The integrability of Lemma C.22 justifies differentiation.
2. **Normalization matrix.** $M_{(E,\alpha),O}=\partial^\alpha_p\tilde G^E_{N[O]}(0)$ is block-injective at order 0. Choose a square invertible submatrix; it is invertible as a formal series, with $q$-independent entries.
3. **Matching.** Differentiating $\sum(\tilde C-C')\tilde G_{N[O]}=\mathcal R'-\tilde N_a$ at $p=0$ gives $\Delta C=M^{-1}_{\rm sq}(\partial\mathcal R'|_0)$, which is bounded by CTp. Likewise for $(m\partial_m)^j\Delta C$.
4. **Conclusion.** $\tilde N_a=\mathcal R'-\sum\Delta C\,\tilde G_{N[O]}$. ∎

CTp is unverified, and position-space theorems (Keller–Kopper Thm 11; AZ as described) do not supply it. The lemma shows that C.24 is equivalent to the existence of a $p$-independent expansion with CTp bounds. No novelty is claimed (zero-momentum normalization of Zimmermann normal products).

### Theorem B (BRST reduction of the OPE coefficients)

**Premises.** Bare DR at fixed generic $\varepsilon$, any $\xi_0$, $B$ off shell, no $\gamma_5$, D-dimensional algebra.
- **(DR-WI)** $sJ=0$, and $\sum_i(-1)^{|X_1|+..+|X_{i-1}|}\langle TX_1\cdots(sX_i)\cdots X_n\rangle=0$ exactly ('t Hooft–Veltman; BM).
- **(DR-SD)** With $\tilde\Phi=\prod_k\int d^Dx_ke^{ip_kx_k}\phi_k$:
  $$\langle T(Y\partial^\alpha\delta_LS/\delta\phi)(y)\tilde\Phi\rangle=i\sum_{k:\phi_k=\phi}\epsilon_k(ip_k)^\alpha e^{ip_ky}\langle TY(y)\tilde\Phi_{\hat k}\rangle,\qquad\epsilon_k=(-1)^{|\phi|\sum_{l<k}|\phi_l|}.$$
  This follows from $\int\mathcal D\phi\,\delta_L/\delta\phi(y)[Y\tilde\Phi e^{iS}]=0$. The factor $(-1)^{|\phi||Y|}$ cancels between the two surviving terms; $-1/i=i$; and $\delta^{(D)}(0)=0$ in DR. Check f5: 400/400.
- **(Eε)** For one composite spectator $Z=s\phi$:
  $$\langle\mathcal JZ\Phi\rangle=\sum C_O\langle OZ\Phi\rangle+\sum C^Z_{O'}(q;p_Z)\langle O'\Phi\rangle+\mathcal R'.$$
  The $C_O$ are those without $Z$. The merged coefficients $C^Z$ (hard subgraphs containing the $Z$ vertex) are polynomial in $p_Z$. All coefficients are graded-homogeneous, and $\mathcal R'=O(|q|^{1-a}\ln^k)$. Grade [A].
- **(LBC)** As in Lemma B.1.

**Conclusions.**
- **(B-i)** $sX_d\in\mathcal E$ for every $d\le a$, where $X_d=\sum_{d_O=d}C_OO$ (bare).
- **(B-ii)** $X_d$ = GI + $s$-exact + EOM, loop by loop, with GI coefficients that are power series in $g_0$.
- **(B-iii)** With JL: $X_d=\sum c'_j[O^{GI}_j]$ + aliens, with $c'=cZ_{GG}^{-1}$ finite; the rest coefficients vanish.
- **(B-iv)** Only GI operators survive between physical states (KO). At twist 2 these are $O^{(n)}_{q,g}$ (reference Lemma C.42).

**Proof.**
1. **Ward identity.** $\sum_k\epsilon'_k\langle\mathcal J\phi_1..(s\phi_k)..\phi_n\rangle=0$, with $\epsilon'_k=(-1)^{\sum_{l<k}|\phi_l|}$.
2. **Non-merged parts.** Inserting Eε, DR-WI turns the non-merged parts into $-\sum_OC_O\langle(sO)\Phi\rangle$.
3. **Merged parts.** Moving $Z_k$ next to $\mathcal J$ costs $(-1)^{(|\phi_k|+1)\sum_{l<k}|\phi_l|}$, which combines with $\epsilon'_k$ to $\epsilon_k$ (rv32_misc (d)). Since $C^{s\phi_k}$ depends on $k$ only through the field type and $p_k$, DR-SD gives
   $$M_\Phi=\langle\mathbb E(q)\Phi\rangle,\qquad\mathbb E(q)=-i\sum_{\phi,O'}O'\,C^{s\phi}_{O'}(q;-i\partial)\,\delta_LS/\delta\phi\in\mathcal E.$$
4. **Combined.** $\langle[-\sum C_O\,sO+\mathbb E]\Phi\rangle=O(|q|^{1-a}\ln^k)$ for all $\Phi$.
5. **Degree matching.** Write the bracket as $\sum_YK_Y(q)Y$ (ghost number 1). The $g_0^m$ part of $K_Y$ is $\propto|q|^{3-d^{(4)}_Y+\varepsilon(W-2)}$ with total weight $W=w_Y-m$; merged terms match the dimension of $C^{s\phi}_{O'}$ (rv32_misc (c)). Lemma A.3(a) gives $K_Y=O(|q|^{1-a}\ln^k)$. Since the exponent exceeds $1-a$, $K_Y\equiv0$, i.e. $\sum_{d_O=d}C_OsO=\mathbb E_{d+1}\in\mathcal E$.
6. **LBC.** Apply Lemma B.1 to each loop component.
7. **Physical states.** EOM operators vanish on shell, and $\langle s\Lambda\rangle=0$ (KO). For partonic trees: $B$ legs give $p\cdot\varepsilon=0$, and there are no ghosts. ∎

**Grades.**
- (B-i), (B-ii): [R, R_cond: Eε; LBC cited].
- (B-iii): add JL.
- (B-iv): add KO.
- Content: [A].

B holds identically in $\xi_0$, so it may be used with $\xi_0=Z_3\xi_R$, $\xi_R=1$. No novelty is claimed (Joglekar 1977 II).

**Reference Prop. C.44** is valid as a conditional statement. The error is Rem. C.45, which calls (B2) "the direct generalization of Thm C.35": the true generalization Eε has merged terms, which (B2) omits. With Eε one obtains $sX_d\in\mathcal E$ rather than $sX_d=0$, and LBC restores the physical conclusion. The second identity of (B1) is trivially true in DR.

**Lemma B.1 (LBC at formal $D$, loop by loop; outline `lem:appM-lbc-formal`; formerly Remark B.1) — 数学 (no tag); uses K6 and invariant theory.** 本书给出的推导 of the formal-D, loop-by-loop form of the local BRST cohomology theorems of BBH, Henneaux 1996 and BHHS.
1. **Rescaling.** Set $\tilde\phi=g_0\phi$ for all fields.
   - Then $S=g_0^{-2}\tilde S[\tilde\phi]$, and $\tilde s$, $\mathcal E$ and GI are $g_0$-independent: $\tilde s\tilde A=\partial\tilde c-i[\tilde A,\tilde c]$, $\tilde s\tilde\psi=i\tilde c\tilde\psi$, $\tilde s\tilde c=-\frac12[\tilde c,\tilde c]$, $\tilde s\tilde{\bar c}=\tilde B$.
   - The rescaled fields have $\varepsilon$-independent dimensions.
   - Monomials of $S$ have weight 2, so $s$ and $\mathcal E$ preserve the total weight $W=w-m$.
   - A connected hard subgraph with $E$ soft legs and $L$ loops carries $g_0^{2L+E-2}$ (vertex count, two bivalent current vertices). So the $L$-loop part has $W=2-2L$: weight grading = loop grading = the $\varepsilon$-classes of step 5 of Theorem B. Hence $X^{(L)}_d=g_0^{2L-2}\tilde X^{(L)}_d(\tilde\phi)$, and (B-i) splits as $\tilde s\tilde X^{(L)}_d\in\tilde{\mathcal E}$.
2. **Finite-dimensional spaces.** Let $V^g$ be the $\mathbb Q$-space of formal-D polynomials in $\tilde\phi$ of given 4D dimension, ghost number $g$ and tensor type (indices contracted with $g$ and $\hat q$; all $\gamma^{[r]}$). It is finite-dimensional. Set $K=\{X\in V^0:\tilde sX\in\tilde{\mathcal E}\}\supset\mathcal L=GI+\tilde s V^{-1}+\tilde{\mathcal E}$. Both are $D$-independent, since $\tilde s$ creates no self-contractions.
3. **Specialization.** For **even** $n\ge n_0$, specialization $D\to n$ is injective on $V$: by the SFT for O($n$), and because the $\gamma^{[r]}$, $r\le n$, are independent. For odd $n$ the top element is central and $\gamma^{[r]}\propto\gamma^{[n-r]}$ (f7 (b)); evenness is sufficient, not necessary. Averaging over compact Pin($n$) (Euclidean real form, or Weyl's unitarian trick), together with the FFT, shows that covariant elements of $\tilde{\mathcal E}$, GI and $\tilde s(\cdot)$ in dimension $n$ are specializations.
4. **LBC in dimension $n$.** BBH, Henneaux 1996 and BHHS give $K(n)=\mathcal L(n)$; hence $K=\mathcal L$.
5. **Power series.** $\tilde X^{(L)}_d\in\mathcal L\otimes\mathbb C$, with parts of the same dimension and type. A GI monomial with $k_j$ factors $\tilde F,\tilde\psi,\tilde{\bar\psi}$ equals $g_0^{k_j}G_j(\phi)$, with $G_j$ polynomial in $g_0$ (note $\tilde D=D$). So the GI part of $X^{(L)}_d$ is $\sum\gamma_jg_0^{k_j+2L-2}G_j$. Non-identity colour-singlet GI monomials have $k_j\ge2$, and the identity occurs only for $\Phi=\varnothing$, where $L\ge1$. All exponents are $\ge0$. ∎

### Theorem I = A + B + twist classification [A]

The statement is that of §0(1). Gap analysis:
1. **DR + B.** Modulo (A1), (A3), Eε (O1) and JL at full-text level.
2. **BPHZL.** Convergence is known; whether the unread sources (Zimmermann 1973, AZ, Zav'yalov, LS–dV, Bergère et al.) contain a C.24-type estimate is open (O3).
3. **Flow equations.** Pure YM only (O2).
4. **Hollands 2008.** Pure YM, Epstein–Glaser framework; §4.1.3 (read, K5) gives the closure of the OPE on $\hat s$-closed fields there.

## 4. Part II: from Euclidean to forward kinematics

**Lemma F.0 (forward 2-forests; outline `lem:appM-forward-forests`) [R, R_PT]; elementary.**

*Setting.* External momenta $p$ at $P_1$, $-p$ at $P_2$, $q$ at $J_1$, $-q$ at $J_2\ne J_1$, with $p^2=0$.

*Claim.* $\mathcal F=Q^2(\hat F_0+\omega\hat F_1)$, where $\hat F_0=\sum_{T:c_q\ne0}\alpha^{E\setminus T}$, $\hat F_1=-\sum_Tc_pc_q\alpha^{E\setminus T}$, and $c_p,c_q\in\{0,\pm1\}$. In particular ${\rm mon}\hat F_1\subset{\rm mon}\hat F_0$ with $|{\rm coef}|\le1$.

*Proof.* For a 2-forest $T$, $-s_T=Q^2(c_q^2-c_pc_q\omega)$. ∎

**Lemma F.1 (Newton-polytope domination; outline `lem:appM-newton`) — 数学 (no tag); standard tools.**

*Setting.* $\mathcal G_\lambda=\mathcal U+\hat F_0+\lambda\hat F_1$, with $\hat F_1$ dominated, $P={\rm Newt}(\mathcal U+\hat F_0)$ full-dimensional, and $|\lambda|\le r<1$.

*Claims.*
- **(a)** $\int\alpha^{s-1}g\,\mathcal G_\lambda^{-c}$ and all Taylor-term integrals (numerator $g\hat F_1^n$, exponent $c+n$) converge on a common open set.
- **(b)** $I(\lambda)=\sum\lambda^nI_n$ there.
- **(c)** The candidate poles are $\lambda$-independent, and $\frac1{n!}\partial^n_\lambda I|_0=I_n$ after continuation.

*Proof.*
- (a) The coefficients $1+c\lambda$ ($|c|\le1$) lie in $|z-1|\le r$, hence in $|\arg|\le\arcsin r$, so Schultka Thm 3.1 applies. Equivalently, the polynomial is completely non-vanishing on the orthant (all truncations have positive real part), and BFP Thm 2.2 applies; for exponent 1 this is Nilsson–Passare Thm 1. Moreover $s+m\in c\,{\rm int}P+nP\subset(c+n){\rm int}P$.
- (b) $\sum|\binom{-c}n|r^n\le(1-r)^{-|c|}$ and $|\hat F_1|\le\mathcal G_0$; then Tonelli–Fubini.
- (c) On Kaneko–Ueda cubes (Schultka's chart construction in the proof of his Thm 3.1), $\mathcal G_\lambda=x^{m_\sigma}(f_{\sigma,0}+\lambda f_{\sigma,1})$ with real part $\ge(1-r)f_{\sigma,0}>0$. Conclude with Gel'fand–Shilov continuation and the identity theorem. ∎

**Lemma F.6 (matroid form; DR admissibility; outline `lem:appM-matroid`) — 数学 (no tag); known in substance.**

*Setting.* $G_0=G+e_q$ ($e_q$ joining $J_1$ and $J_2$), with $N$ lines and $L$ loops.

*Claims.*
- **(a)** $\hat F_0=\mathcal U(G/\{J_1{=}J_2\})$ and $\mathcal U(G_0)=x_q\mathcal U(G)+\hat F_0$. Hence Newt$(\mathcal U+\hat F_0)\cong P(M^*(G_0))$ (drop $x_q=L+1-\sum x_e$).
- **(b)** $\dim=N+1-c(M(G_0))$; the polytope is full-dimensional iff $G_0$ is loopless and 2-connected.
- **(c)** The facet normals are $e_e$ ($d=0$), $-\mathbb 1$ ($d=-(L+1)$), $-\mathbb 1_F$ ($d=-r^*(F)\le-1$) and $\mathbb 1_{E\setminus F'}$ ($d=L+1-r^*(F'\cup e_q)\ge1$). So $d=0$ only for coordinate facets.
- **(d)** For ${\rm Re}\,a_e>0$, polynomial numerators, Tarasov shifts, Taylor terms and all $\omega\in\mathcal C$, the only $D$-independent candidate poles are $a_e\in-\mathbb N_0$.

*Proof.*
- (a) Deletion–contraction.
- (b) Feichtner–Sturmfels Prop. 2.4 ($\dim P_M=n-c(M)$, applied to $M^*(G_0)$ with $c(M^*)=c(M)$) and Whitney.
- (c) FS Prop. 2.3 (facets among the flat inequalities; facet-defining flats: Prop. 2.6), with $r^*(F)\ge1$ since $G_0$ is bridgeless. Copy: `literature/feichtner_sturmfels_math0411260.txt`.
- (d) Schultka Thm 3.6 = BFP Thm 2.4. Its coefficient condition (completely non-vanishing on the orthant) holds for all $\omega\in\mathcal C$, because $1=\frac{(1+\omega)+(1-\omega)}2$ puts the coefficients $1,1\pm\omega$ on a line that misses 0 when ${\rm Im}\,\omega\ne0$, and makes them positive for real $|\omega|<1$. The poles lie at $\langle u_F,s\rangle-c\,d_F+d_F(\cdot)\in-\mathbb N_0$, which is $D$-dependent unless $u_F=e_e$. ∎

*Attribution.* (b)–(d) and (F3) are the $q$-only generic-Euclidean case of Schultka §4 (Def 4.3, Thm 4.15, Prop 4.17, Cor 4.18, Prop 4.29, Rem 4.30/Speer, Prop 4.31, Thm 4.32); see also Borinsky Thm 32 and AHM. For (a): Tellander–Helmer Thm 3.1 proof; Walther Lemma 3.3.

*Checks.* f3 (21 + 1028 graphs, 0 failures), r1, r2, rv2_matroid, rv2_facets_d0, rv22_numeric (H).

### Theorem F (forward on-shell DR amplitude; outline `thm:appM-forward-expansion`) [R, R_PT] per graph

**Setting.** $\Gamma$ is a connected graph of the amputated forward amplitude of a massless on-shell parton ($p^2=0$) with two currents.

**Exclusions.**
- (i) $\pm p$ bridges are external-leg corrections, removed by amputation; the DR LSZ factor is 1.
- (ii) 0-momentum bridges are gluons. Their non-target side carries a single adjoint index, so they vanish by colour, graph by graph.
- $\pm q$ bridges cannot occur.

**Definition.** The parametric (Lee–Pomeransky/Speer) integral at $p^2=0$.
- For real $|\omega|<1$ all coefficients are positive (F.0). Since $\mathcal F>0$ on the orthant, the $(\mathcal F-i0)$ prescription is immaterial and the integral equals the $i\epsilon$ momentum integral.
- Elsewhere it is defined by continuation.
- Components are contracted with tensors polynomial in $p$; $\nu^{-k}$ prefactors are treated in F.7–F.8.

**Claims.**
- **(F1)** For $\omega\in\mathcal C=\mathbb C\setminus((-\infty,-1]\cup[1,\infty))$, convergence on an $\omega$-independent open set; meromorphic continuation with $\omega$-independent candidate poles. Every Laurent coefficient is holomorphic on $\mathcal C$.
- **(F2)** For $|\omega|<1$, each Laurent coefficient equals $\sum_n\omega^nI^{[k]}_n$ (naive Taylor terms), absolutely and locally uniformly.
- **(F3)** Degenerate $G_0$ gives zero on both sides.

**Proof.**
- Tarasov reduction, then F.0.
- For ${\rm Im}\,\omega\ne0$ the coefficients $\{1,1\pm\omega\}$ lie in an open half-plane (rv22 (F)), so Schultka Thm 3.1 applies; Kaneko–Ueda cubes give joint holomorphy. Laurent coefficients commute with the $\omega$-series by joint holomorphy plus Cauchy estimates on $|\varepsilon|=\rho$.
- (F2): F.1, plus pointwise equality of parametric and naive momentum-space Taylor terms (Schwinger–Gauss); restrict to DR by F.6(d).
- (F3): scaling invariance $t^u$. ∎

**Status.** Theorem F is the book's rigorous proof (本书给出的严格证明) of the **analytic step** of the method of projectors. 本书新结果 is withheld (O12).
- *Use without proof in the literature.* LNvRV 1997 §2 (checked): $P_N$ "is applied to the integrands of all Feynman diagrams", with only the remark on a "considerable rearrangement of infrared and ultraviolet divergences"; there is no proof of the analytic step. GLT 1983, GL 1987 and LvRV 1994 were not checked. Nothing is claimed about their content beyond their use of the method.
- *Closest prior result: Semenova–Smirnov–Smirnov, EPJC 79 (2019) 136, §7, Prop. 6* (checked; copy).
  - SSS consider Lee–Pomeransky integrals $\int P^{-\delta}$ with $P(x,t)=\sum_wc_wx^{w}t^{w_{n+1}}$ and **all $c_w>0$**. When the Newton polytope has a single essential facet, they prove the all-order expansion as $t\to+0$ by expanding the integrand in the dominated $t$-terms. The convergence of every term follows from their Prop. 2, under an auxiliary analytic regularization. As an instance they name the small-momentum expansion of a graph "with no massless thresholds", which is analytic up to the first threshold.
  - This is the mechanism of Lemma F.1.
  - In the forward Compton polynomial $\mathcal U+\hat F_0+\omega\hat F_1$ the only essential facet is the base facet. Since ${\rm mon}\hat F_1\subset{\rm mon}\hat F_0$ (Lemma F.0), every point $(w,1)$ lies one unit above the point $(w,0)$, so any face with inward normal $(r',1)$ lies in the base. But $\hat F_1$ has coefficients $-c_pc_q\in\{0,\pm1\}$, so SSS's positivity hypothesis fails for the monomials with $c_pc_q=+1$, whose coefficient is $1-\omega$.
- *What Theorem F adds to SSS 2019 Prop. 6:*
  - (i) sign-indefinite dominated $\omega$-terms (coefficients $1-\omega$);
  - (ii) convergence of the $\omega$-series for complex $|\omega|<1$, not only an asymptotic expansion as $t\to+0$;
  - (iii) holomorphy of every Laurent coefficient on the cut plane $\mathcal C$ (F1);
  - (iv) the DR identification F.6(d): the only $D$-independent candidate poles are $a_e\in-\mathbb N_0$, so the analytic regulator is removed term by term.

  For fixed $\omega$, the convergence/continuation part of (F1) is an instance of Schultka Thms 3.1/3.6 = BFP Thms 2.2/2.4 and of Nilsson–Passare Thms 1–2 (all checked; completely non-vanishing coefficients $1,1\pm\omega$).
- *Jantzen, JHEP 12 (2011) 076* (checked; copy). It gives a general formalism for the expansion by regions without a general convergence proof (§3, p. 17: "I cannot provide a rigorous proof for this convergence issue in the general case"). Its "forward scattering" example (§7) is the high-energy small-momentum-transfer limit $Q^2\gg\vec r_\perp^{\,2}$ of the scattering of two light-like particles (hard, collinear and Glauber regions). That is the Glauber/Regge limit, not the forward Compton expansion in $\omega$.
- *Searches.* The four reviewer INSPIRE searches recorded in rounds 1–3 found no prior proof, but they did not target the expansion-by-regions literature; SSS 2019 was found only in the final review. SSS 2019 §7 and Nilsson–Passare are now on the O12 check list.
- The $\overline{\rm MS}$ identification is Cor. F.2 [A].

**Lemma F.7 ($T_2$ projection in $D$ dimensions; outline `lem:appM-t2-projector`) [R, R_PT].**

*Setting.* Quark target averaged with $\frac12\not p$; gluon target averaged with $d_{ab}/(D-2)$, where $d_{ab}=-g_{ab}+(p_aq_b+q_ap_b)/\nu-q^2p_ap_b/\nu^2$. Then $d\cdot p=d\cdot q=0$, ${\rm tr}\,d=2-D$, and $d$ has degree 0 (f4 (d)).

- **(a) Projector.** For transverse $T\in{\rm span}\{g,pp,pq,qp,qq\}$,
  $$T_2=\frac{Q^4[(D-1)S_1-(\nu^2/Q^2)S_2]}{(D-2)\nu^3},\qquad S_1=ppT,\ S_2=gT.$$
  This follows from $S_1=-\frac{\nu^2}{Q^2}T_1+\frac{\nu^3}{Q^4}T_2$ and $S_2=-(D-1)T_1+\frac\nu{Q^2}T_2$ (f4 (a); rv22 (A); rv32 (e)).
- **(b) Quark target.**
  - Each naive term $T_n$ is transverse: expand $q_\mu T^{\mu\nu}(\lambda p)=0$ termwise, as licensed by Theorem F.
  - By the FFT and $p^2=0$, $T_n=a\nu^ng+b\nu^{n-2}pp+c\nu^{n-1}pq+c'\nu^{n-1}qp+e\nu^nqq$, with $b=0$ for $n<2$ by polynomiality.
  - Transversality gives $c=c'=b/Q^2$ and $a=eQ^2-b/Q^2$, and the projector returns $b\nu^{n-1}$.
  - So the $\omega^{-3..0}$ terms cancel for every $n$: $T_2$ is holomorphic on $\mathcal C$, $O(\omega)$, with naive Taylor series.
  - Oddness follows from crossing of the *summed* graphs.
  - Checks: f4 (b) ($n\le8$), rv22 (B). Tree-level quark handbag in $D$ dimensions (f4 (c)): $T_2=4\omega/(1-\omega^2)$, $T_1=2\omega^2/(1-\omega^2)$.
- **(c) Gluon target.** $T=H_0+H_1/\nu+H_2/\nu^2$, with Theorem F applied to each $H_k$. This gives meromorphy on $\mathcal C$, holomorphy on $\mathcal C\setminus\{0\}$, and the naive Laurent expansion. Regularity at 0 follows from Cor. F.2 [A] or Lemma F.8. ∎

### Corollary F.2 (forward partonic OPE at every order; outline `cor:appM-forward-ope`) [A]

*Premises.* Theorem F, F.6, F.7, (A3), Theorem B, JL, Lemma NE(ii), Lorentz covariance of $\overline{\rm MS}$ counterterms.

- **(a)** For $|\omega|<1$, at every order and Laurent order, $T^{\mu\nu}_j=\sum_OC^{\mu\nu}_O\langle j|[O]|j\rangle$. Only twist-2 GI operators contribute, and $A^{(n)}_{i/j}=\sum Z\cdot$tree. Thus $T^{(j)}_2=4\sum_{n\,\rm even}\omega^{n-1}\sum_iC^{(n)}_{2,i}A^{(n)}_{i/j}$, and $T^{(g)}_2$ is regular at 0.
- **(b)** For $|q|\ge4p^0$, uniformly in direction, $|T_j-\sum_{d_O\le N}C_O\langle j|[O]|j\rangle|\le C|q|^{1-N}(1+\ln|q|)^k$.

*Proof.*
1. **Graphs.** The forward graphs are exactly the AI two-leg hard graphs.
2. **Naive terms.** By Theorem F and F.7 the naive terms sum to $\sum C^{\rm bare}_OV_O(p,-p)$; on-shell bare matrix elements are trees because loops are scaleless.
3. **Renormalization.** $C^{\rm bare}=C^{\overline{\rm MS}}Z$. Theorem B and JL: rest coefficients vanish, GI mixes into GI + aliens, aliens mix only into aliens.
4. **Aliens and evanescent operators.**
   - $\langle j|[O]|j\rangle=\sum_QZ_{OQ}\,{\rm tree}_Q$.
   - **GI** forward on-shell massless trees are built from $p$ alone: $p^2=0$, $\not pu=0$, ${\rm tr}(\not p\gamma^{[r]})=0$ for $r\ne1$, and GI two-gluon vertices are transverse. **Alien** trees contracted with the physical $d_{ab}$ may contain $q$, but they vanish (next bullet). So ${\rm tree}_Q\ne0$ only for GI $Q$ on the $[n]$-isotypic part of dimension $n+2$, i.e. within $\mathcal B^+_n$.
   - $Z$ is Lorentz covariant and preserves dimension, so only $Z$ restricted to that part matters. By Lemma NE(ii) it contains no evanescent and no four-quark operator. Hence evanescent operators contribute nothing, even through mixing $Z_{EQ}$.
   - Aliens: with the **physical** average $d_{ab}$, contracted alien tree vertices vanish (EOM vertices $\propto p^2,p_a$; $B$ legs $\propto p_a$; no external ghosts). This is consistent with R-M24, and says nothing about off-shell or off-forward matrix elements (Hamberg–van Neerven; Collins–Scalise; Falcioni–Herzog).
5. **Gluon regularity.** GI two-gluon vertices are transverse, so $d_{ab}V^{ab}=-g_{ab}V^{ab}$ is polynomial; apply F.7(b).
6. **Twist.** With $p^2=0$ only twist 2 survives, with finite coefficients by (A3).
7. **Bound (b).**
   - $|\omega|\le2p^0/|q|\le\frac12$ and $|\hat P|_E^2=2(p^0)^2-|\nu|^2/Q^2\le2(p^0)^2$ (rv22 (G), rv32 (g)).
   - Cauchy estimates on $|\omega|=\frac34$ bound the tails of $T_1$ and $T_2/\omega$.
   - Then use $T=-\tilde gT_1+2\hat P\hat P(T_2/\omega)/Q^2$. ∎

asm:appM-forward is **reduced** to (A3) + Eε + B + JL, not discharged; prop:dis-ope-forward stays [A]. One-loop instances: c_dis, $N\le8$.

**Lemma F.8 (gluon regularity from OSWI; outline `lem:appM-gluon-regularity`) [R, R_cond: OSWI]; content [A].**

*Premise OSWI.* $p^aM_{ab}\varepsilon^b=0=\varepsilon^aM_{ab}p^b$ for all $\varepsilon$ with $\varepsilon\cdot p=0$ (including $\varepsilon=p$). Equivalently $p^aM_{ab}\propto p_b$: the BRST form, with the ghost amplitude inside the factor.

*Claim.* The naive terms of $d^{ab}M_{ab}$ are polynomial, so $T^{(g)}_2$ is regular at $\omega=0$. Theorem B is not used.

*Proof.*
1. Expand OSWI termwise (F2): $p^aM_{n,ab}\varepsilon^b=0$.
2. By the FFT, $p^aM_{n,ab}=\alpha_np_b$ and $M_{n,ab}p^b=\alpha'_np_a$, with polynomial $\alpha_n,\alpha'_n$.
3. With $p^2=0$: $d^{ab}M_{n,ab}=-g^{ab}M_{n,ab}+\alpha_n+\alpha'_n$ (rv32 (f)).
4. This is transverse, because the EM Ward identity has no contact terms for EM-neutral gluons. Apply F.7(b). ∎

OSWI at theorem level is open (O14).

**Corollary F.3 (outline `cor:appM-cut-plane`).**
- (a) Quarks: holomorphic on $\mathcal C$, [R, R_PT]. Gluons: holomorphic on $\mathcal C\setminus\{0\}$, [R, R_PT]; at $\omega=0$, [A].
- (b) ${\rm Disc}\,T_2^{(j)}=4\pi iF_2^{(j)}$: [A] (DR cutting rules for Laurent coefficients; a definition if $F_2:={\rm Disc}/4\pi i$).
- (c) Moments for even $n>A+1$: [A] (O4).
- c_dis checks one loop, $N\le8$.

**Example F.3 (forward triangle; outline `ex:appM-forward-triangle`) — exact one-loop computation; no tag.**
$$I=\frac{\Gamma(a-\frac D2)}{\prod\Gamma(a_i)}(Q^2)^{\frac D2-a}B(\tfrac D2-a_2,\tfrac D2-a_1-a_3)B(a_1,a_3)\,{}_2F_1(a-\tfrac D2,a_1;a_1+a_3;\omega).$$
- Its $\omega^n$ coefficients equal the naive terms identically (f2 (A); rv32_triangle (A)).
- At $a_i=1$ the poles are $-1/((n+1)\varepsilon)$, from ${}_2F_1(1+\varepsilon,1;2;\omega)$.
- Direct quadrature at six complex $\omega$, four of them outside the disk, agrees to $10^{-10}$ (rv32 (B)). The final reviewer's own simplex quadrature (`review_final_scripts/fr_triangle.py`) agrees at $\omega=0.3$, $0.2+0.5i$, $-1.5+0.4i$ to $\le5.5\times10^{-13}$.
- f2 (B) point 2 agrees only to $1.2\times10^{-5}$ (endpoint singularity; exact-$y$ check $10^{-19}$).
- Independent confirmations: rv21_box (box, all powers free) and rv2_ladder2 (two-loop ladder).

**Example F.4 (non-uniformity; outline `ex:appM-forward-nonuniform`) — exact one-loop computation; no tag.** For $p^2=-P^2$, $\omega=0$, $D=4$: $Q^2I=\ln(Q^2/P^2)+2+O(P^2\ln)$, whereas the on-shell DR value is a pure pole (f2 (D)).

### Proposition F.5 (zero-momentum twist-2 insertions exist in DR; outline `prop:appM-zero-momentum-insertion`)

**Grade.** Proposed **[R, R_PT]**: per graph and per order, with the cited theorems (BM I Thm 1, BM II Thm 1, Prop. 1 and Lemma 3) read in full text, their hypotheses checked in step 1, and the identification of step 2 written out here. **Per LEAD_DECISIONS LA-4 the book prints [A] with the status note until step 2 has been independently confirmed**; on confirmation the lead author upgrades the tag (CHANGELOG v2.4).
- *Weakest step:* 2(iv). It applies BM's ε-Lemma argument, in the way BM I §III applies it to ε-proportional counterterms, to reduced graphs carrying the vertex parts $\eta^kP_j$ of BM II's IR subtraction. Steps 1, 2(i)–(iii) and 3 use only checked statements and elementary analysis.
- 本书给出的推导: an instance of BM II Thm 1 / BM I Thm 1; no novelty is claimed.

**Setting.**
- Massless QCD (D1) in a covariant gauge with any $\xi_0$, with $B$ off shell or integrated out.
- Fix $n\ge2$, a twist-2 operator $O^{(n)}_i$ ($i=q,g$; D7, indices free or contracted with a fixed vector), and elementary fields $\phi,\phi'\in\{A,\psi,\bar\psi,c,\bar c,B\}$.
- $G^{(O)}_{\phi\phi'}(p)$ is the term of first order in $\lambda$ of the connected two-point function $\langle\phi(p)\phi'(-p)\rangle$ in the theory $\mathcal L+\lambda\int d^Dx\,O^{(n)}_i(x)$, i.e. the insertion of $\int O^{(n)}_i$ at zero momentum transfer.
- Renormalization is minimal: the counterterms linear in $\lambda$ are the MS renormalization of the integrated operator. MS-bar is MS at the scale $\bar\mu^2=\mu^2e^{\gamma_E}/(4\pi)$, so every statement below holds in both.
- Green functions are non-amputated; amputation of free propagators is multiplication by a polynomial in $p$.

**Definition (Breitenlohner–Maison).**
- For a graph $G$, $\mathcal T_{G,\eta}(p,D)$ is the dimensionally regularized amplitude with every line damped by $e^{-\eta\alpha_\ell}$ in the α-representation ($\eta>0$; BM's ε). Equivalently, every massless denominator is $k^2+i\eta$: the Feynman $i\epsilon$ kept finite.
- $C$ is the pole part at $D=4$, and $\mathcal R^C_{G,\eta}$ is the MS-subtracted damped amplitude (forest formula with $C$).
- The dimensionally renormalized amplitude of $G$ is $\mathcal R_G:=\lim_{\eta\to0}\mathcal R^C_{G,\eta}(p,4)$ in $\mathcal S'(\mathbb R^4)$ (BM I §III; BM action-principle paper, Thm 1).

**Claims.**
- **(a) Existence.** For every graph $G$ of $G^{(O)}_{\phi\phi'}$ at every order in $g$, $\mathcal R^C_{G,\eta}(p,D)$ is analytic at $D=4$ for $\eta>0$. The limit $\eta\to0$ exists in $\mathcal S'(\mathbb R^4)$ for $D$ in a neighbourhood of 4, in particular at $D=4$. Hence $G^{(O)}_{\phi\phi'}$ exists as a tempered distribution at every order.
- **(b) Independence of BM II's IR subtraction.** With BM II's subtraction operator $S=C+T(1-C)$, $\lim_{\eta\to0}\mathcal R^S_{G,\eta}=\mathcal R_G$.
- **(c) Form on $p^2<0$.** On the open set $\{p^2<0\}$, $\mathcal R_G$ (hence $G^{(O)}_{\phi\phi'}$) is real-analytic. With polynomial covariants $T_i(p)$, homogeneous of degree $d_i$ and built from $p$, $g$, $\gamma$ and the index structure of $O^{(n)}$,
  $$G^{(O)}_{\phi\phi'}(p)=\sum_iT_i(p)\,(-p^2)^{(w-d_i)/2}\sum_{k\le L}c_{ik}\ln^k(-p^2/\mu^2),$$
  where $w$ is the momentum dimension of $G^{(O)}_{\phi\phi'}$ and $L$ the loop order: the exponents are fixed by dimensional analysis.

**Proof.**

*Step 1 (hypotheses of BM II Thm 1).* BM II Thm 1 requires a connected graph whose internal vertices have IR degree $\ge4$, fields of IR degree $\ge1$, and propagators of the form (3.15).
- The fields have $\Delta_A=\Delta_c=\Delta_{\bar c}=1$, $\Delta_\psi=\frac32$, $\Delta_B=2$, all $\ge1$ (K1).
- In any covariant gauge the gluon propagator is a sum of two terms of form (3.15), each of IR degree 1 (K1).
- The QCD vertices are internal, with $\Delta=4$.
- The insertion vertex carries zero momentum, so it is an *internal* vertex in BM's sense (the momenta of internal vertices are set to zero; BM I p. 41). Every monomial of $O^{(n)}_q$ or $O^{(n)}_g$ has $\Delta=\delta=n+2\ge4$: each $iD$ contributes $\partial$ or $gA$, of IR degree 1 either way, and $\Delta_\psi=\frac32$, $\Delta_{\partial A}=2$.
- The two external vertices are attached by one line each.

So BM II Thm 1 applies to every graph $G$: $\mathcal R^S_{G,\eta}(p,D)$ is analytic at $D=4$ and has a limit $\eta\to0$ in $\mathcal S'$ near $D=4$ (BM II p. 72). Graphs with tadpoles vanish (pp. 72–73).
- For $\xi_0=1$ with $B$ integrated out, all propagators have simple poles, and BM I Thm 1 with §II.3 (internal vertices of dimension $\ge4$ allowed; p. 45) gives (a) directly, with MS from the start. Step 2 below is needed to cover general $\xi$ through BM II, and it proves (b).

*Step 2 (identification: $\lim\mathcal R^S=\lim\mathcal R^C$).*
- **(i) Decomposition.** BM II Prop. 1 with $S_1=C$, $S_2=T(1-C)$ (eq. (3.13), p. 61) gives
  $$\mathcal R^S_{G,\eta}=\sum_F\mathcal R^C_\eta(G,F,Y),\qquad Y_{H,\eta}=-T^{\Omega_H-1}(1-C)\bar{\mathcal R}^S_{H,\eta}.$$
  The sum runs over sets $F$ of disjoint 1PI subgraphs $H$ with $\Omega_H>0$. $\mathcal R^C_\eta(G,F,Y)$ is the MS-renormalized amplitude of the reduced graph $G/F$ with the vertex parts $Y_{H,\eta}$ inserted, and $\bar{\mathcal R}^S_H$ is $H$'s amplitude with the $S$-subtractions of its proper subgraphs. The term $F=\varnothing$ is $\mathcal R^C_{G,\eta}$.
- **(ii) Massless degrees.** With the canonical IR degrees $\Delta=\delta$ (admissible, since every integrated monomial has $\Delta\ge4$) and no massive line, $s_H=0$. Hence $\Omega_H=\omega_H$ for every $H$ (BM II p. 69).
- **(iii) Homogeneity lemma.** Write $g_0=\mu^{(4-D)/2}g$.
  - *Structure.* Every term of $\bar{\mathcal R}^S_{H,\eta}$ is $\mu^{(4-D)h_t}$ ($h_t\le h_H$ the loop number of a reduced graph) times a function of $(p,\eta)$ homogeneous of degree $\omega_H-(4-D)h_t$ in $(p,\sqrt\eta)$. This follows from the α-representation, where the scaling is $\alpha\to\alpha/\lambda^2$; BM action principle p. 35 shows that ε enters only through $t_G\sqrt\varepsilon$. The structure is preserved by both operations:
    - the pole parts $C$ are polynomials in $p,\sqrt\eta$ with $\mu$-independent coefficients (BM action principle Thm 1; BM I §III);
    - the Taylor coefficient of order $j$ at $p=0$ of a function homogeneous of degree $w$ in $(p,\sqrt\eta)$ is homogeneous of degree $w-j$ in $\sqrt\eta$.
  - *Coefficients.* By induction over forests, the coefficient of a monomial of degree $j\le\Omega_H-1$ in $p$ in $Y_{H,\eta}$ is a finite sum
    $$c_j(\eta,\mu,D)=\sum_t\mu^{(4-D)h_t}\,\eta^{(\Omega_H-j-(4-D)h_t)/2}\,g_t(D),\qquad g_t\ \text{meromorphic}.$$
  - *Analyticity.* $c_j$ is analytic at $D=4$ for $\eta>0$: the $S_2$-vertex parts are analytic at $n=4$ (BM II pp. 61–62). The candidate poles in $D$ of all terms are rational with denominators $\le h_G$, because the singular manifolds are $\omega_H(n)\in\mathbb Z_{\ge0}$ (BM action principle §II.1). So for $0<r<1/(2h_G)$, $c_j$ is analytic on $|D-4|\le r$.
  - *Uniform vanishing.* On $|D-4|=r$, every exponent has real part $\ge(1-rh_H)/2\ge\frac14$, so $\sup_{|D-4|=r}|c_j|\le K_j\eta^{1/4}$ for $\eta\le1$. By the maximum principle and Cauchy's formula, $c_j$ and all its $D$-derivatives at $D=4$ vanish as $\eta\to0$.
  - *Form at $D=4$.* More precisely, $c_j(\eta,\mu,4)=\eta^{(\Omega_H-j)/2}P_j(\ln(\mu^2/\eta))$ with $P_j$ a polynomial with constant coefficients.
    - At $D=4$, $c_j$ is jointly homogeneous of degree $\Omega_H-j$ in $(\sqrt\eta,\mu)$, so $c_j=\mu^{\Omega_H-j}\varphi_j(\eta/\mu^2)$.
    - It is also a polynomial in $\ln\mu$ of degree $\le h_H$, because the pole orders are $\le h_H$.
    - Setting $\eta=1$ gives $\varphi_j(x)=x^{(\Omega_H-j)/2}P_j(-\frac12\ln x)$.
  - *Checks.* `final2_scripts/fix1_homogeneity.py` verifies all four properties on a quadratically divergent example ($\Omega_H=2$): analyticity at $D=4$, uniform vanishing on $|D-4|=0.4$, Taylor coefficients $O(\eta|\ln\eta|^{m+1})$, and $c_0(\eta,\mu,4)=\eta\,(8\gamma_E-4-8\ln(\mu^2/\eta))$. See also `fix1_bm_illustration.py` (b).
- **(iv) The insertions vanish.**
  - *IR degree.* A vertex part $\eta^kP_j(p_H)$ with $2k=\Omega_H-j\ge1$ has IR degree $d_H+j$, where $d_H$ is the sum of the IR degrees of the fields on the external lines of $H$. Moreover $d_H+j+2k=d_H+\Omega_H=4+\sum_{V\in H}(\Delta_V-4)\ge4$ (definition of $\Omega_H$ and BM II (3.14)).
  - *BM's situation.* This is exactly the situation treated in BM I §III for counterterms proportional to powers of ε with lowered dimension. Counting the explicit $\eta^k$ with weight 2, the reduced graph satisfies BM's IR condition, and the extra factor $\eta^k$ with ${\rm Re}\,k\ge\frac14>0$ makes its contribution vanish as $\eta\to0$.
  - *Cited step.* This rests on BM's tadpole argument with the ε-Lemma, whose last clause states $\lim\varepsilon^kf(q,\rho+2k,\varepsilon)=0$ for $k>0$ (BM II Lemma 3; BM I App. B Remark: ${\rm Re}\,k>0$). Products of several vertex parts carry the product of the $\eta$-powers.
  - *Consequence.* $\mathcal R^S_{G,\eta}-\mathcal R^C_{G,\eta}\to0$ in $\mathcal S'$, so $\lim\mathcal R^C$ exists and equals $\lim\mathcal R^S$. This proves (a) for every $\xi$, and (b).
  - *Consistency.* BM II Prop. 3 asserts that the IR counterterms of decomposition (ii) have limits as $\eta\to0$; here those limits are 0. BM II §1 states that for massless theories the pole subtraction alone suffices.
  - *Illustration.* `fix1_bm_illustration.py` (c): an inserted counterterm $\eta\ln\eta$ on a soft line of a one-loop bubble contributes $\eta\ln\eta\cdot\ln(1/\eta)\to0$.

*Step 3 (form on $p^2<0$).*
- *Covariance.* BM's construction is Lorentz covariant, and limits of covariant distributions are covariant.
  - Use the diffeomorphism $\{p^2<0\}\cong(0,\infty)\times\mathbb H$, with $p=\rho\,n$, $\rho=\sqrt{-p^2}$ and $\mathbb H=\{n^2=-1\}=SO_0(1,3)/SO_0(1,2)$.
  - Fix $n_0\in\mathbb H$ and let $V_0$ be the finite-dimensional space of tensors (of the index and Dirac type of $G^{(O)}_{\phi\phi'}$) invariant under the little group of $n_0$. Then $V_0$ is spanned by the values $T_i(n_0)$ of polynomial covariants $T_i$ built from $g$, $\gamma$ and the vector $n$: the little-group invariants are polynomials in $g$, $n_0$, $\gamma$ (and $\epsilon$, excluded by parity).
  - Covariant distributions on a homogeneous space are smooth along the orbits. Using a local smooth section $n\mapsto\Lambda_n$ with $\Lambda_nn_0=n$, covariance gives $F(\rho\,n)=D(\Lambda_n)f(\rho)$, where $f$ is a $V_0$-valued distribution on $(0,\infty)$.
- *Dimensional analysis.* $\mathcal R_{G,\lambda^2\eta}(\lambda p;\lambda\mu)=\lambda^w\mathcal R_{G,\eta}(p;\mu)$ at $\eta>0$ (joint homogeneity, as in step 2). Taking $\eta\to0$ gives $\mathcal R(\lambda p;\lambda\mu)=\lambda^w\mathcal R(p;\mu)$.
- *Logarithms.* The $\mu$-dependence is polynomial in $\ln\mu$ of degree $\le L$, since pole orders are $\le L$; this persists in the limit because a polynomial of fixed degree is determined by its values at $L+1$ points. Hence $f(\lambda\rho)=\lambda^w\sum_{k\le L}(\ln\lambda)^kf_k(\rho)$.
- *Conclusion.* Put $\rho=e^u$ and $g(u)=e^{-wu}f(e^u)$. The translates of $g$ are polynomials of degree $\le L$ in the translation parameter, so $g^{(L+1)}=0$ in $\mathcal D'(\mathbb R;V_0)$ and $g$ is a $V_0$-valued polynomial of degree $\le L$. Expand its coefficients in the basis $T_i(n_0)$ and use $D(\Lambda_n)T_i(n_0)=T_i(n)$ and $T_i(\rho n)=\rho^{d_i}T_i(n)$. This gives (c), and in particular real-analyticity on $\{p^2<0\}$.
- *Illustration.* `fix1_bm_illustration.py` (d) gives a zero-momentum insertion graph whose damped, MS-subtracted value converges to the undamped DR value, of the form $(\Delta\cdot p)^m[c_0+c_1\ln p^2]$ with $c_1=-1/(m+1)$. ∎

**What it settles.** Prop. F.5 settles, in DR, the existence/IR-finiteness question of reference Rem. C.37 for off-shell forward two-point insertions. The forward remainder estimate of Rem. C.37 remains asm:appM-forward (Cor. F.2 [A]). The BPHZL version of the question, as Rem. C.37 poses it, is not addressed. Prop. F.5 is not used by Theorem F or Cor. F.2; on-shell amplitudes are defined by the parametric continuation of Theorem F. The general agreement of BM's definition with Speer's analytic-regularization definition at Euclidean momenta (recalled in SSS 2019 §3) is not needed and is not claimed; the one-loop illustration (d) agrees.

**Lemma F.9 (logic).** Beyond W1–W3 the hadronic step uses only SA on $\mathcal I_Q$. No perturbative statement implies SA. $M>0$ removes the exceptional-momentum obstruction. Cor. F.2 is the perturbative counterpart.

## 5. Part III: hadron-level DIS

**Assumptions.**
- **W1.** Wightman framework (positive energy, unique vacuum). $J^\mu$ is hermitian, local, covariant, conserved and tempered; parity holds.
- **W2** (corrects ERR-M25). A stable spin-½ target of mass $M$ in its flavour superselection sector $\mathcal H_T$, with ${\rm spec}\subset\{M^2\}\cup[M_1^2,\infty)$, $M_1>M$ (needs $m_\pi>0$). Only ${\rm spec}\subset\{p^2\ge M^2\}$ is used.
- **W3.** The spin-averaged connected forward commutator is tempered, with a retarded part $R$: ${\rm supp}\subset\bar V_+$, $R-A=C$, crossing $A^{\mu\nu}(z)=R^{\nu\mu}(-z)$, covariance, parity, $q_\mu\tilde R^{\mu\nu}=0$; $R$ is unique up to polynomials.
- **SA** (for even $n$). There are $N\ge\max(n+3,n_0+2)$ and $Q_0,K,k$ such that for $Q\ge Q_0$ an odd $P_N=\sum_{m\le N-2}\pi_m\omega^{m-1}$ satisfies:
  - (a) $\sup_{\mathcal I_Q}|T_2-P_N|\le K(M/Q)^{N-2}\ln^kQ$;
  - (b) $|\pi_m|\le K\ln^kQ$;
  - (c) $\pi_n=4\sum_iC^{(n)}_{2,i}A^{(n)}_i+O((M^2+mM)Q^{-2}\ln^k)$.
- **NPOPE.** $T=\sum_{d_j\le N}\tilde C_j\langle P|O_j|P\rangle+O(|q|^{1-N}\ln^k)$ on Euclidean $q$, with $|\tilde C_j|\le K|q|^{2-d_j}\ln^k$, finitely many operators per dimension, twist $\ge2$, twist 2 spanned by $O_{q,g}$, and odd-twist coefficients $\le Km|q|^{1-d}\ln^k$.
- **RG.** Twist-2 RG with $\gamma^{(n)}$ asymptotic to $\overline{\rm MS}$ and $\beta=-b\alpha^2(1+o(1))$, $b>0$. The coefficients at $\mu=Q$ are asymptotic to perturbation theory.
- **PDF.** PDFs exist. **Grow.** $T_2(iy)/(iy)\to0$. **Meas.** $x$-space measures with the twist-2 moments exist.

**Lemma 5.1 [R, R_def].** Euclidean $q$ with $|\mathbf q|\ge Q/2$ gives $\hat P^2=M^2\mathbf q^2/Q^2\ge M^2/4$, and $\omega=2iMq^4/Q^2$ covers $\mathcal I_Q$ (h1 (c)).

**Lemma 5.2 (NPOPE ⇒ SA) [R, R_cond: NPOPE].**
- Transversalize with $\Pi=g-qq/q^2$: $T_2=\sum_j\nu b_j+\Pi_2(\Pi\mathcal R\Pi)$, where $b_j$ is the $PP$ coefficient of $\tilde C_j\langle O_j\rangle$ and $|\Pi_2|\le CQ/M$ on $\mathcal I_Q$ (h1: 6.06).
- $\nu b_j$ has size $(M/Q)^{t-2+2b}\omega^{r-1-2b}$. Twist 2 gives $\pi_n$; trace terms $M^2/Q^2$; chirally suppressed twist 3 $mM/Q^2$; twist $\ge4$ $M^2/Q^2$.
- Take the odd part. Without chiral suppression the error is $O(M/Q)$. This re-proves reference Lemma C.47 (本书给出的证明).

**Lemma 5.3 (Markov; App K `lem:appK-markov`) — 数学 (no tag); classical.** For odd $h$ of degree $\le D_g$: $|h_k|r^k\le2(1+\sqrt2)^{D_g}\sup_{|y|\le r}|h(iy)|$ (Chebyshev extremality, $|T_m(i)|\le(1+\sqrt2)^m$, a factor 2 for complex values; Borwein–Erdélyi; h1 (h)). The outline's form, with $c_{N,k}=|t_{N,k}|$ and a complex factor $\sqrt2$, is sharper; the constant used here is a valid upper bound.

**Lemma 5.4 (App K `lem:appK-entire`) — 数学 (no tag).** An entire $f$ with $|f|\le C(1+|z|)^A|{\rm Im}\,z|^{-B}$ is a polynomial of degree $\le A$.

*Proof.* Subharmonic averages on circles of radius 2 give $\log|f|\le\log C+A\log(3+|z|)-BJ$, where $J(y)=\frac1{2\pi}\int\log|y+2\sin\theta|=\log\max(1,|w_\pm|)\ge0$ (Jensen; $w_+w_-=-1$). Then Cauchy estimates (h1 (a)). ∎

**Lemma 5.5 — 数学 (no tag); standard.**
- **(a)** (outline `lem:appM-green`) If $f$ is holomorphic on $0<{\rm Im}\,z<1$ with $|f|\le C(1+|z|)^A({\rm Im}\,z)^{-B}$, then $|\langle f(\cdot+i0),\chi\rangle|\le C'\sum_{j\le\lceil B\rceil+1}\int(1+|x|)^A|\chi^{(j)}|$ (almost-analytic extension plus Stokes). Hence a positive jump has $\nu([R,2R])\le CR^{A+1}$.
- **(b)** One-dimensional edge of the wedge, via $K$-fold primitives and Painlevé.
- **(c) Curved approaches** (outline `lem:appM-curved-approach`). 本书给出的证明 of a routine extension of the proof of Hörmander Thm 3.1.15.
  - *Setting.* $f$ is holomorphic on $X+i(\Gamma\cap B_\gamma)$ ($\Gamma\ne\mathbb R^m$ an open convex cone) with $|f|\le C|y|^{-N}$ and boundary value $f_0$. $\Theta_\eta:X'\Subset X\to\mathbb C^m$ are smooth with ${\rm Im}\,\Theta_\eta\in(\Gamma'\setminus0)\cap B_{\gamma/2}$ ($\Gamma'$ closed, $\Gamma'\setminus0\subset\Gamma$) and $\Theta_\eta\to{\rm id}$ in $C^\infty$.
  - *Claim.* $\int f(\Theta_\eta)\varphi\to\langle f_0,\varphi\rangle$.
  - *Proof.*
    1. Taylor's formula at $s=1$ for $s\mapsto f(z+isY)$, $Y\in\Gamma$, gives $f=\sum_{k\le N}\frac{(-i)^k}{k!}L^kf_Y+L^{N+1}H$, with $L=Y\cdot\partial_z$ and $H=\frac{(-i)^{N+1}}{N!}\int_0^1s^Nf(z+isY)ds$.
    2. $H$ is continuous up to the edge, since $|y+sY|\ge cs$.
    3. $(L^{N+1}H)\circ\Theta_\eta=(a_\eta\cdot\partial_x)^{N+1}(H\circ\Theta_\eta)$ with $a_\eta=(D\Theta_\eta)^{-1}Y\to Y$.
    4. Integrate by parts; the limit is independent of $\Theta$.
    5. Straight approaches identify the limit with $f_0$. ∎
  - Numerical check: rv32_bv.

**Proposition 5.6 (dispersion relation) [R, R_cond: W1–W3].**
- (a) $T_2(\omega,Q^2)$ is holomorphic and odd on $\mathcal C$.
- (b) $|T_2|\le C_Q(1+|\omega|)^A|{\rm Im}\,\omega|^{-B}$, with $A,B$ independent of $Q$.
- (c) ${\rm Disc}\,T_2=4\pi i\nu_Q$, where $\nu_Q=F_2(1/\omega)d\omega\ge0$, for **every** $Q^2>0$.
- (d) For even $n_0>A+1$: $T_2=\sum_{n<n_0}t_n\omega^{n-1}+4\omega^{n_0-1}\int_{(0,1]}\frac{x^{n_0-2}F_2dx}{1-x^2\omega^2}$, so $t_n=4M^{(n)}_2$ for $n\ge n_0$.

*Proof.*
1. $T=i\tilde R$ on the forward tube, with Vladimirov bounds.
2. Crossing makes $T_2$ odd.
3. On the slice $q=(w,0,0,s)$, $S_1=PPT$ and $S_2=gT$ are even in $s$, hence holomorphic in $(w,s^2)$. The root of $s^2=w^2+Q^2$ with ${\rm Re}\,s>0$ has $|{\rm Im}\,s|<{\rm Im}\,w$.
4. The point $w=iQ$ is removable: $T_2=Q^4(b+a/Q^2)/\nu$ (h1 (d)).
5. ${\rm Im}\,w-|{\rm Im}\,s|\ge{\rm Im}\,w\,Q^2/(2(|w|^2+Q^2))$ (h1 (e)), giving $A=a+2b+2$, $B=b$.
6. $i(\tilde R-\tilde A)=4\pi iW$, and $W=0$ for $|\omega|<1$ by W2.

6′. **Slice restriction.**
- For complex $Q^2$ near $Q_0^2>0$, $|{\rm Im}\,s|<{\rm Im}\,w$ contains local wedges in $(w,Q^2)$. Their cones $|\eta_Q+2x\eta_w|<2\sqrt{x^2+Q^2}\,\eta_w$ (first order; rv22 (W)) contain $(1,0)$ and $(1,-2x)$, and there $|F|\le C|{\rm Im}|^{-B}$.
- (i) $K$-fold primitives in $w$ ($K>B$) give slice boundary values for every $Q^2$, weakly continuous in $Q^2$.
- (ii) **Identification.**
  - Take test functions supported away from $\mathbf q=0$ and in the **spacelike** region $s=|\mathbf q|^2-(q^0)^2>0$, where the wedges are established.
  - SO(3) averaging and $(q^0,|\mathbf q|)\mapsto(x,s)$ (Jacobian $2|\mathbf q|$) turn the 4D approach into $\Theta_\eta=(x+i\eta,\,s+\eta^2-2ix\eta)$, with ${\rm Im}\,\Theta_\eta=\eta(1,-2x)$.
  - Cover the support by finitely many patches, each with a fixed closed subcone containing all directions $(1,-2x)$ of the patch, and use a partition of unity.
  - Lemma 5.5(c) on each patch gives the wedge boundary value, which disintegrates into slice values by (i).
- (iii) By weak continuity, positivity and support hold for every $Q^2>0$; $D_{Q^2}=4\pi i\nu_Q$ (fixes E9). Lemma 5.5(b) gives holomorphy on $\mathcal C$.

7. Positivity: $F_1\ge0$ and $F_2\ge\nu F_1/\hat P^2\ge0$.
8. Growth: by 5.5(a), $n_0>A+1$ suffices.
9. $H=T_2-\sum_{n<n_0}t_n\omega^{n-1}-D_{n_0}$ has no jump. Since $|1-x^2\omega^2|\ge({\rm Im}\,\omega)^2/|\omega|^2$, Lemma 5.4 makes $H$ a polynomial. As $H=O(\omega^{n_0-1})$ and $H(iy)/(iy)^{n_0-1}\to0$, $H\equiv0$. ∎

本书给出的证明 of reference C.64, with corrections (E9 fixed, the point $\hat P=0$ handled) and an explicit $n_0$ (h1 (f)); no novelty claim.

**Theorem 5.7 (fixed-$n$ Taylor coefficients; outline `thm:dis-fixed-n`) [R, R_cond: W, SA].** For every even $n\ge2$: $t_n=4\sum_iC^{(n)}_{2,i}A^{(n)}_i+O((M^2+mM)Q^{-2}\ln^kQ)$.

*Notation.* $n_0$ is as in Prop. 5.6(d), and $N$, $P_N$, $K$, $k$ are as in SA, with $N\ge\max(n+3,n_0+2)$. Set $r_Q=\sqrt3M/Q$ and $\varepsilon_N:=K(M/Q)^{N-2}\ln^kQ$. Let $N'$ be the least even integer $\ge N-1$: $N'=N-1$ for odd $N$, $N'=N$ for even $N$. Then $N'\ge n_0+2$, $N'\ge n+2$ and $N'\ge N-1$ (exponent bookkeeping: fix3_tail (d)).

*Proof.*
1. **Exact tail.** For even $N'\ge n_0$, insert $\frac1{1-u}=\sum_{j<J}u^j+\frac{u^J}{1-u}$ with $u=x^2\omega^2$, $J=(N'-n_0)/2$, into Prop. 5.6(d). Since $t_n=4M^{(n)}_2$ for $n_0\le n<N'$,
   $$T_2(\omega)-\sum_{n<N'}t_n\omega^{n-1}=4\omega^{N'-1}\int_{(0,1]}\frac{x^{N'-2}F_2\,dx}{1-x^2\omega^2}.$$
   At $\omega=iy$, $1-x^2\omega^2=1+x^2y^2\ge1$ and $F_2dx\ge0$. Hence
   $$\Big|T_2(iy)-\sum_{n<N'}t_n(iy)^{n-1}\Big|=4|y|^{N'-1}\int\frac{x^{N'-2}F_2}{1+x^2y^2}dx\le t_{N'}|y|^{N'-1}\le t_{n_0}|y|^{N'-1},$$
   using $x^{N'-2}\le x^{n_0-2}$ on $(0,1]$. On $\mathcal I_Q$ the tail is $\le t_{n_0}r_Q^{N'-1}$: this is $t_{n_0}r_Q^{N-2}$ for odd $N$ and $t_{n_0}r_Q^{N-1}$ for even $N$. The exact remainder needs no condition on $r_Q$.
   - The earlier bound $2t_{n_0}r_Q^{N-1}$ is false for odd $N$: in the elastic model it fails at $N=5,7,9$ (fix3_tail (b)). Its factor 2 also needed $r_Q\le1/\sqrt2$.
2. **Markov.** $h:=P_N-\sum_{n<N'}t_n\omega^{n-1}$ is odd of degree $\le N'-3$. Indeed $P_N$ has degree $\le N-3$, and $\le N-4$ for odd $N$ because its $m$ are even. On $\mathcal I_Q$, SA(a) and step 1 give $|h|\le\varepsilon_N+t_{n_0}r_Q^{N'-1}$. Lemma 5.3 with $D_g=N'-3$ gives, for every even $n'\le N'-2$,
   $$|\pi_{n'}-t_{n'}|\le c_N\big(\varepsilon_N+t_{n_0}r_Q^{N'-1}\big)r_Q^{1-n'},\qquad c_N=2(1+\sqrt2)^{N'-3}.$$
3. **Bootstrap.** Take $n'=n_0$. Since $N'-n_0\ge2$, there is $Q_1\ge Q_0$ with $c_Nr_Q^{N'-n_0}\le\frac12$ for $Q\ge Q_1$. With $t_{n_0}\ge0$ (positivity) and SA(b),
   $$t_{n_0}\le2|\pi_{n_0}|+2c_N\varepsilon_Nr_Q^{1-n_0}\le2K\ln^kQ+2c_NK\,3^{(1-n_0)/2}(M/Q)^{N-1-n_0}\ln^kQ=O(\ln^kQ),$$
   since $N-1-n_0\ge1$.
4. **Conclusion.** For the given even $n$ ($n\le N-3\le N'-2$),
   $$|t_n-\pi_n|\le c_N\big[\varepsilon_Nr_Q^{1-n}+t_{n_0}r_Q^{N'-n}\big]=O\big((M/Q)^{N-1-n}\ln^kQ\big)+O\big((M/Q)^{N'-n}\ln^kQ\big)=O\big((M/Q)^{N-1-n}\ln^kQ\big).$$
   The last step uses $N'\ge N-1$: the tail never dominates the term from $\varepsilon_N$, and for odd $N$ both are of order $(M/Q)^{N-1-n}$. So the conclusion is unchanged by the correction of step 1. Since $N\ge n+3$, $(M/Q)^{N-1-n}\le(M/Q)^2$ for $Q\ge M$. SA(c) gives the claim. ∎

*Check.* `final2_scripts/fix3_tail.py` checks the following and PASSes.
- (a) The exact remainder identity, to $10^{-29}$, and the bound $t_{n_0}|y|^{N'-1}$, with maximal ratio 0.9994, for three test measures (smooth + elastic, valence-like, elastic only) with subtraction constants violating Grow.
- (b) The failure of the old bound for odd $N$.
- (c) The whole Markov chain on synthetic SA data, for $N=7,\dots,10$.
- (d) The exponent bookkeeping, for all even $n,n_0\le20$.

本书给出的证明 of reference C.50; besides W1–W3 it uses only SA (Lemma F.9). No novelty claim.

**Proposition 5.8 [R, R_cond: W].** Given (d) with $n_0\ge4$: $t_n=4M^{(n)}_2$ for all even $2\le n<n_0$ iff Grow holds.

*Proof.* Descending induction with
$$\frac{T_2(iy)}{iy}=\sum_{n<k-2}t_n(iy)^{n-2}+(iy)^{k-4}\Big[t_{k-2}-4\!\int\! x^{k-4}F_2\tfrac{x^2y^2}{1+x^2y^2}\Big]$$
and monotone convergence. Conversely, $T_2(iy)/(iy)=4\int F_2/(1+x^2y^2)\to0$. ∎

A fixed pole $c\omega$ is invisible in $F_2$.

**Theorem 5.9 [R, R_cond: RG].**
$$C^{(n)}_{2,i}(Q^2/\mu^2,\alpha_s(\mu))=\sum_jC^{(n)}_{2,j}(1,\alpha_s(Q))\big[\mathcal P\exp(-\textstyle\int_\mu^Q\frac{d\mu'}{\mu'}\gamma^{(n)})\big]_{ji}.$$
There is no lower-dimension mixing at twist 2, so E10 does not arise. The perturbative counterpart is Cor. A.5.

**Theorem M [R, R_cond]; refines reference C.66.**
- (i) [W, SA] $t_n=4\sum CA+O((M^2+mM)Q^{-2}\ln^k)$.
- (ii) [W] $t_n=4M^{(n)}_2$ for $n\ge n_0$.
- (iii) [+Grow] All even $n\ge2$, including the momentum sum rule; Grow is necessary.
- (iv) [+RG] Agreement with perturbation theory.
- (v) [+Meas] Weak $x$-space convergence (reference Cor. C.52; c_pdf Thm 7.2).

## 6. Part IV: e⁺e⁻ and the Adler function

**Assumptions.**
- **V1:** W1 in the vacuum sector; no massless spin-0 state couples to $J$.
- **VOPE:** a non-perturbative OPE for $D(Q^2)$ with derivative bounds.
- **VPT:** identity coefficient $\asymp R_0\sum d_ka^k$.
- **VSec:** VOPE on $|\arg Q^2|\le\pi-\theta_0$.

**E1 [R, R_cond: V1]; known.**
- $\hat W=2\pi\theta(q^0)(qq-q^2g)\rho$ with $\rho\ge0$ tempered. Set $R=12\pi^2\rho$ and $D=Q^2\int R/(s+Q^2)^2$.
- Equivalent: $\int\rho/(1+s)^2<\infty$; $D<\infty$ at one point; $\Pi$ is once-subtracted (monotone convergence).

**E2 [R, R_cond: V1, VOPE, VPT]; known (reference Rem C.62).** $D=R_0[1+\sum_{k\le K}d_ka^k]+O(a^{K+1})+O(m^2/Q^2)+O(\Lambda^4Q^{-4}\ln^k)$. There is no $1/Q^2$ term, because there is no GI dimension-2 scalar.

**E3 [R, R_cond: V1, VOPE, VPT + derivative bounds].** $M_k=kQ^{2k}\int R/(s+Q^2)^{k+1}$ satisfies $M_1=D$ and $M_{k+1}=M_k-\frac{Q^2}k\frac{dM_k}{dQ^2}$. Hence $M_k=R_0[1+d_1a+(d_2+H_{k-1}b_0d_1)a^2+O(a^3)]$ with $b_0=\beta_0/4$ (e1 (c), (c′)).

**E4 — 数学 (no tag); an explicit spectral function, known in spirit (Shifman; Blok–Shifman–Zhang).** $R=R_0[1+\kappa\sin(\sqrt s/\Lambda)]$, $|\kappa|<1$, gives $D=R_0[1+\kappa\frac\pi2\frac Q\Lambda e^{-Q/\Lambda}]$, from $\int_0^\infty\frac{2t\sin t}{(t^2+b^2)^2}dt=\frac\pi2\frac{e^{-b}}b$ (e1 (a), (b)). So the OPE plus positivity fixes neither pointwise nor fixed-width-smeared $R$. In the book this is an illustration for `conj:ee-duality`(b), not a statement about QCD.

**E5 [R, R_cond: V1 + leading term]; classical (Karamata).** If $R\ge0$ and $D\to R_0$, then $\frac1s\int_0^sR\to R_0$.
- *Proof.* $D/Q^2=\int_0^\infty e^{-uQ^2}uL(u)du$, with $L$ the Laplace transform of $R$. Apply Karamata, then a monotone squeeze $uL(u)\to R_0$, then Karamata again. ∎
- No rate in general (E4 model: $O(\Lambda/\sqrt s)$; e1 (d)).

**E6 [R, R_cond: VSec]; known (Poggio–Quinn–Weinberg).**
$$12\pi\,{\rm Im}\,\Pi(s+i\Delta)=\frac1{2\pi}\int_{-(\pi-\theta)}^{\pi-\theta}D(|s+i\Delta|e^{i\phi})d\phi,\qquad\theta=\arctan(\Delta/s).$$
Proportional smearing is asymptotic to perturbation theory, with leading term $R_0(1-\theta/\pi)$ (e1 (e)). Fixed width needs local duality (E4). Perturbative e⁺e⁻: K10.

## 7. Verification scripts

Author scripts are in `verify/extend/X3-ope/scripts/` (logs in `logs/`); the final reviewer's scripts are in `review_final_scripts/`; this revision's scripts are in `final2_scripts/` (logs in `final2_logs/`).

`final2_scripts/rerun_all.sh` reruns the 9 author scripts, the final reviewer's three scripts and the five final2 scripts.
- Full run of 2026-10-14 (16:48–17:13): all 16 fresh logs are byte-identical to the stored ones. `fix6_rg_legs`, added afterwards, was rerun separately and is also identical.
- sha256 prefixes are in `final2_logs/rerun_all.log`; fresh logs are in `final2_logs/rerun/`. Earlier, reviewers r2-1, r3-1 and r3-2 re-ran f1–f6, h1 and e1, and the final reviewer re-ran f1–f7, h1 and e1 together with five reviewer scripts; all logs were byte-identical.

| Script | Content |
|---|---|
| f1, f3 | Graph polynomials; Lemma F.6 exact on 21 + 1028 graphs |
| f2 | Triangle (Ex. F.3, F.4) |
| f4 | Lemma F.7 |
| f5 | DR-SD signs: 400/400 |
| f6 | Tree-level rank-5 structure (Lemma NE(iii)) |
| f7 | (a) $+D!/(D-5)!$; (b) even/odd $n$ Clifford facts; (c) slot count of Lemma NE(ii) for $n\le12$ |
| h1, e1 | Parts III, IV |
| rv21_box, rv2_ladder2, rv32_triangle | Independent checks of Theorem F |
| rv22_algebra (sign of print fixed; original kept as `.orig_r2`), rv22_numeric, rv32_misc, rv32_bv | Projector, constants, wedge, $\beta_\xi$, weights, signs, OSWI identity, curved approaches |
| c_dis | One loop, $N\le8$ |
| fr_ne_rank, fr_ne_rank_allr (final reviewer) | Numerical rank test of Lemma NE(ii): no $D=4$-only relation in any $\mathcal B^\pm_n$ sector, $n=2..5$, with Gram and Dirac controls |
| fr_triangle (final reviewer) | Ex. F.3 closed form against an independent simplex quadrature, incl. two points outside the disk |
| **final2: fix1_bm_illustration** | Prop. F.5 illustrations: α-damping identity; IR counterterm of a quadratically divergent subgraph $=\eta(8\ln\eta+8\gamma_E-4)\to0$; its insertion into a bubble $\to0$; a zero-momentum insertion graph: damped MS value → undamped DR value, form $(\Delta\cdot p)^m[c_0+c_1\ln p^2]$ |
| **final2: fix1_homogeneity** | Prop. F.5 step 2(iii): analyticity at $D=4$, uniform vanishing on $\vert D-4\vert=0.4$, Taylor coefficients $O(\eta\vert\ln\eta\vert^{m+1})$, $c_0(\eta,\mu,4)=\eta(8\gamma_E-4-8\ln(\mu^2/\eta))$ |
| **final2: fix3_tail** | Thm 5.7: exact remainder identity and bound; failure of the old bound for odd $N$; Markov chain; exponent bookkeeping |
| **final2: fix4_ne_demand** | Lemma NE(ii)(γ): exhaustive demand minimisation ($n=2..30$); numerical rank controls (thresholds $n+6-r'$ sharp for $r'=3,4$) |
| **final2: fix6_rg_legs** | Theorem A (A5) step 3: renormalized-leg identity $\sum_j\gamma_{ij}\tilde G_{[O_j]}=-\hat{\mathcal D}\tilde G_{[O_i]}+(\sum_\phi\gamma_\phi)\tilde G_{[O_i]}$ and the amputation factor (sympy, generic $3\times3$ $Z$) |

## 8. Novelty ledger

| Result | Status |
|---|---|
| Theorem F (analytic step of the method of projectors) | **本书给出的严格证明**; 本书新结果 withheld (O12). Closest prior result: SSS 2019 §7 Prop. 6 (Theorem F status paragraph) |
| Lemma NE(ii) (twist-2 blocks free of evanescent operators, via harmonic + isotypic projection) | proof written out here; the fact is expected in DIS practice; no novelty claim, no marker |
| Lemma F.8 | conditional form written out here (suggested by r2-2); no novelty claim |
| Lemma B.1 (formerly Remark B.1) | 本书给出的推导 of the formal-D, loop-by-loop form of LBC from BBH, Henneaux 1996, BHHS; no novelty claim |
| (A5) in the full basis; Cor. A.5 | standard; 本书给出的推导 |
| Lemma A.7 | proof here; no novelty (Zimmermann normalization) |
| Prop. F.5 | 本书给出的推导: an instance of BM II Thm 1 / BM I Thm 1, with the identification (step 2) written out; no novelty claim |
| Prop 5.6, Thm 5.7, Prop 5.8, Thm M | 本书给出的证明 of reference C.64/C.50/C.65/C.66, with corrections, an explicit $n_0$ and the hypothesis SA; no novelty claim |
| Lemma 5.5(c) | 本书给出的证明 of a routine extension of Hörmander Thm 3.1.15 (classical mathematics; cite Hörmander) |
| A.3, Thm A content, Thm B, F.0, F.1, F.6, 5.3–5.5(a,b), E1–E6 | known, or application of cited results (reference C.30; Smirnov; Joglekar 1977 II; Schultka §4, BFP, Nilsson–Passare; classical); 本书给出的推导 where a derivation is printed |

## 9. Withdrawn and corrected claims

| # | Claim | Disposition |
|---|---|---|
| W1 | "C.24 follows from Smirnov + uniqueness" | withdrawn (circular) |
| W2 | "(B1) contact terms false / log-carrying" | withdrawn |
| W3 | Theorem B novelty; E5 "new in context"; F.0 "new"; F.6 novelty | withdrawn |
| W4 | One-loop moment identity for all $n$ [R] | withdrawn (X3c not delivered) |
| W5 | Theorem F as "new proof of the method of projectors" | narrowed to the analytic step |
| W6 | "[R-cited]" for Theorems A, I and Cor. F.2 | regraded [A] |
| W7 | (A5) without $\beta_\xi\partial_\xi$ (round 1) | withdrawn |
| W8 | (A4)/(A5) via Lemma A.3(b) on the unprojected relation (round 2) | replaced (Def. A.2; direct (A5)) |
| W9 | "(NE) for twist 2, every $n$" and "DIS unaffected" without proof | replaced by Lemma NE(ii) |
| W10 | Cor. F.2: evanescent operators drop because their trees vanish | replaced (mixing $Z_{EQ}$; NE(ii) + covariance) |
| W11 | X3a "FAILS as planned" | corrected to "not delivered (open)" |
| W12 | Gluon regularity at $\omega=0$ [R]; Disc $=4\pi iF_2$ [R] | downgraded to [A] |
| W13 | "Strongest OPE statement for massless QCD with quarks" | deleted |
| W14 | Lemma 5.5(c) "NEW" | relabelled standard |
| W15 | "Literature uses this step without proof (GLT, GL, LvRV, LNvRV)" | corrected: only LNvRV §2 checked |
| W16 | DR-SD sign with $\vert Y\vert$ | corrected (f5) |
| W17 | $\Gamma^{(5)}\cdot\Gamma_{(5)}=-D\cdots(D-4)$ | corrected to $+$ |
| W18 | Remark B.1 for any $n\ge n_0$ | corrected: $n$ even (sufficient) |
| W19 | Remark F.5 "[A] pending O10" → "[R, R_PT] after reading BM II" (round 3), a grade set without stating what BM's ε is | final2: Prop. F.5 rewritten. BM's ε is identified as the damping parameter, BM I is read, and the identification $\lim\mathcal R^S=\lim\mathcal R^C$ is written out (step 2). Proposed [R, R_PT]; printed [A] until the LA-4 confirmation |
| W20 | "BPHZL has no C.24-type estimate"; "Wick rotation legitimate" | qualified (sources unread); replaced by the $(\mathcal F-i0)$ remark |
| W21 | Thm 5.7 step 1: "the positivity tail is $\le2t_{n_0}r_Q^{N-1}$" | false for odd $N$; replaced by the exact remainder bound $t_{n_0}r_Q^{N'-1}$ (Fix 3); conclusion unchanged |
| W22 | Theorem F: "SSS 2019 and Jantzen 2011 do not cover this case" | replaced by the precise comparison; SSS 2019 §7 Prop. 6 is the closest prior result (Fix 2) |
| W23 | NE(ii)(β): "$r'\in\{1,3\}$, since its other indices can only be filled by $\mu,\nu$" | replaced: $r'\le4$ ($\mu$, $\nu$, one $\hat q$ besides the first-row index); demand $n+6-r'$; chirality not needed (Fix 4) |
| W24 | Remark F.5: "settles reference Rem. C.37" | restricted: in DR, only the existence/IR-finiteness part for off-shell forward two-point insertions (Fix 1(c)) |
| W25 | "[R]" for pure-mathematics lemmas (NE, F.1, F.6, 5.3–5.5, Remark B.1) and for E4; "[R, R_PT]" for Examples F.3/F.4 | no tag (数学; examples untagged), per LA-2 and WRITER_SPEC_v2 §4.1; Remark B.1 renamed Lemma B.1 |
| W26 | Novelty wording "new argument", "new detail", "new conditional form", "under a minimal hypothesis" | reworded (本书给出的推导／证明; no novelty claim) |
| W27 | K5 "Hollands §4.1.3 (not verified)"; K1 "BM I abstract only"; "Feichtner–Sturmfels checked" without a copy | located and read (LA-7); BM I read in full; FS copy added (Fix 5) |

## 10. Changes relative to the reference App C and CLAIMS; spec patch

**Changes relative to App C and CLAIMS.**
- C.24 is unnecessary in the DR route; R-M26 is circular; Lemma A.7 gives the correct reduction, and A09(5) stays open.
- C.44 is valid conditionally; the error is in Rem. C.45.
- C.54(a) is reduced (Cor. F.2).
- Rem. C.37: Prop. F.5 settles, in DR, the existence/IR-finiteness question of Rem. C.37 for off-shell forward two-point insertions. The forward remainder estimate of Rem. C.37 remains asm:appM-forward (Cor. F.2 [A]), and the BPHZL version of the question is not addressed.
- Hadronic part: W2 (ERR-M25), E9 fixed, E10 avoided, explicit $n_0$, the point $\hat P=0$ handled, C.58 replaced by SA; the tail estimate of C.50's proof is made exact (Thm 5.7 step 1).
- Rem. C.62 is extended to E1–E6.

**Spec patch.**
- **X3a.** Delete prop:appM-remainder-discharge; asm:appM-remainder stays [A], with the note "reduced by Lemma A.7 to CTp; sources unread (Zimmermann 1973 first)".
- **X3e.** Insert thm:appM-forward-expansion [R, R_PT] per graph. asm:appM-forward is *not* 已解除; prop:dis-ope-forward stays [A].
- **thm:appM-forward-expansion, status.** Replace the sentence on SSS 2019 and Jantzen 2011 by the comparison of the Theorem F status paragraph: SSS 2019 §7 Prop. 6 is the closest prior result, and Theorem F adds (i)–(iv).
- **prop:appM-zero-momentum-insertion.**
  - Keep [A] with the status note until the LA-4 confirmation.
  - The upgrade path ("this identification written out") is now supplied by Prop. F.5 step 2, with BM I and BM II read in full. Replace the proof plan by Prop. F.5 steps 1–3, citing `Breitenlohner:1976te` Thm 1 and Prop. 1, `Breitenlohner:1975hg` Thm 1, §II.3 and §III, and `BreitenlohnerMaison1977a` Thm 1.
  - The sentence describing BM's ε as the damping regulator is now supported by the checked texts: action-principle paper §II.1 (pp. 13, 30, 36); BM I p. 49 ("ε … acts like a mass term"); BM II §1 and (3.17). The writer's note withholding it can be lifted.
  - Restrict the claim "settles … the question left open in rem:appM-exceptional" as in W24.
- **lem:appM-ne.** (ii)(β)–(γ) as revised: $r'\le4$, demand $n+6-r'$, supply $n+1$ resp. $n+4$; chirality not used.
- **thm:dis-fixed-n.** Step 1 with $N'$ and the exact remainder (Thm 5.7).
- **prop:dis-ope-gi.** $sX_d\in\mathcal E$ + LBC (Lemma B.1 = lem:appM-lbc-formal).
- **prop:dis-ope-rg.** (A5) with $\beta_\xi\partial_\xi$, full basis, [R, R_cond: A3], **no (NE) restriction**; renormalized legs as in (A5) step 3.
- **lem:appM-uniqueness(b), prop:dis-ope-euclid.** Uniqueness is blockwise under (NE) (Def. A.2, Lemma NE); twist 2 holds for all $n$.
- **Tags.** Pure-mathematics lemmas untagged (as already in the outline: lem:appM-ne, lem:appM-lbc-formal, lem:appM-newton, lem:appM-matroid, lem:appM-curved-approach, lem:appM-green).
- **Markers.** Only Theorem F carries 本书给出的严格证明.
- **rem:appM-forward-aliens.** Consistent with Cor. F.2 step 4.

## 11. Open problems

| # | Problem |
|---|---|
| O1 | Theorem-level DR function form of (A1)/(A3) and Eε, with direction uniformity and ghosts. Reading list: Smirnov's book; Gorishny 1989; Linhares–Malbouisson–Roditi 2008. |
| O2 | Flow-equation (FHH) existence and bounds for Yang–Mills with Dirac fermions. |
| O3 | X3a sources: Zimmermann 1973 (first); Anikin–Zav'yalov 1976/78; Zav'yalov; LS–dV; Bergère–de Calan–Malbouisson; Bergère–Lam. Check for CTp. |
| O4 | Fixed-order growth bounds in $\omega$ (all-$n$ moment identity; no fixed poles). |
| O4′ | X3c: the one-loop all-$N$ identity. |
| O5 | Construct 4D QCD and derive SA. |
| O6 | Derive Grow. |
| O7 | Convergence of the OPE for YM/QCD. |
| O8 | Polarized structure functions: extend Theorem B with $\gamma_5$ (uniqueness in $\mathcal B^-_n$ already holds). |
| O9 | Local duality and Tauberian remainders. |
| O10 | Closed in DR for the existence part by Prop. F.5, subject to the independent confirmation of its step 2 required by LA-4. The BPHZL question of Rem. C.37 and the forward remainder (asm:appM-forward) stay open. |
| O11 | Renormalons (reference C.68/C.69). |
| O12 | Novelty checks. For Theorem F: Tkachov 1992–97, Smirnov's books, BFP, Nilsson–Passare, Schultka §4, Borinsky, AHM, Tellander–Helmer, Walther, GLT, GL, LvRV, SSS 2019 (§7 Prop. 6 read: closest prior result), and the expansion-by-regions literature in general; the recorded reviewer INSPIRE searches did not target it. For Theorem B: Joglekar 1977 and Collins §12.8 in full. For pure YM: Hollands (§4.1.3 read; transfer to DR+$\overline{\rm MS}$ open). |
| O14 | OSWI at theorem level (would make Lemma F.8 [R, R_PT]). |
| O15 | GP′ for all GI coefficients; JL in full text; an evanescent prescription for blocks without (NE). |

O13 (pipeline) is not a mathematical item.

## 12. Disposition of round-3 required fixes (kept from X3-ope_final.md)

| Fix (reviewer, item) | Done |
|---|---|
| (A5) direct, without (NE); Cor. A.5 needs only GP′ (r3-1 #1, r3-2 #2) | Thm A (A5), Cor. A.5 |
| Blocks; (A4) blockwise; twist 2 for $n\ge4$ (r3-1 #2, r3-2 #1) | Def. A.2, Lemma NE(ii) |
| Remark B.1 (now Lemma B.1): even $n$, compact form, weights, rescaling, power series (r3-1 #3, r3-2 #3) | Lemma B.1 |
| Cor. F.2 step 4 (r3-1 #4, r3-2 #4) | done |
| Gram count; sign $+$; rv22 print (r3-1 #5) | Lemma NE(i), (iii); script fixed |
| NE statements as lemmas (r3-2 #8) | Lemma NE (数学) |
| 5.5(c) label; patches; spacelike support (r3-1 #6, r3-2 #6) | Lemma 5.5(c), Prop 5.6 6′ |
| Theorem F literature claim (r3-1 #7) | Status paragraph (now with the SSS 2019 comparison) |
| Superlative (r3-1 #8) | deleted |
| Literature additions; read BM/LZ (r3-1 #9, r3-2 #7) | §2. BM II and BM I read and used; LZ unread |
| F.7 line move; transversality; crossing (r3-2 #5) | Lemma F.7(b) |
| Literature copies; saving outputs (r3-1 #10, r3-2 #9) | copies of all checked texts in `literature/`; saving outputs is the orchestrator's task |

## 13. Final-review fixes

| Fix | Required change (X3-ope-finalreview.md) | Change made |
|---|---|---|
| **Fix 1(a)** | State in K1 and in the proof that BM II's ε is the damping regulator; Thm 1 gives analyticity at $n=4$ and a limit $\varepsilon_{\rm BM}\to0$ in $\mathcal S'(p)$ | K1 rewritten with locations: action-principle paper §II.1 (factor $\exp[-i\sum\alpha_\ell(m_\ell^2-i\varepsilon)]$, pp. 13/30/36; ε of dimension 2, p. 35); BM I p. 49; BM II §1 and (3.17). "What BM's ε is" paragraph; BM notation fixed in the conventions ($\eta$ = BM's ε, $D$ = BM's $n$). Prop. F.5 Definition and step 1 state analyticity at $D=4$ and the limit $\eta\to0$ in $\mathcal S'(\mathbb R^4)$. |
| **Fix 1(b)** | Add the identification $\lim\mathcal R^S$ = MS-bar DR amplitude (via $\Omega_H=\omega_H$ and the vanishing of the IR counterterms), or read BM I; otherwise revert to [A] | **Both done.** BM I read in full: its Thm 1 is the purely massless MS statement, its §II.3 admits the insertion vertex (dimension $n+2\ge4$), and its §III defines $\mathcal R_G=\lim\mathcal R^C_{G,\eta}$ and makes ε-proportional counterterms vanish. Prop. F.5 step 2 writes out the identification: (i) BM II Prop. 1 with $S_1=C$, $S_2=T(1-C)$; (ii) $\Omega_H=\omega_H$ ($s_H=0$); (iii) homogeneity lemma, coefficients $c_j=\sum_t\mu^{(4-D)h_t}\eta^{(\Omega_H-j-(4-D)h_t)/2}g_t(D)$ vanishing uniformly near $D=4$, and $c_j(\eta,\mu,4)=\eta^{(\Omega_H-j)/2}P_j(\ln(\mu^2/\eta))$; (iv) the insertions vanish by BM's ε-Lemma ($\eta^k$, ${\rm Re}\,k\ge\frac14$; BM I §III). General $\xi$ through BM II (3.15). Step 3 derives the $p^2<0$ form (little-group decomposition on $(0,\infty)\times\mathbb H$, distributional scaling with polynomial $\ln\mu$ dependence), per covariant $T_i$. Scripts fix1_bm_illustration, fix1_homogeneity. Proposed [R, R_PT]; printed [A] until the LA-4 confirmation (§14). |
| **Fix 1(c)** | Replace "settles reference Rem. C.37" by the restricted statement | Done in Prop. F.5 ("What it settles"), §0, §10, W24, O10 (verbatim content of the required sentence, plus "the BPHZL version is not addressed"). |
| **Fix 2** | Theorem F status, §2 forward-expansion list, O12: precise comparison with SSS 2019 §7 Prop. 6 and Jantzen 2011; add SSS 2019 §7 and Nilsson–Passare to O12; say that the reviewer INSPIRE searches did not cover the expansion-by-regions literature; keep 本书新结果 withheld | Done. Status paragraph: SSS 2019 §7 Prop. 6 named as the closest prior result and the mechanism of Lemma F.1, with the reason its positivity hypothesis fails here ($1-\omega$ coefficients) and Theorem F's additions (i)–(iv). Jantzen: no general convergence proof (§3, p. 17, quoted); §7 is the Glauber/Regge limit. Searches sentence added. §2 lists SSS (§§2–4, 7 checked), Jantzen (§§3, 7 checked), Nilsson–Passare and BFP (checked), all with copies. O12 extended. 本书新结果 withheld. Also W22, §0, §8, spec patch. |
| **Fix 3** | Thm 5.7 step 1: exact dispersion remainder with $N'$; bound $t_{n_0}r_Q^{N'-1}$; conclusion unchanged because $\varepsilon_N$ dominates | Done. Steps 1–4 rewritten with explicit constants ($c_N=2(1+\sqrt2)^{N'-3}$, $Q_1$, bookkeeping $N'\ge n_0+2$, $N'\ge n+2$, $N'\ge N-1$). The exact remainder is derived from Prop. 5.6(d); the false old bound is recorded (W21). Script fix3_tail (identity to $10^{-29}$; old bound fails for odd $N$; chain checked). |
| **Fix 4** | NE(ii)(β)–(γ): $r'\le4$ (μ, ν, one $\hat q$); oddness from chirality; general demand $n+6-r$ for rank $r\le4$, $n+3$ for pure $\gamma^{[5]}$; note that $r=4$ gives $n+2>n+1$; optionally cite fr_ne_rank | Done. (β): $r'\le4$ argument; chirality stated and marked as not used. (γ): projected relation, generator types (G), (M$_r$), (G5), the demand formula $n+10+r'-2r-2(Z_{\rm up}+Z_{\rm low}+Z_D)$ with minimum $n+6-r'$ (= $n+6-r$ at $r=r'$), $n+3$ for $\gamma^{[5]}$, the supply, and the conclusion independent of chirality. Checks: fix4_ne_demand (Parts 1–2) and the final reviewer's fr_ne_rank, fr_ne_rank_allr (rerun identical). W23. |
| **Fix 5** | FS is marked checked but has no copy: add it or mark "checked, not copied" | Copy added: `literature/feichtner_sturmfels_math0411260.txt`. Props 2.3, 2.4, 2.6 verified in it; cited with these numbers in K8 and Lemma F.6. §2's statement "copies of all checked texts" is now true; the other newly checked texts were added too (BM I, BM action principle, SSS 2019, Jantzen, Nilsson–Passare, BFP, Hollands 2008). Bibliography note on FS (refs_merged_v2.bib dropped it; arXiv-verifiable, LA-14). |
| **Fix 6(a)** | (A5) step 3 with renormalized legs: extra term $(\sum_\phi\gamma_\phi)\tilde G$, finite | Done, with the derivation ($\phi_0=Z_\phi^{1/2}\phi$, $\gamma_\phi=\frac12\hat{\mathcal D}\ln Z_\phi$, $Z_\phi^{1/2}$ per amputated leg). Symbolic check fix6_rg_legs.py. |
| **Fix 6(b)** | Lemma A.3: induction over the number of legs within each order | Done: proof rewritten as an induction over (order, number of legs), with the reason (fewer-field operators give non-polynomial trees at the same order, with coefficients fixed at lower leg number). |
| **Fix 6(c)** | Cor. F.2 step 4 wording: GI trees from $p$ alone; alien trees with $d_{ab}$ may contain $q$ but vanish | Done verbatim in substance. |
| LEAD_DECISIONS | LA-2 (pure-math lemmas untagged), LA-4, LA-7; novelty wording | Lemma NE, Lemma B.1 (formerly Remark B.1), Lemmas F.1, F.6, 5.3, 5.4, 5.5 and E4 untagged (数学); examples untagged; Prop. F.5 handled per LA-4; K5 Hollands location verified; novelty wording per K4 (§8, W25–W27). LA-5 not applicable. |

## 14. Items needing independent confirmation

Every new or changed proof of this revision:

1. **Prop. F.5, whole proof (LA-4 confirmation; decides [A] → [R, R_PT]).**
   - Step 1: the hypothesis check of BM II Thm 1. This covers the field IR degrees including $\Delta_B=2$, the general covariant-gauge propagator as BM II form (3.15), the insertion vertex as an internal vertex with all monomials of IR degree $n+2$, and the external vertices.
   - Step 2(i)–(ii): BM II Prop. 1 with $S_1=C$, $S_2=T(1-C)$, and $\Omega_H=\omega_H$.
   - Step 2(iii): the homogeneity lemma, i.e. the pure-power structure of $c_j$, analyticity on $|D-4|\le r$, the uniform bound $K_j\eta^{1/4}$, and the $D=4$ form $\eta^{(\Omega_H-j)/2}P_j(\ln(\mu^2/\eta))$.
   - Step 2(iv): the application of BM's ε-Lemma to reduced graphs with the vertex parts $\eta^kP_j$. This is the cited step (BM I §III, BM II Lemma 3).
   - Step 3: the little-group decomposition on $\{p^2<0\}\cong(0,\infty)\times\mathbb H$ (including the spanning of $V_0$ by polynomial covariants) and the distributional scaling argument.
   - The quoted BM locations (K1).
2. **Theorem 5.7**, steps 1–4: the exact remainder, $N'$, the Markov constant $c_N$, the bootstrap with $Q_1$, and the exponent bookkeeping.
3. **Lemma NE(ii)(β)–(γ)**: the $r'\le4$ argument; the demand formula and its minimum $n+6-r'$; the (G5) count; the supply $n+2-3b$ (+2); the split of the relation by Dirac rank.
4. **Theorem A (A5) step 3**: the renormalized-leg identity with $\sum_\phi\gamma_\phi$ (symbolic check: fix6_rg_legs).
5. **Lemma A.3 proof**: the induction over (order, number of legs).
6. **Cor. F.2 step 4**: reworded; check that the argument is unchanged.
7. **Theorem F status paragraph**: the literature comparison. It covers SSS 2019 §7 Prop. 6 and its hypotheses, the short argument that the base facet is the only essential facet of $\mathcal U+\hat F_0+\omega\hat F_1$, the failure of positivity for $1-\omega$, the additions (i)–(iv), and Jantzen §3 p. 17 and §7. Also the added sentence in Lemma F.1(a): coefficients in $|z-1|\le r$ make the polynomial completely non-vanishing (BFP Thm 2.2, Nilsson–Passare Thm 1).
8. **Literature ledger entries changed**:
   - K1: BM I, BM II and the action-principle paper, with page locations;
   - K5: Hollands §4.1.3, pp. 75–76 of arXiv v4;
   - K8: FS Props 2.3, 2.4, 2.6; BFP Def. 2.1, Thms 2.2, 2.4; Nilsson–Passare Def. 1, Thms 1–2.
9. **Regrading**: the pure-mathematics lemmas, E4 and the examples untagged; consistency with FINAL_OUTLINE_v2 (`lem:appM-ne`, `lem:appM-lbc-formal`, `lem:appM-newton`, `lem:appM-matroid`, `lem:appM-curved-approach`, `lem:appM-green`; `prop:appM-zero-momentum-insertion` [A] pending LA-4).
