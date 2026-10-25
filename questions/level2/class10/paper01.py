# AMO Level-2 · Class 10 · Practice Paper 1
# Each question: ch (chapter or star pair), scen (unique scenario key), stem, opts (correct answer FIRST),
# hint, sol, optional fig. fixed=True keeps the option order, with ans = index of the correct option.
import math


def tri_parallel(top='A', left='B', right='C', d='D', e='E', t=0.55, labels=None):
    """Triangle with a segment DE parallel to the base. labels: list of (text, x, y)."""
    A, B, C = (120, 10), (10, 170), (230, 170)
    D = (A[0] + t * (B[0] - A[0]), A[1] + t * (B[1] - A[1]))
    E = (A[0] + t * (C[0] - A[0]), A[1] + t * (C[1] - A[1]))
    prims = [('poly', [A, B, C], 'yellow'), ('line', D[0], D[1], E[0], E[1]),
             ('text', A[0], A[1] - 12, top, 12), ('text', B[0] - 10, B[1] + 8, left, 12), ('text', C[0] + 10, C[1] + 8, right, 12),
             ('text', D[0] - 12, D[1], d, 12), ('text', E[0] + 12, E[1], e, 12)]
    for s, x, y in labels or []:
        prims.append(('text', x, y, s, 11))
    return prims


def tangents(r=45, d=150, lab_r=None, lab_extra=None, angle_mark=None):
    """Circle centre O with two tangents from an external point P touching at A and B."""
    O = (60, 80)
    P = (O[0] + d, O[1])
    phi = math.acos(r / d)
    A = (O[0] + r * math.cos(phi), O[1] - r * math.sin(phi))
    B = (O[0] + r * math.cos(phi), O[1] + r * math.sin(phi))
    prims = [('circle', O[0], O[1], r, None), ('line', P[0], P[1], A[0], A[1]), ('line', P[0], P[1], B[0], B[1]),
             ('line', O[0], O[1], A[0], A[1], True), ('line', O[0], O[1], B[0], B[1], True), ('line', O[0], O[1], P[0], P[1], True),
             ('dot', O[0], O[1], 3), ('text', O[0] - 10, O[1] + 4, 'O', 12), ('text', P[0] + 12, P[1], 'P', 12),
             ('text', A[0] + 2, A[1] - 12, 'A', 12), ('text', B[0] + 2, B[1] + 12, 'B', 12)]
    if lab_r:
        prims.append(('text', (O[0] + A[0]) / 2 - 12, (O[1] + A[1]) / 2, lab_r, 11))
    if angle_mark:
        prims.append(('text', P[0] - 28, P[1], angle_mark, 11))
    for s, x, y in lab_extra or []:
        prims.append(('text', x, y, s, 11))
    return prims


QUESTIONS = [
    # ---------------- Part 1 · Number System
    dict(ch='1', scen='three traffic signals changing every 48 72 and 108 seconds',
         stem='Three traffic signals on a road change every 48 seconds, 72 seconds and 108 seconds. All three change together at 7:00:00 AM. At what time will they next change together?',
         opts=['7:07:12 AM', '7:03:36 AM', '7:04:48 AM', '7:12:00 AM'],
         hint='Write each time as a product of primes and take the highest powers.',
         sol='48 = 2⁴ × 3, 72 = 2³ × 3², 108 = 2² × 3³. LCM = 2⁴ × 3³ = 432 s = 7 min 12 s. So they next change together at 7:07:12 AM. (216 s is only the LCM of 72 and 108.)'),
    dict(ch='1', scen='how many of six fractions have terminating decimals',
         stem='How many of these numbers have a terminating decimal expansion: 77/210, 17/8, 64/455, 15/1600, 13/3125, 129/(2² × 5⁷ × 7⁵)?',
         opts=['3', '4', '2', '5'],
         hint='Reduce each fraction to lowest terms first. Then look at the primes in the denominator.',
         sol='77/210 = 11/30 has a factor 3 below: not terminating. 17/8 = 17/2³: terminating. 64/455 = 64/(5 × 7 × 13): not terminating. 15/1600 = 3/320 = 3/(2⁶ × 5): terminating. 13/3125 = 13/5⁵: terminating. The last has 7⁵ below and cannot cancel: not terminating. So 3.'),

    # ---------------- Part 2 · Fractions, Decimals & Percentages
    dict(ch='3', scen='half-yearly against yearly compounding on ₹10,000 at 20 percent',
         stem='Ananya deposits ₹10,000 for 1 year at 20% per annum. How much more interest does she earn if the interest is compounded half-yearly instead of yearly?',
         opts=['₹100', '₹200', '₹0', '₹2,100'],
         hint='Half-yearly means 10% for each of two half-years.',
         sol='Yearly: ₹10,000 × 1.2 = ₹12,000, interest ₹2,000. Half-yearly: ₹10,000 × 1.1 × 1.1 = ₹12,100, interest ₹2,100. Difference ₹100.'),
    dict(ch='3', scen='partner joining after six months with more capital',
         stem='Arjun starts a business with ₹30,000. Six months later Meera joins with ₹40,000. At the end of the year the profit is ₹26,000. What is Arjun\'s share?',
         opts=['₹15,600', '₹11,143', '₹10,400', '₹13,000'],
         hint='Profit is shared in the ratio capital × time.',
         sol='Arjun: 30,000 × 12 = 3,60,000. Meera: 40,000 × 6 = 2,40,000. Ratio 3 : 2. Arjun gets 3/5 × 26,000 = ₹15,600. (₹11,143 ignores time and uses 3 : 4.)'),
    dict(ch='3', scen='difference of compound and simple interest is ₹50 over two years',
         stem='On a certain sum, the compound interest for 2 years at 10% per annum (compounded yearly) is ₹50 more than the simple interest. What is the sum?',
         opts=['₹5,000', '₹500', '₹50,000', '₹2,500'],
         hint='For 2 years, CI − SI = P × (r/100)².',
         sol='CI − SI = P × (10/100)² = P/100. So P/100 = 50 and P = ₹5,000. (The extra ₹50 is the interest on the first year\'s interest.)'),

    # ---------------- Part 3 · Algebra
    dict(ch='4', scen='value of a squared b plus a b squared for zeros of 2x²−7x+3',
         stem='If α and β are the zeros of 2x² − 7x + 3, what is the value of α²β + αβ²?',
         opts=['21/4', '−21/4', '21/2', '3/2'],
         hint='α²β + αβ² = αβ(α + β).',
         sol='α + β = 7/2 and αβ = 3/2. α²β + αβ² = αβ(α + β) = 3/2 × 7/2 = 21/4.'),
    dict(ch='4', scen='value of k for which kx + 3y = k − 3 and 12x + ky = k have no solution',
         stem='For which value of k does the pair kx + 3y = k − 3 and 12x + ky = k have no solution?',
         opts=['−6', '6', '±6', '0'],
         hint='No solution: a₁/a₂ = b₁/b₂ ≠ c₁/c₂. Check both values that make the first two ratios equal.',
         sol='k/12 = 3/k gives k² = 36, so k = 6 or −6. For k = 6 all three ratios are 1/2 (infinitely many solutions). For k = −6: a₁/a₂ = b₁/b₂ = −1/2 but c₁/c₂ = (−9)/(−6) = 3/2. So k = −6.'),
    dict(ch='4', scen='three-digit numbers divisible by 7',
         stem='How many three-digit numbers are divisible by 7?',
         opts=['128', '129', '127', '142'],
         hint='Find the smallest and the largest three-digit multiples of 7. They form an AP.',
         sol='The smallest is 105 and the largest is 994. 994 = 105 + (n − 1) × 7 gives n − 1 = 127, so n = 128.'),
    dict(ch='4', scen='train covering 360 km 48 minutes faster at 5 km/h more',
         stem='A train covers 360 km at a uniform speed. If its speed were 5 km/h more, it would take 48 minutes less. What is its usual speed?',
         opts=['45 km/h', '40 km/h', '50 km/h', '60 km/h'],
         hint='48 minutes is 4/5 hour. Form a quadratic in the speed v.',
         sol='360/v − 360/(v + 5) = 4/5 gives 1,800/(v(v + 5)) = 4/5, so v(v + 5) = 2,250, i.e. v² + 5v − 2,250 = 0 = (v − 45)(v + 50). So v = 45 km/h. Check: 8 h at 45 km/h and 7.2 h at 50 km/h differ by 0.8 h.'),

    # ---------------- Part 4 · Geometry
    dict(ch='5', scen='DE parallel to BC with sides x x−2 x+2 x−1',
         fig=drawing(250, 185, tri_parallel(labels=[('x', 52, 52), ('x − 2', 44, 136), ('x + 2', 196, 52), ('x − 1', 204, 136)])),
         stem='In triangle ABC, DE ∥ BC. AD = x, DB = x − 2, AE = x + 2 and EC = x − 1 (all in cm). What is the length of AB?',
         opts=['6 cm', '4 cm', '7 cm', '10 cm'],
         hint='Basic Proportionality Theorem: AD/DB = AE/EC.',
         sol='x/(x − 2) = (x + 2)/(x − 1). So x² − x = x² − 4, which gives x = 4. AB = AD + DB = 4 + 2 = 6 cm. (4 cm is x itself.)'),
    dict(ch='5', scen='quadrilateral OAPB from two tangents with OP 13 and radius 5',
         fig=drawing(230, 160, tangents(r=45, d=150, lab_r='5')),
         stem='PA and PB are tangents from P to a circle with centre O and radius 5 cm. If OP = 13 cm, what is the perimeter of quadrilateral OAPB?',
         opts=['34 cm', '36 cm', '30 cm', '26 cm'],
         hint='A tangent is perpendicular to the radius at the point of contact.',
         sol='Triangle OAP is right-angled at A, so PA = √(13² − 5²) = 12 cm. PB = PA = 12 cm. Perimeter = 5 + 12 + 12 + 5 = 34 cm.'),
    dict(ch='5', scen='point where the y-axis cuts the segment from (−3, 5) to (6, −1)',
         stem='The y-axis cuts the line segment joining A(−3, 5) and B(6, −1) at P. What are the coordinates of P?',
         opts=['(0, 3)', '(0, 2)', '(0, 1)', '(0, 4)'],
         hint='Let P divide AB in the ratio k : 1. Its x-coordinate must be 0.',
         sol='x-coordinate: (6k − 3)/(k + 1) = 0 gives k = 1/2, so the ratio is 1 : 2. y-coordinate: (1 × (−1) + 2 × 5)/3 = 9/3 = 3. P = (0, 3).'),

    # ---------------- Part 5 · Mensuration
    dict(ch='6', scen='capacity of a frustum bucket with radii 20 and 10 cm and height 21 cm',
         stem='A bucket is a frustum of a cone with top radius 20 cm, bottom radius 10 cm and height 21 cm. How many litres of water does it hold? (Take π = 22/7.)',
         opts=['15.4 L', '46.2 L', '13.2 L', '30.8 L'],
         hint='V = (1/3)πh(R² + r² + Rr).',
         sol='V = (1/3) × 22/7 × 21 × (400 + 100 + 200) = 22 × 700 = 15,400 cm³ = 15.4 L. (46.2 L forgets the 1/3.)'),
    dict(ch='6', scen='metal sphere of radius 6 cm drawn into a wire of radius 2 mm',
         stem='A metal sphere of radius 6 cm is melted and drawn into a wire of uniform radius 2 mm. How long is the wire?',
         opts=['72 m', '7.2 m', '720 m', '36 m'],
         hint='Equate the volumes. Work in centimetres: 2 mm = 0.2 cm.',
         sol='(4/3)π × 6³ = π × 0.2² × L. So 288 = 0.04 L and L = 7,200 cm = 72 m.'),
    dict(ch='6', scen='area swept by a 21 cm minute hand in 20 minutes',
         stem='The minute hand of a tower clock is 21 cm long. What area does it sweep in 20 minutes? (Take π = 22/7.)',
         opts=['462 cm²', '231 cm²', '924 cm²', '44 cm²'],
         hint='In 20 minutes the minute hand turns through one third of a full turn.',
         sol='20 minutes is 120°, one third of 360°. Area = (1/3) × 22/7 × 21 × 21 = 462 cm². (44 cm is the arc length, not an area.)'),

    # ---------------- Part 6 · Trigonometry
    dict(ch='7', scen='sec theta plus tan theta equals 3 · find sin theta',
         stem='If sec θ + tan θ = 3 for an acute angle θ, what is sin θ?',
         opts=['4/5', '3/5', '3/4', '5/3'],
         hint='sec²θ − tan²θ = 1, so (sec θ − tan θ)(sec θ + tan θ) = 1.',
         sol='sec θ − tan θ = 1/3. Adding: 2 sec θ = 10/3, so sec θ = 5/3 and cos θ = 3/5. Then tan θ = 3 − 5/3 = 4/3, and sin θ = tan θ × cos θ = 4/5.'),
    dict(ch='7', scen='tower elevation 30 degrees then 60 degrees after walking 20 m',
         stem='From a point on level ground, the angle of elevation of the top of a tower is 30°. After walking 20 m towards the tower it becomes 60°. What is the height of the tower?',
         opts=['10√3 m', '20√3 m', '10 m', '20 m'],
         hint='Let the height be h. Write the two distances from the foot using tan 30° and tan 60°.',
         sol='Distances from the foot: h√3 and h/√3. Their difference is 20: h√3 − h/√3 = 2h/√3 = 20, so h = 10√3 m (about 17.3 m).'),

    # ---------------- Part 7 · Data Handling, Statistics & Probability
    dict(ch='8', scen='two dice whose product is a perfect square',
         stem='Two fair dice are thrown together. What is the probability that the product of the two numbers is a perfect square?',
         opts=['2/9', '1/6', '7/36', '1/4'],
         hint='List the doubles first, then look for other pairs such as (1, 4).',
         sol='Squares from two dice: the 6 doubles, plus (1, 4) and (4, 1). That is 8 of the 36 outcomes. 8/36 = 2/9. (1/6 counts only the doubles.)'),
    dict(ch='8', scen='median of a grouped table with frequencies 6 9 10 8 7',
         fig=table(['Marks', '0–10', '10–20', '20–30', '30–40', '40–50'], [['Students', '6', '9', '10', '8', '7']], widths=[80, 62, 62, 62, 62, 62]),
         stem='The table shows the marks of 40 students. What is the median mark?',
         opts=['25', '24', '26', '22.5'],
         hint='Median = l + ((N/2 − cf)/f) × h.',
         sol='N/2 = 20. Cumulative frequencies: 6, 15, 25, … so the median class is 20–30. Median = 20 + ((20 − 15)/10) × 10 = 25.'),

    # ---------------- Part 8 · Applied Mathematics
    dict(ch='9', scen='net CGST paid by a trader on a ₹1,500 margin at 12 percent GST',
         stem='Rohan, a trader, buys a cycle for ₹5,000 plus 12% GST and sells it in the same state for ₹6,500 plus 12% GST. Using input tax credit, how much CGST does he pay to the government?',
         opts=['₹90', '₹180', '₹390', '₹780'],
         hint='He pays GST only on the value he adds. Within a state, GST is split equally into CGST and SGST.',
         sol='Value added = 6,500 − 5,000 = ₹1,500. GST on it = 12% × 1,500 = ₹180. CGST is half of this: ₹90.'),
    dict(ch='9', scen='boat 24 km up and 36 km down in 6 hours',
         stem='A boat goes 24 km upstream and 36 km downstream in 6 hours. It goes 36 km upstream and 24 km downstream in 6 hours 30 minutes. What is the speed of the stream?',
         opts=['2 km/h', '4 km/h', '10 km/h', '1 km/h'],
         hint='Let a = 1/(upstream speed) and b = 1/(downstream speed).',
         sol='24a + 36b = 6 and 36a + 24b = 6.5. Adding: a + b = 5/24; subtracting: a − b = 1/24. So a = 1/8 and b = 1/12: upstream 8 km/h, downstream 12 km/h. Stream = (12 − 8)/2 = 2 km/h.'),
    dict(ch='9', scen='two workers for four days then one finishes alone',
         stem='Kavya can finish a job in 12 days and Vikram in 18 days. They work together for 4 days, then Vikram leaves. In how many more days does Kavya finish the job?',
         opts=['5 1/3 days', '4 days', '6 days', '4 2/3 days'],
         hint='Find the fraction of the job done in the first 4 days.',
         sol='Together they do 1/12 + 1/18 = 5/36 per day. In 4 days: 20/36 = 5/9. Left: 4/9. Kavya needs (4/9) ÷ (1/12) = 16/3 = 5 1/3 days.'),

    # ---------------- Part 9 · Mathematical Reasoning
    dict(ch='10', scen='socks drawn in the dark until two of every colour are certain',
         stem='A drawer has 10 red, 8 blue and 6 green socks. In the dark, what is the least number of socks you must take out to be sure of having at least 2 socks of every colour?',
         opts=['20', '7', '19', '24'],
         hint='Think of the unluckiest order of drawing.',
         sol='In the worst case you take all 10 red, all 8 blue and 1 green: 19 socks, still without 2 greens. The 20th sock must be green. So 20.'),
    dict(ch='10', scen='three-digit numbers with strictly increasing digits',
         stem='How many three-digit numbers have their digits in strictly increasing order from left to right, like 147?',
         opts=['84', '120', '504', '168'],
         hint='0 cannot appear. Once three different digits are chosen, there is only one increasing order.',
         sol='Choose 3 different digits from 1 to 9; each choice gives exactly one number. The number of choices is 9 × 8 × 7 ÷ (3 × 2 × 1) = 84. (504 counts every order.)'),
    dict(ch='10', scen='board numbers 1 to 10 replaced by a plus b minus 1',
         stem='The numbers 1, 2, 3, …, 10 are written on a board. Each step, Ishaan erases two numbers a and b and writes a + b − 1. After 9 steps one number is left. What is it?',
         opts=['46', '55', '45', '37'],
         hint='Each step, how does the total of the numbers on the board change?',
         sol='Each step lowers the total by exactly 1. The starting total is 55 and there are 9 steps, so the last number is 55 − 9 = 46, whatever the order.'),

    # ---------------- Section II · Star Questions
    dict(ch='4+10', scen='positive integer solutions of 3x + 5y = 100',
         stem='How many pairs of positive integers (x, y) satisfy 3x + 5y = 100?',
         opts=['6', '7', '5', '20'],
         hint='3x must leave the same remainder as 100 when divided by 5.',
         sol='100 and 5y are multiples of 5, so 3x is too, and x = 5k. Then 15k + 5y = 100 gives y = 20 − 3k. y ≥ 1 needs k ≤ 6, and k ≥ 1. So k = 1, 2, …, 6: 6 pairs.'),
    dict(ch='5+7', scen='two tangents meeting at 60 degrees to a circle of radius 6',
         fig=drawing(250, 160, tangents(r=40, d=80, lab_r='6', angle_mark='60°')),
         stem='Two tangents PA and PB are drawn from P to a circle with centre O and radius 6 cm. The angle between the tangents is 60°. What is the length of each tangent?',
         opts=['6√3 cm', '12 cm', '6 cm', '3√3 cm'],
         hint='OP bisects angle APB, and OA ⊥ PA.',
         sol='Angle OPA = 30° and angle OAP = 90°. tan 30° = OA/PA, so PA = 6/tan 30° = 6√3 cm. (12 cm is OP.)'),
    dict(ch='4+5', scen='right triangle with sides x x+7 and hypotenuse x+8',
         stem='The sides of a right-angled triangle are x cm, (x + 7) cm and (x + 8) cm, where x + 8 is the hypotenuse. What is the area of the triangle?',
         opts=['30 cm²', '60 cm²', '65 cm²', '39 cm²'],
         hint='Use Pythagoras to get a quadratic in x.',
         sol='(x + 8)² = x² + (x + 7)² gives x² − 2x − 15 = 0, so x = 5 (x = −3 is impossible). The legs are 5 and 12. Area = 1/2 × 5 × 12 = 30 cm².'),
    dict(ch='3+9', scen='loan of ₹2,100 repaid in two equal yearly instalments at 10 percent compound',
         stem='Kunal borrows ₹2,100 at 10% per annum compound interest. He repays it in two equal yearly instalments, the first one year after borrowing. What is each instalment?',
         opts=['₹1,210', '₹1,155', '₹1,050', '₹1,100'],
         hint='The present value of each instalment is the instalment divided by 1.1 for each year.',
         sol='x/1.1 + x/1.21 = 2,100. Multiply by 1.21: 1.1x + x = 2.1x = 2,541, so x = ₹1,210. (₹1,050 ignores interest; ₹1,155 adds only one year of interest.)'),
    dict(ch='6+10', scen='4 by 4 by 4 painted cube · small cubes with exactly one or two painted faces',
         stem='A cube of edge 4 cm is painted on all faces and cut into 64 cubes of edge 1 cm. How many small cubes have paint on exactly one face or exactly two faces?',
         opts=['48', '24', '56', '64'],
         hint='Count face-centre cubes and edge cubes separately.',
         sol='Exactly one face: each of the 6 faces has a 2 × 2 middle, so 24. Exactly two faces: each of the 12 edges has 2 middle cubes, so 24. Total 48. (The other 16 are the 8 corners and the 8 hidden cubes.)'),
]
