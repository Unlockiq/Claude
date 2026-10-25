# AMO Level-2 · Class 9 · Practice Paper 8  (format: see paper01.py)


def chords_meet():
    import math
    O, r = (90, 90), 62
    ang = {'A': 200, 'B': 300, 'C': 20, 'D': 120}
    P = {k: (O[0] + r * math.cos(math.radians(a)), O[1] + r * math.sin(math.radians(a))) for k, a in ang.items()}
    prims = [('circle', O[0], O[1], r, None)]
    for a, b in (('A', 'C'), ('B', 'D'), ('A', 'B'), ('C', 'D')):
        prims.append(('line', P[a][0], P[a][1], P[b][0], P[b][1]))
    for k, a in ang.items():
        dx, dy = math.cos(math.radians(a)), math.sin(math.radians(a))
        prims += [('dot', P[k][0], P[k][1], 3), ('text', P[k][0] + 14 * dx, P[k][1] + 14 * dy, k, 12)]
    # intersection P of AC and BD
    (x1, y1), (x2, y2), (x3, y3), (x4, y4) = P['A'], P['C'], P['B'], P['D']
    d = (x1 - x2) * (y3 - y4) - (y1 - y2) * (x3 - x4)
    px = ((x1 * y2 - y1 * x2) * (x3 - x4) - (x1 - x2) * (x3 * y4 - y3 * x4)) / d
    py = ((x1 * y2 - y1 * x2) * (y3 - y4) - (y1 - y2) * (x3 * y4 - y3 * x4)) / d
    prims += [('dot', px, py, 3), ('text', px + 4, py + 14, 'P', 12)]
    return prims


QUESTIONS = [
    # ---------------- Part 1 · Number System
    dict(ch='1', scen='how many of four decimals lie between 1/3 and 0.343434…',
         stem='How many of the numbers 0.34, 0.3434, 0.335 and 0.344 lie strictly between 1/3 and 0.343434… (34 repeating)?',
         opts=['3', '2', '4', '1'],
         hint='1/3 = 0.3333… Compare digit by digit.',
         sol='0.34, 0.3434 and 0.335 are all more than 0.3333… and less than 0.343434… (0.3434 < 0.343434…). 0.344 is more than 0.3434…, so it is outside. That is 3 numbers.'),
    dict(ch='1', scen='pairs of whole-number legs giving a hypotenuse of √50',
         stem='To mark √50 on a number line, Nitya draws a right triangle with whole-number legs a ≤ b and hypotenuse √50. How many different pairs (a, b) can she use?',
         opts=['2', '1', '3', '0'],
         hint='a² + b² = 50.',
         sol='a² + b² = 50: (1, 7) gives 1 + 49 and (5, 5) gives 25 + 25. No other pair works. So 2 pairs.'),

    # ---------------- Part 2 · Fractions, Decimals & Percentages
    dict(ch='3', scen='town growing 10 percent a year · 1,21,000 now · two years ago',
         stem='A town\'s population grows by 10% every year. It is 1,21,000 now. What was it two years ago?',
         opts=['1,00,000', '1,00,833', '1,02,850', '98,010'],
         hint='Divide by 1.1 twice.',
         sol='1,21,000 ÷ 1.21 = 1,00,000. (1,00,833 divides by 1.2, a simple 20%; 98,010 takes 10% off twice.)'),
    dict(ch='3', scen='alloy of 3 kg at 60 percent and 2 kg at 85 percent copper',
         stem='3 kg of an alloy with 60% copper is melted with 2 kg of an alloy with 85% copper. What percentage of the new alloy is copper?',
         opts=['70%', '72.5%', '75%', '68%'],
         hint='Find the total mass of copper.',
         sol='Copper = 0.6 × 3 + 0.85 × 2 = 1.8 + 1.7 = 3.5 kg out of 5 kg = 70%. (72.5% is the simple average of 60% and 85%.)'),

    # ---------------- Part 3 · Algebra
    dict(ch='4', scen='(x + 1/x)² = 7 with x positive · x³ + 1/x³',
         stem='If x > 0 and (x + 1/x)² = 7, what is x³ + 1/x³?',
         opts=['4√7', '7√7', '√7', '10√7'],
         hint='x + 1/x = √7. Then use (x + 1/x)³.',
         sol='x + 1/x = √7. x³ + 1/x³ = (x + 1/x)³ − 3(x + 1/x) = 7√7 − 3√7 = 4√7.'),
    dict(ch='4', scen='p(x) = 2x³ − 3x² + ax − 6 with p(2) = 4 · p(−1)',
         stem='For p(x) = 2x³ − 3x² + ax − 6, we know p(2) = 4. What is p(−1)?',
         opts=['−14', '−8', '−2', '14'],
         hint='Use p(2) = 4 to find a first.',
         sol='p(2) = 16 − 12 + 2a − 6 = 4 gives 2a = 6, a = 3. p(−1) = −2 − 3 − 3 − 6 = −14.'),
    dict(ch='4', scen='30 coins of ₹5 and ₹2 worth ₹105',
         stem='Kiara has 30 coins, all ₹5 or ₹2, worth ₹105 in all. How many ₹5 coins does she have?',
         opts=['15', '12', '18', '10'],
         hint='If all were ₹2 coins, they would be worth ₹60.',
         sol='All ₹2 coins would make ₹60. Each ₹5 coin adds ₹3 more. (105 − 60) ÷ 3 = 15 coins of ₹5.'),
    dict(ch='4', scen='terms of 3 7 11 less than 500',
         stem='How many terms of the arithmetic progression 3, 7, 11, … are less than 500?',
         opts=['125', '124', '126', '100'],
         hint='The nth term is 4n − 1.',
         sol='4n − 1 < 500 gives n < 125.25. So n = 1, 2, …, 125: 125 terms (the 125th is 499).'),

    # ---------------- Part 4 · Geometry
    dict(ch='5', scen='perimeter of the triangle (−1,0) (3,3) (3,−3)',
         stem='What is the perimeter of the triangle with vertices (−1, 0), (3, 3) and (3, −3)?',
         opts=['16', '18', '15', '11'],
         hint='Find all three side lengths.',
         sol='From (−1, 0) to (3, 3): √(16 + 9) = 5. From (−1, 0) to (3, −3): 5. From (3, 3) to (3, −3): 6. Perimeter = 16.'),
    dict(ch='5', scen='chord 8 at distance 3 · farthest point of the circle from the chord',
         stem='A chord AB of length 8 cm is 3 cm from the centre of a circle. What is the greatest distance from the chord AB to a point on the circle?',
         opts=['8 cm', '5 cm', '3 cm', '2 cm'],
         hint='The farthest point lies on the line through the centre perpendicular to AB, on the far side.',
         sol='Radius = √(4² + 3²) = 5 cm. The farthest point is on the far side of the centre: 3 + 5 = 8 cm from the chord. (2 cm is the nearest point on the other arc.)'),
    dict(ch='5', scen='chords AC and BD meeting at P · angle BAC 40 and angle APD 100 · angle ACD',
         fig=drawing(180, 180, chords_meet()),
         stem='Chords AC and BD of a circle meet at P. Angle BAC = 40° and angle APD = 100°. What is angle ACD?',
         opts=['60°', '40°', '80°', '100°'],
         hint='Angle APB = 180° − 100°. Then use angles in the same segment.',
         sol='Angle APB = 80°, so in triangle APB, angle ABP = 180° − 40° − 80° = 60°. Angle ACD and angle ABD stand on the same arc AD, so angle ACD = 60°.'),
    dict(ch='5', scen='midpoint quadrilateral of perpendicular diagonals 8 and 10 · area',
         stem='A quadrilateral has perpendicular diagonals of lengths 8 cm and 10 cm. The midpoints of its sides are joined in order. What is the area of the new quadrilateral?',
         opts=['20 cm²', '40 cm²', '80 cm²', '18 cm²'],
         hint='The new shape has sides parallel to the diagonals and half as long.',
         sol='By the midpoint theorem the new shape has sides 4 cm and 5 cm, parallel to the diagonals. The diagonals are perpendicular, so it is a rectangle: area 4 × 5 = 20 cm² (half the original area of 40 cm²).'),

    # ---------------- Part 5 · Mensuration
    dict(ch='6', scen='triangle with sides in ratio 3 4 5 and perimeter 60 · area',
         stem='The sides of a triangle are in the ratio 3 : 4 : 5 and its perimeter is 60 cm. What is its area?',
         opts=['150 cm²', '300 cm²', '600 cm²', '120 cm²'],
         hint='Find the sides first.',
         sol='The sides are 15, 20 and 25 cm. With Heron: s = 30, area = √(30 × 15 × 10 × 5) = √22,500 = 150 cm². (It is a right triangle: ½ × 15 × 20.)'),
    dict(ch='6', scen='painting inside a hemispherical dome of radius 14 at ₹50 a m²',
         stem='The inside of a hemispherical dome of radius 14 m is to be painted at ₹50 per m². What is the cost? (Take π = 22/7.)',
         opts=['₹61,600', '₹30,800', '₹92,400', '₹1,23,200'],
         hint='The curved surface of a hemisphere is 2πr².',
         sol='Curved surface = 2 × 22/7 × 14² = 1,232 m². Cost = 1,232 × 50 = ₹61,600. (₹92,400 adds the floor; ₹1,23,200 uses a full sphere.)'),
    dict(ch='6', scen='cone of volume 96π and radius 6 · curved surface',
         stem='A cone has volume 96π cm³ and base radius 6 cm. What is its curved surface area?',
         opts=['60π cm²', '96π cm²', '48π cm²', '36π cm²'],
         hint='Find the height, then the slant height.',
         sol='⅓ × π × 36 × h = 96π gives h = 8 cm. Slant height = √(36 + 64) = 10 cm. Curved surface = π × 6 × 10 = 60π cm².'),

    # ---------------- Part 6 · Data Handling, Statistics & Probability
    dict(ch='8', scen='leap year with 53 Sundays',
         stem='A leap year is chosen at random. What is the probability that it has 53 Sundays?',
         opts=['2/7', '1/7', '3/7', '53/366'],
         hint='366 days = 52 weeks + 2 extra days.',
         sol='The 2 extra days are a pair of consecutive days: (Sun, Mon), (Mon, Tue), …, (Sat, Sun) — 7 equally likely pairs. Two of them include Sunday, so the probability is 2/7.'),
    dict(ch='8', scen='average of 10 numbers 12 and of 15 numbers 18 · overall',
         stem='The average of 10 numbers is 12 and the average of 15 other numbers is 18. What is the average of all 25 numbers?',
         opts=['15.6', '15', '16', '16.2'],
         hint='Combine the totals.',
         sol='Totals: 120 and 270, so 390 for 25 numbers. Average = 390 ÷ 25 = 15.6. (15 is the plain average of 12 and 18.)'),
    dict(ch='8', scen='marks table 10 to 50 with frequencies 4 7 12 9 8 · mean minus median',
         fig=table(['Marks', '10', '20', '30', '40', '50'], [['Students', '4', '7', '12', '9', '8']], widths=[90] + [55] * 5),
         stem='The table shows the marks of 40 students. What is the mean minus the median?',
         opts=['2.5', '0', '7.5', '−2.5'],
         hint='The median is the average of the 20th and 21st marks in order.',
         sol='Mean = (40 + 140 + 360 + 360 + 400)/40 = 1,300/40 = 32.5. The cumulative counts are 4, 11, 23, … so the 20th and 21st marks are both 30: median 30. Mean − median = 2.5.'),

    # ---------------- Part 7 · Applied Mathematics
    dict(ch='9', scen='300 tickets at ₹200 and ₹500 for ₹90,000 · ₹500 tickets',
         stem='A concert sells 300 tickets, some at ₹200 and the rest at ₹500, for ₹90,000 in all. How many ₹500 tickets were sold?',
         opts=['100', '200', '120', '150'],
         hint='If all were ₹200 tickets, the takings would be ₹60,000.',
         sol='300 tickets at ₹200 would give ₹60,000. Each ₹500 ticket adds ₹300 more. (90,000 − 60,000) ÷ 300 = 100 tickets at ₹500.'),
    dict(ch='9', scen='medicine halving every 4 hours from 400 mg at 8 AM · at 8 PM',
         stem='The amount of a medicine in the blood halves every 4 hours. At 8 AM there are 400 mg. How much is left at 8 PM?',
         opts=['50 mg', '100 mg', '25 mg', '0 mg'],
         hint='Count the 4-hour periods from 8 AM to 8 PM.',
         sol='12 hours = 3 halvings: 400 → 200 → 100 → 50 mg. (0 mg assumes 100 mg is lost every 4 hours.)'),
    dict(ch='9', scen='defect estimate from 4 of 200 and 9 of 300 items',
         stem='A factory checks 200 items on Monday and finds 4 faulty, and 300 items on Tuesday and finds 9 faulty. What is the best estimate of the probability that an item is faulty?',
         opts=['2.6%', '2.5%', '3%', '2%'],
         hint='Combine all the data rather than averaging the two rates.',
         sol='Altogether 13 faulty out of 500 items: 13/500 = 2.6%. (2.5% averages 2% and 3% without weighting by the number of items.)'),

    # ---------------- Part 8 · Mathematical Reasoning
    dict(ch='10', scen='counterexample to divisible by 4 and 6 implies divisible by 24',
         stem='Which number is a counterexample to the claim "If a number is divisible by 4 and by 6, then it is divisible by 24"?',
         opts=['12', '24', '48', '18'],
         hint='The number must be divisible by 4 and by 6 but not by 24.',
         sol='12 is divisible by 4 and by 6 but not by 24. 24 and 48 agree with the claim, and 18 is not divisible by 4.'),
    dict(ch='10', scen='halving 100 with whole quotients until reaching 0',
         stem='Algorithm: start with 100; repeatedly replace the number by the whole-number part of half of it, until you reach 0. How many halvings are made?',
         opts=['7', '6', '8', '50'],
         hint='100 → 50 → 25 → 12 → …',
         sol='100 → 50 → 25 → 12 → 6 → 3 → 1 → 0: 7 halvings. (This equals the number of binary digits of 100, which is 1100100.)'),
    dict(ch='10', scen='ways to tile a 2 by 6 board with dominoes',
         stem='In how many ways can a 2 × 6 board be covered completely by 2 × 1 dominoes?',
         opts=['13', '8', '21', '12'],
         hint='The left end is either one upright domino or two flat dominoes: W(n) = W(n − 1) + W(n − 2).',
         sol='W(1) = 1, W(2) = 2, then 3, 5, 8, 13. So W(6) = 13.'),
    dict(ch='10', scen='data that does not fix a unique triangle',
         stem='Which set of data does NOT fix a unique triangle?',
         opts=['Sides 5 cm and 7 cm, and a 30° angle opposite the 5 cm side', 'Sides 5 cm, 7 cm and 9 cm',
               'Sides 5 cm and 7 cm, and a 30° angle between them', 'Angles 30° and 60°, and the 7 cm side between them'],
         hint='SSS, SAS and ASA fix a triangle. Two sides with a non-included angle may not.',
         sol='With the 30° angle opposite the shorter side, the angle opposite 7 cm can be about 44° or about 136°, so two different triangles fit. The other three are SSS, SAS and ASA, which fix the triangle.'),

    # ---------------- Part 9 · Mixed Problems
    dict(ch='4+10', scen='matchstick squares in a row · squares from 301 sticks',
         stem='Squares are made in a row with matchsticks: 1 square needs 4 sticks, 2 squares need 7, 3 squares need 10, and so on. How many squares can be made with exactly 301 sticks?',
         opts=['100', '75', '101', '99'],
         hint='n squares need 3n + 1 sticks.',
         sol='3n + 1 = 301 gives n = 100 squares. (75 divides 301 by 4, as if no sticks were shared.)'),
    dict(ch='5+6', scen='incircle of the triangle (0,0) (12,0) (0,9) · area',
         stem='A circle touches all three sides of the triangle with vertices (0, 0), (12, 0) and (0, 9). What is the area of the circle?',
         opts=['9π', '36π', '4π', '6π'],
         hint='For any triangle, area = r × (half the perimeter).',
         sol='Sides 12, 9 and 15, so half the perimeter is 18. Area of triangle = ½ × 12 × 9 = 54. r = 54 ÷ 18 = 3. Circle area = 9π.'),
    dict(ch='4+5', scen='x-axis gap between y = 2x + 1 and y = 2x − 7',
         stem='The parallel lines y = 2x + 1 and y = 2x − 7 cross the x-axis at P and Q. What is the distance PQ?',
         opts=['4', '8', '3', '6'],
         hint='Find each x-intercept.',
         sol='y = 0 gives x = −1/2 for the first line and x = 7/2 for the second. PQ = 7/2 − (−1/2) = 4. (8 is the gap between the y-intercepts.)'),
    dict(ch='8+10', scen='number 1 to 50 that is a multiple of 4 but not of 6',
         stem='A number is chosen at random from 1 to 50. What is the probability that it is a multiple of 4 but not a multiple of 6?',
         opts=['4/25', '6/25', '1/5', '2/25'],
         hint='Multiples of both 4 and 6 are multiples of 12.',
         sol='Multiples of 4 up to 50: 12. Multiples of 12: 12, 24, 36, 48 — 4 of them. So 12 − 4 = 8 numbers: 8/50 = 4/25.'),
    dict(ch='3+9', scen='principal that becomes ₹14,520 in 2 years at 10 percent compound',
         stem='A sum of money becomes ₹14,520 in 2 years at 10% per year compound interest. What was the sum?',
         opts=['₹12,000', '₹12,100', '₹11,616', '₹13,200'],
         hint='Divide by 1.1 twice.',
         sol='14,520 ÷ 1.21 = ₹12,000. (₹12,100 divides by 1.2; ₹11,616 takes 20% off ₹14,520.)'),
]
