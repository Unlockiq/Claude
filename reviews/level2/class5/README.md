# AMO Level-2 · Class 5 · Practice Papers 1–10

The 10 original Level-2 papers for Class 5 (30 questions each) were reviewed against their answer keys and the **AMO Vertical Syllabus 2026-27 v5.9 (locked)**. They have been replaced by 300 new questions in two booklets in the Level-1 consolidated format:

- `papers/level2/class5/AMO_Class-5_Level-2_Practice_Papers_Set-1.pdf` (Practice Papers 1–5) and `.docx`
- `papers/level2/class5/AMO_Class-5_Level-2_Practice_Papers_Set-2.pdf` (Practice Papers 6–10) and `.docx`

## Why the originals were replaced

Full reviews: `originals_papers1-5.md` and `originals_papers6-10.md`.

| Finding | Papers 1–5 | Papers 6–10 |
|---|---|---|
| Wrong key | 0 | 1 (P9 Q26: the figure shows 15 triangles, key says 13) |
| Questions outside the Class 5 syllabus | 36 | 41 |
| "Rs." instead of ₹ | 14 | 18 |
| Hard questions | 9 of 150 | 10 of 150 |

The out-of-syllabus questions used ratio and inverse proportion, simple and compound interest, profit and loss, negative numbers, algebra with letters, squares and Pythagoras, a pie chart and trapezium, rhombus and parallelogram areas. All papers shared one 30-slot template, so the same breaks repeated in the same slots.

## How the new papers are built

- **Blueprint (30 questions, all Hard).** The Level-1 Class 5 weighting scaled to 25 Section I questions: Number System 3, Operations 3, Fractions, Decimals & Percentages 4, Geometry 3, Mensuration 3, Data Handling 1, Applied Mathematics 4, Mathematical Reasoning 4. Section II has 5 Star Questions in the Class 5 pairings: Ch1+Ch10, Ch3+Ch10, Ch6+Ch10, Ch1+Ch9, Ch3+Ch9.
- **Syllabus.** Numbers to 9,99,999; factors, multiples, primes, HCF and LCM within 100; Roman numerals to M; BODMAS up to two bracket levels; fraction–decimal conversion and percentages through simple fractions; decimals to two places; fraction denominators up to 20; basic angles, triangle and quadrilateral types, line and rotational symmetry, tessellation and directions; area of right triangles and rectangles, volume of cubes and cuboids; pictographs and simple bar graphs; speed, distance, time and average speed; number series, calendar arithmetic and parity. Multiplication up to 3-digit × 2-digit and division up to 4-digit ÷ 2-digit.
- **Unique scenarios, Indian names, ₹, sentences of at most 35 words**, checked by `tools/l2/checks.py`. `question_index.md` lists all 300 questions with answers.

## Verification

Two independent checkers solved all 300 questions from the printed pages before reading the keys; every key matched. Their other findings were fixed: four HCF/LCM questions whose values went above 100, a clock-hand angle question (replaced with angles at a point), a series question whose stem allowed three options, a cube-root step, decimal products with three places, leap-year facts now stated in the stems, an HCF question whose answer equalled the HCF, two give-away options, a repeated "ring together" scenario in one paper, and about eight one-step questions upgraded.

## Rebuilding

```
python3 tools/l2/build_l2.py 4 1 1 5  questions/level2/class5 papers/level2/class5/AMO_Class-5_Level-2_Practice_Papers_Set-1.docx
python3 tools/l2/build_l2.py 4 2 6 10 questions/level2/class5 papers/level2/class5/AMO_Class-5_Level-2_Practice_Papers_Set-2.docx
cd papers/level2/class5 && soffice --headless --convert-to pdf *.docx
python3 tools/l2/index.py 4 questions/level2/class5 1 10 reviews/level2/class5/question_index.md
```
