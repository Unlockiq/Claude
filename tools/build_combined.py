"""Combine five AMO practice papers into one booklet in the REAL olympiad format.

Usage:
  python3 build_combined.py CLASS PAPERS_DIR VERSION COVER_IMAGE LOGO_IMAGE OUT.docx

Reads PAPERS_DIR/AMO_C{CLASS}_L1_PracticePaper{1..5}_{VERSION}.docx and writes
one .docx laid out like the REAL consolidated booklet:
  * section 1, a front cover with no header or footer: logo, olympiad name,
    the class cover image, "PRACTICE PAPERS", class, student-details table
    and publisher lines;
  * one section per paper, each keeping the papers' page set-up, with the
    header "Aryabhatta Maths Olympiad (AMO) Level-1 Sample Papers" (amber rule)
    and the brand footer (grey rule; logo, "Unlock IQ Institute Pvt. Ltd. ·
    www.unlockiqinstitute.com" on the left, "Page x of y" on the right); the
    first page of each paper shows the footer only;
  * each paper opens on a REAL-style page (logo, name, PRACTICE PAPER-n,
    CLASS n, details table, "Hello, friend!" box, parents box) built from
    that paper's own cover text;
  * the questions, answer sheet and answer key of every paper unchanged.
"""
import html, io, re, sys, zipfile
from PIL import Image

EMU = 12700  # per point
NAVY, RED, PURPLE, GREY_T, DARK = '1F3864', 'C00000', '6A1B9A', '595959', '222222'
LABEL_FILL, GRID = 'DEEBF7', 'BFBFBF'
YEL_FILL, YEL_LINE, GRY_FILL, GRY_LINE = 'FFF8E1', 'FFD966', 'F2F2F2', 'BFBFBF'
TEXT_W = 9978  # twips between the AMO page margins
HEADER = 'Aryabhatta Maths Olympiad (AMO) Level-1 Sample Papers'
REL = 'http://schemas.openxmlformats.org/officeDocument/2006/relationships/'


def esc(t):
    return html.escape(t, quote=False)


def run(text, size=11, bold=False, italic=False, color=None):
    rpr = '<w:b/>' if bold else '<w:b w:val="0"/>'
    rpr += '<w:i/>' if italic else '<w:i w:val="0"/>'
    if color:
        rpr += f'<w:color w:val="{color}"/>'
    rpr += f'<w:sz w:val="{int(size * 2)}"/><w:szCs w:val="{int(size * 2)}"/>'
    return f'<w:r><w:rPr>{rpr}</w:rPr><w:t xml:space="preserve">{esc(text)}</w:t></w:r>'


def para(runs, align='left', before=0, after=0, keep=False, sect=''):
    ppr = '<w:keepNext/>' if keep else ''
    ppr += f'<w:spacing w:before="{before}" w:after="{after}" w:line="264" w:lineRule="auto"/>'
    ppr += f'<w:jc w:val="{align}"/>{sect}'
    return f'<w:p><w:pPr>{ppr}</w:pPr>{"".join(runs)}</w:p>'


def image_run(rid, w_pt, h_pt, pid, name):
    cx, cy = int(w_pt * EMU), int(h_pt * EMU)
    return (f'<w:r><w:drawing><wp:inline distT="0" distB="0" distL="0" distR="0" '
            f'xmlns:a="http://schemas.openxmlformats.org/drawingml/2006/main" '
            f'xmlns:pic="http://schemas.openxmlformats.org/drawingml/2006/picture">'
            f'<wp:extent cx="{cx}" cy="{cy}"/><wp:effectExtent l="0" t="0" r="0" b="0"/>'
            f'<wp:docPr id="{pid}" name="{name}"/>'
            f'<wp:cNvGraphicFramePr><a:graphicFrameLocks noChangeAspect="1"/></wp:cNvGraphicFramePr>'
            f'<a:graphic><a:graphicData uri="http://schemas.openxmlformats.org/drawingml/2006/picture">'
            f'<pic:pic><pic:nvPicPr><pic:cNvPr id="0" name="{name}"/><pic:cNvPicPr/></pic:nvPicPr>'
            f'<pic:blipFill><a:blip r:embed="{rid}"/><a:stretch><a:fillRect/></a:stretch></pic:blipFill>'
            f'<pic:spPr><a:xfrm><a:off x="0" y="0"/><a:ext cx="{cx}" cy="{cy}"/></a:xfrm>'
            f'<a:prstGeom prst="rect"><a:avLst/></a:prstGeom></pic:spPr></pic:pic>'
            f'</a:graphicData></a:graphic></wp:inline></w:drawing></w:r>')


def borders(color, sz):
    return ''.join(f'<w:{s} w:val="single" w:sz="{sz}" w:space="0" w:color="{color}"/>'
                   for s in ('top', 'left', 'bottom', 'right', 'insideH', 'insideV'))


def table(rows, widths, line, sz=4, fills=None, mar=(70, 100)):
    out = (f'<w:tbl><w:tblPr><w:tblW w:w="{sum(widths)}" w:type="dxa"/><w:jc w:val="center"/>'
           f'<w:tblBorders>{borders(line, sz)}</w:tblBorders><w:tblLayout w:type="fixed"/>'
           f'<w:tblCellMar><w:top w:w="{mar[0]}" w:type="dxa"/><w:left w:w="{mar[1]}" w:type="dxa"/>'
           f'<w:bottom w:w="{mar[0]}" w:type="dxa"/><w:right w:w="{mar[1]}" w:type="dxa"/></w:tblCellMar>'
           f'</w:tblPr><w:tblGrid>' + ''.join(f'<w:gridCol w:w="{w}"/>' for w in widths) + '</w:tblGrid>')
    for row in rows:
        out += '<w:tr><w:trPr><w:cantSplit/></w:trPr>'
        for i, cell in enumerate(row):
            shd = f'<w:shd w:val="clear" w:color="auto" w:fill="{fills[i]}"/>' if fills and fills[i] else ''
            out += f'<w:tc><w:tcPr><w:tcW w:w="{widths[i]}" w:type="dxa"/>{shd}</w:tcPr>{cell}</w:tc>'
        out += '</w:tr>'
    return out + '</w:tbl>'


def box(paras, fill, line):
    return table([[''.join(paras)]], [TEXT_W], line, sz=8, fills=[fill], mar=(120, 170))


def spacer(pts, sect=''):
    return (f'<w:p><w:pPr><w:spacing w:before="0" w:after="0" w:line="{max(int(pts * 20), 20)}" '
            f'w:lineRule="exact"/><w:rPr><w:sz w:val="2"/></w:rPr>{sect}</w:pPr></w:p>')


def cover_info(xml):
    """Pull the label/value table, pupil bullets and parent notes from a paper cover."""
    body = xml[xml.index('<w:body>'):xml.index('<w:p><w:pPr><w:pageBreakBefore/>')]
    texts = [html.unescape(t) for t in re.findall(r'<w:t[^>]*>([^<]*)</w:t>', body)]
    texts = [t for t in texts if t.strip()]
    i = texts.index('Questions')
    j = texts.index('Hello, friend!')
    k = texts.index('For parents and teachers')
    rows = list(zip(texts[i:j:2], texts[i + 1:j:2]))
    bullets = [t for t in texts[j + 1:k] if t.strip() != '•']
    notes = [t for t in texts[k + 1:] if t not in ('Name:', 'School:', 'Roll No.:')]
    return rows, bullets, notes


LABELS = {'Questions': 'Total Questions', 'Marks': 'Total Marks', 'Negative marking': 'Negative Marking'}


def paper_page(n, cls, info, logo_rid, pid):
    rows, bullets, notes = info
    out = para([image_run(logo_rid, 64.4, 69.8, pid, f'logo{n}')], 'center', after=80)
    out += para([run('ARYABHATTA MATHS OLYMPIAD', 18, True, color=NAVY)], 'center', after=20)
    out += para([run('Level 1', 10, color=GREY_T)], 'center', after=200)
    out += para([run(f'PRACTICE PAPER-{n}', 13.5, True, color=RED)], 'center', after=40)
    out += para([run(f'CLASS {cls}', 26, True, color=NAVY)], 'center', after=200)
    trs = [[para([run(LABELS.get(a, a), 11, True)]), para([run(b, 11)])] for a, b in rows]
    out += table(trs, [3150, TEXT_W - 3150], GRID, fills=[LABEL_FILL, None], mar=(95, 100))
    out += spacer(16)
    hello = [para([run('\U0001F44B ', 13), run('Hello, friend! How to do this paper:', 13, True, color=NAVY)], after=100)]
    hello += [para([run('⭐ ', 12), run(b, 12)], after=70) for b in bullets]
    out += box(hello, YEL_FILL, YEL_LINE)
    out += spacer(14)
    par = [para([run('For parents and teachers', 8.5, True, color=NAVY)], after=50)]
    par += [para([run('•  ', 8), run(t, 8)], after=30) for t in notes]
    out += box(par, GRY_FILL, GRY_LINE)
    return out


def front_cover(cls, logo_rid, cover_rid, cover_size, sect):
    w = 286.0
    h = w * cover_size[1] / cover_size[0]
    out = para([image_run(logo_rid, 44.7, 48.3, 9001, 'logo')], 'center', after=80)
    out += para([run('ARYABHATTA MATHS OLYMPIAD', 27.5, True, color=PURPLE)], 'center', after=200)
    out += para([image_run(cover_rid, w, h, 9002, 'cover')], 'center', after=160)
    out += para([run('PRACTICE PAPERS', 18, True, color=PURPLE)], 'center', after=20)
    out += para([run(f'Class {cls}', 16, color=DARK)], 'center', after=20)
    out += para([run('Five full practice papers  ·  with answer keys & detailed solutions', 10, color='666666')], 'center', after=160)
    cells = [('Name:', '____________________'), ('Class & Section:', '________________'),
             ('Roll No.:', '________________'), ('School:', '____________________'),
             ('City:', '____________________'), ('Date:', '____________________')]
    rows = [[para([run(a + ' ', 10.5, True), run(b, 10.5)]) for a, b in cells[i:i + 2]] for i in (0, 2, 4)]
    out += table(rows, [TEXT_W // 2, TEXT_W - TEXT_W // 2], '999999', sz=6)
    out += spacer(18)
    out += para([run('Published by Unlock IQ Institute Pvt. Ltd.', 9.5, True, color=DARK)], 'center', after=20)
    out += para([run('Register for Olympiads:  www.aryabhattamathsolympiad.com/student-registration', 8.5, color='666666')],
                'center', sect=sect)
    return out


def field(code, size, color):
    rpr = f'<w:rPr><w:b w:val="0"/><w:color w:val="{color}"/><w:sz w:val="{size * 2}"/><w:szCs w:val="{size * 2}"/></w:rPr>'
    return (f'<w:r>{rpr}<w:fldChar w:fldCharType="begin"/></w:r><w:r>{rpr}<w:instrText xml:space="preserve"> {code} </w:instrText></w:r>'
            f'<w:r>{rpr}<w:fldChar w:fldCharType="separate"/></w:r><w:r>{rpr}<w:t>1</w:t></w:r>'
            f'<w:r>{rpr}<w:fldChar w:fldCharType="end"/></w:r>')


def footer_xml(root):
    """Brand footer: grey rule; logo, institute and website on the left; "Page X of Y" on the right."""
    ppr = (f'<w:pPr><w:pStyle w:val="Footer"/><w:pBdr><w:top w:val="single" w:sz="6" w:space="6" w:color="BFBFBF"/></w:pBdr>'
           f'<w:tabs><w:tab w:val="clear" w:pos="4680"/><w:tab w:val="clear" w:pos="9360"/>'
           f'<w:tab w:val="right" w:pos="{TEXT_W}"/></w:tabs>'
           f'<w:spacing w:before="0" w:after="0" w:line="240" w:lineRule="auto"/><w:jc w:val="left"/></w:pPr>')
    body = (image_run('rIdLogo', 15.0, 16.3, 8001, 'footer logo') + run('   ', 9.5)
            + run('Unlock IQ Institute Pvt. Ltd.  \u00b7  www.unlockiqinstitute.com', 9.5, color=GREY_T)
            + '<w:r><w:tab/></w:r>' + run('Page ', 9.5, color=GREY_T) + field('PAGE', 13, '111111')
            + run(' of ', 9.5, color=GREY_T) + field('NUMPAGES', 13, '111111'))
    return f'{root}<w:p>{ppr}{body}</w:p></w:ftr>'


def main(cls, src, ver, cover_img, logo_img, out_path):
    names = [f'{src}/AMO_C{cls}_L1_PracticePaper{p}_{ver}.docx' for p in range(1, 6)]
    papers = []
    for n in names:
        with zipfile.ZipFile(n) as z:
            papers.append({i.filename: z.read(i.filename) for i in z.infolist()})
    base = papers[0]
    new_rels, parts = [], {}

    def add_part(name, data, kind):
        rid = f'rIdM{len(new_rels) + 1}'
        new_rels.append(f'<Relationship Id="{rid}" Type="{REL}{kind}" Target="{name}"/>')
        parts[f'word/{name}'] = data
        return rid

    im = Image.open(cover_img).convert('RGB')
    buf = io.BytesIO(); im.save(buf, 'JPEG', quality=92)
    cover_rid = add_part('media/cover.jpeg', buf.getvalue(), 'image')
    buf = io.BytesIO(); Image.open(logo_img).convert('RGB').save(buf, 'PNG')
    logo_rid = add_part('media/logo.png', buf.getvalue(), 'image')

    # Page set-up of the papers; the cover section has the same size and margins.
    x0 = base['word/document.xml'].decode()
    sect0 = re.search(r'<w:sectPr.*?</w:sectPr>', x0, re.S).group(0)
    setup = ''.join(re.findall(r'<w:pgSz[^>]*/>|<w:pgMar[^>]*/>|<w:cols[^>]*/>|<w:docGrid[^>]*/>', sect0))
    cover_sect = f'<w:sectPr>{setup}</w:sectPr>'
    root = re.match(r'.*?<w:ftr [^>]*>', base['word/footer1.xml'].decode(), re.S).group(0)
    footer_rid = add_part('footer1.xml', footer_xml(root).encode(), 'footer')
    parts['word/_rels/footer1.xml.rels'] = (
        '<?xml version="1.0" encoding="UTF-8" standalone="yes"?>'
        '<Relationships xmlns="http://schemas.openxmlformats.org/package/2006/relationships">'
        f'<Relationship Id="rIdLogo" Type="{REL}image" Target="media/logo.png"/></Relationships>').encode()

    hdr = re.sub(r'<w:t>[^<]*</w:t>', '<w:t>' + esc(HEADER) + '</w:t>', base['word/header1.xml'].decode(), count=1)
    header_rid = add_part('header1.xml', hdr.encode(), 'header')
    body, pid = front_cover(cls, logo_rid, cover_rid, im.size, cover_sect), 1
    for n, pk in enumerate(papers, 1):
        x = pk['word/document.xml'].decode()
        prels = dict(re.findall(r'Id="(rId\d+)"[^>]*Target="(media/[^"]+)"',
                                pk['word/_rels/document.xml.rels'].decode()))
        content = x[x.index('<w:p><w:pPr><w:pageBreakBefore/>'):x.rindex('<w:sectPr')]
        mapping = {old: add_part(f'media/p{n}_{t.split("/")[-1]}', pk['word/' + t], 'image')
                   for old, t in prels.items()}
        content = re.sub(r'r:embed="(rId\d+)"', lambda m: f'r:embed="{mapping[m.group(1)]}"', content)

        def renum(m):
            nonlocal pid
            pid += 1
            return f'<wp:docPr id="{pid}"'
        content = re.sub(r'<wp:docPr id="\d+"', renum, content)
        sect = (f'<w:sectPr><w:headerReference w:type="default" r:id="{header_rid}"/>'
                f'<w:footerReference w:type="default" r:id="{footer_rid}"/>'
                f'<w:footerReference w:type="first" r:id="{footer_rid}"/>'
                f'<w:type w:val="nextPage"/>{setup.replace("<w:docGrid", "<w:titlePg/><w:docGrid")}</w:sectPr>')
        body += paper_page(n, cls, cover_info(x), logo_rid, 9100 + n) + content
        body += spacer(1, sect) if n < 5 else sect

    doc = x0[:x0.index('<w:body>')] + '<w:body>' + body + '</w:body></w:document>'
    rels = base['word/_rels/document.xml.rels'].decode()
    rels = re.sub(r'<Relationship [^>]*relationships/(image|header|footer)"[^>]*/>', '', rels)
    rels = rels.replace('</Relationships>', ''.join(new_rels) + '</Relationships>')
    ct = base['[Content_Types].xml'].decode()
    ct = re.sub(r'<Override PartName="/word/(header|footer)\d*\.xml"[^>]*/>', '', ct)
    hf = 'application/vnd.openxmlformats-officedocument.wordprocessingml.'
    ct = ct.replace('</Types>', ''.join(
        f'<Override PartName="/{p}" ContentType="{hf}{"header" if "header" in p else "footer"}+xml"/>'
        for p in parts if re.match(r'word/(header|footer)\d+\.xml$', p)) + '</Types>')
    for ext, mime in (('jpeg', 'image/jpeg'), ('png', 'image/png')):
        if f'Extension="{ext}"' not in ct:
            ct = ct.replace('</Types>', f'<Default Extension="{ext}" ContentType="{mime}"/></Types>')
    with zipfile.ZipFile(out_path, 'w', zipfile.ZIP_DEFLATED) as o:
        for name, data in base.items():
            if name.startswith('word/media/') or re.match(r'word/(header|footer)\d*\.xml$', name):
                continue
            if name == 'word/document.xml':
                data = doc.encode()
            elif name == 'word/_rels/document.xml.rels':
                data = rels.encode()
            elif name == '[Content_Types].xml':
                data = ct.encode()
            o.writestr(name, data)
        for name, data in parts.items():
            o.writestr(name, data)
    print(f'{out_path}: 5 papers, {sum(1 for p in parts if "/media/" in p)} images')


if __name__ == '__main__':
    main(*sys.argv[1:7])
