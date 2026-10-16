import os, sys, re, json
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import src
TARGET = 'REFS_NOTES_v2.md'
SPEC = '/Users/hao-cheng/Desktop/theorem proof/qcd_factorization_work/spec_v2'
IND = os.path.join(SPEC, 'checks', 'inspire_additions')

# --- the v2.3 additions: tags in the order of checks/add_refs_v23.py, purposes from the fetch script's records
TAGS = ['Gribov1978', 'LeeZinnJustin1972a', 'LeeZinnJustin1972b', 'LeeZinnJustin1972c', 'ZinnJustin1975',
        'AppelquistCarazzone1975', 'BergereDeCalanMalbouisson1978', 'Balaban1987', 'Balaban1989',
        'MagnenRivasseauSeneor1993', 'SchoonderwoerdBakker1998a', 'SchoonderwoerdBakker1998b', 'ChouChen2022',
        'BecherHagerNeubertSchwienbacher2026', 'NakanishiOjima1990b', 'Meggiolaro1997', 'GiordanoMeggiolaro2006',
        'ChengEtAl2025', 'Radyushkin2019', 'Lindsay1984', 'BelitskySmirnov2026', 'BelitskyBorkSmirnov2025',
        'JackiwTempleton1981', 'Borinsky2023', 'Schultka2018', 'LNvRV1997', 'BMMS2019', 'Barcaro2026',
        'ZhouEtAl2022', 'LiuMa2008', 'ScimemiVladimirov2017', 'MoosVladimirov2020', 'ArkaniHamedHillmanMizera2022',
        'Henneaux1996', 'BHHS2000', 'HerrlichNierste1995', 'ChangLi2013', 'Li2022', 'BoerEtAl2017', 'LRS1983',
        'AybatCollinsQiuRogers2012', 'BhattacharyaCocuzzaMetz2020', 'MonahanNeumann2026', 'BuffingMulders2011',
        'BalitskyChirilli2009']
MANUAL = [('Hormander2003', 'Hörmander, L.', 'Springer, Classics in Mathematics (2003; reprint of the 2nd ed. 1990), DOI 10.1007/978-3-642-61497-2 (Crossref)', 'The Analysis of Linear Partial Differential Operators I', 'App M §M.8 (`lem:appM-green`), Ch22 (`prop:lamet-support`: Paley–Wiener–Schwartz, Thm. 7.3.1)'),
          ('Vladimirov2002', 'Vladimirov, V. S.', 'CRC Press (2002), DOI 10.1201/9781482288162 (Crossref)', 'Methods of the Theory of Generalized Functions', 'App M §M.8 (Laplace transforms in tubes); the Mir 1979 edition named in the drafts could not be verified, the location in the 2002 edition is still to be checked (「位置待核实」)'),
          ('NilssonPassare2013', 'Nilsson, L.; Passare, M.', 'J. Geom. Anal. 23 (2013) 24–46, DOI 10.1007/s12220-011-9235-7 (Crossref)', 'Mellin Transforms of Multivariate Rational Functions', 'App M §M.7 (novelty check of `thm:appM-forward-expansion`; open problem)')]

def _records():
    out = []
    for tag in TAGS:
        d = json.load(open(os.path.join(IND, tag + '.json'), encoding='utf-8'))
        p = (d.get('pubinfo') or [{}])[0] if d.get('pubinfo') else {}
        if p and p.get('journal_title'):
            pub = '%s %s (%s) %s' % (p.get('journal_title'), p.get('journal_volume', ''), p.get('year', ''), p.get('page_start') or p.get('artid') or '')
        else:
            ep = (d.get('eprints') or [{}])[0].get('value', '')
            pub = 'arXiv:%s (preprint)' % ep
        auth = (d.get('authors') or [''])[0]
        if len(d.get('authors') or []) > 1:
            auth += ' et al.'
        title = (d.get('title') or '').replace('|', '\\vert ')
        out.append((d['texkey'], auth, pub.strip(), title, d['query'], d['purpose']))
    return out

def _units_citing(outline, key):
    unit, units = '§0', []
    for l in outline.split('\n'):
        m = re.match(r'^## (Chapter (\d+)|Appendix ([A-Q])|0[89] |1[01] |CHANGELOG|F[1-6])', l)
        if m:
            unit = ('Ch%d' % int(m.group(2))) if m.group(2) else ('App ' + m.group(3)) if m.group(3) else l[3:12].strip()
        elif l.startswith('# Part VII annexes'):
            unit = 'Part VII annex'
        if '`%s`' % key in l and unit not in units:
            units.append(unit)
    return ', '.join(units) if units else '—'

def section_51(outline):
    rows = ['| key | first author | publication | title | INSPIRE query | purpose | cited in (FINAL_OUTLINE_v2, v2.3) |', '|---|---|---|---|---|---|---|']
    for key, auth, pub, title, q, why in _records():
        rows.append('| `%s` | %s | %s | %s | `%s` | %s | %s |' % (key, auth, pub, title, q, why.replace('|', '/'), _units_citing(outline, key)))
    for key, auth, pub, title, why in MANUAL:
        rows.append('| `%s` | %s | %s | %s | Crossref DOI | %s | %s |' % (key, auth, pub, title, why, _units_citing(outline, key)))
    return rows

APPQ_OUT = {
 'E01': 'Q1 confirmed: App Q row Q.8 (first corrected by `Chou:2022drv`)', 'E02': 'Q1 confirmed: row Q.11 (noted by the authors, PRD 105 fn. 1)',
 'E03': 'Q1 confirmed: row Q.9', 'E04': 'Q1 confirmed: row Q.10', 'E05': 'Q3 confirmed (status sentence, Ch22)',
 'E06': 'Q2 confirmed: `tab:appQ-errata-b` row Q.17', 'E07': 'Q3 confirmed (attributed)', 'E08': 'Q1 confirmed: row Q.12',
 'E09': 'Q1 confirmed: row Q.13', 'E10': 'Q1 confirmed: row Q.14 (the correct value in `Ji:2023pba` does not note the discrepancy)',
 'E11': 'Q1 confirmed: row Q.15', 'E12': 'Q2 confirmed: row Q.18', 'E13': 'Q1 confirmed: row Q.16', 'E14': 'Q3 confirmed',
 'E15': 'Q3 confirmed', 'E16': 'Q3 confirmed, now by two groups (`Becher:2026kbr`)', 'E17': 'Q1 confirmed: row Q.2 (implicitly corrected in `Aybat:2011ge`)',
 'E18': 'Q1 confirmed: row Q.4', 'E19': 'withdrawn — never printed', 'E20': 'Q1 confirmed: row Q.5', 'E21': 'Q1 confirmed: row Q.6',
 'E22': 'refuted: nothing printed', 'E23': 'Q1 confirmed (journal version too): row Q.1', 'E24': 'Q3 confirmed', 'E25': 'Q1 confirmed: row Q.3',
 'E26': 'Q1 confirmed: row Q.7', 'E27': 'Q2 confirmed: row Q.19', 'E28': 'convention remark (Ch2, Ch16); no App Q row', 'E29': 'Q2 confirmed: row Q.20',
 'E30': 'Q2 confirmed: row Q.21', 'E31': 'quotation of Collins 2011 only (Ch12); no App Q row', 'E32': 'refuted: nothing printed',
 'E33': 'rule confirmed (DHYZ erratum reverses its conclusion)', 'E34': 'disagreements reported without verdict (item (iii) withdrawn by its authors, `Balitsky:2009xg`)',
 'E35': 'Q3 confirmed', 'E36': 'Q3 confirmed (wording: Gaunt shows / suggests; SYZ contradict only the pure-Glauber part)',
}

def appq_outcomes(t):
    lines = t.split('\n')
    k = next(i for i, l in enumerate(lines) if l.startswith('| claim | class | source as printed (merged key) |'))
    lines[k] = lines[k].rstrip() + ' outcome (verify patch v2.3) |'
    lines[k + 1] = lines[k + 1].rstrip() + '---|'
    j = k + 2
    while j < len(lines) and lines[j].startswith('| E'):
        cid = lines[j].split('|')[1].strip()
        lines[j] = lines[j].rstrip() + ' %s |' % APPQ_OUT[cid]
        j += 1
    return '\n'.join(lines)

def keys_for_appendix(outline, app):
    part10 = re.findall(r'@\w+\{([^,]+),', open(os.path.join(SPEC, 'checks', 'refs_part10_v23.bib'), encoding='utf-8').read())
    lines = outline.split('\n')
    a = next(i for i, l in enumerate(lines) if l.startswith('## Appendix %s ' % app))
    b = next(i for i in range(a + 1, len(lines)) if lines[i].startswith('## '))
    body = '\n'.join(lines[a:b])
    return [k for k in part10 if '`%s`' % k in body]

def add_35(t):
    outline = src.TEXTS['FINAL_OUTLINE_v2.md']
    lines = t.split('\n')
    k = next(i for i, l in enumerate(lines) if l.startswith('**App Q (errata candidates; sources only)'))
    add = []
    for app, name in (('M', 'App M'), ('N', 'App N'), ('O', 'App O')):
        ks = keys_for_appendix(outline, app)
        add.append('**%s — keys added by the verify patch v2.3** (%d keys): %s' % (name, len(ks), ', '.join('`%s`' % x for x in ks)))
        add.append('')
    lines[k:k] = add
    return '\n'.join(lines)

def add_51(t):
    outline = src.TEXTS['FINAL_OUTLINE_v2.md']
    lines = t.split('\n')
    k = next(i for i, l in enumerate(lines) if l.startswith('Not found in INSPIRE (cite through textbooks instead):'))
    lines[k] = ('Not found in INSPIRE (cite through textbooks instead): D. Ruelle, Helv. Phys. Acta 35 (1962) 147 (Haag–Ruelle theory: use `Haag:1958vt`, `Jost:1965yxu`, `Streater:1989vi`); '
                'V. S. Vladimirov\'s monographs: the Mir 1979 edition is on neither INSPIRE nor Crossref; the Crossref-verified CRC 2002 monograph `Vladimirov2002` is in the bib since v2.3 (cite it with 「位置待核实」 until the location is checked).')
    sec = ['', '### 5.1 spec-v2.3 additions (verify patch; INSPIRE / Crossref) — 48 entries', '',
           'Fetched 2026-10-11 by `spec_v2/checks/fetch_additions_v23.py` (one INSPIRE hit per query; records and JSON in `spec_v2/checks/inspire_additions/`, log `fetch_additions_v23.log`) and three Crossref-verified manual entries; PART 10 of `refs_merged_v2.bib`, built by `checks/add_refs_v23.py`. Content depth: as documented in the verification records that cite them (`verify/claims/`, `verify/extend_reports/`); a key whose content was not read there is cited for its standard attribution only. **Not added** (verification failed): Bałaban, CMP 116 (1988) 1 (0 INSPIRE hits; not cited); Vladimirov, Mir 1979 (see above); Feichtner–Sturmfels, Port. Math. 62 (2005) 437 (math/0411260; 0 hits on INSPIRE and Crossref — the citing sentence of `lem:appM-matroid` cites `Schultka:2018nrs` §4 instead). Joglekar 1977 = the existing keys `Joglekar:1976eb`, `Joglekar:1976pe` (INSPIRE re-check).', ''] + section_51(outline)
    lines[k + 1:k + 1] = sec
    return '\n'.join(lines)

ROW0_OLD = '| | **total** | **1003** |'
ROW10 = '| 10 | spec-v2.3 verify-patch additions | 48 | 45 INSPIRE records (one hit per query, `spec_v2/checks/fetch_additions_v23.py`, log `fetch_additions_v23.log`) and 3 Crossref-verified manual entries (`Hormander2003`, `Vladimirov2002`, `NilssonPassare2013`); block built by `checks/add_refs_v23.py`; §5.1 |'

CHANGELOG = r'''

**2026-10-11 — spec v2.3 (spec patcher; verify patch).**
1. Bibliography: PART 10 with **48** verified additions (45 INSPIRE, 3 Crossref) → **1051** entries; `key_aliases_v2.tsv` +48 identity rows. Not added: Bałaban CMP 116 (1988) 1, Vladimirov (Mir 1979), Feichtner–Sturmfels (citing text changed). Test: BibTeX `unsrt` with `\nocite{*}`: 1051 entries, exit 0, 0 warnings, 0 errors; XeLaTeX with the common preamble: 0 errors, 0 missing glyphs, 0 overfull boxes, 61 pp. (`checks/bibtest/SUMMARY.txt`).
2. §1.4: CS-exponent, hybrid-kernel and one-jettiness warnings updated with the verification outcomes; §1.5: verdicts recorded (A04, A06, A11 corrected in single items; A20 wording per R-M20; A03, A07, A16, A17, A23 precisions).
3. §3.5: App M/N/O lists extended by the v2.3 keys; App Q table with the outcome column. §5.1: the v2.3 additions with query, purpose and the units that cite them.'''

OPS = [
 ('rep', ROW0_OLD, ROW10 + '\n| | **total** | **1051** |'),
 ('sub', '(59 pp.) — `spec_v2/checks/bibtest/SUMMARY.txt` (spec v2.1 rebuild; v2.0 with 998 entries gave the same results on 58 pp.)', '(61 pp.) — `spec_v2/checks/bibtest/SUMMARY.txt` (spec v2.3: 1051 entries; v2.1 with 1003 entries and v2.0 with 998 entries gave the same results on 59 and 58 pp.)', '| | **total** | **1051** |'),
 ('sub', '`Ji:2021znw` eqs. (49), (51), (73) print $e^{K\\ln(\\zeta_z/\\zeta)}$; the correct exponent is $\\frac12\\tilde K\\ln(\\zeta_z/\\zeta)$ (VF-LAM-15; App Q candidate, [PENDING-VERIFY]). Use the correct form silently until App Q is written.',
  'arXiv:2106.05310v1 of `Ji:2021znw` (eqs. (49), (51), (73)) print $e^{K\\ln(\\zeta_z/\\zeta)}$; the correct exponent is $\\frac12\\tilde K\\ln(\\zeta_z/\\zeta)$ (VF-LAM-15; App Q row Q.11). The journal version of `Ji:2021znw` (PRD 105 (2022) 076014) is correct and notes the omission in its footnote 1 — never list it among the sources with the error.',
  '- **CS exponent.**'),
 ('sub', '`Su:2022fiu` (NPB 991 (2023) 116201) has the correct form (VF-LAM-10).', '`Su:2022fiu` (NPB 991 (2023) 116201) has the correct form (VF-LAM-10); the first published correction is `Chou:2022drv` eq. (35) (App Q row Q.8).', '- **Hybrid kernel.**'),
 ('sub', 'single group, LL coherence-violation approximation; independent confirmation not yet available.', 'LL coherence-violation approximation; confirmed for the $qg\\to q$ channel in SCET with Glauber and new modes by `Becher:2026kbr` (two groups, different methods).', '- **`Banfi:2025mra`** (1-jettiness CVLs)'),
 ('sub', '(A01–A28; binding until the verify patch)', '(A01–A28; verdicts of the verify patch v2.3)', '### 1.5 New in v2.1: attribution rules'),
 ('sub', 'Until the verify patch records a verdict, every writer follows the rule in the second column; after the patch, the verdict replaces the rule (and this table is updated).', '**Verdicts (verify patch v2.3, `verify/CLAIM_VERDICTS.md`):** A01–A03, A05, A07–A10, A12–A28 confirmed — the rules stand, with the precisions written into the rows; A04, A06 and A11 refuted in single items — the rows are corrected; the A20 row follows the correction R-M20.', 'The claims register `verify/CLAIMS.md` (compiled 2026-10-10 by the verification workflow) lists 28'),
 ('sub', 'No priority words (「首次」「第一个」, "first") for results of the Liu programme until verify confirms each claim.', 'Priority words only in the printable forms of `verify/CLAIM_VERDICTS.md` A03 (confirmed), each with 「据我们所知（INSPIRE 检索，2026 年 10 月）」 — (A1) `Ji:2019sxk` time-independent soft factor; (A3) `Liu:2022nnk` classification (cusp-angle analyticity: `KorchemskyRadyushkin1987`); (A5) $S_I$ by JLL (precursor $g^S_q$: `EbertStewartZhao2019`); (A6) `Liu:2023pjb`; (B1) `Ji:2019ewn`; (C2) `Ji:2023pba` (earlier: `Gao:2021hxl`); (D1) `Liu:2024omb` (vacuum-correlator precedent `Beneke:1998eq`).', '| A03 |'),
 ('sub', '`Vladimirov:2020ofp` (one loop, SCET)', '`Vladimirov:2020ofp` (an SCET$_{\\rm II}$ derivation with a one-loop check — A04 corrected)', '| A04 |'),
 ('sub', 'The multiplicative-renormalizability proofs used are not Liu\'s.', 'The multiplicative-renormalizability proofs used are not Liu\'s. **A04 corrections (v2.3):** the APPB §4.4 remark that a detailed explanation beyond one loop "is not presented" concerns `Collins:2011ca` (APPB ref. [47]), not `CollinsSoper1981` (APPB App. D criticises the latter differently: a heuristic IR-safety argument with a loophole for linear divergences); `Ji:2018hvs` has five authors; cite the "open question" quote of `Vladimirov:2017ksc` from the JHEP version (p. 32).', '| A04 |'),
 ('sub', 'needs a repeated search at print time. Preprints are marked.', 'needs a repeated search at print time. Preprints are marked. **A06 corrections (v2.3):** item 3 is false — the N³LO non-singlet kernel exists (`Cheng:2024wyu`; used by `Ji:2024hit`); item 4 is false as stated — the Rossi–Testa resolution was contested in 2017–2018 with published exchanges on both sides (`Rossi:2018zkn`, `Rossi:2017muf`; replies `Karpie:2018zaz`, `Radyushkin:2018nbf`); the other items hold (item 8 not exhaustively; item 10 partially checked).', '| A06 |'),
 ('sub', 'present `Braun:2024snf` (abstract level) and `Su:2026eta` (preprint) side by side, no verdict;', 'present `Braun:2024snf` and `Su:2026eta` (preprint) side by side: not strictly contradictory (no leading-twist soft term vs a first-power correction), neither paper criticises the other (A07 confirmed);', '| A07 |'),
 ('sub', 'RS contain no $e^+e^-$-specific Glauber statement;', 'RS §10.1–10.3 do treat the $n$–$\\bar n$ production current at one and two loops (Glauber phases explicit in SCET$_{\\rm II}$, equal to the soft zero-bin, or carried by ultrasoft graphs in SCET$_{\\rm I}$) and expect the same at any order without proof — cite them for $e^+e^-$ only as one- and two-loop evidence (A11 item (3), corrected in v2.3);', '| A11 |'),
 ('sub', '(I–III; whether II covers non-abelian theories with ghosts is to be verified)', '(I–III; the hypotheses of II are met by massless QCD in covariant gauges including ghosts — BM name Yang–Mills with vector-like fermions, ghosts are not discussed explicitly; N24)', '| A16 |'),
 ('sub', 'Titchmarsh §5.81 and Boas Thm 9.2.1 (locations taken from a secondary source; check them if the books are accessible);', 'Titchmarsh §5.81 (verified in the book) and Boas Thm 9.2.1 (as cited by Waldschmidt);', '| A17 |'),
 ('sub', '`CataniDeFlorianRodrigo2012` do **not** show a cancellation ($P^{(2)}$ not factorized; "may invalidate … starting at the N³LO"); FSS: violation from three loops; GHMMS (`Guan:2024hlf`): cancels in pure QCD to NNLO;', '`CataniDeFlorianRodrigo2012` do **not** show a cancellation ($P^{(2)}$ not factorized; "may invalidate the factorization theorem of mass singularities starting at the N³LO" is their statement); FSS: in pure QCD the two-loop effect vanishes and a violation is expected at three loops (one step of that argument is not proven); the sentence of `Guan:2024hlf` that the effects "appear to cancel in pure-QCD cross sections up to NNLO" is a literature summary, not their result; in $\\mathcal N=4$ SYM the cancellation is shown by Henn et al. (PRD 112 (2025) 076003); never call a two-loop cancellation statement "wrong" (R-M20);', '| A20 |'),
 ('sub', 'The 21 "verify" items of REVIEW §11 (CLAIMS A23) stay hedged until verified.', 'A23 confirmed: the theory class of `Anikin:1978tj` is open (never cite it as a QCD proof); `Lowenstein:1974qt` (BPHZL, massless $A^4$, Goldstone and pre-Higgs models) does not cover gauge-fixed QCD; `Frye:2018xjj`: a sum over initial **or** final states suffices; `Gaunt2014`: shown vs suggested (E36); `AybatSterman2009`: an outline, not a proof; the other items as in `verify/CLAIM_VERDICTS.md` A23.', '| A23 |'),
 ('func', add_35),
 ('func', appq_outcomes),
 ('func', add_51),
 ('func', lambda t: t.rstrip('\n') + CHANGELOG + '\n'),
]
