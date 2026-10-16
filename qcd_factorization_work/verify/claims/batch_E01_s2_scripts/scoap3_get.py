import json, sys, subprocess, os
doi, outdir = sys.argv[1], sys.argv[2]
os.makedirs(outdir, exist_ok=True)
tmp = os.path.join(outdir, 'rec.json')
subprocess.run(['curl', '-sS', '-m', '60', '-o', tmp, 'https://repo.scoap3.org/api/records/?doi=' + doi], check=True)
j = json.load(open(tmp))
print('count', j.get('count'))
for h in j['hits']['hits']:
    m = h['metadata']
    print([d.get('value') for d in m.get('dois', [])], m.get('titles', [{}])[0].get('title', '')[:100])
    for f in m.get('_files', []):
        print('   ', f.get('filetype'), f.get('file'))
        if f.get('filetype') == 'pdf' or f.get('file', '').endswith('.pdf'):
            out = os.path.join(outdir, os.path.basename(f['file']))
            subprocess.run(['curl', '-sS', '-m', '120', '-L', '-o', out, f['file']], check=True)
            print('    saved', out, os.path.getsize(out))
