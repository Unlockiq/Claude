# Review: AMO Level 1, Class 11, Practice Paper 3 (v1)

**Verdict:** This is a strong, clean paper. I solved all 45 questions independently, and every key matches with exactly one correct option. Every figure agrees with its stem. The blueprint is met: Ch1 5, Ch4 9, Ch5 5, Ch7 5, Ch8 7, Ch9 4, Ch10 5. Section I has exactly 24 Easy and 16 Medium, and the Section II pairings match the brief. No calculus, sets/functions, conics, polar form or trig equations appear. Only one item breaks a rule: Q25 goes over the P&C ceiling. The other fixes are small wording and solution changes.

**Key distribution:** A 11 · B 11 · C 11 · D 12. There are no long runs of one letter.

## Errors (must fix)

| Q | Problem | Fix |
|---|---|---|
| Q25 | This question breaks the computational ceiling for P&C ("numbers ≤ 10 in factorials"). With 12 stops the count is ¹²P₂ = 12!/10!. The arithmetic is easy, but the cap is a hard cap in Section I. | Change to **10 stops**. The options become (A) 100, (B) 45, (C) 90, (D) 81, and the key stays **C**. Solution: "The start can be any of 10 stops and the end any of the other 9: 10 × 9 = 90." The answer cell becomes 90. All of this is in the JSON. |

There are no wrong keys, no question with several correct options, and no figure that contradicts its stem.

## Language & clarity

| Q | Current wording | Issue | Suggested rewrite (full text) |
|---|---|---|---|
| Q16 (options) | (A) 90° … (D) 120° | The stem says θ is *acute*, so 120° (and 90°) can be ruled out at once. These are weak distractors. | Change (D) to **45°**, so the options are 90°, 30°, 60°, 45°. Optionally, also replace (A) 90° with 15°. |
| Q37 | "Some different whole numbers are to be chosen. What is the least number of them that must be chosen so that, however they are chosen, some two of them have a difference divisible by 9?" | The opening sentence is awkward and "some two of them" is clumsy. | "What is the least number of different whole numbers that must be chosen so that, however they are chosen, two of them always have a difference divisible by 9?" |
| Q1 (sol) | "A number times its conjugate is a² + b²." | The solution uses a and b without defining them. | "The number a + ib times its conjugate a − ib is a² + b². So (1 + 3i)(1 − 3i) = 1 + 9 = 10." |
| Q4 (sol) | "(1 − i)² = 1 − 2i + i² = −2i. …" | The sentence starts with a numeral expression. | "First, (1 − i)² = 1 − 2i + i² = −2i. So (1 − i)⁶ = (−2i)³ = −8i³ = −8 × (−i) = 8i." |
| Q9 (sol) | "5(3ⁿ − 1) ÷ 2 = 1,820 gives …" | The sentence starts with a numeral, and n is not introduced. | "The sum of n terms is 5(3ⁿ − 1) ÷ 2 = 1,820, so 3ⁿ − 1 = 728, 3ⁿ = 729 and n = 6." |
| Q16 (sol) | "The line x = 2 makes 90° with it" | "With it" reads as 90° with the first line, which is wrong. | "The first line has slope √3, so it makes 60° with the x-axis. The line x = 2 is vertical and makes 90° with the x-axis, so θ = 90° − 60° = 30°." |
| Q22 (sol) | "cos 3A = 4 cos³A − …" | The sentence starts with a formula. | Start with "Here cos 3A = …" and keep the rest unchanged. |
| Q24 (sol) | "tan 50° = (tan 70° − …" | The sentence starts with a formula. | Start with "Here tan 50° = …" and keep the rest unchanged. |
| Q30 (sol) | "4pq³ = 6p²q² gives 4q = 6p, …" | The sentence starts with a numeral, and q is not defined. | "With q = 1 − p, the condition is 4pq³ = 6p²q². Dividing by 2pq² gives 2q = 3p, so 2(1 − p) = 3p and p = 2/5." |
| Q34 (sol) | "200 + 35w ≥ 1,000 gives …" | The sentence starts with a numeral, and w is not defined. | "After w weeks he has ₹(200 + 35w). Then 200 + 35w ≥ 1,000 gives w ≥ 800 ÷ 35 ≈ 22.9. The least whole number of weeks is 23." |
| Q36 (sol) | "3¹ > 1 and 3² > 8, but …" | The sentence starts with a numeral. | "It holds at n = 1 and n = 2 (3 > 1, 9 > 8), but at n = 3 both sides equal 27, so it fails. From n = 4 on it holds (81 > 64), and the step 3k³ ≥ (k + 1)³ keeps it going. The least start is 4." |
| Q44 (sol) | "… tan θ = 1/3. tan 2θ = …" | A sentence starts with lowercase "tan". | "… where tan θ = 1/3. Then tan 2θ = (2/3)/(1 − 1/9) = 3/4, …" |
| Q24 (stem) | "What number goes in the box? tan 70° − tan 20° = □ × tan 50°" | The equation comes after the question mark. This is acceptable, but Q21 and Q22 use the order "For every angle …, [equation]. What …?" (low priority). | If you re-typeset it: "In tan 70° − tan 20° = □ × tan 50°, what number goes in the box?" This is not in the JSON because the equation is an OMML object. |

## Figures

| Q | Issue | Fix |
|---|---|---|
| Q19 | The platform is named as a square in the text, but the drawing has no right-angle marks. The brief says right angles are always shown with a square symbol. Minor, because the stem states "square". | Optional: add a right-angle mark at one corner of the platform. |
| Q18 | The x-axis tick labels "−2 −1 O" are crowded together near the origin. | Optional: space out or drop the "−2" label. |

I checked the other figures and found them correct. Q2 has A at (2, 1) and B at (−1, 3). In Q11 the pattern counts 1/7/19 match 3n² − 3n + 1. In Q15 the slopes are A −2, B 1/2, C −1/2 and D 2, so only C works. In Q16 θ is marked between the vertical line and the line of slope √3, which gives 30°. In Q20 the clock shows 3:40 with the hour hand two-thirds of the way from 3 to 4. In Q23 the right angle at G is marked and the 45°/75°/20 m labels match. Q27's table has bold headers with units. Q40 shows 10 posts numbered 1–10. Q43 has its points at 1, (½, ½), (0, ½), (−¼, ¼), (−¼, 0), (−⅛, −⅛). In Q44 the drawn slopes are 1/3 and 3/4, the right angle is marked and the unknown is shown as "?".

## Syllabus / level / difficulty

- **Q25** goes over the P&C ceiling (12 > 10); see Errors.
- **Q24** uses tan 70°, tan 20° and tan 50°, which are not standard reference values. The ceiling says "compound angles on standard reference values". No values are computed (only the identity tan(A − B) and tan 70° · tan 20° = 1), so I treat this as acceptable but borderline. If you want to be strict, rework it on 75°/15°/60°.
- **Q5** is in Ch1 (complex roots), but Vieta's formulas alone give −16, so the complex-number content is incidental. Acceptable.
- **Q34** is an applied savings problem solved with a linear inequality. At C11, linear inequalities belong to Ch4, but the context is Ch9 (SIP/time value). Acceptable.
- **Q39** (acute angles of a convex polygon) is an extremal argument and fits Ch10.
- **Q43** (z = (1 + i)/2) and **Q44** (tan θ = 1/3) go beyond the "integer a, b" and "standard values" ceilings. They are in Section II, where this is allowed, and they need it.
- **Difficulty:** Section I has 24 E and 16 M, exactly on target. Q6 (cancellation in the binomial sum) and Q22 (cos 3A plus a conversion to sin) are at the top of Easy. If you raise either to Medium, lower one Medium item to Easy to keep 24/16 (Q4 or Q31 are the closest candidates). No change is required.
- All Section II pairings match the brief: Q41 Ch4 + Ch10, Q42 Ch4 + Ch8, Q43 Ch1 + Ch4, Q44 Ch5 + Ch7, Q45 Ch8 + Ch10.
- The cover, the answer sheet and the key are correct. Every answer cell shows the option text as well as the letter. The quick-answer grid matches the solutions table.

## Questions with no issues

Q2, Q3, Q5, Q6, Q7, Q8, Q10, Q11, Q12, Q13, Q14, Q15, Q17, Q18, Q20, Q21, Q23, Q26, Q27, Q28, Q29, Q31, Q32, Q33, Q35, Q38, Q39, Q40, Q41, Q42, Q43, Q45. Q18 and Q19 have only the optional figure notes above.

## Topic list

- Q1 — Ch1 Complex numbers — conjugate: (1 + 3i) × □ = 10
- Q2 — Ch1 Complex numbers — Argand plane, product of two points
- Q3 — Ch1 Complex numbers — modulus of (2 + i)⁴
- Q4 — Ch1 Complex numbers — (1 − i)⁶
- Q5 — Ch1 Complex numbers — α² + β² for x² + 2x + 10 = 0
- Q6 — Ch4 Binomial — number of terms in (x + y)¹⁰ + (x − y)¹⁰
- Q7 — Ch4 Linear inequalities — missing constant from the solution set
- Q8 — Ch4 AP — a₅ + a₁₆ = 40, find S₂₀
- Q9 — Ch4 GP — number of terms for a sum of 1,820
- Q10 — Ch4 GP — sum to infinity from the 4th term
- Q11 — Ch4 Special series — Σ(3n² − 3n + 1), honeycomb
- Q12 — Ch4 Binomial — greatest coefficient in (1 + 2x)⁷
- Q13 — Ch4 GP — each term equals the sum of the next two
- Q14 — Ch4 AP — rows of boats, Sₙ = 300
- Q15 — Ch5 Straight lines — pick the line of slope −1/2 from 4 grids
- Q16 — Ch5 Straight lines — angle between y = √3x + 1 and x = 2
- Q17 — Ch5 Straight lines — intercepts sum to 5
- Q18 — Ch5 Straight lines — perpendicular bisector of AB
- Q19 — Ch5 Straight lines — distance between parallel lines, square area
- Q20 — Ch7 Trig/angle measure — minute-hand turn in radians
- Q21 — Ch7 Compound angles — sin(x + 30°) + sin(x − 30°)
- Q22 — Ch7 Multiple angles — cos 3A in terms of sin²A
- Q23 — Ch7 Heights & distances — tan 75°, tower height
- Q24 — Ch7 Compound angles — tan 70° − tan 20° = 2 tan 50°
- Q25 — Ch8 Permutations — ordered start/end tickets
- Q26 — Ch8 Combinations — C(n, 2) = 28 games
- Q27 — Ch8 Standard deviation — lap-time table
- Q28 — Ch8 Combinations — non-empty subsets of 6 fillings
- Q29 — Ch8 Permutations — 5-digit numbers divisible by 4
- Q30 — Ch8 Binomial probability — P(1 hit) = P(2 hits)
- Q31 — Ch8 Variance — adding a value equal to the mean
- Q32 — Ch9 GST — GST contained in an inclusive price
- Q33 — Ch9 Break-even — least price per pot
- Q34 — Ch9 Savings/time value — weeks to reach ₹1,000
- Q35 — Ch9 Reducing-balance loan — balance after 2 repayments
- Q36 — Ch10 Induction — least base case for 3ⁿ > n³
- Q37 — Ch10 Pigeonhole — difference divisible by 9
- Q38 — Ch10 Induction logic — P(k) ⇒ P(k + 1), P(5) false
- Q39 — Ch10 Extremal — maximum acute angles in a convex 9-gon
- Q40 — Ch10 Combinatorial reasoning — non-adjacent posts, C(8, 3)
- Q41 — Ch4 + Ch10 — least a₁₀ of a super-increasing sequence
- Q42 — Ch4 + Ch8 — AP with given mean and variance
- Q43 — Ch1 + Ch4 — spiral path zᵏ, GP of step lengths
- Q44 — Ch5 + Ch7 — tan 2θ, distance from point to line
- Q45 — Ch8 + Ch10 — pigeonhole on 35 club-sets
