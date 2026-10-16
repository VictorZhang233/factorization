"""Assemble chapters/ch08_pdf.tex, appK_moments.tex, appL_lightray.tex from parts/ (figure blocks inserted verbatim)."""
import os, sys
here = os.path.dirname(os.path.abspath(__file__))
root = os.path.abspath(os.path.join(here, '..', '..', '..'))
parts = os.path.join(here, 'parts')
figs = {'%%FIG:dglap-ladder%%': 'fig_dglap_ladder.tex', '%%FIG:splitting-vertices%%': 'fig_splitting_vertices.tex',
        '%%FIG:pdf-oneloop%%': 'fig_pdf_oneloop.tex'}
def build(out, names):
    txt = ''
    if not any(os.path.exists(os.path.join(parts, n)) for n in names):
        print('skip', out); return
    for n in names:
        p = os.path.join(parts, n)
        if not os.path.exists(p):
            continue
        txt += open(p, encoding='utf-8').read().rstrip('\n') + '\n\n'
    for k, v in figs.items():
        if k in txt:
            blk = open(os.path.join(parts, v), encoding='utf-8').read().rstrip('\n')
            txt = txt.replace(k, blk)
    assert '%%FIG:' not in txt
    open(os.path.join(root, 'chapters', out), 'w', encoding='utf-8').write(txt.rstrip('\n') + '\n')
    print('wrote', out, len(txt), 'chars')
build('ch08_pdf.tex', ['ch08_p%d.tex' % i for i in range(1, 7)])
build('appK_moments.tex', ['appK_p1.tex', 'appK_p2.tex'])
build('appL_lightray.tex', ['appL.tex'])
