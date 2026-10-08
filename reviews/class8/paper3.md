# Review: AMO Level 1, Class 8, Practice Paper 3

## Verdict
This is a strong paper. All 45 keys are correct and each question has exactly one correct option. Blueprint counts are met (24 Easy + 16 Medium; chapter counts 3/3/5/5/5/5/3/5/6), and Section II pairings match the brief. The one must-fix item is Q20, which goes over the square-root ceiling (√2,704). Q9's answer cell also shows only a letter. The rest are small wording and house-rule fixes.

Key distribution: A 11 · B 11 · C 12 · D 11.

## Errors (must fix)
| Q | Problem | Fix |
|---|---|---|
| Q20 | Over the computational ceiling. AC = √2,704, but Class 8 allows square roots only of perfect squares ≤ 400. | Change the playground to 16 m × 12 m, so AC = √400 = 20 m, the usual walk is 28 m and the answer is 8 m. New options: (A) 20 m, (B) 28 m, (C) 8 m ✓, (D) 4 m (all common mistakes). Update the solution and answer cell (in fixes.json) and redraw the figure labels (see Figures). |
| Q9 | Answer cell shows only "(A)". | Add the option text "a 25% discount followed by a further 10% discount" (addrun in fixes.json). |

## Language & clarity
| Q | Current wording | Issue | Suggested rewrite (full text) |
|---|---|---|---|
| Q22 | "… How many plots are there? (1 hectare = 10,000 m².)" | Sentence starts with a numeral. | "A field of area 1.2 hectares is divided into equal square plots of side 20 m, with nothing left over. How many plots are there? (Use 1 hectare = 10,000 m².)" |
| Q25 | "All of its outside is painted except the face it stands on. What area is painted? (Use π = 22/7.)" | Layout: the closing ".)" wraps onto its own line under the fraction. | "… each is 10 cm tall, as in the picture. All of it is painted except the face it stands on. What area is painted? (Use π = 22/7.)" Re-check the line break after the edit. |
| Q26 | "… in the shape of a cylinder, 2 m across and 14 m deep." | "Across" is informal and vague. | "A well is dug in the shape of a cylinder, 2 m in diameter and 14 m deep. …" (rest unchanged) |
| Q27 | "the bar for 6–8 m should be ___ planes tall." | Mixes a count with a height. | "Complete the statement: the bar for 6–8 m should show ___ planes." |
| Q40 | "48, 4,848, 484,848, …" | The commas inside the numbers clash with the commas that separate the list items. | "A number is made by writing the block 48 again and again: 48, 4848, 484848, … (the block is written k times). …". Also change the solution's "484,848" to "484848". |
| Q42 | "on the top side of every square drawn in the step before" | From Step 1 on, the squares are tilted 45°, so two sides face upward and "top side" is ambiguous. | "At each step, on the outer side of every square drawn in the step before (the top side in Step 0), a right-angled isosceles triangle is drawn with that side as its longest side. …" |
| Q1, Q3, Q9, Q10, Q13, Q22, Q23, Q37, Q40 (solutions) | e.g. "13² = 169 …", "190 is 21 more …", "6³ = 216.", "10% then 25% leaves …", "36,000 ÷ …", "9x² + …", "1.2 hectares …", "2πrh = …", "18 is divisible …", "12k is a multiple …" | Solution sentences start with a numeral (house rule). | Prefix with "Here …", "The number …", "Taking 10% off and then 25% off …", "Curved surface area = …", "The field is …", "This is …" (exact text in fixes.json). |
| Q43 (solution) | "Then x² + 5x − 36 = (x + 9)(x − 4) = 0, so x = 4" | Solving a quadratic with the zero-product rule is a Class 10 method. | "Since 4 × 9 = 36, x = 4 and AB = 4 + 9 = 13 cm." |

## Figures
| Q | Issue | Fix |
|---|---|---|
| Q20 | Labels 48 m and 20 m go with the over-ceiling numbers. | Redraw as a 16 m × 12 m rectangle (4:3). Keep the right-angle squares at the corners and the dashed AC. |
| Q26 | The well is drawn as a tall rod standing above the ground. The "2 m" label has no diameter arrow. | Optional: add a diameter arrow across the top ellipse for "2 m". Draw the well as going into the ground, or caption it "earth taken out". |
| Q25 | "14 cm" is written on the dashed bottom-base radius, partly behind the solid. Readable. | Optional: move the label clear of the dashed ellipse. |

Checked and correct: Q17 (48° at A, 77° at E, ? at F). Q18 (rhombus sides measure equal, ∠Q ≈ 115°, tick marks on all four sides). Q19 (side ratio 9:12:15, right-angle square shown). Q21 (front columns 3, 3, 2). Q23. Q24 (right-angle mark at the base). Q27 (bars 4, 9, 7, 3 sit on minor gridlines; y-axis from 0; title and axis labels present). Q28 (140, 180, 160, 200, 220, 200). Q35 (only the three dashed dots are collinear). Q42 (Step 2 square sizes and positions match the construction). Q43 (right angles at C and D marked). Q45 (radii 42 m and 35 m from O).

## Syllabus / level / difficulty
- Blueprint met. Section I: Ch1 3, Ch2 3, Ch3 5, Ch4 5, Ch5 5, Ch6 5, Ch8 3, Ch9 5, Ch10 6. Easy 24: Q1, 2, 4, 5, 7, 8, 9, 12, 13, 14, 17, 18, 19, 22, 23, 24, 27, 28, 30, 31, 32, 35, 36, 37. Medium 16: the rest of Q1–Q40.
- Section II pairings match the brief: Q41 Ch4+Ch10, Q42 Ch5+Ch10, Q43 Ch4+Ch5, Q44 Ch3+Ch9, Q45 Ch6+Ch9.
- Q20 is over the square-root ceiling (fixed above). All other roots are within the ceiling: Q1 only estimates using 169 and 196, Q24 uses √36, and Q2 uses √2.
- Q35 is labelled Easy, but listing all 10 triples of 5 points is really 2 steps (borderline Medium). There is no clear Medium→Easy partner for a swap, so leave it as is.
- Q16 (fractions of a whole leading to a linear equation) sits under Ch4. That is acceptable as a word problem on linear equations.
- The decision log says Ch2 "retires at Class 8", but the locked blueprint still has Ch2: 3 Qs. The paper follows the blueprint. Nothing to change here; this is just flagged for the syllabus owner.
- Q43 is within scope once the solution uses the 4 × 9 product instead of the quadratic factorisation.

## Questions with no issues
Q2, Q4, Q5, Q6, Q7, Q8, Q11, Q12, Q14, Q15, Q16, Q17, Q18, Q19, Q21, Q24, Q28, Q29, Q30, Q31, Q32, Q33, Q34, Q35, Q36, Q38, Q39, Q41, Q44, Q45.

## Topic list
- Q1 — Ch1 squares & roots — whole number closest to √190
- Q2 — Ch1 properties of real numbers — distributive law with √2
- Q3 — Ch1 cubes — 6³ as a sum of 6 consecutive odd numbers
- Q4 — Ch2 standard form — mass of 1.5 × 10⁶ grains of 4 × 10⁻² g
- Q5 — Ch2 negative exponents — (□)⁻³ = 125/8
- Q6 — Ch2 laws of exponents — 9ˣ × 27 = 1/3
- Q7 — Ch3 simple interest — interest in the 4th year alone
- Q8 — Ch3 simple interest — extra interest when rate goes 8%→9%
- Q9 — Ch3 successive discounts — 10% then 25% equals 25% then 10%
- Q10 — Ch3 successive percentages — equal % rise, 25,000→36,000
- Q11 — Ch3 discounts — ₹100 coupon vs 10% discount order
- Q12 — Ch4 identities — (5p − □)² = 25p² − 30pq + 9q²
- Q13 — Ch4 identities — perimeter of square with area 9x² + 30x + 25
- Q14 — Ch4 linear equations — sandwiches over 3 days
- Q15 — Ch4 factorisation — common factor of x² − 25 and x² + 2x − 15
- Q16 — Ch4 linear equations — 1/3 storybooks, 1/4 science, 30 maths
- Q17 — Ch5 similarity — corresponding angles, find ∠F
- Q18 — Ch5 special quadrilaterals — rhombus, ∠QPR from ∠PQR = 116°
- Q19 — Ch5 Pythagoras — squares 81 and 144 on the legs
- Q20 — Ch5 Pythagoras — diagonal shortcut across a rectangle
- Q21 — Ch5 views of solids — front view of a stacked-cube plan
- Q22 — Ch6 unit conversions — hectares into 20 m square plots
- Q23 — Ch6 cylinder — diameter from curved surface area
- Q24 — Ch6 cone — height from slant height and diameter
- Q25 — Ch6 composite solids — painted area of a two-cylinder stand
- Q26 — Ch6 cylinder/cuboid — earth from a well spread as a platform
- Q27 — Ch8 histograms — missing class frequency
- Q28 — Ch8 line graphs — count of day-on-day increases
- Q29 — Ch8 central tendency — combined mean of two sections
- Q30 — Ch9 commercial maths — price before 18% GST
- Q31 — Ch9 profit/loss — buy at 25% off marked price, sell at marked price
- Q32 — Ch9 simple interest application — equal monthly repayments
- Q33 — Ch9 profit/loss — cost falls 20%, selling price unchanged
- Q34 — Ch9 simple interest application — two deposits a year apart
- Q35 — Ch10 casework — triangles from 5 points with 3 collinear
- Q36 — Ch10 parity — least number of even addends
- Q37 — Ch10 divisibility — counterexample to "6 and 9 ⇒ 54"
- Q38 — Ch10 cryptarithm — AA + BB + CC = ABC
- Q39 — Ch10 casework — distinct totals of three spins of 1, 3, 7
- Q40 — Ch10 divisibility — repeated block 48 divisible by 9
- Q41 — Ch4 + Ch10 — 12a + 7c = 200 with a > c
- Q42 — Ch5 + Ch10 — Pythagoras tree fractal, total area Steps 0–4
- Q43 — Ch4 + Ch5 — altitude to hypotenuse, similar triangles, area
- Q44 — Ch3 + Ch9 — new profit % after cost and price changes
- Q45 — Ch6 + Ch9 — ring-shaped track area, discount, profit
