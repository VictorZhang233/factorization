# Verification batch R-S1 to R-M7 (stage 1, independent verifier)

Date: 2026-10-10. Default stance: skeptical. All eleven claims are of kind `correction_of_reference_doc`. For each claim I checked two things. First, that the reference document (`factorization_qcd-2.pdf`, PDF page = printed page) really says what the claim says it says. Second, that the physics statement we would print is correct. I re-derived every formula myself, by a route different from the project scripts where I could, and read the cited literature in fresh downloads.

## 0. Method and sources

**My scripts.** All are in `verify/claims/batch_R-S1_s1_scripts/`, each with a `.log`. Run them with `python3 -I`.

| script | claims | result |
|---|---|---|
| `v2_rs1_propertime.py` | R-S1 | 29/29 PASS |
| `v2_rs2_colour.py` | R-S2 | 19/19 PASS |
| `v2_rs3_weights.py` | R-S3 | 9/9 PASS |
| `v2_rm12_triangle.py` | R-M1, R-M2 | 18/18 PASS |
| `v2_rm4_wilson.py` | R-M4 | 11/11 PASS |

**Project scripts re-run.** Every one reproduced.
- `refdoc/work_R3/scripts/eikonal_box.py` and `eikonal_box_closedform.py`: maximum relative deviation 4.67e−16.
- `refdoc/work_R4/checks_R4.py`: 21/21.
- `refdoc/work_R8/check_weights.py`: K12 and K12b PASS.
- `refdoc/work_R1/check_sudakov.py`, `check_sudakov2.py` and `check_kinematics_pc.py`.
- `research/c_regions/sudakov_regions.py`: 36/36.
- `research/c_wilson/scripts/s1_wilson_rules.py` (48/48), `s4_ward_tree.py` (97/97) and `s6_i0_poles.py` (8/8).

**Leftover scripts.** An earlier, interrupted run of this batch left `rs1_*.py`, `rs2_*.py`, `rs3_*.py`, `rm1_*.py`, `rm2_*.py` and `rm4_*.py` in the same folder. I re-ran them: 20, 12, 6, 6, 10 and 12 PASS, 0 FAIL. My verdicts do not depend on them.

**Reference pages read.**
- As text (`refdoc/refdoc.txt`): pp. 10–27, 52, 56–61, 73–74, 85–87, 156–158, 170, 195–204 and 214–219.
- As 150–200 dpi images: p. 11 (Fig. 4) and p. 217 ((E.51)).

**Literature.** Each item was downloaded fresh into my scratch area and treated as untrusted text.
- Rothstein–Stewart, arXiv:1601.04695 (JHEP 08 (2016) 025): source and PDF, §9 including eqs. (9.1), (9.18), (9.19), plus §5.2.1 and §7.2.
- Meggiolaro, hep-th/9602104 (Z. Phys. C 76 (1997) 523–535), §3, eqs. (3.20)–(3.40).
- Giordano–Meggiolaro, hep-ph/0602143 (PRD 74 (2006) 016003), eq. (4.24).
- Caron-Huot, arXiv:1309.6521 (JHEP 05 (2015) 093): INSPIRE abstract.
- Collins–Qiu, arXiv:0705.2141 (PRD 75 (2007) 114014): eqs. (2.1), (3.9), (3.12), (4.1)–(4.3).
- Collins–Soper–Sterman, hep-ph/0409313 (1989 review): §8.1, §8.6, §8.7, §9.1.
- Collins, arXiv:2007.04085: Theorems 1–3 and App. D.1.
- Collins, "Errata and updates for 'Foundations of Perturbative QCD'", dated 22 May 2026, from https://www.cantab.net/users/johncollins/qcdbook/qcd-errata.pdf: the p. 402 item.
- Aybat–Rogers, arXiv:1101.5057, §IV.
- INSPIRE records checked: Lowenstein–Zimmermann, CMP 44 (1975) 73–86; Usyukina–Davydychev, PLB 298 (1993) 363–370; Meggiolaro 1997; Giordano–Meggiolaro 2006.

## 1. Summary

| id | verdict | the point to print (short) |
|---|---|---|
| R-S1 | **confirmed**, scoped to the reference's own eikonal-spectator model | The residual −¼C_Aχ²X is an artefact of the strict window with independent symmetric cut-offs. Exactly, J_box = (2π/ab)(π+iY) and J_cross = −2πiY/(ab), so p_opp = −iY/π, Re p_opp = 0, and V†V = 1+O(χ³) with no real emission. The C_A term is the one-loop reggeization. (E.51) is arithmetically right; R4's −1/8 is a different quantity. **Not new:** Meggiolaro 1997 (3.26). |
| R-S2 | **confirmed** | The reference's combination reduces to −η_bT_a, which gives no TMD breaking and no Sivers flip. Correctly, the Glauber part ∝ T_a + 2T_b (equivalently P = −T_a − 2T_b in = out). SIDIS gives +T_a, DY gives −T_a, and Collins–Qiu give iπ(g_1+2g_2). |
| R-S3 | **confirmed** | The equal-time limit is w_12O_2O_1 + w_21O_1O_2 with w_12 = z_1/(z_1+z_2). A fixed order errs by w_21[O_1,O_2] = O(1), so Ass. E.33(c1) is false per graph. Replace it by the ordering-weight lemma. |
| R-S4 | **confirmed**, with a wording nuance | (0,0) gives p_J = −2 and (0,1) gives p_J = −1. The reference dismisses (0,0) in one line and never mentions (0,1). Both cancel only in gauge-invariant sums [A]. Their O(λ) and O(λ²) remainders are leading and build F^{+j}. |
| R-M1 | **confirmed** | Zero-momentum massless lines solve the Landau equations for any external momenta. In the Euclidean non-exceptional region they are the only solutions, and they are IR convergent (ω = A + ½A_q ≥ 2). |
| R-M2 | **confirmed** | (3.3) cannot be realised with real Euclidean vectors. Q²I = L² + π²/3 + t(2L² − 4L − 4 + 2π²/3) + O(t²L²). The regions statement is [P]. The reference's own App. D and Table 5 agree. |
| R-M3 | **confirmed** | The α-space analyticity theorem and the momentum-space trapping theorem are distinct (Collins 2020 Thms 1–3, App. D.1). Second-type singularities are not UV and are ignored on pp. 14–15. |
| R-M4 | **confirmed** | Fig. 4 is ambiguous and inconsistent with (2.7) and with its own last row. Correct rules (k_j flowing into the line): past ∏ i/(n·(k_1+…+k_j)+i0); future ∏ (−i)/(n·(k_j+…+k_m)−i0); vertex igt^an^μ. |
| R-M5 | **confirmed** | DIS: K_μν = k_μw_2ν/(k·w_2 − i0), with k flowing into H (future). DY: +i0 (past). Source: Collins (11.6) as listed in the 2026 errata. |
| R-M6 | **confirmed** (grade judgement) | The tree/abelian identity is [R]. The all-order non-abelian statement is [A]: the reference proves only the quark-line, colour-singlet-vertex case and cites the rest. |
| R-M7 | **confirmed** | (3.16) contains a literal "⋯". Use the precise definitions (8.2) (future: e⁺e⁻, SIDIS) and (E.48) (past: DY), with the i0 inherited from the replaced jet propagators. |

---

## 2. R-S1: the two-Glauber "residual"

### 2.1 What the reference says (read in full)

- **p. 57.** Under "independent weighting of the orderings by the strict instantaneous Glauber approximation", the reference says V†V ≠ 1 at N = 2, with a residual ∝ C_Aχ²T_A·T_B. Whether real soft emission from outside the window supplies the missing part "is the content of Ass. E.33(c)".
- **pp. 57–58, Prop. 9.3.** N ≥ 2 exchanges "do not cancel within the graphs of this model".
- **Fig. 36 caption.** The residual "does not cancel within these graphs".
- **p. 61 and p. 85.** "In the strict approximation within the Glauber window two exchanges leave the residual −¼C_Aχ²T_A·T_B, which can only be expected to cancel in the complete graph set including Glauber–soft mixing and real emission." On p. 61 this is reason (a) for grading DY B′, described as "the most substantial" open assumption.
- **p. 196, Prop. E.31(iv).** The residual is −½C_Aχ²(Re p_opp)X, and p_opp = ½ in the strict approximation.
- **p. 204, Ex. E.38, (E.36).** M^(2) = ½(−iχ)²[X² + p_opp·½C_AX]. "Re p_opp = 0 cannot be decided within the Glauber window alone."
- **pp. 217–218, Lemma E.48(d) and (E.51).** The model is the eikonal-spectator model of Lemma 9.2, in which "the sum of the minus components of the two insertions is fixed to zero by the on-shell condition, the plus components likewise". That is exactly the infinite-line elastic kinematics K^± = 0. All four ordering pairs get weight w = ¼.
- **Rem. E.32 (pp. 197–198) and Rem. E.49(2) (p. 218).** "Within G0 the O(χ²) residual should not be expected to vanish." Rem. E.49 also notes that "in the exact graphs the s-channel anti-Hermitian part comes only from the non-crossed graph".

### 2.2 The arithmetic of (E.51); R4's "−1/8"

From the p. 217 image: A_2 = ½(−iχ)²(X² + ¼C_AX) and (1+A_1+A_2)†(1+A_1+A_2) = 1 − ¼C_Aχ²X + O(χ³). Expanding:

A_2 + A_2† + A_1†A_1 = −χ²X² − ¼C_Aχ²X + χ²X² = −¼C_Aχ²X.

This equals −½C_Aχ²(Re p_opp)X at p_opp = ½, so the reference is self-consistent.

`refdoc/work_R4/checks_R4.py`, lines 43–48, computes something else: the amplitude-level deviation (iχ)²/4·(X+L) − (iχ)²/2·c² = −⅛C_Aχ²X. That is not the V†V residual. R4 also attaches "−¼" to the assignment "crossed graph carries the full weight", but that assignment (p_opp = 1) gives −½C_Aχ²X for V†V. So R4's "−1/8" is a slip: a different quantity. My script checks both statements.

### 2.3 Exact box and crossed box: three independent routes

**Setting.** Two infinite time-like lines with v_A·v_B = cosh Y. The gluon mass is m and K_∥ = 0. At fixed transverse momenta, a = k_T² + m² and b = (K−k)_T² + m². In the project normalisation,

J_σ = ∫dx_A dx_B [i/(x_A+i0)][i/(σx_B+i0)] g, with g = 1/((Q−a+i0)(Q−b+i0)),

where x_A = v_A·k, x_B = v_B·k, Q = k_∥², σ = −1 for the box (same ordering on both lines) and σ = +1 for the crossed graph.

The routing:
- Gluon 1 carries k from B to A.
- Line A absorbs gluon 1 first, giving i/(v_A·k + i0).
- Line B emits gluon 1 first in the box, giving i/(−v_B·k + i0). It emits gluon 2 first in the crossed graph, giving i/(v_B·k + i0), because v_B·K = 0.
- Path ordering puts the later attachment on the left, so c_box = Σ(T_A^bT_A^a)(T_B^bT_B^a) = X² and c_cross = X² + (C_A/2)X.

**Route 1 (new; no residues, no principal values): the proper-time representation.** Use

i/(x+i0) = ∫₀^∞dτ e^{iτ(x+i0)} and 1/(Q−a+i0) = −i∫₀^∞ds e^{is(Q−a+i0)}.

The k_∥ integral is a 2D Minkowski Fresnel integral, (π/S)·exp(−iu²/4S), with u = τ_Av_A + στ_Bv_B and S = s_1+s_2. Rescaling τ = 2√S·t removes S completely. Hence

J_σ = (4π sinh Y/(ab))·T_σ, with T_σ = (−i/2)∫₀^{π/2}dφ / (1 + σ cosh Y sin2φ − i0).

This shows that J_σ is *exactly* proportional to 1/(ab), so p_opp does not depend on k_T.
- Crossed graph: ∫₀^{π/2}dφ/(1+cosh Y sin2φ) = Y/sinh Y, so T_+ = −iY/(2 sinh Y).
- Box: the principal value is −Y/sinh Y. The δ-term, π/sinh Y, sits where sin2φ = 1/cosh Y, that is, where τ_Av_A − τ_Bv_B is light-like. So T_− = (π+iY)/(2 sinh Y).

Therefore **J_box = (2π/(ab))(π + iY)** and **J_cross = −2πiY/(ab)**.

Numerical checks of Route 1:
- Polar form with a Gaussian damping δ → 0: relative deviation below 1e−6 at δ = 1e−8, for Y = 0.3, 1, 2.7 and 6.
- Plain 2D Simpson with damping, then Richardson extrapolation (no polar coordinates): relative deviation about 2e−5.
- J itself at four parameter sets: relative deviation below 1e−8.

**Route 2: brute force.** I integrated the momentum-space integrand at finite ε on a uniform (x_A, x_B) grid, using the trapezoidal rule with h = ε/3 (spectrally accurate here), for ε = 0.08, 0.04 and 0.02, and then extrapolated in ε by Richardson.

| (a, b, Y) | rel. deviation, box | rel. deviation, crossed | extrapolated Re J_cross | |J_cross| |
|---|---|---|---|---|
| (1, 2.5, 1) | 6.7e−4 | 4.5e−4 | −1.5e−6 | ≈ 2.5 |
| (3, 1.2, 2) | 2.9e−4 | 6.4e−4 | −2.2e−3 | ≈ 3.5 |

**Route 3: the strict window.** Set g → 1/(ab) and use independent symmetric cut-offs. The analytic window integral gives ∫_{−L}^{L}i/(x+i0)dx = π, so J_box = J_cross = π²/(ab) and p_opp = ½. This is the reference's (E.51) case.

**Colour.** c_box = X² and c_cross = X² + (C_A/2)X hold for SU(2), SU(3) and SU(4), for all nine pairs of F, F̄ and A, with generators I built myself. The identity Σ{T,T}{T′,T′} = 4X² + C_AX used in the reference's proof of (E.51) also holds.

**Normalisation.** J_box + J_cross = 2π²/(ab). This is the abelian eikonal identity, a δ(v_B·k) from summing the B-orderings times ½·2πδ(v_A·k). It fixes M^(2) = −½χ⊗χ·(c_box J_box + c_cross J_cross)/(2π²/ab).

### 2.4 Consequences

- p_opp = J_cross/(J_box + J_cross) = −iY/π, so Re p_opp = 0.
- In b space, V = 1 − iχX − ½χ²X² + i(C_A Y/4π)χ²X + O(χ³). The C_A term is anti-Hermitian, so V†V = 1 + O(χ³) (checked numerically to 1e−16).
- **Reggeization.** The C_A term equals M_tree·ω(t)·Y, with ω = −(g²C_A/4π)(K²+m²)·coth Y·∫d²k/((2π)²ab). For Y → ∞ and m → 0 this is the Lipatov one-loop gluon trajectory −(g²N_c/4π)K²I(K), and it is negative, as it should be. It is a correction to the Hermitian eikonal phase, not a unitarity defect.
- **No real emission at O(g⁴).**
  - One real gluon emitted from a straight infinite time-like line is ∝ δ(v·q), which vanishes on shell.
  - Two real gluons from one line would need v·(q_1+q_2) = 0, which is impossible.
  - So the first non-zero real amplitudes are O(g³), and real cuts enter at O(g⁶).
  - At O(g⁴), unitarity therefore closes among virtual graphs. Meggiolaro computed the remaining O(g⁴) graphs (his (3.28)–(3.34)): the three-gluon graphs vanish, and the vertex and self-energy graphs give a real multiple of the tree. Both are anti-Hermitian in V. So the complete O(g⁴) eikonal amplitude is unitary.

### 2.5 Literature: the computation is known

- **Meggiolaro 1997, eq. (3.26)** (two infinite time-like Wilson lines at hyperbolic angle χ, gluon mass λ, Feynman gauge): the ladder plus cross graphs give M^(G1) = i(N_c g⁴/4π)·I(t)·χ·coth²χ and M^(G2) = −½g⁴·I(t)·coth²χ, where G1 = X and G2 = X². That is exactly p_opp = −iχ/π, and Re[G1 coefficient] = 0.
- **Meggiolaro 1997, eq. (3.36)**: (2s/t)[1 − ᾱ(t)ln s] with ᾱ = (N_cg²/4π)q²I > 0. This is reggeization.
- **Giordano–Meggiolaro 2006, eq. (4.24)**: M^(b) = i(g⁴/2π)I(iπ−|χ|)coth²χ and M^(c) = i(g⁴/2π)I|χ|coth²χ. Their ratio is identical to J_cross/J_box.
- **Rothstein–Stewart 2016, §9.** "All diagrams with crossed Glauber rungs vanish with our rapidity regulator." Eq. (9.1) is the Hermitian colour phase φ(b⊥). Eqs. (9.18)–(9.19) give Σ(boxes) = e^{iφ} − 1. Their regulator realises p_opp = 0, which is also unitary. Their §7.2 obtains reggeization from rapidity renormalization. The attribution of (9.1), (9.18), (9.19) in the claim is correct.
- **Caron-Huot 2013** treats reggeization in the eikonal approach; it is correct as context.
- What is our own is only the observation that the reference's strict-window residual is a truncation artefact. The reference is not citable, so this is not a priority claim.

### 2.6 Assessment

The *arithmetic* of (E.51) is correct for its regularization, p_opp = ½.

Within the reference's own eikonal-spectator model, the following reference statements are **false**:
- the residual "does not cancel within these graphs" (p. 58, Fig. 36);
- it "can only be expected to cancel" together with Glauber–soft mixing and real emission (pp. 57, 61, 85);
- "within G0 the O(χ²) residual should not be expected to vanish" (Rem. E.32, E.49(2)).

The same graphs with exact propagators already cancel. The missing piece is exactly what the reference itself names: the principal-value parts near 2k⁺k⁻ = k_T².

Scope of the correction:
- It does not settle E.33(c) for non-eikonal (composite) spectators or for active partons, nor E.34 or E.44. So it does not by itself upgrade DY.
- "Basis of the B′ grade" is a fair description of the residual's role: on p. 61 it is the concrete evidence for reason (a). But the printed text must not suggest an upgrade.

**Verdict: confirmed**, with the precise statement given in the structured output.

---

## 3. R-S2: TMD-breaking colour bookkeeping (p. 74)

**What the reference says.** The reference writes the eikonal coupling as Σ_j T_j n_j^μ/(n_j·k + iη_j0), whose Glauber part is −iπΣ_j η_jT_j n_j^μ δ(n_j·k). Here η_j = ±1 for initial and final partons, and it uses the in = out conservation law T_a + T_b = T_c + T_d. It then claims that η_bT_b + η_cT_c + η_dT_d "cannot be reduced to an operator on a because η_b ≠ η_{c,d}".

**It does reduce.** With η_c = η_d = −η_b,

η_b(T_b − T_c − T_d) = η_b(T_b − T_a − T_b) = −η_bT_a.

The same bookkeeping gives the same sign in both processes:
- SIDIS: η_cT_c = −η_bT_a;
- DY: η_bT_b = −η_bT_a.

So it predicts no Sivers flip, contradicting the established flip.

**Correct derivation.** Take k flowing into line j.
- Incoming line: i/((p+k)² + i0) ≈ i/(2p·k + i0), giving +T_j/(n·k + i0).
- Outgoing line: 1/((p−k)² + i0) ≈ −1/(2p·k − i0), giving −T_j/(n·k − i0).

Both δ-parts equal −iπδ·T_j: the same sign in the in = out convention. The pole part (coefficient of +iπδ) is therefore

P = −(T_b + T_c + T_d) = −(T_a + 2T_b).

In all-outgoing charges (Σ_jT′_j = 0; initial lines 1/(n·k + i0), final lines 1/(n·k − i0)) this reads T′_b − T_c − T_d = T′_a + 2T′_b. It is irreducible. As coefficients of −iπδ, SIDIS gives +T_a and DY gives −T_a: the sign flip.

**Collins–Qiu.** Their eqs. (4.1) and (4.2) give the same sign, +ig_2πδ^μ_−δ(l⁺), for a final-state line and an initial-state line of equal charge. Eq. (4.3) gives ig_1π…, for a total iπ(g_1 + 2g_2)δ(l⁺). The reference's bookkeeping would give g_2 − g_1 − g_2 = −g_1.

**Checks** (`v2_rs2_colour.py`, explicit 4-leg colour tensors for SU(2), SU(3) and SU(4); 19/19):
- in = out conservation;
- reducibility of the reference's combination;
- irreducibility of T_a + 2T_b: ‖G − kT_a‖/‖G‖ ≥ 0.94 at the best k;
- the all-outgoing identity;
- SIDIS/DY flip under the correct bookkeeping and no flip under the reference's;
- C_G(qq′→qq′, tt*) = 1 + 2⟨T_a·T_b⟩/C_F = (N²−5)/(N²−1) = ½ for SU(3), the same whether computed directly or from P = −T_a − 2T_b;
- the abelian Collins–Qiu total.

This matches the monograph's `prop:break-colour`. **Verdict: confirmed.**

---

## 4. R-S3: Ass. E.33(c1) (p. 198)

**What the reference says.**
- **pp. 195–196:** two non-commuting insertions on one spectator "can only be localized jointly; the result is a weighted sum of the two orders, with weights w_12 + w_21 = 1 depending on the two external factors". For single poles z_j = k_Tj²/(2k_j⁺) in the same half-plane, w_12 = z_1/(z_1+z_2). For N insertions, order π has weight ∏z_j / ∏_m Σ_{l≥m}z_{π(l)}. The reference adds: "we have not proven the general form of joint localization".
- **p. 198, (c1):** "there exists a **fixed** localization order such that per-graph weak equivalence (E.35) holds".
- **(E.35), p. 200:** ∫_V(T_cF_Γ − r_RT_cF_Γ) = O(λ^aL^K) for all V ∈ B. Here r_R applies the l_u "in a fixed order", and **p. 199** says its legitimacy *is* (c1).

**Re-derivation** (sympy, `v2_rs3_weights.py`). Integrating ∏θ(τ_j)e^{−iz_jτ_j} over the ordering regions gives:
- w(τ_2 > τ_1), the weight of O_2O_1, = z_1/(z_1+z_2);
- for N = 3, the order τ_1 < τ_2 < τ_3 has weight z_1z_2/((z_1+z_2+z_3)(z_2+z_3)) = ∏z/∏Σ_{l≥m}z_{π(l)}, i.e. sequential energy denominators;
- Σ_π weights = 1 for N = 2, 3 and 4;
- for opposite half-planes (k_1⁺k_2⁺ < 0) the supports are τ_1 > 0 > τ_2, so the weights are 0 and 1.

A brute-force 2D time integral with su(3) matrices O_1 = t¹ and O_2 = t² reproduces w_12O_2O_1 + w_21O_1O_2 to 1e−7. The fixed-order error is exactly w_21[O_1,O_2], with relative size 2|w_21| (0.85, 0.61 and 1.00 in the three test cases). As k_1⁺/k_2⁺ varies, w_12 = k_2⁺k_T1²/(k_1⁺k_T2² + k_2⁺k_T1²) sweeps all of (0,1), so no single fixed order matches on every V. In the two-SS-line configuration the commutator term has colour (C_A/2)X ≠ 0. The project script R8 K12 and K12b agree.

**Conclusion.** (c1) contradicts the reference's own pp. 195–196 analysis for the very G0 graphs it covers, so it is generically false per graph. The replacement is a lemma with ordering weights, together with the note that the weights are non-analytic at k_j⁺ = 0. The weight formula itself is elementary: ordered integrals of exponentials. **Verdict: confirmed.**

---

## 5. R-S4: super-leading configurations (pp. 19, 22)

**Power counting.** With c_J = 2 (DIS forward amplitude), (3.8) p_J = n_F + n_T + 2n_− − c_J gives:
- (n_F, n_T) = (0, 0): p_J = −2;
- (0, 1): p_J = −1.

So two statements in the reference are false as power-counting statements:
- Cor. 3.8: "other combinations are suppressed by at least λ¹";
- Thm 3.12's proof: "p(R) = Σp_J + p_S ≥ 0".

**How the reference handles them.** The proof of Cor. 3.8 dismisses (0,0) in one sentence: colour singlet plus angular momentum, and "longitudinal gluons decouple from H by the Ward identity". So "omitted" is literally too strong for (0,0); it is dismissed without the remainder analysis. (0,1) is never mentioned.

**(0,1) is not removed by symmetry.** For an unpolarized target, J^{j+…} ∝ k_T^j, and H depends on k_T at relative order λ. This gives λ^{−1}·λ = λ⁰, a leading remainder.

**Cancellation and remainder.** In Feynman gauge, the K part ∝ k^μ drops out by the Ward identity (k·H = 0 for a single gluon whose other legs are physical). The G part ∝ k⁺A^j − k^jA⁺, the abelian part of F^{+j}, is leading.

**Literature.** CSS 1989 §8.6 says: "in Feynman gauge the computation holds in general only when gauge invariant sets of diagrams are combined…; individual diagrams may be much more divergent… and may even grow with energy". CSS §8.1 shows that the potentials of fast charges are total derivatives and that forces go with field strengths. So the attribution is correct, and [A] is the right grade. **Verdict: confirmed**, with the wording "dismissed without remainder analysis" for (0,0).

---

## 6. R-M1: "no Euclidean pinch" (p. 15, Cor. 3.4)

**The reference's proof.** The proof of Cor. 3.4 dismisses zero-momentum lines by requiring "all lines at its two ends on shell". (3.2) imposes no such requirement. One massless line with l_j = 0 and α_j > 0, with all other α = 0, satisfies α_jD_j = 0 and Σα_jε_{aj}l_j = 0 for *any* p.

**α space for (3.3).** Here F = m²α_0(α_1+α_2) + Q²α_1α_2. Every simplex corner satisfies F = 0 and α_i∂_iF = 0 for arbitrary m² and Q², time-like Q² included. For m², Q² > 0 the corners are the only solutions: a sample of 2e5 points found the zero set only at the corners.

**Literature.** Collins 2020, App. D.1, says explicitly: "There is a pinch in the momentum integral for all p… The property of having a pinch on a massless line… when the line's momentum is zero evidently applies to all graphs with massless lines."

**IR degree.**

ω = 4L_S − 2N_g − N_q + V_3 = A_g + (3/2)A_q = A + ½A_q ≥ 2.

I checked this identity by line-end counting over 2000 random soft subgraphs. For the scalar (3.3), ω = 2, and the corner contributions scale like δ: 0.930, 0.0992 and 0.00999 for δ = 1e−2, 1e−3 and 1e−4.

So the integral is analytic in the Euclidean non-exceptional region (Lowenstein–Zimmermann, CMP 44 (1975) 73: IR convergence conditions for massless propagators). It is the *statement* "no pinch" that is false. With massive lines there is no solution. **Verdict: confirmed.**

---

## 7. R-M2: Prop. 3.5 (pp. 16–17)

**Not Euclidean.** For real Euclidean vectors, |p_1+p_2| ≤ 2m, so Q² ≤ 4m². A real Minkowski configuration exists for every Q > 2m (Breit-like; checked). So the reference's "欧氏运动学 (q² < 0)" is the spacelike-invariant region, not a Euclidean configuration. This matters because the collinear regions exist only because of the Minkowski signature.

**What Prop. 3.5 leaves open.** (3.6) states only ln² + O(ln⁰). Its proof says the single poles "can only contribute single logs", and gives no constant. The reference's own App. D, (D.32) on p. 156, supplies π²/3 ("gives the constant term undetermined there").

**Exact result.** Q²I = Φ^(1)(t,t) (Usyukina–Davydychev, PLB 298 (1993) 363). I checked this against direct Feynman-parameter integration (14 digits at t = 0.1, 0.01 and 0.001) and against the App. D representation. The sympy series is:

| order | coefficient |
|---|---|
| t⁰ | L² + π²/3 |
| t¹ | 2L² − 4L − 4 + 2π²/3 |
| t² | 6L² − 14L − 11 + 2π² (for information) |

The numerical residual matches the t² term (3.889e−6 against 3.8878e−6 at t = 1e−4).

**Regions in dimensional regularization**, (D.30)–(D.31): the 1/ε² and 1/ε poles cancel and the finite part is L² + π²/3.

**Table 5 is reproduced.** At t = 1e−10, the −4L form gives 9.7086e−8, which matches the table's 9.71e−8; the +4L form gives 1.155e−7. So the binding form has L = ln(Q²/m²) and −4L.

**Grade.** The regions statement is [P] (verified at one loop). The expansion itself is exact. **Verdict: confirmed.**

---

## 8. R-M3: parameter-space vs momentum-space theorems (pp. 14–15)

**What the reference does.** Thm 3.1 is stated as a necessary condition for singularities in external p. Its proof (App. A) works in Feynman parameters: stationary point in k, deformation η_j = α_j∂_jF. The same text then declares that "points satisfying (3.2) form the pinch surfaces", and §3 uses them as momentum-space trapping surfaces for reduced diagrams. §3.1 says "endpoints do not occur… infinity is a UV problem", and App. A Rem. A.1(a) files U = 0, the second-type singularities, under UV and renormalization.

**What Collins 2020 shows.**
- Thm 1: trapped ⇔ a Landau point exists for the first derivatives of the vanishing denominators. It covers quadratic denominators including Wilson lines.
- Thm 2: not trapped ⇔ there is a v with v·∂A_j > 0.
- Thm 3: the geometric theorem.
- App. D.1: the massless self-energy has a momentum-space collinear pinch at p² = 0 but no pinch in the pure parameter representation, "contrary to what is assumed as obvious in the standard literature".

Second-type singularities (pinch at infinity, U = 0) are not UV divergences. So the two theorems need separate statements and proofs. **Verdict: confirmed.**

---

## 9. R-M4: Wilson-line rules (p. 11, Fig. 4)

**What (2.7) defines.** W^{(±)}(x) = P exp(−ig∫₀^{±∞}dλ v·A(x+λv)), with far points on the right. That is W^{(+)}(x) = W[x, x+∞v] = W[x+∞v, x]† and W^{(−)}(x) = W[x, x−∞v].

**Single-gluon rules derived from (2.7)** (`v2_rm4_wilson.py`):

| line | k flowing in | k flowing out |
|---|---|---|
| future | igv^μt^a × i/(v·k − i0) | −i/(v·k + i0) |
| past | igv^μt^a × i/(v·k + i0) | −i/(v·k − i0) |

Fig. 4 says "i/(v·k ± i0), + future / − past" with vertex igvt. It states no routing, does not separate W from W†, and gives no multi-gluon partial sums. Neither routing convention reproduces both of its ± rows. Its own last row, −g p^μ/(p·k + i0) = igp t × i/(p·k + i0) for an incoming quark absorbing k, puts +i0 on a past-type line, the opposite of row 1.

**Correct rules.** The iterated ordered integrals, done symbolically for m = 1, 2, 3 and checked by brute-force quadrature, give, for k_j flowing into the line and numbered along the path orientation:
- past W[0,−∞n]: ∏_{j=1}^m i/(n·(k_1+…+k_j)+i0);
- future W[∞n,0]: ∏_{j=1}^m (−i)/(n·(k_j+…+k_m)−i0);
- vertex igt^an^μ, with colour matrices path-ordered (later on the left).

Equivalently: i/(n·ℓ+i0), with ℓ the momentum along the path orientation. The project script c_wilson s1 gives 48/48. **Verdict: confirmed.**

---

## 10. R-M5: the i0 of the K projection (pp. 23–25)

**What the reference does.**
- (3.10): K^μ_ν = k̂^μn̄_ν/(n̄·k), with no i0.
- (3.11), the soft K: n^μk^ν/(n·k ± i0).
- Thm 3.14, step 3, gets +i0 only from U being based at −∞ in (3.14).
- Rem. 3.15 admits that this base point is arbitrary.

**Physics.** Take k flowing into H.
- DIS: after the Ward identity the K gluon ends on the outgoing struck quark: 1/((p−k)²+i0) ≈ −1/(2p·k − i0), so −i0 (future).
- DY: it ends on the incoming parton from B: 1/((p+k)²+i0) ≈ 1/(2p·k + i0), so +i0 (past).

The project script c_wilson s6 confirms the pole sides for both.

**Collins.** The errata (22 May 2026), p. 402 item, read: K_{μ_jν_j} = k_{jμ_j}w_{2ν_j}/(k_j·w_2 − i0), with "k_j the momentum of gluon j flowing into H" and w_2 = (0,1,0_T). The erratum itself only swaps upper and lower indices; the −i0 is already in the printed (11.6).

For collinear PDFs the choice is immaterial after the k⁺ integral, but it matters for TMDs and for the Glauber analysis. For DY the direction is fixed only after the contour deformation. **Verdict: confirmed.**

---

## 11. R-M6: the scope of Thm 3.14 (pp. 23–25)

**What the reference claims and proves.** The statement covers a general H with n longitudinal gluons and a collinear quark pair. The proof's step 2 says the identification "can be verified term by term by the telescoping sum (3.15)" only "for H containing only quark lines and colour-singlet vertices". For H with internal gluons it needs Slavnov–Taylor identities with ghosts, and that step is "cited, not repeated". Rem. 3.16 says the same, and App. D even keeps the Ward identity for modified integrands as Ass. D.37. Gluon-initiated H is outside the statement.

**Grades.**
- The tree and abelian identity is exact: c_wilson s4 gives 97/97, including two off-shell longitudinal gluons with the f^{abc} remainder. Grade [R].
- The all-order non-abelian statement rests on standard but sketched graph-by-graph arguments (CSS 1989 §9; Collins 2011 ch. 11). Grade [A] under the CONTEXT definitions.

**Verdict: confirmed.**

---

## 12. R-M7: the soft factor (p. 26)

**The problem.** (3.16) is literally S = (1/N_c)⟨0|Tr W_n̄†W_n ⋯ W_n†W_n̄|0⟩. It gives no positions, no T/T̄ ordering, no sum over soft final states, and no future/past. Cor. 3.17 claims an "identical proof", although the base point of the soft lines (the hard vertex) is physical.

**The precise forms already in the reference.**
- (8.2), p. 52: S(k_tot) = Σ_{X_s}⟨0|T[∏W^{(+)}]†|X_s⟩⟨X_s|T[∏W^{(+)}]|0⟩δ⁴(k_tot − p_{X_s}), future-pointing because of the pole positions of Lemma 8.2.
- (E.48), p. 214: past-pointing, U^{(−)} = W_n^{(−)}(0)W_n̄^{(−)}(0).

**Physics.** The i0 is inherited from the replaced jet propagators: future for final-state jets (e⁺e⁻, SIDIS), past for DY. Aybat–Rogers 2011 state the future (SIDIS) to past (DY) flip. Inclusive DIS has no soft factor at leading power (Thm 3.12(a)). **Verdict: confirmed.**
