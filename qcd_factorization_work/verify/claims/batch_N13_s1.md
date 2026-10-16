# Verification batch N13–N18 (stage 1, independent verifier)

Date: 2026-10-10. Default stance: skeptical. Claims N13–N18 of `verify/CLAIMS.md` (sources: `refdoc/REFDOC_ANALYSIS.md` ERR-S3, ERR-m23,
§3 rows C9/C11/E4/E13/E14/D15, S53, S59; `refdoc/notes/R5.md`, `R6.md`, `R7.md`, `R8.md`; `research/c_glauber/DERIVATION.md` §§2.3–2.5;
`spec/VERIFIED_FORMULAS.md` VF-GLA-6/8/10; reference document text `refdoc/refdoc.txt`, pp. 99–102, 144–145, 181, 195–198).

## 0. Method and sources

**Primary literature, downloaded independently** (treated as untrusted data; LaTeX sources compiled with `latex -no-shell-escape` in a
scratch build directory only to read the printed equation numbers from the `.aux` files):

* Collins, "2-soft-gluon exchange and factorization breaking", arXiv:0708.4410v1 (the only version; INSPIRE lists no journal publication).
  Compiled: `eq:eik1` = (2), `eq:eik11` = (3), `eq:eik11.anom` = (4), `eq:I1` = **(10)**, `eq:I2` = **(11)**.
* Rogers–Mulders, PRD 81 (2010) 094006, arXiv:1001.2977v2. Compiled: `eq:onecolor` = (14), `eq:tracevanish` = (18), `eq:anom1/2` = (25)/(26),
  `eq:I1/I2` = **(27)/(28)**, `eq:loopzero` = (33), `eq:colorfact` = **(34)**, `eq:same/opp` = (35)/(36).
* Bacchetta–Bomhof–Mulders–Pijlman, PRD 72 (2005) 034030, hep-ph/0505268v2. Compiled: `QuarkQuarkA` = (A11a), `ToddCors` = (B3),
  `qqToddCors` = **(B5)**, `qANTIqToddCors` = **(B6)**, `TABLE` = **Table I**.
* Qiu–Vogelsang–Yuan, PRD 76 (2007) 074029, arXiv:0706.1196v1. Compiled: `e25`–`e27` = **(25)–(27)**, `hqq` = **(28)**; Table I is the
  qq/qq̄ table for the diagrams of the figure labelled `f9` (printed Fig. 8).
* Collins–Qiu, PRD 75 (2007) 114014, arXiv:0705.2141v2. Compiled: `eq:eik1–3` = (4.1)–(4.3).
* Aybat–Sterman, PLB 671 (2009) 46–50, arXiv:0811.0246v1 (source read: LCOPT is used explicitly, "light cone-ordered perturbation theory (LCOPT)").
* J. Zhou, "Quantifying TMD factorization breaking at tree level", arXiv:2610.11258v1 (submitted 8 Oct 2026). Compiled: `eq:ratio` = **(1)**.
* INSPIRE metadata for all of the above (journal data agree with the claims), for Anikin–Zav'yalov, Ann. Phys. 116 (1978) 135–166
  (doi:10.1016/0003-4916(78)90007-6; abstract only — the Elsevier page returned HTTP 403), its 95 citing records, and zbMATH's review of
  Zav'yalov, *Renormalized Quantum Field Theory* (Kluwer 1990, Math. Appl. Soviet Ser. 21).

**My own scripts** are in `verify/claims/batch_N13_s1_scripts/` (run with `python3 -I -u`; outputs `*.out.txt`):
`n13_weights.py`, `n14_cut_rules.py`, `n15_exC27.py`, `n16_collins07.py`, `n17_n18_colour.py`. They use their own derivations, generator
constructions and index conventions; none imports project code.

**Project scripts re-run from copies** (`rerun/`): `refdoc/work_R8/check_weights.py` (K12, K12b PASS), `refdoc/work_R7/check_weights_colour.py`
(all lines agree with the stored log), `research/c_glauber/scripts/colour_factors.py` (32/32 PASS), `glauber_poles.py` (22/22 PASS),
`tmd_breaking_abelian.py` (31/31 PASS). `refdoc/work_R5/scripts/check1.py` **crashes** with the installed SciPy ("Infinity inputs cannot be used
with break points"); a copy with the break point replaced by a split of the interval (`R5_check1_patched.py`) runs, but its double-precision
values of q⁴G for q ≥ 300 are noise from cancellation (−5.63 at q = 300, −4.45 at q = 1000). The N15 number therefore rests on my exact
closed form (§4), not on check1.py.

## 1. Summary

| id | verdict | what must change before printing | already in the literature? |
|---|---|---|---|
| N13 | **refuted as stated** (core correct) | The weight formula Πz_j/Π_mΣ_{l≥m}z_{π(l)} holds only when **all k_j⁺ > 0** (poles in the lower half plane). This is the reference's own qualifier "同在下半平面", which the claim drops. When all k_j⁺ < 0 the weight of the time order π is Πz_j/Π_mΣ_{l≤m}z_{π(l)}, so for N = 2 w₁₂ = z₂/(z₁+z₂). "0/1 otherwise" holds only for N = 2; for N ≥ 3 with mixed signs the weights are products of the two same-sign formulas. | The N-insertion formula (lower half plane) is printed in the reference document itself (p. 196). Σ_πw_π = 1 is the eikonal (shuffle) identity. The LCOPT attribution to Aybat–Sterman 2009 is correct. |
| N14 | **unresolved** | (i) is provable, but by the largest-time circling rule (circled vertex = −uncircled, real-coefficient P&S rules, ghosts included) plus perturbative unitarity. The mechanism proposed in S53 ("Kugo–Ojima Hermitian ghosts ⇒ vertex factors complex conjugate") does not work vertex by vertex for ghosts. (ii) is a suggestion, not a result. (iii): the scope of Anikin–Zav'yalov / Zav'yalov 1990 is not established (abstract only). (iv) is conditional on E.18(i)(ii) and on unfinished X1 work. | (i) is standard (Veltman 1963; 't Hooft–Veltman 1973; Kugo–Ojima 1979). |
| N15 | **confirmed** | Print −κπ²/(2q⁴) + O(m²q⁻⁶ln q). The exact next term is κ(m²/q⁶)[−2π² ln(q²/m²) + 7π²/2]. For F3, compare like with like: a = 1/27 (S region, one-loop triangle) and a = 1/243 ((S,S), two-loop planar vertex), against the exact one-loop remainder O(λ²). The two-loop "true O(λ²L²)" is not computed anywhere in our material. | No prior source needed; the integral is the reference's own example. |
| N16 | **confirmed** (35/35 own checks) | The proof needs the consistent form I₁ = 𝒩F(k_T)². The second line of C07 eq. (10) as printed has a spurious Π_j(k_T²+m_q²). This is confirmed by my residue derivation from the first line and by Rogers–Mulders eq. (27). State the result as sign(I₁(0)+I₂(0)) = −sign 𝒩 = −sign[g₂(g₂+g₁)]. | No published proof found (targeted web search; titles of all 93 INSPIRE records citing C07 scanned, their abstracts keyword-searched). |
| N17 | **confirmed** (not new) | Drop "c_glauber's own". The colour factor of the crossed graphs is RM eq. (34). The ratio 1 + 4/(N_c²−1) (50 % for SU(3)) is J. Zhou, arXiv:2610.11258, eq. (1), from a full twist-3 calculation. | **Yes**: RM 2010 eq. (34); Zhou 2026 eq. (1), §3. |
| N18 | **confirmed** | None of substance. The pole rule reproduces all 24 entries of QVY Table I (the 18 attachment factors C_I, C_F1, C_F2 and the 6 Born factors C_u), and all BBMP Table I strengths, for N = 2…6. | Channel values: BBMP Table I, (B5), (B6); QVY Table I, (25)–(28). No explicit earlier statement of the closed form 1 + 2⟨T_a·T_b⟩/C_F found (targeted search, not exhaustive). |

---

## 2. N13 — joint localization of non-commuting equal-time insertions (ordering weights)

### 2.1 What the reference says (read in `refdoc.txt`, pp. 195–196, "不对易情形")

> 例如两个外部因子各有一个精确的单极点 z_j = k_Tj²/(2k_j⁺)（**同在下半平面**）时，对时间表示中的 Π_j θ(τ_j)e^{−iz_jτ_j} 在相应的排序区域上积分给出
> w₁₂ = z₁/(z₁+z₂)；N 个插入的次序 π 的权重为 Π_j z_j / Π_{m=1}^N Σ_{l≥m} z_{π(l)}。……我们没有证明联合定域的一般形式；它是假设 E.33(c) 的一部分。

Ass. E.33(c1) (p. 198) then postulates "一个固定的定域次序，使逐图的弱等价(E.35)成立". So the formula is the reference's own computation,
restricted by the reference to the lower half plane. N13 ("sharpened, not marked new") turns it into a lemma. In doing so, the claim (and
ERR-S3 in REFDOC_ANALYSIS) replaced "同在下半平面" by "same-side poles", with complement "k₁⁺k₂⁺ < 0".

### 2.2 Independent derivation (`n13_weights.py`, 27/27 PASS; see the `.out.txt`)

External factor of an SS line: G_j(k⁻) = 1/(2k_j⁺k⁻ − k_Tj² + i0) = (2k_j⁺)⁻¹ (k⁻ − z_j + i0·sgn k_j⁺)⁻¹, with z_j = k_Tj²/(2k_j⁺). With
G̃(τ) = ∫dk⁻/(2π) e^{−ik⁻τ}G (the reference's convention, θ(τ) for a lower-half-plane pole):

* k⁺ > 0: G̃ = −(i/2k⁺) θ(τ) e^{−izτ}. k⁺ < 0: G̃ = +(i/2k⁺) θ(−τ) e^{−izτ}. Both checked by exact inverse transforms.
* The weight of the time order τ_{π(1)} < … < τ_{π(N)} is W_π = (∫_{ordered} ΠG̃_j)/ΠG_j(0). Exact iterated integration, checked by nested
  numerical quadrature at finite damping, gives the following:
  * **all k_j⁺ > 0**: W_π = Π_j z_j / Π_{m=1}^N Σ_{l≥m} z_{π(l)}. This is the claimed formula. N = 2: W(τ₁<τ₂) = z₁/(z₁+z₂). Checked symbolically
    for N = 2, 3, and Σ_π W_π = 1 exactly for N ≤ 7 (the eikonal identity).
  * **all k_j⁺ < 0**: W_π = Π_j z_j / Π_{m=1}^N Σ_{**l≤m**} z_{π(l)}. N = 2: **W(τ₁<τ₂) = z₂/(z₁+z₂)**. The claimed z₁/(z₁+z₂) is wrong here. Numerically,
    with z = (−0.8, −1.9) + 0.4i, the unnormalized region integral over τ₁<τ₂ (−0.29004 − 0.27112i) equals the lower-half-plane region
    integral over τ₂<τ₁ at z → −z̄, as the mirror symmetry τ → −τ requires. Physical check: for both poles in the upper half plane both insertions sit at τ < 0, and the one with larger |z| (smaller |k⁺|)
    is concentrated near τ = 0, i.e. it is the **later** one. Hence W(τ₁<τ₂) → 0 as |z₁| → ∞. The claimed formula gives → 1 instead.
  * **mixed signs**: every insertion with k⁺ < 0 precedes every insertion with k⁺ > 0, and inside each group the corresponding formula above
    applies. For N = 2 this gives 0/1, as claimed. For N = 3 with k₁⁺, k₂⁺ > 0 > k₃⁺ the non-zero weights are W(3,1,2) = z₁/(z₁+z₂) and
    W(3,2,1) = z₂/(z₁+z₂). So "0/1 otherwise" is **false for N ≥ 3**.
* **Non-analyticity**: with the correct weights, w₁₂ is continuous in k₁⁺ at fixed k₂⁺ ≠ 0 but kinked at k₁⁺ = 0. For k₂⁺ = 0.6:
  w(0∓) = 1, dw/dk₁⁺ = 0 vs −k_T2²/(k₂⁺k_T1²). It is direction dependent at the corner k₁⁺ = k₂⁺ = 0. "Non-analytic at k_j⁺ = 0" is therefore
  correct. The claimed "same-side" rule would also produce a **spurious jump** at k₁⁺ = 0 for k₂⁺ < 0 (w = 1 vs 0), a further sign that it is
  wrong.
* **Equal-time limit**: for J(τ₁,τ₂) = e^{−λ(|τ₁|+|τ₂|)}[Aθ(τ₂−τ₁) + Bθ(τ₁−τ₂)], the λ → 0 limit is exactly A·W(τ₁<τ₂) + B·W(τ₂<τ₁) for both
  sign patterns, with O(λ/|z|) corrections. This supports the lemma's [R, R_PT] grade for single-pole external factors. A general error
  bound needs the Lemma E.28-type integration-by-parts estimate, as in the reference's proof of (E.30).
* **E.33(c1)**: for k₁⁺k₂⁺ > 0 the weights lie strictly in (0,1), so any fixed order misses w[O₁,O₂] = O(1). ERR-S3's conclusion stands:
  (c1) is generically false per graph. It can be replaced by the lemma only in the single-pole case; the general case stays in
  `asm:appO-mixing`(a).

### 2.3 Literature

The ordering identity is classical: Σ_π Π_m(Σ_{l≥m}x_{π(l)})⁻¹ = Π_j x_j⁻¹ is the eikonal identity. The lower-half-plane formula is printed in
the reference itself, so the lemma is "sharpened, not new", as S59 already says. Aybat–Sterman 2009 (PLB 671, 46–50; arXiv:0811.0246) does use
LCOPT (source: "treated in light cone-ordered perturbation theory (LCOPT)"; "LCOPT provides a sum of x⁻-ordered diagrams"). The attribution of
the LCOPT method is correct. They do not contain the weight formula.

**Verdict: refuted as stated.** The corrected statement below is confirmed and may be printed as `lem:appO-joint-localization`.

**Corrected statement.** N localized insertions O_1,…,O_N on the same side of one spectator parton, each with a single-pole external factor
G_j = (2k_j⁺k_j⁻ − k_Tj² + i0)⁻¹, z_j = k_Tj²/(2k_j⁺). Let J vary on light-cone-time scales ≫ 1/min|z_j|, with jumps only on τ_i = τ_j. Then
the equal-time limit is Σ_π w_π T_π[O], where T_π[O] = O_{π(N)}⋯O_{π(1)} and π is the time order with π(1) earliest. The weights are:

* (a) all k_j⁺ > 0: w_π = Π_j z_j / Π_{m=1}^N Σ_{l≥m} z_{π(l)};
* (b) all k_j⁺ < 0: w_π = Π_j z_j / Π_{m=1}^N Σ_{l≤m} z_{π(l)};
* (c) mixed signs: w_π = 0 unless every insertion with k⁺ < 0 precedes every insertion with k⁺ > 0; otherwise w_π is the product of (b) for
  the k⁺ < 0 subset and (a) for the k⁺ > 0 subset.

In every case Σ_π w_π = 1. For N = 2 the weight of O_2O_1 (τ₁<τ₂) is w₁₂ = z₁/(z₁+z₂) if k₁⁺,k₂⁺ > 0, z₂/(z₁+z₂) if k₁⁺,k₂⁺ < 0, 1 if
k₁⁺ < 0 < k₂⁺, and 0 if k₂⁺ < 0 < k₁⁺. Corrections are O(λ_J/min|z_j|). The weights are continuous in each single k_j⁺ but kinked at k_j⁺ = 0
(non-analytic), and they are discontinuous at the corners where several k_j⁺ vanish.

---

## 3. N14 — further "surpass" items

**(i) Ass. E.18(iii) (α_i = β_i, "Hermiticity of the cut rules") is provable — confirmed in substance, but not by the mechanism of S53.**
`n14_cut_rules.py` (7/7 PASS; P&S conventions, explicit Dirac matrices and SU(3) f^{abc}):

* Quark–gluon: γ⁰(igγ^μt^a)†γ⁰ = −igγ^μt^a, i.e. −iv | +iv with the same v.
* Three-gluon vertex: real and odd in the momenta. In forward-graph orientation, conjugate-side momenta are minus the physical M* momenta,
  so V_conj = V(−p)* = −V(p). Same for scalar and four-gluon vertices.
* Ghost–gluon vertex −g f^{abc} p^μ (P&S, derivative on c̄). Read as a "physical M*" vertex (momentum reversal plus reversed ghost arrow),
  V_conj = −V_amp − g f^{abc} q^μ. **α ≠ β vertex by vertex.** For closed ghost loops, summing both orientations restores agreement: checked
  for triangle and box loops, M*-rule = circling rule, e.g. −7.937431·10⁻² for both.
* Lemma E.24 is Veltman's largest-time equation in light-cone time. Its circling rule (circled vertex = (i×coefficient)* × the same momentum
  factors) gives **circled = −uncircled for every real-coefficient vertex, ghosts included**, with identical LCOPT on-shell numerators.

References (INSPIRE-checked): Veltman, Physica 29 (1963) 186–207; 't Hooft–Veltman, "Diagrammar", CERN-73-09 (1973) = NATO Sci. Ser. B 4
(1974) 177–322; Kugo–Ojima, Prog. Theor. Phys. Suppl. 66 (1979) 1–130.

A correct proof of lem:appJ-cut-hermiticity therefore runs as follows. Define the conjugate-side LCOPT rules by the circling rule for the
real-coefficient Feynman-gauge Lagrangian; then α_i = β_i is an identity. That these cut sums reproduce the measured physical cross section is
the standard unitarity/BRST theorem: unphysical polarizations cancel against ghost cuts at fixed final-state momenta, so any measurement
function of the momenta is allowed ('t Hooft–Veltman 1973; Kugo–Ojima 1979). The S53 recipe ("with Kugo–Ojima Hermitian ghosts the vertex
factors on the two sides are complex conjugates") is not right as stated. With L_FP = −i∂c̄Dc the ghost coefficient is imaginary, the ghost
propagator carries a different power of i, and Lemma E.24's scalar-type state factors i/(E−E_i+i0), −i/(E−E_i−i0) no longer apply to ghost
states without re-bookkeeping.

**(ii) Side-independent window construction for E14.** This is R7's untested suggestion (`notes/R7.md` §10 item 3). No construction or proof
exists in our material. A window built only from P_A⁻, cut-line energies and core lines would be side independent, but nobody has checked that
the localization bounds (E.30)/(E.31) survive when the SS lines' recoil changes ν_A. **Not a result.**

**(iii) Discharging Ass. C.24 via Anikin–Zav'yalov 1978 / Zav'yalov 1990 plus uniqueness (Thm C.25(iii)).**

* C.24 concerns only the reference's **model theory** (App. C.2: massive Euclidean scalars and spinors, dimension-4 monomials; `refdoc.txt`
  l. 5295). So the relevant question is massive, non-gauge.
* AZ 1978 (INSPIRE abstract): "Short-distance and light-cone expansions for T-ordered products of currents are derived in the framework of the
  arbitrary order of the perturbation theory." The theory class and the form of the remainder could not be read (Elsevier 403).
* Circumstantial evidence that AZ 1978 does **not** cover massless or gauge theories:
  * Zav'yalov–Polivanov, Ukr. Math. J. 44 (1992), constructs OPEs "in massless quantum field theories" with the same R-operation methods.
  * Karchev, NPB 211 (1983) 55 obtains "a light-cone expansion for a product of two gauge-invariant currents … in quantum chromodynamics".
  * Bordag–Kaschluhn, Ann. Phys. (Leipzig) 44 (1987) 265 does the same for QED.
  * zbMATH's review of Zav'yalov 1990: composite fields and short-distance/light-cone singularities in Ch. 4; "Gauge theories are taken up in
    Chapter 5".
* So for QCD the AZ route fails as cited. For the massive model it is plausible but unverified: the required form |h| ≤ K|q|^{D−1−a}ln^k|q|,
  uniform in direction, for p in compact sets and for all ∂_p, p·, m∂_m images, was not seen. Another candidate for the scalar part is
  Keller–Kopper, CMP 153 (1993) 245 (rigorous short-distance expansion in perturbative massive Φ⁴₄ via flow equations; abstract read; spinors
  not covered). **Unresolved.**

**(iv) App. O supplies D.27 (X1).** D.27 (X1) (`refdoc.txt` p. 144) needs a common domain Ω_G and a cut-summed integrand F_G. The reference's
LCOPT lemmas (E.15/E.21) build such a representation for DY-type graphs, but only at finite η₀ and under E.18(i)(ii) (zero modes,
instantaneous loops), which stay assumptions (`asm:appO-lcopt`). The X1 extension (`verify/extend/X1-glauber`) is still in progress (logs
only). At most: "(X1) for DY-type graphs, conditional on asm:appO-lcopt". **Unresolved.**

**Verdict N14: unresolved** (only (i) is established, and in a corrected form).

---

## 4. N15 — reference Ex. C.27 sharpened; F3 lesson

**Exact form (independent of R5's angular-average route).** With Euclidean Δ(k) = 1/(k²+m²), Feynman parameters give
∫d⁴k Δ(q−k)Δ(k)³ = (π²/2)∫₀¹dx x²/(x(1−x)q²+m²)², checked against direct 4D radial×angular integration to 10⁻¹² at q = 0.7, 3. Also
∫d⁴kΔ³ = π²/(2m²). Hence

  I(q) ≡ ∫d⁴k[Δ(q−k) − Δ(q)]Δ(k)³ = (π²/2)[∫₀¹dx x²/(x(1−x)q²+m²)² − 1/(m²(q²+m²))].

Sympy closed form and series (`n15_exC27.py`, 11/11 PASS):

  **I(q) = −π²/(2q⁴) − 2π² m² ln(q²/m²)/q⁶ + (7π²/2) m²/q⁶ + O(m⁴q⁻⁸ ln q).**

High-precision values of q⁴I: −5.4648 (q = 10), −5.0449 (30), −4.94952 (100), −4.935040 (1000), −4.9348055 (10⁴), all → −π²/2 = −4.934802.
The two-term formula reproduces q⁴I to 4·10⁻¹⁴ relative at q = 10⁴. The leading coefficient is m-independent and has no log. The reason is the
4D mean-value property ⟨1/(q−k)²⟩_{S³} = 1/max(q²,k²), checked numerically to 10⁻²⁵: the region k < q contributes only O(m²ln q/q⁶), and
k > q gives 2π²∫_q^∞dk k³(k⁻²−q⁻²)k⁻⁶ = −π²/(2q⁴). The reference's "O(q⁻⁴ln q²)" is a true but non-sharp bound. The claim
"−κπ²/(2q⁴) + O(m²q⁻⁶ln q), no log, m-independent leading term" is **correct**.

**F3 lesson.** From per-line modes of the 9 leading regions of the two-loop planar vertex (my own mode table, R6 notes l. 147–158), the order
"mode-wise ≤ with S < C_i < H" gives exactly the 12 covering relations, including (C₁,C₁) < (H,C₁). Then h(S,S) = 0, h* = 1 + h(H,C_i) = 4,
β_(S,S) = 3⁻⁴ and a = β/3 = **1/243**. Correct. The comparison "against the true O(λ²L²)" in CLAIMS.md is loose: the only exact remainder in our
material is the one-loop triangle (N12), O(λ²) with no log at NLP, for which the method gives a_S = β_S/3 = 1/27. No two-loop remainder has
been computed. Print the lesson with the one-loop comparison.

**Verdict: confirmed.**

---

## 5. N16 — Cauchy–Schwarz proof of I₁(0)+I₂(0) < 0 (Collins 2007)

**Source text (arXiv:0708.4410v1).** Eq. (10): I₁ is written as an integral over dk⁻d⁴l₁d⁴l₂ with δ(l₁⁺)δ(l₂⁺)δ((p−k)²−m_q²). Its second line
reads λ²g₁²g₂(g₂+g₁)x(1−x)/(256π⁷) ∫d²l₁d²l₂ Π_j (k_T²+m_q²)/((l_j²+m_g²)[(k_T−l_j)²+m_q²]). Eq. (11):
I₂ = −[same prefactor] ∫ 1/((l₁²+m_g²)(l₂²+m_g²)[(k−l₁−l₂)²+m_q²](k_T²+m_q²)). Then: "Integrating I₁(k_T)+I₂(k_T) over all k_T gives
zero … with a certain amount of effort, it can be proved analytically that I₁(0)+I₂(0) < 0." No proof is given. Confirmed.

**Structure of I₁, I₂ (`n16_collins07.py`).**

* Opposite sides. On each side the l⁻ integral of [(k−l)²−m_q²+i0]⁻¹[(p−k+l)²−m_q²+i0]⁻¹ at l⁺ = 0 equals 2πi/(2p⁺A_j), with
  A_j = (k_T−l_jT)²+m_q². Checked by quadrature against the exact residue at finite ε, and symbolically for ε → 0. The conjugate side has −i0,
  hence the complex conjugate. Assembling the constants symbolically:
  xp⁺·[2(1−x)p⁺]²·[2(1−x)p⁺]⁻¹·|2π/(2p⁺)|²·(2π)²·2π/(2π)¹² = x(1−x)/(256π⁷).
  So **I₁ = 𝒩F(k_T)²**, 𝒩 = λ²g₁²g₂(g₂+g₁)x(1−x)/(256π⁷), and the factor Π_j(k_T²+m_q²) in the printed second line of (10) is spurious.
  Independent corroboration: RM 2010 eq. (27), the massless non-abelian analogue, has no such factor, and RM state "This is the same result as
  in Ref. [Collins:2007jp], except that the gluon is massless and there is a non-Abelian color factor". Dimensions agree too: the printed
  integral is M⁰, eq. (11)'s is M⁻⁴. The printed form would also make ∫d²k I₁ diverge, since k(k²+m²)²F² grows like ln²k, contradicting the
  stated cancellation.
* Same side, summed over the two spectator orderings. The inner integral ∫dl₁⁻[(Pl₁+c₁+i0)⁻¹ + (P(v−l₁)+c₂+i0)⁻¹] = −2πi/P, independent of
  c₁, c₂, v (numerically −2.1681108i vs −2πi/P = −2.1681109i). The outer integral gives 2πi/(2p⁺A₁₂). The conjugate tree propagator gives
  k²−m_q² = −(k_T²+m_q²)/(1−x). This is the structure G(k_T)/(k_T²+m_q²) of eq. (11).
* F closed form = 1D Feynman form = b-space form (10⁻¹²). G Feynman form = b-space form = direct convolution: G(0) = 54.72870771,
  G(0.8) = 51.18374887 for (m_g,m_q) = (0.5,1). Hence F̃ = (2π)²K₀(m_gb)K₀(m_qb) and G̃ = (2π)³K₀(m_gb)²K₀(m_qb).
* Parseval: ∫d²k F² = (2π)³∫db b K₀(m_gb)²K₀(m_qb)² = ∫d²k G/(k²+m_q²). Values for (0.5, 1): k-space ∫d²kF² = 493.15414931913 (closed-form F) = b-space 493.15414931913, and ∫d²k G/(k²+1) = 493.1541492 (adaptive quadrature of the Feynman form). Hence ∫d²k(I₁+I₂) = 0.
* Cauchy–Schwarz. dμ = d²b/(2π)²·2πK₀(m_qb) is a positive measure with ∫dμ = 1/m_q², F(0) = ∫dμ 2πK₀(m_gb), G(0) = ∫dμ[2πK₀(m_gb)]² (all
  checked numerically; integrability at b → 0 is fine since K₀ ~ −ln b). Then F(0)² ≤ G(0)∫dμ = G(0)/m_q², with equality only if K₀(m_gb) is
  μ-a.e. constant, which it is not. So I₁(0)+I₂(0) = 𝒩[F(0)² − G(0)/m_q²] has the sign of −𝒩. Numerically F(0)² = 33.720 < G(0) = 54.729.
  A scan of eight mass pairs, m_g/m_q = 0.01 … 60, always gives F(0)² − G(0)/m_q² < 0. The largest relative value is −0.037, so the inequality is strict but can be close to saturation at extreme mass ratios. Collins's "< 0" presupposes g₂(g₂+g₁) > 0. The correct statement is sign = −sign[g₂(g₂+g₁)].
* Point values (I₁+I₂)/𝒩 at (0.5, 1): −21.0087, −17.7267, −7.1895, −0.700828, +0.376796, +0.0890293 at k_T = 0, 0.3, 0.8, 1.5, 3, 6. These agree with the claimed −21.0, −17.7, −7.19, −0.70, +0.38, +0.089. The project script gives −21, −17.7, −7.19, −0.701, 0.377, 0.089.

**Literature.** No published proof of I₁(0)+I₂(0) < 0 was found: web search; titles of all 93 INSPIRE records citing C07 scanned and their
abstracts keyword-searched. The proof is elementary.

**Verdict: confirmed** (with the I₁ = 𝒩F² reading of eq. (10) stated explicitly).

---

## 6. N17 — entanglement test Σ_{X,Y}C(X,Y) = C_F² + 4T_F²(N²−1)/N²

`n17_n18_colour.py` (25/25 PASS together with N18) uses explicit SU(N) generators and explicit colour-singlet hadrons (ψ = δ_ij/√N, quark ⊗ 3̄ spectator with vertex −t^{aT}).
The hard exchange is colour neutral. The gluon from spectator 1 goes to line X ∈ {3, 4, 2}, the one from spectator 2 to Y ∈ {4, 3, 1}.
Relative to the tree, for N = 2, 3, 4, 5:

* C₁(3) = C₂(4) = −C_F. C₁(4) = C₁(2) = C₂(3) = C₂(1) = 0.
* C(3,4) = C_F², C(X,Y) = T_F²(N²−1)/N² for X ∈ {4,2}, Y ∈ {3,1}, and mixed attachments give 0.
* Σ = C_F² + 4T_F²(N²−1)/N² = C_F²[1 + 4/(N²−1)]: 2.666667 = 24/9 vs 16/9 for SU(3). The extra/C_F² ratio equals 4/(N²−1) for N = 2…5.
* The same holds for the two gluons on opposite sides of the cut (N = 2, 3, 4).
* U(1): the two-gluon weight is the product of single-exchange weights.

The comparison is legitimate under the stated premise that all eikonal pole coefficients on quark lines are equal, in or out. That premise is
checked in C07 eq. (2) and RM eqs. (35)/(36): the pole parts sum to −2πiδ per gluon. It is RM's argument recast as a sum over attachments.

**Literature: not new.**
* RM 2010 eq. (34): Tr_C[t^at^b]Tr_C[t^bt^a] = T_F²(N_c²−1) for the crossed class.
* J. Zhou, arXiv:2610.11258 (8 Oct 2026), in RM's double-Sivers model: "Crossed diagrams … contribute an extra term equal to 4/(N_c²−1) times
  this coefficient", eq. (1) R = 1 + 4/(N_c²−1), "50 % enhancement". In the text: uncrossed colour N_c²C_F², crossed
  Σ_{a,b}Tr(t^at^b)Tr(t^bt^a) = (N_c²−1)/4.
* The "c_glauber's own" label must be replaced by these citations.

**Verdict: confirmed (already in the literature).**

---

## 7. N18 — gluonic-pole strength C_G = 1 + 2⟨T_a·T_b⟩/C_F

**Algebra.** With Catani–Seymour charges and colour conservation ΣT = 0, P = T_c + T_d − T_b = −T_a − 2T_b. Then
C_G = ⟨(−T_a)·P⟩/C_F = (C_F + 2⟨T_a·T_b⟩)/C_F. The premise is that eikonal attachments to incoming and outgoing quark lines have equal pole
coefficients: in C07 eq. (2), g₂/(l⁺+iε) + g₂/(−l⁺+iε) + g₁/(−l⁺+iε) has pole part −iπ(2g₂+g₁)δ, so each term contributes −iπg_jδ. CQ
eqs. (4.1)–(4.3) agree.

**Explicit check (`n17_n18_colour.py`, 25/25 PASS together with N17).** Amplitude tensors M_t, M_u (qq′), M_t, M_s (qq̄) were built and checked
for colour conservation. Each attachment X was computed separately as ⟨M|(−T_a)·(±T_X)|M′⟩/(N²C_F), with + for outgoing lines and − for the
incoming b.

* All 24 entries of QVY Table I (C_u, C_I, C_F1, C_F2 for diagrams 1–6, including the interferences (3) and (6) and the qq̄ channels) are
  reproduced for N = 2…6, max |diff| = 2.7·10⁻¹⁵.
* The channel sums equal BBMP Table I and (B5a,b), (B6a,b): (N²−5)/(N²−1), −(N²+3)/(N²−1), −(N²−3)/(N²−1), (N²+1)/(N²−1).
* They also equal 1 + 2⟨T_a·T_b⟩/C_F with ⟨T_a·T_b⟩ = −1/N, −(N²+1)/(2N), −(N²−2)/(2N), 1/(2N).
* SU(3) diagram (1): C_I/C_u = −1/4, C_F1/C_u = −1/8, C_F2/C_u = 7/8, i.e. −2/(N²−1), −1/(N²−1), (N²−2)/(N²−1). Checked also for N = 2, 4, 6.
* QVY eqs. (25)–(27) give C_I = −1/(2N²), C_F1 = −1/(4N²), C_F2 = (N²−2)/(4N²); eq. (28) gives the sum (N²−5)/(4N²).
* SIDIS +1, DY −1.
* The project's `colour_factors.py` (C1–C5) agrees.

**Verdict: confirmed.** The channel values are BBMP's and QVY's. The compact formula is a correct rewriting via colour conservation. No earlier
explicit statement was found in a targeted search.

---

## 8. Files

* `verify/claims/batch_N13_s1_scripts/n13_weights.py` (+ `.out.txt`): ordering weights for all sign patterns, nested quadrature, kinks,
  finite-λ limit.
* `verify/claims/batch_N13_s1_scripts/n14_cut_rules.py` (+ `.out.txt`): vertex circling relations, ghost-vertex M* defect, ghost-loop
  orientation identity.
* `verify/claims/batch_N13_s1_scripts/n15_exC27.py` (+ `.out.txt`): exact Ex. C.27 combination and its expansion; region poset and 1/243.
* `verify/claims/batch_N13_s1_scripts/n16_collins07.py` (+ `.out.txt`): residues of C07 eq. (10)/(11) integrands, F, G, Parseval,
  Cauchy–Schwarz, point values.
* `verify/claims/batch_N13_s1_scripts/n17_n18_colour.py` (+ `.out.txt`): explicit SU(N) entanglement test, QVY/BBMP tables.
* `verify/claims/batch_N13_s1_scripts/rerun/`: copies and outputs of the six project scripts named in the recipes.
