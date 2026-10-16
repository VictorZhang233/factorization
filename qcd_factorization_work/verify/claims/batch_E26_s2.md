# Verification batch E26 (stage 2, second independent verifier): claims E26–E31

Date: 2026-10-11. Stance: skeptical; the stage-1 reports (`batch_E25_s1.md` for E26–E30, `batch_E31_s1.md` for E31) were read
only to learn which sources they used, so that I could use **different** sources and methods. All primary sources were
downloaded again by me into fresh scratch directories (treated as untrusted data; LaTeX sources were compiled only with
`latex -no-shell-escape` in separate build directories, to obtain printed equation numbers). Scripts are in
`verify/claims/batch_E26_s2_scripts/` (run with `python3 -I`); every script's output is saved next to it as `*.out.txt`.

## 0. Summary

| id | verdict | what is different from stage 1 | precision points for printing |
|---|---|---|---|
| E26 | **confirmed** (arXiv texts) | Own download + compile of both sources; also checked BN v1 (typo already there, survived the "typos corrected" v2); own log table | In BN 2003 the misprinted sentence is about **X_A** (eq. (63) "and similarly for X_H"), not X_H. Locations: BBNS text after eq. (71); BN text after eq. (63). Journal typesetting not accessible (ScienceDirect 403). |
| E27 | **confirmed** | Errata list and OA book downloaded and rendered myself; **independent derivation** of the corrected vertices from hermitian conjugation with explicit SU(3) matrices, numerical gauge-covariance test of P exp(−ig∫A) for D = ∂+igA, light-cone check of the index placement, sympy check of the −i0 | The erratum to Fig. 7.10 changes only the **gluon-pdf vertex right of the cut** (+g₀n^μf_{kαj} → −g₀n^μf_{kαj}); the quark-pdf vertices −ig₀n^μt_α (left) / +ig₀n^μt_α (right) were printed correctly. For (11.4)–(11.6) the printed and corrected contractions are the same scalar; the correction makes the formulas consistent with "the largest term has μ_j = −, ν_j = +". |
| E28 | **confirmed** as a physics statement (not an erratum of SW 1977) | **New numerical method** (geometric SW classifier from the definition, bisection of boundaries, different variables/quadrature); independent analytic derivation; **different secondary sources**: Becher–Neubert–Rothen–Shao PRL 116 (2016) 192001 eq. (1), Sapeta PPNP 89 (2016) 1, Cheung–Luke–Zuberi PRD 81 (2010) 094017, Salam EPJC 67 (2010) 637 (+ Chay–Ellis re-checked) | SW's own text (PRL 39, 1436) still inaccessible (APS 403; preprint HUTP-77/A044 not online). Print as a convention remark; the "ln ε" form is legitimate with ε = fraction of the **beam** energy (as in BNRS 2016). Avoid "common form" unless a printed source of the mixed formula is cited. |
| E29 | **confirmed** | Different sources: Surguladze–Samuel RMP 68 (1996) 259 analytic eq. (Ranalytic1) and history; PDG 2025 QCD review eq. (9.9b); INSPIRE records; own d_abc d_abc and π²-term checks | "recalled; verify" can be dropped. |
| E30 | **confirmed** | Read Collins 1993 appendix, Collins 2002, BHS 2002, Boer–Brodsky–Hwang 2003, Boer–Mulders–Pijlman 2003, Collins 2011 pp. 534–536; PT Dirac signs re-derived with **Collins' own 1993 PT matrix** (Bjorken–Drell) | Collins 2002 gives the explicit sign reversal only for f_1T^⊥ (eq. (3)); for h_1^⊥ cite Boer–Mulders–Pijlman 2003, Boer–Brodsky–Hwang 2003, or Collins 2011 §13.17.2 (p. 536). |
| E31 | **confirmed as an attribution only** | Own reading of the OA PDF (p. 553 verbatim, all citations of CSS 1988 located: pp. 553, 558, 560), pagination of the 2011 printing checked against the errata's page references; Aybat–Sterman 2008 read | Collins does **not** say which errors of CSS 1988 he corrects; CSS 1988 (NPB 308, 833) not accessible. Print only as Collins' own assessment. |

---

## 1. E26 — BBNS 2001 / BN 2003: "m_M" must read m_B

**Sources (own download).** BBNS: arXiv:hep-ph/0104110 (v1 = only version; journal ref NPB 606 (2001) 245–321).
BN: arXiv:hep-ph/0308039 **v2** (arXiv comment: "typos and errors in data tables corrected; version to appear in Nuclear Physics B";
NPB 675 (2003) 333–415) and also **v1** (4 Aug 2003). Compiled equation numbers (my build): BBNS (ai) = (46), (Hiexpr) = (57),
(Xdef) = (59), (XHparam) = **(71)**, (XAparam) = (72); BN (fact) = (2), (XHdef) = (50), (XAdef) = (56), (XHparam) = **(63)**; the
unlabelled a_i^p(M_1M_2) formula = **(35)** (label inserted in a copy). The Elsevier pages returned HTTP 403 (curl and WebFetch);
**the journal typesetting was not seen**. INSPIRE lists no erratum for either paper.

**BBNS 2001, eq. (71) and the following sentence (verbatim):**
X_H = (1 + ϱ_H e^{iφ_H}) ln(m_B/Λ_h); ϱ_H ≤ 1 — "with an arbitrary phase φ_H, which may be caused by soft rescattering. In other
words, we assign a 100% uncertainty to the ``default value'' X_H = ln(m_M/Λ_h) ≈ 2.4."
Elsewhere in the same paper: "(using central values for all input parameters and setting X_H = ln(m_B/Λ_h) ≈ 2.4)"; after eq. (72):
"default value X_A = ln(m_B/Λ_h)"; in the parameter section: "fixed at the default value X_H = X_A = ln(m_B/Λ_h)"; and
"μ_h = √(Λ_h μ) with Λ_h = 0.5 GeV". Eq. (59) defines X_H^M = ∫₀¹ dy/(1−y) (M = π or K), and the text says "We thus expect that
X_H^M ∼ ln(m_b/Λ_QCD)" — the superscript M is a meson label, which plausibly produced the misprint m_M.

**BN 2003, eq. (63) and the following sentence (verbatim, identical in v1 and v2):**
X_A = (1 + ϱ_A e^{iφ_A}) ln(m_B/Λ_h); ϱ_A ≤ 1, Λ_h = 0.5 GeV, "and similarly for X_H. Here φ_A is an arbitrary strong-interaction
phase, which may be caused by soft rescattering. In other words, we assign a 100% uncertainty to the ``default value''
X_A = ln(m_M/Λ_h) ≈ 2.4."

**Numerics** (`e26_logs.py`): ln(5.2793/0.5) = 2.3569, ln(5.28/0.5) = 2.3571 (≈ 2.4, as stated); with m_b: 2.13–2.26; with any light
meson the value is ≤ 0.58 (π: −1.276, K: −0.013, ρ: 0.438, K*: 0.579). So only m_B reproduces "≈ 2.4" and the authors' own
parametrizations (71), (63). **Both sentences are misprints: m_M → m_B.** In BN 2003 the misprinted default value is written for X_A
(X_H being "similar"), so the claim's wording "X_H = ln(m_M/Λ_h)" is exact for BBNS only.

**Notation part.** BN 2003, text after eq. (2): "Whenever the spectator antiquark line goes from the B̄ meson to one of the final-state
mesons we call this meson M_1 and the other one M_2." Eq. (35):
a_i^p(M_1M_2) = (C_i + C_{i±1}/N_c) N_i(M_2) + (C_{i±1}/N_c)(C_Fα_s/4π)[V_i(M_2) + (4π²/N_c) H_i(M_1M_2)] + P_i^p(M_2),
so V refers to the emitted meson M_2. BBNS eq. (46) is πK-specific: a_{1,I}, a_{4,I} carry V_K and a_{1,II}, a_{4,II} carry H_{Kπ};
a_{2,I}, a_{3,I}, a_{9,I} carry V_π and H_{πK}; a_5, a_7 carry −V'_π and −H'_{πK}. In eq. (57), H_{Kπ} contains F_0^{B→π}(0) and the
twist-3 term Φ_p^π, i.e. π receives the spectator and K is emitted. Hence BBNS also label V (and the first index of H) by the
emitted meson; the two notations are consistent, and the claim's remark is a transcription caution, not an erratum.

**Verdict: confirmed.** Literature: no published correction found; the correct value is printed elsewhere in BBNS 2001 itself.

---

## 2. E27 — Collins 2011: errata to Fig. 7.10 and eqs. (11.4)–(11.6); sign of g

**Sources (own download).** (i) Author's page https://www.cantab.net/users/johncollins/qcdbook/ (dated 14 May 2026) linking
`qcd-errata.pdf`: "Errata and updates for 'Foundations of Perturbative QCD'", John Collins, **22 May 2026**, 10 pp. Its Sec. 3,
"Corrections and updates relative to published paperback edition of November 2013" (running head "CORRECTIONS AND UPDATES TO
NOV. 2013 PRINTING"), states that the corrections "apply to both editions". (ii) OA reissue (CUP 2023, doi:10.1017/9781009401845),
full-book PDF, 640 pp. (PDF created 2013-01-16, modified 2023-07-17). The errata say its content is that of the Nov. 2013 paperback.
I rendered p. 9 (eq. (2.2)), p. 43 (Fig. 3.1), p. 236 (Fig. 7.10) and read p. 402 and p. 497 (eq. (13.40)) from the text layer.
**Pagination check:** the errata's Sec. 1 page references to the May 2011 edition (eqs. (13.110) p. 530, (13.116) p. 532, (A.16)
p. 587, (12.80) p. 464, (11.18) p. 410, (12.8) p. 428) all fall on the same pages in the reissue, so the page numbers apply to the
2011 printing as well.

**Printed Fig. 7.10 (p. 236, rendered):** quark pdf, bare: −ig₀n^μ(t_α)_{kj} | ig₀n^μ(t_α)_{kj}; renorm.: −ig₀Z₃^{1/2}n^μ(t_α)_{kj} |
ig₀Z₃^{1/2}n^μ(t_α)_{kj}; gluon pdf, bare: g₀n^μf_{kαj} | **g₀n^μf_{kαj}**; renorm.: g₀Z₃^{1/2}n^μf_{kαj} | **g₀Z₃^{1/2}n^μf_{kαj}**.
Caption: "Here, n^μ = δ^μ_− = (0, 1, 0_T). In the Wilson line for a gluon pdf, the generating matrix for the adjoint representation was
used: (T_α)_{kj} = if_{kαj}. The sign of the vertex is reversed compared with Collins and Soper (1982b), and corresponds to the sign of the
coupling in our Lagrangian, whose Feynman rules are in Fig. 3.1."

**Errata (verbatim):** "In Fig. 7.10, there should be a reversal of the sign of the Feynman rule for the gluon-to-Wilson-line coupling to
the right of the final-state cut in the gluon pdf." Corrected table: quark entries unchanged; gluon pdf, bare: g₀n^μf_{kαj} |
**−g₀n^μf_{kαj}**; renorm.: g₀Z₃^{1/2}n^μf_{kαj} | **−g₀Z₃^{1/2}n^μf_{kαj}**.

**Printed p. 402:** H·C = H_{μ1…μN} ∏_j g^{μjνj} C_{ν1…νN} (11.4); "Let k_j be the momentum of gluon j flowing into H. The largest term in
its polarization sum has μ_j = −, ν_j = +"; g^{μjνj} = K^{μjνj} + G^{μjνj} (11.5); K^{μjνj} = k_j^{μj} w₂^{νj}/(k_j·w₂ − i0),
G^{μjνj} = g^{μjνj} − k_j^{μj}w₂^{νj}/(k_j·w₂ − i0) (11.6); "w₂ = (0, 1, 0_T)".
**Errata:** "P. 402: In Eqs. (11.4)–(11.6), subscript Lorentz indices should be replace[d] by superscripts, and vice versa", giving
H·C = H^{μ1…μN} ∏_j g_{μjνj} C^{ν1…νN}, g_{μjνj} = K_{μjνj} + G_{μjνj}, K_{μjνj} = k_{jμj}w_{2νj}/(k_j·w₂ − i0).

**Sign of g (rendered pages).** Eq. (2.2): D_μψ₀ = (∂_μ + ig₀t^αA^α_{(0)μ})ψ₀; eq. (2.3): G = ∂A − ∂A − g₀fAA; Fig. 3.1: quark–gluon
vertex −igμ^ε(t^α)_{ab}γ^μ. With our D = ∂ − igA (vertex +igγ^μt^a): **g_Collins = −g**. Eq. (13.40) (p. 497):
W(x; ∞, n)_{ab} = P e^{−ig₀∫₀^∞dλ n·A^α_{(0)}(x+λn) t_α}.

**Independent derivation** (`e27_wilson_vertices.py`, all 19 checks PASS):
1. For D = ∂ + igA with Collins' gauge transformation (2.4a,b), a path-ordered product in a random SU(3) background transforms as
   W → U(b)WU(a)^† only for P exp(**−**ig∫dz·A) (covariance defect 6×10⁻⁸ versus 1.3 for the other sign).
2. Left of the cut the O(g) term of W is −ig₀n^μ(R_α)_{kj}; right of the cut the line is W^†, whose O(g) term with the **same labels** is
   +ig₀n^μ(R_α)_{kj} for any hermitian R. Fundamental: −ig₀n^μ(t_α)_{kj} | +ig₀n^μ(t_α)_{kj} (as printed). Adjoint with Collins'
   (T_α)_{kj} = if_{kαj} (checked hermitian, = −if_{αkj}, [T_a,T_b] = if_{abc}T_c): **g₀n^μf_{kαj} | −g₀n^μf_{kαj}**, i.e. the errata,
   not the printing.
3. Light-cone algebra: H_μK^{μν}C_ν (printed) and H^μK_{μν}C^ν (corrected) are the same scalar, (H·k)(w₂·C)/(k·w₂), with k·w₂ = k⁺.
   The corrected K has K_{−+} = 1, the printed one K^{−+} = 0. For collinear C (C⁺ large) the largest term of H^μg_{μν}C^ν is
   (μ,ν) = (−,+); in lower-index notation it is (+,−). So the printed sentence "μ_j = −, ν_j = +" fits only the corrected index placement.
4. −i0: attaching k (flowing into H) to the outgoing struck quark p_f = (0,p⁻,0_T) gives (p_f−k)² + i0 = −2p⁻[k⁺ − k²/(2p⁻) − i0];
   Collins (7.50) ∫₀^∞dy e^{i(k+i0)y} = i/(k+i0) for k flowing out of the line, hence −i/(k⁺ − i0) for k flowing **into** a
   future-pointing line. So K_{μν} = k_μw_{2ν}/(k·w₂ − i0) is the DIS (future-pointing) prescription, consistent with Collins p. 553
   ("(SI)DIS, where future-pointing Wilson lines worked").

**Verdict: confirmed.** Precision: describe the Fig. 7.10 erratum as concerning the gluon-pdf vertex to the right of the cut; the
quark-pdf vertices quoted in the claim are correct in both the printing and the errata. Already in the literature: the author's errata
list (22 May 2026 version, Sec. 3).

---

## 3. E28 — Sterman–Weinberg: ln 2ε versus ln ε

**Primary text.** SW, PRL 39 (1977) 1436 (preprint HUTP-77/A044): APS returns HTTP 403 (curl, WebFetch); OpenAlex/Semantic Scholar
list it as closed access; the INSPIRE abstract does not define ε; no preprint scan found (KEK search unavailable, Deep Blue copy behind
a bot check, not circumvented). **SW's own typography was not seen by me either.**

**Secondary sources read by me (different from stage 1 except the last):**
* **Becher–Neubert–Rothen–Shao, PRL 116 (2016) 192001** (arXiv:1508.06645v2 "PRL version"), text before eq. (1): SW "defined a dijet
  cross section … by requiring that for jet events all energy must be inside oppositely directed narrow cones of half-angle δ, except for
  a small fraction β/2 of the center-of-mass energy Q. They computed the corresponding cross section as
  σ(β,δ)/σ₀ = 1 + (α_sC_F/4π)(−16 ln δ ln β − 12 ln δ + c₀)" (eq. (1)), and "the original Sterman-Weinberg jets have c₀ = 10 − 4π²/3"
  (σ₀ = Born). Here β/2 is a fraction of the total energy, i.e. **β is a fraction of the beam energy Q/2**. Converting:
  (α_sC_F/π)[−4 ln δ ln β − 3 ln δ − π²/3 + 5/2], which with β = 2ε is exactly −(C_Fα_s/π)[4 ln δ ln 2ε + 3 ln δ + π²/3 − 5/2].
* **Sapeta, PPNP 89 (2016) 1** (arXiv:1511.09336, Sec. 2): "a final state is classified as a 2-jet event if at least a fraction 1−ε of the
  total available energy is contained in a pair of cones of half-angle δ" and "the exact 3-jet fraction at NLO is
  f₃ = (g_s²/3π²)(3 ln δ + 4 ln δ ln 2ε + π²/3 − 7/4) [SW]". Since g²/3π² = C_Fα_s/π and σ_tot = σ₀(1 + (3/4)C_Fα_s/π),
  f₃ = 1 − σ_2j/σ_tot reproduces the −5/2 bracket for σ_2j/σ₀ (−5/2 + 3/4 = −7/4).
* **Cheung–Luke–Zuberi, PRD 81 (2010) 094017** (arXiv:0912.5509): "The SW algorithm defines a dijet event as one where all but a fraction
  β of the total energy is contained within a pair of oppositely directed cones of half-angle δ"; their SW jet function contains ln 2β.
* **Salam, EPJC 67 (2010) 637** (arXiv:0906.1833): "at least a fraction 1−ε of the event's energy … in two cones of opening half-angle δ".
* Chay–Ellis, PRD 55 (1997) 2728 (hep-ph/9607464), eq. (stweinberg): "a fraction (1−ε) of the total energy …",
  (dσ/dΩ)_B[1 − (4α_s/3π){(3 + 4 ln 2ε) ln δ + π²/3 − 5/2} + O(ε,δ)] (re-checked; also used at stage 1).
* Stagnitto (arXiv:2508.14700) gives only the double-log form 4α_sC_F/π · log(1/ε) log(1/δ) (soft-collinear approximation, with
  "E the total energy"); at that accuracy ln ε versus ln 2ε is beyond the stated precision. No printed **full** O(α_s) bracket combining
  "4 ln δ ln ε" with total-energy ε was found; in our material the ln ε form is "the task's" form (research/c_ee/DERIVATION.md row 4b′, §10 item 1).

**Independent analytic derivation** (`e28_asymptotic.py`, sympy). With u = x₃, r = y₁₃/x₃, exactly
f dx₁dx₂ = [N₀/(r(1−r)) − 2u²] du dr/u, N₀ = 1 + (1−u)². For ε ≲ δ ≪ 1 the leading-power 3-jet region is u > 2ε (ε = fraction of
the total energy, x₃ = 2E_g/√s), σ(1−u) < r < 1 − σ(1−u), σ = sin²δ. Then I₃ = 2(−ln σ)∫_{2ε}^1 N₀du/u + 2∫₀¹N₀(−ln(1−u))du/u − 1
= 8 ln δ ln 2ε + 6 ln δ + 2π²/3 − 7/2, using ∫_{2ε}^1N₀du/u → −2 ln 2ε − 3/2 and ∫₀¹N₀(−ln(1−u))du/u = π²/3 − 5/4 (checked to 25
digits). Hence c_2j ≡ (σ_2j/σ₀ − 1)/(C_Fα_s/π) = 3/4 − I₃/2 = −[4 ln δ ln 2ε + 3 ln δ + π²/3 − 5/2] (sympy difference = 0).

**Independent numerics** (`e28_sw_geometric.py`, 12 s). Different from both earlier computations:
* The two-jet test is implemented **directly from the SW definition by geometry**, with no derived boundary formulas. Parton directions
  fit into a pair of opposite cones of half-angle δ iff their lines (directions mod π) fit into an arc of length 2δ:
  L = π − (largest circular gap) ≤ 2δ.
* 2-jet ⇔ L({1,2,3}) ≤ 2δ, or there is a parton k with E_k ≤ ε√s and L({i,j}) ≤ 2δ. At most one parton can be outside, since two
  outside would need E_in ≥ (1−ε)√s > √s/2.
* Opening angles come from exactly rewritten, well-conditioned half-angle formulas. A first version that built the antiquark
  direction from a vector sum lost precision for a soft antiquark collinear to the gluon. I found this through a broken q↔q̄
  symmetry and fixed it. Checks: Σθ_ij = 2π to 1.8×10⁻¹⁵, momentum balance to 8×10⁻¹⁶.
* Boundaries are found by a dense scan plus bisection to machine precision. The inner integral is exact in the logistic variable t
  (r = 1/(1+e^{−t})); the outer integral is adaptive Gauss–Kronrod in ln u and −ln(1−u).
* On 4×10⁵ random events the geometric classifier agrees with the algebraic conditions (a)/(b) used by the project and by stage 1
  (0 mismatches). This independently confirms the region definition: for three momenta summing to zero, L({1,2,3}) ≤ 2δ ⇔
  min θ_ij ≤ 2δ.

| (ε, δ) | c_2j numeric | ln 2ε form | ln ε form | numeric − (ln 2ε form) |
|---|---|---|---|---|
| (1e-2, 0.1) | −29.921596 | −29.913176 | −36.2973 | −8.4e-3 |
| (1e-3, 0.03) | −77.441171 | −77.437727 | −87.1600 | −3.4e-3 |
| (1e-4, 0.01) | −143.867260 | −143.866854 | −156.6351 | −4.1e-4 |
| (1e-5, 0.005) | −214.201229 | −214.201393 | −228.8914 | +1.6e-4 |
| **(1e-6, 0.003)** | **−288.281051** | **−288.281180** | **−304.3875** | +1.3e-4 |

I₃(1e−6, 0.003) = 578.0621017028, the same to all printed digits as the project script and stage 1, by a different algorithm. The
result is unchanged when the u-integration starts at 10⁻³ε: the classifier finds no 3-jet events with E_g < ε√s, as expected for ε ≪ δ.
**Beam-energy convention** (E_k ≤ ε_b√s/2, same code): at ε_b = 10⁻⁶, δ = 0.003, c_2j = −304.387397 versus the ln ε_b form
−304.387544. So the ln ε form is right exactly when ε is a fraction of the beam energy. The two forms differ by
4 ln 2 |ln δ| = 16.106364 at δ = 0.003.

**Verdict: confirmed as a physics statement.** The formula with ln 2ε for total-energy ε, the beam-energy alternative, the size of the
mismatch, and the three numbers (−288.2811, −288.2812, −304.39) are all reproduced. It is **not an erratum of SW 1977**: every source
says SW used total-energy ε with ln 2ε. Print it as a convention remark, citing e.g. BNRS 2016 eq. (1) for the beam-energy form.

---

## 4. E29 — GKL 1988 O(α_s³) R-ratio, later corrected

**History (INSPIRE records, read via the API).**
* GKL, PLB 212 (1988) 238 (JINR-E2-88-254), abstract: "The obtained correction is large. For example at √s ⋍ 34 GeV in the MS scheme it is
  about 2.5 times larger than the previous O(α_s²) term."
* Surguladze–Samuel, PRL 66 (1991) 560, with the **erratum PRL 66 (1991) 2416 listed in the record**, abstract: "The result differs from a
  previous calculation and is much smaller."
* GKL, PLB 259 (1991) 144 (UM-TH-91-01), abstract: "total analytical reevaluation …
  R(s) = 11/3[1 + α_s/π + 1.409(α_s/π)² − 12.805(α_s/π)³]" for five flavours.
* Surguladze–Samuel, Rev. Mod. Phys. 68 (1996) 259 (hep-ph/9508351, source read), Sec. on R(s): "These calculations were first attempted by
  Gorishny, Kataev and Larin (1988). However, it was shown that those results were incorrect. … an independent calculation … was completed
  (Surguladze and Samuel, 1991a,b). The result is much smaller and has the opposite sign compared with the old 1988 result. This finding
  was confirmed shortly after that by Gorishny, Kataev and Larin (1991)." The introduction has a footnote: "This calculation was attempted
  earlier by Gorishny, Kataev and Larin (1988) but, unfortunately, errors were found."

**Numbers.**
* SS RMP eq. (Ranalytic1) (SU(3), MS-bar, μ² = s): non-singlet a³ coefficient
  87029/288 − (121/8)ζ₂ − (1103/4)ζ₃ + (275/6)ζ₅ + n_f(−7847/216 + (11/6)ζ₂ + (262/9)ζ₃ − (25/9)ζ₅) + n_f²(151/162 − (1/18)ζ₂ − (19/27)ζ₃),
  plus (Σ_fQ_f)² a³ [55/72 − (5/3)ζ₃].
* Their general-group singlet term (Ranalytic0) is (α_s/4π)³(ΣQ_f)²(d_abc/4)²[176/3 − 128ζ₃].
* **PDG 2025** QCD review, eq. (9.9b): c₃ = −6.63694 − 1.20013n_f − 0.00518n_f² − 1.240η, with η = (Σe_q)²/(N_cΣe_q²), N_c = 3.

**My check** (`e29_r3_check.py`, all PASS):
* The SS analytic formula gives −6.636936 − 1.200134n_f − 0.0051784n_f² and singlet 55/72 − 5ζ₃/3 = −1.239539.
* r₂ = 1.9857 − 0.1153n_f.
* The ζ₂ terms of r₃ equal −(π²/3)β₀² exactly, with β₀ = (11 − 2n_f/3)/4, i.e. they are the analytic-continuation terms.
* d_abc d_abc = 40/3, computed from the Gell-Mann matrices; the general-group singlet term reduces exactly to 55/72 − 5ζ₃/3.
* (ΣQ)²r_S = 3ΣQ²·η·r_S for n_f = 3…6.
* Totals: −10.28394 (n_f = 3), −11.68560 (4), **−12.80463 (5)**, −14.27207 (6). The n_f = 5 value agrees with GKL 1991's −12.805.
* Side remark: SS RMP's own numerical eq. prints the constant as "−6.6368"; the exact value of their analytic formula is −6.63694
  (CKK/BCK/PDG).

**Verdict: confirmed.** Print with GKL 1991, SS 1991 (+ erratum) and, for the value, PDG/BCK 2008 or SS RMP 1996.

---

## 5. E30 — Collins 1993 T-odd argument invalidated by the Wilson line

**Collins 1993** (hep-ph/9208213v2, "V. 2 has misprints corrected and an appendix added, as in the published version" = NPB 396 (1993) 161).
* Main text: "Sivers suggested that the k_T distribution of the quark could have an azimuthal asymmetry when the initial hadron has
  transverse polarization. However, such an asymmetry is prohibited because QCD is time-reversal invariant. This is shown in the
  appendix." Just before that, after eq. (1): "We have ignored here the subtleties needed to make this a gauge invariant definition:
  an appropriate path ordered exponential of the gluon field is needed".
* Appendix: PT with "PT = iγ⁰γ¹γ³", "PT|p,L⟩ = |p,R⟩, PT|p,R⟩ = −|p,L⟩", gives f̂(LR) = −f̂(LR), hence "f̂(LR) = f̂(RL) = 0 … This
  contradicts Sivers' suggestion."

**Collins 2002** (hep-ph/0204004v3 = PLB 536 (2002) 43; my compile: eqs. (1)–(4)).
* Abstract: "Recently, Brodsky, Hwang and Schmidt have proposed a new mechanism … An earlier proof that the Sivers asymmetry vanishes
  because of time-reversal invariance is invalidated by the path-ordered exponential of the gluon field in the operator definition of
  parton densities. Instead, the time-reversal argument shows that the Sivers asymmetry is reversed in sign in hadron-induced hard
  processes (e.g., Drell-Yan)".
* Text: "A proof [Collins 1993] that I gave to the contrary must therefore be incorrect."
* Eq. (2): P(x,k_T,s_T,ζ)|_{future-pointing W} = P(x,k_T,−s_T,ζ)|_{past-pointing W}.
* Eq. (3): f_1T^⊥(x,k_T,ζ)|_DIS = −f_1T^⊥(x,k_T,ζ)|_DY.
* For h_1^⊥: "The failure of the time-reversal argument applies to more than the Sivers asymmetry. There is also the possibility of a
  nonzero transversity of a quark in an unpolarized hadron". Eq. (4) defines h_1^⊥ with past-pointing lines for DY. **No explicit
  sign-reversal equation for h_1^⊥** is given.

**BHS 2002** (hep-ph/0201296v2 = PLB 530 (2002) 99): final-state gluon exchange gives a leading-twist SSA in SIDIS.

**Explicit h_1^⊥ statements.**
* Boer–Mulders–Pijlman, NPB 667 (2003) 201 (hep-ph/0303034v3): h_1^{⊥(1)[±]}(x) = ±h̃_1^{⊥(1)}(x), "those involving the functions
  f_1T^{⊥(1)} and h_1^{⊥(1)} change sign".
* Boer–Brodsky–Hwang, PRD 67 (2003) 054003 (hep-ph/0211110): in the scalar-diquark model, "the functions arising from initial-state
  interactions have an overall minus sign compared to those in Eq. (h1perpschem), as pointed out by [Collins-02]", for both f_1T^⊥ and
  h_1^⊥.
* Collins 2011, p. 534: "there is a change of sign between SIDIS and DY (Collins, 2002) for the T-odd functions, i.e., for the Sivers
  and Boer-Mulders functions"; p. 535, eq. (13.124); p. 536: the Boer–Mulders function "therefore also reverses sign between SIDIS and
  Drell-Yan".

**My check** (`e30_pt_bd.py`, all PASS), using Collins' own 1993 conventions: Bjorken–Drell representation, M = iγ⁰γ¹γ³.
* M⁻¹γ^{μ*}M = γ^μ (PT is a symmetry of the Dirac equation).
* For the projections Γ the PT-plus-hermiticity map Γ → γ⁰(γ⁰M^†γ⁰Γ^*M)^†γ⁰ = η_ΓΓ gives η = +1 for γ⁺ and η = −1 for γ⁺γ₅,
  iσ^{j+}γ₅ and γ⁺γ^jγ₅. So Φ^{[Γ]}_future(S) = η_Γ Φ^{[Γ]}_past(−S).
* Hence f_1T^⊥ (S-odd in Φ^{[γ⁺]}) and h_1^⊥ (S-even in Φ^{[iσ^{j+}γ₅]}) reverse sign, while f_1, g_1, h_1 etc. do not.
* Without Wilson lines (future = past) the S-odd part of Φ^{[γ⁺]} must vanish, which is Collins' 1993 conclusion.

**Verdict: confirmed.** The physics is an [R] consequence of PT invariance plus the operator definitions; process assignment is
SIDIS future-pointing, DY past-pointing. Attribution: the invalidation and f_1T^⊥ sign flip are Collins 2002 (eqs. (2)–(3)) after BHS
2002; for h_1^⊥ cite BMP 2003 / BBH 2003 / Collins 2011 §13.17.2.

---

## 6. E31 — CSS 1988 "with correction of errors" (Collins 2011 §14.4, p. 553)

**Verbatim (OA PDF, p. 553, first paragraph of §14.4 "Factorization for Drell-Yan"):** "For the general treatment of the Glauber region,
I will follow the proof given by Collins, Soper, and Sterman (1988), but with some important improvements and with correction of
errors. That reference supersedes earlier work (Bodwin, 1985; Collins, Soper, and Sterman, 1985a)."
**Pagination:** identical in the 2011 printing (see the E27 pagination check). **Bibliography** (pp. 606, 608): Bodwin (1985)
PRD 31, 2616–2642, "Erratum: D34, 3932 (1986)"; CSS (1985a) NPB 261, 104–142; CSS (1988) "Soft gluons and factorization" NPB 308,
833–856. These match the claim's list.

**Which errors?** A full-text search of the book finds CSS 1988 cited only on pp. 553, 558 and 560. **None names an error.** The changes
Collins does describe are:
* p. 558: independence of the remainder factor from the cut placement V — "A proof of this result (Collins, Soper, and Sterman, 1988)
  can be made by examining x⁻-ordered perturbation theory for R … Instead I will show here an argument that uses commutators for the
  gluon field". This is an alternative proof.
* p. 560 (§14.4.5): "the treatment of the Glauber region was originally formulated (CSS 1988) only in the context of situations using
  integrated parton densities … In fact, the argument works equally well for the TMD case." This is an extension.
* pp. 560–561 (§14.4.6): "there is one step that needs enhancement … cancellation of the soft factor". DY has past-pointing lines; they
  are equated to future-pointing ones by T invariance (§13.17.5).

CSS 1988 itself is not accessible: no INSPIRE fulltext, ScienceDirect blocked, no preprint scan (ITP-SB-87-69) found. Aybat–Sterman,
arXiv:0811.0246, "outline an extension of the proof of factorization in Ref. [CSS 1988]" and note that plus-momentum integrals in the
eikonal subdiagram "do not generally converge [CSS 1988]". They do not identify errors either.

**Verdict: confirmed as an attribution only.** Print: "Collins (2011, §14.4, p. 553) states that his treatment of the Glauber region follows
CSS (1988) 'with some important improvements and with correction of errors', and that CSS (1988) 'supersedes earlier work (Bodwin,
1985; Collins, Soper, and Sterman, 1985a)'." Do not list or characterise specific errors of CSS 1988, and do not imply that we checked them.

---

## 7. Files

`verify/claims/batch_E26_s2_scripts/`:
* `e26_logs.py` / `.out.txt`: candidate default values ln(m/0.5 GeV).
* `e27_wilson_vertices.py` / `.out.txt`: SU(3) Wilson-line vertices left and right of the cut, gauge covariance of P exp(−ig∫A) for
  D = ∂+igA, index placement in (11.4)–(11.6), −i0 (19/19 PASS).
* `e28_sw_geometric.py` / `.out.txt`: geometric-classifier evaluation of the SW cross section (total- and beam-energy conventions),
  classifier versus algebraic conditions.
* `e28_asymptotic.py` / `.out.txt`: analytic small-(ε,δ) limit.
* `e29_r3_check.py` / `.out.txt`: O(α_s³) R-ratio coefficients from SS RMP 1996, singlet normalisation, η, totals.
* `e30_pt_bd.py` / `.out.txt`: PT signs of the TMD Dirac projections with Collins' 1993 PT matrix.
