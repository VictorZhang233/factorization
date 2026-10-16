import os, sys, re
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import src
import regtable
ln = src.ln
TARGET = 'FINAL_OUTLINE_v2.md'

S010 = r'''### 0.10 Verification register (resolved by the verify patch v2.3, 2026-10-11)

Sources: `verify/CLAIM_VERDICTS.md` (137 claims, two independent stages per claim), the stage records `verify/claims/batch_*_s1.md`, `batch_*_s2.md`, and the final reports of the proof extensions `verify/extend_reports/X1-glauber_final.md`, `X2-subtraction_final.md`, `X3-ope_final.md` (each with an independent final review). Decision rules: §00.4 (slots), WRITER_SPEC_v2 §6.5 (novelty), §6.13 (App Q). No pending-verification marker remains in this file.

| item | where | outcome (v2.3) | applied in |
|---|---|---|---|
| App M route of the DIS moments | Ch7 (`prop:dis-ope-euclid`, `prop:dis-ope-gi`, `prop:dis-ope-forward`, `prop:dis-ope-rg`, `prop:dis-dispersion-np`, …); App K | X3a not delivered, X3b not passed, X3c not delivered, X3d partial, X3e PASS per graph; S63-1 (Smirnov checked, scope short), S63-2 (circular uniqueness route; reduction to (CTp)), S63-3 (Joglekar at abstract level; the (Eε) route), S63-4 (R-M24 precision) | Ch7 entries; App M; Ch25 OP-A2, OP-A5 |
| App N route of the subtraction theorem | Ch9, Ch10, Ch14 (`prop:tmd-zero-bin-soft`(b), `lem:tmd-sqrt-identity`(b)), Ch19 (`prop:excl-soft-cancel`) | X2a delivered (`prop:appN-triangle-cs`), X2b, X2c not delivered, X2d open; N12 confirmed; S63-12 (Collins 2011 ch. 10 = scaling statements; integral norms only for the triangle) | Ch9, Ch10 entries (tags unchanged); App N; Ch25 OP-B1 |
| App O route of the Glauber cancellation | Ch9, Ch12, Ch14, Ch18; App J `lem:appJ-cut-hermiticity` | X1c PASS ([R, R_cond]), X1f PARTIAL (model theorems [P]), X1a, X1b, X1d, X1e not delivered; N13 refuted as a novelty claim (the lemma is kept, corrected and sharpened); S63-8 = N14(i): the lemma is restated (largest-time circling rule, ghost caveat), N14 unresolved | chapter tags unchanged; App O; App J |
| 「本书新结果」 candidates | Ch12 `prop:dy-eikonal-twogluon`; App N `prop:appN-triangle-cs`(a) | N01 confirmed but known (`Meggiolaro:1996hf`, `Giordano:2006vv`): no marker; S63-5 = N01; the only marker of the book: `prop:appN-triangle-cs`(a), with the search-date wording | Ch12; App N; §00.4 |
| sharpened results (never marked new) | Ch5/Ch9 pointers to `prop:appN-triangle-exact`(c) | N12 confirmed ("no logarithm at NLP") | Ch5, Ch9, Ch21 |
| verified computations (novelty never claimed) | Ch3, Ch6, Ch12, Ch14, Ch18, Ch19, Ch20, App K | N16, N17, N18, N19, N20, N23, N24, N25, N26 confirmed (our derivations of known results, with attribution); N21 confirmed (closed forms; novelty not asserted); N22 refuted (the illustration is dropped) | the entries' attribution sentences |
| literature errata | Ch5, Ch14, Ch15, Ch16, Ch18, Ch19, Ch20, Ch22, Ch23; App B, App F | 16 confirmed Q1 errata printed in App Q (`tab:appQ-errata`); E06, E12, E27, E29, E30 as author corrections (`tab:appQ-errata-b`); E22, E32 refuted (nothing printed); E19 never printed; E28 convention remark; E31 quotation; Q3 items in status paragraphs | App Q; the entries |
| attributions | Ch4, Ch7, Ch8, Ch12, Ch18, Ch22–Ch24 | A01–A03, A05, A07–A10, A12–A28 confirmed; A04, A06, A11 refuted in single items and corrected (A04: APPB §4.4 concerns `Collins:2011ca`; A06: N³LO kernel `Cheng:2024wyu` and the Rossi–Testa exchange; A11 item (3): RS treat the $n$–$\bar n$ current at one and two loops); R-M20 wording per REFS_NOTES_v2 | the entries; WRITER_SPEC_v2 §6.9 |
| open verification items | Ch14, Ch18, Ch20, Ch21, Ch9/Ch12/Ch15 | S63-6 confirmed (`Collins:2016hqq`); S63-7 $p=2$ (`Scimemi:2016ffw`, `Moos:2020wvd`); S63-9 locations verified; S63-10 (`Becher:2024kmk`: "does not amount to a proof"); S63-11 Chay–Kim and BBK confirmed, FMRS 1986 and Bostelmann 2005 not re-read (hedged) | the entries |
| Part VII | Ch22–Ch24 | per-chapter lists 「Verification outcomes (Ch22/Ch23/Ch24)」; N09 refuted as stated (`prop:lamet-tails` rewritten); N02, N03, N04, N07, N08, N10 confirmed without markers | Part VII |
| bibliography | all units | 48 entries added after INSPIRE (45) or Crossref (3) verification (`refs_merged_v2.bib` PART 10); Feichtner–Sturmfels and the Mir 1979 Vladimirov monograph could not be verified (not cited; `Vladimirov2002` instead); Bałaban CMP 116 (1988) not found (not cited) | `REFS_NOTES_v2.md` §6 |

'''

MD19 = r'''| MD19 | **Verify patch v2.3** (2026-10-11, spec patcher): all verification outcomes applied (§0.10; slot outcomes §00.4); the new App M/N/O statements are registered (§08) together with six new assumptions — `asm:appM-oswi`, `asm:appN-lce`, `asm:appN-analytic-reg` (\tagA), `asm:appO-adjacent-swap`, `asm:appO-real-jets` (\tagP), `asm:appO-collinear-ends` (\tagA) — so that the register has 47 entries; rewordings: `asm:appM-brst-ope` ((B1) retired, (B2) ≡ (Eε)), `asm:appO-mixing` (clause (a′)), `asm:appO-envelope` (side-summed families for coincident connections), `asm:appO-deformation`(c)(d); local inner names (Pr1)–(Pr5), (NE), (CTp), (FR), (FI), (IL1)–(IL3), (IRF), (COV), (SEC), (EQ), (ADJ), (REAL), (LCE), (RA1)(RA2) are clash-free (`ASSUMPTIONS.md` §4); App Q final; the only novelty marker `prop:appN-triangle-cs`(a); master row III.12 bottleneck `asm:appN-ir-regulator` (content [C]); new master rows II.30, III.39, III.40. **Lead-author confirmation requested** for the six new assumptions, the [P] grading of the App O model theorems and the printed novelty marker. | §00.4, App M/N/O, App Q, §08, §09; `ASSUMPTIONS.md` v2.3 |'''

NEWROWS_II = r'''| II.30 | 前向在壳 DR 振幅的逐图展开定理 | 硬区振幅中 $\omega^n$ 的系数等于朴素 Taylor 项（逐图，维数加解析正规化） | [R, R_PT] | 部分子 | `thm:appM-forward-expansion` | — | 全阶算符形式（`cor:appM-forward-ope`；OP-A5） | |'''
NEWROWS_III = r'''| III.39 | 单圈离壳三角图满足 Collins 条件 (CS1)–(CS3) | 纤维化积分范数界，对 $\varepsilon$ 一致 | [R, R_PT] | 部分子 | `prop:appN-triangle-cs` | — | 一般图（OP-B1；纤维化纲领 `rem:appN-fibered-allorders`） | |
| III.40 | 全重合旁观者对的 $O(g^4)$ 侧求和（未割线）：全局两时模型中相消 | ${\rm Re}\,p_{\rm opp}$ 幂次压低；$C_A$ 项为 Regge 相位 | [P] | 部分子（模型） | `prop:appO-twoexch-spectator` | `asm:appO-adjacent-swap`、`asm:appO-real-jets`、`asm:appO-collinear-ends` | 被割直接线（`rem:appO-cut-ss`）；QCD 喷注的 (ADJ)(REAL) | |'''

S10_OLD_START = 'Reserved [PENDING-VERIFY] slot labels (§00.4; inserted into the registry by the verification patch only if the slot passes;'
S10_NEW = r'''No reserved slot labels remain (verify patch v2.3). The delivered slots are canonical entries: X1c `lem:appO-side-independent-windows`, X1f `prop:appO-twoexch-spectator` (with the further model results of §O.5), X2a `prop:appN-triangle-cs`, X3e `thm:appM-forward-expansion`. The labels reserved for the slots X1a, X1b, X1d, X1e, X2b, X2c, X3a, X3b, X3c and X3d are **withdrawn** and must not be used (they are named only by slot ID, §00.4); X2d changed nothing but the status sentence of `rem:appN-abs-edge`. `tab:appQ-errata-b` is printed (class Q2 table, decided by the patch; an optional table, not a registry row).
'''

CHANGELOG = r'''

**2026-10-11 — v2.3: verify patch (spec patcher).** Inputs: `verify/CLAIM_VERDICTS.md` (137 claims), `verify/claims/`, `verify/extend_reports/X1-glauber_final.md`, `X2-subtraction_final.md`, `X3-ope_final.md`, the final-review summaries. Applied by the patch scripts saved in `verify/patch_v23_scripts/` (`apply_all.py` re-applies every module to the pre-patch backup `verify/patch_backup_spec_v2_prepatch/`; outline modules for §0, Ch1–Ch25, App A–L, App M, App N, App O, the global rules, App P, App Q, §08–§11).
1. Every pending-verification marker resolved (none remains): confirmed items finalized, refuted items removed or rewritten (E22, E32, N09, N13, N22, A04, A06, A11 item (3)), unresolved or disputed items hedged (N14 in `lem:appJ-cut-hermiticity`, E34 without verdict); §0.10 rewritten as the resolved register; §00.4 as the slot-outcome table; MD19.
2. App M/N/O: slot results inserted (X3d partial, X3e per graph; X2a; X1c, X1f partial) with the new entries listed in §00.4, six new assumptions, the undelivered slots withdrawn, status tables, ledgers, boxes and figure notes updated; grade changes propagated to the chapter statements (`prop:dis-ope-euclid`, `prop:dis-ope-gi`, `prop:dis-ope-rg`, `prop:dis-ope-forward`, `prop:dy-eikonal-twogluon`, `lem:tmd-glauber` status) and to the master table.
3. App Q final: 16 Q1 rows (credits: `Chou:2022drv` for E01; the authors' own footnote for E02) and 5 Q2 rows; the only 「本书新结果」 marker is `prop:appN-triangle-cs`(a).
4. Master table: row III.12 bottleneck `asm:appN-ir-regulator` (content [C]); control characters removed from rows II.28, II.29; rows II.1, II.9, II.27, II.29, III.4, III.25, III.27, III.38, IV.5, IV.25, V.23, VII.28, VII.46 finalized; new rows II.30, III.39, III.40.
5. Bibliography: 48 verified additions (`refs_merged_v2.bib` PART 10); every 「文献待补」 placeholder replaced by a key or the citing text adjusted.
6. Regenerated: §08 registry rows of App M, N, O, the `### Assumptions` register (47 entries; broken math cells rebuilt with `\vert`; users recomputed), §11 counts and the header numbers. Checks: `checks/check_final_outline_v2.py` E1–E14 OK, W1–W2 OK.'''

def regen_counts(t):
    ST = regtable.chk.parse(t)
    owner, rows, asm = regtable.chk.registry(t)
    lines = t.split('\n')
    i11 = next(i for i, l in enumerate(lines) if l.startswith('## 11 Counts'))
    a = next(i for i in range(i11, len(lines)) if lines[i].startswith('| unit |'))
    b = a + 2
    while b < len(lines) and lines[b].startswith('|'):
        b += 1
    old = {}
    for l in lines[a + 2:b]:
        c = [x.strip() for x in l.strip('|').split('|')]
        old[c[0]] = c
    units = [c for c in old if c != '**total**']
    out = []
    tot = [0] * 7
    for u in units:
        st = [s for s in ST if s['unit'] == u]
        n_st = len(st)
        n_ex = sum(1 for s in st if s['pfx'] == 'ex')
        n_asm = sum(1 for s in st if s['pfx'] == 'asm')
        n_sec = sum(1 for (uu, lab, cells) in rows if uu == u and lab.startswith('sec:'))
        n_tab = sum(1 for (uu, lab, cells) in rows if uu == u and lab.startswith('tab:'))
        n_fig = sum(1 for (uu, lab, cells) in rows if uu == u and lab.startswith('fig:'))
        n_opt = int(old[u][7])
        vals = [n_st, n_ex, n_asm, n_sec, n_tab, n_fig, n_opt]
        tot = [x + y for x, y in zip(tot, vals)]
        out.append('| %s | %s |' % (u, ' | '.join(str(v) for v in vals)))
    out.append('| **total** | %s |' % ' | '.join(str(v) for v in tot))
    lines[a + 2:b] = out
    # tag line and marker line
    def tagkey(s):
        if s['pfx'] == 'asm':
            return 'asm ' + ('—' if s['tag'] is None else '[%s]' % s['tag'])
        if s['tag'] == 'R':
            return '[R, %s]' % s['qual']
        if s['tag']:
            return '[%s]' % s['tag']
        return '(数学，无标签)' if s['qual'] == 'math' else '(no tag)'
    cnt = {}
    for s in ST:
        k = tagkey(s); cnt[k] = cnt.get(k, 0) + 1
    tagtxt = '; '.join('%s %d' % (k, v) for k, v in sorted(cnt.items(), key=lambda kv: -kv[1]))
    j = next(i for i in range(b, len(lines)) if lines[i].startswith('Tags of the '))
    lines[j] = 'Tags of the %d statement labels: %s.' % (len(ST), tagtxt)
    lines[j + 1] = 'Reserved slot labels: none (§10). Pending-verification markers in this file: 0 (verify patch v2.3). Registry: %d unit rows + %d register rows.' % (len(rows), len(asm))
    # header numbers (line starting with **Numbers)
    n_ex = sum(1 for s in ST if s['pfx'] == 'ex'); n_asm = sum(1 for s in ST if s['pfx'] == 'asm')
    nonasm = {k: v for k, v in cnt.items() if not k.startswith('asm ')}
    tag_hdr = '; '.join('%s %d' % (k, v) for k, v in sorted(nonasm.items(), key=lambda kv: -kv[1]))
    h = next(i for i, l in enumerate(lines) if l.startswith('**Numbers (generated'))
    lines[h] = ('**Numbers (generated after the verify patch v2.3; `checks/check_final_outline_v2.py`, log `checks/check_final_outline_v2.log`).** '
                '%d canonical statement entries (incl. %d worked examples and %d assumptions) in %d units; no reserved slot labels; '
                '%d registry rows (%d unit rows + %d register rows); 0 pending-verification markers; tags (assumptions excluded): %s. '
                'All checks of §0.5 pass (no duplicate label, no undefined `\\uses` target, no forward dependency between chapters, no dependency cycle, '
                'grade propagation and qualifier compatibility hold, every R_cond premise in `\\uses`, every `asm:` label registered and used, every citation key '
                'in `refs_merged_v2.bib`, every required figure owned, budgets sum to 487 pp).'
                % (len(ST), n_ex, n_asm, len({s['unit'] for s in ST}), len(rows) + len(asm), len(rows), len(asm), tag_hdr))
    return '\n'.join(lines)

def _insert_after_row(t, prefix, rows):
    lines = t.split('\n')
    idx = [i for i, l in enumerate(lines) if l.startswith(prefix)]
    assert len(idx) == 1, (prefix, idx)
    lines[idx[0] + 1:idx[0] + 1] = rows.split('\n')
    return '\n'.join(lines)

OPS = [
 # ---------------- §0 header
 ('sub', 'the merged **[PENDING-VERIFY] register**,', 'the **verification register** (resolved by the verify patch v2.3),', '**What this file contains (in order).**'),
 ('sub', '**integrator decisions MD1–MD18**', '**integrator decisions MD1–MD19**', '**What this file contains (in order).**'),
 ('rep', ln(9) + '\n', '**Planning markers (never printed in the book).** None remains: the verify patch v2.3 (2026-10-11) resolved every pending-verification marker (claims E01–E36, N01–N29, A01–A28 and R-* of `verify/CLAIMS.md`; proof extensions X1/X2/X3; S63-k items of refdoc §5.11; outcomes in §0.10 and §00.4). The merge markers of the drafts ([SYNC-APP], [SYNC-ASM], [SYNC-FRONTIER]) are resolved. The planning phrase 「本书新结果（待文献核查）」 is never printed; the only printed novelty marker is that of `prop:appN-triangle-cs`(a) (WRITER_SPEC_v2 §6.5).\n'),
 ('rep', ln(94) + '\n', '- The reserved slot labels of App M/N/O were resolved by the verify patch v2.3: delivered slots are canonical entries, undelivered ones are withdrawn (§00.4, §10).\n'),
 ('sub', 'MD1–MD18 (binding unless the lead', 'MD1–MD19 (binding unless the lead', '### 0.8 Integrator (merge) decisions'),
 ('sub', '**every claim stays [PENDING-VERIFY]** (single confirmations).', 'every claim stayed pending until the verify patch v2.3 (single confirmations); MD19.', '| MD16 |'),
 ('rep', ln(140) + '\n', ln(140) + '\n' + MD19 + '\n'),
 ('sub', '`prop:appO-tmd`) [PENDING-VERIFY: X1] |', '`prop:appO-tmd`; X1 outcomes §00.4, tags unchanged) |', '| `prop:method-fsi`, `lem:dy-fsi`, `prop:dy-deformation`, `lem:tmd-glauber` | sketches |'),
 ('range', '### 0.10 [PENDING-VERIFY] register (merged; the verify patch finalizes every item)\n', '### 0.11 Where the refdoc changes S1–S63 are applied', S010, False),
 ('sub', '| S59 | 「本书新结果」 | §0.9; Ch12 `prop:dy-eikonal-twogluon` |', '| S59 | 「本书新结果」 | §0.9, §00.4; the only marker is App N `prop:appN-triangle-cs`(a) (Ch12 `prop:dy-eikonal-twogluon` without marker, N01) |', '| S59 |'),
 ('sub', '(all S60 keys now present except Gribov 1978, Lee–Zinn-Justin 1972, Zinn-Justin 1975, Appelquist–Carazzone 1975 — cited as 「文献待补」 where needed)', '(all S60 keys present; the four missing ones were added in v2.3 after INSPIRE verification: `Gribov:1977wm`, `Lee:1972fj`, `Lee:1972ocr`, `Lee:1972yfa`, `Zinn-Justin:1974ggz`, `Appelquist:1974tg`)', '| S60 |'),
 ('sub', '`rem:front-gordan-collins` [PENDING-VERIFY: N02];', '`rem:front-gordan-collins` (N02 confirmed, no marker);', '| `lem:appD-gordan`, `sec:appD-caveats` (App D) |'),
 # ---------------- §09 master rows
 ('sub', 'BM 假设对含鬼场非阿贝尔理论的逐条核对 [PENDING-VERIFY: N24]', '—（BM 假设已逐条核对：协变规范含鬼场的无质量 QCD 满足，N24）', '| II.1 |'),
 ('sub', '| IV.3；`asm:appM-remainder` | [R, R_PT] [PENDING-VERIFY: S63-1] |', '| IV.3；所引欧氏展开定理的适用范围 (A1)–(A4)（`Smirnov:1990rz` 已核对，范围不足） | [R, R_PT]：若某一引用定理覆盖含夸克、鬼场与规范变算符的 QCD（OP-A2） |', '| II.9 |'),
 ('sub', '无一般证明；文献有争议 [PENDING-VERIFY: E35]', '无一般证明；Yukawa 模型反例：$\\mu=0.8$ GeV 时 $\\xi\\in(0.264,1)$ 上 $f<0$，对所有 $\\xi$ 为正当且仅当 $\\mu\\ge1.699$ GeV（`CollinsRogersSato2022`；E35）', '| II.27 |'),
 ('rep', '| II.28 | 微扰论中的 OPE 恒等式（有质量欧氏模型） | $\tilde G^T_{AB}=\\sum_{d_O\\le a}\tilde C_O\tilde G_{N[O]}+\tilde N_a$ |', '| II.28 | 微扰论中的 OPE 恒等式（有质量欧氏模型） | $\\tilde G^T_{AB}=\\sum_{d_O\\le a}\\tilde C_O\\tilde G_{N[O]}+\\tilde N_a$ |'),
 ('rep', '| II.29 | 约化系数的标度与余项（有质量模型） | $\x0bert\tilde C_O\x0bert\\le K\x0bert q\x0bert^{D-d_O}\\ln^k\x0bert q\x0bert$ | [R, R_cond] | 部分子（模型） | `thm:appM-scaling` | `asm:appM-remainder`（内容 [A]） | 槽位 X3a：由引用定理解除 [PENDING-VERIFY: X3] | |',
  '| II.29 | 约化系数的标度与余项（有质量模型） | $\\vert\\tilde C_O\\vert\\le K\\vert q\\vert^{D-d_O}\\ln^k\\vert q\\vert$ | [R, R_cond] | 部分子（模型） | `thm:appM-scaling` | `asm:appM-remainder`（内容 [A]） | 证明零动量匹配估计 (CTp)（`rem:appM-remainder-reduction`；槽位 X3a 未交付） | |\n' + NEWROWS_II),
 ('sub', '| — [PENDING-VERIFY: N12] |', '| —（N12 已证实；完整的 (CS1)–(CS3)：III.39） |', '| III.4 |'),
 ('sub', '| `asm:appN-multren` | (Z2) 正规子 |', '| `asm:appN-ir-regulator`（内容 [C]） | (Z2) 正规子（OP-B3） |', '| III.12 |'),
 ('sub', '| 解除上述假设 [PENDING-VERIFY: X1] |', '| 解除上述假设（OP-C1；窗口边缘项已由 `lem:appO-side-independent-windows` 消去；模型证据 III.40） |', '| III.25 |'),
 ('sub', '| — [PENDING-VERIFY: N01] | 非程函旁观者与全阶 |', '| —（已知结果：`Meggiolaro:1996hf`；N01） | 非程函旁观者与全阶 |', '| III.27 |'),
 ('sub', '（OP-B1） [PENDING-VERIFY: X2] |', '（OP-B1；单圈三角图已完成，III.39） |', '| III.38 |'),
 ('func', lambda t: _insert_after_row(t, '| III.38 |', NEWROWS_III)),
 ('sub', '| $p=2$ [PENDING-VERIFY: S63-7] |', '| $p=2$（`Scimemi:2016ffw`、`Moos:2020wvd`） |', '| IV.5 |'),
 ('sub', '| [PENDING-VERIFY: S63-10] |', '| `Becher:2024kmk` 的恢复证据（作者自述"不构成证明"） |', '| IV.25 |'),
 ('sub', '| [PENDING-VERIFY: S63-11] |', '| 模型情形：`Beneke:1998eq` 已核对；`Feldman:1986ax`、`Gawedzki:1985ez` 未重读 |', '| V.23 |'),
 ('sub', '| 规划标签 [A]；N04 通过（含循环性检查）后升为 [R, R_PT] [PENDING-VERIFY: N04] |', '| N04 已证实为 [A]（先行工作 `Braun:2019qtp`）；App L 证明的循环性检查未做，不升级 |', '| VII.28 |'),
 ('sub', '| Gaunt 论证与 SYZ [PENDING-VERIFY: E36] |', '| Gaunt 论证失效且只是提议；SYZ 只否定纯 Glauber 部分（E36） |', '| VII.46 |'),
 ('sub', 'Reserved [PENDING-VERIFY] slot labels are not rows (§10).', 'Withdrawn slot labels are not rows (§10).', 'Generated at the merge from the entries of this file'),
 ('sub', 'merged [PENDING-VERIFY] register with the stage-1 notes', 'merged pending-verification register with the stage-1 notes', '1. Assembly in book order'),
 # ---------------- §10, §11, CHANGELOG
 ('range', S10_OLD_START, 'Optional labels (drawn or printed only within the page budget;', S10_NEW + '\n', False),
 ('func', regen_counts),
 ('rep', 'The drafters\' changelogs remain in the superseded draft files.', 'The drafters\' changelogs remain in the superseded draft files.' + CHANGELOG),
]
