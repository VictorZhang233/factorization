# Verification batch E33–E36, N01–N02 (stage 2, second independent verifier)

Date: 2026-10-11. Stance: I did not rely on the stage-1 reports (`batch_E31_s1.md` §§4–7, `batch_N01_s1.md` §§2–3). I read them
only to see what had already been examined, and then re-did each item by a different route where one existed:
published erratum texts instead of arXiv diffs, a coordinate-space derivation instead of k± residues, exact rational
certificates instead of floating-point optimisation, light-front wave functions instead of a Dirac trace. All literature was
downloaded fresh into my scratch area and treated as untrusted text (nothing from it was executed).

## 0. Method, sources, reproduction

**My scripts** are in `verify/claims/batch_E33_s2_scripts/`, each with a `.log`. Run them with `python3 -I`.

| script | purpose |
|---|---|
| `e33_inspire.py`, `e33_inspire_arxiv.py` | INSPIRE records (publication + erratum entries) for all 18 papers and 3 extra ones |
| `e33_crossref.py` | Crossref DOIs of the paywalled errata |
| `e33_scoap3.py`, `e33_scoap3_plb.py` | download the **published** erratum PDFs (open access, SCOAP3): 9 JHEP errata and 2 PLB corrigenda |
| `e34_helicity_s2.py` | BK vs BER Δγ_GG: exact series, intercept polynomials, x-space double logs |
| `e35_yukawa_s2.py` | Yukawa PDF from light-front wave functions; d-dimensional MS-bar; mpmath roots; bare PDF sign for ε ≷ 0 |
| `n01_wedge_s2.py` | N01 by a coordinate-space (proper-time wedge) route; finite-ε numerics; SU(2,3,4) colour; O(χ²) unitarity |
| `n02_gordan_exact_s2.py` | Gordan alternative with exact rational certificates (610 instances) and a float-LP cross-check |
| `eqcount.py` | equation-number counter for LaTeX sources (used for CRS) |
| `rerun_project_scripts.log` | output of the re-run project scripts (eikonal_box*.py, s2_crs_yukawa_pdf.py, s1_landau_gordan.py) |

**Project scripts re-run** from a scratch copy, all reproduced exactly:
* `refdoc/work_R3/scripts/eikonal_box.py`, `eikonal_box_check.py`, `eikonal_box_closedform.py`: maximum relative deviation 4.67e−16.
* `frontier/others/scripts/s2_crs_yukawa_pdf.py`: 10/10 PASS.
* `frontier/others/scripts/s1_landau_gordan.py`: 10/10 PASS (226 type I, 174 type II).

**Literature read directly.** arXiv sources unless stated otherwise.
* Published erratum PDFs (SCOAP3):
  * JHEP 06 (2024) 143 (DHYZ); JHEP 04 (2024) 097 (Forshaw–Holguin); JHEP 05 (2017) 154 (BNRS); JHEP 08 (2022) 108 (Bertone et al.).
  * JHEP 07 (2023) 096 (Ebert–Gao–Stewart); JHEP 12 (2022) 048 (Rodini–Vladimirov); JHEP 10 (2016) 148 (KPS).
  * JHEP 09 (2024) 052 (CKTT); JHEP 03 (2016) 001 (DOS).
  * PLB 751 (2015) 596 and PLB 771 (2017) 633 (Penin).
* BBL `erratum.tex`, inside hep-ph/9407339v2.
* Becher–Neubert 0901.0722 v1/v2/v3 sources. Collins hep-ph/9709499 v1/v2 sources.
* E34–E36 papers: 2009.06779v2 (LMNW); 2306.09495 (abstract); 0710.4330v1 (BC 2008); **0903.5326 (BC 2009)**; 1309.7644; 1305.1924; 2304.06161v1 (BK); hep-ph/9603204 (BER); 1409.5131 (MVV 2014); 2111.01170v2 (CRS); 2006.07377v2 (CFH); 2308.00025 v2 and v4 (CFGH); 1801.01138v2 (SYZ); 1601.04695v3 (RS); 1405.2080 (Gaunt); 1507.01652 (Zeng); 2607.14259 (Barcaro–Gao–Gaunt 2026).
* N01: hep-th/9602104 (Meggiolaro 1997, "M97"); hep-ph/0602143 (Giordano–Meggiolaro 2006, "GM06"); hep-ph/9409446 (Korchemskaya–Korchemsky 1995).
* N02: 2007.04085v1 (Collins); 2609.18668, 2407.13738, 2407.17158, 2603.05444, 2204.02988 (searched for theorems of the alternative); Crossref record of Gordan 1873.

**Not accessible** (no circumvention attempted):
* Bodwin PRD 34 (1986) 3932 (APS).
* Collins–Soper NPB 213 (1983) 545 (Elsevier).
* Henneaux PLB 316 (1993) 633 (Elsevier; the landing page carries a TDM reservation).
* Kramer–Lampe ZPC 42 (1989) 504 (Springer).
* FRS NPB 139 (1978) 545 (Elsevier).
* The APS text of the Collins 1998 and Becher–Neubert 2009 errata. Their arXiv revisions were read instead.

## 1. Summary

| id | verdict | main point |
|---|---|---|
| E33 | **confirmed** | All 18 erratum records exist exactly as listed (INSPIRE, my own queries). I read the contents of 13: the published texts for 10, the arXiv-hosted erratum or revisions for 3. Two consequences for our material: (a) the DHYZ conclusion is reversed at cross-section level; (b) Penin's asymptotic claim is withdrawn by his second corrigendum. Minor ones: the BN eq. (12) term and the dipole formula numbered eq. (7); BNRS (5.11) sign. Three further errata in our material are missing from the list. |
| E34 | **refuted as stated** | (i), (ii) and (iv) are accurate. **(iii) is no longer a disagreement.** Balitsky–Chirilli themselves (NPB 822 (2009) 45, Sec. 6, "In QCD") trace the ζ(3) mismatch to an erroneous evaluation of an integral that was assumed to vanish. After correction "the disagreement disappears". OTHERS §9.2's attribution to longitudinal cutoffs is superseded. |
| E35 | **confirmed** (numerical interval corrected) | At μ = 0.8 GeV, f < 0 for ξ ∈ (0.2640, 1), not "[0.28, 0.98]". μ_* = 1.6988 GeV. The CFH step and CRS eqs. (55)–(59) are located. The bare PDF is negative for ε < 0, as CRS state. |
| E36 | **confirmed** (wording refined) | SYZ disprove the pure-Glauber parts of Gaunt 2014 and RS §11.1 for IR-safe single-scale observables, with an all-order argument that uses CSS q_T factorization as input. Their argument "does not apply to doubly-differential observables, like those studied in [Zeng]". No published rebuttal found. |
| N01 | **confirmed (computation); not new** | Re-derived in coordinate space and checked numerically at finite ε. The result is **Meggiolaro, Z. Phys. C 76 (1997) 523, §3, eqs. (3.23)–(3.26)**; graph by graph in **Giordano–Meggiolaro, PRD 74 (2006) 016003, eq. (4.24)**. The other O(g⁴) graphs are in M97 (3.28)–(3.34). **Drop the marker 「本书新结果（待文献核查）」.** |
| N02 | **confirmed** | The statements match Gordan's alternative exactly. The min-norm margin is proved and is tight. Exact certificates on 610 instances. No prior identification with Collins' Thm 3 was found, but the content is classical, so it should be printed as a short remark. |

---

## 2. E33 — published errata whose content was not examined

### 2.1 Existence and bibliographic data (independent INSPIRE queries; log `e33_inspire*.log`)

Every record carries a `material: erratum` entry with exactly the reference in the claim:
* Bodwin PRD 31 (1985) 2616 → PRD 34 (1986) 3932.
* Collins–Soper NPB 193 (1981) 381 → NPB 213 (1983) 545.
* Collins PRD 57 (1998) 3051 → PRD 61 (2000) 019902.
* BBL PRD 51 (1995) 1125 → PRD 55 (1997) 5853.
* Becher–Neubert PRL 102 (2009) 162001 → PRL 111 (2013) 199905.
* Henneaux PLB 313 (1993) 35 → PLB 316 (1993) 633.
* Ebert–Gao–Stewart JHEP 06 (2022) 007 → JHEP 07 (2023) 096.
* Rodini–Vladimirov JHEP 08 (2022) 031 → JHEP 12 (2022) 048.
* KPS JHEP 01 (2016) 072 → JHEP 10 (2016) 148.
* Cougoulic–Kovchegov–Tarasov–Tawabutr JHEP 07 (2022) 095 → JHEP 09 (2024) 052.
* Dixon–Herrmann–Yan–Zhu JHEP 05 (2020) 135 → JHEP 06 (2024) 143.
* Forshaw–Holguin JHEP 12 (2021) 084 → JHEP 04 (2024) 097.
* Becher–Neubert–Rothen–Shao JHEP 11 (2016) 019 → JHEP 05 (2017) 154.
* Bertone–Cacciari–Frixione–Stagnitto JHEP 03 (2020) 135 → JHEP 08 (2022) 108.
* Diehl–Ostermeier–Schäfer JHEP 03 (2012) 089 → JHEP 03 (2016) 001.
* Kramer–Lampe ZPC 34 (1987) 497 → ZPC 42 (1989) 504.
* Penin PLB 745 (2015) 69 → PLB 751 (2015) 596 and PLB 771 (2017) 633.
* **Floratos et al.** = Floratos–Ross–Sachrajda NPB 129 (1977) 66 → NPB 139 (1978) 545. This is how `research/survey/SURVEY.md` and `refs.bib` cite it. FRS NPB 152 (1979) 493 has **no** erratum record.

**Errata in our material that are missing from the list** (also verified on INSPIRE):
* Erdoğan PRD 89 (2014) 085016 → PRD 90 (2014) 089902 (arXiv v2: "Figure 6 corrected").
* Surguladze–Samuel PRL 66 (1991) 560 → ibid. 2416.
* Buffing–Diehl–Kasemets JHEP 01 (2018) 044 → JHEP 07 (2021) 046. INSPIRE files this as a second publication entry titled "Erratum to: …". arXiv v3: "added erratum (main body of paper unchanged)".

### 2.2 Contents (read in the published erratum unless stated)

| paper | erratum content | effect on our material |
|---|---|---|
| **DHYZ** (JHEP 06 (2024) 143, published text) | "A normalization factor ξ_ε = 1+ε²ζ₂ was mistakenly omitted". Eqs. (3.12), (3.16), (4.19), (4.21) are corrected. The strict-collinear-breaking tripole contribution (4.27) to the splitting amplitude is corrected: 15ζ₄, iπ³/6, 8π/3·arg³ … (v1 had 30ζ₄, iπ³/3). Cross-section-level (4.30): "for a purely QCD process, the contributions that break factorization at the cross-section level now completely cancel, as indicated by the zero in the first line. (The second line cancels after summing over colors.)" arXiv v2 abstract: "…potentially dangerous factorization-violating terms can arise, **but they cancel after summing over colors**". arXiv comment: "important correction to eq. (3.12), leading to cancellation of potential factorization-violating terms in the cross section, eq. (4.30)". | **OTHERS §4.3 quotes the v1 abstract verbatim (checked) and must be corrected.** Amplitude-level breaking (4.27) survives with corrected coefficients. The cross-section-level effect cancels. `spec_v2` `rem:front-glauber-status` already says this, tagged [PENDING-VERIFY: E33]. That statement is confirmed. |
| **Penin** (PLB 751 (2015) 596; PLB 771 (2017) 633, published texts) | First corrigendum: a sign misprint in eq. (7), φ_c; the double-log contribution of Fig. 2(d) was missing; new coefficients of series (9); f(∞) = 1.33496, an enhancement "not as significant as it was suggested". Second corrigendum: Fig. 2(e) was also missing; new Table 1; f(x) = −3F₁⁽¹⁾ rises to a maximum 0.881566 at x = 2.60904 and then **decays exponentially**, f ~ e^{−x/2+2 ln x}; "the double logarithmic result is not a valid approximation anymore". Both say "main conclusions unchanged". | Cite with both corrigenda. **Never quote the v1 high-energy enhancement.** The `spec_v2` use, "three loops `Penin:2014msa`, …, as quoted in `Liu:2019oav`", is faithful: Liu–Neubert 2020 cite it among works "validating [the conventional approach] up to three-loop order". |
| **Becher–Neubert 2009** (arXiv v3, "additional term in (12)"; v2 = journal) | Eq. (12), H^{(2)}_{R.S.} (needed for ≥ 4 partons), gains −(if^{abc}/32ε)Σ_{(i,j,k)}T_i^aT_j^bT_k^c(γ₀^i/C_i − γ₀^j/C_j)·ln(−s_ij/−s_jk)·ln(−s_ki/−s_ij) (diffed v2 vs v3). | Not used by us. Side finding confirmed: the dipole formula is **eq. (7)** (`\label{magic}`) in v1, v2 and v3. In v2/v3 it is Σ_{(i,j)} (T_i·T_j/2) γ_cusp ln(μ²/−s_ij) + Σ_i γ^i, with Σ_{(i,j)}T_i·T_j = −ΣC_i (ordered pairs). `VERIFIED_FORMULAS_v2` VF-SUD-5 and `FINAL_OUTLINE_v2` (line ~1050) cite "eq. (2)", which is Catani's I^{(1)}, I^{(2)} display: **change to eq. (7).** |
| **BNRS 2016** (JHEP 05 (2017) 154, published text) | Eqs. (5.6), (5.7) "were missing a sign from the sum over gluon polarizations"; the sign of the anomalous dimension (5.11) changes: V_m = 2Σ_{(ij)}(T_{i,L}·T_{j,L}+T_{i,R}·T_{j,R})∫dΩ/(4π) W_ij^k[Θ_in^{nn̄}+Θ_out^{nn̄}], R_m = −4Σ_{(ij)}T_{i,L}·T_{j,R}W_ij^{m+1}Θ_in^{nn̄}(n_{m+1}). S₂^{(n)} in (5.17) must be multiplied by 1/n!. | §2 (factorization formula, RGEs), which is what VF-FRO-14 and OTHERS §11.1 use, is unaffected. Use these signs if V_m and R_m are printed. |
| **Forshaw–Holguin** (JHEP 04 (2024) 097, published text) | Paragraph of eq. (3.3) replaced. Scalar-sum p_T of W/Z/H: leading CVL α_s⁵L²(ln w)⁴, with "no reason to anticipate a cancellation". Vector-sum p_T: "the seminal CSS proof … indicates that no CVL will be present … the complete momentum conserving delta function forces ln w = 0". Added to the conclusions: CVLs less enhanced than α_sⁿL^{2n−4} carry an O(1) factor that may vanish, and does vanish for the W, Z, H p_T distributions. | OTHERS §4.4 ("almost all") is compatible. Never cite FH for coherence violation in the DY/W/Z q_T spectrum. |
| **Bertone et al.** (JHEP 08 (2022) 108) | (C.18)–(C.20) must be multiplied by 2!, 2!, 3! (normalisation mismatch); "do not affect any of the results". | Abstract level only. |
| **Ebert–Gao–Stewart** (JHEP 07 (2023) 096) | Factors of 2 in the intermediate eqs. (4.56), (4.61), (4.66), (4.76) ("do not affect the final results"). Notation valid for a **complex** C^{(1)}; a footnote and a sentence about reality and hermiticity are removed. | Any printed NLP hard coefficient must allow complex C^{(1)}. |
| **Rodini–Vladimirov 2022** (JHEP 12 (2022) 048) | Sign of λ in (4.6); R = exp(+2D ln δ + B), so the sign of ∂_μD flips in (5.10) and (5.12); factor (−i) on the right-hand sides of (5.15), (5.18)–(5.20); explicit zeroth-moment decomposition. "Do not alter the conclusions". | Abstract level only. |
| **KPS 2016** (JHEP 10 (2016) 148) | Corrected large-N_c (and N_c&N_f) helicity evolution: the first two coefficients of eq. (5.35) doubled (polarized gluon emission by a gluon is 4× that by a quark at large N_c); figures corrected. | Literature level only. The later intercepts (2.31, then 3.66) use corrected or revised equations. |
| **CKTT 2022** (JHEP 09 (2024) 052) | "several sign changes in the intermediate steps … All the final results remain unchanged". | None. |
| **DOS 2012** (JHEP 03 (2016) 001) | (3.41)–(3.42): v⁺v⁻ → v⁺w⁻. (4.25): factor ½ instead of 2. (5.75): drop (2π)² on both sides. (5.78): kernel δ^{ll'}[u²+(1−u)²−ε](1−ε) in 4−2ε dimensions. | Abstract level and DGOPS pointers only. |
| **BBL 1995** (`erratum.tex` in hep-ph/9407339v2) | Velocity scaling: "amplitude of order vⁿ" → "probability of order v²ⁿ"; odd powers of v allowed. Spin-flip |QQ̄g⟩ states have probability ~v³ (soft gluons multipole-suppressed). Error estimates O(v⁴Γ)→O(v³Γ) in (3.1), (4.1a,b), (4.3a,b); O(v³σ) in (6.8a,b), (6.9a,b). Typos: (3.19a,b) prefactor √(3N_c/2π); (5.4) last colour matrix T^a_{i'j'}; (5.5) second coefficient 4/(N_c²−1); (A16), (A25) α_s(2M). | Our VF-NRQ items (velocity rules of Table I, Im f's, decay formula) are unaffected. No BBL error estimate is quoted; if one is, use v³. |
| **Collins 1998** (arXiv v2 vs v1) | Text identical apart from the date. `region.eps` (Fig. 1, leading regions) and `soft1aj.eps` were redrawn. The new region.eps adds three arrowed final-state lines from the target-collinear subgraph. | Region diagrams after Collins' Fig. 1 must show the extra target-collinear lines. Text quotes are unaffected. |
| Bodwin 1986, Collins–Soper 1983, Henneaux 1993, Kramer–Lampe 1989, FRS 1978 | **not examined** (paywalled) | Cite with the erratum. Quote no formula from these papers that is not checked elsewhere. For Henneaux's theorem, cite Barnich–Brandt–Henneaux, Phys. Rept. 338 (2000) 439 for the statement. |

**Verdict E33: confirmed.** The errata exist as stated, and the rule "use the corrected version" is right. The concrete
corrections it implies are listed above. The DHYZ and Penin items change statements we would otherwise print.

---

## 3. E34 — reported disagreements

**(i) LMNW, JHEP 01 (2021) 077 (2009.06779v2): accurate.**
* Abstract: "predict the large logarithms of order αα_s²L^k in the three-loop decay amplitude, L = ln(−M_h²/m_b²), k = 6,5,4,3 … perfect agreement with existing numerical results … and analytical results for the three-loop contributions involving a massless quark loop … we disagree with the results of previous attempts to predict the series of subleading logarithms ~αα_s^nL^{2n+1}".
* Body: "α_b = e_b²α"; the earlier predictions are "[AWY 2001, Anastasiou–Penin 2020], which were based on conventional resummation techniques". So "O(α_bα_s²L^k)" is the paper's own notation.
* I re-expanded both NLL formulas, AWY's (`\label{Akhoury}`) and LMNW's resummed NLL formula, to O(α_s²) by hand. The result, in units C_F(α_s/4π)²:
  * LMNW: (C_F/90)L⁶ + (−3C_F/20 − β₀/30)L⁵.
  * AWY: (C_F/90)L⁶ + (−C_F/10 − β₀/30)L⁵.
* The disagreement is therefore in the NLL (k = 5) C_F² term. The leading double logs agree. For gg→h the colour structures differ:
  * LMNW: (C_A−C_F)(11C_A/9 − C_F − 10T_Fn_b/3)/640.
  * AP: (C_A−C_F)(11C_A/9 − 3C_F/2 − 2T_Fn_b)/640.
  * Both equal 0.0017361 for SU(3) with n_b = 1. LMNW report that Czakon–Niggetiedt confirmed theirs by private communication.

**(ii) Rodini–Vladimirov, PRD 110 (2024) 034009 (2306.09495): accurate.** Abstract: "We found several differences with earlier derivations,
which are due to accounting for nontrivial kinematics of the quark-gluon interference terms".

**(iii) Balitsky–Chirilli, PRD 77 (2008) 014019: accurate as a quotation of the 2008 paper, but retracted by its authors.**
* 0710.4330v1 (the only arXiv version; INSPIRE gives PRD 77 (2008) 014019):
  * Sec. VI: the eigenvalue "coincides … up to the extra term 2ζ(3)", i.e. an extra (α_s²N_c²/4π²)ζ(3)Tr U_xU_y†.
  * Sec. VIII: "agrees with the forward NLO BFKL kernel up to a term proportional α_s²ζ(3) times the original dipole. We think that the difference could be due to different definitions of the cutoff in the longitudinal momenta".
* **But** Balitsky–Chirilli, "NLO evolution of color dipoles in N=4 SYM", NPB 822 (2009) 45 [0903.5326], Sec. 6 ("Evolution equation in the fundamental representation"), subsection "In QCD", last paragraph before the Conclusion, says: "It should be also mentioned that the statement in our previous paper [PRD 77, 014019 (2008)] that our equation (gluonfund) disagrees with NLO BFKL was due to erroneous calculation of the integral (nashel) which was assumed to be zero. After taking into account the δ-function contributions in the r.h.s. of eq. (nashel) the disagreement disappears."
* The appendix formula (nashel) = 4ζ(3)[δ(z₂₃) − δ(z₁₃)] carries the missed ζ(3) δ-terms.
* Hence:
  * (iii) must **not** be printed as a disagreement;
  * OTHERS §9.2 ("…up to a term ∝ α_s²ζ(3)×(the original dipole), attributed to different longitudinal cutoffs") must be corrected;
  * the stage-1 suggestion "BC traced the ζ(3) mismatch to the cutoff" is wrong.
* (The composite-conformal-dipole agreement in BC 2009 and 1309.7644 is a separate, N = 4 SYM statement.)

**(iv) Borden–Kovchegov, PRD 108 (2023) 014001 (2304.06161) vs BER: accurate; open.**
* BK eq. (anomalous_dim): Δγ_GG = (ω/2)[1 − √(1 − (16ā/ω²)√(1−4ā/ω²))], ā = α_sN_c/2π.
* BK eq. (anom_BER), BER pure glue at large N_c: (ω/2)[1 − √(1 − (16ā/ω²)(1−3ā/ω²)/(1−ā/ω²))].
* My exact expansion (`e34_helicity_s2.log`), coefficients of ā^k/ω^{2k−1}:

  | k | 1 | 2 | 3 | 4 | 5 |
  |---|---|---|---|---|---|
  | BK | 4 | 8 | 56 | **496** | 4824 |
  | BER | 4 | 8 | 56 | **504** | 4920 |

* Independent three-loop anchor: in x space, k = 3 gives a_s³(56/3)N_c³ ln⁴x (a_s = α_s/4π). This is exactly the C_A³ term of MVV 2014 (NPB 889 (2014) 351, eq. Dgg-exact): D_gg^{(0)} = 56/3·C_A³ + …, where ΔP_gg^{(2)} = D_gg^{(0)} ln⁴x + ….
* Intercepts:
  * BK: √u with u³ − 256u + 1024 = 0, i.e. 3.6607440452√ā = (4/3^{1/3})√Re[(−9+i√111)^{1/3}].
  * BER: √u with u² − 17u + 48 = 0, i.e. √((17+√97)/2) = 3.6639362578√ā. The difference is 0.087%.
* Attribution: BER (Z. Phys. C72 (1996) 627) print only "z_s = 3.45 (n_f = 4) (the pure gluonic case would have given z = 3.66)". The value 3.66394 is BK's analytic evaluation of BER's equations.
* Status 2026:
  * Borden–Kovchegov PRD 113 (2026) 034002 (abstract): "very slight disagreement" persists with BER, Blümlein–Vogt and Boussarie et al.
  * Ermolaev, Phys. Atom. Nucl. 87 (2024) 244: "confirmed, except for a very small discrepancy".
  * No four-loop fixed-order result was found among the 43 INSPIRE citers.
  * Print no verdict.

**Verdict E34: refuted as stated**, because (iii) presents a disagreement that its own authors withdrew. The corrected
statement (with (i), (ii) and (iv) confirmed) is given in the structured output.

---

## 4. E35 — MS-bar positivity; the Yukawa counterexample

* **The CFH step** (2006.07377v2 = JHEP 11 (2020) 129). Sec. 2, right after the operator definition (JHEP eq. (2.2)), reads: "It can be shown (see e.g. Sect. 6.7 of [Collins 2011]) that the expression Eq. (2) is a number density, and as such before subtraction of divergences it is positive." It is used in §3.1.1 (nonsinglet toy model) and §3.1.2 (POS scheme): "because the bare PDF of Eq. (2) is a probability density, the three factors … are all separately positive when ε → 0⁻".
* **CRS** (2111.01170v2 = PRD 105 (2022) 076010).
  * Abstract: CFH's derivation's "primary failure is in the apparently uncontroversial statement that bare pdfs are always positive".
  * Sections: VI "Failure of an argument for positivity of MS-bar pdfs"; VIII "Examples", with A "Calculation of pdf" and B "Systematics of why the pdf becomes negative".
  * My equation count of the source: (55) f = a_λ(μ)(1−ξ)[(m_q+ξm_p)²/Δ + ln(μ²/Δ) − 1] + O(a_λ²), with a_λ = λ²/(16π²); (56) Δ(ξ) = ξm_s² + (1−ξ)m_q² − ξ(1−ξ)m_p²; (57) counterterm −a_λ(1−ξ)S_ε/ε; (58) the DR k_T integral; (59) the cutoff form.
* **Independent derivation** (`e35_yukawa_s2.py`). I used light-front wave functions instead of a trace: ψ_{+1/2} = (M+m/x)φ, ψ_{−1/2} = −(k¹+ik²)/x·φ, φ = g/√(1−x)/(M² − (k²+m²)/x − (k²+λ_s²)/(1−x)).
  * Then Σ|ψ|² = g²(1−x)[k² + (m+xM)²]/(k²+Δ)², with exactly CRS's Δ (sympy).
  * The d = 2−2ε master integrals give the pole 1 and the MS-bar finite part ln(μ²/Δ) − 1 + A/Δ, with A = (m+xM)².
  * The normalisation is a_λ = g²/(16π²). This reproduces CRS (55)–(57).
* **The failure, explicitly.** The bare one-loop bracket in DR at ξ = 0.5, μ = 0.8 GeV is +99.3 (ε = 0.01) and +19.4 (ε = 0.05), but **−100.7 (ε = −0.01)** and −20.7 (ε = −0.05). So the bare PDF is negative in the ε < 0 regime that CFH use.
* **Numbers** (masses 0.3/1.0/1.5 GeV, mpmath at 30 digits).
  * The threshold μ₀(ξ) = √Δ·exp[(1 − A/Δ)/2] is strictly increasing on (0,1), from m_q = 0.3 GeV to μ_* = m_s exp{½[1 − (m_q+m_p)²/m_s²]} = **1.698778651 GeV**.
  * f < 0 exactly for ξ ∈ (ξ_c, 1), with ξ_c = 0.08515, **0.26403**, 0.40875, 0.56737, 0.82287, 0.99208 at μ = 0.5, **0.8**, 1.0, 1.2, 1.5, 1.69 GeV.
  * The claim's "[0.28, 0.98]" is a 0.02-grid artefact of the project script (`linspace(0.02,0.98,49)`): a true but non-sharp subset.
  * f > 0 for all ξ iff μ ≥ μ_*.
  * The cutoff bracket minus the MS-bar bracket is 3.0×10⁻³ at μ = 30 GeV and 2.7×10⁻⁴ at 100 GeV, i.e. O(m²/μ²).
* **CFGH** (2308.00025; v2 ≈ EPJC 84 (2024) 335; v4 2026).
  * "PDFs always turn positive at high enough scale … and, correspondingly, turn negative at a low enough scale, as pointed out in [CRS]. However, the value of this scale is set by non-perturbative physics".
  * "can be very conservatively estimated to be Q² ≳ 5 GeV²". v2 imposes α_s/2π·C_gg < 1 at x = 0.8; v4 does so at x ~ 0.3; both give α_s ≲ 0.2.

**Verdict E35: confirmed**, with the interval replaced by (0.2640, 1). [V] for "positive for all μ" and [P] for "positive above a (non-perturbative) scale" are appropriate.

---

## 5. E36 — Gaunt / Rothstein–Stewart vs Schwartz–Yan–Zhu

* **Gaunt, JHEP 07 (2014) 110**, abstract:
  * "for hadronic transverse energy E_T … the classic CSS argument for the cancellation of Glauber gluons breaks down at the level of two Glauber gluons exchanged between the spectators";
  * "we suggest that this failure … corresponds to a failure of the 'standard' factorisation formula … at leading power";
  * the same is suggested for "MPI sensitive observables", e.g. beam thrust and transverse thrust.
* **RS, JHEP 08 (2016) 025, §11.1** "Spectator-Spectator" (read in the v3 source):
  * Eq. (11.13): the S–S phase cancels when the Δp_⊥ integral is unrestricted ("taken alone it is far from a proof of factorization").
  * Then: "Assuming that the measurement restricts the Δp_⊥ ∼ Q*, then these spectator-spectator scattering Glauber exchange diagrams will not cancel out … spoils the factorization of the perturbative n- and n̄-collinear initial state beam radiation, but only starting at O(α_s⁴)". This is one perturbative Glauber exchange on each side of the cut plus two collinear splittings.
  * It covers beam thrust, transverse thrust and E_T (crediting Gaunt and Zeng), and "applies to any observable where Δp_⊥ is constrained, including … beam thrust without the spin asymmetries".
* **SYZ, PRD 97 (2018) 096017**:
  * Abstract: "for pure Glauber ladder graphs, all amplitude-level factorization violating effects completely cancel at cross section level for any single-scale observable (such as hadronic transverse energy or beam thrust). This result disproves previous claims that these pure Glauber graphs are factorization-violating."
  * The introduction names the claims: "it has been argued in Ref. [Gaunt, RS] that factorization can be violated by diagrams with pure Glauber gluon exchange".
  * §3.2 "All-orders Glauber cancellation" ends with "The same argument holds for any infrared-safe single-scale observable X". The argument uses IR exponentiation of the ladders (inductive proof in an appendix), scale invariance of the 2→2 amplitude, and **CSS q_T factorization as an input**, so it is an all-order argument, [A].
  * Scope: "Our argument does not apply to doubly-differential observables, like those studied in [Zeng]".
  * Corollary: a leading violation needs the Lipatov vertex (real soft radiation).
* **Zeng, JHEP 10 (2015) 189**: a counterexample in QCD with scalar quarks to any factorization with decoupled collinear sectors. It shows a non-zero leading-power longitudinal-spin asymmetry in the beam-thrust distribution from S–S Glauber exchange. It lies outside SYZ's stated scope.
* **Later literature.** Of the 36 INSPIRE citers of SYZ, none rebuts it. Later work adopts the result:
  * Chien–Rahn–Shao 2022 (2205.05104): "for single-scale observables, [SYZ 2017, 2018] demonstrate that pure Glauber exchanges (i.e. without soft emissions off Lipatov vertices) do not lead to factorization violation".
  * Bijl–Niedenzu–Waalewijn 2023 (2307.02521): "for single-scale observables such contributions necessarily involve a Lipatov vertex".
  * Buccioni–Fang–Yan 2026 (2603.27123): "stronger results established for single-scale observables".
  * Only Barcaro–Gao–Gaunt 2026 (2607.14259) list Gaunt 2014 and SYZ 2018 side by side among works where "factorization violation has been established", without addressing the conflict.
  * So "disputed" should be read as "conflicting published claims, with the later SYZ argument unrebutted and adopted by later work".

**Verdict E36: confirmed**, with two wording changes.
* "Gaunt (two S–S Glauber gluons spoil CSS for E_T)" → "the CSS cancellation *argument* breaks down at two S–S Glauber gluons for E_T; LP factorization failure is *suggested*".
* "the claims survive for multi-differential observables" → "SYZ's argument does not apply to doubly-differential observables. There RS's general Δp_⊥-constraint mechanism is not contradicted, and Zeng's model exhibits it. Gaunt's own observables (E_T, beam thrust, transverse thrust) are single-scale and fall inside SYZ's scope."

---

## 6. N01 — two-gluon exchange between infinite time-like Wilson lines

### 6.1 Independent derivation (coordinate space; differs from the k± residue method of the project and of stage 1)

* **Setup.** Normalisation as in `eikonal_box.py`: J_σ = ∫dx_A dx_B [i/(x_A+i0)][i/(σx_B+i0)] g(k), with x_{A,B} = v_{A,B}·k, g = [(k²−a+i0)(k²−b+i0)]⁻¹, dx_A dx_B = sinhY d²k. σ = −1 is the ladder ("box"; same ordering on both lines) and σ = +1 the crossed graph. (In coordinate space the relative proper times give x = v_AΔτ − v_BΔσ, so Δσ > 0 ↔ σ = −1.)
* **Wedge form.** With i/(y+i0) = ∫₀^∞dλ e^{iλy}:
  J_σ = ∫_{W_σ} d²x G(x), W_σ = {λ_Av_A + σλ_Bv_B : λ ≥ 0},
  G(x) = ∫d²k e^{ik·x}g(k) = (−2πi/(a−b))[K₀(√a s) − K₀(√b s)], s = √(−x²+i0).
* **Polar coordinates** in the (λ_A, λ_B) quadrant: x² = r²(1 + σ sin2θ coshY).
  * The radial integral is ∫₀^∞ r e^{−pr}K₀(κr)dr = 1/(κ²−p²) + p ln((p+w)/κ)/w³, w = √(p²−κ²). As p → 0 it tends to 1/κ².
  * This gives **J_σ = −(2πi sinhY/(ab)) ∫₀^{π/2} dθ /(1 + σ coshY sin2θ − i0).**
* **The angular integral:**
  * σ = +1: ∫ = Y/sinhY, so **J_cross = −2πiY/(ab)**.
  * σ = −1: ∫ = (−Y + iπ)/sinhY. The PV gives −Y/sinhY, and the light-cone poles sin2θ = 1/coshY give +iπ/sinhY. So **J_box = (2π/(ab))(π+iY)**.
* **Two corollaries of the wedge picture:**
  * J_cross ∝ Y, because W₊ is the future-cone sector of rapidity width Y.
  * J_box + J_cross = ½∫_{R²}G = ½(2π)²g(0) = 2π²/(ab) (abelian eikonal identity). This follows from the tiling R² = W₊ ∪ W₋ ∪ (−W₊) ∪ (−W₋) and G(−x) = G(x).
  * The i0 consistency of the angular step was checked: the imaginary part of the regulated radial integral converges to −πδ.
* **Numerics** (`n01_wedge_s2.log`). All checks pass:
  * The radial closed form agrees with direct quadrature, including imaginary κ.
  * The angular identities agree to 1e−7.
  * Finite-ε coordinate-space values converge to the closed forms linearly in ε. For (a,b,Y) = (1,2.5,1), the relative deviation is 2.5e−2 → 2.6e−3 → 2.6e−4 for the box, and similarly for the crossed graph and two other parameter sets. Re J_cross → 0.
  * The project's own residue scripts agree to 4.7e−16.
* **Colour.** c_box = X², c_cross = X² + (C_A/2)X. Algebra: T_B^aT_B^b = T_B^bT_B^a + if^{abc}T_B^c and f^{abc}T_A^bT_A^a = −(iC_A/2)T_A^c. Checked with explicit generators for **SU(2), SU(3), SU(4)** in F⊗F, F⊗F̄, A⊗F, A⊗A; maximum deviation 4.4e−16.
* **Sum and phase.** Σ J c = (2π/(ab))[πX² − iY(C_A/2)X]. Hence p_opp = J_cross/(J_box+J_cross) = −iY/π, and Re p_opp = 0.
* **Unitarity.** For random Hermitian X, V = 1 + iχX + ½(iχ)²[X² + p(C_A/2)X] has V†V = 1 + O(χ³) exactly when p = −iY/π (O(χ²) coefficient 0). For p = ½ (the strict window) it is 2.0.
* **Real cuts.** One-gluon emission from straight infinite time-like lines is ∝ δ(v·k) = 0 on shell (v·k ≥ m > 0). Two-gluon emission at O(g²) gives δ(v·(k₁+k₂)) or δ(v_A·k₁)δ(v_B·k₂), both zero. So the first non-zero production amplitude is O(g³), and real cuts start at O(g⁶). Correct.

### 6.2 Literature: the result is known

* **Meggiolaro, Z. Phys. C 76 (1997) 523 [hep-th/9602104], §3 "The case of QCD at order O(g_R⁴)"**, read in the source (equation numbers counted). The setting is two infinite Wilson lines at hyperbolic angle χ, fixed momentum transfer q, gluon mass λ, Feynman gauge.
  * The ladder (Fig. 2b) and cross (Fig. 2c) graphs, eq. (3.23), carry colour factors G₂ = (T^aT^b)⊗(T^aT^b) and, by eq. (3.25), (T^aT^b)(T^bT^a) = G₂ + (N_c/2)G₁.
  * **Eq. (3.26): M^{(G₁)} = i(N_c g⁴/4π) I(t) χ coth²χ, M^{(G₂)} = −½ g⁴ I(t) coth²χ.** Here I(t) = ∫d²k/(2π)²[(k²+λ²)((q−k)²+λ²)]⁻¹ = ∫d²k/(2π)² 1/(ab).
  * The remaining O(g⁴) graphs are eqs. (3.28)–(3.34). Line vertex corrections are a real multiple of the tree after Z_{1W}; the three-gluon graphs vanish, M_{(2,1)} = M_{(1,2)} = 0 (3.32); the self-energy gives −F^{(2)}(t).
  * Regge limit, (3.36): [1 − ᾱ ln s] with ᾱ = (N_c g²/4π)q²I > 0. M97 notes this "is exactly what can be found by applying ordinary perturbation theory" (Cheng–Wu; Lipatov).
* **Giordano–Meggiolaro, PRD 74 (2006) 016003 [hep-ph/0602143], eq. (4.24)** (arXiv numbering, counted): "In Ref. [Meggiolaro97] it was found that M(b) = i(g⁴/2π)I(t)(iπ − |χ|)coth²χ, M(c) = i(g⁴/2π)I(t)|χ|coth²χ, so that M(b)+M(c) = −½g⁴I coth²χ".
* **Comparison.** M(b) = −(g⁴coth²χ/4π²)∫d²k/(2π)² J_box and M(c) = −(g⁴coth²χ/4π²)∫d²k/(2π)² J_cross, with **the same constant** (χ = Y). The ratio M(c)/[M(b)+M(c)] = −iχ/π = p_opp. The N01 formulas are therefore M97's result.
* **Related.** Korchemskaya–Korchemsky NPB 437 (1995) 127 has the same (iπ−γ)coth γ vs γ coth γ structure at the level of the one-loop cross anomalous dimension (F₂(γ) = −F₁(iπ−γ)). RS §9 (crossed Glauber rungs vanish with the η regulator; the non-abelian part of the cross box sits in the soft region) is consistent with N01.
* **Citation hazard** (re-checked). M97 (3.35) prints the bracket [1 − (F^{(2)} + 2N_cB/(4π)² + (N_c/4π)tIχcothχ)g²]. But removing 2Z_W^{(2)} from (3.34) gives [1 + (−F^{(2)} + 2N_cB/(4π)² + (N_c/4π)tIχcothχ)g²], and only this form reproduces (3.36). GM06 (4.15), (4.16), (4.20), (4.21) and (4.27) print the same flipped sign pattern. **Cite M97 (3.26), (3.34), (3.36) and GM06 (4.24); do not cite M97 (3.35) or GM06 (4.15)–(4.21), (4.27).**

**Verdict N01: confirmed (the computation and the conclusions are correct); not a new result.** The marker 「本书新结果（待文献核查）」 must
not be printed. "Other O(g⁴) graphs not covered" can be upgraded by citing M97 (3.28)–(3.34): the other graphs give a real
multiple of the tree (F^{(2)}(t) real for t < 0, B real), so V†V = 1 + O(g⁶) holds for the full eikonal amplitude at O(g⁴).
What stays open is non-eikonal spectators and active partons. The reference-document artefact (strict-window residual) can be
explained in our own words, but no priority can be claimed.

---

## 7. N02 — Collins' Thm 3 = Gordan's alternative

* **Collins, arXiv:2007.04085v1** (the only version; 39 pp.; read in the source).
  * Thm 3 (`thm:main.geom`): "Let V be a real vector space, and let (D₁,…,D_N) be dual vectors on V. Then, there is a direction v for which D_j(v) > 0 for all j, if and only if there is no Landau point for the D_j."
  * Def. (`def:Landau.point`): λ_j ≥ 0, at least one strictly positive, Σλ_jD_j = 0.
  * Footnote: "Undoubtedly the second part of the proof is closely related to the mathematical subjects of which an account is given in books by Gallier … But I have not yet found the result that is needed for the applications treated in this paper."
* **Gordan**, "Ueber die Auflösung linearer Gleichungen mit reellen Coefficienten", Math. Ann. 6 (1873) 23–28, DOI 10.1007/BF01442864 (Crossref verified). The statement is standard in the optimisation literature: exactly one of (a) ∃x ≠ 0, x ≥ 0 with Ax = 0, or (b) ∃y with Aᵀy > 0. I found it in the Springer *Encyclopedia of Optimization* entry on theorems of the alternative and in course material. The coordinate-free version (linear forms f_j on a finite-dimensional real space) is word for word Collins' Thm 3. (I did not see Gordan's original wording.)
* **Proof of the margin.** Fix an inner product (this identifies V* ≅ V). K = conv{D_j} is compact and convex, so its min-norm point w is unique.
  * If w = 0, the convex weights give a Landau point.
  * If w ≠ 0: for u ∈ K and t ∈ (0,1], |w+t(u−w)|² ≥ |w|². Hence ⟨w,u−w⟩ ≥ 0, so **D_j(w♯) ≥ |w|² > 0** for all j.
  * Exclusivity: a good v and a Landau λ would give 0 = Σλ_jD_j(v) > 0.
  * The bound is tight (equality on the supporting face). |w| is the max-margin value max_{|v|≤1} min_j D_j(v).
* **Exact check** (`n02_gordan_exact_s2.log`). 610 integer instances, d = 2–5, N = 2–7, including degenerate ones and a massless self-energy collinear point. The min-norm point was found by exact face enumeration in Fractions and certified by the variational inequality.
  * 456 instances are type I (certificate v = w with D_j·w ≥ |w|² exactly).
  * 154 are type II (exact Landau-point certificate).
  * 0 certificate failures; 0 disagreements with an independent floating-point LP classification. The minimum margin deficit is exactly 0, as expected for tightness.
* **Prior identification: none found.**
  * INSPIRE full-text queries returned nothing relevant: "Gordan" & "Landau singularit"; "Gordan's theorem" & "Feynman"; "theorem(s) of the alternative" & "Landau"/"Feynman integral"; "Farkas" & "pinch singular"; "Stiemke" & "Landau".
  * Grepping the sources of 2407.13738, 2407.17158, 2603.05444 and 2204.02988 gave 0 hits.
  * A web search found nothing either.
  * Near miss: Ríos-Sánchez–Rodrigo 2026 (2609.18668) use **Farkas' lemma** for cyclic and acyclic graph orientations in LTD geometry, not for Collins' theorem.
  * The equivalent "dual cone / 0 ∉ conv" statement is standard in microlocal analysis (wave-front-set product conditions), so the identification is elementary.

**Verdict N02: confirmed.** Print it as a short remark ("Collins' Thm 3 is Gordan's theorem of the alternative (1873); a
constructive good direction is the min-norm point of conv{D_j}, with margin |w|²"). Say "exactly one of", and say that an inner
product identifies V* with V. Do not present it as a significant new result.

---

## 8. Side findings for the integrator

1. **OTHERS §4.3**: replace the DHYZ v1-abstract quote. Cross-section-level factorization-violating terms from the two-loop soft-collinear limit cancel (corrected (4.30)). The amplitude-level tripole term (4.27) remains, with corrected coefficients.
2. **OTHERS §9.2 and every printed version of E34(iii)**: the BC 2008 ζ(3) mismatch was withdrawn by BC 2009 (NPB 822, 45, Sec. 6). Do not print it as a disagreement and do not attribute it to cutoffs.
3. **VF-SUD-5 / thm:sudakov-ir-poles**: Becher–Neubert's dipole formula is eq. (7), not (2).
4. **OTHERS §7 / E35**: "ξ ∈ [0.28, 0.98]" → "ξ ∈ (0.2640, 1)" at μ = 0.8 GeV.
5. **N01**: drop the 「本书新结果」 marker. Cite M97 (3.23)–(3.26), (3.28)–(3.34), (3.36) and GM06 (4.24). Avoid M97 (3.35) and GM06 (4.15)–(4.21), (4.27), which have flipped signs.
6. **Penin 2015**: cite with both corrigenda. The original high-energy enhancement is withdrawn.
7. **Missing errata** to add to the bibliography: Erdoğan 2014 [PRD 90 089902]; Surguladze–Samuel 1991 [PRL 66 2416]; Buffing–Diehl–Kasemets 2018 [JHEP 07 (2021) 046].
