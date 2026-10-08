# Review: AMO Level 1, Class 4, Practice Paper 4

## Verdict
This is a strong paper. All 45 keys are correct. Each question has exactly one correct option, and every figure agrees with its stem. The blueprint, the Section II pairings and the 24 Easy + 16 Medium split are all met. The must-fix items are small:
- The Q1 answer cell shows only the letter.
- Many solution sentences start with a numeral, which breaks the house rule.
- There are a few small wording issues, and one level swap is proposed.

Key letter distribution: A 11 · B 11 · C 11 · D 12. The spread is well balanced, and no letter runs more than 2 in a row.

## Errors (must fix)
| Q | Problem | Fix |
|---|---|---|
| Q1 | The answer cell in the solutions shows only "(C)", with no option text. | Add "Forty thousand seventy-five" after the letter (addrun). |
| Solutions Q1, Q2, Q5–Q8, Q11, Q16, Q22, Q24, Q27, Q29–Q32, Q35, Q37, Q41, Q42, Q45 | One or more sentences start with a numeral or with ₹ followed by a numeral (house rule). | Text rewrites are in paper4_fixes.json, e.g. "Chairs = 24 × 36 = …", "Since 19 = 14 + 5, …", "Three notes of ₹500 …". |
| Q14, Q15, Q41 (solutions) | The "Why?" cell opens with an equation object (a fraction), so the sentence starts with a number. | This is in an equation object and cannot be fixed as a text run. Optionally prefix the cell with "Here" or "First," in Word by hand. |
| Q22 (solution) | "1650 g" has no comma, unlike "2,525 g" in the same line. | Fixed to "1,650 g" in the JSON. |

There are no wrong keys, no wrong solutions, no options with zero or several correct answers, no figure contradictions and nothing over the computational ceiling.

## Language & clarity
| Q | Current wording | Issue | Suggested rewrite (full text) |
|---|---|---|---|
| Q30 | The 20th day of a month is a Saturday. On which day of the week did the month begin? | The tense switches from "is" to "did". | The 20th day of a month is a Saturday. On which day of the week does the month begin? |
| Q36 | Ojas has the three digit cards shown. … | "three digit cards" can be read as "three-digit cards". | Ojas has the three cards shown. He makes 2-digit numbers by putting two different cards side by side. How many different 2-digit numbers can he make? |
| Q39 | The hooks of an umbrella stand are numbered from 10 to 40. … | An umbrella stand with 31 hooks is not plausible. | The hooks of a coat rack are numbered from 10 to 40. Kiara ties a tag on every hook whose tens digit is greater than its ones digit. For example, she ties a tag on hook 21. How many hooks get a tag? |
| Q41 (solution) | …so the oil lasts 10 using-days. 3 to 8 March gives 6 days, … | "using-days" is an invented term, and the sentence starts with a numeral. | …so the oil lasts for 10 days of use. Monday 3 to Saturday 8 March uses 6 days. Sunday 9 March is skipped, and 10 to 13 March uses 4 more. It is empty on Thursday, 13 March. |
| Q43 (solution) | Just above: 50,149 (149 more). Just below: 49,510 (490 less). … | These are fragments, not sentences. | The closest number above 50,000 is 50,149 (149 more). The closest below is 49,510 (490 less). Since 149 < 490, 50,149 is the closest. |
| Q36 (solution) | Numbers are 14, 17, … | The article is missing. | The numbers are 14, 17, 41, 47, 71 and 74. That is 6 numbers. |
| Q45 (solution) | Total 340 cm. 4 m = 400 cm, so … | This is a fragment, and the next sentence starts with a numeral. | … Total = 340 cm. The wire is 4 m = 400 cm, so 400 − 340 = 60 cm is left. |

## Figures
| Q | Issue | Fix |
|---|---|---|
| Q26 | The photo and the card are rectangles, but no corner carries a right-angle square. The brief says right angles are always marked, never inferred, although the stem does say "rectangular". | Add right-angle squares to the card corners, or at least to one corner of the card and one of the photo. |
| Q33 (minor) | Each minute hand runs through a numeral ("5" on the left clock, "2" on the right). The white halo partly hides the digit. | Optional: shorten the minute hands so they stop just inside the numerals. |

The other figures were checked and are fine:
- Q12: Cup 4 is filled to exactly 2/3.
- Q17: The p–r corner is marked, and q, s and t are vertical.
- Q18 and Q45: The prism has hidden edges dashed, and the drawing is consistent.
- Q20: A (1-4-1), C (2-2-2 staircase) and D (1-4-1) are valid nets; B has a 2×2 block.
- Q23: The perimeters are 22, 24, 20 and 28 cm.
- Q27 and Q28: The farms have A 18, B 27, C 45, D 12 and E 30 cows. The key is explicit, the half symbol is allowed at C4, and only A + B = 45.
- Q32: 1 Aug is a Saturday and 31 Aug is a Monday.
- Q33: The clocks show 8:25 and 11:10, and the hour hands are placed correctly.
- Q35: Figure n has n × n tiles.
- Q36: The cards are 1, 4 and 7.

## Syllabus / level / difficulty
- The blueprint is met: Ch1 5, Ch2 5, Ch3 6, Ch5 4, Ch6 6, Ch8 2, Ch9 6, Ch10 6. The Section II pairings are Q41 Ch3+Ch10, Q42 Ch9+Ch10, Q43 Ch1+Ch10, Q44 Ch3+Ch9 and Q45 Ch5+Ch6, which all match the brief.
- All questions are within the C4 ceiling:
  - The largest multiplications are 24 × 36 and 18 × 45 (2-digit × 2-digit).
  - The largest division is 4,150 ÷ 6 (4-digit ÷ 1-digit).
  - The fraction denominators are 12 or less.
  - Calendar work stays within one year.
- The labels give 24 Easy and 16 Medium. Proposed swap: Q14 Easy → Medium, because it needs a common denominator, a subtraction and a simplification, which is 2 or more steps. Q4 Medium → Easy, because it is one operation repeated. The totals stay 24/16, and both relabels are in the JSON.
- Q40 relies on February in a leap year (29 days). This is fine, but the solution could add "(February in a leap year)".
- No pure aptitude items. Every Section I question stays within one chapter.
- There are no "All/None of the above" options. The distractors are mostly common-mistake answers:
  - Q15 (D) adds the tops and the bottoms.
  - Q34 (D) is the bill, not the change.
  - Q44 (A) is 500 − price, and (C) is 500 − Sonal's share.
  - Q45 (A) is the wire used, not the wire left.
  - The weaker ones are Q24 (B) 15 and Q21 (B) 1,825. These are acceptable.

## Questions with no issues
Q2, Q3, Q4, Q5, Q6, Q7, Q8, Q9, Q10, Q11, Q12, Q13, Q15, Q16, Q17, Q18, Q19, Q20, Q21, Q23, Q24, Q25, Q27, Q28, Q29, Q31, Q32, Q34, Q35, Q37, Q38, Q40, Q42, Q44, Q45. Some of these have only the solution-text numeral-start fixes.

## Topic list
- Q1 — Ch1 Numbers to 1 lakh — reading 40,075 in words
- Q2 — Ch1 Roman numerals — which numeral is invalid (VC)
- Q3 — Ch1 Place value — place value of 8 in 47,860
- Q4 — Ch1 Number patterns — counting down by 250, first number below 97,000
- Q5 — Ch1 Place value / grouping — 36,500 buttons in packets of 100 and cartons of 10
- Q6 — Ch2 Multiplication — 24 × 36 chairs
- Q7 — Ch2 Division — remainder of 4,150 ÷ 6
- Q8 — Ch2 Subtraction — 70,000 − 46,358
- Q9 — Ch2 Inverse operations — multiplied instead of divided by 8
- Q10 — Ch2 Two-step multiplication and subtraction — 18 × 45 − 597
- Q11 — Ch3 Equivalent fractions — which fraction is in simplest form
- Q12 — Ch3 Mixed numbers — measuring cups in the picture
- Q13 — Ch3 Comparing fractions — same numerators
- Q14 — Ch3 Unlike fractions — 7/10 − 1/5
- Q15 — Ch3 Mixed numbers addition — 2 1/3 + 1 3/4 km
- Q16 — Ch3 Equivalent fractions — fraction equal to 2/3 with numerator + denominator = 20
- Q17 — Ch5 Perpendicular and parallel lines — badminton court
- Q18 — Ch5 Solid shapes — faces of a triangular prism
- Q19 — Ch5 Solid shapes — prism with 18 edges, number of faces
- Q20 — Ch5 Nets — which picture is not a net of a cube
- Q21 — Ch6 Area of a square — 45 cm side
- Q22 — Ch6 Unit conversion (mass) — suitcase plus clothes
- Q23 — Ch6 Perimeter of a rectangle — pick the 24 cm one
- Q24 — Ch6 Unit conversion (length) — 3 m 60 cm cut into 40 cm pieces
- Q25 — Ch6 Area and conversion — 25 cm tiles on a 2 m × 1 m 50 cm stage
- Q26 — Ch6 Perimeter — card with a 3 cm border
- Q27 — Ch8 Pictograph — cows on Farm B (half symbol)
- Q28 — Ch8 Pictograph — which two farms equal Farm C
- Q29 — Ch9 Time — 135 minutes in hours and minutes
- Q30 — Ch9 Calendar — 20th is a Saturday, find the day of the 1st
- Q31 — Ch9 Money — ₹500 and ₹100 notes for ₹2,700
- Q32 — Ch9 Calendar — August calendar to 3 September
- Q33 — Ch9 Time — elapsed time between two clocks
- Q34 — Ch9 Money — multi-step change from ₹500
- Q35 — Ch10 Pattern — square numbers of tiles
- Q36 — Ch10 Casework — 2-digit numbers from cards 1, 4, 7
- Q37 — Ch10 Calendar arithmetic — days in July to September
- Q38 — Ch10 Number series — ×2 + 1
- Q39 — Ch10 Casework — tens digit greater than ones digit, 10 to 40
- Q40 — Ch10 Calendar arithmetic — month starts and ends on a Friday
- Q41 — Ch3 + Ch10 — fraction of oil used per day, skipping Sundays
- Q42 — Ch9 + Ch10 — ferries every 40 minutes from 6:20 a.m. to 1:00 p.m.
- Q43 — Ch1 + Ch10 — digits 4, 9, 0, 5, 1, closest to 50,000
- Q44 — Ch3 + Ch9 — shares of a gift price and change from ₹500
- Q45 — Ch5 + Ch6 — wire prism edges and wire left from 4 m
