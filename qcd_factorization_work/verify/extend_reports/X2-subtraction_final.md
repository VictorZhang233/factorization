# X2 — The precise Collins subtraction theorem and its hypotheses (App. N): verification in scalar models — FINAL REPORT

**Proof-extension slot X2 of the monograph 《QCD 因子化定理：严格证明、全阶论证与适用边界》, Appendix N (`app:appN`).**
Final revision, 2026-10-11. This document supersedes `X2-subtraction.md` (round 0), `X2-subtraction-fix1.md` and
`X2-subtraction-fix2.md`. It takes into account the six adversarial reviews `X2-subtraction-rev1-1.md`,
`-rev1-2.md`, `-rev2-1.md`, `-rev2-2.md`, `-rev3-1.md`, `-rev3-2.md` (all in `verify/extend_reports/`). It is
self-contained: the proofs that round 2 cited as "unchanged from round 1" are written out again here. The ledgers in
§12–§13 and the revision record in §17 trace every change.

---

## 0. Status and scope

**What this report is.** Appendix N proves a conditional subtraction theorem (`thm:appN-subtraction`): if Collins'
conditions (CS1)–(CS3) hold on a contour Ω compatible with all subtraction terms (`asm:appN-contour`), the remainder
is power suppressed in an integral norm, uniformly in ε. Even for the one-loop triangle, neither the conditions nor
the contour had been written out. This report proves (CS1)–(CS3) for explicit graphs and integrand families in three
**scalar** models. It does so in a *fibered* form: all minus components are integrated exactly by residues, and the
estimates are made on the real base of plus and transverse components.

**No statement in this report is a statement about QCD.** Gauge numerators, Ward identities and (Abs) for
transverse polarizations are not treated (§14, OQ2).

**Main results of the final revision.**

1. *Fibered subtraction theorem* (Thm A.1, [R, R_cond]). The unconstructed contour hypothesis is replaced by two
   hypotheses, (FR) and (FI), that can be checked graph by graph. Error type E-N^φ.
2. *One-loop off-shell triangle* (Part B). Two results here:
   - (CS1^φ)–(CS3^φ) hold with the optimal λ-exponent λ²L^{≤2}, uniformly in ε ∈ (0,1/10] (Thm B.5). The proof is
     computer-assisted; the certificate archive is now self-contained and has been re-verified exactly by
     independent code.
   - All fibered values are identified *exactly* with the covariant values: Γ (Prop B.3, new in this revision) and
     the four Collins terms (Prop B.2).
   Hence the integrated subtraction theorem for the triangle holds **without premises**: |I_Γ − Σ_R I_{C_RΓ}| ≤
   C(λ²L² + λ^{8/5}) on (0,1/10] (Cor B.6, [R, R_PT], computer-assisted). This delivers slot X2a; §11 states the
   review condition.
3. *DIS in φ³₆* (Part C). All one-loop graphs are treated, and the one-rung ladder is proved completely, including
   its leading norm coefficient. The fibered values of Γ, C_{R_1} and C_H of the one-rung ladder are identified
   exactly (Prop C.4(e)); the C_H identification is new in this revision. Ladders of length n ≥ 2 remain [P].
4. *Massive photon* (Part D). The light-like remainder is computed exactly. For space-like rapidity regulators, the
   complete real-base pole structure is given.
5. *Two-loop planar vertex* (Part E). The algebra is exact. The 50 zeroing patterns have an exact scaling structure.
   *New in this revision:* the nine single-approximator terms are identified with the region integrals of
   Smirnov–Rakhmetov (1999). As a result, the integrated remainder ∫r = Φ^(2)/Q⁴ − LP and its NLP coefficient hold
   under the auxiliary-regulator premises (RA1), (RA2) and the values convention (V2) only.
6. *All orders* (Thm F.1, [R, R_cond]). The theorem is restricted to **infrared-finite graph classes** of the
   super-renormalizable model (M1). The round-2 claims that (CS3^φ) holds for every UV-finite (M1) graph, and that
   the "bubble class" is a graph class of (M1), are **withdrawn**: a three-loop graph is an explicit counterexample to
   the first, and the second rests on a model misidentification (Prop A.6, Thm B.8).

**Verification status flags.** Every result carries one of the following flags:
- **[rev]** — independently re-derived or audited by at least one adversarial reviewer in rounds 1–3;
- **[new-final]** — new in this final revision: proved here and checked by the scripts cited, but not yet seen by an
  independent reviewer.

The results flagged [new-final] are Prop B.3, Prop A.6, Lemma A.8, Lemma A.9, the C_H and Γ parts of Prop C.4(e),
Thm E.3(ii) and (iv)–(vi), and the archive verifier of Lemma A.3(c). Under the PASS rule of `spec_v2/OUTLINE_appMNOPQ.md`
§00.4, these results need one independent confirmation before the integrator prints them with the grades stated here
(§11).

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
- External momenta in (+,−,T) components, both incoming:
  p_1 = (P, −m²/2P, 0_T), p_2 = (m²/2P′, −P′, 0_T), so that p_i² = −m².
- Kinematic variables: Q̃² ≡ 2PP′ and Q² ≡ −(p_1+p_2)² = (Q̃²+m²)²/Q̃² ≥ 4m²; λ² = m²/Q̃²; L = L̃ = ln(Q̃²/m²);
  τ ≡ m²/Q̃².
- One-loop graphs: the triangle (φ exchange) and the J–φ mixing graph. External self-energies are amputated, and
  massless tadpoles vanish in dimensional regularization.
- **Caveat (new in this revision).** The coupling has mass dimension one, so (M1) is *super-renormalizable*. At fixed m,
  its off-shell vertex is infrared divergent for every graph that carries a self-energy insertion on a line able to
  become soft, and for some graphs without any self-energy insertion (Prop A.6; Jackiw–Templeton 1981).
  Statements about (M1) beyond one loop are therefore restricted to graphs that satisfy the infrared-finiteness
  hypothesis (IRF) of §2. The full form factor F^(N) of (M1) is IR divergent at fixed m for N ≥ 2.

**(M2) DIS forward amplitude in φ³₆, d = 6 − 2ε.**
- Same fields and interaction as (M1); the coupling is dimensionless (renormalizable).
- Target: the off-shell ψ with p = (p^+, −m²/2p^+, 0_T). The current J is inserted twice.
- Frame q^+ = 0, q = (0, q^-, q_T), with Q² = q_T² and x = Q²/(2p·q) ≥ x_0 > 1. This is the unphysical region:
  all invariants are space-like and there are no cuts.
- Further variables: λ² = m²/Q² and c_x = 1 − 1/x.

**(M3) Abelian massive photon, d = 4 − 2ε.**
- Massless on-shell legs p_1 = (P, 0, 0_T) and p_2 = (0, −P′, 0_T); the exchanged boson has mass M.
- λ² = M²/Q², with Q² = 2PP′ (space-like momentum transfer).

### 1.2 Fibered densities

The loop momenta k_i = (k_i^+, k_i^-, k_{iT}), i = 1, …, ℓ, are split into a *base* b = (k_i^+, k_{iT})_i and a
*fiber* (k_i^-)_i.

𝒱 denotes the space of finite sums of products
Π_j (a_j(b) + Σ_i β_{ji}(b) k_i^- − i0 w_j)^{−e_j}
times measurement functions of b. Here a_j and β_{ji} are real polynomials in b, the w_j > 0 are constants and
e_j ∈ ℤ. A factor with e_j > 0 is a *denominator* and a factor with e_j ≤ 0 is a *numerator*.

Every propagator −l² + M² − i0 = −2l^+l^- + |l_T|² + M² − i0 is affine in the minus components, with coefficient
−2l^+. Every eikonal factor (2Pk^- − i0, 2P′k^+ − i0) is affine as well. The approximators of §1.3 replace light-cone
components or the infrared regulator by zero, so they map 𝒱 into 𝒱.

The pole of (βk^- + a − i0w) lies in the upper half plane iff w/β > 0.

**Fibered density.** For F ∈ 𝒱, the fibered density ρ_F(b) is the iterated real-line integral over k_ℓ^-, …, k_1^-
in a fixed order, normalized so that, whenever Fubini applies,

  μ^{2ε}∫d^dk_1⋯d^dk_ℓ/(iπ^{d/2})^ℓ F = ∫_B ρ_F dμ_ε.

At one loop in (M1) this reads dμ_ε = μ^{2ε}dx dκ κ^{−ε}/Γ(1−ε), with x = k^+ and κ = k_T². In (M2), with the rung
on shell, the measure is (1/Γ(2−ε))∫dξ/(1−ξ)∫dt t^{1−ε}(…)/v², with t = |k_T|².

Each fiber integral is evaluated as a finite sum of residues by the script `lcpt.py`. The map F ↦ ρ_F is linear, since
it is a sum of real-line integrals.

### 1.3 Regions, approximators, Collins terms

- 𝓡 is a finite set of regions, partially ordered, and T_R: 𝒱 → 𝒱 (R ∈ 𝓡) are the approximators: linear maps that
  replace light-cone components or the infrared regulator by zero.
- The *Collins terms* are defined recursively by
  - C_RΓ = T_R(Γ − Σ_{R′<R} C_{R′}Γ),
  - X_{R_0} = Γ − Σ_{R<R_0} C_RΓ, so that C_{R_0}Γ = T_{R_0}X_{R_0},
  - r = Γ − Σ_R C_RΓ.
  These are `def:method-subtraction` and `prop:method-chains` of the monograph.
- *Soft-first convention* (two loops): a jet line that carries soft momentum enters the hard factor with its
  soft-approximated momentum. This is Collins 2011 §10.6.6, "the requirement that the hard factor does not depend on
  the soft momenta".
- *Collins conditions* (`def:method-collins-conditions`):
  - (CS1)_{R_0}: (1−T_{R_0})X_{R_0} is power suppressed on U_{R_0};
  - (CS2)_{R_0}: C_RΓ is power suppressed on U_{R_0} for every R ≰ R_0;
  - (CS3): Γ ∈ L¹ uniformly in ε, and C_RΓ ∈ L¹ for every ε ∈ (0,ε_0].
- Their fibered versions, (CS1^φ)–(CS3^φ), are the same conditions in the integral norm ∫_{U}|ρ_F| dμ_ε on the real
  base.

### 1.4 Values

1. **Fibered value** of F: ∫_B ρ_F dμ_ε, whenever this integral converges absolutely.
2. **Covariant value** I_F of F, built from quadratic propagators, linear (eikonal) factors and a polynomial
   numerator. It is *defined* by the Feynman/Cheng–Wu parametric representation of the **whole** integrand:
   - combine the denominators;
   - shift, Wick-rotate the shifted pure-quadratic loop integral, and do the Gaussian integral;
   - continue analytically in ε.
   For Γ and the Collins terms of Parts B and C, the resulting parametric integrals converge absolutely in the
   ε-ranges stated. For the two-loop composite patterns they do not, which is why Thm E.3 uses items 3 and 4.
3. **DR linearity** (standard convention, used only where stated). A sum is split into pieces whose parametric
   integrals converge on different ε-domains, and the separately continued values are added. A piece that is exactly
   homogeneous under a scaling of non-zero weight is assigned the value 0; this is the convention (V2) of
   `asm:appN-values`.
4. **Auxiliary analytic regularization.** Each line l is raised to the independent complex power 1+δ_l, the integral
   is continued in (ε,δ), and δ → 0 is taken at the end.

### 1.5 Grades and error types

Grades follow WRITER_SPEC v2.2 §4.3.
- **[R, R_PT]**: rigorous for the stated graphs at the stated order, with no unproven input. "Computer-assisted"
  means that the only non-elementary inequalities are linear-programming optima, certified by exact rational
  primal–dual pairs. The certificates are archived self-contained and re-verified by independent code (Lemma A.3(c)).
- **[R, R_def]**: an algebraic consequence of the definitions.
- **[R, R_cond: …]**: a complete proof from the listed premises; the implication is [R].
- **[P]**: finite subclass, or numerical evidence only.

The error type **E-N^φ** denotes the bound ∫_A|ρ_F| dμ_ε ≤ Cλ^aL^K on the real fibered base, with the fiber
integrated exactly, uniformly in ε ∈ (0,ε_0]. It implies the integrated statement. It is not E-F in the spec's sense,
and it is not comparable with E-N on a deformed four-dimensional contour.

---
## 2. Register of hypotheses

The names below are chosen to avoid the binding names of WRITER_SPEC v2.2 §4.4 item 4 ((GA1)–(GA4), (V1)(V2),
(CU1)–(CU3), (WI1)(WI2), (U1)(U2), (Z1)–(Z3), (AN1)–(AN6), (O1)(O2), (OP1)(OP2), …). All of them are *local*
hypotheses of the statements that use them, as (CS1)–(CS3) are; none is a new `asm:` register entry. Open problems
are numbered OQ1–OQ17, so that they cannot be confused with the items (O1)(O2) of `asm:intro-np-ope`.

| name | content | round-2 name |
|---|---|---|
| **(FR)** *fibered residue admissibility* of F ∈ 𝒱 | For a.e. b and at every stage of the iterated fiber integration, two conditions hold. (i) The current integrand, as a function of the current k_i^-, is rational of degree ≤ −2 and has no pole on the real axis. (ii) On at least one side of the real axis its poles are simple. | (AR) |
| **(FI)** *fibered–covariant identification* for F | ∫_B ρ_F dμ_ε converges absolutely and equals the covariant value I_F (§1.4), for ε in the stated range. | (ID) |
| **(IL1)** | For ε in a non-empty open interval E ⊂ (0,ε_0] and every η > 0, ∫d^dk \|F_η\| < ∞. Here F_η is F with every i0 replaced by iη. | (I1) |
| **(IL2)** | G ∈ L¹(B,dμ_ε) for ε ∈ E, where G is the sum of the moduli of the η = 0 residue terms selected by the algorithm. | (I2) |
| **(IL3)** *bridge* | lim_{η→0+} μ^{2ε}∫d^dk/(iπ^{d/2}) F_η = I_F for ε ∈ E. | new (round 3, required fixes r3_1-6 and r3_2-5) |
| **(IRF)** *infrared finiteness* of a graph G | The parametric (covariant) integral of G converges absolutely for every ε ∈ [0,ε_0]. Its integrand is positive in the space-like kinematics of (M1) and (M2). | new (round 3, required fixes r3_1-2 and r3_2-2) |
| **(LCE)** *LCPT–covariant equivalence* | Let G satisfy the hypotheses of Lemma A.4 and (IRF). Then ∫_B ρ_G dμ_ε = I_G. Sources: Chang–Yan 1973; Ligterink–Bakker 1995; see Collins 2018 for when the elementary light-front derivation fails. It is not proven at the rigour of this report. | "the standard LCPT input" |
| **(RA1)** | The analytically regularized pattern integrals of the two-loop vertex (§1.4 item 4) are meromorphic in (ε,δ). Speer 1968 proves this for quadratic propagators; it is not proven here for the eikonal-type linear factors. | (Reg)(a) |
| **(RA2)** | The nine single-approximator integrals ∫T_RΓ of the two-loop vertex, analytically regularized, are regular at δ = 0 for ε in a punctured neighbourhood of 0, and their δ → 0 limits are their dimensionally regularized values. | (Reg)(b), now reduced to the singles (Thm E.3(iii)) |
| **(FIN2)** | ∫Γ and ∫r are finite at ε = 0 (two-loop vertex). | (F); **discharged** in this revision (Thm E.3(v)) |
| **(COV)** *cover hypothesis* | There is a finite cover {U_R} of B on which (CS1^φ)_{R_0} and (CS2^φ)_{R_0} hold with an exponent a > 0, for every R_0. | (F1) |
| (V2) | The values convention of `asm:appN-values`: scaleless chain terms have value zero. | — |

(FR) and (FI) are the *checkable replacements* of `asm:appN-contour`(a) ((GA1)(a)) in the fibered framework. The
meromorphy part `asm:appN-contour`(b) is still needed where poles in ε are removed (`cor:method-removing-eps`).

---
## 3. Part A — General results

### Theorem A.1 (fibered subtraction theorem) — [R, R_cond: (FR), (FI), (CS1^φ)–(CS3^φ)] [rev]

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
1. Fix R_0. From X_{R_0} = Γ − Σ_{R<R_0}C_RΓ and C_{R_0}Γ = T_{R_0}X_{R_0} we get Γ − Σ_{R≤R_0}C_RΓ =
   (1−T_{R_0})X_{R_0}. Hence

   r = (1−T_{R_0})X_{R_0} − Σ_{R≰R_0} C_RΓ, (A.1)

   an identity in 𝒱 (it is (D.10) of the reference).
2. By (FR), all iterated fiber integrals of Γ and of the C_RΓ exist for a.e. b. Fiber integrals are linear, so (A.1)
   holds for the densities: ρ_r = ρ_{(1−T_{R_0})X_{R_0}} − Σ_{R≰R_0}ρ_{C_RΓ} a.e. on B.
3. By (CS1^φ) and (CS2^φ), ∫_{U_{R_0}}|ρ_r| ≤ (1+|𝓡|)Cλ^aL^K.
4. Summing over the finite cover gives (i).
5. By (CS3^φ), all terms are integrable for ε ∈ (0,ε_0], so ∫ρ_r = ∫ρ_Γ − Σ∫ρ_{C_RΓ}, and |∫ρ_r| ≤ ∫|ρ_r| gives
   (ii).
6. (iii) follows from (ii) and (FI). ∎

All three round-2 reviewers re-derived (A.1).

**What it replaces.** In `thm:appN-subtraction` the premise `asm:appN-contour`(a) is a four-dimensional contour Ω,
assumed to be compatible with all subtraction terms; it is never constructed. Wherever the fibered densities are
absolutely integrable on the real base, it is replaced by (FR)+(FI), which can be checked graph by graph (Parts B, C).
`asm:appN-contour`(b), meromorphy near ε = 0, is still needed for `cor:method-removing-eps`.

**Scope.** The theorem needs fibered densities that are absolutely integrable on the real base. This holds for
- the triangle of (M1);
- graphs of (M1) satisfying (IRF), given (LCE) (Cor A.5);
- (M2) at x > 1.

It does **not** cover:
- Glauber-pinched (cut) processes (OQ7);
- real-base fibrations with poles, e.g. space-like rapidity regulators (Prop D.2);
- graphs with q^+ = 0 subloops. These are pure zero modes in this frame and violate (FR); examples are the J–φ mixing
  and t-channel graphs of (M2), which are treated outside the fibered framework (Prop C.1(iv),(v));
- IR-divergent graphs of (M1), for which (CS3^φ) is false (Prop A.6).

**Prior art and novelty.**
- Nested (forest) subtractions for general graphs exist at the level of pinch surfaces:
  - Collins 2011, ch. 10 (Theorems 1R–4);
  - the coordinate-space analysis of Erdoğan–Sterman 2015;
  - Ma 2020, a BPHZ-like IR forest formula for wide-angle massless amplitudes; the singularities of its subtraction
    terms cancel pairwise.
- New here is the formulation as an integral-norm (power-suppression) statement on a real fibered base, with the
  checkable hypotheses (FR), (FI). The proof is the elementary one of `thm:appN-subtraction`.

**Remarks.**
- (a) The literal (CS3) on the *real* four-dimensional contour fails already for Γ: there is a ln(1/η) divergence across
  light cones. This is why the monograph uses a deformed Ω. It is a remark, not an error of the source.
- (b) *Sharpening.* For (CS2^φ) to be uniform in ε, the non-maximal U_R must be UV-bounded or must carry items that
  decay fast enough. Example, triangle with Def-D.5-type unbounded U_{C_1} (units of §1.1):
  ∫_{U_{C_1}∩{k^+>P}}|ρ_{C_{C_2}}| = ∫_P^∞dx∫_0^{2sx}dκ κ^{−ε}/(Pe_2(e_2+κ)) ≃ (2s)^{1−ε}P^{−ε}/(ε(1−ε)P(2P′)²)
  as s → 0, which is not uniform in ε. The cover of Thm B.5 puts the unbounded sliver
  {−m²/2P′ < k^+ < 0}×{κ>0} in U_{C_2}; this is harmless, because the sliver items decay like κ^{−2}.
- (c) *The fibration is part of the statement.* Adding transverse azimuths to the fiber turns first-order full norms
  into second-order ones (Collins 2011 §10.7.3: "these commonly vanish after an integral over angle. Then the actual
  error is one power better: p = 2"). This is quantified in §7.4 and Prop C.4.

---

### Lemma A.2 (identification lemma for pure-denominator products) — [R] [rev; hypotheses completed in this revision]

**Setting.** F = Π_{j=1}^J D_j^{−e_j}, with every e_j ≥ 1 (no numerator factors), where
D_j = a_j(b) + Σ_iβ_{ji}(b)k_i^- − i0 w_j and w_j > 0. F_η is F with i0w_j replaced by iηw_j, η > 0.

**Hypotheses.**
- **(FR)_η**: (FR) holds for F_η for every η ∈ [0,η_0], with simple poles on the closing side, the same closing
  sides, and no coincident poles, for a.e. b. The closing side sign(w/β) is automatically independent of η.
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

Under (IL1)–(IL2) no zero-mode (k_i^+ = 0) contribution can arise. At finite η the set {k_i^+ = 0} is null, and
(IL2) excludes δ-like concentration as η → 0.

**Scope (round 2, confirmed in round 3).**
- (1) The lemma does **not** cover the composite Collins terms.
  - For C_{C_1} = T_1 + T_2, the η = 0 residue pieces are 1/(Ah_2) and −1/(Bh_2). At P = P′ = 1/√2, m² = 0.01,
    ε = 0.1 their moduli integrate over x > δ to 462.72, 1644.85, 4614.22 and 12072.96 for δ = 10⁻⁴, 10⁻⁸, 10⁻¹²,
    10⁻¹⁶, growing like δ^{−ε}/ε (`r2_triangle_identification.py` PART E; reproduced by reviews r3_1 and r3_2).
  - Written as one product with the numerator D_g, C_H violates |N_η| ≥ |N_0|.
- (2) For the triangle and the one-rung ladder, (FI) is now proven directly and exactly (Props B.2, B.3, C.4(e)), so
  the lemma is not needed there. It remains a general tool for pure-denominator integrands.
- (3) Remarks on the hypotheses.
  - (IL1): Minkowski power counting at fixed η makes it plausible for the triangle's Γ when 0 < ε < 1. The worst
    regions are the two-dimensional cones {k² = 0, p_i·k = 0}, contributing ∫R^{−1−2ε}ln²R dR, and it fails
    logarithmically at ε = 0. It is not proven.
  - (IL3): for propagator-only integrands whose external momenta can be chosen purely spatial (Euclidean region), this
    is the textbook Wick rotation at fixed η followed by dominated convergence. The triangle's kinematics always has
    Q² = (Q̃²+m²)²/Q̃² ≥ 4m², so it is never Euclidean, and (IL3) there would rest on analytic continuation in the
    external invariants (cf. Zimmermann 1968 for Minkowski power counting). It is not proven here and is not used.

---

### Lemma A.3 (tropical/LP certificate lemma) — [R] [rev]; (c) [new-final]

**Setting.**
- f = N/Π_kD_k in local coordinates y_i = e^{LX_i} (i = 1,…,n), with m² = e^{−L} and L = ln(1/λ²).
- N is a real polynomial in (y, m²). Its coefficients may depend on *frozen* variables confined to compact intervals
  in (0,∞).
- Each D_k is comparable on the cell to a positive-coefficient polynomial g_k, with explicit constants: at most 2^{deg}
  per factor for the frozen ranges [1/2,1] and [1,2], and at most (15/7)^{deg} for the sliver range [0.7,1.5].
- w is the vector of measure weights (the κ-weight is 1 − ε).
- For each monomial a = (a_1,…,a_n,a_m) of N:
  ψ_a(X) = ⟨a+w,X⟩ − a_m − Σ_k max_{b∈supp g_k}(⟨b,X⟩ − b_m).
- U is a polyhedron: the cell in normalized log coordinates.

**Hypothesis.** Every ψ_a has a bounded argmax face F_a on U.

**(a) Equivalence.** The hypothesis holds iff ψ_inf(r) := ⟨a+w,r⟩ − Σ_k max_b⟨b,r⟩ < 0 for every
r ∈ rec(U)∖{0}.

*Proof.* Since max(u+v) ≤ max u + max v, ψ_a(x+tr) ≥ ψ_a(x) + tψ_inf(r) for t ≥ 0.
- If ψ_inf(r) ≥ 0 for some r ∈ rec(U)∖{0} and x* ∈ F_a, then x*+tr ∈ U and ψ_a(x*+tr) ≥ max ψ_a. So the ray lies in
  F_a, which is unbounded.
- Conversely, F_a is a polyhedron. If it is unbounded, it contains a ray x*+tr with r ∈ rec(U)∖{0}. Along this ray
  ψ_a is eventually affine with slope ψ_inf(r), and it is constant on F_a, so ψ_inf(r) = 0. ∎

(This proof was in round 1 and was dropped in round 2; review r3_2 checked it.)

**(b) Statement.** ∫_U|f|Πy_i^{w_i−1}dy ≤ C L^d λ^{−2φ*}, with φ* = max_a max_Uψ_a and d = max_a dim F_a ≤ dim U.
With polynomial weights (1+L|X|)^j, which logarithmic insertions require, the power is L^{d+j}.

*Proof.*
1. Borinsky's tropical approximation (AIHPD 10 (2023) 635, Thms 8.A/8.B) gives two bounds.
   - |N| ≤ (Σ|c_a|)max_a y^a m^{2a_m}; frozen coefficients satisfy |c_a(u)| ≤ Σ_j|c_{a,j}|hi^j.
   - A positive-coefficient g_k satisfies g_k ≥ (min_b c_b)max_b y^b m^{2b_m}.
2. In log coordinates the integrand is therefore ≤ C L^n Σ_a e^{Lψ_a(X)} dX.
3. A Hoffman-type error bound for polyhedral concave functions gives max_Uψ_a − ψ_a(X) ≥ c·dist(X,F_a). This uses
   the hypothesis through (a).
4. A Laplace estimate gives ∫_U e^{Lψ_a} ≤ C e^{Lφ_a} L^{−(n−dim F_a)}. Finally e^{Lφ} = λ^{−2φ}. ∎

*Uniformity in ε.*
- ψ_a is affine in ε, so the LP value is convex in ε and the endpoint certificates bound every intermediate ε.
- Uniform constants follow from κ^{−ε} ≤ 1 + κ^{−ε_0} on [0,ε_0].

**(c) Implementation and its independent verification.**
- *Tooling* (`r1_lptools.py`, `r2_lptools.py`; archiving wrapper `r3_lptools.py`):
  - (i) an exact rational dual y and primal x with c·x = b·y are constructed; strong duality is asserted before the
    face bound is used;
  - (ii) the face bound is dim F_a ≤ (n+K) − rank(A_{S⁺}) with S⁺ = {i: y_i > 0}. Only these constraints are forced
    tight by complementary slackness. This is the round-2 repair of review r2_2 F4;
  - (iii) the recession check is exact: in 2D the recession cone is split into closed-quadrant pieces, and endpoints
    and tie points are evaluated;
  - (iv) frozen variables enter only as coefficients.
- *New in this revision (review r3_1 required fix 8, review r3_2 required fix 7).* Every piece record now stores the
  rational function it bounds (numerator, denominators), the local variables, frozen intervals, weights and cell
  constraints, the numerator support and the denominator supports.
- The archives `logs/r3_triangle_certificates_sc.json.gz` and `logs/r3_bubble_certificates_sc.json.gz` are
  re-verified by **`r3_archive_verify.py`**. That script imports no certificate-producing code. It:
  - recomputes the supports from the stored rational functions and checks sign-definiteness and the comparability
    constants;
  - rebuilds every LP;
  - checks exactly y ≥ 0, A^Ty = c, b·y + const = value, Ax ≤ b and c·x + const = value;
  - recomputes S⁺, the rank, the face bound, the exponent −2max_a value_a, the L-power, and the exact maximal
    recession slope with its own algorithm;
  - checks that every certified rational function equals the density it is claimed to bound, coded independently:
    the triangle items, remainder and sliver from Prop B.1, and the bubble pieces P0–P4, corner shells and u>1 pieces
    from the four-shell representation. The four-shell representation is itself checked symbolically against
    Prop B.1.
- *Results.*
  - Triangle: 58/58 piece records, 546/546 monomial certificates, 58/58 closed-form identities; maximal face bound 2;
    minimal exponents as in Thm B.5.
  - Log-weighted family: see Thm B.8.
- The recession check for n ≥ 3 is floating-point only; it is not used, because every cell here is one- or
  two-dimensional.

**Novelty.**
- The ingredients are known: Borinsky's tropical approximation, and polytope and region methods (Jantzen 2011;
  Semenova–Smirnov–Smirnov 2019; Gardi–Herzog–Jones–Ma–Schlenk 2023; Ma 2024; Arkani-Hamed–Hillman–Mizera 2022).
- Belitsky–Smirnov 2026, §4, use Newton polytopes and tropical geometry to *evaluate* region integrals of the same
  off-shell form factor; this is a different use.
- Their use to certify Collins' integral norms (CS1)–(CS3) appears to be new. The INSPIRE searches of reviews r1–r3
  found no prior instance.

---

### Lemma A.4 (light-cone positivity; scalar cubic models, massless internal lines) — [R] [rev]

**Hypotheses.**
- G is a connected graph of (M1) or (M2) without tadpoles.
- In case (b), every loop carries target plus momentum. This excludes the J–φ mixing and t-channel graphs.
- Kinematics: (a) as in (M1); (b) as in (M2) with x > 1.

**Statement.**
- For a.e. b, ρ_G is a finite sum over x^+-orderings of Π_lines(2l^+)^{−1}Π_states(E_st − Σ_{l∈st}l_T²/2l^+)^{−1},
  times a positive constant.
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
- There are no instantaneous terms, because the vertices are scalar. There are no zero modes, because every loop has
  at least two propagators depending on its k^- and non-constant plus momentum.
- Each energy denominator equals E_st − Σ with E_st < 0 and Σ ≥ 0. ∎

**Novelty.** Negativity of the light-cone energy denominators below threshold is classical. It is *analogous to* (round
3: not "equivalent to") the positivity of the Symanzik F polynomial for space-like invariants. Its use for (CS3^φ) is
new but modest.

### Corollary A.5 ((CS3^φ) for Γ) — [R, R_cond: (IRF), (LCE)] [statement corrected in this revision]

Let G satisfy the hypotheses of Lemma A.4 and (IRF). Given (LCE), (CS3^φ) holds for Γ = G:
∫_B|ρ_G|dμ_ε = |I_G| < ∞, uniformly in ε ∈ [0,ε_0].

*Proof.*
1. By the definite sign and (LCE), ∫|ρ_G| = |∫ρ_G| = |I_G|.
2. By (IRF), the positive parametric integrand converges absolutely.
3. For a ∈ (0,C] the bound a^{−s(ε)} ≤ a^{−s(0)} + a^{−s(ε_0)} holds for exponents s affine in ε. It bounds the
   integral uniformly by its values at the two endpoints. ∎

**Unconditional cases.** For the one-loop triangle (Prop B.1) and the one-rung DIS ladder (Prop C.4(c)), ∫ρ_Γ < ∞ is
computed directly. There (CS3^φ) for Γ holds with neither (LCE) nor (IRF) [R, R_PT]. Lemma A.2 cannot replace (LCE):
for a single-signed density, (IL2) *is* ∫|ρ_G| < ∞ (review r2_1).

**Withdrawn** (round 3; reviews r3_1, r3_2). Round 2 claimed that (CS3^φ) holds for Γ, uniformly in ε, for every
UV-finite graph satisfying the hypotheses — in (M1), all graphs without one-loop two-point subgraphs and without
tadpoles. Its proof took UV finiteness for finiteness. Prop A.6(a) gives a counterexample that satisfies every stated
hypothesis.

**Status of (IRF).**
- *Proven* for the one-loop triangle and the one-rung DIS ladder.
- *False* for the (M1) graphs of Prop A.6.
- *Expected* from soft power counting (Prop A.6(c),(d) and the standard IR power-counting theorem, cf. Lowenstein–Zimmermann
  1975; not proven here in this non-Euclidean but positive-F setting), for:
  - the planar and crossed ladder vertex graphs of (M1). For the two-loop planar vertex, the positive fibered density
    integrates numerically to the Usyukina–Davydychev value (§7.4);
  - all UV-finite (M2) graphs satisfying (b), e.g. every DIS ladder.

---

### Proposition A.6 (infrared structure of (M1) beyond one loop) — [R] for (a), (b); power counting for (c), (d) [new-final]

(M1) is massless and super-renormalizable ([g] = mass¹ in d = 4).

**(a) The kite counterexample.** Let G_kite be the three-loop vertex graph obtained from the triangle by inserting the
massless two-loop "kite" self-energy (a ψ loop with an internal φ rung) into the exchanged φ line.
- G_kite is connected and has no tadpole and no one-loop two-point subgraph. Every subgraph is UV finite (ω = 4L − 2I
  < 0; for the kite ω = −2). Every loop carries non-constant plus momentum. So G_kite satisfies all hypotheses of
  round-2 Cor 2.11.
- The kite is a homogeneous function of k² that is UV and IR finite at space-like k ≠ 0:
  Σ_2(k²) = K(ε)(−k²)^{−1−2ε}, with K(0) = 6ζ(3) times positive couplings.
- Hence G_kite = K(ε)×(the triangle with the exchanged line raised to the power ν = 3+2ε).
- The parametric representation of that triangle is
  Γ(ν+2−d/2)/Γ(ν) ∫_simplex α_g^{ν−1}F^{d/2−ν−2}, with F = α_1α_2Q² + m²α_g(α_1+α_2).
- At the soft corner α_1, α_2 → 0, F ≃ m²r with r = α_1+α_2. The corner contributes ∫r^{d/2−ν−1}dr, which is absolutely
  convergent iff ν < d/2 = 2−ε, i.e. ε < −1/3 here.
- The only pole is the corner pole at ε = −1/3 (Γ(ν+2−d/2) = Γ(3+3ε) is finite). Therefore the DR value of G_kite,
  continued from ε < −1/3, is **finite** at ε = 0, while the integral itself diverges for every ε ∈ [0,ε_0].
- Correspondingly, the effective fibered density is obtained by integrating the finite kite subintegral first and
  then closing the outer k^- contour on the D_1 pole (the Σ_2 cut and the D_g poles lie on the other side):
  ρ = K(ε)(P−x)^{2+2ε}/(A^{3+2ε}D̂_2) ≥ 0. It is not integrable at the corner (x,κ) → 0.
- At ε = 0 the proxy 1/(D_g³D_1D_2) has ∫_{x>δ}ρ_3 = 2.46·10⁸, 3.47·10¹⁰, 3.50·10¹², growing like 1/δ, while the
  triangle (n = 1) gives 21.83, 22.82, 22.83 (`r3_M1_infrared.py`, part (c)).
- Hence the step "∫|ρ_Γ| = |∫ρ_Γ| = I_Γ < ∞" of round-2 Cor 2.11 fails for G_kite.

**(b) Self-energy insertions.**
- The renormalized one-loop ψ-bubble on the exchanged φ (in DR: ν = 2+ε for the bare and ν = 2 for the counterterm
  part) violates ν < 2−ε at ε = 0.
- At ε = 0 the corner-cut integrals grow like ln(1/δ) (ν = 2) and like ln² with the renormalized logarithm
  (`r3_M1_infrared.py`, part (b): 5.6·10⁴, 1.0·10⁵, 1.5·10⁵ for ν = 2 and 6.0·10⁵, 1.3·10⁶, 2.3·10⁶ with the
  logarithm, at δ = 10⁻⁴, 10⁻⁶, 10⁻⁸).
- The same holds for a ψ self-energy on an internal ψ line that becomes soft (k → p_1).
- These divergences are positive in the parametric representation, and their coefficients are ∝1/m⁴ and
  ∝1/(m²Q²) respectively. So F^(2) of (M1) is **IR divergent at fixed m**, and F^(N) is IR divergent for N ≥ 2.
- This is the infrared problem of massless super-renormalizable theories (Jackiw–Templeton, PRD 23 (1981) 2291): the
  exact amplitudes are non-analytic in the coupling.

**(c) Soft power counting at fixed m.**
- Consider a set S of internal lines that can be simultaneously soft, with connected complement, V_S all-soft (cubic)
  vertices and n_a endpoints on non-soft vertices.
- Then 2I_S = 3V_S + n_a and L_S = I_S − V_S, so the infrared degree is ω_IR = 4L_S − 2I_S = n_a − V_S.
- A divergence is expected for ω_IR ≤ 0. Examples:

| soft subgraph | ω_IR |
|---|---|
| single soft φ (the triangle) | +2 |
| two soft rungs (planar or crossed two-loop ladder) | +4 |
| one-loop ψ-bubble on a soft φ | 0 |
| ψ self-energy on a soft ψ line | 0 |
| two-loop kite on a soft φ | −2 |
| soft ψ triangle with three soft φ legs on the external ψ lines (three loops, no self-energy insertion) | 0 |
| soft ψ box with four soft φ legs (four loops) | 0 |

- A hard or counterterm two-point insertion on a soft line (a constant of mass dimension two in (M1)) lowers ω by 4;
  this is the counterterm part in (b).
- "No self-energy subgraph" is therefore **not** sufficient for IR finiteness in (M1).

**(d) (M2) has no soft infrared problem.** In φ³₆ (d = 6), ω_IR = 6L_S − 2I_S = 2n_a > 0. MS-bar two-point insertions
are ∝k² and do not lower ω.

*Proofs.*
- (a): the parametric exponent computation, positivity, and the explicit corner integrals. The factorization of the
  kite subintegral uses its absolute convergence at space-like k ≠ 0.
- (b): the same, for ν = 2 and ν = 2+ε.
- (c), (d): power counting. Divergence for ω ≤ 0 follows from a lower bound of the positive parametric integrand on a
  neighbourhood of the corresponding face. Convergence for ω > 0 at all faces is the standard IR power-counting
  theorem, used here only as a heuristic.

Numerics: `r3_M1_infrared.py`, reproducing review r3_1 `r3_M1_infrared.py` and review r3_2 `c7_M1_IR.py`.

**Consequences.**
- Cor A.5 needs (IRF).
- Thm F.1 is restricted to IR-finite graph classes, and the full form factor of (M1) at N ≥ 2 is not covered.
- The round-2 open items "two-loop graphs with UV subdivergences" (O3) and "the full graph beyond the hybrid model"
  (O13) are *not open* in (M1): those graphs are IR divergent (§14, OQ3, OQ13, OQ16).

---

### Lemma A.7 (one-dimensional reduction of rung kernels, d = 6) — [R] [rev]

**Setup.**
- The parent has (v, K); the child has fraction z and transverse momentum k.
- v′ = zv + |k − zK|²/(1−z).
- κ = 1/(π²(1−z)v′²).

**Statement.** For every F ≥ 0:
- ∫d⁴k κF(v′) = (1−z)∫_{zv}^∞dt (t−zv)F(t)/t² ≤ (1−z)∫_{zv}^∞dt F(t)/t;
- for the projected parent (v = 0, K = 0), the right-hand side is (1−z)∫_0^∞dt F(t)/t.

*Proof.* Set l = k − zK. Then d⁴l = π²|l|²d|l|² and |l|² = (1−z)(t−zv). ∎

In d = 6−2ε the reduction carries the factors (1−z)^{1−ε} and (t−zv)^{1−ε}. With the measure d^dk/(iπ^{d/2}), the
rung-on-shell fibered measure is (1/Γ(2−ε))∫dξ/(1−ξ)∫dt t^{1−ε}(…)/v²; review r3_1 re-derived it from the R-pole
residue 1/(p^+(1−ξ)) and S = 1/v at that pole. The lemma is elementary and new only as a tool.

### Lemma A.8 (Vandermonde lemma) — [R] [new-final; review r3_2 suggestion]

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

### Lemma A.9 (continuation of subtracted Mellin integrals) — [R] [new-final]

**Setting.** f: (0,∞) → ℝ is measurable, f(0^+) exists, |f(t) − f(0^+)| ≤ Ct on (0,1], and |f(t)| ≤ Ct^{−1} on
[1,∞).

**Statement.** J(ε) = ∫_0^∞t^{−1−ε}[f(t) − f(0^+)]dt (absolutely convergent for 0 < ε < 1) and
K(ε) = ∫_0^∞t^{−1−ε}f(t)dt (absolutely convergent for −1 < ε < 0) are restrictions of the single function
∫_0^1t^{−1−ε}[f − f(0^+)] + ∫_1^∞t^{−1−ε}f − f(0^+)/ε, which is analytic on (−1,1)∖{0}.

*Proof.* Split both integrals at t = 1 and use ∫_1^∞t^{−1−ε} = 1/ε (ε > 0) and ∫_0^1t^{−1−ε} = −1/ε (ε < 0). ∎

With constants uniform in an outer parameter, the lemma passes under that integral by dominated convergence. It is used
in Prop C.4(e).

---
## 4. Part B — The one-loop off-shell triangle (M1)

**Notation.**
- Denominators, each with −i0: D_g = −k², D_1 = −(p_1−k)², D_2 = −(p_2+k)²; Γ = 1/(D_gD_1D_2).
- e_1 = m² + 2Pk^-, h_1 = 2Pk^-, t_1 = 2Pk^- − k²; e_2 = m² + 2P′k^+, h_2 = 2P′k^+, t_2 = 2P′k^+ − k².
- Note D_1 = e_1 − (m²/P)k^+ + D_g, D_2 = e_2 − (m²/P′)k^- + D_g and h_i − t_i = k² = −D_g.
- Approximators: T_S:(D_1,D_2)→(e_1,e_2); T_{C_1}: D_2→h_2; T_{C_2}: D_1→h_1; T_H:(D_1,D_2)→(t_1,t_2). Each also acts on
  already approximated denominators (T_He_i = h_i, T_St_i = h_i, T_{C_1}e_2 = h_2, …).
- Region set 𝓡 = {S < C_1, C_2 < H}. On each quark line the approximations form the semilattice {1,e,t,h}, so (Com)
  and (Abs) hold exactly.
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
- For 0 < x < P the contour picks up the D_1 pole; on the sliver, the D_2 pole. Every density part has a single
  residue.
- Every C_R satisfies (FR).

**Checks.**
- Symbolic residues (`t1`); the engine `lcpt.py` at 2000 points, maximum deviation 3·10⁻¹⁰ (`t7`); direct k^-
  integration at η = 10⁻⁷.
- Independent residue codes of reviews r1_2, r2_2 (maximum deviation 3.5·10⁻²¹) and r3_2.
- In the normalization du dκ with P = P′ = 1/√2, the densities are those of the table of `t4_triangle_certificates.py`.
  `r3_archive_verify.py` re-checks them symbolically.

**(CS3^φ).**
- ρ_Γ ≥ 0, and ∫ρ_Γ is finite uniformly in ε ∈ [0,ε_0]: the κ-integral is explicit (proof of Prop B.3).
- Each ρ_{C_R} is in L¹ exactly for 0 < ε < 1. The UV needs ε > 0; the endpoint x → P needs ε < 1.
- Every part of every ρ_{C_R} has a definite sign. Its absolute integral is given by the same κ-formulas K1, K2 and by
  Beta integrals of J0+J1 type, whereas the signed integrals involve J0−J1 (wording corrected in round 3).

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
  - For 0 < x < P, ρ = xm²/(Q̃²P²(κ+um²)(κ+um²(1−u))). By K2 this integrates in κ to g(um²)^{−ε}[(1−u)^{−ε}−1]/(Q̃²Pu).
  - With dx = Pdu, the region 0 < u < 1 gives g(m²)^{−ε}J0/Q̃².
  - For x > P, ρ = −1/(Q̃²uP(κ+um²)), which gives −g(m²)^{−ε}J1/Q̃².
  - With the factor 1/Γ(1−ε), C_{C_1} = Γ(ε)(m²)^{−ε}(J0−J1)/Q̃² = Γ(ε)B(−ε,1−ε)(m²)^{−ε}/Q̃².
- *C_{C_2}.*
  - The x > 0 part, −1/(Pe_2(e_2+κ)), gives −g(m²)^{−ε}J1/Q̃².
  - On the sliver put u′ = w/a ∈ (0,1). Then P′w = m²u′ and (a−w)P′w/a = m²u′(1−u′), and by K2 the κ-integral is
    g(m²u′)^{−ε}[(1−u′)^{−ε}−1]/(Pm²u′).
  - With dx = (m²/2P′)du′ the sliver gives g(m²)^{−ε}J0/Q̃². Hence C_{C_2} = C_{C_1}.
- *C_S.* K1 gives g(um²)^{−ε}/(P(m²+Q̃²u)). Then the substitution u = m²s/Q̃² gives C_S = g²(m²)^{−2ε}(Q̃²)^ε/(Γ(1−ε)Q̃²).
- *C_H.*
  - For 0 < x < P, with h_2 = Q̃²u, K2(h_2, h_2(1−u)) gives −g(Q̃²)^{−1−ε}J0.
  - For x > P, K1 gives g(Q̃²)^{−1−ε}J1.
  - Hence C_H = −Γ(ε)B(−ε,1−ε)(Q̃²)^{−1−ε}.
- Finally use Γ(ε)Γ(−ε) = −Γ(1+ε)Γ(1−ε)/ε².

**Proof, covariant side** (whole integrand; §1.4). The l-integrals use
∫d^dl/(iπ^{d/2})(−l²+Δ)^{−n} = Γ(n−d/2)Γ(n)^{−1}Δ^{d/2−n} and the corresponding formula for l²/(−l²+Δ)^n.
- *C_S* = 1/(D_ge_1e_2).
  - Cheng–Wu: 1/(D_ge_1e_2) = 2∫_0^∞∫_0^∞dλ_1dλ_2[D_g+λ_1e_1+λ_2e_2]^{−3}.
  - Here D_g+λ_1e_1+λ_2e_2 = −(k−v)² + Δ, with v = (λ_1P, λ_2P′, 0) and Δ = λ_1λ_2Q̃² + m²(λ_1+λ_2).
  - So C_S = Γ(1+ε)∫∫(λ_1λ_2Q̃²+m²(λ_1+λ_2))^{−1−ε}. The λ_2-integral is (m²λ_1)^{−ε}/(ε(λ_1Q̃²+m²)), and the
    λ_1-integral gives the closed form.
- *C_{C_1}* = (e_1−D_1)/(D_gh_2D_1e_1).
  - Use 6∫_0^1dx∫∫dλ_1dλ_2[xD_1+(1−x)D_g+λ_1h_2+λ_2e_1]^{−4}.
  - The combined denominator is −(k−v)² + Δ, with v^+ = P(x+λ_2), v^- = λ_1P′ − xm²/2P and
    Δ = (x+λ_2)(m²(1−x)+Q̃²λ_1).
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
- `r2_triangle_identification.py`, PARTS A–C: sympy.
- PART D: direct 2D fibered quadrature without the κ-formula, relative agreement 10⁻⁷–10⁻⁵.
- Independent re-derivations: review r2_1 (36–61 digits), review r2_2 (sympy), review r3_1, review r3_2 (2D
  quadrature, 3·10⁻¹¹–5·10⁻⁷).

**Remarks.**
- In the covariant decomposition C_H = [massless on-shell triangle] − 1/(D_gt_1h_2) − 1/(D_gh_1t_2) + 1/(D_gh_1h_2),
  the last term is exactly boost invariant with zero ε-weight. DR does not regulate it; only the whole C_H has a
  value.
- **Withdrawn** (round 2): the wording "massless on-shell triangle plus scaleless terms".

**Positioning (round 3, review r3_1).** The four closed forms are the known region values of the off-shell triangle:
hard, collinear and ultrasoft regions. See Smirnov, *Applied asymptotic expansions* (2002); Belitsky–Bork–Smirnov 2025;
Belitsky–Smirnov 2026, App. A.1, in their normalization T_11^h, T_11^{c_i}, T_11^{us}. **New** is only the
*fibered-side* identification: the absolutely convergent k^--residue integrals of the Collins terms, which include
their zero-bin subtractions (e.g. C_{C_1} = T_{C_1}Γ − T_{C_1}T_SΓ), reproduce these values exactly without any
convention for scaleless integrals.

### Proposition B.3 (exact identification for Γ) — [R, R_PT] [new-final; closes round-2 open item O15]

For every ε ∈ (−1,1), the fibered value of Γ equals its covariant value
I_Γ = Γ(1+ε)∫_simplex F^{−1−ε}, F = x_gm²(x_1+x_2) + x_1x_2Q².

More precisely, let u = x_1 − τx_2 (τ = m²/Q̃², units Q̃ = 1; this is the light-cone variable k^+/P of the
α-representation). Then:
- the main part 0 < k^+ < P equals the covariant integral over {x_1 > τx_2};
- the sliver equals the covariant integral over {x_1 < τx_2}.

**Proof.**
1. *Main part.* Prop B.1 gives ρ_Γ = (1−u)/[P(1+τ)(κ+u(1−u)m²)(κ+(1−u)(m²+u))], 0 < u < 1. Use a Feynman parameter y
   and ∫_0^∞dκ κ^{−ε}(κ+C)^{−2} = Γ(1−ε)Γ(1+ε)C^{−1−ε}; Tonelli applies, since all integrands are positive. This
   gives
   fib_main = Γ(1+ε)(1+τ)^{−1}∫_0^1du∫_0^1dy (1−u)^{−ε}[m²(1−y+yu) + (1−y)u]^{−1−ε}.
2. On {x_1 > τx_2} substitute x_2 = (1−u)z/(1+τ), x_1 = u + τx_2 (Jacobian (1−u)/(1+τ)). Then x_g = (1−u)(1−z) and
   F = (1−u)[m²(u+(1−u)z) + zu]. With z = 1−y the two integrals coincide.
3. *Sliver.* Prop B.1 gives, with s = w/a ∈ (0,1), ρ_Γ = (2s/(2P(1+τ)))/[(κ+m²s(1−s))(κ+m²s(1+τ(1−s)))].
   The same steps give
   fib_sl = Γ(1+ε)τ(1+τ)^{−1}m^{−2−2ε}∫ds dy s^{−ε}[1 − ys + τ(1−y)(1−s)]^{−1−ε}.
4. On {x_1 < τx_2} substitute x_1 = τsv/(1+τ), x_2 = 1 − s + sv/(1+τ) (Jacobian τs/(1+τ)). Then x_g = s(1−v) and
   F = τs[1 − s(1−v) + τv(1−s)]. With y = 1−v and m² = τ the two integrals coincide.
5. All integrals converge absolutely for −1 < ε < 1. ∎

**Checks.**
- `r3_FI_exact.py`, part (1): every algebraic step in sympy — the two maps, Jacobians and F-factorizations, and the
  closed-form densities in (u,κ) and (s,κ) re-derived from the round-2 formulas.
- Part (2): direct quadratures. The fibered main part in (u,z)-form reproduces the round-2 value 13.3963941598142 of
  review r3_2. The sliver forms agree to quadrature accuracy. The fibered total 15.5610705037585 at (P,P′,m²,ε) =
  (0.8,1.3,0.1,0.3) equals the covariant value of reviews r2_1, r3_2 (relative 3·10⁻¹⁷).
- Direct quadratures of the covariant integral over the two simplex sub-regions need breakpoints at both soft corners.
  With them they agree with the fibered main and sliver parts to 7·10⁻⁹ and 5·10⁻⁸ at (0.8,1.3,0.1,0.3), and to
  1·10⁻¹¹ and 2·10⁻¹⁰ at (0.8,1.3,0.02,0.05). The totals agree to all 16 printed digits.

**Consequence.** (FI) holds for Γ and, by Prop B.2, for all four C_RΓ: every value in Thm A.1(iii) is identified for
the triangle. Lemma A.2, with its unproven (IL1) and (IL3), is not needed. **Withdrawn:** the round-2 premise
"(ID)_Γ" of the integrated corollary.

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
  - ∫ρ_Γ(sliver) = 1.644934 at λ² = 10⁻⁶;
  - the sliver remainder is −1.99979λ² (λ² = 10⁻⁴) and −2.00000λ² (λ² = 10⁻⁶) (`t2b`; reproduced by review r1_2).
- Exact LP certificates of the sliver give λ² at ε = 0 and λ^{9/5} at ε_0 = 1/10, with recession slopes −1/2 and −9/20.
- New, elementary.

### Theorem B.5 ((CS1^φ)–(CS3^φ) for the triangle on the natural cover) — [R, R_PT], computer-assisted [rev; archive re-verified in this revision]

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
  exponents 8/5 and 9/5; uniformity follows from κ^{−ε} ≤ 1 + κ^{−ε_0}.
- (iii) (CS3^φ) holds (Prop B.1). (FR) holds for Γ and every C_RΓ.
- Fibered conclusion (Thm A.1(i),(ii)): ∫|ρ_r|dμ_ε ≤ Cλ²L² at ε = 0, and ≤ C(λ²L² + λ^{8/5}) uniformly on (0,1/10].

**Evidence.**
- Exact primal–dual optimal pairs; corrected recession checks (maximal slope −1/2 at ε = 0 and −9/20 at ε_0).
- Frozen variables are coefficients; comparability constants ≤ 2^{deg}, and ≤ (15/7)^{deg} on the sliver.
- The global remainder cells r_I, r_II, r_III and the sliver sub-domains A/B are certified at λ².
- At θ = 2 the item (CS1)_H coincides with the global remainder certificate.
- 58 piece records and 546 monomial certificates, regenerated self-contained (`r3_triangle_recert.py`) and re-verified
  by `r3_archive_verify.py` (Lemma A.3(c)): all checks pass.
- Exact face bounds: 0, 1, 2 for 251, 207, 88 certificates. The L-power L^{≤2} is the trivial bound for
  two-dimensional cells.

**Optimality of the λ-exponent** (cover family s = λ^θ, θ ∈ (0,2]).
- The certified exponent is θ (exactly for θ = 1, 3/2, 19/10, 2).
- Lower bound: ∫_{U_S}ρ_{C_{C_1}} ≥ s/4, since both A and B are ≤ 2um² on U_S.
- So no cover in this family has a better item exponent than θ = 2.
- The (CS1)_{C_1} norm is ≈ (θ/2)sL for θ < 2, and 1.36, 1.41, 1.43, 1.44 sL at θ = 2 for λ² = 10⁻⁴…10⁻¹⁰
  (`r1_theta2_lower.py`).

**Relation to App. N.** The fat neighbourhoods λ^β (β < 1, β_S < β_C) of `def:method-neighbourhoods` and
`lem:appN-beta` are sufficient-condition choices of the general envelope argument. For the triangle, natural-scale
covers give the optimal exponent once the grouped objects are computed explicitly. This is a sharpening, not an error
correction.

New: the integral-norm verification of (CS1)–(CS3) for this graph.

### Corollary B.6 (the integrated subtraction theorem for the triangle) — [R, R_PT], computer-assisted [new-final for the removal of the premise]

Uniformly in ε ∈ (0,1/10]:
- |I_Γ − Σ_{R∈𝓡}I_{C_RΓ}| ≤ ∫|ρ_r|dμ_ε ≤ C(λ²L² + λ^{8/5});
- each I_{C_RΓ} converges absolutely and equals the closed form of Prop B.2.

*Proof.* Thm B.5, Thm A.1(iii), and (FI) for all terms (Props B.2, B.3). ∎

In round 2 this corollary was [R, R_cond] with the single premise (ID)_Γ; Prop B.3 removes it. Together with the exact
NLP remainder of Prop B.7, this is the content of slot X2a (§11).

### Proposition B.7 (remainder: norm versus integral)

- **Rigorous:** ∫|ρ_r| ≤ Cλ²L² at ε = 0 (Thm B.5).
- **Exact integrated remainder** (known; reproduced). In units Q̃ = 1, ρt = m² exactly, so:
  - ∫r = Φ^(1)(t,t)/Q² − (L̃²+π²/3) = 4Li_2(−m²)/(1−m⁴) + (L̃²+π²/3)m⁴/(1−m⁴) = −4λ² + O(λ⁴L̃²);
  - equivalently, in Q units: −4m²/Q⁴ + (m⁴/Q⁶)(L_Q² − 15 + π²/3) + O(m⁶L²/Q⁸).
  - The residual is ≈ 4.7, 5.2, 5.4 × m⁶L² for m² = 10⁻³…10⁻⁵ (reviews r2_2, r3_1).
  - The fibered integral matches Usyukina–Davydychev to 10⁻¹¹ (`t2b`). By Props B.2–B.3, the subtracted
    L̃²+π²/3 is the sum of the identified Collins terms.
- **Numerical [P]:**
  - ∫|ρ_r| = c(λ)λ²L with c = 3.53, 3.79, 3.89, 3.93, 3.95, 3.96, 3.962 for λ² = 10⁻²…10⁻⁸;
  - 91.41525λ² at λ² = 10⁻¹⁰ (review r1_1);
  - hence ∫|ρ_r| ≈ λ²(4L̃ − c′) with c′ → 0.69, one logarithm more than the integrated remainder.
  - Sign structure: soft box −1.04L, C_1 strip −0.54L, k^+ > P strip +0.95L, hard part +0.48L (`t2c`). The monomial
    majorant is sharp to a factor 1.1–1.3 (`t3`).
- A Table-5-type comparison of I with L²+π²/3 in Q² tests the leading power of the exact integral, not the Collins
  remainder in Q̃ (ERR-m25).

### Theorem B.8 (log-weighted triangle family) — [R, R_PT], computer-assisted, for each fixed j [rev for the mathematics; relabelled in this revision]

**Integrand family (relabelled; reviews r3_1 and r3_2).**
- Γ^(j) = ln^j(D_g/μ²)/(D_gD_1D_2), μ = Q̃, j = 0, 1, 2, …
- Hybrid scheme: outer measure d = 4−2ε with the fixed four-dimensional weight ln^j(D_g).
- The family weights the triangle with a power of the logarithm of the exchanged line's virtuality. It *models* the
  insertion structure of a large-β_0 bubble chain in a theory whose self-energy is ∝k²ln k² (the transverse gauge
  vacuum polarization, or φ³₆), grafted onto the (M1) triangle.
- **It is not a graph class of (M1).** In (M1), [g²] = mass² and Π_R(k²) = (g²/16π²)(c − ln(−k²/μ²)) carries no
  factor k². So the MS-bar renormalized j-bubble chain is ∝ g^{2j}[c − ln(−k²/μ²)]^j/(−k²)^{j+1}, which is IR
  divergent at fixed m for j ≥ 1 (Prop A.6(b)). Its d-dimensional form is ∝ g^{2j}(−k²)^{−1−j(1+ε)}×(poles), not
  (−k²)^{−jε}×(poles).

**Lemma B.8.1** [R, R_def]. The approximators act only on D_1, D_2 and the external momenta, never on D_g. Hence
C_RΓ^(j) = ln^j(D_g)·C_RΓ pointwise, with the region set of the triangle.

**Four-shell representation** (0 < u < 1, v = 1−u, P = P′ = 1/√2).
- ρ_r^(j) = Σ_s l_s^jT_s, where l_s = ln D_g on the shell s ∈ {D, e, t, h}.
- The shells are R_D = (um²v+κ)/v, R_e = um²+κ, R_t = κ/v, R_h = κ.
- T_D = (v/D_G − 1/u)/(um²v+κ), T_e = m²/(u(m²+u)(um²+κ)), T_t = 1/(u(uv+κ)),
  T_h = 1/((m²+u)(m²+u+κ)) − 1/(u(u+κ)), with D_G = (m²+u)(v(1+m²)+κ) + κv.
- The k^- contour closes away from the ln D_g cut in every range.
- Σ_sT_s equals the triangle remainder density for 0 < u < 1, and T_e + T_h equals it for u > 1 (checked symbolically
  in `r3_archive_verify.py`).

**Lemma B.8.2 (rectangle rule, exact).**
- l_D − l_e − l_t + l_h = δ = ln(A/B), with |δ| ≤ min(u²m²/(um²v+κ), CL(1+|X|));
- a = l_e − l_h ∈ [0, min(um²/κ, CL)] and b = ln(1/v) ∈ [0, min(u/v, CL)];
- hence ρ^(j) = l_h^jρ_r^(0) + Σ_{n≥1}C(j,n)l_h^{j−n}[a^n(T_D+T_e) + b^n(T_D+T_t) + ((a+b+δ)^n−a^n−b^n)T_D].

**Single-shell structure.**
- On the sliver, Γ^(j) and C_{C_2}^(j) are both D_2-residues, so ρ_r^(j) = l_{sl}^jρ_r^(0) exactly.
- For 1 < u ≤ 2: C_S and C_{C_1} lie on the e shell, C_{C_2} and C_H on the h shell, and Γ = 0.

**Theorem.** On the natural cover of Thm B.5, for each fixed j, every (CS1)/(CS2) item and ∫|ρ_r^(j)| satisfy:
- ≤ C_jλ²L^{j+2} at ε = 0;
- ≤ C_j(λ²+λ^{8/5})L^{j+2} uniformly on (0,1/10].
(CS3^φ) holds for 0 < ε < 1 in the hybrid sense: the logarithms do not affect convergence, but the individual C_R need
ε > 0.

**Evidence.**
- 2986 piece records and 70,373 exact monomial certificates (`r3_bubble_recert.py`).
- Independently re-verified by `r3_archive_verify.py`: all LP checks pass for all records; 2938 closed-form identities
  pass (pieces P0–P4, corner shells, u > 1 pieces). The 48 composite "items" records are verified at the LP level only.
- Remainder 0 < u < 1, 270 cells: minimum exponent 2 at ε = 0 and 8/5 at ε_0, with worst slopes −1/2 and −9/20. At
  ε_0, piece P3 uses the trivial alternative in 9 deep cells.
- Remainder u > 1, 60 cells: exponents 2 and 9/5, slopes −1/2 and −11/20.
- Items: 2 and 8/5.
- Corner {v ≤ λ⁶, κ ≤ λ⁸}: bounded shell by shell, ∫_{corner}|T_s| ≤ Cλ^{a_s}L^k with a_D = 8, a_e = 14, a_t = 8,
  a_h = 16 (`t15f`); the archived corner minimum is 8 at ε = 0 and 36/5 at ε_0.
- Sliver and part III: the triangle certificates times |l|^j ≤ (C(1+L|X|))^j.
- Maximal face bound 2.

**Growth in j.** C_j ≳ 2j!/L_0^{j+2}: the u > 1 UV tail gives ∫_1^∞(ln κ)^jκ^{−2}dκ = j!. No statement about the summed
family is possible. The renormalon interpretation applies only within the large-β_0 analogy, not to (M1).

**Numerics [P]** (`t5`): ∫r^(j) ≈ −4λ²(−L)^j; at λ² = 10⁻¹⁰ the norms are 3.97λ²L (j = 0), 4.84λ²L² (j = 1) and
6.58λ²L³ (j = 2). The round-0 script `t15c` is invalid (its LPs are unbounded) and is not used.

**Withdrawn** (round 3):
- the identification of Γ^(j) with the MS-bar renormalized bubble chain of (M1);
- "the true d-dimensional chain is (−k²)^{−nε} times poles";
- the renormalon reading for (M1);
- the entry "(F1) for the bubble-chain class" in the (M1) status list of Thm F.1;
- the round-1 "model assumption" that Γ^(j) reproduces the leading regions of the full (j+1)-loop graph of (M1),
  which is moot.

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

Tadpoles vanish in massless DR, and external self-energies are amputated. Graphs (iv) and (v) were missing in round 0.

**Definitions and scope.**
- Graph (v) is ∝1/t at t = 0, so it is infinite in the forward limit. It does not depend on x and has no discontinuity
  in ω. The forward amplitude is therefore *defined* modulo x-independent terms: the observable is the x-dependent part,
  equivalently the discontinuity. This removes (v).
- Graphs (iv) and (v) contain q^+ = 0 loops. These are pure zero modes in this frame; they violate (FR) and are treated
  outside the fibered framework. In (iv) the loop is a renormalized insertion Π_R(q²).
- In QCD the analogues of (iv) and (v) vanish by colour, since a single gluon attached to a colour-singlet loop gives
  Tr t^a = 0.

**Statements.**
- (i) The collinear region is leading: Prop C.4 (the u channel is analogous, with A′ = 1+ξ/x ≥ 1).
- (ii), (iii) These graphs are UV divergent: ω = 0 for the vertex and ω = 2 for the self-energy. "(CS3) trivial"
  (round 0) is withdrawn.
  - Unrenormalized, (1−T_H)Γ = S(P)[f(m²)−f(0)] + [S(P)−S(P̂)]f(0) diverges at O(m²): ∫_{|l|<Λ}|ρ| = 25.4, 43.8,
    62.2 m² for Λ = 10², 10⁴, 10⁶ (m² = 10⁻³).
  - *Renormalization.* Integrand-level BPHZ (`asm:appN-uv`) with subtraction points that match the plus components:
    - *Vertex.* Subtract the same graph at a fixed space-like point (p_0,q_0) with p_0^+ = p^+, q_0^+ = 0 and fixed
      invariants p_0² = −μ², q_0² = −Q_0², (p_0+q_0)². The integrated counterterm is a constant times the tree vertex.
      Because the fibered supports agree, the subtraction improves the UV pointwise, to ρ ~ |l|^{−6}.
    - *Self-energy.* After the shift l → l − zP_T the density is (1/π²)/(|l|² + z(1−z)s), with s = −P². Subtract its
      first-order Taylor polynomial in s at s_0. This is a Taylor expansion in P^- at fixed P^+ and P_T, with
      integrated counterterm Σ(s_0) + (s−s_0)Σ′(s_0). The result is g(s) = (c−c_0)²/(π²(a+c)(a+c_0)²), with
      c = z(1−z)s.
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
- *(iv).* These graphs depend on the target only through S(p+q). The remainder is exactly
  [S(P)−S(P̂)]D(q)Π_R(q²) = O(λ²).

**Numerics** (`r1_dis_Honly.py`; x = 2, μ² = 1, x_0 = 2):
- renormalized vertex norm 5.18, 6.32, 7.38, 8.43, 9.48, 10.53 m² for m² = 10⁻²…10⁻⁷, i.e. ≈ (0.46L+3.1)m², with
  definite sign and independent of the cutoff;
- self-energy norm 0.835 m² at m² = 10⁻² and 0.871 m² for m² ≤ 10⁻⁴. Review r2_2 reproduced 0.87123 m² analytically
  from Σ_R(s) = (1/6)[s ln(s/s_0) − s + s_0].

### Lemma C.2 (DIS ladders: light-cone representation and Collins structure) — [R] for the fibered densities [rev]

**Setup.** The n-rung forward ladder is L_n = ∫Π_jd⁶k_j/(iπ³)·H_0(k_n)Π_jS(k_j)²R(k_{j−1}−k_j), with k_0 = p, in the
frame q^+ = 0 and x > 1. Here S, R and H_0 are the spine, rung and hard propagators.

**Statements.**
- (a) *Support.* The iterated k^- integrals (top-down, j = n, …, 1) vanish unless 0 < k_n^+ < … < k_1^+ < p^+.
- (b) *Rungs on shell.* On the support, close each k_j^- contour on the side of the single rung pole. This gives
  ρ_c = Π_i[π^{−2}(1−z_i)^{−1}(v_i^(c))^{−2}]H^(c_{n+1}), where:
  - c ∈ {0,1}^{n+1}; c_i = 1 means that the parent of level i is projected, and c_{n+1} = 1 means that the hard factor
    is projected;
  - v_i = z_i(1−c_i)v_{i−1} + |k_{iT} − (1−c_i)z_ik_{i−1,T}|²/(1−z_i), with v_0 = m²;
  - H^(0) = 1/(A + v_n + 2k_{nT}·q_T), H^(1) = 1/A, A = 1 − ξ_n/x.
- (c) *Invariants.* v ≥ ξm² + |K|²/(1−ξ) for unprojected chains, and v ≥ |K|²/(1−ξ) for all chains. This is
  Cauchy–Schwarz with weights z(1−ξ) and 1−z, which sum to 1−zξ. Hence H^(0) > 0.
- (d) The approximators T_{R_j} commute: T_{R_j} projects s_j in factor j+1, and T_{R_0} = T_H: p → p̂; π(s) depends
  only on ξ. Hence r = Σ_c(−1)^{|c|}ρ_c = U_0(s_0), with U_n(s) = h(s) − h(πs) and
  U_{j−1}(s) = κ(s→s′)U_j(s′) − κ(πs→s′_0)U_j(s′_0).

**Proof of (a), (b) (pole sides).** A factor (βk_j^- + a − i0w) has its pole in the upper half plane iff w/β > 0.
1. At level j, the spine factors S(k_j) and the hard and propagated factors depend on k_j^- with coefficient −2k_j^+
   and positive weight. After the upper rung poles are substituted, the propagated factors acquire the weight
   k_{j−1}^+/(k_{j−1}^+ − k_j^+) > 0.
2. The rung R(k_{j−1}−k_j) depends on k_j^- with coefficient +2(k_{j−1}^+ − k_j^+) and weight 1.
3. Three cases:
   - If k_j^+ > k_{j−1}^+ (> 0), every pole is in the lower half plane; closing upward gives 0.
   - If k_j^+ < 0, every pole is in the upper half plane; closing downward gives 0.
   - If 0 < k_j^+ < k_{j−1}^+, the single rung pole is the only upper pole, and closing upward picks it up.
4. The k_j^- integrands decay like |k_j^-|^{−2} or faster, and the boundary values of k_j^+ are null sets.
5. Substituting the rung poles gives (b). (c) and (d) are algebra. ∎

**Validation.**
- n = 1: the fibered value equals the covariant value *exactly* (Prop C.4(e1)); numerically to 10⁻¹³ (`t6`).
- n = 2: the structure was checked numerically (`t11`).

The structure is known (`prop:appN-ladder`; Ex. D.48 of the source); it is made precise here.

### Lemma C.3 (hard-factor lemma) — [R] [rev]

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
- (ii) Use ∫_0^πsin²θ dθ/(a + b cos θ) = π(a − √(a²−b²))/b², with a = d̄ > |b| = 2|l| by (i). The bound on d̄ follows
  from v − 2|K| ≥ −(1−ξ).
- (iii) Differentiate (ii) with respect to a and use a² − b² ≥ a·d_min.
- (iv) Use (1−z)/(1−z+zξc_x) ≤ 1. ∎

The closed-form S³ average was checked by quadrature to 12 digits (`r1_ladder1_analytic.py`). For d = 6−2ε the S³
averages become S^{3−2ε} averages, ⟨1/(a+b cos θ)⟩ = (1/a)₂F₁(1/2,1;2−ε;b²/a²) = 2/(a+r)·₂F₁(1,ε;2−ε;(a−r)/(a+r)),
r = √(a²−b²). This was checked against direct quadrature in `r2_ladder1_identification.py`. The ε > 0 analogues of
(ii)–(iv) are not proven.

### Proposition C.4 (one-rung DIS ladder) — (a)–(d) [R, R_PT] at ε = 0 [rev]; (e) see grades below

**Hypotheses.** (M2), x ≥ x_0 > 1, Q = 1, λ = m ≤ c_x/8.

**Notation for (a)–(d)** (ε = 0).
- ρ_r(z,k) = κ_1(h_1−ĥ) − κ_0(h_0−ĥ), with k ∈ ℝ⁴ the transverse momentum.
- κ_1 = 1/(π²(1−z)v′²) with v′ = zm² + |k|²/(1−z); κ_0 is the same with v′_0 = |k|²/(1−z).
- h_1 = 1/(A+v′+2k·q), h_0 = 1/(A+v′_0+2k·q), ĥ = 1/A, A = 1 − z/x.
- σ := v′_0 and δ := zm² = v′ − v′_0, so d⁴k = π²(1−z)²σdσ after the angular average.
- All norms are ∫_0^1dz∫_{ℝ⁴}d⁴k|·|: the ε = 0 fibered measure of (M2), with the 1/π² inside the kernels. The constant
  c_1(x) refers to this measure (round 3).
- *Regions:* B = {σ ≤ δ} and A = {σ > δ}.

**Claims.**
- (a) ∫dz d⁴k|ρ_r| ≤ C(x)λ.
- (b) On the cover U_{R_1} = {v′ ≤ λ²}, U_H = complement, all items are ≤ C(x)λ.
- (c) (CS3^φ): ρ_Γ = κ_1h_1 ≥ 0 is integrable uniformly in ε (UV ~|k|^{−6}). ρ_{C_{R_1}} = κ_1ĥ and
  ρ_{C_H} = κ_0(h_0−ĥ) are integrable only for ε > 0 (logarithmic UV divergence).
- (d) ∫|ρ_r| = c_1(x)λ + O(λ²L), with c_1(x) = 4∫_0^1dξ ξ^{1/2}(1−ξ)^{3/2}/(1−ξ/x)². Values: c_1(2) = 1.262984,
  c_1(1.3) = 1.936673, c_1(5) = 0.924158. The coefficient was first derived in review r1_1.

**Proof of (a).**
1. *Positivity.* For |k| ≤ c_x/4, A + v − 2|k| ≥ c_x/2 for every v ≥ 0. For all k, A + v′_0 + 2k·q ≥ zc_x
   (Lemma C.3(i)).
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
   ⟨h_1⟩ ≤ 2/(c_x+σ) and ⟨h_0²⟩ ≤ (2/d̄²)(1 + (d̄/(zc_x))^{1/2}), with d̄ ≥ c_x + σ. The contribution is
   ≤ C(δ + δz^{−1/2}).
6. Integrating over z gives ∫|ρ_r| ≤ C(x)m. ∎

**Proof of (b).**
- (CS1)_{R_1} = κ_1(h_1−ĥ) on U_{R_1}, where |k| ≤ λ and |h_1−ĥ| ≤ c(λ²+2λ). Since
  ∫_{v′≤λ²}d⁴kκ_1 ≤ (1−z)ln(1/z), it is ≤ 3cλ(1−z)ln(1/z).
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
     |R_2(s_1) − R_2(s_0)| ≤ Cδ(v′_0 + δ + 2|k|). On region B use direct bounds. Altogether
     ≤ Cδ(1 + L + ln(1/(z(1−z)))).
3. *On |k| > c_x/4:* ∫|ρ_r| ≤ C(δ + δz^{−1/2}) by step 5 of (a), and ∫|odd| ≤ C(1−z)^{3/2}δ/c_x.
4. Since |∫|a+b| − ∫|a|| ≤ ∫|b|, integrating over z gives |∫|ρ_r| − c_1λ| ≤ C(x)λ²L. ∎

**Numerics** (`r2_ladder1_even.py`, x = 2):
- ∫|odd|/λ = 1.262937…1.262979;
- ∫|rest|/(λ²L) = 0.491, 0.431, 0.401, 0.383, 0.371;
- (∫|ρ_r| − c_1λ)/(λ²L) = −0.076…−0.024 for m² = 10⁻²…10⁻⁶;
- `t6b` gives 1.26329 at m² = 10⁻⁷.

**(e) Identification of the fibered and covariant values** (d = 6−2ε; fibered measure
(1/Γ(2−ε))∫dξ/(1−ξ)∫dt t^{1−ε}(…)/v², t = |k|², v = ξm² + t/(1−ξ); c = c_x).

- **(e1) Γ** — [R] [new-final]. For −1 < ε < 1 the fibered value equals I_Γ exactly.
  1. By §1.2, ∫dt t^{1−ε}⟨F⟩ = (Γ(2−ε)/π^{2−ε})∫d^Dk F with D = 4−2ε. Hence the fibered value is
     π^{−(2−ε)}∫dξ(1−ξ)²∫d^Dk/((|k|²+μ_0²)²(|k+p|²+M_1²)), with μ_0² = ξ(1−ξ)m², p = (1−ξ)q and
     M_1² = ξ(1−ξ)(c+m²).
  2. A Euclidean Feynman parameter (Tonelli) gives Γ(1+ε)∫_0^1dξ(1−ξ)^{1−ε}∫_0^1dy y[yξm² + (1−y)ξ(c+m²) +
     y(1−y)(1−ξ)]^{−1−ε}.
  3. The covariant value is Γ(1+ε)∫_simplex x_1[x_2(x_1+x_3)m² + x_3(x_1+x_2c)]^{−1−ε}.
  4. The map x_2 = ξ, x_1 = (1−ξ)y, x_3 = (1−ξ)(1−y) (Jacobian 1−ξ) carries one integral onto the other.
  - Checks: `r3_FI_exact.py`, symbolic step, and quadratures to 3·10⁻¹³ and 5·10⁻¹⁰.
- **(e2) C_{R_1}** = S²R(p−k)Ĥ, with Ĥ = 1/(Q² − 2q^-k^+) — [R] [rev]. Fibered value = covariant value =
  Γ(ε)∫_0^1dξ(1−ξ)^{1−ε}(ξm²)^{−ε}/(Q²(1−ξ/x)), exactly.
  - Fibered: ∫_0^∞dt t^{1−ε}/v² = (1−ξ)^{2−ε}(ξm²)^{−ε}Γ(2−ε)Γ(ε).
  - Covariant: Feynman/Cheng–Wu with the shift by λn (n² = 0) gives Δ = y(1−y)m² + λQ²(1−(1−y)/x); the λ-integral
    gives (y(1−y)m²)^{−ε}/(εQ²(1−(1−y)/x)), and ξ = 1−y.
  - Values at x = 2: 11.27248142379893 (m² = 0.01, ε = 0.1) and 27.06758503548673 (m² = 0.001, ε = 0.3);
    numerically to 10⁻²¹–10⁻²².
- **(e3) C_H** = S²R(p̂−k)(H_0−Ĥ) — fibered value [R] [new-final]; whole-integrand parametric value [P].
  - For 0 < ε < 1 the fibered value equals
    C_H = Γ(1+ε)Γ(−ε)Γ(2−ε)Γ(2−2ε)^{−1}Q^{−2−2ε}∫_0^1dy y(y+(1−y)c)^{−1−ε}
        = Γ(1+ε)B(−ε,2−ε)Q^{−2−2ε}[(1−c^{1−ε})/(1−ε) + (c−c^{1−ε})/ε]/(1−c)²,
    exactly.
  - This is the continuation of the (absolutely convergent, −1 < ε < 0) covariant value of T_HΓ, the massless
    on-shell target ladder. Equivalently, it is the DR value of C_H obtained with DR linearity and the scaleless
    T_HC_{R_1} set to zero ((V2)).
  - *Proof.*
    1. The fibered C_H is (1/Γ(2−ε))∫dξ(1−ξ)∫dt t^{−1−ε}[⟨h_0⟩ − ĥ], since κ_0 has v_0 = t/(1−ξ). Here
       ⟨h_0⟩(t→0) = ĥ, |⟨h_0⟩−ĥ| ≤ Ct/(1−ξ), and |⟨h_0⟩| ≤ C(1−ξ)/t. With the outer factor (1−ξ) the constants are
       uniform. By Lemma A.9 the fibered C_H is the continuation from −1 < ε < 0 of the fibered T_HΓ.
    2. For −1 < ε < 0: ⟨h_0⟩ = (1−ξ)/(|k+(1−ξ)q|² + M²) with M² = ξ(1−ξ)c. The Euclidean transverse integral
       ∫d^Dk|k|^{−4}h_0 equals π^{D/2}Γ(1+ε)(1−ξ)∫_0^1dy y[(1−y)(1−ξ)(ξc + y(1−ξ))]^{−1−ε}. So the fibered T_HΓ is
       Γ(1+ε)Q^{−2−2ε}T(ε), with T(ε) = ∫_0^1ds s^{1−ε}∫_0^1dy y(1−y)^{−1−ε}(c(1−s)+ys)^{−1−ε} and s = 1−ξ.
    3. The substitution (α,β,γ) = (1−s, sy, s(1−y)) has dβdγ = s ds dy and gives
       T = ∫_simplex βγ^{−1−ε}(cα+β)^{−1−ε}. Then (α,β) = (1−γ)(1−y′, y′) factorizes it:
       T = B(−ε,2−ε)∫_0^1y′(c+y′(1−c))^{−1−ε}dy′.
    4. The covariant parametric value of T_HΓ, Γ(1+ε)∫_simplex x_1(x_3(x_1+x_2c))^{−1−ε}, reduces to the same
       expression by x_3 = γ, (x_1,x_2) = (1−γ)(1−y′, y′).
    5. Both sides are absolutely convergent for −1 < ε < 0; continue. ∎
  - *Values* (x = 2): −6.584962095176247930933 (ε = 0.1), −3.572721309348424999595 (0.2), −2.607837860955034437041
    (0.3).
  - *Checks* (`r3_ladder_CH_exact.py`):
    - the simplex identity to 10⁻¹³–10⁻³¹ for ε ∈ {−0.6, −0.3, 0.1, 0.2, 0.3, 0.45};
    - the covariant T_HΓ to ≤ 8·10⁻³¹ (ε = −0.6, −0.3, −0.1);
    - the fibered 2D quadrature, with the analytic small-t tail c_1t_0^{1−ε}/(1−ε), c_1 = −1/((1−ξ)A²) + 2/((2−ε)A³),
      to 2·10⁻³⁰ (ε = 0.1, 0.2) and 2·10⁻²⁸ (ε = 0.3);
    - the whole-integrand parametric value (§1.4), in two independent forms (the round-2 report and review r3_1),
      agrees to 3·10⁻³¹ (ε = −0.3), 2·10⁻³⁰ (0.1), 2·10⁻²⁷ (0.2) and 1·10⁻²⁴ (0.3). Its analytic reduction is not
      written; hence [P] for that variant.
  - **Corrected** (review r3_1 required fix 7): the round-2 fibered values deviated from the covariant ones by
    4.2·10⁻¹⁵ (ε = 0.2) and 3.4·10⁻¹³ (0.3). The cause was the omitted part t < e^{−40} of the round-2 quadrature,
    ≈ e^{−40(1−ε)} = 1.3·10⁻¹⁴ and 6.9·10⁻¹³. The script comment "< 1e-15" was false. The printed round-2 value
    −2.60783786095414 was the fibered one; the covariant value is −2.60783786095503.
- **(e4) ε-uniformity of (a)–(d)** — sketch only [P].
  - The transverse measure in d = 6−2ε carries (|k|²)^{−ε}.
  - Lemma A.7 brings the factors (1−z)^{1−ε} and (t−zv)^{1−ε}, and the S³ averages become S^{3−2ε} averages.
  - The region |k| ~ m gives the exponent 1−2ε, and uniform constants would follow from
    (|k|²)^{−ε} ≤ 1 + (|k|²)^{−ε_0}.
  - The estimates are not written out.

**Grades.** (a)–(d) [R, R_PT] at ε = 0; (e1) [R]; (e2) [R]; (e3) fibered = closed form = DR value [R], and the
whole-integrand parametric variant [P]; (e4) [P]. The results are new and elementary.

### Claim C.5 (DIS ladders of every length n) — [P] (downgraded in round 1) [rev]

**Claim.** For every n, (CS1^φ)–(CS3^φ) hold on the cover N_{R_j} = {v_i ≤ λ², |k_{iT}|²/(1−z_i) ≤ λ² for i ≤ j},
U_{R_j} = N_{R_j}∖N_{R_{j+1}}, with items ≤ C_nλΛ^n. Moreover ∫|ρ_r| ≤ C_nλ(1+L)^n at ε = 0.

**Status.**
- n = 1: proven (Prop C.4), including the leading coefficient and the exact identification.
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
- (g1) The bound (P1) cannot hold pointwise at the top level j = n: h(s) is unbounded as ξ → 0, and A + v + 2K·q ≥
  ξc_x is sharp. The induction must start at j = n−1, using the direction-averaged Lemma C.3.
- (g2) On region B the projected kernel κ_0 ~ (1−z)/|k|⁴ is not integrable at k = 0 against an O(1) factor. The
  undifferenced form κ(s)|U(Φ(s))| + κ_0|U(Φ(πs))| must be used, with N_{j+1}(Φ(πs)) = O(√v′_0).
- (g3) The Lipschitz bound (P2) at j = n−1 involves ⟨h²⟩, which carries the factor (d̄/d_min)^{1/2} with
  d_min ≥ zξc_x. A weight ξ^{−1/2} must be carried through the induction; it stays integrable through ξ_j = z_jξ_{j−1}.
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

This is the n = 1 case of the ladder structure. The structure is known (Ex. D.48 of the source); it is made precise
here.

---
## 6. Part D — Abelian massive photon (M3)

### Theorem D.1 (light-like approximators: exact remainder) — exact formula [R, R_PT]; norm [P] [rev]

**Setting.**
- Quark denominators t_1 = 2Pk^- − k² and t_2 = 2P′k^+ − k²; eikonals h_1 = 2Pk^-, h_2 = 2P′k^+.
- Photon G = M² − k²; its hard approximation is g_0 = −k².
- Per-line semilattice: T_S:(t_1,t_2)→(h_1,h_2); T_{C_1}: t_2→h_2; T_{C_2}: t_1→h_1; T_H: G→g_0.

**Exact forms.**
- C_S = 1/(Gh_1h_2);
- C_{C_1} = (1/(Gh_2))(1/t_1−1/h_1);
- C_{C_2} = (1/(Gh_1))(1/t_2−1/h_2);
- C_H = (1/g_0)(1/t_1−1/h_1)(1/t_2−1/h_2);
- r = (1/G − 1/g_0)δ_1δ_2 = −M²g_0/(Gt_1h_1t_2h_2), with δ_i = 1/t_i − 1/h_i, using h_i − t_i = −g_0 and g_0 − G = −M².

**Fibered form** (P = P′ = 1/√2).
- ρ_r = (M²/u)[(1−u)/((M²(1−u)+κ)(u(1−u)+κ)) − 1/((M²+κ)(u+κ))] for 0 < u < 1;
- ρ_r = −M²/(u(M²+κ)(u+κ)) for u > 1.
- The κ-integral of the 0 < u < 1 bracket vanishes identically: both terms equal ln(u/M²)/(u−M²).

**Consequences.**
- ∫r = −M²∫_1^∞du ln(u/M²)/(u(u−M²)) = −M²Σ_kM^{2k}[1/(1+k)² + L/(1+k)] = −λ²(L+1) − λ⁴(L/2+1/4) + O(λ⁶L),
  exactly. This is consistent with Jantzen's closed form.
- Numerically, −5.6246…−14.8084λ² against −(L+1) = −5.605…−14.816. The offset 1.7·10⁻⁴ is constant in M² and is a
  κ-cutoff tail.
- The norm is ≈ λ²(3.0L − 0.85) [P].

**(CS3) fails** for C_S, C_{C_1} and C_{C_2} at every ε. These are rapidity divergences: ρ_{C_S} has constant density
per unit ln k^+, and ρ_{C_{C_1}} = −1/(2PP′(M²+κ)k^+) for k^+ > P. So `thm:appN-subtraction` does not apply, although r
is integrable and O(λ²L).

**Known.** The rapidity divergences of light-like Wilson lines with a massive gluon, and their cure by non-light-like
lines, are in:
- Collins 2011 §10.5 (§10.5.6: "the integral has a rapidity divergence") and §10.6.4;
- Collins–Hautmann 2000;
- the same graph with analytic regulators: Jantzen 2011 §6;
- rapidity regulators: Chiu–Jain–Neill–Rothstein 2012; Becher–Neubert 2011.

**New** only:
- the exact light-like remainder formula;
- the remark that the remainder bound holds without (CS3), while factorization into separately defined factors
  needs (CS3).

### Proposition D.2 (rapidity-regulated soft approximators: time-like versus space-like) — (a)–(c) [R]; time-like window [P] [rev]

**Time-like vectors:** h_{1Y} = 2P(k^- + e^{−2Y}k^+), h_{2Y} = 2P′(k^+ + e^{−2Y}k^-).
- The eikonal and photon poles never collide on the real base.
- The rapidity integral converges (545.458 at Y = 3, 1090.909 at Y = 6, linear in Y), and (CS3^φ) holds for ε > 0.
- For Y ≥ L/2 (e^{−2Y} ≤ λ²) the remainder equals the light-like value within O(λ²), with norm ≈ 2.9λ²L [P].
- At Y = L/4 the regulator error ~e^{−2Y} = λ dominates (`t16b`).

**Space-like vectors** (the i0's of `t16`/`r1_spacelike`): h_{1Y} = 2P(k^- − ek^+) − i0 and h_{2Y} = 2P′(k^+ − ek^-) − i0,
with e = e^{−2Y} and S = M² + κ.

**(a) No pinch of the four-dimensional integral.**
- {G, h_{1Y}}: k ∝ n_A with n_A² = −8P²e < 0, incompatible with k² = M² > 0.
- {G, h_{1Y}, h_{2Y}}: the Gram determinant is −16P²P′²(1−e^{−4Y})² ≠ 0, so k = 0 and G = M² ≠ 0.
- {h_{1Y}, h_{2Y}}: the gradients are independent.

**(b) Real-base pole structure** (`r2_spacelike_poles.py`).
- For x = k^+ > 0, closing on the h_{1Y} pole: ρ_{C_S} = 1/(P(S−2ex²−i0)(2P′x(1−e²)−i0)).
- For x < 0, closing on the h_{2Y} pole: ρ_{C_S} = 1/(P′(S−2x²/e−i0)(2Px(1−e²)−i0)).

There are three simple real-base poles:
- (1) x = 0: c/(x−i0) from both sides, with c = 1/(2PP′S(1−e²)) (xρ → 90.9096494773 at M² = 10⁻³, Y = 3,
  κ = 0.01). As x → 0 the h_{1Y} pole (k^- = ex + i0) and the h_{2Y} pole (k^- = x/e − i0) close in on k^- = 0 from
  opposite sides. This pinches the fiber contour, not the four-dimensional integral, because h_{1Y} = 0 and h_{2Y} = 0
  intersect transversally.
- (2) x = −x_0′ + i0, with x_0′ = √(Se^{−2Y}/2) (G–h_{2Y} collision); residue −1/(4PP′S(1−e²)).
- (3) x = x_0 − i0, with x_0 = √(Se^{2Y}/2) (G–h_{1Y} collision); same residue.

Numerics:
- At the same parameters x_0 = 1.48958328542, x_0′ = 0.00369230781107 and the residue is −45.4548247386 (reviews
  r3_1, r3_2).
- At η = 10⁻⁷ the continued densities have poles at +5.89·10⁻⁸i, −0.0036923+4.66·10⁻⁸i and 1.4895833−2.37·10⁻⁵i.
- The real-axis integrals at η = 10⁻⁶, 10⁻⁸, 10⁻¹⁰ converge to PV + iπRes (x = 0 and −x_0′) and to PV − iπRes (x_0),
  to 10⁻⁸.

Consequences:
- The real-base integral exists as a distribution.
- The singular parts can be integrated along small semicircles passing *below* 0 and −x_0′ and *above* x_0.
- There is no global deformation of the base into one half plane.

**(c) The i0 assignment.**
- These i0's are inherited from the light-like eikonals h_1 = 2Pk^- − i0 and h_2 = 2P′k^+ − i0.
- They are compatible, **locally in the Glauber region**, with the symmetric deformation k^± → k^± − iδ that takes
  (M3) out of that region. The t_1 pole in k^- and the t_2 pole in k^+ lie in the upper half planes, and along the
  deformation Im h_{1Y} = −2P(1−e)δ and Im h_{2Y} = −2P′(1−e)δ keep the sign of −i0.
- Round-3 qualification: Im G = 2δ(k^++k^-) can have the wrong sign away from the Glauber region.
- They are **not** the i0's of Collins (10.68). That equation concerns the time-like form factor, with deformation
  (10.67) k^+→k^++iδ, k^-→k^-−iδ. Collins fixes the signs by also requiring compatibility with (10.69): "the relative
  signs between the i0s and the k^+ terms … all be the same".
- Transplanting Collins' pattern (h_{2Y} → +i0) gives ρ_{C_S} = 0 for x < 0, no pole at x = 0, and both remaining
  poles at −i0, so the base becomes deformable into Im x > 0. In (M3), however, it obstructs the symmetric Glauber
  deformation.
- Which assignment gives universal soft factors in space-like form-factor kinematics is not settled here.
- In both assignments what fails is only absolute integrability on the real fibered base. Time-like vectors have no
  real-base poles. Space-like vectors remain admissible for virtual graphs with contour-deformed approximants.

The results are new and elementary. **Withdrawn** (rounds 1–2):
- "genuine pinch";
- "extends erratum E1/ERR-M27";
- "the only colliding pair is h_{1Y}–G";
- "removed by deforming x into Im x > 0";
- the remedy "integrate κ first", which fails because ∫dκ κ^{−ε}c(κ) is a non-zero constant;
- the attribution "as in Collins §10.6.4".

---

## 7. Part E — The two-loop planar vertex (M1)

**Setup.**
- Lines: g_1 = k_1, g_2 = k_2, a_1 = p_1−k_2, a_2 = p_1−k_1−k_2, b_1 = p_2+k_2, b_2 = p_2+k_1+k_2. k_1 is the inner rung
  and k_2 the outer rung.
- Nine regions: HH, HC1, HC2, C1C1, C2C2, HS, C1S, C2S, SS, where XY = (mode of k_1, mode of k_2). The modes in powers
  of λ are H (0,0,0), C1 (+,−,T) = (0,2,1), C2 = (2,0,1) and S (ultrasoft) = (2,2,2).
- Approximators are coordinate-zeroing sets on (k_1^±, k_{1T}, k_2^±, k_{2T}, M), where M = {m², p_1^-, p_2^+} is the
  infrared regulator. The soft-first convention applies.
- This graph is expected to satisfy (IRF): every soft subgraph has ω_IR > 0 (Prop A.6(c)), and the positive fibered
  density integrates numerically to the Usyukina–Davydychev value (§7.4). Convergence of its parametric integral is not
  proven here.

### Theorem E.1 (exact algebra) — [R] [rev]

Verified exactly by `t8`:
- the 12-edge Hasse diagram: C1C1<HC1, C1S<C1C1, C1S<HS, C2C2<HC2, C2S<C2C2, C2S<HS, HC1<HH, HC2<HH, HS<HC1, HS<HC2,
  SS<C1S, SS<C2S;
- meet closure;
- (Com);
- (Abs) for all 9 incomparable pairs;
- chain recursion = product formula, with 50 zeroing patterns.

### Proposition E.2 (the literal convention violates (Abs)) — [R] [rev]

The literal convention of the source has H see π_± of the exact jet momentum, and soft momenta approximated only inside
jet factors. Its zeroing sets differ from soft-first in four entries:
- HS a_2 {k_2^-, k_{2T}, M};
- HS b_2 {k_2^+, k_{2T}, M};
- C1S b_2 {k_1^-, k_{1T}, k_2^+, k_{2T}, M};
- C2S a_2 {k_1^+, k_{1T}, k_2^-, k_{2T}, M}.

With it, (Abs) fails in exactly 4 cases:
- on a_2 the meet zeroes k_2^+ but neither region does: (C1C1,HS) with meet C1S, and (C1C1,C2S) with meet SS;
- on b_2 the same happens for k_2^-: (C2C2,HS) with meet C2S, and (C2C2,C1S) with meet SS.

This is scripted in `r1_abs_naive.py` and confirmed by all reviews. Soft-first is *sufficient*; necessity is not
claimed. This corrects the claim of the source behind `lem:appN-algebra`(iii) that (Abs) "always holds for per-line
meets". It is a different configuration from the edge case of `rem:appN-abs-edge` (slot X2d, open).

### Theorem E.3 (scaling structure, identification with the region integrals, integrated remainder) [parts (i) rev; (ii), (iv)–(vi) new-final]

All parts use Q̃ = 1 and P = P′ = 1/√2.

**(i) Scaling structure** [R] (exact symbolic; `r1_twoloop_exact.py`, `r2_twoloop_regulator.py`).
- *Definitions.* The weights act on (k_1^±, |k_{1T}|, k_2^±, |k_{2T}|), and m² has weight μ. K is the space of
  m²-independent scalings under which every line factor is homogeneous. D_0 is the degree of integrand × measure at
  ε = 0.
- Γ itself is not homogeneous.
- The 9 singles T_RΓ (coefficient −1 in r) have K = 0, i.e. a unique scaling, with D_0 = 0. Their m²-exponent is −k_Rε,
  with k_R = 0 (HH), 1 (HC1, HC2), 2 (C1C1, C2C2, HS), 3 (C1S, C2S), 4 (SS).
- The 40 composites have D_0 = 0 on the whole family, with dim K = 1, 2, 3, 4 for 18, 15, 6, 1 patterns.
- 22 composites have exact, ε-independent ("rapidity-type") invariances, with dim K_0 = 1, 2, 3 for 15, 6, 1 patterns.
  Example: the k_2 boost (0,0,0,−1,1,0) of the pattern a_1 → 2Pk_2^-, b_1 → 2P′k_2^+, with k_2 absent from a_2 and b_2.
  Its k_2-subintegral is ∫d^dk_2/(k_2²·2Pk_2^-·2P′k_2^+).
- So "scaleless ⇒ 0 in DR" does not apply to these 22.
- With independent analytic powers 1+δ_l on the six lines, the weight map K → (ε, δ_{g_1}, …, δ_{b_2}) is injective for
  all 40 composites. Every composite is therefore exactly homogeneous under a scaling of non-zero weight. The singles
  acquire the m²-exponents −k_Rε − ℓ_R(δ).
- Review r3_1 reproduced the counts, and the independent code of review r2_2 agrees.

**(ii) Identification of the singles with the region integrals** [R] (`r3_twoloop_regions.py`).
- *Leading terms.* For each of the nine regions and each of the six lines, the zeroed line factor of T_R equals the
  leading part of the exact line factor under the region scaling. Hence T_RΓ is the leading-power region integrand
  f_0 of Γ.
- *Change of routing.* Smirnov–Rakhmetov's routing is (k, l) = (k_2, k_1+k_2). Let S_t, S′_t be the region scalings and
  A: (k,l) ↦ (k_1,k_2) = (l−k, k). Then B_t = S_t^{−1}AS′_t → B_0, with det B_0 = 1, and the leading term in the new
  routing is g_0 = f_0∘B_0 (checked symbolically for all nine regions).
- B_0 is a translation of l by a linear function of k, e.g. k_1 = (l^+, l^-−k^-, l_T) for C1S. DR integrals are
  invariant under such translations, so ∫T_RΓ = ∫g_0 as DR values.
- *SR's integrands.* With the dictionary p_1 → p_1, p_2 → −p_2 (SR's p_2 is outgoing), m²_SR = −m², Q²_SR = 2p̃_1·p̃_2 =
  Q̃², the region integrands printed in Smirnov–Rakhmetov (1999), eqs. (3), (5), (6), (7), (8), (9), coincide factor by
  factor with g_0. The other three follow by mirror symmetry.
- *Region dictionary.* SR's "1c" means k^+_SR ~ Q, i.e. collinear to p_2 in our coordinates:
  HH↔(h-h), HC2↔(1c-h), HC1↔(2c-h), C2C2↔(1c-1c), C1C1↔(2c-2c), HS↔(us-h), C2S↔(us-1c), C1S↔(us-2c), SS↔(us-us).
- The m²-exponents −k_Rε agree with SR's (−m²)^{−kε} for all nine regions.
- Note that SR's Q² is our Q̃², so their logarithm L = ln(Q²/μ²) is our L̃.

**(iii) Collins terms versus singles** [R, R_cond: (RA1), (RA2), (V2)].
- The sum of the Collins terms is Σ_RC_RΓ = Γ − r = −Σ_{49 non-trivial patterns}(coefficient)·T_pΓ. The singles enter
  with coefficient −1, so with +1 in the sum.
- Under the auxiliary analytic regularization (RA1), each of the 40 composites is exactly homogeneous under a scaling
  of non-zero weight (i), so it has value 0 by (V2).
- Hence, by DR linearity over the analytically continued pieces and (RA2):
  ∫Γ − ∫r = Σ_R∫C_RΓ = Σ_{9 singles}∫T_RΓ.

**(iv) Values of the singles** [R, cited explicit computation].
- SR evaluate the nine region integrals in DR: (h-h) eq. (4), (us-us) eq. (5), (us-h) eq. (6), (us-1c) = (us-2c)
  eq. (7), and the collinear-type combination eq. (10). They show that all poles cancel, with
  (Q²)²F → L⁴/4 + π²L²/2 + 7π⁴/60 (their eq. (11)).
- Here SR's printed values were summed independently (`r3_twoloop_regions.py` part (5), 90 digits, ε = 10⁻⁸, 10⁻¹²,
  10⁻¹⁶). The deviation from LP = L̃⁴/4 + π²L̃²/2 + 7π⁴/60 is O(ε): 1.6·10⁻¹⁴, 2.6·10⁻¹³, 3.3·10⁻¹² at ε = 10⁻¹⁶
  for L̃ = 2, 5, 9.21.
- Belitsky–Smirnov 2026, App. A.2, give the nine integrals to O(ε²).
- SR evaluate the nine singles of this diagram in DR without an auxiliary regulator; they introduce one only for the
  non-planar diagram of their Limit 2. Their prescription "(c) put to zero any scaleless integral (even if it is not
  regulated, e.g., within dimensional regularization)" is (V2).

**(v) Integrated remainder** [R, R_cond: (RA1), (RA2), (V2)]. From (iii) and (iv):
- ∫r = Φ^(2)(t,t)/Q⁴ − LP exactly, where
  ∫Γ = Φ^(2)/Q⁴ = (1+m²)[12Li_4(−m²) + L̃⁴/4 + π²L̃²/2 + 7π⁴/60]/((1−m²)(1+m²)⁴)
  (Usyukina–Davydychev 1993, with ρt = m² at Q̃ = 1). ∫Γ is analytic at δ = 0, since the off-shell vertex is UV and IR
  finite.
- In particular (FIN2) holds; it is **no longer a premise**. Likewise the round-2 premise "(iii) ∫r → 0" is now a
  consequence.
- NLP: ∫r = −λ²(L̃⁴/2 + π²L̃² + 12 + 7π⁴/30) + O(λ⁴L̃⁴), an elementary expansion of the closed form.
- Values on the grid m² = 0.04, 0.01, 0.0025, 6.25·10⁻⁴, 10⁻⁴, 10⁻⁶: ∫r = −7.050661, −4.596744, −2.570489,
  −1.281728, −0.446917, −0.0201338. Their ratios to the NLP formula are 0.92448, 0.98028, 0.99502, 0.99875, 0.99980,
  0.999998.

**(vi) Without (iv): degree bound** [R].
- If only (FIN2) is assumed, Σ_R∫C_RΓ = Σ_kC_k(ε)e^{kεL̃}, grouped by the five distinct exponents k ∈ {0,…,4}.
- Lemma A.8 then shows that the grouped pole coefficients of order ≥ 5 vanish and that P(L̃) is a polynomial of degree
  ≤ 4. This is the pole-order input asked for by review r3_1.

**Norms.**
- Every fibered norm is ≥ |∫_Bρ_r|.
- Identifying ∫_Bρ_r with ∫r is (FI) for r at two loops. This is a **premise** (OQ11), supported by the QMC agreement:
  the n18 run gives −7.036±0.22, −4.593±0.08, −2.386±0.24, −1.319±0.084 against the exact −7.0507, −4.5967, −2.5705,
  −1.2817 (0.05–2.4σ).
- Under (FI)_r, (RA1), (RA2) and (V2), every norm is ≥ ½λ²L̃⁴(1+o(1)). The round-0 claim "averaged norm ~m²L^{2.6–3}"
  is asymptotically false.

**Positioning.**
- Smirnov–Rakhmetov 1999 treat exactly this diagram, with the same nine regions, all region integrals, and the LP sum.
  Belitsky–Bork–Smirnov 2025 and Belitsky–Smirnov 2026 treat the same off-shell scalar integrals.
- The mechanism by which nested subtraction terms reduce to region integrals is the zero-bin/overlap mechanism
  (Manohar–Stewart 2007; Idilbi–Mehen 2007; Jantzen 2011).
- **New** only:
  - the analysis of Collins' composite (zero-bin) patterns, i.e. the 22 rapidity-type composites and the injectivity of
    the regulator weight map;
  - the explicit identification of Collins' nested terms with the region integrals at this order, with the regulator
    requirements made explicit;
  - the NLP coefficient, an elementary expansion of the Usyukina–Davydychev form.

### 7.4 Two-loop numerics: double-residue (LCPT) densities and remainder norms — [P] [rev]

- *Engine.* `lcpt.py` with 6 factors and 2 minus components; order and weight independence to 5·10⁻¹⁰ (`t9`).
- *Validation of ∫ρ_Γ* against Φ^(2)/Q⁴ (exact 82.282, 223.863, 508.102, 1019.383 at m² = 0.04…6.25·10⁻⁴):
  - n18 run: 82.41±2.0, 222.4±1.1, 513.8±6.5, 1016.8±4.6;
  - 16 independently scrambled Sobol randomizations (`r1_twoloop_qmc.py`): 81.66±0.55, 239.1±12, 505.9±1.8,
    1020.2±5.2, with pulls −1.1, +1.3, −1.2, +0.2;
  - the n16 run of `t12` under-covers.
  - The sample distribution is heavy-tailed, so the error bars are indicative only.
- *Remainder norms.*
  - Full light-cone norm ≈ 31.3, 31.7, 31.5, 32.3 λL. This is first order, from angle-odd projection errors such as
    2k_{1T}·k_{2T} (mechanism: Collins §10.7.3).
  - Norm with the relative azimuth averaged in the fiber: 11.3, 7.0, 3.46, 1.88 (`t14`).
- The fitted rates "31λL", "m²L^{2.6–3}" and "−4.7m²L³" are **withdrawn** as determinations.
- These are fibered integrals. Their agreement with the exact covariant values tests (FI) for Γ and r at two loops,
  jointly with the premises of Thm E.3.

---

## 8. Part F — All orders

### Theorem F.1 (conditional subtraction theorem for IR-finite graph classes of (M1)) — [R, R_cond: (FR), (FI), (COV), (CS3^φ), (IRF)] [restricted in this revision]

**Setting.**
- (M1) at fixed order N, and a finite set 𝒢 of graphs each satisfying (IRF).
- Integrand-level renormalization (`asm:appN-uv`(U1)) of their UV-divergent subgraphs. In an IR-finite (M1) graph these
  are J–φ-type two-point insertions on lines of fixed momentum; ψ or φ self-energies on loop lines make a graph IR
  divergent (Prop A.6(b)).
- Regions: the meet closure of the leading regions. Approximators: soft-first.

**Premises** (for each Γ ∈ 𝒢):
- (FR) and (FI) for Γ and every C_RΓ;
- (COV);
- (CS3^φ).

**Conclusion.**
- Σ_{Γ∈𝒢}Σ_RI_{C_RΓ} = Σ_{Γ∈𝒢}I_Γ + O(λ^aL^K), uniformly in ε ∈ (0,ε_0];
- every term converges absolutely for ε > 0;
- if the I_{C_RΓ} are meromorphic at ε = 0 (the analogue of `asm:appN-contour`(b); true for the triangle by Prop B.2),
  the UV poles of single subtraction terms cancel in the sum (`lem:method-no-pole`, `cor:method-removing-eps`).

*Proof.* Apply Thm A.1(iii) to each Γ and sum over the finite set 𝒢. Apply `lem:method-no-pole` to the bounded
meromorphic sum. ∎

Gauge theories would additionally need `asm:appN-ward-product` and the P_A/K-gluon approximators (OQ2).

**Status of the premises (corrected).**

*Verified.*
- **N = 1, all graphs of (M1)**, i.e. the triangle and the J–φ graph:
  - (FR);
  - (FI), exact (Props B.2, B.3; the J–φ graph is an explicit renormalized insertion);
  - (COV): the triangle by Thm B.5; for the J–φ graph the remainder is Π_R(q²)D(q) − Π_R(q̂²)D(q̂) = O(λ²);
  - (CS3^φ) (Prop B.1).
  So at N = 1 the theorem holds **without premises** [R, R_PT, computer-assisted]; the triangle part is Cor B.6.
- (Com), (Abs) (soft-first) and the product formula at N = 2 [R] (Thm E.1).
- The two-loop scaling structure and the identification with the region integrals [R]; the integrated N = 2 planar
  remainder [R, R_cond: (RA1),(RA2),(V2)] (Thm E.3).
- (CS3^φ) for Γ: the triangle [R]; any graph satisfying (IRF), given (LCE) (Cor A.5).

*Not verified.*
- (FR)+(FI) of the Collins terms at N ≥ 2. 22 composites carry rapidity-type invariances, and neither the C_R nor r is
  identified at two loops.
- (COV) for the planar and crossed two-loop vertices (numerical only, §7.4) and for general N ≥ 2.
- Gauge numerators, Ward identities, and slot X2d.

*Removed* (round 3):
- "VERIFIED: (CS3^φ) for Γ at all orders, for UV-finite graphs without tadpoles" — false by Prop A.6(a);
- "(F1) for the bubble-chain class" — not an (M1) graph class (Thm B.8).

### Remark F.2 (scope)

F^(N) of (M1) is IR divergent at fixed m for N ≥ 2 (Prop A.6(b)). Thm F.1 is therefore a statement about IR-finite
graph classes, and not about the physical form factor of (M1). An all-order statement about a physical off-shell form
factor needs an IR-safe model (OQ16). Candidates are a renormalizable scalar theory (cf. (M2)), a massive φ, or a
gauge theory with the inputs of OQ2.

### Remark F.3 (subtraction is not factorization, off shell)

- Belitsky–Smirnov 2026 study the off-shell Sudakov form factor, on the Coulomb branch of N = 4 SYM, built from the
  same off-shell scalar integrals T_11, T_21, T_22.
- They find that hard factorization holds to three loops, but the ultrasoft and collinear modes do not separate.
  - At two loops the c–us region integral is (1/4)z_1(ε)T_11^cT_11^us, with z_1 = Γ(1+2ε)/Γ(1+ε)², which can be
    mended by "twisting".
  - At three loops the c–c–us and c–us–us integrals require incompatible adjustment factors.
- In the present language, the term of T_{C1S} (and of C_{C1S}) that keeps 2(P−k_1^+)k_2^- on line a_2 is leading and
  cannot be dropped. This is the "entangling term" of their eq. (6.18).
- Hence the subtraction theorem, Σ_RC_RΓ = Γ + power-suppressed, does not by itself yield a product of separately
  defined hard, jet and ultrasoft factors in off-shell kinematics. In gauge theories the factorized form uses in
  addition the Ward-identity/Wilson-line structure (`asm:appN-ward-product`), and Belitsky–Smirnov show that the
  separation of collinear and ultrasoft modes can fail off shell (OQ17).

### Remark F.4 (positioning)

- Nested (forest) subtractions for general graphs exist at the level of pinch surfaces:
  - Collins 2011, ch. 10;
  - Erdoğan–Sterman 2015;
  - Ma 2020 (IR forest formula; pairwise cancellation of the singularities of the subtraction terms; factorized form);
  - Feige–Schwartz 2014 (all-order hard–soft–collinear factorization of amplitudes);
  - Anastasiou–Sterman 2019 (local two-loop IR counterterms).
- The integrated leading-power region expansion is covered, at the level of the method-of-regions literature, by
  Bergère–de Calan–Malbouisson 1978; Beneke–Smirnov 1998; Smirnov–Rakhmetov 1999; Jantzen 2011;
  Semenova–Smirnov–Smirnov 2019; Gardi–Herzog–Jones–Ma–Schlenk 2023; Poldaru (preprint, arXiv:2607.26291).
  Belitsky–Smirnov 2026 stress that "the Method of Regions has the status of experimental mathematics" in general.
- What remains open is the off-shell, integrand-level version for general graphs: integral-norm bounds with explicit
  power suppression, uniform in ε, together with the identification of fibered and covariant values. X2 supplies these
  for the graphs listed in Parts B and C.
- **Withdrawn** (round 2): the phrase "genuinely open".

---
## 9. Relation to Appendix N and to the source document (for the integrator)

The monograph never cites the source document (`factorization_qcd-2.pdf`, its App. D). The dictionary below is for the
integrator only.

| source (App. D) | monograph label | relation to this report |
|---|---|---|
| Thm D.10 | `thm:appN-subtraction` | Thm A.1 is its fibered form. (GA1)(a) is replaced by (FR)+(FI), which can be checked graph by graph. |
| (H1)–(H3) | (CS1)–(CS3), `def:method-collins-conditions` | (CS1^φ)–(CS3^φ) are their fibered versions. |
| (A1)(a),(b) | `asm:appN-contour` (GA1)(a),(b) | (a) is replaced where the densities are integrable on the real base; (b) is kept. |
| Def D.5, Lemma D.25 | `def:method-neighbourhoods`, `lem:appN-beta` | Sharpening: natural-scale covers give the optimal exponent (Thm B.5). |
| Def D.9 (H3) on the real contour | — | Remark A.1(a). |
| Lemma D.23(iii) | `lem:appN-algebra`(iii) | Correction confirmed: the literal convention fails (Abs) in 4 cases (Prop E.2). Slot X2d is a different configuration. |
| Def D.21 (space-like vectors) | `def:appN-tmd-approx` | No pinch; three real-base poles (Prop D.2). |
| Ex. D.47 + Table 5 | `prop:appN-triangle-exact` | Thm B.5, Cor B.6, Props B.2–B.4, B.7. |
| Ex. D.48 | `prop:appN-ladder` | Lemma C.2, Prop C.4, Prop C.6. |
| (D1)(D2) | `asm:appN-values` (V1)(V2) | (V1) is verified for the triangle and for the ladder's C_{R_1} and C_H. (V2) enters only Thm E.3 and Prop C.4(e3). |
| D.14 | `asm:appN-collins` | Its 「地位」 can list Thm B.5, Cor B.6, Prop C.4 and the limits stated in §14. |
| D.41 | `asm:appN-uv` | Used in Prop C.1 and Thm F.1. |

**Suggested insertion points** (to be registered by the integrator; no label is created here):
- Thm A.1 as a proposition in §N.3, after `thm:appN-subtraction`, with (FR), (FI) as local items, like (CS1)–(CS3);
- Thm B.5 + Cor B.6 as `prop:appN-triangle-cs` (slot X2a);
- Prop B.3 and Prop B.2 inside the proof of `prop:appN-triangle-exact`(b);
- Prop E.2 in `rem:method-abs-failure`;
- Thm E.3(v) as a sharpening of `ex:method-naive-induction` or as a remark in §N.7;
- Prop A.6 as a remark in §N.7: model choice for all-order examples.

**Corrections and sharpenings relative to the source**, as labelled after review:
- (a) CONFIRMED correction of Lemma D.23(iii) (Prop E.2).
- (b) SHARPENING (Def D.5): natural-scale covers give the optimal exponent.
- (c) REMARK (Def D.9): (H3) fails on the real contour; the fibered form replaces the deformation by (FR)+(FI).
- (d) SHARPENING (Remark A.1(b)): ε-uniform (CS2) needs UV-bounded non-maximal U_R or fast-decaying items.
- (e) WITHDRAWN: the round-0 claim that the space-like vectors of Def D.21 pinch. The replacement analysis is
  Prop D.2.
- (f) CONFIRMED, and absent from the source: ∫|ρ_r| ≈ λ²(4L̃ − 0.69); the sliver carries ζ_2/Q̃² of the integral and
  −2λ² of the remainder.
- (g) CONFIRMED: (H3) is not necessary for the remainder bound (Thm D.1) but is necessary for factorization; the
  mechanism is known.

---

## 10. Error estimates with explicit powers

All at ε = 0 unless stated. For ε ∈ (0,ε_0] the one-loop exponents decrease by at most 4ε_0, certified at ε_0 = 1/10.

| object | estimate | grade |
|---|---|---|
| triangle (M1): all (CS1)/(CS2) items | ≤ Cλ²L^{≤2}; on (0,1/10] ≤ C(λ²L²+λ^{8/5}) | [R, R_PT] ca |
| triangle: fibered remainder norm | ≤ Cλ²L²; numerically ≈ λ²(4L̃ − 0.69) | [R, R_PT] ca / [P] |
| triangle: integrated \|I_Γ − ΣI_{C_R}\| | ≤ C(λ²L²+λ^{8/5}) on (0,1/10] | [R, R_PT] ca (Cor B.6) |
| triangle: signed ∫r | = −4λ² + O(λ⁴L̃²) (exact closed form, Prop B.7) | [R, R_PT] (known) |
| log-weighted family, fixed j | ≤ C_jλ²L^{j+2}, with C_j ≳ 2j!/L_0^{j+2} | [R, R_PT] ca |
| DIS (M2): one-rung ladder | ∫\|ρ_r\| = c_1(x)λ + O(λ²L); numerically \|∫\|ρ_r\| − c_1λ\| ≤ 0.08λ²L | [R, R_PT] |
| DIS: two-rung ladder | full norm ≈ (1.3+0.27L)λ | [P] |
| DIS: H-only one-loop graphs | vertex ≤ Cλ²L (≈ (0.46L+3.1)λ²); self-energy ≤ Cλ² (≈ 0.871λ²); J–φ O(λ²) | [R, R_PT] |
| massive photon (M3), light-like | ∫r = −λ²(L+1) − λ⁴(L/2+1/4) + O(λ⁶L); norm ≈ λ²(3.0L − 0.85) | [R, R_PT] / [P] |
| massive photon, time-like regulator | light-like value for Y ≥ L/2; error ~e^{−2Y} otherwise | [P] |
| two-loop planar vertex: ∫r | = Φ^(2)/Q⁴ − LP = −λ²(L̃⁴/2+π²L̃²+12+7π⁴/30) + O(λ⁴L̃⁴) | [R, R_cond: (RA1),(RA2),(V2)] |
| two-loop: every remainder norm | ≥ ½λ²L̃⁴(1+o(1)) | [R, R_cond: + (FI)_r] |
| two-loop: full fibered norm | ≈ 31–32λL | [P] |

---

## 11. Spec slots (`spec_v2/OUTLINE_appMNOPQ.md` §00.4)

**X2a, `prop:appN-triangle-cs`: DELIVERED.**
- *Fibered statement* (Thm B.5): (CS1^φ)–(CS3^φ) with explicit exponents, uniformly in ε ∈ (0,1/10]. Grade
  [R, R_PT], computer-assisted. It was reviewed in rounds 1–3 (independent audits of the certificate logic and of the
  archives by reviews r2_2, r3_1, r3_2). Its archive is now self-contained and exactly re-verified by independent code.
  This meets the PASS rule.
- *Integrated statement* (Cor B.6): `thm:appN-subtraction` for the triangle without a four-dimensional contour and
  without premises. It rests additionally on Prop B.3 (new-final), which is proved by explicit changes of variables and
  checked symbolically and numerically by `r3_FI_exact.py`, but not yet confirmed by an independent reviewer. Until one
  confirmation is recorded, the integrator may print Cor B.6 as [R, R_cond] with the premise "(FI)_Γ, verified
  numerically to 10⁻¹⁷–10⁻²⁸" (the round-2 form).
- If PASS, the status sentence of `prop:appN-triangle-exact` changes to 「在 k⁻ 留数表示中，(CS1)–(CS3) 对本例已完整验证（\cref{prop:appN-triangle-cs}）；Γ 与各减除项的纤维化值与协变值精确相同」.

**X2b, `thm:appN-oneloop`: NOT DELIVERED.** Only the equal-virtuality triangle and the J–φ graph are covered.
Unequal or hierarchical virtualities, massive internal lines and gauge numerators are not. The fallback (deletion)
stays.

**X2c, `prop:appN-ladder-cs`: NOT DELIVERED.** X2 gives only the scalar φ³₆ analogue: the one-rung ladder is proven
(Prop C.4), including exact identification of Γ, C_{R_1} and C_H; the two-rung ladder is numerical. The fallback
("grouping statement only") stays.

**X2d, `rem:appN-abs-edge`: OPEN.** Prop E.2 is a different, convention-level issue. The configuration of the remark —
a soft line with both ends at hard vertices, and gluon polarizations — has not been checked.

---

## 12. Novelty ledger

"New" means: not found in the literature by the INSPIRE and full-text searches of reviews r1_1, r1_2, r2_1, r2_2,
r3_1 and r3_2. Their queries included "Collins subtraction" combined with tropical, Newton polytope or linear
programming; integral norm with subtraction and factorization; light-cone ordered; and forest formula with infrared.

**New (to our knowledge):**
1. Thm A.1: the integral-norm formulation of Collins' subtraction theorem on a real fibered base, with checkable
   hypotheses (FR), (FI). The proof is the elementary one of `thm:appN-subtraction`.
2. Lemma A.3: certification of Collins' integral norms by exact LP/tropical certificates, with self-contained,
   independently re-verifiable archives. The ingredients are known.
3. Thm B.5: complete verification of (CS1^φ)–(CS3^φ) for the off-shell triangle with the optimal λ-exponent, uniformly
   in ε ∈ (0,1/10].
4. Props B.2, B.3 and Cor B.6: exact fibered–covariant identification for Γ and all Collins terms of the triangle,
   giving the integrated subtraction theorem without premises. The closed forms of the C_R themselves are known
   region values.
5. Prop B.4 (sliver: ζ_2/Q̃² and −2λ²) and Prop D.2 (the three-pole structure of space-like regulators). Both are
   elementary.
6. Prop C.1 and Prop C.4: all one-loop φ³₆ DIS graphs, with renormalization at the integrand level, and the complete
   one-rung ladder proof, including c_1(x) (first derived in review r1_1) and the exact identification of Γ, C_{R_1}
   and C_H. All elementary.
7. Thm B.8: certificates for the log-weighted triangle family. The model interpretation is only by analogy.
8. Prop A.6(a): the explicit counterexample to "UV finite ⇒ (CS3^φ)" in (M1). The mechanism is known
   (Jackiw–Templeton).
9. Thm E.3: the composite/zero-bin regulator analysis (22 rapidity-type composites; injectivity) and the explicit
   identification of Collins' nested terms with the Smirnov–Rakhmetov region integrals. The region values and the
   leading-power sum are known (SR 1999). The NLP coefficient is an elementary expansion.
10. Prop E.2: the explicit (Abs) failure of the literal convention, a correction of the source.
11. Thm D.1: the exact light-like remainder formula, and the remark that the remainder bound does not need (CS3).

**Known (attributed):**
- the subtraction scheme and Theorems 1R–4: Collins 2011, ch. 10;
- forest formulas: Ma 2020; Erdoğan–Sterman 2015; Feige–Schwartz 2014; Anastasiou–Sterman 2019;
- region integrals of the off-shell vertex: Smirnov 2002; Smirnov–Rakhmetov 1999; Belitsky–Bork–Smirnov 2025;
  Belitsky–Smirnov 2026;
- closed forms Φ^(1), Φ^(2): Usyukina–Davydychev 1993;
- light-cone-ordered perturbation theory: Chang–Yan 1973; Ligterink–Bakker 1995; Collins 2018;
- rapidity divergences and non-light-like lines: Collins 2011 §10.5–10.6; Collins–Hautmann 2000; Jantzen 2011;
  Chiu–Jain–Neill–Rothstein 2012; Becher–Neubert 2011;
- the angle-averaging gain p = 1 → 2: Collins 2011 §10.7.3;
- the infrared problem of super-renormalizable theories: Jackiw–Templeton 1981;
- tropical approximation: Borinsky 2023;
- expansion by regions: Bergère–de Calan–Malbouisson 1978; Beneke–Smirnov 1998; Jantzen 2011;
  Semenova–Smirnov–Smirnov 2019; Gardi–Herzog–Jones–Ma–Schlenk 2023; Ma 2024; Arkani-Hamed–Hillman–Mizera 2022;
  Poldaru (preprint);
- zero-bin: Manohar–Stewart 2007; Idilbi–Mehen 2007;
- off-shell ultrasoft–collinear non-factorization: Belitsky–Smirnov 2026, cf. Belitsky–Bork–Smirnov 2025;
- ladder mass-singularity factorization: Ellis–Georgi–Machacek–Politzer–Ross 1979; Curci–Furmanski–Petronzio 1980;
- analytic regularization: Speer 1968;
- massless power counting: Lowenstein–Zimmermann 1975; Minkowski power counting: Zimmermann 1968.

---

## 13. Withdrawn and corrected claims (all rounds)

| # | claim (round) | status | replacement |
|---|---|---|---|
| W1 | "The 4D contour assumption (A1) disappears" (0) | withdrawn (1) | (FR)+(FI) (Thm A.1) |
| W2 | "The Glauber region never appears" (0) | restricted (1) | scope of Thm A.1 |
| W3 | Space-like rapidity vectors give a "genuine pinch"; "extends erratum E1" (0) | withdrawn (1) | Prop D.2(a) |
| W4 | "Only colliding pair h_{1Y}–G"; "deform x into Im x > 0"; "integrate κ first"; "as in Collins §10.6.4" (1) | withdrawn (2) | Prop D.2(b),(c) |
| W5 | DIS ladders of all n [R] (0) | downgraded to [P] (1) | Claim C.5 |
| W6 | One-loop DIS H-only graphs "(H3) trivial" (0) | withdrawn (1) | Prop C.1 (BPHZ) |
| W7 | Two-loop fits "∫r ~ −4.7m²L³", "averaged norm ~ m²L^{2.6–3}", "31λL" as determinations (0) | withdrawn (1) | Thm E.3(v); §7.4 |
| W8 | "Exponent 1 of the 2×2 cover is optimal" (0, own) | retracted (0–1) | Thm B.5 (θ = 2 optimal); marked in the `t18` docstring |
| W9 | "Fat neighbourhoods are harmful"; "(H3) on the real contour" as an App. D error (0) | relabelled (1) | sharpening / remark (§9) |
| W10 | "Soft-first is necessary" (0) | corrected (1) | "sufficient" (Prop E.2) |
| W11 | Bubble class "[R] at all N" without hybrid/factorial caveats (0) | corrected (1) | Thm B.8 |
| W12 | "Admissibility of all Collins terms VERIFIED at all orders" (0) | withdrawn (1) | Thm F.1 status |
| W13 | "Lemma 2.7 gives (ID) for all terms at N = 1"; "by Thm 2.6 and Lemma 2.7" (1) | withdrawn (2) | Props B.2, B.3 |
| W14 | "The 40 composites are homogeneous along a one-parameter family … scaleless ⇒ 0 in DR" (1) | withdrawn (2) | Thm E.3(i) |
| W15 | "Massless on-shell triangle plus scaleless terms" for C_H (1) | withdrawn (2) | Prop B.2 remark |
| W16 | Non-maximal U_R UV-bounded as a *hypothesis* (1) | moved to Remark A.1(b) (2) | — |
| W17 | "Checked: the (M2) one-loop graphs" for (ID) (1) | withdrawn (2) | Prop C.4(e) |
| W18 | "Genuinely open"; Ma 2020 filed as a polytope reference (1) | corrected (2) | Remark F.4 |
| W19 | **Cor 2.11: (CS3^φ) for Γ for every UV-finite (M1) graph without tadpoles or one-loop two-point subgraphs (0–2)** | **withdrawn (final)** | Cor A.5 with (IRF); counterexample Prop A.6(a) |
| W20 | **Thm 6.1 status "VERIFIED: (CS3^φ) for Γ at all orders" (0–2)** | **withdrawn (final)** | Thm F.1 status |
| W21 | **Thm 3.9: Γ^(j) is the MS-bar renormalized bubble chain of (M1); "true d-dim chain (−k²)^{−nε}×poles"; renormalon reading for (M1); "(F1) for the bubble-chain class" (0–2)** | **withdrawn (final)** | Thm B.8 (log-weighted family) |
| W22 | "NEW (elementary)" for the closed forms of Prop 3.1′; "NEW only as a worked example" for Thm 4.3 (2) | narrowed (final) | §12 items 4 and 9 |
| W23 | Premise (ID)_Γ of the integrated triangle corollary (2) | removed (final) | Prop B.3 |
| W24 | Premises (F) and "(iii) ∫r → 0" of Thm 4.3 (1–2) | discharged (final) | Thm E.3(iv),(v) |
| W25 | `r2_ladder1_identification.py` comment "neglected part < 1e-15"; C_H fibered side [P] (2) | corrected (final) | Prop C.4(e3) |
| W26 | Open items O3 ("UV subdivergences") and O13 ("full graph beyond the hybrid model") as open problems *in (M1)* (2) | corrected (final) | OQ3, OQ13, OQ16 |
| W27 | "Equivalent to positivity of the Symanzik F polynomial" (1–2) | corrected (final) | "analogous to" (Lemma A.4) |
| W28 | Thm 4.3 m² values written as "0.04…10⁻⁶" (2) | corrected (final) | explicit grid (Thm E.3(v)) |

The truncated round-0 draft and the scratch copies `X2_REPORT_attempted.md` and `X2_REPORT_orig.md` still contain W8.
They must not be used.

---

## 14. Open problems

- **OQ1 (central).** The fibered form of `asm:appN-collins` for general graphs.
  - Needed: off-shell, integrand-level integral-norm bounds (CS1^φ)/(CS2^φ) with explicit exponents, and (FR)/(FI)
    for the Collins terms.
  - The only inductive mechanism found covers ladders, and it is complete only for n = 1 (Claim C.5).
  - The LP method needs explicit densities.
- **OQ2 (gauge theories).** No one-loop QCD vertex or box with Dirac numerators and the P_A/K projections has been
  certified. Also open:
  - instantaneous terms of light-cone-ordered perturbation theory;
  - (Abs) for transverse polarizations of direction-flipping lines;
  - Ward identities on approximated integrands (`asm:appN-ward-product`).
- **OQ3 (two loops beyond the planar ladder).** In (M1) the crossed ladder is IR finite and open. Two-loop graphs with
  UV subdivergences are IR divergent in (M1) (Prop A.6(b)), so their study needs a different model (OQ16). The J–φ
  class beyond one loop is open.
- **OQ4 (two-loop planar vertex).**
  - A rigorous (CS1)–(CS3) proof is missing; the obstacle is the Gram factors.
  - (CS3^φ) for an individual C_R requires the 22 rapidity-type composites to cancel inside that C_R, as 1/(D_gh_1h_2)
    does inside C_H at one loop. Otherwise (CS3^φ) fails, as in (M3).
- **OQ5 (sharp second-order norms with angle-averaged fibrations).** DIS ladders (conjecture O(λ²L^{b_n})); the
  two-loop vertex (≥ ½λ²L̃⁴ under (FI)_r; conjecture Θ(λ²L̃⁴)).
- **OQ6 (ε-uniformity).** Multi-loop transverse integrals (Gram weights) are open. For the one-rung ladder the
  ε-uniformity is only sketched (Prop C.4(e4)).
- **OQ7 (physical cut processes).** The cut-sum representation (`asm:appN-cutsum`) is untouched. Glauber-pinched
  processes lie outside the scope of Thm A.1.
- **OQ8 (rapidity regulators).**
  - Time-like vectors work at one loop for Y ≥ L/2.
  - Space-like vectors need a fibered method on a locally deformed base, or another fibration in which (CS3^φ) can be
    verified.
  - A decision on the i0 assignment for universal soft factors in space-like form-factor kinematics is also needed.
- **OQ9.** The massive-photon class beyond one loop, and abelian exponentiation.
- **OQ10 (all orders).** Thm F.1 rests on OQ1, OQ11 and OQ16. Exponentiation, `asm:appN-ward-product` and
  `asm:appN-multren` are not addressed, nor is the off-shell factorization obstruction (OQ17). At fixed order the
  integrated statement is covered by the method-of-regions literature (at its level of rigour); the integral-norm
  bounds are not.
- **OQ11 ((FR)/(FI) of all Collins terms).**
  - Identified exactly: Γ and the four Collins terms of the triangle (Props B.2, B.3); Γ, C_{R_1} and the fibered C_H
    of the one-rung ladder (Prop C.4(e)).
  - Open:
    - an analytic reduction of the whole-integrand parametric C_H of the ladder (agreement to 10⁻²⁴–10⁻³¹ only);
    - a grouped-residue version of Lemma A.2, or a rigorous LCPT–covariant equivalence for approximated integrands
      with eikonal factors and numerators;
    - the two-loop C_R and r.
  - The transverse-Euclidean method of Props B.3 and C.4(e) — Feynman-parametrize the residue density, then change
    variables onto the covariant simplex — is a candidate general mechanism at one loop.
- **OQ12 (DIS ladders with n ≥ 2).** Close gaps g1–g5; obtain complex-ω uniformity; treat the fermion ladder (slot
  X2c).
- **OQ13 (log-weighted family).** Two directions:
  - the genuine large-β_0 chain of a theory with Π ∝ k² (φ³₆ or a gauge theory), grafted onto an IR-safe model;
  - the summed family, the renormalon analogue (C_j ≳ j!).
- **OQ14 (spec slots).** X2b: unequal virtualities, massive lines, gauge numerators. X2d: the (Abs) edge case.
- **OQ15 (Lemma A.2 hypotheses).** (IL1) and (IL3) for pure-denominator integrands beyond those of Parts B and C. For
  the triangle and the ladder they are no longer needed.
- **OQ16 (new: IR-safe model for all-order statements).**
  - Choose a model in which the physical off-shell form factor is IR finite at every order: massive φ, a renormalizable
    scalar theory, or a gauge theory with OQ2.
  - Prove the sufficiency direction of soft power counting (Prop A.6(c),(d)) in the non-Euclidean, positive-F
    kinematics used here.
- **OQ17 (new: off-shell factorization).** Can the Collins subtraction terms of off-shell form factors be organized into
  a factorized form, despite the non-product collinear–ultrasoft region integrals of Belitsky–Smirnov 2026? The leading
  entangling term 2(P−k_1^+)k_2^- of T_{C1S}, and its Wilson-line interpretation, are the concrete starting point.

---

## 15. Scripts, logs and archives

All paths are relative to `verify/extend/X2-subtraction/`. Run with `python3 -I`, with
`~/Library/Python/3.9/lib/python/site-packages` on sys.path.

**Final revision (r3).**
- `scripts/r3_FI_exact.py` → `logs/r3_FI_exact.log`: Prop B.3 and Prop C.4(e1), with symbolic maps, Jacobians,
  F-factorizations and densities; quadratures of the simplex sub-regions with corner breakpoints. An earlier crude
  nested quadrature without corner breakpoints was inaccurate (0.4%) and is superseded.
- `scripts/r3_ladder_CH_exact.py` → `logs/r3_ladder_CH_exact.log`: Prop C.4(e3), including the corrected fibered
  quadrature.
- `scripts/r3_twoloop_regions.py` → `logs/r3_twoloop_regions.log`: Thm E.3(ii),(iv)–(vi).
- `scripts/r3_M1_infrared.py` → `logs/r3_M1_infrared.log`: Prop A.6.
- `scripts/r3_lptools.py`, `scripts/r3_triangle_recert.py`, `scripts/r3_bubble_recert.py` → the self-contained archives
  `logs/r3_triangle_certificates_sc.json.gz` (58 pieces, 546 certificates) and
  `logs/r3_bubble_certificates_sc.json.gz` (2986 pieces, 70,373 certificates); logs `logs/r3_triangle_recert.log`,
  `logs/r3_bubble_recert.log`, `logs/r3_bubble_recert_summary.json`.
- `scripts/r3_archive_verify.py` → `logs/r3_archive_verify.log`: the independent exact verification of both archives
  (Lemma A.3(c)). All checks pass.

**Round 2.**
- `r2_triangle_identification.py`: Prop B.2; PART E is the (IL2) failure.
- `r2_spacelike_poles.py`: Prop D.2.
- `r2_twoloop_regulator.py` (+ `.json`): Thm E.3(i).
- `r2_lptools.py`; `r2_bubble_recert.py` (superseded by r3); `r2_cert_audit.py`.
- `r2_ladder1_even.py`: Prop C.4(d).
- `r2_ladder1_identification.py`: C.4(e2), and C_H with the cut, superseded.

**Round 1.**
- `r1_lptools.py`, `r1_triangle_recert.py` (the item, cell and sliver definitions are imported by r3), `r1_theta2_lower.py`.
- `r1_triangle_covariant.py`, `r1_bubble_recert.py`.
- `r1_twoloop_exact.py`, `r1_twoloop_qmc.py`.
- `r1_spacelike.py`, `r1_dis_Honly.py`, `r1_abs_naive.py`, `r1_ladder1_analytic.py`.

**Round 0** (still used).
- Engines and core: `lcpt.py`, `tropical.py`, `exact_verify.py`.
- Triangle: `t1`, `t2`, `t2a`, `t2b`, `t2c`, `t3`, `t4`, `t4x`, `t4y`, `t4z`.
- Log-weighted family: `t5`, `t15`, `t15b`, `t15d`, `t15f`, `t17`, `t17x`, `t17y`.
- DIS: `t6`, `t6b`, `t11`.
- Engine validation and two loops: `t7`, `t8`, `t9`, `t10`, `t12`, `t14`.
- Massive photon: `t13`, `t16`, `t16b`.
- Inputs: `twoloop_dens.py`, `twoloop_patterns.json`, `bubble_cells.json`.
- Superseded or invalid: `recession.py`, `t4w`, `t15e`, `t19`; `t15c` is invalid; the `t18` docstring is marked
  RETRACTED.

**Reviewer check scripts.** `review_r3_1_scripts/` (r3_numbers, r3_ladder_CH, r3_M1_infrared, r3_bubble_archive, with
logs) and `review_r3_2_scripts/` (c1–c7, copied from the session scratchpad).

**Reviews.** `verify/extend_reports/X2-subtraction-rev{1,2,3}-{1,2}.md`.

---

## 16. References (bibliographic data verified on INSPIRE)

- C. Anastasiou, G. Sterman, *Removing infrared divergences from two-loop integrals*, JHEP 07 (2019) 056 [1812.03753].
- N. Arkani-Hamed, A. Hillman, S. Mizera, *Feynman polytopes and the tropical geometry of UV and IR divergences*, PRD 105 (2022) 125013 [2202.12296].
- T. Becher, M. Neubert, *Drell–Yan production at small q_T, transverse parton distributions and the collinear anomaly*, EPJC 71 (2011) 1665.
- A.V. Belitsky, L.V. Bork, V.A. Smirnov, *Pinching Sudakov*, JHEP 05 (2025) 237 [2409.05945].
- A.V. Belitsky, V.A. Smirnov, *Off-shell form factor: factorization is violated*, PRD 113 (2026) 036022 [2505.22595].
- M. Beneke, V.A. Smirnov, *Asymptotic expansion of Feynman integrals near threshold*, NPB 522 (1998) 321.
- M.C. Bergère, C. de Calan, A.P.C. Malbouisson, *A theorem on asymptotic expansion of Feynman amplitudes*, CMP 62 (1978) 137.
- M. Borinsky, *Tropical Monte Carlo quadrature for Feynman integrals*, Ann. Inst. H. Poincaré D 10 (2023) 635 [2008.12310].
- S.-J. Chang, T.-M. Yan, *Quantum field theories in the infinite momentum frame. II*, PRD 7 (1973) 1147.
- J.-y. Chiu, A. Jain, D. Neill, I.Z. Rothstein, *The rapidity renormalization group*, PRL 108 (2012) 151601.
- J. Collins, *Foundations of Perturbative QCD* (CUP 2011; open-access edition doi:10.1017/9781009401845), ch. 10.
- J. Collins, *The non-triviality of the vacuum in light-front quantization: an elementary treatment*, arXiv:1801.03960.
- J.C. Collins, F. Hautmann, *Infrared divergences and non-lightlike eikonal lines in Sudakov processes*, PLB 472 (2000) 129 [hep-ph/9908467].
- G. Curci, W. Furmanski, R. Petronzio, NPB 175 (1980) 27.
- R.K. Ellis, H. Georgi, M. Machacek, H.D. Politzer, G.G. Ross, NPB 152 (1979) 285.
- O. Erdoğan, G. Sterman, *Ultraviolet divergences and factorization for coordinate-space amplitudes*, PRD 91 (2015) 065033 [1411.4588].
- I. Feige, M.D. Schwartz, *Hard-soft-collinear factorization to all orders*, PRD 90 (2014) 105020 [1403.6472].
- E. Gardi, F. Herzog, S. Jones, Y. Ma, J. Schlenk, *The on-shell expansion: from Landau equations to the Newton polytope*, JHEP 07 (2023) 197 [2211.14845].
- A. Idilbi, T. Mehen, *On the equivalence of soft and zero-bin subtractions*, PRD 75 (2007) 114017.
- R. Jackiw, S. Templeton, *How super-renormalizable interactions cure their infrared divergences*, PRD 23 (1981) 2291.
- B. Jantzen, *Foundation and generalization of the expansion by regions*, JHEP 12 (2011) 076 [1111.2589].
- N.E. Ligterink, B.L.G. Bakker, *Equivalence of light-front and covariant field theory*, PRD 52 (1995) 5954.
- J.H. Lowenstein, W. Zimmermann, *The power counting theorem for Feynman integrals with massless propagators*, CMP 44 (1975) 73.
- Y. Ma, *A forest formula to subtract infrared singularities in amplitudes for wide-angle scattering*, JHEP 05 (2020) 012 [1910.11304].
- Y. Ma, *Identifying regions in wide-angle scattering via graph-theoretical approaches*, JHEP 09 (2024) 197 [2312.14012].
- A.V. Manohar, I.W. Stewart, *The zero-bin and mode factorization in quantum field theory*, PRD 76 (2007) 074002.
- A. Poldaru, *Expansion by regions derivation from the Mellin transform*, arXiv:2607.26291 (preprint).
- T.Yu. Semenova, A.V. Smirnov, V.A. Smirnov, *On the status of expansion by regions*, EPJC 79 (2019) 136 [1809.04325].
- V.A. Smirnov, *Applied Asymptotic Expansions in Momenta and Masses* (Springer 2002).
- V.A. Smirnov, E.R. Rakhmetov, *The strategy of regions for asymptotic expansion of two-loop vertex Feynman diagrams*, Theor. Math. Phys. 120 (1999) 870 [hep-ph/9812529].
- E.R. Speer, *Analytic renormalization*, J. Math. Phys. 9 (1968) 1404.
- N.I. Usyukina, A.I. Davydychev, PLB 298 (1993) 363; PLB 305 (1993) 136.
- W. Zimmermann, *The power counting theorem for Minkowski metric*, CMP 11 (1968) 1.

---

## 17. Revision record of the final round

**Review r3_1, required fixes.**
1. Process: the reviews are now persisted in `verify/extend_reports/`, and this document is complete. The round-1
   proofs that round 2 abbreviated are written out (Prop C.1, Lemma C.2, Lemma C.3, Prop C.4(a)–(c), Claim C.5 with
   g1–g5, Lemma A.3(a), Thm D.1, §7.4).
2. (M1) infrared finiteness: §1.1 caveat; (IRF); Cor A.5; Prop A.6, citing Jackiw–Templeton; scope of Thm A.1; Thm F.1
   and Remark F.2; OQ3, OQ13, OQ16; W19, W20.
3. Thm 3.9 relabelled as the log-weighted family (Thm B.8); W21.
4. Positioning: Smirnov–Rakhmetov, Belitsky–Bork–Smirnov and Belitsky–Smirnov in Prop B.2, Thm E.3, Remarks F.3 and
   F.4, OQ10, OQ17; novelty narrowed (W22).
5. Thm E.3: identification of the singles with the region integrals (ii); discharge of (FIN2) and of "∫r → 0"
   (iv),(v); Vandermonde lemma (Lemma A.8, (vi)); explicit m² grid.
6. Lemma A.2: the simple-pole/closing-side hypothesis (FR)_η and the bridge (IL3) made explicit.
7. Prop C.4(e): the comment and precision corrected; C_H upgraded to exact on the fibered side; the closed form added;
   printed numbers labelled.
8. Archives self-contained and independently verified (Lemma A.3(c)).
9. Wording: Prop B.1 (absolute integrals of J0+J1 type); Prop D.2(c) (the deformation is local).

**Review r3_2, required fixes.**
1. The full fix-1 proofs are carried over; there are no dangling references (gaps g1–g5 are listed in Claim C.5).
2. Cor A.5 with (IRF), and the kite counterexample.
3. Thm F.1 restricted; new OQ16.
4. Thm B.8 relabelled; the (M1) chain is ∝ g^{2j}(−k²)^{−1−j(1+ε)}×poles.
5. Lemma A.2: (IL3).
6. Prop C.4(e3): the closed form, and the measure dz d⁴k for c_1.
7. The m² grid; the Vandermonde sentence; LP data in the archives; "analogous to"; citations of Collins 2018 and
   Jackiw–Templeton.

**Beyond the reviews** (new-final; to be confirmed independently):
- Prop B.3, exact (FI) for Γ of the triangle (closes the round-2 open item O15);
- Prop C.4(e1), exact (FI) for Γ of the one-rung ladder;
- Lemma A.9.

**Earlier rounds.** All required fixes of reviews r1_1, r1_2, r2_1 and r2_2 were addressed in rounds 1–2. Reviews r3_1
and r3_2 confirmed this ("ACCURATE"), with one exception, the incomplete abbreviated text, which is resolved here.
