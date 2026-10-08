# AMO Level 1 · Class 3 · Practice Paper 4: Review

**Verdict:** Strong paper. I solved all 45 questions myself. Every keyed answer is correct, each question has exactly one correct option, and every figure matches its stem. The only must-fix item is the blank answer cell for Q20 in the key. The other items are two stems that start with a numeral and some small fixes to the solutions.

**Key distribution:** A = 11 (Q4, 8, 15, 18, 19, 21, 26, 31, 35, 40, 41) · B = 12 (Q3, 6, 11, 12, 20, 24, 28, 30, 36, 39, 44, 45) · C = 11 (Q1, 7, 10, 13, 16, 23, 25, 29, 34, 37, 43) · D = 11 (Q2, 5, 9, 14, 17, 22, 27, 32, 33, 38, 42). The spread is well balanced.

## Errors (must fix)

| Q | Problem | Fix |
|---|---|---|
| Q20 (key) | The answer cell shows only "(B)". The option text is missing, but every other row has it. | Add "2 circles and 1 rectangle" as a separate plain run after "(B) " (see JSON, addrun). |

No wrong keys or wrong solutions. No question is out of syllabus or over the computational ceiling.

## Language & clarity

| Q | Current wording | Issue | Suggested rewrite (full text) |
|---|---|---|---|
| Q11 | A cook gets 7 crates of apples with 36 apples in each crate. 8 apples are bad and are thrown away. How many good apples are left? | A sentence starts with a numeral. | A cook gets 7 crates of apples with 36 apples in each crate. Then 8 bad apples are thrown away. How many good apples are left? |
| Q13 | 52 children come to a school assembly. Each bench seats 6 children. … | The stem starts with a numeral. | There are 52 children at a school assembly. Each bench seats 6 children. What is the smallest number of benches needed so that every child has a seat? |
| Q35 | … In A0, the first digit is A and the second digit is 0. | "first/second digit" is vague, and the final "0." wraps onto a line by itself. Place-value words are clearer for Class 3. | Find the digit A that makes A0 − A = 63 true. In A0, A is the tens digit and 0 is the ones digit. |
| Q4 (solution) | One more than 6,099: the 99 becomes 100, so the number is 6,100. | This is not a complete sentence because of the colon fragment. | One more than 6,099 is 6,100, because 99 + 1 = 100. |
| Q37 (solution) | The numbers 4, 7, 2 repeat. Steps 10, 11 and 12 start a new group: 4, 7, 2. … | Steps 10–12 do not "start" a group. They make up the 4th group. | The numbers 4, 7, 2 repeat in groups of 3. Steps 10, 11 and 12 make the fourth group: 4, 7, 2. So the 11th step has 7. |

Minor points that I did not put in the JSON:
- Q37 option (B) 3 is not in the pattern, so it is not a plausible distractor. A better choice is 11 (the step number) or 1 (the remainder when 11 is divided by 3, if the child mistakes the remainder for the number).
- Q18 "the second most water left" is understandable but slightly awkward. It is acceptable as written.

## Figures

| Q | Issue | Fix |
|---|---|---|
| Answer sheet | Rows 10–15 in the first column are shifted right compared with rows 1–9, because of the two-digit numbers. This is cosmetic only. | Optionally right-align the question numbers. |
| All question figures | Checked and OK. Q4: the counter shows 6,099. Q9: the box holds 12 shuttlecocks (2 × 6). Q14: 5 of the 12 cups have eggs. Q19: a regular hexagon. Q21: a cube. Q22: a cuboid frame with all 12 edges and 8 balls (hidden edges dashed). Q23: the dashed line is at the exact centre of a 6 × 4 grid; the left side has 6 shaded squares, the right side has 2 that already match (r1c6, r4c4), and 4 more are needed (r1c5, r2c5, r3c4, r4c6), so (C) is correct. Q25: 9 m, 13 m and 6 m make a valid triangle. Q27: 1 m × 35 cm with right-angle squares at all four corners. Q32: the minute hand is on 7 and the hour hand is just past halfway from 3 to 4, so the time is 3:35. Q34: 30, 26, 22, 18, ?. Q38: 5, 20, 7, 18, 9, 16, ?. Q39: A8 + 3A = 82 works with A = 4 in both columns, including the carry. Q44: the bill is ₹4,735. Q45: a valid cube net (a column of 4 with side squares on the 2nd) with a perimeter of 14 edges. | — |

## Syllabus / level / difficulty

- The blueprint is met exactly: Ch1 = 6 (Q1–6), Ch2 = 7 (Q7–13), Ch3 = 5 (Q14–18), Ch5 = 5 (Q19–23), Ch6 = 4 (Q24–27), Ch9 = 6 (Q28–33) and Ch10 = 7 (Q34–40). Section I has exactly 24 Easy and 16 Medium.
- The Section II pairings match the brief: Q41 Ch1+Ch10, Q42 Ch3+Ch10, Q43 Ch9+Ch10, Q44 Ch1+Ch9 and Q45 Ch5+Ch6. All five are genuinely multi-step.
- The computational ceiling is respected. The only remainders are with 2-digit dividends (Q10: 59 ÷ 8, Q13: 52 ÷ 6). The 3-digit divisions are exact (Q12: 156 ÷ 6, Q30: 270 ÷ 3). Multiplication stays within 2-digit × 1-digit (Q11: 7 × 36, Q9: 7 × 12, Q40: 15 × 4). Sums stay at most 10,000, fractions are like fractions with denominators up to 12, and Roman numerals stay at or below L (XLVIII = 48).
- Q42 uses "half of the milk left", which is fine as an everyday idea. The arithmetic stays in twelfths.
- Q35 (A0 − A = 63) is labelled Easy but needs some insight, so it is borderline Medium. If it is relabelled, swap it as a pair with Q38 (Medium → Easy) to keep 24/16. I do not consider the swap necessary.
- There is no pure aptitude reasoning. Q38 (two alternating sequences) is a number pattern, so it is fine.
- Cover: the template lines are present. "Fractions, Decimals & Percentages" is the chapter name, so it is acceptable even though Class 3 covers fractions only. The marks totals (80 + 20 = 100) are correct.

## Questions with no issues

Q1, Q2, Q3, Q5, Q6, Q7, Q8, Q9, Q10, Q12, Q14, Q15, Q16, Q17, Q18, Q19, Q21, Q22, Q23, Q24, Q25, Q26, Q27, Q28, Q29, Q30, Q31, Q32, Q33, Q34, Q36, Q38, Q39, Q40, Q41, Q42, Q43, Q44, Q45

## Topic list

- Q1 — Ch1 place value — 3 thousands + 4 hundreds + 6 → 3,406
- Q2 — Ch1 face value — face value of 9 in 2,940 → 9
- Q3 — Ch1 Roman numerals — 34 → XXXIV
- Q4 — Ch1 successor — 6,099 + 1 → 6,100
- Q5 — Ch1 Roman numerals — rearrange XVI → XIV = 14
- Q6 — Ch1 counting numbers in a range — 2,997 to 3,002 → 6
- Q7 — Ch2 4-digit addition — 1,250 + 1,375 → 2,625
- Q8 — Ch2 4-digit subtraction — 4,020 − 2,685 → 1,335
- Q9 — Ch2 multiplication from a picture — 7 × 12 → 84
- Q10 — Ch2 division with remainder — 59 ÷ 8 → r 3
- Q11 — Ch2 multiply then subtract — 7 × 36 − 8 → 244
- Q12 — Ch2 divide then subtract — 156 ÷ 6 − 4 → 22
- Q13 — Ch2 division, round up — 52 ÷ 6 → 9 benches
- Q14 — Ch3 fraction of a set — 5/12
- Q15 — Ch3 improper fraction — 5/4 m is more than 1 m
- Q16 — Ch3 add like fractions — 2/9 + 5/9 = 7/9
- Q17 — Ch3 compare like fractions — only 3/8 ≤ 5/8 → pudding
- Q18 — Ch3 order like fractions — fractions left, 2nd largest → P
- Q19 — Ch5 2D shapes — hexagon
- Q20 — Ch5 nets — cylinder net → 2 circles + 1 rectangle
- Q21 — Ch5 faces — cube has 6 faces
- Q22 — Ch5 edges/vertices — 12 − 8 → 4
- Q23 — Ch5 line symmetry — 4 more squares
- Q24 — Ch6 units of capacity — teaspoon in mL
- Q25 — Ch6 perimeter of a triangle — 28 m
- Q26 — Ch6 kg/g conversion — 1,250 − 800 → 450 g
- Q27 — Ch6 perimeter with m/cm conversion — 270 cm
- Q28 — Ch9 hours to minutes — 80 minutes
- Q29 — Ch9 calendar months — October + 5 → March
- Q30 — Ch9 money sharing — ₹270 ÷ 3 → ₹90
- Q31 — Ch9 calendar dates — 6 June + 14 days → 20 June
- Q32 — Ch9 elapsed time from a clock — 3:35 to 4:10 → 35 minutes
- Q33 — Ch9 multi-step money — buy 2 get 1 free, 6 books → ₹240
- Q34 — Ch10 number pattern — −4 each time → 14
- Q35 — Ch10 cryptarithm — A0 − A = 63 → A = 7
- Q36 — Ch10 working backwards — 35 + 12 → 47
- Q37 — Ch10 repeating pattern — 11th term of 4, 7, 2 → 7
- Q38 — Ch10 alternating patterns — next term → 11
- Q39 — Ch10 cryptarithm (addition) — A8 + 3A = 82 → A = 4
- Q40 — Ch10 working backwards — (9 + 6) × 4 → 60
- Q41 — Ch1 + Ch10 — Roman numerals, work backwards → XIX
- Q42 — Ch3 + Ch10 — fractions, work backwards → 2/12
- Q43 — Ch9 + Ch10 — elapsed time backwards → 10:25 AM
- Q44 — Ch1 + Ch9 — swapped digits in a bill, ₹4,735 − ₹4,375 → ₹360
- Q45 — Ch5 + Ch6 — perimeter of a cube net, 14 × 5 → 70 cm
