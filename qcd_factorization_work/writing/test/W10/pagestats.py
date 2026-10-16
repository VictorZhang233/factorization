import sys, os, glob, subprocess
sys.path.append(os.path.expanduser('~/Library/Python/3.9/lib/python/site-packages'))
from PIL import Image
pdf=sys.argv[1]
for f in glob.glob('ps-*.png'): os.remove(f)
subprocess.run(['pdftoppm','-r','30','-png',pdf,'ps'],check=True)
files=sorted(glob.glob('ps-*.png'))
tot=0
out=[]
for f in files:
    im=Image.open(f).convert('L'); w,h=im.size; px=im.load()
    y0=int(h*0.09); y1=int(h*0.93); blank=0; run=0; maxrun=0
    for y in range(y0,y1):
        ink=any(px[x,y]<200 for x in range(int(w*0.1),int(w*0.9)))
        if not ink: run+=1; blank+=1
        else: maxrun=max(maxrun,run); run=0
    maxrun=max(maxrun,run)
    out.append('%s:%.2f'%(f[3:-4],maxrun/(y1-y0)))
print(len(files),'pages; max blank runs:',' '.join(out))
