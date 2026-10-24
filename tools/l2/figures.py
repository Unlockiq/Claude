"""Picture library for the AMO Level-2 papers.

Every figure is described as data (a dict made by one of the helpers below) and
rendered to a PNG by render(fig, path). Pictures follow the Visual Standards of the
AMO syllabus: crisp drawings, readable in greyscale (information is carried by shape,
number or position, never by colour alone), number-line ticks all labelled except the
one asked about, labels at least 10 pt.

Coordinates are in points; K pixels are drawn per point (K=4 gives 288 dpi).
"""
import math
from PIL import Image, ImageDraw, ImageFont

K = 4
FONT_B = '/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf'
FONT_R = '/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf'
EMOJI = '/usr/share/fonts/truetype/noto/NotoColorEmoji.ttf'
INK = (34, 34, 34)
PURPLE = (106, 62, 161)
RED = (192, 40, 40)
FILL = {'blue': (207, 226, 243), 'peach': (255, 224, 194), 'pink': (248, 205, 220),
        'yellow': (255, 242, 179), 'green': (217, 234, 211), 'grey': (158, 158, 158),
        'white': (255, 255, 255), 'lilac': (230, 220, 245), 'none': None}
SHAPE_FILL = {'circle': 'blue', 'square': 'yellow', 'rectangle': 'green', 'triangle': 'pink',
              'star': (255, 196, 61), 'semicircle': 'lilac',
              'cube': 'yellow', 'cylinder': 'blue', 'cone': 'pink', 'sphere': 'green'}

_fonts = {}


def font(size, bold=True):
    key = (size, bold)
    if key not in _fonts:
        _fonts[key] = ImageFont.truetype(FONT_B if bold else FONT_R, int(size * K))
    return _fonts[key]


_emoji = {}


def emoji_img(ch, size):
    """Colour emoji ch rendered to a square RGBA image of size pt."""
    key = (ch, size)
    if key not in _emoji:
        f = ImageFont.truetype(EMOJI, 109)
        im = Image.new('RGBA', (160, 160), (255, 255, 255, 0))
        ImageDraw.Draw(im).text((8, 8), ch, font=f, embedded_color=True)
        bb = im.getbbox()
        im = im.crop(bb)
        s = int(size * K)
        w, h = im.size
        r = s / max(w, h)
        im = im.resize((max(1, int(w * r)), max(1, int(h * r))), Image.LANCZOS)
        out = Image.new('RGBA', (s, s), (255, 255, 255, 0))
        out.paste(im, ((s - im.size[0]) // 2, (s - im.size[1]) // 2), im)
        _emoji[key] = out
    return _emoji[key]


class Canvas:
    def __init__(self, w, h):
        self.w, self.h = w, h
        self.im = Image.new('RGB', (int(w * K), int(h * K)), 'white')
        self.d = ImageDraw.Draw(self.im)

    def P(self, x, y):
        return (x * K, y * K)

    def rect(self, x, y, w, h, fill='white', outline=INK, width=1.6, radius=0, dashed=False):
        fill = FILL.get(fill, fill) if isinstance(fill, str) else fill
        box = [x * K, y * K, (x + w) * K, (y + h) * K]
        if dashed:
            if fill:
                self.d.rounded_rectangle(box, radius * K, fill=fill)
            self.dashed_poly([(x, y), (x + w, y), (x + w, y + h), (x, y + h)], outline, width, closed=True)
        else:
            self.d.rounded_rectangle(box, radius * K, fill=fill, outline=outline, width=int(width * K))

    def circle(self, cx, cy, r, fill='white', outline=INK, width=1.6, dashed=False):
        fill = FILL.get(fill, fill) if isinstance(fill, str) else fill
        box = [(cx - r) * K, (cy - r) * K, (cx + r) * K, (cy + r) * K]
        if dashed:
            if fill:
                self.d.ellipse(box, fill=fill)
            n = max(12, int(r * 1.2))
            for i in range(n):
                if i % 2 == 0:
                    a0, a1 = 360 * i / n, 360 * (i + 1) / n
                    self.d.arc(box, a0, a1, fill=outline, width=int(width * K))
        else:
            self.d.ellipse(box, fill=fill, outline=outline, width=int(width * K))

    def poly(self, pts, fill='white', outline=INK, width=1.6, dashed=False):
        fill = FILL.get(fill, fill) if isinstance(fill, str) else fill
        if fill:
            self.d.polygon([self.P(*p) for p in pts], fill=fill)
        if dashed:
            self.dashed_poly(pts, outline, width, closed=True)
        elif outline:
            self.d.line([self.P(*p) for p in pts + [pts[0]]], fill=outline, width=int(width * K), joint='curve')

    def line(self, x1, y1, x2, y2, color=INK, width=1.6, dashed=False):
        if dashed:
            self.dashed_poly([(x1, y1), (x2, y2)], color, width, closed=False)
        else:
            self.d.line([self.P(x1, y1), self.P(x2, y2)], fill=color, width=int(width * K))

    def dashed_poly(self, pts, color, width, closed=True, dash=5, gap=3.5):
        seq = pts + [pts[0]] if closed else pts
        for (x1, y1), (x2, y2) in zip(seq, seq[1:]):
            L = math.hypot(x2 - x1, y2 - y1)
            t = 0
            while t < L:
                t2 = min(t + dash, L)
                self.d.line([self.P(x1 + (x2 - x1) * t / L, y1 + (y2 - y1) * t / L),
                             self.P(x1 + (x2 - x1) * t2 / L, y1 + (y2 - y1) * t2 / L)],
                            fill=color, width=int(width * K))
                t += dash + gap

    def text(self, x, y, s, size=13, bold=True, color=INK, anchor='mm'):
        self.d.text(self.P(x, y), str(s), font=font(size, bold), fill=color, anchor=anchor)

    def text_w(self, s, size=13, bold=True):
        return self.d.textlength(str(s), font=font(size, bold)) / K

    def emoji(self, ch, cx, cy, size):
        e = emoji_img(ch, size)
        self.im.paste(e, (int((cx - size / 2) * K), int((cy - size / 2) * K)), e)

    def shape(self, kind, cx, cy, s, fill=None, dashed=False, outline=INK, width=1.6):
        """Draw a named shape of overall size s centred at (cx, cy)."""
        fill = fill or SHAPE_FILL.get(kind, 'white')
        h = s / 2
        if kind == 'circle':
            self.circle(cx, cy, h, fill, outline, width, dashed)
        elif kind == 'square':
            self.poly([(cx - h, cy - h), (cx + h, cy - h), (cx + h, cy + h), (cx - h, cy + h)], fill, outline, width, dashed)
        elif kind == 'rectangle':
            self.poly([(cx - h * 1.25, cy - h * 0.7), (cx + h * 1.25, cy - h * 0.7), (cx + h * 1.25, cy + h * 0.7), (cx - h * 1.25, cy + h * 0.7)], fill, outline, width, dashed)
        elif kind == 'triangle':
            self.poly([(cx, cy - h), (cx + h * 1.1, cy + h * 0.85), (cx - h * 1.1, cy + h * 0.85)], fill, outline, width, dashed)
        elif kind == 'star':
            pts = []
            for i in range(10):
                r = h if i % 2 == 0 else h * 0.45
                a = -math.pi / 2 + i * math.pi / 5
                pts.append((cx + r * math.cos(a), cy + r * math.sin(a)))
            self.poly(pts, fill, outline, width, dashed)
        elif kind == 'semicircle':
            box = [(cx - h) * K, (cy - h * 0.5) * K, (cx + h) * K, (cy + h * 1.5) * K]
            f = FILL.get(fill, fill)
            self.d.pieslice(box, 180, 360, fill=f, outline=outline, width=int(width * K))
        elif kind == 'cube':
            d = s * 0.28
            a = s - d
            x0, y0 = cx - s / 2, cy - s / 2 + d
            f = FILL.get(fill, fill) if isinstance(fill, str) else fill
            self.poly([(x0, y0), (x0 + a, y0), (x0 + a, y0 + a), (x0, y0 + a)], f or 'yellow', outline, width)
            self.poly([(x0, y0), (x0 + d, y0 - d), (x0 + a + d, y0 - d), (x0 + a, y0)], (255, 250, 220), outline, width)
            self.poly([(x0 + a, y0), (x0 + a + d, y0 - d), (x0 + a + d, y0 + a - d), (x0 + a, y0 + a)], (235, 215, 140), outline, width)
        elif kind == 'cylinder':
            w, e = s * 0.7, s * 0.14
            f = FILL.get(fill or 'blue', fill or 'blue')
            top, bot = cy - h + e, cy + h - e
            self.d.rectangle([(cx - w / 2) * K, top * K, (cx + w / 2) * K, bot * K], fill=f)
            self.d.ellipse([(cx - w / 2) * K, (bot - e) * K, (cx + w / 2) * K, (bot + e) * K], fill=f, outline=outline, width=int(width * K))
            self.d.rectangle([(cx - w / 2 + width) * K, (bot - e) * K, (cx + w / 2 - width) * K, bot * K], fill=f)
            self.line(cx - w / 2, top, cx - w / 2, bot, outline, width)
            self.line(cx + w / 2, top, cx + w / 2, bot, outline, width)
            self.d.ellipse([(cx - w / 2) * K, (top - e) * K, (cx + w / 2) * K, (top + e) * K], fill=(225, 238, 250), outline=outline, width=int(width * K))
        elif kind == 'cone':
            w, e = s * 0.8, s * 0.13
            f = FILL.get(fill or 'pink', fill or 'pink')
            bot = cy + h - e
            self.d.ellipse([(cx - w / 2) * K, (bot - e) * K, (cx + w / 2) * K, (bot + e) * K], fill=f, outline=outline, width=int(width * K))
            self.poly([(cx, cy - h), (cx + w / 2, bot), (cx - w / 2, bot)], f, None)
            self.line(cx, cy - h, cx - w / 2, bot, outline, width)
            self.line(cx, cy - h, cx + w / 2, bot, outline, width)
        elif kind == 'sphere':
            f = FILL.get(fill or 'green', fill or 'green')
            self.circle(cx, cy, h, f, outline, width)
            self.d.arc([(cx - h) * K, (cy - h * 0.3) * K, (cx + h) * K, (cy + h * 0.3) * K], 0, 180, fill=outline, width=int(width * 0.7 * K))
        elif kind == 'qbox':
            self.rect(cx - h, cy - h, s, s, 'white', PURPLE, 1.8, 3, dashed=True)
            self.text(cx, cy, '?', s * 0.55, True, PURPLE)
        elif kind == 'blank':
            pass
        else:
            raise ValueError(kind)

    def trim(self, pad=4):
        bg = Image.new('RGB', self.im.size, 'white')
        from PIL import ImageChops
        bb = ImageChops.difference(self.im, bg).getbbox()
        if bb:
            p = int(pad * K)
            bb = (max(bb[0] - p, 0), max(bb[1] - p, 0), min(bb[2] + p, self.im.size[0]), min(bb[3] + p, self.im.size[1]))
            self.im = self.im.crop(bb)
        return self.im


# ---------------------------------------------------------------- figure kinds

def card_row(items, size=34, gap=10, labels=None, fill='yellow', canvas=None, x0=6, y0=6, font_size=None, width=None):
    """A row of cards. Item '?' draws a dashed purple box; ('emoji', ch) draws an emoji card;
    ('shape', kind) a shape card; ('blank',) an empty card; anything else is text."""
    n = len(items)
    wcard = width or size
    W = x0 * 2 + n * wcard + (n - 1) * gap
    H = y0 * 2 + size + (22 if labels else 0)
    c = canvas or Canvas(W, H)
    for i, it in enumerate(items):
        x = x0 + i * (wcard + gap)
        cx, cy = x + wcard / 2, y0 + size / 2
        if it == '?':
            c.rect(x, y0, wcard, size, 'white', PURPLE, 1.8, 4, dashed=True)
            c.text(cx, cy, '?', size * 0.5, True, PURPLE)
        elif isinstance(it, tuple) and it[0] == 'emoji':
            c.rect(x, y0, wcard, size, 'white', INK, 1.4, 4)
            c.emoji(it[1], cx, cy, size * 0.72)
        elif isinstance(it, tuple) and it[0] == 'shape':
            c.shape(it[1], cx, cy, size * 0.7, fill=it[2] if len(it) > 2 else None)
        elif isinstance(it, tuple) and it[0] == 'blank':
            c.rect(x, y0, wcard, size, 'white', INK, 1.4, 4)
        else:
            c.rect(x, y0, wcard, size, fill, INK, 1.6, 4)
            fs = font_size or (size * 0.5 if len(str(it)) <= 2 else size * 0.4)
            c.text(cx, cy + 1, it, fs)
        if labels:
            c.text(cx, y0 + size + 12, labels[i], 12, True, INK)
    return c


def cards(items, **kw):
    return {'kind': 'cards', 'items': items, **kw}


def objects(groups, item=34, gap=6, cols=5, boxed=True, label_size=13):
    """groups: list of dicts {'label': 'P', 'rows': [[emoji, emoji, ...], ...]} or {'items': [...], 'cols': n}."""
    return {'kind': 'objects', 'groups': groups, 'item': item, 'gap': gap, 'cols': cols, 'boxed': boxed, 'label_size': label_size}


def numberline(start, end, step=1, marks=None, hide=None, hops=None, width=420, label_every=1):
    """Horizontal number line with arrows at both ends; every tick labelled except those in hide
    (a tick in marks is lettered instead of numbered)."""
    return {'kind': 'numberline', 'start': start, 'end': end, 'step': step, 'marks': marks or {},
            'hide': hide or [], 'hops': hops or [], 'width': width, 'label_every': label_every}


def blocks(sets, labels=None):
    """Tens rods and ones cubes. sets: list of (tens, ones)."""
    return {'kind': 'blocks', 'sets': sets, 'labels': labels}


def shapes(items, size=40, gap=12, labels=None, divider_after=None):
    """Row of shapes. items: kind names, ('qbox'), or (kind, fill)."""
    return {'kind': 'shapes', 'items': items, 'size': size, 'gap': gap, 'labels': labels, 'divider_after': divider_after}


def drawing(w, h, prims, scale=1.0):
    """Free drawing. prims: ('poly', pts, fill?, dashed?), ('rect', x, y, w, h, fill?), ('circle', cx, cy, r, fill?),
    ('line', x1, y1, x2, y2, dashed?, color?), ('text', x, y, s, size?), ('dot', x, y, r?), ('emoji', ch, cx, cy, size),
    ('shape', kind, cx, cy, s, fill?)."""
    return {'kind': 'drawing', 'w': w, 'h': h, 'prims': prims, 'scale': scale}


def grid(rows, cell=40, fills=None, bold=True, font_size=None, dashed_q=True):
    """Table of cells (numbers, text, '?', '' for blank)."""
    return {'kind': 'grid', 'rows': rows, 'cell': cell, 'fills': fills, 'font_size': font_size}


def week(days, marks=None, short=True):
    return {'kind': 'week', 'days': days, 'marks': marks or {}, 'short': short}


def months(marks=None, items=None):
    return {'kind': 'months', 'marks': marks or {}, 'items': items}


def money(groups):
    """groups: list of {'label': 'P', 'items': [('coin', 5), ('note', 10), ...]}."""
    return {'kind': 'money', 'groups': groups}


def table(header, rows, widths=None, align=None):
    return {'kind': 'table', 'header': header, 'rows': rows, 'widths': widths, 'align': align}


def equations(rows, size=34, gap=8):
    """Rows of tokens drawn without boxes: ('shape', kind), ('emoji', ch), '?', numbers, '+', '=' ..."""
    return {'kind': 'equations', 'rows': rows, 'size': size, 'gap': gap}


def sticks(segments, w, h, color=(150, 90, 40), width=4.0):
    """Matchstick drawing: segments are ((x1, y1), (x2, y2)) in points."""
    return {'kind': 'sticks', 'segments': segments, 'w': w, 'h': h, 'color': color, 'width': width}


def clocks(times, labels=None, r=46):
    """Analogue clocks. times: list of (hour, minute) or None for a blank face."""
    return {'kind': 'clocks', 'times': times, 'labels': labels, 'r': r}


def stack(figs, gap=10):
    """Several figures, one under the other."""
    return {'kind': 'stack', 'figs': figs, 'gap': gap}


def side(figs, gap=18):
    """Several figures side by side."""
    return {'kind': 'side', 'figs': figs, 'gap': gap}


# ---------------------------------------------------------------- renderers

def _cards(f):
    c = card_row(f['items'], size=f.get('size', 34), gap=f.get('gap', 10), labels=f.get('labels'),
                 fill=f.get('fill', 'yellow'), font_size=f.get('font_size'), width=f.get('width'))
    return c.trim()


def _objects(f):
    item, gap, boxed = f['item'], f['gap'], f['boxed']
    ims = []
    for g in f['groups']:
        rows = g.get('rows')
        if rows is None:
            its, cols = g['items'], g.get('cols', f['cols'])
            rows = [its[i:i + cols] for i in range(0, len(its), cols)]
        ncol = max(len(r) for r in rows) if rows else 1
        pad = 8 if boxed else 2
        W = pad * 2 + ncol * item + (ncol - 1) * gap
        H = pad * 2 + len(rows) * item + (len(rows) - 1) * gap
        lab = g.get('label')
        lw = Canvas(1, 1).text_w(lab, f['label_size']) + 8 if lab else 0
        off_x = max(0, (lw - W) / 2)
        c = Canvas(max(W, lw) + 4, H + (24 if lab else 0) + 4)
        if boxed:
            c.rect(2 + off_x, 2, W, H, g.get('fill', 'white'), INK, 1.4, 8, dashed=g.get('dashed', False))
        for r, row in enumerate(rows):
            off = (ncol - len(row)) * (item + gap) / 2 if g.get('center', True) else 0
            for k, e in enumerate(row):
                cx = 2 + off_x + pad + off + k * (item + gap) + item / 2
                cy = 2 + pad + r * (item + gap) + item / 2
                if e in (None, '', ' '):
                    continue
                if isinstance(e, tuple):
                    c.shape(e[0], cx, cy, item * 0.8, fill=e[1] if len(e) > 1 else None)
                elif len(e) <= 2 and not e.isascii():
                    c.emoji(e, cx, cy, item * 0.92)
                else:
                    c.text(cx, cy, e, item * 0.45)
        if lab:
            c.text(2 + off_x + W / 2, H + 16, lab, f['label_size'])
        ims.append(c.im)
    return _join(ims, 16, horizontal=f.get('horizontal', True))


def _join(ims, gap, horizontal=True, align='center'):
    g = int(gap * K)
    if horizontal:
        W = sum(i.size[0] for i in ims) + g * (len(ims) - 1)
        H = max(i.size[1] for i in ims)
        out = Image.new('RGB', (W, H), 'white')
        x = 0
        for i in ims:
            out.paste(i, (x, (H - i.size[1]) // 2 if align == 'center' else 0))
            x += i.size[0] + g
    else:
        W = max(i.size[0] for i in ims)
        H = sum(i.size[1] for i in ims) + g * (len(ims) - 1)
        out = Image.new('RGB', (W, H), 'white')
        y = 0
        for i in ims:
            out.paste(i, ((W - i.size[0]) // 2, y))
            y += i.size[1] + g
    return out


def _numberline(f):
    a, b, st = f['start'], f['end'], f['step']
    W = f['width']
    n = int(round((b - a) / st))
    m = 26
    unit = (W - 2 * m) / n
    hops = f['hops']
    top = 40 if hops else 14
    c = Canvas(W, top + 50)
    y = top + 8
    c.line(6, y, W - 6, y, INK, 1.8)
    for xx, s in ((6, 1), (W - 6, -1)):
        c.poly([(xx, y), (xx + s * 9, y - 5), (xx + s * 9, y + 5)], INK, INK, 1)
    for i in range(n + 1):
        v = a + i * st
        x = m + i * unit
        c.line(x, y - 7, x, y + 7, INK, 1.6)
        if v in f['marks']:
            c.text(x, y + 20, f['marks'][v], 13, True, PURPLE)
        elif v in f['hide']:
            pass
        elif i % f['label_every'] == 0 or i == n:
            c.text(x, y + 20, v, 12, True)
    for (p, q) in hops:
        x1 = m + (p - a) / st * unit
        x2 = m + (q - a) / st * unit
        box = [x1 * K, (y - 30) * K, x2 * K, (y + 4) * K]
        if x2 < x1:
            box = [x2 * K, (y - 30) * K, x1 * K, (y + 4) * K]
        c.d.arc(box, 180, 360, fill=PURPLE, width=int(1.6 * K))
        tip = x2
        s = 1 if q > p else -1
        c.poly([(tip, y - 13), (tip - s * 5, y - 21), (tip + s * 1, y - 22)], PURPLE, PURPLE, 1)
    return c.trim()


def _blocks(f):
    ims = []
    for idx, st in enumerate(f['sets']):
        hnd, t, o = (st if len(st) == 3 else (0,) + tuple(st))
        rod_w, rod_h, cube = 15, 150, 15
        W = 8 + hnd * (rod_h + 8) + t * (rod_w + 5) + 16 + ((o + 4) // 5) * (cube + 4) + 8
        c = Canvas(max(W, 40), rod_h + 40)
        x = 8
        for _ in range(hnd):
            c.rect(x, 6, rod_h, rod_h, 'green', INK, 1.2)
            for k in range(1, 10):
                c.line(x + k * rod_h / 10, 6, x + k * rod_h / 10, 6 + rod_h, INK, 0.6)
                c.line(x, 6 + k * rod_h / 10, x + rod_h, 6 + k * rod_h / 10, INK, 0.6)
            x += rod_h + 8
        for _ in range(t):
            c.rect(x, 6, rod_w, rod_h, 'blue', INK, 1.2)
            for k in range(1, 10):
                c.line(x, 6 + k * rod_h / 10, x + rod_w, 6 + k * rod_h / 10, INK, 0.7)
            x += rod_w + 5
        x += 10
        for k in range(o):
            col, row = divmod(k, 5)
            c.rect(x + col * (cube + 4), 6 + rod_h - (row + 1) * (cube + 3), cube, cube, 'peach', INK, 1.1)
        if f.get('labels'):
            c.text(c.w / 2, rod_h + 26, f['labels'][idx], 13)
        ims.append(c.trim(2))
    return _join(ims, 22)


def _shapes(f):
    items, s, gap = f['items'], f['size'], f['gap']
    n = len(items)
    extra = 20 if f.get('divider_after') is not None else 0
    W = 8 + n * s + (n - 1) * gap + extra + 8
    c = Canvas(W, s + 16 + (24 if f.get('labels') else 0))
    x = 8
    for i, it in enumerate(items):
        kind, fill = (it, None) if isinstance(it, str) else (it[0], it[1])
        c.shape(kind, x + s / 2, 8 + s / 2, s * (0.82 if kind != 'circle' else 0.8), fill=fill)
        if f.get('labels'):
            c.text(x + s / 2, 8 + s + 16, f['labels'][i], 12)
        x += s + gap
        if f.get('divider_after') is not None and i == f['divider_after']:
            c.line(x - gap / 2 + 10, 0, x - gap / 2 + 10, s + 16, RED, 2, dashed=True)
            x += extra
    return c.trim()


def _drawing(f):
    """Free drawing; a 40 pt margin round the stated size keeps labels near the edge from being cut."""
    sc, M = f.get('scale', 1.0), 40
    c = Canvas(f['w'] * sc + 2 * M, f['h'] * sc + 2 * M)
    X = lambda v: v * sc + M      # coordinates
    L = lambda v: v * sc          # lengths
    for p in f['prims']:
        k = p[0]
        if k == 'poly':
            c.poly([(X(x), X(y)) for x, y in p[1]], p[2] if len(p) > 2 else 'white', INK, 1.6, p[3] if len(p) > 3 else False)
        elif k == 'polyline':
            pts = [(X(x), X(y)) for x, y in p[1]]
            for (x1, y1), (x2, y2) in zip(pts, pts[1:]):
                c.line(x1, y1, x2, y2, INK, 1.6, p[2] if len(p) > 2 else False)
        elif k == 'rect':
            c.rect(X(p[1]), X(p[2]), L(p[3]), L(p[4]), p[5] if len(p) > 5 else 'white', INK, 1.6, 0, p[6] if len(p) > 6 else False)
        elif k == 'circle':
            c.circle(X(p[1]), X(p[2]), L(p[3]), p[4] if len(p) > 4 else 'white', INK, 1.6, p[5] if len(p) > 5 else False)
        elif k == 'line':
            c.line(X(p[1]), X(p[2]), X(p[3]), X(p[4]), p[6] if len(p) > 6 else INK, 1.6 if len(p) <= 7 else p[7], p[5] if len(p) > 5 else False)
        elif k == 'text':
            c.text(X(p[1]), X(p[2]), p[3], p[4] if len(p) > 4 else 13, True, p[5] if len(p) > 5 else INK)
        elif k == 'dot':
            r = p[3] if len(p) > 3 else 3.2
            c.circle(X(p[1]), X(p[2]), r, INK, INK, 1)
        elif k == 'emoji':
            c.emoji(p[1], X(p[2]), X(p[3]), p[4])
        elif k == 'shape':
            c.shape(p[1], X(p[2]), X(p[3]), L(p[4]), fill=p[5] if len(p) > 5 else None)
        elif k == 'qbox':
            c.shape('qbox', X(p[1]), X(p[2]), p[3] if len(p) > 3 else 26)
        else:
            raise ValueError(k)
    return c.trim()


def _grid(f):
    rows, cell = f['rows'], f['cell']
    nr, nc = len(rows), max(len(r) for r in rows)
    widths = f.get('widths') or [cell] * nc
    c = Canvas(sum(widths) + 8, nr * cell + 8)
    for r, row in enumerate(rows):
        x = 4
        for k, v in enumerate(row):
            w = widths[k]
            fill = 'white'
            if f.get('fills'):
                fill = f['fills'][r][k] or 'white'
            if v is None:
                x += w
                continue
            c.rect(x, 4 + r * cell, w, cell, fill, INK, 1.4)
            if v == '?':
                c.rect(x + 5, 4 + r * cell + 5, w - 10, cell - 10, 'white', PURPLE, 1.6, 3, dashed=True)
                c.text(x + w / 2, 4 + r * cell + cell / 2, '?', cell * 0.42, True, PURPLE)
            elif isinstance(v, tuple) and v[0] == 'emoji':
                c.emoji(v[1], x + w / 2, 4 + r * cell + cell / 2, cell * 0.7)
            elif isinstance(v, tuple) and v[0] == 'shape':
                c.shape(v[1], x + w / 2, 4 + r * cell + cell / 2, cell * 0.6, fill=v[2] if len(v) > 2 else None)
            elif v != '':
                fs = f.get('font_size') or (cell * 0.42 if len(str(v)) <= 3 else cell * 0.3)
                c.text(x + w / 2, 4 + r * cell + cell / 2 + 1, v, fs)
            x += w
    return c.trim()


DAYS = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']
MONTHS = ['January', 'February', 'March', 'April', 'May', 'June', 'July', 'August', 'September',
          'October', 'November', 'December']


def _week(f):
    days = f['days']
    w, h = 62, 46
    c = Canvas(len(days) * (w + 6) + 8, h + 12)
    for i, d in enumerate(days):
        x = 4 + i * (w + 6)
        m = f['marks'].get(d) if isinstance(d, str) else None
        m = f['marks'].get(i, m)
        lab = d[:3] if (f['short'] and isinstance(d, str) and d in DAYS) else d
        if lab == '?':
            c.rect(x, 4, w, h, 'white', PURPLE, 1.8, 5, dashed=True)
            c.text(x + w / 2, 4 + h / 2, '?', 20, True, PURPLE)
            continue
        c.rect(x, 4, w, h, 'yellow' if m else 'white', INK, 1.5, 5)
        if m:
            c.text(x + w / 2, 4 + 15, lab, 12)
            if m == 'star':
                c.shape('star', x + w / 2, 4 + 33, 15)
            elif m in ('✓', 'tick'):
                c.text(x + w / 2, 4 + 33, '✓', 14)
            else:
                c.emoji(m, x + w / 2, 4 + 33, 16)
        else:
            c.text(x + w / 2, 4 + h / 2, lab, 12)
    return c.trim()


def _months(f):
    items = f.get('items') or MONTHS
    w, h, cols = 88, 44, 6
    rows = (len(items) + cols - 1) // cols
    c = Canvas(cols * (w + 6) + 8, rows * (h + 8) + 8)
    for i, mth in enumerate(items):
        r, k = divmod(i, cols)
        x, y = 4 + k * (w + 6), 4 + r * (h + 8)
        mk = f['marks'].get(mth)
        if mth == '?':
            c.rect(x, y, w, h, 'white', PURPLE, 1.8, 5, dashed=True)
            c.text(x + w / 2, y + h / 2, '?', 20, True, PURPLE)
            continue
        c.rect(x, y, w, h, 'yellow' if mk else 'white', INK, 1.5, 5)
        if mk:
            c.shape('star', x + w / 2, y + 13, 14)
            c.text(x + w / 2, y + 32, mth, 11)
        else:
            c.text(x + w / 2, y + h / 2, mth, 11)
    return c.trim()


def _money(f):
    ims = []
    for g in f['groups']:
        its = g['items']
        x, parts = 0, []
        coins = [v for k, v in its if k == 'coin']
        notes = [v for k, v in its if k == 'note']
        W = 10 + len(notes) * 86 + len(coins) * 44 + 10
        c = Canvas(max(W, 60), 70 + (24 if g.get('label') else 0))
        x = 8
        for v in notes:
            c.rect(x, 12, 78, 42, 'green', INK, 1.5, 4)
            c.rect(x + 5, 17, 68, 32, None, INK, 0.8, 3)
            c.text(x + 39, 33, f'₹{v}', 16)
            x += 86
        for v in coins:
            r = {1: 14, 2: 15.5, 5: 16.5, 10: 17.5, 20: 18.5}.get(v, 16)
            c.circle(x + 20, 33, r, (214, 214, 214) if v in (1, 2, 5) else 'yellow', INK, 1.5)
            c.circle(x + 20, 33, r - 4, None, INK, 0.7)
            c.text(x + 20, 34, f'₹{v}', 10 if v < 10 else 9)
            x += 44
        if g.get('label'):
            c.text(c.w / 2, 80, g['label'], 13)
        im = c.trim(3)
        if len(f['groups']) > 1:  # frame each group so it is clear which money belongs together
            fr = Canvas(im.size[0] / K + 12, im.size[1] / K + 12)
            fr.rect(2, 2, im.size[0] / K + 8, im.size[1] / K + 8, 'white', (150, 150, 150), 1.2, 8)
            fr.im.paste(im, (int(6 * K), int(6 * K)))
            im = fr.im
        ims.append(im)
    per = f.get('per_row', 2 if len(ims) > 3 else len(ims))
    rows = [_join(ims[i:i + per], 26) for i in range(0, len(ims), per)]
    return rows[0] if len(rows) == 1 else _join(rows, 14, horizontal=False)


def _table(f):
    header, rows = f['header'], f['rows']
    nc = len(header)
    widths = f.get('widths') or [110] * nc
    rh = 30
    c = Canvas(sum(widths) + 8, (len(rows) + 1) * rh + 8)
    for r, row in enumerate([header] + rows):
        x = 4
        for k, v in enumerate(row):
            c.rect(x, 4 + r * rh, widths[k], rh, 'lilac' if r == 0 else 'white', INK, 1.3)
            num = isinstance(v, (int,)) or (isinstance(v, str) and v.replace('₹', '').isdigit())
            if r == 0:
                c.text(x + widths[k] / 2, 4 + r * rh + rh / 2, v, 12, True)
            elif num:
                c.text(x + widths[k] - 10, 4 + r * rh + rh / 2, v, 12, False, INK, 'rm')
            elif isinstance(v, tuple) and v[0] == 'emoji':
                c.emoji(v[1], x + widths[k] / 2, 4 + r * rh + rh / 2, 20)
            else:
                c.text(x + 10, 4 + r * rh + rh / 2, v, 12, False, INK, 'lm')
            x += widths[k]
    return c.trim()


def _equations(f):
    s, gap = f['size'], f['gap']
    ims = []
    for row in f['rows']:
        widths = []
        for t in row:
            if isinstance(t, tuple) or t == '?':
                widths.append(s)
            else:
                widths.append(max(18, len(str(t)) * s * 0.36))
        W = sum(widths) + gap * (len(row) - 1) + 12
        c = Canvas(W, s + 12)
        x = 6
        for t, w in zip(row, widths):
            cx, cy = x + w / 2, 6 + s / 2
            if t == '?':
                c.shape('qbox', cx, cy, s * 0.9)
            elif isinstance(t, tuple) and t[0] == 'shape':
                c.shape(t[1], cx, cy, s * 0.8, fill=t[2] if len(t) > 2 else None)
            elif isinstance(t, tuple) and t[0] == 'emoji':
                c.emoji(t[1], cx, cy, s * 0.85)
            else:
                c.text(cx, cy + 1, t, s * 0.55)
            x += w + gap
        ims.append(c.trim(2))
    return _join(ims, 8, horizontal=False)


def _sticks(f):
    c = Canvas(f['w'], f['h'])
    for (x1, y1), (x2, y2) in f['segments']:
        c.d.line([c.P(x1, y1), c.P(x2, y2)], fill=f['color'], width=int(f['width'] * K))
        for (x, y) in ((x1, y1), (x2, y2)):
            r = f['width'] * 0.75
            c.circle(x, y, r, (200, 40, 40), (120, 20, 20), 0.6)
    return c.trim()


def _clocks(f):
    r = f['r']
    ims = []
    for i, t in enumerate(f['times']):
        c = Canvas(2 * r + 20, 2 * r + (40 if f.get('labels') else 20))
        cx, cy = r + 10, r + 10
        c.circle(cx, cy, r, 'white', INK, 2.2)
        for k in range(60):
            a = math.radians(k * 6 - 90)
            r1 = r - (6 if k % 5 == 0 else 3)
            c.line(cx + r1 * math.cos(a), cy + r1 * math.sin(a), cx + (r - 1) * math.cos(a), cy + (r - 1) * math.sin(a), INK, 1.4 if k % 5 == 0 else 0.6)
        for n in range(1, 13):
            a = math.radians(n * 30 - 90)
            c.text(cx + (r - 12) * math.cos(a), cy + (r - 12) * math.sin(a) + 0.5, n, r * 0.19)
        if t is not None:
            hh, mm = t
            am = math.radians(mm * 6 - 90)
            ah = math.radians((hh % 12) * 30 + mm * 0.5 - 90)
            c.line(cx, cy, cx + r * 0.42 * math.cos(ah), cy + r * 0.42 * math.sin(ah), INK, 4.2)
            c.line(cx, cy, cx + r * 0.64 * math.cos(am), cy + r * 0.64 * math.sin(am), INK, 2.2)
        c.circle(cx, cy, 3.2, INK, INK, 1)
        if f.get('labels'):
            c.text(cx, 2 * r + 30, f['labels'][i], 13)
        ims.append(c.trim(2))
    return _join(ims, 22)


def to_image(f):
    k = f['kind']
    if k == 'stack':
        return _join([to_image(x) for x in f['figs']], f['gap'], horizontal=False)
    if k == 'side':
        return _join([to_image(x) for x in f['figs']], f['gap'], horizontal=True)
    return {'cards': _cards, 'objects': _objects, 'numberline': _numberline, 'blocks': _blocks,
            'shapes': _shapes, 'drawing': _drawing, 'grid': _grid, 'week': _week, 'months': _months,
            'money': _money, 'table': _table, 'equations': _equations, 'sticks': _sticks, 'clocks': _clocks}[k](f)


def render(f, path, max_w=440):
    """Render to PNG; returns display size in points (width, height), capped at max_w wide."""
    im = to_image(f)
    im.save(path, optimize=True)
    w, h = im.size[0] / K, im.size[1] / K
    if w > max_w:
        h, w = h * max_w / w, max_w
    return round(w, 1), round(h, 1)
