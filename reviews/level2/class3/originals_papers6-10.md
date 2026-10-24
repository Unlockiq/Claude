# Review: AMO Class 3 Level 2, original Practice Papers 6–10

Sources: `c3/clean/Test06–10_QP.pdf` (pages rendered at 110 dpi, with 250–400 dpi crops for close counts) and `c3/in/Test06–10_AK.pdf`. I solved every question myself before comparing it with the key.

## Summary

### Wrong keys / broken questions (4, all with no correct option or two correct options)
| Paper Q | Key | Correct | Evidence |
|---|---|---|---|
| P8 Q2 rectangles (T-shape) | A 8 | **11** (not offered) | 3 top cells + 2 under the middle cell: 5 singles + 3 horizontal (2 pairs + 1 row) + 3 vertical (2 pairs + 1 column) = 11. Options are 8/5/6/10. |
| P8 Q14 triangles (pentagram) | B 5 | **10** (not offered) | It is a proper 5-line pentagram. Every set of 3 lines makes a triangle, giving C(5,3) = 10: 5 tip triangles + 5 large ones (e.g. apex, inner point, bottom-right point). Options are 8/5/6/4. |
| P9 Q20 mirror image of '3' | C (P) | **P and R both look like Ɛ** | R is P flipped vertically (pixel XOR after flip: 281 vs 593 after a shift only). On paper they look the same, so there are two correct options. |
| P9 Q23 triangles (2 lines from the apex + 1 horizontal) | B 11 | **12** (not offered) | The horizontal line runs from side to side (checked at 400 dpi). 4 lines from the apex give 6 pairs, and each pair makes a triangle with 2 bases: 6 × 2 = 12. Options are 8/11/9/10. |

All other 146 keys are correct.

### Wrong or mismatched solution texts (6)
- P8 Q2: "various combined rectangles totalling 8". This is wrong; the count is 11.
- P8 Q14: "5-pointed star = 5 small triangles". It leaves out the 5 large triangles.
- P9 Q23: "…add up to 11". This is wrong; the count is 12.
- P9 Q11: "5 circles in the row + 1 circle above". The picture is 2 staggered rows plus a small circle inside the orange one. The total of 6 is right, but the description does not match the picture.
- P9 Q18: the solution uses decimals ("1/5 = 0.2, 1/3 ≈ 0.33").
- P6 Q16: the hint "Difference is constant" is irrelevant to the question (minor).

### Syllabus / style violations (by type)
| Type | Count | Questions |
|---|---|---|
| "Rs." instead of ₹ | 11 | P6 Q13, Q24; P7 Q13, Q24; P8 Q13, Q24; P9 Q13, Q24; P10 Q12 (options also have no unit), Q13, Q24 |
| Non-mathematical letter counting (REAL) | 5 | P6 Q9 (vowels), P7 Q9 ('ABC' in a string), P8 Q9 ('A' in MATHEMATICAL), P9 Q9 (repeated letters), P10 Q9 (common letters) |
| Mirror image of letters/digits/arrows (REAL-style, borderline) | 5 | Q20 in every paper |
| Unlike fractions | 5 | P7 Q25 (3/5 vs 2/3), P8 Q25 (3/4 vs 5/8), P9 Q18 (1/2 vs 1/4, 1/5 vs 1/3), P9 Q19 (3/6 vs 1/2), P10 Q25 (1/4, 1/2, 3/4) |
| Simplifying or equivalent fractions (beyond like fractions) | 2 | P9 Q25 (4/8 = 1/2), P10 Q19 (6/12 = 1/2 used as a "both correct" option) |
| Decimals | 3 | P7 Q24 ("1.5 kg"), P10 Q3 (option 32.5 cm), P9 Q18 (solution) |
| Off-syllabus topic | 1 | P10 Q28 (angle sum of a triangle = 180°; degrees are not in Class 3) |
| Non-mathematical odd-one-out | 0 | Q22 in every paper is mathematical (parity, wrong product, sides, units, symmetry) |
| Colour carrying information | 0 | Colours are decorative only |
| Sentence > 25 words / non-Indian names | 0 | — |

### Other quality issues (minor)
- **Picture shows the wrong count (all 5 papers, Q12):** every picture has 3 emoji while the stem says 9 cars, 8 days, 8 rows, 5 stickers or 7 apples.
- **Contrived answer formats:**
  - Q15 in every paper gives the answer as a sum such as "12 + 13".
  - Q29 in P6–P8 gives it as an expression such as "50 − 18" for 4 × 8. This is an odd way to ask for "the correct expression".
- **Rule not stated in a series question:** P6 Q1 and P8 Q1 do not state the rule, yet offer "Cannot find" as an option. The key's answer is the natural one, but the "Cannot find" option is defensible.
- **Wording or dispute risk:**
  - P7 Q17 says "MORE" where it should say "MOST".
  - P6 Q9 assumes Y is not a vowel.
  - P7 Q23 has partly hidden back triangles; the intended count of 8 is OK.

### Difficulty mix (150 Qs)
E 83, M 64, H 3. All three H questions are broken ones (P8 Q2, P8 Q14, P9 Q23), so there is effectively no valid H item. These papers are much easier than a Level 2 paper should be.

### Shared template
**Yes.** All five papers use the same template, with each question number always covering the same topic:
Q1 P–T series, Q2 count rectangles, Q3 length, Q4 circles/semicircles, Q5 forming numbers from digits, Q6 add/subtract, Q7 m–cm, Q8 clock time, Q9 letter counting, Q10 weight, Q11 count circles, Q12 multiplication with 3 emoji, Q13 money (Rs.), Q14 count triangles, Q15 "a + b" options, Q16 ages, Q17 symmetry, Q18 "find the INCORRECT statement", Q19 like fractions, Q20 mirror image P/Q/R/S, Q21 number series, Q22 odd one out, Q23 count triangles, Q24 unit price (Rs.), Q25 compare fractions, Q26 Roman numerals, Q27 time difference, Q28 sides/vertices of N polygons, Q29 "choose the expression", Q30 number line.

---

## Paper 6
| Q | Key | Mine | Key OK? | Sol OK? | Issues | Diff |
|---|---|---|---|---|---|---|
| 1 | A | A (136) | ✓ | ✓ | Rule (doubling) not stated; "Cannot find" option is defensible | M |
| 2 | C | C (18) | ✓ | ✓ | 2×3 grid: 3×6 = 18 | M |
| 3 | A | A (86) | ✓ | ✓ | — | M |
| 4 | B | B (5) | ✓ | ✓ | — | E |
| 5 | A | A (7632, 2367) | ✓ | ✓ | — | M |
| 6 | B | B (548) | ✓ | ✓ | — | E |
| 7 | A | A (1 m 45 cm) | ✓ | ✓ | — | M |
| 8 | A | A (3:45 PM) | ✓ | ✓ | — | M |
| 9 | C | C (7) | ✓ | ✓ | Letter counting (REAL); Y not counted as a vowel | E |
| 10 | B | B (108 g) | ✓ | ✓ | — | E |
| 11 | C | C (4) | ✓ | ✓ | — | E |
| 12 | B | B (36) | ✓ | ✓ | Picture shows 3 cars, stem says 9 | E |
| 13 | A | A (213) | ✓ | ✓ | Rs. | E |
| 14 | A | A (1) | ✓ | ✓ | — | E |
| 15 | A | A (25 = 12+13) | ✓ | ✓ | Contrived "a+b" options | M |
| 16 | C | C (28) | ✓ | ~ | Hint "Difference is constant" irrelevant | E |
| 17 | B | B (A) | ✓ | ✓ | — | E |
| 18 | B | B | ✓ | ✓ | 8,043: 0 is in the hundreds place | E |
| 19 | A | A (4/10) | ✓ | ✓ | — | E |
| 20 | C | C (Q = Ǝ) | ✓ | ✓ | Mirror image of a letter (REAL, borderline) | E |
| 21 | C | C (16) | ✓ | ✓ | — | E |
| 22 | C | C (73 odd) | ✓ | ✓ | — | E |
| 23 | A | A (3) | ✓ | ✓ | Pentagon with 2 diagonals from A | M |
| 24 | A | A (30) | ✓ | ✓ | Rs. | E |
| 25 | A | A (=) | ✓ | ✓ | Picture: 3/4 − 1/4 vs 2/4 | M |
| 26 | A | A (8) | ✓ | ✓ | — | M |
| 27 | A | A (1 h 45 min) | ✓ | ✓ | — | M |
| 28 | B | B (27) | ✓ | ✓ | — | E |
| 29 | A | A (32 = 50−18) | ✓ | ✓ | Contrived "expression" options | M |
| 30 | C | C (4+7 = 11) | ✓ | ✓ | — | M |

## Paper 7
| Q | Key | Mine | Key OK? | Sol OK? | Issues | Diff |
|---|---|---|---|---|---|---|
| 1 | A | A (985+541 = 1526) | ✓ | ✓ | — | M |
| 2 | B | B (4 nested) | ✓ | ✓ | — | E |
| 3 | A | A (3 km 775 m) | ✓ | ✓ | — | E |
| 4 | B | B (4) | ✓ | ✓ | — | E |
| 5 | A | A (592, 925) | ✓ | ✓ | — | M |
| 6 | B | B (433) | ✓ | ✓ | — | E |
| 7 | D | D (45 cm) | ✓ | ✓ | — | M |
| 8 | A | A (1 h 20 min) | ✓ | ✓ | — | M |
| 9 | B | B (4) | ✓ | ✓ | 'ABC' in a letter string: non-mathematical (REAL) | E |
| 10 | A | A (4225 g) | ✓ | ✓ | — | M |
| 11 | C | C (5) | ✓ | ✓ | — | E |
| 12 | B | B (48) | ✓ | ✓ | Picture shows 3 books | E |
| 13 | A | A (84) | ✓ | ✓ | Rs. | E |
| 14 | C | C (8) | ✓ | ✓ | Checked at 250 dpi: 8 triangles | E |
| 15 | D | D (28 = 14+14) | ✓ | ✓ | Contrived options | M |
| 16 | B | B (36) | ✓ | ✓ | — | E |
| 17 | B | B (circle) | ✓ | ✓ | "MORE" should be "MOST" | E |
| 18 | D | D (70 > 70 false) | ✓ | ✓ | — | E |
| 19 | C | C (6/8) | ✓ | ✓ | — | E |
| 20 | B | B (P = ꓘ) | ✓ | ✓ | Mirror image (REAL, borderline) | E |
| 21 | C | C (21) | ✓ | ✓ | — | E |
| 22 | D | D (7×8 ≠ 54) | ✓ | ✓ | — | E |
| 23 | D | D (8) | ✓ | ✓ | 4 overlapping pairs; back triangles partly hidden | M |
| 24 | C | C (120) | ✓ | ✓ | Decimal "1.5 kg"; Rs. | M |
| 25 | B | B (2/3) | ✓ | ✓ | Unlike fractions (3/5 vs 2/3); solution uses LCD 15 | M |
| 26 | B | B (XV) | ✓ | ✓ | — | E |
| 27 | A | A (1 h 45 min) | ✓ | ✓ | — | M |
| 28 | A | A (48) | ✓ | ✓ | — | E |
| 29 | C | C (42 = 60−18) | ✓ | ✓ | Contrived options | M |
| 30 | A | A (9−2 = 7) | ✓ | ✓ | — | E |

## Paper 8
| Q | Key | Mine | Key OK? | Sol OK? | Issues | Diff |
|---|---|---|---|---|---|---|
| 1 | A | A (120+280 = 400) | ✓ | ✓ | Alternating +50/+30 not stated; "Cannot find" option | M |
| 2 | A | **11 (none)** | ✗ | ✗ | **BROKEN**: T-shape 5 + 3 + 3 = 11; no option | H |
| 3 | A | A (1 m 80 cm) | ✓ | ✓ | — | E |
| 4 | C | C (6−4 = 2) | ✓ | ✓ | — | M |
| 5 | A | A (3058) | ✓ | ✓ | — | M |
| 6 | B | B (643) | ✓ | ✓ | — | E |
| 7 | A | A (760 cm) | ✓ | ✓ | — | M |
| 8 | A | A (7:55 PM) | ✓ | ✓ | — | M |
| 9 | B | B (3) | ✓ | ✓ | Letter counting (REAL) | E |
| 10 | A | A (600 g) | ✓ | ✓ | — | M |
| 11 | C | C (6) | ✓ | ✓ | — | E |
| 12 | C | C (48) | ✓ | ✓ | Picture shows 3 chairs | E |
| 13 | B | B (255) | ✓ | ✓ | Rs. | E |
| 14 | B | **10 (none)** | ✗ | ✗ | **BROKEN**: pentagram has 5 small + 5 large = 10 triangles; no option | H |
| 15 | B | B (42) | ✓ | ✓ | — | M |
| 16 | B | B (58) | ✓ | ✓ | — | E |
| 17 | D | D (F) | ✓ | ✓ | — | E |
| 18 | D | D (IV ≠ 6) | ✓ | ✓ | — | E |
| 19 | B | B (5/8) | ✓ | ✓ | — | E |
| 20 | B | B (Q) | ✓ | ✓ | Mirror image (REAL, borderline) | E |
| 21 | B | B (21) | ✓ | ✓ | — | M |
| 22 | C | C (triangle) | ✓ | ✓ | Trivial | E |
| 23 | A | A (6) | ✓ | ✓ | — | M |
| 24 | B | B (165) | ✓ | ✓ | Rs. | E |
| 25 | A | A (3/4) | ✓ | ✓ | Unlike fractions (3/4 vs 5/8) | M |
| 26 | A | A (18) | ✓ | ✓ | — | E |
| 27 | A | A (7 s) | ✓ | ✓ | — | E |
| 28 | B | B (50) | ✓ | ✓ | — | E |
| 29 | C | C (45 = 90−45) | ✓ | ✓ | Contrived options | M |
| 30 | B | B (midpoint of 1 and 9 = 5) | ✓ | ✓ | — | M |

## Paper 9
| Q | Key | Mine | Key OK? | Sol OK? | Issues | Diff |
|---|---|---|---|---|---|---|
| 1 | B | B (145+235 = 380) | ✓ | ✓ | — | M |
| 2 | A | A (5) | ✓ | ✓ | H-shape; no internal lines in the bar (checked at 300 dpi) | E |
| 3 | D | D | ✓ | ✓ | — | M |
| 4 | B | B (4 + 2 = 6) | ✓ | ✓ | — | M |
| 5 | A | A (7540) | ✓ | ✓ | — | M |
| 6 | A | A (367) | ✓ | ✓ | — | E |
| 7 | A | A (400 cm) | ✓ | ✓ | — | M |
| 8 | A | A (5:15 PM) | ✓ | ✓ | — | E |
| 9 | A | A (M, A, T = 3) | ✓ | ✓ | Letter counting (REAL) | M |
| 10 | B | B (Q 1450 g) | ✓ | ✓ | — | M |
| 11 | B | B (6) | ✓ | ✗ | Solution says "5 in a row + 1 above"; picture is 2 staggered rows + a circle inside a circle | E |
| 12 | D | D (20) | ✓ | ✓ | Picture shows 3 tickets | M |
| 13 | A | A (65) | ✓ | ✓ | Rs. | E |
| 14 | B | B (3) | ✓ | ✓ | — | E |
| 15 | A | A (8 = 7+1) | ✓ | ✓ | Contrived options | M |
| 16 | A | A (9) | ✓ | ✓ | — | E |
| 17 | B | B (square) | ✓ | ✓ | — | E |
| 18 | D | D | ✓ | ✗ | Unlike fractions (1/2 vs 1/4, 1/5 vs 1/3); solution uses decimals | M |
| 19 | C | C (=) | ✓ | ✓ | Needs 3/6 = 1/2 (unlike/equivalent fractions) | M |
| 20 | C | **P or R** | ✗ | ✗ | **BROKEN**: R is P flipped vertically; both look like Ɛ | E |
| 21 | B | B (25) | ✓ | ✓ | — | E |
| 22 | B | B (grams) | ✓ | ✓ | — | E |
| 23 | B | **12 (none)** | ✗ | ✗ | **BROKEN**: horizontal line runs side to side, so 6 × 2 = 12; no option | H |
| 24 | A | A (800) | ✓ | ✓ | Rs. | M |
| 25 | A | A (4/8 = 1/2) | ✓ | ✓ | Requires simplifying the fraction | E |
| 26 | B | B (XXIV) | ✓ | ✓ | — | E |
| 27 | A | A (165 min) | ✓ | ✓ | — | M |
| 28 | D | D (36) | ✓ | ✓ | — | E |
| 29 | A | A (22 = 12+10) | ✓ | ✓ | — | M |
| 30 | D | D (S = 9) | ✓ | ✓ | — | E |

## Paper 10
| Q | Key | Mine | Key OK? | Sol OK? | Issues | Diff |
|---|---|---|---|---|---|---|
| 1 | A | A (240) | ✓ | ✓ | — | M |
| 2 | D | D (11) | ✓ | ✓ | Plus shape: 5 + 4 + 2 | M |
| 3 | A | A (130 cm) | ✓ | ✓ | Decimal option "32.5 cm" | E |
| 4 | A | A (5 > 3) | ✓ | ✓ | — | E |
| 5 | A | A (1047) | ✓ | ✓ | — | M |
| 6 | A | A (419) | ✓ | ✓ | — | M |
| 7 | C | C (240 cm = 2 m 40 cm) | ✓ | ✓ | — | M |
| 8 | A | A (2:30 AM) | ✓ | ✓ | — | E |
| 9 | A | A (E, P, A = 3) | ✓ | ✓ | Letter counting (REAL) | M |
| 10 | A | A (565 g) | ✓ | ✓ | — | M |
| 11 | B | B (3) | ✓ | ✓ | — | E |
| 12 | B | B (84) | ✓ | ✓ | Rs. in stem; options have no unit; picture shows 3 apples | E |
| 13 | B | B (200) | ✓ | ✓ | Rs. | E |
| 14 | A | A (2) | ✓ | ✓ | — | E |
| 15 | A | A (11 = 6+5) | ✓ | ✓ | Contrived options | M |
| 16 | A | A (18) | ✓ | ✓ | — | E |
| 17 | A | A (triangle) | ✓ | ✓ | — | E |
| 18 | D | D | ✓ | ✓ | — | E |
| 19 | D | D | ✓ | ✓ | "Both" option relies on 6/12 = 1/2 (simplification) | M |
| 20 | D | D (P ←) | ✓ | ✓ | Mirror image (REAL, borderline) | E |
| 21 | B | B (37) | ✓ | ✓ | — | E |
| 22 | C | C (parallelogram) | ✓ | ✓ | — | E |
| 23 | B | B (8) | ✓ | ✓ | — | M |
| 24 | B | B (360) | ✓ | ✓ | Rs. | M |
| 25 | A | A | ✓ | ✓ | Unlike fractions (1/4, 1/2, 3/4) | M |
| 26 | B | B (XI) | ✓ | ✓ | — | E |
| 27 | B | B (11:50) | ✓ | ✓ | — | M |
| 28 | B | B (180°) | ✓ | ✓ | Off-syllabus: angles/degrees | E |
| 29 | B | B (8) | ✓ | ✓ | — | E |
| 30 | B | B (1+4+7+8 = 20) | ✓ | ✓ | — | M |
