# E33 stage-2: INSPIRE records by arXiv number (JHEP items, where j-searches are ambiguous)
import json, urllib.request, urllib.parse, time
IDS = [("Rodini-Vladimirov 2022","2204.03856"),("KPS 2016","1511.06737"),("Cougoulic et al 2022","2204.11898"),
       ("Dixon-Herrmann-Yan-Zhu 2020","1912.09370"),("Forshaw-Holguin 2021","2109.03665"),
       ("Diehl-Ostermeier-Schafer 2012","1111.0910"),("Buffing-Diehl-Kasemets 2018","1708.03528"),
       ("Ebert-Gao-Stewart 2022","2112.07680"),("Becher et al 2016","1605.02737"),("Bertone et al 2020","1911.12040")]
for name, a in IDS:
    url = ("https://inspirehep.net/api/literature?q=" + urllib.parse.quote("arxiv:"+a) +
           "&fields=titles,authors.full_name,publication_info,control_number")
    d = json.load(urllib.request.urlopen(url, timeout=60))
    for h in d["hits"]["hits"]:
        m = h["metadata"]
        print(f"### {name}  arXiv:{a}  recid={m['control_number']}")
        print("  authors:", ", ".join(x["full_name"] for x in m.get("authors", [])[:6]))
        for t in m["titles"]: print("  title  :", t["title"])
        for p in m.get("publication_info", []):
            print(f"    [{p.get('material','publication')}] {p.get('journal_title','?')} {p.get('journal_volume','?')} ({p.get('year','?')}) {p.get('page_start',p.get('artid','?'))}")
    time.sleep(0.4)
