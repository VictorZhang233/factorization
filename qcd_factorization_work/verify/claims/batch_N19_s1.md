# Verification batch N19–N24 (stage 1, independent verifier)

Date: 2026-10-10. Default stance: skeptical. Claims N19–N24 of `verify/CLAIMS.md` (new results of c_glauber, c_tmd, c_exclusive,
c_scet, c_pdf/c_exclusive/critic, c_ee). Every formula below was re-derived with my own code (not the project's scripts), and the
project scripts named in the recipes were re-run unchanged.

## 0. Method and sources

**My scripts** (all in `verify/claims/batch_N19_s1_scripts/`, run with `python3 -I`, outputs `*.out.txt` next to them):

| script | content | result |
|---|---|---|
| `n19_glauber.py` | telescoping identity (N ≤ 6 symbolic, proof step, E-integral by residues); colour factors with independently built generators (random adjoint-basis rotations; SU(2) F, A, spin 1, 3/2; SU(3) F, F̄, A, **6**; SU(4) F, F̄, A); commutator identity; Glauber kernel by numerical k^∓ integration at finite i0; χ(b) by Fourier transform and by the standard eikonal formula; exact singlet-survival formula | 70/70 PASS |
| `n20_vertex.py` | TMD vertex graph by a **different method** (light-cone variables, l^- residues, region-by-region closed forms with explicit i0 bookkeeping); numerical checks of residues and i0 signs; remainder Fourier transform | 36/36 PASS |
| `n21_ils.py` | R_as, R_CZ by exact sympy integration; 2D quadrature; asymptotics; numbers; Yeh 2001 cross-check | 16/16 PASS |
| `n22_xa.py`, `n22_xa_quick.py` | BBNS integrands → BN-rule values; double-cutoff value by mpmath (analytic x-integral) and direct 2D quadrature; corner-region analysis; symmetry r1 ↔ r2 | 11/11 PASS (shows the claimed −21.6 is wrong) |
| `n23_math.py` | Thm 7.2/Cor 7.3/Prop 7.5/Prop 7.7 ingredients, Jensen, Müntz Gram determinants (exact rationals), infinite product, Carlson borderline functions, ERBL hermiticity, triangularity (k ≤ 12) and Gegenbauer eigenvalues (n ≤ 6), REVIEW counterexamples | 30/30 PASS (one rounding issue) |
| `n24_cut.py` | own D-dimensional trace engine; real-emission matrix element; D-dim 3-body phase space (normalisation by recursion); one-loop form factor exact in ε (own traces + Feynman parameters); two-loop Π from **Grozin's published d-dimensional formula**; cutting identity at 5 values of ε | 29/29 PASS |
| `n24_msbar.py` | MS-bar expansion of Π at one and two loops from Grozin's formula (Laurent coefficients by contour integration) | 9/9 PASS |

**Project scripts re-run** (outputs in `batch_N19_s1_scripts/rerun/`): `unitarity_cuts.py` 58/58, `ss_exchange.py` 23/23, `diffraction.py` 12/12,
`colour_factors.py` 32/32, `virtual_vertex.py` PASS, `s4_pion_ff.py` 20/20, `s4_bbns.py` 26/26 (but see N22: its "regulator dependence" check
prints −21.555 from a non-converged `scipy.dblquad`; the run emits "The algorithm does not converge", "The integral is probably divergent",
"maximum number of subdivisions (50) has been achieved"), `s6_uniqueness.py` 15/15, `s3_erbl_eigen.py` 21/21, `cut_identity_analytic.py` PASS,
`pi_twoloop.py` 18/18, `rg_structure.py` 5/5.

**Literature read in this session** (downloaded as untrusted data into the scratchpad; nothing executed from it):
- Collins, *Foundations of Perturbative QCD* (OA reissue, Cambridge Core chapter PDFs): ch. 10 (pp. 313–397), ch. 13 (pp. 479–539),
  ch. 14 (pp. 540–572); pp. 349, 381, 538, 559 rendered/read in full. (The OAPEN full-book link returned 403.)
- Collins–Metz, PRL 93 (2004) 252001, arXiv:hep-ph/0408249v2 (source). Aybat–Rogers, arXiv:1101.5057v2 (source). Ji–Ma–Yuan, arXiv:hep-ph/0405085 (source).
- Rothstein–Stewart, arXiv:1601.04695v3 (source). Aybat–Sterman, arXiv:0811.0246v1 (source).
- Isgur–Llewellyn Smith, preprint OXFORD-TP 72/83 = PRL 52 (1984) 1080, KEK scan 84-02-270 (14 pp., OCR + page images).
  ILS, NPB 317 (1989) 526 (CERN-TH-5013-88): **not accessible** (CERN CDS bot check; publisher paywall); only the INSPIRE abstract was read.
- Yeh, arXiv:hep-ph/0107192v2 (source). Stefanis, arXiv:hep-ph/9911375 (source; review, ILS passages).
- Beneke–Buchalla–Neubert–Sachrajda, NPB 606 (2001) 245, arXiv:hep-ph/0104110 (source); Beneke–Neubert, NPB 675 (2003) 333, arXiv:hep-ph/0308039 (source).
- Waldschmidt, arXiv:2002.01223v1 (source).
- Grozin, *Lectures on QED and QCD*, arXiv:hep-ph/0508242 (source), eqs. (Photon1:Res1), (Photon2:Pi2), (Photon2:Pi).
- INSPIRE abstracts: Poggio–Quinn PRD 14 (1976) 578; Lowenstein–Zimmermann CMP 44 (1975) 73; Lowenstein CMP 47 (1976) 53;
  Breitenlohner–Maison CMP 52 (1977) 11, 39, 55; Efremov–Guida–Kopper J. Math. Phys. 58 (2017) 093503.
  **BM II full text not accessible** (Project Euclid "Pardon Our Interruption" bot check; Springer JS challenge). No circumvention attempted.

## 1. Summary

| id | verdict | what must change before printing | already in the literature? |
|---|---|---|---|
| N19 | **confirmed** | (iv) must say "for U = exp(i d T_q·T_B)" or "to second order in the phases": with a common phase χ₀ ≠ 0 the d² coefficient is smaller (0.2156 at χ₀ = 0.4, 0.1835 at χ₀ = 1 for SU(3)). | (i) Collins 2011 eqs. (14.29)–(14.30), p. 559 (same identity; **(14.30) as printed has the overall sign reversed**, see §2.1). (ii) One-line Lie-algebra identity; not in RS 2016 (checked). (iii) The same phase is RS 2016 §9 (gluon-mass form of φ(b⊥)); standard eikonal phase. (iv) toy, not found. |
| N20 | **confirmed** | Cite Collins 2011 §10.6.4 (p. 349) and §10.11.1 (p. 381) for the ordering mechanism, and Ex. 13.8 (p. 538), which poses exactly this question. §10.8 is relevant only to the order of limits (§10.8.2). The remainder FT equals 2π²/(Λ_B b_T) only up to O(e^{−Λ_B b_T}) terms (18.23 vs 19.74 at Λ_B b_T = 1). | Mechanism stated qualitatively in Collins–Metz 2004 and Collins 2011; the explicit one-loop 2π² was not found. |
| N21 | **confirmed** (mathematics and numbers) | Attribute the fraction to ILS **1989** (NPB 317), not to the 1984 PRL, which contains no such fraction (read in full). Do not claim novelty for the closed forms: ILS 1989 could not be read. | Yeh 2001 says ILS used f(ε) = 1 − R(ε) and quotes "90% for ε = 1/150" for the asymptotic DA (our formula: 0.892). No closed form in ILS 1984, Yeh 2001 or Stefanis 1999. |
| N22 | **refuted** (the number is wrong; formulas and qualitative conclusion right) | The double cutoff changes only the constant, π²/3 → π²/6 in the bracket. The shift of A_3^i is **−π² ≈ −9.87** (units πα_s(r_χ^{M1} − r_χ^{M2})), independent of X_A. The "−21.6" comes from a non-converged scipy integral. Fix c_scet DERIVATION §5.7 line 480 and `tex/c_scet_bdecays.tex` rem:qcdf-prescription (line 187). | Formulas = BN 2003 eq. (XAmodel), BBNS 2001 eq. (XAdef). "Model-dependent": BN 2003 and BBNS 2001 say so themselves. |
| N23 | **confirmed** | π/sinh(√3π) = 0.0272282: print **0.02723** (or 0.027228), not "0.02722" (a truncation; c_pdf DERIVATION §7.3 line 498). | All classical (Hausdorff, Müntz–Szász, Blaschke/Jensen, Carlson; the ERBL Gegenbauer eigenfunctions are classical, but I recalled the Efremov–Radyushkin / Lepage–Brodsky 1980 attribution and did not re-read it). Carlson's theorem is cited by Waldschmidt at Titchmarsh §5.81 and Boas Thm 9.2.1 (verified). |
| N24 | **confirmed** (logic, exact identity, Π_MS) | (a) BM II gauge-theory scope **could not be verified** (full text inaccessible). Keep "[to verify]", or rest step (a) for QCD on Poggio–Quinn 1976 (physics-level) and say that applying the rigorous massless theorems to gauge fields with ghosts is assumed. (b) Write N_c Σ_q e_q² (charges in units of e), not "N_c e²". | Route = Poggio–Quinn 1976 corollary ("any physical discontinuity ... is also infrared finite"). Two-loop Π in d dims: Grozin hep-ph/0508242 eq. (Photon2:Pi), from which the MS-bar constants 55/12 − 4ζ₃ follow (verified here). |

---

## 2. N19 — further c_glauber results

### 2.1 (i) Finite-ε telescoping identity

With u_f = (a_f + iε)^{−1}, v_f = (a_f − iε)^{−1} one has 2ε/(a²+ε²) = i(u − v) exactly. Define T_c = Π_{f>c} v_f Π_{f≤c} u_f. Then the c-th term is
[Π_{f>c} v_f] i(u_c − v_c) [Π_{f<c} u_f] = i(T_c − T_{c−1}), and the sum telescopes:

  Σ_{c=1}^N [Π_{f>c}(a_f − iε)^{−1}] 2ε/(a_c²+ε²) [Π_{f<c}(a_f + iε)^{−1}] = i Π_f (a_f + iε)^{−1} − i Π_f (a_f − iε)^{−1}.

This is a complete proof for all N. It was checked symbolically for N = 1…6 and the step identity was checked separately. For a_f = E − d_f,
∫dE/2π of the right-hand side is 1 for N = 1 (Lorentzian) and 0 for N ≥ 2 (each product is O(E^{−N}) with all poles in one half plane).
I checked this by residues for N = 2, 3 and numerically (|∫| = 1e−14).

**Literature.** Collins 2011, §14.4.3, eqs. (14.29)–(14.30), p. 559, contains exactly this sum over final-state cut placements:
(14.29) = ∫dk_A^-/2π Σ_c [Π_{f>c} (a_f − i0)^{−1}] 2πδ(a_c) [Π_{f<c}(a_f + i0)^{−1}], with a_f = P_A^- − k_A^- − Σ_{j>f} l_j^- − D_f.
Collins writes "the unitarity identity that the integrand equals i Π (a_f − i0)^{−1} − i Π (a_f + i0)^{−1}" (14.30). **That is minus the correct
result.** At N = 1 his (14.30) gives −2πδ(a), whereas (14.29) and his own sentence "For the case N = 1 ... we simply get unity" give +2πδ(a).
The misprint does not affect his conclusion (each term integrates to zero for N ≥ 2). It is visible in the rendered OA-reissue page 559 (Cambridge Core chapter-14 PDF).
I could not check whether Collins's own errata list ("Corrections and updates to Nov. 2013 printing", cited in c_wilson) records it: his Penn State pages returned 503/404.
Side finding: this may be the unnamed "sign misprint in a specific equation of Collins (2011)" that c_glauber withdrew as E19 for lack of access to the book.
If E19 is revisited, it should name eq. (14.30) and print the corrected form above.
The project's finite-ε version with the correct sign is right. Novelty: none; it is the ε-regulated form of Collins (14.30) with corrected sign.

### 2.2 (ii) Ladder vs crossed colour

With c = Σ_a T_1^a T_2^a, ladder L = T_1^aT_1^b ⊗ T_2^aT_2^b = c² (the operators on different lines commute). Crossed: X = T_1^aT_1^b ⊗ T_2^bT_2^a.
Using T_2^bT_2^a = T_2^aT_2^b + i f^{bae}T_2^e and f^{bae}T_1^aT_1^b = ½ f^{bae} i f^{abg} T_1^g = −(i/2) C_A T_1^e gives **X = c² + (C_A/2) c**.
The only input is [T^a,T^b] = i f^{abc}T^c in each representation (so it also holds for colour-charge operators of incoming/outgoing
partons, T = −t^T etc.). Numerically: 30 representation pairs, generators built independently and randomly rotated, including SU(3) 6⊗6, 6⊗A and
SU(2) spin-3/2; max deviation 2e−15.
[T_A·T_B, T_A·T_j] = i f^{abc} T_A^c T_B^a T_j^b ≠ 0: Frobenius norm √3 = 1.732 on 3̄⊗3̄⊗3 (the "1.73" of c_glauber). It is also non-zero (norm 1) on the
2-dimensional colour-singlet space of four partons, which is the physically relevant statement.
Rothstein–Stewart 2016 (arXiv:1601.04695v3) only say "in QCD the box and crossbox have different color factors" (Sec. 5.2.1). The claim's remark
that RS give no general formula is correct.

### 2.3 (iii) Glauber kernel and phase

I computed the k^- (A side) and k^+ (B side) integrals numerically at finite i0 = 1e−7 with the Glauber-region denominators of c_glauber §1.2.
Results: ∫dk^-/2π (ie_A 2p_A'^+)(i/D_sA)(i/D_a) = (ie_A)[i/D_a]_{on-shell spectator} and the mirror for B (ratio errors ~1e−7). With the gluon
propagator −i/(k²−m_g²) → i/(k_T²+m_g²) this gives **V(k_T) = −ie_Ae_B/(k_T²+m_g²)**. The Fourier transform ∫d²k/(2π)² e^{−ik·b} V = iχ(b) with
**χ(b) = −e_Ae_B K_0(m_g b)/(2π)** (checked at b = 0.3, 1.4, 3; 1e−12).
Independent sign check: the standard eikonal formula χ = (1/2s)∫d²q/(2π)² e^{iq·b} M_Born, with M_Born from the same Feynman rules (s = 2p_A^+p_B^-), gives
the same χ. Like charges give χ < 0 (repulsive), as they should.
**Literature:** Rothstein–Stewart 2016, §9, eq. (eq:phi) and its gluon-mass form, read in the source: φ(b⊥) = −T_1·T_2 g² ∫đ²q e^{iq·b}/(q²+m²) = 2T_1·T_2 α_s ln(b m e^{γ_E}/2) — the same
function with e_Ae_B ↔ g² T_1·T_2. Not new.

### 2.4 (iv) Singlet → octet leakage

q q̄ singlet ⊗ B (fundamental, colour averaged), U = exp(i d T_q·T_B). Using the projectors on the 3̄ and 6 (in general antisymmetric/symmetric) of q⊗B:
  P_singlet = |(1/N)[(N+1)/2 e^{i d(N−1)/(2N)} + (N−1)/2 e^{−i d(N+1)/(2N)}]|² = 1 − d²(N²−1)/(4N²) + O(d⁴),
with no odd powers. So the coefficient is (N²−1)/(4N²) = C_F/(2N) = **2/9** for SU(3). Checked numerically for N = 2…5, at d = 0.05, 0.4, 1.3.
For B in representation R the coefficient is C_R/(2N) (adjoint: ½, checked).
With U = exp(i(χ₁T_q + χ₂T_q̄)·T_B), to second order in all phases the leakage is (χ₁−χ₂)² C_F/(2N). But at a common phase χ₀ ≠ 0 the d² coefficient is
C_F/(2N) × ⟨sinc²(χ₀λ/2)⟩ < C_F/(2N) (numerically 0.2156 at χ₀ = 0.4, 0.1835 at χ₀ = 1). This is why the project's own check D2e at χ₀ = 0.4 gives
2.155e−1, not 2/9. The statement must carry the qualifier.

**Verdict N19: confirmed** (with the qualifier in (iv)).

---

## 3. N20 — time-like vs space-like regulator lines

### 3.1 Independent computation (light-cone method)

Set p = (1, 0, 0_T), n = (a, 1, 0_T) (a > 0 time-like, a < 0 space-like), so n² = 2a and p·n = 1. My own D-dim trace gives N(l) = 2n^-(p^+ − l^+), as in the project.
V = i g² C_F μ^{2ε}∫d^Dl N/[(n·l ∓ i0)(l²+i0)((p−l)²+i0)], with −i0 for SIDIS and +i0 for DY. I re-derived the eikonal rules W[∞n,0] ⊃ g n·Ã/(n·k − i0)
and W[−∞n,0] ⊃ g n·Ã/(n·k + i0) from the binding Wilson-line convention.

Method: do the l^- integral exactly by residues. The poles are z_E = (−x ± i0)/a, z_G = (t − i0)/2x and z_Q = (t − i0)/2(x−1), where x = l^+ and t = l_T².
When one pole z_* is picked up, every other denominator is c(z_* − z_other), and its i0 takes the sign of Im z_* (all other poles are on the opposite side).
Then integrate ∫_0^∞ dt t^{−ε} in closed form. Poles on the t contour arise for DY time-like (0<x<1) and for both space-like cases; they are handled with c^{−1−ε}e^{iπ(1+ε)}.
Finally integrate over x region by region (x < 0, 0 < x < 1, x > 1). Each region has its own convergence strip, so each is continued separately in ε, as usual in DR.
The i0 bookkeeping was checked against finite-i0 numerical l^- integrals, including points 1e−4 away from the t-pole.

Results (C = 2^{−1−ε}|a|^ε π/sin πε, K = ∫dx∫dt t^{−ε}R, V = −(α_sC_F/4π)·4(4πμ²)^ε K/Γ(1−ε)):
- SIDIS time-like: K = C[−B(−2ε,2) + B(2ε−1,2) − B(2ε−1,2−ε)] = −C·B(−ε,2ε−1).
- DY time-like: K = C[B(−ε,2ε−1) + e^{iπ(1+ε)}B(−ε,2−ε)].
- SIDIS space-like: K = C[e^{iπε}B(−ε,2ε−1) − B(−ε,2−ε)].
- DY space-like: K = e^{iπε}·C[−B(−2ε,2) + B(2ε−1,2) − B(2ε−1,2−ε)].

Using B(2ε−1,2−ε) = B(−ε,2ε−1) and B(−ε,2−ε) = 2cos(πε)B(−ε,2ε−1) (both follow from Γ(z)Γ(1−z) = π/sin πz; checked to 35 digits in `n20_vertex.py`), and −B(−2ε,2) + B(2ε−1,2) = 1/(2ε(1−2ε)) + 1/(2ε(2ε−1)) = 0:

  **V_SIDIS^time = V^time ≡ −(α_sC_F/4π)(πμ²|n²|/(p·n)²)^ε Γ(1−ε)Γ(1+2ε)(1−ε)/((1−2ε)ε²)**   (identical to the project's closed form, other method),
  **V_DY^time = e^{2πiε} V^time,  V_SIDIS^space = e^{−iπε} V^time,  V_DY^space = e^{+iπε} V^time.**

Agreement with the project's numbers: 30 digits at ε = 0.17, −0.23, 0.41, −0.07, 0.013. Hence:
- space-like: V_SIDIS = (V_DY)^* exactly (real ε), so 2Re V is the same.
- time-like: Re V_DY − V_SIDIS = 2 sin²(πε)|V^time| = (α_sC_F/4π)·2π²·[1 + O(ε)] (series 2π² + 2π²(1−γ_E)ε + …).
  Also Im V_DY^time = (α_sC_F/4π)(−2π/ε + …), a divergent Coulomb phase.
All four cases are ∝ (|n²|)^ε and vanish in the light-like limit taken first (Re ε > 0). This order of limits is Collins 2011 §10.8.2, pp. 361–362 (read).

### 3.2 The interpretation

For time-like future-directed n, W[−∞n,0] = P exp(...) places points closer to −∞n (earlier times) to the left: it is anti-time-ordered, and ψ(0) (latest time) is on the right.
Feynman rules compute T[W ψ(0)]. Via ⟨0|T̄[Wψ]|p⟩ = ⟨p|T[ψ̄ W†]|0⟩^*, the operator matrix element corresponds to an incoming eikonal line and an *outgoing* quark (no Coulomb phase).
The Feynman-rule value has two incoming lines, hence the phase. The PT argument (antiunitary, preserves operator order) maps the SIDIS operator onto the path-ordered DY operator,
not onto the time-ordered one that factorization produces. For space-like n all points on the line are space-like separated, so the orderings coincide. The interpretation is correct.

### 3.3 Remainder Fourier transform

D(κ) = ln(1+κ²) + 2κ arctan(1/κ) is indeed exact-minus-limit of ∫F_b(s=+1) (checked). Write D/κ² = π/κ + [ln(1+κ²) − 2κ arctan κ]/κ². The second term is real-analytic in the 2D vector κ (singularities at κ² = −1), so
FT[D/κ²](z) = 2π²/z + O(e^{−z}). Numerically: 18.234 vs 19.739 (z = 1), 9.714 vs 9.870 (z = 2), 3.9466 vs 3.9478 (z = 5), difference 1.6e−11 at z = 20.
So "is 2π²/(Λ_B b_T)" holds asymptotically. That suffices for the light-like-limit argument, but it should not be printed as an exact equality.

### 3.4 Literature

- Collins–Metz 2004 (source read): "We choose space-like lines in the counterterms because they are compatible with one of the possibilities for the counterterms in SIDIS, and so
  they allow a proof of universality. Furthermore, exact properties of matrix elements of Wilson lines are simpler when the gluon fields are at space-like separation and hence all
  commute." Conclusions: "Regulator lines should be space-like."
- Collins 2011 §10.6.4, p. 349: "since gluon fields commute at space-like separation, the use of space-like Wilson lines ensures automatic compatibility between the path ordering
  defining the Wilson lines and the time ordering used to define Green functions". p. 350: "If one gave up the argument about universality, one could use time-like auxiliary
  vectors ... The issues of universality in this context need further investigation." §10.11.1, p. 381: "the path ordering on the lines creates no conflict with the time ordering".
  **Exercise 13.8 (***), p. 538**: "Suppose that, contrary to the argument of Collins and Metz (2004), time-like rather than space-like Wilson lines were used ... Determine whether this gives actual problems".
- Aybat–Rogers 2011 (source): n_A = (1, −e^{−2y_A}, 0_t), n_B = (−e^{2y_B}, 1, 0_t), "space-like ... ensures maximum universality ..., as explained in Ref. [Collins:2004nx]". Attribution correct.
- Ji–Ma–Yuan 2004 (DY; source): use time-like v (v² > 0) and state that the one-loop DY soft factor "is the same as that for the DIS process". They give no ordering discussion.
So the mechanism is in the literature qualitatively. The explicit one-loop result (V_DY^time = e^{2πiε}V^time, Re difference 2π²α_sC_F/4π) was not found in the sources read. It is a partial answer to Collins's Ex. 13.8.

**Verdict N20: confirmed.**

---

## 4. N21 — Isgur–Llewellyn Smith soft fractions

R(c) = ∫∫_{x̄ȳ<c} φφ/(x̄ȳ) / ∫∫ φφ/(x̄ȳ). Substituting u = x̄, v = ȳ, the region is uv < c. Exact sympy integration (own code) gives
R_as(c) = c[5c − 2(c+2)ln c − 4] and R_CZ(c) = c[456c³ + 352c² − 675c − 132 − (144c³ + 768c² + 450c + 36)ln c] (with φ_CZ = 30xx̄(2x−1)²), exactly as claimed.
2D quadrature agrees to 1e−12. Further properties: R(1) = 1; R increasing on (0,1) with R′(1) = 0; R_as ≃ 4c ln(1/c), R_CZ ≃ 36c ln(1/c). Numbers for μ₀² = 1 GeV² at Q² = 4, 10, 100 GeV²: 0.8721, 0.6171, 0.1456 (as) and
0.9753, 0.9001, 0.4815 (CZ), which round to the claimed values.
**ILS closed forms?** ILS 1984 (OXFORD-TP 72/83, read in full) has no fraction function and no closed form. Its footnote 4 only says that for the Lepage–Brodsky
"ε = 1/4" DA "more than 50% of the hard scattering is due to the end point regions x < 0.05 and x > 0.95". ILS 1989 could not be read.
Yeh 2001 (hep-ph/0107192v2, §IV) writes that ILS "employed the fraction function f(ε) = ∫∫θ(xy − ε)φ(x)φ(y)/(xy)" and "For the AS model, f(ε) reaches 90% for
ε = 1/150". Our formula gives 1 − R_as(1/150) = 0.892, and R_as = 0.10 at c = 1/165. So the concept (and probably the asymptotic-DA numbers) is ILS 1989. A closed form
appears neither in Yeh nor in Stefanis's review (hep-ph/9911375).
**Verdict N21: confirmed.** Novelty of the closed forms cannot be asserted, because ILS 1989 is unread. The attribution to the 1984 PRL is wrong.

---

## 5. N22 — X_A model

**Formulas.** From the BBNS 2001 building blocks (read in the source) with Φ = 6xx̄, Φ_p = 1 and the BN 2003 rule (XAdef) (∫dy/y → X_A, ∫ ln y/y → −X_A²/2, "similarly for M2 with y → x̄"):
A_1^i = πα_s[18(X_A − 4 + π²/3) + 2r_χ²X_A²] (= 2πα_s[9(…) + r_χ^{M1}r_χ^{M2}X_A²]); A_3^f = 6πα_s(r_χ^{M1}+r_χ^{M2})(2X_A² − X_A); A_3^i = 6πα_s(r_χ^{M1}−r_χ^{M2})(X_A² − 2X_A + π²/3).
All agree with the cutoff realisation up to O(δ ln²δ) and match BN 2003 eq. (XAmodel) and BBNS 2001 eq. (XAdef) verbatim. The finite piece is 18(π²/3 − 3).

**Prescription dependence — the claimed number is wrong.** For the r1 term 12∫∫ xȳ/(y(1−xȳ)) with x < 1−δ and y > δ, the x-integral is exact:
−(1−δ)/ȳ − ln(y+δȳ)/ȳ². The remaining y-integral gives
  I_dbl = 12∫_δ^1[−(1−δ)/y − ln(y+δȳ)/(yȳ)]dy = 6X_A² − 12X_A + π² + O(δ ln²δ),
compared with 6X_A² − 12X_A + 2π² for the BN rule. **Shift = −π² = −9.8696**, independent of X_A. Numerically: −9.86997 (δ = 1e−4), −9.869608 (1e−6, i.e. X_A = 13.8), −9.8696044 (1e−8, 1e−12).
Direct 2D quadrature agrees. The whole difference comes from the excluded corner x ∈ (1−δ,1): 12∫ln(1+δȳ/y)dy/y → 12·π²/12.
The double cutoff is symmetric under (x,y) → (ȳ,x̄), so the r2 term shifts identically and A_3^i → A_3^i − π²·πα_s(r_χ^{M1} − r_χ^{M2}).
Reproducing the project's `si.dblquad` call gives −21.555 together with non-convergence warnings: the −21.6 is a numerical artefact.
The tex remark is also wrong where it says that "the coefficients of X_A², X_A and the constant all change": only the constant changes.
The qualitative conclusion (the X_A parametrisation is a model whose finite parts depend on the regulator) is correct. BN 2003 itself says "The treatment of weak annihilation is model-dependent in the QCD factorization approach",
and BBNS 2001 says "taking the same value of X_A for all annihilation terms is a crude model".

**Verdict N22: refuted as stated** (the numerical claim). The corrected statement is given in the structured output.

---

## 6. N23 — own proofs of classical facts

- **Thm 7.2.** The substitution h(t) = ½t^{k₀−½}g(√t) maps the even-moment tail onto all moments (checked, including singular g). Then Lemma 7.1 (Weierstrass/Riesz) applies.
  The proof is correct. (k₀ = 0 also works, although the statement says k₀ ≥ 1.)
- **Cor. 7.3.** a_N = ∫x^{N−1}[q + (−1)^N q̄] (checked). The conclusions follow.
- **Prop. 7.5.** ∫x^{N−1}[1/(1−x)]_+ = −(ψ(N)+γ_E) and the large-N argument are correct (|∫x^{N−1}r| ≤ C/(N−1)).
- **Prop. 7.7.** Each step checks: |z+1| ≥ max(1,|z|) on Re z > 0; the Cayley map; 1 − |w_k| = 2/(x_k+1); the divergent Blaschke sum; Jensen's inequality (and the bound on Ψ).
  It is the classical Blaschke condition for bounded functions in a half plane; with a polynomial bound it covers all moment applications. Correct.
- **Müntz L² distance.** The Gram-determinant ratio equals (2λ+1)^{−1}Π(λ−λ_k)²/(λ+λ_k+1)² exactly (sympy rationals, three cases) and agrees with direct least squares.
  The Euler product gives π/sinh(√3π) = **0.0272282** (partial products converge like 1/K). It should be printed 0.02723, not 0.02722. The x vs {x^{2k}} rate K^{−3/2} is confirmed (slope 1.4996).
- **Carlson.** sin(πN/2) (type π/2) and (1−cos πn)/2 (type π) are correct borderline/counter-examples. Waldschmidt arXiv:2002.01223v1 cites Carlson's theorem
  ("no nonzero entire function f of exponential type < π satisfying f(ℕ) = {0}") at "[Titchmarsh §5.81], ... [Boas Th. 9.2.1]". The locations are verified through this citation. The half-plane form printed in c_pdf Thm 7.6 is the standard one; it was not checked against the books themselves.
- **ERBL (c_exclusive §3.3).** Hermiticity V(x,y)yȳ = V(y,x)xx̄ holds (the δ-terms are trivially symmetric). Triangularity: M_k(y) = ∫dx(x^k − y^k)V(x,y) is a polynomial of degree ≤ k for k = 0…12 (exact), e.g. M_1 = −2(2y−1)/3.
  For general k the y^{k+1} coefficients of the two regions are ±(1/(k+2) − ½) and cancel. This is an algebraic proof that complements the boost-weight argument.
  V acting on yȳC_n^{3/2}(2y−1) gives v_n xx̄C_n^{3/2}(2x−1) with v_n = −½ + 1/((n+1)(n+2)) − 2Σ_{j=2}^{n+1}1/j = ∫z^nP_qq/C_F (n ≤ 6, exact). The proof (self-adjoint + flag-preserving ⇒ orthogonal-polynomial eigenbasis) is correct.
- **REVIEW counterexamples.** |∫x^n sin(Q²x)| ≤ (n+2)/Q² with sup = 1; ⟨δ′, x^{2m}⟩ = 0 for all m, ⟨δ′, x⟩ = −1; (1−cos πn)/2 = 0 on even n. All correct.

**Verdict N23: confirmed** (with the rounding fix).

---

## 7. N24 — R_{e+e−} finiteness route and the exact cutting identity

**Logic of thm:ee-R-finite.** At fixed order in α_s(μ), every bare (k+1)-loop massless propagator term is c(ε)(μ₀²)^{kε}(−q²−i0)^{−(k+1)ε}, and the MS-bar counterterms are pure poles.
So the Laurent coefficients of Π_MS(q²;ε) are polynomials in L. Euclidean finiteness (a) kills the negative-order coefficients for all real L, hence identically. The continuation L → ℓ − iπ at fixed ε
therefore has a finite limit. The implication is rigorous. The input (a) for massless QCD is Poggio–Quinn 1976. Its abstract (read) states finiteness "for nonexceptional Euclidean momenta in any renormalizable (but not
superrenormalizable) field theory containing zero-mass particles" and the corollary "that any physical discontinuity of Green's functions is also infrared finite", which is this route.
**BM II scope:** the abstract (read) requires "all terms in the interaction Lagrangian have infrared degree Ω ≥ 4". In covariant gauges every QCD vertex has Ω = 4 (gluon and ghost IR dimension 1, including the (1−ξ)kk/k⁴ term; quark 3/2; +1 per derivative), so the hypothesis is plausibly met.
Whether BM's framework explicitly includes non-abelian gauge fields with FP ghosts could not be checked: the full text was blocked by bot checks.
Related rigorous work (abstract only): Efremov–Guida–Kopper 2017 prove perturbative renormalizability of *massless SU(2) Yang–Mills* with flow equations, "a large part of the proof is dedicated to bounds on massless correlation functions". That is not DR, and has no quarks.
The [R] grade is therefore conditional on the cited inputs, as c_ee itself says.

**Exact-in-ε cutting identity (independent).** All inputs are independent of the project's derivation:
- LHS: Grozin's published d-dimensional two-loop photon self-energy, Π_2 = e₀⁴(−p²)^{−2ε}/(4π)^d · 2(d−2)/((d−1)(d−4))[−(d²−7d+16)G₁² + 4(d−3)(d²−4d+8)/(d−4) G₂] with G₂ = G(1,1)G(1,ε).
  Mapped via Π = −Π_G/e₀² (one-loop check: Π^(0) = (Q²)^{−ε}/(4π)^{D/2}·2(D−2)/(D−1)·G(1,1)) and e₀⁴ → e₀²g₀²C_F N_c e_q², it is **identical to c_ee (4.1)** (r₁, r₂ and G(1+ε,1) = −(2−3ε)G(1,ε)/ε; 30 digits).
- RHS: own trace engine. The real-emission −g_{μν}ΣMM* equals c_ee (3.4) exactly.
  The D-dim 3-body phase space (3.5) has the correct total volume (recursion through Φ₂(s;M²,0), ratio 1 to 25 digits).
  The one-loop form factor from my traces + Feynman-parameter integrals is exactly −(α_sC_F/4π)(4πμ₀²/(−q²))^ε c_Γ (2−ε+2ε²)/(ε²(1−2ε)).
- Result: 2(D−1)s Im Π^(1)_bare = ρ_V + ρ_R to 30 digits at ε = 0.1, −0.2, 0.31, −0.43, 0.0123, term by term (G₁₁² ↔ ρ_V, G₁₁G(1+ε,1) ↔ ρ_R). The LO normalisation 2(D−1)s Im Π^(0) = ρ₀ also holds.

**Π_MS.** From Grozin's formula with MS-bar (μ_MS^{2ε}, g₀² = 4πα_sμ_MS^{2ε}, pure-pole subtraction): Π^(0) = (1/12π²)(5/3 − L) and Π^(1) = (1/12π²)(α_s/π)(3C_F/4)(55/12 − 4ζ₃ − L). There is no 1/ε², and the simple pole is L-independent (local).
Checked at L = 0, 1.7, −0.6 to 30 digits. For N_c = 3 this can equivalently be written (3/16π²)[20/9 − (4/3)L + C_F(α_s/π)(55/12 − 4ζ₃ − L)] (pure algebra; I did not re-read a paper that prints this form). The prefactor is N_c Σ e_q² (e_q in units of e).

**Verdict N24: confirmed**, with the BM II caveat and the e² → e_q² notation fix.
