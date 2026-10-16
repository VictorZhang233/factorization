# E33 stage-2: Penin corrigenda (PLB, SCOAP3 open access)
import json, sys, subprocess, os
out = sys.argv[1]; os.makedirs(out, exist_ok=True)
for tag, doi in {"penin_corr1": "10.1016/j.physletb.2015.10.035", "penin_corr2": "10.1016/j.physletb.2017.05.069",
                 "penin_orig": "10.1016/j.physletb.2015.04.036"}.items():
    rec = os.path.join(out, tag + ".json")
    subprocess.run(["curl", "-sS", "-m", "60", "-o", rec, "https://repo.scoap3.org/api/records/?doi=" + doi])
    try: j = json.load(open(rec))
    except Exception as e: print(tag, "no JSON", e); continue
    hits = j.get("hits", {}).get("hits", []); print(tag, doi, "hits", len(hits))
    for h in hits:
        for f in h["metadata"].get("_files", []):
            fn = f.get("file", "")
            if f.get("filetype") == "pdf" or fn.endswith(".pdf"):
                pdf = os.path.join(out, tag + ".pdf")
                subprocess.run(["curl", "-sS", "-m", "120", "-L", "-o", pdf, fn])
                subprocess.run(["pdftotext", "-layout", pdf, os.path.join(out, tag + ".txt")])
                print("   saved", pdf, os.path.getsize(pdf)); break
