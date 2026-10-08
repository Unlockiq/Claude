"""Apply reviewed text fixes to AMO practice-paper DOCX files.

Usage:
  python3 apply_fixes.py SRC_DIR OUT_DIR CLASS FIXES_DIR [IN_VER OUT_VER]

Reads  SRC_DIR/AMO_C{CLASS}_L1_PracticePaper{N}_{IN_VER}.docx  (N = 1..5;
       versions default to v2 -> v3)
       FIXES_DIR/cover.json   (fixes applied to every paper; optional)
       FIXES_DIR/paper{N}.json
Writes OUT_DIR/AMO_C{CLASS}_L1_PracticePaper{N}_{OUT_VER}.docx

A fix is {"old": ..., "new": ...} with optional keys:
  "after":  exact text of a run before the target; the first matching run
            after it is changed (use when "old" occurs more than once)
  "before": exact text of a run after the target; the nearest matching run
            before it is changed
  "mode": "addrun"  keep the "old" run (e.g. a bold "(B) " answer letter)
            and add "new" after it as a plain run, like the other answer cells
Every "old" must match one whole <w:t> run exactly, once (or be located by
"after"/"before"); otherwise the script stops and nothing is written.
Fixes that locate their target by "after"/"before" run first, so an anchor
can be changed by a later fix.
"""
import html, json, os, re, sys, zipfile

PLAIN = '<w:r><w:rPr><w:b w:val="0"/><w:i w:val="0"/><w:sz w:val="20"/></w:rPr><w:t>{}</w:t></w:r>'


def run_tail(text):
    return '>' + html.escape(text, quote=False) + '</w:t>'


def find_runs(x, text):
    return list(re.finditer(r'<w:t(?: [^>]*)?' + re.escape(run_tail(text)), x))


def locate(x, f, where):
    hits = find_runs(x, f['old'])
    if 'after' in f or 'before' in f:
        key = 'after' if 'after' in f else 'before'
        anchor = find_runs(x, f[key])
        assert len(anchor) == 1, (where, key, f[key], len(anchor))
        if key == 'after':
            hits = [m for m in hits if m.start() > anchor[0].end()][:1]
        else:
            hits = [m for m in hits if m.end() < anchor[0].start()][-1:]
    assert len(hits) == 1, (where, 'matches', len(hits), f['old'])
    return hits[0]


def apply(x, f, where):
    m = locate(x, f, where)
    if f.get('mode') == 'addrun':
        e = x.find('</w:r>', m.end()) + len('</w:r>')
        return x[:e] + PLAIN.format(html.escape(f['new'], quote=False)) + x[e:]
    seg = m.group(0).replace(run_tail(f['old']), run_tail(f['new']))
    return x[:m.start()] + seg + x[m.end():]


def main(src, out, cls, fixdir, in_ver='v2', out_ver='v3'):
    cover_path = os.path.join(fixdir, 'cover.json')
    cover = json.load(open(cover_path)) if os.path.exists(cover_path) else []
    os.makedirs(out, exist_ok=True)
    for p in range(1, 6):
        fixes = cover + json.load(open(os.path.join(fixdir, f'paper{p}.json')))
        fixes.sort(key=lambda f: not ('after' in f or 'before' in f))
        name = f'AMO_C{cls}_L1_PracticePaper{p}'
        with zipfile.ZipFile(os.path.join(src, name + f'_{in_ver}.docx')) as z:
            x = z.read('word/document.xml').decode('utf-8')
            for f in fixes:
                x = apply(x, f, f'paper {p} {f.get("q", "cover")}')
            with zipfile.ZipFile(os.path.join(out, name + f'_{out_ver}.docx'), 'w', zipfile.ZIP_DEFLATED) as o:
                for item in z.infolist():
                    data = x.encode('utf-8') if item.filename == 'word/document.xml' else z.read(item.filename)
                    o.writestr(item, data)
        print(f'Paper {p}: {len(fixes)} fixes -> {name}_{out_ver}.docx')


if __name__ == '__main__':
    main(*sys.argv[1:7])
