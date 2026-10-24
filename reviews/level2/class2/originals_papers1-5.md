# AMO Class 2 Level-2: review of original Practice Papers 1–5

Scope: Test01–05 QP (clean) against Test01–05 AK and the Class 2 syllabus (v5.9, cumulative with Class 1). I solved every question before reading the key. I counted every picture from a 220 dpi render, and where the counts were close I also checked the embedded source image (pdfimages). I counted triangles programmatically from line and vertex lists. Working files are in `c2/review_a/`.

## Summary

### Wrong keys (7 clear and 2 broken; 9 of 150)
| Paper Q | Key | Correct | Evidence |
|---|---|---|---|
| P1 Q3 | C KK8 | **D JJ8** | C,D,(E),F,G,(H),I → the gaps go +1,+2,+1,+2, so the next gap is +1 → J. The hint ("skip after every two") itself gives JJ. |
| P1 Q22 | D 10 | **C 11** | The hexagon rows hold 3+3+3+2 = 11. The other two shapes are a pentagon and a square. |
| P2 Q22 | B 9 | **D 10** | Rows hold 3+2+3+2 = 10. The other shapes are circles and rectangles. The solution text says "13", which is not an option. |
| P4 Q18 | A 50 | **C 29** | 50, 18 and 36 are even and 29 is odd. The key's rule "multiples of 9" excludes both 50 and 29. The solution cites "27", which is not an option. |
| P4 Q22 | C 14 | **D 15** | Rows hold 4+5+4+2 = 15. One hexagon is partly behind the bee but is clearly a hexagon. The drip shape is a pentagon. |
| P5 Q22 | C 10 | **A 9** | The honeycomb has 2+2+2+2 = 8, plus the separate hexagon at lower left = 9. The other shapes are a pentagon and a triangle. |
| P3 Q29 | B 12 | none (15) | **Broken.** The full listing is ABC, ADE, ADF, AEF, DFG, EFH, FGH, GHM, BDG, BGM, CEH, CHM, DEM, BDM, CEM = 15. D-G-M and E-H-M are straight lines. The source web image shows options 12/15/16/13. |
| P4 Q29 | C 14 | none (18; 19 with the flag) | **Broken.** Sail: 13 (ALR, APQ, APX, AXQ, PXO, QXO, POQ, PLO, QRO, ALO, AOR, APO, AQO). Hull: 5. The flag is a 19th triangle. The raw embedded image contains the text "Total triangles = 14", hidden under a white mask. |
| P1 Q27 | C 8 | B 7 (ambiguous) | 7 cubes are visible (a 3-high tower and 2+2 in front and back). 8 is only right if a hidden cube sits behind the tower. The solution says "5 bottom + 3 on top", but only 2 cubes are on top. |

### Other broken or ambiguous questions
- **P3 Q10:** two answers can be defended. B (698+4 = 702) is the only sum whose hundreds digit changes. C (350+5 = 355) is the only odd sum.
- **P1 Q13:** the hour hand points exactly at 3 for 3:30, so the face is physically wrong. The key's solution ("hour-hand on 3 → 3:30") teaches a misconception.
- **P3 Q13:** for 6:15 the hour hand is drawn near 7 (about 6:35 on the face). The hint says it is "just past 6".

### Solution texts that do not match the picture (16)
P1 Q11 and Q23 ("pies", but the picture shows bars) · P1 Q13 · P1 Q22 · P1 Q27 · P2 Q17 ("Row 1: 4, Row 2: 1"; the picture has 3 and 2, and the distractors are dresses, not caps or pants) · P2 Q22 ("13") · P2 Q27 ("bottom 2×3 = 6 + 2 on back corners"; the picture has 5 on the bottom and 3 on top, total 8) · P3 Q17 ("Row 1: 3, Row 2: 1"; the picture has 4 pants in row 1) · P3 Q27 ("2×2 grid + 2 stacked"; the picture is a 3×2 wall) · P3 Q29 · P4 Q18 · P4 Q22 · P4 Q29 · P5 Q17 ("Row 1: 4 buses"; the picture has 2 in row 1 and 1 in each other row) · P5 Q22 · P5 Q29 ("circles formed by overlaps" is meaningless, though the count of 6 is right).

### Syllabus violations by type
| Type | Count | Questions |
|---|---|---|
| Letter series (REAL-style) | 5 | Q3 in P1–P5 |
| Letter coding (MNO = 432 …) | 5 | Q28 in P1–P5 |
| Fractions | 10 | Q11 and Q23 in P1–P5 |
| Four-digit numbers (> 999) | 5 | Q25 in P1–P5 |
| "Rs." instead of ₹ (question and key) | 5 | Q4 in P1–P5 |
| Division beyond halving or quartering | 4 | P2 Q6 (30÷5), P3 Q6 (28÷7), P4 Q6 (36÷6), P5 Q6 (45÷5). P1 Q6 (24÷4) is quartering, so it is fine. |
| Multiplication beyond 1-digit × 1-digit | 2 | P5 Q4 (4×₹25, 2×₹50); P3 Q4 (2×₹20, mild) |
| Non-mathematical odd-one-out | 2 | P3 Q24 (vowels), P4 Q24 (bird vs mammals) |
| Concept beyond syllabus in the key (factors and multiples) | 5 | Q18 solutions in P1–P5 ("common factor", multiples of 6/7/8/9). P1, P3 and P5 can be solved by even/odd. P2 needs the 7-times table. P4 is broken. |
| Colour carrying information | 1 (mild) | P5 Q29: overlapping translucent fills; the light-blue circle on orange is weak in greyscale |

No problems found for non-Indian names, sentences over 25 words or clock times in the stems. The minute-level clock options (3:06, 6:12, 12:06, 12:09, 6:35) appear only as distractors. About 36 question slots break the syllabus: 6 fixed slots × 5 papers, plus 4 Q6s and 2 Q24s.

### Provenance
P3 Q29, P4 Q27 and P4 Q29 are cropped internet puzzle images. Their embedded rasters still carry the original text: "How many triangles…" with options 12/15/16/13, "Can you count the number of cubes in 9 seconds?", and "Total triangles = 14". This is a copyright risk, and the answer can be extracted from the file.

### Difficulty mix (E/M/H)
P1 14/14/2 · P2 13/15/2 · P3 16/12/2 · P4 15/12/3 · P5 14/15/1. The papers lean Easy. "Hard" questions are almost only Q4 (3-step money) and the picture-counting Q27/Q29. Few distractors are built on common mistakes; exceptions are P5 Q1 (752 is even), the 0-leading options in Q25 and the hand-swap options in Q13.

### Shared template
**Yes, all five papers use one fixed 30-slot template**, with only numbers, names and pictures swapped: Q1 make a number from digits · Q2 "N children took k each" · Q3 letter+number series · Q4 notes minus purchases · Q5 AP missing term · Q6 equal groups · Q7 "balloons/kites showing '6', add the 6s, subtract" · Q8 incorrect place value · Q9 P,Q,R,S descending · Q10 odd one out of "x + y" in words (carry into hundreds) · Q11 fraction bars · Q12 2-digit subtraction · Q13 clock · Q14 P,Q,R,S ascending, k-th from left/right · Q15 total as "10 + 10 + x" · Q16 ears ×2, then double · Q17 count one item type · Q18 odd number out · Q19 calendar ±10/12 days · Q20 3-digit sum in words · Q21 count objects · Q22 count hexagons · Q23 fraction bars · Q24 varies · Q25 largest and smallest 4-digit number · Q26 marks more/less · Q27 count cubes · Q28 letter code · Q29 count triangles/circles · Q30 polygon sides. The hint and solution sentences are reused verbatim, which is how errors such as "pies" and the wrong row counts carried over.

---

## Paper 1
| Q | Key | Mine | Key OK? | Solution OK? | Syllabus / quality issues | Diff |
|---|---|---|---|---|---|---|
| 1 | B | B 952 | ✓ | ✓ | – | E |
| 2 | C | C 14 | ✓ | ✓ | – | M |
| 3 | C | **D JJ8** | ✗ | ✗ logic (skips J wrongly) | Letter series (not allowed) | M |
| 4 | D | D ₹15 | ✓ | ✓ | "Rs."; 3 steps | H |
| 5 | B | B 16 | ✓ | ✓ | – | E |
| 6 | C | C 6 | ✓ | ✓ | 24÷4 = quartering, OK | E |
| 7 | D | D 22 | ✓ | ✓ | "12 balloons" is unused information; no picture | M |
| 8 | A | A | ✓ | ✓ | – | E |
| 9 | A | A SPRQ | ✓ | ✓ | – | M |
| 10 | B | B (601) | ✓ | ✓ | Weak "odd one out" rule (carry) | M |
| 11 | C | C < | ✓ | "pies", but picture shows bars | Fractions | E |
| 12 | D | D 2 | ✓ | ✓ | – | E |
| 13 | D | D 3:30 | ✓ | ✗ "hour-hand on 3" | Hour hand drawn exactly on 3 at 3:30 (wrong face) | E |
| 14 | B | B Q | ✓ | ✓ | – | M |
| 15 | A | A | ✓ | ✓ | – | M |
| 16 | A | A 2 tens | ✓ | ✓ (5 rabbits) | – | M |
| 17 | C | C 7 | ✓ | ✓ (4+3) | – | E |
| 18 | D | D 47 | ✓ | uses "multiples of 6" | Even/odd suffices; factor concept is off-syllabus | E |
| 19 | C | C Tue | ✓ | ✓ (date verified) | – | M |
| 20 | D | D 347 | ✓ | ✓ | – | M |
| 21 | C | C 4 | ✓ | ✓ | – | E |
| 22 | D | **C 11** | ✗ | ✗ says 10 | Rows 3+3+3+2 | E |
| 23 | C | C > | ✓ | "pies" vs bars | Fractions | E |
| 24 | D | D 8 | ✓ | ✓ (13−5) | – | M |
| 25 | A | A | ✓ | ✓ | Four-digit numbers (> 999) | M |
| 26 | D | D 66 | ✓ | ✓ | – | E |
| 27 | C | B 7 (ambiguous) | ? | ✗ "5 + 3 on top" (only 2 on top) | 8 needs a hidden cube behind the tower; ambiguous picture | M |
| 28 | D | D TN | ✓ | ✓ | Letter coding (not allowed) | M |
| 29 | C | C 9 | ✓ | ✓ | Lines in many colours (not needed to solve) | H |
| 30 | B | B 7 | ✓ | ✓ | – | E |

## Paper 2
| Q | Key | Mine | Key OK? | Solution OK? | Syllabus / quality issues | Diff |
|---|---|---|---|---|---|---|
| 1 | B | B 147 | ✓ | ✓ | – | E |
| 2 | C | C 4 | ✓ | ✓ | – | M |
| 3 | B | B DE4 | ✓ | ✓ | Letter series | M |
| 4 | A | A ₹31 | ✓ | ✓ | "Rs." | H |
| 5 | C | C 15 | ✓ | ✓ | – | E |
| 6 | C | C 6 | ✓ | ✓ | 30÷5 is beyond halving or quartering | E |
| 7 | B | B 15 | ✓ | ✓ | – | M |
| 8 | B | B | ✓ | ✓ | – | E |
| 9 | A | A PRSQ | ✓ | ✓ | – | M |
| 10 | B | B (602) | ✓ | ✓ | – | M |
| 11 | C | C > | ✓ | ✓ | Fractions | E |
| 12 | B | B 3 | ✓ | ✓ | – | E |
| 13 | D | D 9:00 | ✓ | ✓ | – | E |
| 14 | B | B Q | ✓ | ✓ | – | M |
| 15 | C | C | ✓ | ✓ | – | M |
| 16 | C | C 24 | ✓ | ✓ (6 dogs) | – | M |
| 17 | B | B 5 | ✓ | ✗ rows "4 + 1" (actual 3 + 2); hint says caps/pants, but the distractors are dresses | – | E |
| 18 | B | B 41 | ✓ | ✓ | Needs "multiples of 7" (14, 28 even; 35, 41 odd) | M |
| 19 | A | A Sat | ✓ | ✓ | – | M |
| 20 | A | A 519 | ✓ | ✓ | – | M |
| 21 | B | B 5 | ✓ | ✓ | – | E |
| 22 | B | **D 10** | ✗ | ✗ says 13 (not an option) | Rows 3+2+3+2 | E |
| 23 | C | C = | ✓ | ✓ | Fractions | E |
| 24 | D | D 8 | ✓ | ✓ (13 − 5) | "➖" emoji used as the operator | M |
| 25 | B | B | ✓ | ✓ | Four-digit numbers | M |
| 26 | B | B 94 | ✓ | ✓ | – | E |
| 27 | C | C 8 | ✓ | ✗ "6 bottom + 2 on back corners" (actual 5 + 3) | – | H |
| 28 | B | B NO | ✓ | ✓ | Letter coding | M |
| 29 | B | B 10 | ✓ | ✓ (5 up + 5 down) | – | M |
| 30 | C | C 8 | ✓ | ✓ | – | E |

## Paper 3
| Q | Key | Mine | Key OK? | Solution OK? | Syllabus / quality issues | Diff |
|---|---|---|---|---|---|---|
| 1 | C | C 863 | ✓ | ✓ | – | E |
| 2 | C | C 20 | ✓ | ✓ | – | M |
| 3 | B | B G8G | ✓ | ✓ | Letter series | M |
| 4 | B | B ₹33 | ✓ | ✓ | "Rs."; 2×20 is beyond 1-digit × 1-digit (mild) | H |
| 5 | C | C 24 | ✓ | ✓ | – | E |
| 6 | B | B 4 | ✓ | ✓ | 28÷7 is beyond halving or quartering | E |
| 7 | A | A 20 | ✓ | ✓ | – | M |
| 8 | B | B | ✓ | ✓ | – | E |
| 9 | A | A RPSQ | ✓ | ✓ | – | M |
| 10 | B | B (ambiguous) | ? | ✓ | **Ambiguous:** C (355) is the only odd sum | M |
| 11 | B | B = | ✓ | ✓ | Fractions | E |
| 12 | A | A 9 | ✓ | ✓ | – | E |
| 13 | A | A 6:15 | ✓ | hint "just past 6" | Hour hand drawn near 7 (wrong face) | E |
| 14 | D | D Q | ✓ | ✓ | Line break splits "50 + 0" | M |
| 15 | B | B | ✓ | ✓ | – | M |
| 16 | B | B 28 | ✓ | ✓ (7 cats) | – | M |
| 17 | B | B 4 | ✓ | ✗ "Row 1: 3, Row 2: 1" (actual 4 in row 1) | – | E |
| 18 | C | C 35 | ✓ | "multiples of 8" | Even/odd suffices | E |
| 19 | B | B Fri | ✓ | ✓ | – | M |
| 20 | B | B 579 | ✓ | ✓ | – | M |
| 21 | C | C 6 | ✓ | ✓ | – | E |
| 22 | C | C 10 | ✓ | ✓ (3+4+3) | – | E |
| 23 | C | C > | ✓ | ✓ | Fractions | E |
| 24 | C | C T | ✓ | ✓ | **Non-mathematical odd-one-out (vowels)** | E |
| 25 | A | A | ✓ | ✓ | Four-digit numbers | M |
| 26 | B | B 68 | ✓ | ✓ | – | E |
| 27 | C | C 6 | ✓ | ✗ "2×2 + 2 stacked" (picture is a 3×2 wall) | – | E |
| 28 | B | B NB | ✓ | ✓ | Letter coding | M |
| 29 | B | **15 (no option)** | ✗ | ✗ says 12 | **Broken**; cropped web image | H |
| 30 | B | B 6 | ✓ | ✓ | – | E |

## Paper 4
| Q | Key | Mine | Key OK? | Solution OK? | Syllabus / quality issues | Diff |
|---|---|---|---|---|---|---|
| 1 | C | C 257 | ✓ | ✓ | – | E |
| 2 | A | A 12 | ✓ | ✓ | – | M |
| 3 | C | C GI4 | ✓ | ✓ | Letter series | M |
| 4 | B | B ₹20 | ✓ | ✓ | "Rs." | H |
| 5 | B | B 24 | ✓ | ✓ | – | E |
| 6 | D | D 6 | ✓ | ✓ | 36÷6 is beyond halving or quartering | E |
| 7 | B | B 25 | ✓ | ✓ | – | M |
| 8 | C | C | ✓ | ✓ | – | E |
| 9 | A | A SQPR | ✓ | ✓ | – | M |
| 10 | C | C (803) | ✓ | ✓ | – | M |
| 11 | C | C < | ✓ | ✓ | Fractions | E |
| 12 | C | C 6 | ✓ | ✓ | – | E |
| 13 | C | C 12:30 | ✓ | ✓ | – | E |
| 14 | B | B Q | ✓ | ✓ | – | M |
| 15 | A | A | ✓ | ✓ | – | M |
| 16 | B | B 32 | ✓ | ✓ (8 monkeys) | – | M |
| 17 | A | A 8 | ✓ | ✓ | The "caps" are woolly beanies | E |
| 18 | A | **C 29** | ✗ | ✗ cites 27 (not an option) | 29 is the only odd number; 50 and 29 are both non-multiples of 9 | E |
| 19 | A | A Sun | ✓ | ✓ | – | M |
| 20 | B | B 392 | ✓ | ✓ | – | M |
| 21 | B | B 4 | ✓ | ✓ | – | E |
| 22 | C | **D 15** | ✗ | ✗ says 14 | Rows 4+5+4+2; one hexagon partly behind the bee | E |
| 23 | B | B = | ✓ | ✓ | Fractions | E |
| 24 | C | C parrot | ✓ | ✓ | **Non-mathematical odd-one-out (animals)** | E |
| 25 | A | A | ✓ | ✓ | Four-digit numbers | M |
| 26 | B | B 81 | ✓ | ✓ | – | E |
| 27 | C | C 9 | ✓ | ✓ (6 visible + 3 hidden supports) | Cropped web image ("count cubes in 9 seconds") | H |
| 28 | B | B NE | ✓ | ✓ | Letter coding | M |
| 29 | C | **18 (no option)** | ✗ | ✗ says 14 | **Broken**; the raw image contains "Total triangles = 14" under a mask | H |
| 30 | C | C 10 | ✓ | ✓ | – | E |

## Paper 5
| Q | Key | Mine | Key OK? | Solution OK? | Syllabus / quality issues | Diff |
|---|---|---|---|---|---|---|
| 1 | A | A 725 | ✓ | ✓ | Good trap (752 is even) | M |
| 2 | A | A 12 | ✓ | ✓ | – | M |
| 3 | B | B VV25 | ✓ | ✓ | Letter series | M |
| 4 | A | A ₹30 | ✓ | ✓ | "Rs."; 4×25 and 2×50 are beyond 1-digit × 1-digit | H |
| 5 | C | C 35 | ✓ | ✓ | – | E |
| 6 | B | B 9 | ✓ | ✓ | 45÷5 is beyond halving or quartering | E |
| 7 | A | A 18 | ✓ | ✓ | – | M |
| 8 | D | D | ✓ | ✓ | – | E |
| 9 | A | A PRQS | ✓ | ✓ | – | M |
| 10 | C | C (804) | ✓ | ✓ | – | M |
| 11 | B | B > | ✓ | ✓ | Fractions | E |
| 12 | B | B 3 | ✓ | ✓ | – | E |
| 13 | A | A 7:30 | ✓ | ✓ | – | E |
| 14 | C | C R | ✓ | ✓ | – | M |
| 15 | A | A | ✓ | ✓ | – | M |
| 16 | A | A 36 | ✓ | ✓ (9 bears) | – | M |
| 17 | B | B 5 | ✓ | ✗ "Row 1: 4 buses" (actual 2/1/1/1) | – | E |
| 18 | A | A 36 | ✓ | "multiples of 5" | Even/odd suffices | E |
| 19 | B | B Sat | ✓ | ✓ | – | M |
| 20 | A | A 585 | ✓ | ✓ | – | M |
| 21 | B | B 7 | ✓ | ✓ | – | E |
| 22 | C | **A 9** | ✗ | ✗ says 10 | 8 in the honeycomb + 1 separate hexagon | E |
| 23 | A | A < | ✓ | ✓ | Fractions | E |
| 24 | B | B (6 is even) | ✓ | ✓ | – | E |
| 25 | A | A | ✓ | ✓ | Four-digit numbers | M |
| 26 | B | B 64 | ✓ | ✓ | – | E |
| 27 | C | C 10 | ✓ | ✓ (1+2+3+4) | – | M |
| 28 | C | C PO | ✓ | ✓ | Letter coding | M |
| 29 | B | B 6 | ✓ | "formed by overlaps" is meaningless | Translucent colour fills; weak in greyscale | M |
| 30 | B | B 5 | ✓ | ✓ | – | E |
