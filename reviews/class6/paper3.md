# Review: AMO Level 1, Class 6, Practice Paper 3

**Verdict:** This is a strong paper. I solved all 45 questions independently, and every key and worked solution is correct. Each question has exactly one correct option. Blueprint counts (5/5/5/3/5/5/2/5/5), the 24 Easy + 16 Medium split and the Section II pairings all match the brief. Remaining work: two answer cells that show only a letter, one syllabus concern (Q44) and small language and house-rule fixes.

**Key distribution:** A 11 · B 11 · C 12 · D 11. The spread is balanced, and the longest run of one letter is 3 (C at Q40–Q42).

## Errors (must fix)
| Q | Problem | Fix |
|---|---|---|
| Q8 | Solutions table: the answer cell shows only "(D)" with no option text. | Add "(−9) × (−4) × (−3) × (−1) × 2" after "(D)" (in the JSON as addrun). |
| Q22 | Solutions table: the answer cell shows only "(D)" with no option text. | Add "It is obtuse-angled, and its third angle is 92°." (in the JSON as addrun). |
| Q44 | Syllabus: the question depends on the interior-angle sum formula (n − 2) × 180°. That is NCERT Class 8 (Understanding Quadrilaterals). The Class 6 brief lists only "Polygons (regular, irregular)". | Option 1: keep it as a Star Question and accept it as a stretch. Option 2 (preferred): replace the Ch5 step with Class 6 content, e.g. "A piece of wire is bent to make a regular polygon with 15 sides, each 4 cm…", although that weakens the geometry half. Option 3: base the Ch5 step on angles at a point or in a triangle. Decision needed. This is not in the JSON. |

## Language & clarity
| Q | Current wording | Issue | Suggested rewrite (full text) |
|---|---|---|---|
| Q4 | "He fills sacks that all hold the same mass, as large as possible, and every sack is completely full. Rice and wheat are not mixed in a sack." | It is unclear what "as large as possible" refers to (the sacks or the mass). | "Vikram has 168 kg of rice and 252 kg of wheat. He fills sacks so that every sack is full and holds the same mass, as large as possible. Rice and wheat are not mixed. How many sacks does he fill?" |
| Q14 | "60% of them bought lunch." | House rule: the sentence starts with a numeral. | "On Monday, 250 students came to the school canteen. Of these students, 60% bought lunch. Of the students who bought lunch, 40% chose rice. How many students chose rice?" |
| Q16 | "Her brother has 9 fewer than 4 times as many as Nora." | A noun is missing after "as many". | "…Her brother has 9 fewer than 4 times as many planes as Nora. Which expression gives the number of paper planes her brother has?" |
| Q23 | "What is the size of angle AED, marked "?"?" | The quote marks and double question mark read awkwardly. | "…E is joined to D. What is the size of the marked angle AED?" |
| Q27 | "How deep is the notch, marked "?"?" | The quote marks and double question mark read awkwardly. | "…The perimeter of the new shape is 58 cm. How deep is the notch marked in the figure?" |
| Q36 | "The jumps in this pattern grow in the same way all along." | "All along" is an idiom, and "jumps" is not tied to anything in the pattern. | "The jumps between the numbers in this pattern grow in the same way each time. Which number goes in the blank?" |
| Solutions Q14, Q15, Q16, Q31, Q39, Q43, Q45 | e.g. "−1 is the 8th even-place term…", "144 is 40% of the visitors…", "12 km/h = …", "4 times as many…", "56 = 8 × 7, so…" | House rule: these sentences start with a numeral. | Lead-in words are given for each in paper3_fixes.json ("The number −1…", "These 144 children…", "A speed of 12 km/h…", "Four times…", "Since 56 = 8 × 7…", "First, 30% of 120…", "Lunch: … Rice: …"). Solutions to Q1, Q2, Q30 and others that open with a bare equation (e.g. "792 = …") are left as they are, because they are calculations rather than prose. |

## Figures
| Q | Issue | Fix |
|---|---|---|
| Q27 | The notched rectangle has no right-angle square marks. The brief requires squares rather than inference, and Q24 on the same page does use them. | Add square marks at the corners, or at least at the outer corners and the notch corners. |
| Q30 | The table row header "Number of houses" is not bold, but "Number of letters received" is. | Make both row headers bold. |
| Q20 | Every angle is marked by one full circle around O, so it is less clear which label belongs to which angle (the label positions still make it readable). | Optional: draw a separate arc for each angle. |
| Q23 | Right-angle squares appear at D and C but not at A and B. "Square" is stated in the text, so this is minor. | Optional: none needed. |

I checked every figure. Q19 (only C is reflex; B is obtuse; D is straight), Q20 (drawn angles about 57°/76°/129°/98°, consistent), Q23 (E at about 0.87 of the side height), Q24 (14×4 bar + 4×9 stem = 92), Q25, Q26, Q27 (drawn notch depth about 6 cm), Q28, the Q29 bar graph (10, 20, 15, 25, 30, 20; axes labelled with units, title, starts at 0, values on gridlines, greyscale patterns) and the Q30 table (houses total 30). All of them are consistent with the text and give no answer away.

## Syllabus / level / difficulty
- **Q44:** the polygon angle-sum formula is above the Class 6 level (see Errors).
- **Q35:** combining two ratios (x : y and y : z) goes beyond a "ratio introduction". It is acceptable as Medium, but it is at the top of the level.
- **Q21:** diagonals from one vertex is acceptable under polygons and is a one-step count. The Easy label is fine.
- **Q24 (Easy):** this is really 2 short steps. It can stay Easy, because any relabel would have to be a swap and the 24/16 split is exact.
- **Section II:** pairings match the brief (Q41 Ch4+Ch10 parity, Q42 Ch1+Ch10, Q43 Ch3+Ch9, Q44 Ch5+Ch6, Q45 Ch4+Ch9 TSD). All are genuinely multi-step.
- **Computational ceiling:** respected throughout (largest numbers are 2,40,000 cm³ and 52,30,000). No aptitude-only items.

## Questions with no issues
Q1, Q2, Q3, Q5, Q6, Q7, Q9, Q10, Q11, Q12, Q13, Q17, Q18, Q19, Q20, Q21, Q24, Q25, Q26, Q28, Q29, Q32, Q33, Q34, Q35, Q37, Q38, Q40, Q41, Q42

## Topic list
- Q1 — Ch1 Number system / place value — 52,30,000 in thousands
- Q2 — Ch1 Prime factorisation — 2³ × ? × 11 = 792
- Q3 — Ch1 Integers — greatest negative integer
- Q4 — Ch1 HCF word problem — sacks of rice and wheat
- Q5 — Ch1 Integers on a number line — midpoint of −13 and ?
- Q6 — Ch2 Properties of integers — division by −1
- Q7 — Ch2 Integer division — (−72) ÷ ? = 8
- Q8 — Ch2 Integer multiplication — sign of a product
- Q9 — Ch2 BODMAS with integers — missing operation sign
- Q10 — Ch2 BODMAS nested brackets — find the wrong step
- Q11 — Ch3 F→P conversion — 9/40 as %
- Q12 — Ch3 P→F conversion — 6.25% = 1/16
- Q13 — Ch3 Comparing across forms — 18/25, 0.71, 0.709, 69%
- Q14 — Ch3 Percentage word problem — % of a %
- Q15 — Ch3 Percentage — ?% of 80 = 30% of 120
- Q16 — Ch4 Forming expressions — 4p − 9
- Q17 — Ch4 Substitution with negatives — 2(a − b) − ab
- Q18 — Ch4 Expressions word problem — ticket costs
- Q19 — Ch5 Angle types — identify the reflex angle
- Q20 — Ch5 Angles at a point — find x
- Q21 — Ch5 Polygons — diagonals from one vertex of a decagon
- Q22 — Ch5 Triangle classification — third angle 92°, obtuse
- Q23 — Ch5 Triangles in a square — isosceles angle 75°
- Q24 — Ch6 Area — T-shape of two rectangles
- Q25 — Ch6 Volume — missing height of a cuboid
- Q26 — Ch6 Surface area — closed box
- Q27 — Ch6 Perimeter — notched rectangle, find depth
- Q28 — Ch6 Volume and capacity — tank and buckets
- Q29 — Ch8 Bar graph — months with more than 20 kg
- Q30 — Ch8 Frequency table — total letters
- Q31 — Ch9 Equivalent ratios — 3 : 8 = ? : 56
- Q32 — Ch9 Time–speed–distance — arrival time
- Q33 — Ch9 Ratio sharing — ₹84 in 3 : 4
- Q34 — Ch9 Average speed — relay race
- Q35 — Ch9 Combining ratios — x : z
- Q36 — Ch10 Number pattern — second differences
- Q37 — Ch10 Clock arithmetic — 24-hour clock, 9 hours earlier
- Q38 — Ch10 Parity — odd product of die rolls
- Q39 — Ch10 Interleaved patterns — first negative term
- Q40 — Ch10 Working backwards — card exchange
- Q41 — Section II Ch4 + Ch10 — sum of two terms of 6n − 1
- Q42 — Section II Ch1 + Ch10 — 50 as a sum of three different primes
- Q43 — Section II Ch3 + Ch9 — % and ratio, museum visitors
- Q44 — Section II Ch5 + Ch6 — polygon angle sum → wire → square area
- Q45 — Section II Ch4 + Ch9 — speed expression in metres
