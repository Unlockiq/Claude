# Review: AMO Level 1, Class 10, Practice Paper 5

**Verdict:** Mathematically sound. All 45 keys verified independently, every solution is correct, and every figure matches its stem. No must-fix errors. The fixes are wording only: two numeral-first sentences, one misplaced modifier, AP vocabulary, one weak distractor and one solution that checks a guess instead of deriving the answer.

**Key distribution:** A 11 (3, 7, 10, 12, 16, 22, 24, 30, 34, 40, 44) · B 11 (5, 11, 13, 19, 23, 25, 28, 32, 37, 38, 43) · C 11 (2, 4, 8, 15, 18, 20, 27, 31, 35, 39, 42) · D 12 (1, 6, 9, 14, 17, 21, 26, 29, 33, 36, 41, 45). The longest run of the same letter is 2. The balance is good.

## Errors (must fix)

None. Every key was re-derived. The checks for the hardest items:
- **Q37:** Grid coordinates (row from top, column) are S(4,1), A(1,2), C(1,6), D(2,3) and B(3,5). The Manhattan distances from S are 4, 8, 4 and 5. Only B has odd parity, so B is the only square possible after 9 moves.
- **Q41:** The pairs (p ≤ q) with pq ≤ 12 number 12 + 5 + 2 = 19, so the answer is 20.
- **Q42:** The distances from T are (−6,5) → 10, (18,11) → 20, (20,23) → 30 and (20,11) → √468. Only C works.
- **Q45:** The cylinder holds 616 cm³ and the cone 1,386 cm³. Their HCF is 154. Since 693 = 4.5 × 154, it cannot be reached, while 770, 1,232 and 462 can, as the solution shows.

## Language & clarity

| Q | Current wording | Issue | Suggested rewrite (full text) |
|---|---|---|---|
| Q8 | "Hana starts a workshop that makes fishing nets with ₹60,000." | Misplaced modifier: the workshop seems to make nets "with ₹60,000". | "Hana puts ₹60,000 into a workshop that makes fishing nets. After 3 months, Ivan joins with ₹40,000. …" (rest unchanged) |
| Q9 | "… cost ₹550 in all. 5 front-row tickets and 3 back-row tickets cost ₹650 in all." | Sentence starts with a numeral (house rule). | "… cost ₹550 in all. Also, 5 front-row tickets and 3 back-row tickets cost ₹650 in all. What is the price of one front-row ticket?" |
| Q14 | "The fourth number in an arithmetic progression … the first seven numbers …" | The syllabus term is "term". | "The fourth term of an arithmetic progression is 11. Whatever the common difference is, the first seven terms always add up to the same total. What is that total?" |
| Q26 | "θ is an acute angle, so 0° < θ < 90°." | Sentence starts with a bare symbol. | "The angle θ is acute, so 0° < θ < 90°. Which of these could be the value of sec θ?" |
| Q33 | "25 gardeners can plant all the saplings …" | Sentence starts with a numeral (house rule). | "A team of 25 gardeners can plant all the saplings in a park in 12 days. How many days would 20 gardeners take, all working at the same rate?" |
| Q43 | "the incircle … meets the longest side AB at T" | "Meets" could suggest the circle crosses the side. The tangent term is "touches". | "In the figure, the incircle of right-angled △ABC (∠C = 90°) touches the longest side AB at T, splitting it into AT = 14 cm and TB = 15 cm. How long is the radius r of the incircle?" |
| Q11 (option D) | "20 and −13" | Weak distractor that matches no real mistake. Setting each factor equal to 18 gives 20 and 13. | "20 and 13" |
| Q35 (solution) | "Try the current c: … For c = 5: …" | Checks a guess instead of deriving the answer. The class has quadratics. | "Let the current be c. Then 20/(15 − c) − 20/(15 + c) = 1, so c² + 40c − 225 = 0 = (c − 5)(c + 45) and c = 5 km/h. Check: 20 ÷ 10 = 2 hours, 20 ÷ 20 = 1 hour." |
| Q27 (option A) | "1 , 200 √3 m" (equation object) | The equation object adds a space before the comma, and its font differs from options B–D. | Retype as "1,200√3 m" in the normal font, or keep the equation without the extra space. This needs an equation edit, so it is not in the JSON. |

## Figures

| Q | Issue | Fix |
|---|---|---|
| Q28 | The ogive has no title. Gridlines and readings are fine: the curve passes 12 at 20 marks and 44 at 40 marks, both exactly on gridlines. | Add a title such as "Marks of 60 students (less-than ogive)". |
| Q21 | The top radius has a radius line, but the "3 cm" base label floats below the base with no radius line drawn. | Draw a base radius line from the centre dot and attach "3 cm" to it. |
| Q24 | The "3.5 m" label sits outside the bottom rim with no radius line. The basket under the balloon is decorative. | Draw the bottom radius line and attach "3.5 m" to it. Optionally remove the basket. |

All other figures were checked and are fine. Right angles are marked in Q15, Q19, Q27 and Q43. The Q23 cross-section shows 6 m, 6 m, 3 m, 3 m and h. The Q22 annular sector shows 7 cm, 21 cm and 120°. The Q45 radius lines are drawn. The Q37 board is a 4 × 6 grid. Q17 shows a tangential quadrilateral with PQ = 11 cm.

## Syllabus / level / difficulty

- Blueprint counts are correct: Ch1 3, Ch3 5, Ch4 6, Ch5 5, Ch6 5, Ch7 3, Ch8 3, Ch9 5, Ch10 5. Section II pairings match the brief: Q41 Ch4+Ch10 (pigeonhole), Q42 Ch5+Ch7, Q43 Ch4+Ch5, Q44 Ch3+Ch9, Q45 Ch6+Ch10 (invariant).
- Section I labels give exactly 24 Easy and 16 Medium.
- Computational ceiling: CI is 2 years. Quadratics have integer roots. Coordinates are integers. Trig uses standard angles. GST is 18%, a current slab.
- Rigor guardrail (decision D5): Q9 is plain elimination, now taught at C9 under v5.7 D16. Q33 is one-step inverse proportion and Q36 is a single multiplication. These are allowed as spiral content but sit near SOF/Silverzone level. When the paper is next revised, consider replacing Q9 with a cross-multiplication or reducible-form system.
- Possible level relabels: Q37 (parity insight) reads as Medium, and Q6 (two steps) is borderline Easy. If relabelling, swap within the blueprint: Q37 Easy → Medium with Q39 Medium → Easy (complement counting is one idea). This is optional.
- Distractors: Q35 (A) 20 km/h is faster than the boat itself (15 km/h), which is implausible. Consider 3 km/h or 2.5 km/h. Not in the JSON because no option is clearly a common mistake.
- No aptitude-reasoning items. No out-of-syllabus topics. P&C is not needed: Q36, Q38 and Q39 use only the multiplication principle or listing.

## Questions with no issues

Q1, Q2, Q3, Q4, Q5, Q6, Q7, Q10, Q12, Q13, Q15, Q16, Q17, Q18, Q19, Q20, Q22, Q23, Q25, Q29, Q30, Q31, Q32, Q34, Q36, Q37, Q38, Q39, Q40, Q41, Q42, Q44, Q45

## Topic list

- Q1 — Ch1 HCF/LCM — HCF × LCM = product, gives 84
- Q2 — Ch1 decimal expansions — 7/(2ᵃ·5²) terminates after 5 places, so a = 5
- Q3 — Ch1 FTA — factors of 360 that are multiples of 6 (12)
- Q4 — Ch3 partnership — capitals in ratio 1/2 : 1/3 : 1/5, Usha's share
- Q5 — Ch3 partnership — Kian's capital from the profit shares
- Q6 — Ch3 CI variable rate — second-year rate 12%
- Q7 — Ch3 CI — split ₹22,000 so 1-year and 2-year amounts are equal
- Q8 — Ch3 partnership — capital × time with a withdrawal
- Q9 — Ch4 pair of linear equations — ticket prices by elimination
- Q10 — Ch4 AP sum — number of terms from first, last and sum
- Q11 — Ch4 quadratic — (x − 2)(x + 5) = 18
- Q12 — Ch4 polynomials — division algorithm remainder
- Q13 — Ch4 polynomials — conjugate zero, constant term
- Q14 — Ch4 AP sum — S₇ = 7a₄
- Q15 — Ch5 similarity/BPT — ladder-slide bar length
- Q16 — Ch5 coordinate — square area from a diagonal
- Q17 — Ch5 tangents — tangential quadrilateral side
- Q18 — Ch5 section formula — point 5 units along AB
- Q19 — Ch5 tangents — r² = AP·BQ
- Q20 — Ch6 sector — perimeter of a 72° sector
- Q21 — Ch6 frustum — height from volume
- Q22 — Ch6 sector — annular sector area (wiper)
- Q23 — Ch6 volume conservation — well embankment height
- Q24 — Ch6 combined solids — hemisphere + frustum surface area
- Q25 — Ch7 identities — simplify to 2 cosec θ
- Q26 — Ch7 ratios — range of sec θ for an acute angle
- Q27 — Ch7 heights & distances — aeroplane, 60° to 30°
- Q28 — Ch8 ogive — read cumulative frequencies
- Q29 — Ch8 probability — exactly one rainy day of two
- Q30 — Ch8 probability — two cards without replacement, even sum
- Q31 — Ch9 break-even — day pass vs hourly
- Q32 — Ch9 discount stacking — second discount
- Q33 — Ch9 time & work — gardener-days
- Q34 — Ch9 GST — input tax credit
- Q35 — Ch9 boats & streams — speed of the current
- Q36 — Ch10 counting — two people, distinct floors
- Q37 — Ch10 invariant — chessboard parity
- Q38 — Ch10 counting — three-digit numbers with digit sum 3
- Q39 — Ch10 counting — complement, at least one 7
- Q40 — Ch10 extremal — independent tiles on a 5 × 5 grid
- Q41 — Ch4 + Ch10 — pigeonhole on quadratics with c ≤ 12
- Q42 — Ch5 + Ch7 — distance formula + angle of elevation
- Q43 — Ch4 + Ch5 — incircle of a right triangle, quadratic in r
- Q44 — Ch3 + Ch9 — GST-inclusive sales, partnership with interest on capital
- Q45 — Ch6 + Ch10 — water-jug invariant with cylinder and cone volumes
