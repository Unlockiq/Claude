"""Make the Level-2 cover for a class from its Level-1 cover: repaint the '1' of 'Level-1' in the yellow pill as '2'.

Usage: python3 tools/l2/make_cover.py CLASS      (reads assets/AMO_Class{N}_cover.png, writes assets/AMO_Class{N}_L2_cover.png)
Check the result by eye: covers differ slightly, and the glyph search assumes the pill layout of Classes 1-4."""
import sys
import numpy as np
from PIL import Image, ImageDraw, ImageFont

FONT = '/usr/share/fonts/truetype/crosextra/Carlito-Bold.ttf'
INK = (14, 7, 48)
cls = int(sys.argv[1])
im = Image.open(f'assets/AMO_Class{cls}_cover.png').convert('RGB')
a = np.array(im).astype(int)
R, G, B = a[..., 0], a[..., 1], a[..., 2]
yel = (R > 220) & (G > 170) & (B < 160)
ys = np.where(yel[400:800, 200:850].sum(axis=1) > 400)[0] + 400
if cls <= 5:                     # Classes 1-5: dark text on a yellow pill
    p0, p1 = ys.min(), ys.max()
    dark = a[p0:p1, 200:850].sum(axis=2) < 250
    ink = INK
else:                            # Classes 6-11: white text on a purple pill
    wh = a[440:620, 250:800].min(axis=2) > 225
    rows = list(np.where(wh.sum(axis=1) > 3)[0])
    groups, g = [], [rows[0]]
    for r in rows[1:]:
        if r == g[-1] + 1:
            g.append(r)
        else:
            groups.append(g)
            g = [r]
    groups.append(g)
    g = max(groups, key=len)     # the text line is the tallest white band (sparkles are short)
    p0, p1 = g[0] + 440 - 6, g[-1] + 440 + 7
    dark = a[p0:p1, 200:850].min(axis=2) > 200
    ink = (255, 255, 255)
cols = dark.any(axis=0)
runs, start = [], None
for x, v in enumerate(cols):
    if v and start is None:
        start = x
    if not v and start is not None:
        runs.append((start + 200, x - 1 + 200))
        start = None
if ink == INK:
    x0, x1 = runs[7]             # pill edge, L, e, v, e, l, -, 1
else:
    # split the glyph runs into words at gaps > 14 px; 'Level-1' is the word with 7 glyphs
    words, w = [], [runs[0]]
    for r in runs[1:]:
        if r[0] - w[-1][1] > 14:
            words.append(w)
            w = [r]
        else:
            w.append(r)
    words.append(w)
    x0, x1 = [w for w in words if len(w) == 7][0][-1]
sub = a[p0:p1, x0:x1 + 1]
mask = (sub.sum(axis=2) < 200) if ink == INK else (sub.min(axis=2) > 200)
rows = np.where(mask.any(axis=1))[0] + p0
y0, y1 = rows.min(), rows.max()
print('"1" at x', x0, x1, 'y', y0, y1)
f = a.astype(float)
L, Rr = x0 - 3, x1 + 8
for y in range(y0 - 3, y1 + 4):
    for x in range(L + 1, Rr):
        t = (x - L) / (Rr - L)
        f[y, x] = f[y, L] * (1 - t) + f[y, Rr] * t
im = Image.fromarray(f.clip(0, 255).astype('uint8'))
font = ImageFont.truetype(FONT, round(46 * (y1 - y0 + 1) / 31))
bb = font.getbbox('2')
ImageDraw.Draw(im).text((x0 - bb[0] - 1, y1 - bb[3] + 1), '2', font=font, fill=ink)
im.save(f'assets/AMO_Class{cls}_L2_cover.png')
print('written assets/AMO_Class%d_L2_cover.png' % cls)
