# Yizhuang Liu's work on the foundations of factorization
## LaMET for TMDs, Euclidean soft functions, time-ordering and analyticity, threshold limits, renormalons, exactly solvable tests — a verified report for the frontier chapter

Research deliverable for the monograph "QCD 因子化定理：严格证明、全阶论证与适用边界" (frontier chapter).
Directory: `frontier/yzliu/`. Literature checked on 2026-10-10.

| file | content |
|---|---|
| `YZLIU.md` | this report |
| `yzliu.bib` | 82 BibTeX entries. All come from INSPIRE-HEP; every entry with a DOI was cross-checked against Crossref. The manual corrections are listed in the file header and in §8. It compiles with BibTeX (`unsrt`) with no errors; the only warnings are 7 expected "empty journal" warnings for arXiv-only items. |
| `scripts/check_qtmd_1loop.py` | sympy: one-loop consistency of the quasi-TMD matching formula. Shows that the Collins–Soper exponent must carry a factor 1/2 (erratum E1). |
| `scripts/check_GammaS2.py` | mpmath: two-loop constant $\gamma_{HH}$ of the large-angle cusp anomalous dimension, from the Becher–Neubert formula with a zero-recoil cross-check (erratum E2). |
| `scripts/check_gammaC2.py` | sympy: two-loop $\gamma_C\equiv\tilde\gamma_H$ in PLB 2020 vs JHEP 2023, plus the anomalous-dimension algebra (erratum E3). |
| `scripts/check_RGE_structure.py` | sympy + numerical RGE: two-loop log structure of the kernel $H$ and of the intrinsic soft function $S_I$ (erratum E4). |
| `scripts/check_HL_and_C1.py` | sympy/mpmath: $H=C_{HL}^+C_{HL}^-$ at one loop; the final-state-sum identity (C.1) of JHEP 09 (2024) 030. |
| `scripts/check_GN_ineq.py` | mpmath: numerical test of the four inequalities (4.2)–(4.5) behind the convergence proof in the 2D Gross–Neveu paper. |
| `scripts/crossref_check.py` | Crossref cross-check of the BibTeX file. |

Citations use INSPIRE texkeys, e.g. `[Ji:2019ewn]`. Every key is in `yzliu.bib`.

---

## 0. Method, markers, rigor tags

### 0.1 What was read

All papers listed in §1.3 as relevant were downloaded from arXiv, plus the journal PDF of the 89-page Acta Phys. Polon. B lecture notes, which have no arXiv version. Their text was extracted (pdftotext). Every equation transcribed below was checked against a rendering of the original page. Depth of reading:

* **Complete (every section and appendix):** `[Ji:2019sxk]` (arXiv v3), `[Ji:2019ewn]` (v2), `[Liu:2022nnk]` (journal PDF, 89 pp.), `[Liu:2023pjb]` (v6 = published version), `[Ji:2023pba]` (v1, including Apps. A, C, D), `[Su:2026eta]` (v1).
* **Main text plus the relevant appendices:** `[Ji:2020ect]` (Secs. II, III.A–C, V.B–C; the rest skimmed), `[Ji:2021znw]` (Secs. II–V), `[Liu:2023onm]` (Secs. 1–2, 3.6, 4.3–4.4, 6), `[Liu:2024omb]` (Secs. 1–2.1, 4, 7), `[Ji:2026vir]` (Secs. 1–2, 5, 6), `[Ji:2020jeb]` (Secs. I–II, structure of III), `[Guo:2021ibg]` (Secs. I–III), `[Guo:2023pqw]` (Secs. I–II, V), `[Ji:2018waw]` (Secs. I–II, conclusion), `[Liu:2025edu]` (abstract, Secs. 1, 4), `[Liu:2025bqq]` (abstract, Secs. 1, 5).
* **Abstract, introduction and conclusions only:** `[Ji:2020brr]`, `[LatticePartonLPC:2021gpi]`, `[LatticeParton:2020uhz]`, `[Ji:2024hit]`, `[Liu:2021evw]`, `[Ji:2020bby]`, `[Kock:2020frx]`, `[Liu:2026npv]`, `[Liu:2025qsv]`.
* **Career data:** habilitation summary ("Dane osobowe i podsumowanie osiągnięć zawodowych", Aug. 2023), posted on the public information bulletin of the Jagiellonian University (`habilitacje.bip.uj.edu.pl`). Only professional data from it are used here.

### 0.2 Markers

* **[txt §x, eq. (n)]**: read in the full text at the location given.
* **[abs]**: abstract only.
* **[bib]**: bibliographic record only.
* **[chk: script]**: checked independently by my own symbolic or numerical computation (script in `scripts/`).
* **[chk-hand]**: checked by hand; the computation is given or indicated in this report.
* **UNVERIFIED**: could not be checked; do not print as fact.

### 0.3 Rigor tags (binding definitions from CONTEXT.md) and how they are used here

| tag | meaning (CONTEXT.md) |
|---|---|
| [R] 严格 | complete mathematical proof at every order of renormalized perturbation theory, or a complete proof given in the text |
| [A] 全阶论证 | standard all-order argument accepted in the literature; some steps exist only in sketch form |
| [P] 部分 | proven or verified only at fixed order, in a model, or for a subclass |
| [C] 猜想 | widely used but unproven, or the known proof has a gap |
| [V] 破坏 | known to fail |

Two conventions specific to this report:

1. **Results that are exact in a model.** An example is the 2D U(N) Gross–Neveu result at $O(1/N)$. As a statement about QCD factorization it is graded **[P]**. Its status inside the model is stated separately ("rigorous within the model, modulo …").
2. **"Conditional [R]".** A theorem that is mathematically rigorous under explicitly stated axioms (Wightman axioms, a mass gap, etc.) that have not been established for four-dimensional QCD. Such a result counts as [R] only relative to its axioms. For QCD it inherits [C] from the axioms.

Where I give a refined sub-grade (A−, A+), it only describes how close an [A] argument comes to [R] or [P]. The binding tag is the letter.

---

## 1. Identification, career, and publication map

### 1.1 Identity (verified)

* INSPIRE author record 1981577, INSPIRE BAI `Y.Liu.90`, ORCID 0000-0002-0897-1165 [bib]. The record holds 73 literature items, July 2014 – Sept. 2026. A name search (`a "Liu, Yizhuang"`) returns the same 72 items, and the BAI search adds the lecture notes `[Liu:2022nnk]`, which carry the author string "Liu, Y.".
* Three other INSPIRE author stubs named "Liu, Yizhuang" (`Y.Liu.28`, `.38`, `.68`) hold accelerator, medical-physics and mathematics papers by different people. They were excluded. Searches with coauthors (Ji, Su, Zahed, Schäfer) found no unclaimed papers.
* **Chinese name:** the form suggested in the task statement could not be confirmed from any source. **UNVERIFIED — do not print a Chinese name.**

### 1.2 Career (habilitation summary [txt], cross-checked with INSPIRE affiliations [bib])

* B.Sc. in physics, University of Science and Technology of China (USTC), 2012.
* Ph.D. in physics, SUNY Stony Brook, 18 Aug. 2018. Advisor Ismail Zahed; thesis "Non-perturbative studies in QCD". INSPIRE affiliations on papers from 2014–2018: Stony Brook.
* Postdoc at the Tsung-Dao Lee Institute (Shanghai Jiao Tong University), late 2018 – end of 2020. Member of the Lattice Parton Collaboration (LPC) until mid-2021. Papers `[H2]–[H6]` below were completed at SJTU/TDLI [txt].
* Postdoc at Universität Regensburg, late 2020 – April 2021 (with A. Schäfer).
* Jagiellonian University, Kraków: postdoctoral internship in 2021; assistant professor (*adiunkt*) at the Institute of Theoretical Physics since 2021. The 2026 papers also list the Mark Kac Center for Complex Systems Research [txt `Ji:2026vir`].
* **Habilitation series (2023).** Title (Polish original): *"Sformułowanie rozkładu partonów w przestrzeni euklidesowej: faktoryzacja, ewolucja i zastosowanie na sieci"* ("Euclidean formulation of parton distributions: factorization, evolution and lattice application"). The seven papers:
  [H1] `Ji:2021znw` (LFWFs from LaMET), [H2] `Ji:2020brr` (hybrid renormalization), [H3] `LatticeParton:2020uhz` (lattice TMD soft function), [H4] `Ji:2020ect` (RMP review), [H5] `Ji:2019ewn` (TMDPDFs from LaMET), [H6] `Ji:2019sxk` (TMD soft function from LaMET), [H7] `Ji:2023pba` (threshold resummation) [txt].
  This is the author's own choice of core output, and it matches the selection made independently in §3.
* Awards listed: Silsbee Prize (Stony Brook, 2016); Rector's Award of the Jagiellonian University for outstanding scientific achievement (2022) [txt].

### 1.3 Publication map (all 73 INSPIRE items, grouped)

**Groups I–VI relate to factorization and are analysed in §3.**

| # | key | arXiv | journal | content (one line) | read | § |
|---|---|---|---|---|---|---|
| I.1 | `Ji:2019sxk` | 1910.11415 | NPB 955 (2020) 115054 | off-light-cone TMD soft function = HQET form factor of a $Q\bar Q$ pair; $S_I$ from the meson form factor | full | A1, A5, B4 |
| I.2 | `Ji:2019ewn` | 1911.03840 | PLB 811 (2020) 135946 | quasi-TMDPDF factorization with the reduced/intrinsic soft function; RGE of the kernel | full | B1, B2, B5 |
| I.3 | `Liu:2022nnk` | — | APPB 53 (2022) 4-A2 (89 pp.) | lecture notes: leading regions, pinch poles, exponentiation, ultrasoft modes, analyticity, universality classes | full | A1–A5, B1–B4 |
| I.4 | `Ji:2020ect` | 2004.03543 | RMP 93 (2021) 035005 | LaMET review (renormalization, collinear and TMD factorization) | main | E2, E3, B |
| I.5 | `LatticeParton:2020uhz` | 2005.14572 | PRL 125 (2020) 192001 | first lattice extraction of $S_I$ and the CS kernel | intro/method | B4 |
| I.6 | `Ji:2021znw` | 2106.05310 | PRD 105 (2022) 076014 | LFWF amplitudes from LaMET; light-front quantization as an EFT | main | B3 |
| I.7 | `Ji:2020jeb` | 2011.13397 | PRD 103 (2021) 074005 | Sivers asymmetry from quasi-TMD ratios | main | B6 |
| I.8 | `Liu:2023pjb` | 2312.05957 | JHEP 09 (2024) 030 | time ordering of TMD soft factors via coordinate-space analyticity (single author) | full | A6 |
| II.1 | `Ji:2023pba` | 2305.04416 | JHEP 08 (2023) 037 | threshold factorization and resummation of the quasi-PDF matching; NNLO heavy-light Sudakov factor | full | C1–C3 |
| II.2 | `Liu:2023onm` | 2311.06907 | JHEP 02 (2024) 204 | linear IR renormalon of the heavy-light Sudakov kernel; NLP cancellation | main | C4 |
| II.3 | `Ji:2024hit` | 2410.12910 | JHEP 03 (2025) 045 | numerical effects of threshold resummation (pion) | intro | C5 |
| III.1 | `Liu:2024omb` | 2403.06787 | JHEP 09 (2024) 093 | 2D U(N) Gross–Neveu: exact Bjorken (twist) and threshold expansions; convergence theorem (single author) | main + §4 | D1 |
| III.2 | `Liu:2025edu` | 2502.02031 | JHEP 08 (2025) 014 | super-renormalizable 2D O(N): factorial enhancements, divergence of the momentum-space OPE (single author) | intro/concl. | D2 |
| III.3 | `Liu:2025bqq` | 2507.02605 | SciPost Phys. 20 (2026) 156 | NLSM trans-series from condensates (with M. Mariño) | intro/concl. | D3 |
| III.4 | `Liu:2026npv` | 2606.06277 | arXiv | NLSM free energy at fourth order vs. TBA | abs | D3 |
| IV.1 | `Ji:2026vir` | 2601.12189 | arXiv | long-distance asymptotics of Euclidean correlators; exponential-decay theorem | main + §5 | E1 |
| IV.2 | `Su:2026eta` | 2609.20545 | arXiv | computability of GPDs near $x=\pm\xi$ | full | C6 |
| IV.3 | `Ji:2020brr` | 2008.03886 | NPB 964 (2021) 115311 | hybrid renormalization; $O(\Lambda)$ ambiguity of $\delta m$ | partial | E2 |
| IV.4 | `LatticePartonLPC:2021gpi` | 2103.02965 | NPB 969 (2021) 115443 | self-renormalization on the lattice | abs | E2 |
| V.1 | `Guo:2021ibg` | 2103.11506 | PRD 103 (2021) 096010 | near-threshold $J/\psi$ photoproduction: GPD factorization at $\xi\to1$, spin-2 dominance | main | F1 |
| V.2 | `Guo:2023pqw` | 2305.06992 | PRD 108 (2023) 034003 | revised normalization (factor 2) and updated analysis | main | F1 |
| VI.1 | `Ji:2018waw` | 1807.07528 | PRD 99 (2019) 054008 | quasi-PDFs in 2D scalar and spinor QCD at large $N_c$ (leading and subleading order) | main | D4 |
| VI.2 | `Liu:2021evw` | 2102.07248 | arXiv | small-instanton contributions to the quasi-PDF matching kernel | intro | D5 |
| VI.3 | `Kock:2020frx` | 2004.01595 | PRD 102 (2020) 014039 | pion and kaon (quasi-)PDFs in the instanton vacuum | abs | D5 |
| VI.4 | `Ji:2020bby` | 2010.06665 | PRD 103 (2021) 074002 | 't Hooft model: mass structure, light-front sum rules (regular at $x=0$) | abs | D5 |

**Group VII (not about factorization; listed for completeness, not analysed):**

* Holographic QCD: heavy baryons and exotics, pentaquarks, tetraquarks (2016–2022).
* Instanton–dyon liquid model I–V (2015–2018); chiral random matrices and the Dirac spectrum at finite $\mu$ (2015–2016); SYK disorder (2016).
* Rotating fermions and pion condensation (2017–2018); viscous emissivities (2017); Wilson loops in the instanton vacuum and in AdS/QCD (2014–2015).
* Entanglement in Regge scattering, 2D QCD and quarkonium (2018–2023); Mueller-dipole KNO scaling (`Liu:2022bru`, `Liu:2023eve`). These concern small-$x$ multiplicities, not factorization proofs.
* Quantum anomalous energy and proton-mass decomposition (2021); gravitational multipoles and the hydrogen-atom EMT (2021–2023).
* Integrable spin chains and the 2D Ising model (`Liu:2023tft`, 2405.00550, `Liu:2025qsv`, 2601.00751, `Liu:2026rew`, 2609.07612).

The papers on Borel/large-$N$ asymptotics in integrable models (`Liu:2023tft`, `Liu:2026rew`) and the Ising form-factor papers share the *mathematical* themes of §3.D (trans-series, resurgence, convergence of form-factor expansions), but contain no factorization statements. `Liu:2025qsv` (Ising, "low rapidity threshold") does not discuss TMDs or rapidity divergences in QCD [txt check].

---

## 2. Conventions: Liu and coauthors vs. the monograph (translation table)

**Read this before porting any formula.** Most of the errata in §4 come from the different conventions mixed across the papers.

| item | Liu et al. | monograph (CONTEXT.md) | action |
|---|---|---|---|
| covariant derivative / Wilson lines | $D_\mu=\partial_\mu+igA_\mu$ (RMP eq. (44)); $W_n=P\exp[-ig\int ds\,n\cdot A]$ | $D_\mu=\partial_\mu-igA_\mu$; $W=P\exp(+ig\int dz\cdot A)$ | $g\to-g$ in Wilson lines. All quantities quoted below are even in $g$. |
| light-cone vectors | $n^\mu=(1,0,0,-1)/(\sqrt2P^+)$, $p^\mu=P^+(1,0,0,1)/\sqrt2$, $n\cdot p=1$ | $v^\pm=(v^0\pm v^3)/\sqrt2$ | same; only directions matter |
| $b$-logarithm | $L_b=\ln\frac{\mu^2b_\perp^2}{4e^{-2\gamma_E}}$ | $b_0=2e^{-\gamma_E}$, $\mu_b=b_0/b_T$ | $L_b=\ln(\mu^2/\mu_b^2)$; identical |
| CS scale | $\zeta=2(xP^+)^2e^{2y_n}$ (APPB (21)) | — | the sign convention for $y_n$ may differ from Collins' book; not checked here (UNVERIFIED) — compare with the book's definition of $\zeta_A$ before mixing |
| quasi-TMD scale | $\zeta_z=(2xP^z)^2$; $L_z=\ln(\zeta_z/\mu^2)$ | — | — |
| CS kernel | $2\zeta\,\partial_\zeta\ln f^{\rm TMD}=K$; $K^{(1)}=-\frac{\alpha_sC_F}{\pi}L_b$; $\mu^2\frac{dK}{d\mu^2}=-\Gamma_{\rm cusp}$, $\Gamma_{\rm cusp}=\frac{\alpha_sC_F}{\pi}+\dots$ | the CSS/Collins normalization | identical normalization |
| derivative in RGEs | APPB, RMP, PRD105: $\mu^2 d/d\mu^2$; PLB, JHEP 2023/24: $\mu\, d/d\mu$ | $\mu^2 d/d\mu^2$ | $\mu\,d/d\mu=2\mu^2d/d\mu^2$ |
| $\beta$ function | (a) PLB/APPB/RMP/PRD105: "$\beta_0=-\frac{1}{2\pi}(\frac{11}{3}C_A-\frac43N_fT_F)$", with $d\alpha_s/d\ln\mu=\beta_0\alpha_s^2$; (b) JHEP 2023/24: $d\alpha/d\ln\mu=-\beta_0\alpha^2-\beta_1\alpha^3$, $\beta_0=\frac{11C_A}{6\pi}-\frac{n_f}{3\pi}$ | $\mu^2\frac{d\alpha_s}{d\mu^2}=-\frac{\beta_0}{4\pi}\alpha_s^2$, $\beta_0=\frac{11}{3}C_A-\frac43T_Fn_f$ | $\beta_0^{(b)}=\beta_0^{\rm CTX}/(2\pi)=-\beta_0^{(a)}$ |
| constant of the large-angle cusp AD | JHEP 2023: $\Gamma_S\equiv\gamma_{HH}$, where $\Gamma_{\rm cusp}(\alpha_s,Y)\to Y\Gamma_{\rm cusp}+\gamma_{HH}$, $\gamma_{HH}^{(1)}=-\frac{\alpha_sC_F}{\pi}$; PLB: $\mu^2\frac{d\ln S_r}{d\mu^2}=\Gamma_S$, so $\Gamma_S^{\rm PLB}=\gamma_{HH}$; APPB, PRD105: $\mu^2\frac{d\ln S_I}{d\mu^2}=-\Gamma_S$, so $\Gamma_S^{\rm APPB}=-\gamma_{HH}$; RMP: printed signs internally inconsistent (§4, E2) | — | **use $\gamma_{HH}$ only** (the JHEP 2023 convention) |
| placement of the hard kernel | PLB/APPB: $\tilde f\sqrt{S_I}=H\,e^{\dots}f^{\rm TMD}$; RMP (209): $f^{\rm TMD}=H\,e^{\dots}\tilde f\sqrt{S_r}$ | — | $H_{\rm RMP}=H_{\rm PLB}^{-1}$ |
| heavy-light Sudakov factor | JHEP 2023: "$H_{HL}$" denotes the *pair* of form factors ($=H^{\mp}_{\rm LFWF}$) | — | single factor $C_{HL}^\pm$: $H=C_{HL}^+C_{HL}^-$ [chk] |
| Fourier transform | $d\sigma\propto\int d^2b\,e^{i\vec b\cdot\vec Q}$ | $\tilde f(b)=\int d^{2-2\epsilon}k\,e^{-ik\cdot b}f(k)$ | sign matters only for $b$-odd functions (Sivers) |
| time orderings | $T$, $\bar T$; "single-time-ordered" = one overall $T$ (form factor); "double/mixed" = $\bar T\dots T$ (cut diagram) | — | — |

---

## 3. Results at the level of theorems

Each item gives: **statement** (in Liu's conventions unless stated, with the corrections of §4 already applied and flagged), **hypotheses**, **proof architecture** (what is proven and what is assumed), **grade** with justification, **novelty**, **relation to CSS/Collins**, and **presentation advice**.

### 3.A Euclidean formulation of TMD soft physics

#### A1. The off-light-cone TMD soft function is a form factor of a fast colour-source pair (HQET)

*Sources:* `[Ji:2019sxk]` eqs. (1)–(13); `[Liu:2022nnk]` §4.1–4.2, App. A; `[Ji:2020ect]` §V.C [txt].

**Definitions.** Take time-like velocities $v^\mu=\gamma(1,\beta,\vec0_\perp)$ and $v'^\mu=\gamma'(1,-\beta',\vec0_\perp)$ in $(t,z,\vec b_\perp)$, with $\beta=\tanh Y$. Staples are $\mathcal W_v(\vec b_\perp,t)=W_v(0,t)W_\perp W_v^\dagger(\vec b_\perp,t)$, where $W_v(\xi,t)=P\exp[-ig\int_{-t/\gamma}^0ds\,v\cdot A(\xi+sv)]$. Define
$$
W(t,t',b_\perp,Y,Y')=\tfrac1{N_c}{\rm Tr}\langle\Omega|T[\mathcal W^\dagger_{v'}(\vec b_\perp,t')\mathcal W_v(\vec b_\perp,t)]|\Omega\rangle,\qquad Z(2t,b_\perp,Y)=W(t,t,b_\perp,Y,-Y),
$$
$$
S(b_\perp,Y,Y')\equiv\lim_{t,t'\to\infty}\frac{W(t,t',b_\perp,Y,Y')}{\sqrt{Z(2t,b_\perp,Y)Z(2t',b_\perp,Y')}}.
$$

**Statement (`[Ji:2019sxk]` eqs. (1),(3),(8)–(12)).**
$$
S(b_\perp,Y,Y')={}_{v'}\langle Q\bar Q,\vec b_\perp|\,J(\vec b_\perp,v,v')\,|Q\bar Q,\vec b_\perp\rangle_{v},\qquad
J=\eta^\dagger_{v'}(\vec b_\perp)\eta_v(\vec b_\perp)\psi^\dagger_{v'}(0)\psi_v(0).
$$
Here $\psi_v,\eta_v$ are HQET colour sources with $\mathcal L=\psi_v^\dagger iv\cdot D\psi_v+\eta_v^\dagger iv\cdot D\eta_v$, and $|Q\bar Q,\vec b_\perp\rangle_v$ is the lowest colour-singlet state at fixed separation and zero residual momentum. $S$ depends only on $Y+Y'$ (boost invariance). Because the matrix element is at equal time, $S$ has a Euclidean representation, $S=\lim W_E/\sqrt{Z_EZ_E}$ (eq. (12)), computed with Euclidean HQET, $i\tilde v\cdot D_E=D_\tau-i\beta D_z$ (eq. (13)). At large rapidity (`[Ji:2019sxk]` eq. (4); `[Liu:2022nnk]` eq. (50)):
$$
S(b_\perp,\mu,Y,Y')=\exp\big[(Y+Y')K(b_\perp,\mu)+\mathcal D(b_\perp,\mu)+O(e^{-(Y+Y')})\big].
$$

**Hypotheses.**
* (i) In the color-singlet $Q\bar Q$ sector at fixed $\vec b_\perp$ there is an isolated ground state with residual energy $E=\gamma^{-1}V(\vec b_\perp)$, and the continuum is gapped. Excited states are projected out by Riemann–Lebesgue, or equivalently by $t\to t(1-i0)$.
* (ii) The pair interpolating field $O_v$ (eq. (6)) creates the ground state with non-zero overlap $\Phi(\vec b_\perp)$, which is boost invariant.
* (iii) Wilson-line self-energies and the $Q\bar Q$ time evolution cancel against $\sqrt{Z Z}$. This is an LSZ-type amputation; perturbatively it rests on the web decomposition of A2.

**Proof architecture.** Insert complete sets of heavy-pair states before and after $J$ (eq. (8)); take the large-$t$ limit; divide by $Z$ (eq. (11)). The same procedure works in Euclidean time. The one-loop equality is verified explicitly [txt].

**Grade: [A].** The spectral step is standard but rests on a non-perturbative spectral assumption. The perturbative content (cancellation of self-interaction webs) is the partial-exponentiation lemma A2, itself graded [A].

**Novelty.** This is the first representation of the Collins soft factor as a *time-independent* matrix element. The soft factor is a "square of an S-matrix", which had been regarded as intrinsically Minkowskian. The papers stress that it *cannot* be obtained by replacing the light-like links with a finite number of Euclidean links: earlier "bent" Euclidean soft functions (`[Ji:2014hxa]`, `[Ebert:2019okf]`) have the correct one-loop logarithms but the wrong cusp anomalous dimension beyond one loop, because a circular Euclidean angle cannot become arbitrarily large [txt `Ji:2019sxk`, `Ji:2019ewn`]. Lattice caveats acknowledged by the authors: fermion doubling of static sources, renormalization of the velocity, large-velocity noise [txt].

**Relation to CSS.** The soft factor itself is Collins' (`[Collins:2011zzd]`, `[Collins:2011ca]`). The new ingredient is its realization on a Euclidean lattice. A3/A6 show that this time-like form factor equals the space-like Drell–Yan soft factor actually used in Collins' TMD definition.

**Presentation.** Definition + theorem + figure: the Minkowski Wilson loop with two staples next to the HQET picture (two colour sources moving with $v$, kicked to $v'$ at $t=0$). One remark on the LSZ interpretation of $\sqrt Z$.

#### A2. Pinch-pole singularities, partial exponentiation, ultrasoft modes: existence of the $L\to\infty$ limit

*Source:* `[Liu:2022nnk]` §3.2–3.3, §4.2–4.3, Apps. B, D [txt].

**(a) Partial-exponentiation lemma (eq. (46), App. B).** For a correlator $F(C,x,x')={\rm Tr}\langle O(x)W(C,x'\to x)O'(x')\rangle$ with a Wilson line of arbitrary shape,
$$
F(C,x,x')=e^{\Phi(C)}\;{\rm Tr}\langle O(x)W(C,x'\to x)O'(x')\rangle_{\rm 2PI}.
$$
Here $e^{\Phi(C)}$ is the trace-normalized vacuum expectation value of the line, written as the exponential of its webs (maximally non-abelian colour factors). The remainder is the sum of operator–link 2PI vertices $w_0$ with modified colour factors.
*Proof:* a generalized eikonal identity $\sum_{G\in\mathcal G_d}I(G)=\frac1{S_d}\prod_{i=0}^{n(d)}I(w_i)$ (eq. (B.5)) with $w_0$ held fixed, followed by the Gatheral / Frenkel–Taylor resummation (`[Gatheral:1983cz]`, `[Frenkel:1984pz]`). For closed loops the replica trick is used.
**Grade [A].** The combinatorial core is standard. The extension to a fixed $w_0$ is only stated to go through "similarly to the standard one".

**(b) Pinch poles.** Dividing out self-interactions of non-light-like staples with rectangular Wilson loops goes back to Collins' treatment of off-light-cone Wilson lines (`[Collins:2008ht]`) and to `[Ji:2018hvs]`. A2 supplies the all-order justification. For the quasi-TMD staple, $e^{\Phi(\mathcal W_z)}=\langle0|\mathcal W_z|0\rangle\sim e^{-LE(b_\perp)}$ with $E=2\delta m+V(b_\perp)$. The rectangular loop behaves as $Z_E(2L)\sim e^{-2LE}$, so $\lim_{L\to\infty}\langle P|\tilde O_z|P\rangle/\sqrt{Z_E}$ exists. The pinch of the two eikonal propagators $1/[(k^z+i0)(k^z-i0)]$ is made explicit by $z$-ordering the two staples ("single-line notation", eqs. (41)–(43)). **[A]**.

**(c) Ultrasoft modes.** Analogous to the Lamb shift and to the Appelquist–Dine–Muzinich effect in the static potential, individual diagrams develop power-like IR divergences at high orders, scaling as $1/L$. APPB §3.3 says "beyond three loops" for the quasi-TMD; the static-potential analogue starts at $O(\alpha_s^4)$; the §4 overview says "from the 3-loop level". The exact first order is not pinned down here. They cancel after resumming the 2PI dipole self-interactions into a dressed "single-line" propagator. The relevant scale is the octet–singlet splitting $V_8-V$; for the boosted soft function it is $\alpha_sC_A e^{-Y}/(2b_\perp)$ (eqs. (109)–(111)). Y-dependent "ultra-ultrasoft" modes are argued to cancel by colour neutrality and Ward identities (§4.3). **[A]** in structure, with the all-order cancellation argued rather than proven (sub-grade A−).

**(d) Timelike, double-time-ordered soft functions have no pinch poles and are IR finite** (App. D). The proof is by induction on the number of "4PI" webs and assumes the absence of power IR divergences at lower order. **[A]** (A−).

**Presentation.** Lemma (a) belongs in the Wilson-line appendix (App. B of the monograph). Use (b)–(c) as a remark in the frontier chapter. They are the TMD analogue of the HQET heavy-pair ground state.

#### A3. Analyticity in the hyperbolic angle; equality $S_{\rm DY}=S_{\rm FF}$; universality classes

*Source:* `[Liu:2022nnk]` §4.5–4.7, App. F, App. H; Tables 1–2 [txt].

**Statement (single-time-ordered soft functions).** Let $S(b_\perp,\mu;v_1,v_2)$ be the subtracted soft function (eq. (93)) built with one overall $T$ and arbitrary off-light-cone directions. Order by order in perturbation theory, and under the hypotheses below, it depends on the direction vectors only through the complex hyperbolic angle
$$
\theta(v_1,v_2)={\rm Arcosh}\frac{v_1\cdot v_2-i0}{\sqrt{v_1^2+i0}\sqrt{v_2^2+i0}}.
$$
It is the boundary value of a single analytic function $S(\theta)$ on the strip $-\pi\le{\rm Im}\,\theta\le\pi$. Table 1 [txt]:

| $v_1$ | $v_2$ | orientation $v_1$ | orientation $v_2$ | hyperbolic angle |
|---|---|---|---|---|
| spacelike | spacelike | past | past | $Y$ |
| timelike | timelike | past | past | $Y-i\pi$ |
| timelike | timelike | past | future | $Y$ |
| spacelike | spacelike | past | future | $Y+i\pi$ |
| timelike | spacelike | past | future | $Y+i\pi/2$ |
| timelike | spacelike | past | past | $Y-i\pi/2$ |

**Corollaries.**
* (i) $S_{\rm DY}(b_\perp,\mu,Y,Y')=S_{\rm FF}(b_\perp,\mu,Y,Y')$: Collins' space-like (tilted, double-time-ordered) Drell–Yan soft factor equals the form-factor soft function of A1 (eq. (99)).
* (ii) For half-on/half-off light-cone soft functions, $S(b_\perp,\mu,\delta,\hat z)=S(b_\perp,\mu,-i\delta,\hat t)$ (eq. (136)).
* (iii) The universal light-cone form $S(b_\perp,\mu,Y+Y')=e^{(Y+Y')K+\mathcal D}$ (eq. (135)), assuming the light-cone limit is uniform in ${\rm Im}\,Y$.
* (iv) In the $\delta$ regulator, $S^+(b_\perp,\mu,\delta,\delta)=S^{-\dagger}(b_\perp,\mu,\frac{i\delta}{1+i0},\frac{i\delta}{1+i0})$, i.e. $\ln\frac{\mu^2}{2\delta^+\delta^-}K\to(\ln\frac{\mu^2}{2\delta^+\delta^-}+i\pi)K$ (eqs. (H.5)–(H.6)).
* (v) The DY and SIDIS soft factors are equal in the standard $\delta$ regulator (App. H, eqs. (H.7)–(H.11), via Hartogs' theorem on separately holomorphic functions).

**Universality classes in the light-cone limit (Table 2) [txt].** Only three independent objects remain: the light-cone wave function of a $Q\bar Q$ pair ($\Psi$), the TMDPDF of a single heavy-quark state ($f^{\rm TMD}$), and the heavy-quark TMD fragmentation function ($D^{\rm TMD}$).

| type | time order | $v_1$ (orient.) | $v_2$ (orient.) | ultrasoft | factorization | Euclidean |
|---|---|---|---|---|---|---|
| form factor | single | arbitrary | arbitrary | yes | $\Psi^\dagger\Psi$ | yes |
| spacelike DY | double | spacelike (past) | spacelike (past) | yes | $\Psi^\dagger\Psi$ | yes |
| timelike DY | double | timelike (past) | timelike (past) | no | $f^{{\rm TMD}\dagger}f^{\rm TMD}$ | yes |
| $\gamma^*\to\bar QQ$+hadrons | double | timelike (future) | timelike (future) | no | $D^{{\rm TMD}\dagger}D^{\rm TMD}$ | no |
| timelike SIDIS | double | timelike (past) | timelike (future) | no | $D^{\rm TMD}f^{\rm TMD}$ | no |
| spacelike SIDIS | double | spacelike (past) | spacelike (future) | yes | $\Psi^\dagger\Psi$ | yes |
| quasi-TMD | double | timelike (past) | spacelike (arbitrary) | yes | $\Psi^\dagger f^{\rm TMD}$ | yes |
| quasi-fragmentation | double | spacelike (arbitrary) | timelike (future) | yes | $D^{\rm TMD}\Psi$ | no |

**Hypotheses (stated explicitly in the text) [txt §4.5, App. F, App. H].**
* (H1) A physical gauge with a positive-norm Hilbert space (first argument).
* (H2) A regularization that preserves Lorentz invariance in the $(t,z)$ plane and keeps the energy positive, $E-\beta P^z\ge0$ for $|\beta|<1$.
* (H3) The spectral functions have moderate regularity (Paley–Wiener type).
* (H4) A uniform gap for the $t_0\to\infty$ limit. In the author's words, "although no one can prove it!".
* (H5) Analyticity is shown order by order. Convergence of the expansion is not claimed; that the full result shares the analyticity is "natural to expect".
* (H6) For (iii), the light-cone limit is uniform in ${\rm Im}\,Y$. This is checked perturbatively only for ${\rm Im}\,Y\in\{0,\pm\pi/2,\pm\pi\}$.

**Proof architecture.** (1) Energy positivity gives analyticity in $v^0\to z$ in a half-plane. (2) At $z=-iv_0$ both functions become Euclidean Wilson loops that are equal by $(\tau,z)$ rotation invariance; uniqueness of analytic continuation gives the functional equation $g(z)=f(1/z)$ (eqs. (126)–(127)). (3) Map to $\theta$ by $\cosh Y=\frac{1+z^2}{1-z^2}$ (DY) or $\frac{z^2+1}{z^2-1}$ (form factor) (eqs. (128)–(134)).
App. F gives two further proofs:
* analytic continuation at finite staple length;
* a Wightman-function argument: consecutive increments lie in the forward tube $\mathbb R^4-iV_+$, and the complex Lorentz map $\Lambda(t,z)=(it,iz)$ connects the two configurations. The author names the "edge of the wedge" theorem for complex Lorentz covariance in the extended tube. The result actually used is the **Bargmann–Hall–Wightman theorem** (`[Streater:1989vi]`; terminology note E6).

**Grade.** Perturbative statements: **[A]**. The hypotheses are explicit and natural, but H4–H6 are not proven. Double-time-ordered soft functions with time-like vectors (Table 2): universality is **not** claimed. The author is "not clear … whether the heavy-quark TMDPDF and fragmentation functions are equal to all orders" (§6). Non-perturbative statements: **[C]**.

**Novelty.** Yes. This is the first systematic analytic-continuation framework connecting *all* off-light-cone soft functions. Table 2 is new. It turns the folklore that the regulator choice does not matter into a sharp classification: three universality classes, of which only $\Psi$ and $f^{\rm TMD}$ have Euclidean realizations.

**Relation to CSS.** Collins and Collins–Metz (`[Collins:2011zzd]`, `[Collins:2004nx]`) assert, based on space-like separations and contour deformation, that the DY soft factor is time-ordering insensitive and universal across $e^+e^-$, DY and SIDIS. A3 supplies the analytic mechanism, and also shows where universality can fail: time-like double-ordered factors and fragmentation. A6 later sharpens the time-ordering part.

**Presentation.** Theorem (perturbative, hypotheses H1–H6) + Table 1 + figure of the analyticity strip in the complex $\theta$ plane (cf. APPB Fig. 24) + Table 2 as a "universality classes" box.

#### A4. Factorization of rapidity divergences in off-light-cone soft functions

*Source:* `[Liu:2022nnk]` §4.4, App. E [txt].

**Statement.** For $Y+Y'\to\infty$,
$$
\ln S(b_\perp,\mu,Y,Y')=(Y+Y')K(b_\perp,\mu)+\mathcal D(b_\perp,\mu)+O(e^{-(Y+Y')}).
$$
Equivalently $S=\Psi^\dagger(b_\perp,\mu,Y')\Psi(b_\perp,\mu,Y)$ (eq. (115)), with $\Psi$ the rapidity-renormalized light-cone wave function of the $Q\bar Q$ pair (eq. (116)), and
$$
|\Psi(b_\perp,\mu,Y)|=e^{K Y+\mathcal D_1-\frac12\mathcal D_0}\ \Rightarrow\ \mathcal D=2\mathcal D_1-\mathcal D_0\quad(\text{eqs. (120)–(122)}).
$$
Here $\mathcal D_0$ comes from the normalization $\sqrt{S(b_\perp,\mu,\delta,\delta)}$ in the definition (116) of $\Psi$, i.e. it is the rapidity-independent part of the on-light-cone soft function. APPB eq. (10) and `[Ji:2019sxk]` eq. (21) call the same object $\mathcal D_2$. The notation changes within the lecture notes; this reading is mine, but it is consistent with A5(c).

**Proof architecture (two routes).**
* **Route 1, region analysis.** The power-counting parameter is $\lambda=e^{-(Y+Y')/2}$. Leading regions: two collinear subgraphs plus one soft subgraph. The hard kernel is trivial because there is no hard scale: on-shell eikonal external lines kill the external momentum.
* **Route 2, App. E, axial gauge $n\cdot A=0$ with $n=\hat z+\vec n_\perp$.** Then there is no Glauber problem and the collinear $A^\pm$ cannot enter hard parts.
  * Split the webs into self-interaction webs and 2PI vertex webs.
  * Soft factorization plus the replica trick (web contributions are linear in the replica number) shows that vertex webs carry no leading collinear, i.e. rapidity, divergence.
  * The divergent parts then satisfy $\mathrm{div}_1(Y+Y')=\mathrm{div}_2(Y)+\mathrm{div}_2(Y')$. With continuity, Cauchy's functional equation gives linearity in $Y$ (eqs. (E.1)–(E.4)).
  * A rapidity-slicing estimate at fixed order $n$ gives $|V(Y)-V(Y')|\lesssim (Y-Y')e^{-Y'/n}$ and convergence of $V(Y)$ (eqs. (E.5)–(E.13)).

**Assumed step (explicit in the text):** IR control of the highest-rapidity group ("Assuming this can be done", App. E).

**Grade: [A]** (sub-grade A−). The all-order argument is complete except for one explicitly assumed step. It agrees with the claim of Collins–Soper 1981 (`[Collins:1981uk]`). Liu notes that a detailed explanation beyond one loop "is not presented" there [txt]. It also agrees with Vladimirov's conformal-map proof for light-like regulators (`[Vladimirov:2017ksc]`) and with explicit three-loop soft functions (`[Li:2016axz]`).

**Presentation.** Proposition with proof sketch. The Cauchy-functional-equation step is short and pedagogical; include it.

#### A5. Intrinsic (reduced) soft function $S_I$: definitions, equivalence, scheme independence, anomalous dimension

*Sources:* `[Ji:2019sxk]` eqs. (19)–(21); `[Ji:2019ewn]` eqs. (18)–(21); `[Liu:2022nnk]` eqs. (51),(76)–(81),(120)–(122); `[Ji:2021znw]` eqs. (46)–(48),(69)–(72) [txt].

**Statement.**
* (a) Off-light-cone definition: $S_I(b_\perp,\mu)\equiv e^{-\mathcal D(b_\perp,\mu)}$, with $\mathcal D$ the rapidity-independent part of $S_{\rm DY}$ (A1). (Called $S_r$ in `[Ji:2019ewn]` and `[Ji:2020ect]`.)
* (b) On-light-cone definition (`[Liu:2022nnk]` eq. (76)):
$$
\sqrt{S_I(b_\perp,\mu)}=\lim_{\delta^+\to0}\frac{\sqrt{S(b_\perp,\mu,\delta^+,\delta^-=\delta^+)}}{S(b_\perp,\mu,\delta^+,\hat z)},
$$
with $S(b_\perp,\mu,\delta^+,\hat z)$ built from one $\delta$-regulated light-like staple and one space-like $\hat z$ staple, subtracted by $\sqrt{Z_E}$ (eq. (72)).
* (c) **Scheme independence.** Write $S_1(b,\delta,Y')=e^{(Y'-\ln\delta)K+\mathcal D_1}$ and $S_2(b,\delta,\delta')=e^{-\ln(\delta\delta')K+\mathcal D_2}$ (`[Ji:2019sxk]` eqs. (20)–(21)). Then $\mathcal D=2\mathcal D_1-\mathcal D_2$. Definitions (a) and (b) agree, and $S_I$ is rapidity-scheme independent, although $\mathcal D$, $\mathcal D_1$, $\mathcal D_2$ separately are not. Consistency check with (b): $\frac12\ln S_I=\frac12\ln S_2-\ln S_1$ gives $\mathcal D_1=\frac12(\mathcal D+\mathcal D_2)$ [chk-hand].
* (d) **Physical meaning:** $S_I$ is the (squared) light-cone wave function of a static $Q\bar Q$ pair at separation $b_\perp$ (eqs. (120)–(122)).
* (e) **Anomalous dimension** (convention of §2):
$$
\mu^2\frac{d\ln S_I(b_\perp,\mu)}{d\mu^2}=\gamma_{HH}(\alpha_s),\qquad
\gamma_{HH}=-\frac{\alpha_sC_F}{\pi}+\frac{\alpha_s^2}{\pi^2}C_F\Big[C_A\Big(-\frac{49}{36}+\frac{\pi^2}{12}-\frac{\zeta_3}{2}\Big)+\frac{5}{9}T_Fn_f\Big]+O(\alpha_s^3).
$$
Here $\gamma_{HH}$ is the constant term in $\Gamma_{\rm cusp}(\alpha_s,\theta)=\theta\,\Gamma_{\rm cusp}(\alpha_s)+\gamma_{HH}(\alpha_s)+O(e^{-\theta})$, in the normalization where $\Gamma_{\rm cusp}(\alpha_s,\theta)=\frac{\alpha_sC_F}{\pi}(\theta\coth\theta-1)+O(\alpha_s^2)$. One loop: $S_I=1-\frac{\alpha_sC_F}{\pi}L_b$.
**[chk: check_GammaS2.py]:** large-$\beta$ limit of the two-loop velocity-dependent cusp anomalous dimension (`[Becher:2009kw]`, `[Korchemsky:1987wg]`), with the zero-recoil condition $\Gamma_{hh}(0)=0$ satisfied to $10^{-18}$. The $n_f$ term also follows from the running-coupling argument ($-\frac59T_Fn_f\frac{\alpha_s}{\pi}\times$ one loop). It agrees with `[Ji:2023pba]` (A.6) and with the RMP value, but **not** with `[Liu:2022nnk]` eq. (81) or `[Ji:2021znw]` eq. (72) (erratum E2).
* (f) **Two-loop structure (corrected; monograph conventions).** With $\mu^2d\alpha_s/d\mu^2=-\frac{\beta_0}{4\pi}\alpha_s^2$:
$$
\ln S_I=-\frac{\alpha_sC_F}{\pi}L_b+\alpha_s^2\Big[-\frac{C_F\beta_0}{8\pi^2}L_b^2+\hat\gamma_{HH}L_b+c_2\Big]+O(\alpha_s^3),\qquad
\hat\gamma_{HH}=\frac{C_F}{\pi^2}\Big[C_A\Big(-\frac{49}{36}+\frac{\pi^2}{12}-\frac{\zeta_3}{2}\Big)+\frac59T_Fn_f\Big].
$$
$c_2$ is a two-loop constant not determined by the RGE. **[chk: check_RGE_structure.py]**, symbolic and checked numerically against one-loop running. The printed $L_b^2$ coefficients in `[Liu:2022nnk]` (81) and `[Ji:2020ect]` (208) are a factor 2 too large for their own $\beta_0$, and the single-log sign in (81) is wrong (errata E2, E4).

**Grade.**
* (a)–(d): **[A]** (consequences of A3, A4 and the region analysis).
* (e): the identification of the anomalous dimension follows from multiplicative renormalization of cusped Wilson loops, **[A]** to all orders. Its two-loop value is a fixed-order result, **[P]** at two loops. The three-loop constant can be read off from `[Grozin:2015kna]` (not done here: UNVERIFIED).
* (f): fixed order, **[P]**.

**Novelty.** The concept itself is new: a scheme-independent, Euclidean-computable soft object that carries the non-cancelling non-perturbative soft physics of TMD factorization. So is the relation $\mathcal D=2\mathcal D_1-\mathcal D_2$.

#### A6. The time-ordering theorem: coordinate-space analyticity of TMD soft factors (main single-author result)

*Source:* `[Liu:2023pjb]` (JHEP 09 (2024) 030), complete [txt].

**Setting.** Dimensional regularization with $\epsilon\neq0$ throughout; linear covariant gauges; perturbation theory "order by order to an arbitrary finite order" [txt fn. 4]. Exponential regulator $\nu>0$ (`[Li:2016axz]`):
$$
S(b_\perp,\nu,\epsilon)=\tfrac1{N_c}{\rm Tr}\langle\Omega|\bar T\big[W_n^\dagger(-i\nu e_t,\vec b_\perp)W_{\bar n}(-i\nu e_t,\vec b_\perp)\big]\,T\big[W_{\bar n}^\dagger(0)W_n(0)\big]|\Omega\rangle\quad\text{(DY shape, eq. (3.7))},
$$
$$
S_t(b_\perp,\nu,\epsilon)=\tfrac1{N_c}{\rm Tr}\langle\Omega|T\,W_n^\dagger(-\nu e_z+\vec b_\perp)W_{\bar n+}^\dagger(-\nu e_z+\vec b_\perp)W_{\bar n+}(0)W_n(0)|\Omega\rangle\quad\text{(single $T$; eq. (3.20))}.
$$

**Theorem (eqs. (3.12)–(3.16), (3.20)–(3.28), (3.50), (3.71)).**
1. $S(b_\perp,\nu,\epsilon)$ has a *below-threshold* parametric representation without cuts. It is built from Euclidean-type gluon Wightman functions whose invariant length squares are
$x^2_{A,ij}=-2\lambda^R_i\lambda^R_j$, $x^2_{B,ij}=-\nu^2-b_\perp^2-\sqrt2 i\nu(\lambda^L_i-\lambda^R_j)$ and $x^2_{C,ij}=-\nu^2-b_\perp^2-2\lambda^L_i\lambda^R_j-\sqrt2 i\nu(\lambda^L_i-\lambda^R_j)$.
Every imaginary part is accompanied by a real part bounded above by $-b_\perp^2-\nu^2<0$.
2. $S(b_\perp,\nu,\epsilon)=S_t(b_\perp,\nu,\epsilon)$. The DY soft factor, an amplitude squared, equals a space-like form factor of a light-like $Q\bar Q$ pair.
3. **Master equality.** With finite LF lengths $L^\pm$, off-light-cone tilt $Y$ (vectors $n_Y=n-e^{-Y}\bar n$; $v=n+e^{-Y}\bar n$), Z-factor subtractions and "transverse" links along $\vec b_\perp-i\nu e_t$ or $\vec b_\perp-\nu e_z$:
$$
S^{\rm full}(L^+,L^-,b_\perp,\nu,Y,\epsilon)=S_t^{\rm full}(-iL^-,-iL^+,b_\perp,\nu,Y,\epsilon)\qquad\text{(eq. (3.71))}.
$$
The author calls it "the safest identity throughout the work". The unequal-length version is eq. (3.54).
Taking limits in different orders gives the corresponding identities for the off-light-cone, finite-LF-length and exponential regulators.
4. **DY = SIDIS** in the exponential regulator, with infinitely long light-like lines (App. C). It is shown first heuristically in light-front perturbation theory. The final-state sums are real by the identity $\int\frac{dE}{2\pi i}e^{-\nu|E|/\sqrt2}\big[\prod_k\frac1{E-E_k-i\eta}-\prod_k\frac1{E-E_k+i\eta}\big]=\sum_ke^{-\nu E_k/\sqrt2}\prod_{j\neq k}\frac1{E_k-E_j}$ (**[chk: check_HL_and_C1.py]**, $n=2,3,4$). A second argument deforms to time-like and space-like lines at finite lengths.

**Consequences stated by the author.**
* (i) Universality of the TMD soft factor, hence of the CS kernel (rapidity anomalous dimension), between inclusive TMDPDFs and exclusive LFWFs.
* (ii) The exponential regulator can be applied to LFWFs.
* (iii) The lattice route to $S_I$ via form factors (A1, B4) is put on a firmer basis.
* (iv) The $e^+e^-$ soft factor is *not* covered: its operator order is $T\bar T$ rather than $\bar TT$, and the process is "much less local" (§4, item 4).

**Hypotheses.**
* (T1) The perturbative gluon (and ghost) Wightman functions in linear covariant gauges satisfy the spectral condition and local commutativity order by order, with DR at $\epsilon\neq0$ (fn. 4, which cites the covariant operator formalism of `[Kugo:1979gm]`). Making this mathematically rigorous for DR at generic $\epsilon$ in massless theories is listed by the author as open (§4, item 2): "the author believes in it".
* (T2) Positivity of the coordinate-space parametric functions $P_{ij}(\alpha)$. This is proven by an all-minors matrix-tree formula (eq. (2.10), App. A; `[Bogner:2010kv]`). [R]-level combinatorics.
* (T3) Null separations on the same line give scaleless contributions in DR, so $\eta\to0^+$ can be taken at the integrand level ("a general rule in dimensional regularization").
* (T4) Multiplicative renormalization, so the bare identities imply renormalized ones.
* (T5) Definitional: "It is outside the scope of this paper to show that this definition correctly captures soft contributions to the DY process" (fn. 5).

**Proof architecture.**
* (1) Wightman–Osterwalder–Schrader coordinate-space analyticity (`[Streater:1989vi]`): the P-tube $S^P_n$, the permuted extended tube, complex Lorentz covariance, and the below-threshold region $E'_n$ (eq. (2.11)). Path-connectedness of $S^P_n\cap E'_n$ is proven in App. B.
* (2) Enumerate all invariant length squares between points chosen on the $T$ and $\bar T$ parts.
* (3) For $S_t$, Wick-rotate $\lambda\to-i\lambda$ and $\alpha\to-i\rho$ without exponential growth (eqs. (3.21)–(3.24)). Equivalently apply the proper complex Lorentz transformation $\Lambda(t,z)=(iz,it)$, with $\Lambda(-i\lambda n)=\lambda n$, $\Lambda(-i\lambda\bar n)=-\lambda\bar n$, $\Lambda(-\nu e_z)=-i\nu e_t$, $\Lambda v=in_Y$, $\Lambda v'=-i\bar n_Y$ (eqs. (3.25)–(3.32), (3.58)).
* (4) Z-factors and transverse links make the finite-length identities gauge invariant and remove boundary terms at LF infinity.

**Grade: [A]** (sub-grade A+). This is the most careful all-order argument available for this property. Hypotheses T1–T5 are explicit, the combinatorial part is rigorous, and the remaining gap is the (widely believed) perturbative Wightman structure of DR correlators. Non-perturbative extension: **[C]**. The author states explicitly a conjecture on Wilson loops in complex space-time in full QCD (§3.4): for closed loops whose points lie in the permuted extended tube, $\langle{\rm Tr}W(C)\rangle_W$ exists and is invariant under proper complex Lorentz maps.

**Novelty.** Yes. First explicit all-order argument for the time-ordering insensitivity of the DY soft factor in the exponential regulator, and for its equality with a single-time-ordered form factor. Time-ordering insensitivity of the DY soft factor in the finite-LF-length and $\delta$ regulators had already been used, e.g. in the soft–rapidity correspondence (`[Vladimirov:2016dll]`, `[Vladimirov:2017ksc]`). §3.1 of `[Liu:2023pjb]` gives the analytic reason for it. It also clarifies a disputed point: some authors state time-ordering insensitivity directly (`[Collins:2011zzd]`, `[Collins:2004nx]`, `[Echevarria:2015byo]`), while others are cautious (`[Moult:2018jzp]`). The published `[Vladimirov:2017ksc]` calls factorization of rapidity divergences for the SIDIS soft factor "the open question" [txt quote in `Liu:2023pjb`].

**Presentation.** A boxed "Wightman preliminaries" paragraph (tubes, BHW, Schwinger functions). Then the theorem with T1–T5, and a figure of the complex Lorentz map exchanging $t$ and $z$. This is the best example in the TMD literature of an axiomatic QFT tool producing a factorization lemma. It fits the "Lean-like" ambition of the monograph well.

### 3.B Quasi-TMD factorization (LaMET for TMDs)

Background: LaMET was proposed by X. Ji (`[Ji:2013dva]`, `[Ji:2014gla]`). Light-cone correlations are obtained from equal-time correlators in large-momentum states through EFT matching. The TMD extension needs a Euclidean treatment of the soft factor, which is what §3.A supplies.

#### B1. The quasi-TMDPDF factorization theorem

*Sources:* `[Ji:2019ewn]` eq. (22) and the sketch below it; `[Liu:2022nnk]` §3.1–3.6, App. C; `[Ji:2020ect]` §V.B [txt].

**Definition** (`[Liu:2022nnk]` eqs. (33)–(37)):
$$
\tilde f(x,b_\perp,\mu,\zeta_z)=\lim_{L\to\infty}\frac1N\int\frac{d\lambda}{2\pi}e^{i\lambda x}\frac{\langle P|\bar\psi(\tfrac{\lambda\hat z}{2}+\tfrac{\vec b_\perp}2)\Gamma\,\mathcal W_z(\tfrac{\lambda\hat z}2+\vec b_\perp;L)\,\psi(-\tfrac{\lambda\hat z}2-\tfrac{\vec b_\perp}2)|P\rangle}{\sqrt{Z_E(2L,b_\perp,\mu)}}.
$$
* $\mathcal W_z(\xi;L)=W_z^\dagger(\xi;L)W_\perp W_z(-\xi^z\hat z;L)$ with $W_z(\xi;L)=P\exp[-ig\int_0^{L-\xi^z}d\lambda\,\hat z\cdot A(\xi+\hat z\lambda)]$;
* $Z_E(2L,b_\perp,\mu)=\frac1{N_c}{\rm Tr}\langle0|W_\perp\mathcal W_z(\vec b_\perp;2L)|0\rangle$ (rectangular $2L\times b_\perp$ loop);
* $N=|{\rm Tr}(\slashed P\Gamma)|/2$, $\lambda=zP^z$, $\zeta_z=(2xP^z)^2$, $\Gamma\in\{\gamma^t,\gamma^z\}$ (universality);
* staple toward $+\hat z$ for DY, $-\hat z$ for SIDIS.

**Theorem (corrected normalization; erratum E1).**
$$
\boxed{\ \tilde f(x,b_\perp,\mu,\zeta_z)\,\sqrt{S_I(b_\perp,\mu)}=H\Big(\frac{\zeta_z}{\mu^2}\Big)\exp\Big[\tfrac12K(b_\perp,\mu)\ln\frac{\zeta_z}{\zeta}\Big]f^{\rm TMD}(x,b_\perp,\mu,\zeta)+O\Big(\frac{\Lambda^2_{\rm QCD}}{\zeta_z},\frac{M^2}{(P^z)^2},\frac{1}{b_\perp^2\zeta_z}\Big)\ }
$$
* There is **no convolution in $x$**: the hard subgraphs are localized at the two quark–link vertices, and hard momenta flowing between $0$ and $\vec b_\perp$ are power suppressed.
* Equivalently (`[Liu:2022nnk]` eq. (74)), $\tilde f=H\,\frac{f(x,b_\perp,\mu,\delta^-)}{S(b_\perp,\mu,\delta^+,\delta^-)}\,S(b_\perp,\mu,\delta^+,\hat z)$, in any on-light-cone regulator.
* Momentum evolution: $P^z\frac{d}{dP^z}\ln\tilde f=K(b_\perp,\mu)+\mathcal G(\zeta_z/\mu^2)$, with $\mathcal G^{(1)}=\frac{\alpha_sC_F}{\pi}\big(1-\ln\frac{\zeta_z}{\mu^2}\big)$ and $2\zeta_z\partial_{\zeta_z}\ln H=\mathcal G$ ([chk-hand] against $H^{(1)}$).
* **CS kernel from ratios (corrected):**
$$
\frac{\tilde f(x,b_\perp,\mu,\zeta_{z,1})}{\tilde f(x,b_\perp,\mu,\zeta_{z,2})}=\frac{H(\zeta_{z,1}/\mu^2)}{H(\zeta_{z,2}/\mu^2)}\Big(\frac{\zeta_{z,1}}{\zeta_{z,2}}\Big)^{K/2}=\frac{H_1}{H_2}\Big(\frac{P^z_1}{P^z_2}\Big)^{K}\quad(\text{fixed }x),
$$
which is the Ebert–Stewart–Zhao form `[Ebert:2018gzl]`.

**Hypotheses.** These are the standard CSS/Collins ingredients adapted to the staple:
* (Q1) Leading regions come from Landau equations (App. C). With one external collinear direction, the collinear and staple displacements decouple; the gauge-link propagators admit non-zero Feynman-parameter solutions only via dipole 2→2 insertions, i.e. the pinch poles of A2.
* (Q2) Collinear directions other than $p$, possible in individual cut diagrams, cancel by the **"sum over cuts"** argument (`[Collins:2011zzd]`).
* (Q3) The Glauber region is absent: inside the hard region all small-$k^z$ link poles can be deformed into the upper half-plane, and the same deformation avoids $k^+k^-\ll k_\perp^2$.
* (Q4) Pinch poles and ultrasoft modes are handled as in A2: subtraction by $\sqrt{Z_E}$ and resummation of dipole self-energies.
* (Q5) Hard subgraphs are homogeneous, all components $\sim P^z$ (eqs. (62)–(63)).
* (Q6) Multiplicative renormalizability of the staple operator (E2).
* (Q7) Perturbation theory with on-shell massless external partons. Non-perturbative validity is assumed.

**Proof architecture: power counting** (`[Liu:2022nnk]` eqs. (54)–(68)). Use the single-line notation, in which a staple pair has mass dimension $3/2$ and spin $0$. Let $\lambda\sim1/(b_\perp P^z)$. The leading power is $\lambda^{F(H)+F(SC)+F(H')+F(H'')}$ with
$$
F(H)=\sum_{s=0,1}\big[N(CH,1,s)+N(SH,1,s)\big]+N(CH,\tfrac32,\tfrac12)+\tfrac32\sum_{s=0,\frac12}N(SH,\tfrac32,s)-N(CH,1,\ell)-\tfrac72,
$$
$$
F(SC)=\tfrac12N(SC,\tfrac32,\tfrac12)+N(SC,1,0),\qquad F(H')=F(H'')=0.
$$
Here $N(XY,d,s)$ counts lines of mass dimension $d$ and spin $s$ connecting subgraphs $X$ and $Y$, and $\ell$ marks longitudinally polarized collinear gluons.
* No super-leading regions: $F(H),F(SC)\ge0$.
* The leading region has $N(CH,\frac32,\frac12)=2$ and $N(SH,\frac32,0)=1$ (one soft "staple"), arbitrarily many longitudinal collinear gluons into $H$, arbitrarily many soft gluons into $C$, and nothing else. **[chk-hand]:** $F(H)=-\frac72+2+\frac32=0$, and each extra soft gluon into $H$ costs $+1$.

The soft-to-collinear (Grammer–Yennie-type) approximation and the Ward identities then give eq. (74). Converting to $f^{\rm TMD}$ with A5(b),(c) gives the theorem.

**Grade: [A].** Justification:
* The author's own assessment (`[Liu:2022nnk]` §6): "all the proofs in the paper, except the ones for the analyticity, follow the typical rigorous standards in the TMD factorization literature". He adds that promoting these "physical proofs" to "fully mathematically consistent proofs at the level of those works for UV renormalization remains to be an important but difficult task", requiring Minkowski-space multi-scale analysis.
* The PLB version is explicitly only a "sketch of mathematical proof" [txt].
* Independent confirmations: Vladimirov–Schäfer (SCET; one loop) `[Vladimirov:2020ofp]`; Ebert–Schindler–Stewart–Zhao, an all-order proof via a "Large-Rapidity" intermediate scheme, which also shows that there is no flavor mixing `[Ebert:2022fmh]` [abs]; the NNLO coefficient `[delRio:2023pse]` [abs] and `[Ji:2023pba]`.
* One-loop check: **[chk: check_qtmd_1loop.py]**. The formula with $\frac12K$ reproduces APPB (39), (23), (85) exactly. The printed version with $K$ leaves a residual $L_b(L_z-L_\zeta)$.

**Novelty.** Yes. This is the first matching formula between a lattice-computable quasi-TMD and the scheme-independent TMDPDF that has a well-defined, Euclidean-computable non-perturbative soft factor. Earlier proposals (`[Ji:2014hxa]`, `[Ji:2018hvs]`, `[Ebert:2019okf]`) either used soft factors with the wrong IR physics beyond one loop or left a soft factor $g^S_q$ undetermined [txt]. The power-counting formula with the staple in single-line notation is new.

**Relation to CSS.** It reuses the CSS technology (leading regions, Grammer–Yennie, Ward identities, sum over cuts, Glauber deformation). The new aspects are the space-like staple, which must be amputated, and the absence of light-like lines, so that $P^z$ acts as a physical off-light-cone regulator. In the Collins scheme (tilted Wilson lines) the quasi-TMD is literally the unsubtracted TMD boosted by Lorentz invariance (`[Liu:2022nnk]` §3.4). This explains why the CS kernel controls the $P^z$ dependence.

**Presentation.** The central theorem of the frontier chapter (draft in §6.2). It needs a figure of the leading region in single-line and double-line notation (APPB Figs. 16–17), the power-counting box, and an erratum footnote on $\frac12K$.

#### B2. The matching kernel: RGE, decomposition, fixed-order results

*Sources:* `[Ji:2019ewn]` eqs. (23)–(26); `[Liu:2022nnk]` eqs. (82)–(86); `[Ji:2023pba]` (4.1)–(4.11), (5.7), (5.11)–(5.12), App. A [txt].

**RGE.** $\mu\frac{d}{d\mu}\ln H\big(\frac{\zeta_z}{\mu^2}\big)=\Gamma_{\rm cusp}(\alpha_s)\ln\frac{\zeta_z}{\mu^2}+\gamma_C(\alpha_s)$, with
$$
\gamma_C\equiv\tilde\gamma_H=\gamma_V+2\gamma_F+\gamma_{HH}=\gamma_V+2\gamma_F+2\gamma_{HL}-\gamma_s .
$$
In terms of `[Ji:2023pba]` (A.11), $\gamma_V$ is the non-cusp anomalous dimension of the light-quark Sudakov form factor, $\gamma_F$ that of the heavy-light current, $\gamma_{HL}$ the constant of the heavy-light cusp, and $\gamma_s$ the light-like soft constant. (PLB writes $2\gamma_F+\Gamma_S+2\gamma_H$, APPB writes $2\gamma_F-\Gamma_S+2\gamma_J$; with §2, all three agree.)

**One loop:** $H=1+\frac{\alpha_sC_F}{2\pi}\big(-2+\frac{\pi^2}{12}-\frac{L_z^2}{2}+L_z\big)$. This equals the Ebert–Stewart–Zhao form $\frac{\alpha_sC_F}{4\pi}(-L_z^2+2L_z-4+\frac{\pi^2}{6})$ [chk].

**Decomposition [chk: check_HL_and_C1.py].** $H=C_{HL}^+C_{HL}^-$, with a single heavy-light Sudakov factor ($L_\pm=L_z\pm i\pi$)
$$
C_{HL}^\pm=1+\frac{\alpha_sC_F}{8\pi}\Big(-4-\frac{5\pi^2}{6}+2L_\pm-L_\pm^2\Big)+O(\alpha_s^2).
$$
The pair $(C_{HL}^\pm)^2$ is the LFWF kernel $H^\pm_{\rm LFWF}$ of `[Ji:2023pba]` (4.2). Its one-loop phase is $\frac{\alpha_sC_F}{2}(1-L_z)$, consistent with $A^{(1)}=\frac{C_F}{2}(L_z-1)$ up to the sign$(z)$ convention. In the threshold problem $H=|H_{HL}|$ (eq. (4.5)). The phase satisfies $\frac{d\ln H_{HL}}{d\ln\mu}=\Gamma_{\rm cusp}\ln\frac{\zeta_z}{\mu^2}+\tilde\gamma_H-i\pi\,{\rm sign}(z)\Gamma_{\rm cusp}$ (eq. (4.4)).

**Two loops** (`[Ji:2023pba]` (A.13), (5.7), (5.11); conventions (b) of §2):
$$
\tilde\gamma_H^{(1)}=-\frac{C_F}{\pi},\qquad
\tilde\gamma_H^{(2)}=\frac{1188\zeta_3-99\pi^2-1108}{432\pi^2}C_FC_A-\frac{36\zeta_3+6-7\pi^2}{12\pi^2}C_F^2+\Big(\frac1{24}+\frac{10}{27\pi^2}\Big)C_Fn_f,
$$
$$
\ln H^{(2)}=\frac{C_F\beta_0}{24\pi}L_z^3-\frac14\Big(\Gamma^{(2)}_{\rm cusp}+\frac{C_F\beta_0}{2\pi}\Big)L_z^2-\Big(\frac{C_F\beta_0}{4\pi}\Big(-2+\frac{\pi^2}{12}\Big)+\frac{\tilde\gamma_H^{(2)}}{2}\Big)L_z+c_H,
$$
$$
c_H=\Big(\frac{241\zeta_3}{144\pi^2}+\frac{11\pi^2}{320}-\frac{559}{1728}-\frac{971}{324\pi^2}\Big)C_FC_A+\frac{-45\zeta_3-2\pi^4+30\pi^2-30}{24\pi^2}C_F^2+\frac{36\zeta_3+51\pi^2+1312}{1296\pi^2}C_Fn_fT_F .
$$
Numerically $c_H=0.0725\,C_F^2-0.0840\,C_FC_A+0.1453\,C_Fn_fT_F$.

Checks:
* (A.11) = (A.13) given (A.2)–(A.5) [chk: check_gammaC2.py].
* Numerical value of $c_H$ [chk].
* The log structure follows from the RGE [chk: check_RGE_structure.py].
* The $n_f$ parts of $\tilde\gamma_H^{(2)}$ and $c_H$ agree exactly with the independent large-$\beta_0$ (bubble-chain) results of `[Liu:2023onm]` (2.41)–(2.42) [chk]: $(\frac1{24}+\frac{10}{27\pi^2})=\frac{80+9\pi^2}{216\pi^2}$ and $T_F\cdot\frac{36\zeta_3+51\pi^2+1312}{1296\pi^2}=\frac{36\zeta_3+1312+51\pi^2}{2592\pi^2}$.
* The authors verified the full prediction against the exact NNLO quasi-PDF (`[Li:2020xml]`, `[Chen:2020ody]`): 41 singular terms. The result agrees with `[delRio:2023pse]` [txt].
* **Erratum E3:** the earlier $\gamma_C^{(2)}$ in `[Ji:2019ewn]` eq. (26) is incorrect.

**Grade.** RGE structure: **[A]**. Two-loop values: **[P]** (fixed order, cross-checked by three independent routes).

#### B3. Quasi-LFWF amplitudes; the CS kernel from LFWFs; LF quantization as an EFT

*Source:* `[Ji:2021znw]` §§II–V [txt].

**Statements.**
* (i) Light-front quantization is an effective theory: small-$k^+$ (zero) modes are "integrated out", at the price of infinitely many counterterms. The LaMET large-momentum expansion of equal-time correlators is an "effective light-front quantization" (§II.C, eq. (14)). This is a conceptual statement, not a theorem.
* (ii) Rapidity-renormalized LFWF amplitudes $\psi^\pm_N(x_i,\vec b_{i\perp},\mu,\zeta)$ are defined with generalized soft functions $S^\pm_N$ (eqs. (27)–(32)). They obey $2\zeta\partial_\zeta\ln\psi_N^\pm=K_N$ and the RGE (36). The $\pm$ (future/past) versions are related by analytic continuation, e.g. $S_N^{-\dagger}(\delta^+\delta^-)=S_N^+(-\delta^+\delta^-+i0)$ (eq. (31)).
* (iii) **Factorization of quasi-LFWF amplitudes** (eq. (49); with the same $\frac12$ correction as B1, erratum E1):
$$
\tilde\psi^\pm_N\sqrt{S_{rN}}=e^{\frac12\ln\frac{\mp\zeta_z-i0}{\zeta}K_N}H^\pm_N\,\psi^\pm_N+\dots .
$$
For the $q\bar q$ meson amplitude (eqs. (62), (68), (71), (73)) the one-loop rapidity logarithms differ by $\frac12K\ln(\zeta_z/\zeta)$, since $\sqrt{\zeta_z\bar\zeta_z/(\zeta\bar\zeta)}=\zeta_z/\zeta$ [chk-hand]. The kernel $H^\pm_N$ has an imaginary part that does not cancel, unlike the TMDPDF case.
* (iv) $K_N$ from ratios of quasi-LFWFs at two momenta (eq. (51); same $\frac12$ caveat).

**Grade: [A]** (sub-grade A−; "a sketch of its proof is included" [txt]). Universality of $K$ between LFWFs and TMDPDFs is later supported by A6.

**Presentation.** Short subsection: the LFWF as an exclusive analogue, with imaginary parts and the $\pm i0$ choices fixed by exponential decay at LF infinity.

#### B4. Meson form factor at large momentum transfer: extraction of $S_I$

*Sources:* `[Ji:2019sxk]` eqs. (14)–(21); `[Liu:2022nnk]` §5, eqs. (143)–(155); lattice: `[LatticeParton:2020uhz]`, `[LatticePartonLPC:2023pdv]` [txt/abs].

**Statement.** Take $F(b_\perp,P,P',\mu)=\langle P'|\bar\eta(\vec b_\perp)\Gamma'\eta(\vec b_\perp)\bar\psi(0)\Gamma\psi(0)|P\rangle$, with $P,P'$ approaching opposite light-cone directions and $\Gamma=\Gamma'=1$ or $\gamma_\perp$. At large $P^z$ and $b_\perp\gg1/P^z$:
$$
F(b_\perp,P,P',\mu)=S_I(b_\perp,\mu)\int dx\,dx'\,H(x,x')\,\tilde\psi^\dagger(x',b_\perp)\tilde\psi(x,b_\perp)+\dots\qquad(\text{eq. (154)}),
$$
* $H(x,x')=H_1(Q^2,\bar Q^2,\mu^2)/[H_2(\zeta_z,\bar\zeta_z)H_2(\zeta'_z,\bar\zeta'_z)]$, with $Q^2=\sqrt{\zeta_z\zeta'_z}$ and $\bar Q^2=\sqrt{\bar\zeta_z\bar\zeta'_z}$;
* $H_1=H^{\rm Sud}(-Q^2)H^{\rm Sud}(-\bar Q^2)$, a product of space-like Sudakov kernels (eq. (148));
* $\tilde\psi$ are quasi-TMD wave functions (eq. (149)), which themselves factorize as in B3 (eq. (150)).

Interpretation: a gauge-invariant completion of the Collins–Soper axial-gauge factorization. On endpoints: if $x+x'=1$ is imposed, the endpoint behaviour improves to $x^2\ln^2x$.

**Hypotheses.** TMD factorization of this exclusive form factor in the Li–Sterman spirit (`[Liu:2022nnk]` Fig. 25): two hard cores at $0$ and $\vec b_\perp$, two collinear subgraphs, one soft subgraph, Glauber handled as in DY/SIDIS. All gauge links can be chosen future-pointing.

**Grade: [A]** (sub-grade A−) for the factorization; **[P]** for the one-loop checks (eqs. (146)–(147), (153)). The lattice extraction `[LatticeParton:2020uhz]` used leading-order factorization; the later `[LatticePartonLPC:2023pdv]` includes one-loop corrections [abs].

#### B5. Regularization-independent factorization of DY at small $q_T$ in terms of quasi-TMDs

*Sources:* `[Ji:2019sxk]` eq. (22); `[Ji:2019ewn]` eq. (27); `[Liu:2022nnk]` eq. (155) [txt].
$$
\frac{d\sigma_{\rm DY}}{d^2\vec b_\perp\,dx\,dx'}=\hat\sigma(x,x',\mu,\zeta_z,\zeta'_z)\,S_I(b_\perp,\mu)\,\tilde f(x,b_\perp,\mu,\zeta_z)\tilde f(x',b_\perp,\mu,\zeta'_z)+\dots,
$$
with $\sigma(Q^2/\mu^2)=H(\zeta_z/\mu^2)H(\zeta'_z/\mu^2)\hat\sigma$. The CS-kernel factors cancel when $\zeta_z\zeta'_z=\zeta^2=Q^4$. No light-cone limit is needed.

**Grade: [A],** conditional on CSS TMD factorization for DY (graded [A] in the monograph) and on B1.

#### B6. Single transverse-spin asymmetry (Sivers) from quasi-TMDs

*Source:* `[Ji:2020jeb]` [txt §§I–II, structure of III].

**Statement.** The matching kernel is spin independent, because it involves only hard gluons. Hence the ratio of the quasi-Sivers to the unpolarized quasi-TMD at the same $(x,b_\perp,P^z)$ equals the light-cone ratio up to power corrections: $S_I$ and $H$ cancel. The sign of the Sivers function (DY vs. SIDIS) follows from the staple direction $\pm\hat z$.

**Verification.** In the small-$b_\perp$ limit at one loop, the quasi-Sivers function reproduces the collinear twist-3 (Qiu–Sterman) description. The hard-gluon-pole contributions (colour factor $C_A/2$) partly cancel the soft-gluon-pole contributions ($1/2N_c$), leaving a result proportional to $C_F$ for the end-point and pinch-pole terms. This is consistent with soft-gluon radiation and the spin-independent soft-factor subtraction [txt eq. (54) ff.].

**Grade:** general statement **[A]** (sub-grade A−); one-loop twist-3 check **[P]**.

### 3.C Threshold limits and power corrections in LaMET

#### C1. Space-like and time-like heavy-quark jet functions are related by analytic continuation to all orders

*Source:* `[Ji:2023pba]` §3.2, App. C [txt].

**Statement.** Define
* $\tilde J(\mu z)=\langle\Omega|T\,W_{n,+}(zn_z)W_z^\dagger(zn_z)W_z(0)W_{n,-}(0)|\Omega\rangle$ (eq. (3.7); equivalently the cut form (3.6));
* $\tilde J(\mu t)$, the same with $n_z\to n_t$ (eq. (3.14)).

Then, for $t>0$ and to all orders in perturbation theory (DR),
$$
\tilde J(t=-i|z|,D)=\tilde J(z,D).
$$
**Proof 1 (App. C.1).** Coordinate-space Schwinger representation of all $m$-point gluon correlators. Contractions preserve the form $\int D\alpha\,\mathcal P(\alpha)\exp[-\frac i2\sum Q_{ij}(x_i-x_j)^2]$ with $Q\ge0$. All residue poles of the remaining scale parameter $s$ lie in quadrant II, so $s\to-is$ is allowed, after which $t\to-iz$. The spin structures match term by term (eqs. (C.19)–(C.21)).
**Proof 2 (App. C.2).** Wightman functions in the forward tube plus complex Lorentz covariance under $\Lambda$.
Consequence: the two-loop space-like jet function follows from the time-like heavy-quark jet function of Jain–Scimemi–Stewart (`[Jain:2008gb]`). Consistency checks at one loop: $\tilde J=1+\frac{\alpha_sC_F}{2\pi}\big(\frac12l_z^2+l_z+\frac{\pi^2}{12}+2\big)$ with $l_z=\ln\frac{e^{2\gamma_E}\mu^2z^2}{4}$ (eq. (3.9)), and $\frac{d\ln\tilde J}{d\ln\mu}=\Gamma_{\rm cusp}l_z-\tilde\gamma_J$ with $\tilde\gamma_J^{(1)}=-\frac{\alpha_sC_F}{\pi}$ [chk-hand].

**Grade: [A].** The same type of argument as A6, with a full combinatorial sketch.

#### C2. Threshold factorization of the quasi-PDF matching kernel

*Source:* `[Ji:2023pba]` eqs. (1.3), (2.1)–(2.7), (3.17)–(3.19), (4.5)–(4.10), (6.1)–(6.19) [txt].

**Statement.** For the $\overline{\rm MS}$ matching kernel $C$ in $\tilde f(y,P^z)=\int\frac{dx}{|x|}C(\frac yx,\frac{xP^z}\mu)f(x,\mu)$, in the threshold limit $\xi=y/x\to1$:
$$
C\Big(\xi,\frac{xP^z}{\mu}\Big)\Big|_{\xi\to1}=H\Big(\frac{4x^2P_z^2}{\mu^2}\Big)\,|xP^z|\,J_f\Big(\frac{(1-\xi)xP^z}{\mu},\frac{4x^2P_z^2}{\mu^2}\Big)\big[1+O(1-\xi)\big].
$$
* $H=|H_{HL}|$ is real (B2).
* $J_f(z\mu)=\tilde J(z^2\mu^2)\exp[i\,{\rm sign}(z)A(L_z)]$ carries the semi-hard scale $\mu_i=|1-\xi||xP^z|$ and the phase of the Sudakov pair.
* RGEs: $\frac{d\ln H}{d\ln\mu}=\Gamma_{\rm cusp}\ln\frac{\zeta_z}{\mu^2}+\tilde\gamma_H$. The momentum-space jet function satisfies a non-local evolution with the plus/principal-value kernel $-2\Gamma_{\rm cusp}\mathcal P\int_{\xi'>\xi}\frac{J_f(\xi')}{\xi'-\xi}$ (eq. (2.3)).
* Fully resummed form: eq. (6.19), with the star distribution (6.18).

**DGLAP consistency (eqs. (6.4)–(6.8)).** Endpoint matching to $P_{qq}\to\frac{2\Gamma_{\rm cusp}}{(1-z)_+}+2\gamma_\phi\delta(1-z)$ requires $2\gamma_\phi+\tilde\gamma_H-\tilde\gamma_J=2\gamma_F$, which is satisfied by the anomalous-dimension algebra C3.

**Hypotheses and proof.**
* A space-time picture: almost all collinear momentum flows in and out at the two quark–link vertices, because two hard real exchanges with opposite $k_z=O(p_z)$ are phase-space suppressed.
* A leading-region argument in coordinate space at large $|z|$ ($\mu_i\sim1/|z|$), analogous to DIS threshold factorization in SCET.
* The NNLO check: the threshold limit of the exact two-loop kernel `[Li:2020xml]`, `[Chen:2020ody]` reproduces 41 non-vanishing singular terms ($\delta(1-y)$ and $\ln^k(y-1)/(y-1)$, $k\le3$). This fixes two constants, $c_a$ (5.10) and $c_H$ (5.11).
* **One-loop check [chk-hand].** For $0<y<1$ the $\overline{\rm MS}$ quasi-PDF behaves as $\frac{\alpha_sC_F}{2\pi}\frac{2}{1-y}(L_z+\ln(1-y)-1)$, from `[Ji:2020ect]` eq. (89). This equals $J_f^{(1)}$ (eq. (4.10)): $\mathcal P(\frac1{|1-y|})+\mathcal P(\frac1{1-y})=\frac2{1-y}$. For $y>1$ the quasi-PDF gives $\frac{2\ln(y-1)}{y-1}$, which equals $J_f^{(1)}$ because the two principal values cancel.

**Grade: [A]** for the factorization: a leading-region argument with spacetime picture, no complete power-counting proof (sub-grade A−). **[P]** for the explicit NNLO verification.

**Novelty.** Yes. First threshold factorization and resummation of LaMET matching kernels. It establishes that the heavy-light Sudakov kernel is a universal object shared by quasi-TMDs, quasi-LFWFs and the threshold limit of quasi-PDFs. It also gives a non-trivial all-order statement relating space-like and time-like jet functions.

#### C3. Algebra of anomalous dimensions ("critical-exponent relations")

*Source:* `[Ji:2023pba]` App. A [txt].
Basis: $\{\Gamma_{\rm cusp},\gamma_F,\gamma_V,\gamma_s,\gamma_{HL}\}$. Derived quantities:
$$
\gamma_\phi=-\tfrac12\gamma_V-\tfrac12\gamma_s,\quad \gamma_J^{\rm thr}=\tfrac12\gamma_V-\tfrac12\gamma_s,\quad \tilde\gamma_J=2\gamma_{HL}-2\gamma_s,\quad \gamma_{HH}=2\gamma_{HL}-\gamma_s,\quad \tilde\gamma_H=\gamma_V+2\gamma_F+2\gamma_{HL}-\gamma_s .
$$
Two-loop inputs: (A.1)–(A.5) [txt].
* (A.6) $2\gamma_{HL}-\gamma_s=\gamma_{HH}$ and (A.11) ⇒ (A.13) are reproduced symbolically [chk: check_gammaC2.py].
* $\gamma_{HH}^{(2)}$ is reproduced independently from the large-angle cusp anomalous dimension [chk: check_GammaS2.py].
* $\gamma_V$ (A.3) coincides with the standard quark form-factor non-cusp anomalous dimension.
* $\tilde\gamma_J^{(2)}=C_FC_A(-\frac{1396}{27}+\frac{23\pi^2}{9}+20\zeta_3)+C_Fn_f(\frac{232}{27}-\frac{2\pi^2}{9})$ in units of $(\alpha_s/4\pi)^2$ follows from (A.4)–(A.5) [chk-hand].

**Grade.** Structural relations: **[A]** (from the consistency of factorization formulas). Two-loop numbers: **[P]**.

#### C4. Linear IR renormalon of the heavy-light Sudakov kernel; cancellation with next-to-leading-power operators

*Source:* `[Liu:2023onm]` [txt §§1–2, 3.6, 4.3–4.4, 6].

**Statement (large-$\beta_0$ / bubble chain).** The Borel transform of the $\overline{\rm MS}$ heavy-light kernel (eqs. (2.44)–(2.47); $u=\beta_0t/2$) has its first right-half-plane singularity at $u=\frac12$, in the *imaginary part only*:
$$
{\rm Im}\,B(u)\to\frac{\mu}{p^z}\frac{C_Fe^{5/6}}{2\pi}\frac{{\rm sign}(z)}{u-\frac12}.
$$
So the phase angle has the asymptotics $A_{\rm asym}=-2\frac{\mu}{p^z}\sum_nr_n\alpha^{n+1}$ with $r_n=N_m\beta_0^n\Gamma(n+1)$ and
$$
N_m=\frac{C_Fe^{5/6}}{\pi}\simeq0.977\ \text{(large $\beta_0$)},
$$
which is the normalization of the pole-mass and Wilson-line linear renormalon [chk-hand: residue from $V_0(u)$ (eq. (2.45)); numerical value]. The real part has no linear renormalon (App. B).

**Conjecture (eq. (2.52)):** the same $N_m$ holds beyond large $\beta_0$ ($N_m=0.622,\dots,0.524$ for $n_f=0,\dots,5$) — **[C]**.

**Cancellation.**
* (i) In the threshold expansion of space-like quark-bilinear coefficient functions (coordinate and moment space), the $u=\frac12$ IR renormalon of the leading-power hard kernel cancels against the UV renormalon of an explicit next-to-leading-power threshold soft operator (§3.4).
* (ii) In the TMD expansion of the quasi-LFWF, it cancels against the UV renormalon of an NLP soft factor $S_q^\pm$ containing a dimension-1 "high-dimensional Wilson-line cusp" $\hat O=[n_z\infty,0]\int_{-\infty}^0dx^+[0,x^+]D_\perp^2[x^+,-\infty]$ (eqs. (4.28)–(4.33)). The renormalon is tied to the *linear UV divergence*, not to the linear rapidity divergence.
* (iii) The TMD expansion of the quasi-LFWF at bubble-chain level is *not convergent*: residues alternate, and there are exponentially small terms (§4.4).
* (iv) The quark wave-function renormalization in Coulomb gauge also has a linear renormalon (§5).

**Conjecture (eq. (3.50)):** a fully factorized $\lambda\to+i\infty$ (threshold) asymptotics of the *hadronic* quark-bilinear matrix element at moderate $z$, with a non-perturbative threshold soft factor $J(z\Lambda_{\rm QCD})$ — **[C]**.

**Grade:** **[P]** (exact within the large-$\beta_0$ approximation); conjectures **[C]**. Background: IR renormalons as indicators of power corrections in general (`[Beneke:1998ui]`); renormalons and power corrections of quasi-distributions at leading power (`[Braun:2018brg]`). The new element here is a *linear* renormalon specific to the heavy-light (space-like Wilson line) Sudakov kernel of the double-logarithmic factorizations.

**Practical consequence:** explains the slow convergence of the imaginary parts in lattice extractions of the CS kernel [txt].

#### C5. Effects of threshold resummation for large-$x$ PDFs in LaMET

*Source:* `[Ji:2024hit]` [abs/intro]. The matching factorizes into a hard kernel at $xP^z$ times a threshold soft function at $(1-x)P^z$; RG resummation of $\alpha^k\ln^{2k}(1-x)$ follows. The pion valence analysis shows that perturbative matching breaks down when $(1-x)P^z\to\Lambda_{\rm QCD}$ but works when both $xP^z,(1-x)P^z\gg\Lambda_{\rm QCD}$. Leading-renormalon resummation is incorporated. **[P]** (numerical, phenomenological). This fixes the domain of validity $x\in[x_{\min},x_{\max}]$, as in `[Ji:2022ezo]`.

#### C6. GPDs near $x=\pm\xi$

*Source:* `[Su:2026eta]` [txt]. **Claim:** the EFT requirement $2|x\pm\xi|P^z\gg\Lambda_{\rm QCD}$ can be relaxed at large $\xi$. Soft contributions near $x=\pm\xi$ are power suppressed, as in DVCS with a real photon (the double logarithms in $\xi-x_B$ are multiplied by a linear factor $(x_B-\xi)$). The part of the one-loop matching kernel sensitive to $x\pm\xi$ is (eq. (7), from the rendered page)
$$
\Big(\frac{1}{2(y-x)}\mp\frac1{4\xi}\Big)\frac{|x\pm\xi|}{y\pm\xi}\ln\frac{4P_z^2(x\pm\xi)^2}{\mu^2}.
$$
The logarithm of the would-be soft scale $2|x\pm\xi|P^z$ comes multiplied by $|x\pm\xi|$, so it vanishes as $x\to\mp\xi$, plus the virtual $\delta(x/y-1)$ terms.
Reanalysis of four lattice data sets (ETMC20, ETMC21, MSULat23, ETMC25) with complete one-loop matching gives GPDs that are continuous at $x=\pm\xi$, with discontinuous derivatives. This needs the regulator ordering $\epsilon_2\ll|\epsilon_1|\to0$ in eqs. (9)–(10); other orderings diverge.
**Grade [P]:** a power-counting argument with one-loop evidence; no all-order proof.

### 3.D Exactly solvable laboratories for the twist expansion and the OPE

#### D1. 2D U(N) Gross–Neveu: exact twist and threshold expansions; absolute convergence

*Source:* `[Liu:2024omb]` [txt §§1–2.1, 4, 7].

**Object.** The valence "structure function" $\langle p,i|\bar\psi^i(x)\psi^i(0)|p,i\rangle-\langle p,i|\bar\psi^j(x)\psi^j(0)|p,i\rangle=\bar u(p)u(p)\,\mathcal E(z^2m^2,\lambda)$, with $z^2=-x^2>0$ and $\lambda=-p\cdot x$, at order $1/N$ (one ladder diagram). Double Mellin representations in $s$ (coupling) and $u$ (with respect to $z^2m^2/4$), eqs. (2.4), (2.6)–(2.15).

**Results.**
* (i) Explicit **twist expansion** in the Bjorken limit $z^2\to0$ at fixed $\lambda$, to all powers. Hard functions $H_k^{l,p}$ and PDF-like non-perturbative functions $q_k^{l,p}$, $\hat q_k^{(l)}$ appear naturally as Borel integrals.
* (ii) **Renormalon cancellation to all powers.** The poles at $t=n$ cancel between the hard function at power $p$ and the non-perturbative function at power $p+n$, for each $l$. At $t=0$ this is the logarithmic UV–IR cancellation; it is the source of scale/scheme dependence.
* (iii) The leading-power non-perturbative functions are given explicitly, in coordinate space and in momentum-fraction space $0<\alpha<1$, with "zero-mode-type" subtractions at $\alpha=0$.
* (iv) Threshold expansion to next-to-next-to-leading threshold power; resurgence between threshold and "Regge" asymptotics.
* (v) **Theorem (§4):** the twist expansion converges absolutely, pointwise, for every $0<z^2<\infty$ and $\lambda\in i\mathbb R_{\ge0}$. Proof for $F_1$ uses Gamma-function and ${}_1F_1$ inequalities (4.2)–(4.5), a remainder bound (4.7) and dominated sums (4.11), (4.13). For $F_2$, $F_3$: "can be shown in similar ways".

**Checks.** Inequalities (4.2)–(4.5) tested on 4000 random points ($l\le8$, $0<c<\frac12$, $|y|\le40$, $10^{-3}\le\lambda\le10^{2.5}$): every ratio $\le1$ [chk: check_GN_ineq.py]. (4.4) also follows analytically from the product formula for $|\Gamma(x+iy)|$ [chk-hand].

**Grade.** Rigorous within the model at $O(1/N)$, modulo the parts stated to be "similar" (sketched). As a statement about QCD factorization: **[P]** (model-exact).

**Significance.** The author stresses that "the specific structure of the QCD Bjorken limit commonly called 'collinear factorization', strictly speaking, has no exact derivation up to now", because no approximation to QCD works both at $\Lambda_{\rm QCD}$ and in the UV [txt §1]. This paper gives the first exactly worked example of a marginal (asymptotically free) theory in which the twist expansion — hard kernels ⊗ PDF-like functions, with manifest renormalon cancellation — is derived and shown to converge pointwise in coordinate space.

**Presentation.** A highlighted "model theorem" box in the frontier chapter. It anchors the monograph's discussion of what "factorization up to power corrections" means beyond perturbation theory (Ch. 16).

#### D2. Super-renormalizable 2D O(N) quartic model: factorial enhancement and divergence of the momentum-space OPE

*Source:* `[Liu:2025edu]` [txt §§1, 4]. At NLO in $1/N$, the large-$p^2$ OPE of the scalar two-point function has factorial enhancements in high-power coefficient functions. The mechanism is a $\frac1\epsilon\times\epsilon$ effect of IR subtractions combined with bubble-chain logarithms. A typical contribution to the identity-operator coefficient at the $n$-th power is (eqs. (1.1)–(1.2), transcribed from the rendered page)
$$
\mathcal H_{0,0,s_1=n}(p^2)\sim\frac{1}{(p^2)^n}\Big(\frac{g}{4\pi}\Big)^{n+1}\frac{d^n}{dt^n}\Big[\Big(\frac{m^2}{p^2}\Big)^t\psi(1-n-t)-\frac1t\Big]_{t=0},
$$
$$
\mathcal H_{0,0,s_1=n}(p^2)\Big|_{n\to\infty}\to-n!\,\frac{g^{n+1}}{(4\pi)^{n+1}}\frac{m^2}{(p^2)^{n+1}}+n!\,\frac{(-1)^ng^{n+1}}{(4\pi)^{n+1}}\frac{1}{m^2(p^2)^{n-1}}+\dots
$$
The poles of the digamma function at $t=\pm1,\pm2,\dots$ produce factorial growth that **changes the power** ($(p^2)^{-n\mp1}$ instead of $(p^2)^{-n}$).

Findings:
* The enhancements cancel between coefficient functions and condensates only *off-diagonally* across powers, so the momentum-space power expansion **diverges**.
* Making the OPE convergent would require infinitely many redefinitions of operators; a single Borel prescription is not enough.
* In coordinate space the $1/(n!)^2$ suppression keeps the expansion convergent.
* $\overline{\rm MS}$ renormalization factors introduce no factorial growth.

**Grade [P]** (model-exact at NLO in $1/N$). Relevance: this sharpens the distinction, used throughout the monograph, between asymptotic and convergent power expansions.

#### D3. NLSM: trans-series from condensates (with M. Mariño); free energy

*Sources:* `[Liu:2025bqq]` [txt §§1, 5], `[Liu:2026npv]` [abs].
* A manifestly O(N)-symmetric massless perturbative framework for the 2D NLSM, as a limit of the quartic linear sigma model.
* At NLO in $1/N$ it reproduces the perturbative two-point function and its first exponentially small correction, from the condensate of the Lagrangian (trace-anomaly) operator, in full agreement with the exact large-$N$ solution.
* The first positive-axis Borel singularity ($y=2$) of the perturbative self-energy is a **UV** renormalon, cancelled by the ambiguity of the condensate. This is explained by power divergences in the LSM regularization; UV–IR "matching at a common UV point".
* `[Liu:2026npv]` checks the fourth-order free energy against TBA.

**Grade [P].** Relevance: precision test of the "OPE + condensates = trans-series" paradigm underlying the treatment of power corrections.

#### D4. Quasi-PDFs in 2D QCD at large $N_c$

*Source:* `[Ji:2018waw]` [txt]. For 2D scalar and spinor QCD in the $1/N_c$ expansion (axial-gauge canonical quantization, bosonization), the quasi-PDF of a meson tends to the light-cone PDF as $P\to\infty$ at leading and subleading order in $1/N_c$, *without additional renormalization* (2D QCD is super-renormalizable). **[P]** (model check of LaMET; non-perturbative in the coupling).

#### D5. Model and non-perturbative studies (brief)

* `[Liu:2021evw]` (with Zahed; arXiv only): small-size instanton contributions to the quark quasi-PDF and the matching kernel, from semi-classics in the dilute instanton ensemble ($\rho\approx\frac13$ fm). Claims a trans-series structure and substantial effects at current lattice momenta. Model-dependent: **[P]/[C]**.
* `[Kock:2020frx]`: pion and kaon quasi-PDFs in the instanton vacuum. Factorization is "assumed" [abs].
* `[Ji:2020bby]`: 't Hooft model light-front sum rules for the scalar charge and Coulomb energy, regular at $x=0$ (no delta function) [abs]. Relevant for zero-mode questions.

### 3.E Euclidean correlators: renormalization and long-distance asymptotics

#### E1. Exponential decay of space-like correlators; asymptotic forms of quasi-distributions

*Source:* `[Ji:2026vir]` [txt §§1–2, 5, 6].

**Theorem (§5.1, conditional [R]).** Assumptions:
* (S1) spectrum: vacuum; massive one-particle states; multi-particle states with gap $\Delta m>0$ relative to the external state;
* (S2) $\phi$ is a local field, tempered, with power-law bounds;
* (S3) locality.

Then the zero-momentum matrix element without one-particle intermediate states obeys
$$
f(t=0,\vec z)-2Z=O(e^{-\Delta m|\vec z|}),
$$
and the rate is sharp (saturated by forward-singularity contributions). Proof: the two analytic continuations $G_>$ (lower half-plane) and $G_<$ (upper half-plane) agree on the space-like edge by locality, so the (1D) edge-of-the-wedge theorem glues them. A Jensen/subharmonicity argument (`[Fredenhagen:1984bz]`) then transfers the decay in imaginary time to $w=0$.

**Extensions.**
* (§5.2) One-particle intermediate states via a "locality completion" (two one-loop Feynman integrals). Decay rates $M$, $\sqrt{s_0}m$, $m_c(s_0,m,M)$ (eqs. (5.21)–(5.23)). Locality cancels the final-state form-factor singularities.
* (§5.3) An all-order perturbative proof, in $\phi^3/\phi^4$ theories, of the spectral representation and of the exponential decay, via parametric representations.

**Physics results (§§2–3).** Using HQET reduction of the light propagator to a gauge link, dispersive analysis, Lorentz symmetry and heavy-flavor spectra:
$$
\tilde h_{\rm LA}(z,P^z)=\big[A_2e^{i\,{\rm sign}(z)\phi_2}+A_1e^{i\,{\rm sign}(z)\phi_1}e^{-iP^zz}+A_3e^{i\,{\rm sign}(z)\phi_3}e^{iP^zz}\big]e^{-\Lambda|z|}
$$
for the pion quasi-PDF matrix element, with next-to-leading asymptotics $\propto e^{-\Lambda|z|}/|z|$ (eqs. (2.1)–(2.2)). Here $\Lambda$ is a binding energy of a heavy-light meson ($\sim500$ MeV). Analogous forms hold for nucleon PDFs, transversity, helicity, DAs and GPDs (eqs. (2.3)–(2.9)), together with FT error bounds.

**Grade.** §5.1: conditional **[R]** — rigorous given S1–S3 (Wightman framework with a gap); for QCD the axioms are assumed, so **[C]** at that level. Asymptotic forms in QCD: **[A]** (sub-grade A−; HQET reduction plus dispersive arguments, two-loop $\phi^3$ checks).

**Relevance.** These results control the Fourier transform from lattice coordinate space to momentum space, i.e. LaMET as a "forward problem" vs. the "inverse problem" debate (`[Ji:2022ezo]`, `[Dutrieux:2025jed]`).

#### E2. Renormalization of quasi-light-front operators

*Sources:* `[Ji:2020ect]` §III.A; `[Ji:2020brr]`; `[LatticePartonLPC:2021gpi]` [txt/abs].
* **Multiplicative renormalizability** $O_\Gamma^B(z)=Z_J^2e^{\delta m|z|}O_\Gamma^R(z)$, $\overline{\rm MS}$: $\delta m=0$ (eqs. (43), (54)). Proofs (not by Liu, reviewed in the RMP):
  * the auxiliary "heavy quark" field method (`[Dorn:1986dt]`, `[Ji:2017oey]`, `[Green:2017xeu]`), which rests on the BRST renormalizability of the auxiliary-field theory;
  * a diagrammatic all-order analysis (`[Ishikawa:2017faj]`).
  * The quark operator does not mix with gluons or other flavours. Gluon operators work similarly, with a $3\times3$ mixing matrix in which the EOM operator contributes only at $z=0$ (eqs. (59)–(69)).

  **Grade: [R]-level** within renormalization theory, at the same standard as the renormalization of HQET (`[Dorn:1986dt]`). The one-loop $Z_{\psi,z}=1+\frac{\alpha_sC_F}{4\pi}\frac3{\epsilon_{\rm UV}}$ (eq. (55)).
* **Hybrid scheme** `[Ji:2020brr]`. Ratio/RI-type renormalization at $|z|\le z_S$ (leading-twist region). Wilson-line mass subtraction $e^{-\delta m|z|}$ at $|z|>z_S$, matched at $z_S$. The $O(\Lambda_{\rm QCD})$ ambiguity of $\delta m$ (renormalon) is analysed: it changes $\tilde h$ by $e^{-m|z|}$, $m\sim\Lambda$, and is irrelevant at large $P^z$. Physics-based large-$z$ extrapolation is recommended. A scheme construction, not a theorem.
* **Self-renormalization** `[LatticePartonLPC:2021gpi]`: data-driven separation of $\frac{m_{-1}(a)}a+m_0$ and logarithmic factors. Renormalization factors are universal across hadrons and valence-fermion formulations; RI/MOM and ratio schemes show large non-perturbative effects. Lattice methodology.

#### E3. Collinear quasi-PDF factorization (as presented in the RMP)

*Source:* `[Ji:2020ect]` §III.B–C [txt]. The all-order perturbative factorization $\tilde q(y,P^z)=\int\frac{dx}{|x|}C(\frac yx,\frac{\mu}{xP^z})q(x)+O(\frac{\Lambda^2}{(yP^z)^2},\frac{\Lambda^2}{((1-y)P^z)^2})$ is outlined following Ma–Qiu:
* ladder decomposition in light-cone gauge;
* collinear regions $R_i$;
* a BPHZ-like recursive subtraction $C^{n-i}$;
* the OPE route (`[Izubuchi:2018srq]`, `[Ma:2017pxb]`, `[Ma:2014jla]`).

The proof is for perturbative free-quark states; non-perturbative validity is "widely believed" [txt]. **Grade [A]** (the proof is by Ma–Qiu and IJJSZ; Liu is a coauthor of the review only). This is covered in detail by the parallel LaMET (Ji) report; cross-reference it rather than duplicating.

### 3.F Exclusive processes

#### F1. Near-threshold heavy-quarkonium photoproduction in the heavy-quark limit

*Sources:* `[Guo:2021ibg]` [txt §§I–III], erratum/revision `[Guo:2023pqw]` [txt §§I–II, V].

**Statement (LO in $\alpha_s(M_V)$, NRQCD at LO, $M_V\to\infty$).** Near threshold $\xi=1+O(M_N/M_V)$ and $-t\sim M_NM_V$. The amplitude is
$$
\mathcal M=\frac{8\sqrt2\pi\alpha_s(M_V)}{M_V^2}\phi^*(0)\,G(t,\xi)\,(\varepsilon_V^*\cdot\varepsilon),\qquad G(t,\xi)=\frac1{2\xi}\int_{-1}^1dx\,A(x,\xi)F_g(x,\xi,t),\qquad A=\frac1{x+\xi-i0}-\frac1{x-\xi+i0}.
$$
The gluon GPD is $F_g=\frac1{(\bar P^+)^2}\int\frac{d\lambda}{2\pi}e^{i\lambda x}\langle P'|F^{a+i}(-\frac{\lambda n}2)F^{a+}{}_i(\frac{\lambda n}2)|P\rangle$. This is the corrected normalization of `[Guo:2023pqw]` eq. (1); the 2021 definition contained a spurious factor $\frac12$ from a trace.

At $\xi\to1$ the spin-2 moments (gluonic gravitational form factors) dominate:
$$
|G|^2=\frac4{\xi^4}\Big\{\Big(1-\frac{t}{4M_N^2}\Big)E_2^2-2E_2(H_2+E_2)+(1-\xi^2)(H_2+E_2)^2\Big\},
$$
with $H_2=A^g_{2,0}+(2\xi)^2C^g_2$ and $E_2=B^g_{2,0}-(2\xi)^2C^g_2$ (2023 eq. (5); a factor 4 relative to 2021). The cross section is $\frac{d\sigma}{dt}=\frac{\alpha_{\rm EM}e_Q^2}{4(W^2-M_N^2)^2}\frac{(16\pi\alpha_s)^2}{3M_V^3}|\psi_{\rm NR}(0)|^2|G|^2$.

**Grade [P].** The analysis is LO (two-gluon exchange). The claim that the all-order GPD factorization of the high-energy region (`[Ivanov:2004vd]`) persists at threshold is argued, not proven. The truncation to spin 2 is an approximation requiring large $|t|$ and $\xi$ (a cut $\xi>0.4$ in 2023).

**Presentation.** Fits Ch. 13 (exclusive) rather than the TMD frontier. Mention it as an example of a *new factorization regime* together with its erratum history.

---

## 4. Errata and physics checks

### 4.1 Errata found (all verified)

| ID | location | issue | correct form | evidence | status in later papers |
|---|---|---|---|---|---|
| **E1** | `[Ji:2019ewn]` eq. (22); `[Liu:2022nnk]` eqs. (53), (75) (but eq. (52) is correct); `[Ji:2020ect]` eqs. (209)–(210); `[Ji:2021znw]` eqs. (49), (51), (73) | The Collins–Soper factor is printed as $e^{K\ln(\zeta_z/\zeta)}$ or $(\zeta_{z1}/\zeta_{z2})^{K}$. This is inconsistent with each paper's own CS equation $2\zeta\partial_\zeta\ln f=K$ and momentum RGE $P^z\partial_{P^z}\ln\tilde f=K+\mathcal G$. | $e^{\frac12K\ln(\zeta_z/\zeta)}$; ratio $(\zeta_{z1}/\zeta_{z2})^{K/2}=(P^z_1/P^z_2)^K$ | one-loop: [chk: check_qtmd_1loop.py] (TMDPDF); [chk-hand] with PRD105 (62), (68), (71) (LFWF) | APPB (52) has the $\frac12$; the inconsistency persists elsewhere |
| **E2** | `[Liu:2022nnk]` eq. (81); `[Ji:2021znw]` eq. (72) | Two-loop $\Gamma_S^{(2)}$ quoted with the wrong sign relative to the papers' own one-loop $\Gamma_S^{(1)}=+\alpha_sC_F/\pi$. In those conventions $\Gamma_S=-\gamma_{HH}$. | $\Gamma_S^{(2)}=\frac{\alpha_s^2}{\pi^2}C_F\big[C_A(\frac{49}{36}-\frac{\pi^2}{12}+\frac{\zeta_3}{2})-\frac{5}{18}n_f\big]$, i.e. $-\gamma_{HH}^{(2)}$ | [chk: check_GammaS2.py]: Becher–Neubert two-loop cusp AD at large angle, zero-recoil check, $n_f$ running-coupling argument | RMP (2021) has the correct value; JHEP 2023 (A.6) correct (as $\gamma_{HH}$) |
| **E2′** | `[Ji:2020ect]` eqs. (205)–(206) | Printed RGE signs ($d\ln S_r/d\ln\mu^2=+\Gamma_S$) contradict the stated $\Gamma_S^{(1)}=+\alpha_sC_F/\pi$ and $S_r^{(1)}=-\frac{\alpha_sC_F}{\pi}L_b$ | $\mu^2\frac{d\ln S_r}{d\mu^2}=-\Gamma_S$ (equivalently $=\gamma_{HH}$) | [chk-hand] | — |
| **E3** | `[Ji:2019ewn]` eq. (26) | $\gamma_C^{(2)}=\frac1{16\pi^2}(a_1C_FC_A+a_2C_F^2+a_3C_FN_f)$ is incorrect. It differs from the correct value by $-2\gamma^{(2)}_{HH}+\frac{C_Fn_f}{24\pi^2}$ (wrong sign of the two-loop $\Gamma_S$ plus an extra $n_f$ term). The $C_F^2$ term agrees. | `[Ji:2023pba]` (A.13) (§3.B2) | [chk: check_gammaC2.py]; (A.13) verified against the exact NNLO quasi-PDF (41 terms, `[Ji:2023pba]`) and `[delRio:2023pse]` | corrected in JHEP 2023 |
| **E4** | `[Liu:2022nnk]` eq. (81); `[Ji:2020ect]` eq. (208) | The two-loop $L_b^2$ coefficient of $\ln S_I$ ($\mathcal D$) is printed as $\alpha_s^2\beta_0C_F/(2\pi)$ with $\beta_0=-\frac{1}{2\pi}(\frac{11}3C_A-\frac43N_fT_F)$. This $\beta_0$ is the coefficient of $d\alpha/d\ln\mu$, consistent with the kernel formulas (86)/(26), so the $L_b^2$ coefficient is a factor 2 too large. | $\alpha_s^2\beta_0C_F/(4\pi)$ in that convention, i.e. $-\frac{C_F\beta_0^{\rm CTX}}{8\pi^2}\alpha_s^2L_b^2$ | [chk: check_RGE_structure.py], symbolic plus numerical integration of the one-loop running | not revisited |
| **E5** | `[Guo:2021ibg]` eq. (16) (gluon GPD with an extra $\frac12$) and its consequences ((24)–(26)) | normalization of the gluon GPD and GFFs | `[Guo:2023pqw]` eqs. (1), (5) | authors' own revision | corrected 2023 |
| **E6** | `[Liu:2022nnk]` App. F | "edge of the wedge theorem" cited for complex Lorentz covariance of Wightman functions in the extended tube | the Bargmann–Hall–Wightman theorem (`[Streater:1989vi]`). Edge-of-the-wedge enters in gluing/locality, e.g. `[Ji:2026vir]` §5.1. | terminology | `[Liu:2023pjb]` phrases it correctly ("covariant under proper complex Lorentz transforms") |

### 4.2 Statements checked and found correct

* One-loop quasi-TMD, TMD and soft functions and the matching kernel, mutually consistent with the $\frac12K$ factor. $H^{(1)}$ equals the Ebert–Stewart–Zhao form; $\mathcal G^{(1)}=2\zeta_z\partial_{\zeta_z}\ln H^{(1)}$; $\gamma_F^{(1)}=\frac{3\alpha_sC_F}{4\pi}$ follows from APPB (39) [chk].
* $H=C_{HL}^+C_{HL}^-$ and the LFWF pair $(C_{HL}^\pm)^2$ with its phase [chk].
* $\gamma_{HH}^{(2)}$ (JHEP 2023 (A.6)) from an independent computation [chk]. (A.11) ⇒ (A.13) [chk].
* $c_H$ numerics; $n_f$ parts consistent with the independent large-$\beta_0$ results of `[Liu:2023onm]` [chk].
* Two-loop log structure of $\ln H^{(2)}$ in PLB (26), APPB (86) and JHEP (5.7), each with its own $\beta_0$ convention [chk].
* Linear-renormalon residue and $N_m=C_Fe^{5/6}/\pi\approx0.977$ [chk-hand].
* GN inequalities (4.2)–(4.5) [chk].
* The final-state-sum identity (C.1) of JHEP 09 (2024) 030 [chk].
* Power-counting formula (59) and leading region (64)–(68) [chk-hand].
* One-loop threshold structure of the quasi-PDF kernel [chk-hand]. $\tilde\gamma_J^{(2)}$ from (A.4)–(A.5) [chk-hand].
* Tables 1–2 transcribed from the rendered page.

### 4.3 Points that are correct but easy to misread

* "IR divergences starting at the $\alpha_s^4$ order" (static potential, `[Liu:2022nnk]` §3.3), "beyond three loops" (quasi-TMD, §3.3) and "from the 3-loop level" (§4 overview) all refer to the ADM-type ultrasoft effect: $O(\alpha_s^4)$ in $V$ is three loops beyond the tree-level $\alpha_s$ term. The wording differs; quote the static-potential statement, which is unambiguous, and avoid stating an exact first loop order for the quasi-TMD.
* In JHEP 2023, "heavy-light Sudakov form factor $H_{HL}$" denotes the pair at a vertex pair (§2), and the quasi-TMD kernel is $|H_{HL}|$. With a single-vertex factor $C_{HL}$, $H=|C_{HL}|^2$.
* The RMP's "$H$" multiplies $\tilde f$, the PLB's multiplies $f^{\rm TMD}$.

---

## 5. Placement relative to CSS, Collins and SCET; what lies beyond; what is still missing

**What is taken over from CSS/Collins without re-proof.**
* TMD factorization of DY/SIDIS with Collins' soft factor and the square-root definition of $f^{\rm TMD}$ (`[Collins:1984kg]`, `[Collins:1988ig]`, `[Collins:2011ca]`, `[Collins:2012uy]`, `[Collins:2017oxh]`, `[Ji:2004wu]`).
* CS evolution, and the cancellation of Glauber exchanges and final-state interactions in the inclusive processes.

Liu's work does *not* re-derive these. They enter as assumptions, graded [A] in the monograph's Ch. 11. The same framework underlies the global TMD extractions cited in these papers (e.g. `[Scimemi:2019cmh]`), whose large-$b_\perp$ non-perturbative input the lattice program of §3.A–B is meant to provide from first principles.

**What goes beyond CSS.**
1. **Euclidean realizations of soft physics** (A1, A5, B4). The CSS soft factor is turned into (i) an HQET form factor and (ii) the intrinsic soft function $S_I$, obtainable from a meson form factor and quasi-TMDWFs. This made the first lattice extraction of TMD soft physics possible (`[LatticeParton:2020uhz]`, `[LatticePartonLPC:2023pdv]`, `[LatticePartonCollaborationLPC:2022myp]`).
2. **New factorization theorems for lattice-computable objects** (B1–B6): quasi-TMDPDFs, quasi-TMDWFs/LFWFs, meson form factors, Sivers ratios, DY in terms of quasi-TMDs. They are proven at the CSS standard ([A]) with new technical components: the staple in single-line notation, pinch-pole amputation, ultrasoft resummation, and the power-counting formula.
3. **Lemmas that CSS-type arguments use implicitly.** Time-ordering independence (A3, A6). Analyticity in the hyperbolic angle and in regulators (A3, A6). Universality classes of soft functions and their failure for time-like double-ordered and fragmentation-type soft functions (Table 2). DY = SIDIS soft factors in specific regulators (A3(v), A6.4). Factorization of rapidity divergences (A4).
4. **Threshold and renormalon structure of the new hard kernels** (C1–C4). The heavy-light Sudakov kernel is a universal object with an RGE, an NNLO value, and a linear IR renormalon in its phase cancelled by NLP operators.
5. **Exact model laboratories** (D1–D4). They show what "factorization + power corrections" means non-perturbatively: absolute convergence of the coordinate-space twist expansion (D1), divergence of momentum-space power expansions (D2), condensate trans-series (D3).
6. **Axiomatic tools** (A6, C1, E1). Coordinate-space analyticity, tubes, complex Lorentz covariance and exponential clustering are used to prove properties of TMD soft factors and Euclidean correlators. This is new in the TMD literature.

**Comparison with SCET-based derivations.**
* `[Vladimirov:2020ofp]`: quasi-TMD factorization in SCET with a lattice-related soft factor, checked at one loop.
* `[Ebert:2022fmh]`: all-order proof through a "Large-Rapidity" intermediate scheme; also no flavour mixing between quark flavours and gluons.
* `[delRio:2023pse]`: NNLO coefficient.

All agree with B1 once the lattice soft factor is identified with $S_I$. Liu's route is Collins-style (off-light-cone scheme plus Ward identities); ESSZ's is SCET-style (order of limits between the LR and Collins schemes). For the monograph, B1 can be stated once with both routes cited, which raises its credibility within [A].

**What is still missing for [R] (the author's statements and my assessment).**
* A mathematically complete proof of TMD/quasi-TMD factorization requires a rigorous multi-scale analysis of singular Minkowski-space Feynman integrals ("simultaneous decomposition of the longitudinal and transverse phase space") [txt APPB §6].
* The analyticity proofs assume the perturbative Wightman structure of DR correlators at generic $\epsilon$ (A6, T1), plus uniform gaps and light-cone limits (A3, H4–H6).
* Non-perturbative statements (A3, A6, E1 for QCD) are conjectures or conditional.
* Polarized and gluon quasi-TMDs were not treated in the APPB (§6). The double-time-ordered universality for time-like vectors and the $e^+e^-$ soft factor are open (A6(iv)).

---

## 6. Recommendations for the frontier chapter

### 6.1 Proposed structure (Chinese titles; tags in brackets)

**前沿章：大动量有效理论中的TMD因子化与软函数的欧氏化（刘一壮及合作者的工作）**

1. **动机。** 为什么TMD软函数被认为"本质上是闵氏的"；LaMET原理回顾（交叉引用Ji的LaMET章节与第16章）。
2. **离光锥软函数：定义、捏点奇点与部分指数化。** 定理A1 [A]；引理A2(a) [A]；注：超软模式A2(c)。
3. **双曲角解析性、普适类与时序无关性。** 定理A3 [A]（非微扰[C]）；表1、表2；定理A6 [A]，附"Wightman预备知识"框；猜想（复时空Wilson圈）[C]。
4. **快度发散的因子化与本征软函数。** 命题A4 [A]；定理A5 [A]；两圈结构（修正版）[P]。
5. **准TMD因子化定理。** 定理B1 [A]（含领头区域图、幂次计数框、勘误E1脚注）；匹配核的RGE与两圈结果B2（RGE [A]，两圈 [P]）。
6. **介子形状因子、光前波函数与Collins–Soper核。** B3、B4 [A]；B5 [A]；Sivers比值B6 [A]（单圈 [P]）。
7. **阈值极限。** 重-轻Sudakov形状因子、类空喷注函数、阈值因子化与反常量纲代数：C1 [A]，C2 [A]（NNLO [P]），C3 [A]（两圈 [P]）。
8. **重整子与幂次修正；可精确求解的模型。** C4 [P]（猜想 [C]）；D1（模型严格；对QCD为[P]）；D2、D3、D4 [P]。
9. **欧氏关联函数的长程渐近与可计算性。** E1（条件性[R]；QCD中[A]/[C]）；C6 [P]；E2（重整化：[R]级）。
10. **勘误与核对表**（§4）。
11. **严格性等级总表与开放问题**（§7）。

### 6.2 Draft theorem statements (LaTeX, Chinese; ready to port)

```latex
\begin{theorem}[准TMDPDF的因子化（Ji--Liu--Liu 2020；Liu 2022）]\tagA
\label{thm:quasiTMD}
设 $\tilde f(x,b_\perp,\mu,\zeta_z)$ 由沿 $\hat z$ 方向的订书钉形Wilson线与长 $2L$、宽 $b_\perp$ 的矩形Wilson圈
$\sqrt{Z_E}$ 减除定义（$L\to\infty$），$\zeta_z=(2xP^z)^2$。在 $P^z\to\infty$、$b_\perp\gg 1/(xP^z)$ 时，
\begin{equation}
\tilde f(x,b_\perp,\mu,\zeta_z)\sqrt{S_I(b_\perp,\mu)}
=H\!\Big(\frac{\zeta_z}{\mu^2}\Big)\,
\exp\!\Big[\tfrac12 K(b_\perp,\mu)\ln\frac{\zeta_z}{\zeta}\Big]\,
f^{\rm TMD}(x,b_\perp,\mu,\zeta)
+O\!\Big(\frac{\Lambda^2_{\rm QCD}}{\zeta_z},\frac{M^2}{(P^z)^2},\frac{1}{b_\perp^2\zeta_z}\Big),
\end{equation}
其中 $2\zeta\partial_\zeta\ln f^{\rm TMD}=K$，$S_I=e^{-\mathcal D}$ 为本征软函数，$H$ 为微扰匹配核；
准TMD与物理TMD的纵向动量分数相同，匹配中不出现关于 $x$ 的卷积。
\end{theorem}
\begin{proofsketch}
Landau方程给出领头区域（单共线方向；规范线不参与共线发散）；单线记号下的幂次计数
$F(H)\ge0$、$F(SC)\ge0$，领头区域为两条共线夸克、一条软“订书钉”进入硬核，任意纵向共线胶子
与任意软胶子；Glauber区可变形移除；捏点奇点由 $\sqrt{Z_E}$ 截肢、超软模式经偶极自能重求和后
消失；软--共线近似与Ward恒等式得 $\tilde f=H\,[f/S(\delta^+,\delta^-)]\,S(\delta^+,\hat z)$，
再利用本征软函数的等价定义。注：原文 PLB 811 式(22)及若干后续公式中指数缺少因子 $\tfrac12$
（单圈核对见本书附录）。
\end{proofsketch}

\begin{theorem}[DY形TMD软因子的时序无关性与类空形状因子表示（Liu 2024）]\tagA
在维数正规化（$\epsilon\ne0$）、线性协变规范的微扰论各阶，若胶子Wightman函数满足谱条件与局域对易性，
则指数正规子下的DY形软因子 $S(b_\perp,\nu,\epsilon)$ 具有无割线的阈下参数表示，且等于单一时序的
类空形状因子 $S_t(b_\perp,\nu,\epsilon)$。更一般地，含有限光前长度、离光锥倾斜与横向规范线的规范不变
版本满足 $S^{\rm full}(L^+,L^-,b_\perp,\nu,Y,\epsilon)=S^{\rm full}_t(-iL^-,-iL^+,b_\perp,\nu,Y,\epsilon)$。
\end{theorem}

\begin{theorem}[准PDF匹配核的阈值因子化（Ji--Liu--Su 2023）]\tagA
当 $\xi=y/x\to1$ 时，
$C\big(\xi,\tfrac{xP^z}{\mu}\big)=H\big(\tfrac{4x^2P_z^2}{\mu^2}\big)\,|xP^z|\,
J_f\big(\tfrac{(1-\xi)xP^z}{\mu},\tfrac{4x^2P_z^2}{\mu^2}\big)\,[1+O(1-\xi)]$，
其中 $H$ 为重-轻Sudakov形状因子对的模，$J_f$ 为带相位的类空重夸克喷注函数；该式在NNLO与精确两圈
结果的全部41个奇异项一致（\tagP）。
\end{theorem}

\begin{theorem}[2D $U(N)$ Gross--Neveu模型中扭度展开的绝对收敛（Liu 2024）]\tagP
在 $1/N$ 展开的次领头阶，价“结构函数” $\mathcal E(z^2m^2,\lambda)$ 的Bjorken极限扭度展开
（硬函数与类PDF非微扰函数的Borel积分表示，重整子极点在不同幂次间相消）对任意 $0<z^2<\infty$、
$\lambda\in i\mathbb R_{\ge0}$ 逐点绝对收敛。（模型内为严格结果；作为QCD因子化的陈述记为部分。）
\end{theorem}
```

### 6.3 Figures to draw (TikZ)

1. Quasi-TMD staple with the $Z_E$ rectangle (APPB Fig. 3).
2. Off-light-cone DY loop vs. the HQET form-factor picture (NPB Fig. 1, APPB Fig. 2).
3. Single-line notation and dipole 2PI decomposition (APPB Figs. 5, 7).
4. Leading region in single- and double-line notation (APPB Figs. 16–17).
5. The analyticity strip $-\pi\le{\rm Im}\,\theta\le\pi$ with the six configurations of Table 1.
6. Complex Lorentz map $\Lambda(t,z)=(iz,it)$ taking $S_t$ to $S$ (JHEP 2024).
7. Space-time picture of threshold factorization: DIS vs. quasi-PDF (JHEP 2023 Fig. 2).
8. Borel plane of the heavy-light kernel ($u=\frac12$ pole in Im only).

---

## 7. Open problems

1. **Mathematical rigor of quasi-TMD and TMD factorization:** a multi-scale analysis in Minkowski space (`[Liu:2022nnk]` §6).
2. **Perturbative Wightman axioms for DR correlators** at generic $\epsilon$, in massless gauge theory (spectral condition and locality order by order). This is the key missing lemma behind A6 and C1 (`[Liu:2023pjb]` §4, item 2).
3. **Non-perturbative status** of the complex-space-time Wilson-loop conjecture (`[Liu:2023pjb]` §3.4) and of the uniform-gap hypotheses (A3).
4. **Universality of double-time-ordered soft functions with time-like vectors:** equality or inequality of heavy-quark TMDPDF and fragmentation soft factors to all orders (`[Liu:2022nnk]` §6). The $e^+e^-$ (fragmentation) soft factor in a Wightman framework (`[Liu:2023pjb]` §4, item 4; `[Collins:2023cuo]`).
5. **Polarized and gluon quasi-TMDs** within the $S_I$ framework (partly addressed by `[Ebert:2022fmh]`: no mixing).
6. **Beyond-large-$\beta_0$ normalization** of the linear renormalon of the heavy-light kernel (conjecture (2.52) of `[Liu:2023onm]`). The threshold conjecture (3.50) for hadronic matrix elements.
7. **Convergence vs. asymptoticity** of twist expansions in four-dimensional QCD. The model results D1–D2 suggest coordinate-space convergence and momentum-space divergence. A general theorem is lacking.
8. **Rigorous control of the ultrasoft and "ultra-ultrasoft" modes** to all orders (A2(c)), and of the IR control assumed in the rapidity-slicing proof (A4).
9. **Factorization near $x=\pm\xi$ for GPDs** beyond one loop (C6). Near-threshold quarkonium factorization beyond LO and at moderate $M_V$ (F1).

---

## 8. Bibliography notes

* `yzliu.bib` holds the 30 relevant Liu papers (groups I–VII as cited) and 52 context references (CSS/Collins, SCET quasi-TMD derivations, renormalization proofs, cusp anomalous dimensions, exponentiation, analyticity, NNLO quasi-PDF, lattice TMD works, axiomatic QFT). Each comes from INSPIRE, and each entry with a DOI was cross-checked against Crossref (title, journal, volume, page/article, year).
* Manual corrections:
  * `LatticeParton:2020uhz`: INSPIRE merges PRL 125, 192001 with PoS LATTICE2021 477 and exports the PoS DOI. The entry uses DOI 10.1103/PhysRevLett.125.192001 and the published title "Lattice QCD Calculations of Transverse-Momentum-Dependent Soft Function through Large-Momentum Effective Theory", per Crossref.
  * `Liu:2023onm`: JHEP volume = issue 02.
  * `Collins:2011zzd`: the 2011 print DOI 10.1017/CBO9780511975592 instead of the 2023 OA DOI.
  * `Ji:2022ezo`: published title in *Research* 8 (2025) 0695 differs from the arXiv title (noted).
  * `Streater:1989vi`: Princeton Landmarks edition (ISBN 0-691-07062-8), verified via Open Library.
* arXiv-only items (no journal version on INSPIRE as of 2026-10-10): `Ji:2026vir`, `Su:2026eta`, `Liu:2021evw`, `Liu:2026npv`, `Liu:2023eve`, `Liu:2023tft`, `Liu:2026rew`.
* The habilitation summary is cited for career data only:
  `https://habilitacje.bip.uj.edu.pl/documents/143381317/155189849/Yizhuang+Liu_opis_kariery_zawodowej/1e34461d-a3e7-4962-8042-a1b80ebc6b4e`.
  It contains personal identifiers that must not be reproduced.
* `Kugo:1979gm` (covariant operator formalism, cited in `[Liu:2023pjb]` fn. 4) was added after INSPIRE and Crossref verification (Prog. Theor. Phys. Suppl. 66 (1979) 1–130, doi:10.1143/PTPS.66.1). The bib file therefore has 82 entries.
