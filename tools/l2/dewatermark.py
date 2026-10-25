"""Remove the grey diagonal 'aryabhattamathsolympiad.com' watermark from an L2 question paper.

Each question is a slide embedded as a form XObject (/fullpage). The watermark is a
BT..ET text block drawn in pale grey (0.84-0.89) under a rotated cm. We delete that text block.

Usage: python3 tools/l2/dewatermark.py IN.pdf OUT.pdf"""
import re, sys, pypdf
from pypdf.generic import NameObject

src, out = sys.argv[1], sys.argv[2]
r = pypdf.PdfReader(src)
w = pypdf.PdfWriter(clone_from=r)
WM = re.compile(rb'((\.8[4-9]\d*) \2 \2 rg\s.*?)BT\s.*?ET', re.S)
done, removed = set(), 0

def walk(xo):
    global removed
    xo = xo.get_object()
    if id(xo) in done:
        return
    done.add(id(xo))
    if xo.get('/Subtype') == '/Form':
        data = xo.get_data()
        new, n = WM.subn(rb'\1', data)
        if n:
            xo.set_data(new)
            removed += n
    for k, v in xo.get('/Resources', {}).get('/XObject', {}).items():
        walk(v)

for page in w.pages:
    for k, v in page['/Resources'].get('/XObject', {}).items():
        walk(v)
w.write(out)
print(src, 'watermark blocks removed:', removed)
