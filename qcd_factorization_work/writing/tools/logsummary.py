#!/usr/bin/env python3
r"""logsummary.py -- summary of a XeLaTeX log of the book (used by build/build.sh).

    python3 -I logsummary.py --log build/qcd_factorization.log [--aux build/qcd_factorization.aux]
            [--src build/src] [--outline spec_v2/FINAL_OUTLINE_v2.md] [--register spec_v2/ASSUMPTIONS.md]
            [--out build/build_summary.txt] [--max 25]

Run xelatex with max_print_line=100000 so that the log lines are not wrapped (file names in the log are then intact).
The file stack is reconstructed from the parentheses of the log; the contents of overfull/underfull boxes and the
context lines of errors are skipped, so that their unbalanced parentheses cannot corrupt the stack.

Reported: LaTeX errors (file, line, message); undefined references and citations grouped by unit, the references
classified with the registry as 'expected' (canonical label of a unit not present), 'owner present' (canonical label
missing although its unit is present) or 'unknown' (not in the registry); multiply defined labels with the files that
define them; overfull boxes > 1 pt with file and line; missing characters; the page count; the page counts of App P and
App Q from the .aux.  Exit code 1 if the log contains LaTeX errors.
"""
import os, re, sys, argparse, collections
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import booklib as B

FILE_RE = re.compile(r'(?:\.{1,2}/|/)?[^\s()\[\]{}"<>]+?\.(?:tex|sty|cls|cfg|def|clo|fd|aux|toc|lof|lot|bbl|out|ldf|dict|'
                     r'ltx|ini|cnf|map|enc|otf|ttf|pfb|lua|tikz|bst|code\.tex)(?=[\s()]|$)')


def classify(label, registry, register, present):
    if registry is None:
        return 'unclassified'
    if label in B.GENERATED_LABELS or label in ('app:appP',):
        return 'generated'
    owner = registry.owner.get(label) or registry.optional_owner.get(label)
    if owner is None:
        a = register.get(label) or registry.asm.get(label)
        if a:
            owner = a.get('owner')
    if owner is None:
        for u, cl in B.CHAPTER_LABEL.items():
            if cl == label:
                owner = u
    if owner is None:
        return 'unknown'
    return 'owner present' if owner in present else 'expected'


def main():
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument('--log', required=True)
    ap.add_argument('--aux', default=None)
    ap.add_argument('--src', default=None)
    ap.add_argument('--outline', default=None)
    ap.add_argument('--register', default=None)
    ap.add_argument('--out', default=None)
    ap.add_argument('--max', type=int, default=25, help='maximum items listed per group')
    a = ap.parse_args()
    if not os.path.exists(a.log):
        sys.exit('logsummary: %s not found' % a.log)
    log = B.read_text(a.log)
    builddir = os.path.dirname(os.path.abspath(a.log))
    lines = log.split('\n')
    stack = []
    errors, undef_ref, undef_cite, multi, overfull, missing = [], [], [], [], [], []
    other = collections.Counter()

    def cur_file():
        for f in reversed(stack):
            if f and f.endswith('.tex'):
                return f
        return '?'
    skip = False
    i = 0
    while i < len(lines):
        line = lines[i]
        if skip:
            if not line.strip():
                skip = False
            i += 1
            continue
        m = re.match(r'^(Overfull|Underfull) \\([hv])box \(([\d.]+)pt (too wide|too high)\) (?:in paragraph|in alignment|detected|has occurred)'
                     r'(?: at lines? (\d+)(?:--(\d+))?)?', line)
        if m:
            if m.group(1) == 'Overfull':
                overfull.append((float(m.group(3)), cur_file(), m.group(5) or '?', m.group(2)))
            skip = True
            i += 1
            continue
        if line.startswith('! '):
            msg = line[2:].strip()
            ln = '?'
            for j in range(i + 1, min(i + 30, len(lines))):
                mm = re.match(r'^l\.(\d+)', lines[j])
                if mm:
                    ln = mm.group(1)
                    break
            errors.append((cur_file(), ln, msg))
            skip = True
            i += 1
            continue
        m = re.search(r'LaTeX Warning: Reference `([^\']*)\' on page (\S+) undefined on input line (\d+)', line)
        if m:
            undef_ref.append((m.group(1), cur_file(), m.group(3)))
        m = re.search(r'LaTeX Warning: Citation `([^\']*)\' on page (\S+) undefined on input line (\d+)', line)
        if m:
            undef_cite.append((m.group(1), cur_file(), m.group(3)))
        m = re.search(r'LaTeX Warning: Label `([^\']*)\' multiply defined', line)
        if m and not m.group(1).endswith('@cref'):
            multi.append(m.group(1))
        m = re.search(r'Missing character: There is no (.+?) in font ([^!]+)!', line)
        if m:
            missing.append((m.group(1), m.group(2).split(':')[0], cur_file()))
        if 'Font shape' in line and 'undefined' in line:
            other['font shape undefined'] += 1
        if 'Rerun to get' in line or 'Label(s) may have changed' in line:
            other['rerun requested'] += 1
        if 'Package hyperref Warning' in line:
            other['hyperref warnings'] += 1
        # parentheses -> file stack
        j = 0
        while j < len(line):
            c = line[j]
            if c == '(':
                mm = FILE_RE.match(line, j + 1)
                if mm:
                    name = mm.group(0)
                    stack.append(name)
                    j = mm.end()
                    continue
                stack.append(None)
            elif c == ')':
                if stack:
                    stack.pop()
            j += 1
        i += 1
    m = re.search(r'Output written on (\S+) \((\d+) pages?', log)
    pages = int(m.group(2)) if m else None
    # registry, present units
    registry = B.read_outline(a.outline) if a.outline and os.path.exists(a.outline) else None
    register = B.read_register(a.register) if a.register else {}
    present = set()
    defs = collections.defaultdict(list)
    if a.src and os.path.isdir(a.src):
        for f in sorted(os.listdir(a.src)):
            if f.endswith('.tex'):
                if f in B.FILE_UNIT:
                    present.add(B.FILE_UNIT[f])
                st, _ = B.strip_comments(B.read_text(os.path.join(a.src, f)))
                for mm in B.LABEL_RE.finditer(st):
                    defs[mm.group(1).strip()].append('%s:%d' % (f, st.count('\n', 0, mm.start()) + 1))
    appdir = os.path.join(builddir, 'appP')
    if os.path.isdir(appdir):
        for f in sorted(os.listdir(appdir)):
            if f.endswith('.tex'):
                st, _ = B.strip_comments(B.read_text(os.path.join(appdir, f)))
                for mm in B.LABEL_RE.finditer(st):
                    defs[mm.group(1).strip()].append('appP/%s' % f)

    def unit_of_file(f):
        b = os.path.basename(f)
        return B.FILE_UNIT.get(b, b)
    out = []
    w = out.append
    w('== LaTeX log summary: %s' % a.log)
    w('pages: %s' % (pages if pages is not None else 'n/a (no PDF written)'))
    if a.aux and os.path.exists(a.aux):
        aux = B.parse_aux(a.aux)

        def pg(l):
            v = aux.get(l)
            try:
                return int(v[1]) if v else None
            except ValueError:
                return None
        p, q, e, bib = pg('app:appP'), pg('app:appQ'), pg('appP:end'), pg('book:bibstart')
        appP = (q - p) if (p is not None and q is not None) else ((e - p + 1) if (p is not None and e is not None) else None)
        appQ = (bib - q) if (q is not None and bib is not None) else None
        w('App P: %s pages%s; App Q: %s pages' % (appP if appP is not None else 'n/a',
                                                  ' (pp. %s-%s)' % (p, (q - 1) if q else e) if appP is not None else '',
                                                  appQ if appQ is not None else 'n/a'))
    w('LaTeX errors: %d' % len(errors))
    for (f, ln, msg) in errors[:a.max]:
        w('  %s:%s: %s' % (f, ln, msg))
    # undefined references
    labs = collections.OrderedDict()
    for (lab, f, ln) in undef_ref:
        labs.setdefault(lab, []).append((f, ln))
    cls = collections.Counter()
    byunit = collections.defaultdict(lambda: collections.defaultdict(list))
    for lab, occ in labs.items():
        k = classify(lab.strip(), registry, register, present)
        if lab != lab.strip():
            k = 'spaces in a label list'
        cls[k] += 1
        for (f, ln) in occ:
            byunit[unit_of_file(f)][k].append((lab, ln))
    w('undefined references: %d distinct labels (%d occurrences)%s' % (
        len(labs), len(undef_ref), '; ' + ', '.join('%s %d' % (k, v) for k, v in sorted(cls.items())) if cls else ''))
    if cls.get('spaces in a label list'):
        w('  NOTE: labels with a leading space come from \\cref{a, b} / \\uses lists with spaces or line breaks '
          '(cleveref does not trim them); run figsync.py --normalize-refs or remove the spaces.')
    for u in sorted(byunit, key=lambda x: B.UNIT_INDEX.get(x, 99)):
        parts = []
        for k, lst in sorted(byunit[u].items()):
            parts.append('%s %d' % (k, len(set(l for l, _ in lst))))
        w('  %-22s %s' % (u, ', '.join(parts)))
        for k in ('owner present', 'unknown', 'generated', 'spaces in a label list', 'unclassified'):
            lst = byunit[u].get(k, [])
            seen = []
            for (lab, ln) in lst:
                if lab not in [x for x, _ in seen]:
                    seen.append((lab, ln))
            for (lab, ln) in seen[:a.max]:
                w('      [%s] %s (line %s)' % (k, lab, ln))
            if len(seen) > a.max:
                w('      ... %d more' % (len(seen) - a.max))
    # citations
    cites = collections.defaultdict(list)
    for (key, f, ln) in undef_cite:
        cites[unit_of_file(f)].append((key, ln))
    w('undefined citations: %d distinct keys (%d occurrences)' % (len(set(k for k, _, _ in undef_cite)), len(undef_cite)))
    for u in sorted(cites, key=lambda x: B.UNIT_INDEX.get(x, 99)):
        ks = []
        for k, ln in cites[u]:
            if k not in [x for x, _ in ks]:
                ks.append((k, ln))
        w('  %-22s %s' % (u, ', '.join('%s (l.%s)' % x for x in ks[:a.max]) + (' ...' if len(ks) > a.max else '')))
    # multiply defined
    md = B.dedupe(multi)
    w('multiply defined labels: %d' % len(md))
    for lab in md[:a.max]:
        w('  %s: %s' % (lab, ', '.join(defs.get(lab, ['?']))))
    # overfull boxes
    big = [o for o in overfull if o[0] > 1.0]
    w('overfull boxes > 1pt: %d (all overfull: %d)' % (len(big), len(overfull)))
    byf = collections.defaultdict(list)
    for (amt, f, ln, hv) in big:
        byf[f].append((amt, ln, hv))
    for f in sorted(byf):
        lst = sorted(byf[f], key=lambda x: -x[0])
        w('  %s: %s' % (f, ', '.join('l.%s %.1fpt%s' % (ln, amt, '' if hv == 'h' else '(v)') for amt, ln, hv in lst[:a.max])
                        + (' ...' if len(lst) > a.max else '')))
    # missing characters
    mc = collections.Counter((ch, font, f) for (ch, font, f) in missing)
    w('missing characters: %d' % len(missing))
    for (ch, font, f), n in sorted(mc.items(), key=lambda kv: -kv[1])[:a.max]:
        w('  %s in %s (%s) x%d' % (ch, font, f, n))
    if other:
        w('other: ' + ', '.join('%s %d' % (k, v) for k, v in sorted(other.items())))
    txt = '\n'.join(out) + '\n'
    if a.out:
        with open(a.out, 'w', encoding='utf-8') as fh:
            fh.write(txt)
    sys.stdout.write(txt)
    sys.exit(1 if errors else 0)


if __name__ == '__main__':
    main()
