# Verification batch E19–E24 (stage 1, independent verifier)

Date: 2026-10-10. Default stance: skeptical. Claims E19–E24 come from `research/c_glauber/DERIVATION.md` §0.3,
`research/c_exclusive/DERIVATION.md` §0, §7, §8, §10, `research/c_scet/DERIVATION.md` §3.1, §6 items 10 and 13, and
`spec/VERIFIED_FORMULAS.md` (VF-EXC-8, VF-CONV-23, VF-SCET-16; in spec v2 also VF-REF-15, VF-SCET-9).

## 0. Method and sources

* **Primary literature was downloaded again, independently of the project copies.** The downloads are untrusted data and were read as text only
  (LaTeX sources and `pdftotext`; the equations that matter were also looked at as rendered pages).
  * arXiv sources and PDFs: Ji hep-ph/9603249 (v1, the only version); Ji hep-ph/9609381 (v3); Vanderhaeghen–Guichon–Guidal (VGG)
    hep-ph/9905372 (v1, the only version); Mankiewicz–Piller (MP) hep-ph/9905287 (v1, the only version); Collins–Diehl (CD) hep-ph/9907498
    (v1, the only version); Hoodbhoy–Lu (HL) hep-ph/9902286 (v2); Hoodbhoy hep-ph/0108214; Diehl–Gousset–Pire (DGP) hep-ph/9808479;
    Becher–Schwartz (BS) 0803.0342 (**v1 and v2**); Becher–Neubert hep-ph/0603140; Becher–Neubert–Pecjak (BNP) hep-ph/0607228;
    Korchemsky–Marchesini (KM) hep-ph/9210281; Moch–Vermaseren–Vogt (MVV) hep-ph/0403192; Diehl's review hep-ph/0307382.
  * **Journal version of BS:** JHEP 07 (2008) 034 is a free article on IOPscience. I read the PDF (pages 5 and 29 rendered).
  * **Collins' own errata list** ("Errata and updates for 'Foundations of Perturbative QCD'", version of 22 May 2026,
    https://www.cantab.net/users/johncollins/qcdbook/qcd-errata.pdf), read in full (10 pages).
  * **Not accessible:** the published PRL 78 (1997) 610 (APS bot wall; Semantic Scholar and OpenAlex list only the arXiv copy as open access);
    PRD 61 (2000) 074013 (MP) and PRD 61 (2000) 114015 (CD) journal PDFs; Korchemsky–Radyushkin NPB 283 (1987) 342 (Elsevier, 403).
    For KR 1987 I used KM 1993, which quotes the KR two-loop result with an explicit citation, plus BNP 2006 and MVV 2004.
* INSPIRE API: bibliographic data, erratum records, and full-text searches `refersto:recid:… and fulltext:typo|misprint|…` for earlier reports.
* My own scripts are in `verify/claims/batch_E19_s1_scripts/` and use no project code (run with `python3 -I`; logs `*.log` next to them):
  `e20_dvcs.py` (17/17 PASS), `e21_mp.py` (11/11), `e22_dirac.py` (6/6), `e23_cusp.py` (13/13), `e24_jet.py` (10/10).
  The project scripts named in the recipes were also re-run: `research/c_exclusive/scripts/s7_dvcs.py` (17/17 PASS),
  `research/c_exclusive/scripts/s8_meson.py` (11/11 PASS), `research/c_scet/scripts/s1_scet_algebra.py` (52 PASS, 0 FAIL).

## 1. Summary

| id | verdict | what must change before printing | already in the literature? |
|---|---|---|---|
| E19 | **confirmed (as a withdrawal: print nothing)** | Nothing to print. The only Collins-2011 corrections in our material (Fig. 7.10; eqs. (11.4)–(11.6)) are in the author's own errata, Sec. 3. The cross-reference "(E28)" in CLAIMS.md §E19 should read "(E27)". | n/a. The author's errata list also has sign corrections in Ch. 14 ((14.30); l̂→l̃ in (14.22), (14.23), (14.27)). Cite them only as the author's errata. |
| E20 | **confirmed** | Cite as arXiv:hep-ph/9603249v1 eq. (15). The +iε is in the 2nd denominator of **both** brackets (vector and axial). State the conventions (T^{μν}, ε^{0123}, ε⊥, F, F̃) with the corrected formula. | The correct −iε is in Ji's own PRD 55 (1997) 7114, eq. (4) of hep-ph/9609381v3, and in VGG 1999 eq. (38). No explicit erratum or remark found. |
| E21 | **confirmed** | Refer to arXiv:hep-ph/9905287v1, the text after eq. (10). The journal text was not accessible. Also do not quote MP's inference "I₁/I₂ close to one", which rests on 12:9. With eq. (10) as printed the ratio of the divergent coefficients is exactly 2 for every DA. | Not found. INSPIRE full text: 0 hits for refersto MP ∧ (misprint, "9/tau", "12/tau"). The 2 "typo" hits concern other papers. |
| E22 | **refuted as phrased** (wrong photon polarization). The corrected statement below is verified. | The NLO calculation criticized by CD is Hoodbhoy–Lu, hep-ph/9902286 (unpublished). It concerns **γ\*_L N → V_T N**: HL write γ\*(q,e_L), and CD speak of "transversely polarized vector mesons by longitudinally polarized virtual photons". It is not γ\*_T → V_T. | **Yes, retracted by the author:** Hoodbhoy, PRD 65 (2002) 077501 [hep-ph/0108214] redid the one-loop calculation with the subtractions and found zero ("confirms the all-orders proof by Collins and Diehl"). |
| E23 | **confirmed** | The misprint is also in the **journal** version: JHEP 07 (2008) 034, eq. (A.10), p. 29, besides arXiv v1 and v2. | The correct Γ₁ is standard: KM 1993 quoting KR 1987; BNP 2006 (BS's own ref. [24]); MVV 2004 eq. (3.11). The misprint itself was not found reported. INSPIRE full text, refersto BS ∧ typo (11 hits) / misprint (4 hits): I read the 7 most relevant, and none concerns it. |
| E24 | **confirmed** | It is eq. (2.6) of JHEP 07 (2008) 034 (p. 5), identical in arXiv v1 and v2. For a normalized operator definition cite Becher–Neubert PLB 637 (2006) 251, eqs. (3) and (6) [hep-ph/0603140] (BS's ref. [23]), or use the cut definition (verified). | Not found as a reported erratum. The properly normalized form is in BN 2006. |

## 2. E19 — withdrawn Collins-2011 sign-misprint claim

What I checked:
1. `research/c_glauber/DERIVATION.md` §0.3 records the withdrawal verbatim: "An earlier (interrupted) draft of `unitarity_cuts.py` claimed a sign
   misprint in a specific equation of Collins (2011); this could not be verified and has been **withdrawn**." The current
   `research/c_glauber/scripts/unitarity_cuts.py` contains no such claim. It states instead that "the exact equations there were NOT available to us, so no equation
   number is quoted". The c_glauber logs and tex files contain no misprint claim about Collins 2011. The only "typo" in c_glauber is E18
   (Collins arXiv:0708.4410, not the book).
2. I searched the whole work directory (`*.md, *.tex, *.py, *.tsv, *.json, *.txt`) for Collins + misprint, typo, errat*, sign error, wrong, 勘误, 笔误, 印刷错误.
   The only assertions that something in Collins (2011) is printed wrongly are:
   * Fig. 7.10 (Wilson-line vertices): `research/c_wilson/DERIVATION.md` l. 198, 559; `research/c_wilson/tex/c_wilson_rules.tex` l. 162;
   * eqs. (11.4)–(11.6) (Grammer–Yennie, indices interchanged): `research/c_wilson/DERIVATION.md` §6.2, `tex/c_wilson_gy.tex` l. 22;
     `spec/FINAL_OUTLINE.md` l. 552, 1836; `spec/VERIFIED_FORMULAS.md` l. 598; `spec_v2/VERIFIED_FORMULAS_v2.md` l. 624; REFDOC ERR-M5.
   Everything else is a convention difference (sign of g, Fourier sign), not a misprint claim. Examples: WRITER_SPEC rows 4 and 30; FINAL_OUTLINE l. 837.
   `spec_v2/REFS_NOTES_v2.md` l. 349 lists E19 as "withdrawn — never print".
3. **Collins' errata list was read** (version 22 May 2026). Both items are in its Sec. 3 ("Corrections and updates relative to published paperback edition of
   November 2013"). Fig. 7.10: "there should be a reversal of the sign of the Feynman rule for the gluon-to-Wilson-line coupling to the
   right of the final-state cut in the gluon pdf", followed by the corrected table. P. 402, eqs. (11.4)–(11.6): "subscript Lorentz indices should be replaced by
   superscripts, and vice versa", with K_{μν} = k_μ w_{2ν}/(k·w₂ − i0). So the material asserts no Collins-2011 misprint beyond the author's errata.
   (This also supports E27's identification of the errata.)
4. Side information for the writers, not part of E19:
   * The errata list contains other sign corrections, in particular in the Glauber chapter used by our Ch. 10. Eq. (14.30) (p. 559): "the sign of each
     of the terms should be reversed". In eqs. (14.22), (14.23), (14.27), l̂ → l̃. The withdrawn c_glauber draft may have meant one of these, but the
     equation it named was not recorded, so the two cannot be matched. Any use of Collins Ch. 14 must cite the corrected forms **as the author's errata**,
     which the E19 rule permits.
   * The 2023 OA reissue reproduces the Nov. 2013 printing. Errata from Secs. 1–2 are incorporated; those from **Sec. 3 are not**. This includes Fig. 7.10, (11.4)–(11.6),
     (14.30), (9.41), (9.48a,c), (9.52)–(9.54) and (13.34).
5. Bookkeeping: CLAIMS.md §E19 "How to verify" refers to "(E28)", but the Collins errata claim is E27 (E28 is Sterman–Weinberg).

Verdict: **confirmed** as a withdrawal. Print nothing.

## 3. E20 — Ji PRL 1997 (arXiv v1) eq. (15): iε of the second denominator

### 3.1 What is printed
`spin1.tex` of hep-ph/9603249v1 (lines 382–400). Equation counting from the source gives no. (15), and the arXiv PDF agrees (pdftotext: "(15)"):

  T^{μν} = −½(p^μn^ν + p^νn^μ − g^{μν}) ∫dx [1/(x − ξ/2 + iε) + **1/(x + ξ/2 + iε)**] [H Ū n̸ U + E Ū iσ^{αβ}n_αΔ_β/(2M) U]
           − (i/2) ε^{μναβ} p_α n_β ∫dx [1/(x − ξ/2 + iε) − **1/(x + ξ/2 + iε)**] [H̃ Ū n̸γ₅ U + Ẽ (Δ·n/2M) Ū γ₅ U],

with T^{μν} = i∫d⁴y e^{−iq·y}⟨P′|TJ^ν(y)J^μ(0)|P⟩, ξ = Q²/(2P̄·q), Δ^μ = −ξ(p^μ − …), p·n = 1. So Ji's ξ ≡ ξ_Ji = −Δ^+/P̄^+ = 2ξ_modern.
The +iε occurs in the second denominator of **both** brackets. arXiv has only v1. INSPIRE records no erratum, and the published PRL text could not be accessed.

### 3.2 Independent derivation (`e20_dvcs.py`, explicit Dirac matrices)
* Wick contraction of i∫e^{iq′z}⟨p′|T J^μ(z)J^ν(0)|p⟩ gives an s-channel term with l_s = xP̄ + q̄ = k′+q′ and a u-channel term with l_u = xP̄ − q̄ = k−q′.
  The skewness drops out of the kernels at LO.
* **Feynman propagators:** l_s² + i0 = 2P̄^+q̄^−(x − ξ′ + i0), but **l_u² + i0 = −2P̄^+q̄^−(x + ξ′ − i0)**. So the second denominator carries −i0 (exact symbolic identity in the script).
* **Crossing check:** for the C-even vector kernel g(x) = 1/(x−ξ+iε) + 1/(x+ξ∓iε), crossing antisymmetry g(−x) = −g(x) holds only with −iε. Ji's printed form violates it.
* Result (transverse components, with ε^{0123} = +1, γ₅ = iγ⁰γ¹γ²γ³, n̄ = (1,0,0,1)/√2 along the hadron, n = (1,0,0,−1)/√2, ε⊥^{μν} = ε^{μνρσ}n̄_ρn_σ, ε⊥^{12} = +1;
  all 256 traces Tr(γγγγγ₅) = −4iε checked):
  T^{μν} = +g⊥^{μν}Σe_q²∫dx F^q[1/(x−ξ′+i0) + 1/(x+ξ′−i0)] − iε⊥^{μν}Σe_q²∫dx F̃^q[1/(x−ξ′+i0) − 1/(x+ξ′−i0)].
  This matches the claim (ξ′ = generalized Bjorken variable, = ξ for DVCS). All components with a longitudinal or time index vanish.
* Ji's tensor: p^μn^ν + p^νn^μ − g^{μν} = −g⊥^{μν} (checked), and [HŪn̸U + …] = 2F^q. So Ji's vector term equals ours apart from the iε.
  His axial term equals ours if his ε^{0123} = +1 and his γ₅ matches ours. Caution: Ji's own PRD 55 (1997) 7114, eq. (4), has **+**(i/2)ε^{μναβ}p_αn_β, the opposite of the PRL v1.
  Ji's axial sign must therefore not be copied without fixing conventions.
* **DIS limit with finite iε** (η = 0, ξ′ = x_B = 0.25, model q, q̄): Im T^{11} = 4.311534 at ε = 10⁻³ vs 2πF₁ = 4.311560, with F₁ = ½(q+q̄)
  (relative deviation 6·10⁻⁶). This is consistent with the binding DIS normalization, since Im T = 2πW for W = (1/4π)∫e^{iqz}⟨[J,J]⟩.
  With Ji's +iε in the u-channel instead, Im T^{11} → π(q − q̄)(x_B) (3.6448 vs 3.6406): antiquarks enter with the wrong sign, which violates positivity.
* Project script `s7_dvcs.py` re-run: 17/17 PASS (Im T^{11} = 1.395731 vs 2πF₁ = 1.395547 at ε = 10⁻³).

### 3.3 VGG and later literature
* VGG hep-ph/9905372v1 eq. (38), read in the LaTeX source, lines 593–596. Both brackets have 1/(x−ξ+iε) ± 1/(x+ξ−iε), with ε_{0123} = +1.
  Analytically H^{μν}_{VGG} = −T^{μν}: the vector term because ½(p̃^μn^ν + p̃^νn^μ − g^{μν}) = −½g⊥^{μν}; the axial term because ε^{0123}_{VGG} = −1. This agrees with VF-EXC-9.
* Ji, PRD 55 (1997) 7114 [hep-ph/9609381v3], eq. (4): the same amplitude with **1/(x + ξ/2 − iε)** in both brackets. The author used the correct prescription a few months later,
  without commenting on the PRL. A search for remarks on the PRL iε found none. INSPIRE returns 9 hits for refersto Ji ∧ misprint. The three DVCS-era ones
  (hep-ph/9806305, 9801252, 9704406) were read and concern other misprints. The other six are on unrelated topics (chiral-perturbation-theory GPDs, EMT form factors,
  elastic scattering, reviews) and were not read.

Verdict: **confirmed** for arXiv:hep-ph/9603249v1 eq. (15). The published PRL is unchecked.

## 4. E21 — Mankiewicz–Piller: "12/τ and 9/τ"

### 4.1 What is printed (hep-ph/9905287v1, `rhot7.tex`; numbering checked against the PDF)
* (3) Φ_∥(τ) = ½[τ̄∫₀^τ du φ_∥/ū − τ∫_τ¹ du φ_∥/u];
* (4) g^v = ½[∫₀^τ φ_∥/ū + ∫_τ¹ φ_∥/u];
* (5) g^a = 2[τ̄∫₀^τ φ_∥/ū + τ∫_τ¹ φ_∥/u];
* (10) I₁ = ∫₀¹(dτ/τ)(4g^v − 2Φ_∥/τ + g^a/(2ττ̄)), I₂ = ∫₀¹(dτ/τ)(2g^v + g^a/(2ττ̄)).
* Text after (10), l. 428–435: "For the asymptotic distribution amplitude φ_∥(τ) = 6ττ̄ the integrands in eq.(10) are proportional to 12/τ and 9/τ, respectively.
  One, therefore, might expect that any phenomenological regularization … leads to a ratio I₁/I₂ close to one."

### 4.2 Check (`e21_mp.py`, exact sympy)
* φ_∥ = 6ττ̄ gives g^v = (3/2)(τ²+τ̄²), g^a = 6ττ̄ and Φ_∥ = (3/2)ττ̄(2τ−1). The integrands are **exactly** 12/τ − 21 + 18τ and **6/τ** − 6 + 6τ.
* General DA (Gegenbauer a₂, a₄) in the WW approximation: g^v(0) = ½∫φ/u, and the integrands behave as 8g^v(0)/τ and 4g^v(0)/τ. The ratio is 2 for every DA.
* "9" would need, for example, 4g^v instead of 2g^v in I₂, **or** g^a/(ττ̄) instead of g^a/(2ττ̄). Both give 9. Which is misprinted, the text or eq. (10),
  cannot be decided without redoing MP's calculation.
* The endpoint-suppressed DA 30τ²τ̄² gives 10/τ and 5/τ: the log divergence persists.
* Project script `s8_meson.py` re-run: 11/11 PASS (12 and 6).
* Consequence beyond the claim: MP's next sentence, "I₁/I₂ close to one", rests on 12:9. With eq. (10) as printed the divergent parts are in ratio 2:1.
  That sentence must not be quoted either.

Verdict: **confirmed**. The arXiv v1 is internally inconsistent. Do not quote "9/τ" or the "I₁/I₂ ≈ 1" inference. The journal text was not checked.

## 5. E22 — Collins–Diehl on the NLO "non-zero" result

### 5.1 What CD say (hep-ph/9907498v1, full text read)
* Abstract: "the leading-twist hard-scattering coefficient for the production of a transversely polarized vector meson V vanishes to all orders … a recent
  calculation obtained a non-zero value at NLO. We show that this calculation is incorrect because it failed to include the necessary collinear subtractions."
* Intro: transversity "appears in the factorization formula for production of transversely polarized vector mesons **by longitudinally polarized virtual
  photons**". The criticized paper is ref. [hl] = Hoodbhoy–Lu, hep-ph/9902286.
* Sec. II: tree graphs ∝ ε via γ^λγ^+γ^iγ_λ = −εγ^+γ^i (D = 4−ε). The one-loop 1/ε collinear poles multiply this ε. The correct coefficient
  H₁ = A₁ − H₀⊗f₁⊗φ₀ − H₀⊗f₀⊗φ₁ cancels the finite term.
* Conclusions: "The claim of Hoodbhoy and Lu … fails because the authors omitted to make the collinear subtractions necessary in a correct calculation of a
  hard-scattering coefficient."

### 5.2 What the criticized paper computed
HL (hep-ph/9902286v2; INSPIRE Hoodbhoy:1999ur, never published) state explicitly "γ\*(q,e_L) + N(P,S) → V(K,e_T) + N(P′,S′)", with chiral-odd GPDs
H_T, E_T and the chiral-odd V_T DA, i.e. **γ\*_L → V_T**.

### 5.3 Later literature
* Hoodbhoy, PRD 65 (2002) 077501 [hep-ph/0108214], again for γ\*(q,e_L) → V(K,e_T): "it was pointed out by Collins and Diehl that Hoodbhoy and Lu had
  neglected to subtract the one-loop evolution … the above omission will be rectified … an exact cancellation occurs". The abstract says this "confirms the all-orders proof by Collins and Diehl".
* Diehl's review (Phys. Rept. 388 (2003) 41; arXiv:hep-ph/0307382, selection-rule paragraph on p. 119 of the arXiv PDF): "The hard scattering kernel is however zero, as was explicitly
  checked at leading [MPW 1998] and next-to-leading [Hoodbhoy 2002] order in α_s. It holds in effect to all orders [DGP; CD]."
* DGP 1999 (hep-ph/9808479), Sec. 4: "the above derivation is valid for any spin state of the incoming virtual photon". So the leading-twist V_T
  amplitude also vanishes for γ\*_T. That physics statement is true, but it is **not** what HL computed or what CD attribute to them.

### 5.4 Technical core reproduced (`e22_dirac.py`)
* γ^λγ^+γ^iγ_λ = −(4−D)γ^+γ^i was checked with explicit Clifford algebras in D = 4, 6, 8 and 10. The identity is linear in D, hence it holds for all D. This is CD eq. (1).
* Toy subtraction: A₁ = εb(2/ε + c) → 2b ≠ 0, while H₁ = A₁ − εb·(2/ε) → 0.

Verdict: **refuted as phrased.** The attribution labels the criticized calculation "γ\*_T → V_T", but it is γ\*_L → V_T. Corrected statement (verified):
"Collins and Diehl (PRD 61 (2000) 114015) proved that the leading-twist hard-scattering coefficient for producing a transversely polarized vector meson
(γ\*_L N → V_T N in the CFS factorization, via transversity GPDs and the chiral-odd DA φ_⊥) vanishes to all orders of perturbation theory. They showed that the NLO
calculation of Hoodbhoy and Lu (hep-ph/9902286), which had found a non-zero result, omitted the necessary collinear subtractions. Hoodbhoy (PRD 65 (2002) 077501)
redid the one-loop calculation with the subtractions and found zero. By DGP (PRD 59 (1999) 034023), the same chirality/angular-momentum argument
holds for any photon polarization."

## 6. E23 — Becher–Schwartz App. A: Γ₁

### 6.1 What is printed
* arXiv v1 and v2 (paper.tex l. 1193–1199 in v1, l. 1201–1207 in v2): Γ₁ = 4C_F[C_A(67/9 − π²/3) − (20/9)**C_F**T_Fn_f].
* **JHEP 07 (2008) 034, eq. (A.10), p. 29 (rendered page inspected): the same, with C_F inside the bracket.**
* Normalization: Γ_cusp = Σ_n(α_s/4π)^{n+1}Γ_n, eq. (A.6). Their Γ₂ = −0.7901n_f² − 183.2n_f + 1175 is correct (it matches the analytic three-loop value: −0.7901, −183.19, 1174.90).

### 6.2 Correct value (`e23_cusp.py`)
* KM 1993 [hep-ph/9210281], eq. (cusp), citing KR NPB 283 (1987) 342: Γ_cusp = (α_s/π)C_F + (α_s/π)²C_F[C_A(67/36 − π²/12) − (5/18)N_f].
  Multiplying by 16 gives exactly 4C_F[(67/9 − π²/3)C_A − (20/9)T_Fn_f] at T_F = ½.
* BNP 2006 [hep-ph/0607228] (BS's own ref. [24]) prints Γ₁ = 4C_F[(67/9 − π²/3)C_A − (20/9)T_Fn_f] ≈ 36.8436 (n_f = 5). Reproduced: 36.8436.
  The BS formula would give 26.967.
* MVV 2004 [hep-ph/0403192] eq. (3.11): A₂ = 8C_F[(67/18 − ζ₂)C_A − (5/9)n_f], which is identical.
* **BS's own results need the corrected Γ₁.** I solved the RGEs of H, j̃ and s̃_T (BS App. B: t̃ = H j̃(ln(sQ²/μ²))² s̃_T(ln(sQ/μ)), s = 1/(νe^{γ_E})) to O(a²),
  checking the solution symbolically, and converted exactly from Laplace space to the cumulant via ln^k(νe^{γ_E}) ↔ (−∂_η + γ_E)^k[τ^η/Γ(1+η)].
  The results are G₁₂ = −2C_F, G₁₁ = 3C_F and G₂₃ = C_F(4/3 n_fT_F − 11/3 C_A).
  **G₂₂ = C_F[−(4π²/3)C_F + (11/9)n_fT_F + C_A(−169/36 + π²/3)] equals BS eq. (Gijcoeff) only with the corrected Γ₁.** The printed Γ₁ would add (20/9)C_FT_Fn_f(C_F − 1).
  The D_B n_f-part C_FT_Fn_f[−4ln²τ + (22/9)lnτ + …]/τ (BS App. C; checked by BS against EVENT2) is also reproduced only with the corrected Γ₁.
  So the App. A formula is a transcription misprint; their numerics evidently used the correct value.

Verdict: **confirmed**. Correct: Γ₁ = 4C_F[(67/9 − π²/3)C_A − (20/9)T_Fn_f]. The misprint is in the arXiv versions and in JHEP eq. (A.10).
Not found reported. INSPIRE refersto:780596 ∧ typo gives 11 hits and ∧ misprint 4. I read 0904.1077, 1011.6247, 2311.12768, 2311.07282, 2402.09536, 1804.09146 and 1606.03453;
their typo or misprint remarks concern other papers.

## 7. E24 — Becher–Schwartz jet-function normalization

### 7.1 What is printed
JHEP 07 (2008) 034, eq. (2.6), p. 5 (rendered page inspected), identical in arXiv v1 and v2:
J(p²,μ) = (1/(n̄·p))(1/π) Im[i∫d⁴x e^{−ipx}⟨0|T{χ̄_n(x)(n̸̄/2)χ_n(0)}|0⟩] = δ(p²) + O(α_s).

### 7.2 Check (`e24_jet.py`)
* For free fields: P_n p̸ P̄_n = (n̸/2)n̄·p, exact off shell (20 random momenta). So ⟨Tχ(z)χ̄(0)⟩ has the propagator (n̸/2)i n̄·k/(k²+i0).
* Fermionic T-ordering gives ⟨T χ̄_a(x)Γ_{ab}χ_b(0)⟩ = −Γ_{ab}⟨Tχ_b(0)χ̄_a(x)⟩. The Dirac trace is tr[(n̸̄/2)(n̸/2)] = n·n̄ = 2, and the colour trace gives N_c.
  So i∫e^{−ipx}⟨…⟩ = +2N_c n̄·p/(p²+i0). Since Im 1/(p²+i0) = −πδ(p²) (checked by integration), **J_literal = −2N_c δ(p²)**.
  With the opposite Fourier sign, or without the fermion sign, one gets +2N_c δ(p²). The normalization is off by 2N_c in any reading.
* The required factor is −1/(2N_c): the sign from T-ordering, ½ from the Dirac trace, 1/N_c from colour.
* Becher–Neubert 2006 [hep-ph/0603140] eqs. (3) and (6), BS's ref. [23]: (n̸/2)n̄·p 𝒥 = ∫e^{−ipx}⟨T{𝒳(0)𝒳̄(x)}⟩ and J = (1/π)Im[i𝒥]. This gives +δ(p²), properly normalized.
* The cut definition Σ_X(2π)^Dδ^D(p−p_X)⟨0|χ_n|X⟩⟨X|χ̄_n|0⟩ = 2π(n̸/2)n̄·p J 𝟙_c gives J⁽⁰⁾ = δ(p²), using Σ_s u ū = p̸ and P_n p̸ P̄_n = (n̸/2)n̄·p on shell.
* Project script `s1_scet_algebra.py` re-run: PASS for the same −2N_c statement.

Verdict: **confirmed.**

## 8. Files

* `verify/claims/batch_E19_s1_scripts/e20_dvcs.py`, `e21_mp.py`, `e22_dirac.py`, `e23_cusp.py`, `e24_jet.py` and their `*.log` files.
* Downloads (untrusted, scratchpad only, not in the project): Ji v1 and PRD v3, VGG, MP, CD, HL, Hoodbhoy 2002, DGP, BS v1, v2 and JHEP, BN 2006, BNP 2006, KM 1993, MVV 2004,
  Diehl review, Collins errata PDF.
