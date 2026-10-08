# Review: AMO Level 1, Class 9, Practice Paper 1

## Verdict
This is a strong paper. All 45 keys are correct, and each question has exactly one correct option. I found no wrong answers, no broken questions and no topics outside the syllabus (no trigonometry). The blueprint is met exactly. What remains is small: two answer cells that show only a letter, one figure label that is cut off (Q42), one solution that uses a Class 10 theorem (Q2), and a few wording fixes.

**Key letter distribution:** A 11 · B 11 · C 11 · D 12. No letter appears more than twice in a row.

**Blueprint check:**
- Questions per chapter: Ch1 3 · Ch3 3 · Ch4 7 · Ch5 7 · Ch6 5 · Ch8 5 · Ch9 4 · Ch10 6 = 40 ✓
- Section I levels: 24 Easy + 16 Medium ✓
- Section II pairings: Q41 Ch4+Ch10, Q42 Ch5+Ch6, Q43 Ch4+Ch5, Q44 Ch8+Ch10, Q45 Ch3+Ch9 ✓

## Errors (must fix)
| Q | Problem | Fix |
|---|---|---|
| Q35 | In the solutions table, the Answer cell shows only "(B)". The answer text is missing. | Add "If two angles add up to 180°, then they form a linear pair." (addrun in the fixes JSON) |
| Q40 | In the solutions table, the Answer cell shows only "(D)". | Add "n² is a multiple of 3 but n is not a multiple of 3." (addrun) |
| Q42 | The "6 cm" label for AB sits outside the circle, next to the arc. Its "m" is cut off by the circle, and it does not clearly mark side AB. | Redraw the figure: put "6 cm" beside chord AB, inside the circle or clear of the arc (see Figures). |

## Language & clarity
| Q | Current wording | Issue | Suggested rewrite (full text) |
|---|---|---|---|
| Q3 | "Each outer side AB, BC, CD, … is 1 unit long and is at right angles to the line from O." | "The line from O" is vague: it does not say which line. | "The square-root spiral in the picture starts with OA = 1 unit. Each outer side AB, BC, CD, … is 1 unit long, with AB at right angles to OA, BC at right angles to OB, and so on. How many of the nine lengths OB, OC, OD, …, OJ are rational numbers?" |
| Q11 | "…three straight cuts, as shown by the dashed lines, each 10 cm from a corner along an edge…" | "A corner" lets each cut be measured from a different corner. Two of the blocks are cubes only if all three cuts are measured from the same corner. Also, a "straight cut" through a solid is really a flat (plane) cut. | "Swati has a wooden cube of edge 13 cm. She makes three flat cuts, as shown by the dashed lines, each 10 cm from the same corner along an edge, so the cube splits into 8 blocks. Two of the blocks are cubes. What is the total volume of the other six blocks?" |
| Q21 | "On a bicycle trip, Mei's wheel has a diameter of 70 cm." | "Mei's wheel" is unclear (it means her bicycle's wheel), and "On a bicycle trip" adds nothing. | "The wheel of Mei's bicycle has a diameter of 70 cm. How many complete turns does the wheel make in going 1.1 km? (Use π = 22/7.)" |
| Q27 | "Using this as the probability of being late, on about how many…" | "This" is vague (18 is a count, not a probability), and the opening phrase has no clear subject. | "The school bus was late on 18 of the last 60 school days. Use this record to estimate the probability that the bus is late. On about how many of the next 40 school days can the bus be expected to be late?" |
| Q21 (solution) | "…= 220 cm. 1.1 km = 110,000 cm, and…" | A sentence starts with a numeral (house rule). | "One turn covers the circumference πd = 22/7 × 70 = 220 cm. Then 1.1 km = 110,000 cm, and 110,000 ÷ 220 = 500 turns." |
| Q2 (solution) | "In lowest terms, a fraction terminates only if its denominator has no prime factor other than 2 and 5…" | This is the decimal-expansion theorem, which the brief keeps at Class 10. The solution also lists the reduced fractions in a different order from the options. | "27/150 = 9/50 = 0.18, 13/64 = 0.203125 and 21/56 = 3/8 = 0.375 all terminate: each can be written over a power of 10. Dividing, 14/45 = 0.3111…, which recurs." |

## Figures
| Q | Issue | Fix |
|---|---|---|
| Q42 | The "6 cm" label is outside the circle near the lower-left arc. It is partly hidden ("6 c…"), and it is not next to chord AB. | Place "6 cm" next to the midpoint of AB, inside the circle, with a white background or offset so it stays readable. |
| Q3 (minor) | The label "O" overlaps the meeting point of the many spokes, so it is hard to read. | Move the "O" label slightly below and to the left, clear of the lines. |
| Q4 (minor) | In the table, the "?" for Year 4 is left-aligned, while the other numbers are right-aligned. | Right-align (or centre) the "?" so the row reads consistently. |

I checked every other figure against its stem and found it accurate:
- Q1: the spacing on the number line is equal, and P is 2 parts after 3/4.
- Q7: the tiles are 3 x², 7 x and 2 ones.
- Q8: the line passes through (0, 3) and (2, −1).
- Q9 and Q39: there are 7 discs (Q39); the rows match the stem.
- Q11: the cut proportions are 10 : 3.
- Q14: P is (−5, 4) and Q is (3, −2).
- Q19: P, Q, R, S are at the midpoints, and the diagonals are in the ratio 1.4.
- Q22: the side lengths are in proportion.
- Q24: the angle drawn is about 90°.
- Q26 and Q29: the bars read exactly on gridlines and carry hatching, so they work in greyscale.
- Q28: there are 15 dots.
- Q30: the spinner parts are equal.
- Q32: F is (−4, −3) and G is (5, 9).
- Q38: Step 2 has 25 squares.
- Q44: AN : BN = 12 : 9.
- Right-angle squares are shown wherever an angle is given as 90°. Q20 and Q42 rely on the angle-in-a-semicircle theorem, which is intended.

## Syllabus / level / difficulty
- All 45 questions are inside the Class 9 syllabus (Ganita Manjari scope). There is no trigonometry anywhere, and Q44 (the SSA ambiguous case) is solved by circle geometry, not by sine. No question uses removed topics (surds, P/L drills, combined solids, range, time and work, or pigeonhole).
- Every Section I question stays within one chapter. All questions respect the computational ceiling: CI is 2 years at an integer rate (Q45), polynomials are degree ≤ 2, and no question uses unlisted surds.
- Q2's solution uses the Class 10 "denominator only 2s and 5s" theorem. The question itself is fine (students can divide), so only the solution needs the rewrite above.
- Possible level relabels (optional, kept as a swap so the counts stay 24 Easy + 16 Medium):
  - Q32 is labelled Easy but takes three steps (read coordinates, use the distance formula, apply the scale), which is Medium.
  - Q3 is labelled Medium but only needs spotting that √4 and √9 are the perfect squares among √2 to √10, which is Easy.
  - Suggested swap: Q32 to Medium and Q3 to Easy.
  - Q7 (factorising 3x² + 7x + 2 from tiles) is also borderline Easy/Medium. It can stay Easy because the tiles support the method.
- Distractors are mostly common-mistake answers. Examples: Q5 72% (averaging the two percentages); Q13 −92 (treating the GP as an AP); Q21 250/1,000 (radius/diameter mix-ups); Q30 5/12 (using ≥ instead of >); Q42 265 (using r = 10); Q43 (0, 6) (wrong fourth vertex) and (0, 1) (diagonal AC); Q44 3/10, 7/20, 11/20 (boundary errors). A few are weaker but acceptable: Q12 option D "2", Q24 180°, Q33 8 years.

## Questions with no issues
Q1, Q4 (apart from the minor table alignment), Q5, Q6, Q7, Q8, Q9, Q10, Q12, Q13, Q14, Q15, Q16, Q17, Q18, Q19, Q20, Q22, Q23, Q24, Q25, Q26, Q28, Q29, Q30, Q31, Q32, Q33, Q34, Q36, Q37, Q38, Q39, Q41, Q43, Q44, Q45.

## Topic list
- Q1 — Ch1 Number System — rational on a number line between 3/4 and 1 (17/20)
- Q2 — Ch1 — terminating vs recurring decimals (14/45)
- Q3 — Ch1 — square-root spiral: how many of √2 to √10 are rational (2)
- Q4 — Ch3 — constant-% growth (GP) in a table: 1,440 × 1.2 = 1,728
- Q5 — Ch3 — weighted average of pass percentages (70%)
- Q6 — Ch3 — 2-year depreciation at a constant % (₹150,000)
- Q7 — Ch4 Algebra — algebra tiles: factorise 3x² + 7x + 2
- Q8 — Ch4 — equation of a line from a graph (y = −2x + 3)
- Q9 — Ch4 — Σn: triangular marble pattern, 24 rows (300)
- Q10 — Ch4 — pair of linear equations with infinitely many solutions
- Q11 — Ch4 — (a + b)³ identity in a cut cube (1,170 cm³)
- Q12 — Ch4 — simplifying a rational expression by factorisation (51/50)
- Q13 — Ch4 — GP: find the 1st term from the 2nd and 5th terms (4)
- Q14 — Ch5 Geometry — midpoint from a grid (−1, 1)
- Q15 — Ch5 — exterior angle of a cyclic quadrilateral (84°)
- Q16 — Ch5 — perpendicular from the centre bisects a chord (42 cm)
- Q17 — Ch5 — congruence rule in a kite (SSS)
- Q18 — Ch5 — collinear points, find k (11)
- Q19 — Ch5 — midpoint quadrilateral perimeter = AC + BD (24 cm)
- Q20 — Ch5 — angle in a semicircle + cyclic quadrilateral (118°)
- Q21 — Ch6 Mensuration — wheel turns from circumference (500)
- Q22 — Ch6 — Heron's formula 11-13-20 (66 m²)
- Q23 — Ch6 — volume of a square pyramid (384 cm³)
- Q24 — Ch6 — sector angle from its perimeter (90°)
- Q25 — Ch6 — sphere in a cylinder, volume fraction (2/3)
- Q26 — Ch8 Data — stacked bar: total non-fiction (88)
- Q27 — Ch8 — empirical probability → expected count (12)
- Q28 — Ch8 — median from a dot plot (21)
- Q29 — Ch8 — stacked bar: greatest fraction (9C)
- Q30 — Ch8 — two spinners, product > 6 (1/4)
- Q31 — Ch9 Applied — linear model from a graph (2,300 L)
- Q32 — Ch9 — distance on an orchard grid with scale (600 m)
- Q33 — Ch9 — ages, pair of linear equations (12 years)
- Q34 — Ch9 — AP savings: first week over ₹400 (Week 25)
- Q35 — Ch10 Reasoning — converse of a statement
- Q36 — Ch10 — counterexample (28)
- Q37 — Ch10 — flowchart algorithm trace (65)
- Q38 — Ch10 — fractal counting, 5ⁿ (625)
- Q39 — Ch10 — Tower of Hanoi: moves of the 3rd-smallest disc (16)
- Q40 — Ch10 — proof by contradiction: the starting assumption
- Q41 — SII Ch4+Ch10 — algorithm with telescoping product (280)
- Q42 — SII Ch5+Ch6 — circle minus inscribed quadrilateral (29.5 cm²)
- Q43 — SII Ch4+Ch5 — parallelogram 4th vertex + line BD meets the y-axis (0, 4)
- Q44 — SII Ch8+Ch10 — SSA ambiguous case + probability (1/4)
- Q45 — SII Ch3+Ch9 — SI vs CI split of ₹30,000 (₹12,000)
