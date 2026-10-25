# AMO Level-2 · Class 8 · Practice Papers 1–10

The 10 original Level-2 papers for Class 8 (30 questions each) were reviewed against their answer keys and the **AMO Vertical Syllabus 2026-27 v5.9 (locked)**. They have been replaced by 300 new questions in two booklets in the Level-1 consolidated format:

- `papers/level2/class8/AMO_Class-8_Level-2_Practice_Papers_Set-1.pdf` (Practice Papers 1–5) and `.docx`
- `papers/level2/class8/AMO_Class-8_Level-2_Practice_Papers_Set-2.pdf` (Practice Papers 6–10) and `.docx`

## Why the originals were replaced

Full reviews: `originals_papers1-5.md` and `originals_papers6-10.md`.

| Finding | Papers 1–5 | Papers 6–10 |
|---|---|---|
| Wrong key (no correct option) | 1 (P1 Q23) | 0 |
| More than one correct option | 4 | 0 |
| Figure missing or mismatched | 2 | 0 |
| Hard questions | 2 of 150 | 5 of 150 |
| "Rs." instead of ₹ | every paper | 34 questions |

All ten papers shared one 30-slot template with exact and near duplicates. The fixed slots used compound interest, simultaneous equations, cube identities, quadratics and polygon–circle radii, while Pythagoras, similarity, statistics, cryptarithms, fractals and nets never appeared. Two names were not Indian ("John", "Mr. X").

## How the new papers are built

- **Blueprint (30 questions, all Hard).** Chapter Parts with 25 questions, from the Level-1 Class 8 weighting scaled to 25: Number System 2, Exponents 2, Percentages & Interest 3, Algebra 3, Geometry 3, Mensuration 3, Data Handling 2, Applied Mathematics 3, Mathematical Reasoning 4. The last Part, "Mixed Problems", has 5 questions that each join two chapters (Ch4+Ch10, Ch5+Ch10, Ch4+Ch5, Ch3+Ch9, Ch6+Ch9). Level-2 papers have no sections.
- **Syllabus.** Squares and square roots (perfect squares ≤ 400 or √2, √3, √5), cubes and cube roots; integer, zero and negative exponents, standard form; successive discounts, simple interest, successive percentages; identities (a ± b)², a² − b² and factorisation, linear-equation word problems; similarity, special quadrilaterals, congruence, Pythagoras, nets, views and Euler's formula; cylinders and cones; histograms, frequency polygons, line graphs and pie charts; profit, loss and commercial problems; cryptarithms, casework, parity and fractals.
- **Unique scenarios, Indian names, ₹, sentences of at most 50 words**, checked by `tools/l2/checks.py`. `question_index.md` lists all 300 questions with answers.

## Verification

Two independent checkers solved all 300 questions from the printed pages before reading the keys; every key matched. Their findings were fixed: a kite question made unambiguous ("convex kite"), four solution notes corrected, axis titles and value labels added to every graph, a cramped Koch-curve figure spaced out, quadratic and line-equation steps replaced by identity and trial methods, two repeated fractal questions replaced, and about 40 one-step questions upgraded. A third checker then re-solved all 63 changed questions; every key matched, and the near-repeats it found were replaced.

## Rebuilding

```
python3 tools/l2/build_l2.py 4 1 1 5  questions/level2/class8 papers/level2/class8/AMO_Class-8_Level-2_Practice_Papers_Set-1.docx
python3 tools/l2/build_l2.py 4 2 6 10 questions/level2/class8 papers/level2/class8/AMO_Class-8_Level-2_Practice_Papers_Set-2.docx
cd papers/level2/class8 && soffice --headless --convert-to pdf *.docx
python3 tools/l2/index.py 4 questions/level2/class8 1 10 reviews/level2/class8/question_index.md
```
