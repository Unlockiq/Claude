# Review: AMO Level 1, Class 11, Practice Paper 5 (v1)

**Verdict:** This is a strong paper. All 45 keys are correct, every question has exactly one correct option, and the worked solutions check out. There is one must-fix: Q27 goes over the computational ceiling because its answer needs 4 decimal places. Q21's answer cell shows only the letter. The rest are small wording, distractor and greyscale fixes.

**Key distribution:** A 11 · B 11 · C 12 · D 11 (balanced). Blueprint: Ch1 5, Ch4 9, Ch5 5, Ch7 5, Ch8 7, Ch9 4, Ch10 5, plus Section II 5. Section I labels: 24 Easy + 16 Medium. Section II pairings (Q41 Ch4+Ch10, Q42 Ch4+Ch8, Q43 Ch1+Ch4, Q44 Ch5+Ch7, Q45 Ch8+Ch10) match the brief.

## Errors (must fix)
| Q | Problem | Fix |
|---|---|---|
| Q27 | The answer 0.7599 and the distractors 0.2401, 0.4116 and 0.9919 have 4 decimal places. The C11 ceiling is "Decimals: up to 3 dp", and Section I has a hard cap. | Change "4 days" to "3 days" (in both places). Options become (A) 0.657 (correct: 1 − 0.7³), (B) 0.343 (all dry), (C) 0.441 (exactly one rainy day), (D) 0.973 (1 − 0.3³). Update the key cell and the solution. This is in the JSON. |
| Q21 | The answer cell in the key shows only "(A)". | Add the text "(−4/5, 3/5)" (addrun, in the JSON). |

## Language & clarity
| Q | Current wording | Issue | Suggested rewrite (full text) |
|---|---|---|---|
| Q21 | "…lie on a unit circle about the origin O. … Where is Q?" | "Where is Q?" is vague, and the options are coordinates. "About the origin" is loose. | "In the figure, P(3/5, 4/5) and Q lie on a unit circle centred at the origin O. OP makes the angle θ with the positive x-axis, and OQ is OP turned anticlockwise through a right angle. What are the coordinates of Q?" |
| Q28 | "…the numbers of planes that landed in five hours were recorded as 5, 8, 11, 14 and 17." | This reads as one total for the five hours, but the data are per hour. | "At an airport, the numbers of planes that landed in each of five hours were recorded as 5, 8, 11, 14 and 17. The variance of these numbers is 18. Later it was found that the 17 was a mistake: the true number was 2. What is the variance of the corrected numbers?" |
| Q31 | "6 parallel lines (black) are crossed by 4 other parallel lines (purple)." | Colour carries information here, which breaks the greyscale rule. Direction already tells the two families apart. | "In the figure, 6 horizontal parallel lines are crossed by 4 slanting parallel lines. How many parallelograms of all sizes are formed whose four sides lie along these lines?" (The solution also changes to say "horizontal" and "slanting".) |
| Q40 | "…such as 1,358?" | A comma inside a digit-pattern example is distracting. | "How many 4-digit numbers have digits that strictly increase from left to right, such as 1358?" |
| Q43 | "…the others are imaginary." | The precise term is "purely imaginary". | "The expression (x + 2i)⁶ is expanded in powers of x. Some of the coefficients are real numbers and the others are purely imaginary. What is the sum of the real coefficients?" |
| Q10 (solution) | "3x + 2 > 14 gives 3x > 12, … 13 − 2x ≥ −5 gives …" | Two sentences start with a numeral (house rule). | "From 3x + 2 > 14, 3x > 12, so x > 4. From 13 − 2x ≥ −5, −2x ≥ −18, so x ≤ 9 (the sign turns round). Together, 4 < x ≤ 9." |
| Q11 (option A) | "−8" | This is not a plausible mistake. | Use "−4", which is the reversed subtraction 6 − 10. |

## Figures
| Q | Issue | Fix |
|---|---|---|
| Q5 | The tick labels "5" (imaginary axis) and "3" (real axis) sit on the arrowheads, and "O" crowds the 0 position. P(−1, 4) and R(−1, −4) are on grid intersections, which is correct. | Cosmetic only: move the end-tick labels clear of the arrowheads. No text change is needed. |
| Q35 | The "60" tick label overlaps the line x + y = 60. The corners (60, 0), (40, 20) and (0, 40) are drawn correctly, and the hatching works in greyscale. | Cosmetic: nudge the label. |

The other figures were checked and are correct:
- **Q16:** negative x-intercept, positive y-intercept, no numbers given away.
- **Q18:** A(2, 6), B(8, 3), and M at about x = 6, which matches the scale.
- **Q21:** the right angle at O is marked with a square.
- **Q24:** the right angle at G is marked with a square, GA = 100 m, GB = 600 m, and the "?" is at P.
- **Q31:** there are 6 horizontal and 4 slanting lines.
- **Q38:** the 8 columns show all 8 distinct patterns.
- **Q44:** A is on y = x in quadrant I, B is above the line with x < 0, and equal-side ticks are shown.

## Syllabus / level / difficulty
- All topics are in the C11 syllabus. No calculus, sets, functions, conics or polar form appear. Q35 (graphical linear inequalities / LP corner points) fits the Ch9 "LP/optimisation foundation" item.
- The ceiling is respected everywhere except Q27 (4 dp, fixed above). The binomial index is ≤ 10, and the P&C factorials are ≤ 10.
- Each Section I question stays within one chapter. There is no pure aptitude reasoning.
- Difficulty (optional): Q17 is labelled Easy but needs the distance formula with two absolute-value cases, so it reads as Medium. Q31 (C(6,2) × C(4,2)) is close to one step. If you change one, swap them (Q17 to Medium, Q31 to Easy) to keep 24 Easy + 16 Medium.
- Distractor (minor): Q45 option (D) "2" is not a common-mistake answer. Something like 5 or 6 (a miscount of pair usage) would be better. It is not in the JSON because no single obvious mistake gives a specific value.

## Questions with no issues
Q1, Q2, Q3, Q4, Q5 (text), Q6, Q7, Q8, Q9, Q12, Q13, Q14, Q15, Q16, Q17, Q18, Q19, Q20, Q22, Q23, Q24, Q25, Q26, Q29, Q30, Q32, Q33, Q34, Q35, Q36, Q37, Q38, Q39, Q41, Q42, Q44, Q45.

## Topic list
- Q1 — Ch1 complex numbers — conjugate equality, find x + y
- Q2 — Ch1 complex numbers — |z| = |z − 4|
- Q3 — Ch1 powers of i — count real values among i¹…i²⁰
- Q4 — Ch1 modulus — z + |z| = 2 + 8i
- Q5 — Ch1 Argand plane — conjugate roots from a figure, then p + q
- Q6 — Ch4 GP — first term from T2 and T5
- Q7 — Ch4 AP — first negative term
- Q8 — Ch4 AP — pentagon angles
- Q9 — Ch4 binomial — C(n,2) = 36
- Q10 — Ch4 linear inequalities — two conditions combined
- Q11 — Ch4 AM and GM — difference of middle terms
- Q12 — Ch4 infinite GP — sum and sum of squares
- Q13 — Ch4 series — alternating sum of squares
- Q14 — Ch4 binomial — ratio of middle-term coefficients
- Q15 — Ch5 straight lines — intercept form, y-intercept
- Q16 — Ch5 straight lines — intercept signs from a figure
- Q17 — Ch5 distance of a point from a line — two points on the y-axis
- Q18 — Ch5 straight lines — reflection point on a mirror
- Q19 — Ch5 family of lines — fixed point
- Q20 — Ch7 trig of any angle — sin 200°
- Q21 — Ch7 compound angle — rotating a point by 90°
- Q22 — Ch7 sum-to-product — (sin 80° − sin 20°)/cos 50°
- Q23 — Ch7 multiple angle — tan 22.5°
- Q24 — Ch7 heights and distances + tan(A − B) — angle at the balloon
- Q25 — Ch8 combinations — cone and scoops
- Q26 — Ch8 permutations — Myra first or last
- Q27 — Ch8 probability — at least one rainy day
- Q28 — Ch8 variance — shift invariance
- Q29 — Ch8 combinations — both-or-neither condition
- Q30 — Ch8 binomial probability — exactly 2 of 3
- Q31 — Ch8 combinations — parallelograms from line families
- Q32 — Ch9 GST — two slabs
- Q33 — Ch9 compound interest — doubling time
- Q34 — Ch9 depreciation — 10% for 3 years
- Q35 — Ch9 linear inequalities / LP — maximum income
- Q36 — Ch10 combinatorial reasoning — handshake parity
- Q37 — Ch10 induction — base cases for an n → n + 3 step
- Q38 — Ch10 pigeonhole — 3-row columns
- Q39 — Ch10 extremal — chess wins
- Q40 — Ch10 combinatorial reasoning — strictly increasing 4-digit numbers
- Q41 — SII Ch4 + Ch10 — 105 as a sum of consecutive integers
- Q42 — SII Ch4 + Ch8 — 3-term APs from 1 to 25
- Q43 — SII Ch1 + Ch4 — real coefficients of (x + 2i)⁶
- Q44 — SII Ch5 + Ch7 — slopes in an equilateral triangle on y = x
- Q45 — SII Ch8 + Ch10 — maximum scenes (Fano plane)
