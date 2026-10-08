# Review — AMO Level 1, Class 11, Practice Paper 1 (v1)

**Verdict:** Strong paper. All 45 keys re-solved independently and correct; every question has exactly one correct option; figures match stems. Fixes needed: an outdated GST slab (Q32), two answer cells that show only a letter (Q33, Q38), and the conjugate symbol z̄ rendering as "ź" in Q2/Q3 (equation object).

**Key distribution:** A 11 · B 12 · C 11 · D 11 (balanced). Section I: 24 Easy + 16 Medium (meets the blueprint). Chapter counts Ch1 5 · Ch4 9 · Ch5 5 · Ch7 5 · Ch8 7 · Ch9 4 · Ch10 5 (match the blueprint). Section II pairings Q41 Ch4+Ch10, Q42 Ch4+Ch8, Q43 Ch1+Ch4, Q44 Ch5+Ch7, Q45 Ch8+Ch10 (all match).

## Errors (must fix)
| Q | Problem | Fix |
|---|---|---|
| Q32 | Fact: "GST of 12%". The 12% slab was abolished from 22 Sept 2025 (GST 2.0: 5% / 18%, plus 40%). | Use 18%: options (A) ₹1,526 (B) ₹126 (C) ₹252 (D) ₹63; key stays B; solution "CGST is half of 18%, that is 9%. 9% of ₹1,400 = ₹126." (in JSON) |
| Q33 | Answer cell shows only "(B)". | Add "4x + y ≤ 12 and x + 2y ≤ 10" (JSON addrun). |
| Q38 | Answer cell shows only "(A)". | Add the option text (JSON addrun). |
| Q2, Q3 | The conjugate z̄ is an OMML accent with chr "‾" (U+203E). It renders as an acute-like tick ("ź") in the PDF, so it does not read as a conjugate bar. The solutions correctly use z̄. | Equation edit, not in JSON: change the accent character to U+0305 (combining overline) or U+00AF, or use m:bar (top). Alternatively, replace the OMML with italic text "z̄" (z + U+0304), as in the solutions. Check both Q2 (stem) and Q3 (stem "z z̄"). |

## Language & clarity
| Q | Current wording | Issue | Suggested rewrite (full text) |
|---|---|---|---|
| Q11 sol | "Down: 12 m first. … Total 12 + 8 = 20 m." | Fragments | "The first fall is 12 m. After that, each bounce is travelled up and down: 2(3 + 0.75 + …) = 2 × 3 ÷ (1 − 1/4) = 8 m. The total is 12 + 8 = 20 m." |
| Q12 sol | "the terms with odd powers of 1 cancel" | Confusing: every power of 1 is 1 | "In the two expansions the terms with odd powers of √2 cancel, and the others double: 2[(√2)⁴ + 6(√2)² + 1] = 2(4 + 12 + 1) = 34." |
| Q25 sol | "8 stamps with 3 alike: 8!/3! = …" | Starts with a numeral; fragment | "There are 8 stamps with 3 alike, so there are 8!/3! = 40,320 ÷ 6 = 6,720 arrangements." |
| Q28 sol | "Mean = 50 ÷ 10 = 5. Squared deviations: …" | Fragments | "The mean is 50 ÷ 10 = 5. The squared deviations add up to 16 + 2 × 4 + 4 × 0 + 2 × 4 + 16 = 48, so the variance is 48 ÷ 10 = 4.8." |
| Q41 sol | "(p/q)⁶ ≤ 10 forces q ≥ 3" | Key step not justified | "…(p/q)⁶ ≤ 10 rules out q = 1 (ratio ≥ 2) and q = 2 ((3/2)⁶ > 11), so q ≥ 3, p ≥ 4 and the last term is at least 4⁶ = 4,096, which is too big." |
| Q43 (minor) | Options "−15 + 15i" etc. | The *i* is upright in the options but italic in the stem | Optional: italicise *i* in the options. Not in JSON. |

## Figures
| Q | Issue | Fix |
|---|---|---|
| Q2/Q3 | Conjugate accent renders as "ź" (see Errors). | Fix the equation accent. |
| Q33 (minor) | At the origin, the "0" tick labels on both axes overlap the "O" label. The axes are not named (trays of buns / trays of biscuits). | Drop the duplicate 0 labels or offset "O". Optional: axis titles "x (trays of buns)" and "y (trays of biscuits)". |
| Q44 (optional) | Only L and the 45° turning arc are drawn. This is acceptable (the new line is the unknown). | No change needed. |

All other figures checked: Q2 points P(−3,2), A(3,2), B(3,−2), C(−3,−2), D(2,−3). Q7 has distances from the gate. Q8 layers 1/4/9/16. Q10 number line −2 open, 3 filled. Q11 shows 12 m and 3 m. Q13 rows 1–5. Q15 points (−2,−1) and (2,5) with the line through (0,2). Q18 A(4,−1), B(0,1), C(4,4), with a square at the foot of the perpendicular (≈(1.6,2.2)). Q20 P at 210°. Q24 has a right-angle mark, 0.5 m, 1.5 m and 2 m. Q26 shows 8 vertices. Q27 has 3 equal sectors with hatching. Q28 dots 1,2,4,2,1 at 1,3,5,7,9 (n = 10). Q33 vertices (0,0), (3,0), (2,4), (0,5). Q45 shows 2/4/8/16 regions.

## Syllabus / level / difficulty
- All topics are within the Class 11 brief: complex numbers (no polar form or De Moivre), AP/GP/Σn², binomial (index ≤ 7), one-variable inequality, straight lines, compound/multiple/sum-to-product trig, P&C, binomial probability, variance, GST/EMI/time-work/two-variable inequality (Ch9 lists two-variable graphical inequalities), and pigeonhole/extremal/induction/invariant. **No calculus**, sets or conics.
- Computational ceiling respected: integer complex parts, integer sequence parameters, factorials ≤ 8!, standard trig values.
- Optional relabel swap, keeping the 24E/16M count: Q38 Easy → Medium (it needs the insight that the base case fails and n² + n + 1 is always odd), and Q30 Medium → Easy (one-step use of the property Var(ax + b) = a²Var). Q28 (two steps) is borderline Easy and can stay.
- Distractors are mostly common-mistake answers: Q9 (other terms / missing 2³), Q10 (sign and direction slips), Q28 (48, 29.8, 9.6), Q31 (complement, P(0) only), Q34 (no drain), Q40 (C(12,4) = 495), Q44 (clockwise turn gives (6,0)), Q45 (32 pattern trap).
- Cover chapter list and answer sheet: correct.

## Questions with no issues
Q1, Q4, Q5, Q6, Q7, Q8, Q9, Q10, Q13, Q14, Q15, Q16, Q17, Q18, Q19, Q20, Q21, Q22, Q23, Q24, Q26, Q27, Q29, Q30, Q31, Q34, Q35, Q36, Q37, Q39, Q40, Q42, Q44, Q45. Q11, Q12, Q25, Q28 and Q41 need solution wording only.

## Topic list
- Q1 — Ch1 — powers of i (i⁷⁵ = −i)
- Q2 — Ch1 — conjugate on an Argand diagram
- Q3 — Ch1 — z·z̄ = |z|²
- Q4 — Ch1 — product with zero real part
- Q5 — Ch1 — principal argument of a quotient
- Q6 — Ch4 — GP terms below 10,000
- Q7 — Ch4 — AP stakes (25th term)
- Q8 — Ch4 — Σn² apple pyramid
- Q9 — Ch4 — binomial 4th term of (x² + 2)⁷
- Q10 — Ch4 — linear inequality from a number line
- Q11 — Ch4 — bouncing ball, infinite GP
- Q12 — Ch4 — binomial (√2 + 1)⁴ + (√2 − 1)⁴
- Q13 — Ch4 — triangular-row sum (row 10)
- Q14 — Ch4 — three numbers in GP (product/sum)
- Q15 — Ch5 — line through two grid points
- Q16 — Ch5 — point-slope form, y-intercept
- Q17 — Ch5 — parallel lines, find k
- Q18 — Ch5 — distance from a point to a line
- Q19 — Ch5 — angle between lines
- Q20 — Ch7 — trig of 210° on the unit circle
- Q21 — Ch7 — sin(A − B)
- Q22 — Ch7 — cos⁴A − sin⁴A = cos 2A
- Q23 — Ch7 — sum-to-product
- Q24 — Ch7 — tan(A − B), notice board angle
- Q25 — Ch8 — permutations with identical items
- Q26 — Ch8 — C(8,3) triangles from cube vertices
- Q27 — Ch8 — binomial probability (spinner)
- Q28 — Ch8 — variance from a dot plot
- Q29 — Ch8 — lane arrangements, one lane between
- Q30 — Ch8 — variance under a linear change
- Q31 — Ch8 — binomial "at most one"
- Q32 — Ch9 — GST CGST/SGST split
- Q33 — Ch9 — two-variable inequalities from a graph
- Q34 — Ch9 — pipes and drain
- Q35 — Ch9 — EMI reducing balance (interest in instalment 2)
- Q36 — Ch10 — pigeonhole (marbles)
- Q37 — Ch10 — extremal (books)
- Q38 — Ch10 — induction needs a base case
- Q39 — Ch10 — invariant (a + b − 1)
- Q40 — Ch10 — stars and bars with a minimum of 2
- Q41 — Ch4 + Ch10 — longest integer GP in [100, 1000]
- Q42 — Ch4 + Ch8 — first-six game, infinite GP
- Q43 — Ch1 + Ch4 — GP sum of powers of 1 + i
- Q44 — Ch5 + Ch7 — line rotated 45°, tan(θ + 45°)
- Q45 — Ch8 + Ch10 — circle regions (1 + C(n,2) + C(n,4))
