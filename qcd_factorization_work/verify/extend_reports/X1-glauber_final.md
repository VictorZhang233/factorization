# X1 — Glauber cancellation in inclusive Drell–Yan: final report (Appendix O)

**Status of this document.** Final revision of the proof-extension report X1 (topic: spectator–spectator Glauber exchanges in inclusive Drell–Yan, App O of the monograph), written after three rounds of adversarial review with two independent reviewers per round. It supersedes `X1-glauber.md`, `X1-glauber-fix1.md` and `X1-glauber-fix2.md`. It is self-contained: every definition, hypothesis and proof needed for transcription is given here. Reviews, scripts and logs are listed in §14 and Appendix A. Grades use the monograph's system: [R, R_PT], [R, R_def], [R, R_cond: premises], [A], [P], [C]. A statement about an explicitly defined class of functions or model integrals, proved with no unproven input, is graded [R, R_PT] ("pure mathematics, R_PT type"). Its application to QCD jets is graded separately.

---

## 0. Summary

### 0.1 Setting and question

App O (the two-time localization framework, taken over from App E of the reference document `factorization_qcd-2.pdf` and corrected) proves the cancellation of spectator–spectator (SS) Glauber exchanges in inclusive Drell–Yan (DY) for the graph class $\mathcal G_0$, in which the soft subgraph consists of direct soft lines between the two collinear subgraphs $J_A$, $J_B$. For non-commuting localized insertions on one spectator parton (*coincident* connections), the cancellation rests on the complete-set clause `asm:appO-mixing`(c). This report

1. supplies analytic tools for coincident insertions, each an identity or an explicit bound: joint localization with error bounds, multi-pole external factors, rotation of the $k^+$ contour, a ray identity, and bounds for two-insertion jets;
2. proves model theorems for the two coincident $O(g^4)$ patterns (fully and half coincident) in the *global two-time model* (Def. D4);
3. repairs the window construction of `prop:appO-ss-cancel` (side-independent windows);
4. states precisely what remains assumed, and where.

### 0.2 Principal results

| result | content (one line) | grade |
|---|---|---|
| L1 | joint localization of $N$ insertions: exact sector formula, corrected error bound with $\sum_\sigma\lvert w_\sigma\rvert$, closed-quadrant lemma | [R, R_PT] |
| L8 | explicit bounds for two-insertion jets on the rotated contour | [R, R_PT] |
| P1 | side-independent windows remove the window-edge terms of `prop:appO-ss-cancel` | [R, R_cond: `asm:appO-lcopt`] |
| T2 | fully coincident SS pair, $O(g^4)$, uncut lines: ${\rm Re}\,p_{\rm opp}=O(\varepsilon^{1/2}(1+L_B)^2(1+L))$, ${\rm Im}\,p_{\rm opp}=-\frac1\pi\ln\frac1\varepsilon+O(1)$ | model [R, R_PT]; QCD jets [R, R_cond], content [P]; physical reading [P] |
| T2′ | regulated version, with explicit rate; end-pole formula; two-sided regulator study | (a)(b) [R, R_PT]; (c) [P] |
| P2 | strict window: $p_{\rm opp}=\tfrac12+2\delta_A\delta_B$, i.e. set by the regulator shape | (a) known; (b)(c) [R, R_PT] |
| T3 | half-coincident pair: residual $2ic_1c_2\,{\rm Im}W_{12}[X_1,X_2]$; ${\rm Im}W_{12}=O(1)$ unregulated, power suppressed with an in-window $k^-$ regulator (proved bound) | (a)(b)(c)(e) [R, R_PT]; (d)(f) [P] |
| L4 | colour: the half-coincident colour factor vanishes for valence remnants and for real colour states | [R, R_def] |
| P4 | per-graph ordering weights are not fixed by window data, within the stated class | (a)(b) [R, R_PT]; (c) [P] |
| P5 | the direct-line ladder class is not closed under unitarity at $O(g^6)$ | [A] |
| ERR-S1b | correction to the reference's Rem E.32 / E.33 status / Rem E.49(2), restricted to uncut lines | [R, R_cond] + [P] |

### 0.3 What is not claimed

* The grade of inclusive DY collinear factorization (`thm:dy-factorization`) is unchanged, [A]. The TMD versions of the results are [C] (§11).
* Every statement that an assumption of type `asm:appO-mixing`(c) is "needed" or "not needed" is relative to App O's two-time framework. None is a statement about QCD factorization as such; the graph-by-graph argument of CSS/Collins/DGOPS (§10) has no ordering weights, and no gap in it is identified here.
* The coincident-pattern theorems concern the side sums of **uncut** SS lines (`def:appO-family`). Direct SS gluons that cross the final-state cut (real emission) belong to $\mathcal G_0$ and to `asm:appO-mixing`(c). They are not covered (Remark C, OPEN-13).
* The model theorems are statements about the global two-time model $\mathbb M_{\rm glob}$ (Def. D4). They hold pointwise on the domains $\mathcal N_A\cap\mathcal N_B$ (or $\mathcal N_B$) of Def. D5. Those domains exclude an $O(1)$ part of spectator phase space, so nothing is claimed for the spectator-integrated cross section (OPEN-2). Their physical reading needs the proposed matching assumption `asm:appO-collinear-ends` (§2).

---

## 1. Conventions, framework and definitions

### 1.1 Conventions

These follow CONTEXT.md. The metric is $(+,-,-,-)$, and $v^\pm=(v^0\pm v^3)/\sqrt2$. Hadron $A$ moves along $+z$ and hadron $B$ along $-z$, with $P_A^+\sim P_B^-\sim Q$. $J_A$ uses the light-cone time $\tau=x^+$ and light-cone energies $l^-$; $J_B$ uses $\tau=x^-$ and energies $l^+$. The quark–gluon vertex is $+ig\gamma^\mu t^a$, and $C_A=3$. On-shell light-cone energies are $E(l)=(\mathbf l_T^2+m^2-i0)/(2l^+)$ in $J_A$.

### 1.2 The framework (App O)

The following is a summary; the binding statements are in App O.

* **Region and subgraphs.** $\Gamma$ is a DY forward graph with leading region $R$. Its collinear subgraphs $J_A$, $J_B$ cross the final-state cut. The hard parts $H$, $H^\dagger$ sit at the vertices $V_H$, $V_H^\dagger$, placed at $\tau=0$ by `lem:appO-hard-locality`.
* **Active lines and spectators.** Lines of $J_A$ ending at $V_H$ are *active*; the others are *spectators*. $J_A$ is cut-summed and written in light-cone-ordered perturbation theory (LCOPT; `lem:appO-lcopt`, `lem:appO-unitarity`).
* **Class $\mathcal G_0$.** The soft subgraph consists of direct lines between $J_A$ and $J_B$. In the reference these lines "可以被割" (may be cut), Def. E.1(e).
* **SS lines and families.** An *SS line* is a direct line with both ends on spectators. The *family* $\mathfrak F(\Gamma_0)$ (`def:appO-family`, reference Def. E.30) adds SS lines to a core graph $\Gamma_0$. Each added line lies **wholly on the amplitude side or wholly on the conjugate side**.
* **Side sums.** A *side assignment* gives each SS line a side. The *side sum* is the sum over side assignments and cuts.
* **Windows and coincidence.** The windows are $\Theta_j$ (`def:appO-windows`). A connection is *coincident* if two localized insertions sit on one spectator parton.
* **Complete-set clause.** `asm:appO-mixing`(c) combines the window with the adjacent near-on-shell soft region, real emission included ("含实发射"), and with the graphs carrying three- and four-gluon (Lipatov-type) vertices.

**Scope convention of this report.** "Side sum" always means the sum over side assignments of uncut SS lines, as in `def:appO-family`. Contributions in which a direct SS gluon crosses the final-state cut are called *cut contributions*. They are excluded unless stated otherwise (Remark C).

### 1.3 Scales

* **Jet scales.** For a jet $X\in\{A,B\}$: $\lambda_X:=\max|A|$ and $\mu_X:=\min|A|$ over all light-cone energy differences $A$ in the energy denominators of $J_X$. One has $\mu_X>0$ pointwise: initial states of a bound hadron always qualify, and final states do so on the domain $\mathcal N_X$ of Def. D5. Both scales are $O(\lambda^2Q)$ in the Glauber scaling region.
* **Transverse scales.** For SS line $e$: $a_e:=\mathbf k_{Te}^2$, $a:=(a_1a_2)^{1/2}$, $a_{\min}:=\min a_e$, $a_{\max}:=\max a_e$.
* **Small parameter.** $\varepsilon:=\lambda_A\lambda_B/a$ and $L:=\ln(1/\varepsilon)$.
* **Logarithms.** $\ell_A:=\ln(1+\lambda_A/\mu_A)$, $\ell_B:=\ln(1+16\lambda_B/\mu_B)$, and $L_B:=\ln(1+4\varepsilon^{-1/2}\lambda_B/\mu_B)\le L/2+\ln(1+4\lambda_B/\mu_B)$.

### 1.4 Connecting propagators

On the amplitude side,
$$R_e(k)=\frac{1}{2k_e^+k_e^--a_e+i0}=\frac{r_e}{k_e^--z_e},\qquad r_e=\frac1{2k_e^+},\qquad z_e=\frac{a_e-i0}{2k_e^+}.$$
The pole lies in the lower half plane (LHP) for $k_e^+>0$ and in the upper half plane (UHP) for $k_e^+<0$.

### 1.5 Definitions

**Definition D1 (insertion sectors).** Consider $N$ amplitude-side insertions into a jet $J$, with injected light-cone energies $q=(q_1,\dots,q_N)$. Here $q=k^-$ for $J_A$, and $q=p:=-k^+$ for $J_B$ (the energy injected into $J_B$ in the standard flow).

* A *sector* $\sigma$ splits $\{1,\dots,N\}$ into the insertions before $V_H$, in time order $b_1,\dots,b_n$, and those after $V_H$, in time order $f_1,\dots,f_m$. Write $B_\sigma$ and $F_\sigma$ for the two sets.
* Gap momenta: $K^B_l:=\sum_{l'\le l}q_{b_{l'}}$ for $l=1..n$, and $K^F_l:=\sum_{l'\ge l}q_{f_{l'}}$ for $l=1..m$.
* The *colour order* of $\sigma$ is $b_1\dots b_nf_1\dots f_m$.

**Definition D2 (class $\mathcal J$; condition (SEC)).** A jet function $J$ satisfies **(SEC)** (sector structure) if it has the form
$$J=\sum_\sigma J^{(\sigma)},\qquad J^{(\sigma)}(q)=\sum_tc_t\prod_{l=1}^n\phi^t_{B,l}(K^B_l)\prod_{l=1}^m\phi^t_{F,l}(K^F_l),$$
with the following properties.

* All sums are finite.
* Each initial gap function $\phi^t_{B,l}$ is a product of $n^t_l\ge1$ factors $i/(A+K+i0)$.
* Each final gap function $\phi^t_{F,l}$ is a product of $n^t_l\ge1$ factors $i/(A'-K+i0)$.
* The energies are real, with $\mu_J\le|A|,|A'|\le\lambda_J$.

Associated quantities:

* Number of extra states: $d_t:=\sum_l(n^t_l-1)$.
* *Equal-time value*: $\mathcal J_\sigma:=\sum_{t:\,\text{all }n^t_l=1}c_t$.
* Norms: $M_\sigma:=\sum_t|c_t|\lambda_J^{-d_t}$ and $M^\flat_\sigma:=\sum_t|c_t|\mu_J^{-d_t}$, so that $M^\flat_\sigma\ge M_\sigma\ge|\mathcal J_\sigma|$. Put $M:=\max_\sigma M_\sigma$ and $M^\flat:=\max_\sigma M^\flat_\sigma$. For the two jets, $m_X:=M_X/|\mathcal J_X|$ and $m^\flat_X:=M^\flat_X/|\mathcal J_X|$.
* The *eikonal product* is $e_\sigma:=\prod_l(-iK^B_l)^{-1}\prod_l(iK^F_l)^{-1}$. For large gap momenta, $J^{(\sigma)}\approx\mathcal J_\sigma e_\sigma$.

*Status.* (SEC) is the LCOPT form of a leading-power cut-summed jet factor with insertions. It follows from `lem:appO-lcopt`, `lem:appO-numerators` and `lem:appO-orientation` (initial and final denominators have opposite orientations) under `asm:appO-lcopt` (reference Lemmas E.15, E.16, E.21, E.22 under E.18).

**Definition D3 (structural conditions).**

* **(EQ)** (equal-time values). For insertions on spectators, all $\mathcal J_\sigma$ are equal: $\mathcal J_\sigma=\mathcal J$ for every sector, colour-stripped. *Verified in LCOPT*: $V_H$ commutes with operators acting on spectators, so moving $V_H$ past spectator insertions leaves the equal-time value unchanged (`lem:appO-insertion-values`(b),(c); reference Lemma E.28(i)).
* **(ADJ)** (adjacent swap). Suppose two sectors of the same jet differ only by the order of two *adjacent* operations $O,O'\in\{\text{insertion }1,\text{insertion }2,V_H\}$. Then the terms with a single-state gap between $O$ and $O'$ correspond bijectively, with equal coefficients $c_t$ and equal gap functions in all other gaps. Restricted to all-single-state terms, (ADJ) implies (EQ).
* **(REAL)** (reality). Every colour-stripped jet function is a fixed phase times a rational function with real coefficients.

*Status of (ADJ) and (REAL).* Both hold exactly in the scalar spectator model (§14.1). There every gap function depends only on the set of operations already performed, and all couplings and energies are real. For spin-summed leading-power LCOPT jets they are *argued*, not proven:

* adjacent operations acting on different partons commute on Fock states;
* two insertions on one spectator have equal good-component couplings, proportional to the spectator's plus momentum, which the insertion does not change;
* energies and good-component couplings are real, traces without $\gamma_5$ are real, and each extra intermediate state brings a factor $i$ from its denominator and $-i$ from its extra vertex.

For general hadron wave functions they are open. When applied to QCD jets they enter through the proposed register entries `asm:appO-adjacent-swap` and `asm:appO-real-jets` (§2.2). A round-3 reviewer test shows that (ADJ) cannot simply be dropped from L8: with one final-state energy changed so that (ADJ) fails, the $1/\kappa_2$ strip tails no longer cancel (`review_r3_1_logs/l8_general.log`).

**Definition D4 (global two-time model $\mathbb M_{\rm glob}$).** This is a model definition, not an assumption. Take colour-stripped jet functions $J_A(k^-)$, depending only on the minus components of the insertion momenta, and $J_B(p)$ with $p=-k^+$, together with exact connecting propagators. The model integral of a connection is
$$\int\prod_e\frac{d^4k_e}{(2\pi)^4}\;J_A(k^-)\prod_eR_e(k_e)\;J_B(-k^+)$$
over all of $\mathbb R^4$ per line. Equivalently, `lem:appO-glauber-pc`(a),(b) are applied globally: $k^+$ is dropped inside $J_A$ and $k^-$ inside $J_B$. This is done also at $|k^+|\sim a/\lambda_A$ and $|k^-|\sim a/\lambda_B$, where those approximations fail at relative $O(1)$.

For two SS lines, define
$$I(\pi_A,\pi_B):=\int\frac{d^2k^+}{(2\pi)^2}F_A^{[\pi_A]}(k^+)\,J_B^{[\pi_B]}(-k^+),\qquad F_A^{[\pi]}(k^+):=\int\frac{d^2k^-}{(2\pi)^2}J_A^{[\pi]}(k^-)\prod_eR_e(k_e),$$
where $[\pi]$ denotes the sum of the sectors of colour order $\pi$. $I(\pi_A,\pi_B)$ is exactly the colour-stripped covariant ladder graph ($\pi_A=\pi_B$) or crossed graph ($\pi_A\ne\pi_B$) built from $J_A$ and $J_B$.

*Remark (representation dependence).* By L1(a), the $k^-$ integrals equal sector functions of $J_A$ evaluated at the gluon-pole positions $z_e=a_e/(2k_e^+)$. For $|k^+|\sim\lambda_B$ these lie at $|k^-|\sim a/\lambda_B=O(Q)$, where `lem:appO-glauber-pc`(b) fails. This is a feature of one representation, obtained by closing the $k^-$ contours on the gluon poles. The representation-independent content is given by the sensitivity statements T3(e) and T2′(c). Physical conclusions drawn from model theorems are conditional on `asm:appO-collinear-ends`.

**Definition D5 (NF domains).** $\mathcal N_X$ is the set of internal configurations of $J_X$ (spectator momenta, masses, transverse momenta of the insertions) on which every final-state energy difference $A'$ of $J_X$ is negative. Initial differences are negative automatically for bound hadrons. Statements "on $\mathcal N_A\cap\mathcal N_B$" are pointwise.

*Remark.* This is not a mild restriction. In the scalar spectator model,
$$\alpha_1=E_s-E(s-k_2)=\frac{2\mathbf s_T\cdot\mathbf k_{2T}-\mathbf k_{2T}^2}{2x_sP^+}>0\iff \mathbf s_T\cdot\mathbf k_{2T}>\tfrac12\mathbf k_{2T}^2,$$
which holds on an $O(1)$ part of spectator phase space; the model's "alt" set has $\alpha_2=0.518\lambda^2>0$.

**Definition D6 (patterns, colour factors, ordering weights).**

* **Patterns.** Take two SS lines on the amplitude side. They are *non-coincident* if they join different $A$- and different $B$-spectators, *fully coincident* if they join the same $A$-spectator $i$ and the same $B$-spectator $j$, and *half-coincident* if they join the same $i$ and different $j_1\ne j_2$.
* **Fully coincident colour structure.** Put $X:=\mathbf T_i\cdot\mathbf T_j$. With the one-exchange amplitude $\mathcal M^{(1)}=-i\chi X$ ($\chi$ real; `lem:appO-glauber-operator`, reference E.36),
$$\mathcal M^{(2)}=\frac{(-i\chi)^2}{2}\Big[X^2+p_{\rm opp}\tfrac{C_A}{2}X\Big],\qquad p_{\rm same}+p_{\rm opp}=1.$$
The ladder graphs carry colour $X^2$ and the crossed graphs $X^2+\frac{C_A}2X$.
* **Ordering weights.** $N:=\sum_{\pi_A,\pi_B}I(\pi_A,\pi_B)$, $W(\pi_A,\pi_B):=I(\pi_A,\pi_B)/N$, $N_0:=\mathcal J_A\mathcal J_B/(a_1a_2)$ and $p_{\rm opp}:=W(12,21)+W(21,12)$.

**Definition D7 (rotated-contour notation).** Put $k^+=i\kappa$ with $\kappa\in\mathbb R^2$. Define:

* $h_\pi(\kappa):=(a_1a_2/\mathcal J_A)\,F_A^{[\pi]}(i\kappa)$, where each quadrant piece is continued from the corresponding real quadrant (L3);
* $f_\pi(\kappa):=J_B^{[\pi]}(-i\kappa)$, $S_B:=f_{12}+f_{21}$ and $\Delta_B:=f_{12}-f_{21}$;
* $r_e:=|\kappa_e|$, $\kappa_P:=\kappa_1+\kappa_2$, $r_P:=|\kappa_P|$, $R:=\max(r_1,r_2)$;
* $\langle y\rangle:=(\mu^2+y^2)^{1/2}$, with the $\mu$ of the jet in question.

**Definition D8 (regulators).**

* **Class $\mathfrak X$.** A factor $\prod_e\chi(k_e^+)$ in which $\chi$ is holomorphic in each closed quadrant obtained by rotating a half line counterclockwise by up to $\pi/2$ (the first quadrant for $k^+>0$, the third for $k^+<0$), real on the half lines, and satisfies
  $$|\chi(k)-1|\le|k|/K_c\ \ (|k|\le K_c),\qquad|\chi(k)|\le K_c/|k|\ \ (|k|\ge K_c),$$
  with $\lambda_B\ll K_c\ll a/\lambda_A$. Example: $\chi=1/(1+k/K_c)$ on $k>0$ and $1/(1-k/K_c)$ on $k<0$; the bounds follow from $|1\pm k/K_c|\ge\max(1,|k|/K_c)$ in the respective quadrant. Class $\mathfrak X$ is sufficient, not necessary: a Lorentzian $k^+$ regulator also gives ${\rm Re}\,p_{\rm opp}\to0$ numerically (§7, T2′).
* **Even Lorentzian.** $\chi_K(k):=K^2/(k^2+K^2)$, used on $k^-$ on the $A$ side.
* **Two-sided window** (`asm:appO-collinear-ends`). Use $\chi^+(k^+)$ at a scale $K^+$ with $\lambda_B\ll K^+\ll a/\lambda_A$, and $\chi^-(k^-)$ at a scale $K^-$ with $\lambda_A\ll K^-\ll a/\lambda_B$. Require $K^+K^-\gg a$, so that the near-shell segment $2k^+k^-\sim\mathbf k_T^2$ is retained. The range $a\ll K^+K^-\ll a/\varepsilon$ is non-empty for $\varepsilon\ll1$.

---

## 2. Assumptions

### 2.1 Register entries used

These are existing entries of `spec_v2/ASSUMPTIONS.md` v2.2, with their registered tags.

* `asm:appO-lcopt` [\tagA]: (i) no zero modes or endpoint contributions; minus-component truncation can be dropped; (ii) instantaneous loops. It is the source of (SEC).
* `asm:appO-envelope` [\tagA]: the fibre-integrated envelope. A rewording is proposed in §2.3.
* `asm:appO-mixing` [\tagA]: (a) half-plane splitting of external factors for general soft subgraphs (a reformulation (a′) is proposed in §2.3); (b) cut compatibility of $S$; (c) the complete-set clause.
* `asm:appO-deformation` [\tagA], items (a)–(d).
* `asm:appO-rewritten-cs` [\tagA].
* The App N inputs listed for `thm:appO-main` (`asm:appN-envelope`, `asm:appN-separation`, `asm:appN-ward-product`).

### 2.2 Proposed new entries

The owner is App O. The tags are proposed; the register is the lead author's decision.

**`asm:appO-adjacent-swap` (相邻交换对称性) — proposed \tagP.**

* *Statement:* every leading-power cut-summed LCOPT jet factor $J_X$ ($X=A,B$) with two amplitude-side insertions on spectator partons satisfies (ADJ) of Def. D3.
* *Status:* exact in the scalar spectator model; argued for spin-summed good-component couplings (Def. D3); no literature argument.
* *Used by:* the QCD transfer of T2 (item T2(b), §7), T3 (§8) and P4 (§7).
* *Discharge:* OPEN-12.

**`asm:appO-real-jets` (旁观者喷注函数的实性) — proposed \tagP.**

* *Statement:* (REAL) of Def. D3 holds for these jet factors.
* *Status:* exact in the scalar model; argued for perturbative spin-summed leading-power LCOPT jets; open for general hadron wave functions.
* *Used by:* the QCD transfer of T2, T3 and P4.

**`asm:appO-collinear-ends` (共线端点匹配) — proposed \tagA.**

* *Statement:* the SS windows carry the two-sided analytic rapidity regulators of Def. D8. The complements are the $A$-collinear end ($|k^+|\gtrsim K^+$) and the $B$-collinear end ($|k^-|\gtrsim K^-$), together with the cut contributions located there. They are assigned to the collinear regions, where collinear factorization (Wilson lines and subtraction terms) reproduces them with no leftover Hermitian $C_AX$ term (fully coincident pattern) and no leftover $[X_1,X_2]$ term (half-coincident pattern).
* *Status:* open. Supporting evidence: P3; `prop:dy-eikonal-twogluon`; T2′; T3(e). DGOPS §4 removes soft–collinear overlaps by subtraction terms. The SCET argument of Zhou et al. is an EFT form of the statement (§10).
* *Tag:* the subtraction treatment of soft–collinear overlaps is part of the CSS/Collins/DGOPS all-order argument but is not proven in this form; hence \tagA is proposed. With \tagP, the physical readings below remain [P].
* *Effect:* the entry **relocates, rather than removes,** the content of `asm:appO-mixing`(c) for the coincident $O(g^4)$ patterns. What that clause asserts inside the window and near-shell region becomes a matching statement at the collinear ends (OPEN-1, OPEN-6, OPEN-13).

### 2.3 Proposed rewordings of existing entries

* **`asm:appO-envelope`.** For coincident connections, the envelope bound is to be imposed on *side-summed* families. Within the class of P4, the per-graph version cannot hold for coincident pairs (P4). For graph-generated jets the per-graph question is open (OPEN-10).
* **`asm:appO-mixing`(a) → (a′).** Localization is performed *before* the integration over the internal loops of $S$, pointwise outside an exceptional set $E_j$ (L7). Assumed: envelope bounds $C\lambda^aL^K$ (i) for the $S$-loop integral of the absolute localization error, including the factor $\sum_\sigma|w_\sigma(p)|$ when there are several insertions, and (ii) for the unlocalized integrand on $E_j$. These bounds also justify the Fubini interchange.

### 2.4 Local hypotheses, not registered

The precedents are those of ASSUMPTIONS.md §6.

* (SEC) and (EQ): hypotheses of mathematical lemmas, verified in LCOPT, like (ET1)(ET2) of `lem:appO-equal-time`.
* $\mathbb M_{\rm glob}$: a model definition, like the class definition (GC1)–(GC3).
* $\mathcal N_A,\mathcal N_B$: domain definitions for pointwise statements.
* Class $\mathfrak X$: a definition.
* (ADJ) and (REAL): hypotheses of the mathematical statements L8, T2(a), T3 and P4, which concern defined classes. They become registered premises only when applied to QCD jets, as `asm:appO-adjacent-swap` and `asm:appO-real-jets`.

### 2.5 Naming dictionary

The names below replace those used in the earlier versions and in the reviews.

| earlier name | final name |
|---|---|
| (J) | (SEC) |
| (Sp) | (EQ) |
| (Sp′) | (ADJ), and `asm:appO-adjacent-swap` for QCD jets |
| (R) | (REAL), and `asm:appO-real-jets` for QCD jets |
| (H_glob) | the model $\mathbb M_{\rm glob}$ (Def. D4) |
| NF$_X$ | the domain $\mathcal N_X$ (Def. D5) |
| G1 / G2 / G3′ / G4 / G5 / G6 / G7 | `asm:appO-lcopt` / `asm:appO-envelope` (side-summed) / `asm:appO-mixing`(a′) / `asm:appO-mixing`(b) / `asm:appO-mixing`(c) / `asm:appO-deformation` / `asm:appO-collinear-ends` |
| E1–E8 (T2 error terms) | $\mathcal E_1$–$\mathcal E_8$ |
| O1–O12 | OPEN-1–OPEN-12; OPEN-13 is new |
| reference E.18, E.19, E.26, E.28, E.30, E.31, E.33, E.34, E.44, E.48 | `asm:appO-lcopt`, `lem:appO-glauber-pc`, `lem:appO-unitarity`, `lem:appO-equal-time`/`lem:appO-insertion-values`, `def:appO-family`, `prop:appO-ss-cancel`, `asm:appO-mixing`, `asm:appO-envelope`, `asm:appO-deformation`, `lem:appO-joint-localization`(c) and `lem:appO-glauber-operator` |

---

## 3. Localization lemmas

### Lemma L1 (joint localization of $N$ insertions) — [R, R_PT]

*Proposed label:* revision of `lem:appO-joint-localization`. It supplies the proof of its part (b) and corrects (b) for complex poles.

**Hypotheses.**

* $J$ satisfies (SEC) with $N$ insertions.
* $R_e(k)=r_e/(k-z_e)$ for $e=1..N$, with ${\rm Im}\,z_e\ne0$ and $r_e\in\mathbb C$.
* $\mathcal F:=\{e:{\rm Im}\,z_e<0\}$ and $\mathcal B:=\{e:{\rm Im}\,z_e>0\}$.
* Every $i0$ in $J$ is replaced by $i\eta$, $\eta>0$. All statements hold for each $\eta>0$ and in the limit $\eta\to0^+$.

**Statement.**

**(a) Exact form.** The integral converges absolutely, and
$$\int_{\mathbb R^N}\prod_e\frac{dk_e}{2\pi}\,J(k)\prod_eR_e(k_e)=\Big[\prod_{e\in\mathcal F}(-ir_e)\prod_{e\in\mathcal B}(+ir_e)\Big]\sum_{\sigma:\,B_\sigma=\mathcal B}J^{(\sigma)}(z_1,\dots,z_N).$$

**(b) Error bound.** Let $\kappa:=\min|K_l(z)|$ over all contributing sectors ($B_\sigma=\mathcal B$) and all their gaps, and assume $\kappa\ge2\lambda_J$. Then
$$\big|J^{(\sigma)}(z)-\mathcal J_\sigma e_\sigma(z)\big|\le N2^{N+1}M_\sigma\frac{\lambda_J}{\kappa}\prod_l|K_l(z)|^{-1},$$
and hence
$$\Big|\int\cdots-\prod_eR_e(0)\sum_\sigma w_\sigma(z)\mathcal J_\sigma\Big|\le\Big|\prod_eR_e(0)\Big|\,N2^{N+1}\frac{\lambda_J}{\kappa}\sum_\sigma M_\sigma|w_\sigma(z)|,$$
where
$$w_\sigma(z):=\frac{\prod_{e\in\mathcal F}z_e}{\prod_lK^F_l(z)}\cdot\frac{\prod_{e\in\mathcal B}z_e}{\prod_lK^B_l(z)}.$$

**(b1) Closed-quadrant lemma.** If the poles of each group ($\mathcal F$; $\mathcal B$) lie in one closed cone of opening $\pi/2$, then $|w_\sigma|\le1$ for every $\sigma$, and $\sum_\sigma|w_\sigma|\le n_F!\,n_B!\le N!$.

**(b2) Glauber case.** Let $z_e=a_e/(2k_e^+)\mp i0$, with the limit taken after the integration. Within each group the $z_e$ then have one sign, $w_\sigma\in[0,1]$ and $\sum_\sigma w_\sigma=1$. The bound of (b) becomes $|\prod_eR_e(0)|\,N2^{N+1}\max_\sigma M_\sigma\,\lambda_J/\kappa$, with $\kappa\ge\min_ea_e/(2|k_e^+|)$. Under (EQ), relative to the leading term $\prod_eR_e(0)\mathcal J$, the error is therefore $O(m\,\lambda_J|k^+|/a)$.

**(c) Eikonal identity.** $\sum_\sigma w_\sigma=1$. For real poles of one sign in each group, $w_\sigma$ is the probability of an exponential race with rates $|z_e|$:

* in the final group the insertions follow $V_H$ in the order in which the clocks ring, $w_\pi=\prod z/\prod_m\sum_{l\ge m}z_{\pi(l)}$;
* the initial group is time-reversed, $w_\pi=\prod z/\prod_m\sum_{l\le m}z_{\pi(l)}$.

**(d) Rotated contour.** Suppose $N=2$ and the $z_e$ of each group lie on one ray of the imaginary axis. Then, whenever $\kappa\ge\lambda_J$,
$$|J^{(\sigma)}(z)-\mathcal J_\sigma e_\sigma|\le2M_\sigma(\lambda_J/\kappa)\prod_l|K_l|^{-1}.$$

**Proof.**

*Step 1 (absolute convergence).* At finite $\eta$ all denominators are bounded away from zero. By Weinberg's power-counting theorem it suffices that, for every linear subspace $W\subset\mathbb R^N$ along which the variables go to infinity, the number of factors that are not constant on $W$ exceeds $\dim W$.

* At least $\dim W$ of the variables $k_e$ are non-constant on $W$, each contributing a factor $R_e=O(|k_e|^{-1})$.
* The gap function containing the earliest variable non-constant on $W$ contributes one more decaying factor.

*Step 2 (sector selection and residues).*

* *Vanishing sectors.* Take a sector $\sigma$ with some $e\in F_\sigma$ but ${\rm Im}\,z_e>0$. In $J^{(\sigma)}$, $k_e$ enters only final gaps, whose factors $i/(A'-K+i\eta)$ have their $k_e$ poles in the UHP when the other variables are real; $R_e$ also has its pole in the UHP. The integrand is $O(|k_e|^{-2})$, so closing the $k_e$ contour in the LHP gives zero. The case $e\in B_\sigma$ with ${\rm Im}\,z_e<0$ is the mirror image (close in the UHP).
* *Surviving sectors* ($B_\sigma=\mathcal B$). Integrate the final variables one after another, closing in the LHP. If the other final variables have already been set to poles with ${\rm Im}\,z<0$, the pole of $i/(A'-K+i\eta)$ in $k_e$ sits at imaginary part $\eta-{\rm Im}(\text{others})>0$. Only $R_e$ contributes, giving $-ir_eG(z_e)$.
* *Initial variables.* Integrate them closing in the UHP. The initial-gap poles sit at imaginary part $-\eta-{\rm Im}(\text{others})<0$, so only $R_b$ contributes, giving $+ir_bG(z_b)$. This proves (a).

*Step 3 (the bound (b)).* Put $\phi=i/(A\pm K)$ (single-state gap) and $e=i/(\pm K)$. If $|K|\ge2\lambda_J\ge2|A|$, then $|\phi|\le2/|K|$ and $|\phi-e|=|A|/(|K||A\pm K|)\le2\lambda_J/|K|^2\le(2\lambda_J/\kappa)|K|^{-1}$.

* *Single-state terms.* Telescoping over the $N$ gaps, $\prod\phi-\prod e=\sum_m(\prod_{l<m}e_l)(\phi_m-e_m)(\prod_{l>m}\phi_l)$. Each summand is at most $(2\lambda_J/\kappa)2^{N-1}\prod_l|K_l|^{-1}$, so a single-state term is bounded by $N2^N|c_t|(\lambda_J/\kappa)\prod_l|K_l|^{-1}$.
* *Terms with $d_t\ge1$ extra states.* These are entirely error. Their modulus is at most
$$|c_t|2^{N+d_t}\kappa^{-d_t}\prod|K_l|^{-1}=|c_t|\lambda_J^{-d_t}2^{N+d_t}(\lambda_J/\kappa)^{d_t}\prod|K_l|^{-1}\le|c_t|\lambda_J^{-d_t}2^{N+1}(\lambda_J/\kappa)\prod|K_l|^{-1},$$
since $2\lambda_J/\kappa\le1$.
* *Sum.* Summing over $t$ gives the first inequality of (b).
* *Global bound.* Multiply by the prefactor of (a). The modulus of the prefactor times $\prod_l|K_l|^{-1}$ equals $\prod|r_e|/\prod|K_l|=|\prod_eR_e(0)|\,|w_\sigma|$. The leading term reproduces $\prod_eR_e(0)\,w_\sigma\mathcal J_\sigma$, because
$$\prod_F(-ir_f)\prod_B(ir_b)\prod_l(iK^F_l)^{-1}\prod_l(-iK^B_l)^{-1}=\prod_e(-r_e/z_e)\cdot\prod z/\prod K .$$

*Step 4 ((b1), (b2), (c)).*

* *(b1).* For $z_i,z_j$ in a closed cone of opening $\pi/2$, ${\rm Re}(z_i\bar z_j)\ge0$. Hence $|\sum_{l\ge m}z_{\pi(l)}|^2\ge\sum_{l\ge m}|z_{\pi(l)}|^2\ge|z_{\pi(m)}|^2$, and every factor of $w_\pi$ has modulus at most 1. The number of sectors with $B_\sigma=\mathcal B$ is $n_F!\,n_B!$.
* *(c).* Apply the eikonal identity $\sum_\pi\prod_m(\sum_{l\ge m}z_{\pi(l)})^{-1}=\prod_ez_e^{-1}$ to each group. For ${\rm Re}\,z_e>0$ it follows by summing the race integrals $\int_{\mathbb R_+^n}\prod dt_e\,z_e e^{-z_et_e}$ over the ordered regions, which partition $\mathbb R_+^n$. Being a rational identity, it extends to complex $z$ with non-vanishing partial sums.
* *(b2).* For real same-sign poles all partial sums have that sign, so $w_\sigma\in[0,1]$, and (c) gives $\sum w=1$.

*Step 5 ((d)).* For $K$ purely imaginary and $A$ real, $|A+K|=(A^2+|K|^2)^{1/2}\ge\max(|A|,|K|)$. Same-ray sums satisfy $|K_l|\ge\kappa$.

* A single-state gap gives $|\phi|\le1/|K|$ and $|\phi-e|\le\lambda_J/|K|^2$, so the two-gap telescoping gives at most $2(\lambda_J/\kappa)\prod|K_l|^{-1}$.
* A term with $d_t$ extra states is at most $|c_t|\lambda_J^{-d_t}(\lambda_J/\kappa)^{d_t}\prod|K_l|^{-1}\le|c_t|\lambda_J^{-d_t}(\lambda_J/\kappa)\prod|K_l|^{-1}$ for $\kappa\ge\lambda_J$. $\square$

**Verification.**

* `scripts/checks_misc.py` C1a–c: $N=3$ race integrals, with sum 1.
* `scripts/checks_C2_C3_C4.py` C2: $N=3$, all six colour orders, mixed half planes; agreement with exact iterated residues to $10^{-25}$ relative.
* `scripts/test_twoexch_parts2.py`: $N=2$.
* `review_r1_1_scripts/check_L3.py`: covariant jet times exact propagators, 40-digit iterated residues with distinct finite $i\eta$; $5.3\times10^{-14}$ relative at 32 points.
* `review_r1_2_scripts/l1_bruteforce.py`: finite-$\eta$ quadrature with multi-state gaps; agreement $\sim10^{-7}$.
* `fix_r2_scripts/l1_bound_quadrant.py` → `fix_r2_logs/l1_bound_quadrant.log`, ALL PASS:
  * closed-quadrant lemma on 20000 random groups, $\max|w|=0.9995$;
  * corrected bound on 20000 random sectors with arbitrary complex poles, $\max$ lhs/bound $=0.37$;
  * the round-2 counterexample to the uncorrected bound ($N=2$, $z=(1-0.01i,-0.99-0.01i)$): actual relative error 8.86 against the old bound 3.58, with $\sum|w|=44.7$; the corrected bound 160 holds.
* `review_r3_2_scripts/r3_quadrant_P2.py`: groups with both cone edges occupied give $\max|w|=0.9999992$. The condition is sharp: an opening of $\pi/2+0.3$ gives $|w|=1.047$.

**Novelty.** Known: the race formula, which appears in the reference (App E.4.4, as an example) and in `lem:appO-joint-localization`(a); and $\sum w=1$, which is the eikonal identity (App B) and coincides with the sector-sum ("causal") identity of Aybat–Sterman, eq. (10). New: the half-plane sector rule, exactness at finite $\eta$, the bound (b) with the factor $\sum_\sigma|w_\sigma|$, the closed-quadrant lemma (b1), and (d).

**Consequence.** A fixed localization order, as in the deleted clause (c1) of `asm:appO-mixing`, cannot give per-graph weak equivalence for non-commuting coincident insertions whose colour-dressed equal-time values depend on the order. L1 is an exact identity at fixed $k^+$; it is not a per-graph jet-local rewriting (P4).

### Lemma L1′ (multi-pole external factors) — [R, R_PT]

*Proposed label:* `lem:appO-multipole-localization`.

**Hypotheses.**

* (SEC).
* Each $R_e$ is a proper rational function of $k_e$ with simple poles $p\in P_e$, ${\rm Im}\,p\ne0$, and residues $\rho_{e,p}$. Higher-order poles are obtained as limits.

**Statement.**

**(a)** With $s(p)=-i$ for ${\rm Im}\,p<0$ and $s(p)=+i$ for ${\rm Im}\,p>0$,
$$\int\prod_e\frac{dk_e}{2\pi}J\prod_eR_e=\sum_{(p_e)\in\prod_eP_e}\Big[\prod_es(p_e)\rho_{e,p_e}\Big]\sum_{\sigma:\,B_\sigma=\{e:{\rm Im}\,p_e>0\}}J^{(\sigma)}(p_1,\dots,p_N).$$

**(b)** Suppose $|K_l(p)|\ge\kappa\ge2\lambda_J$ for every pole choice and every contributing sector. Then the integral equals
$$\sum_{(p)}\prod_e(-\rho_{e,p_e}/p_e)\sum_\sigma w_\sigma(p)\mathcal J_\sigma+{\rm Err},$$
with
$$|{\rm Err}|\le N2^{N+1}\frac{\lambda_J}{\kappa}\sum_{(p)}\prod_e|\rho_{e,p_e}/p_e|\sum_\sigma M_\sigma|w_\sigma(p)|.$$
If the closed-quadrant condition holds for every pole choice, $\sum_\sigma|w_\sigma(p)|\le N!$, and then $|{\rm Err}|\le N!\,N2^{N+1}\max_\sigma M_\sigma\,(\lambda_J/\kappa)\prod_e\|R_e\|$ with $\|R_e\|:=\sum_p|\rho_{e,p}/p|$. The uncorrected form, without the factor $\sum_\sigma|w_\sigma|$, holds only when $\sum_\sigma|w_\sigma(p)|\le1$ for every pole choice.

**(c)** For each pole choice, $\sum_p(-\rho_{e,p}/p)=R_e(0)$ and $\sum_\sigma w_\sigma(p)=1$. If all $\mathcal J_\sigma$ are equal, the leading term is $\mathcal J\prod_eR_e(0)$. For $N=1$, (b) is `lem:appO-equal-time`(iii) (reference Lemma E.28(iii)).

**Proof.**

* Partial fractions give $R_e=\sum_p\rho_{e,p}/(k-p)$, with no polynomial part since $R_e$ is proper.
* The integral is multilinear in the $R_e$, so L1(a),(b) apply to each pole choice; L1 uses no relation between $r_e$ and $z_e$.
* For (c): $R_e(0)=\sum_p\rho_{e,p}/(-p)$, and L1(c) gives $\sum_\sigma w_\sigma=1$. $\square$

**Example (even Lorentzian regulator; used in T3(e) and T2′(c)).** The factor $R_e(k)\chi_K(k)$ has poles at $z_e$, at $+iK$ (initial) and at $-iK$ (final). Its normalized pole weights $u_e(p):=(-\rho_{e,p}/p)/R_e(0)$ are
$$u_z=\frac{K^2}{z_e^2+K^2},\qquad u_+=\frac{z_e}{2(z_e-iK)},\qquad u_-=\frac{z_e}{2(z_e+iK)},\qquad u_z+u_++u_-=1.$$

* *Closed quadrants.* On the contour $k^+=e^{i\theta}x$ with $\theta\in[0,\pi/2]$, $z_e=(a_e/2|x_e|)e^{-i\theta}{\rm sgn}(x_e)$. The final group $\{z_e:x_e>0\}\cup\{-iK\}$ lies in the closed fourth quadrant, and the initial group $\{z_e:x_e<0\}\cup\{+iK\}$ in the closed second quadrant. So (b) holds with $\sum_\sigma|w_\sigma|\le2$ for $N=2$.
* *Pole collision.* At $\theta=\pi/2$ the poles $z_e$ and $\mp iK$ can coincide. The numerics therefore use $\theta\le\pi/4$.
* *Constant.* On the $\pi/4$ rays, $\sum_p|u_e(p)|\le c_U:=1.6485$.
* *Limits.* For $|z_e|\ll K$ the race weights are recovered. For $|z_e|\gg K$ both regulator poles carry weight $\tfrac12$; this is the strict-Glauber limit of P2.

**Verification.**

* The sum rule symbolically (`review_r2_1_scripts/symbolic_checks_r2.py`).
* The $K\to\infty$ limit (`fix_r1_logs/regulator_indep_A.log`).
* $c_U=1.6485$ (`fix_r2_logs/t3e_sensitivity.log`), reproduced as 1.64853 by both round-3 reviewers.

**Novelty:** new (elementary).

### Lemma L2 (the weights as functions of $k^+$) — [R, R_PT]

*Proposed:* consequence item of `lem:appO-joint-localization`.

**Hypotheses.** Glauber factors $z_e=a_e/(2k_e^+)\mp i0$. Put $W_\pi(k^+):=\sum_{\sigma\text{ of colour order }\pi}w_\sigma$.

**Statement.**

* (a) $W_\pi$ is homogeneous of degree 0 and rational in each orthant.
* (b) $W_\pi$ is continuous wherever at most one $k_e^+$ vanishes. As $k_e^+\to0^\pm$, $|z_e|\to\infty$ and $e$ moves next to $V_H$: it becomes the first final insertion from one side and the last initial insertion from the other, i.e. the same colour position. Under (EQ) the localized value $\sum_\sigma w_\sigma\mathcal J_\sigma$ is continuous there as well.
* (c) $W_\pi$ is not analytic across $k_e^+=0$. Example ($N=2$, $k_2^+>0$): $W_{(12)}=1-a_2k_1^+/(a_1k_2^+)+\dots$ as $k_1^+\to0^+$, but $W_{(12)}\equiv1$ for $k_1^+<0$.
* (d) $W_\pi$ is discontinuous where two or more components vanish; the limits depend on the direction.
* (e) For an insertion on an active line emitted by $V_H$ ($\mathcal J_-=0$), the weight is $\theta(k_e^+)$.

Two-line formulas:
$$W^{[12]}=\frac{a_1k_2^+}{a_1k_2^++a_2k_1^+}\ \text{in }(+,+),\qquad\frac{a_2k_1^+}{a_2k_1^++a_1k_2^+}\ \text{in }(-,-),\qquad1\ \text{in }(-,+),\qquad0\ \text{in }(+,-).$$

**Proof.** Immediate from L1(c). $\square$

**Verification.** `scripts/checks_misc.py` C1d, C1e. Re-derived independently by reviewers in rounds 1–3.

**Physical caveat.** $W_\pi(k^+)$ is the equal-time asymptotics of the sector functions of $J_A$ at the gluon-pole positions $k_e^-=z_e$. For $|k^+|\sim\lambda_B$ these lie at $|k^-|\sim a/\lambda_B$, outside the domain of `lem:appO-glauber-pc`(b). L2 is exact for the localized integrand; physical use needs $\mathbb M_{\rm glob}$ or `asm:appO-collinear-ends`.

**Novelty.** New. It corrects the wording of REFDOC_ANALYSIS ERR-S3, which said that coincident weights are non-analytic "exactly like $\theta(k^+)$": for spectators they are continuous, with a kink.

### Lemma L3 (exact $k^-$ residues for two SS lines: quadrant formulas) — [R, R_PT]

*Proposed label:* `lem:appO-quadrant-residues`.

**Statement.** This is L1 with $N=2$. In the quadrant $Q=({\rm sgn}\,k_1^+,{\rm sgn}\,k_2^+)$,
$$F_A^{[\pi]}(k^+)=\prod_e\big(-i\,{\rm sgn}(k_e^+)\,r_e\big)\,J_A^{(\sigma(\pi,Q))}(z_1,z_2),$$
where $\sigma(\pi,Q)$ is the sector with initial set $\{e:k_e^+<0\}$ and colour order $\pi$.

* *Incompatible orders.* $F_A^{[\pi]}=0$ if $\pi$ is incompatible with $Q$: the quadrant $(+,-)$ kills $[12]$ and $(-,+)$ kills $[21]$.
* *Mixed quadrant.* In $(-,+)$, $\prod(\cdots)=1/(4k_1^+k_2^+)$, so $F_A^{[12]}(-k,k)=-\frac{1}{4k^2}J_A^{(1V2)}(z_1,z_2)$ with $z_1=-a_1/(2k)$ and $z_2=a_2/(2k)$.
* *Localized regime.* For $|z_e|\ge2\lambda_A$,
$$F_A^{[\pi]}=\frac{\mathcal J_A}{a_1a_2}\,w^{[\pi]}(k^+)\,[1+O(\lambda_A|k^+|/a)]\quad\text{(under (EQ))}.$$
* *Holomorphy.* Each quadrant piece extends holomorphically to $\{{\rm Im}\,z_e<0$ for final $e$, ${\rm Im}\,z_e>0$ for initial $e\}$: the UHP in $k_e^+$ for $k_e^+>0$ and the LHP for $k_e^+<0$.

**Proof.** L1(a),(b) with the sign rule of Step 2. $\square$

**Verification.**

* `scripts/test_twoexch_parts2.py`.
* `review_r1_1_scripts/check_L3.py` ($5.3\times10^{-14}$ at 32 points).
* The round-2 real-contour codes (`review_r2_1_scripts/t2c_realcontour_r2.py`, `t3_realcontour_r2.py`) use this quadrant structure and agree with the rotated-contour results to $\sim10^{-6}$.

**Novelty:** new (an explicit instance).

### Lemma L7 (pre-integration localization for far-off-shell soft lines) — (a),(b) [R, R_PT]

*Proposed label:* `lem:appO-preintegration-localization`. Its item (c) is the reformulation (a′) of `asm:appO-mixing`(a), §2.3.

**Hypotheses.**

* $j$ is a localizable endpoint on a spectator whose soft line ends on an internal vertex of the soft subgraph $S$.
* The $S$-loop momenta $l_S$ and all other variables are fixed and real, and $k_j^+\ne0$.
* Every internal line $l$ of $S$ whose momentum depends on $k_j^-$, written $l=l_0+\epsilon_lk_j$ with $\epsilon_l=\pm1$ and $l^+=l_0^++\epsilon_lk_j^+$, satisfies $|l^2(0)-m_l^2|\ge4|l^+|\Lambda_j$ at $k_j^-=0$. The connecting line satisfies the same.
* $R_j(\cdot;l_S)$ is proper in $k_j^-$, which holds for leading-power numerators.

**Statement.**

**(a)** At fixed $l_S$, $R_j(\cdot;l_S)$ is a proper rational function of $k_j^-$ whose poles all lie at distance $\ge2\Lambda_j$ from 0. On $|k_j^-|<\Lambda_j$ it is holomorphic and bounded by $2^{n_j}$ times the product of the moduli of its factors at $k_j^-=0$ (times the numerator bound). Here $n_j$ is the number of $k_j^-$-dependent denominators.

**(b)** At fixed $l_S$:

* For **one** localizable insertion, `lem:appO-equal-time`(iii) applies in $k_j^-$ with absolute error $O(M\lambda_J\|R_j(\cdot;l_S)\|/\Lambda_j)$, where $\|R_j\|=\sum_p|\rho_p/p|$; no extra factor appears.
* For **several** insertions, L1′(b) applies with the factor $\sum_\sigma|w_\sigma(p)|$. This factor is bounded by $N!$ if the soft-line poles of each group lie in a closed quadrant (L1(b1)). Soft-line poles in one group can have opposite real parts, and then the factor is not bounded in general.

**(c)** What this gives:

* Localization before the $l_S$ integration, pointwise outside the exceptional set $E_j:=\{l_S:\text{some soft line carrying }k_j\text{ has }|l^2-m^2|<4|l^+|\Lambda_j\}$, with $\Lambda_j=\lambda^{-a'}\nu_A$.
* It does **not** prove `asm:appO-mixing`(a). That clause concerns $R_j$ after the $l_S$ integration, where $R_j$ has cuts and the half-plane splitting $R_{j\downarrow}+R_{j\uparrow}$ with bounds is required. Instead, (a) is replaced by (a′).
* The Fubini interchange is justified at finite $\eta$ by absolute integrability. The limit $\eta\to0$ is controlled only through the envelope bounds of (a′).

**Proof.**

* *(a).* $l^2-m^2$ is affine in $k_j^-$ with slope $2\epsilon_ll^+$. Its zero lies at distance $|l^2(0)-m^2|/(2|l^+|)\ge2\Lambda_j$. On $|k_j^-|<\Lambda_j$, $|l^2-m^2|\ge|l^2(0)-m^2|-2|l^+|\Lambda_j\ge\tfrac12|l^2(0)-m^2|$.
* *(b).* `lem:appO-equal-time`(iii) for one insertion, and L1′(b) for several. $\square$

**Novelty:** elementary; new as a pre-integration replacement of `asm:appO-mixing`(a).

---

## 4. Contour rotation, ray identity, two-insertion jets

### Lemma L5 (rotation of the $k^+$ contour) — [R, R_PT]

*Proposed label:* `lem:appO-kplus-rotation`.

**Hypotheses.** The model $\mathbb M_{\rm glob}$ for two SS lines. $J_A$ and $J_B$ satisfy (SEC). The configuration lies on $\mathcal N_B$. No condition on the final energies of $J_A$ is needed.

**Statement.** For each colour pair and every $\theta\in[0,\pi/2]$,
$$I(\pi_A,\pi_B)=e^{2i\theta}\int\frac{d^2\kappa}{(2\pi)^2}F_A^{[\pi_A]}(e^{i\theta}\kappa)\,J_B^{[\pi_B]}(-e^{i\theta}\kappa),$$
with each quadrant piece of $F_A$ continued analytically from its real quadrant. At $\theta=\pi/2$,
$$I=-\int\frac{d^2\kappa}{(2\pi)^2}F_A(i\kappa)J_B(-i\kappa).$$
The same holds with class-$\mathfrak X$ regulators on $k^+$, and with rational regulators on the $A$-side $k^-$ (L1′).

**Proof.**

*Step 1 (holomorphy).* Fix $\eta>0$. For each real quadrant $Q$, set $G_Q(u):=F_A^Q(u)J_B^{[\pi_B]}(-u)$ and let $D_Q:=\{e^{it}x:x\in Q,\ t\in[0,\pi/2]\}$ be the swept set. Then $G_Q$ is holomorphic on $D_Q$.

* *$F_A$:* by L3, $z_e=a_e/(2u_e)$ has ${\rm Im}\,z_e\le0$ for $x_e>0$ and $\ge0$ for $x_e<0$ on $D_Q$. Initial gaps $A+K^B+i\eta$ therefore have imaginary part $\ge\eta$, and final gaps $A'-K^F+i\eta$ have imaginary part $\ge\eta$; neither vanishes.
* *$J_B$, initial factors:* with $p=-e^{it}x$, an initial factor is $A+p+i\eta$ with $A<0$. A zero would need $e^{it}X=A+i\eta$, which lies in the second quadrant, while $e^{it}X$ sweeps the first and third quadrants.
* *$J_B$, final factors:* a final factor is $A'-p+i\eta$. A zero would need $e^{it}X=-A'-i\eta$, which lies in the fourth quadrant when $A'<0$ (domain $\mathcal N_B$).

*Step 2 (radial identity).* For $G$ holomorphic on $D_Q$,
$$\frac{d}{dt}\big[e^{2it}G(e^{it}\kappa)\big]=ie^{2it}\Big[2G+\sum_eu_e\partial_{u_e}G\Big]_{u=e^{it}\kappa}=i\,{\rm div}_\kappa\big(\kappa\,e^{2it}G(e^{it}\kappa)\big),$$
because ${\rm div}_\kappa(\kappa G(e^{it}\kappa))=2G+\sum_eu_e\partial_{u_e}G$ (Euler's relation). Integrate over $Q\cap\{\rho<|\kappa|<R\}$ and apply the divergence theorem. The outward normal $n$ satisfies $\kappa\cdot n=0$ on the two half-axes bounding $Q$, so only the arcs $|\kappa|=\rho$ and $|\kappa|=R$ contribute:
$$\Big|\frac{d}{dt}I_Q(t)\Big|\le R^2\int_{\rm arc}|G(e^{it}Re^{i\varphi})|\,d\varphi+\rho^2\int_{\rm arc}|G(e^{it}\rho e^{i\varphi})|\,d\varphi .$$

*Step 3 (arcs, at fixed $\eta>0$ and uniformly in $t$).*

* *Inner arc.* $G$ is bounded near the origin: $F_A$ tends to the localized weights and $J_B$ is bounded. The inner arc is therefore $O(\rho^2)$.
* *Bounds on $J_B$ on $D_Q$.* Each gap factor of $J_B$ is continuous and non-vanishing on $D_Q$ and grows linearly, so it is bounded below by $c_\eta(1+|y|)$, where $y$ is the corresponding sum of the $x$'s. Hence $|J_B^{(\sigma)}|\le C_\eta\prod_l(1+|y_l|)^{-1}$.
* *Bounds on $F_A$ on $D_Q$.* The gap factors of $J_A$ have imaginary part $\ge\eta$, so $|F_A|\le C_\eta/(|u_1||u_2|)$ where both $|u_e|\sim R$. Near an axis ($|u_1|\lesssim1$) one has $J_A^{(\sigma)}(z)\sim1/z_1\sim u_1$, so $F_A=O(R^{-1})$ there.
* *Outer arc, region by region:*
  * generic region: $R^2\cdot R^{-2}\cdot R^{-2}=O(R^{-2})$;
  * strip $|\kappa_P|\lesssim1$: $R^2\int(d\kappa_P/R)\,R^{-2}(R(1+|\kappa_P|))^{-1}=O(R^{-2}\ln R)$;
  * axis bands $|\kappa_1|\lesssim1$: $R^2\int(d\kappa_1/R)\,R^{-1}(R(1+|\kappa_1|))^{-1}=O(R^{-1}\ln R)$.

Hence $I_Q(\theta)=I_Q(0)$ for every $\theta\in[0,\pi/2]$. Only the crude bounds of (SEC) are used here; no cancellation is needed.

*Step 4 ($\eta\to0$ at $\theta=\pi/2$).* For $\eta\le\mu_B$, $|A+i(\eta-y)|\ge\langle y\rangle/\sqrt5$. Indeed, if $|y|\le2\mu$ the modulus is at least $|A|\ge\mu\ge\langle y\rangle/\sqrt5$; if $|y|>2\mu$ it is at least $|y|/2\ge\langle y\rangle/\sqrt5$. Together with the rotated L1 bounds for $F_A$ (decay $O(R^{-2})$, and $O(R^{-1})$ near the axes), $|F_AJ_B|$ is dominated by an integrable function uniformly in $\eta$. Dominated convergence applies. At $\theta=0$, the limit $\eta\to0$ defines $I$. $\square$

*Remarks.*

1. The range is $\theta\le\pi/2$: at $t=\pi$ an initial factor $A-e^{i\pi}x$ vanishes at $x=-A>0$.
2. With a rational $A$-side $k^-$ regulator, individual pole terms of L1′ can have cancelling singularities at $\theta=\pi/2$ (pole collision $z_e=\mp iK$). $F_A^{\rm reg}$ is nevertheless holomorphic, because $z_e$ never crosses the real $k^-$ axis. The numerics use $\theta\le\pi/4$.

**Verification.**

* Rotated contour versus real contour (`scripts/twoexch_rotated_fast2.py` vs `scripts/twoexch_exact.py`): 7–10 digits at $\lambda=1$ and $\lambda=0.01$, and $|\Delta p_{\rm opp}|\le10^{-5}$ at $\lambda=0.001$.
* Independence of $\theta$: $\theta=\pi/8,\pi/4,3\pi/8$ agree to 8 digits (`review_r1_2_logs/t3_theta_check.log`, `fix_r1_logs/regulator_indep_A.log`, `final_logs/t3f_recompute.log`).
* Round-2 real-contour codes, with no rotation at all, agree with the rotated values to $\sim10^{-6}$.
* A naive polar grid cannot resolve the strip: `logs/twoexch_rotated_fast_0.01.log` gives $p_{\rm opp}=0.174$ instead of $0.0123$.

**Novelty:** new.

### Lemma L6 (ray identity) — [R, R_PT]

*Proposed label:* `lem:appO-ray-identity`.

**Hypotheses.**

* $\rho$ is holomorphic in $0<\arg k<\pi/2$.
* It is continuous up to the boundary, except for finitely many simple poles $k_p$ on the positive real axis, where the boundary values $\rho(k+i0)$ are taken.
* $|\rho(k)-1|\le C|k|/k_1$ for $|k|\le k_1$, and $|\rho(k)|\le Ck_2/|k|$ for $|k|\ge k_2$, in the closed quadrant.

**Statement.**
$$\int_0^\infty\frac{d\kappa}{\kappa}\,{\rm Im}\,\rho(i\kappa)=-\frac\pi2+{\rm Im}\int_0^\infty\frac{dk}{k}\,\rho(k+i0).$$
If $\rho$ is real on the positive axis away from its poles, with real residues, this equals $-\frac\pi2-\pi\sum_p{\rm Res}_{k_p}\rho/k_p$. Without poles it is exactly $-\pi/2$.

**Proof.** Put $f(k):=[\rho(k)-(1+k)^{-1}]/k$. It is holomorphic in the quadrant, $O(1)$ at 0 and $O(|k|^{-2})$ at $\infty$. Apply Cauchy's theorem on the boundary of the quadrant, indenting the axis poles from inside; the arcs at 0 and $\infty$ vanish. This gives
$$\int_0^\infty[\rho(i\kappa)-(1+i\kappa)^{-1}]\frac{d\kappa}{\kappa}=\int_0^\infty[\rho(k+i0)-(1+k)^{-1}]\frac{dk}{k}.$$
Take imaginary parts and use $\int_0^\infty\frac{d\kappa}{\kappa}{\rm Im}(1+i\kappa)^{-1}=-\int_0^\infty\frac{d\kappa}{1+\kappa^2}=-\frac\pi2$. Near $k_p$, ${\rm Im}\,\rho(k+i0)={\rm Res}_{k_p}\rho\cdot(-\pi)\delta(k-k_p)+$ (a real part). $\square$

**Verification.**

* `scripts/checks_C2_C3_C4.py` C4: 8 random rational $\rho$, including axis poles; agreement $10^{-15}$.
* `review_r1_1_scripts/check_L6.py`: agreement $<2\times10^{-17}$.
* Re-derived by reviewers in rounds 1–3.

**Novelty:** elementary; only its role in T2 and T2′ is new.

### Lemma L8 (two-insertion jets on the rotated contour) — [R, R_PT]

*Proposed label:* `lem:appO-two-insertion-bounds`.

**Hypotheses.**

* $J$ satisfies (SEC) with $N=2$ insertions, of energies $p_1,p_2$, and $P:=p_1+p_2$.
* $J$ satisfies (EQ) and (ADJ).
* All final energies of $J$ are negative (domain $\mathcal N$).

**Notation** (at $\theta=\pi/2$).

* $p_e=-i\kappa_e$; $\lambda:=\lambda_J$ and $\mu:=\mu_J$; $\langle y\rangle=(\mu^2+y^2)^{1/2}$.
* $f_\pi(\kappa):=J^{[\pi]}(-i\kappa)$ and $S:=f_{12}+f_{21}$.
* The sectors of colour order $[12]$: $BB=(12|)$, with gaps $p_1$ (initial) and $P$ (initial); $BF=(1|2)$, with gaps $p_1$ (initial) and $p_2$ (final); $FF=(|12)$, with gaps $P$ (final) and $p_2$ (final). For $[21]$, exchange the labels.

**Statement.**

**(a)** For $K=-iy$: $|i/(A+K)|\le1/\langle y\rangle$ and $|i/(A+K)-i/K|\le\lambda/(|y|\langle y\rangle)$. The same holds for final factors $i/(A'-K)$.

**(b)** $|J^{(\sigma)}|\le M^\flat_\sigma/(\langle y_1\rangle\langle y_2\rangle)$, where $y_1,y_2$ are the gap momenta of $\sigma$.

**(c) Off-strip.** If $R\ge4\lambda$ and $r_P\ge R/4$, then $|f_\pi|\le400\,M^\flat\lambda/(R^2\langle\min(r_1,r_2)\rangle)$.

**(d) Strip.** If $R\ge4\lambda$ and $r_P<R/4$, then
$$f_{12}=g(-i\kappa_P)/\kappa_2+E_{12},\qquad f_{21}=-g(-i\kappa_P)/\kappa_2+E_{21},\qquad|E_\pi|\le16\,M^\flat\lambda/(R^2\langle r_P\rangle),$$
where
$$g(P):=\sum_{t\in BB,\ \text{single-state first gap}}c_t\phi^t_2(P)+\sum_{t\in FF,\ \text{single-state second gap}}c_t\phi^t_1(P).$$
By (ADJ) for the adjacent pair (1,2), the same expression built from $[21]$ gives the same $g$.

**(e)** $|g(-iU)|\le\min(2M^\flat/\langle U\rangle,\ 4M\lambda/U^2)$, and $\int_{\mathbb R}g(-iU)\,dU/(2\pi)=-i\mathcal J$.

**(f)** $S\in L^1(\mathbb R^2)$, and $\int S\,d^2\kappa/(2\pi)^2=-\mathcal J$. On the contour $p=-e^{i\theta}\kappa$ the value is $e^{-2i\theta}\mathcal J$.

**(g) Integrated bounds.** For $K\ge4\lambda$ and $l:=\ln(1+4K/\mu)$:

* $\int_{R\le K}|f_\pi|\,d^2\kappa\le12M^\flat l^2$;
* $\int_{R>K,\,r_P\ge R/4}|f_\pi|\le3200M^\flat(\lambda/K)(1+l)$;
* $\int_{R>K,\,r_P<R/4}|E_\pi|\le86M^\flat(\lambda/K)(1+l)$;
* hence $\big|\int_{R>K}S\big|\le6600M^\flat(\lambda/K)(1+l)$.

**(h) The $\pi/4$ contour.** On $p=-e^{i\pi/4}\kappa$, (a) holds with $2/\langle y\rangle$ and $2\lambda/(|y|\langle y\rangle)$, and (b)–(g) hold with every constant multiplied by 8, and with $e^{-2i\theta}$ and $1/(ip_2)$ in place of $-1$ and $1/\kappa_2$.

**Proof.**

*(a).* $|A-iy|=(A^2+y^2)^{1/2}\ge\langle y\rangle$, and $i/(A+K)-i/K=-iA/(K(A+K))$.

*(b).* A gap with $n$ states is bounded by $\langle y\rangle^{-1}\prod_{j\ge2}|A_j-iy|^{-1}\le\mu^{-(n-1)}/\langle y\rangle$.

*(c), generic case* ($r_1,r_2,r_P\ge R/4$). All gap momenta satisfy $|y|\ge R/4\ge\lambda$.

* A single-state term has telescoping error at most $\lambda[y_1^{-2}|y_2|^{-1}+|y_1|^{-1}y_2^{-2}]\le128\lambda/R^3$.
* A term with $d_t\ge1$ is at most $|c_t|(4/R)^{2+d_t}\le|c_t|\lambda^{-d_t}(4\lambda/R)^{d_t}(16/R^2)\le|c_t|\lambda^{-d_t}\,64\lambda/R^3$.
* Hence $|J^{(\sigma)}-\mathcal J e_\sigma|\le128M_\sigma\lambda/R^3$.
* The eikonal products cancel in the sector sum, by (EQ):
$$\mathcal J\Big[-\frac{1}{p_1P}+\frac{1}{p_1p_2}-\frac{1}{Pp_2}\Big]=\mathcal J\,\frac{-p_2+P-p_1}{p_1p_2P}=0 .$$
* So $|f_{12}|\le384M\lambda/R^3$. Finally $\langle\min r\rangle\le\sqrt{17/16}\,R$, which gives $384M\lambda/R^3\le400M^\flat\lambda/(R^2\langle\min r\rangle)$.

*(c), axis band $r_1<R/4$.* Then $r_2=R$ and $r_P\ge3R/4$, and the eikonal approximation fails only in the gap $p_1$, which is shared by $BB$ and $BF$.

* *Pairing.* $BB=(1,2,V_H)$ and $BF=(1,V_H,2)$ differ only by the order of the adjacent operations (2, $V_H$). By (ADJ), the terms with a single-state gap between them correspond: $BB$'s second gap $i/(A_t+P)$ corresponds to $BF$'s final gap $i/(A'_t-p_2)$, with equal $c_t$ and equal first gap $\phi^t_1(p_1)$. Hence
$$BB_s+BF_s=\sum_tc_t\phi^t_1(p_1)\Big[\frac{i}{A_t+P}+\frac{i}{A'_t-p_2}\Big]=-\frac{i}{Pp_2}\sum_tc_tp_1\phi^t_1(p_1)+\sum_tc_t\phi^t_1(p_1)\delta_t,$$
using $i/P-i/p_2=-ip_1/(Pp_2)$. Here $|\delta_t|\le\lambda/y_P^2+\lambda/y_2^2\le(16/9+1)\lambda/R^2$.
* *The sum $\sum c_tp_1\phi^t_1$.* For a single-state first gap, $p_1\cdot i/(A+p_1)=i-iA/(A+p_1)$. For an $n$-state first gap, $|p_1\phi|\le\mu^{-(n-1)}\lambda/\langle\kappa_1\rangle$, using $|A+p|\ge|p|$. Hence $\sum_tc_tp_1\phi^t_1=i\mathcal J_{BB}+O(M^\flat\lambda/\langle r_1\rangle)$.
* *Remaining pieces of $BB$ and $BF$:*
  * the leading term gives $\mathcal J_{BB}/(Pp_2)$, with error at most $\frac43M^\flat\lambda/(R^2\langle r_1\rangle)$;
  * the $\delta_t$ piece is at most $\frac{25}{9}M^\flat\lambda/(R^2\langle r_1\rangle)$;
  * multi-state second gaps of $BB$ and $BF$ add at most $(\frac{16}9+1)M^\flat\lambda/(R^2\langle r_1\rangle)$. (The round-2 text had 2 here; the correct value is $16/9+1\approx2.78$.)
* *$FF$.* Both gaps are $\ge3R/4$, so $FF=-\mathcal J_{FF}/(Pp_2)+O(3.2M\lambda/R^3)$, and $M\lambda/R^3\le0.36M^\flat\lambda/(R^2\langle r_1\rangle)$ because $\langle r_1\rangle\le0.36R$ in the band.
* *Total.* The leading terms $(\mathcal J_{BB}-\mathcal J_{FF})/(Pp_2)$ cancel by (EQ). The remainder is at most $(1.34+2.78+2.78+1.15)M^\flat\lambda/(R^2\langle r_1\rangle)\le9M^\flat\lambda/(R^2\langle r_1\rangle)$.
* *The band $r_2<R/4$* is treated the same way, pairing $BF$ with $FF$ through (ADJ) for the adjacent pair (1, $V_H$), whose shared gap is $p_2$.

*(d), strip.* Here $r_1,r_2\ge3R/4$ and $|p_1|,|p_2|\ge3R/4$.

* *$BB$, single-state first gap.* Write
$$\frac{i}{A_t+p_1}=-\frac{i}{p_2}+\frac{i(P+A_t)}{(A_t+p_1)p_2}.$$
The first piece produces $-(i/p_2)\times$ [the $BB$ part of $g$].
* *$FF$, single-state second gap.* Write $i/(A'_t-p_2)=-i/p_2+iA'_t/((A'_t-p_2)p_2)$, which produces $-(i/p_2)\times$ [the $FF$ part of $g$]. Since $-i/p_2=1/\kappa_2$, together these give $g/\kappa_2$.
* *Error pieces.* $E_{12}$ is the sum of five pieces:
  * (i) the $FF$ remainder $\sum c_t\phi^t_1(P)\,iA'_t/((A'_t-p_2)p_2)$, at most $\frac{16}{9}M^\flat\lambda/(R^2\langle r_P\rangle)$;
  * (ii) multi-state first gaps of $BB$;
  * (iii) multi-state second gaps of $FF$; each of (ii), (iii) is at most $\frac{16}{9}M^\flat\lambda/(R^2\langle r_P\rangle)$;
  * (iv) the second $BB$ piece, rewritten with $1/(A_t+p_1)=1/p_1-A_t/(p_1(A_t+p_1))$ as $(i/(p_1p_2))\Gamma(P)$ plus a remainder at most $1.8M^\flat\lambda/(R^2\langle r_P\rangle)$, where
  $$\Gamma(P):=\sum_tc_t\phi^t_2(P)(P+A_t)=i\mathcal J_{BB}+O(2M^\flat\lambda/\langle r_P\rangle);$$
  * (v) $BF=\mathcal J_{BF}/(p_1p_2)+O(4.8M\lambda/R^3)$.
* *Cancellation.* The leading terms $(-\mathcal J_{BB}+\mathcal J_{BF})/(p_1p_2)$ cancel by (EQ). The total is at most $13.2M^\flat\lambda/(R^2\langle r_P\rangle)\le16M^\flat\lambda/(R^2\langle r_P\rangle)$.
* *$f_{21}$.* For $[21]$ the roles of $BB$ and $FF$ are exchanged.
  * $BB'=(2,1|)$ has first gap $p_2$, so $i/(A_t+p_2)=i/p_2-iA_t/(p_2(A_t+p_2))$ gives $(i/p_2)\times$[the $BB'$ part of $g^{[21]}$] directly. The remainder is at most $\frac{16}{9}M^\flat\lambda/(R^2\langle r_P\rangle)$.
  * $FF'=(|2,1)$ has second gap $p_1$, and $i/(A'_t-p_1)=i/p_2+i(P-A'_t)/((A'_t-p_1)p_2)$. This produces $(i/p_2)\times$[the $FF'$ part], plus a term that, through $\Gamma'(P):=\sum_tc_t\phi^t_1(P)(P-A'_t)=-i\mathcal J_{FF}+O(2M^\flat\lambda/\langle r_P\rangle)$, cancels against $BF'=\mathcal J_{BF}/(p_1p_2)+O(4.8M\lambda/R^3)$ by (EQ).
  * Since $i/p_2=-1/\kappa_2$, $f_{21}=-g^{[21]}(-i\kappa_P)/\kappa_2+E_{21}$, with the same bound.
  * Finally $g^{[12]}=g^{[21]}$ by (ADJ) for the adjacent pair (1,2), within $BB$ and within $FF$.

*(e).*

* *Pointwise.* Each term of $g$ is at most $\mu^{-(n-1)}/\langle U\rangle$, giving $2M^\flat/\langle U\rangle$. For $|U|\ge\lambda$ the $1/P$ parts are $(i/P)(\mathcal J_{BB}-\mathcal J_{FF})=0$ by (EQ), and the remainders give $4M\lambda/U^2$.
* *Real-axis integral.* On the real $P$ axis, $g=O(P^{-2})$. Close the contour in the UHP. Only the final-gap factors $i/(A'-P+i0)$ of $FF$ have poles there; multi-state gaps have zero total residue. This gives $\int g\,dP/(2\pi)=\mathcal J_{FF}=\mathcal J$.
* *Rotation.* With $P=-iU$, $\int_{\mathbb R}g(-iU)dU=-i\int_{-i\infty}^{i\infty}g(P)dP$. The upward imaginary axis is the real axis rotated counterclockwise by $\pi/2$, sweeping the first and third quadrants. The poles of $g$ lie in the second quadrant ($FF$: $P=A'+i0$ with $A'<0$) and in the fourth ($BB$: $P=-B-i0$ with $B<0$), and $|g|=O(P^{-2})$ on the arcs. Hence $\int_{-i\infty}^{i\infty}g\,dP=2\pi\mathcal J$.

*(f).*

* *$L^1$.* $S\in L^1(\mathbb R^2)$ by (b)–(d), since the $g$ terms cancel in $S$.
* *Value on the real plane.* Work at finite $\eta$ and insert $\chi_\Lambda(p_1)\chi_\Lambda(p_2)$, $\chi_\Lambda(p)=\Lambda^2/(p^2+\Lambda^2)$. Its poles $\pm i\Lambda$ have normalized weights $\tfrac12$ each and give gap momenta of modulus $\ge\Lambda$. By L1′, in the closed-quadrant case with $\sum|w|\le2$, and since all $\mathcal J_\sigma$ in $S$ are equal by (EQ), the integral equals $\mathcal J+O(M\lambda/\Lambda)$.
* *Limit $\Lambda\to\infty$.* The real-plane analogues of (b)–(d) hold at finite $\eta$ with $\eta$-dependent constants, because the cancellations used are algebraic. So $S\in L^1(\mathbb R^2)$ at finite $\eta$, and dominated convergence applies.
* *Rotation.* Rotate as in L5. $S(-e^{it}x)$ is holomorphic on all of $\mathbb R^2$ for $t\in[0,\pi/2]$ (Step 1 of L5 applied to its factors), and the arcs vanish because $S$ has no $1/R$ strip tail.
* *Limit $\eta\to0$.* Let $\eta\to0$, dominated by (b)–(d) with constants multiplied by a bounded factor for $\eta\le\mu$, by the inequality of L5, Step 4.
* *Orientation.* $d^2p=-d^2\kappa$ at $\theta=\pi/2$.

*(g).* Integrate (b)–(d), using linear changes of variables of unit Jacobian to the gap momenta, together with

* $\int_{-X}^X dy/\langle y\rangle=2\,{\rm asinh}(X/\mu)\le2\ln(1+2X/\mu)$;
* $\int_X^\infty\ln(1+cR)R^{-2}dR\le(1+\ln(1+cX))/X$.

The first bound: the region $R\le K$ maps into $|y_e|\le2K$, giving $4M^\flat l^2$ per sector. The third: in the strip $|\kappa_2|\ge3R/4$ and $|\kappa_P|<|\kappa_2|/3$, which gives $(256/3)M^\flat(\lambda/K)(1+l)$. In $S$ the $g$ terms cancel, so $|\int_{R>K}S|\le(2\cdot3200+2\cdot86)M^\flat(\lambda/K)(1+l)$.

*(h).* On the $\pi/4$ ray, $|A-e^{i\pi/4}y|^2=A^2+y^2-\sqrt2Ay\ge\max(A^2,y^2)/2$; this reduces to $(t-1/\sqrt2)^2\ge0$. So $|A+K|\ge\max(|A|,|y|)/\sqrt2\ge\langle y\rangle/2$. Each gap factor bound doubles; repeat the argument. $\square$

**Verification.**

* `fix_r2_scripts/l8_bounds.py` → `fix_r2_logs/l8_bounds.log`, ALL PASS: 300 random factorized jets × 400 points, $\theta=\pi/2$ and $\pi/4$, multi-state gaps, $\mu/\lambda\in[10^{-3},0.6]$. Maximum ratio lhs/bound: (b) 0.39, (c) 0.015, (d) 0.023, (e) 0.28; at $\pi/4$ with constants ×8: 0.26, 0.002, 0.006, 0.05.
* $\int g$ and $\int S$ reproduce $-i\mathcal J$ and $-\mathcal J$ to $3\times10^{-6}$ and $2\times10^{-4}$.
* Round-3 reviewer test on **general, non-factorized** (ADJ)-class jets (hexagon orbits, winding cycles, two-chains with multi-state shared gaps): maximum ratios (b) 0.52, (c) 0.025, (d) 0.044, (e) 0.42 at $\theta=\pi/2$; $g^{[12]}=g^{[21]}$ to $3\times10^{-12}$ (`review_r3_1_scripts/l8_general.py` → `review_r3_1_logs/l8_general.log`).
* Independent check with a different jet generator (`review_r3_2_scripts/r3_L8_check.py`): (b) 0.357, (c) 0.0083, (d) 0.033, (e) 0.216.
* The proven constants are crude; numerically the sharp ones are about 6 and 0.4 (OPEN-12).

**Novelty:** new (elementary).

---

## 5. Colour

### Lemma L4 (colour bookkeeping for coincident pairs) — [R, R_def]

*Proposed labels:* (a) is `lem:appO-glauber-operator` (existing); (b)–(d) form a new `lem:appO-halfcoinc-colour`.

**(a) Fully coincident pair** (reference). With $X=\mathbf T_i\cdot\mathbf T_j$ and $\mathcal M^{(1)}=-i\chi X$,
$$\mathcal M^{(2)}+\mathcal M^{(2)\dagger}+\mathcal M^{(1)\dagger}\mathcal M^{(1)}=-\tfrac12C_A\chi^2({\rm Re}\,p_{\rm opp})X .$$
The ladder carries $X^2$ and the crossed graph $X^2+\frac{C_A}{2}X$.

**(b) Half-coincident pair** (spectator $i$; spectators $j_1\ne j_2$), with $X_e:=\mathbf T_i\cdot\mathbf T_{j_e}$.

* *Convention.* One exchange on the amplitude side is $\mathcal M^{(1)}_e=-ic_eX_e$ with $c_e$ **real** (the reference's $-i\chi X$, i.e. $c_e=\chi_e$). On the conjugate side it is $+ic_eX_e$.
* *Colour of the configurations.* With line 1 first on $i$, the amplitude side carries $X_2X_1$ (later insertions to the left). The conjugate side carries $X_1X_2$. One line on each side gives $X_1X_2+X_2X_1$, because conjugate insertions stand to the left in the closed-time-path form.
* *Result.* With $W_{12}+W_{21}=1$, the $O(c_1c_2)$ residual is
$$\mathcal R=2ic_1c_2\,{\rm Im}W_{12}\,[X_1,X_2],\qquad[X_1,X_2]=if^{abc}\,T^c_iT^a_{j_1}T^b_{j_2}.$$
* *Sign.* If $c_e$ denoted instead the complex coefficient in $\mathcal M^{(1)}_e=c_eX_e$, the sign would flip (explicit-matrix check, round 2).

**(c)** $[X_1,X_2]=0$ on the colour-singlet subspace of $(i,j_1,j_2)$ alone.

**(d) Drell–Yan remnant states.**

*Setting.*

* Hadron $A$ = active parton $a$, in an irrep $R_a\in\{3,\bar3\}$, plus a remnant A-rem containing $i$.
* Hadron $B$ = active parton $b$ plus a remnant B-rem containing $j_1,j_2$; $a\bar b\to\gamma^*$ is a colour singlet.
* The remnant colour state $\psi$ is a singlet of A-rem $\otimes$ B-rem. Its A-rem part lies in the $\bar R_a$-isotypic component, with multiplicity space $\mathcal M$.

*Statements.*

* **(d1)** $\langle\psi|[X_1,X_2]|\psi\rangle=-\langle\psi|(K_i\otimes1)\,if^{abc}T^a_{j_1}T^b_{j_2}\sum_{k\in\text{B-rem}\setminus\{j_1,j_2\}}T^c_k|\psi\rangle$. Here $K_i$ acts on $\mathcal M$; it is a number $\kappa_i$ if $\dim\mathcal M=1$, with $\kappa_i=1$ for A-rem $=\bar q$ and $\frac12$ for a diquark. In particular the expectation **vanishes for every $\psi$ when B-rem $=\{j_1,j_2\}$**, however many partons A-rem contains (example: valence $p\bar p\to$ DY).
* **(d2)** In a common real weight (tensor-product) basis of all irreps, $(T^a)^*=s_aT^a$ with the same signs $s_a$ for $3,\bar3,8$, and $s_as_bs_c=-1$ whenever $f^{abc}\ne0$. In such a basis every $X_e$ is real symmetric and $[X_1,X_2]$ is real antisymmetric. Hence $\langle\psi|[X_1,X_2]|\psi\rangle=0$ for every real $\psi$, and ${\rm Tr}(\rho[X_1,X_2])=0$ for every real colour density matrix. (In the standard adjoint basis all $s_a=-1$, so a weight basis is needed.)
* **(d3) Scope.** The residual's colour factor vanishes for valence (minimal-Fock) remnants with B-rem $=\{j_1,j_2\}$, and for real colour states. A non-zero value needs both a further remnant parton in the hadron of $j_1,j_2$ **and** complex relative phases between distinct real singlet couplings.
  * Generic multi-parton remnants with momentum-dependent complex colour amplitudes are *not* covered. They are generic in the leading-twist sum over Fock states.
  * No symmetry is known that forces $\int d\Phi\,{\rm Im}W_{12}(\Phi)\langle\psi(\Phi)|i[X_1,X_2]|\psi(\Phi)\rangle$ to vanish; both factors can change sign under conjugation of the colour state. This is open (OPEN-1).
* **Basis-independent norms.** The norms $\|P[X_1,X_2]P\|$ on the DY remnant spaces are:
  * 0.4330 for A-rem $=\bar q$, B-rem $=\bar q\bar qg$;
  * 0.2165 for A-rem $=qq$, B-rem $=\bar q\bar qg$;
  * 0.3536 for A-rem $=qq$, B-rem $=\bar qqq$;
  * 0.7071 for A-rem $=\bar q$, B-rem $=\bar qqq$.
* **Restriction.** (d1) uses $\dim{\rm Hom}(8\otimes R_A,R_A)=1$, which holds for $R_A\in\{3,\bar3\}$. A gluon-active hadron of $i$ ($R_A=8$, which also has a $d$-type coupling) is not covered.

**Proofs.**

*(a).* $\mathcal M^{(1)\dagger}\mathcal M^{(1)}=\chi^2X^2$ and $\mathcal M^{(2)}+\mathcal M^{(2)\dagger}=-\chi^2X^2-\frac{\chi^2}{2}C_A{\rm Re}(p_{\rm opp})X$. The crossed-graph colour factor follows from $\sum_{a,b}T^aT^bT'^bT'^a=X^2+\frac12C_AX$.

*(b).* Collect the contributions:

* amplitude side: $-c_1c_2[W_{12}X_2X_1+W_{21}X_1X_2]$;
* conjugate side: $-c_1c_2[W_{12}^*X_1X_2+W_{21}^*X_2X_1]$;
* one line on each side: $+c_1c_2(X_1X_2+X_2X_1)$.

The coefficient of $X_1X_2$ is $c_1c_2(1-W_{21}-W_{12}^*)=2ic_1c_2{\rm Im}W_{12}$. The coefficient of $X_2X_1$ is its negative. Finally $[X_1,X_2]=[T_i^a,T_i^b]T^a_{j_1}T^b_{j_2}=if^{abc}T^c_iT^a_{j_1}T^b_{j_2}$.

*(c).* $X_e$ commutes with the total colour, so it preserves the singlet subspace. On it, $\mathbf T_i=-(\mathbf T_{j_1}+\mathbf T_{j_2})$, so $X_1=-C_{j_1}-\mathbf T_{j_1}\!\cdot\mathbf T_{j_2}$ and $X_2=-C_{j_2}-\mathbf T_{j_1}\!\cdot\mathbf T_{j_2}$, which commute.

*(d1).*

* Both $\psi$ and the bra lie in $(\mathcal M\otimes R_A)\otimes\mathcal H_{\rm B\text{-}rem}$, so only $PT^c_iP$ enters.
* By the Wigner–Eckart theorem, $PT^c_iP=K_i\otimes T^c_{R_A}=(K_i\otimes1)T^c_{\rm A\text{-}rem}P$.
* $K_i\otimes1$ and $T_{\rm A\text{-}rem}$ commute with every operator on B-rem, and the singlet condition gives $T^c_{\rm A\text{-}rem}\psi=-T^c_{\rm B\text{-}rem}\psi$. Hence $\langle\psi|T^c_iO^c_B|\psi\rangle=-\langle\psi|(K_i\otimes1)O^c_BT^c_{\rm B\text{-}rem}|\psi\rangle$ with $O^c_B=if^{abc}T^a_{j_1}T^b_{j_2}$.
* Finally $f^{abc}T^a_{j_1}T^b_{j_2}(T^c_{j_1}+T^c_{j_2})=0$. Indeed, $f^{abc}T^a_{j_1}T^c_{j_1}=-\frac i2C_AT^b_{j_1}$ and $f^{abc}T^b_{j_2}T^c_{j_2}=\frac i2C_AT^a_{j_2}$, so the two terms give $\frac i2C_A(-\mathbf T_{j_1}\!\cdot\mathbf T_{j_2}+\mathbf T_{j_1}\!\cdot\mathbf T_{j_2})=0$.

*(d2).*

* $X_e^*=\sum_as_a^2T^a_iT^a_{j_e}=X_e$, and $X_e$ is Hermitian, hence real symmetric.
* The commutator of two real symmetric matrices is real antisymmetric, and a real antisymmetric operator has zero expectation in real vectors.
* The singlet space is invariant under complex conjugation, so it has a real basis. $\square$

**Context.**

* The structure "$f^{abc}TTT$ from non-commuting interactions at different times, vanishing by colour conservation when no further parton is present" parallels the two-loop operator that breaks strict collinear factorization in Catani–de Florian–Rodrigo, JHEP 07 (2012) 026 (read in part). There $\Delta^{(2)}\propto f_{abc}T^a_1T^b_2T^c_3$ (their eq. (186)). For $n=4$ partons the *operator* does not vanish, but its contribution to the squared amplitude does, by colour conservation (eqs. (187)–(190)); it contributes from $n=5$ on.
* Compare also the non-commutation of Coulomb/Glauber exchanges with other soft exchanges in Forshaw–Seymour–Siodmok, JHEP 11 (2012) 066.
* For Glauber pinches and Reggeization in space-like collinear limits see Barcaro–Gao–Gaunt–Pathak, arXiv:2607.14259 (2026).

**Verification.**

* `scripts/checks_C2_C3_C4.py` C3a–f, ALL PASS.
* `fix_r1_scripts/colour_dy_check.py` → `fix_r1_logs/colour_dy_check.log`, ALL PASS: real structure; the identity of (d1) for (3,3), (3,$\bar3$), (8,3), (8,8), ($\bar3$,8); (d1) on eight DY configurations; (d2); the norms.
* `scripts/check_halfcoinc_singlets_v2.py` → `logs/check_halfcoinc_singlets_v2.log`, ALL PASS. This is the fixed re-run of a check that crashed in round 0.
* Independent reviewer codes in random real bases in all three rounds: (d1) to $\le4\times10^{-16}$; (d2); the norms for every choice of $(j_1,j_2)$ (`review_r2_1_scripts/colour_indep_r2.py`, `review_r2_2_scripts/chkC_colour.py`).

**Novelty.** (a) is the reference's. (b)–(d) are new as statements; (d2) is elementary linear algebra, new only in this context. The colour-singlet-target mechanism itself is that of Lindsay–Ross–Sachrajda, NPB 222 (1983) 189.

---

## 6. Commuting insertions and windows

### Proposition T1 (commuting insertions to all orders: a uniform re-derivation) — [R, R_cond: `asm:appO-lcopt`]

The integrated form also uses `asm:appO-envelope`, exactly as `prop:appO-ss-cancel` does.

**Hypotheses.**

* $(\Gamma_0,R_0)\in\mathcal G_0$ without H-emission endpoints.
* The family has any number of SS lines, with any coincidences and any localized SA/AS insertions.
* All localized insertions on every spectator commute. In the non-abelian theory this is essentially the abelian case plus the non-coincident patterns: commuting non-abelian coincident insertions on one spectator form an essentially empty class.

**Conclusion.** On the window cores:

* per-graph weak equivalence holds with the reference's rewriting map, without clause (c1);
* one-sidedness holds;
* the family cancellation of `prop:appO-ss-cancel`(iii) holds.

With the windows of P1 there are no window-edge terms.

**Proof.**

* By L1(a),(c) (L1′(a),(c) for multi-pole factors), the localized value is $\prod R_e(0)\sum_\sigma w_\sigma\mathcal J_\sigma$.
* For commuting insertions the colour-dressed equal-time values do not depend on the order, and by `lem:appO-insertion-values` they do not depend on the position of $V_H$ either. So $\mathcal J_\sigma=\mathcal J(0)$ for every $\sigma$, and $\sum w=1$ gives $\prod R_e(0)\mathcal J(0)$. This is identical to the line-by-line localization, so the proofs of `prop:appO-ss-cancel`(iii) and of per-graph weak equivalence apply verbatim.
* For multi-pole (soft-line) external factors, the *error* estimate is taken from the line-by-line localization (`lem:appO-equal-time`(iii), one insertion at a time, which is legitimate because the insertions commute), not from L1′(b), whose constant carries $\sum_\sigma|w_\sigma(p)|$. For Glauber factors both routes give the same bound. $\square$

**Novelty.** The statements are `prop:appO-ss-cancel`(iii) and the reference's Props E.35/E.31(iii). Only the uniform route via L1 is new. The TMD version is [C] (§11).

### Lemma P1 (side-independent windows remove the window-edge terms) — [R, R_cond: `asm:appO-lcopt`]

*Proposed label:* `lem:appO-side-independent-windows` (slot X1c).

**Definitions.**

* $J_A^0$ is the uncut forward $A$-subgraph with the SS-insertion vertices removed, and $L(J_A^0)$ its set of lines. Both are defined on the forward graph, so they do not depend on the cut position, as the order "cut sum first, family sum second" requires.
* *Routing.* Each SS momentum $k_m$ is routed in the standard flow (`def:appO-orientation`(c)) from its $A$-end through $J_A$ to $V_H$ ($V_H^\dagger$ on the conjugate side), along a path fixed for each side assignment.
* $L_A^{\rm SS}$ is the set of lines of $J_A^0$ that carry SS momentum under at least one side assignment of the family.
* $x^A_{\min}:=\min_{l\in L_A^{\rm SS}}l^+/P_A^+$ is a **momentum fraction**. It is independent of side and cut. By `lem:appO-glauber-pc`(a), the plus components $l^+$ do not depend on the SS momenta. $L_A^{\rm SS}$ may be replaced by $L(J_A^0)$.
* $n_A$ is the maximal number of SS-carrying lines in a single state, over all side assignments; it equals 1 per SS momentum for time-monotone routings.
* $E^{(0)}(l)$ is the on-shell energy of $l$ at zero SS momenta.
* The window scales and window factors are
$$\hat\nu_A:=P_A^-+2\sum_{l\in L(J_A^0)}E^{(0)}(l)+\frac{2n_A(\sum_m|\mathbf k_{Tm}|)^2}{x^A_{\min}P_A^+},$$
with $\hat\nu_B$ defined in the same way ($A\leftrightarrow B$, plus $\leftrightarrow$ minus), and $\hat\Theta_m:=\vartheta\big(4\hat\nu_A\hat\nu_B/(\lambda^{a_G}\mathbf k_{Tm}^2)\big)$ with $\vartheta$ as in `def:appO-windows`.

**Statement.**

* **(a)** $\hat\nu_A$ and $\hat\nu_B$ are independent of the side assignment and of the cut.
* **(b)** For every side assignment and every state $S$ of $J_A$: $|A_D|\le\hat\nu_A$ for initial states and $|A'_D|\le\hat\nu_A$ for final states.
* **(c)** On $\{x^A_{\min}\ge c,\ x^B_{\min}\ge c\}$, with a fixed $c>0$, one has $\hat\nu\sim\lambda^2Q$ in the Glauber scaling region, so $\hat\Theta=1$ on the Glauber core. The complement is the region of wee lines carrying SS momentum ($x_{\min}\to0$); there the last term of $\hat\nu$ is enhanced, and $\lambda_J\le C\hat\nu$ degrades the localization error $\lambda_J/\kappa$. It is assigned to the soft-angle region $K_R$, i.e. to `asm:appO-deformation`(c).
* **(d)** The localization bounds of `prop:appO-ss-localize` hold with $\lambda_J\le C\hat\nu$. The family identity $\sum_{\rm sides}\prod_l(\cdots)=\prod_l(-iG_lX_l+iG_lX_l)=0$ holds at every point of the support, so the window-edge terms of `prop:appO-ss-cancel`(iv) **vanish identically**. The out-of-window parts are not removed: the rewriting map changes and $K_R$ is enlarged (`asm:appO-deformation`(c)).

**Proof.**

*(a)* holds by construction:

* $E^{(0)}$ is evaluated at zero SS momenta;
* the SS transverse momenta enter only through $\sum|\mathbf k_{Tm}|$;
* $x^A_{\min}$ and $n_A$ are extremal over all side assignments;
* everything is defined on the forward graph.

*(b).*

* For an initial state, $A_D=P^--\sum_{l\in S}E(l)$ with $P^-\ge0$ and $E(l)\ge0$, so $|A_D|\le\max(P^-,\sum_SE(l))$.
* For a final state, $A'_D=\mathcal E_{\rm cut}-\sum_SE(l)$ with $\mathcal E_{\rm cut}\ge0$, so $|A'_D|\le\max(\mathcal E_{\rm cut},\sum_SE(l))$.
* Let $\Delta_l$ be the SS transverse momentum carried by $l$; $l^+$ is unchanged. By $(a+b)^2\le2a^2+2b^2$, $E(l)\le2E^{(0)}(l)+\Delta_l^2/l^+\le2E^{(0)}(l)+(\sum_m|\mathbf k_{Tm}|)^2/(x^A_{\min}P_A^+)$.
* A state contains at most one segment of each line of $J_A^0$ and at most $n_A$ SS-carrying lines. Hence $\sum_SE(l)<\hat\nu_A$.
* The same bound holds for $\mathcal E_{\rm cut}$, since cut lines are lines of $J_A^0$.

*(c)* is power counting with $x_{\min}\ge c$.

*(d).* The family algebra needs only that the window factors are equal for all side assignments. $\square$

**Novelty.** New; the idea was suggested, without proof, in the reference work notes (R7).

**Slot decision.** X1c: PASS, recommended by both round-3 reviewers after the notational fix ($x_{\min}$ as a momentum fraction).

---

## 7. The fully coincident pattern

### Theorem T2 (fully coincident SS pair at $O(g^4)$; model theorem for the uncut side sum)

*Proposed label:* `prop:appO-twoexch-spectator` (slot X1f), inserted as a model theorem (decision PARTIAL; Appendix A).

**First sentence (scope).** In the global two-time model $\mathbb M_{\rm glob}$, pointwise on $\mathcal N_A\cap\mathcal N_B$, at $O(g^4)$, for two **uncut** SS lines joining the same $A$-spectator $i$ and the same $B$-spectator $j$ on the amplitude side, the following holds.

**Hypotheses.**

* (i) The model $\mathbb M_{\rm glob}$ (Def. D4), with exact connecting propagators.
* (ii) $J_A$ satisfies (SEC), (EQ), (REAL). $J_B$ satisfies (SEC), (EQ), (ADJ), (REAL).
* (iii) The configuration lies in $\mathcal N_A\cap\mathcal N_B$.
* (iv) $\varepsilon\le\varepsilon_0:=\min\big(\frac1{16},\frac{a_{\min}^2}{4a_1a_2}\big)$.
* (v) $\delta_Y\le\frac12$, where $\delta_Y:=2\mathcal E_1+2\mathcal E_2+2\mathcal E_3+\mathcal E_4$ is given explicitly in Steps 3–5. Condition (v) is not implied by (iv): the term $2\mathcal E_2$ alone is $\approx167\,m^\flat_B\varepsilon^{1/2}(1+L_B)$. It holds for $\varepsilon$ small enough, given the jet constants.

**Conclusion.**

**(a) [R, R_PT] (model-internal).**
$$|N/N_0-1|\le\delta_Y\le C_N\,\varepsilon^{1/2}(1+L_B)^2,$$
$$|{\rm Re}\,p_{\rm opp}|\le C_T\,\varepsilon^{1/2}(1+L_B)^2(1+L),$$
$$\Big|{\rm Im}\,p_{\rm opp}+\frac1\pi\ln\frac1\varepsilon\Big|\le C_I .$$
$C_N$, $C_T$, $C_I$ are explicit polynomials in $m_A$, $m^\flat_A$, $m^\flat_B$, $m_B$, $c_\rho$, $a_{\max}/a_{\min}$, $\ell_A$ and $\ell_B$ (Step 8). In particular, $C_T$ and $C_I$ depend on $\ln(\lambda_B/\mu_B)$ and $\ln(\lambda_A/\mu_A)$ through $\ell_B$ and $\ell_A$.

*Consequences.*

* The side-sum residual $-\frac12C_A\chi^2({\rm Re}\,p_{\rm opp})X$ of the uncut lines is power suppressed.
* The $C_A$ term of $\mathcal M^{(2)}$ equals $(-i\chi X)\big(-C_A\chi\ln(1/\varepsilon)/(4\pi)\big)$ at leading-logarithmic accuracy. This is a real multiple of the anti-Hermitian one-exchange amplitude: the gluon reggeization phase.

**(b) [R, R_cond: `asm:appO-lcopt`, `asm:appO-adjacent-swap`†, `asm:appO-real-jets`†] (QCD jets; † = proposed entry).** For leading-power cut-summed LCOPT jets of QCD graphs:

* (SEC) and (EQ) hold under `asm:appO-lcopt` (Def. D2; `lem:appO-insertion-values`);
* (ADJ) and (REAL) are the proposed entries.

Hence (a) holds for these jets. The content grade is [P], set by the proposed tags. In the scalar spectator model (§14.1) all of (ii) holds exactly, and (a) holds there with no premise.

**(c) [P] (physical reading).** See below. It is conditional on `asm:appO-collinear-ends` and on OPEN-13.

**Proof.**

*Step 0 (rotation and regions).*

* By L5 at $\theta=\pi/2$, applied to each colour pair,
$$W(\pi_A,\pi_B)\frac{N}{N_0}=-\frac1{\mathcal J_B}\int h_{\pi_A}f_{\pi_B}\frac{d^2\kappa}{(2\pi)^2},\qquad Y:=\frac N{N_0}=-\frac1{\mathcal J_B}\int(h_{12}+h_{21})S_B\,\frac{d^2\kappa}{(2\pi)^2},$$
$$X:=p_{\rm opp}Y=-\frac1{\mathcal J_B}\int(h_{12}f_{21}+h_{21}f_{12})\frac{d^2\kappa}{(2\pi)^2}.$$
* *Regions.* $\mathsf S:=\{R\le K\}$ (inner square); $\mathsf T:=\{R>K,\ r_P<R/4\}=\mathsf T_+\cup\mathsf T_-$, split by the sign of $\kappa_2$ (strips); $\mathsf O:=\{R>K,\ r_P\ge R/4\}$ (off-strip).
* *Geometry of the strips.* In $\mathsf T$, $|\kappa_2|\ge3R/4$ and ${\rm sgn}\,\kappa_1=-{\rm sgn}\,\kappa_2$. So $\mathsf T_+$ lies in the quadrant $(-,+)$, where $h_{21}=0$ and $h_{12}=\rho(\kappa_1,\kappa_2):=(a_1a_2/\mathcal J_A)F_A^{(1V2)}$, the exact mixed sector. $\mathsf T_-$ is the mirror image, with $\rho'$ from $2V1$.
* *Choice of $K$.* Put $K:=(a\lambda_B/\lambda_A)^{1/2}=\lambda_B\varepsilon^{-1/2}$. Then $4\lambda_B\le K\le a_{\min}/(2\lambda_A)$, which is equivalent to (iv). Moreover $\lambda_AK/a_{\min}=(a/a_{\min})\varepsilon^{1/2}$, $\lambda_B/K=\varepsilon^{1/2}$, and $l_K:=\ln(1+4K/\mu_B)=L_B$.

*Step 1 ($A$-side facts).*

* **(A1)** For $R\le a_{\min}/(2\lambda_A)$: $h_\pi=w^{[\pi]}+e_\pi$ with $|e_\pi|\le4m_A\lambda_AR/a_{\min}$. This is L1(d) with (EQ): on the rotated contour $z_e=-ia_e/(2\kappa_e)$, the poles of a group lie on one ray, and $|K_l|\ge a_{\min}/(2R)\ge\lambda_A$. The localized weights are real:
$$w^{[12]}=\frac{a_1\kappa_2}{a_1\kappa_2+a_2\kappa_1}\ (+,+),\qquad\frac{a_2\kappa_1}{a_2\kappa_1+a_1\kappa_2}\ (-,-),\qquad1\ (-,+),\qquad0\ (+,-),$$
and $w^{[21]}=1-w^{[12]}$. The function $v:=w^{[12]}-\frac12$ is real and odd under $\kappa\to-\kappa$, with $|v|\le\frac12$.
* **(A2)** Everywhere, $|h_\pi|\le m^\flat_A$. Indeed $|A+K|\ge\max(|A|,|K|)$ on the imaginary axis gives $|J^{(\sigma)}(z)|\le M^\flat_\sigma\prod|K_l|^{-1}$, and $\prod|z_e|/\prod|K_l|=|w_\sigma|\le1$.
* **(A3)** $\rho(-\kappa,\kappa)=\varrho_{12}(\kappa):=\rho_{12}(i\kappa)$, where, summing over the terms of sector $1V2$ (first-gap energies $A_j$, second-gap energies $A'_j$),
$$\rho_{12}(k):=\frac{a_1a_2}{\mathcal J_A}\sum_tc_t\frac{(2ik)^{n_1+n_2-2}}{\prod_j(2kA_j-a_1)\prod_j(2kA'_j-a_2)}.$$
  * $\rho_{12}$ is holomorphic in ${\rm Re}\,k>0$: its poles $a_1/(2A_j)$ and $a_2/(2A'_j)$ are negative on $\mathcal N_A$.
  * It is real on $k>0$ by (REAL), $\rho_{12}(0)=1$ by (EQ), and $\rho_{12}=O(k^{-2})$ at infinity.
  * By (A1), $|\varrho_{12}(\kappa)-1|\le4m_A\lambda_A\kappa/a_{\min}$ for $\kappa\le a_{\min}/(2\lambda_A)$.
  * Decay bound: $|\varrho_{12}(\kappa)|\le m^\flat_A\min\big(1,a_1a_2/(4\kappa^2\mu_A^2)\big)$, from $|2i\kappa A-a|\ge\max(a,2\kappa|A|)$ and $(2\kappa)/|2i\kappa A_j-a|\le1/\mu_A$ for the extra states.
  * The same holds for $\varrho_{21}$.
* **(A4)** On the strip $|\kappa_1+\kappa_2|\le\kappa_2/3$ (with $\kappa_2>0$):
$$|\partial\rho/\partial\kappa_1|\le c_\rho\,(\lambda_A/a_{\min})\min\big(1,(\kappa_*/\kappa_2)^2\big),\qquad\kappa_*:=a_{\min}/(4\lambda_A),$$
$$c_\rho\le50(2\bar n_A-1)\,m^\flat_A(a_{\max}/a_{\min})^2(\lambda_A/\mu_A)^2,$$
where $\bar n_A$ is the maximal number of states in a gap. Reason: on the imaginary axis an $n$-state initial gap of $1V2$ contributes $(2s)^{n-1}\prod_j(a_1-2isA_j)^{-1}$ with $s=|\kappa_1|$, and $\frac{d}{ds}\ln(a-2isA)=-2iA/(a-2isA)$ has modulus at most $\min(2\lambda_A/a,1/s)$.

*Step 2.* L8 applies to $J_B$, with constants $\lambda_B$, $\mu_B$, $M^\flat_B$.

*Step 3 (inner square).*

* *Split.* By (A1),
$$-\frac1{\mathcal J_B}\int_{\mathsf S}[h_{12}f_{21}+h_{21}f_{12}]=-\frac1{\mathcal J_B}\int_{\mathsf S}\big[\tfrac12S_B-v\Delta_B\big]+P_1,$$
with $|P_1|\le\mathcal E_1:=\frac{24}{\pi^2}m_Am^\flat_B\frac{\lambda_AK}{a_{\min}}l_K^2$, by L8(g).
* *The $S_B$ term.* By L8(f), $-\frac1{2\mathcal J_B}\int_{\mathsf S}S_B=\frac12+T_{\rm tail}$, where $T_{\rm tail}:=\frac1{2\mathcal J_B}\int_{R>K}S_B$ satisfies $|T_{\rm tail}|\le\mathcal E_2:=\frac{825}{\pi^2}m^\flat_B\frac{\lambda_B}K(1+l_K)$.
* *The $v$ term.* $V_{\mathsf S}:=\frac1{\mathcal J_B}\int_{\mathsf S}v\Delta_B$ is **purely imaginary**. By (REAL), $\Delta_B(\kappa)=e^{i\varphi}D(\kappa)$ with $D(-\kappa)=\overline{D(\kappa)}$, and $\mathcal J_B\in e^{i\varphi}\mathbb R$. Since $v$ is real and odd and $\mathsf S$ is symmetric, $\int_{\mathsf S}vD=-\overline{\int_{\mathsf S}vD}$.

*Step 4 (strips).*

* *Rewriting in $\mathsf T_+$.* There $h_{12}f_{21}=\rho\,[-g(-i\kappa_P)/\kappa_2+E_{21}]$ by L8(d). The $E$-part, over both strips, is at most $\mathcal E_4:=\frac{43}{\pi^2}m^\flat_Am^\flat_B\frac{\lambda_B}K(1+l_K)$.
* *Main term.* Change variables to $(\kappa_P,\kappa_2)$ (unit Jacobian). In $\mathsf T_+$ the strip is $\kappa_P\in(-\kappa_2/3,\kappa_2/4)$, and $R>K$ means $\kappa_2>K$ for $\kappa_P>0$ and $\kappa_2>K-|\kappa_P|$ for $\kappa_P<0$. Then
$$\frac1{\mathcal J_B}\int_{\mathsf T_+}\rho\,g\,\kappa_2^{-1}\frac{d^2\kappa}{(2\pi)^2}=\frac1{\mathcal J_B}\int_K^\infty\frac{d\kappa_2}{2\pi\kappa_2}\varrho_{12}(\kappa_2)\int_{\mathbb R}g(-iU)\frac{dU}{2\pi}+P_5+P_6+P_7=-\frac{i}{2\pi}\int_K^\infty\frac{d\kappa}\kappa\varrho_{12}(\kappa)+P_5+P_6+P_7,$$
using L8(e).
* *Corrections* (each bound is over both strips):
  * $P_5$, the variation of $\rho$ across the strip. Use (A4) and $\int_{|U|\le X}|U||g(-iU)|dU\le4M^\flat_B\lambda_B(1+2\ln(X/\lambda_B))$. Then $|P_5|\le\mathcal E_5:=\frac{2c_\rho}{\pi^2}m^\flat_B\frac{\lambda_A\lambda_B}{a_{\min}}(1+2\ln(\kappa_*/\lambda_B))^2$.
  * $P_6$, the tail $|U|>\kappa_2/4$ of $g$, where $\int_{|U|>\kappa_2/4}|g|\le32M_B\lambda_B/\kappa_2$. Then $|P_6|\le\mathcal E_6:=\frac{16}{\pi^2}m^\flat_Am^\flat_B\frac{\lambda_B}{K}$.
  * $P_7$, the sliver $K-|\kappa_P|<\kappa_2\le K$. Then $|P_7|\le\mathcal E_7:=\frac4{\pi^2}m^\flat_Am^\flat_B\frac{\lambda_B}K(1+2l_K)$.
* Adding $\mathsf T_-$ gives the outer contribution
$$p^{\rm out}_{\rm opp}:=-\frac{i}{2\pi}\int_K^\infty\frac{d\kappa}{\kappa}\big[\varrho_{12}+\varrho_{21}\big].$$

*Step 5 (off-strip).* By (A2) and L8(g), the off-strip contribution $P_{\mathsf O}$, summed over both pairs, satisfies $|P_{\mathsf O}|\le\mathcal E_3:=\frac{1600}{\pi^2}m^\flat_Am^\flat_B\frac{\lambda_B}K(1+l_K)$.

*Step 6 (real parts; L6).*

* By L6, applicable on $\mathcal N_A$ with (REAL), each ray integral $\int_0^\infty\frac{d\kappa}\kappa{\rm Im}\,\varrho_{12}$ and $\int_0^\infty\frac{d\kappa}\kappa{\rm Im}\,\varrho_{21}$ is exactly $-\pi/2$. Hence
$${\rm Re}\,p^{\rm out}_{\rm opp}=\frac1{2\pi}\int_K^\infty\frac{d\kappa}\kappa{\rm Im}(\varrho_{12}+\varrho_{21})=\frac1{2\pi}\Big[-\pi-\int_0^K\frac{d\kappa}\kappa{\rm Im}(\varrho_{12}+\varrho_{21})\Big].$$
* The head is bounded by (A3): ${\rm Re}\,p^{\rm out}_{\rm opp}=-\frac12+O(\mathcal E_8)$, with $\mathcal E_8:=\frac4\pi m_A\frac{\lambda_AK}{a_{\min}}$.
* *Collecting.* $X=\frac12+T_{\rm tail}+V_{\mathsf S}+P_1+p^{\rm out}_{\rm opp}+P_5+P_6+P_7+P_E+P_{\mathsf O}$, with $|P_E|\le\mathcal E_4$ (the $E$-part of Step 4) and $|P_{\mathsf O}|\le\mathcal E_3$. Hence $|{\rm Re}\,X|\le\mathcal E_{\rm tot}:=\sum_{i=1}^8\mathcal E_i$.
* *Normalization.* The same steps with $h_{12}+h_{21}$ give $|Y-1|\le\delta_Y=2\mathcal E_1+2\mathcal E_2+2\mathcal E_3+\mathcal E_4$. In the strips, $(h_{12}+h_{21})S_B=\rho(E_{12}+E_{21})$, since the $g$ terms cancel.

*Step 7 ($|X|$ and the imaginary part).*

* *Bound on $V_{\mathsf S}$.* Use $|v|\le\frac12$ and split $\mathsf S$ into three parts:
  * $\{R\le4\lambda_B\}$: by L8(g) with $K\to4\lambda_B$;
  * the off-strip part of $\{4\lambda_B<R\le K\}$: by L8(g);
  * the strip part of $\{4\lambda_B<R\le K\}$: there $\Delta_B=2g/\kappa_2+E_{12}-E_{21}$, $|\kappa_2|\in[3\lambda_B,K]$, and $\int|g|\le4M^\flat_B(1+\ell_B)$ by L8(e).

  Together,
$$|V_{\mathsf S}|\le\frac{m^\flat_B}{\pi^2}\Big[3\ell_B^2+206(1+\ell_B)+2(1+\ell_B)\ln\frac{K}{3\lambda_B}\Big].$$
* *Bound on $p^{\rm out}_{\rm opp}$.* By the decay bound of (A3), with $\kappa_\mu:=a/(2\mu_A)\ge K$,
$$|p^{\rm out}_{\rm opp}|\le\frac{m^\flat_A}{\pi}\Big[\ln\frac{a}{2\mu_AK}+\frac12\Big].$$
* *Bound on $|X|$.* With $K=\lambda_B\varepsilon^{-1/2}$ one has $\ln\frac{a}{2\mu_AK}=\frac L2+\ln\frac{\lambda_A}{2\mu_A}\le\frac L2+\ell_A$ and $\ln\frac K{3\lambda_B}\le\frac L2$. Hence
$$|X|\le C_{X1}L+C_{X0},\qquad C_{X1}:=\frac{m^\flat_A}{2\pi}+\frac{m^\flat_B(1+\ell_B)}{\pi^2},$$
$$C_{X0}:=\frac12+\mathcal E_{\rm tot}+\frac{m^\flat_B}{\pi^2}\big[3\ell_B^2+206(1+\ell_B)\big]+\frac{m^\flat_A}{\pi}\Big(\ell_A+\frac12\Big).$$
* *Imaginary part of $V_{\mathsf S}$.* The strip part of $\mathsf S$, $\{4\lambda_B<R\le K,\ r_P<R/4\}$, lies in the quadrant $(-,+)$ for $\kappa_2>0$, where $v=+\frac12$, and in $(+,-)$ for $\kappa_2<0$, where $v=-\frac12$. Hence $v\Delta_B=g(-i\kappa_P)/|\kappa_2|+v(E_{12}-E_{21})$ there. With L8(e),
$$V_{\mathsf S}=-\frac i\pi\ln\frac{K}{4\lambda_B}+R_{\mathsf S},\qquad|R_{\mathsf S}|\le\frac{m^\flat_B}{\pi^2}\big[3\ell_B^2+208(1+\ell_B)\big]+\frac4{\pi^2}m_B .$$
  The remainder collects the tails $|U|>\kappa_2/4$, the slivers at $R=4\lambda_B$ and $R=K$ (where $\ln(3/2)\le\frac12$), the $E$-parts, and the non-strip parts.
* *Imaginary part of $p^{\rm out}_{\rm opp}$.* With $\kappa':=a_{\min}/(2\lambda_A)\ge K$, use (A3) below $\kappa'$ and the decay bound above it:
$$p^{\rm out}_{\rm opp}=-\frac i\pi\ln\frac{\kappa'}{K}+R_{\rm out},\qquad|R_{\rm out}|\le\frac1\pi\Big[2m_A+m^\flat_A\Big(\ln\frac{a_{\max}}{a_{\min}}+\ell_A+\frac12\Big)\Big].$$
* *Sum.* Since $\ln\frac{\kappa'}{4\lambda_B}=L+\ln\frac{a_{\min}}{8a}$,
$$\Big|{\rm Im}\,X+\frac L\pi\Big|\le C_{IX}:=\frac1\pi\ln\frac{8a_{\max}}{a_{\min}}+|R_{\mathsf S}|+|R_{\rm out}|+\mathcal E_{\rm tot}.$$

*Step 8 (division by $Y$; the constants).*

* For $\delta_Y\le\frac12$: $|1/Y|\le2$ and $|p_{\rm opp}-X|=|X||1-Y|/|Y|\le2|X|\delta_Y$. Hence
$$|{\rm Re}\,p_{\rm opp}|\le\mathcal E_{\rm tot}+2(C_{X1}L+C_{X0})\delta_Y,\qquad\Big|{\rm Im}\,p_{\rm opp}+\frac L\pi\Big|\le C_{IX}+2(C_{X1}L+C_{X0})\delta_Y .$$
* *Size of the error terms* with the chosen $K$, writing $r:=a_{\max}/a_{\min}$:
  * $\mathcal E_1,\mathcal E_8\le C\,r\,\varepsilon^{1/2}L_B^2$;
  * $\mathcal E_2,\mathcal E_3,\mathcal E_4,\mathcal E_6,\mathcal E_7\le C\varepsilon^{1/2}(1+L_B)$;
  * $\mathcal E_5\le\frac{2c_\rho}{\pi^2}m^\flat_B\,r\,\varepsilon(1+2L)^2\le\frac{22.4\,c_\rho}{\pi^2}m^\flat_B\,r\,\varepsilon^{1/2}$, using $\varepsilon(1+2L)^2\le11.2\,\varepsilon^{1/2}$ for $\varepsilon\le\frac1{16}$.
* Hence $\mathcal E_{\rm tot}\le C_E\varepsilon^{1/2}(1+L_B)^2$ and $\delta_Y\le C_N\varepsilon^{1/2}(1+L_B)^2$, with
$$C_E:=\frac1{\pi^2}\big[24m_Am^\flat_Br+825m^\flat_B+1667m^\flat_Am^\flat_B+22.4\,c_\rho m^\flat_Br\big]+\frac4\pi m_Ar,$$
$$C_N:=\frac1{\pi^2}\big[48m_Am^\flat_Br+1650m^\flat_B+3243m^\flat_Am^\flat_B\big].$$
* *Final constants.* In $C_{X0}$, replace $\mathcal E_{\rm tot}$ by its bound $C_E(3+\ell_B^2)$; this is valid because $\sup_{\varepsilon\le1/16}\varepsilon^{1/2}(1+L_B)^2\le3+\ell_B^2$. Then
$$C_T:=C_E+2C_N(C_{X1}+C_{X0}),\qquad C_I:=C_{IX}+2C_N\sup_{\varepsilon\le1/16}\big[\varepsilon^{1/2}(1+L_B)^2(C_{X1}L+C_{X0})\big],$$
and the supremum is finite and explicit in $\ell_B$. This proves (a). (b) follows from (a) and the status of the hypotheses (Def. D2, D3; §2.2). $\square$

**Where the $-\frac12$ is generated (remark).**

* *Rotated contour.* The $-\frac12$ is the sum of two L6 ray integrals, one per mixed sector. They are non-zero only where $\rho$ departs from 1, i.e. at $\kappa\sim a/\lambda_A$: the $A$-collinear end, which has the same status as the end poles of T2′(b).
* *Real contour.* It is the near-mass-shell region $2k^+k^-\sim\mathbf k_T^2$ of the exchanged gluons.
* *Strict propagator.* With the strict Glauber propagator that region is absent, and the value is fixed by the regulators (P2).

The physical content of T2 therefore requires `asm:appO-collinear-ends`, or the regulated T2′.

**Numerics (scalar spectator model, §14).**

* *Base set* (both jets on $\mathcal N$): ${\rm Re}\,p_{\rm opp}=0.0123,\ 0.00205,\ 0.00035$ at $\lambda=0.01,0.003,0.001$. Methods I and II agree to $10^{-5}$.
  * Independent reviewer values: $0.012347,\ 0.002048,\ 0.000345$, and $0.0000436$ at $\lambda=0.0003$ (round 1); $0.0123468,\ 0.0020501,\ 0.0003476$ (round 3).
  * $N/N_0=0.99843,\ 0.99987,\ 0.99998$.
  * ${\rm Im}\,p_{\rm opp}+\frac1\pi\ln\frac1\varepsilon=+0.036,\ +0.040,\ +0.041$ at $\varepsilon=1.17\times10^{-3},1.05\times10^{-4},1.17\times10^{-5}$ (`final_logs/t2_constants.log`): bounded and converging, as stated.
* *Non-factorized jet pairs* (round-3 reviewer, `review_r3_1_logs/t2_general.log`):
  * ${\rm Re}\,p_{\rm opp}\to0$ roughly as $\varepsilon^{0.7}$ to $\varepsilon^{0.77}$, and $N/N_0\to1$;
  * ${\rm Im}\,p_{\rm opp}$ falls by 0.717–0.730 per decade of $\varepsilon$, against $(1/\pi)\ln10=0.733$;
  * ${\rm Im}\,p_{\rm opp}+L/\pi$ is stable at $-0.08$, $-0.21$ and $+0.70$ for the three pairs;
  * one pair has a $J_A$ that violates (ADJ), consistent with T2 requiring (ADJ) only of $J_B$.
* *Robustness.* ${\rm Re}\,p_{\rm opp}$ is insensitive to an $A$-side $k^-$ form factor $\Lambda^2/(k^2+\Lambda^2)$: at $\lambda=0.003$ it is $0.00205\to0.00267$ for $\Lambda=\infty\to0.03$, while ${\rm Im}\,p_{\rm opp}$ moves from $-2.875$ to $-2.367$. The vanishing of the real part is robust; the $O(1)$ imaginary constant depends on the scheme.

**Physical reading (scope restricted).**

* *What T2 shows.* Within App O's framework, in $\mathbb M_{\rm glob}$, pointwise on $\mathcal N_A\cap\mathcal N_B$, at $O(g^4)$ and for this pattern: the side sum of the **uncut** direct lines cancels once the window is combined with the adjacent near-shell region of the same uncut lines. This is the uncut-line part of what `asm:appO-mixing`(c) prescribes.
* *What it does not show.* The cut contributions of the direct lines, which belong to $\mathcal G_0$ and to the "含实发射" clause, are not included (Remark C). In the unregulated model they are not expected to be power suppressed. So T2 does **not** establish that the $\mathcal G_0$-restricted complete-set clause holds.
* *Conditions.* The physical content is conditional on `asm:appO-collinear-ends`. With two-sided in-window regulators the uncut-line statement is T2′(c).
* *Relation to the reference.* For the uncut-line part, T2 contradicts the reference's expectation, stated in three places, that within $\mathcal G_0$ the $O(\chi^2)$ residual should not be expected to vanish (ERR-S1b, §12). T2 does not refute `asm:appO-mixing`(c), which concerns the complete set. It says nothing about the spectator-integrated cross section (OPEN-2).
* *Consistency check.* P3: two-particle unitarity of box plus crossed box for exact on-shell lines.
* *Three-gluon-vertex graphs.* They are not needed for the uncut-line cancellation; their own sum is not computed. If the complete-set clause holds, then the cut direct lines and the three-gluon-vertex graphs must together have zero net Hermitian $C_AX$ part.

**Contrast.** Boer–van Daal–Gaunt–Kasemets–Mulders, SciPost Phys. 3 (2017) 040 (read §4), find in a quark–scalar-diquark spectator model at $O(\alpha_s^2)$ that the three-gluon-vertex graph, summed over cuts, is essential to cancel the colour entanglement of the double-Boer–Mulders DY term. With their regulators the whole term sits in the double-Glauber region. There is no conflict:

* their observable is T-odd and is generated by the imaginary parts of Wilson-line denominators, i.e. by what T2 leaves regulator dependent (${\rm Im}\,p_{\rm opp}$ and the constant in it); T2's statement concerns the Hermitian $C_AX$ residual $\propto{\rm Re}\,p_{\rm opp}$;
* their surviving entangled graphs couple spectators of one hadron to the active parton of the other (SA/AS), not the SS–SS pattern of T2.

**Grades.** (a) [R, R_PT] in the model; (b) [R, R_cond] with content [P]; physical reading [P].

**Novelty (restricted).**

* *Prior art.* The physical $O(\alpha_s^2)$ cancellation for this fully coincident SS pattern was shown by explicit two-loop calculations in models with a spectator in each hadron: Lindsay, NPB 231 (1984) 397 (meson + meson, Feynman gauge, all graphs), and Brandt–Frenkel–Taylor, NPB 312 (1989) 589 (eikonal "mesons"). Lindsay–Ross–Sachrajda are not prior art for this pattern: they treat quark + hadron, with no $A$-side spectator. The reggeization reading is textbook (Lipatov; Kuraev–Lipatov–Fadin; Rothstein–Stewart).
* *New.* The derivation for general LCOPT jets inside App O's framework with explicit estimates; the ray-identity mechanism; the regulator analysis (T2′). This extends ERR-S1 from eikonal lines to composite LCOPT spectators.

### Proposition T2′ (regulated version; end poles; two-sided regulators)

The regulated statement (a) is the main physical form for the fully coincident pattern.

**(a) [R, R_PT] (model; QCD transfer as in T2(b)).** Assume the hypotheses of T2 except $\mathcal N_A$. Insert $\prod_e\chi(k_e^+)$ with $\chi$ in class $\mathfrak X$ and $\lambda_B\ll K_c\ll a/\lambda_A$. Then, up to logarithms,
$${\rm Re}\,p_{\rm opp}=O\Big((\lambda_B/K_c)^{1/2}+K_c\lambda_A/a\Big).$$

*Proof.* Steps 0–7 of T2 with $\chi(i\kappa_1)\chi(i\kappa_2)$ inserted. L5 holds with the regulator: $\chi$ is holomorphic on the swept sets (the first quadrant for $x_e>0$ and the third for $x_e<0$), and $F_A$ is holomorphic there without any condition on $J_A$'s final energies (L5, Step 1).

* (i) *Inner square.* $|\chi\chi-1|\le2R/K_c$ (with $|\chi|\le2$), which costs $O((K/K_c)l_K^2)$ in the $S_B$ term and in the real part of the $v$ term. The latter is no longer purely imaginary, since $\chi(i\kappa)$ is complex. So $K\ll K_c$ is needed.
* (ii) *Strip tail, $E$-terms, off-strip region.* $O(\lambda_B/K)$, as in T2.
* (iii) *Strips.* Apply L6 to $\tilde\rho(k):=\rho_{12}(k)\chi_+(k)\chi_-(-k)$, where $\chi_\pm$ are the half-line functions. It is holomorphic in the first quadrant ($\chi_-(-k)$ continues into the third quadrant), real on $k>0$, and $\tilde\rho(0)=1$; moreover $|\tilde\rho-1|=O(k/K_c+\lambda_Ak/a)$.
  * Without $\mathcal N_A$, $\rho_{12}$ has poles at $k_p=a_2/(2\alpha)\sim a/\lambda_A>0$, whose residues are multiplied by $\chi_+(k_p)\chi_-(-k_p)=O((K_c\lambda_A/a)^2)$. So L6's pole term is power suppressed.
  * The head $\int_0^K$ is $O(K/K_c+\lambda_AK/a)$.
* *Total.* ${\rm Re}\,p_{\rm opp}=O(\lambda_B/K+K/K_c+\lambda_AK/a+(K_c\lambda_A/a)^2)$ up to logarithms. The choice $K=(\lambda_BK_c)^{1/2}$ gives the rate, using $\lambda_AK/a\le\frac12(\varepsilon+K_c\lambda_A/a)$. This slightly over-estimates the last two terms. $\square$

*Further remarks on (a).*

* The slow convergence observed, about $\lambda^{1/2}$ for $K_c=\lambda$ with $\lambda_B\propto\lambda^2$ (0.103, 0.054, 0.028), matches the rate.
* *Mirror statement:* a regulator on $k^-$, with $\mathcal N_A$ instead of $\mathcal N_B$.
* The imaginary constant remains regulator dependent.
* The real part is regulator independent only for regulators that retain the near-shell segment. If an $A$-side $k^-$ regulator at $K^-$ is added, the statement needs $K_cK^-\gg\mathbf k_T^2$; for $K^+K^-\ll\mathbf k_T^2$ the value is set by the regulators (P2; (c)).

**(b) [R, R_PT] End poles.** Without a regulator and without $\mathcal N_A$ (keeping $\mathcal N_B$),
$${\rm Re}\,p_{\rm opp}=-\frac12\sum_p{\rm Res}_{k_p}(\rho_{12}+\rho_{21})/k_p+O(\text{power}).$$

* *Proof:* L6 with axis poles, in Step 6 of T2.
* *Scalar model.* There $\rho_{12}(k)=a_1a_2/((a_1-2d_{10}k)(a_2-2\alpha_1k))$, so ${\rm Res}(\rho_{12})/k_p=-a_1\alpha_1/(a_1\alpha_1+a_2|d_{10}|)$ (verified symbolically by both round-2 reviewers). Hence ${\rm Re}\,p_{\rm opp}=+\frac12a_1\alpha_1/(a_1\alpha_1+a_2|d_{10}|)$ if $\alpha_1>0$, and $+\frac12a_2\alpha_2/(a_2\alpha_2+a_1|d_{20}|)$ if $\alpha_2>0$.
* *Which energies enter.* Only the final-gap energies of the *mixed* sectors enter: $\alpha_1$ for $1V2$ and $\alpha_2$ for $2V1$. A positive $\alpha_0$, the first final gap of the both-final sector, gives no end-pole term, because that sector does not reach the strip. (The "apole" set has $\alpha_0=0.5625\lambda^2>0$.)
* *Location.* The poles sit at $k^+=a/(2\alpha)\sim a/\lambda_A$, the $A$-collinear end.
* *Mirror statement.* Rotating $k^-$ instead of $k^+$, valid on $\mathcal N_A$, gives the analogous end-pole formula for positive final energies of $J_B$. The case where NF fails for both jets is open (OPEN-2).
* *Interpretation.* For **massive** spectators these poles are artefacts of $\mathbb M_{\rm glob}$: exact kinematics forbids an on-shell massive spectator from absorbing an on-shell gluon, since $(s+k)^2=m_s^2$ forces $s\cdot k=0$. For **massless** partons $s\cdot k=0$ is reached for collinear $k$, so the poles are genuine $A$-collinear configurations; `asm:appO-collinear-ends` assigns them to the $A$-collinear region, or (a) removes them.
* *Numerics.*
  * apole set (method II): 0.2626, 0.2536, 0.2520 at $\lambda=0.01,0.003,0.001$, against the prediction 0.2517 (reviewer round 2: 0.25172).
  * alt set (pole in $J_B$; mirror formula; method I): 0.0692, 0.0520, 0.0490 against 0.0483 (reviewer: 0.04834). The altswap set equals alt.

**(c) [P, model] Two-sided analytic regulators.** Take $\chi^+(k^+)$ at scale $K^+$, and on both lines an $A$-side $\chi^-(k^-)=K^{-2}/(k^{-2}+K^{-2})$, which is even and line-identical. In the table below $\chi^+$ is also a Lorentzian, $K^{+2}/(k^{+2}+K^{+2})$, as implemented in `fix_r1_scripts/regulator_indep.py`, and the contour angle is $\theta\le\pi/4$. Jet $A$ is localized and jet $B$ is the base set.

* *Behaviour.* ${\rm Re}\,p_{\rm opp}\to0$ when the near-shell segment is retained ($K^+K^-\gg\mathbf k_T^2$), and $\to\frac12$ when it is excluded ($K^+K^-\ll\mathbf k_T^2$). The transition is a **crossover**: ${\rm Re}\,p_{\rm opp}=0.149$ at $K^+K^-/a=1$. The limit $\frac12$ is the value for these even, line-identical regulators; once the near-shell segment is excluded, the value depends on the regulator shape (P2).
* *Values* (`fix_r1_logs/regulator_indep_B.log`):

| $K^+K^-/a$ | $10^3$ | 10 | 1 | 0.1 | $10^{-3}$ | no $k^-$ regulator |
|---|---|---|---|---|---|---|
| $K^+=10^2\lambda_B$ | 0.0137 | 0.0122 | 0.149 | 0.448 | 0.4995 | 0.0139 |
| $K^+=10^4\lambda_B$ | 0.0002 | 0.0044 | 0.147 | 0.448 | 0.4995 | 0.00026 |

* *Independent recomputations.*
  * A round-2 reviewer reproduced the $K^+=10^2\lambda_B$ row on the **real** contour, with $\delta\to0$ and no rotation: $0.0138825-1.5646509i$ (no $k^-$ regulator), $0.0137517-1.5504271i$ ($10^3$), $0.1491170-0.2171151i$ (1), $0.4994934$ ($10^{-3}$), with $N/\mathcal J_B=0.999918-0.009210i$.
  * Round-1 reviewer, class-$\mathfrak X$ $k^+$ regulator times a Lorentzian $k^-$ regulator: 0.441, 0.4935, 0.4994 for $K^+K^-/a=0.1,0.01,0.001$.
  * A Lorentzian $k^+$ regulator (outside class $\mathfrak X$) gives 0.0453, 0.0177, 0.0072.
* *Conclusion.* With in-window regulators at both ends and $K^+K^-\gg\mathbf k_T^2$, the model has no in-window $O(g^4)$ residual for this pattern from the **uncut** lines. The cut contributions are not part of this computation (Remark C).

**Novelty.** New: the end-pole formula, the regulated proof with its rate, and the two-sided regulator study, as model statements.

### Proposition P2 (the strict window and its regulator-shape dependence)

**(a) (reference; `lem:appO-joint-localization`(c), `lem:appO-glauber-operator`).** With the strict Glauber propagator $-1/\mathbf k_{Te}^2$ and independent *symmetric* truncations of $k^-$ and $k^+$: $W=\frac14$ for every order pair, $p_{\rm opp}=\frac12$, and the residual is $-\frac14C_A\chi^2X$.

**(b) [R, R_PT] General independent regulators.** Take the strict-Glauber limit ($|z_e|\to\infty$, i.e. the near-shell region excluded), with both jets eikonal-localized. Put independent regulators $\chi^X_1,\chi^X_2$ on jet $X\in\{A,B\}$, as functions of **the light-cone energy injected into jet $X$** ($q=k^-$ for $A$; $q=p=-k^+$ for $B$). Define
$$\delta_X:=\frac1{2\pi}\,{\rm PV}\!\int\chi^X_1(q)\chi^X_2(-q)\frac{dq}{q}\Big/\big(\chi^X_1(0)\chi^X_2(0)\big).$$
Then $w^X_{12}=\frac12+i\delta_X$, $w^X_{21}=\frac12-i\delta_X$, and the identity
$$p_{\rm opp}=\tfrac12+2\delta_A\delta_B$$
holds. If $\delta_B$ is defined with $k^+$ instead of $p=-k^+$ as the variable, the sign of the last term flips: $p_{\rm opp}=\frac12-2\delta_A\delta_B^{(k^+)}$.

*Proof.*

* *Three-sector identity.* Summing the three sectors of colour order $[12]$ gives the time-ordered product with no restriction relative to $V_H$, since by (EQ) the equal-time value does not depend on the position of $V_H$. Hence
$$J^{[12]}_{\rm eik}(q_1,q_2)=\mathcal J\,2\pi\delta(q_1+q_2)\,\frac{i}{q_1+i0},$$
and $J^{[21]}_{\rm eik}$ has $i/(-q_1+i0)$ instead.
* *Weights.* Integrate against $\chi_1\chi_2$ and use $i/(q+i0)=i\,{\rm PV}(1/q)+\pi\delta(q)$.
* *Factorization.* In the strict-Glauber limit the propagators do not depend on $k^\pm$, so $I(\pi_A,\pi_B)$ factorizes and $W(\pi_A,\pi_B)=w^A_{\pi_A}w^B_{\pi_B}$. Then $p_{\rm opp}=w^A_{12}w^B_{21}+w^A_{21}w^B_{12}=\frac12+2\delta_A\delta_B$.
* *Orientation.* The change of variables $p=-k$ gives $\delta^{(p)}_B=-\delta^{(k^+)}_B$. $\square$

**(c) [R, R_PT] Consequences.**

* $p_{\rm opp}=\frac12$ iff $\delta_A\delta_B=0$. This happens in particular for even regulators, or for **line-identical** ones ($\chi_1=\chi_2$ makes $\chi_1(q)\chi_2(-q)$ even), on at least one side.
* *Sharp windows.* Independent sharp windows (line 1 $[-K_1,K_2]$, line 2 $[-K'_1,K'_2]$) give the real value $\delta=\ln\big(\min(K_2,K'_1)/\min(K_1,K'_2)\big)/(2\pi)$. So $p_{\rm opp}=\frac12+2\delta_A\delta_B$ can take **any real value**; it lies in $[0,1]$ iff $|\delta_A\delta_B|\le\frac14$.
* *Rational regulators.* Non-even, line-dependent regulators $\chi_e(q)=K_{1e}K_{2e}/((K_{1e}+iq)(K_{2e}-iq))$ give complex $\delta$. For example $w_{12}=97/105$ for $(K_1,K_2;K'_1,K'_2)=(1,3;4,\frac12)$, identical to the regulator-pole race of L1′.

**Diagnosis.**

* Excluding the near-shell region decorrelates the orderings in the two jets; what remains is fixed by the regulators alone.
* $\frac12$ is the symmetric-regulator value, not a universal one. This is the quantitative form of the reference's "a property of the regularization" (its Lemma E.48(d)), and the near-shell mechanism is that of the reference's own Rem. E.32 and E.49(2).
* With exact propagators and regulators that retain the near-shell segment ($K^+K^-\gg\mathbf k_T^2$), ${\rm Re}\,p_{\rm opp}\to0$ independently of the regulator (T2, T2′(a),(c)).

**Verification.**

* `fix_r2_scripts/p2_window_shape.py` → `fix_r2_logs/p2_window_shape.log`, ALL PASS: sharp windows against the formula; Lorentzian regulators with line-dependent scales ($\delta=0$); rational regulators (PV formula equals the L1′ race to $10^{-15}$); the identity.
* **Orientation check (final round):** `final_scripts/p2_orientation.py` → `final_logs/p2_orientation.log`, ALL PASS.
  * The weights are computed **exactly by iterated residues of the three LCOPT sector terms**, without using the PV formula: $w_{12}=97/105$, $43/455$, $1/2$, $7/72$, with $I_{12}+I_{21}=1$.
  * They agree with $\frac12+i\delta$ in each jet's own energy variable.
  * For $B$-side regulators given as functions of $k^+$, $\delta_B^{(p)}=-\delta_B^{(k^+)}$.
  * $p_{\rm opp}$ from the exact factorized weights equals $\frac12+2\delta_A\delta_B^{(p)}=\frac12-2\delta_A\delta_B^{(k^+)}$.
* Reviewer checks: `review_r2_2_scripts/chkB_window_shape.py`; `review_r3_2_scripts/r3_quadrant_P2.py` (97/105 three ways).

**Novelty.** (a) is the reference's. The formula (b) and the classification (c) are new (elementary).

### Proposition P3 (on-shell lines) — [R, R_PT] at $O(g^4)$; known in substance

**Statement.** Take two on-shell external lines (massive scalars, or time-like eikonal lines) with exact gluon propagators and a gluon-mass IR regulator. At $O(g^4)$, box plus crossed box obey exact two-particle unitarity,
$${\rm Disc}_s({\rm box}+{\rm crossed})=\int d\Phi_2\,T_1^\dagger T_1,$$
by Cutkosky's rules applied graph by graph (Cutkosky 1960; Veltman 1963; 't Hooft–Veltman).

* *No cut of the crossed box.* The crossed box has no $s$-channel cut: a cut through both lines between their vertices must also cut both gluons, i.e. it requires a single on-shell emission from an on-shell massive line, which is forbidden.
* *Higher cuts.* Three-particle cuts appear only at $O(g^6)$.
* *High-energy limit.* $p_{\rm opp}$ is purely imaginary there (ERR-S1: $-iY/\pi$; `prop:dy-eikonal-twogluon`). The residual of the strict window is not a property of the exact graphs.

**Remark (supporting evidence only; not certified).** For three on-shell lines $(i;j_1;j_2)$, the $O(g^4)$ relation $\mathcal M+\mathcal M^\dagger+\mathcal M^\dagger\mathcal M=0$ with only physical three-line cuts suggests $W_{12}+W_{21}^*=1$, i.e. no half-coincident residual for exact on-shell lines. A complete argument must also include the graphs that combine an $(i$–$j_e)$ exchange with a $(j_1$–$j_2)$ exchange, whose colour factor has the same $f\,T_iT_{j_1}T_{j_2}$ structure (OPEN-9).

### Proposition P4 (per-graph weights of a fully coincident pair are not fixed by window data)

**Definitions.** $D_{\rm win}(J_X):=\{\mathcal J_\sigma\text{ for all sectors};\lambda_X\}$, and $D:=(D_{\rm win}(J_A),D_{\rm win}(J_B),a_e,\mathbf k_{Te})$.

**Class.** The hypotheses of T2(a): $J_A$ satisfies (SEC), (EQ), (REAL) on $\mathcal N_A$; $J_B$ satisfies (SEC), (EQ), (ADJ), (REAL) on $\mathcal N_B$. The class imposes (ADJ) on $J_B$ only; that is all T2 needs. Items (a), (b) are statements about this class, [R, R_PT]. Whether graph-generated QCD jets realize the perturbations used in (b) is OPEN-10. Membership of QCD jets in the class is as in T2(b).

**(a) [R, R_PT].** $W(12,21)=W^{\rm in}+W^{\rm out}$, where $W^{\rm out}=-\frac{i}{2\pi}\int_K^\infty\frac{d\kappa}\kappa\varrho_{12}(\kappa)+O(\lambda_B/K)$ (T2, Step 4) and $W^{\rm in}$ depends on $J_A$ only through $D$, up to $O(\lambda_AK/a_{\min})$.

**(b) [R, R_PT] The perturbation.** Add to the mixed sector $1V2$ of $J_A$ the two-state term
$$s\,c_2\,\frac{i}{A_1+k_1}\,\frac{i}{A_2+k_1}\,\frac{i}{A'-k_2},\qquad c_2=-i\tilde c_2,\quad\tilde c_2/\mathcal J_A\in\mathbb R,\quad|A_1|,|A_2|\le\lambda_A,\quad A_1,A_2,A'<0 .$$

* *What it preserves.* (SEC), (EQ) and $D$, since no single-state term is added, and (REAL), by the phase choice.
* *What it breaks.* It does **not** preserve (ADJ) for $J_A$: its final gap $i/(A'-k_2)$ is single-state, and (ADJ) for the adjacent pair $(V_H,2)$ would require a partner $s\,c_2[i/(A_1+k_1)][i/(A_2+k_1)][i/(A''+k_1+k_2)]$ in sector $12V$. This is harmless, because the class imposes (ADJ) on $J_B$ only.
* *Effect.* $\varrho_{12}$ changes by $s\rho_2(i\kappa)$, with
$$\rho_2(k)=\frac{a_1a_2}{\mathcal J_A}\,\frac{2k\tilde c_2}{(2kA_1-a_1)(2kA_2-a_1)(2kA'-a_2)},\qquad\delta W(12,21)=-\frac{is}{2\pi}\int_0^\infty\frac{dk}k\rho_2(k)+o(1).$$
  The rotation to the real axis is Cauchy's theorem: $\rho_2$ is holomorphic in ${\rm Re}\,k>0$, real on $k>0$, $\rho_2(0)=0$ and $\rho_2=O(k^{-2})$. The head $\int_0^K$ is $O(\lambda_AK/a)$.
* *Sign.* For $k>0$ each bracket is negative, so $\rho_2$ has the fixed sign $-{\rm sgn}(\tilde c_2/\mathcal J_A)$ on $(0,\infty)$. Therefore $\delta W(12,21)$ is purely imaginary and **non-zero whenever $\tilde c_2\ne0$**.
* *Values.* $\delta W/s=+0.0615i,\ +0.0599i,\ -0.0790i$ for three parameter sets, with closed forms $\int\rho_2dk/k=1-\ln4$, $-0.37619672$ and $\frac{39}{50}\ln6-\frac{13}{10}\ln2$ (round-2 reviewers, sympy and `chkE_P4.py`).
* *With the (ADJ) partner* (if (ADJ) is also wanted for $J_A$). A round-3 reviewer added the partner in $12V$. It changes $\delta W(12,21)$ only at power level: $-7\times10^{-5}i$ at $\lambda=0.01$ and $-1.6\times10^{-5}i$ at $\lambda=0.003$, against $+0.0078i$. The shift formula is confirmed independently ($+0.007838i$ predicted, $+0.00785i$ computed; `review_r3_1_logs/t2_general.log`). This is consistent with the estimate $O(\lambda_AK/a+\lambda_B/K)$: the $BB$ sector never reaches the strip.

**(c) [P, model] $G7$-regulated version.**

* With in-window regulators (class $\mathfrak X$ on $k^+$ at $K^+\ll a/\lambda_A$, and a $k^-$ regulator at $K^-$), the $A$-side out-of-window dependence of (b) is suppressed: $\rho_2(i\kappa)=O(\lambda_A\kappa/a)$ for $\kappa\ll a/\lambda_A$, so $\delta W=O(K^+\lambda_A/a)$.
* The per-graph weights still depend on the in-window **shape** of the mixed sectors of $J_B$. Example: add to the mixed sectors $1V2$ and $2V1$ of the base jet $B$ the two-state term $s(-\mathcal J_B)\,r\,[i/(A_1+p_1)][i/(A_2+p_1)][i/(A_3-p_2)][i/(A_4-p_2)]$ and its mirror, with $|A_i|\le\lambda_B$ and $r=\lambda_B^2/2$.
  * This leaves $D_{\rm win}(J_B)$, (EQ), (ADJ) and (REAL) unchanged, since all gaps are two-state, and $\int\delta J=0$.
  * It changes $W(21,12)$ by $-0.0287i$ with $G7$ regulators ($K^+=10^2\lambda_B$, $K^+K^-/a=10^3$).
  * Without regulators (jet $A$ localized) the change is $-0.0308i$, against the prediction $-0.0309i$ from Step 3 of T2.
  * The real part of $\delta p_{\rm opp}$ is $5.5\times10^{-4}$ ($G7$) and $3\times10^{-6}$ (unregulated) (`fix_r2_logs/p4_regulated_B.log`).
  * In the same runs, perturbations confined to the all-initial sector left the per-graph weights unchanged to $\le10^{-5}$. This selection is observed, not proved (OPEN-10).

**Consequence.**

* Within the class, no **per-graph jet-local rewriting** that replaces each jet by its window data $D$ can satisfy per-graph weak equivalence with an error $C\lambda^aL^K$ for coincident pairs. For the unregulated $\mathbb M_{\rm glob}$ integrand this follows from (b) [R, R_PT]; with $G7$ regulators, from the example in (c) [P].
* For graph-generated (physical LCOPT) jets the statement is open (OPEN-10).
* All these shifts are purely imaginary in the side sum, so ${\rm Re}\,p_{\rm opp}$ is unaffected. The envelope `asm:appO-envelope` must therefore be imposed on side-summed families for coincident connections (§2.3).

**Proof of (a), (b).** Step 4 of T2 applied per colour pair, with $F_A^{[12]}(-k,k)=-\frac{1}{4k^2}J^{(1V2)}(z_1,z_2)$, $z_1=-a_1/(2k)$, $z_2=a_2/(2k)$ (L3). $\square$

**Novelty.** New; it sharpens ERR-S3.

---

## 8. The half-coincident pattern

### Theorem T3 (half-coincident pair: the unregulated two-time model and a sensitivity proposition)

*Proposed placement:* remark `rem:appO-halfcoinc` in §O.5, with (e) as the proposition `prop:appO-halfcoinc-sensitivity`.

**First sentence (scope).** In $\mathbb M_{\rm glob}$, on $\mathcal N_B$, at $O(g^4)$, for two **uncut** SS lines $i$–$j_1$ and $i$–$j_2$ on the amplitude side ($j_1\ne j_2$ spectators of $J_B$), the following holds.

**Hypotheses.**

* $J_A$ satisfies (SEC) and (EQ). $J_B$ satisfies (SEC), (EQ), (ADJ), (REAL).
* The configuration lies in $\mathcal N_B$, and $\varepsilon\ll1$, with smallness conditions of the type (iv), (v) of T2.
* No rapidity regulator is used unless stated.

*Structure of $J_B$.* The two $B$-insertions sit on different spectators, so $J_B$ carries no colour order. $f_B(\kappa):=J_B(-i\kappa)$, the sum of all six sectors, is an $S$-type function in the sense of L8: its strip terms cancel between the two time orders by (ADJ). It obeys L8(b)–(d),(g) for $S$, and L8(f): $\int f_B\,d^2\kappa/(2\pi)^2=-\mathcal J_B$.

*Grades.* The items graded [R, R_PT] below are statements about the defined class in the model. For leading-power LCOPT jets of QCD graphs they hold as in T2(b): [R, R_cond: `asm:appO-lcopt`, `asm:appO-adjacent-swap`†, `asm:appO-real-jets`†], with content grade [P]. The physical reading is at most [P].

**(a) [R, R_def].** $\mathcal R=2ic_1c_2\,{\rm Im}W_{12}\,[X_1,X_2]$ (L4(b), with $c_e$ real).

**(b) [R, R_PT].**
$$W_{12}=\frac12-\frac1{\mathcal J_B}\int v(\kappa)f_B(\kappa)\frac{d^2\kappa}{(2\pi)^2}+E_b,$$
and the integral is **purely imaginary**. Indeed, by (REAL) for $J_B$, $f_B(-\kappa)=e^{2i\varphi}\overline{f_B(\kappa)}$ and $\mathcal J_B\in e^{i\varphi}\mathbb R$, while $v$ is real and odd. The error satisfies $|E_b|\le C_b\,\varepsilon(1+L')^2$ with $L':=\ln(1+a/(\lambda_A\mu_B))$, and $C_b$ is an explicit polynomial in $m_A$, $m^\flat_A$, $m^\flat_B$, $a_{\max}/a_{\min}$. Hence ${\rm Re}\,W_{12}=\frac12+O(\varepsilon L'^2)$.

*Proof.*

* *Numerator and denominator.* $W_{12}=I_{12}/N$, with $I_{12}=-\frac{\mathcal J_A}{a_1a_2}\int h_{12}f_B$ (L5), and $N$ the same with $h_{12}+h_{21}$.
* *$A$-side input.* Use (A1) for $R\le a_{\min}/(2\lambda_A)$, i.e. $h_\pi=w^{[\pi]}+e_\pi$ with $|e_\pi|\le4m_A\lambda_AR/a_{\min}$, and $|h_\pi|\le m^\flat_A$ beyond (A2).
* *$B$-side input.* For $S$-type $f_B$, L8 gives
$$\int_{R\le X}R|f_B|\le CM^\flat_B\lambda_B\big(1+\ln(1+2X/\mu_B)\big)^2,\qquad\int_{R>X}|f_B|\le CM^\flat_B(\lambda_B/X)\big(1+\ln(1+2X/\mu_B)\big).$$
  The off-strip region uses $|f|\le400M^\flat\lambda/(R^2\langle m\rangle)$; the strip uses $|E|\le16M^\flat\lambda/(R^2\langle r_P\rangle)$, since the $g$ terms cancel.
* *Conclusion.* With $X=a_{\min}/(2\lambda_A)$, the errors of numerator and denominator are $O(\varepsilon(a/a_{\min})(1+L')^2)$. L8(f) fixes the normalization $-\frac1{\mathcal J_B}\int f_B=1$. The imaginarity follows from the symmetry $\kappa\to-\kappa$ exactly as in Step 3 of T2. $\square$

**(c) [R, R_PT].** ${\rm Im}W_{12}=0$ for configurations symmetric under $1\leftrightarrow2$: then $W_{12}=W_{21}$, and since $W_{12}+W_{21}=1$, $W_{12}=\frac12$.

**(d) [P, model].** ${\rm Im}W_{12}=O(1)$ in general. Values:

* Model $B\to b+s_1+s_2$: $W_{12}=0.49788-0.03663i,\ 0.49980-0.03161i,\ 0.499992-0.03069i,\ 0.49999912-0.03058i$ at $\lambda=0.03,0.01,0.003,0.001$ (`scripts/halfcoinc.py`; real-contour `scripts/halfcoinc_real.py` identical).
* These tend to the localized limit $0.5-0.030559i$. A round-2 reviewer reproduced it on the real contour without rotation: $0.5000000-0.0305591i$.
* Symmetric configuration: $-0.000028i$. $B$-asymmetric: $+0.0468i$ (real contour $+0.0468158i$). Asymmetric $a_e$: $-0.0212i$ (`scripts/halfcoinc_sym.py`).
* *Colour note.* In this very model B-rem $=\{j_1,j_2\}$, so by L4(d1) its own DY colour factor $\langle\psi|[X_1,X_2]|\psi\rangle$ **vanishes identically**. The $O(1)$ ${\rm Im}W_{12}$ matters only in configurations with a further $B$-remnant parton and complex colour phases (L4(d3)).

**(e) [R, R_PT] Sensitivity proposition.** Put the even Lorentzian regulator $\chi_K(k^-)=K^2/(k^{-2}+K^2)$ on the $A$-side minus components of both lines, with $\lambda_A\ll K\ll a/\lambda_B$. Then
$$\Big|W_{12}(K)-\frac12\Big|\le C_e\Big[\frac{K\lambda_B}{a_{\min}}\Big(1+\ln\Big(1+\frac{a_{\min}}{K\mu_B}\Big)\Big)^2+\frac{\lambda_A}{K}\Big(1+\ln\Big(1+\frac{a_{\min}}{K\mu_B}\Big)\Big)^2+\varepsilon(1+L')^2\Big].$$
$C_e$ is an explicit polynomial in $m_A$, $m^\flat_A$, $m^\flat_B$ and $a_{\max}/a_{\min}$; crudely, $C_e\le10^6m^\flat_B(1+m_A+m^\flat_A)\,a_{\max}/a_{\min}$.

*Boost invariance.* Every term is boost invariant. Under $k^+\to e^yk^+$ and $k^-\to e^{-y}k^-$, the combinations $K\lambda_B/a$, $\lambda_A/K$ and $a/(K\mu_B)$ are invariant, since $K$ is a $k^-$ scale and $\mu_B$ a $k^+$ scale (`final_logs/t3f_recompute.log`). The round-2 statement had $\ln(1+K/\mu_B)$ in the second term; that combination is not boost invariant ($\propto e^{-2y}$) and was corrected.

*Proof.*

* *(1) Rotation.* L5 at $\theta=\pi/4$ with the regulator. For $\theta<\pi/2$ there is no collision of $z_e$ with $\mp iK$, and $F_A^{\rm reg}$ is holomorphic on the swept set.
* *(2) Localization with the regulator.* On the $\pi/4$ contour the final group $\{z_e,-iK\}$ and the initial group $\{z_e,+iK\}$ lie in closed quadrants (L1′, example). So L1′(b) holds with $\sum|w|\le2$ and $\sum_p|u_e(p)|\le c_U$. The gap momenta satisfy $|K_l|\ge\min(a_{\min}/(2R),K)$ by the closed-quadrant property. Hence $F_A^{\rm reg}=\frac{\mathcal J_A}{a_1a_2}[w_K+e_K]$ with
$$|e_K|\le32c_U^2m_A\lambda_A\max(1/K,\,2R/a_{\min})\qquad(K\ge2\lambda_A,\ R\le a_{\min}/(4\lambda_A)).$$
* *(3) The regulated weight.* $v_K:=w_K^{[12]}-\frac12$ depends only on $x_e:=iK/z_e$, with $|x_e|=2K|\kappa_e|/a_e$. It satisfies $|v_K|\le(|x_1|+|x_2|)/4$ for $|x_e|\le\frac14$, and $|v_K|\le\frac12$ everywhere, in all four quadrants. Hence $|v_K|\le\min(\frac12,\,8KR/a_{\min})$.
* *(4) Integration.* Apply L8(h) ($\theta=\pi/4$, constants ×8) to the $S$-type $f_B$:
  * split $\int|v_K||f_B|$ at $R=X_K:=a_{\min}/(16K)$; this gives the first term, with logarithm $\ln(1+2X_K/\mu_B)\le\ln(1+a_{\min}/(K\mu_B))$;
  * split $\int|e_K||f_B|$ at $R=a_{\min}/(2K)$, where $1/K=2R/a_{\min}$:
    * the inner part gives $(\lambda_A/K)\int_{R\le a_{\min}/(2K)}|f_B|$, i.e. the second term, with logarithm $\ln(1+2a_{\min}/(K\mu_B))$, a $k^+$ scale over a $k^+$ scale;
    * the part $a_{\min}/(2K)<R\le a_{\min}/(4\lambda_A)$ gives $(\lambda_A/a_{\min})\int R|f_B|=O(\varepsilon(1+L')^2)$;
    * the region $R>a_{\min}/(4\lambda_A)$, where $|F_A^{\rm reg}|$ is bounded, gives $O(\varepsilon(1+L'))$.
* *(5) Normalization.* $N(K)/N_0=1+O(\text{the same})$. $\square$

*What (e) shows, and what it does not.* The unregulated model has ${\rm Im}W_{12}=O(1)$ (part (d)). With the in-window Lorentzian $A$-side regulator, $W_{12}(K)-\frac12$ is power suppressed by the bound above. The regulator $\chi_K$ suppresses $|k^-|\gtrsim K$, but it also changes the integrand at $|k^-|\ll K$ by a relative $O((k^-/K)^2)$. Hence:

* the proved statement is that **any in-window Lorentzian suppression of $|k^-|\gtrsim K$ removes the $O(1)$ part of ${\rm Im}W_{12}$, up to the stated bound**;
* this does *not* by itself show that the $O(1)$ part is "not determined by the integrand on a window"; it shows that the $O(1)$ part is not stable under in-window regulators of this type.

This is the representation-independent content of the withdrawn "location" statement.

**(e′) [R, R_PT] (algebraic) + [P] (numerics).**

* *Leading term.* $v_K=(x_1-x_2)/4+O(|x|^2)=\frac{iK}4(1/z_1-1/z_2)+\dots$, i.e. $v_K\approx\frac{iK}2(k_1^+/a_1-k_2^+/a_2)$ for $|z_e|\gg K$. Numerically, $|v_K-(x_1-x_2)/4|\le0.044(|x_1|+|x_2|)^2$.
* *Linear behaviour in $K$* (recomputed in the final round, `final_logs/t3f_recompute.log`, at $\theta=\pi/8$ and $\pi/4$ agreeing to $\le2\times10^{-8}$). For $K=0.1,0.01,0.001\,a/\lambda_B$:
  * author set: ${\rm Im}W_{12}(K)/(K\lambda_B/a)=-0.0500,\ -0.0601,\ -0.0612$;
  * $B$-asymmetric set: $+0.0435,\ +0.0500,\ +0.0468$.

  The behaviour is linear in $K$ up to slowly varying factors, so the logarithms of the proven bound are not sharp. This is consistent with (e′) and a symmetric-limit first moment of $J_B$.

**(f) [P, model] Regulator dependence.**

* Author set: ${\rm Im}W_{12}=-0.030560,\ -0.030541,\ -0.029750,\ -0.020357,\ -0.004999,\ -0.000601,\ -0.0000612$ for $K=10^4,10^2,10,1,0.1,0.01,0.001\times a/\lambda_B$, with ${\rm Re}W_{12}=\frac12$ to $3\times10^{-7}$ (`fix_r1_logs/regulator_indep_A.log`; recomputed for $K\le1$ in `final_logs/t3f_recompute.log`).
* $B$-asymmetric set: $+0.046818\to+0.000047$ over the same range of $K$.
* Real contour without rotation (round 2): $-0.0297491,\ -0.0203564,\ -0.0049989,\ -0.00060104$ for $K=10,1,0.1,0.01$ (`review_r2_1_logs/t3_realcontour_r2_reg.log`).
* In the strict window, $W_{12}=\frac12$ exactly for even, line-identical regulators (P2).

**(g) [R, R_def] Colour.** $\mathcal R$ vanishes for valence (minimal-Fock) remnants with B-rem $=\{j_1,j_2\}$, for real colour states, and in the abelian theory (L4(d)). Generic multi-parton remnants with complex colour amplitudes are not covered; whether the remnant-integrated residual vanishes is open (OPEN-1).

**(h) Unitarity.** For exact on-shell lines the residual is expected to be absent (P3, Remark). This is not certified (OPEN-9).

**(i) Incompleteness.** The coincident SA patterns ($i$–$j_e$ together with $i$–$b$, where $b$ is $B$'s active parton) carry the same colour structure once colour conservation $\mathbf T_b=-\sum_{j\in\text{B-rem}}\mathbf T_j$ is used. The Lindsay–Ross–Sachrajda cancellation for baryon targets involves AS-type insertions (there is no $A$-spectator), so it is analogous in mechanism, not identical. These patterns were not included.

**(j) Scope.** Only uncut SS lines are included. The cut contributions of the $i$–$j_e$ lines (Remark C) are not.

**Conclusion.**

* In App O's framework, with global $\mathbb M_{\rm glob}$ jets, exact propagators and no $k^-$ regulator, the uncut half-coincident family leaves $2ic_1c_2\,{\rm Im}W_{12}[X_1,X_2]$ with ${\rm Im}W_{12}=O(1)$.
* This residual is removed, up to power corrections, by any in-window even Lorentzian $A$-side $k^-$ regulator (proved bound (e)).
* Its colour factor vanishes for valence remnants and for real colour states, including the model's own configuration.
* Its fate in QCD is the matching question of `asm:appO-collinear-ends` at the $k^-$ end (OPEN-1, OPEN-6), together with the cut contributions (OPEN-13).
* *Regulators.* The half-coincident part of `asm:appO-collinear-ends` is proved here with the $k^-$ regulator **alone**. Including in addition the class-$\mathfrak X$ $k^+$ factor of the two-sided window is expected to cost $O(a/(K^+K^-))$ by the same estimates; this is **not proved**.

**Novelty.** The model computation and (e) are new, to our knowledge. The configuration (one $A$-spectator connected to two different $B$-spectators) does not occur in Lindsay 1984 or in Brandt–Frenkel–Taylor 1989 (one spectator per hadron), nor in Lindsay–Ross–Sachrajda (no $A$-spectator).

---

## 9. Beyond $O(g^4)$ uncut coincident pairs

### Proposition P5 (at $O(g^6)$ the direct-line ladder class is not closed under unitarity) — [A]

**Setting.** Two on-shell eikonal (or massive) lines $A$ and $B$. $\mathsf C$ is the class of direct-line ladder graphs at $O(g^6)$: all three gluons join the two lines, with any crossings.

**Definition (unitarity defect).**
$$D_{\mathsf C}:={\rm Disc}_s\Big(\sum_{\Gamma\in\mathsf C}\Gamma\Big)-\int d\Phi_2\,(\mathcal M_{\mathsf C})^\dagger\mathcal M_{\mathsf C}\quad\text{at }O(g^6).$$
It is the part of the class's $s$-channel discontinuity that is not reproduced by two-line intermediate states built from the class's own lower-order amplitudes.

**Statement.**

**(i) The defect is an interference term.** By Cutkosky's rules applied graph by graph, $D_{\mathsf C}$ is the sum of the three-particle cuts of class-$\mathsf C$ graphs. A three-particle cut cuts one rung whose two ends lie on **opposite** sides of the cut: line $A$ on one side, line $B$ on the other. Hence
$$D_{\mathsf C}=\int d\Phi_3\,\big[A_A^\dagger A_B+A_B^\dagger A_A\big].$$
Here $A_X$ is the tree $2\to3$ amplitude with one gluon exchanged between the lines and one gluon radiated from line $X$, with emissions before and after the exchange combined. The self terms $A_A^\dagger A_A$ and $A_B^\dagger A_B$, in which a gluon is emitted and absorbed by the same line, lie outside $\mathsf C$.

**(ii) Sign in Feynman gauge.** For straight lines, emissions before and after the exchange combine into the line part of the Lipatov vertex (Lipatov 1976; Kuraev–Lipatov–Fadin 1977; Del Duca 1995):
$$A_A\propto C\,\frac{v_A^\mu}{v_A\cdot k},\qquad A_B\propto-C\,\frac{v_B^\mu}{v_B\cdot k},\qquad C=f^{a_1a_2b}\,T_A^{a_1}T_B^{a_2},$$
with the common colour operator $C$ ($b$ is the colour of the radiated gluon) and the common factor $1/\mathbf q_T^2$. In Feynman gauge (polarization sum $-g_{\mu\nu}$),
$$D_{\mathsf C}\propto\int d\Phi_3\,C^\dagger C\;\frac{2\,v_A\cdot v_B}{(v_A\cdot k)(v_B\cdot k)}\ \ge0 .$$
This is non-zero in the non-abelian theory. In the abelian eikonal limit the line part vanishes outside the collinear regions. The self terms are $-C^\dagger C\,v_X^2/(v_X\cdot k)^2\le0$, and zero for light-like lines. So $D_{\mathsf C}$ equals $\int|A_A+A_B|^2$ only for light-like lines or in the Regge limit.

**(iii) Gauge dependence.** $\mathsf C$ is not gauge invariant, so $D_{\mathsf C}$ is gauge dependent. In a light-cone gauge the interference term differs. The full $|A_A+A_B|^2$ is gauge invariant, because the total current is conserved: $k\cdot(J_A+J_B)=1-1=0$.

**Conclusion.**

* In Feynman gauge with eikonal lines, $D_{\mathsf C}\ne0$: the class $\mathsf C$ is not closed under unitarity.
* The gauge-invariant $2\to3$ amplitude needs the three-gluon-vertex term, i.e. the full Lipatov vertex.
* In DY, part of this real emission corresponds to cut direct lines (inside $\mathcal G_0$), and part to soft lines emitted and absorbed by the same spectator (outside $\mathcal G_0$).

**Qualification.** The conclusion concerns the closure of $\mathcal G_0$ under unitarity, i.e. the SS-family bookkeeping. It is not a failure of factorization. It is consistent with Schwartz–Yan–Zhu, PRD 97 (2018) 096017 (pure Glauber ladders cancel for single-scale observables; the leading violation needs the Lipatov vertex), and with Rothstein–Stewart, JHEP 08 (2016) 025.

**Grade.** [A]. This is an argument whose substance is standard (BFKL). The interference identity and its Feynman-gauge sign are checked numerically for eikonal currents.

**Verification.**

* `final_scripts/p5_interference.py` → `final_logs/p5_interference.log`, ALL PASS. The Feynman-gauge interference equals $2v_A\cdot v_B/((v_A\cdot k)(v_B\cdot k))$ to $4\times10^{-16}$ and is positive. The self terms are $\le0$, and vanish for light-like lines. $|A_A+A_B|^2$ agrees between Feynman and light-cone gauge to $10^{-10}$, while the interference alone differs by factors up to $10^3$.
* `review_r3_2_scripts/r3_P5_cut_structure.py`: cross/full $=2.9$–$3.5$ at $Y=0.5$, $1.005$–$1.12$ at $Y=3$, and $1.000001$ at $Y=8$.

**Novelty.** The formulation is new; the substance is standard (BFKL). The round-2 identity $D_{\mathsf C}=\int d\Phi_3|A^{\rm lines}|^2$ and its justification ("a sum of $B^\dagger B$ terms") are withdrawn (§16).

### Remark P6 (coincident SA/AS insertions and H-emission endpoints: where the obstruction lies) — ungraded

* **(a) Coincident SS + SA on one $A$-spectator.** Take one SS line and one SA line whose $B$-end sits on an active line absorbed by $V_H$.
  * The $A$-localized weights $W_\pi(k^+_{\rm SS},k^+_{\rm SA})$ of L1 are continuous but not analytic at $k^+_{\rm SA}=0$ (L2), and they depend on the ratio $k^+_{\rm SA}/k^+_{\rm SS}$.
  * The $k^+_{\rm SA}$ integral against $B$'s active-line factor $\Phi_B$ is dominated by $|k^+_{\rm SA}|\sim\lambda_B$, where $\Phi_B$ is not eikonal.
  * The reference's uniform deformation, which produces the past-pointing Wilson line, needs analyticity across 0. Deforming each half line separately leaves a non-eikonal neighbourhood of 0 with $O(1)$ weight.
* **(b) H-emission endpoints.** The same holds there ($c_j=\theta(k_j^+)$).
* **(c) Non-coincident SA line.** For a non-coincident SA line the $A$-factor does not depend on $k^+$, and the reference's deformation works.

*Status.* This is an argument, not a theorem; "a half-line deformation does not cure it" is not proved. It uses $\mathbb M_{\rm glob}$ and inherits the regulator sensitivity of the weights (T3(e)). It refines `asm:appO-deformation`(d) and `rem:appO-h-emission`. The obstruction is non-analyticity in the region that dominates the integral, not the discontinuity itself. Open item: OPEN-4.

### Remark C (cut direct SS lines) — ungraded power counting

**Setting.** In $\mathcal G_0$ a direct SS gluon may cross the final-state cut: it is emitted by spectator $i$ in the amplitude and by spectator $j$ in the conjugate amplitude. `asm:appO-mixing`(c) includes these real-emission contributions together with the near-shell region. An on-shell gluon has $2k^+k^-=\mathbf k_T^2$, so these contributions lie outside every window. They are **not** part of the side sums of T2, T2′ and T3.

**Power counting in $\mathbb M_{\rm glob}$.** This is a careful estimate, not a proof.

* **(i) A single insertion alone on one side of a jet localizes.** In the eikonal regime the sector sum $J^{\rm in}+J^{\rm fi}$ of one spectator insertion equals $2\pi\mathcal J\delta(q)+r(q)$, with $|r(q)|\lesssim M\lambda/q^2$ for $|q|\gg\lambda$ (`lem:appO-insertion-values`(c)). The on-shell condition forbids $q=0$ for $\mathbf k_T\ne0$, so a cut line attached alone on its side of a jet contributes only through $r$.
* **(ii) Two insertions on the same side of a jet do not localize.** If one of them belongs to a cut line, the colour-ordered eikonal form is $2\pi\mathcal J\delta(q_1+q_2)\,i/(q_1\pm i0)$ (P2(b)), which is not suppressed at large $q_1$. Take the cut gluon on the $A$ amplitude side with its $B$ end on the conjugate side, and the uncut gluon on the amplitude side. Combining the δ-like single insertion on each side of $J_B$ with the on-shell condition $k_1^+=a_1/(2k_1^-)$ forces $|k_1^-|\gtrsim a/\lambda_B$. The result is an $O(N_0)$ contribution at the $B$-collinear end; the mirror cut gives the same at the $A$-collinear end.
* **(iii) Suppressed cuts.** Cuts that put both jets' insertions on opposite sides, or that cut both gluons, are suppressed by (i).

So in the unregulated $\mathbb M_{\rm glob}$ the cut contributions of the fully and half-coincident patterns are **not expected to be power suppressed**. They sit at the collinear ends, where `lem:appO-glauber-pc` fails, just as T2's $-\frac12$ does.

**With the two-sided regulators** of Def. D8, the retained part of the mass shell has $k^+\ge a/(2K^-)\gg\lambda_B$ and $k^-\ge a/(2K^+)\gg\lambda_A$. Every cut configuration then contains a jet in which a single insertion sits alone on its side, far above the jet's scale. By (i) this suggests $O(\lambda_BK^-/a+\lambda_AK^+/a)$, up to logarithms.

**Status.** Power counting only; recorded as OPEN-13. Consequently the physical readings of T2, T2′(c) and T3 refer to the uncut lines; ERR-S1b and §13 are restricted accordingly; and the matching of `asm:appO-collinear-ends` must also absorb the collinear-end cut contributions.

---

## 10. Comparison with other all-order arguments

**Sources read.**

* Diehl–Gaunt–Ostermeier–Plößl–Schäfer (DGOPS), JHEP 01 (2016) 076, arXiv:1510.08696, only v1 exists: §4, pp. 38–52, with single DY in §4.3.1 and §4.3.4.
* The CSS review, hep-ph/0409313: §8.4 and §10.
* Aybat–Sterman, PLB 671 (2009) 46, arXiv:0811.0246.
* Zhou–Yan–Zhang–Li, Commun. Theor. Phys. 74 (2022) 115202 (arXiv:1708.01743v2): §§I, III, V and VII were read. The statements below about Sec. VI and eqs. (85)–(86) were checked by both round-3 reviewers.

**Not accessed:** CSS NPB 308 (1988) 833 (publisher only; no scanned preprint is linked on INSPIRE) and Collins 2011, §14.4.

**The graph-by-graph argument (DGOPS §4, single DY).**

1. Each graph is decomposed into region approximants with subtraction terms, and each term is integrated over the full range of loop momenta. So E.19-type soft approximations are applied globally, and the soft–collinear overlaps at the rapidity ends are removed by the subtraction terms of the larger regions.
2. For a given graph and region, all cuts are summed. Written in LCPT, the remainder is independent of how the soft vertices on $A$ are split between amplitude and conjugate (§4.3.4).
3. The final-state factor of $A$, summed over cuts and integrated over $k^-$, equals 0 or 1 (eqs. (4.18)–(4.20)). So the final-state pinches disappear, and $l_j^-$ is deformed into the UHP to $|l_j^-|\sim|l_{jT}|$. This assumes a routing for which DGOPS state: "It would be desirable to have a formal proof that this is always possible".
4. Grammer–Yennie approximations and Ward identities give Wilson lines; for inclusive DY the soft factor is unity. The argument needs an observable that is constant over the cuts of the final-state factor (cf. Gaunt 2014 for $E_T$).

*Difference from App O.* Each forward graph has a fixed colour factor, and the insertions are never localized at equal times in both jets. No ordering weights arise: the Glauber region is avoided by deformation, not cancelled by side sums.

**Aybat–Sterman 2009.** An outline of an all-order argument, with incoming partons and Wilson lines, in a hybrid LCOPT form.

* Spectator attachments of the "eikonal field" cancel by their causal identity (eq. (10)), which holds for fixed colour orderings. It is the sector-sum identity used in L1(c) and L8(c).
* The remaining pole contributions are the origin of divergent phases, which cancel after the sum over final states.
* Like DGOPS, it never localizes two non-commuting insertions in both jets, so the ordering-weight issue of App O does not arise. The paper presents its argument as an outline.

**Zhou–Yan–Zhang–Li.** SCET with explicit Glauber fields, the strict Glauber propagator (their eq. (1)) and the Rothstein–Stewart regulator $|q^+-q^-|^{-\eta}$ (eq. (4)).

* Spectator states are evolved along one time-like direction $n_f^+$ (eqs. (58)–(62)). The localizations $\delta(y^+)$ and $\delta(y'^-)$ at the two ends of each $A_G^+$ line (eq. (64)) are both rewritten as $\delta(n_f^+\cdot y)$ (eqs. (66)–(70)).
* All SS exchanges (the $A^+_G$ sector) are then generated by one unitary operator $U_{+G}(\infty,-\infty)$, which cancels in the cut sum (eqs. (80)–(84)).
* The $A^-_G$ sector, which includes spectator–soft exchanges, is treated afterwards along a **second** time-like direction $n_f^-$ (eqs. (85)–(86)). So the single operator $U_{+G}$ covers the $A^+_G$ sector only.
* In App O's language, the treatment of the SS sector is the **common-ordering** prescription (`lem:appO-joint-localization`; reference Rem. E.56: the RS regulator realizes it). With a common ordering $p_{\rm opp}=0$ and the half-coincident $W_{12}$ is real, so neither coincident residual arises.
* Their caveat that the graphical discussion "should not be viewed as strict proofs" (pp. 22, 29) qualifies their **graphical Section VI**. The operator-level argument is presented as a proof (abstract; Secs. V, VII).
* Our non-acceptance of it as a proof of `asm:appO-collinear-ends` is **our own assessment** of its key step: one evolution parameter for both jets, which is exactly the point at issue in the reference's Lemma E.48(d). Their argument does not compute the ordering weights with exact propagators, and the end regions where T3's unregulated residual is produced are handled only through the zero-bin assignment of eikonalized couplings.
* We therefore read it as an EFT form of the `asm:appO-collinear-ends` matching statement, consistent with T2′(c) and T3(e): in-window regulators remove both uncut coincident residuals in the model.

**Conclusion.**

* No gap is identified in the graph-by-graph argument for the coincident patterns studied here. T3's unregulated residual is not stable under in-window $k^-$ regulators (T3(e)). In the subtraction formalism, the region of large $|k^-|$ belongs to the subtraction term of the region in which the gluon is $B$-collinear; DGOPS step 6 states that failures of the approximations in larger regions are removed by subtraction terms.
* Every statement here that an `asm:appO-mixing`(c)-type assumption is "needed" or "not needed" is relative to App O's two-time framework.
* The graph-by-graph argument has its own stated inputs: the routing assumption of DGOPS step 3, the validity of LCPT (zero modes, instantaneous vertices), and the region/subtraction formalism. App O shares them in other forms (`asm:appO-lcopt`, `asm:appO-mixing`(a′), `asm:appO-deformation`).

---

## 11. TMD version — [C]

**What carries over.**

* The measurement does not see the SS momenta (reference Prop. E.50(b); `prop:appO-tmd`).
* L1–L8 are statements at fixed transverse momenta and hold verbatim.
* $\varepsilon\sim\lambda^2$ with $\lambda=q_T/Q$.

**Not checked** (each is required before any grade above [C]):

* (i) the regulators of `asm:appO-collinear-ends` versus the TMD rapidity regulator and Collins–Soper evolution;
* (ii) the soft-scale windows of `lem:appO-glauber-pc`(e), where the relative error is $O(\lambda)$;
* (iii) the staple direction;
* (iv) the reference's E.9(iii′).

*On (iii).* ${\rm Im}\,p_{\rm opp}$ and the half-coincident ${\rm Im}W_{12}$ are exactly the Coulomb/Glauber phases that distinguish past- from future-pointing staples, and for T-odd TMDs they enter at leading power. Collins, PLB 536 (2002) 43, showed that the Wilson line invalidates the time-reversal argument and reverses the Sivers sign between SIDIS and DY. Collins–Metz, PRL 93 (2004) 252001, gave Wilson-line directions consistent with factorization.

**Related tests.**

* Buffing–Mulders, PRL 112 (2014) 092002, proposed colour entanglement for double-T-odd DY terms.
* Boer–van Daal–Gaunt–Kasemets–Mulders, SciPost Phys. 3 (2017) 040 (read §4, App. A), computed the leading-power double-Boer–Mulders term at $O(\alpha_s^2)$ in a quark–scalar-diquark model with Collins subtractions. The entangled colour structure cancels once the three-gluon-vertex graph, summed over cuts, is combined with two-gluon graphs whose gluons connect a spectator to the other hadron's active parton. This concerns SA/AS patterns and imaginary parts, which this report leaves regulator dependent, so it neither contradicts nor confirms T2 or T3; it supports factorization.

**A dissenting claim.** Chang–Li, PLB 726 (2013) 262, and Li, PRD 106 (2022) 014029 (both read), attribute the Lam–Tung violation in pion-induced DY at $q_T$ of a few GeV to a non-cancelling, non-perturbative Glauber phase in $k_T$ factorization.

* The phase is a single constant $S\simeq0.8$, fixed from NA10 and reused for E615 and COMPASS.
* It is argued to be large for the pion because the pion is a Nambu–Goldstone boson.

*Assessment.*

1. The framework is $k_T$ factorization with off-shell partons, not the CSS collinear/TMD factorization analysed here.
2. The non-cancellation is asserted by reference to Collins (arXiv:0708.4410) and Collins–Qiu (PRD 75 (2007) 114014). Those papers concern processes with observed hadrons in the final state, and Collins–Qiu state explicitly that the situation differs from DY.
3. The explicit $O(\alpha_s^2)$ spectator-model check of the T-odd term (Boer et al. 2017) found standard factorization.
4. The phase is fitted, not derived.

The claim is recorded as an unconfirmed phenomenological proposal, in tension with [A]-level factorization for inclusive DY. The statements of this report are perturbative and model-level, so they cannot exclude a non-perturbative pion-specific effect of this kind (OPEN-7).

---

## 12. Errata item ERR-S1b (proposed App Q entry; addendum to ERR-S1)

**Location in the reference** (`factorization_qcd-2.pdf`, App E). Quotations from `refdoc/refdoc.txt`, lines 11801–11816, 11862 and 13014; the superscripts are restored.

* (i) Rem E.32, last sentences: 「剩余项 ∝ $C_AX$ 的色结构与 Glauber 胶子经三胶子顶点发射软胶子的图相同（例 E.38(4)），所以 QCD 的幺正性只能在包括这些图与相应的实发射的完整图集中保证相消：在 $\mathcal G_0$ 之内，$O(\chi^2)$ 的剩余项不应期望为零。」
* (ii) The status paragraph of Assumption E.33: 「(c)…对非阿贝尔理论中的重合连接方式，它不是 Glauber 窗口内的定域表达式的性质（引理 E.48(d)），而且在 $\mathcal G_0$ 之内不应期望成立（注 E.32）——所以即使对 $\mathcal G_0$，它也是关于包含 $\mathcal G_0$ 之外的图的完整图集 $\mathfrak G$ 的假设。」
* (iii) Rem E.49(2), last sentence: 「这与注 E.32 的结论一致：在 $\mathcal G_0$ 之内，$O(\chi^2)$ 的剩余不应期望为零。」

**What the reference already gets right.**

* Rem E.32 states that with exact propagators the orderings in the two jets are correlated; that the correlation comes from the near-mass-shell points $|k^+k^-|\sim\mathbf k_T^2$ of the connecting lines; and that the strict window loses it.
* Rem E.49(2) attributes the missing $-\frac14C_A\chi^2X$ to two sources of the same colour structure: the principal-value part near $2k^+k^-=\mathbf k_T^2$, *and* the three-gluon-vertex real and virtual graphs.

So the reference identified the near-shell mechanism.

**Correction.**

1. *Location of the error.* The error lies in the **expectation** that this mechanism is insufficient within $\mathcal G_0$, for the uncut direct lines, and that the three-gluon-vertex graphs are needed. The only reason the reference gives is that the colour structures coincide (Ex. E.38(4)), and a coincidence of colour structures is not an argument for non-cancellation.
2. *Eikonal lines.* For two straight eikonal lines, box and crossed box alone give $\mathcal V^\dagger\mathcal V=1+O(\chi^3)$ (ERR-S1; $p_{\rm opp}=-iY/\pi$; `prop:dy-eikonal-twogluon`).
3. *Composite spectators.* In $\mathbb M_{\rm glob}$, pointwise on $\mathcal N_A\cap\mathcal N_B$, at $O(g^4)$, the side sum of the **uncut** direct lines of the fully coincident SS pattern cancels once the window is combined with the near-shell region of the same uncut lines (T2; [R, R_PT] in the model, [R, R_cond] for QCD jets with content [P]). The near-shell part of the uncut direct lines therefore supplies the whole $-\frac14C_A\chi^2X$ for this pattern. With in-window two-sided regulators that retain the near-shell segment ($K^+K^-\gg\mathbf k_T^2$), the model has ${\rm Re}\,p_{\rm opp}\to0$ for the uncut lines (T2′(c), [P]).
4. *Consistency.* Two-particle unitarity of box plus crossed box for on-shell lines (P3) agrees.
5. *Consequence.* If E.33(c2) holds for the complete set, the remaining contributions must together have zero net Hermitian $C_AX$ part at leading power. These are the **cut** direct lines (real emission, which also belongs to $\mathcal G_0$) and the three-gluon-vertex graphs. Neither group is computed here (OPEN-13; slot X1e).

**What stays.**

* E.33(c2), i.e. `asm:appO-mixing`(c), remains an assumption about the complete set. It is still needed for the $O(g^6)$ ladder class (P5, [A]) and for coincident SA/AS insertions and H-emission endpoints (Remark P6).
* Whether the full $\mathcal G_0$ sum at $O(g^4)$, including the cut direct lines, cancels is **open** (OPEN-13). The reference's conclusion "within $\mathcal G_0$ the residual should not be expected to vanish" is therefore contradicted for the uncut-line part. For the complete $\mathcal G_0$ it is neither established nor refuted.
* The strict window-localized expression does not cancel (`lem:appO-joint-localization`(c)); P2 quantifies its regulator dependence.
* Under `asm:appO-collinear-ends`, the content of E.33(c2) for the coincident $O(g^4)$ patterns is relocated to the matching at the collinear ends.
* This is not a refutation of App E.

**Status.** [R, R_cond] (T2: uncut lines, model scope) + [P] (T2′(c)).

---

## 13. Register consequences

All "needed / not needed" statements below are relative to App O's two-time framework (§10).

| register entry | effect of this report |
|---|---|
| `asm:appO-lcopt` | unchanged; it is the premise of (SEC) and of P1 and T1 |
| `asm:appO-envelope` | rewording proposed: for coincident connections, impose on side-summed families (§2.3). The per-graph version is incompatible with P4 within the class; open for graph-generated jets (OPEN-10) |
| `asm:appO-mixing`(a) | reformulation (a′) proposed (L7, §2.3) |
| `asm:appO-mixing`(b) | unchanged |
| `asm:appO-mixing`(c) | see the list below |
| deleted clause (c1) | superseded by L1 together with `asm:appO-envelope` on side-summed families |
| `asm:appO-deformation` | (c) also receives the out-of-window parts of P1's windows and the wee-line endpoint region of P1(c); for (d) see Remark P6 |
| `asm:appO-rewritten-cs` | unchanged |
| new, proposed | `asm:appO-adjacent-swap` [\tagP], `asm:appO-real-jets` [\tagP], `asm:appO-collinear-ends` [\tagA] (§2.2) |

**`asm:appO-mixing`(c), pattern by pattern.**

* **Commuting patterns:** not needed (T1, unconditionally; this is `prop:appO-ss-cancel`(iii)).
* **Fully coincident SS–SS pairs at $O(g^4)$, uncut lines:** not needed, given `asm:appO-collinear-ends` with $K^+K^-\gg\mathbf k_T^2$, pointwise on $\mathcal N_B$ (T2′(a),(c)). The NF-free symmetric version is OPEN-2.
* **Half-coincident SS pairs at $O(g^4)$, uncut lines:** not needed, given `asm:appO-collinear-ends` at the $k^-$ end (T3(e), proved with the $k^-$ regulator alone; adding the class-$\mathfrak X$ $k^+$ factor is expected to cost $O(a/(K^+K^-))$, not proved).
* **Cut direct lines** (real emission) of both coincident patterns at $O(g^4)$: open (Remark C, OPEN-13). In the unregulated model they are not expected to be suppressed. Under the two-sided regulators, power counting suggests suppression; this is to be proved.
* **The fully coincident two-line ladder class from $O(g^6)$ on:** needed, argued [A] (P5). It is expected, not shown, for the other coincident patterns from $O(g^6)$ on.
* **Coincident SA/AS insertions and H-emission endpoints:** needed (Remark P6).

**Proposed status sentence for `asm:appO-mixing`.** "(c) holds for two-gluon exchange between eikonal lines at $O(g^4)$ (`prop:dy-eikonal-twogluon`). For composite spectators in the global two-time model, the uncut-line part of the fully coincident $O(g^4)$ family cancels pointwise on NF (`prop:appO-twoexch-spectator`, model theorem). Cut direct lines, the half-coincident pattern at the collinear ends, $O(g^6)$ and coincident SA/AS insertions are open."

**Overall.** `thm:dy-factorization` stays [A]. The report upgrades sub-steps only within App O's framework. Its TMD versions are [C].

---

## 14. Examples and verification

### 14.1 The scalar spectator model

Each hadron splits at a point vertex into an active parton and a spectator $s$, in light-front kinematics with $P^+=1$.

* *Jet $A$.* The colour-ordered covariant jet functions are
$$J_A^{[12]}=\frac{i^3}{(k_1^-+k_2^--\beta+i0)(\alpha_0-k_1^--k_2^-+i0)(\alpha_1-k_2^-+i0)},$$
and $J_A^{[21]}$ has $(\alpha_2-k_1^-+i0)$ in the last factor. The parameters are
  * $\beta=E_a+E_s-P^-$;
  * $\alpha_0=E_s-E(s-k_1-k_2)$, $\alpha_1=E_s-E(s-k_2)$, $\alpha_2=E_s-E(s-k_1)$;
  * $d_0=P^--E_a-E(s-k_1-k_2)$, $d_{10}=P^--E_a-E(s-k_2)$, $d_{20}=P^--E_a-E(s-k_1)$;
  * $\mathcal J_A=i/d_0$.
* *Sector form.* The covariant $J_A^{[12]}$ equals the sum of its three LCOPT sector terms, each a single term with single-state gaps and coefficient $c=i/d_0$ (sympy; round-2 `chkD_endpole.py`, round-3 reviewer 1). Hence (SEC), (EQ), (ADJ) and (REAL) hold exactly, and $m_X=m^\flat_X=1$.
* *Jet $B$* is analogous, with energies $p=-k^+$. For the half-coincident test,
$$J_B=\frac{i^3}{(p_1+p_2-\beta+i0)(\alpha^{(1)}-p_1+i0)(\alpha^{(2)}-p_2+i0)}.$$
* *Parameter sets* (in `scripts/twoexch_rotated_fast.py`):
  * base: both jets on $\mathcal N$;
  * apole: $A$ has $\alpha_1>0$ (and $\alpha_0>0$);
  * alt: $B$ has $\alpha_2>0$;
  * altswap/baseswap: $A$ and $B$ exchanged.

### 14.2 Methods

* **(I) Real contour** (`scripts/twoexch_exact.py`): exact $k^-$ residues, an exact log-residue inner integral, and principal value plus $i\pi$ for real poles of the outer integrand. *Known defect:* it mishandles a pinch in the outer variable when $J_A$ has $\alpha_1$-type poles, so its apole and "both" values are invalid. Method (II) supersedes them, and (I) must not be used for these sets.
* **(II) Rotated contour with strip adaptation** (`scripts/twoexch_rotated_fast2.py`; valid on $\mathcal N_B$).
* **(III) Brute force at finite $\eta$** (`scripts/twoexch_bruteforce.py`): qualitative only. $W(12,12)=0.136,\ 0.118,\ 0.110,\ 0.107$ at $\eta=0.2,0.1,0.05,0.025$, trending to the value 0.1044 of (I)/(II).
* At $\lambda=1$, (I) and (II) agree to 7 digits; at $\lambda=0.01$, to 6–10 digits. Independent third implementation (round 1): $0.3740971311-0.2694186095i$ against $0.374097135-0.269418606i$.

### 14.3 Main numbers

${\rm Re}\,p_{\rm opp}$ at $\lambda=0.01,\ 0.003,\ 0.001$:

| set / method | $\lambda=0.01$ | $\lambda=0.003$ | $\lambda=0.001$ | prediction |
|---|---|---|---|---|
| base (I = II) | 0.0123 | 0.0021 | 0.00035 | → 0 (T2) |
| apole (II) | 0.263 | 0.254 | 0.2520 | 0.2517 (T2′(b)) |
| alt (I) | 0.069 | 0.052 | 0.0490 | 0.0483 (mirror T2′(b)) |
| class $\mathfrak X$, $K_c=\lambda$: base | 0.103 | 0.054 | 0.028 | → 0 as $\lambda^{1/2}$ (T2′(a)) |
| class $\mathfrak X$, $K_c=\lambda$: apole | 0.103 | 0.054 | 0.028 | → 0 |
| class $\mathfrak X$, $K_c=\lambda$: altswap | — | 0.035 | 0.017 | → 0 |

* The slope of ${\rm Im}\,p_{\rm opp}$ tends to $-2/\pi$ per unit $\ln(1/\lambda)$ unregulated, and to $-1/\pi$ regulated.
* $N/N_0\to1$ ($0.9998$ at $\lambda=0.003$).
* The half-coincident, colour, two-sided-regulator and P4 numbers are given under T3, L4, T2′(c) and P4.

### 14.4 Log account (honest history)

1. `logs/checks_C2_C3_C4.log` originally ended with "SOME CHECK FAILED". Checks C3e/C3f tested the author's **original, wrong** prediction "Re $W_{12}\to\frac12$, hence cancellation"; they were not "deliberately mis-specified", as an early version stated. The checks now test the correct L4(b) formula, and the re-run gives ALL PASS. The original is kept as `checks_C2_C3_C4_r0.py` / `_r0.log`.
2. `scripts/check_halfcoinc_singlets.py` crashed (LAPACK error on a 4096×4096 Casimir) before the (8,8,8,8) and ($\bar3$,8,8,3) cases. The fixed version `check_halfcoinc_singlets_v2.py` gives ALL PASS for all ten label sets.
3. Stale labels in script headers ("Thm T4", "Thm T5") are annotated and mapped to T2′ and T3.
4. `logs/twoexch_rotated_0.01.log` and `_0.1.log` are empty: they come from aborted runs of a slow superseded code. `logs/twoexch_rotated_fast_0.01.log` documents the failure of a naive polar grid ($p_{\rm opp}=0.174$ instead of 0.0123).
5. `fix_r2_scripts/t3e_sensitivity.py`, item (iv), only **reprinted** the round-1 values of ${\rm Im}W_{12}(K)$, and its "ALL PASS" tested only $c_v<1$, $c_{\rm inf}<1$ and the leading-term error. These values are now **recomputed** in `final_scripts/t3f_recompute.py`, with agreement to all printed digits.

### 14.5 Scripts and logs

All paths are relative to `verify/extend/X1-glauber/`.

**Original run** (`scripts/`, `logs/`):

* two-exchange model: `twoexch_model.py`, `twoexch_exact.py`, `twoexch_rotated_fast(2).py`, `twoexch_regulated.py`, `twoexch_bruteforce.py`, `test_twoexch_parts2.py`;
* half-coincident: `halfcoinc.py`, `halfcoinc_real.py`, `halfcoinc_sym.py`;
* checks: `checks_misc.py`, `checks_C2_C3_C4.py`, `check_halfcoinc_colour.py`, `check_halfcoinc_singlets_v2.py`.

**Fix round 1** (`fix_r1_scripts/` → `fix_r1_logs/`): `regulator_indep.py` (regulator studies A, B), `colour_dy_check.py`, `p4_perturbation.py`.

**Fix round 2** (`fix_r2_scripts/` → `fix_r2_logs/`): `l1_bound_quadrant.py`, `p2_window_shape.py`, `l8_bounds.py`, `p4_regulated_B.py`, `t3e_sensitivity.py`.

**Final round** (`final_scripts/` → `final_logs/`), all ALL PASS:

* `p2_orientation.py`: exact sector-sum weights by iterated residues; orientation of $\delta_B$.
* `p5_interference.py`: interference structure, Feynman-gauge sign and gauge dependence of $D_{\mathsf C}$.
* `t3f_recompute.py`: recomputation of T3(e′),(f), and boost invariance of the T3(e) terms.
* `t2_constants.py`: (A3) and the decay bound of $\varrho$ on 400 random multi-state jets; the $O(1)$ remainder of ${\rm Im}\,p_{\rm opp}$ for four jet pairs.

**Reviewer checks.**

* Round 1: `review_r1_1_scripts/`, `review_r1_2_scripts/` with `review_r1_2_logs/`.
* Round 2: `review_r2_1_scripts/` with `review_r2_1_logs/`; `review_r2_2_scripts/` (chkA–chkE).
* Round 3: `review_r3_1_scripts/` with `review_r3_1_logs/` (general non-factorized jets for L8 and T2; the P4 partner; T3(e) constants; P2); `review_r3_2_scripts/` (L8, P5 cut structure, T3(e) constants, P2, INSPIRE searches).

The integral form of every result still needs `asm:appO-envelope` on side-summed families.

---

## 15. Novelty ledger

"New" means new to our knowledge after the literature checks described below. No novelty marker is to be printed in the monograph before OPEN-8 is closed (WRITER_SPEC_v2 §6.5).

| result | new / known | prior work and references |
|---|---|---|
| L1 | partly known | Known: the race formula (reference App E.4.4; `lem:appO-joint-localization`(a)) and $\sum w=1$ (the eikonal identity; Aybat–Sterman 2009, eq. (10)). New: half-plane sector rule, exactness at finite $\eta$, the bound with $\sum\lvert w_\sigma\rvert$, the closed-quadrant lemma, part (d) |
| L1′ | new (elementary) | — |
| L2 | new | corrects the wording of REFDOC ERR-S3 |
| L3 | new (explicit instance) | — |
| L4 | (a) known; (b)–(d) new as statements | (a): reference Ex. E.38 / `lem:appO-glauber-operator`. Colour-singlet-target mechanism: Lindsay–Ross–Sachrajda 1983. Context: Catani–de Florian–Rodrigo 2012; Forshaw–Seymour–Siodmok 2012; Barcaro–Gao–Gaunt–Pathak 2026 |
| L5 | new | — |
| L6 | elementary; its role new | — |
| L7 | elementary; new as a pre-integration replacement of `asm:appO-mixing`(a) | — |
| L8 | new (elementary) | — |
| T1 | known; only the uniform route is new | `prop:appO-ss-cancel`(iii); reference Props E.35, E.31(iii) |
| P1 | new | idea suggested without proof in the reference work notes (R7) |
| T2 | physical cancellation known in models; general derivation new | Lindsay 1984; Brandt–Frenkel–Taylor 1989; reggeization reading: Lipatov 1976, Kuraev–Lipatov–Fadin 1977, Rothstein–Stewart 2016. New: general-LCOPT derivation with explicit estimates, ray-identity mechanism, regulator analysis; extends ERR-S1 |
| T2′ | new | end-pole formula; regulated proof with rate; two-sided regulator study (model statements) |
| P2 | (a) known; (b), (c) new (elementary) | (a): reference Lemma E.48(d); `lem:appO-joint-localization`(c) |
| P3 | known in substance | Cutkosky 1960; Veltman 1963; 't Hooft–Veltman; ERR-S1 / `prop:dy-eikonal-twogluon` |
| T3 | new | the configuration does not occur in Lindsay 1984, Brandt–Frenkel–Taylor 1989 or Lindsay–Ross–Sachrajda |
| P4 | new | sharpens ERR-S3 |
| P5 | formulation new; substance standard | BFKL; Lipatov 1976; Kuraev–Lipatov–Fadin 1977; Del Duca 1995; Schwartz–Yan–Zhu 2018; Rothstein–Stewart 2016 |
| Remark P6 | refinement | `asm:appO-deformation`(d), `rem:appO-h-emission` |
| Remark C | new observation (power counting only) | — |
| ERR-S1b | new erratum item | addendum to ERR-S1 |

**Literature checks.**

* Bibliographic data for every entry of §19 were verified on INSPIRE by reviewers in rounds 1–3 (`review_r3_2_scripts/logs/r3_inspire_refs.log`). Barcaro et al. was verified in this round (INSPIRE record for arXiv:2607.14259: DESY-26-091, SLAC-PUB-260713).
* Novelty searches by reviewers in rounds 1–3 found no prior statement of T2 for general LCOPT jets, of T3's configuration, of P1, P2(b), P4 or L8 (`review_r3_2_scripts/logs/r3_inspire_novelty*.log`, `r3_inspire_citers.log`). They covered title searches (Glauber with spectator, Glauber with Drell–Yan, spectator interactions, cancellation, factorization) and the Glauber/spectator citers of DGOPS, Aybat–Sterman and Rothstein–Stewart.
* Not accessed: CSS NPB 308 (1988) 833 and Collins 2011 §14.4 (OPEN-8).

---

## 16. Withdrawn-claims ledger

**Withdrawn in round 1** (claims of the original report):

1. T3 graded [V] ("$\mathcal G_0$ does not suffice for half-coincident patterns").
2. "An E.33(c2)-type compensation is genuinely needed already at $O(g^4)$", and "any compensation must carry the three-gluon colour structure".
3. The Glauber–soft "Y-graph" candidate statement.
4. "The half-coincident residual does not vanish once a fourth spectator is present", together with the basis-dependent values 0.38/0.71 presented as DY statements.
5. Register item G5(i) (half-coincident patterns from $O(g^4)$).
6. T2 "refutes the reference"; "E.33(c2) is not needed for this pattern at $O(g^4)$"; "holds unchanged for TMD".
7. T2′: "mechanism: a universal $-\frac14$ from each analytic rapidity end".
8. P2: the "sharp, non-analytic truncation" diagnosis and its novelty claim.
9. T1 presented as a new result; "valid unchanged for TMD".
10. Remark P6 graded [R].
11. L1: "replaces E.33(c1)" as a per-graph statement; the dimensionally inhomogeneous constant $M_\sigma=\sum|c_t|$; the stray factor $i^N$ in $\mathcal J_\sigma$.
12. L5: the range "$t\in(0,\pi]$".
13. P1: a side-dependent $x_{\min}$; the missing multiplicity $n_A$; the cut-dependent wording "each spectator line counted once on each side".
14. L7: "E.33(a) holds on the far-off-shell set". It is now a pre-integration lemma plus the assumption (a′).
15. P4: the base/apole "same window data" illustration.
16. EX: "all checks pass" and "deliberately mis-specified" (§14.4).
17. "And its TMD version" for all results; TMD is now [C].

**Withdrawn in round 2:**

18. L1(b), L1′(b), L7(b): the error bounds without the factor $\sum_\sigma|w_\sigma|$, which are false for general complex poles (counterexample in §3).
19. P2: "smooth two-sided cut-offs that exclude the near-shell region give the same $\frac12$" as a general statement, and "$\to\frac12$ otherwise".
20. T3(e): the "location" statement graded [R_cond], which depends on the representation.
21. L4(d3)/T3(g): "vanishes in the commonest DY colour configurations".
22. P4: the consequence for all LCOPT jets; "generically non-zero" (now "non-zero whenever $\tilde c_2\ne0$").
23. G5(ii): "needed for every non-abelian coincident pattern from $O(g^6)$".
24. T2′(b): "artefacts of the model" for all spectators; it now distinguishes massive from massless spectators.
25. The DGOPS citation as "v2" (only v1 exists).
26. Lindsay–Ross–Sachrajda as prior art for the fully coincident SS cancellation.
27. The T2 rate $O(\varepsilon^{1/2}L^2)$, which was asserted without proof.

**Withdrawn or corrected in this final revision (round 3):**

28. "T2 shows that the $\mathcal G_0$-restricted form of E.33(c2) holds". It is now restricted to the side sum of uncut direct lines; cut lines are OPEN-13.
29. ERR-S1b(ii) in unrestricted form. It is restricted to uncut lines and reframed: the reference identified the near-shell mechanism; its error is the expectation of insufficiency.
30. P4(b): "the perturbation leaves (Sp′) unchanged (no single-state gap)". This is false: it breaks (ADJ) for $J_A$, which is harmless since the class imposes (ADJ) on $J_B$ only.
31. P5: the identity $D_{\mathsf C}=\int d\Phi_3|A^{\rm lines}|^2$ and the reason "a sum of $B^\dagger B$ terms". Replaced by the interference form, with Feynman-gauge positivity and gauge dependence.
32. T2: "${\rm Im}\,p_{\rm opp}=-\frac1\pi\ln\frac1\varepsilon+c+O(\varepsilon^{1/2}\dots)$" with a convergence rate. Weakened to $+O(1)$, with an explicit bound $C_I$.
33. T2: "$C_T$ is a polynomial in $m_A,m^\flat_A,m^\flat_B,c_\rho,a_{\max}/a_{\min}$". It also depends on $\ell_A$, $\ell_B$. The hidden condition $\delta_Y\le\frac12$ is now hypothesis (v).
34. T3(e): the term $(\lambda_A/K)(1+\ln(1+K/\mu_B))^2$, which is not boost invariant; corrected to $\ln(1+a_{\min}/(K\mu_B))$. Also the sentence "not determined by the integrand on any window $|k^-|\le K$".
35. T2′(b): "jet $B$'s poles give the same by symmetry". Replaced by the mirror statement valid on $\mathcal N_A$.
36. REG: "(Sp′), (R), NF, (H_glob) are local hypotheses and are not registered", a misreading of rule 00.1-1. They are now recast or proposed for registration (§2). Also "G5(ii) … (shown, P5)", now "argued [A]".
37. CMP: "all SS and spectator-soft exchanges are generated by one unitary operator $U_{+G}$" (Zhou et al.). This holds for the $A^+_G$ sector only. Also the reading of their "not strict proofs" caveat as qualifying the whole argument; it qualifies Sec. VI only.
38. L8(c): the intermediate constant 2, corrected to $16/9+1$.
39. P2: the unfixed orientation of $\delta_B$.
40. P1: "$x_{\min}\ge c$" with $x_{\min}$ a momentum. $x_{\min}$ is now a fraction.
41. L4 context: "$\Delta^{(2)}$ vanishes for $n=4$". The operator does not vanish; its contribution to the squared amplitude does.
42. EX: `t3e_sensitivity.py` item (iv) presented as a check. The values are now recomputed.
43. L5 listed among the users of (Sp′). L5 needs only (SEC) and $\mathcal N_B$; this weakens its hypotheses.

---

## 17. Open problems

* **OPEN-1** (main). Prove `asm:appO-collinear-ends` at the $k^-$ end for the half-coincident family: the $B$-collinear-end contribution ($|k^-|\gtrsim K^-$) must be reproduced by the collinear factorization of $J_B$ (Wilson lines, subtraction terms as in DGOPS §4) without the leftover $2ic_1c_2{\rm Im}W_{12}[X_1,X_2]$.
  * Equivalently, compute the family with exact $B$ kinematics at $|k^-|\sim Q$.
  * Include the coincident SA patterns and colour conservation on $B$ (the LRS mechanism), and the collinear-end cut contributions (OPEN-13).
  * Decide whether the remnant-integrated residual $\int d\Phi\,{\rm Im}W_{12}(\Phi)\langle\psi(\Phi)|i[X_1,X_2]|\psi(\Phi)\rangle$ vanishes for generic multi-parton remnants with complex colour amplitudes (L4(d3)). A test needs a hadron model in which the hadron of $j_1,j_2$ has a further remnant parton and complex colour phases.
* **OPEN-2.** A symmetric T2, with analytic regulators at both rapidity ends and no NF hypothesis on either jet.
  * Needed for any statement about the spectator-integrated cross section.
  * Also open: a proof that ${\rm Re}\,p_{\rm opp}\to0$ survives any real-analytic $k^-$ form factor (observed numerically).
* **OPEN-3** (all orders; conjectures).
  * C1: the leading-log tower of the fully coincident pattern is anti-Hermitian to every order (gluon reggeization; cf. Rothstein–Stewart 2016).
  * C2: from $O(g^6)$ on, unitarity of the window is restored only after soft real emission and the Lipatov vertex are added (P5; Schwartz–Yan–Zhu 2018). For ordering Glauber loops against soft emissions see Forshaw–Holguin–Pathak 2021 and Pathak 2022.
* **OPEN-4.** Coincident SA/AS insertions and H-emission endpoints (`asm:appO-deformation`(d); Remark P6). Treat the non-analytic weights of L2 together with the Wilson-line deformation, or derive the past-pointing Wilson line without a deformation; replace Remark P6 by a theorem.
* **OPEN-5.** The remaining analytic inputs:
  * `asm:appO-envelope` for side-summed families;
  * `asm:appO-lcopt` (zero modes, instantaneous loops);
  * `asm:appO-deformation`(b),(c), including the out-of-window parts of P1's windows and the wee-line endpoint region of P1(c);
  * the envelope bounds of `asm:appO-mixing`(a′), including the factor $\sum_\sigma|w_\sigma(p)|$.
* **OPEN-6.** `asm:appO-collinear-ends` at both collinear ends: no leftover Hermitian $C_AX$ (fully coincident) and no $[X_1,X_2]$ (half-coincident), shown with exact kinematics at the ends or within DGOPS's subtraction formalism. The matching must also absorb the collinear-end cut contributions of the direct SS lines (OPEN-13). The SCET argument of Zhou et al. is an EFT form of this statement, not a proof (§10).
* **OPEN-7.** TMD transcription (graded [C]):
  * (i) the regulators versus the TMD rapidity regulator and Collins–Soper evolution;
  * (ii) the soft-scale windows;
  * (iii) the staple direction and the imaginary parts (Collins 2002; Collins–Metz 2004; Boer et al. 2017);
  * (iv) the reference's E.9(iii′);
  * (v) a decisive assessment of the Chang–Li/Li claim.
* **OPEN-8** (literature). Read CSS NPB 308 (1988) 833 and Collins 2011 §14.4 for any explicit treatment of non-commuting coincident exchanges or of the half-coincident colour structure, before novelty markers are printed. A new attempt in this round found no freely accessible scan.
* **OPEN-9.** Three-on-shell-line unitarity at $O(g^4)$ for the colour structure $f\,T_iT_{j_1}T_{j_2}$, including the Y graph, the half-coincident ladders and the $(i$–$j_e,\ j_1$–$j_2)$ graphs (P3, Remark).
* **OPEN-10.**
  * (i) An explicit pair of graph-generated scalar-model jets with identical $D_{\rm win}$ but different per-graph $W(12,21)$.
  * (ii) A proof or disproof of the observed sector selection: perturbations of $J_B$ confined to the all-initial (or all-final) sector leave the per-graph weights unchanged (shift $\le10^{-5}$).
* **OPEN-11.** The regulator-shape dependence of the residual once the near-shell region is excluded, with exact propagators across the crossover $K^+K^-\sim\mathbf k_T^2$, for non-even line-dependent regulators. Also: which regulator class the matching of `asm:appO-collinear-ends` must use.
* **OPEN-12.**
  * Prove (ADJ) and (REAL) for spin-summed leading-power LCOPT jets, which would discharge `asm:appO-adjacent-swap` and `asm:appO-real-jets`.
  * Alternatively, remove (ADJ) from L8 by treating the axis bands with a kink estimate against the continuous weights (L2).
  * Sharpen the constants of L8 (numerically about 6 and 0.4, against the proven 400 and 16) and the power of the logarithm in T2.
* **OPEN-13** (new). The cut (real-emission) contributions of the direct SS lines for the fully and half-coincident patterns at $O(g^4)$ (Remark C).
  * Compute them, or prove them power suppressed under the two-sided regulators; power counting suggests $O(\lambda_BK^-/a+\lambda_AK^+/a)$.
  * In the unregulated model, determine their net Hermitian $C_AX$ and $[X_1,X_2]$ parts.
  * Together with the three-gluon-vertex graphs (slot X1e), this decides the full $\mathcal G_0$ form of ERR-S1b.

---

## 18. Results table

| id | grade | status | new / known |
|---|---|---|---|
| D1–D8 | definitions | — | — |
| L1 | [R, R_PT] | proven | partly new |
| L1′ | [R, R_PT] | proven | new |
| L2 | [R, R_PT] | proven | new |
| L3 | [R, R_PT] | proven | new |
| L4 | [R, R_def] | proven | (a) known; (b)–(d) new |
| L5 | [R, R_PT] | proven | new |
| L6 | [R, R_PT] | proven | elementary |
| L7 | (a),(b) [R, R_PT]; (c) → assumption (a′) | proven; reformulated | new (elementary) |
| L8 | [R, R_PT] | proven | new |
| T1 | [R, R_cond: `asm:appO-lcopt`] | proven | known (re-derivation) |
| P1 | [R, R_cond: `asm:appO-lcopt`] | proven | new |
| T2(a) | [R, R_PT] (model) | proven | new |
| T2(b) | [R, R_cond: `asm:appO-lcopt`, `asm:appO-adjacent-swap`†, `asm:appO-real-jets`†], content [P] | proven (conditional) | new |
| T2 physical reading | [P] | conditional on `asm:appO-collinear-ends` and OPEN-13 | known in models |
| T2′(a), (b) | [R, R_PT] (model) | proven | new |
| T2′(c) | [P] | numerics | new |
| P2(a) | [R, R_PT] | proven | known |
| P2(b), (c) | [R, R_PT] | proven | new |
| P3 | [R, R_PT] at $O(g^4)$ | proven | known in substance |
| T3(a), (g) | [R, R_def] | proven | new |
| T3(b), (c), (e), (e′)-algebra | [R, R_PT] | proven | new |
| T3(d), (f), (e′)-numerics | [P] | numerics | new |
| P4(a), (b) | [R, R_PT] within the class | proven | new |
| P4(c) | [P] | numerics | new |
| P5 | [A] | argued | formulation new |
| Remark P6 | ungraded | argument | refinement |
| Remark C | ungraded | open (OPEN-13) | new observation |
| ERR-S1b | [R, R_cond] + [P] | proposed, restricted | new |
| TMD | [C] | open | — |
| Inclusive DY collinear factorization | [A] | unchanged | — |

(† = proposed register entry.)

---

## 19. References

**Original claim.**
* G.T. Bodwin, S.J. Brodsky, G.P. Lepage, PRL 47 (1981) 1799.

**Non-abelian Bloch–Nordsieck violation.**
* R. Doria, J. Frenkel, J.C. Taylor, NPB 168 (1980) 93.
* C. Di'Lieto, S. Gendron, I.G. Halliday, C.T. Sachrajda, NPB 183 (1981) 223.
* A. Andrasi, M. Day, R. Doria, J. Frenkel, J.C. Taylor, NPB 182 (1981) 104.

**Two-loop spectator calculations.**
* W.W. Lindsay, D.A. Ross, C.T. Sachrajda, PLB 117 (1982) 105; NPB 214 (1983) 61; NPB 222 (1983) 189.
* P.V. Landshoff, W.J. Stirling, Z. Phys. C 14 (1982) 251.
* C.A. Nelson, NPB 223 (1983) 366.
* W.W. Lindsay, NPB 231 (1984) 397.
* F.T. Brandt, Z. Phys. C 45 (1989) 287.
* F.T. Brandt, J. Frenkel, J.C. Taylor, NPB 312 (1989) 589.

**All-order arguments.**
* G.T. Bodwin, PRD 31 (1985) 2616; Erratum PRD 34 (1986) 3932.
* J.C. Collins, D.E. Soper, G. Sterman, NPB 261 (1985) 104; NPB 308 (1988) 833; Adv. Ser. Direct. High Energy Phys. 5 (1989) 1 [hep-ph/0409313].
* J.C. Collins, *Foundations of Perturbative QCD* (CUP, 2011).
* M.G. Aybat, G. Sterman, PLB 671 (2009) 46 [arXiv:0811.0246].
* M. Diehl, J.R. Gaunt, D. Ostermeier, P. Plößl, A. Schäfer, JHEP 01 (2016) 076 [arXiv:1510.08696].
* F. Liu, J.P. Ma, arXiv:0802.2973.
* G.-L. Zhou, Z.-X. Yan, X. Zhang, F. Li, Commun. Theor. Phys. 74 (2022) 115202 [arXiv:1708.01743].

**Glauber exchange, reggeization, Coulomb phases.**
* L.N. Lipatov, Sov. J. Nucl. Phys. 23 (1976) 338.
* E.A. Kuraev, L.N. Lipatov, V.S. Fadin, Sov. Phys. JETP 45 (1977) 199.
* V. Del Duca, hep-ph/9503226.
* J.R. Gaunt, JHEP 07 (2014) 110 [arXiv:1405.2080].
* R. Ángeles-Martínez, J.R. Forshaw, M.H. Seymour, JHEP 12 (2015) 091 [arXiv:1510.07998].
* I.Z. Rothstein, I.W. Stewart, JHEP 08 (2016) 025 [arXiv:1601.04695].
* M.D. Schwartz, K. Yan, H.X. Zhu, PRD 97 (2018) 096017 [arXiv:1801.01138].
* J.R. Forshaw, A. Kyrieleis, M.H. Seymour, JHEP 08 (2006) 059 [hep-ph/0604094].
* J.R. Forshaw, M.H. Seymour, A. Siodmok, JHEP 11 (2012) 066 [arXiv:1206.6363].
* S. Catani, D. de Florian, G. Rodrigo, JHEP 07 (2012) 026 [arXiv:1112.4405].
* T. Becher, P. Hager, S. Jaskiewicz, M. Neubert, D. Schwienbacher, PRL 134 (2025) 061901 [arXiv:2408.10308].
* J.R. Forshaw, J. Holguin, A. Pathak, PRD 104 (2021) L091501 [arXiv:2108.13439].
* A. Pathak, JHEP 06 (2022) 118 [arXiv:2108.13440].
* S. Nabeebaccus, J. Schoenleber, L. Szymanowski, S. Wallon, PRD 111 (2025) L091502 [arXiv:2409.16067]: a contrast, with a trapped Glauber pinch in an exclusive process.
* D. Barcaro, A. Gao, J.R. Gaunt, A. Pathak, arXiv:2607.14259 (2026).
* G. Sterman, O. Erdoğan, EPJ ST 235 (2026) 1493 [arXiv:2502.14230].

**TMD and colour entanglement.**
* J.C. Collins, PLB 536 (2002) 43 [hep-ph/0204004].
* J.C. Collins, A. Metz, PRL 93 (2004) 252001 [hep-ph/0408249].
* M.G.A. Buffing, P.J. Mulders, PRL 112 (2014) 092002 [arXiv:1309.4681].
* D. Boer, T. van Daal, J.R. Gaunt, T. Kasemets, P.J. Mulders, SciPost Phys. 3 (2017) 040 [arXiv:1709.04935].
* C.-P. Chang, H.-n. Li, PLB 726 (2013) 262 [arXiv:1305.4694].
* H.-n. Li, PRD 106 (2022) 014029 [arXiv:2201.10901].
* J.C. Collins, J.-W. Qiu, PRD 75 (2007) 114014 [arXiv:0705.2141].
* J.C. Collins, arXiv:0708.4410.

**Unitarity and cutting rules.**
* R.E. Cutkosky, J. Math. Phys. 1 (1960) 429.
* M. Veltman, Physica 29 (1963) 186.
* G. 't Hooft, M. Veltman, *Diagrammar* (1974).

---

## Appendix A. Provenance, slot decisions and transcription notes

### A.1 Versions and reviews

**Versions.** `verify/extend_reports/`: `X1-glauber.md` (original), `X1-glauber-fix1.md` (revision after round 1), `X1-glauber-fix2.md` (revision after round 2), and this file (final revision after round 3).

**Reviews.** `X1-glauber-rev1-1.md`, `-rev1-2.md`, `-rev2-1.md`, `-rev2-2.md`, `-rev3-1.md`, `-rev3-2.md`; also `verify/extend/X1-glauber/review_r2_1.md` and `review_r3_1.md`.

**Round 3, how each required fix was applied.**

| fix (rev3-1 / rev3-2) | where applied |
|---|---|
| F1 / — (scope: cut SS lines) | §0.3, §1.2, T2 physical reading, T2′(c), T3(j), Remark C, §12, §13, OPEN-13 |
| F2 / item 2 (P4(b)) | P4(b): class imposes (ADJ) on $J_B$ only; the partner option and its power-level effect recorded |
| F3 / item 3 (P5) | P5: interference form, Feynman-gauge positivity, gauge dependence; new check `p5_interference.py` |
| F4 / item 4 (T2) | hypothesis (v); explicit $C_N,C_T,C_I$; ${\rm Im}\,p_{\rm opp}=-L/\pi+O(1)$ with a bound; numerical support `t2_constants.py` |
| F5 / item 9 (T3(e)) | corrected boost-invariant bound; interpretive sentence reduced |
| F6 / items 5, 11 (REG, qualifiers) | §2 (recast and proposed entries), §13; G5(ii) "argued [A]"; one qualifier per [R] |
| F7 / — (P2 orientation) | P2(b); exact check `p2_orientation.py` |
| F8 / — (P1) | $x_{\min}$ defined as a fraction |
| F9 / item 8 (T2′(b)) | mirror statement on $\mathcal N_A$; the $k^-$-only remark for T3 added (T3 conclusion, §13) |
| F10 / item 7 (CMP) | Zhou et al.: Sec. VI caveat, the $n_f^-$ sector, our own assessment |
| F11 / item 12 (LIT) | Barcaro et al. (verified); Forshaw–Holguin–Pathak; Pathak; Nabeebaccus et al. |
| F12 / item 10 (L8(c)) | constant $16/9+1$; the final constant 9 kept, total $\approx8.05$ |
| — / item 6 (ERR-S1b) | §12 acknowledges the reference's near-shell mechanism; the error is located in its expectation |
| per-result notes | L4 CdFR precision; EX item (iv) recomputed (`t3f_recompute.py`); L5 hypotheses weakened to (SEC) |
| F13 / item 1 (process) | outside a subagent's remit; this document is returned in full for the parent session to persist |

**Items from rounds 1–2.** All are resolved, except OPEN-8 (CSS 1988 and Collins 2011 §14.4 not accessed; re-tried in this round, but INSPIRE lists no free scan) and the process items.

### A.2 Slot decisions (App O, `OUTLINE_appMNOPQ.md` §00.4)

* **X1c `lem:appO-side-independent-windows`: PASS.** P1, with the grade [R, R_cond: `asm:appO-lcopt`] instead of the planned [R, R_PT]. The premise is that of `prop:appO-ss-cancel`.
* **X1f `prop:appO-twoexch-spectator`: PARTIAL.**
  * Insert T2 as a model theorem about the **uncut** side sum. Its first sentence states the restrictions: $\mathbb M_{\rm glob}$, $\mathcal N_A\cap\mathcal N_B$, $O(g^4)$, this pattern, $\delta_Y\le\frac12$.
  * Add T2′(a),(b) and T2′(c) [P].
  * The physical reading for $\mathcal G_0$ is [P], conditional on `asm:appO-collinear-ends` and OPEN-13.
* **X1a, X1b, X1d, X1e: not delivered.** The fallbacks stay.
* **T3:** a remark in §O.5, with (e) as a proposition. Its physical reading is at most [P].
* **ERR-S1b:** to App Q, in the restricted wording of §12.

### A.3 Proposed labels

| result | proposed label |
|---|---|
| D1–D8 | `def:appO-sectors`, `def:appO-jet-class`, `def:appO-structural-conditions`, `def:appO-glob-model`, `def:appO-nf-domain`, `def:appO-ordering-weights`, `def:appO-rotated-notation`, `def:appO-regulator-class` |
| L1, L2 | revision of `lem:appO-joint-localization` |
| L1′ | `lem:appO-multipole-localization` |
| L3 | `lem:appO-quadrant-residues` |
| L4 | (a) `lem:appO-glauber-operator`; (b)–(d) `lem:appO-halfcoinc-colour` |
| L5 | `lem:appO-kplus-rotation` |
| L6 | `lem:appO-ray-identity` |
| L7 | `lem:appO-preintegration-localization` |
| L8 | `lem:appO-two-insertion-bounds` |
| T1 | remark (alternative proof) in `prop:appO-ss-cancel` |
| P1 | `lem:appO-side-independent-windows` |
| T2, T2′ | `prop:appO-twoexch-spectator`, items (a)–(c), and `prop:appO-twoexch-regulated` |
| P2 | `prop:appO-strict-window-shape` |
| P3 | remark at `prop:dy-eikonal-twogluon` |
| T3 | `rem:appO-halfcoinc`, `prop:appO-halfcoinc-sensitivity` |
| P4 | `prop:appO-pergraph-weights` |
| P5 | `rem:appO-g6-ladder` |
| Remark P6 | extension of `rem:appO-h-emission` |
| Remark C | `rem:appO-cut-ss` |

### A.4 Transcription notes

* Print grades as in §18. For model theorems, print [P] as the QCD statement whose first sentence names the model, and give the model-internal proof in full (WRITER_SPEC_v2 §4.3, item 4). Where useful, add the [R, R_cond] transfer item with the proposed premises.
* The proposed register entries (§2.2) and rewordings (§2.3) require the lead author's decision before writers use them. Until then, writers put `% PENDING-VERIFY: <label> X1` before the affected environments.
* No novelty marker before OPEN-8.
