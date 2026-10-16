# frontier/others — Rigorous and foundational progress on factorization (≈2010–2026), beyond LaMET

Directory: `"/Users/hao-cheng/Desktop/theorem proof/qcd_factorization_work/frontier/others"` (note the space).
Files: `OTHERS.md` (this report), `others.bib` (BibTeX, INSPIRE-verified), `scripts/s1–s5*.py`, `logs/*.log`.
Date of the literature check: 2026-10-10. Conventions and rigor tags: `CONTEXT.md`.

This report is the raw material for the **frontier chapter** of the monograph. LaMET (Ji) and Yizhuang Liu's
rigorous factorization programme are treated by the sibling agents (`frontier/lamet`, `frontier/yzliu`) and are
deliberately *not* repeated here. Everything below is either

* (a) **read in the original paper in this session** (arXiv full text; section/equation numbers refer to the arXiv
  version listed in §0.3), or
* (b) **checked by a script** in `scripts/` (check IDs `[S1]`–`[S5]`, logs in `logs/`), or
* (c) **INSPIRE-abstract level only** — marked *(abstract only)*, or
* (d) explicitly flagged **not verified**.

No result is quoted from memory without one of these labels.

---------------------------------------------------------------------------------------------------------

## 0. Scope, conventions, verification summary

### 0.1 Rigor tags (binding, from CONTEXT.md) and the extra qualifiers used here

| tag | meaning (CONTEXT.md) |
|---|---|
| **[R]** 严格 | mathematically complete proof at every order of renormalized perturbation theory (or in this text); non-perturbative validity stated separately |
| **[A]** 全阶论证 | standard all-order argument, accepted in the literature, some steps only sketched |
| **[P]** 部分 | proven/verified only at finite order, in a model, or for a subclass |
| **[C]** 猜想 | widely used but unproven, or the known proof has a gap |
| **[V]** 破坏 | known to be false (explicit counterexample/proof) |

Extra qualifiers used in this report (they refine, never replace, the tags):

* **†** — the proof exists only in an *unrefereed preprint* (arXiv only, as of 2026-10-10).
* **(model)** — rigorous in a specified model/class, not for QCD.
* **(cond.)** — rigorous *conditional on* an explicitly listed hypothesis that is itself only [A]/[C].
* **[Sx]** — the formula/claim was re-derived or numerically checked by script `sx`.

A *statement about a single integral* (e.g. a pinch criterion) has no "order"; for such statements [R] means a
complete proof for the stated class of integrals.

### 0.2 Verification scripts (all run with `python3 -I`; numpy 2.0.2, sympy 1.14, scipy 1.13.1, mpmath 1.3)

| script | content | result |
|---|---|---|
| `s1_landau_gordan.py` | Collins' geometric theorem ≡ Gordan's alternative (400 random instances, min-norm construction + LP exclusivity); Landau points for massless collinear/soft and massive threshold configurations; Collins' sign condition (8.15); Coleman–Norton displacements | 10/10 PASS |
| `s2_crs_yukawa_pdf.py` | Collins–Rogers–Sato Yukawa-model $\overline{\rm MS}$ pdf: DR derivation of their Eq. (55) from Eq. (58), cut-off version, sign pattern, thresholds $\xi\to0,1$ | 10/10 PASS |
| `s3_luxqed_pointlike.py` | LUXqed master formula on a point-like target reproduces Frixione's $O(\alpha)$ $\overline{\rm MS}$ photon-in-lepton pdf; role of $F_L$ and of the $\overline{\rm MS}$ conversion term | 3/3 PASS |
| `s4_resummed_series.py` | Becher–Neubert–Shao SLL tower ⇒ ${}_2F_2(1,1;2,\tfrac52;-w)$ closed form, first SLL coefficient, large-$w$ falloff; Liu–Neubert LDL series ⇒ ${}_2F_2(1,1;\tfrac32,2;\cdot)$ and match to NLO | 8/8 PASS |
| `s5_bk_kernel.py` | LO BK/BFKL dipole kernel: eigenvalue on $(x-y)^{2\gamma}$ equals $\chi(\gamma)=2\psi(1)-\psi(\gamma)-\psi(1-\gamma)$ (4 values of $\gamma$) | 5/5 PASS |

**Total: 36 checks, 36 PASS, 0 FAIL.**

### 0.3 Sources read in full in this session (arXiv versions)

Collins arXiv:2007.04085v1 (no journal publication; INSPIRE `Collins:2020euz` lists none; arXiv shows only v1);
Ma JHEP 05 (2020) 012 [1910.11304v2]; Feige–Schwartz PRD 90 (2014) 105020 [1403.6472v3];
Hollands–Kopper CMP 313 (2012) 257 [1105.3375v3]; Fröb–Holland [1603.08012v2, unpublished];
Hollands RMP 20 (2008) 1033 [0705.3340v4] (scanned for scope); Jantzen JHEP 12 (2011) 076 [1111.2589v2];
Semenova–Smirnov–Smirnov EPJC 79 (2019) 136 [1809.04325v3]; Gardi–Herzog–Jones–Ma–Schlenk JHEP 07 (2023) 197
[2211.14845v1]; Rothstein–Stewart JHEP 08 (2016) 025 [1601.04695v3]; Schwartz–Yan–Zhu PRD 97 (2018) 096017
[1801.01138v2]; Becher–Neubert–Shao PRL 127 (2021) 212002 [2107.01212v1]; Becher–Hager–Jaskiewicz–Neubert–
Schwienbacher PRL 134 (2025) 061901 [2408.10308v1]; Banfi–Forshaw–Holguin PRL 136 (2026) 221901 [2511.11799v1];
Liu–Neubert JHEP 04 (2020) 033 [1912.08818v3]; Liu–Mecaj–Neubert–Wang JHEP 01 (2021) 077 [2009.06779v2];
Beneke et al. JHEP 07 (2022) 144 [2205.04479v1]; Beneke–Schnubel–Szafron [2608.25502v1, unpublished];
Collins–Rogers–Sato PRD 105 (2022) 076010 [2111.01170v2]; Candido–Forte–Giani–Hekhorn EPJC 84 (2024) 335
[2308.00025v4]; Manohar–Nason–Salam–Zanderighi PRL 117 (2016) 242002 [1607.04266v3]; Frixione JHEP 11 (2019) 158
[1909.03886v2]; Becher–Neubert–Rothen–Shao JHEP 11 (2016) 019 [1605.02737v3]; Diehl–Gaunt–Schönwald JHEP 06
(2017) 083 [1702.06486v2]; partially (sections named in the text): Caron-Huot JHEP 05 (2015) 093 [1309.6521]
(Sec. 4, dipole formula); Balitsky–Chirilli PRD 77 (2008) 014019 [0710.4330] (Sec. VIII). **Collins, *Foundations of Perturbative QCD*** (CUP 2011; OA reissue 2023,
DOI 10.1017/9781009401845): chapters 11, 14, 15 read from the open-access chapter PDFs on Cambridge Core
(page numbers of the 2023 OA edition = 2011 edition). The OAPEN PDF is behind an anti-bot page and was **not**
used (and no attempt was made to circumvent it).

All other items: INSPIRE metadata + abstract (verified 2026-10-10), marked *(abstract only)* when a claim
depends on more than the abstract.

### 0.4 Global caveats

1. All "rigorous" results in this chapter are **perturbative** statements — including the OPE convergence theorems
   of §2, which are theorems of mathematical physics valid at each *fixed loop order* in scalar models. The only
   non-perturbative statements are those formulated in conformal field theory (light-ray OPE, §11.3) and explicit
   counterexamples. None of them controls the non-perturbative validity of factorization in QCD.
2. Several of the most important recent results (Collins 2020, Fröb–Holland 2016, Beneke–Schnubel–Szafron 2026,
   Gamberg et al. 2022, Bodwin et al. 2025) are **unrefereed preprints** (†).
3. Where two groups disagree (e.g. NLP TMD evolution; small-$x$ helicity intercept vs. BER; NQS vs. Bodwin et al.
   two-loop NRQCD test; Rothstein–Stewart/Gaunt vs. Schwartz–Yan–Zhu on pure-Glauber violation), both sides are
   reported with the exact scope of each claim.

---------------------------------------------------------------------------------------------------------

## 1. Landau condition, pinch surfaces and the status of Coleman–Norton

Every region analysis of the monograph (Ch. 3, power counting; Ch. 7–14) starts from "pinch surfaces of the
massless theory, located by the Landau equations, interpreted à la Coleman–Norton". Until 2020 the textbook
proofs of these statements had real gaps. This section records exactly what is now proven.

### 1.1 Setting and definitions (Collins 2020, Sec. II)

Collins treats integrals of the form (his Eq. (2.4))
$$
I(z)=\lim_{\epsilon\to0^+}\int_{\Gamma_0}\! d^dw\;\frac{B(w;z)}{\prod_{j=1}^N\big[A_j(w;z)+i\epsilon\big]^{n_j}},
\qquad n_j\notin\{0,-1,-2,\dots\},
$$
with: external parameters $z$ real; $\Gamma_0$ = all real $w$ ("physical region"; external momenta need not be on
shell); every $A_j$ real for real arguments and analytic; $B$ analytic. Momentum-space Feynman graphs are the
case $w=$ loop momenta, $A_j=k_j^2-m_j^2$ ($m_j=0$ allowed), plus linear "eikonal" denominators $A_j=n\cdot k_j$ from
Wilson lines and the approximated denominators used in factorization proofs.

* Contour deformations: $w=w_R+i\lambda\,v(w_R)$, $0\le\lambda\le1$, $v$ real, continuous, piecewise
  differentiable, $v=0$ on boundaries (Eq. (2.5)).
* *Allowed* deformation: no zero of $A_j+i\epsilon$ is crossed for $0<\epsilon\le\epsilon_0$, $0\le\lambda\le1$;
  *avoiding* a singularity at $w_S$; *trapped (pinched)* at $w_S$ ⇔ no allowed deformation avoids the
  singularity at $w_S$ (Defs. 1–5; precise operational versions in the paper).
* **Definition (Landau point, Collins Def. 6).** For dual vectors $D_1,\dots,D_N$ on a real vector space $V$,
  a Landau point is a list $\lambda_j\ge0$, not all zero, with $\sum_j\lambda_jD_j=0$. The *Landau condition*
  holds iff a Landau point exists (Def. 7). In applications $D_j=\partial A_j(w_S)$ for the $A_j$ that vanish
  at $w_S$; the sign constraint $\lambda_j\ge0$ is what distinguishes *physical-region* pinches.

### 1.2 Theorem (Collins 2020, Thm. 1) — physical-region pinch criterion   **[R]†**

> **Theorem 1.1.** Let $I$ be as above, and let $w_S$ be a real point where a non-empty set
> $\{A_j\}_{j\in J}$ vanishes. Assume in addition
> (a) every $A_j$ is at most quadratic in $w$;
> (b) *sign condition* (Collins Eq. (8.15)): writing $A_j(w_S+\delta w)=D_j\cdot\delta w+\tfrac12\,\delta w\cdot
> E_j\cdot\delta w$, for every direction $v_0$ with $D_j\cdot v_0=0$ the non-zero numbers
> $v_0\cdot E_j\cdot v_0$, $j$ "relevant" (i.e. $A_j(w_S)=0$, $D_j\neq0$, $D_j\cdot v_0=0$, $\alpha_j\neq0$ in the
> Landau point), all have the **same sign**.
> Then the integration is trapped at $w_S$ **if and only if** the derivatives $\{D_j=\partial A_j(w_S)\}_{j\in J}$
> admit a Landau point.

*Proof architecture.* Thm. 1 = Thm. 3 (purely geometric, below) ∘ Thm. 2 (contour deformations):

* **Thm. 2** (same hypotheses): the integration is *not* trapped at $w_S$ ⇔ there is a direction $v$ with
  $v\cdot\partial A_j(w_S)>0$ for every $A_j$ vanishing at $w_S$. The "⇐" direction is the elementary
  first-order computation $A_j(w_S+i\lambda v)+i\epsilon=i\lambda\,v\cdot\partial A_j+O(\lambda^2)+i\epsilon$
  (Eq. (2.7)). The "⇒" direction is the hard part: Collins shows (App. B.1) that the textbook assumption
  "avoiding a singularity requires a strictly positive first-order shift" is **false** — in $\ge2$ complex
  dimensions there exist *anomalous deformations* (Def. 15) that avoid a singularity with $v\cdot\partial A_j=0$
  (explicit example with the non-relativistic propagator $1/(E-p^2/2m+i\epsilon)$, $D=(1,-p/m)$). He then proves
  that when a Landau point exists no allowed deformation (anomalous or not) avoids the singularity
  (Sec. VIII); this is where (a) and (b) are used: the same-sign condition guarantees that one value of the
  auxiliary parameter $x$ makes the second-order terms negative for *all* relevant denominators simultaneously,
  and $\sum_j\alpha_jD_j\cdot\delta v=0$ then forbids compensation.
* **Thm. 3** (geometric): for dual vectors $D_1,\dots,D_N$ on a finite-dimensional real $V$, a "good
  direction" ($D_j(v)>0\ \forall j$) exists ⇔ there is no Landau point. Collins proves this in Secs. V–VII
  (~12 pages: positive cones, edge vectors, boundary segments).

*Where (b) holds* (Collins Sec. VIII B, verified **[S1(c)]**): standard propagators $k^2-m^2$ — for $m>0$ any
$\hat v$ with $k\cdot\hat v=0$ is spacelike or zero, for $m=0$, $k\neq0$ it is spacelike or null, so
$v_0\cdot E\cdot v_0=2\hat v^2\le0$; soft lines ($k=0$) have $D=0$ and are not "relevant"; Wilson-line
(eikonal) denominators are linear ($E=0$); non-relativistic propagators; and approximated denominators in which
a longitudinal light-front component is set to zero (quadratic in $k_T$ only, same sign). Hence Thm. 1.1
applies to all graphs (including Wilson lines and Glauber-approximated graphs) used in this monograph.

*Status/grade.* Complete written proof of a statement about single integrals, but **only in an arXiv preprint**
(v1, 8 Jul 2020, 39 pp.; no later version, no journal publication by 2026-10-10 — checked on arXiv and
INSPIRE). Collins himself flags that (a),(b) are artefacts of the method ("a more general proof (or
counterexample) would obviously be useful"). Grade **[R]†** for the class (a)+(b); **[C]** without (b).

### 1.3 New observation: Collins' Thm. 3 is Gordan's theorem of the alternative (1873)   **[R]** [S1(a)]

Collins remarks (footnote 6) that he had not found the needed geometric result in the convex-geometry
literature. It is in fact the classical **theorem of the alternative of P. Gordan**, *Math. Ann.* **6** (1873)
23–28 (DOI 10.1007/BF01442864, verified via Crossref): for a real $N\times d$ matrix $D$ (rows $D_j$),
*exactly one* of (I) $\exists v:\ Dv>0$ (componentwise), (II) $\exists\lambda\ge0,\ \lambda\ne0:\ D^{\mathsf T}\lambda=0$
holds. (I) = "good direction", (II) = "Landau point". A self-contained proof suitable for the monograph:

> **Proposition 1.2 (Gordan).** Fix any inner product on $V^*\simeq V$. Let $K=\mathrm{conv}\{D_1,\dots,D_N\}$
> (compact, convex). (i) If $0\in K$, the convex weights give a Landau point. (ii) If $0\notin K$, let $w$ be
> the unique point of $K$ of minimal norm. For $u\in K$, $t\in[0,1]$: $|w+t(u-w)|^2\ge|w|^2$ ⇒
> $\langle w,u-w\rangle\ge0$ ⇒ $\langle w,u\rangle\ge|w|^2>0$; in particular $D_j(w)\ge|w|^2>0$ for all $j$, so
> $w$ is a good direction. (iii) Both cannot hold: $0=\sum\lambda_jD_j(v)>0$ is absurd. ∎

This replaces Secs. V–VII of Collins' paper by six lines, and is *constructive* (the min-norm point is a valid
deformation direction with margin $|w|^2$ — useful for numerical contour deformation, cf. Gong–Nagy–Soper,
PRD 79 (2009) 033005; Becker–Weinzierl, PRD 86 (2012) 074009, both cited by Collins). Script **[S1(a)]** checks exclusivity and the margin $D_j\cdot w\ge|w|^2$
on 400 random instances (226 of type I, 174 of type II, worst margin deficit $-1\times10^{-14}$).
The analytic half (Thm. 2, anomalous deformations) is *not* affected by this observation and remains Collins'
own contribution. *Not verified:* whether the Gordan connection has been noted elsewhere in the Landau
literature (none of the papers read here mention it).

### 1.4 What exactly failed in the classic proofs (Collins Sec. IV)

* **Coleman–Norton** (Nuovo Cim. 38 (1965) 438): their proof works in the Feynman-parameter representation and
  tacitly assumes "momentum-space pinch ⇔ parameter-space pinch". This **fails in the simplest massless graph**:
  for the one-loop massless self-energy with $p^2=0$ the parameter integral has *no* pinch corresponding to the
  well-known collinear momentum-space pinch (Collins App. D.1); with linear (eikonal) propagators the parameter
  integral can have a pinch *independently* of the momentum integral (App. D.2). For massive theories the
  remaining gap is the zero-eigenvalue case of the quadratic form in their Eq. (4.1)-type expansion
  ("very exceptional points"), whose physical-region status is unresolved. Collins: "it is not the result that
  breaks down, but the proof."
* **ELOP** (Eden–Landshoff–Olive–Polkinghorne 1966) Sec. 2.1: avowedly heuristic; deformation "in the direction
  of the normal" (meaningless without a metric; there is a half-space of allowed directions); assumes non-zero
  first-order shifts (false, App. B.1); the condition (2.1.19b) lacks the positivity $\lambda_j\ge0$ needed for
  physical-region pinches; refers for rigor to an inaccessible Fotiadi–Froissart–Lascoux–Pham manuscript.
* **Necessary vs sufficient.** The Landau condition is necessary *and sufficient for a trap of the contour*
  (Thm. 1.1), but only **necessary for a singularity of $I(z)$** in the external parameters (App. A gives a
  trapped contour without singularity). For factorization what matters is the *location of traps*
  (regions), not singularities — so Thm. 1.1 is exactly the needed statement.

### 1.5 Corollary: Coleman–Norton picture in massless theories, without Feynman parameters   **[R]†** [S1(b,d)]

> **Corollary 1.3.** For a momentum-space graph with lines $k_j=\sum_L\eta_{jL}\ell_L+(\text{external})$,
> $\eta_{jL}\in\{0,\pm1\}$, quadratic denominators $k_j^2-m_j^2$ and eikonal denominators $n_j\cdot k_j$, under
> the hypotheses of Thm. 1.1, the integration is trapped at real loop momenta $\{\ell_L\}$ iff there are
> $\lambda_j\ge0$, not all zero, supported on the lines that are on shell (resp. $n_j\cdot k_j=0$), such that
> for every loop $L$:
> $$\sum_j\eta_{jL}\,\lambda_j\,\Delta_j^\mu=0,\qquad \Delta_j^\mu=\begin{cases}k_j^\mu&\text{(propagator)}\\ n_j^\mu&\text{(eikonal line)}\end{cases}.$$
> Equivalently (Coleman–Norton): with displacements $\Delta x_j=\lambda_j\Delta_j$ assigned to the on-shell lines
> and zero length to off-shell lines, there exist vertex positions consistent with all displacements, i.e. the
> pinch is a classical process of on-shell particles (light-like for massless lines; eikonal lines move along
> $n_j$); off-shell lines collapse to points (hard vertices); zero-momentum massless lines have $D_j=0$ and are
> always pinched (soft lines).

*Proof.* $\partial(k_j^2-m_j^2)/\partial\ell_L^\mu=2\eta_{jL}k_{j\mu}$, $\partial(n_j\cdot k_j)/\partial\ell_L^\mu=
\eta_{jL}n_{j\mu}$; so $\sum_j\lambda_jD_j=0$ is the displayed loop equation; Thm. 1.1 gives "trapped ⇔ Landau
point"; the loop equations are exactly the closure conditions for vertex positions. ∎ (Checks: collinear
self-energy, Landau point $(1-x,x)$, equal displacements; soft point; massive threshold; massive single
on-shell line not trapped — **[S1(b,d)]**.)

*Status.* This derivation never uses Feynman parameters, so Collins' objection to the CN *proof* does not
apply; the grade is inherited from Thm. 1.1 (**[R]†**). What it does **not** give (Collins' open items 2–3,
and Ma 2020 §2.2): (i) *which* of the vanishing denominators actually trap the contour and the cone of allowed
deformations of the others (needed to justify the approximations of Ch. 7); (ii) pinch surfaces of
*approximated* graphs $t_\sigma A$ (momentum is not conserved between hard/jet/soft "bubbles", so the CN picture
of the original graph does not apply and a separate analysis is needed — done by Ma for wide-angle
amplitudes, §1.6); (iii) power counting near the pinch surfaces (Libby–Sterman), which remains [A].

### 1.6 Related all-order and foundational results on IR structure

**(a) Ma's IR forest formula for wide-angle amplitudes** — Ma, JHEP 05 (2020) 012 [read]. **[A]**
*Statement.* For any massless gauge-theory amplitude $A$ with wide-angle kinematics (arbitrary number of external
legs, Feynman gauge), with approximation operators $t_\sigma$ (hard-collinear and soft-collinear) attached to
the leading pinch surfaces $\sigma$,
$$\Big[\sum_{F\in\mathcal F[A]}\ \prod_{\sigma\in F}(-t_\sigma)\,A\Big]_{\rm div}=0\qquad\text{(Ma Eq. (1.1))},$$
i.e. all IR divergences — including the new ones generated by the subtraction terms — cancel pairwise, and,
with the Ward identity, $A$ can be rewritten in a gauge-invariant factorized form (soft × jet × hard, Ma
Eq. (5.28)), generalizing Collins' Sudakov-form-factor result to arbitrary wide-angle amplitudes.
*Proof architecture.* Power counting for pinch surfaces $\rho\{\sigma_n\cdots\sigma_1\}$ of repeatedly
approximated amplitudes (at worst logarithmic, App. A); "enclosed pinch surfaces" are leading pinch surfaces of
$A$ (Thms. 3–4, a new "algebra of normal spaces"); case-by-case pairwise cancellation (nested, overlapping,
exotic); Ward identities for the factorized form. *Hypotheses.* Wide angle (Glauber region not pinched — by the
contour-deformation argument; forward/Regge kinematics explicitly excluded), massless partons, amplitude level.
*Grade.* [A] (long refereed all-order argument; not independently re-derived here).

**(b) Feige–Schwartz, "Hard-soft-collinear factorization to all orders"**, PRD 90 (2014) 105020 [read].
**[A]** Amplitude-level statement: at leading power, QCD amplitudes equal matrix elements of a product of
collinear and soft operators (with kinked Wilson lines for the soft-collinear overlap), regulator- and
gauge-independent; soft currents and splitting functions are process independent to all orders.
*Scope (verified in the text):* "we will only have final state collinear directions, so we can ignore Glauber
scaling"; configurations with incoming and outgoing partons collinear are avoided — consistent with the known
violation of strict collinear factorization for space-like splittings (§4.3).

**(c) Coordinate-space factorization (Erdoğan–Sterman).** Erdoğan PRD 89 (2014) 085016; Erdoğan–Sterman PRD 91
(2015) 065033; PRD 95 (2017) 116015; Sterman–Erdoğan EPJ ST 235 (2026) 1493 *(abstract only)*. **[A]**
Coordinate-space pinch surfaces of fixed-angle amplitudes (collinear and short-distance limits become UV
divergences), finite set of regions per diagram, nested subtractions, Ward identities ⇒ hard × jet × soft;
multiplicative renormalizability of products of light-like Wilson lines; webs as integrals of UV-finite
functions over surfaces.

**(d) Local (integrand-level) IR factorization** — Anastasiou–Sterman JHEP 07 (2019) 056; Anastasiou et al.
JHEP 04 (2021) 222; Anastasiou–Sterman JHEP 05 (2023) 242; Anastasiou–Karlen–Sterman–Venkata JHEP 11 (2024)
043; further 2025–26 preprints *(abstract only)*. **[P]** Explicit locally finite two-loop amplitude integrands
built from IR universality (factorization of soft/collinear singularities at the integrand level), for specific
electroweak-production processes; an existence proof of the integrand-level version of factorization at two
loops for these processes, not a general theorem.

**(e) Mathematical Landau analysis** *(abstract only unless stated)*: Mizera–Telen, JHEP 08 (2022) 200
(Landau discriminants); Fevola–Mizera–Telen, PRL 132 (2024) 101601 and CPC 303 (2024) 109278 (principal Landau
determinants); Berghoff–Panzer, J. Geom. Phys. 216 (2025) 105539 (relative Picard–Lefschetz hierarchies);
Helmer–Papathanasiou–Tellander, PRD 114 (2026) L011901 (Whitney stratifications); Hannesdottir–Mizera,
SpringerBriefs (2023) ("What is the $i\epsilon$ for the S-matrix?"). These give algorithms/rigorous algebraic-
geometric descriptions of the *singular loci* of Feynman integrals as functions of external kinematics
(complexified, all sheets). They are complementary to Thm. 1.1: they do not address physical-region traps of
the *integration contour* with the $\lambda_j\ge0$ positivity, which is what regions in factorization need.

**(f) IR factorization of amplitudes and the dipole formula.** The all-order structure "amplitude = $Z(\epsilon)\times$
finite hard function", with $Z$ generated by a soft anomalous dimension acting in colour space, follows from
hard–jet–soft factorization of amplitudes (items (a)–(c)) — **[A]**. Its simplest form, the *dipole formula*
(only pairwise colour correlations; Becher–Neubert, PRL 102 (2009) 162001; Gardi–Magnea, JHEP 03 (2009) 079), is exact
through two loops but **fails at three loops**: Almelid–Duhr–Gardi, PRL 117 (2016) 172002 *(abstract)*, computed the
complete three-loop correction — non-dipole terms already for three coloured partons (a constant), kinematic
dependence through conformal cross ratios for ≥4 partons; strict collinear factorization of the splitting-amplitude
anomalous dimension is preserved. Independently, Caron-Huot (JHEP 05 (2015) 093, Sec. 4, checked) showed that
BFKL dynamics in the Regge limit rules out the dipole conjecture from four loops. Dipole formula beyond two loops:
**[V]**.

### 1.7 Status table for §1

| statement | grade | key reference |
|---|---|---|
| Physical-region pinch ⇔ Landau point (denominators ≤ quadratic, sign condition (8.15)) | [R]† | Collins 2007.04085 Thm. 1 |
| same without the sign condition | [C] | Collins Sec. VIII B |
| geometric half (good direction ⇔ no Landau point) | [R] | Gordan 1873; Prop. 1.2 [S1] |
| "positive first-order shift needed to avoid a singularity" | [V] | Collins App. B.1 (anomalous deformations) |
| CN classical picture, massive theories, via Feynman parameters | [A] (gap at zero eigenvalues) | Coleman–Norton 1965; Collins Sec. IV |
| CN classical picture, massless theories, via Feynman parameters (as published) | proof [V], result true | Collins App. D |
| CN picture from Thm. 1.1 (momentum space, massless included) | [R]† | Cor. 1.3 [S1] |
| Landau condition ⇒ singularity of $I(z)$ | [V] (only necessary) | Collins App. A |
| IR forest formula + factorized form, massless wide-angle amplitudes | [A] | Ma 2020 |
| amplitude-level H-S-C factorization, final-state collinear only | [A] | Feige–Schwartz 2014 |
| coordinate-space factorization of fixed-angle amplitudes | [A] | Erdoğan–Sterman 2015, 2017 |
| integrand-level local IR factorization (specific 2-loop processes) | [P] | Anastasiou–Sterman et al. 2019–2024 |
| IR factorization $A=Z(\epsilon)H$ with a colour-space soft anomalous dimension | [A] | (a)–(c) |
| dipole formula for the soft anomalous dimension beyond two loops | [V] | Almelid–Duhr–Gardi 2016; Caron-Huot 2015 |

---------------------------------------------------------------------------------------------------------

## 2. Rigorous operator product expansion: existence, gauge invariance, convergence

The OPE is the oldest factorization theorem and the only one with genuinely rigorous mathematical-physics
results. For the monograph it underpins Ch. 4–5 (e⁺e⁻ correlator, DIS moments). The question is what has been
*proven*, in which theory, and in which sense (asymptotic vs convergent).

### 2.1 Background: the asymptotic OPE in renormalized perturbation theory

Zimmermann, Ann. Phys. 77 (1973) 570: in BPHZ-renormalized perturbation theory of renormalizable (scalar)
theories, products of composite operators have a short-distance expansion
$\mathcal O_A(x)\mathcal O_B(y)\sim\sum_C\mathcal C_{AB}^C(x-y)\,\mathcal O_C(y)$ in the sense of
insertions into Green functions, with remainder vanishing faster than any prescribed power once enough
operators are kept (asymptotic expansion), at every order. For gauge theories the gauge-invariant version
relies in addition on BRST/Slavnov–Taylor identities and on the classification of operator mixing
(Kluberg-Stern–Zuber 1975; Joglekar–Lee 1976; see §8) — standard textbook material (Collins 1984), which the
monograph grades [R] in perturbation theory for the moment form of DIS factorization (Ch. 5). The post-2006
results below make this *self-contained and mathematically rigorous* in specific settings, and add new
statements (curved spacetime, convergence, associativity, recursion).

### 2.2 Hollands 2007: OPE in curved spacetime (scalar)   **[R] (model)**

Hollands, CMP 273 (2007) 1 [gr-qc/0605072] *(abstract only)*: algorithm constructing the OPE for perturbative
interacting scalar QFT on arbitrary Lorentzian curved spacetimes to arbitrary order; the remainder goes to zero
at short distances in expectation values in arbitrary Hadamard states. The OPE coefficients (a) depend only
locally and covariantly on metric and couplings, (b) satisfy associativity, (c) an RG equation, (d) a microlocal
wave-front-set condition, (e) a "scaling expansion" (curvature polynomials × Lorentz-invariant Minkowski
distributions).

### 2.3 Hollands 2008: renormalized Yang–Mills in curved spacetime; OPE closes on gauge-invariant operators   **[R] (pure YM)**

Hollands, Rev. Math. Phys. 20 (2008) 1033 [0705.3340v4; abstract and scope checked]: perturbative quantum
Yang–Mills theory on any globally hyperbolic spacetime is constructed as a formal-power-series algebra of
observables (BRST cohomology of an auxiliary gauge-fixed algebra with ghosts and antifields, renormalized Ward
identities ensuring conservation of the interacting BRST current and nilpotency of the interacting BRST
charge). Consequences proven: **the OPE closes on the space of gauge-invariant operators, and the RG flow does
not leave it.** Matter fields are only discussed (Sec. 5.1, "Matter fields, anomalies": possible anomalies with
chiral fermions); QCD with quarks is not constructed in that paper.

### 2.4 Flow-equation (Wilson–Polchinski) proofs of renormalizability with explicit bounds

| theory | result | reference | grade |
|---|---|---|---|
| massive $\varphi^4_4$ | perturbative renormalizability, effective Lagrangians | Keller–Kopper–Salmhofer, Helv. Phys. Acta 65 (1992) 32 | [R] (model) |
| QED (with electrons) | renormalizability proof | Keller–Kopper, PLB 273 (1991) 323; CMP 176 (1996) 193 | [R] (model) |
| spontaneously broken SU(2) YM–Higgs | renormalizability, restoration of STI | Kopper–Müller, CMP 209 (2000) 477; RMP 21 (2009) 781 | [R] (model) |
| massless $\varphi^4_4$ | all-order uniform momentum bounds | Guida–Kopper arXiv:1103.5692 (unpubl.) | [R]† |
| SU(2) YM (pure) | renormalizability with physical renormalization conditions, IR control of massless correlators | Efremov–Guida–Kopper, J. Math. Phys. 58 (2017) 093503 | [R] (pure YM) |
| Euclidean YM, semisimple group, arbitrary composite operators | "complete, self-contained, mathematically rigorous" renormalizability with Ward (BRST) identities for correlators of arbitrary composite operators; tree-weighted bounds; UV and IR controlled | Fröb–Holland–Hollands, J. Math. Phys. 57 (2016) 122301 | [R] (pure YM) |

(abstracts; FHH 2016 abstract and arXiv journal-ref verified.)

### 2.5 Convergence of the OPE (scalar $\varphi^4_4$)   **[R] (model)**

> **Theorem 2.1 (Hollands–Kopper, CMP 313 (2012) 257; read, Eq. (7)).** Euclidean $g\varphi^4$ in four
> dimensions, mass $m>0$, fixed loop order $l$. Composite fields $\mathcal O_A=\partial^{w_1}\varphi\cdots
> \partial^{w_n}\varphi$, dimension $[A]=n+\sum_i|w_i|$. Spectator fields $\varphi(f_{p_i})=\int d^4x\,\varphi(x)
> f_{p_i}(x)$ with $\hat f_{p_i}$ compactly supported in a ball of radius $\epsilon$ around $p_i$. Summing the
> OPE over all $C$ with $[C]-[A]-[B]\le\Delta$,
> $$\Big|\big\langle\mathcal O_A(x)\mathcal O_B(0)\textstyle\prod_i\varphi(f_{p_i})\big\rangle-\sum_C\mathcal C^C_{AB}(x)
> \big\langle\mathcal O_C(0)\prod_i\varphi(f_{p_i})\big\rangle\Big|
> \le m^{[A]+[B]+n}\sqrt{[A]![B]!}\,\tilde K^{[A]+[B]}\prod_i\sup|\hat f_{p_i}|\;
> \Big(\sup(1,\tfrac{|\vec p|_n}{m})\Big)^{2([A]+[B])(n+2l+1)+3n}\sum_{\lambda=0}^{n/2+2l}\frac{\log^\lambda\sup(1,\frac{|\vec p|_n}{m})}{2^\lambda\lambda!}
> \;\frac{1}{\sqrt{\Delta!}}\Big(\tilde K\,m|x|\,\sup(1,\tfrac{|\vec p|_n}{m})^{n+2l+1}\Big)^{\Delta},$$
> $\tilde K=\tilde K(n,l)$. Since $c^\Delta/\sqrt{\Delta!}\to0$ for every $c$, **the OPE converges at every
> finite $|x|$** (not only asymptotically), at each loop order.

*Proof architecture.* Wilson–Wegner–Polchinski flow equations with IR cutoff $\Lambda$, UV cutoff $\Lambda_0$;
inductive bounds (in loop order and number of legs) on the remainder of the OPE uniform in $\Lambda_0$; a refined
induction hypothesis that reproduces itself. Side result: convergence of the gradient expansion of the effective
action at fixed loop order (their Cor. 3.1). *Caveats (from the paper):* convergence depends on the "state"
(spectator momenta of compact support; worse high-energy behaviour of the state ⇒ worse convergence); the
$\hbar$ (loop) series itself is not addressed; in Minkowski space convergence is expected only for spacelike
separations.

* **Massless case:** Holland–Hollands–Kopper, CMP 342 (2016) 385 — same conclusion for massless
  $\varphi^4_4$, with entirely new techniques to control exceptional-momentum singularities ("tree
  dominance") *(abstract only)*. **[R] (model)**
* **Recursion and associativity:** Holland–Hollands, CMP 336 (2015) 1555 (a UV-finite formula for
  $\partial_g\mathcal C$ in terms of OPE coefficients only; recursive construction from free-field coefficients;
  conjectured to hold non-perturbatively) and J. Math. Phys. 56 (2015) 122303 (strong associativity to all
  orders; "coherence theorem": 2-point OPE coefficients determine the $n$-point ones), both for $\varphi^4_4$
  *(abstract only)*. **[R] (model)**

### 2.6 Yang–Mills: existence and gauge invariance of the OPE   **[R]† (pure YM)**

Fröb–Holland, arXiv:1603.08012 (v2; not published; read, Sec. 1.1):

> **Theorem 2.2 (FH Thm. 1).** For an arbitrary massless superficially renormalizable theory, to arbitrary
> fixed order, renormalization conditions can be chosen such that
> $\langle\mathcal O_{A_1}(x_1)\cdots\mathcal O_{A_s}(x_s)\rangle\sim\sum_B\mathcal C^B_{A_1\cdots A_s}(x)
> \langle\mathcal O_B(x_s)\rangle$ with remainder bound
> $\lim_{\tau\to0}\tau^{[\mathcal O_A]-D+\delta}\big[\langle\cdots\rangle-\sum_{[B]<D}\cdots\big]=0$ for all
> $\delta>0$, and OPE coefficients of bounded scaling degree; valid also in states generated by smeared fields
> without exceptional momenta (incl. finite-energy states after Wick rotation).
>
> **Theorem 2.3 (FH Thm. 2).** For a massless renormalizable gauge theory, the OPE coefficients satisfy the
> BRST Ward identity (so the OPE of gauge-invariant operators involves only gauge-invariant operators) provided
> the $E(4)$-equivariant cohomology class $H^{1,4}_{E(4)}(\hat s|d)$ vanishes — true for pure YM with
> semisimple gauge group (the only non-trivial classes are parity-odd: the axial anomaly), "but not, for
> instance, in the presence of chiral fermions in non-real representations".

Recursion relations for OPE coefficients, quantum BRST differential and antibracket, UV-finite from the start;
associativity follows. *Grade:* **[R]†** — the bounds used (FHH 2016) are established for pure YM only, and the
paper is an unrefereed preprint.

### 2.7 Status for QCD with quarks (what the monograph can and cannot claim)

1. **Asymptotic OPE, all orders, with gauge-invariant operators:** standard (Zimmermann-type normal products
   + BRST + Joglekar–Lee classification + algebraic renormalization, Piguet–Sorella 1995). No single
   self-contained flow-equation proof including quarks exists in the papers checked here; FHH/FH cover pure YM,
   Keller–Kopper covers QED with fermions. Grade for QCD: **[R] in renormalized PT as a combination of
   classical results**, with the caveat that the fully self-contained modern proof is pure-YM only. *Not
   verified:* that no flow-equation proof for QCD with quarks exists anywhere (none found in INSPIRE searches
   "flow equation + QCD/fermion").
2. **Convergence of the OPE:** proven only for scalar $\varphi^4_4$ (massive and massless), at fixed loop
   order. For YM/QCD: **[C]** (FH remark: "no obstacle in principle", but requires refined bounds).
3. **Minkowski light-cone OPE (DIS):** obtained from the Euclidean OPE + analyticity/dispersion relations for
   moments (Ch. 5); the Hollands–Kopper convergence statement is Euclidean; its Minkowski analogue is expected
   only for spacelike separations, so it does **not** imply convergence of the light-cone expansion relevant
   to DIS beyond moments.
4. **Non-perturbative status:** none of the above is non-perturbative. The OPE as an *axiom* of QFT (Hollands–
   Wald programme) is motivated by, but not derived from, these results.

| statement | grade |
|---|---|
| asymptotic OPE to all orders (scalar, flat or curved spacetime) | [R] |
| OPE closes on gauge-invariant operators, pure YM (curved spacetime; Euclidean flat) | [R] (Hollands 2008); [R]† (FH 2016) |
| same for QCD with quarks | [R] in PT via classical results; no self-contained modern proof |
| OPE convergent at finite distance, fixed loop order, $\varphi^4_4$ massive/massless | [R] (model) |
| OPE convergent for YM/QCD | [C] |
| associativity / recursion of OPE coefficients ($\varphi^4_4$; YM†) | [R] (model); [R]† |

---------------------------------------------------------------------------------------------------------

## 3. The method of regions: what is proven, and where it can fail

The method of regions (MoR; "expansion by regions") is the computational backbone of SCET and of every explicit
check of a factorization theorem. Its status has moved substantially since 2011.

### 3.1 The recipe (Beneke–Smirnov, Nucl. Phys. B522 (1998) 321) — as formulated by Jantzen 2011, Sec. 1

1. Divide loop-momentum space into regions and, in each, Taylor-expand the integrand according to the region's
   scaling; 2. integrate every expanded term over the **whole** integration domain; 3. set scaleless integrals to
   zero. The claim is that the sum over regions reproduces the asymptotic expansion of the integral in the small
   parameter (to all orders in it).

### 3.2 Euclidean ("large/small") limits: rigorous   **[R]**

For limits typical of Euclidean space (off-shell large-momentum and large-mass limits) the expansion can be
written as a sum over asymptotic subgraphs with Taylor operators, and the remainder after $n$ terms can be
identified with a UV/IR-subtracted integral via a variant of Zimmermann's forest formula: Smirnov, CMP 134
(1990) 109 (INSPIRE-verified; content as summarized in Semenova–Smirnov–Smirnov 2019, Sec. 1, and in Gardi et
al. 2022, Sec. 6 — both read). This is the rigorous core. It covers e.g. heavy-mass decoupling and the
Euclidean OPE of §2, **not** the Sudakov, threshold, Regge or on-shell limits relevant for factorization.

### 3.3 Jantzen 2011: a conditional general derivation   identity **[R](cond.)**, applicability **[P]**

Jantzen, JHEP 12 (2011) 076 [read, Sec. 3]. Regions $x\in R$ with expansion operators $T^{(x)}$ and domains
$D_x$ on which $T^{(x)}$ converges absolutely. **Conditions:** (1) the $D_x$ are disjoint and cover the full
domain $D$; (2) all expansions commute, $T^{(x)}T^{(x')}=T^{(x')}T^{(x)}$ (relaxed in his Sec. 5 for
non-commuting expansions); (3) every integral (original, expanded, restricted or not) is regularized; (4) each
expansion still converges absolutely (or is properly regularized) when integrated over all of $D$. Then
(his master identity (3.22))
$$\int_D I\;=\;\sum_{x}F^{(x)}-\sum_{\{x,x'\}}F^{(x,x')}+\sum_{\{x,x',x''\}}F^{(x,x',x'')}-\dots-(-1)^NF^{(x_1\cdots x_N)},\qquad
F^{(x_1\cdots x_n)}=\int_D T^{(x_1)}\cdots T^{(x_n)}\,I .$$
The usual recipe keeps only the first sum; the *overlap contributions* (multiple expansions) vanish when they are
scaleless (each single expansion is homogeneous in the expansion parameter with a region-specific power), but
can be non-zero for other regularizations — they are the MoR counterpart of SCET **zero-bin subtractions**
(his Sec. 7: forward scattering evaluated without analytic regulators). *Gap acknowledged by the author:* the
derivation exchanges infinite summations, which requires absolute convergence; "I cannot provide a rigorous
proof for this convergence issue in the general case" (Sec. 3). For truncated (finite-order) expansions the
issue is absent. Verified explicitly in examples: one-loop large-momentum expansion, threshold expansion
(hard/potential/soft/ultrasoft; convergence checked in his App. A.2), forward scattering.
*Grade:* the identity is an exact consequence of (1)–(4) (+ summation exchange): **[R](cond.)**; checking
(1)–(4) for multi-loop Minkowski integrals is the open part: **[P]**.

### 3.4 Semenova–Smirnov–Smirnov 2019: geometric formulation and partial proofs   **[R]** (positive polynomials) / **[C]** (general)

EPJC 79 (2019) 136 [read, Secs. 1–2, 8], building on the Newton-polytope algorithm `asy` of Pak–Smirnov
(EPJC 71 (2011) 1626) for non-threshold expansions. Lee–Pomeransky representation (up to Γ-factors)
$G(t,\varepsilon)=\int_0^\infty d^nx\,P(x,t)^{-\delta}$, $\delta=2-\varepsilon$, $P=\mathcal U+\mathcal F$; for a
general polynomial $P=\sum_{w\in S}c_w\,x_1^{w_1}\cdots x_n^{w_n}t^{w_{n+1}}$ with **all $c_w>0$**, Newton polytope
$NP\subset\mathbb R^{n+1}$.

> **Main conjecture.** $G(t,\varepsilon)\sim\sum_{\gamma}\int d^nx\,\mathcal M_\gamma\big(P^{-\delta}\big)$, the sum over
> the *essential facets* $\gamma$ of $NP$ (inward normal $r^\gamma$ with $r^\gamma_{n+1}>0$, normalized to 1);
> $\mathcal M_\gamma$ = substitute $x_i\to t^{r_i^\gamma}x_i$ and expand in $t$ (with auxiliary analytic
> regularization to define each term).

**Proven** (their Sec. 8): convergence analysis of the LP representation and a generalization of Speer's theorem
(definition of the dimensionally regularized integral via analytic regularization); equivalence of the
Feynman-parametric ($\mathcal U\mathcal F$, code `asy`) and LP prescriptions for Feynman integrals; **the
leading order of each essential facet**; **all orders when only one facet is essential**. Not proven: the
general-order statement with several facets. Positivity of all coefficients is essential — this is the
"Euclidean-type" situation; Minkowski kinematics with mixed-sign $\mathcal F$ is outside the theorem.

### 3.5 Minkowski kinematics: regions ↔ Landau equations ↔ facets, and hidden regions

**(a) On-shell expansion of wide-angle Green functions** — Gardi–Herzog–Jones–Ma–Schlenk, JHEP 07 (2023) 197
[read]. Massless propagators, off-shell Green functions with non-exceptional momenta, expansion $p_i^2\to0$.
*Results:* every IR region (hard $H$, jets $J_i$ collinear to $p_i$, soft $S$) is a solution of the Landau
equations and a facet of the Newton polytope of $\mathcal U\mathcal F$ (resp. $\mathcal U+\mathcal F$); explicit
graph-theoretical requirements on $H,J,S$ proven necessary and sufficient for a facet (their App. C);
graph-finding algorithm reproducing the polytope regions. **Theorem 4** (their Sec. 5): for *jet-pairing soft*
regions (each connected soft component attaches to exactly two jets) the non-analytic dependence factorizes into
powers of $p_i^2$, hence **multiple on-shell expansions commute**; this covers all Sudakov form-factor diagrams
and all planar wide-angle diagrams; non-commutativity requires non-planar graphs with ≥3 on-shell legs and a soft
vertex. *Explicit caveat (Sec. 6):* the facet-based MoR is guaranteed to capture all regions only when there is
an analytic continuation from a Euclidean domain (no cancellations in $\mathcal F$); for $2\to2$ massless
scattering this fails, "we have not provided a proof of this". Grades: facet characterization **[R]**;
commutativity theorem **[R](cond.: MoR valid)**; completeness in Minkowski kinematics **[C]** (but see (c)).

**(b) Graph-theoretical all-order region forms** — Ma, JHEP 09 (2024) 197 *(abstract only)*: generic all-order
forms of the regions (lower facets) for (i) on-shell expansion of wide-angle scattering, (ii) soft expansion of
wide-angle scattering, (iii) mass expansion of heavy-to-light decay. **[R]** as statements about lower facets;
validity of MoR itself as in (a).

**(c) Hidden regions from cancellations — the facet recipe fails** — Gardi–Herzog–Jones–Ma, JHEP 08 (2024) 127
*(abstract only)*: in massless $2\to2$ scattering, from **three loops** in particular non-planar graphs,
cancellations between opposite-sign terms of $\mathcal F$ produce **pinches in parameter space** (not endpoint
singularities); standard sector decomposition and facet-based MoR then fail. Fix: linearize the graph
polynomial and split the integration domain at the singular locus ("dissecting the polytope"); the new facets
are **new regions**, sometimes governing the leading power: in the on-shell expansion they have ≥2 connected
hard subgraphs; in the Regge limit they are **Glauber** modes. Independently, Becher–Hager–Jaskiewicz–Neubert–
Schwienbacher (PRL 134 (2025) 061901, read) found a three-loop active–active **Glauber region** in gap-between-
jets box/pentagon integrals "missed by the available computer codes used to search for regions" (§4.4).
Earlier: Ananthanarayan–Pal–Ramanan–Sarkar, EPJC 79 (2019) 57 (Landau equations + power geometry + Gröbner
bases reveal potential/Glauber regions in examples) and the `pySecDec` implementation (Heinrich et al., CPC 273
(2022) 108267) *(abstracts only)*.

**Consequence for the monograph.** "MoR with regions = lower facets of the Newton polytope" is **[V]** as a
general statement in Minkowski kinematics (explicit three-loop counterexamples), and MoR with a correctly
completed region set is **[C]** in general (proven: Euclidean limits [R]; positive-polynomial facets at LO
[R]). SCET factorization theorems inherit this: they presuppose a *complete* list of modes; Glauber modes are
precisely the kind of region that hides in parameter space.

### 3.6 Status table for §3

| statement | grade | reference |
|---|---|---|
| MoR for Euclidean large-momentum / large-mass limits | [R] | Smirnov 1990 |
| Jantzen master identity under conditions (1)–(4) + summation exchange | [R](cond.) | Jantzen 2011 |
| overlap terms = zero-bin subtractions, vanish if scaleless | [R](cond.) | Jantzen 2011 Sec. 3, 7 |
| LP-facet prescription: LO of each essential facet; all orders with one facet (positive coeffs) | [R] | SSS 2019 |
| LP-facet prescription, all orders, several facets | [C] | SSS 2019 (main conjecture) |
| regions of on-shell expansion = Landau solutions = facets; H/J/S requirements | [R] (facets) | Gardi et al. 2022; Ma 2023 |
| commutativity of multiple on-shell expansions (jet-pairing soft regions) | [R](cond.) | Gardi et al. 2022 Thm. 4 |
| "regions = lower facets" in Minkowski kinematics | [V] (3 loops, non-planar 2→2) | Gardi–Herzog–Jones–Ma 2024 |
| MoR with a complete region set, general Minkowski limits | [C] | — |

---------------------------------------------------------------------------------------------------------

## 4. Glauber gluons: effective theory, cancellations, and factorization violation

Background (Ch. 10, 12; `research/c_glauber`): in inclusive Drell–Yan the Glauber region is leading power but
cancels after the sum over cuts / contour deformation (Bodwin 1985; Collins–Soper–Sterman 1985, 1988) — grade
[A] with known gaps (Collins 2011, §14.4.8, read: rapidity-graduated exchanges "very quickly one gets into a
situation of trying to develop a good and deductive QCD version of Regge theory"; "the current versions of
genuine proofs are evidently formidable"). This section records the post-2010 developments.

### 4.1 Rothstein–Stewart 2016: an EFT for Glauber exchange   **[A]** (construction), claims graded individually

Precursor: Bauer–Lange–Ovanesyan, JHEP 07 (2011) 077 (a Glauber mode must be added to SCET for consistency in
spectator interactions; *abstract only*).
Rothstein–Stewart, JHEP 08 (2016) 025 [read: abstract, Sec. 5.2 (Eq. (5.21), Table 2), Sec. 11]. SCET is extended
by Glauber *potential operators*; at leading power the complete Glauber Lagrangian (SCET$_{\rm II}$; identical
in SCET$_{\rm I}$ before the BPS field redefinition) is
$$
\mathcal L_G^{\rm II(0)}=e^{-ix\cdot\mathcal P}\sum_{n,\bar n}\sum_{i,j=q,g}\mathcal O_n^{iB}\,\frac{1}{\mathcal P_\perp^2}\,
\mathcal O_s^{BC}\,\frac{1}{\mathcal P_\perp^2}\,\mathcal O_{\bar n}^{jC}
\;+\;e^{-ix\cdot\mathcal P}\sum_{n}\sum_{i,j=q,g}\mathcal O_n^{iB}\,\frac{1}{\mathcal P_\perp^2}\,\mathcal O_s^{j_nB},
$$
with collinear bilinears $\mathcal O_n^{qB}=\bar\chi_nT^B\frac{\bar{n}\!\!\!/}{2}\chi_n$,
$\mathcal O_n^{gB}=\frac i2f^{BCD}\mathcal B^C_{n\perp\mu}\frac{\bar n}{2}\cdot(\mathcal P+\mathcal P^\dagger)\mathcal B^{D\mu}_{n\perp}$, and
a gauge-invariant pure-glue soft operator $\mathcal O_s^{BC}$ (built from soft Wilson lines $\mathcal S_n,\mathcal S_{\bar n}$,
$\mathcal P_\perp$ and $\mathcal B_{S\perp}$, $G_s^{\mu\nu}$; its one-gluon Feynman rule is the **Lipatov vertex**, but it
also governs emissions with ≥2 soft gluons). Notation as in RS (their $\bar n\cdot p$ = large component of an
$n$-collinear momentum; the monograph's SCET conventions agree, CONTEXT.md).

Claims and their status:

* (i) The operator basis is fixed by tree-level and one-loop matching from QCD to SCET$_{\rm I,II}$, and "there are
  no loop corrections to this form" (RS Sec. 5.3) — **[A]**.
* (ii) Rapidity renormalization of the one-loop forward amplitude gives gluon Reggeization; the rapidity RGEs
  of the leading soft and collinear functions in forward scattering are the **BFKL equation** — **[A]**
  (agreement with known results).
* (iii) Glauber zero-bin subtractions make hard-scattering soft/collinear loops insensitive to Wilson-line
  directions; conversely some Glauber exchanges can be absorbed into Wilson lines by choosing their directions
  (the EFT version of the CSS "deformation into Wilson lines") — **[A]**.
* (iv) Spectator–spectator (S–S) exchanges resum to a phase $e^{i\phi(b_\perp)}$, $b_\perp$ conjugate to the relative
  transverse momentum $\Delta p_\perp$ of the spectators; the phase **cancels iff the $\Delta p_\perp$ integral is
  unrestricted** (RS Eq. (11.13)). RS add: "taken alone it is far from a proof of factorization, even in the
  abelian case". **[R]** for the eikonal computation as stated.
* (v) If the measurement constrains $\Delta p_\perp\sim Q_*$ with perturbative spectators, S–S Glauber exchanges
  "spoil the factorization ... starting at $O(\alpha_s^4)$" for beam thrust, transverse thrust, $E_T$ (RS Sec. 11.1).
  **Contradicted** for pure Glauber ladders and single-scale IR-safe observables by the all-order cancellation
  argument of Schwartz–Yan–Zhu 2018 (§4.2(c), [A]), which explicitly "disproves previous claims"; the claim survives
  only for multi-differential measurements. Status: **disputed / not established**.

### 4.2 Spectator interactions in hadron–hadron collisions: violation vs cancellation

**(a) Gaunt 2014** (JHEP 07 (2014) 110) *(abstract + SYZ's summary, read)*: for hadronic transverse energy
$E_T$ the CSS cancellation fails at the level of two Glauber gluons exchanged between spectators; relating these
graphs to additional soft scatterings he argues that "MPI-sensitive observables" ($E_T$, beam thrust
$B^+_{a,b}$, transverse thrust) receive leading-power MPI/spectator-Glauber contributions and do not obey the
standard hard–soft–collinear factorization. **[C]** (argument, not a proof; partly superseded by (c)).

**(b) Zeng 2015** (JHEP 10 (2015) 189) *(abstract)*: explicit counterexample, in QCD with scalar quarks, to any
"generalized factorization" in which the two collinear sectors decouple, for Drell–Yan with jet vetoes / beam
thrust: decoupling implies zero dependence on the longitudinal spins of the hadrons, but S–S Glauber exchange
gives a non-zero leading-power spin asymmetry. **[V] (model)** for generalized factorization of that observable.

**(c) Schwartz–Yan–Zhu 2018** (PRD 97 (2018) 096017) [read]. **Theorem (as stated):** for *pure Glauber ladder*
graphs (S–S exchanges, perturbative spectators), all amplitude-level factorization-violating effects cancel at the
cross-section level for **any infrared-safe single-scale observable** (e.g. $E_T$, beam thrust):
$\int dz\,d\bar z\sum_{\rm cuts}(\text{ladders})=0$. *Proof architecture:* conformal variables $(z,\bar z)$ for the
spectator transverse kinematics in which the phase-space integral is inclusive in $z$ for every single-scale
observable, using scale invariance of the $2\to2$ amplitudes; explicit NLO check (cancellation between the $O(\epsilon^0)$
two-loop and $\epsilon\times1/\epsilon$ one-loop terms); all orders: IR divergences of the ladders exponentiate into a
phase (their Eq. (53) for the singular part), the remainder is integrable. *Corollary:* leading violation needs
**soft radiation off the Glauber rungs (Lipatov vertex)**, linking factorization violation to the underlying event.
*Scope (verbatim):* "Our argument does not apply to doubly-differential observables, like those studied in
[Zeng]." **[A]** (all-order argument for the stated class).

**(d) Mitov–Sterman 2012** (PRD 86 (2012) 114038) *(abstract)*: soft final-state interactions between high-$p_T$
heavy particles and spectators are power suppressed for single-particle-inclusive cross sections with an
unconstrained recoiling partner (e.g. single-top inclusive in $t\bar t$), but give **leading-power** effects in
multi-particle-inclusive cross sections (incl. pair $q_T$ distributions) without hard recoil; NP effects suppressed
by $\Lambda/p'_T$. **[A]**. Related: $t\bar t$ small-$q_T$ resummation requires a non-trivial soft factor with
azimuthal correlations (Catani–Grazzini–Torre, Nucl. Phys. B890 (2014) 518, *abstract only*).

### 4.3 Strict collinear factorization is violated for space-like splittings (amplitude level)   **[V]**

* **Catani–de Florian–Rodrigo 2012** (JHEP 07 (2012) 026) *(abstract; details in research/c_glauber)*: strict
  (process-independent) collinear factorization holds at tree level but **fails at one loop and beyond in the
  space-like collinear limit** (initial-state collinear radiation); a generalized factorization holds in which the
  splitting factor depends on momenta and colour of the non-collinear partons; explicit one- and two-loop results;
  implications for non-abelian logarithms from NNLO and mass-singularity factorization from N³LO.
* **Forshaw–Seymour–Siódmok 2012** (JHEP 11 (2012) 066): for pure QCD the breaking appears in non-inclusive
  hadron–hadron cross sections at **three loops**, driven by the non-commutation of Coulomb/Glauber exchanges with
  other soft exchanges — the same structure as super-leading logarithms; beyond QCD (hard processes with phase
  differences between colour topologies) already at two loops.
* **Schwartz–Yan–Zhu 2017** (PRD 96 (2017) 056005): these violations are reproduced in SCET with Glauber
  operators from an amplitude factorized *before* the splitting (one Glauber at one loop, two at two loops);
  Glauber contributions are non-analytic in external momenta through the rapidity regulator; when no initial- and
  final-state particles are collinear, the Glauber contribution is contained in the soft one.
* **Dixon–Herrmann–Yan–Zhu 2020** (JHEP 05 (2020) 135; erratum 2024): two-loop soft current in full colour
  (tripole terms); "in the limit where the outgoing soft gluon is also collinear with an incoming hard parton,
  potentially dangerous factorization-violating terms can arise".
* **Guan–Herzog–Ma–Mistlberger–Suresh 2025** (JHEP 01 (2025) 090): time-like splitting amplitudes to three loops;
  owing to the violation of strict factorization, space-like splitting amplitudes are given for three-parton
  amplitudes at three loops (expansion-by-subgraph technology based on MoR).

### 4.4 Super-leading logarithms (SLLs) and their resummation

*Definition.* In non-global hadron-collider observables (gap between jets, jet vetoes) with veto scale $Q_0\ll Q$,
$L=\ln(Q/Q_0)$, the expected LL are $\alpha_s^nL^n$; complex (Coulomb/Glauber) phases in the hard amplitudes break
colour coherence and produce **double** logarithms $\alpha_s^3L^3\times(\alpha_sL^2)^n$, i.e. $\alpha_s^4L^5$ at four
loops (Forshaw–Kyrieleis–Seymour, JHEP 08 (2006) 059; colour-basis-independent: JHEP 09 (2008) 128; ordering
variable: Ángeles-Martínez–Forshaw–Seymour JHEP 12 (2015) 091; general coherence violation in almost all
soft-sensitive hadron-collider observables: Forshaw–Holguin JHEP 12 (2021) 084, erratum 2024).

> **Result 4.1 (Becher–Neubert–Shao, PRL 127 (2021) 212002; read Eqs. (14)–(21))** **[A]** [S4].
> In the SCET factorization $\sigma(Q_0)=\sum_{a_1a_2}\int dx_1dx_2\sum_{m\ge4}\langle\mathcal H_m(\{n\},Q,\mu)\otimes
> \mathcal W_m(\{n\},Q_0,x_1,x_2,\mu)\rangle$ (their Eq. (1)), iterating the one-loop anomalous dimension
> (soft + collinear parts, Glauber phase $\propto i\pi$) gives the tower
> $$\hat\sigma_n^{\rm SLL}=\Big(\frac{\alpha_s}{4\pi}\Big)^{n+3}L^{2n+3}\frac{(-4)^n\,n!}{(2n+3)!}\sum_{r=0}^n\frac{(2r)!}{4^r(r!)^2}\,C_{rn},$$
> with explicit colour traces $C_{rn}$ (their Eq. (18), checked by them with ColorMath to eight loops). For
> $q\bar q$ singlet exchange in forward scattering ($J_2=J_{43}/2=\Delta Y$, the gap rapidity)
> $$\Delta\hat\sigma^{(S)}=\sum_{n\ge0}\hat\sigma_n^{\rm SLL}=-\hat\sigma_B\,\frac{4C_F}{3\pi}\,\alpha_s^3L^3\,\Delta Y\;
> {}_2F_2\!\big(1,1;2,\tfrac52;-w\big),\qquad w=\frac{N_c\alpha_s}{\pi}L^2 .$$

*Verified [S4]:* the closed form follows term by term ($n\le8$) from their Eqs. (14), (19); the first SLL is
$\hat\sigma_1^{(S)}=\hat\sigma_B\,\frac{4}{15\pi^2}C_FN_c\,\alpha_s^4L^5\Delta Y$; the $n=0$ term is single-logarithmic;
${}_2F_2(1,1;2,\frac52;-w)\simeq\frac32\ln w/w$ at large $w$ (numerically $1.497$ at $w=10^8$), i.e. a slow
power-like falloff instead of Sudakov $e^{-cw}$. SLLs arise also for $2\to1$ (from four loops) and $2\to0$
processes such as $q\bar q\to V$ with a central jet veto (from five loops).

**Further results** *(abstracts; verified metadata):*
* Becher–Neubert–Shao–Stillger, JHEP 12 (2023) 116: full SCET factorization theorem for non-global LHC observables
  (hard functions × low-energy matrix elements at $Q_0$), one-loop RG; first all-order LL resummation of SLLs for
  arbitrary $2\to M$; alternating series, terms much larger than the sum; sizeable for $pp\to2$ jets, suppressed for
  $H/Z(+$jet$)$. **[A]**
* Böer–Neubert–Stillger JHEP 10 (2023) 075; Böer–Hager–Neubert–Stillger–Xu JHEP 02 (2024) 109; JHEP 08 (2024)
  035 (RG-improved, running coupling); JHEP 08 (2024) 036 (large $N_c$): the full "Glauber series" (arbitrary
  numbers of Glauber phases $(i\pi)^2$) at LL. **[A]**
* Becher–Hager–Martinelli–Neubert–Schwienbacher–Stillger, JHEP 01 (2025) 171: $pp\to2$ jets, all partonic channels;
  some $q\bar q\to q\bar q$ interference terms only $1/N_c$-suppressed; numerically important for small $Q_0$.
* Banerjee–Grünhofer–König–Li–Neubert–Scholze, JHEP 02 (2026) 092: massive final states ($t\bar t$) give an
  additional Coulomb phase and a new source of SLLs.

### 4.5 SLLs and PDF factorization: "factorization restoration"   **[P]**

Since PDF evolution is single-logarithmic, double-logarithmic collinear evolution *must* be compensated by
low-energy interactions between the incoming partons if PDF factorization is to survive.

> **Result 4.2 (Becher–Hager–Jaskiewicz–Neubert–Schwienbacher, PRL 134 (2025) 061901, read; JHEP 01 (2026) 024,
> abstract).** In the low-energy matrix elements $\mathcal W_m$ of gap-between-jets cross sections there is a
> three-loop **perturbative active–active Glauber contribution**, unambiguously defined in pure DR, which at LL
> has exactly the structure needed to turn the double-logarithmic evolution back into single-logarithmic DGLAP
> evolution below the veto scale; it "breaks soft-collinear factorization at the cross-section level but restores
> PDF factorization". The JHEP paper derives consistency relations from EFT renormalization conditions and verifies
> them by an explicit three-loop computation.

*Status (authors' own words):* "our analysis does not amount to a proof of PDF factorization, [but] demonstrates
that the breaking of collinear factorization does not necessarily translate into a breaking of PDF
factorization." The relevant Glauber region is missed by automated region finders (cf. §3.5(c)). **[P]** (three
loops, LL structure).

### 4.6 One-jettiness contains "super-super-leading" logarithms   **[V]** (LL-coherence-violation approximation) [read]

> **Result 4.3 (Banfi–Forshaw–Holguin, PRL 136 (2026) 221901; read, Eqs. (1)–(18)).** For one-jettiness
> (Stewart–Tackmann–Waalewijn, PRL 105 (2010) 092002)
> $\tau_1=\frac1Q\sum_k\min\{n_a\cdot p_k,n_b\cdot p_k,n_J\cdot p_k\}$ in colour-singlet + jet production
> ($qg\to qZ$ studied), coherence-violating logarithms start at **$\alpha_s^4\ln^6(1/\tau_1)$** relative to Born:
> $$\frac{d\sigma_1^{\rm CVL}}{dx_a\,dx_b\,d\mathcal B}\simeq\sum_{a=q,g}\mathcal A_a\Big(\frac{\alpha_s}\pi\Big)^4(-i\pi)^2\,\frac1{480}\,
> \ln^6\frac1{\tau_1},\qquad \mathcal A_q=\frac83N_c^2T_R^4f^q_Af^g_B\sigma^{(0)}_{qg},\quad
> \mathcal A_g=-\frac{32}{3}N_c^2T_R^4f^g_Af^q_B\sigma^{(0)}_{gq}$$
> (PDFs at $\mu_F=\tau_1Q$), and are expected as $\alpha_s^nL^{2n-2}$ for $n\ge4$ ($\alpha_s^5L^8$ argued). Consequently
> the cumulant **cannot** be written in the standard exponentiated form
> $\sigma(\tau_1)=\sigma\,e^{-\frac{\alpha_s}{2\pi}L^2(2C_F+C_A)}[g_0(\alpha_sL)+\alpha_sg_1(\alpha_sL)+\dots]$ (their
> Eq. (2)).

*Mechanism (from the paper):* Coulomb phases make $[\mathbf T^2_{ad},\mathbf T^2_s]\neq0$ (the colour of the
incoming parton $a$ is resolved from that of its collinear emissions — explicit breaking of initial-state angular
ordering); the extra logarithm comes from a double-logarithmic soft wide-angle phase-space area that never touches
the collinear limit, hence **no extra poles** — consistent with PDF factorization at $\tau_1Q$, but in conflict with
the claim (Alioli et al., PRD 109 (2024) 094009, cited by BFH) that $\tau_1$ in $V+$jet is free of non-global and
super-leading logarithms (basis of N³LL resummation and of $N$-jettiness slicing at higher orders).
*Hypotheses/approximations:* fixed coupling, strongly ordered soft-collinear emissions, multiple-uncorrelated-
emission approximation of the measurement, dipole-$k_T$ ordering (the $\alpha_s^4L^6$ term is ordering-independent,
$\alpha_s^4L^5$ is not). *Grade:* **[V]** for the all-order validity of the standard (3-Wilson-line soft function)
factorization/exponentiation of $\tau_1$ in hadron collisions **at the level of an explicit LL-CVL computation**;
independent confirmation not yet available (single group, 2025–26).

### 4.7 Status table for §4 (and consequences for the monograph's grades)

| statement | grade | reference |
|---|---|---|
| Glauber cancellation in inclusive DY (all orders) | [A] (unchanged) | CSS 1985/88; Collins 2011 §14.4 |
| RS Glauber Lagrangian complete at LP, no loop corrections | [A] | Rothstein–Stewart 2016 |
| S–S Glauber phase cancels iff $\Delta p_\perp$ unconstrained | [R] (eikonal) | RS Eq. (11.13) |
| pure-Glauber ladders cancel for all single-scale IR-safe observables | [A] | Schwartz–Yan–Zhu 2018 |
| standard factorization for MPI-sensitive observables ($E_T$, beam thrust) in $pp$ | [C] (violation expected via soft emission off Glauber rungs / MPI) | Gaunt 2014; SYZ 2018 |
| generalized (decoupled-collinear) factorization, DY + beam-thrust spin asymmetry | [V] (model) | Zeng 2015 |
| strict space-like collinear factorization of amplitudes | [V] (1 loop) | CdFR 2012 |
| collinear factorization of non-inclusive $pp$ cross sections (pure QCD) | [V] from 3 loops | FSS 2012 |
| SLL tower and LL resummation, arbitrary $2\to M$ | [A] | BNS 2021; BNSS 2023 [S4] |
| PDF factorization for gap-between-jets despite SLLs | [P] (3 loops) | Becher et al. 2025, 2026 |
| standard SCET factorization/exponentiation of $\tau_1$ in $V+$jet | [V] (LL-CVL computation) | Banfi–Forshaw–Holguin 2026 |
| heavy final states: FSI power-suppressed for single-inclusive, LP for multi-inclusive | [A] | Mitov–Sterman 2012 |

---------------------------------------------------------------------------------------------------------

## 5. Next-to-leading-power (NLP) factorization and endpoint factorization

### 5.1 The problem

At subleading power in a scale ratio $\lambda$, SCET factorization formulas contain convolutions
$\int_0^1dz\,H(z)\,\langle O(z)\rangle$ of single-scale functions that **diverge at the endpoints** ($z\to0,1$) once the
functions are renormalized/expanded in $d=4$. In SCET$_{\rm I}$-type problems the divergences are regularized
by $\epsilon$, but the $1/\epsilon^n$ poles of the convolution cannot be removed by renormalizing the individual
functions ("an unexpected failure of dimensional regularization and the $\overline{\rm MS}$ scheme", Liu–Neubert
2020, abstract); in SCET$_{\rm II}$-type problems additional rapidity regulators are needed. First seen in
exclusive $B$ decays (power corrections in QCD factorization), it is generic at NLP: threshold Drell–Yan/Higgs/DIS
off-diagonal channels, event shapes with a power-suppressed partonic channel, light-quark-loop induced Higgs
amplitudes.

### 5.2 $h\to\gamma\gamma$ via a $b$-quark loop: the first complete endpoint-factorized theorem   **[A]**

$\lambda=m_b/M_h$; the amplitude is $O(\lambda)$ (one mass insertion), with soft-quark exchange between the two
photon-collinear sectors.

* **Bare theorem** (Liu–Neubert, JHEP 04 (2020) 033 [read], Eq. (34)):
  $$\mathcal M_b=H_1\langle O_1\rangle+\int_0^1dz_1\,H_2(z_1)\langle O_2(z_1)\rangle+(z_1\to z_2)+H_3\langle O_3\rangle,$$
  $\langle O_3\rangle$ = convolution of two **radiative jet functions** $J$ and a **soft-quark function** $S$ in
  $\ell_\pm$ (Eq. (33)); with an analytic (rapidity) regulator $\eta$ the convolutions are defined (Eq. (50));
  expand in $\eta$ before $\epsilon$.
* **Refactorization conditions** (Eqs. (54), (55)): with $[\![f(z)]\!]$ the terms of $f$ leading as $z\to0$
  (modulo logarithms),
  $$[\![\bar H_2(z)]\!]=-H_3\,J(zM_h^2),\qquad [\![\langle O_2(z)\rangle]\!]=-\frac{g_\perp^{\mu\nu}}{2}\int_0^\infty\frac{d\ell_+}{\ell_+}
  J(-\bar n_1\!\cdot k_1\,\ell_+)\,S(\ell_+\ell_-)\Big|_{z=\ell_-/\bar n_1\cdot k_1}.$$
  They imply cancellation of the rapidity-regulator dependence **to all orders**; the dimensionally regularized
  endpoint divergences are removed by rearranging the theorem (subtractions in the $T_2$ term, cutoffs in $T_3$).
  In LN 2020 the conditions were verified at NLO and conjectured to all orders ("it would be desirable to derive
  them rigorously from SCET").
* **Renormalized theorem — Liu–Mecaj–Neubert–Wang, JHEP 01 (2021) 077** [read, Eq. (4.1)]: the two
  $D$-dimensional refactorization conditions are **proven** (Sec. 3; the second via the discontinuity of the soft
  function, their Eqs. (3.12)–(3.14)); the renormalized formula ($\bar z=1-z$)
  $$\mathcal M_b=H_1(\mu)\langle O_1(\mu)\rangle+2\!\int_0^1\!dz\Big[H_2(z,\mu)\langle O_2(z,\mu)\rangle-\frac{[\![\bar H_2(z,\mu)]\!]}{z}[\![\langle O_2(z,\mu)\rangle]\!]
  -\frac{[\![\bar H_2(\bar z,\mu)]\!]}{\bar z}[\![\langle O_2(\bar z,\mu)\rangle]\!]\Big]
  +g_\perp^{\mu\nu}\lim_{\sigma\to-1}H_3(\mu)\!\int_0^{M_h}\!\frac{d\ell_-}{\ell_-}\!\int_0^{\sigma M_h}\!\frac{d\ell_+}{\ell_+}J(M_h\ell_-,\mu)J(-M_h\ell_+,\mu)S(\ell_+\ell_-,\mu)\Big|_{\rm LP}$$
  holds to all orders, the non-commutativity of endpoint cutoffs and renormalization being absorbed into
  $H_1(\mu)$; RGEs for all ingredients (most anomalous dimensions at two loops); prediction of the three-loop
  logarithms $O(\alpha_b\alpha_s^2L^k)$, $k=6,5,4,3$, $L=\ln(-M_h^2/m_b^2)$, agreeing with a numerical computation, and
  **disagreeing** with earlier conventional predictions of the subleading-log series.
* **Leading double logs** (Kotsky–Yakovlev, PLB 418 (1998) 335; Akhoury–Wang–Yakovlev, PRD 64 (2001) 113008;
  extended to three loops by Penin and Liu–Penin; quoted as LN Eq. (3) with LN refs. [40–44] checked):
  $\mathcal M_b|_{\rm LDL}=\mathcal M_0\hat L^2\sum_n\frac{n!}{(2n+2)!}\big(-\frac{C_F\alpha_s}{2\pi}\hat L^2\big)^n
  =\mathcal M_0\frac{\hat L^2}{2}\,{}_2F_2\big(1,1;\tfrac32,2;-\frac{C_F\alpha_s}{8\pi}\hat L^2\big)$, reproduced by the
  SCET theorem. **[S4]**: the hypergeometric identity (term by term to $n=10$) and the match of the $n=0,1$ terms
  to the exact NLO amplitude ($\hat L^2/2$ and $\frac{C_F\alpha_s}{4\pi}(-\hat L^4/12)$, LN Eq. (1)).

*Grade:* **[A]** — all-order SCET argument with proven refactorization conditions; SCET's own assumptions
(complete mode set, no Glauber issue: a decay with colour-neutral final state) are standard.

**$gg\to h$ via light quarks** — Liu–Neubert–Schnubel–Wang, JHEP 06 (2023) 183 *(abstract)*: same structure with
external colour; the **"refactorization-based subtraction" (RBS) scheme** yields a theorem free of endpoint
divergences; three-loop logs $\alpha_s^3\ln^k$, $k=6,\dots,3$, predicted; first three towers
$\alpha_s^n\ln^{2n-k}(-M_h^2/m_b^2)$, $k=0,1,2$, resummed. **[A]**. Conventional-QCD precursors: Liu–Penin PRL 119
(2017) 262001; JHEP 11 (2018) 158 (all-order LL for mass-suppressed amplitudes) *(abstract)* **[A]**.

**Position-space SCET analyses (Bodwin, Ee, Lee/Kang, Wang)** *(abstracts)*: analyticity, renormalization and
evolution of the soft-quark function (PRD 104 (2021) 016010); renormalization of the radiative jet function (PRD
104 (2021) 116025); gauge invariance of radiative jet functions in position-space SCET (PRD 109 (2024) 056020);
"hidden self-energy contributions of collinear functions" (arXiv:2512.11647†). These scrutinize individual
ingredients of the endpoint theorems; Beneke–Ji–Wang JHEP 05 (2024) 246 give a rapidity-divergence-free definition
of the $gg\to h$ soft-quark operator and relate the $\gamma\gamma\to h$ soft kernel to the $B$-meson LCDA kernel
to all orders (conformal symmetry), bootstrapping it to two loops.

### 5.3 Beneke et al.: threshold and event-shape NLP factorization, $d$-dimensional consistency, endpoint conditions

* **Threshold DY at NLP** — Beneke–Broggio–Jaskiewicz–Vernazza, JHEP 07 (2020) 078 *(abstract)*: general
  factorization near $z=Q^2/\hat s\to1$ for $q\bar q\to\gamma^*+X$ at any subleading power; NLP collinear functions
  (operator matching; checked against MoR to NNLO). **"Factorization holds only before the dimensional regulator is
  removed, due to a divergent convolution"** when collinear and soft functions are expanded around $d=4$ first ⇒
  problem for NLP resummation beyond LL. **[P]** (bare, $d$-dimensional).
* **LL threshold resummation at NLP** — DY: JHEP 03 (2019) 043; $gg\to H$: JHEP 01 (2020) 094 *(abstracts)*. **[A]** at
  LL.
* **Off-diagonal DIS at large $x$ from $d$-dimensional refactorization** — JHEP 10 (2020) 196 *(abstract)*:
  $1/\epsilon$-pole cancellation between regions bootstraps the LL series; reproduces Vogt's Bernoulli-number series
  for the off-diagonal DGLAP kernel at large $x$; identifies off-diagonal splitting functions and soft-quark
  Sudakov logs as **two-scale objects**. **[A]** at LL.
* **"Gluon thrust" (off-diagonal, power-suppressed $q\bar q$ vs gluon jet)** — JHEP 07 (2022) 144 [read: Secs. 1–2,
  4]: operatorial **endpoint factorization conditions** (their Eq. (63) and its soft-quark analogue (II)): the
  $r\to0$ limit of the B-type (anti-collinear) term equals the $\omega\to\infty$ limit of the A-type (soft) term to all
  orders, a "prerequisite for endpoint factorization", checked at $O(\alpha_s)$. With them, a factorization formula
  whose terms are separately endpoint-finite and expressed through renormalized four-dimensional functions;
  first resummation of an endpoint-divergent SCET$_{\rm I}$ observable at LL by RG methods; agreement with the earlier
  $d$-dimensional result. **[A]** at LL (all-order endpoint conditions argued, verified at one loop).
* **NLP soft functions** — Beneke–Ji–Sünderhauf–Wang, JHEP 05 (2025) 067 (DY $qg$ channel, renormalization and
  RGE) *(abstract)*.
* **NLP DIS and PDF factorization** — Beneke–Schnubel–Szafron, arXiv:2608.25502† [read: abstract, conclusion]:
  position-space SCET factorization of the off-diagonal DIS channel at NLP in $1-x$ (leading twist); the anti-
  hardcollinear $B1$-current and soft-collinear (subleading-Lagrangian) contributions have endpoint divergences
  resolved by endpoint factorization relations; **the PDF near threshold becomes a two-scale object at NLP**; at
  LP the threshold PDFs coincide with the $\xi\to1$ limit of $\overline{\rm MS}$ PDFs and $\overline{\rm MS}$
  renormalization commutes with the endpoint limit; LL resummation both in $d$-dimensional $\overline{\rm MS}$ and in
  a refactorization "endpoint scheme", with the all-order relation between the two PDF definitions (to double-log
  accuracy). **[A]†** at LL.

### 5.4 Other NLP structures (diagrammatic and SCET) *(abstracts)*

* Next-to-eikonal / generalized Low–Burnett–Kroll factorization for NLP threshold logarithms: Bonocore–Laenen–
  Magnea–Melville–Vernazza–White JHEP 06 (2015) 008; Bonocore–Laenen–Magnea–Vernazza–White JHEP 12 (2016) 121
  (non-abelian); checks at N³LO (Bahjat-Abbas et al. JHEP 10 (2018) 144). **[A]/[P]**.
* SCET NLP event shapes: Moult–Stewart–Vita–Zhu JHEP 08 (2018) 013 (first subleading-power resummation, thrust in
  $H\to gg$, LL); Moult–Stewart–Vita JHEP 11 (2019) 153 (radiative functions). **[A]** at LL.
* $q_T$ at NLP: power-law rapidity divergences and a pure rapidity regulator (Ebert et al. JHEP 04 (2019) 123), see §6.

### 5.5 Status table for §5

| statement | grade | reference |
|---|---|---|
| endpoint divergences generic at NLP; $\overline{\rm MS}$ of individual functions insufficient | [R] (explicit examples) | LN 2020; BBJV 2020 |
| $h\to\gamma\gamma$ ($b$ loop): renormalized endpoint-factorized theorem, all orders | [A] | LN 2020; LMNW 2021 |
| refactorization conditions for $h\to\gamma\gamma$, all orders ($D$-dim.) | [A] (proved within SCET) | LMNW 2021 Sec. 3 |
| $gg\to h$ (light quarks), RBS scheme, three towers of logs | [A] | LNSW 2023 |
| threshold DY at NLP: bare $d$-dim. factorization; fails if $d\to4$ first | [P] | BBJV 2020 |
| LL resummation at NLP: DY, $gg\to H$, off-diagonal DIS, gluon thrust | [A] (LL only) | Beneke et al. 2019–2022 |
| NLP DIS; threshold PDF two-scale at NLP; $\overline{\rm MS}$ ↔ endpoint scheme | [A]† (LL) | BSS 2026 |
| NLP resummation beyond LL for endpoint-divergent cross sections with incoming hadrons | [C]/open | — |

---------------------------------------------------------------------------------------------------------

## 6. TMD factorization beyond leading power

The LP TMD factorization theorem for DY/SIDIS/$e^+e^-$ (Ch. 11) is [A]. At NLP ($q_T/Q$) three kinds of
corrections enter: **kinematic** (from the exact kinematics/frame dependence of the LP term), **intrinsic/
twist-3** (quark–gluon–quark correlators, "TMD twist"), and **dynamic** (new hard functions). All results below
are **perturbative and assume that Glauber exchanges do not spoil factorization at NLP** (stated explicitly by
Ebert–Gao–Stewart; implicit elsewhere).

* **TMD operator expansion** — Vladimirov–Moos–Scimemi, JHEP 01 (2022) 110 *(abstract)*: operator-level
  derivation of TMD factorization, operators ordered by TMD twist (separating kinematic and genuine power
  corrections), process dependence through boundary conditions of background fields; effective operator for the
  hadronic tensor to NLP ($\sim q_T/Q$) at NLO for any process with two detected states. **[A]** (NLO, NLP).
* **Twist-3 TMDs** — Rodini–Vladimirov, JHEP 08 (2022) 031 (erratum JHEP 12 (2022) 048) *(abstract)*: definition,
  evolution equations (autonomous at large $N_c$), small-$b$ asymptotics, singularity structure of TMD-twist-3
  distributions; "physical" twist-3 TMDs for applications. **[A]** (one-loop kernels).
* **SIDIS at NLP, complete** — Rodini–Vladimirov, PRD 110 (2024) 034009 *(abstract)*: all SIDIS structure functions
  at NLP, coefficient functions and kernels at one loop, twist-3 TMD FFs with LO kernel; **"several differences with
  earlier derivations"** traced to the kinematics of quark–gluon interference terms. **[P]** (one loop; literature
  not yet consistent).
* **Kinematic power corrections** — Vladimirov, JHEP 12 (2023) 008 *(abstract)*: each genuine term generates a
  series of KPCs with the same non-perturbative content; the series attached to the LP term is summed, restoring
  EM-current conservation and frame invariance (violated at fixed power), giving a factorized form resembling the
  free-massless-quark hadronic tensor; NLO check. SIDIS version: Piloneta–Vladimirov, JHEP 03 (2026) 049; quasi-TMD
  version (link to LaMET): Bris Cuerpo–Arroyo-Castro–Vladimirov, PRD 114 (2026) 034028. **[A]** (as stated).
* **SCET at NLP for SIDIS azimuthal asymmetries** — Ebert–Gao–Stewart, JHEP 06 (2022) 007 (erratum JHEP 07 (2023)
  096) *(abstract)*: *"Working under the assumption that leading power Glauber interactions do not spoil
  factorization at this order"*: complete NLP factorization for power-suppressed hard-scattering effects; TMDs
  depending on **two** longitudinal momentum fractions (one only beyond tree level); **proof that only the LP soft
  function appears** and is absorbed into the TMDs; one new hard coefficient. **[A](cond.: Glauber)**.
* **Gamberg–Kang–Shao–Terry–Zhao**, arXiv:2211.13209† *(abstract)*: kinematic/intrinsic/dynamic NLP pieces for DY
  and SIDIS; RG consistency at one loop; anomalous-dimension matrices mixing LP and NLP distributions; hard and soft
  functions differ from LP; rapidity anomalous dimension of the dynamic NLP distributions equals the LP one.
  **[P]†**.
* **DY at NLP in an EFT without explicit soft/collinear modes** — Inglis-Whalen–Luke–Roy–Spourdalakis, PRD 104
  (2021) 076018 *(abstract)*: power-suppressed operators $T_{(i,j)}$ giving the $O(q_T^2/q^2)$ coefficients of the
  usual PDFs; factorization at NLP for $q^2\gg q_T^2\gg\Lambda^2$, rapidity-divergence cancellation and overlap
  subtractions at NLP. **[P]**.
* **Power-law rapidity divergences** — Ebert–Moult–Stewart–Tackmann–Vita–Zhu, JHEP 04 (2019) 123 *(abstract)*: at
  subleading power rapidity divergences can be power-law, producing derivatives of PDFs; a pure rapidity regulator
  and an $\overline{\rm MS}$-like scheme preserving homogeneity of the power expansion; complete $O(\alpha_s)$
  $q_T^2/Q^2$ corrections for colour-singlet production. **[R]** at $O(\alpha_s)$.
* **Small-$x$ / Wilson-line approach** — Balitsky–Tarasov JHEP 07 (2017) 095, JHEP 05 (2018) 150; Balitsky NPB 1006
  (2024) 116658 ($1/Q^2$ corrections to the unpolarized DY tensor at large $N_c$, EM gauge invariance) *(abstracts)*.
  **[P]**.

| statement | grade |
|---|---|
| LP TMD factorization (DY, SIDIS, $e^+e^-$) | [A] (Ch. 11) |
| operator-level NLP TMD factorization, NLO | [A] (VMS 2022), [A](cond.: Glauber) (EGS 2022) |
| one-loop NLP coefficient functions / twist-3 TMD evolution | [P] (differences between groups) |
| summation of kinematic power corrections of the LP term | [A] |
| Glauber cancellation at NLP in TMD processes | [C] (assumed everywhere) |
| NLP TMD factorization beyond one loop / non-perturbatively | open |

---------------------------------------------------------------------------------------------------------

## 7. Positivity of $\overline{\rm MS}$ parton densities

Context (Ch. 6): the bare light-front number-density interpretation suggests $f\ge0$; renormalization
($\overline{\rm MS}$ subtraction of the UV divergence of the operator) destroys any automatic positivity. The
2020–2024 debate settled the following.

**Claims.**
* Candido–Forte–Hekhorn, JHEP 11 (2020) 129 *(abstract)*: NLO $\overline{\rm MS}$ PDFs are positive "in the
  perturbative regime": construct a positive factorization scheme (collinear subtraction keeping partonic cross
  sections positive), then show positivity survives the scheme change to $\overline{\rm MS}$ when the NLO scheme
  change is smaller than LO.
* Collins–Rogers–Sato, PRD 105 (2022) 076010 [read]: the CFH argument fails at the step "bare PDFs are positive".
  In the approach they call **track B** (collinear divergences of massless partonic quantities regulated with
  $n>4$ and convoluted with bare hadronic PDFs) the UV-divergent contributions are positive for $n<4$ but "can and
  often do become negative after analytic continuation to $n>4$". In **track A** (renormalized operator PDFs of the
  hadron; partonic calculations only for hard coefficients) this problem does not arise, and nothing in the
  definition or in the factorization theorems excludes negative $\overline{\rm MS}$ PDFs at low/moderate scales.
* Candido–Forte–Giani–Hekhorn, EPJC 84 (2024) 335 [read, Secs. 3–4]: agree that PDFs "always turn positive at high
  enough scale" and "turn negative at a low enough scale", that scale being non-perturbative; maintain that within
  the perturbative domain $\overline{\rm MS}$ PDFs inherit positivity of physical-scheme PDFs; conservative
  semi-quantitative estimate $Q^2\gtrsim5\ {\rm GeV}^2$ (from $\frac{\alpha_s}{2\pi}C_{gg}(x)<1$ at $x\sim0.3$,
  $\alpha_s\lesssim0.2$); the non-trivial ingredient is the **sign** of the $O(\alpha_s)$ diagonal term
  ($\overline{\rm MS}$ over-subtracts collinear singularities, which in the diagonal channel have the Sudakov sign).

> **Proposition 7.1 (negativity is possible; explicit model)** **[R] (model)** [S2]. In the Yukawa theory
> $\mathcal L_{\rm int}=-\lambda\bar\Psi_N\psi_q\phi+{\rm h.c.}$ with all particles massive and weak coupling, the
> one-loop quark-in-"nucleon" $\overline{\rm MS}$ pdf is (CRS Eqs. (55)–(56))
> $$f^{\rm renorm}_{q/p}(\xi;\mu)=a_\lambda(\mu)(1-\xi)\Big[\ln\frac{\mu^2}{\Delta(\xi)}-1+\frac{(m_q+\xi m_p)^2}{\Delta(\xi)}\Big]+O(a_\lambda^2),\quad
> \Delta(\xi)=\xi m_s^2+(1-\xi)m_q^2-\xi(1-\xi)m_p^2,$$
> $a_\lambda=\lambda^2/(16\pi^2)$, $\Delta>0$ for a stable target ($m_p<m_q+m_s$). For any $\xi$ it is negative for
> small enough $\mu$ and positive for large $\mu$. Hence "$\overline{\rm MS}$ PDFs are positive" is **[V]** as a
> general theorem.

*Verified [S2]:* (i) the DR integral (CRS Eq. (58)) with $\overline{\rm MS}$ subtraction gives exactly the bracket
above and the counterterm $-a_\lambda(1-\xi)S_\epsilon/\epsilon$ (CRS Eq. (57)); (ii) the $k_T$-cut-off version (CRS
Eq. (59)), manifestly positive, agrees with (55) up to $O(m^2/\mu^2)$ ($6.7\times10^{-4}$ max deviation at
$\mu=30$ GeV); (iii) for $m_q=0.3$, $m_p=1.0$, $m_s=1.5$ GeV: negative for $\xi\in[0.28,0.98]$ at $\mu=0.8$ GeV,
smaller region at $1.2$ GeV, positive for all $\xi$ at $2.5$ GeV; (iv) $\xi\to0$: bracket $\to\ln(\mu^2/m_q^2)$
(negative iff $\mu<m_q$); $\xi\to1$: sign change at $\mu_*=m_s\exp\{\frac12[1-(m_q+m_p)^2/m_s^2]\}=1.70$ GeV.
Mechanism (CRS Sec. VIII B): the $\overline{\rm MS}$ pdf equals the cut-off pdf minus
$a_\lambda(1-\xi)\int dk_T^2/k_T^2$ over $[\mu^2,k^2_{\rm cut}]$; at low $\mu$ the $1/k_T^2$ asymptote over-subtracts the
true small-$k_T$ behaviour.

> **Proposition 7.2 (positivity at sufficiently large scale)** **[P]**. Assume LP collinear factorization for a set
> of positive observables defining a "physical" scheme (e.g. DIS structure functions), negligible higher twist, and
> perturbativity of the scheme transformation at NLO. Then $\overline{\rm MS}$ PDFs are positive above a scale which
> (thanks to the Sudakov sign of the diagonal $O(\alpha_s)$ term) is $x$-independent at large $x$; CFGH estimate it
> conservatively as $Q^2\gtrsim5$ GeV². CRS agree qualitatively ("once the $\overline{\rm MS}$ scale is large enough
> compared with intrinsic transverse momentum scales, the pdfs indeed become positive"). Grade [P]: NLO argument,
> higher orders and power corrections not controlled; the threshold scale is non-perturbative.

*Consequences for the monograph (Ch. 6).* (1) Do not state positivity of $\overline{\rm MS}$ PDFs (or Soffer-type
bounds) as theorems; (2) positivity constraints in fits at low input scales are a theoretical bias (CRS); (3) a
fixed-order factorized cross section can be negative without contradiction (CRS App. A); (4) known physical
example: $\overline{\rm MS}$ heavy-quark PDFs are negative just below the matching threshold (CRS Sec. I).

| statement | grade |
|---|---|
| $\overline{\rm MS}$ PDFs positive for all $\mu$ | [V] (Yukawa counterexample) |
| positivity for $\mu$ above a (non-perturbative) scale | [P] (NLO + assumptions) |
| bare-PDF positivity in track B with $n>4$ continuation | [V] (CRS) |
| existence of positive schemes (e.g. $k_T$ cut-off, physical schemes) | [R] at one loop in the model; [A] in general |

---------------------------------------------------------------------------------------------------------

## 8. BRST classification of operators: the non-local gap (Collins 2011, §11.3.2)

### 8.1 What Collins' factorization proof needs, and what he assumes (read: Collins 2011, pp. 407–412)

In Feynman gauge the leading regions of DIS involve arbitrarily many longitudinally polarized ("K") gluons
attached to the hard part. A diagrammatic non-abelian Ward-identity proof (Labastida–Sterman 1985; Collins §11.9)
works only in the strictly collinear limit; Collins–Rogers (PRD 78 (2008) 054012) showed by explicit calculation
that the remainder is **non-zero** at leading power (pure K-gluon terms contribute to the gluon density through
the gluons' transverse momenta; a non-abelian effect needed to build the gauge-invariant gluon pdf). Collins
therefore uses BRST invariance (§11.3.2):

1. Off-shell Green function $T^{\mu\nu}_{\rm off\text{-}shell}(q)=\frac1{4\pi}\int d^4z\,e^{iq\cdot z}\langle0|T\,{\rm fields}\,j^\mu(z/2)j^\nu(-z/2)|0\rangle$
   (Eq. (11.11)); leading regions ⇒ $\sum_iC_i\otimes\langle0|T\,{\rm fields}\,O_i|0\rangle+{\rm p.s.c.}$ (11.12), where the
   $O_i$ may a priori be "arbitrarily complicated multilocal operators" on the light ray.
2. BRST invariance of Green functions, $\delta_{\rm BRST}\langle0|T\,(\text{any fields})|0\rangle=0$ (11.13), and of the
   currents ⇒ $\delta_{\rm BRST}\sum_iC_i\otimes O_i=0$ (11.17): only BRST-invariant operators appear.
3. For **local** operators: BRST-invariant = gauge-invariant ⊕ (A) BRST variations $\delta_{\rm BRST}A_{\rm source}$
   ⊕ (B) operators vanishing by the equations of motion (Joglekar–Lee 1976; Joglekar 1977; Nakanishi–Ojima
   1990); classes A and B vanish in physical matrix elements (and in Green functions with gauge-invariant operators
   at separated points). An example of a non-local class-A operator (11.18):
   $\delta_{\rm BRST}[\bar\eta_\alpha(0,x^-,0_T)A_{\beta\mu}(0)]/\delta\lambda=\partial\!\cdot\!A_\alpha(0,x^-,0_T)A_{\beta\mu}(0)+\bar\eta_\alpha(0,x^-,0_T)D_\mu{}_{\beta}\,\eta(0)$.
4. **The gap, verbatim (p. 410):** *"Unfortunately, the published proofs that BRST-invariant operators are either
   gauge invariant or are in one of classes A or B apply as written to local operators. It is natural that the
   result also applies to the non-local operators we use in factorization. But, as far as I know, no proof has
   been given. For the purposes of the discussion, I will assume the result is true, and leave the proof (or
   refutation) to future research."*
5. Renormalization of PDFs (§11.4): triangular mixing
   $$\begin{pmatrix}O\\A\\B\end{pmatrix}=\begin{pmatrix}Z_{OO}&Z_{OA}&Z_{OB}\\0&Z_{AA}&Z_{AB}\\0&0&Z_{BB}\end{pmatrix}\begin{pmatrix}O_{(0)}\\A_{(0)}\\B_{(0)}\end{pmatrix}\quad(11.20),$$
   so in physical matrix elements $O=Z_{OO}O_{(0)}$; one loop can be done on shell, but beyond one loop off-shell
   calculations need A, B (Hamberg–van Neerven 1992; Collins–Scalise 1994).
6. Even granting gauge invariance, the *path* of the Wilson line is fixed by the remaining requirements (fields
   localized on a light-like line, all but two fields $A^+$), and the light-like straight path follows; for TMDs the
   path is genuinely process dependent (staples).

### 8.2 Local operators: the classification is a theorem   **[R]** (local)

* Joglekar–Lee, Ann. Phys. 97 (1976) 160 (general theory); Kluberg-Stern–Zuber, PRD 12 (1975) 467, 482, 3159
  (Ward identities; background-field gauge; the "Kluberg-Stern–Zuber conjecture"); Dixon–Taylor, Nucl. Phys. B78
  (1974) 552 (first explicit gauge-variant counterterms for Wilson operators).
* Henneaux, PLB 313 (1993) 35 (erratum PLB 316 (1993) 633) and Barnich–Brandt–Henneaux, Phys. Rept. 338 (2000)
  439: the statement as a theorem on local BRST cohomology (ghost number 0, modulo $d$), for semisimple gauge groups
  with matter *(abstracts)*.
* All-loop structure of the gauge-variant ("alien") operators needed for off-shell twist-2 renormalization:
  Falcioni–Herzog, JHEP 05 (2022) 177 — generalized BRST from the Dixon–Taylor generalized gauge symmetry (adding EOM
  operators to the Lagrangian), ghost operator generated from a single generalized-BRST-exact operator,
  generalized anti-BRST relations among anomalous dimensions, consistency with Joglekar–Lee; explicit basis to four
  loops; Mellin moments $N=2,4$ of $P_{gg}$ to four loops and $N=6$ to three loops. Gehrmann–von Manteuffel–Yang,
  JHEP 04 (2023) 041 — systematic counterterm Feynman rules for the gauge-variant operators; three-loop singlet
  anomalous dimensions rederived; gauge-parameter independence observed *(abstracts)*.

### 8.3 Non-local operators: status after Collins 2011

**(a) General multilocal light-ray operators (what step 2→3 needs):** no published proof found in this session
(INSPIRE/web searches 2026-10-10; *not verified* that none exists). **[C]**.

**(b) The standard bilocal twist-2 light-ray operators (what renormalization of PDFs needs):** a reduction to the
local theorem is available, which we state with explicit hypotheses:

> **Proposition 8.1 (moment reduction, this report).** Let $O_q(w^-)=\bar\psi(w)\gamma^+W[w,0]\psi(0)$ and the
> analogous gluon operator, $w=(0^+,w^-,0_T)$. Assume (H1) the Joglekar–Lee/Henneaux classification for the local
> operators $\bar\psi\gamma^+(iD^+)^{N-1}\psi$, $F^{+\mu}(iD^+)^{N-2}F^{+}{}_\mu$ (all indices "+", hence automatically
> symmetric and traceless: these are exactly the twist-2 operators); (H2) at each order of perturbation theory the
> forward matrix elements in physical states define distributions in $\xi$ supported in $[-1,1]$ (support property);
> (H3) the bare non-local matrix element equals the generating function of the bare local ones (Taylor expansion in
> $w^-$, exact for compact support, since the Fourier transform of a compactly supported distribution is entire with
> Taylor coefficients = moments). Then in physical matrix elements $O^R=Z_{OO}\otimes O_{(0)}$ with
> $\int_0^1dz\,z^{N-1}Z_{OO}(z)=Z^{(N)}_{\rm twist\text{-}2}$ for all $N$, and class-A/B admixtures drop out; the kernel
> $Z_{OO}(z)$ is uniquely fixed by its moments (compact support; for the C-even/C-odd combinations $q\pm\bar q$ and for
> the gluon only even or odd $N$ occur, and uniqueness then follows from the Müntz–Szász theorem, cf. Ch. 5). Hence
> (11.20) restricted to physical matrix elements holds.

*Grade:* **[A]** — (H1) is [R] for local operators; (H2) is the standard support property ([A]; proven order by
order in the literature on PDF definitions, Ch. 6); (H3) and uniqueness are elementary distribution theory ([R]).
The c_pdf agent verified the one-loop instance (moments of the bilocal operator = local twist-2 matrix elements,
graph by graph, `research/c_pdf/DERIVATION.md` §5.4).

**(c) What (b) does not cover:** the classification step *inside* the factorization proof, where multilocal
operators with several fields at different light-cone positions appear before gauge invariance is imposed; TMD
operators (staple paths, rapidity divergences — a different problem, Ch. 11); off-shell renormalization of the
light-ray operators themselves (not needed for physical predictions).

**(d) Alternative routes.** Light-cone gauge $A^+=0$ removes the K gluons (Collins: "given the known problems with
$A^+=0$ gauge, it would be nice to have a proof that does not rely on the gauge"); for *space-like* straight Wilson-
line operators (quasi-PDFs, LaMET) multiplicative renormalizability to all orders is proven by treating the Wilson
line as an auxiliary (heavy-quark-like) field (Ji–Zhang–Zhao PRL 120 (2018) 112001; Ishikawa–Ma–Qiu–Yoshida PRD
96 (2017) 094019; Green–Jansen–Steffens PRL 121 (2018) 022004) — see `frontier/lamet`; that method turns the
non-local operator into local operators of an extended theory, the natural tool to close gap (a).

| statement | grade |
|---|---|
| local: BRST-invariant (gh. 0) = gauge-inv. ⊕ BRST-exact ⊕ EOM | [R] |
| all-loop basis of gauge-variant counterterms for twist-2 (off-shell) | [A] (explicit to 4 loops) |
| renormalization of standard bilocal PDF operators in physical matrix elements (triangular (11.20)) | [A] (Prop. 8.1) |
| classification of general multilocal BRST-invariant light-ray operators (needed in the factorization proof) | [C] (Collins: assumed) |
| non-zero K-gluon remainder in Feynman-gauge DIS (non-abelian) | [R] (explicit; Collins–Rogers 2008) |

---------------------------------------------------------------------------------------------------------

## 9. Small $x$: Wilson-line (high-energy) factorization and its status

*Framing.* Small-$x$ "factorization" is a **different expansion** from the collinear one: the Regge limit
$s\gg|t|$ (DIS: $x\to0$ at fixed $Q^2$), organized by **rapidity factorization** of Wilson lines (shockwave
picture): projectile wave functions/impact factors ⊗ target Wilson-line correlators evolved in rapidity
(BK/JIMWLK). Its results are all-order statements *within the eikonal (Regge) expansion at fixed logarithmic
accuracy*, not leading-power theorems in $\Lambda/Q$ with power counting control; the grades below are relative to
that framework.

### 9.1 LO Balitsky–Kovchegov equation (statement used in the monograph)   **[A]** [S5]

With $S_Y(x,y)=\frac1{N_c}\langle{\rm tr}[U_xU_y^\dagger]\rangle_Y$ ($U_x$ the light-like Wilson line of a fast parton at
transverse position $x$ in the target field; direction conventions differ between papers and do not affect the
equation), $Y=\ln(1/x_{\rm Bj})$, $\bar\alpha_s=\alpha_sN_c/\pi$:
$$\frac{\partial S_Y(x,y)}{\partial Y}=\frac{\bar\alpha_s}{2\pi}\int d^2z\,\frac{(x-y)^2}{(x-z)^2(z-y)^2}\Big[S_Y(x,z)S_Y(z,y)-S_Y(x,y)\Big]$$
(large $N_c$ / mean-field truncation of the Balitsky–JIMWLK hierarchy). Linearizing ($N=1-S$) gives the dipole
form of LO BFKL; **[S5]** checks numerically that the kernel acting on $(x-y)^{2\gamma}$ has eigenvalue
$\bar\alpha_s\chi(\gamma)$, $\chi(\gamma)=2\psi(1)-\psi(\gamma)-\psi(1-\gamma)$ (to $10^{-9}$ for
$\gamma=0.15,0.3,0.5,0.7$; $\chi(\tfrac12)=4\ln2$).

### 9.2 Next-to-leading order and beyond   **[A]**

* **NLO BK** — Balitsky–Chirilli, PRD 77 (2008) 014019 *(abstract)*: gluon contribution to NLO small-$x$
  evolution of Wilson lines (quark part and running coupling: Balitsky, PRD 75 (2007) 014001; Kovchegov–Weigert,
  Nucl. Phys. A784 (2007) 188),
  with quadratic and cubic non-linearities. [Checked in the paper, Sec. VIII:] the NLO kernel = running-coupling
  part ($\propto\beta_0$) + conformal part ($1\to3$ dipole transitions) + a non-conformal double-log term; its forward
  linearization agrees with NLO BFKL up to a term $\propto\alpha_s^2\zeta(3)\times$(the original dipole), attributed to
  different longitudinal cutoffs.
* **NLO JIMWLK** — Balitsky–Chirilli, PRD 88 (2013) 111501; Kovner–Lublinsky–Mulian, PRD 89 (2014) 061704, JHEP 04
  (2014) 030 (conformal symmetry), JHEP 08 (2014) 114 ("unabridged") *(abstracts)*.
* **Three loops (planar $\mathcal N=4$)** — Caron-Huot–Herranen, JHEP 02 (2018) 058 *(abstract)*: three-loop BK
  kernel via the equivalence with non-global logarithms (§11), a Lorentz-covariant IR/collinear subtraction
  method; checks against the Pomeron trajectory and twist-2 spectrum.
* **Instability and collinear resummation** — the NLO BK solution is unstable for realistic initial conditions
  (Lappi–Mäntysaari, PRD 91 (2015) 074016); kinematic constraints/collinear resummation cure it (Beuf, PRD 89
  (2014) 074039; Iancu–Madrigal–Mueller–Soyez–Triantafyllopoulos, PLB 744 (2015) 293) *(abstracts)*. **[P]**
  (resummation prescriptions differ beyond the controlled logarithms).

### 9.3 Regge factorization of amplitudes and its breakdown   **[A]/[V]**

* **Caron-Huot, "When does the gluon reggeize?"**, JHEP 05 (2015) 093 *(abstract; Sec. 4 checked)*: the eikonal approximation with
  rapidity-dependent collections of Wilson lines (Balitsky–JIMWLK) as a reliable tool; reggeization and BFKL
  rederived; **from four loops BFKL dynamics is incompatible with a then-conjectured structure of IR divergences**
  (the "dipole formula"); in the strict planar limit, theory formulated with a finite, process-dependent number of
  Wilson lines without reference to a reggeized gluon (exact $\mathcal N=4$ check). **[A]**
* **Breaking of simple Regge-pole factorization at NNLL** — Del Duca–Falcioni–Magnea–Vernazza, PLB 732 (2014) 233;
  JHEP 02 (2015) 029 *(abstracts)*: using IR factorization, the simplest Regge factorization of $2\to2$ amplitudes
  fails at NNLL in $\ln(s/|t|)$ (two-loop non-logarithmic double pole; non-factorizing single-log singular terms at
  three loops); hard functions vanish in $d=4$ to all orders up to NLL. **[V]** (Regge-pole factorization beyond
  NLL), **[A]** (corrected multi-Reggeon picture).
* Caron-Huot–Gardi–Reichel–Vernazza, JHEP 03 (2018) 098 *(abstract)*: closed form for the IR-singular part of
  $2\to2$ amplitudes to all orders at NLL in the high-energy limit (two-Reggeon contribution), predicting the Regge
  limit of the soft anomalous dimension to any loop order. **[A]**

### 9.4 Small-$x$ TMDs and the interplay with Sudakov logarithms *(abstracts)*

* Dominguez–Marquet–Xiao–Yuan, PRD 83 (2011) 105005: effective $k_t$-factorization for dijets in dilute–dense
  collisions; Weizsäcker–Williams vs dipole gluon distributions as universal small-$x$ TMDs (process-dependent gauge
  links at small $x$). **[A]** (LO in the CGC framework).
* Mueller–Xiao–Yuan, PRL 110 (2013) 082301: Sudakov double logs in the saturation formalism (collinear-$k_t$ and
  small-$x$ resummations combined). **[A]** (LL).
* Balitsky–Tarasov, JHEP 10 (2015) 017: rapidity evolution of gluon TMDs interpolating between low and moderate
  $x$; Balitsky, JHEP 05 (2021) 046, JHEP 09 (2021) 022, JHEP 03 (2023) 029, PLB 882 (2026) 141002: gauge-invariant
  TMD factorization at small $x$, rapidity-only factorization, Sudakov–BFKL interpolation. **[P]**

### 9.5 Small-$x$ helicity *(abstracts)*

* Kovchegov–Pitonyak–Sievert, JHEP 01 (2016) 072 (erratum JHEP 10 (2016) 148); PRL 118 (2017) 052001: helicity
  evolution at small $x$ (double logarithms $\alpha_s\ln^2(1/x)$) from polarized dipole amplitudes (sub-eikonal Wilson-
  line operators).
* Cougoulic–Kovchegov–Tarasov–Tawabutr, JHEP 07 (2022) 095 (erratum 2024): **revised** evolution equations.
* Borden–Kovchegov, PRD 108 (2023) 014001: exact large-$N_c$ solution; $\Delta\Sigma\sim\Delta G\sim g_1\sim(1/x)^{\alpha_h}$
  with $\alpha_h\simeq3.66074\sqrt{\alpha_sN_c/2\pi}$; the resummed $\Delta\gamma_{GG}(\omega)$ agrees with all fixed-order
  results (to three loops) but **differs from the infrared-evolution-equation result of Bartels–Ermolaev–Ryskin
  starting at four loops**; BER intercept $3.66394\sqrt{\alpha_sN_c/2\pi}$. Large-$N_c\&N_f$: Adamiak–Kovchegov–Tawabutr PRD
  108 (2023) 054005; Borden–Kovchegov–Li JHEP 09 (2024) 037 (quark↔gluon transition operators); Borden–Kovchegov PRD
  113 (2026) 034002 (analytic solution; slight disagreement with BER and Blümlein–Vogt persists).
  **[A]** (DLA, large $N_c$ or large $N_c\&N_f$); the discrepancy with BER is an **open problem**.
* Hatta et al.: gluon orbital angular momentum at small $x$ (Hatta–Nakagawa–Yuan–Zhao–Xiao, PRD 95 (2017) 114032);
  small-$x$ evolution of the gluon GPD $E_g$ (Hatta–Zhou, PRL 129 (2022) 252002). **[A]/[P]**

| statement | grade |
|---|---|
| LO BK/JIMWLK from QCD in the eikonal (LL Regge) approximation | [A] [S5] |
| NLO BK/JIMWLK | [A] (stability requires collinear resummation: [P]) |
| simple Regge-pole factorization of $2\to2$ amplitudes beyond NLL | [V] |
| IR-singular part of Regge-limit amplitudes to all orders at NLL | [A] |
| small-$x$ TMD universality (WW vs dipole), Sudakov at small $x$ | [A] (LO/LL) |
| small-$x$ helicity intercept (large $N_c$); agreement with BER | [A]; disagreement from 4 loops = open |

---------------------------------------------------------------------------------------------------------

## 10. Double parton scattering (DPS): towards a factorization theorem

*Setting.* Two hard scatterings in one $pp$ collision, e.g. double Drell–Yan (two colour-singlet bosons). The DPS
cross section is formally power suppressed for integrated cross sections but leading for transverse-momentum-
differential ones ($q_{T,i}\ll Q_i$) and enhanced for many final states at small $x$. Since 2011 the elements of a
QCD factorization proof have been assembled, mostly by Diehl and collaborators.

* **Framework** — Diehl–Ostermeier–Schäfer, JHEP 03 (2012) 089 (erratum JHEP 03 (2016) 001) *(abstract)*:
  space-time, spin and **colour** structure of DPS (colour-correlated DPDs), power counting, elements needed for
  all-order factorization, Sudakov logs, links to GPDs and lattice. Manohar–Waalewijn, PRD 85 (2012) 114009 and PLB
  713 (2012) 196 ("What is double parton scattering?"): colour correlations, interference, evolution; the
  $1\to2$ splitting singularity ($\propto1/y^2$ at small separation $y$) and the double-counting problem with single
  scattering *(abstracts)*.
* **Glauber cancellation for double Drell–Yan, all orders** — Diehl–Gaunt–Ostermeier–Plößl–Schäfer, JHEP 01 (2016)
  076 *(abstract)*: cancellation of Glauber exchange at all orders for double DY, **both for the integrated cross
  section and for the cross section differential in the boson transverse momenta**; clarifies the relation of the
  Glauber cancellation to the rest of the single-DY proof. **[A]** (same level as CSS for single DY).
* **Soft-gluon decoupling** — Diehl–Nagar, JHEP 04 (2019) 124 *(abstract)*: soft gluons exchanged between the two
  protons in multiparton scattering decouple into vacuum expectation values of Wilson lines; non-abelian Ward
  identities; generalizes the CSS single-DY proof. **[A]**
* **Rapidity divergences of multi-parton soft factors** — Vladimirov, JHEP 04 (2018) 045 *(abstract)*: rapidity
  divergences arise from exchanges with the distant transverse plane and are structurally equivalent to UV
  divergences (conformal map) ⇒ a **renormalization theorem for rapidity divergences** (proof via the conformal
  transformation), definition of multi-parton TMDs, exact relation between soft and rapidity anomalous dimensions
  (three-loop rapidity anomalous dimension derived). **[A]**
* **Double counting (1v1, 2v1)** — Diehl–Gaunt–Schönwald, JHEP 06 (2017) 083 [read, Sec. 4.1]:
  $$\sigma=\sigma_{\rm SPS}+\sigma_{\rm DPS}-\sigma_{\rm sub},\qquad
  \frac{d\sigma_{\rm DPS}}{dx_1dx_2d\bar x_1d\bar x_2}=\sum\hat\sigma_{a_1b_1}\hat\sigma_{a_2b_2}\int d^2y\,\Phi^2(y\nu)\,F_{b_1b_2}(\bar x_i,y)\,F_{a_1a_2}(x_i,y),$$
  with a cut-off function $\Phi(u)\to1$ for $u\gg1$, $\Phi(u)=O(u^\delta)$ at small $u$ (e.g. $\Theta(u-b_0)$ or
  $1-e^{-u^2/4}$), $\nu\sim Q$; $\sigma_{\rm sub}$ (for 1v1: $\sigma_{1v1,\rm pt}$, their Eq. (4.5)) is the DPS formula with
  both DPDs replaced by their fixed-order perturbative splitting forms. At small $y$ the $\Phi$ dependence cancels
  between $\sigma_{\rm DPS}$ and $\sigma_{\rm sub}$ (leaving SPS); at large $y$, $\sigma_{\rm SPS}\simeq\sigma_{\rm sub}$
  (leaving DPS). DPDs are thereby defined as operator matrix elements usable at higher orders. **[A]** (scheme
  consistency argued at fixed order; cancellation only up to higher orders when DPDs are evolved).
* **Evolution and matching** *(abstracts)*: TMD DPS factorization, evolution and matching — Buffing–Diehl–Kasemets,
  JHEP 01 (2018) 044 (+2021 erratum/addendum); NLO kernels for colour-non-singlet DPDs — Diehl–Fabry–Vladimirov,
  JHEP 05 (2023) 067; two-loop $1\to2$ splitting — Diehl–Gaunt–Plößl–Schäfer, SciPost Phys. 7 (2019) 017; quark-
  mass effects in the splitting — Diehl–Nagar–Plößl, JHEP 09 (2023) 100; momentum/number sum rules in position space
  — Diehl–Gaunt–Lang–Plößl–Schäfer, EPJC 80 (2020) 468; review — Diehl–Gaunt, Adv. Ser. Direct. HEP 29 (2018) 7.
* **Glauber gluons and MPI (single scattering observables)** — Gaunt 2014 (§4.2): MPI-sensitive observables.

| statement | grade |
|---|---|
| Glauber cancellation for double DY (integrated and $q_T$-differential), all orders | [A] |
| soft-factor decoupling into Wilson-line VEVs (multiparton) | [A] |
| renormalization theorem for rapidity divergences of multi-parton soft factors | [A] |
| consistent DPS/SPS combination without double counting (DGS scheme) | [A] |
| full DPS factorization for coloured final states / jets | [C] |
| colour-correlated DPD evolution kernels | [P] (computed to NLO) |

---------------------------------------------------------------------------------------------------------

## 11. Jets, jet substructure and non-global observables

### 11.1 Factorization for jet processes with non-global logarithms (NGLs)   **[A]** ($e^+e^-$)

> **Result 11.1 (Becher–Neubert–Rothen–Shao, PRL 116 (2016) 192001; JHEP 11 (2016) 019 (erratum JHEP 05 (2017)
> 154); read, Sec. 2).** For Sterman–Weinberg-type cone-jet cross sections in $e^+e^-$ (energy outside the cones
> $<\beta Q$, cone half-angle $\delta$), wide-angle case ($\delta\sim1$, modes: hard $Q(1,1,1)$ and soft
> $Q\beta(1,1,1)$):
> $$\sigma(\beta,\delta)=\sum_{m\ge2}\big\langle\mathcal H_m(\{n\},Q,\delta)\otimes\mathcal S_m(\{n\},Q\beta,\delta)\big\rangle,\qquad
> \mathcal S_m=\sum_{X_s}\langle0|S_1^\dagger(n_1)\cdots S_m^\dagger(n_m)|X_s\rangle\langle X_s|S_1(n_1)\cdots S_m(n_m)|0\rangle\,\theta(Q\beta-2E_{\rm out}),$$
> $S_i(n_i)={\bf P}\exp\big(ig_s\int_0^\infty ds\,n_i\cdot A_s^a(sn_i)\,{\bf T}_i^a\big)$ (their Eqs. (2.4), (2.12)–(2.15));
> $\mathcal H_m$ = squared $m$-parton amplitudes integrated over energies at fixed directions (distribution-valued in
> the angles), $\otimes$ = integration over directions, $\langle\cdot\rangle$ = colour trace. Narrow cones
> ($\delta\ll1$): additional coft modes and multi-Wilson-line coft functions. The functions obey RGEs that are
> matrices in multiplicity space, $\frac{d}{d\ln\mu}\mathcal H_m=-\sum_{l=2}^m\mathcal H_l\,\Gamma^H_{lm}$ and
> $\frac{d}{d\ln\mu}\mathcal S_l=\sum_{m\ge l}\hat\Gamma^H_{lm}\otimes\mathcal S_m$ (their Eqs. (2.38)–(2.39)); at LL and
> large $N_c$ they reproduce the Banfi–Marchesini–Smye equation; two-loop logarithmic terms checked against
> numerical fixed-order results.

*Grade* **[A]** (EFT derivation + MoR + explicit two-loop checks; $e^+e^-$, no Glauber issue). Hadron-collider
version: Becher–Neubert–Shao–Stillger 2023 (§4.4), with Glauber phases ⇒ SLLs; PDF factorization there is [P]
(§4.5). Related: Becher–Pecjak–Shao, JHEP 12 (2016) 018 (light-jet mass, hemisphere soft function) *(abstract)*.

### 11.2 Resummation of NGLs beyond LL *(abstracts)*

* **Colour density matrix** — Caron-Huot, JHEP 03 (2018) 036: a colour density matrix resums NGLs to all
  logarithmic orders; anomalous dimension at LO and NLO; via a conformal transformation equivalent to shockwave
  (Regge) evolution — NLO BFKL/Balitsky–JIMWLK rederived; exponentiation of divergences to all logarithmic orders
  demonstrated. **[A]**
* **NLL NGLs** — Banfi–Dreyer–Monni, JHEP 10 (2021) 006 (integro-differential equations, planar large $N_c$,
  formulated in DR and in a manifestly finite 4D form; checked against full QCD at $O(\alpha_s^2)$) and JHEP 03 (2022)
  135 (jet calculus); Becher–Rauh–Xu, JHEP 08 (2022) 134 (two-loop anomalous dimension); Becher–Schalch–Xu, PRL 132
  (2024) 081602 (NLL resummation at the LHC in a large-$N_c$ parton shower); further 2026 preprints† (two-loop
  anomalous dimension for non-global and clustering logs; NLL NGLs in Higgs production). **[A]** (large $N_c$, NLL).
* **Measurement-driven factorization of NGLs** — Larkoski–Moult–Neill, JHEP 09 (2015) 143: NGLs factorize and are
  resummed down to an unresolved scale by making sufficiently many measurements ("dressed gluons"). **[A]**

### 11.3 Jet substructure and jet functions *(abstracts)*

* **Soft-drop groomed observables** — Frye–Larkoski–Schwartz–Yan, JHEP 07 (2016) 064: factorization for a large
  class of soft-drop observables (incl. jet mass); without the groomed soft wide-angle radiation all singular
  contributions are collinear ⇒ normalized distributions have **no NGLs to all orders** and are process independent
  up to the quark/gluon fraction; NNLL resummation. **[A]** (in the soft-drop power counting $z_{\rm cut}\ll1$).
* **Hadronization in groomed jets** — Hoang–Mantry–Pathak–Stewart, JHEP 12 (2019) 002: field-theoretic description
  (SCET + coherent branching); in an intermediate jet-mass region the leading power corrections are three universal
  NP parameters with perturbative coefficients; at smaller mass a non-normalized shape function. **[A]**
* **Semi-inclusive jet functions** — Kang–Ringer–Vitev, JHEP 10 (2016) 125: jet functions $J_i(z,\omega_J,\mu)$ obey
  exactly timelike-DGLAP evolution (ln $R$ resummation); single-inclusive jet production shares the hard functions
  of single-inclusive hadron production with $D_i^h\to J_i$. **[A]** (NLO + RG consistency).
* **Energy correlators** — Dixon–Moult–Zhu, PRD 100 (2019) 014009: leading-power factorization of the EEC in the
  collinear limit of a generic QFT, anomalous dimensions = moments of timelike splitting functions; NNLL in QCD.
  **[A]**. Kologlu–Kravchuk–Simmons-Duffin–Zhiboedov, JHEP 01 (2021) 128: a **non-perturbative, convergent** OPE for
  null-integrated (light-ray) operators on the same null plane in a CFT ("light-ray OPE"; celestial blocks for event
  shapes). **[A] (CFT, non-perturbative)** (derived within non-perturbative CFT using the Lorentzian inversion
  formula; not a QCD statement) — the non-perturbative analogue of the collinear factorization of event shapes.

| statement | grade |
|---|---|
| NGL factorization (multi-Wilson-line soft functions) for $e^+e^-$ jet processes | [A] |
| NLL resummation of NGLs (large $N_c$) | [A] |
| soft-drop groomed observables free of NGLs; factorization | [A] |
| collinear EEC factorization (generic QFT, perturbative) | [A] |
| light-ray OPE convergence in CFT | [A] (CFT, non-perturbative) |
| same structures at hadron colliders | see §4 ([P]/[V]) |

---------------------------------------------------------------------------------------------------------

## 12. Heavy-quarkonium production: status of NRQCD factorization (updates since 2005)

*Background (Ch. 15).* NRQCD factorization (Bodwin–Braaten–Lepage 1995) for inclusive production,
$d\sigma(H)=\sum_nd\hat\sigma_n(\Lambda)\,\langle\mathcal O^H_n(\Lambda)\rangle$, is a **conjecture** for production
(decays: [A]). The questions are (i) whether IR divergences of the short-distance coefficients match those of the
LDMEs at all orders, and (ii) the universality of the LDMEs.

* **Gauge completion at NNLO** — Nayak–Qiu–Sterman, PLB 613 (2005) 45; PRD 72 (2005) 114012; PRD 74 (2006) 074007
  *(abstracts)*: in gluon fragmentation at large $p_T$, NNLO IR poles are **not** matched by the conventional octet
  production operators; gauge invariance and factorization require operators with **Wilson lines (non-abelian
  phases)**; with these "gauge-completed" matrix elements factorization is restored at NNLO, first to $O(v^2)$ and then
  **to all orders in $v$** for the octet→singlet transition. Caveat (NQS 2005): beyond NNLO, "in the absence of special
  cancellations", additional non-local operators outside the NRQCD velocity expansion may be needed. **[P]** (NNLO).
* **Independent two-loop test** — Bodwin–Chung–Ee–Kim–Lee, PRD 101 (2020) 096011 *(abstract)*: covariant two-loop
  calculation of the LDME for an S-wave colour-octet pair fragmenting into a colour-singlet pair of arbitrary orbital
  angular momentum; universality requires the IR divergences to be independent of the Wilson-line direction — **found
  to hold**; results differ from NQS in some respects (sources identified); both consistent with NRQCD factorization;
  "the general principle that underlies this confirmation ... has yet to be revealed". **[P]** (two loops).
* **Collinear (fragmentation) factorization at large $p_T$, LP + NLP in $1/p_T$** — Kang–Qiu–Sterman, PRL 108 (2012)
  102002; Kang–Ma–Qiu–Sterman, PRD 90 (2014) 034006 and PRD 91 (2015) 014030 *(abstracts)*: LP (single-parton
  fragmentation) and NLP (heavy-quark-pair fragmentation, double-parton FFs) contributions factorize into IR-safe
  partonic coefficients and universal FFs; evolution equations, projection operators, operator definitions, first
  non-trivial kernels. Fleming–Leibovich–Mehen–Rothstein, PRD 86 (2012) 094012: all-order SCET factorization of
  short-distance production as double-parton fragmentation, one-loop anomalous-dimension matrix; logs of $Q/p_\perp$
  are power suppressed. Ma–Qiu–Zhang, PRD 89 (2014) 094029/094030 (FFs from a heavy-quark pair); Bodwin–Chung–Kim–
  Lee, PRL 113 (2014) 022001 (fragmentation contributions at Tevatron/LHC). **[A]** for the $p_T$-expansion
  structure (it rests on standard single-inclusive collinear factorization at high $p_T$, for which the NQS 2005 PRD
  argument is singled out by Collins 2011, p. 571, as the "notable exception" to the lack of detailed proofs);
  NRQCD factorization of the FFs themselves inherits [C]/[P] from above.
* **Phenomenological tension** *(abstracts)*: LHCb $\eta_c$ data vs heavy-quark spin symmetry relating $\eta_c$ and
  $J/\psi$ LDMEs — "challenges NRQCD factorization" (Butenschoen–He–Kniehl, PRL 114 (2015) 092004) vs. consistent
  with other fits (Han–Ma–Meng–Shao–Chao, PRL 114 (2015) 092005; Zhang–Sun–Sang–Li, PRL 114 (2015) 092006). The
  polarization puzzle persists in global fits (not reviewed here).
* **Alternative: soft-gluon factorization (SGF)** — Ma–Chao, PRD 100 (2019) 094007 *(abstract)*: a factorization in
  which soft hadronization effects are treated without expanding in the relative velocity first; claimed better
  velocity convergence. **[C]** as a theorem (proposal with partial checks).

| statement | grade |
|---|---|
| NRQCD factorization for quarkonium decays | [A] (Ch. 15) |
| NRQCD factorization for inclusive production, all orders | [C] |
| NNLO IR consistency with gauge-completed (Wilson-line) octet operators; all orders in $v$ at NNLO | [P] |
| Wilson-line-direction independence of IR poles at two loops | [P] |
| LP+NLP collinear factorization in $1/p_T$ for quarkonium (single and double-parton FFs) | [A] |

---------------------------------------------------------------------------------------------------------

## 13. QED corrections, photon and lepton PDFs, electroweak factorization

### 13.1 The photon PDF from structure functions (LUXqed)   **[A]** [S3]

> **Result 13.1 (Manohar–Nason–Salam–Zanderighi, PRL 117 (2016) 242002, Eq. (6) [read]; JHEP 12 (2017) 046
> [abstract]).** In the $\overline{\rm MS}$ scheme,
> $$x f_{\gamma/p}(x,\mu^2)=\frac{1}{2\pi\alpha(\mu^2)}\int_x^1\frac{dz}{z}\Bigg\{\int_{\frac{x^2m_p^2}{1-z}}^{\frac{\mu^2}{1-z}}\frac{dQ^2}{Q^2}\,
> \alpha^2(Q^2)\Big[\Big(zp_{\gamma q}(z)+\frac{2x^2m_p^2}{Q^2}\Big)F_2\big(\tfrac xz,Q^2\big)-z^2F_L\big(\tfrac xz,Q^2\big)\Big]
> -\alpha^2(\mu^2)\,z^2F_2\big(\tfrac xz,\mu^2\big)\Bigg\},\qquad zp_{\gamma q}(z)=1+(1-z)^2,$$
> including all terms of order $\alpha L(\alpha_sL)^n$, $\alpha(\alpha_sL)^n$ and $\alpha^2L^2(\alpha_sL)^n$
> ($L=\ln\mu^2/m_p^2$); $F_{2,L}$ include the **elastic** parts
> $F_2^{\rm el}=\frac{G_E^2+\tau G_M^2}{1+\tau}\delta(1-x)$, $F_L^{\rm el}=\frac{G_E^2}{\tau}\delta(1-x)$, $\tau=Q^2/4m_p^2$.

*Proof architecture.* A fictitious BSM process $l+p\to L+X$ through a transition magnetic moment
$(e/\Lambda)\bar L\sigma^{\mu\nu}F_{\mu\nu}l$: its cross section is computed (i) exactly in terms of $F_2,F_L$ (the
lepton current is not renormalized), (ii) via collinear factorization with $\overline{\rm MS}$ PDFs; equating the two
up to the stated accuracy fixes $f_\gamma$. The JHEP paper also obtains it from the operator definition of the
photon PDF, gives an *exact* representation in terms of $F_2,F_L$ to all orders in QED and QCD including
non-perturbative corrections, the formula one order higher, polarized and TMD photon PDFs, and derives
$P_{\gamma i}$ at $O(\alpha\alpha_s)$ and $O(\alpha^2)$ in agreement with direct calculations.
*Grade:* **[A]** (relies on collinear factorization of the auxiliary process; the operator-definition derivation
makes it process independent).

*Verified [S3]:* for a point-like Dirac fermion target (elastic, $G_E=G_M=1$, so $F_2=\delta(1-x')$,
$F_L=\frac{4m^2}{Q^2}\delta(1-x')$) the formula gives
$xf_\gamma=\frac{\alpha}{2\pi}[1+(1-x)^2][\ln\frac{\mu^2}{m^2}-2\ln x-1]+\frac{\alpha m^2x^2(1-x)}{\pi\mu^2}$, i.e. exactly
Frixione's $O(\alpha)$ $\overline{\rm MS}$ photon-in-lepton PDF (JHEP 11 (2019) 158, Eq. (4.189), read) up to a
power correction; dropping $F_L$ would shift the constant by $\frac{\alpha}{2\pi}4(1-x)$, dropping the
$\overline{\rm MS}$-conversion term by $\frac{\alpha}{2\pi}x^2$.

### 13.2 Leptons, electrons, mixed QCD×QED evolution *(abstracts)*

* Lepton PDFs of the proton from the same structure-function input, at NLO: Buonocore–Nason–Tramontano–Zanderighi,
  JHEP 08 (2020) 019. **[A]**
* Electron (positron, photon) PDFs of the electron at NLL in QED, all-order large-$z$ resummation matched to
  $O(\alpha^3)$: Frixione JHEP 11 (2019) 158 (initial conditions); Bertone–Cacciari–Frixione–Stagnitto, JHEP 03
  (2020) 135 (erratum JHEP 08 (2022) 108). **[A]**
* QED and mixed corrections to the Altarelli–Parisi kernels: $O(\alpha\alpha_s)$ (de Florian–Sborlini–Rodrigo, EPJC 76
  (2016) 282) and $O(\alpha^2)$ by "Abelianization" (JHEP 10 (2016) 056): explicit kernels at the stated orders
  (finite-order results).

### 13.3 Electroweak corrections: Bloch–Nordsieck violation and EW PDFs *(abstracts)*

* Since collider initial states carry definite **non-abelian** (weak isospin) flavour, EW Sudakov double logs do
  **not** cancel in inclusive TeV-scale cross sections (Ciafaloni–Ciafaloni–Comelli, PRL 84 (2000) 4810): explicit
  perturbative analysis; i.e. Bloch–Nordsieck cancellation is **[V]** for non-singlet initial states.
* EW PDFs and resummation at $Q\gg M_W$: Bauer–Ferland–Webber JHEP 08 (2017) 036; Bauer–Webber JHEP 03 (2019) 013
  (polarization effects); Fornal–Manohar–Waalewijn JHEP 05 (2018) 106 ($W,Z$ PDFs from structure functions);
  Manohar–Waalewijn JHEP 08 (2018) 137: NLL framework, factorization analysis showing that the objects in the
  factorization theorem need not be $SU(2)\times U(1)$ singlets; DGLAP-type evolution captures all EW logs only for
  sufficiently inclusive measurements (invariant mass), while identifying a final-state lepton requires FFs and soft
  exchanges. **[A]**
* **Factorization violation at very high energies:** Baumgart–Erdoğan–Rothstein–Vaidya, PRD 100 (2019) 096008: for
  observables measuring the weak charge of final states in hadronic collisions, non-factorizable EW corrections
  break the parton-model picture at leading power, starting at $O(\alpha_s^2\alpha_W^2\log^4(Q^2/M_W^2))$; not
  resummable by DGLAP alone. **[V]** (as computed in that paper).

| statement | grade |
|---|---|
| photon PDF in terms of $F_2$, $F_L$ (LUXqed), stated accuracy | [A] [S3] |
| exact all-order representation of $f_\gamma$ via $F_2,F_L$ | [A] |
| lepton/electron PDFs (NLO / NLL) | [A] |
| mixed QCD×QED kernels at $O(\alpha\alpha_s)$, $O(\alpha^2)$ | explicit (finite order) |
| Bloch–Nordsieck cancellation of EW logs for non-singlet initial states | [V] |
| naive parton-model factorization for weak-charge-measuring observables at $Q\gg M_W$ | [V] (from $\alpha_s^2\alpha_W^2L^4$) |

---------------------------------------------------------------------------------------------------------

## 14. Master table, new statements, open problems, and hand-off to the monograph

### 14.1 Master table (frontier results, 2010–2026)

| # | result | grade | § |
|---|---|---|---|
| 1 | Physical-region pinch ⇔ Landau point (Collins; denominators ≤ quadratic + sign condition) | [R]† | 1.2 |
| 2 | Geometric half = Gordan's alternative; 6-line constructive proof | [R] (new remark) [S1] | 1.3 |
| 3 | Coleman–Norton picture for massless graphs from (1) | [R]† (new remark) [S1] | 1.5 |
| 4 | "Avoiding a singularity needs a positive first-order shift"; Landau ⇒ singularity of $I(z)$ | [V]; [V] | 1.2, 1.4 |
| 5 | IR forest formula and factorized form for massless wide-angle amplitudes | [A] | 1.6 |
| 6 | Amplitude-level H–S–C factorization (final-state collinear only) | [A] | 1.6 |
| 6a | Dipole formula for IR singularities beyond two loops | [V] (3 loops) | 1.6(f) |
| 7 | Asymptotic OPE (scalar, curved spacetime); OPE closure on gauge-invariant operators (pure YM) | [R]; [R] / [R]† | 2.2–2.6 |
| 8 | Convergent OPE at fixed loop order ($\varphi^4_4$, massive/massless) | [R] (model) | 2.5 |
| 9 | Convergent OPE for YM/QCD; self-contained flow-equation proof for QCD with quarks | [C]; not available | 2.7 |
| 10 | MoR: Euclidean limits | [R] | 3.2 |
| 11 | MoR: Jantzen identity under (1)–(4); LP-facet prescription (LO; one facet) | [R](cond.); [R] | 3.3–3.4 |
| 12 | MoR: regions = lower facets in Minkowski kinematics | [V] (3-loop non-planar) | 3.5 |
| 13 | Glauber EFT (complete LP Lagrangian; BFKL as rapidity RGE) | [A] | 4.1 |
| 14 | Pure Glauber ladders cancel for single-scale observables | [A] | 4.2 |
| 15 | Generalized factorization for DY+beam thrust spin asymmetry | [V] (model) | 4.2 |
| 16 | Strict space-like collinear factorization; collinear factorization of non-inclusive $pp$ cross sections | [V] (1 loop); [V] (3 loops) | 4.3 |
| 17 | SLL tower + LL resummation | [A] [S4] | 4.4 |
| 18 | PDF factorization in gap-between-jets despite SLLs | [P] (3 loops) | 4.5 |
| 19 | Standard factorization/exponentiation of 1-jettiness in $V+$jet | [V] (LL-CVL computation) | 4.6 |
| 20 | Endpoint-factorized renormalized theorem $h\to\gamma\gamma$; $gg\to h$ | [A]; [A] | 5.2 |
| 21 | LL NLP resummation (DY, $gg\to H$, DIS off-diagonal, gluon thrust); NLP threshold PDF two-scale | [A]; [A]† | 5.3 |
| 22 | NLP TMD factorization (operator level, NLO) | [A] / [A](cond.: Glauber); evolution [P] | 6 |
| 23 | $\overline{\rm MS}$ PDF positivity: always / above a scale | [V]; [P] [S2] | 7 |
| 24 | BRST classification: local; bilocal PDF operators (physical m.e.); general multilocal | [R]; [A] (new Prop. 8.1); [C] | 8 |
| 25 | LO/NLO BK–JIMWLK (eikonal framework) | [A] [S5] | 9 |
| 26 | Regge-pole factorization beyond NLL | [V] | 9.3 |
| 27 | Small-$x$ helicity: intercept (large $N_c$) vs BER | [A]; discrepancy open | 9.5 |
| 28 | Double DY: Glauber cancellation; soft decoupling; rapidity renormalization theorem; no double counting | [A] | 10 |
| 29 | NGL factorization in $e^+e^-$; NLL NGL resummation; soft-drop factorization | [A] | 11 |
| 30 | Light-ray OPE convergence in CFT | [A] (CFT, non-pert.) | 11.3 |
| 31 | NRQCD production factorization: all orders / NNLO with gauge completion / 2-loop direction independence | [C] / [P] / [P] | 12 |
| 32 | LP+NLP $1/p_T$ collinear factorization for quarkonium | [A] | 12 |
| 33 | LUXqed photon PDF; exact representation | [A] [S3] | 13.1 |
| 34 | EW Bloch–Nordsieck violation; naive parton model for weak-charge observables at $Q\gg M_W$ | [V]; [V] | 13.3 |

### 14.2 New rigorous statements contributed by this report (for the monograph, to be cited as "this work")

1. **Prop. 1.2** — Collins' geometric Thm. 3 is Gordan's theorem (1873); short constructive proof with explicit
   margin $D_j(w)\ge|w|^2$ for the min-norm direction $w$ (usable as a contour-deformation recipe). [R], [S1].
2. **Cor. 1.3** — momentum-space derivation of the Coleman–Norton picture *including massless lines and Wilson
   lines*, as an algebraic corollary of Collins' Thm. 1 (no Feynman parameters); inherits [R]†.
3. **Prop. 8.1** — moment reduction of the BRST-classification problem for the standard bilocal PDF operators to the
   local Joglekar–Lee/Henneaux theorem (hypotheses H1–H3 stated); closes the renormalization part of Collins'
   §11.3.2 gap for physical matrix elements; the multilocal classification step of the factorization proof remains
   [C]. [A].
4. Checked transcriptions: BNS SLL tower ⇒ ${}_2F_2(1,1;2,\frac52;-w)$ with first SLL coefficient
   $\frac{4}{15\pi^2}C_FN_c\alpha_s^4L^5\Delta Y\,\hat\sigma_B$ and $f\sim\frac32\ln w/w$; LN LDL series ⇒
   ${}_2F_2(1,1;\frac32,2;\cdot)$ consistent with the NLO amplitude; LUXqed ⇒ Frixione point-like limit, with the
   separate roles of $F_L$ and of the $\overline{\rm MS}$ conversion term; CRS Yukawa $\overline{\rm MS}$ PDF formula and its
   sign structure; LO BK kernel eigenvalue. [S2–S5].

### 14.3 Open problems (frontier list for the final chapter)

1. **Landau/pinch theory:** remove Collins' sign condition (8.15) and the quadratic restriction; a refereed version;
   characterize *which* vanishing denominators trap the contour and the cone of allowed deformations at a pinch
   (needed to justify every approximation of Ch. 7); systematic coordinate-space version (Erdoğan–Sterman).
2. **Method of regions in Minkowski kinematics:** a proof (SSS main conjecture; Jantzen's convergence step) and an
   algorithm guaranteed to find hidden regions (Glauber, multi-hard) — cf. three-loop counterexamples.
3. **Glauber/factorization in hadron–hadron collisions:** an [R]-level proof for inclusive DY; the fate of
   MPI-sensitive observables beyond pure Glauber ladders (soft emission off Glauber rungs, SYZ); PDF factorization
   for non-global observables beyond three loops; independent confirmation and resummation of the
   $\alpha_s^nL^{2n-2}$ coherence-violating logarithms in $N$-jettiness (consequences for $N$-jettiness slicing).
4. **NLP:** endpoint factorization beyond LL for processes with incoming hadrons; a general theorem for
   refactorization conditions; Glauber cancellation at NLP (assumed in all NLP TMD work); reconciliation of NLP TMD
   evolution results between groups.
5. **BRST:** classification of multilocal BRST-invariant light-ray operators (Collins 2011, p. 410) — natural tool:
   auxiliary-field (Wilson line as a field) localization as in the LaMET renormalizability proofs.
6. **OPE:** convergence for Yang–Mills/QCD; a self-contained rigorous renormalization proof for QCD with quarks
   (flow equations).
7. **Positivity:** a non-perturbative/first-principles determination of the scale above which $\overline{\rm MS}$ PDFs
   are positive.
8. **Small $x$:** origin of the Kovchegov et al. vs BER discrepancy in the polarized small-$x$ anomalous dimension
   (from four loops); scheme-independent collinear improvement of NLO BK; consistent matching of small-$x$ and
   collinear factorization.
9. **DPS:** factorization with coloured final states; phenomenology of colour-correlated DPDs.
10. **Quarkonium:** NRQCD production factorization beyond NNLO; the "general principle" behind the two-loop
    confirmation.
11. **Electroweak:** resummation of the non-factorizing EW logarithms at $Q\gg M_W$.

### 14.4 Hand-off: where each item enters the monograph

* Ch. 3 (Landau, CN, regions): §1 (Thm. 1.1, Prop. 1.2 with proof, Cor. 1.3) and §3 (MoR status, hidden regions).
* Ch. 4–5 (OPE): §2 (asymptotic vs convergent; pure-YM vs QCD with quarks).
* Ch. 6 (PDFs): §7 (positivity), §8 (BRST, Prop. 8.1), §13 (photon/lepton PDFs).
* Ch. 7 / 10 / 12 (Glauber, breaking): §4 (RS EFT, SYZ cancellation, CdFR/FSS, SLLs, factorization restoration,
  1-jettiness SSLLs), §10 (double DY Glauber cancellation).
* Ch. 11 (TMD): §6 (NLP).
* Ch. 13–14 (exclusive/SCET): §5 (endpoint factorization), §3.5 (mode completeness), §11 (NGLs, jets).
* Ch. 15 (quarkonium): §12.
* Ch. 16 (power corrections, non-perturbative): §5, §6, §2.
* Ch. 12/16 (small $x$): §9.
* Ch. 17 (summary): §14.1 table and §14.3 open problems.

---------------------------------------------------------------------------------------------------------

## Appendix A. Verified bibliography (INSPIRE-HEP, fetched 2026-10-10; full BibTeX in `others.bib`)

All 236 INSPIRE entries below were downloaded verbatim from INSPIRE (keys = INSPIRE texkeys); "preprint" = no journal
publication recorded on 2026-10-10. Additional manual entry: `Gordan:1873` (Math. Ann. 6 (1873) 23–28,
DOI 10.1007/BF01442864, Crossref). Section labels refer to this report. Which papers were read in full is listed in
§0.3; all others were checked at the level of INSPIRE metadata + abstract.


**§0–1 Landau, IR structure**

| key | authors | journal / status | arXiv | DOI |
|---|---|---|---|---|
| `Collins:2011zzd` | Collins | Cambridge University Press (2011) |  | 10.1017/9781009401845 |
| `Collins:2020euz` | Collins | preprint (2020) | 2007.04085 |  |
| `Coleman:1965xm` | Coleman–Norton | Nuovo Cim. 38 (1965) 438--442 |  | 10.1007/BF02750472 |
| `Libby:1978bx` | Libby–Sterman | Phys. Rev. D 18 (1978) 4737 |  | 10.1103/PhysRevD.18.4737 |
| `Eden:1966dnq` | Eden et al. | Cambridge Univ. Press (1966) |  |  |
| `Ma:2019hjq` | Ma | JHEP 05 (2020) 012 | 1910.11304 | 10.1007/JHEP05(2020)012 |
| `Feige:2014wja` | Feige–Schwartz | Phys. Rev. D 90 (2014) 105020 | 1403.6472 | 10.1103/PhysRevD.90.105020 |
| `Erdogan:2013bga` | Erdoğan | Phys. Rev. D 89 (2014) 085016; [Erratum: Phys.Rev.D 90, 089902 (2014)] | 1312.0058 | 10.1103/PhysRevD.89.085016 |
| `Erdogan:2014gha` | Erdoğan–Sterman | Phys. Rev. D 91 (2015) 065033 | 1411.4588 | 10.1103/PhysRevD.91.065033 |
| `Erdogan:2017gyf` | Erdoğan–Sterman | Phys. Rev. D 95 (2017) 116015 | 1705.04539 | 10.1103/PhysRevD.95.116015 |
| `Sterman:2025qsq` | Sterman–Erdoğan | Eur. Phys. J. ST 235 (2026) 1493--1512 | 2502.14230 | 10.1140/epjs/s11734-025-01804-8 |
| `Anastasiou:2018rib` | Anastasiou–Sterman | JHEP 07 (2019) 056 | 1812.03753 | 10.1007/JHEP07(2019)056 |
| `Anastasiou:2020sdt` | Anastasiou et al. | JHEP 04 (2021) 222 | 2008.12293 | 10.1007/JHEP04(2021)222 |
| `Anastasiou:2022eym` | Anastasiou–Sterman | JHEP 05 (2023) 242 | 2212.12162 | 10.1007/JHEP05(2023)242 |
| `Anastasiou:2024xvk` | Anastasiou et al. | JHEP 11 (2024) 043 | 2403.13712 | 10.1007/JHEP11(2024)043 |
| `Anastasiou:2025cvy` | Anastasiou et al. | preprint (2025) | 2509.07805 |  |
| `Anastasiou:2026kpm` | Anastasiou et al. | preprint (2026) | 2601.22936 |  |
| `Anastasiou:2026jta` | Anastasiou et al. | preprint (2026) | 2603.12862 |  |
| `Mizera:2021icv` | Mizera–Telen | JHEP 08 (2022) 200 | 2109.08036 | 10.1007/JHEP08(2022)200 |
| `Fevola:2023kaw` | Fevola–Mizera–Telen | Phys. Rev. Lett. 132 (2024) 101601 | 2311.14669 | 10.1103/PhysRevLett.132.101601 |
| `Fevola:2023fzn` | Fevola–Mizera–Telen | Comput. Phys. Commun. 303 (2024) 109278 | 2311.16219 | 10.1016/j.cpc.2024.109278 |
| `Berghoff:2022mqu` | Berghoff–Panzer | J. Geom. Phys. 216 (2025) 105539 | 2212.06661 | 10.1016/j.geomphys.2025.105539 |
| `Helmer:2024wax` | Helmer–Papathanasiou–Tellander | Phys. Rev. D 114 (2026) L011901 | 2402.14787 | 10.1103/8tk7-3gkn |
| `Hannesdottir:2022bmo` | Hannesdottir–Mizera | Springer (2023) | 2204.02988 | 10.1007/978-3-031-18258-7 |
| `Gong:2008ww` | Gong–Nagy–Soper | Phys. Rev. D 79 (2009) 033005 | 0812.3686 | 10.1103/PhysRevD.79.033005 |
| `Becker:2012nk` | Becker–Weinzierl | Phys. Rev. D 86 (2012) 074009 | 1208.4088 | 10.1103/PhysRevD.86.074009 |
| `Becher:2009cu` | Becher–Neubert | Phys. Rev. Lett. 102 (2009) 162001; [Erratum: Phys.Rev.Lett. 111, 199905 (2013)] | 0901.0722 | 10.1103/PhysRevLett.102.162001 |
| `Gardi:2009qi` | Gardi–Magnea | JHEP 03 (2009) 079 | 0901.1091 | 10.1088/1126-6708/2009/03/079 |
| `Almelid:2015jia` | Almelid–Duhr–Gardi | Phys. Rev. Lett. 117 (2016) 172002 | 1507.00047 | 10.1103/PhysRevLett.117.172002 |

**§2 OPE**

| key | authors | journal / status | arXiv | DOI |
|---|---|---|---|---|
| `Zimmermann:1972tv` | Zimmermann | Annals Phys. 77 (1973) 570--601 |  | 10.1016/0003-4916(73)90430-2 |
| `Collins:1984xc` | Collins | Cambridge University Press (1984) |  | 10.1017/9781009401807 |
| `Hollands:2006ag` | Hollands | Commun. Math. Phys. 273 (2007) 1--36 | gr-qc/0605072 | 10.1007/s00220-007-0230-6 |
| `Hollands:2007zg` | Hollands | Rev. Math. Phys. 20 (2008) 1033--1172 | 0705.3340 | 10.1142/S0129055X08003420 |
| `Hollands:2011gf` | Hollands–Kopper | Commun. Math. Phys. 313 (2012) 257--290 | 1105.3375 | 10.1007/s00220-012-1457-4 |
| `Holland:2014pna` | Holland–Hollands–Kopper | Commun. Math. Phys. 342 (2016) 385--440 | 1411.1785 | 10.1007/s00220-015-2486-6 |
| `Holland:2015tia` | Holland–Hollands | J. Math. Phys. 56 (2015) 122303 | 1507.07730 | 10.1063/1.4937811 |
| `Holland:2014ifa` | Holland–Hollands | Commun. Math. Phys. 336 (2015) 1555--1606 | 1401.3144 | 10.1007/s00220-014-2274-8 |
| `Frob:2016mzv` | Fröb–Holland | preprint (2016) | 1603.08012 |  |
| `Frob:2015uqy` | Fröb–Holland–Hollands | J. Math. Phys. 57 (2016) 122301 | 1511.09425 | 10.1063/1.4967747 |
| `Efremov:2017sqi` | Efremov–Guida–Kopper | J. Math. Phys. 58 (2017) 093503 | 1704.06799 | 10.1063/1.5000041 |
| `Kopper:2009zw` | Kopper–Muller | Rev. Math. Phys. 21 (2009) 781--820 | 0902.2486 | 10.1142/S0129055X0900375X |
| `Kopper:1999qx` | Kopper–Muller | Commun. Math. Phys. 209 (2000) 477--516 | hep-th/9902114 | 10.1007/s002200050028 |
| `Keller:1991cj` | Keller–Kopper | Phys. Lett. B 273 (1991) 323--332 |  | 10.1016/0370-2693(91)91692-O |
| `Keller:1995qn` | Keller–Kopper | Commun. Math. Phys. 176 (1996) 193--226 |  | 10.1007/BF02099368 |
| `Keller:1990ej` | Keller–Kopper–Salmhofer | Helv. Phys. Acta 65 (1992) 32--52 |  |  |
| `Guida:2011np` | Guida–Kopper | preprint (2011) | 1103.5692 |  |
| `Piguet:1995er` | Piguet–Sorella | preprint (1995) |  | 10.1007/978-3-540-49192-7 |

**§3 method of regions**

| key | authors | journal / status | arXiv | DOI |
|---|---|---|---|---|
| `Beneke:1997zp` | Beneke–Smirnov | Nucl. Phys. B 522 (1998) 321--344 | hep-ph/9711391 | 10.1016/S0550-3213(98)00138-2 |
| `Smirnov:1990rz` | Smirnov | Commun. Math. Phys. 134 (1990) 109--137 |  | 10.1007/BF02102092 |
| `Smirnov:2002pj` | Smirnov | Springer Tracts Mod. Phys. 177 (2002) 1--262 |  |  |
| `Pak:2010pt` | Pak–Smirnov | Eur. Phys. J. C 71 (2011) 1626 | 1011.4863 | 10.1140/epjc/s10052-011-1626-1 |
| `Jantzen:2011nz` | Jantzen | JHEP 12 (2011) 076 | 1111.2589 | 10.1007/JHEP12(2011)076 |
| `Semenova:2018cwy` | Semenova–Smirnov–Smirnov | Eur. Phys. J. C 79 (2019) 136 | 1809.04325 | 10.1140/epjc/s10052-019-6653-3 |
| `Gardi:2022khw` | Gardi et al. | JHEP 07 (2023) 197 | 2211.14845 | 10.1007/JHEP07(2023)197 |
| `Ma:2023hrt` | Ma | JHEP 09 (2024) 197 | 2312.14012 | 10.1007/JHEP09(2024)197 |
| `Gardi:2024axt` | Gardi et al. | JHEP 08 (2024) 127 | 2407.13738 | 10.1007/JHEP08(2024)127 |
| `Ananthanarayan:2018tog` | Ananthanarayan et al. | Eur. Phys. J. C 79 (2019) 57 | 1810.06270 | 10.1140/epjc/s10052-019-6533-x |
| `Heinrich:2021dbf` | Heinrich et al. | Comput. Phys. Commun. 273 (2022) 108267 | 2108.10807 | 10.1016/j.cpc.2021.108267 |

**§4 Glauber, factorization violation, SLLs**

| key | authors | journal / status | arXiv | DOI |
|---|---|---|---|---|
| `Bodwin:1984hc` | Bodwin | Phys. Rev. D 31 (1985) 2616; [Erratum: Phys.Rev.D 34, 3932 (1986)] |  | 10.1103/PhysRevD.34.3932 |
| `Collins:1985ue` | Collins–Soper–Sterman | Nucl. Phys. B 261 (1985) 104--142 |  | 10.1016/0550-3213(85)90565-6 |
| `Collins:1988ig` | Collins–Soper–Sterman | Nucl. Phys. B 308 (1988) 833--856 |  | 10.1016/0550-3213(88)90130-7 |
| `Bauer:2010cc` | Bauer–Lange–Ovanesyan | JHEP 07 (2011) 077 | 1010.1027 | 10.1007/JHEP07(2011)077 |
| `Rothstein:2016bsq` | Rothstein–Stewart | JHEP 08 (2016) 025 | 1601.04695 | 10.1007/JHEP08(2016)025 |
| `Gaunt:2014ska` | Gaunt | JHEP 07 (2014) 110 | 1405.2080 | 10.1007/JHEP07(2014)110 |
| `Zeng:2015iba` | Zeng | JHEP 10 (2015) 189 | 1507.01652 | 10.1007/JHEP10(2015)189 |
| `Schwartz:2018obd` | Schwartz–Yan–Zhu | Phys. Rev. D 97 (2018) 096017 | 1801.01138 | 10.1103/PhysRevD.97.096017 |
| `Schwartz:2017nmr` | Schwartz–Yan–Zhu | Phys. Rev. D 96 (2017) 056005 | 1703.08572 | 10.1103/PhysRevD.96.056005 |
| `Mitov:2012gt` | Mitov–Sterman | Phys. Rev. D 86 (2012) 114038 | 1209.5798 | 10.1103/PhysRevD.86.114038 |
| `Catani:2014qha` | Catani–Grazzini–Torre | Nucl. Phys. B 890 (2014) 518--538 | 1408.4564 | 10.1016/j.nuclphysb.2014.11.019 |
| `Catani:2011st` | Catani–de Florian–Rodrigo | JHEP 07 (2012) 026 | 1112.4405 | 10.1007/JHEP07(2012)026 |
| `Forshaw:2012bi` | Forshaw–Seymour–Siodmok | JHEP 11 (2012) 066 | 1206.6363 | 10.1007/JHEP11(2012)066 |
| `Dixon:2019lnw` | Dixon et al. | JHEP 05 (2020) 135; [Erratum: JHEP 06, 143 (2024)] | 1912.09370 | 10.1007/JHEP05(2020)135 |
| `Guan:2024hlf` | Guan et al. | JHEP 01 (2025) 090 | 2408.03019 | 10.1007/JHEP01(2025)090 |
| `Forshaw:2006fk` | Forshaw–Kyrieleis–Seymour | JHEP 08 (2006) 059 | hep-ph/0604094 | 10.1088/1126-6708/2006/08/059 |
| `Forshaw:2008cq` | Forshaw–Kyrieleis–Seymour | JHEP 09 (2008) 128 | 0808.1269 | 10.1088/1126-6708/2008/09/128 |
| `Angeles-Martinez:2015rna` | \'Angeles-Mart\'\inez–Forshaw–Seymour | JHEP 12 (2015) 091 | 1510.07998 | 10.1007/JHEP12(2015)091 |
| `Forshaw:2021fxs` | Forshaw–Holguin | JHEP 12 (2021) 084; [Erratum: JHEP 04, 097 (2024)] | 2109.03665 | 10.1007/JHEP12(2021)084 |
| `Becher:2021zkk` | Becher–Neubert–Shao | Phys. Rev. Lett. 127 (2021) 212002 | 2107.01212 | 10.1103/PhysRevLett.127.212002 |
| `Becher:2023mtx` | Becher et al. | JHEP 12 (2023) 116 | 2307.06359 | 10.1007/JHEP12(2023)116 |
| `Boer:2023jsy` | Böer–Neubert–Stillger | JHEP 10 (2023) 075 | 2307.11089 | 10.1007/JHEP10(2023)075 |
| `Boer:2023ljq` | Böer et al. | JHEP 02 (2024) 109 | 2311.18811 | 10.1007/JHEP02(2024)109 |
| `Boer:2024hzh` | Böer et al. | JHEP 08 (2024) 035 | 2405.05305 | 10.1007/JHEP08(2024)035 |
| `Boer:2024xzy` | Böer et al. | JHEP 08 (2024) 036 | 2407.01691 | 10.1007/JHEP08(2024)036 |
| `Becher:2024nqc` | Becher et al. | JHEP 01 (2025) 171 | 2411.12742 | 10.1007/JHEP01(2025)171 |
| `Banerjee:2025kkq` | Banerjee et al. | JHEP 02 (2026) 092 | 2510.24848 | 10.1007/JHEP02(2026)092 |
| `Becher:2024kmk` | Becher et al. | Phys. Rev. Lett. 134 (2025) 061901 | 2408.10308 | 10.1103/PhysRevLett.134.061901 |
| `Becher:2025igg` | Becher et al. | JHEP 01 (2026) 024 | 2509.07082 | 10.1007/JHEP01(2026)024 |
| `Banfi:2025mra` | Banfi–Forshaw–Holguin | Phys. Rev. Lett. 136 (2026) 221901 | 2511.11799 | 10.1103/flv7-ksvf |
| `Alioli:2023rxx` | Alioli et al. | Phys. Rev. D 109 (2024) 094009 | 2312.06496 | 10.1103/PhysRevD.109.094009 |
| `Stewart:2010tn` | Stewart–Tackmann–Waalewijn | Phys. Rev. Lett. 105 (2010) 092002 | 1004.2489 | 10.1103/PhysRevLett.105.092002 |

**§5 NLP / endpoint factorization**

| key | authors | journal / status | arXiv | DOI |
|---|---|---|---|---|
| `Liu:2019oav` | Liu–Neubert | JHEP 04 (2020) 033 | 1912.08818 | 10.1007/JHEP04(2020)033 |
| `Liu:2020wbn` | Liu et al. | JHEP 01 (2021) 077 | 2009.06779 | 10.1007/JHEP01(2021)077 |
| `Liu:2022ajh` | Liu et al. | JHEP 06 (2023) 183 | 2212.10447 | 10.1007/JHEP06(2023)183 |
| `Liu:2017vkm` | Liu–Penin | Phys. Rev. Lett. 119 (2017) 262001 | 1709.01092 | 10.1103/PhysRevLett.119.262001 |
| `Liu:2018czl` | Liu–Penin | JHEP 11 (2018) 158 | 1809.04950 | 10.1007/JHEP11(2018)158 |
| `Kotsky:1997rq` | Kotsky–Yakovlev | Phys. Lett. B 418 (1998) 335--344 | hep-ph/9708485 | 10.1016/S0370-2693(97)01260-4 |
| `Akhoury:2001mz` | Akhoury–Wang–Yakovlev | Phys. Rev. D 64 (2001) 113008 | hep-ph/0102105 | 10.1103/PhysRevD.64.113008 |
| `Penin:2014msa` | Penin | Phys. Lett. B 745 (2015) 69--72; [Erratum: Phys.Lett.B 751, 596--596 (2015), Erratum: Phys.Lett.B 771, 633--634 (2017)] | 1412.0671 | 10.1016/j.physletb.2015.04.036 |
| `Bodwin:2021cpx` | Bodwin et al. | Phys. Rev. D 104 (2021) 016010 | 2101.04872 | 10.1103/PhysRevD.104.016010 |
| `Bodwin:2021epw` | Bodwin et al. | Phys. Rev. D 104 (2021) 116025 | 2107.07941 | 10.1103/PhysRevD.104.116025 |
| `Bodwin:2023asf` | Bodwin et al. | Phys. Rev. D 109 (2024) 056020 | 2302.05856 | 10.1103/PhysRevD.109.056020 |
| `Bodwin:2025zzi` | Bodwin et al. | preprint (2025) | 2512.11647 |  |
| `Beneke:2024cpq` | Beneke–Ji–Wang | JHEP 05 (2024) 246 | 2403.17738 | 10.1007/JHEP05(2024)246 |
| `Beneke:2019oqx` | Beneke et al. | JHEP 07 (2020) 078 | 1912.01585 | 10.1007/JHEP07(2020)078 |
| `Beneke:2018gvs` | Beneke et al. | JHEP 03 (2019) 043 | 1809.10631 | 10.1007/JHEP03(2019)043 |
| `Beneke:2019mua` | Beneke et al. | JHEP 01 (2020) 094 | 1910.12685 | 10.1007/JHEP01(2020)094 |
| `Beneke:2020ibj` | Beneke et al. | JHEP 10 (2020) 196 | 2008.04943 | 10.1007/JHEP10(2020)196 |
| `Beneke:2022obx` | Beneke et al. | JHEP 07 (2022) 144 | 2205.04479 | 10.1007/JHEP07(2022)144 |
| `Beneke:2025ufd` | Beneke et al. | JHEP 05 (2025) 067 | 2502.01973 | 10.1007/JHEP05(2025)067 |
| `Beneke:2026miy` | Beneke–Schnubel–Szafron | preprint (2026) | 2608.25502 |  |
| `Bonocore:2015esa` | Bonocore et al. | JHEP 06 (2015) 008 | 1503.05156 | 10.1007/JHEP06(2015)008 |
| `Bonocore:2016awd` | Bonocore et al. | JHEP 12 (2016) 121 | 1610.06842 | 10.1007/JHEP12(2016)121 |
| `Bahjat-Abbas:2018hpv` | Bahjat-Abbas et al. | JHEP 10 (2018) 144 | 1807.09246 | 10.1007/JHEP10(2018)144 |
| `Moult:2018jjd` | Moult et al. | JHEP 08 (2018) 013 | 1804.04665 | 10.1007/JHEP08(2018)013 |
| `Moult:2019mog` | Moult–Stewart–Vita | JHEP 11 (2019) 153 | 1905.07411 | 10.1007/JHEP11(2019)153 |

**§6 TMD beyond LP**

| key | authors | journal / status | arXiv | DOI |
|---|---|---|---|---|
| `Vladimirov:2021hdn` | Vladimirov–Moos–Scimemi | JHEP 01 (2022) 110 | 2109.09771 | 10.1007/JHEP01(2022)110 |
| `Rodini:2022wki` | Rodini–Vladimirov | JHEP 08 (2022) 031; [Erratum: JHEP 12, 048 (2022)] | 2204.03856 | 10.1007/JHEP08(2022)031 |
| `Rodini:2023plb` | Rodini–Vladimirov | Phys. Rev. D 110 (2024) 034009 | 2306.09495 | 10.1103/PhysRevD.110.034009 |
| `Vladimirov:2023aot` | Vladimirov | JHEP 12 (2023) 008 | 2307.13054 | 10.1007/JHEP12(2023)008 |
| `Piloneta:2025jjb` | Piloneta–Vladimirov | JHEP 03 (2026) 049 | 2510.14496 | 10.1007/JHEP03(2026)049 |
| `BrisCuerpo:2026pma` | Bris Cuerpo–Arroyo-Castro–Vladimirov | Phys. Rev. D 114 (2026) 034028 | 2603.19833 | 10.1103/6l3x-7phx |
| `Ebert:2021jhy` | Ebert–Gao–Stewart | JHEP 06 (2022) 007; [Erratum: JHEP 07, 096 (2023)] | 2112.07680 | 10.1007/JHEP06(2022)007 |
| `Gamberg:2022lju` | Gamberg et al. | preprint (2022) | 2211.13209 |  |
| `Inglis-Whalen:2021bea` | Inglis-Whalen et al. | Phys. Rev. D 104 (2021) 076018 | 2105.09277 | 10.1103/PhysRevD.104.076018 |
| `Ebert:2018gsn` | Ebert et al. | JHEP 04 (2019) 123 | 1812.08189 | 10.1007/JHEP04(2019)123 |
| `Balitsky:2017flc` | Balitsky–Tarasov | JHEP 07 (2017) 095 | 1706.01415 | 10.1007/JHEP07(2017)095 |
| `Balitsky:2017gis` | Balitsky–Tarasov | JHEP 05 (2018) 150 | 1712.09389 | 10.1007/JHEP05(2018)150 |
| `Balitsky:2024ozy` | Balitsky | Nucl. Phys. B 1006 (2024) 116658 | 2404.15116 | 10.1016/j.nuclphysb.2024.116658 |

**§7 positivity**

| key | authors | journal / status | arXiv | DOI |
|---|---|---|---|---|
| `Candido:2020yat` | Candido–Forte–Hekhorn | JHEP 11 (2020) 129 | 2006.07377 | 10.1007/JHEP11(2020)129 |
| `Collins:2021vke` | Collins–Rogers–Sato | Phys. Rev. D 105 (2022) 076010 | 2111.01170 | 10.1103/PhysRevD.105.076010 |
| `Candido:2023ujx` | Candido et al. | Eur. Phys. J. C 84 (2024) 335 | 2308.00025 | 10.1140/epjc/s10052-024-12681-1 |

**§8 BRST**

| key | authors | journal / status | arXiv | DOI |
|---|---|---|---|---|
| `Joglekar:1975nu` | Joglekar–Lee | Annals Phys. 97 (1976) 160 |  | 10.1016/0003-4916(76)90225-6 |
| `Kluberg-Stern:1974iel` | Kluberg-Stern–Zuber | Phys. Rev. D 12 (1975) 467--481 |  | 10.1103/PhysRevD.12.467 |
| `Kluberg-Stern:1974nmx` | Kluberg-Stern–Zuber | Phys. Rev. D 12 (1975) 482--488 |  | 10.1103/PhysRevD.12.482 |
| `Kluberg-Stern:1975ebk` | Kluberg-Stern–Zuber | Phys. Rev. D 12 (1975) 3159--3180 |  | 10.1103/PhysRevD.12.3159 |
| `Dixon:1974ss` | Dixon–Taylor | Nucl. Phys. B 78 (1974) 552--560 |  | 10.1016/0550-3213(74)90598-7 |
| `Henneaux:1993jn` | Henneaux | Phys. Lett. B 313 (1993) 35--40; [Erratum: Phys.Lett.B 316, 633 (1993)] | hep-th/9306101 | 10.1016/0370-2693(93)91187-R |
| `Barnich:2000zw` | Barnich–Brandt–Henneaux | Phys. Rept. 338 (2000) 439--569 | hep-th/0002245 | 10.1016/S0370-1573(00)00049-1 |
| `Falcioni:2022fdm` | Falcioni–Herzog | JHEP 05 (2022) 177 | 2203.11181 | 10.1007/JHEP05(2022)177 |
| `Gehrmann:2023ksf` | Gehrmann–von Manteuffel–Yang | JHEP 04 (2023) 041 | 2302.00022 | 10.1007/JHEP04(2023)041 |
| `Hamberg:1991qt` | Hamberg–van Neerven | Nucl. Phys. B 379 (1992) 143--171 |  | 10.1016/0550-3213(92)90593-Z |
| `Collins:1994ee` | Collins–Scalise | Phys. Rev. D 50 (1994) 4117--4136 | hep-ph/9403231 | 10.1103/PhysRevD.50.4117 |
| `Collins:2008sg` | Collins–Rogers | Phys. Rev. D 78 (2008) 054012 | 0805.1752 | 10.1103/PhysRevD.78.054012 |
| `Labastida:1984gy` | Labastida–Sterman | Nucl. Phys. B 254 (1985) 425--440 |  | 10.1016/0550-3213(85)90226-3 |
| `Ji:2017oey` | Ji–Zhang–Zhao | Phys. Rev. Lett. 120 (2018) 112001 | 1706.08962 | 10.1103/PhysRevLett.120.112001 |
| `Ishikawa:2017faj` | Ishikawa et al. | Phys. Rev. D 96 (2017) 094019 | 1707.03107 | 10.1103/PhysRevD.96.094019 |
| `Green:2017xeu` | Green–Jansen–Steffens | Phys. Rev. Lett. 121 (2018) 022004 | 1707.07152 | 10.1103/PhysRevLett.121.022004 |

**§9 small x**

| key | authors | journal / status | arXiv | DOI |
|---|---|---|---|---|
| `Balitsky:2007feb` | Balitsky–Chirilli | Phys. Rev. D 77 (2008) 014019 | 0710.4330 | 10.1103/PhysRevD.77.014019 |
| `Balitsky:2006wa` | Balitsky | Phys. Rev. D 75 (2007) 014001 | hep-ph/0609105 | 10.1103/PhysRevD.75.014001 |
| `Kovchegov:2006vj` | Kovchegov–Weigert | Nucl. Phys. A 784 (2007) 188--226 | hep-ph/0609090 | 10.1016/j.nuclphysa.2006.10.075 |
| `Balitsky:2013fea` | Balitsky–Chirilli | Phys. Rev. D 88 (2013) 111501 | 1309.7644 | 10.1103/PhysRevD.88.111501 |
| `Kovner:2013ona` | Kovner–Lublinsky–Mulian | Phys. Rev. D 89 (2014) 061704 | 1310.0378 | 10.1103/PhysRevD.89.061704 |
| `Kovner:2014xia` | Kovner–Lublinsky–Mulian | JHEP 04 (2014) 030 | 1401.0374 | 10.1007/JHEP04(2014)030 |
| `Kovner:2014lca` | Kovner–Lublinsky–Mulian | JHEP 08 (2014) 114 | 1405.0418 | 10.1007/JHEP08(2014)114 |
| `Caron-Huot:2016tzz` | Caron-Huot–Herranen | JHEP 02 (2018) 058 | 1604.07417 | 10.1007/JHEP02(2018)058 |
| `Lappi:2015fma` | Lappi–Mäntysaari | Phys. Rev. D 91 (2015) 074016 | 1502.02400 | 10.1103/PhysRevD.91.074016 |
| `Beuf:2014uia` | Beuf | Phys. Rev. D 89 (2014) 074039 | 1401.0313 | 10.1103/PhysRevD.89.074039 |
| `Iancu:2015vea` | Iancu et al. | Phys. Lett. B 744 (2015) 293--302 | 1502.05642 | 10.1016/j.physletb.2015.03.068 |
| `Caron-Huot:2013fea` | Caron-Huot | JHEP 05 (2015) 093 | 1309.6521 | 10.1007/JHEP05(2015)093 |
| `DelDuca:2013ara` | Del Duca et al. | Phys. Lett. B 732 (2014) 233--240 | 1311.0304 | 10.1016/j.physletb.2014.03.033 |
| `DelDuca:2014cya` | Del Duca et al. | JHEP 02 (2015) 029 | 1409.8330 | 10.1007/JHEP02(2015)029 |
| `Caron-Huot:2017zfo` | Caron-Huot et al. | JHEP 03 (2018) 098 | 1711.04850 | 10.1007/JHEP03(2018)098 |
| `Dominguez:2011wm` | Dominguez et al. | Phys. Rev. D 83 (2011) 105005 | 1101.0715 | 10.1103/PhysRevD.83.105005 |
| `Mueller:2012uf` | Mueller–Xiao–Yuan | Phys. Rev. Lett. 110 (2013) 082301 | 1210.5792 | 10.1103/PhysRevLett.110.082301 |
| `Balitsky:2015qba` | Balitsky–Tarasov | JHEP 10 (2015) 017 | 1505.02151 | 10.1007/JHEP10(2015)017 |
| `Balitsky:2020jzt` | Balitsky | JHEP 05 (2021) 046 | 2012.01588 | 10.1007/JHEP05(2021)046 |
| `Balitsky:2021fer` | Balitsky | JHEP 09 (2021) 022 | 2105.13391 | 10.1007/JHEP09(2021)022 |
| `Balitsky:2023hmh` | Balitsky | JHEP 03 (2023) 029 | 2301.01717 | 10.1007/JHEP03(2023)029 |
| `Balitsky:2026lop` | Balitsky | Phys. Lett. B 882 (2026) 141002 | 2606.07429 | 10.1016/j.physletb.2026.141002 |
| `Kovchegov:2015pbl` | Kovchegov–Pitonyak–Sievert | JHEP 01 (2016) 072; [Erratum: JHEP 10, 148 (2016)] | 1511.06737 | 10.1007/JHEP01(2016)072 |
| `Kovchegov:2016weo` | Kovchegov–Pitonyak–Sievert | Phys. Rev. Lett. 118 (2017) 052001 | 1610.06188 | 10.1103/PhysRevLett.118.052001 |
| `Cougoulic:2022gbk` | Cougoulic et al. | JHEP 07 (2022) 095; [Erratum: JHEP 09, 052 (2024)] | 2204.11898 | 10.1007/JHEP07(2022)095 |
| `Borden:2023ugd` | Borden–Kovchegov | Phys. Rev. D 108 (2023) 014001 | 2304.06161 | 10.1103/PhysRevD.108.014001 |
| `Adamiak:2023okq` | Adamiak–Kovchegov–Tawabutr | Phys. Rev. D 108 (2023) 054005 | 2306.01651 | 10.1103/PhysRevD.108.054005 |
| `Borden:2024bxa` | Borden–Kovchegov–Li | JHEP 09 (2024) 037 | 2406.11647 | 10.1007/JHEP09(2024)037 |
| `Borden:2025ehe` | Borden–Kovchegov | Phys. Rev. D 113 (2026) 034002 | 2508.00195 | 10.1103/ljl6-zvrq |
| `Hatta:2016aoc` | Hatta et al. | Phys. Rev. D 95 (2017) 114032 | 1612.02445 | 10.1103/PhysRevD.95.114032 |
| `Hatta:2022bxn` | Hatta–Zhou | Phys. Rev. Lett. 129 (2022) 252002 | 2207.03378 | 10.1103/PhysRevLett.129.252002 |

**§10 double parton scattering**

| key | authors | journal / status | arXiv | DOI |
|---|---|---|---|---|
| `Diehl:2011yj` | Diehl–Ostermeier–Schafer | JHEP 03 (2012) 089; [Erratum: JHEP 03, 001 (2016)] | 1111.0910 | 10.1007/JHEP03(2012)089 |
| `Manohar:2012jr` | Manohar–Waalewijn | Phys. Rev. D 85 (2012) 114009 | 1202.3794 | 10.1103/PhysRevD.85.114009 |
| `Manohar:2012pe` | Manohar–Waalewijn | Phys. Lett. B 713 (2012) 196--201 | 1202.5034 | 10.1016/j.physletb.2012.05.044 |
| `Diehl:2015bca` | Diehl et al. | JHEP 01 (2016) 076 | 1510.08696 | 10.1007/JHEP01(2016)076 |
| `Diehl:2018wfy` | Diehl–Nagar | JHEP 04 (2019) 124 | 1812.09509 | 10.1007/JHEP04(2019)124 |
| `Vladimirov:2017ksc` | Vladimirov | JHEP 04 (2018) 045 | 1707.07606 | 10.1007/JHEP04(2018)045 |
| `Diehl:2017kgu` | Diehl–Gaunt–Schönwald | JHEP 06 (2017) 083 | 1702.06486 | 10.1007/JHEP06(2017)083 |
| `Buffing:2017mqm` | Buffing–Diehl–Kasemets | JHEP 01 (2018) 044 | 1708.03528 | 10.1007/JHEP01(2018)044 |
| `Diehl:2022rxb` | Diehl–Fabry–Vladimirov | JHEP 05 (2023) 067 | 2212.11843 | 10.1007/JHEP05(2023)067 |
| `Diehl:2019rdh` | Diehl et al. | SciPost Phys. 7 (2019) 017 | 1902.08019 | 10.21468/SciPostPhys.7.2.017 |
| `Diehl:2022dia` | Diehl–Nagar–Plö\ssl | JHEP 09 (2023) 100 | 2212.07736 | 10.1007/JHEP09(2023)100 |
| `Diehl:2020xyg` | Diehl et al. | Eur. Phys. J. C 80 (2020) 468 | 2001.10428 | 10.1140/epjc/s10052-020-8038-z |
| `Diehl:2017wew` | Diehl–Gaunt | Adv. Ser. Direct. High Energy Phys. 29 (2018) 7--28 | 1710.04408 | 10.1142/9789813227767_0002 |

**§11 jets, NGLs**

| key | authors | journal / status | arXiv | DOI |
|---|---|---|---|---|
| `Becher:2015hka` | Becher et al. | Phys. Rev. Lett. 116 (2016) 192001 | 1508.06645 | 10.1103/PhysRevLett.116.192001 |
| `Becher:2016mmh` | Becher et al. | JHEP 11 (2016) 019; [Erratum: JHEP 05, 154 (2017)] | 1605.02737 | 10.1007/JHEP11(2016)019 |
| `Becher:2016omr` | Becher–Pecjak–Shao | JHEP 12 (2016) 018 | 1610.01608 | 10.1007/JHEP12(2016)018 |
| `Caron-Huot:2015bja` | Caron-Huot | JHEP 03 (2018) 036 | 1501.03754 | 10.1007/JHEP03(2018)036 |
| `Banfi:2021owj` | Banfi–Dreyer–Monni | JHEP 10 (2021) 006 | 2104.06416 | 10.1007/JHEP10(2021)006 |
| `Banfi:2021xzn` | Banfi–Dreyer–Monni | JHEP 03 (2022) 135 | 2111.02413 | 10.1007/JHEP03(2022)135 |
| `Becher:2021urs` | Becher–Rauh–Xu | JHEP 08 (2022) 134 | 2112.02108 | 10.1007/JHEP08(2022)134 |
| `Becher:2023vrh` | Becher–Schalch–Xu | Phys. Rev. Lett. 132 (2024) 081602 | 2307.02283 | 10.1103/PhysRevLett.132.081602 |
| `Becher:2026zon` | Becher–Haag–Schalch | preprint (2026) | 2609.09104 |  |
| `Becher:2026iim` | Becher et al. | preprint (2026) | 2609.35972 |  |
| `Larkoski:2015zka` | Larkoski–Moult–Neill | JHEP 09 (2015) 143 | 1501.04596 | 10.1007/JHEP09(2015)143 |
| `Frye:2016aiz` | Frye et al. | JHEP 07 (2016) 064 | 1603.09338 | 10.1007/JHEP07(2016)064 |
| `Hoang:2019ceu` | Hoang et al. | JHEP 12 (2019) 002 | 1906.11843 | 10.1007/JHEP12(2019)002 |
| `Kang:2016mcy` | Kang–Ringer–Vitev | JHEP 10 (2016) 125 | 1606.06732 | 10.1007/JHEP10(2016)125 |
| `Dixon:2019uzg` | Dixon–Moult–Zhu | Phys. Rev. D 100 (2019) 014009 | 1905.01310 | 10.1103/PhysRevD.100.014009 |
| `Kologlu:2019mfz` | Kologlu et al. | JHEP 01 (2021) 128 | 1905.01311 | 10.1007/JHEP01(2021)128 |

**§12 quarkonium**

| key | authors | journal / status | arXiv | DOI |
|---|---|---|---|---|
| `Bodwin:1994jh` | Bodwin–Braaten–Lepage | Phys. Rev. D 51 (1995) 1125--1171; [Erratum: Phys.Rev.D 55, 5853 (1997)] | hep-ph/9407339 | 10.1103/PhysRevD.55.5853 |
| `Nayak:2005rw` | Nayak–Qiu–Sterman | Phys. Lett. B 613 (2005) 45--51 | hep-ph/0501235 | 10.1016/j.physletb.2005.03.031 |
| `Nayak:2005rt` | Nayak–Qiu–Sterman | Phys. Rev. D 72 (2005) 114012 | hep-ph/0509021 | 10.1103/PhysRevD.72.114012 |
| `Nayak:2006fm` | Nayak–Qiu–Sterman | Phys. Rev. D 74 (2006) 074007 | hep-ph/0608066 | 10.1103/PhysRevD.74.074007 |
| `Bodwin:2019bpf` | Bodwin et al. | Phys. Rev. D 101 (2020) 096011 | 1910.05497 | 10.1103/PhysRevD.101.096011 |
| `Kang:2011mg` | Kang–Qiu–Sterman | Phys. Rev. Lett. 108 (2012) 102002 | 1109.1520 | 10.1103/PhysRevLett.108.102002 |
| `Kang:2014tta` | Kang et al. | Phys. Rev. D 90 (2014) 034006 | 1401.0923 | 10.1103/PhysRevD.90.034006 |
| `Kang:2014pya` | Kang et al. | Phys. Rev. D 91 (2015) 014030 | 1411.2456 | 10.1103/PhysRevD.91.014030 |
| `Fleming:2012wy` | Fleming et al. | Phys. Rev. D 86 (2012) 094012 | 1207.2578 | 10.1103/PhysRevD.86.094012 |
| `Ma:2013yla` | Ma–Qiu–Zhang | Phys. Rev. D 89 (2014) 094029 | 1311.7078 | 10.1103/PhysRevD.89.094029 |
| `Ma:2014eja` | Ma–Qiu–Zhang | Phys. Rev. D 89 (2014) 094030 | 1401.0524 | 10.1103/PhysRevD.89.094030 |
| `Bodwin:2014gia` | Bodwin et al. | Phys. Rev. Lett. 113 (2014) 022001 | 1403.3612 | 10.1103/PhysRevLett.113.022001 |
| `Butenschoen:2014dra` | Butenschoen–He–Kniehl | Phys. Rev. Lett. 114 (2015) 092004 | 1411.5287 | 10.1103/PhysRevLett.114.092004 |
| `Han:2014jya` | Han et al. | Phys. Rev. Lett. 114 (2015) 092005 | 1411.7350 | 10.1103/PhysRevLett.114.092005 |
| `Zhang:2014ybe` | Zhang et al. | Phys. Rev. Lett. 114 (2015) 092006 | 1412.0508 | 10.1103/PhysRevLett.114.092006 |
| `Ma:2017xno` | Ma–Chao | Phys. Rev. D 100 (2019) 094007 | 1703.08402 | 10.1103/PhysRevD.100.094007 |

**§13 QED/EW**

| key | authors | journal / status | arXiv | DOI |
|---|---|---|---|---|
| `Manohar:2016nzj` | Manohar et al. | Phys. Rev. Lett. 117 (2016) 242002 | 1607.04266 | 10.1103/PhysRevLett.117.242002 |
| `Manohar:2017eqh` | Manohar et al. | JHEP 12 (2017) 046 | 1708.01256 | 10.1007/JHEP12(2017)046 |
| `Frixione:2019lga` | Frixione | JHEP 11 (2019) 158 | 1909.03886 | 10.1007/JHEP11(2019)158 |
| `Buonocore:2020nai` | Buonocore et al. | JHEP 08 (2020) 019 | 2005.06477 | 10.1007/JHEP08(2020)019 |
| `Bertone:2019hks` | Bertone et al. | JHEP 03 (2020) 135; [Erratum: JHEP 08, 108 (2022)] | 1911.12040 | 10.1007/JHEP03(2020)135 |
| `deFlorian:2015ujt` | de Florian–Sborlini–Rodrigo | Eur. Phys. J. C 76 (2016) 282 | 1512.00612 | 10.1140/epjc/s10052-016-4131-8 |
| `deFlorian:2016gvk` | de Florian–Sborlini–Rodrigo | JHEP 10 (2016) 056 | 1606.02887 | 10.1007/JHEP10(2016)056 |
| `Ciafaloni:2000df` | Ciafaloni–Ciafaloni–Comelli | Phys. Rev. Lett. 84 (2000) 4810--4813 | hep-ph/0001142 | 10.1103/PhysRevLett.84.4810 |
| `Bauer:2017isx` | Bauer–Ferland–Webber | JHEP 08 (2017) 036 | 1703.08562 | 10.1007/JHEP08(2017)036 |
| `Bauer:2018arx` | Bauer–Webber | JHEP 03 (2019) 013 | 1808.08831 | 10.1007/JHEP03(2019)013 |
| `Fornal:2018znf` | Fornal–Manohar–Waalewijn | JHEP 05 (2018) 106 | 1803.06347 | 10.1007/JHEP05(2018)106 |
| `Manohar:2018kfx` | Manohar–Waalewijn | JHEP 08 (2018) 137 | 1802.08687 | 10.1007/JHEP08(2018)137 |
| `Baumgart:2018ntv` | Baumgart et al. | Phys. Rev. D 100 (2019) 096008 | 1811.04120 | 10.1103/PhysRevD.100.096008 |

## Appendix B. Reproducing the checks

```
cd "/Users/hao-cheng/Desktop/theorem proof/qcd_factorization_work/frontier/others/scripts"
for s in s1_landau_gordan s2_crs_yukawa_pdf s3_luxqed_pointlike s4_resummed_series s5_bk_kernel; do
  python3 -I $s.py | tee ../logs/$s.log; done
```
Each script prints `[PASS]/[FAIL]` lines and a total; logs of the 2026-10-10 run are in `logs/` (36/36 PASS).
