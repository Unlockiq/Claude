# AMO Level-2 · Class 6 · Practice Papers 1–10

The 10 original Level-2 papers for Class 6 (30 questions each) were reviewed against their answer keys and the **AMO Vertical Syllabus 2026-27 v5.9 (locked)**. They have been replaced by 300 new questions in two booklets in the Level-1 consolidated format:

- `papers/level2/class6/AMO_Class-6_Level-2_Practice_Papers_Set-1.pdf` (Practice Papers 1–5) and `.docx`
- `papers/level2/class6/AMO_Class-6_Level-2_Practice_Papers_Set-2.pdf` (Practice Papers 6–10) and `.docx`

## Why the originals were replaced

Full reviews: `originals_papers1-5.md` and `originals_papers6-10.md`.

| Finding | Papers 1–5 | Papers 6–10 |
|---|---|---|
| Wrong key | The Paper 2 answer key belongs to a different paper (23 of 30 letters wrong); other keys correct | 0 |
| Broken questions | 3 (a mislabelled angle figure, an impossible triangle description, two equal options) | 0 |
| Questions outside the Class 6 syllabus | about 40% of each paper | 11–14 per paper |
| "Rs." instead of ₹ | in every paper | 21 questions |
| Hard questions | 8 of 150 | 10 of 150 |

The out-of-syllabus questions used profit and loss, discount, simple interest, mean/median/mode, circles and π, square roots and Heron's formula, parallel lines, algebraic identities, solving linear and simultaneous equations, AP formulas, quadratics and time-and-work. All papers shared one 30-slot template, so the same breaks repeated in the same slots.

## How the new papers are built

- **Blueprint (30 questions, all Hard).** Chapter Parts with 25 questions, from the Level-1 Class 6 weighting scaled to 25: Number System 3, Operations 3, Fractions, Decimals & Percentages 3, Algebra 2, Geometry 3, Mensuration 3, Data Handling 2, Applied Mathematics 3, Mathematical Reasoning 3. The last Part, "Mixed Problems", has 5 questions that each join two chapters, using the Class 6 pairings: Ch4+Ch10, Ch1+Ch10, Ch3+Ch9, Ch5+Ch6, Ch4+Ch9. Level-2 papers have no sections.
- **Syllabus.** Numbers to crores, prime factorisation, integers, HCF/LCM; BODMAS with up to three bracket levels; fraction–decimal–percentage conversions and percentage problems; algebra as variables, expressions and substitution (no multi-step equation solving); angle types, triangle classification and polygons; perimeter, area, volume and surface area of rectangles, cubes and cuboids; bar graphs and frequency tables; speed, distance, time and the unitary method; patterns, clock arithmetic, parity and working backwards. Multiplication up to 3-digit × 3-digit, division up to 5-digit ÷ 2-digit.
- **Unique scenarios, Indian names, ₹, sentences of at most 35 words**, checked by `tools/l2/checks.py`. `question_index.md` lists all 300 questions with answers.

## Verification

Two independent checkers solved all 300 questions from the printed pages before reading the keys; every key matched. Their other findings were fixed: three shop/discount questions recast as successive percentage changes (discount is Class 7), about ten solutions rewritten without multi-step equations, a joined-cubes surface question that allowed a second reading, a triangle-inequality question (replaced), two bar graphs redrawn so every bar ends on a gridline, small wording fixes, and 18 one-step questions upgraded.

## Rebuilding

```
python3 tools/l2/build_l2.py 4 1 1 5  questions/level2/class6 papers/level2/class6/AMO_Class-6_Level-2_Practice_Papers_Set-1.docx
python3 tools/l2/build_l2.py 4 2 6 10 questions/level2/class6 papers/level2/class6/AMO_Class-6_Level-2_Practice_Papers_Set-2.docx
cd papers/level2/class6 && soffice --headless --convert-to pdf *.docx
python3 tools/l2/index.py 4 questions/level2/class6 1 10 reviews/level2/class6/question_index.md
```
