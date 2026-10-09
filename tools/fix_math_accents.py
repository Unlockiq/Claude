"""Make Word equation accents render correctly in LibreOffice PDFs.

Usage: python3 fix_math_accents.py IN.docx OUT.docx

In equation objects, an accent written with U+203E (overline) shows in
LibreOffice as an acute-like stroke, so the conjugate z-bar prints as "ź".
This replaces that accent character with U+0305 (combining overline), the
bar accent Word itself uses, which prints correctly in Word and LibreOffice.
"""
import sys, zipfile

OLD = '<m:chr m:val="‾"/>'
NEW = '<m:chr m:val="̅"/>'


def main(src, dst):
    with zipfile.ZipFile(src) as z:
        items = [(it, z.read(it.filename)) for it in z.infolist()]
    n = 0
    with zipfile.ZipFile(dst, 'w', zipfile.ZIP_DEFLATED) as o:
        for it, data in items:
            if it.filename == 'word/document.xml':
                x = data.decode('utf-8')
                n = x.count(OLD)
                data = x.replace(OLD, NEW).encode('utf-8')
            o.writestr(it, data)
    print(f'{src}: {n} accent(s) changed')


if __name__ == '__main__':
    main(*sys.argv[1:3])
