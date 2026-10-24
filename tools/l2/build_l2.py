"""Build an AMO Level-2 practice-paper booklet in the Level-1 consolidated (REAL) format.

Usage:
  python3 tools/l2/build_l2.py CLASS SET_NO FIRST_PAPER LAST_PAPER QUESTIONS_DIR OUT.docx

Reads QUESTIONS_DIR/paperNN.py for each paper (a list QUESTIONS of 30 question dicts, see
questions/level2/README.md), checks every paper against the house rules, renders the
pictures and writes one .docx laid out exactly like the Level-1 consolidated booklet:
front cover, then for each paper an opening page, the questions in Part bands, an answer
sheet and the answer key with solutions. Convert with
  soffice --headless --convert-to pdf OUT.docx
"""
import html, io, os, random, re, sys, zipfile
from PIL import Image

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.dirname(os.path.dirname(HERE))
sys.path.insert(0, HERE)
sys.path.insert(0, os.path.dirname(HERE))
import build_combined as bc  # noqa: E402
import figures as F  # noqa: E402
import checks  # noqa: E402

TEMPLATE = os.path.join(ROOT, 'papers/combined/AMO_Class-1_Practice_Papers.docx')
LOGO = os.path.join(ROOT, 'assets/unlockiq_logo.png')
PURPLE_T, AMBER, WHITE = '5A2D8F', 'E8A800', 'FFFFFF'
bc.HEADER = 'Aryabhatta Maths Olympiad (AMO) Level-2 Practice Papers'

BLUEPRINT = {  # class: (Section I parts as (chapter, band title, count), Section II pairings) — syllabus v5.9
    1: ([('1', 'Part 1 — Number System (Syllabus Chapter 1)', 7),
         ('2', 'Part 2 — Operations (Syllabus Chapter 2)', 6),
         ('5', 'Part 3 — Geometry (Syllabus Chapter 5)', 4),
         ('9', 'Part 4 — Applied Mathematics (Syllabus Chapter 9)', 4),
         ('10', 'Part 5 — Mathematical Reasoning (Syllabus Chapter 10)', 4)],
        ['1+10', '5+10', '9+10', '1+9', '2+5']),
    2: ([('1', 'Part 1 — Number System (Syllabus Chapter 1)', 6),
         ('2', 'Part 2 — Operations (Syllabus Chapter 2)', 6),
         ('5', 'Part 3 — Geometry (Syllabus Chapter 5)', 5),
         ('9', 'Part 4 — Applied Mathematics (Syllabus Chapter 9)', 4),
         ('10', 'Part 5 — Mathematical Reasoning (Syllabus Chapter 10)', 4)],
        ['1+10', '2+10', '5+10', '1+9', '5+9']),
}
PARTS, STARS = BLUEPRINT[1]


def use_class(cls):
    global PARTS, STARS
    PARTS, STARS = BLUEPRINT[cls]
    checks.set_class(cls)


CH_NAME = {'1': 'Ch1', '2': 'Ch2', '5': 'Ch5', '9': 'Ch9', '10': 'Ch10'}


def esc(t):
    return html.escape(str(t), quote=False)


def R(text, size=14, bold=False, italic=False, color=None, font=None):
    rpr = ''
    if font:
        rpr += f'<w:rFonts w:ascii="{font}" w:hAnsi="{font}" w:eastAsia="{font}" w:cs="{font}"/>'
    rpr += '<w:b/>' if bold else '<w:b w:val="0"/>'
    rpr += '<w:i/>' if italic else '<w:i w:val="0"/>'
    if color:
        rpr += f'<w:color w:val="{color}"/>'
    rpr += f'<w:sz w:val="{int(size * 2)}"/><w:szCs w:val="{int(size * 2)}"/>'
    return f'<w:r><w:rPr>{rpr}</w:rPr><w:t xml:space="preserve">{esc(text)}</w:t></w:r>'


def P(runs, before=0, after=0, align=None, keep=False, line=None, extra=''):
    ppr = '<w:keepNext/>' if keep else ''
    ppr += extra
    sp = f'<w:spacing w:before="{before}" w:after="{after}"'
    if line:
        sp += f' w:line="{line}" w:lineRule="auto"'
    ppr += sp + '/>'
    if align:
        ppr += f'<w:jc w:val="{align}"/>'
    return f'<w:p><w:pPr>{ppr}</w:pPr>{"".join(runs)}</w:p>'


def band(title, sub, fill, color, page_break=False):
    pb = '<w:pageBreakBefore/>' if page_break else ''
    bdr = ''.join(f'<w:{s} w:val="single" w:sz="4" w:space="4" w:color="{fill}"/>' for s in ('top', 'left', 'bottom', 'right'))
    runs = (f'<w:r><w:rPr><w:b/><w:i w:val="0"/><w:color w:val="{color}"/><w:sz w:val="26"/></w:rPr><w:t>{esc(title)}</w:t></w:r>')
    if sub:
        runs += (f'<w:r><w:rPr><w:b w:val="0"/><w:i w:val="0"/><w:color w:val="{color}"/><w:sz w:val="21"/></w:rPr>'
                 f'<w:t xml:space="preserve">   {esc(sub)}</w:t></w:r>')
    return (f'<w:p><w:pPr><w:keepNext/><w:spacing w:before="80" w:after="120"/><w:shd w:val="clear" w:color="auto" w:fill="{fill}"/>'
            f'{pb}<w:pBdr>{bdr}</w:pBdr><w:ind w:left="85" w:right="85"/></w:pPr>{runs}</w:p>')


def part_band(title):
    bdr = ''.join(f'<w:{s} w:val="single" w:sz="4" w:space="4" w:color="{PURPLE_T}"/>' for s in ('top', 'left', 'bottom', 'right'))
    return (f'<w:p><w:pPr><w:keepNext/><w:spacing w:before="80" w:after="120"/><w:shd w:val="clear" w:color="auto" w:fill="{PURPLE_T}"/>'
            f'<w:pBdr>{bdr}</w:pBdr><w:ind w:left="85" w:right="85"/></w:pPr>'
            f'<w:r><w:rPr><w:b/><w:i w:val="0"/><w:color w:val="FFFFFF"/><w:sz w:val="25"/></w:rPr><w:t>{esc(title)}</w:t></w:r></w:p>')


TBL_PR = ('<w:tblPr><w:tblW w:type="auto" w:w="0"/>{jc}<w:tblLayout w:type="fixed"/>'
          '<w:tblLook w:firstColumn="1" w:firstRow="1" w:lastColumn="0" w:lastRow="0" w:noHBand="0" w:noVBand="1" w:val="04A0"/></w:tblPr>')
CELL_MAR = '<w:tcMar><w:top w:w="30" w:type="dxa"/><w:left w:w="60" w:type="dxa"/><w:bottom w:w="30" w:type="dxa"/><w:right w:w="60" w:type="dxa"/></w:tcMar>'


def opt_table(opts):
    """Options laid out 4 across when short, else 2 by 2 (as in the Level-1 papers)."""
    four = max(len(o) for o in opts) <= 13
    cols = 4 if four else 2
    w = 2451 if four else 4903
    out = f'<w:tbl>{TBL_PR.format(jc="")}<w:tblGrid>' + f'<w:gridCol w:w="{w}"/>' * cols + '</w:tblGrid>'
    for r in range(4 // cols):
        out += '<w:tr><w:trPr><w:cantSplit/></w:trPr>'
        for c in range(cols):
            i = r * cols + c
            out += (f'<w:tc><w:tcPr><w:tcW w:type="dxa" w:w="{w + 1}"/>{CELL_MAR}<w:vAlign w:val="center"/></w:tcPr>'
                    + P([R(f'({"ABCD"[i]})  ', 14, True, color=PURPLE_T), R(opts[i], 14)], 20, 20, keep=True) + '</w:tc>')
        out += '</w:tr>'
    return out + '</w:tbl>'


def question_block(n, q, img_xml, star):
    stem_runs = [R(f'Q{n}.  ', 14, True, color=PURPLE_T), R(q['stem'], 14)]
    if star:
        stem_runs.append(R('   [Star]', 11, False, True, '7F7F7F'))
    inner = ''
    if img_xml:
        inner += P([img_xml], 40, 80, 'center', keep=True)
    inner += P(stem_runs, 40, 80, keep=True, line=269)
    inner += opt_table(q['_opts'])
    inner += ('<w:p><w:pPr><w:spacing w:before="0" w:after="0" w:line="60" w:lineRule="exact"/></w:pPr>'
              '<w:r><w:rPr><w:sz w:val="4"/></w:rPr></w:r></w:p>')
    tbl = (f'<w:tbl>{TBL_PR.format(jc=chr(60) + "w:jc w:val=" + chr(34) + "center" + chr(34) + "/>")}'
           '<w:tblGrid><w:gridCol w:w="9977"/></w:tblGrid><w:tr><w:trPr><w:cantSplit/></w:trPr>'
           f'<w:tc><w:tcPr><w:tcW w:type="dxa" w:w="9978"/>{CELL_MAR}</w:tcPr>{inner}</w:tc></w:tr></w:tbl>')
    return tbl + P([R(' ', 9)])


def bubble_cell(n, shade, w_num=620, w_b=2700):
    fill = '<w:shd w:val="clear" w:color="auto" w:fill="FFF8E1"/>' if shade else ''
    mar = '<w:tcMar><w:top w:w="28" w:type="dxa"/><w:left w:w="60" w:type="dxa"/><w:bottom w:w="28" w:type="dxa"/><w:right w:w="40" w:type="dxa"/></w:tcMar>'
    num = (f'<w:tc><w:tcPr><w:tcW w:type="dxa" w:w="{w_num}"/>{mar}{fill}<w:vAlign w:val="center"/></w:tcPr>'
           + P([R(f'{n}.', 12, True)], align='right') + '</w:tc>')
    bub = (f'<w:tc><w:tcPr><w:tcW w:type="dxa" w:w="{w_b}"/>{mar}{fill}<w:vAlign w:val="center"/></w:tcPr>'
           + P([R('Ⓐ   Ⓑ   Ⓒ   Ⓓ', 15, font='DejaVu Sans')]) + '</w:tc>')
    return num + bub


def answer_sheet(cls, pno):
    out = band('Answer Sheet', f'AMO Level 2 · Class {cls} · Practice Paper {pno}', PURPLE_T, WHITE, page_break=True)
    # name / school / roll row
    widths = [4082, 3628, 2268]
    cells = ''
    for w, lab in zip(widths, ['Name:', 'School:', 'Roll No.:']):
        cells += (f'<w:tc><w:tcPr><w:tcW w:type="dxa" w:w="{w}"/><w:tcBorders><w:bottom w:val="single" w:sz="6" w:space="0" w:color="7F7F7F"/></w:tcBorders>'
                  '<w:tcMar><w:top w:w="100" w:type="dxa"/><w:left w:w="60" w:type="dxa"/><w:bottom w:w="60" w:type="dxa"/><w:right w:w="60" w:type="dxa"/></w:tcMar></w:tcPr>'
                  + P([R(lab, 11, True)]) + '</w:tc>')
    out += (f'<w:tbl>{TBL_PR.format(jc="<w:jc w:val=" + chr(34) + "center" + chr(34) + "/>")}<w:tblGrid>'
            + ''.join(f'<w:gridCol w:w="{w}"/>' for w in widths) + f'</w:tblGrid><w:tr>{cells}</w:tr></w:tbl>')
    out += P([R('Shade or tick one circle for each question.', 10, italic=True, color='595959')], 160, 100)
    grid = [620, 2700] * 3
    out += (f'<w:tbl>{TBL_PR.format(jc="<w:jc w:val=" + chr(34) + "center" + chr(34) + "/>")}<w:tblGrid>'
            + ''.join(f'<w:gridCol w:w="{w}"/>' for w in grid) + '</w:tblGrid>')
    for r in range(10):
        out += '<w:tr>' + ''.join(bubble_cell(c * 10 + r + 1, c * 10 + r + 1 > 25) for c in range(3)) + '</w:tr>'
    out += '</w:tbl>'
    out += P([R('Q26–Q30 are Section II Star Questions. Each joins two chapters.', 10, italic=True, color='595959')], 120, 40)
    box = (P([R('For the parent or teacher', 11, True, color=PURPLE_T)], 0, 80)
           + P([R('Section I correct: ______ / 25          Section II correct: ______ / 5', 11)], 0, 40)
           + P([R('Correct: ______ / 30', 12, True)], 80, 0))
    out += ('<w:tbl>' + TBL_PR.format(jc='<w:jc w:val="center"/>') + '<w:tblGrid><w:gridCol w:w="9977"/></w:tblGrid><w:tr><w:tc>'
            '<w:tcPr><w:tcW w:type="dxa" w:w="9978"/><w:tcBorders>'
            + ''.join(f'<w:{s} w:val="single" w:sz="8" w:space="0" w:color="{PURPLE_T}"/>' for s in ('top', 'left', 'bottom', 'right'))
            + '</w:tcBorders><w:tcMar><w:top w:w="110" w:type="dxa"/><w:left w:w="180" w:type="dxa"/><w:bottom w:w="110" w:type="dxa"/>'
            '<w:right w:w="180" w:type="dxa"/></w:tcMar><w:shd w:val="clear" w:color="auto" w:fill="F1EAFB"/></w:tcPr>'
            + box + '</w:tc></w:tr></w:tbl>')
    return out


def kcell(w, content, fill=None, mar=(40, 70), border='B9A6D9', header=False):
    shd = f'<w:shd w:val="clear" w:color="auto" w:fill="{fill}"/>' if fill else ''
    b = ''.join(f'<w:{s} w:val="single" w:sz="4" w:space="0" w:color="{border}"/>' for s in ('top', 'left', 'bottom', 'right'))
    return (f'<w:tc><w:tcPr><w:tcW w:type="dxa" w:w="{w}"/>{shd}<w:tcBorders>{b}</w:tcBorders>'
            f'<w:tcMar><w:top w:w="{mar[0]}" w:type="dxa"/><w:left w:w="{mar[1]}" w:type="dxa"/><w:bottom w:w="{mar[0]}" w:type="dxa"/>'
            f'<w:right w:w="{mar[1]}" w:type="dxa"/></w:tcMar></w:tcPr>{content}</w:tc>')


def answer_key(cls, pno, qs):
    out = band('Answer Key and Solutions', f'AMO Level 2 · Class {cls} · Practice Paper {pno}', PURPLE_T, WHITE, page_break=True)
    out += P([R('Quick answers', 12, True, color=PURPLE_T)], 0, 80)
    w = 1663
    out += (f'<w:tbl>{TBL_PR.format(jc="<w:jc w:val=" + chr(34) + "center" + chr(34) + "/>")}<w:tblGrid>'
            + f'<w:gridCol w:w="{w}"/>' * 6 + '</w:tblGrid>')
    for r in range(5):
        out += '<w:tr>'
        for c in range(6):
            n = c * 5 + r + 1
            out += kcell(w, P([R(f'{n}  ', 10.5, color='595959'), R(qs[n - 1]['_letter'], 11.5, True, color=PURPLE_T)], align='center'),
                         'FFF8E1' if n > 25 else None, (40, 60))
        out += '</w:tr>'
    out += '</w:tbl>'
    out += P([R('Solutions', 12, True, color=PURPLE_T)], 200, 80)
    widths = [624, 2041, 1644, 5669]
    out += (f'<w:tbl>{TBL_PR.format(jc="<w:jc w:val=" + chr(34) + "center" + chr(34) + "/>")}<w:tblGrid>'
            + ''.join(f'<w:gridCol w:w="{x}"/>' for x in widths) + '</w:tblGrid>')
    out += '<w:tr><w:trPr><w:tblHeader w:val="true"/></w:trPr>' + ''.join(
        kcell(x, P([R(t, 10.5, True, color=WHITE)]), PURPLE_T, (50, 70), PURPLE_T)
        for x, t in zip(widths, ['Q', 'Part · level', 'Answer', 'Why?'])) + '</w:tr>'
    for n, q in enumerate(qs, 1):
        if q['ch'] in STARS:
            pl = 'Section II · ' + ' + '.join(CH_NAME[c] for c in q['ch'].split('+')) + ' · Hard'
        else:
            k = [p[0] for p in PARTS].index(q['ch']) + 1
            pl = f'Part {k} · {CH_NAME[q["ch"]]} · Hard'
        why = P([R('Hint: ', 10, True, True, '595959'), R(q['hint'], 10, False, True, '595959')], 0, 30, line=252)
        why += P([R(q['sol'], 10)], 0, 0, line=252)
        out += ('<w:tr><w:trPr><w:cantSplit/></w:trPr>' + kcell(widths[0], P([R(n, 10.5, True)]))
                + kcell(widths[1], P([R(pl, 9.5)])) + kcell(widths[2], P([R(f'({q["_letter"]}) ', 10.5, True, color=PURPLE_T), R(q['_opts']['ABCD'.index(q['_letter'])], 10)]))
                + kcell(widths[3], why) + '</w:tr>')
    return out + '</w:tbl>'


INFO_ROWS = [
    ('Total Questions', '30 multiple-choice questions'),
    ('Level', 'Level-2 (final round): every question is Hard'),
    ('Time', '45 minutes'),
    ('Section I', '25 questions, each from one chapter'),
    ('Section II', '5 Star Questions, each joining two chapters'),
    ('Negative Marking', 'No negative marking'),
    ('Calculator', 'Not allowed'),
    ('Chapters', 'Number System · Operations · Geometry · Applied Mathematics · Mathematical Reasoning'),
]
HELLO = [
    'Every question has four answer choices: (A), (B), (C) and (D). Only one is correct.',
    'Read each question and look at its picture carefully. Then mark your answer on the answer sheet at the end.',
    'This is a Level-2 paper. Every question needs careful thinking, so take your time and check each step.',
    'Section I has 25 questions. Section II has 5 Star Questions.',
    'There is no negative marking, so try every question.',
    'Do not use a calculator. You may do rough work on a separate sheet.',
    'All figures are not necessarily drawn to scale unless stated.',
]
NOTES = [
    'Pictures are part of the questions. Every picture also works when printed in black and white.',
    'You may read a question aloud to the child, exactly as printed. Please do not explain it or point to an answer choice.',
    'Parts follow the AMO syllabus chapters. Chapters 3, 4, 6, 7 and 8 are not part of the Class {cls} syllabus, so the chapter numbers shown in the Part headings have gaps.',
    'The answer sheet and the answer key are at the end. Remove only the answer key before the child begins.',
]


def paper_page(n, cls, logo_rid, pid):
    run, para, table, box, spacer = bc.run, bc.para, bc.table, bc.box, bc.spacer
    out = para([bc.image_run(logo_rid, 64.4, 69.8, pid, f'logo{n}')], 'center', after=80)
    out += para([run('ARYABHATTA MATHS OLYMPIAD', 18, True, color=bc.NAVY)], 'center', after=20)
    out += para([run('Level 2', 10, color=bc.GREY_T)], 'center', after=200)
    out += para([run(f'PRACTICE PAPER-{n}', 13.5, True, color=bc.RED)], 'center', after=40)
    out += para([run(f'CLASS {cls}', 26, True, color=bc.NAVY)], 'center', after=200)
    trs = [[para([run(a, 11, True)]), para([run(b, 11)])] for a, b in INFO_ROWS]
    out += table(trs, [3150, bc.TEXT_W - 3150], bc.GRID, fills=[bc.LABEL_FILL, None], mar=(95, 100))
    out += spacer(16)
    hello = [para([run('\U0001F44B ', 13), run('Hello, friend! How to do this paper:', 13, True, color=bc.NAVY)], after=100)]
    hello += [para([run('⭐ ', 12), run(b, 12)], after=70) for b in HELLO]
    out += box(hello, bc.YEL_FILL, bc.YEL_LINE)
    out += spacer(14)
    par = [para([run('For parents and teachers', 8.5, True, color=bc.NAVY)], after=50)]
    par += [para([run('•  ', 8), run(t.format(cls=cls), 8)], after=30) for t in NOTES]
    out += box(par, bc.GRY_FILL, bc.GRY_LINE)
    return out


def front_cover(set_no, first, last, cover_rid, cover_size, sect):
    run, para, table, spacer = bc.run, bc.para, bc.table, bc.spacer
    w = bc.COVER_W
    h = w * cover_size[1] / cover_size[0]
    out = para([bc.image_run(cover_rid, w, h, 9002, 'cover')], 'center', after=160)
    out += para([run(f'Set {set_no}  ·  Practice Papers {first}–{last}  ·  with answer keys & detailed solutions', 10, color='666666')], 'center', after=160)
    cells = [('Name:', '____________________'), ('Class & Section:', '________________'),
             ('Roll No.:', '________________'), ('School:', '____________________'),
             ('City:', '____________________'), ('Date:', '____________________')]
    rows = [[para([run(a + ' ', 10.5, True), run(b, 10.5)]) for a, b in cells[i:i + 2]] for i in (0, 2, 4)]
    out += table(rows, [bc.TEXT_W // 2, bc.TEXT_W - bc.TEXT_W // 2], '999999', sz=6)
    out += spacer(18)
    out += para([run('Published by Unlock IQ Institute Pvt. Ltd.', 9.5, True, color=bc.DARK)], 'center', after=20)
    out += para([run('Register for Olympiads:  www.aryabhattamathsolympiad.com/student-registration', 8.5, color='666666')], 'center', sect=sect)
    return out


def assign_letters(qs, seed):
    """Place each correct answer so the paper uses A-D evenly (8/8/7/7) with no letter three times in a row."""
    rng = random.Random(seed)
    fixed = {i: 'ABCD'[q['ans']] for i, q in enumerate(qs) if q.get('fixed')}
    for _ in range(5000):
        pool = list('AABBCCDD' * 4)[:30]
        counts = {L: 0 for L in 'ABCD'}
        target = dict(zip('ABCD', rng.sample([8, 8, 7, 7], 4)))
        for L in fixed.values():
            counts[L] += 1
        free = [i for i in range(30) if i not in fixed]
        bag = []
        for L in 'ABCD':
            bag += [L] * max(0, target[L] - counts[L])
        if len(bag) != len(free):
            continue
        rng.shuffle(bag)
        seq = [None] * 30
        for i, L in fixed.items():
            seq[i] = L
        for i, L in zip(free, bag):
            seq[i] = L
        if all(not (seq[i] == seq[i + 1] == seq[i + 2]) for i in range(28)):
            return seq
    raise RuntimeError('could not balance answer letters')


def place_options(q, letter):
    if q.get('fixed'):
        return list(q['opts'])
    correct, wrong = q['opts'][0], list(q['opts'][1:])
    i = 'ABCD'.index(letter)
    return wrong[:i] + [correct] + wrong[i:]


def load_paper(qdir, pno):
    path = os.path.join(qdir, f'paper{pno:02d}.py')
    ns = {k: getattr(F, k) for k in dir(F) if not k.startswith('_')}
    exec(compile(open(path, encoding='utf8').read(), path, 'exec'), ns)
    return ns['QUESTIONS']


def main(cls, set_no, first, last, qdir, out_path):
    cls, set_no, first, last = int(cls), int(set_no), int(first), int(last)
    use_class(cls)
    papers = {p: load_paper(qdir, p) for p in range(first, last + 1)}
    for p, qs in papers.items():
        checks.check_paper(p, qs, PARTS, STARS)
    with zipfile.ZipFile(TEMPLATE) as z:
        base = {i.filename: z.read(i.filename) for i in z.infolist()}
    new_rels, parts = [], {}

    def add_part(name, data, kind):
        rid = f'rIdM{len(new_rels) + 1}'
        new_rels.append(f'<Relationship Id="{rid}" Type="{bc.REL}{kind}" Target="{name}"/>')
        parts[f'word/{name}'] = data
        return rid

    cover = os.path.join(ROOT, f'assets/AMO_Class{cls}_L2_cover.png')
    im = Image.open(cover).convert('RGB')
    buf = io.BytesIO(); im.save(buf, 'JPEG', quality=92)
    cover_rid = add_part('media/cover.jpeg', buf.getvalue(), 'image')
    buf = io.BytesIO(); Image.open(LOGO).convert('RGB').save(buf, 'PNG')
    logo_rid = add_part('media/logo.png', buf.getvalue(), 'image')

    x0 = base['word/document.xml'].decode()
    sect0 = re.findall(r'<w:sectPr>.*?</w:sectPr>', x0, re.S)[-1]
    setup = ''.join(re.findall(r'<w:pgSz[^>]*/>|<w:pgMar[^>]*/>|<w:cols[^>]*/>|<w:docGrid[^>]*/>', sect0))
    cover_sect = f'<w:sectPr>{setup.replace("<w:titlePg/>", "")}</w:sectPr>'
    root = re.match(r'.*?<w:ftr [^>]*>', base['word/footer1.xml'].decode(), re.S).group(0)
    footer_rid = add_part('footer1.xml', bc.footer_xml(root).encode(), 'footer')
    parts['word/_rels/footer1.xml.rels'] = (
        '<?xml version="1.0" encoding="UTF-8" standalone="yes"?>'
        '<Relationships xmlns="http://schemas.openxmlformats.org/package/2006/relationships">'
        f'<Relationship Id="rIdLogo" Type="{bc.REL}image" Target="media/logo.png"/></Relationships>').encode()
    hdr_root = re.match(r'.*?<w:hdr [^>]*>', base['word/header1.xml'].decode(), re.S).group(0)

    body = front_cover(set_no, first, last, cover_rid, im.size, cover_sect)
    pid = 100
    tmpdir = os.path.join(os.path.dirname(os.path.abspath(out_path)), '_fig_tmp')
    os.makedirs(tmpdir, exist_ok=True)
    for p in range(first, last + 1):
        qs = papers[p]
        letters = assign_letters(qs, 1000 * cls + p)
        for q, L in zip(qs, letters):
            q['_letter'] = L
            q['_opts'] = place_options(q, L)
            if q.get('fixed'):
                q['_letter'] = 'ABCD'[q['ans']]
        content = ''
        k = 0
        for ch, title, cnt in PARTS:
            if ch == '1':
                content += band('SECTION I', '25 questions · every question is Hard', AMBER, '1F1F1F')
            content += part_band(title)
            for _ in range(cnt):
                content += qblock(p, k, qs[k], add_part, tmpdir, star=False)
                k += 1
        content += band('SECTION II — Star Questions', '5 questions · each joins two chapters', AMBER, '1F1F1F')
        for _ in STARS:
            content += qblock(p, k, qs[k], add_part, tmpdir, star=True)
            k += 1
        content += answer_sheet(cls, p) + answer_key(cls, p, qs)

        def renum(m):
            nonlocal pid
            pid += 1
            return f'<wp:docPr id="{pid}"'
        content = re.sub(r'<wp:docPr id="\d+"', renum, content)
        header_rid = add_part(f'header{p}.xml', bc.header_xml(hdr_root, p).encode(), 'header')
        sect = (f'<w:sectPr><w:headerReference w:type="default" r:id="{header_rid}"/>'
                f'<w:footerReference w:type="default" r:id="{footer_rid}"/>'
                f'<w:footerReference w:type="first" r:id="{footer_rid}"/>'
                f'<w:type w:val="nextPage"/>{setup.replace("<w:docGrid", "<w:titlePg/><w:docGrid") if "<w:titlePg/>" not in setup else setup}</w:sectPr>')
        opening = paper_page(p, cls, logo_rid, 9100 + p)
        opening += ('<w:p><w:pPr><w:pageBreakBefore/><w:spacing w:before="0" w:after="0"/></w:pPr>'
                    '<w:r><w:rPr><w:sz w:val="4"/></w:rPr><w:t xml:space="preserve"> </w:t></w:r></w:p>')
        body += opening + content
        body += bc.spacer(1, sect) if p < last else sect

    doc = x0[:x0.index('<w:body>')] + '<w:body>' + body + '</w:body></w:document>'
    rels = base['word/_rels/document.xml.rels'].decode()
    rels = re.sub(r'<Relationship [^>]*relationships/(image|header|footer)"[^>]*/>', '', rels)
    rels = rels.replace('</Relationships>', ''.join(new_rels) + '</Relationships>')
    ct = base['[Content_Types].xml'].decode()
    ct = re.sub(r'<Override PartName="/word/(header|footer)\d*\.xml"[^>]*/>', '', ct)
    hf = 'application/vnd.openxmlformats-officedocument.wordprocessingml.'
    ct = ct.replace('</Types>', ''.join(
        f'<Override PartName="/{q}" ContentType="{hf}{"header" if "header" in q else "footer"}+xml"/>'
        for q in parts if re.match(r'word/(header|footer)\d+\.xml$', q)) + '</Types>')
    for ext, mime in (('jpeg', 'image/jpeg'), ('png', 'image/png')):
        if f'Extension="{ext}"' not in ct:
            ct = ct.replace('</Types>', f'<Default Extension="{ext}" ContentType="{mime}"/></Types>')
    with zipfile.ZipFile(out_path, 'w', zipfile.ZIP_DEFLATED) as o:
        for name, data in base.items():
            if name.startswith('word/media/') or re.match(r'word/(header|footer)\d*\.xml$', name) or name.startswith('word/_rels/header') or name.startswith('word/_rels/footer'):
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
    print(f'{out_path}: papers {first}-{last}, {sum(1 for q in parts if "/media/" in q)} images')


def qblock(p, k, q, add_part, tmpdir, star):
    img = ''
    if q.get('fig'):
        path = os.path.join(tmpdir, f'p{p:02d}_q{k + 1:02d}.png')
        w, h = F.render(q['fig'], path, max_w=q.get('fig_w', 430))
        scale = q.get('fig_scale', 1.0)
        rid = add_part(f'media/p{p:02d}_q{k + 1:02d}.png', open(path, 'rb').read(), 'image')
        img = bc.image_run(rid, w * scale, h * scale, 1, f'fig p{p} q{k + 1}')
    return question_block(k + 1, q, img, star)


if __name__ == '__main__':
    main(*sys.argv[1:7])
