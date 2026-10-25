# AMO Level-2 · Class 3 · Practice Papers 1–10

The 10 original Level-2 papers for Class 3 (30 questions each) were reviewed against their answer keys and the **AMO Vertical Syllabus 2026-27 v5.9 (locked)**. They have been replaced by 300 new questions in two booklets in the Level-1 consolidated format:

- `papers/level2/class3/AMO_Class-3_Level-2_Practice_Papers_Set-1.pdf` (Practice Papers 1–5) and `.docx`
- `papers/level2/class3/AMO_Class-3_Level-2_Practice_Papers_Set-2.pdf` (Practice Papers 6–10) and `.docx`

## Why the originals were replaced

Full reviews: `originals_papers1-5.md` and `originals_papers6-10.md`.

| Finding | Papers 1–5 | Papers 6–10 |
|---|---|---|
| Key letter wrong | 5 (3 of these have no correct option at all) | 0 |
| No correct option (key marks a wrong count) | — | 3 |
| Two correct options | 2 | 1 |
| Hard questions (rubric) | none | 3, all broken |

Every paper used one 30-question template. The slots broke the syllabus in every paper: "Rs." for ₹, letter counting and letter mirror images (not mathematics), unlike fractions, denominators above 12, decimals, and colour carrying the answer.

## How the new papers are built

- **Blueprint (30 questions, all Hard).** The Level-1 Class 3 weighting scaled to 25 single-chapter questions: Number System 4, Operations 4, Fractions 3, Geometry 3, Mensuration 3, Applied Mathematics 4, Mathematical Reasoning 4. The last Part, "Mixed Problems", has 5 questions that each join two chapters, using the Class 3 pairings: Ch1+Ch10, Ch3+Ch10, Ch9+Ch10, Ch1+Ch9, Ch5+Ch6.
- **Syllabus.** Numbers to 10,000, place and face value, Roman numerals to L; tables to 12, multiplication to 2-digit × 1-digit, division to 3-digit ÷ 1-digit with exact quotients (remainders only with 2-digit dividends); like fractions with denominators up to 12, no decimals; 2D/3D properties, faces, edges and vertices, line symmetry by folding, nets; metric units and perimeter (no area); elapsed time, calendar and money; patterns, simple cryptarithms and working backwards.
- **Unique scenarios, Indian names, ₹, sentences of at most 25 words**, checked by `tools/l2/checks.py`. `question_index.md` lists all 300 questions with answers.

## Verification

Two independent checkers solved all 300 questions from the printed pages before reading the keys; every key matched. Their other findings were fixed: wording that allowed a second reading (a symmetry cut, a calendar tense, a fold direction, a perimeter "inside and outside"), working that went past the Class 3 limits (4-digit × 1-digit, numbers above 10,000), a leap-year question (replaced), pyramid names in two questions (recast), a fold-and-cut question that now has a picture, and about 15 one-step questions upgraded.

## Rebuilding

```
python3 tools/l2/build_l2.py 3 1 1 5  questions/level2/class3 papers/level2/class3/AMO_Class-3_Level-2_Practice_Papers_Set-1.docx
python3 tools/l2/build_l2.py 3 2 6 10 questions/level2/class3 papers/level2/class3/AMO_Class-3_Level-2_Practice_Papers_Set-2.docx
cd papers/level2/class3 && soffice --headless --convert-to pdf *.docx
python3 tools/l2/index.py 3 questions/level2/class3 1 10 reviews/level2/class3/question_index.md
```
