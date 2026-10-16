# Verification batch E07–E12 (stage 2, second independent verifier)

Date: 2026-10-11. Stance: skeptical; the stage-1 report (`batch_E07_s1.md`) was read only to learn what it checked, so that a different method could be used here. No stage-1 number was taken over. Every printed equation quoted below was read by me on a **rendered page** (pdftoppm), in addition to the extracted text.

## 0. Method, sources, and how this differs from stage 1

**Literature downloaded by me** (each into its own scratch directory, read as text and rendered pages):

| paper | versions read | journal version |
|---|---|---|
| Alexandrou et al., PRD 92 (2015) 014502 | arXiv:1504.07455 v1 (28 Apr 2015), v2, v3: eq. (11) identical in all three | APS PDF not accessible |
| Chen–Cohen–Ji–Lin–Zhang, NPB 911 (2016) 246 | arXiv:1603.06664v1 | journal PDF (SCOAP3) read |
| Ji–Sun–Xiong–Yuan, PRD 91 (2015) 074009 | arXiv:1405.7640 | not accessible |
| Ebert–Stewart–Zhao, JHEP 09 (2019) 037 | arXiv:1901.03685 | Springer blocked; arXiv used |
| Ji–Jin–Yuan–Zhang–Zhao, PRD 99 (2019) 114006 | arXiv:1801.05930 | – |
| Ji–Liu–Liu, NPB 955 (2020) 115054 | arXiv:1910.11415v3 | journal PDF (SCOAP3) read |
| Ebert–Schindler–Stewart–Zhao, JHEP 04 (2022) 178 | arXiv:2201.08401 | arXiv used |
| Jia–Mo–Xiong–Yu, PRD 109 (2024) 014042 | arXiv:2401.12786v1 | journal PDF (SCOAP3) read |
| Xiong–Ji–Zhang–Zhao, PRD 90 (2014) 014051 | arXiv:1310.7471v1 | not accessible |
| Ji et al., RMP 93 (2021) 035005 | arXiv:2004.03543 v1, v2; **OSTI accepted manuscript 1819506 (= arXiv v2)** | APS typeset PDF not accessible |
| Liu, APPB 53 (2022) 4-A2 | no arXiv version | journal PDF (APPB site) read |
| Ji–Liu, PRD 105 (2022) 076014 | arXiv:2106.05310v1 | journal PDF (SCOAP3) read |
| Ji–Liu–Liu, PLB 811 (2020) 135946 | arXiv:1911.03840 v1, v2 | journal PDF (SCOAP3) read |
| Ji–Liu–Su, JHEP 08 (2023) 037 | arXiv:2305.04416v1 | journal PDF (INSPIRE OA file) read |
| Guo–Ji–Liu, PRD 103 (2021) 096010 | arXiv:2103.11506v1 | journal PDF (SCOAP3) read |
| Guo–Ji–Liu–Yang, PRD 108 (2023) 034003 | arXiv:2305.06992 v1, v2 | journal PDF (SCOAP3) read |

**Independent physics sources (none by Liu et al.)**: Kidonakis, PRL 102 (2009) 232003 [arXiv:0903.2561], eqs. (6), (9); Grozin–Henn–Korchemsky–Marquard (GHKM), JHEP 01 (2016) 140 [arXiv:1510.07803], eqs. (2.13)–(2.14), (5.2)–(5.5); Bell, NPB 812 (2009) 264 [arXiv:0810.5695], eqs. (39)–(42) (direct two-loop heavy-to-light current); Neubert, EPJC 40 (2005) 165, eq. (66) (earlier prediction of γ′); Broadhurst–Grozin, PRD 52 (1995) 4082 [hep-ph/9410240], eqs. (1.3), (2.1) (two-loop HQET heavy–light current); Diehl, Phys. Rept. 388 (2003) 41, eqs. (18), (19), (22); Ryskin–Roberts–Martin–Levin (RRML), Z. Phys. C 76 (1997) 231 [hep-ph/9511228], eq. (2). For literature status only: del Río–Vladimirov, arXiv:2304.14440.

**INSPIRE**: no erratum is recorded for any paper in this batch.

**My scripts**: `verify/claims/batch_E07_s2_scripts/`, with outputs in `run_outputs.txt`. Run them with `python3 -I`.
* `s2_e07i_tmc.py`: exact symbolic moments, plus quadrature with a test PDF different from the one stage 1 used.
* `s2_e07ii_cusp.py`: exact analytic evaluation at φ = π/2 from two independent formulas. In Kidonakis' formula, coth(iπ/2) = 0. In GHKM's, ξ = 0, and the HPLs are integrated along the path by my own code.
* `s2_e07iv_linear.py`: my own derivation of the linear-divergence coefficient.
* `s2_e08_e09_e11.py`: sign algebra, the RGE solution, and numerical integration with running coupling.
* `s2_e10_gammaC.py`: a different decomposition from stage 1, γ_C = 2(γ′ − γ̃_J), with inputs from Bell and Broadhurst–Grozin.
* `s2_e12_gpd.py`: Dirac traces, Gordon reduction, and the RRML normalization test, derived by hand.

I also re-ran the project scripts `check_GammaS2.py`, `check_gammaC2.py` and `check_RGE_structure.py`. They agree with my results.

**Notation.**
* γ_HH is the constant in Γ_cusp(α_s, θ) → θ Γ_cusp(α_s) + γ_HH(α_s) as θ → ∞. Γ_cusp(α_s, θ) is the d/d ln μ anomalous dimension of a single cusp, with Γ_cusp(α_s, θ) = (α_sC_F/π)(θ coth θ − 1) + O(α_s²). Continuing θ = iφ gives the Euclidean angle φ.
* L_b = ln(μ²b²/b_0²) (APPB eq. (15)).
* β_0^CTX = 11C_A/3 − 4T_Fn_f/3, β_0^Liu = −β_0^CTX/(2π), so dα_s/d ln μ = β_0^Liu α_s².

## 1. Summary

| id | verdict | what must be corrected before printing | already in the literature? |
|---|---|---|---|
| E07 | **confirmed** (i)–(iv) | (ii): JLL do not state "π/2" or a number. The π/2 follows from the geometry (JSXY eqs. (3)–(4), ESZ eq. (4.26)); the mismatch C_FC_A(ζ_3/2 − π²/24)(α_s/π)² is computed here. ESSZ only *report* JLL's argument. (iii) and (iv) are self-corrections by overlapping author groups. (iii): Jia et al. also state that the missing piece was absent in Ji–Liu–Zahed 2019 [Ji:2018waw], which affects LAMET §11 row Y6. | yes (by construction) |
| E08 | **confirmed** | The PRD 105 Γ_S^(2) display is **eq. (73)** in the journal (eq. (72) only in arXiv v1; journal (72) is S_r1^(1)). In APPB it is the unnumbered display directly below eq. (81). | no (JHEP 2023 (A.6) has the right value, but claims agreement with the old formulas) |
| E09 | **confirmed** | The equation numbers refer to arXiv v2, which is identical to the OSTI accepted manuscript; the typeset RMP was not accessible. Equivalent fix: flip (205)–(206), or flip the quoted Γ_S^(1), Γ_S^(2) and the single log of (208). The minimal fix, consistent with most of the paper, is to flip (205)–(206). | no |
| E10 | **confirmed** | none | not as an erratum; correct value in JHEP 2023 (A.13) and del Río–Vladimirov 2023 |
| E11 | **confirmed** | The single-log error is in APPB (81) only, and it is the E08 sign error propagated. RMP (208) has only the factor-2 error in the L_b² term. | no |
| E12 | **confirmed** | The ½ enters via (24) into (26), and into the polarized (58)–(59). Eq. (25) is unaffected. Print the contraction unambiguously. | yes (authors' own correction, 2023) |

---------------------------------------------------------------------------------------------------------------------------------

## 2. E07 — LaMET literature errors reported by others

### 2.1 (i) Alexandrou et al. TMC formula
*Printed* (identical in arXiv v1, v2, v3; rendered pp. 3, 5):
* eq. (4): ⟨P|O^{3…3}|P⟩ = 2ã^{(0)}_{2k}(P_3)^{2k} Σ_j C(2k−j, j) μ^j ≡ 2ã_{2k}(P_3)^{2k}, with μ = M²/4P_3²;
* eq. (11): **q̃(x,P_z) = q̃^{(0)}(ξ,P_z)/(1+μξ²), ξ = 2x/(1+√(1+4μx²))**, "the Nachtmann variable".
So ã_n = K_n ã_n^{(0)} with K_n = Σ_j C(n−j, j)μ^j, and K_1 = 1.

*Independent check* (`s2_e07i_tmc.py`, exact):
* The inverse map is x = ξ/(1−μξ²), so dx/dξ = (1+μξ²)/(1−μξ²)².
* Hence ∫dx x^{n−1} q̃ = ∫dξ ξ^{n−1} q̃^{(0)}(ξ)/(1−μξ²)^{n+1}. The weight for n = 1 is (1−μξ²)^{−2} = 1 + 2μξ² + 3μ²ξ⁴ + … ≠ K_1 = 1, so ∫q̃ = ∫q̃^{(0)} + 2μ⟨ξ²⟩ + O(μ²).
* **Particle number is not conserved**, and the higher moments miss K_n as well.
* With the test PDF q ∝ x^{−0.3}(1−x)^{3.5}, the deviations are:

| μ | n = 1 | n = 2 | n = 3 | n = 4 |
|---|---|---|---|---|
| 0.05 | +0.37 % | −3.3 % | −5.9 % | −8.0 % |
| 0.25 | +1.98 % | −13 % | −19.6 % | −23.7 % |

*Correct inversion*: Chen et al., NPB 911 (2016) 246, App. B (journal = arXiv), **eq. (61)**:
q̃(x) = [(f_+/2) q(2x/f_+) − (f_−/2) q(−2x/f_−)]/√(1+4c), with f_± = √(1+4c) ± 1 and c = M²/4P_z².
* Its moment factor is [(f_+/2)^{n+1} − (−f_−/2)^{n+1}]/√(1+4c) (a Lucas sequence), which equals K_n identically (sympy, n = 1…8).
* Eq. (62) gives ∫q̃ = ∫q. Numerically it is exact.

*Attribution* (journal, rendered/text): App. B, below (61): "Note that this is different from the result obtained in Ref. [30]. Their result does not conserve quark number." Also Sec. 3.2, below (24): "Unlike the mass-correction expression of Ref. [30], particle number is conserved in this expression." Ref. [30] in the journal ([25] in arXiv) = Alexandrou et al. PRD 92, 014502. **Confirmed.**

### 2.2 (ii) Bent Euclidean soft functions
*Geometry (read)*:
* JSXY, eqs. (3)–(4): the subtraction is √(S_{n_x,n_y}/(S_{n_x,n_z}S_{n_z,n_y})), with S_{v̄,v} built from links to −∞ along v and v̄, and n_x² = n_y² = −1, n_x·n_z = n_y·n_z = n_x·n_y = 0.
* ESZ, eq. (4.26): the bent soft function has lines along ẑ and −n̄_⊥, where n̄_⊥ ⊥ (b_⊥, ẑ), closed by transverse links (Fig. 9b).
* Every cusp of either construction therefore joins two orthogonal space-like directions. After Wick rotation this is a Euclidean cusp of angle **φ = π/2**: cos φ = 0, independent of orientation conventions.
* ESZ footnote 7: the JSXY combination with finite links equals the bent function at one loop.
* Ji:2018hvs (1801.05930, eq. (3)) uses the *rectangular* (naive) loop S_{n_z,n_z}. ESSZ's attribution of the bent function to it ("Refs. [34,36]") is loose. JLL's attribution [17,19] = Ji:2014hxa, Ebert:2019okf is the accurate one.

*Physics — two independent two-loop formulas, evaluated exactly at π/2* (`s2_e07ii_cusp.py`):
* (A) Kidonakis eq. (9), Minkowski angle γ, normalization (α_s/π)², Γ_S^(1) = C_F(γ coth γ − 1). At γ = iπ/2:
  * coth(iπ/2) = 0, and every bracket multiplying coth or coth² is finite (Li_n(e^{−2γ}) = Li_n(−1), ln(1−e^{−2γ}) = ln 2), so those terms drop.
  * This leaves Γ^{(2)}(π/2) = −(K/2)C_F + C_FC_A(½ + ζ_2/2 − π²/8), with K = C_A(67/18 − ζ_2) − 5n_f/9.
  * Result: **Γ^{(2)}(π/2) = C_FC_A(π²/24 − 49/36) + (5/9)C_FT_Fn_f**.
* (B) GHKM (5.5) at x = e^{iφ} = i:
  * ξ_GHKM = (1+x²)/(1−x²) = 0 kills every ξ-term.
  * Ã_1 = −1, Ã_2 = π²/3 + ½H_{1,1} − A_2(1) = 2 − π²/4, Ã_3 = −A_3(1) = π²/3 − 1. Here A_2(1) = π²/3 − 2 and A_3(1) = 1 − π²/3, both checked numerically at φ = 10⁻⁶.
  * Result: (½)C_A(Ã_2+Ã_3) − (67/36)C_A + (5/9)T_Fn_f = the same value.
* A and B agree to 14 digits at φ = 0.7, 1.2 and π/2 − 10⁻⁶.
* Large angle: both give **γ_HH^{(2)} = C_FC_A(−49/36 + π²/12 − ζ_3/2) + (5/9)C_FT_Fn_f** (Kidonakis at θ = 40: C_A coefficient −1.1396725292668).
* One loop: both values equal −C_F.
* **Mismatch: Γ^{(2)}(π/2) − γ_HH^{(2)} = C_FC_A(ζ_3/2 − π²/24)(α_s/π)² = 0.18979 C_FC_A(α_s/π)²**; the n_f parts are equal.

*Why this breaks the matching (logic checked)*: a constant anomalous-dimension mismatch alone could be absorbed into a different γ_C of H(ζ_z/μ²). The point is that the soft subtraction factors depend only on μb.
* The ratio S_bent/S_I therefore carries δγ^{(2)} α_s² ln(μ²b²) at O(α_s²).
* This b-dependence cannot be absorbed into a b-independent kernel, so the factorization fails from two loops.

*Attribution (read)*:
* JLL NPB 955 (2020) 115054, pp. 7–8 (journal) = arXiv v3 p. 4–5: "the soft function is controlled by cusp anomalous dimension at large hyperbolic angle, while other proposed soft functions are composed by Euclidean gauge links with circular angle which cannot be arbitrarily large. Although, the cusp anomalous dimension of the bent soft functions in Ref. [17,19] coincide with S_I at one-loop level, in general it is different beyond one-loop order [24]. The difference … will lead to different logarithmic structure ln μ²b⊥² …". Here [17] = Ji:2014hxa, [19] = Ebert:2019okf, [24] = Korchemsky–Radyushkin 1987.
* The same remark appears in PLB 811, pp. 4–5 (journal).
* ESSZ (arXiv:2201.08401, §2, p. 14): "it was argued that the factorization utilizing this function will break down at two loops [38]", with [38] = JLL. This is a report, not an independent derivation.
* ESZ §5.1 left the two-loop question open.

**Confirmed.**

### 2.3 (iii) Jia et al. 2024
Read in arXiv:2401.12786v1 and in the journal PRD 109 014042:
* Abstract: "we take this chance to correct the incomplete expression of the quasi-PDFs in the 't Hooft model reported in our preceding work [Y. Jia et al. Phys. Rev. D 98, 054011 (2018)]".
* Sec. VII (journal): "the expression of the quasi-PDF given in Ref. [21] is incomplete because the authors of Ref. [21] have neglected the contribution from Õ_{1/2}(z) and the next-to-leading Fock component of the mesonic state, which actually renders a net O(N_c⁰) contribution".
  * Eq. (83) splits q̃_n = q̃_n^{(0)} + q̃_n^{(1)}; (85) q̃^{(0)} "agrees with Ref. [21]"; (86) q̃^{(1)} is new.
  * The new term fades away as P → ∞.
* Conclusions: "correct the mistake made in Ref. [21]". App. C compares old and new.
* [21] (journal; [19] in arXiv) = Jia–Liang–Xiong–Yu PRD 98 054011 = Jia:2018qee. This is a **self-correction**, for flavour-neutral mesons.
* The same paper states that "the q̃_n^{(1)} piece arising from the higher Fock state has been missed in the preceding work [21, 49, 50]", with [49] = Ma–Ji PRD 104 036004 (2021) and **[50] = Ji–Liu–Zahed PRD 99 054008 (2019) = Ji:2018waw**. LAMET §11 row Y6 cites Ji:2018waw as recovering the PDF at LO and NLO in 1/N_c; that row needs this caveat.

I did not re-derive the 't Hooft-model computation. **Confirmed as an attribution.**

### 2.4 (iv) Xiong et al. 2014, transverse-momentum cutoff
*Printed* (arXiv v1, rendered pp. 4, 6):
* eq. (7) q̃^{(1)} contains +μ/((1−x)²P^z) in all three regions;
* eq. (8) Z̃_F^{(1)} contains −μ/((1−y)²P^z);
* the matching factor (14)–(16) contains μ/((1−ξ)²P^z);
* μ is the transverse-momentum cutoff.

Text: "There is a linear divergence arising from the self-energy of the gauge link … present in lattice regularization", and p. 6: "we propose to include this linearly divergent term within our factorization formula".

RMP (arXiv v2 = OSTI accepted manuscript), Sec. II.B: "There is a linear divergence in the cut-off regulator, leading to Λ_UV/P^z term, which is absent in DR. Thus, to keep 1/(P^z)² power counting, it is important to work in a renormalization scheme where this term does not exist."

*Independent derivation* (`s2_e07iv_linear.py`):
* One-loop Feynman-gauge self-energy of the space-like link: log W(z) = −g²C_F ∫d³k/((2π)³2|k|) (1−cos k_z z)/k_z², with |k_⊥| < Λ.
* Fourier transform with P^z/2π, for x ≠ 1: q̃_tad(x) = (α_sC_F/2π)[√(Λ² + (1−x)²P_z²) − |1−x|P^z]/((1−x)²P^z) → (α_sC_F/2π)[Λ/((1−x)²P^z) − 1/|1−x|] + O(P^z/Λ).
* The linear term reproduces Xiong et al.'s term exactly, in coefficient and sign. Equivalently, log W = −δm|z| with δm = α_sC_FΛ/2.
* The remainder −1/|1−x| is the DR tadpole of LAMET §4.6(b).

**Confirmed.** It is a scheme defect, flagged by the authors themselves and by the RMP; the author lists overlap.

---------------------------------------------------------------------------------------------------------------------------------

## 3. E08 — Γ_S^(2) sign in APPB and PRD 105

*Printed* (journal pages, rendered):
* **APPB 53 (2022) 4-A2**, pp. 4-A2.32–33:
  * (77) μ²d ln S_I/dμ² = −Γ_S;
  * (78) μ²d ln S_DY/dμ² = −(Y+Y′)Γ_cusp + Γ_S;
  * (79) S_DY^{(1)} = (α_sC_F/π)[1−(Y+Y′)]L_b;
  * (80) Γ_S^{(1)} = α_sC_F/π;
  * (81) ln S_I^{(2)} = c_2 − Γ_S^{(2)}L_b + α_s²(β_0C_F/2π)L_b², followed by the unnumbered display **Γ_S^{(2)} = (α_s²/π²)[C_FC_A(−49/36 + π²/12 − ζ_3/2) + C_FN_F·5/18]**, "the two-loop anomalous dimension for S_I^{−1}";
  * (15) L_b = ln(μ²b⊥²/(4e^{−2γ_E})).
* **PRD 105 (2022) 076014, journal**, pp. 076014-11, -12, -15:
  * (46) S_rN = e^{−D_N};
  * (47) μ²d ln S_rN/dμ² = −((N+1)/2)Γ_S;
  * (48) μ²d ln S_N^−/dμ² = −(Y+Y′)((N+1)/2)Γ_cusp + ((N+1)/2)Γ_S;
  * (70) S_1^{−(1)} = (α_sC_F/π)[1−(Y+Y′)]L_b;
  * (72) S_{r1}^{(1)} = −(α_sC_F/π)L_b;
  * text: "Γ_S^{(1)} = α_sC_F/π";
  * **(73)**: the same Γ_S^{(2)} expression as APPB.
  * In arXiv:2106.05310v1 the Γ_S^{(2)} display is eq. (72), and S_{r1}^{(1)} is (71).

*Analysis*:
* At one loop, (78)+(79) [or (48)+(70)] give the constant term of μ²d ln S_DY/dμ² as +α_sC_F/π = +Γ_S^{(1)}, consistent with (80).
* To all orders, μ²d ln S_DY/dμ² = −Γ_cusp(θ). At one loop this is (α_sC_F/π)(1 − θ coth θ), matching (79). For θ → ∞ it becomes −θΓ_cusp − γ_HH.
* Hence **Γ_S^{APPB/PRD105} = −γ_HH**, and μ²d ln S_I/dμ² = γ_HH. With S_I^{(1)} = −(α_sC_F/π)L_b, this gives −α_sC_F/π = γ_HH^{(1)} at one loop.
* γ_HH^{(2)} was computed from two independent formulas in §2.2.
* sympy: printed Γ_S^{(2)} − γ_HH^{(2)} = 0 (T_F = ½). So the papers print **+γ_HH^{(2)}**, and both colour structures carry the wrong sign.
* APPB's own words, "anomalous dimension for S_I^{−1}", mean +Γ_S by (77). The printed value is that of S_I.
* Correct: **Γ_S^{(2)} = −γ_HH^{(2)} = (α_s²/π²)C_F[C_A(49/36 − π²/12 + ζ_3/2) − (5/9)T_Fn_f]**.

*Cross-checks of the "correct" references*:
* RMP (arXiv v2, display after (208)): Γ_S^{(2)} = −(α_s²/π²)[…] = −γ_HH^{(2)}. This is consistent with its stated Γ_S^{(1)} = +α_sC_F/π; for its RGE signs, see E09.
* JHEP 08 (2023) 037 (A.6) (journal = arXiv): 2γ_HL − γ_s = −α_sC_F/π + (α_s²/π²)[C_FC_A(−49/36+π²/12−ζ_3/2) + 5C_Fn_f/18]. I verified by hand that (A.4)–(A.5) combine to this. It is correct as γ_HH.
* However, its sentence "agrees with our previous formula for γ_HH = Γ_S [43,72,76]" (journal numbering; [44,73,77] = RMP, PLB 811, PRD 105 in arXiv) glosses over the opposite sign convention of PRD 105 and APPB.

**Confirmed** (with the citation corrected to PRD 105 eq. (73)).

---------------------------------------------------------------------------------------------------------------------------------

## 4. E09 — RMP eqs. (205)–(206)
*Printed* (arXiv v2 pp. 41–42; identical in the OSTI accepted manuscript 1819506):
* (203) S_DY = e^{(Y+Y′)K + D};
* (204) S_r ≡ e^{−D};
* **(205) μ²d ln S_r/dμ² = Γ_S(α_s)**, "where Γ_S is the constant part of the cusp-anomalous dimension at large hyperbolic cusp angle Y+Y′ for the off-light-cone soft function";
* **(206) μ²d ln S_DY/dμ² = −(Y+Y′)Γ_cusp − Γ_S**;
* (207) S_DY^{(1)} = (α_sC_F/2π)[2−2(Y+Y′)]L_b, "and Γ_S^{(1)} = α_sC_F/π";
* (208) D^{(2)} = c_2 + Γ_S^{(2)}L_b − (α_s²β_0C_F/2π)L_b², with Γ_S^{(2)} = −(α_s²/π²)[…].

*Check* (`s2_e08_e09_e11.py`):
* (203), (204), (207) give K^{(1)} = −(α_sC_F/π)L_b, D^{(1)} = +(α_sC_F/π)L_b, and therefore S_r^{(1)} = −(α_sC_F/π)L_b.
* Then μ²d ln S_r/dμ² = −α_sC_F/π + O(α_s²) = −Γ_S^{(1)}, which contradicts (205).
* (206) has constant term −α_sC_F/π, while (207) gives +α_sC_F/π. Contradiction.

*Remark*: (205)–(206) are consistent with each other, and with a literal reading of the verbal definition (Γ_S = γ_HH). In that reading, the stated Γ_S^{(1)}, the quoted Γ_S^{(2)} and the single-log sign of (208) would all be wrong instead. The paper is internally inconsistent either way.
* Minimal correction, consistent with three of its statements: (205) → −Γ_S and (206) → −(Y+Y′)Γ_cusp + Γ_S. These are the signs of APPB (77)–(78) and PRD 105 (47)–(48).
* Convention-free statement: **μ²d ln S_r/dμ² = γ_HH(α_s) = −α_sC_F/π + (α_s/π)²C_F[C_A(−49/36+π²/12−ζ_3/2) + (5/9)T_Fn_f] + O(α_s³)**.
* PLB 811 (20) also prints μ²d ln S_r/dμ² = Γ_S, but there Γ_S^{PLB} = γ_HH by its (18), (19), (21). So PLB is consistent.

**Confirmed** (numbering of arXiv v2 / accepted manuscript).

---------------------------------------------------------------------------------------------------------------------------------

## 5. E10 — PLB 811 eq. (26), γ_C^(2)

*Printed*:
* **PLB 811**, journal p. 5 (= arXiv v2):
  * (23) μ d ln H/dμ = Γ_cusp ln(ζ_z/μ²) + γ_C, with γ_C = 2γ_F + Γ_S + 2γ_H;
  * (25) one loop, giving γ_C^{(1)} = −α_sC_F/π;
  * (26) and the text below it: **γ_C^{(2)} = (a_1C_FC_A + a_2C_F² + a_3C_FN_f)/(16π²)**, with a_1 = 60ζ_3 − 19π²/3 + 68/27, a_2 = −48ζ_3 + 28π²/3 − 8, a_3 = 2π²/3 − 62/27.
  * γ_C^{(2)} is the coefficient of α_s². This is consistent with the printed Γ_cusp^{(2)} and with the RGE structure of (26) for dα_s/d ln μ = β_0α_s².
* **JHEP 08 (2023) 037** (journal = arXiv):
  * (4.4) d ln H_HL/d ln μ = Γ_cusp ln(ζ_z/μ²) + γ̃_H − iπ sign(z)Γ_cusp, with "γ̃_H ≡ γ_C";
  * (A.12) γ̃_H^{(1)} = −C_F/π;
  * (A.13) as quoted in the claim.

*Independent derivation by a route different from stage 1* (`s2_e10_gammaC.py`):
* H = C_HL^+ C_HL^−, the pair of heavy–light Sudakov form factors.
* The QCD heavy-to-light current matches onto SCET as J_QCD = C J_SCET, with d ln C/d ln μ = Γ_cusp ln(u m_b/μ) + γ′ (Bell (39)).
* It also matches onto HQET as J_QCD = C_m(μ) J̃(μ), with J̃(μ) = Z̃_J^{−1}J̃_0 and γ̃_J = d ln Z̃_J/d ln μ (Broadhurst–Grozin (1.3)).
* Hence the HQET→SCET coefficient C_HL has d ln C_HL/d ln μ = ½Γ_cusp ln(ζ_z/μ²) + γ′ − γ̃_J, and **γ_C = 2(γ′ − γ̃_J)**.
* Inputs:
  * Bell (41)–(42), a direct two-loop computation that "confirms the conjecture" of Neubert 2004, eq. (66) with κ = 4/3: γ′ = −5C_F a + a²[C_F²(2π² − 3/2 − 24ζ_3) + C_AC_F(22ζ_3 − 1549/54 − 7π²/6) + n_lT_FC_F(250/27 + 2π²/3)];
  * Broadhurst–Grozin (2.1): γ̃_J = −3C_F a + C_F a²[C_F(5/2 − 16ζ_2) + C_A(−49/6 + 4ζ_2) + (10/3)T_FN_f];
  * a = α_s/4π.
* Result: γ_C^{(1)} = −C_F/π, and **γ_C^{(2)} − JHEP (A.13) = 0 exactly** (sympy).
* Consistency: γ′^{(2)} = γ_1^q + γ_1^Q (Becher–Neubert values) holds exactly. So the result is equivalent to γ_C = γ_V + 2γ_F + γ_HH, with the inputs of JHEP (A.2), (A.3), (A.6).

*Comparison*:
* **PLB(26) − correct = −C_F[C_A(12π² − 196 − 72ζ_3) + 37n_f]/(72π²) = −2γ_HH^{(2)} + C_Fn_f/(24π²)** exactly.
* The C_F² parts agree.
* For n_f = 4: correct 0.10335, PLB 0.74944.
* The β-function convention does not affect these coefficients.

*Literature status*:
* JHEP 2023, below (4.4), states "γ̃_H ≡ γ_C … is known to two-loop [PLB 811, PRD 105]" without noting the discrepancy.
* del Río–Vladimirov (arXiv:2304.14440 = PRD 108 114009) computed the NNLO qTMD coefficient directly and state that Ji–Liu–Su's results "agree with ours".
* No erratum to PLB 811 exists.

**Confirmed.**

---------------------------------------------------------------------------------------------------------------------------------

## 6. E11 — two-loop L_b² coefficient of ln S_I
*Printed*:
* APPB (81) (§3);
* RMP (208): D^{(2)} = c_2 + Γ_S^{(2)}L_b − (α_s²β_0C_F/2π)L_b², with D = −ln S_r;
* both with β_0 = −(11C_A/3 − 4N_FT_F/3)/(2π) = β_0^Liu.

*Derivation*:
* ln S_I(μ) = ∫_{ln μ_b²}^{ln μ²} γ_HH(α_s(μ′)) d ln μ′² + O(α_s²) constant, which gives **ln S_I = −(α_sC_F/π)L_b + α_s²[−(C_Fβ_0^CTX/(8π²))L_b² + γ̂_HH L_b + c_2]**.
* In Liu's convention the L_b² coefficient of ln S_I is +α_s²β_0^Liu C_F/(4π); the papers print 1/(2π).
* RGE residuals at O(α_s²) (sympy):
  * APPB (81): −(C_Fβ_0^CTX/4π²)L_b (the factor 2) − 2γ̂_HH (the single-log sign).
  * RMP (208): −(C_Fβ_0^CTX/4π²)L_b only.
* Numerical integration with exact one-loop running: the L_b² coefficient is −0.14112 at α_s = 0.001 and −0.14231 at α_s = 0.004. It tends to −C_Fβ_0/(8π²) = −0.14072 (n_f = 4); the printed value is −0.28145.
* The APPB single-log error is not independent of E08. The structure "−Γ_S^{(2)}L_b" is right, given (77); the wrong-sign printed Γ_S^{(2)} turns +γ̂_HH α_s²L_b into −γ̂_HH α_s²L_b.

**Confirmed.**

---------------------------------------------------------------------------------------------------------------------------------

## 7. E12 — Guo–Ji–Liu 2021: spurious ½ in the gluon GPD
*Printed*:
* **GJL 2021**, journal (= arXiv v1), pp. 096010-4 to -6:
  * (13) M = (8√2πα_s/M_V²)φ*(0)G(t,ξ)(ε_V*·ε);
  * (14) G = (1/2ξ)∫dx A(x,ξ)F_g;
  * (16) "The standard gluon GPD F_g is defined as [40]": F_g ≡ (1/(P̄^+)²)∫(dλ/2π)e^{iλx}⟨P′|**Tr**{F^{+i}(−λn/2)F^+_i(λn/2)}|P⟩;
  * (17) dσ/dt = α_EMe_Q²(16πα_s)²|ψ_NR(0)|²|G|²/(4(W²−M_N²)²·3M_V³);
  * (20) the standard parametrization;
  * (21)–(23) the standard moments, ∫_0^1 dx H_g = A_{2,0}^g + (2ξ)²C_2^g ≡ H_2;
  * (24) G = (1/(ξ²P̄^{+2}))⟨P′|**½**Σ_{a,i}F^{a,+i}F_i^{a,+}|P⟩ = (1/(2ξ²P̄^{+2}))⟨P′|T_g^{++}|P⟩;
  * (25) the EMT form factors;
  * (26) |G|² = (1/ξ⁴){(1−t/4M_N²)E_2² − 2E_2(H_2+E_2) + (1−ξ²)(H_2+E_2)²};
  * (32) A_{2,0}^g = (1 − t/m_A²)^{−2}∫_0^1 dx x f_g(x).
* **GJLY 2023**, journal (= arXiv v1, v2), Sec. II:
  * "the definition of gluon GPDs in Eq. (16) of the previous work [22] includes an extra factor of ½ from the trace operator Tr, which should be removed. Correspondingly, the extra factor of ½ in Eq. (24) … shall be removed as well. The revision will leave the main cross section formula unchanged, i.e., Eqs. (13) and (17)";
  * **(1)** F_g = (1/(P̄^+)²)∫(dλ/2π)e^{iλx}⟨P′|F^{a+i}(−λn/2)F_i^{a+}(λn/2)|P⟩, "where the index a sums over all colors";
  * **(5)** |G|² = (4/ξ⁴){…}, "an extra factor of 4 … compared to the Eq. (26) in Ref. [22]. The same factor of 4 should be multiplied to the polarized |G|² in Eqs. (58) and (59)".
  * [22] = GJL PRD 103 096010.

*Independent checks* (`s2_e12_gpd.py`):
* (a) **Internal inconsistency of 2021.**
  * With Tr(t^at^b) = δ^{ab}/2, (16) gives ∫_{−1}^1 dx F_g = ⟨T_g^{++}⟩/(2P̄^{+2}).
  * With (20) and the Gordon reduction this means ∫_0^1 dx H_g = (A_{2,0} + 4ξ²C_2)/2. That contradicts (23), and (32) in the forward limit (∫_0^1 H_g = ⟨x⟩_g).
* (b) **Forward limit of 2023 (1).** With λ = P̄^+z^−, (1/(P̄^+)²)∫dλ = (1/P̄^+)∫dz^−, so (1) is Diehl's F^g, eq. (18), with contraction G^{+μ}G_μ{}^{+} = Σ_{i=1,2}G^{+i}G^{+i}. Its forward limit is H^g(x,0,0) = x g(x) (Diehl (22)).
* (c) **Spin sum by Dirac traces** (20 random on-shell kinematic points, relative deviation 1.3×10⁻¹⁵):
  * ½Σ|ū(P′)[Hγ^+ + E iσ^{+ν}Δ_ν/2M]u(P)|² = 4P̄^{+2}[(1−ξ²)H² − 2ξ²HE − (ξ² + t/4M²)E²].
  * The C term of (25) reduces to H_2 = A + 4ξ²C, E_2 = B − 4ξ²C (residual 10⁻¹⁵).
  * The trace form equals the printed brace identically.
  * Leading moment: G = (1/ξ²)∫_{−1}^1 dx F_g = ⟨T^{++}⟩/(ξ²P̄^{+2}) (corrected), which gives **(4/ξ⁴){…} = 2023 (5)**. With the 2021 ½ one gets (1/ξ⁴){…} = 2021 (26).
* (d) **Independent normalization test.** In the high-energy limit:
  * Im A = π[δ(x−ξ)+δ(x+ξ)], H_g(ξ,ξ,0) ≈ xg(x) with x = 2ξ = M_V²/W², and Γ_ee = 16πα²e_Q²|ψ(0)|²/M_V².
  * GJL (13), (14), (17) give dσ/dt|_0 = 256π⁴αe_Q²α_s²|ψ(0)|²(xg)²/(3M_V⁷).
  * This equals RRML eq. (2) (read: Γ_eeM³π³α_s²[xg]²/(48αQ̄⁸), Q̄² = M²/4, x = 4Q̄²/W²) with **ratio 1** for the corrected F_g, and ratio **1/4** for the 2021 trace normalization.
  * So the unchanged amplitude (13)–(17) requires the standard F_g.

*Printing notes*:
* Eq. (25) is unaffected; the ½ enters via (24) into (26), and into the polarized (58)–(59).
* The contraction "F^{a+i}F^{a+}_i" is typographically ambiguous. Read literally with the mostly-minus metric, F^{a+}{}_i = −F^{a+i}. Print F^{a+i}F^{a}{}_{i}{}^{+} = Σ_{i=1,2}F^{a+i}F^{a+i}, or Diehl's G^{+μ}G_μ{}^{+}.
* Diehl (19) records that Goeke et al.'s gluon GPDs differ from Diehl's by a factor 2. The 2021 ½ amounts to that convention, but it is inconsistent with GJL's own moment relations and amplitude.

**Confirmed.**

---------------------------------------------------------------------------------------------------------------------------------

## 8. Required edits to our material (beyond stage 1)
1. CLAIMS E08 / YZLIU §4.1 E2:
   * "[Ji:2021znw] eq. (72)" → "PRD 105 (2022) 076014, eq. (73) (journal; eq. (72) of arXiv:2106.05310v1)";
   * APPB: "unnumbered display directly below eq. (81)".
2. E09, E11: cite the RMP equations as in arXiv:2004.03543v2 (identical to the OSTI accepted manuscript 1819506).
3. E11: the APPB single-log error is the E08 sign error propagated into (81). RMP (208) has only the L_b² error.
4. LAMET §10.4(c):
   * add the explicit mismatch Γ^{(2)}(π/2) − γ_HH^{(2)} = C_FC_A(ζ_3/2 − π²/24)(α_s/π)², with equal n_f parts;
   * add the b-dependence argument of §2.2;
   * attribute the bent functions as JLL do (Ji:2014hxa, Ebert:2019okf), not as ESSZ do (Ji:2018hvs uses the rectangular loop).
5. LAMET §11 (Jia:2024atq): mark it as a self-correction of Jia:2018qee. Add that Jia et al. state that the same O(N_c⁰) piece was missed in Ji–Liu–Zahed 2019 (Ji:2018waw) and Ma–Ji 2021. Row Y6 needs this caveat.
6. LAMET §4.6(e): add the coefficient check: the term equals the Wilson-line linear divergence with δm = α_sC_FΛ/2 for a transverse cutoff Λ.
7. YZLIU §3.F1 / E5:
   * "propagates to (24)–(26)" → "enters via (24) into (26), and into the polarized (58)–(59); (25) unaffected";
   * print the contraction unambiguously.
