# research/c_pdf — PDFs, one-loop renormalization, DGLAP kernels, OPE moments, uniqueness

Directory: `/Users/hao-cheng/Desktop/theorem proof/qcd_factorization_work/research/c_pdf`
(quote the path: it contains a space).

Everything below was derived by hand and then verified by the scripts in `scripts/`
(sympy for exact algebra and integrals, numpy/mpmath for numerical cross-checks).
`sh run_all.sh` re-runs all of them (about 4 minutes) and writes `logs/*.log` and `logs/SUMMARY.txt`.

| script | content | checks |
|---|---|---|
| `s1_free_field.py` | item (1): spinors, free-field PDFs of q, q̄, g; charge conjugation; Wilson-line orientation | 21/21 PASS |
| `s2_oneloop_qq.py` | item (2): one-loop quark-in-quark PDF, Feynman gauge, gluon-mass IR regulator, pure DR | 29/29 PASS |
| `s3_splitting.py` | item (3): D-dim real-emission kernels, δ-terms, sum rules, Mellin moments, conventions | 19/19 PASS |
| `s4_moments_local.py` | item (4): moments ↔ local operators (Fourier identity, vertices, one loop exact in ε) | 8/8 PASS |
| `s5_anomalous_dims.py` | item (5): UV poles of local twist-2 operators, all four mixing entries, N = 1…14, Feynman gauge | 90/90 PASS |
| `s5b_gauge_independence.py` | item (5): same in a general covariant gauge ξ_g; δZ₂(ξ_g), δZ₃(ξ_g) | 28/28 PASS |
| `s6_uniqueness.py` | item (6): even-moment uniqueness, Müntz–Szász in L², Jensen/Blaschke, Carlson sharpness | 15/15 PASS |
| helpers | `lorentz_engine.py` (D-dim Dirac traces), `fourd.py` (UV-pole extraction, plane-wave vertex generator) | self-tests PASS |

LaTeX snippets (Chinese, monograph macros) are in `tex/`; `tex/test_c_pdf.tex` compiles them with the
common preamble (see §10).

---------------------------------------------------------------------------------------------------

## 0. Results at a glance, with literature cross-checks

"PASS" means the independently derived result equals the literature value after the stated conversion of
conventions. Sources are listed in §9; the verification status of each citation is stated there.

| # | result (our conventions, §1) | literature / conversion | status |
|---|---|---|---|
| 1a | $f^{(0)}_{q/q}(\xi)=\delta(1-\xi)$ from $\int\frac{dw^-}{4\pi}e^{-i\xi P^+w^-}\langle P|\bar\psi(w)\gamma^+W[w,0]\psi(0)|P\rangle$ | Collins–Soper 1982; Collins 2011 §7.5 (same normalization) | PASS |
| 1b | $f^{(0)}_{q/\bar q}=-\delta(1+\xi)$, hence $f^{(0)}_{\bar q/\bar q}(\xi)\equiv-f^{(0)}_{q/\bar q}(-\xi)=\delta(1-\xi)$; identical to the definition with $\psi^c=C\bar\psi^{\mathsf T}$ | CONTEXT.md $f_{\bar q}(\xi)=-f_q(-\xi)$; Collins 2011 | PASS |
| 1c | $f_g(\xi)=\sum_{j}\int\frac{dw^-}{2\pi\xi P^+}e^{-i\xi P^+w^-}\langle P|G^{+j}_a(w)W^{(A)}_{ab}[w,0]G^{+j}_b(0)|P\rangle$ gives $f^{(0)}_{g/g}=\delta(1-\xi)-\delta(1+\xi)$ | Collins–Soper 1982 normalization; momentum sum rule $\langle k\vert T^{++}_g\vert k\rangle=2(k^+)^2$ | PASS |
| 1d | $W[b,a]\to U(b)W[b,a]U^\dagger(a)$ needs "later points to the left" with $D=\partial-igA$; $\partial_zW[z,a]=+igA(z)W[z,a]$ | CONTEXT.md convention (numerical SU(2) test) | PASS |
| 2a | UV counterterm $Z_{qq}(x)=\delta(1-x)-\frac{\alpha_s}{2\pi}\frac1\varepsilon P_{qq}(x)$ for $f_{\rm ren}=Z\otimes f_{\rm bare}$ ($\overline{\rm MS}$ with $S_\varepsilon=(4\pi)^\varepsilon e^{-\varepsilon\gamma_E}$) | standard (Curci–Furmanski–Petronzio 1980; Collins 2011 Ch. 8–9) | PASS |
| 2b | Feynman-gauge pieces: ladder $\to(1-\xi)$, Wilson-line real+virtual $\to[2\xi/(1-\xi)]_+$, self-energy $\to-\frac12\delta(1-\xi)$ (UV-pole coefficients, units $\frac{\alpha_s}{2\pi}\frac{C_F}{\varepsilon}$) | sum $=C_F[(1+\xi^2)/(1-\xi)]_+$ (Altarelli–Parisi 1977) | PASS |
| 2c | $\delta Z_2=-\frac{\alpha_s}{4\pi}\frac{C_F\xi_g}{\varepsilon}$; $\delta Z_3=\frac{\alpha_s}{4\pi}\frac1\varepsilon\big[(\tfrac{13}6-\tfrac{\xi_g}2)C_A-\tfrac43T_Fn_f\big]$ | Peskin–Schroeder Ch. 16 (Feynman gauge $\xi_g=1$); standard covariant-gauge results | PASS |
| 3a | $\hat P_{qq}=C_F[\frac{1+z^2}{1-z}-\varepsilon(1-z)]$, $\hat P_{gq}=C_F[\frac{1+(1-z)^2}{z}-\varepsilon z]$, $\hat P_{qg}=T_F[1-\frac{2z(1-z)}{1-\varepsilon}]$, $\hat P_{gg}=2C_A[\frac z{1-z}+\frac{1-z}z+z(1-z)]$ | CDR spin-averaged kernels (Catani–Seymour 1997) | PASS |
| 3b | δ-terms $\frac32C_F$ and $\frac{11C_A-4n_fT_F}6=\frac{\beta_0}2$; number and momentum sum rules | Altarelli–Parisi 1977 ($(33-2n_f)/6$ for SU(3)) | PASS |
| 3c | $\gamma_{qq}(N)=C_F[\frac32+\frac1{N(N+1)}-2S_1(N)]$ etc. (all four, closed forms, non-integer $N$ via $S_1(N)=\psi(N+1)+\gamma_E$) | ESW 1996 Ch. 4 (same convention); MVV 2004: $\gamma^{(0)}_{\rm ns}=-2\gamma_{qq}=C_F[4S_1-3-\frac2{N(N+1)}]$; Gross–Wilczek/Georgi–Politzer: $\gamma_O=-\frac{\alpha_s}\pi\gamma_{qq}=\frac{\alpha_s}{2\pi}C_F[1-\frac2{N(N+1)}+4\sum_{j=2}^N\frac1j]$ | PASS |
| 3d | $N=2$ singlet eigenvalues $\{0,-\frac{4C_F+2n_fT_F}3\}$; $\langle x\rangle_q\to\frac{3n_f}{16+3n_f}$ | Gross–Wilczek 1974 | PASS |
| 4a | $\int_{-1}^1d\xi\,\xi^{n-1}f_q=\frac{\langle P\vert\bar\psi\gamma^+(iD^+)^{n-1}\psi\vert P\rangle}{2(P^+)^n}=a_n$, $\langle P\vert O^{+\cdots+}\vert P\rangle=2a_n(P^+)^n$, $a_n=\int_0^1x^{n-1}[q+(-1)^n\bar q]$ | standard (e.g. Collins 2011; ESW 1996) | PASS |
| 4b | one loop, exact in ε: $n$-th moment of the bare PDF = bare local matrix element ($n=1..8$), graph by graph | (derived; consistency) | PASS |
| 5a | from local operators: $\Gamma_{qq},\Gamma_{gq},\Gamma_{q_kg}=2\gamma_{qg},\Gamma_{gg}$ for $N=2,4,\dots,14$; odd $N$ non-singlet | Gross–Wilczek 1974; Georgi–Politzer 1974; = moments of $P_{ij}$ | PASS |
| 5b | $N=2$ matrix $\begin{pmatrix}-\frac43C_F&\frac23n_fT_F\\ \frac43C_F&-\frac23n_fT_F\end{pmatrix}$, columns sum to 0 ($T^{++}$ conserved) | momentum conservation | PASS |
| 5c | gauge-parameter independence of all $\Gamma_{ij}$ (per-graph $\xi_g$ dependence listed in §6) | general requirement | PASS |
| 6 | even-moment uniqueness (proof), $L^2$ Müntz distance formula (verified), Carlson statement | Carlson 1914; Titchmarsh 1939 §5.81; Boas 1954 Thm 9.2.1; Müntz 1914; Szász 1916; Hausdorff 1921/23 | PASS (proofs given; citations checked, §9) |

No FAIL remains. Two checks failed during development, and both were traced to my own test code, not to
the physics: an over-tight tolerance in s6(d) (the exact limit is now used) and a sympy `nsimplify` artefact in s5
(it rewrote the exact rational $-481/280$ as a product of fractional powers). Both are fixed in the scripts.

---------------------------------------------------------------------------------------------------

## 1. Conventions (in addition to CONTEXT.md, which is followed throughout)

* Metric $(+,-,-,-)$; $v^\pm=(v^0\pm v^3)/\sqrt2$; $v\cdot w=v^+w^-+v^-w^+-v_T\cdot w_T$; $\partial_-=\partial/\partial w^-=\partial^+$.
* Light-like vector $n^\mu$ with $n\cdot v=v^+$ ($n^+=0$, $n^-=1$, $n_T=0$), so $n^2=0$, $\slashed n=\gamma^+$, $(\gamma^+)^2=0$, $\{\gamma^+,\gamma^-\}=2$.
* $D_\mu=\partial_\mu-igA^a_\mu t^a$; quark–gluon vertex $ig\gamma^\mu t^a$; three-gluon vertex
  $gf^{abc}[g^{\mu\nu}(k-p)^\rho+g^{\nu\rho}(p-q)^\mu+g^{\rho\mu}(q-k)^\nu]$ (all momenta incoming; checked against
  $i\mathcal L_{\rm int}$ from $-\frac14G^2$ by plane waves in s5); ghost vertex $-gf^{abc}p^\mu$ ($p$ outgoing ghost
  momentum); gluon propagator $-i[g^{\mu\nu}-(1-\xi_g)k^\mu k^\nu/k^2]\delta^{ab}/k^2$ (Feynman gauge $\xi_g=1$).
  $G^a_{\mu\nu}=\partial_\mu A^a_\nu-\partial_\nu A^a_\mu+gf^{abc}A^b_\mu A^c_\nu$; adjoint $(D_\mu X)^a=\partial_\mu X^a+gf^{abc}A^b_\mu X^c$.
* States: $\langle P'|P\rangle=2P^+(2\pi)^3\delta(P'^+-P^+)\delta^{(2)}(P'_T-P_T)$ (covariant normalization); hence
  $\langle P|T^{\mu\nu}|P\rangle=2P^\mu P^\nu$ and $\bar u\gamma^\mu u=2p^\mu$.
* Matrix elements in PDF definitions are connected (vacuum subtracted), colour summed over the operator's
  indices and averaged over the target's colour and spin (polarization).
* Wilson line $W[b,a]=P\exp\big(ig\int_a^b dz^\mu A^a_\mu(z)t^a\big)$, later points (closer to $b$) to the left.
  For $w=(0^+,w^-,0_T)$: $W[w,0]=P\exp\big(ig\int_0^{w^-}dz^-A^+(0^+,z^-,0_T)\big)$ since $dz^\mu A_\mu=dz^-A_-=dz^-A^+$.
  Adjoint line: $W^{(A)}_{ab}[b,a]=2\,{\rm Tr}\big[t^aW[b,a]t^bW[a,b]\big]$.
* Dimensional regularization $D=4-2\varepsilon$; $\overline{\rm MS}$: $g_0^2=4\pi\alpha_s(\mu)\mu^{2\varepsilon}S_\varepsilon^{-1}+\dots$ with
  $S_\varepsilon=(4\pi)^\varepsilon e^{-\varepsilon\gamma_E}$, i.e. $\mu^2\to\mu^2e^{\gamma_E}/(4\pi)$. Useful: $\frac{g_0^2}{(2\pi)^{3-2\varepsilon}}\pi^{1-\varepsilon}=\frac{\alpha_s}{2\pi}\mu^{2\varepsilon}e^{\varepsilon\gamma_E}$
  (s2) and $e^{\varepsilon\gamma_E}\Gamma(\varepsilon)=\frac1\varepsilon+O(\varepsilon)$ (no constant term).
* Euclidean transverse master integral (checked numerically at non-integer $d$, s2):
  $\int d^dl\,\frac{(l^2)^a}{(l^2+M^2)^b}=\pi^{d/2}\frac{\Gamma(a+d/2)\Gamma(b-a-d/2)}{\Gamma(d/2)\Gamma(b)}(M^2)^{a+d/2-b}$.
* Plus distribution (CONTEXT): $\int_0^1dz\,[g(z)]_+h(z)=\int_0^1dz\,g(z)[h(z)-h(1)]$. Note
  $[2z/(1-z)]_+=2z/(1-z)_++2\delta(1-z)$ and $C_F[\frac{1+z^2}{1-z}]_+=C_F[\frac{1+z^2}{(1-z)_+}+\frac32\delta(1-z)]$.
* $S_1(N)=\sum_{j=1}^N1/j$, continued as $\psi(N+1)+\gamma_E$; Mellin moment $\gamma_{ij}(N)=\int_0^1dz\,z^{N-1}P_{ij}(z)$.
* DGLAP (CONTEXT): $\partial f_i/\partial\ln\mu^2=\frac{\alpha_s}{2\pi}\sum_jP_{ij}\otimes f_j$.

---------------------------------------------------------------------------------------------------

## 2. Item (1): free-field normalization, antiquarks, gluons, Wilson-line orientation

### 2.1 Quark PDF of a free quark

Definition (CONTEXT): $f_{q/H}(\xi)=\int\frac{dw^-}{4\pi}e^{-i\xi P^+w^-}\langle P|\bar\psi(w)\gamma^+W[w,0]\psi(0)|P\rangle_c$.
At $g^0$, $W=1$. With $\psi=\int[b\,u\,e^{-ip\cdot x}+d^\dagger v\,e^{ip\cdot x}]$, the connected matrix element in a quark
state of momentum $p=(p^+,0,0_T)$, spin $s$, colour $c$ is
$\langle p|\bar\psi_i(w)\gamma^+\psi_i(0)|p\rangle_c=\bar u_s(p)\gamma^+u_s(p)\,e^{ip\cdot w}$, $p\cdot w=p^+w^-$
(colour: $\sum_i\delta_{ic}\delta_{ic}=1$). For massless spinors along $+z$, $\bar u_s\gamma^+u_s=2p^+$ for **each**
helicity (s1, explicit Dirac representation). Then
$$f^{(0)}_{q/q}(\xi)=\frac{2p^+}{4\pi}\int dw^-e^{i(1-\xi)p^+w^-}=\frac{2p^+}{4\pi}\,2\pi\,\delta\big((1-\xi)p^+\big)=\delta(1-\xi).$$
The prefactor $1/(4\pi)$ is precisely what compensates $\bar u\gamma^+u=2p^+$ and $\int dw^-e^{ikw^-}=2\pi\delta(k)$.

### 2.2 Antiquarks

In an antiquark state, $\bar\psi(w)$ annihilates through $d\,\bar v\,e^{-ip\cdot w}$ and $\psi(0)$ creates through $d^\dagger v$;
normal ordering ($:dd^\dagger:=-d^\dagger d$) gives
$\langle\bar p|\bar\psi(w)\gamma^+\psi(0)|\bar p\rangle_c=-\bar v(p)\gamma^+v(p)\,e^{-ip^+w^-}$, with $\bar v_s\gamma^+v_s=2p^+$. Hence
$$f^{(0)}_{q/\bar q}(\xi)=-\delta(1+\xi),\qquad f_{\bar q}(\xi)\equiv-f_q(-\xi)\ \Rightarrow\ f^{(0)}_{\bar q/\bar q}(\xi)=\delta(1-\xi).$$
**Equivalence with the charge-conjugate definition.** With $\psi^c=C\bar\psi^{\mathsf T}$, $C=i\gamma^2\gamma^0$
($C^{-1}\gamma^\mu C=-\gamma^{\mu\mathsf T}$, $C^{\mathsf T}=-C$, $C^\dagger C=1$), $\bar\psi^c=-\psi^{\mathsf T}C^{-1}$, and since $\psi^c$ transforms in the
conjugate representation its Wilson line is $W^*$:
$\bar\psi^c(w)\gamma^+W^*[w,0]\psi^c(0)=-\bar\psi(0)\gamma^+W[0,w]\psi(w)+\text{c-number}$
(anticommutation; the c-number drops from connected matrix elements). Translating by $-w$ and substituting
$w^-\to-w^-$:
$$f_{\bar q}(\xi)\equiv\int\frac{dw^-}{4\pi}e^{-i\xi P^+w^-}\langle P|\bar\psi^c(w)\gamma^+W^*[w,0]\psi^c(0)|P\rangle_c=-f_q(-\xi).$$
s1 checks the free-field version: $C\bar u^{\mathsf T}$ span the $v$-spinors and $C\bar v^{\mathsf T}$ the $u$-spinors (spin sums), and the
$\psi^c$-definition gives $f^{(0)}_{\bar q/\bar q}=\delta(1-\xi)$ directly.

### 2.3 Gluon PDF and its normalization

Definition (Collins–Soper normalization; adjoint Wilson line with the same orientation):
$$f_{g/H}(\xi)=\sum_{j=1,2}\int\frac{dw^-}{2\pi\,\xi P^+}e^{-i\xi P^+w^-}\langle P|G^{+j}_a(w)\,W^{(A)}_{ab}[w,0]\,G^{+j}_b(0)|P\rangle_c
=\int\frac{dw^-}{\pi\,\xi P^+}e^{-i\xi P^+w^-}\langle P|{\rm Tr}\big[G^{+j}(w)W[w,0]G^{+j}(0)W[0,w]\big]|P\rangle_c .$$
(Sum over $D-2$ transverse $j$ in $D$ dimensions.) Gauge invariance: $G(x)\to U(x)G(x)U^\dagger(x)$ and $W[w,0]\to U(w)W[w,0]U^\dagger(0)$
leave the trace invariant.

Free gluon $|k,\lambda,b\rangle$ with $A^\mu_a\sim\epsilon^\mu_\lambda\delta_{ab}e^{-ik\cdot x}$, $\epsilon^+=0$, $k_T=0$:
$\langle0|G^{+j}_a(0)|k,\lambda,b\rangle=-ik^+\epsilon^j_\lambda\delta_{ab}$ (from $G^{+j}=\partial^+A^j-\partial^jA^+$ and $\partial^+=\partial_-\to-ik^+$).
The connected matrix element has two terms, creation at $w$/annihilation at $0$ and the reverse:
$\sum_j\langle k|G^{+j}_a(w)G^{+j}_a(0)|k\rangle_c=(k^+)^2\big(e^{ik^+w^-}+e^{-ik^+w^-}\big)$ (polarization average $\sum_j|\epsilon^j|^2=1$). Hence
$$f^{(0)}_{g/g}(\xi)=\frac{(k^+)^2}{2\pi\xi k^+}\cdot\frac{2\pi}{k^+}\big[\delta(\xi-1)+\delta(\xi+1)\big]=\delta(1-\xi)-\delta(1+\xi).$$
So $f_g$ is **odd** in $\xi$ (in general $\xi f_g(\xi)$ is even), $g(x)=f_g(x)$ for $x>0$, and
$\int_{-1}^1d\xi\,\xi^{n-1}f_g=[1+(-1)^n]\int_0^1dx\,x^{n-1}g(x)$. Normalization cross-check: with $T^{++}_g=G^{+\nu}G_\nu{}^+=\sum_jG^{+j}G^{+j}$,
$\langle k|T^{++}_g|k\rangle=2(k^+)^2$, i.e. the momentum sum rule $\int_0^1x\,g=\langle T^{++}_g\rangle/(2(P^+)^2)$ is correctly normalized (s1).

### 2.4 Wilson-line orientation and Feynman rules

* $W[b,a]$ defined with later points to the left satisfies $\frac{d}{dz}W[z,a]=+igA(z)W[z,a]$ (left multiplication) and,
  for $D=\partial-igA$ (so $A\to UAU^\dagger-\frac ig(\partial U)U^\dagger$), $W[b,a]\to U(b)W[b,a]U^\dagger(a)$. s1 verifies both numerically
  with a discretized SU(2) path-ordered exponential (error $O(N^{-2})$), and shows that the reversed ordering is
  **not** covariant (error $O(1)$). Hence $\bar\psi(w)\gamma^+W[w,0]\psi(0)$ is gauge invariant with $\psi\to U\psi$.
* Composition and retracing: $W[c,b]W[b,a]=W[c,a]$, $W[b,c]W[c,b]=1$. For the collinear PDF the points lie on one
  light-like line, so $W[w,0]=W[w,\infty n]\,W[\infty n,0]$ (future-pointing) $=W[w,-\infty n]\,W[-\infty n,0]$ (past-pointing):
  the direction to infinity is immaterial for collinear PDFs (it matters for TMDs).
* Eikonal rule (amplitude $\langle X|W[\infty n,0]\psi(0)|p\rangle$): a gluon of momentum $l$, colour $a$, index $\mu$ **emitted** by
  $W[\infty n,0]$ gives $ig\,t^an^\mu\int_0^\infty ds\,e^{is\,n\cdot l-0s}=-\,g\,t^an^\mu/(n\cdot l+i0)$; a gluon **absorbed** from a
  propagator gives $+g\,t^an^\mu/(n\cdot l-i0)$ ($l$ flowing into the line). With one real gluon (s2):
  $$\langle l,a,\epsilon|W[\infty n,0]\psi(0)|p\rangle=-g\,t^a\epsilon^*_\mu\Big[\frac{\slashed k\gamma^\mu}{k^2}+\frac{n^\mu}{n\cdot l+i0}\Big]u(p),\qquad k=p-l .$$
  The relative sign is fixed by gauge invariance: $l_\mu\times[\dots]u=\big(\frac{\slashed k\slashed l}{k^2}+1\big)u=0$ because $\slashed l u=-\slashed k u$
  (s2 checks this both contracted and as a matrix identity). Without the eikonal term the amplitude is not
  transverse.

---------------------------------------------------------------------------------------------------

## 3. Item (2): one-loop quark-in-quark PDF from the operator definition (Feynman gauge)

Target: on-shell massless quark, $p=(p^+,0^-,0_T)$, spin and colour averaged. IR regulator: gluon mass $m$
(propagator $-ig_{\mu\nu}/(l^2-m^2)$; the massive vector couples to a conserved current once the eikonal term is
included, and s2 verifies that the $l^\mu l^\nu/m^2$ part of the massive polarization sum gives zero).
UV: dimensional regularization. The PDF is written as a sum over final states,
$$f(\xi)=\sum_X\tfrac12\,\delta\big(\xi P^+-(P-p_X)^+\big)\,\langle P|[\bar\psi W](0)|X\rangle\gamma^+\langle X|[W\psi](0)|P\rangle ,$$
(the $\frac12=2\pi/(4\pi)$ comes from $\int dw^-$), with $W[w,0]=W[w,\infty n]W[\infty n,0]$ split across the cut.

**Graphs at $O(\alpha_s)$** (cut-diagram language):

| graph | description | contribution |
|---|---|---|
| R1 | real gluon, attached to the quark line on both sides of the cut (ladder) | $\propto(1-\varepsilon)(1-\xi)$ |
| R2 + h.c. | real gluon, quark line on one side, Wilson line on the other | $\propto2\xi/(1-\xi)$ |
| R3 | real gluon, Wilson line on both sides | $\propto n^2=0$ |
| V1 + h.c. | virtual gluon between the Wilson line and the quark line (same side) | $-\delta(1-\xi)\int dx\,2x/(1-x)\dots$ |
| V2 | quark self-energy on the external legs (LSZ residue) | $(R-1)\,\delta(1-\xi)$ |
| V3 | Wilson-line self-energy | $\propto n^2=0$ |

### 3.1 Real emission

Kinematics: $l=\big((1-\xi)p^+,\frac{l_T^2+m^2}{2(1-\xi)p^+},l_T\big)$, $k=p-l$, $n\cdot k=\xi p^+$, $k^2=-\frac{l_T^2+\xi m^2}{1-\xi}$.
Squaring the amplitude of §2.4 with $\sum\epsilon^\mu\epsilon^{*\nu}\to-g^{\mu\nu}$ and $\frac12\sum_s u\bar u=\frac12\slashed p$ (D-dimensional Dirac algebra, s2):
$$\tfrac12{\rm Tr}\Big[\slashed p\,\bar\Gamma^\nu\,\gamma^+\,\Gamma^\mu\Big](-g_{\mu\nu})\,g^2C_F
=g^2C_F\,p^+\Big[\underbrace{\frac{4(1-\varepsilon)(1-\xi)^2l_T^2}{(l_T^2+\xi m^2)^2}}_{\rm R1}+\underbrace{\frac{8\xi}{l_T^2+\xi m^2}}_{\rm R2+h.c.}\Big],\qquad{\rm R3}=0 .$$
The one-gluon phase space $\int\frac{dl^+d^{D-2}l_T}{(2\pi)^{D-1}2l^+}$ with the $\delta$-function fixing $l^+=(1-\xi)p^+$ gives
$$f_R(\xi)=\frac{g^2C_F}{(2\pi)^{D-1}}\int d^{D-2}l_T\Big[\frac{(1-\varepsilon)(1-\xi)\,l_T^2}{(l_T^2+\xi m^2)^2}+\frac{2\xi}{(1-\xi)(l_T^2+\xi m^2)}\Big]
=A_\varepsilon\Big[(1-\varepsilon)^2(1-\xi)\,\xi^{-\varepsilon}+\frac{2\xi^{1-\varepsilon}}{1-\xi}\Big],$$
$$A_\varepsilon\equiv\frac{\alpha_s}{2\pi}C_F\,e^{\varepsilon\gamma_E}\Gamma(\varepsilon)\Big(\frac{\mu^2}{m^2}\Big)^{\varepsilon}=\frac{\alpha_s}{2\pi}C_F\Big[\frac1\varepsilon+\ln\frac{\mu^2}{m^2}+O(\varepsilon)\Big].$$
In the massless limit, $l_T^2\times$(integrand) $=\frac{1+\xi^2}{1-\xi}-\varepsilon(1-\xi)=\hat P_{qq}(\xi;\varepsilon)/C_F$, and the light-cone-gauge
ladder graph alone (numerator $d^{\mu\nu}(l)=-g^{\mu\nu}+\frac{l^\mu n^\nu+n^\mu l^\nu}{n\cdot l}$) reproduces exactly the same D-dimensional kernel (s2).

### 3.2 Virtual Wilson-line graph V1

With the gluon emitted by the quark (momentum $l$) and absorbed by $W[\infty n,0]$, and using
$\bar u\gamma^+(\slashed p-\slashed l)\gamma^+u=2(p^+-l^+)\,\bar u\gamma^+u$:
$$\frac{V_1}{\rm tree}=ig^2C_F\int\frac{d^Dl}{(2\pi)^D}\frac{2(p^+-l^+)}{(l^+-i0)\,(l^2-m^2+i0)\,((p-l)^2+i0)} .$$
$l^-$ integral: the poles of the two propagators lie on opposite sides of the real axis iff $0<l^+<p^+$; closing the contour,
$$\int dl^-\frac{1}{(2l^+l^--l_T^2-m^2+i0)(-2(p^+-l^+)l^--l_T^2+i0)}=\frac{\pi i\,\theta(0<l^+<p^+)}{p^+(l_T^2+x\,m^2)},\qquad l^+=(1-x)p^+$$
(checked numerically in s2, including the vanishing outside $0<x<1$). Hence
$$\frac{V_1+V_1^\dagger}{\rm tree}=-\frac{g^2C_F}{(2\pi)^{D-1}}\int_0^1dx\int d^{D-2}l_T\,\frac{2x}{(1-x)(l_T^2+x\,m^2)}=-A_\varepsilon\int_0^1dx\,\frac{2x^{1-\varepsilon}}{1-x}.$$
It multiplies $\delta(1-\xi)$. Its integrand is exactly minus the R2 integrand at $\xi=x$, so R2 and V1 combine into
$A_\varepsilon\,[2\xi^{1-\varepsilon}/(1-\xi)]_+$. The endpoint singularity $x\to1$ ($l^+\to0$) is not regulated by DR. It cancels only in
this combination, which must be formed at fixed $x=\xi$ (as a distribution) before integrating.

### 3.3 Self-energy V2 (external-leg residue)

$\Sigma(p)=\slashed p\,\Sigma_V(p^2)$, residue $R=1/(1-\Sigma_V(0))$. With a massive gluon and a massless quark,
$$\Sigma_V(0)=(2-D)\frac{g_0^2C_F}{(4\pi)^{D/2}}\Gamma(\varepsilon)\int_0^1dy\,(1-y)\big[(1-y)m^2\big]^{-\varepsilon}=-A_\varepsilon\frac{1-\varepsilon}{2-\varepsilon},$$
and its UV pole $-\frac{\alpha_s}{4\pi}\frac{C_F}{\varepsilon}$ is the Feynman-gauge $\delta Z_2$ (re-derived independently from the self-energy in s5/s5b,
$\delta Z_2=-\frac{\alpha_s}{4\pi}\frac{C_F\xi_g}{\varepsilon}$ in a general covariant gauge). The two external legs together give $(R-1)\delta(1-\xi)$.

### 3.4 Bare result, quark number, UV pole

For a test function $h$:
$$\langle f^{(1)}_{\rm bare},h\rangle=A_\varepsilon\Big\{\int_0^1d\xi\Big[(1-\varepsilon)^2(1-\xi)\xi^{-\varepsilon}h(\xi)+\frac{2\xi^{1-\varepsilon}}{1-\xi}\big(h(\xi)-h(1)\big)\Big]-\frac{1-\varepsilon}{2-\varepsilon}h(1)\Big\}.$$
* Quark number holds exactly in $\varepsilon$: $(1-\varepsilon)^2\int_0^1(1-\xi)\xi^{-\varepsilon}d\xi=\frac{1-\varepsilon}{2-\varepsilon}$, so $\int_0^1f^{(1)}_{\rm bare}=0$.
* UV pole: $f^{(1)}_{\rm bare}\big|_{1/\varepsilon}=\frac{\alpha_s}{2\pi}\frac{C_F}{\varepsilon}\big\{(1-\xi)+[\frac{2\xi}{1-\xi}]_+-\frac12\delta(1-\xi)\big\}=\frac{\alpha_s}{2\pi}\frac1\varepsilon P_{qq}(\xi)$, because
  $$(1-\xi)+\Big[\frac{2\xi}{1-\xi}\Big]_+-\tfrac12\delta(1-\xi)=\Big[\frac{1+\xi^2}{1-\xi}\Big]_+=\frac{1+\xi^2}{(1-\xi)_+}+\tfrac32\delta(1-\xi)$$
  (checked against six test functions in s2). **Origin of the $\delta$-term:** $\frac32=2-\frac12$. The 2 comes from rewriting the Wilson-line
  combination R2+V1, $[2\xi/(1-\xi)]_+=2\xi/(1-\xi)_++2\delta(1-\xi)$; the $-\frac12$ is the self-energy (Z₂). The ladder R1 contributes no $\delta$-term.
* Graph-by-graph UV poles (units $\frac{\alpha_s}{2\pi}\frac{C_F}\varepsilon$): R1 $\to(1-\xi)$; R2+V1+h.c. $\to[2\xi/(1-\xi)]_+$; V2 $\to-\frac12\delta(1-\xi)$.

### 3.5 Renormalization ($\overline{\rm MS}$) and the counterterm

Convention: $f_{\rm ren}=Z\otimes f_{\rm bare}$, $(Z\otimes f)(x)=\int_x^1\frac{dz}zZ(z)f(x/z)$, $Z$ a pure pole series in $\varepsilon$ when expressed
through $\alpha_s(\mu)$ with $g_0^2=4\pi\alpha_s\mu^{2\varepsilon}S_\varepsilon^{-1}$. Finiteness at $O(\alpha_s)$ requires
$$\boxed{Z_{qq}(x)=\delta(1-x)-\frac{\alpha_s}{2\pi}\frac1\varepsilon P_{qq}(x)+O(\alpha_s^2)}\qquad\big(\text{equivalently }f_{\rm bare}=f_{\rm ren}+\tfrac{\alpha_s}{2\pi}\tfrac1\varepsilon P\otimes f_{\rm ren}\big).$$
With the opposite convention $f_{\rm bare}=Z'\otimes f_{\rm ren}$, $Z'=\delta+\frac{\alpha_s}{2\pi}\frac1\varepsilon P$; the monograph must say which is meant.
Since $d\alpha_s/d\ln\mu^2=-\varepsilon\alpha_s+O(\alpha_s^2)$ in $D$ dimensions, $\frac{dZ}{d\ln\mu^2}Z^{-1}=\frac{\alpha_s}{2\pi}P+O(\alpha_s^2)$, which reproduces the
DGLAP equation of CONTEXT.md with the same sign.

Renormalized result with the gluon-mass IR regulator (s2; regulator dependent, so not a physical PDF):
$$f^{(1)}_{q/q}(\xi;\mu)=\frac{\alpha_s}{2\pi}\Big\{P_{qq}(\xi)\ln\frac{\mu^2}{m^2}+C_F\Big[-(1-\xi)(2+\ln\xi)-\Big[\frac{2\xi\ln\xi}{1-\xi}\Big]_++\frac14\delta(1-\xi)\Big]\Big\},\qquad\int_0^1f^{(1)}=0 .$$
The $\ln\mu^2$ dependence is $\frac{\alpha_s}{2\pi}P_{qq}$, as DGLAP requires.

Off-shell regulator (cross-check of the UV coefficient only): for $p^2=-\Lambda^2$ with a massless gluon,
$\lim_{l_T\to\infty}l_T^2\times$(real integrand) $=\frac{1+\xi^2}{1-\xi}$ (s2). Off-shellness breaks gauge invariance of the finite parts and
invalidates LSZ, so only the UV coefficient is meaningful there.

### 3.6 Pure dimensional regularization (massless gluon, on-shell massless target)

All one-loop integrals are scaleless. The real graphs are $\propto\int d^{2-2\varepsilon}l_T/l_T^2$, the virtual ones vanish identically,
and (s2, with an auxiliary split at $l_T=M$)
$$\int\frac{d^{2-2\varepsilon}l_T}{l_T^2}=\underbrace{\int\frac{d^{2-2\varepsilon}l_T}{l_T^2+M^2}}_{\pi^{1-\varepsilon}\Gamma(1+\varepsilon)M^{-2\varepsilon}/\varepsilon_{\rm UV}}
+\underbrace{\int d^{2-2\varepsilon}l_T\,\frac{M^2}{l_T^2(l_T^2+M^2)}}_{-\pi^{1-\varepsilon}\Gamma(1+\varepsilon)M^{-2\varepsilon}/\varepsilon_{\rm IR}}
=\pi^{1-\varepsilon}\Gamma(1+\varepsilon)M^{-2\varepsilon}\Big(\frac1{\varepsilon_{\rm UV}}-\frac1{\varepsilon_{\rm IR}}\Big)=0$$
(the first integral converges for $\varepsilon>0$, the second for $\varepsilon<0$; after analytic continuation the sum vanishes, independently of $M$).
Hence $f^{\rm bare}_{q/q}(\xi)=\delta(1-\xi)$ to all orders in DR (no scale), and after $\overline{\rm MS}$ renormalization
$$f_{q/q}(\xi;\mu)=Z_{qq}\otimes\delta=\delta(1-\xi)-\frac{\alpha_s}{2\pi}\frac1{\varepsilon}P_{qq}(\xi)+O(\alpha_s^2)\qquad(\varepsilon\text{ now an IR pole}).$$
Generally $f_{i/j}=\delta_{ij}\delta(1-\xi)-\frac{\alpha_s}{2\pi}\frac1\varepsilon P_{ij}(\xi)+O(\alpha_s^2)$: the form used when matching partonic cross sections onto
coefficient functions. The UV counterterm is the same as in §3.5 because UV poles do not depend on the IR regulator.

---------------------------------------------------------------------------------------------------

## 4. Item (3): the four LO splitting functions, sum rules, moments, anomalous dimensions

### 4.1 D-dimensional real-emission kernels (light-cone gauge $A^+=0$, $W=1$)

For a massless on-shell parton $j$ of momentum $p$ and one real massless parton in the final state, the operator
definitions give (s3; colour factors included; CDR averages: $\frac12$ over quark spins, $\frac1{D-2}=\frac1{2(1-\varepsilon)}$ over gluon polarizations)
$$f^{\rm real}_{i/j}(\xi)=\frac{g^2}{(2\pi)^{D-1}}\int d^{D-2}l_T\,\frac{\hat P_{ij}(\xi;\varepsilon)}{l_T^2}\qquad\Big(\xrightarrow{D=4}\ \frac{\alpha_s}{2\pi}\hat P_{ij}(\xi)\int\frac{dl_T^2}{l_T^2}\Big),$$
$$\hat P_{qq}=C_F\Big[\frac{1+z^2}{1-z}-\varepsilon(1-z)\Big],\quad \hat P_{gq}=C_F\Big[\frac{1+(1-z)^2}{z}-\varepsilon z\Big],\quad
\hat P_{qg}=T_F\Big[1-\frac{2z(1-z)}{1-\varepsilon}\Big],\quad \hat P_{gg}=2C_A\Big[\frac z{1-z}+\frac{1-z}z+z(1-z)\Big].$$
Ingredients: $q\leftarrow q$: amplitude $\propto\slashed k\gamma^\mu u(p)/k^2$ with numerator $d_{\mu\nu}(l)$. $g\leftarrow q$: the gluon operator vertex
$X^{j\beta}=(n\cdot k\,g^{j\alpha}-k^jn^\alpha)d_\alpha{}^\beta(k)$ and the normalization $\frac1{\xi p^+}$ of §2.3. $q\leftarrow g$: $\sum v\bar v=\slashed l$, gluon average
$-g_T/(D-2)$. $g\leftarrow g$: the three-gluon vertex. Kinematics $k^2=-l_T^2/(1-z)$, $n\cdot k=zp^+$. These coincide with the
spin-averaged CDR kernels $\langle\hat P_{ij}(z;\varepsilon)\rangle$ of Catani–Seymour (1997).

### 4.2 Regularized kernels, $\delta$-terms, sum rules

The UV poles ($\overline{\rm MS}$ counterterms) give $P_{ij}=\hat P_{ij}(z;0)$ for $z<1$, completed at $z=1$ by the virtual graphs. The
$\delta(1-z)$ coefficients can be obtained either from the virtual graphs (§3 for $qq$; §6 for $gg$ via $\delta Z_3$) or from the
conservation laws, with identical results:
$$P_{qq}=C_F\Big[\frac{1+z^2}{1-z}\Big]_+=C_F\Big[\frac{1+z^2}{(1-z)_+}+\frac32\delta(1-z)\Big],\qquad P_{qg}=T_F\big[z^2+(1-z)^2\big],\qquad P_{gq}=C_F\frac{1+(1-z)^2}{z},$$
$$P_{gg}=2C_A\Big[\frac z{(1-z)_+}+\frac{1-z}z+z(1-z)\Big]+\frac{11C_A-4n_fT_F}{6}\,\delta(1-z),\qquad \frac{11C_A-4n_fT_F}6=\frac{\beta_0}2 .$$
* Quark number ($\psi^\dagger\psi$-type conserved current, §5): $\int_0^1P_{qq}=0\Rightarrow b_q=-C_F\int_0^1\frac{1+z^2-2}{1-z}dz=C_F\int_0^1(1+z)dz=\frac32C_F$.
* Momentum, gluon column: $\int_0^1z[P_{gg}+2n_fP_{qg}]=0$. With $\int_0^1z\frac{z}{(1-z)_+}=-\frac32$, $\int_0^1(1-z)=\frac12$, $\int_0^1z^2(1-z)=\frac1{12}$
  and $2n_fT_F\int_0^1z[z^2+(1-z)^2]=\frac23n_fT_F$: $b_g=\frac{11}6C_A-\frac23n_fT_F$.
* Momentum, quark column (an independent check; no free parameter left): $\int_0^1z[P_{qq}+P_{gq}]=C_F[-\frac{17}6+\frac32]+\frac43C_F=0$.
* Charge conjugation: $P_{\bar q\bar q}=P_{qq}$, $P_{\bar qg}=P_{qg}$, $P_{g\bar q}=P_{gq}$; $P_{q\bar q}=P_{q_kq_l}=0$ for $k\neq l$ at LO (no graph).
  Singlet $\Sigma=\sum_k(q_k+\bar q_k)$: $\frac{d}{d\ln\mu^2}\binom{\Sigma}{g}=\frac{\alpha_s}{2\pi}\begin{pmatrix}P_{qq}&2n_fP_{qg}\\P_{gq}&P_{gg}\end{pmatrix}\otimes\binom{\Sigma}{g}$;
  non-singlet $q_k\pm\bar q_k$, $q_k-q_l$: $P_{qq}$.

### 4.3 Mellin moments ("anomalous dimensions" in the DGLAP normalization)

$\gamma_{ij}(N)\equiv\int_0^1dz\,z^{N-1}P_{ij}(z)$; the moments $a_i(N)=\int_0^1x^{N-1}f_i$ obey $\frac{da_i}{d\ln\mu^2}=\frac{\alpha_s}{2\pi}\sum_j\gamma_{ij}(N)a_j$:
$$\gamma_{qq}(N)=C_F\Big[\frac32+\frac1{N(N+1)}-2S_1(N)\Big]=C_F\Big[-\frac12+\frac1{N(N+1)}-2\sum_{k=2}^N\frac1k\Big],$$
$$\gamma_{qg}(N)=T_F\frac{N^2+N+2}{N(N+1)(N+2)},\qquad \gamma_{gq}(N)=C_F\frac{N^2+N+2}{(N-1)N(N+1)},$$
$$\gamma_{gg}(N)=2C_A\Big[\frac1{N(N-1)}+\frac1{(N+1)(N+2)}-S_1(N)\Big]+\frac{11C_A-4n_fT_F}6 .$$
Key integral: $\int_0^1\frac{z^{N-1}-1}{1-z}dz=-S_1(N-1)=-[\psi(N)+\gamma_E]$ for ${\rm Re}\,N>0$ (series $\frac1{1-z}=\sum z^k$; checked at complex $N$).
Hence $\int_0^1z^{N-1}[\frac{1+z^2}{1-z}]_+=-S_1(N-1)-S_1(N+1)+\frac32=\frac32+\frac1{N(N+1)}-2S_1(N)$.
Checks (s3): direct integration for $N=2..12$ (and $N=1$ for $qq,qg$); non-integer $N=1.37,2.5,3.91,7.25$ numerically with
$S_1(N)=\psi(N+1)+\gamma_E$; $\gamma_{qq}(1)=0$; $\gamma_{qq}(2)+\gamma_{gq}(2)=0$; $2n_f\gamma_{qg}(2)+\gamma_{gg}(2)=0$; large $N$:
$\gamma_{qq}\to-2C_F(\ln N+\gamma_E)+\frac32C_F$, $\gamma_{gg}\to-2C_A(\ln N+\gamma_E)+\frac{\beta_0}2$.
$N=2$: $\begin{pmatrix}\gamma_{qq}&2n_f\gamma_{qg}\\\gamma_{gq}&\gamma_{gg}\end{pmatrix}=\begin{pmatrix}-\frac43C_F&\frac23n_fT_F\\\frac43C_F&-\frac23n_fT_F\end{pmatrix}$, eigenvalues $0$ and $-\frac{4C_F+2n_fT_F}3$;
asymptotic momentum fractions (SU(3)) $\langle x\rangle_\Sigma\to\frac{3n_f}{16+3n_f}$, $\langle x\rangle_g\to\frac{16}{16+3n_f}$.

### 4.4 Conversion table of conventions

| convention | definition | LO non-singlet | relation to ours |
|---|---|---|---|
| ours = ESW (1996) | $P=\frac{\alpha_s}{2\pi}P^{(0)}+\dots$, $\gamma=\int z^{N-1}P^{(0)}$ | $C_F[-\frac12+\frac1{N(N+1)}-2\sum_{k=2}^N\frac1k]$ | identical |
| MVV (2004) | $\frac{df}{d\ln\mu^2}=\sum_na_s^{n+1}P^{(n)}\otimes f$, $a_s=\frac{\alpha_s}{4\pi}$, $\gamma^{(n)}=-\int x^{N-1}P^{(n)}$ | $C_F[4S_1-3-\frac2{N(N+1)}]$ | $P^{(0)}_{\rm MVV}=2P$, $\gamma^{(0)}_{\rm MVV}=-2\gamma$ |
| operator (GW/GP) | $\mu\frac{dO_N}{d\mu}=-\gamma_O O_N$ | $\frac{\alpha_s}{2\pi}C_F[1-\frac2{N(N+1)}+4\sum_{j=2}^N\frac1j]$ | $\gamma_O=-\frac{\alpha_s}\pi\gamma(N)$ |
| $\frac{dO}{d\ln\mu^2}=\frac{\alpha_s}{2\pi}\Gamma O$ (§6) | $Z=1-\frac{\alpha_s}{2\pi}\frac1\varepsilon\Gamma$ | | $\Gamma_{qq}=\gamma_{qq}$, $\Gamma_{q_kg}=2\gamma_{qg}$, $\Gamma_{gq}=\gamma_{gq}$, $\Gamma_{gg}=\gamma_{gg}$ |

The MVV convention was checked against the paper itself (eqs. 2.6, 2.7, 3.4 of hep-ph/0403192). Its eq. (3.4) reads
$\gamma^{(0)}_{\rm ns}=C_F(2(S_1(N-1)+S_1(N+1))-3)$, which equals $C_F[4S_1-3-\frac2{N(N+1)}]$ because
$S_1(N-1)+S_1(N+1)=2S_1(N)-\frac1{N(N+1)}$. The paper also warns that older literature often carries an extra factor 2.

---------------------------------------------------------------------------------------------------

## 5. Item (4): Mellin moments of PDFs = matrix elements of local twist-2 operators

### 5.1 Derivation (exact identity between bare operators)

Write $M(w^-)\equiv\langle P|\bar\psi(w)\gamma^+W[w,0]\psi(0)|P\rangle_c$, so $f_q(\xi)=\int\frac{dw^-}{4\pi}e^{-i\xi P^+w^-}M(w^-)$. Use
$\xi^{n-1}e^{-i\xi P^+w^-}=\big(\frac{i}{P^+}\partial_{w^-}\big)^{n-1}e^{-i\xi P^+w^-}$, integrate by parts (boundary terms vanish for the Fourier transform
of a tempered distribution) and use $\int d\xi\,e^{-i\xi P^+w^-}=\frac{2\pi}{P^+}\delta(w^-)$:
$$\int_{-\infty}^{\infty}d\xi\,\xi^{n-1}f_q(\xi)=\frac1{2P^+}\Big(\frac{-i}{P^+}\Big)^{n-1}\frac{d^{n-1}M}{d(w^-)^{n-1}}\Big|_{w^-=0}$$
(s4(a), with a Gaussian test correlator, $n=1..6$). The derivative acts on $\bar\psi(w)W[w,0]$. From $\partial_{w^-}W[w,0]=igA^+(w)W[w,0]$ (§2.4),
$$\partial_{w^-}\big[\bar\psi(w)W[w,0]\big]=\big[\bar\psi\overleftarrow{D}{}^+\big](w)\,W[w,0],\qquad \bar\psi\overleftarrow{D}_\mu\equiv\partial_\mu\bar\psi+ig\bar\psi A_\mu ,$$
and iterating, $\partial^{n-1}_{w^-}[\bar\psi W](0)=\bar\psi(\overleftarrow{D}{}^+)^{n-1}(0)$. Hence
$$\int d\xi\,\xi^{n-1}f_q(\xi)=\frac{\langle P|\bar\psi(-i\overleftarrow{D}{}^+)^{n-1}\gamma^+\psi|P\rangle}{2(P^+)^n}=\frac{\langle P|\bar\psi\gamma^+(iD^+)^{n-1}\psi|P\rangle}{2(P^+)^n}.$$
The last step uses $\partial^+(\bar\psi X\psi)=\bar\psi\overleftarrow{D}{}^+X\psi+\bar\psi X\overrightarrow{D}{}^+\psi$ for gauge-covariant $X$ and $\langle P|\partial^+\mathcal O|P\rangle=0$ (forward
matrix element, translation invariance). The left-acting and right-acting forms agree **only in forward matrix elements**; this matters
for GPDs. The support property $f_q(\xi)=0$ for $|\xi|>1$ (Collins–Soper 1982; Jaffe 1983; Collins 2011 Ch. 6) makes $\int_{-\infty}^\infty=\int_{-1}^1$.

### 5.2 Normalization and covariant form

Let $O_q^{\mu_1\cdots\mu_n}=\mathcal S\,\bar\psi\gamma^{\mu_1}iD^{\mu_2}\cdots iD^{\mu_n}\psi-\text{traces}$ ($\mathcal S$ = symmetrization). Lorentz covariance gives
$\langle P|O_q^{\mu_1\cdots\mu_n}|P\rangle=2a_n\,(P^{\mu_1}\cdots P^{\mu_n}-\text{traces})$. For a spin-$\frac12$ target the vector operators have no
spin-dependent forward structure (parity), so spin averaging is automatic. Contracting with $n_{\mu_1}\cdots n_{\mu_n}$ (all traces vanish since $n^2=0$,
and every term of $\mathcal S$ gives the same) yields $O^{+\cdots+}=\bar\psi\gamma^+(iD^+)^{n-1}\psi$ and
$$\boxed{a_n=\int_{-1}^{1}d\xi\,\xi^{n-1}f_q(\xi)=\frac{\langle P|\bar\psi\gamma^+(iD^+)^{n-1}\psi|P\rangle}{2(P^+)^n}=\int_0^1dx\,x^{n-1}\big[q(x)+(-1)^n\bar q(x)\big]}$$
with the state normalization of §1. Gluon (even $n\ge2$), with $O_g^{(n)}=G^{+\nu}(iD^+)^{n-2}G_\nu{}^{+}=\sum_jG^{+j}(iD^+)^{n-2}G^{+j}$:
$$\int_{-1}^1d\xi\,\xi^{n-1}f_g(\xi)=\frac{\langle P|O_g^{(n)}|P\rangle}{(P^+)^n}\quad\Longrightarrow\quad \int_0^1dx\,x^{n-1}g(x)=\frac{\langle P|O_g^{(n)}|P\rangle}{2(P^+)^n}\qquad(n\ \text{even}).$$
(The $\frac1\xi$ in the gluon definition removes one power of $\xi$, hence $(iD^+)^{n-2}$ and no $\frac12$ before using the oddness of $f_g$.)
For odd $n$, $\langle P|G_a[(iD^+)^{n-2}]_{ab}G_b|P\rangle=0$ identically: moving the odd number of adjoint derivatives across gives a minus sign.
Free targets (s4(c)): quark moment 1; antiquark $(-1)^n$; gluon $1+(-1)^n$; each equals the local matrix element.

### 5.3 Even/odd $n$ and C-parity

Under charge conjugation $\mathcal S\bar\psi\gamma^{\mu_1}D^{\mu_2}\cdots D^{\mu_n}\psi\to(-1)^n(\cdots)$. So $O_q^{(n)}$ with even $n$ is C-even and measures
$q+\bar q$; with odd $n$ it is C-odd and measures $q-\bar q$ (s4(d) checks $\int_{-1}^1\xi^{n-1}f_q=\int_0^1x^{n-1}[q+(-1)^n\bar q]$ symbolically).
Only C-even ($n$ even) quark operators can mix with the gluon operators, which exist only for even $n$. In §6 this is seen
explicitly: for odd $N$ the two orientations of the quark loop in $\langle g|O_q^{(N)}|g\rangle$ cancel. For $N=1$ this is Furry's theorem for
$\langle g|\bar\psi\gamma^+\psi|g\rangle$.

### 5.4 Feynman-rule level and one-loop checks

* Vertices (s4(b)). The one-gluon term of the bilocal operator in momentum space is
  $\frac{g\,t^an^\mu\gamma^+}{2q^+}[\delta(\xi P^+-k_2^+)-\delta(\xi P^+-k_1^+)]$ ($k_2=k_1+q$). Its $n$-th moment is
  $\frac{g\,t^an^\mu\gamma^+}{2(P^+)^n}\frac{(k_2^+)^{n-1}-(k_1^+)^{n-1}}{q^+}=\frac{1}{2(P^+)^n}\big[g\,t^an^\mu\gamma^+\sum_{j=0}^{n-2}(k_2^+)^j(k_1^+)^{n-2-j}\big]$, which is exactly the
  one-gluon vertex of $\bar\psi\gamma^+(iD^+)^{n-1}\psi$. At second order the moments give the second divided differences, i.e. the complete
  homogeneous polynomials that form the two-gluon local vertex. Both are checked for $n\le7$, together with the path-ordered $s$-integral.
* One loop, exact in $\varepsilon$ (s4(e)). With the gluon-mass regulator of §3, the $n$-th moment of the bare PDF equals the bare one-loop
  matrix element of the local operator, graph by graph:
  ladder R1 ↔ vertex graph, $A_\varepsilon\frac{(1-\varepsilon)^2}{(n-\varepsilon)(n+1-\varepsilon)}$; Wilson-line R2+V1 ↔ operator-gluon graphs,
  $-2A_\varepsilon\sum_{i=1}^{n-1}\frac1{i+1-\varepsilon}$; V2 ↔ self-energy, $-A_\varepsilon\frac{1-\varepsilon}{2-\varepsilon}$. Total for $n=1$: $0$; for $n=2$: $-\frac{4A_\varepsilon}{3-\varepsilon}$ (pole $\frac{\alpha_s}{2\pi}\frac{C_F}\varepsilon(-\frac43)=\frac{\alpha_s}{2\pi}\frac{\gamma_{qq}(2)}\varepsilon$).
* Renormalized relation. The bare identity holds for every bare matrix element. $\overline{\rm MS}$ renormalization of the PDF in Mellin
  space ($f_{\rm ren}(N)=Z_f(N)f_{\rm bare}(N)$) and of the local operators ($O^R=Z_OO$) are both minimal pole subtractions making the
  same quantities finite. So $Z_f(N)=Z_O(N)$ (flavour matrices) and the boxed relation holds for renormalized quantities, given the
  multiplicative renormalizability of the gauge-invariant twist-2 operators: their mixing with BRST-exact and EOM operators drops out of
  physical matrix elements (Joglekar–Lee 1976). Verified explicitly at one loop (s4(e), §6).

---------------------------------------------------------------------------------------------------

## 6. Item (5): one-loop anomalous dimensions from the local operators (with quark–gluon mixing)

### 6.1 Operators, Feynman rules, renormalization

$O_q^{(N)}=\bar\psi\slashed n(in\cdot D)^{N-1}\psi$ (one flavour), $O_g^{(N)}=-g_{\lambda\rho}G^{a,n\lambda}[(in\cdot D)^{N-2}G]^{a,n\rho}$ ($N\ge2$), $G^{a,n\lambda}\equiv n_\mu G^{a\mu\lambda}$.
Operator-insertion vertices (no factor $i$; all momenta incoming):
* $O_q$, 2-point: $\slashed n\,(n\cdot k)^{N-1}$. 3-point (gluon $q$, colour $a$, index $\mu$; quark $k$ in): $g\,t^an^\mu\slashed n\sum_{j=0}^{N-2}(n\cdot k+n\cdot q)^j(n\cdot k)^{N-2-j}$.
* $O_g$, 2-gluon: $\delta^{ab}\,X_1\cdot X_2\,[(n\cdot q_1)^{N-2}+(n\cdot q_2)^{N-2}]$ with $X_i^\lambda=n\cdot q_i\,\epsilon_i^\lambda-n\cdot\epsilon_i\,q_i^\lambda$. Forward ($q_1=-q_2=p$,
  physical $\epsilon$): $\langle g|O_g^{(N)}|g\rangle^{(0)}=[1+(-1)^N](n\cdot p)^N$. 3-gluon ($N=2$): $2ig\sum_{\{i,j,k\}}f^{c_ic_jc_k}(n\cdot\epsilon_j)(X_i\cdot\epsilon_k)$. For general
  $N$ the 3-gluon vertex is generated mechanically by inserting plane waves into the operator (`fourd.O_gluon`); the 2- and 3-point
  rules above are checked against that generator for random momenta (s5).

Renormalization: $O_i^R=\sum_jZ_{ij}O_j$, $Z=1-\frac{\alpha_s}{2\pi}\frac1\varepsilon\Gamma$, so $\frac{dO^R}{d\ln\mu^2}=\frac{\alpha_s}{2\pi}\Gamma\,O^R$. With tree-level matrix elements
$\langle j|O_i|j\rangle^{(0)}=\delta_{ij}\cdot2(n\cdot p)^N$ (even $N$), finiteness of the on-shell matrix elements (LSZ, including the external
residues) requires
$$\frac{\text{UV pole of }\langle j|O_i|j\rangle^{(1)}_{\rm bare}}{2(n\cdot p)^N}=\frac{\alpha_s}{2\pi}\frac1\varepsilon\,\Gamma_{ij},\qquad
\langle j|O_i|j\rangle^{(1)}_{\rm bare}=\Gamma^{(1)}_{\rm 1PI}+\delta Z_j^{\rm UV}\,\langle j|O_i|j\rangle^{(0)} ,$$
with $\delta Z_q=\delta Z_2$, $\delta Z_g=\delta Z_3$ (UV poles of the on-shell residues). Matching to DGLAP via §5:
$\Gamma_{q_kq_k}=\gamma_{qq}$, $\Gamma_{q_kg}=2\gamma_{qg}$ (quark plus antiquark: $\langle g|O_{q_k}|g\rangle=2(p^+)^N\cdot2\!\int x^{N-1}f_{q/g}$ for even $N$), $\Gamma_{gq_k}=\gamma_{gq}$, $\Gamma_{gg}=\gamma_{gg}$.
Physical (on-shell, transverse) external states remove the mixing into EOM and BRST-exact operators.

**Method for UV poles** (`fourd.uv_coeff`). The UV divergence of a one-loop integral is local and independent of the IR regulator. It equals
the $1/\varepsilon$ pole of the part of the large-$l$ expansion (propagators expanded in external momenta) that is homogeneous of degree $-4$
in $l$, evaluated with $\int\frac{d^Dl}{(2\pi)^D}\frac1{(l^2)^2}\big|_{\rm UV}=\frac{i}{16\pi^2\varepsilon}$ and the angular average
$\langle l^{\mu_1}\cdots l^{\mu_{2j}}\rangle=(l^2)^j\frac{\sum_{\rm pairings}g\cdots g}{D(D+2)\cdots(D+2j-2)}$. At one loop $D\to4$ in the numerator algebra suffices
for the pole. On-shell massless kinematics is therefore allowed although the full integrals are scaleless. Tested on scalar, vector and
rank-2 bubbles, e.g. ${\rm UV}\int\frac{l^\mu l^\nu}{l^2(l-q)^2}=\frac{i}{16\pi^2\varepsilon}(\frac{q^\mu q^\nu}3-\frac{g^{\mu\nu}q^2}{12})$.
External states in the code: $p=t(1,0,0,1)$, $n=(1,0,0,-1)$, linear polarizations $\hat x,\hat y$ (averaged); explicit 4×4 Dirac matrices; explicit
SU(2) colour for gluon graphs ($C_A=2$, divided out; every one-loop gluon graph is $\propto f f=C_A\delta$).

### 6.2 Self-energies (independent re-derivation of $\delta Z_2$, $\delta Z_3$)

Covariant gauge $\xi_g$ (s5b; Feynman gauge in s5):
$\Sigma_V^{\rm UV}=-\frac{\alpha_s}{4\pi}\frac{C_F\xi_g}{\varepsilon}$, i.e. $\delta Z_2=-\frac{\alpha_s}{4\pi}\frac{C_F\xi_g}\varepsilon$. Gluon loop + ghost loop give $\Pi^{\rm UV}=\frac{\alpha_s}{4\pi}\frac1\varepsilon(\frac{13}6-\frac{\xi_g}2)C_A$;
the quark loop gives $-\frac{\alpha_s}{4\pi}\frac1\varepsilon\frac43T_Fn_f$ (sum of 1PI graphs $=i(p^2g^{\mu\nu}-p^\mu p^\nu)\Pi$). The UV pole is transverse, and
$\delta Z_3=\Pi^{\rm UV}$. In units $\frac{\alpha_s}{2\pi}\frac1\varepsilon$: $\delta Z_2=-\frac{\xi_g}2C_F$, $\delta Z_3=(\frac{13}{12}-\frac{\xi_g}4)C_A-\frac23T_Fn_f$ (Feynman: $-\frac12C_F$, $\frac56C_A-\frac23T_Fn_f$).

### 6.3 Hand derivation of the quark-sector graphs (Feynman gauge)

Throughout: Feynman parameters, shift, keep the numerator terms of degree 2 (for three propagators) or 0 (for two), and use
$\langle(n\cdot q)(p\cdot q)\rangle=\frac{q^2}4n\cdot p$, $\langle(n\cdot q)^2\rangle=\frac{q^2}4n^2=0$, $\langle(\epsilon\cdot q)^2\rangle=-\frac{q^2}4$, $p^2=0$. The tree is $2(n\cdot p)^N$.

**A1 (vertex graph, $\langle q|O_q|q\rangle$).** $A_1=-ig^2C_F\int_k\frac{\frac12{\rm Tr}[\slashed p\gamma^\mu\slashed k\slashed n\slashed k\gamma_\mu](n\cdot k)^{N-1}}{(k^2)^2(p-k)^2}$; $\gamma^\mu\slashed k\slashed n\slashed k\gamma_\mu=-2\slashed k\slashed n\slashed k$ gives
the numerator $-8(n\cdot k)^N(p\cdot k)+4k^2(n\cdot k)^{N-1}n\cdot p$. With $k=q+yp$ and weight $2(1-y)dy$, the degree-2 part is $2y^{N-1}(n\cdot p)^Nq^2$, so
$$A_1^{\rm UV}=\frac{\alpha_s}{4\pi}\frac{C_F}\varepsilon(n\cdot p)^N\!\int_0^1\!2(1-y)\,2y^{N-1}dy=\frac{\alpha_s}{4\pi}\frac{C_F}{\varepsilon}\frac{4(n\cdot p)^N}{N(N+1)}\ \Rightarrow\ \frac{\alpha_s}{2\pi}\frac{C_F}{\varepsilon}\,\frac1{N(N+1)} .$$
**A2 = A3 (operator–gluon graphs).** $A_2=ig^2C_F\int_l\frac{\frac12{\rm Tr}[\slashed p\slashed n\slashed k\slashed n]\sum_j(n\cdot p)^j(n\cdot k)^{N-2-j}}{l^2k^2}$, $k=p-l$, with $\slashed n\slashed k\slashed n=2n\cdot k\,\slashed n$. Only the
$q$-independent term survives ($k=q+xp$, $(n\cdot q)^m$ averages to 0):
$$A_2^{\rm UV}=-\frac{\alpha_s}{4\pi}\frac{C_F}\varepsilon4(n\cdot p)^N\sum_{j=0}^{N-2}\int_0^1x^{N-1-j}dx=-\frac{\alpha_s}{4\pi}\frac{C_F}{\varepsilon}4(n\cdot p)^N\sum_{m=2}^N\frac1m\ \Rightarrow\ -\frac{\alpha_s}{2\pi}\frac{C_F}\varepsilon\big(S_1(N)-1\big).$$
Total: $\Gamma_{qq}=C_F[\frac1{N(N+1)}-2(S_1-1)-\frac12]=\gamma_{qq}(N)$.

**B ($\langle q|O_g|q\rangle$).** $B=ig^2C_F\int_l\frac{T^{\sigma\nu}V_{\nu\sigma}(l,-l)}{(l^2)^2(l-p)^2}$, $T^{\sigma\nu}=\frac12{\rm Tr}[\slashed p\gamma^\sigma\slashed k\gamma^\nu]$, $k=p-l$, and for even $N$
$V_{\nu\sigma}=2(n\cdot l)^{N-2}[-(n\cdot l)^2g_{\nu\sigma}+n\cdot l(l_\nu n_\sigma+n_\nu l_\sigma)-l^2n_\nu n_\sigma]$. Then
$T\cdot V=8(n\cdot l)^{N-2}[2(n\cdot p)(n\cdot l)(p\cdot l)-(n\cdot l)^2(p\cdot l)-l^2(n\cdot p)^2]$. With $l=q+yp$ and weight $2(1-y)$, the degree-2 part is
$-(4y^{N-2}+2Ny^{N-1})(n\cdot p)^Nq^2$, so
$$B^{\rm UV}=\frac{\alpha_s}{4\pi}\frac{C_F}\varepsilon(n\cdot p)^N\Big[\frac8{N(N-1)}+\frac4{N+1}\Big]\ \Rightarrow\ \frac{\alpha_s}{2\pi}\frac{C_F}\varepsilon\frac{N^2+N+2}{(N-1)N(N+1)}=\frac{\alpha_s}{2\pi}\frac{\gamma_{gq}(N)}\varepsilon .$$
**C1 = C2 ($\langle g|O_q|g\rangle$, the two orientations of the quark loop).**
$C_1=-iT_F\int_l\frac{(n\cdot l)^{N-1}{\rm Tr}[\slashed n\slashed l\slashed\epsilon(\slashed l-\slashed p)\slashed\epsilon\slashed l]}{(l^2)^2(l-p)^2}$; the trace is $16(n\cdot l)(\epsilon\cdot l)^2+4l^2(n\cdot l)-8(n\cdot l)(p\cdot l)+4(n\cdot p)l^2$
($n\cdot\epsilon=\epsilon\cdot p=0$, $\epsilon^2=-1$). The degree-2 part is $(2Ny^N+2y^{N-1})(n\cdot p)^Nq^2$ (the $(\epsilon\cdot q)^2$ and $q^2$ pieces cancel), so
$$C_1^{\rm UV}=\frac{\alpha_s}{4\pi}\frac{T_F}\varepsilon\frac{4(N^2+N+2)}{N(N+1)(N+2)}(n\cdot p)^N\ \Rightarrow\ \frac{\alpha_s}{2\pi}\frac{T_F}\varepsilon\frac{N^2+N+2}{N(N+1)(N+2)} .$$
$C_2=(-1)^NC_1$ (C-parity), so $\Gamma_{q_kg}=C_1+C_2=2\gamma_{qg}(N)$ for even $N$ and $0$ for odd $N$. Graphs with the operator's
$\bar\psi\psi A$ vertex on an external gluon vanish because they are $\propto n\cdot\epsilon=0$.

### 6.4 Per-graph results (units $\frac{\alpha_s}{2\pi}\frac1\varepsilon\times$colour factor, relative to tree), verified for $N=1..14$

| graph | Feynman gauge | general covariant gauge $\xi_g$ |
|---|---|---|
| A1 vertex ($C_F$) | $\frac1{N(N+1)}$ | $\frac1{N(N+1)}+\frac{\xi_g-1}2$ |
| A2 = A3 operator–gluon ($C_F$) | $-(S_1(N)-1)$ | same |
| $\delta Z_2$ ($C_F$) | $-\frac12$ | $-\frac{\xi_g}2$ |
| **sum** | $\gamma_{qq}/C_F=\frac32+\frac1{N(N+1)}-2S_1$ | same |
| B ($C_F$) | $\frac{N^2+N+2}{(N-1)N(N+1)}$ | same ($N=2,4,6,8$) |
| C1 = C2 ($T_F$, per flavour) | $\frac{N^2+N+2}{N(N+1)(N+2)}$ (odd $N$: $C_1=-C_2$) | gauge independent (no internal gluon) |
| D1 (2-gluon vertex + two 3-gluon vertices; $C_A$) | $\frac2{N(N-1)}+\frac2{(N+1)(N+2)}+\frac1{N+1}$ | $+\frac{\xi_g-1}2$ |
| D2 = D3 (3-gluon operator vertex; sym. factor $\frac12$; $C_A$) | $-(S_1(N)-1)-\frac{N+2}{2(N+1)}$ | $-\frac{\xi_g-1}8$ |
| $\delta Z_3$ | $\frac56C_A-\frac23T_Fn_f$ | $\frac56C_A-\frac{\xi_g-1}4C_A-\frac23T_Fn_f$ |
| **sum** | $\gamma_{gg}$ | same |

Graphs with vanishing UV pole: the tadpoles built from the operator's two-gluon-field terms (one propagator, no log) and the graph
"operator 2-vertex + QCD 4-gluon vertex" (no external momentum flows through the loop, so no degree $-4$ term). The $D_2$ formula was
inferred from $N\le10$ and then confirmed out of sample at $N=12,14$. The $n_f$ part of $\gamma_{gg}$ comes entirely from $\delta Z_3$ (there is no
1PI quark graph in $\langle g|O_g|g\rangle$ at one loop). Notably $D_1+D_2+D_3+\delta Z_3|_{C_A}=0$ at $N=2$.

### 6.5 $N=2$ mixing and $T^{++}$

$\Gamma^{(N=2)}$ in the basis $(\Sigma=\sum_kO_{q_k},\,O_g)$: $\begin{pmatrix}-\frac43C_F&\frac23n_fT_F\\\frac43C_F&-\frac23n_fT_F\end{pmatrix}$, identical to the moments of $P_{ij}$ (§4.3). Both
columns sum to zero, so $T^{++}=\Sigma^{(2)}+O_g^{(2)}$ is not renormalized (energy-momentum conservation). Odd $N$: pure non-singlet,
$\Gamma=\gamma_{qq}(N)$ (C-odd; $N=1$: $\gamma=0$, conserved vector current).

Literature: Gross–Wilczek (1974) and Georgi–Politzer (1974) obtained these operator anomalous dimensions. In their normalization
$\gamma_O=-\frac{\alpha_s}\pi\Gamma$ (§4.4), e.g. $\gamma^{\rm NS}_O=\frac{g^2}{8\pi^2}C_F[1-\frac2{N(N+1)}+4\sum_{j=2}^N\frac1j]$. Equality with the Mellin moments of the
Altarelli–Parisi kernels is the classic statement (Altarelli–Parisi 1977); Peskin–Schroeder Ch. 18 reproduces it. **PASS** for all
four entries and all $N$ computed.

---------------------------------------------------------------------------------------------------

## 7. Item (6): uniqueness from even moments; Müntz–Szász; Carlson-type continuation in $N$

### 7.1 Hausdorff uniqueness

**Lemma 7.1.** Let $\mu$ be a finite signed Borel measure on $[0,1]$ with $\int t^m\,d\mu=0$ for all $m\in\mathbb N_0$. Then $\mu=0$. In
particular, if $h\in L^1(0,1)$ and $\int_0^1t^mh(t)\,dt=0$ for all $m\ge0$, then $h=0$ a.e.

*Proof.* For $\varphi\in C[0,1]$ choose polynomials $P_j\to\varphi$ uniformly (Weierstrass). Then $|\int\varphi\,d\mu|=|\int(\varphi-P_j)d\mu|\le\|\varphi-P_j\|_\infty|\mu|([0,1])\to0$.
So $\int\varphi\,d\mu=0$ for all continuous $\varphi$, and $\mu=0$ by the uniqueness part of the Riesz representation theorem. For $h\in L^1$ without
measure theory: approximate $\mathbf 1_{[a,b]}$ pointwise by continuous $0\le\varphi_k\le1$. Dominated convergence gives $\int_a^bh=0$ for all $a<b$, so
$H(x)=\int_0^xh\equiv0$ and $h=H'=0$ a.e. (Lebesgue differentiation). ∎
(Hausdorff 1921, 1923 for the moment problem on a finite interval; uniqueness is the easy half.)

### 7.2 Even moments suffice (the substitution $t=x^2$)

**Theorem 7.2.** Let $g$ be measurable on $(0,1)$ with $x^{2k_0}g\in L^1(0,1)$ for some integer $k_0\ge1$. If $\int_0^1x^{2k}g(x)\,dx=0$ for all
$k\ge k_0$, then $g=0$ a.e. on $(0,1)$.

*Proof.* Put $h(t)=\frac12t^{k_0-\frac12}g(\sqrt t)$. With $t=x^2$, $dt=2x\,dx$:
$\int_0^1|h|\,dt=\int_0^1x^{2k_0}|g|\,dx<\infty$ and $\int_0^1t^mh(t)\,dt=\int_0^1x^{2(m+k_0)}g(x)\,dx=0$ for all $m\ge0$. By Lemma 7.1, $h=0$ a.e. The map $t\mapsto\sqrt t$
and its inverse are locally Lipschitz on $(0,1)$, so they preserve null sets, and $g=0$ a.e. ∎
For $k_0=1$, $h(t)=\sqrt t\,g(\sqrt t)/2$ and $\int_0^1x^{2k}g=\int_0^1t^{k-1}h(t)dt$ (s6(a): one exact case and three cases with integrable endpoint
singularities at 40 digits). Any tail $k\ge k_0$ of the even moments suffices, and Müntz–Szász is not needed.

**Corollary 7.3 (PDFs).** Let $f_q$ be supported in $[-1,1]$ with $x^{N_1-1}(q+\bar q)$ and $x^{N_1-1}(q-\bar q)$ in $L^1(0,1)$. The moments
$a_N=\int_{-1}^1\xi^{N-1}f_q$ for **even** $N\ge N_1$ determine $q_+=q+\bar q$ a.e.; those for **odd** $N\ge N_1$ determine $q_-=q-\bar q$; the gluon moments
$\int_0^1x^{N-1}g$ for even $N\ge N_1$ determine $g$. (Apply Theorem 7.2 to $q_+(x)/x$, to $q_-(x)$, and to $g(x)/x$.) Even moments alone do **not**
determine $q$ and $\bar q$ separately (s6(h): an explicit pair with equal $q+\bar q$ has identical even and different odd moments).

**Caveat: uniqueness is not stability.** Recovering $h$ from finitely many moments is exponentially ill-conditioned. The $K\times K$ moment Gram
(Hilbert) matrix has ${\rm cond}_2\approx e^{3.5K}$ ($4.8\times10^5$ at $K=5$, $2.5\times10^{28}$ at $K=20$; s6(c)). With exact rational moments the
shifted-Legendre expansion of $h$ converges in $L^2$ (relative error $9\times10^{-5}$ with 48 terms for $g=x^{1/2}(1-x)^3(1+4x)$; s6(b)). In
practice one continues analytically in $N$ and inverts the Mellin transform along a contour (§7.5).

### 7.3 Müntz–Szász (for reference)

**Theorem 7.4 (Müntz 1914, Szász 1916).** For $0<\lambda_1<\lambda_2<\cdots\to\infty$, ${\rm span}\{1,x^{\lambda_1},x^{\lambda_2},\dots\}$ is dense in $C[0,1]$ iff
$\sum_k1/\lambda_k=\infty$. (Rudin, *Real and Complex Analysis*, 3rd ed., Ch. 15, §§15.25–15.27; proof via Jensen and Blaschke.)

$L^2$ version, fully explicit. The Gram matrix of $\{x^{a_i}\}$ in $L^2(0,1)$ is the Cauchy matrix $\big(\frac1{a_i+a_j+1}\big)$. Cauchy's determinant
formula then gives, for distinct $\lambda,\lambda_k>-\frac12$,
$$\operatorname{dist}_{L^2(0,1)}\big(x^\lambda,{\rm span}\{x^{\lambda_1},\dots,x^{\lambda_K}\}\big)=\frac1{\sqrt{2\lambda+1}}\prod_{k=1}^K\frac{|\lambda-\lambda_k|}{\lambda+\lambda_k+1}$$
(s6(d) verifies the Gram-determinant ratio exactly). For $\lambda_k\to\infty$ the product tends to 0 iff $\sum1/\lambda_k=\infty$. Illustration: $x^1$ against
$\{x^{2k}\}$ has distance $\sim K^{-3/2}\to0$, whereas $x^1$ against $\{x^{k^2+1}\}$ has distance $\to\pi/\sinh(\sqrt3\pi)=0.02722\ne0$ (Euler product for
$\sinh$; s6(d)).

### 7.4 LO kernels are fixed by their even moments

**Proposition 7.5.** Let $P=r(x)+a\,[\frac1{1-x}]_++b\,\delta(1-x)$ with $|r(x)|\le C/x$ on $(0,1]$. Its Mellin transform
$M_P(N)=\int_0^1x^{N-1}r\,dx-a[\psi(N)+\gamma_E]+b$ (${\rm Re}\,N>1$) vanishes for all even $N\ge N_1$ only if $a=b=0$ and $r=0$ a.e.

*Proof.* Along even $N\to\infty$: $|\int x^{N-1}r|\le C/(N-1)\to0$ and $\psi(N)=\ln N+O(1/N)$. So $0=-a\ln N+(b-a\gamma_E)+o(1)$, which forces $a=0$ and
then $b=0$. What remains is $\int_0^1x^{N-1}r\,dx=\int_0^1x^{2k}\,[r(x)/x]\,dx=0$ for all $k\ge N_1/2$ ($N=2k$). Since $x^{2k_0}|r/x|\le Cx^{2k_0-2}$ is integrable for $k_0\ge1$,
Theorem 7.2 gives $r/x=0$, i.e. $r=0$ a.e. ∎
So the x-space LO kernels are uniquely determined by the even-$N$ anomalous dimensions that the OPE provides (s6(g) recovers $a=2$,
$b=\frac32$ for $P_{qq}/C_F$ from the large-$N$ behaviour).

### 7.5 Continuation in $N$: Carlson's theorem and the version actually needed

**Theorem 7.6 (Carlson 1914).** Let $F$ be holomorphic in ${\rm Re}\,z>0$ and continuous in ${\rm Re}\,z\ge0$, with $|F(z)|\le Ce^{\tau|z|}$ there for some
$\tau<\infty$, $|F(iy)|\le Ce^{c|y|}$ for real $y$ with some $c<\pi$, and $F(n)=0$ for $n=0,1,2,\dots$. Then $F\equiv0$.
The constant $\pi$ is sharp: $\sin\pi z$. Proof via Phragmén–Lindelöf; see Titchmarsh, *The Theory of Functions* (2nd ed., 1939) §5.81 and
Boas, *Entire Functions* (1954) Thm 9.2.1 (both locations confirmed through Waldschmidt 2020, arXiv:2002.01223, which cites them for
this theorem). The statement above follows the form given in standard references (e.g. the Wikipedia article on Carlson's theorem, which
cites Titchmarsh §5.81). For zeros only at **even** integers, apply it to $F(2z+N_1)$: the admissible type along ${\rm Im}\,N$ halves to $<\pi/2$, and
$\sin(\pi N/2)$ (type exactly $\pi/2$; $|\sin(\pi(2+iy)/2)|=\sinh(\pi|y|/2)$, s6(f)) is the borderline counterexample.

**Proposition 7.7 (sufficient for all applications to moments; full proof).** Let $F$ be holomorphic in ${\rm Re}\,z>\sigma_0$ with
$|F(z)|\le C(1+|z|)^m$ there. If $F(z_k)=0$ for $z_k=z_0+kd$, $k=1,2,\dots$ ($z_0\in\mathbb R$, $d>0$, $z_0+d>\sigma_0$), then $F\equiv0$.

*Proof.* Translate so that $\sigma_0=0$ and set $H(z)=F(z)/(z+1)^m$. Since $|z+1|\ge\max(1,|z|)$ for ${\rm Re}\,z>0$, $H$ is bounded, say by $M$. The map
$w=\frac{z-1}{z+1}$ sends ${\rm Re}\,z>0$ onto the unit disc, so $\Phi(w)=H(\frac{1+w}{1-w})$ is bounded and holomorphic for $|w|<1$, with zeros
$w_k=\frac{x_k-1}{x_k+1}$, where $x_k=z_k-\sigma_0\to\infty$ are real, and $1-|w_k|=\frac2{x_k+1}$ once $x_k>1$, so $\sum_k(1-|w_k|)=\infty$ (harmonic tail). Suppose $\Phi\not\equiv0$; write $\Phi=w^j\Psi$ with $\Psi(0)\ne0$.
$\Psi$ is still bounded by $M$ (maximum principle on $|w|=r\uparrow1$). Jensen's formula on $|w|=r<1$ (no zeros on the circle) gives
$\log|\Psi(0)|=\sum_{|w_k|<r}\log\frac{|w_k|}r+\frac1{2\pi}\int_0^{2\pi}\log|\Psi(re^{i\theta})|d\theta\le\sum_{|w_k|<r}\log\frac{|w_k|}r+\log M$. Hence
$\sum_{|w_k|<r}\log\frac r{|w_k|}\le\log\frac M{|\Psi(0)|}$ for all $r<1$, and by monotone convergence $\sum_k\log\frac1{|w_k|}<\infty$. Since $\log\frac1s\ge1-s$, this gives
$\sum(1-|w_k|)<\infty$, a contradiction. ∎
(Jensen's formula: Rudin RCA 3rd ed. Ch. 15, §§15.16–15.20; s6(e) checks the formula numerically and the divergence
$\sum2/(2k+1)\sim\ln K$ for zeros at the even integers.)

**Corollary 7.8.**
(i) For $x^{\sigma_0-1}q\in L^1(0,1)$, $M_q(N)=\int_0^1x^{N-1}q\,dx$ is holomorphic and bounded by $\int x^{\sigma_0-1}|q|$ in ${\rm Re}\,N\ge\sigma_0$. So two such Mellin
transforms that agree on an arithmetic progression of (even) integers agree identically, and the continuation of a moment sequence from
even $N$ is unique.
(ii) Mellin transforms of LO kernels (class of Prop. 7.5) are $O(\ln|N|)$ for ${\rm Re}\,N\ge\sigma_0>1$, hence polynomially bounded. Their
continuation from even $N$ is unique, e.g. $S_1(N)\mapsto\psi(N+1)+\gamma_E$. Adding $c\,\sin(\pi N/2)$ keeps all even-$N$ values but grows like
$e^{\pi|{\rm Im}N|/2}$, so it is excluded.
(iii) The continuations from even and from odd $N$ are in general **different** functions ($q+\bar q$ vs $q-\bar q$). At LO they coincide for
$qq$. Beyond LO $\gamma^+_{\rm ns}\ne\gamma^-_{\rm ns}$ (MVV 2004 treat them separately).
(iv) Carlson's theorem proper (exponential type $<\pi$ on the imaginary axis, after rescaling) is needed only when one starts from integer
values without a polynomial bound. For moments of PDFs and of DGLAP kernels, Proposition 7.7 suffices and is proved above.

---------------------------------------------------------------------------------------------------

## 8. Discrepancies, corrections and additions for CONTEXT.md / OUTLINE v0; suggested rigor tags

1. **Gluon PDF missing from CONTEXT.md.** Add (binding):
   $f_{g/H}(\xi;\mu)=\sum_{j}\int\frac{dw^-}{2\pi\xi P^+}e^{-i\xi P^+w^-}\langle P|G^{+j}_a(w)W^{(A)}_{ab}[w,0]G^{+j}_b(0)|P\rangle_c$ ($\overline{\rm MS}$), with
   $W^{(A)}_{ab}[w,0]=2{\rm Tr}[t^aW[w,0]t^bW[0,w]]$. Then $f^{(0)}_{g/g}=\delta(1-\xi)-\delta(1+\xi)$ (odd in $\xi$), $g(x)=f_g(x)$ for $x>0$, and
   $\int_0^1x\,g=\langle T^{++}_g\rangle/(2(P^+)^2)$. The task's "$f^{(0)}_{g/g}=\delta(1-\xi)$" holds on $\xi>0$.
2. **OUTLINE Ch. 6, "support $0\le\xi\le1$".** As defined, $f_q(\xi)$ has support $-1\le\xi\le1$; its negative-$\xi$ part is $-\bar q(-\xi)$. The densities
   $q(x),\bar q(x),g(x)$ have support $0\le x\le1$ (perturbation theory: Collins–Soper 1982, Jaffe 1983).
3. **OUTLINE Ch. 5, "Hausdorff/Müntz uniqueness from even moments".** Correct but sharpen it. (a) Even moments determine only the C-even
   combinations ($q+\bar q$, $g$); $q-\bar q$ needs odd moments (e.g. $F_3$). (b) The substitution $t=x^2$ reduces the problem to Hausdorff
   uniqueness (Weierstrass), so Müntz–Szász is not needed (Theorem 7.2, full proof). (c) Uniqueness is not stability: the inversion is
   exponentially ill-conditioned. (d) For the continuation of $\gamma(N)$ from even $N$, Proposition 7.7 (polynomial bound, proof via Jensen)
   suffices. Carlson's theorem is the sharp general tool (exponential type $<\pi/2$ in $N$ for even-integer data).
4. **Sign convention of $Z$.** $Z_{qq}=\delta-\frac{\alpha_s}{2\pi}\frac1\varepsilon P_{qq}$ is correct for $f_{\rm ren}=Z\otimes f_{\rm bare}$. For $f_{\rm bare}=Z'\otimes f_{\rm ren}$ (also common) the sign of
   the pole flips. The monograph should fix one convention explicitly.
5. **Moment identity, left versus right derivatives.** Differentiating $\bar\psi(w)W[w,0]$ produces $\bar\psi(-i\overleftarrow D{}^+)^{n-1}\gamma^+\psi$. It equals
   $\bar\psi\gamma^+(iD^+)^{n-1}\psi$ only in forward matrix elements, which matters if the chapter is extended to GPDs.
6. **Gauge dependence of individual graphs.** In the local-operator computation only the sum including $\delta Z_{2,3}$ is gauge independent
   (§6.4 lists each graph's $\xi_g$-dependence). Statements like "the vertex graph gives $1/(N(N+1))$" are Feynman-gauge statements.
7. **Correspondence of graphs (useful for the text).** PDF graphs and local-operator graphs map one to one, exactly in $\varepsilon$ (s4(e)):
   ladder ↔ vertex graph; Wilson-line real+virtual ↔ graphs with the gluon from $D^+$; self-energy ↔ self-energy.
8. **Regulator-dependent finite parts.** The gluon-mass finite part in §3.5 is not a physical quantity. Only its UV pole and its $\ln\mu^2$
   coefficient are regulator independent. In pure DR the partonic PDF is $\delta_{ij}\delta(1-\xi)-\frac{\alpha_s}{2\pi\varepsilon}P_{ij}$.
9. No error found in the binding conventions themselves: metric, $D_\mu$, $W[b,a]$ orientation, $S_\varepsilon$, DGLAP normalization, plus
   distribution and $\beta_0$ are mutually consistent with all results here, as checked.

**Suggested rigor tags.**
* Free-field normalizations, gauge invariance, Wilson-line orientation: \tagR.
* One-loop quark-in-quark PDF and $Z_{qq}$ at $O(\alpha_s)$: \tagR (explicit).
* LO $P_{ij}$ with $\delta$-terms: \tagR (one loop; $\delta_{gg}$ from both $\delta Z_3$ and momentum conservation).
* Bare moment identity: \tagR. Renormalized moment identity: \tagR at one loop (shown). To all orders it rests on the renormalization theory of
  gauge-invariant operators (Joglekar–Lee 1976), which I would tag \tagA unless the monograph proves it.
* One-loop anomalous dimensions from local operators, including mixing: \tagR.
* Theorems 7.2, 7.5, 7.7 and Lemma 7.1: \tagR (complete proofs here). Carlson and Müntz–Szász: classical, cited.

---------------------------------------------------------------------------------------------------

## 9. References and verification status

Verified online during this work (statement or citation location checked):
* F. Carlson, *Sur une classe de séries de Taylor*, Dissertation, Uppsala (1914). E.C. Titchmarsh, *The Theory of Functions*, 2nd ed., OUP
  (1939), §5.81. R.P. Boas, *Entire Functions*, Academic Press (1954), Thm 9.2.1. These locations are as cited in M. Waldschmidt,
  arXiv:2002.01223 (2020) (text read), which states the theorem as "no nonzero entire function of exponential type $<\pi$ vanishes on $\mathbb N$".
  The Wikipedia article "Carlson's theorem" gives the half-plane form with the imaginary-axis bound $c<\pi$ and cites Titchmarsh §5.81.
* C.H. Müntz, "Über den Approximationssatz von Weierstrass", in *H.A. Schwarz Festschrift*, Berlin (1914) 303–312. O. Szász, "Über die
  Approximation stetiger Funktionen durch lineare Aggregate von Potenzen", Math. Ann. **77** (1916) 482–496.
* F. Hausdorff, "Summationsmethoden und Momentfolgen I, II", Math. Z. **9** (1921) 74–109, 280–299; "Momentprobleme für ein endliches
  Intervall", Math. Z. **16** (1923) 220–248.
* W. Rudin, *Real and Complex Analysis*, 3rd ed. (1987), Ch. 15. Section ranges confirmed: §§15.16–15.20 Jensen's formula, §§15.21–15.24
  Blaschke products, §§15.25–15.27 Müntz–Szász. Individual theorem numbers not checked.
* S. Moch, J.A.M. Vermaseren, A. Vogt, Nucl. Phys. **B688** (2004) 101, hep-ph/0403192 (eqs. 2.6, 2.7, 3.4 read). A. Vogt, S. Moch,
  J.A.M. Vermaseren, Nucl. Phys. **B691** (2004) 129, hep-ph/0404111.
* J.C. Collins, *Foundations of Perturbative QCD*, CUP (2011). Chapter titles confirmed: Ch. 6 "Parton model to parton theory: simple model
  theories"; Ch. 7 "Parton theory: further developments" (§7.5 "Parton densities in gauge theories"); Ch. 8 "Factorization for DIS, mostly in
  simple field theories"; Ch. 9 "Corrections to the parton model in QCD". Finer section and equation numbers not checked.
* M.E. Peskin, D.V. Schroeder, *An Introduction to Quantum Field Theory* (1995). Chapter structure confirmed (Ch. 16 quantization of
  non-abelian gauge theories, Ch. 17 QCD, Ch. 18 "Operator Products and Effective Vertices"). Section and equation numbers not checked.

Standard references cited from memory (bibliographic data believed correct, not re-checked online):
* J.C. Collins, D.E. Soper, "Parton distribution and decay functions", Nucl. Phys. **B194** (1982) 445.
* G. Altarelli, G. Parisi, Nucl. Phys. **B126** (1977) 298. V.N. Gribov, L.N. Lipatov, Sov. J. Nucl. Phys. **15** (1972) 438. Yu.L. Dokshitzer,
  Sov. Phys. JETP **46** (1977) 641.
* D.J. Gross, F. Wilczek, Phys. Rev. D **8** (1973) 3633; Phys. Rev. D **9** (1974) 980. H. Georgi, H.D. Politzer, Phys. Rev. D **9** (1974) 416.
* G. Curci, W. Furmanski, R. Petronzio, Nucl. Phys. **B175** (1980) 27.
* S. Catani, M.H. Seymour, Nucl. Phys. **B485** (1997) 291 (D-dimensional kernels).
* R.K. Ellis, W.J. Stirling, B.R. Webber, *QCD and Collider Physics*, CUP (1996), Ch. 4 (form of $\gamma^{(0)}_{ij}$; chapter from memory).
* R.L. Jaffe, Nucl. Phys. **B229** (1983) 205 (support of parton distributions).
* S.D. Joglekar, B.W. Lee, Ann. Phys. **97** (1976) 160 (renormalization of gauge-invariant operators).

---------------------------------------------------------------------------------------------------

## 10. Files

* `DERIVATION.md` (this file).
* `run_all.sh`; `logs/SUMMARY.txt` and `logs/s*.log`.
* `scripts/lorentz_engine.py`, `scripts/fourd.py`, `scripts/s1_free_field.py`, `scripts/s2_oneloop_qq.py`, `scripts/s3_splitting.py`,
  `scripts/s4_moments_local.py`, `scripts/s5_anomalous_dims.py`, `scripts/s5b_gauge_independence.py`, `scripts/s6_uniqueness.py`.
* `tex/` — LaTeX snippets (Chinese, monograph macros), self-contained, each one `\input`-able:
  `c_pdf_definitions.tex` (§2), `c_pdf_oneloop.tex` (§3, with TikZ cut diagrams), `c_pdf_splitting.tex` (§4),
  `c_pdf_moments.tex` (§5), `c_pdf_anomdim.tex` (§6), `c_pdf_uniqueness.tex` (§7); `test_c_pdf.tex` is the driver
  (copy `../../common/preamble_fact.tex` into `tex/` and run `xelatex test_c_pdf.tex` twice). Built here: `tex/test_c_pdf.pdf`
  (9 pages), no errors and no undefined references; two harmless overfull lines (< 4 pt) remain. The pages, including the TikZ
  cut diagrams R1/R2/V1/V2, were rendered and inspected.
