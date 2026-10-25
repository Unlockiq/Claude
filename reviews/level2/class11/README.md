# AMO Level-2 · Class 11 · Practice Papers 1–10

The Class 11 Level-2 practice papers were written from scratch: 300 new questions in two booklets in the Level-1 consolidated format:

- `papers/level2/class11/AMO_Class-11_Level-2_Practice_Papers_Set-1.pdf` (Practice Papers 1–5) and `.docx`
- `papers/level2/class11/AMO_Class-11_Level-2_Practice_Papers_Set-2.pdf` (Practice Papers 6–10) and `.docx`

## Source

There were no original Level-2 papers for Class 11. All 300 questions were written from scratch to the **AMO Vertical Syllabus 2026-27 v5.9** for Class 11.

## How the papers are built

- **Blueprint (30 questions, all Hard).** Chapter Parts with 25 questions, from the Level-1 Class 11 weighting scaled to 25: Number System (complex numbers) 3, Algebra (sequences, series, binomial theorem, linear inequalities) 6, Coordinate Geometry (straight lines) 3, Trigonometry 3, Permutations, Combinations, Probability & Statistics 4, Applied Mathematics (finance) 3, Mathematical Reasoning 3. The last Part, "Mixed Problems", has 5 questions that each join two chapters (Ch4+Ch10, Ch4+Ch8, Ch1+Ch4, Ch5+Ch7, Ch8+Ch10). Level-2 papers have no sections.
- **Syllabus.** Complex numbers a + ib with integer parts (no polar form or De Moivre); AP, GP, AM–GM, Σn, Σn², Σn³, infinite GP; binomial theorem with index ≤ 10; linear inequalities; straight lines in all forms, point–line distance and angle between lines (no conics or 3-D); trigonometric functions of any angle, compound and multiple angles, sum–product formulas at standard reference values (no trig equations); permutations and combinations (factorial evaluations ≤ 10!), binomial probability, variance and standard deviation; GST, EMI, compound interest, SIP, break-even and effective rates; induction, pigeonhole, combinatorics and extremal arguments.
- **Unique scenarios, Indian names, ₹, sentences of at most 60 words**, checked by `tools/l2/checks.py`. `question_index.md` lists all 300 questions with answers.

## Verification

Two independent checkers solved all 300 questions from the printed pages before reading the keys; every key matched. Their findings were fixed: a trigonometric equation and a non-integer complex-number question replaced, a binomial sum cut to stay within 10!, a solution rewritten without circle (conic) language, wording made unambiguous, weak and equal-valued options replaced, and about 50 one-step questions upgraded. A third checker then re-solved all 59 changed questions; every key matched, and its last findings (an equal-valued option pair, two solution notes, one repeated and three near-repeated questions) were fixed.

## Rebuilding

```
python3 tools/l2/build_l2.py 4 1 1 5  questions/level2/class11 papers/level2/class11/AMO_Class-11_Level-2_Practice_Papers_Set-1.docx
python3 tools/l2/build_l2.py 4 2 6 10 questions/level2/class11 papers/level2/class11/AMO_Class-11_Level-2_Practice_Papers_Set-2.docx
cd papers/level2/class11 && soffice --headless --convert-to pdf *.docx
python3 tools/l2/index.py 4 questions/level2/class11 1 10 reviews/level2/class11/question_index.md
```
