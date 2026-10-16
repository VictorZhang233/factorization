# research/c_glauber — Glauber region, factorization breaking, colour algebra

Directory: `"/Users/hao-cheng/Desktop/theorem proof/qcd_factorization_work/research/c_glauber"` (note the space).
Scripts: `scripts/`; logs: `logs/`; LaTeX snippets: `tex/`.

Everything below is either (a) derived here and checked by a script (check IDs in brackets, e.g. **[SS1d]**),
or (b) a statement of the literature whose text I read in this session (arXiv version given; equation
numbers refer to that version), or (c) explicitly flagged as **not verified**.

---------------------------------------------------------------------------------------------------------

## 0. Scope, conventions, sources, verification summary

### 0.1 Files

| file | content | result |
|---|---|---|
| `scripts/glauber_poles.py` | pole half-planes for all one-gluon attachment classes (DY, DIS, e+e-); two-pole residue; E7.24; DIS FSI deformation; DY S–S trapping; power counting | 22/22 PASS |
| `scripts/ss_exchange.py` | exact residue derivation of the spectator–spectator Glauber kernel; b-space phase; exponentiation; Δ-integrated cancellation; non-abelian colour phase; DY active–spectator deformation | 23/23 PASS |
| `scripts/unitarity_cuts.py` | cut-sum (unitarity) identity; Aybat–Sterman eikonal & causal identities; S–S cut graphs; colour-matrix phase; ladder vs crossed colour | 58/58 PASS |
| `scripts/colour_factors.py` | SU(N) identities; QVY Table I; BBMP C_G; closed formula C_G = 1+2⟨T_a·T_b⟩/C_F (numeric + exact symbolic N); BBMP links; Rogers–Mulders colour factors; entanglement test | 32/32 PASS |
| `scripts/tmd_breaking_abelian.py` | Collins–Qiu / Collins 2007 / Rogers–Mulders eikonal algebra; anomaly functions I1, I2; Cauchy–Schwarz proof of I1(0)+I2(0)<0 | 31/31 PASS |
| `scripts/diffraction.py` | DDIS vs hadron–hadron pole structure; unitarity vs gap selection (dipole toy, abelian and SU(3)) | 12/12 PASS |
| `scripts/spacelike_colour.py` | CdFR colour algebra (coherence, eq.(68), non-factorization, eq.(187)); FSS cancellation pattern (Tr[SA]=0, double commutator) | 25/25 PASS |

Total: **203 checks, 203 PASS, 0 FAIL** (logs in `logs/*.log`; run with `python3 -I script.py`).

### 0.2 Conventions (binding, CONTEXT.md)

* Metric (+,−,−,−); light front `v^± = (v^0 ± v^3)/√2`, `v·w = v^+w^- + v^-w^+ − v_T·w_T` (`v_T·w_T` Euclidean).
  Hadron A along +z (large plus momentum), hadron B along −z. `n_A·k = k^-`, `n_B·k = k^+` for
  `n_A=(1^+,0^-,0_T)`, `n_B=(0^+,1^-,0_T)`.
* Scalings (λ = m/Q): A-collinear `(1, λ², λ)Q`; B-collinear `(λ², 1, λ)Q`; soft `(λ, λ, λ)Q`;
  **Glauber** `k ~ (λ², λ², λ)Q`, i.e. `|k^+k^-| ≪ k_T²`.
* `D_μ = ∂_μ − i g A^a_μ t^a`; quark–gluon vertex `+ i g γ^μ t^a`; for a charged scalar `D = ∂ − i e A` the vertex is
  `+ i e (p+p')^μ`; propagators `i/(p²−m²+i0)`, gluon `−i g_{μν}/(k²−m_g²+i0)`; `Tr(t^at^b)=δ^{ab}/2`.
* Antitriplet generator `t̄^a = −(t^a)^T`. Catani–Seymour colour charges (all partons outgoing): outgoing quark `T=t`,
  outgoing antiquark `T=−t^T`, incoming quark = outgoing antiquark, incoming antiquark = outgoing quark;
  colour conservation `Σ_k T_k |M⟩ = 0`.
* Wilson line `W[b,a] = P exp(i g ∫_a^b dz^μ A^a_μ t^a)`. With `A(x) = ∫ đ^4k e^{−ik·x} Ã(k)` the one-gluon terms are
  (derived): `W[∞n,0] ⊃ g t^a n^μ Ã_μ(k)/(n·k − i0)`, `W[−∞n,0] ⊃ g t^a n^μ Ã_μ(k)/(n·k + i0)`, so the
  future-minus-past difference of the one-gluon term is `2πi g t^a n^μ δ(n·k)` (the T-odd "gluonic pole" term).

### 0.3 Sources read in this session (texts verified; arXiv versions)

Collins–Qiu PRD 75 (2007) 114014 [arXiv:0705.2141v2]; Collins arXiv:0708.4410v1 (no journal publication);
Rogers–Mulders PRD 81 (2010) 094006 [arXiv:1001.2977v2]; Bacchetta–Bomhof–Mulders–Pijlman PRD 72 (2005) 034030
[hep-ph/0505268v2]; Qiu–Vogelsang–Yuan PRD 76 (2007) 074029 [arXiv:0706.1196v1]; Vogelsang–Yuan PRD 76 (2007)
094013 [arXiv:0708.4398v1]; Collins PRD 57 (1998) 3051 [Erratum PRD 61 (2000) 019902] [hep-ph/9709499v2];
Collins–Frankfurt–Strikman PLB 307 (1993) 161 [hep-ph/9212212v1]; Catani–de Florian–Rodrigo JHEP 07 (2012) 026
[arXiv:1112.4405v2]; Forshaw–Seymour–Siódmok JHEP 11 (2012) 066 [arXiv:1206.6363v2]; Forshaw–Kyrieleis–Seymour
JHEP 08 (2006) 059 [hep-ph/0604094v2]; Becher–Neubert–Shao PRL 127 (2021) 212002 [arXiv:2107.01212v1];
Aybat–Sterman PLB 671 (2009) 46 [arXiv:0811.0246v1]; Collins–Soper–Sterman review (Adv. Ser. Direct. HEP 5 (1989) 1)
[hep-ph/0409313v1]; Rothstein–Stewart JHEP 08 (2016) 025 [arXiv:1601.04695v3]; CDF PRD 86 (2012) 032009
[arXiv:1206.3955]; Guan–Herzog–Ma–Mistlberger–Suresh JHEP 01 (2025) 090 [arXiv:2408.03019v1].
INSPIRE abstracts (verified, from `research/survey/inspire_raw`): CSS 1983, 1985, 1988; Bodwin 1985; BBL 1981;
Lindsay–Ross–Sachrajda 1982, 1983; Brandt–Frenkel–Taylor 1989; Doria–Frenkel–Taylor 1980; Frenkel–Gatheral–Taylor
1984; Cardy–Winbow 1974; DeTar–Ellis–Landshoff 1975; Henyey–Savit 1974; Landshoff–Polkinghorne 1971; Bjorken 1993;
CDF 1997 (W), CDF 2000 (dijets); ACTW 1999; H1 2006, 2007; ZEUS 2008; Klasen–Kramer 2008; CMS 2013; Gaunt 2014;
Zeng 2015; Schwartz–Yan–Zhu 2018; DGOPS 2016; Rogers 2013; FKS 2008; BNSS 2023; BHMN 2025; Banfi–Forshaw–Holguin 2026;
Dixon–Herrmann–Yan–Zhu 2020.

**Not available / not verified:** Collins, *Foundations of Perturbative QCD* (2011; OA reissue 2023): the OAPEN
copy is behind an anti-bot challenge and Cambridge Core loads chapters dynamically, so **no equation or section
number of the book is quoted here**. Full texts of Bodwin 1985 and CSS 1985/1988 (not on arXiv): only their
abstracts were read. CDF PRL 84 (2000) 5043: abstract only; the "factor O(10)" is quoted from CDF's own summary in
arXiv:1206.3955. An earlier (interrupted) draft of `unitarity_cuts.py` claimed a sign misprint in a specific
equation of Collins (2011); this could not be verified and has been **withdrawn**.

---------------------------------------------------------------------------------------------------------

## 1. Glauber pinch in Drell–Yan

### 1.1 Why the Glauber region is leading power **[P5]**

For one extra gluon exchanged between a spectator of A and a spectator of B (Glauber scaling), relative to the
graph without it: measure `dk^+dk^-d²k_T ~ λ^6Q^4`; gluon propagator `1/k² ≈ −1/k_T² ~ λ^{-2}Q^{-2}`; two new
spectator propagators, each off shell by `O(λ²Q²)`: `λ^{-4}Q^{-4}`; numerator: couplings to the large components
`(2p_A^+)(2p_B^-) ~ Q²`; active lines keep virtuality `O(λ²Q²)`. Product: `λ^0 Q^0`. (CSS review §8: the Glauber
region gives "a contribution of order Q^0 times logarithms" — verified.)

### 1.2 Pole structure of one-gluon exchange between the two collinear subgraphs **[P1a–g, SS1a]**

Routing: the exchanged momentum `k` flows from the B-side line Y into the A-side line X. Final spectator momenta
`p_A'`, `p_B'` (on shell); active partons `l_a = P_A − p_A'`, `l_b = P_B − p_B'`. To leading power in the Glauber
region (errors of relative order λ²):

$$
\begin{aligned}
D_{sA}&\equiv(p_A'-k)^2-m_s^2+i0=-2p_A'^{+}\,(k^- - c_A)+i0, & c_A&=\frac{2\,p'_{A,T}\!\cdot k_T-k_T^2}{2p_A'^{+}},\\
D_{a}&\equiv(l_a+k)^2-m_a^2+i0=2l_a^{+}\,(k^- - d_A)+i0, & d_A&=\frac{(l_{a,T}+k_T)^2+m_a^2-2l_a^+l_a^-}{2l_a^{+}},\\
D_{sB}&\equiv(p_B'+k)^2-m_s^2+i0=2p_B'^{-}\,(k^+ - c_B)+i0, & c_B&=\frac{2\,p'_{B,T}\!\cdot k_T+k_T^2}{2p_B'^{-}},\\
D_{b}&\equiv(l_b-k)^2-m_b^2+i0=-2l_b^{-}\,(k^+ - d_B)+i0, & d_B&=\frac{2l_b^+l_b^- -(l_{b,T}-k_T)^2-m_b^2}{2l_b^{-}}.
\end{aligned}
$$

Poles: `k^- = c_A + i0` (UHP, A spectator), `k^- = d_A − i0` (LHP, A active), `k^+ = c_B − i0` (LHP, B spectator),
`k^+ = d_B + i0` (UHP, B active). All four lie at distance `O(λ²Q)` from the origin, i.e. *in* the Glauber region;
the gluon pole `k^- = (k_T²+m_g²−i0)/(2k^+)` is at `|k^-| ~ Q` (outside it).

| X (A side) | Y (B side) | k^- (A lines) | k^+ (B lines) | consequence |
|---|---|---|---|---|
| spectator s_A | spectator s_B | UHP + LHP: **trapped** | LHP + UHP: **trapped** | **Glauber pinch** (no deformation possible) |
| spectator s_A | active b | trapped | only b (UHP): free | deform k^+ into the LHP to `|k^+|~Q` (A-collinear): b eikonalizes into a past-pointing Wilson line in f_A |
| active a | spectator s_B | only a (LHP): free | trapped | mirror: deform k^- into the UHP |
| active a | active b | only a | only b | no collinear pinch (A–A Coulomb phase belongs to the soft/hard vertex) |

This reproduces CSS review eq. (166) (verified): for a soft gluon `q` on the A jet, "the poles in the `q^-` plane due
to the jet propagators" of the spectator and active lines are "on opposite sides of the contour, both at a
distance of order `2ℓ_⊥·q_⊥/p^+` from the origin".

### 1.3 Initial- vs final-state interactions; DIS and e+e− **[P1f, P1g, P4a–e, SS5a–b]**

Rule (exact for the half-plane, from the propagators above): a line carrying `l + s k` with large plus momentum puts
its `k^-` pole in the LHP if `s=+1` and in the UHP if `s=−1`, irrespective of its mass/virtuality; similarly for
`k^+` and large minus momentum. Hence: for the lines of a collinear subgraph through which the routing of `k` runs,
**all poles lie on one side iff these lines are all initial-state or all final-state relative to the hard vertex**.
* DY: each hadron's subgraph has both (active parton = initial; spectator = final) → `k^-` trapped by A, `k^+`
  trapped by B. Only S–S has both trapped.
* DIS: the target subgraph traps `k^-`, but the only other collinear subgraph is the current jet (final state):
  `k^+` meets only final-state poles → deformable. Numerically (exact jet propagator, finite widths): pushing the
  `l^+` contour into the LHP by `λQ` reproduces the real-axis value to `2×10^{-11}` of `2π|Res|`, and on the
  deformed contour the eikonal (future-pointing) jet line is accurate to `< λ` **[P4a,b,e]**.
* e+e−: all collinear lines are final-state lines (also through internal splittings): no trapping **[P1g]**.
* DY active–spectator: the `k^+` contour (only the initial-state pole of b, UHP) deformed into the LHP reproduces
  the real-axis value (`10^{-12}`); on it the eikonal line `1/(−2l_b^-k^+ + i0)` (past-pointing Wilson line in `f_A`)
  is accurate to `≲ 2×10^{-3}` **[SS5a,b]**.

### 1.4 Eikonal lines and the Glauber term **[P3a–d]**

With the Wilson-line one-gluon terms of §0.2, past- and future-pointing lines differ by
`1/(n·k+i0) − 1/(n·k−i0) = −2πi δ(n·k)` (checked on a test function, **[P3d]**). Blueprint E7.24 (past–past
eikonal lines) verified exactly:

$$
\int_{-\infty}^{\infty}\! dk^-\;\frac{1}{(k^-+i0)\,(-k^++i0)\,(2k^+k^- - k_T^2+i0)}=
\begin{cases}0, & k^+>0,\\[2pt] -\dfrac{2\pi i}{k_T^2\,k^+}, & k^+<0,\end{cases}
$$

(both poles in the LHP for `k^+>0`; for `k^+<0` the gluon pole moves to the UHP) **[P3a–c]**.

### 1.5 The Bodwin / Collins–Soper–Sterman cancellation at one-gluon level, step by step

Model: each hadron = active parton + spectator (colour-singlet bound state); one gluon (abelian charges `e_A`, `e_B`
on the spectators, or non-abelian generators) exchanged between the A and B subgraphs.

**Step 0 (classification).** Graphs with the gluon inside one collinear subgraph belong to that PDF. Exchanges between
subgraphs: A–A, S_A–b, a–S_B, S–S (table in §1.2), each with the gluon to the left or to the right of the final-state
cut.

**Step 1 (A–A).** No collinear pinch; after deformation the soft approximation holds and the gluon couples via
past-pointing Wilson lines `W[0,−∞n_A]`, `W[0,−∞n_B]` in the soft factor. Its Glauber (Coulomb, `iπ`) part is a
phase of the soft factor. (Rothstein–Stewart 2016, Sec. 10.1, verified: for active–active interactions the Glauber
contribution equals the Glauber zero-bin of the soft graph, so the result is the same with or without an explicit
Glauber mode.)

**Step 2 (S_A–b and a–S_B).** `k^-` is trapped by A, but `k^+` meets only the initial-state pole of b:
deform `k^+` (into the LHP) out of the Glauber region to `|k^+| ~ Q`, where `k` is A-collinear. There the b propagator
eikonalizes, `1/((l_b−k)²−m_b²+i0) → 1/(−2l_b^-k^+ + i0)`, and the Ward identity (sum over all attachments to the
B side) turns the gluon into the past-pointing Wilson line `W[·,−∞n_B]` of the A-PDF **[SS5]**. For the collinear PDF
(`w = (0^+,w^-,0_T) ∥ n_B`) `W[w,−∞n_B]W[−∞n_B,0] = W[w,0]` = the same straight segment as in DIS (universality).

**Step 3 (S–S): the pinched case, done exactly.** Both contours are trapped, so one cannot deform. Do the `k^-`
integral by closing in the UHP (only the A-spectator pole; the integrand falls like `1/(k^-)²`) and the `k^+`
integral by closing in the LHP (only the B-spectator pole). Exactly (sympy) **[SS1b–e]**:

$$
\int\!\frac{dk^-}{2\pi}\,(ie_A\,2p_A'^{+})\,\frac{i}{D_{sA}}\,\frac{i}{D_a}=(ie_A)\Big[\frac{i}{D_a}\Big]_{k^-=c_A},\qquad
\int\!\frac{dk^+}{2\pi}\,(ie_B\,2p_B'^{-})\,\frac{i}{D_{sB}}\,\frac{i}{D_b}=(ie_B)\Big[\frac{i}{D_b}\Big]_{k^+=c_B},
$$

i.e. the internal spectators are put on shell, and the remaining factors are *the tree amplitude with shifted
spectator momenta*. With the Glauber gluon propagator `−i/(k²−m_g²) ≈ i/(k_T²+m_g²)`:

$$
\boxed{\;\mathcal M^{(1)}_{SS}(p_A',p_B')=\int\!\frac{d^2k_T}{(2\pi)^2}\;V(k_T)\;\mathcal M^{(0)}(p_A'-k_T,\;p_B'+k_T),\qquad
V(k_T)=\frac{-\,i\,e_Ae_B}{k_T^2+m_g^2}\;}
$$

(purely imaginary and even in `k_T`; non-abelian: `e_Ae_B → g² T_A·T_B`, a Hermitian colour matrix). The exchange
only shifts the **relative** transverse momentum `Δ = (p'_{B,T}−p'_{A,T})/2 → Δ + k_T` at fixed total
`q_T = −(p'_{A,T}+p'_{B,T})`.

**Step 4 (the two cuts cancel only after the Δ integral) [SS3e, U3a,b].** The two cut graphs (gluon left or right of
the cut) sum to

$$
\int\! d^2\Delta\;2\,\mathrm{Re}\big[\mathcal M^{(1)}\mathcal M^{(0)*}\big]
=\int\!\frac{d^2k}{(2\pi)^2}\Big[V(k)\,C(k)+V^*(k)\,C^*(k)\Big]=\int\!\frac{d^2k}{(2\pi)^2}\,V(k)\,\big[C(k)-C(-k)\big]=0,
$$

with `C(k) = ∫d²Δ M^{(0)}(Δ+k)M^{(0)*}(Δ)`, `C(−k) = C(k)^*`, `V^* = −V`, `V(−k)=V(k)`. Point by point in Δ the sum
is non-zero (numerically 30% of a single graph in the toy of **[U3a]**, 3% for the all-orders phase in **[SS3d]**).
In impact-parameter space (`M(Δ) = ∫d²b e^{−iΔ·b} M̃(b)`):

$$
\tilde{\mathcal M}^{(1)}(b)=i\chi(b)\,\tilde{\mathcal M}^{(0)}(b),\qquad \chi(b)=-\frac{e_Ae_B}{2\pi}\,K_0(m_g b)
\;\xrightarrow{m_g\to0}\;\frac{e_Ae_B}{2\pi}\Big[\ln\frac{m_g b}{2}+\gamma_E\Big]+O(m_g^2b^2)
$$

**[SS3a,b, U3c]**, and in the abelian eikonal approximation the n-fold iteration gives `(iχ)^n/n!`, i.e.
`M̃ = e^{iχ(b)} M̃^{(0)}`, so `∫d²Δ|M|² = (2π)²∫d²b|M̃|² = ∫d²Δ|M^{(0)}|²` **[SS3c]**. The IR-divergent Coulomb phase
is harmless because it is a phase. (Same structure: Aybat–Sterman eq. (14), an explicit abelian phase; Rothstein–
Stewart eqs. (11.12)–(11.13): the S–S Glauber phase "cancels as long as we carry out the phase space integral over
`Δp_⊥`"; both verified.) Since DY measures only the lepton pair, Δ is always integrated — also at fixed `q_T`, so the
S–S cancellation holds for TMD Drell–Yan as well.

**Step 5 (unitarity formulation, all placements of the cut) [U1, U1-int, U2, U2b].** In `x^+`-ordered (light-front)
perturbation theory the final-state factor is a chain of energy denominators `a_f = E − d_f`; summing over the
position `c` of the final-state cut (amplitude `1/(a+i0)`, conjugate `1/(a−i0)`, cut `2πδ(a)`) one has the exact
finite-ε telescoping identity (derived here; `2πδ(a) → 2ε/(a²+ε²) = i[(a+iε)^{-1}−(a−iε)^{-1}]`):

$$
\sum_{c=1}^{N}\Big[\prod_{f>c}\frac{1}{a_f-i\varepsilon}\Big]\frac{2\varepsilon}{a_c^2+\varepsilon^2}\Big[\prod_{f<c}\frac{1}{a_f+i\varepsilon}\Big]
= i\prod_{f=1}^{N}\frac{1}{a_f+i\varepsilon}-i\prod_{f=1}^{N}\frac{1}{a_f-i\varepsilon},
$$

and after `∫dE/(2π)` the right-hand side gives `1` for `N=1` and `0` for `N≥2`: final-state interactions cancel
(checked symbolically for N ≤ 3, exactly on rationals for N ≤ 7, and numerically after the E integral; the opposite
overall sign fails). The analogous combinatorial statements for gluons attached to an incoming Wilson line are
Aybat–Sterman's eikonal identity `Σ_{j=0}^n E_{nj}(q_1^-,…,q_n^-) = 0` (their eqs. (3)–(4)) and their "causal identity"
eq. (10) `Σ_{a=0}^n Π_{k≤a}[−(q_1^++…+q_k^+)]^{-1} Π_{l>a}[q_l^++…+q_n^+]^{-1} = 0` — both verified exactly here.

**Step 6 (conclusion of the one-gluon argument).** After Step 4/5 the S–S final-state interactions are gone; the
remaining poles in each variable come from initial-state lines only, the contours can be deformed out of the Glauber
region (Collins–Soper–Sterman review §9.3; Aybat–Sterman: "the Glauber 'pinch' of covariant perturbation theory is
then replaced in the hybrid form by a mismatch between the directions of the deformations for initial and final
states"), the soft approximation holds, soft gluons decouple into past-pointing Wilson lines, and the soft factor is
1 for the inclusive (collinear) cross section. Collins–Qiu (Sec. III B, Fig. 5(d,e), verified) state the same at one
gluon for DY: the two spectator–spectator graphs "are equal, but exactly opposite in sign. The cancellation is
exactly one of those needed to prove factorization, and involves a sum over all allowed cuts of a particular graph."

### 1.6 What changes at two gluons (non-abelian)

1. **Colour of ladder vs crossed ladder.** For two exchanged gluons between lines in representations `R_1, R_2`
   with `c ≡ T_1·T_2`: ladder `L = c²`, crossed ladder `X = c² + (C_A/2) c` (any pair of representations; checked for
   F×F, F×F̄, F×A, A×A in SU(2,3,4)) **[U5a]**. In the abelian theory box + crossed box combine at the integrand level
   (`1/(−k+i0)+1/(k+i0) = −2πiδ(k)` **[U5b]**) into `δ(k^+)δ(k^-)` and the iteration gives the eikonal phase; in QCD
   "the box and crossbox have different color factors, so this type of manipulation does not suffice"
   (Rothstein–Stewart Sec. 5.2.1, verified). With their rapidity regulator every crossed Glauber diagram vanishes,
   the ladders exponentiate to `exp(iφ(b))` with
   `φ(b) = −T_1^A⊗T_2^A g² ∫đ^{d−2}q_⊥ e^{iq_⊥·b_⊥}/q_⊥²` a **Hermitian colour matrix** (RS eqs. (9.1), (9.18), (9.19)),
   and the non-abelian part of the crossed-box topology is carried by the soft region (two soft gluons). (With a
   gluon mass, `φ(b) = −g² T_1·T_2 K_0(m_g b)/(2π)`, the same form as `χ(b)` above.)
2. **Unitarity still gives the inclusive cancellation.** `U(b) = e^{iχ(b)T_A·T_B}` is unitary, so the colour-traced,
   Δ-integrated probability is unchanged, `Tr[UρU^†] = Tr ρ` **[SS4a,b, U4a,b]**; at `O(χ²)` the cut identity
   `|ic|² + 2Re(−c²/2) = 0` holds for any Hermitian colour matrix **[SS4d]**.
3. **But the Glauber phase no longer commutes with the other soft colour exchanges.**
   `[T_A·T_B, T_A·T_j] ≠ 0` for a third coloured line j (norm 1.73 in SU(3)) **[SS4c]**. The abelian argument —
   factor the c-number phase off and cancel it — therefore fails at the amplitude level as soon as a Glauber
   exchange and a soft (eikonal) exchange to an active or outgoing coloured parton occur together. This
   non-commutation is the engine of the non-inclusive breakdowns (Forshaw–Seymour–Siódmok: factorization breaking is
   "driven by the non-commutation of Coulomb/Glauber gluon exchanges with other soft exchanges"; Schwartz–Yan–Zhu 2018
   abstract: for pure Glauber ladders all amplitude-level violations cancel for any single-scale observable, "the
   leading factorization violating effects therefore come from graphs with at least one soft gluon, involving the
   Lipatov vertex off of the Glauber ladders"). Gaunt 2014 argued that for hadronic transverse energy the CSS
   cancellation breaks down "at the level of two Glauber gluons exchanged between the spectators"; Schwartz–Yan–Zhu
   later state that their result "disproves previous claims that these pure Glauber graphs are factorization
   violating". The literature on *which* graphs first violate factorization for MPI-sensitive observables is thus not
   settled; that such observables (E_T, beam thrust with vetoes, transverse thrust) are not described by standard
   factorization is supported by Gaunt 2014 and by Zeng 2015's explicit counterexample (leading-power longitudinal
   spin asymmetry of beam thrust from spectator Glauber exchange in QCD with scalar quarks).
4. **Why inclusive DY survives in the non-abelian theory.** CSS review §9.3 (verified, qualitative): the softest
   colour field "cannot resolve the hadron jet into individual partons. Thus the jet appears as a color singlet until
   the time of the hard interaction ... the only interactions ... occur long after the hard scattering event, and such
   interactions cancel because of unitarity"; for harder components "we could as well replace all of the spectator
   partons with an equivalent color charge located at x_⊥ = 0, right on top of the active quark". Aybat–Sterman
   (verified) make this into an outline: Glauber exchanges "act to dress light-cone wave functions with nonabelian
   phases", the subtracted eikonal form factor of each colour representation "is a pure phase", and "these phases then
   cancel, because ... the color representation ... is the same in the amplitude and the complex conjugate after the
   cancellation of final state interactions" — which requires an inclusive sum over final states at every scale.
5. **Explicit higher-order checks (abstracts verified).** BBL 1981 claimed initial-state interactions "violate the
   usual QCD factorization predictions ... in leading twist"; CSS 1983 (all one-loop corrections incl. spectator
   exchanges: "weak factorization at measured dimuon Q_T"); Lindsay–Ross–Sachrajda 1982/1983 (all two-loop graphs with
   virtual gluons on the spectator: "the sum of all these non-factorising terms is zero"); Brandt–Frenkel–Taylor 1989
   (two-loop cancellation of soft spectator interactions in an eikonal-meson model). Doria–Frenkel–Taylor 1980
   (massive coloured initial partons, two soft gluons: non-leading IR divergences do not cancel) — power suppressed at
   high energy (Frenkel–Gatheral–Taylor 1984; CSS review: cancellation "at leading power (although not at higher
   twist)").
6. **Colour projections are not protected.** Unitarity protects only traces: a projector on a colour configuration
   that does not commute with `T_A·T_B` (e.g. "A remnant + another parton in a singlet", the kind of condition a
   rapidity gap imposes) is changed by the Glauber phase (`0.132 → 0.094` in **[SS4e]**; `0.086 → 0.130` in
   **[U4e]**) — the bridge to §3.

### 1.7 Status of the Glauber step for DY

[A]: CSS 1985 ("factorization holds at leading twist in the Drell-Yan cross section dσ/dQ²dy and related inclusive
hadron-hadron cross sections"), CSS 1988 ("mechanisms by which they [soft gluons] decouple from the incoming hadrons
and cancel"), Bodwin 1985 (one- and two-loop examples, all-order implementation; IR finiteness "if one integrates
over the transverse momentum of the lepton pair") — abstracts verified; detailed texts not read here. The CSS review
itself (verified) says "there is plenty of room for improvement in our understanding". Rothstein–Stewart: the S–S
cancellation in their EFT, "taken alone ... is far from a proof of factorization, even in the abelian case".
Independent all-order Glauber-cancellation proof for double DY: Diehl–Gaunt–Ostermeier–Plößl–Schäfer 2016 (abstract
verified; also "revisit and clarify some issues regarding the Glauber cancellation argument ... for the single
Drell-Yan process").

---------------------------------------------------------------------------------------------------------

## 2. Collins–Qiu / Rogers–Mulders: TMD factorization breaking in h1 + h2 → H1 + H2 + X

Process: two hadrons collide and two hadrons (or jets) H3, H4 are produced nearly back to back at large `P_T`;
the transverse-momentum imbalance `q_T` (partonically `k_{3T}+k_{4T}`) is measured with `q_T ≪ P_T`, so TMD
("k_T") factorization would be the appropriate form.

### 2.1 Definitions: standard vs generalized TMD factorization

* **Standard TMD factorization** (RM eq. (2), verified):
  `dσ = H ⊗ Φ_{H1} ⊗ Φ_{H2} ⊗ Δ_{H3} ⊗ Δ_{H4} + p.s.c.` (plus a soft factor), with **process-independent** TMD
  correlators — the same objects as in SIDIS, DY, e+e− → h1h2X (T-odd functions allowed to flip sign by the known
  Wilson-line T-reversal rule). Collins 2007 (verified) defines "standard factorization" as: the non-perturbative
  functions "either are those extracted from e+e− annihilation and from reactions in deep-inelastic scattering (DIS),
  or are related to them by purely perturbatively-based calculations".
* **Generalized TMD factorization** (RM eq. (3), verified; introduced by Bacchetta–Bomhof–Mulders–Pijlman 2005 and
  Bomhof–Mulders–Pijlman 2004/2006):

$$
d\sigma=\sum_{j,c} H_{j,c}\otimes\Phi^{[\mathrm{WL}_{c,j1}]}_{H_1,j}\otimes\Phi^{[\mathrm{WL}_{c,j2}]}_{H_2,j}\otimes
\Delta^{[\mathrm{WL}_{c,j3}]}_{H_3,j}\otimes\Delta^{[\mathrm{WL}_{c,j4}]}_{H_4,j}+\text{p.s.c.}
$$

  "`H_{c,j}` is the hard part for subprocess j and color routing c"; each correlator is a single-hadron matrix
  element of two parton fields joined by a (possibly complicated, process- and routing-dependent) gauge-invariant
  Wilson-line structure, e.g. `⟨H_1| ψ̄(ξ) U^{[WL]}(ξ,0) ψ(0) |H_1⟩`; and, crucially, "Eq. (3) contains **no matrix
  element of the form ⟨H1 H2|···|H1 H2⟩**". Example of such a structure (BBMP eq. (A11a), verified):

$$
U^{[tt^*]}_{qq}=\frac{1}{N^2-1}\Big[(N^2+1)\,\frac{\mathrm{Tr}\,U^{[\square]}}{N}\,U^{[+]}-2\,U^{[\square]}U^{[+]}\Big],
\qquad U^{[\square]}=U^{[+]}U^{[-]\dagger}.
$$

* **What fails** (precise): (i) standard TMD factorization fails for TMD-sensitive observables of this process
  (Collins–Qiu: SSA, abelian model, one extra gluon; Collins 2007: unpolarized cross section, abelian model, two extra
  gluons); (ii) generalized TMD factorization fails in a non-abelian gauge theory (Rogers–Mulders: double transverse
  spin asymmetry, SU(N_c) spectator model, two extra gluons, one from each hadron). "A single counter-example suffices
  to show that a general proof does not exist" (RM abstract).

### 2.2 One extra gluon, abelian model (Collins–Qiu) **[A1, A1b]**

CQ model (verified): abelian massive gluon; neutral Dirac "hadrons" `H_i` coupled to a Dirac spectator `ψ_i`
(charge `g_i`) and a scalar active parton `φ_i` (opposite charge); H1, H2 of different flavours; H3, H4 = the two
scalar flavours. An extra gluon from the spectator of the polarized H1 can attach to the outgoing active line k3 (own
flavour), to the outgoing line k4 (flavour 2) or to the incoming line k2 (flavour 2). The eikonal replacements
(CQ eqs. (4.1)–(4.3)) all give `i g π δ^μ_− δ(l^+)`, "for a total of `iπ(g1 + 2g2)δ(l^+)`"; equivalently (Collins 2007
eq. (2)):

$$
E(l)=\frac{g_2}{l^++i0}+\frac{g_2}{-l^++i0}+\frac{g_1}{-l^++i0}
=-2\pi i\,g_2\,\delta(l^+)+\frac{g_1}{-l^++i0}
=-\pi i\,(2g_2+g_1)\,\delta(l^+)-g_1\,\mathrm{PV}\frac{1}{l^+}.
$$

The principal values of the k2 (initial-state) and k4 (final-state) attachments cancel; the T-even part is the
future-pointing Wilson line of charge `g1` (standard). The T-odd (Sivers) part has coefficient `g1+2g2`: "it is
impossible for the contribution proportional to `g2` to be represented in terms of a Wilson line connecting the two
parton fields for the distribution of partons of type `φ1` in the hadron H1. This is simply because the coupling for
any such Wilson line has to correspond to the color charge of the parton, i.e., `g1`, and not `g2`" (CQ, verified).

### 2.3 One extra gluon in QCD: SU(N) gluonic-pole factors **[C1, C1n, C2, C4, C5]**

**Pole rule (derived; agrees with CQ eqs. (4.1)–(4.3), RM eqs. (8), (15), (16)).** For a gluon of momentum `l` from
the polarized hadron's spectator, the pole part of an eikonal attachment has the same coefficient for a quark line
whether it is incoming or outgoing, and the opposite one for an antiquark line; principal parts differ. In
Catani–Seymour charges this means the pole parts sum to the colour operator

$$
P=\sum_{j\ \mathrm{out}}\mathbf T_j-\sum_{j\ \mathrm{in},\,j\neq a}\mathbf T_j=-\mathbf T_a-2\,\mathbf T_b
\qquad(\text{colour conservation }\textstyle\sum_{\rm all}\mathbf T=0),
$$

acting on the hard amplitude, contracted with the hadron-1 correlator through `−T_a`. Normalizing to SIDIS
(`P = T_c = −T_a`, value `C_F`):

$$
\boxed{\;C_G=\frac{\langle M|(-\mathbf T_a)\cdot P|M'\rangle}{C_F\,\langle M|M'\rangle}=1+\frac{2\,\langle\mathbf T_a\cdot\mathbf T_b\rangle}{C_F}\;}
$$

(a = polarized incoming parton, b = the other incoming parton; for an interference `⟨M|M'⟩` use the matrix element
between the two amplitudes). Checks: SIDIS (no coloured b) `C_G=+1`; DY (`T_a+T_b=0`, `⟨T_a·T_b⟩=−C_F`) `C_G=−1`
(Collins 2002 sign rule) **[C1n]**. With SU(N) projectors (`3⊗3 = S⊕A`, `T_a·T_b = (N−1)/(2N)` on S,
`−(N+1)/(2N)` on A; `3⊗3̄ = 1⊕8`, `T_a·T_b = −C_F` on 1, `1/(2N)` on 8), exactly in N **[C5, C5b]**:

| channel (BBMP / QVY diagram) | colour structure | ⟨T_a·T_b⟩ | C_G | SU(3) |
|---|---|---|---|---|
| qq′→qq′ t-channel, tt* (QVY 1) | `½[(1−1/N)P_S−(1+1/N)P_A]` | `−1/N` | `(N²−5)/(N²−1)` | 1/2 |
| uu* (QVY 2) | | `−1/N` | `(N²−5)/(N²−1)` | 1/2 |
| tu* interference (QVY 3) | | `−(N²+1)/(2N)` | `−(N²+3)/(N²−1)` | −3/2 |
| qq̄′→qq̄′ t-channel, tt* (QVY 4) | `½[(N−1/N)P_1−P_8/N]` | `−(N²−2)/(2N)` | `−(N²−3)/(N²−1)` | −3/4 |
| qq̄→q′q̄′ s-channel, ss* (QVY 5) | `½P_8` | `1/(2N)` | `(N²+1)/(N²−1)` | 5/4 |
| st* interference (QVY 6) | | `1/(2N)` | `(N²+1)/(N²−1)` | 5/4 |

These equal BBMP eqs. (B5a,b), (B6a,b) and Table I (verified), for every N = 2…6 numerically **[C1, C2]** and
symbolically **[C5]**. Large N: `C_G → +1` (tt*, uu*, ss*, st*), `−1` (tu*, qq̄ tt*) **[C5c]**. BBMP's own links reproduce
their strengths, e.g. (A11a): `C_G = [(N²+1)·1 − 2·3]/(N²−1) = (N²−5)/(N²−1)` using `C_G[U^{[+]}]=1`,
`C_G[U^{[□]}U^{[+]}]=3`, `C_G[Tr U^{[□]}U^{[+]}/N]=1` (BBMP eq. (B3), Table I) **[C4]**.

**Graph by graph (QVY Table I, verified entry by entry, all N) [C1].** For diagram (1) (t-channel qq′→qq′):
`C_u = (N²−1)/(4N²)`, initial-state interaction on the incoming parton of h2 `C_I = −1/(2N²)`, final-state
interaction on the outgoing parton with momentum `P1` `C_F1 = −1/(4N²)`, on the one with momentum `P2`
`C_F2 = (N²−2)/(4N²)` (QVY eqs. (25)–(27)); `C_I+C_F1+C_F2 = (N²−5)/(4N²)` (QVY eq. (28)). Relative to the Born:
`C_I/C_u = −2/(N²−1)`, `C_{F1}/C_u = −1/(N²−1)`, `C_{F2}/C_u = (N²−2)/(N²−1)`; SU(3): `−1/4, −1/8, +7/8`, sum `1/2`.
Thus **the one-gluon exchange between the spectator of h1 and the outgoing parton that fragments into H2** (the
parton with momentum `P2` in the t-channel diagram) carries `(N²−2)/(N²−1) = 7/8`, the mirror attachment to the
other outgoing parton `−1/(N²−1) = −1/8`, and the initial-state attachment `−2/(N²−1) = −1/4`. (The mirror graphs
with the gluon from the spectator of h2 give the analogous factors for h2's Sivers function, with a ↔ b.)

**Why this is "entangled".** `C_G − 1 = 2⟨T_a·T_b⟩/C_F` is a colour correlation between the parton from hadron 1 and
the parton from hadron 2. A process-independent Wilson line attached to hadron 1's correlator can only produce
`C_G = ±1`; the actual factors depend on the channel and on N. At this order one can still absorb `C_G` into a
channel-dependent hard part ("gluonic-pole cross sections", BBMP; "modified hard parts", QVY) — this is *already* a
departure from standard factorization, and Collins 2007 shows it does not survive the next order (§2.4).

### 2.4 Two extra gluons, abelian model, unpolarized (Collins 2007) **[A2, A3, A4]**

Gluons on opposite sides of the cut (C07 eq. (3)):

$$
E(l_1)E(l_2)^*=g_1^2\,\mathrm{PV}\tfrac1{l_1^+}\mathrm{PV}\tfrac1{l_2^+}
+i\pi g_1(2g_2+g_1)\Big[\delta(l_1^+)\mathrm{PV}\tfrac1{l_2^+}-\mathrm{PV}\tfrac1{l_1^+}\delta(l_2^+)\Big]
+\pi^2(2g_2+g_1)^2\,\delta(l_1^+)\delta(l_2^+),
$$

so the T-even part exceeds the standard (charge `g1`) Wilson-line value by the **anomaly** (C07 eq. (4))

$$
\boxed{\;E(l_1)E(l_2)^*\big|_{\rm anom}=4\pi^2\,g_2(g_2+g_1)\,\delta(l_1^+)\,\delta(l_2^+)\;}
$$

(vanishes iff `g2 = 0` or `g2 = −g1`) **[A3a–c]**. Same side of the cut: the `g2²` terms give `−(2π)² g2² δδ`
(C07 eq. (7)) and the `g1g2` terms give `−(2π)²g1g2δδ + 2πi g1g2[δ(l_1^+)PV(1/l_2^+)+δ(l_2^+)PV(1/l_1^+)]` (C07 eq. (8)),
i.e. exactly the product `E(l1)E(l2)`: "exponentiation in a Wilson-line operator, with the nonstandard one-gluon term
E(l). Thus we have verified factorization in the generalized sense" (C07) **[A2c, A3d]**; the same-side anomaly is
minus the opposite-side one. In the scalar model (all fields scalars, `m_q`, `m_g`, `M=0`) the anomalous
contributions to the TMD of H1 are (C07 eqs. (10), (11) — see the remark below; RM eqs. (27), (28) are the
massless-gluon, non-abelian analogues):

$$
I_1(k_T)=\mathcal N\,F(k_T)^2,\qquad I_2(k_T)=-\mathcal N\,\frac{G(k_T)}{k_T^2+m_q^2},\qquad
\mathcal N=\frac{\lambda^2g_1^2\,g_2(g_2+g_1)\,x(1-x)}{256\pi^7},
$$

$$
F(k)=\int\!\frac{d^2l}{(l^2+m_g^2)((k-l)^2+m_q^2)}=\frac{\pi}{\sqrt{\Lambda}}\ln\frac{s+\sqrt\Lambda}{s-\sqrt\Lambda},\quad
s=k^2+m_g^2+m_q^2,\ \Lambda=s^2-4m_g^2m_q^2,
$$

$$
G(k)=\int\!\frac{d^2l_1\,d^2l_2}{(l_1^2+m_g^2)(l_2^2+m_g^2)((k-l_1-l_2)^2+m_q^2)}
=\pi^2\!\int_0^1\!\!dx\!\int_0^1\!\!dy\;\frac{1}{x(1-x)\,[y(1-y)k^2+(1-y)m_g^2]+y\,[x m_q^2+(1-x)m_g^2]}
$$

(closed form of F and the representation of G derived here; checked against Feynman-parameter and Hankel/`K_0`
forms to `10^{-11}` **[A4a, A4a2]**). In b space `F̃ = (2π)²K_0(m_gb)K_0(m_qb)`, `G̃ = (2π)³K_0(m_gb)²K_0(m_qb)`, and by
Parseval

$$
\int\! d^2k_T\,I_1=\mathcal N(2\pi)^3\!\int_0^\infty\! db\,b\,K_0(m_gb)^2K_0(m_qb)^2=-\int\! d^2k_T\,I_2
\quad\Longrightarrow\quad\int\! d^2k_T\,(I_1+I_2)=0
$$

(k-space integrals agree with the b-space value to `10^{-10}`) **[A4d]**: collinear factorization survives at this
order, as C07 states. Point by point `I_1+I_2 ≠ 0` and changes sign (e.g. `(m_g,m_q)=(0.5,1)`:
`(I_1+I_2)/𝒩 = −21.0, −17.7, −7.19, −0.70, +0.38, +0.089` at `k_T = 0, 0.3, 0.8, 1.5, 3, 6`) **[A4e]**.
C07 says "with a certain amount of effort, it can be proved analytically that `I_1(0)+I_2(0)<0`" without the proof;
**proof (ours)**: with the positive measure `dμ(b) = d²b/(2π)²·2πK_0(m_qb)`, `∫dμ = 1/m_q²`,
`F(0) = ∫dμ 2πK_0(m_gb)`, `G(0) = ∫dμ [2πK_0(m_gb)]²`; by Cauchy–Schwarz `F(0)² ≤ G(0)∫dμ = G(0)/m_q²`, strictly
because `K_0(m_gb)` is not constant, hence `I_1(0)+I_2(0) = 𝒩[F(0)² − G(0)/m_q²]` has the sign of `−𝒩` (`<0` in
units of 𝒩) **[A4b, A4c]**.
*Remark (typo in the source):* as printed in arXiv:0708.4410v1, eq. (10) carries an extra factor
`Π_j (k_T²+m_q²)` in the numerator; this contradicts the first line of the same equation, eq. (11) (mass dimension
`M^0` vs `M^{-4}`) and the stated cancellation; the form above is the consistent one **[A4f]**.

### 2.5 Non-abelian: Rogers–Mulders — no generalized TMD factorization **[C3, C6, A2d, A2e]**

RM model (verified): massless SU(N_c) gluon with equal coupling to all coloured fields; scalar "quarks" `φ_f`
(triplets), Dirac "hadrons" and spectator "diquarks"; hard part = exchange of a massive **colour-neutral** U(1) boson X
("only one subprocess and one color flow", so the generalized formula can contain only one term). Colour factors:
* Fig. 3 (gluon from spectator 1 to the outgoing quark of hadron 1, k3 — the standard future-pointing link):
  `T_F(N_c²−1)` (RM eq. (14)) per colour loop, i.e. `C_F` relative to the tree loop (`−C_F` with an explicit
  antitriplet spectator generator `−t^T`; RM write `t^a` at both vertices) **[C3]**;
* Fig. 4 (gluon from spectator 1 to k4 or to the incoming k2 — the CQ graphs): `Tr_C[t^a] = 0` (RM eqs. (15)–(18)) —
  the CQ anomaly vanishes "only due to the highly simple color structure" **[C3]**;
* Fig. 7 (two gluons from spectator 1 to the k2/k4 lines): `Tr_C[t^at^b]Tr_C[t^bt^a] = T_F²(N_c²−1)` (RM eqs. (25)–(28);
  eq. (25) `= +4π²g² n_1^μn_1^ν Tr[t^at^b]δ(l_1^+)δ(l_2^+)` opposite sides, eq. (26) `−4π²…` same side) **[A2d,e, C3]**.
  These fix the generalized Wilson-line structure of hadron 1 to contain a colour-traced loop
  `U^{n_1}_{(□)} = Tr_C[V_0 I V_w^† V_w I^† V_0^†]` (RM eq. (30)), whose one-gluon term vanishes:
  `U^{n_1}_{(□)}|_{O(g)} = U^{n_2}_{(□)}|_{O(g)} = 0` (RM eq. (33)).
* Fig. 8 (one gluon from spectator 1 to k4/k2 **and** one from spectator 2 to k3/k1; 16 graphs): colour factor
  `Tr_C[t^at^b]Tr_C[t^bt^a] = T_F²(N_c²−1) ≠ 0` (RM eq. (34)); eikonal sums `−4π²δ(l_1^+)δ(l_2^-)` (same side, eq. (35))
  and `+4π²δδ` (opposite sides, eq. (36)); with the spectator factors `i²` resp. `i(−i)` both give
  `+4π²δ(l_1^+)δ(l_2^-)`, and the remaining integral (RM eq. (38)) "is not generally zero".
* In the generalized formula (RM eq. (32)) this class would be the product of the **one-gluon** terms of the two
  separate Wilson-line structures, which vanish by eq. (33): prediction **0**. Contradiction ⇒ "a TMD-factorization
  formula cannot be recovered by simply modifying the Wilson lines in each TMD PDF separately."

**Entanglement test (ours) [C6, C6b].** Attach the gluon from spectator 1 to line X ∈ {3 (own loop), 4, 2} and the gluon
from spectator 2 to Y ∈ {4 (own loop), 3, 1}; all pole coefficients are equal (quark lines, in or out), so the
double-pole (double-Sivers) coefficient is proportional to `Σ_{X,Y} C(X,Y)` in the full theory, but to
`(Σ_X C_1(X))(Σ_Y C_2(Y))` in any formula with separate Wilson-line structures per hadron. With explicit colour-singlet
hadrons (quark ⊗ antitriplet spectator), relative to the tree, for SU(N):

$$
C_1(3)=C_2(4)=-C_F,\quad C_1(4)=C_1(2)=C_2(3)=C_2(1)=0,\quad C(3,4)=C_F^2,\quad
C(X,Y)=\frac{T_F^2(N^2-1)}{N^2}\ \ (X\in\{4,2\},Y\in\{3,1\}),\quad\text{mixed}=0,
$$

$$
\sum_{X,Y}C(X,Y)=C_F^2+\frac{4T_F^2(N^2-1)}{N^2}\;\neq\;\Big(\sum_XC_1(X)\Big)\Big(\sum_YC_2(Y)\Big)=C_F^2
$$

(same for gluons on opposite sides of the cut). SU(3): `24/9` vs `16/9`; the entangled class has colour weight
`4/(N²−1)` relative to the factorized one (`1/2` for SU(3); suppressed at large N). For U(1) charges every two-gluon
weight is the product of single-exchange charges, so "actual = product" identically: no contradiction with
generalized factorization at this order (consistent with C07 eq. (8) and Vogelsang–Yuan 2007, whose abelian two-gluon
results "are consistent with the expected gauge-link structure"). RM: "the breakdown of generalized TMD-factorization
that we have found is a specific consequence of the non-Abelian nature of QCD."

### 2.6 What fails, what survives, status

* **[V]** Standard TMD factorization for back-to-back hadron/jet production in hadron–hadron collisions (CQ 2007,
  C07, RM 2010; model counterexamples to the *method of proof*, which is general: "if methods fail in the model, they
  will also fail in QCD", C07).
* **[V]** Generalized TMD factorization (RM eq. (3)) in a non-abelian theory (RM 2010; the explicit counterexample is
  a double transverse-spin asymmetry; for the unpolarized cross section RM indicate that at least one more gluon is
  needed, their Fig. 11, not computed). Rogers 2013 (abstract): TMD-factorization breaking can even generate
  leading-power spin asymmetries that a generalized-factorization framework would classify as subleading, already
  at one extra gluon when a gluon TMD is involved.
* **Survives** at the orders examined: collinear factorization for `k_T`-integrated observables
  (`∫d²k_T(I_1+I_2) = 0`, C07). CQ: "a proof of factorization can only succeed in a situation where conventional
  collinear factorization is appropriate", citing Nayak–Qiu–Sterman for such arguments. In partonic language the
  mechanism could first give uncancelled divergences in unpolarized partonic cross sections at N³LO (CQ, Fig. 9);
  CdFR independently predict "entangled logarithms" in small-`Q_T` dihadron/dijet production from N³LO (§4).
* The CQ/RM mechanism does not arise in SIDIS, DY and e+e− → h1h2X: there, all interactions between a hadron's
  spectators and the other coloured partons are either all final-state (SIDIS: future-pointing staple; e+e−) or all
  initial-state with a colour-singlet final state (DY: past-pointing staple, S–S exchanges cancel at fixed `q_T`,
  §1.5 Step 4); TMD factorization for these processes keeps its [A] status (Ch. 11).

---------------------------------------------------------------------------------------------------------

## 3. Diffraction: why Collins' 1998 proof works for diffractive DIS and fails for hadron–hadron diffraction

### 3.1 The theorem (Collins, PRD 57 (1998) 3051 [Erratum PRD 61 (2000) 019902], hep-ph/9709499v2; verified)

$$
F_2^{(D)}(x_{bj},Q,x_{\mathbb P},t)=\sum_i C_{2i}\otimes f_i^{D}+\text{non-leading power of }Q,\qquad
x_{\mathbb P}=1-\frac{q\cdot p'}{q\cdot p},\quad t=(p-p')^2,
$$

for `Q → ∞` at fixed `x_bj, x_P, t` (Collins eq. (1)), with: `C_{2i}` **the inclusive-DIS coefficients**; `f_i^D` the
diffractive parton densities of Berera–Soper (PRD 53 (1996) 6162, "operator definition"), i.e. "suitable 'cut matrix
elements' of the same operators that define ordinary parton densities", with the final state restricted to contain
the detected `p'`; hence **ordinary DGLAP evolution** for `f^D`. Generalizations covered by the same proof: any
requirement in the target fragmentation region "fixed relative to the initial hadron" (all `x_P`, not only small;
`p'` may be a neutron or a two-pion state, etc.; fracture functions of Trentadue–Veneziano without the integral over
`p'_T`), and any lepton-induced hard process (`F_L^D`, jets in the current region; direct photoproduction).
**Not** covered: resolved photoproduction and all hadron–hadron processes. (`F_2^D` here includes everything with a
detected `p'`; the "truly diffractive" small-`x_P` part follows.)

### 3.2 The decisive step of the proof (Collins 1998, Sec. III) **[D1a–c, P1f]**

Leading regions (Collins Fig. 1): target subgraph A (lines collinear to p **and** p′), hard H, current jets `J_i`,
soft S. The only new element relative to inclusive DIS is the soft-gluon cancellation (Berera–Soper):
1. *Soft gluon on a final-state jet J* (Collins eq. (4)): `J^μ(l,k) = k^+ J^-(l,(k^+,0,0_T)) n_J^μ/k^+ +` power
   corrections; this fails in the region `|k^+k^-| ≪ k_T²` ("this region was called the Coulomb region"), but there
   "the only nearby pole in `k^+` is the explicit pole" of the jet line, so the `k^+` contour is deformed away;
   `n_J^μ/k^+ → n_J^μ/(k^+ − iε)`. All jet interactions are final-state, the deformation direction is common, the Ward
   identities apply: eikonal lines `1/(k^+ − iε)`.
2. *Soft gluon on A* (Collins eq. (5)): `A^μ(r,p,…) = r^- A^+((0,r^-,0_T),p,…) n_A^μ/r^- +` power corrections, valid
   only if `r^-` is not too small. "Precisely because A contains both initial- and final-state interactions, there
   are nearby poles in both the upper and lower half-planes, and we cannot deform the `r^-` contour" **[D1a]**. Note
   that one may **not** sum over the cuts of A (as in inclusive DIS), because `p'` is measured.
3. *The escape* — deform the **other** component `r^+`: near the soft region the only `r^+` poles are those of the
   final-state jets (one side) **[D1c]**; A-collinear lines put their `r^+` poles at `|r^+| ~ Q` **[D1b]**, and the
   soft gluon's own pole is at `r^+ = r_T²/(2r^-)`. "In either case the contour is deformed to a region where
   `|r^+| ≫ |r^-|`, which is not part of the soft region. This is sufficient to show that there is no pinch in the soft
   region at small `r^-`. Hence we can use the soft approximation at both the A and J ends of the soft gluon."
   For general soft subgraphs a possible pinch of `r^+` by other soft lines is avoided by rerouting `r` "back against
   the flow of − momentum" until it reaches an incoming line (proton or **virtual photon**) and then through A lines,
   which "by definition ... have large + momenta" and cannot pinch `r^+`.
4. Ward identities then factor the soft gluons; the soft factor cancels by the real/virtual sum, and "the
   cancellation only concerns a kinematic region unaffected by the diffractive requirement on the final state".
   Non-perturbative final-state interactions do not spoil the argument: deforming `s^+` to `O(Λ)` puts the jet lines
   off shell by `O(ΛQ)`.

**Where the lepton enters.** Step 3 uses that the second incoming particle (the virtual photon) has no soft
interactions and no spectators: no line other than final-state jets can trap `r^+` near the soft region. Collins:
"It is only when one of the initiating particles is a lepton that the proof of factorization is valid."

### 3.3 Why it fails for hadron–hadron diffraction (precise argument) **[D1d,e, SS4e, U4e, D2]**

Consider `A + B → p' + X` with a hard subprocess and a detected leading `p'` (or an imposed rapidity gap) on the A side.
1. A soft/Glauber gluon `r` between the A system and the **spectators of B** has `r^-` trapped by A exactly as in DDIS
   (A has initial and final-state lines; its final state is constrained) **[D1a]**, and now also `r^+` trapped by B:
   the active parton of B (initial state, `r^+` pole UHP) and the B remnant (final state, LHP) both put poles at
   `|r^+| ~ λ²Q` **[D1d]**. Pinch in **both** light-cone components — the spectator–spectator Glauber pinch of §1.2
   — so neither the DDIS escape (deform `r^+`) nor any other deformation exists **[D1e]**.
2. In inclusive DY the same pinch is harmless because the S–S exchange is a pure Δ-redistribution (phase) that cancels
   after the sum over all final-state cuts of the spectator systems (§1.5, Steps 3–5). This requires the cross section
   to be **inclusive in the remnants' final states**. The diffractive condition — intact `p'` with fixed `(x_P, t)`, or no
   particles in a rapidity interval — is precisely a restriction on those final states. Glauber exchanges that break up
   `p'` or exchange colour across the gap move the event out of the diffractive sample; by unitarity these events are
   not lost but reappear as non-diffractive ones, so the inclusive sum is unchanged while the **diffractive fraction is
   reduced**: `⟨i|U^†PU|i⟩ < ⟨i|P|i⟩` for a projector `P` that does not commute with the Glauber operator `U`
   (`0.132→0.094` **[SS4e]**; `0.086→0.130`, i.e. it can also change upward for a generic state, **[U4e]**). For an
   initially diffractive (singlet / intact) configuration the change is a loss: "gap survival" `< 1` **[D2]**.
3. Independently, a leading-power **coherent pomeron** contribution, in which "the whole Pomeron can initiate the hard
   scattering", breaks the diffractive-PDF form in hadron–hadron collisions and is not expected to dominate in DDIS
   (Collins–Frankfurt–Strikman 1993, verified; Collins 1998 conclusions: "Furthermore, the 'coherent pomeron mechanism'
   ... may exist").
4. History (Collins 1998 footnote 1, verified): in pre-QCD parton models there are factorization-breaking terms in both
   the diffractive and non-diffractive parts of DY (Landshoff–Polkinghorne 1971; Henyey–Savit 1974) which cancel in the
   inclusive sum (Cardy–Winbow 1974; DeTar–Ellis–Landshoff 1975); "this result forms part of the proof of factorization
   for inclusive hard processes in QCD". Collins 1998 footnote 2: the fracture-function formalism therefore also fails in
   hadron–hadron scattering.
5. Related: Forshaw–Seymour–Siódmok (verified) remark that the Coulomb-gluon factorization breaking of §4 "can be thought
   of as the perturbative tail of the gap survival effect"; Bjorken 1993 (abstract verified) introduced the "survival
   probability of the rapidity gap" ("most of the time the gap is filled by soft interactions of spectator degrees of
   freedom"; his estimate ~5% within a factor 3 refers to colour-singlet electroweak-boson fusion at multi-TeV energies).

### 3.4 Toy model: unitarity vs gap selection (ours, illustration only) **[D2a–f]**

Diffracted hadron = colour-singlet two-constituent dipole of transverse size `r` at impact parameter `b` from a B
spectator; Glauber phase `χ(b) = −e_Ae_B K_0(m_gb)/(2π)` (§1.5).
* Abelian: the internal state is multiplied by `e^{iδφ(r)}`, `δφ = χ(|b+r/2|) − χ(|b−r/2|)`. Survival
  `S = |∫d²r |ψ(r)|² e^{iδφ}|² < 1`, `S → 1` as the dipole size → 0 (`S = 0.99998, 0.99912, 0.98974` for Gaussian sizes
  `R = 0.05, 0.3, 1`); survival + break-up summed over a complete set of internal states `→ 1` (partial sums
  `0.9999866, 0.9999938, 0.9999966` with `20², 40², 70²` states; the deficit is basis truncation) **[D2a,b]**.
* SU(3): `U = exp(iχ_1 T_q·T_B + iχ_2 T_q̄·T_B)`. Colour-summed probability `= 1` always **[D2c]**; the singlet-survival
  probability is exactly 1 when `χ_1 = χ_2` (zero size: `(T_q+T_q̄)|1⟩ = 0`, colour transparency) and `< 1` otherwise
  (`0.99782, 0.96492, 0.34558`) **[D2d]**; the singlet→octet leakage is quadratic in the phase difference (two-gluon,
  cut level) with coefficient `C_F/(2N) = 2/9` for `U = e^{i d T_q·T_B}`, B in the fundamental **[D2e,f]**.

### 3.5 Experimental evidence (texts/abstracts verified)

* CDF Run I diffractive dijets with a leading antiproton (PRL 84 (2000) 5043): summarized by CDF (PRD 86 (2012) 032009)
  as "a breakdown of QCD factorization, expressed as a suppression by a factor of O(10) of the diffractive structure
  function measured in dijet production relative to that derived from fits to parton densities measured in diffractive
  deep inelastic scattering ... at HERA".
* Alvero–Collins–Terron–Whitmore 1999: DPDFs fitted to DDIS and diffractive photoproduction predict Tevatron diffractive
  jet and W/Z cross sections "substantially higher than data; this signals a breakdown of hard-scattering factorization
  in diffractive hadron-hadron collisions". CDF 1997: diffractive W, `R_W = (1.15 ± 0.55)%`.
* HERA: diffractive DIS dijets "are well described, supporting the validity of QCD factorisation"; in photoproduction the
  NLO prediction "has to be multiplied by a factor of approximately 0.5 for both direct and resolved photon interactions"
  (H1 2007); Klasen–Kramer 2008: global NLO suppression 0.42 (H1 cuts) and 0.71 (ZEUS cuts), or resolved-only suppression
  by about 3. The suppression of the *direct* component reported by H1 is not explained by Collins' proof (which covers
  direct photoproduction); Collins notes that the direct/resolved separation is not unambiguous. Open point.
* CMS 2013 (7 TeV): diffractive contribution to dijets observed, "the associated rapidity gap survival probability is
  estimated".

### 3.6 Status

DDIS (and any lepton-induced hard process with a condition on the target fragmentation region): **[A]** (Collins 1998,
all-order argument at the standard of the inclusive proofs). Hadron–hadron hard diffraction: **[V]** — no factorization
theorem; mechanism identified (uncancelled spectator–spectator Glauber exchanges + coherent pomeron), experimentally
violated by O(10). Diffractive photoproduction: resolved **[V]** (hadron-like), direct: covered by the proof in principle,
experimental status mixed (H1 vs ZEUS) — mark **[P]**.

---------------------------------------------------------------------------------------------------------

## 4. Space-like collinear factorization violation (Catani–de Florian–Rodrigo 2012) and super-leading logarithms

Notation of CdFR (arXiv:1112.4405v2; all momenta outgoing, colour-space vectors `|M⟩`, Catani–Seymour charges):
`p_1 ∥ p_2`, `p_i ≃ z_i P̃`, `z_1+z_2 = 1`; **time-like (TL)**: `z_1, z_2 > 0` (both collinear partons outgoing, or both
incoming); **space-like (SL)**: one of them negative (one incoming, one outgoing — initial-state collinear radiation).
Strict factorization at tree level: `|M^{(0)}(p_1,p_2,…)⟩ ≃ Sp^{(0)}(p_1,p_2;P̃)|M^{(0)}(P̃,…)⟩` with a universal `Sp^{(0)}`.

### 4.1 What fails at one loop (amplitude level) **[S1, S1b, S2, S3, S4a–c]**

General one-loop formula (CdFR eqs. (33)–(35)):

$$
|M^{(1)}(p_1,p_2,\dots)\rangle\simeq \mathrm{Sp}^{(1)}(p_1,p_2;\tilde P;p_3,\dots,p_n)\,|M^{(0)}(\tilde P,\dots)\rangle
+\mathrm{Sp}^{(0)}(p_1,p_2;\tilde P)\,|M^{(1)}(\tilde P,\dots)\rangle,\qquad
\mathrm{Sp}^{(1)}=\mathrm{Sp}^{(1)}_H+\boldsymbol I_C\,\mathrm{Sp}^{(0)},
$$

$$
\boldsymbol I_C=g_S^2c_\Gamma\Big(\frac{-s_{12}-i0}{\mu^2}\Big)^{-\epsilon}\Big\{\frac{C_{12}-C_1-C_2}{\epsilon^2}
+\frac{\gamma_{12}-\gamma_1-\gamma_2+b_0}{\epsilon}
-\frac1\epsilon\Big[(C_{12}+C_1-C_2)f(\epsilon;z_1)-2\sum_{j=3}^n\mathbf T_2\cdot\mathbf T_j\,f(\epsilon;z_2-i0\,s_{j2})\Big]\Big\}
\quad(z_1>0),
$$

`c_Γ = Γ(1+ε)Γ²(1−ε)/[(4π)^{2−ε}Γ(1−2ε)]`, `γ_q = (3/2)C_F`, `γ_g = b_0 = (11C_A−2N_f)/6`,
`f(ε;1/x) = [₂F₁(1,−ε;1−ε;1−x)−1]/ε = ln x − ε Li₂(1−x) + …` (eqs. (24), (25)), `s_{j2} = (p_j+p_2)²`. The only
difference from the TL c-number `I_C` (eq. (29)) is the replacement

$$
\delta_{\rm TL}=-\frac1\epsilon\,(C_{12}+C_2-C_1)\,f(\epsilon;z_2)\;\longrightarrow\;
\boldsymbol\delta=+\frac2\epsilon\sum_{j=3}^n\mathbf T_2\cdot\mathbf T_j\,f(\epsilon;z_2-i0\,s_{j2})
$$

(eqs. (36), (37)): a "colour–energy correlated `i0` prescription", i.e. colour correlations between collinear and
non-collinear partons.
* **TL: coherence restores strict factorization.** With `Σ_{j≥3}T_j = −(T_1+T_2)` (eq. (39)) and
  `2T_2·(T_1+T_2)Sp^{(0)} = (C_12+C_2−C_1)Sp^{(0)}` (eq. (42), from `(T_1+T_2)Sp^{(0)} = Sp^{(0)}T_P̃`, eq. (40)), eq. (43)
  reduces to eq. (44) = eq. (36) **[S1b, S2]** (checked for q→qg, g→qq̄, g→gg on several reduced processes).
* **n = 3 QCD partons** (+ colourless legs): `δ = −(1/ε)(C_12+C_2−C_1) f(ε; z_2 − i0 s_23)` (eq. (46)) — proportional to the
  unit matrix **[S4c]** but process dependent through the `i0`: for `q → q* g`, DIS `−(1/ε)C_A f(ε;z_2−i0)` vs DY
  `−(1/ε)C_A f(ε;z_2+i0)` (eqs. (51), (52)).
* **SL with only one incoming coloured parton (DIS kinematics)**: `δ = −(1/ε)(C_12+C_2−C_1) f(ε; z_2 − i0)` (eq. (65)):
  "effectively ... strictly-factorized" — all interactions are final-state and act coherently.
* **SL in hadron–hadron collisions** (incoming non-collinear parton 3: `s_23 < 0 < s_{j2}`, j ≥ 4): using
  `−T_2·Σ_j T_j sign(s_{j2}) = ½(C_12+C_2−C_1) + 2T_2·T_3` (eq. (68)) **[S3]**,

$$
\boldsymbol\delta=-\frac1\epsilon(C_{12}+C_2-C_1)\,f(\epsilon;z_2-i0)+\frac{i}{\epsilon}\,4\,\mathbf T_2\cdot\mathbf T_3\,f_I(\epsilon;z_2),
\qquad f_I(\epsilon;x)=-\Theta(-x)\,\pi\Big(\frac{-x}{1-x}\Big)^{-\epsilon}
$$

  (eqs. (62), (66), (67)). For n ≥ 4 QCD partons `T_2·T_3` is not proportional to 1 on the reduced colour space: e.g. for
  `q → qg` off `qq̄ → q′q̄′` its matrix in the basis `{δ_12δ_34, δ_14δ_32}` is `[[−3/2, −9/16],[0, 3/16]]` **[S4a]**, and it
  depends on which non-collinear parton is incoming **[S4b]**. **Strict collinear factorization of amplitudes fails at one
  loop in SL limits with two incoming coloured partons [V].** FSS's reading (verified): the violating term is "the
  Coulomb interaction between the two incoming partons long before the hard interaction or between two outgoing partons
  much later".

### 4.2 Squared amplitudes **[S5a–g, S6, S7]**

`|M|² ≃ ⟨M|P|M⟩`, `P = Sp^†Sp = P^{(0,R)}+P^{(1,R)}+P^{(2,R)}+…` (CdFR eqs. (166)–(171)).
* **One loop:** `P^{(1,R)} = Ĩ_P^{(1)}P^{(0,R)} + (Sp^{(0,R)†}Sp_H^{(1,R)}+h.c.)` with the c-number `Ĩ_P^{(1)} = Ĩ_C^{(1)}+h.c.`
  (eqs. (178)–(180)): the breaking terms are anti-Hermitian and cancel — "`P^{(1,R)}` is strictly factorized" (recipe:
  use the real part `f_R` in the TL formula) **[S7]**.
* **Two loops:** `P^{(2,R)}` contains the Hermitian, non-abelian operator `Δ̃_P^{(2)} = Δ̃_C^{(2)}+h.c.` (eqs. (181), (183)),

$$
\tilde{\boldsymbol\Delta}^{(2)}_P\propto\Big(\frac{\alpha_S}{2\pi}\Big)^2 f_{abc}\sum_{i=1,2}\;\sum_{\substack{j,k=3\\ j\neq k}}^{n}
\mathbf T_i^a\mathbf T_j^b\mathbf T_k^c\;\Theta(-z_i)\,\mathrm{sign}(s_{ij})\,\Theta(-s_{jk})\;
\ln\frac{s_{j\tilde P}\,s_{k\tilde P}\,z_1z_2}{s_{jk}\,s_{12}}\times[\text{IR poles; CdFR eq. (184)}],
$$

  non-zero only in the SL region and absent in DIS kinematics. For n = 4 QCD partons it is `∝ f_abc T_1^aT_2^bT_3^c`
  (eq. (186)) and `Sp^{(0)†} f_abc T_1^aT_2^b Sp^{(0)} = 0` (eq. (187), from colour conservation in the splitting) **[S6]**, so
  it does not contribute; for n ≥ 5 (parton + parton → 3 partons) the term `f_abc T_2^aT_3^bT_4^c ln(s_34 s_5P̃/(s_35 s_4P̃))`
  survives as an operator (eq. (192)).
* **Pure QCD (FSS 2012):** the two-loop non-factorizing part is (FSS eq. (5.5))
  `P^{(2)}_{n.f.} = ½ Sp^{(0)†}[I^{(1)}+I^{(1)†}+I_C^{(1)fact}+I_C^{(1)fact†}, Δ̃_C^{(1)}]Sp^{(0)} + …`, a commutator of the
  Coulomb operator with eikonal exchanges. In a colour basis in which all `T_i·T_j` are real (which exists), this
  Hermitian operator is purely imaginary, hence antisymmetric, while pure-QCD tree amplitudes have relatively real
  components (`|M^{(0)}⟩⟨M^{(0)}|` symmetric): `⟨M^{(0)}|A|M^{(0)}⟩ = Tr[SA] = 0` (FSS eq. (5.8)) ⇒ no two-loop violation in
  pure QCD (FSS eq. (5.9); up to their not-yet-proven "second line"). Non-zero with relative phases between colour flows —
  in the SM only `qq̄′→qq̄′` and `qq̄→qq̄` with an s-channel W/Z (width) interfering with t-channel exchange. At three loops
  the double commutators of two Coulomb and one eikonal exchange survive (FSS eq. (6.1)), "in one-to-one correspondence with
  those obtained for the first non-zero super-leading logarithm" **[S5a–g]**: in the trace basis of `qq̄q′q̄′g` all `T_i·T_j`
  are real; `f_abc T_i^aT_j^bT_k^c = i[T_i·T_j, T_j·T_k]` (Hermitian); its expectation vanishes on real vectors and not on
  complex ones; `⟨[A,D]⟩ = 0`, `⟨[D,[D,A]]⟩ ≠ 0` on real vectors.

### 4.3 At which order — summary

| level | first order of violation | condition | source |
|---|---|---|---|
| amplitude (splitting matrix) | one loop | SL, two incoming coloured partons; genuine colour correlations need n ≥ 4 QCD partons; for n = 3 only the `i0` is process dependent | CdFR (46), (51)–(52), (66)–(67) |
| amplitude, DIS-type SL | none found (effective strict factorization at the orders computed) | all non-collinear partons outgoing | CdFR (65), Sec. 8 |
| squared, `P^{(1)}` | strictly factorized | — | CdFR (178)–(180) |
| squared, `P^{(2)}` | two loops (operator level) | n ≥ 5 QCD partons | CdFR (181)–(192) |
| squared, pure QCD | three loops | expectation on QCD tree amplitudes | FSS (5.8)–(5.9), (6.1) |
| squared, QCD+EW | two loops | relative phases between colour flows (s-channel W/Z) | FSS Sec. 5 |
| cross section: mass-singularity factorization | "may invalidate ... starting at the N³LO" unless cancelled | single-inclusive high-p_T jet/hadron in hadron–hadron | CdFR Sec. 7.4 |
| entangled logarithms | small-Q_T dijet/dihadron: N³LO; 3-jet with small p_T,min: NNLO; gaps-between-jets SLL: N⁴LO | non-inclusive observables | CdFR Sec. 7.4 |
| current status | "appear to cancel at the level of cross sections in pure QCD up to NNLO, their impact at higher orders is still an open question" | — | Guan–Herzog–Ma–Mistlberger–Suresh 2024 |

### 4.4 Why collinear factorization survives for sufficiently inclusive cross sections

1. The violating terms are Coulomb/Glauber exchanges among incoming (or among outgoing) coloured partons (FSS). In a
   hadronic cross section the incoming states are colour-singlet hadrons: "at the longest distance scales, which
   contribute to the infrared poles of the full hadron-hadron cross section, the incoming particles are the colourless
   hadrons and the colour factor associated with the factorization violation is zero. This was a crucial step in the
   proof of the factorization theorem in Ref. [1] [= CSS 1988]" (FSS, verified). The exchanges involved are those of
   §1, which cancel by unitarity + contour deformation when the final state is summed over inclusively.
2. "We fully expect that the factorization breaking effects we have been discussing will cancel in inclusive
   observables, in accord with the theorem derived by Collins, Soper and Sterman and more recently by Aybat and Sterman.
   The cancellation ought to occur upon accounting for real emissions with the same cut-diagram topology as the virtual
   corrections we consider here. However, these cancellations will not be complete in non-inclusive observables ... we
   expect to be able to factorize collinear logarithms only up to a scale μ below which real emissions are summed
   inclusively" (FSS). Aybat–Sterman: the phases cancel "so long as the weight S(N) is chosen so that radiation of this
   scale is summed inclusively in all directions".
3. At the partonic level CdFR identify the configurations whose IR poles must cancel at N³LO (two-loop `2→3` with one
   low-p_T parton, eq. (212); one-loop `2→4`, eq. (213); one-loop `2→3+1 soft`, eq. (214)); "an explicit quantitative proof
   of such a cancellation would represent a highly non-trivial check of the validity of the factorization theorem beyond
   the NNLO" — not yet available (status 2024: GHMMS).
4. The mechanism is algebraic and visible in **[S5d,f,g]**: one Coulomb insertion is a phase (anti-Hermitian, drops out of
   `2Re⟨M^{(0)}|M^{(1)}⟩` **[S7]**); one Coulomb + one eikonal gives a commutator with zero expectation for relatively real
   amplitudes; two Coulomb + one eikonal give a double commutator that survives — and in an inclusive hadronic cross
   section it must then be cancelled by the Glauber/unitarity mechanism of §1, not by colour algebra alone.

Status: amplitude-level strict collinear factorization in SL limits **[V]**; inclusive collinear factorization in
hadron–hadron collisions **[A]** for DY-like processes (Ch. 10), weaker for jet/hadron production; the explicit N³LO
cancellation of the CdFR/FSS terms in such cross sections **[C]** (open).

### 4.5 Super-leading logarithms (Forshaw–Kyrieleis–Seymour 2006 → Becher–Neubert–Shao 2021)

* Observable: "gaps between jets" — dijets with a veto `Q_0` on radiation in a rapidity interval of width `Y` between them.
  The Coulomb (`iπ`) terms of the soft anomalous dimension spoil the real–virtual cancellation for an out-of-gap gluon
  collinear to an incoming parton ("breakdown of the plus prescription"): "collinear logarithms can be summed into the
  parton density functions only up to scale `Q_0`" (FKS, verified).
* First SLL at `O(α_s⁴)` relative to Born (FKS eq. (3.22)): `σ ∼ σ_0 (2α_s/π)⁴ ln⁵(Q/Q_0) π² Y`; for quark–quark scattering
  with one gluon outside the gap (FKS eq. (3.24)):

$$
\sigma_{1,\rm SLL}=-\,\sigma_0\Big(\frac{2\alpha_s}{\pi}\Big)^4\ln^5\!\frac{Q}{Q_0}\;\pi^2\,Y\;\frac{3N^2-4}{480}.
$$

  Why `α_s⁴`: the `O(α_s)` and `O(α_s²)` corrections "never involve more than one iπ term and hence any iπ terms must cancel
  since the cross-section is real"; two `iπ`'s first at `O(α_s³)`, but "the addition of the gluon with the lowest `k_T` can
  never generate a net factor of iπ" ⇒ first at `O(α_s⁴)` (FKS, verified). One out-of-gap gluon: tower `α_s^nL^{n+1}`,
  n ≥ 4; leading behaviour `α_s^nL^{2n−3}`, confirmed at n = 5 with two out-of-gap gluons (Keates–Seymour, JHEP 04 (2009)
  040, as cited by FSS).
* All orders (BNS 2021, verified): SLLs `α_s³L³ × α_s^nL^{2n} = α_s^{n+3}L^{2n+3}` (n ≥ 1) for generic `2 → l`; they need two
  insertions of the Glauber-phase operator `V^G` and one `Γ` in the last step, colour traces
  `C_{rn} = ⟨H_4 (Γ^c)^r V^G (Γ^c)^{n−r} V^G Γ ⊗ 1⟩` (BNS eq. (13)) and

$$
\hat\sigma^{\rm SLL}_n=\Big(\frac{\alpha_s}{4\pi}\Big)^{n+3}L^{2n+3}\,\frac{(-4)^n\,n!}{(2n+3)!}\sum_{r=0}^{n}\frac{(2r)!}{4^r(r!)^2}\,C_{rn}
\qquad(\text{BNS eq. (14)}),
$$

  absent at large `N_c`; only with two coloured incoming partons; `2→1` (e.g. `qq̄→V+jet`) from four loops, `2→0` (e.g. Higgs
  with a central jet veto) from five loops, contrary to earlier statements that two coloured final-state partons are
  needed. Follow-ups (abstracts verified): BNSS 2023 (SCET factorization theorem, all-order resummation; sizable for
  `pp→2` jets, suppressed for H/Z(+jet)); BHMN 2025 (`pp→2` jets, all channels; some `qq̄→qq̄` interference terms only
  linearly suppressed in `1/N_c`); Banfi–Forshaw–Holguin 2026 (one-jettiness in colour-singlet + jet production has SLLs
  from `α_s⁴ ln⁶(1/τ_1)`, "consistent with the factorization of universal parton distribution functions at scale `τ_1Q`").
* Link to §4.2: FSS — the three-loop collinear-factorization-violating terms have "a structure identical to that
  encountered previously in the case of super-leading logarithms", both "driven by the non-commutation of Coulomb/Glauber
  gluon exchanges with other soft exchanges".
* Status: **[P]** (computed at fixed order and resummed at LL in specific observables; they signal the limit of collinear
  factorization for non-global observables rather than a failure of PDF universality for inclusive ones).

---------------------------------------------------------------------------------------------------------

## 5. Cross-checks against the literature (PASS/FAIL), with convention conversions

| # | result derived/checked here | checks | literature | conversion / remark | verdict |
|---|---|---|---|---|---|
| 1 | DY S–S: A-spectator `k^-` pole UHP, A-active LHP, both `O(λ²Q)`; `k^+` mirror | P1a,e; SS1a | CSS review eq. (166) | CSS route the soft momentum into the active line `ℓ+q` (spectator `p−ℓ−q`) = our routing | PASS |
| 2 | S–A, A–S: one variable free (deformable); A–A: no collinear pinch | P1b–d; SS5 | CSS review §9.3; CQ eq. (3.12) (DY initial-state eikonal) | — | PASS |
| 3 | DIS FSI and e+e−: no trapping; eikonal line accurate on the deformed contour | P1f,g; P4 | CQ eqs. (3.8)–(3.9); Collins 1998 Sec. III B | — | PASS |
| 4 | Glauber exchange is leading power (`Q^0λ^0`) | P5 | CSS review §8 ("order Q^0 times logarithms") | — | PASS |
| 5 | `V(k_T) = −ie_Ae_B/(k_T²+m_g²)`, `χ(b) = −e_Ae_B K_0(m_gb)/(2π)` | SS1d; SS3a,b | RS eq. (9.1) `φ(b) = −T_1·T_2 g²∫đ^{d−2}q e^{iq·b}/q²`; AS eq. (14) | `e_Ae_B ↔ g²T_A·T_B`; `∫d²q e^{iq·b}/[(2π)²(q²+m²)] = K_0(mb)/(2π)` | PASS (same form, same sign) |
| 5b | same kernel and phase | SS1d, SS3a | independent computation of the c_dy agent (`research/c_dy/DERIVATION.md` §7.2–7.3, eikonal Wilson lines and residues) | identical conventions (vertex `+ig(p+p')^μ`, Feynman gauge); their relative momentum `p = −Δ` | PASS (agree) |
| 6 | two S–S cuts cancel only after `∫d²Δ`; all-orders abelian phase | SS3c–e; U3a,b | RS eqs. (11.12)–(11.13); CQ Sec. III B | — | PASS |
| 7 | cut-sum identity `= i(ΠA − ΠB)`, `∫dE/2π → δ_{N1}` | U1, U1-int | derived (Collins 2011 Ch. 14 equation numbers not verified) | — | PASS (derived) |
| 8 | AS eikonal identity and causal identity | U2, U2b | AS eqs. (3)–(4), (10) | `i0` dropped for non-zero `q_i` | PASS |
| 9 | E7.24 | P3a–c | blueprint E7.24 | — | PASS |
| 10 | `X = L + (C_A/2)c` | U5a | RS §5.2.1 ("different color factors") | RS give no explicit formula | PASS (consistent) |
| 11 | `E(l) = −iπ(2g_2+g_1)δ(l^+) − g_1PV(1/l^+)` | A1, A1b | C07 eq. (2); CQ eqs. (4.1)–(4.3) | CQ write `−g(2k−l)/(…)` ↦ `+igπδ`: overall sign convention only | PASS |
| 12 | anomaly `4π²g_2(g_2+g_1)δδ`; same-side = minus; `g_1g_2` terms = `E(l_1)E(l_2)` | A3a–d, A2c | C07 eqs. (3), (4), (7), (8) | — | PASS |
| 13 | RM eikonal sums `±4π²δδ` | A2d,e | RM eqs. (25), (26), (35), (36) | — | PASS |
| 14 | `∫d²k(I_1+I_2) = 0`, `I_1(0)+I_2(0) < 0`, sign change | A4a–e | C07 text after eq. (11); RM eqs. (27)–(28) | printed C07 eq. (10) has a typo (extra numerator), corrected | PASS (source typo noted) |
| 15 | `C_G = 1 + 2⟨T_a·T_b⟩/C_F`, six channels, exact in N | C1, C2, C5 | BBMP (B5a,b), (B6a,b), Table I | SIDIS = +1 normalization identical | PASS |
| 16 | QVY Table I (`C_u, C_I, C_F1, C_F2`) for all six diagrams | C1 | QVY Table I, eqs. (25)–(28) | QVY's colour factors include the `1/N_c²` average | PASS |
| 17 | BBMP gauge links reproduce their `C_G` | C4 | BBMP (A11)–(A12), (B3), Table I | — | PASS |
| 18 | RM colour factors (Figs. 3, 4, 7, 8) | C3 | RM eqs. (14), (18), (27)–(28), (34) | RM write `t^a` at the spectator vertex; with `t̄ = −t^T` Fig. 3 is `−C_F` relative to the tree; divide by `N_c` (`N_c²`) for one (two) loops | PASS |
| 19 | entanglement: `Σ C(X,Y) = C_F² + 4T_F²(N²−1)/N² ≠ C_F²` (SU(N)); equal for U(1) | C6, C6b | RM Sec. VI (generalized prediction 0 for Fig. 8) | — | PASS (consistent) |
| 20 | CdFR eqs. (40), (42)–(44), (46), (68), (187); non-proportionality for n ≥ 4 | S1b, S2, S3, S4a–c, S6 | CdFR | CS charges = CdFR's | PASS |
| 21 | `P^{(1)}` strictly factorized (anti-Hermitian breaking term) | S7 | CdFR eqs. (178)–(180) | — | PASS |
| 22 | `Tr[SA]=0`; tripole Hermitian; single vs double commutator | S5a–g | FSS eqs. (5.5)–(5.9), (6.1) | — | PASS |
| 23 | DDIS: `r^-` trapped, `r^+` escapes; hh diffraction: both trapped | D1a–e | Collins 1998 §III D (Figs. 5, 6), conclusions | — | PASS |
| 24 | first SLL at `α_s⁴L⁵`; `(3N²−4)/480` coefficient; BNS tower | — | FKS eqs. (3.22), (3.24); BNS eqs. (13), (14) | quoted, not recomputed | quoted |

No check failed. The single "failure" encountered is in the literature (C07 eq. (10), see §2.4).

---------------------------------------------------------------------------------------------------------

## 6. Discrepancies with the outline / blueprint (with corrections)

1. **Blueprint P10.4** ("for a gluon exchanged between an outgoing spectator of A and an incoming active parton line of B
   (or between spectators), poles in `k^-` (or `k^+`) lie on both sides, so P7.19 does not apply graph by graph").
   *Correction:* for spectator(A)–active(B) the `k^-` contour is trapped but the `k^+` contour is **not** (only the
   initial-state pole of b); P7.19 applies via `k^+` deformation and yields the past-pointing Wilson line in `f_A`. Only
   the spectator–spectator exchange is a genuine Glauber pinch in both variables (§1.2 table).
2. **Blueprint E10.10 / R10.12 / P12.3.** The eikonal-phase attribution "(Cheng & Wu, verify)" can be replaced by verified
   sources: Aybat–Sterman eq. (14) (explicit abelian phase), Rothstein–Stewart eqs. (9.1), (9.18)–(9.19), (11.12)–(11.13).
   The exact one-exchange kernel is `V(k_T) = −ie_Ae_B/(k_T²+m_g²)`, `χ(b) = −e_Ae_BK_0(m_gb)/(2π)` (§1.5). RS do **not** give
   an independent full proof for DY: their S–S cancellation after the `Δp_⊥` integral, "taken alone ... is far from a proof
   of factorization, even in the abelian case". R10.12's "[A] independent support" should read "supporting evidence (S–S
   Glauber phase cancels after the `Δp_⊥` integral; A–A Glauber = soft zero-bin)".
3. **Blueprint T12.2** (description of the counterexamples). (a) The Rogers–Mulders explicit counterexample is a **double
   transverse-spin asymmetry** (double Sivers effect) in an SU(N_c) spectator model with a colour-neutral hard exchange;
   the unpolarized non-abelian case is only indicated (their Fig. 11). (b) "In an abelian version the phases cancel, in the
   non-abelian case they do not" is inaccurate: in the abelian model the two-gluon terms are consistent with
   **generalized** factorization (C07 eq. (8); Vogelsang–Yuan 2007) but violate **standard** factorization (anomaly
   `4π²g_2(g_2+g_1)δδ`, `I_1+I_2 ≠ 0` point by point, cancelling only after `∫d²k_T`); the non-abelian failure of
   **generalized** factorization comes from graphs with one gluon from each hadron (RM Fig. 8, colour `T_F²(N_c²−1)` vs
   generalized prediction 0). (c) "Collins, arXiv:0708.4410 (verify)": verified; not published in a journal; its eq. (10)
   contains a typo (§2.4).
4. **Blueprint P12.4** "(verify order)": first SLL at `O(α_s⁴)` relative to Born, `∝ α_s⁴L⁵` (FKS eqs. (3.22), (3.24));
   all-order tower `α_s^{n+3}L^{2n+3}` (BNS 2021, verified); `2→0` processes from five loops.
5. **Blueprint P12.5** "(verify)" and "according to CdFR the violating terms cancel in inclusive cross sections at the orders
   they examined": *correction* — CdFR do **not** show a cancellation; they show `P^{(1)}` is strictly factorized, `P^{(2)}`
   is not (operator non-zero for n ≥ 5 QCD partons), and state that this "may invalidate the factorization theorem of mass
   singularities starting at the N³LO" unless cancelled by other subprocesses (which they identify). FSS: for pure QCD the
   two-loop term has zero expectation; violation at three loops; two loops only with EW phases. Status as of
   arXiv:2408.03019 (2024): appear to cancel in pure-QCD cross sections up to NNLO; open beyond.
6. **Blueprint T12.8** ("no Glauber problem with only one incoming hadron"; "final-state interactions are summed over
   (P7.17)"): *correction* — in DDIS there **is** a Glauber pinch in `r^-` for soft gluons attached to the target subgraph
   (initial + final-state lines; the target final state is constrained, so one cannot sum over its cuts); the proof
   escapes by deforming `r^+` (only final-state jet poles nearby, target poles at `|r^+| ~ Q`), Collins 1998 §III D. The
   soft-factor cancellation concerns only the region unaffected by the diffractive requirement.
7. **Blueprint R12.9** ("overestimated ... by about an order of magnitude (CDF 2000)"): confirmed via CDF's own summary
   ("suppression by a factor of O(10)", arXiv:1206.3955); the CDF 2000 abstract itself does not quote the factor. Add
   ACTW 1999 and H1 2007 / Klasen–Kramer 2008 (photoproduction factors 0.5 / 0.42–0.71) as further evidence.
8. **Blueprint L10.5** and **P7.17** cite "Collins (2011) ch. 14 (verify section numbers)": could not be verified here (book
   not accessible); the corresponding identities are derived and checked in this directory (§1.5 Step 5).
9. **Blueprint E7.24**: verified as stated (with `∫dk^-`, no `1/2π`), **[P3a–c]**.
10. **Ch. 10 / Ch. 12 wording "Glauber region, contour deformation, cancellation"**: add the two-gluon non-abelian caveats
   of §1.6 (colour-matrix phase; non-commutation with soft exchanges; Gaunt 2014 vs Schwartz–Yan–Zhu 2018 for
   MPI-sensitive observables; Zeng 2015 counterexample for vetoed DY), which the blueprint does not mention.

---------------------------------------------------------------------------------------------------------

## 7. Open points and limitations

* No equation/section number of Collins (2011) is quoted (book not accessible). The full texts of Bodwin 1985 and CSS
  1985/1988 were not read (abstracts only); the step-by-step argument in §1.5 is reconstructed from the CSS review,
  Collins–Qiu, Aybat–Sterman, Rothstein–Stewart and our own explicit model computation.
* The pole-coefficient rule used in §2.3 (same pole coefficient for incoming and outgoing quark lines, opposite for
  antiquarks) is derived from the eikonal propagators and agrees with all CQ/RM eikonal formulas and with every entry of
  QVY Table I / BBMP; it assumes the standard eikonal approximation at leading power.
* The toy models (§3.4, §1.5 Step 4 grids) illustrate mechanisms; they are not quantitative QCD predictions.
* The bracket of IR poles in CdFR eq. (184) was not transcribed (typesetting ambiguous in the extracted text); only the
  operator structure is quoted.
* Experimental tension: H1 reports suppression also of direct diffractive photoproduction, which Collins' proof covers in
  principle; unresolved here.

## 8. LaTeX snippets

`tex/c_glauber_snippets.tex` (Chinese, monograph style, uses `\tagA \tagV …`, `proofsketch`); test build
`tex/test_c_glauber.tex` (compile with XeLaTeX inside `tex/` after copying `../../../common/*.tex`).
