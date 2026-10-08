# Review — AMO Level 1, Class 10, Practice Paper 4

**Verdict:** Mathematically sound. I solved all 45 questions on my own. Every key is correct, every question has exactly one correct option, and every worked solution is right. Q40 was also checked by a full state search: (12, 15, 17) can reach (0, 0, 44) and no other single-colour state. The blueprint is met exactly: the Section I chapter counts are 3/5/6/5/5/3/3/5/5, there are 24 Easy and 16 Medium, and all Section II pairings match the brief. What remains to fix is minor: missing right-angle marks in 3 figures (Q16, Q27, Q42), 2 cluttered figure labels, one stem that starts with a numeral (Q36), and a few solution wordings.

**Key distribution:** A 12 · B 11 · C 11 · D 11, which is balanced. The longest run of one letter is 2 (31–32 D, 35–36 A).

## Errors (must fix)
No wrong keys. No question has zero or several correct options. No question is over the computational ceiling. Q4 is quarterly compounding for only 6 months, and Q8 is half-yearly for 1 year, so both are within the CI cap.

| Q | Problem | Fix |
|---|---|---|
| — | None found | — |

## Language & clarity
| Q | Current wording | Issue | Suggested rewrite (full text) |
|---|---|---|---|
| Q36 | "37 players enter a badminton singles knockout. …" | Stem starts with a numeral (house rule). | "There are 37 players in a badminton singles knockout. In each match two players play, the loser is out, and there are no draws. In some rounds a player may get a free pass to the next round. How many matches are played to find the champion?" |
| Q19 | "… and they touch each other, as shown." | The solution's MN = 9 + 4 needs the circles to touch **externally**. At present only the figure says so. | "Two circles with centres M and N have radii 9 cm and 4 cm, and they touch each other externally, as shown. A straight line touches the larger circle at A and the smaller circle at B. What is the length of AB?" |
| Q24 | "The semicircle on AB passes through C." | "The semicircle on AB" is used before it has been introduced. | "In the figure, ABC is a triangle with ∠C = 90°, CA = 6 cm and CB = 8 cm. Semicircles are drawn outwards on CA and on CB. A third semicircle, on AB, passes through C. What is the total area of the two shaded crescents?" |
| Q24 (solution) | "Large semicircle on AB = 10 cm: (π/2)(5²) …" | Sets an area equal to a length, and does not show that AB = 10. | "… By Pythagoras AB = 10 cm, so the semicircle on AB is (π/2)(5²) = 25π/2. …" |
| Q7 (solution) | "Capital is profit ÷ time: …" | Not literally true. Capital is only *proportional to* share ÷ time. | "Each capital is in proportion to share ÷ time: 5/10 : 3/12 = 1/2 : 1/4 = 2 : 1." |
| Q4 (solution) | "… per quarter. 40,000 × 1.03 = …" | A sentence starts with a numeral. | "… per quarter. Then 40,000 × 1.03 = 41,200 …" |
| Q20 (solution) | "462 is one-third of 1,386, …" | A sentence starts with a numeral. | "The area 462 m² is one-third of this, so the angle is 360° ÷ 3 = 120°." |
| Q37 (solution) | "1 × 1 squares: 5 × 3 = 15. 2 × 2 squares: …" | Sentences start with numerals. | "Squares of size 1 × 1: 5 × 3 = 15. Size 2 × 2: 4 × 2 = 8. Size 3 × 3: 3 × 1 = 3. Total 15 + 8 + 3 = 26." |
| Q43 (optional) | "… and the fourth corner of the shelf lies on the longest side" | Understandable, but "fourth" is slightly indirect. Not put in the JSON. | "… and the corner of the shelf opposite the right angle lies on the longest side" |

All the fixes above except Q43 are in `paper4_fixes.json`. Each "old" value was checked and appears exactly once in runs4.txt.

## Figures
| Q | Issue | Fix |
|---|---|---|
| Q16 | No right-angle squares where Kiara and the tree meet the ground. The solution relies on "the two right triangles". | Add square marks at the foot of Kiara and at the foot of the tree. |
| Q27 | The vertical dotted line through the bird and its reflection meets the water line and the horizontal from P at right angles, but neither is marked. The solution uses both right triangles. The "water" label also sits on the dotted line. | Add a square where the dotted vertical meets the horizontal through P (or the water line). Move the "water" label clear of the dotted line. |
| Q42 | No right-angle mark at T, although the solution uses OT ⊥ ground (T, O, K collinear, TK = 3 m). The right angle at A is marked. | Add a square at T between OT and the ground. |
| Q43 | The "shelf" label sits in the orange (unused) triangle above the hatched rectangle, so it labels the wrong region. The "60 cm" label overlaps the vertical edge. | Put "shelf" inside the hatched rectangle, or use a leader line to it. Move "60 cm" left, clear of the edge. |
| Q19 | The "4 cm" label overlaps radius NB and the right-angle mark at B. | Move "4 cm" to the left of NB. |
| Q23 (minor) | The height (dashed) meets the top and bottom radii with no right-angle marks. | Optional: add small squares at both ends of the 15 cm height. |
| Q21 (minor) | Perspective: the top of the ball rises above the front rim of the lid, so the ball looks as if it pokes out of the box. | Optional: redraw so the ball meets the lid inside the top ellipse. |
| Answer sheet (cosmetic) | Rows 10–15 in column 1 are pushed right by the two-digit numbers, so the circles do not line up with rows 1–9. | Pad the numbers in column 1 or right-align them. |

Checked and found correct: Q17 (right angle at T marked; 6 cm and 4 cm match the stem), Q24 (the arcs are geometrically correct for the circle on AB through C; the right angle at C is marked), Q27 (drawn to scale: h ≈ 16, with 30° and 60° consistent), Q37 (5 × 3 grid), Q42 (PT ≈ √3 at the drawn scale; the 60° arc is on PK), Q43 (the drawn shelf is not the optimum, so it does not give the answer away), and the Q6 and Q28 tables.

## Syllabus / level / difficulty
- Blueprint counts are exact. Every Section I question stays within one chapter. The Section II pairings are Q41 Ch4+Ch10, Q42 Ch5+Ch7, Q43 Ch4+Ch5, Q44 Ch3+Ch9 and Q45 Ch6+Ch10, all as in the brief.
- Q13 uses the relations between the zeroes and coefficients of a **cubic**. The current rationalised CBSE Grade-10 board book covers only quadratics. The brief says "Polynomials: zeroes ↔ coefficients" at olympiad depth, so I accept it. Confirm this with the syllabus owner if a strict board-only reading is intended.
- Q41 is listed as "Ch10 pigeonhole applied" in the pairing table. The Ch10 part is actually case enumeration of integer solutions, not pigeonhole. This is acceptable as combinatorial reasoning, but it does not use pigeonhole.
- Q29 is effectively a single-event classical probability question (a C9 rung) dressed as two stages. That is allowed as spiral review, and Q30 supplies a genuine two-stage event. Ch8 has no grouped mean, median or mode question. Q28, the cumulative "more than" table, is the only statistics item, which is fine for 3 slots.
- Applied Mathematics covers discount (Q31), break-even (Q32), work-rate (Q33), boats and streams (Q34) and time and work (Q35). There is no GST question, so the GST slabs (5%, 18%, 40%) are not an issue.
- Difficulty labels are reasonable. Q36 (knockout matches = n − 1) is an insight item labelled Easy. If a stronger Easy is wanted, it could swap with Q7 (Medium), but no change is needed.
- Guardrail D5 ("harder than SOF/Silverzone"): several Easy items are textbook one-steppers (Q17, Q20, Q21, Q25, Q26). They are acceptable as Easy, but these are where the paper is weakest against the guardrail.

## Questions with no issues
Q1, Q2, Q3, Q5, Q6, Q8, Q9, Q10, Q11, Q12, Q13, Q14, Q15, Q17, Q18, Q22, Q25, Q26, Q28, Q29, Q30, Q31, Q32, Q33, Q34, Q35, Q38, Q39, Q40, Q41, Q44, Q45.

## Topic list
- Q1 — Ch1 Real numbers — Euclid's algorithm, HCF(1001, 455) = 91
- Q2 — Ch1 Divisibility — n³ − n always divisible by 6
- Q3 — Ch1 HCF — pairs with HCF 18 and sum 216 (2 pairs)
- Q4 — Ch3 Compound interest (quarterly) — time to reach ₹42,436 (6 months)
- Q5 — Ch3 Partnership — working partner's salary, then capital ratio (₹27,500)
- Q6 — Ch3 Partnership — capital × time from a table (₹12,000)
- Q7 — Ch3 Partnership — capital ratio from shares and times (2 : 1)
- Q8 — Ch3 CI half-yearly with a mid-year deposit (₹42,640)
- Q9 — Ch4 Polynomials — reciprocal zeroes, k = 4
- Q10 — Ch4 Linear equations (modelling) — boxes and trays (8)
- Q11 — Ch4 AP nth term — hiking climb, 8th hour
- Q12 — Ch4 Quadratic (biquadratic reducible) — sum of positive roots 5
- Q13 — Ch4 Polynomials — cubic with zeroes in AP, k = 39
- Q14 — Ch4 AP sum — first term from two block sums (2)
- Q15 — Ch5 Coordinate geometry — fourth vertex of a parallelogram (3, 5)
- Q16 — Ch5 Similar triangles — mirror and tree height (9 m)
- Q17 — Ch5 Tangents — PT from OP and radius (8 cm)
- Q18 — Ch5 Distance formula — circumcentre of a right triangle (4, 5)
- Q19 — Ch5 Tangents — common tangent of touching circles (12 cm)
- Q20 — Ch6 Sector area — sprinkler angle 120°
- Q21 — Ch6 Sphere in cylinder — empty fraction 1/3
- Q22 — Ch6 Volume conservation — water rise 2 cm
- Q23 — Ch6 Frustum — volume against average-radius cylinder (20π)
- Q24 — Ch6 Areas of circles — lunes of Hippocrates (24 cm²)
- Q25 — Ch7 Specific angles — (1 − tan²30°)/(1 + tan²30°) = 1/2
- Q26 — Ch7 Identities — tan θ + cot θ = sec θ cosec θ
- Q27 — Ch7 Heights & distances — bird and its reflection (16 m)
- Q28 — Ch8 Cumulative frequency ("more than") — class count 22
- Q29 — Ch8 Probability — second draw after a known first draw (2/3)
- Q30 — Ch8 Probability — two dice, second number greater (5/12)
- Q31 — Ch9 Discount — buy 3 get 1 free, 25%
- Q32 — Ch9 Break-even / profit target — 600 candles
- Q33 — Ch9 Work-rate (unitary) — sandwiches, 540
- Q34 — Ch9 Boats & streams — raft drift time 12 h
- Q35 — Ch9 Time & work — alternate days, 6½ days
- Q36 — Ch10 Invariant/counting — knockout matches 36
- Q37 — Ch10 Combinatorial counting — squares in a 5 × 3 grid (26)
- Q38 — Ch10 Counting principle — 3-stripe flags (150)
- Q39 — Ch10 Extremal — largest subset of 1–20 with no x and 2x together (14)
- Q40 — Ch10 Invariants (mod 3) — counter recolouring, blue
- Q41 — Ch4 + Ch10 — integer solutions for ticket mixes (3)
- Q42 — Ch5 + Ch7 — equal tangents and angle of elevation, PA = √3 m
- Q43 — Ch4 + Ch5 — largest rectangle in a right triangle (1,200 cm²)
- Q44 — Ch3 + Ch9 — time & work plus partnership (₹24,000)
- Q45 — Ch6 + Ch10 — recasting spheres, surface area doubles each round (4)
