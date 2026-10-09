# Manual work still needed (after the automatic text fixes)

**37 of the 55 papers** need at least one manual fix that matters:
- **10 papers** need a hand edit in Word, because the text sits in an equation object or can't be reached by the fix tool.
- **33 papers** need a picture redrawn because it breaks a syllabus rule or could mislead a student.
- Some papers need both.

There are also 3 content decisions, and some purely cosmetic picture fixes. Those are listed at the end; the cosmetic ones are in the class summaries.

## A. Hand edits in Word (10 papers)
| Paper | What to change |
|---|---|
| C4 P4 | Solutions to Q14, Q15 and Q41 start with a fraction (an equation object). Add a word before each. |
| C4 P5 | 5 solutions start with a fraction (an equation object). Add a word before each. |
| C7 P5 | Q45 stem starts with a bare "x". Write "The number x …". |
| C8 P1 | Q12 options: the spacing around "+" is uneven. |
| C8 P2 | Q5 stem starts with the equation "8⁻² = 2ˣ". Write "It is given that 8⁻² = 2ˣ …". |
| C9 P3 | Q21 and Q25: the number and "cm" split across lines. Join them with a non-breaking space. |
| C10 P5 | Q27 option A "1 , 200√3" is in a different font, with a stray space. |
| C11 P1 | **Done:** Q2 and Q3 z̄ fixed with `tools/fix_math_accents.py`. |
| C11 P2 | **Done:** Q5 z̄ and Q36 raised ⁿ fixed. |
| C11 P4 | **Done:** Q2 z̄ fixed. |

## B. Pictures to redraw — affects correctness or a syllabus rule (33 papers)
| Class | Paper | Picture fix |
|---|---|---|
| 1 | P1 | Q7: number line, number every tick except the one asked about. Q42: the grey card looks like a square option. |
| 1 | P2 | Q11: number line ticks. |
| 2 | P1 | Q8: number line (330 and 390 have no number). |
| 2 | P2 | Q3: number line (A–D instead of numbers). |
| 2 | P5 | Q41: number line (only every second tick is numbered). |
| 3 | P1 | Q26: right-angle marks on the L-shaped plan. |
| 3 | P2 | Q23 (square C needs right-angle and equal-side marks), Q25, Q27 and Q45: right-angle marks. Q36: number line (your call). |
| 4 | P1 | **Q19: the pyramid hides an edge**, so counting the drawing gives 11, not 12. Then change option 7 to 11. Q45: right-angle marks on the inner corners. |
| 4 | P2 | Q26: right-angle marks. Q27: the half symbol must be half of the key bird. Q45: unclear "8 cm" and "3 cm" labels. |
| 4 | P3 | Q27/28: the pictograph key should read "= 5 bees". |
| 4 | P4 | Q26: right-angle marks. |
| 4 | P5 | Q28: cut the half trumpet cleanly. |
| 5 | P1 | Q20: right angles at O. Q27: the key should read "= 2 goals". |
| 5 | P2 | **Q20: equal-side ticks on triangle D and trapezium C** (otherwise a second answer is defensible). Q19: right-angle square. |
| 5 | P4 | Q22: the triangle's perimeter equals the answer. Redraw as 9-12-15. |
| 5 | P5 | Q27: the key should read "= 4 boats". |
| 6 | P1 | Q19: stray "O" mark. Q7: number line labels only the even ticks. Q11: light shading is lost in greyscale. |
| 6 | P3 | Q27: right-angle marks. |
| 6 | P5 | Q44: right-angle marks. |
| 7 | P2 | Q21: an arrow sits on point E, and the arcs are unequal. Q22: "x" should be "x°". |
| 7 | P5 | Q15: inner-corner right angle. Q44: right angles at A and B. Q20: line m is tilted, which gives the answer away. |
| 8 | P1 | Q27: gridlines every 1 (values fall between gridlines). |
| 8 | P3 | **Q20: new numbers in text and picture together** (16 m × 12 m; see the Class 8 summary). |
| 8 | P5 | **Q45: slant height 50 cm in text and picture together** (see the Class 8 summary). |
| 9 | P1 | Q42: the "6 cm" label is cut off and outside the circle. |
| 9 | P2 | Q25: "21 m" reads as MC, not BC. |
| 9 | P4 | Q23: right-angle mark on the pyramid height. Q25: the "4 cm" label gives away a step. |
| 9 | P5 | Q38: "24 cm" sits on half the diagonal. |
| 10 | P3 | Q27: right angle where the building meets the ground. |
| 10 | P4 | Q16, Q27 and Q42: right-angle marks. Q43: the "shelf" label is in the wrong region. |
| 11 | P2 | Q22: the "ribbon unwound" label is by the wrong arc, and only colour links them. |
| 11 | P3 | Q19: right-angle mark on the square platform. |
| 11 | P4 | Q21: the θ arc stops at 180°, not at OP. |

## C. Decisions for you
- **C6 P3 Q44:** uses the polygon angle-sum formula (Class 8 material). Keep it as a stretch star question, or rework it.
- **C7 P3 Q39:** exponents up to 44, above the "≤ 5" ceiling, although nothing is computed. Keep it or change it.
- **C1 P3 Q43:** putting the months in calendar order changes the answer letter to (C).
- **Cover of all 55 papers:** "Print or view this paper in colour" conflicts with the greyscale rule 12(c).

## D. Cosmetic only (optional)
These are listed in the class summaries:
- Clock hands crossing numerals, overlapping labels, table headers not bold.
- Answer-sheet bubbles in rows 10–15 out of line.
- Optional difficulty-label swaps.

## Symbol fixes done with `tools/fix_math_accents.py`
- **z̄ (printed as "ź"):** C11 P1, P2 and P4.
- **Raised ⁿ (printed as a quote mark):** C11 P1, P2, P3 and P5. This includes the P5 Q9 question, "(1 + x)ⁿ". It was also fixed in C7 P3, C9 P2, C9 P4 and C10 P4, which had the same problem in their solutions.

All 9 rebuilt PDFs keep the same page size, page count, question positions and margins as before.
