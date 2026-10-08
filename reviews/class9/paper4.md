# Review: AMO Level 1, Class 9, Practice Paper 4

## Verdict
The paper is sound. All 45 keys are correct, every question has exactly one correct option, the worked solutions are right, and the figures match their stems. Must-fix items are small: Q30 uses multi-stage probability (C10 content) in its solution, and six answer cells show only a letter. Blueprint (3/3/7/7/5/5/4/6 = 40), 24 Easy + 16 Medium and the Section II pairings all match the brief.

Key distribution: A 11 · B 11 · C 12 · D 11 (balanced).

## Errors (must fix)
| Q | Problem | Fix |
|---|---|---|
| Q30 | The solution multiplies stage probabilities (5/6 × 1/6 + 1/6 × 5/6). The v5.7 log (D19) moves compound / multi-stage probability to C10. C9 has only theoretical probability on a sample space, with tables and tree diagrams. | Keep the stem and the answer, and count outcomes in the solution instead: "There are 6 × 6 = 36 equally likely (Monday, Tuesday) choices. The boy leads on exactly one day in 5 + 5 = 10 of them (girl then boy, or boy then girl), so the probability is 10/36 = 5/18." (in fixes JSON) |
| Q2, Q10, Q17, Q20, Q28, Q31 | The answer cell in the solutions table shows only the letter. | Add the option text after the letter (addrun fixes in JSON). |

## Language & clarity
| Q | Current wording | Issue | Suggested rewrite (full text) |
|---|---|---|---|
| Q6 | "Sonal runs a bookshop. She kept some money in a bank…" | The first sentence is irrelevant to the question. | "Sonal kept some money in a bank for 2 years at 20% per year compound interest, compounded annually, and it grew to ₹36,000. How much would the same money have grown to in the same 2 years at 20% per year simple interest?" |
| Q37 | Option (C) "51 is a prime number." | The sentence starts with a numeral (house rule). | Option (C): "The number 51 is prime." Update the answer cell to match. Solution: "The sentence "The number 51 is prime" is a proposition; it happens to be false, since 51 = 3 × 17. A question, an instruction and an exclamation are not true or false." |
| Q43 | "The points are A(0, 3) and B(4, 1)." | Awkward opening. | "A is the point (0, 3) and B is the point (4, 1). The point P lies on the line y = 3x − 5, and P is at the same distance from A as from B. What are the coordinates of P?" |
| Solutions Q1, Q9, Q10, Q12, Q13, Q41 | For example, "3y = 6x − 9, so…" and "…d = 8. 93 = 13 + …" | These solution sentences start with a numeral. | Add a lead-in word: "Here 7/37 = …", "Then 5n + 1 = 151 …", "Here 3y = 6x − 9 …", "Here 3x² + 10x + 8 = …", "Then 93 = 13 + (n − 1) × 8 …", "Since 100 = 16 × 6 + 4, the sum is …" (all in JSON) |
| Q38 | Options "a = 6 and b = 9" etc. | The letters are upright in the options but italic in the stem. | Optional: italicise a and b in the options (formatting only; not in JSON). |

## Figures
| Q | Issue | Fix |
|---|---|---|
| Q23 | The 4 m vertical height has no right-angle square where it meets the base. The visual rule says right angles are always shown and never inferred, and Q22's cone does mark it. | Add a small right-angle square at the foot of the height. |
| Q25 | The cube is labelled 4 cm on every edge. This gives away the step "volume 64 cm³ → edge 4 cm" that the question means students to work out. | Mark the cube edges "?" (or leave the cube unlabelled). |
| Q32 | Axis labels collide: "−1" and "O" run together as "−1O", the y-axis "−1" sits on the arrowhead, and the "7" on the x-axis and the "8" on the y-axis touch the arrowheads. | Space out the origin labels, and stop the axes one unit beyond the last numbered tick. |
| Q21 | The "14 cm" label sits on the radius line and touches the centre. | Move the label just above the radius. |
| Q24, Q25 | The "10 m" label (Q24) and the slab's "4 cm" label (Q25) touch the drawn edges. | Nudge the labels clear of the lines (cosmetic). |

All other figures were checked and are correct: Q9 (6/11/16 crayons with shared sides), Q15 (midpoint ticks, parallel arrows), Q18 (x at ∠BEC; 35° at A, 40° at C), Q19 (equal-chord marks, x at C), Q22 (right angle marked), Q26 table (bold headers, units), Q32 (K(−2,1), L(6,1), M(6,7), N(−2,7) → 8 × 6 units), Q35 (3 lines with 3 distinct crossings, 7 regions) and Q42 (tick marks match 15/20 cm).

## Syllabus / level / difficulty
- Blueprint is exact: Ch1 Q1–3, Ch3 Q4–6, Ch4 Q7–13, Ch5 Q14–20, Ch6 Q21–25, Ch8 Q26–30, Ch9 Q31–34, Ch10 Q35–40. There are exactly 24 Easy and 16 Medium.
- Section II pairings match the brief: Q41 Ch4+Ch10, Q42 Ch5+Ch6, Q43 Ch4+Ch5, Q44 Ch8+Ch10, Q45 Ch3+Ch9. Q44 uses algorithm tracing (GM Ch11) rather than the brief's proposition/converse, which is acceptable within Ch10.
- There is no trigonometry, no surds beyond √2 in a solution, no quadratic equations, and CI runs only 2 years at an integer rate. Everything is within the ceiling.
- Q30: the stem is fine, but the solution method is C10 (see Errors). Q44's 36-outcome two-dice sample space is a single event on a table, so it is fine at C9.
- Q33 (boats and streams) is in syllabus because it is solved as a pair of linear equations (speed contexts, GM Ch13). It is close to competitive-exam arithmetic, so avoid more of this type.
- Q44's key insight is that the subtraction algorithm preserves the HCF. That is acceptable for a Hard question, and brute-force tracing also works.
- Q22 and Q23 are labelled Easy but each needs two steps (slant height, then area). They are borderline. No swap is proposed because no Medium question is clearly 1-step.
- Q24 needs √7,056 (raw arithmetic). This is acceptable for Heron's formula at Medium.

## Questions with no issues
Q3, Q4, Q5, Q7, Q8, Q11, Q14, Q15, Q16, Q18, Q19, Q22, Q26, Q27, Q29, Q33, Q34, Q35, Q36, Q39, Q40, Q42, Q44, Q45

## Topic list
- Q1 — Ch1 recurring decimals — 7/37 from 1/37 = 0.027027…
- Q2 — Ch1 recurring decimals — which value ≠ 0.5 (0.4555…)
- Q3 — Ch1 irrational numbers — rational + irrational is always irrational
- Q4 — Ch3 compound growth (GP) — 250 × 1.08ⁿ
- Q5 — Ch3 SI as AP — amount after 5 years
- Q6 — Ch3 CI vs SI — back out principal from 2-yr CI, find SI amount
- Q7 — Ch4 pair of linear equations — x − y by subtraction
- Q8 — Ch4 identities — x² + y² from x + y, xy
- Q9 — Ch4 AP nth term — crayon hexagons, 151 crayons
- Q10 — Ch4 straight-line graph — slope/intercept of 6x − 3y = 9
- Q11 — Ch4 factorisation — x² − (y − 3)²
- Q12 — Ch4 factorising quadratic — rectangle perimeter
- Q13 — Ch4 AP — two-digit numbers ≡ 5 (mod 8)
- Q14 — Ch5 circles — diameter is longest chord
- Q15 — Ch5 midpoint theorem converse — AE
- Q16 — Ch5 cyclic quadrilaterals — isosceles trapezium
- Q17 — Ch5 circles — perpendicular bisectors of chords meet at centre
- Q18 — Ch5 angles in the same segment — ∠BEC
- Q19 — Ch5 equal chords, equal central angles — base angle 55°
- Q20 — Ch5 coordinates — classify ABCD by distances (rhombus)
- Q21 — Ch6 sector area — 1/8 of a circle, r = 14
- Q22 — Ch6 cone CSA — slant height then πrl
- Q23 — Ch6 pyramid lateral area — slant height 5 m
- Q24 — Ch6 Heron's formula — altitude to 21 m side
- Q25 — Ch6 SA/volume — cuboid melted into cube, SA difference
- Q26 — Ch8 weighted mean — egg masses
- Q27 — Ch8 theoretical probability — not red
- Q28 — Ch8 statistical questions — identify the one with variable data
- Q29 — Ch8 probability — square or cube in 1–50
- Q30 — Ch8 probability — boy leads on exactly one of two days
- Q31 — Ch9 linear model — meaning of slope
- Q32 — Ch9 coordinates in real world — floor-plan area with scale
- Q33 — Ch9 two-variable modelling — current speed (downstream/upstream)
- Q34 — Ch9 linear model — temperature vs height
- Q35 — Ch10 recurrence — regions made by lines
- Q36 — Ch10 algorithms — trial-division step count for 91
- Q37 — Ch10 propositions — identify a proposition
- Q38 — Ch10 converse — counterexample
- Q39 — Ch10 recurrence — staircase 1/2-step ways (34)
- Q40 — Ch10 Tower of Hanoi — move on which largest disc moves
- Q41 — Ch4+Ch10 — recursive sequence a(n) = a(n−1) − a(n−2), sum of 100 terms
- Q42 — Ch5+Ch6 — cyclic kite → diameter 25, circumference
- Q43 — Ch4+Ch5 — point on line equidistant from A and B
- Q44 — Ch8+Ch10 — subtraction (HCF) algorithm on two dice, P(prints 1)
- Q45 — Ch3+Ch9 — AP vs GP estimate of the missing middle year
