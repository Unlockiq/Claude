# Review — AMO Level 1, Class 9, Practice Paper 5

**Verdict:** Strong paper. All 45 keys verified by independent solution; every question has exactly one correct option; no trigonometry or other out-of-syllabus content except one borderline item (Q39 needs an invariant argument). Fixes are mainly small: two letter-only answer cells, one undefined-symbol stem (Q38), sentences starting with a numeral in solutions, one weak distractor and one crowded figure.

**Key distribution:** A 11 · B 11 · C 11 · D 12 (45). Blueprint per chapter matches (3/3/7/7/5/5/4/6 = 40). Section I labels: 24 Easy + 16 Medium ✓. Section II pairings Q41 Ch4+Ch10, Q42 Ch5+Ch6, Q43 Ch4+Ch5, Q44 Ch8+Ch10, Q45 Ch3+Ch9 ✓.

## Errors (must fix)

| Q | Problem | Fix |
|---|---|---|
| Q1 | Solutions table answer cell shows only "(C)". | Add option text "0.67777…". |
| Q27 | Solutions table answer cell shows only "(D)". | Add option text "The mean goes up by 2 and the median does NOT change." |
| Q38 | The formula √((s − a)(s − b)(s − c)(s − d)) is given but a, b, c, d are never defined, so information is missing. | Add "where a, b, c, d are the sides and s is half the perimeter". (Key A 49 cm² is correct: 169 − 120.) |
| Q39 | Syllabus: "least number of moves" can only be justified by the inversion-count invariant (the solution uses it). Invariants were removed from C9 (Decision D15). | Recast it as tracing an algorithm (bubble sort): "Lata sorts the list 5, 1, 4, 2, 3 into increasing order. She goes along the list from left to right, swapping any two neighbours in the wrong order, and repeats this until no swap is needed. How many swaps does she make?" Answer stays (B) 6 (passes: 4 + 2 + 0). Update the solution to match. |

No wrong keys, no wrong worked solutions, no question with zero or several correct options, nothing over the computational ceiling (Q45 compound growth: 2 years, integer rates ✓).

## Language & clarity

| Q | Current wording | Issue | Suggested rewrite (full text) |
|---|---|---|---|
| Q8 (soln) | "14d = 59 − 3 = 56, so d = 4. …" | Sentence starts with a numeral | "The common difference d satisfies 14d = 59 − 3 = 56, so d = 4. The 8th term is 3 + 7 × 4 = 31 (it is also the average of the 1st and 15th terms, since 8 is halfway between 1 and 15)." |
| Q21 (soln) | "2πr = 8.8 gives r = …" | Starts with a numeral | "The rim is the circumference, so 2πr = 8.8 and r = 8.8 × 7 ÷ 44 = 1.4 m. Area = 22/7 × 1.4 × 1.4 = 6.16 m²." |
| Q22 (soln) | "4πr² is 616 cm² for r = 7 …" | Starts with a numeral | "The surface area 4πr² is 616 cm² for r = 7 and 2,464 cm² for r = 14 (four times as much). The increase is 2,464 − 616 = 1,848 cm²." |
| Q25 | "Varsha cuts a triangle with sides 25 cm, 25 cm and 14 cm, as shown." | "cuts a triangle" is vague (cuts it into pieces?) | "Varsha cuts out a paper triangle with sides 25 cm, 25 cm and 14 cm, as shown. She wants a DIFFERENT triangle that also has two 25 cm sides and exactly the same area. How long must its third side be?" |
| Q25 (soln) | "… The only other length giving 168 cm² is 48 cm." | Uniqueness asserted, not shown | "Heron: s = 32, area = √(32 × 7 × 7 × 18) = 168 cm². The height on the 14 cm side is 24 cm, so the triangle is two 7-24-25 right triangles. Swapping their legs (half-base 24 cm, height 7 cm) gives the same area, so the third side is 48 cm. Check: s = 49, area = √(49 × 24 × 24 × 1) = 168 cm²." |
| Q26 (soln) | "0.3 × 60 = 18, so …" | Starts with a numeral | "Test A gives 0.3 × 60 = 18, so 0.7 × B = 74 − 18 = 56 and B = 56 ÷ 0.7 = 80." |
| Q31 (soln) | "30 + 25(n − 1) = 230 gives …" | Starts with a numeral | "Rung n is 30 + 25(n − 1) cm high. Solving 30 + 25(n − 1) = 230 gives n − 1 = 8, so n = 9." |
| Q34 (soln) | "20 − 2k = 3k gives k = 4 …" | Starts with a numeral | "After k intervals of 5 seconds, P is at 20 − 2k and Q is at 3k. Solving 20 − 2k = 3k gives k = 4, so they pass at floor 3 × 4 = 12 (after 20 seconds)." |
| Q41 (soln) | "17 + 28(k − 1) ≤ 500 gives k ≤ 18.25 …" | Starts with a numeral | "… with d = 28. Then 17 + 28(k − 1) ≤ 500 gives k ≤ 18.25, so 18 numbers." |
| Q45 | Option (C) ₹32 | Distractor does not come from a likely mistake | Use ₹30 (the Year 2 lily price, a likely slip), alongside ₹36 (Year 3). |
| Q41 | "Put n = 1." … "print n." | Variable n is set upright here; elsewhere variables are italic (minor typography) | Italicise n (formatting only; not in JSON). |

## Figures

| Q | Issue | Fix |
|---|---|---|
| Q38 | Labels collide with lines: "10 cm" crosses the lower edge and the horizontal diagonal, "24 cm" sits on the upper-left edge, and "13 cm" touches the upper-right edge. "24 cm" is on the left half only, so it can be read as a half-diagonal. | Redraw with clear offsets. Put "24 cm" centred along the full horizontal diagonal (or use a dimension arrow) and "10 cm" beside the vertical diagonal, clear of the edges. |
| Q30 | In the table, the "x" cell is left-aligned while the numbers are right-aligned. | Centre or right-align "x" to match (cosmetic). |

The other figures were checked and are correct: Q16 (labels at AO/OC), Q17 (equal-side ticks and bisector arcs; right angle at D correctly NOT marked because it is to be deduced), Q18 (AB = AD ticks, 104° at C, x at B), Q19 (O, 30°, 7 cm), Q23, Q24 (right angle marked in the cone), Q25, Q42 (cross-section consistent with r = 10: 4 cm sag, 16 cm chord) and Q44 (Step 2 has 16 segments, 6 horizontal).

## Syllabus / level / difficulty

- No trigonometry anywhere ✓ (Decision D18 / v5.9). All topics are in GM Class 9 or earlier: recurring decimals and irrationals (Q1–3), SI/CI as AP/GP and weighted rates (Q4–6), identities, AP/GP and rational expressions (Q7–13), chords, coordinates, circle theorems and midpoint theorem (Q14–20), circle, sphere, sector-to-cone and Heron (Q21–25), weighted average, mean/median/mode and theoretical probability (Q26–30), linear models (Q31–34), propositions/converse, algorithms, proof by contradiction, special case vs generalisation and sieve (Q35–40).
- Q39: as written it is borderline (minimum moves = inversion-count invariant, removed from C9 per D15). The recast as bubble-sort tracing is in the JSON.
- Q41's Section II pairing (Ch4 AP + Ch10 algorithm tracing) fits. Q44 pairs Ch8 probability with Ch10 fractal counting instead of the brief's suggested "tree diagram + converse". Fractal counting is listed under Ch10 C9 (GM Ch8), so this is acceptable.
- Difficulty: Q38 is labelled Easy but needs s, the formula, the true area and the difference, so it is closer to Medium. If relabelling, swap it with Q40 (Medium → Easy; a single sieve-tracing step) to keep 24 E + 16 M. This is optional and not in the JSON.
- Section I questions each stay within one chapter ✓. No pure aptitude items.

## Questions with no issues

Q2, Q3, Q4, Q5, Q6, Q7, Q9, Q10, Q11, Q12, Q13, Q14, Q15, Q16, Q17, Q18, Q19, Q20, Q23, Q24, Q28, Q29, Q32, Q33, Q35, Q36, Q37, Q40, Q42, Q43, Q44

## Topic list

- Q1 — Ch1 Number System — compare terminating/recurring decimals
- Q2 — Ch1 — which square root is irrational (√0.4)
- Q3 — Ch1 — recurring decimal 0.31818… → 7/22
- Q4 — Ch3 — simple interest as constant growth (AP), find principal
- Q5 — Ch3 — 4% compound population growth, increase in Year 2
- Q6 — Ch3 — weighted average of interest rates
- Q7 — Ch4 Algebra — complete the square with identity (3x + 4)²
- Q8 — Ch4 — AP nth term
- Q9 — Ch4 — difference-of-squares identity
- Q10 — Ch4 — evaluate polynomial, find coefficient
- Q11 — Ch4 — rational expression, value excluded by cancelling
- Q12 — Ch4 — factorising quadratics, count of k
- Q13 — Ch4 — AP vs GP 5th terms
- Q14 — Ch5 Geometry — chord length vs distance from centre
- Q15 — Ch5 — distance formula
- Q16 — Ch5 — parallelogram diagonals bisect
- Q17 — Ch5 — isosceles triangle, congruence + Pythagoras
- Q18 — Ch5 — cyclic quadrilateral + isosceles triangle
- Q19 — Ch5 — angle at centre = 2 × angle at circumference
- Q20 — Ch5 — midpoint theorem with coordinates
- Q21 — Ch6 Mensuration — circle area from circumference
- Q22 — Ch6 — sphere surface area increase
- Q23 — Ch6 — perimeter of a semicircle
- Q24 — Ch6 — sector rolled into a cone, height
- Q25 — Ch6 — Heron's formula, two isosceles triangles with equal area
- Q26 — Ch8 Data — weighted average of test marks
- Q27 — Ch8 — effect of a changed value on mean and median
- Q28 — Ch8 — theoretical probability (8-sided die)
- Q29 — Ch8 — probability change after adding items
- Q30 — Ch8 — mode = mean, find missing value
- Q31 — Ch9 Applied — AP context (ladder rungs)
- Q32 — Ch9 — linear model from a table
- Q33 — Ch9 — linear model, find the start time
- Q34 — Ch9 — two linear motions meet (lifts)
- Q35 — Ch10 Reasoning — statement and converse (multiples of 100)
- Q36 — Ch10 — tracing an algorithm (halving–doubling multiplication)
- Q37 — Ch10 — proof by contradiction (no greatest rational < 2)
- Q38 — Ch10 — special case vs generalisation (Brahmagupta on a rhombus)
- Q39 — Ch10 — adjacent-swap sorting (recast as bubble-sort tracing)
- Q40 — Ch10 — tracing the sieve, count of crossings in step 2
- Q41 — SII Ch4 + Ch10 — algorithm with two remainder conditions → AP count
- Q42 — SII Ch5 + Ch6 — ball in a hole: chord theorem → sphere surface area
- Q43 — SII Ch4 + Ch5 — parallelogram vertices with line and axis constraints
- Q44 — SII Ch8 + Ch10 — Koch curve segment count → probability
- Q45 — SII Ch3 + Ch9 — compound price rise, two unknowns (pair of equations)
