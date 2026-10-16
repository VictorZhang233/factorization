# $e^+e^-\to$ hadrons: LO, $O(\alpha_s)$ in DR, the Euclidean correlator at two loops, all-order IR finiteness, KLN and Sterman–Weinberg jets

Directory: `"/Users/hao-cheng/Desktop/theorem proof/qcd_factorization_work/research/c_ee"`
(every script runs with `python3 -I <script>.py`; logs `*.log` are the outputs of the last run; see §11).

Everything below was derived from scratch from the Feynman rules of `CONTEXT.md`. It was checked by computer
algebra (sympy, **exact in $\varepsilon$** wherever stated) and by independent numerics (mpmath/numpy).
**All 57 automated checks pass**: 27 in `ee_nlo.py`, 18 in `pi_twoloop.py`, 1 in `cut_identity_analytic.py`, 6 in `sw_jets.py`,
5 in `rg_structure.py`, plus the trace-engine self-test. Literature statements that I could not check against the
original text are marked **[unverified]**. Every bibliographic entry in §12 was checked on INSPIRE-HEP and
Crossref (`refs_verification_log.txt`).

---------------------------------------------------------------------------------------------------

## 0. Results at a glance

Units and conventions: §1.  $a\equiv\alpha_s(\mu)/\pi$, $L\equiv\ln(-q^2/\mu^2)$, $\ell\equiv\ln(s/\mu^2)$,
$c_\Gamma\equiv\Gamma(1+\varepsilon)\Gamma^2(1-\varepsilon)/\Gamma(1-2\varepsilon)$, $D=4-2\varepsilon$.

| # | result | status |
|---|---|---|
| 1 | $\sigma_0=\dfrac{4\pi\alpha^2}{3s}N_c\sum_q e_q^2$, $R_0=N_c\sum_q e_q^2$ | PASS (sympy, from the full $2\to2$ matrix element) |
| 2a | $F(s+i0)=1+\dfrac{\alpha_sC_F}{4\pi}\Big[-\dfrac{2}{\varepsilon^2}+\dfrac{2L-3}{\varepsilon}-L^2+3L-8+\zeta_2+O(\varepsilon)\Big]$, $L=\ell-i\pi$ ($\overline{\rm MS}$) | PASS; exact form below |
| 2b | real: $\dfrac{\rho_R}{\rho_0}=\dfrac{\alpha_sC_F}{2\pi}\Big(\dfrac{4\pi\mu_0^2}{s}\Big)^{\!\varepsilon}c_\Gamma\Big[\dfrac{2}{\varepsilon^2}+\dfrac{3}{\varepsilon}+\dfrac{19}{2}-\pi^2+O(\varepsilon)\Big]$; virtual: same prefactor $\times\Big[-\dfrac{2}{\varepsilon^2}-\dfrac{3}{\varepsilon}-8+\pi^2+O(\varepsilon)\Big]$ | PASS (exact in $\varepsilon$) |
| 2c | $R=R_0\big(1+\tfrac{3C_F}{4}\tfrac{\alpha_s}{\pi}\big)=R_0\big(1+\tfrac{\alpha_s}{\pi}\big)$; $1/\varepsilon^2$ and $1/\varepsilon$ cancel exactly | PASS |
| 3a | $\Pi_{\overline{\rm MS}}(q^2)=\dfrac{N_c\sum e_q^2}{12\pi^2}\Big[\dfrac53-L+\dfrac{\alpha_s}{\pi}\dfrac{3C_F}{4}\Big(\dfrac{55}{12}-4\zeta_3-L\Big)\Big]+O(\alpha_s^2)$ | PASS (genuine 2-loop Euclidean computation) |
| 3b | exact bare 2-loop result: $\Pi^{(1)}_{\rm bare}=N_ce_q^2C_F\dfrac{g_0^2(Q^2)^{-2\varepsilon}}{(4\pi)^D}\big[r_1G(1,1)^2+r_2G(1,1)G(1{+}\varepsilon,1)\big]$ | PASS (transversality, IBP cross-checks) |
| 3c | **exact-in-$\varepsilon$ cutting identity** $2(D-1)s\,{\rm Im}\,\Pi^{(1)}_{\rm bare}(s+i0)=\rho_V+\rho_R$ | PASS (analytic, termwise; and 30 digits at 5 values of $\varepsilon$) |
| 3d | $\mu^2\frac{d\Pi}{d\mu^2}=\frac{N_c\sum e_q^2}{12\pi^2}(1+a)$; Adler $D(Q^2)=N_c\sum e_q^2(1+a)$; $R=12\pi\,{\rm Im}\,\Pi(s+i0)$ | PASS |
| 3e | all orders: $r_1=d_1,\ r_2=d_2,\ r_3=d_3-\frac{\pi^2}{3}b_0^2d_1,\ r_4=d_4-\pi^2\big(b_0^2d_2+\frac56b_0b_1d_1\big)$ | PASS (two independent continuations) |
| 4a | KLN: $\sigma(q\bar q)$ and $\sigma(q\bar qg)$ each $\propto\pm2/\varepsilon^2$; the sum is finite. $d\sigma/dx_q$ keeps $-\frac1\varepsilon\frac{\alpha_s}{2\pi}P_{qq}(x)$ | PASS (moments $n=0..3$) |
| 4b | **Sterman–Weinberg**: $\sigma_{2j}=\sigma_0\big\{1-\frac{4}{3}\frac{\alpha_s}{\pi}\big[4\ln\delta\ln 2\epsilon+3\ln\delta+\frac{\pi^2}{3}-\frac52\big]\big\}$, with $\epsilon$ = fraction of the **total** energy $\sqrt s$ and $\epsilon<\delta\ll1$ | PASS (exact numerics) |
| 4b′ | the task's "$4\ln\delta\ln\epsilon$" form is correct only if $\epsilon$ is the fraction of the **beam** energy $\sqrt s/2$ | see §8 |

---------------------------------------------------------------------------------------------------

## 1. Conventions and normalisation

* $\hbar=c=1$, metric $(+,-,-,-)$; quark–gluon vertex $ig\gamma^\mu t^a$, ${\rm Tr}(t^at^b)=\frac12\delta^{ab}$, $C_F=\frac43$;
  gluon propagator $-ig_{\mu\nu}\delta^{ab}/(k^2+i0)$ (Feynman gauge); quark propagator $i\slashed p/(p^2+i0)$.
* CDR: $D=4-2\varepsilon$, $\{\gamma^\mu,\gamma^\nu\}=2g^{\mu\nu}$, $g^\mu{}_\mu=D$, ${\rm Tr}\,\mathbb 1=4$. No $\gamma_5$ appears.
* Bare coupling $g_0^2=4\pi\alpha_s(\mu)\mu^{2\varepsilon}e^{\varepsilon\gamma_E}(4\pi)^{-\varepsilon}$ ($\overline{\rm MS}$, as in `CONTEXT.md`).
  Where I write $\mu_0$ I mean the bare-coupling scale, $g_0^2=4\pi\alpha_s\mu_0^{2\varepsilon}$ (no $\overline{\rm MS}$ factor).
  At $O(\alpha_s)$ in $R$ no coupling renormalisation is needed.
* Current $j^\mu=\sum_q e_q\,\bar q\gamma^\mu q$ (in units of $e$).
* **Correlator** (sign chosen so that ${\rm Im}\,\Pi>0$):
  $$\Pi^{\mu\nu}(q)=i\!\int\! d^4x\,e^{iq\cdot x}\langle0|T\,j^\mu(x)j^\nu(0)|0\rangle=(q^\mu q^\nu-q^2g^{\mu\nu})\,\Pi(q^2).\tag{1.1}$$
  Relation to the QED vacuum polarisation of Peskin–Schroeder ($\Pi_{\rm PS}^{\mu\nu}=(q^2g^{\mu\nu}-q^\mu q^\nu)\Pi_{\rm PS}$, the 1PI photon self-energy):
  at lowest order in $e$, $\Pi_{\rm PS}=-e^2\,\Pi$.
* **Spectral (Wightman) function**:
  $$W^{\mu\nu}(q)=\int d^4x\,e^{iq\cdot x}\langle0|j^\mu(x)j^\nu(0)|0\rangle=\sum_X(2\pi)^4\delta^4(q-p_X)\langle0|j^\mu(0)|X\rangle\langle X|j^\nu(0)|0\rangle
  =2\,{\rm Im}\,\Pi^{\mu\nu}(q)\quad(q^0>0).\tag{1.2}$$
  The factor 2 is the Källén–Lehmann relation ${\rm Im}\,\Pi=\pi\rho$. Here it is *checked*, not assumed: exactly in $D$ at LO (check A5) and at $O(\alpha_s)$ (check C1 in `pi_twoloop.py`).
* **Cross section and $R$** (one-photon exchange, massless leptons, lowest order in $\alpha$). With the
  spin-averaged lepton tensor $L_{\mu\nu}=k_{1\mu}k_{2\nu}+k_{1\nu}k_{2\mu}-g_{\mu\nu}k_1\!\cdot\!k_2$ one has
  $L_{\mu\nu}(q^\mu q^\nu-q^2g^{\mu\nu})=s^2$, so
  $$\sigma=\frac{1}{2s}\frac{e^4}{s^2}L_{\mu\nu}W^{\mu\nu}=\frac{16\pi^2\alpha^2}{s}{\rm Im}\,\Pi(s+i0),\qquad
  R(s)\equiv\frac{\sigma(e^+e^-\to{\rm hadrons})}{\sigma(e^+e^-\to\mu^+\mu^-)}=12\pi\,{\rm Im}\,\Pi(s+i0),\tag{1.3}$$
  with $\sigma_{\mu\mu}=4\pi\alpha^2/(3s)$.
* **$D$-dimensional bookkeeping.** At $O(\alpha_s)$ I compare only hadronic objects. I use
  $\rho(s)\equiv-g_{\mu\nu}W^{\mu\nu}$, which equals $2(D-1)\,s\,{\rm Im}\,\Pi(s)$ in any $D$ by transversality. The ratio
  $R^{(1)}/R_0=\lim_{\varepsilon\to0}(\rho_V+\rho_R)/\rho_0$ does not depend on how the leptonic side is continued to $D$ dimensions,
  because the poles cancel.

---------------------------------------------------------------------------------------------------

## 2. Leading order

**2.1 Matrix element (4D).** For $e^-(k_1)e^+(k_2)\to q(p_1)\bar q(p_2)$:
$\sum_{\rm spins,col}|M|^2=\frac{e^4e_q^2N_c}{s^2}{\rm Tr}[\slashed k_2\gamma^\mu\slashed k_1\gamma^\nu]{\rm Tr}[\slashed p_1\gamma_\mu\slashed p_2\gamma_\nu]
=8e^4e_q^2N_c\frac{t^2+u^2}{s^2}$ (check A2). So $\frac{d\sigma}{d\Omega}=\frac{\alpha^2}{4s}N_ce_q^2(1+\cos^2\theta)$ and
$$\boxed{\sigma_0=\frac{4\pi\alpha^2}{3s}N_c\sum_qe_q^2,\qquad R_0=N_c\sum_q e_q^2}\tag{2.1}$$
(check A3). Numerically $R_0=2,\ \frac{10}{3},\ \frac{11}{3}$ for $n_f=3,4,5$.

**2.2 $D$-dimensional two-body phase space** (massless):
$$\Phi_2=\int\!d\Phi_2=\frac{1}{8\pi}\Big(\frac{4\pi}{s}\Big)^{\varepsilon}\frac{\Gamma(1-\varepsilon)}{\Gamma(2-2\varepsilon)}\tag{2.2}$$
(obtained from $(2\pi)^{2-D}\Omega_{D-1}(\sqrt s/2)^{D-4}/8$ and the duplication formula; check A4 compares the two forms).

**2.3 LO spectral weight and correlator in $D$ dimensions.** $-g_{\mu\nu}{\rm Tr}[\slashed p_1\gamma^\mu\slashed p_2\gamma^\nu]=2(D-2)s$ (A1), so
$\rho_0=N_ce_q^2\,2(D-2)s\,\Phi_2$. The one-loop correlator is
$$\Pi_0(q^2)=N_ce_q^2\,\frac{2(D-2)}{D-1}\,\frac{G(1,1)}{(4\pi)^{D/2}}(-q^2-i0)^{-\varepsilon},\qquad G(1,1)=\frac{\Gamma(\varepsilon)\Gamma(1-\varepsilon)^2}{\Gamma(2-2\varepsilon)}.\tag{2.3}$$
Since $(-s-i0)^{-\varepsilon}=s^{-\varepsilon}e^{i\pi\varepsilon}$ and $\Gamma(\varepsilon)\Gamma(1-\varepsilon)\sin\pi\varepsilon=\pi$, one finds
$\rho_0=2(D-1)s\,{\rm Im}\,\Pi_0(s+i0)$ **for every $\varepsilon$** (A5). At $D=4$ this gives ${\rm Im}\,\Pi_0=N_ce_q^2/(12\pi)$, hence $R_0$ (A6).
$\overline{\rm MS}$ (see §4.3): $\Pi_0^{\overline{\rm MS}}=\frac{N_ce_q^2}{12\pi^2}\big(\frac53-L\big)$.

---------------------------------------------------------------------------------------------------

## 3. $O(\alpha_s)$ in dimensional regularisation

### 3.1 One-loop massless timelike quark form factor
$$\Lambda^\mu=-ig_0^2C_F\!\int\!\frac{d^Dl}{(2\pi)^D}\frac{\gamma^\alpha(\slashed p_1-\slashed l)\gamma^\mu(-\slashed p_2-\slashed l)\gamma_\alpha}{l^2\,(p_1-l)^2\,(p_2+l)^2},\qquad
F^{(1)}=\frac{{\rm Tr}[\slashed p_1\Lambda^\mu\slashed p_2\gamma_\mu]}{{\rm Tr}[\slashed p_1\gamma^\mu\slashed p_2\gamma_\mu]}.$$
For massless on-shell spinors the projection is exact, because chirality conservation leaves only the $\gamma^\mu$ structure.
Scalar products become inverse propagators: $l\!\cdot\!p_1=(D_a-D_b)/2$, $l\!\cdot\!p_2=(D_c-D_a)/2$. Only three
integrals survive (the others are scaleless):
$J(1,1,1)=-\frac{i}{(4\pi)^{D/2}}\frac{\Gamma(1+\varepsilon)\Gamma(-\varepsilon)^2}{\Gamma(1-2\varepsilon)}(-s-i0)^{-1-\varepsilon}$,
$J(0,1,1)=\frac{i}{(4\pi)^{D/2}}G(1,1)(-s-i0)^{-\varepsilon}$, $J(-1,1,1)=-\frac s2J(0,1,1)$. The result is **exact in $\varepsilon$**:
$$\boxed{F^{(1)}(q^2)=-\frac{\alpha_sC_F}{4\pi}\Big(\frac{4\pi\mu_0^2}{-q^2-i0}\Big)^{\varepsilon}c_\Gamma\,
\frac{2-\varepsilon+2\varepsilon^2}{\varepsilon^2(1-2\varepsilon)}}
=\frac{\alpha_sC_F}{4\pi}\Big(\frac{4\pi\mu_0^2}{-q^2-i0}\Big)^{\varepsilon}c_\Gamma\Big[-\frac{2}{\varepsilon^2}-\frac3\varepsilon-8-16\varepsilon+O(\varepsilon^2)\Big]\tag{3.1}$$
(checks B0, B1). In $\overline{\rm MS}$ normalisation, $e^{\varepsilon\gamma_E}c_\Gamma=1-\frac{\zeta_2}{2}\varepsilon^2-\frac73\zeta_3\varepsilon^3+\dots$, so
$$F^{(1)}=\frac{\alpha_sC_F}{4\pi}\Big[-\frac{2}{\varepsilon^2}+\frac{2L-3}{\varepsilon}-L^2+3L-8+\zeta_2
+\varepsilon\big(\dots\big)\Big],\qquad L=\ln\frac{-q^2-i0}{\mu^2}\tag{3.2}$$
(B4). At $L=0$ the $O(\varepsilon)$ term is $-16+\frac32\zeta_2+\frac{14}{3}\zeta_3$ (B5). This agrees with the one-loop coefficient
quoted by Moch–Vermaseren–Vogt 2005 **[recalled, not re-read]**.
**Timelike, $q^2=s+i0$:** $L=\ell-i\pi$, so
$${\rm Im}\,F^{(1)}=\frac{\alpha_sC_F}{4\pi}\Big[-\frac{2\pi}{\varepsilon}+2\pi\ell-3\pi\Big],\qquad
2{\rm Re}\,F^{(1)}=\frac{\alpha_sC_F}{2\pi}\Big[-\frac2{\varepsilon^2}+\frac{2\ell-3}{\varepsilon}-\ell^2+3\ell-8+\zeta_2+\pi^2\Big].\tag{3.3}$$
The divergent phase drops out of $|F|^2$. Because ${\rm Re}L^2=\ell^2-\pi^2$, the timelike value exceeds the spacelike one by $\pi^2$ (B6).
In $c_\Gamma$ normalisation the exact result is $2{\rm Re}F^{(1)}=\frac{\alpha_sC_F}{2\pi}(\frac{4\pi\mu_0^2}{s})^\varepsilon c_\Gamma\cos(\pi\varepsilon)\,f(\varepsilon)$
with $f=-(2-\varepsilon+2\varepsilon^2)/(\varepsilon^2(1-2\varepsilon))$, which gives $[-\frac2{\varepsilon^2}-\frac3\varepsilon-8+\pi^2+O(\varepsilon)]$ (B3).
*Origin of the poles.* In DR the external self-energies are scaleless and vanish. The UV pole of the vertex graph is
cancelled by the UV part of the (zero) on-shell LSZ factor, by the Ward identity $Z_1=Z_2$. The conserved current needs no
renormalisation. So **all poles of $F$ are infrared**: $1/\varepsilon^2$ is soft–collinear, $1/\varepsilon$ is soft or collinear.

### 3.2 Real emission $\gamma^*\to q(p_1)\bar q(p_2)g(k)$
Amplitude: $M^\nu=-g_0t^a\,\bar u(p_1)\big[\gamma^\alpha(\slashed p_1+\slashed k)\gamma^\nu/s_{13}-\gamma^\nu(\slashed p_2+\slashed k)\gamma^\alpha/s_{23}\big]v(p_2)\varepsilon^*_\alpha$.
The polarisation sum $-g_{\alpha\beta}$ is exact here, since $k_\alpha M^{\alpha}=0$ with a single gluon. With $y_{ij}=2p_i\!\cdot\!p_j/s$ and $y_{12}+y_{13}+y_{23}=1$:
$$-g_{\mu\nu}\sum_{\rm pol,col} M^\mu M^{\nu*}=8(1-\varepsilon)g_0^2C_FN_ce_q^2\Big[(1-\varepsilon)\Big(\frac{y_{13}}{y_{23}}+\frac{y_{23}}{y_{13}}\Big)+\frac{2y_{12}}{y_{13}y_{23}}-2\varepsilon\Big]\tag{3.4}$$
(C1, from my own $D$-dimensional trace code `diracD.py`). At $\varepsilon=0$, with $x_i=2E_i/\sqrt s$, this is $\propto(x_1^2+x_2^2)/((1-x_1)(1-x_2))$ (C2).
**Three-body phase space** (derived by iterating two-body phase spaces; check C3):
$$d\Phi_3=\frac{(4\pi)^{2\varepsilon-3}s^{1-2\varepsilon}}{2\,\Gamma(2-2\varepsilon)}\,dy_{13}\,dy_{23}\,(y_{12}y_{13}y_{23})^{-\varepsilon}.\tag{3.5}$$
The angular factor $(1-c^2)^{-\varepsilon}$ in the $P_{23}$ rest frame combines with $(M^2)^{-\varepsilon}(1-M^2/s)^{1-2\varepsilon}$ into the symmetric form shown.
Normalising to $\rho_0$ (prefactor check C4) and using Dirichlet integrals
$\int[dy]\,y_{12}^{a-1}y_{13}^{b-1}y_{23}^{c-1}=\Gamma(a)\Gamma(b)\Gamma(c)/\Gamma(a+b+c)$:
$$\boxed{\frac{\rho_R}{\rho_0}=\frac{\alpha_sC_F}{2\pi}\Big(\frac{4\pi\mu_0^2}{s}\Big)^{\varepsilon}
\frac{2(1-2\varepsilon)(2-2\varepsilon+\varepsilon^2)\,\Gamma(1-\varepsilon)^2}{\varepsilon^2(1-3\varepsilon)(2-3\varepsilon)\,\Gamma(1-3\varepsilon)}}
=\frac{\alpha_sC_F}{2\pi}\Big(\frac{4\pi\mu_0^2}{s}\Big)^{\varepsilon}c_\Gamma\Big[\frac2{\varepsilon^2}+\frac3\varepsilon+\frac{19}{2}-\pi^2+O(\varepsilon)\Big]\tag{3.6}$$
(C4b, C5). In 4D: $\frac{1}{\sigma_0}\frac{d\sigma}{dx_1dx_2}=\frac{C_F\alpha_s}{2\pi}\frac{x_1^2+x_2^2}{(1-x_1)(1-x_2)}$.

### 3.3 Sum and cancellation of poles
$$\frac{\rho_R+\rho_V}{\rho_0}=\frac{\alpha_sC_F}{2\pi}\Big(\frac{4\pi\mu_0^2}{s}\Big)^{\varepsilon}\Big[\frac32+\Big(\frac{45}{4}-12\zeta_3-\frac32\gamma_E\Big)\varepsilon+O(\varepsilon^2)\Big]
\;\Rightarrow\;\boxed{R=R_0\Big(1+\frac{3C_F}{4}\frac{\alpha_s}{\pi}\Big)=R_0\Big(1+\frac{\alpha_s}{\pi}\Big)}\tag{3.7}$$
(D1–D4). The $1/\varepsilon^2$ and $1/\varepsilon$ poles cancel identically. The finite part $\frac32=\frac{19}{2}-8$ does not depend on the common
normalisation. It would depend on it if real and virtual were normalised differently: the two $\Gamma$-prefactors differ at $O(\varepsilon^2)$,
$\Gamma(1-\varepsilon)^2/\Gamma(1-3\varepsilon)=c_\Gamma(1-\frac{\pi^2}{2}\varepsilon^2+\dots)$, and this difference is precisely the $-\pi^2$ in $\frac{19}{2}-\pi^2$.
Literature: Appelquist–Georgi 1973, Zee 1973 ($R=R_0(1+\alpha_s/\pi)$). The brackets $[2/\varepsilon^2+3/\varepsilon+19/2-\pi^2]$ and
$[-2/\varepsilon^2-3/\varepsilon-8+\pi^2]$ are those quoted in Ellis–Stirling–Webber, Ch. 3. I could not re-read the book to confirm that its
prefactor $H(\varepsilon)$ coincides with our $c_\Gamma(4\pi\mu^2/s)^\varepsilon$ through $O(\varepsilon^2)$, so this is **[unverified]**.

---------------------------------------------------------------------------------------------------

## 4. The vector correlator at two loops in the Euclidean region

### 4.1 Set-up
The $O(g^2)$ diagrams (Feynman gauge) are the gluon exchange across the quark loop (V) and the two self-energy insertions (S1, S2).
All carry the factor $i\cdot(-1)\cdot(ig)^2\cdot(-i)\cdot i^4\cdot C_FN_c=g^2C_FN_c$. With $r=k+l$ the denominators are those of the
standard propagator topology
$$D_1=k^2,\ D_2=(k-q)^2,\ D_3=r^2,\ D_4=(r-q)^2,\ D_5=(k-r)^2:\quad V\!:(1,1,1,1,1),\ S_1\!:(2,1,1,0,1),\ S_2\!:(1,2,0,1,1).$$
Traces come from `diracD.py`, contracted with $-g_{\mu\nu}$ (for $\Pi$) and with $q_\mu q_\nu$ (for the Ward identity).
All five scalar products are linear in the $D_i$. After Wick rotation
($\int\!\!\int\frac{d^Dk\,d^Dr}{(2\pi)^{2D}}\prod D_i^{-a_i}=-\frac{(-1)^{\sum a}}{(4\pi)^D}\hat I(a)(Q^2)^{D-\sum a}$, $Q^2=-q^2$) one needs
$\hat I(a)=\int\!\!\int\frac{d^Dk\,d^Dr}{\pi^D}\prod D_i^{-a_i}$ for integer $a_i$ of either sign.

**Evaluation (exact in $D$).**
* $G(a,b)$: $\int\frac{d^Dk}{\pi^{D/2}}\frac{1}{(k^2)^a((k-q)^2)^b}=G(a,b)(Q^2)^{D/2-a-b}$, with
  $G(a,b)=\frac{\Gamma(a+b-D/2)\Gamma(D/2-a)\Gamma(D/2-b)}{\Gamma(a)\Gamma(b)\Gamma(D-a-b)}$.
* One-loop tensor formula, derived with Feynman parameters ($k=l+xp$):
  $$\int\!\frac{d^Dk}{\pi^{D/2}}\frac{k^{\mu_1}\cdots k^{\mu_m}}{(k^2)^\alpha((p-k)^2)^\beta}=\sum_t A(m,t)(p^2)^{\frac D2+t-\alpha-\beta}\{g^tp^{m-2t}\}^{\mu_1..\mu_m},\quad
  A=\frac{\Gamma(\alpha+\beta-\frac D2-t)\Gamma(\frac D2-\alpha+m-t)\Gamma(\frac D2-\beta+t)}{2^t\Gamma(\alpha)\Gamma(\beta)\Gamma(D-\alpha-\beta+m)},$$
  where $\{\cdot\}$ is the sum of the $m!/(2^tt!(m-2t)!)$ distinct terms. This handles numerators $D_5^{n}$ (factorised case) and
  $D_4^n$ (nested case); the remaining cases follow by the symmetries $(k,r)\to(q-k,q-r)$ and $k\leftrightarrow r$.
* IBP (triangle rule, Chetyrkin–Tkachov 1981), from $\int d^Dk\,\partial_k\!\cdot\![(k-r)\cdots]=0$:
  $$(D-a_1-a_2-2a_5)\,\hat I=a_1\big[\hat I(1^+5^-)-\hat I(1^+3^-)\big]+a_2\big[\hat I(2^+5^-)-\hat I(2^+4^-)\big].$$
  For instance $\hat I(1,1,1,1,1)=-\frac1\varepsilon G(1,1)\big[G(2,1)-G(2,1+\varepsilon)\big]=6\zeta_3+O(\varepsilon)$ (T2). The triangle on
  lines (3,4,5) gives the same result (T3); a nested integral with a numerator matches a hand reduction (T4).

### 4.2 Bare result (exact in $\varepsilon$)
$q_\mu q_\nu\Pi^{\mu\nu}=0$ exactly at one and two loops (W1a, W1b), a strong check of traces, routing and integrals. Every
integral reduces to two transcendental structures (P0):
$$\boxed{\Pi^{(1)}_{\rm bare}=N_ce_q^2\,C_F\frac{g_0^2\,(Q^2)^{-2\varepsilon}}{(4\pi)^D}\Big[r_1\,G(1,1)^2+r_2\,G(1,1)\,G(1{+}\varepsilon,1)\Big],\quad
r_1=-\frac{4(1-\varepsilon)(2-\varepsilon+2\varepsilon^2)}{\varepsilon(3-2\varepsilon)},\ \ r_2=\frac{16(1-\varepsilon)(1-2\varepsilon)(2-2\varepsilon+\varepsilon^2)}{\varepsilon(3-2\varepsilon)(2-3\varepsilon)}}\tag{4.1}$$
with $G(1{+}\varepsilon,1)=\frac{\Gamma(2\varepsilon)\Gamma(1-2\varepsilon)\Gamma(1-\varepsilon)}{\Gamma(1+\varepsilon)\Gamma(2-3\varepsilon)}$ and $Q^2=-q^2-i0$.
$r_1$ carries the form-factor polynomial $2-\varepsilon+2\varepsilon^2$ and $r_2$ the real-emission polynomial $2-2\varepsilon+\varepsilon^2$:
the $G(1,1)^2$ structure is the two-particle cut and $G(1,1)G(1+\varepsilon,1)$ the three-particle cut.

Expansion with the $\overline{\rm MS}$ factor (units $\frac{\alpha_s}{\pi}C_F\frac{N_ce_q^2}{12\pi^2}$; $L=\ln(Q^2/\mu^2)$):
$$\Pi^{(1)}_{\rm bare}\to\frac{3}{8\varepsilon}+\frac{55}{16}-3\zeta_3-\frac34L+O(\varepsilon).\tag{4.2}$$
Diagram by diagram (P2b): ${\rm V}=\frac{1}{4\varepsilon^2}+\frac{17/12-L/2}{\varepsilon}+\frac{L^2}{2}-\frac{17L}{6}-3\zeta_3-\frac{\pi^2}{24}+\frac{259}{36}$ and
${\rm S_1+S_2}=-\frac{1}{4\varepsilon^2}+\frac{L/2-25/24}{\varepsilon}-\frac{L^2}{2}+\frac{25L}{12}+\frac{\pi^2}{24}-\frac{541}{144}$. The $1/\varepsilon^2$ and
the non-local $L/\varepsilon$ terms cancel in the sum (Ward identity $Z_1=Z_2$: subdivergences cancel). What remains is a
**local** simple pole, removed by the additive (contact-term) counterterm of $\Pi$ (P2).

### 4.3 $\overline{\rm MS}$ renormalisation, RG, Adler function
$\Pi$ has mass dimension $-2\varepsilon$. Define $\hat\Pi=\mu_{\rm MS}^{2\varepsilon}\Pi_{\rm bare}$ with $\mu_{\rm MS}^2=\mu^2e^{\gamma_E}/4\pi$ and subtract pure poles in $\alpha_s(\mu)$:
$$\boxed{\Pi_{\overline{\rm MS}}(q^2)=\frac{N_c e_q^2}{12\pi^2}\Big[\frac53-L+\frac{\alpha_s}{\pi}\,\frac{3C_F}{4}\Big(\frac{55}{12}-4\zeta_3-L\Big)\Big]+O(\alpha_s^2),\qquad L=\ln\frac{-q^2}{\mu^2}}\tag{4.3}$$
(P3a, P3b). The constants are scheme dependent (contact terms). The $L$-coefficients are not.
With $Z=z_0/\varepsilon+\alpha_sz_1/\varepsilon+\dots$ and $\mu^2d\alpha_s/d\mu^2=-\varepsilon\alpha_s+\beta(\alpha_s)$:
$$\mu^2\frac{d\Pi}{d\mu^2}=z_0+2z_1\alpha_s+\dots=\frac{N_ce_q^2}{12\pi^2}\Big(1+\frac{3C_F}{4}\frac{\alpha_s}{\pi}\Big)\quad(q\text{-independent}),\tag{4.4}$$
$$D(Q^2)\equiv-12\pi^2Q^2\frac{d\Pi}{dQ^2}=N_ce_q^2\Big(1+\frac{3C_F}{4}\frac{\alpha_s}{\pi}\Big)\quad\text{(finite, $\mu$-independent, Euclidean)}\tag{4.5}$$
(P4, P5). [Abelian check: $C_F\to1$ gives the two-loop QED $\beta$ function $\propto1+\frac34\frac{\alpha}{\pi}$.]
**Continuation:** $\Pi$ is analytic in $q^2\in\mathbb C\setminus[0,\infty)$, and $L\to\ell-i\pi$ at $q^2=s+i0$:
$${\rm Im}\,\Pi(s+i0)=\frac{N_ce_q^2}{12\pi}\Big(1+\frac{3C_F}{4}\frac{\alpha_s}{\pi}\Big)\ \Rightarrow\ R=12\pi{\rm Im}\,\Pi=R_0(1+\alpha_s/\pi)\quad\text{(C2).}$$

### 4.4 Exact-in-$\varepsilon$ cutting identity
Since $(Q^2)^{-2\varepsilon}\to s^{-2\varepsilon}e^{2\pi i\varepsilon}$,
$$2(D-1)\,s\,{\rm Im}\,\Pi^{(1)}_{\rm bare}(s+i0)=2(D-1)s\,N_ce_q^2C_F\frac{g_0^2s^{-2\varepsilon}\sin(2\pi\varepsilon)}{(4\pi)^D}\big[r_1G_{11}^2+r_2G_{11}G_{1+\varepsilon,1}\big]
\overset{!}{=}\rho_V+\rho_R\tag{4.6}$$
with $\rho_{V,R}$ from (3.1)–(3.6). The ratio LHS/RHS is $1$ to $30$ digits at $\varepsilon=0.1,-0.2,0.31,-0.43,0.0123$ (C1). It is also proved
**analytically, term by term** (`cut_identity_analytic.py`, check X1): with $\sin2\pi\varepsilon=2\sin\pi\varepsilon\cos\pi\varepsilon$ and the reflection formulas
$\Gamma(z)\Gamma(1-z)=\pi/\sin\pi z$ ($z=\varepsilon,2\varepsilon$), the $r_1G_{11}^2$ term equals $\rho_V$ and the $r_2G_{11}G_{1+\varepsilon,1}$ term equals $\rho_R$; both ratios simplify
symbolically to exactly $1$. This is unitarity at
$O(g^2)$ verified in $D$ dimensions: two independent calculations (Euclidean two-loop integrals versus Minkowski phase-space integrals) agree
before $\varepsilon\to0$.

---------------------------------------------------------------------------------------------------

## 5. IR finiteness of $R$ to all orders in perturbation theory: the rigorous argument

**Theorem 5.1.** In massless QCD with $n_f$ flavours, renormalised in $\overline{\rm MS}$, let $R^{(n)}(s;\varepsilon)$ be the coefficient of $a^n$
($a=\alpha_s(\mu)/\pi$) in the sum over all cut diagrams (= all partonic final states, with physical polarisations) for $\gamma^*\to$ partons.
Compute it with $D$-dimensional loops and phase space, including the $\overline{\rm MS}$ counterterm insertions, and normalise it to $\rho_0$. Then for every $n$:
(i) $\lim_{\varepsilon\to0}R^{(n)}$ exists;
(ii) for $n\ge1$ the limit is a polynomial of degree $\le n-1$ in $\ln(s/\mu^2)$ ($R^{(0)}=R_0$);
(iii) $R=12\pi\,{\rm Im}\,\Pi_{\overline{\rm MS}}(s+i0)$, where $\Pi_{\overline{\rm MS}}$ is the Euclidean renormalised correlator continued analytically.

**Ingredients (precise statements and sources).**
1. **Euclidean IR finiteness at non-exceptional momenta.**
   *Statement:* in a renormalisable theory with massless fields and **no super-renormalisable couplings**, the renormalised Green functions at
   non-exceptional Euclidean momenta (no proper partial sum of external momenta vanishes) are finite at every order. This holds when
   the UV renormalisation does not subtract at zero momentum, e.g. MS/$\overline{\rm MS}$, or BPHZL with the auxiliary-mass subtractions.
   *Sources:* Poggio–Quinn 1976 give a general physics-level proof; their abstract states it for "any renormalizable (but not
   superrenormalizable) field theory containing zero-mass particles". Their corollary is that physical discontinuities are also IR finite,
   which is exactly the use made here. Mathematically rigorous versions are Lowenstein–Zimmermann 1975 (power-counting theorem with
   massless propagators, Euclidean absolute convergence), Lowenstein 1976 (BPHZL convergence theorems), and Breitenlohner–Maison 1977 I, II
   (existence to all orders of *dimensionally renormalised* Green functions of massless theories without super-renormalisable couplings, resp.
   with all interactions of IR degree $\Omega\ge4$).
   *Application:* $\Pi^{\mu\nu}$ is, up to $e^2$, the photon self-energy of massless QCD$\times$QED at lowest order in $e$ and all orders in $g$.
   It is therefore a Green function of **elementary** fields of a renormalisable massless theory with only dimension-4 couplings. A two-point
   function at $q\neq0$ is automatically non-exceptional. **[To verify:]** that the hypotheses of BM II are spelled out for non-abelian
   gauge fields with Faddeev–Popov ghosts in covariant gauges. The power counting is the same: every QCD vertex has dimension 4, and the
   gluon propagator, including the $(1-\xi)k_\mu k_\nu/k^4$ part, has IR degree $-2$. The correlator of gauge-invariant currents is
   gauge independent.
2. **Structure of massless propagator-type integrals.** By dimensional analysis every bare $(n{+}1)$-loop contribution equals
   $c_n(\varepsilon)\,(\mu_0^2)^{n\varepsilon}(-q^2-i0)^{-(n+1)\varepsilon}$, with $c_n$ meromorphic in $\varepsilon$ (e.g. (2.3), (4.1)).
   $\overline{\rm MS}$ counterterms are polynomials in $1/\varepsilon$ ('t Hooft 1973; 't Hooft–Veltman 1972 for gauge invariance of DR). Hence
   the Laurent coefficients of $\Pi_{\overline{\rm MS}}(q^2;\varepsilon)$ at fixed order are **polynomials in $L=\ln(-q^2/\mu^2)$**.
3. **Unitarity (cutting rules) in $D$ dimensions.** For each diagram, the sum of its cuts separating the two current vertices equals its
   discontinuity: Cutkosky 1960, Veltman 1963 (largest-time equation), 't Hooft–Veltman *Diagrammar* 1973. In covariant gauges the
   ghost and unphysical-polarisation cuts cancel ('t Hooft–Veltman 1972 *Combinatorics*; BRST, Kugo–Ojima 1979). The sum over cuts
   therefore equals the sum over physical final states. The identity holds for dimensionally regularised integrals as an identity between
   meromorphic functions of $\varepsilon$. It is checked explicitly and exactly in $\varepsilon$ at $O(g^2)$ (§4.4).
   The additive counterterm of $\Pi$ is real and $q$-independent, so it has no discontinuity. Coupling counterterms correspond to
   counterterm-vertex insertions in the cut diagrams.

**Proof.**
(a) By 1, for $q^2<0$ the renormalised $\Pi^{(n)}_{\overline{\rm MS}}(q^2;\varepsilon)$ has a finite limit as $\varepsilon\to0$, for every real $L$.
(b) By 2, each Laurent coefficient $p_{n,k}(L)$ ($k<0$) is a polynomial in $L$. A polynomial vanishing for all real $L$ vanishes identically, so
$p_{n,k}(L)\equiv0$ also at complex $L$, in particular at $L=\ell-i\pi$. Hence $\Pi^{(n)}_{\overline{\rm MS}}(s+i0;\varepsilon)$, defined by continuation of
the bare expressions $(-q^2-i0)^{-(n+1)\varepsilon}$ at fixed $\varepsilon$, has a finite limit. The limit is the polynomial in $L$ evaluated at $L=\ell-i\pi$
(this is where the limit $\varepsilon\to0$ and the continuation commute). Its imaginary part is a polynomial in $\ell$ with real coefficients.
(c) By 3, $\rho^{(n)}(s;\varepsilon)=2(D-1)s\,{\rm Im}\,\Pi^{(n)}_{\overline{\rm MS}}(s+i0;\varepsilon)$ at each $\varepsilon$, so $R^{(n)}(s;\varepsilon)$ has the finite limit
$12\pi\,{\rm Im}\,\Pi^{(n)}_{\overline{\rm MS}}(s+i0)$. The degree statement (ii) follows from the RG (§6, G4). $\square$

**Status tags for the monograph.** Steps (a)–(b) are **[R]**, given the cited theorems (rigorous perturbative results; Poggio–Quinn as the
physics-level general proof); the BM hypothesis check for gauge theories is **[to verify]**. The identification of $12\pi\,{\rm Im}\,\Pi$ with the sum
over partonic cuts in DR is **[A]**: cutting rules plus BRST unitarity are standard, but I know of no single source that writes the $D$-dimensional,
massless, IR-regulated version in complete rigour. If $R$ is *defined* as $12\pi\,{\rm Im}\,\Pi$, which is the physical cross section by unitarity of the
full theory, then the IR finiteness of its perturbative expansion is [R].
*Independent all-order arguments in Minkowski space:* Sterman 1976 (Kinoshita's theorem in Yang–Mills theories, sketch); Sterman 1978a,b (origin
and cancellation of mass divergences in cut vacuum-polarisation diagrams).
*Regulator independence:* with massive quarks as IR regulator, the Euclidean correlator has a smooth $m\to0$ limit at fixed $Q^2$, because there
are no mass singularities at non-exceptional Euclidean points (cf. Kinoshita 1962; Kinoshita–Ukawa 1976). The massless $R$ is therefore also the
$m\to0$ limit of the massive one. **[A]**; I did not re-derive this.
*Minkowski boundary values:* Lowenstein–Speer 1976 show that the $i0\to0$ limits of renormalised Feynman integrals exist as Lorentz-invariant tempered
distributions, also with zero masses. So ${\rm Im}\,\Pi$ is well defined order by order as a distribution; for the massless two-point function the explicit form makes it an
ordinary function for $s>0$. (For the early IR analysis of massless $\phi^4$ see Symanzik 1973.)
*Beyond PT:* $R(s)$ itself has resonances. Comparison with data needs smearing (Poggio–Quinn–Weinberg 1976) or Euclidean quantities such as the
Adler function, plus the OPE (SVZ 1979), where for massless quarks the leading power correction is $\langle\frac{\alpha_s}{\pi}G^2\rangle/Q^4$ (dimension 4; quark condensates enter multiplied by $m_q$).
The non-perturbative validity of the OPE and of local duality is **[C]**.

---------------------------------------------------------------------------------------------------

## 6. RG and analyticity to higher orders (`rg_structure.py`)

With $a=\alpha_s/\pi$, $\mu^2da/d\mu^2=-b_0a^2-b_1a^3-\dots$, $b_0=\beta_0/4$, $b_1=\beta_1/16$ (`CONTEXT.md` normalisation of $\beta_0$), and
$D=R_0\,d(a(Q^2))$, $d=1+d_1a+d_2a^2+\dots$:
* $\Pi_{\overline{\rm MS}}=\Pi(0)-\frac{R_0}{12\pi^2}\int_0^L D\,dL'$ is, at order $a^n$, a polynomial in $L$ of degree $\max(1,n)$ (G1).
* Two independent routes give the same $R$ (G2): substituting $L\to\ell-i\pi$, and the contour formula
  $$R(s)=\frac{1}{2\pi}\int_{-\pi}^{\pi}d\theta\,D(s\,e^{i\theta}),$$
  derived from $\Pi(se^{-i\pi})-\Pi(se^{i\pi})$ and $d\Pi/d\ln Q^2=-D/12\pi^2$.
* In terms of $a(s)$ (G3), with $r_n$ defined by $R=R_0\sum r_na^n$:
  $$r_1=d_1,\quad r_2=d_2,\quad r_3=d_3-\frac{\pi^2}{3}b_0^2d_1,\quad r_4=d_4-\pi^2\Big(b_0^2d_2+\frac56b_0b_1d_1\Big).$$
  For SU(3), $\frac{\pi^2}{3}b_0^2=16.66,\ 14.28,\ 12.09$ for $n_f=3,4,5$. This "$\pi^2$-term" dominates the known $r_3$.
  The structure is discussed in Krasnikov–Pivovarov 1982, Radyushkin 1982 (republished 1996) and Kataev–Starshenko 1995;
  I did not check whether their normalisations match mine.
* Expressed in $a(\mu)$, the coefficient of $a^n$ in $R$ is a polynomial of degree $\le n-1$ in $\ln(s/\mu^2)$ (G4), as claimed in Theorem 5.1(ii).

Literature values for orientation (normalisation $R=R_0[1+a+r_2a^2+\dots]$, SU(3); quoted **[from memory; to verify against the originals]**):
$r_2=1.9857-0.1153\,n_f$ (Chetyrkin–Kataev–Tkachov 1979; Dine–Sapirstein 1979; Celmaster–Gonsalves 1980). For a general gauge group,
$R=R_0\big[1+\frac34C_Fa+a^2\big(-\frac{3}{32}C_F^2+C_FC_A(\frac{123}{32}-\frac{11}{4}\zeta_3)+C_FT_Fn_f(-\frac{11}{8}+\zeta_3)\big)+\dots\big]$,
which reproduces the SU(3) numbers; I checked this arithmetic, but the two recalled forms are not an independent source. At $a^3$: $-6.63694-1.20013n_f-0.00518n_f^2-1.2395\,\eta$, with $\eta=(\sum e_q)^2/(3\sum e_q^2)$ and the
singlet coefficient $\frac{55}{72}-\frac53\zeta_3=-1.2395$ (Gorishny–Kataev–Larin 1991; Surguladze–Samuel 1991; the earlier GKL 1988 value was later
corrected, **[recalled; verify]**). The singlet ("light-by-light") term starts at $a^3$ because two-gluon intermediate states between the two quark loops are forbidden by
$C$ invariance (Furry's theorem, with colour factor $\delta^{ab}$); three gluons give $d^{abc}d^{abc}$. This links to the Furry monograph.

---------------------------------------------------------------------------------------------------

## 7. KLN at $O(\alpha_s)$: exclusive versus inclusive (`ee_nlo.py`, part E)

* **Exclusive pieces diverge** (E1). With $N_\varepsilon\equiv\frac{\alpha_sC_F}{2\pi}(\frac{4\pi\mu_0^2}{s})^\varepsilon c_\Gamma$:
  $\sigma(q\bar q)^{(1)}/\sigma_0=N_\varepsilon[-\frac2{\varepsilon^2}-\frac3\varepsilon-8+\pi^2]$ and $\sigma(q\bar qg)/\sigma_0=N_\varepsilon[\frac2{\varepsilon^2}+\frac3\varepsilon+\frac{19}2-\pi^2]$. The sum is finite, (3.7).
  For $e^+e^-$, KLN (Kinoshita 1962; Lee–Nauenberg 1964) needs only the sum over **final-state** degeneracies, since the initial state is
  colourless. The known failures of non-abelian Bloch–Nordsieck (Doria–Frenkel–Taylor 1980; Di'Lieto et al. 1981) involve coloured initial
  states and are irrelevant here. On the need for initial-state/forward-scattering sums in general, see Frye et al. 2019.
* **A non-IR-safe "inclusive" quantity: the quark energy spectrum** (E2–E4). At fixed $x=x_q<1$ the $q\parallel g$ region is integrated
  over, and
  $$\frac{1}{\sigma_0}\frac{d\sigma}{dx}\Big|_{\rm pole}=-\frac{1}{\varepsilon}\frac{\alpha_s}{2\pi}P_{qq}(x),\qquad P_{qq}=C_F\Big[\frac{1+x^2}{1-x}\Big]_+ .$$
  This is verified for $x<1$ pointwise and, including $\delta(1-x)$, through the Mellin moments $n=0..3$: the $1/\varepsilon^2$ poles cancel, and
  the $1/\varepsilon$ coefficient equals $-\int_0^1x^nC_F[(1+x^2)/(1-x)]_+$, i.e. $0,\ \frac43,\ \frac{25}{12},\ \frac{157}{60}$ (times $C_F$; units of $\frac{\alpha_s}{2\pi}$).
  $n=0$ is the total rate: finite by quark-number conservation. For $n\ge1$ the leftover collinear pole is absorbed into $\overline{\rm MS}$ fragmentation
  functions (Ch. 9; cf. Altarelli–Ellis–Martinelli–Pi 1979).
* **IR safety.** An observable built from measurement functions $S_n$ that are insensitive to soft emission and collinear splitting is finite
  order by order (Sterman–Weinberg 1977; Sterman 1978a,b, 1979). The Sterman–Weinberg cross section is the classic example (§8).

---------------------------------------------------------------------------------------------------

## 8. Sterman–Weinberg cone cross section at $O(\alpha_s)$ (`sw_jets.py`)

**Definition.** An event is 2-jet if *some* pair of back-to-back cones of half-angle $\delta$ contains all the energy except at most $\epsilon\sqrt s$.
Here $\epsilon$ is a fraction of the **total** c.m. energy and the axis is free.
**Region at $O(\alpha_s)$** (exact geometry). Since $-\vec p_k=\vec p_i+\vec p_j$ lies on the arc between $\hat n_i$ and $\hat n_j$, the smallest cone
containing $\hat n_i,\hat n_j,-\hat n_k$ has half-angle $\theta_{ij}/2$. Hence: 2-jet $\iff$ (a) some $\theta_{ij}\le2\delta$, **or** (b) some $x_k<2\epsilon$ and
$\pi-\theta_{ij}\le2\delta$ for the other two. Two outside partons are impossible, since they would carry at least $\sqrt s/2$.
Then $\sigma_{2j}=\sigma_{\rm tot}-\sigma_{3j}$. This is legitimate in DR because the 3-jet region avoids all singular configurations, so its
integral converges at $D=4$.

**Analytic asymptotics** ($\epsilon<\delta\ll1$, $d=\sin^2\delta$). Use $y_{13}=x_3v$, $y_{23}=x_3(1-v)$, Jacobian $x_3$, and the exact identity
$M\,dx_1dx_2=[N_0/(v(1-v))-2x_3^2]\,dx_3dv/x_3$ with $N_0=1+(1-x_3)^2$. The collinear conditions are $a<v<1-a$, $a=d(1-x_3)/(1-x_3d)$.
For $\epsilon<\delta$ the soft condition removes exactly $x_3<2\epsilon$, because the $q\bar q$ acollinearity is $\le x_3(1+O(x_3))<2\delta$. The soft-quark and $q\parallel\bar q$ regions
give $O(\epsilon\ln d)$ and $O(d)$. Then
$$I_{3j}=\int_{2\epsilon}^1\frac{dx_3}{x_3}\Big[2N_0\ln\frac{1-a}{a}-2x_3^2(1-2a)\Big]=4\ln d\ln2\epsilon+3\ln d+\frac{2\pi^2}{3}-\frac72+O(\epsilon\ln d,\,d\ln\epsilon),$$
using $\int_0^1(2-2x+x^2)\frac{\ln(1-x)}{x}dx=-\frac{\pi^2}{3}+\frac54$. Hence $\sigma_{3j}=\sigma_0\frac{C_F\alpha_s}{\pi}[4\ln\delta\ln2\epsilon+3\ln\delta+\frac{\pi^2}{3}-\frac74]$ and
$$\boxed{\sigma_{2j}=\sigma_0\Big\{1-\frac{C_F\alpha_s}{\pi}\Big[4\ln\delta\,\ln2\epsilon+3\ln\delta+\frac{\pi^2}{3}-\frac52\Big]\Big\},\qquad C_F=\frac43.}$$
**Numerical check** (exact regions, closed-form $v$-integrals, mpmath quadrature in $x_3$): the residual falls from $2.5\times10^{-2}$ at
$(\epsilon,\delta)=(10^{-2},0.1)$ to $4\times10^{-4}$ at $(10^{-6},0.003)$, consistent with $O(\epsilon\ln d,\,d\ln\epsilon)$ power corrections (S1, S2). At
$(10^{-6},0.003)$: $c_{2j}=-288.2811$ numerically, $-288.2812$ from the formula with $\ln2\epsilon$, $-304.39$ with $\ln\epsilon$ (S3, S4).
**Verdict on the classic formula.** The bracket $4\ln\delta\ln(\cdot)+3\ln\delta+\pi^2/3-5/2$ with prefactor $\frac43\frac{\alpha_s}{\pi}$ is **correct**. The argument of the
log must be **$2\epsilon$** if $\epsilon$ is the fraction of the total energy $\sqrt s$, as in the SW definition. The form "$4\ln\delta\ln\epsilon$" quoted in the task is
correct iff $\epsilon$ denotes the fraction of the **beam** energy $\sqrt s/2$ (S5); with $\epsilon$ the fraction of $\sqrt s$ it is wrong by
$4\ln2\,|\ln\delta|\cdot\frac43\frac{\alpha_s}{\pi}$. Validity requires $\epsilon\lesssim\delta\ll1$. For $\epsilon\gg\delta$, recoil (acollinearity) generates additional
$\ln(\epsilon/\delta)$ terms (S6: $102.70$ versus $68.89$ at $\epsilon=0.05$, $\delta=0.005$). SW's own typography could not be checked (only metadata/abstract
accessible): **[unverified]**. The bracket matches the commonly quoted form with $\ln2\epsilon$.

---------------------------------------------------------------------------------------------------

## 9. Cross-checks against the literature (conventions converted)

| quantity | ours | literature | conversion | result |
|---|---|---|---|---|
| $\sigma_0$, $R_0$ | (2.1) | textbook (ESW Ch. 3; Peskin–Schroeder) | none | PASS |
| $R^{(1)}$ | $R_0\frac{3C_F}{4}\frac{\alpha_s}{\pi}$ | Appelquist–Georgi 1973; Zee 1973: $1+\alpha_s/\pi$ | $C_F=4/3$ | PASS |
| one-loop $F$ ($\overline{\rm MS}$) | $-2/\varepsilon^2-3/\varepsilon-8+\zeta_2$; $O(\varepsilon)$: $-16+\frac32\zeta_2+\frac{14}3\zeta_3$ | Gonsalves 1983; MVV 2005 | $e^{\varepsilon\gamma_E}c_\Gamma$ vs $c_\Gamma$ | PASS (recalled values) |
| real/virtual brackets | (3.6), (3.1)$\times\cos\pi\varepsilon$ | ESW Ch. 3 | prefactor $c_\Gamma$ | PASS, prefactor [unverified] |
| $\Pi^{(1)}_{\overline{\rm MS}}$ constant | $55/12-4\zeta_3$ per unit $(-L)$ | CKT 1979; CKK 1996 review | $\Pi$ sign, $3/(16\pi^2)$ vs $N_c/(12\pi^2)$ normalisations | PASS (recalled) |
| $\hat I(1,1,1,1,1)$ | $6\zeta_3/Q^2$ | Chetyrkin–Tkachov 1981 | none | PASS |
| QED limit | $1+\frac34\frac\alpha\pi$ | two-loop QED $\beta$ | $C_F\to1$ | PASS |
| $r_3-d_3$ | $-\frac{\pi^2}{3}b_0^2$ | Kataev–Starshenko 1995 etc. | $b_0=\beta_0/4$ | PASS (symbolic) |
| SW formula | §8 | SW 1977 | $\epsilon$ (total) $=\epsilon'$ (beam)$/2$ | PASS with $\ln2\epsilon$ |

---------------------------------------------------------------------------------------------------

## 10. Discrepancies / corrections to report

1. **SW formula in the task.** "$4\ln\delta\ln\epsilon$" holds only if $\epsilon$ is the fraction of the beam energy. With the SW definition ($\epsilon$ a fraction of the total
   energy) it must read $4\ln\delta\ln2\epsilon$. The rest of the bracket ($3\ln\delta+\pi^2/3-5/2$) and the prefactor $\frac43\frac{\alpha_s}{\pi}$ are correct. The formula
   assumes a free cone axis and $\epsilon\lesssim\delta\ll1$.
2. **Outline Ch. 4.** Suggested tags: the all-order IR finiteness of $R$ is [R] as a statement about $12\pi\,{\rm Im}\,\Pi$ (Euclidean finiteness + polynomial structure
   + continuation), and [A] for its identification with the DR sum over partonic cuts (cutting rules + BRST in $D$ dimensions). Two additions are worth making:
   the exact-in-$\varepsilon$ cutting identity (4.6), a strong pedagogical check; and the remark that the $\pi^2$ terms of $R$ come from the continuation (§6).
3. **Sign conventions for $\Pi$.** Ours (1.1) has ${\rm Im}\,\Pi>0$ and $\Pi_{\rm PS}=-e^2\Pi$. When quoting literature constants (e.g. $55/12-4\zeta_3$), state the normalisation
   explicitly: some references use $3/(16\pi^2)$ with $\frac{20}{9}-\frac43L$, which equals our $\frac{N_c}{12\pi^2}(\frac53-L)$ for $N_c=3$.
4. No conflicts with `CONTEXT.md` conventions were found ($\overline{\rm MS}$ factor, $\beta_0$, vertex $ig\gamma^\mu t^a$ all used as stated).

---------------------------------------------------------------------------------------------------

## 11. Files

* `diracD.py`: $D$-dimensional Dirac traces (anticommuting $\gamma$'s); self-test includes a numerical 4×4 comparison with interleaved contractions.
* `ee_nlo.py` (27 checks): LO, phase spaces, exact LO cutting identity, exact one-loop form factor, real emission, pole cancellation, KLN/quark spectrum.
* `pi_twoloop.py` (18 checks): IBP and tensor evaluator for two-loop propagator integrals; two-loop correlator; Ward identity; $\overline{\rm MS}$; RG; Adler; exact cutting identity.
* `cut_identity_analytic.py` (1 check): termwise analytic proof of (4.6).
* `rg_structure.py` (5 checks): RG polynomial structure, contour formula, $\pi^2$ terms through $a^4$.
* `sw_jets.py` (6 checks): Sterman–Weinberg exact numerics versus asymptotics.
* `verify_refs.py`, `refs_verification_log.txt`: INSPIRE/Crossref verification of all references below that are not in `research/refs/refs.bib`.
* `ee_total.tex`: Chinese LaTeX section for Ch. 4 (8 subsections, 4 TikZ figures, 1 table, rigor tags); compiles cleanly with
  the monograph preamble (XeLaTeX: 0 errors, 0 overfull boxes, no undefined references).
* `ee_bibitems.tex`: the 33 new verified `\bibitem`s cited by `ee_total.tex` (bare entries, to append to `research/refs/refs_bibitems.tex`;
  key scheme of `refs/NOTES.md`; `BreitenlohnerMaison1977a/b/c` = CMP 52 pp. 11/39/55; `tHooftVeltman1972b` = *Combinatorics*).
  All other citation keys used in `ee_total.tex` already exist in `refs_bibitems.tex`.
* `test_build.tex` (driver), `test_bib.tex` (generated: `refs_bibitems.tex` + `ee_bibitems.tex`), `preamble_fact.tex` (copy of
  `common/`), `test_build.pdf` (22 pp.; the section is pp. 1–8).
* `*.log`: outputs of the last runs (`diracD.log`, `ee_nlo.log`, `pi_twoloop.log`, `cut_identity_analytic.log`, `rg_structure.log`, `sw_jets.log`).

---------------------------------------------------------------------------------------------------

## 12. References (all verified on INSPIRE + Crossref; see `refs_verification_log.txt`; keys not in `refs.bib` marked *)

* Appelquist, Georgi, PRD 8 (1973) 4000–4002 · Zee, PRD 8 (1973) 4038–4041 · Ellis–Stirling–Webber, *QCD and Collider Physics* (CUP 1996).
* \*Chetyrkin, Kataev, Tkachov, PLB 85 (1979) 277–279 · \*Dine, Sapirstein, PRL 43 (1979) 668–671 · \*Celmaster, Gonsalves, PRL 44 (1980) 560–564; PRD 21 (1980) 3112–3128.
* \*Gorishny, Kataev, Larin, PLB 212 (1988) 238–244; PLB 259 (1991) 144–150 · \*Surguladze, Samuel, PRL 66 (1991) 560–563 [Erratum ibid. 2416] · \*Baikov, Chetyrkin, Kühn, PRL 101 (2008) 012002.
* \*Adler, PRD 10 (1974) 3714–3728 · \*Chetyrkin, Kühn, Kwiatkowski, Phys. Rept. 277 (1996) 189–281 · \*Kataev, Starshenko, MPLA 10 (1995) 235–250 · \*Krasnikov, Pivovarov, PLB 116 (1982) 168–170 · \*Radyushkin, JINR E2-82-159 (1982), JINR Rapid Commun. 78 (1996) 96–99.
* \*Chetyrkin, Tkachov, NPB 192 (1981) 159–204 · \*Tkachov, PLB 100 (1981) 65–68 · \*'t Hooft, NPB 61 (1973) 455–468 · 't Hooft, Veltman, NPB 44 (1972) 189 · \*'t Hooft, Veltman, NPB 50 (1972) 318–353 · \*'t Hooft, Veltman, *Diagrammar*, CERN-73-09 (NATO Sci. Ser. B 4 (1974) 177–322).
* Cutkosky, J. Math. Phys. 1 (1960) 429–433 · Veltman, Physica 29 (1963) 186–207 · \*Kugo, Ojima, Prog. Theor. Phys. Suppl. 66 (1979) 1–130.
* Poggio, Quinn, PRD 14 (1976) 578–582 · Lowenstein, Zimmermann, CMP 44 (1975) 73–86 · Lowenstein, CMP 47 (1976) 53–68 · \*Lowenstein, Speer, CMP 47 (1976) 43–51 · Breitenlohner, Maison, CMP 52 (1977) 11–38 (\*), 39–54, 55–75 · \*Symanzik, CMP 34 (1973) 7–36 · \*Kinoshita, Ukawa, PRD 13 (1976) 1573–1591.
* Kinoshita, J. Math. Phys. 3 (1962) 650–677 · Lee, Nauenberg, PR 133 (1964) B1549–B1562 · Sterman, PRD 14 (1976) 2123–2125 · Sterman, PRD 17 (1978) 2773–2788, 2789–2799 · \*Sterman, PRD 19 (1979) 3135–3138 · Doria, Frenkel, Taylor, NPB 168 (1980) 93–110 · Di'Lieto et al., NPB 183 (1981) 223–250 · Frye et al., PRD 99 (2019) 056015.
* Sterman, Weinberg, PRL 39 (1977) 1436–1439 · \*Kramer, Lampe, Z. Phys. C 34 (1987) 497–522 [Erratum 42 (1989) 504] · \*Ellis, Ross, Terrano, NPB 178 (1981) 421–456.
* \*Gonsalves, PRD 28 (1983) 1542–1549 · \*Moch, Vermaseren, Vogt, JHEP 08 (2005) 049 · \*Altarelli, Ellis, Martinelli, Pi, NPB 160 (1979) 301–329.
* Poggio, Quinn, Weinberg, PRD 13 (1976) 1958–1968 · Shifman, Vainshtein, Zakharov, NPB 147 (1979) 385–447.
