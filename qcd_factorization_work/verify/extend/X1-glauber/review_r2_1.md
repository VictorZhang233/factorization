# X1 (Glauber cancellation in inclusive Drell–Yan) — adversarial review, round 2, reviewer #1

Date 2026-10-11. Agent: X1-glauber-rev2-1 (a86d01bc4945f45a7). This is a restart: the first rev2-1 attempt
(agent a965df72c47e2cb4e) stopped at 02:40 on a session limit before writing anything.

## 0. Input and process

* `verify/extend/X1-glauber/REPORT.md` still does not exist. Neither do `review_r1_1.md`, `review_r1_2.md`, or
  any REPORT.md for X2 or X3. I searched the whole home directory. The current version of the report is the
  structured result of **X1-glauber-fix1** (agent a4cf5517baa9f46e2), as recorded in the workflow journal
  `~/.claude/projects/-Users-hao-cheng-Desktop-theorem-proof/c211c739-758d-4b40-bbac-67f4e1a65da4/subagents/workflows/wf_52f29317-58b/journal.jsonl`,
  line 101 (1-based). I read all of it: the summary, results[0]–[24] (DEFS … REVISIONS) and open[0]–[9]
  (O1–O10). I also read the original author result (line 42) and both round-1 reviews (lines 78 and 80), to
  check that every round-1 item was handled. Every round-1 item was handled.
* Run status (relayed question 「在正常运行吗」): the workflow is running, but not fully normally.
  - X1 and X2 are in round-2 review and X3 is in fix round 1. All three stages were restarted at 03:21 after a
    session limit.
  - Report and review files are still not written to disk, so every stage reads its input from `journal.jsonl`.
  - The parent session must write REPORT.md and the review files for X1, X2 and X3.
* My scripts are in `verify/extend/X1-glauber/review_r2_1_scripts/` and their logs in `review_r2_1_logs/`.

## 1. Verdict

**Fixable issues, all minor.**

* **Correctness.** Every statement graded [R] or [R_cond] in the revised report is correct under its stated
  hypotheses.
* **Numbers.** Every numerical claim I re-checked was reproduced. Most were reproduced by a method that neither
  the author nor the round-1 reviewers used: the inner $k^+$ integral in closed form on the **real** axis, a
  finite width $\delta\to0$, and **no contour rotation**.
* **Honesty.** The revision is honest. The [V] grade, the overclaims and the TMD claim were withdrawn. (H_glob)
  and G7 are explicit, and the CMP section correctly makes all "needed / not needed" statements relative to
  App E's framework.

What remains is listed in §4. None of it needs new mathematics:

* one factual mis-citation (LRS listed as covering the spectator–spectator pattern);
* missing literature, some of it directly relevant (Boer–van Daal–Gaunt–Kasemets–Mulders 2017;
  Doria–Frenkel–Taylor 1980 and its follow-ups; Zhou et al.; Chang–Li);
* how T2 is positioned against an explicit sentence of the reference (Rem E.32 and the status paragraph of
  Assumption E.33);
* precision gaps: the sign convention in L4(b), a hidden lower bound in P1(c), the rate in T2'(a), the scope of
  P4's consequence, the scope of L4(d)/T3(g), and an undefined term in P5.

## 2. Independent checks performed in this round

| # | claim | method (script → log) | result |
|---|---|---|---|
| C1 | L1(b), corrected constant $N2^{N+1}M_\sigma\lambda_J/\kappa$, $M_\sigma=\sum_t|c_t|\lambda_J^{-d_t}$ | 20 000 random sectors: $N\le4$, 1–2 factors per gap, complex $z$ with initial gaps in the UHP and final gaps in the LHP, $\kappa\ge2\lambda_J$ (`l1b_bound_r2.py`) | max lhs/bound = 0.42, so the bound holds. The multi-state step $2^{N+d}(\lambda_J/\kappa)^d\le2^{N+1}\lambda_J/\kappa$ is also checked |
| C2 | L1' pole weights $u_z,u_\pm$ and their sum rule | sympy (`symbolic_checks_r2.py` (2)) | exact; $u_z+u_++u_-=1$ |
| C3 | L4(a) side sum | sympy (6) | $-\tfrac12C_A\chi^2\,{\rm Re}\,p_{\rm opp}X$, exact |
| C4 | L4(b) sign | explicit commuting colour matrices on $3\otimes\bar3\otimes8$ (`colour_indep_r2.py` (S)) | $R=+2ic_1c_2\,{\rm Im}W_{12}[X_1,X_2]$ **iff** $M^{(1)}_e=-ic_eX_e$ with real $c_e$; with $M^{(1)}_e=c_eX_e$, $c_e=-i\chi_e$, the sign is opposite (see fix F3) |
| C5 | L4(c), (d1), (d2) and the four quoted norms | own SU(3) code (octet as traceless $3\otimes\bar3$ in a **random** real orthonormal basis; singlet and DY spaces from null spaces of real symmetric Casimirs) | (c): $\le5\cdot10^{-17}$ on the singlets of $(3,\bar3,8),(8,8,8),(3,3,3),(\bar3,8,3)$. (d1): $|{\rm lhs}-{\rm rhs}|\le4\cdot10^{-16}$ on random complex DY states, including $\kappa_i=\tfrac12$ with a further B-remnant parton; $0$ when B-rem $=\{j_1,j_2\}$ (A-rem $=qq,\ qqg,\ \bar qg$). (d2): $P[X_1,X_2]P$ real antisymmetric, real $\psi\to\le4\cdot10^{-17}$. Norms $0.4330,\ 0.2165,\ 0.3536,\ 0.7071$ for **every** choice of $(j_1,j_2)$ |
| C6 | T2'(b) end-pole residue | sympy, built from L3 and the scalar model (1); set values (`endpole_pred_r2.py`) | $\rho_{12}(k)=a_1a_2/[(a_1-2d_{10}k)(a_2-2\alpha_1k)]$, $\rho_{12}(0)=1$, ${\rm Res}/k_p=-a_1\alpha_1/(a_1\alpha_1+a_2|d_{10}|)$ ✓. Predicted values: apole $0.25172$ (report $0.2517$, with $\alpha_1=1.35\lambda^2$ ✓); alt $0.04834$ (report $0.0483$, with $\alpha_2=0.518\lambda^2$ ✓). The apole set also has $\alpha_0=0.5625\lambda^2>0$. That pole sits in the both-final sector, which does not reach the strip, so it gives no end-pole term, consistent with the numerics; the report should say this in T2'(b) |
| C7 | NF formula in DEFS | sympy (5) | $\alpha_1=(2s_T\!\cdot\!k_{2T}-k_{2T}^2)/(2x_sP^+)$ ✓ |
| C8 | P4 perturbation integrals | sympy closed forms (3) | $\int_0^\infty\frac{dk}{k}\rho_2=1-\ln4=-0.38629436$, $-0.37619672$, $\tfrac{39}{50}\ln6-\tfrac{13}{10}\ln2=0.49648105$, so $\delta W/s=+0.0614807i,\ +0.0598736i,\ -0.0790174i$ ✓. Also, $\rho_2$ has a **fixed sign** on $(0,\infty)$ when $A_1,A_2,A'<0$, so $\delta W\ne0$ for every admissible set with $\tilde c_2\neq0$ |
| C9 | T3(b),(d): localized race value | real contour, inner $u_2$ integral by exact partial fractions (principal Log), outer by mpmath, $\delta=10^{-3}\ldots10^{-6}$ (`t3_realcontour_r2.py`) | author set: $W_{12}\to0.5000000-0.0305591i$ (report $0.5-0.030560i$). B-asymmetric set: $0.5000000+0.0468158i$ (report $+0.046818i$). ${\rm Re}W_{12}=\tfrac12$ exactly in the localized limit |
| C10 | T3(f): A-side $k^-$ regulator | same code with L1' weights (`t3_realcontour_r2_reg.log`) | ${\rm Im}W_{12}=-0.0297491,\ -0.0203564,\ -0.0049989,\ -0.00060104$ for $K^-=10,1,0.1,0.01\times a/\lambda_B$ (report $-0.029750,-0.020357,-0.004999,-0.000601$); ${\rm Re}W_{12}=\tfrac12$ to $2\cdot10^{-9}$ |
| C11 | T2'(c): two-sided regulators, fully coincident, base set, Lorentzian $k^+$ regulator at $K^+=100\lambda_B$ | real-contour code for $J_B^{[12]},J_B^{[21]}$ with L1' weights (`t2c_realcontour_r2.py`) | see the table under T2' in §3 |
| C12 | CMP's reading of DGOPS §4 | arXiv text of 1510.08696 | the step-3 sentence ("It would be desirable to have a formal proof that this is always possible …") and eqs. (4.18)–(4.20) (cut sum + $k^-$ integral $=0$ or $1$) are as the report describes ✓ |
| C13 | bibliography | INSPIRE API | all 19 entries of the report's LIT that I checked are correct: LRS ×3, Nelson, Lindsay, Brandt, BFT, BBL, Bodwin (+ erratum), CSS 1985 and 1988, Liu–Ma, Gaunt, AFS, RS, SYZ, Del Duca, Sterman–Erdoğan (EPJ ST 235 (2026) 1493), DGOPS. I did not check Lipatov 1976 or Kuraev–Lipatov–Fadin 1977. DGOPS exists on arXiv only as **v1** |

C9–C11 never rotate the $k^+$ contour, so they also confirm L5 independently in these cases.

## 3. Per-result verdicts

**DEFS — correct.**
* (H_glob) is now an explicit hypothesis. The remark on where ordering information is generated agrees with C9
  and C10: the weights are values of the external factors at $k^-=z_e=a_e/(2k_e^+)$.
* Def 3.2 is now consistent with the model: $\mathcal J_A=i/d_0$ gives $\rho_{12}(0)=1$ (C6).
* (R) is listed as an assumption, and the NF formula is right (C7).
* Minor: in "(Def 3.4) side-independent window: see P1", P1 also uses (E.19(a)) to make $l^+$ independent of
  the SS momenta; say so (see P1).

**L1 [R] — correct.**
* The corrected constant holds (C1).
* The novelty statement is now accurate. The race formula is App E.4.4, $\sum w=1$ is the eikonal identity, and
  the new parts are the sector rule, finite-$\eta$ exactness and the error bound.

**L1' [R] — correct.** The weights and sum rule are exact (C2). Its use with regulator poles is validated by C10
and C11.

**L2 [R] — correct.** I re-derived the two-line formulas and the continuity with a kink.

**T1 — correct.** It is now presented as a re-derivation, which is right.

**P1 [R_cond] — correct as revised, with one hidden assumption.**
* (c) "$\hat\nu\sim\lambda^2Q$ on the Glauber core" requires $x^A_{\min}$ (and $x^B_{\min}$) to be bounded
  below by an $O(1)$ fraction. Otherwise the last term $2n_A(\sum|k_T|)^2/x^A_{\min}\sim\lambda^2Q/x^A_{\min}$
  is enhanced. That does not break (a), (b) or (d), but it degrades $\lambda_J\le C\hat\nu$ and with it the
  localization error $\lambda_J/\kappa$ of (E.30)–(E.31).
* The proof of (b) uses $E(l)\le2E^{(0)}(l)+\Delta_l^2/l^+$ with the *same* $l^+$ on both sides. This holds
  because SS plus components are dropped in $J_A$ (E.19(a)); state it.
* Fix F4.

**L3 [R] — correct** (round 1 verified it independently). My real-contour codes use exactly this quadrant
structure and agree with the rotated results.

**L4 [R].**
* (a) correct (C3).
* (b) correct only with the implicit convention $M^{(1)}_e=-ic_eX_e$, $c_e\in\mathbb R$ (this is the
  convention of `checks_C2_C3_C4.py` C3e). $c_e$ is never defined in the report, and the sign of $R$ flips if
  $c_e$ denotes the complex coefficient (C4). Fix F3.
* (c), (d1), (d2) and the norms are correct (C5). The proofs are right; I re-derived
  $f^{abc}T^a_{j_1}T^b_{j_2}(T^c_{j_1}+T^c_{j_2})=0$ and the reality argument.
* Scope remark, fix F7. (d3) and T3(g) say the colour factor "vanishes in the commonest DY colour
  configurations". That holds for valence (minimal-Fock) remnants. But in the leading-twist sum over Fock
  states the hadron containing $j_1,j_2$ generically has further partons, with momentum-dependent complex
  amplitudes for the different singlet couplings. I see no symmetry that forces
  $\int d\Phi\,{\rm Im}W_{12}(\Phi)\,\langle\psi(\Phi)|i[X_1,X_2]|\psi(\Phi)\rangle$ to vanish. Under complex
  conjugation of the colour state the second factor changes sign, but so can the first (it is an absorptive
  part), and their product need not vanish after integrating over the remnant phase space. This should be
  stated as open.

**L5 [R] — correct.** The $t$-range is fixed. C9–C11 confirm it without any rotation.

**L6 [R] — correct.** I re-derived it via Cauchy for $[\rho-(1+k)^{-1}]/k$; signs and the $-\pi\,{\rm Res}/k_p$
term are right.

**T2 [R_cond] — mathematically correct; two textual issues.**

I re-derived the key coefficients independently:
* $\int S_B(-i\kappa)\,d^2\kappa/(2\pi)^2=-\mathcal J_B$, from $d^2u=-d^2\kappa$;
* $\int g_B(-iU)dU/(2\pi)=-i\mathcal J_B$ under NF_B: $\alpha_0+i0$ stays in the second quadrant and
  $\beta-i0$ in the fourth;
* $W^{\rm out}(12,21)=-(i/2\pi)\int_K^\infty(d\kappa/\kappa)\varrho_{12}$, from $J_B^{[21]}\simeq-g_B/(ip_2)$
  in the strip;
* the v-term is imaginary, by (R) and the oddness of $v$;
* L6 then gives $-\tfrac14$ per mixed sector.

Issues:
* (i) **Mis-citation.** The NOVELTY paragraph cites LRS PLB 117 (1982) 105, NPB 214 (1983) 61 and NPB 222 (1983)
  189 among the "explicit two-loop calculations" that showed the physical cancellation **for this pattern**.
  But LRS have no A-side spectator (a bare quark on the A side; the report's own T3 novelty paragraph says so),
  so they contain no spectator–spectator pattern at all. Only Lindsay 1984 and BFT 1989, with a spectator in
  each hadron, can contain the fully coincident SS pattern; I checked their abstracts, not the full texts. The
  same error is in LIT ("… fully coincident pattern … (Lindsay 1984; BFT 1989; LRS)"). Fix F1.
* (ii) **Positioning against the reference.** The PHYSICAL READING says T2 "verifies the $\mathcal G_0$-restricted
  form of E.33(c2)" and "does NOT refute the reference". But the reference states the opposite expectation
  explicitly. Rem E.32 ends with 「在 $G_0$ 之内，$O(\chi^2)$ 的剩余项不应期望为零」, and the status paragraph of
  Assumption E.33 says (c) 「在 $G_0$ 之内不应期望成立（注 E.32）——所以即使对 $G_0$，它也是关于包含 $G_0$ 之外的图的完整图集
  $G$ 的假设」. The only reason given there is that the residual's colour structure coincides with that of the
  three-gluon-vertex graphs, which is not an argument that the $\mathcal G_0$ part fails.
  - T2, together with T2'(c), shows that for this pattern at $O(g^4)$ the $\mathcal G_0$ part does cancel once the
    window is combined with the near-shell region. This holds in the H_glob model, pointwise on NF, and with
    in-window regulators satisfying $K^+K^-\gg k_T^2$.
  - "Refutes App E" would be wrong, since E.33 is an assumption and stays needed elsewhere. But the report should
    say plainly that the quoted expectation and its justification are contradicted, within this scope. The
    point should go into the App Q / REFDOC errata.
  - Relatedly, the remark that the three-gluon-vertex graphs "are not needed for this cancellation" should be set
    against Boer–van Daal–Gaunt–Kasemets–Mulders, SciPost Phys. 3 (2017) 040. There, in a spectator model at
    two-gluon exchange, the three-gluon-vertex diagrams are *essential* for cancelling colour entanglement in
    the double-Boer–Mulders DY cross section, and the Glauber region gives the whole dBM term. Different
    observable (T-odd, sensitive to the imaginary parts that T2 leaves scheme dependent), so there is no
    contradiction, but the report should say why. Fix F2.

**T2' — correct; one quantitative gap in (a).**
* (a) "Re $p_{\rm opp}=O$(power)" should give the rate the proof actually yields. The inner square needs
  $K\ll K_c$, so that $\chi\chi=1-O(K/K_c)$, and the strip tail is $O(\lambda_B/K)$. Optimizing $K$ gives,
  up to logarithms, ${\rm Re}\,p_{\rm opp}=O((\lambda_B/K_c)^{1/2}+K_c\lambda_A/a)$. This is exactly the slow
  convergence seen in the numerics ($0.103, 0.054, 0.028\approx{\rm const}\cdot\lambda^{1/2}$ for $K_c=\lambda$,
  $\lambda_B\propto\lambda^2$). Fix F5.
* (b) correct (C6).
* (c) [P, model]: confirmed on the real contour (C11). With jet A localized, jet B = base set and a Lorentzian
  $k^+$ regulator at $K^+=100\lambda_B$:

| $K^+K^-/a$ | real contour, $\delta=10^{-3}$ | $\delta=10^{-4}$ | $\delta=10^{-5}$ | report (rotated) |
|---|---|---|---|---|
| none | $0.0141496-1.5646569i$ | $0.0139068-1.5646515i$ | $0.0138825-1.5646509i$ | $0.013880-1.564651i$ |
| $10^{3}$ | $0.0139942-1.5504332i$ | $0.0137738-1.5504277i$ | $0.0137517-1.5504271i$ | $0.013749-1.550427i$ |
| $1$ | $0.1491185-0.2171163i$ | $0.1491171-0.2171152i$ | $0.1491170-0.2171151i$ | $0.149117-0.217115i$ |
| $10^{-3}$ | $0.4994934+7\cdot10^{-7}i$ | — | — | $0.499493+0.000001i$ |

  The $\delta\to0$ limits agree with the rotated-contour values to about $10^{-6}$, and $N/\mathcal J_B\to
  0.999918-0.009210i$ (report $0.999918-0.009215i$). This confirms the transition: ${\rm Re}\,p_{\rm opp}\to
  \tfrac12$ when the near-shell segment is excluded and $\to O(\lambda_B/K^+)$ when it is retained. The check
  is independent of L5.

**P2 — correct.** It is known; the diagnosis is now the right one. I read Lemma E.48(d) in the reference: it gives
$w=\tfrac12\cdot\tfrac12$ for all four order pairs.

**P3 — correct** and known in substance. The REMARK is properly marked as uncertified (O9).

**T3 — correct as restated.**
* (a)–(c) hold.
* (d) is reproduced on the real contour (C9) and (f) is reproduced (C10).
* The location claim (e) is consistent with C9 and C10: everything comes from the A-side weights at
  $k^-=a/(2k^+)$.
* For (g), see the L4 scope remark (F7).
* The novelty paragraph (configuration absent from LRS, Lindsay and BFT) is accurate.

**P4 [R_cond] — correct; two refinements.**
* (1) Strengthen "generically non-zero" to "non-zero whenever $\tilde c_2\neq0$" (C8: $\rho_2$ has a fixed sign
  on $(0,\infty)$).
* (2) The CONSEQUENCE holds for the *unregulated* H_glob integrand. With G7's in-window $k^+$ regulator
  ($K^+\ll a/\lambda_A$), the out-of-window dependence at $\kappa\sim a/\lambda_A$ is cut off and $W^{\rm out}$
  becomes regulator-determined. The per-graph obstruction then rests only on the in-window $J_B$-shape
  dependence of $W^{\rm in}$ (the imaginary $v\Delta_B$ term), which is still not a function of $D$.
* State which version of (E.35) is excluded: per graph, jet-local rewriting by $D$, unregulated or regulated.
  Fix F6.

**P5 [A] — acceptable.** "Its defect is a positive operator" is undefined: either define the defect (e.g.
${\rm Disc}_s$ of the class minus the cuts that stay inside the class) or delete the phrase. Fix F8. The
description of Schwartz–Yan–Zhu matches their abstract: for pure Glauber ladders the amplitude-level violation
cancels in the cross section for single-scale observables, and the leading violation comes from graphs with at
least one soft gluon, through the Lipatov vertex.

**L7 [R] — correct and elementary.** The restriction to a pre-integration statement, with G3' replacing E.33(a),
is the honest form.

**Remark P6 — acceptable** as an ungraded remark.

**REG — consistent with the results.**
* G7 is a *new* assumption. It relocates rather than removes the content of E.33(c2) for the coincident
  $O(g^4)$ patterns: matching at the collinear ends. The report says overall [A] is unchanged, which is right;
  say this relocation explicitly in REG.
* Suggestion: map G1–G7, (H_glob), (R), (Sp), (J) and NF onto `asm:appO-*` labels. Under WRITER_SPEC_v2 §4.3 an
  [R, R_cond] statement must name every premise as an `asm:` label.

**CMP — accurate** (C12). Only the citation "arXiv:1510.08696v2" is wrong: arXiv has v1 only, and the published
version is JHEP 01 (2016) 076.

**TMD [C] — acceptable.** Add the directly relevant references:
* Boer et al. 2017 (above), which bears on item (iii) about imaginary parts and staples;
* Buffing–Mulders, PRL 112 (2014) 092002 (the colour-entanglement proposal that Boer et al. test);
* Chang–Li, PLB 726 (2013) 262, and Li, PRD 106 (2022) 014029, which claim observable Glauber phases
  (Lam–Tung violation) in pion-induced DY within $k_T$ factorization. A complete review must assess this
  contrary claim.

**EX — the log account is now accurate.** I checked `checks_C2_C3_C4.log` (ALL PASS), `checks_C2_C3_C4_r0.log`
(SOME CHECK FAILED, kept as history), `check_halfcoinc_singlets_v2.log` (ALL PASS) and `colour_dy_check.log`
(ALL PASS).

**LIT — the data are correct (C13), but the list is incomplete.** Missing, and needed for an honest novelty and
context statement:
* Doria–Frenkel–Taylor, NPB 168 (1980) 93; Di'Lieto–Gendron–Halliday–Sachrajda, NPB 183 (1981) 223;
  Andrasi–Day–Doria–Frenkel–Taylor, NPB 182 (1981) 104. These are the two-loop non-abelian Bloch–Nordsieck
  violation for coloured initial states, the origin of the colour-singlet / spectator issue that LRS resolved.
* Landshoff–Stirling, ZPC 14 (1982) 251.
* Zhou–Yan–Zhang–Li, Commun. Theor. Phys. 74 (2022) 115202 (arXiv:1708.01743): a SCET argument that SS and
  spectator–soft Glauber exchanges cancel in inclusive processes. It must be compared with CMP/REG.
* Forshaw–Kyrieleis–Seymour, JHEP 08 (2006) 059; Forshaw–Seymour–Siodmok, JHEP 11 (2012) 066 ("driven by the
  non-commutation of Coulomb/Glauber gluon exchanges with other soft exchanges", the same theme as the
  non-commuting coincident insertions here); Catani–de Florian–Rodrigo, JHEP 07 (2012) 026. These are the
  context for the $f^{abc}T_iT_jT_k$ colour structure of T3/L4.
* Becher–Hager–Jaskiewicz–Neubert–Schwienbacher, PRL 134 (2025) 061901 (factorization restoration by Glauber
  exchanges).
* Boer et al. 2017 and Buffing–Mulders 2014 (above).

My INSPIRE searches (title/abstract: Glauber with Drell–Yan/cancellation/factorization; spectator with
Drell–Yan; Glauber with spectator after 2015) found no prior statement of T2 for general LCOPT jets (ray-identity
mechanism), of T3's configuration, of P1 or of P4. The novelty claims as now restricted are therefore plausible.
(d2) of L4 is elementary linear algebra and should not be advertised beyond "new in this context".

**REVISIONS — accurate.** Every round-1 item I checked against lines 78 and 80 is addressed as described.

## 4. Required fixes

* **F1 (factual).** Remove LRS (PLB 117, NPB 214, NPB 222) from the list of calculations that showed the
  fully coincident SS cancellation, in T2's NOVELTY and in LIT. They have no A-side spectator. Keep Lindsay 1984
  and BFT 1989; describe LRS as covering the active–spectator patterns.
* **F2 (positioning).** In T2's PHYSICAL READING, state explicitly what is contradicted: within the H_glob model,
  pointwise on NF, at $O(g^4)$, for the fully coincident SS pattern, the $\mathcal G_0$-restricted E.33(c2) holds
  (T2, T2'(c)). This contradicts the expectation in Rem E.32 and in the status paragraph of Assumption E.33, and
  the colour-structure reason given there is not an argument for non-cancellation. Add the item to the errata
  (App Q). Contrast the "three-gluon-vertex graphs not needed" remark with Boer et al., SciPost Phys. 3 (2017)
  040 (different, T-odd observable).
* **F3.** L4(b): define $c_e$ by $M^{(1)}_e=-ic_eX_e$, $c_e\in\mathbb R$ (the reference's $-i\chi X$). Otherwise
  the formula's sign is ambiguous (C4).
* **F4.** P1(c): add the hypothesis $x^A_{\min},x^B_{\min}\ge c>0$, or assign the endpoint region (wee lines
  carrying SS momentum) to $K_R$ / E.44(c). State that (b) uses the E.19(a) independence of $l^+$ from the SS
  momenta.
* **F5.** T2'(a): replace "O(power)" by ${\rm Re}\,p_{\rm opp}=O((\lambda_B/K_c)^{1/2}+K_c\lambda_A/a)$ up to
  logarithms, with the one-line reason given in §3.
* **F6.** P4: "non-zero whenever $\tilde c_2\ne0$". Qualify the CONSEQUENCE as in §3 (unregulated versus
  G7-regulated; which version of E.35 is excluded).
* **F7.** L4(d3) and T3(g): replace "vanishes in the commonest DY colour configurations" by "vanishes for valence
  (minimal-Fock) remnants and for real colour states". State that generic multi-parton remnants with complex
  colour amplitudes are not covered, and that whether the remnant-integrated residual vanishes is open (add it to
  O1).
* **F8.** P5: define the "defect", or drop "positive operator".
* **F9.** LIT/TMD: add the references listed under LIT and TMD, and compare with Zhou et al. (an EFT cancellation
  argument) in CMP or REG.
* **F10.** CMP/LIT: DGOPS is arXiv:1510.08696 (v1); remove "v2".
* **F11 (process, parent session; cannot be done by a subagent).** Write
  `verify/extend/X1-glauber/REPORT.md` from journal line 101, write the round-1 reviews (lines 78 and 80) and the
  round-2 reviews, and do the same for X2 and X3. Add a persistence check to the workflow's `extend()`.

## 5. Recommended decisions for the App O slots (OUTLINE_appMNOPQ §00.4)

* **X1c `lem:appO-side-independent-windows`: PASS** (P1), after F4. Independent confirmations: both round-1
  reviewers (before the definitional repairs, which follow their requests) and this review (after them,
  re-deriving (a), (b) and (d)).
* **X1f `prop:appO-twoexch-spectator`: PARTIAL.** Insert T2 with its restrictions in the first sentence: H_glob,
  pointwise on NF_A ∧ NF_B, $O(g^4)$, this pattern. Grade it [R, R_cond] as an implication and [P] for its
  physical reading. Add T2'(c) as a [P] model statement. The model numbers have at least three independent
  confirmations (author I/II, both round-1 reviewers, and this review's real-contour code).
* **X1a, X1b, X1d, X1e: not delivered**, so use the fallbacks.
  - P3 (box plus crossed box only) does not cover X1b's three-gluon and one-loop single-exchange graphs.
  - T2 covers only the $\mathcal G_0$ part of X1e, not the Lipatov-vertex graphs.
* **T3:** at most a remark in App O §O.5 (unregulated-model property, generated at the B-collinear end,
  regulator-dependent), with no grade above [P].
* **P4:** a remark supporting the rule "E.34/E.35 on side-summed families (G2)".
