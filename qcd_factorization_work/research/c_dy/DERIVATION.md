# Drell–Yan: leading order, the $O(\alpha_s)$ $\overline{\rm MS}$ coefficient functions, and an abelian Glauber toy model

Directory: `"/Users/hao-cheng/Desktop/theorem proof/qcd_factorization_work/research/c_dy"`.
Every script runs with `python3 -I <script>.py` from this directory. Logs are in `logs/`. The LaTeX snippet for the
monograph is `dy_oneloop.tex`; `test_build.tex` builds it with the common preamble.

I derived everything below from scratch, with my own D-dimensional trace engine (`dtrace.py`). I then checked it
with sympy (exact in $\varepsilon$ where stated), with numpy/scipy/mpmath numerics, and against **downloaded**
literature sources (§6). **Status:** every check suite passes, with no FAIL:
- `dtrace` self-tests 7/7;
- `lo_check` 10/10;
- `nlo_checks` 25/25;
- `me_numeric` 3/3;
- `scale_check` 4/4;
- `glauber_toy` 25/25;
- `moments_exact` 1/1. Where an original
paper could not be consulted directly, I say so explicitly.

---------------------------------------------------------------------------------------------------------------

## 0. Results at a glance

**Conventions.** These are the binding conventions of `CONTEXT.md`: metric $(+,-,-,-)$, $D=4-2\varepsilon$, CDR,
$\overline{\rm MS}$ with $S_\varepsilon=(4\pi)^\varepsilon e^{-\varepsilon\gamma_E}$,
$a\equiv\alpha_s(\mu_R)/2\pi$, DGLAP $\partial f_i/\partial\ln\mu^2=a\,P_{ij}\otimes f_j$. Further:
- $\tau=Q^2/s$, $z=Q^2/\hat s$, and $D_k(z)\equiv[\ln^k(1-z)/(1-z)]_+$ with the CONTEXT plus prescription.
- A smooth prefactor *multiplies* a plus distribution: $\langle g\,D_k,h\rangle\equiv\langle D_k,gh\rangle=\int_0^1dz\,[g(z)h(z)-g(1)h(1)]\frac{\ln^k(1-z)}{1-z}$, i.e. $g(z)D_k=g(1)D_k+\frac{g(z)-g(1)}{1-z}\ln^k(1-z)$.
- One lepton flavour, massless leptons, photon exchange only.

**LO (derived and verified, §2):**
$$
\boxed{\frac{d\sigma}{dQ^2}=\frac{4\pi\alpha^2}{3N_cQ^2s}\sum_q e_q^2\int_0^1\!dx_1\,dx_2\,\delta(x_1x_2-\tau)
\big[q(x_1)\bar q(x_2)+\bar q(x_1)q(x_2)\big]}
=\frac{4\pi\alpha^2}{3N_cQ^4}\,\tau\sum_q e_q^2\int_\tau^1\frac{dx_1}{x_1}\big[q(x_1)\bar q(\tfrac{\tau}{x_1})+\bar q(x_1)q(\tfrac{\tau}{x_1})\big],
$$
$$
\boxed{\frac{d^2\sigma}{dQ^2\,dy}=\frac{4\pi\alpha^2}{3N_cQ^2s}\sum_q e_q^2\big[q(x_1)\bar q(x_2)+\bar q(x_1)q(x_2)\big],\qquad
x_{1,2}=\sqrt\tau\,e^{\pm y},\quad |y|\le\tfrac12\ln\tfrac1\tau .}
$$
Here $y=\frac12\ln(q^+/q^-)$ is the pair rapidity in the hadronic c.m. frame, with $q^+=x_1P_A^+$, $q^-=x_2P_B^-$, and hadron masses neglected (they enter only through $x_1x_2=\tau[1+O(M^2/s)]$).
The task's LO formula is correct **in every factor** (PASS).

**NLO, normalization (precise).**
$$
\frac{d\sigma}{dQ^2}=\frac{\sigma_0}{s}\sum_q e_q^2\int_0^1\!dx_1dx_2dz\,\delta(x_1x_2z-\tau)\Big\{\big[q(x_1)\bar q(x_2)+\bar q(x_1)q(x_2)\big]\Delta_{q\bar q}(z)
+\big[g(x_1)\big(q(x_2)+\bar q(x_2)\big)+\big(q(x_1)+\bar q(x_1)\big)g(x_2)\big]\Delta_{qg}(z)\Big\}+O(\alpha_s^2),
$$
where:
- $\sigma_0=4\pi\alpha^2/(3N_cQ^2)$;
- all PDFs are $\overline{\rm MS}$ at the scale $\mu_F$;
- $\Delta_{ij}$ is the $\overline{\rm MS}$-subtracted partonic cross section, normalized as $\hat s\,d\hat\sigma_{ij}/dQ^2=\sigma_0e_q^2\Delta_{ij}(z)$;
- $\Delta_{qg}$ is the coefficient for *one* quark (or antiquark) of flavour $q$ and one gluon.

Equivalently, $d\sigma/dQ^2=(\sigma_0/s)\sum e_q^2\,(f\otimes\Delta\otimes f)(\tau)$ with the Mellin convolution
$(f\otimes g)(x)=\int_x^1\frac{dy}{y}f(y)g(x/y)$.

**NLO coefficient functions (derived, all PASS, §3–§6):**
$$
\boxed{\begin{aligned}
\Delta_{q\bar q}&=\delta(1-z)+\frac{\alpha_s}{2\pi}\Big\{C_F\Big[4(1+z^2)\Big(\frac{\ln(1-z)}{1-z}\Big)_+-2\,\frac{1+z^2}{1-z}\ln z+\Big(\frac{2\pi^2}{3}-8\Big)\delta(1-z)\Big]+2P_{qq}(z)\ln\frac{Q^2}{\mu_F^2}\Big\},\\
\Delta_{qg}&=\frac{\alpha_s}{2\pi}\Big\{T_F\Big[\big(z^2+(1-z)^2\big)\ln\frac{(1-z)^2}{z}+\frac12+3z-\frac72z^2\Big]+P_{qg}(z)\ln\frac{Q^2}{\mu_F^2}\Big\},
\end{aligned}}
$$
with:
- $P_{qq}=C_F[\frac{1+z^2}{1-z}]_+=C_F[2D_0-(1+z)+\frac32\delta(1-z)]$ and $P_{qg}=T_F[z^2+(1-z)^2]$;
- $C_F=4/3$, $T_F=\frac12$ (the "$\frac12$" of the older literature *is* $T_F$, see §6.4);
- $\alpha_s=\alpha_s(\mu_R)$; there is no $\mu_R$ dependence at this order (checked: $\partial/\partial\ln\mu^2$ of every component vanishes).

Each term of the task's expected formulas (attributed there to Altarelli–Ellis–Martinelli 1979 / Ellis–Stirling–Webber) is reproduced exactly. That covers the coefficient of $D_1$, the $\ln z$ term, the $\delta$ term, the three logarithmic pieces of $\Delta_{qg}$ and its rational part, and the colour factors.

**$\mu_F$ independence:** $d\sigma/d\ln\mu_F^2=O(\alpha_s^2)$. This is shown exactly in Mellin space, and numerically in $x$ space with toy PDFs, where the cancellation holds to $10^{-13}$ (§5).

**Glauber toy (§7).** The model is an abelian theory with a massive vector boson in Feynman gauge, with eikonal (light-like) spectators. What it shows, precisely:
- **(G-i)** Spectator–spectator exchanges sum to $e^{i\chi(b)}$, with $\chi(b)=-\frac{g_Ag_B}{2\pi}K_0(m|b|)$ real and $b$ the spectators' relative transverse separation. This is exact in the abelian eikonal model; at one loop it is also derived from momentum-space residues.
- **(G-ii)** The phase cancels in any cross section inclusive in the spectators' relative transverse momentum: $O(g^2)$: $i\chi-i\chi=0$; $O(g^4)$: $\chi^2-\frac{\chi^2}2-\frac{\chi^2}2=0$; all orders $|e^{i\chi}|^2=1$. This includes $d\sigma/dQ^2$, $d\sigma/dQ^2dy$, and even $q_T$ spectra at leading power.
- **(G-iii)** For this exchange the $k^\pm$ contours are trapped (a genuine Glauber pinch), so contour deformation cannot replace (G-ii).
- **(G-iv)** At one loop, the exchange between the B-active parton and the A-spectator is *not* trapped in $k^+$. Its $k^+$ integral is saturated at $|k^+|\sim k_T^2/|k^-|\sim Q$, i.e. it is an A-collinear exchange with an eikonal B line. It therefore belongs to the A-PDF with its (past-pointing) Wilson line.
- **Not shown:** the non-abelian case; the all-order region analysis; power corrections; observables with measured hadrons.

---------------------------------------------------------------------------------------------------------------

## 1. Conventions and normalization

### 1.1 Process and factorized form
$h_A(P_A)+h_B(P_B)\to\ell^+\ell^-(q)+X$ through a virtual photon. $Q^2=q^2$, $s=(P_A+P_B)^2$, $\tau=Q^2/s$.
Hadron A moves in $+z$ and B in $-z$ (CONTEXT), so that
- A-collinear momenta have large $k^+$, and
- B-collinear momenta have large $k^-$.

Partons: $p_1=x_1P_A$ and $p_2=x_2P_B$ (massless), so $\hat s=x_1x_2s$ (hadron masses neglected) and $z=Q^2/\hat s$.

### 1.2 Master formula (§2.1)
$$
\hat s\,\frac{d\hat\sigma}{dQ^2}=\frac{2\alpha^2}{3Q^2}\int d\Phi_{\gamma^*X}\,\Big\langle-g_{\mu\nu}H^\mu H^{\nu*}\Big\rangle .
$$
- $H^\mu$ is the amplitude for $p_1+p_2\to\gamma^*(\mu)+X$. The photon propagator and the lepton charge are stripped; the quark charge $e_q$ and all QCD couplings are included.
- $\langle\cdot\rangle$ denotes the spin/colour average and the final-state sum.
- $d\Phi_{\gamma^*X}$ includes $(2\pi)^D\delta^D(p_1+p_2-q-p_X)$, with $q^2=Q^2$ fixed.
- The lepton tensor is integrated in 4 dimensions, $\int d\Phi_2L_{\mu\nu}=(q_\mu q_\nu-q^2g_{\mu\nu})/(6\pi)$. It is common to all channels and cancels in the coefficient functions.

### 1.3 Dimensional regularization and averages
- CDR, $\{\gamma^\mu,\gamma^\nu\}=2g^{\mu\nu}$, $g^\mu{}_\mu=D$, ${\rm Tr}\,1=4$, no $\gamma_5$.
- Bare coupling: $g_0^2=4\pi\alpha_s(\mu)\mu^{2\varepsilon}S_\varepsilon^{-1}=4\pi\alpha_s\mu^{2\varepsilon}e^{\varepsilon\gamma_E}(4\pi)^{-\varepsilon}$.
- Averages:
  - quark: spin $\frac12$ (two spin states in CDR), colour $\frac1{N_c}$;
  - gluon: polarization $\frac1{D-2}=\frac1{2(1-\varepsilon)}$, colour $\frac1{N_c^2-1}$.
- Polarization sums: $-g_{\mu\nu}$ for the photon index (current conservation, checked numerically: $q_\mu M^\mu=0$) and $-g_{\alpha\beta}$ for the single external gluon (QED-like Ward identity $k_\alpha M^{\mu\alpha}=0$, checked numerically; ghosts are not needed with one external gluon).
- **Gluon average convention.** The $\frac1{D-2}$ average is part of the $\overline{\rm MS}$ convention for the gluon density. With an average $\frac12$ instead, $\Delta_{qg}$ would shift by $+P_{qg}(z)$ (§3.10).

### 1.4 Bare partonic coefficient
$$
\Delta^{\rm bare}_{ij}(z,\varepsilon)=\frac{N_c}{2\pi e_q^2(1-\varepsilon)}\int d\Phi^{(D)}_{\gamma^*X}\big\langle-g_{\mu\nu}H^\mu H^{\nu*}\big\rangle ,
$$
which gives $\Delta^{(0)}_{q\bar q}=\delta(1-z)$. The factor $(1-\varepsilon)=(D-2)/2$ is the D-dimensional Born trace. Dividing by the *D-dimensional* Born is required for consistency, because the mass-factorization counterterm is $\Gamma\otimes\hat\sigma^{(0)}(\varepsilon)$, i.e. it multiplies the D-dimensional Born (§3.6).

---------------------------------------------------------------------------------------------------------------

## 2. Leading order

### 2.1 Master formula, step by step (`lo_check.py` (C))
1. With $J$ the lepton current, $|M|^2$ summed over lepton spins is $\frac{e^4}{Q^4}L_{\mu\nu}H^\mu H^{\nu*}$, with $L_{\mu\nu}={\rm Tr}[\ell\!\!/_1\gamma_\mu\ell\!\!/_2\gamma_\nu]$.
2. **Lepton tensor:** $\int d\Phi_2\,L_{\mu\nu}=\frac{1}{6\pi}(q_\mu q_\nu-q^2g_{\mu\nu})$.
   - Verified exactly in the rest frame (sympy angular integration), and by Monte Carlo in a boosted frame: PASS.
   - With $q_\mu H^\mu=0$, the contraction gives $\frac{e^4}{Q^4}\frac{Q^2}{6\pi}\langle-gHH^*\rangle=\frac{8\pi\alpha^2}{3Q^2}\langle-gHH^*\rangle$.
3. **Phase-space split:** $\frac{d^4q}{(2\pi)^4}=\frac{dQ^2}{2\pi}\frac{d^3q}{(2\pi)^32q^0}$.
4. **Flux:** $1/(2\hat s)$. Steps 1–4 combine to $\hat s\,d\hat\sigma/dQ^2=\frac{2\alpha^2}{3Q^2}\int d\Phi_{\gamma^*X}\langle-gHH^*\rangle$: PASS.

### 2.2 Born
- $\int d\Phi_{\gamma^*}=2\pi\,\delta(\hat s-Q^2)$, in any $D$.
- $\langle-gHH^*\rangle=\frac14\cdot\frac1{N_c^2}\cdot N_c\cdot e_q^2\,(D-2)\,2\hat s=e_q^2(1-\varepsilon)\hat s/N_c$.
- Hence
$$
\hat s\frac{d\hat\sigma^{(0)}}{dQ^2}=\frac{4\pi\alpha^2e_q^2}{3N_cQ^2}(1-\varepsilon)\,\hat s\,\delta(\hat s-Q^2)=\sigma_0e_q^2(1-\varepsilon)\,\delta(1-z).
$$

**Factor table** ($D=4$):

| factor | origin |
|---|---|
| $4\pi\alpha^2/(3Q^2)$ | point cross section $\sigma(e^+e^-\to\mu^+\mu^-)$ at c.m. energy$^2=Q^2$ (lepton tensor $\frac1{6\pi}$, photon propagator$^2$, $dQ^2/2\pi$, flux) |
| $e_q^2$ | quark charge |
| $1/N_c$ | colour average $\frac1{N_c^2}\sum_{ij}\delta_{ij}\delta_{ij}$ |
| $\delta(\hat s-Q^2)$ | $2\to1$ kinematics; $\delta(x_1x_2s-Q^2)=\delta(x_1x_2-\tau)/s$ supplies the $1/s$ |
| two orderings | $q$ from A and $\bar q$ from B, and vice versa |

**Explicit-matrix check** (`lo_check.py` (B), independent of `dtrace.py`; 4×4 Dirac matrices, explicit massless spinors, colour average):
- $\sigma(q\bar q\to\gamma^*\to\ell^+\ell^-)=4\pi\alpha^2e_q^2/(3N_c\hat s)$: ratio $1.000000000000$, PASS.
- Angular distribution $\propto1+\cos^2\theta$: PASS.

### 2.3 Hadronic formulae
Inserting the PDFs gives the boxed formulas of §0.
- **Rapidity.** In light-front variables, $q^+=x_1P_A^+$ and $q^-=x_2P_B^-$, so $Q^2=2q^+q^-=x_1x_2(2P_A^+P_B^-)$ and $y=\frac12\ln\frac{q^+}{q^-}=\frac12\ln\frac{x_1}{x_2}$ in the frame $P_A^+=P_B^-$. Also $2P_A^+P_B^-/s=1-O(M^2/s)$ (`lo_check.py` (D), PASS).
- **Jacobian.** $|\partial(x_1,x_2)/\partial(y,x_1x_2)|=1$ (symbolic, PASS). Therefore $\int dx_1dx_2\delta(x_1x_2-\tau)\delta(y-\frac12\ln\frac{x_1}{x_2})F=F(\sqrt\tau e^y,\sqrt\tau e^{-y})$.
- **Numerical check.** $\int dy\,d^2\sigma/dQ^2dy=d\sigma/dQ^2$ with toy PDFs: ratio $1.000000000000$, PASS.
- **Equivalent forms.** $d\sigma/dM=2M\,d\sigma/dQ^2$. Drell–Yan scaling: $Q^4d\sigma/dQ^2=\frac{4\pi\alpha^2}{3N_c}\tau\sum e_q^2\int_\tau^1\frac{dx_1}{x_1}[\dots]$ is a function of $\tau$ only at LO.

---------------------------------------------------------------------------------------------------------------

## 3. $O(\alpha_s)$ in dimensional regularization

### 3.1 Matrix elements (`dy_core.py`, `nlo_checks.py` §1, `me_numeric.py`)

**$q(p_1)\bar q(p_2)\to\gamma^*(q)g(k)$**, with $\hat t=(p_1-k)^2$ and $\hat u=(p_2-k)^2$. The amplitude, couplings stripped, is
$\bar v(p_2)\big[\gamma^\mu\frac{p\!\!/_1-k\!\!/}{\hat t}\gamma^\alpha+\gamma^\alpha\frac{k\!\!/-p\!\!/_2}{\hat u}\gamma^\mu\big]u(p_1)$. My trace engine gives
$$
T_{q\bar q}\equiv\sum_{\rm spins}\big|\ldots\big|^2_{(-g)(-g)}=8(1-\varepsilon)\Big[(1-\varepsilon)\Big(\frac{\hat u}{\hat t}+\frac{\hat t}{\hat u}\Big)+\frac{2\hat sQ^2}{\hat t\hat u}-2\varepsilon\Big],
\qquad \sum|H|^2=e_q^2g_0^2\,C_FN_c\,T_{q\bar q}.
$$

**$q(p_1)g(p_2)\to\gamma^*(q)q(k)$**, with $\hat t=(p_2-k)^2$ and $\hat u=(p_1-k)^2$:
$$
T_{qg}=-8(1-\varepsilon)\Big[(1-\varepsilon)\Big(\frac{\hat s}{\hat t}+\frac{\hat t}{\hat s}\Big)+\frac{2\hat uQ^2}{\hat s\hat t}-2\varepsilon\Big],\qquad
\sum|H|^2=e_q^2g_0^2\,T_F(N_c^2-1)\,T_{qg}.
$$

Checks:
- Crossing: $T_{qg}(\hat s,\hat t,\hat u)=-T_{q\bar q}(\hat s\to\hat u,\hat t\to\hat s,\hat u\to\hat t)$: PASS.
- **Independent numerical check** at $D=4$ (`me_numeric.py`): explicit spinors and *physical* gluon polarization vectors (no $-g$ replacement), 6 random phase-space points, both channels agree to $10^{-15}$. Ward identities hold to $10^{-14}$. PASS.

### 3.2 D-dimensional two-body phase space
In the partonic c.m. frame, with $v=(1-\cos\theta)/2$:
$$
d\Phi_2=\frac{1}{8\pi}\Big(\frac{4\pi}{\hat s}\Big)^\varepsilon\frac{(1-z)^{1-2\varepsilon}}{\Gamma(1-\varepsilon)}\,[v(1-v)]^{-\varepsilon}dv .
$$
- $q\bar q$: $\hat t=-\hat s(1-z)v$, $\hat u=-\hat s(1-z)(1-v)$. For $qg$: $\hat u=-\hat s(1-z)v$, $\hat t=-\hat s(1-z)(1-v)$.
- Checks: the angular measure equals the total solid angle in $D-1$ space dimensions (exact), and the total volume equals $|\vec k|^{D-3}\Omega_{D-1}/(4\sqrt{\hat s}(2\pi)^{D-2})$ (high-precision numerics). PASS.

### 3.3 Real emission, exact in $\varepsilon$
The $v$ integrals are Beta functions. Writing $K_r(\varepsilon)\equiv e^{\varepsilon\gamma_E}\Gamma(1-\varepsilon)/\Gamma(1-2\varepsilon)=1-\frac{3}{2}\zeta_2\varepsilon^2-\frac73\zeta_3\varepsilon^3+\dots$:
$$
\Delta^R_{q\bar q}=-\frac{\alpha_s}{2\pi}\,\frac{2C_F}{\varepsilon}\Big(\frac{\mu^2}{Q^2}\Big)^{\!\varepsilon}K_r(\varepsilon)\,z^\varepsilon(1-z)^{-1-2\varepsilon}\Big[1+z^2+\frac{2\varepsilon^2(1-z)^2}{1-2\varepsilon}\Big],
$$
$$
\Delta^R_{qg}=-\frac{\alpha_s}{2\pi}\,\frac{T_F}{2\varepsilon}\Big(\frac{\mu^2}{Q^2}\Big)^{\!\varepsilon}K_r(\varepsilon)\,z^\varepsilon(1-z)^{-2\varepsilon}\,
\frac{2\big(z^2+(1-z)^2\big)-\varepsilon(5z^2-6z+7)+\varepsilon^2(1+z)^2}{(1-\varepsilon)(1-2\varepsilon)} .
$$
Both closed forms equal the direct computation identically (`gammasimp` ratio $=1$): PASS.
- The prefactors are $\frac{g_0^2C_F}{8\pi(1-\varepsilon)}\int d\Phi_2T_{q\bar q}$ and $\frac{g_0^2T_F}{8\pi(1-\varepsilon)^2}\int d\Phi_2T_{qg}$. The extra $\frac1{1-\varepsilon}$ in the second is the gluon polarization average.
- The $q\bar q$ pole structure: soft $1/\varepsilon^2$ via $(1-z)^{-1-2\varepsilon}$, and collinear $-\frac2\varepsilon(1+z^2)$ from the two legs.
- The $qg$ channel has only a collinear $\frac1\varepsilon$ pole, from $\hat t\to0$, and no soft singularity.

### 3.4 Virtual correction (`dy_core.vertex_exact`)
The one-loop $q\bar q\gamma^*$ vertex, bare, massless, in Feynman gauge, with $\Gamma^\mu_1=-ig_0^2C_F\int\frac{d^Dk}{(2\pi)^D}\frac{\gamma^\alpha(-p\!\!/_2-k\!\!/)\gamma^\mu(p\!\!/_1-k\!\!/)\gamma_\alpha}{(k+p_2)^2(p_1-k)^2k^2}$, was computed as follows:
- Feynman parameters, with $\Delta=xy(-q^2-i0)$;
- the D-dimensional numerator, using $l^\rho l^\sigma\to g^{\rho\sigma}l^2/D$;
- the projection $F={\rm Tr}[p\!\!/_2\Gamma^\mu p\!\!/_1\gamma_\mu]/{\rm Tr}[p\!\!/_2\gamma^\mu p\!\!/_1\gamma_\mu]$, which is exact for massless on-shell quarks.

External self-energies are scaleless and vanish in DR, and $Z_1=Z_2$; coupling renormalization does not enter at this order. Result:
$$
F^{(1)}=\frac{\alpha_s}{4\pi}C_F\Big(\frac{\mu^2}{-q^2-i0}\Big)^{\!\varepsilon}f(\varepsilon),\qquad
f(\varepsilon)=-K_v(\varepsilon)\,\frac{2-\varepsilon+2\varepsilon^2}{\varepsilon^2(1-2\varepsilon)}=-\frac2{\varepsilon^2}-\frac3\varepsilon-8+\zeta_2+O(\varepsilon),
$$
with $K_v=e^{\varepsilon\gamma_E}\Gamma(1+\varepsilon)\Gamma^2(1-\varepsilon)/\Gamma(1-2\varepsilon)=1-\frac12\zeta_2\varepsilon^2-\frac73\zeta_3\varepsilon^3+\dots$
- The Feynman-parameter result equals the closed form at 5 values of $\varepsilon$ to 35 digits: PASS.
- **Literature:** it equals the one-loop quark form factor of Moch–Vermaseren–Vogt (§6.3) through $\varepsilon^3$ in the script, and through $\varepsilon^4$ in a separate run: PASS.
- **Timelike continuation.** $(-q^2-i0)^{-\varepsilon}=(Q^2)^{-\varepsilon}e^{i\pi\varepsilon}$, so the interference with the Born gives
$$
\Delta^V=2{\rm Re}\,F^{(1)}\,\delta(1-z)=\frac{\alpha_s}{2\pi}C_F\Big(\frac{\mu^2}{Q^2}\Big)^{\!\varepsilon}\cos(\pi\varepsilon)\,f(\varepsilon)\,\delta(1-z).
$$

### 3.5 Laurent expansion in distributions
I use the exact distributional identity on $[0,1]$
$$
(1-z)^{-1-2\varepsilon}=-\frac{\delta(1-z)}{2\varepsilon}+\sum_{k\ge0}\frac{(-2\varepsilon)^k}{k!}D_k(z),
$$
and bring everything into canonical form, $a\,\delta(1-z)+\sum_kb_kD_k+{\rm regular}$, with constants $a,b_k$.

Units $a=\alpha_s/2\pi$, $L=\ln(\mu^2/Q^2)$ (log `logs/expansions_print.log`):

| piece | $\varepsilon^{-2}$ | $\varepsilon^{-1}$ | $\varepsilon^{0}$ |
|---|---|---|---|
| real $q\bar q$ | $2C_F\delta$ | $2C_FL\,\delta-4C_FD_0+2C_F(1+z)$ | $C_F(L^2-\frac{\pi^2}2)\delta-4C_FL\,D_0+8C_FD_1+2C_F(1+z)L-4C_F(1+z)\ln(1-z)-2C_F\frac{1+z^2}{1-z}\ln z$ |
| virtual | $-2C_F\delta$ | $-C_F(3+2L)\delta$ | $C_F(-L^2-3L-8+\frac{7\pi^2}6)\delta$ |
| real $qg$ | — | $-P_{qg}(z)$ | $T_F\big[(z^2+(1-z)^2)\ln\frac{(1-z)^2}z+\frac{1+6z-7z^2}2\big]-P_{qg}L$ |

- **Soft double poles cancel** between real and virtual: PASS.
- **The remaining pole** of real+virtual is exactly $-\frac{2}{\varepsilon}P_{qq}(z)$, one for each incoming parton (initial-state collinear): PASS.
- **Origin of $\pi^2$** in the $\delta$ coefficient (`plus_trap.py`): $-\frac{\pi^2}2$ from $K_r$, $+\frac{\pi^2}6$ from $K_v$, and $+\pi^2$ from the timelike continuation $\cos\pi\varepsilon$, totalling $\frac{2\pi^2}3$.
  - The $+\pi^2C_F$ is the "$\pi^2$ enhancement", i.e. $|F(q^2)/F(-q^2)|^2-1$ at one loop.
  - The $i\pi/\varepsilon$ Coulomb phase of the active $q\bar q$ pair cancels in $2{\rm Re}F$.

### 3.6 $\overline{\rm MS}$ mass factorization
The bare partonic cross section factorizes as $\Delta^{\rm bare}_{ij}(\varepsilon)=\sum_{kl}\Gamma_{ki}\otimes\Gamma_{lj}\otimes\Delta_{kl}(\varepsilon)$, with the $\overline{\rm MS}$ parton-in-parton densities
$$
\Gamma_{ki}(x)=\delta_{ki}\delta(1-x)-\frac{\alpha_s(\mu)}{2\pi}\frac1\varepsilon\Big(\frac{\mu^2}{\mu_F^2}\Big)^{\!\varepsilon}P_{ki}(x)+O(\alpha_s^2)
$$
(pure poles with the 4-dimensional $P$; the factor $(\mu^2/\mu_F^2)^\varepsilon$ converts $\alpha_s(\mu_F)$ to $\alpha_s(\mu)$ at this order). Therefore
$$
\Delta_{q\bar q}=\Delta^{\rm bare}_{q\bar q}+2\,a\,\tfrac1\varepsilon(\mu^2/\mu_F^2)^\varepsilon P_{qq},\qquad
\Delta_{qg}=\Delta^{\rm bare}_{qg}+a\,\tfrac1\varepsilon(\mu^2/\mu_F^2)^\varepsilon P_{q g} .
$$
In the $qg$ channel the subtraction is $f_{\bar q/g}\otimes\hat\sigma_{q\bar q}$, with $P_{\bar qg}=P_{qg}$.

All poles cancel in both channels, and the result is independent of $L$ (the $\mu_R$-type logarithm): PASS. The boxed results of §0 follow. Explicitly, at $\mu_F=Q$ in canonical form:

$\Delta^{(1)}_{q\bar q}=C_F\big\{8D_1+(\frac{2\pi^2}3-8)\delta(1-z)-4(1+z)\ln(1-z)-2\frac{1+z^2}{1-z}\ln z\big\}$, where $4(1+z^2)D_1=8D_1-4(1+z)\ln(1-z)$.

### 3.7 Equivalent forms, moments, threshold limit
- **Mellin moments** at $\mu_F=Q$, with $C_F=4/3$ and $T_F=\frac12$. These are exact closed forms, derived by hand and checked to 40 digits in `moments_exact.py` (PASS):
  - $N=1$: $\Delta_{q\bar q}^{(1)}=C_F(8\zeta_2-\frac72)=12.879296713\ldots$ and $\Delta^{(1)}_{qg}=T_F/9$;
  - $N=2$: $\Delta^{(1)}_{q\bar q}=C_F(8\zeta_2+\frac{13}{18})=18.508926342\ldots$ and $\Delta^{(1)}_{qg}=-\frac{11}{18}T_F$.
- **Large $N$:** $\Delta_{q\bar q,N}=1+a\,C_F\big[4\ln^2\bar N+8\zeta_2-8\big]+O(\ln N/N)$ with $\bar N=Ne^{\gamma_E}$. This uses $\langle D_1,z^{N-1}\rangle=\frac12[S_1(N-1)^2+S_2(N-1)]$ (PASS) and $\langle D_0,z^{N-1}\rangle=-S_1(N-1)$.
- **DIS scheme.** Here $q^{\rm DIS}=q+a\,[C_2^q\otimes q+C_2^g\otimes g]$, where $C_2^{q,g}$ are the $\overline{\rm MS}$ DIS coefficient functions in the normalization $F_2/x=\sum e_q^2\{q+\bar q+a[C_2^q\otimes(q+\bar q)+2C_2^g\otimes g]\}$, as derived independently in `research/c_dis` (they agree with Vermaseren–Vogt–Moch 2005, checked by c_dis). Then
$$
\Delta^{\rm DIS}_{q\bar q}=\Delta_{q\bar q}-2C_2^q=C_F\Big[\Big(1+\frac{4\pi^2}3\Big)\delta(1-z)+2(1+z^2)D_1+3D_0-6-4z\Big],
\qquad
\Delta^{\rm DIS}_{qg}=\Delta_{qg}-C_2^g=T_F\Big[(z^2+(1-z)^2)\ln(1-z)+\frac32-5z+\frac92z^2\Big].
$$
  These are the commonly quoted DIS-scheme forms (AEM worked in this scheme). I have **not** compared them with the printed AEM 1979 paper, which I could not consult: PASS relative to the commonly quoted forms; original unverified.

### 3.8 Literature comparisons: see §6.

### 3.9 Factorization-scale independence: see §5.

### 3.10 Remarks on conventions that change the finite parts
1. **Plus prescription placement.** $(1+z^2)D_1$ and $[(1+z^2)\ln(1-z)/(1-z)]_+$ differ by $\frac74\delta(1-z)$, from $\int_0^1(1+z)\ln(1-z)dz=-\frac74$ (`plus_trap.py`). With the plus on the whole term the $\delta$ coefficient of $\Delta_{q\bar q}$ would read $C_F(\frac{2\pi^2}3-1)$, not $C_F(\frac{2\pi^2}3-8)$. The monograph must state which convention is meant; the task's formula, and mine, has $(1+z^2)$ *multiplying* $D_1$.
2. **Gluon polarization average.** $\frac1{2(1-\varepsilon)}$, the standard $\overline{\rm MS}$ convention, is used throughout. With $\frac12$, the bare $qg$ term is multiplied by $(1-\varepsilon)$ and $\Delta_{qg}\to\Delta_{qg}+P_{qg}$; this is a different scheme. My result agrees with the modern $\overline{\rm MS}$ literature (§6.1), which fixes the convention.
3. **D-dimensional Born normalization.** Normalizing by the D-dimensional Born, including $(1-\varepsilon)$, is consistent with the counterterm $\Gamma\otimes\hat\sigma^{(0)}(\varepsilon)$. Normalizing by the 4-dimensional Born in one place but not the other would shift $\Delta_{q\bar q}$ by $\pm2P_{qq}$.
4. **No $\mu_R$ dependence at $O(\alpha_s)$.** The first $\mu_R$ logarithm is $\propto\beta_0\ln(\mu_R^2/\mu_F^2)\Delta^{(1)}$ at $O(\alpha_s^2)$.

---------------------------------------------------------------------------------------------------------------

## 4. LO formulas: what exactly was verified
`lo_check.py`, 10/10 PASS:
- (A) the lepton-tensor identity, exact and Monte Carlo;
- (B) explicit-spinor completeness, the $1+\cos^2\theta$ distribution, and $\sigma=4\pi\alpha^2e_q^2/(3N_c\hat s)$ to $10^{-12}$;
- (C) the master-formula prefactor $2\alpha^2/(3Q^2)$, and the Born limit $\sigma_0e_q^2\delta(1-z)$;
- (D) the rapidity Jacobian, $\int dy\,d^2\sigma/dQ^2dy=d\sigma/dQ^2$ to $10^{-12}$, and the light-front kinematics.

---------------------------------------------------------------------------------------------------------------

## 5. $\mu_F$ independence at $O(\alpha_s)$ (`scale_check.py`, 4/4 PASS)

**(A) Mellin space, exact.** With $\gamma_{ij}(N)=\int_0^1z^{N-1}P_{ij}$ and $\ell_F=\ln(\mu_F^2/Q^2)$:
- $\Delta_{q\bar q,N}=1+a[\Delta^{(1)}_N-2\gamma_{qq}\ell_F]$ and $\Delta_{qg,N}=a[\Delta^{(1)}_{qg,N}-\gamma_{qg}\ell_F]$;
- DGLAP: $dq_N/d\ell_F=a(\gamma_{qq}q_N+\gamma_{qg}g_N)$.

Then
$$
\frac{d\sigma_N}{d\ell_F}\propto a\big[(\gamma_{qq}q_A+\gamma_{qg}g_A)\bar q_B+q_A(\gamma_{qq}\bar q_B+\gamma_{qg}g_B)+(A\leftrightarrow B,\ q\leftrightarrow\bar q)\big]
-2a\gamma_{qq}(q_A\bar q_B+\bar q_Aq_B)-a\gamma_{qg}\big[g_A(q_B+\bar q_B)+(q_A+\bar q_A)g_B\big]+O(a^2)=O(a^2).
$$
The $\gamma_{qq}$ terms cancel within the $q\bar q$ channel. The $\gamma_{qg}$ terms, coming from $\bar q$ (or $q$) being generated by $g$, cancel against the $qg$ channel. Symbolic check: PASS.

**(B) $x$ space, numerical.** Toy PDFs; DGLAP derivatives built with the CONTEXT convolution, $(D_0\otimes f)(x)=\int_x^1dz\frac{f(x/z)/z-f(x)}{1-z}+f(x)\ln(1-x)$; triple convolutions $\int dx_1dx_2dz\,\delta(x_1x_2z-\tau)$ with the plus prescription handled exactly.
- $q\bar q$ sector: Born×$P_{qq}$-evolution $=-78.50206648071$ against PDFs×$\partial_{\ln\mu_F^2}(2P_{qq}\ln)$ $=+78.50206648069$. Relative residual $3\times10^{-13}$: PASS.
- $qg$ sector: residual $8\times10^{-14}$: PASS.
- Control: replacing the factor 2 in front of $P_{qq}\ln(Q^2/\mu_F^2)$ by 1 leaves a 50% residual: PASS. The check is sensitive.

---------------------------------------------------------------------------------------------------------------

## 6. Literature comparisons (sources downloaded; conventions converted explicitly)

### 6.1 Duhr–Dulat–Mistlberger, JHEP 11 (2020) 143, arXiv:2007.13313 (INSPIRE Duhr:2020sdp), ancillary files
**Source.** `Distributions.m` and `XSReg.m`, read as text in an isolated directory and transcribed by hand into `nlo_checks.py`; nothing was executed.

**Their conventions** (paper §2, read from the arXiv source):
- $\sigma_W=\tau\sigma_0\sum_{ij}f_i\otimes\eta_{ij}\otimes f_j$, with $(f\otimes g)(x)=\int_x^1\frac{dx'}{x'}f(x')g(x/x')$;
- $\eta^{(0)}_{d\bar u}=|V|^2\delta(1-z)$, expansion in $a_S=\alpha_s(\mu_R)/\pi$, $\overline{\rm MS}$, CDR.
- V and A currents give identical QCD corrections, so they compute with a vector current. For a $W$, the flavour structure replaces $e_q^2$ by $|V|^2$.

**Conversion:** $\Delta^{(1)}$ (units $\alpha_s/2\pi$) $=2\,\eta^{(1)}$ (units $\alpha_s/\pi$), with $|V|^2\to1$, $\ln(Q^2/\mu_F^2)=-L_F$, and their $G[0,\bar z]=\ln(1-z)$, $G[1,\bar z]=\ln z$.

**Their NLO entries.** These are short enough to verify by hand; in units $\alpha_s/\pi$, with $\bar z=1-z$:
- $d\bar u$: $\frac{16}{3}D_1+\frac83L_QD_0-\frac{1440-120\pi^2-540L_Q}{270}\delta+\frac{(N_c^2-1)}{N_c}(\bar z-2)\ln\bar z-\frac{N_c^2-1}{2N_c}\frac{1+z^2}{1-z}\ln z+\frac{N_c^2-1}{2N_c}(\bar z-2)L_Q$;
- $g\bar u$: $\frac{1+6z-7z^2}8+\frac{z^2+(1-z)^2}2\ln(1-z)-\frac{z^2+(1-z)^2}4\ln z+\frac{z^2+(1-z)^2}4L_Q$.

**Result:** $\Delta_{q\bar q}$ and $\Delta_{qg}$, including the full $\mu_F$ dependence, agree **exactly** ($\delta$, $D_k$, regular part, and test-function actions): **PASS, PASS.**

### 6.2 Moch–Vogt, Phys. Lett. B 631 (2005) 48, hep-ph/0508265 (Moch:2005ky), eq. (g01DY)
They write $C^N=(1+a_sg_{01}+\dots)\exp(G^N)$, with $a_s=\alpha_s/4\pi$, $G^N$ in powers of $\ln N$ and without a constant term at $O(a_s)$, and $g_{01}^{\rm DY}=C_F(-16+16\zeta_2+8\gamma_E^2)$.

Our large-$N$ moments give $2\Delta^{(1)}_N=C_F[8\ln^2N+16\gamma_E\ln N+g_{01}/C_F]+O(\ln N/N)$. Numerically, the residual is $0.234$, $0.033$, $0.0042$ at $N=200$, $2000$, $20000$, i.e. $\propto\ln N/N$: **PASS.**

### 6.3 Moch–Vermaseren–Vogt, JHEP 08 (2005) 049, hep-ph/0507039 (Moch:2005id), eq. (ff1loopexplicit)
They define $\mathcal F_b=1+a_s^b(Q^2/\mu^2)^{-\varepsilon}\mathcal F_1$, spacelike $Q^2=-q^2$, with $S_\varepsilon$ absorbed per loop. Their
$\mathcal F_1=C_F[-\frac2{\varepsilon^2}-\frac3\varepsilon-8+\zeta_2+\varepsilon(-16+\frac32\zeta_2+\frac{14}3\zeta_3)+\dots]$, through $\varepsilon^4$, equals our $C_Ff(\varepsilon)$ term by term: **PASS.**

Their timelike continuation, $(-q^2/\mu^2)^{-l\varepsilon}\to(q^2/\mu^2)^{-l\varepsilon}[\cos(\pi l\varepsilon)-i\sin(\pi l\varepsilon)]$, gives the same $\cos\pi\varepsilon$ as ours in $2{\rm Re}F$. The sign of the imaginary part depends on whether $\pm i0$ is used, and is irrelevant for $|F|^2$.

### 6.4 The task's expected formulas (attributed to AEM 1979 / ESW 1996)
- Every term agrees (`nlo_checks.py` §6): **PASS** for $\Delta_{q\bar q}$ and **PASS** for $\Delta_{qg}$.
- **$T_F$ versus $\frac12$:** the colour factor of the $qg$ channel is computed, not assumed. $\frac{1}{N_c(N_c^2-1)}{\rm Tr}(t^at^a)=\frac{T_F}{N_c}$, against the Born's $\frac1{N_c}$, gives an overall $T_F$, with $T_F=\frac12$ for ${\rm Tr}(t^at^b)=T_F\delta^{ab}$. The "$\frac12$" in older formulas is this $T_F$ (often written $T_R$).
- The equation numbers in AEM 1979 and in ESW were **not** checked (the sources were not accessible). The verification rests on §6.1–6.3 and on the internal checks.

### 6.5 Status of the original NLO literature
- AEM 1979 (`AltarelliEllisMartinelli1979`, verified reference) is the standard citation for the first NLO DY calculation, in the DIS scheme. DDM's paper also cites Kubar-André–Paige, Harada–Kaneko–Sakai and Aurenche–Lindfors (refs. in arXiv:2007.13313) as NLO references. I did not consult these originals and make no claim about their printed formulas.
- The full $O(\alpha_s^2)$ result is Hamberg–van Neerven–Matsuura 1991 (`HambergVanNeervenMatsuura1991`, verified reference).

---------------------------------------------------------------------------------------------------------------

## 7. Glauber toy model (`glauber_toy.py`, 25/25 PASS)

### 7.1 Model and power counting
**Fields.** An abelian vector boson of mass $m$ (an IR regulator), in Feynman gauge with propagator $-ig_{\mu\nu}/(k^2-m^2+i0)$, and charged scalars $\phi_j$ with $D_\mu=\partial_\mu-ig_jA_\mu$, so the vertex is $+ig_j(p+p')^\mu$.
- Using fermions instead of scalars changes nothing at leading power: $\bar u(p+k)\gamma^\mu u(p)\to2p^\mu$.

**Hadrons and hard vertex.** Hadron A ($+z$) dissociates through a $\phi^3$-type vertex into an active parton $a$ and a spectator $s_A$; similarly B ($-z$) into $b$ and $s_B$. Then $a$ and $b$ annihilate at a hard vertex into a neutral state of mass $Q$ (the "$\gamma^*$").

**Power counting.** With $\lambda\ll1$:
- A-collinear: $(1,\lambda^2,\lambda)Q$;
- B-collinear: $(\lambda^2,1,\lambda)Q$;
- Glauber: $k\sim(\lambda^2,\lambda^2,\lambda)Q$, $|k^+k^-|\ll k_T^2$.

At leading power in the Glauber region:
- A-collinear propagators depend on $k^-$ only, $(p+k)^2-m^2\simeq2p^+(k^--k_0^-)$ with $k_0^-$ real;
- B-collinear propagators depend on $k^+$ only;
- the boson propagator $\simeq-1/(k_T^2+m^2)$.

### 7.2 (G-i) Spectator–spectator exchange: an exact phase for eikonal spectators
Represent the spectators as infinite straight light-like lines, $x_j(\lambda)=b_j+\lambda v_j$, with $v_A=(1^+,0^-,0_T)$ and $v_B=(0^+,1^-,0_T)$. Then:
- $W_j=\exp(ig_j\int_{-\infty}^\infty d\lambda\,v_j\!\cdot\!A)$;
- for a free abelian field, $\langle T\,W_AW_B\rangle=\exp(-\frac12\langle(\int J\!\cdot\!A)^2\rangle)$;
- the self terms are $\propto v_j^2=0$ and vanish in Feynman gauge;
- the cross term is
$$
-g_Ag_B\,v_A\!\cdot\!v_B\!\int\!\frac{d^4k}{(2\pi)^4}\frac{-i\,e^{-ik\cdot(b_A-b_B)}}{k^2-m^2+i0}\,2\pi\delta(k^-)\,2\pi\delta(k^+)
=-ig_Ag_B\!\int\!\frac{d^2k_T}{(2\pi)^2}\frac{e^{ik_T\cdot b}}{k_T^2+m^2}\equiv i\chi(b),
$$
$$
\boxed{\chi(b)=-\frac{g_Ag_B}{2\pi}K_0(m|b|),\qquad b=b_A-b_B .}
$$

Notes:
- Infinite lines force $k^\pm=0$ exactly: the exchange is *purely* Glauber.
- The Fourier transform was checked numerically (3 points, `quadosc`): PASS.
- Coulomb limit $m\to0$: $\chi\to\frac{g_Ag_B}{2\pi}[\ln\frac{mb}2+\gamma_E]$. This is IR divergent but real, i.e. a pure (divergent) phase: PASS.
- The exponent is purely imaginary, so the vacuum-persistence probability is 1 and there is no real radiation, consistent with uniformly moving sources.

### 7.3 (G-i') The same at one loop from momentum-space residues
Take finite-energy spectators: $s_A$ has final momentum $p'_A$, on shell. Route the boson momentum $k$ from $s_B$ to $s_A$. Then $s_A$ carries $p'_A-k$ before the exchange; $a$ carries $P_A-p'_A+k$, $b$ carries $P_B-p'_B-k$, and $q=P_A+P_B-p'_A-p'_B$ is independent of $k$.
- **$k^-$ integral.** The A-side poles are $s_A$, $i/(-2p'^+_A(k^--k_1)+i0)$, in the **UHP**, and $a$, $i/(2p_a^+(k^--k_2)+i0)$, in the **LHP**. Closing above,
$$
\int\frac{dk^-}{2\pi}\frac{i}{-2p'^+_A(k^--k_1)+i0}F(k^-)=\frac{F(k_1)}{2p'^+_A}.
$$
  The spectator is put on shell at momentum $p'_A-k$.
  - Numerically, on an exactly indented contour: $30.63725490\,i$ against the prediction $30.63725490\,i$, PASS.
  - Control: with both poles on the same side the integral vanishes, $3\times10^{-15}$, PASS.
- **$k^+$ integral.** The same, with the B side.
- **Assembly:** $(\frac1{2p'^+_A})(\frac1{2p'^-_B})(ig_A)(ig_B)(4p'^+_Ap'^-_B)\frac{-i}{-k_T^2-m^2}=\frac{-ig_Ag_B}{k_T^2+m^2}$, so
$$
M_1(p'_A,p'_B)=\int\frac{d^2k_T}{(2\pi)^2}\,\frac{-ig_Ag_B}{k_T^2+m^2}\,M_0(p'_A-k_T,\,p'_B+k_T).
$$
  In impact-parameter space (conjugate to the relative spectator momentum) this is $M_1=i\chi(b)M_0$, identical to §7.2 at $O(g^2)$: PASS.
- **Higher orders.** The $n$-exchange ladder plus crossed ladders sum to $(i\chi)^n/n!$ by the eikonal identity. Algebraically, $\sum_{\rm perms}\prod_j1/(w_{\sigma1}+\dots+w_{\sigma j})=\prod_j1/w_j$ (symbolic for $n\le4$, exact rationals for $n=5,6$, PASS). Its on-shell distributional form, $2\pi\delta(w_1+w_2)[\frac{i}{w_1+i0}+\frac{i}{w_2+i0}]=(2\pi)^2\delta(w_1)\delta(w_2)$, was checked numerically: PASS. For abelian infinite lines, §7.2 gives the exponential directly.

### 7.4 (G-ii) Unitarity: the phase cancels in inclusive cross sections
Write the final-state spectator momenta as total $P=p'_A+p'_B$ and relative $p=(p'_A-p'_B)/2$, with conjugates $B$ and $b$. The Glauber exchange shifts only $p$; $q_T=-P$ is untouched, and $q^\pm$ change only at $O(\lambda^2)$.

For any observable not depending on $p$ (in particular $d\sigma/dQ^2$, $d\sigma/dQ^2dy$, and even $d\sigma/dQ^2dyd^2q_T$ at leading power), integrating over $p$ and applying Parseval gives
$$
\int d^2p\,|M|^2=(2\pi)^2\!\int d^2b\,|\tilde M_0(P,b)|^2\,|e^{i\chi(b)}|^2=\int d^2p\,|M_0|^2 .
$$

At fixed order the cancellation is between different cut positions relative to the exchanged bosons:
- $O(g^2)$: $i\chi-i\chi=0$;
- $O(g^4)$: $|M_1|^2+2{\rm Re}M_0^*M_2\leftrightarrow\chi^2-\frac12\chi^2-\frac12\chi^2=0$;
- $O(g^{2n})$: $\sum_j\frac{(i\chi)^j}{j!}\frac{(-i\chi)^{n-j}}{(n-j)!}=0$ (symbolic, $n\le8$, PASS).

**Numerical demonstration** (FFT, $512^2$ grid, *complex* toy amplitude $M_0(p)$):
- the pointwise $O(g^2)$ interference is $O(1)$, with $\int|\cdot|=0.39$, but its integral is $4\times10^{-17}$: PASS;
- the $O(g^4)$ cut sum gives $-4\times10^{-18}$ against $\int|M_1|^2=0.16$: PASS;
- the discretized $i\chi(b)$ is purely imaginary to $10^{-15}$: PASS;
- all orders: $\int|e^{i\chi}\otimes M_0|^2/\int|M_0|^2=1.000000000000000$: PASS;
- the relative-$k_T$ distribution *is* changed ($\langle p^2\rangle$ shifts by $0.137$): PASS.

So the cancellation is not trivial: it requires summing over the spectator states.

### 7.5 (G-iii) The spectator–spectator Glauber region is trapped
For the $k^+$ integral with the **exact** boson propagator, the B-side poles are $s_B$ at $\kappa_s-i0$ (LHP) and $b$ at $\kappa_b+i0$ (UHP), with $|\kappa|\sim\lambda^2$.
- The real-axis value (exact indented contour) equals the residue formula at a Glauber-scale pole: PASS for $k^-=\pm0.6\lambda^2$.
- At that point, the Glauber approximation for the boson propagator is accurate to $<\lambda^2$: PASS.
- Lifting or lowering the contour by $i\lambda$ changes the value: PASS. The contour cannot be moved out of the Glauber region.
- The same holds for $k^-$ (the poles of $s_A$ and $a$ lie on opposite sides).

This is the DY "Glauber pinch". It is handled by (G-ii), not by deformation.

### 7.6 (G-iv) Active–spectator exchange is deformable into the collinear region (one loop)
Take the boson between $s_A$ and the active $b$ (an initial-state interaction).
- The $k^-$ contour is trapped by $s_A$ and $a$.
- The **only** leading-power $k^+$ dependence near the Glauber region is the $b$ propagator, $1/(2p_b^-k^++c_b+i0)$, with its pole in the LHP. The other $k^+$ singularities sit at $|k^+|\sim Q$: the boson pole at $k^+=k_T^2/(2k^-)$, and the A-collinear lines.

With the exact boson propagator:
$$
I_{as}(k^-)\equiv\int dk^+\frac{1}{(2p_b^-k^++c_b+i0)(2k^+k^--K^2+i0)}=\frac{2\pi i\,\theta(-k^-)}{2p_b^-K^2+2k^-c_b},\qquad K^2=k_T^2+m^2 .
$$
- It is saturated by the boson pole at $k^+=-K^2/(2|k^-|)$, which is $-1.08$ for $\lambda=0.1$, i.e. $|k^+|\sim Q$: **A-collinear, not Glauber.**
- Numerically (exact indented contours, PASS for both signs of $k^-$), the real-axis value, the formula, and the value on a contour lifted by $i\lambda$ over $|{\rm Re}\,k^+|<3\lambda$ all agree.
- On the lifted contour, $|2p_b^-k^+|\gg k_T^2$, and replacing $b$ by the eikonal line $1/(2p_b^-k^++i0)$ changes the result by $2.8\times10^{-3}<\lambda^2$: PASS.

**Interpretation.** At one loop the exchange is part of the A-collinear subgraph, attached to an eikonal line along $n_B$. The $+i0$ of $b$ corresponds to a **past-pointing** line, which is the Wilson line in $f_{q/A}$.
- For **collinear** PDFs, past and future pointing are identical: $W[w,-\infty n_-]\,W[-\infty n_-,0]=W[w,0]=W[w,+\infty n_-]\,W[+\infty n_-,0]$ when $w$ and $0$ lie on the same light-like ray (an operator identity, the group property).
- In the toy: semi-infinite past and future lines give $-i/(k-i0)$ and $i/(k+i0)$. Each carries $\pi\delta(k)$; their principal parts are opposite; their sum is the full line $2\pi\delta(k)$ (symbolic, PASS).
- For TMDs (transverse separation) the staple does not collapse, which is where the past/future distinction becomes physical (Ch. 11).

### 7.7 What is shown, and what is not

**Shown** (abelian theory, massive boson, Feynman gauge, leading power in $\lambda$):
1. Eikonal (infinite light-like) spectators: spectator–spectator exchanges give exactly $e^{i\chi(b)}$ with $\chi$ real. Self-energies vanish since $v^2=0$.
2. Finite-energy spectators at one loop: the Glauber-region contribution equals $i\chi\otimes M_0$, with the spectators on shell; the $k^\pm$ contours are trapped.
3. Any cross section inclusive in the spectators' relative transverse momentum is unaffected, order by order (cut sums) and to all orders in the eikonal model. The phase does affect spectator-differential distributions.
4. At one loop, the B-active/A-spectator exchange is not trapped in $k^+$: its $k^+$ integral equals that of an eikonal B line up to $O(\lambda^2)$ and is saturated at $|k^+|\sim Q$. It is therefore an A-collinear contribution to $f_{q/A}$ with a past-pointing Wilson line.

**Not shown:**
- (a) **Non-abelian theory.** Phases become colour matrices that do not commute with the hard colour flow; the full argument is Collins–Soper–Sterman 1988 (`CollinsSoperSterman1988`).
- (b) **All-order region analysis.** Overlapping soft/collinear/Glauber regions, Glauber subtractions, and multiple simultaneous active–spectator and spectator–spectator exchanges: Bodwin 1985 (`Bodwin1985`), CSS 1985 (`CollinsSoperSterman1985b`), and the textbook treatment of Collins 2011 (`Collins2011`), Ch. 14.
- (c) **Power corrections.** The issue raised by Bodwin–Brodsky–Lepage 1981 (`BodwinBrodskyLepage1981`).
- (d) **Validity of the eikonal approximation for the spectators** beyond leading power.
- (e) **Observables with measured hadrons,** where the corresponding cancellations fail: TMD factorization breaking, Collins–Qiu 2007, Rogers–Mulders 2010 (`CollinsQiu2007`, `RogersMulders2010`); related phases with initial-state partons, Aybat–Sterman 2009 (`AybatSterman2009`); the SCET Glauber operator framework, Rothstein–Stewart 2016 (`RothsteinStewart2016`); Glauber gluons and MPI, Gaunt 2014 (`Gaunt2014`).
- The one-loop DY cancellation is the subject of CSS 1983 (`CollinsSoperSterman1983`). I have not compared my toy computation line by line with that paper.

**Suggested rigor tags:**
- toy-model statements 1–4: **[P]** (proved in a model and at one loop);
- leading-power DY collinear factorization including the Glauber cancellation: **[A]**, consistent with OUTLINE v0.

---------------------------------------------------------------------------------------------------------------

## 8. Cross-check summary (PASS/FAIL)

| # | check | source / conversion | result |
|---|---|---|---|
| 1 | lepton tensor $\int d\Phi_2L=(qq-q^2g)/6\pi$ | exact + MC | PASS |
| 2 | $\sigma(q\bar q\to\ell\ell)=4\pi\alpha^2e_q^2/(3N_c\hat s)$, $1+\cos^2\theta$ | explicit spinors; standard textbook result | PASS |
| 3 | LO $d\sigma/dQ^2$ (task formula), every factor | derivation + numerics | PASS |
| 4 | LO $d^2\sigma/dQ^2dy$, Jacobian 1 | symbolic + numerics | PASS |
| 5 | $T_{q\bar q}$, $T_{qg}$ (D dims), crossing | trace engine; physical polarizations at $D=4$ | PASS |
| 6 | D-dim phase space | exact/numeric | PASS |
| 7 | real closed forms | gammasimp identity | PASS |
| 8 | one-loop form factor | MVV JHEP08(2005)049, through $\varepsilon^4$ | PASS |
| 9 | soft $1/\varepsilon^2$ cancels; remaining pole $=-\frac2\varepsilon P_{qq}$ | exact | PASS |
| 10 | $\overline{\rm MS}$ removes all poles; $\mu_R$-independence | exact | PASS |
| 11 | $\Delta_{q\bar q}$ = task formula (each term) | exact | PASS |
| 12 | $\Delta_{qg}$ = task formula (each term, $T_F$) | exact | PASS |
| 13 | $\Delta_{q\bar q}$, $\Delta_{qg}$ incl. $\mu_F$ terms | DDM JHEP11(2020)143 ancillary; $\times2$ for $\alpha_s/\pi\to\alpha_s/2\pi$ | PASS, PASS |
| 14 | threshold constant $g_{01}^{\rm DY}$ | Moch–Vogt PLB631(2005)48; $a_s=\alpha_s/4\pi$, $\ln N$ | PASS |
| 15 | DIS-scheme forms | c_dis $C_2^{q,g}$; commonly quoted AEM forms (original not consulted) | PASS (orig. unverified) |
| 16 | $\mu_F$ independence | Mellin exact; $x$-space numeric $10^{-13}$ | PASS |
| 17 | Glauber G1–G5 (25 checks) | internal | PASS |

---------------------------------------------------------------------------------------------------------------

## 9. Notes for the lead author (possible discrepancies / pitfalls)
1. **Plus-prescription placement** (§3.10.1). Formulas like "$4(1+z^2)(\ln(1-z)/(1-z))_+$" must be read with $(1+z^2)$ *outside* the plus prescription. Otherwise the $\delta$ coefficient changes by $7C_F$. The monograph should state this once, next to the CONTEXT definition of $[\,]_+$.
2. **Gluon polarization average** $1/(D-2)$ is part of the $\overline{\rm MS}$ definition used here (and in c_dis). It should be stated with the coefficient functions.
3. **CONTEXT/OUTLINE.** I found no error in the binding conventions relevant to Drell–Yan.
   - The rapidity definition $y=\frac12\ln(k^+/k^-)$, the light-front conventions, the PDF definition and the DGLAP/plus conventions are all used as given, and lead to the standard results.
   - OUTLINE Ch. 10's "soft factor = 1 for inclusive" is correct for the $q_T$-integrated cross section (unitarity of Wilson lines at coincident transverse positions). It does **not** hold for $q_T$-differential spectra; that is Ch. 11's business.
4. **The task's formulas** are confirmed as written. The attribution of the $\overline{\rm MS}$ form to AEM 1979 should be phrased carefully, because AEM worked in the DIS scheme; the $\overline{\rm MS}$ form appears in later literature (e.g. ESW).

---------------------------------------------------------------------------------------------------------------

## 10. Files and reproduction
| file | content |
|---|---|
| `dtrace.py` | D-dimensional Dirac trace engine + self-tests (`logs/dtrace_selftest.log`) |
| `lo_check.py` | LO checks (A)–(D) (`logs/lo_check.log`) |
| `dy_core.py` | matrix elements, phase space, exact real/virtual, distribution algebra |
| `nlo_checks.py` | full NLO pipeline + literature checks (`logs/nlo_checks.log`, `results_nlo.tex`); ~4 min |
| `me_numeric.py` | explicit-spinor/physical-polarization check (`logs/me_numeric.log`) |
| `expansions_print.py` | Laurent expansions of the pieces (`logs/expansions_print.log`) |
| `plus_trap.py` | plus-prescription trap, $\pi^2$ bookkeeping (`logs/plus_trap.log`) |
| `moments_exact.py` | Mellin moments $N=1,2$ against closed forms, 40 digits (`logs/moments_exact.log`) |
| `scale_check.py` | $\mu_F$ independence (`logs/scale_check.log`) |
| `glauber_toy.py` | Glauber toy model G1–G5 (`logs/glauber_toy.log`) |
| `dy_oneloop.tex` | LaTeX section (Chinese) for Ch. 10 / App. G, with TikZ diagrams; `test_build.tex` → `test_build.pdf` |
