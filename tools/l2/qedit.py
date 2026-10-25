"""Small helpers for fixing question files after review.

    from qedit import rep, replq
    rep('questions/level2/class3/paper04.py', [(old_text, new_text), ...])   # each old_text must occur exactly once
    replq('questions/level2/class3/paper04.py', 'scen prefix', '''    dict(ch='6', scen='...', ...),''')   # replace a whole question
"""


def rep(f, pairs):
    s = open(f, encoding='utf8').read()
    for old, new in pairs:
        assert s.count(old) == 1, (f, old[:80], s.count(old))
        s = s.replace(old, new)
    open(f, 'w', encoding='utf8').write(s)


def replq(f, scen, block):
    """Replace the whole dict(...) whose scen starts with `scen` by `block` (text without trailing newline)."""
    lines = open(f, encoding='utf8').read().split('\n')
    i = [k for k, l in enumerate(lines) if l.lstrip().startswith('dict(') and f"scen='{scen}" in l]
    assert len(i) == 1, (f, scen, i)
    i = i[0]
    j = i + 1
    while not (lines[j].lstrip().startswith('dict(') or lines[j].lstrip().startswith('#') or lines[j].strip() == ']'):
        j += 1
    while lines[j - 1].strip() == '':
        j -= 1
    lines[i:j] = block.rstrip('\n').split('\n')
    open(f, 'w', encoding='utf8').write('\n'.join(lines))
