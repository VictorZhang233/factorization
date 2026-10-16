
---

## Chapter 17 — Summary: master table and open problems (总结)

### 17.1 Purpose
Close the book with (i) the **master table** (identical rows and tags as Table 1.1, plus a column "which hypothesis of T7.20 is the bottleneck" and a column "what would upgrade the tag"), (ii) a list of open problems, each tied to a specific statement in the book.

### 17.2 Master table — extra columns to add to Table 1.1
| Result | Bottleneck | Upgrade path |
|---|---|---|
| T4.8 | — (already [R] in PT) | non-perturbative: construction of QCD |
| T5.12/T6.14 | (NP-OPE) for hadrons | non-perturbative OPE |
| T8.6 | L7.10 (non-abelian multi-gluon Ward identity), T7.14 | complete subtraction proof (as for the Sudakov form factor) |
| T9.3 | as T8.6 | same |
| T10.9 | (H3) Glauber + interplay with subtractions | complete all-order Glauber subtraction formalism |
| P10.14 | (H3)/(H4) with coloured final states | detailed published proof |
| T11.10 | (H3), rapidity-divergence scheme equivalence | as T10.9 + all-order scheme equivalence |
| Cj15.5 | gauge completion beyond NNLO | all-order proof or counterexample |
| P14.12 | endpoint divergences at subleading power | subleading-power factorization with endpoint refactorization |

### 17.3 Open problems (each 1 paragraph, with the precise statement it would settle)
1. Complete, published all-order proof of inclusive DY factorization including Glauber subtractions (would upgrade T10.9 to [R] in PT).
2. Non-perturbative status of factorization (any of the theorems in a constructed QFT; relation to lattice).
3. Collinear factorization for $pp\to$ jets/hadrons in the same detail as DY (P10.14).
4. Positivity of $\MSbar$ PDFs (R6.17).
5. NRQCD production factorization (Cj15.5).
6. Factorization at subleading power: endpoint divergences and their refactorization (e.g. Liu & Neubert, JHEP 04 (2020) 033; Beneke et al., JHEP 03 (2019) 043 — **verify both**), relevance for $B$ physics (P14.12) and DY threshold.
7. Unification of collinear, TMD and high-energy factorization at small $x$ (P12.12).
8. Consequences of amplitude-level factorization violation (P12.5) and super-leading logarithms (P12.4) at higher orders.
9. Double parton scattering beyond double DY (P12.11).
10. Power corrections in LaMET near the endpoints; renormalon-free schemes (T16.10).

### 17.4 Page budget: 4 (min 3). Figures: none (tables only).

---

## Appendices (附录)

**General rule:** appendices contain complete proofs that would interrupt the chapters; every appendix result carries a tag and is referenced from the chapter where it is used.

### Appendix A — Light-front coordinates, plus distributions, Mellin transforms (4 pp)
Contents: γ-matrix identities for $\gamma^\pm$ ($(\gamma^\pm)^2=0$, $\{\gamma^+,\gamma^-\}=2$), projectors $P_\pm$, Fierz decomposition used in D7.2 (leading term $\frac14\gamma^-\operatorname{Tr}[\gamma^+\Phi]$ and the transverse-spin and helicity terms); boosts (L2.8, full proof); plus distributions (L2.20 proof); table of Mellin transforms of $\mathcal D_k$, $\ln^kz$, $z^m$; harmonic sums $S_k(N)$, analytic continuation via $\psi^{(k)}$; Mellin inversion contour; L2.22 proof for distributions. Tags: all [R].

### Appendix B — Wilson lines (6 pp)
Contents: path-ordered exponential as solution of $\frac{d}{ds}W=ig\,\dot z\cdot A\,W$; covariance proof (P2.10); composition/retracing; derivation of the momentum-space rules for past/future/conjugate lines (P2.11); abelian eikonal identity (L2.12) and its colour-ordered non-abelian form; eikonal limits of incoming/outgoing quark propagators with $\pm i0$; one-loop cusp divergence (time-like vs light-like cusps; light-like lines and rapidity divergences; Korchemsky & Radyushkin, Nucl. Phys. B283 (1987) 342). Tags [R].

### Appendix C — Dimensional-regularization integrals (5 pp)
Contents: one-loop master formula $\int\frac{d^Dl}{(2\pi)^D}\frac{(l^2)^a}{(l^2-\Delta)^b}$ (c_pdf checked numerically for non-integer $D$); Feynman parameters; transverse integrals $\int d^{2-2\varepsilon}l_T$; $D$-dimensional two- and three-body phase space (with the $\Omega_{D-2}$ normalization used by c_dis); scaleless integrals $=0$ and the UV/IR interpretation ($\int d^{2-2\varepsilon}l_T/l_T^2\propto\frac1{\varepsilon_{\rm UV}}-\frac1{\varepsilon_{\rm IR}}$); the $\MSbar$ factor $S_\varepsilon=(4\pi)^\varepsilon e^{-\varepsilon\gamma_E}$ and the identity $g_0^2(2\pi)^{-(3-2\varepsilon)}\pi^{1-\varepsilon}=\frac{\alpha_s}{2\pi}\mu^{2\varepsilon}e^{\varepsilon\gamma_E}$ (c_pdf); $\Gamma$-function expansions ($e^{\varepsilon\gamma_E}\Gamma(1+\varepsilon)\Gamma^2(1-\varepsilon)/\Gamma(1-2\varepsilon)=1-\frac{\zeta_2}2\varepsilon^2+O(\varepsilon^3)$). Tags [R].

### Appendix D — Landau equations and Coleman–Norton (7 pp)
Full proofs of T3.2 (α-form; contour deformation $\alpha_j\to\alpha_j-i\eta\alpha_j\partial_j\mathcal F$, homogeneity, envelope theorem), T3.3 (momentum form; Gordan's theorem of alternatives, with proof of Gordan's theorem via separating hyperplanes), T3.5 (Coleman–Norton); endpoint singularities; an example of a non-isolated pinch surface (massless vertex). Tags [R].

### Appendix E — Power counting (5 pp)
Full derivation of P3.9 by the dimension + boost method: rest-frame scaling of collinear subgraphs, boost factors of indices and spinors (L2.8), counting of collinear loop measures, the one-dimensional jet-direction measure for cut graphs, soft subgraphs by dimensional analysis; the three checks (Sudakov form factor; real emission with the explicit numerator suppression; twist-3/twist-4 counting); the SCET$_{\rm II}$ (soft $\sim\lambda Q$) variant used in Ch. 11; comparison with Sterman (1978) and Collins (2011) ch. 5 formulas **(the writer must reconcile notation and confirm equality with the literature formula)**. Tags: computation [R]; leading-region theorem [A].

### Appendix F — Graphical Ward identities (5 pp)
Abelian identity in full (L7.7–L7.8); non-abelian one-gluon identity from BRST (P7.9) in full; two-gluon identity with the ghost term computed explicitly (E7.23) in full; inductive step for $n$ gluons in sketch (L7.10); derivation of the Wilson-line Feynman rules of the PDF from the summed identities. Tags: [R] for $n\le2$, [A] for the general inductive step.

### Appendix G — One-loop calculations (6 pp)
Only what is not in the chapters: $e^+e^-$ three-body integrals (P4.11) in one fixed normalization; optional two-loop massless $\Pi$ (E4.17); DY real/virtual integrals (E10.11); TMD one-loop (E11.15); details of P6.12 (massive-gluon regulator). Each with a short "how this was verified" note (sympy scripts of c_dis/c_pdf and the corresponding agents).

### Appendix H — Annotated bibliography (3 pp + reference list)
Per chapter: primary sources (what each proves, at what level), textbooks (Collins 1984, 2011; Sterman 1993; Muta; Ellis–Stirling–Webber; Becher–Broggio–Ferroglia), reviews (CSS 1989; Beneke 1999; Diehl 2003; Ji et al. 2021). Every **(verify)** flag of this blueprint must be resolved by the `refs` agent before the bibliography is frozen.
