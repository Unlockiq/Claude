# AMO Level-2 practice papers — handoff for a new chat

Use this file to continue the Level-2 work (Classes 5–11, or any class) in a new Claude Code chat.

## 1. Where things are

- **Repository:** `Unlockiq/Claude`. **Branch:** `claude/exciting-hypatia-b3jk1w`. All work is on this branch; it has not been merged.
- **Done:** Classes 1–5. Each has 300 new questions, two booklets (Set-1 = Papers 1–5, Set-2 = Papers 6–10, as PDF and DOCX), reviews of the original papers, a question index and a README:
  - `questions/level2/classN/paper01.py … paper10.py`
  - `papers/level2/classN/AMO_Class-N_Level-2_Practice_Papers_Set-1|2.{pdf,docx}`
  - `reviews/level2/classN/` (`README.md`, `originals_papers1-5.md`, `originals_papers6-10.md`, `question_index.md`)
- **Ready for Classes 5–11 (not yet used for a booklet):** blueprints in `tools/l2/build_l2.py`, word caps in `tools/l2/checks.py`, and covers `assets/AMO_ClassN_L2_cover.png`. Look at each cover before first use: the new "2" was painted in a sans-serif font, and some senior covers use a serif font.
- **Syllabus:** `reference/AMO_Vertical_Syllabus_v5.9.xlsx` (the authority) and `reference/syllabus_by_class.md` (a readable topic list and computational ceiling per class).

## 2. The user's requirements (verbatim intent)

- Review the 10 original Level-2 "Extra Mock" papers per class (question paper + answer key PDFs) rigorously.
- Consolidate them into **two booklets per class in the same template as the Level-1 consolidated booklet**: Set-1 = Papers 1–5, Set-2 = Papers 6–10.
- "All questions are of difficulty level **hard** for all the classes and should **follow the attached syllabus**. If the 10 attached papers have any low quality question, replace it. **Each question has to be of unique scenario, Indian names only.**"
- Level-2 format: **30 questions, 45 minutes** (Level-1 is 45 questions, 60 minutes). Section I = 25 questions (one chapter each), Section II = 5 Star questions (two chapters each).
- The user wants the PDFs sent in the chat when a class is done.

In practice every class so far had wrong keys, broken questions, a single repeated template and many syllabus breaks, so all 300 questions were rewritten each time.

## 3. Workflow per class (what worked)

1. **Get the originals.** The user uploads 20 PDFs per class (QP + AK for Test01–10), sometimes as RAR files (`unrar`/`7z` to extract). Put each upload in its own new folder in the scratchpad.
2. **Remove the watermark** (grey diagonal site name) so the pages can be read: `python3 tools/l2/dewatermark.py IN.pdf OUT.pdf`.
3. **Review the originals** with two background agents (Papers 1–5 and 6–10). Each agent solves every question before reading the key and writes a markdown report: wrong keys, broken/ambiguous questions, syllabus violations, difficulty count, template reuse. Save the reports to `reviews/level2/classN/originals_papers1-5.md` and `…6-10.md` (strip scratch paths).
4. **Write the 10 papers** as `questions/level2/classN/paperNN.py`. One agent (a fork with full context, or yourself) should write all ten so scenarios stay unique. Format in section 5.
5. **Check:** `python3 tools/l2/check_papers.py N 1 10` until there are no errors and `dups []`. Warnings about sentence-start words are usually false alarms; add real names to `GIRLS`/`BOYS` and ordinary words to `STARTERS`/`NOT_NAMES` in `tools/l2/checks.py`.
6. **Build:**
   ```
   python3 tools/l2/build_l2.py N 1 1 5  questions/level2/classN OUT/AMO_Class-N_Level-2_Practice_Papers_Set-1.docx
   python3 tools/l2/build_l2.py N 2 6 10 questions/level2/classN OUT/AMO_Class-N_Level-2_Practice_Papers_Set-2.docx
   cd OUT && soffice --headless --convert-to pdf *.docx
   ```
7. **Look at every page** (`pdftoppm -r 60 -png`, montage, Read). Check clipped figures, overlapping labels, and that each paper's opening page fits on one page.
8. **Verify independently:** two background agents (Set-1, Set-2) solve every question from the PDF *before* reading the key and report mismatches, ambiguity, syllabus breaks and one-step questions. Prompt template in section 7.
9. **Fix** with `tools/l2/qedit.py` (`rep` for exact text swaps, `replq` to replace a whole question by its `scen` prefix), re-check and rebuild.
10. **Publish:** copy the four files to `papers/level2/classN/`, run `python3 tools/l2/index.py N questions/level2/classN 1 10 reviews/level2/classN/question_index.md`, write `reviews/level2/classN/README.md` (copy the Class 4 one and update the numbers), add a section to the root `README.md`, commit and push, and send the two PDFs to the user.

Commit and push often (a stop hook asks for it). Never put the model name in repo files.

## 4. House rules (enforced or checked)

- **Blueprint:** exact Part order and counts from `BLUEPRINT[N]` in `build_l2.py`; stars in the listed order (e.g. `'4+10'`).
- **Hard:** 3+ steps or one real insight. Wrong options are common-mistake answers. The checkers flag one-step questions; upgrade them (add a second condition, ask for a derived quantity, etc.).
- **Exactly one defensible answer.** Odd-one-out questions were the biggest source of trouble: test every option for parity, multiples, squares, digit sums and digit patterns. Prefer stems like "Three of these are in the same times table".
- **Syllabus caps:** numbers, multiplication/division sizes, fraction denominators, decimals and topics per `reference/syllabus_by_class.md`. This also applies to the *worked solution* and to *wrong options* (e.g. no 4-digit distractors in Class 2).
- **Unique scenario** (`scen`) and **unique stem** across all 10 papers.
- **Indian names only**, girls and boys roughly balanced; **₹** (never "Rs."); sentence word cap 25 (C1–3), 35 (C4–6), 50 (C7–10), 60 (C11).
- **Pictures** must work in black and white (no colour carrying meaning), labels ≥ 10 pt, and must not contradict the text. Count figure answers twice and write the breakdown in the solution.
- **Answer letters** are balanced automatically (7–8 per letter, no letter three times in a row). Write the correct option **first**; use `fixed=True, ans=i` only for label options like P/Q/R/S.

## 5. Question file format

```python
# AMO Level-2 · Class N · Practice Paper K


def my_picture():                       # optional helpers built from drawing() primitives
    return [('rect', 10, 10, 120, 80, 'yellow'), ('line', 10, 10, 130, 90), ('text', 70, 105, 'label', 11)]


QUESTIONS = [
    # ---------------- Part 1 · Number System
    dict(ch='1', scen='short unique scenario key',
         fig=drawing(140, 110, my_picture()),          # optional
         stem='Question text. Ask one clear thing?',
         opts=['correct', 'trap 1', 'trap 2', 'trap 3'],
         hint='One-line nudge (printed in the key).',
         sol='Full worked solution, within the class limits.'),
    ...
    # ---------------- Section II · Star Questions
    dict(ch='4+10', scen='…', stem='…', opts=[…], hint='…', sol='…'),
]
```

Picture helpers (all in `tools/l2/figures.py`, available by name in paper files): `cards`, `objects`, `numberline`, `blocks`, `shapes`, `drawing` (prims: `poly`, `polyline`, `rect`, `circle`, `line`, `text`, `dot`, `emoji`, `shape`, `qbox`), `grid`, `week`, `months`, `money`, `table`, `equations`, `sticks`, `clocks`, `stack`, `side`. Class 4 papers also show pictographs, nets, views and composite shapes built from `drawing` (see `questions/level2/class4/paper01.py`). Senior classes will probably need new helpers (coordinate grids, graphs, angle diagrams, triangles with marked angles); add them to `figures.py` or to the paper file.

## 6. Notes for Classes 6–11 (Class 5 is done)

- **Blueprints** (25 Section I questions = Level-1 weights × 25/40, largest remainder; Section II from the "Section II Pairings" tab):

  | Class | Section I (chapter: count) | Section II |
  |---|---|---|
  | 5 | 1:3, 2:3, 3:4, 5:3, 6:3, 8:1, 9:4, 10:4 | 1+10, 3+10, 6+10, 1+9, 3+9 |
  | 6 | 1:3, 2:3, 3:3, 4:2, 5:3, 6:3, 8:2, 9:3, 10:3 | 4+10, 1+10, 3+9, 5+6, 4+9 |
  | 7 | 1:3, 2:2, 3:3, 4:3, 5:3, 6:3, 8:2, 9:3, 10:3 | 4+10, 3+10, 4+9, 5+6, 1+4 |
  | 8 | 1:2, 2:2, 3:3, 4:3, 5:3, 6:3, 8:2, 9:3, 10:4 | 4+10, 5+10, 4+5, 3+9, 6+9 |
  | 9 | 1:2, 3:2, 4:4, 5:4, 6:3, 8:3, 9:3, 10:4 | 4+10, 5+6, 4+5, 8+10, 3+9 |
  | 10 | 1:2, 3:3, 4:4, 5:3, 6:3, 7:2, 8:2, 9:3, 10:3 | 4+10, 5+7, 4+5, 3+9, 6+10 |
  | 11 | 1:3, 4:6, 5:3, 7:3, 8:4, 9:3, 10:3 | 4+10, 4+8, 1+4, 5+7, 8+10 |

  The syllabus allows ±1 per chapter per year. Change `BLUEPRINT` if the user prefers another split.
- **Opening page text** (`HELLO`, `NOTES`, `INFO_ROWS` in `build_l2.py`) was written for young children ("Hello, friend!", reading the question aloud). For Class 6+ consider a more grown-up version.
- **Maths notation:** stems are plain text. Fractions are written `3/4`, mixed numbers `2 3/4`, powers can use Unicode superscripts (x², 10³), roots √. Keep expressions short.
- `checks.py` has an addition cap only up to Class 5 (`CAPS`); check senior ceilings by hand and in the verifier prompt.

## 7. Verifier prompt template (one per Set)

> You are an independent checker for a maths olympiad practice booklet for Indian Class N children. PDF: `<path>` (Practice Papers a–b, 30 questions each; each paper is followed by an answer sheet and an answer key with solutions).
> 1. Render pages to PNG (`pdftoppm -r 110 -png -f N -l M file out`) and read them; `pdftotext -layout` helps for text. For each paper, solve EVERY question yourself from the question pages BEFORE looking at that paper's key. Zoom into each figure and count carefully.
> 2. Compare with the key. Report every question where your answer differs; there is no correct option or more than one defensible option (check odd-one-out questions for other rules such as parity, multiples, digit sums); the figure contradicts the text or is unclear; the solution text has an error.
> 3. Flag Class N syllabus breaks: `<list the class caps and forbidden topics from reference/syllabus_by_class.md>`; non-Indian names; "Rs."; questions that are too easy (one obvious step).
> Write the report to `<scratch>/cN/verify_setK.md` and return a concise list of findings (paper, Q, issue, suggested fix). Edit no other files.

## 8. Starting prompt for the new chat

> Continue the AMO Level-2 practice-paper project in repo Unlockiq/Claude on branch `claude/exciting-hypatia-b3jk1w`. First read `docs/LEVEL2_HANDOFF.md` and follow it exactly. Classes 1–5 are done. Now do Class **N**: I am uploading its 10 question papers and 10 answer keys. Review the originals, then write 300 new Hard questions that follow the syllabus with unique scenarios and Indian names, build Set-1 (Papers 1–5) and Set-2 (Papers 6–10) in the same template, verify them independently, commit and push, and give me the two PDFs.
