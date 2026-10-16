# E33 stage-2: query INSPIRE for each paper of the erratum list and print every
# publication_info entry (the erratum entries carry material = "erratum").
# Run: python3 -I e33_inspire.py > e33_inspire.log
import json, urllib.request, urllib.parse, time, sys

ITEMS = [
    ("Bodwin 1985",             "j Phys.Rev.D,31,2616"),
    ("Collins-Soper 1981",      "j Nucl.Phys.B,193,381"),
    ("Collins 1998 DDIS",       "j Phys.Rev.D,57,3051"),
    ("BBL 1995",                "j Phys.Rev.D,51,1125"),
    ("Becher-Neubert 2009",     "j Phys.Rev.Lett.,102,162001"),
    ("Henneaux 1993",           "j Phys.Lett.B,313,35"),
    ("Ebert-Gao-Stewart 2022",  "j JHEP,06,007"),
    ("Rodini-Vladimirov 2022",  "j JHEP,08,031"),
    ("KPS 2016",                "j JHEP,01,072"),
    ("Cougoulic et al 2022",    "j JHEP,07,095"),
    ("Dixon et al 2020",        "j JHEP,05,135"),
    ("Forshaw-Holguin 2021",    "j JHEP,12,084"),
    ("Becher et al 2016",       "j JHEP,11,019"),
    ("Bertone et al 2020",      "j JHEP,03,135"),
    ("Diehl-Ostermeier-Schafer","j JHEP,03,089"),
    ("Kramer-Lampe 1987",       "j Z.Phys.C,34,497"),
    ("Penin 2015",              "j Phys.Lett.B,745,69"),
    ("Floratos-Ross-Sachrajda 1977", "j Nucl.Phys.B,129,66"),
    ("FRS 1979 (check: no erratum?)", "j Nucl.Phys.B,152,493"),
    # errata present in our material but possibly missing from the list
    ("Erdogan 2014",            "j Phys.Rev.D,89,085016"),
    ("Surguladze-Samuel 1991",  "j Phys.Rev.Lett.,66,560"),
    ("Buffing-Diehl-Kasemets 2018", "j JHEP,01,044"),
]

def get(q):
    url = ("https://inspirehep.net/api/literature?size=10&q=" + urllib.parse.quote(q) +
           "&fields=titles,authors.full_name,publication_info,arxiv_eprints,control_number")
    with urllib.request.urlopen(url, timeout=60) as r:
        return json.load(r)

for name, q in ITEMS:
    try:
        d = get(q)
    except Exception as e:
        print(f"### {name}: query failed: {e}")
        continue
    hits = d["hits"]["hits"]
    print(f"### {name}   [{q}]  hits={len(hits)}")
    for h in hits:
        m = h["metadata"]
        auth = ", ".join(a["full_name"] for a in m.get("authors", [])[:5])
        tit = m["titles"][0]["title"]
        arx = ",".join(e["value"] for e in m.get("arxiv_eprints", []))
        print(f"  recid={m['control_number']}  arXiv={arx or '-'}")
        print(f"  authors: {auth}")
        print(f"  title  : {tit}")
        for p in m.get("publication_info", []):
            mat = p.get("material", "publication")
            jt = p.get("journal_title", "?"); jv = p.get("journal_volume", "?")
            ps = p.get("page_start", p.get("artid", "?")); yr = p.get("year", "?")
            print(f"    [{mat}] {jt} {jv} ({yr}) {ps}")
    time.sleep(0.4)
