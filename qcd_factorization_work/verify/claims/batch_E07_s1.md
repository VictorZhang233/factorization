# Verification batch E07–E12 (stage 1, independent verifier)

Date: 2026-10-10. Default stance: skeptical. The claims come from `frontier/lamet/LAMET.md` (§4.6(e), §5.1, §10.4(c), §11) and
`frontier/yzliu/YZLIU.md` (§2, §3.A5(e)–(f), §3.B2, §3.F1, §4.1 E2–E5).

## 0. Method and sources

* **I downloaded all primary literature myself** into a scratch directory. I did not use the copies in `frontier/lamet/papers/`. The downloads are untrusted data and were read as text and rendered pages only. Every equation quoted below was read on a **rendered page** (pdftoppm), not only in the extracted text.
  * **arXiv** (latest versions): 1504.07455 (v3, 2015-07-08, after publication), 1603.06664, 1405.7640, 1901.03685, 1910.11415 (v3), 2401.12786, 1310.7471,
    2106.05310 (v1, the only version), 2305.04416, 0904.1021 (v3), 2004.03543 (v2, 2021-04-25), 1911.03840 (v2, 2020-11-09), 2311.06907, 2103.11506,
    2305.06992 (v2), 2201.08401, 2304.14440. Auxiliary: 0903.2561, 1510.07803, hep-ph/0303113, 0903.1126, hep-ph/0307382, hep-ph/9511228v2, hep-ph/9407339.
  * **Journal versions** (SCOAP3 repository PDFs, open access): PLB 811 (2020) 135946; **PRD 105 (2022) 076014**; NPB 955 (2020) 115054; NPB 911 (2016) 246;
    PRD 103 (2021) 096010; PRD 108 (2023) 034003; PRD 109 (2024) 014042; JHEP 08 (2023) 037; JHEP 02 (2024) 204; PRD 108 (2023) 114009; JHEP 09 (2019) 037;
    JHEP 04 (2022) 178. **APPB 53 (2022) 4-A2**: journal PDF from the APPB site (it has no arXiv version).
  * **Not accessible:** the RMP 93 (2021) 035005 journal PDF (APS, not open access). I used arXiv v2 (final revision 2021-04-25; the journal appeared online 2021-08-30).
    Also inaccessible: the journals PRD 92 (2015) 014502 (arXiv v3 is post-publication), PRD 90 (2014) 014051 and PRD 91 (2015) 074009 (arXiv v1 used).
* **INSPIRE API:** every texkey resolves to exactly one record. INSPIRE records no erratum for any paper of this batch. Full-text searches among the papers citing PLB 811 for "incorrect", "typo", "misprint", "wrong sign" and "erratum" found no notice of E08–E11.
* **Independent formula sources** (none by Liu et al.):
  * two-loop cusp anomalous dimension: Becher–Neubert PRD 79 (2009) 125004, eqs. (11), (13)–(15), (17); Kidonakis PRL 102 (2009) 232003, eq. (9);
    Grozin–Henn–Korchemsky–Marquard JHEP 01 (2016) 140, eqs. (2.13)–(2.14), (2.21), (5.2)–(5.5);
  * HQET heavy–light current: Chetyrkin–Grozin NPB 666 (2003) 289, eq. (13);
  * γ^q (2γ^q = γ^V): Becher–Neubert JHEP 06 (2009) 081, App. A;
  * direct NNLO quasi-TMD coefficient: del Río–Vladimirov PRD 108 (2023) 114009, eqs. (8), (26), (27), (29)–(32);
  * gluon GPD normalization: Diehl Phys. Rept. 388 (2003) 41, eqs. (18), (19), (22);
  * LO J/ψ photoproduction: Ryskin–Roberts–Martin–Levin Z. Phys. C 76 (1997) 231, eq. (2);
  * leptonic width: Bodwin–Braaten–Lepage PRD 51 (1995) 1125, eqs. (4.4d), (A34).
* **My scripts** are copied to `verify/claims/batch_E07_s1_scripts/` (run with `python3 -I`; outputs in `run_outputs.txt`):
  `v_e07i_tmc.py`, `v_cusp2.py`, `v_e10_gammaC.py`, `v_e11_SI.py`, `v_e12_gpd.py`.
  I also re-ran the project scripts `frontier/yzliu/scripts/check_GammaS2.py`, `check_gammaC2.py` and `check_RGE_structure.py`. Their outputs agree with mine.

Notation: γ_HH is the constant in Γ_cusp(α_s, θ) → θ Γ_cusp(α_s) + γ_HH(α_s) for θ → ∞, in the normalization Γ_cusp(α_s, θ) = (α_sC_F/π)(θ coth θ − 1) + O(α_s²).
L_b = ln(μ²b²/b_0²). β_0^CTX = 11C_A/3 − 4T_Fn_f/3.

## 1. Summary

| id | verdict | what must change before printing | already in the literature? |
|---|---|---|---|
| E07 | **confirmed** (all four items) | (ii) ESSZ only *report* JLL's argument ("it was argued … [38]"). ESSZ attribute the bent function to Ji:2018hvs and ESZ, JLL to Ji:2014hxa and ESZ. Add the exact two-loop mismatch C_FC_A(ζ_3/2 − π²/24)(α_s/π)² ≈ 0.190 C_FC_A(α_s/π)². (iii) It is a self-correction, for flavour-neutral mesons, at O(N_c⁰). I did not re-derive it. (iv) In Xiong et al. the cutoff is called μ. The authors themselves flagged the term. | Yes, by construction (errors reported by others): Chen et al. 2016; JLL 2020 (also PLB 811 p. 5); ESSZ 2022; Jia et al. 2024; RMP 2021. |
| E08 | **confirmed** | PRD 105 citation: the **journal** equation is **(73)**. Eq. (72) is the arXiv:2106.05310v1 number. The journal (73) has the same wrong sign. | Not as an erratum. The correct value is in JHEP 08 (2023) 037 (A.6). That paper even claims agreement with APPB/PLB/PRD 105 ("[43,72,76]"), so it did not notice the convention clash. |
| E09 | **confirmed** | Cite the arXiv:2004.03543v2 numbering. The journal PDF was not accessible. (206) should read −(Y+Y′)Γ_cusp + Γ_S. | Not found. APPB (77)–(78) and PRD 105 (47)–(48) use the correct signs. |
| E10 | **confirmed** | None. The journal eq. number is (26), and the content is identical to arXiv v2. | Not as an erratum. The correct value is in JHEP 2023 (A.13), and independently from del Río–Vladimirov 2023's direct NNLO computation. |
| E11 | **confirmed** | State that the single-log error concerns APPB (81) only. In RMP (208) the single log is correct and only the L_b² term is wrong. | Not found. |
| E12 | **confirmed** | The ½ enters through (24) into (26). Eq. (25) (the EMT parametrization) is not wrong. Write the contraction unambiguously as F^{a+i}F^{a}{}_{i}{}^{+} = Σ_{i=1,2}F^{a+i}F^{a+i}. | Yes, by the authors themselves: Guo–Ji–Liu–Yang PRD 108 (2023) 034003, Sec. II. |

---------------------------------------------------------------------------------------------------------------------------------

## 2. E07 — literature errors reported by others (LaMET)

### 2.1 (i) Alexandrou et al. 2015, target-mass correction (TMC)
*What is printed* (arXiv:1504.07455v3 = PRD 92 014502). With μ = M²/(4P_3²), eq. (4) gives
⟨P|O^{3…3}|P⟩ = 2ã_{2k}^{(0)}(P_3)^{2k} Σ_j C(2k−j, j) μ^j, i.e. ã_n = K_n ã_n^{(0)} with K_n = Σ_j C(n−j, j)μ^j. Their claimed Mellin inversion is
**eq. (11): q̃(x,P_z) = q̃^{(0)}(ξ,P_z)/(1+μξ²), with ξ = 2x/(1+√(1+4μx²))** (the Nachtmann variable).

*Check.* The inverse map is x = ξ/(1−μξ²), so dx = (1+μξ²)/(1−μξ²)² dξ. Hence
∫dx q̃ = ∫dξ q̃^{(0)}(ξ)/(1−μξ²)² = Σ_m (m+1)μ^m ⟨ξ^{2m}⟩_{(0)} ≠ ∫q̃^{(0)}, whereas K_1 = 1 requires equality.
Numerically (`v_e07i_tmc.py`, q ∝ x^{1/2}(1−x)³): the n=1 moment changes by +1.07 % at c = μ = 0.05 and by +5.8 % at c = 0.25. The higher moments also miss K_n
(n = 2: 0.02848 instead of 0.02909 at c = 0.05). The formula therefore conserves neither particle number nor the moment relation it is meant to invert.
*Corrected version.* Chen–Cohen–Ji–Lin–Zhang NPB 911 (2016) 246, App. B (journal = arXiv), **eq. (61): q̃(x) = [ (f_+/2) q(2x/f_+) − (f_−/2) q(−2x/f_−) ]/√(1+4c)**,
with f_± = √(1+4c) ± 1 and c = M²/(4P_z²) (for γ^z); eq. (62) gives ∫q̃ = ∫q. My check reproduces K_n⟨x^{n−1}⟩_q for n = 1–4 to 12 digits.
*Attribution.* Read verbatim in App. B (journal and arXiv): "Note that this is different from the result obtained in Ref. [30]/[25]. Their result does not conserve quark number."
Ref. [30] in the journal ([25] in arXiv) is Alexandrou et al. PRD 92 014502. Also the main text after eq. (24): "Unlike the mass-correction expression of Ref. […], particle number is conserved in this expression." **Confirmed.**

### 2.2 (ii) Bent Euclidean soft functions: Euclidean π/2 cusp; wrong from two loops
*Geometry (read).*
* Ji–Sun–Xiong–Yuan PRD 91 074009, eqs. (3)–(4): the subtraction is √(S_{n_x,n_y}/(S_{n_x,n_z}S_{n_z,n_y})), with n_x² = n_y² = −1 and n_x·n_z = n_y·n_z = n_x·n_y = 0.
* ESZ JHEP 09 (2019) 037, §4.5, eq. (4.26): S̃_bent uses lines along ẑ and −n̄_⊥, with n̄_⊥ ⊥ (ẑ, b_⊥); "+ẑ and +ŷ sectors". ESZ's footnote 7 shows that the JSXY combination (finite links) equals the bent function at one loop.

So every cusp of both constructions is a Euclidean right angle, π/2.

*Attribution (read in the journal and arXiv texts).*
* JLL NPB 955 (2020) 115054, p. 5: "other proposed soft functions are composed by Euclidean gauge links with circular angle which cannot be arbitrarily large. Although, the cusp anomalous dimension of the bent soft functions in Ref. [17,19] coincide with S_I at one-loop level, in general it is different beyond one-loop order [24]. The difference … will lead to different logarithmic structure ln μ²b⊥² …". Here [17] = Ji:2014hxa, [19] = Ebert:2019okf, [24] = Korchemsky–Radyushkin NPB 283 (1987) 342.
* The same remark appears in PLB 811, p. 5 (journal).
* ESSZ JHEP 04 (2022) 178, §2: "Although refs. [34, 36] proposed a bent quasi-soft function that works at one-loop order, it was argued that the factorization utilizing this function will break down at two loops [38]". Here [34] = Ji:2018hvs, [36] = Ebert:2019okf, [38] = JLL. ESSZ therefore report JLL's argument; they do not give an independent proof.
* ESZ themselves (§5.1) left the two-loop question open ("at two loops one can recouple the −ẑ and +ŷ sectors …").

*Independent physics check (`v_cusp2.py`).* I implemented three published two-loop cusp formulas:
Becher–Neubert (Γ_hh = C_Fγ_cusp(β) + 2γ^Q, eqs. (11), (13), (15)), Kidonakis eq. (9), and GHKM eq. (5.5) with HPLs (5.2), which is natively written for the Euclidean x = e^{iφ}.
* The three agree to 14 digits at β = 0.3, 1, 3, 8, 20.
* At φ = π/2 (approached from below), all three give, in units (α_s/π)²:
  **Γ^{(2)}(π/2) = C_FC_A(π²/24 − 49/36) + (5/9)C_FT_Fn_f**, while **γ_HH^{(2)} = C_FC_A(−49/36 + π²/12 − ζ_3/2) + (5/9)C_FT_Fn_f**.
  At one loop both equal −C_F (since φ cot φ − 1 = −1 at π/2).
* The difference is **C_FC_A(ζ_3/2 − π²/24)(α_s/π)² = 0.18979 C_FC_A(α_s/π)²**; the n_f parts coincide.

The soft functions contain no scale besides b and μ, so a constant mismatch of anomalous dimensions forces a ln(μ²b²) mismatch at O(α_s²). That cannot be absorbed into a b-independent matching kernel. **Confirmed.**

### 2.3 (iii) Jia et al. 2024, 't Hooft model
Read in arXiv:2401.12786 and the journal PRD 109 014042:
* Abstract: "As a bonus, we take this chance to correct the incomplete expression of the quasi-PDFs in the 't Hooft model reported in our preceding work [Y. Jia et al. Phys. Rev. D 98, 054011 (2018)]".
* Sec. VII: "the expression of the quasi-PDF given in [19] is incomplete, because the authors of Ref. [19] have neglected the contribution from Õ_{1/2}(z) and the next-to-leading Fock component …, which actually renders a net O(N_c⁰) contribution". The missing term q̃_n^{(1)} is their eq. (86); q̃_n^{(0)} (85) "agrees with Ref. [19]". The new term fades away for P → ∞.
* Conclusions: "We take this opportunity to correct the mistake made in Ref. [19]". Their App. C compares old and new for flavour-neutral mesons.

The earlier work is Jia:2018qee (arXiv:1804.04644). This is an attribution of a self-correction. I did not re-derive the 't Hooft-model computation. **Confirmed as an attribution.**

### 2.4 (iv) Xiong et al. 2014, transverse-momentum cutoff
Read in arXiv:1310.7471 (PRD 90 014051):
* Eq. (7) (quasi-PDF) and eqs. (14)–(16) (matching factor) contain **μ/((1−ξ)²P^z)** in all three regions ξ > 1, 0 < ξ < 1, ξ < 0, where μ is the transverse-momentum UV cutoff.
* The authors: "it is important to note the existence of a linear divergence coupled to the axial-gauge singularity, which is a double pole at ξ = 1 … we propose to include this linearly divergent term within our factorization formula".
* RMP (arXiv v2, Sec. II.B) reproduces q̃^{(1)} with Λ_UV/((1−y)²P^z) and states: "There is a linear divergence in the cut-off regulator, leading to Λ_UV/P^z term, which is absent in DR. Thus, to keep 1/(P^z)² power counting, it is important to work in a renormalization scheme where this term does not exist."

**Confirmed** (it is a scheme defect rather than an algebraic error).

---------------------------------------------------------------------------------------------------------------------------------

## 3. E08 — Γ_S^{(2)} sign in APPB (81) and PRD 105

*What is printed (rendered pages).*
* **APPB 53 (2022) 4-A2** (journal):
  * (77): μ²d ln S_I/dμ² = −Γ_S;
  * (78): μ²d ln S_DY/dμ² = −(Y+Y′)Γ_cusp + Γ_S;
  * (79): S_DY^{(1)} = (α_sC_F/π)[1−(Y+Y′)]L_b;
  * (80): Γ_S^{(1)} = α_sC_F/π;
  * below (81): **Γ_S^{(2)} = (α_s²/π²)[C_FC_A(−49/36 + π²/12 − ζ_3/2) + C_FN_F·5/18]**, "the two-loop anomalous dimension for S_I^{−1}".
* **PRD 105 (2022) 076014, journal**:
  * (47): μ²d ln S_{rN}/dμ² = −((N+1)/2)Γ_S;
  * (48): … = −(Y+Y′)((N+1)/2)Γ_cusp + ((N+1)/2)Γ_S;
  * (70)–(72): S_1^{−(1)} = (α_sC_F/π)[1−(Y+Y′)]L_b and S_{r1}^{(1)} = −(α_sC_F/π)L_b; "Γ_S^{(1)} = α_sC_F/π";
  * **(73)**: the same expression as APPB.
  * In arXiv:2106.05310v1 the same content is eqs. (47), (48), (69)–(71) and **(72)**. The journal changed the CS exponent (see batch E01) but not Γ_S^{(2)}.

*Convention.* From (78) and (79) (equivalently (48) and (70)), at one loop: μ²d ln S_DY/dμ² = (α_sC_F/π)(1−θ), θ = Y+Y′. To all orders, μ²d ln S_DY/dμ² = −Γ_cusp(θ):
the soft function is the matrix element of two heavy–heavy currents at 0 and b_⊥, each with anomalous dimension Γ_{J_hh}(θ) = C_Fγ_cusp(θ) + 2γ^Q (Becher–Neubert eq. (14)).
Hence Γ_S = −γ_HH in APPB/PRD 105.

*γ_HH^{(2)} independently* (`v_cusp2.py`): Becher–Neubert eq. (17) says no constant survives in γ_cusp(β) at large β. So γ_HH = 2γ^Q, with γ^Q_1 = C_FC_A(2π²/3 − 98/9 − 4ζ_3) + (40/9)C_FT_Fn_f (eq. (13)).
The large-β limit of all three formulas (BN, Kidonakis, GHKM) gives C_A: −1.1396725292668 and T_Fn_f: +0.5555…, i.e.
**γ_HH = −α_sC_F/π + (α_s²/π²)C_F[C_A(−49/36 + π²/12 − ζ_3/2) + (5/9)T_Fn_f]**.
The zero-recoil condition Γ_hh(0) = 0 holds to 10⁻¹⁸ (project script `check_GammaS2.py`).

Further cross-checks:
* JHEP 08 (2023) 037 (A.6): 2γ_HL − γ_s = −α_sC_F/π + (α_s²/π²)[C_FC_A(−49/36 + π²/12 − ζ_3/2) + 5C_Fn_f/18]. This is consistent with (A.4)–(A.5) by hand, and identical to 2γ^Q (BN) for T_F = ½.
* del Río–Vladimirov eq. (32): −4γ_Ψ^{(2)} equals the same γ_HH^{(2)}.

*Conclusion.* APPB and PRD 105 print **+γ_HH^{(2)}** while their own convention requires Γ_S^{(2)} = −γ_HH^{(2)}. Both colour structures carry the wrong sign. Correct:
**Γ_S^{(2)} = (α_s²/π²)C_F[C_A(49/36 − π²/12 + ζ_3/2) − (5/18)n_f]** (T_F = ½).
* RMP (arXiv v2, display below (208)): Γ_S^{(2)} = −(α_s²/π²)[C_FC_A(−49/36 + π²/12 − ζ_3/2) + C_FN_F·5/18] = −γ_HH^{(2)}. This is correct relative to its stated Γ_S^{(1)} = +α_sC_F/π (but see E09 for its RGE signs).
* JHEP 2023 (A.6) is correct as γ_HH. Its sentence "agrees with our previous formula for γ_HH = Γ_S [43,72,76]" glosses over the opposite Γ_S convention of [76] = PRD 105.

Numerically, for n_f = 4: γ_HH^{(2)} = −3.077(α_s/π)². **Confirmed.**

---------------------------------------------------------------------------------------------------------------------------------

## 4. E09 — RMP eqs. (205)–(206)

*What is printed* (arXiv v2, rendered pp. 41–42):
* (203): S_DY = e^{(Y+Y′)K+𝒟} + …;
* (204): S_r ≡ e^{−𝒟};
* **(205): μ²d ln S_r/dμ² = Γ_S**;
* **(206): μ²d ln S_DY/dμ² = −(Y+Y′)Γ_cusp − Γ_S**;
* (207): S_DY^{(1)} = (α_sC_F/2π)[2−2(Y+Y′)]L_b; "and Γ_S^{(1)} = α_sC_F/π";
* (208): 𝒟^{(2)} = c_2 + Γ_S^{(2)}L_b − (α_s²β_0C_F/2π)L_b², with Γ_S^{(2)} = −γ_HH^{(2)} (see E08).

*Check* (`v_e11_SI.py`, last line). From (203), (204) and (207): K^{(1)} = −(α_sC_F/π)L_b, 𝒟^{(1)} = +(α_sC_F/π)L_b, so S_r^{(1)} = −(α_sC_F/π)L_b and μ²d ln S_r/dμ² = −α_sC_F/π + O(α_s²).
* (205) with the stated Γ_S^{(1)} = +α_sC_F/π gives +α_sC_F/π. Contradiction.
* (206) gives the constant −α_sC_F/π at one loop where (207) gives +α_sC_F/π. Contradiction.
* (205)–(206) are consistent with each other, but they are the odd ones out. The stated Γ_S^{(1)}, the printed Γ_S^{(2)} and the single-log sign of (208) all require μ²d𝒟/dμ² = +Γ_S.

Correct: **μ²d ln S_r/dμ² = −Γ_S = γ_HH** and **μ²d ln S_DY/dμ² = −(Y+Y′)Γ_cusp + Γ_S** (as in APPB (77)–(78), PRD 105 (47)–(48)).
This is also physically right: μ²d ln S_DY/dμ² = −Γ_cusp(θ) → −θΓ_cusp − γ_HH.
PLB 811 (20) prints μ²d ln S_r/dμ² = Γ_S, but there Γ_S ≡ γ_HH (Γ_S^{(1),PLB} = −α_sC_F/π from its (18), (21)), so PLB (20) is consistent. **Confirmed.**

---------------------------------------------------------------------------------------------------------------------------------

## 5. E10 — PLB 811 eq. (26), γ_C^{(2)}

*What is printed* (journal = arXiv v2, rendered):
* (23): μ d ln H/dμ = Γ_cusp ln(ζ_z/μ²) + γ_C, with γ_C = 2γ_F + Γ_S + 2γ_H;
* (26): γ_C^{(2)} = (1/16π²)(a_1C_FC_A + a_2C_F² + a_3C_FN_f), with **a_1 = 60ζ_3 − 19π²/3 + 68/27, a_2 = −48ζ_3 + 28π²/3 − 8, a_3 = 2π²/3 − 62/27**;
  β_0 = −(1/2π)(11C_A/3 − 4N_fT_F/3).

JHEP 08 (2023) 037 (journal = arXiv): (4.4) gives d ln H_HL/d ln μ = Γ_cusp ln(ζ_z/μ²) + γ̃_H − iπ sign(z)Γ_cusp, and states "γ̃_H ≡ γ_C". The same normalization and direction of H holds, since the one-loop values agree: γ̃_H^{(1)} = γ_C^{(1)} = −C_F/π. The values are
**(A.13): γ̃_H^{(2)} = (1188ζ_3 − 99π² − 1108)/(432π²)·C_FC_A − (36ζ_3 + 6 − 7π²)/(12π²)·C_F² + (1/24 + 10/(27π²))·C_Fn_f**, with (5.3): dα/d ln μ = −β_0α² − β_1α³, β_0 = 11C_A/(6π) − n_f/(3π).

*Two independent determinations of the correct value* (`v_e10_gammaC.py`):
1. **Building blocks from non-Liu literature.**
   * Structure: γ_C = γ_V + 2γ_F + γ_HH. This follows from f̃√S_r = H e^{½K ln(ζ_z/ζ)} f^TMD with μ d ln f̃/dμ = 2γ_F, μ d ln√S_r/dμ = γ_HH, μ d ln f^TMD/dμ = Γ_cusp ln(μ²/ζ) − γ_V and μ dK/dμ = −2Γ_cusp. I checked it at one loop against the RMP's f̃^{(1)} and f^{TMD(1)}.
   * Inputs:
     * γ_V^{(2)} = 2γ^q_1 (Becher–Neubert JHEP 06 (2009) 081, App. A);
     * γ_F^{(2)} = −γ̃_{j1} (Chetyrkin–Grozin eq. (13): γ̃_j = −3C_Fa + C_F[C_F(5/2 − 16ζ_2) + C_A(4ζ_2 − 49/6) + (10/3)T_Fn_l]a², with a = α_s/4π);
     * γ_HH^{(2)} = 2γ^Q_1 (BN; verified three ways).
   * Result: the sum equals (A.13) **exactly** (sympy difference 0).
2. **del Río–Vladimirov's direct NNLO coefficient function** (PRD 108 114009 eq. (26); a_s = α_s/4π, L_p = ln(μ²/(2xvP)²) = −L_z).
   * Taking ln ℂ_11 and imposing d ln ℂ_11/d ln μ² = (non-cusp) − (Γ_cusp/2)L_p with da_s/d ln μ² = −β_0a_s² leaves no L_p dependence at O(a_s) or O(a_s²). This is a consistency check of the transcription.
   * The extracted two-loop non-cusp anomalous dimension equals (A.13) **exactly**.
   * Their anomalous dimensions agree with the building blocks: γ_F = 2γ_J and γ_HH = −4γ_Ψ.

*Comparison.* **PLB (26) − correct = −C_F[C_A(12π² − 196 − 72ζ_3) + 37n_f]/(72π²) = −2γ_HH^{(2)} + C_Fn_f/(24π²)** (exactly).
* The C_F² terms agree.
* Numerically, for n_f = 4: correct γ_C^{(2)} = 0.1034, PLB 0.7494 (coefficients of α_s²).
* The n_f coefficient of (A.13), (80+9π²)/(216π²), also equals Liu–Su JHEP 02 (2024) 204 eq. (2.41) (journal = arXiv), and differs from PLB's 1/24 − 31/(216π²).

**Confirmed.**

---------------------------------------------------------------------------------------------------------------------------------

## 6. E11 — two-loop log structure of ln S_I

*What is printed.*
* **APPB (81)**: ln S_I^{(2)} = c_2 − Γ_S^{(2)}L_b + α_s²(β_0C_F/2π)L_b², with β_0 = −(11C_A/3 − 4N_fT_F/3)/(2π) "the coefficient of one-loop β-function", and Γ_S^{(2)} as in E08.
* **RMP (208)**: 𝒟^{(2)} = c_2 + Γ_S^{(2)}L_b − (α_s²β_0C_F/2π)L_b², with the same β_0; 𝒟 = −ln S_r.
* Within APPB and PLB, the H formulas (86)/(26) show that β_0 is the coefficient of dα/d ln μ: the ln³ coefficient −α_s²β_0C_F/(24π) follows from the RGE only for dα/d ln μ = β_0α². Either way, the printed numerical value fixes the L_b² coefficient of ln S_I at −C_Fβ_0^CTX/(4π²)·α_s².

*Derivation.* Write ln S_I(μ) = ln S_I(μ_b) + ∫_{ln μ_b²}^{ln μ²} γ_HH(α_s(μ′)) d ln μ′². With α_s(μ′) = α_s(μ)[1 + (β_0^CTX/4π)α_s ln(μ²/μ′²) + …], this gives
**ln S_I = −(α_sC_F/π)L_b + α_s²[−(C_Fβ_0^CTX/(8π²))L_b² + γ̂_HH L_b + c_2]**, with γ̂_HH = (C_F/π²)[C_A(−49/36 + π²/12 − ζ_3/2) + (5/9)T_Fn_f].
`v_e11_SI.py` verifies that this satisfies μ²d ln S_I/dμ² = γ_HH through α_s² (residual 0, with two-loop running).

*Printed forms tested* (`v_e11_SI.py`):
* APPB (81): the RGE residual is −(C_Fβ_0^CTX/4π²)α_s²L_b, from the factor 2 in L_b², plus −2γ_HH^{(2)}, from the single-log sign (because the printed Γ_S^{(2)} has the wrong sign).
* RMP (208): only the L_b² factor 2 is wrong (residual −C_F(11C_A − 2n_f)α_s²L_b/(12π²)). The single log is correct.
* The project's numerical integration (`check_RGE_structure.py`) gives the same L_b² coefficient: −0.14085 (α_s = 0.002) against −0.14072 predicted, versus −0.2814 printed.

**Confirmed.**

---------------------------------------------------------------------------------------------------------------------------------

## 7. E12 — Guo–Ji–Liu 2021: spurious ½ in the gluon GPD

*What is printed* (journal PRD 103 096010 = arXiv v1, rendered):
* (16): F_g ≡ (1/(P̄^+)²)∫(dλ/2π)e^{iλx}⟨P′|**Tr**{F^{+i}(−λn/2)F^+_i(λn/2)}|P⟩;
* (20): F_g = (1/2P̄^+)[H_g ūγ^+u + E_g ū iσ^{+α}Δ_α u/(2m)];
* (21)–(23): the standard moments ∫_0^1 dx H_g = A_{2,0} + (2ξ)²C_2 ≡ H_2, and similarly E_2;
* **(24)**: G = (1/(ξ²(P̄^+)²))⟨P′|**½**Σ_{a,i}F^{a,+i}F^{a,+}_i|P⟩ = (1/(2ξ²(P̄^+)²))⟨P′|T_g^{++}|P⟩;
* (25): the standard EMT form factors;
* **(26)**: |G|² = (1/ξ⁴){(1 − t/4M_N²)E_2² − 2E_2(H_2+E_2) + (1−ξ²)(H_2+E_2)²};
* (32): A_{2,0}^g(0) = ∫dx x f_g(x).

Guo–Ji–Liu–Yang PRD 108 034003 (journal = arXiv v2), Sec. II:
> "the definition of gluon GPDs in eq. (16) of the previous work … includes an extra factor of ½ from the trace operator Tr, which should be removed. Correspondingly, the extra factor of ½ in eq. (24) … shall be removed as well."

It also says that (13) and (17) stay unchanged. Its **eq. (1)**: F_g = (1/(P̄^+)²)∫(dλ/2π)e^{iλx}⟨P′|F^{a+i}(−λn/2)F^{a+}_i(λn/2)|P⟩, "where the index a sums over all colors". Its **eq. (5)** = 4 × (26), "an extra factor of 4 … compared to the Eq. (26)". The same factor applies to the polarized eqs. (58)–(59).

*Checks* (`v_e12_gpd.py`).
1. **Forward limit.** Eq. (1) with n·P̄ = 1 is exactly Diehl's eq. (18), F^g = (1/P^+)∫(dz^-/2π)e^{ixP^+z^-}⟨p′|G^{+μ}(−z/2)G_μ{}^{+}(z/2)|p⟩, with no trace factor. Diehl (22) gives H^g(x,0,0) = x g(x).
   * Hence the 2023 definition gives H_g(x,0,0) = x g(x) and ∫_0^1 dx H_g = A_g(0) = ⟨x⟩_g. The 2023 paper uses A_g(0) = 0.414.
   * The 2021 definition (16) gives x g(x)/2, which contradicts its own moment relations (23) and (32).
2. **Spin sum.** Explicit Dirac matrices: (½)Σ|ū(P′)[Hγ^+ + E iσ^{+ν}Δ_ν/2M]u(P)|² = 4P̄^{+2}[(1−ξ²)H² − 2ξ²HE − (ξ²+t/4M²)E²] (relative deviation 5×10⁻¹⁵, 20 random kinematic points).
   * The Gordon identity reduces the C-term to H_2 = A + 4ξ²C, E_2 = B − 4ξ²C (residual 2×10⁻¹²).
   * Hence, with G = ⟨T_g^{++}⟩/(ξ²P̄^{+2}) (no ½), (½)Σ|G|² = **(4/ξ⁴){(1 − t/4M²)E_2² − 2E_2(H_2+E_2) + (1−ξ²)(H_2+E_2)²}**, which is 2023 eq. (5). With the 2021 ½ one gets (26).
3. **Independent normalization test of the amplitude.** At high energy (Im part, H_g(ξ,ξ) ≈ xg(x), x = 2ξ ≈ M_V²/W²), Guo et al. (13)+(17) with the corrected F_g reproduce **exactly** Ryskin's LO formula:
   dσ/dt|₀ = Γ_eeM³π³α_s²[xg]²/(48αQ̄⁸), Q̄² = M²/4 (Z. Phys. C 76 (1997) 231, eq. (2)), with Γ_ee = 16πα²e_Q²|ψ(0)|²/M² (BBL (4.4d), (A34), N_c = 3). The ratio is 1.000.
   With the 2021 normalization the ratio is 0.25. This confirms that the amplitude (13) presupposes the standard (no-trace) F_g, i.e. that the ½ in (16) is spurious.

*Caveats for printing.*
* Eq. (25) is not affected; the error propagates through (24) into (26).
* With metric (+,−,−,−), F^{a+i}F^{a+}{}_{i} read literally (F^{a+ν}g_{νi}) equals −Σ_i(F^{a+i})². The positive contraction that gives x g(x) is F^{a+i}F^{a}{}_{i}{}^{+} = F^{a+μ}F^{a}{}_{μ}{}^{+} (Diehl). The typography of 2021 (16) and 2023 (1) is ambiguous on this point. It affects only the overall sign, not the factor 2.

**Confirmed.**

---------------------------------------------------------------------------------------------------------------------------------

## 8. Required edits to our material

1. YZLIU §4.1 E2 and CLAIMS E08: "[Ji:2021znw] eq. (72)" → "PRD 105 (2022) 076014, eq. (73) (eq. (72) of arXiv:2106.05310v1)". Note that the journal version corrected the CS exponent but not Γ_S^{(2)}.
2. LAMET §10.4(c): add the explicit two-loop mismatch Γ^{(2)}(π/2) − γ_HH^{(2)} = C_FC_A(ζ_3/2 − π²/24)(α_s/π)² (n_f parts equal). Say that ESSZ report JLL's argument, and that PLB 811 p. 5 makes the same remark.
3. LAMET §11 (Jia:2024atq): upgrade *(abstract)* to *(read)*. The correction is a self-correction of Jia:2018qee, for flavour-neutral mesons, at O(N_c⁰), via the Õ_{1/2} term and the higher Fock component (eq. (86)); the term vanishes as P → ∞.
4. YZLIU §3.F1 / §4.1 E5: "propagates to (24)–(26)" → "propagates through (24) into (26) (and the polarized (58)–(59))". Write the contraction as F^{a+μ}F^{a}{}_{μ}{}^{+}.
5. E11: state explicitly that the single-log error is in APPB (81) only. RMP (208) has only the L_b² error.
6. RMP equation numbers (205)–(208) refer to arXiv:2004.03543v2. The journal PDF was not accessible.
