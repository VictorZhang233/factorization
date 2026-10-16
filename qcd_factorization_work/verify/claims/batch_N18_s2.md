# Verification batch N18, N19, N20, N21, N23, N24 (stage 2, second independent verifier)

Date: 2026-10-11. Stance: skeptical. I did not rely on the stage-1 reports (batch_N13_s1.md §7, batch_N19_s1.md). Each claim was
re-derived with my own code, using a method different from both the project's and stage 1's wherever one existed, and the
literature was re-read in the original sources.

## 0. Method, scripts, sources

**My scripts** (`verify/claims/batch_N18_s2_scripts/`, run with `python3 -I -u`; outputs in `*.out.txt` next to each script):

| script | method (how it differs from project / stage 1) | result |
|---|---|---|
| `n18_colour_exactN.py` | Birdtrack (Fierz) engine, **exact in symbolic N**. Colour space spanned by the two index pairings, Catani–Seymour charges acting through Fierz, scalar products N^{#loops}. Stage 1 used explicit numerical SU(N) matrices for N = 2…6. QVY eqs. (25)–(27) also recomputed literally as traces (SU(3), SU(4)). | 63/63 PASS |
| `n19_glauber_s2.py` | (i) exact polynomial identity (N ≤ 5), a symbolic induction step for all N, the E integral by exact residues; (ii) **exact rational arithmetic** in a Cartan–Weyl basis (no square roots): SU(3) 3, 3̄, 8, 6 and SU(2) spins ½…2 in a polynomial basis; (iii) exact residue, Hankel transform, sign fixed by the classical Yukawa line integral; (iv) **exact closed form** 1−P = (N²−1)/N² sin²(d/2) from projectors, checked against explicit matrices. | 61/61 PASS |
| `n20_vertex_s2.py` | (A) the DY−SIDIS **difference** computed directly from δ(n·l): a Euclidean (D−1)-dim integral in the rest frame of time-like n, and a Minkowski (D−1)-dim bubble for space-like n; (B) my own Feynman/Schwinger parametrisation with λ = (x/\|a\|)u; (C) the exact representation FT(z) = 4π∫₀^∞ sin s·arcsinh(s/z)/s² ds, which I derived. | 47/47 PASS |
| `n21_ils_s2.py` | **Mellin transform / residues**: R(c) = P(UV < c), M_W = M_U², f_W = Σ residues. Cross-checked by 1D quadrature of ∫f(u)F(c/u)du and by Monte Carlo. | 25/25 PASS |
| `n23_math_s2.py` | substitution identity (symbolic plus singular numerics), Mellin of the plus distribution, Blaschke divergence, Jensen formula, Müntz distance by **high-precision least squares and quadrature** (not Gram determinants), ERBL triangularity/eigenvalues, the REVIEW counterexamples incl. their exponential types | 46/46 PASS |
| `n24_twoloop_s2.py` | **own two-loop computation of Π^(1)_bare**: own D-dim trace engine (pairing recursion plus index-chain contraction), own integral evaluator (triangle rule; nested and factorised one-loop tensor integrals from the Feynman-parameter tensor formula, re-derived here). Also own one-loop form factor, own real-emission trace and D-dim 3-body phase space. Then the cutting identity, and the MS-bar Laurent coefficients by contour integrals. Stage 1 took Π^(1) from Grozin's published formula. | 51/51 PASS |

**Project scripts re-run unchanged** (outputs in `batch_N18_s2_scripts/rerun/`): colour_factors 32/32, glauber_poles 22/22, unitarity_cuts 58/58,
ss_exchange 23/23, diffraction 12/12, virtual_vertex PASS, s4_pion_ff 20/20, s6_uniqueness 15/15, s3_erbl_eigen 21/21,
cut_identity_analytic X1 PASS, pi_twoloop 18/18.

**Literature read in this session** (downloads kept as untrusted data in the scratchpad; TeX sources were compiled with `latex -no-shell-escape`
only to read equation numbers from the `.aux` files):
- Bacchetta–Bomhof–Mulders–Pijlman, hep-ph/0505268v2 = PRD 72 (2005) 034030. Compiled: QuarkQuark = (A11), QuarkQuarkA = (A11a), QuarkAntiquark = (A12),
  ToddCors = (B3), qqToddCors = (B5), qANTIqToddCors = (B6), TABLE = Table I.
- Qiu–Vogelsang–Yuan, arXiv:0706.1196v1 = PRD 76 (2007) 074029. Compiled: e25–e27 = (25)–(27), hqq = (28), the diagram figure is Fig. 8; Table I.
- Collins–Qiu, arXiv:0705.2141v2: eq:eik1–3 = (4.1)–(4.3) (compiled). Collins, arXiv:0708.4410v1, eq. (2) (source).
- Liu–Ringer–Vogelsang–Yuan, arXiv:2008.03666 (source). Ratcliffe–Teryaev, hep-ph/0703293 (source). Buffing–Mulders, arXiv:1105.4804 (source).
  J. Zhou, arXiv:2610.11258 (source; double-Sivers only). INSPIRE full-text queries ("gluonic pole" and "color charge", 15 hits; titles screened).
- Collins, *Foundations of Perturbative QCD*, OA reissue (Cambridge Core chapter PDFs, chs. 10, 13, 14): §10.6.4 pp. 349–350; §10.8.2 pp. 361–362;
  §10.11.1 p. 381; Exercise 13.8 p. 538; §14.4.3 eqs. (14.29)–(14.30) p. 559.
- Yeh, hep-ph/0107192v2 (source, §IV); Brodsky–Ji–Pang–Robertson, hep-ph/9705221 (source); Waldschmidt, arXiv:2002.01223v1 (source).
- Breitenlohner–Maison II, CMP 52 (1977) 55–75: **full text read** (Project Euclid open-access PDF; text extracted). BM I/II abstracts: INSPIRE.
- **Not accessible:** Isgur–Llewellyn Smith NPB 317 (1989) 526 (CERN CDS bot challenge; ScienceDirect JS challenge) and the KEK scan of the 1984 preprint
  (request rejected). I made no attempt to get around these blocks.

## 1. Summary

| id | verdict | corrections needed before printing | already in the literature |
|---|---|---|---|
| N18 | **confirmed** | Labels only: uu*, tu* belong to qq→qq (identical quarks); st* is the s–t interference of q q̄ → q q̄ (same flavour), not of q q̄ → q′q̄′. All values are right. | Channel values: BBMP Table I, (B5), (B6); QVY Table I, (25)–(28). The attachment rule in Wilson-line language: Buffing–Mulders 2011; qualitative "colour charge of the ISI/FSI parton": Ratcliffe–Teryaev 2007. The compact form 1+2⟨T_a·T_b⟩/C_F was not found (INSPIRE full-text, LRVY 2020; not exhaustive). |
| N19 | **confirmed** | (iv) must carry "for U = exp(i d T_q·T_B) (leading order in d)" or "to second order in the phases". Exact: 1−P_singlet = (N²−1)/N² sin²(d/2). With a common phase χ₀ the δ² coefficient is smaller (0.2156 at χ₀ = 0.4; 0.1836 at χ₀ = 1). | (i) Collins 2011 eqs. (14.29)–(14.30), p. 559, at i0. **(14.30) as printed has the overall sign reversed** (re-checked here). (ii) A one-line Lie-algebra identity (standard). (iii) The standard eikonal phase. (iv) Toy model; not found. |
| N20 | **confirmed** | The remainder FT is **not exactly** 2π²/(Λ_Bb_T): it equals 2π²/z + O(e^{−z}), z = Λ_Bb_T (18.234 vs 19.739 at z = 1). Cite Collins 2011 §10.6.4 (pp. 349–350), §10.8.2, §10.11.1 (p. 381), Ex. 13.8 (p. 538), not "§10.8" alone. | Mechanism stated qualitatively in Collins–Metz 2004 and Collins 2011 §10.6.4/§10.11.1; Ex. 13.8 poses the question. The explicit one-loop relations were not found. |
| N21 | **confirmed** (formulas and numbers) | Do not claim novelty for the closed forms; ILS 1989 is unread. The concept of the fraction is ILS's (Yeh 2001 §IV). | ILS fraction function f(ε) = 1−R(ε): Yeh 2001 quotes ILS's "90% at ε = 1/150" (asymptotic DA); our formula gives 0.892. No closed form in Yeh 2001 or BJPR 1997. |
| N23 | **confirmed** | (a) π/sinh(√3π) = 0.0272282: print 0.02723, not 0.02722. (b) REVIEW L4: (1−cos πn)/2 = sin²(πn/2) has type π, so it does **not** show that "from even integers one needs c < π/2". The sharp counterexample is sin(πn/2) (type π/2), as c_pdf §7.5 already says. | All classical (Hausdorff, Müntz–Szász, Blaschke/Jensen, Carlson: Titchmarsh §5.81, Boas Th. 9.2.1 via Waldschmidt, verified). |
| N24 | **confirmed** | Write N_c Σ_q e_q² (e_q in units of e) instead of "N_c e²". BM II scope: the hypotheses are met by massless QCD in covariant gauge, ghosts included. BM name YM + fermions explicitly; they do not discuss ghosts explicitly; their result is distributional (see §7.4). | Route: the Poggio–Quinn 1976 corollary. The two-loop d-dim Π is standard (Grozin hep-ph/0508242, per stage 1); 55/12 − 4ζ₃ is standard. |

---------------------------------------------------------------------------------------------------------

## 2. N18 — gluonic-pole strength C_G = 1 + 2⟨T_a·T_b⟩/C_F

### 2.1 Pole rule (derived)
A gluon of momentum l (collinear to hadron 1, coupling through A⁺) leaves the spectator of hadron 1 and attaches eikonally to a line of the hard part.
- Outgoing line of momentum k: denominator (k−l)² + i0 ≈ −2k⁻l⁺ + i0, i.e. 1/(−l⁺+i0) = −PV(1/l⁺) − iπδ(l⁺). Colour t^a on the line, CS charge T = t.
- Incoming quark of momentum p: (p+l)² + i0 ≈ 2p⁻l⁺ + i0, i.e. 1/(l⁺+i0) = PV(1/l⁺) − iπδ(l⁺). Colour t^a acts on the incoming index as (t^a)^T,
  i.e. as −T_b with T_b = −t^T.
- The pole parts are therefore equal, −iπδ·g t^a, for incoming and outgoing quark lines; the principal parts differ.

In CS charges the pole parts sum to P = Σ_out T − Σ_{in, ≠a} T. Colour conservation Σ_all T = 0 then gives P = −T_a − 2T_b, for any number of
outgoing partons. This agrees with Collins–Qiu (4.1)–(4.3), read in the source: k4 (outgoing) and k2 (incoming), both of charge g₂, each give iπg₂δ(l⁺),
"for a total of iπ(g₁+2g₂)δ(l⁺)". It also agrees with Collins 2007 eq. (2): g₂/(l⁺+iε) + g₂/(−l⁺+iε) + g₁/(−l⁺+iε).
Normalising to SIDIS (P = T_c = −T_a, value C_F): C_G = ⟨(−T_a)·P⟩/C_F = 1 + 2⟨T_a·T_b⟩/C_F. The overall sign of the spectator charge cancels in this ratio.
SIDIS: +1. DY (T_a + T_b = 0): −1. Both reproduced exactly.

### 2.2 Exact-in-N results (`n18_colour_exactN.py`, 63/63)
Amplitudes: M_t = t^x_{ca}t^x_{db} = ½(S − I/N), M_u = ½(I − S/N) (qq→qq); M_t = t^x_{ca}t^x_{bd}, M_s = t^x_{ba}t^x_{cd} (q q̄). Colour conservation
Σ_j T_k·T_j|M⟩ = 0 was verified symbolically for every leg.

| channel | ⟨T_a·T_b⟩ (exact) | C_G (pole rule = closed form = BBMP Table I) | SU(3) |
|---|---|---|---|
| qq tt*, uu* | −1/N | (N²−5)/(N²−1) | 1/2 |
| qq tu* | −(N²+1)/(2N) | −(N²+3)/(N²−1) | −3/2 |
| q q̄ tt* | −(N²−2)/(2N) | −(N²−3)/(N²−1) | −3/4 |
| q q̄ ss*, st* | 1/(2N) | (N²+1)/(N²−1) | 5/4 |

**QVY Table I** (read in the source): all 24 entries (C_u, C_I, C_F1, C_F2 for diagrams (1)–(6)) are reproduced **exactly in N**. The normalisation is
C_u = ⟨M|M′⟩/N² and C_X = C_u⟨M|(−T_a)·(σ_X T_X)|M′⟩/C_F, with σ = +1 out and −1 in. F1 is the jet on the polarised quark's line in the t-channel graph,
F2 the other jet. Diagram (1): C_I/C_u = −2/(N²−1), C_F1/C_u = −1/(N²−1), C_F2/C_u = (N²−2)/(N²−1) (SU(3): −1/4, −1/8, 7/8). The sum
(N²−5)/(4N²) is eq. (28). QVY's literal traces (25)–(27) also give −1/(2N²), −1/(4N²), (N²−2)/(4N²) for SU(3) and SU(4).
BBMP's own link algebra ((A11), (A12) with Table I upper part: C_G[U±] = ±1, C_G[U□U⁺] = 3, C_G[Tr U□ U⁺/N] = 1) gives the same C_G, and every link is
normalised to 1. The QVY antiquark diagrams (4)–(6), where QVY insert extra signs for antiquark eikonal propagators, also follow from the CS form of the rule.

**Labelling.** BBMP label the channels "qq: tt*, uu*, tu*, ut*" and "q q̄: tt*, ss*, st*, ts*". The interference st* exists only for q q̄ → q q̄ of the
same flavour, and uu*, tu* only for identical quarks. The claim's "q q̄ → q′q̄′ ss*, st*" should read "q q̄ → q′q̄′ (ss*) and q q̄ → q q̄ (st*)". The values
are unaffected.

**Literature/novelty.** The channel values are BBMP's and QVY's. Ratcliffe–Teryaev 2007 (hep-ph/0703293) say in words that "the colour factor is defined
by the colour charge of the parton participating in the ISI and FSI". Their numbers −1/(2N_c) and N_c/2 for high-p_T SIDIS are exactly ⟨−T_a·T_X⟩.
Buffing–Mulders 2011 build the links from Wilson lines "stuck" at the external partons; this is the same rule in Wilson-line language. LRVY 2020 use
QVY's C's. I did not find the compact form 1 + 2⟨T_a·T_b⟩/C_F stated explicitly. **Verdict: confirmed.**

---------------------------------------------------------------------------------------------------------

## 3. N19 — further c_glauber results (`n19_glauber_s2.py`, 61/61)

**(i)** With u_f = (a_f+iε)⁻¹ and v_f = (a_f−iε)⁻¹: S_{N+1} = v_{N+1}S_N + i(u_{N+1}−v_{N+1})Π_{f≤N}u_f. If S_N = i(ΠU − ΠV), then
S_{N+1} = i(Π_{N+1}u − Π_{N+1}v). This induction step was checked symbolically, so the identity holds for all N. It was also checked as an exact polynomial
identity for N ≤ 5 and numerically for N ≤ 12 (240 random configurations, 9e−15). ∫dE/2π of the right-hand side is 1 for N = 1 and 0 for N ≥ 2 (exact residues).
**Collins 2011, p. 559, read myself.** (14.29) is exactly the cut sum, Σ_c[Π_{f>c}(a_f−i0)⁻¹]2πδ(a_c)[Π_{f<c}(a_f+i0)⁻¹]. (14.30) states "the integrand equals
iΠ(a_f−i0)⁻¹ − iΠ(a_f+i0)⁻¹". At N = 1 this gives −2πδ(a), so the overall sign is reversed (stage 1's observation, confirmed). Collins's conclusion is
unaffected. The project's finite-ε version has the correct sign. Novelty: none (it is the ε-regulated (14.30)).

**(ii)** X − L = T₁^aT₁^b[T₂^b,T₂^a] = (i/2)f^{bac}[T₁^a,T₁^b]T₂^c = (C_A/2)T₁·T₂. This uses only [T^a,T^b] = if^{abc}T^c in each representation, which also holds for
CS charges (−t^T). Checked with **exact rationals** (Cartan–Weyl basis, c = Σg^{ab}T₁(X_a)⊗T₂(X_b)): SU(3) 3×3, 3×3̄, 3×8, 8×8, 3̄×6, 6×8, 6×6 and
SU(2) spin ½×½, ½×3/2, 1×2, 3/2×3/2, 2×2. Casimirs 4/3, 3, 10/3 came out exact. [T_A·T_B, T_A·T_j] ≠ 0 on 3̄⊗3̄⊗3, with basis-independent norm √3 = 1.732.

**(iii)** ∫dk⁻/2π (ie_A2p′⁺)(i/D_sA)(i/D_a) = (ie_A)[i/D_a] at the spectator pole (exact residue). With −i/(k²−m²)|_{k²=−k_T²} this gives
V = −ie_Ae_B/(k_T²+m_g²). The Hankel transform gives Ṽ(b) = −ie_Ae_BK₀(m_gb)/(2π) = iχ. Sign: the straight-line integral of the repulsive Yukawa
potential e_Ae_Be^{−mr}/(4πr) is K₀(mb)/(2π). So χ = −e_Ae_BK₀/(2π) < 0 for like charges, as it should be.

**(iv)** Exact, from projectors (Tr_q P_R = (d_R/N)1_B): 1 − P_singlet = (N²−1)/N² · sin²(d/2) for U = e^{idT_q·T_B}. This agrees with explicit matrices
for N = 2…5 and d = 0.05, 0.7, 2.1. The leading coefficient is C_F/(2N) = 2/9 for SU(3). For U = exp(i(χ₁T_q+χ₂T_q̄)·T_B) the second-order leakage is
(χ₁−χ₂)²C_F/(2N). But at a common phase χ₀ the δ² coefficient is C_F/(2N)⟨sinc²⟩: 0.215644 at χ₀ = 0.4 and 0.183578 at χ₀ = 1. Hence the qualifier.
**Verdict: confirmed** (with the qualifier in (iv)).

---------------------------------------------------------------------------------------------------------

## 4. N20 — time-like vs space-like regulator lines (`n20_vertex_s2.py`, 47/47)

Set-up: V = ig²C_Fμ^{2ε}∫d^Dl/(2π)^D N/[(n·l ∓ i0)(l²+i0)((p−l)²+i0)], with −i0 for SIDIS and +i0 for DY. The rules W[±∞n,0] ⊃ gn·Ã/(n·l ∓ i0) were re-derived
from the binding convention, with l the momentum flowing into the line. Covariantly, N = 2p·n − 2l·n + (l·p)n²/(p·n); in the light-cone frame this equals
2n⁻(p⁺−l⁺).

**(B) Direct parametrisation (own).** Combine the quadratic propagators with x and the linear one with 1/(QA) = ∫₀^∞dλ 2/(Q+λA)³. This is legitimate when
both have +i0, so for SIDIS rewrite 1/(n·l−i0) = −1/(−n·l+i0). Wick-rotate with Δ_S = 2xλ(p·n) + λ²n² and Δ_D = −2xλ(p·n) + λ²n², then substitute
λ = (x/|a|)u, with n² = 2a and p·n = 1. Results:
V_SIDIS^time = −(α_sC_F/4π)(πμ²n²/(p·n)²)^ε Γ(1−ε)Γ(1+2ε)(1−ε)/((1−2ε)ε²) ≡ V^time (real, since Δ_S > 0),
V_DY^time = e^{2πiε}V^time, V_SIDIS^space = e^{−iπε}V^time, V_DY^space = e^{iπε}V^time (Δ_D < 0 everywhere).
All agree to 30 digits at seven values of ε.

**(A) Difference method (new).** V_DY − V_SIDIS = 2πg²C_Fμ^{2ε}∫d^Dl/(2π)^D N δ(n·l)/[(l²+i0)((p−l)²+i0)].
- Time-like n, rest frame: δ(l⁰). Then N = n₀(2E−l_z), l² = −l⃗², (p−l)² = 2E l_z − l⃗². The remaining integral is
  E^{−2ε}∫d^{3−2ε}k (2−k_z)/[k²((k−ẑ)²−1−i0)] = −ie^{iπε}π^{d/2}Γ(½+ε)(1−ε)/(ε(1−2ε)). The −i0 mass term gives the phase; a contour check is included.
  Result: V_DY − V_SIDIS = −ie^{iπε}(α_sC_F/(2√π))(4πμ²n²/(p·n)²)^εΓ(½+ε)(1−ε)/(ε(1−2ε)).
  Duplication and reflection give 4^ε√πΓ(½+ε)ε = sin(πε)Γ(1−ε)Γ(1+2ε), so this is **exactly (e^{2πiε}−1)V^time**.
- Space-like n: δ(l_z). On the hyperplane the integral is a Minkowski bubble with M² = p_∥² = (p·n)²/|n²| and Feynman Δ = x²M² > 0, so it is purely
  imaginary: **V_DY − V_SIDIS = 2i sin(πε)V^time(|n²|)**.
- Both directions are also consistent with analyticity: V_σ(n²) is analytic for Im n² < 0, since Δ − i0 and n² − i0 have the same sign of Im.

**Consequences.** Space-like lines: V_SIDIS = (V_DY)* exactly. Time-like lines: Re V_DY − V_SIDIS = −2sin²(πε)V^time = (α_sC_F/4π)[2π² + 2π²(1−γ_E)ε + …],
times X^ε → 1. Im V_DY^time = (α_sC_F/4π)(−2π/ε + …) is the divergent Coulomb phase. Everything is ∝ |n²|^ε, so it vanishes when the light-like limit is
taken first (Re ε > 0).

**Interpretation, checked.** W[−∞n,0] with time-like n puts earlier times to the left, so it is anti-time-ordered. The factorisation and Feynman-rule object
is T-ordered. PT preserves operator order, so it maps the SIDIS operator (path order = time order) onto the path-ordered DY operator, which is not the
T-ordered one. For space-like n all points are mutually space-like (and space-like to 0), so the orderings coincide. The statement is correct "at finite
rapidity".

**Remainder FT.** D(κ) = ln(1+κ²) + 2κ arctan(1/κ) is exactly the exact-minus-limit (checked). Since D′ = 2arctan(1/κ) and
arctan(1/t) = ∫₀^∞e^{−st}sin s/s ds, one gets **FT(z) = 2π∫₀^∞dκ J₀(κz)D/κ = 4π∫₀^∞ sin(s) arcsinh(s/z)/s² ds**. Numerically (Hankel = representation):

| z = Λ_Bb_T | 0.5 | 1 | 2 | 5 | 10 | 20 |
|---|---|---|---|---|---|---|
| FT(z) | 31.6667 | 18.2342 | 9.71400 | 3.946643 | 1.9739191 | 0.98696044009 |
| 2π²/z | 39.4784 | 19.7392 | 9.86960 | 3.947842 | 1.9739209 | 0.98696044011 |

So FT = 2π²/z + O(e^{−z}). This suffices for Λ_B → ∞ at fixed b_T, but the printed "equals" must become "→ 2π²/(Λ_Bb_T), up to exponentially small terms".

**Literature (read).** Collins 2011 §10.6.4, pp. 349–350: "since gluon fields commute at space-like separation, the use of space-like Wilson lines ensures
automatic compatibility between the path ordering defining the Wilson lines and the time ordering used to define Green functions"; also "If one gave up
the argument about universality, one could use time-like auxiliary vectors … need further investigation". §10.8.2, pp. 361–362: the order of limits.
§10.11.1, p. 381: "the path ordering on the lines creates no conflict with the time ordering". **Exercise 13.8 (***), p. 538** asks exactly whether time-like lines
give problems. **Verdict: confirmed** (with the FT and citation corrections).

---------------------------------------------------------------------------------------------------------

## 5. N21 — Isgur–Llewellyn Smith soft fractions (`n21_ils_s2.py`, 25/25)

Write u = x̄ and v = ȳ. Then R(c) = P(UV < c) for iid U, V with density f ∝ φ(1−u)/u.
- Asymptotic DA: f = 2(1−u), M_U(s) = 2/(s(s+1)), M_W = M_U², f_W(w) = Σ Res M_W w^{−s} = −4(1+w)ln w − 8(1−w). Hence
  R_as(c) = ∫₀^c f_W = c[5c − 2(c+2)ln c − 4], exactly as claimed.
- CZ DA: f = 6(1−u)(1−2u)², M_U = 6(s²−3s+6)/(s(s+1)(s+2)(s+3)), f_W = −(576w³+2304w²+900w+36)ln w + 1680w³+288w²−1800w−168. Hence
  R_CZ = c[456c³+352c²−675c−132 − (144c³+768c²+450c+36)ln c], exactly as claimed.
- R(1) = 1; R′ = f_W ≥ 0 and R′(1) = 0; R ~ f(0)²c ln(1/c), i.e. 4c ln(1/c) (as) and 36c ln(1/c) (CZ).
- The 1D quadrature agrees to 1e−20 and the Monte Carlo (2·10⁶) to within statistics.
- Numbers (μ₀² = 1 GeV², Q² = 4, 10, 100): as 0.872081, 0.617086, 0.145628; CZ 0.975251, 0.900082, 0.481494. These round to the quoted values.

**Literature.** Yeh 2001 §IV (read): ILS "employed the fraction function f(ε) = ∫∫θ(xy−ε)φ(x)φ(y)/(xy)", and "for the AS model f(ε) reaches 90% for ε = 1/150".
f = 1 − R, and 1 − R_as(1/150) = 0.8924. Yeh cites ILS 1984 and 1989 together. BJPR 1997 also cite ILS PLB 217 (1989) 535. I could read neither ILS paper. Stage 1
read the 1984 preprint and found no fraction function, so the attribution goes to ILS 1989. A closed form appears in neither Yeh nor BJPR. Novelty of the
closed forms cannot be asserted. **Verdict: confirmed.**

---------------------------------------------------------------------------------------------------------

## 6. N23 — own proofs of classical facts (`n23_math_s2.py`, 46/46)

- **Thm 7.2.** t^m h(t)dt = x^{2(m+k₀)}g(x)dx exactly (symbolic, for every k₀ ≥ 0). With singular g (α = 0.3, β = −0.6) the t-side quadrature matches the
  exact Beta values. Lemma 7.1 (Weierstrass + Riesz; L¹ variant via Lebesgue differentiation) is correct. Null sets are preserved by √ on (0,1). Correct.
- **Cor 7.3.** a_N = ∫x^{N−1}[q + (−1)^N q̄], with f_q(−ξ) = −q̄(ξ) (checked N = 1…6). The (q+φ, q̄−φ) pair has equal even and different odd moments. Correct.
- **Prop 7.5.** ∫x^{N−1}[1/(1−x)]₊ = −(ψ(N)+γ_E), checked at non-integer N as well. |∫x^{N−1}r| ≤ C/(N−1). The large-even-N fit recovers a = 1.9998, b = 1.498
  for P_qq/C_F. Correct.
- **Prop 7.7.** |z+1| ≥ max(1,|z|); the Cayley map; 1−|w_k| = 2/(x_k+1); Σ diverges like (2/d)ln K (checked for d = 1, 2, ½). Jensen's formula was checked
  numerically. Ψ = Φ/w^j stays bounded by M (maximum principle). log(1/s) ≥ 1 − s gives the contradiction. This is the classical Blaschke condition: correct.
- **Müntz L² distance.** (2λ+1)^{−1/2}Π|λ−λ_k|/(λ+λ_k+1) equals the least-squares distance for 12 random non-integer exponent sets (rel. dev 5e−43) and the
  quadrature of the residual. x vs {x^{k²+1}}: (1/√3)Π k²/(k²+3) = π/sinh(√3π) = **0.0272281954**, which rounds to **0.02723**; "0.02722" is a truncation.
  x vs {x^{2k}}: rate K^{−3/2}.
- **ERBL (c_exclusive §3.3).** Hermiticity V(x,y)yȳ = V(y,x)xx̄ holds. Triangularity holds exactly for k ≤ 10. For general k the x^{k+1} coefficients of the
  y<x and y>x regions are ±(1/(k+2) − ½) and cancel (hand derivation), which completes the "boost-weight" argument algebraically. Eigenvalues for n ≤ 8:
  v_n = −½ + 1/((n+1)(n+2)) − 2Σ_{j=2}^{n+1}1/j = ∫z^n[(1+z²)/(1−z)]₊ (the plus distribution already contains (3/2)δ). Self-adjoint + flag-preserving ⇒
  Jacobi P^{(1,1)} ∝ C^{3/2}. Correct.
- **REVIEW counterexamples.** |∫₀¹x^n sin(Q²x)| ≤ 2/Q² uniformly in n (by parts), while sup = 1. ⟨δ′, x^{2m}⟩ = 0 for all m, ⟨δ′, x⟩ = −1.
  (1−cos πn)/2 = 0 on even n and 1 on odd n. **But** its type on the imaginary axis is π (measured 3.07 at y = 20 → π), so it already violates Carlson's c < π.
  It therefore does not show that "from even integers one needs c < π/2". The sharp counterexample is sin(πn/2) (type π/2), which is what c_pdf §7.5 uses.
- **Carlson location.** Waldschmidt arXiv:2002.01223v1 (source) writes that Carlson's theorem "states that there is no nonzero entire function f of
  exponential type < π satisfying f(ℕ) = {0} — see for instance [Titchmarsh §5.81], [Gelfond], [Boas Th. 9.2.1], [Boas–Buck IV §19]". Verified.
  The half-plane form printed in c_pdf Thm 7.6 was not checked against the books.

**Verdict: confirmed** (with the 0.02723 and L4 corrections).

---------------------------------------------------------------------------------------------------------

## 7. N24 — R_{e+e−} finiteness route and exact cutting identity (`n24_twoloop_s2.py`, 51/51)

### 7.1 Logic of thm:ee-R-finite
At order α_s(μ)^n, Π_MS^(n) = Σ_m [Laurent series from Z_α^k] × c_m(ε)e^{−(m+1)εL} + (pure-pole, q-independent counterterm). So every Laurent coefficient
is a polynomial in L. Euclidean finiteness makes the negative-order coefficients vanish for all real L, hence identically. Since e^{−kεL} is entire in L, the
continuation L → ℓ − iπ at fixed ε has the finite limit P₀(ℓ − iπ). The implication is correct and complete given input (a). The DR-cut identification is
honestly graded [A].

### 7.2 Own two-loop Π^(1)_bare (independent of c_ee and of Grozin)
- Normalisation chain: Π^{μν} = i∫e^{iqx}⟨Tjj⟩, which gives Π^{μν}_{1-loop} = iN_ce_q²∫Tr[γ^μk̸γ^ν(k̸−q̸)]/(k²(k−q)²) and Π^{μν}_{2-loop} = g²C_FN_ce_q²∫∫Tr/(…)
  (i·(−1)·i⁴·(ig)²·(−i) = g²).
- The one-loop normalisation 2(D−2)/(D−1)G(1,1) is reproduced at five ε values.
- Traces: V = [μ,k,α,r,μ,r−q,α,k−q], S1 = [μ,k,α,r,α,k,μ,k−q], S2 = [μ,k,μ,k−q,α,r−q,α,k−q].
- Integrals: triangle rule (D−a₁−a₂−2a₅)F = a₁[F(1⁺5⁻)−F(1⁺3⁻)] + a₂[F(2⁺5⁻)−F(2⁺4⁻)] (re-derived). The factorised and nested sectors use the one-loop
  tensor formula A(m,t) = Γ(α+β−D/2−t)Γ(D/2−α+m−t)Γ(D/2−β+t)/(2^tΓ(α)Γ(β)Γ(D−α−β+m)), re-derived with Feynman parameters.
- Results at ε = 1/10, −1/5, 31/100, −43/100, 123/10000, 7/30: **Π^(1)_bare = N_ce_q²C_Fg₀²(Q²)^{−2ε}/(4π)^D [r₁G(1,1)² + r₂G(1,1)G(1+ε,1)]** to 37–41 digits,
  with c_ee's r₁, r₂. **Transversality q_μq_νΠ^{μν} = 0 exactly.** F(1,1,1,1,1) → 6ζ₃.

### 7.3 Cut side (own) and the identity
- Form factor from my traces and the integrals J(1,1,1) (Feynman parameters), J(0,1,1), J(−1,1,1):
  F^(1) = −(α_sC_F/4π)(4πμ₀²/(−s−i0))^εc_Γ(2−ε+2ε²)/(ε²(1−2ε)) exactly (four values of ε).
- Real emission: my D-dim trace equals 8(1−ε)[(1−ε)(y₁₃/y₂₃+y₂₃/y₁₃) + 2y₁₂/(y₁₃y₂₃) − 2ε] on y₁₂+y₁₃+y₂₃ = 1. dΦ₃ = s^{1−2ε}(y₁₂y₁₃y₂₃)^{−ε}dy₁₃dy₂₃/(2(4π)^{3−2ε}Γ(2−2ε)),
  with the total volume checked against the recursion ∫dM²/2π Φ₂(s;M²,0)Φ₂(M²).
- **2(D−1)s Im Π^(1)_bare = ρ_V + ρ_R** to 37–41 digits at five values of ε, term by term (r₁G₁₁² ↔ ρ_V, r₂G₁₁G₁₊ε,₁ ↔ ρ_R). The LO relation ρ₀ = 2(D−1)s Im Π₀
  also holds.

### 7.4 MS-bar constants and the BM II scope
- Laurent coefficients by contour integrals (|ε| = 0.1, 40 digits), in units (α_s/π)C_FN_ce_q²/(12π²): no 1/ε²; a local pole 3/(8ε); finite part
  55/16 − 3ζ₃ − (3/4)L = (3/4)(55/12 − 4ζ₃ − L), at L = 0, 1.7, −0.6. One loop: pole 1/ε, finite 5/3 − L. So
  **Π_MS = N_cΣe_q²/(12π²)[5/3 − L + (α_s/π)(3C_F/4)(55/12 − 4ζ₃ − L)]**, and R = N_cΣe_q²(1 + (3C_F/4)α_s/π).
- **BM II (CMP 52 (1977) 55), read in full text.** Fields are characterised only by the small-p behaviour of their propagators, with IR degree Δ_φ (1 for a
  massless scalar). The theorem requires every interaction monomial to have degree ≥ 4. In covariant gauge every QCD monomial has degree 4: q̄Aq is
  3/2+3/2+1; A³∂ and A⁴ are 4; c̄∂(Ac) is 1+1+1+1. So the hypotheses hold, ghosts included. BM explicitly list "QED, Yang–Mills field + fermions without
  axial coupling" (p. 57) and "QED, the Goldstone model and certain non-abelian gauge theories" (§6, pp. 73–74) as cases where the IR subtractions cancel
  through Ward identities ("absence of IR-counterterms"). FP ghosts are **not discussed explicitly**. The existence result is distributional (Thm 2: "as a
  distribution"). For the two-point function this is enough given the explicit (Q²)^{−kε} structure, and the pointwise non-exceptional-momentum statement
  is Poggio–Quinn's. The "[to verify]" can therefore be replaced by this precise remark.
- Notation: write N_cΣ_q e_q² (e_q in units of e), not "N_c e²".

**Verdict: confirmed.**

---------------------------------------------------------------------------------------------------------

## 8. Files
- `verify/claims/batch_N18_s2_scripts/n18_colour_exactN.py` (+ `.out.txt`): exact-in-N birdtrack engine; BBMP and QVY tables; QVY literal traces.
- `verify/claims/batch_N18_s2_scripts/n19_glauber_s2.py` (+ `.out.txt`): telescoping identity (induction), exact-rational colour algebra, Glauber kernel/phase,
  exact leakage formula.
- `verify/claims/batch_N18_s2_scripts/n20_vertex_s2.py` (+ `.out.txt`): δ-function difference method, own parametrisation, 2π², FT representation.
- `verify/claims/batch_N18_s2_scripts/n21_ils_s2.py` (+ `.out.txt`): Mellin/residue derivation of R_as, R_CZ; quadrature; Monte Carlo; numbers.
- `verify/claims/batch_N18_s2_scripts/n23_math_s2.py` (+ `.out.txt`): classical-mathematics checks; rounding; exponential types.
- `verify/claims/batch_N18_s2_scripts/n24_twoloop_s2.py` (+ `.out.txt`): own two-loop correlator, form factor, real emission, cutting identity, MS-bar constants.
- `verify/claims/batch_N18_s2_scripts/rerun/`: outputs of the eleven project scripts named in the recipes.
