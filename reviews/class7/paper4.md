# Review: AMO Level 1, Class 7, Practice Paper 4

**Verdict:** The paper is strong and ready after small fixes. I re-solved all 45 keys and every one is correct, with exactly one correct option each. Every figure matches its stem. The blueprint, the difficulty split (24 Easy + 16 Medium in Section I) and the Section II pairings all match the brief. The one fix that matters most is in Q43, where the stem starts with a numeral and contradicts itself. Most other fixes are numeral-led sentences in the solutions.

**Key distribution:** A 11 (1, 2, 5, 10, 14, 20, 22, 30, 36, 37, 44) · B 11 (4, 7, 11, 16, 19, 25, 28, 31, 34, 38, 41) · C 11 (3, 8, 9, 15, 17, 18, 23, 29, 35, 39, 42) · D 12 (6, 12, 13, 21, 24, 26, 27, 32, 33, 40, 43, 45). The spread is balanced.

## Errors (must fix)
| Q | Problem | Fix |
|---|---|---|
| Q43 | The stem breaks a house rule because a sentence starts with a numeral ("3 big candles have…"). It is also self-contradictory: "She packs a box with some big candles" is followed by "The box has twice as many small candles as big candles", so the reader cannot tell whether the box holds small candles. The key (D) 36 is correct. | Rewrite the stem as shown in the Language table and in fixes.json. |

No question has a wrong key, a wrong solution, an ambiguous answer or an out-of-syllabus topic.

## Language & clarity
| Q | Current wording | Issue | Suggested rewrite (full text) |
|---|---|---|---|
| Q43 | "…from the same wax. 3 big candles have the same mass as 5 small candles. … She packs a box with some big candles. The box has twice as many small candles as big candles. …" | A sentence starts with a numeral, and the box contents are contradictory. | Garima makes big candles and small candles from the same wax. The mass of 3 big candles is the same as the mass of 5 small candles. A small candle has a mass of 60 g. She packs a box with big and small candles. The box has twice as many small candles as big candles. Together they have a mass of 2,640 g. How many candles are in the box? |
| Q45 | "x is a rational number greater than −2/3 and less than −1/3." | The sentence starts with a lower-case variable. The plain-text "x" is also upright while the equation's x is italic. | A rational number x is greater than −2/3 and less than −1/3. On the number line, x and 4x + 5/2 are at the same distance from 0. What is the value of x? (Also italicise every x in the stem.) |
| Q27 | "the cuboid container shown, 70 cm long, 33 cm wide and 20 cm high is full of milk" | The parenthetical has no closing comma. | At a milk dairy, the cuboid container shown, 70 cm long, 33 cm wide and 20 cm high, is full of milk. All the milk is poured into cylindrical tubs like the one shown, of radius 7 cm and height 6 cm. How many tubs can be filled completely? Use π = 22/7. |
| Q20 | "What is the size of ∠ABE, marked "?"" | The question has no question mark of its own; the quoted "?" stands in for it. | In the figure, ABCD is a square and BCE is an equilateral triangle drawn outside the square on the side BC. What is the size of ∠ABE (marked "?")? |
| Q17 (solution) | "5n − 12 = 3n + 10, so…" | The solution uses n without defining it and starts with a numeral. | Let the number be n. Then 5n − 12 = 3n + 10, so 2n = 22 and n = 11. Check: 55 − 12 = 43 and 33 + 10 = 43. |
| Q14 (solution) | "… = 3x + 5 cm." | Without brackets, "cm" attaches only to 5, and the result does not match option (A). | Left = (5x + 3) − 2(x − 1) = 5x + 3 − 2x + 2 = (3x + 5) cm. |
| Q6, Q7, Q8, Q18, Q29, Q35, Q36, Q45 (solutions) | For example: "6% of 450 = …", "7 + x must be…", "14 students have 1 pet…", "4 kg of apples…", "123,456 has six digits…", "4x + 5/2 = x gives…" | These solution sentences start with a numeral (house rule). | Add a lead-in word, for example "The cracked eggs are 6% of 450 = …", "The sum 7 + x must…", "There are 14 students with 1 pet…", "Then 4 kg of apples…", "Since ₹2,880 ÷ ₹960 = 3, she buys…", "The number 123,456 has…", "If 4x + 5/2 = x, then…". The exact replacements are in fixes.json. |
| Q41 (solution) | "Only 32 divides by 4" | The usage is wrong. | Only 32 is divisible by 4, so b = 9 and there are 23 red counters. |

## Figures
| Q | Issue | Fix |
|---|---|---|
| Q20 | The single arc at B runs from BA to BE, which is correct. The "?" sits inside the square, just left of BC, so a reader may take it to mean ∠ABC. This is minor. | Move the "?" to sit on the arc near its middle, or just outside the square above BC. Optionally add the 90° square at B inside the arc. |
| Q45 | The x in the stem's text runs is upright, while the x in the equation is italic. | Italicise x throughout. (This is a formatting fix only.) |

The other figures were checked and are correct:
- Q19: the parallelogram has single and double parallel arrows, and AB is labelled 9 cm.
- Q20: the square shows right-angle marks and equal-side ticks, and the triangle shows equal ticks.
- Q21: l ∥ m is marked by arrows. The 48° is between l and AB, x = ∠BAC, and 115° = ∠ACD with D to the right of C.
- Q22: the kite has single ticks on AB and AD and double ticks on CB and CD.
- Q25: the rise of 2 cm, 20 cm and 15 cm are labelled.
- Q26: 5 cm corners are cut from a 30 × 20 card.
- Q27: the cuboid and cylinder are labelled with their dimensions.
- Q28: the y-axis starts at 0 in steps of 20, all values sit on gridlines, there is a title and axis labels, and hatching makes it readable in greyscale.
- Q29: the frequency total is 40.
- Q30: the sector angles add up to 360° and the sectors are hatched.
- Q39: the grid is 4 × 2, so C(6,2) = 15.
- Q40: the grid has rows of 7 and an example square.
- Q44: the tick marks show OA = OC (single) and OB = OD (double), CD = 35 cm, and the seat is 6 cm thick.

## Syllabus / level / difficulty
- The blueprint matches exactly: Ch1 ×4, Ch2 ×3, Ch3 ×5, Ch4 ×5, Ch5 ×5, Ch6 ×5, Ch8 ×3, Ch9 ×5, Ch10 ×5.
- Section I has 24 Easy and 16 Medium questions, as the brief requires.
- The Section II pairings match the brief: Q41 Ch4+Ch10, Q42 Ch3+Ch10, Q43 Ch4+Ch9, Q44 Ch5+Ch6 (SAS congruence and cylinder), Q45 Ch1+Ch4.
- Calculations stay within the ceiling. Q27's 46,200 ÷ 924 is a 5-digit ÷ 3-digit division. Q44's 17.5 × 17.5 is in Section II and is acceptable there.
- Q2 is labelled Easy but needs an LCM and subtraction of a negative, so it is closer to Medium. If anything is relabelled, swap Q2 to Medium and Q36 or Q38 to Easy. This is optional.
- Q42's distractor (B) 3 has no obvious common-mistake origin. Consider 5 (counting only multiples of 4) or 10 (including 10 or 30). This is optional.
- No question is pure aptitude. Q39 (grid routes) and Q40 (calendar-style grid) count as Ch10 casework and patterns.

## Questions with no issues
Q1, Q2, Q3, Q4, Q5, Q9, Q10, Q11, Q12, Q13, Q15, Q16, Q19, Q21, Q22, Q23, Q24, Q25, Q26, Q28, Q30, Q31, Q32, Q33, Q34, Q37, Q38, Q39, Q40, Q42, Q44

## Topic list
- Q1 — Ch1 rationals: comparison on a number line — which point lies left of −5/8
- Q2 — Ch1 operations on rationals — distance between −5/6 and 3/8
- Q3 — Ch1 division of rationals — days for a −9/4 m change at −3/8 m/day
- Q4 — Ch1 rationals between two rationals — count p/10 between −2/5 and 3/10
- Q5 — Ch2 standard form — compare four numbers
- Q6 — Ch2 laws of exponents — 3⁵ ÷ 3²
- Q7 — Ch2 standard form — add 3.5×10⁴ + 2.5×10³
- Q8 — Ch3 percentage — eggs not cracked (6% of 450)
- Q9 — Ch3 profit & loss — loss % on ₹1,250 → ₹1,000
- Q10 — Ch3 discount — 20% off two books
- Q11 — Ch3 percentage application — election margin 16% = 112 votes
- Q12 — Ch3 percentage — 25% more, so 20% less
- Q13 — Ch4 expressions — n + (3n − 5)
- Q14 — Ch4 simplification — (5x + 3) − 2(x − 1)
- Q15 — Ch4 linear equations — find the wrong step
- Q16 — Ch4 linear equation word problem — paper collected
- Q17 — Ch4 linear equation — think-of-a-number
- Q18 — Ch5 triangle inequality — smallest whole-number side
- Q19 — Ch5 parallelogram diagonals — perimeter of △AOB
- Q20 — Ch5 square + equilateral triangle — ∠ABE
- Q21 — Ch5 parallel lines + exterior angle — x
- Q22 — Ch5 congruence (SSS) in a kite — ∠ABC
- Q23 — Ch6 volume — cuboid recast as a cube
- Q24 — Ch6 cylinder volume — compare r²h
- Q25 — Ch6 volume by displacement — stone in a tank
- Q26 — Ch6 open box from a card — volume
- Q27 — Ch6 cuboid and cylinder volume — number of tubs
- Q28 — Ch8 double bar graph — greatest difference
- Q29 — Ch8 mode from a frequency table
- Q30 — Ch8 pie chart — total from a sector-angle difference
- Q31 — Ch9 unitary method — rice for 10 people
- Q32 — Ch9 inverse variation — rows of students
- Q33 — Ch9 unit price — best value pack
- Q34 — Ch9 unitary method (two variables) — food for hikers
- Q35 — Ch9 ratio — apples and pears cost
- Q36 — Ch10 number pattern — 123,456 × 8 + 6
- Q37 — Ch10 casework — 3-digit palindromes divisible by 5
- Q38 — Ch10 pattern n² + 1 — which term is 101
- Q39 — Ch10 casework — lattice routes on a 4 × 2 grid
- Q40 — Ch10 number grid — 2 × 2 square with total 116
- Q41 — Ch4 + Ch10 — counters: red = 2b + 5, total in 31–39 and divisible by 4
- Q42 — Ch3 + Ch10 — whole-rupee discounts on ₹250
- Q43 — Ch4 + Ch9 — candle masses, numbers of big and small candles
- Q44 — Ch5 + Ch6 — SAS congruence gives AB = 35, then cylinder volume
- Q45 — Ch1 + Ch4 — |4x + 5/2| = |x| on an interval of rationals
