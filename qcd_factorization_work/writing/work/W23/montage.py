# Build a contact sheet (montage) of rendered PDF pages, for layout inspection.
# Usage: python3 -I montage.py OUT.png COLS page1.png page2.png ...
import sys, os
sys.path.append(os.path.expanduser('~/Library/Python/3.9/lib/python/site-packages'))
from PIL import Image, ImageDraw

out, cols = sys.argv[1], int(sys.argv[2])
files = sys.argv[3:]
ims = [Image.open(f).convert('RGB') for f in files]
w = max(i.width for i in ims); h = max(i.height for i in ims)
rows = (len(ims) + cols - 1) // cols
sheet = Image.new('RGB', (cols * (w + 6) + 6, rows * (h + 6) + 6), (90, 90, 90))
for k, im in enumerate(ims):
    r, c = divmod(k, cols)
    x, y = 6 + c * (w + 6), 6 + r * (h + 6)
    sheet.paste(im, (x, y))
    ImageDraw.Draw(sheet).text((x + 4, y + 4), str(k + 1), fill=(200, 0, 0))
sheet.save(out)
print('saved', out, sheet.size)
