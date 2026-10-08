# Review — AMO Level 1, Class 10, Practice Paper 1

**Verdict:** The paper is sound. All 45 keys and worked solutions are correct, every figure matches its stem, the blueprint is exact (3/5/6/5/5/3/3/5/5 plus 5 Section II, 24 Easy + 16 Medium) and all Section II pairings match the brief. The only must-fix is factual. Q31 uses a bakery bill at 18% GST, but cakes and biscuits have been taxed at 5% since Sept 2025. The other fixes are small wording and layout changes.

**Key distribution:** A 11 · B 11 · C 12 · D 11 (balanced).

## Errors (must fix)

| Q | Problem | Fix |
|---|---|---|
| Q31 | The fact is out of date. A bakery bill charges CGST 9% + SGST 9% (18%) on a cake and cookies, but under GST 2.0 (from Sept 2025) cakes, pastries and biscuits are taxed at 5%. The 18% slab still exists, so the maths is right but the context is wrong. | Keep 18% and change the goods. Table title: "Bill from an electronics shop (sale within the state)". "Cake" → "Headphones", "Box of cookies" → "Charging cable". In the stem, "a bakery bill" → "a shop bill". Prices, options, key (C) ₹1,416 and the solution stay the same. The table is Word text, so this is in the JSON. |

There are no wrong keys, no question with two or zero correct options, and no solution errors. Each key was re-derived independently. Q40 was checked with a grid count (35 − 3 × 6 = 17), and Q28 with the ogive points (0,0), (10,2), (20,6), (30,14), (40,26), (50,36), (60,40), which give a median of 35.

## Language & clarity

| Q | Current wording | Issue | Suggested rewrite (full text) |
|---|---|---|---|
| Q15 | "In each triangle ABC below, D lies on AB…" | The figure is **above** the stem (page 4). | "In each triangle ABC in the figure, D lies on AB and E lies on AC, and the lengths are in cm. In which picture is DE parallel to BC?" |
| Q24 | "A rainfall of 2 cm falls on it, …" | Redundant ("rainfall … falls") and unclear. | "A flat roof measures 22 m by 20 m. Rain falls on it to a depth of 2 cm, and all the water drains into an empty cylindrical rainwater tank of radius 1 m. How high does the water rise in the tank? (Use π = 22/7.)" |
| Q26 | "θ is an acute angle and cos θ = 1/2." | The sentence starts with a symbol (house rule). | "The angle θ is acute and cos θ = 1/2. What is the value of sin θ × tan θ?" |
| Q18 | "…AB = 12 / cm…" (line break) | The number and its unit are split across lines. | Same text with non-breaking spaces in "12 cm", "8 cm", "15 cm". |
| Q19 | "…AB = / 8 cm…" (line break) | "AB =" is split from its value. | Same text with non-breaking spaces in "∠B = 90°", "AB = 8 cm", "BC = 15 cm". |
| Q20 | "(Use π = / 22/7.)" | The break falls inside the formula. | Non-breaking spaces in "π = 22/7" and "14 m". |
| Q21 | "slant height is 12 / cm" | The number and its unit are split. | Non-breaking spaces in "10.5 cm", "7 cm", "12 cm", "π = 22/7". |
| Q2 sol | "40 = 2³ × 5, so … 13/16 has 4 places, …" | Sentences start with numerals. | "Since 40 = 2³ × 5, 21/40 ends after 3 places: 21/40 = 0.525. Also, 13/16 has 4 places, 27/150 = 9/50 has 2 places and 7/24 does not end." |
| Q3 sol | "360 = 2³ × 3² × 5. …" | The sentence starts with a numeral. | "Here 360 = 2³ × 3² × 5. …" |
| Q5 sol | "Ratio 300,000 : 360,000 = 5 : 6." | This is a fragment. | "The ratio is 300,000 : 360,000 = 5 : 6." |
| Q36 sol | "n points give n(n − 1)/2 lines. 8 × 7 ÷ 2 = 28, …" | Sentences start with a variable or numeral. | "With n points there are n(n − 1)/2 lines. Since 8 × 7 ÷ 2 = 28, there are 8 points." |
| Q43 sol | "x² + 7x − 144 = 0 = (x + 16)(x − 9)" | The equation chain is awkward. | "x² + 7x − 144 = (x + 16)(x − 9) = 0" |
| Q45 sol | "2πr = 132 gives … 36 saplings could be 2 in every sector…" | Sentences start with numerals. | "Here 2πr = 132 gives … With 36 saplings there could be 2 in every sector, so 2 × 18 + 1 = 37 saplings are needed." |

All of the above are in `paper1_fixes.json` (17 items, each `old` verified unique in runs1.txt).

## Figures

| Q | Issue | Fix |
|---|---|---|
| Q32 | The cost/income line graph has no title. The visual standard asks for a title on graphs. | Add a title, e.g. "Cost and sales income of a bag workshop". |
| Q29 | Each spinner's pointer points exactly at the boundary between parts 4 and 3, which looks like an undecided spin. | Turn the pointer to the middle of one part, or remove the pointer. |
| Q9 | The origin label "O" sits under the axis next to the marked zero at x = −1 and duplicates the "0" tick label, so the spot is crowded. | Move "O" up and to the right of the origin, or drop it. |
| Answer sheet (p.13) | In rows 10–15 the bubbles are shifted right compared with rows 1–9, because the two-digit numbers push them over. | Pad the numbers to a fixed width so the bubble columns line up. |

All other figures were checked and are fine:
- Q1: the cut pattern is 24, 24 | 18 | 6, 6, 6.
- Q5: Kartik's bar covers months 5–12 (8 months).
- Q12: the rows hold 4, 7, 10, 13 marbles.
- Q15: picture B has 4:6 = 6:9.
- Q16: R is at (−2, 5) and S at (6, −3).
- Q17, Q19, Q25, Q42, Q43: right angles are shown with squares.
- Q27: the angles of depression are drawn from the horizontal.
- Q28: the grid lines are every 5 cm and every 2 plants.
- Q40: the closed crossing is at (2, 1).

## Syllabus / level / difficulty

- Blueprint is exact: Ch1 Q1–3, Ch3 Q4–8, Ch4 Q9–14, Ch5 Q15–19, Ch6 Q20–24, Ch7 Q25–27, Ch8 Q28–30, Ch9 Q31–35 and Ch10 Q36–40. Section II pairings match the brief: Q41 Ch4+Ch10, Q42 Ch5+Ch7, Q43 Ch4+Ch5, Q44 Ch3+Ch9, Q45 Ch6+Ch10.
- There are exactly 24 Easy and 16 Medium in Section I, and the labels look reasonable. No relabel swaps are needed.
- Every topic is inside the re-based Class 10 (CBSE Grade-10) scope:
  - Q29 is a compound two-spinner event, which is the C10 probability scope.
  - Q13 uses the discriminant.
  - Q12 uses the AP sum. No question relies only on the AP nth term (now C9).
  - Q17 and Q19 use tangent lengths.
  - Q6 and Q7 use half-yearly compound interest for 1 year, within the ceiling.
  - No complex numbers, straight-line equations or P&C formulas appear.
- The computational ceiling is respected. All roots and coordinates are integers and only standard trig angles are used.
- D5 guardrail ("harder than SOF/Silverzone") is a soft concern. Q32 only reads two values off a graph, and Q4, Q20–Q22 and Q33 are direct textbook one-steppers. They are acceptable as Easy items, but if any item is replaced, Q32 is the weakest; a break-even question would suit better (for example, "How many bags must be sold to break even?" gives 100).
- Q36–Q40 are combinatorics, extremal, pigeonhole, invariant and lattice-path problems. None is pure aptitude reasoning.

## Questions with no issues

Q1, Q3, Q4, Q5, Q6, Q7, Q8, Q10, Q11, Q12, Q13, Q14, Q16, Q17, Q22, Q23, Q25, Q27, Q28, Q30, Q33, Q34, Q35, Q37, Q38, Q39, Q40, Q41, Q42, Q44.

Q2, Q3, Q5, Q36, Q43 and Q45 have only small solution-wording fixes; their stems are fine.

## Topic list

- Q1 — Ch1 Real numbers — Euclid's algorithm as square cuts (HCF 66, 24)
- Q2 — Ch1 Real numbers — terminating decimal with exactly 3 places
- Q3 — Ch1 Real numbers / FTA — smallest k so that 360k is a cube
- Q4 — Ch3 Partnership — equal capital, different times
- Q5 — Ch3 Partnership — capital × months from a bar chart
- Q6 — Ch3 Compound interest — effective annual rate, half-yearly
- Q7 — Ch3 Compound interest — passbook table, 2nd half-year balance
- Q8 — Ch3 Partnership — finding when a partner joined
- Q9 — Ch4 Polynomials — zeroes from a graph give b
- Q10 — Ch4 Linear pair — condition for no solution
- Q11 — Ch4 Polynomials — division algorithm, p(2)
- Q12 — Ch4 AP — sum of 12 terms from a marble pattern
- Q13 — Ch4 Quadratics — discriminant < 0, counting integer k
- Q14 — Ch4 Polynomials — zeroes differ by 4, find k
- Q15 — Ch5 Triangles — converse of BPT, pick the picture
- Q16 — Ch5 Coordinate — section formula 3:1
- Q17 — Ch5 Circles — equal tangents
- Q18 — Ch5 Triangles — similarity in a trapezium, AO
- Q19 — Ch5 Circles/tangents — inradius of a 8-15-17 triangle
- Q20 — Ch6 Circles — arc length of a 135° sector
- Q21 — Ch6 Frustum — curved surface area
- Q22 — Ch6 Combined solids — cylinder + cone volume
- Q23 — Ch6 Segments — leaf area in a square
- Q24 — Ch6 Volume conservation — roof rain into a tank
- Q25 — Ch7 Trig ratios — cosec θ from a 20-21-29 triangle
- Q26 — Ch7 Specific angles — sin θ tan θ for cos θ = 1/2
- Q27 — Ch7 Heights & distances — tree height from two depressions
- Q28 — Ch8 Statistics — median from a less-than ogive
- Q29 — Ch8 Probability — two spinners, sum ≥ 3 (complement)
- Q30 — Ch8 Statistics — grouped mode
- Q31 — Ch9 Financial — CGST + SGST bill
- Q32 — Ch9 Break-even — profit read from cost/income graph
- Q33 — Ch9 Boats & streams — round-trip time
- Q34 — Ch9 EMI / reducing balance — total interest from a table
- Q35 — Ch9 Time & work — finishing a job alone
- Q36 — Ch10 Combinatorics — points from the number of chords
- Q37 — Ch10 Extremal — minimise the largest of 7 numbers summing to 50
- Q38 — Ch10 Pigeonhole — 2³ colour patterns
- Q39 — Ch10 Invariant — remainder mod 3
- Q40 — Ch10 Combinatorics — lattice paths avoiding a blocked crossing
- Q41 — Ch4+Ch10 — AP sum + pigeonhole (stamps on distinct pages)
- Q42 — Ch5+Ch7 — two discs tangent in a 60° corner
- Q43 — Ch4+Ch5 — altitude to the hypotenuse with a quadratic
- Q44 — Ch3+Ch9 — break-even profit shared by capital × time
- Q45 — Ch6+Ch10 — sector areas + generalised pigeonhole
