# research/c_wilson — Wilson lines, eikonal approximation, Ward identities, Grammer–Yennie

Working directory: `/Users/hao-cheng/Desktop/theorem proof/qcd_factorization_work/research/c_wilson`
(quote the path: it contains a space).

Everything below was derived independently and then checked with sympy (exact algebra) and numpy (explicit
Dirac matrices, spinors, SU(3) generators). The scripts live in `scripts/`, the logs in `logs/`, and
`./run_all.sh` re-runs everything. Formulas use the monograph macros of `common/preamble_fact.tex`
(`\ii`, `\dd`, `\ee`, `\sla{}`, `\order{}`), so they can be pasted into the LaTeX source directly.

| script | content | result |
|---|---|---|
| `scripts/qcdtools.py` | Dirac matrices (Dirac representation), spinors, SU(3) $t^a,f^{abc}$, PS Feynman rules, kinematics | self-test OK |
| `scripts/s1_wilson_rules.py` | item (1): Wilson-line Feynman rules (exact iterated integrals to $m=3$, induction step; ODE path-ordered exponential in an SU(3) background to $g^4$, all four semi-infinite lines; conjugation; covariance) | **48/48 PASS** |
| `scripts/s2_eikonal_identity.py` | item (2): abelian eikonal identity ($m\le7$), exact finite-$\epsilon$ version, shuffle identity, eikonal Ward identity, Ward identity of a Wilson line (non-abelian remainder), $O(g^2)$ exponentiation/webs | **44/44 PASS** |
| `scripts/s3_eikonal_approx.py` | item (3): eikonal approximation for in/out quark/antiquark, $M=0$ and $M>0$, $m\le3$ soft gluons, $\lambda$-scaling, equality with the Wilson-line rules, colour$\times$Dirac sum over $3!$ orderings, soft-bremsstrahlung form | **125/125 PASS** |
| `scripts/s4_ward_tree.py` | item (4): elementary Ward identities, abelian/non-abelian fermion-line identity, $\gamma^*\to q\bar qg$ on/off shell, DIS seed of the PDF Wilson line (1 and 2 K-gluons), $q\bar q\to g^*g^*$ and $\gamma^*\to q\bar qg^*g^*$ with three-gluon vertex and ghosts, unitarity, literature cross sections | **97/97 PASS** |
| `scripts/s5_grammer_yennie.py` | item (5): K/G algebra, collinear power counting (one-loop DIS vertex integrand), soft vs Glauber, gluon-PDF exception, original GY form | **28/28 PASS** |
| `scripts/s6_i0_poles.py` | $i0$ of the eikonal propagators vs poles of the propagators they replace (DIS future / DY past); $1/(a-i0)-1/(a+i0)$; blueprint example E7.24 | **8/8 PASS** |

Total **350/350 PASS**. LaTeX snippets (Chinese, monograph style, with TikZ figures) are in `tex/`; see §10.

---------------------------------------------------------------------------------------------------------

## 0. Results at a glance

| # | result | formula (conventions of §1) | status |
|---|---|---|---|
| 1a | past-pointing line $W[0,-\infty n]$ | $W^{(m)}=\prod_j[\ii g\,n\!\cdot\!\tilde A(k_j)]_{\text{path order}}\prod_{j=1}^m\frac{\ii}{n\cdot(k_1+\dots+k_j)+\ii0}$, $k_1$ nearest $-\infty$ | [R], PASS |
| 1b | future-pointing line $W[\infty n,0]$ | $\prod_{j=1}^m\frac{-\ii}{n\cdot(k_j+\dots+k_m)-\ii0}$, $k_1$ nearest $0$ | [R], PASS |
| 1c | universal rule | vertex $\ii g t^a v^\mu$, propagator $\ii/(v\cdot\ell+\ii0)$, $\ell$ along the orientation, $\ell=0$ at $\infty$ | [R], PASS |
| 2a | abelian eikonal identity | $\sum_{\pi\in S_m}\prod_j\frac{1}{n\cdot(k_{\pi(1)}+\dots+k_{\pi(j)})}=\prod_j\frac1{n\cdot k_j}$ (exact at finite $\epsilon$ with the adiabatic regulator) | [R], PASS |
| 2b | non-abelian: path ordering | symmetric part obeys 2a; antisymmetric part $=\tfrac12[T_b,T_a](E_{12}-E_{21})$ (webs) | [R], PASS |
| 2c | Ward identity of a Wilson line | $\sum_{\rm insertions}=-gT_qY+g\sum_pZ_p(\dots[T_q,T_{p+1}]\dots)$ | [R], PASS |
| 3 | eikonal approximation | e.g. incoming quark $S(p+k)\ii g\gamma^\mu t^au(p)\simeq-g\,t^a\frac{p^\mu}{p\cdot k+\ii0}u(p)$; $m$ gluons $\to$ $W[0,-\infty p]$ | [R] (asymptotic statement), PASS |
| 4a | elementary Ward identity | $S(p+k)\,\ii g\sla k\,t^a\,S(p)=g\,t^a[S(p+k)-S(p)]$ | [R], PASS |
| 4b | $\gamma^*\to q\bar qg$, $\epsilon\to k$ | $0$ on shell; with the $\bar q$ leg off shell the hard part gives $-g\,t^aH_0$ $\Rightarrow$ $W^{(1)}$ | [R], PASS |
| 4c | DIS seed of the PDF Wilson line | $k_\mu H^\mu=g\,t^aH_0$; two collinear K-gluons $\Rightarrow(n_B\!\cdot\!k_1)(n_B\!\cdot\!k_2)W^{(2)}[\infty n_B,0]H_0$ | [R] (tree), PASS |
| 4d | non-abelian tree identity | $k_{1\mu}\mathcal A^{\mu\nu}_{ab}=\frac{\ii gf^{abc}}{Q^2}(k_2^\nu k_2^\sigma-k_2^2g^{\nu\sigma})\mathcal A^c_\sigma(Q)$; ghosts in polarization sums | [R] (tree), PASS |
| 4e | graphical Ward identity (all orders) | BRST form, §5.6 | identity [R]; use for Wilson lines [A] |
| 5a | collinear K/G (Collins (11.5)–(11.6)) | $K_{\mu\nu}=\frac{k_\mu w_{2\nu}}{k\cdot w_2-\ii0}$, $w_2=n_B$; $G$ suppressed by $\ge\lambda$ | algebra [R], power counting [A], PASS |
| 5b | soft K/G | $K_{\rm s}^{\mu\nu}=\frac{k^\mu n_A^\nu}{n_A\cdot k\pm\ii0}$; $G_{\rm s}$ suppressed by $\lambda$ outside the Glauber region, $O(1)$ inside | algebra [R], power counting [A], PASS |

---------------------------------------------------------------------------------------------------------

## 1. Conventions

**Binding (CONTEXT.md).** $\hbar=c=1$, metric $(+,-,-,-)$; $v^\pm=(v^0\pm v^3)/\sqrt2$,
$v\cdot w=v^+w^-+v^-w^+-\mathbf v_T\cdot\mathbf w_T$. $D_\mu=\partial_\mu-\ii gA^a_\mu t^a$, quark–gluon vertex
$\ii g\gamma^\mu t^a$, $\Tr(t^at^b)=\frac12\delta^{ab}$.
$W[b,a]=P\exp\big(\ii g\int_a^b\dd z^\mu A^a_\mu(z)t^a\big)$, points closer to $b$ to the left,
$W[b,a]\to U(b)W[b,a]U^\dagger(a)$.

**Additional conventions fixed here** (I propose to make (C1)–(C4) binding; they coincide with blueprint §0.4(10)):

* **(C1) Fourier convention.** $A^a_\mu(x)=\int\frac{\dd^4k}{(2\pi)^4}\,\ee^{-\ii k\cdot x}\tilde A^a_\mu(k)$: $k$ is the
  momentum flowing **into** the Wilson line (out of the gluon line) at the attachment point. For hermitian
  $A$: $\tilde A(k)^\dagger=\tilde A(-k)$.
* **(C2) Directions.** $n$ future-pointing ($n^0>0$; light-like or time-like). Semi-infinite straight lines are
  written $W[\infty n,y]=\lim_{L\to\infty}W[y+Ln,y]$, $W[y,-\infty n]$, $W[-\infty n,y]$, $W[y,\infty n]$.
  For a line attached at $y\neq0$ every rule below acquires $\ee^{-\ii y\cdot K_{\rm tot}}$, $K_{\rm tot}$ the total
  gluon momentum flowing in.
* **(C3) Adiabatic regulator.** Along a semi-infinite line every field is multiplied by $\ee^{-\epsilon s}$, $s\ge0$ the
  distance (affine parameter) from the finite end, $\epsilon\to0^+$ at the end. Equivalently each gluon momentum
  is shifted, $n\cdot k\to n\cdot k+\ii\epsilon$ on lines reaching $-\infty$ and $n\cdot k\to n\cdot k-\ii\epsilon$ on lines
  reaching $+\infty$; the $j$-th eikonal denominator counted from the infinite end then carries $\pm\ii j\epsilon$.
* **(C4) Light-cone vectors.** $n_A=(1^+,0^-,\mathbf 0_T)$, so $n_A\cdot v=v^-$; $n_B=(0^+,1^-,\mathbf 0_T)$, so
  $n_B\cdot v=v^+$ ($n_B$ is Collins' $w_2$, "projects onto plus components"). For hadron $A$ along $+z$ the
  PDF line $W[w,0]$, $w=(0^+,w^-,\mathbf 0_T)$, runs along $n_B$ and contains $n_B\cdot A=A^+$.
* **(C5)** "Amplitude" $\mathcal A$ = sum of Feynman diagrams with the rules above, $\mathcal A=\ii\mathcal M$.
  Propagators: quark $S(p)=\ii/(\sla p-m)=\ii(\sla p+m)/(p^2-m^2+\ii0)$; gluon (Feynman gauge)
  $-\ii g^{\mu\nu}\delta^{ab}/(k^2+\ii0)$; ghost $\ii\delta^{ab}/(p^2+\ii0)$. Three-gluon vertex (all momenta incoming,
  $(a,\mu,k),(b,\nu,p),(c,\rho,q)$): $gf^{abc}[g^{\mu\nu}(k-p)^\rho+g^{\nu\rho}(p-q)^\mu+g^{\rho\mu}(q-k)^\nu]$.
  Ghost–gluon vertex $-gf^{abc}p^\mu$ ($p$ = outgoing ghost momentum, $a$ outgoing ghost, $b$ gluon, $c$ incoming
  ghost), from $\mathcal L_{\rm gh}=\bar c^a(-\partial^\mu D^{ac}_\mu)c^c$, $D^{ac}_\mu=\partial_\mu\delta^{ac}+gf^{abc}A^b_\mu$.
  These are Peskin–Schroeder's rules (PS ch. 16); the relative sign of the three-gluon and quark vertices is
  confirmed independently by the Ward identities of §5 (they fail with the opposite sign) and by the
  $q\bar q\to gg$ cross section.

---------------------------------------------------------------------------------------------------------

## 2. Item (1): momentum-space Feynman rules of semi-infinite Wilson lines

### 2.1 Expansion of $W[b,a]$

For a path $z(s)$, $s\in[0,1]$, $z(0)=a$, $z(1)=b$, and $A\equiv A^at^a$:
$$
W[b,a]=\sum_{m=0}^\infty(\ii g)^m\int_{0<s_1<\dots<s_m<1}\dd s_1\cdots\dd s_m\;
\dot z\cdot A(z(s_m))\cdots\dot z\cdot A(z(s_1)),
$$
the unique solution of $\frac{\dd}{\dd s}W(s)=\ii g\,\dot z\cdot A(z(s))\,W(s)$, $W(0)=1$, $W(s)\equiv W[z(s),a]$.
Covariance $W\to U(b)WU^\dagger(a)$ follows from this ODE because
$\dot z\cdot A'=U\dot z\cdot AU^\dagger-\frac{\ii}{g}\frac{\dd U}{\dd s}U^\dagger$ (verified numerically for SU(3), s1(E);
the reversed ordering fails).

For a straight line $z=y+\lambda v$ the field enters through $\dot z\cdot A=v\cdot A$ and the phase
$\ee^{-\ii k\cdot z}=\ee^{-\ii k\cdot y}\ee^{-\ii\lambda\,v\cdot k}$.

### 2.2 Past-pointing line $W[0,-\infty n]$

$W[0,-\infty n]=P\exp\big(\ii g\int_{-\infty}^0\dd\lambda\,n\cdot A(\lambda n)\big)$. Label the gluons in path order,
gluon 1 nearest $-\infty$ (earliest). Then
$$
W^{(m)}[0,-\infty n]=(\ii g)^m\!\int\prod_{j=1}^m\frac{\dd^4k_j}{(2\pi)^4}\;n\cdot\tilde A(k_m)\cdots n\cdot\tilde A(k_1)
\int_{-\infty<\lambda_1<\dots<\lambda_m<0}\prod_j\dd\lambda_j\,\ee^{-\ii\lambda_j(n\cdot k_j+\ii\epsilon)} .
$$
The $\lambda_1$ integral is $\int_{-\infty}^{\lambda_2}\dd\lambda_1\ee^{-\ii\lambda_1(n\cdot k_1+\ii\epsilon)}=\frac{\ii}{n\cdot k_1+\ii\epsilon}\ee^{-\ii\lambda_2(n\cdot k_1+\ii\epsilon)}$;
by induction (s1(A), "induction step")
$$
\int_{-\infty<\lambda_1<\dots<\lambda_m<0}=\prod_{j=1}^m\frac{\ii}{n\cdot(k_1+\dots+k_j)+\ii j\epsilon}.
$$
**Result.**
$$
\boxed{\;W^{(m)}[0,-\infty n]=\int\prod_{j=1}^m\frac{\dd^4k_j}{(2\pi)^4}\;
\big[\ii g\,n^{\mu_m}t^{a_m}\tilde A^{a_m}_{\mu_m}(k_m)\big]\cdots\big[\ii g\,n^{\mu_1}t^{a_1}\tilde A^{a_1}_{\mu_1}(k_1)\big]
\prod_{j=1}^m\frac{\ii}{n\cdot(k_1+\dots+k_j)+\ii0}\;}
$$
**Second order** (the requested check):
$W^{(2)}[0,-\infty n]=(\ii g)^2\!\int\!\!\int n\cdot\tilde A(k_2)\,n\cdot\tilde A(k_1)\,
\frac{\ii}{n\cdot k_1+\ii0}\,\frac{\ii}{n\cdot(k_1+k_2)+\ii0}$, colour $t^{a_2}t^{a_1}$ ($k_2$ later, i.e. closer to $b=0$,
to the left). The eikonal line from $-\infty$ carries no momentum, after absorbing $k_1$ it carries $k_1$, after
$k_2$ it carries $k_1+k_2$, which it delivers to the vertex at $0$.

### 2.3 Future-pointing line $W[\infty n,0]$

Path $0\to+\infty$, gluon 1 nearest $0$:
$\int_{0<\lambda_1<\dots<\lambda_m<\infty}\prod_j\ee^{-\ii\lambda_j(n\cdot k_j-\ii\epsilon)}=\prod_{j=1}^m\frac{-\ii}{n\cdot(k_j+\dots+k_m)-\ii(m-j+1)\epsilon}$
(do $\lambda_m$ first). **Result:**
$$
\boxed{\;W^{(m)}[\infty n,0]=\int\prod_j\frac{\dd^4k_j}{(2\pi)^4}\;
\big[\ii g\,n\cdot\tilde A(k_m)\big]\cdots\big[\ii g\,n\cdot\tilde A(k_1)\big]\prod_{j=1}^m\frac{-\ii}{n\cdot(k_j+\dots+k_m)-\ii0}\;}
$$
Second order: $(\ii g)^2\,n\cdot\tilde A(k_2)\,n\cdot\tilde A(k_1)\,\frac{-\ii}{n\cdot(k_1+k_2)-\ii0}\,\frac{-\ii}{n\cdot k_2-\ii0}$, colour
$t^{a_2}t^{a_1}$. The momenta are summed from the far end ($+\infty$).

### 2.4 The conjugate lines

* $W[-\infty n,0]=W[0,-\infty n]^\dagger$ (path $0\to-\infty$, orientation $-n$), gluon 1 nearest $0$:
  $W^{(m)}=\int[-\ii g\,n\cdot\tilde A(k_m)]\cdots[-\ii g\,n\cdot\tilde A(k_1)]\prod_{j=1}^m\frac{\ii}{n\cdot(k_j+\dots+k_m)+\ii0}$
  (gluon $m$, nearest $b=-\infty$, leftmost).
* $W[0,\infty n]=W[\infty n,0]^\dagger$ (path $\infty\to0$, orientation $-n$), gluon 1 nearest $+\infty$:
  $W^{(m)}=\int[-\ii g\,n\cdot\tilde A(k_m)]\cdots[-\ii g\,n\cdot\tilde A(k_1)]\prod_{j=1}^m\frac{-\ii}{n\cdot(k_1+\dots+k_j)-\ii0}$
  (gluon $m$, nearest $b=0$, leftmost).

With $\tilde A(k)^\dagger=\tilde A(-k)$ the hermitian conjugate of the rule of 2.2 (and $k\to-k$) reproduces the
first line (s1(D), symbolic and order by order to $g^4$ numerically, including order-by-order unitarity).

### 2.5 The universal rule (statement for the monograph)

> **Proposition (Feynman rules of straight semi-infinite Wilson lines)** [R]. Let a straight path run from $a$ to
> $b$ with tangent $v=\dd z/\dd\lambda$, one end at infinity, gluon fields expanded as in (C1). The term with $m$
> attached gluons (indices $\mu_j$, colours $a_j$, momenta $k_j$ flowing in) equals
> 1. one **vertex** $\ii g\,t^{a}v^{\mu}$ per attached gluon;
> 2. one **eikonal propagator** $\dfrac{\ii}{v\cdot\ell+\ii0}$ per segment, except the segment that reaches
>    infinity; $\ell$ is the momentum flowing along the path *in the direction of its orientation* ($a\to b$), fixed
>    by momentum conservation at the vertices and by $\ell=0$ on the segment that reaches infinity (the segment
>    ending at the finite endpoint carries the total momentum into the rest of the diagram);
> 3. the **colour matrices in path order**, the point closest to $b$ leftmost;
> 4. at finite $\epsilon$ (C3) the $\ii0$ of a segment is $\ii\epsilon$ times the number of attachments between it and
>    the infinite end.
>
> Equivalently, with $n$ future-pointing and $K$ = sum of the momenta flowing in between the segment and the infinite end:
> lines reaching $-\infty$ (past-pointing): $\dfrac{\ii}{n\cdot K+\ii0}$; lines reaching $+\infty$ (future-pointing):
> $\dfrac{-\ii}{n\cdot K-\ii0}$; vertex $+\ii g\,t^an^\mu$ for orientation $+n$ ($W[0,-\infty n]$, $W[\infty n,0]$) and
> $-\ii g\,t^an^\mu$ for orientation $-n$ ($W[-\infty n,0]$, $W[0,\infty n]$). A third equivalent form: all four lines
> have propagators $\ii/(n\cdot\ell_n+\ii0)$ with $\ell_n$ the momentum flowing along $n$ (towards the future).

*Proof.* §2.2–2.4. *Checks:* s1(A,B) exact for all four lines to $m=3$ + induction step; s1(C) path-ordered
exponential solved as an ODE in an SU(3) background made of three complex plane-wave modes, coefficients of
$g^1\dots g^4$ agree with the rule to $10^{-11}$ for all four lines; negative controls (wrong $\ii0$, reversed colour
order) fail by $O(1)$.

**Remarks.** (i) The rules are invariant under $n\to\alpha n$ for $\alpha>0$ (vertex $\propto\alpha$, propagator
$\propto1/\alpha$); for $\alpha<0$ the $\ii0$ flips, so $n$ must point in the physical direction of the parton.
(ii) The rule "$+\ii0$ with the momentum along the orientation" is literally the eikonal limit of a Feynman
propagator of a particle moving along the orientation (§4, s6). (iii) A light-like line has no self-energy in
Feynman gauge ($\propto n^2=0$). (iv) For the collinear PDF the points $0$ and $w$ lie on one light-like line and
$W[w,0]=W[w,\infty n_B]W[\infty n_B,0]=W[w,-\infty n_B]W[-\infty n_B,0]$ (at $\epsilon\to0$): the direction to infinity is
immaterial there (it matters for TMDs).

### 2.6 External partons and cut diagrams

* Incoming quark $\leftrightarrow W[0,-\infty v]$, outgoing quark $\leftrightarrow W[\infty v,0]$, incoming antiquark
  $\leftrightarrow W[-\infty v,0]$, outgoing antiquark $\leftrightarrow W[0,\infty v]$ ($v\propto$ parton momentum; §4).
  Operator form: $\psi(0)\to W[0,-\infty v]\psi_{\rm in}$, $\bar\psi(0)\to\bar\psi_{\rm out}W[\infty v,0]$, etc.
* Cut diagrams: the part right of the final-state cut is the complex-conjugate amplitude. For the PDF,
  $W[w,0]=W[w,\infty n_B]W[\infty n_B,0]$; $W[\infty n_B,0]$ (vertex $+\ii gt^an_B^\mu$, propagators $-\ii/(n_B\cdot K-\ii0)$)
  stands in the amplitude, $W[w,\infty n_B]$ (vertex $-\ii gt^an_B^\mu$) in the conjugate. A real gluon of momentum
  $l$ gives $-g\,t^a\frac{n^\mu}{n\cdot l+\ii0}$ (emitted, left) and $-g\,t^a\frac{n^\mu}{n\cdot l-\ii0}$ (absorbed from $|X\rangle$, right):
  complex conjugates of each other (colour handled by the trace).

### 2.7 Cross-checks against the literature (item 1)

| source | their statement | conversion | verdict |
|---|---|---|---|
| Blueprint §0.4(10) (architect) | past: $\prod_j\ii gn^{\mu_j}\frac{\ii}{n\cdot(k_1+\dots+k_j)+\ii0}$; future: $\prod_j\ii gn^{\mu_j}\frac{-\ii}{n\cdot(k_j+\dots+k_m)-\ii0}$ | same conventions | PASS |
| c_pdf DERIVATION §2.4 | $W[\infty n,0]$: absorbed gluon $+gt^an^\mu/(n\cdot l-\ii0)$, emitted $-gt^an^\mu/(n\cdot l+\ii0)$ | same conventions | PASS |
| Collins (2011), Fig. 7.10 as corrected in his errata ("Corrections and updates to Nov. 2013 printing") | quark pdf, bare fields: vertex $-\ii g_0n^\mu(t_\alpha)_{kj}$ left of the cut, $+\ii g_0n^\mu(t_\alpha)_{kj}$ right of the cut; "corresponds to the sign of the coupling in our Lagrangian, whose Feynman rules are in Fig. 3.1" | the Wilson-line vertex equals the quark–gluon vertex with $\gamma^\mu\to n^\mu$ in the amplitude and has the opposite sign in the conjugate: ours $+\ii gn^\mu t^a$ / $-\ii gn^\mu t^a$ with quark vertex $+\ii g\gamma^\mu t^a$. Collins' overall sign of $g$ is opposite to PS ($g_{\rm Collins}=-g$; **verify against his Fig. 3.1**) | PASS (relative signs) |
| Collins (2011) eq. (11.6) (corrected) | $K_{\mu\nu}=k_\mu w_{2\nu}/(k\cdot w_2-\ii0)$, $k$ flowing into $H$ in DIS | future-pointing line along $w_2=n_B$ with $k$ flowing in: $-\ii0$ | PASS |

---------------------------------------------------------------------------------------------------------

## 3. Item (2): eikonal identities

### 3.1 Abelian eikonal identity

> **Lemma** [R]. For real $a_1,\dots,a_m$ with no vanishing partial sum,
> $$\sum_{\pi\in S_m}\prod_{j=1}^m\frac{1}{a_{\pi(1)}+\dots+a_{\pi(j)}}=\prod_{j=1}^m\frac1{a_j}.$$
> With the adiabatic regulator it holds **exactly at finite $\epsilon$**:
> $\sum_\pi\prod_j\frac{\ii}{n\cdot(k_{\pi(1)}+\dots+k_{\pi(j)})+\ii j\epsilon}=\prod_j\frac{\ii}{n\cdot k_j+\ii\epsilon}$ (past), and
> $\sum_\pi\prod_j\frac{-\ii}{n\cdot(k_{\pi(j)}+\dots+k_{\pi(m)})-\ii(m-j+1)\epsilon}=\prod_j\frac{-\ii}{n\cdot k_j-\ii\epsilon}$ (future).

$m=2$ (the requested case):
$$
\frac{1}{n\cdot k_1\,n\cdot(k_1+k_2)}+\frac{1}{n\cdot k_2\,n\cdot(k_1+k_2)}=\frac{n\cdot k_2+n\cdot k_1}{n\cdot k_1\,n\cdot k_2\,n\cdot(k_1+k_2)}=\frac1{n\cdot k_1\,n\cdot k_2}.
$$
*Proof A (integral representation).* $\prod_j\frac{\ii}{a_j+\ii\epsilon}=\prod_j\int_{-\infty}^0\dd\lambda_j\ee^{-\ii\lambda_j(a_j+\ii\epsilon)}$;
$(-\infty,0]^m$ is, up to a null set, the disjoint union of the $m!$ simplices
$\lambda_{\pi(1)}<\dots<\lambda_{\pi(m)}$, and each simplex gives $\prod_j\frac{\ii}{a_{\pi(1)}+\dots+a_{\pi(j)}+\ii j\epsilon}$ by §2.2.
(Physically: the abelian Wilson line is an ordinary exponential, $W^{(m)}=(W^{(1)})^m/m!$.)
*Proof B (induction).* Group the permutations by their last element $\pi(m)=l$. The last factor
$1/(a_1+\dots+a_m)$ is common; by the induction hypothesis the remaining sum is $\prod_{j\ne l}1/a_j$; hence the
total is $\frac{1}{\sum_ja_j}\sum_l\prod_{j\neq l}\frac1{a_j}=\frac{\sum_la_l}{\sum_ja_j}\prod_j\frac1{a_j}$.
*Checks (s2):* symbolic for $m\le4$, exact rationals for $m=5,6,7$ (points with a vanishing partial sum, i.e. on the
singular locus, rejected); finite-$\epsilon$ versions symbolic for $m\le4$ and exact Gaussian rationals for
$m=5,6$. **Caveat:** with a *uniform* $+\ii\epsilon$ on every denominator the identity is not exact,
e.g. $m=2$: difference $=-\ii\epsilon/[(a_1+\ii\epsilon)(a_2+\ii\epsilon)(a_1+a_2+\ii\epsilon)]\to0$ (distributionally). Use the
adiabatic regulator in the monograph.

### 3.2 Shuffle identity

$\sum_{\sigma\in{\rm Sh}(p,q)}E(\sigma)=E(k_1,\dots,k_p)\,E(l_1,\dots,l_q)$, $E(q_1,\dots,q_r)=\prod_{j=1}^r\frac{1}{n\cdot(q_1+\dots+q_j)}$,
where the sum runs over the $\binom{p+q}{p}$ interleavings preserving the internal orders (same proof as A).
Checked for $p,q\le3$ (s2(4)). This is the form used when two groups of attachments carry mutually commuting
colour factors.

### 3.3 Non-abelian case: path ordering

The colour matrices follow the path order, so the sum over attachments does not factorize. For two gluons on
$W[0,-\infty n]$ ($T_j\equiv\ii g\,n\cdot\tilde A^{a_j}t^{a_j}$, $E_{12}=\frac{\ii}{n\cdot k_1+\ii0}\frac{\ii}{n\cdot(k_1+k_2)+\ii0}$):
$$
T_bT_aE_{12}+T_aT_bE_{21}=\tfrac12\{T_a,T_b\}\,\frac{\ii}{n\cdot k_1+\ii0}\,\frac{\ii}{n\cdot k_2+\ii0}+\tfrac12[T_b,T_a]\,(E_{12}-E_{21}),
$$
$E_{12}-E_{21}=\frac{\ii}{n\cdot(k_1+k_2)+\ii0}\big(\frac{\ii}{n\cdot k_1+\ii0}-\frac{\ii}{n\cdot k_2+\ii0}\big)$, and $[t^b,t^a]=\ii f^{bac}t^c$: the symmetric
part obeys the abelian identity, the antisymmetric part is a single adjoint "web" carrying $k_1+k_2$.
Equivalently (s2(7), exact at finite $\epsilon$):
$$
W^{(2)}-\tfrac12\big(W^{(1)}\big)^2=\tfrac14\sum_{r,s}[T_s,T_r]\big(E(r,s)-E(s,r)\big),
$$
i.e. $\ln W$ starts at $O(g^2)$ with commutators only (non-abelian exponentiation in terms of webs: Gatheral,
Phys. Lett. B133 (1983) 90; Frenkel & Taylor, Nucl. Phys. B246 (1984) 231); in the abelian case
$\ln W=W^{(1)}$ exactly.

### 3.4 Eikonal Ward identity

$$
\frac{n\cdot k}{(n\cdot\ell+\ii0)(n\cdot(\ell+k)+\ii0)}=\frac1{n\cdot\ell+\ii0}-\frac1{n\cdot(\ell+k)+\ii0}
\iff
\frac{\ii}{n\cdot(\ell+k)}\,(\ii g\,n\cdot k\,t^a)\,\frac{\ii}{n\cdot\ell}=g\,t^a\Big[\frac{\ii}{n\cdot(\ell+k)}-\frac{\ii}{n\cdot\ell}\Big],
$$
exact with the same $\ii0$ on both propagators; it is the quark-line identity (4a) with $S(p)\to\ii/n\cdot p$,
$\gamma^\mu\to n^\mu$. This is why a Wilson line reproduces the Ward identities of the parton line it replaces.

### 3.5 Ward identity of a semi-infinite Wilson line

$m$ gluons on $W[0,-\infty n]$ (colour matrices $T_1,\dots,T_m$, gluon 1 nearest $-\infty$, polarization factors
set to $n\cdot\epsilon_j=1$), plus one scalar-polarized gluon ($\epsilon^\mu=q^\mu$, colour $T_q$) inserted in all $m+1$ places:
$$
\sum_{p=0}^{m}(\text{insertion after }p\text{ gluons})=-g\,T_q\,Y+g\sum_{p=0}^{m-1}Z_p\;T_m\cdots T_{p+2}\,[T_q,T_{p+1}]\,T_p\cdots T_1 ,
$$
$Y$ = the original $m$-gluon term, $Z_p$ = the eikonal propagators of the $m$-gluon line in which gluon $p+1$
carries $k_{p+1}+q$. Future line: $+g\,Y\,T_q+g\sum_pZ'_p(\cdots[T_q,T_{p}]\cdots)$ ($T_q$ at the finite end, rightmost).
Abelian: $-gY$ (past), $+gY$ (future). The endpoint term is the infinitesimal gauge rotation at the finite end
($W[0,-\infty n]\to U(0)W[0,-\infty n]$; the rotation at infinity is switched off by the adiabatic damping); the
commutator terms are cancelled by the attachments of the scalar gluon to the other gluon lines through the
three-gluon vertex (§5.5). Exact at finite $\epsilon$ provided the scalar gluon's polarization carries the same
adiabatic shift as its momentum (s2(6)).

---------------------------------------------------------------------------------------------------------

## 4. Item (3): eikonal approximation

### 4.1 One soft gluon

$k$ flows **into** the line, $p^2=M^2$, $k=O(\lambda Q)$. Using $(\sla p+M)\gamma^\mu u(p)=2p^\mu u(p)$,
$\bar u(p)\gamma^\mu(\sla p+M)=2p^\mu\bar u(p)$, $(-\sla p+M)\gamma^\mu v(p)=-2p^\mu v(p)$, $\bar v(p)\gamma^\mu(-\sla p+M)=-2p^\mu\bar v(p)$:

| external line | exact | eikonal limit | $=$ Wilson-line rule |
|---|---|---|---|
| incoming quark | $S(p+k)\,\ii g\gamma^\mu t^a\,u(p)$ | $-g\,t^a\dfrac{p^\mu}{p\cdot k+\ii0}\,u(p)$ | $W[0,-\infty p]$: $(\ii gp^\mu t^a)\frac{\ii}{p\cdot k+\ii0}$ |
| outgoing quark | $\bar u(p)\,\ii g\gamma^\mu t^a\,S(p-k)$ | $+g\,t^a\dfrac{p^\mu}{p\cdot k-\ii0}\,\bar u(p)$ | $W[\infty p,0]$: $(\ii gp^\mu t^a)\frac{-\ii}{p\cdot k-\ii0}$ |
| incoming antiquark | $\bar v(p)\,\ii g\gamma^\mu t^a\,S(-p-k)$ | $+g\,t^a\dfrac{p^\mu}{p\cdot k+\ii0}\,\bar v(p)$ | $W[-\infty p,0]$: $(-\ii gp^\mu t^a)\frac{\ii}{p\cdot k+\ii0}$ |
| outgoing antiquark | $S(-p+k)\,\ii g\gamma^\mu t^a\,v(p)$ | $-g\,t^a\dfrac{p^\mu}{p\cdot k-\ii0}\,v(p)$ | $W[0,\infty p]$: $(-\ii gp^\mu t^a)\frac{-\ii}{p\cdot k-\ii0}$ |

For an **emitted** gluon (momentum $k$ flowing out) replace $k\to-k$; e.g. an outgoing antiquark emitting $k$
gives $+g\,t^a\frac{p^\mu}{p\cdot k+\ii0}$ — this is the form "$g\,t^ap^\mu/(p\cdot k+\ii0)$" of the task; in Collins'
sign convention ($g\to-g$) it is also the incoming quark absorbing $k$. The universally valid content: magnitude
$g\,t^ap^\mu/p\cdot k$; overall sign $+$/$-$ according to (antiquark-like/quark-like ordering, absorbed/emitted);
the $\ii0$ is that of the propagator replaced, $(p\pm k)^2-M^2+\ii0$ (s6(1)). Corrections are $O(\lambda)$: the dropped
$k^2$ in the denominator and $\sla k$ in the numerator.

### 4.2 $m$ soft gluons $\to$ Wilson line

> **Proposition** [R] (asymptotic statement). Incoming quark absorbing $k_1,\dots,k_m$ in time order,
> $K_j=k_1+\dots+k_j$:
> $$S(p+K_m)\,\ii g\sla\epsilon_mt^{a_m}\cdots S(p+K_1)\,\ii g\sla\epsilon_1t^{a_1}\,u(p)=\Big[\prod_{j=1}^m\frac{-g\,p\cdot\epsilon_j}{p\cdot K_j+\ii0}\Big]\,t^{a_m}\cdots t^{a_1}\,u(p)\,\big[1+O(\lambda)\big],$$
> which is the $m$-th order term of $W[0,-\infty p]$ with $\tilde A^a_\mu\to\epsilon_\mu$; analogously outgoing quark
> $\to W[\infty p,0]$ ($K'_j=k_j+\dots+k_m$, factors $+g\,p\cdot\epsilon_j/(p\cdot K'_j-\ii0)$, colour $t^{a_m}\cdots t^{a_1}$),
> incoming antiquark $\to W[-\infty p,0]$ ($+g\,p\cdot\epsilon_j/(p\cdot K_j+\ii0)$, colour $t^{a_1}\cdots t^{a_m}$),
> outgoing antiquark $\to W[0,\infty p]$ ($-g\,p\cdot\epsilon_j/(p\cdot K'_j-\ii0)$, colour $t^{a_1}\cdots t^{a_m}$).
> Summing over the $m!$ attachment orders reproduces the full $m$-th order term of the path-ordered exponential,
> colour order included.

*Proof.* Drop $K_j^2$ and $\sla K_j$ (relative $O(\lambda)$) and use
$(\sla p+M)\gamma^\mu(\sla p+M)=2p^\mu(\sla p+M)+(M^2-p^2)\gamma^\mu=2p^\mu(\sla p+M)$ on shell, so each step removes one
numerator; induction on $m$.
*Checks (s3):* 4 line types $\times$ $M\in\{0,0.4\}$ $\times$ $m\in\{1,2,3\}$ $\times$ two kinematic classes
(well-conditioned future time-like $\hat k_j$; generic off-shell $\hat k_j$): relative error $\propto\lambda^{1.00}$
(fitted slopes $1.00$ for $\lambda=10^{-3}\dots10^{-5}$); exact equality of the eikonal factors with the
Wilson-line rules of §2.5; colour$\times$Dirac sum over $3!$ orders equals the $W^{(3)}$ term to $O(\lambda)$.
The coefficient of $\lambda$ grows like $1/\min_j|p\cdot K_j|$: the approximation fails where $p\cdot K_j\to0$ with
$K_j^2\ne0$ (e.g. the Glauber region, §6.3).

### 4.3 Literature cross-check (item 3)

* **Soft bremsstrahlung** (Peskin–Schroeder §6.1; QED vertex $-\ii e\gamma^\mu$): $\ii\mathcal M=\bar u(p')\mathcal M_0u(p)\,e\big(\frac{p'\cdot\epsilon^*}{p'\cdot k}-\frac{p\cdot\epsilon^*}{p\cdot k}\big)$.
  Conversion $g\,t^a\to-e$: our outgoing quark emitting $k$ gives $-g\,t^a\frac{p'\cdot\epsilon^*}{p'\cdot k}\to+e\frac{p'\cdot\epsilon^*}{p'\cdot k}$,
  the incoming quark emitting $k$ gives $+g\,t^a\frac{p\cdot\epsilon^*}{p\cdot k}\to-e\frac{p\cdot\epsilon^*}{p\cdot k}$. **PASS** (structure; PS equation
  number to be verified by the writer). Numerically: the full $\gamma^*\to q(p_1)\bar q(p_2)g(k)$ amplitude tends to
  $g\big(\frac{p_2\cdot\epsilon^*}{p_2\cdot k}-\frac{p_1\cdot\epsilon^*}{p_1\cdot k}\big)t^a\mathcal A_0$ (s3, rel. error $2.6\times10^{-4}$ at $\lambda=10^{-4}$).
* The abelian multi-photon version (eikonal identity + soft factorization) is classical: S. Weinberg,
  "Infrared photons and gravitons", Phys. Rev. 140 (1965) B516 (verified bibliographic data, INSPIRE 48759;
  the location of the identity inside the paper is not verified).

---------------------------------------------------------------------------------------------------------

## 5. Item (4): Ward identities

### 5.1 Elementary identities (exact; s4(a))

* (W1) $S(p+k)\,(\ii g\sla k\,t^a)\,S(p)=g\,t^a\,[S(p+k)-S(p)]$, from $\sla k=(\sla p+\sla k-M)-(\sla p-M)$.
* (W2) on-shell ends: $\bar u(p')\,\ii g\sla k\,S(p'-k)=g\,\bar u(p')$; $S(p+k)\,\ii g\sla k\,u(p)=-g\,u(p)$;
  $\bar v(p)\,\ii g\sla k\,S(-p-k)=+g\,\bar v(p)$; $S(-p+k)\,\ii g\sla k\,v(p)=-g\,v(p)$.
* (W3) three-gluon vertex (all momenta incoming, $q_1+q_2+q_3=0$):
  $q_{1\mu}V^{\mu\nu\rho}_{abc}(q_1,q_2,q_3)=gf^{abc}\big[(q_3^2g^{\nu\rho}-q_3^\nu q_3^\rho)-(q_2^2g^{\nu\rho}-q_2^\nu q_2^\rho)\big]$:
  a difference of inverse transverse propagators.
* (W4) ghost vertex: $k_\mu\,(-gf^{abc}p'^\mu)=-\frac g2f^{abc}(p'^2-p^2+k^2)$, $p'=p+k$: not a pure difference
  (extra $k^2$) — the origin of the additional ghost terms when several gluons are longitudinal.
* (W5) eikonal line: §3.4.

### 5.2 Fermion line: abelian Ward identity and non-abelian remainder

Open line $\bar u(p')V_nS\cdots SV_1u(p)$, $V_r=\ii g\sla\epsilon_rT_r$ with momenta $q_r$ flowing in, on-shell ends,
and a scalar gluon (polarization $k$, colour $T_K$, momentum $k$ flowing in) inserted in all $n+1$ places:
$$
\sum_{\rm insertions}=g\sum_{r=1}^n\Big[\text{the line with gluon } r \text{ carrying } q_r+k \text{ and colour } [T_K,T_r]\Big],
$$
hence **0 in the abelian case**. *Proof:* (W1) telescopes the internal insertions, (W2) evaluates the two end
insertions; summation by parts gives $\sum=g\sum_{r=1}^nZ_r(C_r-C_{r-1})$, $C_r$ the colour product with $T_K$
after vertex $r$. Checked with generic colour matrices for $n\le3$, $M\in\{0,0.5\}$ (s4(b)).

### 5.3 $\gamma^*\to q(p_1)\bar q(p_2)g(k)$ with $\epsilon\to k$

$\mathcal A^{\mu\nu}=\bar u(p_1)\big[\ii g\gamma^\mu t^aS(p_1+k)\gamma^\nu+\gamma^\nu S(-p_2-k)\,\ii g\gamma^\mu t^a\big]v(p_2)$ (photon index $\nu$, unit coupling).

* **On shell:** $k_\mu\mathcal A^{\mu\nu}=-g\,t^a\bar u\gamma^\nu v+g\,t^a\bar u\gamma^\nu v=0$ (s4(c): $\le10^{-12}$ relative to one diagram,
  massless and massive, all spins).
* **Antiquark leg off shell** (collinear to a hadron/jet; open Dirac index $X$, $p_2^2\neq0$): the diagram with the
  gluon on the on-shell quark alone gives, exactly, $k_\mu\mathcal A^{\mu\nu}_{(1)}=-g\,t^a\,\bar u(p_1)\gamma^\nu X$; the sum of
  both diagrams gives $-g\,t^a\bar u(p_1)\gamma^\nu S(-p_2-k)S(-p_2)^{-1}X$, and with $X=S(-p_2)J$ this is
  $-g\,t^a\bar u(p_1)\gamma^\nu S(-p_2-k)J$ (the gluon disappears, its momentum is routed into the collinear line).
* **Seed of the Wilson line.** If $p_2$ and $k$ belong to the same collinear subgraph, only diagram (1) is in the
  hard part $H$, and $k_\mu H^\mu=-g\,t^aH_0$. With the K projector $\frac{k^\mu n_1^\alpha}{n_1\cdot k+\ii0}$ ($n_1\propto p_1$) this is
  $H_0\times\big[-g\,t^a\frac{n_1^\alpha}{n_1\cdot k+\ii0}\big]$ = first-order term of $W[\infty n_1,0]$ with the gluon momentum $k$
  flowing *out* of the line ($-k$ in): the antiquark jet function acquires a Wilson line along the quark direction.
* **Literature:** $\sum|\mathcal M|^2=8N_cC_Fg^2\frac{x_1^2+x_2^2}{(1-x_1)(1-x_2)}$ (unit photon coupling, $-g_{\nu\nu'}$ photon sum,
  $x_i=2p_i\cdot q/q^2$), i.e. $\frac{1}{\sigma_0}\frac{\dd\sigma}{\dd x_1\dd x_2}=\frac{\alpha_sC_F}{2\pi}\frac{x_1^2+x_2^2}{(1-x_1)(1-x_2)}$ (Ellis–Stirling–Webber ch. 3;
  equation number to be verified): **PASS** (ratio $-1<10^{-12}$).

### 5.4 DIS: the seed of the PDF Wilson line

Hard part with one target-collinear gluon $k$ flowing into $H$, attached to the final-state struck quark $p'$,
incoming quark leg off shell (open index):
$$
H^\mu_a=\bar u(p')\,\ii g\gamma^\mu t^a\,S(p'-k)\,\Gamma,\qquad k_\mu H^\mu_a=g\,t^a\,\bar u(p')\Gamma\equiv g\,t^aH_0\quad\text{(exact)},
$$
$$
H_\mu\,\frac{k^\mu n_B^\alpha}{n_B\cdot k-\ii0}=\Big[\ii g\,n_B^\alpha t^a\,\frac{-\ii}{n_B\cdot k-\ii0}\Big]H_0=W^{(1)}[\infty n_B,0]\,H_0 .
$$
The $-\ii0$ is the pole of the replaced propagator: $(p'-k)^2+\ii0=-2p'^-k^++\dots+\ii0$ has its $k^+$ pole in the upper
half plane (s6(2)) — **future-pointing** line along $n_B$ (DIS). In Drell–Yan the same K-gluon attaches to the
incoming antiquark from $B$, $(\bar p_B+k)^2+\ii0=2\bar p_B^-k^++\dots+\ii0$, pole in the lower half plane (s6(3)) —
**past-pointing** line, $+\ii0$.

**Two K-gluons** (colours $a,b$, both orderings on the struck quark): exact (s4(f), any $k_1,k_2$, $M=0,0.5$)
$$
k_{1\mu}k_{2\nu}H^{\mu\nu}_{ab}=g^2\,t^bt^a\,H_0+\ii g^2\,[t^a,t^b]\;\bar u(p')\sla k_2\,S(p'-k_1-k_2)\,\Gamma .
$$
For exactly collinear $\hat k_i=(k_i^+,0,\mathbf 0_T)$, $\sla{\hat k}_2\sla{\hat K}=0$ gives $\ii\bar u(p')\sla{\hat k}_2S(p'-\hat K)\Gamma=\frac{n_B\cdot k_2}{n_B\cdot K}H_0$, hence
$$
k_{1\mu}k_{2\nu}H^{\mu\nu}_{ab}=(n_B\!\cdot\!k_1)(n_B\!\cdot\!k_2)\;g^2\Big[\frac{t^bt^a}{n_B\cdot K\;n_B\cdot k_2}+\frac{t^at^b}{n_B\cdot K\;n_B\cdot k_1}\Big]H_0
=(n_B\!\cdot\!k_1)(n_B\!\cdot\!k_2)\,W^{(2)}_{ab}[\infty n_B,0]\,H_0 ,
$$
$K=k_1+k_2$ (s4(f), $10^{-12}$). The **path ordering** of the Wilson line comes from the commutator term; the
abelian part alone gives $g^2H_0$ (eikonal identity). No three-gluon-vertex or ghost graph enters at this order:
the graph in which $k_1,k_2$ merge has a collinear internal gluon and belongs to the PDF side.

### 5.5 Non-abelian: three-gluon vertex and ghosts

**(i) $q(p_1)\bar q(p_2)\to g^*(k_1,a,\mu)\,g^*(k_2,b,\nu)$**, quarks on shell, gluons off shell, $Q=k_1+k_2$:
$$
k_{1\mu}\mathcal A^{\mu\nu}_{ab}=\frac{g^2f^{abc}}{Q^2}\big(k_2^2g^{\nu\sigma}-k_2^\nu k_2^\sigma\big)J_{c\sigma},\qquad J_c^\sigma=\bar v(p_2)\gamma^\sigma t^cu(p_1).
$$
Derivation: the $t$- and $u$-channel graphs telescope to $\ii g^2\bar v\gamma^\nu[t^b,t^a]u=g^2f^{abc}J^\nu_c$; in the $s$-channel graph (W3)
gives $gf^{abc}[(Q^\sigma Q^\nu-Q^2g^{\sigma\nu})-(k_2^\sigma k_2^\nu-k_2^2g^{\sigma\nu})]$; the $Q^2g^{\sigma\nu}$ piece cancels the commutator, the
$Q^\sigma Q^\nu$ piece vanishes by current conservation ($\bar v\sla Qu=0$), the $k_2$ piece remains. Consequences
(s4(g)): (a) $=0$ for a physical gluon 2 ($k_2^2=0$, $\epsilon_2\cdot k_2=0$); (b) $k_{1\mu}k_{2\nu}\mathcal A^{\mu\nu}=0$ even off shell;
(c) for on-shell gluon 2 with the unphysical polarization $\bar k_2=(k_2^0,-\mathbf k_2)$:
$k_{1\mu}\bar k_{2\nu}\mathcal A^{\mu\nu}_{ab}=(k_2\cdot\bar k_2)\,\mathcal A_{\rm gh}$, $\mathcal A_{\rm gh}=\frac{g^2}{Q^2}f^{abd}\,k_1\cdot J_d$ = amplitude for
$q\bar q\to c^a(k_1)\bar c^b(k_2)$ with the PS ghost vertex (checked in modulus; its overall phase is convention);
(d) **ghosts in polarization sums**:
$\sum_{\rm phys}|\mathcal A|^2=\sum_{-g,-g}|\mathcal A|^2-2\sum|\mathcal A_{\rm gh}|^2$ (ghost + antighost final states);
(e) **literature:** $\frac1{36}\sum_{\rm phys}|\mathcal A|^2=g^4\big[\frac{32}{27}\frac{t^2+u^2}{tu}-\frac83\frac{t^2+u^2}{s^2}\big]$
(Combridge, Kripfganz & Ranft, Phys. Lett. B70 (1977) 234; Ellis–Stirling–Webber Table 7.1 — table number to be
verified): **PASS** (ratio $-1=2\times10^{-13}$).

**(ii) $\gamma^*\to q\bar q\,g^*(k_1,a)\,g^*(k_2,b)$** (6 quark-line orders + 2 three-gluon graphs):
$$
k_{1\mu}\mathcal A^{\mu\nu}_{ab}=\frac{\ii gf^{abc}}{Q^2}\big(k_2^\nu k_2^\sigma-k_2^2g^{\nu\sigma}\big)\,\mathcal A^c_\sigma(Q),
$$
$\mathcal A^c_\sigma(Q)$ = the amputated one-gluon amplitude $\gamma^*\to q\bar q g^*(Q,c,\sigma)$; (i) is the special case
$\mathcal A^c_\sigma=\ii g J_{c\sigma}$. Hence $k_{1\mu}k_{2\nu}\mathcal A^{\mu\nu}=0$ for off-shell gluons and physical quarks (s4(h)) — the
tree-level instance of the BRST statement below. The same formula holds for any number of colour-singlet
currents on the quark line.

### 5.6 The graphical Ward identity: precise statement

Setting: covariant gauge, $\mathcal L_{\rm gf}=-\frac1{2\xi}(\partial\cdot A^a)^2$ (auxiliary-field form $B^a\partial\cdot A^a+\frac\xi2B^aB^a$,
$B^a=-\frac1\xi\partial\cdot A^a$), $\mathcal L_{\rm gh}=\bar c^a(-\partial^\mu D_\mu^{ac})c^c$; BRST transformations (PS §16.4, written with a
Grassmann parameter $\varepsilon$; signs to be re-checked by the writer against PS):
$\delta\psi=\ii g\varepsilon c^at^a\psi$, $\delta A^a_\mu=\varepsilon D_\mu^{ac}c^c$, $\delta c^a=-\frac g2\varepsilon f^{abc}c^bc^c$, $\delta\bar c^a=\varepsilon B^a$.
Thus $\partial\cdot A^a=-\xi\,s\bar c^a$, $s$ nilpotent, the vacuum and the physical asymptotic states BRST invariant
(Kugo–Ojima).

> **Theorem (Slavnov–Taylor/'t Hooft identity, form used in factorization)** [R] in renormalized perturbation
> theory with a BRST-invariant regulator (dimensional regularization). Let $\Phi$ be a product of fields for
> physical external particles (quarks, transversely polarized gluons), LSZ-amputated and on shell. Then, at
> non-exceptional momenta,
> $$\langle0|T\,\partial\cdot A^{a_1}(x_1)\cdots\partial\cdot A^{a_N}(x_N)\;\Phi|0\rangle=0\qquad(N\ge1,\ \Phi\neq1),$$
> and with one longitudinal and further arbitrary gluons
> $$\langle0|T\,\partial\cdot A^{a}(x)\,A^{\nu_1}_{b_1}(y_1)\cdots A^{\nu_r}_{b_r}(y_r)\,\Phi|0\rangle
> =\xi\sum_{j=1}^r\langle0|T\,\bar c^{a}(x)\,A^{\nu_1}_{b_1}(y_1)\cdots(D^{\nu_j}c)_{b_j}(y_j)\cdots A^{\nu_r}_{b_r}(y_r)\,\Phi|0\rangle ,$$
> $(D^\nu c)_b=\partial^\nu c_b+gf_{bcd}A^\nu_cc_d$ (the sign of each term follows from moving the Grassmann-odd $s$
> through $\bar c$; to be fixed together with the BRST signs). The $\partial^\nu c$ term produces a ghost propagator ending in a
> longitudinal ($\propto k_j^{\nu_j}$) polarization, the $gfAc$ term a composite insertion without single-gluon pole:
> both vanish for a physical on-shell gluon $j$, so a single longitudinal gluon decouples when all other external
> particles are physical. When the other gluons are off shell or unphysical, ghost terms survive — e.g. §5.5(i)(c).

*Proof sketch.* $\langle s(\bar c^a\,\mathcal O)\rangle=0$ for any $\mathcal O$ (BRST-invariant vacuum), $s\Phi$ has no single-particle
pole (vanishes after LSZ), $sA=Dc$; for $\mathcal O=\prod\partial\cdot A$ the ghost terms reduce, by the ghost equation of motion
($\partial^\mu D_\mu c$ inserted next to $\bar c$ gives a contact term), to contact terms $\propto\delta(x_1-x_j)$ that vanish at
non-exceptional momenta; induction on $N$.

*Use in factorization.* The K-gluons are internal (attached to collinear/soft subgraphs), so the second identity
is applied with off-shell gluon legs; the ghost terms generated must be shown to cancel or to be absorbed into
the Wilson-line operators. This step is given in outline in the literature: Collins (2011) §11.9 "Ward identities
to convert K gluons to Wilson line" (title and page 416 verified from the table of contents; the BRST discussion is
indexed at pp. 407–411), Collins & Soper, Nucl. Phys. B194 (1982) 445; Labastida & Sterman, Nucl. Phys. B254
(1985) 425; an amplitude-level all-order argument: Feige & Schwartz, Phys. Rev. D90 (2014) 105020. Original
identities: 't Hooft, Nucl. Phys. B33 (1971) 173 (diagrammatic Ward identities of massless Yang–Mills); J. C. Taylor,
Nucl. Phys. B33 (1971) 436; Slavnov, Theor. Math. Phys. 10 (1972) 99; BRST: Becchi, Rouet & Stora, Commun.
Math. Phys. 42 (1975) 127 and Ann. Phys. 98 (1976) 287; Tyutin, Lebedev preprint FIAN-39 (1975),
arXiv:0812.0580; Kugo & Ojima, Prog. Theor. Phys. Suppl. 66 (1979) 1. **Status:** the identities [R]; their use to
convert arbitrary numbers of non-abelian K-gluons into Wilson lines to all orders [A]; abelian case [R] (§5.2 +
eikonal identity).

---------------------------------------------------------------------------------------------------------

## 6. Item (5): Grammer–Yennie decomposition

### 6.1 Original (QED) form

Grammer & Yennie, Phys. Rev. D8 (1973) 4332. In the form reproduced by Sen, Indumathi & Choudhury (arXiv:1812.06468,
eqs. (7)–(9)) — I could not access the original, **verify against GY**: for a photon of momentum $k$ attached to the
final ($p_f$) and initial ($p_i$) charged lines,
$$
g_{\mu\nu}=\big[g_{\mu\nu}-b_k(p_f,p_i)k_\mu k_\nu\big]+b_k(p_f,p_i)k_\mu k_\nu\equiv G+K,\qquad
b_k=\frac12\Big[\frac{(2p_f-k)\cdot(2p_i-k)}{((p_f-k)^2-m^2)((p_i-k)^2-m^2)}+(k\to-k)\Big].
$$
Since $(2p-k)\cdot k=-[(p-k)^2-m^2]$, the K part contracted with the convection currents equals $b_k$, the
$k$-symmetrized eikonal product: all IR divergences sit in K-photons (which factorize and exponentiate by Ward
identities), G-photons are IR finite. s5(5): K-part = full eikonal product $\times[1+O(k)]$ (slope $1.01$).

### 6.2 Collinear attachments (Collins' form)

Collins (2011), eqs. (11.4)–(11.6), p. 402, **as corrected in the errata** (upper/lower indices interchanged
relative to the printing): $H\cdot C=H^{\mu_1\cdots\mu_N}\prod_jg_{\mu_j\nu_j}C^{\nu_1\cdots\nu_N}$, $k_j$ flowing into $H$, "the largest term in
its polarization sum has $\mu_j=-$, $\nu_j=+$", and
$$
\boxed{\;g_{\mu\nu}=K_{\mu\nu}+G_{\mu\nu},\qquad K_{\mu\nu}(k)=\frac{k_\mu\,w_{2\nu}}{k\cdot w_2-\ii0},\qquad G_{\mu\nu}=g_{\mu\nu}-\frac{k_\mu\,w_{2\nu}}{k\cdot w_2-\ii0},\qquad w_2=n_B=(0^+,1^-,\mathbf 0_T)\;}
$$
($\mu$ = index on $H$, $\nu$ on $C$; $k\cdot w_2=k^+$). Exact properties (s5(1)):
(i) $G_{\mu\nu}k^\nu=0$ — G kills the scalar polarization on the collinear side;
(ii) $K$ feeds $k_\mu H^\mu$, i.e. the Ward identity (§5.4) $\Rightarrow$ Wilson line along $n_B$;
(iii) $H\cdot G\cdot C=H\cdot\big(C-\frac{C^+}{k^+}k\big)$.

**Power counting.** $A$-collinear $k\sim(1,\lambda^2,\lambda)Q$, $C^\nu\sim(1,\lambda^2,\lambda)C^+$, $H$ hard. Then
$C-\frac{C^+}{k^+}k=(0,O(\lambda^2),O(\lambda))\,C^+$, so $H\cdot G\cdot C=O(\lambda)\,H\cdot C$: **each G-gluon beyond the minimal parton
content costs at least one power of $\lambda$; K-gluons (the boosted $A^+$ components) cost none** and arbitrarily many
of them contribute at leading power — they are summed by the Ward identity into the Wilson line. In $H$ one may set
$k\to\hat k=(k^+,0,\mathbf 0_T)$ (error $O(\lambda)$), making $\hat k_\mu H^\mu(\hat k)$ a Ward identity with a light-like K-gluon.
Numerics (s5(2)): one-loop DIS vertex integrand, gluon collinear to the target quark: generic off-shell collinear
parent $|G|/|{\rm full}|\propto\lambda^{1.00}$; on-shell massless parent quark $\propto\lambda^{2.00}$ (the bad spinor components vanish,
$\sla Pu(P)=0$, so $S(P-k)\gamma_Tu(P)$ is suppressed); the K term equals exactly $g\times$Born$\times$[the Wilson-line vertex
graph of the PDF].

**Exception — gluon as active parton.** If the only collinear parton entering $H$ is a gluon, $k\cdot H=0$ (Ward
identity, other legs physical), the K term vanishes and the G term is leading:
$$
H\cdot C=H^+\Big(C^--\frac{k^-}{k^+}C^+\Big)-\mathbf H_T\cdot\Big(\mathbf C_T-\frac{\mathbf k_T}{k^+}C^+\Big),
$$
the combination $k^+A^j-k^jA^+$ of the field strength $G^{+j}$ in the gluon PDF (s5(4), photon–gluon fusion).

$\ii0$: Collins' $-\ii0$ belongs to DIS (attachments to the final-state struck quark, future-pointing line); for
attachments to initial-state lines (DY) the matching choice is $+\ii0$ (s6). Choosing the $\ii0$ of the propagator being
approximated keeps the approximation compatible with the contour deformations used elsewhere.

### 6.3 Soft attachments

Soft gluon $k$ between an $A$-collinear line (index $\mu$) and the soft subgraph $S$ (index $\nu$):
$$
\boxed{\;K^{\mu\nu}_{\rm s}(k)=\frac{k^\mu\,n_A^\nu}{n_A\cdot k\pm\ii0},\qquad G_{\rm s}^{\mu\nu}=g^{\mu\nu}-K^{\mu\nu}_{\rm s},\qquad n_A=(1^+,0^-,\mathbf 0_T),\ n_A\cdot k=k^-\;}
$$
($+\ii0$ for an incoming $A$ line, $-\ii0$ for an outgoing one). $J\cdot K_{\rm s}\cdot S=(J\cdot k)\,S^-/k^-$: the Ward
identity on the jet side decouples the soft gluons from $J$ and attaches them to a Wilson line along $n_A$ in the
soft factor. The pure eikonal current $J^\mu\propto n_A^\mu$ is annihilated exactly by $G_{\rm s}$; the remainder is
$$
J\cdot G_{\rm s}\cdot S=J^-S^+-\mathbf J_T\cdot\mathbf S_T-\frac{(J^-k^+-\mathbf J_T\cdot\mathbf k_T)\,S^-}{k^-},
$$
of relative size $O\big(\lambda\,|\mathbf k_T|/|k^-|\big)$: **$O(\lambda)$ for soft $k$** (all components comparable), **$O(1)$ in the Glauber
region** $|k^+k^-|\ll\mathbf k_T^2$. Numerics (s5(3), three random draws): soft $\propto\lambda^{1.00}$; Glauber plateau at
$0.34,\,0.15,\,0.85$. Hence the soft approximation is valid only after the contour is deformed out of the Glauber
region (or the Glauber contribution is cancelled), cf. blueprint D7.3, L7.5, P7.19.

### 6.4 Which part is power suppressed — summary

* Collinear gluons into $H$: K leading (any number $\Rightarrow$ Wilson line); every additional G-gluon suppressed by
  $\ge\lambda$; exception: a single transversely polarized gluon as the active parton (gluon PDF).
* Soft gluons on collinear lines: K leading ($\Rightarrow$ Wilson lines in the soft factor); G suppressed by $\lambda$, outside
  the Glauber region only.
* QED original: K contains all IR divergences, G is IR finite.

---------------------------------------------------------------------------------------------------------

## 7. Literature cross-checks (summary)

| check | source (verified bibliographic data) | conversion | result |
|---|---|---|---|
| Wilson-line vertex and $\ii0$ | Collins 2011 Fig. 7.10 (errata) and eq. (11.6) | $g_{\rm Collins}=-g$ (verify Fig. 3.1); relative signs compared | PASS |
| Wilson-line rules | blueprint §0.4(10); c_pdf §2.4 | none | PASS |
| soft bremsstrahlung | Peskin–Schroeder §6.1 | $gt^a\to-e$ | PASS |
| $e^+e^-\to q\bar qg$ matrix element | Ellis–Stirling–Webber ch. 3 | unit photon coupling, $N_cC_F=4$ | PASS ($10^{-12}$) |
| $q\bar q\to gg$ cross section (physical pols; and $-g$ sums minus ghosts) | Combridge–Kripfganz–Ranft PLB 70 (1977) 234; ESW Tab. 7.1 | average $1/36$ | PASS ($2\times10^{-13}$) |
| ghost subtraction rule | standard (PS ch. 16) | — | PASS |
| collinear K/G | Collins 2011 eqs. (11.5)–(11.6) (errata) | $w_2=n_B$ | PASS (structure + power counting) |
| original GY K photon | Grammer–Yennie 1973 as reproduced in arXiv:1812.06468 eq. (9) | — | PASS (property); original not seen |
| one-gluon exchange between past-pointing lines (E7.24) | blueprint | — | PASS (0 for $k^+>0$; $-2\pi\ii/(k_T^2k^+)$ for $k^+<0$) |

Bibliographic data verified (INSPIRE) and **not** yet in `research/refs/refs.bib`: Weinberg, Phys. Rev. 140
(1965) B516 [48759]; Gatheral, Phys. Lett. B133 (1983) 90 [13589]; Frenkel & Taylor, Nucl. Phys. B246 (1984) 231
[15021]; Combridge, Kripfganz & Ranft, Phys. Lett. B70 (1977) 234 [120351]; Becchi, Rouet & Stora, Commun. Math.
Phys. 42 (1975) 127 [91174], Ann. Phys. 98 (1976) 287 [99402]; Tyutin, LEBEDEV-75-39, arXiv:0812.0580 [107066];
Kugo & Ojima, Prog. Theor. Phys. Suppl. 66 (1979) 1 [8189]; Labastida & Sterman, Nucl. Phys. B254 (1985) 425
[15811] (in the survey table); Sen, Indumathi & Choudhury, arXiv:1812.06468 (secondary source for the GY form).

---------------------------------------------------------------------------------------------------------

## 8. Discrepancies, corrections and suggestions for the outline/blueprint

1. **Blueprint L7.8** ("the sum equals the product of eikonal factors $\prod_ie\,n^\mu/(n\cdot k_i)$"): imprecise. The Ward
   identity gives $\sum_{\rm insertions}\prod_ik_{i\mu_i}H^{\mu_1\cdots\mu_m}=(\pm g)^mH_0$ (shifted kinematics, abelian); the eikonal
   factors appear only after the K projectors $\prod_i\frac{k_i^{\mu_i}n^{\nu_i}}{n\cdot k_i\mp\ii0}$, giving $H_0\prod_i\frac{\pm g\,n^{\nu_i}}{n\cdot k_i\mp\ii0}$, which by the
   eikonal identity is the abelian Wilson line; sign and $\ii0$ depend on initial/final state (§4.1, §5.4).
2. **Blueprint L7.6**: $K^{\mu\nu}=n_A^\mu k^\nu/(n_A\cdot k)$ must state which index goes where (first index on the soft
   subgraph, second on the $A$-collinear line — consistent with D7.3) and carry an $\ii0$. Attribution: the one-sided
   form is Collins' adaptation ("a Grammer–Yennie decomposition", 2011 eqs. (11.5)–(11.6)); the original GY (1973)
   K photon is the symmetric $b_kk_\mu k_\nu$ of §6.1.
3. **Blueprint D7.2(b)**: the K term should carry the $\ii0$ of Collins (11.6) ($-\ii0$ in DIS; $+\ii0$ for initial-state
   attachments).
4. **Blueprint L7.4** ("$O(\lambda)$, or $O(\lambda^2)$ for spin-averaged unpolarized observables"): a nuance found numerically —
   at amplitude level the G term is $O(\lambda^2)$ already for an on-shell massless parent quark and $O(\lambda)$ for a
   generic off-shell collinear parent (§6.2). Not a contradiction; the general bound is $O(\lambda)$.
5. **Blueprint L7.10** ("ghost contributions cancel in the sum"): should state its conditions. At tree level, two
   collinear K-gluons on the DIS hard part reproduce $W^{(2)}$ exactly with no ghost or three-gluon term (§5.4); ghost
   terms appear through the BRST identity when the other gluons are off shell/unphysical (§5.5–5.6). The all-order
   non-abelian combinatorics is [A].
6. **CONTEXT.md**: no error found. Suggest adding (C1)–(C4) of §1 as binding conventions (Fourier convention with
   $k$ flowing into the line; $n$ future-pointing; adiabatic regulator; $n_A$, $n_B$ with $n_B$ = Collins' $w_2$), and a
   sentence that the Wilson-line vertex is the quark–gluon vertex with $\gamma^\mu\to n^\mu$.
7. The task wording "soft gluon on an energetic quark line $\to g\,t^ap^\mu/(p\cdot k+\ii0)$" holds as written only for
   particular cases in our conventions (incoming antiquark absorbing $k$, outgoing antiquark emitting $k$; or the
   incoming quark absorbing $k$ in Collins' sign of $g$); the general table is §4.1.
8. Collins (2011) section numbers usable in the monograph (from the CUP table of contents and the errata):
   ch. 10 "Factorization and subtractions" (§10.3 Sudakov form factor, p. 321; §10.8 "Sudakov form factor
   factorization: first version", p. 359); ch. 11 "DIS and related processes in QCD" (§11.3 "Factorization for DIS",
   Grammer–Yennie decomposition eqs. (11.4)–(11.6) on p. 402; §11.4 renormalization of parton densities, p. 411;
   §11.9 "Ward identities to convert K gluons to Wilson line", p. 416, Fig. 11.6; index: "BRST transformation and
   operators in factorization, 407–411"); Fig. 7.10 (Wilson-line vertices in parton densities). The blueprint's
   "Collins ch. 11 (DIS) (verify)" is thereby confirmed for the Ward-identity/Wilson-line step.

## 9. Suggested rigor tags

| statement | tag | reason |
|---|---|---|
| Wilson-line Feynman rules (§2.5), conjugation, cut-diagram rules | [R] | complete derivation (iterated integrals) |
| abelian eikonal identity, shuffle identity, eikonal Ward identity, Wilson-line Ward identity | [R] | complete proofs |
| non-abelian decomposition / $O(g^2)$ webs | [R] | algebra; all-order exponentiation (Gatheral, Frenkel–Taylor) [A] |
| eikonal approximation, $m$ gluons $\to$ Wilson line | [R] | as an asymptotic statement in the soft region (power counting [A] when embedded in loops) |
| elementary and tree-level Ward identities (§5.1–5.5) | [R] | complete proofs + numerics |
| BRST/Slavnov–Taylor identities (§5.6) | [R] | in renormalized PT with DR |
| all-order conversion of non-abelian K-gluons into Wilson lines | [A] | combinatorics with ghosts only outlined |
| K/G algebra | [R] | identities |
| power suppression of G (collinear, soft outside Glauber) | [A] | standard power counting, proofs in outline |

## 10. Files

* `DERIVATION.md` (this file).
* `scripts/qcdtools.py`, `scripts/s1_wilson_rules.py`, `scripts/s2_eikonal_identity.py`,
  `scripts/s3_eikonal_approx.py`, `scripts/s4_ward_tree.py`, `scripts/s5_grammer_yennie.py`,
  `scripts/s6_i0_poles.py`; `run_all.sh`; logs in `logs/*.log`.
* LaTeX (Chinese, monograph style, labels prefixed `cw-`): `tex/c_wilson_rules.tex` (Wilson-line Feynman rules,
  Fig. `fig:cw-rules`, eikonal identities, Wilson-line Ward identity), `tex/c_wilson_eikonal_ward.tex` (eikonal
  approximation with Table `tab:cw-eikonal` and Fig. `fig:cw-eikonal`, tree-level Ward identities, DIS seed with
  Fig. `fig:cw-dis-seed`, non-abelian identities, BRST theorem and its status), `tex/c_wilson_gy.tex`
  (K/G decompositions, power counting, Fig. `fig:cw-kg`), `tex/c_wilson_bib.tex` (bibitems: verbatim copies from
  `refs_bibitems.tex` + NEW verified entries), test driver `tex/test_c_wilson.tex` with a copy of the preamble;
  `xelatex` (twice) builds `tex/test_c_wilson.pdf` (13 pages) with no errors, no overfull/underfull boxes, all
  references and citations resolved (the only warning, `\l@section not patched`, comes from the shared preamble).
  Figures use only the shared styles (`wilson`, `quark`, `gluon`, `longit` + `\longitmark`, `mom`, `opvertex`,
  `hard blob`, `jet blob`, `soft blob`, `photon`).
