import json, re, sys, urllib.request, time
bib=open(sys.argv[1]).read()
entries=re.findall(r'@\w+\{([^,]+),(.*?)\n\}', bib, re.S)
for key, body in entries:
    f=dict(re.findall(r'(\w+)\s*=\s*[{"](.*?)["}],?\s*\n', body+'\n'))
    doi=f.get('doi')
    if not doi:
        print(f"{key:28s} NO-DOI  arXiv:{f.get('eprint')}  ({f.get('year')})"); continue
    try:
        req=urllib.request.Request('https://api.crossref.org/works/'+doi, headers={'User-Agent':'bibcheck/1.0 (mailto:none)'})
        m=json.load(urllib.request.urlopen(req, timeout=60))['message']
        ct=(m.get('container-title') or [''])[0]; vol=m.get('volume'); pg=m.get('page') or m.get('article-number')
        yr=(m.get('published-print') or m.get('published-online') or m.get('issued'))['date-parts'][0][0]
        iss=m.get('issue'); t=(m.get('title') or [''])[0]
        ok_pg = (str(pg)==str(f.get('pages'))) 
        print(f"{key:28s} CR: {ct[:28]:28s} vol={vol} iss={iss} pg={pg} yr={yr} | bib: vol={f.get('volume')} pg={f.get('pages')} yr={f.get('year')} {'OK' if ok_pg else 'CHECK-PG'}")
        print(f"{'':28s} title: {t[:110]}")
    except Exception as e:
        print(key,'ERR',e)
    time.sleep(0.3)
