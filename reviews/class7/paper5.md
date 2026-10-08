# Review — AMO Level 1, Class 7, Practice Paper 5

**Verdict:** Strong paper. All 45 keys and worked solutions check out. Every question has exactly one correct option. The blueprint is met (chapter counts, 24 Easy + 16 Medium, Section II pairings). The must-fix items are small: the Q15 stem is false for an L-shape (one corner is reflex), the Q44 figure has no right-angle marks, and the Q18 answer cell shows only a letter.

**Key distribution:** A 11 · B 11 · C 11 · D 12 (A: 4, 5, 10, 12, 18, 21, 25, 30, 33, 39, 44; B: 2, 13, 17, 19, 20, 24, 29, 32, 36, 42, 43; C: 1, 6, 9, 11, 15, 23, 27, 31, 34, 40, 45; D: 3, 7, 8, 14, 16, 22, 26, 28, 35, 37, 38, 41).

## Errors (must fix)
| Q | Problem | Fix |
|---|---|---|
| 15 | The stem says "All its corners are right angles", but the L-shaped playground has a reflex (270°) inside corner. The figure marks only the 5 convex corners with squares, so the inside corner is unmarked. | Reword: "Its sides meet at right angles, and the length of each side is marked." (in the JSON file). Figure: add a right-angle square at the inside corner, drawn on the outside (unshaded) side. |
| 44 | ABCD is called a rectangle, and the solution relies on ∠ABE = 90° and ∠DAB = 90°. The figure shows no right-angle squares, which breaks the visual rule (right angles are always shown, never inferred). | Redraw: add right-angle squares at A (between AB and AD) and at B (between BA and BC). |
| 18 | The answer-key cell shows only "(A)", with no option text. | Add "AB = PQ, BC = QR, ∠A = ∠P" (addrun in the JSON file). |

## Language & clarity
| Q | Current wording | Issue | Suggested rewrite |
|---|---|---|---|
| 15 | "The figure shows the plan of a playground. All its corners are right angles, and the length of each side is marked. What is the perimeter of the playground?" | Factually wrong for the L-shape (see Errors). | "The figure shows the plan of a playground. Its sides meet at right angles, and the length of each side is marked. What is the perimeter of the playground?" |
| 23 | "… How many times as long as an edge of the small cube is an edge of the large cube?" | Inverted, hard-to-parse question. | "The total surface area of a small cube is 54 cm². The total surface area of a large cube is 864 cm². The edge of the large cube is how many times the edge of the small cube?" |
| 45 | "x is a negative rational number. When (3x − 1/2) is multiplied by itself, …" | The question opens with a bare lowercase variable. In the runs, "x" is a separate italic run after the bold "Q45." run, so this needs a manual edit, not a JSON fix. | "The number x is negative and rational. When (3x − 1/2) is multiplied by itself, the result is 49/16. What is the value of x?" |
| Solutions 5, 7, 9, 19, 23, 27, 33, 36 | e.g. "2 kg = 2,000 g. 300 ÷ 2,000 × 100 = 15%." | These solution sentences start with a numeral (house rule). | Add a short lead word ("There are…", "Here…", "Write…", "Then…"). The full text of each is in the JSON file. |

Everything else meets the house rules. Sentences are well under 50 words, there are no idioms, and no other sentence starts with a numeral. ₹ amounts are sensible and units are metric. Options are parallel within each question.

## Figures
| Q | Issue | Fix |
|---|---|---|
| 15 | The inside (reflex) corner has no right-angle mark. | Add a square at the inside corner (see Errors). |
| 44 | There are no right-angle squares at A and B. | Add squares at A and B. The rest of the figure checks out: AB : AD = 42 : 84 is drawn about 1 : 2, BE ≈ 11.3 cm matches ∠EAB = 15°, and ED = 84 cm with ∠DEC = 30° is geometrically consistent. |
| 20 | Optional: line m is drawn with a clear tilt while l and n look parallel. A student can guess the answer from the picture. | Optional: reduce m's visible tilt. The 80° vs 72° difference is real, but a smaller visual tilt would keep the question about angles. The arcs and angle values are consistent (72° above-right at l, 100° above-left at m, 108° below-right at n). |

Other figures checked and correct:
- **Q2:** the number line has equal fifths, every tick is labelled except the four lettered option points, and A = −8/5, B = −7/5, C = −3/5, D = 7/5.
- **Q21:** the bisector marks are single at B and double at C, and I and x are labelled.
- **Q24:** a closed drum, with the radius and height labelled.
- **Q26:** the face areas 20/15/12 are placed so that front = 5 × 4, top = 5 × 3 and side = 3 × 4, which fits the drawn proportions.
- **Q30:** the bar graph has a title, both axes are labelled, the y-axis starts at 0 with steps of 5, and every value sits on a gridline (40, 25, 55, 30, 50).
- **Q36:** the tile counts are 5, 8, 11.
- **Q42:** the table header is bold and has the unit (₹).

## Syllabus / level / difficulty
- Chapter counts match the blueprint: Ch1 4, Ch2 3, Ch3 5, Ch4 5, Ch5 5, Ch6 5, Ch8 3, Ch9 5, Ch10 5.
- Section I labels: 24 Easy + 16 Medium, which is correct. Section II pairings match the brief: Q41 Ch4+Ch10, Q42 Ch3+Ch10, Q43 Ch4+Ch9, Q44 Ch5+Ch6, Q45 Ch1+Ch4.
- All topics are Class 7 or earlier.
  - Q18 uses congruence criteria SSS/SAS/ASA, which is correctly introduced at C7.
  - Q24 and Q44 use the cylinder intro.
  - Q35 uses direct variation.
  - Q28–Q30 use mean and median.
- The computational ceiling is respected. Denominators are ≤ 50, exponents ≤ 5, P&L percentages are integers, and equation coefficients are ≤ 20. The largest computation is Q44 (22 × 63 × 84), which is acceptable in Section II.
- There is no pure aptitude reasoning. Q37–Q40 are number patterns or casework.
- Optional difficulty swap: Q20 (Easy) needs a linear pair at two lines plus corresponding angles, so it is closer to Medium. Q7 (Medium) is close to one step. If relabelling, swap Q20 → Medium and Q7 → Easy, which keeps 24/16. Q36 (Easy) is borderline but acceptable.
- Distractors are strong overall and mostly common mistakes. Some examples:
  - Q11: ₹836 = 760 × 1.1 and ₹950 = the cost price.
  - Q24: 8,052 = total surface area and 5,280 = curved surface area.
  - Q26: 94 = surface area, 47 = sum, 3,600 = product.
  - Q28: 48 and 44 are the means.
  - Q30: 3 counts Monday, which equals the mean.
  - Q34: 9 : 10 forgets to subtract.
  - Q45: 3/4 with its sign flipped, and −5/4 not divided by 3.
  - A few are weaker but still plausible (Q16 Floor 14/17, Q35 22).

## Questions with no issues
1, 2, 3, 4, 5\*, 6, 8, 9\*, 10, 11, 12, 13, 14, 16, 17, 19\*, 21, 22, 24, 25, 26, 27\*, 28, 29, 30, 31, 32, 33\*, 34, 35, 36\*, 37, 38, 39, 40, 41, 42, 43
(\* = stem fine; solution wording only)

## Topic list
- Q1 — Ch1 Rationals — standard form of 21/−56, p + q
- Q2 — Ch1 Number line for rationals — locate −7/5
- Q3 — Ch1 Operations/comparison of rationals — add to −2/3, result in (0, 1/4)
- Q4 — Ch1 Operations on rationals — telescoping product (1/k − 1)
- Q5 — Ch2 Laws of exponents — digits of 2⁴ × 5⁴ × 7
- Q6 — Ch2 Powers of −1 — sum of (−1)¹ … (−1)⁹
- Q7 — Ch2 Laws of exponents — multiplier from 2³ × 3² to 6⁴
- Q8 — Ch3 Profit & loss — profit % given SP and profit
- Q9 — Ch3 Percentage — 300 g of 2 kg
- Q10 — Ch3 Percentage of percentage — quarter of 40%
- Q11 — Ch3 Profit & loss — SP for 10% profit from 20% loss
- Q12 — Ch3 Successive % change — price +20%, rides −10%
- Q13 — Ch4 Linear equation — 7 − 3y = 2y + 22
- Q14 — Ch4 Simplification — removing brackets, sign error
- Q15 — Ch4 Expressions — perimeter of L-shape in x
- Q16 — Ch4 Linear equation (word) — lift floors
- Q17 — Ch4 Linear equation with fractions — 2/3 n − 2/5 n = 12
- Q18 — Ch5 Congruence criteria — spot SSA
- Q19 — Ch5 Quadrilateral angle sum — three equal angles
- Q20 — Ch5 Parallel lines & transversal — which pair is parallel
- Q21 — Ch5 Triangle angle sum + bisectors — ∠BIC
- Q22 — Ch5 Triangle angle sum — ∠P = ∠Q + ∠R, ∠Q = 2∠R
- Q23 — Ch6 Surface area of cube — edge ratio from TSAs
- Q24 — Ch6 Cylinder — area of two circular ends
- Q25 — Ch6 Volume — cuboid equal to 6 cm cube
- Q26 — Ch6 Volume of cuboid — from three face areas
- Q27 — Ch6 Volume & capacity — rain on roof to litres
- Q28 — Ch8 Mean — correction of one value
- Q29 — Ch8 Median — even count, find x
- Q30 — Ch8 Bar graph + mean — days above mean
- Q31 — Ch9 Inverse variation — speed and time
- Q32 — Ch9 Ratio comparison — greatest ratio
- Q33 — Ch9 Ratio — possible total for 5 : 4 : 2
- Q34 — Ch9 Ratio sharing — after a transfer
- Q35 — Ch9 Direct variation — change of 8 gives change of 12
- Q36 — Ch10 Number patterns — tile figures, 3n + 2
- Q37 — Ch10 Casework / number puzzle — two-digit multiple of 7
- Q38 — Ch10 Number theory casework — 30 as sum of two primes
- Q39 — Ch10 Casework — staircase 1/2-step ways (6 steps)
- Q40 — Ch10 Number patterns — n(n + 1) divisible by 3, first 20
- Q41 — Section II Ch4 + Ch10 — consecutive multiples of 6 summing to repdigit
- Q42 — Section II Ch3 + Ch10 — profit/loss subsets break even
- Q43 — Section II Ch4 + Ch9 — mixture replacement, milk : water
- Q44 — Section II Ch5 + Ch6 — isosceles triangle gives height, cylinder volume
- Q45 — Section II Ch1 + Ch4 — (3x − 1/2)² = 49/16, negative root
