#!/usr/bin/env python3
"""Fetch INSPIRE-HEP metadata (title, authors, publication info, abstract, arXiv id, texkeys,
errata/notes) for every reference used in claims A23-A28 (verification batch A23, stage 1).

Usage:  python3 -I inspire_fetch.py OUTDIR
Writes one JSON file per query label into OUTDIR (downloaded data = untrusted text) and a
summary file OUTDIR/_summary.txt.  Standard library only.
"""
import json, os, sys, time, urllib.parse, urllib.request

FIELDS = ("titles,authors.full_name,publication_info,abstracts,arxiv_eprints,texkeys,"
          "dois,control_number,number_of_pages,public_notes,document_type,refereed,"
          "preprint_date,earliest_date")

# label -> INSPIRE search query
Q = {
 # ---------------- A23 (REVIEW §11) ----------------
 "A23_01_AnikinZavyalov": "texkey Anikin:1978tj",
 "A23_01b_Zavyalov1990": "texkey Zavyalov:1990kv",
 "A23_02_LowensteinZimmermann_NPB86": "j Nucl.Phys.B,86,77",
 "A23_02b_LowensteinZimmermann_CMP44": "j Commun.Math.Phys.,44,73",
 "A23_02c_Lowenstein_CMP47": "j Commun.Math.Phys.,47,53",
 "A23_03_Frye2019": "j Phys.Rev.D,99,056015",
 "A23_04_Gaunt2014": "texkey Gaunt:2014ska",
 "A23_05_AybatSterman": "texkey Aybat:2008ct",
 "A23_06_FSS2012": "texkey Forshaw:2012bi",
 "A23_07_CSS1986": "j Nucl.Phys.B,263,37",
 "A23_08_Collins1998": "texkey Collins:1998rz",
 "A23_09a_DFT1980": "j Nucl.Phys.B,168,93",
 "A23_09b_DiLieto1981": "j Nucl.Phys.B,183,223",
 "A23_09c_Andrasi1981": "j Nucl.Phys.B,182,104",
 "A23_09d_FGT1984": "j Nucl.Phys.B,233,307",
 "A23_10_BenekeBraun1995": "j Nucl.Phys.B,454,253",
 "A23_11a_BNRS2016": "texkey Becher:2016mmh",
 "A23_11b_BNS2021": "texkey Becher:2021zkk",
 "A23_12_MankiewiczPiller": "texkey Mankiewicz:1999tt",
 "A23_13_EMSS2022": "j JHEP,2207,129",
 "A23_14_BVZ2019": "texkey Braun:2018brg",
 "A23_15_KorchemskySterman1999": "j Nucl.Phys.B,555,335",
 "A23_16_Shifman2000": "eprint hep-ph/0009131",
 "A23_17_Graudenz1994": "a Graudenz and t semi-inclusive and date 1994",
 "A23_17b_Graudenz_NPB432": "j Nucl.Phys.B,432,351",
 "A23_18a_LiSterman1992": "j Nucl.Phys.B,381,129",
 "A23_18b_Soffer1995": "j Phys.Rev.Lett.,74,1292",
 "A23_18c_LabastidaSterman1985": "j Nucl.Phys.B,254,425",
 "A23_18d_Kodaira1980": "j Nucl.Phys.B,165,129",
 "A23_18e_ChristLee1966": "j Phys.Rev.,143,1310",
 # ---------------- A24 (misconception boxes) ----------------
 "A24_01a_Collins1993": "j Nucl.Phys.B,396,161",
 "A24_01b_Collins2002": "j Phys.Lett.B,536,43",
 "A24_01c_BHS2002": "j Phys.Lett.B,530,99",
 "A24_02a_CollinsMetz2004": "j Phys.Rev.Lett.,93,252001",
 "A24_02b_MeissnerMetz2009": "j Phys.Rev.Lett.,102,172003",
 "A24_03a_JiYuan2002": "j Phys.Lett.B,543,66",
 "A24_03b_BJY2003": "j Nucl.Phys.B,656,165",
 "A24_04a_LamTung1980": "j Phys.Rev.D,21,2712",
 "A24_04b_MirkesOhnemus1994": "j Phys.Rev.D,50,5692",
 "A24_04c_Mirkes1992": "j Nucl.Phys.B,387,3",
 "A24_04d_LambertsenVogelsang2016": "j Phys.Rev.D,93,114013",
 "A24_04e_BrandenburgNachtmannMirkes1993": "j Z.Phys.C,60,697",
 "A24_06a_CallanCooteGross1976": "j Phys.Rev.D,13,1649",
 "A24_06b_Einhorn1976": "j Phys.Rev.D,14,3451",
 "A24_07_BurkardtKoike2002": "j Nucl.Phys.B,632,311",
 "A24_08a_CFP1980": "j Nucl.Phys.B,175,27",
 "A24_08b_FRS1977": "j Nucl.Phys.B,129,66",
 "A24_09a_NMC1991": "j Phys.Rev.Lett.,66,2712",
 "A24_09b_NMC1994": "j Phys.Rev.D,50,R1",
 "A24_09c_Gottfried1967": "j Phys.Rev.Lett.,18,1174",
 # ---------------- A25 (quarkonium, EW, DPS) ----------------
 "A25_01a_NQS2005PLB": "j Phys.Lett.B,613,45",
 "A25_01b_NQS2005PRD": "j Phys.Rev.D,72,114012",
 "A25_01c_NQS2006PRD": "j Phys.Rev.D,74,074007",
 "A25_01d_Bodwin2020": "j Phys.Rev.D,101,096011",
 "A25_02a_BHK2015": "j Phys.Rev.Lett.,114,092004",
 "A25_02b_Han2015": "j Phys.Rev.Lett.,114,092005",
 "A25_02c_Zhang2015": "j Phys.Rev.Lett.,114,092006",
 "A25_03_CCC2000": "j Phys.Rev.Lett.,84,4810",
 "A25_04_BERV2019": "j Phys.Rev.D,100,096008",
 "A25_05_DGOPS2016": "texkey Diehl:2015bca",
 "A25_06_EGS2022": "j JHEP,2206,007",
 "A25_07_Gamberg2022": "eprint 2211.13209",
 # ---------------- A27 (Sivers, twist 3, Collins 1998) ----------------
 "A27_01a_COMPASS2017": "texkey COMPASS:2017jbv",
 "A27_01b_COMPASS2024": "j Phys.Rev.Lett.,133,071902",
 "A27_01c_STAR2016": "j Phys.Rev.Lett.,116,132301",
 "A27_01d_BPV2021": "j Phys.Rev.Lett.,126,112002",
 "A27_01e_EKT2021": "j JHEP,2101,126",
 "A27_01f_STAR2023Z": "texkey STAR:2023jwh",
 "A27_02a_BMP2009": "j Phys.Rev.D,80,114002",
 "A27_02b_KangQiu2009": "j Phys.Rev.D,79,016003",
 "A27_02c_Kang2011": "j Phys.Rev.D,83,094001",
 "A27_02d_JAM2020": "j Phys.Rev.D,102,054002",
 # ---------------- A28 (NLP endpoint factorization) ----------------
 "A28_01_LN2020": "j JHEP,2004,033",
 "A28_02_LMNW2021": "j JHEP,2101,077",
 "A28_03_LNSW2023": "j JHEP,2306,183",
 "A28_04_BBJV2020": "j JHEP,2007,078",
 "A28_05a_BeneketDY2019": "j JHEP,1903,043",
 "A28_05b_BenekeHiggs2020": "j JHEP,2001,094",
 "A28_05c_BenekeDIS2020": "j JHEP,2010,196",
 "A28_05d_BenekeThrust2022": "j JHEP,2207,144",
 "A28_06_BSS2026": "eprint 2608.25502",
 "A28_07a_Bodwin2021a": "j Phys.Rev.D,104,016010",
 "A28_07b_Bodwin2021b": "j Phys.Rev.D,104,116025",
 "A28_07c_Bodwin2024": "j Phys.Rev.D,109,056020",
 "A28_07d_Bodwin2025": "eprint 2512.11647",
 "A28_08_LiuPenin2017": "j Phys.Rev.Lett.,119,262001",
}


def fetch(q):
    url = ("https://inspirehep.net/api/literature?size=5&q=" + urllib.parse.quote(q)
           + "&fields=" + FIELDS)
    req = urllib.request.Request(url, headers={"Accept": "application/json",
                                               "User-Agent": "verify-batch-A23/1.0"})
    with urllib.request.urlopen(req, timeout=60) as r:
        return json.loads(r.read().decode("utf-8"))


def summarize(label, data):
    out = []
    hits = data.get("hits", {}).get("hits", [])
    out.append(f"### {label}: {len(hits)} hit(s)")
    for h in hits:
        m = h["metadata"]
        t = "; ".join(x.get("title", "") for x in m.get("titles", [])[:1])
        au = [a["full_name"] for a in m.get("authors", [])]
        aus = "; ".join(au[:8]) + (f" (+{len(au)-8})" if len(au) > 8 else "")
        pubs = []
        for p in m.get("publication_info", []):
            pubs.append(" ".join(str(p.get(k, "")) for k in
                                 ("journal_title", "journal_volume", "year", "artid", "page_start",
                                  "page_end", "material") if p.get(k)))
        ax = ",".join(e.get("value", "") for e in m.get("arxiv_eprints", []))
        tk = ",".join(m.get("texkeys", []))
        doi = ",".join(d.get("value", "") + ("[" + d.get("material", "") + "]" if d.get("material") else "")
                       for d in m.get("dois", []))
        notes = " | ".join(n.get("value", "") for n in m.get("public_notes", []))
        out.append(f"recid {m.get('control_number')} | texkeys {tk} | arXiv {ax}")
        out.append(f"  title: {t}")
        out.append(f"  authors: {aus}")
        out.append(f"  pub: {' || '.join(pubs)}")
        out.append(f"  doi: {doi} | refereed: {m.get('refereed')} | doc_type: {m.get('document_type')}"
                   f" | earliest: {m.get('earliest_date')}")
        if notes:
            out.append(f"  notes: {notes}")
        for a in m.get("abstracts", [])[:2]:
            out.append(f"  abstract[{a.get('source','')}]: {a.get('value','')}")
    return "\n".join(out)


def main():
    outdir = sys.argv[1]
    os.makedirs(outdir, exist_ok=True)
    summ = []
    for label, q in Q.items():
        fn = os.path.join(outdir, label + ".json")
        if not os.path.exists(fn):
            for attempt in range(3):
                try:
                    data = fetch(q)
                    break
                except Exception as e:  # network hiccup: retry
                    data = {"error": str(e)}
                    time.sleep(3)
            with open(fn, "w") as f:
                json.dump(data, f)
            time.sleep(0.4)
        with open(fn) as f:
            data = json.load(f)
        if "error" in data:
            summ.append(f"### {label}: ERROR {data['error']}")
        else:
            summ.append(f"[query: {q}]\n" + summarize(label, data))
    with open(os.path.join(outdir, "_summary.txt"), "w") as f:
        f.write("\n\n".join(summ) + "\n")
    print(f"{len(Q)} queries done; summary in {os.path.join(outdir, '_summary.txt')}")


if __name__ == "__main__":
    main()
