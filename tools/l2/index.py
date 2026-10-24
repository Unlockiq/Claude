"""Write a markdown index of every Level-2 question: paper, Q, chapter, scenario, answer letter and answer.

Usage: python3 tools/l2/index.py CLASS QUESTIONS_DIR FIRST LAST OUT.md
Answer letters are placed exactly as build_l2.py places them."""
import os, sys
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
import build_l2 as b, checks

cls, qdir, first, last, out = int(sys.argv[1]), sys.argv[2], int(sys.argv[3]), int(sys.argv[4]), sys.argv[5]
papers = {p: b.load_paper(qdir, p) for p in range(first, last + 1)}
dup = checks.check_all(papers)
lines = [f'# AMO Level-2 · Class {cls} · question index (Papers {first}–{last})', '',
         'One row per question. Every scenario is used once across all papers'
         + (' (checked by `tools/l2/checks.py`).' if not dup else f' — DUPLICATES FOUND: {dup}'), '']
for p, qs in papers.items():
    letters = b.assign_letters(qs, 1000 * cls + p)
    counts = {L: 0 for L in 'ABCD'}
    lines += [f'## Practice Paper {p}', '', '| Q | Chapter | Scenario | Answer |', '|---|---|---|---|']
    for i, (q, L) in enumerate(zip(qs, letters), 1):
        if q.get('fixed'):
            L = 'ABCD'[q['ans']]
        opts = b.place_options(q, L)
        counts[L] += 1
        ch = ' + '.join(b.CH_NAME[c] for c in q['ch'].split('+'))
        lines.append(f'| {i} | {ch} | {q["scen"]} | ({L}) {opts["ABCD".index(L)]} |')
    lines += ['', 'Answer letters: ' + ', '.join(f'{L} {n}' for L, n in counts.items()), '']
open(out, 'w', encoding='utf8').write('\n'.join(lines))
print(out, 'written;', 'duplicates:', dup)
