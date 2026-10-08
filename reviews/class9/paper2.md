# Review — AMO Level 1, Class 9, Practice Paper 2

**Verdict:** A sound paper. All 45 keys are correct and every question has exactly one correct option. No content is out of syllabus (no trigonometry; blueprint 3/3/7/7/5/5/4/6 and 24 Easy + 16 Medium are met). The fixes needed are small: 11 answer cells show only a letter, a few solutions start with a numeral or are imprecise (Q16, Q12), the Q25 solution uses raw arithmetic, two stems need light rewording (Q9, Q45), and two figures have label-placement problems (Q25, Q35).

**Key distribution:** A 11 · B 13 · C 11 · D 10 (balanced).

## Errors (must fix)
| Q | Problem | Fix |
|---|---|---|
| Q1, Q6, Q16, Q21, Q28, Q32, Q33, Q35, Q36, Q38, Q40 | The answer cell in the solutions table shows only the letter (e.g. "(D)"), with no answer text. | Add the option text as a separate run (addrun items in paper2_fixes.json). |
| Q16 (solution) | "An isosceles trapezium or a kite fits each of the other descriptions" is inaccurate. A kite does not fit (C) or (D), and an isosceles trapezium does not fit (B). | "A kite fits (B) and an isosceles trapezium fits (C) and (D), but neither is a parallelogram." |
| Q25 (solution) | √15,876 is raw multiplication plus a square root, which goes against the C9 ceiling ("use simplification; avoid raw multiplication"). | Show the factorisation: √(27 × 14 × 7 × 6) = √(3⁴ × 2² × 7²) = 9 × 2 × 7 = 126 m². |

No wrong keys, no broken questions and nothing out of syllabus.

## Language & clarity
| Q | Current wording | Issue | Suggested rewrite (full text) |
|---|---|---|---|
| Q9 | p(x) = ax + b is a linear polynomial with p(0) = 5 and p(2) = −1. What is p(4)? | The sentence starts with a symbol rather than a word. | The linear polynomial p(x) = ax + b has p(0) = 5 and p(2) = −1. What is p(4)? |
| Q45 | …At the end of each year, Umesh sells the same number of fish. Just after the second year's sale there are 3,000 fish… | "the same number of fish" does not say what it is the same as. | A fish farm has 2,000 fish at the start. During each year the number of fish grows by 50%. At the end of each of the 2 years, Umesh sells the same number of fish. Just after the second sale there are 3,000 fish. How many fish does he sell each year? |
| Q2 (sol) | 160 = 2⁵ × 5, so multiply… | Starts with a numeral. | Since 160 = 2⁵ × 5, multiply top and bottom by 5⁴: 13/160 = 8,125/100,000 = 0.08125, which has 5 digits after the point. |
| Q3 (sol) | …6 digits. 50 = 6 × 8 + 2, so… | Starts with a numeral. | The block has 6 digits. Since 50 = 6 × 8 + 2, after 8 full blocks the 50th digit is the 2nd digit of 428571, which is 2. |
| Q12 (sol) | 30k + 50b = 600 gives… | Starts with a numeral, and k and b are never defined. | For k kites and b balls, 30k + 50b = 600, so 3k + 5b = 60 and k must be a multiple of 5. With k, b ≥ 1: (5, 9), (10, 6), (15, 3) — 3 ways. |
| Q31 (sol) | 2.5 m = 250 cm = 5 units… | Starts with a numeral. | The distance 2.5 m = 250 cm = 5 units. Desk K is √(3² + 4²) = 5 units = 2.5 m from the origin. The others are √13, 2.5 and √50 units away. |
| Q37 (sol) | 79,868 → … | Starts with a numeral. | The number changes as 79,868 → 7 + 9 + 8 + 6 + 8 = 38 → 3 + 8 = 11 → 1 + 1 = 2. The number 2 has one digit, so 2 is printed. |
| Q39 (sol) | 63 → 62 → … 64 takes 6, … | Two sentences start with numerals. | Starting from 63: 63 → 62 → 31 → 30 → 15 → 14 → 7 → 6 → 3 → 2 → 1 takes 10 steps. The number 64 takes 6, 96 takes 7 and 100 takes 8 steps. |
| Q41 (sol) | These are m = 5, 7, … | Does not explain why m = 1 is left out, although distractor (D) 11 counts it. | …Since 1 is not in the list, these are m = 5, 7, 11, 13, 17, 19, 23, 25, 29 and 31 (31² = 961), so the list has 10 squares. |
| Q35 (distractor) | (D) Two triangles with one equal side and one equal angle are always congruent. | Weak distractor: the figure plainly contradicts it, and it is not a common misconception about what the figure shows. Optional fix, not in the JSON. | e.g. (D) Two angles and a side do not always fix a triangle. |
| Q34 (distractor) | (D) Day 33 | Implausible (it comes from 65 ÷ 2). Optional fix. | e.g. (D) Day 12 |

## Figures
| Q | Issue | Fix |
|---|---|---|
| Q25 | The "21 m" label sits under MC, next to the second tick mark, so it reads as MC = 21 m rather than BC = 21 m. The "13 m" label also touches AB. | Centre "21 m" under the whole of BC (or use a B–C dimension line below the base), and move "13 m" clear of AB. |
| Q35 | The labels "7 cm", "5 cm" (BC) and "5 cm" (BD) each overlap their segment lines. | Offset each label off its segment (for BC, put it inside the orange region or outside clearly). |
| Q26 | The x-axis has no title (category labels only). Minor. | Optionally add the axis title "Stall". |

All other figures check out: Q14 K(−3, 2), L(9, 7); Q15 tick marks and angle arcs; Q18 the non-reflex ∠AOB is marked and C is on the minor arc; Q20 x = ∠APC; Q22 and Q24 dimensions; Q26 B = 25/35/40%; Q27 table totals 200; Q42 chord AC ≈ radius, matching ∠AOC = 60°, with B on the shaded minor arc; Q44 the tree has 8 leaves and gives no values away.

## Syllabus / level / difficulty
- Chapter counts match the blueprint: Ch1 3, Ch3 3, Ch4 7, Ch5 7, Ch6 5, Ch8 5, Ch9 4, Ch10 6. There is no trigonometry anywhere.
- Section I labels give exactly 24 Easy and 16 Medium. An optional swap: Q38 (Easy, but it means generating terms and testing 4 rules, which is 2+ steps) ↔ Q3 (Medium, one remainder step). Not included in the JSON.
- Q44 pairing: the brief gives Ch8 + Ch10 as "tree diagram + proposition/converse". Q44 uses algorithm tracing instead (also Ch10, GM Ch11), so the pairing is acceptable but not the exact intended flavour.
- Q19 uses the "longest² > sum of other two squares ⇒ obtuse" test. This is fine as an extension of the converse of Baudhāyana–Pythagoras inside the circumcentre topic.
- Q34 relies on Σn (allowed at C9), not the general AP sum formula. OK.
- Q6 CI: 2 years, integer rate. Within the ceiling.
- Section II questions are genuinely multi-step and their pairings match the brief (Q41 Ch4 + Ch10, Q42 Ch5 + Ch6, Q43 Ch4 + Ch5, Q45 Ch3 + Ch9).

## Questions with no issues
Q4, Q5, Q7, Q8, Q10, Q11, Q13, Q14, Q15, Q17, Q18, Q19, Q20, Q22, Q23, Q24, Q26, Q27, Q29, Q30, Q42, Q43, Q44. (The others have only the solution-text, answer-cell or figure items above.)

## Topic list
- Q1 — Ch1 rationals/irrationals — which decimal is irrational
- Q2 — Ch1 terminating decimals — digits after the point of 13/160
- Q3 — Ch1 recurring decimals — 50th digit of 3/7
- Q4 — Ch3 successive % (decay as GP) — 10% fall twice = 19%
- Q5 — Ch3 weighted average of rates — average speed 72 km/h
- Q6 — Ch3 SI vs CI — best 2-year scheme
- Q7 — Ch4 polynomials — degree 3
- Q8 — Ch4 identities — 1,001² − 999²
- Q9 — Ch4 linear polynomial — find p(4)
- Q10 — Ch4 GP — non-term of 3, −6, 12, …
- Q11 — Ch4 factorising a quadratic — factor of 6x² + x − 15
- Q12 — Ch4 linear equation in 2 variables — positive whole-number solutions
- Q13 — Ch4 AP nth term — first negative term
- Q14 — Ch5 coordinates — distance on a grid
- Q15 — Ch5 midpoint theorem — corresponding angle
- Q16 — Ch5 quadrilaterals — parallelogram characterisation
- Q17 — Ch5 cyclic quadrilateral — opposite angles supplementary
- Q18 — Ch5 circles — angle at centre = 2 × inscribed (reflex case)
- Q19 — Ch5 circumcentre — obtuse triangle
- Q20 — Ch5 parallelogram + angle bisector — ∠APC
- Q21 — Ch6 area of a circle — equal-area rectangle
- Q22 — Ch6 cylinder volume
- Q23 — Ch6 arc length
- Q24 — Ch6 sphere/hemisphere — added surface area when cut
- Q25 — Ch6 Heron + median halves area
- Q26 — Ch8 100% stacked bar graph
- Q27 — Ch8 empirical probability from a table
- Q28 — Ch8 theoretical probability = 1/2
- Q29 — Ch8 probability with replacement (same colour)
- Q30 — Ch8 mean correction
- Q31 — Ch9 coordinates on a floor plan (scale)
- Q32 — Ch9 likelihood from data
- Q33 — Ch9 pair of linear equations — inconsistent
- Q34 — Ch9 AP context — day the fence is finished
- Q35 — Ch10 SSA counterexample
- Q36 — Ch10 special case vs generalisation
- Q37 — Ch10 algorithm tracing — repeated digit sum
- Q38 — Ch10 recursive → explicit rule
- Q39 — Ch10 algorithm step counting
- Q40 — Ch10 statement with a false converse
- Q41 — Ch4 + Ch10 AP algorithm — perfect squares in the list
- Q42 — Ch5 + Ch6 cyclic quad + segment perimeter
- Q43 — Ch4 + Ch5 lines/coordinates — circumcentre of a right triangle
- Q44 — Ch8 + Ch10 tree diagram + operation tracing
- Q45 — Ch3 + Ch9 50% growth with equal sales
