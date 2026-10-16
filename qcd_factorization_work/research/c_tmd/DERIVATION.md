# TMD factorization ingredients — derivations and checks (agent `c_tmd`)

Directory: `/Users/hao-cheng/Desktop/theorem proof/qcd_factorization_work/research/c_tmd`
(`scripts/` = sympy/numpy/mpmath verification scripts, `logs/` = their output, `tex/` = LaTeX snippets for the monograph,
compiled by `tex/test_build.tex`).  Every formula below was derived here and checked by a script; the script name is given
in brackets.  Literature values were checked against the **source text of the papers** (arXiv LaTeX sources downloaded
in this session) unless explicitly marked *recalled, not verified*.

---------------------------------------------------------------------------------------------------------------------

## 0. Summary of results and checks

Notation: $a\equiv \alpha_sC_F/(2\pi)$, $L_b\equiv\ln(\mu^2b_T^2/b_0^2)$, $b_0=2e^{-\gamma_E}$, $l_\zeta\equiv\ln(\zeta/\mu^2)$,
$p(x)\equiv(1+x^2)\big[\tfrac1{1-x}\big]_+$, so that $P_{qq}=C_F[p(x)+\tfrac32\delta(1-x)]$.
"binding" = $\overline{\rm MS}$ with $S_\epsilon=(4\pi)^\epsilon e^{-\epsilon\gamma_E}$ (CONTEXT.md); "Collins" =
$S_\epsilon=(4\pi)^\epsilon/\Gamma(1-\epsilon)$ (Collins 2011, Sec. 3.3.2, as quoted in Collins–Rogers 2013).

| # | Result (one loop unless stated) | Check | Literature | Status |
|---|---|---|---|---|
| R1 | real graphs of the unsubtracted TMD with Wilson line $n_B(y_B)$: $F_a=(1-\epsilon)(1-x)$, $F_b=\frac{2x(1-x)}{(1-x)^2+s\delta^2}$, $F_c=-\frac{2s\delta^2(1-x)}{((1-x)^2+s\delta^2)^2}$, $\delta^2=\frac{e^{2y_B}k_T^2}{2(p^+)^2}$ | exact $D$-dim traces [`real_graphs.py`] | — | PASS |
| R2 | rapidity regulator: $F_b\to 2x[\frac1{1-x}]_++\delta(1-x)\ln\frac1{\delta^2}$; $F_c^{\rm time}\to-\delta(1-x)$ | analytic + numeric [`one_loop_tmd.py`,`rapidity_checks.py`] | — | PASS |
| R3 | virtual vertex with non-light-like line $\propto(\mu^2|n^2|/(p\cdot n)^2)^\epsilon$, closed form; $\to0$ in light-like limit taken first | Beta-function reps, numerics [`virtual_vertex.py`] | order of limits: Collins–Rogers 2013 (citing Collins 2011 §10.8, §10.11.1) | PASS |
| R3' | space-like lines: $V^{\rm SIDIS}=(V^{\rm DY})^*$ exactly; time-like: $\mathrm{Re}V^{\rm DY}-V^{\rm SIDIS}\to2\pi^2\frac{\alpha_sC_F}{4\pi}$ | [`virtual_vertex.py`] | consistent with space-like choice of Collins 2011, Aybat–Rogers 2011 (citing Collins–Metz 2004) | PASS (new illustration) |
| R4 | soft factor: $\tilde S^{(1)}=\frac{\alpha_sC_F}{\pi}S_\epsilon(Y\coth Y-\sigma)A(\epsilon)$, renormalized $-\frac{\alpha_sC_F}\pi(Y\coth Y-\sigma)L_b$ | rapidity integrals analytic+numeric [`soft_factor.py`] | cusp $\frac{\alpha_sC_F}\pi(Y\coth Y-1)$: Polyakov 1980, Korchemsky–Radyushkin 1987 (standard) | PASS |
| R5 | Collins TMD, $k_T\neq0$: $f^{(1)}=\frac{c_S}{k_T^2}\big[p(x)-\epsilon(1-x)+\delta(1-x)\ln\frac{\zeta}{k_T^2}\big]$, $\zeta=2(xp^+)^2e^{-2y_n}$ | [`one_loop_tmd.py`] | $\zeta$: Collins–Rogers 2013 eq. (zeta.A) | PASS |
| R6 | UV counterterm $Z_FZ_2-1=aS_\epsilon[-\frac1{\epsilon^2}+\frac{l_\zeta-3/2}\epsilon]$ | [`one_loop_tmd.py`,`collins_tmd.py`] | — | PASS |
| R7 | $\tilde K=-\frac{\alpha_sC_F}\pi L_b$, $\gamma_K=\frac{2\alpha_sC_F}\pi$, $\gamma_F=\frac{\alpha_sC_F}\pi(\frac32-l_\zeta)$; $\tilde K$ also from soft factor alone | [`one_loop_tmd.py`,`soft_factor.py`] | Aybat–Rogers 2011 (B1)–(B3); EIS 2012 eq. (g_collins) | PASS |
| R8 | $\tilde C_{q/q}=\delta+a\{-L_bp(x)+(1-x)+\delta(1-x)[-\frac{L_b^2}2-L_bl_\zeta-\kappa\frac{\pi^2}{12}]\}$, $\kappa=1$ (binding), $0$ (Collins); $\tilde C_{q/g}=\frac{\alpha_sT_F}{2\pi}\{-L_b[x^2+(1-x)^2]+2x(1-x)\}$ | [`one_loop_tmd.py`,`quark_in_gluon.py`] | Aybat–Rogers 2011 (A10),(A11) [Collins $S_\epsilon$]; EIS 2012 matching coeff. [std $S_\epsilon$] | PASS |
| R9 | $\delta$-regulator gives the same TMD with $\zeta=2(p^+)^2\delta^-/\delta^+$ | [`delta_regulator.py`] | Collins–Rogers 2013 eq. (zetaA) | PASS |
| R10 | $H_{\rm DY}=1+a[-L^2+3L-8+\frac{7\pi^2}6]$ (binding), $1+a[-L^2+3L-8+\pi^2]$ (Collins); $H_{\rm SIDIS}$: $\frac{\pi^2}6$ resp. $0$ | independent form factor [`form_factor.py`] | EIS 2012 §7; Aybat–Rogers arXiv:1107.3973; CR13 "factor 7/6" | PASS |
| R11 | CSS: $A^{(1)}=C_F$, $B^{(1)}=-\frac32C_F$, $C^{(1)}_{qq}=\frac{C_F}2(1-z)+C_F(\frac{\pi^2}4-2)\delta(1-z)$, $C^{(1)}_{qg}=T_Fz(1-z)$ (units $\alpha_s/\pi$); $O(\alpha_s)$ expansion = fixed-order small-$q_T$ limit | symbolic [`css_expansion.py`], numeric vs exact matrix elements [`dy_qt_check.py`,`dy_qt_check2.py`] | Balázs–Yuan 1997 App. (citing CSS 1985, Davies–Stirling 1984) | PASS |
| R12 | $f_{1T}^{\perp\,\rm SIDIS}=-f_{1T}^{\perp\,\rm DY}$ (PT + hermiticity + translation); $b$-space form; spectator model $f_{1T}^{\perp\,\rm SIDIS}=\frac{g^2e_qe_s}{4(2\pi)^4}\frac{M(m+xM)(1-x)}{k_T^2(k_T^2+L^2)}\ln\frac{k_T^2+L^2}{L^2}<0$ (attractive) | Dirac identities, spinors [`sivers_symmetry.py`], model numerics [`sivers_spectator.py`] | Collins 2002; Trento conventions 2004; Bacchetta–Conti–Radici 2008 eq. (SivBM2-s-pl) | PASS |

All checks in the 17 verification scripts pass (`scripts/run_all.sh`; logs in `logs/`, none contains FAIL).

---------------------------------------------------------------------------------------------------------------------

## 1. Conventions

**Binding (CONTEXT.md).** Metric $(+,-,-,-)$; $v^\pm=(v^0\pm v^3)/\sqrt2$, $v\cdot w=v^+w^-+v^-w^+-\boldsymbol v_T\cdot\boldsymbol w_T$;
hadron A along $+z$; rapidity $y=\frac12\ln(k^+/k^-)$. $D_\mu=\partial_\mu-igA_\mu^at^a$, quark–gluon vertex $ig\gamma^\mu t^a$.
$W[b,a]=P\exp\!\big(ig\int_a^b dz^\mu A_\mu^a t^a\big)$ (points closer to $b$ to the left), $W\to U(b)WU^\dagger(a)$.
$D=4-2\epsilon$; $\overline{\rm MS}$ with $S_\epsilon=(4\pi)^\epsilon e^{-\epsilon\gamma_E}$, i.e. $g_0^2=4\pi\alpha_s\mu^{2\epsilon}S_\epsilon^{-1}$.
Collinear PDF $f_{q/H}(\xi)=\int\frac{dw^-}{4\pi}e^{-i\xi P^+w^-}\langle P|\bar\psi(w)\gamma^+W[w,0]\psi(0)|P\rangle$.
TMD Fourier convention $\tilde f(x,\boldsymbol b_T)=\int d^{2-2\epsilon}k_T\,e^{-i\boldsymbol k_T\cdot\boldsymbol b_T}f(x,\boldsymbol k_T)$, $\mu_b=b_0/b_T$.

**Additional conventions used here (proposed for Ch. 11).**

1. *Direction vectors.* $n\equiv(0,1,\boldsymbol 0_T)$ ($n\cdot k=k^+$), $\bar n\equiv(1,0,\boldsymbol 0_T)$.  Non-light-like regulators
   (Collins 2011; Aybat–Rogers 2011 eq. (8)): space-like $n_A(y_A)=(1,-e^{-2y_A},\boldsymbol 0_T)$, $n_B(y_B)=(-e^{2y_B},1,\boldsymbol0_T)$;
   the time-like variants $(1,e^{-2y_A},\boldsymbol0_T)$, $(e^{2y_B},1,\boldsymbol0_T)$ are used for cross-checks only.
   A vector $v$ has rapidity $\frac12\ln|v^+/v^-|$; $y_B\to-\infty$ makes $n_B\to n$.
2. *Eikonal Feynman rules* (blueprint §0.4(10), momentum $k$ flowing **into** the line): future-pointing $W[\infty n,0]$:
   $(ign^\mu t^a)\frac{-i}{n\cdot k-i0}$; past-pointing $W[0,-\infty n]$: $(ign^\mu t^a)\frac{i}{n\cdot k+i0}$; hermitian-conjugate lines
   get the conjugate rules.  For the TMD the line multiplying $\psi(0)$ is $W[\infty n,0]$ (SIDIS) or
   $W[-\infty n,0]=W[0,-\infty n]^\dagger$ (DY), giving $\frac{g n^\mu t^a}{n\cdot k\mp i0}$ for $k$ into the line.
3. *Two $\overline{\rm MS}$ conventions.* binding $S_\epsilon=(4\pi)^\epsilon e^{-\epsilon\gamma_E}$; Collins $S_\epsilon=(4\pi)^\epsilon/\Gamma(1-\epsilon)$.
   They differ at $O(\epsilon^2)$: $\frac{(4\pi)^\epsilon/\Gamma(1-\epsilon)}{(4\pi)^\epsilon e^{-\epsilon\gamma_E}}=1-\frac{\pi^2}{12}\epsilon^2+O(\epsilon^3)$.
   This matters only for quantities with $1/\epsilon^2$ UV poles per loop (TMDs, hard factors), see §4.3.
4. *Rapidity scale.* $\zeta_A=M_A^2x_A^2e^{2(y_P-y_n)}=2(x_AP_A^+)^2e^{-2y_n}$, $\zeta_B=2(x_BP_B^-)^2e^{2y_n}$,
   $\zeta_A\zeta_B=(2x_Ax_BP_A^+P_B^-)^2=Q^4$ at leading power (Collins–Rogers 2013 eqs. (zeta.A),(zeta.B); EIS 2012 eq. (g_collins)
   quotes Collins' $\gamma_F$ with $2(p^+)^2e^{-2y_n}$, consistent).  **Caveat:** Aybat–Rogers 2011 eq. (3) prints
   $\zeta_F=2M_p^2x^2e^{2(y_P-y_s)}$ (checked in the arXiv source); since $M^2e^{2y_P}=2(P^+)^2$ this is twice the above and
   contradicts their own $\sqrt{\zeta_F\zeta_D}\approx Q^2$; their one-loop results (A10),(A11),(B1) agree with ours only for
   $\zeta=2(xP^+)^2e^{-2y_n}$.  We regard the factor 2 in their eq. (3) as a misprint.
5. *$\overline{\rm MS}$ bookkeeping and abbreviations.* We use Collins' bookkeeping: bare coupling $g_0^2=4\pi\alpha_s\mu^{2\epsilon}$ (to the order
   needed) and $\overline{\rm MS}$ counterterms of the form $S_\epsilon\times$(pure poles).  This is equivalent to CONTEXT's
   "$\mu^2\to\mu^2e^{\gamma_E}/4\pi$" ($g_0^2=4\pi\alpha_s\mu^{2\epsilon}S_\epsilon^{-1}$, counterterms $=$ pure poles): a bare one-loop quantity is
   $aS_\epsilon X(\epsilon)$ in the first and $aX(\epsilon)$ in the second bookkeeping with the **same** Laurent series $X$, so the renormalized
   results coincide.  $a=\alpha_sC_F/(2\pi)$; $c_S\equiv4\pi\alpha_s\mu^{2\epsilon}C_F/(2\pi)^{3-2\epsilon}$, so that $c_S\,{\rm FT}[1/k_T^2]=aS_\epsilon A(\epsilon)$ (§3.7);
   $L_b$, $l_\zeta$, $p(x)$ as in §0. Useful identities:
   $p(x)=2[\frac1{1-x}]_+-1-x=(1-x)+2x[\frac1{1-x}]_+$, $\;[\frac{1+x^2}{1-x}]_+=p(x)+\frac32\delta(1-x)$.

---------------------------------------------------------------------------------------------------------------------

## 2. Definitions

### 2.1 Staple Wilson lines and the unsubtracted TMD

For $w=(0^+,w^-,\boldsymbol b_T)$ define the future- (SIDIS, $[+]$) and past-pointing (DY, $[-]$) staples from $0$ to $w$:
$$
\mathcal W^{[\pm]}(w,0;n)=W[w,\,w\pm\infty n]\;W[w\pm\infty n,\,\pm\infty n]\;W[\pm\infty n,\,0],
$$
where the middle factor is the **transverse link** at light-front time $w^-=\pm\infty$, running in the transverse plane from
$\boldsymbol 0_T$ to $\boldsymbol b_T$.  Since each segment transforms as $U(\text{end})\,W\,U^\dagger(\text{start})$,
$$
\mathcal W^{[\pm]}\to U(w)\,\mathcal W^{[\pm]}\,U^\dagger(0)\qquad\text{for all gauge transformations, including those not trivial at infinity.}
$$
The unsubtracted TMD (Collins 2011; Aybat–Rogers 2011 eq. (11), there with $\psi(w/2)\dots\psi(-w/2)$, equivalent by
translation invariance) is
$$
\tilde f^{[\pm]\,\rm unsub}_{q/H}(x,\boldsymbol b_T;y_P-y_B)=\int\frac{dw^-}{4\pi}e^{-ixP^+w^-}
\langle P,S|\bar\psi(w)\gamma^+\mathcal W^{[\pm]}(w,0;n_B)\psi(0)|P,S\rangle_{c,\ \text{no S.I.}},
$$
colour summed, with non-light-like $n_B$; "no S.I." (no Wilson-line self-interactions) as in Aybat–Rogers eqs. (soft),(11): the
self-energies of space-like lines are badly (linearly) divergent; they cancel in the final definition (§3.6 shows this explicitly
with time-like lines, where they are finite).  Momentum space: $f(x,\boldsymbol k_T)=\int\frac{d^{2-2\epsilon}b_T}{(2\pi)^{2-2\epsilon}}e^{i\boldsymbol k_T\cdot\boldsymbol b_T}\tilde f(x,\boldsymbol b_T)$
(Aybat–Rogers eq. (27) at $\epsilon=0$).  With $\boldsymbol b_T=0$ and a light-like line, $\tilde f$ reduces to the collinear PDF of CONTEXT.md.

**Role of the transverse link (Ji–Yuan 2002; Belitsky–Ji–Yuan 2003).**
(i) In covariant (non-singular) gauges the gauge potential vanishes at light-cone infinity and the transverse link equals 1; it
can be omitted (Aybat–Rogers 2011, remark after eq. (soft)).
(ii) In light-cone gauge $n\cdot A=A^+=0$ the longitudinal segments are unity, but $\boldsymbol A_T(w^-\to\pm\infty,\boldsymbol x_T)$
need not vanish: with $A^+=0$, $F^{+\perp}=\partial^+A^\perp$, so with $A(x)=\int e^{-il\cdot x}\tilde A(l)$,
$\tilde A^\perp=i\tilde F^{+\perp}/[l^+]$ and the prescription $[1/l^+]$ is a boundary condition:
$\boldsymbol A_T(+\infty^-)=0\iff[1/l^+]=1/(l^+-i0)$ and $\boldsymbol A_T(-\infty^-)=0\iff[1/l^+]=1/(l^++i0)$ (close the $l^+$ contour
in the lower/upper half plane).  For SIDIS with $1/(l^+-i0)$ the link is trivial and the final-state-interaction phase sits in the
gauge term of the propagator with exactly the eikonal prescription of the Feynman-gauge Wilson line; with the PV prescription
the propagator is "real" and the whole phase is carried by the transverse link.  This is the content of Ji–Yuan 2002 (the BHS
asymmetry is reproduced in light-cone gauge either by a prescription consistent with the gauge link, or by a link involving the
potential at infinity) and BJY 2003 (transverse links at light-cone infinity are needed for gauge invariance in light-cone gauge).
*(Statement of these two papers checked against their arXiv abstracts; the boundary-condition/prescription correspondence is
derived above.)*

**Rapidity (light-cone) divergence.** With a light-like line the real graph $F_b$ of §3.2 becomes $2x/(1-x)$ at fixed $k_T$: the
$x\to1$ region (gluon rapidity $\to-\infty$ at fixed $k_T$) is not integrable and is **not** regulated by dimensional
regularization, which acts on transverse integrals.  $n_B(y_B)$ cuts it off at $1-x\sim\delta\propto k_Te^{y_B}/p^+$.

### 2.2 Soft factor
In the conventions of Collins (Aybat–Rogers 2011 eq. (soft)):
$$
\tilde S(\boldsymbol b_T;y_A,y_B)=\frac1{N_c}\langle0|W(\tfrac{\boldsymbol b_T}2,\infty;n_B)^\dagger_{ca}W(\tfrac{\boldsymbol b_T}2,\infty;n_A)_{ad}
W(-\tfrac{\boldsymbol b_T}2,\infty;n_B)_{bc}W(-\tfrac{\boldsymbol b_T}2,\infty;n_A)^\dagger_{db}|0\rangle_{\text{no S.I.}},
$$
with $W(x,\infty;n)$ the line from $x$ to $x+\infty n$ (Collins writes $P\exp(-ig_0\int_0^\infty ds\,n\cdot A)$ because his $g$ has the
opposite sign; physically the same parallel transporter as our $W[x+\infty n,x]$).  Properties used: boost invariance
($\tilde S$ depends on $y_A-y_B$ only) and $\tilde S(\boldsymbol b_T=0)=1$ (unitarity: the indices reduce to
$N_c^{-1}{\rm Tr}[W_B^\dagger W_AW_A^\dagger W_B]=1$).

### 2.3 Collins' definition (D11.5)
$$
\boxed{\tilde f_{q/H}(x,\boldsymbol b_T;\mu,\zeta)=\lim_{\substack{y_A\to+\infty\\y_B\to-\infty}}
\tilde f^{\rm unsub}_{q/H}(x,\boldsymbol b_T;y_P-y_B)\,
\sqrt{\frac{\tilde S(\boldsymbol b_T;y_A,y_n)}{\tilde S(\boldsymbol b_T;y_A,y_B)\,\tilde S(\boldsymbol b_T;y_n,y_B)}}\;Z_FZ_2,\qquad
\zeta=2(xP^+)^2e^{-2y_n}}
$$
(Aybat–Rogers 2011 eq. (12) [their $y_s\equiv y_n$]; Collins–Rogers 2013 eq. (A.JCC.def), who cite Collins 2011 eqs. (13.106),
(14.31)).  **Order of limits** (Collins–Rogers 2013 §3, citing Collins 2011 §10.8 and §10.11.1): first the light-like limit at fixed
$\epsilon$, then $\overline{\rm MS}$ renormalization, then $\epsilon\to0$.  §3.4 shows explicitly why this order matters.

### 2.4 $\delta$-regulator (EIS 2012, as formalized by Collins–Rogers 2013)
Light-like Wilson-line propagators $\frac{i}{-k^++i\delta^+}$, $\frac{i}{k^-+i\delta^-}$ and
$\tilde f^{\rm EIS}=\lim_{\delta^\pm\to0}\tilde f_0(\delta^+)/\sqrt{\tilde S_0(\delta^-,\delta^+)}\times$UV renormalization, with
$\delta^+/\delta^-$ fixed.  Collins–Rogers 2013 prove equality with Collins' TMD for $\zeta_A=2(k_A^+)^2\delta^-/\delta^+$, i.e.
$y_n=\ln\sqrt{\delta^+/\delta^-}$ (their eqs. (zetaA),(zetaB)), up to the $\overline{\rm MS}$ convention.

---------------------------------------------------------------------------------------------------------------------

## 3. One-loop TMD of a quark in a quark

### 3.1 Set-up
Target: on-shell massless quark $p=(p^+,0,\boldsymbol0_T)$, spin and colour averaged; tree level $f^{(0)}=\delta(1-x)\delta^{(2-2\epsilon)}(\boldsymbol k_T)$,
$\tilde f^{(0)}=\delta(1-x)$.  Inserting a one-gluon final state $l=p-k$ ($l^+=(1-x)p^+$, $\boldsymbol l_T=-\boldsymbol k_T$,
$l^-=k_T^2/2l^+$) in the definition gives exactly
$$
f^{\rm real}(x,\boldsymbol k_T)=\frac{1}{4(2\pi)^{D-1}l^+}\;\frac12\sum_{\rm spins}\sum_{\rm pol}\overline{\mathcal M}\gamma^+\mathcal M
\equiv\frac{c_S}{k_T^2}\,F(x,\ldots),
$$
($\int dw^-e^{-ixp^+w^-}e^{i(p^+-l^+)w^-}=2\pi\delta(l^+-(1-x)p^+)$, light-front phase space $dl^+d^{D-2}l_T/((2\pi)^{D-1}2l^+)$.)
The cut amplitude for SIDIS (future-pointing line, outgoing gluon $l$) is
$$
\mathcal M^\mu=-g\,t^a\Big[\frac{\slashed k\gamma^\mu}{k^2+i0}+\frac{n_B^\mu}{n_B\cdot l+i0}\Big]u(p),
$$
(DY: $n_B\cdot l-i0$).  It satisfies the Ward identity $l_\mu\mathcal M^\mu=0$ ($\slashed k\slashed l u=-k^2u$), so
$\sum_{\rm pol}\to-g_{\mu\nu}$.  The colour factor is $C_F$.

### 3.2 Real graphs (R1) [`real_graphs.py`]
With $n_B=(se^{2y_B},1,\boldsymbol0_T)$ ($s=+1$ time-like, $s=-1$ space-like/Collins) and $\delta^2\equiv e^{2y_B}k_T^2/(2(p^+)^2)$
(so $n_B\cdot l=\frac{p^+}{1-x}[(1-x)^2+s\delta^2]$):
$$
F_a=(1-\epsilon)(1-x),\qquad F_b=\frac{2x(1-x)}{(1-x)^2+s\delta^2},\qquad F_c=-\frac{2s\,\delta^2(1-x)}{\big((1-x)^2+s\delta^2\big)^2},
$$
for the quark–quark ($a$), interference ($b$, both orderings) and Wilson–Wilson ($c$) cuts.  For space-like lines the
interference is the principal value ($\frac1{n\cdot l+i0}+\frac1{n\cdot l-i0}=2{\rm PV}\frac1{n\cdot l}$), so SIDIS and DY agree
for $f_1$ at this order; $F_c$ is the Wilson-line self-energy ("S.I."); it is non-integrable for $s=-1$ and finite for $s=+1$.

### 3.3 Rapidity-regulator limit (R2) [`one_loop_tmd.py`, `rapidity_checks.py`]
With $u=1-x$:
$\int_0^1\!dx\,F_b^{(s=+1)}=\ln(1+\delta^{-2})+2\delta\arctan\frac1\delta-2=-2-2\ln\delta+\pi\delta+O(\delta^2)$;
${\rm PV}\!\int_0^1\!dx\,F_b^{(s=-1)}=\ln(1-\delta^2)-\ln\delta^2-2-\delta\ln\frac{1-\delta}{1+\delta}$.
Since $\langle 2x[\frac1{1-x}]_+,h\rangle=\int_0^1\frac{2x(h(x)-h(1))}{1-x}dx-2h(1)$, for any test function $h$
$$
F_b\;\xrightarrow{\delta\to0}\;2x\Big[\frac1{1-x}\Big]_++\delta(1-x)\ln\frac1{\delta^2},\qquad
F_c^{(s=+1)}\to-\delta(1-x)\quad\big(\textstyle\int_0^1F_c=-\frac1{1+\delta^2}\big),
$$
with $O(\delta)$ corrections, uniformly for $k_T\to0$ (where $\delta\to0$ faster).  Numerically checked to $O(\delta)$ ($O(\delta^2)$ for PV).
Hence, for $k_T\ne0$,
$$
f^{\rm unsub\,(1)}(x,\boldsymbol k_T;y_B)=\frac{c_S}{k_T^2}\Big\{p(x)-\epsilon(1-x)+\delta(1-x)\Big[\ln\frac{2(p^+)^2e^{-2y_B}}{k_T^2}-\sigma\Big]\Big\},
$$
$\sigma=1$ (time-like, self-energy included) or $\sigma=0$ (space-like, "no S.I.").  The $-2y_B$ is the rapidity divergence.

### 3.4 Virtual graphs (R3, R3') [`virtual_vertex.py`]
(a) Quark self-energy on the on-shell massless leg: scaleless, $=0$ in DR.  (b) Wilson-line self-energy: scaleless (no scale at all),
$=0$.  (c) Soft-factor virtual graphs: depend only on dimensionless $n_A,n_B$: scaleless, $=0$.
(d) **Vertex graph** (gluon between the quark line and the Wilson line, same side of the cut):
$$
V=ig^2C_F\mu^{2\epsilon}\!\int\!\frac{d^Dl}{(2\pi)^D}\frac{N(l)}{(n\cdot l\mp i0)(l^2+i0)((p-l)^2+i0)},\quad
N=\frac{\bar u\gamma^+(\slashed p-\slashed l)\slashed nu}{\bar u\gamma^+u}=2p\cdot n-2n\cdot l+\frac{\bar u\gamma^+\slashed n\slashed lu}{\bar u\gamma^+u}.
$$
By Lorentz invariance, dimensional analysis and homogeneity in $n$: $V=c(\epsilon)\,(\mu^2n^2/(p\cdot n)^2)^\epsilon$ — **not** scaleless for
$n^2\ne0$.  Feynman parameter $x$ for the two quadratic propagators, Schwinger parameter $\lambda$ for the linear one,
$l=l'+xp\pm\lambda n/2$; then $N\to2(1-x)p\cdot n\mp\lambda n^2/2$ (checked with $D$-dimensional traces) and for time-like
$n$, SIDIS ($\Delta=x\lambda p\cdot n+\lambda^2n^2/4>0$; substitute $\lambda=4xp\cdot n\,t/n^2$):
$$
V_{\rm SIDIS}^{\rm time}=-\frac{\alpha_sC_F}{4\pi}\Big(\frac{\pi\mu^2n^2}{(p\cdot n)^2}\Big)^{\!\epsilon}2\Gamma(1+\epsilon)\Big[B(-2\epsilon,2)B(-\epsilon,1+2\epsilon)-\frac{B(1-\epsilon,2\epsilon)}{1-2\epsilon}\Big]
=-\frac{\alpha_sC_F}{4\pi}\Big(\frac{\pi\mu^2n^2}{(p\cdot n)^2}\Big)^{\!\epsilon}\frac{\Gamma(1-\epsilon)\Gamma(1+2\epsilon)(1-\epsilon)}{(1-2\epsilon)\epsilon^2}.
$$
For $n=n_B$: $\frac{4(p\cdot n)^2}{n^2}=2(p^+)^2e^{-2y_B}\equiv\Lambda_B^2$ and, in binding $\overline{\rm MS}$,
$V=-\frac{\alpha_sC_F}{4\pi}S_\epsilon\big[\frac1{\epsilon^2}+\frac{1-\ell}{\epsilon}+2+\frac{5\pi^2}{12}-\ell+\frac{\ell^2}2+O(\epsilon)\big]$, $\ell=\ln\frac{\Lambda_B^2}{\mu^2}$.
Its UV pole (large-$l$ power counting: $-2n\cdot l$ and $\langle l^\mu/n\cdot l\rangle\to n^\mu/n^2$ give $(-2+1)\int d^Dl/l^4$) is
$+\frac{\alpha_sC_F}{4\pi\epsilon}$, independent of $n$; the $\ell$-dependent poles are IR.

*Light-like limit.* $|(\mu^2/\Lambda_B^2)^\epsilon|\to0$ as $y_B\to-\infty$ for ${\rm Re}\,\epsilon>0$; the limit taken **first** (Collins'
prescription) therefore sets $V\to0$, and the result continues analytically to all $\epsilon$.  If one expanded in $\epsilon$
first, $\ell^2/2$ terms would survive: the limits do not commute (Collins–Rogers 2013, citing Collins 2011 §10.8, §10.11.1).
In the same limit the real-graph corrections of §3.3, which live at $k_T\gtrsim\Lambda_B$, vanish at fixed $b_T$: for the $\delta(1-x)$
part the exact-minus-limit remainder is $D(\kappa)=\ln(1+\kappa^2)+2\kappa\arctan(1/\kappa)$, $\kappa=k_T/\Lambda_B$, and its 2D Fourier
transform $2\pi\int_0^\infty\frac{d\kappa}{\kappa}J_0(\kappa\Lambda_Bb_T)D(\kappa)$ equals $2\pi^2/(\Lambda_Bb_T)$ (numerically, to 8 digits, for
$\Lambda_Bb_T=20,200,2000$ [`one_loop_tmd.py`, item 7]).  Hence **only the real graphs and the real soft graphs contribute**
to the bare Collins TMD in pure DR; the UV poles appear as $k_T\to0$ poles of these graphs (the scaleless virtual graphs equal
"UV $-$ IR" and are zero).

*Future vs past pointing, time-like vs space-like (new one-loop illustration).* For the past-pointing (DY) line,
$\Delta=-x\lambda p\cdot n+\lambda^2n^2/4$ changes sign and Beta functions with phases $e^{i\pi(1+\epsilon)}$ appear (formulas in the
script header).  Numerically (and to $O(\epsilon^0)$ analytically):
* space-like $n$ (Collins): $V_{\rm SIDIS}=(V_{\rm DY})^*$ exactly, so $2{\rm Re}V$ is the same — as required by PT invariance
  (§6.2), because for space-like paths path ordering and time ordering of the field operators coincide;
* time-like $n$: ${\rm Re}V_{\rm DY}-V_{\rm SIDIS}=\frac{\alpha_sC_F}{4\pi}\,2\pi^2+O(\epsilon)$ (times the common power): for a past-pointing
  *time-like* line the path-ordered operator is anti-time-ordered, whereas Feynman rules compute the time-ordered one; the
  difference is a Coulomb phase between the incoming quark and the incoming eikonal line.  At finite rapidity this would make even
  $f_1$ process dependent.  All these terms are $\propto(|n^2|)^\epsilon$ and vanish in the light-like limit.
This supports the use of space-like lines by Collins 2011 and Aybat–Rogers 2011 (who cite Collins–Metz 2004 for the
universality argument).  The interpretation in terms of operator ordering is mine; the numbers are in `logs/virtual_vertex.log`.

### 3.5 Soft factor at one loop (R4) [`soft_factor.py`]
Real gluon exchange between the two lines; colour-singlet current $J^\mu=gt^a[\frac{n_A^\mu}{n_A\cdot l}-\frac{n_B^\mu}{n_B\cdot l}]$,
$-J\cdot J/(g^2C_F)=\frac{2n_A\cdot n_B}{(n_A\cdot l)(n_B\cdot l)}-\frac{n_A^2}{(n_A\cdot l)^2}-\frac{n_B^2}{(n_B\cdot l)^2}$ ($\ge0$, since $J\cdot l=0$).
Phase space $\int\frac{d^Dl}{(2\pi)^{D-1}}\delta^+(l^2)=\int\frac{d^{D-2}l_T}{2(2\pi)^{D-1}}\int dy$.  With
$l=(\frac{l_T}{\sqrt2}e^y,\frac{l_T}{\sqrt2}e^{-y},\boldsymbol l_T)$ and $Y=y_A-y_B$:
* time-like: $l_T^2\frac{n_A\cdot n_B}{(n_A\cdot l)(n_B\cdot l)}=\frac{\cosh Y}{\cosh(y-y_A)\cosh(y-y_B)}$; using
  $\frac1{\cosh(y-a)\cosh(y-b)}=\frac{\tanh(y-b)-\tanh(y-a)}{\sinh(a-b)}$ and $\int_{-L}^L\tanh(y-c)dy\to-2c$:
  $\int dy=2Y\coth Y$; self-energies $-\int\frac{dy}{\cosh^2(y-y_A)}=-2$ each;
* space-like: $-\frac{\cosh Y}{\sinh(y-y_A)\sinh(y-y_B)}$, simple poles at $y=y_{A,B}$ (where $n\cdot l=0$); the real part of
  $\frac1{(n_A\cdot l\mp i0)(n_B\cdot l\pm i0)}$ is PV$\times$PV (no common zero for $Y\ne0$); with
  $\frac1{\sinh(y-a)\sinh(y-b)}=\frac{\coth(y-b)-\coth(y-a)}{\sinh(b-a)}$ and ${\rm PV}\!\int_{-L}^L\coth(y-c)\to-2c$: again $2Y\coth Y$;
  the self-energies $\propto1/\sinh^2$ are non-integrable (length divergence) and are excluded ("no S.I.").

So $\int dy\,l_T^2(-J\cdot J)/(g^2C_F)=4(Y\coth Y-\sigma)$ and
$$
\tilde S^{(1)}_{\rm bare}(b_T;y_A,y_B)=\frac{\alpha_sC_F}{\pi}S_\epsilon\,(Y\coth Y-\sigma)\,A(\epsilon),\qquad
A(\epsilon)=-\frac1\epsilon-L_b-\epsilon\Big(\frac{L_b^2}2+\frac{\pi^2}{12}\Big)+O(\epsilon^2)\ \text{(binding)},
$$
($A$ defined in §3.7; Collins $S_\epsilon$: $\pi^2/12\to\pi^2/6$).  The pole is IR from $l_T\to0$; since the virtual graphs are
scaleless ("UV$-$IR"$=0$) it is equivalently the UV pole, $-\frac{\alpha_sC_F}{\pi}\frac{Y\coth Y-1}{\epsilon}$ for $\sigma=1$, i.e. two cusps
with the one-loop cusp anomalous dimension $\frac{\alpha_sC_F}{\pi}(Y\coth Y-1)$ (Polyakov 1980; Korchemsky–Radyushkin 1987).
Pole-subtracted: $\tilde S^{(1)}=-\frac{\alpha_sC_F}\pi(Y\coth Y-\sigma)L_b$.  At large $|Y|$, $Y\coth Y\to|Y|$.

*$\tilde K$ from the soft factor alone.* $\tilde K=\frac12\frac{\partial}{\partial y_n}\ln\frac{\tilde S(b_T;y_n,-\infty)}{\tilde S(b_T;+\infty,y_n)}=-\frac{\alpha_sC_F}\pi L_b$ (renormalized), independent of $\sigma$.

### 3.6 The Collins combination in momentum space (R5)
At large rapidity gaps, $\frac12[\tilde S(y_A,y_n)-\tilde S(y_A,y_B)-\tilde S(y_n,y_B)]\to\frac{c_S}{k_T^2}\,\delta(1-x)\,[2y_B-2y_n+\sigma]$
(per unit $c_S/k_T^2$ in momentum space; $y_A$ drops out).  Adding §3.3, $y_B$ **and** the self-energy constant $\sigma$ cancel:
$$
\boxed{f^{(1)}(x,\boldsymbol k_T;\zeta)=\frac{c_S}{k_T^2}\Big[p(x)-\epsilon(1-x)+\delta(1-x)\ln\frac{\zeta}{k_T^2}\Big]+\text{(no virtual terms)},\qquad\zeta=2(p^+)^2e^{-2y_n}.}
$$
At $\epsilon=0$, $k_T>0$: $f^{(1)}=\frac{\alpha_sC_F}{2\pi^2}\frac1{k_T^2}\big[p(x)+\delta(1-x)\ln\frac{\zeta}{k_T^2}\big]$.

### 3.7 Transverse-coordinate space (R6) [`ft_check.py`, `one_loop_tmd.py`, `collins_tmd.py`]
$\int d^dk\,e^{-i\boldsymbol k\cdot\boldsymbol b}(k^2)^{-a}=\pi^{d/2}2^{d-2a}\frac{\Gamma(d/2-a)}{\Gamma(a)}(b^2)^{a-d/2}$ (checked by Hankel transform).
With $d=2-2\epsilon$, $a=1+\eta$ and $\Phi(\eta)\equiv c_S\,{\rm FT}[(k^2)^{-1-\eta}]/(aS_\epsilon)$:
$$
A(\epsilon)\equiv\Phi(0)=-\frac{e^{\epsilon L_b}e^{-\gamma_E\epsilon}\Gamma(1-\epsilon)}{\epsilon}\ \ \text{(binding)},\qquad
A^{\rm Collins}=A\cdot e^{-\gamma_E\epsilon}\Gamma(1-\epsilon);
$$
$$
B(\epsilon)\equiv\frac{c_S\,{\rm FT}[\ln(\zeta/k^2)/k^2]}{aS_\epsilon}=A(\epsilon)\Big[l_\zeta+L_b-\frac1\epsilon-\psi(1-\epsilon)-\gamma_E\Big]
=\frac1{\epsilon^2}-\frac{l_\zeta}\epsilon-\frac{L_b^2}2-L_bl_\zeta-\kappa\frac{\pi^2}{12}+O(\epsilon),
$$
($\psi(-\epsilon)=\psi(1-\epsilon)+1/\epsilon$; $\kappa=1$ binding, $0$ Collins).  The **bare Collins TMD**:
$$
\tilde f^{(1)}_{\rm bare}=aS_\epsilon\Big\{-\frac{p(x)}\epsilon-L_bp(x)+(1-x)+\delta(1-x)\Big[\frac1{\epsilon^2}-\frac{l_\zeta}\epsilon-\frac{L_b^2}2-L_bl_\zeta-\kappa\frac{\pi^2}{12}\Big]\Big\}+O(\epsilon).
$$
For comparison, the unsubtracted TMD (time-like, light-like limit not yet taken; $\Lambda_B^2=2(p^+)^2e^{-2y_B}$):
$\tilde f^{\rm unsub\,(1)}_{\rm bare}=aS_\epsilon\{[p-\epsilon(1-x)]A+\delta(1-x)[B|_{\zeta\to\Lambda_B^2}-\sigma A]\}$, whose $\delta(1-x)$ part contains
$-\ln(\Lambda_B^2/\mu^2)\,(1/\epsilon+L_b)$: divergent as $y_B\to-\infty$.

### 3.8 Renormalization, $\gamma_F$, $\tilde K$, $\gamma_K$ (R6, R7)
The IR poles of the TMD of an on-shell quark must be those of the $\overline{\rm MS}$ collinear PDF in pure DR,
$f_{q/q}=\delta(1-x)-\frac{\alpha_s}{2\pi}\frac{S_\epsilon}{\epsilon}P_{qq}(x)$, i.e. $-\frac a\epsilon[p(x)+\frac32\delta(1-x)]$ (this is what makes $\tilde C$
finite; the $x$-dependent pole $-p/\epsilon$ matches automatically — a non-trivial check).  The remaining poles are UV:
$$
\boxed{Z_FZ_2=1+aS_\epsilon\Big[-\frac1{\epsilon^2}+\frac{l_\zeta-\frac32}{\epsilon}\Big]}\qquad(\text{same in both }S_\epsilon\text{ conventions}).
$$
With $d\alpha_s/d\ln\mu=-2\epsilon\alpha_s+O(\alpha_s^2)$ and $dl_\zeta/d\ln\mu=-2$:
$$
\gamma_F(\mu;\zeta/\mu^2)=\frac{d\ln(Z_FZ_2)}{d\ln\mu}=\frac{\alpha_sC_F}{\pi}\Big(\frac32-\ln\frac{\zeta}{\mu^2}\Big),\qquad
\tilde K(b_T;\mu)=\frac{\partial\ln\tilde f}{\partial\ln\sqrt\zeta}=-\frac{\alpha_sC_F}\pi\ln\frac{\mu^2b_T^2}{b_0^2},\qquad
\gamma_K=-\frac{d\tilde K}{d\ln\mu}=\frac{2\alpha_sC_F}{\pi}.
$$
Consistency: $\partial\gamma_F/\partial\ln\sqrt\zeta=-\gamma_K$; the finiteness of $\gamma_F$ ties the $1/\epsilon^2$ to the
$l_\zeta/\epsilon$ coefficient; $\tilde K$ from the $\zeta$-derivative equals $\tilde K$ from the soft factor (§3.5); the
$\mu$-dependence of $\tilde C\otimes f$ (with DGLAP) reproduces $\gamma_F$ (§3.9); RG consistency with the independently computed
hard factor (§4).  Collins' normalizations ($\partial\ln\tilde f/\partial\ln\sqrt\zeta=\tilde K$, $d\tilde K/d\ln\mu=-\gamma_K$,
$d\ln\tilde f/d\ln\mu=\gamma_F$, $\gamma_F(\zeta/\mu^2)=\gamma_F(1)-\frac12\gamma_K\ln\frac\zeta{\mu^2}$) are exactly those of
Aybat–Rogers 2011 eqs. (18),(20)–(22), and their (B1)–(B3) are our values: **PASS**.  Also $\gamma_K=2\Gamma_{\rm cusp}$,
$\Gamma_{\rm cusp}=\alpha_sC_F/\pi$; EIS 2012's $D$ ($\partial\ln\tilde j/\partial\ln Q^2=-D$ at $\zeta=Q^2$) is $D=-\tilde K/2$.

*Remark (critic's misconception 14).* The bare TMD at $b_T=0$ (i.e. $\int d^{2-2\epsilon}k_Tf_{\rm bare}$) is scaleless in pure DR, $=$ bare
PDF; for renormalized quantities $\int d^2k_Tf\ne f$: the $k_T$-integral of the renormalized TMD is UV divergent (EIS 2012 make the
bare statement explicit in their §4).

### 3.9 Small-$b$ matching (R8) [`one_loop_tmd.py`, `quark_in_gluon.py`]
$\tilde f_{q/H}(x,b_T;\mu,\zeta)=\sum_j\int_x^1\frac{d\xi}\xi\tilde C_{q/j}(x/\xi,b_T;\mu,\zeta)f_{j/H}(\xi;\mu)+O((mb_T)^p)$, $p>0$.
Dividing the renormalized partonic TMD by the renormalized partonic PDF:
$$
\boxed{\tilde C_{q/q}=\delta(1-x)+\frac{\alpha_sC_F}{2\pi}\Big\{-L_b\,p(x)+(1-x)+\delta(1-x)\Big[-\frac{L_b^2}2-L_b\ln\frac\zeta{\mu^2}-\kappa\frac{\pi^2}{12}\Big]\Big\}+O(\alpha_s^2)}
$$
$$
\boxed{\tilde C_{q/g}=\frac{\alpha_sT_F}{2\pi}\Big\{-L_b\,[x^2+(1-x)^2]+2x(1-x)\Big\}+O(\alpha_s^2)},\qquad \tilde C_{q/\bar q},\tilde C_{q/q'}=O(\alpha_s^2).
$$
($q/g$: real graph $g\to q\bar q$, physical gluon polarizations averaged over $D-2$ states (blueprint §0.4(5)), so that the
$x$-dependence is $[x^2+(1-x)^2-\epsilon]/(1-\epsilon)$; no Wilson-line or soft contribution at this order.)
At $\mu=\mu_b$, $\zeta=\mu_b^2$:
$$
\tilde C_{q/q}=\delta(1-x)+\frac{\alpha_sC_F}{2\pi}\Big[(1-x)-\kappa\frac{\pi^2}{12}\delta(1-x)\Big],\qquad\tilde C_{q/g}=\frac{\alpha_sT_F}{2\pi}2x(1-x).
$$
**Literature.** Aybat–Rogers 2011 (A11) (Collins $S_\epsilon$, checked in source; their $2[\ln\frac2{\mu b_T}-\gamma_E]=-L_b$,
$[\frac2{(1-x)_+}-1-x]=p(x)$, $\ln(b_T^2\mu^2)-2(\ln2-\gamma_E)=L_b$) $=$ ours with $\kappa=0$; their (A10) $=$ our $\tilde C_{q/g}$: **PASS**.
EIS 2012 §4 eq. labelled `coeff` (standard $S_\epsilon$, $\zeta=Q^2$, $\mathcal P_{q/q}=[\frac{1+x^2}{1-x}]_+$, $L_T=L_b$):
$\tilde C_n=\delta+a[-\mathcal P_{q/q}L_T+(1-x)-\delta(\frac12L_T^2-\frac32L_T+L_T\ln\frac{Q^2}{\mu^2}+\frac{\pi^2}{12})]$ $=$ ours with $\kappa=1$: **PASS**.
RG check: $\frac{d}{d\ln\mu}(\tilde C\otimes f)=\gamma_F\,(\tilde C\otimes f)$ at $O(\alpha_s)$ (requires the coefficient of $L_b$ to be $-p(x)$, not $-P_{qq}/C_F$): **PASS**.

### 3.10 $\delta$-regulator cross-check (R9) [`delta_regulator.py`]
Unsubtracted: $F_b=\frac{2x(1-x)}{(1-x)^2+r^2}$, $r=\delta^+/p^+$ ($k_T$-independent, so the small-$r$ expansion is uniform),
$\to2x[\frac1{1-x}]_++\delta(1-x)\ln\frac{(p^+)^2}{(\delta^+)^2}$; $F_c\propto n^2=0$; virtual vertex scaleless (invariant under
$l^-\to\kappa l^-$, $\boldsymbol l_T\to\sqrt\kappa\boldsymbol l_T$).  Soft: rapidity integral $\to\ln\frac{l_T^2}{2\delta^+\delta^-}$ (checked); the
soft virtual graph is **not** scaleless (scale $\delta^+\delta^-$), but $\tilde S(0)=1$ gives
$\tilde S(b)=\int d^{2-2\epsilon}l\,(e^{i\boldsymbol l\cdot\boldsymbol b}-1)\rho(l)$ and replacing $\rho$ by its small-$\delta$ form costs only
$O(b^2\delta^+\delta^-)$.  Combination: $\ln\frac{(p^+)^2}{(\delta^+)^2}-\ln\frac{k_T^2}{2\delta^+\delta^-}=\ln\frac{\zeta}{k_T^2}$ with
$\zeta=2(p^+)^2\delta^-/\delta^+$ — exactly Collins–Rogers 2013 eq. (zetaA).  **PASS.**

---------------------------------------------------------------------------------------------------------------------

## 4. Hard factor and RG consistency (R10) [`form_factor.py`, `hard_and_scheme.py`]

### 4.1 One-loop massless quark form factor (independent computation)
Feynman gauge, $\Lambda^\mu=-ig^2C_F\mu^{2\epsilon}\int\frac{d^Dl}{(2\pi)^D}\frac{\gamma^\alpha(\slashed p_1+\slashed l)\gamma^\mu(\slashed l-\slashed p_2)\gamma_\alpha}{l^2(p_1+l)^2(l-p_2)^2}$,
projected with $F={\rm Tr}[\slashed p_1\Lambda^\mu\slashed p_2\gamma_\mu]/{\rm Tr}[\slashed p_1\gamma^\mu\slashed p_2\gamma_\mu]$; Feynman parameters
$(x,y,z)$, $\Delta=-yzq^2$; numerators $T_0=8s_{12}^2(D-2)[(D-2)yz-2y-2z+2]$, $T_{ll}=-4s_{12}(D-2)^3$.  Result (exact in $\epsilon$,
verified at six complex values of $\epsilon$ to 30 digits):
$$
F=1+\frac{\alpha_sC_F}{4\pi}\Big(\frac{4\pi\mu^2}{-q^2-i0}\Big)^{\epsilon}\frac{\Gamma(1+\epsilon)\Gamma^2(1-\epsilon)}{\Gamma(1-2\epsilon)}\Big[-\frac{2-\epsilon+2\epsilon^2}{\epsilon^2(1-2\epsilon)}\Big],\qquad
-\frac{2-\epsilon+2\epsilon^2}{\epsilon^2(1-2\epsilon)}=-\frac2{\epsilon^2}-\frac3\epsilon-8+O(\epsilon).
$$
### 4.2 Hard factor
(Dividing $F^{(1)}$ by $aS_\epsilon$ leaves the factor $(4\pi)^\epsilon/S_\epsilon=e^{\gamma_E\epsilon}$ (binding) or $\Gamma(1-\epsilon)$ (Collins).)
$\mathcal H=1+2{\rm Re}F^{(1)}-(Z_{F,A}Z_2-1)-(Z_{F,B}Z_2-1)$ at $\zeta_A\zeta_B=Q^4$ (pure DR: the TMD virtual graphs vanish, the real
emission is reproduced by the TMDs).  All poles cancel and, with $L=\ln(Q^2/\mu^2)$, $a=\alpha_sC_F/2\pi$:

| | binding $S_\epsilon$ | Collins $S_\epsilon$ |
|---|---|---|
| DY ($q^2=+Q^2$, $\ln(-q^2-i0)=\ln Q^2-i\pi$) | $1+a[-L^2+3L-8+\frac{7\pi^2}6]$ | $1+a[-L^2+3L-8+\pi^2]$ |
| SIDIS ($q^2=-Q^2$) | $1+a[-L^2+3L-8+\frac{\pi^2}6]$ | $1+a[-L^2+3L-8]$ |

RG: $\frac{d\ln\mathcal H}{d\ln\mu}=a(4L-6)=-\gamma_F(\zeta_A)-\gamma_F(\zeta_B)$ for $\zeta_A\zeta_B=Q^4$: **PASS** (all four).
**Literature:** EIS 2012 §7 ("Factorization at $O(\alpha_s)$"): $H=1+a[-3\ln\frac{\mu^2}{Q^2}-\ln^2\frac{\mu^2}{Q^2}-8+\frac{7\pi^2}6]$ and
$\gamma_H=-a[6+4\ln\frac{\mu^2}{Q^2}]$ (standard $S_\epsilon$) — **PASS**.  Aybat–Rogers, arXiv:1107.3973 (proceedings "TMD-factorization,
Factorization Breaking and Evolution", using Collins 2011 §10.12.3): $|\mathcal H|^2_{\rm SIDIS}=1+\frac{C_F\alpha_s}\pi[\frac32L-\frac12L^2-4]$,
$|\mathcal H|^2_{\rm DY}=1+\frac{C_F\alpha_s}\pi[\frac32L-\frac12L^2-4+\frac{\pi^2}2]$ (Collins $S_\epsilon$) — **PASS**.  Collins–Rogers 2013
("Different versions of $\overline{\rm MS}$"): the $\pi^2$ terms of the two hard factors differ by a factor $7/6$, explained by the
$S_\epsilon$ convention — **PASS** ($\frac{7\pi^2}6:\pi^2$).
### 4.3 Scheme dependence
$\tilde C_{\rm binding}=\tilde C_{\rm Collins}-a\frac{\pi^2}{12}\delta(1-x)$, $\mathcal H_{\rm binding}=\mathcal H_{\rm Collins}+a\frac{\pi^2}6$ (DY and SIDIS);
$\gamma_F$, $\gamma_K$, $\tilde K$ unchanged at one loop; the products $\mathcal H\tilde C\tilde C$ (hence cross sections) are identical.

---------------------------------------------------------------------------------------------------------------------

## 5. Evolution and CSS resummation for Drell–Yan (R11)

### 5.1 Solution of the evolution equations
$\frac{\partial\ln\tilde f}{\partial\ln\sqrt\zeta}=\tilde K(b_T;\mu)$, $\frac{d\tilde K}{d\ln\mu}=-\gamma_K(\alpha_s(\mu))$,
$\frac{d\ln\tilde f}{d\ln\mu}=\gamma_F(\alpha_s(\mu);1)-\frac12\gamma_K\ln\frac{\zeta}{\mu^2}$, integrated from $(\mu_b,\zeta=\mu_b^2)$ to $(\mu,\zeta)$:
$$
\tilde f(x,b_T;\mu,\zeta)=\tilde f(x,b_T;\mu_b,\mu_b^2)\exp\Big\{\ln\frac{\sqrt\zeta}{\mu_b}\tilde K(b_T;\mu_b)+\int_{\mu_b}^{\mu}\frac{d\mu'}{\mu'}\Big[\gamma_F(\mu';1)-\ln\frac{\sqrt\zeta}{\mu'}\gamma_K(\mu')\Big]\Big\}
$$
(the form of Aybat–Rogers 2011 eq. (26) at small $b_T$; $b_*$ and $g_K$, $g_{j/H}$ for large $b_T$ are not part of this check).
DY: $\tilde W=\mathcal H(Q;\mu)\tilde f_A(x_A,b;\mu,\zeta_A)\tilde f_B(x_B,b;\mu,\zeta_B)$, $\zeta_A\zeta_B=Q^4$;
$\frac{d\sigma}{dQ^2dy\,d^2q_T}=\sigma_0\sum_qe_q^2\int\frac{d^2b}{(2\pi)^2}e^{i\boldsymbol q_T\cdot\boldsymbol b}\tilde W+\dots$, $\sigma_0=\frac{4\pi\alpha^2}{3N_cQ^2s}$.
### 5.2 CSS form and one-loop dictionary [`css_expansion.py`]
At $\mu=Q$, $\zeta_A=\zeta_B=Q^2$ and with $\tilde K^{(1)}(b;\mu_b)=0$:
$$
\tilde W=\exp\Big\{-\int_{\mu_b^2}^{Q^2}\frac{d\mu^2}{\mu^2}\Big[A(\alpha_s)\ln\frac{Q^2}{\mu^2}+B(\alpha_s)\Big]\Big\}\,(C\otimes f)(x_A;\mu_b)\,(C\otimes f)(x_B;\mu_b),
$$
$$
A^{(1)}=\tfrac12\gamma_K^{(1)}=C_F,\qquad B^{(1)}=-\gamma_F^{(1)}(1)=-\tfrac32C_F\qquad(\text{units }\alpha_s/\pi),
$$
$$
C_{qq}(z)=\tilde C_{q/q}(z;\mu_b,\mu_b^2)+\tfrac12\mathcal H^{(1)}(Q;Q)\delta(1-z)
=\delta(1-z)+\frac{\alpha_s}\pi\Big[\frac{C_F}2(1-z)+C_F\Big(\frac{\pi^2}4-2\Big)\delta(1-z)\Big],\qquad C_{qg}=\frac{\alpha_s}\pi T_Fz(1-z),
$$
identical in both $S_\epsilon$ conventions; for SU(3): $\frac{\alpha_s}\pi[\frac23(1-z)+\frac{\pi^2-8}3\delta(1-z)]$ and $\frac{\alpha_s}\pi\frac12z(1-z)$.
**Literature:** Balázs–Yuan, Phys. Rev. D 56 (1997) 5558, appendix "A, B and C functions" (canonical $C_1=b_0$, $C_2=1$; they cite CSS
1985 and Davies–Stirling, Nucl. Phys. B244 (1984) 337): $A^{(1)}=C_F$, $B^{(1)}=-3C_F/2$,
$C^{(1)}_{jk}=\delta_{jk}\{\frac23(1-z)+\frac13\delta(1-z)(\pi^2-8)\}$, $C^{(1)}_{jG}=\frac12z(1-z)$ — **PASS** (checked in source).
(Beyond one loop $A$, $B$ receive contributions from $\tilde K(b;\mu_b)$ and the running coupling; not derived here.)
### 5.3 $O(\alpha_s)$ expansion vs fixed order
Fourier identities ($\boldsymbol q_T\ne0$, $L\equiv\ln(Q^2b^2/b_0^2)$), from the exact generating function
$\int\frac{d^2b}{(2\pi)^2}e^{i\boldsymbol q\cdot\boldsymbol b}\big(\frac{Q^2b^2}{b_0^2}\big)^\eta=-\frac{\eta}{\pi q^2}\big(\frac{Q^2}{q^2}\big)^\eta e^{2\gamma_E\eta}\frac{\Gamma(1+\eta)}{\Gamma(1-\eta)}$:
$$
{\rm FT}[L]=-\frac1{\pi q_T^2},\qquad{\rm FT}[L^2]=-\frac2\pi\frac{\ln(Q^2/q_T^2)}{q_T^2},\qquad {\rm FT}[L^3]=-\frac3\pi\frac{\ln^2(Q^2/q_T^2)}{q_T^2},
$$
equivalently $\int_0^\infty d\eta J_1(\eta)\ln^m(\eta/b_0)=1,0,0$ ($m=0,1,2$; numerically to $10^{-8}$, analytically from
$\int_0^\infty J_1\eta^s=2^s\Gamma(1+\frac s2)/\Gamma(1-\frac s2)$): this is why $b_0=2e^{-\gamma_E}$ removes constants.  Expanding,
$$
\frac{d\sigma}{dQ^2dy\,dq_T^2}\Big|_{q_T\ll Q}=\sigma_0\frac{\alpha_s}{2\pi}\frac1{q_T^2}\Big\{\Big[2A^{(1)}\ln\frac{Q^2}{q_T^2}+2B^{(1)}\Big]q(x_A)\bar q(x_B)
+(P_{qq}\otimes q)(x_A)\bar q(x_B)+q(x_A)(P_{qq}\otimes\bar q)(x_B)+(P_{qg}\otimes g)(x_A)\bar q(x_B)+\dots\Big\}+O\Big(\frac{\alpha_s}{Q^2}\Big),
$$
($P$ in the CONTEXT normalization $\frac{\alpha_s}{2\pi}P$; the $\frac32\delta$ in $P_{qq}$ and $2B^{(1)}$ cancel as they must).
Exact $O(\alpha_s)$ fixed order from the matrix elements $\overline{|\mathcal M|^2}_{q\bar q\to\gamma^*g}\propto\frac tu+\frac ut+\frac{2Q^2s}{tu}$,
$\overline{|\mathcal M|^2}_{qg\to\gamma^*q}\propto-(\frac st+\frac ts+\frac{2Q^2u}{st})$ [`dy_matrix_elements.py`]: ratio exact/expansion
$\to1$ as $q_T\to0$ (e.g. $1.0000000$ at $q_T/Q=10^{-4}$, deviation $\sim q_T^2/Q^2$) for two kinematic points and PDF sets, for the
$q\bar q$ and $qg$ channels; altering $A^{(1)}$ or $B^{(1)}$ destroys the agreement by $10^{5}$–$10^{7}$ times the residual
[`dy_qt_check.py`, `dy_qt_check2.py`] — **PASS**.

---------------------------------------------------------------------------------------------------------------------

## 6. Sivers function: process dependence (R12)

### 6.1 Definitions and sign convention
Trento (Bacchetta, D'Alesio, Diehl, Miller, PRD 70 (2004) 117504, eq. (sivers-def), checked in source):
$f_{q/p^\uparrow}(x,\boldsymbol k_T)=f_1(x,k_T^2)-f_{1T}^\perp(x,k_T^2)\frac{(\hat{\boldsymbol P}\times\boldsymbol k_T)\cdot\boldsymbol S}{M}$; for
$\hat{\boldsymbol P}=\hat z$, $(\hat z\times\boldsymbol k_T)\cdot\boldsymbol S=\epsilon^{ij}k_T^iS_T^j$ with $\epsilon^{12}=+1$.
$f_{1T}^\perp>0$ means quarks prefer to move to the left for a proton moving towards the observer with spin up (Trento).
### 6.2 Theorem (T11.14) and proof
For the operator-defined TMDs, $\tilde f^{[+]}(x,\boldsymbol b_T;S)=\tilde f^{[-]}(x,\boldsymbol b_T;-S)$, hence
$f_1^{\rm SIDIS}=f_1^{\rm DY}$, $f_{1T}^{\perp\,\rm SIDIS}=-f_{1T}^{\perp\,\rm DY}$ (Collins 2002).
*Proof* (antiunitary $\mathcal A=\mathcal{PT}$; Dirac rep., $T_D=i\gamma^1\gamma^3$):
1. Fields: $\mathcal T\psi(x)\mathcal T^{-1}=T_D\psi(\tilde x)$, $\tilde x=(-x^0,\boldsymbol x)$; $\mathcal P\psi(x)\mathcal P^{-1}=\gamma^0\psi(\bar x)$. Checked:
   $T_D\gamma^{\mu*}T_D^{-1}=\gamma_\mu$, $\gamma^0T_D^\dagger\gamma^0=T_D$, $T_D^2=1$, $\gamma^0\gamma^\mu\gamma^0=\gamma_\mu$.  Hence for a bilinear
   (antiunitarity conjugates the c-number matrix $\Gamma$): $\mathcal T\bar\psi(x)\Gamma\psi(y)\mathcal T^{-1}=\bar\psi(\tilde x)\,\gamma^0T_D^\dagger\gamma^0\Gamma^*T_D\,\psi(\tilde y)$;
   $\gamma^+\xrightarrow{\mathcal T}\gamma^-\xrightarrow{\mathcal P}\gamma^+$ [`sivers_symmetry.py`].  T alone maps a TMD of a hadron moving in $+z$
   with $\gamma^+$ to one of a hadron moving in $-z$ with $\gamma^-$; P (or a rotation by $\pi$) maps it back.
2. Gauge field: $\mathcal{PT}A^\mu(x)(\mathcal{PT})^{-1}=A^\mu(-x)$ with the colour matrices conjugated by antiunitarity, which is
   compensated by $\eta_at^{a*}=t^a$.  For a Wilson line, $i\to-i$ and $dz\to-dz$ combine:
   $\mathcal{PT}\,W[b,a]\,(\mathcal{PT})^{-1}=W[-b,-a]$ along the reflected path, **with the same path ordering** (antiunitary maps preserve
   operator order).  Thus $\mathcal W^{[+]}(w,0;n)\to\mathcal W^{[-]}(-w,0;n)$ (future $\to$ past pointing, transverse link included).
3. States: $\mathcal{PT}|P,S\rangle=\eta|P,-S\rangle$ (momentum kept, spin vector reversed; checked with spinors:
   $\gamma^0T_Du^*(P,S)\,\overline{(\cdots)}\propto(\slashed P+M)(1-\gamma_5\slashed S)/2$).
4. $\langle\alpha|O|\alpha\rangle=\langle\mathcal A\alpha|\mathcal AO\mathcal A^{-1}|\mathcal A\alpha\rangle^*$ gives
   $\langle P,S|O^{[+]}(w)|P,S\rangle=\langle P,-S|O^{[-]}(-w)|P,-S\rangle^*$, with $O^{[\pm]}(w)=\bar\psi(w)\gamma^+\mathcal W^{[\pm]}(w,0)\psi(0)$; then
   $\langle O\rangle^*=\langle O^\dagger\rangle$, $[O^{[-]}(-w)]^\dagger=\bar\psi(0)\gamma^+\mathcal W^{[-]}(0,-w)\psi(-w)$ and translation by $+w$
   give $\langle P,-S|O^{[-]}(w)|P,-S\rangle$. Fourier transforming in $w^-$ (with $x$ real) proves the claim.  The Sivers structure
   $\epsilon^{ij}k^iS^j$ is odd in $S$, $f_1$ even. $\square$
*Status:* [R] given the operator definitions ("R_def"; it uses only P, T invariance of QCD, hermiticity and translation invariance);
relating measured asymmetries with opposite sign uses TMD factorization [A].
*Caveat found here (§3.4):* with **time-like** non-light-like Wilson lines the past-pointing path-ordered operator is anti-time-ordered,
whereas the operator generated by factorization (and computed with Feynman rules) is time-ordered; then the PT image of the
SIDIS TMD is **not** the DY TMD at finite rapidity (one-loop vertex differs by $2\pi^2\frac{\alpha_sC_F}{4\pi}$ in its real part).  With space-like
(Collins) or light-like lines the two orderings coincide and the theorem holds.
### 6.3 $b$-space form (CONTEXT Fourier convention)
${\rm FT}[k^ig(k^2)]=2ib^i\,\partial\tilde g/\partial(b^2)$, hence
$$
\tilde f(x,\boldsymbol b_T;S)=\tilde f_1(x,b_T)+iM\epsilon^{ij}b_T^iS_T^j\,\tilde f_{1T}^{\perp(1)}(x,b_T),\qquad
\tilde f_{1T}^{\perp(1)}\equiv-\frac2{M^2}\frac{\partial\tilde f_{1T}^\perp}{\partial b_T^2},\qquad\tilde f_{1T}^{\perp(1)}(x,0)=\int d^2k_T\frac{k_T^2}{2M^2}f_{1T}^\perp,
$$
(checked with a Gaussian); the Sivers term is imaginary, as required by $\tilde f(x,\boldsymbol b)^*=\tilde f(x,-\boldsymbol b)$; the theorem
reads $\tilde f_{1T}^{\perp(1)[+]}=-\tilde f_{1T}^{\perp(1)[-]}$.
### 6.4 One-gluon final-state-interaction phase (Brodsky–Hwang–Schmidt mechanism) [`sivers_spectator.py`]
Scalar-diquark model: nucleon ($M$) $\to$ quark ($m$) $+$ scalar diquark ($\lambda$), point-like Yukawa coupling $g$; abelian gluon
coupling $e_q$ (quark and Wilson line) and $e_s$ (diquark); vertex conventions of §1.  Tree amplitude
$\mathcal M_0=-g\frac{\slashed k+m}{k^2-m^2}U(P,S)$, $k^2-m^2=-\frac{k_T^2+L^2}{1-x}$, $L^2=x\lambda^2+(1-x)m^2-x(1-x)M^2$.
One-gluon exchange between the eikonal line and the outgoing diquark:
$$
\mathcal M_1=-ie_qe_sg\!\int\!\frac{d^4l}{(2\pi)^4}\frac{[2(1-x)P^++l^+]\,(\slashed k-\slashed l+m)U}{(l^+\mp i0)(l^2+i0)((P-k+l)^2-\lambda^2+i0)((k-l)^2-m^2+i0)}\qquad(\text{SIDIS}:-,\ \text{DY}:+).
$$
The T-odd part comes from $\frac1{l^+\mp i0}={\rm PV}\pm i\pi\delta(l^+)$; at $l^+=0$ the $l^-$ integral is done by residues
($=\frac{\pi i}{P^+[(\boldsymbol k-\boldsymbol l)_T^2+L^2]}$), the $l^-\gamma^+$ term drops ($\gamma^+\gamma^+=0$):
$$
\mathcal M_1^{\rm odd}=\mp2\pi^2i(1-x)\frac{e_qe_sg}{(2\pi)^4}\int d^2l_T\frac{(\slashed k+\boldsymbol\gamma_T\cdot\boldsymbol l_T+m)U}{\boldsymbol l_T^2[(\boldsymbol k-\boldsymbol l)_T^2+L^2]},\qquad
\int d^2l_T\frac{\boldsymbol l_T}{\boldsymbol l_T^2[(\boldsymbol k-\boldsymbol l)_T^2+L^2]}=\frac{\pi\boldsymbol k_T}{k_T^2}\ln\frac{k_T^2+L^2}{L^2}.
$$
With $f=\frac{1}{4(2\pi)^3(1-x)P^+}\sum\overline{\mathcal M}\gamma^+\mathcal M$ and $U\bar U=(\slashed P+M)(1+\gamma_5\slashed S)/2$:
$$
f_1=\frac{g^2}{16\pi^3}\frac{(1-x)[(m+xM)^2+k_T^2]}{(k_T^2+L^2)^2},\qquad
f_{1T}^{\perp\,\rm SIDIS}=\frac{g^2e_qe_s}{4(2\pi)^4}\frac{M(m+xM)(1-x)}{k_T^2(k_T^2+L^2)}\ln\frac{k_T^2+L^2}{L^2}=-f_{1T}^{\perp\,\rm DY}
$$
(full Dirac traces evaluated numerically, closed forms agree to $10^{-10}$, DY/SIDIS $=-1$ to $10^{-12}$).  For an attractive FSI
($e_qe_s<0$; QCD colour singlet $e_qe_s\to-4\pi C_F\alpha_s$) $f_{1T}^{\perp\,\rm SIDIS}<0$ for $m+xM>0$.
**Literature:** Bacchetta–Conti–Radici, PRD 78 (2008) 074010 [arXiv:0807.0323], eq. (SivBM2-s-pl) (point-like scalar diquark, SIDIS,
Trento): $f_{1T}^{\perp}=-\frac{g_s^2}4\frac{Me_c^2}{(2\pi)^4}\frac{(m+xM)(1-x)}{p_T^2[L^2+p_T^2]}\log\frac{L^2+p_T^2}{L^2}$, with eikonal vertex $-ie_cn^\rho$,
propagator $\frac{i}{-l^++i\epsilon}$, diquark vertex $+ie_c(2P-2p+l)^\rho$, i.e. $e_q=-e_c$, $e_s=e_c$, $e_qe_s=-e_c^2$ in our conventions, and
$e_c^2\to4\pi C_F\alpha_s$ for QCD: identical to ours — **PASS**; BCR also state that the $l^++i\epsilon$ propagator of DY gives the
opposite sign.  Physical picture (BHS 2002): the struck quark rescatters on the spectator with an on-shell (Coulomb-like) phase; the
asymmetry is the interference of this phase with the tree amplitude between nucleon helicity states differing by one unit of orbital
angular momentum (factor $m+xM$).  The negative sign is tied to a positive anomalous magnetic moment: BCR 2008 eq. (Sivers-kappa)
find $\int_0^1dx\,(1-x)f_{1T}^{\perp q}(x)=-\frac32MC_F\alpha_s\kappa^q$ in their (dipolar form factor) model, generalizing Burkardt 2003 and
Lu–Schmidt 2006 (as cited there; "lensing").  That the phenomenological $f_{1T}^{\perp u}$ (SIDIS, Trento) is negative is *recalled, not verified*.

---------------------------------------------------------------------------------------------------------------------

## 7. Literature cross-check table

| Quantity | Our convention | Source (checked text) | Their convention / conversion | Result |
|---|---|---|---|---|
| $\tilde C_{q/q}$, $\tilde C_{q/g}$ | §3.9 | Aybat–Rogers, PRD 83 (2011) 114042, arXiv:1101.5057v2, (A10),(A11) | Collins $S_\epsilon$ (their (A4),(A9) counterterms $\propto(4\pi)^\epsilon/\Gamma(1-\epsilon)$); same $\zeta$ normalization as ours (see §1.4 caveat on their eq. (3)) | PASS |
| $\gamma_F$, $\tilde K$, $\gamma_K$ | §3.8 | same, (B1)–(B3) and eqs. (18),(20)–(22) | identical | PASS |
| $\tilde C_n$ (std $\overline{\rm MS}$) | §3.9, $\kappa=1$ | EIS, JHEP 07 (2012) 002, arXiv:1111.4996, §4 (label `coeff`) | $\mathcal P_{q/q}=[\frac{1+x^2}{1-x}]_+$, $L_T=L_b$, $\zeta=Q^2$ | PASS |
| $\mathcal H_{\rm DY}$ (std) | §4.2 | EIS 2012 §7 | identical | PASS |
| $\mathcal H_{\rm DY},\mathcal H_{\rm SIDIS}$ (Collins) | §4.2 | Aybat–Rogers, arXiv:1107.3973 | $\frac{C_F\alpha_s}\pi$ normalization | PASS |
| $\pi^2$ ratio 7/6 | §4.3 | Collins–Rogers, PRD 87 (2013) 034018, arXiv:1210.2100 | statement | PASS |
| $\zeta$, $\delta$-regulator map | §1, §3.10 | Collins–Rogers 2013 eqs. (zeta.A), (zetaA) | identical | PASS |
| order of limits | §2.3, §3.4 | Collins–Rogers 2013 §3 | — | consistent |
| CSS $A,B,C$ | §5.2 | Balázs–Yuan, PRD 56 (1997) 5558, hep-ph/9704258, App. | units $\alpha_s/\pi$, $C_1=b_0$, $C_2=1$ | PASS |
| Sivers convention | §6.1 | Trento 2004, hep-ph/0410050 | identical | — |
| Sivers in model | §6.4 | BCR 2008, arXiv:0807.0323, (SivBM2-s-pl) | $e_qe_s=-e_c^2$ | PASS |
| sign reversal | §6.2 | Collins, PLB 536 (2002) 43 (statement as quoted in Trento) | — | consistent |

Recalled but **not** re-checked in this session: Collins 2011 equation numbers other than those quoted by Collins–Rogers 2013
(13.106), (14.31), §3.3.2, §10.8, §10.11.1, §10.12.3; Davies–Stirling 1984 (only via Balázs–Yuan); BHS 2002 sign conventions;
phenomenological sign of $f_{1T}^{\perp u}$; Meissner–Metz 2009 (universality of T-odd FFs, mentioned by the critic).

---------------------------------------------------------------------------------------------------------------------

## 8. Discrepancies, caveats and recommendations

1. **Blueprint P11.11 vs P11.13 mix two $\overline{\rm MS}$ conventions.** P11.11 quotes $\mathcal H=1+a[-L^2+3L-8+\frac{7\pi^2}6]$ (binding/standard
   $S_\epsilon$) while P11.13 quotes $\tilde C_{q/q}(\mu_b,\mu_b^2)=\delta+a(1-x)$ (Collins $S_\epsilon$).  Combined they give $\tilde W$ wrong by
   $a\frac{\pi^2}6\delta(1-x)$ at $O(\alpha_s)$.  Fix: with the binding $S_\epsilon$ of CONTEXT.md use
   $\tilde C_{q/q}=\delta+a[(1-x)-\frac{\pi^2}{12}\delta(1-x)]$; or state both and the conversion of §4.3.
2. **CONTEXT.md should state** that for TMDs and hard factors (double poles) the choice of $S_\epsilon$ changes finite terms, and fix it
   for Ch. 11 (recommended: keep binding $S_\epsilon$, quote Collins-scheme numbers only with the conversion).
3. **$\zeta$ normalization:** $\zeta=M^2x^2e^{2(y_P-y_n)}=2(xP^+)^2e^{-2y_n}$ (blueprint D11.5 is correct); do not copy Aybat–Rogers eq. (3) (spurious factor 2).
4. **Order of limits** must be stated in D11.5: light-like limit first (at fixed $\epsilon$), then renormalization, then $\epsilon\to0$; otherwise the
   non-light-like vertex graph leaves $\ln^2(\Lambda_B^2/\mu^2)$ terms (§3.4).
5. **Wilson-line directions:** state that the regulator lines are space-like (Collins; Aybat–Rogers citing Collins–Metz 2004).  With time-like
   past-pointing lines the PT argument of T11.14 fails at finite rapidity (§3.4, §6.2) — a concrete one-loop reason for the choice.
6. **Blueprint P11.13 error term** "$O(b_Tm)$": write $O((mb_T)^p)$, $p>0$, unless a specific power is justified.
7. **Blueprint E11.16** is fine; note the eikonal factor for the line attached to $\psi(0)$ is $\frac{gn^\mu}{n\cdot l\mp i0}$ (momentum into the line),
   and for an emitted gluon $\frac{-gn^\mu}{n\cdot l\pm i0}$.
8. Statement "$\tilde K$ verified (c7)" in the critic table: consistent with R7 here.
9. *Not a discrepancy but a warning:* individual pieces (unsubtracted TMD, soft factor, vertex graph) are regulator dependent; e.g. the
   time-like vs space-like vertex differ by $\pi^2$ terms at finite rapidity; only the combined object of D11.5 is regulator independent
   (critic C10) — confirmed at one loop by the agreement of the non-light-like-line and $\delta$-regulator results.

---------------------------------------------------------------------------------------------------------------------

## 9. Files and reproduction
`scripts/run_all.sh` runs every script and writes `logs/<name>.log` (total run time ≈ 3 min).

| script | content |
|---|---|
| `dirac.py` | minimal $D$-dimensional trace/contraction utility |
| `real_graphs.py` | R1 |
| `rapidity_checks.py`, `one_loop_tmd.py` | R2, R5–R8 assembly, RG checks |
| `virtual_vertex.py` | R3, R3' |
| `soft_factor.py` | R4, $\tilde K$ from soft factor |
| `ft_check.py` | $d$-dim Fourier transform |
| `collins_tmd.py` | R6–R8 (both $S_\epsilon$), independent implementation |
| `quark_in_gluon.py` | $\tilde C_{q/g}$ |
| `delta_regulator.py` | R9 |
| `form_factor.py`, `hard_and_scheme.py` | R10 |
| `css_expansion.py`, `dy_matrix_elements.py`, `dy_qt_check.py`, `dy_qt_check2.py` | R11 |
| `sivers_spectator.py`, `sivers_symmetry.py` | R12 |

LaTeX: `tex/tmd_definitions.tex`, `tex/tmd_oneloop.tex`, `tex/tmd_evolution.tex`, `tex/tmd_sivers.tex` (Chinese text, monograph macros),
test driver `tex/test_build.tex` (XeLaTeX with `preamble_fact.tex` copied from `../../common/`).
