# AMO Level 1 · Class 11 · Practice Paper 4 (v1) — Review

**Verdict:** Strong paper. I solved all 45 questions on my own, and all 45 keys and worked solutions are correct. The blueprint is met: chapter counts 5/9/5/5/7/4/5, 24 Easy + 16 Medium, and the Section II pairings match the brief. Nothing breaks the answer. The fixes are small: one figure (the θ arc in Q21), one notation error (the conjugate in Q2), and a glyph that does not render (superscript ⁿ shows as a quote mark in the PDF in Q14 sol, Q38 stem and Q41 sol). The rest is minor wording.

**Key distribution:** A 11 (4, 8, 12, 15, 21, 23, 27, 32, 38, 40, 44) · B 12 (1, 5, 10, 11, 18, 22, 26, 28, 31, 36, 42, 45) · C 11 (2, 6, 9, 13, 16, 20, 25, 30, 34, 39, 41) · D 11 (3, 7, 14, 17, 19, 24, 29, 33, 35, 37, 43). Balanced.

## Errors (must fix)

| Q | Problem | Fix |
|---|---|---|
| Q2 | The conjugate is typeset as **ź** (z with an acute accent) in the stem equation, both in "let ź be its conjugate" and in "z² + ź²". The standard notation is z̄ (overbar). As printed, the symbol is not a conjugate. The symbol sits inside an OMML equation, not a text run, so the JSON cannot fix it. | Edit the equation: replace the acute accent with an overbar (z̄), in both places. |
| Q14 sol, Q38 stem, Q41 sol | The character ⁿ (U+207F) renders as a straight quote **"** in the PDF: "4" = 4,096", "(1 + x)" ≥ 1 + nx" and "2"⁻¹". In Q38 this is in the **stem** that candidates read. (ᵏ renders correctly.) | Text fixes are in the JSON. Q38 now uses k (ᵏ, kx, k), and the Q14 and Q41 solutions are reworded to avoid ⁿ. Alternatives: a font with U+207F, or Word superscript formatting. |

No wrong keys, no question with two correct options, nothing out of syllabus.

## Language & clarity

| Q | Current wording | Issue | Suggested rewrite (full text) |
|---|---|---|---|
| Q30 | "…How many different doubles matches can be chosen from the 6 friends?" | Trisha and 5 friends make 6 players. Trisha is not one of her own "friends". | "Trisha and 5 friends meet at a badminton court. A doubles match is played by two teams of 2 players each. Two matches are different if the two teams are different. How many different doubles matches can be chosen from these 6 players?" |
| Q37 | "In its step, the board is cut into four 4 × 4 quarters…" | "its step" is vague. | "…In the induction step, the board is cut into four 4 × 4 quarters, and one tile is put at the centre so that it covers one square from each quarter that has no removed square. …" |
| Q11 | "The squares go on in this way for ever." | Spelling. | "The squares go on in this way forever." |
| Q36 sol | "9 points placed 1.5 cm apart are all more than √2 cm apart, so 9 is too few." | The sentence starts with a numeral (house rule). The placement of the points is also unclear. | "But 9 points in a 3 × 3 grid, 1.5 cm apart, are all more than √2 cm apart, so 9 is too few." |
| Q38 | "(1 + x)ⁿ ≥ 1 + nx for every natural number n" | Glyph problem (see Errors). | "By induction one can prove that (1 + x)ᵏ ≥ 1 + kx for every natural number k and every x > −1. Using this result, which of these statements is surely true?" |
| Q14 sol | "the coefficients add up to 4ⁿ = 4,096" | Glyph problem. | "Putting x = 1, the coefficients add up to 4 to the power n, and 4,096 = 4⁶, so n = 6. The middle term is the 4th: C(6, 3)(3x)³ = 20 × 27x³ = 540x³." |
| Q41 sol | "so aₙ = n × 2ⁿ⁻¹" | Glyph problem. | "…so term k is k × 2ᵏ⁻¹; by induction, …" (rest unchanged) |

Minor, optional, not in JSON: in Q38, "surely true" could read "must be true".

## Figures

| Q | Issue | Fix |
|---|---|---|
| Q21 | The θ arc starts on the positive x-axis and stops, with its arrowhead, on the **negative x-axis** (180°). It does not reach the ray OP, which is at about 202.6° (third quadrant). As drawn, the marked angle looks like 180°. | Redraw the arc anticlockwise from the positive x-axis through 180° so it ends on ray OP, with the arrowhead at OP. Keep θ as the label. |

All other figures check out against the text:
- **Q1:** P(2, 5) and R(4, 3), axes labelled.
- **Q11:** midpoint squares are correct, 8 cm is given.
- **Q15:** N(2, −3); the right-angle square is marked; the line has slope 2/3 and crosses at −13/3.
- **Q16:** A(−3, −1), B(3, 3), C(3, −1); the line crosses at (0, 1).
- **Q19:** the line has intercepts −3 and 4; the camp is at (6, −2).
- **Q27:** the bars read 40/55/45/60/50 on gridlines; the y-axis starts at 0; there is a title and both axes are labelled.
- **Q29:** 12 cups and 4 eggs, split 3 + 1.
- **Q37:** the removed square is at column 5, row 7, which is the bottom-right quarter, the same quarter as H.
- **Q40:** 5 × 5 grid, one 2 × 2 block outlined.
- **Q44:** OB : OA ≈ 2.44, close to the true 2.414.

## Syllabus / level / difficulty

- **Chapter counts** match the blueprint: Ch1 Q1–5, Ch4 Q6–14, Ch5 Q15–19, Ch7 Q20–24, Ch8 Q25–31, Ch9 Q32–35, Ch10 Q36–40. There is no calculus and nothing from Sets, Relations or Functions, conics, polar form or De Moivre.
- **Section II pairings** match the brief: Q41 Ch4 + Ch10 (recurrence and induction), Q42 Ch4 + Ch8 (binomial and probability), Q43 Ch1 + Ch4, Q44 Ch5 + Ch7, Q45 Ch8 + Ch10 (Mantel/extremal and C(10, 5)).
- **Ceiling:** Section I stays within limits. Binomial index is 6, P&C numbers are ≤ 12 (C(12, 4) in Q29 is a binomial coefficient and fine), and complex numbers use integer parts. Q44 uses 22.5°, which is not a standard reference angle. That is acceptable in Section II because it cancels through sin 2A.
- **Difficulty:** 24 Easy and 16 Medium, exactly. Suggested swap: **Q27 Easy → Medium** (SD from a graph needs reading 5 values, the mean, the deviations and the root) and **Q18 Medium → Easy** (a direct 2×2 solve and substitution). Optional second swap: Q36 Easy → Medium (pigeonhole that needs an extremal construction for 9) with Q19 Medium → Easy (a direct formula).
- **Q31** (combined variance of two groups) is at the top end of Section I Medium but is within "variance & SD".
- **Distractors** are mostly common-mistake answers, for example:
  - Q9: Σn = 91, Σn² = 819, 13³ = 2,197.
  - Q23: 5/7 and 1/7 = tan 2B.
  - Q32: Rupa's share; the money-only ratio.
  - Q34: one-year discount; simple-interest-like value.
  - Q41: off-by-one values.
  - Weaker: Q35 (5.2 and 0.4 km/h) and Q10 (324 litres) have no clear mistake behind them. Optional: Q35 (B) 6 km/h, Q10 (D) 720 litres (2,430 × (2/3)³).

## Questions with no issues

Q1, Q3, Q4, Q5, Q6, Q7, Q8, Q9, Q10, Q12, Q13, Q15, Q16, Q17, Q18, Q19, Q20, Q22, Q23, Q24, Q25, Q26, Q27, Q28, Q29, Q31, Q32, Q33, Q34, Q35, Q39, Q40, Q42, Q43, Q44, Q45. (Some carry the optional notes above.)

## Topic list

- Q1 — Ch1 complex numbers — modulus of z₁ + z₂ read from Argand grid
- Q2 — Ch1 complex numbers — z² + z̄² for z = 2 + 3i
- Q3 — Ch1 powers of i — i⁻¹ + … + i⁻⁵
- Q4 — Ch1 complex algebra — polynomial value at 1 + 2i (factor z² − 2z + 5)
- Q5 — Ch1 argument — a from arg = 3π/4, then z²
- Q6 — Ch4 AP — number of arithmetic means inserted between 3 and 43
- Q7 — Ch4 linear inequality — greatest integer with x/2 − (x − 3)/5 < 3
- Q8 — Ch4 binomial — equal coefficients of x⁴ and x³ in (x + a)⁶
- Q9 — Ch4 special series — Σk³ for k = 1 to 13
- Q10 — Ch4 GP — tank water on day 6, ratio 2/3
- Q11 — Ch4 GP sum to infinity — nested midpoint squares
- Q12 — Ch4 GP — S₆ = 28 S₃
- Q13 — Ch4 AP — sum of two-digit numbers ≡ 5 (mod 8)
- Q14 — Ch4 binomial — middle term of (1 + 3x)ⁿ given coefficient sum
- Q15 — Ch5 straight lines — line with foot of perpendicular N(2, −3)
- Q16 — Ch5 straight lines — parallel line through C, y-intercept
- Q17 — Ch5 straight lines — y-intercept equals slope, through (1, 3)
- Q18 — Ch5 straight lines — concurrency, find k
- Q19 — Ch5 distance from point to line — map scale
- Q20 — Ch7 trig of any angle — allied angles of sin
- Q21 — Ch7 trig of any angle — sin θ + cos θ for P(−12, −5)
- Q22 — Ch7 multiple angle — tan A from cos 2A
- Q23 — Ch7 compound angle — tan 2A from tan(A ± B)
- Q24 — Ch7 compound angle — (1 + tan A)(1 + tan B) with A + B = 45°
- Q25 — Ch8 permutations — 3-stripe flags from 7 colours
- Q26 — Ch8 binomial probability — exactly 2 of 5 guesses right
- Q27 — Ch8 standard deviation — bar graph of milk collected
- Q28 — Ch8 permutations — lion house before tiger house
- Q29 — Ch8 combinations — 4 eggs in a 2 × 6 tray, no empty row
- Q30 — Ch8 combinations — doubles matches from 6 players
- Q31 — Ch8 variance — combined variance of two groups
- Q32 — Ch9 partnership — profit share by money × time
- Q33 — Ch9 percentage yield — unpeeled potatoes needed
- Q34 — Ch9 compound interest — present value
- Q35 — Ch9 boats and streams — stream speed
- Q36 — Ch10 pigeonhole — points in a 3 cm square within √2
- Q37 — Ch10 induction — L-tromino tiling, centre tile
- Q38 — Ch10 induction — Bernoulli's inequality application
- Q39 — Ch10 pigeonhole — divisor pair in 1..20
- Q40 — Ch10 extremal — least shading to hit every 2 × 2 block
- Q41 — SII Ch4 + Ch10 — recurrence aₙ = n·2ⁿ⁻¹, sum of 15 terms
- Q42 — SII Ch4 + Ch8 — even number of reds in 8 draws (binomial trick)
- Q43 — SII Ch1 + Ch4 — Σ k·iᵏ⁻¹ for k = 1 to 20
- Q44 — SII Ch5 + Ch7 — intercept length of the normal-form line at 22.5°
- Q45 — SII Ch8 + Ch10 — triangle-free graphs with the most edges on 10 points (K₅,₅ count)
