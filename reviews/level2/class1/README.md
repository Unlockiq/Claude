# AMO Level-2 · Class 1 · Practice Papers 1–10

The 10 original Level-2 "Extra Mock" papers (Test01–Test10, 30 questions each) were reviewed against their answer keys and the **AMO Vertical Syllabus 2026-27 v5.9 (locked)**. They have been replaced by 300 new questions, published as two booklets in the Level-1 consolidated format:

- `papers/level2/class1/AMO_Class-1_Level-2_Practice_Papers_Set-1.pdf` (Practice Papers 1–5) and `.docx`
- `papers/level2/class1/AMO_Class-1_Level-2_Practice_Papers_Set-2.pdf` (Practice Papers 6–10) and `.docx`

## Why the originals were replaced

The full question-by-question reviews are in `originals_papers1-5.md` and `originals_papers6-10.md`.

| Finding | Papers 1–5 | Papers 6–10 |
|---|---|---|
| Wrong key letter | 7 | 2 |
| Question with no correct option | 2 | 2 |
| Solution text that contradicts the picture | 11 | 9 |
| Hard questions (rubric: 3+ steps or real insight) | 6 of 150 | 0 of 150 |

Every paper used the same 30-question template, so the same scenario appeared 10 times. Each template slot also broke at least one syllabus rule in every paper:

- **Sums above 20.** The Class 1 ceiling is "within 20". Examples are 15 + 24, 53 + 6, and price totals of ₹24–₹30.
- **Ranking.** "Third from the front" is a REAL topic and is not allowed in AMO.
- **Letter counting.** Counting the letter R in a sentence is not mathematics.
- **Non-mathematical odd-one-out.** Examples are a cap versus a crown, and a dog versus a cat.
- **Colour carries the answer.** These questions fail when printed in black and white (Visual Standards rule 12c).
- **Size judged by eye.** Coiled ribbons and ball sizes are not measured.
- **Clock time.** This topic starts in Class 2.
- **Currency.** The papers wrote "Rs." instead of ₹.

## How the new papers are built

- **Blueprint (each paper, 30 questions, all Hard).**
  - Parts 1–5 hold 25 single-chapter questions:
    - Number System: 7
    - Operations: 6
    - Geometry: 4
    - Applied Mathematics: 4
    - Mathematical Reasoning: 4
  - The last Part, "Mixed Problems", has 5 questions that each join two chapters. They follow the syllabus's Class 1 Section II pairings in this order: Ch1+Ch10, Ch5+Ch10, Ch9+Ch10, Ch1+Ch9 and Ch2+Ch5.
- **Syllabus.** The questions stay within Class 1 content: numbers to 100, adding and subtracting within 20, and multiplication only as equal groups. Geometry covers circle, square, rectangle, triangle and visual symmetry. Applied questions use days, months and Indian coins and notes. Reasoning covers patterns, sequences and mathematical odd-one-out. Place-value counting in tens (such as 4 tens and 7 ones) is used for numbers above 20.
- **Hard.** Every question needs three or more steps or one real insight. Wrong options are common-mistake answers, for example counting "between" numbers inclusively, forgetting that 0 cannot lead, or doubling the wrong number.
- **Unique scenarios.** Every question has its own scenario key, and no stem repeats across the 10 papers. `question_index.md` lists all 300 with their answers.
- **Names and language.** Only Indian names are used, about evenly split between girls and boys, and money is written in ₹. No sentence is longer than 25 words, and every stem names its picture.
- **Pictures.** All pictures are redrawn as clean figures by `tools/l2/figures.py`. Every one works in black and white, every number-line tick is labelled, and labels are at least 10 pt.
- **Answer letters.** Letters are spread 7–8 per letter in each paper, with no letter three times in a row.
- **Template.** The layout matches the Level-1 Class 1 booklet:
  - the front cover, using the same art relabelled "Level-2 Practice Papers";
  - an opening page for each paper;
  - the header and brand footer;
  - Part bands;
  - an answer sheet for all 30 questions;
  - quick answers and a solutions table, where each "Why?" cell has a hint and a full solution.

## Rebuilding

```
python3 tools/l2/build_l2.py 1 1 1 5  questions/level2/class1 papers/level2/class1/AMO_Class-1_Level-2_Practice_Papers_Set-1.docx
python3 tools/l2/build_l2.py 1 2 6 10 questions/level2/class1 papers/level2/class1/AMO_Class-1_Level-2_Practice_Papers_Set-2.docx
cd papers/level2/class1 && soffice --headless --convert-to pdf *.docx
python3 tools/l2/index.py 1 questions/level2/class1 1 10 reviews/level2/class1/question_index.md
```

The questions live in `questions/level2/class1/paperNN.py`. Each question is a small record: chapter, scenario, stem, options (correct answer first), hint, solution and an optional picture. The builder refuses to run if a paper breaks the house rules in `tools/l2/checks.py`. Those rules cover the blueprint, four distinct options, the word cap, ₹ for currency, names from the Indian-names list, and scenarios and stems that are unique across the papers.
