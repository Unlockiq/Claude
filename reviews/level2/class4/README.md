# AMO Level-2 · Class 4 · Practice Papers 1–10

The 10 original Level-2 papers for Class 4 (30 questions each) were reviewed against their answer keys and the **AMO Vertical Syllabus 2026-27 v5.9 (locked)**. They have been replaced by 300 new questions in two booklets in the Level-1 consolidated format:

- `papers/level2/class4/AMO_Class-4_Level-2_Practice_Papers_Set-1.pdf` (Practice Papers 1–5) and `.docx`
- `papers/level2/class4/AMO_Class-4_Level-2_Practice_Papers_Set-2.pdf` (Practice Papers 6–10) and `.docx`

## Why the originals were replaced

Full reviews: `originals_papers1-5.md` and `originals_papers6-10.md`.

| Finding | Papers 1–5 | Papers 6–10 |
|---|---|---|
| Wrong key (no option matches) | 1 | 0 |
| Two defensible answers or misleading figure | 4 | 1 (+2 minor figure issues) |
| Questions outside the Class 4 syllabus | about 43 | about 62 |
| Hard questions | 15 of 150 | 4 of 150 |

The out-of-syllabus questions used HCF/LCM and primes, percentages and simple interest, averages, ratio and speed, angle measures, circles and π, volume, triangle area, bar and pie charts, decimals with two places, numbers above 1,00,000 and Roman numerals beyond C. All papers shared one template, so the same breaks repeated in the same slots, and money was written "Rs.".

## How the new papers are built

- **Blueprint (30 questions, all Hard).** The Level-1 Class 4 weighting scaled to 25 single-chapter questions: Number System 3, Operations 3, Fractions & Decimals 4, Geometry 3, Mensuration 4, Data Handling 1, Applied Mathematics 3, Mathematical Reasoning 4. The last Part, "Mixed Problems", has 5 questions that each join two chapters, using the Class 4 pairings: Ch3+Ch10, Ch9+Ch10, Ch1+Ch10, Ch3+Ch9, Ch5+Ch6.
- **Syllabus.** Numbers to 1,00,000 and Roman numerals to C; four operations up to 2-digit × 2-digit or 3-digit × 1-digit and 4-digit ÷ 1-digit, properties and estimation; mixed, equivalent and unlike fractions (denominators to 12), decimals to one place (add and subtract only); lines and rays, prisms and pyramids, nets, F + V − E, reflection, tiling, grid positions and views; perimeter and area of rectangles and squares; pictographs with a stated key; time to the minute, day-of-week calendar logic and money; series, casework and calendar arithmetic.
- **Unique scenarios, Indian names, ₹, sentences of at most 35 words**, checked by `tools/l2/checks.py`. `question_index.md` lists all 300 questions with answers.

## Verification

Two independent checkers solved all 300 questions from the printed pages before reading the keys; every key matched. Their other findings were fixed: working beyond the Class 4 limits (250 × 250, 498 × 21, 1,800 ÷ 12, a 4-digit × 1-digit check and an option above 1,00,000), a fraction comparison that needed eighteenths, a clock-rate question (replaced), wording that allowed a second reading (a race with no number of runners, "every other chair", temperature written as "degrees"), a repeated series rule, and about ten one-step questions upgraded.

## Rebuilding

```
python3 tools/l2/build_l2.py 4 1 1 5  questions/level2/class4 papers/level2/class4/AMO_Class-4_Level-2_Practice_Papers_Set-1.docx
python3 tools/l2/build_l2.py 4 2 6 10 questions/level2/class4 papers/level2/class4/AMO_Class-4_Level-2_Practice_Papers_Set-2.docx
cd papers/level2/class4 && soffice --headless --convert-to pdf *.docx
python3 tools/l2/index.py 4 questions/level2/class4 1 10 reviews/level2/class4/question_index.md
```
