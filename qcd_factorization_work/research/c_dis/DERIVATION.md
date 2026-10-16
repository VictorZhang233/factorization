# DIS at $O(\alpha_s)$ in dimensional regularisation: partonic $F_2$, $F_L$ and the $\overline{\rm MS}$ coefficient functions

Directory: `"/Users/hao-cheng/Desktop/theorem proof/qcd_factorization_work/research/c_dis"`
(all scripts run with `python3 -I <script>.py`; see §14).

Everything below was derived from scratch and checked by computer algebra (sympy, exact in $\varepsilon$
wherever stated) and by independent numerical cross-checks (numpy / mpmath).  Every check listed
in §12 passes.  Items that could **not** be verified against the original literature are marked
**[unverified]**.

---------------------------------------------------------------------------------------------------

## 0. Results at a glance

Normalisation (binding conventions of `CONTEXT.md`; $a\equiv\alpha_s(\mu)/2\pi$, $\mu_F=\mu_R=\mu$):

$$
\frac{F_2(x,Q^2)}{x}=\sum_q e_q^2\Big\{q(x,\mu)+\bar q(x,\mu)
+\frac{\alpha_s(\mu)}{2\pi}\Big[C_2^q\otimes(q+\bar q)+2\,C_2^g\otimes g\Big](x)\Big\}+O(\alpha_s^2),
$$
$$
\frac{F_L(x,Q^2)}{x}=\sum_q e_q^2\,\frac{\alpha_s(\mu)}{2\pi}\Big[C_L^q\otimes(q+\bar q)+2\,C_L^g\otimes g\Big](x)+O(\alpha_s^2),
\qquad (C\otimes f)(x)=\int_x^1\frac{d\xi}{\xi}\,C\!\left(\frac{x}{\xi}\right)f(\xi).
$$
The factor 2 in front of the gluon terms counts the quark **and** the antiquark of flavour $q$
(both are produced in $\gamma^*g\to q\bar q$); $C_{2,L}^g$ is "per flavour and per (anti)quark".
At $\mu=Q$:

$$
\boxed{\;
\begin{aligned}
C_2^q(z)&=C_F\Big[2\Big(\frac{\ln(1-z)}{1-z}\Big)_+-\frac32\Big(\frac{1}{1-z}\Big)_+-(1+z)\ln(1-z)
-\frac{1+z^2}{1-z}\ln z+3+2z-\Big(\frac92+\frac{\pi^2}{3}\Big)\delta(1-z)\Big]\\
&=C_F\Big[\frac{1+z^2}{1-z}\Big(\ln\frac{1-z}{z}-\frac34\Big)+\frac{9+5z}{4}\Big]_+ ,\\
C_2^g(z)&=T_F\Big[\big(z^2+(1-z)^2\big)\ln\frac{1-z}{z}-8z^2+8z-1\Big],\\
C_L^q(z)&=C_F\,2z,\qquad\qquad C_L^g(z)=T_F\,4z(1-z).
\end{aligned}\;}
$$

(In the second form of $C_2^q$ the plus prescription acts on the whole bracket; the two forms are
identical distributions, checked in `moments.py`/§8.)  For general $\mu$:
$C_2^i(z,Q^2/\mu^2)=C_2^i(z)+\ln(Q^2/\mu^2)\,P_{qi}(z)$, $i=q,g$, with
$P_{qq}=C_F\big[\frac{1+z^2}{1-z}\big]_+=C_F\big\{2\big(\frac1{1-z}\big)_+-1-z+\frac32\delta(1-z)\big\}$,
$P_{qg}=T_F[z^2+(1-z)^2]$; $C_L^{q,g}$ have no $\mu$ dependence at this order.

All four agree **exactly** (including every overall factor) with the expected forms in the task.

---------------------------------------------------------------------------------------------------

## 1. Conventions and normalisation

### 1.1 Hadronic tensor, structure functions, factorisation formula

$J^\mu=\sum_q e_q\bar\psi_q\gamma^\mu\psi_q$ (in units of $e$),
$$
W^{\mu\nu}=\frac{1}{4\pi}\int d^4z\,e^{iq\cdot z}\langle P|[J^\mu(z),J^\nu(0)]|P\rangle
=\frac{1}{4\pi}\sum_X(2\pi)^4\delta^4(P+q-p_X)\langle P|J^\mu(0)|X\rangle\langle X|J^\nu(0)|P\rangle
\quad(q^0>0),
$$
spin averaged, $\langle P'|P\rangle=(2\pi)^3 2E\,\delta^3(\vec P'-\vec P)$.
Decomposition (CONTEXT): $W^{\mu\nu}=(-g^{\mu\nu}+q^\mu q^\nu/q^2)F_1+\tilde P^\mu\tilde P^\nu F_2/(P\cdot q)$,
$\tilde P=P-(P\cdot q/q^2)q$, $F_L=F_2-2xF_1$, $Q^2=-q^2$, $x=Q^2/(2P\cdot q)$.
**The factor $1/4\pi$ is not stated in `CONTEXT.md`; it is the normalisation that reproduces the
binding parton-model formula $F_2=\sum e_q^2x(q+\bar q)$ (verified in §3).**

Factorisation at leading power: $W^{\mu\nu}(P,q)=\sum_j\int_x^1\frac{d\xi}{\xi}f_j(\xi,\mu)\,\hat W_j^{\mu\nu}(\xi P,q;\mu)$.
Writing the partonic tensor with the same decomposition, $\hat W_j^{\mu\nu}=(-g+qq/q^2)\hat F_{1,j}(z)
+\tilde p^\mu\tilde p^\nu\hat F_{2,j}(z)/(p\cdot q)$, $z=Q^2/(2p\cdot q)=x/\xi$, and using
$\tilde p\tilde p/(p\cdot q)=\xi\,\tilde P\tilde P/(P\cdot q)$ for $p=\xi P$:
$$
F_1(x)=\sum_j\int_x^1\frac{d\xi}{\xi}f_j(\xi)\hat F_{1,j}(x/\xi),\qquad
\frac{F_{2,L}(x)}{x}=\sum_j\int_x^1\frac{d\xi}{\xi}f_j(\xi)\,\Big[\frac{\hat F_{2,L,j}(z)}{z}\Big]_{z=x/\xi}.
$$
So the objects computed below are $\hat F_{2,L}^{\,j}(z)/z$ for on-shell massless partons $j=q,g$.

### 1.2 Dimensional regularisation, $\overline{\rm MS}$, D-dimensional averaging

* $D=4-2\varepsilon$, conventional dimensional regularisation (CDR): all momenta, polarisations and
  Dirac matrices are $D$-dimensional, $\{\gamma^\mu,\gamma^\nu\}=2g^{\mu\nu}$, $g^\mu{}_\mu=D$,
  ${\rm Tr}\,1=4$. No $\gamma_5$ occurs.
* Bare coupling $g_0^2=4\pi\alpha_s(\mu)\,\mu^{2\varepsilon}e^{\varepsilon\gamma_E}(4\pi)^{-\varepsilon}\,[1+O(\alpha_s)]$
  $=4\pi\alpha_s\mu^{2\varepsilon}/S_\varepsilon$, $S_\varepsilon=(4\pi)^\varepsilon e^{-\varepsilon\gamma_E}$ (CONTEXT).
  $\overline{\rm MS}$ = subtraction of pure poles in this normalisation. Coupling renormalisation does
  not enter at $O(\alpha_s)$.
* Averages: quark spin $1/2$, quark colour $1/N_c$; gluon polarisation $1/(D-2)=1/[2(1-\varepsilon)]$,
  gluon colour $1/(N_c^2-1)$. Colour sums: quark target $\frac1{N_c}{\rm Tr}(t^at^a)=C_F$; gluon target
  $\frac1{N_c^2-1}{\rm Tr}(t^at^a)=T_F$.
  **The $1/(D-2)$ average is part of the $\overline{\rm MS}$ convention for the gluon density** (the
  tree-level gluon density of a gluon, $f_{g/g}=\delta(1-x)$, is normalised with the same average);
  with an average $1/2$ instead, $C_2^g$ would change by $+P_{qg}$ (see §13).
* Gluon polarisation sums are replaced by $-g_{\rho\sigma}$; legitimate because the amplitudes with one
  gluon satisfy $k^\rho M_\rho=0$ (checked numerically, and the $-g$ result is compared with an explicit
  sum over the $D-2$ physical polarisations in $D=4,6,8,10$, §12).

### 1.3 Partonic kinematics

$p^2=0$, $q^2=-Q^2$, $z=Q^2/(2p\cdot q)$, $\hat s=(p+q)^2=Q^2(1-z)/z$.
Two-body final states, in the $\gamma^*$–parton c.m. frame; $\theta$ = angle between the gluon
($\gamma^*q$) or the quark ($\gamma^*g$) and $\vec p$; $y=(1-\cos\theta)/2\in[0,1]$:
* $\gamma^*(q)+q(p)\to q(p')+g(k)$: $\hat t=(p-k)^2=-Q^2y/z$, $\hat u=(q-k)^2=(p-p')^2=-Q^2(1-y)/z$,
  $\hat s+\hat t+\hat u=-Q^2$; $p\cdot k=y\,p\cdot q$.
* $\gamma^*(q)+g(p)\to q(k_1)+\bar q(k_2)$: $\hat t=(p-k_1)^2=-Q^2y/z$, $\hat u=(p-k_2)^2=(k_1-q)^2=-Q^2(1-y)/z$.

---------------------------------------------------------------------------------------------------

## 2. D-dimensional projectors

Contracting the decomposition (massless $P$):
$$
-g_{\mu\nu}W^{\mu\nu}=(D-1)F_1-\frac{F_2}{2x},\qquad
P_\mu P_\nu W^{\mu\nu}=\frac{(P\cdot q)^2}{Q^2}\Big(\frac{F_2}{2x}-F_1\Big)=\frac{Q^2}{8x^3}F_L .
$$
Hence
$$
\boxed{\frac{F_L}{x}=\frac{8x^2}{Q^2}P_\mu P_\nu W^{\mu\nu},\qquad
\frac{F_2}{x}=\frac{1}{1-\varepsilon}\Big[-g_{\mu\nu}+(3-2\varepsilon)\frac{4x^2}{Q^2}P_\mu P_\nu\Big]W^{\mu\nu}}
$$
(for partons: $P\to p$, $x\to z$).
*Massive target* (relevant for target-mass corrections in Ch. 5): with $P^2=M^2$ and
$\rho^2=1+4x^2M^2/Q^2$ the longitudinal structure function must be defined as $F_L=\rho^2F_2-2xF_1$
(the CONTEXT definition $F_L=F_2-2xF_1$ is its $M\to0$ limit); then
$F_L/x=\frac{8x^2}{Q^2\rho^2}PWP$ and $\rho^2F_2/x=[2(-gW)+(D-1)F_L/x]/(D-2)$.
Checked symbolically in $D$ and with explicit components in $D=4,5,6,7$ (`checks_setup.py`).

---------------------------------------------------------------------------------------------------

## 3. Born term

$\hat W^{\mu\nu}_{(0)}=\frac1{4\pi}\,2\pi\delta\big((p+q)^2\big)\,\frac12\,e_q^2\,{\rm Tr}[\not p\gamma^\mu(\not p+\not q)\gamma^\nu]$,
$\delta((p+q)^2)=\delta(Q^2(1-z)/z)=\delta(1-z)/Q^2$. With $\gamma^\mu\not a\gamma_\mu=-(D-2)\not a$:
$-g_{\mu\nu}{\rm Tr}[\dots]=4(D-2)\,p\cdot q$, $p_\mu p_\nu{\rm Tr}[\dots]=0$, so
$$
\frac{\hat F_2^{(0)}}{z}=e_q^2\,\delta(1-z),\qquad \hat F_L^{(0)}=0\qquad\text{(exact in }D),
$$
and $F_2/x=\sum_q e_q^2(q+\bar q)$: the normalisation of §1.1 is the parton-model one.

---------------------------------------------------------------------------------------------------

## 4. Virtual correction: the one-loop quark form factor in DR

Vertex graph (Feynman gauge), $p'=p+q$:
$$
\Lambda^\mu=-ig_0^2C_F\int\frac{d^Dl}{(2\pi)^D}
\frac{\gamma^\alpha(\not p'-\not l)\gamma^\mu(\not p-\not l)\gamma_\alpha}{(l^2+i0)\,((p-l)^2+i0)\,((p'-l)^2+i0)},
\qquad \bar u(p')\Lambda^\mu u(p)=F^{(1)}\,\bar u(p')\gamma^\mu u(p)
$$
(for massless on-shell quarks $\gamma^\mu$ is the only structure). $F^{(1)}$ is extracted with the projector
${\rm Tr}[\not p'\Lambda^\mu\not p\gamma_\mu]/{\rm Tr}[\not p'\gamma^\mu\not p\gamma_\mu]$; Feynman parameters
$l=L+x_1p+x_2p'$, $\Delta=x_1x_2Q^2$, and the standard integrals
$\int\!\frac{d^DL}{(2\pi)^D}\frac{\{L^2,1\}}{(L^2-\Delta)^3}=\frac{i}{(4\pi)^{D/2}}\{\tfrac D4\Gamma(\varepsilon)\Delta^{-\varepsilon},\,-\tfrac12\Gamma(1+\varepsilon)\Delta^{-1-\varepsilon}\}$.
Result (exact in $\varepsilon$, `dis_nlo.py` §1):
$$
\boxed{F(Q^2)=1+\frac{\alpha_s}{4\pi}C_F\Big(\frac{\mu^2}{Q^2}\Big)^{\varepsilon}
\frac{e^{\varepsilon\gamma_E}\Gamma(1+\varepsilon)\Gamma^2(1-\varepsilon)}{\Gamma(1-2\varepsilon)}
\Big[-\frac{2-\varepsilon+2\varepsilon^2}{\varepsilon^2(1-2\varepsilon)}\Big]}
$$
$$
=1+\frac{\alpha_s}{4\pi}C_F\Big(\frac{\mu^2}{Q^2}\Big)^{\varepsilon}\Big[-\frac{2}{\varepsilon^2}-\frac{3}{\varepsilon}-8+\zeta_2
+\varepsilon\Big(-16+\frac32\zeta_2+\frac{14}{3}\zeta_3\Big)+O(\varepsilon^2)\Big],
$$
with $e^{\varepsilon\gamma_E}\Gamma(1+\varepsilon)\Gamma^2(1-\varepsilon)/\Gamma(1-2\varepsilon)=1-\frac{\zeta_2}{2}\varepsilon^2+O(\varepsilon^3)$
and $-\frac{2-\varepsilon+2\varepsilon^2}{\varepsilon^2(1-2\varepsilon)}=\frac1\varepsilon-\frac{2}{\varepsilon^2(1-2\varepsilon)}$.

* UV/IR bookkeeping: the vertex graph contains the UV pole $+\frac{\alpha_s}{4\pi}C_F\frac{1}{\varepsilon_{\rm UV}}$;
  the on-shell external-leg factor $Z_2^{\rm OS}-1=\frac{\alpha_s}{4\pi}C_F(\frac1{\varepsilon_{\rm IR}}-\frac1{\varepsilon_{\rm UV}})$
  is scaleless and vanishes in DR with one $\varepsilon$; its UV part cancels the vertex UV pole
  ($Z_1=Z_2$, conserved current), so $F=1+F^{(1)}$ with **only IR poles** left. No other counterterm
  contributes at this order.
* For $Q^2>0$ (spacelike) $F$ is real. (Timelike continuation, needed for $e^+e^-$/Drell–Yan:
  $Q^2\to-q^2-i0$, $(\mu^2/Q^2)^\varepsilon\to(\mu^2/q^2)^\varepsilon e^{i\pi\varepsilon}$.)
* Contribution to DIS: $\hat F_a^{q,\rm V}/(ze_q^2)=\delta_{a2}\,2F^{(1)}\delta(1-z)$, i.e.
  $\frac{\alpha_s}{2\pi}C_F(\frac{\mu^2}{Q^2})^\varepsilon[-\frac2{\varepsilon^2}-\frac3{\varepsilon}-8+\zeta_2+O(\varepsilon)]\delta(1-z)$
  for $F_2$ and nothing for $F_L$.

---------------------------------------------------------------------------------------------------

## 5. Real emission $\gamma^*q\to qg$

### 5.1 Amplitude and D-dimensional squared matrix elements
$M^\mu=e_q\,g\,t^a\,\bar u(p')\Big[\gamma^\rho\frac{\not p+\not q}{\hat s}\gamma^\mu+\gamma^\mu\frac{\not p-\not k}{\hat t}\gamma^\rho\Big]u(p)\,\varepsilon^*_\rho(k)$
(common phase dropped). With ${\rm Tr}\,1=4$ and the polarisation sum $-g_{\rho\sigma}$:
$$
(-g_{\mu\nu})\!\sum M^\mu M^{\nu*}\Big|_{\rm Dirac}=8(1-\varepsilon)\Big[(1-\varepsilon)\Big(-\frac{\hat t}{\hat s}-\frac{\hat s}{\hat t}\Big)
+\frac{2\hat uQ^2}{\hat s\hat t}+2\varepsilon\Big],\qquad
(p_\mu p_\nu)\!\sum M^\mu M^{\nu*}\Big|_{\rm Dirac}=-4(1-\varepsilon)\,\hat u ,
$$
times $e_q^2g_0^2\,{\rm Tr}(t^at^a)$; average $\frac12\cdot\frac1{N_c}$ gives the factor $e_q^2g_0^2\,C_F/2$.
(At $\varepsilon=0$ the first is the familiar $8[-\hat t/\hat s-\hat s/\hat t+2\hat uQ^2/(\hat s\hat t)]$.)
Checked: symbolic D-dim traces (`real_me.py`), invariant forms (`laurent_pieces.py`), explicit matrices and
physical polarisations in $D=4,6,8,10$ (`check_real_me_numeric.py`).

### 5.2 D-dimensional two-body phase space
$$
\int d\Phi_2\equiv\int\frac{d^{D-1}p'}{(2\pi)^{D-1}2E'}\frac{d^{D-1}k}{(2\pi)^{D-1}2E_k}(2\pi)^D\delta^D(p+q-p'-k)
=\frac{1}{8\pi}\Big(\frac{4\pi}{\hat s}\Big)^{\varepsilon}\frac{1}{\Gamma(1-\varepsilon)}\int_0^1dy\,[y(1-y)]^{-\varepsilon}
$$
for integrands depending only on $\theta$ (the azimuthal $(D-2)$-sphere is integrated; $d\Omega_{D-1}=
\Omega_{D-2}\,2^{1-2\varepsilon}[y(1-y)]^{-\varepsilon}dy$, $\Omega_n=2\pi^{n/2}/\Gamma(n/2)$).
Total: $\Phi_2=\frac1{8\pi}(4\pi/\hat s)^\varepsilon\Gamma(1-\varepsilon)/\Gamma(2-2\varepsilon)$
(checked against the direct solid-angle evaluation, `checks_setup.py`). The $y$ integrals are Beta functions,
$\int_0^1dy\,y^{a-\varepsilon}(1-y)^{b-\varepsilon}=\Gamma(1+a-\varepsilon)\Gamma(1+b-\varepsilon)/\Gamma(2+a+b-2\varepsilon)$
(analytic continuation for $a,b=-1$).

Overall prefactor: $\frac1{4\pi}\cdot\frac12 C_F\,g_0^2\cdot\frac1{8\pi}\big(\frac{4\pi}{\hat s}\big)^\varepsilon\frac1{\Gamma(1-\varepsilon)}
=\frac{\alpha_s}{2\pi}C_F\,\frac18\Big(\frac{\mu^2}{\hat s}\Big)^{\varepsilon}\frac{e^{\varepsilon\gamma_E}}{\Gamma(1-\varepsilon)}$,
and $(\mu^2/\hat s)^\varepsilon=(\mu^2/Q^2)^\varepsilon\,z^\varepsilon(1-z)^{-\varepsilon}$.

### 5.3 Exact-in-$\varepsilon$ results (quark channel)
Writing $\hat F_a^{q,\rm R}/(ze_q^2)=\frac{\alpha_s}{2\pi}C_F\big(\frac{\mu^2}{Q^2}\big)^\varepsilon R_a^q(z,\varepsilon)$:
$$
\boxed{R_2^q=\frac{e^{\varepsilon\gamma_E}\Gamma(-\varepsilon)}{2\,\Gamma(2-2\varepsilon)}\,z^{\varepsilon}(1-z)^{-1-\varepsilon}
\big[2(1+z^2)-\varepsilon(7-2z)+\varepsilon^2\big],\qquad
R_L^q=\frac{e^{\varepsilon\gamma_E}\Gamma(2-\varepsilon)}{\Gamma(2-2\varepsilon)}\,2z\Big(\frac{z}{1-z}\Big)^{\varepsilon}}
$$
(`dis_nlo.py` §2, closed forms re-verified in `check_closed_forms.py`).
Hand check of $R_2^q$: the projected integrand is
$8\,[(1-\varepsilon)y^2-2y(z-\varepsilon(1-z))+1+z^2-\varepsilon(1-z)^2]/[y(1-z)]+16(3-2\varepsilon)z(1-y)$; with
$I_a=\int_0^1dy\,y^{a-\varepsilon}(1-y)^{-\varepsilon}$, $I_1=I_0/2$, $I_{-1}=-(1-2\varepsilon)I_0/\varepsilon$, $I_0=\Gamma^2(1-\varepsilon)/\Gamma(2-2\varepsilon)$,
one finds $(1-z)\times[\dots]/8=-(1+z^2)/\varepsilon+(7-2z)/2-\varepsilon/2$, i.e. exactly the bracket above.

### 5.4 Expansion in distributions
With $(1-z)^{-1-\varepsilon}=-\frac1\varepsilon\delta(1-z)+\sum_{k\ge0}\frac{(-\varepsilon)^k}{k!}\Big[\frac{\ln^k(1-z)}{1-z}\Big]_+$
(plus prescription of CONTEXT) and $\mathcal D_k\equiv[\ln^k(1-z)/(1-z)]_+$:
$$
R_2^q=\frac{2\delta(1-z)}{\varepsilon^2}+\frac1\varepsilon\Big[-2\mathcal D_0+1+z+\frac32\delta(1-z)\Big]
+2\mathcal D_1-\frac32\mathcal D_0-(1+z)\ln(1-z)-\frac{1+z^2}{1-z}\ln z+3+2z+\Big(\frac72-3\zeta_2\Big)\delta(1-z)+O(\varepsilon),
$$
$R_L^q=2z+O(\varepsilon)$ (finite: the $F_L$ projector kills the collinear region).

---------------------------------------------------------------------------------------------------

## 6. Photon–gluon fusion $\gamma^*g\to q\bar q$

$M^\mu=e_q\,g\,t^a\,\bar u(k_1)\Big[\gamma^\mu\frac{\not k_1-\not q}{\hat u}\gamma^\rho+\gamma^\rho\frac{\not k_1-\not p}{\hat t}\gamma^\mu\Big]v(k_2)\,\varepsilon_\rho(p)$;
$$
(-g_{\mu\nu})\!\sum M^\mu M^{\nu*}\Big|_{\rm Dirac}=8(1-\varepsilon)\Big[(1-\varepsilon)\Big(\frac{\hat u}{\hat t}+\frac{\hat t}{\hat u}\Big)-\frac{2\hat sQ^2}{\hat t\hat u}-2\varepsilon\Big],
\qquad (p_\mu p_\nu)\!\sum M^\mu M^{\nu*}\Big|_{\rm Dirac}=8\hat s ,
$$
times $e_q^2g_0^2{\rm Tr}(t^at^a)$; average $\frac1{2(1-\varepsilon)}\frac1{N_c^2-1}$ gives $e_q^2g_0^2T_F/[2(1-\varepsilon)]$.
With $\hat F_a^{g}/(ze_q^2)=\frac{\alpha_s}{2\pi}T_F\big(\frac{\mu^2}{Q^2}\big)^\varepsilon R_a^g$ (one flavour, $q$ and $\bar q$ both in the final state):
$$
\boxed{R_2^g=\frac{2e^{\varepsilon\gamma_E}\Gamma(-\varepsilon)}{\Gamma(2-2\varepsilon)}\Big(\frac{z}{1-z}\Big)^{\varepsilon}
\frac{z^2+(1-z)^2-3\varepsilon+4\varepsilon^2-2\varepsilon^3}{(1-\varepsilon)^2},\qquad
R_L^g=\frac{e^{\varepsilon\gamma_E}\Gamma(1-\varepsilon)}{\Gamma(2-2\varepsilon)}\,\frac{8z(1-z)}{1-\varepsilon}\Big(\frac{z}{1-z}\Big)^{\varepsilon}}
$$
(also re-derived by hand: with $P(z)=z^2+(1-z)^2$ and $z(1-z)=(1-P)/2$ the $y$-integral of the $F_2$ projection is
$-\frac{16}{\varepsilon}\frac{\Gamma^2(1-\varepsilon)}{\Gamma(2-2\varepsilon)}\frac{P-3\varepsilon+4\varepsilon^2-2\varepsilon^3}{1-\varepsilon}$).
Expansion:
$$
R_2^g=-\frac{2}{\varepsilon}\big[z^2+(1-z)^2\big]+2\Big\{\big[z^2+(1-z)^2\big]\ln\frac{1-z}{z}-8z^2+8z-1\Big\}+O(\varepsilon),\qquad
R_L^g=8z(1-z)+O(\varepsilon).
$$
The pole comes twice: from $y\to0$ (quark collinear to the gluon) and $y\to1$ (antiquark collinear).

---------------------------------------------------------------------------------------------------

## 7. Sum of real and virtual, collinear poles, $\overline{\rm MS}$ mass factorisation

Quark target, $F_2$ ($\mu$ arbitrary):
$$
\frac{\hat F_2^q}{ze_q^2}=\delta(1-z)+\frac{\alpha_s}{2\pi}\Big(\frac{\mu^2}{Q^2}\Big)^{\varepsilon}
\Big[-\frac{1}{\varepsilon}P_{qq}(z)+C_2^q(z)+O(\varepsilon)\Big]:
$$
* $1/\varepsilon^2$: $2\delta$ (real) $-2\delta$ (virtual) $=0$ — soft–collinear cancellation;
* $1/\varepsilon$: $-2\mathcal D_0+1+z+(\frac32-3)\delta(1-z)=-P_{qq}/C_F$ — the final-state collinear
  singularity (gluon $\parallel p'$) and the soft singularity cancel between real and virtual (KLN for the
  inclusive final state); what remains is the **initial-state collinear** pole, with exactly the LO DGLAP kernel,
  including its $\frac32\delta(1-z)$ end-point term which comes from the virtual graph;
* $\varepsilon^0$: the $\delta$ coefficient $\frac72-3\zeta_2-8+\zeta_2=-\frac92-2\zeta_2=-(\frac92+\frac{\pi^2}{3})$.

Gluon target: $\hat F_2^g/(ze_q^2)=\frac{\alpha_s}{2\pi}(\frac{\mu^2}{Q^2})^\varepsilon[-\frac2\varepsilon P_{qg}+2C_2^g+O(\varepsilon)]$.
$F_L$: finite for both targets.

**Partonic PDFs and mass factorisation.** In pure DR the bare PDFs of on-shell massless partons are
$f^{\rm bare}_{i/j}=\delta_{ij}\delta(1-z)$ to all orders (every loop correction is scaleless,
$\propto 1/\varepsilon_{\rm UV}-1/\varepsilon_{\rm IR}=0$). The $\overline{\rm MS}$ renormalisation of the light-cone
operators (pure UV pole, 4-dimensional kernel) then gives
$$
f_{i/j}(z,\mu)=\delta_{ij}\delta(1-z)-\frac{\alpha_s(\mu)}{2\pi}\frac{1}{\varepsilon}P_{ij}(z)+O(\alpha_s^2),
$$
where the surviving $1/\varepsilon$ is now of IR (collinear) origin; consistent with DGLAP:
$\partial f/\partial\ln\mu^2=\frac{\alpha_s}{2\pi}P\otimes f$. Applying the factorisation formula to partonic targets,
$\hat F_a^j/z=\sum_k C_a^k\otimes f_{k/j}$:
$$
\frac{\hat F_2^q}{ze_q^2}=\delta+\frac{\alpha_s}{2\pi}\Big[C_2^q-\frac{P_{qq}}{\varepsilon}\Big],\qquad
\frac{\hat F_2^g}{ze_q^2}=\underbrace{\Big(f_{q/g}+f_{\bar q/g}\Big)}_{-\frac{\alpha_s}{2\pi}\frac{2}{\varepsilon}P_{qg}}+\frac{\alpha_s}{2\pi}2C_2^g ,
$$
so the poles are removed exactly by the $\overline{\rm MS}$ PDFs and the coefficient functions are the
finite remainders. The factor $(\mu^2/Q^2)^\varepsilon$ multiplying the bare $O(\alpha_s)$ result while the
counterterm is $\mu$-independent produces $C_2^i(z,Q^2/\mu^2)=C_2^i(z)+\ln(Q^2/\mu^2)P_{qi}(z)$ (`dis_nlo.py` §5).
Remark: $e^{\varepsilon\gamma_E}$ versus $1/\Gamma(1-\varepsilon)$ differ at $O(\varepsilon^2)$ and do not matter at one loop;
the $D$-dimensional **gluon average** does matter (it multiplies a $1/\varepsilon$ pole by $O(\varepsilon)$), see §13.

---------------------------------------------------------------------------------------------------

## 8. $\overline{\rm MS}$ coefficient functions

The finite parts give exactly the boxed results of §0 (`dis_nlo.py` §4, every term compared as a distribution
with the expected form: **PASS** for $C_2^q$, $C_2^g$, $C_L^q$, $C_L^g$; overall factors $C_F$, $T_F$ and the
per-flavour factor 2 for the gluon confirmed).
Alternative "whole-bracket plus" form (often quoted):
$C_2^q=C_F[\frac{1+z^2}{1-z}(\ln\frac{1-z}{z}-\frac34)+\frac{9+5z}4]_+$: both forms agree for $z<1$ and both have
vanishing integral over $[0,1]$ (Adler sum rule, §11), hence they are the same distribution
(checked symbolically in `moments.py`: $\int_0^1 r(z)\,dz=\frac92+\frac{\pi^2}{3}$ for the regular part $r$).
For $F_1$: $2F_1=F_2/x-F_L/x$, so in the same normalisation $C_1^i\equiv C_2^i-C_L^i$, e.g.
$C_1^q=C_2^q-2C_Fz$, $C_1^g=C_2^g-4T_Fz(1-z)$.

---------------------------------------------------------------------------------------------------

## 9. Factorisation- and renormalisation-scale dependence

With $L=\ln(Q^2/\mu^2)$, $a=\alpha_s(\mu)/2\pi$:
$$
\frac{F_2}{x}=\sum_qe_q^2\Big\{(q+\bar q)(\mu)+a\big[(C_2^q+LP_{qq})\otimes(q+\bar q)+2(C_2^g+LP_{qg})\otimes g\big]\Big\}.
$$
DGLAP: $\partial(q+\bar q)/\partial\ln\mu^2=a[P_{qq}\otimes(q+\bar q)+2P_{qg}\otimes g]$, $\partial L/\partial\ln\mu^2=-1$,
$\partial a/\partial\ln\mu^2=-\frac{\beta_0}{2}a^2$. Therefore
$$
\frac{\partial}{\partial\ln\mu_F^2}\frac{F_2}{x}=a\sum_qe_q^2\big\{[P_{qq}\otimes(q+\bar q)+2P_{qg}\otimes g]-[P_{qq}\otimes(q+\bar q)+2P_{qg}\otimes g]\big\}+O(a^2)=O(a^2),
$$
and $\partial F_2/\partial\ln\mu_R^2=-\frac{\beta_0}{2}a^2\sum e_q^2[C_2^q\otimes(q+\bar q)+2C_2^g\otimes g]=O(a^2)$;
$F_L$ is $\mu$-independent at $O(a)$. Verified symbolically in Mellin space with generic moments
(`scale_scheme.py` A; the $O(a^2)$ remainder is printed there). Numerical illustration (`scale_scheme.py` B):
exact LO singlet evolution (2×2, $n_f=4$) + one-loop running, $F_{2,N}(\mu=Q/2)-F_{2,N}(\mu=2Q)$ divided by
$\alpha_s^2$ tends to a constant as $\alpha_s(Q)=0.2\to0.025$ ($N=2$: $-0.0310,-0.0240,-0.0208,-0.0192$;
$N=4$: $0.044,0.066,0.075,0.080$), i.e. the residual scale dependence is $O(\alpha_s^2)$. The same run checks
momentum conservation of the LO kernels at $N=2$.

---------------------------------------------------------------------------------------------------

## 10. DIS scheme

Definition (quarks: $F_2$ is "all quark" to all orders; gluon fixed by the momentum sum rule — the choice usually
attributed to Diemoz, Ferroni, Longo, Martinelli, Z. Phys. C39 (1988) 21 **[attribution recalled, not re-checked]**;
the DIS scheme for quark densities goes back to Altarelli, Ellis, Martinelli, Nucl. Phys. B157 (1979) 461
**[recalled]**):
$$
q_i^{\rm DIS}=q_i+a\big[C_2^q\otimes q_i+C_2^g\otimes g\big],\quad \bar q_i^{\rm DIS}=\bar q_i+a\big[C_2^q\otimes\bar q_i+C_2^g\otimes g\big],\quad
g^{\rm DIS}=g-a\big[C_2^q\otimes\Sigma+2n_fC_2^g\otimes g\big],
$$
$\Sigma=\sum_i(q_i+\bar q_i)$, all at the same $\mu$, with the $\mu$-independent $C_2^i(z)$ (i.e. the
$\overline{\rm MS}$ coefficients at $Q=\mu$; the PDFs must not depend on $Q$). Then
$F_2(x,Q^2)/x=\sum e_q^2\{(q+\bar q)^{\rm DIS}(\mu)+a\ln(Q^2/\mu^2)[P_{qq}\otimes(q+\bar q)+2P_{qg}\otimes g]\}+O(a^2)$,
i.e. $C_2^{q,\rm DIS}(z,Q^2/\mu^2)=\ln(Q^2/\mu^2)P_{qq}(z)$, $C_2^{g,\rm DIS}=\ln(Q^2/\mu^2)P_{qg}(z)$, both vanishing at $\mu=Q$.
Consequences (checked in `scale_scheme.py` C):
* $F_2/x=\sum e_q^2(q+\bar q)^{\rm DIS}+O(\alpha_s^2)$, i.e. $C_2^{q,\rm DIS}=C_2^{g,\rm DIS}=0$;
* $\int_0^1dx\,x(\Sigma^{\rm DIS}+g^{\rm DIS})=\int_0^1dx\,x(\Sigma+g)$ (exactly, for every $N$ in fact);
* $C_L^{q,g}$ unchanged at $O(\alpha_s)$ (scheme independent at their first non-vanishing order);
* LO kernels unchanged; NLO kernels: for $f'=(1+aZ)\otimes f$,
  $P'^{(1)}=P^{(1)}+Z\otimes P^{(0)}-P^{(0)}\otimes Z-\frac{\beta_0}{2}Z$ (normalisation $P=P^{(0)}+aP^{(1)}$),
  with $Z=\begin{pmatrix}C_2^q&2n_fC_2^g\\-C_2^q&-2n_fC_2^g\end{pmatrix}$ in the $(\Sigma,g)$ basis; non-singlet:
  $P^{(1),\rm DIS}_{\rm NS}=P^{(1),\overline{\rm MS}}_{\rm NS}-\frac{\beta_0}{2}C_2^q$.
* Any other hard coefficient changes accordingly: e.g. a cross section $\sigma=\sum f_i\otimes f_j\otimes\hat\sigma_{ij}$
  needs $\hat\sigma^{\rm DIS}_{ij}=\hat\sigma^{\overline{\rm MS}}_{ij}-a\sum_k(Z_{ki}\otimes\hat\sigma^{(0)}_{kj}+Z_{kj}\otimes\hat\sigma^{(0)}_{ik})$
  at this order.

---------------------------------------------------------------------------------------------------

## 11. Mellin moments and the one-loop OPE Wilson coefficients

$X_N=\int_0^1dz\,z^{N-1}X(z)$, $S_k\equiv S_k(N)=\sum_{j=1}^Nj^{-k}$ (normalisation $\alpha_s/2\pi$ as in §0):
$$
\boxed{
\begin{aligned}
C^q_{2,N}&=C_F\Big[S_1^2-S_2+\frac32S_1-\frac{S_1}{N(N+1)}+\frac{3}{2N}+\frac{2}{N+1}+\frac{1}{N^2}-\frac92\Big],\\
C^g_{2,N}&=T_F\Big[-\frac{N^2+N+2}{N(N+1)(N+2)}S_1+\frac1{N^2}-\frac1N+\frac{6}{(N+1)(N+2)}\Big],\\
C^q_{L,N}&=\frac{2C_F}{N+1},\qquad C^g_{L,N}=\frac{4T_F}{(N+1)(N+2)},\\
P_{qq,N}&=C_F\Big[\frac32+\frac{1}{N(N+1)}-2S_1\Big],\qquad P_{qg,N}=T_F\frac{N^2+N+2}{N(N+1)(N+2)} .
\end{aligned}}
$$
Analytic continuation: $S_1(N)=\psi(N+1)+\gamma_E$, $S_2(N)=\zeta_2-\psi'(N+1)$.
In the normalisation $a_s=\alpha_s/4\pi$ used by BBDM and by most of the modern literature:
$c^{(1)}_{2,q}(N)=2C^q_{2,N}=C_F\big[2S_1^2-2S_2+3S_1-\frac{2S_1}{N(N+1)}+\frac3N+\frac4{N+1}+\frac2{N^2}-9\big]$.

| $N$ | $C^q_{2,N}/C_F$ | $C^g_{2,N}/T_F$ | $C^q_{L,N}/C_F$ | $C^g_{L,N}/T_F$ | $P_{qq,N}/C_F$ | $P_{qg,N}/T_F$ |
|---|---|---|---|---|---|---|
| 1 | 0 | 1/3 | 1 | 2/3 | 0 | 2/3 |
| 2 | 1/6 | −1/4 | 2/3 | 1/3 | −4/3 | 1/3 |
| 3 | 29/24 | −7/20 | 1/2 | 1/5 | −25/12 | 7/30 |
| 4 | 91/40 | −133/360 | 2/5 | 2/15 | −157/60 | 11/60 |
| 5 | 589/180 | −23/63 | 1/3 | 2/21 | −91/30 | 16/105 |
| 6 | 5281/1260 | −1777/5040 | 2/7 | 1/14 | −709/210 | 11/84 |
| 7 | 50791/10080 | −27/80 | 1/4 | 1/18 | −1027/280 | 29/252 |
| 8 | 58703/10080 | −16231/50400 | 2/9 | 2/45 | −9883/2520 | 37/360 |

Checks (`moments.py`): closed forms = numerical Mellin transforms of the x-space distributions for $N=1..10$ and for
non-integer $N$ (agreement $<10^{-29}$); x-space convolution with a toy PDF reproduces $C_Nf_N$ ($10^{-15}$).

**OPE check (independent computation of the Wilson coefficients).** The forward Compton amplitude
$T^{\mu\nu}$ of an on-shell massless parton is expanded in $p$ at fixed $q$ (hard region). For $p^2=0$ every other
region is scaleless, so the coefficient of $\omega^N$ ($\omega=2p\cdot q/Q^2=1/z$) is
$C_N^{\rm bare}(\varepsilon)\langle O_N\rangle^{\rm bare}_{\rm parton}$ with $\langle O_N\rangle^{\rm bare}_{\rm parton}=$ tree;
by the dispersion relation in $\omega$ it equals the $N$-th moment of the partonic structure function.
Diagrams: quark target — box, two vertex corrections, self-energy (direct channel; the crossed channel only
doubles even moments); gluon target — quark box, all $3!=6$ orderings (crossing even: odd moments vanish).
All loop integrals reduce to $\int d^Dl\,(p\cdot l)^a/[(l^2)^\alpha((l+sq)^2)^\beta]$ (closed form in `ope_check.py`).
Results:
1. `ope_check.py`: the Taylor coefficients agree **exactly in $\varepsilon$** (rational functions of $\varepsilon$) with the
   Mellin moments of the bare cut results real + virtual (§5, §6) for $N=1..8$ (quark, $F_2$ and $F_L$) and even
   $N\le8$ (gluon; the odd ones vanish) — `logs/ope_check_N8.log` (1604 s), `logs/ope_check_N6.log`;
2. `ope_wilson.py`: the $\overline{\rm MS}$-renormalised Wilson coefficients (finite parts at $\mu=Q$) reproduce
   $C^q_{2,N}$, $C^q_{L,N}$ ($N=1..6$) and $C^g_{2,N}$, $C^g_{L,N}$ ($N=2,4,6$) of the table exactly, the residues of
   the $1/\varepsilon$ poles are $-P_{qq,N}$ and $-P_{qg,N}$ (LO anomalous dimensions), and no $1/\varepsilon^2$ survives
   — `logs/ope_wilson_N6.log`.

This is a one-loop check of the equivalence between moment factorisation from the local OPE (Ch. 5) and
$x$-space factorisation with cut diagrams and $\overline{\rm MS}$ parton densities (Ch. 8).

---------------------------------------------------------------------------------------------------

## 12. Cross-checks: list with PASS/FAIL and literature conversions

Internal (all **PASS**):
* D-dim Dirac algebra vs explicit Clifford matrices in $D=2,4,6,8$ (`test_dirac.py`).
* Projectors (symbolic $D$; explicit components $D=4..7$; massive target) (`checks_setup.py`).
* Born normalisation exact in $D$; phase-space normalisation; angular measure; overall prefactor (`checks_setup.py`).
* Real matrix elements: symbolic $D$-dim traces = explicit $2^{D/2}$-dim matrices with explicit physical
  polarisation sums in $D=4,6,8,10$; Ward identity (`check_real_me_numeric.py`).
* Virtual form factor exact in $\varepsilon$ vs the closed form; Laurent coefficients $-2,-3,-8+\zeta_2$ (`dis_nlo.py`).
* No $1/\varepsilon^2$ in $F_2^q$; $1/\varepsilon$ pole $=-P_{qq}/\varepsilon$ incl. $\frac32\delta$; $F_L$ finite; gluon pole $=-2P_{qg}/\varepsilon$ (`dis_nlo.py`).
* $\mu$-dependence $=\ln(Q^2/\mu^2)P$ (from the $D$-dim result); $\mu_F$, $\mu_R$ independence at $O(\alpha_s)$ (symbolic + numerical) (`dis_nlo.py`, `scale_scheme.py`).
* OPE: bare moments exact in $\varepsilon$ for $N\le8$; renormalised Wilson coefficients and LO anomalous dimensions for $N\le6$ (`ope_check.py`, `ope_wilson.py`).
* Mellin moments: closed forms vs numerical transforms; whole-bracket-plus form of $C_2^q$; toy-PDF convolution (`moments.py`).

Literature (conversions stated explicitly):

| Source | Their normalisation | Conversion to ours | Result |
|---|---|---|---|
| Task statement (attributed to BBDM 1978 / Furmanski–Petronzio 1982 / ESW eq. (4.80)ff) | as §0 | identity | **PASS** (all four) |
| Vermaseren, Vogt, Moch, Nucl. Phys. B724 (2005) 3, hep-ph/0504242, eqs. (4.1)–(4.4), (B.3)–(B.4) (x-space), (A.3)–(A.4) (N-space); they attribute the first-order results to BBDM (their ref. [50]) | $x^{-1}F_2=C_{\rm ns}\otimes q_{\rm ns}+\langle e^2\rangle(C_q\otimes q_s+C_g\otimes g)$, $C=\sum a_s^nc^{(n)}$, $a_s=\alpha_s/4\pi$, $q_s=\sum_{i=1}^{n_f}(q_i+\bar q_i)$, $\langle e^2\rangle=\frac1{n_f}\sum e_i^2$ | $c^{(1)}_{2,\rm ns}=2C_2^q$; $c^{(1)}_{2,g}=4n_fC_2^g$ (with $T_F=\frac12$: $n_f\{(2-4x(1-x))(L_1-L_0)-2+16x(1-x)\}$) | **PASS** (x-space as distributions; N-space exact for $N=1..20$) |
| Moch, Vermaseren, Vogt, Phys. Lett. B606 (2005) 123, hep-ph/0411112, eqs. (1)–(3) | same, for $F_L$ | $c^{(1)}_{L,\rm ns}=4C_Fx=2C_L^q$; $c^{(1)}_{L,g}=8n_fx(1-x)=4n_fC_L^g$ | **PASS** |
| BBDM results as reported by T. Muta, Proc. 19th Int. Conf. High Energy Physics (Tokyo 1978), talk A12, p. 235 | sum rules | Adler: no $O(\alpha_s)$ correction $\Leftrightarrow C^q_{2,1}=0$; Bjorken $\int dx(F_1^{\bar\nu}-F_1^{\nu})=2[1-8/((33-2f)\ln(Q^2/\Lambda^2))]=2[1-\frac23\frac{\alpha_s}{\pi}]$ $\Leftrightarrow$ $C^q_{1,1}=C^q_{2,1}-C^q_{L,1}=-C_F$ (using $2F_1=F_2/x-F_L/x$) | **PASS** |
| Altarelli–Martinelli $F_L$ formula, Phys. Lett. B76 (1978) 89 **[form and reference recalled, not re-checked]**: $F_L=\frac{\alpha_s}{4\pi}x^2\int_x^1\frac{d\xi}{\xi^3}\big[\frac{16}{3}F_2(\xi)+8\sum_qe_q^2(1-\frac{x}{\xi})\xi g(\xi)\big]$ | $O(\alpha_s)$ with LO $F_2$ | follows from $C_L^q=2C_Fz$, $C_L^g=4T_Fz(1-z)$ ($C_F=4/3$, $T_F=1/2$, sum over flavours only) | **PASS** (algebraic) |
| Bardeen, Buras, Duke, Muta, Phys. Rev. D18 (1978) 3998 (original) | Wilson coefficients $1+\frac{g^2}{16\pi^2}B_n$ | $B_n=2C_N$ | **not opened** — compared only through the MVV and Muta citations above |
| Furmanski, Petronzio, Z. Phys. C11 (1982) 293 | — | — | **[unverified]**: paper not accessible here; only the task-quoted form was compared |
| Ellis, Stirling, Webber, *QCD and Collider Physics* (CUP 1996), eq. (4.80)ff | — | — | **[unverified]**: book not accessible; equation number and the presentation (sum over $q$ and $\bar q$ with one gluon term each, which is equivalent to our factor 2) taken from the task statement / memory |

---------------------------------------------------------------------------------------------------

## 13. Remarks and caveats for the monograph

1. **Gluon polarisation average.** The standard $\overline{\rm MS}$ $C_2^g$ requires averaging the incoming gluon
   over $D-2=2(1-\varepsilon)$ polarisations (consistent with the CDR normalisation of the gluon PDF). Averaging
   over 2 instead multiplies $R_2^g$ by $(1-\varepsilon)$ and shifts $C_2^g\to C_2^g+P_{qg}
   =T_F[(z^2+(1-z)^2)\ln\frac{1-z}{z}+6z(1-z)]$. $C_L^g$ is unaffected. **CONTEXT.md defines only the quark PDF;
   the gluon PDF definition (with $D-2$ transverse indices / polarisations in DR) should be added.**
2. **Normalisation of $W^{\mu\nu}$** ($1/4\pi$, §1.1) should be added to CONTEXT.md; it is fixed by the binding
   parton-model formula.
3. **$F_L$ definition**: $F_L=F_2-2xF_1$ holds for a massless target; with target mass,
   $F_L=(1+4x^2M^2/Q^2)F_2-2xF_1$ (§2).
4. The collinear pole has the form $-\frac1\varepsilon P$ with $\varepsilon<0$ (IR); in pure DR it is matched by the
   $\overline{\rm MS}$ PDF of the partonic target, $f_{i/j}=\delta_{ij}\delta-\frac{\alpha_s}{2\pi}\frac{P_{ij}}\varepsilon$. The
   statement "the PDF counterterm cancels the collinear pole" is literally the identity of §7.
5. The $1/\varepsilon^2$ cancellation real↔virtual and the cancellation of the final-state collinear pole are the
   one-loop instance of the unitarity/KLN argument used in the all-order DIS proof (Ch. 8): only initial-state
   collinear singularities survive the inclusive sum over final states.
6. $C_L$ is finite and scheme independent at $O(\alpha_s)$; $C_2^q$, $C_2^g$ are scheme dependent (DIS scheme, §10).
7. Rigor status: this is an explicit fixed-order computation; with the conventions above it is complete
   ([R] at $O(\alpha_s)$, given the definitions). The OPE cross-check uses the hard-region (large-momentum)
   expansion, whose validity for this one-loop integrand follows from the vanishing of scaleless integrals and
   the analyticity of $T(\omega)$ at $\omega=0$.

---------------------------------------------------------------------------------------------------

## 14. Files and how to reproduce

All in `"/Users/hao-cheng/Desktop/theorem proof/qcd_factorization_work/research/c_dis"`:

| File | Content |
|---|---|
| `dirac_d.py` | exact D-dim Dirac traces (Clifford relation only) |
| `test_dirac.py` | validation vs explicit matrices, $D=2,4,6,8$ |
| `real_me.py` | D-dim projected squared matrix elements, both channels |
| `check_real_me_numeric.py` | explicit-matrix / physical-polarisation check, $D=4,6,8,10$; Ward identity |
| `checks_setup.py` | projectors, Born normalisation, D-dim phase space, prefactor |
| `distributions.py` | plus-distribution algebra, Laurent expansion of $(1-z)^{-1-\varepsilon}G$ |
| `dis_nlo.py` | form factor, real emission exact in $\varepsilon$, poles, $\overline{\rm MS}$ coefficient functions, $\mu$ dependence |
| `check_closed_forms.py` | compact closed forms of §5–6 |
| `laurent_pieces.py` | separate real/virtual Laurent coefficients; invariant forms of the matrix elements |
| `moments.py` | Mellin moments, literature (MVV) N- and x-space, sum rules, x-space convolution test |
| `ope_check.py` | forward Compton amplitude (hard region) vs exact moments; `python3 -I ope_check.py 8` |
| `ope_wilson.py` | $\overline{\rm MS}$ Wilson coefficients and anomalous dimensions from the OPE; `python3 -I ope_wilson.py 6` |
| `scale_scheme.py` | $\mu_F$/$\mu_R$ independence (symbolic + numerical), DIS scheme |
| `dis_oneloop.tex` | Chinese LaTeX section (6 TikZ diagrams, all formulas, table, literature comments) for Ch. 8 / App. G |
| `test_build.tex`, `preamble_fact.tex` (copy), `test_build.pdf` | test driver (`xelatex test_build.tex`, twice): 7 pages, no errors, no overfull boxes, no undefined references |
| `logs/` | outputs of all scripts (`*.log`), incl. `ope_check_N8.log`, `ope_check_N6.log`, `ope_wilson_N6.log`, LaTeX runs |
