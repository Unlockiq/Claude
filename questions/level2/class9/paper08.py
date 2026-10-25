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
    dict(ch='3', scen='machine falling from ₹50,000 to ₹32,000 in 2 years · yearly rate',
         stem='A machine bought for ₹50,000 is worth ₹32,000 after 2 years. It lost the same percentage of its value each year. What is that yearly percentage?',
         opts=['20%', '18%', '36%', '16%'],
         hint='The value is multiplied by the same factor twice: factor² = 32,000 ÷ 50,000.',
         sol='factor² = 32,000/50,000 = 0.64, so the factor is 0.8: a 20% loss each year. Check: 50,000 × 0.8 = 40,000 and 40,000 × 0.8 = 32,000. (18% splits the total ₹18,000 loss as a percentage; 36% is the total fall over both years.)'),
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
    dict(ch='5', scen='circumcentre of the triangle (−1,0) (3,3) (3,−3)',
         stem='The triangle has vertices A(−1, 0), B(3, 3) and C(3, −3). Its circumcentre lies on the x-axis. How far is the circumcentre from A?',
         opts=['25/8', '4', '5/2', '3'],
         hint='Let the circumcentre be (x, 0) and make its distances to A and B equal.',
         sol='(x + 1)² = (x − 3)² + 9 gives 2x + 1 = −6x + 18, so x = 17/8. Distance from A = 17/8 + 1 = 25/8. Check with B: √((3 − 17/8)² + 9) = √(49/64 + 576/64) = 25/8. (4 is the distance from A to the midpoint of BC.)'),
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
    dict(ch='6', scen='3 4 5 ratio triangle of area 150 · altitude to the longest side',
         stem='The sides of a triangle are in the ratio 3 : 4 : 5 and its area is 150 cm². What is the length of the altitude drawn to the longest side?',
         opts=['12 cm', '15 cm', '20 cm', '10 cm'],
         hint='Write the sides as 3k, 4k, 5k. The triangle is right-angled.',
         sol='Area = ½ × 3k × 4k = 6k² = 150, so k = 5 and the sides are 15, 20, 25 cm. Altitude to the 25 cm side = 2 × 150 ÷ 25 = 12 cm. (15 and 20 cm are the other two sides, which are also altitudes.)'),
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
    dict(ch='8', scen='new number that lifts the average of the larger group to 18.5',
         stem='The average of 25 numbers is 15.6. The average of the first 10 of them is 12. A new number is added to the other 15, and their average becomes 18.5. What is the new number?',
         opts=['26', '18.5', '34', '22'],
         hint='Find the total of the other 15 numbers first.',
         sol='Total of 25 = 25 × 15.6 = 390; first 10 = 120; other 15 = 270 (average 18). After adding x: 16 × 18.5 = 296, so x = 296 − 270 = 26. (18.5 is the new average, not the new number.)'),
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
    dict(ch='9', scen='two 400 mg doses halving every 4 hours · amount at midnight',
         stem='The amount of a medicine in the blood halves every 4 hours. A patient takes 400 mg at 8 AM and another 400 mg at 4 PM. How much is in the blood at midnight?',
         opts=['125 mg', '100 mg', '150 mg', '225 mg'],
         hint='Find the amount just after the second dose, then halve it twice.',
         sol='From 8 AM to 4 PM is 2 halvings: 400 → 200 → 100 mg. After the second dose: 500 mg. From 4 PM to midnight is 2 more halvings: 500 → 250 → 125 mg. (100 mg forgets the second dose.)'),
    dict(ch='9', scen='defect estimate from 4 of 200 and 9 of 300 items',
         stem='A factory checks 200 items on Monday and finds 4 faulty, and 300 items on Tuesday and finds 9 faulty. What is the best estimate of the probability that an item is faulty?',
         opts=['2.6%', '2.5%', '3%', '2%'],
         hint='Combine all the data rather than averaging the two rates.',
         sol='Altogether 13 faulty out of 500 items: 13/500 = 2.6%. (2.5% averages 2% and 3% without weighting by the number of items.)'),

    # ---------------- Part 8 · Mathematical Reasoning
    dict(ch='10', scen='counterexamples up to 100 to divisible by 4 and 6 means divisible by 24',
         stem='How many whole numbers from 1 to 100 are counterexamples to the claim "If a number is divisible by 4 and by 6, then it is divisible by 24"?',
         opts=['4', '8', '3', '5'],
         hint='Divisible by 4 and by 6 means divisible by 12.',
         sol='Numbers divisible by 4 and by 6 are the multiples of 12: 12, 24, 36, 48, 60, 72, 84, 96. Those not divisible by 24 are 12, 36, 60 and 84. So there are 4 counterexamples. (8 counts every multiple of 12.)'),
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
         sol='Construct it: draw the 7 cm side and a 30° angle at one end. The far vertex lies on that arm, 5 cm from the other end of the 7 cm side. That end is 3.5 cm from the arm, so a circle of radius 5 cm cuts the arm at two points, giving two different triangles. The other three are SSS, SAS and ASA, which fix the triangle.'),

    # ---------------- Part 9 · Mixed Problems
    dict(ch='4+10', scen='matchstick grid two squares tall · squares from 302 sticks',
         stem='Matchsticks form a grid of unit squares that is 2 squares tall and n squares long. For example, a 2 × 1 grid uses 7 sticks. How many unit squares are in the grid made with exactly 302 sticks?',
         opts=['120', '60', '100', '150'],
         hint='Count horizontal sticks (3 rows of n) and vertical sticks (n + 1 columns of 2).',
         sol='Sticks = 3n + 2(n + 1) = 5n + 2. Check n = 1: 7 ✓. 5n + 2 = 302 gives n = 60 columns, so there are 2 × 60 = 120 unit squares. (60 is the length, not the number of squares.)'),
    dict(ch='5+6', scen='trapezium between parallel chords 16 and 12 in a circle of radius 10',
         stem='Two parallel chords of lengths 16 cm and 12 cm lie on opposite sides of the centre of a circle of radius 10 cm. Their ends form a trapezium. What is its area?',
         opts=['196 cm²', '28 cm²', '56 cm²', '98 cm²'],
         hint='The perpendicular from the centre bisects each chord. Find each chord\'s distance from the centre.',
         sol='16 cm chord: half is 8, distance = √(100 − 64) = 6 cm. 12 cm chord: half is 6, distance = √(100 − 36) = 8 cm. On opposite sides, the chords are 6 + 8 = 14 cm apart. Area = ½ × (16 + 12) × 14 = 196 cm². (28 cm² uses a height of 2, as if both chords were on the same side.)'),
    dict(ch='4+5', scen='quadrilateral from the axis crossings of y = 2x + 1 and y = 2x − 7',
         stem='The lines y = 2x + 1 and y = 2x − 7 cross the y-axis at P and Q and the x-axis at R and S. What is the area of the quadrilateral PRQS?',
         opts=['16', '32', '8', '12'],
         hint='Its diagonals PQ and RS lie on the two axes.',
         sol='P = (0, 1), Q = (0, −7), so PQ = 8. R = (−1/2, 0), S = (7/2, 0), so RS = 4. The diagonals are perpendicular (they lie on the axes), so area = ½ × 8 × 4 = 16. (32 forgets the ½.)'),
    dict(ch='8+10', scen='number 1 to 50 that is a multiple of 4 but not of 6',
         stem='A number is chosen at random from 1 to 50. What is the probability that it is a multiple of 4 but not a multiple of 6?',
         opts=['4/25', '6/25', '1/5', '2/25'],
         hint='Multiples of both 4 and 6 are multiples of 12.',
         sol='Multiples of 4 up to 50: 12. Multiples of 12: 12, 24, 36, 48 — 4 of them. So 12 − 4 = 8 numbers: 8/50 = 4/25.'),
    dict(ch='3+9', scen='loan of ₹60,000 repaid ₹5,000 a month plus 1 percent on the balance',
         stem='A loan of ₹60,000 is repaid at ₹5,000 a month. Each month, before the payment, interest of 1% is also paid on the amount still owed. How much interest is paid in total?',
         opts=['₹3,900', '₹7,200', '₹3,600', '₹4,200'],
         hint='The amounts owed are ₹60,000, ₹55,000, …, ₹5,000.',
         sol='The loan lasts 12 months. Interest = 1% of (60,000 + 55,000 + … + 5,000) = 1% of 5,000 × (12 + 11 + … + 1) = 1% of 5,000 × 78 = ₹3,900. (₹7,200 charges 1% on the full ₹60,000 every month.)'),
]
