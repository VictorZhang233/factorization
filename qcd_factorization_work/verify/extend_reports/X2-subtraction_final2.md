# X2 — The precise Collins subtraction theorem and its hypotheses (App. N): verification in scalar models — FINAL REPORT, REVISION 2 (final2)

**Proof-extension slot X2 of the monograph 《QCD 因子化定理：严格证明、全阶论证与适用边界》, Appendix N (`app:appN`).**
Final revision 2, 2026-10-14. This document supersedes `X2-subtraction_final.md` (and through it `X2-subtraction.md`,
`-fix1.md`, `-fix2.md`). It applies every required fix of the independent final review
`verify/extend_reports/X2-subtraction-finalreview.md` (Fixes 1–9) and the lead-author decisions LA-2, LA-3 and LA-12 of
`writing/LEAD_DECISIONS.md`; it also takes into account the six adversarial reviews `X2-subtraction-rev{1,2,3}-{1,2}.md`.
The report is self-contained: every proof is written out, including those carried over unchanged from earlier rounds.
New scripts and logs of this revision are in `verify/extend/X2-subtraction/final2_scripts/` and `.../final2_logs/`.
The section **Final-review fixes** at the end maps each fix to the change made, and the section **Items needing
independent confirmation** lists every new or changed proof.

---

## 0. Status and scope

**What this report is.** Appendix N proves a conditional subtraction theorem (`thm:appN-subtraction`): if Collins'
conditions (CS1)–(CS3) hold on a contour Ω compatible with all subtraction terms (`asm:appN-contour`), the remainder is
power suppressed in an integral norm, uniformly in ε. Even for the one-loop triangle, neither the conditions nor the
contour had been written out. This report proves (CS1)–(CS3) for explicit graphs and integrand families in three
**scalar** models. It does so in a *fibered* form: all minus components are integrated exactly by residues, and the
estimates are made on the real base of plus and transverse components.

**No statement in this report is a statement about QCD.** Gauge numerators, Ward identities and (Abs) for transverse
polarizations are not treated (§14, OQ2).

**Print conventions (LA-2; WRITER_SPEC_v2 §4.1, §4.3 item 4).**
- Pure mathematics carries **no tag** in print (「数学」): Thm A.1, Lemmas A.2, A.3, A.7, A.8, A.9, C.3, B.8.1, B.8.2,
  E.6. The grades written next to them below ([R], [R, R_cond: …]) describe the logical status of the implication for
  the integrator; FINAL_OUTLINE_v2 already lists `thm:appN-fibered-subtraction`, `lem:appN-identification` and
  `lem:appN-lp-certificate` as (数学).
- Statements about the explicit graphs of the scalar models (M1)–(M3) are fixed-order statements about the named model
  graphs. FINAL_OUTLINE_v2 prints them as [R, R_PT] (`prop:appN-triangle-cs`, `prop:appN-phi36-dis`,
  `prop:appN-massive-photon`, `prop:appN-twoloop-algebra`). Their first sentence names the model and the order, and they
  carry 「（本命题只涉及部分子态。）」. Wherever such a result is used as evidence for a QCD statement, that QCD statement is
  [P] and its first sentence names the model (the row "[R] (model)" of WRITER_SPEC_v2 §4.3 item 4; LA-2). No X2 result
  is printed as a QCD theorem.
- LA-5 (X1 exponents) does not apply: no X1 exponent is quoted in this report.
- Instances of known theorems are presented as 「本书给出的推导」, never as new results (WRITER_SPEC_v2 §6.5 item 2.3; LA-3).

**Main results of the final revision 2.**

1. *Fibered subtraction theorem* (Thm A.1; mathematics; the implication from (FR), (FI), (CS1^φ)–(CS3^φ)). The
   unconstructed contour hypothesis is replaced by two hypotheses, (FR) and (FI), that can be checked graph by graph.
   Error type E-N^φ.
2. *One-loop off-shell triangle* (Part B).
   - (CS1^φ)–(CS3^φ) hold with λ-exponent λ²L^{≤2}, uniformly in ε ∈ (0,1/10] (Thm B.5, [R, R_PT], computer-assisted).
     The exponent 2 is optimal within the cover family s = λ^θ and, by a cover-independent argument, among all covers
     (given Prop B.3). The certificate archive is self-contained. It is now re-verified with **exact** closed-form
     identities and an **exact** coverage check (Lemma A.3(c); final-review Fix 8).
   - The four Collins terms are identified exactly with their covariant values (Prop B.2). Γ is identified exactly too
     (Prop B.3). Prop B.3 is 「本书给出的推导」 of an explicit instance of the known light-front (LCPT)–covariant
     equivalence for scalar graphs; the sliver is the non-valence (k⁺ < 0) ordering.
   - Integrated subtraction theorem for the triangle: |I_Γ − Σ_R I_{C_RΓ}| ≤ C(λ²L² + λ^{8/5}) on (0,1/10] (Cor B.6).
     The implication from Thm B.5, Thm A.1(iii), Prop B.2 and Prop B.3 is [R, R_PT], computer-assisted. Prop B.3 has
     **one** independent confirmation recorded (the final review). The PASS rule needs two (Fix 2). So, until the LA-3
     confirmation stage records the second, Cor B.6 is printed as [R, R_cond: (FI)_Γ], with the premise named.
3. *DIS in φ³₆* (Part C). All one-loop graphs are treated. For the one-rung ladder, the remainder bounds and the leading
   norm coefficient are **proved at ε = 0 (d = 6); their ε-uniformity is only sketched** (Prop C.4(e4), [P]). The
   fibered values of Γ and C_{R_1} are identified exactly with their covariant values (Prop C.4(e1),(e2); (e1) is
   「本书给出的推导」 of an instance of the LCPT–covariant equivalence). **C_H is identified with its DR-linearity value under
   (V2); its whole-integrand parametric value is [P]** (Prop C.4(e3)). Ladders of length n ≥ 2 remain [P].
4. *Massive photon* (Part D). The light-like remainder is computed exactly. For space-like rapidity regulators the
   complete real-base pole structure is given.
5. *Two-loop planar vertex* (Part E).
   - The algebra is exact, and the 50 zeroing patterns have an exact scaling structure (Thm E.1, Thm E.3(i)).
   - The nine single-approximator terms are identified with the region integrals of Smirnov–Rakhmetov 1999
     (Thm E.3(ii)).
   - **New in final2 (Prop E.4):** the auxiliary-regulator premises (RA1) and (RA2) are **proved** for the nine singles.
     The tools are the Euler–Mellin theorems of Berkesch–Forsgård–Passare 2014 and explicit closed forms obtained from
     the Schwinger representation. The proof shows why Smirnov–Rakhmetov's pure-DR values do not by themselves
     discharge (RA2): seven of the nine singles have **no** ε-domain of absolute convergence in pure DR.
   - The collinear-type values are computed independently. Together they reproduce Smirnov–Rakhmetov's eq. (10)
     **exactly**, and the nine singles sum to the leading power LP exactly. Only the (h-h) value is cited (SR eq. (4);
     Gonsalves 1983).
   - **New in final2 (Prop E.5):** (IRF) is proved for the planar and the crossed two-loop vertex, with ε₀ = 1/108.
   - The integrated remainder ∫r = Φ^(2)/Q⁴ − LP and its NLP coefficient hold as [R, R_cond: (RA1),(RA2),(V2)]. Once
     Prop E.4 is confirmed independently, the premise list reduces to the convention (V2).
6. *All orders* (Thm F.1, an implication). It is restricted to **infrared-finite graph classes** of the
   super-renormalizable model (M1), with (IRF) now defined for the renormalized integrand (Fix 5). The round-2 claims
   that (CS3^φ) holds for every UV-finite (M1) graph, and that the "bubble class" is a graph class of (M1), remain
   **withdrawn** (Prop A.6, Thm B.8).

**Verification status flags.** Every result carries one of the following flags.
- **[rev]**: re-derived or audited by at least two independent reviewers in rounds 1–3 and the final review.
- **[rev-1]**: confirmed by exactly **one** independent reviewer so far (mostly the final review). If the result is
  unchanged, one more confirmation is needed under the PASS rule.
- **[new-final2]**: new or changed in this revision. It is proved here and checked by the scripts cited, but no
  independent reviewer has seen it yet.

**The PASS rule (corrected; final-review Fix 2).** `spec_v2/OUTLINE_appMNOPQ.md` §00.4 and WRITER_SPEC_v2 §6.5 item 2.2
define PASS as follows:
- **two** independent confirmations recorded in `verify/` (two separate verification records, by independent verifiers);
- for any novelty claim, in addition, a literature check.

The final report wrongly said "one confirmation". The confirmations recorded so far are listed below. The integrator
prints a result with the grade stated here only after its record is complete. Otherwise the result is printed as an
R_cond implication with the missing premise named, or as evidence [P].

| result | confirmations recorded in `verify/` | status for print |
|---|---|---|
| Thm A.1, Lemma A.2, Lemma A.4, Props B.1, B.2, B.4, C.1, C.6, Lemma C.3, Prop C.4(a)–(d),(e2), Thm D.1, Prop D.2, Thm E.1, Prop E.2, Thm E.3(i),(iii) | ≥ 2 (rounds 1–3 and final review) | PASS |
| Thm B.5 (fibered statement) and its archive | r2_2, r3_1, r3_2; archive re-verified by the final review | PASS (X2a). The lower-bound remark of Thm B.5 is changed in final2 (Fix 9) and needs confirmation. |
| Lemma A.3(a),(b) | r3_2 (a); final review (a),(b) | PASS |
| Lemma A.3(c) verifier `r3_archive_verify.py` | final review (re-run; two limitations stated) | 1. The final2 verifier `f2_archive_verify.py` removes the limitations and is [new-final2]. |
| Prop B.3 | final review (`review_final_scripts/chk_B3.log`) | 1; second pending (LA-3 stage) |
| Cor B.6 | final review (implication) | printed [R, R_cond: (FI)_Γ] until Prop B.3 has its second confirmation |
| Prop C.4(e1); fibered closed form of C.4(e3) | final review (`chk_C4e.log`, `chk_C4e3b.log`) | 1; second pending (LA-3 stage) |
| Prop A.6(a),(b) | final review | 1 |
| Prop A.6(c) | corrected in final2 (Fix 1), following the final review's own derivation | 1 (the reviewer's derivation) |
| Lemmas A.8, A.9 | final review | 1 |
| Thm E.3(ii),(iv)–(vi) | final review (SR full text; sympy) | 1 (after the Fix 4 corrections) |
| Prop B.7 | r2_2, r3_1 (numbers), final review | PASS |
| Props E.4, E.5; Lemma E.6; f2 archive verifier; Thm B.5 lower bounds; Prop C.4(e3) step-1 bound; Prop A.6(c) formula; Lemma C.2 step 1 | none (new or changed in final2) | need two confirmations |

LA-3 schedules a pre-writing confirmation stage for Prop B.3, Prop C.4(e1),(e3), `prop:appN-phi36-dis`(c) and
`prop:appN-twoloop-remainder`(ii),(iv), using this report. Under LA-12, App N is written from this report together with
the spec entries as updated in CHANGELOG v2.4. In print, verification bookkeeping appears only in `%` comments
(WRITER_SPEC_v2 §6.12).

---
## 1. Setting, notation and conventions

Metric (+,−,−,−). Light-front components are v^± = (v^0 ± v^3)/√2 and v_T = (v^1, v^2), so that
v·w = v^+w^- + v^-w^+ − v_T·w_T. Dimensional regularization uses d = 4 − 2ε (in (M2), d = 6 − 2ε). Every loop is
integrated with the measure μ^{2ε}∫d^dk/(iπ^{d/2}), and every propagator is written 1/(−l² + M² − i0). Units are
Q̃ = 1 in (M1) and Q = 1 in (M2), (M3); the scripts mostly use P = P′ = 1/√2.

### 1.1 Models

**(M1) Off-shell Sudakov vertex, d = 4 − 2ε.**
- Fields: a complex scalar "quark" ψ and a real scalar "gluon" φ, both massless. The interaction is g ψ*ψ φ and the
  current is J = ψ*ψ.
- External momenta in (+,−,T) components, both incoming: p_1 = (P, −m²/2P, 0_T) and p_2 = (m²/2P′, −P′, 0_T), so that
  p_i² = −m².
- Kinematic variables: Q̃² ≡ 2PP′ and Q² ≡ −(p_1+p_2)² = (Q̃²+m²)²/Q̃² ≥ 4m²; λ² = m²/Q̃²; L = L̃ = ln(Q̃²/m²);
  τ ≡ m²/Q̃².
- One-loop graphs: the triangle (φ exchange) and the J–φ mixing graph. External self-energies are amputated, and
  massless tadpoles vanish in dimensional regularization.
- **Caveat.** The coupling has mass dimension one, so (M1) is *super-renormalizable*. At fixed m its off-shell vertex is
  infrared divergent for every graph that carries a self-energy insertion on a line able to become soft. It is also
  divergent for some graphs without any self-energy insertion (Prop A.6; Jackiw–Templeton 1981). Statements about (M1)
  beyond one loop are therefore restricted to graphs that satisfy the infrared-finiteness hypothesis (IRF) of §2. The
  full form factor F^(N) of (M1) is IR divergent at fixed m for N ≥ 2.

**(M2) DIS forward amplitude in φ³₆, d = 6 − 2ε.**
- Same fields and interaction as (M1); the coupling is dimensionless (renormalizable).
- Target: the off-shell ψ with p = (p^+, −m²/2p^+, 0_T). The current J is inserted twice.
- Frame q^+ = 0 and q = (0, q^-, q_T), with Q² = q_T² and x = Q²/(2p·q) ≥ x_0 > 1. This is the unphysical region: all
  invariants are space-like and there are no cuts.
- Further variables: λ² = m²/Q² and c_x = 1 − 1/x.

**(M3) Abelian massive photon, d = 4 − 2ε.**
- Massless on-shell legs p_1 = (P, 0, 0_T) and p_2 = (0, −P′, 0_T); the exchanged boson has mass M.
- λ² = M²/Q², with Q² = 2PP′ (space-like momentum transfer).

### 1.2 Fibered densities

The loop momenta k_i = (k_i^+, k_i^-, k_{iT}), i = 1, …, ℓ, are split into a *base* b = (k_i^+, k_{iT})_i and a *fiber*
(k_i^-)_i.

𝒱 denotes the space of finite sums of products Π_j (a_j(b) + Σ_i β_{ji}(b) k_i^- − i0 w_j)^{−e_j}, times measurement
functions of b. Here a_j and β_{ji} are real polynomials in b, the w_j > 0 are constants and e_j ∈ ℤ. A factor with
e_j > 0 is a *denominator*, and a factor with e_j ≤ 0 is a *numerator*.

Every propagator −l² + M² − i0 = −2l^+l^- + |l_T|² + M² − i0 is affine in the minus components, with coefficient −2l^+.
Every eikonal factor (2Pk^- − i0, 2P′k^+ − i0) is affine as well. The approximators of §1.3 replace light-cone components
or the infrared regulator by zero, so they map 𝒱 into 𝒱. The pole of (βk^- + a − i0w) lies in the upper half plane iff
w/β > 0.

**Fibered density.** For F ∈ 𝒱, the fibered density ρ_F(b) is the iterated real-line integral over k_ℓ^-, …, k_1^- in a
fixed order. It is normalized so that, whenever Fubini applies,

  μ^{2ε}∫d^dk_1⋯d^dk_ℓ/(iπ^{d/2})^ℓ F = ∫_B ρ_F dμ_ε.

At one loop in (M1) this reads dμ_ε = μ^{2ε}dx dκ κ^{−ε}/Γ(1−ε), with x = k^+ and κ = k_T². In (M2), with the rung on
shell, the measure is (1/Γ(2−ε))∫dξ/(1−ξ)∫dt t^{1−ε}(…)/v², with t = |k_T|². Each fiber integral is evaluated as a finite
sum of residues (script `lcpt.py`). The map F ↦ ρ_F is linear, since it is a sum of real-line integrals.

### 1.3 Regions, approximators, Collins terms

- 𝓡 is a finite set of regions, partially ordered, and T_R: 𝒱 → 𝒱 (R ∈ 𝓡) are the approximators: linear maps that
  replace light-cone components or the infrared regulator by zero.
- The *Collins terms* are defined recursively:
  - C_RΓ = T_R(Γ − Σ_{R′<R} C_{R′}Γ);
  - X_{R_0} = Γ − Σ_{R<R_0} C_RΓ, so that C_{R_0}Γ = T_{R_0}X_{R_0};
  - r = Γ − Σ_R C_RΓ.
  These are `def:method-subtraction` and `prop:method-chains` of the monograph.
- *Soft-first convention* (two loops): a jet line that carries soft momentum enters the hard factor with its
  soft-approximated momentum. This is Collins 2011 §10.6.6, "the requirement that the hard factor does not depend on the
  soft momenta".
- *Collins conditions* (`def:method-collins-conditions`):
  - (CS1)_{R_0}: (1−T_{R_0})X_{R_0} is power suppressed on U_{R_0};
  - (CS2)_{R_0}: C_RΓ is power suppressed on U_{R_0} for every R ≰ R_0;
  - (CS3): Γ ∈ L¹ uniformly in ε, and C_RΓ ∈ L¹ for every ε ∈ (0,ε_0].
- Their fibered versions (CS1^φ)–(CS3^φ) are the same conditions in the integral norm ∫_U|ρ_F| dμ_ε on the real base.

### 1.4 Values

1. **Fibered value** of F: ∫_B ρ_F dμ_ε, whenever this integral converges absolutely.
2. **Covariant value** I_F of F, built from quadratic propagators, linear (eikonal) factors and a polynomial numerator.
   It is *defined* by the Feynman/Cheng–Wu (equivalently Schwinger or Lee–Pomeransky) parametric representation of the
   **whole** integrand:
   - combine the denominators;
   - shift, Wick-rotate the shifted pure-quadratic loop integral, and do the Gaussian integral;
   - continue analytically in ε.
   For Γ and the Collins terms of Parts B and C, the resulting parametric integrals converge absolutely in the ε-ranges
   stated. For the two-loop composite patterns they converge nowhere, which is why Thm E.3 uses items 3 and 4.
3. **DR linearity** (standard convention, used only where stated). A sum is split into pieces whose parametric integrals
   converge on different ε-domains, and the separately continued values are added. A piece that is exactly homogeneous
   under a scaling of non-zero weight is assigned the value 0; this is the convention (V2) of `asm:appN-values`.
4. **Auxiliary analytic regularization.** Each line l is raised to the independent complex power a_l = 1 + δ_l. The
   integral is continued in (ε,δ), and δ → 0 is taken at the end. For the two-loop patterns the value is defined by the
   Lee–Pomeransky form

     I_p(ε,δ) = Γ(d/2)/(Γ(3d/2 − |a|) Π_l Γ(a_l)) ∫_{ℝ_+^6} x^{a−1}(U_p + F_p)^{−d/2} dx,

   continued meromorphically (Prop E.4). This form agrees with the Schwinger form
   (Π_lΓ(a_l))^{−1}∫x^{a−1}U^{−d/2}e^{−F/U}dx and with the Feynman form Γ(w)/(Π_lΓ(a_l)) ∫_{simplex}x^{a−1}U^{w−d/2}F^{−w}
   (w = |a| − d) wherever both members of a pair converge (the λ-integration of the overall scale needs 0 < Re w <
   Re d/2 for the Lee–Pomeransky form and Re w > 0 for the Schwinger form).
5. **DR value of an integral without a pure-DR domain** (new, made explicit by Prop E.4). Seven of the nine two-loop
   singles converge absolutely for **no** real ε when δ = 0. For them the phrase "dimensionally regularized value" can
   only mean a continuation: the iterated one-loop evaluation of Smirnov–Rakhmetov, or the restriction I_p(ε,0) of the
   continuation in (ε,δ). Prop E.4(d) proves that these agree.

### 1.5 Grades and error types

Grades follow WRITER_SPEC v2.2 §4.3.
- **[R, R_PT]**: rigorous for the stated graphs at the stated order, with no unproven input. "Computer-assisted" means
  that the only non-elementary inequalities are linear-programming optima, certified by exact rational primal–dual
  pairs. The certificates are archived self-contained and re-verified by independent code, which checks exactly:
  - the LP data;
  - the identity of every certified rational function with the density it bounds (an exact polynomial identity, no
    random points);
  - the coverage of every region by the archived cells (exact polygon arithmetic);
  - the completeness of the piece decompositions.
  See Lemma A.3(c); final-review Fix 8.
- **[R, R_def]**: an algebraic consequence of the definitions.
- **[R, R_cond: …]**: a complete proof from the listed premises; the implication is [R].
- **[P]**: finite subclass, or numerical evidence only.
- **(数学)**: pure mathematics, no tag in print (§0).

The error type **E-N^φ** denotes the bound ∫_A|ρ_F| dμ_ε ≤ Cλ^aL^K on the real fibered base, with the fiber integrated
exactly, uniformly in ε ∈ (0,ε_0]. It implies the integrated statement. It is not E-F in the spec's sense, and it is not
comparable with E-N on a deformed four-dimensional contour.

---
## 2. Register of hypotheses

The names below avoid the binding names of WRITER_SPEC v2.2 §4.4 item 4 ((GA1)–(GA4), (V1)(V2), (CU1)–(CU3), (WI1)(WI2),
(U1)(U2), (Z1)–(Z3), (AN1)–(AN6), (O1)(O2), (OP1)(OP2), …). All are *local* hypotheses of the statements that use them,
as (CS1)–(CS3) are, except (LCE) and (RA1)(RA2), which FINAL_OUTLINE_v2 registers as `asm:appN-lce` and
`asm:appN-analytic-reg` (both \tagA). Open problems are numbered OQ1–OQ17, so that they cannot be confused with the items
(O1)(O2) of `asm:intro-np-ope`.

| name | content | status (final2) |
|---|---|---|
| **(FR)** *fibered residue admissibility* of F ∈ 𝒱 | For a.e. b and at every stage of the iterated fiber integration: (i) the current integrand, as a function of the current k_i^-, is rational of degree ≤ −2 and has no pole on the real axis; (ii) on at least one side of the real axis its poles are simple. | local; verified for the triangle (Prop B.1) and the ladders (Lemma C.2) |
| **(FI)** *fibered–covariant identification* for F | ∫_B ρ_F dμ_ε converges absolutely and equals the covariant value I_F (§1.4), for ε in the stated range. | local; proved for the Collins terms of the triangle (Prop B.2), Γ of the triangle (Prop B.3, [rev-1]), and the one-rung ladder (Prop C.4(e)) |
| **(IL1)** | For ε in a non-empty open interval E ⊂ (0,ε_0] and every η > 0, ∫d^dk \|F_η\| < ∞, where F_η is F with every i0 replaced by iη. | local; not proven in general (OQ15) |
| **(IL2)** | G ∈ L¹(B,dμ_ε) for ε ∈ E, where G is the sum of the moduli of the η = 0 residue terms selected by the algorithm. | local |
| **(IL3)** *bridge* | lim_{η→0+} μ^{2ε}∫d^dk/(iπ^{d/2}) F_η = I_F for ε ∈ E. | local; not proven in general (OQ15) |
| **(IRF)** *infrared finiteness* of a graph G (**redefined, Fix 5**) | The parametric (covariant) integral of the **renormalized** integrand of G converges absolutely for every ε ∈ [0,ε_0]. The renormalized integrand is the integrand-level BPHZ subtraction of the UV-divergent subgraphs of G (`asm:appN-uv`(U1)); in an IR-finite (M1) graph these are J–φ-type two-point insertions on lines of fixed momentum (Thm F.1). For a graph without UV-divergent subgraphs it is the bare integrand. The integrand is positive in the space-like kinematics of (M1) and (M2). | local; proved for the triangle, the one-rung DIS ladder, and the planar and crossed two-loop vertices (Prop E.5, [new-final2]); false for the graphs of Prop A.6 |
| **(LCE)** *LCPT–covariant equivalence* (`asm:appN-lce`, \tagA) | Let G satisfy the hypotheses of Lemma A.4 and (IRF). Then ∫_B ρ_G dμ_ε = I_G. Sources: Chang–Yan 1973; Ligterink–Bakker 1995; see Collins 2018 for when the elementary light-front derivation fails. | not proven at the rigour of this report; explicit instances proved: Props B.3 and C.4(e1) |
| **(RA1)** (`asm:appN-analytic-reg`, \tagA) | The analytically regularized pattern integrals of the two-loop vertex (§1.4 item 4) are meromorphic in (ε,δ). | **proved for the nine singles** (Prop E.4(b), [new-final2]). For the 40 composites no analytically regularized integral exists (degenerate Newton polytope, Prop E.4(a)); their value is fixed by (V2). |
| **(RA2)** (`asm:appN-analytic-reg`) | The nine single-approximator integrals ∫T_RΓ, analytically regularized, are regular at δ = 0 for ε in a punctured neighbourhood of 0, and their δ → 0 limits are their dimensionally regularized values. | **proved** (Prop E.4(c),(d), [new-final2]); SR's pure-DR values alone do not discharge it (Prop E.4(e)) |
| **(FIN2)** | ∫Γ and ∫r are finite at ε = 0 (two-loop vertex). | ∫Γ: proved (Prop E.5). ∫r: **discharged given (RA1), (RA2), (V2)** (Thm E.3(v); Fix 4(d)), with (RA1),(RA2) now proved for the singles (Prop E.4). |
| **(COV)** *cover hypothesis* | There is a finite cover {U_R} of B on which (CS1^φ)_{R_0} and (CS2^φ)_{R_0} hold with an exponent a > 0, for every R_0. | local; verified for the triangle (Thm B.5) |
| (V2) | The values convention of `asm:appN-values`: scaleless chain terms have value zero. | convention (no tag) |

(FR) and (FI) are the *checkable replacements* of `asm:appN-contour`(a) ((GA1)(a)) in the fibered framework. The
meromorphy part `asm:appN-contour`(b) is still needed where poles in ε are removed (`cor:method-removing-eps`).

---
## 3. Part A — General results

### Theorem A.1 (fibered subtraction theorem) — mathematics (the implication from (FR), (FI), (CS1^φ)–(CS3^φ)) [rev]

**Setting.**
- Γ ∈ 𝒱 is an integrand with region set 𝓡 and approximators T_R: 𝒱 → 𝒱.
- {U_R}_{R∈𝓡} is a finite measurable cover of the base B; no boundedness of the U_R is required.

**Hypotheses.**
- (FR) holds for Γ and for every C_RΓ.
- (CS1^φ)_{R_0}: ∫_{U_{R_0}}|ρ_{(1−T_{R_0})X_{R_0}}| dμ_ε ≤ Cλ^aL^K.
- (CS2^φ)_{R_0}: ∫_{U_{R_0}}|ρ_{C_RΓ}| dμ_ε ≤ Cλ^aL^K for every R ≰ R_0.
- (CS1^φ) and (CS2^φ) hold for every R_0 ∈ 𝓡, uniformly in ε ∈ (0,ε_0], with a > 0.
- (CS3^φ): ρ_Γ ∈ L¹(B) with ∫|ρ_Γ| bounded uniformly in ε ∈ (0,ε_0], and ρ_{C_RΓ} ∈ L¹(B) for each R and each
  ε ∈ (0,ε_0].

**Statement.** Uniformly in ε ∈ (0,ε_0]:
- (i) ∫_B|ρ_Γ − Σ_R ρ_{C_RΓ}| dμ_ε ≤ C′λ^aL^K, with C′ = |𝓡|(1+|𝓡|)C;
- (ii) |∫_Bρ_Γ − Σ_R∫_Bρ_{C_RΓ}| ≤ C′λ^aL^K;
- (iii) if moreover (FI) holds for Γ and every C_RΓ, then |I_Γ − Σ_R I_{C_RΓ}| ≤ C′λ^aL^K.

**Proof.**
1. Fix R_0. From X_{R_0} = Γ − Σ_{R<R_0}C_RΓ and C_{R_0}Γ = T_{R_0}X_{R_0} we get
   Γ − Σ_{R≤R_0}C_RΓ = (1−T_{R_0})X_{R_0}. Hence

   r = (1−T_{R_0})X_{R_0} − Σ_{R≰R_0} C_RΓ, (A.1)

   an identity in 𝒱 (it is (D.10) of the reference).
2. By (FR), all iterated fiber integrals of Γ and of the C_RΓ exist for a.e. b. Fiber integrals are linear, so (A.1) holds
   for the densities: ρ_r = ρ_{(1−T_{R_0})X_{R_0}} − Σ_{R≰R_0}ρ_{C_RΓ} a.e. on B.
3. By (CS1^φ) and (CS2^φ), ∫_{U_{R_0}}|ρ_r| ≤ (1+|𝓡|)Cλ^aL^K.
4. Summing over the finite cover gives (i).
5. By (CS3^φ), all terms are integrable for ε ∈ (0,ε_0], so ∫ρ_r = ∫ρ_Γ − Σ∫ρ_{C_RΓ}; then |∫ρ_r| ≤ ∫|ρ_r| gives (ii).
6. (iii) follows from (ii) and (FI). ∎

Identity (A.1), the constant C′ and the proof were re-derived by reviewers r2_1, r2_2, r3_1 and r3_2 and by the final
review (corrected wording; final-review Fix 9).

**What it replaces.** In `thm:appN-subtraction` the premise `asm:appN-contour`(a) is a four-dimensional contour Ω,
assumed to be compatible with all subtraction terms; it is never constructed. Wherever the fibered densities are
absolutely integrable on the real base, it is replaced by (FR)+(FI), which can be checked graph by graph (Parts B, C).
`asm:appN-contour`(b), meromorphy near ε = 0, is still needed for `cor:method-removing-eps`.

**Scope.** The theorem needs fibered densities that are absolutely integrable on the real base. This holds for:
- the triangle of (M1);
- graphs of (M1) satisfying (IRF), given (LCE) (Cor A.5);
- (M2) at x > 1.

It does **not** cover:
- Glauber-pinched (cut) processes (OQ7);
- real-base fibrations with poles, e.g. space-like rapidity regulators (Prop D.2);
- graphs with q^+ = 0 subloops. These are pure zero modes in this frame and violate (FR); examples are the J–φ mixing and
  t-channel graphs of (M2), which are treated outside the fibered framework (Prop C.1(iv),(v));
- IR-divergent graphs of (M1), for which (CS3^φ) is false (Prop A.6).

**Prior art and novelty.**
- Nested (forest) subtractions for general graphs exist at the level of pinch surfaces:
  - Collins 2011, ch. 10 (Theorems 1R–4);
  - the coordinate-space analysis of Erdoğan–Sterman 2015;
  - Ma 2020, a BPHZ-like IR forest formula for wide-angle massless amplitudes, in which the singularities of the
    subtraction terms cancel pairwise.
- New here is the formulation as an integral-norm (power-suppression) statement on a real fibered base, with the
  checkable hypotheses (FR), (FI). The proof is the elementary one of `thm:appN-subtraction`.

**Remarks.**
- (a) The literal (CS3) on the *real* four-dimensional contour fails already for Γ: there is a ln(1/η) divergence
  across light cones. This is why the monograph uses a deformed Ω. It is a remark, not an error of the source.
- (b) *Sharpening.* For (CS2^φ) to be uniform in ε, the non-maximal U_R must be UV-bounded or must carry items that decay
  fast enough. Example, the triangle with a Def-D.5-type unbounded U_{C_1} (units of §1.1):
  ∫_{U_{C_1}∩{k^+>P}}|ρ_{C_{C_2}}| = ∫_P^∞dx∫_0^{2sx}dκ κ^{−ε}/(Pe_2(e_2+κ)) ≃ (2s)^{1−ε}P^{−ε}/(ε(1−ε)P(2P′)²) as s → 0,
  which is not uniform in ε. The cover of Thm B.5 puts the unbounded sliver {−m²/2P′ < k^+ < 0}×{κ>0} in U_{C_2}; this is
  harmless, because the sliver items decay like κ^{−2}.
- (c) *The fibration is part of the statement.* Adding transverse azimuths to the fiber turns first-order full norms
  into second-order ones (Collins 2011 §10.7.3: "these commonly vanish after an integral over angle. Then the actual
  error is one power better: p = 2"). This is quantified in §7.4 and Prop C.4.

---

### Lemma A.2 (identification lemma for pure-denominator products) — mathematics [rev]

**Setting.** F = Π_{j=1}^J D_j^{−e_j}, with every e_j ≥ 1 (no numerator factors), where D_j = a_j(b) + Σ_iβ_{ji}(b)k_i^-
− i0 w_j and w_j > 0. F_η is F with i0w_j replaced by iηw_j, η > 0.

**Hypotheses.**
- **(FR)_η**: (FR) holds for F_η for every η ∈ [0,η_0], with simple poles on the closing side, the same closing sides,
  and no coincident poles, for a.e. b. The closing side sign(w/β) is automatically independent of η.
- (IL1).
- (IL2).

**Statement.** For ε ∈ E: ∫_Bρ_F dμ_ε = lim_{η→0+} μ^{2ε}∫d^dk/(iπ^{d/2}) F_η.

**Corollary A.2′.** If in addition (IL3) holds, then (FI) holds for F.

**Proof.**
1. For η > 0, Fubini applies by (IL1): ∫d^dk F_η = ∫_Bρ_{F,η}dμ_ε.
2. At each stage of the residue algorithm, substituting the pole of a factor f, k_i^- = (−a_f − … + iηw_f)/β_f, turns
   every other factor g into an affine function of the remaining minus variables. Its real part does not depend on η,
   and its imaginary part is η times a real coefficient. Hence |g_η| ≥ |g_0|.
3. The prefactors 1/β_f do not depend on η.
4. All exponents are positive, so each residue term at η is bounded in modulus by the corresponding term at η = 0.
5. The set of contributing poles does not depend on η: it is fixed by sign(w/β). Hence |ρ_{F,η}| ≤ G.
6. ρ_{F,η} → ρ_F a.e., and dominated convergence (IL2) gives the statement. ∎

Under (IL1)–(IL2) no zero-mode (k_i^+ = 0) contribution can arise: at finite η the set {k_i^+ = 0} is null, and (IL2)
excludes δ-like concentration as η → 0.

**Scope.**
- (1) The lemma does **not** cover the composite Collins terms.
  - For C_{C_1} = T_1 + T_2, the η = 0 residue pieces are 1/(Ah_2) and −1/(Bh_2). At P = P′ = 1/√2, m² = 0.01, ε = 0.1
    their moduli integrate over x > δ to 462.72, 1644.85, 4614.22 and 12072.96 for δ = 10⁻⁴, 10⁻⁸, 10⁻¹², 10⁻¹⁶,
    growing like δ^{−ε}/ε (`r2_triangle_identification.py` PART E; reproduced by reviews r3_1 and r3_2).
  - Written as one product with the numerator D_g, C_H violates |N_η| ≥ |N_0|.
- (2) For the triangle and the one-rung ladder, (FI) is proved directly and exactly (Props B.2, B.3, C.4(e)), so the lemma
  is not needed there. It remains a general tool for pure-denominator integrands.
- (3) On the hypotheses:
  - (IL1): Minkowski power counting at fixed η makes it plausible for the triangle's Γ when 0 < ε < 1. The worst regions
    are the two-dimensional cones {k² = 0, p_i·k = 0}, which contribute ∫R^{−1−2ε}ln²R dR, so it fails logarithmically at
    ε = 0. It is not proven.
  - (IL3): for propagator-only integrands whose external momenta can be chosen purely spatial (Euclidean region), this is
    the textbook Wick rotation at fixed η followed by dominated convergence. The triangle's kinematics always has
    Q² = (Q̃²+m²)²/Q̃² ≥ 4m² > 0 with p_i² = −m²; purely spatial p_1, p_2 would need |p_1+p_2| ≤ 2m, so the triangle is
    never in the Euclidean region. (IL3) there would rest on analytic continuation in the external invariants
    (cf. Zimmermann 1968 for Minkowski power counting). It is not proven here and is not used.

---

### Lemma A.3 (tropical/LP certificate lemma) — mathematics; (a),(b) [rev]; (c) [new-final2] (exact verifier)

**Setting.**
- f = N/Π_kD_k in local coordinates y_i = e^{LX_i} (i = 1,…,n), with m² = e^{−L} and L = ln(1/λ²).
- N is a real polynomial in (y, m²). Its coefficients may depend on *frozen* variables confined to compact intervals in
  (0,∞).
- Each D_k is comparable on the cell to a positive-coefficient polynomial g_k, with explicit constants: at most 2^{deg} per
  factor for the frozen ranges [1/2,1] and [1,2], and at most (15/7)^{deg} for the sliver range [0.7,1.5].
- w is the vector of measure weights (the κ-weight is 1 − ε).
- For each monomial a = (a_1,…,a_n,a_m) of N: ψ_a(X) = ⟨a+w,X⟩ − a_m − Σ_k max_{b∈supp g_k}(⟨b,X⟩ − b_m).
- U is a polyhedron: the cell in normalized log coordinates.

**Hypothesis.** Every ψ_a has a bounded argmax face F_a on U.

**(a) Equivalence.** The hypothesis holds iff ψ_inf(r) := ⟨a+w,r⟩ − Σ_k max_b⟨b,r⟩ < 0 for every r ∈ rec(U)∖{0}.

*Proof.* Since max(u+v) ≤ max u + max v, ψ_a(x+tr) ≥ ψ_a(x) + tψ_inf(r) for t ≥ 0.
- If ψ_inf(r) ≥ 0 for some r ∈ rec(U)∖{0} and x* ∈ F_a, then x*+tr ∈ U and ψ_a(x*+tr) ≥ max ψ_a. So the ray lies in F_a,
  which is unbounded.
- Conversely, F_a is a polyhedron. If it is unbounded, it contains a ray x*+tr with r ∈ rec(U)∖{0}. Along this ray ψ_a is
  eventually affine with slope ψ_inf(r), and it is constant on F_a, so ψ_inf(r) = 0. ∎

**(b) Statement.** ∫_U|f|Πy_i^{w_i−1}dy ≤ C L^d λ^{−2φ*}, with φ* = max_a max_Uψ_a and d = max_a dim F_a ≤ dim U. With
polynomial weights (1+L|X|)^j, which logarithmic insertions require, the power is L^{d+j}.

*Proof.*
1. Borinsky's tropical approximation (AIHPD 10 (2023) 635, Thms 8.A/8.B) gives two bounds:
   - |N| ≤ (Σ|c_a|)max_a y^a m^{2a_m}, where frozen coefficients satisfy |c_a(u)| ≤ Σ_j|c_{a,j}|hi^j;
   - a positive-coefficient g_k satisfies g_k ≥ (min_b c_b)max_b y^b m^{2b_m}.
2. In log coordinates the integrand is therefore ≤ C L^n Σ_a e^{Lψ_a(X)} dX.
3. A Hoffman-type error bound for polyhedral concave functions gives max_Uψ_a − ψ_a(X) ≥ c·dist(X,F_a). This uses the
   hypothesis through (a).
4. A Laplace estimate gives ∫_U e^{Lψ_a} ≤ C e^{Lφ_a} L^{−(n−dim F_a)}. Finally e^{Lφ} = λ^{−2φ}. ∎

*Uniformity in ε.* ψ_a is affine in ε, so the LP value is convex in ε and the endpoint certificates bound every
intermediate ε. Uniform constants follow from κ^{−ε} ≤ 1 + κ^{−ε_0} on [0,ε_0].

**(c) Implementation and its independent verification.**
- *Tooling* (`r1_lptools.py`, `r2_lptools.py`; archiving wrapper `r3_lptools.py`):
  - (i) an exact rational dual y and primal x with c·x = b·y are constructed; strong duality is asserted before the face
    bound is used;
  - (ii) the face bound is dim F_a ≤ (n+K) − rank(A_{S⁺}) with S⁺ = {i: y_i > 0}. Only these constraints are forced tight
    by complementary slackness (the round-2 repair of review r2_2 F4);
  - (iii) the recession check is exact: in 2D the recession cone is split into closed-quadrant pieces, and endpoints and
    tie points are evaluated;
  - (iv) frozen variables enter only as coefficients.
- *Archives.* Every piece record stores:
  - the rational function it bounds (numerator, denominators);
  - the local variables, frozen intervals, weights and cell constraints;
  - the numerator support and the denominator supports.
  The archives are `logs/r3_triangle_certificates_sc.json.gz` (58 piece records, 546 monomial certificates) and
  `logs/r3_bubble_certificates_sc.json.gz` (2986 piece records, 70,373 certificates).
- *First verifier* (`scripts/r3_archive_verify.py`; re-run by the final review with 0 failures). It imports no
  certificate-producing code. It:
  - recomputes supports, sign-definiteness and comparability constants;
  - rebuilds every LP;
  - checks exactly y ≥ 0, A^Ty = c, b·y + const = value, Ax ≤ b and c·x + const = value;
  - recomputes S⁺, the rank, the face bound, the exponent −2max_a value_a, the L-power and the exact maximal recession
    slope;
  - compares the certified rational functions with independently coded densities.

  The final review found **two limitations** (Fix 8): (i) the closed-form comparison was an exact evaluation at three
  random rational points, i.e. a randomized identity test, not a symbolic proof; (ii) the coverage of each U_R and of the
  base by the archived cells was not machine-checked (the reviewer checked it by inspection and by sampling,
  `review_final_scripts/chk_coverage.py`, 0 uncovered points).
- *Final2 verifier* (`final2_scripts/f2_archive_verify.py`, log `final2_logs/f2_archive_verify.log`; [new-final2]). It
  repeats the LP checks verbatim and **removes both limitations**:
  - (C′) *exact closed forms.* For every record, the archived rational function f_arch is proved equal to c·f_exp, with c a
    non-zero constant, by an exact polynomial identity over ℚ(√2): √2 is kept as a symbol s₂ and reduced modulo s₂² − 2,
    and c is computed at one rational point with s₂ symbolic. No random points are used. f_exp is coded independently:
    - from Prop B.1 for the triangle items, remainder and sliver;
    - from the four-shell representation of Thm B.8 for the remainder pieces P0–P4, the corner shells and the u > 1
      pieces;
    - from the shell forms Γ = l_D^j r_G, C_S = l_e^j r_S, C_{C_1} = l_D^j a_1 − l_e^j a_2, C_{C_2} = l_h^j r_{C_2},
      C_H = −l_t^j b_1 + l_h^j b_2 for the **48 log-weighted item records**, which round 3 had verified at the LP level
      only.
    The shell forms are themselves checked exactly against Prop B.1, and each item decomposition (main part plus
    log-difference corrections) is checked as an identity in independent symbols l_D, l_e, l_t, l_h for j = 1, 2, 3.
  - (V) *exact coverage.* For every region, the union of the archived cells contains the target region. The proof is
    exact rational polygon subtraction in normalized log coordinates: target ∩ box minus the cells has zero area. The box
    contains every vertex of the line arrangement of the target, the cells and the coordinate axes, so every face of
    that arrangement meets the box in positive area. One-dimensional cells are checked by interval inclusion. The
    targets are the cover sets of Thm B.5 intersected with each frozen strip, relaxed to L-independent polyhedra
    ("u ≤ 1/2" ⊂ "X_u ≤ 0").
  - (Pc) *piece completeness.* Every remainder cell carries P0–P4, each with one certified alternative; every u > 1 cell
    carries ρ_r and w_a|T_e|; the corner carries its four shells; every item cell carries its main part and corrections
    that connect all shells of the item's terms.
- *Results* (both archives, ε = 0 and ε_0 = 1/10):
  - 3044/3044 piece records and 70,919/70,919 monomial certificates pass the LP checks;
  - 3044/3044 closed-form identities hold exactly, all with c = 1 (58 triangle, 2938 bubble pieces, 48 bubble items);
  - coverage holds exactly for:
    - triangle items at θ = 2 and θ = 1;
    - the triangle remainder strips;
    - the sliver strips, with the frozen range [7/10, 3/2] ⊃ [1/√2, √2] checked exactly;
    - bubble region I (135 cells);
    - bubble region II (134 cells plus the corner cell);
    - bubble u > 1 (60 cells);
    - all 10 bubble (U_R, item) pairs;
  - piece completeness holds;
  - maximal face bound 2; minimal exponents as in Thms B.5 and B.8.
- The recession check for n ≥ 3 is floating-point only. It is not used, because every cell here is one- or
  two-dimensional.

**Novelty.**
- The ingredients are known: Borinsky's tropical approximation, and polytope and region methods (Jantzen 2011;
  Semenova–Smirnov–Smirnov 2019; Gardi–Herzog–Jones–Ma–Schlenk 2023; Ma 2024; Arkani-Hamed–Hillman–Mizera 2022).
- Belitsky–Smirnov 2026, §4, use Newton polytopes and tropical geometry to *evaluate* region integrals of the same
  off-shell form factor; this is a different use.
- Their use to certify Collins' integral norms (CS1)–(CS3) appears to be new. The INSPIRE searches of reviews r1–r3 found
  no prior instance.

---

### Lemma A.4 (light-cone positivity; scalar cubic models, massless internal lines) — [R, R_PT] [rev]

**Hypotheses.**
- G is a connected graph of (M1) or (M2) without tadpoles.
- In case (b), every loop carries target plus momentum. This excludes the J–φ mixing and t-channel graphs.
- Kinematics: (a) as in (M1); (b) as in (M2) with x > 1.

**Statement.**
- For a.e. b, ρ_G is a finite sum over x^+-orderings of Π_lines(2l^+)^{−1}Π_states(E_st − Σ_{l∈st}l_T²/2l^+)^{−1}, times
  a positive constant.
- Every energy denominator is strictly negative.
- All orderings have the same number of states: 2ℓ for the vertex (V = 2ℓ+1) and 2ℓ+1 for DIS (V = 2ℓ+2).
- Hence ρ_G has a definite sign.

**Bounds.**
- (a) The current vertex is last, and E_st ∈ {p_1^-, p_2^-, p_1^-+p_2^-}, so |E_st − Σ| ≥ m²/2P.
- (b) DIS.
  - Before the absorption and after the emission, E_st = p^- and |·| ≥ m²/2p^+.
  - After the absorption the state carries total plus momentum p^+ and transverse momentum q_T. Cauchy–Schwarz gives
    Σl_T²/2l^+ ≥ Q²/2p^+, hence |E_st − Σ| ≥ (m² + Q²(1−1/x))/2p^+.
  - For the crossed ordering the bound improves to (m² + Q²(1+1/x))/2p^+ (review r2_2).
  - The variant with 1/ξ proposed in review r1_2 fails when spectators carry transverse momentum.

**Proof.**
- The residue algorithm for scalar cubic graphs reproduces light-cone-ordered perturbation theory (Chang–Yan 1973;
  Ligterink–Bakker 1995).
- There are no instantaneous terms, because the vertices are scalar. There are no zero modes, because every loop has at
  least two propagators depending on its k^- and non-constant plus momentum.
- Each energy denominator equals E_st − Σ with E_st < 0 and Σ ≥ 0. ∎

**Novelty.** Negativity of the light-cone energy denominators below threshold is classical. It is *analogous to* (not
"equivalent to") the positivity of the Symanzik F polynomial for space-like invariants. Its use for (CS3^φ) is modest.

### Corollary A.5 ((CS3^φ) for Γ) — [R, R_cond: (LCE)]; (IRF) is a hypothesis on G [rev]

Let G satisfy the hypotheses of Lemma A.4 and (IRF). Given (LCE), (CS3^φ) holds for Γ = G:
∫_B|ρ_G|dμ_ε = |I_G| < ∞, uniformly in ε ∈ [0,ε_0].

*Proof.*
1. By the definite sign (Lemma A.4) and (LCE), ∫|ρ_G| = |∫ρ_G| = |I_G|.
2. By (IRF), the positive parametric integrand converges absolutely.
3. For a ∈ (0,C], the bound a^{−s(ε)} ≤ a^{−s(0)} + a^{−s(ε_0)} holds for exponents s affine in ε. It bounds the
   integral uniformly by its values at the two endpoints (the integrand is exp(εA + B), convex in ε). ∎

**Unconditional cases.** For the one-loop triangle (Prop B.1) and the one-rung DIS ladder (Prop C.4(c)), ∫ρ_Γ < ∞ is
computed directly. There, (CS3^φ) for Γ holds with neither (LCE) nor (IRF) [R, R_PT]. Lemma A.2 cannot replace (LCE):
for a single-signed density, (IL2) *is* ∫|ρ_G| < ∞ (review r2_1).

**Withdrawn** (final round; reviews r3_1, r3_2). Round 2 claimed that (CS3^φ) holds for Γ, uniformly in ε, for every
UV-finite graph satisfying the hypotheses — in (M1), all graphs without one-loop two-point subgraphs and without
tadpoles. Its proof took UV finiteness for finiteness. Prop A.6(a) gives a counterexample that satisfies every stated
hypothesis.

**Status of (IRF).**
- *Proven* for the one-loop triangle and the one-rung DIS ladder (direct computation), and — new in final2 — for the
  planar and the crossed two-loop vertex graphs of (M1), for ε ∈ [0, 1/108] (Prop E.5, exact certificate). For these two
  graphs Cor A.5 therefore holds given (LCE) alone. In addition, the positive fibered density of the planar vertex
  integrates numerically to the Usyukina–Davydychev value (§7.4).
- *False* for the (M1) graphs of Prop A.6.
- *Expected*, from soft power counting (Prop A.6(c),(d) and the standard IR power-counting theorem, cf.
  Lowenstein–Zimmermann 1975; not proven here in this non-Euclidean but positive-F setting), for the ladder vertex graphs
  of (M1) beyond two loops and for all UV-finite (M2) graphs satisfying (b), e.g. every DIS ladder.
- **Recorded deviation** (final review [7]; §17): round 2 had stated an (M2) clause "every DIS ladder" conditional on
  (LCE) as part of the corollary. The final report downgraded it to "(IRF) expected", because IR finiteness in (M2) is
  only power-counted (OQ16). That deviates from review r3_2's fix 2 ("keep the (M2) clause unchanged"). The downgrade is
  kept in final2: an unproven (IRF) cannot be stated as part of the corollary.

---

### Proposition A.6 (infrared structure of (M1) beyond one loop) — (a),(b) [R] [rev-1]; (c),(d) power counting; (c) corrected in final2 (Fix 1) [new-final2]. In print: the remark `rem:appN-m1-infrared` (no tag).

(M1) is massless and super-renormalizable ([g] = mass¹ in d = 4).

**(a) The kite counterexample.** Let G_kite be the three-loop vertex graph obtained from the triangle by inserting the
massless two-loop "kite" self-energy (a ψ loop with an internal φ chord across it) into the exchanged φ line.
- G_kite is connected and has no tadpole and no one-loop two-point subgraph. Every subgraph is UV finite (ω = 4L − 2I < 0;
  for the kite ω = −2). Every loop carries non-constant plus momentum. So G_kite satisfies all hypotheses of round-2
  Cor 2.11.
- The kite is a homogeneous function of k² that is UV and IR finite at space-like k ≠ 0:
  Σ_2(k²) = K(ε)(−k²)^{−1−2ε}, with K(0) = 6ζ(3) times positive couplings.
- Hence G_kite = K(ε)×(the triangle with the exchanged line raised to the power ν = 3+2ε). This factorization uses the
  absolute convergence of the kite subintegral at space-like k ≠ 0.
- The parametric representation of that triangle is Γ(ν+2−d/2)/Γ(ν) ∫_simplex α_g^{ν−1}F^{d/2−ν−2}, with
  F = α_1α_2Q² + m²α_g(α_1+α_2) (U = 1 on the simplex).
- At the soft corner α_1, α_2 → 0, F ≃ m²r with r = α_1+α_2, and dα_1dα_2 = r dr dθ. The corner contributes
  ∫r^{d/2−ν−1}dr, which converges absolutely iff ν < d/2 = 2−ε, i.e. ε < −1/3 here.
- The only pole is the corner pole at ε = −1/3; Γ(ν+2−d/2) = Γ(3+3ε) is finite. Therefore the DR value of G_kite,
  continued from ε < −1/3, is **finite** at ε = 0, while the positive parametric integral itself diverges for every
  ε ∈ [0,ε_0].
- *What the refutation needs* (Fix 9). The divergence of this positive parametric integral alone shows that the step
  "I_Γ < ∞" of round-2 Cor 2.11 fails, i.e. the round-2 proof is invalid. To conclude that the round-2 **statement**
  ((CS3^φ) for G_kite) is false, one uses the effective fibered density. It is obtained by integrating the kite subgraph
  covariantly first — an (LCE)-type step for the subgraph, not proven here — and then closing the outer k^- contour on the
  D_1 pole (the Σ_2 cut and the D_g poles lie on the other side): ρ = K(ε)(P−x)^{2+2ε}/(A^{3+2ε}D̂_2) ≥ 0, with D_g = A/(P−x)
  at the D_1 pole. It is not integrable at the corner (x,κ) → 0.
- *Proxy numerics* (ε = 0, the integer-power proxy 1/(D_g³D_1D_2); parameters m² = 0.01, P = P′ = 1/√2; cut x > δ):
  ∫_{x>δ}ρ_3 = 2.46·10⁸, 3.47·10¹⁰, 3.50·10¹² for δ = 10⁻³, 10⁻⁵, 10⁻⁷, growing like 1/δ. The triangle (n = 1) gives
  21.83, 22.82, 22.83 (`r3_M1_infrared.py`, part (c)).

**(b) Self-energy insertions.**
- The renormalized one-loop ψ-bubble on the exchanged φ violates ν < 2−ε at ε = 0. In DR, ν = 2+ε for the bare part and
  ν = 2 for the counterterm part.
- At ε = 0 the corner-cut integrals grow like ln(1/δ) (ν = 2), and like ln² with the renormalized logarithm. The numbers
  (`r3_M1_infrared.py`, part (b); Q² = 1, m² = 0.01; δ = 10⁻⁴, 10⁻⁶, 10⁻⁸) are 5.6·10⁴, 1.0·10⁵, 1.5·10⁵ for ν = 2 and
  6.0·10⁵, 1.3·10⁶, 2.3·10⁶ with the logarithm. The increments 4.602·10⁴ and 4.605·10⁴ per two decades match
  ln(100)/m⁴ = 4.605·10⁴.
- The same holds for a ψ self-energy on an internal ψ line that becomes soft (k → p_1).
- These divergences are positive in the parametric representation, with coefficients ∝1/m⁴ and ∝1/(m²Q²) respectively.
  So F^(2) of (M1) is **IR divergent at fixed m**, and F^(N) is IR divergent for N ≥ 2.
- This is the infrared problem of massless super-renormalizable theories (Jackiw–Templeton, PRD 23 (1981) 2291): the
  exact amplitudes are non-analytic in the coupling.

**(c) Soft power counting at fixed m (corrected in final2; final-review Fix 1).**
- Consider a set S of internal lines that can be simultaneously soft, with connected complement. Let V_S be the number of
  all-soft (cubic) vertices, V_2 the number of two-valent insertions of mass dimension two on soft lines (hard or
  counterterm two-point insertions, which in (M1) are constants), and n_a the number of endpoints of soft lines on
  non-soft vertices.
- Counting line ends gives 2I_S = 3V_S + 2V_2 + n_a. Each all-soft vertex and each insertion imposes one momentum
  conservation constraint, so L_S = I_S − V_S − V_2.
- Under the uniform soft scaling k ~ λ_s, each soft loop gives λ_s⁴, each soft propagator λ_s^{−2} and each constant
  insertion λ_s⁰. The infrared degree is therefore

  **ω_IR = 4L_S − 2I_S = n_a − V_S − 2V_2.**

- **Each two-valent constant insertion lowers ω_IR by 2** (one more propagator and one more vertex: Δω = 4·0 − 2·1). The
  final report said "by 4"; that was wrong (final review [9]), and with "4" the counterterm graph would be power
  divergent, contradicting (b). With the corrected rule, the triangle with one counterterm insertion on the soft φ has
  ω_IR = 2 − 2 = 0. This is exactly the logarithmic case ν = 2 of (b): the corner integrand is r^{d/2−ν−1} = r^{−1−ε}
  (`r3_M1_infrared.log`, part (a)).
- A divergence is expected for ω_IR ≤ 0. Examples (all with V_2 = 0; each table entry re-derived by the final review):

| soft subgraph | I_S | V_S | n_a | ω_IR |
|---|---|---|---|---|
| single soft φ (the triangle) | 1 | 0 | 2 | +2 |
| two soft rungs (planar or crossed two-loop ladder) | 2 | 0 | 4 | +4 |
| one-loop ψ-bubble on a soft φ (bubble lines soft) | 4 | 2 | 2 | 0 |
| ψ self-energy on a soft ψ line | 4 | 2 | 2 | 0 |
| two-loop kite on a soft φ | 7 | 4 | 2 | −2 |
| soft ψ triangle with three soft φ legs on the external ψ lines (three loops, no self-energy insertion) | 6 | 3 | 3 | 0 |
| soft ψ box with four soft φ legs (four loops) | 8 | 4 | 4 | 0 |
| single soft φ with one constant (counterterm) insertion | 2 | 0 | 2 (V_2 = 1) | 0 |

- "No self-energy subgraph" is therefore **not** sufficient for IR finiteness in (M1).

**(d) (M2) has no soft infrared problem.** In φ³₆ (d = 6), ω_IR = 6L_S − 2I_S = 2n_a > 0 (with insertions, 6L_S − 2I_S is
unchanged by MS-bar two-point insertions, which are ∝k² and do not lower ω).

*Proofs.*
- (a): the parametric exponent computation, positivity, and the explicit corner integrals. The factorization of the kite
  subintegral uses its absolute convergence at space-like k ≠ 0. The fibered statement uses the effective density, as
  stated.
- (b): the same, for ν = 2 and ν = 2+ε.
- (c), (d): power counting. Divergence for ω ≤ 0 follows from a lower bound of the positive parametric integrand on a
  neighbourhood of the corresponding face. Convergence for ω > 0 at all faces is the standard IR power-counting theorem,
  used here only as a heuristic.

Numerics: `r3_M1_infrared.py`, reproducing review r3_1 `r3_M1_infrared.py` and review r3_2 `c7_M1_IR.py`.

**Consequences.**
- Cor A.5 needs (IRF).
- Thm F.1 is restricted to IR-finite graph classes, and the full form factor of (M1) at N ≥ 2 is not covered.
- The round-2 open items "two-loop graphs with UV subdivergences" (O3) and "the full graph beyond the hybrid model" (O13)
  are *not open* in (M1): those graphs are IR divergent (§14, OQ3, OQ13, OQ16).
- Prop A.6(a) is a correction of this report's own round-2 claim (W19). It is not a result for the monograph's novelty
  ledger (Fix 3; §12).

---

### Lemma A.7 (one-dimensional reduction of rung kernels, d = 6) — mathematics [rev]

**Setup.**
- The parent has (v, K); the child has fraction z and transverse momentum k.
- v′ = zv + |k − zK|²/(1−z).
- κ = 1/(π²(1−z)v′²).

**Statement.** For every F ≥ 0:
- ∫d⁴k κF(v′) = (1−z)∫_{zv}^∞dt (t−zv)F(t)/t² ≤ (1−z)∫_{zv}^∞dt F(t)/t;
- for the projected parent (v = 0, K = 0), the right-hand side is (1−z)∫_0^∞dt F(t)/t.

*Proof.* Set l = k − zK. Then d⁴l = π²|l|²d|l|² and |l|² = (1−z)(t−zv). ∎

In d = 6−2ε the reduction carries the factors (1−z)^{1−ε} and (t−zv)^{1−ε}. With the measure d^dk/(iπ^{d/2}), the
rung-on-shell fibered measure is (1/Γ(2−ε))∫dξ/(1−ξ)∫dt t^{1−ε}(…)/v²; review r3_1 re-derived it from the R-pole residue
1/(p^+(1−ξ)) and S = 1/v at that pole. The lemma is elementary and new only as a tool.

### Lemma A.8 (Vandermonde lemma) — mathematics [rev-1]

**Setting.** c_k(ε), k = 0,…,K, are meromorphic at ε = 0 with Laurent coefficients c_{k,j} (j ≥ −p). Put
S(ε,L) = Σ_k c_k(ε)e^{kεL}, and suppose that lim_{ε→0}S(ε,L) exists for every L in a non-empty open interval.

**Statement.**
- (i) c_{k,−N} = 0 for all k and all N ≥ K+1.
- (ii) lim_{ε→0}S(ε,L) = Σ_{n=0}^{K}(L^n/n!)Σ_k k^n c_{k,−n}, a polynomial in L of degree ≤ K.

*Proof.*
1. The coefficient of ε^{−s} (s ≥ 1) in S is the polynomial Σ_n(L^n/n!)Σ_kk^n c_{k,−s−n}. It vanishes on an open
   interval, so Σ_kk^n c_{k,−N} = 0 for all N ≥ 1 and 0 ≤ n ≤ N−1.
2. For N ≥ K+1 the equations n = 0,…,K form a Vandermonde system with the distinct nodes 0,…,K (det = 288 for K = 4).
   Hence c_{k,−N} = 0.
3. The finite part is the stated sum; its terms with n ≥ K+1 vanish by (i). ∎

### Lemma A.9 (continuation of subtracted Mellin integrals) — mathematics [rev-1]

**Setting.** f: (0,∞) → ℝ is measurable, f(0^+) exists, |f(t) − f(0^+)| ≤ Ct on (0,1], and |f(t)| ≤ Ct^{−1} on [1,∞).

**Statement.** J(ε) = ∫_0^∞t^{−1−ε}[f(t) − f(0^+)]dt (absolutely convergent for 0 < ε < 1) and
K(ε) = ∫_0^∞t^{−1−ε}f(t)dt (absolutely convergent for −1 < ε < 0) are restrictions of the single function
∫_0^1t^{−1−ε}[f − f(0^+)] + ∫_1^∞t^{−1−ε}f − f(0^+)/ε, which is analytic on (−1,1)∖{0}.

*Proof.* Split both integrals at t = 1 and use ∫_1^∞t^{−1−ε} = 1/ε (ε > 0) and ∫_0^1t^{−1−ε} = −1/ε (ε < 0). ∎

If the constants C = C(ξ) depend on an outer parameter ξ and ∫dξ C(ξ)w(ξ) < ∞ for the outer weight w, the lemma passes
under the ξ-integral by dominated convergence. This weaker requirement (integrable rather than uniform constants) is
what Prop C.4(e3) uses (Fix 7(a)).

---
## 4. Part B — The one-loop off-shell triangle (M1)

**Notation.**
- Denominators, each with −i0: D_g = −k², D_1 = −(p_1−k)², D_2 = −(p_2+k)²; Γ = 1/(D_gD_1D_2).
- e_1 = m² + 2Pk^-, h_1 = 2Pk^-, t_1 = 2Pk^- − k²; e_2 = m² + 2P′k^+, h_2 = 2P′k^+, t_2 = 2P′k^+ − k².
- D_1 = e_1 − (m²/P)k^+ + D_g, D_2 = e_2 − (m²/P′)k^- + D_g, and h_i − t_i = k² = −D_g.
- Approximators: T_S:(D_1,D_2)→(e_1,e_2); T_{C_1}: D_2→h_2; T_{C_2}: D_1→h_1; T_H:(D_1,D_2)→(t_1,t_2). Each also acts on
  already approximated denominators (T_He_i = h_i, T_St_i = h_i, T_{C_1}e_2 = h_2, …).
- Region set 𝓡 = {S < C_1, C_2 < H}. On each quark line the approximations form the semilattice {1,e,t,h}, so (Com) and
  (Abs) hold exactly.
- Collins terms (`prop:appN-triangle-exact`(a)):
  - C_SΓ = 1/(D_ge_1e_2);
  - C_{C_1}Γ = (1/(D_gh_2))(1/D_1 − 1/e_1) = (e_1−D_1)/(D_gh_2D_1e_1), with e_1 − D_1 = (m²/P)k^+ + k²;
  - C_{C_2}Γ is the mirror image;
  - C_HΓ = (1/D_g)(1/t_1−1/h_1)(1/t_2−1/h_2) = D_g/(t_1h_1t_2h_2).
- Fibered variables: x = k^+, κ = k_T², u = x/P, e_2 = m²+2P′x, h_2 = 2P′x, A = xm²(1−u)+Pκ, B = xm²+Pκ, a = m²/P′,
  w = 2x+a.

### Proposition B.1 (fibered densities) — [R, R_PT] [rev]

With the normalization μ^{2ε}∫d^dk/(iπ^{d/2})F = (μ^{2ε}/Γ(1−ε))∫dx dκ κ^{−ε}ρ_F:

- ρ_Γ = 1/(AD̂_2) for 0 < x < P, with D̂_2 = e_2[1 + m²/Q̃² + κ/(Q̃²(1−u))] + κ.
- On the sliver −a/2 < x < 0, ρ_Γ = 2/(wD_gD_1) at k^- = P′ + κ/w.
- ρ_Γ = 0 elsewhere.
- ρ_{C_S} = 1/(Be_2) for x > 0.
- ρ_{C_{C_1}} = xm²/(Q̃²AB) for 0 < x < P, and −1/(h_2B) for x > P.
- ρ_{C_{C_2}} = −1/(Pe_2(e_2+κ)) for x > 0, and w/(P[(a−w)P′w + aκ](P′w+κ)) on the sliver.
- ρ_{C_H} = −x/(P(h_2+κ)(h_2(P−x)+Pκ)) for 0 < x < P, and 1/(P(h_2+κ)h_2) for x > P.
- ρ_{C_S}, ρ_{C_{C_1}} and ρ_{C_H} vanish on the sliver.

**Proof.**
- Close the k^- contour; each term decays like |k^-|^{−2}.
- For 0 < x < P the contour picks up the D_1 pole; on the sliver, the D_2 pole. In the normalization above,
  ρ = 2·Res at the D_1 pole (0 < x < P) and ρ = −2·Res at the D_2 pole (sliver). Every density part has a single residue.
- Every C_R satisfies (FR).

**Checks.**
- Symbolic residues (`t1`); the engine `lcpt.py` at 2000 points, maximum deviation 3·10⁻¹⁰ (`t7`); direct k^- integration
  at η = 10⁻⁷.
- Independent residue codes of reviews r1_2, r2_2 (maximum deviation 3.5·10⁻²¹) and r3_2. The final review re-derived the
  residues at general P, P′ with sympy (main = 1/(AD̂_2), sliver = 2/(wD_gD_1) at k^- = P′+κ/w).
- In the normalization du dκ with P = P′ = 1/√2, the densities are those of the certificate archives. Both archive
  verifiers check them; `f2_archive_verify.py` does so as exact identities.

**(CS3^φ).**
- ρ_Γ ≥ 0, and ∫ρ_Γ is finite uniformly in ε ∈ [0,ε_0]; the κ-integral is explicit (proof of Prop B.3).
- Each ρ_{C_R} is in L¹ exactly for 0 < ε < 1. The UV needs ε > 0; the endpoint x → P needs ε < 1.
- Every part of every ρ_{C_R} has a definite sign. Its absolute integral is given by the same κ-formulas K1, K2 and by
  Beta integrals of J0+J1 type, whereas the signed integrals involve J0−J1.

The closed forms are known (`prop:appN-triangle-exact`); this is an independent verification.

### Proposition B.2 (exact identification of the four Collins terms) — [R, R_PT] [rev]

For 0 < ε < 1 and all P, P′, m² > 0 (μ = 1), the fibered value equals the covariant value, and both equal:

- C_S = Γ(ε)²Γ(1−ε)(Q̃²/m⁴)^ε/Q̃²;
- C_{C_1} = C_{C_2} = Γ(ε)Γ(−ε)Γ(1−ε)Γ(1−2ε)^{−1}(m²)^{−ε}/Q̃² = −Γ(1+ε)Γ(1−ε)²(ε²Γ(1−2ε))^{−1}(m²)^{−ε}/Q̃²;
- C_H = Γ(1+ε)Γ(1−ε)²(ε²Γ(1−2ε))^{−1}(Q̃²)^{−ε}/Q̃².

As ε → 0, Σ_R C_R → (L̃² + π²/3)/Q̃².

**Proof, fibered side.** Let g = Γ(ε)Γ(1−ε).
- κ-integrals: K1(α) = ∫_0^∞dκ κ^{−ε}/(κ+α) = gα^{−ε} and K2(α,β) = ∫_0^∞dκ κ^{−ε}/((κ+α)(κ+β)) =
  g(α^{−ε}−β^{−ε})/(β−α).
- x-integrals:
  - J0 = ∫_0^1du u^{−1−ε}[(1−u)^{−ε}−1] = B(−ε,1−ε) + 1/ε, convergent for ε < 1;
  - J1 = ∫_1^∞u^{−1−ε}du = 1/ε;
  - ∫_0^∞s^{−ε}(1+s)^{−1}ds = g.
- *C_{C_1}.*
  - For 0 < x < P, ρ = xm²/(Q̃²P²(κ+um²)(κ+um²(1−u))). By K2 it integrates in κ to g(um²)^{−ε}[(1−u)^{−ε}−1]/(Q̃²Pu).
  - With dx = Pdu, the region 0 < u < 1 gives g(m²)^{−ε}J0/Q̃².
  - For x > P, ρ = −1/(Q̃²uP(κ+um²)), which gives −g(m²)^{−ε}J1/Q̃².
  - With the factor 1/Γ(1−ε), C_{C_1} = Γ(ε)(m²)^{−ε}(J0−J1)/Q̃² = Γ(ε)B(−ε,1−ε)(m²)^{−ε}/Q̃².
- *C_{C_2}.*
  - The x > 0 part, −1/(Pe_2(e_2+κ)), gives −g(m²)^{−ε}J1/Q̃².
  - On the sliver put u′ = w/a ∈ (0,1). Then P′w = m²u′ and (a−w)P′w/a = m²u′(1−u′), and by K2 the κ-integral is
    g(m²u′)^{−ε}[(1−u′)^{−ε}−1]/(Pm²u′).
  - With dx = (m²/2P′)du′ the sliver gives g(m²)^{−ε}J0/Q̃². Hence C_{C_2} = C_{C_1}.
- *C_S.* K1 gives g(um²)^{−ε}/(P(m²+Q̃²u)). The substitution u = m²s/Q̃² gives C_S = g²(m²)^{−2ε}(Q̃²)^ε/(Γ(1−ε)Q̃²).
- *C_H.*
  - For 0 < x < P, with h_2 = Q̃²u, K2(h_2, h_2(1−u)) gives −g(Q̃²)^{−1−ε}J0.
  - For x > P, K1 gives g(Q̃²)^{−1−ε}J1.
  - Hence C_H = −Γ(ε)B(−ε,1−ε)(Q̃²)^{−1−ε}.
- Finally use Γ(ε)Γ(−ε) = −Γ(1+ε)Γ(1−ε)/ε².

**Proof, covariant side** (whole integrand; §1.4). The l-integrals use ∫d^dl/(iπ^{d/2})(−l²+Δ)^{−n} =
Γ(n−d/2)Γ(n)^{−1}Δ^{d/2−n} and the corresponding formula for l²/(−l²+Δ)^n.
- *C_S* = 1/(D_ge_1e_2).
  - Cheng–Wu: 1/(D_ge_1e_2) = 2∫_0^∞∫_0^∞dλ_1dλ_2[D_g+λ_1e_1+λ_2e_2]^{−3}.
  - Here D_g+λ_1e_1+λ_2e_2 = −(k−v)² + Δ, with v = (λ_1P, λ_2P′, 0) and Δ = λ_1λ_2Q̃² + m²(λ_1+λ_2).
  - So C_S = Γ(1+ε)∫∫(λ_1λ_2Q̃²+m²(λ_1+λ_2))^{−1−ε}. The λ_2-integral is (m²λ_1)^{−ε}/(ε(λ_1Q̃²+m²)), and the
    λ_1-integral gives the closed form.
- *C_{C_1}* = (e_1−D_1)/(D_gh_2D_1e_1).
  - Use 6∫_0^1dx∫∫dλ_1dλ_2[xD_1+(1−x)D_g+λ_1h_2+λ_2e_1]^{−4}.
  - The combined denominator is −(k−v)² + Δ, with v^+ = P(x+λ_2), v^- = λ_1P′ − xm²/2P and Δ = (x+λ_2)(m²(1−x)+Q̃²λ_1).
  - The even part of the numerator after the shift is l² + (m²/P)v^+ + v² = l² + Δ.
  - The l-integral is Γ(1+ε)(2ε−1)Δ^{−1−ε}.
  - Then ∫dλ_2 gives x^{−ε}/ε, ∫dλ_1 gives (m²(1−x))^{−ε}/(εQ̃²), and ∫dx gives B(1−ε,1−ε).
  - So C_{C_1} = Γ(1+ε)(2ε−1)B(1−ε,1−ε)(m²)^{−ε}/(ε²Q̃²), which equals the closed form.
- *C_{C_2}*: exchange 1↔2.
- *C_H* = D_g/(t_1h_1t_2h_2).
  - Use the Feynman parameter x between t_1 and t_2, and Cheng–Wu parameters λ_1 for h_1 and λ_2 for h_2.
  - Then Δ = Q̃²(x+λ_1)(1−x+λ_2), and the even part of the numerator is −l² − Δ.
  - The l-integral is Γ(1+ε)(1−2ε)Δ^{−1−ε}, which leads to Γ(1+ε)(1−2ε)B(1−ε,1−ε)(Q̃²)^{−1−ε}/ε².
- All parameter integrals converge absolutely for 0 < ε < 1. No scaleless-term convention is used. ∎

**Checks.**
- `r2_triangle_identification.py`, PARTS A–C (sympy); PART D: direct 2D fibered quadrature without the κ-formula,
  relative agreement 10⁻⁷–10⁻⁵.
- Independent re-derivations: review r2_1 (36–61 digits), review r2_2 (sympy), review r3_1, review r3_2 (2D quadrature,
  3·10⁻¹¹–5·10⁻⁷), and the final review (closed forms re-checked; ε → 0 sum L̃²+π²/3).

**Remarks.**
- In the covariant decomposition C_H = [massless on-shell triangle] − 1/(D_gt_1h_2) − 1/(D_gh_1t_2) + 1/(D_gh_1h_2), the
  last term is exactly boost invariant with zero ε-weight. DR does not regulate it; only the whole C_H has a value.
- **Withdrawn** (round 2): the wording "massless on-shell triangle plus scaleless terms".

**Positioning.** The four closed forms are the known region values of the off-shell triangle: hard, collinear and
ultrasoft regions (Smirnov, *Applied asymptotic expansions* (2002); Belitsky–Bork–Smirnov 2025; Belitsky–Smirnov 2026,
App. A.1, eqs. (A.1)–(A.3), in their normalization T_11^h, T_11^{c_i}, T_11^{us}). They coincide with ours up to the
factor e^{εγ_E}: Γ(−ε)²Γ(1+ε)/Γ(1−2ε), Γ(−ε)²Γ(ε)/(2Γ(−2ε)) and Γ(1−ε)Γ(ε)² (final review). **New**, and the only part of
the triangle identification kept as new (Fix 3), is the *fibered-side* identification of the Collins terms that contain
**zero-bin subtractions** (e.g. C_{C_1} = T_{C_1}Γ − T_{C_1}T_SΓ). Their absolutely convergent k^--residue integrals
reproduce these values exactly, without any convention for scaleless integrals.

### Proposition B.3 (exact identification for Γ) — [R, R_PT] [rev-1: final review]; 「本书给出的推导」

For every ε ∈ (−1,1), the fibered value of Γ equals its covariant value
I_Γ = Γ(1+ε)∫_simplex F^{−1−ε}, F = x_gm²(x_1+x_2) + x_1x_2Q².

More precisely, let u = x_1 − τx_2 (τ = m²/Q̃², units Q̃ = 1; this is the light-cone variable k^+/P of the
α-representation). Then:
- the main part 0 < k^+ < P equals the covariant integral over {x_1 > τx_2};
- the sliver equals the covariant integral over {x_1 < τx_2}.

**Proof.**
1. *Main part.* Prop B.1 gives ρ_Γ = (1−u)/[P(1+τ)(κ+u(1−u)m²)(κ+(1−u)(m²+u))], 0 < u < 1. Use a Feynman parameter y and
   ∫_0^∞dκ κ^{−ε}(κ+C)^{−2} = Γ(1−ε)Γ(1+ε)C^{−1−ε}; Tonelli applies, since all integrands are positive. This gives
   fib_main = Γ(1+ε)(1+τ)^{−1}∫_0^1du∫_0^1dy (1−u)^{−ε}[m²(1−y+yu) + (1−y)u]^{−1−ε}.
2. On {x_1 > τx_2} substitute x_2 = (1−u)z/(1+τ), x_1 = u + τx_2 (Jacobian (1−u)/(1+τ)). Then x_g = (1−u)(1−z) and
   F = (1−u)[m²(u+(1−u)z) + zu]. With z = 1−y the two integrals coincide.
3. *Sliver.* Prop B.1 gives, with s = w/a ∈ (0,1), ρ_Γ = (2s/(2P(1+τ)))/[(κ+m²s(1−s))(κ+m²s(1+τ(1−s)))]. The same steps
   give fib_sl = Γ(1+ε)τ(1+τ)^{−1}m^{−2−2ε}∫ds dy s^{−ε}[1 − ys + τ(1−y)(1−s)]^{−1−ε}.
4. On {x_1 < τx_2} substitute x_1 = τsv/(1+τ), x_2 = 1 − s + sv/(1+τ) (Jacobian τs/(1+τ)). Then x_g = s(1−v),
   F = τs[1 − s(1−v) + τv(1−s)], and x_1 < τx_2 ⟺ s < 1. With y = 1−v and m² = τ the two integrals coincide.
5. All integrals converge absolutely for −1 < ε < 1. ∎

**Checks.**
- `r3_FI_exact.py`, part (1): every algebraic step in sympy — the two maps, Jacobians and F-factorizations, and the
  closed-form densities in (u,κ) and (s,κ) re-derived from Prop B.1.
- Part (2): direct quadratures. The fibered total 15.5610705037585 at (P,P′,m²,ε) = (0.8,1.3,0.1,0.3) equals the
  covariant value of reviews r2_1 and r3_2 (relative 3·10⁻¹⁷). The quadratures of the two simplex sub-regions need
  breakpoints at both soft corners; with them they agree with the fibered main and sliver parts to 7·10⁻⁹ and 5·10⁻⁸, and
  to 1·10⁻¹¹ and 2·10⁻¹⁰ at (0.8,1.3,0.02,0.05).
- *Independent confirmation (final review, `review_final_scripts/chk_B3.py`)*. The reviewer re-derived both maps and the
  κ-integrals by hand. With their own residues and their own simplex quadrature:
  - (P,P′,m²,ε) = (0.8,1.3,0.1,0.3): main 13.396394159814183728 on both sides (rel 5·10⁻²⁵), sliver 2.164676343944342866
    (rel 3·10⁻²²);
  - (0.5,0.9,0.02,−0.4): main 5.0789343503040503353 (rel 3·10⁻²⁶), sliver 0.3265132115884442963 (rel 1·10⁻²⁶).

**Positioning (final-review Fix 3; LA-3).**
- For Γ this is an explicit instance of the known equivalence of light-front (light-cone-ordered) and covariant
  perturbation theory for scalar graphs (Chang–Yan 1973; Ligterink–Bakker 1995). The general statement is (LCE).
- The main part 0 < k^+ < P is the valence ordering. The sliver −m²/2P′ < k^+ < 0 is the **non-valence** (k^+ < 0)
  ordering, in which the exchanged φ carries negative plus momentum. It exists because p_2 has the non-zero plus
  component m²/2P′.
- Prop B.3 is a self-contained derivation for this graph: the two orderings are mapped exactly onto the two simplex
  sub-regions. In print it is 「本书给出的推导」, **not** a new result.

**Consequence.** (FI) holds for Γ and, by Prop B.2, for all four C_RΓ: every value in Thm A.1(iii) is identified for the
triangle. Lemma A.2, with its unproven (IL1) and (IL3), is not needed. **Withdrawn:** the round-2 premise "(ID)_Γ" of
the integrated corollary — mathematically. For print it stays until the second confirmation (Cor B.6).

### Proposition B.4 (the negative-k^+ sliver) — [R] [rev]

The region is −m²/2P′ < k^+ < 0, at ε = 0, in the routing and fibration of Prop B.1.
- ∫_{sliver}ρ_{C_{C_2}} = ζ_2/Q̃² **exactly**, to all orders in m. Indeed ∫dκ ρ_{C_{C_2}} = ln(a/(a−w))/(PP′w), and
  (1/2PP′)∫_0^1du′(−ln(1−u′))/u′ = Li_2(1)/Q̃².
- ∫_{sliver}ρ_Γ = ζ_2/Q̃² + O(m²/Q̃⁴). This is half of the π²/3 in the sum of the Collins terms.
- ∫_{sliver}r = −2m²/Q̃⁴ + o(m²), half of the total −4m²/Q̃⁴. On the sliver ρ_r = ρ_Γ − ρ_{C_{C_2}} =
  (2/(wD_g))(1/D_1 − 1/h_1) = −(2/(wD_g))(m²(1+c/2P) + D_g)/(D_1h_1), with c = a − w. Its two negative terms each
  integrate to −m²/Q̃⁴ + o(m²).
- For ε > 0 the weight κ^{−ε} changes these values. In another routing or fibration the sliver is not a separate base
  region.
- Numerics:
  - ∫ρ_Γ(sliver) = 1.644934 at λ² = 10⁻⁶; the sliver remainder is −1.99979λ² (λ² = 10⁻⁴) and −2.00000λ² (λ² = 10⁻⁶)
    (`t2b`; reproduced by review r1_2);
  - final review, own code: ∫_sl ρ_{C_{C_2}} − ζ_2 = 4·10⁻³¹ at m² = 10⁻³ and 10⁻⁵; ∫_sl ρ_Γ − ζ_2 = −2.0·10⁻³ and
    −2.0·10⁻⁵; ∫_sl r/m² = −1.99786 and −1.99998.
- Exact LP certificates of the sliver give λ² at ε = 0 and λ^{9/5} at ε_0 = 1/10, with recession slopes −1/2 and −9/20.
- New, elementary.

### Theorem B.5 ((CS1^φ)–(CS3^φ) for the triangle on the natural cover) — [R, R_PT], computer-assisted [rev]; lower-bound remark changed in final2 [new-final2]

**Cover** (Q̃ = 1, P = P′ = 1/√2, u = k^+/P, κ = k_T², s = λ² = m²):
- U_S = {0 < u ≤ s, κ ≤ us};
- U_{C_1} = {s < u ≤ 1, κ ≤ us} ∪ {1 < u ≤ 2, κ ≤ s};
- U_{C_2} = {0 < u ≤ s, us < κ ≤ u} ∪ sliver;
- U_H = the complement, which contains every UV direction and, at s = λ², the interior of the Sudakov diamond.

**Statement.**
- (i) At ε = 0 every (CS1)/(CS2) item is ≤ Cλ²L^{≤2}. The items are:
  - on U_S: (1−T_S)Γ, C_{C_1}, C_{C_2}, C_H (C_H is λ⁴);
  - on U_{C_1}: (1−T_{C_1})X_{C_1}, C_{C_2}, C_H;
  - on U_{C_2}: (1−T_{C_2})X_{C_2}, C_{C_1}, C_H;
  - on U_H: r.
- (ii) For ε ∈ (0,1/10] every item is ≤ C(λ²L² + λ^{8/5}), uniformly. The exact certificates at ε_0 = 1/10 give the
  exponents 8/5 and 9/5; uniformity follows from κ^{−ε} ≤ 1 + κ^{−ε_0} and the convexity in ε of the LP value.
- (iii) (CS3^φ) holds (Prop B.1). (FR) holds for Γ and every C_RΓ.
- Fibered conclusion (Thm A.1(i),(ii)): ∫|ρ_r|dμ_ε ≤ Cλ²L² at ε = 0, and ≤ C(λ²L² + λ^{8/5}) uniformly on (0,1/10].

**Evidence.**
- Exact primal–dual optimal pairs; exact recession checks (maximal slope −1/2 at ε = 0 and −9/20 at ε_0).
- Frozen variables are coefficients; comparability constants ≤ 2^{deg}, and ≤ (15/7)^{deg} on the sliver.
- The global remainder cells r_I, r_II, r_III and the sliver sub-domains A/B are certified at λ². At θ = 2 the item
  (CS1)_H coincides with the global remainder certificate.
- 58 piece records and 546 monomial certificates, regenerated self-contained (`r3_triangle_recert.py`).
- Re-verified twice by independent code:
  - `r3_archive_verify.py` (re-run by the final review);
  - `f2_archive_verify.py` (final2), with exact closed-form identities (constant c = 1 for all 58 records) and exact
    coverage. Every item cell contains its target U_R ∩ strip at θ = 2 and θ = 1; the remainder cells cover the base;
    the sliver frozen range [7/10, 3/2] contains [1/√2, √2].
- Exact face bounds 0, 1, 2 for 251, 207, 88 certificates. The L-power L^{≤2} is the trivial bound for two-dimensional
  cells.

**Optimality of the λ-exponent.**
- *(a) Within the cover family s = λ^θ, θ ∈ (0,2].* The certified exponent is θ (exactly for θ = 1, 3/2, 19/10, 2).
  - *Lower bound (corrected; final-review Fix 9).* On U_S, x = Pu, A = xm²(1−u)+Pκ and B = xm²+Pκ. The final report
    wrote "∫_{U_S}ρ_{C_{C_1}} ≥ s/4, since both A and B are ≤ 2um² on U_S". The bound A, B ≤ 2um² holds only at θ = 2
    (s = m²). For θ < 2 one only has A, B ≤ Pu(m² + s) ≤ 2Pus, hence ρ_{C_{C_1}} = xm²/(AB) ≥ m²/(4Pus²) and
    ∫_{U_S}ρ_{C_{C_1}} ≥ ∫_0^s P du·us·m²/(4Pus²) = m²/4 = **λ²/4**. This suffices for the conclusion: every cover in
    the family has an item ≥ λ²/4, so none has a better item exponent than 2, which θ = 2 attains.
  - *Sharper bound (new in final2).* Since A ≤ B, ρ_{C_{C_1}} ≥ xm²/B² = um²/(P(um²+κ)²). Exactly,
    ∫_0^{us}dκ um²/(P(um²+κ)²) = (1/P)[1 − m²/(m²+s)] = s/(P(m²+s)), and ∫_0^s P du·s/(P(m²+s)) = s²/(s+m²). Hence

    ∫_{U_S}ρ_{C_{C_1}} ≥ s²/(s+m²) ≥ s/2 for every θ ∈ (0,2] (s ≥ m²).

    So the inequality "≥ s/4" of the final report is in fact true on the whole family, but for this reason, not the one
    given. It also shows that the certified exponent θ is attained, i.e. sharp, for every cover of the family.
    Numerically (`f2_C4e3_checks.py`, part (C)):
    - θ = 1, 1.5, 2 at λ² = 10⁻⁴: ∫_{U_S}ρ_{C_{C_1}}/λ² = 99.26, 9.093, 0.5000, against the bound s²/((s+m²)λ²) =
      99.01, 9.091, 0.5000;
    - θ = 1, 1.5, 2 at λ² = 10⁻⁶: 999.3, 30.654, 0.5000, against the bound 999.0, 30.653, 0.5000.
  - The (CS1)_{C_1} norm is ≈ (θ/2)sL for θ < 2, and 1.36, 1.41, 1.43, 1.44 sL at θ = 2 for λ² = 10⁻⁴…10⁻¹⁰
    (`r1_theta2_lower.py`).
- *(b) Among all covers (cover-independent optimality; new in final2, the final review's suggestion [14]).* Let {U_R} be
  any finite measurable cover of B and take the items on it as in (i).
  - By (A.1), on U_{R_0} one has pointwise |ρ_r| ≤ |ρ_{(1−T_{R_0})X_{R_0}}| + Σ_{R≰R_0}|ρ_{C_RΓ}|, hence
    ∫_B|ρ_r|dμ_0 ≤ Σ(all items).
  - The bounds of Thm B.5 at ε = 0 and at ε_0 make |ρ_r|(1+κ^{−ε_0}) integrable. So, by dominated convergence and
    Thm A.1(ii),
    ∫_Bρ_r dμ_0 = lim_{ε→0+}∫_Bρ_r dμ_ε = lim_{ε→0+}(I_Γ − Σ_RI_{C_RΓ}).
  - The last step uses (FI) from Props B.2 and B.3. The limit equals Φ^(1)(t,t)/Q² − (L̃² + π²/3) = −4λ²(1 + O(λ²L̃²))
    (Prop B.7).
  - Hence, for **every** cover, Σ(items) ≥ |∫_Bρ_r dμ_0| = 4λ²(1+o(1)), and the largest item is
    ≥ 4λ²(1+o(1))/(|𝓡|(1+|𝓡|)). No cover beats the exponent 2.
  - This argument uses Prop B.3 ([rev-1]). Without it, the same conclusion follows from the direct fibered evaluation of
    ∫ρ_r at ε = 0 (Prop B.7, numerics `t2b`), but only as [P].

**Relation to App. N.** The fat neighbourhoods λ^β (β < 1, β_S < β_C) of `def:method-neighbourhoods` and
`lem:appN-beta` are sufficient-condition choices of the general envelope argument. For the triangle, natural-scale covers
give the optimal exponent once the grouped objects are computed explicitly. This is a sharpening, not an error
correction.

New: the integral-norm verification of (CS1)–(CS3) for this graph, with exponent 2. The exponent is optimal within the
cover family, and — given Prop B.3 — among all covers.

### Corollary B.6 (the integrated subtraction theorem for the triangle) — implication [R, R_PT], computer-assisted; **printed as [R, R_cond: (FI)_Γ] until Prop B.3 has its second confirmation** (Fix 2)

Uniformly in ε ∈ (0,1/10]:
- |I_Γ − Σ_{R∈𝓡}I_{C_RΓ}| ≤ ∫|ρ_r|dμ_ε ≤ C(λ²L² + λ^{8/5});
- each I_{C_RΓ} converges absolutely and equals the closed form of Prop B.2.

*Proof.* Thm B.5, Thm A.1(iii), and (FI) for all terms (Props B.2, B.3). ∎

**Grade for print.** Mathematically the corollary is [R, R_PT] (computer-assisted) once Prop B.3 is accepted. Prop B.3
has **one** independent confirmation recorded (the final review, `review_final_scripts/chk_B3.log`). The PASS rule
requires two (§0). Until the LA-3 confirmation stage records the second, the integrator prints the corollary as
[R, R_cond] with the premise "(FI)_Γ: the fibered value of Γ equals I_Γ, ε ∈ (−1,1)". This is the form of
`prop:appN-triangle-cs`(c) in FINAL_OUTLINE_v2. The numerical agreement (10⁻¹⁷–10⁻²⁸ in `r3_FI_exact.py`; 10⁻²⁵ in the
final review) may be quoted as evidence [P]. After the second confirmation, (c) becomes unconditional with the status
sentence of §11.

In round 2 this corollary was [R, R_cond] with the single premise (ID)_Γ. Together with the exact NLP remainder of
Prop B.7 it is the content of slot X2a (§11).

### Proposition B.7 (remainder: norm versus integral) — [rev] (r2_2, r3_1 for the numbers; final review: CORRECT)

- **Rigorous:** ∫|ρ_r| ≤ Cλ²L² at ε = 0 (Thm B.5).
- **Exact integrated remainder** (known; reproduced). In units Q̃ = 1, ρt = m² exactly, so:
  - ∫r = Φ^(1)(t,t)/Q² − (L̃²+π²/3) = 4Li_2(−m²)/(1−m⁴) + (L̃²+π²/3)m⁴/(1−m⁴) = −4λ² + O(λ⁴L̃²); with ρt = m² and
    λ = (1−m²)/(1+m²), Φ^(1)(t,t)/Q² = [4Li_2(−m²) + L̃² + π²/3]/(1−m⁴) (final review);
  - equivalently, in Q units: −4m²/Q⁴ + (m⁴/Q⁶)(L_Q² − 15 + π²/3) + O(m⁶L²/Q⁸);
  - the residual is ≈ 4.7, 5.2, 5.4 × m⁶L² for m² = 10⁻³…10⁻⁵ (reviews r2_2, r3_1);
  - the fibered integral matches Usyukina–Davydychev to 10⁻¹¹ (`t2b`). By Props B.2–B.3, the subtracted L̃²+π²/3 is the
    sum of the identified Collins terms.
- **Numerical [P]:**
  - ∫|ρ_r| = c(λ)λ²L with c = 3.53, 3.79, 3.89, 3.93, 3.95, 3.96, 3.962 for λ² = 10⁻²…10⁻⁸, and 91.41525λ² at λ² = 10⁻¹⁰
    (review r1_1); hence ∫|ρ_r| ≈ λ²(4L̃ − c′) with c′ → 0.69, one logarithm more than the integrated remainder;
  - sign structure: soft box −1.04L, C_1 strip −0.54L, k^+ > P strip +0.95L, hard part +0.48L (`t2c`). The monomial
    majorant is sharp to a factor 1.1–1.3 (`t3`).
- A Table-5-type comparison of I with L²+π²/3 in Q² tests the leading power of the exact integral, not the Collins
  remainder in Q̃ (ERR-m25).

### Theorem B.8 (log-weighted triangle family) — [R, R_PT], computer-assisted, for each fixed j [rev]

**Integrand family.**
- Γ^(j) = ln^j(D_g/μ²)/(D_gD_1D_2), μ = Q̃, j = 0, 1, 2, …
- Hybrid scheme: outer measure d = 4−2ε with the fixed four-dimensional weight ln^j(D_g).
- The family weights the triangle with a power of the logarithm of the exchanged line's virtuality. It *models* the
  insertion structure of a large-β_0 bubble chain in a theory whose self-energy is ∝k²ln k² (the transverse gauge vacuum
  polarization, or φ³₆), grafted onto the (M1) triangle.
- **It is not a graph class of (M1).** In (M1), [g²] = mass² and Π_R(k²) = (g²/16π²)(c − ln(−k²/μ²)) carries no factor
  k². So the MS-bar renormalized j-bubble chain is ∝ g^{2j}[c − ln(−k²/μ²)]^j/(−k²)^{j+1}, which is IR divergent at fixed
  m for j ≥ 1 (Prop A.6(b)). Its d-dimensional form is ∝ g^{2j}(−k²)^{−1−j(1+ε)}×(poles), not (−k²)^{−jε}×(poles).

**Lemma B.8.1** (mathematics; R_def-type). The approximators act only on D_1, D_2 and the external momenta, never on
D_g. Hence C_RΓ^(j) = ln^j(D_g)·C_RΓ pointwise, with the region set of the triangle.

**Four-shell representation** (0 < u < 1, v = 1−u, P = P′ = 1/√2).
- ρ_r^(j) = Σ_s l_s^jT_s, where l_s = ln D_g on the shell s ∈ {D, e, t, h}.
- The shells are R_D = (um²v+κ)/v, R_e = um²+κ, R_t = κ/v, R_h = κ.
- T_D = (v/D_G − 1/u)/(um²v+κ), T_e = m²/(u(m²+u)(um²+κ)), T_t = 1/(u(uv+κ)),
  T_h = 1/((m²+u)(m²+u+κ)) − 1/(u(u+κ)), with D_G = (m²+u)(v(1+m²)+κ) + κv.
- The k^- contour closes away from the ln D_g cut in every range.
- Σ_sT_s equals the triangle remainder density for 0 < u < 1, and T_e + T_h equals it for u > 1 (checked symbolically in
  `r3_archive_verify.py` and `f2_archive_verify.py`).

**Lemma B.8.2 (rectangle rule, exact; mathematics).**
- l_D − l_e − l_t + l_h = δ = ln(A/B), with |δ| ≤ min(u²m²/(um²v+κ), CL(1+|X|));
- a = l_e − l_h ∈ [0, min(um²/κ, CL)] and b = ln(1/v) ∈ [0, min(u/v, CL)];
- hence ρ^(j) = l_h^jρ_r^(0) + Σ_{n≥1}C(j,n)l_h^{j−n}[a^n(T_D+T_e) + b^n(T_D+T_t) + ((a+b+δ)^n−a^n−b^n)T_D].

**Single-shell structure.**
- On the sliver, Γ^(j) and C_{C_2}^(j) are both D_2-residues, so ρ_r^(j) = l_{sl}^jρ_r^(0) exactly.
- For 1 < u ≤ 2: C_S and C_{C_1} lie on the e shell, C_{C_2} and C_H on the h shell, and Γ = 0.
- Items. Each item density is l_ref^j·(the j = 0 item) plus log-difference corrections (l_a^j − l_b^j)·(rational), with
  |l_a^j − l_b^j| ≤ j(CL(1+|X|))^{j−1}min(ratio_ab, CL(1+|X|)). The shell forms are Γ = l_D^j r_G, C_S = l_e^j r_S,
  C_{C_1} = l_D^j a_1 − l_e^j a_2, C_{C_2} = l_h^j r_{C_2} and C_H = −l_t^j b_1 + l_h^j b_2 (checked exactly against
  Prop B.1 in `f2_archive_verify.py`).

**Theorem.** On the natural cover of Thm B.5, for each fixed j, every (CS1)/(CS2) item and ∫|ρ_r^(j)| satisfy:
- ≤ C_jλ²L^{j+2} at ε = 0;
- ≤ C_j(λ²+λ^{8/5})L^{j+2} uniformly on (0,1/10].

(CS3^φ) holds for 0 < ε < 1 in the hybrid sense: the logarithms do not affect convergence, but the individual C_R need
ε > 0.

**Evidence.**
- 2986 piece records and 70,373 exact monomial certificates (`r3_bubble_recert.py`).
- Re-verified by `r3_archive_verify.py`: all LP checks pass for all records, and 2938 closed-form identities pass
  (randomized test) for pieces P0–P4, the corner shells and the u > 1 pieces; the 48 composite "items" records were
  verified at the LP level only.
- Re-verified by `f2_archive_verify.py` (final2): all LP checks pass, and **all 2986** closed-form identities hold exactly
  with constant 1, including the 48 item records. Coverage is exact for region I (135 cells), region II (134 cells plus
  the corner), u > 1 (60 cells) and all item cells. The piece decompositions are complete.
- Remainder 0 < u < 1, 270 cells: minimum exponent 2 at ε = 0 and 8/5 at ε_0, with worst slopes −1/2 and −9/20. At ε_0,
  piece P3 uses the trivial alternative in 9 deep cells.
- Remainder u > 1, 60 cells: exponents 2 and 9/5, slopes −1/2 and −11/20.
- Items: 2 and 8/5.
- Corner {v ≤ λ⁶, κ ≤ λ⁸}: bounded shell by shell, ∫_{corner}|T_s| ≤ Cλ^{a_s}L^k with a_D = 8, a_e = 14, a_t = 8, a_h = 16
  (`t15f`); the archived corner minimum is 8 at ε = 0 and 36/5 at ε_0.
- Sliver and part III: the triangle certificates times |l|^j ≤ (C(1+L|X|))^j. Their cells are covered as in Thm B.5.
- Maximal face bound 2.

**Growth in j.** C_j ≳ 2j!/L_0^{j+2}: the u > 1 UV tail gives ∫_1^∞(ln κ)^jκ^{−2}dκ = j!. No statement about the summed
family is possible. The renormalon interpretation applies only within the large-β_0 analogy, not to (M1).

**Numerics [P]** (`t5`): ∫r^(j) ≈ −4λ²(−L)^j; at λ² = 10⁻¹⁰ the norms are 3.97λ²L (j = 0), 4.84λ²L² (j = 1) and 6.58λ²L³
(j = 2). The round-0 script `t15c` is invalid (its LPs are unbounded) and is not used.

**Withdrawn** (final round):
- the identification of Γ^(j) with the MS-bar renormalized bubble chain of (M1);
- "the true d-dimensional chain is (−k²)^{−nε} times poles";
- the renormalon reading for (M1);
- the entry "(F1) for the bubble-chain class" in the (M1) status list of Thm F.1;
- the round-1 "model assumption" that Γ^(j) reproduces the leading regions of the full (j+1)-loop graph of (M1), which is
  moot.

---
## 5. Part C — DIS forward amplitude in φ³₆ (M2)

### Proposition C.1 (all one-loop graphs of the forward amplitude) — (i)–(iii) [R, R_PT]; (iv) [R] outside the fibered framework [rev]

**Graph list.** With the current vertex Jψ*ψ and the coupling gψ*ψφ, the O(g²) graphs are:
- (i) 2 ladders: the rung φ(p−k), the spine ψ(k) twice, and the hard line ψ(k±q);
- (ii) 4 vertex corrections: φ exchanged between the target line and the hard line, at J_in or J_out, in the s or u
  channel;
- (iii) 2 hard-line self-energies;
- (iv) 4 J–φ mixing graphs: a ψ loop between one current and a φ of momentum q, which the target line absorbs;
- (v) 1 t-channel graph: a ψ loop carrying both currents, coupled to the target by a φ of zero momentum.

Tadpoles vanish in massless DR, and external self-energies are amputated.

**Definitions and scope.**
- Graph (v) is ∝1/t at t = 0, so it is infinite in the forward limit. It does not depend on x and has no discontinuity in
  ω. The forward amplitude is therefore *defined* modulo x-independent terms: the observable is the x-dependent part,
  equivalently the discontinuity. This removes (v).
- Graphs (iv) and (v) contain q^+ = 0 loops. These are pure zero modes in this frame; they violate (FR) and are treated
  outside the fibered framework. In (iv) the loop is a renormalized insertion Π_R(q²).
- In QCD the analogues of (iv) and (v) vanish by colour: a single gluon attached to a colour-singlet loop gives
  Tr t^a = 0.

**Statements.**
- (i) The collinear region is leading: Prop C.4 (the u channel is analogous, with A′ = 1+ξ/x ≥ 1).
- (ii), (iii) These graphs are UV divergent: ω = 0 for the vertex and ω = 2 for the self-energy. "(CS3) trivial"
  (round 0) is withdrawn.
  - Unrenormalized, (1−T_H)Γ = S(P)[f(m²)−f(0)] + [S(P)−S(P̂)]f(0) diverges at O(m²): ∫_{|l|<Λ}|ρ| = 25.4, 43.8, 62.2 m²
    for Λ = 10², 10⁴, 10⁶ (m² = 10⁻³).
  - *Renormalization.* Integrand-level BPHZ (`asm:appN-uv`) with subtraction points that match the plus components:
    - *Vertex.* Subtract the same graph at a fixed space-like point (p_0,q_0) with p_0^+ = p^+, q_0^+ = 0 and fixed
      invariants p_0² = −μ², q_0² = −Q_0², (p_0+q_0)². The integrated counterterm is a constant times the tree vertex.
      Because the fibered supports agree, the subtraction improves the UV behaviour pointwise, to ρ ~ |l|^{−6}.
    - *Self-energy.* After the shift l → l − zP_T the density is (1/π²)/(|l|² + z(1−z)s), with s = −P². Subtract its
      first-order Taylor polynomial in s at s_0. This is a Taylor expansion in P^- at fixed P^+ and P_T, with integrated
      counterterm Σ(s_0) + (s−s_0)Σ′(s_0). The result is g(s) = (c−c_0)²/(π²(a+c)(a+c_0)²), with c = z(1−z)s.
    - *Commutation.* T_H acts only on p (p → p̂ with p̂^+ = p^+ and P_T unchanged), and the subtraction point does not
      depend on p. Hence T_H∘R = R∘T_H.

**Theorem.** Write f(m²) = 1/(π²(1−z)vH), with v = zm² + |l|²/(1−z), H = A + v + 2l·q and A = 1 − z/x.
- *Vertex.* (1−T_H)RΓ = S(P)[f(m²)−f(0)] + [S(P)−S(P̂)][f(0)−f_0], and ∫|ρ| ≤ C(x)λ²L.
- *Self-energy.* ∫|g(s)/s² − g(ŝ)/ŝ²| ≤ C(x)λ², with ŝ = s − m² = Q²(1−1/x).
- (CS3^φ) holds uniformly in ε, and R = {H} suffices: the collinear region is power suppressed in φ³₆ for these graphs.

**Proofs.**
- *Vertex.*
  - From v_0H_0 − vH = −zm²(v_0+H): |f(m²)−f(0)| ≤ zm²/(|l|²HH_0) + zm²/(v|l|²H_0).
  - The first term integrates to O(zm²). The second integrates to O(zm²(1−z)[L + ln(1/(z(1−z)))]), using
    v ≥ max(zm², |l|²/(1−z)).
  - H, H_0 ≥ zc_x (Lemma C.3(i)), and the endpoint z → 0 is integrable.
  - |S(P)−S(P̂)| ≤ m²/(sŝ), and f(0) − f_0 ∈ L¹ (|l|^{−6} in the UV, |l|^{−2} in the IR).
- *Self-energy.* |∂_sg| integrates to ≤ Cz(1−z)(|s−s_0|/s_0 + (s−s_0)²/(ss_0)), and g(ŝ) ∈ L¹.
- *(iv).* These graphs depend on the target only through S(p+q). The remainder is exactly [S(P)−S(P̂)]D(q)Π_R(q²) = O(λ²).

**Numerics** (`r1_dis_Honly.py`; x = 2, μ² = 1, x_0 = 2):
- renormalized vertex norm 5.18, 6.32, 7.38, 8.43, 9.48, 10.53 m² for m² = 10⁻²…10⁻⁷, i.e. ≈ (0.46L+3.1)m², with
  definite sign and independent of the cutoff;
- self-energy norm 0.835 m² at m² = 10⁻² and 0.871 m² for m² ≤ 10⁻⁴. Review r2_2 reproduced 0.87123 m² analytically from
  Σ_R(s) = (1/6)[s ln(s/s_0) − s + s_0].

### Lemma C.2 (DIS ladders: light-cone representation and Collins structure) — [R] for the fibered densities [rev]; proof of (a),(b) rewritten in final2 (Fix 9) [new-final2]

**Setup.** The n-rung forward ladder is L_n = ∫Π_jd⁶k_j/(iπ³)·H_0(k_n)Π_jS(k_j)²R(k_{j−1}−k_j), with k_0 = p, in the
frame q^+ = 0 and x > 1. Here S, R and H_0 are the spine, rung and hard propagators.

**Statements.**
- (a) *Support.* The iterated k^- integrals (top-down, j = n, …, 1) vanish unless 0 < k_n^+ < … < k_1^+ < p^+.
- (b) *Rungs on shell.* On the support, close each k_j^- contour on the side of the single rung pole. This gives
  ρ_c = Π_i[π^{−2}(1−z_i)^{−1}(v_i^(c))^{−2}]H^(c_{n+1}), where:
  - c ∈ {0,1}^{n+1}; c_i = 1 means that the parent of level i is projected, and c_{n+1} = 1 means that the hard factor is
    projected;
  - v_i = z_i(1−c_i)v_{i−1} + |k_{iT} − (1−c_i)z_ik_{i−1,T}|²/(1−z_i), with v_0 = m²;
  - H^(0) = 1/(A + v_n + 2k_{nT}·q_T), H^(1) = 1/A, A = 1 − ξ_n/x.
- (c) *Invariants.* v ≥ ξm² + |K|²/(1−ξ) for unprojected chains, and v ≥ |K|²/(1−ξ) for all chains. This is
  Cauchy–Schwarz with weights z(1−ξ) and 1−z, which sum to 1−zξ. Hence H^(0) > 0.
- (d) The approximators T_{R_j} commute: T_{R_j} projects s_j in factor j+1, and T_{R_0} = T_H: p → p̂; π(s) depends only
  on ξ. Hence r = Σ_c(−1)^{|c|}ρ_c = U_0(s_0), with U_n(s) = h(s) − h(πs) and
  U_{j−1}(s) = κ(s→s′)U_j(s′) − κ(πs→s′_0)U_j(s′_0).

**Proof of (a), (b) (pole sides; corrected and completed in final2).** A factor (βk_j^- + a − i0w) has its pole in the
upper half plane iff w/β > 0.
1. *Coefficients and weights.* At the stage where k_j^- is integrated (after k_n^-, …, k_{j+1}^-), every factor still
   present is affine in k_j^- and of one of three types:
   - (α) the spine factors S(k_j), and H_0(k_n) if j = n: coefficient −2k_j^+, weight 1;
   - (β) a factor **propagated from a level l > j**, i.e. a factor of level l after the rung poles of the levels l, l−1, …,
     j+1 have been substituted: **coefficient −2k_l^+** (not −2k_j^+; final review [20]) and a weight w_l > 0. Indeed,
     substituting the rung pole of level i, k_i^- = k_{i−1}^- − |Δ_{iT}|²/(2Δ_i^+) + i0/(2Δ_i^+) with
     Δ_i^+ = k_{i−1}^+ − k_i^+, into a factor −2k_l^+k_i^- + a − i0w gives −2k_l^+k_{i−1}^- + a′ − i0(w + k_l^+/Δ_i^+).
     The weight therefore increases by k_l^+/Δ_i^+, which is positive in every non-vanishing case (step 3: k_l^+ and
     Δ_i^+ then have the same sign);
   - (γ) the rung R(k_{j−1}−k_j): coefficient +2(k_{j−1}^+ − k_j^+), weight 1.
2. *Sides.* The (α) poles lie on the side −sign(k_j^+), the (β) poles on the side −sign(k_l^+), and the rung pole on the
   side sign(k_{j−1}^+ − k_j^+).
3. *Induction on the common sign.* At level n there are no (β) factors. The integral vanishes, by closing the contour on
   the empty side (all integrands decay like |k^-|^{−2} or faster), unless the rung pole is alone on its side, i.e.
   unless sign(k_n^+) = sign(k_{n−1}^+ − k_n^+) =: σ. Then k_{n−1}^+ = k_n^+ + (k_{n−1}^+ − k_n^+) also has sign σ.
   Suppose that at level j all (α) and (β) factors have coefficients of sign −σ and positive weights, i.e. sign(k_j^+) =
   sign(k_l^+) = σ for the l > j involved. Then they all lie on the side −σ. The integral vanishes unless the rung pole
   lies on the side σ: sign(k_{j−1}^+ − k_j^+) = σ. In that case sign(k_{j−1}^+) = σ, and the weights propagated to level
   j−1 stay positive. In the non-vanishing case the contour is closed on the side σ and picks up only the **simple**
   rung pole; the double poles of S(k_j)² lie on the other side, so (FR) holds.
4. *The last level fixes σ.* At level 1 the rung is R(p − k_1) with k_0^+ = p^+ > 0. Non-vanishing requires
   sign(k_1^+) = sign(p^+ − k_1^+) = σ, hence sign(p^+) = σ, i.e. σ = +. Therefore the iterated integral vanishes unless
   0 < k_n^+ < k_{n−1}^+ < … < k_1^+ < p^+, which is (a). The boundary values of the k_j^+ are null sets.
5. Substituting the rung poles gives (b); (c) and (d) are algebra. ∎

(The final report's step 3 assumed k_{j−1}^+ > 0 at every level. That is true only after the induction has been closed at
level 1. The argument above makes the induction explicit, with the corrected coefficient −2k_l^+.)

**Validation.**
- n = 1: the fibered value equals the covariant value *exactly* (Prop C.4(e1)); numerically to 10⁻¹³ (`t6`).
- n = 2: the structure was checked numerically (`t11`).

The structure is known (`prop:appN-ladder`; Ex. D.48 of the source); it is made precise here.

### Lemma C.3 (hard-factor lemma) — mathematics [rev]

**Setup.**
- A parent state (ξ, K, v) with 0 < ξ ≤ 1 and v ≥ |K|²/(1−ξ).
- A child (z, l) ∈ (0,1)×ℝ⁴, with k = l + zK and v′ = zv + |l|²/(1−z).
- d = A(zξ) + v′ + 2k·q, with A(y) = 1 − y/x, |q| = 1 and c_x = 1 − 1/x.
- d̄ = A(zξ) + zv + |l|²/(1−z) + 2zK·q.

**Statement.**
- (i) d ≥ zξc_x > 0 in every direction of l.
- (ii) ⟨1/d⟩_{l̂∈S³} = 2/(d̄ + √(d̄² − 4|l|²)) ≤ 2/d̄ ≤ 2/(1 − z + zξc_x + |l|²/(1−z)).
- (iii) ⟨1/d²⟩_{S³} ≤ (2/d̄²)(1 + (d̄/(zξc_x))^{1/2}).
- (iv) ∫_0^1(1−z)⟨1/d⟩dz ≤ 2, uniformly in ξ.

**Proof.**
- (i) Cauchy–Schwarz with weights z(1−ξ) and 1−z gives the child invariant v′ ≥ |k|²/(1−zξ). Then
  min_r(r²/(1−zξ) − 2r) = −(1−zξ) gives d ≥ 1 − zξ/x − (1−zξ) = zξc_x.
- (ii) Use ∫_0^πsin²θ dθ/(a + b cos θ) = π(a − √(a²−b²))/b², with a = d̄ > |b| = 2|l| by (i). The bound on d̄ follows from
  v − 2|K| ≥ −(1−ξ).
- (iii) Differentiate (ii) with respect to a and use a² − b² ≥ a·d_min.
- (iv) Use (1−z)/(1−z+zξc_x) ≤ 1. ∎

The closed-form S³ average was checked by quadrature to 12 digits (`r1_ladder1_analytic.py`). For d = 6−2ε the S³
averages become S^{3−2ε} averages, ⟨1/(a+b cos θ)⟩ = (1/a)₂F₁(1/2,1;2−ε;b²/a²) = 2/(a+r)·₂F₁(1,ε;2−ε;(a−r)/(a+r)),
r = √(a²−b²). This was checked against direct quadrature in `r2_ladder1_identification.py`; the final review checked both
forms (e.g. 1.04300240082267 by three routes). The ε > 0 analogues of (ii)–(iv) are not proven.

### Proposition C.4 (one-rung DIS ladder) — (a)–(d) [R, R_PT] **at ε = 0 (d = 6)** [rev]; (e1) [R], 「本书给出的推导」 [rev-1]; (e2) [R] [rev]; (e3) fibered value [R] [rev-1], step-1 bound corrected [new-final2], whole-integrand parametric value [P]; (e4) [P]

**Hypotheses.** (M2), x ≥ x_0 > 1, Q = 1, λ = m ≤ c_x/8.

**Notation for (a)–(d)** (ε = 0).
- ρ_r(z,k) = κ_1(h_1−ĥ) − κ_0(h_0−ĥ), with k ∈ ℝ⁴ the transverse momentum.
- κ_1 = 1/(π²(1−z)v′²) with v′ = zm² + |k|²/(1−z); κ_0 is the same with v′_0 = |k|²/(1−z).
- h_1 = 1/(A+v′+2k·q), h_0 = 1/(A+v′_0+2k·q), ĥ = 1/A, A = 1 − z/x.
- σ := v′_0 and δ := zm² = v′ − v′_0, so d⁴k = π²(1−z)²σdσ after the angular average.
- All norms are ∫_0^1dz∫_{ℝ⁴}d⁴k|·|: the ε = 0 fibered measure of (M2), with the 1/π² inside the kernels. The constant
  c_1(x) refers to this measure.
- *Regions:* B = {σ ≤ δ} and A = {σ > δ}.

**Claims** (all at ε = 0).
- (a) ∫dz d⁴k|ρ_r| ≤ C(x)λ.
- (b) On the cover U_{R_1} = {v′ ≤ λ²}, U_H = complement, all items are ≤ C(x)λ.
- (c) (CS3^φ): ρ_Γ = κ_1h_1 ≥ 0 is integrable uniformly in ε (UV ~|k|^{−6}). ρ_{C_{R_1}} = κ_1ĥ and
  ρ_{C_H} = κ_0(h_0−ĥ) are integrable only for ε > 0 (logarithmic UV divergence).
- (d) ∫|ρ_r| = c_1(x)λ + O(λ²L), with c_1(x) = 4∫_0^1dξ ξ^{1/2}(1−ξ)^{3/2}/(1−ξ/x)². Values: c_1(2) = 1.262984,
  c_1(1.3) = 1.936673, c_1(5) = 0.924158 (re-checked by the final review). The coefficient was first derived in review
  r1_1.

**Proof of (a).**
1. *Positivity.* For |k| ≤ c_x/4, A + v − 2|k| ≥ c_x/2 for every v ≥ 0. For all k, A + v′_0 + 2k·q ≥ zc_x (Lemma C.3(i)).
2. *Region B.* Here |k| ≤ m/2, and |h − ĥ| = |v + 2k·q|/(A|A+v+2k·q|) ≤ (8/(7c_x²))(v + 2|k|). Integrating with
   d⁴k = π²(1−z)²σdσ:
   - ∫_Bκ_1|h_1−ĥ| ≤ c(1−z)[δ + (4/5)√((1−z)δ)];
   - ∫_Bκ_0|h_0−ĥ| ≤ c(1−z)[δ + 4√((1−z)δ)];
   with c = 8/(7c_x²).
3. *Region A.* ρ_r = (κ_1−κ_0)(h_1−ĥ) + κ_0(h_1−h_0), with
   - |κ_1−κ_0| = δ(2σ+δ)/(π²(1−z)σ²(σ+δ)²) ≤ 2δ/(π²(1−z)σ³);
   - |h_1−h_0| = δh_1h_0 ≤ δh_0².
4. On |k| ≤ c_x/4: |h−ĥ| ≤ (2/c_x²)(v+2|k|) and h_0 ≤ 2/c_x. The contribution is ≤ C[√δ + δ(L + ln(1/(z(1−z))))].
5. On |k| > c_x/4 the kernels depend only on |k|, so average over the direction of k. Lemma C.3 gives
   ⟨h_1⟩ ≤ 2/(c_x+σ) and ⟨h_0²⟩ ≤ (2/d̄²)(1 + (d̄/(zc_x))^{1/2}), with d̄ ≥ c_x + σ. The contribution is ≤ C(δ + δz^{−1/2}).
6. Integrating over z gives ∫|ρ_r| ≤ C(x)m. ∎

**Proof of (b).**
- (CS1)_{R_1} = κ_1(h_1−ĥ) on U_{R_1}, where |k| ≤ λ and |h_1−ĥ| ≤ c(λ²+2λ). Since ∫_{v′≤λ²}d⁴kκ_1 ≤ (1−z)ln(1/z), it is
  ≤ 3cλ(1−z)ln(1/z).
- (CS2)_{R_1} is C_H on U_{R_1}, ≤ c(1−z)(λ² + 4√(1−z)λ). Review r2_2 gives the slightly sharper
  c(1−z)[(1−z)m² + 4(1−z)m].
- (CS1)_H is r on U_H, bounded by (a). ∎

**Proof of (d).** Write ρ_r = odd + rest, with odd := −2k·q(κ_1−κ_0)/A².
1. *The odd part.* κ_1 − κ_0 depends only on |k| and is negative. Exactly,
   ∫d⁴k|k||κ_1−κ_0| = (1−z)^{3/2}∫_0^∞σ^{3/2}(σ^{−2} − (σ+δ)^{−2})dσ = (1−z)^{3/2}δ^{1/2}·3π/2.
   With ⟨|cos θ|⟩_{S³} = 4/(3π) and |q| = 1, ∫|odd| = ∫dz 4z^{1/2}(1−z)^{3/2}m/A² = c_1(x)λ, exactly.
2. *The rest on |k| ≤ c_x/4.* Here A + s ≥ c_x/2, with s = v + 2k·q. The exact identity h − ĥ = −s/A² + R_2(s),
   R_2(s) = s²/(A²(A+s)), gives rest = −E1 + E2.
   - E1 = −δ/(π²(1−z)A²v′v′_0) integrates to ≤ C(1−z)δ(1 + ln(1/((1−z)δ))).
   - E2 = κ_1R_2(s_1) − κ_0R_2(s_0). On region A write it as (κ_1−κ_0)R_2(s_1) + κ_0(R_2(s_1)−R_2(s_0)), with
     |R_2(s_1) − R_2(s_0)| ≤ Cδ(v′_0 + δ + 2|k|). On region B use direct bounds. Altogether ≤ Cδ(1 + L + ln(1/(z(1−z)))).
3. *On |k| > c_x/4:* ∫|ρ_r| ≤ C(δ + δz^{−1/2}) by step 5 of (a), and ∫|odd| ≤ C(1−z)^{3/2}δ/c_x.
4. Since |∫|a+b| − ∫|a|| ≤ ∫|b|, integrating over z gives |∫|ρ_r| − c_1λ| ≤ C(x)λ²L. ∎

**Numerics** (`r2_ladder1_even.py`, x = 2):
- ∫|odd|/λ = 1.262937…1.262979;
- ∫|rest|/(λ²L) = 0.491, 0.431, 0.401, 0.383, 0.371;
- (∫|ρ_r| − c_1λ)/(λ²L) = −0.076…−0.024 for m² = 10⁻²…10⁻⁶;
- `t6b` gives 1.26329 at m² = 10⁻⁷.

**(e) Identification of the fibered and covariant values** (d = 6−2ε; fibered measure
(1/Γ(2−ε))∫dξ/(1−ξ)∫dt t^{1−ε}(…)/v², t = |k|², v = ξm² + t/(1−ξ); c = c_x).

- **(e1) Γ** — [R] [rev-1: final review]; 「本书给出的推导」. For −1 < ε < 1 the fibered value equals I_Γ exactly.
  1. By §1.2, ∫dt t^{1−ε}⟨F⟩ = (Γ(2−ε)/π^{2−ε})∫d^Dk F with D = 4−2ε. Hence the fibered value is
     π^{−(2−ε)}∫dξ(1−ξ)²∫d^Dk/((|k|²+μ_0²)²(|k+p|²+M_1²)), with μ_0² = ξ(1−ξ)m², p = (1−ξ)q and M_1² = ξ(1−ξ)(c+m²).
  2. A Euclidean Feynman parameter (Tonelli) gives
     Γ(1+ε)∫_0^1dξ(1−ξ)^{1−ε}∫_0^1dy y[yξm² + (1−y)ξ(c+m²) + y(1−y)(1−ξ)]^{−1−ε}.
  3. The covariant value is Γ(1+ε)∫_simplex x_1[x_2(x_1+x_3)m² + x_3(x_1+x_2c)]^{−1−ε}.
  4. The map x_2 = ξ, x_1 = (1−ξ)y, x_3 = (1−ξ)(1−y) (Jacobian 1−ξ) carries one integral onto the other; the bracket
     transforms as F(x(ξ,y)) = (1−ξ)·[…].
  - Checks: `r3_FI_exact.py` (symbolic step; quadratures to 3·10⁻¹³ and 5·10⁻¹⁰, limited by the fibered quadrature).
    Final review, own code: m² = 0.01, ε = 0.1 gives 4.68929374814784151 on both sides (rel 4·10⁻²⁶); m² = 0.05,
    ε = 0.25 gives 4.852772726725455 (rel 1·10⁻²⁴).
  - *Positioning (Fix 3).* An explicit instance of the light-front–covariant equivalence for scalar graphs (as for
    Prop B.3). 「本书给出的推导」, not new.
- **(e2) C_{R_1}** = S²R(p−k)Ĥ, with Ĥ = 1/(Q² − 2q^-k^+) — [R] [rev]. Fibered value = covariant value =
  Γ(ε)∫_0^1dξ(1−ξ)^{1−ε}(ξm²)^{−ε}/(Q²(1−ξ/x)), exactly.
  - Fibered: ∫_0^∞dt t^{1−ε}/v² = (1−ξ)^{2−ε}(ξm²)^{−ε}Γ(2−ε)Γ(ε) (a Beta integral).
  - Covariant: Feynman/Cheng–Wu with the shift by λn (n² = 0) gives Δ = y(1−y)m² + λQ²(1−(1−y)/x); the λ-integral gives
    (y(1−y)m²)^{−ε}/(εQ²(1−(1−y)/x)), and ξ = 1−y.
  - Values at x = 2: 11.27248142379893 (m² = 0.01, ε = 0.1) and 27.06758503548673 (m² = 0.001, ε = 0.3); numerically to
    10⁻²¹–10⁻²².
- **(e3) C_H** = S²R(p̂−k)(H_0−Ĥ) — **C_H is identified with its DR-linearity value under (V2)**: the fibered value equals
  the closed form below [R] [rev-1]; the whole-integrand parametric value is [P].
  - For 0 < ε < 1 the fibered value equals
    C_H = Γ(1+ε)Γ(−ε)Γ(2−ε)Γ(2−2ε)^{−1}Q^{−2−2ε}∫_0^1dy y(y+(1−y)c)^{−1−ε}
        = Γ(1+ε)B(−ε,2−ε)Q^{−2−2ε}[(1−c^{1−ε})/(1−ε) + (c−c^{1−ε})/ε]/(1−c)²,
    exactly.
  - This is the continuation of the covariant value of T_HΓ, the massless on-shell target ladder, which is absolutely
    convergent for −1 < ε < 0. Equivalently, it is the DR value of C_H obtained with DR linearity and the scaleless
    T_HC_{R_1} set to zero ((V2)).
  - *Proof.*
    1. *Reduction to T_HΓ; constants corrected in final2 (final-review Fix 7(a)).* The fibered C_H is
       (1/Γ(2−ε))∫dξ(1−ξ)∫dt t^{−1−ε}[⟨h_0⟩ − ĥ], since κ_0 has v_0 = t/(1−ξ). Here ⟨h_0⟩(t) = a^{−1}F(z), with
       F = ₂F₁(1/2,1;2−ε;·), a = A + t/(1−ξ), z = 4t/a², and A = 1 − ξ/x ∈ [c_x,1]. The ingredients:
       - *Range of z.* z is maximal at t = A(1−ξ), z_max = (1−ξ)/A, so 1 − z ≥ ξc_x/A ≥ ξc_x.
       - *Bounds on F* (0 ≤ z < 1, 0 < ε < 1, ε ≠ 1/2). From Euler's representation
         F(z) = (1−ε)∫_0^1(1−s)^{−ε}(1−zs)^{−1/2}ds, splitting at 1−s = 1−z and using 1−zs ≥ max(1−z, z(1−s)):
         1 ≤ F(z) ≤ K_ε[1 + (1−z)^{1/2−ε}]. From (1−y)^{−1/2} − 1 ≤ y(1−y)^{−1/2}: F(z) − 1 ≤ zF(z). At ε = 1/2 the
         growth is logarithmic.
       - *Constants.* Hence |⟨h_0⟩ − ĥ| ≤ |a^{−1} − A^{−1}|F + A^{−1}(F − 1) ≤ C(ξ)t/(1−ξ) on (0,1], and
         |⟨h_0⟩| ≤ C(ξ)(1−ξ)/t on [1,∞), with C(ξ) = K′_ε[1 + (ξc_x)^{1/2−ε}].
       - *Uniform for ε < 1/2.* There F(1) = Γ(2−ε)Γ(1/2−ε)/(Γ(3/2−ε)Γ(1−ε)) is finite (3.5000 at ε = 0.3).
       - *Not uniform for 1/2 < ε < 1.* There F(z) ∼ [Γ(2−ε)Γ(ε−1/2)/Γ(1/2)](1−z)^{1/2−ε} as z → 1, and z_max → 1 as
         ξ → 0. So the constants **grow like ξ^{1/2−ε}** (logarithmically at ε = 1/2). The final report's "with the
         outer factor (1−ξ) the constants are uniform" holds only for ε < 1/2.
       - *Integrability.* C(ξ) is integrable against the outer measure (1−ξ)dξ for every ε < 3/2. So Lemma A.9, with
         ξ-integrable constants and dominated convergence, shows that for every ε ∈ (0,1) the fibered C_H is the
         continuation from −1 < ε < 0 of the fibered T_HΓ. Alternatively: prove it for 0 < ε < 1/2, where the
         constants are uniform; the fibered C_H converges absolutely, hence is analytic, on (0,1); extend by
         analyticity.
       - *Checks* (`f2_C4e3_checks.py`, part (A), x = 2):
         - sup_z F(z)/(1 + (1−z)^{1/2−ε}) = 3.47, 6.71, 5.97, 4.24, 1.19 at ε = 0.3, 0.45, 0.55, 0.6, 0.9;
         - F(z)(1−z)^{ε−1/2} → 4.762 = Γ(1.4)Γ(0.1)/Γ(1/2) at ε = 0.6;
         - max(C_1,C_2) at ξ = 10⁻², 10⁻⁴, 10⁻⁶, 10⁻⁸ is 1.24, 1.54, 1.67, 1.72 (ε = 0.3), 2.06, 4.41, 8.16, 14.1
           (ε = 0.6) and 4.84, 31.1, 197, 1245 (ε = 0.9);
         - max(C_1,C_2)/(1 + (ξc_x)^{1/2−ε}) stays ≤ 1.82 in all three cases.
    2. For −1 < ε < 0: ⟨h_0⟩ = (1−ξ)/(|k+(1−ξ)q|² + M²) with M² = ξ(1−ξ)c. The Euclidean transverse integral
       ∫d^Dk|k|^{−4}h_0 equals π^{D/2}Γ(1+ε)(1−ξ)∫_0^1dy y[(1−y)(1−ξ)(ξc + y(1−ξ))]^{−1−ε}. So the fibered T_HΓ is
       Γ(1+ε)Q^{−2−2ε}T(ε), with T(ε) = ∫_0^1ds s^{1−ε}∫_0^1dy y(1−y)^{−1−ε}(c(1−s)+ys)^{−1−ε} and s = 1−ξ.
    3. The substitution (α,β,γ) = (1−s, sy, s(1−y)) has dβdγ = s ds dy and gives T = ∫_simplex βγ^{−1−ε}(cα+β)^{−1−ε}.
       Then (α,β) = (1−γ)(1−y′, y′) factorizes it: T = B(−ε,2−ε)∫_0^1y′(c+y′(1−c))^{−1−ε}dy′.
    4. The covariant parametric value of T_HΓ, Γ(1+ε)∫_simplex x_1(x_3(x_1+x_2c))^{−1−ε}, reduces to the same expression
       by x_3 = γ, (x_1,x_2) = (1−γ)(1−y′, y′).
    5. Both sides converge absolutely for −1 < ε < 0; continue. ∎
  - *Values* (x = 2): −6.584962095176247930933 (ε = 0.1), −3.572721309348424999595 (0.2), −2.607837860955034437041
    (0.3). Final review, own 2D quadrature with the t^{−1−ε} tail done analytically: −6.5849620951762479309,
    −3.5727213093484249996, −2.607837860955034437 (rel 4·10⁻²⁵, 1·10⁻²⁵, 6·10⁻²⁶), and x = 1.3, ε = 0.15:
    −5.5948279175487600717 (rel 3·10⁻²⁶).
  - *Checks* (`r3_ladder_CH_exact.py`; precision statement corrected, final-review Fix 7(b)):
    - *the simplex identity.* In `r3_ladder_CH_exact.log`, T(square) and T(simplex) agree to 4.1·10⁻²¹ (ε = −0.6) and
      only **5.6·10⁻¹¹ (ε = −0.3)**. The latter is limited by the (1−y)^{−1−ε} endpoint of the square-form quadrature
      (T(square) itself is off by 7.5·10⁻¹³ there). In the continued forms they agree to 1.5·10⁻²⁸, 4.0·10⁻²⁵,
      9.9·10⁻²², 1.6·10⁻¹⁶ at ε = 0.1, 0.2, 0.3, 0.45. The final report's "10⁻¹³–10⁻³¹" overstated the agreement.
      **Recomputed in final2** with the endpoint substitutions y = 1 − u^{2/(−ε)} and γ = u^{2/(−ε)}
      (`f2_C4e3_checks.py`, part (B)): T(square) = 1.405405541037487618909109 at ε = −0.3 and 0.4752994027639299558613118
      at ε = −0.6; square, simplex and closed forms agree to < 2·10⁻³¹ at both points;
    - the covariant T_HΓ to ≤ 8·10⁻³¹ (ε = −0.6, −0.3, −0.1);
    - the fibered 2D quadrature, with the analytic small-t tail c_1t_0^{1−ε}/(1−ε), c_1 = −1/((1−ξ)A²) + 2/((2−ε)A³), to
      2·10⁻³⁰ (ε = 0.1, 0.2) and 2·10⁻²⁸ (ε = 0.3);
    - the whole-integrand parametric value (§1.4), in two independent forms (the round-2 report and review r3_1), agrees
      to 3·10⁻³¹ (ε = −0.3), 2·10⁻³⁰ (0.1), 2·10⁻²⁷ (0.2) and 1·10⁻²⁴ (0.3). Its analytic reduction is not written;
      hence [P] for that variant.
  - **Corrected** (review r3_1 required fix 7): the round-2 fibered values deviated from the covariant ones by 4.2·10⁻¹⁵
    (ε = 0.2) and 3.4·10⁻¹³ (0.3). The cause was the omitted part t < e^{−40} of the round-2 quadrature,
    ≈ e^{−40(1−ε)} = 1.3·10⁻¹⁴ and 6.9·10⁻¹³. The script comment "< 1e-15" was false. The printed round-2 value
    −2.60783786095414 was the fibered one; the covariant value is −2.60783786095503.
- **(e4) ε-uniformity of (a)–(d)** — sketch only [P].
  - The transverse measure in d = 6−2ε carries (|k|²)^{−ε}.
  - Lemma A.7 brings the factors (1−z)^{1−ε} and (t−zv)^{1−ε}, and the S³ averages become S^{3−2ε} averages.
  - The region |k| ~ m gives the exponent 1−2ε, and uniform constants would follow from (|k|²)^{−ε} ≤ 1 + (|k|²)^{−ε_0}.
  - The estimates are not written out.

**Grades.** (a)–(d) [R, R_PT] **at ε = 0 (d = 6)**; their ε-uniformity is only sketched ((e4), [P]). (e1) [R]
(「本书给出的推导」). (e2) [R]. (e3): fibered value = closed form = DR-linearity value under (V2) [R]; the
whole-integrand parametric variant [P]. The results are elementary; c_1(x) was first derived in review r1_1.

### Claim C.5 (DIS ladders of every length n) — [P] (downgraded in round 1) [rev]

**Claim.** For every n, (CS1^φ)–(CS3^φ) hold on the cover N_{R_j} = {v_i ≤ λ², |k_{iT}|²/(1−z_i) ≤ λ² for i ≤ j},
U_{R_j} = N_{R_j}∖N_{R_{j+1}}, with items ≤ C_nλΛ^n. Moreover ∫|ρ_r| ≤ C_nλ(1+L)^n at ε = 0.

**Status** (wording corrected, final-review Fix 6).
- n = 1: proved **at ε = 0 (d = 6)**, including the leading coefficient c_1(x) (Prop C.4(a)–(d)). The ε-uniformity is
  only sketched (Prop C.4(e4), [P]). The fibered values of Γ and C_{R_1} are identified exactly. C_H is identified with
  its DR-linearity value under (V2); its whole-integrand parametric value is [P] (Prop C.4(e)).
- n = 2: numerical (`t11`).
  - The full norm is 2.63, 3.26, 3.90, 4.54, 5.19 λ for m² = 10⁻²…10⁻⁶, ≈ (1.3+0.27L)λ.
  - With the q-azimuth averaged it is 0.83–0.88λ, since the rung cross terms keep first order.
  - With both azimuths averaged it is second order: 0.93, 1.51, 2.22, 3.06, 4.07 m².
- General n: proof sketch only.

**Strategy.** Induction on N_j(s) = ‖U_j(s;·)‖_{L¹} and on D_j(s,s̃) = ‖U_j(s) − U_j(s̃)‖ for equal (ξ,K):
- (R1) N_j ≤ ∫_A|Δκ|N_{j+1} + ∫_Aκ_0D_{j+1}, plus the undifferenced bound on region B;
- (R2) D_j ≤ ∫|κ(s)−κ(s̃)|N_{j+1} + ∫κ(s̃)D_{j+1}. The projected parts cancel, since πs = πs̃.

Exact region-A constants, for |k| ≥ 8√v:
- |v′−v′_0| ≤ (17/8)z√v|k|/(1−z);
- v′/v′_0 ∈ [47/64, 81/64];
- |Δκ| ≤ 9z(√v/|k|)κ_0.

All k-integrals reduce to one-dimensional integrals by Lemma A.7.

**Gaps (open).**
- (g1) The bound (P1) cannot hold pointwise at the top level j = n: h(s) is unbounded as ξ → 0, and A + v + 2K·q ≥ ξc_x
  is sharp. The induction must start at j = n−1, using the direction-averaged Lemma C.3.
- (g2) On region B the projected kernel κ_0 ~ (1−z)/|k|⁴ is not integrable at k = 0 against an O(1) factor. The
  undifferenced form κ(s)|U(Φ(s))| + κ_0|U(Φ(πs))| must be used, with N_{j+1}(Φ(πs)) = O(√v′_0).
- (g3) The Lipschitz bound (P2) at j = n−1 involves ⟨h²⟩, which carries the factor (d̄/d_min)^{1/2} with d_min ≥ zξc_x. A
  weight ξ^{−1/2} must be carried through the induction; it stays integrable through ξ_j = z_jξ_{j−1}.
- (g4) For large v the bounds grow like powers of Λ(v) = 1 + |ln v| (two-sided logarithm).
- (g5) ε-uniformity in d = 6−2ε, with weights (t−zv)^{1−ε}, is not addressed.

**Scope.** This is a statement about φ³₆ only. It does not deliver slot X2c, which concerns the fermion two-rung ladder
with Dirac projections. The bounds hold at real x ≥ x_0 > 1, not with the complex-ω uniformity that
`prop:disall-two-routes`(b) needs.

**Prior art.**
- The OPE proof of moment factorization in the unphysical region (Ch. 5).
- Ladder mass-singularity factorization: Ellis–Georgi–Machacek–Politzer–Ross 1979; Curci–Furmanski–Petronzio 1980.
- Collins' inductive Theorems 1R–4 (§10.7.5–10.7.6).

**Conjecture [P].** The angle-averaged norm is O(λ²L^{b_n}).

### Proposition C.6 (two-element chains) — [R, R_def] [rev]

**Setting.** Γ = H(k)J(k,p) with regions {A < H}. T_A acts only on H (H(k) → H(πk)), and T_H acts only on J (J → J̃).

**Identities.** C_A = H(πk)J, C_H = ΔH·J̃ and r = ΔH·ΔJ. Hence:
- (CS1)_A ⟺ ∫_{U_A}|ΔH·J| is small;
- (CS2)_A ⟺ ∫_{U_A}|ΔH·J̃| is small;
- (CS1)_H ⟺ ∫_{U_H}|ΔH·ΔJ| is small;
- (CS3) ⟺ HJ is integrable (uniformly), and H(πk)J and ΔH·J̃ are integrable (for ε > 0).

This is the n = 1 case of the ladder structure. The structure is known (Ex. D.48 of the source); it is made precise here.

