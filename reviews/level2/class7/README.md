# AMO Level-2 · Class 7 · Practice Papers 1–10

The 10 original Level-2 papers for Class 7 (30 questions each) were reviewed against their answer keys and the **AMO Vertical Syllabus 2026-27 v5.9 (locked)**. They have been replaced by 300 new questions in two booklets in the Level-1 consolidated format:

- `papers/level2/class7/AMO_Class-7_Level-2_Practice_Papers_Set-1.pdf` (Practice Papers 1–5) and `.docx`
- `papers/level2/class7/AMO_Class-7_Level-2_Practice_Papers_Set-2.pdf` (Practice Papers 6–10) and `.docx`

## Why the originals were replaced

Full reviews: `originals_papers1-5.md` and `originals_papers6-10.md`.

| Finding | Papers 1–5 | Papers 6–10 |
|---|---|---|
| Wrong keys | 0 | 0 |
| Broken questions | 4 (two equal options; a clock that is not drawn; photo-frame labels that contradict the text) | 5 (two equal options; impossible HCF/LCM data; an impossible triangle; two frame figures that contradict the key) |
| Hard questions | 6 of 150 | 4 of 150 |
| "Rs." instead of ₹ | everywhere | 72 times |

All ten papers shared one 30-slot template with exact and near duplicates. The fixed slots broke the Class 7 syllabus in every paper: simple and compound interest, circle areas, square/cube roots, algebraic identities, quadratics and simultaneous equations. Lines and angles, congruence, data handling and cryptarithms never appeared.

## How the new papers are built

- **Blueprint (30 questions, all Hard).** Chapter Parts with 25 questions, from the Level-1 Class 7 weighting scaled to 25: Number System 3, Exponents 2, Percentages 3, Algebra 3, Geometry 3, Mensuration 3, Data Handling 2, Applied Mathematics 3, Mathematical Reasoning 3. The last Part, "Mixed Problems", has 5 questions that each join two chapters (Ch4+Ch10, Ch3+Ch10, Ch4+Ch9, Ch5+Ch6, Ch1+Ch4). Level-2 papers have no sections.
- **Syllabus.** Rational numbers; positive-integer exponents with bases ≤ 10 and exponents ≤ 5 (no zero or negative exponents); percentages, basic profit and loss, discount; expressions and linear equations in one variable; parallel lines and transversals, triangle and quadrilateral properties, congruence; surface area and volume of cubes, cuboids and cylinders; bar graphs, pie charts, mean/median/mode; ratio, unitary method, direct and inverse variation; cryptarithms, casework, number patterns.
- **Unique scenarios, Indian names, ₹, sentences of at most 50 words**, checked by `tools/l2/checks.py`. `question_index.md` lists all 300 questions with answers.

## Verification

Two independent checkers solved all 300 questions from the printed pages before reading the keys; every key matched. Their findings were fixed: exponent questions rewritten to the Class 7 limits, a prism question and an inequality question replaced, a 90° angle figure redrawn, wording slips, about ten repeated question types replaced, and about 35 one-step questions upgraded. A third checker then re-solved all 66 changed questions; every key matched, and its last wording and repeat findings were fixed.

## Rebuilding

```
python3 tools/l2/build_l2.py 4 1 1 5  questions/level2/class7 papers/level2/class7/AMO_Class-7_Level-2_Practice_Papers_Set-1.docx
python3 tools/l2/build_l2.py 4 2 6 10 questions/level2/class7 papers/level2/class7/AMO_Class-7_Level-2_Practice_Papers_Set-2.docx
cd papers/level2/class7 && soffice --headless --convert-to pdf *.docx
python3 tools/l2/index.py 4 questions/level2/class7 1 10 reviews/level2/class7/question_index.md
```
