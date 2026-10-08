# Review — AMO Level 1, Class 10, Practice Paper 2

## Verdict
Mathematically sound: all 45 keys verified independently and each has exactly one correct option. The blueprint is exact (3/5/6/5/5/3/3/5/5; 24 Easy + 16 Medium; Section II pairings Ch4+10, Ch5+7, Ch4+5, Ch3+9, Ch6+10 all match). No must-fix maths errors. The fixes are seven answer cells that show only a letter, Q11 sentences that start with a numeral, a Q44 option set that gives away the "which way" part, and small solution and figure polish.

Key distribution: A 11 · B 11 · C 11 · D 12 (A: 2,6,11,16,19,23,26,30,34,38,43; B: 3,8,12,15,20,21,28,29,36,37,44; C: 4,5,9,14,18,24,27,31,33,40,42; D: 1,7,10,13,17,22,25,32,35,39,41,45).

## Errors (must fix)
| Q | Problem | Fix |
|---|---|---|
| Q5, Q8, Q9, Q20, Q30, Q31 (answer key) | The solution "Answer" cell shows only the letter, e.g. "(C)", with no option text. Q9's option is an equation object, so the cell is empty after the letter. | Add the option text as a run (addrun items in the JSON): Q5 "Jai ₹45,000 for 8 months; Gita ₹36,000 for 10 months"; Q8 "10% per year, compounded half-yearly"; Q9 "9x² − 30x + 25 = 0"; Q20 "radius 21 cm, angle 45°"; Q30 "a head, or a number from 3 to 6"; Q31 "10% off, then a further 25% off". |

No wrong keys, wrong solutions, multiple-correct items or out-of-syllabus items were found. Checks done:
- Q8: B 66,150 beats A 66,144, but only by ₹6.
- Q30: the options are 10/12, 8/12, 9/12 and 5/12.
- Q40: the 7 triangles were enumerated by hand.
- Q41: the tens-digit groups are 3,3,4,3,3,4,3,1 (sum 24), so 22 + 1 = 23.
- Q45: a brute-force search over all factorisations of 616 gives 442 (7×8×11), then 508 and 540.

## Language & clarity
| Q | Current wording | Issue | Suggested rewrite (full text) |
|---|---|---|---|
| Q11 | "…together cost ₹310. 1 kg of apples and 1 kg of bananas cost ₹190. 1 kg of bananas and 1 kg of grapes cost ₹170. …" | Two sentences start with a numeral (house rule). | "At a fruit market, 1 kg of apples, 1 kg of bananas and 1 kg of grapes together cost ₹310. Apples and bananas, 1 kg each, cost ₹190. Bananas and grapes, 1 kg each, cost ₹170. What is the price of 1 kg of bananas?" |
| Q44 | Options: "Paying later, by ₹1,180 / ₹562 / ₹382 / ₹400" | All four options say "Paying later", so the "Which way…" half of the stem is given away. | Change (C) to "Paying now, by ₹562" (sign-error distractor). Key stays (B). |
| Q30 | (D) "a tail with a number less than 6" | "with" is vague. The event is an AND event and should read clearly against the "or" options. | "a tail and a number less than 6" |
| Q43 | "…drawn from the right-angled corner to the longest side." | "Corner" is informal; the syllabus term is "vertex". | "A perpendicular is drawn from the vertex of the right angle to the longest side." |
| Q40 | "…a perimeter of 15 cm?" | "15" and "cm" break across lines. | Use a non-breaking space: "15 cm". |
| Q2, Q14, Q16, Q24, Q36, Q37 (solutions) | e.g. "150 = 2 × 3 × 5²…", "32 birds can sit…", "50 multiples of 2…" | The solution sentences start with numerals, and Q37 is not a complete sentence. | Q2 "Here 150 = …"; Q14 "S₁₀ = S₁₅ gives 5(96 + 9d) = 7.5(96 + 14d), so d = −4. …"; Q16 "The ratios 6/4 = 9/6 = 12/8 = 1.5 are equal, so the triangles are similar (SSS similarity)."; Q24 see next row; Q36 "With 32 birds, each nest can hold 4, so 32 is not enough. …"; Q37 "There are 50 multiples of 2 …". |
| Q24 (solution) | "…: 1,176 + 154 = 1,330 cm²." | The net "+154" hides the step of subtracting 154 and adding 308. | "The cube gives 6 × 196 = 1,176. Subtract the hidden circle 154 and add the curved surface 2 × 154 = 308: 1,176 − 154 + 308 = 1,330 cm²." |
| Q8 (solution) | "The amounts are ₹66,150 (…), ₹64,896 (…), ₹66,144 (…) and ₹66,000." | The amounts are listed in the order B, C, A, D with no labels. A and B differ by only ₹6, so the student needs to see which amount belongs to which option. | "Amounts: (A) 60,000 × 1.04 × 1.06 = ₹66,144; (B) 60,000 × 1.05 × 1.05 = ₹66,150; (C) 60,000 × 1.04 × 1.04 = ₹64,896; (D) ₹66,000. Scheme (B) gives the most." |
| Q17 (solution) | "M = ((2 × A + B) ÷ 3), …" | Redundant brackets, and the formula used is not named. | "By the section formula, M = (2A + B) ÷ 3, so B = 3M − 2A = (3 + 2, 6 − 8) = (5, −2)." |

## Figures
| Q | Issue | Fix |
|---|---|---|
| Q21 | The "3 cm" label sits below the cup, away from the dashed bottom radius, so it could be read as the base diameter. | Place "3 cm" on or just above the dashed bottom radius. |
| Q24 | The hemisphere radius (7 cm) is not labelled, and the hemisphere's base rim looks slightly lifted off the top face. | Add a radius line labelled "7 cm" and seat the rim on the top face. The text already gives 7 cm, so no text change is needed. |
| Q27 | The left "10 m" label overlaps the left wall's outline. | Move the label to the right of the solid ladder line. |
| Q28 | The row header "Number of fish" is not bold, but the brief requires bold headers. | Make the row header bold. |
| Q22 | The "6 cm" label floats above the top face rather than on the radius line. Minor. | Put the label on the radius line. |

Checked and fine:
- Q18 shows the right-angle squares at A and B and has "?" at ∠OAB.
- Q19 marks the equal angles at D and C, and AD = DB are drawn equal.
- Q42 is to scale: the height/BC ratio is about 1/3, D and E sit at about 1/3 of the way from A, and DE carries the parallel arrows.
- Q23 and Q45 have correct labels, and the right angles are marked.

## Syllabus / level / difficulty
- All topics sit in the v5.6/5.7 Class 10 board re-base or in the spiral:
  - Ch1: FTA, terminating decimals, Euclid.
  - Ch3: half-yearly CI/depreciation for 1 year, which is within the ceiling, and partnership.
  - Ch4: discriminant, AP sum, 3-variable system, polynomial zeroes.
  - Ch5: distance, section formula, similarity, tangents.
  - Ch6: sector, frustum, recasting, combined solid.
  - Ch7: identities, standard angles, heights and distances.
  - Ch8: grouped mean, compound probability.
  - Ch9: discount stacking, T&W, GST, pipes, boats.
  - Ch10: pigeonhole, inclusion–exclusion, invariant game, extremal, counting.
- None of the relocated C11 content appears (complex numbers, P&C, straight lines, compound angles).
- Q33 GST: 9% SGST + 9% CGST = 18%, which is a current slab (5/18/40). The fact is correct.
- Q38 is labelled Easy. It is really a two-step invariant argument and fits Medium better. If relabelled, swap it with Q12 (Medium → Easy; a one-step product-of-zeroes) to keep the 24 Easy + 16 Medium count. Optional.
- Rigor guardrail (D5): Q6, Q10, Q15, Q16, Q36 and Q37 are close to standard SOF/board level. That is acceptable for Easy slots, but consider sharpening one or two in a later revision.
- Q44 does not use partnership or T&W as the pairing note mentions, but CI combined with cost-benefit fits Ch3 + Ch9 (NEP 4.6), so this is fine.

## Questions with no issues
Q1, Q3, Q4, Q6, Q7, Q10, Q12, Q13, Q15, Q18, Q19, Q23, Q25, Q26, Q29, Q32, Q33, Q34, Q35, Q39, Q41, Q42, Q45.

## Topic list
- Q1 — Ch1 FTA — HCF from prime factorisations
- Q2 — Ch1 decimal expansions — k/150 terminating
- Q3 — Ch1 Euclid's algorithm — reconstruct a from steps
- Q4 — Ch3 CI (half-yearly depreciation) — machine value after 1 year
- Q5 — Ch3 partnership — which plan gives equal shares
- Q6 — Ch3 partnership — profit ratio from capital and time ratios
- Q7 — Ch3 partnership — added capital mid-year, share of profit
- Q8 — Ch3 CI — compare half-yearly/yearly/variable-rate schemes
- Q9 — Ch4 quadratics — discriminant zero
- Q10 — Ch4 AP — which number is a term
- Q11 — Ch4 linear equations (3-variable) — price of bananas
- Q12 — Ch4 polynomials — third zero from product of zeroes
- Q13 — Ch4 quadratics — rows of desks
- Q14 — Ch4 AP sum — S10 = S15, find S25
- Q15 — Ch5 distance formula — point at distance 13
- Q16 — Ch5 similarity — SSS similar sides
- Q17 — Ch5 section formula — find endpoint B
- Q18 — Ch5 tangents — ∠OAB from ∠APB
- Q19 — Ch5 similarity (AA) — length AC
- Q20 — Ch6 sector area — compare four sectors
- Q21 — Ch6 frustum volume — paper cup
- Q22 — Ch6 volume conservation — cylinder into hemispherical bowls
- Q23 — Ch6 sector — radius from arc length and area
- Q24 — Ch6 combined solid — cube + hemisphere TSA
- Q25 — Ch7 standard angles — greatest value
- Q26 — Ch7 identities — sin⁴θ − cos⁴θ
- Q27 — Ch7 heights & distances — ladder between two walls
- Q28 — Ch8 grouped mean — fish lengths
- Q29 — Ch8 compound probability — two bowls, both white
- Q30 — Ch8 compound probability — coin + die events
- Q31 — Ch9 discount stacking — lowest price
- Q32 — Ch9 time & work — Rekha alone
- Q33 — Ch9 GST — price from SGST
- Q34 — Ch9 pipes & cisterns — leak empties tank
- Q35 — Ch9 boats & streams — boats meet
- Q36 — Ch10 pigeonhole — birds in nests
- Q37 — Ch10 combinatorial counting — divisible by 2 or 5
- Q38 — Ch10 invariants / game — matchstick strategy
- Q39 — Ch10 extremal — tug-of-war teams with ≥4 wins
- Q40 — Ch10 counting — integer triangles of perimeter 15
- Q41 — Ch4 + Ch10 — AP berths + pigeonhole on tens digit
- Q42 — Ch5 + Ch7 — BPT + 30° height, trapezium area
- Q43 — Ch4 + Ch5 — AP right triangle, altitude to hypotenuse
- Q44 — Ch3 + Ch9 — CI half-yearly vs discount decision
- Q45 — Ch6 + Ch10 — cone recast to integer cuboid, minimal surface
