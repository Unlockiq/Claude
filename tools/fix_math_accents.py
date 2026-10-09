"""Make symbols render correctly in LibreOffice-built PDFs.

Usage: python3 fix_math_accents.py IN.docx OUT.docx

1. Equation accents written with U+203E (overline) show in LibreOffice as an
   acute-like stroke, so the conjugate z-bar prints as "ź". They are changed
   to U+0305 (combining overline), the bar accent Word itself uses, which
   prints correctly in Word and LibreOffice.
2. The character "ⁿ" (U+207F) is missing from the paper's body font, so it
   prints as a quote mark. Each group of superscript characters containing it
   (e.g. "ⁿ⁻¹") is replaced by normal characters ("n−1") in Word superscript,
   italic, keeping the run's other formatting.
"""
import re, sys, zipfile

OLD_ACC = '<m:chr m:val="‾"/>'
NEW_ACC = '<m:chr m:val="̅"/>'
SUP_N = 'ⁿ'
SUPS = {'\u207f': 'n', '\u1d4f': 'k', '\u207a': '+', '\u207b': '\u2212', '\u2070': '0',
        '\u00b9': '1', '\u00b2': '2', '\u00b3': '3', '\u2074': '4', '\u2075': '5',
        '\u2076': '6', '\u2077': '7', '\u2078': '8', '\u2079': '9'}
GROUP = re.compile('[' + ''.join(SUPS) + ']*' + SUP_N + '[' + ''.join(SUPS) + ']*')
RUN = re.compile(r'<w:r>(<w:rPr>(.*?)</w:rPr>)?<w:t( xml:space="preserve")?>([^<]*)</w:t></w:r>')


def sup_rpr(props):
    props = re.sub(r'<w:i w:val="0"/>|<w:i/>|<w:vertAlign [^>]*/>', '', props)
    return '<w:rPr>' + props + '<w:i/><w:vertAlign w:val="superscript"/></w:rPr>'


def split_run(m):
    text = m.group(4)
    if SUP_N not in text:
        return m.group(0)
    props = m.group(2) or ''
    out, pos = [], 0
    for g in GROUP.finditer(text):
        if g.start() > pos:
            out.append('<w:r><w:rPr>' + props + '</w:rPr><w:t xml:space="preserve">' + text[pos:g.start()] + '</w:t></w:r>')
        sup = ''.join(SUPS[c] for c in g.group(0))
        out.append('<w:r>' + sup_rpr(props) + '<w:t>' + sup + '</w:t></w:r>')
        pos = g.end()
    if pos < len(text):
        out.append('<w:r><w:rPr>' + props + '</w:rPr><w:t xml:space="preserve">' + text[pos:] + '</w:t></w:r>')
    return ''.join(out)


def main(src, dst):
    with zipfile.ZipFile(src) as z:
        items = [(it, z.read(it.filename)) for it in z.infolist()]
    with zipfile.ZipFile(dst, 'w', zipfile.ZIP_DEFLATED) as o:
        for it, data in items:
            if it.filename == 'word/document.xml':
                x = data.decode('utf-8')
                acc, sup = x.count(OLD_ACC), x.count(SUP_N)
                x = RUN.sub(split_run, x.replace(OLD_ACC, NEW_ACC))
                assert SUP_N not in x, 'a superscript n was not in a plain text run'
                data = x.encode('utf-8')
                print(f'{src}: {acc} accent(s), {sup} superscript n changed')
            o.writestr(it, data)


if __name__ == '__main__':
    main(*sys.argv[1:3])
