# AMO Level-2 · Class 9 · Practice Papers 1–10

The 10 original Level-2 papers for Class 9 (30 questions each) were reviewed against their answer keys and the **AMO Vertical Syllabus 2026-27 v5.9 (locked)**. They have been replaced by 300 new questions in two booklets in the Level-1 consolidated format:

- `papers/level2/class9/AMO_Class-9_Level-2_Practice_Papers_Set-1.pdf` (Practice Papers 1–5) and `.docx`
- `papers/level2/class9/AMO_Class-9_Level-2_Practice_Papers_Set-2.pdf` (Practice Papers 6–10) and `.docx`

## Why the originals were replaced

Full reviews: `originals_papers1-5.md` and `originals_papers6-10.md`.

| Finding | Papers 1–5 | Papers 6–10 |
|---|---|---|
| Wrong key | 0 | 1 (P9 Q30: the key's own working gives 28π, option B, but the key marks C) |
| Two correct options | 2 | 0 (one equal-valued distractor pair) |
| Hard questions | 15 of 150 | 5 of 150 |
| Questions outside the Class 9 syllabus | 17 | 22 |
| "Rs." instead of ₹ | 16 | 15 |

All ten papers shared one 30-slot template with exact and near duplicates and skewed answer letters. The fixed slots used Class 10 topics (quadratics from roots, the discriminant, combined solids, rationalising surds, similar solids, tangents), while AP/GP, growth and decay, irrationality, Heron's and Brahmagupta's formulas, coordinate geometry, circle theorems, stacked bar graphs, tree diagrams, propositions, algorithms and recurrences never appeared.

## How the new papers are built

- **Blueprint (30 questions, all Hard).** Chapter Parts with 25 questions, from the Level-1 Class 9 weighting scaled to 25: Number System 2, Growth & Percentages 2, Algebra 4, Geometry 4, Mensuration 3, Statistics & Probability 3, Applied Mathematics 3, Mathematical Reasoning 4. The last Part, "Mixed Problems", has 5 questions that each join two chapters (Ch4+Ch10, Ch5+Ch6, Ch4+Ch5, Ch8+Ch10, Ch3+Ch9). Level-2 papers have no sections.
- **Syllabus.** The v5.9 Class 9 syllabus (NCERT Ganita Manjari): rationals and irrationality; linear vs compound growth, annual compound interest, weighted averages; polynomials, linear graphs, identities, pairs of linear equations, AP/GP terms and Σn; coordinate geometry, circle theorems, quadrilaterals, the midpoint theorem and congruence; Heron's and Brahmagupta's formulas, circles and solids; statistics, stacked bar graphs and probability; linear and sequence models; propositions, counterexamples, algorithms, recurrences and fractals. Class 10 topics (trigonometry, the quadratic formula, similarity, combined solids, grouped data) are excluded.
- **Unique scenarios, Indian names, ₹, sentences of at most 50 words**, checked by `tools/l2/checks.py`. `question_index.md` lists all 300 questions with answers.

## Verification

Two independent checkers solved all 300 questions from the printed pages before reading the keys; every key matched. Their findings were fixed: solution notes rewritten to name options by content, sine-rule and similarity steps replaced by construction and direct methods, an incircle question replaced, wording made unambiguous, repeated growth/percentage/coordinate question types replaced, and about 40 one-step questions upgraded. A third checker then re-solved all 70 changed questions; every key matched, and its repeat and wording findings were fixed.

## Rebuilding

```
python3 tools/l2/build_l2.py 4 1 1 5  questions/level2/class9 papers/level2/class9/AMO_Class-9_Level-2_Practice_Papers_Set-1.docx
python3 tools/l2/build_l2.py 4 2 6 10 questions/level2/class9 papers/level2/class9/AMO_Class-9_Level-2_Practice_Papers_Set-2.docx
cd papers/level2/class9 && soffice --headless --convert-to pdf *.docx
python3 tools/l2/index.py 4 questions/level2/class9 1 10 reviews/level2/class9/question_index.md
```
