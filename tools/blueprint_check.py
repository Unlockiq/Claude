"""Check an AMO paper's answer key labels against the syllabus blueprint.

Usage: python3 blueprint_check.py SYLLABUS.xlsx CLASS PAPER_TEXT...
PAPER_TEXT is `pdftotext -layout` output of a paper. Reports, per paper, the
Section I count per chapter and Easy/Medium/Hard, and the Section II
chapter pairs, each next to what the syllabus requires.
"""
import re, sys
import openpyxl


def blueprint(xlsx, cls):
    wb = openpyxl.load_workbook(xlsx, data_only=True)
    need = {}
    for r in wb['Distributions'].iter_rows(values_only=True):
        m = re.match(r'Ch(\d+):', str(r[0] or ''))
        if m and isinstance(r[cls], int):
            need[int(m.group(1))] = r[cls]
    pairs = {}
    for r in wb['Section II Pairings'].iter_rows(values_only=True):
        if r[0] == f'C{cls}':
            a = re.match(r'Ch(\d+)', str(r[3])).group(1)
            b = re.match(r'Ch(\d+)', str(r[4])).group(1)
            pairs[int(str(r[1])[1:])] = {int(a), int(b)}
    return need, pairs


def paper(text):
    sol = text[text.find('Solutions'):]
    sec1 = re.findall(r'^(\d+)\s+Part \d+ · Ch(\d+) · (Easy|Medium|Hard)', sol, re.M)
    sec2 = re.findall(r'^(4[1-5])\s+Section II · Ch(\d+) \+ Ch(\d+)', sol, re.M)
    return sec1, sec2


def main(xlsx, cls, *files):
    cls = int(cls)
    need, pairs = blueprint(xlsx, cls)
    for f in files:
        sec1, sec2 = paper(open(f).read())
        got = {}
        lv = {'Easy': 0, 'Medium': 0, 'Hard': 0}
        for q, ch, l in sec1:
            got[int(ch)] = got.get(int(ch), 0) + 1
            lv[l] += 1
        bad = []
        if len(sec1) != 40:
            bad.append(f'{len(sec1)} Section I rows found')
        for ch in sorted(set(need) | set(got)):
            if need.get(ch, 0) != got.get(ch, 0):
                bad.append(f'Ch{ch} {got.get(ch, 0)} (needs {need.get(ch, 0)})')
        if (lv['Easy'], lv['Medium'], lv['Hard']) != (24, 16, 0):
            bad.append(f"mix E{lv['Easy']}/M{lv['Medium']}/H{lv['Hard']} (needs 24/16/0)")
        for q, a, b in sec2:
            if {int(a), int(b)} != pairs.get(int(q)):
                bad.append(f'Q{q} Ch{a}+Ch{b} (needs ' + '+'.join(f'Ch{c}' for c in sorted(pairs.get(int(q), []))) + ')')
        if len(sec2) != 5:
            bad.append(f'{len(sec2)} Section II rows found')
        print(f'{f}: ' + ('OK' if not bad else '; '.join(bad)))


if __name__ == '__main__':
    main(*sys.argv[1:])
