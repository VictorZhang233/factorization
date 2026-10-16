# Shared context for all agents — QCD factorization monograph

WORK DIR (persistent): `/Users/hao-cheng/Desktop/theorem proof/qcd_factorization_work`
**The path contains a space ("theorem proof").** Always quote paths in shell commands
(e.g. `cd "/Users/hao-cheng/Desktop/theorem proof/qcd_factorization_work/research/c_dis"`).
For LaTeX test builds: `cd` into your own directory, copy the needed files from `../../common/`
into it, and use RELATIVE paths in `\input{...}` (TeX dislikes spaces in paths).

Common files (`common/`): `preamble_fact.tex` (the monograph preamble: ctexbook, chapters, theorem
environments incl. `conjecture`, rigor tags `\tagR \tagA \tagP \tagC \tagV`, environment `proofsketch`,
macros `\ii \dd \ee \tp \MSbar \order{} \Lqcd \as \kT \bT \qT \pT \sla{}`, TikZ styles),
`fd_styles.tex` (plain-TikZ Feynman styles: quark, gluon, photon, ghost, mom, vertex, blob ...),
`fd_styles_ext.tex` (wilson, wilson plain, cut, hard blob, jet blob, jetB blob, soft blob,
hadron blob, glauber, opvertex, scalar, longit + `\longitmark{(A)}{(B)}`, lcaxis, region).

Python3 with numpy 2.0 and sympy 1.14: run `python3 -I script.py`; inside scripts first do
`import sys,os; sys.path.append(os.path.expanduser('~/Library/Python/3.9/lib/python/site-packages'))`.
`pdftoppm` renders PDFs to PNG (Ghostscript is broken; PIL not installed).

## PROJECT
A Chinese-language LaTeX monograph (ctexbook, XeLaTeX; TeX Live 2022 with ctex, tikz, pgfplots,
amsthm, mathtools, slashed, cleveref, tcolorbox, booktabs, enumitem, dsfont, placeins) titled roughly
"QCD 因子化定理：严格证明、全阶论证与适用边界". The user's request (verbatim): "用 LaTeX 写一个 PDF 文件，
严格、完整、详细地证明 QCD 因子化定理（包含各种情况，严格的和不严格的），同样要求费曼图（用 TikZ 画）、
公式、论证清晰。这将是个更困难更大的任务，尽全力、不计成本去做。" A previous monograph by the same team
(Furry's theorem in QCD, `/Users/hao-cheng/Desktop/theorem proof/furry_qcd.tex`) sets the quality bar.

## BINDING CONVENTIONS
- ħ = c = 1; metric (+,−,−,−). Light-front: v^± = (v^0 ± v^3)/√2, v_T = (v^1,v^2);
  v·w = v^+w^- + v^-w^+ − v_T·w_T. Hadron A moves in +z: P_A = (P_A^+, M_A²/(2P_A^+), 0_T);
  hadron B in −z. Rapidity y = ½ ln(k^+/k^-).
- QCD: D_μ = ∂_μ − i g A^a_μ t^a (Peskin–Schroeder; quark–gluon vertex i g γ^μ t^a; Tr(t^at^b) = δ^{ab}/2;
  C_F = 4/3, C_A = 3, T_F = 1/2 for SU(3)); α_s = g²/(4π).
- Dimensional regularization D = 4 − 2ε; MS-bar: μ² → μ² e^{γ_E}/(4π) (S_ε = (4π)^ε e^{−εγ_E}).
- β: μ² dα_s/dμ² = −(β_0/(4π)) α_s² + O(α_s³), β_0 = (11/3)C_A − (4/3)T_F n_f.
- Wilson line along a path from a to b: W[b,a] = P exp( i g ∫_a^b dz^μ A^a_μ(z) t^a ), points closer to b
  to the left; gauge transformation W → U(b) W U†(a).
- Collinear quark PDF (hadron along +z):
  f_{q/H}(ξ;μ) = ∫ dw^-/(4π) e^{−iξP^+w^-} ⟨P| ψ̄(w) γ^+ W[w,0] ψ(0) |P⟩, w = (0^+, w^-, 0_T),
  colour summed, spin averaged, MS-bar renormalized; antiquark f_{q̄}(ξ) = −f_q(−ξ).
- DGLAP: ∂f_i(x,μ)/∂ln μ² = (α_s(μ)/(2π)) Σ_j (P_ij ⊗ f_j)(x), (P⊗f)(x) = ∫_x^1 (dξ/ξ) P(x/ξ) f(ξ).
  Plus distribution: ∫_0^1 dz [g(z)]_+ h(z) = ∫_0^1 dz g(z)[h(z) − h(1)].
- DIS: Q² = −q², x = Q²/(2P·q), y = P·q/P·ℓ;
  W^{μν} = (−g^{μν} + q^μq^ν/q²)F_1 + (P^μ − (P·q/q²)q^μ)(P^ν − (P·q/q²)q^ν) F_2/(P·q);
  F_L = F_2 − 2xF_1; parton model F_2 = Σ_q e_q² x [q(x) + q̄(x)].
- TMD Fourier convention: f̃(x,b_T) = ∫ d^{2−2ε}k_T e^{−i k_T·b_T} f(x,k_T); b_0 = 2e^{−γ_E}; μ_b = b_0/b_T.
- SCET (only in the SCET chapter): n = (1,0,0,1), n̄ = (1,0,0,−1), n·n̄ = 2,
  p^μ = n̄·p n^μ/2 + n·p n̄^μ/2 + p_⊥^μ; n̄·p = √2 p^+, n·p = √2 p^- (n along +z).
- Rigor tags used throughout the monograph (macros \tagR etc.):
  [R] 严格：在重整化微扰论的每一阶有数学上完整的证明（或本文给出完整证明）；非微扰有效性另行说明。
  [A] 全阶论证：有标准的全阶微扰论证明，文献中公认，但部分步骤的完整细节只以概要形式存在。
  [P] 部分：只在有限阶、特定模型或特定子类中被证明/验证。
  [C] 猜想：广泛使用但未被证明，或已知证明有缺口。
  [V] 破坏：已知不成立（有显式反例或证明）。

## OUTLINE v0 (lead author's draft; titles in English, document in Chinese)
Front matter: abstract; TOC; notation; legend of rigor tags.
Ch1 Introduction: parton model & physical picture (time dilation/incoherence); general form
σ = Σ H ⊗ f ⊗ f + power corrections; what "proof" means (asymptotic expansion in Λ/Q, all orders in α_s;
perturbative vs nonperturbative validity); rigor taxonomy; boxed overview table of all theorems with status;
misconceptions; organisation.
Ch2 Preliminaries: QCD, Feynman rules, light-front coordinates, Sudakov decomposition; Wilson lines
(definition, gauge covariance, Feynman rules for eikonal lines incl. iε for future/past pointing, eikonal
identity); DR, renormalization, MS-bar, RG, running coupling, asymptotic freedom; distributions (plus,
Mellin transform, convolution); cut diagrams, optical theorem, unitarity/cutting rules.
Ch3 Infrared structure: Landau equations (necessary conditions for pinch singularities; proof in
Feynman-parameter space); pinch vs endpoint; Coleman–Norton theorem; pinch singular surfaces in massless gauge
theories; reduced diagrams for e+e-, DIS, SIA, DY; power counting (Sterman / Libby–Sterman): normal variables,
collinear/soft/ultrasoft/Glauber scalings, IR degree of divergence ω(R), leading regions; KLN & Bloch–Nordsieck,
IR safety; method of regions (statement, example: off-shell Sudakov form factor; status).
Ch4 Rigorous core I — e+e- total cross section: R ratio, optical theorem, current correlator, spectral
representation, analyticity; theorem: IR finiteness to all orders and R = R_0(1 + α_s/π + O(α_s²)); explicit
O(α_s) real+virtual computation in DR; Euclidean OPE of the correlator, condensates (status), duality & smearing
(Poggio–Quinn–Weinberg).
Ch5 Rigorous core II — DIS and the light-cone OPE: kinematics, hadronic tensor, forward Compton amplitude,
analyticity in ω, dispersion relation, moments; twist; light-cone OPE with twist-2 operators; Wilson
coefficients; RG, anomalous dimensions; theorem (moment factorization) [R in PT]; from moments to x-space
(Hausdorff/Müntz uniqueness from even moments; identification with operator-defined PDFs; DGLAP from anomalous
dimensions); one-loop Wilson coefficients and anomalous dimensions; higher twist, target-mass corrections.
Ch6 Operator definitions of PDFs and FFs: Collins–Soper definitions; gauge invariance; light-cone gauge
number-density interpretation; support 0 ≤ ξ ≤ 1; moments = twist-2 matrix elements; renormalization, DGLAP
from operator renormalization; explicit one-loop P_qq from the operator in Feynman gauge with Wilson line;
PDFs of partonic targets in DR (scaleless integrals); sum rules; positivity issues in MS-bar; fragmentation
functions & timelike DGLAP; polarized PDFs (brief).
Ch7 General method of all-order factorization proofs: strategy (regions → approximations → Ward identities →
subtractions → factorized form); Collins' subtraction formalism (successive approximations, analogue of the
BPHZ forest formula); collinear approximation & Grammer–Yennie decomposition; graphical Ward identities
(abelian → non-abelian with ghosts); collinear Wilson lines; soft approximation & soft Wilson lines;
unitarity/sum over cuts for inclusive observables; Glauber region (definition, why problematic, contour
deformation); renormalization, factorization-scale dependence, scheme dependence.
Ch8 DIS all-order factorization (momentum-space proof): leading regions; factorization step by step;
final-state interactions cancel by unitarity; theorem [A] (consistent with Ch5 [R]); one-loop check: quark and
gluon coefficient functions for F_2, F_L in MS-bar; factorization-scale independence at O(α_s); schemes (MS-bar
vs DIS); heavy quarks (brief).
Ch9 e+e- → h X and fragmentation functions; event shapes / jets (IR safety) bridging to SCET.
Ch10 Drell–Yan and hadron–hadron collisions: kinematics; leading regions incl. spectator soft/Glauber
exchanges; initial- vs final-state interactions; Glauber pinch; cancellation argument (Bodwin; Collins–Soper–
Sterman 1985, 1988): contour deformation, unitarity sum over spectator cuts, eikonalization, soft factor = 1 for
inclusive; explicit abelian one-exchange example; status [A] with honest discussion of gaps; one-loop MS-bar
coefficient functions for qq̄ and qg channels; other hadron–hadron processes (W/Z, Higgs, high-p_T jets/hadrons,
heavy quarks) and their status.
Ch11 TMD factorization: small q_T, Sudakov logs, regions; TMD definitions with staple Wilson lines, transverse
links, rapidity divergences and regulators, soft factor; factorization theorem for DY/SIDIS/e+e- → h1 h2 X [A];
Collins–Soper evolution, RG, one-loop CS kernel, CSS resummation, nonperturbative large-b; small-b OPE onto
collinear PDFs; process dependence & Sivers sign change (T-reversal) [R given factorization]; one-loop checks.
Ch12 Breakdown of factorization and non-rigorous cases: TMD factorization breaking in hadron–hadron →
back-to-back hadrons (Collins–Qiu 2007, Rogers–Mulders 2010) [V]; Glauber operators (Rothstein–Stewart 2016);
super-leading logarithms; violation of strict collinear factorization for space-like splittings
(Catani–de Florian–Rodrigo 2012); diffractive factorization: proof for diffractive DIS (Collins 1998) vs failure
in hadron–hadron diffraction [V]; multiparton interactions / double parton scattering (status); small-x k_T
factorization, BFKL, saturation [P/C].
Ch13 Hard exclusive processes: light-cone DAs, pion form factor (Lepage–Brodsky, Efremov–Radyushkin), LO hard
kernel and asymptotic limit, ERBL evolution, endpoint issues, Sudakov suppression; GPDs, DVCS and hard exclusive
meson production (Collins–Frankfurt–Strikman; Ji; Radyushkin), status; transverse-photon meson production and
endpoint divergences.
Ch14 Effective-field-theory proofs: SCET modes and power counting (hard, collinear, soft, ultrasoft, Glauber;
SCET_I vs SCET_II); Lagrangian; collinear Wilson lines W_n; ultrasoft decoupling field redefinition Y_n (proof at
LO); dijet/thrust factorization H J⊗J⊗S with RG consistency; B → Dπ (all orders in α_s at leading power) vs
B → ππ QCD factorization (BBNS, endpoint divergences at subleading power) [P]; zero-bin subtractions; rapidity
RG; what the EFT assumes (Glauber).
Ch15 Heavy quarkonium: NRQCD, velocity power counting; decay factorization (BBL) [A]; production factorization
conjecture [C], NNLO tests with gauge-completed operators (Nayak–Qiu–Sterman) [P].
Ch16 Power corrections, renormalons, non-perturbative issues: higher twist in DIS (twist-4), twist-3 and
single-spin asymmetries (Qiu–Sterman); renormalons (asymptotic series, IR renormalon ambiguities ↔ higher-twist
matrix elements; large-β_0 example); status of factorization beyond perturbation theory; lattice approaches
(LaMET quasi-PDFs, pseudo-PDFs and their own factorization theorems).
Ch17 Summary: master table of rigor levels; open problems.
Appendices: A light-front coordinates, plus distributions, Mellin transforms; B Wilson-line Feynman rules &
eikonal identities (proofs); C DR integrals; D proof of Landau equations & Coleman–Norton; E derivation of the
power-counting formula; F graphical Ward identities (proof sketch, non-abelian); G one-loop calculations in
detail (DIS, DY, e+e-, P_qq, TMD); H annotated bibliography.
