# Review — AMO Level 1, Class 8, Practice Paper 2

**Verdict:** A strong paper. I solved all 45 questions myself, and every key is correct with exactly one correct option. The blueprint counts (3/3/5/5/5/5/3/5/6) and the Section I Easy/Medium split (24/16) are both met, and the Section II pairings match the brief. No question is broken. The fixes needed are three answer cells that show only a letter, a few solutions that start with a numeral or skip a step, one stem that starts with an equation, and one stem that refers to a pie chart that is not drawn.

**Key letter distribution:** A 11 · B 11 · C 12 · D 11 (balanced).

## Errors (must fix)
| Q | Problem | Fix |
|---|---|---|
| Q7 | The answer cell shows only "(C)". | Add the option text "₹2,000 at 7.5% a year for 4 years" (in the JSON as addrun). |
| Q18 | The answer cell shows only "(A)". | Add "One of its angles is 90°." (addrun). |
| Q19 | The answer cell shows only "(B)". | Add "a prism whose base has 10 sides" (addrun). |
| Q38 | The solution says "the product is even, so the first digit is 2 and the last digit is 8" but never explains why D = 8. | "…so A is 1 or 2. A is the last digit of an even product, so A = 2. Then 4 × D ends in 2 and D ≥ 8, so D = 8. Checking gives 2,178 × 4 = 8,712." |

## Language & clarity
| Q | Current wording | Issue | Suggested rewrite (full text) |
|---|---|---|---|
| Q5 | "8⁻² = 2ˣ. What is the value of x?" | The stem starts with a numeral (house rule). The equation is an equation object, so this needs a **manual** edit in Word. It is not in the JSON. | "It is given that 8⁻² = 2ˣ. What is the value of x?" |
| Q5 (sol.) | "8 = 2³, so 8⁻² = …" | Starts with a numeral. | "Since 8 = 2³, 8⁻² = (2³)⁻² = 2⁻⁶, because 3 × (−2) = −6. Check: 8⁻² = 1/64 = 2⁻⁶." |
| Q23 | "How many times the volume of A is the volume of B?" | The word order is awkward and reads like a statement. | "Cylinder A has radius r and height h. Cylinder B has radius 2r and height h ÷ 2, as in the picture. The volume of B is how many times the volume of A?" |
| Q27 | "The data is shown in a pie chart. Which subject has a sector of 90°?" | No pie chart is drawn, so "is shown" is misleading. | "The table shows the favourite subjects of 480 students. The data is to be shown in a pie chart. Which subject will have a sector of 90°?" |
| Q27 (sol.) | "90° is one quarter of 360°, …" | Starts with a numeral. | "An angle of 90° is one quarter of 360°, so the subject must have one quarter of 480 = 120 students: Maths (120/480 × 360° = 90°)." |
| Q19 (sol.) | "The others have 45, 20 and 24 edges." | The list is not in option order (A = 24, C = 20, D = 45). | "…The others have 24, 20 and 45 edges." |
| Q40 (sol.) | "36 = 4 × 9, … 5,832: last two digits 32 are…" | Two sentences start with a numeral, and "5,832: …" is a fragment. | "Here 36 = 4 × 9, and 4 and 9 have no common factor. For 5,832, the last two digits 32 are divisible by 4, and 5 + 8 + 3 + 2 = 18 is divisible by 9. Each of the others fails one test." |
| Q41 (sol.) | "10a + b = a + b + ab + 12 gives …" | Starts with a numeral and does not explain why 1 × 12 and 12 × 1 are excluded. | "Let the number be 10a + b. Then 10a + b = a + b + ab + 12 gives a(9 − b) = 12. As 9 − b ≤ 9, a × (9 − b) can be 2 × 6, 3 × 4, 4 × 3 or 6 × 2, giving 23, 35, 46 and 67 — 4 numbers." |
| Q15 | "Which of these can NOT be the value of k?" | Optional: "cannot" is standard English. The capitals do match the emphasis style of Q12, so I made no change. | "Which of these cannot be the value of k?" |

## Figures
| Q | Issue | Fix |
|---|---|---|
| Q43 | The rectangle is drawn almost exactly to the answer's proportions (MF ≈ 2 cm, MD ≈ 8 cm against the labelled 6 cm and 12 cm), so a student could estimate the answer by measuring. This is low priority because the disclaimer covers it. | Optional: redraw with a less telling rectangle (for example MF about 0.45 × MN). |
| Q23 | Cylinder B's radius is drawn about 1.7 times A's, not 2 times. This is covered by the "not to scale" line. | Optional: none needed. |

I checked all the other figures and found them correct:
- **Q17:** the right angle at D is marked, AB and AC have tick marks, and h is labelled.
- **Q20:** the triangles are similar at scale 3 (pixel ratios match), and the vertex correspondence is consistent.
- **Q21:** both base right angles are marked, the pole heights are in proportion, and "?" marks the unknown.
- **Q24, Q25, Q26, Q45:** all labels match the stem.
- **Q28:** the line graph values are 18, 8, 14, 6, 4, 10 (total 60). The y-axis starts at 0, both axes are labelled and there is a title.
- **Q29:** the histogram frequencies are 4, 10, 14, 8, 6, with hatching for greyscale. None of (15, 10), (17.5, 14) or (20, 10) lies on the polygon, so (17.5, 10) is the only answer.
- **Q35:** Step 2 correctly shows 8 small holes around the centre hole.
- **Q42:** the grid has 5 × 5 dots with a 1 cm scale.
- **Q43:** the right angle at M is marked.

## Syllabus / level / difficulty
- **Blueprint:** Ch1 3, Ch2 3, Ch3 5, Ch4 5, Ch5 5, Ch6 5, Ch8 3, Ch9 5, Ch10 6, which is 40 in total. Section I has 24 Easy and 16 Medium, so both blueprint counts are met.
- **Section II pairings match the brief:** Q41 Ch4+Ch10, Q42 Ch5+Ch10, Q43 Ch4+Ch5 (similarity), Q44 Ch3+Ch9 (successive discounts), Q45 Ch6+Ch9. Q45 uses a cylinder where the brief suggests a cone, which is acceptable.
- **Q42** pairs Pythagoras with counting rather than the brief's suggested "similarity + parity". That is still a valid Ch5 + Ch10 pairing.
- **Q43** solves x² − 6x + 8 = 0 by basic factorization, which is in the C8 Ch4 syllabus and acceptable in Section II.
- **Computational ceiling:** all within limits. The square roots are 2.89 (from 289), 0.64, 169 and 225; the cube roots are 0.729 and 0.343; successive percentages are all integers; the largest number is 176,000.
- **Optional relabel swap:** Q24 (Easy) needs a mm→cm conversion, halving the diameter and the ⅓πr²h formula with 2.1², so it is closer to Medium. Q3 (Medium) is four single-step evaluations, so it is closer to Easy. Swapping the two labels keeps the 24/16 split.
- **Q17** (Easy) has 2 short steps but is a standard Pythagoras exercise, so Easy is acceptable.
- **No pure aptitude items.** Q37 (necklace) is a divisibility/periodicity question, not an aptitude puzzle.
- **Note on the brief:** the decision log says "Ch2 retires at Class 8", but the locked blueprint still lists Ch2 with 3 questions. The paper follows the blueprint.

## Questions with no issues
Q1, Q2, Q3, Q4, Q6, Q8, Q9, Q10, Q11, Q12, Q13, Q14, Q16, Q17, Q20, Q21, Q22, Q24, Q25, Q26, Q28, Q29, Q30, Q31, Q32, Q33, Q34, Q35, Q36, Q37, Q39, Q42, Q44, Q45

## Topic list
- Q1 — Ch1 real numbers — which expression is rational (√3 × √12 = 6)
- Q2 — Ch1 square roots — side of a square mat with area 2.89 m²
- Q3 — Ch1 squares/cubes/roots — greatest of 0.9², √0.64, ∛0.729, ∛0.343
- Q4 — Ch2 negative exponents — which power is negative
- Q5 — Ch2 laws of exponents — 8⁻² = 2ˣ
- Q6 — Ch2 standard form — drops of 5 × 10⁻² mL in a 1.5 × 10³ mL bottle
- Q7 — Ch3 simple interest — which deposit earns ₹600
- Q8 — Ch3 simple interest — rate from ₹480 earned in 9 months
- Q9 — Ch3 successive percentages — 25% of 60% of 400
- Q10 — Ch3 successive discounts — lowest final price
- Q11 — Ch3 successive percentages — area change (+20%, −10%)
- Q12 — Ch4 identities — which trinomial is not a perfect square
- Q13 — Ch4 a² − b² — find x − y
- Q14 — Ch4 linear equation word problem — ribbon pieces
- Q15 — Ch4 factorization — impossible k in x² + kx + 24
- Q16 — Ch4 linear equation word problem — passengers on a train coach
- Q17 — Ch5 Pythagoras — height of an isosceles triangle
- Q18 — Ch5 special quadrilaterals — when a parallelogram is a rectangle
- Q19 — Ch5 solids — prism or pyramid with 30 edges
- Q20 — Ch5 similarity — longest side from the perimeter ratio
- Q21 — Ch5 Pythagoras — distance between the tops of two poles
- Q22 — Ch6 cone volume — compare r²h
- Q23 — Ch6 cylinder — volume ratio
- Q24 — Ch6 cone volume with unit conversion — wax cone
- Q25 — Ch6 unit conversion — jugs to fill a cuboid tank
- Q26 — Ch6 composite solid — cone height of a rocket
- Q27 — Ch8 pie charts — which subject has a 90° sector
- Q28 — Ch8 line graph / mean — students absent
- Q29 — Ch8 histogram / frequency polygon — point on the polygon
- Q30 — Ch9 profit percent — compare four items
- Q31 — Ch9 simple interest application — monthly interest
- Q32 — Ch9 profit/loss — selling price from profit = 15% of the cost price
- Q33 — Ch9 mixed commercial problem — mixture of oranges
- Q34 — Ch9 profit/loss — profit is 1/5 of the selling price
- Q35 — Ch10 fractals — Sierpiński carpet side at Step 3
- Q36 — Ch10 casework — two-digit numbers whose digits differ by 7
- Q37 — Ch10 divisibility — repeating bead necklace
- Q38 — Ch10 cryptarithm — ABCD × 4 = DCBA
- Q39 — Ch10 casework — shoe pairs on 3 shelves (1–5 each)
- Q40 — Ch10 divisibility — divisible by 36
- Q41 — Section II Ch4 + Ch10 — digit sum + product + 12 = number
- Q42 — Section II Ch5 + Ch10 — tilted squares of area 5 on a dot grid
- Q43 — Section II Ch4 + Ch5 — rectangle inscribed in a right triangle
- Q44 — Section II Ch3 + Ch9 — successive discounts plus a free desk, dealer's profit percent
- Q45 — Section II Ch6 + Ch9 — painting the curved surfaces of posts, profit percent
