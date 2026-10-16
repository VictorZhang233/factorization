# WRITER_SPEC_v2 — binding rules for the chapter and appendix writers (spec v2)

Monograph: 《QCD 因子化定理：严格证明、全阶论证与适用边界》. This file was drafted on 2026-10-10 by the spec-v2 writer-spec/figures/bibliography drafter (revision v2.1, same day: keyed to `verify/CLAIMS.md`, rule corrections in §4.4, §4.6, §10) and brought to **revision v2.2** at the merge by the spec-v2 integrator (aligned with `FINAL_OUTLINE_v2.md`: merge decisions MD1–MD18, named gaps, global-only R_cond rule, hidden forward dependencies, App A–L budgets, Part VII ownership, writer assignment §12.3 — see CHANGELOG). It **supersedes** `spec/WRITER_SPEC.md` (v1) in full: every v1 rule that is still valid is restated here, so a writer never needs the v1 file.

**Companion files (all in `spec_v2/`).**
- `FINAL_OUTLINE_v2.md` — what each unit must contain: sections, canonical statements (type, label, Chinese title, tag + qualifier, assumption/MA line, precise statement, `\uses` list, proof plan), the master-table rows (§09) and the **label registry** (§08; owner of every canonical label), the merge decisions MD1–MD18 (§0.8) and the merged [PENDING-VERIFY] register (§0.10). Its §08 contains the register table `### Assumptions`; the full register is `ASSUMPTIONS.md` (revision v2.2; binding texts = the owners' entries, MD18). The drafts `OUTLINE_core.md`, `OUTLINE_appMNOPQ.md`, `OUTLINE_frontier.md` are **superseded** and must not be used.
- `VERIFIED_FORMULAS_v2.md` — the only source from which formulas are copied (IDs `VF-…`).
- `FIGURES_INDEX_v2.md` — which figures exist, who owns them, and how to draw the new ones.
- `refs_merged_v2.bib` (1003 entries), `key_aliases_v2.tsv`, `REFS_NOTES_v2.md` — what may be cited and how.
- `checks/` — the scripts referred to below (`check_unit_v2.py`, `build_refs_v2.py`, `vf_v2_checks.py`, …) and their logs.

**Order of authority** when documents conflict:
1. the binding lead-author decisions quoted in §1.1 (structure, keys, page budgets, tag system, formalism);
2. this file;
3. `FINAL_OUTLINE_v2.md` (content, labels, tags, owners, assumption register);
4. `VERIFIED_FORMULAS_v2.md` (formulas);
5. `CONTEXT.md` and `REQUIREMENTS.md`;
6. spec v1 files (`spec/`), where not superseded;
7. research, frontier, refdoc and verify files.

A writer who finds an actual error in a higher-ranked file fixes it in the unit, explains the fix in the final report (§13), and **never** silently changes a tag, a canonical label, an owner or an assumption.

**Pending inputs.** The verification workflow (`verify/`: two-stage independent verification of all claimed errata and new results; proof extensions X1 Glauber, X2 subtraction, X3 OPE) was still running when this file was written. Every place that depends on its outcome is marked **[PENDING-VERIFY]** in FINAL_OUTLINE_v2 and here; a later spec patch finalizes them (protocol in §6.12). The workflow's claims register `verify/CLAIMS.md` (137 claims: errata **E01–E36**, new results **N01–N29**, corrections of the reference document **R-…**, attributions **A01–A28**) appeared while this file was being finished; spec v2.1 keys every pending item to these IDs (§6.5, §6.9, §6.12, §6.13; REFS_NOTES_v2 §1.5, §3.5; the pending register of VERIFIED_FORMULAS_v2; FIGURES_INDEX_v2 §0 rule 9), so that the verify patch can be applied mechanically.

---------------------------------------------------------------------------------------------------

## 0. What changed with respect to v1 (summary)

| topic | v1 | v2 | section |
|---|---|---|---|
| structure | 22 chapters, 6 parts, App A–L, 300 pp | 25 chapters, 7 parts + summary, App A–Q, ≈487 pp | §1, §11 |
| new chapters | — | Ch2 `qcd` (pedagogical QCD), Ch22 `lamet`, Ch23 `yzliu`, Ch24 `front` | §1, §7, §12 |
| moved material | — | QCD basics of v1 Ch2 → Ch2 `qcd`; v1 Ch21 `lattice` → Ch22 `lamet` (labels unchanged) | §5.3 |
| new appendices | — | M `appM` (OPE), N `appN` (subtraction), O `appO` (LCOPT/Glauber), P `appP` (blueprint), Q `appQ` (errata) | §1, §6.3, §6.13 |
| `[R]` qualifiers | R_PT, R_def, "以 OPE 为前提" | R_PT, R_def, **R_OPE**, **R_cond** (exactly one per `[R]`) | §4.3 |
| assumptions | MA0–MA4 (umbrella) | `assumption` environments with `asm:` labels; register; MA0–MA4 kept as umbrella names | §4.4 |
| dependencies | `\uses` "inside theorems" | **mandatory** `\uses` in every def/asm/lem/prop/thm/cor/conj; completeness and ordering rules; grade propagation; App P generated from it | §4.5–§4.6 |
| error types | — | E-S, E-P, E-F, E-N, E-W (refdoc S7) | §4.7 |
| grade dictionary | — | external A/A*/B/B′/C/D ↔ our tags (refdoc S8), printed without citing the reference document | §4.8 |
| chapter format | status paragraphs | + box 「本章证明了什么／没有证明什么」, correspondence tables with App M/N/O (refdoc S45) | §6.6, §6.7 |
| misconceptions | M1–M28 | M1–M35 (refdoc S57) with v2 allocation | §6.8 |
| forbidden over-claims | v1 list | v1 list + refdoc S58 + frontier items | §6.9 |
| new results | "no new results" | 「本书新结果」 only after two independent confirmations in `verify/` + literature check (refdoc S59) | §6.5 |
| reference document | — | never cited, quoted or copied (refdoc S62) | §6.10 |
| readability | — | Part I: start from basics, define before use, many worked examples | §7 |
| bibliography | 646 entries | 1003 entries (v1 + frontier + 46 spec-v2 additions, 5 of them in v2.1), 0 BibTeX warnings | §9 |
| pending items | — | keyed to the claim IDs of `verify/CLAIMS.md` (E/N/R/A) and to X1–X3 (v2.1) | §6.5, §6.12, §6.13 |
| QA | v1 label script | `checks/check_unit_v2.py` (owners from registry, `asm:`, `\uses`, qualifiers, status paragraphs); integrator: `checks/check_final_outline_v2.py` | §10 |
| integration (v2.2) | — | FINAL_OUTLINE_v2 assembled from the drafts; merge decisions MD1–MD18 (named gap `asm:appN-brst-nonlocal` [C]; (Z2) split; App A–L budgets; Part VII ownership; App P rules); writer assignment W01–W30 | §4.4–§4.7, §5.3, §5.6, §6.11–§6.13, §12 |

The refdoc change numbers S1–S63 refer to `refdoc/REFDOC_ANALYSIS.md` §5; they are given only to help the reader trace a rule. The reference document itself is never cited (§6.10).

---------------------------------------------------------------------------------------------------

## 1. Units, files and their structure

### 1.1 Binding structure (lead-author decision; chapter keys are label prefixes)

| # | key | file | short title (binding) | full Chinese title (v1 title where not binding) | pp | format | part |
|---|---|---|---|---|---|---|---|
| — | — | `front.tex` | 摘要、阅读指南、严格性标签、记号与约定 | 同左 | 6 | front (written by the Ch1 writer) | — |
| 1 | `intro` | `ch01_intro.tex` | 引言 | 引言：部分子图像、因子化的含义与严格性分级 | 14 | full | I 基础 |
| 2 | `qcd` | `ch02_qcd.tex` | QCD 基础——从规范不变性到渐近自由 | 同左 | 18 | **pedagogical** (§7) | I |
| 3 | `prelim` | `ch03_prelim.tex` | 因子化的数学与场论工具 | 同左 | 12 | full | I |
| 4 | `ir` | `ch04_ir.tex` | 红外结构 | 费曼积分的红外结构：钳夹、幂次计数与红外安全 | 15 | full | I |
| 5 | `sudakov` | `ch05_sudakov.tex` | Sudakov 形状因子与振幅的红外结构 | 同左 | 14 | full | I |
| 6 | `ee` | `ch06_ee.tex` | $e^+e^-$ | 严格核心 I：$e^+e^-$ 湮灭总截面 | 14 | full | II 严格核心 |
| 7 | `dis` | `ch07_dis.tex` | DIS 与 OPE | 严格核心 II：深度非弹散射与算符乘积展开 | 18 | full | II |
| 8 | `pdf` | `ch08_pdf.tex` | 算符定义 | 严格核心 III：部分子分布与碎裂函数的算符定义 | 15 | full | II |
| 9 | `method` | `ch09_method.tex` | 一般方法 | 全阶因子化证明的一般方法 | 20 | full | III 共线因子化 |
| 10 | `disall` | `ch10_disall.tex` | DIS 全阶 | DIS 的全阶动量空间证明、重夸克与核靶 | 13 | full | III |
| 11 | `coll` | `ch11_coll.tex` | 其他共线过程 | 其他共线过程：单举湮灭、SIDIS、光生、极化与横度 | 13 | full | III |
| 12 | `dy` | `ch12_dy.tex` | Drell–Yan | Drell–Yan 过程与强子—强子碰撞 | 18 | full | III |
| 13 | `thr` | `ch13_thr.tex` | 阈值 | 阈值重求和与重新因子化 | 9 | short | III |
| 14 | `tmd` | `ch14_tmd.tex` | TMD | 横动量依赖（TMD）因子化 | 16 | full | IV 共线之外 |
| 15 | `scet` | `ch15_scet.tex` | SCET | 有效场论方法：SCET | 13 | full | IV |
| 16 | `jets` | `ch16_jets.tex` | 喷注 | 喷注、事件形状、非全局对数与超领头对数 | 10 | short | IV |
| 17 | `smallx` | `ch17_smallx.tex` | 小 $x$ | 小 $x$ 与高能因子化 | 9 | short | IV |
| 18 | `break` | `ch18_break.tex` | 破坏 | 因子化的破坏与非标准情形 | 14 | full | IV |
| 19 | `excl` | `ch19_excl.tex` | 遍举 | 硬遍举过程 | 11 | short | V 其他硬过程 |
| 20 | `heavy` | `ch20_heavy.tex` | 重夸克 | 重夸克物理：$B$ 介子衰变与重夸克偶素 | 10 | short | V |
| 21 | `power` | `ch21_power.tex` | 幂次修正 | 幂次修正、次领头幂次、重整化子与非微扰地位 | 13 | full | VI 极限 |
| 22 | `lamet` | `ch22_lamet.tex` | LaMET 与格点因子化：季向东等人的因子化证明 | 同左 | 18 | **frontier** (§6.11) | VII 前沿进展 |
| 23 | `yzliu` | `ch23_yzliu.tex` | Yizhuang Liu 的严格因子化研究 | 同左 | 15 | frontier | VII |
| 24 | `front` | `ch24_front.tex` | 其他前沿严格结果 | 同左 | 18 | frontier | VII |
| 25 | `summary` | `ch25_summary.tex` | 总结：主表、依赖图与开放问题 | 同左 | 12 | full | (after Part VII) |
| A–L | `appA`…`appL` | as v1: `appA_lightfront.tex`, `appB_wilson.tex`, `appC_dimreg.tex`, `appD_landau.tex`, `appE_powercount.tex`, `appF_ward.tex`, `appG_oneloop.tex`, `appH_literature.tex`, `appI_gamma5.tex`, `appJ_brst.tex`, `appK_moments.tex`, `appL_lightray.tex` | v1 titles | v1 titles | 3,3,3,4,3,3,3,2,2,3,4,2 (= 35; rebalanced at the merge, MD5; v1: 3,4,3,4,3,3,4,2,2,2,3,2) | appendix | 附录 |
| M | `appM` | `appM_ope.tex` | OPE：微扰证明、无质量 QCD、非微扰条件定理 | 同左 | 24 | appendix (proofs) | 附录 |
| N | `appN` | `appN_subtraction.tex` | Collins 减除法的精确形式 | 同左 | 24 | appendix (proofs) | 附录 |
| O | `appO` | `appO_glauber.tex` | 光锥排序微扰论与 Drell–Yan 的 Glauber 相消 | 同左 | 32 | appendix (proofs) | 附录 |
| P | `appP` | `appP_blueprint.tex` | 形式化蓝图：假设登记表、依赖图与状态表 | 同左 | 10 | generated + written introduction (§6.13) | 附录 |
| Q | `appQ` | `appQ_errata.tex` | 经核实的文献勘误 | 同左 | 4 | written after `verify/` completes (§6.13) | 附录 |
| | | | | **total** front 6 + chapters 352 + appendices 129 | **≈487** | | |

Notes.
1. The full titles of Ch1, Ch4, Ch6–Ch21 are the v1 titles; FINAL_OUTLINE_v2 may shorten them to the binding short titles. If the two differ, FINAL_OUTLINE_v2 wins; the `\chapter{}` title is whatever FINAL_OUTLINE_v2 prints.
2. **Key clash `front`.** The key of Ch24 is `front`. The front matter (`front.tex`) owns exactly one label with this prefix, the v1 table label `tab:front-notation` (and continuation labels `tab:front-notation-b`, `-c`, … if the table is split). Every other `…:front-…` label belongs to Ch24. Ch24 must not define `tab:front-notation*`.
3. Appendix budgets A–L total 35 pp (lead-author decision). At the merge they were rebalanced inside the 35 pp (MD5): A 3, B 3, C 3, D 4, E 3, F 3, G 3, H 2, I 2, J 3, K 4, L 2, because refdoc S50/S53 add lemmas to App K and App J; the lead author may restore the v1 split, never by deleting statements.
4. **Parts.** The master file issues seven `\part` commands (I 基础 before Ch1; II 严格核心 before Ch6; III 共线因子化 before Ch9; IV 共线之外 before Ch14; V 其他硬过程 before Ch19; VI 极限 before Ch21; VII 前沿进展 before Ch22) and `\appendix` before App A. Ch25 follows Part VII; whether it gets an unnumbered part divider is decided by the integrator. Writers never issue `\part` or `\appendix`.

### 1.2 File structure

1. A chapter file starts with `\chapter{<中文标题>}\label{ch:<key>}`; an appendix file with `\chapter{<中文标题>}\label{app:<key>}` (e.g. `app:appM`).
2. No `\documentclass`, `\usepackage`, `\begin{document}`, `\part`, `\appendix`, `\bibliography` or `\bibliographystyle`.
3. `front.tex` contains the abstract, the reading guide (incl. the five tags, the **four** `[R]` qualifiers, the register in one paragraph, reading paths through the seven parts) and the notation table `tab:front-notation` (§3). It uses `\chapter*` with `\addcontentsline`.
4. **Macros.** Use only the packages and macros of `common/preamble_fact.tex` (it must not be modified). No `\newcommand`/`\def` at file level; a local abbreviation is allowed inside a group and must be reported. Missing macro → write the expansion and ask in the report. There are **no** macros for the qualifiers or for the boxes of §6.6: write them out as specified.
5. **Encoding and comments.** UTF-8, LaTeX `%` comments only, no TODOs in the output. Use the placeholder protocols of FIGURES_INDEX_v2 §0 (figures) and §9 (citations) instead. The planning markers `[PENDING-VERIFY]` and 「待文献核查」 must never be printed (§6.12).
6. **Self-containment.** Each unit reads correctly on its own. The first paragraph says what the unit proves and at which level, in the tag vocabulary; it is followed by the box of §6.6 (where required). Material from other units is cited with `\cref`, never repeated at length.

---------------------------------------------------------------------------------------------------

## 2. Language, typography, terminology

1. **Language.** Simplified Chinese, academic monograph style: complete sentences, no bullet-point prose in the main text except lists of hypotheses, steps, and the boxes of §6.6. At first use of a technical term give the English in parentheses, e.g. 「钳夹（pinch）」「程函线（eikonal line）」「快度发散（rapidity divergence）」「大动量有效理论（large-momentum effective theory，LaMET）」; afterwards use the Chinese term consistently.
2. **Glossary (binding; v1 list extended).**

   | English | 中文 | English | 中文 |
   |---|---|---|---|
   | factorization | 因子化 | gauge invariance | 规范不变性 |
   | leading power | 领头幂次 | gauge fixing | 规范固定 |
   | power correction | 幂次修正 | ghost (field) | 鬼场 |
   | Wilson line | Wilson 线 | running coupling | 跑动耦合 |
   | soft factor | 软因子 | asymptotic freedom | 渐近自由 |
   | collinear | 共线 | (anti)screening | （反）屏蔽 |
   | ultrasoft | 超软 | vacuum polarization | 真空极化 |
   | Glauber region | Glauber 区 | infrared safety | 红外安全 |
   | coefficient function | 系数函数 | quasi-PDF / pseudo-PDF | 准分布 / 赝分布 |
   | hard part | 硬部分 | Ioffe time | Ioffe 时间 |
   | parton distribution | 部分子分布 | matching kernel | 匹配核 |
   | fragmentation function | 碎裂函数 | hybrid (renormalization) scheme | 混合（重整化）方案 |
   | splitting function | 分裂函数 | ratio scheme | 比值方案 |
   | anomalous dimension | 反常维度 | off-light-cone | 离光锥 |
   | subtraction | 减除 | intrinsic (reduced) soft function | 本征（约化）软函数 |
   | reduced diagram | 约化图 | heavy–light Sudakov form factor | 重—轻 Sudakov 形状因子 |
   | pinch surface | 钳夹面 | space-like jet function | 类空喷注函数 |
   | light-cone ordered perturbation theory (LCOPT) | 光锥序微扰论 | short-distance factorization (SDF) | 短距离因子化 |
   | normal product | 正规乘积 | edge-of-the-wedge theorem | 楔边定理 |
   | weak equivalence | 弱等价 | forward tube | 前向管 |
   | assumption (numbered) | （编号）假设 | dependency graph | 依赖图 |
   | rigorous / all-order argument / partial / conjecture / violated | 严格 / 全阶论证 / 部分 / 猜想 / 破坏 | blueprint | 蓝图 |

3. **Names.** Personal names stay in Latin script, except names that are part of a binding title. In particular **"Yizhuang Liu" is never transliterated** into Chinese characters (the frontier agent could not verify the Chinese name; different drafts even use different characters). 「季向东」 may be used because it is in the binding title of Ch22; elsewhere write "Ji" or 「季向东（Xiangdong Ji）」 at first use. No biographical or career information beyond an affiliation printed in a cited paper.
4. **Punctuation.** Full-width punctuation in Chinese prose（，。；：？！（）“”「」、）; ASCII inside math. A displayed equation ends with ASCII punctuation inside the display (`,` or `.`, preceded by `\,` or `\quad` if needed); never a full-width 「，」 inside math.
5. **Spacing.** No space between Chinese text and `\cite`, `\cref` or inline math: 「见\cref{thm:dis-ope}的证明」「文献\cite{Collins2011}指出」「其中$x$为」. The preamble inserts the CJK–Latin glue, including after `\cref`. `~` only in Western contexts and in location arguments (§9).
6. **Cross-references.** Always `\cref{...}` (no `\ref`, except inside table captions referring to tables, and no hard-coded numbers). Do not put several *section/chapter/appendix* labels in one `\cref` (the preamble lacks the multi-format for these and prints English): write 「\cref{sec:a}与\cref{sec:b}」. Several *statement* labels in one `\cref` are fine (Chinese conjunctions are defined).
7. **Macros from the preamble.** Symbols `\as`, `\MSbar`, `\dd`, `\ii`, `\ee`, `\order{…}`, `\Tr`, `\TrD`, `\Trc`, `\sla{p}`, `\pT`, `\kT`, `\bT`, `\qT`, `\Lqcd`, `\Real`, `\Imag`, `\Disc`; tags `\tagR`, `\tagA`, `\tagP`, `\tagC`, `\tagV`; `\uses{…}`; environments of §4.1 and `proofsketch`. Use either the macros or the explicit forms consistently within a unit (recommended: `\as`, `\MSbar`, `\dd` in integrals, `\ii` in exponentials and propagators, `\ee` for Euler's number).
8. **Parts of a cut.** $H$, $J$, $S$ for the hard, jet and soft subgraphs; a reduced diagram is 「约化图」.
9. **Numbers and units.** 「$\alpha_s(M_Z)=0.1180$」 with GeV in roman (`\,\mathrm{GeV}`). No experimental number without a citation (the only experimental numbers in the VF file are the PDG world average, VF-QCD-7, and the numbers quoted in v1 entries with their sources).
10. **Harmless warning.** The `cremark` head font produces "Font shape `TU/FandolKai-Regular(0)/m/it' undefined"; do not try to fix it in a unit file.

---------------------------------------------------------------------------------------------------

## 3. Notation and conventions (typeset in `front.tex` as `tab:front-notation`)

These conventions are binding for every unit. "VF" refers to `VERIFIED_FORMULAS_v2.md`. When quoting literature in other conventions, convert, and say so in a footnote or remark: 「（换算到本书约定：…）」. Rows 1–37 are the v1 rows (with the audit corrections); rows 38–48 are new in v2.

| # | object | convention of this book | remarks / conversions | VF |
|---|---|---|---|---|
| 1 | metric, light front | $(+,-,-,-)$; $v^\pm=(v^0\pm v^3)/\sqrt2$; $v\cdot w=v^+w^-+v^-w^+-\mathbf v_T\cdot\mathbf w_T$ | hadron $A$ along $+z$, hadron $B$ along $-z$ | CONV-1 |
| 2 | light-like vectors (all units except Ch15) | $n_A=(1^+,0^-,\mathbf 0_T)$, $n_A\cdot v=v^-$; $n_B=(0^+,1^-,\mathbf 0_T)$, $n_B\cdot v=v^+$ | $n_B$ = Collins' $w_2$; the PDF line of $A$ runs along $n_B$ ($n_B\cdot A=A^+$); c_exclusive's $\bar n,n$ are our $n_A,n_B$ | CONV-1 |
| 3 | SCET vectors (Ch15 only) | $n=(1,0,0,1)$, $\bar n=(1,0,0,-1)$, $n\cdot\bar n=2$, $\bar n\cdot p=\sqrt2p^+$, $n\cdot p=\sqrt2p^-$ | RS and the blueprint use the swapped order; convert | CONV-22 |
| 4 | covariant derivative, couplings | $D_\mu=\partial_\mu-igA^a_\mu t^a$, vertex $ig\gamma^\mu t^a$, ${\rm Tr}(t^at^b)=\frac12\delta^{ab}$, $C_F=\frac{N_c^2-1}{2N_c}$, $C_A=N_c$, $T_F=\frac12$; $[D_\mu,D_\nu]=-igG_{\mu\nu}$ | **Collins 2011, BBL, the LaMET/Liu papers and Ji et al. use $g\to-g$ relative to us** (their $D=\partial+igA$, Wilson lines $P\exp(-ig\int A)$); BBL's $c_{2,3,4}$ signs flip; all LaMET one-loop kernels are even in $g$ | CONV-2/3, QCD-1/2, NRQ-1 |
| 5 | Feynman rules | quark $\frac{i(\slashed p+m)}{p^2-m^2+i0}$; gluon $\frac{-i}{k^2+i0}[g^{\mu\nu}-(1-\xi_g)\frac{k^\mu k^\nu}{k^2}]$; ghost $\frac{i}{p^2+i0}$; three-gluon $gf^{abc}[g^{\mu\nu}(k-p)^\rho+\dots]$ (incoming); ghost vertex $-gf^{abc}p^\mu$ ($p$ outgoing ghost) | = Peskin–Schroeder ch. 16; $\xi_g=1$ Feynman gauge | CONV-3 |
| 6 | dimensional regularization | $D=4-2\varepsilon$, CDR ($\{\gamma^\mu,\gamma^\nu\}=2g^{\mu\nu}$, $g^\mu{}_\mu=D$, ${\rm Tr}\,1=4$); bare scale $\mu_0$ ($g_0^2=4\pi\alpha_s\mu_0^{2\varepsilon}$) | pole origin always stated: $\varepsilon_{\rm UV}$ vs $\varepsilon_{\rm IR}$ (critic C14) | CONV-4 |
| 7 | $\overline{\rm MS}$ | $g_0^2=4\pi\alpha_s(\mu)\mu^{2\varepsilon}S_\varepsilon^{-1}Z_g^2$, $S_\varepsilon=(4\pi)^\varepsilon e^{-\varepsilon\gamma_E}$ | **Collins 2011: $S^{\rm C}_\varepsilon=(4\pi)^\varepsilon/\Gamma(1-\varepsilon)$**; $S_\varepsilon/S^{\rm C}_\varepsilon=1+\frac{\pi^2}{12}\varepsilon^2$; ESZ/JJYZZ differ by $\pi^2/6$ terms in the same way | CONV-4, TMD-5 |
| 8 | running coupling | $\mu^2\frac{d\alpha_s}{d\mu^2}=-\frac{\beta_0}{4\pi}\alpha_s^2-\frac{\beta_1}{(4\pi)^2}\alpha_s^3-\frac{\beta_2}{(4\pi)^3}\alpha_s^4$, $\beta_0=\frac{11}3C_A-\frac43T_Fn_f$ | for $a=\alpha_s/\pi$: $b_0=\beta_0/4$, $b_1=\beta_1/16$ (Ch6); SCET/BS: $b=\beta_0/(4\pi)$; **Liu et al. use two other normalizations** (row 45) | CONV-5, QCD-5/6, EE-9 |
| 9 | expansion parameters | stated at the head of every formula block: $\frac{\alpha_s}{2\pi}$ (DIS, DY, PDFs), $a=\frac{\alpha_s}\pi$ ($e^+e^-$, CSS), $a=\frac{C_F\alpha_s}{4\pi}$ (SCET), $\frac{\alpha_s}{4\pi}$ (cusp $\Gamma_n$), **$a=\frac{\alpha_sC_F}{2\pi}$ (LaMET kernels, Ch22–Ch23)** | never mix within one display | LAM-0 |
| 10 | power counting | $\lambda=m/Q$ (or $q_T/Q$); scalings in $(k^+,k^-,k_T)$: $A$-coll. $(1,\lambda^2,\lambda)$, $B$-coll. $(\lambda^2,1,\lambda)$, soft $(\lambda,\lambda,\lambda)$, usoft $(\lambda^2,\lambda^2,\lambda^2)$, Glauber $(\lambda^2,\lambda^2,\lambda)$ | **Sterman units:** $\omega$ = power of $\lambda_S=\lambda^2$; Libby–Sterman "soft" = our ultrasoft; **in Ch22–Ch23 the letter $\lambda$ is the Ioffe time (row 40)**: write power-counting parameters there as explicit ratios ($\Lambda/P^z$, $1/(b_TP^z)$, $e^{-Y}$) | CONV-19, REG-7/8 |
| 11 | e.m. current, $\Pi$, $R$ | $j^\mu=\sum e_q\bar q\gamma^\mu q$; $i\int e^{iqx}\langle Tj^\mu j^\nu\rangle=(q^\mu q^\nu-q^2g^{\mu\nu})\Pi$; $R=12\pi\,{\rm Im}\,\Pi(s+i0)$; $\sigma_{\mu\mu}=\frac{4\pi\alpha^2}{3s}$ | $\Pi_{\rm PS}=-e^2\Pi$ | CONV-12 |
| 12 | hadronic tensor | $W^{\mu\nu}=\frac1{4\pi}\int e^{iqz}\langle P|[j^\mu(z),j^\nu(0)]|P\rangle=(-g+\frac{qq}{q^2})F_1+\frac{\tilde P\tilde P}{P\cdot q}F_2$ | general $F_L=(1+\frac{4M^2x^2}{Q^2})F_2-2xF_1$ | CONV-13 |
| 13 | Compton amplitude | $T^{\mu\nu}=i\int e^{iqz}\langle P|Tj^\mu j^\nu|P\rangle$; ${\rm Im}\,T_i=2\pi F_i$; $T_1$ even, $T_2$ odd in $\omega=1/x$ | free quark $T_2=4e_q^2\omega/(1-\omega^2)$; Euclidean segment $\mathcal I_Q$ (VF-REF-1) | CONV-14, REF-1 |
| 14 | quark PDF | $f_{q/H}(\xi;\mu)=\int\frac{dw^-}{4\pi}e^{-i\xi P^+w^-}\langle P|\bar\psi(w)\gamma^+W[w,0]\psi(0)|P\rangle_c$, $w=(0^+,w^-,\mathbf 0_T)$; colour summed, target averaged; $f_{\rm ren}=Z\otimes f_{\rm bare}$ | support $|\xi|\le1$ (PT [R]; hadrons [A]) | PDF-1, PDF-4 |
| 15 | antiquark PDF | $f_{\bar q}(\xi)=-f_q(-\xi)$; $q(x)=f_q(x)$, $\bar q(x)=-f_q(-x)$ ($x>0$) | equivalent to the $\psi^c$ definition | PDF-1 |
| 16 | gluon PDF | $f_{g/H}(\xi)=\sum_j\int\frac{dw^-}{2\pi\xi P^+}e^{-i\xi P^+w^-}\langle P|G^{+j}_aW^{(A)}_{ab}G^{+j}_b|P\rangle_c$; $f_g(-\xi)=-f_g(\xi)$ | CDR: partonic gluons averaged over $D-2$ polarizations | PDF-2, CONV-6 |
| 17 | DGLAP | $\frac{\partial f_i}{\partial\ln\mu^2}=\sum_j\mathcal P_{ij}\otimes f_j$, $\mathcal P_{ij}=\frac{\alpha_s}{2\pi}P_{ij}+\dots$; $(f\otimes g)(x)=\int_x^1\frac{d\xi}\xi f(\xi)g(x/\xi)$ | MVV: $P^{(0)}_{\rm MVV}=2P$ | PDF-7, PDF-10 |
| 18 | anomalous dimensions | $\gamma_{ij}(N)=\int_0^1z^{N-1}P_{ij}$; $\frac{dA^{(n)}}{d\ln\mu^2}=\frac{\alpha_s}{2\pi}\gamma(n)A^{(n)}$; $\Gamma_{q_kg}=2\gamma_{qg}$ | $\gamma^{(0)}_{\rm MVV}=-2\gamma$; Gross–Wilczek $\gamma_O=-\frac{\alpha_s}\pi\gamma$ | CONV-16, PDF-8 |
| 19 | twist-2 operators | $\langle P|O_i^{\mu_1\cdots\mu_n}|P\rangle=2A_i^{(n)}(P\cdots P-{\rm tr})$; $O_g^{+\cdots+}=\sum_jG^{+j}(iD^+)^{n-2}G^{+j}$ | $A_q^{(n)}=\int_0^1x^{n-1}[q+(-1)^n\bar q]$ | CONV-15, PDF-11 |
| 20 | fragmentation function | hadron frame $\mathbf p_{h,T}=0$: $d_{h/q}(z)=\frac{z^{1-2\varepsilon}}{4N_c}\sum_X\int\frac{dw^-}{2\pi}e^{ik^+w^-}{\rm Tr}[\gamma^+\langle0|W[\infty n_B,w]\psi(w)|hX\rangle\langle hX|\bar\psi(0)W[0,\infty n_B]|0\rangle]$, future-pointing lines; parton frame: $\frac1{4N_cz}$ with explicit $\int d^{2-2\varepsilon}\mathbf p_{h,T}$ | refdoc S9 (applied); partonic $\overline{\rm MS}$ coefficient functions unaffected | CONV-17 |
| 21 | plus distributions | $\int_0^1[g]_+h=\int_0^1g(h-h(1))$; $\mathcal D_k=[\ln^k(1-z)/(1-z)]_+$; product convention $g\mathcal D_k=g(1)\mathcal D_k+\frac{g-g(1)}{1-z}\ln^k(1-z)$ | $(1+z^2)\mathcal D_1=[\frac{(1+z^2)\ln(1-z)}{1-z}]_++\frac74\delta(1-z)$; **LaMET kernels use plus distributions on three domains, $[g]^{D}_{+(1)}$ (row 41)** | CONV-7, DY-12, LAM-8 |
| 22 | event-shape distributions | star distributions $[\cdot]_*$; $\tau$-space plus distributions subtract at $\tau=0$, with the sentence 「此处加号分布在 $\tau=0$ 处减除」 | never mix with row 21 in one formula | CONV-20 |
| 23 | Mellin transform | $\tilde f(N)=\int_0^1z^{N-1}f$; $S_1(N)=\psi(N+1)+\gamma_E$; $\bar N=Ne^{\gamma_E}$ | continuation from even $N$ unique under polynomial bounds (App K) | CONV-8, MISC-1 |
| 24 | Laplace transform (Ch15) | $\tilde t(\nu)=\int d\tau\,e^{-\nu\tau}\frac1{\sigma_0}\frac{d\sigma}{d\tau}$, $s=1/(e^{\gamma_E}\nu)$ | Becher–Schwartz | CONV-21 |
| 25 | $\gamma_5$, $\epsilon$ tensor | $\gamma_5=i\gamma^0\gamma^1\gamma^2\gamma^3$, $\epsilon^{0123}=+1$, ${\rm Tr}(\gamma^\mu\gamma^\nu\gamma^\rho\gamma^\sigma\gamma_5)=-4i\epsilon^{\mu\nu\rho\sigma}$; DR: HVBM + Larin | Larin's replacement in our convention: $\gamma^\mu\gamma_5=-\frac i6\epsilon^{\mu\nu\rho\sigma}\gamma_\nu\gamma_\rho\gamma_\sigma$ | CONV-10, CONV-24, POL-1 |
| 26 | transverse tensors | $g_\perp^{\mu\nu}=g^{\mu\nu}-n_A^\mu n_B^\nu-n_B^\mu n_A^\nu$, $\epsilon_\perp^{\mu\nu}=\epsilon^{\mu\nu\rho\sigma}n_{A\rho}n_{B\sigma}$, $\epsilon_\perp^{12}=+1$ | | CONV-10 |
| 27 | Wilson lines | $W[b,a]=P\exp(ig\int_a^bdz\cdot A)$, later points left, $W\to U(b)WU^\dagger(a)$; $A(x)=\int\frac{d^4k}{(2\pi)^4}e^{-ikx}\tilde A(k)$, $k$ flows into the line; adjoint $W^{(A)}_{ab}=2{\rm Tr}[t^aWt^bW^\dagger]$ | space-like lines (Ch22–Ch23): same definition with a space-like path | CONV-9 |
| 28 | eikonal rules | vertex $igt^av^\mu$, propagator $\frac i{v\cdot\ell+i0}$; past-pointing $W[0,-\infty n]$: $\prod\frac{i}{n\cdot(k_1+\dots+k_j)+i0}$; future-pointing $W[\infty n,0]$: $\prod\frac{-i}{n\cdot(k_j+\dots+k_m)-i0}$; future − past at the same point: $2\pi i\,gt^an^\mu\delta(n\cdot k)\tilde A_\mu$ | DIS future ($-i0$); DY past ($+i0$) **after** the one-sided rewriting (a single cut graph gives future lines, VF-REF-11) | WL-1, WL-12, REF-11 |
| 29 | cusp, CS kernel | $\Gamma_{\rm cusp}=\sum(\frac{\alpha_s}{4\pi})^{n+1}\Gamma_n$, $\Gamma_0=4C_F$; $\gamma_K=2\Gamma_{\rm cusp}$; $\tilde K=-\frac{\alpha_sC_F}\pi\ln\frac{\mu^2b_T^2}{b_0^2}$; $\Gamma(\beta)=\frac{\alpha_sC_F}\pi(\beta\coth\beta-1)$ | BS arXiv $\Gamma_1$ misprint; **Liu et al.'s $K$ = our $\tilde K$** ($2\zeta\partial_\zeta\ln f=\tilde K$) | CONV-18/23, TMD-1/2, YZL-1 |
| 30 | TMD Fourier transform | $\tilde f(x,b_T)=\int d^{2-2\varepsilon}k_T\,e^{-ik_T\cdot b_T}f(x,k_T)$; $b_0=2e^{-\gamma_E}$, $\mu_b=b_0/b_T$; cross sections $\int\frac{d^2b_T}{(2\pi)^2}e^{+iq_T\cdot b_T}\tilde f_A\tilde f_B$ | Collins 2011 eq. (13.35) uses $e^{+ik_T\cdot b_T}$ for the soft factor and TMD FFs; Liu et al. write $d\sigma\propto\int d^2b\,e^{i\vec b\cdot\vec Q}$; check the sign of every $b$-odd structure | CONV-11 |
| 31 | TMD scheme | Collins' definition, $\zeta=2(xP^+)^2e^{-2y_n}$, $\zeta_A\zeta_B=Q^4$; space-like regulator lines; light-like limit at fixed $\varepsilon$, then $\overline{\rm MS}$, then $\varepsilon\to0$ | Liu's $\zeta=2(xP^+)^2e^{2y_n}$: the sign of $y_n$ may differ — convert before mixing (UNVERIFIED in the frontier report) | TMD-3/4/9 |
| 32 | spin conventions (TMD) | Trento conventions | Sivers sign (SIDIS) negative for attractive FSI in the spectator model | TMD-8 |
| 33 | DY normalization | $\sigma_0=\frac{4\pi\alpha^2}{3N_cQ^2}$; $\hat s\,d\hat\sigma_{ij}/dQ^2=\sigma_0e_q^2\Delta_{ij}(z)$; TMD cross sections carry $\sigma_0/s$ | | DY-1, DY-8, TMD-10 |
| 34 | exclusive | $f_\pi\approx130$ MeV ($F_\pi=f_\pi/\sqrt2$); DA with $x$ = quark fraction; GPD $\xi=\frac{p^+-p'^+}{p^++p'^+}$ ($\xi_{\rm Ji}=2\xi$) | VGG: $f_\pi=92.4$ MeV | EXC-1/2/12 |
| 35 | NRQCD | $\Gamma=\sum_n\frac{2{\rm Im}f_n}{m_Q^{d_n-4}}\langle O_n\rangle$, $m_Q$ = pole mass | BBL sign flips (row 4) | NRQ-1…4 |
| 36 | Borel transform | $R=\sum r_n\alpha_s^{n+1}$, $B[R](t)=\sum r_nt^n/n!$, $u=\beta_0t/(4\pi)$; pole at $u_0$ ⇒ ambiguity $(\Lambda^2/Q^2)^{u_0}$ | Liu–Su use $u=\beta_0t/2$ with their $\beta_0$ (row 45) | `def:power-borel` |
| 37 | colour, spin sums | averages: quark spin $\frac12$, colour $\frac1{N_c}$; gluon polarization $\frac1{D-2}$, colour $\frac1{N_c^2-1}$; polarization sums $-g_{\mu\nu}$ only where the Ward identity allows | | CONV-6, WL-9 |
| 38 | Glauber direction (refdoc S11) | $e_G\equiv n_B-n_A=(-1^+,+1^-,\mathbf 0_T)$, $e_G^2=-2$, $n_A\cdot e_G=+1$, $n_B\cdot e_G=-1$; $(l+it\sigma fe_G)^2-m^2=(l^2-m^2+2t^2f^2)+2it\sigma f(l^+-l^-)$ | an amplitude-side ($\sigma=+1$) soft momentum flowing into $J_A$ is deformed with ${\rm Im}\,k^->0$, ${\rm Im}\,k^+<0$ | REF-7 |
| 39 | error types (refdoc S7) | E-S scaling statement; E-P pointwise bound; E-F fibre-integral bound; E-N integral-norm bound $\int_A|F|\le C\lambda^aL^K$ uniformly in $\varepsilon$; E-W weak equivalence | §4.7 | — |
| 40 | Ioffe time (Ch22–Ch23) | space-like separation $z^\mu=z\,\hat e_z^\mu$; hadron $P=(P^0,0,0,P^z)$; **Ioffe time $\lambda\equiv P\cdot z=-P^zz$**; light-cone ITD $I(\lambda)=\int_{-1}^1dx\,e^{ix\lambda}f(x)$ | IJJSZ $\zeta=P^zz=-\lambda$; Radyushkin $\nu=-(p\cdot z)=-\lambda$; Ji et al. $\tilde\lambda=zP^z=-\lambda$ | LAM-1 |
| 41 | quasi-, pseudo-distributions | $\tilde q_\Gamma(x,P^z)=N_\Gamma\int\frac{dz}{4\pi}e^{ixP^zz}\langle P|[\bar\psi(z\hat e_z)\Gamma W[z\hat e_z,0]\psi(0)]_R|P\rangle$, $N_{\gamma^z}=1$, $N_{\gamma^0}=P^z/P^0$; pseudo-PDF $\mathcal P(x,-z^2)=\int\frac{d\lambda}{2\pi}e^{-ix\lambda}\tilde h(\lambda,z^2)$; plus distributions on a domain $D$: $\int_D[g]^D_{+(1)}h=\int_Dg\,(h-h(1))$ | $\Gamma=\gamma^0$ (= $\gamma^t$) preferred on the lattice (no same-dimension mixing at $O(a^0)$) | LAM-1, LAM-8 |
| 42 | LaMET logarithms | coordinate: $L_z=\ln(-z^2\mu^2e^{2\gamma_E}/4)$ ($-z^2=z_3^2>0$); momentum: $\ell_p=\ln(\mu^2/(4p_z^2))$, $p^z=|y|P^z$ (parton momentum), and $L_\zeta\equiv\ln(\zeta_z/\mu^2)=-\ell_p$ with $\zeta_z=(2xP^z)^2=4p_z^2$; TMD: $L_b=\ln(\mu^2b_T^2/b_0^2)$ | **Liu et al., JLS and the LaMET report's threshold section write $L_z$ for $\ln(\zeta_z/\mu^2)$ and $l_z$ for the coordinate log: in this book these are $L_\zeta$ and $L_z$**; the matching kernel depends on the parton momentum $|y|P^z$ | LAM-4…8, LAM-14 |
| 43 | quasi-TMD normalization | staple $\mathcal W_z$ of length $L$ along $\hat z$, $Z_E(2L,b_T,\mu)=\frac1{N_c}{\rm Tr}\langle0|W_\perp\mathcal W_z(b_T;2L)|0\rangle$; CS exponent **$\exp[\frac12\tilde K\ln(\zeta_z/\zeta)]$** | the printed $e^{\tilde K\ln(\zeta_z/\zeta)}$ of PLB 811 / RMP 2021 is wrong by a factor 2 (App Q candidate, [PENDING-VERIFY]) | LAM-15, YZL-5 |
| 44 | large-angle cusp constant | $\Gamma_{\rm cusp}(\alpha_s,\theta)=\theta\,\Gamma_{\rm cusp}(\alpha_s)+\gamma_{HH}(\alpha_s)+O(e^{-\theta})$, $\gamma_{HH}^{(1)}=-\frac{\alpha_sC_F}\pi$; $\mu^2\frac{d\ln S_I}{d\mu^2}=\gamma_{HH}$ | use $\gamma_{HH}$ only; Liu et al.'s $\Gamma_S$ has two opposite sign conventions | YZL-3 |
| 45 | $\beta$ conventions of Liu et al. | (a) PLB/APPB/RMP/PRD105: "$\beta_0=-\frac1{2\pi}(\frac{11}3C_A-\frac43N_fT_F)$" with $d\alpha_s/d\ln\mu=\beta_0\alpha_s^2$; (b) JHEP 2023/24: $d\alpha/d\ln\mu=-\beta_0\alpha^2$, $\beta_0=\frac{11C_A}{6\pi}-\frac{n_f}{3\pi}$ | $\beta_0^{(b)}=\beta_0^{\rm ours}/(2\pi)=-\beta_0^{(a)}$; RGEs in $\mu\,d/d\mu=2\mu^2d/d\mu^2$ | YZL-1 |
| 46 | hyperbolic angle | $\theta(v_1,v_2)={\rm Arcosh}\frac{v_1\cdot v_2-i0}{\sqrt{v_1^2+i0}\sqrt{v_2^2+i0}}$ | Table of the six configurations: VF-YZL-4 | YZL-4 |
| 47 | SU(N) identities | $[t^a,t^b]=if^{abc}t^c$, $t^at^a=C_F$, $f^{acd}f^{bcd}=C_A\delta^{ab}$, $t^a_{ij}t^a_{kl}=\frac12(\delta_{il}\delta_{kj}-\frac1N\delta_{ij}\delta_{kl})$, ${\rm Tr}(t^at^bt^c)=\frac14(d^{abc}+if^{abc})$ | verified for SU(2), SU(3) | QCD-1 |
| 48 | assumption labels | `asm:<owner-key>-<name>`; inner items cited as 「\cref{asm:intro-wightman}(W2)」 | inner item names are scoped by their assumption (§4.4) | — |

---------------------------------------------------------------------------------------------------

## 4. Statements: environments, tags, qualifiers, assumptions, dependencies

### 4.1 Environments

- `definition`, `assumption`, `theorem`, `lemma`, `proposition`, `corollary`, `conjecture`, `example`, `remark`; `proof` and `proofsketch` (prints 「证明概要」). All share one counter per chapter.
- Use the type given in FINAL_OUTLINE_v2 (定义/假设/定理/引理/命题/推论/猜想/例/注).
- Title: the Chinese title of the outline, then the tag macro: `\begin{theorem}[DIS 结构函数矩的因子化 \tagR]\label{thm:dis-moments}`.
- Pure mathematics carries **no tag** (`\begin{lemma}[偶数矩决定函数]`). Definitions carry no tag. A remark carries a tag only if the outline gives one.
- The tag is the outline's. It may be **weakened** with a justification in the report; it may **never be strengthened**.

### 4.2 The five tags (definitions printed in Ch1 `def:intro-tags`)

[R] 严格 · [A] 全阶论证 · [P] 部分 · [C] 猜想 · [V] 破坏, with the CONTEXT.md meanings. A tag refers to the statement **exactly as formulated**. 「凡涉及强子的陈述，最多只能达到'有严格的微扰论内容 + 编号假设'的地位」 (Ch1). Every hadron-level statement therefore separates its perturbative status (the tag) from its non-perturbative status (the line of §4.4 item 6).

### 4.3 The four `[R]` qualifiers (exactly one per `[R]`; verbatim)

The **first sentence** inside every `\tagR` environment is exactly one of the following strings (copy them; `check_unit_v2.py` compares character by character after mapping `–` to `--`):

| qualifier | verbatim first sentence | use |
|---|---|---|
| **R_PT** | 「（$R_{\mathrm{PT}}$：在重整化微扰论中对红外正规化的部分子态严格。）」 | statements about Feynman graphs / partonic Green functions with IR regulators, at every order, with **no** unproven input (incl. explicit fixed-order computations whose first sentence states the order) |
| **R_def** | 「（$R_{\mathrm{def}}$：由算符定义直接推出。）」 | algebraic consequences of field/operator definitions, symmetries and kinematics |
| **R_OPE** | 「（$R_{\mathrm{OPE}}$：以 OPE 为前提而严格。QCD 中含夸克的微扰 OPE 是全阶论证（\cref{thm:dis-ope}），严格证明只对标量理论与纯 Yang--Mills 的规范不变算符给出；对强子态还须非微扰 OPE（\cref{asm:intro-np-ope}）。）」 — after the first use in a unit the short form 「（$R_{\mathrm{OPE}}$：以 OPE 为前提。）」 is allowed | complete proofs whose only unproven input is the OPE (v1's 「以 OPE 为前提」; e.g. `thm:dis-moments`, `thm:pdf-dis-xspace`) |
| **R_cond** | 「（$R_{\mathrm{cond}}$：在所列编号假设之下证明完整；结论的地位不高于其中最弱的假设。）」, **immediately followed by** 「前提：\cref{asm:…}、\cref{asm:…}（及 \cref{…}）。」 | complete proofs from explicitly numbered assumptions and/or tagged statements, perturbative (`thm:appN-subtraction`-type) or non-perturbative (`thm:dis-moments-np`-type) |

Rules.
1. The premise sentence of R_cond lists **every** assumption and every non-[R] statement the proof uses; the same labels appear in `\uses` (§4.5).
2. The `\cref` inside the R_OPE qualifier is a pointer, not a dependency; it is not repeated in `\uses` unless the proof actually uses `thm:dis-ope`.
3. **Composite statements** (two tags for two parts, e.g. `prop:sudakov-kg` "[A]; one-loop content [R, R_PT]"): the environment title carries the **first** tag (the registry tag); the other part is a separate item with its status in words and macro, 「(b)（单圈内容，\tagR，$R_{\mathrm{PT}}$）…」. The qualifier rule then applies to that item, not to the first sentence of the environment.
4. **Frontier grade notations** are mapped as follows (never print the frontier notations):

   | frontier report notation | our representation |
   |---|---|
   | [R] in PT, diagram by diagram | [R, R_PT] |
   | [R]$_{1L}$ / [R]$_{2L}$ (explicit one-/two-loop computation, independently cross-checked) | [R, R_PT] **for the statement restricted to that order** (first sentence states the order); the all-order statement keeps its own tag ([A]/[P]) |
   | [R] (cond.), "rigorous given hypotheses" | [R, R_cond] with the hypotheses as `asm:` labels in the premise sentence |
   | [R] under Wightman-type axioms | [R, R_cond] with `asm:intro-wightman` (and the frontier assumptions it needs) |
   | [R] (model), "exact in a model" | [P] as a QCD statement whose first sentence names the model; the model-internal claim may get a full proof (as `prop:power-thooft-model`) |
   | [R]† (proof only in an unrefereed preprint) | the outline's tag; if the outline does not decide: [R] only if the proof is printed in full in this book (re-derived) or confirmed in `verify/`, otherwise [A]; the status paragraph says 「（证明仅见于预印本）」 |
   | sub-grades A−, A+ | dropped; the status paragraph may say how close the argument comes to [R] or [P] |
   | "open", "UNVERIFIED" | [C], or not printed (UNVERIFIED items are never printed as facts) |

### 4.4 Assumptions (`assumption` environment, `asm:` labels, the register)

1. **Every numbered assumption of the book** is an `assumption` environment with label `asm:<owner-key>-<name>`, owned by exactly one unit (the key is the owner's key: `asm:intro-*` in Ch1, `asm:appM-*`, `asm:appN-*`, `asm:appO-*`, and frontier assumptions such as `asm:lamet-*`, `asm:yzliu-*`, `asm:front-*` in their chapters). The list and the owners are those of the register (41 entries: 6 global `asm:intro-*`, 3 `asm:appM-*`, 13 `asm:appN-*`, 5 `asm:appO-*`, 9 `asm:lamet-*`, 3 `asm:yzliu-*`, 2 `asm:front-*`; FINAL_OUTLINE_v2 §08 `### Assumptions` = `ASSUMPTIONS.md` v2.2 §1). A writer never invents an assumption; an assumption that seems to be missing is reported.
2. **Title and tag.** `\begin{assumption}[<中文标题> \tag?]\label{asm:…}`. The tag records the status of the assumed claim **as the literature covers it** and is used by the grade propagation (§4.6): `\tagA` = the claim is covered by an all-order argument in the literature, although it is not proven as a precise statement ("[A]-level", e.g. `asm:appN-collins`, which Collins 2011 ch. 10 asserts; the App O inputs that the CSS/Collins Glauber argument covers); `\tagP` = proven only in special cases, at finite order or in models, with no all-order argument for the general claim; `\tagC` = no all-order argument exists; no tag = a convention or a choice (e.g. `asm:appN-values`). **The tag is the register's (FINAL_OUTLINE_v2) and is copied, never inferred**: the register's status sentences use "open" in the sense "not proven as stated", which is compatible with `\tagA` — do not map the word "open" to `\tagC`. If the register gives a status sentence but no tag, report it; only an explicit "no all-order argument" justifies `\tagC`, "[A]-level"/"argued at all orders" gives `\tagA`, "verified in cases/at fixed order" gives `\tagP`, "convention" gives no tag. (Spec v2.1 correction: v2.0 mapped "open" → `\tagC`, which would have forced `thm:dy-factorization` to [C] through the App O register entries, contrary to refdoc S5/S8, where these steps are the delicate but all-order-argued steps of an [A] result.) **v2.2:** `asm:appN-brst-nonlocal` (the multilocal BRST classification that Collins 2011 §11.3.2 assumes) is `\tagC` — no all-order argument exists — and is handled as a *named gap* (§4.6 item 6, MD1); `asm:appN-ir-regulator` is `\tagC` and a premise only of `thm:disall-renorm-compat` (MD2).
3. **Body fields, in this order** (refdoc S12): the statement (precise, with formulas, in our conventions; inner items (W1), (W2), … where needed); 「地位：」 (status, with the evidence); 「文献：」 (sources with locations); 「被使用于：」 (the labels that use it — copied from the register; the generator of App P checks it against the `\uses` data; these are **reverse** dependencies and never go into the assumption's own `\uses`, which would create forward edges or cycles — `check_unit_v2.py` C5 ignores this field); 「解除途径：」 (what would discharge it). A `\uses{…}` line lists the definitions the statement refers to (or `% uses: none`).
4. **Inner item names** ((W1)–(W4), (B1)(B2), (T1)–(T4), (Z1)–(Z3), (E1)–(E3), (GA1)–(GA4), …) are scoped by their assumption and always cited together with it: 「\cref{asm:appN-tmd}(T2)」. **Naming to avoid clashes:** the template hypotheses (H1)–(H5) of `thm:method-template` keep their names; Collins' subtraction conditions are (CS1)–(CS3); the geometric–analytic inputs (GA1)–(GA4); the CSS/Bodwin Glauber steps (CSS-1)–(CSS-6); the App O proof steps (O-1)–(O-8); the Glauber interface clauses (Gla-a)–(Gla-c). Hypothesis lists of the frontier reports must be renamed: the LaMET report's (H1)–(H5) become the register entries `asm:lamet-*` (or local items (L1)–(L5) if not in the register); Liu's lists (H1)–(H6), (T1)–(T5), (Q1)–(Q7), (S1)–(S3) become register entries or local items with chapter-unique prefixes (e.g. (AN1)–(AN6) for analyticity, (TO1)–(TO5) for time ordering, (QT1)–(QT7) for quasi-TMD, (ED1)–(ED3) for exponential decay). Never print a frontier report's own numbering (Thm 4.3, Prop 10.4, …). **Binding inner names (v2.2; full table `ASSUMPTIONS.md` §4):** `asm:intro-wightman` (W1)–(W4); `asm:intro-composite` (C1)–(C3); `asm:intro-np-ope` (O1)(O2); `asm:intro-bridge` (Br1)–(Br3); `asm:appM-brst-ope` (B1)(B2); (GA1)–(GA4) (`asm:appN-contour`, `def:appN-meet-closed`, `asm:appN-envelope`, `asm:appN-separation`); `asm:appN-values` (V1)(V2); `asm:appN-cutsum` (CU1)–(CU3); `asm:appN-ward-product` (WI1)(WI2); `asm:appN-uv` (U1)(U2); `asm:appN-multren` (Z1), (Z3)(i)(ii); `asm:appN-ir-regulator` (Z2); `asm:appN-tmd` (T1)–(T4); `asm:appN-endpoint` (E1)–(E3); `asm:appO-lcopt` (i)(ii); `asm:appO-mixing` (a)–(c); `asm:appO-deformation` (a)–(d); `asm:appO-rewritten-cs` (i)(ii); frontier (AX1)–(AX3), (OP1)(OP2), (UI-a)(UI-b), (TW1)(TW2), (LZ1)(LZ2), (GP1)–(GP3), (ST1)–(ST3), (SR), (OL1)(OL2), (HP1)–(HP3), (WP1)(WP2), (UL), (MR), (SM1)(SM2). Local (not assumptions): (CS1)–(CS3), (H1)–(H5), (Ctr) of `lem:appM-chain-expansion`, (ET1)(ET2) of `lem:appO-equal-time`, (GC1)–(GC3) of `def:appO-graded`, (h1)(h2) of `prop:appN-dy`, (Com)(Abs), (Φ) of `cor:dis-weak-xspace`, (QT1)–(QT7), (PS1)–(PS3), (J1)–(J4) of Part VII; App M's parts of "the OPE holds" are **(OPE1)–(OPE5)** (MD15; never "(O1)" without the scope `asm:intro-np-ope`).
5. **Stated once.** An assumption is stated only by its owner. Other units cite it (`\cref`, `\uses`) and may paraphrase it in one sentence. Ch1 prints the short register `tab:intro-assumptions` (label, one-line content, status, used by); App M §M.8 adds the technical commentary on `asm:intro-*` (which axiom is used where) but never a second statement. App P prints the generated register `tab:appP-register`.
6. **Non-perturbative status line** (replaces v1's MA line). Every statement about hadrons ends its hypotheses with
   「非微扰地位：\cref{asm:…}、\cref{asm:…}（MA…）。」
   listing the global assumptions of the register (`asm:intro-wightman`, `asm:intro-composite`, `asm:intro-np-ope`, `asm:intro-af-coeff`, `asm:intro-growth`, `asm:intro-bridge`) that the hadronic version needs, with the umbrella names MA0–MA4 in parentheses (dictionary: MA0 ⊃ wightman, composite; MA1+MA2 = bridge; MA3 = analyticity, now a theorem under MA0, + growth; MA4 ⊃ af-coeff). Statements about partonic states, operators or models only say so: 「（本命题只涉及部分子态。）」. A hadron-level statement found without this line gets the line of the corresponding master-table row (or `asm:intro-wightman`, `asm:intro-composite` for operator identities between hadron states) and is reported.
7. **Global vs technical assumptions.** The six `asm:intro-*` entries are *global non-perturbative* assumptions: they appear in the line of item 6 and as premises of explicitly non-perturbative R_cond theorems; they do **not** lower the (perturbative) tags of ordinary statements (§4.6). All other `asm:` entries are *technical* assumptions and enter the grade propagation.

### 4.5 `\uses` lists (mandatory; Lean-blueprint style)

1. **Where.** Every `definition`, `assumption`, `lemma`, `proposition`, `theorem`, `corollary` and `conjecture` environment contains exactly one `\uses{…}` line, written as the **last line of the statement body** (before `\end{…}`; it prints 「依赖：…」 inside the box). A tagged `remark` and every `example` that relies on other statements also carry one. If a statement depends on nothing in the book, write the comment line `% uses: none` instead (an empty `\uses{}` would break `\cref`).
2. **What.** List **every** label the statement or its proof actually uses as a step: definitions of the objects in the statement, the assumptions, the lemmas, propositions and theorems invoked in the proof (including those whose proofs are in an appendix), the examples/remarks used as steps. Pointers ("compare", "for a generalization see") are not dependencies. The writer's QA (`check_unit_v2.py`, check C5) lists every statement label that is `\cref`'d inside a statement or its proof but missing from its `\uses`; each must be added or justified as a pointer in the report.
3. **Only statement labels**: prefixes `def thm lem prop cor conj rem ex asm`. Never `sec:`, `eq:`, `fig:`, `tab:`, `ch:`, `app:` (they break the generator and print English with multiple targets).
4. **Order (no forward edges).** Each listed label must be (a) an assumption (`asm:`) owned by an earlier or the same unit, or by an appendix; (b) a statement of an earlier chapter; (c) an **earlier** statement of the same unit; or (d) a statement of an appendix. A label of a later chapter may appear only as a forward pointer in running text (「其一般形式见\cref{…}（第~N~章）」), never in `\uses` or as a proof step. Ch1, Ch25 and the front matter are overviews and may point forward freely, but their own statements (definitions, assumptions) obey these rules.
5. **Appendices.** Appendix statements may use statements of any chapter and of other appendices, provided no dependency cycle arises (the generator of App P reports cycles; the units concerned must resolve them, normally by moving a lemma into the appendix). **No hidden forward dependency (v2.2):** an appendix statement that a chapter-$k$ statement uses must not depend, directly or through other appendix statements, on a statement of a chapter $>k$; such references inside appendix statements are pointers in text (e.g. App O cites `def:dy-kin` and `ex:dy-future-vs-past` only as pointers, and owns the precise orientation lemma `lem:appO-orientation`, of which Ch12 `lem:dy-poles-orientation` is the chapter statement). Likewise a chapter statement never lists an appendix assumption that is formulated with objects of a later chapter (Ch4/Ch5 name `asm:appN-envelope`, `asm:appN-separation`, `asm:appN-ward-product`, `asm:appN-collins` only as pointers). Checked by `checks/check_final_outline_v2.py` (W2; FINAL_OUTLINE_v2 passes). A chapter statement whose proof is in an appendix lists, in its own `\uses`, the appendix lemmas the proof uses; the appendix section starts with 「\cref{…} 的证明」 and the appendix statement itself does not repeat the chapter statement.
6. **R_cond.** All assumptions and non-[R] statements of the premise sentence appear in `\uses`.
7. **Moved labels** (§5.3) are used with their unchanged names; the generator knows their owners from the registry.

### 4.6 Grade-propagation rule (refdoc S5; printed in Ch1 `def:intro-tags` and App P)

Order the tags $[R]>[A]>[P]>[C]$; $[V]$ is outside the order (a [V] statement is never the premise of a positive claim; it may be used in a remark or as a counterexample). Ignore, in the following, premises that are definitions, pure mathematics (no tag) or global non-perturbative assumptions (§4.4 item 7).

1. **Ordinary statements.** For a statement $S$ that is not R_cond: $\mathrm{tag}(S)\le\min_p\mathrm{tag}(p)$ over its `\uses` premises $p$, **except** that for an R_OPE statement the OPE premises — `thm:dis-ope` and its sub-statements `prop:dis-ope-euclid`, `prop:dis-ope-gi`, `prop:dis-ope-forward` (all [A]) — are not counted: they are the premise named by the qualifier, exactly as the `asm:` premises of an R_cond statement (spec v2.1 correction; without it every R_OPE statement, e.g. `thm:dis-moments`, would violate the rule). Qualifier compatibility for $[R]$: an R_def statement uses only R_def premises; an R_PT statement uses R_def and R_PT premises; an R_OPE statement uses R_def, R_PT, R_OPE premises and the OPE premises. **Content grade of R_OPE:** $c(S)=[A]$ (that of the perturbative OPE for QCD with quarks); a statement $T$ that uses an R_OPE statement and is not itself R_OPE or R_cond obeys $\mathrm{tag}(T)\le[A]$; an R_cond statement that uses it lists `thm:dis-ope` in its premise sentence. **Global-only R_cond premises (v2.2, MD4):** an R_cond statement whose premise sentence lists only global assumptions (`asm:intro-*`) and [R] statements has effective content grade [R] for perturbative users; it may be used in the hadron-level part of an R_PT or R_OPE statement provided that statement's 「非微扰地位」 line names the same global assumptions (`thm:dis-moments`(b) and `prop:lattice-moments` use `prop:dis-dispersion-np`, `thm:dis-fixed-n`, `thm:dis-moments-np` in this way).
2. **R_cond statements.** The implication is [R]; its **content grade** is $c(S)=\min_p\mathrm{tag}(p)$ over all premises listed in the premise sentence (assumption tags as in §4.4 item 2). A statement $T$ that uses $S$ is treated as using the premises of $S$: $\mathrm{tag}(T)\le c(S)$ (technical premises only, unless $T$ is itself non-perturbative).
3. **Process-level statements** built from R_cond implications carry the weakest grade among the technical assumptions they use: e.g. `thm:dy-factorization` stays [A] because the `asm:appN-*` and `asm:appO-*` it depends on are [A]-level (`\tagA`: the CSS/Collins argument covers them, while none is proven as a precise statement — the 「地位与缺口」 paragraph names them, refdoc S8 "B′") — if the register lists one of them as `\tagC` (no all-order argument at all), the process statement cannot be [A] and the outline must say how it is handled (report any mismatch).
4. **Status paragraph.** The 「地位与缺口」 paragraph (§4.9) of an [A]/[P] statement names the premise(s) that fix its grade.
5. **Generator checks (App P).** No forward edges; every `asm:` label is used at least once; no statement carries a tag stronger than allowed by items 1–3; every R_cond statement lists its premises in its first two sentences; no cycles; named gaps named (item 6, check C-P17).
6. **Named gaps (v2.2, MD1).** An explicitly assumed step of the standard literature argument that has no all-order argument of its own is registered (tag `\tagC`) so that the precise R_cond theorems can list it, but it is **not** a `\uses` premise of the chapter [A] statements whose literature grade already contains that step; those statements **name it** in their 「地位与缺口」 paragraph (「该论证中被明确假定的一步（\cref{asm:appN-brst-nonlocal}，[C]）」). At present exactly one entry is a named gap: `asm:appN-brst-nonlocal` (premise only of `thm:appN-structure`, whose content grade is therefore [C]); it is named by `lem:method-ward-multi`, `thm:method-template`, `prop:appF-induction`, `thm:disall-factorization`, `thm:dy-factorization`, and every other Feynman-gauge process chapter recalls it in its status paragraph (or through `thm:method-template`). A writer never adds a named gap to a `\uses` list and never creates a new one; a step that looks like one is reported.

### 4.7 Error types (refdoc S7; Ch1 `def:intro-error-types`, no tag)

| code | 中文 | meaning |
|---|---|---|
| E-S | 标度陈述 | scaling statement (power counting of a region, no bound) |
| E-P | 逐点界 | pointwise bound on an integrand |
| E-F | 纤维积分界 | bound after integrating one variable, pointwise in the rest |
| E-N | 积分范数界 | $\int_A|F|\,d\mu\le C\lambda^aL^K$ uniformly in $\lambda\in(0,\lambda_0]$, $\varepsilon\in(0,\varepsilon_0]$ |
| E-W | 弱等价 | equality of integrals over the sets of a fixed algebra, with all subtraction-term weights |

Every status table (`tab:dy-status`, `tab:appN-status`, `tab:appO-checklist`, `tab:appP-status`, `tab:appM-status`) has a column 「误差类型」; every step of an [A] or [P] proof sketch that rests on power counting says which type it establishes (「（此步只给出 E-S 型陈述）」). Writers record the error type of a statement's weakest step, where the outline gives one, in a comment line `% errtype: E-S` (or E-P, E-F, E-N, E-W) inside the environment; the App P generator reads it (column 「误差类型」 of `tab:appP-status`).

### 4.8 Grade dictionary (refdoc S8; Ch1 `rem:intro-grade-dictionary`, no tag)

Printed **without citing the reference document** (and without naming it): introduce it as 「文献中常见的另一种分级（按非微扰结构定理、CSS 标准的全阶证明等划分）」.

| external grade (literature practice) | our representation |
|---|---|
| non-perturbative structure theorem conditional on QFT axioms + OPE ("A") | PT part: [R, R_PT] or [R, R_OPE]; non-perturbative part: [R, R_cond] listing `asm:intro-*` |
| "as rigorous as the OPE given an EFT" ("A*") | [A] (quarkonium decay; non-perturbatively needs local duality, [C]) |
| all-order argument "by the CSS standard" ("B") | [A] for the process; the implication from the register is [R, R_cond] (App N); the bridge is `asm:intro-bridge` |
| "B with a delicate step" ("B′") | [A] + mandatory 「地位与缺口」 naming the `asm:appO-*` items (no extra tag) |
| conjecture *or* partial proof ("C") | split per statement: [P] (finite order / subclass / model) or [C] |
| proven broken ("D") | [V] + evidence type (model counterexample / explicit calculation / experiment) |

### 4.9 Status paragraphs (「地位与缺口」)

1. Required immediately after every [A], [P], [C] or [V] environment (and after its proof sketch, if any), starting with `\paragraph{地位与缺口}` or a bold run-in 「地位与缺口：」.
2. It names: the weakest step; **the `asm:` labels it depends on** (not only (H1)–(H5) or MA; refdoc S45.3); the error type of that step (§4.7); the literature location where the gap is acknowledged (e.g. 「\cite[第~14.4.8~节]{Collins2011}」); what would upgrade the tag; for frontier results whether the proof is refereed (「（预印本）」).
3. For [V]: whether the evidence is an explicit perturbative counterexample (model or QCD), an explicit calculation, or experiment (critic O17).
4. For [P] statements with a complete restricted proof: the paragraph states the general claim and why it is only partially established.

### 4.10 Proofs

1. "Proof: full" in the outline = a complete `proof` environment: every step justified, nothing deferred except standard mathematics with a citation, or a `\cref` to an earlier statement.
2. "Proof: sketch" = a `proofsketch` with the numbered steps of the outline, ending with 「完整论证见…」 (citation with location, or `\cref{app:…}` / the appendix statement when the full proof is in this book).
3. **[R, R_cond]** statements always get a full proof of the implication (they are the backbone of App M/N/O); write it "deliberately elementary" where the outline says so (e.g. `thm:appN-subtraction`).
4. **[A]** statements always get a `proofsketch`, never a `proof`. For deductions from stated hypotheses (`thm:method-template` and the process theorems deduced from it) the deduction is written out completely inside the `proofsketch` and the status paragraph names the weakest ingredient.
5. A **[P]** statement whose first sentence states its restriction may get a full `proof` of that restricted claim (`prop:dy-abelian-model`, `prop:power-adler-large-beta0`, `prop:power-thooft-model`, model theorems of Ch23).
6. **Appendix proofs.** The appendix section begins with 「\cref{thm:…} 的证明」; the chapter statement's proof environment says 「证明见\cref{app:appM}」 plus a three-line summary (or the `proofsketch` of the outline).

### 4.11 Forbidden phrasing (tags)

Never write 「严格证明了」 or 「已被证明」 for an [A] statement; use 「给出了全阶论证」 or 「在…假设下论证了」. Never write 「证明」 for the general claim of a [P], [C] or [V] statement; for the restricted claim of a [P] statement write 「在…模型（极限、阶）中证明了」. For R_cond write 「在\cref{asm:…}之下证明了」. When a statement of another unit is used, repeat its tag in words the first time in your unit: 「由\cref{thm:dy-factorization}（全阶论证，[A]）…」.

---------------------------------------------------------------------------------------------------

## 5. Labels

### 5.1 Scheme

- chapters `ch:<key>`, appendices `app:<key>`; sections `sec:<key>-<name>`; statements `def|asm|thm|lem|prop|cor|conj|rem|ex:<key>-<name>`; tables `tab:<key>-<name>`; figures `fig:<name>` (existing names) or `fig:<key>-<name>` (new) per FIGURES_INDEX_v2; equations `eq:<key>-<name>`.
- The labels in FINAL_OUTLINE_v2 are **canonical**: spelled exactly as given, never renamed, never reused for another object.
- You may add internal labels with your own key (equations, subsections, extra remarks, auxiliary lemmas `lem:<key>-…`); report them. Never create a new label with another unit's key.

### 5.2 Ownership is fixed by the registry, not by the prefix

The registry of FINAL_OUTLINE_v2 lists every canonical label under its **owner unit**. The owner writes the environment; every other unit cites it. `check_unit_v2.py` reads the owners from the registry (checks C1, C2).

### 5.3 Moved labels (binding: labels of existing statements are not renamed)

| family | v1 owner | v2 owner (expected; the registry decides) |
|---|---|---|
| QCD-basics labels of v1 Ch2 with prefix `prelim`: `def:prelim-qcd`, `def:prelim-feynman-rules`, `def:prelim-brst`, `lem:prelim-brst-nilpotent`, `thm:prelim-slavnov-taylor`, `def:prelim-msbar`, `prop:prelim-beta`, `prop:prelim-rg`, and (renormalization) `thm:prelim-composite-renorm`; section labels `sec:prelim-qcd`, `sec:prelim-brst`, `sec:prelim-renorm` | Ch2 `prelim` | **Ch2 `qcd`** |
| remaining `prelim` labels: `def:prelim-lightfront`, `lem:prelim-boost`, `def:prelim-wilson`, `prop:prelim-wilson-covariance`, `prop:prelim-wilson-rules`, `lem:prelim-eikonal-identity`, `def:prelim-gamma5`, `def:prelim-plus`, `lem:prelim-plus-expansion`, `def:prelim-mellin`, `lem:prelim-mellin`, `def:prelim-cut`, `thm:prelim-cutting-rules`, `rem:prelim-cutting-dr`, `prop:prelim-optical`, `prop:prelim-unitarity`, `ex:prelim-*`; section labels `sec:prelim-lightfront`, `sec:prelim-wilson`, `sec:prelim-distributions`, `sec:prelim-cuts` | Ch2 | **Ch3 `prelim`** |
| `lattice` labels (`def:lattice-quasi`, `prop:lattice-moments`, …, `sec:lattice-*`, `tab:lattice-*`, `fig:lattice-matching`) | Ch21 | **Ch22 `lamet`** |
| `summary` labels | Ch22 | **Ch25 `summary`** |
| all other v1 labels | v1 Ch$n$ ($n=2..20$) | same key, chapter number $n+1$ |

The section labels of the moved families are canonical too; FINAL_OUTLINE_v2 lists their owners. **Labels changed at the merge (no v1 label affected):** `rem:prelim-bphz-brst` (proposed by refdoc S14) is `rem:qcd-bphz-brst` (owner Ch2, MD11); `lem:appO-past-unitarity` was deleted (use the past-pointing case of Ch9 `lem:method-soft-unitarity`, MD10); new App O lemma `lem:appO-orientation` (the precise orientation lemma; Ch12 `lem:dy-poles-orientation` cites it). Figure labels move by first use as fixed in FIGURES_INDEX_v2 (`fig:prelim-feynman-rules` → Ch2; `fig:prelim-lightcone`, `fig:prelim-wilson-rules`, `fig:soft-eikonal` → Ch3; `fig:quasi-pdf`, `fig:lattice-matching` → Ch22). New statements of Ch2 use the key `qcd`, of Ch22 `lamet`, of Ch23 `yzliu`, of Ch24 `front`.

### 5.4 Equation labels are unit-internal

Other units cannot know your equation labels; any external `eq:` reference is treated as non-canonical. Cross-unit references always point to the **statement** (or section, figure, table) containing the formula: 「\cref{thm:dis-moments}中的矩关系」.

### 5.5 External labels

In a standalone compile, references to other units appear as "??"; this is allowed. Every external label you use must be canonical (in the registry) and listed in your report.

### 5.6 Definition ownership (each definition is written once, by its owner, and `\cref`'d elsewhere; at most one sentence of reminder)

| owner | definitions (v1 labels keep their names; v2 additions from refdoc S5–S49; frontier definitions per FINAL_OUTLINE_v2) |
|---|---|
| front | (none; notation table only) |
| Ch1 `intro` | `def:intro-hard-process`, `def:intro-factorization`, `def:intro-tags` (five tags, four qualifiers, grade propagation), `def:intro-MA` (umbrella names + dictionary to `asm:intro-*`), **`def:intro-error-types`**; assumptions `asm:intro-wightman`, `asm:intro-composite`, `asm:intro-np-ope`, `asm:intro-af-coeff`, `asm:intro-growth`, `asm:intro-bridge` |
| Ch2 `qcd` | `def:prelim-qcd`, `def:prelim-feynman-rules`, `def:prelim-brst`, `def:prelim-msbar`; new `def:qcd-*` of FINAL_OUTLINE_v2 (gauge group and representations, gauge-fixed generating functional / Faddeev–Popov, renormalization constants, running coupling and $\Lambda$, informal IR-safety notion — the **canonical** definition of IR safety remains `def:ir-safe` in Ch4) |
| Ch3 `prelim` | `def:prelim-lightfront`, `def:prelim-wilson`, `def:prelim-gamma5`, `def:prelim-plus`, `def:prelim-mellin`, `def:prelim-cut`; DR conventions of Ch3 (ε_UV/ε_IR, scaleless integrals) per FINAL_OUTLINE_v2 |
| Ch4 `ir` | `def:ir-landau-setup`, `def:ir-pinch-surface`, `def:ir-scalings`, `def:ir-glauber`, `def:ir-safe`, `def:ir-regions` |
| Ch5 `sudakov` | `def:sudakov-ff`, `def:sudakov-cusp` |
| Ch6 `ee` | `def:ee-R`, `def:ee-adler` |
| Ch7 `dis` | `def:dis-kinematics`, `def:dis-compton`, `def:dis-twist` |
| Ch8 `pdf` | `def:pdf-quark`, `def:pdf-antiquark`, `def:pdf-gluon`, `def:pdf-lightray`, `def:pdf-ff`, `def:pdf-polarized` |
| Ch9 `method` | `def:method-regions` (revised: per-line mode assignments), `def:method-collinear-approx`, `def:method-soft-approx` (idempotent-projector form), `def:method-subtraction`, **`def:method-power-suppressed`**, **`def:method-neighbourhoods`**, **`def:method-collins-conditions`** |
| Ch10 `disall` | `def:disall-breit` |
| Ch11 `coll` | `def:coll-sia`, `def:coll-g1`, `def:coll-transversity` |
| Ch12 `dy` | `def:dy-kin` |
| Ch13 `thr` | `def:thr-limit` |
| Ch14 `tmd` | `def:tmd-kin`, `def:tmd-unsub`, `def:tmd-soft`, `def:tmd-collins`, `def:tmd-etqs` |
| Ch15 `scet` | `def:scet-modes`, `def:scet-zero-bin` |
| Ch16 `jets` | `def:jets-algorithms` |
| Ch17 `smallx` | `def:smallx-regge` |
| Ch18 `break` | `def:break-generalized-tmd`, `def:break-diffraction`, `def:break-dpdf` |
| Ch19 `excl` | `def:excl-da`, `def:excl-gpd` |
| Ch20 `heavy` | `def:heavy-nrqcd` |
| Ch21 `power` | `def:power-borel` |
| Ch22 `lamet` | `def:lattice-quasi` (quasi-, pseudo-distributions, lattice cross sections), `def:lamet-schemes` (schemes incl. hybrid), `def:lamet-quasi-gpd`, and (MD9) `def:lamet-quasi-tmd`, `def:lamet-soft-offlc` (off-light-cone soft function), `def:lamet-reduced-soft`; frontier assumptions `asm:lamet-*` |
| Ch23 `yzliu` | `def:yzliu-hyperbolic-angle`, `def:yzliu-intrinsic-soft-lc` (intrinsic soft function $S_I$), `def:yzliu-exp-soft` (exponential-regulator soft factors), `def:yzliu-hl-jet` (heavy–light jet functions); the off-light-cone and reduced soft functions and the quasi-TMD are Ch22's (MD9); `asm:yzliu-*` |
| Ch24 `front` | `def:front-trap` (trapped contours / Landau points), `def:front-facets` (region facets), `def:front-endpoint` (endpoint refactorization); `asm:front-*` |
| Ch25 `summary` | none |
| App I | `def:appI-hvbm` |
| App M | **`def:appM-normal-product`**; `asm:appM-remainder`, `asm:appM-brst-ope`, `asm:appM-forward` |
| App N | the `def:appN-*` of FINAL_OUTLINE_v2 (integrand, meet closure, TMD and exclusive approximators, …); `asm:appN-contour`, `asm:appN-envelope`, `asm:appN-separation`, `asm:appN-collins`, `asm:appN-values`, `asm:appN-cutsum`, `asm:appN-ward-product`, `asm:appN-brst-nonlocal`, `asm:appN-uv`, `asm:appN-multren`, `asm:appN-ir-regulator`, `asm:appN-tmd`, `asm:appN-endpoint` |
| App O | the `def:appO-*` of FINAL_OUTLINE_v2 (light-cone time and intermediate states, orientation, windows, rewriting, deformation targets, …); `asm:appO-lcopt`, `asm:appO-envelope`, `asm:appO-mixing`, `asm:appO-deformation`, `asm:appO-rewritten-cs` |

Objects defined inside theorem statements are owned by that theorem: (H1)–(H5) by `thm:method-template` (Ch9); (CS1)–(CS3) by `def:method-collins-conditions` (Ch9); the soft factor of collinear factorization by `lem:method-soft-unitarity` (Ch9); the TMD soft factor by `def:tmd-soft` (Ch14).

---------------------------------------------------------------------------------------------------

## 6. Content obligations

### 6.1 Canonical statements

Every canonical statement of your unit in FINAL_OUTLINE_v2 appears with its label, type, Chinese title, tag and qualifier, the line of §4.4 item 6 (or the partonic remark), its precise content (formulas from VERIFIED_FORMULAS_v2), the `\uses` list (§4.5), the requested proof type with the literature locations given, and the VF IDs where relevant (in a `%` comment next to the formula: `% VF-DIS-7`).

### 6.2 Worked examples

Worked examples are in the text, not deferred. They show the computation step by step, with intermediate results checked against VERIFIED_FORMULAS_v2. Part I has quantitative targets (§7).

### 6.3 Promised appendix proofs (the chapters announce them; the appendix writers deliver)

| appendix | promised content |
|---|---|
| A | `lem:prelim-boost`, `lem:prelim-plus-expansion`, `lem:prelim-mellin`, the Fierz decomposition; the precise test-function class and the weak-convergence statement used in `cor:dis-weak-xspace` (S51) |
| B | `prop:prelim-wilson-rules`, `lem:prelim-eikonal-identity`, the one-loop cusp; the partial-exponentiation lemma of Ch23 if FINAL_OUTLINE_v2 places it here |
| C | DR integrals and phase spaces used in Ch6, Ch10, Ch12; the $d$-dimensional splitting kernels with the averaging conventions (S51) |
| D | `thm:ir-landau-alpha`, `thm:ir-landau-momentum`, `prop:ir-coleman-norton`; `sec:appD-alpha` (Feynman-parameter proof with caveats; details of `rem:ir-euclid-corners`) (S52) |
| E | `prop:ir-power-counting` (`prop:appE-degree`, boost-and-dimension proof); `rem:appE-actual-bound` (S52) |
| F | `prop:method-ward-one`, `prop:method-ward-tree`, outline of `lem:method-ward-multi`; telescoping example; Grammer–Yennie with its $i0$ (S52) |
| G | detailed one-loop calculations of Ch6, Ch7 (`prop:dis-c-oneloop`), Ch8, Ch10, Ch12, Ch14 |
| I | Larin scheme |
| J | `lem:prelim-brst-nilpotent`, `thm:prelim-slavnov-taylor` details, ghost cuts, `thm:prelim-composite-renorm` context; `lem:appJ-cut-hermiticity` (S53) |
| K | `rem:dis-uniqueness`, `rem:pdf-ns-plusminus` lemmas; `lem:appK-entire`, `lem:appK-markov` (S50) |
| L | `thm:pdf-moments-local` |
| M | full proofs of `prop:dis-ope-euclid` (location), `prop:dis-ope-gi`, `prop:dis-ope-forward`, `lem:dis-ope-segment`, `thm:dis-fixed-n`, `prop:dis-dispersion-np`, `prop:dis-low-moments`, `thm:dis-moments-np`, `cor:dis-weak-xspace`, `lem:dis-twist-classification`, `lem:dis-twist-chirality`, `prop:dis-chiral-suppression`, `prop:dis-ope-rg` (from uniqueness); the perturbative OPE machinery (`lem:appM-*`, `thm:appM-*`) — **X3 outcome [PENDING-VERIFY]** |
| N | `thm:appN-subtraction` and proofs of `lem:method-meets`, `lem:method-covering`, `prop:method-chains`, `lem:method-pairing`, `prop:method-product`, `cor:method-removing-eps`, `lem:method-i0-compat`, `lem:method-telescoping`, `lem:method-local-accuracy`, the rows of `tab:method-errors`; `prop:disall-two-routes`, `prop:disall-factorized-subtraction`, `thm:disall-renorm-compat`, `prop:appN-dy`, `prop:tmd-zero-bin-soft`(b), `prop:excl-soft-cancel`, `prop:appN-triangle-exact` — **X2 outcome [PENDING-VERIFY]** |
| O | `lem:appO-lcopt` … `thm:appO-main`, `cor:appO-interface`, `prop:appO-tmd`; `lem:appO-orientation` (Ch12 `lem:dy-poles-orientation` is its chapter statement); proofs of `prop:dy-eikonal-twogluon`, `prop:appO-past-wilson`; `tab:appO-checklist` — **X1 outcome [PENDING-VERIFY]** |
| P | generated register, status table, dependency graph (§6.13) |
| Q | verified literature errata (§6.13) — **[PENDING-VERIFY]** |

### 6.4 Formulas

1. Copy formulas only from VERIFIED_FORMULAS_v2. A formula with status **T** is accompanied in the text by 「（待核实）」 or, better, re-derived by the writer, who reports "writer-verified: VF-… (method)". Formulas with status V/VL/A may be used directly.
2. A formula you need that is not there: derive it, mark it "writer-derived" in the report and list the check made (limit, sum rule, numerical test, script path).
3. Literature formulas in other conventions are converted (rows 4, 8, 30, 31, 40, 44, 45 of §3 list the known traps) and the conversion is stated.

### 6.5 「本书新结果」 (refdoc S59, amended by the verification workflow)

1. Do not add theorems that are not in FINAL_OUTLINE_v2, except auxiliary lemmas needed for a full proof (label `lem:<key>-…`, report them).
2. The words 「本书新结果」 (and any equivalent claim of novelty: 「首次」「本书首次证明」「文献中未见」) may be printed **only** for a statement that FINAL_OUTLINE_v2 (after the verify patch) marks as new **and** that satisfies all of the following:
   1. a full derivation is printed in this book;
   2. **two independent confirmations** are recorded in `verify/` (two separate verification records with PASS, by independent verifiers, e.g. the two stages of the verification workflow), and the record paths are cited in the final report;
   3. a **literature check** (refs agent or verify workflow) found no prior source; if a prior source is found, it is cited and the marker is dropped (the result is then presented as a re-derivation, 「本书给出的推导」).
3. Until the patch, FINAL_OUTLINE_v2 uses the planning marker 「本书新结果（待文献核查）」 [PENDING-VERIFY]; it is never printed.
4. **Planning classification of the claimed new results** (spec v2.1; keyed to `verify/CLAIMS.md` N01–N29; all [PENDING-VERIFY] — the verify patch decides, starting from this table):

   | class | meaning | claims (labels, VF IDs) |
   |---|---|---|
   | K1 | candidate 「本书新结果」: printed with the marker only if item 2 is satisfied, otherwise as 「本书给出的推导」 with the prior source | N01 `prop:dy-eikonal-twogluon` (VF-REF-9, VF-REF-10, `fig:dy-two-gluon-exchange`); N02 the identification of Collins' geometric theorem with Gordan's alternative (`lem:appD-gordan`, VF-FRO-1); N03 the momentum-space Coleman–Norton corollary (VF-FRO-3; it inherits the preprint status of `Collins:2020euz`); N04 the moment reduction of the BRST classification for bilocal PDF operators (VF-FRO-15); N07 the exact $\gamma^0$ target-mass correction and its commutation with matching (VF-LAM-11); N08 the Fourier lemma and the endpoint dichotomy (VF-LAM-12); N09 tails, moments and convolution domain of the one-loop quasi-PDF (VF-LAM-9); N10 the analyticity strip and the truncation bound of the Fourier step (VF-LAM-17; the mode count itself is classical, `SlepianPollak1961`, `LandauWidom1980`); the proof extensions X1 (App O), X2 (App N), X3 (App M) |
   | K2 | candidate only if the literature check finds no prior source; default presentation 「本书给出的推导」 with attribution | N17 the entanglement colour test of TMD breaking (VF-GLA-10; compare `RogersMulders2010`, `CollinsQiu2007`, `Collins2007`); N18 the closed formula for the gluonic-pole strength (VF-GLA-6; compare `BacchettaBomhofMuldersPijlman2005`, `QiuVogelsangYuan2007`); N20 time-like vs space-like regulator lines, the $2\pi^2$ difference (VF-TMD-9); N21 the exact Isgur–Llewellyn Smith soft fractions (VF-EXC-14) |
   | K3 | sharpened explicit results, never marked new (refdoc S59) | N12 `prop:appN-triangle-exact`(c) (no logarithm at NLP; VF-REF-2, VF-REF-3); N13 `lem:appO-joint-localization` (VF-REF-12); N14(i) `lem:appJ-cut-hermiticity`; N15 `ex:appM-unreduced` (VF-REF-14) and the sharpness lesson of `rem:power-np-status` |
   | K4 | our derivation or proof of a published result: printed as 「本书给出的推导／证明」 next to the published source; never a novelty claim | N05 the one-loop quasi-PDF in the unphysical regions (VF-LAM-7 = `IzubuchiEtAl2018` App. B); N06 the one-loop check of the threshold factorization (VF-LAM-14; `Ji:2023pba`); N16 the Cauchy–Schwarz proof of $I_1(0)+I_2(0)<0$, which `Collins2007` states without proof (VF-GLA-8); N23 proofs of classical mathematics (cite the classical sources); N24 the route to $R_{e^+e^-}$ finiteness and the exact cutting identity (VF-EE-8); N25 the abelian Glauber toy and the "plus trap" (VF-DY-12, VF-DY-13); N26 the eikonal identity and the adiabatic regulator (VF-WL-2); N27 the distributional checks of the one-loop LaMET kernels (VF-LAM-8); N29 the cross-checks of Liu-programme formulas (VF-YZL-6, -7, -9, -10, -11, -12, -13) |
   | K5 | not printed as results | N11 (the Lean-style dependency graph of the LaMET matching theorem becomes the `\uses` structure of Ch22); N19 (auxiliary c_glauber results, novelty not claimed; VF-GLA-9, VF-GLA-11); N22 (prescription dependence of the $X_A$ model — an illustration; VF-BQ-3, VF-BQ-5); N28 (checked transcriptions; VF-FRO-7, -9, -10, -11, -12); N14(ii)–(iv) are verification items of X1 and X3 |

   A K1 or K2 statement printed before the patch follows §6.12 (comment with the claim ID, no marker).
5. **Corrections of the reference document** (CLAIMS R-S1 … R-m26) are never printed as corrections of that document (§6.10): the physics is printed in our words with the primary literature. R-OUR1 and R-OUR2 are corrections of our own spec v1 found by the refdoc readers (already applied).
6. Literature errata are **not** new results; they go to App Q (§6.13) once verified.

### 6.6 The box 「本章证明了什么／没有证明什么」 (refdoc S45.1; extended)

Required right after the first paragraph of **every chapter Ch2–Ch24** and of App M, N, O (not in Ch1, Ch25, App A–L, P, Q). Content: 5–8 lines, labels only, with tags; two run-in parts. Use exactly this frame (no macro exists):

```latex
\begin{tcolorbox}[enhanced,breakable,title=本章证明了什么／没有证明什么,fonttitle=\bfseries,
  colback=gray!3!white,colframe=gray!55!black,boxrule=0.6pt,arc=2pt,
  left=5pt,right=5pt,top=3pt,bottom=3pt,before skip=6pt,after skip=6pt]
\textbf{证明了：}\cref{thm:...}（\tagR，$R_{\mathrm{PT}}$）；\cref{prop:...}（\tagR，$R_{\mathrm{cond}}$，前提\cref{asm:...}）；……\par
\textbf{给出全阶论证：}\cref{thm:...}（\tagA；瓶颈\cref{asm:...}）……\par
\textbf{没有证明：}……（\cref{asm:...}，\cref{conj:...}）；……
\end{tcolorbox}
```
For appendices the title is 「本附录证明了什么／没有证明什么」. Pedagogical Ch2 may phrase the parts as 「本章给出完整推导的」 and 「本章只陈述、留待后文或文献的」.

### 6.7 Correspondence tables (refdoc S45.2)

Every chapter whose precise versions live in App M/N/O ends with `tab:<key>-correspondence`: chapter statement | precise version (appendix label) | what differs (assumptions, error type). Required for Ch7 `dis` (↔ App M), Ch9 `method` and Ch10 `disall` (↔ App N), Ch12 `dy` (↔ App O, App N), Ch14 `tmd` (↔ App N, App O), Ch18 `break` (↔ App O, measurement criterion), Ch19 `excl` (↔ App N §N.6). Labels as given in FINAL_OUTLINE_v2.

### 6.8 Honesty checklist: critic items and misconceptions M1–M35

Address explicitly, in text or in a remark (or in the misconception box of the unit), the items allocated to your unit. Texts: C1–C15, O1–O21, M1–M28 in `research/critic/REVIEW.md` §3.2, §2, §7 (frozen); M29–M35 below (refdoc S57).

| unit | critic C | critic O | misconceptions (M#) and other items |
|---|---|---|---|
| Ch1 | C1, C2, C3 (preview) | O1, O2 | misconception box of 14: M28, M1, M2, M3, M4, M7, M8, M9, M10, M15, M18, M24, **M32, M35** (each with correction and forward reference) |
| Ch2 `qcd` | C14 (preview) | — | 「维数正规化消除红外发散」 (it regulates them; pointer to `prop:pdf-partonic-dr`); M28 (preview: QCD is not constructed as a mathematical QFT, so "[R]" is perturbative) |
| Ch3 `prelim` | — | — | M24 preview (scaleless integrals: $\varepsilon_{\rm UV}$ vs $\varepsilon_{\rm IR}$); "a single cut graph is unitary" (no: only the sum over cuts) |
| Ch4 `ir` | C5, C15 | O11, O12 | M8, M9, M19, M20, **M29** |
| Ch5 `sudakov` | — | O11 (massive exchange needs analytic regulators) | M16, M21 (preview) |
| Ch6 `ee` | — | O3, O21 (part) | M27; "the $O(\alpha_s^2)$ singlet term" (Furry) |
| Ch7 `dis` | C4, C15 | O4, O5, O6, O7 | M3, M4, M5, M6, **M34**; Adler sum rule; Bloom–Gilman |
| Ch8 `pdf` | C1, C2, C3, C13, C14 | O6, O8, O9 | M2, M6, M11, M23, M24; "PDFs are defined by DIS" (C1) |
| Ch9 `method` | C2, C7, C14 | O10, O13 | M15, M24, M25, **M31, M35** |
| Ch10 `disall` | — | O7 | M4, M25, M26 |
| Ch11 `coll` | — | — | Christ–Lee; M23; "diffractive PDFs are universal" |
| Ch12 `dy` | C8, C11 | O13, O14 | M7, M25, **M30, M31, M32, M33**; "the soft factor is 1 for $q_T$-differential DY" |
| Ch13 `thr` | — | — | prescriptions are not theorems |
| Ch14 `tmd` | C8, C9, C10 | O15 | M12, M13, M14, M15, M16, M17, **M33** |
| Ch15 `scet` | C6 | — | M18, M19 |
| Ch16 `jets` | — | — | M8, M9, M10 |
| Ch17 `smallx` | — | — | non-uniformity at small $x$ |
| Ch18 `break` | C8 | O16, O17 | M7, M21; "diffractive PDFs are universal" |
| Ch19 `excl` | — | O18 | — |
| Ch20 `heavy` | — | O19 | — |
| Ch21 `power` | C11 | O20, O21 | M10, M22, M28 |
| Ch22 `lamet` | C12 | — | M17 (lattice CS kernel is non-perturbative input); "lattice computes PDFs directly" (critic §7 candidate); "LaMET is proven non-perturbatively" (no: [C], §6.9) |
| Ch23 `yzliu` | C9, C10 | — | M15, M16 (rapidity divergences are physical: Euclidean realizations of the soft factor) |
| Ch24 `front` | C5 | O11, O12 | M2 (positivity status), M19, M20, M21 |
| Ch25 `summary` | all (summary) | — | — |
| App M | C4 | O4, O5 | M34 (precise form) |
| App N | C5, C7 | O10 | M35 (precise form) |
| App O | C8 | O13 | M30, M31, M32, M33 (precise forms) |

**M29–M35 (texts; REVIEW.md is frozen, so they are given here).**

| M# | misconception (中文) | correct statement | unit |
|---|---|---|---|
| M29 | 「欧氏区没有钳夹，所以欧氏 Green 函数红外有限」 | zero-momentum massless lines always solve the Landau equations; finiteness follows from IR power counting | Ch4 (`rem:ir-euclid-corners`) |
| M30 | 「NNLO/N3LO 的 DY 与数据一致，说明 Glauber 相消已被检验」 | partonic fixed-order results contain no hadron spectators; they test active-parton contributions only | Ch12 (`rem:dy-nnlo-not-glauber`) |
| M31 | 「把 $k^-$ 围道推到 $|k^-|\sim|k_T|$ 就离开了 Glauber 区」 | a one-component deformation stays in $G_\delta$; both components must move along $e_G$ | Ch9 (`rem:method-two-component`), Ch12 |
| M32 | 「非阿贝尔双 Glauber 交换留下非幺正残差」 | an artefact of a strict truncation; the exact graphs give ${\rm Re}\,p_{\rm opp}=0$ | Ch12 (`prop:dy-eikonal-twogluon`) |
| M33 | 「单个割图中的软 Wilson 线已经是过去指向的」 | a single cut graph gives the future-pointing line; past-pointing only after the one-sided rewriting | Ch12, Ch14 (`ex:dy-future-vs-past`) |
| M34 | 「欧氏 OPE 代入、收缩、比较系数即得强子结构函数的矩」 | the OPE informs only on a segment of length $O(M/Q)$; positivity and a dispersion relation are needed; $n<n_0$ needs the growth condition | Ch7 (`thm:dis-fixed-n`) |
| M35 | 「减除定理可以逐项归纳证明」 | single chain terms need not be integrable; only grouped expressions are suppressed | Ch9 (`ex:method-naive-induction`) |

### 6.9 Over-claims to avoid (v1 list + refdoc S58 + frontier)

From v1 (each has occurred in drafts or in the literature):
- 「Rothstein–Stewart (2016) 证明了 Drell–Yan 因子化」 — false: RS state that the S–S cancellation "taken alone is far from a proof".
- 「软因子等于 1」 without 「对共线单举截面」.
- 「Glauber 胶子在单举截面中总是相消」 — write: inclusive in the spectators, and the measurement must commute with the light-cone evolution (C8; `prop:break-measurement`).
- 「SCET 独立于区域分析证明了因子化」 (C6, M18); SCET proofs are not more rigorous than Collins'; they are complementary.
- 「Collins (2011) 证明了非定域算符的 BRST 分类」 — false: assumed (§11.3.2).
- 「偶极子公式对所有阶精确」 — fails at three loops.
- 「$\overline{\rm MS}$ PDF 是正的」 / 「在所有标度上非负」 — false (Yukawa counterexample, `CollinsRogersSato2022`); positivity above a non-perturbative scale is [P]/[C] (`conj:pdf-positivity`).
- 「Soffer 不等式对 $\overline{\rm MS}$ 分布成立」 as a theorem — only its preservation by LO evolution (`prop:coll-soffer`).
- 「Sivers 符号反转已被实验确认」 — consistent, not decisive.
- 「$B\to\pi\pi$ 的 QCD 因子化已全阶证明」 — [P]. 「BBNS 只在 $O(\alpha_s)$ 成立」 — understates: the LP formula is [P] with all-order arguments.
- 「NRQCD 产生的因子化已证明」 — [C]. 「NRQCD 衰变因子化与 OPE 同样严格」 — false (local duality needed).
- 「格点检验了因子化」 (C12) — lattice supplies matrix elements.
- 「DY 的幂次修正是 $1/Q^2$」 as a theorem — [C].
- Attributing to RS 2016 an $e^+e^-$-specific statement; citing `SenIndumathiChoudhury2019` as a QCD paper (only next to `GrammerYennie1973`).
- 「衍射 DIS 只有一个强子，因而没有 Glauber 问题」 — wrong argument (`thm:break-ddis`).
- 「区域 = Newton 多面体的下表面」 in Minkowski kinematics — false at three loops (`Gardi:2024axt`).
- 「推力的领头对数重求和在微扰论中已严格证明」 — inherits [A].

From refdoc S58:
- 「欧氏区无 Landau 奇点」 (M29).
- 「非阿贝尔双 Glauber 残差是 DY 因子化的开放障碍」 (M32).
- 「纯规范论证证明了非阿贝尔 Wilson 线结构」 — heuristic whose step 2 is the [A] Ward identity; it cannot fix the Wilson-line direction.
- 「间隙截面的因子化已被证明破坏」 — amplitude-level violation is [V]; PDF factorization of gap cross sections is [C] with restoration evidence (`Becher:2024kmk`).
- 「NQS 的规范完备 Wilson 线在 NNLO 不改变结果」 — they are necessary at NNLO.
- 「Gaunt (2014) 证明了强子 $E_T$ 的因子化破坏」 without Schwartz–Yan–Zhu (`Schwartz:2018obd`).
- 「DGLAP 与 OPE 重整化群在所有阶以单一核等价」 — $P^\pm_{\rm NS}$ differ beyond LO.
- 「横向光子失效源于 $\int\phi/z^2$ 型发散」 — logarithmic WW divergence ($g_\perp^{(v)}(0)\ne0$) and double poles.
- 「前向在壳部分子矩阵元直接给出 Wilson 系数，无需额外步骤」 — exceptional momenta; `prop:dis-ope-forward` needs `asm:appM-forward`.
- 「Glauber 相消的方法是 Collins (2011) 首创的光锥序处理」 — credit Aybat–Sterman 2009 (`AybatSterman2009`) and `Diehl:2015bca`.

Frontier (new in v2):
- 「LaMET 原理已被非微扰地证明」 — the non-perturbative principle is [C]; the perturbative matching theorems are [A]; one-/two-loop kernels are [R, R_PT] at that order.
- 「准 PDF 匹配定理对强子严格成立」 — the hadronic statement rests on uniformity in Ioffe time and large-distance control (`asm:lamet-*`), [C].
- 「准 TMD 因子化已严格证明」 / 「时序无关性定理是严格的」 — [A] (the latter conditional on the perturbative Wightman structure of DR correlators).
- 「指数衰减定理在 QCD 中成立」 — proven under Wightman-type axioms with a gap (R_cond); for QCD Wilson-line correlators [A]/[C].
- 「二维 Gross–Neveu 模型的结果证明了 QCD 的扭度展开收敛」 — model result; as a QCD statement [P]; momentum-space power expansions can diverge (O(N) model).
- 「Collins (2020) 的 Landau 定理已正式发表」 — arXiv preprint only (as of 2026-10-10); sign condition required.
- 「SCET 的 Glauber 拉氏量证明了强子对撞中的因子化」 — RS: far from a proof; SYZ contradicts RS claim (v) for single-scale observables.
- 「NLP TMD 因子化中的 Glauber 相消已证明」 — assumed everywhere ([C]).
- 「BK/JIMWLK 是 QCD 的领头幂次定理」 — results within the eikonal (Regge) expansion at fixed logarithmic accuracy.
- 「格点直接计算了 $x$ 依赖」 — the Fourier/inverse problem needs decay information; with data up to $\lambda_L$ only $\approx2\lambda_L/\pi$ modes are determined (VF-LAM-17).
- Printing a frontier report's "UNVERIFIED" item, a Chinese name for Yizhuang Liu, or career details.

Attribution traps (spec v2.1, from `verify/CLAIMS.md` A01–A28; the full rules are in REFS_NOTES_v2 §1.5 and bind until the verify patch):
- 「Ji、Liu、Liu、Zhang、Zhao 等（NPB 964）」 — wrong author list (A01): `Ji:2020brr` is Ji, Yizhuang Liu, Schäfer, Wang, Yang, Zhang, Zhao; "Ji, Liu, Liu, Zhang, Zhao" is the RMP `JiEtAl2021`.
- Priority words (「首次」「第一个」) for Liu-programme results before verification (A03); in particular 「LPC（2020）首次在格点上提取了 Collins–Soper 核」 — `Shanahan:2020zxr` is earlier.
- 「IJJSZ 与 Ma–Qiu 对强子态证明了准 PDF 匹配」 — the RMP states the proof only for perturbative free-quark states; 「Ji（2014）证明了匹配可以逐阶证明」 — asserted without proof (A05).
- 「类空 Wilson 线算符的乘法可重整性已由 BPHZ 完整证明」 — degree counting and an asserted space-like extension of the auxiliary-field argument: [A] (A05, A26).
- 「两圈阈值因子化是严格的」 — two constants were fitted to the NNLO singular terms; the two-loop values are [P] (A26).
- 「Beneke–Smirnov（1998）给出了离壳 Sudakov 形状因子的区域分析」 — the example is in `BecherBroggioFerroglia2015` §2.2 (massive exchange: `Jantzen2011` §6); BS 1998 introduced the method for the threshold expansion (A10).
- 「Cheng–Wu 给出了旁观者 Glauber 相位的相消」 — cite `AybatSterman2009` eq. (14) and `RothsteinStewart2016` (A11).
- 「Catani–de Florian–Rodrigo 证明了类空劈裂中的相消」 — they show that $P^{(2)}$ is not factorized (A20).
- PRL 84 (2000) 2589 for hard pseudoscalar production and the pion pole in $\tilde E$ — wrong paper, use `Frankfurt:1999fp` (A21); PRD 66 (2002) 054005 for SCET endpoint singularities — use `Bauer:2002aj` (A22).
- 「文献中没有……」 without the date and basis of the search (A06).
- 「$u$ 夸克的 Sivers 函数为负」 without a fit citation (A19); 「Sivers 符号反转已被确认」 (A27).

### 6.10 The reference document (refdoc S62)

`factorization_qcd-2.pdf` is an unpublished text of unknown authorship. It is **not cited, not quoted, not named**, and its figures are not copied. Every adopted construction is re-derived in our conventions and attributed to the primary literature (Collins 2011; Collins–Soper–Sterman; Aybat–Sterman; Zimmermann; Joglekar–Lee; …) or presented as our own derivation. Its numbering (Thm C.50, Ass. E.33, …) never appears. Formulas taken from the reader notes are checked against the page images (`refdoc/work_R*/png*`), never against `pdftotext` output (which detaches minus signs). Its errors (refdoc §2, ERR-…) are never copied; where our text treats the same topic, the "correct version" column of refdoc §2 is binding unless VERIFIED_FORMULAS_v2 says otherwise. Its errors do **not** go into App Q (App Q is about published literature).

### 6.11 Frontier chapters (Ch22–Ch24): additional rules

1. **Format.** For each result: precise statement in our conventions (rows 40–46 of §3); hypotheses as `asm:` labels or local numbered items (§4.4 item 4); proof architecture (what is proven, what is assumed, which steps are sketched in the source); tag per §4.3 item 4 with justification; relation to the CSS/Collins/SCET results of Parts II–VI (`\cref`); evidence (fixed-order checks, models, lattice — evidence, never proof).
2. **Reading depth.** Attribute to a paper only what the frontier report documents as read (*(read)*, [txt], "read in full"). Claims documented only at abstract level are introduced with 「据该文摘要」 or hedged; *(title)* and *(recall)* items are not used for content. REFS_NOTES_v2 §4 lists the recorded depth of every new key.
3. **Preprints.** arXiv-only items (REFS_NOTES_v2 §4, column "preprint") are marked 「（预印本）」 at first citation in a unit, and in every status paragraph that relies on them.
4. **"This work" results** of the frontier agents are our derivations, not literature: they follow §6.5 (candidates for 「本书新结果」, [PENDING-VERIFY]) and need the scripts of the frontier directories cited in the report.
5. **Ownership between Ch22 and Ch23** (binding as fixed in FINAL_OUTLINE_v2, MD9): Ch22 owns the LaMET principle, the collinear quasi-/pseudo-distribution theory (definitions, support, renormalization of straight space-like Wilson-line operators, schemes incl. hybrid, the matching theorems with hypotheses, one-/two-loop kernels, target-mass and power corrections, linear renormalons/LRR, LaMET vs SDF, the Fourier step incl. the exponential-decay theorem it needs, quasi-GPD/DA), the absorbed v1 `lattice` material, the lattice operator geometries, **and the quasi-TMD factorization theorem (`thm:lamet-quasi-tmd`), the off-light-cone and reduced soft functions as definitions, the lattice Collins–Soper kernel (`prop:lattice-cs-kernel`, a moved v1 label) and TMD ratios** (required by the no-forward-edge rule, since `prop:lattice-cs-kernel` uses the quasi-TMD theorem); Ch23 owns the rest of the TMD side (Euclidean soft functions as HQET form factors, $S_I$, analyticity and time ordering, rapidity-divergence factorization, Liu's Collins-style proof route of the quasi-TMD theorem `prop:yzliu-qtmd-powercount`, the hard kernel, LFWFs, meson form factor, DY in quasi-TMDs, Sivers ratios), the heavy–light Sudakov kernel and the threshold factorization of the quasi-PDF kernel, its renormalons, and the exactly solvable models. Ch22 may state forward pointers to Ch23 in text, never as dependencies. Ch24 owns all other frontier items (OTHERS.md): Landau/Gordan/Coleman–Norton theorems, rigorous OPE results, method of regions and hidden regions, Glauber EFT and SLL/factorization restoration, NLP endpoint factorization, NLP TMD, positivity debate, BRST non-local gap, small $x$, DPS, NGL/jets, quarkonium updates, QED/EW.
6. **Literature problems** found by the frontier agents (LAMET §0.3; YZLIU §4.1) are printed only after verification (App Q, §6.13); before that, use the correct form silently with a `%` comment and report it.
7. **Slips inside the frontier reports** (not literature errata; never print them): (a) LAMET §1.1 writes $L_z$ for the coordinate logarithm, its threshold section (like Liu et al. and JLS) for $\ln(\zeta_z/\mu^2)$ — use $L_z$ and $L_\zeta$ of row 42; (b) YZLIU §3.A3 writes the complex Lorentz map as $\Lambda(t,z)=(it,iz)$; the correct map is $(iz,it)$, as in YZLIU §3.A6, §6.3 (VF-YZL-12); (c) OTHERS §7 reports the negative region of the Yukawa-model PDF at $\mu=0.8$ GeV as $[0.28,0.98]$ from a grid; the exact statement is $\xi>0.264$ up to $\xi=1$ (VF-FRO-10). Copy formulas and numbers from VERIFIED_FORMULAS_v2, not from the reports.

### 6.12 [PENDING-VERIFY] protocol

FINAL_OUTLINE_v2 marks with [PENDING-VERIFY] every statement or wording whose final form depends on `verify/` (App M/N/O content affected by X1–X3; 「本书新结果」 candidates; App Q; errata of §3 rows 43). Writers normally write after the patch. If a unit must be written before: write the planned statement with a tag **not stronger** than the outline's planning tag (and, where the outline names a fallback tag — e.g. `prop:yzliu-gpd-oneloop` without re-derivation, `prop:front-commuting` without a reproduced proof — the fallback tag unless the condition is met; `prop:front-brst-bilocal` has planning tag [A], upgraded to [R, R_PT] only by the patch, MD7), put the comment `% PENDING-VERIFY: <label> <claim ID of verify/CLAIMS.md (E…, N…, A…) or X1/X2/X3>` on the line before the environment (the patch looks up every such comment), print no marker and no novelty claim, and list every such place in the final report (§13 item 9). FINAL_OUTLINE_v2 §0.10 is the merged register of all pending items (core, App M/N/O slots X1–X3, Part VII lists, and the stage-1 notes available at the merge, which do not end the pending status). The verification records will live under `verify/` (the proof-extension work started in `verify/extend/`, e.g. `verify/extend/X2-subtraction/`, at 17:45 on 2026-10-10); the patch cites their paths.

### 6.13 App P and App Q

**App P (generated + introduction).** A writer writes `sec:appP-intro` (≈2 pp): what the blueprint is (Lean-blueprint analogy), how to read the tables and the graph, the tag/qualifier/assumption system in one page, the grade-propagation rule (§4.6), the error types (§4.7), the legend of `fig:appP-dependency`. The integrator's generator reads all unit files and produces: `tab:appP-register` (label | owner | content one line | status tag | used by | upgrade path), `tab:appP-status` (label | type | tag | qualifier | premises | error type of the weakest step), `tab:appP-uses` (the dependency list), `fig:appP-dependency` and the per-part graphs `fig:appP-dependency-b` … `-h` (main theorems per part, at most 60 nodes; template in FIGURES_INDEX_v2 §4.9). Generator checks: §4.6 items 5–6 (incl. named gaps, C-P17); mismatches go back to the writers. **Typesetting (MD12):** the generated longtables need `longtable`, which the integrator loads in the master driver (`\usepackage{longtable}` after `\input{preamble_fact.tex}`); `common/preamble_fact.tex` is not changed and unit writers never use `longtable` (§8 item 6). Budget 10 pp with the compaction levels of FINAL_OUTLINE_v2 App P §P.7.

**App Q (verified literature errata).** Written after `verify/` completes. It contains **only** items confirmed by the verification workflow (two independent confirmations recorded in `verify/`), each as a row: ID | source (bib key + equation/section) | as printed | correct form (our conventions) | verification (verify/ record paths; independent check) | status in later literature (corrected by the authors / not corrected) | where the book relies on it. Not included: the reference document's errors (§6.10); authors' own published errata that we merely use (cite them where used); disputes between groups (those belong in status paragraphs). **Candidates, keyed to `verify/CLAIMS.md` E01–E36 (spec v2.1; all [PENDING-VERIFY]).** **Q1 — App Q candidates:** E01 the hybrid-kernel $\delta$ term (`Ji:2020brr`, `JiEtAl2021`; correct form in `Su:2022fiu`; first corrected in print by Chou–Chen, PRD 106 (2022) 014507 — 文献待补; an erratum, not a new result); E02 the CS exponent factor $\frac12$ (`Ji:2019ewn`, `JiEtAl2021`, `Liu:2022nnk`; **not** the journal version of `Ji:2021znw`, which is correct — only its arXiv v1 lacks the $\frac12$; stage 1); E03 `Braun:2018brg` eq. (cR); E04 the inconsistent sign of $g$ between the two links of `IzubuchiEtAl2018` (minor, no effect at $O(g^2)$); E08 the two-loop $\Gamma_S$ sign; E09 the RGE signs of `JiEtAl2021` eqs. (205)–(206); E11 the $L_b^2$ coefficient of $\ln S_I$; E13 "edge of the wedge" for Bargmann–Hall–Wightman in `Liu:2022nnk`; E17 the factor 2 in `AybatRogers2011` eq. (3); E18 the spurious factor in `Collins2007` eq. (10) (preprint); E20 the $i\epsilon$ of `Ji1997a` eq. (15) (arXiv v1; check the PRL); E21 the "$9/\tau$" of `Mankiewicz:1999tt`; E23 the spurious $C_F$ in `BecherSchwartz2008` App. A (arXiv; check the journal version); E25 the ghost-term invariance statement of `BauerPirjolStewart2002`; E26 "$m_M$" for $m_B$ in `BenekeEtAl2001`, `BenekeNeubert2003`; E28 and E32 are **not** App Q items after stage 1 (E28: the $\ln2\epsilon$ form is SW's own result, no printed source of the "common" variant — convention remark only; E32: refuted as an erratum, no printed source of the variant; `verify/claims/batch_E25_s1.md`, `batch_E31_s1.md`; the patch confirms). **Q2 — corrected by the authors or superseded by the same group** (cite the corrected version where used; App Q lists them only if the patch so decides): E06, E10, E12, E27, E29, E30, E31. **Q3 — not App Q** (proof gaps, disputes between groups, convention hazards, errors reported by others: status paragraphs and remarks, with attribution): E05, E07, E14, E15, E16, E22, E24, E34, E35, E36. **Never printed:** E19 (withdrawn). **Rule E33:** for every cited paper with a published erratum, use the corrected version. The full table (sources, corrected forms, VF IDs, units) is REFS_NOTES_v2 §3.5.

---------------------------------------------------------------------------------------------------

## 7. Readability rules for Part I (REQUIREMENTS 3e; binding for Ch1–Ch5, recommended everywhere)

The user asked that the book start, like the Furry monograph (`furry_qcd.tex`), from the basics and move gradually to the deep material. In Part I:

1. **Start from basics.** Each chapter opens with a physical or mathematical question, answered informally in one paragraph, before the first definition. Ch2 begins with the gauge principle (from QED to SU(3)), not with the Lagrangian as a given.
2. **Define everything before use.** Every symbol, convention and term is defined (or `\cref`'d to its definition) before its first use; no forward reference is ever used as a step; acronyms are spelled out at first use; each chapter ends with 「本章小结」 (one paragraph) and Ch2–Ch3 with a short 「记号速查」 table of the symbols introduced (it may be a `table` float).
3. **Many worked examples.** Minimum numbers of `example` environments (each a complete computation, step by step, with the intermediate results checked against VERIFIED_FORMULAS_v2): Ch2 ≥ 8, Ch3 ≥ 5, Ch4 ≥ 5, Ch5 ≥ 4 (FINAL_OUTLINE_v2 lists the canonical ones; add the rest as `ex:<key>-…` and report them). Suggested Ch2 examples: gauge covariance of $D_\mu$ and $G_{\mu\nu}$ (VF-QCD-2); SU(N) colour algebra and the Fierz identity (VF-QCD-1); the Faddeev–Popov determinant at lowest order / the ghost propagator; tree-level $q\bar q\to gg$ with physical vs ghost-subtracted polarization sums (VF-WL-9); the one-loop gluon self-energy and $Z_3$ (VF-PDF-14, VF-QCD-4); $\beta_0$ from $Z_g$ in four Slavnov–Taylor-equivalent ways (VF-QCD-4); solving the RG equation and the running coupling at one and two loops with numbers (VF-QCD-6/7); the real-virtual cancellation in $e^+e^-\to q\bar q(g)$ and the Sterman–Weinberg cross section as the first IR-safe observable (VF-EE-5/6/12).
4. **Derivations shown.** No 「容易证明」「可以证明」 without the computation or a precise citation with location; intermediate steps of multi-line algebra are printed.
5. **Pedagogical format of Ch2.** About 40 % motivation and explanation, 35 % definitions, statements and proofs, 25 % worked examples; the rigour vocabulary (tags, `\uses`) is used from the start, but the first section explains it in plain words with a forward pointer to `def:intro-tags`.
6. **Figures for orientation.** Ch2 has at least four figures (FIGURES_INDEX_v2 §4.1), every other Part I chapter at least two.
7. **Pointers forward.** Each Part I chapter ends with a paragraph 「这些工具在后文的用途」 listing, with `\cref`, where each tool is used later (forward pointers are allowed in running text).

---------------------------------------------------------------------------------------------------

## 8. Figures

`FIGURES_INDEX_v2.md` is binding. In summary:
1. **Existing figures** (`research/tikz1/figures1.tex`, `research/tikz2/figures2.tex`, `research/tikz3/figures3.tex`; **all three are final**): the owner copies the whole block from `%%% BEGIN fig:<name>` to `%%% END fig:<name>` verbatim (coordinates, styles, caption, label). A caption that seems wrong is kept and reported.
2. **New figures** (required/optional, with drawing descriptions, owners, caption drafts): plain TikZ or pgfplots with the preamble styles only; wrapped in `%%% BEGIN fig:<label>` / `%%% END fig:<label>`; width ≤ `\textwidth`; light colours for greyscale print; formulas and numbers only from VERIFIED_FORMULAS_v2 (pgfplots curves are computed from the VF formulas or from the inline coordinate tables given in FIGURES_INDEX_v2).
3. **Ownership = first use** (with the v2 chapter order); later units refer back with `\cref`. Captions of existing figures that use $n,\bar n$ outside Ch15 get the one-sentence conversion to $n_A,n_B$ in the text at the first reference (FIGURES_INDEX_v2 §1 notes).
4. **Placeholder protocol** (FIGURES_INDEX_v2 §0 rule 4) for a missing figure; report it.
5. **Inspection**: render every figure page as PNG and look at it before submitting (§10).
6. **Floats**: `[htbp]`; caption self-contained, Chinese, 1–4 sentences, stating the conventions that matter (directions, $\pm i0$, which subgraph is which). Tables: `table` + `tabular`/`tabularx` with `booktabs` (`longtable` is not loaded for unit writers — the only exception is the integrator's generated App P, §6.13; split long tables into floats with 「（续）」 captions; no vertical rules). `placeins` with `[section]` keeps floats inside their section.

---------------------------------------------------------------------------------------------------

## 9. Citations

1. **Bibliography.** Cite only keys present in `spec_v2/refs_merged_v2.bib` (1003 entries in spec v2.1; BibTeX `unsrt`: 0 errors, 0 warnings; XeLaTeX with the preamble and `\nocite{*}`: 0 errors, 0 missing glyphs, 0 overfull boxes — `checks/bibtest/SUMMARY.txt`). All 646 v1 keys are unchanged (spec v2.1 format fixes only: two internal remarks removed from printed `note` fields, eight legacy all-caps titles replaced by the published titles, numeric `month` fields written as BibTeX month macros; REFS_NOTES_v2 §0 rule 6, §1.2).
2. **Aliases.** Look up survey labels, frontier texkeys and agent keys in `key_aliases_v2.tsv` (alias → merged key → origin) and use the merged key; e.g. `Izubuchi:2018srq` → `IzubuchiEtAl2018`, `Collins:2011zzd` → `Collins2011` (first row wins; the 2023 OA reissue is `Collins2023`, not a new edition, but its pagination was never compared with 2011 — quote page, section and equation numbers from `Collins2011`). The alias-replacement script of v1 works unchanged with the v2 file name.
3. **Missing references.** Never cite a key that is not in the bib. Write the claim with 「（文献待补：<author year, journal>）」 and list it in the report.
4. **Syntax.** `\cite` attached without space: 「文献\cite{Collins2011}」「（见\cite{CollinsSoperSterman1989}）」. Locations: `\cite[第~14.4~节]{Collins2011}`, `\cite[式~(64)]{Sterman:1995fz}`, `\cite[第~112~页]{EdenEtAl1966}`, `\cite[式~(9.25)]{ParticleDataGroup:2024cfk}`.
5. **What a citation may support.** Attribute to a paper only what REFS_NOTES_v2, REFS_NOTES (v1, for v1 keys), `research/survey/SURVEY.md` (markers [txt]/[abs]/[bib]) or the frontier reports document for it (§6.11 item 2). Statements marked "(recall)" or "(verify)" in the sources are hedged or re-checked. Direct English quotations only where verified, in 「“…”」 with location, followed by a Chinese paraphrase.
6. **Known warnings**: REFS_NOTES_v2 §1 (binding), including the attribution rules keyed to `verify/CLAIMS.md` A01–A28 (§1.5). Examples: `Collins2023` = OA reissue of `Collins2011`; `QiuSterman1992` is about direct photons (pion paper `Qiu:1998ia`); `SenIndumathiChoudhury2019` only next to `GrammerYennie1973`; preprints (`Collins2007`, `Collins:2020euz`, `Beneke:2026miy`, `Ji:2026vir`, `Su:2026eta`, …) are said to be preprints; `Ji:2022ezo` has a published title different from its arXiv title; `LatticeParton:2020uhz` is the PRL (INSPIRE's merged PoS DOI was corrected). **Alias trap:** `Radyushkin1996` in the c_ee snippets is a JINR paper that is not in the bib, while the alias table maps the survey label of the same name to `Radyushkin:1996nd` (DVCS) — remove the c_ee citation before running the alias script (REFS_NOTES_v2 §0).
7. **Citation density.** Every [A], [P], [C] or [V] statement cites at least one primary source and one location of the gap. Every [R] statement that is not proved in full cites the source of the proof.
8. **Never** cite or quote the reference document (§6.10).

---------------------------------------------------------------------------------------------------

## 10. Compile and quality assurance (mandatory before submission)

1. **Test directory.** Work in a scratch directory of your own (never in `spec_v2/`, `spec/`, `research/`, `frontier/`, `refdoc/`, `verify/`). Copy into it `common/preamble_fact.tex`, `spec_v2/refs_merged_v2.bib`, `spec_v2/FINAL_OUTLINE_v2.md`, `spec_v2/checks/check_unit_v2.py` and your unit file. Use relative paths in `\input` (the project path contains a space).
2. **Driver** `test_<key>.tex`:
   ```latex
   \input{preamble_fact.tex}
   \begin{document}
   % \appendix        % uncomment for appendix files
   \input{ch07_dis.tex}
   \bibliographystyle{unsrt}
   \bibliography{refs_merged_v2}
   \end{document}
   ```
3. **Build.** `xelatex -interaction=nonstopmode test_<key>.tex && bibtex test_<key> && xelatex -interaction=nonstopmode test_<key>.tex && xelatex -interaction=nonstopmode test_<key>.tex`.
4. **Log checks** (each must pass):
   - `grep -c "LaTeX Error\|Undefined control sequence\|Emergency stop" test_<key>.log` → **0**;
   - `grep "Missing character" test_<key>.log` → none (replace the offending character, e.g. U+202F);
   - `grep "Overfull \\\\hbox" test_<key>.log` → none above 1 pt (reword or break displays; never `\sloppy` for the whole unit);
   - `grep "Citation .* undefined" test_<key>.log` → none;
   - `grep "multiply defined" test_<key>.log` → none;
   - `grep "Reference .* undefined" test_<key>.log` → only labels of other units (list them);
   - `test_<key>.blg` → no warnings for the entries you cite.
5. **Renders.** Every page with a figure, a table, a box (§6.6) or a long display: `pdftoppm -r 110 -png -f N -l N test_<key>.pdf pg`; look at each PNG (overlaps, clipped labels, wrong arrows, unreadable fonts, colours in greyscale); fix and re-render.
6. **Unit check.** `python3 -I check_unit_v2.py <unit file> <UNITID> FINAL_OUTLINE_v2.md` with UNITID = `Ch07`, `AppM`, `front`, … Required results: C1 = OK (or deliberate omissions justified in the report); C2 = OK; C3 "not canonical" = OK; C4 = OK; C5 = OK or every item justified as a pointer; C6 = OK; C7 = OK; C8a = OK (no printed planning marker; the comment `% PENDING-VERIFY: …` of §6.12 is allowed); C8b = OK or every occurrence justified in the report (the phrases are over-claims only when unqualified, e.g. 「已被证明」 is correct for an [R] or [V] statement, 「软因子等于 1」 after 「对共线单举截面」). The script reads the registry in §08 of FINAL_OUTLINE_v2 (unit headings `### ChNN` / `### AppX` / `### front` / `### Assumptions`, backticked labels in the first table column — the format FINAL_OUTLINE_v2 uses; checked at the merge). The integrator's whole-outline checker is `checks/check_final_outline_v2.py` (log `checks/check_final_outline_v2.log`).
7. **Tag check** (also part of C6): every `\tagR` environment opens with one of the four qualifier sentences; every R_cond has the premise sentence; every [A]/[P]/[C]/[V] statement is followed by 「地位与缺口」.
8. **Box and table check.** The box of §6.6 is present (where required) and contains only labels that exist; the correspondence table of §6.7 is present (where required).
9. **Page count.** From the unit title to the start of the bibliography: within the budget of §1.1 with tolerance −15 %/+10 %.

---------------------------------------------------------------------------------------------------

## 11. Page budgets, formats and density

Budgets: §1.1 (front 6; chapters 352; appendices 129; total ≈487 pp, A4, 11 pt, 2.5 cm margins). Tolerance −15 %/+10 %. If the lead author must cap the size, cut first the optional figures and App O §O.11 (neighbouring problems); never cut statements, `\uses` lists, status lines or the boxes of §6.6.

| format | units | density |
|---|---|---|
| full (core) | Ch1, Ch3–Ch12, Ch14, Ch15, Ch18, Ch21, Ch25 | ≈60 % statements and proofs, 25 % worked examples, 15 % motivation and status |
| pedagogical | Ch2 | §7 item 5 |
| short | Ch13, Ch16, Ch17, Ch19, Ch20 | each main result as precise statement + status (tag, assumption line, evidence) + `proofsketch` + one worked example; shorten the discussion, never the statements |
| frontier | Ch22, Ch23, Ch24 | §6.11 item 1; ≈55 % statements with hypotheses and proof architecture, 20 % explicit results (one-loop kernels, checks), 25 % status, evidence and open problems |
| appendix (proofs) | App M, N, O | complete proofs; status table with error types at the end (`tab:appM-status`, `tab:appN-status`, `tab:appO-checklist`) |
| appendix (tools) | App A–L | as v1 |
| generated | App P | §6.13 |
| errata | App Q | §6.13 |

---------------------------------------------------------------------------------------------------

## 12. Writer order, inter-unit ownership, interaction with the input files

### 12.1 Writer order and critical path (refdoc S61, adapted to v2)

1. FINAL_OUTLINE_v2 is frozen and patched with the `verify/` outcomes (App M/N/O, 「本书新结果」, App Q); the registry is regenerated.
2. **Part I foundations first:** Ch2 `qcd` and Ch3 `prelim` (every later unit uses their definitions), then Ch4, Ch5. App A, B, C, I, J can be written in parallel with them.
3. **App N first among the deep appendices** (Ch9, Ch10, Ch14, Ch19 cite its labels). Each unit file has exactly one writer (§12.3); the App N writer (W11) delivers a draft of Ch9 `sec:method-subtraction` to the Ch9 writer (W10), who integrates it.
4. **App O after the App N labels of §N.3–§N.5 are frozen.** The App O writer (W15) delivers drafts of Ch12 `sec:dy-glauber`, `sec:dy-model`, `sec:dy-theorem` to the Ch12 writer (W14).
5. **App M is independent** (W08, with the Ch7 statements of FINAL_OUTLINE_v2 frozen; W07 and W08 exchange the 13 proof-delivery targets).
6. Parts II–VI in chapter order where possible (dependency order); Ch6–Ch8 before Ch9; Ch9 before Ch10–Ch14.
7. **Frontier:** Ch22 after Ch8, Ch14, Ch21 are frozen; Ch23 after Ch22 and Ch14; Ch24 after Ch4, Ch9, Ch12, Ch18, Ch21.
8. **Last:** Ch1, front matter, Ch25 (they summarize everything), App P (generated at integration, introduction written last), App Q (after `verify/` completes).
9. **Critical path:** FINAL_OUTLINE_v2 (+ verify patch) → App N → App O → Ch12/Ch14/Ch18 → Ch22–Ch24 → Ch25 → App P.

### 12.2 Inter-unit ownership of topics that have two plausible homes

| topic | owner | others |
|---|---|---|
| QCD Lagrangian, gauge invariance, Faddeev–Popov, BRST, Feynman rules, renormalization, $\overline{\rm MS}$, RG, running coupling, asymptotic freedom | Ch2 | Ch3+ cite; App J holds BRST proofs |
| introductory IR divergences and IR safety | Ch2 (motivation, examples, informal notion) | Ch4 owns `def:ir-safe`, KLN, Bloch–Nordsieck; Ch6 owns the full $e^+e^-$ computation; Ch2 uses VF-EE entries with forward pointers |
| DR: definition needed for renormalization ($D=4-2\varepsilon$, $\mu$, $\overline{\rm MS}$) | Ch2 | Ch3 owns the technical conventions (ε_UV/ε_IR, scaleless integrals, CDR traces), App C the integrals, App I $\gamma_5$ |
| light-cone coordinates, Wilson lines, eikonal rules, distributions, Mellin, Carlson/Müntz, cut diagrams, cutting rules, unitarity, $\gamma_5$ | Ch3 | App A, B, I, J, K proofs; App O the light-cone cut-position identity |
| Landau/pinches, power counting, regions | Ch4 (+ App D, E) | Ch24 frontier status (Collins 2020, Gordan, hidden regions) with `\cref` back; Ch4 may point forward |
| one-loop off-shell triangle (exact remainder) | App N (`prop:appN-triangle-exact`) | Ch5 example quotes VF-REF-2, Ch9 `ex:method-sudakov-subtraction` |
| OPE: vacuum correlator | Ch6 | — |
| OPE: DIS, moments | Ch7 (statements) | App M (proofs and machinery) |
| PDF/FF definitions, positivity | Ch8 (`conj:pdf-positivity`) | Ch24 debate status and explicit Yukawa curves (`fig:front-yukawa-pdf`) |
| subtraction theorem | Ch9 (statement, examples) | App N (precise form, proofs) |
| Glauber deformation | Ch9 (`prop:method-glauber-deformation`, `fig:method-glauber-direction`) | App O (proof), Ch12 (DY) |
| TMD factorization (DY/SIDIS/$e^+e^-$) | Ch14 | Ch22 (quasi-TMD theorem, lattice CS kernel, MD9) and Ch23 (Liu's proof route, Euclidean soft functions) cite it as [A] input |
| SCET, Glauber EFT | Ch15 (SCET), Ch18/Ch24 (Glauber EFT status) | — |
| renormalons, power corrections | Ch21 | Ch22 (linear renormalon of the Wilson-line self-energy, LRR), Ch23 (heavy–light kernel renormalon) |
| lattice moments, quasi-distributions | Ch22 (`lattice-*` labels kept) | Ch7, Ch14 forward pointers |
| exponential decay of space-like correlators | Ch22 (needed for the Fourier step) | Ch23 cites it |
| threshold factorization of the quasi-PDF kernel, heavy–light Sudakov kernel | Ch23 | Ch22 forward pointer; Ch13 (threshold in QCD) |
| near-threshold quarkonium photoproduction (Guo–Ji–Liu) | Ch19 (exclusive, as a new regime with its erratum history) | Ch23 pointer |

### 12.3 Writer assignment (30 parallel writers; v2.2)

One writer per unit file; a writer may own several files. "Start" = the frozen inputs a writer needs (frozen = the statements of FINAL_OUTLINE_v2 for those units, plus the drafts of the listed units where a section is delivered). Page counts are budgets (FINAL_OUTLINE_v2 §0.1). The integrator generates the App P tables and graphs (8 pp) and assembles the book.

| writer | units | pp | start | delivers to / coordination |
|---|---|---|---|---|
| W01 | front matter, Ch1 | 20 | last (all chapters drafted; §09 ★ rows) | `tab:intro-overview`, `tab:intro-assumptions`, `fig:intro-dependency` |
| W02 | Ch2, App J | 21 | first wave | App J proofs for Ch2/Ch3 (BRST nilpotency details, Slavnov–Taylor details, ghost cuts, `lem:appJ-cut-hermiticity`) |
| W03 | Ch3, App A, App I | 17 | first wave | tools used by every later unit |
| W04 | Ch4, App D, App E | 22 | Ch2, Ch3 | App D/E proofs of the Ch4 statements |
| W05 | Ch5, App B | 17 | Ch3, Ch4 | App B Wilson-line proofs (also used by Ch3, Ch23) |
| W06 | Ch6, App C | 17 | Ch2, Ch3 | App C integrals for Ch6, Ch10, Ch12 |
| W07 | Ch7 | 18 | Ch2, Ch3, Ch6 | 13 proof-delivery targets with W08 |
| W08 | App M | 24 | FINAL_OUTLINE_v2 (Ch7 statements) | proofs of the Ch7 targets |
| W09 | Ch8, App K, App L | 21 | Ch7 | App K/L lemmas for Ch7, Ch8, App M, Ch24 |
| W10 | Ch9, App F | 23 | Ch4, Ch5, Ch8; App N statements | integrates W11's draft of `sec:method-subtraction` |
| W11 | App N | 24 | FINAL_OUTLINE_v2 (first among the deep appendices) | draft of Ch9 `sec:method-subtraction` to W10 |
| W12 | Ch10 | 13 | Ch9, App N | — |
| W13 | Ch11 | 13 | Ch9, Ch10 | — |
| W14 | Ch12 | 18 | Ch9; App O statements | integrates W15's drafts of `sec:dy-glauber`, `sec:dy-model`, `sec:dy-theorem` |
| W15 | App O | 32 | App N §N.3–§N.5 frozen | drafts for Ch12 to W14 |
| W16 | Ch13 | 9 | Ch12 | — |
| W17 | Ch14 | 16 | Ch9, Ch12, App N, App O | — |
| W18 | Ch15 | 13 | Ch5, Ch9 | — |
| W19 | Ch16 | 10 | Ch15 | — |
| W20 | Ch17 | 9 | Ch9 | — |
| W21 | Ch18 | 14 | Ch12, Ch14 | — |
| W22 | Ch19 | 11 | Ch9, App N | — |
| W23 | Ch20 | 10 | Ch15 | — |
| W24 | Ch21 | 13 | Ch7, Ch9 | — |
| W25 | Ch22 | 18 | Ch8, Ch14, Ch21 | Part VII preface |
| W26 | Ch23 | 15 | Ch14, Ch22 | — |
| W27 | Ch24 | 18 | Ch4, Ch9, Ch12, Ch18, Ch21 | — |
| W28 | Ch25, App P introduction (`sec:appP-intro`, 2 pp) | 14 | everything else | master-table rows from FINAL_OUTLINE_v2 §09 |
| W29 | App G, App H | 5 | drafts of Ch6–Ch14 | App G one-loop details not printed in the chapters |
| W30 | App Q | 4 | `verify/` complete (after the verify patch) | errata table from the verification records |

Total written 479 pp + 8 pp generated (App P) = 487 pp. A writer who finishes early may be assigned to the critical path (App N → App O → Ch12/Ch14/Ch18 → Ch22–Ch24 → Ch25 → App P, §12.1 item 9) by the lead author; files never change hands without the lead author.

### 12.4 Input files (read-only)

1. Ready-made Chinese drafts in the monograph style may be adapted: `research/c_dis/dis_oneloop.tex`, `research/c_dy/dy_oneloop.tex`, `research/c_ee/ee_total.tex`, `research/c_regions/{landau,powercounting,regions}.tex`, `research/c_wilson/tex/*`, `research/c_pdf/tex/*`, `research/c_exclusive/tex/*`, `research/c_scet/tex/*`, `research/c_tmd/tex/*`, `research/c_glauber/tex/c_glauber_snippets.tex`. Relabel to canonical labels; convert conventions ($\bar n,n\to n_A,n_B$ outside Ch15; $g\to-g$ where needed); remove local `\newcommand`s; check every formula against VERIFIED_FORMULAS_v2.
2. Frontier reports (`frontier/lamet/LAMET.md`, `frontier/yzliu/YZLIU.md`, `frontier/others/OTHERS.md`) and their scripts are sources for Ch22–Ch24 and for some items elsewhere; their chapter numbers refer to older outlines — always use labels. YZLIU §6.2 contains draft LaTeX statements: they must be relabelled, retagged (§4.3 item 4), corrected (½K) and converted.
3. `refdoc/REFDOC_ANALYSIS.md` and `refdoc/notes/R*.md` are sources of constructions to re-derive (never to quote, §6.10).
4. `verify/` (when available): the verification records decide 「本书新结果」 (§6.5), App Q (§6.13) and the [PENDING-VERIFY] items (§6.12). Its claims register `verify/CLAIMS.md` indexes the items (E01–E36, N01–N29, R-…, A01–A28); this spec and REFS_NOTES_v2 refer to them by these IDs.
5. If a derivation contradicts a VF entry, the derivation wins only if its checks pass; report the discrepancy.
6. Do not modify research, frontier, refdoc, verify files, `CONTEXT.md`, `REQUIREMENTS.md`, `common/preamble_fact.tex`, or anything in `spec/` or `spec_v2/`.

---------------------------------------------------------------------------------------------------

## 13. Final report (return to the lead author), in this order

1. **File:** path, page count, compile status (errors 0; overfull > 1 pt 0; undefined citations 0; BibTeX warnings 0).
2. **Canonical labels:** implemented / missing (with reasons); output of `check_unit_v2.py` (C1–C8).
3. **Additional labels** defined (incl. auxiliary lemmas and extra examples).
4. **External labels** referenced (all canonical).
5. **Tags:** each canonical statement with its final tag and qualifier; any weakening justified; grade-propagation conflicts found.
6. **Assumptions:** `asm:` labels defined (owners only) and used; premise sentences of R_cond statements; non-perturbative status lines added.
7. **`\uses`:** C5 items justified as pointers; dependency problems (forward edges, cycles) found.
8. **Formulas:** VF IDs used; writer-derived formulas with the check made; T-status formulas and how they were handled.
9. **Pending items:** every `% PENDING-VERIFY` place with its claim ID; 「本书新结果」 items printed with their `verify/` record paths; candidate errata noticed (for App Q), with the CLAIMS ID if the claim is already registered.
10. **Citations:** keys used; aliases resolved; 「文献待补」 items; 「位置待核实」 locations; preprints marked.
11. **Figures:** existing figures copied (source file and timestamp); new figures drawn; placeholders; figure issues (caption conventions, errors).
12. **Boxes and tables:** the box of §6.6, correspondence tables (§6.7), status tables with error types.
13. **Deviations** from FINAL_OUTLINE_v2 or this spec, with justification; errors found in the spec files.
14. **Open items** for the lead author.

---------------------------------------------------------------------------------------------------

## CHANGELOG

**2026-10-10 — v2 drafted (spec-v2 writer-spec/figures/bibliography drafter).** Inputs: `spec/WRITER_SPEC.md` (v1, audited), `spec/FINAL_OUTLINE.md`, `spec/FIGURES_INDEX.md`, `spec/VERIFIED_FORMULAS.md`, `spec/REFS_NOTES.md`, `refdoc/REFDOC_ANALYSIS.md` (§1.2–1.3, §2, §3.e, §4, §5 S1–S63), `frontier/{lamet,yzliu,others}` reports and bibliographies, `research/critic/REVIEW.md` §2, §3.2, §7, `CONTEXT.md`, `REQUIREMENTS.md`, `common/preamble_fact.tex`, the binding v2 structure of the lead author.
1. Structure, keys, files, page budgets and parts of the v2 book (§1.1); key clash `front` resolved (§1.1 note 2).
2. Tag system v2: four `[R]` qualifiers with verbatim sentences (R_OPE replaces 「以 OPE 为前提」 and now names `asm:intro-np-ope` for hadron states; R_cond with the premise sentence) (§4.3); frontier grade notations mapped (§4.3 item 4).
3. Assumption environment, fields, tags, inner-item scoping, naming rules, global vs technical assumptions; MA line replaced by the non-perturbative status line with `asm:` labels (§4.4).
4. Mandatory `\uses` lists with completeness, label-type and ordering rules; appendix and moved-label rules (§4.5); grade-propagation rule incl. R_cond content grades (§4.6); error types (§4.7); grade dictionary printed without citing the reference document (§4.8).
5. Labels: moved labels keep their keys; ownership from the registry; `asm:` prefix; definition-ownership table for v2 (§5).
6. Content: promised appendix proofs incl. App M/N/O/P/Q (§6.3); 「本书新结果」 rule with two independent confirmations in `verify/` and a literature check (§6.5); boxes and correspondence tables (§6.6–§6.7); misconceptions M1–M35 allocated to v2 units (§6.8); over-claims v1 + S58 + frontier (§6.9); S62 (§6.10); frontier rules incl. Ch22/Ch23/Ch24 ownership (§6.11); [PENDING-VERIFY] protocol (§6.12); App P and App Q (§6.13).
7. Readability rules for Part I with quantitative example targets (§7).
8. Notation table: rows 38–48 added (Glauber direction, error types, Ioffe time, quasi/pseudo distributions, LaMET logarithms, quasi-TMD normalization, $\gamma_{HH}$, Liu's $\beta$ conventions, hyperbolic angle, SU(N) identities, assumption labels); rows 4, 8, 9, 10, 21, 27–31, 36 extended with the frontier conversions (§3).
9. QA: `checks/check_unit_v2.py` (owners from the registry; `asm:`; `\uses` checks; qualifier and status-paragraph checks; forbidden phrases), tested on a synthetic unit (§10).
10. Bibliography: `refs_merged_v2.bib` (998 entries), `key_aliases_v2.tsv` (1067 rows), tested with BibTeX and XeLaTeX (§9).

**2026-10-10 (later) — spec v2.1 (resumed writer-spec/figures/bibliography drafter).** Input added: `verify/CLAIMS.md` (claims register of the verification workflow, compiled after v2.0 was drafted).
1. Every pending item keyed to the CLAIMS IDs: §6.5 item 4 now classifies N01–N29 (K1 candidates 「本书新结果」, K2 candidates subject to a literature check, K3 sharpened results never marked new, K4 our derivations of published results, K5 not printed as results); §6.5 item 5 on the R-claims; §6.13 classifies E01–E36 (Q1 App Q candidates, Q2 author-corrected, Q3 not App Q, E19 never, E33 rule); §6.12 comments carry the claim ID; §13 item 9 asks for the IDs.
2. §6.9: attribution traps from A01–A28 (author list of NPB 964, priority words, LaMET proof scope, regions attributions, Glauber attributions, wrong references for the pion pole and SCET endpoint singularities, literature-absence statements, Sivers sign).
3. Bibliography counts updated to 1003 entries (REFS_NOTES_v2 CHANGELOG v2.1); §0 table extended.
4. QA: `checks/check_unit_v2.py` fixed after a synthetic-unit test — C5 no longer treats the 「被使用于：」 field of an assumption (reverse dependencies) as missing `\uses` entries (§4.4 item 3 says so explicitly); C8 split into C8a (printed planning markers, must be absent; the comment form is allowed) and C8b (context-dependent phrases, shown with context, to be justified) (§10 item 6). The synthetic unit (box of §6.6, assumption with all fields, [R, R_cond] theorem with premise sentence, [A] statement with 「地位与缺口」, pointer) compiles with 0 errors.
5. §4.4 item 2 corrected: assumption tags are copied from the register, and the register's "open" (= not proven as stated) is not mapped to `\tagC`; `\tagC` is reserved for claims without any all-order argument (otherwise the grade propagation of §4.6 would have demoted `thm:dy-factorization` through the App O inputs, contrary to refdoc S5/S8); §4.6 item 3 says the same.
6. §4.6 item 1 corrected: the OPE premises of an R_OPE statement are excluded from $\min_p\mathrm{tag}(p)$ (as the `asm:` premises of R_cond are), and the content grade of an R_OPE statement is [A] for its users; without this, every R_OPE statement (e.g. `thm:dis-moments`, which uses the [A] statement `thm:dis-ope`) would violate the rule and the App P generator check.

**2026-10-10 (merge) — spec v2.2 (spec-v2 integrator; aligned with `FINAL_OUTLINE_v2.md`).**
1. Companion files: FINAL_OUTLINE_v2 now exists (registry §08, master rows §09, merge decisions MD1–MD18 §0.8, merged pending register §0.10); the three outline drafts are superseded; `ASSUMPTIONS.md` v2.2 (binding texts = owners' entries, MD18).
2. §4.4: 41 register entries; `asm:appN-brst-nonlocal` `\tagC` (named gap, MD1), `asm:appN-ir-regulator` premise only of `thm:disall-renorm-compat` (MD2); binding inner names incl. (OPE1)–(OPE5) (MD15).
3. §4.5 item 5: no hidden forward dependencies through appendices (checked, W2).
4. §4.6: global-only R_cond premises in R_PT/R_OPE statements (MD4, closing the rule gap reported by the core drafter); new item 6 "named gaps" (MD1) with generator check C-P17.
5. §4.7: `% errtype:` comment convention for the App P generator.
6. §5.3: labels changed at the merge (`rem:qcd-bphz-brst`; `lem:appO-past-unitarity` deleted; new `lem:appO-orientation`); §5.6 ownership of the frontier and App N/O definitions (MD9).
7. §6.3, §6.11 item 5, §12.2: Part VII ownership as in FINAL_OUTLINE_v2 (Ch22 owns the quasi-TMD theorem, the off-light-cone and reduced soft functions, the lattice CS kernel and TMD ratios).
8. §6.12: fallback tags for writers before the patch; §6.13: App P longtable in the master driver, per-part graphs, C-P17; App Q candidate list updated with the stage-1 notes (E02 journal version correct; E01 first corrected by Chou–Chen 2022; E28, E32 not App Q).
9. §1.1: App A–L budgets rebalanced inside 35 pp (MD5). §10 item 6: registry format confirmed; integrator checker named.
10. §12.1, §12.3 (new): one writer per file; writer assignment W01–W30 with start conditions; old §12.3 is §12.4.

