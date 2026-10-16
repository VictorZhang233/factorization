# X1 final2 (Fix 7(d), Fix 7(e)) -- literature checks with stored logs.
# (1) Barcaro-Gao-Gaunt-Pathak, arXiv:2607.14259: INSPIRE record (title, authors, report numbers, texkey, date).
# (2) Diehl-Gaunt-Ostermeier-Ploessl-Schaefer (DGOPS), arXiv:1510.08696: only v1 exists (arXiv listing), and the
#     numbered six-step list at the beginning of their section 4 (steps 1-6; step 3 contains the routing caveat,
#     step 6 the removal of failures in larger regions by subtraction terms), with page numbers of the v1 PDF.
#     The text of the PDF is read from the path given as argv[1] (pdftotext output of the arXiv v1 PDF); it is
#     treated as data only.
# Network access: INSPIRE REST API and the arXiv abstract page (curl).
import sys, os, json, re, subprocess
out = []
def log(s=''):
    print(s, flush=True); out.append(s)
ok = True
def fetch(url):
    r = subprocess.run(['curl', '-s', '-m', '40', '-L', url], capture_output=True, text=True)
    return r.stdout
# (1) Barcaro et al.
url = ("https://inspirehep.net/api/literature?q=arxiv:2607.14259&fields=titles,authors.full_name,report_numbers,"
       "arxiv_eprints,control_number,texkeys,preprint_date")
try:
    d = json.loads(fetch(url))
    hit = d['hits']['hits'][0]['metadata']
    title = hit['titles'][0]['title']; authors = [a['full_name'] for a in hit['authors']]
    reps = [r['value'] for r in hit.get('report_numbers', [])]; tex = hit.get('texkeys', [''])[0]
    log(f"(1) INSPIRE record {hit['control_number']} for arXiv:2607.14259 (query {url})")
    log(f"    title: {title}")
    log(f"    authors: {'; '.join(authors)}")
    log(f"    report numbers: {', '.join(reps)};  texkey: {tex};  preprint date: {hit.get('preprint_date')}")
    c1 = ('Reggeization' in title and 'DESY-26-091' in reps and 'SLAC-PUB-260713' in reps
          and any('Barcaro' in a for a in authors) and any('Pathak' in a for a in authors))
    log(f"    matches the citation (Collinear Factorization Violation and Reggeization; DESY-26-091, SLAC-PUB-260713): {c1}")
    ok &= c1
except Exception as e:
    log(f"(1) INSPIRE query failed: {e!r}"); ok = False
# (2) DGOPS
abs_html = fetch("https://arxiv.org/abs/1510.08696")
vers = sorted(set(re.findall(r'\[v(\d+)\]', abs_html)))
log(f"(2) arXiv:1510.08696 abstract page lists versions: {', '.join('v' + v for v in vers) if vers else '(none parsed)'}")
ok &= (vers == ['1'])
if len(sys.argv) > 1 and os.path.exists(sys.argv[1]):
    txt = open(sys.argv[1], encoding='utf-8', errors='replace').read()
    i0 = txt.find('4    All-order proof of Glauber gluon cancellation')
    seg = txt[i0:i0 + 20000]
    # page markers "– NN –" in the pdftotext output; find the page of each step heading
    def page_of(pos):
        pages = [(m.start(), int(m.group(1))) for m in re.finditer(r'–\s*(\d+)\s*–', txt)]
        for (p, n) in pages:
            if p > pos:
                return n
        return None
    steps = {}
    for n in range(1, 7):
        m = re.search(r'\n\s*%d\.\s+(\S.{0,90})' % n, seg)
        if m:
            steps[n] = (page_of(i0 + m.start()), m.group(1).strip())
    for n in sorted(steps):
        log(f"    DGOPS sec. 4, step {n} (p. {steps[n][0]} of v1): {steps[n][1][:90]}")
    j3 = txt.find('It would be desirable to have a formal proof that this is always possible')
    j6 = txt.find('removed by appropriate')
    log(f"    routing caveat 'It would be desirable to have a formal proof that this is always possible' on p. {page_of(j3)} (step 3)")
    log(f"    'their possible failure in larger regions ... removed by appropriate subtraction terms' on p. {page_of(j6)} (step 6)")
    ok &= len(steps) == 6 and page_of(j3) == 39 and page_of(j6) == 40
else:
    log("    (no local text of the v1 PDF given; step list not re-checked)"); ok = False
log("ALL PASS" if ok else "SOME CHECK FAILED")
with open(os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', 'final2_logs', 'lit_checks_final2.log'), 'w') as f:
    f.write('\n'.join(out) + '\n')
