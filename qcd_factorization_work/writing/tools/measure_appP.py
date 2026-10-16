#!/usr/bin/env python3
r"""measure_appP.py -- page count of Appendix P for a given set of generated files, without compiling the book.

    python3 -I measure_appP.py --build build --appP build/appP [--aux build/qcd_factorization.aux]
            [--src build/src] [--work build/measure_appP] [--keep]

Builds a standalone document in --work: the preamble, longtable, all \newlabel entries of the book's .aux (so that
printed numbers, and hence column widths, are those of the book; labels defined by App P itself are left out),
\appendix, App P's written introduction (src/appP_blueprint.tex, or the fallback heading of make_master.py) and the
generated files; compiles it twice with xelatex and prints the number of pages ("APPP_PAGES <n>").  Used by build.sh
to choose the lowest compaction level of blueprint_gen.py that fits the 10-page budget (FINAL_OUTLINE_v2 App P §P.7);
the authoritative count is then read from the book's .aux after the full build.
"""
import os, re, sys, shutil, argparse, subprocess
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import booklib as B

GENERATED = ['appP_register.tex', 'appP_status.tex', 'appP_uses.tex'] + ['appP_graph_%s.tex' % g for g in 'abcdefgh'] + \
            ['appP_checks.tex']


def main():
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument('--build', required=True, help='build directory (contains preamble_fact.tex)')
    ap.add_argument('--appP', required=True, help='directory with the generated App P files')
    ap.add_argument('--aux', default=None)
    ap.add_argument('--src', default=None, help='directory with the unit files (for appP_blueprint.tex)')
    ap.add_argument('--work', default=None)
    ap.add_argument('--keep', action='store_true')
    a = ap.parse_args()
    work = a.work or os.path.join(a.build, 'measure_appP')
    if os.path.isdir(work):
        shutil.rmtree(work)
    os.makedirs(os.path.join(work, 'appP'))
    shutil.copy(os.path.join(a.build, 'preamble_fact.tex'), work)
    own = set(B.GENERATED_LABELS) | {'app:appP', 'appP:end'}
    intro = None
    if a.src and os.path.exists(os.path.join(a.src, 'appP_blueprint.tex')):
        intro = B.read_text(os.path.join(a.src, 'appP_blueprint.tex'))
        own |= set(m.group(1) for m in B.LABEL_RE.finditer(B.strip_comments(intro)[0]))
        with open(os.path.join(work, 'appP_blueprint.tex'), 'w', encoding='utf-8') as f:
            f.write(intro)
    for g in GENERATED:
        p = os.path.join(a.appP, g)
        if os.path.exists(p):
            shutil.copy(p, os.path.join(work, 'appP', g))
    lab = []
    if a.aux and os.path.exists(a.aux):
        t = B.read_text(a.aux)
        for line in t.split('\n'):
            m = re.match(r'\\newlabel\{([^}]*)\}', line)
            if m:
                l = m.group(1)
                if l.endswith('@cref'):
                    l = l[:-5]
                if l not in own:
                    lab.append(line)
    with open(os.path.join(work, 'labels.tex'), 'w', encoding='utf-8') as f:
        f.write('\n'.join(lab) + '\n')
    L = ['\\input{preamble_fact.tex}', '\\usepackage{longtable}',
         '\\makeatletter\\input{labels.tex}\\makeatother   % \\newlabel is a preamble-only command',
         '\\begin{document}', '\\appendix', '\\setcounter{chapter}{15}']
    if intro is not None:
        L.append('\\input{appP_blueprint.tex}')
    else:
        L.append('\\chapter{形式化蓝图：假设登记表、依赖图与状态表}\\label{app:appP}')
    for g in GENERATED:
        L.append('\\InputIfFileExists{appP/%s}{}{}' % g)
    L.append('\\end{document}')
    with open(os.path.join(work, 'measure.tex'), 'w', encoding='utf-8') as f:
        f.write('\n'.join(L) + '\n')
    env = dict(os.environ, max_print_line='100000')
    pages = None
    for _ in range(2):
        subprocess.run(['xelatex', '-interaction=nonstopmode', '-halt-on-error', 'measure.tex'], cwd=work, env=env,
                       stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
    log = B.read_text(os.path.join(work, 'measure.log')) if os.path.exists(os.path.join(work, 'measure.log')) else ''
    m = re.search(r'Output written on measure\.pdf \((\d+) page', log)
    if m:
        pages = int(m.group(1))
    errs = len(re.findall(r'^! ', log, re.M))
    print('APPP_PAGES %s' % (pages if pages is not None else 'n/a'))
    if errs:
        print('measure_appP: %d LaTeX errors in the standalone App P document (%s)' % (errs, os.path.join(work, 'measure.log')))
    if not a.keep and pages is not None and not errs:
        shutil.rmtree(work, ignore_errors=True)
    sys.exit(0 if pages is not None and not errs else 1)


if __name__ == '__main__':
    main()
