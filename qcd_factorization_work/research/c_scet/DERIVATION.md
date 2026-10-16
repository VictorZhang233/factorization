# research/c_scet — SCET (modes, Lagrangian, Wilson lines, decoupling, thrust), NRQCD, QCD factorization for B decays (BBNS/BPS)

Directory: `"/Users/hao-cheng/Desktop/theorem proof/qcd_factorization_work/research/c_scet"` (quote the path, it contains a space).
Re-run everything with `sh run_all.sh` (about 35 s); the logs go to `logs/*.log`, the summary to `logs/SUMMARY.txt`.

All results below were derived from the Feynman rules of `CONTEXT.md` ($D_\mu=\partial_\mu-igA_\mu^at^a$, vertex $ig\gamma^\mu t^a$,
$D=4-2\varepsilon$, $\overline{\rm MS}$) and checked by the scripts in `scripts/`. sympy was used for exact algebra and for
results exact in $\varepsilon$, and an own $D$-dimensional trace engine was validated against explicit $4\times4$ matrices.
numpy, scipy and mpmath were used for numerical cross-checks.
Literature values were compared with the **original arXiv LaTeX sources, which I downloaded and read during this work**; these
are marked *(read)*. On 2026-10-10 the sources of BS 2008, RS 2016, BBNS 2000/2001, BN 2003, BPS 2001/2002 and BBL 1995 were downloaded again and
every equation quoted in `tex/` was re-checked against them (two attribution corrections resulted, §6 items 14 and 16). Abstracts read on INSPIRE are marked *(abstract)*. Values I recall but whose source I could not open are marked
*(recall)*. Every bibliographic entry in §7 was checked on INSPIRE (one hit per query).

| script | content | checks |
|---|---|---|
| `common.py` | $D$-dim trace engine (self-test against $4\times4$ traces), spinors, SU(3) | 9/9 |
| `s1_scet_algebra.py` | light-cone algebra; projectors; $\bar\psi i\slashed D\psi$ decomposition; integrating out $\phi$; exact tree-level identity for the collinear vertex; power counting of all modes (virtualities, field scalings, multipole expansion, which interactions stay on shell); jet-function normalization (cut definition vs. the literal Becher–Schwartz formula) | 52/52 |
| `s1_wilson_decoupling.py` | path-ordered exponentials solved numerically for random su(3) backgrounds (unitarity, $v\cdot D\,W=0$, ordering, $O(g^2)$ expansion, **key identity $in\cdot D_{us}Y_n=Y_n\,in\cdot\partial$**, conjugation of $n\cdot A_n$, gauge covariance); eikonal rules from the LO Lagrangian (absorbed and emitted usoft gluons); tree-level QCD$\to$SCET matching that generates $W_n$; collinear Ward identity; SCET$_{\rm II}$ soft Wilson line | 23/23 |
| `s2_thrust_oneloop.py` | massless form factor exact in $\varepsilon$ $\to C_V$, $H$; one-loop jet function from the cut (exact in $\varepsilon$; projected $|M|^2$ = $D$-dim splitting function); one-loop thrust soft function; distributions; Laplace transforms; anomalous dimensions | 21/21 |
| `s2_thrust_rg.py` | RG consistency (one loop, and all orders for the cusp part); two-loop $C_F^2$ cancellation in $\gamma^S$; $e^+e^-\to q\bar qg$ matrix element; LO thrust distribution; singular terms; $\delta(\tau)$ coefficient from the total-rate sum rule; Laplace transform of the cumulant; LL exponent vs. CTTW; exact thrust–hemisphere-mass identity on random 3- and 4-parton events | 18/18 |
| `s3_nrqcd.py` | velocity scaling; LO $\Gamma(V\to e^+e^-)$ and $\Gamma(\eta\to\gamma\gamma)$ from threshold amplitudes; BBL coefficients ${\rm Im}\,f$; $\langle O_1\rangle=2N_c|\psi(0)|^2$; **one-loop $c_v$ at threshold in DR** | 22/22 |
| `s4_bbns.py` | QCDF power counting; origin of $12\ln(m_b/\mu)$ from operator mixing; vertex kernel $g(x)$ Gegenbauer integrals; hard-spectator virtualities; twist-3 and annihilation endpoint divergences; prescription dependence of $X_A$; colour transparency | 26/26 |

**Total: 171/171 PASS** (re-run 2026-10-10). LaTeX snippets (Chinese, monograph macros, TikZ figures) are in `tex/`. `tex/test_c_scet.tex`
compiles them with the common preamble (§8).

---------------------------------------------------------------------------------------------------------------------

## 0. Results at a glance (with literature cross-checks)

$a\equiv C_F\alpha_s(\mu)/(4\pi)$. In the "lit." column, "(read)" means I read the equation in the source file during this work.

| # | result (this work) | literature | conversion | status |
|---|---|---|---|---|
| 1 | Modes in $(\bar n\!\cdot\!p,\,n\!\cdot\!p,\,p_\perp)/Q$: hard $(1,1,1)$; $n$-coll $(1,\lambda^2,\lambda)$; $\bar n$-coll $(\lambda^2,1,\lambda)$; usoft $(\lambda^2,\lambda^2,\lambda^2)$; soft $(\lambda,\lambda,\lambda)$; hard-coll $(1,\lambda,\lambda^{1/2})$; Glauber $n\bar n$ $(\lambda^2,\lambda^2,\lambda)$, $ns$ $(\lambda,\lambda^2,\lambda)$, $\bar ns$ $(\lambda^2,\lambda,\lambda)$ | Rothstein–Stewart 2016, Table 1 (read): $(n\!\cdot\!p,\bar n\!\cdot\!p,p_\perp)$, Glauber $Q(\lambda^a,\lambda^b,\lambda)$, $a+b>2$, $\{2,2\},\{2,1\},\{1,2\}$ | swap first two entries | PASS |
| 2 | field scalings $\xi_n\sim\lambda$, $(\bar n\!\cdot\!A_n,n\!\cdot\!A_n,A_{n\perp})\sim(1,\lambda^2,\lambda)$, $A_{us}\sim\lambda^2$, $q_{us}\sim\lambda^3$, $A_s\sim\lambda$, $q_s\sim\lambda^{3/2}$ | BPS 2001 §2 (read); RS 2016 Table 1 (read) | same | PASS |
| 3 | $\mathcal L^{(0)}_{\xi\xi}=\bar\xi_n\big[in\!\cdot\!D+i\slashed D_{\perp c}\frac1{i\bar n\cdot D_c}i\slashed D_{\perp c}\big]\frac{\bar{\slashed n}}2\xi_n$, $in\!\cdot\!D=in\!\cdot\!\partial+gn\!\cdot\!A_n+gn\!\cdot\!A_{us}(x_-)$ | BFPS 2001, BPS 2002 eq. (Lcq) (read) | $D=\partial-igA$ in both | PASS |
| 4 | collinear vertex $ig t^a\big[n^\mu+\frac{\gamma_\perp^\mu\slashed p_\perp}{\bar n\cdot p}+\frac{\slashed p'_\perp\gamma_\perp^\mu}{\bar n\cdot p'}-\frac{\slashed p'_\perp\slashed p_\perp\bar n^\mu}{\bar n\cdot p\,\bar n\cdot p'}\big]\frac{\bar{\slashed n}}2$; usoft vertex $igt^an^\mu\frac{\bar{\slashed n}}2$; propagator $i\frac{\slashed n}2\frac{\bar n\cdot p}{p^2+i0}$ | BFPS 2001 (recall of the form; checked by an exact identity) | — | PASS (exact tree identity) |
| 5 | $W_n(x)=W[x,x-\infty\bar n]=P\exp\!\big(ig\int_{-\infty}^0\!ds\,\bar n\!\cdot\!A_n(x+s\bar n)\big)=\sum_{\rm perms}\exp\!\big[-\frac g{\bar{\mathcal P}}\bar n\!\cdot\!A_n\big]$; one-gluon rule $-g\,\bar n^\mu t^a/(\bar n\cdot k+i0)$ | BPS 2001 eq. (W) (read) | none | PASS |
| 6 | key identity $in\!\cdot\!D_{us}\,Y_n=Y_n\,in\!\cdot\!\partial$; decoupling $\xi_n=Y_n\xi^{(0)}_n$, $A_n=Y_nA^{(0)}_nY_n^\dagger$, $c_n=Y_nc_n^{(0)}Y_n^\dagger$ | BPS 2002 §IV (read) | none | PASS |
| 7 | $F^{(1)}_{\rm bare}=\frac{\alpha_sC_F}{4\pi}\big(\frac{4\pi\mu_0^2}{Q^2}\big)^{\varepsilon}c_\Gamma\Big[-\frac{2-\varepsilon+2\varepsilon^2}{\varepsilon^2(1-2\varepsilon)}\Big]$ (exact) | c_dis agent, same Laurent series incl. $O(\varepsilon)$ | — | PASS |
| 8 | $C_V=1+a[-L^2+3L-8+\zeta_2]$, $L=\ln\frac{-q^2-i0}{\mu^2}$; $H=1+a[-2L_Q^2+6L_Q-16+\frac{7\pi^2}3]$ | Becher–Schwartz 2008 App. B (read): $c_1^H=C_F(-16+\frac{7\pi^2}3)$, $\Gamma_0=4C_F$, $\gamma^H_0=-6C_F$ | none | PASS |
| 9 | $J^{(1)}_{\rm bare}(p^2)=-\frac{\alpha_sC_F}{4\pi}(4\pi\mu_0^2)^\varepsilon\frac{4-\varepsilon}{\varepsilon}\frac{\Gamma(2-\varepsilon)}{\Gamma(2-2\varepsilon)}(p^2)^{-1-\varepsilon}$; $J=\delta(p^2)+a\{(7-\pi^2)\delta(p^2)-3[\frac1{p^2}]_*+4[\frac{\ln(p^2/\mu^2)}{p^2}]_*\}$; $\tilde j=1+a(2L^2-3L+7-\frac{2\pi^2}3)$ | BS 2008 (read): $c_1^J=C_F(7-\frac{2\pi^2}3)$, $\gamma_0^J=-3C_F$ | none | PASS |
| 10 | $S_T=\delta(k)+a\{\frac{\pi^2}3\delta(k)-16[\frac{\ln(k/\mu)}k]_*\}$; $\tilde s_T=1+a(-8L^2-\pi^2)$ | BS 2008 (read): $c_1^S=-C_F\pi^2$, $\gamma^S=\gamma^H-2\gamma^J$ | none | PASS |
| 11 | RG consistency: cusp terms cancel identically, $\gamma^S=\gamma^H-2\gamma^J$; at two loops the $C_F^2$ terms of $\gamma^H_1-2\gamma^J_1$ cancel and $\gamma^S_1=C_FC_A(\frac{808}{27}-\frac{11\pi^2}9-28\zeta_3)+C_FT_Fn_f(-\frac{224}{27}+\frac{4\pi^2}9)$ | BS 2008 eq. (gw), App. A (read) | none | PASS |
| 12 | $\frac1{\sigma_0}\frac{d\sigma}{d\tau}=\delta(\tau)+\frac{C_F\alpha_s}{2\pi}\{(\frac{\pi^2}3-1)\delta(\tau)-3[\frac1\tau]_+-4[\frac{\ln\tau}\tau]_+\}$ (plus at $\tau=0$ on $[0,1]$) | full QCD $O(\alpha_s)$ (derived here): $\delta$ coefficient $2.289868133697$ from the sum rule vs $\pi^2/3-1=2.289868133696$ | — | PASS ($10^{-12}$) |
| 13 | LO thrust $\frac{C_F\alpha_s}{2\pi}\big[\frac{2(3T^2-3T+2)}{T(1-T)}\ln\frac{2T-1}{1-T}-\frac{3(3T-2)(2-T)}{1-T}\big]$ (integrated from the matrix element) | De Rújula–Ellis–Floratos–Gaillard 1978 (recall) | — | PASS ($7\times10^{-15}$) |
| 14 | $\ln\tilde t_{\rm LL}=\ell\,g_1(\lambda)$, $g_1=-\frac{C_F}{\pi b\lambda}[(1-2\lambda)\ln(1-2\lambda)-2(1-\lambda)\ln(1-\lambda)]$, $\lambda=b\alpha_s(Q)\ell$, $b=\beta_0/4\pi$ | CTTW 1993 (recall; pre-arXiv) | their $\beta_0=(11C_A-2n_f)/(12\pi)=b$ | PASS (exact identity) |
| 15 | NRQCD velocity rules $\psi\sim(mv)^{3/2}$, $D\sim mv$, $D_t\sim mv^2$, $gE\sim m^2v^3$, $gB\sim m^2v^4$; $1/m^2$ bilinears $O(v^2)$; P-wave singlet $\sim$ octet $^3S_1$ in $\chi_J$ $\sim mv^5$ | BBL 1995 §II.C (read headings; recall of table), BBL 1992 (abstract) | — | PASS |
| 16 | $\Gamma(^3S_1\to e^+e^-)=\frac{16\pi N_c}{3}\frac{e_Q^2\alpha^2|\psi(0)|^2}{M^2}=\frac{N_ce_Q^2\alpha^2|R(0)|^2}{3m_Q^2}$ | Van Royen–Weisskopf 1967 (recall, $N_c=3$ form $16\pi e_Q^2\alpha^2|\psi(0)|^2/M^2$); BBL: $\Gamma=\frac{N_c{\rm Im}f_{ee}}{\pi M^2}|\bar R|^2$, ${\rm Im}f_{ee}=\frac{\pi Q^2\alpha^2}3$ (read; BBL's $M$ = quark mass) | $M_{\rm meson}=2m_Q$ | PASS |
| 17 | $\Gamma(^1S_0\to\gamma\gamma)=16\pi N_c\frac{e_Q^4\alpha^2|\psi(0)|^2}{M^2}=\frac{4N_ce_Q^4\alpha^2|R(0)|^2}{M^2}$ | BBL ${\rm Im}f_{\gamma\gamma}(^1S_0)=\pi Q^4\alpha^2$ (read); para-positronium $\alpha^5m/2$ | same | PASS |
| 18 | $c_v=1-2C_F\frac{\alpha_s}\pi$ (vertex at threshold $a(\frac3\varepsilon-4+3\ln\frac{\mu^2}{m^2})$, $\delta Z_2^{\rm OS}=-a(\frac3\varepsilon+4+3\ln\frac{\mu^2}{m^2})$) $\Rightarrow$ $\Gamma(V\to e^+e^-)\propto 1-\frac{16\alpha_s}{3\pi}$ | BBL App. A (read): ${\rm Im}f_{ee}=\frac{\pi Q^2\alpha^2}3[1-4C_F\frac{\alpha_s}\pi]$ [Barbieri–Gatto–Kögerler–Kunszt 1975; Celmaster 1979] | $4C_F=16/3$ | PASS |
| 19 | QCDF formula; $V_M=12\ln\frac{m_b}\mu-18+\int g\Phi_M$; $12$ forced by $\mu$-independence of $a_{1,2}$ for any $N_c$ | BBNS 2001 eqs. (ai), (FM) (read) | none | PASS |
| 20 | $\int_0^1g\,\Phi_M=-\frac12-3i\pi+(\frac{11}2-3i\pi)\alpha_1^M-\frac{21}{20}\alpha_2^M$ | BBNS 2001 eq. (vgegenb) (read) | Gegenbauer convention of BBNS | PASS ($10^{-20}$) |
| 21 | $X_H=\int_0^1\frac{dy}{1-y}\Phi_p(y)$, $X_A=\int_0^1\frac{dy}y$ (divergent); $X=(1+\varrho e^{i\varphi})\ln\frac{m_B}{\Lambda_h}$, $\varrho\le1$, $\Lambda_h=0.5$ GeV | BBNS 2001 (Xdef),(XHparam),(XAparam); BN 2003 (read) | none | PASS |
| 22 | $A_1^i\approx\pi\alpha_s[18(X_A-4+\frac{\pi^2}3)+2r_\chi^2X_A^2]$, $A_3^f\approx12\pi\alpha_sr_\chi(2X_A^2-X_A)$, $A_3^i$ $r_1$-term $6\pi\alpha_sr_1(X_A^2-2X_A+\frac{\pi^2}3)$ (re-derived from the integrands) | BBNS 2001 (XAdef); BN 2003 (XAmodel) (read) | BN: $2\pi\alpha_s[9(\dots)+r_1r_2X_A^2]$ | PASS |
| 23 | $B\to D\pi$ at leading power, all orders in $\alpha_s$: $\langle D\pi|O|B\rangle=N F^{B\to D}(0)\int_0^1dx\,T(x,\mu)\phi_\pi(x,\mu)$, $N=\frac i2m_BE_\pi f_\pi$ | BPS 2001 (read) | — | statement verified |
| 24 | massless particles: $\frac{M_L^2+M_R^2}{Q^2}=\tau-\frac{\tau^2}2+\frac{(M_R^2-M_L^2)^2}{2Q^4}$ exactly, so $\tau=\frac{M_L^2+M_R^2}{Q^2}+O(\tau^2)$; $=\tau$ exactly for 3 partons | (derived; standard) | — | PASS ($3\times10^{-16}$) |
| 25 | one-loop jet function: projected $|M|^2=\frac{4\bar n\cdot p}{p^2}\big[\frac{1+(1-x)^2}x-\varepsilon x\big]=\frac{4\bar n\cdot p}{p^2}\frac{P_{gq}(x)}{C_F}$ ($D$ dims), $\int_0^1(x\bar x)^{-\varepsilon}[\dots]=-\frac{(4-\varepsilon)(1-\varepsilon)}{2\varepsilon(1-2\varepsilon)}\frac{\Gamma^2(1-\varepsilon)}{\Gamma(1-2\varepsilon)}$ | consistency with row 9 | — | PASS (exact) |

---------------------------------------------------------------------------------------------------------------------

## 1. Conventions

**Light-cone vectors (CONTEXT.md, SCET chapter only).** $n=(1,0,0,1)$, $\bar n=(1,0,0,-1)$, $n^2=\bar n^2=0$, $n\cdot\bar n=2$;
$$p^\mu=\bar n\!\cdot\!p\,\frac{n^\mu}{2}+n\!\cdot\!p\,\frac{\bar n^\mu}2+p_\perp^\mu,\qquad \bar n\!\cdot\!p=\sqrt2\,p^+,\quad n\!\cdot\!p=\sqrt2\,p^-,$$
$$p\cdot q=\tfrac12(\bar n\!\cdot\!p\,n\!\cdot\!q+n\!\cdot\!p\,\bar n\!\cdot\!q)+p_\perp\!\cdot q_\perp=p^+q^-+p^-q^+-\boldsymbol p_T\!\cdot\boldsymbol q_T,\qquad p^2=\bar n\!\cdot\!p\,n\!\cdot\!p+p_\perp^2,\ p_\perp^2=-\boldsymbol p_T^2 .$$
(`s1` A, all PASS.) An $n$-collinear particle moves along $+z$ (large $p^+$). It is the "A-collinear" particle of CONTEXT.md.

**Ordering of scalings.** As in the task, scalings are written for $(\bar n\!\cdot\!p,\ n\!\cdot\!p,\ p_\perp)$, so $n$-collinear $=Q(1,\lambda^2,\lambda)$.
The blueprint (D14.1) and Rothstein–Stewart use $(n\!\cdot\!p,\bar n\!\cdot\!p,p_\perp)$, in which $n$-collinear reads $Q(\lambda^2,1,\lambda)$.
The writer must state the ordering once and convert all quotations accordingly.

**Projectors.** $P_n=\frac{\slashed n\bar{\slashed n}}4$, $P_{\bar n}=\frac{\bar{\slashed n}\slashed n}4$, $P_n^2=P_n$, $P_n+P_{\bar n}=1$, $P_nP_{\bar n}=0$,
$\slashed nP_n=0$, $\gamma^0P_n^\dagger\gamma^0=P_{\bar n}$. Hence $\xi_n=P_n\psi$ satisfies $\slashed n\xi_n=0$ and $\bar\xi_n=\bar\psi P_{\bar n}$.
(`s1` B.)

**Wilson lines** (CONTEXT: $W[b,a]=P\exp(ig\int_a^bdz\cdot A)$, later points to the left, $W\to U(b)WU^\dagger(a)$):
$$W_n(x)\equiv W[x,x-\infty\bar n]=P\exp\Big(ig\!\int_{-\infty}^0\!ds\;\bar n\!\cdot\!A_n(x+s\bar n)\Big),\qquad
Y_n(x)\equiv W[x,x-\infty n]=P\exp\Big(ig\!\int_{-\infty}^0\!ds\;n\!\cdot\!A_{us}(x+sn)\Big),$$
and the future-pointing version $Y_n^{(+)}(x)\equiv W[x,x+\infty n]=\big(W[x+\infty n,x]\big)^\dagger$. All of them satisfy
$v\cdot D\,W=0$ along their direction $v$, in the sense $\partial_sW(x+sv)=ig\,v\!\cdot\!A\,W$ (`s1_wilson` A2).

**Distributions.** Star distributions (jet: reference $\mu^2$; soft: reference $\mu$):
$\int_0^{\mu^2}\!dp^2\,\big[\frac{\ln^k(p^2/\mu^2)}{p^2}\big]_*f(p^2)=\int_0^{\mu^2}\!dp^2\,\frac{\ln^k(p^2/\mu^2)}{p^2}[f(p^2)-f(0)]$. Above $\mu^2$ they are ordinary functions.
Identity: $\mu^{2\varepsilon}(p^2)^{-1-\varepsilon}=-\frac{\delta(p^2)}\varepsilon+\sum_{k\ge0}\frac{(-\varepsilon)^k}{k!}\big[\frac{\ln^k(p^2/\mu^2)}{p^2}\big]_*$.
For the soft function, $\mu^{2\varepsilon}k^{-1-2\varepsilon}=-\frac{\delta(k)}{2\varepsilon}+\sum_k\frac{(-2\varepsilon)^k}{k!}\big[\frac{\ln^k(k/\mu)}{k}\big]_*$.
**In $\tau$-space the plus distributions subtract at $\tau=0$:** $\int_0^1d\tau\,[g(\tau)]_+h(\tau)=\int_0^1d\tau\,g(\tau)[h(\tau)-h(0)]$.
CONTEXT.md's plus distribution subtracts at $z=1$ (DGLAP), so the writer must state which endpoint is meant (see §6).

**Laplace transforms** (Becher–Schwartz convention, read): $\tilde t(\nu)=\int_0^\infty d\tau\,e^{-\nu\tau}\frac1{\sigma_0}\frac{d\sigma}{d\tau}$, $s\equiv1/(e^{\gamma_E}\nu)$,
$L_Q=\ln\frac{Q^2}{\mu^2}$, $L_J=\ln\frac{sQ^2}{\mu^2}$, $L_S=\ln\frac{sQ}{\mu}$. With $\ell\equiv\ln(\nu e^{\gamma_E})=\ln(1/s)$: $L_J=L_Q-\ell$ and $L_S=\frac12L_Q-\ell$.

**$\overline{\rm MS}$:** $g_0^2=4\pi\alpha_s\mu^{2\varepsilon}e^{\varepsilon\gamma_E}(4\pi)^{-\varepsilon}$. $\mu_0$ denotes the bare scale ($g_0^2=4\pi\alpha_s\mu_0^{2\varepsilon}$).
Anomalous dimensions are expanded as $\Gamma_{\rm cusp}=\sum_n(\frac{\alpha_s}{4\pi})^{n+1}\Gamma_n$, and similarly $\gamma^{H,J,S}$ (Becher–Schwartz).
$\beta$: $\mu^2d\alpha_s/d\mu^2=-\frac{\beta_0}{4\pi}\alpha_s^2$ (CONTEXT), $b\equiv\beta_0/(4\pi)$.

---------------------------------------------------------------------------------------------------------------------

## 2. Part (1): SCET$_{\rm I}$, SCET$_{\rm II}$

### 2.1 Modes, virtualities, interactions (`s1` E)

| mode | $(\bar n\!\cdot\!p,\ n\!\cdot\!p,\ p_\perp)/Q$ | $p^2$ | fields | appears in |
|---|---|---|---|---|
| hard | $(1,1,1)$ | $Q^2$ | integrated out (Wilson coefficients) | matching |
| $n$-collinear | $(1,\lambda^2,\lambda)$ | $\lambda^2Q^2$ | $\xi_n\sim\lambda$; $(\bar n\!\cdot\!A_n,n\!\cdot\!A_n,A_{n\perp})\sim(1,\lambda^2,\lambda)$ | I, II |
| $\bar n$-collinear | $(\lambda^2,1,\lambda)$ | $\lambda^2Q^2$ | $\xi_{\bar n}\sim\lambda$ | I, II |
| ultrasoft | $(\lambda^2,\lambda^2,\lambda^2)$ | $\lambda^4Q^2$ | $q_{us}\sim\lambda^3$, $A_{us}\sim\lambda^2$ | I |
| soft | $(\lambda,\lambda,\lambda)$ | $\lambda^2Q^2$ | $q_s\sim\lambda^{3/2}$, $A_s\sim\lambda$ | II |
| hard-collinear | $(1,\lambda,\lambda^{1/2})$ | $\lambda Q^2$ | integrated out in SCET$_{\rm I}\to$SCET$_{\rm II}$ | intermediate |
| Glauber $n$–$\bar n$ | $(\lambda^2,\lambda^2,\lambda)$ | $\simeq-\boldsymbol q_T^2\sim\lambda^2Q^2$, $n\!\cdot\!q\,\bar n\!\cdot\!q\sim\lambda^4$ | off-shell potential | I, II |
| Glauber $n$–$s$ | $(\lambda,\lambda^2,\lambda)$ | $\lambda^2Q^2$, $n\!\cdot\!q\,\bar n\!\cdot\!q\sim\lambda^3$ | off-shell | II |
| Glauber $\bar n$–$s$ | $(\lambda^2,\lambda,\lambda)$ | as above | off-shell | II |

Derivation of the field scalings: require $\int d^4x\,e^{ip\cdot x}\langle0|T\phi(x)\phi(0)|0\rangle\sim$ propagator. Equivalently,
$\langle\phi\phi\rangle\sim\int d^4p\times(\text{propagator})$:
* collinear quark: $d^4p\sim\lambda^4$, $\frac{\slashed n}2\frac{\bar n\cdot p}{p^2}\sim\lambda^{-2}$, so $\xi_n\sim\lambda$;
* collinear gluon: the gauge term $p^\mu p^\nu/p^4$ gives $A^\mu A^\nu\sim p^\mu p^\nu$, so $A_n^\mu\sim p^\mu$. The Feynman-gauge term alone gives $\langle\bar n\!\cdot\!A\,\bar n\!\cdot\!A\rangle\propto\bar n^2=0$, which is why the gauge term is needed to see $\bar n\!\cdot\!A_n\sim1$;
* usoft: $d^4k\sim\lambda^8$, so $A_{us}\sim\lambda^2$ and $q_{us}\sim\lambda^3$; soft: $d^4k\sim\lambda^4$, so $A_s\sim\lambda$ and $q_s\sim\lambda^{3/2}$.

Each term of the LO collinear Lagrangian scales as $\lambda^4$. Since the collinear measure is $d^4x\sim\lambda^{-4}$, the action is $O(\lambda^0)$.
For usoft fields the corresponding numbers are $\lambda^8$ and $d^4x\sim\lambda^{-8}$.

Interactions (does mode X absorbing momentum of mode Y stay on its mass shell?):
* $n$-coll + usoft: $(p+k)^2\sim\lambda^2$, so it stays collinear and usoft gluons couple in the SCET$_{\rm I}$ Lagrangian;
* $n$-coll + soft: $(p+k)^2\simeq\bar n\!\cdot\!p\,n\!\cdot\!k\sim\lambda Q^2$, which is **hard-collinear**. The intermediate line is integrated out, giving soft Wilson lines $S_n$ in SCET$_{\rm II}$ operators;
* $n$ + $\bar n$: $p^2\sim Q^2$, hard;
* Glauber exchanges keep both collinear sectors (and soft) on shell. They are not propagating modes, since $q^2\simeq-\boldsymbol q_T^2\gg n\!\cdot\!q\,\bar n\!\cdot\!q$, and so they act as instantaneous ($x^\pm$-local) potentials $\propto1/\boldsymbol q_T^2$ (RS 2016, read).

**Multipole expansion.** For collinear $x$ we have $(n\!\cdot\!x,\bar n\!\cdot\!x,x_\perp)\sim(1,\lambda^{-2},\lambda^{-1})$, so
$k_{us}\!\cdot x=\frac12n\!\cdot\!k\,\bar n\!\cdot\!x\,[O(1)]+k_\perp\!\cdot x_\perp\,[O(\lambda)]+\frac12\bar n\!\cdot\!k\,n\!\cdot\!x\,[O(\lambda^2)]$.
Hence $A_{us}(x)=A_{us}(x_-)+O(\lambda)$ with $x_-^\mu\equiv\bar n\!\cdot\!x\,\frac{n^\mu}2$. In momentum space,
$(p_c+k_{us})^2=\bar n\!\cdot\!p\,(n\!\cdot\!p+n\!\cdot\!k)+p_\perp^2+O(\lambda^3)$: only $n\!\cdot\!k_{us}$ enters at LO (`s1` E, PASS).

### 2.2 The leading collinear quark Lagrangian (`s1` B–D)

With $\psi=\xi_n+\phi_{\bar n}$, $\xi_n=P_n\psi$, $\phi_{\bar n}=P_{\bar n}\psi$, one has the exact identities
$P_{\bar n}\slashed DP_n=n\!\cdot\!D\,\frac{\bar{\slashed n}}2P_n$, $P_n\slashed DP_{\bar n}=\bar n\!\cdot\!D\,\frac{\slashed n}2P_{\bar n}$,
$P_{\bar n}\slashed DP_{\bar n}=\slashed D_\perp P_{\bar n}$, $P_n\slashed DP_n=\slashed D_\perp P_n$. Therefore
$$\bar\psi\,i\slashed D\,\psi=\bar\xi_n\frac{\bar{\slashed n}}2in\!\cdot\!D\,\xi_n+\bar\xi_n\,i\slashed D_\perp\phi_{\bar n}+\bar\phi_{\bar n}\,i\slashed D_\perp\xi_n+\bar\phi_{\bar n}\frac{\slashed n}2i\bar n\!\cdot\!D\,\phi_{\bar n}.$$
The field equation of $\phi$ (vary $\bar\phi$) is $\frac{\slashed n}2i\bar n\!\cdot\!D\,\phi+i\slashed D_\perp\xi=0$, so $\phi_{\bar n}=-\frac1{i\bar n\cdot D}\frac{\bar{\slashed n}}2i\slashed D_\perp\xi_n$.
(On shell, $P_{\bar n}u(p)=-\frac1{\bar n\cdot p}\frac{\bar{\slashed n}}2\slashed p_\perp P_nu(p)$ was checked.) Inserting it, and using that $\bar{\slashed n}$ anticommutes with $\slashed D_\perp$,
$$\boxed{\ \mathcal L_{\xi\xi}=\bar\xi_n\Big[in\!\cdot\!D+i\slashed D_\perp\frac1{i\bar n\!\cdot\!D}\,i\slashed D_\perp\Big]\frac{\bar{\slashed n}}2\,\xi_n\ }\qquad(\text{exact at tree level}).$$
Free-field check: the operator equals $(p^2/\bar n\!\cdot\!p)\frac{\bar{\slashed n}}2$ on $P_n$-space, and the $\xi$ propagator is
$P_n\frac{i\slashed p}{p^2}P_{\bar n}=i\frac{\slashed n}2\frac{\bar n\cdot p}{p^2+i0}$, exactly off shell.

Leading power with $A=A_n+A_{us}$: in $in\!\cdot\!D$ all three pieces are $O(\lambda^2)$, while in $i\bar n\!\cdot\!D$ and $iD_\perp$ the usoft parts are suppressed. Hence
$$\mathcal L^{(0)}_{\xi\xi}=\bar\xi_n\Big[in\!\cdot\!D+i\slashed D_{\perp c}\,W_n\frac1{\bar{\mathcal P}}W_n^\dagger\,i\slashed D_{\perp c}\Big]\frac{\bar{\slashed n}}2\xi_n,\quad
in\!\cdot\!D=in\!\cdot\!\partial+gn\!\cdot\!A_n+gn\!\cdot\!A_{us}(x_-),\ \ iD^\mu_{\perp c}=i\partial^\mu_\perp+gA^\mu_{n\perp},$$
where $\frac1{i\bar n\cdot D_c}=W_n\frac1{i\bar n\cdot\partial}W_n^\dagger$ follows from $i\bar n\!\cdot\!D_c\,W_n=W_n\,i\bar n\!\cdot\!\partial$ (§2.3).
(In label notation, $i\partial_\perp\to\mathcal P_\perp$ and $i\bar n\!\cdot\!\partial\to\bar{\mathcal P}$ act on labels. This is BPS 2002 eq. (Lcq), read.)

Feynman rules (our conventions; `s1` D verifies that the vertex below satisfies the **exact** tree identity
$P_nS_{\rm QCD}(p')(ig\gamma^\mu)S_{\rm QCD}(p)P_{\bar n}=S_\xi(p')V^\mu S_\xi(p)$ off shell):
* collinear propagator $i\frac{\slashed n}2\frac{\bar n\cdot p}{p^2+i0}$;
* ultrasoft gluon: $ig\,t^a\,n^\mu\frac{\bar{\slashed n}}2$;
* collinear gluon (quark $p\to p'$): $ig\,t^a\big[n^\mu+\frac{\gamma_\perp^\mu\slashed p_\perp}{\bar n\cdot p}+\frac{\slashed p'_\perp\gamma_\perp^\mu}{\bar n\cdot p'}-\frac{\slashed p'_\perp\slashed p_\perp}{\bar n\cdot p\,\bar n\cdot p'}\bar n^\mu\big]\frac{\bar{\slashed n}}2$,
  with $\gamma_\perp^\mu=\gamma^\mu-n^\mu\frac{\bar{\slashed n}}2-\bar n^\mu\frac{\slashed n}2$.

### 2.3 Collinear Wilson line $W_n$ (`s1_wilson` A, B, C)

* Definition: §1. It is unitary and unimodular, $W[s_2,s_0]=W[s_2,s_1]W[s_1,s_0]$ (later points left; the reversed order fails), and its $O(g^2)$ term is
  $(ig)^2\int_{s_1>s_2}a(s_1)a(s_2)$ (all checked numerically for random su(3) backgrounds).
* $(\bar n\!\cdot\!\partial-ig\bar n\!\cdot\!A_n)W_n=0$, i.e. $\bar n\!\cdot\!D_cW_n=0$, hence $W_n^\dagger\,i\bar n\!\cdot\!D_c\,W_n=i\bar n\!\cdot\!\partial$.
* Gauge covariance: under $A'=UAU^\dagger-\frac ig(\partial U)U^\dagger$ (the law for $D=\partial-igA$), $W'[b,a]=U(b)W[b,a]U^\dagger(a)$ (checked, error $4\times10^{-10}$).
  For collinear gauge transformations that vanish at infinity, $W_n\to U_c(x)W_n$, so $\chi_n\equiv W_n^\dagger\xi_n$ and
  $\mathcal B^\mu_{n\perp}\equiv\frac1g[W_n^\dagger iD^\mu_{n\perp}W_n]$ are collinear gauge invariant (Bauer–Stewart 2001).
* Momentum space: $W_n=\sum_{\rm perms}\exp\big[-\frac g{\bar{\mathcal P}}\bar n\!\cdot\!A_n\big]$ (BPS 2001 eq. (W), read), consistent with:
  absorbing a gluon (field $\propto e^{-ik\cdot y}$) gives $ig\int_{-\infty}^0ds\,e^{-is\bar n\cdot k+0s}=-\frac{g}{\bar n\cdot k+i0}$, and
  creating an outgoing gluon gives $+\frac{g\,\bar n\cdot\varepsilon^*}{\bar n\cdot k-i0}$. Both coincide with the blueprint §0.4(10) past-pointing rule
  $(ig\bar n^\mu)\frac i{\bar n\cdot k+i0}$.
* **Origin (tree-level matching).** In $\gamma^*\to q(p_1)\bar q(p_2)g(k)$ with $k\parallel p_1$ ($n$) and $p_2$ along $\bar n$, the diagram with the gluon on the
  antiquark has $(p_2+k)^2\simeq n\!\cdot\!p_2\,\bar n\!\cdot\!k\sim Q^2$. At leading power it equals $\bar u\gamma^\mu v\cdot g\,\bar n\!\cdot\!\varepsilon^*/\bar n\!\cdot\!k$, which is the $W_n$ rule
  (relative error $1.0\times10^{-1}$, $9.6\times10^{-3}$, $9.5\times10^{-4}$ at $\lambda=10^{-1,-2,-3}$). The full amplitude equals the SCET amplitude of
  $J^\mu=\bar\xi_nW_n\gamma_\perp^\mu W_{\bar n}^\dagger\xi_{\bar n}$, using the collinear LO vertex plus the $W_n$ term, up to $O(\lambda)$. For $\varepsilon^*=k$ the QCD sum vanishes,
  and in SCET the collinear term $-gt^a\bar u\gamma^\mu v$ is cancelled exactly by the $W_n$ term $+gt^a\bar u\gamma^\mu v$ (collinear gauge invariance).

### 2.4 Ultrasoft decoupling (BPS 2002) — statement and proof

**Key identity.** $n\!\cdot\!\partial\,Y_n(x)=ig\,n\!\cdot\!A_{us}(x)Y_n(x)$, i.e. $n\!\cdot\!D_{us}Y_n=0$ as a function. As an operator identity this means, for any $f$,
$$in\!\cdot\!D_{us}\,(Y_nf)=(in\!\cdot\!\partial+gn\!\cdot\!A_{us})(Y_nf)=-gn\!\cdot\!A_{us}Y_nf+Y_n\,in\!\cdot\!\partial f+gn\!\cdot\!A_{us}Y_nf=Y_n\,in\!\cdot\!\partial f ,$$
so $Y_n^\dagger\,in\!\cdot\!D_{us}\,Y_n=in\!\cdot\!\partial$. This was verified numerically, with path ordering, for random su(3) fields (error $2\times10^{-10}$, `s1_wilson` A5).
Also $Y_n^\dagger(in\!\cdot\!\partial+gn\!\cdot\!A_{us}+gn\!\cdot\!A_n)Y_n=in\!\cdot\!\partial+gn\!\cdot\!A_n^{(0)}$ for $A_n=Y_nA_n^{(0)}Y_n^\dagger$ (A6).

**Theorem (LO ultrasoft decoupling).** Let $Y_n$ be built from $n\!\cdot\!A_{us}(x_-)$ (multipole expanded). The field redefinitions
$$\xi_n=Y_n\,\xi_n^{(0)},\qquad A_n^\mu=Y_nA_n^{(0)\mu}Y_n^\dagger,\qquad c_n=Y_nc_n^{(0)}Y_n^\dagger\ \ (\text{collinear ghosts})$$
give
$\mathcal L^{(0)}_{\xi\xi}[\xi_n,A_n,n\!\cdot\!A_{us}]+\mathcal L^{(0)}_{cg}[A_n,c_n,n\!\cdot\!A_{us}]=\mathcal L^{(0)}_{\xi\xi}[\xi_n^{(0)},A_n^{(0)},0]+\mathcal L^{(0)}_{cg}[A^{(0)}_n,c^{(0)}_n,0]$,
**provided the collinear gauge-fixing term is covariant under usoft gauge transformations** (background-field gauge with $A_{us}$ as
background, $\frac1\alpha{\rm tr}\{[i\mathcal D_\mu,A_n^\mu]\}^2$, $i\mathcal D^\mu=\frac{n^\mu}2\bar{\mathcal P}+\mathcal P_\perp^\mu+\frac{\bar n^\mu}2in\!\cdot\!D_{us}$; BPS 2002, read: "it is crucial that the
derivative in the $1/\alpha$ gauge fixing term … is covariant with respect to the usoft $n\cdot A_{us}$ background field").

*Proof (quark part).* (i) $Y_n$ depends only on $x_-$, so it commutes with the label operators $\mathcal P_\perp,\bar{\mathcal P}$. Its derivatives are $O(\lambda^2)$, which is power suppressed against
$\mathcal P_\perp\sim\lambda$ and $\bar{\mathcal P}\sim1$. Hence $Y^\dagger iD_{\perp c}Y=iD^{(0)}_{\perp c}$ and $W_n[YA^{(0)}Y^\dagger]=YW_n^{(0)}Y^\dagger$ (A8).
(ii) By the key identity, $Y^\dagger in\!\cdot\!D\,Y=in\!\cdot\!\partial+gn\!\cdot\!A_n^{(0)}$. (iii) The colour matrices $Y$ commute with Dirac matrices. Therefore
$\bar\xi_n[\dots]\frac{\bar{\slashed n}}2\xi_n=\bar\xi^{(0)}_n\big[in\!\cdot\!\partial+gn\!\cdot\!A^{(0)}_n+i\slashed D^{(0)}_{\perp c}W^{(0)}_n\frac1{\bar{\mathcal P}}W^{(0)\dagger}_ni\slashed D^{(0)}_{\perp c}\big]\frac{\bar{\slashed n}}2\xi^{(0)}_n$.
*Gluon and ghost part:* $i\mathcal D^\mu+gA_n^\mu=Y(i\mathcal D^\mu_{(0)}+gA_n^{(0)\mu})Y^\dagger$, so commutators, the usoft-covariant gauge-fixing term and the ghost term all transform by conjugation, and the traces are invariant.
*Jacobian:* $Y$ is unitary and independent of the collinear fields, so the Jacobian is 1 (fermions: $\det Y=1$; gluons and ghosts: an orthogonal adjoint rotation). $\square$

*Consequences.* Usoft gluons survive only in operators, through $Y$:
$\bar\xi_nW_n\Gamma W^\dagger_{\bar n}\xi_{\bar n}=\bar\chi^{(0)}_nY_n^\dagger\Gamma Y_{\bar n}\chi^{(0)}_{\bar n}$. The matrix element then factorizes into
(n-collinear)$\times$($\bar n$-collinear)$\times\langle Y^\dagger Y\rangle$, which is the origin of $H\,J\otimes J\otimes S$.

*Limitations.* (a) The decoupling holds at **leading power only**: subleading usoft couplings cannot be written solely as factors of $Y$ (BPS 2002, read).
(b) As a statement about QCD it requires that SCET reproduce the IR of QCD (mode completeness, zero-bin subtractions, Glauber).

*Direction and $i0$ of $Y$.* The Lagrangian proof uses only $n\!\cdot\!DY=0$, which holds for $Y_n$ and for $Y_n^{(+)}$ alike.
For an **outgoing** on-shell collinear quark the LO Feynman rules give, for one usoft gluon **absorbed** by the line ($k$ flowing into it), $\bar u_n\,g\,t^an\!\cdot\!\varepsilon/(n\!\cdot\!k-i0)$; for one gluon **emitted** with outgoing momentum $k$ they give $-\bar u_n\,g\,t^an\!\cdot\!\varepsilon^*/(n\!\cdot\!k+i0)$ (the same rule with inflow $-k$; `s1_wilson` B2'); for two absorbed gluons,
$g^2\big[\frac{t^bt^a}{(n\cdot(k_1+k_2)-i0)(n\cdot k_2-i0)}+(a,k_1\leftrightarrow b,k_2)\big]$ (`s1_wilson` B2). This is the expansion of the **future-pointing** line
$W[x+\infty n,x]=Y_n^{(+)\dagger}$, identical to the blueprint §0.4(10) future-pointing rule. If $Y_n$ is taken from $-\infty$, as in BPS and BS, the eikonal denominators carry
$+i0$. The imaginary parts of individual amplitudes then differ (Chay–Kim–Kim–Lee 2005, abstract). This does not affect the one-loop thrust soft function: the
virtual graphs are scaleless, and real emission has $n\!\cdot\!k,\bar n\!\cdot\!k>0$. Hemisphere soft functions for $e^+e^-$, DIS and DY are equal up to
$O(\alpha_s^2)$ (Kang–Labun–Lee 2015, abstract). RS 2016 (read) state the general rule: "Ultrasoft Wilson line directions in SCET$_{\rm I}$ are determined by the
physical directions since their diagrams do not have subtractions", whereas for soft and collinear Wilson lines the direction dependence is cancelled by (Glauber) 0-bin subtractions.

### 2.5 SCET$_{\rm II}$, soft Wilson lines, rapidity divergences, Glauber

In SCET$_{\rm II}$ the collinear modes $(1,\lambda^2,\lambda)$ and the soft modes $(\lambda,\lambda,\lambda)$ have the same virtuality $\lambda^2Q^2$. A soft gluon attached
to a collinear line produces $(p_c+k_s)^2\simeq\bar n\!\cdot\!p_c\,n\!\cdot\!k_s\sim\lambda Q^2$. This hard-collinear line is integrated out, either in one step or through
QCD $\to$ SCET$_{\rm I}$(hard-collinear + soft) $\to$ SCET$_{\rm II}$ (Hill–Neubert 2003; Bauer–Fleming–Pirjol–Rothstein–Stewart 2002).
What remains is the eikonal factor $\propto n\!\cdot\!\varepsilon/n\!\cdot\!k_s$, i.e. the soft Wilson line $S_n=P\exp(ig\int_{-\infty}^0ds\,n\!\cdot\!A_s(x+sn))$ in the operators
(`s1_wilson` D: relative error $7.7\times10^{-1,-2,-3}$ for $\lambda=10^{-1,-2,-3}$).
Because soft and collinear modes are separated only in rapidity, individual SCET$_{\rm II}$ integrals have **rapidity divergences** that dimensional regularization does not
regulate. Rapidity regulators are needed: the rapidity RG (Chiu–Jain–Neill–Rothstein 2012), the collinear anomaly (Becher–Neubert 2011), or Collins' non-light-like
lines (Ch. 11).
**Glauber modes** are absent from the standard SCET Lagrangians. Rothstein–Stewart 2016 (abstract, read) derive Glauber operators coupling the $n$, $\bar n$ and soft
sectors. Glauber exchange "can induce corrections which invalidate factorization", and for hard-scattering operators "Glauber subtractions for soft and collinear loop
diagrams ensure that we are not sensitive to the directions for soft and collinear Wilson lines". A factorization proof must therefore show that Glauber contributions cancel
(e.g. $e^+e^-\to$ dijets, inclusive DY) or are absent. This is the EFT version of hypothesis (GLAU) of the blueprint.

### 2.6 Status (Ch. 14, first half)
* D14.1 modes: definition. The claim that the listed modes are **complete** for a given observable is the leading-region analysis of Ch. 3: [A].
* D14.2 $\mathcal L_{\xi\xi}$: tree-level derivation [R] (exact identity, verified); power counting [R].
* P14.3 $W_n$ from integrating out off-shell modes: [R] at tree level (one gluon verified numerically; all orders by the induction of BFPS 2001).
* T14.5 LO decoupling: [R] as an identity of the LO SCET Lagrangian, with the conditions above (usoft-covariant gauge fixing, ghosts redefined); [A] as a statement about QCD.

---------------------------------------------------------------------------------------------------------------------

## 3. Part (2): thrust factorization $d\sigma/d\tau=H\,J\otimes J\otimes S$

### 3.1 Statement and definitions
For $\tau=1-T\ll1$, at leading power (BS 2008 eq. (scetfact), read; BLMW 2004; Schwartz 2008):
$$\frac1{\sigma_0}\frac{d\sigma}{d\tau}=H(Q^2,\mu)\int dp_L^2\,dp_R^2\,dk\;J(p_L^2,\mu)\,J(p_R^2,\mu)\,S_T(k,\mu)\;\delta\Big(\tau-\frac{p_L^2+p_R^2}{Q^2}-\frac kQ\Big)\;+\;(\text{terms integrable at }\tau\to0).$$
Kinematics (derived, `s2_rg`): for massless particles $\frac{M_L^2+M_R^2}{Q^2}=\tau-\frac{\tau^2}2+\frac{(M_R^2-M_L^2)^2}{2Q^4}$ exactly (thrust axis along a hemisphere
momentum), hence $\tau=(M_L^2+M_R^2)/Q^2+O(\tau^2)$, and $=\tau$ exactly for three partons; checked on random 3- and 4-parton events to $3\times10^{-16}$.
Equivalently, for the two hemisphere masses at leading power,
$\frac{d^2\sigma}{dM_L^2dM_R^2}=\sigma_0H\int dk_Ldk_R\,J(M_L^2-Qk_L)J(M_R^2-Qk_R)S_{\rm hemi}(k_L,k_R)$, with
$\tau=(M_L^2+M_R^2)/Q^2$ and $S_T(k)=\int dk_Ldk_R\,\delta(k-k_L-k_R)S_{\rm hemi}$ (BLMW 2004; Korchemsky–Sterman 1999, abstract).
* $H=|C_V(-Q^2-i0,\mu)|^2$, where $C_V$ is the matching coefficient of $\bar\psi\gamma^\mu\psi\to C_V\,\bar\chi_{\bar n}\gamma^\mu_\perp\chi_n$.
* Jet function (cut form used here): $\sum_X(2\pi)^D\delta^D(p-p_X)\langle0|\chi_n|X\rangle\langle X|\bar\chi_n|0\rangle=2\pi\frac{\slashed n}2\,\bar n\!\cdot\!p\,J(p^2)\,\mathbb 1_c$, so that $J^{(0)}=\delta(p^2)$.
  BS 2008 (read, re-checked) write $J(p^2)=\frac1{\bar n\cdot p}\frac1\pi{\rm Im}\big[i\int d^4x\,e^{-ipx}\langle0|T\{\bar\chi_n(x)\frac{\bar{\slashed n}}2\chi_n(0)\}|0\rangle\big]=\delta(p^2)+O(\alpha_s)$ **without explicit
  Dirac/colour normalization**: read literally (fermionic $T$-ordering sign, Dirac and colour traces) the free field gives $-2N_c\,\delta(p^2)$, so a factor $-\frac1{2N_c}{\rm tr}$ is
  implicit. **The writer must not copy that formula literally**; the cut definition above is normalized explicitly ($J^{(0)}=\delta(p^2)$, verified).
* Soft function: $S_T(k)=\frac1{N_c}\sum_X{\rm tr}\big|\langle X|Y^\dagger_nY_{\bar n}|0\rangle\big|^2\delta(k-n\!\cdot\!p_{X_R}-\bar n\!\cdot\!p_{X_L})$. Here $X_R$ ($X_L$) are the soft particles in the
  $n$ ($\bar n$) hemisphere (BS, read). At $O(\alpha_s)$ the choice of $i0$ of $Y$ is irrelevant (§2.4).

### 3.2 Hard function from the massless form factor (`s2_oneloop` (i))
Feynman gauge: $\delta\Gamma^\mu=-ig^2C_F\mu_0^{2\varepsilon}\int\frac{d^Dk}{(2\pi)^D}\frac{\gamma^\alpha(\slashed p_2-\slashed k)\gamma^\mu(\slashed p_1-\slashed k)\gamma_\alpha}{k^2(k-p_2)^2(k-p_1)^2}$, with
$F^{(1)}={\rm Tr}[\slashed p_2\delta\Gamma^\mu\slashed p_1\gamma_\mu]/{\rm Tr}[\slashed p_2\gamma^\mu\slashed p_1\gamma_\mu]$. This projection is exact for massless quarks: chirality allows only $\gamma^\mu$.
Feynman parameters: $\Delta=xyQ^2$, $Q^2=-q^2=2p_1\!\cdot\!p_2$. Exact result:
$$F^{(1)}_{\rm bare}=\frac{\alpha_sC_F}{4\pi}\Big(\frac{4\pi\mu_0^2}{Q^2}\Big)^{\varepsilon}\frac{\Gamma(1+\varepsilon)\Gamma^2(1-\varepsilon)}{\Gamma(1-2\varepsilon)}\Big[-\frac{2-\varepsilon+2\varepsilon^2}{\varepsilon^2(1-2\varepsilon)}\Big]
=\dots\Big[-\frac2{\varepsilon^2}-\frac3\varepsilon-8-16\varepsilon+O(\varepsilon^2)\Big].$$
In $\overline{\rm MS}$ at $\mu^2=Q^2$ the bracket is $-\frac2{\varepsilon^2}-\frac3\varepsilon-8+\zeta_2+\varepsilon(-16+\frac32\zeta_2+\frac{14}3\zeta_3)$, identical to the c_dis agent's result.
On-shell SCET graphs are scaleless, so the IR poles of $F$, $-\frac2{\varepsilon^2}+\frac{2L-3}\varepsilon$, are the UV poles of the SCET current, and
$$C_V(-q^2,\mu)=1+\frac{\alpha_sC_F}{4\pi}\Big[-L^2+3L-8+\zeta_2\Big],\quad L=\ln\frac{-q^2-i0}{\mu^2},\qquad \frac{dC_V}{d\ln\mu}=[\Gamma_{\rm cusp}L+\gamma^V]C_V,\ \Gamma_0=4C_F,\ \gamma^V_0=-6C_F.$$
Timelike $q^2=Q^2$: $L=L_Q-i\pi$, so
$$\boxed{H(Q^2,\mu)=1+\frac{\alpha_sC_F}{4\pi}\Big[-2L_Q^2+6L_Q-16+\frac{7\pi^2}3\Big]},\qquad\frac{dH}{d\ln\mu}=\big[2\Gamma_{\rm cusp}L_Q+2\gamma^H\big]H,\ \gamma^H=\gamma^V.$$
BS 2008 (read): $h(L)=1+\frac{\alpha_s}{4\pi}[-\frac12\Gamma_0L^2-\gamma^H_0L+c^H_1]$, $c_1^H=C_F(-16+\frac{7\pi^2}3)$. **PASS.**

### 3.3 Jet function (`s2_oneloop` (ii))
One-loop real emission $q(k_1)g(k_2)$, $p=k_1+k_2$, $x=\bar n\!\cdot\!k_2/\bar n\!\cdot\!p$:
$\langle qg|\bar\chi_n|0\rangle=gt^a\bar u(k_1)\big[-\gamma^\nu\frac{\slashed p}{p^2}+\frac{\bar n^\nu}{\bar n\cdot k_2}\big]P_{\bar n}\varepsilon^*_\nu$. It satisfies the Ward identity, so $-g_{\nu\nu'}$ may be used.
The projected trace (with $+g_{\nu\nu'}$) is $T=-\frac{\bar n\cdot p}{p^2}\big[4(1-\varepsilon)x+8\frac{1-x}x\big]$, i.e. with the physical sum $-g_{\nu\nu'}$
$-T=\frac{4\bar n\cdot p}{p^2}\big[\frac{1+(1-x)^2}x-\varepsilon x\big]=\frac{4\bar n\cdot p}{p^2}\frac{P_{gq}(x)}{C_F}$ ($D$-dim splitting function, `s2_oneloop`), and the $D$-dimensional two-body phase space is $\int d\Phi_2=\frac1{8\pi}(\frac{4\pi}{p^2})^\varepsilon\frac1{\Gamma(1-\varepsilon)}\int_0^1dx\,(x\bar x)^{-\varepsilon}$
(checked against the rest-frame formula, exact in $\varepsilon$). The virtual graphs and the zero-bin are scaleless. Result (exact in $\varepsilon$):
$$J^{(1)}_{\rm bare}(p^2)=-\frac{\alpha_sC_F}{4\pi}(4\pi\mu_0^2)^\varepsilon\,\frac{4-\varepsilon}{\varepsilon}\,\frac{\Gamma(2-\varepsilon)}{\Gamma(2-2\varepsilon)}\,(p^2)^{-1-\varepsilon}.$$
$\overline{\rm MS}$ and distributions: $a\{(\frac4{\varepsilon^2}+\frac3\varepsilon+7-\pi^2)\delta(p^2)-(\frac4\varepsilon+3)[\frac1{p^2}]_*+4[\frac{\ln(p^2/\mu^2)}{p^2}]_*\}$. After minimal subtraction of the poles,
$$\boxed{J(p^2,\mu)=\delta(p^2)+\frac{\alpha_sC_F}{4\pi}\Big\{(7-\pi^2)\delta(p^2)-3\Big[\frac1{p^2}\Big]_*+4\Big[\frac{\ln(p^2/\mu^2)}{p^2}\Big]_*\Big\}},\qquad
\tilde j(L)=1+\frac{\alpha_sC_F}{4\pi}\Big(2L^2-3L+7-\frac{2\pi^2}3\Big),$$
with $\frac{d\tilde j}{d\ln\mu}=[-2\Gamma_{\rm cusp}L-2\gamma^J]\tilde j$ and $\gamma^J_0=-3C_F$. BS (read): $c_1^J=C_F(7-\frac{2\pi^2}3)$, $\gamma^J_0=-3C_F$. **PASS.**
Laplace-space $Z$ poles: $a[\frac4{\varepsilon^2}+\frac{3-4L}\varepsilon]$.

### 3.4 Soft function (`s2_oneloop` (iii))
One gluon: $|M|^2=g^2C_F(-g_{\mu\nu})(\frac{n^\mu}{n\cdot k}-\frac{\bar n^\mu}{\bar n\cdot k})(\dots)^\nu=\frac{4g^2C_F}{n\cdot k\,\bar n\cdot k}$. The measure is
$\int\frac{d^Dk}{(2\pi)^{D-1}}\delta^+(k^2)=\frac{\pi^{1-\varepsilon}}{2(2\pi)^{3-2\varepsilon}\Gamma(1-\varepsilon)}\int dn\!\cdot\!k\,d\bar n\!\cdot\!k\,(n\!\cdot\!k\,\bar n\!\cdot\!k)^{-\varepsilon}$, and the virtual graphs are scaleless.
$$S^{(1)}_{\rm bare}(k)=\frac{\alpha_sC_F}{4\pi}\,\frac{8e^{\varepsilon\gamma_E}}{\varepsilon\,\Gamma(1-\varepsilon)}\,\mu^{2\varepsilon}k^{-1-2\varepsilon}\ (\overline{\rm MS})
= a\Big\{\Big(-\frac4{\varepsilon^2}+\frac{\pi^2}3\Big)\delta(k)+\frac8\varepsilon\Big[\frac1k\Big]_*-16\Big[\frac{\ln(k/\mu)}k\Big]_*\Big\},$$
$$\boxed{S_T(k,\mu)=\delta(k)+\frac{\alpha_sC_F}{4\pi}\Big\{\frac{\pi^2}3\delta(k)-16\Big[\frac{\ln(k/\mu)}k\Big]_*\Big\}},\qquad\tilde s_T(L)=1+\frac{\alpha_sC_F}{4\pi}(-8L^2-\pi^2),$$
with $\frac{d\tilde s_T}{d\ln\mu}=[4\Gamma_{\rm cusp}L-2\gamma^S]\tilde s_T$ and $\gamma^S_0=0$. BS (read): $c_1^S=-C_F\pi^2$. **PASS.**

### 3.5 RG consistency (`s2_rg`)
$\tilde t(\nu)=H(Q^2,\mu)\,\tilde j(L_J)^2\,\tilde s_T(L_S)$. At one loop
$H^{(1)}+2j^{(1)}(L_Q-\ell)+s^{(1)}(\tfrac12L_Q-\ell)=-4\ell^2+6\ell-2$ (in units of $a$), which is $\mu$-independent.
To all orders,
$$\frac{d\ln\tilde t}{d\ln\mu}=\Gamma_{\rm cusp}\big[2L_Q-4L_J+4L_S\big]+2\gamma^H-4\gamma^J-2\gamma^S,\qquad 2L_Q-4L_J+4L_S\equiv0 .$$
So the **cusp terms cancel identically for any $\Gamma_{\rm cusp}(\alpha_s)$**, and the non-cusp terms cancel iff $\boxed{\gamma^S=\gamma^H-2\gamma^J}$ (BS eq. (gw), read).
One loop: $-6C_F-2(-3C_F)=0=\gamma^S_0$, which agrees with the direct computation.
Two loops (BS values, read): $\gamma^S_1=C_FC_A(\frac{808}{27}-\frac{11\pi^2}9-28\zeta_3)+C_FT_Fn_f(-\frac{224}{27}+\frac{4\pi^2}9)$. **The $C_F^2$ terms cancel**, as non-abelian
exponentiation requires for a soft function. This is a non-trivial consistency check of the two-loop $\gamma^H_1,\gamma^J_1$.

### 3.6 Fixed-order check against full QCD (`s2_rg`)
SCET at $\mu=Q$: $J\to Q^2J(Q^2\tau)$ and $S\to QS(Q\tau)$, with $[\cdot]_*\to[\cdot]_+$ on $[0,1]$. This gives
$$\frac1{\sigma_0}\frac{d\sigma}{d\tau}=\delta(\tau)+\frac{C_F\alpha_s}{2\pi}\Big\{\Big(\frac{\pi^2}3-1\Big)\delta(\tau)-3\Big[\frac1\tau\Big]_+-4\Big[\frac{\ln\tau}\tau\Big]_+\Big\}+\text{(integrable)}.$$
Full QCD, derived here with the trace engine: $\frac1{\sigma_0}\frac{d\sigma}{dx_1dx_2}=\frac{C_F\alpha_s}{2\pi}\frac{x_1^2+x_2^2}{(1-x_1)(1-x_2)}$. Integrating along $T=\max x_i$ reproduces
$\frac1{\sigma_0}\frac{d\sigma}{dT}=\frac{C_F\alpha_s}{2\pi}\big[\frac{2(3T^2-3T+2)}{T(1-T)}\ln\frac{2T-1}{1-T}-\frac{3(3T-2)(2-T)}{1-T}\big]$ to $7\times10^{-15}$.
As $\tau\to0$ this is $-(4\ln\tau+3)/\tau+O(\ln\tau)$, which matches the plus-distribution coefficients.
The $\delta(\tau)$ coefficient follows from $\sigma_{\rm tot}=\sigma_0(1+\frac{3C_F\alpha_s}{4\pi})$:
$c_\delta=\frac32-\int_0^1r(\tau)d\tau=2.289868133697$, against $\frac{\pi^2}3-1=2.289868133696$. This checks $H+2J+S$ constants
($(-16+\frac{7\pi^2}3)+2(7-\pi^2)+\frac{\pi^2}3=-2+\frac{2\pi^2}3$) against QCD to $10^{-12}$.
Cumulant: $R(\tau)=1+\frac{C_F\alpha_s}{2\pi}(-2\ln^2\tau-3\ln\tau+\frac{\pi^2}3-1)+O(\tau\ln\tau)$. Its Laplace transform, using
$\nu\int e^{-\nu t}\ln t=-\ell$ and $\nu\int e^{-\nu t}\ln^2t=\ell^2+\zeta_2$, equals $\tilde t$. **PASS.**

### 3.7 LL resummed exponent (`s2_rg`)
At LL keep one-loop $\Gamma$ and $\beta$, $\alpha(\mu')=\alpha_s(Q)/(1+b\alpha_s(Q)\ln(\mu'^2/Q^2))$. Evolve $\tilde j$ from $\mu_j^2=sQ^2$ and $\tilde s$ from $\mu_s=sQ$ to $\mu=Q$
($H$ has no large log there):
$$\ln\tilde t_{\rm LL}=\frac{C_F\alpha_s(Q)}\pi\big[2I_J-I_S\big],\quad I_J=\int_{-\ell}^0\!\frac{(\ell+t)\,dt}{1+b\alpha_st}=\frac{(1-\lambda)\ln(1-\lambda)+\lambda}{(b\alpha_s)^2},\quad I_S=\int_{-2\ell}^0\!\frac{(2\ell+t)\,dt}{1+b\alpha_st}=\frac{(1-2\lambda)\ln(1-2\lambda)+2\lambda}{(b\alpha_s)^2},$$
$$\boxed{\ln\tilde t_{\rm LL}=\ell\,g_1(\lambda),\qquad g_1(\lambda)=-\frac{C_F}{\pi b\lambda}\Big[(1-2\lambda)\ln(1-2\lambda)-2(1-\lambda)\ln(1-\lambda)\Big],\qquad\lambda=b\,\alpha_s(Q)\,\ell=\frac{\beta_0\alpha_s(Q)}{4\pi}\ln(\nu e^{\gamma_E})}$$
This is exactly the CTTW form for thrust (recall; CTTW 1993 is pre-arXiv and I could not open it), with their $\beta_0=(11C_A-2n_f)/(12\pi)=b$.
The series is $-\frac{C_F\alpha_s}\pi\ell^2-\frac{C_Fb}{\pi}\alpha_s^2\ell^3-\frac{7C_Fb^2}{6\pi}\alpha_s^3\ell^4-\dots$, and its first term is the fixed-order LL.
The LL functions of the Laplace exponent and of the $\tau$-space cumulant coincide (they differ from NLL on). The Landau singularity sits at $\lambda=\frac12$, where $\mu_s=Q/\bar\nu$ reaches $\Lambda$.

### 3.8 Status (T14.8, E14.9)
[A]: all orders within SCET, with modes hard, two collinear and usoft. No Glauber pinch arises for $e^+e^-$, since all collinear particles are outgoing
(blueprint P7.19, the contour-deformation argument of Ch. 7). **Correction of the attribution:** RS 2016 (re-read) contains no $e^+e^-$-specific statement; what it shows is that
"for the simplest examples … iterated Glauber exchange yields either phases or contributions that are related to the direction of soft or collinear Wilson lines in the hard
scattering operators (i.e. can be absorbed into Wilson lines), and hence cancel for an inclusive cross section". Cite RS 2016 only for this general mechanism.
The one-loop content is [R] (verified against full QCD to $10^{-12}$).
Non-perturbatively, for $Q\tau\sim\Lambda$ the soft function becomes a shape function (Korchemsky–Sterman 1995, 1999; BLMW 2004). The leading hadronization effect is a shift
$\propto\Lambda/Q$, which is [C] as a universal statement (critic B18).

---------------------------------------------------------------------------------------------------------------------

## 4. Part (3): NRQCD

### 4.1 Lagrangian and velocity scaling (`s3` A)
BBL (Sec. II.B, read): $\mathcal L=\mathcal L_{\rm light}+\psi^\dagger(iD_t+\frac{\boldsymbol D^2}{2m_Q})\psi+\chi^\dagger(iD_t-\frac{\boldsymbol D^2}{2m_Q})\chi+\delta\mathcal L_{\rm bilinear}+\delta\mathcal L_{4f}$.
Here $\psi$ annihilates a heavy quark and $\chi$ creates a heavy antiquark.
**Convention warning:** BBL use $D^\mu=\partial^\mu+igA^\mu$, i.e. CONTEXT's convention with $A\to-A$. The covariant-derivative operator is the same,
but $E^i=G^{0i}$ and $B^i=\frac12\epsilon^{ijk}G^{jk}$ change sign, because $[D_\mu,D_\nu]=+igG^{\rm BBL}_{\mu\nu}=-igG^{\rm CONTEXT}_{\mu\nu}$.
So the $c_2,c_3,c_4$ terms of BBL's $\delta\mathcal L_{\rm bilinear}$ (Darwin, spin-orbit, Fermi) change sign when written with CONTEXT's $\boldsymbol E,\boldsymbol B$. The four-fermion operators are unchanged.
Velocity-scaling rules (BBL Sec. II.C; Lepage et al. 1992; derived here by dimensional analysis):

| quantity | scaling | reason |
|---|---|---|
| $\psi,\chi$ | $(m v)^{3/2}$ | $\int d^3x\,\psi^\dagger\psi\simeq1$ over volume $(mv)^{-3}$ |
| $\boldsymbol D$ | $mv$ | momentum |
| $D_t$ | $mv^2$ | Schrödinger equation $iD_t\psi=-\frac{\boldsymbol D^2}{2m}\psi$ |
| $\alpha_s(mv)$ | $v$ | Coulomb binding |
| $g\boldsymbol E$ | $m^2v^3$ | Gauss law $\boldsymbol D\cdot g\boldsymbol E=g^2\psi^\dagger T\psi$ |
| $g\boldsymbol B$ | $m^2v^4$ | Ampère law $\boldsymbol D\times g\boldsymbol B=D_tg\boldsymbol E+g^2\boldsymbol j$, $\boldsymbol j\sim\psi^\dagger\boldsymbol D\psi/m$ |

All $1/m^2$-type bilinears ($\boldsymbol D^4/8m^3$, Darwin, spin-orbit, Fermi $\sigma\!\cdot\!g\boldsymbol B/2m$) are $O(v^2)$ relative to the LO terms.
Typical values are $v^2\approx0.3$ ($c\bar c$) and $0.1$ ($b\bar b$) (BBL Sec. II.A, read).
Decay contributions: S-wave colour singlet $\sim mv^3$; P-wave singlet (dimension 8) $\sim m^5v^5/m^4=mv^5$; colour-octet $^3S_1$ in $\chi_J$ $\sim v^2(mv)^3/m^2=mv^5$.
The last two are of the same order. That is why the octet term is needed to absorb the IR log of the singlet P-wave rate
(Barbieri–Gatto–Kögerler 1976; BBL 1992, abstract: "Logarithms of the binding energy … are factored into a phenomenological parameter … related to the probability for
the heavy quark-antiquark pair to be in a color-octet S-wave state").

### 4.2 Factorization formulas (BBL, read)
* Decays (BBL Sec. II.F–G): $\Gamma(H\to{\rm LH})=\sum_n\frac{2\,{\rm Im}f_n(\Lambda)}{m_Q^{d_n-4}}\langle H|\mathcal O_n(\Lambda)|H\rangle$ and $\Gamma(H\to{\rm EM})=\sum_n\frac{2\,{\rm Im}f_{{\rm EM},n}}{m_Q^{d_n-4}}\langle H|\mathcal O^{\rm EM}_n|H\rangle$,
  where $\mathcal O^{\rm EM}_n=\psi^\dagger\mathcal K_n\chi|0\rangle\langle0|\chi^\dagger\mathcal K_n'\psi$. States have NR normalization, and **BBL's "$M$" is the heavy-quark pole mass $m_Q$**.
* S-wave EM: $\Gamma(\eta_c\to\gamma\gamma)=\frac{2{\rm Im}f_{\gamma\gamma}(^1S_0)}{m_Q^2}|\langle0|\chi^\dagger\psi|\eta_c\rangle|^2+O(v^2)$ and
  $\Gamma(\psi\to e^+e^-)=\frac{2{\rm Im}f_{ee}(^3S_1)}{m_Q^2}|\langle0|\chi^\dagger\boldsymbol\sigma\psi|\psi\rangle|^2+O(v^2)$.
* Vacuum saturation (Sec. III.C–D): $\langle\psi|\mathcal O_1(^3S_1)|\psi\rangle=|\langle0|\chi^\dagger\boldsymbol\sigma\psi|\psi\rangle|^2(1+O(v^4))=\frac{N_c}{2\pi}|\bar R_\psi|^2$.
  The same holds for $\eta_c$ with $\chi^\dagger\psi$. In terms of $\psi(0)=R(0)/\sqrt{4\pi}$: $\langle0|\chi^\dagger\boldsymbol\sigma\psi|V(\boldsymbol\varepsilon)\rangle=\sqrt{2N_c}\,\psi(0)\,\boldsymbol\varepsilon$, so $\langle\mathcal O_1\rangle=2N_c|\psi(0)|^2$ (`s3`).
* Production (Sec. VI.A): $\sigma(H)=\sum_n\frac{F_n(\Lambda)}{m_Q^{d_n-4}}\langle0|\mathcal O^H_n(\Lambda)|0\rangle$, with
  $\mathcal O^H_n=\chi^\dagger\mathcal K_n\psi\big(\sum_X\sum_{m_J}|H+X\rangle\langle H+X|\big)\psi^\dagger\mathcal K_n'\chi$.
  BBL's argument is a KLN cancellation for soft gluons that attach to jets; "if both ends of a soft gluon attach to a heavy $Q$ or $\bar Q$ line, then there is no KLN cancellation.
  However, this contribution is part of the matrix element" (read).

### 4.3 Verified coefficients (`s3` B, C)
From explicit threshold amplitudes, using the projectors $\sum C\,u(p)\bar v(\bar p)=\frac1{2\sqrt2m}(\slashed p+m)\Gamma_S(\bar{\slashed p}-m)$ with
${\rm Tr}[\bar\Pi\Pi]=-4m^2$, and bound-state amplitude $\mathcal M=\frac{\sqrt{2M}}{2m}\sqrt{N_c}\,\psi(0)\,{\rm Tr}[\Gamma_f\Pi]$:
$$\Gamma(^3S_1\to e^+e^-)=\frac{16\pi N_c}{3}\frac{e_Q^2\alpha^2|\psi(0)|^2}{M^2}=\frac{4N_c}3\frac{e_Q^2\alpha^2|R(0)|^2}{M^2},\qquad
\Gamma(^1S_0\to\gamma\gamma)=16\pi N_c\frac{e_Q^4\alpha^2|\psi(0)|^2}{M^2}=4N_c\frac{e_Q^4\alpha^2|R(0)|^2}{M^2},$$
with $M=2m_Q$ (ratio to the formula: 1.000000000000 in both cases). For $N_c=3$ these become the Van Royen–Weisskopf form $16\pi e_Q^2\alpha^2|\psi(0)|^2/M^2$ and
$12e_Q^4\alpha^2|R(0)|^2/M^2$. The QED limit $16\pi\alpha^2|\psi(0)|^2/M^2=\alpha^5m/2$ (para-positronium) holds.
The selection rules (singlet $\not\to\gamma^*$, triplet $\not\to\gamma\gamma$) hold, and the LO ratio is $\Gamma(\eta_c\to\gamma\gamma)/\Gamma(J/\psi\to e^+e^-)=3e_Q^2=\frac43$ (spin symmetry).
BBL normalization: ${\rm Im}f_{ee}(^3S_1)=\frac{\pi e_Q^2\alpha^2}3$ and ${\rm Im}f_{\gamma\gamma}(^1S_0)=\pi e_Q^4\alpha^2$, both **PASS** against BBL App. A (read).

**$O(\alpha_s)$ correction (derived).** The hard-region matching of the vector current at threshold ($p_1=p_2=p$, $p^2=m^2$, Feynman gauge, DR for UV and IR) gives:
vertex $=\frac{\alpha_sC_F}{4\pi}\big(\frac3\varepsilon-4+3\ln\frac{\mu^2}{m^2}\big)$ (the pole is mixed, $\frac1{\varepsilon_{\rm UV}}+\frac2{\varepsilon_{\rm IR}}$);
on-shell $\delta Z_2=-\frac{\alpha_sC_F}{4\pi}\big(\frac3\varepsilon+4+3\ln\frac{\mu^2}{m^2}\big)$. Hence
$$\boxed{c_v=1-2C_F\frac{\alpha_s}\pi},\qquad \Gamma(V\to e^+e^-)=\Gamma_{\rm LO}|c_v|^2=\Gamma_{\rm LO}\Big(1-4C_F\frac{\alpha_s}\pi\Big)=\Gamma_{\rm LO}\Big(1-\frac{16\alpha_s}{3\pi}\Big)\ (N_c=3).$$
BBL App. A (read): ${\rm Im}f_{ee}(^3S_1)=\frac{\pi Q^2\alpha^2}3[1-4C_F\frac{\alpha_s}\pi]$, citing Barbieri–Gatto–Kögerler–Kunszt 1975 and Celmaster 1979. **PASS.**
(The potential and soft regions are scaleless at exact threshold. The Coulomb $\pi^2/v$ term belongs to NRQCD.)
Not re-derived here: ${\rm Im}f_{\gamma\gamma}(^1S_0)=\pi Q^4\alpha^2[1+(\frac{\pi^2}4-5)C_F\frac{\alpha_s}\pi]=\pi Q^4\alpha^2[1-\frac{(20-\pi^2)\alpha_s}{3\pi}]$ (BBL App. A, read;
Barbieri–Curci–d'Emilio–Remiddi 1979). Its QED analogue is the Harris–Brown 1957 correction $1-(5-\frac{\pi^2}4)\frac\alpha\pi$ for para-positronium (recall; reference verified on INSPIRE).

### 4.4 Status (Ch. 15)
* T15.3 decay factorization [A] (BBL: NRQCD matching plus KLN for inclusive light hadrons; P-wave consistency demonstrated in BBL 1992).
* P15.2 matching coefficients [R] in (PT); the one-loop $c_v$ was re-derived here.
* Cj15.5 production [C]. NQS 2005a (abstract): "uncanceled infrared poles at NNLO that are not matched by conventional NRQCD matrix elements … gauge invariance and
  factorization require that conventional NRQCD production operators be modified to include non-Abelian phases or Wilson lines. With appropriately modified operators,
  factorization is restored at NNLO … infrared poles at yet higher orders may require … additional nonlocal operators". NQS 2006 (abstract): consistent to all orders in $v$
  for that NNLO topology, with the gauge-completed matrix elements. So the NNLO tests are [P].
* P15.6 (KQS 2012, abstract): LP + NLP pQCD factorization in $m_Q^2/p_T^2$ at large $p_T$, with NRQCD estimates of the fragmentation functions. Leave [A] for the
  pQCD part (as in the blueprint), and [C] for the NRQCD step.

---------------------------------------------------------------------------------------------------------------------

## 5. Part (4): QCD factorization for $B\to M_1M_2$ (BBNS) and $B\to D\pi$ (BPS)

### 5.1 Setup (BBNS 2001, read)
$\mathcal H_{\rm eff}=\frac{G_F}{\sqrt2}\sum_{p=u,c}\lambda_p\big(C_1Q_1^p+C_2Q_2^p+\sum_{i=3}^{10}C_iQ_i+C_{7\gamma}Q_{7\gamma}+C_{8g}Q_{8g}\big)$, with
$Q_1^p=(\bar pb)_{V-A}(\bar sp)_{V-A}$ and $Q_2^p=(\bar p_ib_j)_{V-A}(\bar s_jp_i)_{V-A}$. At $\mu=m_b$: $C_1=1.081$, $C_2=-0.190$ (BBNS Table, read).
Light-cone DAs: $\Phi_M(x)=6x\bar x[1+\sum_n\alpha_n^MC_n^{(3/2)}(2x-1)]$, $\int\Phi_M=1$. The B DA enters through $\int_0^1\frac{d\xi}\xi\Phi_B(\xi)\equiv m_B/\lambda_B$.

### 5.2 The factorization formula at leading power (BBNS 2000 eq. (fff); BBNS 2001 eq. (fact), read)
$$\langle M_1M_2|Q_i|\bar B\rangle=F^{B\to M_1}(m_2^2)\,T^{\rm I}_{M_2,i}*f_{M_2}\Phi_{M_2}\;+\;F^{B\to M_2}(m_1^2)\,T^{\rm I}_{M_1,i}*f_{M_1}\Phi_{M_1}\;+\;T^{\rm II}_i*f_B\Phi_B*f_{M_1}\Phi_{M_1}*f_{M_2}\Phi_{M_2}\;+\;O(\Lambda/m_b).$$
* The second form-factor term is present only if the spectator can go into either meson.
* $T^{\rm I}=1+O(\alpha_s)$ (naive factorization plus "non-factorizable" vertex and penguin corrections). $T^{\rm II}=O(\alpha_s)$ (hard spectator scattering).
* Heavy–light ($\bar B_d\to D^+\pi^-$, spectator $\to D$): $\langle D\pi|Q|\bar B\rangle=F^{B\to D}(m_\pi^2)\,T^{\rm I}*f_\pi\Phi_\pi$. **No $T^{\rm II}$ term**: the spectator graphs give
  $\sim G_F\alpha_sf_\pi f_Df_B\int\frac{\Phi_B}\xi\int\frac{\Phi_D}\eta\int\frac{\Phi_\pi}u\sim G_F\alpha_sm_b\Lambda^2$, against the leading $G_Fm_b^2F^{B\to D}f_\pi\sim G_Fm_b^2\Lambda$
  (BBNS 2000 eqs. (abd), (specd), read; `s4` A).
* If the spectator goes to the light meson and the other meson is heavy, factorization fails, but such amplitudes are power suppressed (BBNS 2000, read).
* Annihilation topologies do not contribute at leading power.

### 5.3 Power counting (`s4` A)
$F^{B\to\pi}(0)\sim(\Lambda/m_b)^{3/2}$ (endpoint suppression), $f_B\sim\Lambda^{3/2}m_b^{-1/2}$, $f_\pi\sim\lambda_B\sim\Lambda$. Then
term I $\sim F\,m_b^2f_\pi\sim\Lambda^{5/2}m_b^{1/2}$ and term II $\sim f_Bf_{M_1}f_{M_2}\,m_b/\lambda_B\sim\Lambda^{5/2}m_b^{1/2}$.
Both are leading power, and $H_{M_2M_1}=\frac{f_Bf_{M_1}}{m_B\lambda_BF^{B\to M_1}(0)}[\dots]=O(1)$.

### 5.4 What is established (references verified on INSPIRE; claims from sources/abstracts read)
* **$O(\alpha_s)$:** the soft and collinear IR divergences of the "non-factorizable" vertex and spectator graphs cancel at leading power (colour transparency). The kernels
  $T^{\rm I},T^{\rm II}$ were computed at one loop or tree level (BBNS 1999, 2000, 2001).
* **Two-loop IR analysis for $B\to D\pi$:** BBNS 2000 (read), "we analyze in detail the infrared singularities for $\bar B_d\to D^+\pi^-$ decays at two-loop order and demonstrate
  [factorization] … the following does not accomplish an all-order 'proof'".
* **All orders, $B\to D\pi$:** BPS 2001 (§5.8).
* **NNLO kernels (IR finiteness established explicitly):**
  - two-loop vertex corrections to the tree amplitudes: Bell 2008 (imaginary part) and Bell 2009 (real part; "the hard-scattering kernels are free of soft and collinear infrared
    divergences at the 2-loop level"); Beneke–Huber–Li 2010 (analytic, with full charm-mass dependence);
  - one-loop ($\alpha_s^2$) spectator scattering: Beneke–Jäger 2006 ("the infrared finiteness of our result establishes factorization of spectator scattering at the 1-loop order"),
    Kivel 2007, Pilipp 2008; hard-collinear jet function: Beneke–Yang 2006;
  - NNLO penguin amplitudes: Bell–Beneke–Huber–Li 2015 and 2020 ("the last missing piece … at leading power");
  - heavy–light $B\to D^{(*)}L$ at NNLO: Huber–Kränkl–Li 2016.
* **SCET all-order analyses at leading power:** BPRS 2004 (abstract) "derive the factorization theorem for the decays $B\to M_1M_2$ … at leading order in $\Lambda/E_M$ and
  $\Lambda/m_b$ … even if $\alpha_s(E_M\Lambda)$ is not perturbative … We argue that $c\bar c$ penguins could give long-distance effects at leading order". Beneke–Feldmann 2004
  (abstract) show the heavy-to-light form-factor factorization formula "is valid to all orders in perturbation theory", circumventing endpoint divergences by defining the
  universal (soft-overlap) form factors. Hill–Neubert 2003 treat spectator interactions in SCET.
* **Open dispute:** BBNS's comment (2005) states that the BPRS formula "is equivalent to the corresponding formula in the QCD factorization approach". The BPRS reply (2005) states
  "We disagree with their criticisms" (charming penguins, treatment of the spectator term). The writer should report this without a verdict.

### 5.5 The $O(\alpha_s)$ vertex term (`s4` B, C)
$a_{1,\rm I}=C_1+\frac{C_2}{N_c}\big[1+\frac{C_F\alpha_s}{4\pi}V_M\big]$, $a_{2,\rm I}=C_2+\frac{C_1}{N_c}\big[1+\frac{C_F\alpha_s}{4\pi}V_M\big]$, and
$a_{1,\rm II}=\frac{C_2}{N_c}\frac{C_F\pi\alpha_s}{N_c}H_{M_2M_1}$ (BBNS 2001 eq. (ai), read). Here
$$V_M=12\ln\frac{m_b}\mu-18+\int_0^1\!dx\,g(x)\Phi_M(x)\quad(\text{NDR}),\qquad
g(x)=3\Big(\frac{1-2x}{1-x}\ln x-i\pi\Big)+\Big[2{\rm Li}_2(x)-\ln^2x+\frac{2\ln x}{1-x}-(3+2i\pi)\ln x-(x\leftrightarrow1-x)\Big].$$
* **Origin of $12\ln(m_b/\mu)$ (derived):** with $\frac{dC}{d\ln\mu}=\frac{\alpha_s}{4\pi}\gamma^TC$, $\gamma=\begin{pmatrix}-6/N&6\\6&-6/N\end{pmatrix}$
  ($\gamma_\pm=\pm6(N\mp1)/N$ for $C_\pm=C_1\pm C_2$), one finds
  $\frac d{d\ln\mu}(C_1+\frac{C_2}N)=\frac{\alpha_s}{4\pi}\frac{12C_F}NC_2$. This is cancelled iff $V_M\ni12\ln\frac{m_b}\mu$, for any $N_c$; the same holds for $a_2$.
  The constants $-18$ and $-6$ (for $V'$) are NDR-specific (BBNS).
* $\int_0^1g\,\Phi_M=-\frac12-3i\pi+(\frac{11}2-3i\pi)\alpha_1^M-\frac{21}{20}\alpha_2^M+\dots$ (BBNS (vgegenb)), verified to $10^{-20}$ with mpmath.
  For a symmetric DA, $V'_\pi=V_\pi+12$. At $\mu=m_b$ with the asymptotic DA, $V=-18.5-3i\pi$: **the strong phase is $O(\alpha_s)$ and perturbative at leading power**.

### 5.6 Hard spectator term and the twist-3 endpoint divergence (`s4` D)
BBNS 2001 eq. (Hiexpr) (read):
$$H_{K\pi}=\frac{f_Bf_\pi}{m_B^2F_0^{B\to\pi}(0)}\int_0^1\frac{d\xi}\xi\Phi_B(\xi)\int_0^1\frac{dx}{\bar x}\Phi_K(x)\int_0^1\frac{dy}{\bar y}\Big[\Phi_\pi(y)+\frac{2\mu_\pi}{m_b}\frac{\bar x}x\Phi_p^\pi(y)\Big]
=\frac{f_Bf_\pi}{m_B\lambda_BF_0^{B\to\pi}(0)}\big[\langle\bar x^{-1}\rangle_K\langle\bar y^{-1}\rangle_\pi+r_\chi^\pi\langle x^{-1}\rangle_KX_H^\pi\big].$$
* Kinematics (derived): the spectator gluon has $k^2\simeq-\bar y\,\xi\,m_B^2\sim m_b\Lambda$, i.e. it is **hard-collinear**, not hard. Hence $\alpha_s(\mu_h)$ with $\mu_h=\sqrt{\Lambda_h\mu}$.
  The quark propagators at the emission vertex have virtuality $\sim x\bar y\,m_B^2$ (hard).
* Twist-2 convolutions are finite: $\langle\bar x^{-1}\rangle=\langle x^{-1}\rangle=3$ for the asymptotic DA.
* The chirally enhanced twist-3 term ($r_\chi^M=2\mu_M/m_b$, formally $\Lambda/m_b$ but numerically $O(1)$) with $\Phi_p(y)=1$ gives
  $X_H=\int_0^1\frac{dy}{1-y}\Phi_p(y)$, which is **logarithmically divergent**. Physically it is cut off at $1-y\sim\Lambda/m_b$, so $X_H\sim\ln(m_b/\Lambda)$ with a possibly complex coefficient.

### 5.7 Annihilation and the $X_A$ model (`s4` E)
BBNS 2001 give the building blocks $A_k^{i,f}$ as convolutions (read). For example,
$A_1^i=\pi\alpha_s\int dxdy\{\Phi_{M_2}(x)\Phi_{M_1}(y)[\frac1{y(1-x\bar y)}+\frac1{\bar x^2y}]+r_\chi^{M_1}r_\chi^{M_2}\frac2{\bar xy}\}$. With asymptotic DAs and
$\int_0^1\frac{dy}y\to X_A$, $\int_0^1\frac{\ln y}ydy\to-\frac12X_A^2$ (BN 2003 eq. (XAdef), read), I re-derived:
$$A_1^i\approx A_2^i\approx\pi\alpha_s\Big[18\Big(X_A-4+\frac{\pi^2}3\Big)+2r_\chi^2X_A^2\Big],\quad
A_3^i\approx6\pi\alpha_s(r_\chi^{M_1}-r_\chi^{M_2})\Big(X_A^2-2X_A+\frac{\pi^2}3\Big),\quad A_3^f\approx6\pi\alpha_s(r_\chi^{M_1}+r_\chi^{M_2})(2X_A^2-X_A),$$
with $A_1^f=A_2^f=0$ (PP final states). This agrees with BBNS 2001 (XAdef) and BN 2003 (XAmodel). The finite piece is $36\int\!\!\int\frac{x\bar x\bar y}{1-x\bar y}=18(\frac{\pi^2}3-3)$.
**Parametrization** (BBNS 2001 (XHparam),(XAparam); BN 2003, read):
$$X_{A,H}=\big(1+\varrho_{A,H}e^{i\varphi_{A,H}}\big)\ln\frac{m_B}{\Lambda_h},\qquad\varrho_{A,H}\le1,\quad\Lambda_h=0.5\ {\rm GeV},\quad\varphi\ \text{arbitrary}.$$
The "default value" is $\ln(m_B/\Lambda_h)\approx2.4$, assigned a 100% uncertainty, and $|X|\in[0,2\ln(m_B/\Lambda_h)]$. BN 2003 scenario S3 uses $\varrho_A=1$ and
$\varphi_A=-45^\circ$; a variant uses $\varrho_A=2$ and $\varphi_A=-60^\circ$ (read).
**Prescription dependence (derived):** if the same divergent $A_3^i$ integral is regulated by cutting both $x<1-\delta$ and $y>\delta$, the result differs from the BN-rule
value by $-21.6$ at $X_A=13.8$. The $X_A$ model is therefore not a factorization theorem: its finite parts depend on how the divergence is cut off.

### 5.8 $B\to D\pi$ to all orders (BPS 2001, read)
Statement: for $\bar B^0\to D^+\pi^-$ and $B^-\to D^0\pi^-$, in the limit $Q=\{m_b,m_c,E_\pi\}\gg\Lambda$,
$$\langle D\pi|O_{\bf 0,8}|B\rangle=N\,F^{B\to D}(0)\int_0^1\!dx\,T(x,\mu)\,\phi_\pi(x,\mu),\qquad N=\frac i2m_BE_\pi f_\pi,$$
to all orders in $\alpha_s$, up to corrections suppressed by $1/m_b,1/m_c,1/E_\pi$. Here $O_{\bf0}=[\bar c\gamma^\mu P_Lb][\bar d\gamma_\mu P_Lu]$ and $O_{\bf8}$ is the same with $T^a\otimes T^a$.
In the heavy-quark limit $F^{B\to D}(0)=\frac12\sqrt{m_D/m_B}\,(1+m_B/m_D)\,\xi(v\!\cdot\!v')$.
"It is not necessary to assume that the pion state is dominated by the $q\bar q$ Fock state"; "it was not necessary to set the transverse momenta of partons to zero";
"this proof also goes through for other class I decays".
Proof structure:
1. Modes: HQET heavy quarks, soft quarks and gluons ($Q\lambda$), collinear pion constituents, usoft.
2. Tree-level matching onto $Q_{\bf0}=[\bar h_{v'}\Gamma_hh_v][\bar\xi\Gamma_\ell\xi]$ and $Q_{\bf8}=[\bar h_{v'}\Gamma_h(W^\dagger T^AW)h_v][\bar\xi\Gamma_\ell T^A\xi]$. Here $W^\dagger W=1$
   "encodes … that collinear gluon interactions from the $b$ and $c$ quarks cancel identically to all orders for the color singlet operators".
3. Only $n\!\cdot\!A_s$ soft gluons couple to collinear particles at $O(\lambda^0)$, and soft momenta drop out of collinear propagators. Ward identities factor them into $S=P\exp[ig\int n\!\cdot\!A_s]$.
   For $Q_{\bf0}$, $S^\dagger S=1$; for $Q_{\bf8}$ the colour trace ${\rm Tr}[MW^\dagger T^AW]\propto{\rm Tr}T^A=0$ kills the matrix element.
4. Collinear gauge invariance restricts the hard coefficients to $\bar\xi WC(\bar{\mathcal P}_+)\Gamma W^\dagger\xi$. This gives the convolution with $T(x,\mu)=C^1_{\bf0}(\mu,2(2x-1)E_\pi)$.
**Assumption** (BPS, read): "We will assume that the tail end of wavefunctions are suppressed by $\lambda^a$ with $a>0$". This is what makes annihilation and hard-spectator
contributions power suppressed. The writer must state it in the theorem box.
Colour transparency (`s4` F): the eikonal couplings of a soft gluon to the collinear colour-singlet $q\bar q$ pair cancel. The remainder is a dipole term $\propto k_T/E$
($6.9\times10^{-2}\to6.6\times10^{-4}$ as $k_T$ decreases by $10^2$), i.e. $O(\Lambda/m_b)$.

### 5.9 Related results to mention
* Colour-suppressed $\bar B^0\to D^0M^0$: Mantry–Pirjol–Stewart 2003 (abstract) "prove a factorization theorem … Both the color-suppressed and W-exchange/annihilation
  amplitudes contribute at lowest order … so no power suppression of annihilation contributions is found".
* Endpoint divergences at subleading power: Liu–Neubert 2020 (abstract) refactorize $h\to\gamma\gamma$ via a $b$-quark loop ("endpoint divergences caused by rapidity
  divergences cancel to all orders … endpoint divergences that are regularized dimensionally can be removed by rearranging the terms in the factorization theorem").
  Beneke et al. 2019 treat DY threshold at NLP. No analogous refactorization exists for $B\to M_1M_2$ annihilation.

### 5.10 Status (proposal; see §6 for the comparison with the blueprint and the critic)
* $B\to D\pi$ (class I) at leading power, all orders in $\alpha_s$: **[A]** (BPS 2001; two-loop IR demonstration BBNS 2000; NNLO kernel HKL 2016), with the stated endpoint assumption.
* $B\to M_1M_2$ (two light mesons) leading-power formula: **[A]** as formulated. The SCET derivation is BPRS 2004 (with Beneke–Feldmann 2004 and Hill–Neubert 2003), and IR finiteness
  is explicitly verified through NNLO for $T^{\rm I}$ and one loop for $T^{\rm II}$. A caveat box must report the unresolved dispute on long-distance charming penguins.
* Power corrections (annihilation, twist-3 spectator): the naive collinear-factorized form gives divergent convolutions at $O(\alpha_s)$. Standard factorization of these terms
  is therefore **[V]** (explicitly divergent). The $X_A,X_H$ parametrization is a **model**. A refactorization of these endpoint divergences is **[C]**.

---------------------------------------------------------------------------------------------------------------------

## 6. Discrepancies, corrections and notes for the writer

1. **RG-consistency relation (blueprint T14.8).** "$\gamma_H+2\gamma_J+\gamma_S=0$ (in Laplace space)" is correct only as a statement about the **total** logarithmic
   derivatives, $\frac{d\ln H}{d\ln\mu}+2\frac{d\ln\tilde j}{d\ln\mu}+\frac{d\ln\tilde s}{d\ln\mu}=0$. With the standard normalization of the non-cusp anomalous dimensions
   ($d\ln H=\dots+2\gamma^H$, $d\ln\tilde j=\dots-2\gamma^J$, $d\ln\tilde s=\dots-2\gamma^S$; Becher–Schwartz), the relation is $\gamma^S=\gamma^H-2\gamma^J$, together with the identity
   $2L_Q-4L_J+4L_S=0$ for the cusp parts. The book must fix the convention and print both statements.
2. **Plus distributions.** The thrust distribution needs plus distributions subtracted at $\tau=0$: $\int_0^1[g]_+h=\int_0^1g(h-h(0))$. CONTEXT.md defines the plus distribution at
   $z=1$. Both conventions should be named in the notation section, e.g. $[\cdot]_+$ for $z\to1$ and $[\cdot]_{+}^{(0)}$ or $\mathcal D_k(\tau)$ for $\tau\to0$.
3. **E14.9 coefficient** (requested by the blueprint): $\frac{C_F\alpha_s}{2\pi}\{-4[\frac{\ln\tau}\tau]_+-3[\frac1\tau]_++(\frac{\pi^2}3-1)\delta(\tau)\}$, verified against QCD.
4. **Glauber modes (blueprint D14.1, "Glauber $Q(\lambda^2,\lambda^2,\lambda)$ etc.").** The full list in $(\bar n\!\cdot\!p,n\!\cdot\!p,p_\perp)$ ordering is $n$–$\bar n$ $(\lambda^2,\lambda^2,\lambda)$,
   $n$–soft $(\lambda,\lambda^2,\lambda)$ and $\bar n$–soft $(\lambda^2,\lambda,\lambda)$. RS 2016 write $(\lambda^a,\lambda^b,\lambda)$ in $(n\!\cdot\!p,\bar n\!\cdot\!p,p_\perp)$ ordering, so their $\{2,1\}$ is
   "$s$–$n$". The orderings must not be mixed.
5. **Decoupling theorem (blueprint T14.5).** The "two-line proof" must also (i) redefine the collinear ghosts, $c_n=Yc_n^{(0)}Y^\dagger$, (ii) use a collinear gauge fixing that is covariant
   under usoft gauge transformations, (iii) note the unit Jacobian, (iv) restrict to leading power, and (v) build $Y_n$ from the multipole-expanded $n\!\cdot\!A_{us}(x_-)$.
   The blueprint writes $Y_n$ from $-\infty$. For outgoing collinear quarks the QCD eikonal rules produce the future-pointing line (§2.4, verified). This is immaterial for the
   Lagrangian identity and for one-loop thrust, but it should be remarked (Chay et al. 2005; Kang–Labun–Lee 2015).
6. **$W_n$ orientation (blueprint P14.3).** In CONTEXT notation $W_n(x)=W[x,x-\infty\bar n]$. Its momentum-space form is $\sum_{\rm perms}\exp[-\frac g{\bar{\mathcal P}}\bar n\!\cdot\!A_n]$ in the
   conventions of BFPS, BPS and Bauer–Stewart, who use $D=\partial-igA$ (read). **No sign change of $g$ is needed**.
7. **$B\to D\pi$ (blueprint T14.11).** BPS write $F^{B\to D}(0)$ (not $F^{B\to D}(m_\pi^2)$; the difference is power suppressed), with $N=\frac i2m_BE_\pi f_\pi$ and channels
   $\bar B^0\to D^+\pi^-$, $B^-\to D^0\pi^-$. The endpoint-suppression **assumption** must appear in the statement.
8. **Rigor tag of P14.12 (blueprint: overall [P]; critic O19: split).** I support the critic's split: leading power [A] with an explicit caveat on charming penguins;
   subleading power standard factorization [V]; the $X_A,X_H$ model is a model; refactorization is [C]. If the lead author prefers one tag for the whole proposition, [P] is
   defensible only if the statement includes the power corrections.
9. **NRQCD conventions.** (a) BBL use $D^\mu=\partial^\mu+igA^\mu$, so the signs of the $c_{2,3,4}$ bilinears flip when transcribed with CONTEXT's $E,B$ (§4.1). (b) In BBL's
   formulas $2{\rm Im}f_n/M^{d_n-4}$, **$M$ is the heavy-quark pole mass**, not the meson mass. The blueprint's $m_Q^{d_n-4}$ is correct, but the VRW formula is usually quoted with
   the meson mass $M=2m_Q$. (c) For the decay formula cite "BBL 1995, Sec. II.F–G", and for production "Sec. VI.A" (the blueprint has "§?").
10. **Typo in the Becher–Schwartz arXiv source.** Their App. A prints $\Gamma_1=4C_F[C_A(\frac{67}9-\frac{\pi^2}3)-\frac{20}9C_FT_Fn_f]$. The $C_F$ inside the bracket is spurious; the
    correct form is $\Gamma_1=4C_F[(\frac{67}9-\frac{\pi^2}3)C_A-\frac{20}9T_Fn_f]$ (Korchemsky–Radyushkin 1987). Writers copying two-loop values must use the correct form.
11. **Reference correction.** Phys. Rev. D66 (2002) 054005 is BPS, "Power counting in the soft collinear effective theory". The endpoint-singularity paper is BPS, Phys. Rev. D67
    (2003) 071502 (INSPIRE).
12. **Blueprint T14.8 references.** "Bauer, Lee, Manohar, Wise, PRD 70 (2004) 034014" is verified (INSPIRE: "Enhanced nonperturbative effects in Z decays to hadrons"), as is
    "Fleming, Hoang, Mantry, Stewart PRD 77 (2008) 074010" ("Jets from massive unstable particles: Top-mass determination"). The NLL-resummed peak-region analysis is
    PRD 77 (2008) 114003.

13. **Jet-function definition of Becher–Schwartz (normalization implicit).** BS 2008 print
    $J(p^2)=\frac1{\bar n\cdot p}\frac1\pi{\rm Im}[i\int d^4x\,e^{-ipx}\langle0|T\{\bar\chi_n(x)\frac{\bar{\slashed n}}2\chi_n(0)\}|0\rangle]=\delta(p^2)+O(\alpha_s)$. Read literally (fermionic
    $T$-ordering sign, Dirac and colour traces) the free field gives $-2N_c\,\delta(p^2)$ (`s1` check), i.e. a factor $-\frac1{2N_c}{\rm tr}$ is implicit. The book must use
    the explicitly normalized cut definition (`tex/c_scet_thrust.tex`, eq. thrust-Jdef; remark rem:thrust-Jnorm).
14. **Attribution correction (Glauber in $e^+e^-$).** RS 2016 contains no $e^+e^-$-specific statement. For thrust the absence of a Glauber pinch is the Ch. 7
    contour-deformation argument (blueprint P7.19); RS 2016 may be cited only for the general mechanism ("iterated Glauber exchange yields either phases or
    contributions … related to the direction of soft or collinear Wilson lines … and hence cancel for an inclusive cross section") and for the rule "Ultrasoft
    Wilson line directions in SCET$_{\rm I}$ are determined by the physical directions". After the BPS field redefinition the Glauber Lagrangian still couples
    $n$ and $\bar n$ (only adjoint $\mathcal Y$ lines appear; RS 2016 §5.1): usoft decoupling does **not** remove Glauber interactions.
15. **Collinear gauge invariance of the ghost term.** BPS 2002 write that "the first two terms in Eq. (Lcg)" (field strength and ghost term) "are invariant under
    collinear gauge transformations". For the ghost term this is not literally true (its outer derivative $[i\mathcal D_\mu,\cdot]$ is not collinear covariant;
    gauge-fixing + ghost terms are BRST invariant). The correct statement, used in `tex/c_scet_scet.tex` (prop:scet-gauge): the field-strength term is invariant
    under both collinear and usoft transformations; gauge-fixing and ghost terms are usoft covariant (this is what the decoupling proof needs) and BRST invariant.
16. **Attribution correction (reparameterization).** The sentence "this global reparameterization invariance fixes the collinear action, except for the way in
    which $in\cdot D$ appears" is a BPS 2002 footnote and refers to the $x$-independent collinear transformations of Bauer–Stewart 2001, not to the Lorentz RPI of
    Manohar–Mehen–Pirjol–Stewart 2002. Cite accordingly.
17. **Minor typos in the QCDF literature.** BBNS 2001 and BN 2003 call "$X_H=\ln(m_M/\Lambda_h)\approx2.4$" the default value next to a parametrization written
    with $\ln(m_B/\Lambda_h)$; $m_M$ must read $m_B$ (BBNS 2001 has $\ln(m_B/\Lambda_h)\approx2.4$ correctly elsewhere). In the general $(M_1M_2)$ notation of BN 2003,
    $V$ always refers to the emitted meson $M_2$; BBNS 2001's $\pi K$-specific labels ($a_1$ with $V_K$, $a_2$ with $V_\pi$) are a special case — do not mix the two.
18. **Preamble issues found in the test build** (for the lead author): (a) `\cref` with several **section** labels prints English "sections 1.7与1.8", because
    the preamble sets only `\crefformat{section}`; add `\crefmultiformat{section}{第~#2#1#3}{~与~#2#1#3~节}{、#2#1#3}{~与~#2#1#3~节}` (and the same for
    subsection), or avoid multi-label section references (done in `tex/`). (b) The `cremark` head font `\itshape` triggers
    "Font shape `TU/FandolKai-Regular(0)/m/it' undefined" (harmless substitution; also present in the c_wilson build).

---------------------------------------------------------------------------------------------------------------------

## 7. References used (all checked on INSPIRE; keys of `research/refs/refs.bib` where available)

In refs.bib: BauerFlemingLuke2000; BauerEtAl2001 (BFPS); BauerStewart2001; BauerPirjolStewart2001 (BPS $B\to D\pi$); BauerPirjolStewart2002 (decoupling);
BauerEtAl2002 (BFPRS); ManoharStewart2007; BecherSchwartz2008; BecherNeubert2011; BecherBroggioFerroglia2015; RothsteinStewart2016; CataniEtAl1993 (CTTW);
KorchemskyRadyushkin1987; BenekeEtAl1999/2000/2001 (BBNS); BenekeNeubert2003; CaswellLepage1986; BodwinBraatenLepage1995 (+Erratum); NayakQiuSterman2005a/2005b/2006;
BrambillaEtAl2011; BenekeSmirnov1998.

New (verified on INSPIRE, texkey in brackets):
- C. W. Bauer, C. Lee, A. V. Manohar, M. B. Wise, Phys. Rev. D 70 (2004) 034014, hep-ph/0309278 [Bauer:2003di]
- S. Fleming, A. H. Hoang, S. Mantry, I. W. Stewart, Phys. Rev. D 77 (2008) 074010, hep-ph/0703207 [Fleming:2007qr]; Phys. Rev. D 77 (2008) 114003, 0711.2079 [Fleming:2007xt]
- M. D. Schwartz, Phys. Rev. D 77 (2008) 014026, 0709.2709 [Schwartz:2007ib]
- C. W. Bauer, A. V. Manohar, Phys. Rev. D 70 (2004) 034024, hep-ph/0312109 [Bauer:2003pi] (one-loop jet function)
- T. Becher, M. Neubert, Phys. Lett. B 637 (2006) 251, hep-ph/0603140 [Becher:2006qw] (two-loop jet function)
- T. Becher, M. Neubert, Phys. Rev. Lett. 102 (2009) 162001, 0901.0722 [Becher:2009cu]
- S. Moch, J. Vermaseren, A. Vogt, JHEP 08 (2005) 049, hep-ph/0507039 [Moch:2005id]
- G. P. Korchemsky, G. Sterman, Nucl. Phys. B 437 (1995) 415 [Korchemsky:1994is]; Nucl. Phys. B 555 (1999) 335 [via INSPIRE, "Power corrections to event shapes and factorization"]
- A. De Rújula, J. Ellis, E. Floratos, M. K. Gaillard, Nucl. Phys. B 138 (1978) 387 [DeRujula:1978vmq]
- J. Chay, C. Kim, Y. G. Kim, J.-P. Lee, Phys. Rev. D 71 (2005) 056001, hep-ph/0412110 [Chay:2004zn]
- D. Kang, O. Z. Labun, C. Lee, Phys. Lett. B 748 (2015) 45, 1504.04006 [Kang:2015moa]
- C. W. Bauer, B. O. Lange, G. Ovanesyan, JHEP 07 (2011) 077, 1010.1027 [Bauer:2010cc]
- J.-Y. Chiu, A. Jain, D. Neill, I. Z. Rothstein, JHEP 05 (2012) 084, 1202.0814 [Chiu:2012ir]
- R. J. Hill, M. Neubert, Nucl. Phys. B 657 (2003) 229, hep-ph/0211018 [Hill:2002vw]
- C. W. Bauer, D. Pirjol, I. W. Stewart, Phys. Rev. D 66 (2002) 054005, hep-ph/0205289 [Bauer:2002uv] (power counting); Phys. Rev. D 67 (2003) 071502, hep-ph/0211069 [Bauer:2002aj] (endpoint singularities)
- M. Beneke, T. Feldmann, Nucl. Phys. B 685 (2004) 249, hep-ph/0311335 [Beneke:2003pa]
- M. Beneke, D. Yang, Nucl. Phys. B 736 (2006) 34, hep-ph/0508250 [Beneke:2005gs]
- C. W. Bauer, D. Pirjol, I. Z. Rothstein, I. W. Stewart, Phys. Rev. D 70 (2004) 054015, hep-ph/0401188 [Bauer:2004tj]
- M. Beneke, G. Buchalla, M. Neubert, C. T. Sachrajda, Phys. Rev. D 72 (2005) 098501, hep-ph/0411171 [Beneke:2004bn]; reply: BPRS, Phys. Rev. D 72 (2005) 098502, hep-ph/0502094 [Bauer:2005wb]
- G. Bell, Nucl. Phys. B 795 (2008) 1, 0705.3127 [Bell:2007tv]; Nucl. Phys. B 822 (2009) 172, 0902.1915 [Bell:2009nk]
- M. Beneke, T. Huber, X.-Q. Li, Nucl. Phys. B 832 (2010) 109, 0911.3655 [Beneke:2009ek]
- M. Beneke, S. Jäger, Nucl. Phys. B 751 (2006) 160, hep-ph/0512351 [Beneke:2005vv]
- N. Kivel, JHEP 05 (2007) 019, hep-ph/0608291 [Kivel:2006xc]
- V. Pilipp, Nucl. Phys. B 794 (2008) 154, 0709.3214 [Pilipp:2007mg]
- G. Bell, M. Beneke, T. Huber, X.-Q. Li, Phys. Lett. B 750 (2015) 348, 1507.03700 [Bell:2015koa]; JHEP 04 (2020) 055, 2002.03262 [Bell:2020qus]
- T. Huber, S. Kränkl, X.-Q. Li, JHEP 09 (2016) 112, 1606.02888 [Huber:2016xod]
- S. Mantry, D. Pirjol, I. W. Stewart, Phys. Rev. D 68 (2003) 114009, hep-ph/0306254 [Mantry:2003uz]
- Z. L. Liu, M. Neubert, JHEP 04 (2020) 033, 1912.08818 [Liu:2019oav]
- M. Beneke et al., JHEP 03 (2019) 043, 1809.10631 [Beneke:2018gvs]
- H. D. Politzer, M. B. Wise, Phys. Lett. B 257 (1991) 399 [Politzer:1991au]; M. J. Dugan, B. Grinstein, Phys. Lett. B 255 (1991) 583 [Dugan:1990de]; J. D. Bjorken, Nucl. Phys. B Proc. Suppl. 11 (1989) 325 [Bjorken:1988kk]
- B. O. Lange, M. Neubert, Phys. Rev. Lett. 91 (2003) 102001 [Lange:2003ff]; A. G. Grozin, M. Neubert, Phys. Rev. D 55 (1997) 272 [Grozin:1996pq]
- R. Van Royen, V. F. Weisskopf, Nuovo Cim. A 50 (1967) 617 [VanRoyen:1967nq]
- R. Barbieri, R. Gatto, R. Kögerler, Z. Kunszt, Phys. Lett. B 57 (1975) 455 [Barbieri:1975ki]; W. Celmaster, Phys. Rev. D 19 (1979) 1517 [Celmaster:1978yz]
- R. Barbieri, E. d'Emilio, G. Curci, E. Remiddi, Nucl. Phys. B 154 (1979) 535 [Barbieri:1979be]
- R. Barbieri, R. Gatto, R. Kögerler, Phys. Lett. B 60 (1976) 183 [Barbieri:1975am]
- G. P. Lepage, L. Magnea, C. Nakhleh, U. Magnea, K. Hornbostel, Phys. Rev. D 46 (1992) 4052, hep-lat/9205007 [Lepage:1992tx]
- G. T. Bodwin, E. Braaten, G. P. Lepage, Phys. Rev. D 46 (1992) R1914, hep-lat/9205006 [Bodwin:1992ye]
- Z.-B. Kang, J.-W. Qiu, G. Sterman, Phys. Rev. Lett. 108 (2012) 102002, 1109.1520 [Kang:2011mg]
- I. Harris, L. M. Brown, Phys. Rev. 105 (1957) 1656 [Harris:1957zza]

- A. V. Manohar, T. Mehen, D. Pirjol, I. W. Stewart, Phys. Lett. B 539 (2002) 59, hep-ph/0204229 [Manohar:2002fd]

`tex/c_scet_bibitems.tex` renders all new entries (bare `\bibitem`s, house key scheme `<Surname…><Year>` / `<First>EtAl<Year>` of refs/NOTES.md, INSPIRE texkey in a
comment above each entry, titles and page ranges from INSPIRE records fetched on 2026-10-10 with exactly one hit each). New house keys: BauerPirjolStewart2002b,
ManoharEtAl2002, HillNeubert2003, ChayEtAl2005, KangLabunLee2015, BauerLangeOvanesyan2011, BauerEtAl2004a (BLMW), Schwartz2008, FlemingEtAl2008a/b, BauerManohar2004,
BecherNeubert2006, MochVermaserenVogt2005, KorchemskySterman1995/1999, DeRujulaEtAl1978, Bjorken1989, DuganGrinstein1991, PolitzerWise1991, GrozinNeubert1997,
BauerPirjolStewart2003, MantryPirjolStewart2003, BenekeFeldmann2004, BauerEtAl2004b (BPRS), BenekeEtAl2005, BauerEtAl2005, BenekeYang2006, BenekeJager2006, Kivel2007,
Pilipp2008, Bell2008, Bell2009, BenekeHuberLi2010, BellEtAl2015, BellEtAl2020, HuberKranklLi2016, LiuNeubert2020, BenekeEtAl2019, VanRoyenWeisskopf1967 (+Erratum),
BarbieriEtAl1975, BarbieriGattoKogerler1976, Celmaster1979, BarbieriEtAl1979, HarrisBrown1957, BodwinBraatenLepage1992, LepageEtAl1992, KangQiuSterman2012.
NB: the existing key BauerPirjolStewart2002 is PRD 65 054022 (decoupling); the power-counting paper is the new BauerPirjolStewart2002b.

---------------------------------------------------------------------------------------------------------------------

## 8. Files

* `DERIVATION.md` (this file)
* `run_all.sh`; `scripts/common.py`, `scripts/s1_scet_algebra.py`, `scripts/s1_wilson_decoupling.py`, `scripts/s2_thrust_oneloop.py`, `scripts/s2_thrust_rg.py`,
  `scripts/s3_nrqcd.py`, `scripts/s4_bbns.py`; `logs/*.log`, `logs/SUMMARY.txt`, `logs/s2_oneloop_results.json`
* LaTeX snippets (Chinese, monograph macros and rigor tags, plain-TikZ figures; labels follow the blueprint registry, cross-chapter references are given as
  `% XREF:` comments so that each file compiles stand-alone):
  - `tex/c_scet_scet.tex` — Ch. 14 first half: conventions, D14.1 `def:scet-modes` (table + `fig:scet-modes`), mode interactions, multipole expansion,
    projectors, exact tree-level $\mathcal L_{\xi\xi}$, D14.2 `def:scet-lagrangian` (quark, gluon, ghost, usoft-covariant gauge fixing), Feynman rules,
    P14.3 `prop:scet-wilson` (with proof), P14.4 `prop:scet-gauge`, key identity, T14.5 `thm:usoft-decoupling` (full proof, two versions), corollary, remarks on
    leading power / $i0$ direction / QCD status (`fig:usoft-decoupling`), SCET$_{\rm II}$ soft Wilson line, rapidity divergences, Glauber, D14.6 `def:zero-bin`,
    R14.10 `rem:eft-assumptions`, status table.
  - `tex/c_scet_thrust.tex` — T14.8 `thm:thrust-factorization` (proof sketch, `fig:thrust-HJJS`), P14.7 `prop:hard-matching`, one-loop jet and soft functions
    (with proofs, `fig:thrust-oneloop`), RG consistency (`prop:thrust-RG`, table of anomalous dimensions with the corrected $\Gamma_1$), E14.9 fixed-order check,
    LL exponent, non-perturbative remark, status table.
  - `tex/c_scet_bdecays.tex` — P14.12 `prop:b-pipi` (split status), power counting, $O(\alpha_s)$ vertex term and RG origin of $12\ln(m_b/\mu)$, hard spectator
    term and $X_H$, annihilation and $X_A$ (prescription dependence), SCET-vs-QCDF dispute, T14.11 `thm:b-dpi` (with the endpoint assumption, proof sketch,
    `fig:qcdf`, `fig:b-dpi`), related results, status table.
  - `tex/c_scet_nrqcd.tex` — Ch. 15: D15.1 `def:nrqcd` (+ BBL convention remark), velocity table, T15.3 `thm:nrqcd-decay`, P15.2, E15.4, LO EM widths and
    one-loop $c_v$ (with proofs), $\eta_c\to\gamma\gamma$ remark, Cj15.5 `conj:nrqcd-production`, NQS, P15.6, `fig:nrqcd-decay`, `fig:nqs-nnlo`, status table.
  - `tex/c_scet_bibitems.tex` — 47 new bibliography entries (bare `\bibitem`s, to be appended to `research/refs/refs_bibitems.tex`).
  - `tex/test_c_scet.tex` (+ `test_c_scet.pdf`, 42 pp., `test_c_scet.log`) — test driver; `tex/preamble_fact.tex` and `tex/refs_bibitems.tex` are copies of
    `common/preamble_fact.tex` and `research/refs/refs_bibitems.tex` made for the build. Build: `cd` into `tex/`, `xelatex test_c_scet.tex` three times.
    Result: no errors, no undefined references or citations; one overfull box of 5 pt; one font-substitution warning caused by the preamble (§6 item 18).
