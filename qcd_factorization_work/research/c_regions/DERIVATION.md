# Landau equations, IR power counting and the method of regions — derivations and checks

Directory: `"/Users/hao-cheng/Desktop/theorem proof/qcd_factorization_work/research/c_regions"`
(all scripts: `python3 -I <script>.py`; logs in `logs/`; LaTeX snippets `landau.tex`, `powercounting.tex`,
`regions.tex`, test driver `test_build.tex`).

Everything below was derived independently and checked by computer algebra (sympy, exact in ε where stated)
and by numerical cross-checks (mpmath/numpy/scipy). Literature values used as cross-checks were read in
the original source when that source is openly accessible (arXiv PDFs downloaded 2026-10-09; see §5). Items
that could **not** be verified against the original text are marked **[unverified]**.

Units and conventions follow `CONTEXT.md`: metric $(+,-,-,-)$; light-front $v^\pm=(v^0\pm v^3)/\sqrt2$,
$v\cdot w=v^+w^-+v^-w^+-\vec v_T\cdot\vec w_T$; $D=4-2\epsilon$. **Two different small parameters** appear in the
literature and are kept apart here:

* $\lambda$ ("SCET units"): collinear $k\sim Q(1,\lambda^2,\lambda)$ in $(k^+,k^-,k_T)$, soft $Q(\lambda,\lambda,\lambda)$,
  ultrasoft $Q(\lambda^2,\lambda^2,\lambda^2)$, Glauber $Q(\lambda^2,\lambda^2,\lambda)$;
* $\lambda_S=\lambda^2$ ("Sterman units"; Sterman 1978, TASI'95, CSS 1989): soft momenta $\sim\lambda_S$ in all components,
  collinear normal variables $(k^-,k_T)\sim(\lambda_S,\lambda_S^{1/2})$. Sterman's degree of divergence $\omega$ is the power of
  $\lambda_S$; the power of $\lambda$ is $p=2\omega$.

Loop-integral normalisation (Part 3): $\displaystyle I=e^{\epsilon\gamma_E}\mu^{2\epsilon}\!\int\!\frac{d^Dk}{i\pi^{D/2}}\prod_j\frac{1}{(-q_j^2+m_j^2-i0)^{\nu_j}}$.

---------------------------------------------------------------------------------------------------

## 0. Results at a glance

| # | result (exact form, conventions above) | check | status |
|---|---|---|---|
| L1 | α-space Landau theorem: if no $\alpha\in\bar\Delta$ with $\mathcal F=0,\ \alpha_j\partial_j\mathcal F=0\ \forall j$, the parametric integral is finite and analytic at $p_0$ (deformation $z_j=\alpha_j[1-i\eta(\partial_j\mathcal F-\sum_k\alpha_k\partial_k\mathcal F)]$, $\operatorname{Im}\mathcal F(z)=-\eta\sum_j\alpha_j w_j^2+O(\eta^3)$) | `landau_oneloop.py` L2 (symbolic), L6 (numeric) | PASS |
| L2 | envelope identity $\partial(\mathcal F/\mathcal U)/\partial\alpha_j=-D_j(k_c)$, $\mathcal F/\mathcal U=\sum_j\alpha_j(m_j^2-q_j^2)|_{k_c}$ | L1 (exact, random rational kinematics) | PASS |
| L3 | momentum-space necessary condition for a trapped point (Gordan alternative) | L5 (LP) | PASS |
| L4 | massless vertex: Landau set = closed edges $\{\alpha_2=0\}$ (collinear to $p_1$, $k=xp_1$), $\{\alpha_1=0\}$ (collinear to $p_2$), soft corner $k=0$; edge $\{\alpha_0=0\}$ (normal threshold) only at $Q^2=0$ | L3a, L4 | PASS |
| L5 | massless box: Landau set = 4 edges $(01),(12),(23),(30)$ + 4 corners; $(02),(13)$ only at $s=0$, $t=0$ | L3e | PASS |
| P1 | collinear region of the vertex: $\int dk^-\,[D_0D_1D_2]^{-1}=\dfrac{2\pi i}{2p_1^+}\dfrac{1}{k_T^2\,(xQ^2-k_T^2/(1-x))}$, poles pinch $k^-=0$ from opposite sides; $\int d^2k_T/k_T^2$: log | `vertex_collinear_numeric.py` C1–C5 | PASS |
| P2 | $\omega(R)=\sum_J\tfrac12\big(f_J^{g}+t_J+2u_J+2f_J^{b}-e_J\big)+\tfrac12\sum_J s^{q}_J+b_{S\to H}+\tfrac32 f_{S\to H}$ (Feynman gauge, Sterman units) | `power_counting.py` P1,P4,P5,P7; agrees with Sterman TASI'95 eq.(64) and architect P3.9 | PASS |
| P3 | Glauber, soft, ultrasoft exchanges all scale as $\lambda^0$; eikonal error $O(\lambda)$, $O(\lambda^2)$, $O(1)$ resp.; vertex Glauber region untrapped, DY-type trapped | P1, P3, P6 | PASS |
| R1 | off-shell Sudakov, regions (each $\times 1/Q^2$): $H=(\tfrac{\mu^2}{Q^2})^\epsilon e^{\epsilon\gamma_E}\tfrac{\Gamma(1+\epsilon)\Gamma^2(-\epsilon)}{\Gamma(1-2\epsilon)}$, $C_{1,2}=-(\tfrac{\mu^2}{P^2})^\epsilon e^{\epsilon\gamma_E}\tfrac{\Gamma(1+\epsilon)\Gamma^2(-\epsilon)}{\Gamma(1-2\epsilon)}$, $S=-(\tfrac{\mu^2Q^2}{P^4})^\epsilon e^{\epsilon\gamma_E}\Gamma(1+\epsilon)\Gamma(\epsilon)\Gamma(-\epsilon)$ | `sudakov_regions.py` A2 (= BBF 2015 eqs. 2.39, 2.41, 2.43) | PASS |
| R2 | $H+C_1+C_2+S=\frac1{Q^2}\big[\ln^2\tfrac{Q^2}{P^2}+\tfrac{\pi^2}{3}\big]+\epsilon\,(\dots)$; poles cancel; $=Q^{-2}\Phi^{(1)}(t,t)$ at LP | A1, A3, A4 (= BBF eq. 2.44; Usyukina–Davydychev) | PASS |
| R3 | NLP and NNLP coefficients from the regions $=$ exact: $Q^2I=L^2+\frac{\pi^2}3+t(2L^2+4L-4+\frac{2\pi^2}3)+t^2(6L^2+14L-11+2\pi^2)+O(t^3L^2)$, $L=\ln t$, $t=P^2/Q^2$ | A5 | PASS |
| R4 | massive exchange, on-shell massless legs: pure DR ill-defined; with analytic regulators $H+C_1+C_2=\frac1{Q^2}[\tfrac12\ln^2\tfrac{Q^2}{M^2}+\tfrac{\pi^2}3]$ | B1–B4 (= Jantzen 2011 eqs. 6.26–6.30; BBF eqs. 2.50–2.52) | PASS |
| R5 | massive on-shell legs, massless gluon: pure DR suffices; $H+C_1+C_2=\frac1{Q^2}[\tfrac1\epsilon\ln\tfrac{m^2}{Q^2}-\tfrac12\ln^2\tfrac{m^2}{Q^2}-\tfrac{\pi^2}6]$ ($\mu=Q$) | C1 | PASS (corrects critic O11) |
| R6 | LL coefficient: $\delta F_{\rm LL}=-\frac{\alpha}{2\pi}\ln\frac{Q^2}{P_1^2}\ln\frac{Q^2}{P_2^2}$ (off-shell), $-\frac{\alpha}{4\pi}\ln^2\frac{Q^2}{M^2}$ (massive photon) | E (= Sudakov 1956, Jackiw, as quoted by Collins 1989) | PASS |

(Statuses of the *theorems* for the monograph are given in §1.9, §2.7, §3.9.)

---------------------------------------------------------------------------------------------------

## 1. Landau equations

### 1.1 Feynman-parameter representation

Graph $G$ with $L$ loops, $N$ internal lines; line $j$ carries $q_j=\sum_{l}\eta_{jl}k_l+r_j$ ($\eta_{jl}\in\{0,\pm1\}$,
$r_j$ a combination of external momenta), mass $m_j$, propagator $i/(D_j+i0)$ with $D_j\equiv q_j^2-m_j^2$. For a scalar
integrand (numerators: §1.8)
$$
I(p)=\int\prod_{l=1}^{L}\frac{d^Dk_l}{i\pi^{D/2}}\prod_{j=1}^{N}\frac{1}{(-D_j-i0)^{\nu_j}}
=\frac{\Gamma(\nu-LD/2)}{\prod_j\Gamma(\nu_j)}\int_{\mathbb R_+^N}\prod_j d\alpha_j\,\alpha_j^{\nu_j-1}\,
\delta\Big(1-\sum_{j\in\sigma}\alpha_j\Big)\frac{\mathcal U^{\,\nu-(L+1)D/2}}{(\mathcal F-i0)^{\nu-LD/2}},
\qquad \nu=\sum_j\nu_j ,
$$
for any non-empty $\sigma\subset\{1..N\}$ (Cheng–Wu). Define the quadratic form
$\mathcal D(\alpha,k)\equiv\sum_j\alpha_j(m_j^2-q_j^2)=-\sum_{ll'}A_{ll'}\,k_l\!\cdot\! k_{l'}-2\sum_lB_l\!\cdot\! k_l+C$. Then
$\mathcal U=\det A=\sum_{T\in\mathcal T_1}\prod_{j\notin T}\alpha_j$ and
$\mathcal F=\mathcal U\,\mathcal D(\alpha,k_c)=-\sum_{T\in\mathcal T_2}\big(\prod_{j\notin T}\alpha_j\big)s_T+\mathcal U\sum_j\alpha_jm_j^2$,
where $k_c(\alpha)$ is the stationary point of $\mathcal D$ in $k$, $\mathcal T_{1,2}$ are spanning trees / 2-forests and $s_T$ is
the square of the momentum flowing into one component of the 2-forest. $\mathcal U$, $\mathcal F$ are homogeneous of degrees
$L$, $L+1$. (Derivation: $\prod a_j^{-\nu_j}=\frac{\Gamma(\nu)}{\prod\Gamma(\nu_j)}\int d\alpha\,\delta(1-\sum\alpha)\prod\alpha_j^{\nu_j-1}(\sum\alpha_ja_j)^{-\nu}$,
valid since all $a_j=-D_j-i0$ have ${\rm Im}\,a_j<0$; shift $k=k_c+\ell$; Wick rotation of the Gaussian-type integral.)
In the Euclidean region (all $s_T\le0$, $m_j^2\ge0$) $\mathcal F\ge0$ on the simplex.

### 1.2 Theorem L1 (Landau, α-space form; necessary condition) — [R]

**Statement.** Let $p_0$ be real external kinematics, and assume $D$ is such that the parametric integral converges
absolutely when $(\mathcal F-i0)$ is replaced by any function bounded away from zero (i.e. all non-integrabilities
come from zeros of $\mathcal F$; this is the UV-convergence hypothesis). If there is **no** point $\alpha$ of the *closed*
simplex $\bar\Delta=\{\alpha_j\ge0,\ \sum_{j}\alpha_j=1\}$ with
$$
\mathcal F(\alpha,p_0)=0\quad\text{and}\quad \alpha_j\,\frac{\partial\mathcal F}{\partial\alpha_j}(\alpha,p_0)=0\ \ (j=1..N),
$$
then (a) the integral is finite at $p_0$ (no IR divergence) and (b) $I(p)$ extends holomorphically to a complex
neighbourhood of $p_0$ (in the invariants); in particular it is real-analytic at $p_0$. Contrapositive: an IR divergence
or a singularity at $p_0$ requires a solution of the α-space Landau equations. (By Euler's relation
$(L+1)\mathcal F=\sum_j\alpha_j\partial_j\mathcal F$, the condition $\mathcal F=0$ is implied by the others.)

**Proof.** Use $\sigma=\{1..N\}$, so the domain is the compact simplex. Put $c(\alpha)\equiv\sum_k\alpha_k\partial_k\mathcal F$,
$w_j\equiv\partial_j\mathcal F-c$ and deform
$$
\alpha_j\ \longrightarrow\ z_j(\alpha,\tau)=\alpha_j\big[1-i\tau\eta\,w_j(\alpha)\big],\qquad 0\le\tau\le1,\ \eta>0 \text{ small}.
$$
(i) *The constraint is preserved:* $\sum_jz_j=1-i\tau\eta\sum_j\alpha_jw_j=1-i\tau\eta(c-c)=1$.
(ii) *Faces are preserved:* $z_j=0$ whenever $\alpha_j=0$; hence the boundary of the chain moves inside the complexified
faces, and the contribution of the "side" $H([0,1]\times\partial\bar\Delta)$ to Stokes' theorem vanishes (a holomorphic
$(N-1,0)$-form restricted to a real $(N-1)$-chain lying in a complex $(N-2)$-dimensional face is zero). Endpoint
(boundary) singularities in α-space are therefore treated on the same footing as interior ones.
(iii) *Sign of the imaginary part* (check L2, symbolic): for real $p$,
$$
\mathcal F(z)=\mathcal F(\alpha)-i\tau\eta\sum_j\alpha_jw_j\,\partial_j\mathcal F+O(\eta^2)
=\mathcal F(\alpha)-i\tau\eta\,V(\alpha)+O(\eta^2),\qquad V=\sum_j\alpha_jw_j^2=\sum_j\alpha_j(\partial_j\mathcal F)^2-c^2\ \ge0 ,
$$
using $\sum_j\alpha_jw_j=0$; the $O(\eta^2)$ term is real, so ${\rm Im}\,\mathcal F(z)=-\tau\eta V+O(\eta^3)$.
(iv) *No zeros on the deformed chain.* $V(\alpha)=0$ and $\mathcal F(\alpha)=0$ imply $\partial_j\mathcal F=c$ for all $j$ with
$\alpha_j>0$, hence $\mathcal F=c/(L+1)$, hence $c=0$ and $\alpha_j\partial_j\mathcal F=0$ for all $j$: a Landau point. By hypothesis
there is none, so the continuous function $|\mathcal F|+V$ is $\ge2\delta>0$ on $\bar\Delta\times\mathcal N$ for some
neighbourhood $\mathcal N$ of $p_0$ (compactness, continuity). For $\eta$ small: where $|\mathcal F(\alpha)|\ge\delta$,
$|\mathcal F(z)|\ge\delta-C\eta^2>0$; where $|\mathcal F(\alpha)|<\delta$, $V\ge\delta$ and ${\rm Im}\,\mathcal F(z)\le-\tau\eta\delta+C\eta^3<0$.
Thus $\mathcal F(z)-i\varepsilon\neq0$ for all $\tau\in[0,1]$, $\varepsilon\ge0$: the homotopy never crosses the singular set
on the side forbidden by $-i0$, and the $\varepsilon\to0^+$ limit of the original integral equals the integral over
$z(\cdot,1)$ uniformly in $p\in\mathcal N$.
(v) $\mathcal U(z)=\sum_T\prod_{j\notin T}\alpha_j(1-i\tau\eta w_j)$ is a sum of positive monomials times factors in a narrow cone
around the positive axis, so $|\mathcal U(z)|\ge\cos\theta\,\mathcal U(\alpha)$: integrability of $\mathcal U^{a}$ (the UV
hypothesis) is unaffected; likewise $z_j^{\nu_j-1}=\alpha_j^{\nu_j-1}(1-i\tau\eta w_j)^{\nu_j-1}$.
(vi) For complex $p$ near $p_0$, $|\mathcal F(z,p)-\mathcal F(z,p_0)|\le C'|p-p_0|$; shrinking $\mathcal N$ so that $C'|p-p_0|<\eta\delta/2$
keeps $\mathcal F(z,p)\neq0$ on the deformed chain. There the integrand is bounded by $C\,\mathcal U(\alpha)^{a}\prod\alpha_j^{\nu_j-1}$ and
is holomorphic in $p\in\mathcal N$ (complexified); dominated convergence gives finiteness and holomorphy. $\square$

Numerical illustration (L6): massive vertex ($m=1$, gluon mass $0.3$, on-shell legs) — above threshold ($s=5$) the
real simplex contains zeros of $\mathcal F$ but the deformed simplex has $\min|\mathcal F(z)|=1.2\times10^{-3}>0$; at the
normal threshold $s=4m^2$ (Landau point $\alpha=(0,\tfrac12,\tfrac12)$) the zero cannot be avoided.

### 1.3 Lemma L2 (equivalence with the momentum-space Landau equations) — [R]

For $\alpha$ with $\mathcal U(\alpha)\neq0$:
$\{\mathcal F=0,\ \alpha_j\partial_j\mathcal F=0\ \forall j\}\iff$ there is a real $k$ with
$$
\alpha_j\,D_j(k)=0\ \ \forall j,\qquad \sum_j\alpha_j\,\eta_{jl}\,q_j^\mu(k)=0\ \ \forall l\quad(\text{loop equations}),
$$
and then $k=k_c(\alpha)$. *Proof.* The loop equations are $\partial\mathcal D/\partial k_l=0$, i.e. $k=k_c$ ($A$ invertible since
$\det A=\mathcal U\ne0$). Envelope theorem: $\partial_j(\mathcal F/\mathcal U)=\partial\mathcal D/\partial\alpha_j|_{k_c}=m_j^2-q_j(k_c)^2=-D_j(k_c)$
(check L1, exact for 3- and 4-line graphs with random rational kinematics). At $\mathcal F=0$, $\partial_j\mathcal F=\mathcal U\,\partial_j(\mathcal F/\mathcal U)$,
so $\alpha_j\partial_j\mathcal F=-\mathcal U\alpha_jD_j(k_c)$. Conversely, $\alpha_jD_j(k_c)=0$ gives
$\mathcal F/\mathcal U=\mathcal D(k_c)=-\sum_j\alpha_jD_j(k_c)=0$. $\square$
Points with $\mathcal U=0$ (all $\alpha$'s of some loop vanish; $k_c$ escapes to infinity) are the origin of
"second-type" singularities and of UV behaviour; they are excluded here.

**Caveat (important for massless QCD).** The lemma is an *algebraic* equivalence of the two systems of equations. It
does **not** say that a *pinch of the momentum-space contour* occurs iff there is a pinch of the *parameter-space*
contour. Collins (arXiv:2007.04085, App. D1) shows that this implication, implicitly assumed by Landau and by
Coleman–Norton, fails already for the one-loop massless self-energy: the momentum-space collinear pinch at
$p^2=0$ has no counterpart pinch in the parameter integral. Consistent with this, for that graph
$\mathcal F=-p^2\alpha_1\alpha_2$ has only the trivial corner solutions for $p^2\neq0$ and vanishes identically at $p^2=0$
(check L3f). Hence Theorem L1 is used for *singularities in external parameters* (and as an IR-finiteness criterion),
while the *location of trapped regions in loop-momentum space* — what QCD factorization needs — is governed by
Theorem L3 below.

### 1.4 Theorem L3 (momentum space; necessary condition for a trapped point) — [R] (necessity)

Fix real external momenta. For real $k_0\in\mathbb R^{4L}$ let $S=\{j:D_j(k_0)=0\}$ and $u_j=\partial D_j/\partial k\,(k_0)$
(components $2\eta_{jl}q_{j\mu}$). **If there is no $\alpha\in\mathbb R_{\ge0}^{S}\setminus\{0\}$ with $\sum_{j\in S}\alpha_ju_j=0$, then there
is a real direction $v\in\mathbb R^{4L}$ and a neighbourhood $\mathcal V$ of $k_0$ such that the deformation
$k\to k+i\eta\chi(k)v$ ($0\le\chi\le1$ smooth, $\chi=1$ near $k_0$, ${\rm supp}\,\chi\subset\mathcal V$, $\eta$ small) gives
${\rm Im}\,D_j>0$ wherever $\chi>0$ for $j\in S$, and $D_j\neq0$ on the deformed contour for $j\notin S$:** the
integrand is non-singular on the deformed contour near $k_0$ ($k_0$ is not trapped). Equivalently: a trapped
(pinched) real point satisfies the momentum-space Landau equations with $\alpha_j\ge0$ ("physical-region" solutions).

*Proof.* Gordan's alternative: for vectors $u_j$ exactly one holds — (I) $\exists v$: $u_j\cdot v>0\ \forall j$; (II) $\exists\alpha\ge0$,
$\alpha\ne0$, $\sum\alpha_ju_j=0$. [If $0\in{\rm conv}\{u_j\}$ we have (II); otherwise let $v$ be the point of the compact
convex set ${\rm conv}\{u_j\}$ nearest to $0$; then $u\cdot v\ge|v|^2>0$ on it, giving (I); (I) and (II) together give
$0=\sum\alpha_ju_j\cdot v>0$.] Under the hypothesis (I) holds. Because $D_j$ is quadratic,
$D_j(k+i\eta\chi v)=D_j(k)-\eta^2\chi^2(v_j')^2+2i\eta\chi\,q_j(k)\cdot v_j'$ *exactly* ($v'_j=\sum_l\eta_{jl}v_l$), so
${\rm Im}\,D_j=\eta\chi\,u_j(k)\cdot v$, positive near $k_0$ by continuity for $j\in S$. For $j\notin S$, $|D_j|\ge c>0$ on a
small $\mathcal V$ and the deformation changes $D_j$ by $O(\eta)$. $\square$
Numerical check (L5): at $k=0.3p_1$ (collinear point) the LP finds $\alpha=(0.7,0.3)$ (trapped); on a generic point of
$k^2=0$, and on the $q\bar q$ two-particle-cut surface $\{(p_1-k)^2=(p_2+k)^2=0\}$ with $Q^2\neq0$, a deformation exists.

*Remarks.* (a) Zero-momentum massless lines have $u_j=2q_j=0$, so they always satisfy the Landau equations trivially;
whether such a point produces a divergence is decided by power counting (§2). (b) Gluing local deformations into a
global one: the set of admissible directions at a point (those with $u_j\cdot v>0$ for the lines on shell there) is a
convex cone, and the cones of nearby points are compatible, so a partition of unity gives a global deformation away
from trapped points; a careful treatment, including the converse (Landau $\Rightarrow$ trapped, which is the delicate part
because of "anomalous" deformations with vanishing first-order shift), is given in Collins (arXiv:2007.04085) for
integrands whose denominators are at most quadratic with a sign condition — satisfied by standard Feynman graphs and
by graphs with Wilson-line (linear) denominators. That preprint has no journal publication listed on INSPIRE
(2026-10). (c) The sign $\alpha_j\ge0$ is tied to the $+i0$ prescription.

### 1.5 Coleman–Norton picture — [R] as an algebraic statement

For a solution with $\alpha_j\ge0$ and real $k$, assign to each line the space–time displacement $\Delta x_j=\alpha_jq_j$
(along its orientation). The loop equations state exactly that $\sum\Delta x_j$ around every loop vanishes, i.e.
vertex positions $x_v$ exist with $x_{\rm end}-x_{\rm start}=\alpha_jq_j$: on-shell lines with $\alpha_j>0$ are classical
particles propagating with velocity $\vec q_j/q_j^0$ (light-like for massless lines), lines with $\alpha_j=0$ have zero
length (contracted into effective vertices). Zero-momentum lines are degenerate ($\alpha_j\cdot0=0$); in the scaled
limit $\alpha_j\to\infty$, $\alpha_jq_j$ finite, they connect arbitrary points (soft exchange). The algebraic equivalence is
trivial; the stronger statement "trapped $\iff$ classically realizable" needs Theorem L3 *and* its converse
(Coleman & Norton 1965; gaps in their proof, not in the result, are discussed by Collins 2020).

### 1.6 One-loop massless vertex $\gamma^*(q)\to q(p_1)\bar q(p_2)$

$p_1^2=p_2^2=0$, $q^2=2p_1\cdot p_2=Q^2>0$. Lines: $\ell_0=k$ (gluon), $\ell_1=p_1-k$ (quark), $\ell_2=p_2+k$ (antiquark);
Feynman parameters $\alpha_{0,1,2}$:
$$
\mathcal U=\alpha_0+\alpha_1+\alpha_2,\qquad \mathcal F=-\alpha_1\alpha_2\,q^2-\alpha_0\alpha_1p_1^2-\alpha_0\alpha_2p_2^2=-Q^2\alpha_1\alpha_2,\qquad
k_c=\alpha_1p_1-\alpha_2p_2\ \ (\textstyle\sum\alpha=1).
$$
**α-space Landau set** (L3a): $\alpha_1\partial_1\mathcal F=\alpha_2\partial_2\mathcal F=-Q^2\alpha_1\alpha_2=0$, $\partial_0\mathcal F=0$: the
two closed edges $\{\alpha_2=0\}$ and $\{\alpha_1=0\}$ of the triangle. Interpretation via Lemma L2:

* **edge $\alpha_2=0$** ($\alpha_1=x\in[0,1]$): $k=xp_1$, lines 0 and 1 on shell and collinear to $p_1$, the antiquark line
  off shell — the **collinear-to-$p_1$ pinch surface** $C_1$. Loop equation (orientation $X\to Y_2\to Y_1\to X$):
  $\alpha_2(p_2+k)+\alpha_0k+\alpha_1(k-p_1)=0\Rightarrow\alpha_0x=\alpha_1(1-x)$, so $0\le x\le1$ (physical region).
* **edge $\alpha_1=0$**: $k=-yp_2$, $0\le y\le1$ — **collinear-to-$p_2$** surface $C_2$.
* **corner $(1,0,0)$**: $k=0$, all three lines on shell, only $\alpha_0\neq0$ — the **soft point** $S$ (zero-momentum gluon).
* corners $(0,1,0)$, $(0,0,1)$: $k=p_1$ resp. $k=-p_2$ — a zero-momentum *quark* line: the soft-quark endpoints
  ($x=1$, $y=1$) of $C_1$, $C_2$.
* **edge $\alpha_0=0$ and interior: no solution for $Q^2\neq0$** — this is the "hard" configuration (all lines off shell,
  generic $k\sim Q$; in reduced-diagram language: all lines contracted into the **hard point** $H$). The surface
  $\{\ell_1^2=\ell_2^2=0\}$ (the $q\bar q$ two-particle cut) exists for timelike $Q^2$ but is *not* trapped (Theorem L3,
  check L5); it produces the absorptive part, not a singularity. It would be trapped only at $Q^2=0$ (normal threshold;
  Cayley minor $\det Y_{\{12\}}=-Q^4/4$, check L4).

The same list follows directly in momentum space from the one-loop Cayley matrix $Y_{ij}=q_i\cdot q_j|_{\rm on\ shell}$
$=\begin{pmatrix}0&0&0\\0&0&-Q^2/2\\0&-Q^2/2&0\end{pmatrix}$: null vectors of $Y_S$ with $\alpha\ge0$ exist for
$S=\{0\},\{1\},\{2\},\{0,1\},\{0,2\}$ and not for $\{1,2\}$ (L4).

**Coleman–Norton pictures.** $H$: everything at the production point $X$. $C_1$: at $X$ the photon produces the
antiquark ($p_2$) and a collinear quark–gluon pair; quark $(1-x)p_1$ and gluon $xp_1$ fly together along the light ray of
$p_1$ and recombine at $Y_1=X+\alpha_1(1-x)p_1=X+\alpha_0xp_1$ (both arrive simultaneously; the internal antiquark line is
contracted into $X$). $S$: a zero-momentum gluon connecting arbitrary points of the two outgoing light rays.

**Which surfaces give divergences** is decided by power counting (§2): $C_1$, $C_2$, $S$ are logarithmic ($\omega=0$),
overlapping at the corner $S$ $\Rightarrow$ $1/\epsilon^2$; the soft-quark endpoints are suppressed (e.g. for the scalar
integral near $\ell_1=0$ with $\ell_1\sim\lambda^2$: measure $\lambda^8$, $\ell_1^{-2}\sim\lambda^{-4}$, $(p_1-\ell_1)^{-2}\sim\lambda^{-2}$, hard
line $\lambda^0$ $\Rightarrow\lambda^2$; with Dirac numerators $\slashed\ell_1\sim\lambda^2$ even more).

### 1.7 Massless box (brief)

Lines $q_j=k+r_j$, $r_0=0$, $r_1=p_1$, $r_2=p_1+p_2$, $r_3=-p_4$, all $p_i^2=0$, $s=(p_1+p_2)^2$, $t=(p_2+p_3)^2$:
$$
\mathcal F=-s\,\alpha_0\alpha_2-t\,\alpha_1\alpha_3 .
$$
Landau set (L3e): $\alpha_0\alpha_2=\alpha_1\alpha_3=0$, i.e. the four edges $(01),(12),(23),(30)$ of the 3-simplex (two adjacent
lines on shell, collinear to the external momentum entering between them) and their endpoints (four corners =
zero-momentum lines, i.e. soft exchange between two adjacent external legs). The edges $(02)$, $(13)$ ($s$- and
$t$-channel two-particle cuts) are solutions only at $s=0$, resp. $t=0$ (normal thresholds); the leading Landau
singularity (all four lines on shell) requires $\det Y=s^2t^2/16=0$. For the scalar box in $D=4$ each corner and each edge
has $\omega=0$ (power counting as in §2; e.g. soft: $\lambda^8\cdot\lambda^{-4}\lambda^{-2}\lambda^{-2}$; checked numerically, P1b), whence the familiar
$1/\epsilon^2$ IR poles.

### 1.8 Remarks

* **Necessary, not sufficient.** Massless graphs always have the trivial corner solutions. For the *off-shell*
  Euclidean vertex ($\mathcal F=P^2\alpha_0(\alpha_1+\alpha_2)+Q^2\alpha_1\alpha_2$) the Landau set consists of the three corners only
  (L3b); near the soft corner $\mathcal F=rP^2+O(r^2)$ ($r=\alpha_1+\alpha_2$), so $\int r\,dr/r$ converges: no divergence. For
  on-shell *massive* legs with a massless gluon ($\mathcal F=Q^2\alpha_1\alpha_2+m^2(\alpha_1+\alpha_2)^2$) the same corner is the only
  solution (L3d), but now $\mathcal F=r^2(m^2+u(1-u)Q^2)$ and $\int r\,dr/r^2$ diverges logarithmically (the soft IR
  divergence). The Landau solution is identical in both cases; power counting decides (L7).
* **Pinch vs endpoint.** In momentum space there are no endpoints; after partial integrations (light-cone fractions,
  Feynman parameters) the soft region of the momentum integral appears as the endpoint $x\to0$ of the collinear
  surfaces. In α-space, endpoints are automatically part of the Landau conditions (option $\alpha_j=0$).
* **Numerators.** Polynomial numerators give, after the Gaussian integration, extra factors polynomial in $\alpha$ and
  $p$ multiplying $\mathcal U^{a'}\mathcal F^{-b'}$ with shifted powers; the proof of L1 goes through unchanged.
* **Singularities vs divergences.** Theorem L1 concerns analyticity in external invariants (Landau 1959; ELOP 1966)
  and IR finiteness at fixed kinematics; for factorization the relevant objects are the trapped *regions* of
  loop-momentum space at fixed external momenta (Sterman 1978), i.e. Theorem L3 + power counting.

### 1.9 Suggested status tags

T(L1) [R] (proof above, complete for UV-convergent/DR-continued scalar or polynomial-numerator integrals);
L2 [R]; L3 necessity [R]; L3 sufficiency + global deformation [A] (complete proof claimed in Collins 2020, unpublished
preprint); Coleman–Norton algebraic restatement [R], "trap ⇔ classical process" [A] (via Collins 2020).

---------------------------------------------------------------------------------------------------

## 2. Power counting

### 2.1 Normal coordinates and scalings

Near a pinch surface $\mathcal S$ choose intrinsic coordinates (along $\mathcal S$) and normal coordinates $\kappa_i$ (out of
$\mathcal S$); scale $\kappa_i=\lambda^{a_i}\kappa_i'$, keep in each denominator the lowest power $\lambda^{A_j}$, and in numerators
the lowest power $\lambda^{s}$. The homogeneous integral scales as $\lambda^{p}$,
$$
p=\sum_i a_i-\sum_jA_j+s ,\qquad p>0:\ \text{suppressed},\quad p=0:\ \text{logarithmic},\quad p<0:\ \text{power divergent},
$$
(Sterman TASI'95 eqs. (60)–(62), in his units). The bound is complete only after the homogeneous integral itself has
been checked for further pinch surfaces (sub-surfaces where some normal variables vanish faster) — Sterman's step iv.

Region scalings used throughout (light-cone components $(k^+,k^-,k_T)$ for jets along $\pm z$):

| region | scaling | $k^2$ | coupling to an $A$-collinear line $p_A\sim Q(1,\lambda^2,\lambda)$ |
|---|---|---|---|
| hard | $Q(1,1,1)$ | $Q^2$ | — |
| $A$-collinear | $Q(1,\lambda^2,\lambda)$ | $\lambda^2Q^2$ | — |
| $B$-collinear | $Q(\lambda^2,1,\lambda)$ | $\lambda^2Q^2$ | $(p_A+k)^2\sim Q^2$ (hard) |
| soft | $Q(\lambda,\lambda,\lambda)$ | $\lambda^2Q^2$ | $(p_A+k)^2-p_A^2\simeq2p_A^+k^-\sim\lambda Q^2$, eikonal error $O(\lambda)$ |
| ultrasoft (Libby–Sterman "soft") | $Q(\lambda^2,\lambda^2,\lambda^2)$ | $\lambda^4Q^2$ | $\simeq2p_A^+k^-\sim\lambda^2Q^2$, eikonal error $O(\lambda^2)$ |
| Glauber | $Q(\lambda^2,\lambda^2,\lambda)$ | $\simeq-k_T^2\sim\lambda^2Q^2$ | $2p_A^+k^--2\vec p_{AT}\!\cdot\vec k_T-k_T^2\sim\lambda^2Q^2$: **not eikonal** (error $O(1)$) |

The eikonal-error column is check P3 (fitted exponents 1.000, 2.000, 0.000).

### 2.2 Collinear region of the one-loop vertex: logarithmic scaling (explicit)

Massless vertex of §1.6 with $p_1=(p_1^+,0,0_T)$, $p_2=(0,p_2^-,0_T)$, $Q^2=2p_1^+p_2^-$, $x=k^+/p_1^+$:
$$
D_0=2k^+k^--k_T^2,\quad D_1=-2(p_1^+-k^+)k^--k_T^2,\quad D_2=2k^+(p_2^-+k^-)-k_T^2\qquad(\text{each }+i0).
$$
For $0<x<1$ the $k^-$-poles of $D_0$ and $D_2$ lie below the real axis, that of $D_1$ above; for $x<0$ or $x>1$ all three lie
on one side and the $k^-$ integral vanishes (C1, C2). As $k_T\to0$ the $D_0$ pole $k^-=(k_T^2-i0)/(2xp_1^+)$ and the $D_1$ pole
$k^-=-(k_T^2-i0)/(2(1-x)p_1^+)$ approach $k^-=0$ from opposite sides: the collinear pinch. Closing above,
$$
\int_{-\infty}^{\infty}\!dk^-\,\frac{1}{(D_0+i0)(D_1+i0)(D_2+i0)}=\frac{2\pi i}{2p_1^+}\,\frac{1}{k_T^2\big(xQ^2-k_T^2/(1-x)\big)}
\ \xrightarrow{\ k_T\to0\ }\ \frac{2\pi i}{2p_1^+\,xQ^2}\,\frac{1}{k_T^2}
$$
(C3: agreement with direct integration to $<10^{-9}$). Hence $\int d^2k_T/k_T^2$: every shell $\lambda<|k_T|<2\lambda$ contributes
$\pi\ln4\times2\pi i/(2p_1^+xQ^2)$, independent of $\lambda$ (C4) — a logarithmic divergence; the remaining $\int dx/x$ at
$x\to0$ is the soft endpoint and produces the second logarithm. In normal coordinates $k^-=\lambda^2\kappa$, $k_T=\lambda\tau$
($k^+=xp_1^+$ intrinsic): measure $dk^-d^2k_T\sim\lambda^4$, $D_0,D_1\sim\lambda^2$, $D_2\simeq xQ^2\sim\lambda^0$, so $p=4-2-2=0$ (C5,
fitted $|p|<10^{-5}$). The same scaling holds for every region of the *on-shell* massless vertex, collinear, soft,
ultrasoft and Glauber alike (P1; contrasting scalings $(0,1,1)$ and $(2,2,3)$ give $p=1$ and $2$): the on-shell
massless vertex has no intrinsic small scale, which is why all its low-energy regions are scaleless in DR.

*Off-shell vertex* ($p_i^2=-P^2=-\lambda^2Q^2$, task convention, P2): collinear family $(0,2c,c)$ gives $p=0$ for $c\le1$
and $p=2c-2$ for $c\ge1$; soft family $(c,c,c)$ gives $p=0$ for $c\le2$ and $2c-4$ for $c\ge2$. The external virtuality cuts
the collinear logarithm off at $k_T\sim P$ and the soft logarithm at $k\sim P^2/Q$ (the ultrasoft scale). The double
logarithm $\ln^2(Q^2/P^2)$ is the area of the resulting logarithmic domain in the $(\ln k^+,\ln k^-)$ plane.

### 2.3 Sterman's IR degree of divergence: ingredients

Reduced diagram $R$: hard part(s) $H$ (and $H^*$ on the other side of a final-state cut), jets $J$ (collinear to
light-like $\beta_J$), ultrasoft subdiagram $S$ (lines with vanishing momentum). Ingredients in Sterman units:

1. **measure**: soft loop $\lambda_S^4$ (all four components normal); jet loop $\lambda_S^2$ (normal variables $\ell^-\sim\lambda_S$,
   $\ell_T\sim\lambda_S^{1/2}$, i.e. $\ell^2$ and $\ell\cdot\beta_J$ in TASI'95 language);
2. **denominators**: jet lines (quark or gluon) $\lambda_S^{-1}$; soft gluon $\lambda_S^{-2}$; soft quark $\lambda_S^{-1}$ (numerator
   $\slashed k\sim\lambda_S$ included); jet line carrying soft momentum: $(p+k)^2\simeq p^2+2p\cdot k\sim\lambda_S$;
3. **numerators**: Dirac numerators of jet fermion lines and momenta at three-gluon vertices: in a physical gauge each
   three-point vertex internal to a jet costs $\lambda_S^{1/2}$ (Sterman's bound $s'_T\ge\frac12(V_{3,J}+V_{3,J'}-M_J-M_{J'})$,
   TASI'95 eq. 65); in Feynman gauge a gluon connecting a jet to $H$ through its *scalar* polarization ($J^+$ component,
   $k^\mu$-like) costs nothing, because the large $J^+\propto p^+$ is contracted with an $O(1)$ component of $H$;
   soft-gluon–jet vertices are eikonal, $\propto p_J^\mu$, unsuppressed; soft-quark–jet vertices cost $\lambda_S^{1/2}$;
4. **self-energies**: renormalized two-point insertions on jet lines have a single pole, i.e. a $+1$ per insertion relative
   to naive counting (CSS 1989 eq. 122, term $N_2$) — in the derivation below they are automatically included in $\dim J$.

Direct numerical confirmation of item 3 in a concrete case (P4): for $\gamma^*\to q\bar qg$ with the gluon collinear to
the quark, the quark-emission squared numerator scales as $\lambda^{2}$ (it would be $\lambda^0$ term by term: the leading
$\gamma^-\!\dots\gamma^-$ structures cancel), the squared propagator as $\lambda^{4}$, so $|M|^2\sim\lambda^{-2}$ and with the
collinear phase space $\lambda^2$ the region is logarithmic; the same code reproduces
$\sum|M|^2\propto8\,(x_1^2+x_2^2)/((1-x_1)(1-x_2))$ exactly (P4(i)).

### 2.4 Derivation of $\omega(R)$ in Feynman gauge (boost + dimension argument) — superficial degree [R]

Notation for a jet $J$ (collinear to $+z$): lines to $H$ (and $H^*$), *unamputated*: $f$ quark lines, of which $f^g$
contracted with $H$ through "good" ($\gamma^-\gamma^+/2$) spinor components and $f^b$ through "bad" ones; $b$ gluon lines, of
which $b_+$ through the jet component $J^+$ (scalar/longitudinal polarization), $t$ (=$b_T$) transverse, $u$ (=$b_-$) through
$J^-$; soft attachments, *amputated*: $s^g$ gluons, $s^q$ quarks; $e_J=1$ for a jet in an amplitude with one external
on-shell parton, $e_J=2$ for a jet whose external parton enters and leaves (forward amplitude, DIS/DY target jets) or
for a final-state jet of a cut diagram (no external legs, total momentum integrated).

**Lemma (boost scaling).** The jet subgraph is a Lorentz-covariant function of its momenta. Boost along $z$ by rapidity
$y$ with $e^{y}=\lambda$: collinear momenta $Q(1,\lambda^2,\lambda)\to\lambda Q(1,1,1)$ (jet rest frame), ultrasoft momenta
$Q(\lambda^2,\lambda^2,\lambda^2)\to Q(\lambda^3,\lambda,\lambda^2)$, whose dominant ($-$) component is again $\sim\lambda Q$; the jet depends on it only
through $k^-$ at leading power (eikonal coupling). In the rest frame the jet is, at leading power, homogeneous of degree
$\dim J$ (its mass dimension) in momenta $\sim\lambda Q$: $J\sim\lambda^{\dim J}$ (superficially, i.e. up to logarithms from
sub-regions). Boosting back multiplies each upper $+$ index by $\lambda^{-1}$, each $-$ index by $\lambda^{+1}$, transverse
indices by $1$, good spinor components by $\lambda^{-1/2}$, bad ones by $\lambda^{+1/2}$. Numerical check (P5, tilted jet axis):
$|J^+|\sim\lambda^{0.000}$, $|J_T|\sim\lambda^{1.000}$, $|J^-|\sim\lambda^{2.000}$ for $J^\nu=\bar u(p_1)\gamma^\nu(\slashed p_1-\slashed k)$.

**Counting (SCET units $\lambda$).** Mass dimension of an amputated connected Green function in $D=4$:
$4-\sum_{\rm legs}d$ with $d=1$ (gluon), $3/2$ (quark); unamputating adds $-2$ (gluon) or $-1$ (quark); an external spinor
adds $+1/2$, a polarization vector $0$. For $e_J=1$:
$$
\dim J=4-3b-\tfrac52f-s^g-\tfrac32s^q-1,\qquad \#(J\!-\!H\ \text{loops})=b+f-1\ \ (\text{each}\sim\lambda^4),
$$
boost factors $\lambda^{-b_++b_--\frac12f^g+\frac12f^b}$, soft attachments $\lambda^{-s^g-\frac12s^q}$ ($J^+$ resp. good components
contracted with $O(1)$ soft vertices). Hence
$$
p_J=\dim J+4(b+f-1)-b_++b_--\tfrac12f^g+\tfrac12f^b-s^g-\tfrac12s^q
=\big(f^g+t-1\big)+2\big(u+f^b\big)-2\big(s^g+s^q\big).
$$
For $e_J=2$: forward jets have two amputated external legs ($\dim J$ lower by 1) and still $b+f-1$ loops (the momentum
transferred to $H$ is integrated); final-state jets of a cut diagram have no external legs, $b+f-2$ relative loops and the
jet momentum with one normal variable $P_J^2\sim\lambda^2$. Both give $p_J=(f^g+t-2)+2(u+f^b)-2(s^g+s^q)$. Each connected soft
component $a$ with $M_a^{g}$ gluon and $M_a^{q}$ quark external lines (unamputated, momenta $\sim\lambda^2Q$):
$p_{S_a}=2\big(4-3M_a^g-\tfrac52M_a^q\big)+8(M_a-1)=2M_a^g+3M_a^q$. $H$ is $O(1)$. Summing, with
$\sum_aM_a^g=\sum_Js^g_J+b_{S\to H}$, $\sum_aM_a^q=\sum_Js^q_J+f_{S\to H}$:
$$
\boxed{\;\omega(R)=\frac p2=\sum_J\frac12\Big(f_J^{g}+t_J+2u_J+2f_J^{b}-e_J\Big)+\frac12\sum_Js^{q}_J+b_{S\to H}+\frac32f_{S\to H}\;}
$$
(Sterman units; $\omega=0$: logarithmic; the power of $\lambda$ is $2\omega$.) Soft gluons attached to jets cost nothing;
soft quarks attached to jets cost $\frac12$ each; soft gluons (quarks) attached to $H$ cost $1$ ($\frac32$).
This coincides with the architect's formula (outline P3.9) once the bad-component term is added; with $f_J^b=0$ (the
minimum) it is identical.

**Cross-checks (P7).** Table of reduced diagrams (Sudakov soft and collinear: 0; transverse gluon into $H$: $\frac12$;
"$-$" gluon: $1$; three quark lines into $H$: $1$; soft quark exchanged: $1$; soft gluon into $H$: $1$; soft quark into $H$: $2$;
$e^+e^-$ two-jet cut with any number of scalar gluons and soft gluons: $0$; gluon jet with one transverse and only scalar
gluons: $-\frac12$, super-leading). Sterman's direct count, TASI'95 eq. (64)
$n_T=M_J+M_{J'}+2L_J+2L_{J'}-N_J-N_{J'}+s'_T$, $s'_T\ge\frac12(V_{3,J}+V_{3,J'}-M_J-M_{J'})$, gives $n_T=0$ for one soft gluon, the
two-gluon ladder and a $3g\to1g$ soft web (P7) — equal to $\omega$. *Note:* eq. (63) of TASI'95 with
$4(L_S+M_J+M_{J'}-1)$ presupposes a connected $S$; eq. (64) holds for any number $c_S$ of soft components because
$4L_S-2N_S+s_S=\dim S=\sum_a(4-3M_a)$ and the number of soft loops linking $S$ to the jets is $M-c_S$ (my first, naive use
of (63) for the ladder gave a spurious $n_T=4$). CSS 1989 eq. (143),
$\omega=4S+2C-2I_S-I_C+N_2+\frac12N_3+F$, is the physical-gauge version; for configurations with $b_+=0$ both give the same
classification.

**Numerical confirmation of the Feynman-gauge statement (P5).** One-loop vertex numerator
$J^\nu H_\nu$, $J^\nu=\bar u(p_1)\gamma^\nu(\slashed p_1-\slashed k)$, $H_\nu=\gamma^\mu(-\slashed p_2-\slashed k)\gamma_\nu v(p_2)$, in the collinear-1
region: $J^+H^-\sim\lambda^0$; $J^-H^+\equiv0$ ($\bar u(p_1)\gamma^-=0$ for $p_1$ exactly along $+$; and $H^+\propto\gamma^+v(p_2)=0$);
$J_T\!\cdot H_T$ vanishes identically in $D=4$ for exactly back-to-back light-like quarks, because
$\sum_{i=1,2}\gamma^i\gamma^j\gamma^i=0$ in two transverse dimensions ($O(\epsilon)$ in $D$ dimensions) — the bound $\lambda^1$ is
respected, not saturated. Moreover $J\cdot H=(J^+/k^+)\,(k\cdot H)+O(\lambda^2)$: only the scalar ("K-gluon") polarization
survives at leading power, which after the Ward identity yields the Wilson line.

**What is and is not proved.** The formula is the superficial degree of the homogeneous integral, i.e. a theorem about
scaling of integrand and measure near the pinch surface (it uses only Lorentz covariance, dimensional analysis and the
leading-power independence of $H$ of small components) — [R] in that sense. That the full contribution of the region is
bounded by $\lambda^{2\omega}$ times logarithms requires the iterated analysis of nested pinch surfaces (Sterman 1978a for
$e^+e^-$ cut diagrams; Libby–Sterman 1978; Collins 2011 ch. 5) — [A]. In Feynman gauge individual graphs can be
super-leading ($\omega<0$); these terms cancel only in gauge-invariant sums (Ward identities), cf. CSS 1989 §8.6.

### 2.5 Leading regions (Feynman gauge)

Setting $\omega=0$ (and using the Ward-identity cancellation of $\omega<0$ terms):

* **$e^+e^-\to$ hadrons** (cut vacuum polarization; Sterman 1978a): one hard vertex $H$ ($H^*$); final-state jets $J_i$
  ($e=2$); each jet connected to $H$ and to $H^*$ by **exactly one physical parton** on each side of the cut (one good quark
  component, or one transversely polarized gluon) **plus any number of scalar(longitudinally)-polarized gluons**; no
  "$-$"-polarized gluons, no bad components; the ultrasoft subdiagram $S$ is connected to the jets **only by gluons** (soft
  quark loops internal to $S$ allowed) and **never to $H$**.
* **DIS** (forward Compton amplitude / cut): target jet $A$ ($e=2$) with one physical parton on each side + scalar gluons;
  final-state jets and soft lines as above; after summing over final-state cuts the final-state pinches are not trapped
  (inclusive), so the leading region reduces to $H\otimes$(target jet) with soft exchanges absorbed (CSS 1989 §8.7).
* **Drell–Yan**: two incoming jets $A$, $B$ ($e=2$ each), each with one physical parton into $H$ on each side + any number of
  scalar gluons; $S$ connects $A$, $B$ (and final-state spectators), not $H$; in addition the **Glauber region** of
  spectator–spectator exchanges is leading by power counting ($\lambda^0$, §2.6) and is trapped; it cancels only after the
  sum over final-state cuts (CSS 1985, 1988; Bodwin 1985) — [A].

Literature statement (CSS 1989 §8.7, read in hep-ph/0409313): "at leading power only a single line from each jet enters
a given hard subdiagram … in covariant gauges … arbitrary numbers of longitudinally polarized gluons may attach the jet
to the hard part … [soft] external lines are always gluons … always attach to (energetic) lines and not to the hard
subdiagrams … the sum over final states eliminates pinch singularities involving final state jets" — **PASS** (same
rules as derived above).

### 2.6 Glauber vs soft vs ultrasoft

One gluon exchanged between an $A$-collinear and a $B$-collinear line (vertex integrand of §2.2):
soft $\lambda^4\cdot\lambda^{-2}\cdot\lambda^{-1}\cdot\lambda^{-1}$, ultrasoft $\lambda^8\cdot\lambda^{-4}\cdot\lambda^{-2}\cdot\lambda^{-2}$,
Glauber $\lambda^6\cdot\lambda^{-2}\cdot\lambda^{-2}\cdot\lambda^{-2}$: all $\lambda^0$ (P1, fitted). The difference is the eikonal
approximation: valid (error $\lambda$, $\lambda^2$) for soft/ultrasoft, invalid in the Glauber region (P3).
*Trapping.* In the Glauber region $D_1\simeq-2p_1^+k^--k_T^2$ depends only on $k^-$, $D_2\simeq2p_2^-k^+-k_T^2$ only on $k^+$,
$D_0\simeq-k_T^2$ on neither: each light-cone integral sees a single pole, the contour can be moved to $|k^\pm|\sim k_T$
where the eikonal approximation holds (CSS 1989 eq. 138): **the one-loop vertex is not trapped in the Glauber region**.
With an *incoming and an outgoing* $A$-collinear line carrying $k$ (initial- and final-state spectator interactions
in DY), the poles $k^-=-k_T^2/(2p_A^+)+i0$ and $k^-=+k_T^2/(2p_{A'}^+)-i0$ pinch at $|k^-|\sim k_T^2/p^+$; the exact $k^-$
integral is finite, $=2\pi i/[2k_T^2(p_A^++p_{A'}^+)]$, while the eikonal version is singular $\propto1/\varepsilon$ as the
$i0\to0$ (P6): in a trapped Glauber region the eikonal approximation cannot be used and a separate cancellation
argument is needed. (With analytic regularization the Glauber region of the vertex gives a scaleless integral; BBF
2015 §2.2 leave this as an exercise; Jantzen 2011 App. A.3.1 shows it explicitly for the massive-exchange case.)

### 2.7 Suggested status tags

Superficial degree formula [R] (as a scaling statement); bound on actual contributions incl. nested regions [A];
leading-region theorem for $e^+e^-$, DIS, DY [A]; Glauber cancellation in DY [A] with known gaps for
non-inclusive observables (Ch. 10/12).

---------------------------------------------------------------------------------------------------

## 3. Method of regions

### 3.1 Prescription (Beneke–Smirnov 1998)

(i) Choose regions (scalings of loop momenta, or of Feynman parameters); (ii) in each region Taylor-expand the integrand
in the quantities that are small there; (iii) integrate every expanded term over the **whole** integration domain in
dimensional regularization (with auxiliary analytic regulators where DR does not regularize); (iv) set scaleless
integrals to zero; (v) sum over regions. Requirements: every expanded integral must be regularized; the set of regions
must be complete; overlap contributions (multiple expansions) must vanish or be subtracted (§3.3).

### 3.2 Off-shell (Euclidean) Sudakov form factor — the main example

$$
I=e^{\epsilon\gamma_E}\mu^{2\epsilon}\!\int\!\frac{d^Dk}{i\pi^{D/2}}\frac{1}{(-k^2-i0)\,(-(k+p_1)^2-i0)\,(-(k+p_2)^2-i0)},\qquad
p_1^2=p_2^2=-P^2,\ \ (p_1-p_2)^2=-Q^2,\ \ t\equiv P^2/Q^2\ll1 .
$$
Feynman parameters: $\mathcal F=P^2\alpha_0(\alpha_1+\alpha_2)+Q^2\alpha_1\alpha_2>0$, so $I$ is real and finite in $D=4$:
$$
Q^2I\big|_{\epsilon=0}=\int_0^1\!du\,\frac{\ln\!\big(u(1-u)/t\big)}{u(1-u)-t}=\Phi^{(1)}(t,t),
$$
where $\Phi^{(1)}(x,y)=\lambda^{-1}\{2[{\rm Li}_2(-\rho x)+{\rm Li}_2(-\rho y)]+\ln\frac yx\ln\frac{1+\rho y}{1+\rho x}+\ln(\rho x)\ln(\rho y)+\frac{\pi^2}3\}$,
$\lambda=\sqrt{(1-x-y)^2-4xy}$, $\rho=2/(1-x-y+\lambda)$ is the Usyukina–Davydychev function (Phys. Lett. B 298 (1993) 363;
B 305 (1993) 136; bibliographic data verified on INSPIRE; the *formula* as written here is from memory and is verified
numerically: agreement $<10^{-20}$ at $t=10^{-1},10^{-2},10^{-4},10^{-8}$ and at the asymmetric point $(0.02,0.05)$, check A1).
*Kinematics remark.* With all invariants negative the parametric polynomial is positive, but the limit $Q^2\gg P^2$ cannot
be realized with Euclidean external vectors ($|p_1-p_2|^2\le4P^2$ there); real momenta are Minkowskian and space-like,
$p_1=(p_1^+,-P^2/2p_1^+,0_T)$, $p_2=(-P^2/2p_2^-,p_2^-,0_T)$, $2p_1^+p_2^-=Q^2+O(P^2)$. This is why the Sudakov limit is not
covered by the Euclidean large-momentum theorems (§3.9).

**Regions** (light-cone frame above; $\lambda^2\sim t$):

| region | scaling of $k$ | expanded denominators | value $\times Q^2$ |
|---|---|---|---|
| hard $H$ | $Q(1,1,1)$ | $-k^2,\ -(k^2+2k\cdot\hat p_1),\ -(k^2+2k\cdot\hat p_2)$, $\hat p_i^2=0$ | $\big(\tfrac{\mu^2}{Q^2}\big)^{\epsilon}e^{\epsilon\gamma_E}\dfrac{\Gamma(1+\epsilon)\Gamma^2(-\epsilon)}{\Gamma(1-2\epsilon)}$ |
| collinear-1 $C_1$ | $Q(1,\lambda^2,\lambda)$ | $-k^2,\ -(k+p_1)^2,\ -2p_2^-k^+$ | $-\big(\tfrac{\mu^2}{P^2}\big)^{\epsilon}e^{\epsilon\gamma_E}\dfrac{\Gamma(1+\epsilon)\Gamma^2(-\epsilon)}{\Gamma(1-2\epsilon)}$ |
| collinear-2 $C_2$ | $Q(\lambda^2,1,\lambda)$ | $-k^2,\ -2p_1^+k^-,\ -(k+p_2)^2$ | same as $C_1$ |
| ultrasoft $S$ | $Q(\lambda^2,\lambda^2,\lambda^2)$ | $-k^2,\ -(2p_1^+k^--P^2),\ -(2p_2^-k^+-P^2)$ | $-\big(\tfrac{\mu^2Q^2}{P^4}\big)^{\epsilon}e^{\epsilon\gamma_E}\Gamma(1+\epsilon)\Gamma(\epsilon)\Gamma(-\epsilon)$ |
| soft $(\lambda,\lambda,\lambda)$ | | $-k^2,\ -2p_1^+k^-,\ -2p_2^-k^+$ | $0$ (scaleless) |
| Glauber $(\lambda^2,\lambda^2,\lambda)$ | | $k_T^2,\ -(2p_1^+k^--k_T^2-P^2),\ \dots$ | $0$ with an analytic regulator (each $k^\pm$ integral has one pole; not trapped) |

*Derivations (momentum space).* $C_1$: combine $-k^2$ and $-(k+p_1)^2$ with a Feynman parameter $x$, shift
$\ell=k+xp_1$, combine with the linear denominator $-2p_2^-k^+=-2p_2^-\ell^++xQ^2$ via $1/(A^2B)=2\int_0^\infty d\eta\,(A+\eta B)^{-3}$; the
$\ell^+$-linear term is absorbed by a light-like shift ($\ell\to\ell+\eta p_2^-v$, $v\cdot\ell=\ell^+$, $v^2=0$), leaving
$\Gamma(1+\epsilon)\int_0^1\!dx\int_0^\infty\!d\eta\,[x(1-x)P^2+\eta xQ^2]^{-1-\epsilon}=\Gamma(1+\epsilon)\frac{(P^2)^{-\epsilon}}{\epsilon Q^2}\int_0^1dx\,x^{-1-\epsilon}(1-x)^{-\epsilon}$.
The $\eta$ integral requires ${\rm Re}\,\epsilon>0$, the $x$ integral ${\rm Re}\,\epsilon<0$ (the soft end $x\to0$ is regulated by DR): no common
strip, the factorized form defines the region by analytic continuation (both factors checked numerically in their
strips, A2). $S$: two Schwinger parameters for the two linear denominators, $-k^2-2\eta_1p_1^+k^--2\eta_2p_2^-k^+=-(k+\eta_1p_1^+u+\eta_2p_2^-v)^2+\eta_1\eta_2Q^2$
($u\cdot k=k^-$, $v\cdot k=k^+$, $u\cdot v=1$), giving $\Gamma(1+\epsilon)\!\int\!\!\int d\eta_1d\eta_2[\eta_1\eta_2Q^2+(\eta_1+\eta_2)P^2]^{-1-\epsilon}$, convergent for
$0<{\rm Re}\,\epsilon<1$. $H$ is the on-shell massless triangle. The same closed forms follow from the parametric
representation (Cheng–Wu $\alpha_0=1$): $C_1\leftrightarrow\alpha_2\sim t$, $S\leftrightarrow\alpha_1,\alpha_2\sim t$ (A2, A5).
**Literature: identical to BBF 2015 eqs. (2.39), (2.41), (2.43)** after removing the factor $e^{\epsilon\gamma_E}$ (A2; BBF's
$I=i\pi^{-d/2}\mu^{4-d}\int d^dk/[(k^2+i0)((k+l)^2+i0)((k+p)^2+i0)]$ equals our $I/e^{\epsilon\gamma_E}$).

**Laurent expansions** ($\mu=Q$, $L=\ln(P^2/Q^2)$, A3):
$$
\begin{aligned}
Q^2H&=\frac1{\epsilon^2}-\frac{\pi^2}{12}-\frac73\zeta_3\,\epsilon+O(\epsilon^2),\\
Q^2C_{1}=Q^2C_2&=-\frac1{\epsilon^2}+\frac{L}{\epsilon}-\frac{L^2}2+\frac{\pi^2}{12}+\epsilon\Big(\frac{L^3}6-\frac{\pi^2L}{12}+\frac73\zeta_3\Big)+O(\epsilon^2),\\
Q^2S&=\frac1{\epsilon^2}-\frac{2L}{\epsilon}+2L^2+\frac{\pi^2}4+\epsilon\Big(-\frac43L^3-\frac{\pi^2L}2-\frac{\zeta_3}3\Big)+O(\epsilon^2),
\end{aligned}
$$
$$
\boxed{\;Q^2\,(H+C_1+C_2+S)=\ln^2\frac{Q^2}{P^2}+\frac{\pi^2}3+\epsilon\Big(-L^3-\frac{2\pi^2}3L+2\zeta_3\Big)+O(\epsilon^2)\;}
$$
(the $O(\epsilon)$ term for $\mu=Q$; for general $\mu$ multiply by $(\mu^2/Q^2)^\epsilon$). **Pole cancellation:** $1/\epsilon^2$:
$1-2+1=0$; $1/\epsilon$: with general $\mu$, $\ln\frac{\mu^2}{Q^2}-2\ln\frac{\mu^2}{P^2}+\ln\frac{\mu^2Q^2}{P^4}=0$. The poles of $H$ are IR (soft and
collinear poles of the on-shell triangle), those of $S$ are UV (BBF eq. 2.45), and $C_i$ carry both; the IR poles of the
hard region are cancelled by the UV poles of the low-energy regions — the general mechanism behind matching and IR
pole structure. Constants (μ=Q): $-\frac{\pi^2}{12}+2\cdot\frac{\pi^2}{12}+\frac{\pi^2}4=\frac{\pi^2}3$.
**Literature: BBF 2015 eq. (2.44)** $I=\frac1{Q^2}[\ln\frac{Q^2}{L^2}\ln\frac{Q^2}{P^2}+\frac{\pi^2}3]$ (their $L^2=-l^2$ is our second
virtuality) — **PASS**; and $=Q^{-2}\Phi^{(1)}(t,t)$ at leading power — **PASS** (A1, A4: $(I-{\rm LP})/(t\ln^2t)\to2$).
For unequal virtualities the same regions give $\frac1{Q^2}[\ln\frac{Q^2}{P_1^2}\ln\frac{Q^2}{P_2^2}+\frac{\pi^2}3]$ (A1 asymmetric point).

**Beyond leading power** (A5): expanding each region to higher order in the parametric representation,
$$
Q^2I=L^2+\frac{\pi^2}3+t\Big(2L^2+4L-4+\frac{2\pi^2}3\Big)+t^2\big(6L^2+14L-11+2\pi^2\big)+O(t^3L^2),
$$
with the NLP and NNLP coefficients from the regions identical to those of the expansion of $\Phi^{(1)}(t,t)$; their
$1/\epsilon^2$, $1/\epsilon$ poles cancel separately at each power; the numerical remainder after NNLP is $O(t^3\ln^2t)$.
**$O(\epsilon)$ check** (A6): the exact $O(\epsilon)$ coefficient, $-\int_\Delta\ln\mathcal F/\mathcal F
=-\int_0^1du\,[{\rm Li}_2(-(a-t)/t)/(a-t)+(\ln^2a-\ln^2t)/(2(a-t))]$ ($a=u(1-u)$), agrees with the regions at
$t=10^{-4},10^{-6},10^{-8}$ up to $O(t\ln^3t)$: the regions reproduce the full $\epsilon$-dependence at leading power, not only
the finite part.

### 3.3 Overlaps, zero-bin, and Jantzen's conditions

All pairwise overlap contributions are scaleless (A7). In parameter space: $T_{S}T_{C_1}$ gives
$\int_0^\infty dx_1x_1^{-1-\epsilon}\int_0^\infty dx_2(t+x_2)^{-1-\epsilon}=0$; $T_{C_1}T_H$ gives $\int_0^\infty dx_2\,x_2^{-1-\epsilon}=0$; $T_{C_2}T_{C_1}$ and
$T_ST_H$ likewise. In momentum space, e.g. $T_ST_{C_1}$: $\int d^Dk/[(-k^2)(-2p_1^+k^-+P^2)(-2p_2^-k^+)]$ leads to
$\int_0^\infty d\eta_1\eta_1^{-1-\epsilon}\int_0^\infty d\eta_2(\eta_2Q^2+P^2)^{-1-\epsilon}=0$. Hence no zero-bin subtractions are needed in DR
(Manohar–Stewart 2007 zero-bin = expansion of a collinear integrand about the soft limit; BBF 2015 §2.2 make the
same point). Jantzen (2011, §3) derives the method from a partition of the integration domain into domains $D_x$ on
which the expansions $T^{(x)}$ converge absolutely, under four conditions (quoted from the paper): **1.** the domains are
non-intersecting and cover the integration domain; **2.** all expansions commute ($T^{(x)}T^{(x')}=T^{(x')}T^{(x)}$; relaxed in
his §5); **3.** the original integral and all integrals over expanded terms, restricted or not, are regularized;
**4.** the expansions converge absolutely (or are properly regularized) when integrated over the whole domain. The
result is $I=\sum_xT^{(x)}I-\sum_{x<x'}T^{(x)}T^{(x')}I+\dots$; with DR the overlap terms are normally scaleless.
*1D illustration* (Part D): $I=\int_0^\infty dk/[(k+m)(k+M)]$; with the regulator $k^{-e}$:
$T_s+T_h=\frac{m^{-e}\Gamma(e)\Gamma(1-e)}M+M^{-1-e}\Gamma(-e)\Gamma(1+e)\to\frac{\ln(M/m)}M$ and $T_sT_h=\int k^{-1-e}/M=0$; with explicit cutoffs
$[10^{-12},10^{12}]$ instead, $T_s+T_h$ double-counts ($62.17$ instead of $6.908$) and only $T_s+T_h-T_sT_h$ reproduces the leading
power — the zero-bin subtraction.

### 3.4 Parameter space: regions = facets of the Newton polytope

With $\alpha_0=1$, $\mathcal U\mathcal F=(1+x_1+x_2)\,(t(x_1+x_2)+x_1x_2)$ ($Q^2=1$). The lower facets of its Newton polytope (normal
vectors with positive $t$-component; Pak–Smirnov 2011) give $x_i\sim t^{r_i}$ with $r\in\{(0,0),(0,1),(1,0),(1,1)\}$ = hard,
$C_1$, $C_2$, $S$ (A8, scipy ConvexHull). For the massive exchange (§3.5) the facets are $\{(0,0),(0,1),(1,0)\}$ only; the
soft weight $(\frac12,\frac12)$ is minimized on an *edge* (two points), not a facet — the geometric signature of the
rapidity degeneracy that forces analytic regularization (B4).

### 3.5 On-shell massless legs with a massive exchange: analytic regulators needed

$$
I_M=e^{\epsilon\gamma_E}\mu^{2\epsilon}\!\int\!\frac{d^Dk}{i\pi^{D/2}}\frac{1}{(-k^2+M^2)\,(-(k+p_1)^2)^{1+\delta_1}\,(-(k+p_2)^2)^{1+\delta_2}},\quad
p_i^2=0,\ (p_1-p_2)^2=-Q^2,\ t=M^2/Q^2 .
$$
(This is the "on-shell massless case" of the task: massless on-shell quarks, IR regulated by a gauge-boson mass; it is
Jantzen 2011 §6 and BBF 2015 §2.3; with a massless exchange the on-shell integral has no low-energy scale at all,
§3.7.) **Exact** at $\delta_i=0$, $\epsilon=0$ (Jantzen eq. 6.30 with $I_M=-F$, verified numerically to $<10^{-10}$, B1):
$$
Q^2I_M=\frac12\ln^2\frac{Q^2}{M^2}+\ln\frac{Q^2}{M^2}\ln\Big(1-\frac{M^2}{Q^2}\Big)-{\rm Li}_2\Big(\frac{M^2}{Q^2}\Big)+\frac{\pi^2}3
\ \xrightarrow{\rm LP}\ \frac12\ln^2\frac{Q^2}{M^2}+\frac{\pi^2}3 .
$$
**Regions** (parametric form, $\nu=3+\delta_1+\delta_2$, $\alpha_0=1$, $\mathcal F=t(1+x_1+x_2)+x_1x_2$; $Q^2=\mu=1$; restore dimensions by
$(\mu^2)^\epsilon$):
$$
\begin{aligned}
H&=e^{\epsilon\gamma_E}\,\frac{\Gamma(1+\delta_1+\delta_2+\epsilon)\,\Gamma(-\epsilon-\delta_1)\,\Gamma(-\epsilon-\delta_2)}{\Gamma(1+\delta_1)\,\Gamma(1+\delta_2)\,\Gamma(1-2\epsilon-\delta_1-\delta_2)}
\qquad(\text{massless on-shell triangle, regular at }\delta_i\to0),\\
C_1&=e^{\epsilon\gamma_E}\frac{\Gamma(1+\delta_1+\delta_2+\epsilon)}{\Gamma(1+\delta_1)\Gamma(1+\delta_2)}\;t^{-\delta_1-\epsilon}\;
B(1+\delta_2,\epsilon+\delta_1)\,B(\delta_1-\delta_2,\,1-\epsilon-\delta_1),\qquad C_2=C_1\big|_{\delta_1\leftrightarrow\delta_2}.
\end{aligned}
$$
(From $\int_0^\infty\!\!\int_0^\infty dx_1dx_2\,x_1^{a-1}x_2^{b-1}(1+x_1+x_2)^{-c}=\Gamma(a)\Gamma(b)\Gamma(c-a-b)/\Gamma(c)$ with $a=-\epsilon-\delta_2$, $b=-\epsilon-\delta_1$,
$c=1-2\epsilon-\delta_1-\delta_2$, $c-a-b=1$; at $\delta_i=0$ it is the $H$ of §3.2. Restoring dimensions: $H\propto(\mu^2)^\epsilon(Q^2)^{-1-\epsilon-\delta_1-\delta_2}$,
$C_1\propto(\mu^2)^\epsilon(M^2)^{-\epsilon-\delta_1}(Q^2)^{-1-\delta_2}$; with a regulator scale $\nu$ multiply by $\nu^{2(\delta_1+\delta_2)}$.)
*Pure DR fails* (B2): at $\delta_1=\delta_2$ the factor $B(\delta_1-\delta_2,\cdot)\propto\Gamma(\delta_1-\delta_2)$ is singular for every $\epsilon$ — in momentum
space $C_1=e^{\epsilon\gamma_E}\Gamma(1+\epsilon)\int_0^1dx\,[(1-x)M^2]^{-\epsilon}/(\epsilon xQ^2)$ with an unregulated $\int dx/x$ (rapidity divergence).
*Soft region* $k\sim M$: $\int dx_1dx_2\,x_1^{\delta_1}x_2^{\delta_2}(t+x_1x_2)^{-\nu+D/2}$ is invariant under $x_1\to\kappa x_1$, $x_2\to x_2/\kappa$ up to
$\kappa^{\delta_1-\delta_2}$: zero for $\delta_1\neq\delta_2$, undefined for $\delta_1=\delta_2$ (equivalently: under the boost $k^\pm\to\kappa^{\pm1}k^\pm$ the
eikonal integrand picks up $\kappa^{\delta_1-\delta_2}$). Glauber and Jantzen's auxiliary "collinear-plane" region are scaleless
(Jantzen App. A.3.1). Results (B3):

* Jantzen's choice $\delta_1=-\delta_2=\delta$: $C_1=(\frac{\mu^2}{M^2})^{\epsilon}(\frac{Q^2}{M^2})^{\delta}\frac{e^{\epsilon\gamma_E}\Gamma(\epsilon+\delta)\Gamma(1-\epsilon-\delta)\Gamma(2\delta)}{Q^2\,\Gamma(1-\epsilon+\delta)\Gamma(1+\delta)}$
  **= $-F^{(1c)}$ of Jantzen eq. (6.27) at leading power (exactly)**; the $1/\delta$ poles cancel in $C_1+C_2$, and
  $\lim_{\delta\to0}(C_1+C_2)=\frac1{Q^2}(\frac{\mu^2}{Q^2})^\epsilon[-\frac1{\epsilon^2}+\frac12\ln^2\frac{Q^2}{M^2}+\frac{5\pi^2}{12}]+O(\epsilon)$ **= Jantzen (6.29) at LP**.
* BBF's single regulator ($\delta_1=0$, $\delta_2=\alpha$, factor $\nu^{2\alpha}$): the bracket of the region collinear to the
  regulated line is $\frac1{\alpha\epsilon}-\frac1{\epsilon^2}+\frac{\pi^2}3$, that of the other $-\frac1{\alpha\epsilon}+\frac{\pi^2}6$ (with BBF's prefactors
  $(\nu^2/M^2)^\alpha$, $(\nu^2/Q^2)^\alpha$ and $\Gamma(1+\epsilon)(\mu^2/M^2)^\epsilon/Q^2$ removed) **= BBF eq. (2.50)**.
* Both choices: $H+C_1+C_2=\frac1{Q^2}\big[\frac12\ln^2\frac{Q^2}{M^2}+\frac{\pi^2}3\big]$ **= Jantzen (6.30), BBF (2.52) at LP — PASS**; the
  analytic regulator must be removed *before* $\epsilon\to0$ (BBF).

The sum $C_1+C_2$ depends on $\ln(Q^2/M^2)$ although each collinear integral, before regularization, knows only one
light-cone direction and $M$: the regulator breaks boost invariance and the large logarithm reappears through the
cancellation of the $1/\delta$ poles — the "collinear anomaly" of Becher–Neubert (2011) [their analysis is for $q_T$
factorization; the analogy is drawn in BBF §2.3].

### 3.6 On-shell massive legs with a massless gluon: pure DR suffices

$p_i^2=m^2$, internal quarks of mass $m$, massless gluon, $(p_1-p_2)^2=-Q^2$, $t=m^2/Q^2$: $\mathcal F=Q^2\alpha_1\alpha_2+m^2(\alpha_1+\alpha_2)^2$.
**Exact, all orders in $\epsilon$ and $m$** ($\rho=\alpha_1+\alpha_2$, $\alpha_1=\rho u$): 
$$
I_m=-\frac{e^{\epsilon\gamma_E}\Gamma(1+\epsilon)}{2\epsilon}\,\mu^{2\epsilon}\!\int_0^1\!du\,\big[m^2+u(1-u)Q^2\big]^{-1-\epsilon}
$$
(single pole: the soft IR divergence). **Regions:** $H$ as in §3.2; $C_1=C_2=-\frac1{Q^2}(\frac{\mu^2}{m^2})^\epsilon\frac{e^{\epsilon\gamma_E}\Gamma(1+\epsilon)}{2\epsilon^2}$, finite
Gamma functions — the soft end of the collinear integral is $\int dx\,x^{-1-2\epsilon}$, regulated by DR; soft region scaleless.
Sum ($\mu=Q$, $L=\ln(m^2/Q^2)$): $\frac1{Q^2}[\frac L\epsilon-\frac{L^2}2-\frac{\pi^2}6]$, reproducing the exact single pole and finite part at
leading power (C1, checked at $t=10^{-3},10^{-5},10^{-7}$). **Hence DR alone separates the regions when the exchanged
boson is massless, even for on-shell massive legs; analytic regulators are needed when the exchanged boson is massive
(§3.5), with massless or massive legs.** (For massive legs and massive boson, $\mathcal F|_{C_1}$ contains $x_0M^2+x_1^2m^2$, whose
$x_1\to0$ limit is not regulated.)

### 3.7 On-shell massless legs, massless exchange

$\mathcal F=Q^2\alpha_1\alpha_2$: the integral *is* its hard region,
$I=\frac1{Q^2}(\frac{\mu^2}{Q^2})^\epsilon e^{\epsilon\gamma_E}\Gamma(1+\epsilon)\Gamma^2(-\epsilon)/\Gamma(1-2\epsilon)$; all low-energy regions are scaleless. Its IR poles
are, in region language, the UV poles of scaleless soft/collinear integrals ($\frac1{\epsilon_{UV}}-\frac1{\epsilon_{IR}}=0$) —
the standard bookkeeping by which on-shell IR poles are matched to UV poles of effective operators.

### 3.8 QCD-like vertex at leading-logarithmic accuracy

Space-like form factor (incoming $p_1$, outgoing $p_2$, $q=p_2-p_1$, $q^2=-Q^2$), Feynman gauge, one loop. With the
eikonal numerator $\gamma^\nu\slashed p_2\gamma^\mu\slashed p_1\gamma_\nu=-2\slashed p_1\gamma^\mu\slashed p_2\to4p_1\!\cdot\!p_2\,\gamma^\mu$
between nearly on-shell spinors, $\Lambda^\mu=-ie\gamma^\mu\delta F$ with
$$
\delta F_{\rm LL}=-\frac{\alpha}{\pi}\,p_1\!\cdot\!p_2\,I\ \Rightarrow\
\delta F_{\rm LL}=-\frac{\alpha}{2\pi}\ln\frac{Q^2}{P_1^2}\ln\frac{Q^2}{P_2^2}\ (\text{off-shell}),\qquad
-\frac{\alpha}{4\pi}\ln^2\frac{Q^2}{M^2}\ (\text{on-shell, photon mass }M),
$$
(using $2p_1\cdot p_2\simeq Q^2$ and the leading-power triangles of §3.2, §3.5; single logarithms and constants need the full
numerator). **Literature:** Collins 1989 (hep-ph/0312336, text around his eq. 24) quotes Sudakov's off-shell result
$F\sim\exp[-(g^2/8\pi^2)\ln^2Q^2]$ and Jackiw's on-shell massive-photon result $F\sim\exp[-(g^2/16\pi^2)\ln^2Q^2]$; with
$g^2=4\pi\alpha$ these are $-\frac\alpha{2\pi}$ and $-\frac\alpha{4\pi}$ — **PASS** (Sudakov's and Jackiw's original papers not consulted;
Collins' quote is schematic in the argument of the logarithm). For QCD $\alpha\to C_F\alpha_s$ at one loop. For on-shell massless
quarks the same numerator times the hard region gives $\frac{\alpha_sC_F}{4\pi}(\frac{\mu^2}{Q^2})^\epsilon(-\frac2{\epsilon^2}+\dots)$, the known double pole
of the one-loop quark form factor.

### 3.9 Status of proofs of the method of regions (careful)

* **Euclidean-type limits** (large external momenta that are Euclidean, large masses): the expansion by regions coincides
  with the *expansion by subgraphs* (Chetyrkin 1988; Gorishnii 1989; Smirnov 1990 CMP 134, 109), which is proven;
  SSS 2019 call this "only an indirect proof of expansion by regions, for limits typical of Euclidean space" — **[R]** for
  that class.
* **General (Minkowskian) limits** — threshold, Sudakov, Regge, on-shell expansions: **no general proof** **[P]**.
  - Jantzen 2011: derivation from a partition of the integration domain under the four conditions of §3.3, plus a
    generalization for non-commuting expansions; demonstrated on one-loop examples including the massive Sudakov form
    factor. SSS 2019 (Introduction) judge that this analysis "can hardly be considered as a base of mathematical proofs"
    because inequalities defining domains are not meaningful for dimensionally regularized integrals.
  - Pak–Smirnov 2011: regions = facets of the Newton polytope (algorithm `asy`); SSS 2019: "there is no mathematical
    justification of this procedure", it "works consistently at least in the case where all the terms in the function F
    are positive"; for terms of both signs (potential, Glauber regions) extra variable changes are needed (Jantzen–Smirnov–
    Smirnov 2012).
  - Semenova–Smirnov–Smirnov 2019 (Lee–Pomeransky representation, polynomials with positive coefficients): prove the
    prescription for the leading-order contribution *of each facet*, and the full expansion to all orders *when only one
    facet contributes*; that the leading order of the integral equals the *sum* over facets is reduced to an unproven
    commutativity of expansion and analytic continuation in the regulators ("we believe … and hope that this property can
    be proven"). Even the off-shell Sudakov example (four facets, positive $\mathcal F$) is therefore not covered by a complete
    proof; it is verified here exactly at one loop (and to NNLP).
  - Gardi–Herzog–Jones–Ma–Schlenk 2022 (JHEP 07 (2023) 197): for the on-shell expansion of off-shell massless Green
    functions, regions ↔ Landau solutions ↔ Newton-polytope facets, a graph-finding algorithm, and a proof that multiple
    on-shell expansions commute for regions in which every connected soft subgraph connects just two jets (all
    Sudakov-form-factor regions). Ma 2023/2024: graph-theoretic region identification for wide-angle scattering.
  - Smirnov 1999 ("Problems of the strategy of regions"): two-loop examples of the difficulties; new regions can appear
    at higher loops (BBF §2.2).
* **Regularization.** When DR does not regularize the regions (massive exchange, $q_T$-type observables), auxiliary analytic
  regulators are required; individual regions then depend on the regulator, only the sum does not
  (Jantzen §6; BBF §2.3; Becher–Bell 2012; Chiu–Jain–Neill–Rothstein 2012 rapidity regulator).
* **Use in factorization proofs.** The method of regions is a computational tool and a cross-check; the identification of
  leading regions for all-order factorization must come from Landau/pinch analysis + power counting (§§1–2), otherwise the
  argument is circular in Minkowski kinematics (critic C5) — agreed.

---------------------------------------------------------------------------------------------------

## 4. Discrepancies and corrections (CONTEXT / outline v0 / architect / critic)

1. **Critic O11 (and architect's Ch3 example table): "on-shell massive form factor ($m^2\ll Q^2$): pure DR fails to
   regulate the collinear regions separately" — incorrect as stated.** For on-shell *massive quarks with a massless
   gluon* the collinear integrals are DR-regulated (soft end $\int dx\,x^{-1-2\epsilon}$), the soft region is scaleless, and
   hard + 2 collinear reproduce the exact result including its soft IR pole (§3.6, check C1). Pure DR fails when the
   **exchanged boson is massive** ($M\neq0$), with massless *or* massive legs — the electroweak-Sudakov / SCET$_{\rm II}$
   situation (§3.5; Jantzen 2011 §6; BBF 2015 §2.3; check B2). Correction: pair the off-shell example with the
   *massive-exchange* (or gluon-mass-regulated on-shell massless) form factor.
2. **Architect E3.19 attributes the off-shell Sudakov example to Beneke–Smirnov 1998.** That paper introduces the
   method for the *threshold* expansion (abstract verified); the off-shell Sudakov example by regions with exactly our
   kinematics is BBF 2015 §2.2 (verified), the massive-exchange version Jantzen 2011 §6 and BBF §2.3 (verified).
   Suggested citation: "method: Beneke–Smirnov 1998; this example: BBF 2015; cf. Smirnov 2002/2012".
3. **Architect E3.19 normalization:** "$q^2C_0\to\ln\frac{p_1^2}{q^2}\ln\frac{p_2^2}{q^2}+\frac{\pi^2}3$" is correct if $C_0$ is defined with
   Minkowski propagators $(k^2-m^2)$ and measure $d^Dk/(i\pi^{D/2})$ (LoopTools-like), because then $C_0=-I$ and
   $q^2=-Q^2$ give $q^2C_0=Q^2I$; state this explicitly in the text.
4. **Architect P3.9 formula** agrees with my derivation for good spinor components; add the bad-component term
   ($+f_J^{b}$ in Sterman units) or state that $f_J$ counts good components (the minimum). Its "Proof: full (App. E)"
   should be qualified: the boost/dimension argument proves the *superficial* degree [R]; the bound on actual
   contributions including nested regions is [A].
5. **Architect T3.2/T3.3/T3.5:** keep the α-space theorem [R] as a statement about singularities in external
   parameters and IR finiteness; do **not** claim that α-space pinches coincide with momentum-space pinches (fails for
   massless graphs, Collins 2020 App. D1). Momentum-space necessity [R] via Gordan; sufficiency and global deformation
   [A] (Collins 2020, unpublished). Coleman–Norton: the algebraic restatement is [R]; "trap ⇔ classical process" [A].
6. **Sterman TASI'95 eq. (63)** presupposes a connected soft subdiagram (the term $4(L_S+M_J+M_{J'}-1)$); for
   disconnected $S$ (e.g. the two-gluon ladder) use eq. (64), which follows for any number of components. Not an error
   of the source, but a trap for the writer.
7. **Glauber region of the Sudakov vertex:** it is power-counting leading ($\lambda^0$) but *not trapped*; textbooks
   sometimes describe the timelike vertex's $i\pi$ terms as "Glauber/Coulomb" contributions — after contour deformation
   they are reproduced by the eikonal (soft) region with the correct $i0$ (Wilson-line) directions. With analytic
   regularization the Glauber region integral of the vertex vanishes.
8. **Euclidean vs Minkowski for the off-shell Sudakov limit:** although all invariants are negative ($\mathcal F>0$), the
   limit cannot be realized with Euclidean external vectors, so it is *not* covered by the Euclidean large-momentum
   theorems; and SSS 2019 do not prove the multi-facet case. Status [P], verified exactly at one loop.
9. No discrepancies found with the binding conventions of `CONTEXT.md` for this material (metric, light-front
   conventions, $D=4-2\epsilon$, rapidity). Note for the writer: Becher–Broggio–Ferroglia use $p^\pm$ for $n\cdot p$, $\bar n\cdot p$
   (factor $\sqrt2$ relative to CONTEXT's $v^\pm$); our formulas use CONTEXT's $v^\pm$ throughout.

## 5. References used (all bibliographic data verified)

*In shared `refs.bib`:* Landau1959; ColemanNorton1965; EdenEtAl1966; Sterman1978a; Sterman1978b; LibbySterman1978a;
LibbySterman1978b; CollinsSterman1981; Sen1983; Sudakov1956; BenekeSmirnov1998; Jantzen2011; Smirnov2002;
BecherBroggioFerroglia2015; ManoharStewart2007; IdilbiMehen2007; ChiuEtAl2012b; RothsteinStewart2016;
CollinsSoperSterman1983/1985b/1988/1989; Bodwin1985; Collins2011; Sterman1993; LowensteinZimmermann1975.
*In the survey table (`survey/verified_refs_table.tsv`):* Collins2020Landau (arXiv:2007.04085, no journal publication);
PakSmirnov2011; SemenovaSmirnovSmirnov2019; JantzenSmirnovSmirnov2012; GardiEtAl2022 (JHEP 07 (2023) 197);
Ma2023regions (JHEP 09 (2024) 197); Smirnov1990CMP; Smirnov1999; BecherNeubert2011; Collins1989Sudakov
(hep-ph/0312336); Muhlbauer2020; AnanthanarayanEtAl2019.
*Verified here on INSPIRE (2026-10-09), not in the shared lists:* Usyukina & Davydychev, Phys. Lett. B 298 (1993) 363
and B 305 (1993) 136; Becher & Bell, Phys. Lett. B 713 (2012) 41 (arXiv:1112.3907); Gorishnii, Nucl. Phys. B 319 (1989)
633; Chetyrkin, Theor. Math. Phys. 75 (1988) 346 and 76 (1988) 809; Lee & Pomeransky, JHEP 11 (2013) 165; Akhoury,
Phys. Rev. D 19 (1979) 1250; Smirnov, *Analytic tools for Feynman integrals*, Springer Tracts Mod. Phys. 250 (2012).
*Content read (arXiv PDFs):* Collins 2020 (Introduction, §IV), SSS 2019 (Introduction, §§6–8), Jantzen 2011 (§3, §6),
BBF 2015 (§§2.2–2.3), Sterman TASI'95 hep-ph/9606312 (§§2.3–2.4), CSS 1989 hep-ph/0409313 (§§7.4, 8.4–8.7), Collins
1989 hep-ph/0312336 (around eq. 24). **[unverified]**: equation/section numbers inside Sterman 1978a, Libby–Sterman
1978, Collins 2011 ch. 5, Smirnov's books (paywalled; not consulted); the UD formula text (verified numerically only);
Sudakov's and Jackiw's original papers (only Collins' quotation consulted).

## 6. Files and reproduction

| file | content | runtime | result |
|---|---|---|---|
| `landau_oneloop.py` | L1–L7: envelope identity, deformation identity, α-space Landau sets (vertex variants, box, bubble), Cayley matrix, Coleman–Norton, Gordan LP, deformed-simplex numerics, soft-corner power counting | ~10 s | 23/23 PASS |
| `vertex_collinear_numeric.py` | C1–C5: $k^-$ pole structure, pinch, residue vs numerics, log scaling of $k_T$ shells, normal-coordinate exponent | ~4 s | 6/6 PASS |
| `power_counting.py` | P1–P7: region exponents (on-/off-shell vertex; P1b massless box corners/edges), eikonal validity, real-emission traces & numerator suppression, Feynman-gauge collinear numerator & boost scaling, Glauber trapping, $\omega(R)$ table, Sterman eq. (64) | ~2 s | 14/14 PASS |
| `sudakov_regions.py` | A1–A8 off-shell Sudakov (UD, regions, poles, LP/NLP/NNLP, $O(\epsilon)$, overlaps, polytope); B1–B4 massive exchange (Jantzen, BBF, analytic regulators, polytope); C1 massive legs (pure DR); D 1D zero-bin toy; E LL coefficients | ~10 min | 36/36 PASS |
| `landau.tex`, `powercounting.tex`, `regions.tex` | Chinese LaTeX sections with 3 TikZ figures (vertex, simplex, Coleman–Norton), leading-region reduced diagrams (e+e−, DIS, DY+Glauber), mode plane; tables | — | compile cleanly |
| `test_build.tex` | `xelatex test_build.tex` (twice) with copies of `preamble_fact.tex`, `fd_styles*.tex` | ~1 min | 12 pp., 0 errors / undefined refs / overfull boxes |
| `logs/*.log` | outputs of all runs | | |
