# Verification batch E19–E25 (stage 2, second independent verifier)

Date: 2026-10-11. Claims in this stage-2 batch: E19, E20, E21, E23, E24, E25 (E22 was refuted as phrased at stage 1 and is not
re-verified here). Default stance: skeptical; the stage-1 report (`batch_E19_s1.md`, and `batch_E25_s1.md` for E25) was read
only to know *what* had been checked, and every check below was redone with a different method and from independently
downloaded sources.

## 0. Method and sources

**Primary sources, downloaded again in this stage** (scratchpad only, untrusted, read as text; the decisive pages were also
rendered and inspected as images):

* Ji, arXiv:hep-ph/9603249**v1** (the only version; LaTeX `spin1.tex` + PDF) — preprint of PRL 78 (1997) 610.
* Ji, arXiv:hep-ph/9609381 **v1 and v3** (`dvcs.tex` + v3 PDF) — PRD 55 (1997) 7114.
* Vanderhaeghen–Guichon–Guidal, arXiv:hep-ph/9905372 (`paper_web.tex` + PDF) — PRD 60 (1999) 094017.
* Mankiewicz–Piller, arXiv:hep-ph/9905287 (the only version; `rhot7.tex` + PDF) — PRD 61 (2000) 074013.
* Becher–Schwartz, arXiv:0803.0342 **v1 and v2** (`paper.tex`) **and the journal version JHEP 07 (2008) 034** (IOPscience PDF;
  p. 29 = PDF page 31 rendered; p. 5 located).
* Becher–Neubert, arXiv:hep-ph/0603140 (PLB 637 (2006) 251), arXiv:hep-ph/0605050 (PRL 97 (2006) 082001),
  arXiv:0903.1126v5 (JHEP 06 (2009) 081); Moch–Vermaseren–Vogt, arXiv:hep-ph/0403192 (NPB 688 (2004) 101).
* Bauer–Pirjol–Stewart, arXiv:hep-ph/0109045 **v1 and v2** (`bpssoft.tex`; the two versions were diffed).
* Collins, "Errata and updates for 'Foundations of Perturbative QCD'", 22 May 2026, 10 pp.,
  https://www.cantab.net/users/johncollins/qcdbook/qcd-errata.pdf (read in full), and the Open-Access reissue chapter 14
  (Cambridge Core PDF `9781009401838c14_540-572.pdf`; p. 559 rendered).
* Diehl, Phys. Rept. 388 (2003) 41, arXiv:hep-ph/0307382 (relevant paragraphs), and 11 further citing papers scanned for
  remarks (list in §8).

**Not accessible:** the published PRL 78 (1997) 610 (APS returns HTTP 403 to curl and to WebFetch; OpenAlex lists only the arXiv
copy as open access); PRD 61 (2000) 074013 (APS); Korchemsky–Radyushkin NPB 283 (1987) 342 (no scan on INSPIRE).

**Own scripts** (`verify/claims/batch_E19_s2_scripts/`, run with `python3 -I`, logs `*.log` next to them; no project code used):

| script | content | result |
|---|---|---|
| `e19_scan.py` | proximity scan of all 2440 text files of the work dir: Collins-2011 reference ± 3 lines of an error word (EN + ZH) | 210 hits, all inspected (§2) |
| `e19_scan2.py` | complementary scan: Collins + book equation number + error word; every mention of the sign-type errata items | §2 |
| `e19_collins1430.py` | exact check of Collins (14.29) vs printed (14.30) vs the author's erratum, N = 1…4 | PASS |
| `e20_dvcs_s2.py` | (A) exact denominators in Ji's own parametrization; (B) exact tree amplitude on an on-shell quark target with explicit helicity spinors; (C) crossing-symmetric dispersion relation, positivity, finite-η integration | 14/14 PASS |
| `e21_mp_s2.py` | eqs. (3)–(5), (10) of MP evaluated by adaptive quadrature exactly as printed, 1/τ coefficient by Richardson extrapolation, four DAs | 11/11 PASS |
| `e23_cusp_s2.py` | three independent sources converted to one normalization; colour/coupling counting; BS's own Padé numbers | 9/9 PASS |
| `e24_jet_s2.py` | canonical mode expansion of the fermionic T-product, explicit spinor sums (Dirac rep.), explicit time integrals | 13/13 PASS |
| `e25_ghost_s2.py` | exact field-theory counterexample (Gaussian test functions, 4D Minkowski integral); reduced matrix model with finite collinear/usoft transformations, Faddeev–Popov determinant, hand-written Grassmann algebra for BRST | 16/16 PASS |

Sanity re-runs of the project scripts named in the recipes (scratch copies, not independent evidence): `c_exclusive/scripts/s7_dvcs.py`
17/17 PASS, `s8_meson.py` 11/11 PASS, `c_scet/scripts/s1_scet_algebra.py` 52 PASS / 0 FAIL.

**How the methods differ from stage 1.** E20: stage 1 projected light-cone correlators and took traces; here the amplitude is
computed on an on-shell quark target with explicit helicity spinors (no Fierz/trace step), the i0 is derived symbolically in Ji's
own variables, and the physical requirement is tested through the crossing-symmetric dispersion relation. E21: numerical
quadrature instead of exact sympy. E23: different correct-value sources (BN 2009, MVV 2004 read here; KR attribution via BN 2009),
a coupling-counting proof, and BS's own Padé numbers (stage 1 used KM 1993, BNP 2006 and a G₂₂ consistency check). E24:
mode expansion instead of the Feynman propagator. E25: exact action integral on explicit test functions and an algebraic matrix
model (stage 1: random SU(2) jets). E19: proximity scans instead of keyword grep, plus the book page and the errata list read here.

## 1. Summary

| id | verdict | what may be printed (short) | literature |
|---|---|---|---|
| E19 | **confirmed** (as a withdrawal) | Nothing on our own authority. Collins-2011 corrections may be cited only as the author's errata: Fig. 7.10, (11.4)–(11.6) (E27) and, if N19's material is used, **(14.30)**, which is also in the errata (Sec. 3, p. 559 item). | Collins errata list (22 May 2026), Sec. 3 |
| E20 | **confirmed** for arXiv:hep-ph/9603249v1 eq. (15) | Second denominator of **both** brackets must be x + ξ_Ji/2 − iε; corrected formula below, with conventions. Do not attribute to the PRL text (unchecked). | Correct form in Ji's own PRD 55 (1997) 7114 eq. (4) and VGG eq. (38); no erratum or remark found |
| E21 | **confirmed** for arXiv:hep-ph/9905287 | Eq. (10) as printed gives 12/τ and 6/τ (generally 4σ_φ/τ and 2σ_φ/τ = 8g^v(0)/τ, 4g^v(0)/τ), not "12/τ and 9/τ"; do not quote 9/τ (nor the "I₁/I₂ close to one" inference). | Not reported |
| E23 | **confirmed** (arXiv v1, v2 **and** JHEP eq. (A.10), p. 29) | Γ₁ = 4C_F[(67/9 − π²/3)C_A − (20/9)T_F n_f]; the printed inner C_F is spurious. | Correct value: KR 1987 (attr.), MVV 2004, BN 2009; misprint not reported |
| E24 | **confirmed** | BS eq. (2.6) read literally gives −2N_c δ(p²); a factor −1/(2N_c) is implicit; use the cut definition (or BN 2006 eqs. (3), (6)). | Normalized definition in BN 2006; not reported |
| E25 | **confirmed, with one precision** | Ghost term is not collinear-gauge invariant; field-strength term is collinear + usoft invariant; gauge-fixing and ghost terms are each usoft invariant; **only their sum** is BRST invariant. | No published correction |

## 2. E19 — withdrawn Collins-2011 sign-misprint claim

**Record of the withdrawal.** `research/c_glauber/DERIVATION.md` §0.3 (l. 63–68): "An earlier (interrupted) draft of
`unitarity_cuts.py` claimed a sign misprint in a specific equation of Collins (2011); this could not be verified and has been
**withdrawn**." `scripts/unitarity_cuts.py` l. 13 now says "the exact equations there were NOT available to us, so no equation number
is quoted". `logs/*.log`, `tex/*.tex` and the compiled `test_c_glauber.pdf` contain no misprint claim about the book (the only
"sign" mention is the physics of the Collins-2002 Sivers sign reversal). `spec_v2/REFS_NOTES_v2.md` l. 349: "E19 | withdrawn — never print".

**Does the material assert any other Collins-2011 misprint?** `e19_scan.py` (210 hits) and `e19_scan2.py` were inspected hit by hit.
In the monograph material (`research/`, `spec/`, `spec_v2/`, `refdoc/`, `frontier/`) the only assertions that something in Collins (2011)
is printed wrongly are
* Fig. 7.10 (Wilson-line vertices): `research/c_wilson/DERIVATION.md` l. 198, 559; `tex/c_wilson_rules.tex` l. 162;
* eqs. (11.4)–(11.6) (indices interchanged): `research/c_wilson/DERIVATION.md` l. 496, 565, `tex/c_wilson_gy.tex` l. 22,
  `scripts/s5_grammer_yennie.py` l. 8; `spec*/FINAL_OUTLINE*.md`, `spec*/VERIFIED_FORMULAS*.md`, `spec_v2/OUTLINE_core.md`, REFDOC ERR-M5, `refdoc/notes/R1.md` l. 850.

All other hits are conventions (sign of g, Fourier sign of (13.35)), Collins correcting *CSS 1988* (E31), textbook-proof remarks
(§5.4.3), or misprints in *other* papers (BS Γ₁, Aybat–Rogers ζ).

Both items are in the author's errata list, Sec. 3 ("Corrections and updates relative to published paperback edition of November 2013"):
the Fig. 7.10 item ("reversal of the sign of the Feynman rule for the gluon-to-Wilson-line coupling to the right of the final-state cut in
the gluon pdf", with the corrected table) and the p. 402 item ("In Eqs. (11.4)–(11.6), subscript Lorentz indices should be replace[d] by
superscripts, and vice versa", with K_{μν} = k_μ w_{2ν}/(k·w₂ − i0)).

**One further item, in a verification report only.** `verify/claims/batch_N19_s1.md` (l. 46, 68–76) independently finds that Collins
eq. (14.30) "as printed has the overall sign reversed" and suggests: "If E19 is revisited, it should name eq. (14.30)". It could not check
the errata list. I checked both ends:
* Printed (OA reissue, p. 559, rendered): "the unitarity identity that the integrand equals i∏_f 1/(P_A^− − k_A^− − Σ_{j>f} l_j^− − D_f − i0)
  − i∏_f 1/(… + i0)" (14.30).
* Errata, Sec. 3: "P. 559. In Eq. (14.30), the sign of each of the terms should be reversed", i.e. −i∏(… − i0)⁻¹ + i∏(… + i0)⁻¹.
* `e19_collins1430.py`: with 2πδ_ε(a) = i[1/(a + iε) − 1/(a − iε)], the (14.29) integrand equals the **errata** form exactly for
  N = 1…4 (telescoping), and the printed (14.30) is minus it. At N = 1 the printed form gives −2πδ(a), against Collins' own
  "For the case N = 1 … we simply get unity".

So (14.30) **is a genuine sign misprint, but the author has already corrected it**. It must not be revived as E19, i.e. as our erratum. If
the N19 material (Ch. 10/12) mentions it, it is cited as the author's erratum, class Q2, next to E27. (The withdrawn draft may well
have meant (14.30), but the equation it named was not recorded, so this cannot be established.)

Bookkeeping: `verify/CLAIMS.md` §E19 "How to verify" cites "(E28)"; it should be E27 (E28 is Sterman–Weinberg).

**Verdict: confirmed** (withdrawal). Nothing printed as our own erratum of Collins (2011).

## 3. E20 — i0 of the u-channel denominator in Ji's DVCS amplitude

### 3.1 What is printed
* hep-ph/9603249v1, `spin1.tex` l. 382–400. My count of numbered rows gives **(15)**. With T^{μν} = i∫d⁴y e^{−iq·y}⟨P′|TJ^ν(y)J^μ(0)|P⟩
  ("ν and μ are the polarization indices of the initial and final photons") and q = −ξp + (Q²/2ξ)n, Δ = −ξ(p − M̄²n/2) + Δ_⊥ (eq. (14)):
  T^{μν} = −½(p^μn^ν + p^νn^μ − g^{μν})∫dx[1/(x − ξ/2 + iε) + **1/(x + ξ/2 + iε)**][H Ūn̸U + E Ū iσ^{αβ}n_αΔ_β/(2M) U]
           − (i/2)ε^{μναβ}p_αn_β∫dx[1/(x − ξ/2 + iε) − **1/(x + ξ/2 + iε)**][H̃ Ūn̸γ₅U + Ẽ (Δ·n/2M) Ūγ₅U].
  So the +iε stands in the second denominator of **both** brackets. Ji's ξ: Δ^+ = −ξ_Ji P̄^+, hence ξ_Ji = 2ξ. Diehl's review
  (hep-ph/0307382, l. 556–559) states "ξ_[Ji:1998pc] = ξ_[Ji:1997ek]/2".
* Ji's own PRD 55 (1997) 7114 (hep-ph/9609381): the same amplitude with **1/(x + ξ/2 − iε)** in both brackets, already in **v1 of
  Sept. 1996** (source) and in v3, where it is **eq. (4)** (source count and PDF). That paper defines μ as the *virtual*-photon index ("μ and ν are the polarization indices of the
  virtual and real photons"), which accounts for its +(i/2)ε^{μναβ} versus the PRL's −(i/2).
* VGG (hep-ph/9905372) **eq. (38)** (PDF numbering checked): [1/(x − ξ + iε) ± 1/(x + ξ − iε)], with ε_{0123} = +1.
* The published PRL could not be read (APS 403). INSPIRE lists no erratum.

### 3.2 Independent derivation (`e20_dvcs_s2.py`)
(A) In Ji's own variables, with collinear k = (x + ξ/2)p:
  (k + q)² = (Q²/ξ)(x − ξ/2) **exactly**, and (k − q′)² = −(Q²/ξ)(x + ξ/2) + O(Q⁰).
  Feynman's +i0 then gives 1/(x − ξ/2 + i0) for the s-channel and **−(ξ/Q²)/(x + ξ/2 − i0)** for the u-channel (symbolic, PASS).
(B) Exact tree-level T^{μν} = −e²ū(P′)[γ^μ(P̸+q̸)γ^ν/((P+q)²+i0) + γ^ν(P̸−q̸′)γ^μ/((P−q′)²+i0)]u(P) on an on-shell massless quark
  target (t = −0.3, ξ_Ji = 0.4, Δ_⊥ ≠ 0), with explicit helicity spinors. For this target H = H̃ = δ(1−x), so the i0 does not matter here
  and the check tests signs and normalization.
  For both helicities the transverse components agree with
  **T^{μν} = g_⊥^{μν}Σe_q²∫dx F^q[1/(x−ξ+i0) + 1/(x+ξ−i0)] − iε_⊥^{μν}Σe_q²∫dx F̃^q[1/(x−ξ+i0) − 1/(x+ξ−i0)]**
  to 7.1·10⁻⁵, 7.1·10⁻⁷, 7.4·10⁻⁹ at Q² = 10³, 10⁵, 10⁷ (∝ t/Q²). Ji's eq. (15) (iε aside) agrees equally well with ε^{0123} = +1.
  Negative control: ε^{0123} = −1 gives a 40 % mismatch in the axial term.
(C) With −i0 the C-even amplitude is A(ξ) = ∫₀¹dx F^{(+)}(x)[1/(x − ξ + i0) + 1/(x + ξ)], F^{(+)} = q + q̄, i.e. the boundary value at
  ξ − i0 (ν + i0) of **one** function analytic off the cuts. With Ji's +i0 the two terms are boundary values from opposite sides.
  Numerically (model q = x^{−1/2}(1−x)³, q̄ = 0.3x^{−1/2}(1−x)⁷, ξ = 0.2):
  * Re A, computed directly from the two-term PV integral on [−1,1], is −1.62239188011. The crossing-symmetric dispersion integral of
    Im A gives −1.62239188011 with −i0, but −0.72319549539 with Ji's +i0.
  * Forward limit: Im T^{11} = π(q + q̄)(x_B) = 2πF₁ > 0 with −i0, whereas +i0 gives π(q − q̄): antiquarks enter with the wrong sign.
  * Direct integration at η = 10⁻³ and 10⁻⁴ converges to both imaginary parts.
  The relative i0 between the two terms is convention independent: flipping the Fourier sign or the time ordering flips both.

### 3.3 Verdict and printable statement
**Confirmed.** Printable:
> In arXiv:hep-ph/9603249v1 (the preprint of Ji, PRL 78 (1997) 610), eq. (15), the second denominator of both brackets is printed
> 1/(x + ξ_Ji/2 + iε). It must be 1/(x + ξ_Ji/2 − iε) (u-channel Feynman propagator; analyticity and positivity of Im T in the forward limit).
> ξ_Ji = 2ξ. Ji's PRD 55 (1997) 7114, eq. (4), and VGG (1999) eq. (38) have −iε.

The corrected LO result above is right in the conventions
T^{μν} = i∫d⁴z e^{iq′·z}⟨P′|T J^μ(z)J^ν(0)|P⟩ (μ outgoing, ν incoming; identical to Ji's), γ₅ = iγ⁰γ¹γ²γ³, ε^{0123} = +1,
ε_⊥^{μν} = ε^{μνρσ}n̄_ρn_σ with n̄ along the hadron (Ji's p), n̄·n = 1 (so ε_⊥^{12} = +1),
F^q = (2P̄^+)^{−1}[H ū′γ^+u + E ū′ iσ^{+α}Δ_α u/(2M)] and F̃^q = (2P̄^+)^{−1}[H̃ ū′γ^+γ₅u + Ẽ Δ^+ ū′γ₅u/(2M)].
These conventions must be printed with it. The PRL text itself is unchecked, so the erratum must be attributed to the arXiv v1.

## 4. E21 — Mankiewicz–Piller "12/τ and 9/τ"

**Printed** (`rhot7.tex`; numbering counted and matched with the PDF): (3) Φ_∥ = ½[τ̄∫₀^τ φ/ū − τ∫_τ¹ φ/u]; (4) g^v = ½[∫₀^τ φ/ū + ∫_τ¹ φ/u];
(5) g^a = 2[τ̄∫₀^τ φ/ū + τ∫_τ¹ φ/u]; (10) I₁ = ∫₀¹(dτ/τ)(4g^v − 2Φ_∥/τ + g^a/(2ττ̄)), I₂ = ∫₀¹(dτ/τ)(2g^v + g^a/(2ττ̄)).
Text after (10): "For the asymptotic distribution amplitude φ_∥(τ) = 6ττ̄ the integrands in eq.(10) are proportional to 12/τ and 9/τ,
respectively. One, therefore, might expect that any phenomenological regularization … leads to a ratio I₁/I₂ close to one."

**Analytic (by hand).** For τ → 0: g^v → σ_φ/2 = g^v(0), g^a → 2σ_φτ, Φ_∥ → −σ_φτ/2, with σ_φ = ∫₀¹φ/u. Hence the I₁ integrand
→ (4·σ/2 + σ + σ)/τ = 4σ_φ/τ = 8g^v(0)/τ, and the I₂ integrand → (σ + σ)/τ = 2σ_φ/τ = 4g^v(0)/τ. For φ = 6ττ̄, σ_φ = 3, giving **12/τ and 6/τ**.

**Numerical** (`e21_mp_s2.py`; eqs. (3)–(5) integrated by quadrature as printed):
* asymptotic DA: coefficients 12.0 and 6.0; the integrands are exactly 12/τ − 21 + 18τ and 6/τ − 6 + 6τ;
* a₂ = 0.2: 14.4, 7.2; a₂ = −0.1, a₄ = 0.15: 12.6, 6.3; 30τ²τ̄²: 10, 5. Always 4σ_φ and 2σ_φ, ratio exactly 2.

A "9" would require a different I₂, e.g. 4g^v or g^a/(ττ̄); both give 6g^v(0) = 9. Which of the two, text or eq. (10), is misprinted
cannot be decided from the paper. Diehl's review says MP and Anikin–Teryaev "agree" but quotes no coefficients.
The divergence is logarithmic in every case, so the physics conclusion (no factorization for γ*_T → ρ_T) is unaffected.

**Verdict: confirmed.** Printable: "In Mankiewicz–Piller, PRD 61 (2000) 074013 [arXiv:hep-ph/9905287], the text after eq. (10) states
that for φ_∥ = 6ττ̄ the integrands of eq. (10) behave as 12/τ and 9/τ. Eq. (10) with eqs. (3)–(5), as printed, gives 12/τ and 6/τ;
in general 8g^v(0)/τ and 4g^v(0)/τ, with g^v(0) = ½∫₀¹du φ_∥(u)/u. The paper is internally inconsistent; '9/τ' should not be quoted."
Recommended addition: do not quote MP's inference "I₁/I₂ close to one" either; it rests on 12:9, while eq. (10) gives 2:1 for every DA.
The journal text was not accessible.

## 5. E23 — Becher–Schwartz Γ₁

**Printed.** arXiv v1 (l. 1196–1197) and v2 (l. 1204–1205), and **JHEP 07 (2008) 034, eq. (A.10), p. 29** (rendered):
Γ₁ = 4C_F[C_A(67/9 − π²/3) − (20/9) **C_F** T_F n_f], with Γ_cusp = Σ(α/4π)^{n+1}Γ_n (their eq. (A.6) block). Γ₀ = 4C_F.

**Correct value, independently** (`e23_cusp_s2.py`):
* (S1) Becher–Neubert JHEP 06 (2009) 081 [Erratum JHEP 11 (2013) 024; arXiv:0903.1126v5, i.e. post-erratum, read]: γ₁^cusp = (268/9 − 4π²/3)C_A − (80/9)T_F n_f, with
  Γ^q_cusp = C_F γ_cusp and γ = Σγ_n(α_s/4π)^{n+1}. So C_F γ₁ = 4C_F[(67/9 − π²/3)C_A − (20/9)T_F n_f] identically. They attribute the
  two-loop result to Korchemsky–Radyushkin, NPB 283 (1987) 342, among others.
* (S2) MVV 2004, eq. (3.11) (label `eq:An`; PDF numbering checked): A₂ = 8C_F[(67/18 − ζ₂)C_A − (5/9)n_f], identical at T_F = ½;
  same normalization, since A₁ = 4C_F.
* (S3) Coupling counting: at O(α_s²) a closed quark loop costs g² (a self-energy insertion into a single exchange, colour C_F T_F n_f),
  while a C_F² factor needs two exchanges (g⁴). So **C_F²T_F n_f cannot occur at two loops**; it first appears at three loops (present
  in MVV's A₃). BS's formula differs from the correct one by (80/9)C_F T_F n_f(1 − C_F), i.e. it contains a forbidden C_F²T_F n_f term.
  The correct form contains only C_F C_A and C_F T_F n_f.
* Numbers (SU(3), n_f = 5): **36.8436** (correct) versus 26.9670 (printed).
* (S4) **BS's own numerics used the correct value.** Their text (v2 l. 840) says that with Padé×2 "Γ₄ ≈ ±2×10⁴". Their App. A gives
  Γ₃ ≈ Γ₂²/Γ₁, and Γ₄ = 2Γ₃²/Γ₂ = 2Γ₂³/Γ₁². This is **2.02×10⁴** with the correct Γ₁ and 3.77×10⁴ with the printed one.
  So the App. A line is a transcription misprint.

**Verdict: confirmed.** Printable: "Becher–Schwartz, JHEP 07 (2008) 034, eq. (A.10) [also arXiv:0803.0342 v1, v2, App. A], print
Γ₁ = 4C_F[C_A(67/9 − π²/3) − (20/9)C_F T_F n_f]; the C_F multiplying T_F n_f is spurious. Correct (Γ_cusp = Σ(α_s/4π)^{n+1}Γ_n):
Γ₁ = 4C_F[(67/9 − π²/3)C_A − (20/9)T_F n_f] (Korchemsky–Radyushkin 1987; e.g. Moch–Vermaseren–Vogt 2004, eq. (3.11)/(An))."
Not found reported: INSPIRE has no erratum record. A full-text search `refersto:780596 ∧ cusp ∧ (misprint ∨ typo ∨ erratum)` gave 68
broad hits; I scanned 2502.01570, 2205.05702, 2002.00942, 2002.05730, 1708.00867, 1308.4473 and 0903.1126, and stage 1 had read seven
others. None mentions it.
Patch note: `research/c_scet/DERIVATION.md` §6 item 10 says "Typo in the Becher–Schwartz arXiv source"; it is also in the journal version.

## 6. E24 — Becher–Schwartz jet-function normalization

**Printed.** JHEP 07 (2008) 034, **eq. (2.6), p. 5** (PDF page 7), identical in arXiv v1/v2 (diffed):
J(p², μ) = (n̄·p)^{−1}(1/π) Im[i∫d⁴x e^{−ipx}⟨0|T{χ̄_n(x)(n̸̄/2)χ_n(0)}|0⟩] = δ(p²) + O(α_s). No Dirac or colour normalization is given.

**Mode-expansion derivation** (`e24_jet_s2.py`):
1. P_n p̸ P̄_n = (n̸/2)n̄·p exactly, off shell; tr[(n̸̄/2)(n̸/2)] = 2; χ̄ = ψ̄P̄_n with P̄_n = γ⁰P_n†γ⁰.
2. Massless spin sums Σuū = Σvv̄ = k̸ (explicit Dirac-representation spinors).
3. Fermionic T-ordering by modes: ⟨Tψ̄_a(x)Γ_{ab}ψ_b(0)⟩ = θ(x⁰)∫dk̃ tr[Γk̸]e^{−ik·x} − θ(−x⁰)∫dk̃ tr[Γk̸]e^{+ik·x}.
   With explicit time integrals (−i/(p⁰+E−iη), +i/(p⁰−E+iη)) this gives
   i∫d⁴x e^{−ipx}⟨Tψ̄(x)Γψ(0)⟩ = tr[Γp̸]/(p² + i0) (symbolic, PASS).
4. For χ_n with Γ = n̸̄/2: 2N_c n̄·p/(p² + i0). With (1/π)Im 1/(p²+i0) = −δ(p²) (checked against a test function), **J = −2N_c δ(p²)**.
   With e^{+ipx} instead one gets +2N_c δ(p²); either way the stated normalization needs a factor ∓1/(2N_c).
5. Becher–Neubert, PLB 637 (2006) 251 [hep-ph/0603140] (BS's ref. [23]), **eqs. (3) and (6)**:
   (n̸/2)n̄·p 𝒥 = ∫d⁴x e^{−ipx}⟨0|T{𝒳(0)𝒳̄(x)}|0⟩ (matrix-valued, "proportional to a unit matrix in color space"), J = (1/π)Im[i𝒥].
   This gives 𝒥 = i/(p²+i0) and J = +δ(p²): properly normalized.
6. Cut definition Σ_X(2π)^Dδ^D(p − p_X)⟨0|χ_n|X⟩⟨X|χ̄_n|0⟩ = 2π(n̸/2)n̄·p J 𝟙_c gives J⁽⁰⁾ = δ(p²)θ(p⁰) (spin sums, PASS).

**Verdict: confirmed.** Printable: "Becher–Schwartz, JHEP 07 (2008) 034, eq. (2.6), define the jet function as (n̄·p)^{−1}π^{−1}Im[i∫d⁴x
e^{−ipx}⟨0|T{χ̄_n(x)(n̸̄/2)χ_n(0)}|0⟩] = δ(p²) + O(α_s). Read literally (scalar operator summed over Dirac and colour indices, fermionic
T-ordering), the free field gives −2N_c δ(p²), so a factor −1/(2N_c) is implicit. We use the explicitly normalized cut definition
Σ_X(2π)^Dδ^D(p−p_X)⟨0|χ_n|X⟩⟨X|χ̄_n|0⟩ = 2π(n̸/2)n̄·p J(p²)𝟙_c (equivalently Becher–Neubert 2006, eqs. (3), (6))." Not found reported.

## 7. E25 — BPS 2002: the ghost term and collinear gauge invariance

**Printed.** arXiv:hep-ph/0109045 v1 and v2 are identical in this passage (diffed; v2 is the journal version). Eq. (24) (label `Lcg`;
my own equation count of the source gives (Dc) = (17), (Dus) = (18), (Lcg) = (24), and the arXiv PDF prints "(24)"):
𝓛_c^{(g)} = (1/2g²)tr{[i𝒟^μ + gA^μ_{n,q}, i𝒟^ν + gA^ν_{n,q′}]}² + 2tr{c̄_{n,p′}[i𝒟_μ,[i𝒟^μ + gA^μ_{n,q}, c_{n,p}]]} + (1/α)tr{[i𝒟_μ, A^μ_{n,q}]}².
Text: "The first two terms in Eq. (Lcg) are invariant under collinear gauge transformations, while the last is the gauge fixing term
with parameter α. Furthermore, the complete collinear Lagrangian is invariant under usoft gauge transformations, including the 1/α
gauge fixing term." Table I gives A → U A U† + (1/g)U[i𝒟 U†] (so i𝒟 + gA → U(i𝒟 + gA)U†), and the ghost rows are **commented out**
in the source, so the printed paper specifies no ghost transformation.

**Checks** (`e25_ghost_s2.py`, 16/16):
* Field theory, SU(2), A = 0, A_us = 0. Brute-force variation agrees with the closed forms derived via the Jacobi identity:
  adjoint ghosts δ𝓛_gh = −2i tr{c̄[∂_μω, ∂^μc]} (in general 2i tr{c̄[[i𝒟_μ, ω],[Π^μ, c]]}); inert ghosts δ𝓛_gh = 2tr{c̄[i∂_μ,[∂^μω, c]]}.
  On Gaussian test functions the **action** variation is exactly −π²/9 (adjoint) and −π²/27 (inert), times θ̄θ for Grassmann ghosts.
  It is not a total derivative. It vanishes in the abelian case.
* Reduced matrix model (i𝒟_μ → fixed matrices, trace cyclicity ↔ integration by parts), finite U:
  * field-strength term invariant; ghost term not invariant (relative change 1.67 adjoint, 0.65 inert); gauge-fixing term not invariant;
  * under usoft V (background conjugated, c, c̄ → V·V†) all three terms are invariant;
  * |det M_FP| changes under the collinear transformation (1.02·10⁷ → 4.72·10⁶) and not under the usoft one. Hence no ghost
    reassignment with unit Jacobian can restore invariance. Caveat: in the matrix model the background components do not commute,
    so this is supporting evidence only; the field-theory counterexample above uses a commuting background and is decisive.
* BRST, explicit Grassmann algebra: s² = 0 on A and c singles out sc = icc (normalization sA = −(i/g)[Π, c]); s𝓛_F = 0;
  s(𝓛_gf + 𝓛_gh) = 0 exactly for sc̄ = (i/αg)G, unique among ±1/(αg), ±i/(αg); s𝓛_gf and s𝓛_gh are **separately non-zero** (equal and opposite).

**Verdict: confirmed, with one precision.** Printable: "BPS, PRD 65 (2002) 054022 [hep-ph/0109045], state after eq. (24) that its first two
terms, the field-strength and ghost terms, are invariant under collinear gauge transformations. For the ghost term this is false: the
outer [i𝒟_μ, ·] is not collinear covariant, and the variation is non-zero for adjoint as well as for inert ghosts. The field-strength
term is invariant under collinear and usoft transformations. The gauge-fixing and ghost terms are each invariant under usoft
transformations (c, c̄ → V_us c V_us†; the usoft field acts as a background), but not under collinear ones. **Their sum** (not each
separately) is BRST invariant, and so is the full 𝓛_c^{(g)}. Usoft invariance and BRST invariance are what the decoupling proof uses."
Patch note: `research/c_scet/DERIVATION.md` §6 item 15 and `tex/c_scet_scet.tex` prop:scet-gauge should say "their sum is BRST invariant".

## 8. Literature searches (prior reports)
* INSPIRE records (API): Ji:1996ek, Mankiewicz:1999tt, Becher:2008cf, Bauer:2001yt, Becher:2006qw carry **no erratum** publication_info.
* Full-text searches (combinations different from stage 1):
  * `refersto:416559 ∧ prescription ∧ (misprint ∨ typo)`: 17 hits; the DVCS-era ones (hep-ph/9704406, 9801252, 9806305) were read by
    stage 1 (other misprints). Diehl's review was grepped: no remark on Ji's iε.
  * `refersto:780596 ∧ cusp ∧ (misprint ∨ typo ∨ erratum)`: 68 hits, 7 scanned here (see §5).
  * `refersto:780596 ∧ "jet function" ∧ normalization ∧ (misprint ∨ typo)`: 7 hits, none relevant by title; stage 1 read two.
  * `refersto:562452 ∧ ghost ∧ "collinear gauge" ∧ (…)`: 11 hits. Scanned 1808.04742 (its misprint footnote concerns Beneke et al. 2017),
    hep-ph/0409277, 1506.05301, 1106.6047: nothing on the BPS sentence.
  * `refersto:499583 ∧ (9/τ ∨ 12/τ ∨ misprint ∨ typo)`: 2 hits (hep-ph/0210045, hep-ph/0307382); neither concerns MP's coefficients.

## 9. Agreement with stage 1, and bookkeeping
Stage 2 agrees with stage 1 on all six verdicts, with these additions:
* E19: (14.30) is an author erratum, now checked on the printed page and in the errata list. It resolves N19-s1's open question and
  must be cited as the author's correction, not revived as E19.
* E20: the opposite axial sign in Ji's PRD eq. (4) is explained by its swapped photon indices. It is not an independent sign problem.
* E23: BS's own Padé number (Γ₄ ≈ ±2×10⁴) independently shows that their numerics used the correct Γ₁.
* E25: the Faddeev–Popov determinant test excludes any unit-Jacobian ghost reassignment.

CLAIMS.md §E19 cross-reference "(E28)" → "(E27)" (also noted by stage 1).

## 10. Files
* Report: `verify/claims/batch_E19_s2.md` (this file).
* Scripts and logs: `verify/claims/batch_E19_s2_scripts/` — `e19_scan.py` (+`.log`), `e19_scan2.py` (+`.log`), `e19_collins1430.py` (+`.log`),
  `e20_dvcs_s2.py`, `e21_mp_s2.py`, `e23_cusp_s2.py`, `e24_jet_s2.py`, `e25_ghost_s2.py` (each with `.log`).
* Downloads (untrusted; scratchpad only, not in the project): Ji v1, Ji PRD v1/v3, VGG, MP, BS v1/v2/JHEP, BN 2006 (×2), BN 2009, MVV 2004,
  BPS v1/v2, Collins errata PDF, Collins OA chapter 14, Diehl review and 11 scanned citing papers.
