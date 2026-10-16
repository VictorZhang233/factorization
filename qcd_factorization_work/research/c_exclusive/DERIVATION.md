# research/c_exclusive — hard exclusive processes: DAs, ERBL, pion form factors, GPDs, DVCS, meson production

Directory: `/Users/hao-cheng/Desktop/theorem proof/qcd_factorization_work/research/c_exclusive`
(quote the path: it contains a space).

Everything below was derived by hand and then verified by the scripts in `scripts/` (sympy with explicit
4×4 Dirac matrices for all traces; exact residues and sympy integrals for the loop/convolution
integrals; mpmath/numpy for finite-$i0$ and quadrature cross-checks). `sh run_all.sh` re-runs all of
them (about 50 s) and writes `logs/*.log` and `logs/SUMMARY.txt`.

| script | content | checks |
|---|---|---|
| `s1_da.py` | Dirac/ε conventions, leading-twist Fierz projector, pion projector, DA Fourier conventions, Gegenbauer machinery, moments, $f_\pi$ from $\pi\to\mu\nu$ | 32/32 PASS |
| `s2_erbl_kernel.py` | one-loop ERBL kernel from the four Feynman-gauge graphs (Wilson-line vertex, Dirac numerators, exact $k^-$ residues + finite-$i0$ numerics, plus prescription, current conservation; virtual = −∫real at integrand level) | 17/17 PASS |
| `s3_erbl_eigen.py` | exact Gegenbauer eigenvalues ($n\le10$), triangularity, anomalous dimensions, DGLAP comparison, literature exponents, numerical plus-prescription and evolution-normalization checks, moment-space triangularity | 21/21 PASS |
| `s4_pion_ff.py` | LO pion form factor: four graphs, current conservation, $T_H$, sign, convolution, asymptotic limit, general $N_c$, Gegenbauer/CZ, endpoint analysis (exact soft fractions $R_{\rm as}$, $R_{\rm CZ}$) | 20/20 PASS |
| `s5_tff.py` | LO $\gamma^*\gamma^{(*)}\to\pi^0$: tensor structure, $Q^2F\to\sqrt2f_\pi$, general virtualities, symmetric point, width/anomaly normalization, BL interpolation | 17/17 PASS |
| `s6_gpd.py` | GPD kinematics ($\xi$, $t$, $t_0$, $x_B$), forward limits with explicit nucleon spinors, Gordon identity, polynomiality in a closed-form double-distribution model with a D-term | 16/16 PASS |
| `s7_dvcs.py` | LO handbag (doubly-virtual Compton): coefficient functions, $i0$ from the propagators, C-parity, DIS limit $\operatorname{Im}T=2\pi W$ with the binding $F_1$, DVCS $\operatorname{Im}/\operatorname{Re}$ of the CFF | 17/17 PASS |
| `s8_meson.py` | LO $\gamma^*_L N\to MN'$ (quark exchange) for $\pi$ (via $\tilde H,\tilde E$) and $\rho_L$ (via $H,E$); parity and C-parity selection (C-parity from the computed amplitudes), transverse-photon decoupling, Mankiewicz–Piller twist-3 integrals (WW), $1/Q$ scaling | 11/11 PASS |

Total: **151/151 PASS** (re-run 2026-10-10, ≈50 s). LaTeX snippets (Chinese, monograph macros, TikZ/pgfplots figures) are in `tex/`;
`tex/test_c_exclusive.tex` compiles them with the common preamble (see §11).

**Resume pass (2026-10-10).** After an interruption the work was resumed: all scripts were re-run; every script was audited and the
key factors re-derived by hand (ERBL prefactor $ig^2C_F$ and $\ell^-$ residue; $F_\pi$ reordering sign, projectors, colour; TFF Wick
contractions and anomaly normalization; $\operatorname{Im}T=2\pi W$ from the $T$-product definitions; meson-production $i0$'s and constant).
Changes: a tautological check in `s8` was replaced by a genuine one (C-parity from the computed amplitudes); `s4` gained the exact CZ soft
fraction; two rigor fixes in `tex/c_exclusive_da_erbl.tex`; the DVCS proof sketch and the transverse-photon remark were corrected
(§8, §10 items 10–12); a quantitative endpoint figure (`fig:cex-endpoint`) was added. The literature equations marked *(read)* below were
**re-read from the arXiv v1 PDFs in this pass**: Ji PRL eqs. (12)–(19); VGG eqs. (38), (63), (65); BKM eqs. (139)–(151); BaBar eq. (2);
Belle 2012 abstract; Mankiewicz–Piller full text; DGP 1999, Collins–Diehl 2000, Collins–Freund 1999, Ji–Osborne 1998 abstracts.

---------------------------------------------------------------------------------------------------

## 0. Results at a glance, with literature cross-checks

"PASS" = my independently derived result equals the literature value after the stated conversion of
conventions. For the items marked *(read)* I read the equation in the source myself during this work
(arXiv versions); the others rest on standard values whose consistency I checked but whose original
I could not open (marked *(recall)*).

| # | result (this work) | literature | conversion | status |
|---|---|---|---|---|
| 1 | DA: $\langle0|\bar d(z)\gamma^+\gamma_5W[z,-z]u(-z)|\pi^+(p)\rangle=if_\pi p^+\!\int_0^1\!dx\,e^{i(2x-1)p^+z^-}\phi_\pi(x)$, $x$ = $u$-quark fraction, $\int\phi=1$, $f_\pi\approx130$ MeV | Braun–Korchemsky–Müller 2003, eq. (140): $\langle0|\bar d(0)[0,\alpha]\gamma_+\gamma_5u(\alpha)|\pi^+\rangle=if_\pi p_+\int du\,e^{-iu\alpha p_+}\phi_\pi(u)$; "$f_\pi\simeq132$ MeV" (stated below their eq. 139) *(read)* | translation by $-\alpha$, $w=-\alpha$: $e^{ip\alpha}e^{-iu\alpha p}=e^{-i\bar u p w}$ = my asymmetric form (s1) | PASS |
| 2 | $f_\pi$ normalization: tree level from $\Gamma(\pi\to\mu\nu)$ gives 131.7 MeV | PDG-type value ≈130 MeV; BaBar 2009 uses 0.131 GeV; VGG 1999 uses $f_\pi=92.4$ MeV $=f_\pi^{(130)}/\sqrt2$ *(read)* | $F_\pi=f_\pi/\sqrt2$ | PASS |
| 3 | LO ERBL kernel $V_0(x,y)=C_F\big[\tfrac xy(1+\tfrac1{y-x})\theta(y-x)+\tfrac{\bar x}{\bar y}(1+\tfrac1{x-y})\theta(x-y)\big]_+$ with $\mu^2\partial_{\mu^2}\phi=\tfrac{\alpha_s}{2\pi}V_0\otimes\phi$ | BKM 2003, eqs. (141)–(143), identical (their $u,v$ = my $x,y$) *(read)* | none | PASS |
| 4 | $\gamma_n\equiv-\,(4\pi/\alpha_s)\,\mu\,d\ln a_n/d\mu=2C_F\big[1-\tfrac2{(n+1)(n+2)}+4\sum_{j=2}^{n+1}\tfrac1j\big]$; $\gamma_0=0$, $\gamma_2=\tfrac{25}3C_F$ | BKM 2003, eqs. (146)–(147): $\gamma_n^{(0)}=C_F[\dots]$, $a_n\propto\alpha_s^{\gamma^{(0)}_n/\beta_0}$ *(read)*; Lepage–Brodsky form $(C_F/\beta_0)[\dots]$ *(recall)* | $\gamma_n^{(0)}{}^{\rm BKM}=\gamma_n/2$; exponent $\gamma_n/(2\beta_0)$ in both | PASS ($n=0$: 0; $n=2$: exponent $50/81$ at $n_f=3$) |
| 5 | ERBL eigenvalues = DGLAP non-singlet moments at $N=n+1$ | BKM 2003 statement below eq. (145) *(read)*; c_pdf agent's $P_{qq}$ | — | PASS |
| 6 | $T_H=\dfrac{2\pi C_F\alpha_s f_\pi^2}{N_cQ^2}\Big[\dfrac{e_u}{\bar x\bar y}+\dfrac{e_{\bar d}}{xy}\Big]$, $Q^2F_\pi\to8\pi\alpha_sf_\pi^2$ ($f_\pi\simeq130$ MeV) | VGG 1999 eq. (65): $F_\pi^{\rm as}=16\pi\alpha_sf_\pi^2/Q^2$ with $f_\pi=0.0924$ GeV *(read)*; Lepage–Brodsky 1979/80 $16\pi\alpha_sf_\pi^2$ ($f_\pi\simeq93$ MeV) *(recall)* | $f^{(130)}=\sqrt2f^{(93)}$ | PASS |
| 7 | $Q^2F_{\gamma^*\gamma\pi}=\frac{\sqrt2f_\pi}3\int_0^1\!dx\,\phi_\pi(x)/x\to\sqrt2f_\pi$ | BaBar 2009 eq. (2), identical, $f_\pi=0.131$ GeV *(read)*; Brodsky–Lepage 1981 limit $2f_\pi$ ($f_\pi\simeq93$ MeV) *(recall)* | none | PASS |
| 8 | DVCS: $T^{\mu\nu}=+g_\perp^{\mu\nu}\sum e_q^2\!\int dx\,F^q\big[\tfrac1{x-\xi+i0}+\tfrac1{x+\xi-i0}\big]-i\epsilon_\perp^{\mu\nu}\sum e_q^2\!\int dx\,\tilde F^q\big[\tfrac1{x-\xi+i0}-\tfrac1{x+\xi-i0}\big]$ | Ji, PRL 78 (1997) 610, eq. (15) (arXiv v1) *(read)*: same, with $\xi_{\rm Ji}=2\xi$ | $\xi_{\rm Ji}/2=\xi$; Ji's second denominator printed "$x+\xi/2+i\epsilon$" (see §10) | PASS (vector part: sign and normalization; axial part if Ji's $\epsilon^{0123}=+1$) |
| 9 | same | VGG 1999 eq. (38) *(read)*, $\varepsilon_{0123}=+1$ | VGG's $H^{\mu\nu}=-T^{\mu\nu}$ (common overall sign of the tensor definition), $\epsilon$ sign flip | PASS (both terms) |
| 10 | DIS limit of the same kernel: $\operatorname{Im}T^{11}=2\pi F_1$, $F_1=\frac12\sum e_q^2(q+\bar q)$ | binding conventions (CONTEXT.md; c_dis) | — | PASS (numerical, finite $i0$) |
| 11 | $\varepsilon_L\!\cdot\!A_\pi=-i\frac{C_F}{N_c}\frac{4\pi\alpha_sf_\pi}{Q}\int dz\,\phi_\pi(z)\int dx\big[\frac{e_a}{\bar z(x-\xi+i0)}+\frac{e_b}{z(x+\xi-i0)}\big]\tilde F^{ba}$ | VGG 1999 eqs. (48), (59) *(read)*: $-ie\frac49\frac1Q[\int dz\frac{\Phi_\pi}z]\frac12\int dx[\dots](4\pi\alpha_s)\{\dots\}$ | $\Phi=f_\pi^{(130)}\phi$, $\frac12\{\tilde H\bar N\gamma\!\cdot\!n\gamma_5N+\dots\}=\tilde F$; VGG's charged-meson phase ($|\rho^+\rangle=-|u\bar d\rangle$) | PASS (factor $4/9=C_F/N_c$, $1/Q$, kernel and charges; even the phase $-i$ for $\pi^0$) |
| 12 | Polynomiality, $\int H=F_1$, $\int xH=A+4\xi^2C$, $\int x(H+E)=A+B$, $J^q=\frac12[A^q(0)+B^q(0)]$ | Ji PRL 1997 eqs. (12), (13), (17)–(19) *(read)* | $\xi_{\rm Ji}=2\xi$ | PASS (model check + Gordon identity) |

---------------------------------------------------------------------------------------------------

## 1. Conventions (binding ones from CONTEXT.md, plus the ones fixed here)

Binding: metric $(+,-,-,-)$; $v^\pm=(v^0\pm v^3)/\sqrt2$; $D_\mu=\partial_\mu-igA_\mu^at^a$ (vertex $+ig\gamma^\mu t^a$);
quark propagator $i\slashed k/(k^2+i0)$, gluon $-ig_{\mu\nu}\delta^{ab}/(k^2+i0)$ (Feynman gauge);
$W[b,a]=P\exp(ig\int_a^b dz\cdot A)$ with points nearer $b$ to the left, $W\to U(b)WU^\dagger(a)$;
$\mu^2d\alpha_s/d\mu^2=-\beta_0\alpha_s^2/(4\pi)$, $\beta_0=\frac{11}3C_A-\frac43T_Fn_f$.

**Fixed here (not in CONTEXT.md; needed for the transition form factor, $\tilde H$ and the axial DVCS term):**
$\gamma_5=i\gamma^0\gamma^1\gamma^2\gamma^3$, $\epsilon^{0123}=+1$ ⇒ $\operatorname{Tr}(\gamma^\mu\gamma^\nu\gamma^\rho\gamma^\sigma\gamma_5)=-4i\epsilon^{\mu\nu\rho\sigma}$
(s1, all 256 index sets). Light-like vectors $\bar n=(1,0,0,1)/\sqrt2$ (so $\bar n\cdot v=v^-$) and
$n=(1,0,0,-1)/\sqrt2$ ($n\cdot v=v^+$, $\slashed n=\gamma^+$);
$g_\perp^{\mu\nu}=g^{\mu\nu}-\bar n^\mu n^\nu-n^\mu\bar n^\nu$, $\epsilon_\perp^{\mu\nu}\equiv\epsilon^{\mu\nu\rho\sigma}\bar n_\rho n_\sigma$, so $\epsilon_\perp^{12}=+1$ (s7).
Note VGG 1999 use $\varepsilon_{0123}=+1$, i.e. the opposite sign.

**Collinear projectors and Fierz identity (s1).** For a quark moving along $+z$, $\slashed k u=k^+\gamma^-u=0$:
$P_u=\frac12\gamma^-\gamma^+$, $P_v=\frac12\gamma^+\gamma^-$ ($\gamma^-P_u=0$, $P_v\gamma^-=0$) and for any $4\times4$ matrix $M$
$$P_uMP_v=\tfrac14\Big[\operatorname{Tr}(\gamma^+M)\gamma^-+\operatorname{Tr}(\gamma^+\gamma_5M)\gamma_5\gamma^-+\textstyle\sum_{j=1,2}\operatorname{Tr}(\gamma^+\gamma^jM)\gamma^-\gamma^j\Big].$$
This is the leading-twist decomposition used for all DA and GPD projectors below.

**Leading-region rule for amplitudes.** In the tree-level hard part the parton momenta are replaced by
their collinear projections ($k\to xp$), and the soft/collinear matrix element of the two fields is
replaced by its leading-twist Fierz projection. For a meson in the initial (final) state:
$$\langle0|\bar d_\beta(z)u_\alpha(0)|\pi^+(p)\rangle\to\tfrac{if_\pi}4(\gamma_5\slashed p)_{\alpha\beta}\tfrac{\delta_{ij}}{N_c}\!\int_0^1\!dx\,e^{-i\bar xp\cdot z}\phi_\pi(x),\qquad
\langle\pi^+(p)|\bar u_\alpha(0)d_\beta(z)|0\rangle\to\tfrac{if_\pi^*}4(\slashed p\gamma_5)_{\beta\alpha}\tfrac{\delta_{ij}}{N_c}\!\int_0^1\!dy\,e^{i\bar yp\cdot z}\phi_\pi^*(y),$$
checked: $\operatorname{Tr}[\gamma^\mu\gamma_5\,\tfrac{if}4\gamma_5\slashed p]=ifp^\mu$; the second follows from the first by
$C=\gamma^0A^\dagger\gamma^0$ (s1). When the two quark lines of a graph are joined through the two
projectors, reordering $\bar u_cu_a\bar d_bd_d=-(\bar u_cd_d)(\bar d_bu_a)$ gives an overall factor $-1$.

---------------------------------------------------------------------------------------------------

## 2. Item (1a): the pion distribution amplitude

### 2.1 Definition (light-like Wilson line), normalization, dictionary

For light-like $z=(0^+,z^-,\mathbf 0_T)$ and the pion moving along $+z$:
$$\boxed{\;\langle0|\,\bar d(z)\,\gamma^+\gamma_5\,W[z,-z]\,u(-z)\,|\pi^+(p)\rangle=if_\pi\,p^+\!\int_0^1\!dx\;e^{\,i(2x-1)\,p^+z^-}\,\phi_\pi(x;\mu)\;}$$
- $W[z,-z]=P\exp\big(ig\int_{-z^-}^{z^-}dw^-A^+(0^+,w^-,\mathbf 0_T)\big)$; gauge invariance:
  $\bar d(z)\to\bar d(z)U^\dagger(z)$, $W\to U(z)WU^\dagger(-z)$, $u(-z)\to U(-z)u(-z)$. In $A^+=0$ gauge $W=1$.
- $x$ is the light-front momentum fraction of the **$u$ quark** (the field at $-z$): a free $|u(x_0p)\bar d(\bar x_0p)\rangle$ gives
  the phase $e^{-ix_0p\cdot(-z)}e^{-i\bar x_0p\cdot z}=e^{i(2x_0-1)p\cdot z}$, i.e. $\phi=\delta(x-x_0)$ (s1). This fixes the sign of
  the exponent asked for in blueprint D13.1: it is $+i(2x-1)P^+z^-$ as written there.
- Asymmetric form (by translation invariance): $\langle0|\bar d(w)\gamma^+\gamma_5W[w,0]u(0)|\pi^+\rangle=if_\pi p^+\int dx\,e^{-i\bar xp^+w^-}\phi_\pi(x)$,
  which is BKM eq. (140) translated by $-\alpha$: their $u$ = my $x$ (quark fraction), their $\alpha=-w$ (*(read)*, matches).
- Inversion: $\phi_\pi(x;\mu)=\frac1{if_\pi}\int\frac{dw^-}{2\pi}e^{i\bar xp^+w^-}\langle0|\bar d(w)\gamma^+\gamma_5W[w,0]u(0)|\pi^+(p)\rangle
  =\frac1{i\pi f_\pi}\int dz^-e^{-i(2x-1)p^+z^-}\langle0|\bar d(z)\gamma^+\gamma_5W[z,-z]u(-z)|\pi^+(p)\rangle$ (s1, numerical check of the $\delta$-function identity).
- Support $0\le x\le1$ (as for PDFs: in light-front quantization both partons must carry positive plus momentum);
  $\phi_\pi(x)=\phi_\pi(1-x)$ by charge conjugation × isospin ($G$-parity), so only even Gegenbauer moments occur.
- The bilocal operator is UV divergent; $\phi_\pi(x;\mu)$ is the $\overline{\rm MS}$-renormalized matrix element. Lepage–Brodsky's
  interpretation $\phi\propto\int^{\mu^2}d^2k_T\,\psi_{q\bar q}(x,\mathbf k_T)$ (light-cone gauge, $k_T$ cutoff) is a leading-log statement, not an identity in $\overline{\rm MS}$.

**Normalization.** The local limit $z\to0$ gives $\langle0|\bar d\gamma^\mu\gamma_5u|\pi^+(p)\rangle=if_\pi p^\mu\int_0^1\phi$, so
$\int_0^1dx\,\phi_\pi(x;\mu)=1$ for all $\mu$ (the axial current is conserved ⇒ not renormalized, cf. $\gamma_0=0$ below).
**$f_\pi$ convention: $f_\pi\approx130$ MeV** (the decay constant in $\langle0|A^\mu|\pi\rangle=if_\pi p^\mu$ with $A^\mu=\bar d\gamma^\mu\gamma_5u$).
Check: the tree-level rate $\Gamma(\pi\to\mu\nu)=G_F^2|V_{ud}|^2f_\pi^2m_\pi m_\mu^2(1-m_\mu^2/m_\pi^2)^2/(8\pi)$ with
$\tau_\pi=26.033$ ns, BR $=0.999877$, $|V_{ud}|=0.97373$ gives $f_\pi=131.7$ MeV (s1); radiative corrections (not computed here)
lower this by about 1%, to the quoted ≈130 MeV. Dictionary: $F_\pi\equiv f_\pi/\sqrt2\approx92$–$93$ MeV (chiral perturbation theory;
Lepage–Brodsky; VGG); the Lepage–Brodsky DA is $\phi_{\rm LB}(x)=\frac{f_\pi}{2\sqrt{2N_c}}\phi_\pi(x)=\frac{F_\pi}{2\sqrt{N_c}}\phi_\pi(x)$,
$\int\phi_{\rm LB}=F_\pi/(2\sqrt{N_c})$ *(recall for LB's normalization)*. The phase of $|\pi^+\rangle$ is chosen so that $f_\pi>0$.

### 2.2 Moments and local operators

Expanding $\bar d(z)\Gamma u(-z)=\sum_n\frac1{n!}\bar d[z\cdot(\overleftarrow\partial-\overrightarrow\partial)]^n\Gamma u$ and comparing powers of $p\cdot z$:
$$\langle0|\bar d\gamma^+\gamma_5(i\overleftrightarrow D^+)^nu|\pi^+(p)\rangle=if_\pi(p^+)^{n+1}\langle\xi^n\rangle,\quad \overleftrightarrow D=\overrightarrow D-\overleftarrow D,\quad \langle\xi^n\rangle=\int_0^1dx\,(2x-1)^n\phi_\pi(x)$$
(BKM eq. 144 *(read)*, identical). Closed form: $\int_0^1dx\,e^{i(2x-1)\lambda}6x\bar x=3(\sin\lambda-\lambda\cos\lambda)/\lambda^3$.
$\langle\xi^2\rangle=\frac15(1+\frac{12}7a_2)$, $\langle\xi^4\rangle=\frac3{35}+\frac8{35}a_2+\frac8{77}a_4$ (s1).

### 2.3 Gegenbauer expansion

$$\phi_\pi(x;\mu)=6x\bar x\sum_{n=0}^\infty a_n(\mu)\,C_n^{3/2}(2x-1),\quad a_0=1,\quad a_n=\frac{2(2n+3)}{3(n+1)(n+2)}\int_0^1dx\,C_n^{3/2}(2x-1)\phi_\pi(x),$$
$$\int_0^1dx\,x\bar x\,C^{3/2}_n(2x-1)C^{3/2}_m(2x-1)=\delta_{nm}\frac{(n+1)(n+2)}{4(2n+3)}\quad(\text{BKM eq. 150, \emph{read}}).$$
Useful: $C_n^{3/2}(\xi)=P'_{n+1}(\xi)$, $C_n^{3/2}(1)=\frac{(n+1)(n+2)}2$, hence
$\int_0^1\frac{\phi}{x}=3\sum_n(-1)^na_n$, $\int_0^1\frac{\phi}{\bar x}=3\sum_na_n$ (s1, $n\le12$).
Chernyak–Zhitnitsky DA: $30x\bar x(2x-1)^2=6x\bar x[1+\frac23C_2^{3/2}(2x-1)]$ ⇒ $a_2=\frac23$, $\int\phi_{\rm CZ}/x=5$.

---------------------------------------------------------------------------------------------------

## 3. Item (1b): ERBL evolution at one loop — derivation and anomalous dimensions

### 3.1 Set-up

Partonic matrix element ($p^+\equiv1$, external partons exactly collinear and on shell, $k_1=yp$, $k_2=\bar yp$):
$\Phi(x;y)\equiv\int\frac{dw^-}{2\pi}e^{i\bar xw^-}\langle0|\bar d(w)\gamma^+\gamma_5W[w,0]u(0)|u(k_1)\bar d(k_2)\rangle
=\bar v(k_2)\gamma^+\gamma_5u(k_1)\,[\delta(x-y)+\Phi^{(1)}(x;y)+\dots]$. Operator vertices in momentum-fraction space
($k$ = momentum of the $u$ line entering the vertex at $0$, $\ell$ = gluon momentum absorbed by the Wilson line):
- no gluon: $\Gamma\,\delta(x-k^+)$, $\Gamma=\gamma^+\gamma_5$;
- one gluon (colour $a$, index $\mu$): $\dfrac{g\,t^a n^\mu}{\ell^+}\big[\delta(x-k^+-\ell^+)-\delta(x-k^+)\big]\Gamma$,
  from $\int_0^1ds\,w^-e^{i(c-s\ell^+)w^-}=\frac i{\ell^+}[e^{i(c-\ell^+)w^-}-e^{icw^-}]$ (s2). It is regular at $\ell^+=0$ (no $i0$ needed).

After the $k^-$ integral every graph is $\frac{\alpha_s}{2\pi}V_{\rm graph}(x,y)\int\frac{dk_T^2}{k_T^2}$ — a pure logarithm (in DR,
$1/\epsilon_{\rm UV}-1/\epsilon_{\rm IR}$). The $\overline{\rm MS}$ counterterm removes the UV pole, so
$\mu^2\frac{d}{d\mu^2}\Phi(x;y)=\frac{\alpha_s}{2\pi}V(x,y)$ and, by the factorization of the pion matrix element into partonic ones,
$$\boxed{\;\mu^2\frac{d}{d\mu^2}\phi_\pi(x;\mu)=\frac{\alpha_s(\mu)}{2\pi}\int_0^1dy\,V_0(x,y)\,\phi_\pi(y;\mu)\;}$$

### 3.2 The graphs (Feynman gauge)

(a) **Gluon exchange between the quark and antiquark legs.** $M_a=ig^2C_F\!\int\!\frac{d^4k}{(2\pi)^4}\delta(x-k^+)
\frac{\bar v\,\gamma^\alpha(\slashed p-\slashed k)\Gamma\slashed k\gamma_\alpha u}{[(p-k)^2+i0][k^2+i0][(k_1-k)^2+i0]}$.
Between the collinear spinors $P_v\gamma^\alpha(\slashed p-\slashed k)\Gamma\slashed k\gamma_\alpha P_u=2|\mathbf k_T|^2P_v\Gamma P_u$ —
independent of $k^-$ (s2, matrix identity). With $D_1=2xk^--k_T^2$, $D_2=-2(1-x)k^--k_T^2$, $D_3=-2(y-x)k^--k_T^2$:
$$\int dk^-\frac1{D_1D_2D_3}=-\frac{i\pi}{k_T^4}\Big[\frac xy\theta(y-x)+\frac{\bar x}{\bar y}\theta(x-y)\Big]\theta(x)\theta(1-x)$$
(exact residues and direct numerical integration at finite $i0$, s2). Hence $V_a=C_F\big[\frac xy\theta(y-x)+\frac{\bar x}{\bar y}\theta(x-y)\big]$.

(b) **Wilson line – quark leg.** Numerator: $\Gamma\,\slashed n\,(\slashed k_1-\slashed\ell)\gamma^\nu\to\gamma^+\gamma_5(\slashed k_1-\slashed\ell)\gamma^+=2(y-\ell^+)\gamma^+\gamma_5$
(exact). $\int d\ell^-\frac1{[(k_1-\ell)^2+i0][\ell^2+i0]}=\frac{i\pi}{y\,\ell_T^2}\theta(\ell^+)\theta(y-\ell^+)$. The term $-\delta(x-y+\ell^+)$
(real emission into the Wilson line) gives $V_b^{\rm real}=C_F\frac{x}{y(y-x)}\theta(y-x)\theta(x)$; the term $+\delta(x-y)$ gives
exactly $-\delta(x-y)\int_0^ydt\,V_b^{\rm real}(t,y)$ (checked at integrand level, s2). So
$V_b=C_F\big[\frac{x}{y(y-x)}\theta(y-x)\big]_+$, where $[V]_+(x,y)=V(x,y)-\delta(x-y)\int_0^1dt\,V(t,y)$.

(c) **Wilson line – antiquark leg.** Numerator $\gamma^+(\slashed k_2-\slashed\ell)\gamma^+\gamma_5=2(\bar y-\ell^+)\gamma^+\gamma_5$; by the same steps
$V_c=C_F\big[\frac{\bar x}{\bar y(x-y)}\theta(x-y)\big]_+$ (s2).

(d) **External self-energies.** $(Z_2-1)\delta(x-y)=-\frac{\alpha_s}{4\pi}C_F(\frac1{\epsilon_{\rm UV}}-\frac1{\epsilon_{\rm IR}})\delta(x-y)$ in Feynman gauge,
i.e. $V_d=-\frac12C_F\delta(x-y)$.  (e) The Wilson-line self-energy is $\propto n^2=0$.

Since $\int_0^1dx\,V_a(x,y)=\frac y2+\frac{1-y}2=\frac12$, (a)+(d) is the plus distribution of (a), and
$$\boxed{\;V_0(x,y)=C_F\Big[\frac xy\Big(1+\frac1{y-x}\Big)\theta(y-x)+\frac{\bar x}{\bar y}\Big(1+\frac1{x-y}\Big)\theta(x-y)\Big]_+\;}$$
identical to BKM eq. (142) *(read)*. Independent check of (d): conservation of the local axial current, $\int dx\,V_0(x,y)=0$,
*requires* the $\delta$-coefficient $-\frac12C_F$, i.e. $\delta Z_2=-\alpha_sC_F/(4\pi\epsilon)$ (s2). Action on a test function:
$$(V_0\otimes\phi)(x)=C_F\Big\{\int_x^1\!dy\Big(1+\frac1{y-x}\Big)\Big[\frac xy\phi(y)-\frac{\bar y}{\bar x}\phi(x)\Big]+\int_0^x\!dy\Big(1+\frac1{x-y}\Big)\Big[\frac{\bar x}{\bar y}\phi(y)-\frac yx\phi(x)\Big]\Big\}.$$

### 3.3 Eigenfunctions: a proof for all $n$

(i) *Hermiticity:* $V_0(x,y)\,y\bar y=V_0(y,x)\,x\bar x$ (s2), i.e. $V_0$ is self-adjoint w.r.t. $\langle f,g\rangle=\int_0^1\frac{f g}{x\bar x}dx$ on functions $x\bar x\,P(x)$.
(ii) *Triangularity:* $V_0$ maps $x\bar x\cdot\mathcal P_k$ into $x\bar x\cdot\mathcal P_k$ ($\mathcal P_k$ = polynomials of degree $\le k$).
General argument: by (i), exactly (plus prescription included), $V_0\otimes(y\bar y\,P)=x\bar x\,(V_0^{\sf T}P)$ with
$(V_0^{\sf T}P)(x)=\int_0^1dy\,V_0(y,x)[P(y)-P(x)]$, and $V_0^{\sf T}$ maps $\mathcal P_k$ into itself because the $k$-th moment of $V_0\otimes\phi$
involves only moments $\le k$ of $\phi$ (the one-loop counterterm of a local operator with $k$ factors $D^+$ contains only operators with
$k$ factors $D^+$/$\partial^+$ — boost weight). (A naive degree count region by region gives degree $k+1$; the top terms cancel
between $y<x$ and $y>x$.) Checks (s3): $V_0(x\bar x\mathcal P_k)\subset x\bar x\mathcal P_k$ for $k\le8$; $V_0^{\sf T}\mathcal P_n\subset\mathcal P_n$ for $n\le10$;
the identity $V_0\otimes(y\bar yP)=x\bar x\,V_0^{\sf T}P$ for test polynomials.
A self-adjoint operator preserving a flag of finite-dimensional subspaces is diagonal in the orthogonal basis adapted to the flag,
here the orthogonal polynomials for the weight $x\bar x$ on $[0,1]$: $C_n^{3/2}(2x-1)$. Exact eigenvalues (s3, $n=0..10$):
$$\int_0^1dy\,V_0(x,y)\,y\bar yC_n^{3/2}(2y-1)=v_n\,x\bar xC_n^{3/2}(2x-1),\qquad v_n=C_F\Big[-\frac12+\frac1{(n+1)(n+2)}-2\sum_{j=2}^{n+1}\frac1j\Big]=\int_0^1\!dz\,z^n P_{qq}(z),$$
$P_{qq}=C_F[\frac{1+z^2}{1-z}]_+$ (equality of ERBL eigenvalues with DGLAP moments at $N=n+1$: s3; it reflects that the diagonal
elements of the triangular mixing of $\bar d\gamma^+\gamma_5(i\overleftrightarrow D^+)^{n-k}(i\partial^+)^ku$ are the forward anomalous dimensions).

### 3.4 Anomalous dimensions and solution

$$\mu\frac{da_n}{d\mu}=-\gamma_n\frac{\alpha_s}{4\pi}a_n,\qquad \boxed{\;\gamma_n=-4v_n=2C_F\Big[1-\frac2{(n+1)(n+2)}+4\sum_{j=2}^{n+1}\frac1j\Big]=8C_F\Big[\psi(n+2)+\gamma_E-\frac34-\frac1{2(n+1)(n+2)}\Big]\;}$$
$$a_n(\mu)=a_n(\mu_0)\Big[\frac{\alpha_s(\mu)}{\alpha_s(\mu_0)}\Big]^{\gamma_n/(2\beta_0)}\quad\text{(one-loop running)}.$$
Dictionary: BKM (and the blueprint) write $\gamma_n^{(0)}=C_F[\dots]=\gamma_n/2$ with exponent $\gamma^{(0)}_n/\beta_0$ — the same exponent.
Lepage–Brodsky: $(\ln Q^2/\Lambda^2)^{-\gamma_n^{\rm LB}}$, $\gamma_n^{\rm LB}=\frac{C_F}{\beta_0}[1+4\sum_{k=2}^{n+1}\frac1k-\frac2{(n+1)(n+2)}]=\gamma_n/(2\beta_0)$ (s3).
Checks: **$n=0$: $\gamma_0=0$** (conserved axial current). **$n=2$: $\gamma_2=\frac{25}3C_F=\frac{100}9$**, exponent $\frac{50}{81}$ ($n_f=3$), $\frac23$ ($n_f=4$), $\frac{50}{69}$ ($n_f=5$).
Normalization of the exponent checked against the kernel by finite differences (s3, $10^{-9}$).

| $n$ | 0 | 1 | 2 | 3 | 4 | 6 | 8 |
|---|---|---|---|---|---|---|---|
| $\gamma_n/C_F$ | 0 | 16/3 | 25/3 | 157/15 | 182/15 | 1027/70 | 1045/63 |
| exponent, $n_f=3$ | 0 | 32/81 | 50/81 | 314/405 | 364/405 | 1027/945 | 2090/1701 |

($n$ odd matters for the kaon.) $\gamma_n>0$ for $n\ge1$ and increasing; $\gamma_n=8C_F(\ln n+\gamma_E-\frac34)+O(1/n)$.
Hence $\phi_\pi(x;\mu)\to6x(1-x)$ as $\mu\to\infty$ (**asymptotic DA**). Rigor: LO kernel and solution **[R]** (perturbative,
complete derivation); the convergence of the Gegenbauer series pointwise near the endpoints for a given nonperturbative
$\phi(x;\mu_0)$ is an assumption about $\phi$, not a theorem (BKM make the same remark).

---------------------------------------------------------------------------------------------------

## 4. Item (2a): the LO hard kernel of the pion electromagnetic form factor

### 4.1 Definition and graphs

$\langle\pi^+(p')|J^\mu(0)|\pi^+(p)\rangle=(p+p')^\mu F_\pi(Q^2)$, $J^\mu=\sum_qe_q\bar q\gamma^\mu q$, $q=p'-p$, $Q^2=-q^2$, $F_\pi(0)=1$.
Breit frame, massless pions: $p=(P,0,\mathbf0_T)$, $p'=(0,P,\mathbf 0_T)$, $Q^2=2P^2$. Partons: $u(xp)\bar d(\bar xp)\to u(yp')\bar d(\bar yp')$.
At $O(\alpha_s)$ exactly **four** graphs (one gluon connecting the two lines; the photon on either line, on either side of the gluon vertex):

| graph | photon | internal quark | gluon | contribution (s4) |
|---|---|---|---|---|
| A | absorbed by incoming $u$, then gluon | $(xp+q)^2=-\bar xQ^2$ | $(\bar yp'-\bar xp)^2=-\bar x\bar yQ^2$ | $\mathcal T_u\,p^\mu$ |
| B | gluon first, then photon on $u$ | $(p-\bar yp')^2=-\bar yQ^2$ | $-\bar x\bar yQ^2$ | $\mathcal T_u\,p'^\mu$ |
| C | absorbed by incoming $\bar d$, then gluon | $(xp-p')^2=-xQ^2$ | $(xp-yp')^2=-xyQ^2$ | $\mathcal T_{\bar d}\,p^\mu$ |
| D | gluon first, then photon on $\bar d$ | $(yp'-p)^2=-yQ^2$ | $-xyQ^2$ | $\mathcal T_{\bar d}\,p'^\mu$ |

with $\mathcal T_u=\frac{C_Fg^2f_\pi^2}{2N_cQ^2}\frac{e_u}{\bar x\bar y}$, $\mathcal T_{\bar d}=\frac{C_Fg^2f_\pi^2}{2N_cQ^2}\frac{-e_d}{xy}$. Each graph alone violates current
conservation ($q\cdot p=-q\cdot p'=p\cdot p'$); A+B and C+D are separately conserved (s4). Factors: colour
$\operatorname{Tr}_c[t^a\frac{1}{N_c}t^a\frac1{N_c}]=C_F/N_c$; $g^2=4\pi\alpha_s$; $(\frac14)^2|f_\pi|^2$ from the projectors; Dirac traces (explicit matrices);
overall $(-1)$ from the fermion reordering (§1). The resulting sign is **positive**, as it must be (same sign as $F_\pi(0)=1$).

### 4.2 Result

$$\boxed{\;F_\pi(Q^2)=\int_0^1\!\!dx\,dy\;\phi_\pi^*(y;\mu)\,T_H(x,y)\,\phi_\pi(x;\mu),\qquad T_H=\frac{2\pi C_F\,\alpha_s(\mu)\,f_\pi^2}{N_c\,Q^2}\Big[\frac{e_u}{\bar x\bar y}+\frac{e_{\bar d}}{xy}\Big]\;}\quad(e_{\bar d}=-e_d=\tfrac13)$$
$$Q^2F_\pi=\frac{2\pi C_F\alpha_sf_\pi^2}{N_c}\Big[e_u\Big|\!\int\!\frac{\phi}{\bar x}\Big|^2+e_{\bar d}\Big|\!\int\!\frac{\phi}{x}\Big|^2\Big]\overset{N_c=3,\ \phi(x)=\phi(\bar x)}{=}\frac{8\pi\alpha_sf_\pi^2}{9}\Big|\int_0^1\!dx\frac{\phi_\pi(x)}{x}\Big|^2=8\pi\alpha_sf_\pi^2\,(1+a_2+a_4+\dots)^2.$$
Asymptotic DA: $\boxed{Q^2F_\pi\to8\pi\alpha_sf_\pi^2\ (f_\pi\simeq130\text{ MeV})\;\Leftrightarrow\;16\pi\alpha_sF_\pi^2\ (F_\pi\simeq93\text{ MeV})}$; general $N_c$:
$18\pi C_F\alpha_sf_\pi^2/N_c$. CZ DA: $\frac{25}9\times$ asymptotic. Numbers ($f_\pi=130.2$ MeV, $\alpha_s=0.3$): $0.128$ GeV² (asymptotic), $0.355$ GeV² (CZ).
Literature: VGG 1999 eq. (65) $F_\pi^{\rm as}=16\pi\alpha_sf_\pi^2/Q^2$, $f_\pi=92.4$ MeV *(read)* — PASS.
Rigor: the LO computation is exact; the factorization theorem (leading power, all orders) is **[A]**
(Lepage–Brodsky 1979/80; Efremov–Radyushkin 1980; Duncan–Mueller 1980; Farrar–Jackson 1979 for the asymptotic behaviour).
NLO hard kernel (blueprint T13.4 "(verify)" — all four verified on INSPIRE in this pass, not re-derived): Field, Gupta, Otto & Chang, NPB 186 (1981) 429;
Dittes & Radyushkin, Sov. J. Nucl. Phys. 34 (1981) 293 [Yad. Fiz. 34 (1981) 529]; Braaten & Tse, PRD 35 (1987) 2255; Melić, Nižić & Passek,
PRD 60 (1999) 074004 [hep-ph/9802204].

### 4.3 Endpoint behaviour

- *Convergence.* $T_H\propto1/(\bar x\bar y)$ (and $1/(xy)$): the convolution converges iff $\phi$ vanishes at the endpoints. For
  $\phi\propto(x\bar x)^a$ normalized: $\int\phi/x=(2a+1)/a$ — finite iff $a>0$, divergent like $1/a$ for a "flat" DA (s4). Any finite
  Gegenbauer sum has $a=1$; ERBL evolution drives $a_n\to0$.
- *Soft-gluon region (Isgur–Llewellyn Smith).* Fraction of the LO $u$-line integral with gluon virtuality $\bar x\bar yQ^2<\mu_0^2$
  ($c=\mu_0^2/Q^2\le1$; $u=\bar x$, $v=\bar y$; region $uv<c$), derived here (sympy exact, s4, analytic = numerical):
  $$\boxed{R_{\rm as}(c)=c\,[\,5c-2(c+2)\ln c-4\,],\qquad R_{\rm CZ}(c)=c\,[\,456c^3+352c^2-675c-132-(144c^3+768c^2+450c+36)\ln c\,]}$$
  ($R(1)=1$, monotonic; $c\to0$: $R_{\rm as}\simeq4c\ln(1/c)$, $R_{\rm CZ}\simeq36c\ln(1/c)$.)
  With $\mu_0^2=1$ GeV²: $Q^2=4$: 0.87; $Q^2=10$: 0.62; $Q^2=100$: 0.15 GeV² (CZ DA: 0.98, 0.90, 0.48). At accessible $Q^2$ most of
  the LO integral comes from gluon virtualities below 1 GeV², where perturbation theory is not reliable. Formally this is a
  power correction ($O(c\ln(1/c))$) only because $\phi\sim x$; numerically it dominates. Plotted in `fig:cex-endpoint` (tex).
- *Feynman (soft-overlap) mechanism.* With a soft spectator the overlap contribution is formally power suppressed relative to the
  hard $1/Q^2$ term (the commonly quoted scaling for the pion is $\propto1/Q^4$; **not derived here**). Isgur–Llewellyn Smith
  1984/1989 argued that it dominates at accessible $Q^2$.
- *Sudakov suppression.* Li–Sterman 1992 resum Sudakov logarithms in impact-parameter space, which suppresses the endpoint
  regions; status of this $k_T$-modified scheme: **[P]** (model-dependent intrinsic $k_T$; not a theorem of collinear factorization).

---------------------------------------------------------------------------------------------------

## 5. Item (2b): the $\gamma^*\gamma\to\pi^0$ transition form factor at LO

**Definition (normalization).** $T^{\mu\nu}\equiv\int d^4z\,e^{-iq_1\cdot z}\langle\pi^0(p)|T\{J^\mu(z)J^\nu(0)\}|0\rangle=-i\epsilon^{\mu\nu\alpha\beta}q_{1\alpha}q_{2\beta}F(Q_1^2,Q_2^2)$,
i.e. $\mathcal M(\gamma^*\gamma^*\to\pi^0)=e^2F\,\epsilon^{\mu\nu\alpha\beta}\varepsilon_{1\mu}\varepsilon_{2\nu}q_{1\alpha}q_{2\beta}$ and
$\Gamma(\pi^0\to\gamma\gamma)=\frac{\pi\alpha^2m_\pi^3}4|F(0,0)|^2$ (polarization sum $2(k_1\cdot k_2)^2=m^4/2$ and phase space, s5).
With the anomaly value $|F(0,0)|=1/(4\pi^2F_\pi)$: $\Gamma=\alpha^2m^3/(64\pi^3F_\pi^2)=7.76$ eV ($F_\pi=92.2$ MeV). Overall signs depend on
the phase of $|\pi^0\rangle$, the sign of $e$ and of $\epsilon^{0123}$; only $|F|$ is compared.

**Projector.** $\pi^0=(u\bar u-d\bar d)/\sqrt2$ with $\langle0|(\bar u\gamma^\mu\gamma_5u-\bar d\gamma^\mu\gamma_5d)/\sqrt2|\pi^0\rangle=if_\pi p^\mu$ (same $f_\pi$ as for $\pi^+$ by isospin);
flavour factor $(e_u^2-e_d^2)/\sqrt2=\sqrt2/6$; colour factor 1. Two graphs (photon 1 attached on the quark or the antiquark side).

**Result (s5, all 16 tensor components).**
$$\boxed{\;F(Q_1^2,Q_2^2)=\frac{\sqrt2f_\pi}{6}\int_0^1\!dy\,\phi_\pi(y)\Big[\frac1{\bar yQ_1^2+yQ_2^2}+\frac1{yQ_1^2+\bar yQ_2^2}\Big]\;}$$
Real photon: $\boxed{Q^2F(Q^2)=\frac{\sqrt2f_\pi}{3}\int_0^1dx\frac{\phi_\pi(x)}{x}=\sqrt2f_\pi(1+a_2+a_4+\dots)\to\sqrt2f_\pi=2F_\pi\approx0.184\text{ GeV}}$.
Symmetric point $Q_1^2=Q_2^2=Q^2$: $Q^2F=\sqrt2f_\pi/3$ for any normalized DA (computed in a transverse-momentum frame, s5).
Literature: BaBar 2009 eq. (2) $Q^2F=\frac{\sqrt2f_\pi}3\int_0^1\frac{dx}x\phi_\pi(x,Q^2)+O(\alpha_s)+O(\Lambda^2/Q^2)$, $f_\pi=0.131$ GeV *(read)* — **PASS**.
Brodsky–Lepage interpolation $F(0)/(1+Q^2/(8\pi^2F_\pi^2))$ with $F(0)=1/(4\pi^2F_\pi)$ has $Q^2F\to2F_\pi=\sqrt2f_\pi$ (s5) — consistent.
Data (qualitative): CELLO 0.7–2.2 GeV², CLEO 1.6–8 GeV², BaBar 4–40 GeV² (from the BaBar introduction *(read)*). Belle 2012 abstract *(read)*:
its values "agree well with the previous measurements below $Q^2\simeq9$ GeV²" and "do not exhibit the rapid growth in the higher $Q^2$
region seen in another recent measurement [BaBar 2009], which exceeds the asymptotic QCD expectation by as much as 50%".
NNLO: Gao, Huber, Ji, Wang 2022 (verified reference). Rigor: **[A]** (simplest exclusive process: one DA, no gluon at LO).

---------------------------------------------------------------------------------------------------

## 6. Item (3a): GPDs — definitions, kinematics, forward limits, polynomiality

### 6.1 Definitions (Ji's $H,E$ in the light-front normalization of Diehl 2003)
$$F^q=\frac12\!\int\!\frac{dz^-}{2\pi}e^{ix\bar P^+z^-}\langle p'|\bar q(-\tfrac z2)\gamma^+W[-\tfrac z2,\tfrac z2]q(\tfrac z2)|p\rangle\Big|_{z^+=0,\mathbf z_T=0}
=\frac1{2\bar P^+}\Big[H^q\,\bar u(p')\gamma^+u(p)+E^q\,\bar u(p')\frac{i\sigma^{+\alpha}\Delta_\alpha}{2M}u(p)\Big],$$
$$\tilde F^q=(\gamma^+\to\gamma^+\gamma_5)=\frac1{2\bar P^+}\Big[\tilde H^q\,\bar u(p')\gamma^+\gamma_5u(p)+\tilde E^q\,\frac{\Delta^+}{2M}\bar u(p')\gamma_5u(p)\Big],$$
$\bar P=\frac{p+p'}2$, $\Delta=p'-p$, $t=\Delta^2$, $\boxed{\xi=-\frac{\Delta^+}{2\bar P^+}=\frac{p^+-p'^+}{p^++p'^+}}$. Ji's covariant form
$\int\frac{d\lambda}{2\pi}e^{i\lambda x}\langle p'|\bar\psi(-\frac{\lambda n}2)\gamma^\mu\psi(\frac{\lambda n}2)|p\rangle=H\bar u\gamma^\mu u+E\bar u\frac{i\sigma^{\mu\nu}\Delta_\nu}{2M}u+\dots$ ($n\cdot\bar P=1$; PRL eq. 16 *(read)*)
defines the same $H,E$ (contract with $n_\mu$, $\lambda=\bar P^+z^-$). **Warning:** Ji 1997 uses $\xi_{\rm Ji}=Q^2/(2\bar P\cdot q)$ with $\Delta^+=-\xi_{\rm Ji}\bar P^+$,
i.e. $\xi_{\rm Ji}=2\xi$ (his poles sit at $x=\pm\xi_{\rm Ji}/2$) *(read)*. VGG 1999 use the modern $\xi$ *(read)*. The binding PDF
convention is recovered in the forward limit: $F^q(x,0,0)=f_{q}(x)$ (by translation $w=-z$).

### 6.2 Kinematics (s6)
Frame $\bar P_T=0$: $p^+=(1+\xi)\bar P^+$, $p'^+=(1-\xi)\bar P^+$, $\mathbf p_T=-\mathbf p'_T=-\boldsymbol\Delta_T/2$:
$t=-\frac{4\xi^2M^2+\boldsymbol\Delta_T^2}{1-\xi^2}$, $t_0=-\frac{4\xi^2M^2}{1-\xi^2}$ (so $-t\ge-t_0$). DVCS at leading power ($q'^+=0$): $q^+=\Delta^+$,
$Q^2=4\xi\bar P^+q^-$, $\boxed{\xi=x_B/(2-x_B)}$ (VGG eqs. 10–11 give the exact versions *(read)*). Regions: $\xi<x<1$ quark (DGLAP-like),
$-1<x<-\xi$ antiquark, $|x|<\xi$ emission of a $q\bar q$ pair (ERBL-like, DA-like).

### 6.3 Forward limits (s6, explicit Dirac spinors)
$\bar u(p,s)\gamma^+u(p,s')=2p^+\delta_{ss'}$, $\bar u(p,s)\gamma^+\gamma_5u(p,s')=2p^+(2\lambda)\delta_{ss'}$ ⇒
$H^q(x,0,0)=q(x)\theta(x)-\bar q(-x)\theta(-x)$, $\tilde H^q(x,0,0)=\Delta q(x)\theta(x)+\Delta\bar q(-x)\theta(-x)$ (Ji PRL eq. 17 *(read)*).
$E,\tilde E$ multiply structures $\propto\Delta$; $E(x,0,0)$ exists but is not a density.

### 6.4 Polynomiality, D-term, Ji sum rule
Moments are local twist-2 matrix elements: $\int dx\,x^nF^q=\frac{1}{2(\bar P^+)^{n+1}}\langle p'|\bar q\gamma^+(i\overleftrightarrow D^+)^nq|p\rangle$, $\overleftrightarrow D=\frac12(\overrightarrow D-\overleftarrow D)$.
Lorentz covariance + hermiticity + time reversal of $\langle p'|\bar q\gamma^{\{\mu}i\overleftrightarrow D^{\mu_1}\cdots i\overleftrightarrow D^{\mu_n\}}q|p\rangle$ (form factors
$A_{n+1,i},B_{n+1,i}$ with even numbers $i$ of $\Delta$'s, plus $C_{n+1}$ multiplying $\bar u u\,\Delta^{\mu}\Delta^{\mu_1}\cdots\Delta^{\mu_n}/M$ for odd $n$) and the
Gordon identity $\bar u(p')u(p)=\frac M{\bar P^+}\big[\bar u\gamma^+u-\bar u\frac{i\sigma^{+\alpha}\Delta_\alpha}{2M}u\big]$ (s6, explicit spinors) give
$$\int_{-1}^1\!dx\,x^nH^q=\sum_{i\ {\rm even}}^{n}(2\xi)^iA^q_{n+1,i}(t)+[n\ {\rm odd}]\,(2\xi)^{n+1}C^q_{n+1}(t),\qquad
\int_{-1}^1\!dx\,x^nE^q=\sum_{i\ {\rm even}}^{n}(2\xi)^iB^q_{n+1,i}(t)-[n\ {\rm odd}]\,(2\xi)^{n+1}C^q_{n+1}(t).$$
$n=0$: $\int H^q=F_1^q(t)$, $\int E^q=F_2^q(t)$, $\int\tilde H^q=G_A^q$, $\int\tilde E^q=G_P^q$ (Ji PRL eq. 18 *(read)*).
$n=1$: $\int xH=A+(2\xi)^2C$, $\int xE=B-(2\xi)^2C$ ⇒ $\int x(H+E)=A+B$ ($\xi$-independent; Ji eq. 19) and **Ji's sum rule**
$J^q=\frac12[A^q(0)+B^q(0)]$ (Ji eq. 13 *(read)*; proof via $J^i=\frac12\epsilon^{ijk}\int d^3x\,M^{0jk}$ — not re-derived here).
Rigor: polynomiality and forward limits **[R]** given the definitions (Lorentz covariance; renormalization preserves it).

**Model check (s6).** Double distribution with profile $b=1$, $h(\beta,\alpha)=\frac34\frac{(1-|\beta|)^2-\alpha^2}{(1-|\beta|)^3}$, $q(\beta)=(1-\beta)^3$, plus a D-term
$D(z)=(1-z^2)\sum_{n\ {\rm odd}}d_nC_n^{3/2}(z)$ entering $H$ with $+\theta(|x|<\xi)D(x/\xi)$ and $E$ with $-$. Closed-form $H(x,\xi)$, continuous at $x=\xi$,
forward limit $(1-x)^3$; moments $n=0..6$ are even polynomials of degree $\le n+1$, e.g. $\int xH=\frac{1+16d_1\xi^2}{20}$, $\int x^2H=\frac{1+2\xi^2}{60}$,
$\int x^3H=\frac{9+18\xi^2+(432d_1+320d_3)\xi^4}{1260}$; $C_2=\frac14\int zD=\frac{d_1}5$.

---------------------------------------------------------------------------------------------------

## 7. Item (3b): DVCS at LO — the coefficient functions

**Tensor.** $T^{\mu\nu}=i\int d^4z\,e^{iq'\cdot z}\langle p'|T\{J^\mu(z)J^\nu(0)\}|p\rangle$ ($\nu$: incoming $\gamma^*(q)$, $\mu$: outgoing $\gamma(q')$); this equals Ji's definition
($i\int d^4y\,e^{-iq\cdot y}\langle p'|TJ^\nu(y)J^\mu(0)|p\rangle$, by translation) and in the forward limit it is the DIS Compton amplitude with
$\operatorname{Im}T^{\mu\nu}=2\pi W^{\mu\nu}$ (c_dis convention). Leading-twist correlator:
$\langle p'|\bar q_a(-\frac w2)q_b(\frac w2)|p\rangle\to\int dx\,e^{-ix\bar P\cdot w}\frac14[\gamma^-\mathcal H+\gamma_5\gamma^-\tilde{\mathcal H}]_{ba}$, $\mathcal H=2\bar P^+F^q$, $\tilde{\mathcal H}=2\bar P^+\tilde F^q$, so
$$T^{\mu\nu}=i\sum_qe_q^2\int dx\,\operatorname{Tr}\Big\{\big[\gamma^\mu S(k'+q')\gamma^\nu+\gamma^\nu S(k-q')\gamma^\mu\big]\tfrac14\big[\gamma^-\mathcal H+\gamma_5\gamma^-\tilde{\mathcal H}\big]\Big\},\quad k^+=(x+\eta)\bar P^+,\ k'^+=(x-\eta)\bar P^+.$$
General (doubly-virtual) kinematics: $\bar q=\frac{q+q'}2=(-\xi'\bar P^+,\bar q^-,\mathbf0_T)$, $\Delta^+=-2\eta\bar P^+$; $\xi'=-\bar q^2/(2\bar P\cdot\bar q)$ is the generalized Bjorken
variable, $\eta$ the skewness; DVCS: $q'^2=0\Leftrightarrow\xi'=\eta=\xi$; DIS: $\eta=0$, $\xi'=x_B$. Propagators: $(k'+q')^2+i0=2\bar P^+\bar q^-(x-\xi'+i0)$,
$(k-q')^2+i0=-2\bar P^+\bar q^-(x+\xi'-i0)$.

**Result (s7, explicit traces).**
$$\boxed{\;T^{\mu\nu}=-g_\perp^{\mu\nu}\sum_qe_q^2\!\int_{-1}^1\!dx\,C_V(x,\xi')F^q(x,\eta,t)+i\epsilon_\perp^{\mu\nu}\sum_qe_q^2\!\int_{-1}^1\!dx\,C_A(x,\xi')\tilde F^q(x,\eta,t)\;}$$
$$\boxed{\;C_V=\frac1{\xi'-x-i0}-\frac1{\xi'+x-i0}=-\Big[\frac1{x-\xi'+i0}+\frac1{x+\xi'-i0}\Big],\qquad C_A=\frac1{\xi'-x-i0}+\frac1{\xi'+x-i0}=-\Big[\frac1{x-\xi'+i0}-\frac1{x+\xi'-i0}\Big]\;}$$
- The kernels depend on $\xi'$ only (not on $\eta$) at LO. All components with a longitudinal index vanish: photon helicity is
  conserved; the $\gamma^*_L$ amplitude is twist 3 (s7).
- **In the form "$1/(x-\xi+i0)\mp1/(x+\xi-i0)$" the vector ($H,E$) coefficient carries the PLUS sign and the axial ($\tilde H,\tilde E$) the MINUS sign**
  (overall sign convention dependent). C-parity: $C_V(-x)=-C_V(x)$ selects $H^q(x)-H^q(-x)$ (forward $q+\bar q$); $C_A(-x)=C_A(x)$ selects
  $\tilde H^q(x)+\tilde H^q(-x)$ (forward $\Delta q+\Delta\bar q$) — the C-even exchange required by two photons.
- **DIS limit (normalization and $i0$ check):** with $\eta=0$, $\xi'=x_B$, spin-averaged $F^q=q$, and the $i\varepsilon$ kept in the propagators,
  $\operatorname{Im}T^{11}\to2\pi F_1$ with $F_1=\frac12\sum e_q^2(q+\bar q)$ (finite-$\varepsilon$ numerics; 1.39573 vs 1.39555) — **PASS against the binding DIS conventions**.
- **CFFs:** $\mathcal H(\xi,t)=\sum e_q^2\int dx\,C_V(x,\xi)H^q(x,\xi,t)$, etc.; $\operatorname{Im}\mathcal H=\pi\sum e_q^2[H^q(\xi,\xi,t)-H^q(-\xi,\xi,t)]$ (numerical: 2.26635 vs 2.26893 at $\varepsilon=10^{-3}$);
  $\operatorname{Re}\mathcal H=\mathrm{PV}\!\int dx\,H[\frac1{\xi-x}-\frac1{\xi+x}]$ (s7). At LO the imaginary part probes the GPD on the crossover line $x=\pm\xi$ only.
- Literature: Ji PRL eq. (15) gives $T^{\mu\nu}=-\frac12(p^\mu n^\nu+p^\nu n^\mu-g^{\mu\nu})\int dx(\frac1{x-\xi_{\rm Ji}/2+i\epsilon}+\frac1{x+\xi_{\rm Ji}/2+i\epsilon})[H\bar U\slashed nU+\dots]
  -\frac i2\epsilon^{\mu\nu\alpha\beta}p_\alpha n_\beta\int dx(\frac1{x-\xi_{\rm Ji}/2+i\epsilon}-\frac1{x+\xi_{\rm Ji}/2+i\epsilon})[\tilde H\bar U\slashed n\gamma_5U+\dots]$ *(read)*. Since $p^\mu n^\nu+p^\nu n^\mu-g^{\mu\nu}=-g_\perp^{\mu\nu}$
  and $[H\bar U\slashed nU+\dots]=2F^q$, this equals my result (vector term identical; axial term identical if Ji's $\epsilon^{0123}=+1$), except for
  the $i\epsilon$ of the second denominator, which must be $-i\epsilon$ (Feynman propagator; required by the optical theorem — checked).
  VGG eq. (38) *(read)* has $-i\epsilon$ and equals $-T^{\mu\nu}$ (overall sign of their $H^{\mu\nu}$; $\varepsilon_{0123}=+1$ there).
- Rigor: factorization of DVCS at leading power, all orders **[A]** (Collins–Freund 1999; Ji–Osborne 1998; also Radyushkin 1996/97).
  Abstracts *(read)*: Collins–Freund prove factorization to all orders up to power corrections and state that the virtuality of the produced
  photon does not influence the theorem; their v2 (2 July 1998) has, per the arXiv comments, an "improved treatment of endpoint/breakpoint
  regions" ($x=\pm\xi$, where one parton line has zero plus momentum). Ji–Osborne show at one loop that the IR divergences are absorbed into
  the GPDs (also with one photon on shell) and argue all-order factorization. (The earlier tex wording "soft gluons cancel by Ward identities"
  was replaced: the Ward identities are used for the longitudinal collinear gluons that build the Wilson line.)
  The LO handbag violates EM gauge invariance for the real photon at $O(\Delta_\perp/Q)$ (restored at twist 3; VGG eqs. 41–44).
  Kinematic power corrections (blueprint P13.9 "(verify)" — verified on INSPIRE, not re-derived): Braun & Manashov, PRL 107 (2011) 202001
  [arXiv:1108.2394]; JHEP 01 (2012) 085 [arXiv:1111.6765]; Braun, Manashov & Pirnay, PRD 86 (2012) 014003 [arXiv:1205.3332, scalar target];
  PRL 109 (2012) 242001 [arXiv:1209.2559, nucleon].

---------------------------------------------------------------------------------------------------

## 8. Item (3c): LO meson production by a longitudinal photon

$A^\nu=\langle M(p_M)N'(p')|J^\nu(0)|N(p)\rangle$. Leading-power kinematics: $\bar P=(\bar P^+,0,\mathbf 0_T)$, $\Delta^+=-2\xi\bar P^+$, $q=(-2\xi\bar P^+,q^-,\mathbf0_T)$,
$p_M=q-\Delta=(0,q^-,\mathbf0_T)$, $Q^2=4\xi\bar P^+q^-$, $\varepsilon_L=(q^+,-q^-,\mathbf0_T)/Q$ ($\varepsilon_L^2=1$, $\varepsilon_L\cdot q=0$).
Quark-exchange graphs: line 1 runs from the nucleon quark $a$ ($k^+=(x+\xi)\bar P^+$) to the meson quark ($zp_M$), line 2 from the meson antiquark
($\bar zp_M$) to the quark $b$ returned to the nucleon ($k'^+=(x-\xi)\bar P^+$); one gluon; the photon on line 1 (graphs 1, 2) or line 2 (graphs 3, 4).
Virtualities: graph 1 quark $(x-\xi)Q^2/(2\xi)$, gluon (1, 2) $\bar z(x-\xi)Q^2/(2\xi)$; graph 2 quark $-\bar zQ^2$; graph 3 quark $-(x+\xi)Q^2/(2\xi)$, gluon (3, 4)
$-z(x+\xi)Q^2/(2\xi)$; graph 4 quark $-zQ^2$. Projectors: $M_N=\frac14[\gamma^-\mathcal H+\gamma_5\gamma^-\tilde{\mathcal H}]$, $M_\pi=\frac{if_\pi}4\slashed p_M\gamma_5\phi_\pi(z)$,
$M_{\rho_L}=\frac{f_\rho}4\slashed p_M\phi_\rho(z)$; colour $C_F/N_c$; overall $(-1)$ as for $F_\pi$.

**Result (s8).** The double pole $(x-\xi+i0)^{-2}$ of graph 1 cancels against its numerator; graphs 1 and 2 contribute equally, as do 3 and 4:
$$\boxed{\;\varepsilon_L\!\cdot\!A_\pi=-i\,\frac{C_F}{N_c}\,\frac{4\pi\alpha_sf_\pi}{Q}\int_0^1\!dz\,\phi_\pi(z)\int_{-1}^1\!dx\Big[\frac{e_a}{\bar z\,(x-\xi+i0)}+\frac{e_b}{z\,(x+\xi-i0)}\Big]\tilde F^{ba}(x,\xi,t)\;}$$
$$\varepsilon_L\!\cdot\!A_{\rho_L}=+\frac{C_F}{N_c}\frac{4\pi\alpha_sf_\rho}{Q}\int_0^1\!dz\,\phi_\rho(z)\int_{-1}^1\!dx\Big[\frac{e_a}{\bar z(x-\xi+i0)}+\frac{e_b}{z(x+\xi-i0)}\Big]F^{ba}(x,\xi,t)\quad(+\text{gluon-GPD graphs for neutral }V,\text{ not computed})$$
(the relative phase between the $\pi$ and $\rho$ lines is a projector-phase convention). For a symmetric DA $\int\phi/z=\int\phi/\bar z=3(1+a_2+\dots)$, so the
kernel is $\propto e_a/(x-\xi+i0)+e_b/(x+\xi-i0)$; for $\gamma^*p\to\pi^+n$: $a=u$, $b=d$, $\tilde F^{du}\to\tilde H^u-\tilde H^d$ (isospin), plus the pion pole in $\tilde E$.
- Parity: pseudoscalar mesons couple only to $\tilde H,\tilde E$; longitudinal vector mesons only to $H,E$ (s8; CFS 1997).
- C-parity (convention independent): for $\pi^0,\rho^0$ ($e_a=e_b$) the kernel $1/(x-\xi)+1/(x+\xi)$ is odd in $x$: $\rho^0$ selects $H(x)-H(-x)$ (C-even exchange,
  $C(\gamma^*)C(\rho^0)=+1$), $\pi^0$ selects $\tilde H(x)-\tilde H(-x)$ (C-odd exchange, $C(\gamma^*)C(\pi^0)=-1$). ✓
- Transverse photons: $\varepsilon_T\cdot A=0$ for $\pi$ and $\rho_L$ at leading twist (s8) ⇒ $\sigma_T/\sigma_L=O(1/Q^2)$.
- Scaling: $A\propto1/Q$ ⇒ $d\sigma_L/dt\propto1/Q^6$ at fixed $x_B,t$.
- Literature: VGG 1999 eqs. (47), (48), (58), (59) *(read)*: $\mathcal M^L=-ie\frac49\frac1Q[\int_0^1dz\frac{\Phi(z)}z]\frac12\int dx[\frac{e_a\text{-type}}{x-\xi+i\epsilon}+\frac{e_b\text{-type}}{x+\xi-i\epsilon}](4\pi\alpha_s)\{\dots\}$ with
  $\Phi_\pi=\sqrt2\,(0.0924\text{ GeV})\,6z\bar z=f_\pi^{(130)}\phi^{\rm as}$, $\frac12\{\tilde H\bar N\gamma\cdot n\gamma_5N+\tilde E\bar N\gamma_5\frac{\Delta\cdot n}{2m}N\}=\tilde F$; for $\pi^\pm$ the charges are
  $\{-\frac23,\frac13\}$ = $-\{e_u,e_d\}$, the overall minus coming from their charged-meson phase convention ($|\rho^+\rangle=-|u\bar d\rangle$, stated before their eq. 58). **PASS** (colour factor $4/9=C_F/N_c$, $4\pi\alpha_s$, $1/Q$,
  DA integral, kernel with charges, and the phase $-i$ for $\pi^0$).
- Rigor: **[A]** for $\gamma^*_L$ (Collins–Frankfurt–Strikman 1997: endpoint regions power suppressed for longitudinal photons).
  $\gamma^*_T$: the leading-twist $\gamma^*_T\to V_T$ amplitude vanishes to all orders. At twist 2 a $V_T$ enters only through the chiral-odd DA
  $\phi_\perp$, which needs a chiral-odd (transversity) GPD, and that contribution vanishes to all orders: Diehl–Gousset–Pire 1999 (abstract *(read)*:
  the leading-twist contribution "vanishes at all orders in perturbation theory"); Collins–Diehl 2000, PRD 61, 114015 (abstract *(read)*: all-orders
  argument; an NLO calculation claiming a non-zero result omitted necessary collinear subtractions). The first non-vanishing $\gamma^*_T\to V_T$
  amplitude is twist 3. **Mankiewicz–Piller 2000** *(full text read, arXiv v1)* compute it at LO with the twist-3 DAs $g^v\equiv g_\perp^{(v)}$,
  $g^a\equiv g_\perp^{(a)}$ in the Wandzura–Wilczek approximation (their eqs. 4–5): (i) the amplitude contains
  $\mathcal I_{1}=\int_0^1\frac{d\tau}{\tau}\big(4g^v-2\Phi_\parallel/\tau+\frac{g^a}{2\tau\bar\tau}\big)$ and $\mathcal I_2=\int_0^1\frac{d\tau}{\tau}\big(2g^v+\frac{g^a}{2\tau\bar\tau}\big)$
  (their eq. 10), whose integrands behave as $1/\tau$ for $\tau\to0$ — a *logarithmic* divergence — because the WW relation gives
  $g^v(0)=\frac12\int_0^1du\,\phi_\parallel(u)/u\neq0$, so no modification of the endpoint behaviour of $\phi_\parallel$ can cure it; (ii) the GPD
  convolutions contain double poles $(\xi\mp x-i0)^{-2}$ (their eqs. 7, 8, 11–13), defined only if the GPD and its first derivative are continuous
  at $x=\pm\xi$, and for the asymptotic singlet quark GPD the real part is IR singular (their eq. 16). Hence collinear factorization fails: **[V]**.
  (Check, s8 §5b: with their eqs. 3–5 and 10 *as printed* (text-extracted from the v1 PDF) and $\phi_\parallel=6\tau\bar\tau$ one has
  $g^v=\frac32(\tau^2+\bar\tau^2)$, $g^a=6\tau\bar\tau$, $\Phi_\parallel=\frac32\tau\bar\tau(2\tau-1)$, so the integrands behave as $12/\tau$ and $6/\tau$
  (in general $8g^v(0)/\tau$ and $4g^v(0)/\tau$); their text says "$12/\tau$ and $9/\tau$", which would require $4g^v$ instead of $2g^v$ in $\mathcal I_2$.
  The source is internally inconsistent here — immaterial for the divergence, but do not quote "9/τ". An endpoint-suppressed DA $30\tau^2\bar\tau^2$
  still gives $10/\tau$ and $5/\tau$.) *Correction:* an earlier version of this file and of the tex said "$\int dz\,\phi(z)/z^2$-type
  divergences"; that is not what the source says and has been replaced. $k_T$-modified treatments (Goloskokov–Kroll 2005) are models **[P]**.

---------------------------------------------------------------------------------------------------

## 9. Rigor tags proposed for Chapter 13

| statement | tag | basis |
|---|---|---|
| DA/GPD definitions, gauge invariance, support, forward limits, polynomiality, Ji sum rule (given definitions) | [R] | §2, §6 (Lorentz covariance; explicit checks) |
| LO ERBL kernel, Gegenbauer eigenfunctions, $\gamma_n$, asymptotic DA | [R] (PT, LO) | §3 (complete derivation) |
| NLO ERBL (conformal-symmetry breaking, mixing of $a_n$) | [R] at fixed order in the literature (not redone here) | BKM 2003 §5 |
| $F_\pi$ factorization at leading power, all orders | [A] | LB 1979/80, ER 1980, DM 1980 |
| $\gamma^*\gamma\to\pi^0$ at leading power | [A] | as above; NNLO known |
| endpoint/soft-overlap dominance at accessible $Q^2$ | [P] (numerical statement; formal power counting) | §4.3, ILS 1984/89 |
| Sudakov/$k_T$ resummation scheme (Li–Sterman) | [P] | model-dependent |
| DVCS factorization | [A] | Collins–Freund 1999; Ji–Osborne 1998 |
| $\gamma^*_L$ meson production | [A] | CFS 1997 |
| vanishing of the leading-twist $\gamma^*_T\to V_T$ amplitude (transversity decoupling), all orders | [A] | DGP 1999; Collins–Diehl 2000 (chirality + helicity conservation) |
| collinear factorization for $\gamma^*_T\to V_T$ (twist 3) | [V] | Mankiewicz–Piller 2000: log endpoint divergence of the WW twist-3 DA integrals, not curable by endpoint suppression of $\phi_\parallel$; double poles in the GPD convolution (s8 §5b) |

---------------------------------------------------------------------------------------------------

## 10. Discrepancies / corrections to the conventions, outline, blueprint and task text

1. **Missing conventions (CONTEXT.md).** No $\gamma_5$ / $\epsilon^{0123}$ convention is fixed, but the $\pi^0\gamma\gamma$ form factor, $\tilde H,\tilde E$ and the
   axial DVCS term depend on it. Proposal: $\gamma_5=i\gamma^0\gamma^1\gamma^2\gamma^3$, $\epsilon^{0123}=+1$ ⇒ $\operatorname{Tr}(\gamma^\mu\gamma^\nu\gamma^\rho\gamma^\sigma\gamma_5)=-4i\epsilon^{\mu\nu\rho\sigma}$,
   $\epsilon_\perp^{\mu\nu}=\epsilon^{\mu\nu\rho\sigma}\bar n_\rho n_\sigma$ ($\epsilon_\perp^{12}=+1$). Warn readers that VGG 1999 use $\varepsilon_{0123}=+1$.
2. **Task/blueprint DVCS kernel signs.** The task writes "$1/(x-\xi+i0)\mp1/(x+\xi-i0)$". Correct statement: $H,E$ come with $1/(x-\xi+i0)+1/(x+\xi-i0)$, $\tilde H,\tilde E$ with
   $1/(x-\xi+i0)-1/(x+\xi-i0)$ (equivalently $1/(\xi-x-i0)\mp1/(\xi+x-i0)$ with the upper sign for $H$), overall sign tied to the definition of $T^{\mu\nu}$.
   Blueprint E13.13 ("$\propto\frac1{x-\xi+i0}+\frac1{x+\xi-i0}$, signs to be fixed") is right for $H$; fixed here.
3. **Blueprint E13.11 "four/five tree graphs":** there are exactly **four** $O(\alpha_s)$ graphs for $F_\pi$ in Feynman gauge (no $\gamma gg$ vertex; graphs with
   the gluon on one line do not turn the spectator). Individually they are not gauge invariant; A+B and C+D are.
4. **Ji's $\xi$ and $i\epsilon$.** Ji 1997 uses $\xi_{\rm Ji}=2\xi$; when quoting Ji's formulas convert. In the arXiv v1 of Ji's PRL (eq. 15) the second denominator
   reads $x+\xi/2+i\epsilon$; the correct prescription is $-i\epsilon$ (published version not checked).
5. **$f_\pi$ value.** Blueprint "≈131 MeV" vs survey "≈130 MeV": same (130-MeV) normalization; tree-level extraction gives 131.7 MeV, PDG-type value ≈130 MeV;
   BKM quote 132 MeV, BaBar 131 MeV. Recommend writing "$f_\pi\approx130$ MeV ($F_\pi=f_\pi/\sqrt2\approx92$ MeV)".
6. **Blueprint T13.4 parenthetical "soft/Feynman contribution $\propto1/Q^4$":** standard statement, not derived here — keep as a remark with citation (ILS)
   rather than as part of the theorem.
7. **Anomalous-dimension normalization.** Blueprint P13.2 uses BKM's $\gamma_n^{(0)}=C_F[\dots]$ with exponent $\gamma^{(0)}_n/\beta_0$ — correct; the
   "$\mu\,d/d\mu$, $\alpha_s/4\pi$" normalization gives twice that ($\gamma_2=\frac{25}3C_F$) with exponent $\gamma_n/(2\beta_0)$. Either is fine if stated.
8. **Reference warning.** Phys. Rev. Lett. 84 (2000) 2589 (Frankfurt–Polyakov–Strikman–Vanderhaeghen) is about *decuplet baryons*; the standard reference
   for hard pseudoscalar-meson production and $\tilde E$'s pion pole is Frankfurt–Pobylitsa–Polyakov–Strikman, PRD 60 (1999) 014010 (both verified on INSPIRE).
9. **Survey item 16 formula** $Q^2F_\pi=\frac{8\pi}9\alpha_sf_\pi^2|\int\phi/x|^2$ holds for a symmetric DA; for a general DA the $u$ and $\bar d$ terms differ
   ($e_u|\int\phi/\bar x|^2+e_{\bar d}|\int\phi/x|^2$, $\times\frac{2\pi C_F}{N_c}\alpha_sf_\pi^2$).
10. **Transverse photons (self-correction + answer to critic REVIEW "Mankiewicz–Piller 2000 (verify)").** The reference is correct (PRD 61 (2000)
   074013, hep-ph/9905287) and supports blueprint P13.10. But the divergence is *not* "$\int dz\,\phi(z)/z^2$-type" (my earlier wording, now removed):
   in the WW approximation the twist-3 integrals $\mathcal I_{1,2}=\int_0^1\frac{d\tau}\tau(\dots)$ diverge *logarithmically* because
   $g_\perp^{(v)}(0)=\frac12\int_0^1du\,\phi_\parallel(u)/u\neq0$, so suppressing the endpoints of $\phi_\parallel$ does not help; in addition the GPD
   convolutions have double poles $(\xi\mp x-i0)^{-2}$. The leading-twist $\gamma^*_T\to V_T$ amplitude vanishes to all orders (DGP 1999 and
   Collins–Diehl 2000, PRD 61 (2000) 114015 — the latter should be added to the Ch13 reference list). MP's text value "$9/\tau$" is inconsistent with
   their eq. (10) as printed ($6/\tau$); do not quote it.
11. **DVCS proof sketch.** Do not write that "soft gluons cancel by Ward identities" in DVCS: per Collins–Freund the issues are the collinear region
   (Ward identities → Wilson line) and the endpoint/breakpoint regions $x=\pm\xi$ (their v2 "improved treatment of endpoint/breakpoint regions").
12. **Blueprint "(verify)" items resolved.** T13.4 NLO references and P13.9 Braun–Manashov references: all verified on INSPIRE (§4.2, §7, §12).
   Blueprint `fig:endpoint` can use `fig:cex-endpoint` (exact $R_{\rm as}$, $R_{\rm CZ}$ curves, pgfplots).

---------------------------------------------------------------------------------------------------

## 11. Files and how to run

- `DERIVATION.md` (this file), `run_all.sh`, `scripts/common.py`, `scripts/s1_da.py` … `scripts/s8_meson.py`, `logs/*.log`, `logs/SUMMARY.txt`.
- `tex/c_exclusive_da_erbl.tex` (DA, ERBL derivation and solution, TikZ graphs), `tex/c_exclusive_formfactors.tex` ($F_\pi$ and $F_{\gamma^*\gamma\pi}$, TikZ graphs,
  pgfplots endpoint figure `fig:cex-endpoint`),
  `tex/c_exclusive_gpd.tex` (GPDs, DVCS, meson production, TikZ graphs), `tex/test_c_exclusive.tex` (driver), `tex/test_c_exclusive.pdf`.
  Build: `cd tex; cp ../../../common/preamble_fact.tex .; xelatex test_c_exclusive.tex` (twice).

## 12. References (verification status)

Verified on INSPIRE by the refs/survey agents (`research/refs/NOTES.md`, `research/survey/verified_refs_table.tsv`):
Lepage & Brodsky, PLB 87 (1979) 359; PRD 22 (1980) 2157. Efremov & Radyushkin, PLB 94 (1980) 245; TMP 42 (1980) 97.
Duncan & Mueller, PLB 90 (1980) 159; PRD 21 (1980) 1636. Chernyak & Zhitnitsky, Phys. Rept. 112 (1984) 173. Isgur & Llewellyn Smith,
PRL 52 (1984) 1080; NPB 317 (1989) 526. Li & Sterman, NPB 381 (1992) 129. Müller et al., Fortsch. Phys. 42 (1994) 101. Ji, PRL 78 (1997) 610;
PRD 55 (1997) 7114. Radyushkin, PLB 380 (1996) 417; PRD 56 (1997) 5524. Collins, Frankfurt & Strikman, PRD 56 (1997) 2982. Ji & Osborne,
PRD 58 (1998) 094018. Collins & Freund, PRD 59 (1999) 074009. Mankiewicz & Piller, PRD 61 (2000) 074013. Goloskokov & Kroll (2005)
(Goloskokov:2005sd). Diehl, Phys. Rept. 388 (2003) 41. Belitsky & Radyushkin, Phys. Rept. 418 (2005) 1. Gao, Huber, Ji, Wang, PRL 128 (2022) 062003.

Verified on INSPIRE in this work (control numbers): Brodsky & Lepage, PRD 24 (1981) 1808 [165280]; BaBar (Aubert et al.), PRD 80 (2009) 052002,
arXiv:0905.4778 [821653]; Belle (Uehara et al.), PRD 86 (2012) 092007, arXiv:1205.3249 [1114749]; Brodsky, Frishman, Lepage & Sachrajda, PLB 91
(1980) 239 [152273]; Braun, Korchemsky & Müller, Prog. Part. Nucl. Phys. 51 (2003) 311, hep-ph/0306057 [620571]; Belitsky, Müller & Kirchner,
NPB 629 (2002) 323 [567921]; Goeke, Polyakov & Vanderhaeghen, Prog. Part. Nucl. Phys. 47 (2001) 401 [557665]; Vanderhaeghen, Guichon & Guidal,
PRD 60 (1999) 094017, hep-ph/9905372 [500047]; Mankiewicz, Piller & Weigl, EPJC 5 (1998) 119 [450668]; Frankfurt, Pobylitsa, Polyakov & Strikman,
PRD 60 (1999) 014010 [494554]; Diehl, Gousset & Pire, PRD 59 (1999) 034023 [475578]; Polyakov & Weiss, PRD 60 (1999) 114017 [495824];
Farrar & Jackson, PRL 43 (1979) 246 [140564]; Gross & Wilczek, PRD 8 (1973) 3633 [81404], PRD 9 (1974) 980 [95436]; CLEO (Gronberg et al.),
PRD 57 (1998) 33 [446031]; CELLO (Behrend et al.), Z. Phys. C 49 (1991) 401 [299282]; Ji, J. Phys. G 24 (1998) 1181 [473266].
Verified in the resume pass (2026-10-10; INSPIRE control numbers or arXiv listing): Collins & Diehl, PRD 61 (2000) 114015, hep-ph/9907498 (arXiv
abstract read); Mankiewicz & Piller, PRD 61 (2000) 074013, hep-ph/9905287 (full text read); Field, Gupta, Otto & Chang, NPB 186 (1981) 429 [10292];
Dittes & Radyushkin, Sov. J. Nucl. Phys. 34 (1981) 293, Yad. Fiz. 34 (1981) 529 [171766]; Braaten & Tse, PRD 35 (1987) 2255 [21110]; Melić, Nižić & Passek,
PRD 60 (1999) 074004, hep-ph/9802204 [466760]; Braun & Manashov, PRL 107 (2011) 202001, arXiv:1108.2394 [922946]; Braun & Manashov, JHEP 01 (2012) 085,
arXiv:1111.6765 [1079223]; Braun, Manashov & Pirnay, PRD 86 (2012) 014003, arXiv:1205.3332 [1114766]; PRL 109 (2012) 242001, arXiv:1209.2559 [1185275];
Collins & Freund (arXiv listing: v2 2 July 1998, "Improved treatment of endpoint/breakpoint regions"); Ji & Osborne (abstract read).
Equations *read* in this work: BKM 2003 eqs. (139)–(152) (arXiv v1); VGG 1999 eqs. (4)–(13), (38)–(48), (58)–(65) (arXiv v1); Ji PRL 1997 eqs. (12)–(19) (arXiv v1);
BaBar 2009 eq. (2) (arXiv v1); Mankiewicz–Piller eqs. (1)–(16) (arXiv v1). In the resume pass Ji eqs. (12)–(19), VGG eqs. (38), (63), (65), BKM eqs. (139)–(151)
and BaBar eq. (2) were re-read from the PDFs and agree with what is quoted here.
Not verified (do not cite without checking): the original LB normalization statement "$\int\phi_{\rm LB}=f_\pi/(2\sqrt{N_c})$", the "$1/Q^4$" soft-overlap
scaling, any experimental $F_\pi$ numbers.
