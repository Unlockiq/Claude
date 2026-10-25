# AMO practice-paper reviews

Reviews of the AMO Level 1 practice papers against the AMO Vertical Syllabus v5.9.

- `reviews/README.md`: overall summary for Classes 1–11.
- `reviews/classN/README.md`: summary for each class. The `paperN.md` files have question-by-question notes.
- `reviews/syllabus_visual_rules.md`: number-line and colour checks (Visual Standards rules 9 and 12c).
- `fixes/classN/*.json`: the text fixes applied to each paper. `cover.json` is applied to every paper.
- `tools/apply_fixes.py`: makes the v3 DOCX from v2 (`python3 tools/apply_fixes.py SRC OUT CLASS fixes/classN`). PDFs are rebuilt with `soffice --headless --convert-to pdf`.
- `papers/classN_vX/`: the corrected DOCX and PDF files, with a zip of each class (Classes 1–2 and 5–10 v2→v3; Classes 3–4 v3→v4; Class 11 v1→v2). PDFs need the LibreOffice Math module (`libreoffice-math`), otherwise the equations (fractions) disappear.
- `tools/blueprint_check.py`: checks the chapter counts, the Easy/Medium mix and the Section II pairs against the syllabus workbook.
- `tools/build_combined.py`: combines a class's 5 papers into one booklet in the REAL olympiad format: a front cover with the class cover image, a REAL-style opening page for each paper, the header "Aryabhatta Maths Olympiad (AMO) Level-1 Practice Papers" with "Practice Paper n" on the right, and the brand footer with logo and page numbers. Booklets for Classes 1–11 are in `papers/combined/`. Usage: `python3 tools/build_combined.py CLASS papers/classN_vX vX assets/AMO_ClassN_cover.png assets/unlockiq_logo.png OUT.docx`, then convert with soffice.
- `tools/fix_math_accents.py`: fixes z̄ and raised ⁿ so they print correctly in LibreOffice PDFs.

## Level-2 (Class 1)

- `reviews/level2/class1/README.md`: review of the 10 original Level-2 Class 1 papers and how they were replaced. The question-by-question reviews of the originals are `originals_papers1-5.md` and `originals_papers6-10.md`, and `question_index.md` lists all 300 new questions with their answers.
- `questions/level2/class1/paperNN.py`: the 300 new questions (all Hard, Class 1 syllabus, unique scenarios, Indian names).
- `papers/level2/class1/`: the two booklets in the Level-1 consolidated format: Set-1 (Practice Papers 1–5) and Set-2 (Practice Papers 6–10), as DOCX and PDF.
- `tools/l2/build_l2.py` builds a booklet, `tools/l2/figures.py` draws the pictures, `tools/l2/checks.py` holds the house-rule checks and `tools/l2/index.py` writes the question index. `assets/AMO_Class1_L2_cover.png` is the Class 1 cover relabelled for Level-2.

## Level-2 (Class 2)

- `reviews/level2/class2/README.md`: review of the 10 original Level-2 Class 2 papers, how they were replaced and how the new ones were verified. `originals_papers1-5.md` and `originals_papers6-10.md` are the question-by-question reviews; `question_index.md` lists all 300 new questions with their answers.
- `questions/level2/class2/paperNN.py`: the 300 new questions.
- `papers/level2/class2/`: Set-1 (Practice Papers 1–5) and Set-2 (Practice Papers 6–10), as DOCX and PDF. The cover is `assets/AMO_Class2_L2_cover.png`.

## Level-2 (Class 3)

- `reviews/level2/class3/README.md`: review of the 10 original Level-2 Class 3 papers, how they were replaced and verified; `originals_papers1-5.md`, `originals_papers6-10.md` and `question_index.md` alongside.
- `questions/level2/class3/paperNN.py`: the 300 new questions.
- `papers/level2/class3/`: Set-1 (Practice Papers 1–5) and Set-2 (Practice Papers 6–10), DOCX and PDF. Cover: `assets/AMO_Class3_L2_cover.png`.

## Level-2 (Class 4)

- `reviews/level2/class4/README.md`: review of the 10 original Level-2 Class 4 papers, how they were replaced and verified; `originals_papers1-5.md`, `originals_papers6-10.md` and `question_index.md` alongside.
- `questions/level2/class4/paperNN.py`: the 300 new questions.
- `papers/level2/class4/`: Set-1 (Practice Papers 1–5) and Set-2 (Practice Papers 6–10), DOCX and PDF. Cover: `assets/AMO_Class4_L2_cover.png`.

## Level-2 (Class 5)

- `reviews/level2/class5/README.md`: review of the 10 original Level-2 Class 5 papers, how they were replaced and verified; `originals_papers1-5.md`, `originals_papers6-10.md` and `question_index.md` alongside.
- `questions/level2/class5/paperNN.py`: the 300 new questions.
- `papers/level2/class5/`: Set-1 (Practice Papers 1–5) and Set-2 (Practice Papers 6–10), DOCX and PDF. Cover: `assets/AMO_Class5_L2_cover.png`.

## Level-2 (Class 6)

- `reviews/level2/class6/README.md`: review of the 10 original Level-2 Class 6 papers, how they were replaced and verified; `originals_papers1-5.md`, `originals_papers6-10.md` and `question_index.md` alongside.
- `questions/level2/class6/paperNN.py`: the 300 new questions.
- `papers/level2/class6/`: Set-1 (Practice Papers 1–5) and Set-2 (Practice Papers 6–10), DOCX and PDF. Cover: `assets/AMO_Class6_L2_cover.png`.

## Level-2 (Class 10)

- `reviews/level2/class10/README.md`: review of the 10 original Level-2 Class 10 papers, how they were replaced and verified; `originals_papers1-5.md`, `originals_papers6-10.md` and `question_index.md` alongside.
- `questions/level2/class10/paperNN.py`: the 300 new questions.
- `papers/level2/class10/`: Set-1 (Practice Papers 1–5) and Set-2 (Practice Papers 6–10), DOCX and PDF. Cover: `assets/AMO_Class10_L2_cover.png`.

## Level-2 (Class 7)

- `reviews/level2/class7/README.md`: how the Class 7 papers were built and verified; `question_index.md` lists all 300 questions with answers, and `originals_papers1-5.md` / `originals_papers6-10.md` review the original papers.
- `questions/level2/class7/paperNN.py`: the 300 new questions.
- `papers/level2/class7/`: Set-1 (Practice Papers 1–5) and Set-2 (Practice Papers 6–10), DOCX and PDF. Cover: `assets/AMO_Class7_L2_cover.png`.

## Level-2 (Class 11)

- `reviews/level2/class11/README.md`: how the Class 11 papers were built and verified; `question_index.md` lists all 300 questions with answers.
- `questions/level2/class11/paperNN.py`: the 300 new questions.
- `papers/level2/class11/`: Set-1 (Practice Papers 1–5) and Set-2 (Practice Papers 6–10), DOCX and PDF. Cover: `assets/AMO_Class11_L2_cover.png`.

## Level-2 (Class 8)

- `reviews/level2/class8/README.md`: how the Class 8 papers were built and verified; `question_index.md` lists all 300 questions with answers, and `originals_papers1-5.md` / `originals_papers6-10.md` review the original papers.
- `questions/level2/class8/paperNN.py`: the 300 new questions.
- `papers/level2/class8/`: Set-1 (Practice Papers 1–5) and Set-2 (Practice Papers 6–10), DOCX and PDF. Cover: `assets/AMO_Class8_L2_cover.png`.

## Level-2 (Class 9)

- `reviews/level2/class9/README.md`: how the Class 9 papers were built and verified; `question_index.md` lists all 300 questions with answers, and `originals_papers1-5.md` / `originals_papers6-10.md` review the original papers.
- `questions/level2/class9/paperNN.py`: the 300 new questions.
- `papers/level2/class9/`: Set-1 (Practice Papers 1–5) and Set-2 (Practice Papers 6–10), DOCX and PDF. Cover: `assets/AMO_Class9_L2_cover.png`.

## Level-2: continuing in a new chat

- `docs/LEVEL2_HANDOFF.md`: workflow, house rules, file format, blueprints for Classes 5–11, verifier prompt and a starting prompt for a new chat.
- `reference/AMO_Vertical_Syllabus_v5.9.xlsx` and `reference/syllabus_by_class.md`: the syllabus and a readable topic list per class.
- `tools/l2/check_papers.py` (house-rule checks), `tools/l2/qedit.py` (fix helpers), `tools/l2/dewatermark.py` (clean original PDFs) and `tools/l2/make_cover.py` (Level-2 covers).
