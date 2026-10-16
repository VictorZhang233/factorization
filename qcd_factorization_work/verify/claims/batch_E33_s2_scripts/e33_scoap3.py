# E33 stage-2: download the published JHEP erratum notes (open access, SCOAP3) and convert to text.
# usage: python3 -I e33_scoap3.py OUTDIR
import json, sys, subprocess, os
out = sys.argv[1]; os.makedirs(out, exist_ok=True)
DOIS = {"dhyz_err": "10.1007/JHEP06(2024)143", "fh_err": "10.1007/JHEP04(2024)097",
        "bnrs_err": "10.1007/JHEP05(2017)154", "bccs_err": "10.1007/JHEP08(2022)108",
        "egs_err": "10.1007/JHEP07(2023)096", "rv_err": "10.1007/JHEP12(2022)048",
        "kps_err": "10.1007/JHEP10(2016)148", "cktt_err": "10.1007/JHEP09(2024)052",
        "dos_err": "10.1007/JHEP03(2016)001"}
for tag, doi in DOIS.items():
    rec = os.path.join(out, tag + ".json")
    subprocess.run(["curl", "-sS", "-m", "60", "-o", rec, "https://repo.scoap3.org/api/records/?doi=" + doi])
    try:
        j = json.load(open(rec))
    except Exception as e:
        print(tag, doi, "no JSON", e); continue
    hits = j.get("hits", {}).get("hits", [])
    print(tag, doi, "hits", len(hits))
    for h in hits:
        for f in h["metadata"].get("_files", []):
            fn = f.get("file", "")
            if f.get("filetype") == "pdf" or fn.endswith(".pdf"):
                pdf = os.path.join(out, tag + ".pdf")
                subprocess.run(["curl", "-sS", "-m", "120", "-L", "-o", pdf, fn])
                subprocess.run(["pdftotext", "-layout", pdf, os.path.join(out, tag + ".txt")])
                print("   saved", pdf, os.path.getsize(pdf))
                break
