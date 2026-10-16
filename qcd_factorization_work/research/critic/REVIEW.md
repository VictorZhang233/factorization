# Critical review of OUTLINE v0 — QCD factorization monograph

Author: critic agent (research phase). Directory: `research/critic/`.
Python checks of every formula used here: `research/critic/checks/c1–c7_*.py` (log in §10).
Status labels: **verified** = checked numerically/symbolically in `checks/`; **standard** = textbook
result I did not re-derive here (the writer must re-check it before using it as a displayed formula);
**(verify)** = an attribution or content claim I am not fully sure of. The refs agent should check these.

Convention: the binding conventions of `CONTEXT.md` (metric $(+,-,-,-)$, $D=4-2\epsilon$, $\overline{\rm MS}$,
$\beta_0 = 11 - \tfrac23 n_f$, $\partial f/\partial\ln\mu^2 = \tfrac{\alpha_s}{2\pi}P\otimes f$, ...) are used throughout.
I write $a\equiv\alpha_s/\pi$, $S_k(n)=\sum_{j=1}^n j^{-k}$, $\mathcal D_k(z)=[\ln^k(1-z)/(1-z)]_+$.

---------------------------------------------------------------------------------------------------

## 0. Executive summary

**Verdict.** OUTLINE v0 is a solid skeleton for collinear and TMD factorization in the
Collins–Soper–Sterman (CSS) tradition, and it is commendably honest about the breakdown cases. As a plan for a
monograph that claims rigor and wants to cover "各种情况，严格的和不严格的", it has five structural defects:

1. **The two levels of "proof" are never separated.** Every [R] statement in factorization theory is a statement
   about *renormalized perturbation theory with IR-regulated partonic external states*, or an algebraic
   consequence of operator definitions. Nothing at the hadron level is rigorous. Even the existence of 4D
   Yang–Mills/QCD as a QFT is unproven (Clay problem). The tag definition already says "非微扰有效性另行说明", but
   the outline never says *where* this separate discussion happens, and it never lists the meta-assumptions that
   carry PT statements over to hadrons. Fix: add explicit meta-assumptions MA0–MA4 (§3) and give every theorem
   box a line "非微扰地位：…".
2. **The step from moments to x-space (Ch5 → Ch8) has real gaps that the outline hides.** (a) If moments are
   $O(1/Q^2)$ for every fixed $n$, the x-space function need not be $O(1/Q^2)$ pointwise. Counterexample:
   $\sin(Q^2x)$ (verified, `c5`). (b) Even moments determine measures and $L^1$ functions on $[0,1]$, but they do
   not determine distributions supported at $x=0$: $\delta'(x)$ has all even moments equal to zero (verified).
   (c) Analytic continuation in $n$ is not unique without growth bounds (Carlson). This is exactly why
   $P_{\rm NS}^{+}\neq P_{\rm NS}^{-}$ from NLO on. "Consistent with Ch5 [R]" (Ch8) is therefore an overstatement
   unless it is made precise.
3. **Mandatory topics are missing or only "brief".** Missing: threshold resummation and refactorization; jets,
   event shapes, non-global and super-leading logarithms; collinear SIDIS; photoproduction and photon structure;
   nuclear targets; polarized DIS (with the $\gamma_5$ problem) and transversity; heavy-quark schemes;
   hadron–hadron jets and hadrons, with their [C] status made explicit; double parton scattering in depth;
   small-$x$; next-to-leading-power (NLP) factorization with endpoint divergences; inclusive $B$ decays. Also
   missing, and foundational: the **Sudakov form factor**, the simplest all-order factorization theorem and the
   template for cusp/rapidity evolution and Wilson lines; and the IR structure of multi-leg amplitudes (Coulomb
   phases), without which the Ch12 material (Catani–de Florian–Rodrigo, super-leading logs) cannot be explained.
4. **The chapter order inverts a dependency.** Ch12 (breakdown; Rothstein–Stewart Glauber *operators*) comes
   before Ch14 (SCET). Jets and event shapes (Ch9) are separated from the SCET machinery that proves their
   factorization (Ch14). Twist-3 single-spin asymmetries (Ch16) are separated from the TMD Sivers function
   (Ch11), although the two match at intermediate $q_T$.
5. **The theorems have no hypotheses.** No theorem in v0 states its kinematic domain (fixed $x$, or
   $x\to1$?), the form of the error term, whether the error is uniform, or which variables are held fixed. A
   rigorous monograph must state these. See the 30 backbone statements in §8.

**Top-10 action list for the lead author.**

| # | Action | Where |
|---|---|---|
| 1 | Make [R] precise as two sub-kinds, $R_{\rm PT}$ (all orders of PT, partonic/IR-regulated Green functions) and $R_{\rm def}$ (algebraic consequence of operator definitions + symmetries). State MA0–MA4. Give every theorem box a "非微扰地位" line. | Ch1, legend |
| 2 | Insert the Sudakov form factor (regions → Ward identities → Wilson lines → $K$+$G$ evolution → cusp → exponentiation) as the first all-order factorization theorem. | new Ch "Sudakov" before Ch7 |
| 3 | Rebuild the Ch5 logic: Euclidean OPE applied to the Taylor coefficients of $T(\omega,Q^2)$ at $\omega=0$, then the dispersion relation. The light-cone OPE is **not needed** for moments. Add Lemmas L1–L4 (§8, B8). | Ch5 |
| 4 | Add to Ch2/App: $\gamma_5$ in DR (HVBM + Larin finite renormalization); BRST and ghosts in cut diagrams; renormalization and mixing of gauge-invariant composite operators (Joglekar–Lee, Kluberg-Stern–Zuber); Wilson-loop (cusp) renormalization. | Ch2, App |
| 5 | Put SCET before the breakdown chapter, or move the Glauber-operator material into the SCET chapter. | reorder |
| 6 | Add chapters/sections: threshold & refactorization; jets/NGLs/SLLs; other collinear processes (SIA, SIDIS, photoproduction, nuclei, polarized, heavy-quark schemes); small-$x$; NLP and endpoint factorization. | §4, §5 |
| 7 | Split hadron–hadron statements: DY/W/Z/H (colourless final state) [A]; $pp\to$ jets/hadrons [C]; heavy-quark pairs [A] or [C] after the refs agent checks CSS 1986. | Ch10 |
| 8 | State every theorem with hypotheses, domain, error term and uniformity (templates in §8). | all |
| 9 | Add misconception boxes (28 candidates in §7). | all |
| 10 | Use only verified one-loop constants as displayed formulas (§6, §10). Several half-remembered literature formulas are wrong (example in §10). | all |

---------------------------------------------------------------------------------------------------

## 1. Global assessment

**What is right.** The overall arc is right: a rigorous core (OPE) first, then all-order arguments
(diagrammatic), then breakdown. The choice of Collins' subtraction formalism as the organizing method is right.
The one-loop checks chosen (DIS $F_2$, $F_L$; DY $q\bar q$, $qg$; $P_{qq}$ from the operator; CS kernel) are the
right ones. Honest [V] items (TMD breaking in $pp\to h_1h_2X$, hadron–hadron diffraction) are present.

**Structural weaknesses.**

- (W1) PT and hadron-level statements are not separated (see 0.1).
- (W2) The book is collinear-centric. The process catalogue is incomplete (see §4).
- (W3) The order inverts dependencies (see 0.4).
- (W4) There is no amplitude-level IR factorization: no Sudakov form factor, no multi-leg IR poles, no Coulomb
  phases, no splitting amplitudes. These are prerequisites for understanding (i) why the Glauber region exists,
  (ii) the Catani–de Florian–Rodrigo violation, (iii) super-leading logarithms, and (iv) the cusp anomalous
  dimension that drives every Sudakov resummation in the book.
- (W5) Statement hygiene is missing (see 0.5). Typical failures: "$O(\Lambda^2/Q^2)$" written without saying
  that the coefficient depends on $x$ and blows up as $x\to1$ or $x\to0$; "all orders" written without saying
  "as a formal power series" (perturbative series are asymptotic, with renormalons).
- (W6) There is no explicit glossary of the *kinds* of factorization: collinear, TMD, threshold (soft), high-energy
  ($k_T$), exclusive (DA/GPD), heavy-quark (NRQCD/HQET), EFT-matching (SCET), lattice (LaMET/SDF). Ch1 should
  have a taxonomy table with columns: which scales; which functions; what is evolved (μ, ζ, ν, rapidity, x);
  typical proof technique; status.

---------------------------------------------------------------------------------------------------

## 2. Over-claimed, imprecise or wrong rigor statements in OUTLINE v0

Each item gives: what v0 says → problem → correction and recommended tag.

**O1 (Ch1, "what proof means: asymptotic expansion in Λ/Q, all orders in α_s").** This mixes two different
expansions. What has actually been proved, at best, is the following. *For partonic external states with an IR
regulator (DR or masses), at each fixed order in α_s, the leading term of the large-Q expansion of the cross
section equals $H\otimes f_{\rm partonic}$; H is IR finite and independent of the external state.* Carrying this
over to hadrons is an **assumption** (MA1–MA2 in §3). The exception is inclusive DIS and $e^+e^-$, where the OPE
plus nonperturbative OPE validity gives a cleaner route. "All orders" means formal power series. The series is
asymptotic (renormalons), so "$+O((\Lambda/Q)^p)$" only has meaning once a definition of the power-correction
term is specified. Ch1 must state all of this.

**O2 (the [R] tag).** "严格：在重整化微扰论的每一阶有数学上完整的证明" is far stronger than what exists for almost
any factorization statement at the level of rigor of BPHZ or Zimmermann. Recommendation: keep the tag but make
explicit, in the legend and in Ch1, that [R] has exactly two sub-kinds.
- $R_{\rm PT}$: e.g. IR finiteness of $\sigma_{\rm tot}(e^+e^-)$; the Euclidean OPE; twist-2 DIS moments; DGLAP from
  renormalization of local operators; one-loop statements.
- $R_{\rm def}$: algebraic consequences of operator definitions and symmetries, e.g. gauge invariance, support,
  charge-conjugation relation, sum rules, Sivers sign reversal, the CS/RG equations once the TMD definition is
  fixed.

Everything diagrammatic at all orders (DIS momentum-space, DY, TMD, SCET) is at most [A]. In each theorem box the
line "非微扰地位" must say which meta-assumptions are used.

**O3 (Ch4, "IR finiteness to all orders and R = R_0(1 + α_s/π + O(α_s²))").** The PT statement is correct, but
v0 gives no proof route. The cleanest rigorous route:
- (i) $\Pi(q^2)$ at Euclidean $q^2<0$ has no IR divergences in massless PT, because there are no exceptional
  momenta. This is Euclidean power counting; Lowenstein–Zimmermann-type arguments (verify the gauge-theory
  coverage).
- (ii) The RG plus dimensional analysis make $\Pi^{(n)}$ a polynomial in $\ln(-q^2/\mu^2)$ with finite
  coefficients.
- (iii) $R = 12\pi\,{\rm Im}\,\Pi(s+i0)$ then follows by trivial analytic continuation at each order.

Sterman's cut-diagram proof (1976, 1978) is the diagrammatic alternative and should be presented as such. The
claim must **not** be read pointwise in $s$ for hadrons: near resonances and thresholds the perturbative $R(s)$
is meaningful only after smearing (Poggio–Quinn–Weinberg). Duality violations are a [C]-level issue (Shifman).
A verified NNLO statement worth displaying: (verified, `c4`)
$$R=N_c\sum_q e_q^2\Big[1+a+\Big(\tfrac{365}{24}-11\zeta_3-n_f\big(\tfrac{11}{12}-\tfrac23\zeta_3\big)\Big)a^2+O(a^3)\Big],
\quad a=\frac{\alpha_s(\sqrt s)}{\pi},$$
numerically $1.9857-0.1153\,n_f$. It is MS-bar at $\mu^2=s$, for massless quarks, without $Z$ exchange. The singlet
$(\sum e_q)^2$ term first appears at $O(a^3)$; at $O(a^2)$ it vanishes by Furry's theorem (a link to the previous
monograph).

**O4 (Ch5, "light-cone OPE with twist-2 operators … theorem (moment factorization) [R in PT]").** The moment theorem
does **not** need the light-cone OPE. The $n$-th Taylor coefficient of the forward Compton amplitude
$T(\omega,Q^2)$ at $\omega=0$ (i.e. at $P\cdot q=0$, $q$ spacelike, the Euclidean-like region) is governed by the
**Euclidean short-distance OPE** (Wilson–Zimmermann), which is $R_{\rm PT}$ for Green functions at non-exceptional
Euclidean momenta. Moments then follow from analyticity in $\omega$ (cuts only on $|\omega|\ge1$) and a contour
argument. The contour argument needs the large-$|\omega|$ behaviour of $T$ (Regge input) for the **lowest**
moments. For example, $\int dx\,F_1$ requires $F_1\lesssim x^{-1+\delta}$. Recommendation:
(a) present moments via the Euclidean OPE ($R_{\rm PT}$);
(b) present the light-cone/light-ray OPE (Christ–Hasslacher–Mueller 1972; Balitsky–Braun light-ray operators;
proof in renormalized PT by Anikin–Zavialov 1978 (verify)) as the x-space structure behind it, tagged [A] unless
the refs agent confirms a complete proof;
(c) list the gauge-theory subtleties: mixing with BRST-exact and EOM-vanishing operators (Joglekar–Lee 1976;
Kluberg-Stern–Zuber 1975), and trace subtractions.

**O5 (Ch5, "Hausdorff/Müntz uniqueness from even moments").** The statement is true for finite measures and
$L^1$ functions on $[0,1]$. Müntz–Szász is overkill: push forward under $x\mapsto x^2$ (a bijection of $[0,1]$),
and the even moments of $\mu$ become *all* moments of the image measure. These determine it by
Hausdorff/Weierstrass. The statement is **false for distributions supported at $x=0$**: $\langle\delta',x^{2m}\rangle=0$
for all $m\ge0$ (verified, `c5`). This matters because twist-3 distributions can contain $\delta(x)$ terms
(Burkardt–Koike 2002), and partonic structure functions are distributions. State the lemma for measures/$L^1$,
and separately for distributions supported in $[0,1]$ when all integer moments are known. In that case the
Fourier transform is entire and its Taylor coefficients are the moments, so they determine the distribution.

**O6 (Ch5, "DGLAP from anomalous dimensions").** The x-space kernel is the inverse Mellin transform of an
**analytic continuation** of $\gamma(n)$ off the integers where the operators exist. Carlson's theorem gives
uniqueness only for functions of exponential type $<\pi$ along the imaginary direction. From even integers alone
the bound is effectively $<\pi/2$. $(1-\cos\pi n)/2$ vanishes on all even $n$ (verified). In practice: the
non-singlet "$+$" (from even $n$, $q+\bar q$) and "$-$" (from odd $n$, $q-\bar q$) continuations are different
functions. $P_{\rm NS}^{+}-P_{\rm NS}^{-}$ starts at NLO with colour factor $C_F(C_F-C_A/2)$ (standard;
Curci–Furmanski–Petronzio 1980). The chapter must say which continuation defines which kernel. In e.m. DIS only
even moments are measured.

**O7 (Ch8, "theorem [A] (consistent with Ch5 [R])").** As written, "consistent" suggests that x-space
factorization at fixed $x$ with an $O(\Lambda^2/Q^2)$ error follows from Ch5. It does not.
- (i) The twist-2 part of the x-space formula is equivalent to the moment statement **in the sense of
  distributions** ($R_{\rm PT}$ for partonic targets).
- (ii) The size of the remainder pointwise in $x$ is *not* controlled by the moments. Moments $O(1/Q^2)$ for each
  fixed $n$ do not give pointwise $O(1/Q^2)$; $\sin(Q^2x)$ is the counterexample (verified).
- (iii) The higher-twist coefficients grow with $n$, so the expansion is non-uniform as $x\to1$. The heuristic
  expansion parameter is $\Lambda^2/(Q^2(1-x))$, i.e. one needs $W^2\gg\Lambda^2$ (heuristic). It is also
  non-uniform as $x\to0$ (saturation).

Correct form: x-space leading-power factorization at fixed $0<x<1$ is [A], resting on MA1–MA2 and smoothness.
The resonance region is described only after smearing (Bloom–Gilman duality, [C]).

**O8 (Ch6, "light-cone gauge number-density interpretation").** This is a **heuristic**, not a theorem. It holds
for *bare* PDFs in $A^+=0$ gauge, which are UV divergent; in $A^+=0$ gauge they also have spurious $1/k^+$
singularities that need prescriptions. It does not imply positivity of $\overline{\rm MS}$ PDFs. Positivity is
[C] and genuinely debated: Candido–Forte–Hekhorn 2020 vs. Collins–Rogers–Sato 2022.

**O9 (Ch6, "support 0 ≤ ξ ≤ 1").** With the CONTEXT convention $f_{\bar q}(\xi)=-f_q(-\xi)$, the support is
$-1\le\xi\le1$. The proof is the spectral condition $p_X^+\ge0$ (Jaffe 1983; Collins 2011). Support survives
$\overline{\rm MS}$ renormalization because the renormalization kernel $Z(\xi/\zeta)$ vanishes for $\xi>\zeta$. Tag
$R_{\rm def}$ (given the matrix elements exist). Mention that the point $\xi=0$ is delicate (twist-3 $\delta(x)$
terms) and that light-cone gauge needs separate care.

**O10 (Ch7, "Collins' subtraction formalism … analogue of the BPHZ forest formula").** The analogy is fine
pedagogically, but the text must not suggest BPHZ-level rigor. BPHZ rests on Weinberg's (Euclidean) power-counting
theorem and Zimmermann's convergence theorem. No Minkowski-space, massless-gauge-theory analogue of Weinberg's
theorem exists. IR power counting needs pinch-surface analysis with contour deformations, nested and overlapping
regions, and the Glauber region; for TMDs it also needs rapidity regulators. Tag [A].

**O11 (Ch3, "method of regions … status").** Be precise.
- For Euclidean limits (large momenta/masses) the asymptotic expansion theorems are proven [R] (Smirnov 1990;
  Chetyrkin, Gorishny, Tkachov asymptotic operation).
- For Minkowskian limits (threshold, Sudakov, Regge) there is no general proof [P]. Partial justifications exist
  (Jantzen 2011; the geometric/Newton-polytope approach of Pak–Smirnov 2011; Semenova–Smirnov–Smirnov 2019).
  Additional analytic or rapidity regulators are needed when DR does not separate regions (collinear anomaly,
  rapidity divergences).
- The off-shell Sudakov example is good, but it should be paired with the on-shell massive form factor
  ($m^2\ll Q^2$), where pure DR fails to regulate the collinear regions separately.

**O12 (Ch3, Landau equations).** They are **necessary** conditions for singularities (non-analyticity in external
invariants), not sufficient. Also distinguish:
- (i) singularities of amplitudes as functions of external invariants (Landau, Coleman–Norton), from
- (ii) IR divergences and logarithmic sensitivity at *fixed* external momenta in massless theories (Sterman 1978:
  pinch surfaces in loop-momentum space).

The outline merges the two. Also include endpoint (non-pinch) contributions and second-type singularities, at
least as a remark.

**O13 (Ch10, "soft factor = 1 for inclusive").** This is correct only for **collinear-integrated** inclusive
cross sections. It holds after (i) contour deformation out of the Glauber region, (ii) the eikonal approximation,
(iii) the unitarity sum over soft final states, which gives $\langle0|\bar T(W^\dagger\cdots)T(W\cdots)|0\rangle\to1$
for fully inclusive soft radiation, and (iv) in DR, scaleless integrals. In TMD factorization the soft factor is
essential, carries rapidity divergences, and is absorbed into the TMDs by definition.

**O14 (Ch10, "other hadron–hadron processes … and their status").** Tag separately.
- $W/Z/\gamma^*$, Higgs, and colourless final states in general: [A]. This is the same argument as DY; for Higgs
  add EFT matching to the $ggH$ operator, or keep the full top loop.
- High-$p_T$ jets and hadrons in $pp$: [C]. They are universally assumed, but no complete all-order proof exists.
  Coloured final states obstruct the CSS Glauber argument. Partial arguments: Aybat–Sterman 2009 (verify).
  Strict collinear factorization is violated at amplitude level (Catani–de Florian–Rodrigo 2012). Super-leading
  logs appear in gap observables (Forshaw–Kyrieleis–Seymour 2006).
- Heavy-quark pairs: Collins–Soper–Sterman 1986 argued factorization. The refs agent must check how complete
  their Glauber treatment is; tag [A] if confirmed, otherwise [C].

**O15 (Ch11, "Sivers sign change (T-reversal) [R given factorization]").** Split. (a) $f_{1T}^{\perp,\rm SIDIS}=-f_{1T}^{\perp,\rm DY}$
as a relation between **operator-defined** functions is $R_{\rm def}$ (PT + time reversal + parity applied to
future- vs past-pointing staples; Collins 2002). It does not depend on factorization. (b) The statement that
the measured asymmetries are related with opposite sign uses TMD factorization [A]. Add the companion
statement that the T-odd *fragmentation* functions (Collins function) are universal (no sign change)
(Collins–Metz 2004; Meissner–Metz 2009).

**O16 (Ch12, "violation of strict collinear factorization for space-like splittings [V]").** This is correct
**at the amplitude (and squared-amplitude) level** for multi-parton configurations. Do not conflate it with a
violation of PDF factorization for DY. Its cross-section-level consequences are tied to the Coulomb/Glauber
exchanges behind super-leading logarithms, and they cancel in sufficiently inclusive observables. The general
status is open. Tag: [V] for strict amplitude-level collinear factorization; the DY collinear theorem stays [A].

**O17 (Ch12, diffraction).** Diffractive DIS with universal diffractive PDFs: [A] (Collins 1998). Hadron–hadron
hard diffraction with the *same* diffractive PDFs: [V]. The violation is established phenomenologically
(Tevatron vs HERA, gap-survival suppression) and has a theoretical mechanism (spectator–spectator interactions;
the Glauber argument fails for gap observables). Say explicitly that the [V] is not an explicit perturbative
counterexample of the Collins–Qiu kind.

**O18 (Ch13, "transverse-photon meson production and endpoint divergences").** Do not leave this as an open
"status". At leading twist, $\gamma_T^*\,p\to M\,p$ is power suppressed, and the would-be factorized twist-3
amplitude has endpoint divergences. Collinear factorization therefore fails in its standard form [V], in
contrast to $\gamma_L^*$ [A] (Collins–Frankfurt–Strikman 1997). Mankiewicz–Piller 2000 (verify) is the usual
reference.

**O19 (Ch14, "B → ππ QCD factorization … [P]").** Split.
- The leading-power factorization formula (BBNS 1999/2000; SCET: Bauer–Pirjol–Rothstein–Stewart 2004): [A],
  with known disagreements about the power counting of charm penguins and the treatment of hard-spectator
  terms.
- Subleading power (annihilation, twist-3 spectator): endpoint divergences, so standard factorization fails
  there [V]. It is usually parametrized ($X_A$, $X_H$).
- $B\to D\pi$: [A] (BBNS 2000; Bauer–Pirjol–Stewart 2001).

**O20 (Ch16, renormalons).** Tag the large-$\beta_0$ (bubble-chain) statements [P]. The general statement that
IR-renormalon ambiguities correspond one-to-one to higher-twist matrix elements is [C]. Example to include: in the
Adler function at large $\beta_0$, there is no IR renormalon at $u=1$, consistent with the absence of a
dimension-2 gauge-invariant operator, and the first one is at $u=2$ (gluon condensate) (standard).

**O21 (Ch4, Ch16, "status of factorization beyond perturbation theory").** Add the only genuinely
nonperturbative "laboratories". (i) The 't Hooft model (2D QCD at large $N_c$): Bjorken scaling and parton
distributions computable exactly (Callan–Coote–Gross 1976; Einhorn 1976) [R in that model]. (ii) Convergence of
the OPE in perturbative Euclidean $\varphi^4$ (Hollands–Kopper 2012) [R]. (iii) Lattice evidence [P].

---------------------------------------------------------------------------------------------------

## 3. Circular arguments and hidden assumptions

### 3.1 Meta-assumptions that must be stated explicitly in Ch1

Every hadron-level factorization statement silently uses some of these. Each theorem box should cite them.

- **MA0 (existence).** QCD exists as a QFT. Hadron states $|P\rangle$ exist. Renormalized composite (light-ray)
  operators have well-defined matrix elements, at least as distributions in $\xi$. This is unproven: the
  existence of 4D Yang–Mills is a Clay Millennium problem.
- **MA1 (region completeness).** The leading-power regions found in PT (massless partons, IR regulated) are the
  *only* leading-power regions of full QCD. Confinement modifies only the IR-sensitive factors (PDFs, FFs, soft
  factors) and creates no new leading region.
- **MA2 (power-counting transfer).** Power suppression of non-leading regions, established in PT, becomes
  suppression by $(\Lambda/Q)^p$ in full QCD. PT alone does not fix $p$ outside OPE-accessible processes.
- **MA3 (analyticity and high-energy behaviour).** These are needed for dispersion relations (moments), in
  particular for the lowest moments and their convergence at small $x$.
- **MA4 (asymptoticity).** Perturbative series are asymptotic. "All orders" means formal power series.
  Renormalon ambiguities are of the same order as power corrections, so leading-power factorization is an
  asymptotic statement, and "exact up to power corrections" has meaning only once the power-correction term is
  defined.

### 3.2 Places where a proof in the planned chapters would be circular or rest on unproven input

**C1 (Ch6 ↔ Ch5/Ch8). PDFs defined by the cross section.** If the PDF is defined as "whatever multiplies $C$ in
DIS" (the DIS scheme is a legitimate *choice*), then universality is not a consequence; it *is* the content of
the factorization theorem for the second process. The book must use operator definitions first (Ch6), prove
factorization with them, and only then discuss schemes.

**C2 (DGLAP ↔ μ-independence).** Deriving DGLAP from the $\mu$-independence of $\sigma$ and then using DGLAP to
"prove" that $\sigma$ is $\mu_F$-independent is circular. The correct logical order: (i) DGLAP from operator
renormalization (Ch6); (ii) factorization; (iii) RG consistency of $C$ as a corollary, checked at $O(\alpha_s)$.

**C3 (number-density picture → support, positivity, sum rules).** Using the probabilistic picture to "prove"
properties of renormalized $\overline{\rm MS}$ PDFs is invalid. Support and sum rules have independent proofs
(spectral condition; conserved currents; energy–momentum tensor). Positivity has none ([C]).

**C4 (OPE → x-space power corrections).** Using the OPE to justify pointwise $O(\Lambda^2/Q^2)$ x-space errors
is invalid; see O7 and the counterexample in §10.

**C5 (method of regions ↔ leading regions).** Using the method of regions to identify the leading regions, and
then the factorized result to "confirm" the method of regions, is circular in Minkowski kinematics. The region
identification must come from Landau/pinch analysis plus power counting (Ch3). The method of regions is a
cross-check.

**C6 (SCET mode completeness).** An SCET factorization "proof" assumes that the chosen modes (hard, collinear,
soft/ultrasoft, possibly Glauber) reproduce the full IR of QCD. That assumption *is* the region analysis. It is
not circular, but it is the hard part and must be stated as a hypothesis. The Glauber mode either has to be
argued away or kept through the Rothstein–Stewart Glauber operator, and then its cancellation must still be
shown. Zero-bin subtractions (Manohar–Stewart 2007) are the EFT counterpart of Collins' subtractions; double
counting is avoided only if they are carried out consistently.

**C7 (Ward identities on unapproximated graphs).** Graphical Ward identities hold for on-shell, physically
polarized external lines (plus ghost terms in the non-abelian case). In factorization proofs they are applied to
**approximated** graphs: the collinear momenta entering the hard part are replaced by $\hat k$ and the
Grammer–Yennie K-gluons are isolated. Applying Ward identities before making the approximations generates
uncontrolled terms. The order "approximate → Ward identity → Wilson line" must be respected, and the leftover
non-abelian/ghost terms must be shown to cancel or to be power suppressed. Labastida–Sterman 1985 and CSS
discuss this; tag [A].

**C8 (Glauber cancellation "because the observable is inclusive").** Inclusivity is needed *in the spectator
final state*, and the measured variable must not obstruct the contour deformation. For TMD DY the measurement
of $q_T$ does not obstruct it. For $pp\to h_1h_2X$ (TMD) it fails (Collins–Qiu 2007; Rogers–Mulders 2010). For
hadronic $E_T$ / beam-thrust-type observables Gaunt (2014) argued it fails (verify the exact claims). So
"inclusive enough" is a theorem to be proved for each observable, not a slogan.

**C9 (TMD universality from definitions).** If TMDs are *defined* through the factorization formula (with the
square root of the soft factor), then universality between SIDIS and DY holds only **up to the Wilson-line
direction**. It must be derived from the operator definitions (staple orientation) together with T-invariance.
It cannot be assumed.

**C10 (rapidity regulators).** Some regulators break gauge invariance or non-abelian exponentiation (e.g. naive
$\delta$-regulators at higher orders), or need a limit (tilted Wilson lines, $y_n\to-\infty$) that may be taken
only after the factors are combined. Claims that an *individual* TMD or soft function is regulator-independent
are false. Only the properly combined objects (Collins' $\tilde f(x,b_T;\mu,\zeta)$) are.

**C11 (power of the remainder).** "The remainder is $O(\Lambda^2/Q^2)$ because the first higher-twist operators
have dimension two higher" is an OPE statement. It is valid for inclusive DIS and $e^+e^-$ moments (in PT
plus MA0, MA4), but in DY and other non-OPE processes it is [C]. Renormalon analyses (e.g. Beneke–Braun 1995 for
DY, verify) suggest but do not prove $1/Q^2$.

**C12 (lattice "verification").** Lattice determinations of moments or quasi-PDFs supply matrix elements. They do
not test factorization of a hadronic cross section. LaMET and pseudo-PDF approaches rely on their own
factorization theorems (Ma–Qiu 2018; Izubuchi et al. 2018), [A].

**C13 (positivity preservation).** "LO DGLAP preserves positivity, hence $\overline{\rm MS}$ PDFs are positive" is
circular: the positivity of the initial condition in $\overline{\rm MS}$ is exactly what is in question.
Beyond LO, positivity preservation is also scheme-dependent.

**C14 (partonic PDF in DR).** "$f_{q/q}=\delta(1-x)$ to all orders in DR, so $C$ = partonic cross section". The
*bare* partonic PDF is $\delta(1-x)$ because all loop corrections are scaleless. The *renormalized* one is
$\delta(1-x)$ plus pure IR poles, $-\tfrac{\alpha_s}{2\pi}\tfrac{1}{\epsilon_{\rm IR}}P_{qq}(x)+\dots$, whose
precise sign and normalization depend on the convention for $\epsilon$. In other words, the UV counterterm is
re-interpreted as an IR pole. The text must make this UV/IR bookkeeping explicit, or the cancellation of
collinear poles in $C$ looks like magic and invites sign errors.

**C15 (Coleman–Norton used for Euclidean or unphysical regions).** Coleman–Norton applies to physical-region
pinches with $\alpha_i\ge0$. It cannot be used to argue the absence of singularities elsewhere, e.g. in the
unphysical $\omega$ region used in the dispersion relation; there the argument is spectral support/causality.

---------------------------------------------------------------------------------------------------

## 4. Missing topics

Priority: **M** = must (otherwise "包含各种情况" is not met), **S** = should, **c** = could.
Tags are my recommendations.

| # | Topic (what to cover) | Status / tag | Placement | Key references | Pri. |
|---|---|---|---|---|---|
| 1 | **Amplitude-level IR factorization**: Sudakov form factor ($K+G$ evolution, exponentiation, cusp $\gamma_K=2C_F\alpha_s/\pi$ at one loop, verified); multi-leg IR poles (Catani 1998; Sterman–Tejeda-Yeomans 2003; Becher–Neubert 2009; Gardi–Magnea 2009); first non-dipole corrections at three loops (Almelid–Duhr–Gardi 2016); Coulomb phases; splitting amplitudes | Sudakov FF [A]; dipole structure [R] through the orders computed, [A] all-order structure | new chapter before Ch7 | Mueller 1979; Collins 1980, 1989; Sen 1981, 1983; Korchemsky–Radyushkin 1987; Magnea–Sterman 1990 | M |
| 2 | **$\gamma_5$ in DR**, BRST and ghosts in cut diagrams, renormalization/mixing of gauge-invariant composite operators, Wilson-loop (cusp) renormalization | [R] (standard results) | Ch2 + App | 't Hooft–Veltman 1972; Breitenlohner–Maison 1977; Larin 1993; Joglekar–Lee 1976; Kluberg-Stern–Zuber 1975; Brandt–Neri–Sato 1981 | M |
| 3 | **Polarized DIS & PDFs**: $g_1,g_2$; OPE with odd $n$; Bjorken sum rule (verified $a^2$ coefficient: $\tfrac{g_A}{6}[1-a-(\tfrac{55}{12}-\tfrac{n_f}{3})a^2]$); Ellis–Jaffe (assumption-based, violated: "spin crisis"); axial anomaly and the scheme dependence of the first moment/$\Delta G$; Burkhardt–Cottingham [C]; Wandzura–Wilczek [V] in general; polarized DY ([A]) and $A_{LL}$ for jets/$\pi^0$ ([C]) | mixed | new section in "other collinear processes" | Kodaira 1980; Altarelli–Ross 1988; Carlitz–Collins–Mueller 1988; Larin–Vermaseren 1991; Altarelli–Lampe–Nason–Ridolfi 1994 | M |
| 4 | **Transversity $h_1$**: chiral-odd; absent from inclusive DIS at leading twist; LO evolution has no gluon mixing; Soffer bound (LO; scheme-dependent beyond); access via SIDIS Collins effect (TMD), dihadron FFs (collinear), transversely polarized DY | [A] for the processes | same | Ralston–Soper 1979; Jaffe–Ji 1991–92; Soffer 1995 | M |
| 5 | **Heavy-quark schemes**: Collins–Wilczek–Zee decoupling scheme; FFNS vs ZM-VFNS vs GM-VFNS (ACOT, S-ACOT, FONLL, TR); Collins 1998 theorem (error power suppressed uniformly in $m/Q$, verify wording); PDF matching at thresholds (Buza et al. 1998); perturbative heavy-quark FFs (Mele–Nason 1991); intrinsic charm (a nonperturbative and scheme question) | [A] | other collinear processes | Collins–Wilczek–Zee 1978; ACOT 1994; Collins 1998; Krämer–Olness–Soper 2000; Cacciari–Greco–Nason 1998; Thorne–Roberts 1998 | M |
| 6 | **Threshold resummation & refactorization** (DY, DIS, Higgs): refactorization near $z\to1$; Mellin exponent (verified normalization: $A^{(1)}=C_F\alpha_s/\pi$ reproduces the $8C_F\mathcal D_1$ term); partonic vs hadronic threshold; Landau pole and minimal prescription; SCET momentum-space version | refactorization [A]; prescriptions are prescriptions | new chapter after DY | Sterman 1987; Catani–Trentadue 1989; Catani–Mangano–Nason–Trentadue 1996; Becher–Neubert–Pecjak 2007; Becher–Neubert–Xu 2008 | M |
| 7 | **Jets, event shapes, NGLs, SLLs**: Sterman–Weinberg cones; IR safety of algorithms (iterative cones unsafe; $k_t$/anti-$k_t$/SISCone safe); thrust factorization (verified singular terms); hadronization $1/Q$ corrections; non-global logs; BMS equation; multi-Wilson-line factorization; jet vetoes; super-leading logs and their Coulomb-phase origin | thrust [A]; NGL factorization [A] (verify the status of Becher–Neubert–Rothen–Shao 2016); $1/Q$ universality [C] | new chapter after SCET | Sterman–Weinberg 1977; Dasgupta–Salam 2001; Banfi–Marchesini–Smye 2002; Forshaw–Kyrieleis–Seymour 2006; Becher–Neubert–Shao 2021 (verify); Dokshitzer–Webber 1995; Korchemsky–Sterman 1995 | M |
| 8 | **Collinear SIDIS** ($P_{hT}$ integrated, or $P_{hT}\sim Q$), with both PDF and FF; matching to TMD (W+Y) | [A] | other collinear processes | Collins 2011 (ch. 12–13); Graudenz 1994 (verify) | M |
| 9 | **Hadron–hadron jets/hadrons/heavy quarks**, status made explicit | [C] / [A?] | Ch10 | CSS 1986; Aybat–Sterman 2009 (verify); Catani–de Florian–Rodrigo 2012; Forshaw–Seymour–Siodmok 2012 (verify) | M |
| 10 | **NLP factorization**: next-to-soft theorems (Low 1958; Burnett–Kroll 1968; Del Duca 1990); NLP SCET; endpoint divergences and refactorization; DY threshold at NLP | [P]/[A] in specific cases | power-corrections chapter | Liu–Neubert 2020; Liu–Mecaj–Neubert–Wang 2021; Beneke et al. 2019 | M |
| 11 | **Photoproduction and photon structure**: direct vs resolved; inhomogeneous evolution; point-like photon structure function (Witten 1977); factorization breaking in resolved and diffractive photoproduction; photon PDF of the proton from structure functions (LUXqed) | [A] (direct, inclusive); [C] (resolved, diffractive) | other collinear processes | Witten 1977; Manohar–Nason–Salam–Zanderighi 2016, 2017 | S |
| 12 | **Nuclear targets**: the same theorem with nuclear PDFs at leading power; nuclear-enhanced power corrections $\propto A^{1/3}\Lambda^2/Q^2$; leading-twist shadowing via diffractive PDFs; $p_T$ broadening; hard probes in $AA$ (vacuum FFs fail in medium) | LP [A]; enhanced HT [P]; medium [C]/[V] | other collinear processes | Qiu–Vitev 2004; Frankfurt–Guzey–Strikman 2012 | S |
| 13 | **Double parton scattering**: double DY at leading power with colour/spin-correlated DPDFs, $1\!\otimes\!2$ splitting and double counting with SPS; Glauber cancellation in double DY; the "pocket formula" $\sigma_{\rm eff}$ is a model | double DY [A]; pocket formula [C] | breakdown/beyond chapter | Diehl–Ostermeier–Schäfer 2012; Manohar–Waalewijn 2012; Diehl–Gaunt–Ostermeier–Plößl–Schäfer 2016; Diehl–Gaunt–Schönwald 2017; Gaunt–Stirling 2010 | S |
| 14 | **Small-$x$**: non-uniformity of collinear factorization as $x\to0$ at fixed $Q$; high-energy ($k_T$) factorization; BFKL (LL, NLL); BK/JIMWLK; saturation; WW vs dipole gluon TMDs | BFKL [A] in the perturbative Regge limit; $k_T$ factorization [P]; saturation [C] | new chapter | Kuraev–Lipatov–Fadin 1977; Balitsky–Lipatov 1978; Catani–Ciafaloni–Hautmann 1991; Collins–Ellis 1991; Fadin–Lipatov 1998; Ciafaloni–Camici 1998; Balitsky 1996; Kovchegov 1999 | S |
| 15 | **Inclusive $B$ decays**: heavy-quark expansion (OPE in $1/m_b$); shape-function factorization at the endpoint of $B\to X_s\gamma$; local duality | HQE [A] ($R_{\rm PT}$ for coefficients); shape function [A]; duality [C] | heavy-quark chapter | Chay–Georgi–Grinstein 1990; Bigi–Uraltsev–Vainshtein 1992; Manohar–Wise 1994; Neubert 1994; Bigi–Shifman–Uraltsev–Vainshtein 1994; Korchemsky–Sterman 1994 | S |
| 16 | **Lattice and factorization**: local moments (H(4) mixing); LaMET/quasi-PDFs; pseudo-PDFs; "good lattice cross sections"; lattice CS kernel; endpoint-enhanced power corrections | [A] | lattice chapter | Ji 2013; Ma–Qiu 2018; Izubuchi et al. 2018; Radyushkin 2017; Braun–Vladimirov–Zhang 2019 (verify) | S |
| 17 | **Hadron-mass / target-mass corrections**: Georgi–Politzer $\xi$-scaling and its threshold problem; Accardi–Qiu; hadron masses in SIDIS/SIA | [A] / prescription-dependent | Ch5, other collinear processes | Georgi–Politzer 1976; Accardi–Qiu 2008 | S |
| 18 | **Twist-3 collinear factorization for SSAs** and its matching with TMD Sivers at intermediate $q_T$ | SIDIS/DY one-loop [P]; $pp\to\pi X$ [C] | next to the TMD chapter | Qiu–Sterman 1991, 1992, 1999; Ji–Qiu–Vogelsang–Yuan 2006 | S |
| 19 | **Nonperturbative laboratories**: 't Hooft model (exact scaling and parton model); OPE convergence in perturbative $\varphi^4$ | [R] within the models | power-corrections chapter | Callan–Coote–Gross 1976; Einhorn 1976; Hollands–Kopper 2012 | c |
| 20 | **Quark–hadron duality** (Bloom–Gilman; PQW smearing) and its relation to O7 | [C] | Ch4/Ch5 | Poggio–Quinn–Weinberg 1976; Shifman 2000 (verify) | c |
| 21 | **QED/EW within factorization** (photon and lepton PDFs, mixed QCD×QED evolution) | [A] | could be an appendix | Manohar et al. 2016–17 | c |

---------------------------------------------------------------------------------------------------

## 5. Recommended ordering (TOC v1)

Design principles:
- (i) Every tool appears in its simplest setting first. The Sudakov form factor introduces regions, Ward
  identities, Wilson lines, evolution in a rapidity-type variable, and the cusp, with no PDFs in the way.
- (ii) Rigorous ($R_{\rm PT}$) material comes before [A] material, and [A] before [C]/[V].
- (iii) No chapter uses machinery introduced later. In particular SCET comes before jets/NGLs and before the
  Glauber-operator part of the breakdown chapter.
- (iv) Each process class gets a home.

| New # | Title | Content (old chapter → new) | Depends on |
|---|---|---|---|
| **Part I** | **Foundations** | | |
| 1 | Introduction; what is proved | old Ch1 + MA0–MA4 + taxonomy of factorization kinds + master status table + misconception overview | — |
| 2 | Preliminaries | old Ch2 + BRST/ghosts in cut diagrams + $\gamma_5$ + composite-operator renormalization/mixing + Wilson-loop cusp renormalization + Mellin/Carlson/Müntz lemmas (L1–L4) | — |
| 3 | IR structure of Feynman integrals | old Ch3 (Landau/CN, pinch surfaces, power counting, Glauber region, KLN/BN incl. Doria–Frenkel–Taylor, IR safety, method of regions with status) | 2 |
| 4 | **The Sudakov form factor and the IR structure of amplitudes** (new) | one-loop regions; all-order $H\,J\,J\,S$; Ward identities → Wilson lines; $K+G$ evolution; cusp; exponentiation; multi-leg IR poles; Coulomb phases; splitting amplitudes; preview of the spacelike collinear violation | 2, 3 |
| **Part II** | **Rigorous core (OPE)** | | |
| 5 | $e^+e^-$ total cross section | old Ch4 (+ NNLO + Crewther, verified) | 2 |
| 6 | DIS and the OPE | old Ch5 rebuilt per O4–O7 (+ polarized OPE: Bjorken, BC; target mass) | 2, 5 |
| 7 | Operator definitions of PDFs and FFs | old Ch6 + gluon, helicity, transversity definitions + $d$-dim averaging conventions + light-ray ↔ local moments + positivity debate | 2, 6 |
| **Part III** | **Collinear factorization to all orders** | | |
| 8 | General method | old Ch7 (must follow Ch4) | 3, 4, 7 |
| 9 | DIS to all orders | old Ch8 + heavy-quark schemes + nuclear targets | 8 |
| 10 | Other collinear processes (new) | SIA (old Ch9, first half), collinear SIDIS, photoproduction/photon structure, polarized processes, transversity | 8, 9 |
| 11 | Drell–Yan and hadron–hadron collisions | old Ch10 + explicit [A]/[C] split + heavy-quark pairs | 8 |
| 12 | Threshold resummation and refactorization (new) | DY/DIS/Higgs | 4, 9, 11 |
| **Part IV** | **Beyond collinear** | | |
| 13 | TMD factorization | old Ch11 + twist-3 matching (from old Ch16) | 4, 11 |
| 14 | SCET | old Ch14 + Glauber operator + rapidity RG / collinear anomaly | 4, 8, 13 |
| 15 | Jets, event shapes, NGLs, super-leading logs (new) | old Ch9 second half + new | 14 |
| 16 | Small-$x$ and high-energy factorization (new) | from old Ch12 | 4, 13 |
| 17 | Breakdown and non-standard cases | old Ch12 minus small-$x$: TMD breaking, diffraction, spacelike collinear violation, SLLs, Glauber in $E_T$/beam thrust, DPS | 11, 13, 14, 15 |
| **Part V** | **Other hard processes** | | |
| 18 | Hard exclusive processes | old Ch13 | 7, 8 |
| 19 | Heavy-quark physics | $B\to D\pi$, $B\to\pi\pi$ (from old Ch14), inclusive $B$ decays (new), quarkonium (old Ch15) | 14 |
| **Part VI** | **Limits** | | |
| 20 | Power corrections, NLP factorization, renormalons, nonperturbative status | old Ch16 minus lattice + NLP + 't Hooft model | 6, 14 |
| 21 | Lattice QCD and factorization | from old Ch16 + lattice CS kernel | 7, 13 |
| 22 | Summary, master table, open problems | old Ch17 | all |
| App | A–H as in v0, plus I ($\gamma_5$), J (BRST and ghosts in cut diagrams), K (Mellin/Carlson/Müntz lemmas with proofs), L (light-ray ↔ local operator moments, all orders in $\overline{\rm MS}$) | | |

If the book must be trimmed, the **core** is Ch1–14, 17, 20, 22. Give Ch12, 15, 16, 18, 19, 21 at least a
"statement + status + one worked example" format, so that the "各种情况" promise is kept.

---------------------------------------------------------------------------------------------------

## 6. Explicit calculations that best illustrate each theorem

"Verified" means the displayed numbers were reproduced in `checks/` (see §10). Constants that depend on the
$D$-dimensional normalization (e.g. separate real and virtual finite parts in $e^+e^-$) are deliberately not quoted.

| Theorem / concept | Best explicit calculation | What it shows | Status here |
|---|---|---|---|
| Landau equations, Coleman–Norton | one-loop massless vertex (Sudakov triangle): Landau equations in Feynman parameters give the collinear-to-$p_1$, collinear-to-$p_2$ and soft pinch surfaces, with their space-time (CN) picture. Fixed-angle one-loop box: the Glauber/Coulomb pinch and the $i\pi/\epsilon$ phase | pinch vs endpoint; CN; the origin of Glauber | algebraic (writer) |
| Power counting | same vertex: hard ($\lambda^0$), collinear and soft (logarithmic) regions; their overlap gives the $1/\epsilon^2$ | degree $\omega(R)=0$ ⇒ log divergence | algebraic |
| Method of regions | off-shell Sudakov FF ($p_1^2,p_2^2\ll Q^2$): hard + 2 collinear + soft = exact one-loop. On-shell massive FF: pure DR fails, needs an analytic regulator | Euclidean-like success vs Minkowski subtleties | standard (Smirnov) |
| Sudakov evolution | one-loop $\ln F=\frac{\alpha_sC_F}{4\pi}\big(\frac{\mu^2}{Q^2}\big)^\epsilon\big(-\frac{2}{\epsilon^2}-\frac3\epsilon+\dots\big)$ gives $K=\frac{\alpha_sC_F}{4\pi}\frac4\epsilon$ and $G=\frac{\alpha_sC_F}{2\pi}\big(3+2\ln\frac{\mu^2}{Q^2}\big)$, with $\mu\frac{dG}{d\mu}=-\mu\frac{dK}{d\mu}=\gamma_K=\frac{2C_F\alpha_s}{\pi}$ | $K+G$ structure; cusp | **verified** (`c7`; pole and log terms only) |
| $e^+e^-$ total, IR finiteness | $O(\alpha_s)$ via ${\rm Im}$ of the two-loop $\Pi$, *and* via cut diagrams (real + virtual in DR). Sum $=\frac{3}{2}\frac{C_F\alpha_s}{2\pi}=\frac{\alpha_s}{\pi}$ | KLN at work; analytic continuation | standard; NNLO + Crewther **verified** (`c4`) |
| IR-safe event shape | $O(\alpha_s)$ thrust: $\frac{1}{\sigma_0}\frac{d\sigma}{d\tau}=\frac{C_F\alpha_s}{2\pi}\big[-4\big(\frac{\ln\tau}{\tau}\big)_+-3\big(\frac1\tau\big)_++\big(\frac{\pi^2}{3}-1\big)\delta(\tau)\big]+$ nonsingular; cumulant $1+\frac{C_F\alpha_s}{2\pi}\big[-2\ln^2\tau-3\ln\tau+\frac{\pi^2}{3}-1\big]+O(\tau\ln\tau)$ | IR safety; Sudakov logs; the target of SCET $H\,J\otimes J\otimes S$ | **verified** (`c3`, 20 digits) |
| Euclidean OPE in PT | free-field plus one-loop OPE of $j^\mu j^\nu$; LO gluon-condensate coefficient (SVZ) | condensates; no $1/Q^2$ term | standard |
| DIS moments, anomalous dimensions | $\int_0^1 z^{n-1}P_{qq}=C_F\big[\frac32+\frac{1}{n(n+1)}-2S_1(n)\big]$; $n=1$ gives 0 (number), $n=2$ momentum sum rule for both columns | OPE ↔ DGLAP | **verified** (`c1`) |
| One-loop coefficient moments | $C^{q,(1)}_{2,n}=C_F\big[2S_1^2-2S_2+3S_1-\frac{2S_1}{n(n+1)}+\frac3n+\frac{4}{n+1}+\frac{2}{n^2}-9\big]$ (units $\alpha_s/4\pi$, $S_k\equiv S_k(n)$); vanishes at $n=1$ (Adler) | moment-space factorization | **verified** (`c2`; a common misquoted variant fails the $n=1$ check) |
| PDF from the operator | one-loop $f_{q/q}$ in Feynman gauge with the Wilson line: quark-ladder graph $\propto(1-\epsilon)(1-z)$; two Wilson-line graphs $\propto 2z/(1-z)$; Wilson-line self-energy $\propto n^2=0$; virtual graphs produce the plus prescription: $P_{qq}=C_F\big[\frac{1+z^2}{1-z}\big]_+=C_F\big[\frac{1+z^2}{(1-z)_+}+\frac32\delta(1-z)\big]$ | Wilson lines are needed; UV/IR bookkeeping (C14) | identity **verified** (`c1`) |
| DIS one loop | $\gamma^*q\to q(g)$, $\gamma^*g\to q\bar q$ in DR ⇒ ($F_2/x$, units $\alpha_s/2\pi$) $C_q=C_F[2\mathcal D_1-\tfrac32\mathcal D_0-(1+z)\ln(1-z)-\tfrac{1+z^2}{1-z}\ln z+3+2z-(\tfrac92+\tfrac{\pi^2}{3})\delta(1-z)]$ and $C_g=T_R[(z^2+(1-z)^2)\ln\tfrac{1-z}{z}-8z^2+8z-1]$ per $q$ or $\bar q$. $F_L$: $C_L^q=2C_Fz$, $C_L^g=4T_Rz(1-z)$ per $q$ or $\bar q$, finite with no subtraction (Altarelli–Martinelli) | collinear subtraction; scheme | $C_q$, $C_g$ **verified** by cross-consistency (`c2`); $C_L$ standard |
| DY one loop | $\overline{\rm MS}$, $\mu=Q$: $\Delta_{q\bar q}=C_F[4(1+z^2)\mathcal D_1-2\tfrac{1+z^2}{1-z}\ln z+(\tfrac{2\pi^2}{3}-8)\delta(1-z)]$, $\Delta_{qg}=T_R[(z^2+(1-z)^2)\ln\tfrac{(1-z)^2}{z}+\tfrac12+3z-\tfrac72z^2]$. DIS scheme: $C_F[2(1+z^2)\mathcal D_1+3\mathcal D_0-6-4z+(1+\tfrac{4\pi^2}{3})\delta(1-z)]$ and $T_R[(z^2+(1-z)^2)\ln(1-z)+\tfrac32-5z+\tfrac92z^2]$. ($g(z)\mathcal D_k$ means $\int(g h-g(1)h(1))\ln^k(1-z)/(1-z)$.) | universality of PDFs between DIS and DY; the "$\pi^2$" from the timelike form factor | **verified**: $\Delta^{\overline{\rm MS}}-2C_q=\Delta^{\rm DIS}$ and $\Delta^{\overline{\rm MS}}_{qg}-C_g=\Delta^{\rm DIS}_{qg}$ to $10^{-30}$ (`c2`) |
| Glauber cancellation (DY) | abelian/Yukawa model: one soft exchange between spectators. The sum over final-state cuts cancels the phase; the cancellation fails if the spectator final state is constrained (gap) | why inclusivity matters | algebraic (writer) |
| TMD factorization | one-loop TMD PDF with Collins' rapidity regulator; one-loop soft factor; $\tilde K(b_T;\mu)=-\frac{\alpha_sC_F}{\pi}\ln\frac{\mu^2b_T^2}{b_0^2}$, $\frac{d\tilde K}{d\ln\mu}=-\gamma_K$; small-$b$ matching coefficient | CS evolution; rapidity divergences | $\tilde K$ **verified** (`c7`) |
| Sivers sign reversal | scalar-diquark model (Brodsky–Hwang–Schmidt 2002): one-gluon final-state vs initial-state interaction gives opposite signs | staple direction | standard |
| TMD breaking | Collins–Qiu abelian model; Rogers–Mulders colour entanglement at two-gluon exchange | [V] mechanism | standard |
| Threshold | large-$N$: $\langle\mathcal D_0,z^{N-1}\rangle=-S_1(N-1)\to-\ln\bar N$, $\langle\mathcal D_1,z^{N-1}\rangle=\tfrac12[S_1(N-1)^2+S_2(N-1)]\to\tfrac12(\ln^2\bar N+\zeta_2)$, $\ln\bar N=\ln N+\gamma_E$. Exponent with $A^{(1)}=C_F\alpha_s/\pi$ reproduces the $8C_F\mathcal D_1$ of $\Delta_{q\bar q}$ | refactorization ↔ fixed order | **verified** (`c6`) |
| SCET, thrust | one-loop $H$, $J$, $S$; RG consistency (anomalous dimensions sum to zero); reproduces the singular thrust terms above | EFT proof structure | target **verified**; factor pieces to be done by the writer |
| Ultrasoft decoupling | tree-level demonstration that $\xi_n=Y_n\xi_n^{(0)}$, $A_n=Y_nA_n^{(0)}Y_n^\dagger$ removes $n\cdot A_{us}$ from $\mathcal L_n^{(0)}$ | LO decoupling | algebraic |
| Polarized OPE | Bjorken: $\int(g_1^p-g_1^n)=\frac{g_A}{6}[1-a-(\frac{55}{12}-\frac{n_f}{3})a^2+O(a^3)]$; Crewther: $C_{\rm Bjp}D_{\rm NS}=1+(\tfrac78-\zeta_3)\beta_0a^2+\dots$, i.e. $K_1=C_F(-\tfrac{21}{8}+3\zeta_3)$. Also the first moment of $g_1$ from the $\gamma^*g$ box with HVBM vs anticommuting $\gamma_5$ (scheme dependence) | conformal symmetry; anomaly | Bjorken/Crewther **verified** (`c4`) |
| Heavy quarks | LO $\gamma^*g\to Q\bar Q$ with full mass dependence; its $m\to0$ limit gives $\ln(Q^2/m^2)P_{qg}$, the ACOT subtraction | VFNS construction | standard |
| Exclusive | LO pion FF hard kernel; asymptotic $Q^2F_\pi\to8\pi\alpha_sf_\pi^2$ ($f_\pi\simeq131$ MeV); $Q^2F_{\gamma^*\gamma\pi}\to\sqrt2 f_\pi$ | DA factorization | standard, **not re-derived** |
| NRQCD | LO $\eta_c\to\gamma\gamma$ matching; summary of the Nayak–Qiu–Sterman NNLO IR pole requiring gauge completion | decay vs production | standard |
| Renormalons | large-$\beta_0$ Adler function: no IR pole at $u=1$, first at $u=2$ | IR renormalon ↔ OPE | standard |
| LaMET | one-loop quasi-PDF matching (Xiong–Ji–Zhang–Zhao 2014) | lattice factorization | standard |
| DPS | LO double DY with the $1\to2$ splitting DPDF ($\propto1/y^2$) and its overlap with an SPS loop | double counting | standard |
| x-space vs moments | $R(x)=\sin(Q^2x)$: $Q^2\times$moments bounded, $\sup|R|=1$; $\delta'(x)$: all even moments zero | lemmas L3, L2 | **verified** (`c5`) |
| Target mass | contraction of the CONTEXT $W^{\mu\nu}$ with $\epsilon_L$: $2xW_L=(1+\frac{4M^2x^2}{Q^2})F_2-2xF_1$ | correct $F_L$ definition | **verified** (`c7`) |

---------------------------------------------------------------------------------------------------

## 7. Common misconceptions to address explicitly (28)

Format: **misconception** → correction (placement in TOC v1).

1. **"Factorization has been proven for all standard hard processes."** → Rigorous ($R_{\rm PT}$) results exist only
   for OPE-accessible quantities ($\sigma_{\rm tot}(e^+e^-)$, DIS moments). DIS (x-space), SIA, SIDIS, DY and
   colourless final states are [A]. $pp\to$ jets/hadrons is [C]. Several cases are [V]. (Ch1 master table.)
2. **"PDFs are probability densities, so $\overline{\rm MS}$ PDFs are positive."** → The number-density reading holds
   only for bare PDFs in light-cone gauge, which are UV divergent. Renormalized PDFs are scheme-dependent and
   need not be positive. Positivity in $\overline{\rm MS}$ is debated [C] (Candido–Forte–Hekhorn 2020 vs
   Collins–Rogers–Sato 2022). (Ch7.)
3. **"Factorization is just the OPE."** → The OPE covers only cross sections given by a forward matrix element of
   a current product summed over all final states (inclusive DIS, $e^+e^-$ total). Drell–Yan involves a
   two-hadron initial state and is **not** an OPE; its proof is diagrammatic and has a Glauber problem with no
   OPE analogue. (Ch6, Ch11.)
4. **"Moment factorization implies x-space factorization with a uniform $O(\Lambda^2/Q^2)$ error."** → Moments
   $O(1/Q^2)$ for each $n$ do not give a pointwise bound (counterexample $\sin(Q^2x)$). Power corrections grow
   with $n$, i.e. as $x\to1$. The resonance region needs smearing (duality). (Ch6, Ch9.)
5. **"Even moments always determine the structure function."** → They do for measures and $L^1$ functions. For
   distributions they fail at $x=0$ ($\delta'(x)$ has vanishing even moments). Twist-3 distributions can carry
   $\delta(x)$ terms, and sum rules such as Burkhardt–Cottingham can be affected. (Ch6, App K.)
6. **"The anomalous dimensions fix the x-space kernel uniquely."** → Only after choosing the analytic continuation
   (Carlson). Continuations from even and from odd $n$ differ, which is why $P_{\rm NS}^\pm$ differ at NLO.
   (Ch6, Ch7.)
7. **"Glauber gluons cancel in every inclusive cross section."** → The cancellation needs a sum over unobserved
   spectator final states, and an observable that does not obstruct the contour deformation. It fails for TMD
   $pp\to h_1h_2X$, for hadron–hadron diffraction (gap survival), and (argued) for $E_T$/beam thrust; it is
   unproven for $pp\to$ jets. (Ch11, Ch17.)
8. **"The KLN theorem explains why hadron-collider cross sections are finite."** → Initial-state collinear
   singularities do **not** cancel. They are absorbed into PDFs. KLN with initial-state degeneracy sums is
   unphysical for hadron beams and is subtle even formally (disconnected/forward contributions; verify
   Frye–Hannesdottir–Paul–Schwartz–Yan 2019). Bloch–Nordsieck fails in non-abelian theories with coloured
   initial states at two loops (Doria–Frenkel–Taylor 1980; Di'Lieto–Gendron–Halliday–Sachrajda 1981). For DY
   the failure is believed to be power suppressed (verify the exact statement). (Ch3.)
9. **"IR safety guarantees factorization and perturbative control."** → IR safety handles final-state
   singularities only. Initial-state hadrons still need factorization. IR-safe observables can have NGLs,
   super-leading logarithms, Glauber sensitivity, and $O(\Lambda/Q)$ hadronization corrections. (Ch3, Ch15.)
10. **"Power corrections are always $O(\Lambda^2/Q^2)$."** → Event shapes have $O(\Lambda/Q)$ corrections; jet
    observables have $\sim\Lambda/(RQ)$; some spin observables (twist-3) are $O(M/Q)$; corrections are enhanced at
    large $x$, at small $x$, and in nuclei ($A^{1/3}$). Even the DY $1/Q^2$ is [C]. (Ch20.)
11. **"Light-cone gauge removes all Wilson lines, so PDFs are 'just' parton-number operators."** → Transverse
    gauge links at light-cone infinity remain (Ji–Yuan 2002; Belitsky–Ji–Yuan 2003). Spurious $1/k^+$ poles need
    prescriptions. T-odd TMDs exist precisely because of these links. (Ch7, Ch13.)
12. **"Time-reversal invariance forbids the Sivers function."** → This was the original argument (Collins 1993).
    It is wrong because T exchanges future- and past-pointing Wilson lines. The correct consequence is the sign
    reversal SIDIS ↔ DY (Collins 2002, after Brodsky–Hwang–Schmidt 2002). (Ch13.)
13. **"The Collins fragmentation function changes sign between processes, like Sivers."** → T-odd fragmentation
    functions are universal between SIDIS and $e^+e^-$ (Collins–Metz 2004; Meissner–Metz 2009). (Ch13.)
14. **"$\int d^2k_T\,f(x,k_T;\mu,\zeta)=f(x;\mu)$."** → False beyond tree level for renormalized TMDs. The
    $k_T$ integral is UV divergent and $\zeta$-dependent. The correct relation is the small-$b_T$ OPE, or
    cutoff-dependent relations (Ebert–Michel–Stewart–Sun 2022, verify). (Ch13.)
15. **"The soft factor always cancels / equals 1."** → It equals 1 only in collinear-inclusive cross sections. In
    TMD factorization it is essential and is absorbed (as a square root) into the TMDs. (Ch11, Ch13.)
16. **"Rapidity divergences are an artifact of a bad regulator."** → They signal a genuine additional factorization
    variable ($\zeta$ or $\nu$), with evolution governed by the CS kernel. Different regulators give different
    individual pieces; properly combined objects agree. (Ch4, Ch13, Ch14.)
17. **"The Collins–Soper kernel is perturbative."** → Only for $b_T\ll1/\Lambda$. At large $b_T$ it is
    nonperturbative. It is a lattice target, and $b_*$ prescriptions are conventions, not part of the theorem.
    (Ch13, Ch21.)
18. **"SCET proves factorization independently of region analysis."** → SCET assumes the mode content (that is the
    region analysis), needs zero-bin subtractions, and must treat Glauber modes. Its all-order statements are
    [A], like the diagrammatic ones. (Ch14.)
19. **"The method of regions is a theorem."** → Yes for Euclidean large-momentum/mass limits; no general proof for
    Minkowskian limits. It may need analytic regulators. (Ch3.)
20. **"Landau equations give the singularities."** → They give *necessary* conditions. Solutions can be harmless
    (numerator suppression, integrable). Endpoint and second-type singularities need separate care. (Ch3.)
21. **"Strict collinear factorization violation (Catani–de Florian–Rodrigo) shows that PDF factorization fails."**
    → It is an amplitude-level statement about spacelike multi-parton collinear limits. Its consequences for
    inclusive cross sections cancel in many cases; DY collinear factorization stays [A]. (Ch4, Ch17.)
22. **"Leading-power factorization extends straightforwardly to subleading power."** → At NLP, endpoint divergences
    appear in convolutions ($B\to\pi\pi$ annihilation, $H\to\gamma\gamma$ via light-quark loops, DY threshold at
    NLP). They require refactorization (Liu–Neubert). Higher-power DY factorization is expected to fail (DFT-type
    effects). (Ch20.)
23. **"Spacelike and timelike splitting functions are the same."** → Equal at LO (Gribov–Lipatov relation). They
    differ beyond LO in $\overline{\rm MS}$. (Ch10.)
24. **"In dimensional regularization the PDF of a quark in a quark is $\delta(1-x)$, so nothing happens."** → True
    for the bare PDF. The renormalized partonic PDF consists of IR poles, because the UV counterterm is
    re-labelled as IR. Mishandling this is the classic source of sign errors in collinear subtractions. (Ch7.)
25. **"Varying $\mu_R,\mu_F$ by a factor 2 gives the theory error."** → This is a convention with no theorem
    behind it. Factorization guarantees only that the residual scale dependence is of higher order. (Ch9, Ch11.)
26. **"Callan–Gross ($F_L=0$) and Lam–Tung are QCD theorems."** → They are parton-model or LO results. $F_L=O(\alpha_s)$
    (Altarelli–Martinelli). Lam–Tung holds at $O(\alpha_s)$ but is violated at $O(\alpha_s^2)$ and by Boer–Mulders
    (nonperturbative) effects. (Ch9, Ch13.)
27. **"The perturbative $R(s)$ is valid pointwise in $s$."** → Only in the Euclidean region, or after smearing
    (Poggio–Quinn–Weinberg). Near thresholds and resonances it is meaningless pointwise. (Ch5.)
28. **"[R] means mathematically proven for real-world QCD."** → QCD itself has not been constructed as a
    mathematical QFT. [R] in this book always means "at every order of renormalized PT, for IR-regulated
    partonic Green functions" ($R_{\rm PT}$), or "an algebraic consequence of the definitions" ($R_{\rm def}$).
    (Ch1 legend.)

Further candidates if space allows:
- "Diffractive PDFs are universal across all processes" (only in DDIS).
- "Gottfried sum rule $=1/3$ is a QCD prediction" (it assumes $\bar u=\bar d$; violated by NMC).
- "The Adler sum rule receives QCD corrections" (it does not: current algebra, given an unsubtracted dispersion
  relation, MA3).
- "Inclusive DIS has transverse single-target-spin asymmetries from FSI" (zero at one-photon exchange by T
  invariance; Christ–Lee 1966).
- "Lattice computes PDFs directly" (it needs LaMET/SDF matching with endpoint-enhanced power corrections).

---------------------------------------------------------------------------------------------------

## 8. Backbone theorem statements (30) with recommended rigor tags

Each statement lists hypotheses, the statement, a proof route, and its nonperturbative status ("NP").
$R_{\rm PT}$ / $R_{\rm def}$ are the two sub-kinds of [R] (O2). MA0–MA4 are defined in §3.1.

**B1 (Landau conditions; Coleman–Norton) — [R].**
*Setting:* a connected, UV-regularized Feynman integral $I(p)=\int\prod_l d^Dk_l\,N/\prod_i(q_i^2-m_i^2+i0)$ with
$q_i=\sum_l\eta_{il}k_l+\sum_e\sigma_{ie}p_e$, at real external momenta $p$.
*Statement:* (a) $I$ can fail to be analytic at $p$ only if there exist $\alpha_i\ge0$ (not all zero) and loop
momenta such that, for every line, $\alpha_i(q_i^2-m_i^2)=0$, and for every loop $l$,
$\sum_{i\in l}\alpha_i\eta_{il}q_i^\mu=0$. Otherwise the singularity is of second type (infinite $k$).
(b) Real solutions with $\alpha_i\ge0$ are equivalent to classical space-time processes: vertices $x_v$ with
$x_{v'}-x_v=\alpha_iq_i$ along each on-shell line $i$, with momentum conservation at the vertices.
*Proof:* local contour deformation $k\to k-i\kappa$ with $\kappa\cdot\partial D/\partial k>0$ wherever $D=0$, unless
pinched; the boundaries $\alpha_i=0$ give reduced diagrams; (b) is algebraic.
*Caveats:* necessary, not sufficient. IR divergences at fixed $p$ in massless theories are analysed through pinch
surfaces in loop-momentum space (Sterman 1978).
*Refs:* Landau 1959; Coleman–Norton 1965; Eden–Landshoff–Olive–Polkinghorne 1966; Collins 2011 ch. 5.

**B2 (pinch-surface power counting and leading regions; $e^+e^-$, DIS, SIA, DY in Feynman gauge) — [A].**
*Statement:* every pinch surface $R$ of the (cut) amplitude has superficial degree $\omega(R)\ge0$. The surfaces
with $\omega=0$ are exactly those with:
- one hard subgraph $H$ (virtualities $O(Q^2)$);
- one jet subgraph per collinear direction, attached to $H$ by one physical parton (a quark or a transversely
  polarized gluon) plus any number of scalar-polarized collinear gluons;
- a soft subgraph attached only to jets, and only by gluons (soft-quark attachments are power suppressed);
- for DY, also Glauber subregions of spectator–spectator soft exchanges.

*Proof:* Sterman 1978; Libby–Sterman 1978; Collins 2011 ch. 5. The degree formula is [R]. That it controls the
actual contribution (nested regions, numerator suppression, Glauber) is [A].
*NP:* MA1.

**B3 (cancellation theorems) — mixed.** (a) [$R_{\rm PT}$, regulated theory] KLN: rates summed over all
degenerate initial *and* final states are IR finite at each order (Kinoshita 1962; Lee–Nauenberg 1964), with
caveats about disconnected/forward contributions (verify Frye et al. 2019). (b) [R] Bloch–Nordsieck in QED.
(c) [V] Bloch–Nordsieck for coloured initial states in non-abelian theories fails at two loops
(Doria–Frenkel–Taylor 1980; Di'Lieto–Gendron–Halliday–Sachrajda 1981). The non-cancelling terms are
power suppressed for DY at large $Q$ (verify).

**B4 ($e^+e^-$ total cross section) — [$R_{\rm PT}$].** *Setting:* massless QCD with $n_f$ flavours, one-photon
exchange. *Statement:* at every order $R(s)=\sigma(e^+e^-\to{\rm hadrons})/\sigma_{\mu\mu}$ is UV and IR finite, and
$R=N_c\sum e_q^2[1+a+(\frac{365}{24}-11\zeta_3-n_f(\frac{11}{12}-\frac23\zeta_3))a^2+O(a^3)]$ with
$a=\alpha_s(\sqrt s)/\pi$ in $\overline{\rm MS}$ (verified). *Proof:* (i) Euclidean IR finiteness of $\Pi(q^2)$;
(ii) RG ⇒ polynomial in $\ln(-q^2/\mu^2)$; (iii) $R=12\pi\,{\rm Im}\,\Pi(s+i0)$. Alternative: Sterman's cut-diagram
proof. *NP:* valid for hadrons only after smearing (PQW) and under MA0 + nonperturbative OPE [C]. Duality
violations [C].

**B5 (Euclidean OPE) — [$R_{\rm PT}$].** *Statement:* for gauge-invariant local operators $A,B$ and Green functions
with IR-regulated external legs at non-exceptional Euclidean momenta,
$\int d^4x\,e^{iq\cdot x}T\,A(x)B(0)=\sum_{\dim O\le N}C_O(q;\mu)[O](0)+R_N$. Here $R_N$ is suppressed by
$|q|^{-(N+1-\dim A-\dim B+4)}$ (up to logarithms) at each order. The sum includes gauge-variant BRST-exact and
EOM-vanishing operators, whose physical matrix elements vanish. *Refs:* Wilson 1969; Zimmermann 1970/73;
Joglekar–Lee 1976; Kluberg-Stern–Zuber 1975; Collins, *Renormalization* (1984). Convergence at finite distance in
perturbative $\varphi^4$: Hollands–Kopper 2012. *NP:* nonperturbative validity [C], MA0, MA4.

**B6 (twist-2 moments of DIS structure functions) — [$R_{\rm PT}$].** *Statement:* for e.m. unpolarized DIS and
each even $n\ge2$ (subject to MA3 for convergence),
$$\int_0^1dx\,x^{n-2}F_2(x,Q^2)=\sum_{i=q,\bar q,g}C^{i}_{2,n}\Big(\frac{Q^2}{\mu^2},\alpha_s(\mu)\Big)\,A^{i}_n(\mu)+O\Big(\frac{\Lambda^2}{Q^2}\Big),\qquad
A^i_n(\mu)=\int_0^1d\xi\,\xi^{n-1}f_i(\xi;\mu),$$
with $\mu\,dA_n/d\mu$ given by the anomalous-dimension matrix (B9) and
$C^{q,(1)}_{2,n}=C_F[2S_1^2-2S_2+3S_1-\frac{2S_1}{n(n+1)}+\frac3n+\frac4{n+1}+\frac2{n^2}-9]\cdot\frac{\alpha_s}{4\pi}e_q^2$
(verified). Analogous statements: $F_1$ (even $n$), $F_3$ (odd $n$), $g_1$ (odd $n$). The $O(\Lambda^2/Q^2)$
contains twist-4 and target-mass terms; its coefficient grows with $n$. *Proof:* B5 applied to the Taylor
coefficients of $T(\omega,Q^2)$ at $\omega=0$; analyticity in $\omega$; contour argument. *NP:* MA0, MA3, MA4 +
nonperturbative OPE.

**B7 (Mellin lemmas L1–L4) — [R] (mathematics).**
- L1: a finite signed Borel measure on $[0,1]$ whose even moments all vanish is zero. Proof: push forward under
  $x\mapsto x^2$, then Weierstrass.
- L2: L1 fails for distributions supported at $x=0$ ($\delta'$). A compactly supported distribution all of whose
  integer moments vanish is zero (its Fourier transform is entire).
- L3: there exist $R_Q\in C[0,1]$ with $\sup|R_Q|=1$ and $|\int x^nR_Q\,dx|\le c_n/Q^2$ for every $n$, e.g.
  $R_Q=\sin(Q^2x)$ (verified).
- L4 (Carlson): if $f$ is holomorphic of exponential type for ${\rm Re}\,n\ge0$, $|f(iy)|\le Ce^{c|y|}$ with $c<\pi$,
  and $f$ vanishes on $\mathbb N$, then $f\equiv0$. From even integers alone one needs $c<\pi/2$; counterexample
  $(1-\cos\pi n)/2$.

**B8 (properties of operator-defined PDFs) — [$R_{\rm def}$], (d)–(f) also [$R_{\rm PT}$].** With the CONTEXT definition:
- (a) Gauge invariance ($W\to U(b)WU^\dagger(a)$).
- (b) Support $-1\le\xi\le1$ (spectral condition $p_X^+\ge0$), preserved by $\overline{\rm MS}$ renormalization.
- (c) $f_{\bar q}(\xi)=-f_q(-\xi)$ (charge conjugation).
- (d) For $n\ge1$: $\int_{-1}^1d\xi\,\xi^{n-1}f_q(\xi;\mu)=\langle P|[\bar\psi\gamma^+(iD^+)^{n-1}\psi]_\mu|P\rangle/(2(P^+)^n)$,
  up to the symmetrization and trace terms irrelevant for the $+\cdots+$ component. This follows from the
  CONTEXT definition with $D=\partial-igA$ and translation invariance; for renormalized operators in
  $\overline{\rm MS}$ it holds at all orders.
- (e) $\int_0^1(q-\bar q)\,d\xi=N_q$ (conserved current, not renormalized).
- (f) $\sum_i\int_0^1\xi f_i(\xi;\mu)\,d\xi=1$ exactly in $\overline{\rm MS}$ (conservation and finiteness of the total
  $T^{++}$).
- (g) Gluon: $f_g(\xi)=\int\frac{dw^-}{2\pi\xi P^+}e^{-i\xi P^+w^-}\langle P|F_a^{+j}(w)W_{ab}[w,0]F_b^{+j}(0)|P\rangle$, summed
  over $j$ and averaged over $2-2\epsilon$ polarizations; a free gluon gives $\delta(1-\xi)$ (checked by hand).

Positivity is **not** a theorem ([C], debated).

**B9 (DGLAP from renormalization) — [$R_{\rm PT}$].** $f^{\rm bare}_i=\sum_jZ_{ij}\otimes f_j(\mu)$ with
$\overline{\rm MS}$ pure-pole $Z$ ⇒ $\partial f_i/\partial\ln\mu^2=\frac{\alpha_s}{2\pi}\sum_jP_{ij}\otimes f_j$, with finite
$P_{ij}$ order by order. At LO:
- $P_{qq}=C_F[\frac{1+z^2}{1-z}]_+$
- $P_{qg}=T_R[z^2+(1-z)^2]$
- $P_{gq}=C_F\frac{1+(1-z)^2}{z}$
- $P_{gg}=2C_A[\frac{z}{(1-z)_+}+\frac{1-z}{z}+z(1-z)]+\delta(1-z)\frac{11C_A-4n_fT_R}{6}$

Moments obey the $n=1$ and $n=2$ sum rules (verified). *Proof:* local-operator renormalization + B8(d) + B7(L4),
specifying the even/odd continuation, or directly from the light-ray operator. *NP:* MA0.

**B10 (DIS collinear factorization in x-space) — [A]; its twist-2 part is equivalent to B6 in the sense of
distributions [$R_{\rm PT}$].** *Statement:* for fixed $0<x<1$ with $W^2\gg\Lambda^2$, as $Q\to\infty$,
$$\frac{F_2(x,Q^2)}{x}=\sum_i\int_x^1\frac{d\xi}{\xi}\,C_{2,i}\Big(\frac{x}{\xi},\frac{Q}{\mu},\alpha_s(\mu)\Big)f_{i/H}(\xi;\mu)+R(x,Q),$$
with $C_{2,q}=e_q^2[\delta(1-z)+\frac{\alpha_s}{2\pi}C_q(z)+\dots]$ and $C_{2,g}=\sum_{q,\bar q}e_q^2\frac{\alpha_s}{2\pi}C_g(z)+\dots$
(one loop verified, §6), and $R=O(\Lambda^2/Q^2)$ with an $x$-dependent coefficient that is non-uniform as
$x\to1$ and $x\to0$. *Proof:* Collins 2011 ch. 8–10 (regions; Ward identities; subtractions; sum over final-state
cuts by unitarity); CSS 1989. *NP:* MA1, MA2; smoothness (L3).

**B11 (SIA and collinear SIDIS) — [A].**
- $e^+e^-\to hX$: $\frac{d\sigma^h}{dz}=\sum_i\int_z^1\frac{dz'}{z'}\,d\hat\sigma_i(z/z',Q/\mu,\alpha_s)\,d_{h/i}(z';\mu)+$ power corrections
  (their size is [C]).
- SIDIS ($P_{hT}$ integrated, or $P_{hT}\sim Q$): $d\sigma=\sum_{ij}f_{i/H}\otimes d\hat\sigma_{ij}\otimes d_{h/j}+\dots$

The FF definition is Collins–Soper 1982, including the $d$-dimensional normalization factor (CONTEXT must fix
it; see §9). *Refs:* Collins–Soper 1982; Collins 2011 ch. 12–13.

**B12 (Drell–Yan and colourless final states) — [A].** *Statement:* as $s\to\infty$ with $\tau=Q^2/s$ and $y$ fixed,
$$\frac{d\sigma}{dQ^2dy}=\sum_{ij}\int d\xi_ad\xi_b\,f_{i/A}(\xi_a;\mu)f_{j/B}(\xi_b;\mu)\,\frac{d\hat\sigma_{ij}}{dQ^2dy}(\xi_a,\xi_b,Q,y;\mu)+R,$$
with $R$ power suppressed. The power is [C] (expected $\Lambda^2/Q^2$). The same holds for $W$, $Z$, $H$ and other
colourless final states. *Proof ingredients:* leading regions including Glauber; contour deformation out of the
Glauber region after summing spectator cuts; Ward identities → Wilson lines; soft factor → 1 by unitarity;
subtractions (Bodwin 1985; CSS 1985, 1988; Collins 2011 ch. 14). The *Gaps* box must list: completeness of the
non-abelian all-order Glauber argument; the Glauber–collinear overlap; nested regions. One-loop check verified
(§6). *NP:* MA1, MA2.

**B13 (hadron–hadron collisions with coloured final states) — [C].** The factorized form for $pp\to{\rm jet}\,X$,
$pp\to hX$ (large $p_T$) and dijets is universally used but not proven. Obstructions: final-state Glauber
interactions, the spacelike collinear violation, super-leading logarithms in non-global and gap observables.
Heavy-quark pairs: CSS 1986, [A] if the refs agent confirms, otherwise [C].

**B14 (factorization with heavy quarks; Collins 1998) — [A].** Keeping heavy-quark masses in the hard part, with
heavy-quark PDFs defined in the CWZ/ACOT framework, $\sigma=\sum_if_i\otimes\hat C_i(m_h/Q,Q/\mu)$ with error power
suppressed in $\Lambda/Q$, uniformly in $m_h/Q$ (verify wording). Schemes FFNS/ZM-VFNS/S-ACOT/FONLL are choices
within this theorem.

**B15 (Sudakov form factor) — [A]; one-loop check [R].** For the massless on-shell quark form factor in DR:
$\frac{\partial\ln F}{\partial\ln Q^2}=\frac12[K(\epsilon,\alpha_s(\mu))+G(Q^2/\mu^2,\alpha_s(\mu),\epsilon)]$, with
$\mu\frac{dK}{d\mu}=-\gamma_K=-\mu\frac{dG}{d\mu}$, $K$ a pure counterterm series, and $G$ finite as $\epsilon\to0$.
Hence $F$ exponentiates, with double logarithms controlled by $\gamma_K=2C_F\alpha_s/\pi+O(\alpha_s^2)$ (one loop
verified). Factorized form $F=H\cdot J\cdot J/S$ (or with Collins' rapidity variables). *Refs:* Mueller 1979;
Collins 1980, 1989; Sen 1981; Korchemsky 1989; Magnea–Sterman 1990.

**B16 (IR structure of massless multi-leg amplitudes) — [R] at the orders computed explicitly; [A] for the all-order
structure; [V] for strict collinear factorization in spacelike configurations.** The statement:
- $|\mathcal M(\{p\},\epsilon)\rangle=\mathbf Z(\{p\},\mu,\epsilon)\,|\mathcal M_{\rm fin}(\{p\},\mu)\rangle$, with $\mathbf Z$ fixed by a colour-space
  anomalous-dimension matrix.
- That matrix consists of dipole terms $\propto\gamma_{\rm cusp}\,\mathbf T_i\!\cdot\!\mathbf T_j\ln(\mu^2/(-s_{ij}))$, plus
  single-particle collinear terms, plus, starting at three loops, terms depending on conformal cross ratios
  (Almelid–Duhr–Gardi 2016).
- The $i\pi$ (Coulomb) terms differ between spacelike and timelike invariants. They cause the breakdown of strict
  collinear factorization of spacelike splitting amplitudes (Catani–de Florian–Rodrigo 2012).

The writer should take the exact normalization of the sum over pairs from Becher–Neubert 2009. *Refs:* Catani
1998; Sterman–Tejeda-Yeomans 2003; Becher–Neubert 2009; Gardi–Magnea 2009.

**B17 (ultrasoft decoupling in SCET$_{\rm I}$) — [R] as a statement about the LO SCET Lagrangian; [A] as a
statement about QCD.** The field redefinitions $\xi_n=Y_n\xi_n^{(0)}$ and $A_n=Y_nA_n^{(0)}Y_n^\dagger$, with
$Y_n$ an ultrasoft Wilson line along $n$, remove all ultrasoft couplings from $\mathcal L_n^{(0)}$ at leading power,
to all orders in $\alpha_s$. Ultrasoft interactions move into Wilson lines in the operators (Bauer–Pirjol–Stewart
2002). The QCD statement requires SCET to reproduce the IR of QCD (mode completeness, zero-bin, Glauber).

**B18 (thrust / dijet factorization) — [A]; one-loop singular terms [R] (verified).** For $\tau\ll1$, at leading
power,
$\frac{1}{\sigma_0}\frac{d\sigma}{d\tau}=H(Q^2,\mu)\int dp_a^2\,dp_b^2\,dk\,J(p_a^2,\mu)J(p_b^2,\mu)S_\tau(k,\mu)\,\delta\big(\tau-\frac{p_a^2+p_b^2}{Q^2}-\frac kQ\big)+$ (non-singular).
The anomalous dimensions are consistent ($\mu$-independence in Laplace space). At $O(\alpha_s)$ this reproduces
$\frac{C_F\alpha_s}{2\pi}[-4(\frac{\ln\tau}{\tau})_+-3(\frac1\tau)_++(\frac{\pi^2}{3}-1)\delta(\tau)]$.
*Refs:* Korchemsky–Sterman 1999 (verify); Schwartz 2008; Becher–Schwartz 2008. *NP:* the leading hadronization
effect shifts the distribution by $\delta\tau\propto\Lambda/Q$ (relative effect $\propto\Lambda/(Q\tau)$ in the tail) [C].

**B19 (threshold refactorization and resummation for DY) — [A].** As $z=Q^2/\hat s\to1$, at leading power in
$1-z$, $\hat\sigma_{q\bar q}=H(Q,\mu)\,Q\,S_{\rm DY}(Q(1-z),\mu)$ (distributions $\delta,\mathcal D_k$). In Mellin space,
up to $N$-independent terms and $O(1/N)$,
$$\ln\Delta_N=\int_0^1dz\,\frac{z^{N-1}-1}{1-z}\Big[2\int_{\mu_F^2}^{(1-z)^2Q^2}\frac{dq^2}{q^2}A(\alpha_s(q^2))+D(\alpha_s((1-z)^2Q^2))\Big],$$
with $A=C_F\alpha_s/\pi+O(\alpha_s^2)$ (normalization verified against the one-loop $8C_F\mathcal D_1$) and
$D=O(\alpha_s^2)$. *Caveats:* the Landau pole in the $q^2$ integral needs a prescription (e.g. minimal
prescription); partonic vs hadronic threshold. *Refs:* Sterman 1987; Catani–Trentadue 1989; Becher–Neubert–Xu
2008.

**B20 (TMD factorization: DY, SIDIS, $e^+e^-\to h_1h_2X$) — [A]; the evolution equations given the definitions are
[$R_{\rm def}$].** For $q_T\ll Q$, including $q_T\sim\Lambda$:
$$\tilde W(b_T,Q)=\sum_jH_j(Q,\mu)\,\tilde f_{j/A}(x_A,b_T;\mu,\zeta_A)\,\tilde f_{\bar j/B}(x_B,b_T;\mu,\zeta_B)+\dots,\qquad\zeta_A\zeta_B=Q^4,$$
and the cross section is $\int\frac{d^2b_T}{(2\pi)^2}e^{iq_T\cdot b_T}\tilde W+Y(q_T,Q)$. The evolution equations:
- CS equation: $\partial\ln\tilde f/\partial\ln\sqrt\zeta=\tilde K(b_T;\mu)$, with $d\tilde K/d\ln\mu=-\gamma_K$;
- RG equation: $d\ln\tilde f/d\ln\mu=\gamma_F(\alpha_s;1)-\frac12\gamma_K\ln(\zeta/\mu^2)$;
- one-loop kernel: $\tilde K=-\frac{\alpha_sC_F}{\pi}\ln\frac{\mu^2b_T^2}{b_0^2}$ (verified);
- small-$b_T$ OPE: $\tilde f=\sum_j\tilde C_j\otimes f_j+O((b_T\Lambda)^p)$, [A].

*Refs:* Collins–Soper 1981; CSS 1985; Collins 2011 ch. 10, 13–14; SCET formulations (e.g. Chiu–Jain–Neill–Rothstein
2012; Becher–Neubert 2011). *NP:* MA1; the large-$b_T$ behaviour of $\tilde K$ and $\tilde f$ is nonperturbative.

**B21 (Sivers sign reversal) — [$R_{\rm def}$]; observable consequence [A].** For the operator-defined TMDs with
future-pointing (SIDIS) and past-pointing (DY) staple Wilson lines,
$f_{1T}^{\perp\,\rm SIDIS}(x,k_T)=-f_{1T}^{\perp\,\rm DY}(x,k_T)$. Proof: parity + time reversal applied to the
definitions (Collins 2002). Companion statement: T-odd FFs are universal (Collins–Metz 2004; Meissner–Metz 2009).

**B22 (no generalized TMD factorization for $pp\to h_1h_2X$, back-to-back) — [V].** No factorization with
process-independent (universal) TMDs exists. Explicit counterexamples: Collins–Qiu 2007 (abelian model,
spin-dependent); Rogers–Mulders 2010 (colour entanglement, also unpolarized). Collinear factorization of the
$q_T$-integrated cross section is not refuted by this; it is [C] (B13).

**B23 (diffractive factorization) — [A] for DDIS; [V] for hadron–hadron with the same dPDFs.** In DIS with a
leading proton (or a rapidity gap) at fixed $x_{\mathbb P}$ and $t$, the cross section factorizes with
diffractive PDFs (Collins 1998). In hadron–hadron hard diffraction the same dPDFs fail; the gap-survival
suppression is observed and has a theoretical mechanism. Say that this is not a perturbative counterexample.

**B24 (polarized sum rules and relations).**
- Bjorken sum rule, [$R_{\rm PT}$] + isospin + $g_A$ input:
  $\int_0^1(g_1^p-g_1^n)dx=\frac{g_A}{6}[1-a-(\frac{55}{12}-\frac{n_f}3)a^2+O(a^3)]+O(\Lambda^2/Q^2)$ (verified via
  Crewther).
- First moment of singlet $g_1$: scheme-dependent split between $\Delta\Sigma$ and $\Delta G$ (axial anomaly).
- Burkhardt–Cottingham $\int g_2=0$: [C] (assumes no $J=0$ fixed pole or $\delta(x)$ term; holds at $O(\alpha_s)$
  in PT).
- Wandzura–Wilczek: [V] in general (genuine twist-3 $\bar qGq$ terms).
- Soffer bound $|h_1|\le\frac12(f_1+g_1)$: [R] at LO and preserved by LO evolution; scheme-dependent beyond.
- Every statement needs a declared $\gamma_5$ scheme.

**B25 (hard exclusive processes).**
- [A]: $\gamma^*\gamma\to\pi^0$ and $F_\pi$ at leading power. Asymptotically $Q^2F_\pi\to8\pi\alpha_sf_\pi^2$ and
  $Q^2F_{\gamma^*\gamma\pi}\to\sqrt2f_\pi$ ($f_\pi\simeq131$ MeV; standard, not re-derived).
- [A]: DVCS (Collins–Freund 1999; Ji–Osborne 1998) and meson production by longitudinal photons
  (Collins–Frankfurt–Strikman 1997).
- [V] in standard form: transverse photons (endpoint divergences).
- Pion FF endpoint (Feynman) contributions are power suppressed; Sudakov suppression helps
  (Li–Sterman 1992). The claimed all-order status should be checked by the refs agent.

**B26 (heavy-quark processes).**
- $B\to D\pi$: [A].
- $B\to\pi\pi$ at leading power: [A], with disputes (charm penguins, hard-spectator counting).
- Subleading power: endpoint-divergent [V for standard factorization].
- Inclusive $B\to X_s\gamma$: heavy-quark expansion [A] (coefficients $R_{\rm PT}$); shape-function factorization
  at the endpoint [A].
- NRQCD decays: [A] (BBL 1995). NRQCD production: [C]. NNLO checks with gauge-completed operators: [P]
  (Nayak–Qiu–Sterman 2005–06).

**B27 (double parton scattering) — [A] for double DY at leading power; [C] for the pocket formula.**
- The double DY cross section factorizes into DPDFs (including colour- and spin-correlated and interference
  terms) times partonic cross sections, with a subtraction against SPS for the $1\to2$ splitting region
  (Diehl–Gaunt–Schönwald 2017).
- Glauber exchanges cancel (Diehl–Gaunt–Ostermeier–Plößl–Schäfer 2016).
- $\sigma_{\rm DPS}=\sigma_A\sigma_B/\sigma_{\rm eff}$ is a model [C].

**B28 (small-$x$ and high-energy factorization).**
- BFKL at LL and NLL in the perturbative Regge limit: [A].
- High-energy ($k_T$) factorization (Catani–Ciafaloni–Hautmann 1991; Collins–Ellis 1991): [P] (LL, specific
  processes).
- BK: [A] within LL and mean field/large $N_c$. JIMWLK: [A] at LL.
- Saturation and the CGC as a description of hadrons: [C].
- Collinear factorization at fixed $Q$ as $x\to0$ is non-uniform: higher-twist enhancement, so B10 needs
  "fixed $x$".

**B29 (lattice-oriented factorization) — [A].** Quasi-PDFs, pseudo-PDFs and "good lattice cross sections" obey
short-distance/LaMET factorization onto light-cone PDFs, with perturbative matching kernels and power corrections
that are enhanced at the endpoints $x\to0,1$ (Ma–Qiu 2018; Izubuchi–Ji–Jin–Stewart–Zhao 2018; Radyushkin 2017;
renormalon analyses, verify). Lattice systematics (continuum limit, renormalization, finite $P_z$) are separate
issues.

**B30 (twist-3 collinear factorization for single-spin asymmetries) — [P] for SIDIS/DY at one loop; [C] for
$pp\to\pi X$.** $A_N$ at large $p_T$ is power suppressed ($\propto M/p_T$) and expressed through
Qiu–Sterman (Efremov–Teryaev) quark–gluon–quark correlators and twist-3 FFs. It matches the TMD Sivers
description at $\Lambda\ll q_T\ll Q$ (Ji–Qiu–Vogelsang–Yuan 2006). There is no all-order proof for hadron–hadron
initial states (gauge-link complexity).

---------------------------------------------------------------------------------------------------

## 9. Discrepancies and gaps in the binding conventions (CONTEXT.md)

**D1 ($F_L$).** CONTEXT: "$F_L=F_2-2xF_1$". From the CONTEXT tensor $W^{\mu\nu}$ itself, contracting with the
longitudinal polarization $\epsilon_L$ ($\epsilon_L^2=1$, $q\cdot\epsilon_L=0$) gives
$2x\,\epsilon_L^\mu\epsilon_L^\nu W_{\mu\nu}=(1+\frac{4M^2x^2}{Q^2})F_2-2xF_1$, and $\epsilon_T\epsilon_TW=F_1$
(verified, `c7`). The physical longitudinal structure function (∝ $\sigma_L$) is therefore
$F_L=(1+4M^2x^2/Q^2)F_2-2xF_1$. The CONTEXT formula holds only for $M\to0$. *Fix:* state "for $M^2/Q^2\to0$", or adopt
the general definition. This is needed in the target-mass section of Ch5.

**D2 (normalization of $W^{\mu\nu}$; antisymmetric parts).** Fix
$W^{\mu\nu}=\frac{1}{4\pi}\int d^4z\,e^{iq\cdot z}\langle P,S|[j^\mu(z),j^\nu(0)]|P,S\rangle$ (spin-averaged for the
unpolarized part, states normalized relativistically), so that the parton model gives
$F_2=x\sum e_q^2(q+\bar q)$ (standard normalization; the writer must check it against the chosen state
normalization). Add the antisymmetric parts ($F_3$; $g_1,g_2$), which require an $\epsilon^{0123}$ sign convention
and a $\gamma_5$ convention. Neither is in CONTEXT.

**D3 ($\gamma_5$, $\epsilon$-tensor, polarized definitions).** CONTEXT fixes no $\gamma_5$ definition, no
$\epsilon^{0123}$ sign, no $\gamma_5$ scheme in DR (HVBM + Larin finite renormalization, or another), and no helicity
($\gamma^+\gamma_5$) or transversity ($i\sigma^{j+}\gamma_5$ or $\gamma^+\gamma^j\gamma_5$) PDF definitions with spin
vectors. All of these are needed for B24 and for $W/Z$ processes.

**D4 (gluon PDF and FF definitions).** These are missing. Proposed gluon definition (normalization checked:
a free gluon gives $\delta(1-\xi)$):
$f_g(\xi)=\int\frac{dw^-}{2\pi\,\xi P^+}e^{-i\xi P^+w^-}\langle P|F^{+j}_a(w)\,W_{ab}[w,0]\,F^{+j}_b(0)|P\rangle$ (adjoint
Wilson line, sum over $j$). The FF definition must include the $d$-dimensional normalization conventions of
Collins–Soper/Collins 2011. I recall a factor $z^{1-2\epsilon}$ in $d$ dimensions (verify against Collins 2011,
ch. 12).

**D5 (averaging in $d$ dimensions).** CONTEXT says "spin averaged". In CDR one must say whether gluon
polarizations are averaged over $2-2\epsilon$ or over 2. The choice shifts the finite parts of gluon-initiated
$\overline{\rm MS}$ coefficients by a term $\propto P_{qg}(z)$. The standard $\overline{\rm MS}$ results quoted in §6 are, I
believe, the $2-2\epsilon$ convention (verify). My `c2` cross-check cannot detect this choice, because the shift
cancels in $\Delta_{qg}-C_g$. Similarly, "colour summed" should read: summed over the colour index of the field
operators, and averaged over target colour for partonic targets.

**D6 (products with plus distributions).** CONTEXT defines $[g]_+$ for a whole function. Most literature formulas
(e.g. "$4(1+z^2)\mathcal D_1$" in DY) use the **product** convention
$\langle g\,\mathcal D_k,h\rangle=\int(gh-g(1)h(1))\ln^k(1-z)/(1-z)$. The two differ by $\delta$-terms, e.g.
$C_F[\frac{1+z^2}{1-z}]_+=C_F[\frac{1+z^2}{(1-z)_+}+\frac32\delta(1-z)]$ (verified). *Fix:* add the product convention
explicitly. Otherwise $\delta(1-z)$ coefficients will be wrong.

**D7 (support).** Ch6 "support $0\le\xi\le1$" vs the CONTEXT convention $f_{\bar q}(\xi)=-f_q(-\xi)$: the support of
$f_q$ is $-1\le\xi\le1$ (O9).

**D8 (normalization of $\Pi$).** The relation $R=12\pi\,{\rm Im}\,\Pi(s+i0)$ depends on the normalization and sign of
$\Pi$. Fix, e.g., $i\int d^4x\,e^{iq\cdot x}\langle0|T j^\mu(x)j^\nu(0)|0\rangle=(q^\mu q^\nu-q^2g^{\mu\nu})\Pi(q^2)$, and
check that ${\rm Im}\,\Pi>0$ and $R_0=N_c\sum e_q^2$ with it. (The writer must do this check; I did not fix the sign
here.)

**D9 (TMD conventions).** Choose one rapidity regulator for the main text (I recommend Collins 2011:
$\tilde f(x,b_T;\mu,\zeta)$, $\zeta_A\zeta_B=Q^4$) and give a conversion table to the SCET ($\nu$, $\eta$-regulator,
$\delta$-regulator, exponential regulator) conventions. Fix the staple orientation and sign convention behind
"Sivers $>0$". The Fourier convention in CONTEXT is consistent with Collins (2011) for even functions; the sign
matters for the Sivers term.

**D10 (the [R] tag).** Suggested (non-binding) refinement: the $R_{\rm PT}$/$R_{\rm def}$ sub-kinds (O2). Each theorem box
gets a "非微扰地位" line citing MA0–MA4.

**D11 (outline order).** Ch12 uses SCET Glauber operators before Ch14 introduces SCET. See §5.

**D12 (Ch8 "consistent with Ch5 [R]").** Replace with the precise statement of B10 (twist-2 part equivalent in the
distribution sense; pointwise error [A]).

---------------------------------------------------------------------------------------------------

## 10. Verification log (python, `research/critic/checks/`)

All scripts run with `python3 -I`; output reproduced in the agent's session. A summary:

| Script | What was checked | Result |
|---|---|---|
| `c1_splitting.py` | Mellin moments of LO $P_{ij}$ (sympy, exact); $\int z^{n-1}P_{qq}=C_F[\frac32+\frac1{n(n+1)}-2S_1(n)]$ for $n=1..6$; identity $[\frac{1+z^2}{1-z}]_+=\frac{1+z^2}{(1-z)_+}+\frac32\delta$; $n=1$ number sum rule; $n=2$ momentum sum rule for the quark column ($\gamma_{qq}+\gamma_{gq}=0$) and the gluon column ($2n_f\gamma_{qg}+\gamma_{gg}=0$) | all exact |
| `c2_coeff_consistency.py` | $\overline{\rm MS}$ $C_q$, $C_g$ (DIS) vs $\Delta_{q\bar q}$, $\Delta_{qg}$ (DY) vs DIS-scheme DY ($1+\frac{4\pi^2}{3}$ and $\frac32-5z+\frac92z^2$): $\Delta^{\overline{\rm MS}}_{q\bar q}-2C_q=\Delta^{\rm DIS}_{q\bar q}$ and $\Delta^{\overline{\rm MS}}_{qg}-C_g=\Delta^{\rm DIS}_{qg}$ on 8 test functions; Adler $\langle C_q,1\rangle=0$; closed form of $C^{q,(1)}_{2,n}$ | residuals $\lesssim3\times10^{-30}$; Adler exact; closed form exact for $n=1..6$. **A commonly quoted variant** (with $\frac2{n+1}+\frac1{n^2}$ in place of $\frac4{n+1}+\frac2{n^2}$) **fails** the $n=1$ (Adler) check |
| `c3_thrust.py` | DEFG $O(\alpha_s)$ thrust: small-$\tau$ limit $-(4\ln\tau+3)/\tau$; $\delta(\tau)$ coefficient from $\sigma_{\rm tot}=\sigma_0(1+\alpha_s/\pi)$; cumulant | $c_\delta=\pi^2/3-1$ to 20 digits; cumulant differs from the singular form by $O(\tau\ln\tau)$ |
| `c4_R_crewther.py` | $R$ at $O(a^2)$ ($1.9857-0.1153\,n_f$); Bjorken $O(a^2)$ ($-3.5833$ at $n_f=3$); Crewther: $C_{\rm Bjp}D_{\rm NS}=1+\beta_0(\frac78-\zeta_3)a^2$ | exact; $K_1=C_F(-\frac{21}8+3\zeta_3)$ reproduced, which cross-validates both inputs |
| `c5_lemmas.py` | L3: $Q^2\int x^n\sin(Q^2x)dx$ bounded while $\sup|R|=1$; L2: $\delta'$ has vanishing even moments; L4: $\sin\pi n$, $(1-\cos\pi n)/2$ | as claimed |
| `c6_threshold.py` | $\langle\mathcal D_0,z^{N-1}\rangle=-S_1(N-1)$, $\langle\mathcal D_1,z^{N-1}\rangle=\frac12[S_1^2+S_2](N-1)$ and their $\ln\bar N$ asymptotics; normalization $A^{(1)}=C_F\alpha_s/\pi$ vs the $8C_F\mathcal D_1$ of DY | exact / consistent |
| `c7_misc.py` | $F_L$ with target mass from the CONTEXT $W^{\mu\nu}$; one-loop Sudakov FF $\Rightarrow K$, $G$, $\gamma_K=2C_F\alpha_s/\pi$; $\tilde K$ one loop and $d\tilde K/d\ln\mu=-\gamma_K$; $\bar n\cdot p=\sqrt2p^+$, $n\cdot p=\sqrt2p^-$ | all as claimed |

**Not verified here (marked "standard" in the text):** the asymptotic pion and transition form factors; the
Altarelli–Martinelli $F_L$ coefficients (only their moment normalization was checked by hand); the
$P_{\rm NS}^\pm$ colour factor; the separate real/virtual constants in $e^+e^-$ (deliberately not quoted).

---------------------------------------------------------------------------------------------------

## 11. Attributions and claims flagged "(verify)" for the refs agent

1. Anikin–Zavialov, Ann. Phys. 116 (1978) 135: proof of the light-cone expansion in renormalized PT.
2. Lowenstein–Zimmermann, Nucl. Phys. B86 (1975) 77 (BPHZL, massless theories): does it cover IR finiteness of
   off-shell Green functions in *gauge-fixed QCD*?
3. Frye–Hannesdottir–Paul–Schwartz–Yan, PRD 99 (2019) 056015: KLN and forward/disconnected contributions.
4. Gaunt, JHEP 07 (2014) 110: exact claim about Glauber non-cancellation for $E_T$ / beam thrust.
5. Aybat–Sterman, PLB 671 (2009) 46: scope of the Glauber/Coulomb-phase cancellation with coloured final states.
6. Forshaw–Seymour–Siodmok, JHEP 11 (2012) 066: order at which collinear-factorization breaking appears in cross
   sections.
7. Collins–Soper–Sterman, Nucl. Phys. B263 (1986) 37 (heavy-particle production): completeness of the Glauber
   argument; this decides the [A]/[C] tag in B13.
8. Collins, PRD 58 (1998) 094002: wording "error suppressed uniformly in $m/Q$".
9. Doria–Frenkel–Taylor 1980 / Di'Lieto et al. 1981: precise statement that the non-cancelling terms are power
   suppressed for DY.
10. Beneke–Braun, Nucl. Phys. B454 (1995) 253: absence of $1/Q$ renormalon corrections in DY.
11. Becher–Neubert–Rothen–Shao 2016 (NGL factorization) and Becher–Neubert–Shao 2021 (SLL resummation):
    journal data and claimed status.
12. Mankiewicz–Piller 2000: transverse-photon endpoint divergence reference.
13. Ebert–Michel–Stewart–Sun 2022: $k_T$-integrated TMDs vs collinear PDFs.
14. Braun–Vladimirov–Zhang 2019: endpoint scaling of quasi-PDF power corrections.
15. Korchemsky–Sterman 1999 (Nucl. Phys. B555, 335): thrust factorization with power corrections.
16. Shifman 2000 (hep-ph/0009131): quark–hadron duality review.
17. Graudenz 1994: NLO SIDIS.
18. Li–Sterman 1992; Soffer 1995; Labastida–Sterman 1985; Kodaira 1980; Christ–Lee 1966: standard, but check the
    page data.
19. The factor $z^{1-2\epsilon}$ in the $d$-dimensional FF definition (Collins 2011, ch. 12).
20. Which $d$-dimensional gluon-polarization average underlies the standard $\overline{\rm MS}$ $C_g$, $\Delta_{qg}$ (D5).
21. Chapter numbers of Collins (2011) quoted in this review (ch. 5, 8–10, 12–14) are from memory; verify them.

---------------------------------------------------------------------------------------------------

## 12. Draft Chinese text for Ch1 (meta-assumptions and tag refinement), ready to adapt

**元假设（建议写入第一章，并在每个定理框的"非微扰地位"一栏引用）**

- **MA0（存在性）**：QCD 作为四维量子场论存在；强子态 $|P\rangle$ 存在；重整化的复合（光线）算符的强子矩阵元至少作为
  $\xi$ 的分布有定义。（四维 Yang–Mills 理论的存在性是尚未解决的千禧年问题。）
- **MA1（区域完备性）**：微扰论（无质量部分子、红外正规化）中识别出的领头幂次区域，就是完整 QCD 的全部领头幂次区域；
  禁闭只改变红外敏感因子（PDF、FF、软因子）的数值，而不产生新的领头区域。
- **MA2（幂次计数的传递）**：微扰论中非领头区域的幂次压低，在完整 QCD 中表现为 $(\Lambda/Q)^p$ 压低；
  除可用 OPE 处理的过程外，指数 $p$ 不能由微扰论确定。
- **MA3（解析性与高能行为）**：色散关系（求矩）所需的解析性，以及小 $x$（Regge）行为的假设，对最低阶矩尤为关键。
- **MA4（渐近性）**：微扰级数是渐近级数；"全阶"指形式幂级数；红外重整子歧义与幂次修正同阶，
  因此领头幂次因子化是渐近意义下的陈述。

**严格性标签 [R] 的细化**：$R_{\rm PT}$——在重整化微扰论的每一阶、对红外正规化的部分子格林函数成立的完整证明；
$R_{\rm def}$——由算符定义与对称性直接推出的代数性质（如规范不变性、支撑、电荷共轭关系、求和规则、Sivers 变号）。
凡涉及强子的陈述，最多只能达到"$R_{\rm PT}$ + 元假设"的地位。
