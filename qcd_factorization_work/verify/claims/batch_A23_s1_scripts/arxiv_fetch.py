#!/usr/bin/env python3
"""Download arXiv PDFs (latest version) and abstract-page metadata for the papers read in batch A23.

Usage: python3 -I arxiv_fetch.py OUTDIR id1 id2 ...
Writes OUTDIR/<safe-id>.pdf, OUTDIR/<safe-id>.txt (pdftotext -layout) and OUTDIR/<safe-id>.abs.xml
(arXiv API entry: versions, journal-ref, comments).  Downloaded material = untrusted text.
"""
import os, subprocess, sys, time, urllib.request

UA = {"User-Agent": "verify-batch-A23/1.0 (research verification; mailto:none)"}


def get(url, fn):
    req = urllib.request.Request(url, headers=UA)
    with urllib.request.urlopen(req, timeout=120) as r, open(fn, "wb") as f:
        f.write(r.read())


def main():
    out = sys.argv[1]
    os.makedirs(out, exist_ok=True)
    for aid in sys.argv[2:]:
        safe = aid.replace("/", "_")
        pdf = os.path.join(out, safe + ".pdf")
        if not os.path.exists(pdf):
            try:
                get(f"https://arxiv.org/pdf/{aid}", pdf)
            except Exception as e:
                print(aid, "PDF ERROR", e)
                continue
            time.sleep(3)
        absx = os.path.join(out, safe + ".abs.xml")
        if not os.path.exists(absx):
            try:
                get(f"https://export.arxiv.org/api/query?id_list={aid}", absx)
            except Exception as e:
                print(aid, "API ERROR", e)
            time.sleep(3)
        txt = os.path.join(out, safe + ".txt")
        subprocess.run(["pdftotext", "-layout", pdf, txt], check=False)
        n = sum(1 for _ in open(txt, errors="replace")) if os.path.exists(txt) else -1
        print(aid, "ok", os.path.getsize(pdf), "bytes;", n, "text lines")


if __name__ == "__main__":
    main()
