# montage of page thumbnails (W03 QA helper): python3 -I montage.py out.png cols img1 img2 ...
import sys, os
sys.path.append(os.path.expanduser('~/Library/Python/3.9/lib/python/site-packages'))
from PIL import Image, ImageDraw
out, cols = sys.argv[1], int(sys.argv[2])
ims = [Image.open(p).convert('RGB') for p in sys.argv[3:]]
w = max(i.width for i in ims); h = max(i.height for i in ims)
rows = (len(ims) + cols - 1) // cols
M = Image.new('RGB', (cols * (w + 6), rows * (h + 6)), 'gray')
for k, im in enumerate(ims):
    r, c = divmod(k, cols)
    M.paste(im, (c * (w + 6) + 3, r * (h + 6) + 3))
    ImageDraw.Draw(M).text((c * (w + 6) + 8, r * (h + 6) + 6), str(k + 1), fill=(255, 0, 0))
M.save(out)
print(M.size)
