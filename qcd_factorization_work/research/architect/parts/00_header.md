# BLUEPRINT — 《QCD 因子化定理：严格证明、全阶论证与适用边界》

**Author of this file:** proof-architect agent (research phase).
**Input:** `CONTEXT.md` (binding conventions + OUTLINE v0), the Furry monograph as quality bar, and (read-only) intermediate results of the `c_dis` and `c_pdf` agents.
**Output:** a chapter-by-chapter, statement-by-statement plan that a writer can turn into LaTeX without re-deciding structure, conventions, rigor tags or proof strategy.

How to read this file

* Every chapter section has the same seven parts: **(1) purpose & dependencies; (2) statements; (3) proof strategies; (4) worked examples / one-loop checks; (5) figures; (6) page budget; (7) key references.** For readability, (2) and (3) are merged: each statement is immediately followed by its proof plan.
* Numbering `D/L/P/T/C/Cj/E k.m` = Definition / Lemma / Proposition / Theorem / Corollary / Conjecture / Example, number m in chapter k. The preamble uses ONE shared counter per chapter (`theorem` counter with `[chapter]`), so the numbers here are *planning* numbers; writers must use the suggested `\label{...}` keys (given in `code` font) so that cross-chapter references survive renumbering.
* Rigor tags are those of `CONTEXT.md`: **[R]** strict (complete at every order of renormalized PT, or complete proof given here), **[A]** standard all-order argument with some steps only sketched in the literature, **[P]** partial, **[C]** conjecture, **[V]** violated. A tag always refers to the statement *exactly as formulated*; a perturbative theorem that is applied to hadrons carries the additional hypothesis label (see §0.3).
* "Proof: full" = the writer must give a complete proof in the book. "Proof: sketch" = use the `proofsketch` environment and end it with the sentence 「完整论证见 …」 giving the precise literature location. Literature locations marked **(verify)** were recalled by me and must be checked by the `refs` agent before transcription. I have not invented any reference; where I am unsure of a section/equation number I say so.

---

## 0. Global architecture decisions

### 0.1 Three tracks

The book is organised in three tracks that share Chapters 1–3.

| Track | Chapters | Nature | Typical tag |
|---|---|---|---|
| **R** (rigorous core) | 4, 5, 6 (§6.1–6.6) | Analyticity, unitarity, Euclidean IR finiteness, renormalization group, OPE in renormalized perturbation theory, moment problem | [R] in PT (+ named NP hypothesis for hadrons) |
| **A** (all-order graphical proofs) | 7 (method), 8 (DIS), 9 (SIA), 10 (DY), 11 (TMD) | Landau pinches → power counting → approximations → Ward identities → subtractions → factorized form | [A] (with explicit "gap" remarks) |
| **B** (boundaries) | 12–16 | Violations, conjectures, exclusive, EFT, NRQCD, power corrections | [P]/[C]/[V] mixed |

The single most important structural device is a **uniform "factorization template"** (Ch. 7, T7.20 `thm:template`) with five hypotheses (H1)–(H5); every process chapter (8–11) then consists of *verifying* (H1)–(H5) for the process, and every chapter of Track B identifies *which* hypothesis fails. This gives the reader one proof to understand and many applications, and it makes the honest status statements precise ("(H4) is proved only at the level of [A] for DY because of the Glauber region", etc.).

### 0.2 Recommended changes to OUTLINE v0 (details in `18_discrepancies` section at the end)

1. **Ch. 5/6 interface.** Ch. 5 ends with moment factorization (T5.12) and the uniqueness lemma (L5.14). The *x-space* DIS theorem with *operator-defined* PDFs (T6.14 `thm:DIS-x-space-R`) is stated and proved in Ch. 6 after the moment↔local-operator theorem (T6.10). Ch. 5 must not use the Collins–Soper definitions before they are introduced.
2. **Uniqueness from even moments** must be stated with its hypothesis (no component supported at $x=0$); without it the statement is false (counterexample $T=\delta'(x)$, all even moments vanish). Müntz–Szász is unnecessary: Hausdorff + the substitution $t=x^2$ suffices. See L5.14.
3. **Ch. 2 must contain BRST/Slavnov–Taylor identities** (needed for the non-abelian graphical Ward identities of Ch. 7/App. F) and the **Joglekar–Lee theorem** on mixing of gauge-invariant operators with BRST-exact and EOM operators (needed in Ch. 5/6 for singlet operators).
4. **Ch. 3 must distinguish "soft" (all components $\sim\lambda Q$) from "ultrasoft/central soft" (all components $\sim\lambda^2 Q$)**: Libby–Sterman's original e⁺e⁻ analysis uses the latter; TMD factorization needs the former; the Glauber region is $|k^+k^-|\ll k_T^2$. The IR degree $\omega(R)$ must be quoted with its unit (powers of $\lambda$ with $k_T\sim\lambda Q$, or powers of $\lambda^2$).
5. **Ch. 3 Landau equations in two forms**: (i) α-parameter form = necessary condition for non-analyticity of an integral in its external parameters; (ii) loop-momentum form = necessary condition for a pinch of the integration contour at a point of the integration domain (this is what Coleman–Norton and the factorization proofs use). Both get full proofs (App. D).
6. Add a short **assumption environment** to the preamble (`\theoremstyle{cdefinition}\newtheorem{assumption}[theorem]{假设}` + `\crefname{assumption}{假设}{假设}`), used for the named hypotheses of §0.3. If the lead author prefers not to change the preamble, use `definition` with title 「假设 NP1」 etc.
7. **R-ratio coefficient** in OUTLINE Ch. 4 should be stated for a general gauge group: $R=R_0\,[1+\tfrac34 C_F\,\alpha_s(s)/\pi+O(\alpha_s^2)]$, which is $R_0(1+\alpha_s/\pi)$ only for $C_F=4/3$; $R_0=N_c\sum_q e_q^2$ (photon exchange only, $n_f$ massless flavours).

### 0.3 Named hypotheses (to be used verbatim in status lines)

* **(PT)** Framework: renormalized perturbation theory of QCD with $n_f$ flavours, DR with $D=4-2\varepsilon$, $\MSbar$; external states are on-shell partons (IR-regulated by DR, by masses, or by off-shellness when stated). All [R]/[A] statements are statements in (PT) unless they say otherwise.
* **(NP-OPE)** The operator product expansion of Ch. 5 holds, as an asymptotic expansion in $1/Q^2$, for forward matrix elements between hadron states, with the same Wilson coefficients.
* **(NP-REG)** The leading-region/factorized structure derived in (PT) holds for hadronic external states, the long-distance factors being the hadronic matrix elements of the same operators (PDFs, FFs, TMDs …); the remainder is suppressed by a power of $\Lambda_{\rm QCD}/Q$.
* **(SPEC)** Spectral condition + completeness of the physical state space (Wightman-type axioms, colour-singlet asymptotic states, mass gap for hadrons). Used for analyticity, positivity and support properties for hadron targets.
* **(GLAU)** For the process considered, Glauber-region contributions cancel at leading power (so the soft approximation and the Ward identities are applicable after contour deformation). Status is process dependent: proved at the level [A] for inclusive DY-type processes (Ch. 10), violated for TMD hadro-production of hadrons (Ch. 12).

A typical status line therefore reads: 「状态：在 (PT) 中 [R]；对强子靶需要 (NP-OPE) 与 (SPEC)。」

### 0.4 Conventions that are used but not fixed in CONTEXT.md (BINDING for all chapters once accepted)

All of these were checked for consistency with the binding conventions (signs and normalizations re-derived by me; c_dis/c_pdf results agree where they overlap).

1. **Electromagnetic current** (in units of $e$): $j^\mu=\sum_q e_q\,\bar\psi_q\gamma^\mu\psi_q$.
2. **Hadronic tensor** (spin averaged):
   $$W^{\mu\nu}(P,q)=\frac{1}{4\pi}\int d^4z\,e^{iq\cdot z}\langle P|[j^\mu(z),j^\nu(0)]|P\rangle=\frac{1}{4\pi}\sum_X(2\pi)^4\delta^4(P+q-p_X)\langle P|j^\mu(0)|X\rangle\langle X|j^\nu(0)|P\rangle ,$$
   (the second term of the commutator does not contribute for $q^0>0$ and $x<1$); with the decomposition of CONTEXT.md this gives the parton-model $F_2=\sum_q e_q^2x(q+\bar q)$, $F_1=\frac12\sum_q e_q^2(q+\bar q)$ (checked on a free quark: $F_2=e_q^2\delta(1-x)$, $F_L=0$).
   Exact longitudinal structure function (needed in §5.7, target-mass corrections): $F_L=(1+4M^2x^2/Q^2)F_2-2xF_1$, which reduces to the CONTEXT.md definition at $M=0$.
3. **Forward Compton amplitude:** $T^{\mu\nu}=i\int d^4z\,e^{iq\cdot z}\langle P|T\,j^\mu(z)j^\nu(0)|P\rangle$, decomposed with the same tensors as $W^{\mu\nu}$ into $T_1,T_2$. With $\omega\equiv 2P\cdot q/Q^2=1/x$: $\ \operatorname{Im}T_i(\omega+i0)=2\pi F_i$ for $\omega>1$; crossing $T^{\mu\nu}(P,q)=T^{\nu\mu}(P,-q)$ gives **$T_1$ even, $T_2$ odd in $\omega$**. (Derivation: insert states; $\operatorname{Im}[-1/(\Delta+i0)]=\pi\delta(\Delta)$.)
4. **Vacuum polarization:** $i\int d^4x\,e^{iq\cdot x}\langle0|T\,j^\mu(x)j^\nu(0)|0\rangle=(q^\mu q^\nu-q^2g^{\mu\nu})\,\Pi(q^2)$. Then $\operatorname{Im}\Pi(s+i0)\ge0$, $R(s)=12\pi\operatorname{Im}\Pi(s+i0)$ (free massless Dirac fermion of unit charge: $\operatorname{Im}\Pi=1/12\pi$), and the Adler function $D(Q^2)\equiv-12\pi^2Q^2\,d\Pi(-Q^2)/dQ^2=Q^2\int_0^\infty ds\,R(s)/(s+Q^2)^2$. $\sigma(e^+e^-\to\mu^+\mu^-)=4\pi\alpha^2/3s$ (massless muons, photon exchange).
5. **Gluon PDF** (Collins' normalization):
   $$f_{g/H}(\xi)=\sum_{j=1,2}\int\frac{dw^-}{2\pi\,\xi P^+}\,e^{-i\xi P^+w^-}\langle P|G^{+j}_a(w)\,\mathcal W^{\rm adj}_{ab}[w,0]\,G^{+j}_b(0)|P\rangle ,$$
   $f_g(-\xi)=-f_g(\xi)$; free gluon: $f_{g/g}^{(0)}=\delta(1-\xi)-\delta(1+\xi)$ (c_pdf check). **$\MSbar$ convention for partonic gluon targets: average over the $D-2=2-2\varepsilon$ gluon polarizations** (c_dis: averaging over 2 instead shifts $C_2^g\to C_2^g+P_{qg}$). This must be stated explicitly in Ch. 6 and Ch. 8.
6. **Local twist-2 operators and reduced matrix elements** (forward, spin averaged, trace terms $\propto M^2$ dropped at leading twist):
   $O_q^{\mu_1\cdots\mu_n}=\bar\psi\gamma^{\{\mu_1}iD^{\mu_2}\cdots iD^{\mu_n\}}\psi-\text{traces}$, $\ O_g^{\mu_1\cdots\mu_n}=G^{\{\mu_1\alpha}iD^{\mu_2}\cdots iD^{\mu_{n-1}}G_\alpha^{\ \mu_n\}}-\text{traces}$ ($\{\}$ = normalized symmetrization), $\langle P|O_i^{\mu_1\cdots\mu_n}|P\rangle=2A_i^{(n)}P^{\mu_1}\cdots P^{\mu_n}$.
   Then (T6.10) $A_q^{(n)}=\int_{-1}^1d\xi\,\xi^{n-1}f_q(\xi)=\int_0^1dx\,x^{n-1}[q(x)+(-1)^n\bar q(x)]$ and $A_g^{(n)}=\int_0^1dx\,x^{n-1}f_g(x)$ ($n$ even). [The overall sign convention of $O_g$ must be fixed so that $\langle g|O_g^{+\cdots+}|g\rangle=2(k^+)^n$, i.e. $O_g^{+\cdots+}=G^{+j}(iD^+)^{n-2}G^{+j}$ summed over $j$; c_pdf verified $\langle k|\sum_jG^{+j}G^{+j}|k\rangle=2(k^+)^2$.]
7. **Anomalous-dimension convention:** $\gamma_{ij}(N)\equiv\int_0^1dz\,z^{N-1}P_{ij}(z)$, so $\partial f_N/\partial\ln\mu^2=\frac{\alpha_s}{2\pi}\gamma(N)f_N$ at LO and $f^{\rm NS}_N(Q)=f^{\rm NS}_N(Q_0)\,[\alpha_s(Q)/\alpha_s(Q_0)]^{-2\gamma^{(0)}(N)/\beta_0}$. LO: $\gamma_{qq}(N)=C_F[-\tfrac12+\tfrac1{N(N+1)}-2\sum_{k=2}^N\tfrac1k]$ (c_pdf). Relation to Moch–Vermaseren–Vogt: $\gamma^{(0)}_{\rm MVV}(N)=-2\gamma_{qq}(N)$ (with their $a_s=\alpha_s/4\pi$). Writers must quote this dictionary whenever citing literature values.
8. **Fragmentation function** (hadron $h$ moving in $+z$, parton momentum $k$, $z=p_h^+/k^+$, frame with $\boldsymbol p_{h,T}=0$):
   $$d_{h/q}(z)=\frac{1}{4N_c\,z}\sum_X\int\frac{dw^-}{2\pi}e^{ik^+w^-}\operatorname{Tr}_c\operatorname{Tr}_D\Big[\gamma^+\langle0|\mathcal W\psi(w)|hX\rangle\langle hX|\bar\psi(0)\mathcal W^\dagger|0\rangle\Big],$$
   with future-pointing Wilson lines along $n_B$; free quark: $d_{q/q}=\delta(1-z)$ (checked). The $D$-dimensional factor $z^{-2\varepsilon}$ that appears when the definition is written in the parton frame must be fixed by the FF writer (see Collins 2011, ch. 12, **(verify)** equation numbers).
9. **Cusp & CS kernel:** $\Gamma_{\rm cusp}=C_F\alpha_s/\pi+O(\alpha_s^2)$; Collins' $\gamma_K=2\Gamma_{\rm cusp}$; $\tilde K(b_T;\mu)=-\frac{\alpha_sC_F}{\pi}\ln(\mu^2b_T^2/b_0^2)+O(\alpha_s^2)$, $d\tilde K/d\ln\mu=-\gamma_K$; TMD anomalous dimension $\gamma_q(\alpha_s;\zeta/\mu^2)=\gamma_q(\alpha_s;1)-\frac12\gamma_K\ln(\zeta/\mu^2)$ with $\gamma_q(\alpha_s;1)=\frac32C_F\alpha_s/\pi+O(\alpha_s^2)$ (consistency with the DY hard factor checked in §11).
10. **Eikonal propagators (Wilson-line Feynman rules)**, for $D_\mu=\partial_\mu-igA_\mu$, $W[b,a]=P\exp(ig\int_a^bdz\cdot A)$ and the field expansion $A_\mu(x)=\int\frac{d^4k}{(2\pi)^4}e^{-ik\cdot x}\tilde A_\mu(k)$ ($k$ flows *into* the line). Expanding the path-ordered exponential:
   * past-pointing line $W[0,-\infty]$ along $n$ (incoming parton), gluons $k_1,\dots,k_m$ attached in order from the far end $-\infty$ towards $0$: colour factor $t^{a_m}\cdots t^{a_1}$ (later points to the left) times
     $\prod_{j=1}^m (ig\,n^{\mu_j})\,\dfrac{i}{n\cdot(k_1+\cdots+k_j)+i0}$;
   * future-pointing line $W[+\infty,0]$ (outgoing parton), gluons $k_1,\dots,k_m$ attached in order from $0$ towards $+\infty$: colour factor $t^{a_m}\cdots t^{a_1}$ times $\prod_{j=1}^m (ig\,n^{\mu_j})\,\dfrac{-i}{n\cdot(k_j+\cdots+k_m)-i0}$ (momenta summed from the far end $+\infty$).
   The $\pm i0$ follow from convergence of $\int_{-\infty}^0d\lambda\,e^{-i\lambda n\cdot k+0\lambda}=i/(n\cdot k+i0)$ and $\int_0^\infty d\lambda\,e^{-i\lambda n\cdot k-0\lambda}=-i/(n\cdot k-i0)$; they coincide with the eikonal limits of an incoming ($i\slashed p/(2p\cdot k+i0)$) and an outgoing ($-i\slashed p/(2p\cdot k-i0)$) quark propagator. Hermitian conjugate lines (right of the final-state cut) get the complex-conjugate rules. App. B proves these rules and the eikonal identity. The c_pdf agent verified numerically $dW[z,a]/dz=+igA(z)W[z,a]$, composition, retracing and covariance $W\to U(b)WU^\dagger(a)$ (reversed ordering is not covariant).

### 0.5 What "proof of factorization" means in this book (to be stated in Ch. 1 and used everywhere)

**Definition 0 (factorization statement; to become D1.2 `def:factorization`).** Let $\sigma(Q;m)$ be an observable with hard scale $Q$ and IR scales $m$ (hadron/parton masses, $\Lambda$, IR regulators). A *collinear factorization theorem at leading power* asserts
$$\sigma(Q;m)=\sum_{i,j}\int\frac{d\xi_a}{\xi_a}\frac{d\xi_b}{\xi_b}\,\hat\sigma_{ij}\Big(\frac{x_a}{\xi_a},\frac{x_b}{\xi_b},\frac{Q}{\mu},\alpha_s(\mu)\Big)f_{i/A}(\xi_a;\mu)f_{j/B}(\xi_b;\mu)+r(Q;m),$$
where (a) $f$ are defined as matrix elements of specified gauge-invariant renormalized operators; (b) $\hat\sigma$ is independent of the external states and of the IR regularization, and is computable order by order in $\alpha_s$; (c) $r=O((m/Q)^p)$ for some $p>0$ (often $p=2$ or $1$), the bound being understood order by order in $\alpha_s$ in (PT), and as an asymptotic statement for hadrons under (NP-REG). "All orders" always means "at every fixed order of $\alpha_s$", never convergence of the series.

### 0.6 Page budget (A4, 11 pt, ctexbook; target total 285, admissible 230–300)

| Part | Target pp. | Minimum |
|---|---|---|
| Front matter (abstract, notation, tag legend, overview table) | 6 | 5 |
| Ch. 1 Introduction | 10 | 8 |
| Ch. 2 Preliminaries | 18 | 15 |
| Ch. 3 IR structure | 20 | 16 |
| Ch. 4 e⁺e⁻ total (rigorous core I) | 14 | 12 |
| Ch. 5 DIS & OPE (rigorous core II) | 20 | 17 |
| Ch. 6 PDFs & FFs (incl. x-space DIS theorem) | 18 | 15 |
| Ch. 7 General method | 22 | 18 |
| Ch. 8 DIS all orders | 14 | 11 |
| Ch. 9 SIA, FFs, event shapes | 8 | 6 |
| Ch. 10 Drell–Yan, Glauber | 18 | 15 |
| Ch. 11 TMD | 18 | 15 |
| Ch. 12 Breakdown & non-rigorous cases | 14 | 11 |
| Ch. 13 Hard exclusive | 10 | 8 |
| Ch. 14 SCET | 14 | 11 |
| Ch. 15 Quarkonium | 6 | 5 |
| Ch. 16 Power corrections, renormalons, lattice | 10 | 8 |
| Ch. 17 Summary | 4 | 3 |
| App. A–H | 41 | 32 |
| **Total** | **285** | **231** |

Appendix split: A 4, B 6, C 5, D 7, E 5, F 5, G 6 (only those one-loop calculations not already in the chapters), H 3 (+ bibliography ≈ 6 pp inside H or after it).
