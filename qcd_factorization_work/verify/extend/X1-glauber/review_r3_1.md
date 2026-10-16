# X1 (Glauber cancellation in inclusive Drell–Yan) — adversarial review, round 3, reviewer #1

Date 2026-10-11. Agent: X1-glauber-rev3-1 (a6c2ca192a1982f9b; journal line 126).

## 0. Input, process and run status

* **Run status (relayed question 「在正常运行吗」): the workflow is running, but not fully normally.**
  - Progress in the journal (`~/.claude/projects/-Users-hao-cheng-Desktop-theorem-proof/c211c739-758d-4b40-bbac-67f4e1a65da4/subagents/workflows/wf_52f29317-58b/journal.jsonl`, 133 lines at 06:11):
    - X1: round-3 review. rev3-2 finished (line 132); this is rev3-1.
    - X2: both round-3 reviews have finished (lines 131 and 133).
    - X3: fix 2 finished (line 128); round-3 review is running (lines 129–130).
  - The persistence fault is still there:
    - `verify/extend/X1-glauber/REPORT.md` does not exist. Neither do `review_r1_1.md`, `review_r1_2.md` and `review_r2_2.md`, nor any REPORT.md for X2 or X3.
    - `review_r2_1.md` is the only review file on disk. Fix 2 again returned its report only as a structured result.
  - rev3-2 reports that the script stops after round 3. If so, the fixes below can only be applied by the parent session when it patches the spec.
* **What I reviewed.** The current report is the structured result of **X1-glauber-fix2** (agent aff8996e9d3974c62), journal **line 125**: summary, results[0]–[26] (DEFS … REVISIONS) and open[0]–[11] (O1–O12). I read all of it. A readable extraction is in my scratchpad (`…/scratchpad/j/line125.txt`).
  - I also read both round-2 reviews (line 117 = `review_r2_1.md`, and line 111). Every round-2 item is addressed at least nominally.
  - I read the parallel review rev3-2 (line 132) only after my own checks were finished. Three points in it that I had not raised (P5, the δ_Y condition in T2, Zhou et al.'s second direction) I re-derived or re-read myself before including them. Agreement is marked "(= rev3-2)".
* **My scripts and logs.** Scripts are in `verify/extend/X1-glauber/review_r3_1_scripts/` (`genjet.py`, `l8_general.py`, `t2_general.py`, `t3e_p2_checks.py`). Logs are in `review_r3_1_logs/`. Downloaded papers are in my scratchpad only.

## 1. Verdict

**Fixable issues. The mathematics is sound; one physical claim is overstated.**

* **Mathematics: correct under the stated hypotheses.** This covers L1 (as corrected), L1′, L2, L3, L4, L5 (proof now complete), L6, L8 (new), T2, T2′(a)(b), P2, T3(a)–(c),(e) and P4(a),(c).
* **Independent confirmations new in this round:**
  - L8 holds on **general, non-factorized** (Sp′)-class jets. All earlier checks used factorized jets.
  - T2's conclusion holds **end to end** for non-factorized jets, including a J_A that violates (Sp′). T2 requires only (Sp) of J_A.
  - The T3(e) weight bounds, c_U, the P2(b) examples and the P4(b) shift formula are reproduced from scratch.
* **What remains.** None of it needs new mathematics except item (1), which needs a short power-counting lemma or a scope restriction.
  1. **(Substantive, scope.) Real-emission cuts of the direct SS lines are omitted.**
     - T2, T2′(c) and T3 treat only SS lines lying wholly on one side of the final-state cut.
     - But G₀ explicitly contains *cut* direct lines (reference Def. E.1(e): 「可以被割」), and E.33(c2) explicitly includes real emission (「含实发射」).
     - So the PHYSICAL READING ("the G₀-restricted form of E.33(c2) HOLDS"), ERRATA ERR-S1b(ii) and the REG "not needed" list claim more than is shown.
     - By power counting, these cuts are *not* suppressed in the unregulated H_glob model. With the two-sided G7 regulators they are.
  2. P4(b): the sentence "(Sp′) (no single-state gap) unchanged" is **false**. The conclusion survives once an (Sp′) partner term is added; I verified this numerically.
  3. P5: the identity D_C = ∫dΦ₃ (A^lines)†A^lines is **wrong**. Class C yields only the A/B interference term (= rev3-2, verified independently). The conclusion D_C ≠ 0 survives.
  4. T2: three precision gaps.
     - The smallness condition δ_Y ≤ ½ is used but not implied by ε ≤ ε₀ (= rev3-2).
     - The constant C_c is not explicit and depends on ln(λ_B/μ_B).
     - The rate of the Im p_opp expansion is not derived.
  5. T3(e): the second term of the proved bound has a wrong logarithm. It is not boost invariant. Separately, the interpretive sentence says more than the bound.
  6. REG misreads register rule 00.1-1 (= rev3-2). There are also smaller precision points in P1, P2, T2′(b), CMP, LIT and the L8 constants.

## 2. Independent checks performed in this round

| # | claim | method (script → log) | result |
|---|---|---|---|
| R1 | L8(b)–(f) for **general** (Sp′)+(Sp)+(R)+NF jets | `genjet.py` builds the jets from 1–3 hexagon orbits, 0–2 **winding cycles** (twelve terms twice round the hexagon with different energies on the two turns; neither factorized nor a sum of orbits), 0–6 two-chains with multi-state shared gaps, and isolated multi–multi terms; (Sp′) and (R) are checked structurally. Script `l8_general.py` → `l8_general.log` | θ=π/2, 117 jets × 300 points: max lhs/bound **(b) 0.52, (c) 0.025, (d) 0.044, (e) 0.42**. θ=π/4 with constants ×8: 0.46, 0.008, 0.012, 0.09. g^[12]=g^[21] to 3·10⁻¹². ∫g dU/2π ÷ (−iJcal) = 1 to 10⁻⁷ and ∫S ÷ (−Jcal) = 1 to 8·10⁻⁴ (4 jets). **Counter-test:** changing one FF energy breaks (Sp′); then \|S\|κ₂/Mflat = 0.50 in the strip, i.e. the 1/κ₂ tails no longer cancel. (Sp′) is necessary for L8(d),(f) as stated |
| R2 | validation of my T2 integrator (own strip variables U = μ_B sinh s, log-log diagonal quadrants) | `t2_general.py val` → `t2_general.log` | scalar base set, Re p_opp = **0.0123468** (λ=0.01; reference 0.0123471), **0.0020501** (λ=0.003; ref. 0.0020476), **0.0003476** (λ=0.001; ref. 0.0003448). The ∫S_B check gives 0.999996 |
| R3 | **T2 end to end for non-factorized jets** | `t2_general.py gen`; J_B general (Sp′), J_A general (Sp); in pair 2 J_A **violates (Sp′)**; ε scanned by scaling the A energies (c_t → c_t s^{d_t}, so M is invariant) | Re p_opp = 0.0318 / 0.0066 / 0.0011 (pair 0); 0.0670 / 0.0148 / 0.0026 (pair 1); 0.0891 / 0.0246 / 0.0049 (pair 2), at ε ≈ 9·10⁻³ / 9·10⁻⁴ / 9·10⁻⁵, i.e. ∝ ε^{0.7–0.77}. N/N₀ → 1 (\|1−N/N₀\| ≤ 4·10⁻⁴ at the smallest ε). Im p_opp falls by 0.717–0.730 per decade of ε, against (1/π)ln 10 = 0.733. Quadrature error at the smallest ε ≤ 1.5·10⁻⁴ (n = 1200 vs 1600) |
| R4 | P4(b) and the missing (Sp′) partner | `t2_general.py p4` | `check_spprime`: **False** without the partner, True with the 12V partner. Prediction δW(12,21) = −(is/2π)∫ρ2 dk/k = **+0.007838i** (ρ2 has a fixed sign, verified). Numerics without the partner: 0.000121+0.007860i (λ=0.01), 0.000022+0.007848i (λ=0.003). With the partner: 0.000103+0.007790i, 0.000020+0.007832i. The partner's effect falls from −7·10⁻⁵ i to −1.6·10⁻⁵ i (power suppressed) |
| R5 | T3(e)(3),(e′) and c_U, derived from scratch (sympy L1′ pole weights in x_e = iK/z_e, race weights, four quadrants, π/4 rays) | `t3e_p2_checks.py` → `t3e_p2_checks.log` | linear term **(x₁−x₂)/4 exactly** in all quadrants. sup\|v_K\|/(\|x₁\|+\|x₂\|) = **0.25000** on \|x\| ≤ ¼; sup\|v_K\| = **0.50000**; remainder coefficient 0.0441; **c_U = 1.64853** |
| R6 | P2(b),(c) | same script; algebra | w^A_12 = **97/105** and **43/455** by exact residues. Sharp window δ = 0.1748495763. The three-sector eikonal identity Σ_{σ∈[12]}J_eik = 2πδ(k₁+k₂) i/(k₁+i0) is re-derived from the sector denominators. The sign of the δ_Aδ_B term depends on the B-side orientation (see P2) |
| R7 | L5, L6, L4(b)(c), T2 Steps 0–7 (E1–E8, the choice of K, the strip geometry), T2′(a) rate, T2′(b) residue, L1(b) telescoping, closed-quadrant lemma, P1(b) | by hand | correct except as noted in §3 |
| R8 | literature | INSPIRE API; arXiv PDFs via pdftotext | 21 bibliographic entries correct: all round-2 additions; Zhou et al. (two unlinked INSPIRE records, as stated); DFT, DGHS, ADDFT, LS. Content checks pass for CdFR eqs. (186)–(190), FSS, Becher et al., Aybat–Sterman eq. (10), Zhou et al. eqs. (4), (64)–(70) and (85)–(86), Chang–Li and Li 2022. Novelty searches: see LIT |
| R9 | reference text (`refdoc/refdoc.txt`) | grep/read | the three ERR-S1b quotations are verbatim (lines 11816, 11862, 13014). **Def. E.1(e)** (l. 9905–9910): G₀ soft lines 「可以被割」. **Def. E.30**: every SS line in the family lies on one side. **E.33(c2)**: window + near-shell soft region 「（含实发射）」; same in the Prop. E.31(iv) text (l. 11758–11760) |

## 3. Per-result verdicts

**DEFS — correct; minor points.**
* The class-X definition and its example are right. A hypothesis that is only listed in DEFS but used by several statements is a registered premise (see REG).
* "(Sp′) … exact in the scalar model" is right. I checked that the covariant scalar J^[12] equals the sum of the three LCOPT sector terms with c = i/d₀ (energies e₁ = d₁₀, e₁₂ = −β, e_V = α₀, e₁V = α₁).

**L1 [R] — correct as corrected.**
* The telescoping bound N2^{N+1}M_σ(λ_J/κ)∏\|K_l\|⁻¹ is right, including the multi-state step, which uses 2λ_J/κ ≤ 1.
* The closed-quadrant lemma is right: pairwise Re(z_i z̄_j) ≥ 0 gives \|Σz\|² ≥ \|z_m\|². Then Σ\|w\| ≤ n_F! n_B! ≤ N!.

**L1′ [R] — correct.** I re-derived the example weights by partial fractions. The sum rule holds, c_U = 1.6485 (R5), and the closed-quadrant placement holds for every θ ∈ [0, π/2]. The θ ≤ π/4 restriction is needed only to avoid the pole collision at π/2.

**L2, L3, L6 [R] — correct** (unchanged; L6 re-derived by Cauchy for [ρ − (1+k)⁻¹]/k).

**T1 — correct** as a re-derivation of Props E.35 and E.31(iii).

**P1 [R_cond] — correct, one notational defect.**
* x^A_min is defined as min l⁺, which is a *momentum*. "x^A_min ≥ c" must then read x^A_min ≥ cP_A⁺, or x must be defined as a momentum fraction.
* The proof of (b) is right: E(l) ≤ 2E⁽⁰⁾(l) + Δ_l²/l⁺ with l⁺ unchanged by E.19(a), and a state cuts each line of J_A⁰ at most once.

**L4 [R] — correct.**
* (b): with M⁽¹⁾_e = −ic_eX_e and c_e real, the coefficient of X₁X₂ is c₁c₂(1 − W₂₁ − W₁₂*) = 2ic₁c₂ Im W₁₂ (re-derived).
* (c): on the singlet of (i, j₁, j₂) the two terms are ∓(i/2)C_A T_{j1}·T_{j2} and cancel (re-derived).
* The CONTEXT sentence on CdFR is accurate. I read arXiv:1112.4405: for n = 4 the operator is ∝ f_abc T₁T₂T₃ (eq. 186) and Sp†fT₁T₂Sp = 0 (eqs. 187–190), so it contributes to P^(2,R) only for n ≥ 5. Precision: the *operator* does not vanish at n = 4; its contribution to the squared amplitude does.

**L5 [R] — correct; the proof is now complete.**
* I re-derived the radial identity d/dt[e^{2it}G(e^{it}κ)] = i div_κ(κe^{2it}G), with κ·n = 0 on the half-axes.
* At fixed η > 0, no gap factor vanishes for t ∈ [0, π/2]. Initial factors have real part ≤ A < 0 for x > 0 and imaginary part ≥ η for x < 0.
* \|A + i(η−y)\| ≥ ⟨y⟩/√5 for η ≤ μ, by the case split \|y\| ≤ 2μ versus \|y\| > 2μ.
* The arc decay rates are as stated or better.

**L8 [R] (new) — correct, and robust beyond the factorized class (R1).**
* I re-derived (a), the π/4 inequality \|A+K\| ≥ max(\|A\|,\|y\|)/√2, the eikonal sector sum −1/(p₁P) + 1/(p₁p₂) − 1/(Pp₂) = 0, the axis-band pairing via (Sp′), the strip structure f₁₂ = g/κ₂ + E₁₂ with g^[12] = g^[21], and (e)(f): the UHP residues of FF give ∫g dP = 2πJcal, and the counterclockwise rotation gives −iJcal.
* Minor (= rev3-2, re-derived): in the axis-band step of (c), the multi-state second-gap pieces add up to (16/9 + 1)·Mflat λ/(R²⟨r₁⟩), not 2·Mflat λ/(R²⟨r₁⟩). The final constant 9 still holds (total about 8).
* The counter-test in R1 shows (Sp′) cannot simply be dropped. O12 is correctly stated.

**T2 [R_cond] — mathematically correct as a statement about the uncut side sum. Its physical reading is overstated (F1), and it has three precision gaps.**
* Re-derived:
  - Step 0's normalisation −(1/Jcal_B)∫hf.
  - The partition S/T/O. T₊ lies in the quadrant (−,+), where only 1V2 contributes.
  - h = (a₁a₂/Jcal_A)·J_A^(σ)(−ia₁/2κ₁, −ia₂/2κ₂)/(4\|κ₁κ₂\|), checked against w^[12] = a₁κ₂/(a₁κ₂ + a₂κ₁).
  - The K-choice conditions ⇔ ε ≤ ε₀, and E1–E8 from L8(g): 24/π², 825/π², 1600/π², 43/π², 16/π², 4/π.
  - The v-term is purely imaginary, L6 gives −½ per mixed sector, and the Im p_opp logarithm is −(1/π)ln(1/ε).
* **R3 confirms the theorem's generality numerically.** For non-factorized jets Re p_opp → 0 (roughly ∝ ε^{0.7}), N/N₀ → 1, and the Im slope agrees. It holds even when J_A violates (Sp′), consistent with T2 requiring (Sp′) only of J_B.
* **Gaps.**
  - (i) The final step uses δ_Y ≤ ½. This is not implied by ε ≤ ε₀ (2E2 alone is ≈ 167·mflat_B ε^{1/2}(1+L_B)), so it must be added as a hypothesis (= rev3-2).
  - (ii) C_c in \|X\| ≤ \|Re X\| + L/π + C_c is not written. Bounding it with L8 (∫\|g\| ≲ Mflat(1 + ln(λ_B/μ_B)), and 12Mflat ln²(1 + 16λ_B/μ_B) for R ≤ 4λ_B) makes C_T depend on ln(λ_B/μ_B). Then C_T is not "a polynomial in m_A, mflat_A, mflat_B, c_ρ, a_max/a_min".
  - (iii) "Im p_opp = −(1/π)ln(1/ε) + c + O(ε^{1/2}…)" asserts the convergence rate of the O(1) remainders without derivation. Either derive it under an explicit scaling (fixed jet shapes) or weaken it to + O(1).
* **PHYSICAL READING — overstated (F1).** Details:
  - T2's side sum is L4(a)'s M⁽²⁾ + M⁽²⁾† + M⁽¹⁾†M⁽¹⁾. These are the side assignments of Def. E.30, in which **no SS line crosses the final-state cut**.
  - The reference's G₀ (Def. E.1(e)) contains direct soft lines that **may be cut**. E.33(c2) combines the window with the near-shell soft region **including real emission** (「含实发射」; also Prop. E.31(iv)'s text: 「完整图集 G 连同相邻的、连接线接近质壳的软区与实发射」).
  - Off the window, a direct SS gluon can be cut: a real gluon emitted by spectator i in the amplitude and by spectator j in the conjugate. T2, T2′(c) and T3 contain no such contribution.
  - **Power counting** (a careful estimate, not a computation). Cut g₁ (A amplitude ↔ B conjugate) and keep g₂ uncut on the amplitude side.
    - J_A then carries two amplitude-side insertions, so the A-side strip (k₁⁻ + k₂⁻ ~ λ_A, \|k_e⁻\| large) is available. There J_A^[π] ≈ g_A(P⁻)/k₂⁻, with no eikonal cancellation.
    - J_B carries one insertion on each side. After B's cut sum its factor is δ-like in each insertion energy (width λ_B, height ~1/λ_B; tails λ_B/p²).
    - The on-shell condition k₁⁺ = a₁/(2k₁⁻) then forces \|k₁⁻\| ≳ a/λ_B, i.e. the cut gluon is B-collinear.
    - With u = a/(2k₂⁻λ_B) the remaining integral is ∫(dk₂⁻/k₂⁻)(1/2k₂⁻)·J_B^conj(a/2k₂⁻) ≈ (1/a)∫Φ(u)du. The contribution is therefore **O(N₀), not power suppressed**. It sits at the B-collinear end, where E.19(b) fails, just as T2's −½ sits at the A-collinear end.
    - The mirror cut gives the same at the A end. Cuts that put both jets' insertions on opposite sides, or cut both gluons, are suppressed.
    - With the **two-sided G7 regulators** (K⁺ ≪ a/λ_A, K⁻ ≪ a/λ_B), the retained on-shell segment has k⁺ ≥ a/(2K⁻) ≫ λ_B and k⁻ ≥ a/(2K⁺) ≫ λ_A. Every cut configuration then contains a jet with single insertions per side far above its scale, which gives O(λ_BK⁻/a + λ_AK⁺/a): power suppressed.
  - Consequences:
    - (a) "T2 shows … the G₀-restricted form of E.33(c2) HOLDS" is **not established** for the unregulated H_glob model (its O(1) cut terms and their colour content are not computed).
    - (b) In the G7-regulated form the claim needs the cut-suppression estimate above, written as a lemma. Until then it must be stated for the **uncut** direct lines.
    - (c) ERR-S1b and REG need the same restriction.
  - Also (= rev3-2): Rem E.32 and Rem E.49(2) themselves attribute the ordering correlation, and part of the missing −¼C_Aχ²X, to the near-shell region of the direct lines. What T2 contradicts is the reference's expectation that this is *insufficient* within G₀ (E.33 status paragraph).
* NOVELTY: correct as restricted to Lindsay 1984 and BFT 1989.

**T2′ — (a) correct, (b) correct with one wording issue, (c) [P] consistent.**
* (a): ρ̃ = ρχ(k)χ(−k) is holomorphic in the first quadrant (χ(−k) continues into the third quadrant), real on k > 0, and suppresses the end-pole residues by O((K_cλ_A/a)²). K = (λ_BK_c)^{1/2} gives the stated rate.
* (b): Res(ρ₁₂)/k_p = −a₁α₁/(a₁α₁ + a₂\|d₁₀\|) is re-derived. But "jet B's poles give the same by symmetry" can only mean the mirror statement under NF_A (a k⁻ rotation), since L5 needs NF_B. Dropping NF on both jets is O2 (= rev3-2).
* (c): see F1. The real-part statement is about uncut lines.

**P2 [R] — correct; one convention to fix.**
* I reproduced (R6) the eikonal identity, the PV formula, the sharp-window δ, and 97/105 (also 43/455).
* The identity p_opp = ½ + 2δ_Aδ_B holds only if w^B₁₂ = ½ + iδ_B with the *same* orientation as on A. With the opposite orientation it is ½ − 2δ_Aδ_B. "δ_B is defined in the same way" leaves open whether χ′ is evaluated at k⁺ or at the B energy p = −k⁺. The definition must fix this.
* The qualitative conclusions (any real value; ½ iff δ_Aδ_B = 0) are unaffected.

**P3 — correct** (unchanged).

**T3 — (a)–(c) correct; (d),(f) [P] reproduced earlier; (e) correct in substance, with one wrong term.**
* (e)(3),(e′) and c_U are confirmed from scratch (R5).
* **Error in the stated bound:** the second term (λ_A/K)(1 + ln(1 + K/μ_B))² is not boost invariant. K is a k⁻ scale and μ_B a k⁺ scale.
  - The proof produces this term from ∫_{R ≤ a_min/(2K)}\|f_B\|, i.e. (λ_A/K)(1 + ln(1 + 2a_min/(Kμ_B)))².
  - The cut-off X = a_min/(2K) is a k⁺ scale. Replace K/μ_B by a_min/(Kμ_B).
* The interpretive sentence "not determined by the integrand on any window \|k⁻\| ≤ K" says more than the proven bound. The Lorentzian changes the in-window integrand by a relative O(k²/K²), not by zero. State the proposition only (= rev3-2).
* (g),(i): scope correct. F1 applies to T3 too: cuts through i–j_e lines are not included.

**P4 [R_cond] — (a),(c) correct; the result of (b) is correct, but one stated reason is false.**
* The added 1V2 term s c₂[i/(A₁+k₁)][i/(A₂+k₁)][i/(A′−k₂)] **has a single-state gap**: the final gap between V_H and insertion 2.
* (Sp′) for the adjacent pair (V_H, 2) therefore requires a partner in sector 12V, s c₂[i/(A₁+k₁)][i/(A₂+k₁)][i/(A″+k₁+k₂)]. Without it J_A leaves the (Sp′) class (R4: `check_spprime` = False).
* This is harmless for T2, which imposes (Sp′) on J_B only. But P4's CONSEQUENCE and REG-G2 speak of "the class (J),(Sp),(Sp′),(R)".
* Adding the partner restores (Sp′) and changes δW(12,21) only at power level. R4: −7·10⁻⁵ i at λ = 0.01 and −1.6·10⁻⁵ i at λ = 0.003, against δW ≈ +0.0078i.
* R4 also confirms the (b) shift formula independently (+0.007838i predicted, +0.00785i computed).

**P5 [A] — conclusion acceptable; the round-2 identity is wrong** (= rev3-2; independently checked).
* A three-particle cut of a class-C graph cuts a rung whose endpoints lie on **opposite sides** of the cut: line A on one side, line B on the other. So D_C = ∫dΦ₃[A_A†A_B + h.c.], where A_X is emission from line X. It is not ∫\|A_A + A_B\|²; the self terms lie outside C.
* "Sum of B†B terms" is therefore no reason for positivity. Positivity does hold in Feynman gauge for straight lines, because A_A = C·v_A/(v_A·k) and A_B = −C·v_B/(v_B·k) share the colour operator C, giving C†C·2v_A·v_B/((v_A·k)(v_B·k)) ≥ 0. Class C is not gauge invariant, so D_C is gauge dependent.
* D_C ≠ 0 survives. REG's "G5(ii) … (shown, P5)" should read "argued [A]".

**L7 [R] — correct as corrected.**

**Remark P6 — acceptable** as an ungraded remark.

**REG — mapping correct; two errors.**
* The asm labels exist in `spec_v2/ASSUMPTIONS.md` (appO-lcopt, appO-envelope, appO-mixing (a)–(c), appO-deformation (a)–(d), appO-rewritten-cs). appO-collinear-ends is correctly marked as proposed.
* (i) **Rule 00.1-1 misread** (= rev3-2). The rule registers exactly the unproven hypotheses that are R_cond premises **or are shared by several statements**. (Sp′) (L5/L8/T2/T3), (R) (T2/T3/P4), NF and (H_glob) are shared R_cond premises. Register them, or recast them along §6's precedents: (H_glob) as a model definition, NF as the domain definition, (J) and (Sp) as hypotheses of an LCOPT lemma.
* (ii) The "not needed, but only conditionally" entries for coincident O(g⁴) patterns must add "for uncut SS lines; cut SS lines (real emission) power suppressed under two-sided G7 by power counting (to be proved)" (F1).
* The G7 relocation statement is right. G2's register text (appO-envelope) must be rewritten for side-summed families. The report says this, but the register entry is per graph.
* WRITER_SPEC_v2 §4.3 requires exactly one qualifier per [R]. The L-lemmas and P2 are R_PT-type; T1, P1, T2, T3(a)–(c),(e) and P4(b) are R_cond.

**CMP — accurate on DGOPS and Aybat–Sterman; two precision points on Zhou et al.**
* Aybat–Sterman (verified): eq. (10) is the sector-sum identity and "holds for fixed color orderings"; the paper "outline[s] arguments".
* Zhou et al. (verified in arXiv:1708.01743v2):
  - The "should not be viewed as strict proofs" caveat qualifies their **graphical Sec. VI**. The abstract and Sec. V present the operator-level argument as proved ("It is proved …", "are proved to cancel out"). The report's non-acceptance is its own assessment of the single-evolution-parameter step and should be worded so.
  - Only the A⁺_G sector, which contains every SS exchange, is generated by U_{+G}. Glauber gluons A⁻_G are treated afterwards along a second direction n_f⁻ (eqs. 85–86). "All SS and spectator-soft exchanges … one unitary operator U_{+G}" is therefore imprecise for the spectator-soft part.

**TMD [C] — appropriate.**
* Chang–Li: the abstract attributes the large effect to the pion's role as "a Nambu–Goldstone boson and a qq̄ bound state".
* Li 2022: the abstract confirms k_T factorization and a single Glauber phase for NA10/E615/COMPASS.
* The assessment is fair.

**EX — accurate.** The fix-r2 logs contain the quoted numbers. One note: `t3e_sensitivity.py` (iv) prints hard-coded round-1 values; it does not recompute them. The "ALL PASS" there tests only c_v < 1, c_inf < 1 and lead_err < 5.

**LIT — bibliographic data correct (R8). One recent work is missing.**
* Novelty: my INSPIRE searches (title: Glauber since 2021; Glauber with Drell–Yan/spectator/cancellation/factorization; spectator with Drell–Yan; full text: "spectator-spectator" with Glauber) found no prior statement of T2 for general LCOPT jets, of T3's configuration, of P1, P2(b), P4 or L8. Sterman–Erdoğan (EPJ ST 235 (2026) 1493 = arXiv:2502.14230) is a coordinate-LCOPT review with no Glauber/DY content.
* **Add** Barcaro–Gao–Gaunt–Pathak, arXiv:2607.14259 (July 2026), "Collinear Factorization Violation and Reggeization": an all-order soft-collinear factorization in space-like collinear limits with a single Glauber-pinched gluon, exhibiting Reggeization. It is context for L4's CdFR remark and for T2's reggeization reading. It does not pre-empt anything.

**ERRATA ERR-S1b — valid in substance, but over-scoped.**
* The quotations are verbatim.
* Correction (ii) must say "for the uncut direct lines". The [R_cond] status covers only the uncut side sum (F1).
* It should also acknowledge that Rem E.32 and Rem E.49(2) already name the near-shell mechanism. The reference's error is its expectation that the mechanism is insufficient within G₀ (= rev3-2).
* The regulated (G7) G₀ statement additionally needs the cut-suppression estimate.

**REVISIONS — accurate.** Every round-2 item of both reviewers is addressed. The stated departures are justified. One exception: departure (b), "any real value", is right, but see the P2 orientation point.

**OPEN — honest.** Add O13: compute, or prove power suppressed under two-sided G7, the cut (real-emission) contributions of the direct SS lines for the fully and half-coincident patterns. Add to O1/O6 that the G7 matching at the collinear ends must also absorb these cuts.

## 4. Required fixes

* **F1 (scope; T2/T2′/T3 physical readings, ERR-S1b, REG).**
  - State that the side sums contain only SS lines lying wholly on one side of the cut (Def. E.30).
  - Note that G₀ (Def. E.1(e)) and E.33(c2) (「含实发射」) also contain cuts through the direct SS gluons.
  - Restrict "the G₀-restricted E.33(c2) HOLDS" and ERR-S1b(ii) to the uncut lines.
  - Add the power-counting lemma: O(1) unregulated, located at the collinear ends; O(λ_BK⁻/a + λ_AK⁺/a) with two-sided G7 regulators. Or record it as O13.
* **F2 (P4(b)).** Delete "(Sp′) (no single-state gap) unchanged". Either add the 12V partner s c₂[i/(A₁+k₁)][i/(A₂+k₁)][i/(A″+k₁+k₂)] and state that it shifts W(12,21) only by O(λ_AK/a + λ_B/K) (verified: R4), or state that the class imposes (Sp′) on J_B only.
* **F3 (P5).** Replace the identity by D_C = ∫dΦ₃[A_A†A_B + h.c.]. Give positivity in Feynman gauge (eikonal) via the common colour operator, and note the gauge dependence. Drop "sum of B†B terms".
* **F4 (T2).**
  - Add the hypothesis δ_Y ≤ ½ (or put it into ε₀).
  - Write C_c, and state that C_T depends on ln(λ_B/μ_B).
  - Derive the rate in the Im p_opp expansion or weaken it to + O(1).
* **F5 (T3(e)).** Replace ln(1 + K/μ_B) by ln(1 + a_min/(Kμ_B)) in the second term of the bound. Reduce the interpretive sentence to the proved sensitivity statement.
* **F6 (REG).** Register or recast (Sp′), (R), NF and (H_glob) per rule 00.1-1 and §6. Change "G5(ii) (shown, P5)" to "argued [A]". Give each [R] exactly one qualifier.
* **F7 (P2).** Fix the orientation convention of δ_B, since the sign of 2δ_Aδ_B depends on it.
* **F8 (P1).** Write x^A_min ≥ cP_A⁺, or define x as a fraction.
* **F9 (T2′(b)).** Make "jet B's poles give the same by symmetry" the mirror statement under NF_A.
* **F10 (CMP).** For Zhou et al.: the caveat applies to Sec. VI only; the A⁻_G sector uses n_f⁻ (eqs. 85–86).
* **F11 (LIT).** Add Barcaro–Gao–Gaunt–Pathak, arXiv:2607.14259.
* **F12 (L8(c), minor).** Change the intermediate constant from 2 to 16/9 + 1. The final constant 9 is unaffected.
* **F13 (process; parent session).**
  - Write journal line 125 as `verify/extend/X1-glauber/REPORT.md`.
  - Save lines 80, 78, 111 and 132 as review_r1_1.md, review_r1_2.md, review_r2_2.md and review_r3_2.md. (This file is review_r3_1.md.)
  - Do the same for X2 and X3, and add the "save returned text if REPORT.md is missing" check to `extend()`.
  - Apply F1–F12 while patching the spec, since round 3 is the last.

## 5. Recommended decisions for the App O slots

* **X1c `lem:appO-side-independent-windows`: PASS** (P1), after F8.
* **X1f `prop:appO-twoexch-spectator`: PARTIAL.**
  - Insert T2 as an [R_cond] model theorem about the **uncut** side sum, with its restrictions in the first sentence: H_glob, NF_A∧NF_B, O(g⁴), this pattern, δ_Y ≤ ½.
  - Add T2′(c) as [P]. My non-factorized-jet check (R3) adds a fourth independent numerical confirmation of the general-jet statement.
  - The physical reading for G₀ is [P], conditional on G7 and on the cut-suppression estimate (F1).
* **X1a, X1b, X1d, X1e: not delivered**; use the fallbacks (as in round 2).
* **T3:** a remark in §O.5 with (e) as an [R_cond] sensitivity proposition after F5. Its physical reading is at most [P].
* **ERR-S1b:** include in App Q in the restricted wording of F1.
