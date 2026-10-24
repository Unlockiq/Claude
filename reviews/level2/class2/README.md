# AMO Level-2 · Class 2 · Practice Papers 1–10

The 10 original Level-2 "Extra Mock" papers for Class 2 (30 questions each) were reviewed against their answer keys and the **AMO Vertical Syllabus 2026-27 v5.9 (locked)**. They have been replaced by 300 new questions, published as two booklets in the Level-1 consolidated format:

- `papers/level2/class2/AMO_Class-2_Level-2_Practice_Papers_Set-1.pdf` (Practice Papers 1–5) and `.docx`
- `papers/level2/class2/AMO_Class-2_Level-2_Practice_Papers_Set-2.pdf` (Practice Papers 6–10) and `.docx`

## Why the originals were replaced

The full question-by-question reviews are in `originals_papers1-5.md` and `originals_papers6-10.md`.

| Finding | Papers 1–5 | Papers 6–10 |
|---|---|---|
| Wrong key letter | 6 | 4 |
| Question with no correct option | 2 | 1 |
| Question with two defensible answers | 2 | 2 |

All ten papers used the same 30-question template, so the same scenario appeared ten times. The template slots also broke the Class 2 syllabus: letter series and letter coding, fractions other than half and quarter, 4-digit numbers, division beyond halving and quartering, and "Rs." instead of ₹. Most questions were one-step.

## How the new papers are built

- **Blueprint (each paper, 30 questions, all Hard).** Section I has 25 questions: Number System 6, Operations 6, Geometry 5, Applied Mathematics 4, Mathematical Reasoning 4. Section II has 5 Star Questions in the syllabus's Class 2 pairings: Ch1+Ch10, Ch2+Ch10, Ch5+Ch10, Ch1+Ch9 and Ch5+Ch9.
- **Syllabus.** Numbers to 999 (hundreds, tens, ones; number line; even and odd); adding and subtracting with carrying, sums within 999; multiplication within 1-digit × 1-digit (repeated addition for anything larger); division only as halving and quartering; 2D shape properties and the 3D solids cube, sphere, cylinder and cone (faces, edges and vertices are not counted — that is Class 3); clock times at o'clock, half past, quarter past and quarter to, with AM and PM (no elapsed-time arithmetic); two-step money; patterns, analogies and simple counting.
- **Hard.** Every question needs three or more steps or one real insight. Wrong options are common-mistake answers.
- **Unique scenarios, Indian names, ₹, sentences of at most 25 words.** Checked by `tools/l2/checks.py`; `question_index.md` lists all 300 questions with their answers.
- **Pictures** are drawn by `tools/l2/figures.py` and work in black and white.
- **Answer letters** are spread 7–8 per letter in each paper, with no letter three times in a row.

## Verification

Two independent checkers solved all 300 questions from the printed pages before reading the keys. Every key matched. Their other findings were fixed before publishing: two odd-one-out questions that had a second defensible answer (a parity reading), a pattern stem that pointed to the wrong rule, a fold-and-cut question that needed "no square corner", option values above 999, a clock whose hands overlapped at quarter past 3 (the hour hand is now a thicker grey line), and about 15 questions upgraded from one step to two or more.

## Rebuilding

```
python3 tools/l2/build_l2.py 2 1 1 5  questions/level2/class2 papers/level2/class2/AMO_Class-2_Level-2_Practice_Papers_Set-1.docx
python3 tools/l2/build_l2.py 2 2 6 10 questions/level2/class2 papers/level2/class2/AMO_Class-2_Level-2_Practice_Papers_Set-2.docx
cd papers/level2/class2 && soffice --headless --convert-to pdf *.docx
python3 tools/l2/index.py 2 questions/level2/class2 1 10 reviews/level2/class2/question_index.md
```
