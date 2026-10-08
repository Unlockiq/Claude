# AMO Level 1 — Class 10 — Practice Paper 3 — Review

**Verdict:** Sound paper. I solved all 45 independently and every key is correct, with exactly one correct option and a correct worked solution each time. There are no must-fix maths errors. The fixes are language only: two stems open with a numeral, Q37 uses vague "could see", and several solutions need small wording changes. One figure needs a right-angle mark (Q27). Blueprint counts, the 24 Easy + 16 Medium split and the Section II pairings all match the brief.

**Key distribution:** A 11 · B 11 · C 11 · D 12 (45). No long runs of the same letter.

## Errors (must fix)

None. Checks done: Q11 system has the unique solution (1, 2, 3), so x + y + z = 6 holds. Q19: the crossing point is 8 m from the 10 m pole, and the figure puts it at 40% of the gap, which is consistent. Q42 figure: M is at 0.24 of AB from A, which fits AM : MB = 1 : 3. Q43: both (2, 0) and (4, 0) give a dot product of 0. Q45: a = 1 sphere and b = 18 cones gives 19, and 21 would need 0 spheres. Q40: a parity argument and the sequence 12 → 7 → 2 → 5 → 0 are both valid.

## Language & clarity

| Q | Current wording | Issue | Suggested rewrite (full text) |
|---|---|---|---|
| Q6 | "Vidya empties her piggy bank and deposits ₹26,000 for 2 years…" | ₹26,000 from a piggy bank is not a plausible amount | "Vidya deposits her savings of ₹26,000 for 2 years at 5% per year, compounded yearly. The interest she earns is □. Which amount completes the statement?" |
| Q26 | "3θ − 15° is an acute angle and tan(3θ − 15°) = 1. Then θ = □." | Sentence starts with a numeral | "The angle 3θ − 15° is acute and tan(3θ − 15°) = 1. Then θ = □. Which angle goes in the box?" |
| Q37 | "On a museum visit, 35 students could see the science gallery, the art gallery, both or neither. 28 students saw…" | "could see" is vague (were they allowed to, or did they?). The second sentence starts with a numeral | "On a museum visit, each of 35 students saw the science gallery, the art gallery, both or neither. Of them, 28 saw the science gallery and 25 saw the art gallery. What is the least possible number of students who saw both galleries?" |
| Q37 sol | "… 18 is possible when every student saw a gallery." | Starts with a numeral | "… This is possible when every student saw a gallery." |
| Q38 sol | "(A sends to B and B sends to A are different messages.)" | Ungrammatical | "(A message from A to B and one from B to A are different.)" |
| Q39 sol | "0, 1, 2, 3, 4, 5 show that 6 are not." | Starts with a numeral | "The numbers 0, 1, 2, 3, 4, 5 show that 6 are not." |
| Q40 sol | "…; 2 moves turn at most 10 cards. 4 moves work: …" | Starts with a numeral | "…; two moves turn at most 10 cards. Four moves work: 12 → 7 → 2 → 5 → 0 face-up cards." |

All of these are in `paper3_fixes.json`, and I checked that each "old" string matches a run in runs3.txt. The solutions to Q2, Q12, Q16 and Q30 open with an equation such as "8² + (k − 2)² = 10²". I left these unchanged because they read as displayed working, not prose.

## Figures

| Q | Issue | Fix |
|---|---|---|
| Q27 | No right-angle square where the building's front face meets the ground. The solution needs that right angle (tan 30°, tan 60° over 24 m), and the visual rules say right angles must be marked. | Add a right-angle square at the foot of the building's front face, below B. |
| Q24 | The "21 cm" label overlaps the top rim ellipse, so it is hard to read. | Move "21 cm" just above the radius line, clear of the rim. |
| Q30 (table) | The row header "Number of students" is not bold, but "Time (minutes)" is. The brief says headers must be bold. | Make "Number of students" bold. |
| Q23 (minor) | The tick for the "7 m" width runs into the label. | Shift the label slightly up or sideways. |

Figures with no issues: Q17 (right angles at A, B and P are marked; 5 cm is given), Q19, Q20, Q22, Q42 (right angle at O is marked) and Q43.

## Syllabus / level / difficulty

- **Section I blueprint:** Ch1 3 · Ch3 5 · Ch4 6 · Ch5 5 · Ch6 5 · Ch7 3 · Ch8 3 · Ch9 5 · Ch10 5 = 40, which matches the brief. There are 24 Easy and 16 Medium, which is also correct. Every Section I question stays within one chapter.
- **Section II pairings match the brief:** Q41 Ch4+Ch10, Q42 Ch5+Ch7, Q43 Ch4+Ch5, Q44 Ch3+Ch9, Q45 Ch6+Ch10. Q41 is AP counting, not the "pigeonhole applied" item the brief suggests. Counting still counts as Ch10 combinatorial reasoning, so this is acceptable.
- **Computational ceiling respected:**
  - Q7 and Q44 use half-yearly compounding for 1 year only.
  - Q5 covers years 2–3, within the 3-year limit.
  - Q14 is completing the square with integer values.
  - Q26 uses a standard angle.
  - Coordinates are all integers.
- **No relocated C11 topics appear** (complex numbers, straight-line equations, compound angles, P&C formulas, SD). Q36, Q38 and Q41 use only the multiplication principle and a direct count, which is acceptable as Ch10 reasoning.
- **GST (Q34):** the 18% slab is current (5/18/40) and the CGST/SGST split is correct.
- **AP coverage:** Q10 and Q13 use only the middle-term property, which is C9 content and allowed as spiral. Ch4 Section I has no item on the C10-specific AP sum formula. Consider swapping one of them for a sum-of-n-terms item in a later revision (optional).
- **D5 guardrail ("harder than SOF/Silverzone"):** Q2, Q15, Q21, Q26 and Q33 are NCERT-exercise level. They are fine as Easy items but give little olympiad lift.
- **Q25** is labelled Easy but needs two steps (factorise, then simplify). It is borderline. Any relabel would need a swap within Ch7, and Q26 is the only clear 1-step item there, so I would leave it.

## Questions with no issues

Q1, Q2, Q3, Q4, Q5, Q7, Q8, Q9, Q10, Q11, Q12, Q13, Q14, Q15, Q16, Q17, Q18, Q19, Q20, Q21, Q22, Q25, Q28, Q29, Q31, Q32, Q33, Q34, Q35, Q36, Q41, Q42, Q43, Q44, Q45.

## Topic list

- Q1 — Ch1 Real numbers — LCM of 1 to 10 = 2,520
- Q2 — Ch1 FTA / composite numbers — 3·5·7·11 + 11 = 11 × 106
- Q3 — Ch1 Euclid division / remainders — n ≡ 5 (mod 9), so n² ≡ 7
- Q4 — Ch3 Partnership — capital ratio 3 : 5, total profit ₹12,000
- Q5 — Ch3 Compound interest — 3rd-year interest = 1.1 × 2nd-year interest
- Q6 — Ch3 Compound interest — 2 years at 5%, interest ₹2,665
- Q7 — Ch3 Compound interest, half-yearly — principal ₹62,500
- Q8 — Ch3 Partnership (capital × time) — total profit ₹29,000
- Q9 — Ch4 Polynomials, zeroes and coefficients — other zero 2/3
- Q10 — Ch4 AP — middle-term condition, x = 3
- Q11 — Ch4 3-variable linear system — add the equations, x + y + z = 6
- Q12 — Ch4 Polynomials, remainder theorem — a = −4
- Q13 — Ch4 AP — sum 27, product 648, largest term 12
- Q14 — Ch4 Quadratics, completing the square — minimum 5
- Q15 — Ch5 Similar triangles — perimeter ratio, 36 cm
- Q16 — Ch5 Distance formula — k = 8
- Q17 — Ch5 Tangents — perpendicular tangents form a square, PA = 5 cm
- Q18 — Ch5 Section formula — x = 6
- Q19 — Ch5 Similar triangles — crossing wires, h = 6 m
- Q20 — Ch6 Areas — rectangle plus semicircle = 217 cm²
- Q21 — Ch6 Volume conservation — cubes recast, edge 6 cm
- Q22 — Ch6 Frustum — curved surface area from circumferences = 1,408 cm²
- Q23 — Ch6 Circle perimeter — track, extra 44 m
- Q24 — Ch6 Combined solids — cylinder minus cone, TSA 5,940 cm²
- Q25 — Ch7 Identities — 1 − sin²θ/(1 + cos θ) = cos θ
- Q26 — Ch7 Standard angles — tan = 1, θ = 20°
- Q27 — Ch7 Heights & distances — flagpole on building, 16√3 m
- Q28 — Ch8 Compound probability — two letters in the same box, 1/3
- Q29 — Ch8 Complementary probability — even product, 3/4
- Q30 — Ch8 Grouped median — 32 minutes
- Q31 — Ch9 Percentage yield — 16 sacks
- Q32 — Ch9 Break-even — ₹60 per kit
- Q33 — Ch9 Pipes & cisterns — 9 hours
- Q34 — Ch9 GST (CGST/SGST) — CGST ₹450
- Q35 — Ch9 Boats & streams — b : s = 2 : 1
- Q36 — Ch10 Counting — 4-digit palindromes = 90
- Q37 — Ch10 Extremal / sets — at least 18 saw both
- Q38 — Ch10 Counting — ordered messages 9 × 8 = 72
- Q39 — Ch10 Pigeonhole — n = 7
- Q40 — Ch10 Invariants (parity) — 4 moves
- Q41 — Sec II Ch4+Ch10 — 3-term APs from 1 to 30 = 210
- Q42 — Sec II Ch5+Ch7 — lamp on a guy wire, OM = 6√3 m
- Q43 — Sec II Ch4+Ch5 — right angle at C on the x-axis, C = (2, 0) or (4, 0)
- Q44 — Sec II Ch3+Ch9 — loan plus fuel, break-even at 1,000 pots
- Q45 — Sec II Ch6+Ch10 — recast into spheres and cones, maximum 19 solids
