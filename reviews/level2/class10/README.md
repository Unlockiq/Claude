# AMO Level-2 · Class 10 · Practice Papers 1–10

The 10 original Level-2 papers for Class 10 (30 questions each) were reviewed against their answer keys and the **AMO Vertical Syllabus 2026-27 v5.9 (locked)**. They have been replaced by 300 new questions in two booklets in the Level-1 consolidated format:

- `papers/level2/class10/AMO_Class-10_Level-2_Practice_Papers_Set-1.pdf` (Practice Papers 1–5) and `.docx`
- `papers/level2/class10/AMO_Class-10_Level-2_Practice_Papers_Set-2.pdf` (Practice Papers 6–10) and `.docx`

## Why the originals were replaced

Full reviews: `originals_papers1-5.md` and `originals_papers6-10.md`.

| Finding | Papers 1–5 | Papers 6–10 |
|---|---|---|
| Broken questions | 3 (options in the wrong unit, no correct option, two equal options) | 4 (three with no correct option, one with two equal options) |
| Hard questions | 0 of 150 | 1 of 150 |
| "Rs." instead of ₹ | 19 times | 18 times |

The papers were CBSE board-level exercises, not Level-2 olympiad questions. All ten shared one 30-slot template with skewed answer letters (B was correct about half the time). Large parts of the Class 10 syllabus never appeared: compound interest, GST/EMI/SIP, partnership, grouped data and ogives, zeroes and coefficients, Euclid and irrationality, the Basic Proportionality Theorem, frustums, pigeonhole and invariants.

## How the new papers are built

- **Blueprint (30 questions, all Hard).** Chapter Parts with 25 questions, from the Level-1 Class 10 weighting scaled to 25: Number System 2, Fractions/Finance 3, Algebra 4, Geometry 3, Mensuration 3, Trigonometry 2, Statistics & Probability 2, Applied Mathematics 3, Mathematical Reasoning 3. The last Part, "Mixed Problems", has 5 questions that each join two chapters, using the Class 10 pairings: Ch4+Ch10, Ch5+Ch7, Ch4+Ch5, Ch3+Ch9, Ch6+Ch10. Level-2 papers have no sections.
- **Syllabus.** The v5.9 Class 10 syllabus (CBSE Grade-10 topics at olympiad difficulty): real numbers, compound interest and partnership, polynomials, linear systems, quadratics and APs, similar triangles, coordinate geometry and tangents, frustums, combined solids and circle areas, trigonometry at standard angles and heights and distances, grouped statistics and probability, GST/EMI/SIP and time-work, and pigeonhole, counting, extremal and invariant arguments. Class 11 topics (line equations, nCr, compound angles, calculus) are excluded.
- **Unique scenarios, Indian names, ₹, sentences of at most 50 words**, checked by `tools/l2/checks.py`. `question_index.md` lists all 300 questions with answers.

## Verification

Two independent checkers solved all 300 questions from the printed pages before reading the keys; every key matched. Their other findings were fixed: one solution sentence, seven figures (labels, angles drawn to match, a scale drawing), a cubic zero–coefficient question replaced by a quadratic one, a line-equation remark removed, counting solutions rewritten without nCr formulas, and 47 one-step questions upgraded to olympiad level. A third checker then re-solved every changed question; all keys matched, and its findings (a repeated identity question, two options with equal value, solution notes) were fixed.

## Rebuilding

```
python3 tools/l2/build_l2.py 4 1 1 5  questions/level2/class10 papers/level2/class10/AMO_Class-10_Level-2_Practice_Papers_Set-1.docx
python3 tools/l2/build_l2.py 4 2 6 10 questions/level2/class10 papers/level2/class10/AMO_Class-10_Level-2_Practice_Papers_Set-2.docx
cd papers/level2/class10 && soffice --headless --convert-to pdf *.docx
python3 tools/l2/index.py 4 questions/level2/class10 1 10 reviews/level2/class10/question_index.md
```
