# Review — AMO Level 1, Class 6, Practice Paper 1

## Verdict
Strong paper. I solved all 45 questions and each key is correct, with exactly one correct option. The blueprint (5/5/5/3/5/5/2/5/5) and the Section II pairings match the brief, and Section I has exactly 24 Easy and 16 Medium. What needs work is small: one answer cell shows only a letter (Q20), two stems start a sentence with a numeral (Q15, Q28), one figure has a stray mark (Q19), and there is some solution-wording polish.

Key distribution: A = 11, B = 12, C = 11, D = 11 (balanced; no long runs).

## Errors (must fix)
| Q | Problem | Fix |
|---|---|---|
| Q20 | The answer cell in the solutions table shows only "(D)" with no option text. | Add "obtuse-angled and isosceles" (addrun in fixes JSON). |
| Q19 | Figure: a stray "O" (a circle or letter) sits on the upper-left arm, away from the vertex, and overlaps the start of the "?" arc. The stem names no point O. | Redraw: remove the mark (or put the vertex label at the actual vertex) so the arc start is clear. |

No wrong keys, wrong solutions, multiple-correct or no-correct options, or out-of-ceiling items were found.

## Language & clarity
| Q | Current wording | Issue | Suggested rewrite (full text) |
|---|---|---|---|
| Q6 | "…" Which expression does this? | "does this" is vague | "Subtract 4 from 9. Multiply the result by 3. Then subtract this answer from 30." Which expression matches these steps? |
| Q15 | A school library has 640 books. 3/8 of them are storybooks and 45% are science books. … | The sentence starts with a numeral (fraction) | A school library has 640 books. Of these books, 3/8 are storybooks and 45% are science books. All the other books are maths books. How many maths books are there? |
| Q28 | …20 m long and 8 m wide, and straight sides. 32,000 litres of water are pumped into it. … (1 cubic metre = 1,000 litres) | The sentence starts with a numeral; "straight sides" is unclear; the bracketed note is not a sentence | A swimming pool has a rectangular floor 20 m long and 8 m wide, and its sides are vertical. Then 32,000 litres of water are pumped into it. By how many centimetres does the water level rise? Use 1 cubic metre = 1,000 litres. |
| Q33 | …with the distance between stops. | Should be plural | The map shows the route of a school bus from stop P to stop S, with the distances between stops. The bus takes 36 minutes from P to S. What is its average speed? |
| Q36 | Figure 1 has 1 dot, and the numbers of dots go on growing in the same way. | Awkward wording | Look at the pattern of dot figures. Figure 1 has 1 dot, and the pattern keeps growing in the same way. How many dots will Figure 5 have? |
| Q21 (option D) | 247° | Implausible distractor: an angle on a straight line cannot be 247° | 132° (= 180° − 48°, forgetting the 65°) |
| Solutions Q3, Q5, Q11, Q13, Q14, Q16, Q28, Q29, Q31, Q33, Q40, Q43 | e.g. "−4 comes just after −5…", "36 of the 100 small squares…", "139 is 9 more…", "36 km is left…" | Sentences start with a numeral (house rule) | Lead-in words added ("The integer −4…", "There are 36 shaded squares…", "The number 139…", "Then 36 km…", "Check:", "So the ratio is…"); full text is in paper1_fixes.json |

Minor, not in the JSON: solutions write fractions as 3/8 or 36/60 inline, while the brief prefers ÷ notation up to C6. This is acceptable in a key, but the fraction objects could be used instead.

## Figures
| Q | Issue | Fix |
|---|---|---|
| Q19 | Stray "O" mark on the arm (see Errors). | Remove or reposition. |
| Q7 | Only even ticks are numbered; odd ticks are unlabelled (the brief says every tick is numbered except the one asked about). | Optional: number every tick, or accept a labelling interval of 2 as a scale convention. |
| Q3 | Four lettered ticks (A, B, D, C) where the rule expects one unlabelled tick. | Acceptable because the question is built on it; no change needed. |
| Q23 | The 115° arc overlaps the vertex label "C". | Move the label C below or left of the vertex. |
| Q37 | The minute hands run across the numerals "2" and "7" and partly hide them. | Shorten the minute hand or draw it under the numerals. |
| Q22 | Two vertices (upper-left and upper-right, next to A) are almost straight (angles close to 180°), so the 9 sides are hard to see. The count is given in the stem, so the question still works. | Optional: make those corners more visible. |
| Q11 | The very light blue shading may disappear in greyscale print. | Use a darker tint or hatching. |
| Q30 | The "?" cell is left-aligned while the numbers are right-aligned; the row header is not bold. | Cosmetic: centre the cells and make the header bold. |
| Q36 | The labels "Figure 1" and "Figure 2" are crowded together. | Add spacing. |

Verified by counting or measuring: Q1 abacus = 30,62,054 (3,0,6,2,0,5,4 beads). Q2 tree leaves = 2,2,5,3,3,11. Q3 points A = −6, B = −4, D = −3, C = 4. Q7 has four jumps of −3 ending at −12. Q11 has 36 shaded squares (6×4 + 4×3). Q21 angles measure about 48° and 66°. Q22 has 9 vertices and 6 dashed diagonals. Q29 bars are 25, 40, 15, 35, 30. Q31 has 8 dark and 10 white tiles. Q36 dots are 1, 5, 13, 25. Q37 shows 9:10 and 9:35 (hour hands placed correctly). Q40 table is boustrophedon. Q44 has right-angle squares at the base, and the 7 cm and 12 cm are given.

## Syllabus / level / difficulty
- Blueprint counts per chapter match exactly, and Section II pairings match (Q41 Ch4+Ch10 parity, Q42 Ch1+Ch10 working backwards, Q43 Ch3+Ch9 TSD, Q44 Ch5+Ch6, Q45 Ch4+Ch9 TSD).
- Section I has 24 Easy and 16 Medium, which is correct. Possible swap (optional): Q36 (second-difference pattern) and Q38 (working backwards in 2 steps) are labelled Easy but feel Medium; Q10 or Q26 could go to Easy in exchange. Swap only in pairs.
- Q22 (angle sum of a polygon) is NCERT Class 8 content. It is reachable here through the drawn triangulation, so it is acceptable as an olympiad stretch under "Polygons", but it is the most advanced Section I item.
- Exponent notation (2³, p², n²) in Q2, Q5, Q17 and Q41 is fine with "prime factorisation (advanced)" and substitution.
- Q27 needs guess-and-check with the options ((20−w)(15−w) = 234). This is fine at Medium.
- No pure aptitude items. All computation is within the C6 ceiling.

## Questions with no issues
Q1, Q2, Q4, Q5 (stem), Q8, Q9, Q10, Q12, Q13 (stem), Q14 (stem), Q16 (stem), Q17, Q18, Q24, Q25, Q26, Q27, Q29 (stem), Q30, Q31 (stem), Q32, Q34, Q35, Q38, Q39, Q41, Q42, Q44, Q45.

## Topic list
- Q1 — Ch1 place value — read a 7-digit number from an abacus
- Q2 — Ch1 prime factorisation — factor tree of 1,980
- Q3 — Ch1 integers — locate −4 on a number line
- Q4 — Ch1 LCM word problem — marbles in jars of 15/20, 100–150
- Q5 — Ch1 factors — which is not a factor of 2³×3²×7
- Q6 — Ch2 BODMAS — words to bracketed expression
- Q7 — Ch2 integer multiplication — jumps on a number line
- Q8 — Ch2 distributive property — (−8)×37 + (−8)×63
- Q9 — Ch2 nested brackets — missing number
- Q10 — Ch2 integer operations — quiz score with negative marking
- Q11 — Ch3 F-D-P — hundred grid as a decimal and a percentage
- Q12 — Ch3 equivalence — how many equal 3/5
- Q13 — Ch3 percentage — 64% of 2,500 L
- Q14 — Ch3 comparing forms — true inequality
- Q15 — Ch3 fraction and % word problem — maths books in a library
- Q16 — Ch4 expressions — function-machine rule 3n+2
- Q17 — Ch4 substitution — p² − 2q with negative p
- Q18 — Ch4 forming an expression — boxes of cookies sold
- Q19 — Ch5 angles — reflex angle 230°
- Q20 — Ch5 triangle classification — obtuse isosceles
- Q21 — Ch5 angles on a straight line — angle COD
- Q22 — Ch5 polygons — interior-angle sum of a 9-gon
- Q23 — Ch5 triangles — isosceles with an exterior angle
- Q24 — Ch6 area — card with a window cut out
- Q25 — Ch6 volume — cube from a net
- Q26 — Ch6 perimeter with mixed units — ribbon round a board
- Q27 — Ch6 area — path width in a garden
- Q28 — Ch6 volume/capacity — water-level rise in a pool
- Q29 — Ch8 bar graph — most minus fewest kites
- Q30 — Ch8 frequency table — missing frequency, 2 or more siblings
- Q31 — Ch9 ratio — dark to white tiles
- Q32 — Ch9 ratio — apple to pear trees from a fraction
- Q33 — Ch9 TSD — average speed on a bus route
- Q34 — Ch9 TSD — two vans, same direction, gap of 6 km
- Q35 — Ch9 ratio — stamps 7:3, equal after a transfer
- Q36 — Ch10 patterns — diamond dot figures
- Q37 — Ch10 clock — angle turned by the minute hand
- Q38 — Ch10 working backwards — notebooks sold
- Q39 — Ch10 parity — possible leg totals
- Q40 — Ch10 patterns — snake numbering, column of 139
- Q41 — Ch4+Ch10 — parity of expressions in n
- Q42 — Ch1+Ch10 — working backwards with integers
- Q43 — Ch3+Ch9 — % of trip, required speed
- Q44 — Ch5+Ch6 — perimeter of a rectangle with an equilateral triangle on top
- Q45 — Ch4+Ch9 — average speed as an expression
