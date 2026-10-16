# E33 stage-2: find DOIs of the paywalled errata through Crossref (journal, volume, first page).
import json, urllib.request, urllib.parse, time
Q = [("Bodwin erratum", "Physical Review D", "34", "3932"),
     ("Collins-Soper erratum", "Nuclear Physics B", "213", "545"),
     ("Collins 1998 erratum", "Physical Review D", "61", "019902"),
     ("BBL erratum", "Physical Review D", "55", "5853"),
     ("Becher-Neubert erratum", "Physical Review Letters", "111", "199905"),
     ("Henneaux erratum", "Physics Letters B", "316", "633"),
     ("Kramer-Lampe erratum", "Zeitschrift für Physik C Particles and Fields", "42", "504"),
     ("Penin erratum 1", "Physics Letters B", "751", "596"),
     ("Penin erratum 2", "Physics Letters B", "771", "633"),
     ("FRS erratum", "Nuclear Physics B", "139", "545")]
for name, jt, vol, pg in Q:
    url = ("https://api.crossref.org/works?rows=5&query.bibliographic=" +
           urllib.parse.quote(f"{jt} {vol} {pg} erratum") + "&filter=" + urllib.parse.quote("type:journal-article"))
    try:
        d = json.load(urllib.request.urlopen(urllib.request.Request(url, headers={"User-Agent": "verify-script/1.0 (mailto:none@example.org)"}), timeout=60))
    except Exception as e:
        print(name, "failed", e); continue
    print("###", name)
    for it in d["message"]["items"]:
        ct = it.get("container-title", [""])[0]; v = it.get("volume"); p = it.get("page") or it.get("article-number")
        if v == vol and str(p).split("-")[0] in (pg, pg.lstrip("0")):
            print("   MATCH", it["DOI"], "|", ct, v, p, "|", (it.get("title") or [""])[0][:100])
    time.sleep(0.5)
