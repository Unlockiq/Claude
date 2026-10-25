"""Run the house-rule checks on a class's question files without building a booklet.

Usage: python3 tools/l2/check_papers.py CLASS FIRST LAST
Prints (errors, warnings) per paper, then any duplicate scenarios or stems across the papers."""
import os, sys
HERE = os.path.dirname(os.path.abspath(__file__))
sys.path[:0] = [HERE, os.path.dirname(HERE)]
import build_l2 as b, checks

cls, first, last = int(sys.argv[1]), int(sys.argv[2]), int(sys.argv[3])
b.use_class(cls)
root = os.path.dirname(os.path.dirname(HERE))
papers = {p: b.load_paper(os.path.join(root, f'questions/level2/class{cls}'), p) for p in range(first, last + 1)}
for p, qs in papers.items():
    print(p, checks.check_paper(p, qs, b.PARTS, b.STARS))
print('dups', checks.check_all(papers))
