# Review — AMO Level 1, Class 11, Practice Paper 2 (v1)

**Verdict:** Strong paper. All 45 keys verified independently; every question has exactly one correct option and every solution is mathematically correct. No must-fix maths errors. The fixes are small: one answer cell shows only a letter (Q32), two solutions list values out of option order (Q7, Q32), two figure/rendering problems (Q22 label, Q44 label) and two equation glyph problems (Q5 conjugate, Q36 ⁿ).

**Key distribution:** A 11 · B 11 · C 12 · D 11 (balanced).
**Blueprint:** Ch1 5, Ch4 9, Ch5 5, Ch7 5, Ch8 7, Ch9 4, Ch10 5 = 40 ✔. Section I labels: 24 Easy + 16 Medium ✔. Section II pairings Q41 Ch4+Ch10, Q42 Ch4+Ch8, Q43 Ch1+Ch4, Q44 Ch5+Ch7, Q45 Ch8+Ch10 all match the brief ✔. No calculus, sets/functions, conics, polar form/De Moivre or trig equations ✔.

## Errors (must fix)
| Q | Problem | Fix |
|---|---|---|
| Q32 | Answer cell shows only "(C)" with no option text. | Add "a single discount of 30%" (JSON addrun). |

(No wrong keys, no double-correct options, no out-of-syllabus items.)

## Language & clarity
| Q | Current wording | Issue | Suggested rewrite (full text) |
|---|---|---|---|
| Q7 (solution) | "The other pairs come from 8 and 2, 18 and 2, and 6 and 6." | Pairs listed in order B, A, D — reads as mismatched. | "The other pairs come from 18 and 2, 8 and 2, and 6 and 6." |
| Q32 (solution) | "the prices are ₹1,400 (single 30%), ₹1,408, ₹1,404 and ₹1,410." | Prices unlabelled and not in option order; a student cannot tell which is which. | "Successive discounts multiply: the prices are ₹1,410 for (A), ₹1,408 for (B), ₹1,400 for (C) and ₹1,404 for (D). The single 30% discount is lowest." |
| Q35 | "…at the START of each of the 2 years." | All-caps word mid-sentence (house style uses plain text; timing is already clear). | "…at the start of each of the 2 years." |
| Q5 | Equation object "z + 2ź = 12 + 7i, where ź is the conjugate of z" | The conjugate renders with an ACUTE accent (ź), not an overbar (z̄); the solution uses z̄. Notation inconsistent and non-standard. Equation object — not in text runs. | Re-enter both equation objects with an overbar accent: z + 2z̄ = 12 + 7i, where z̄ is the conjugate of z. |
| Q36 | Options "2ⁿ > n²" and "4ⁿ ≥ 3n + 1" (also solution cell) | The Unicode ⁿ (U+207F) renders as a tiny mark that looks like a quote sign ("2" > n²") at print size, while ² renders well. | Use a superscript-formatted italic *n* (or an equation object) for the exponent in (A), (C) and the Q36 answer/solution cells. Formatting change, so not in JSON. |

## Figures
| Q | Issue | Fix |
|---|---|---|
| Q22 | The label "ribbon unwound" sits beside the lower-right quarter, i.e. next to the thin 90° arc that is NOT unwound; only colour (purple text = purple arc) links it to the thick 270° arc. Fails greyscale rule and can mislead. | Move the label next to the thick 270° arc (e.g. top-left) or add a leader line/arrow to the thick arc. |
| Q44 | The extended line AB passes through the "B" label, so B looks struck through. | Shift label B up-left clear of the line (or stop the line at the circle). |

Checked and correct: Q18 grid (A(3,1), B(1,3), angle marked at O); Q19 (P is the marked midpoint with equal-tick marks, M on x-axis, N on y-axis); Q27 dot plots (A = 2,4,6,8; B = 2,5,5,8; C = 1,1,9,9; D = 0,5,5,10 — all mean 5, variances 5, 4.5, 16, 12.5 as in the solution); Q44 angles 20° and 100° drawn from the positive x-axis.

## Syllabus / level / difficulty
- All topics inside the C11 brief; Q22 uses radian measure/arc length (part of "trig functions of any angle", NCERT C11) — acceptable.
- Q34 (budget with "at least 6 juice packs") is a one-variable linear inequality in an applied setting; the brief lists Linear Inequalities under both Ch4 (v5.1) and Ch9 (v5.6 receive), so Ch9 placement is acceptable.
- Computational ceiling respected: binomial index ≤ 6 in Section I (Q9 index 4, Q30 n = 6), factorials ≤ 10, complex numbers with integer parts, trig on standard values.
- Easy/Medium labels reasonable; counts are exactly 24/16. No relabel needed.
- Q45 uses population variance (NCERT convention); sample variance (19.2) is not an option, so no ambiguity.
- Distractors are mostly genuine common mistakes (e.g. Q9 101⁴, Q11 66, Q29 160 overcount / 330 = C(11,4), Q33 single-rate CI and SI, Q35 5,304/2, /2.04, /2.08, Q40 ordered 360 / C(24,2) = 276, Q41 242 = 3⁵ − 1, Q45 SD 4 and range² 64).

## Questions with no issues
Q1, Q2, Q3, Q4, Q6, Q8, Q9, Q10, Q11, Q12, Q13, Q14, Q15, Q16, Q17, Q18, Q19, Q20, Q21, Q23, Q24, Q25, Q26, Q27, Q28, Q29, Q30, Q31, Q33, Q34, Q37, Q38, Q39, Q40, Q41, Q42, Q43, Q45.

## Topic list
- Q1 — Ch1 complex numbers — greatest modulus
- Q2 — Ch1 complex numbers — quadrant of (2 − i)/i
- Q3 — Ch1 complex numbers — square root of 7 + 24i
- Q4 — Ch1 complex numbers — |z₁ − z₂| for complex roots of a quadratic
- Q5 — Ch1 complex numbers — solve z + 2z̄ = 12 + 7i
- Q6 — Ch4 GP — identify a GP
- Q7 — Ch4 AM–GM — impossible AM/GM pair
- Q8 — Ch4 AP — which number is a term
- Q9 — Ch4 binomial — 99⁴ via (100 − 1)⁴
- Q10 — Ch4 GP — ratio from sum to infinity
- Q11 — Ch4 special series — Σn³ = 4,356
- Q12 — Ch4 binomial — coefficient of x⁶ in (1 − x²)⁵
- Q13 — Ch4 GP — x, x + 8, x + 24
- Q14 — Ch4 sequences — aₙ = Sₙ − Sₙ₋₁
- Q15 — Ch5 straight lines — perpendicular line
- Q16 — Ch5 straight lines — collinear points
- Q17 — Ch5 straight lines — distance of point from line
- Q18 — Ch5 straight lines — angle between OA and OB (figure)
- Q19 — Ch5 straight lines — intercept form from midpoint (figure)
- Q20 — Ch7 trig of any angle — sign of values
- Q21 — Ch7 sum-to-product — sin 70° + sin 50°
- Q22 — Ch7 radian measure — arc length 270° (figure)
- Q23 — Ch7 multiple angle — sin 2A from sin A − cos A
- Q24 — Ch7 product-to-sum — 4 cos 52.5° cos 7.5°
- Q25 — Ch8 P&C — compare values
- Q26 — Ch8 permutations — 3 friends on 5 seats
- Q27 — Ch8 SD — dot plots (figure)
- Q28 — Ch8 binomial probability — exactly 2 of 3
- Q29 — Ch8 combinations — at least 3 girls
- Q30 — Ch8 binomial probability — most likely number (mode)
- Q31 — Ch8 variance — Σx² from mean and variance
- Q32 — Ch9 discount stacking — lowest price
- Q33 — Ch9 compound interest — variable rates
- Q34 — Ch9 budget linear inequality — max bottles
- Q35 — Ch9 SIP/time value — equal annual deposits
- Q36 — Ch10 induction — statement true for all n
- Q37 — Ch10 pigeonhole — baskets of mangoes
- Q38 — Ch10 induction — inductive step constant
- Q39 — Ch10 extremal — spreading pots
- Q40 — Ch10 combinatorial reasoning — desks in different rows and columns
- Q41 — Section II Ch4 + Ch10 — balanced-ternary weights, GP sum and extremal bound
- Q42 — Section II Ch4 + Ch8 — C(n,1), C(n,2), C(n,3) in AP
- Q43 — Section II Ch1 + Ch4 — i^(n(n+1)/2) = 1
- Q44 — Section II Ch5 + Ch7 — slope of chord via sum-to-product (figure)
- Q45 — Section II Ch8 + Ch10 — maximum variance (extremal)
