#!/usr/bin/env python3
r"""Test runner for the integration tools on the synthetic mini-book (build/test_synth/).

    python3 -I build/test_synth/run_tests.py [--skip-build]

Runs figsync (dry run and --apply into a scratch copy), bibmerge, check_book, the full build/build.sh on the synthetic
book, blueprint_gen twice (determinism) and once without ch25 (master-table fallback), and asserts that every
deliberate error of the synthetic units (marked "DELIBERATE" in the sources) is reported by the intended check, that
the synthetic chapters directory is never modified, and that the build has 0 LaTeX errors.  Prints PASS/FAIL per
expectation; exit code 1 if any expectation fails.
"""
import os, re, sys, json, shutil, hashlib, subprocess, tempfile, filecmp

HERE = os.path.dirname(os.path.abspath(__file__))
W = os.path.dirname(os.path.dirname(HERE))
TOOLS = os.path.join(W, 'writing', 'tools')
CH = os.path.join(HERE, 'chapters')
SPEC = os.path.join(HERE, 'spec')
OUTLINE = os.path.join(SPEC, 'FINAL_OUTLINE_synth.md')
REGISTER = os.path.join(SPEC, 'ASSUMPTIONS_synth.md')
BUILD = os.path.join(HERE, 'build')
BIB = os.path.join(W, 'spec_v2', 'refs_merged_v2.bib')
results = []


def run(args, **kw):
    r = subprocess.run(args, stdout=subprocess.PIPE, stderr=subprocess.STDOUT, **kw)
    return r.returncode, r.stdout.decode('utf-8', 'replace')


def expect(name, cond, detail=''):
    results.append((name, bool(cond), detail))


def tree_hash(d):
    h = hashlib.sha1()
    for f in sorted(os.listdir(d)):
        h.update(f.encode())
        with open(os.path.join(d, f), 'rb') as fh:
            h.update(fh.read())
    return h.hexdigest()


def has_finding(findings, check, label=None, sev=None, text=None):
    for f in findings:
        if f['check'] != check:
            continue
        if label and f.get('label') != label and label not in (f.get('msg') or ''):
            continue
        if sev and f['sev'] != sev:
            continue
        if text and text not in f['msg']:
            continue
        return True
    return False


def main():
    skip_build = '--skip-build' in sys.argv
    py = [sys.executable, '-I']
    h0 = tree_hash(CH)
    # ---------------------------------------------------------------- figsync
    rc, out = run(py + [os.path.join(TOOLS, 'figsync.py'), '--chapters', CH, '--root', HERE, '--normalize-refs'])
    expect('figsync dry run: exit 0', rc == 0, out[-300:])
    expect('figsync: DIFFERS fig:synth-changed (old caption)', re.search(r'DIFFERS\s+fig:synth-changed', out))
    expect('figsync: REMOVED fig:appP-dependency (generated graph)', re.search(r'REMOVED\s+fig:appP-dependency', out))
    expect('figsync: NOSOURCE fig:synth-nosource', re.search(r'NOSOURCE\s+fig:synth-nosource', out))
    expect('figsync: DUPLICATE fig:synth-same', re.search(r'DUPLICATE\s+fig:synth-same', out))
    expect('figsync: label list with spaces normalised in ch07', re.search(r'REFLISTS.*ch07_dis.tex: 1 label list', out))
    expect('figsync: dry run writes nothing', 'dry run: nothing written' in out)
    tmp = tempfile.mkdtemp(prefix='figsync_')
    try:
        rc, out = run(py + [os.path.join(TOOLS, 'figsync.py'), '--chapters', CH, '--root', HERE, '--apply', '--out', tmp,
                            '--normalize-refs'])
        c07 = open(os.path.join(tmp, 'ch07_dis.tex'), encoding='utf-8').read()
        cP = open(os.path.join(tmp, 'appP_blueprint.tex'), encoding='utf-8').read()
        expect('figsync --apply: copy carries the corrected caption', '图源中已更正的图题' in c07 and '旧图题' not in c07)
        expect('figsync --apply: generated graph block removed from the copy', 'figsync: block fig:appP-dependency removed' in cP)
        expect('figsync --apply: \\cref list normalised in the copy', '\\cref{thm:dis-ope,thm:dis-moments}' in c07)
        rc2, out2 = run(py + [os.path.join(TOOLS, 'figsync.py'), '--chapters', CH, '--root', HERE, '--apply', '--out', CH])
        expect('figsync refuses to write into the chapters directory', rc2 != 0 and 'refusing' in out2)
    finally:
        shutil.rmtree(tmp, ignore_errors=True)
    # ---------------------------------------------------------------- bibmerge
    tmpb = tempfile.mkdtemp(prefix='bibmerge_')
    try:
        rc, out = run(py + [os.path.join(TOOLS, 'bibmerge.py'), '--base', BIB, '--additions', CH, '--aliases',
                            os.path.join(W, 'spec_v2', 'key_aliases_v2.tsv'), '--out', os.path.join(tmpb, 'refs_final.bib')])
        expect('bibmerge: exit 0 and bibtex test without errors', rc == 0 and '0 error(s)' in out, out[:400])
        expect('bibmerge: identical duplicate Collins2011 dropped', re.search(r'SAME\s+Collins2011', out))
        expect('bibmerge: conflicting duplicate Collins2023 (base wins)', re.search(r'CONFLICT\s+Collins2023.*year', out))
        expect('bibmerge: conflicting duplicate between additions Synth:2026abc', re.search(r'CONFLICT\s+Synth:2026abc', out))
        expect('bibmerge: alias key Sterman:1993hfp reported', re.search(r'ALIAS\s+Sterman:1993hfp.*Sterman1993', out))
        expect('bibmerge: same DOI under different keys reported', re.search(r'SAME-DOI\s+10\.1017/cbo9780511975592', out))
        merged = open(os.path.join(tmpb, 'refs_final.bib'), encoding='utf-8').read()
        expect('bibmerge: merged file has the new entry once', merged.count('@article{Synth:2026abc') == 1)
    finally:
        shutil.rmtree(tmpb, ignore_errors=True)
    # ---------------------------------------------------------------- check_book
    cb = os.path.join(HERE, 'check_book.txt')
    rc, out = run(py + [os.path.join(TOOLS, 'check_book.py'), '--chapters', CH, '--outline', OUTLINE, '--register', REGISTER,
                        '--bib', BIB, '--out', cb])
    rep = open(cb, encoding='utf-8').read()
    kexp = [('K1', 'fig:synth-same defined 2 times'), ('K2', 'withdrawn slot label thm:appN-oneloop'),
            ('K2', 'equation label eq:dis-foreign'), ('K2', 'canonical labels of units not yet written (Ch05 1)'),
            ('K3', 'prop:dis-missing'), ('K3', 'prop:dy-misplaced is owned by Ch07'), ('K3', 'asm:appN-missing'),
            ('K4', 'lem:dis-forward uses thm:dy-factorization of the later unit'), ('K4', 'dependency cycle'),
            ('K4', 'hidden forward dependency: lem:dis-hidden'), ('K5', 'prop:dis-weakened: [P] vs registry [A] -- weakened'),
            ('K5', 'prop:dis-strengthened: [A] vs registry [P] -- strengthened'), ('K5', 'asm:appN-wrongtag'),
            ('K6', 'prop:dis-notverbatim'), ('K7', 'thm:appN-noprem'), ('K7', 'prop:appN-late'),
            ('K8', 'conj:dy-coloured'), ('K8', 'prop:dy-late'), ('K9', '文献待补'), ('K10', 'prop:dy-forbidden'),
            ('K11', 'factorization'), ('K12', 'thm:dis-ope, thm:dis-moments'), ('K13', 'lem:dis-twouses'),
            ('K13', 'thm:dis-nouses'), ('K13', 'sec:dis-kin'), ('K14', 'asm:appN-wrongtag'), ('K15', 'NoSuchKey2099')]
    sections = {}
    for m in re.finditer(r'^-- (K\d+) .*?(?=^-- K\d+ |\Z)', rep, re.M | re.S):
        sections[m.group(1)] = m.group(0)
    for k, txt in kexp:
        expect('check_book %s: %s' % (k, txt), txt in sections.get(k, ''))
    # ---------------------------------------------------------------- full build
    if not skip_build:
        rc, out = run(['bash', os.path.join(W, 'build', 'build.sh'), '--chapters', CH, '--builddir', BUILD,
                       '--outline', OUTLINE, '--register', REGISTER, '--figroot', HERE])
        expect('build.sh: exit 0 (no LaTeX errors)', rc == 0, out[-800:])
    summ = open(os.path.join(BUILD, 'build_summary.txt'), encoding='utf-8').read()
    expect('build summary: 0 LaTeX errors', 'LaTeX errors: 0' in summ)
    expect('build summary: undefined citation NoSuchKey2099 reported', 'NoSuchKey2099' in summ)
    expect('build summary: multiply defined fig:synth-same reported', 'fig:synth-same: ch07_dis.tex' in summ)
    expect('build summary: no label list with spaces left (normalised copy)', 'spaces in a label list' not in summ)
    expect('build summary: App P page count read from the aux', re.search(r'App P: \d+ pages', summ))
    for g in ['appP_register.tex', 'appP_status.tex', 'appP_uses.tex', 'appP_checks.tex'] + \
            ['appP_graph_%s.tex' % x for x in 'abcdefgh']:
        expect('generated %s exists' % g, os.path.exists(os.path.join(BUILD, 'appP', g)))
    aux = open(os.path.join(BUILD, 'qcd_factorization.aux'), encoding='utf-8', errors='replace').read()
    for lab in ['sec:appP-status', 'sec:appP-uses', 'sec:appP-graphs', 'sec:appP-checks', 'tab:appP-register',
                'tab:appP-status', 'tab:appP-uses', 'tab:appP-checks', 'fig:appP-dependency'] + \
               ['fig:appP-dependency-%s' % x for x in 'bcdefgh']:
        expect('label %s defined in the book' % lab, '\\newlabel{%s}' % lab in aux)
    js = json.load(open(os.path.join(BUILD, 'appP', 'blueprint.json'), encoding='utf-8'))
    F = js['findings']
    cexp = [('C-P0', 'lem:dis-brackets', 'W', None), ('C-P0', 'def:dis-latelabel', 'W', None), ('C-P0', None, 'W', 'unlabelled remark'),
            ('C-P1', 'lem:dis-twouses', 'E', None), ('C-P1', 'thm:dis-nouses', 'E', None), ('C-P1', 'ex:dis-seclabel', 'E', None),
            ('C-P1', 'rem:dis-tagged', 'W', None),
            ('C-P2', 'prop:dis-missing', 'E', None), ('C-P2', 'prop:dy-misplaced', 'E', None), ('C-P2', 'asm:appN-missing', 'E', None),
            ('C-P2', 'prop:dis-weakened', 'W', None), ('C-P2', 'prop:dis-strengthened', 'E', None),
            ('C-P2', 'asm:appN-wrongtag', 'E', None),
            ('C-P3', 'lem:dis-forward', 'E', None), ('C-P3', 'lem:appN-cyc-a', 'E', None), ('C-P3', 'lem:dis-hidden', 'W', None),
            ('C-P4', 'lem:appN-cyc-a', 'E', None),
            ('C-P5', 'lem:dis-forward', 'E', None), ('C-P5', 'prop:dy-ctech', 'E', None),
            ('C-P6', 'thm:dis-usesv', 'E', None),
            ('C-P7', 'prop:dis-rdef', 'E', None), ('C-P7', 'prop:dis-notverbatim', 'E', None), ('C-P7', 'asm:appN-values', 'I', None),
            ('C-P8', 'thm:appN-structure', 'E', 'asm:appN-wrongtag'), ('C-P8', 'thm:appN-structure', 'E', 'lem:appN-cyc-a'),
            ('C-P8', 'thm:appN-noprem', 'E', None), ('C-P8', 'prop:appN-late', 'E', None),
            ('C-P9', 'asm:appN-unused', 'E', None),
            ('C-P10', 'asm:appN-collins', 'W', None),
            ('C-P11', 'thm:dis-nonexistent', 'E', None), ('C-P11', 'thm:dis-ope', 'E', None),
            ('C-P12', 'fig:synth-same', 'E', None), ('C-P12', 'sec:appP-register', 'E', None),
            ('C-P12', 'sec:appP-register', 'W', 'heading omitted'),
            ('C-P13', None, 'W', 'pending-verification comment'), ('C-P13', 'thm:appN-oneloop', 'W', None),
            ('C-P14', 'prop:dy-model', 'W', None),
            ('C-P15', 'prop:dy-npline', 'E', None), ('C-P15', 'prop:dy-hadron', 'E', None),
            ('C-P16', 'conj:dy-coloured', 'E', None), ('C-P16', 'prop:dy-late', 'W', None), ('C-P16', 'prop:method-gapless', 'W', None),
            ('C-P17', 'prop:method-gapless', 'W', None)]
    for (ck, lab, sev, txt) in cexp:
        expect('blueprint %s %s [%s]%s' % (ck, lab or '', sev, (' "%s"' % txt) if txt else ''), has_finding(F, ck, lab, sev, txt))
    expect('blueprint: no C-P17 finding for lem:method-relay (passes through lem:method-ward-multi)',
           not has_finding(F, 'C-P17', 'lem:method-relay'))
    expect('blueprint: master table read from ch25_summary.tex', js['meta']['master_source'] == 'ch25_summary.tex')
    node = dict((n['label'], n) for n in js['nodes'])
    expect('content grade thm:appN-structure = C (named gap premise)', node['thm:appN-structure']['content_grade'] == 'C')
    expect('content grade thm:dis-moments = A (R_OPE)', node['thm:dis-moments']['content_grade'] == 'A')
    expect('bottleneck thm:dy-factorization = [asm:appN-collins]', node['thm:dy-factorization']['bottleneck'] == ['asm:appN-collins'])
    expect('errtype read from the comment (thm:dy-factorization E-N)', node['thm:dy-factorization']['errtype'] == 'E-N')
    # ---------------------------------------------------------------- determinism, fallback
    d1, d2, d3 = (tempfile.mkdtemp(prefix='bp%d_' % i) for i in range(3))
    try:
        base = py + [os.path.join(TOOLS, 'blueprint_gen.py'), '--root', BUILD, '--master', 'qcd_factorization.tex',
                     '--aux', 'qcd_factorization.aux', '--outline', OUTLINE, '--register', REGISTER, '--level', '2']
        run(base + ['--out', d1])
        run(base + ['--out', d2])
        same = all(filecmp.cmp(os.path.join(d1, f), os.path.join(d2, f), shallow=False) for f in sorted(os.listdir(d1)))
        expect('blueprint_gen output is deterministic (two runs, all files identical)', same)
        m = open(os.path.join(BUILD, 'qcd_factorization.tex'), encoding='utf-8').read()
        m2 = m.replace('\\input{src/ch25_summary.tex}', '% ch25 removed for the fallback test')
        with open(os.path.join(BUILD, 'master_noch25.tex'), 'w', encoding='utf-8') as fh:
            fh.write(m2)
        rc, out = run(py + [os.path.join(TOOLS, 'blueprint_gen.py'), '--root', BUILD, '--master', 'master_noch25.tex',
                            '--outline', OUTLINE, '--register', REGISTER, '--out', d3, '--stub'])
        js3 = json.load(open(os.path.join(d3, 'blueprint.json'), encoding='utf-8'))
        expect('master-table fallback to FINAL_OUTLINE §09 when ch25 is absent',
               js3['meta']['master_source'].startswith('FINAL_OUTLINE_v2 §09'))
        expect('--stub mode writes placeholder files', 'refstepcounter{table}\\label{tab:appP-status}' in
               open(os.path.join(d3, 'appP_status.tex'), encoding='utf-8').read())
        rc, out = run(py + [os.path.join(TOOLS, 'blueprint_gen.py'), '--root', BUILD, '--master', 'qcd_factorization.tex',
                            '--outline', OUTLINE, '--register', REGISTER, '--out', d3, '--stub', '--final'])
        js4 = json.load(open(os.path.join(d3, 'blueprint.json'), encoding='utf-8'))
        expect('--final turns C-P13 into errors', has_finding(js4['findings'], 'C-P13', None, 'E') and rc == 1)
    finally:
        for d in (d1, d2, d3):
            shutil.rmtree(d, ignore_errors=True)
        try:
            os.remove(os.path.join(BUILD, 'master_noch25.tex'))
        except OSError:
            pass
    expect('synthetic chapters directory unchanged by all tools', tree_hash(CH) == h0)
    # ---------------------------------------------------------------- report
    npass = sum(1 for r in results if r[1])
    for name, ok, detail in results:
        print('%s  %s%s' % ('PASS' if ok else 'FAIL', name, ('' if ok or not detail else '\n      ' + detail.replace('\n', '\n      '))))
    print('\n%d of %d expectations passed' % (npass, len(results)))
    sys.exit(0 if npass == len(results) else 1)


if __name__ == '__main__':
    main()
