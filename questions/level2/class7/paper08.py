# AMO Level-2 · Class 7 · Practice Paper 8
# Each question: ch, scen (unique), stem, opts (correct FIRST), hint, sol, optional fig.


def bars(data, top, step, unit='', bw=34, gap=22, h=150):
    """Bar graph: data = [(label, value)], y axis from 0 to top with gridlines every step."""
    x0, y0 = 40, 10
    w = len(data) * (bw + gap) + gap
    prims = []
    for v in range(0, top + 1, step):
        y = y0 + h - v * h / top
        prims += [('line', x0, y, x0 + w, y, True, (170, 170, 170), 0.8), ('text', x0 - 16, y, str(v), 10)]
    for i, (lab, v) in enumerate(data):
        x = x0 + gap + i * (bw + gap)
        prims += [('rect', x, y0 + h - v * h / top, bw, v * h / top, 'blue'), ('text', x + bw / 2, y0 + h + 14, lab, 10)]
    prims += [('line', x0, y0, x0, y0 + h), ('line', x0, y0 + h, x0 + w, y0 + h)]
    if unit:
        prims.append(('text', x0 + w / 2, y0 + h + 32, unit, 10))
    return prims


def pie(data, r=62):
    """Pie chart: data = [(label, degrees)]; each sector is labelled outside the circle."""
    import math
    cx = cy = r + 50
    fills = ['blue', 'yellow', 'green', 'pink', 'peach', 'lilac']
    prims, a0 = [], -90.0
    for i, (lab, deg) in enumerate(data):
        n = max(4, int(deg / 6))
        pts = [(cx, cy)] + [(cx + r * math.cos(math.radians(a0 + deg * k / n)),
                             cy + r * math.sin(math.radians(a0 + deg * k / n))) for k in range(n + 1)]
        prims.append(('poly', pts, fills[i % len(fills)]))
        m = math.radians(a0 + deg / 2)
        prims.append(('text', cx + (r + 50) * math.cos(m), cy + (r + 16) * math.sin(m), lab, 10))
        a0 += deg
    return prims


def trans(labels):
    """Parallel lines l and m (horizontal) cut by a transversal rising to the right.
    Crossings: A = (150, 40) on l and B = (90, 110) on m. At each crossing the upper-right
    and lower-left angles are acute; labels = [(x, y, text)].
    Label centres that clear the lines: near A use (115, 28) upper-left, (200, 28) upper-right,
    (100, 54) lower-left, (180, 54) lower-right; near B use (58, 98), (140, 98), (40, 122), (122, 122)."""
    prims = [('line', 0, 40, 240, 40), ('line', 0, 110, 240, 110), ('line', 60, 145, 180, 5),
             ('text', 254, 40, 'l', 12), ('text', 254, 110, 'm', 12)]
    return prims + [('text', x, y, t, 11) for x, y, t in labels]


def zig(b_lab, d_lab, e_lab):
    """AB ∥ CD with a bent path B–E–D; the angles at B and D are measured towards A and C."""
    return [('line', 0, 20, 240, 20), ('line', 0, 140, 240, 140), ('line', 40, 20, 190, 80), ('line', 40, 140, 190, 80),
            ('text', 40, 6, 'B', 12), ('text', 236, 6, 'A', 12), ('text', 40, 156, 'D', 12), ('text', 236, 156, 'C', 12),
            ('text', 204, 80, 'E', 12), ('text', 98, 31, b_lab, 11), ('text', 98, 129, d_lab, 11), ('text', 168, 80, e_lab, 11)]


QUESTIONS = [
    # ---------------- Part 1 · Number System
    dict(ch='1', scen='journey 2/3 by car 1/4 by bus and 5 km on foot',
         stem='Suresh travels 2/3 of a journey by car, 1/4 of it by bus and walks the last 5 km. How long is the whole journey?',
         opts=['60 km', '45 km', '30 km', '72 km'],
         hint='What fraction of the journey is walked?',
         sol='Car and bus: 2/3 + 1/4 = 11/12. Walked: 1/12 of the journey = 5 km. Whole journey: 60 km.'),
    dict(ch='1', scen='rational between −1/2 and −1/3 among four choices',
         stem='Which of these rational numbers lies between −1/2 and −1/3?',
         opts=['−5/12', '−7/12', '−1/4', '−7/24'],
         hint='Write everything with the denominator 24: −1/2 = −12/24 and −1/3 = −8/24.',
         sol='−5/12 = −10/24 lies between −12/24 and −8/24. −7/12 = −14/24 is below −1/2. −1/4 = −6/24 and −7/24 are above −1/3.'),
    dict(ch='1', scen='telescoping sum (1/2 − 1/3) + … + (1/10 − 1/11)',
         stem='What is (1/2 − 1/3) + (1/3 − 1/4) + (1/4 − 1/5) + … + (1/10 − 1/11)?',
         opts=['9/22', '1/2', '10/11', '9/11'],
         hint='Look at what cancels.',
         sol='Every middle term cancels: −1/3 with +1/3, −1/4 with +1/4, and so on. Only 1/2 − 1/11 = 11/22 − 2/22 = 9/22 is left.'),

    # ---------------- Part 2 · Operations
    dict(ch='2', scen='(6⁴ × 9² × 5⁴) ÷ (3⁵ × 10⁴)',
         stem='What is (6⁴ × 9² × 5⁴) ÷ (3⁵ × 10⁴)?',
         opts=['27', '9', '81', '3'],
         hint='Write every number as powers of 2, 3 and 5.',
         sol='Top: 2⁴ × 3⁴ × 3⁴ × 5⁴. Bottom: 3⁵ × 2⁴ × 5⁴ = 3⁴ × 3 × 2⁴ × 5⁴. Cancel 2⁴, 5⁴ and one 3⁴: what is left is 3⁴ ÷ 3 = 3³ = 27.'),
    dict(ch='2', scen='notes of 3.2 × 10⁵ pages in books of 8 × 10² pages packed 2.5 × 10 to a box',
         stem='A library has 3.2 × 10⁵ pages of notes to print as books of 8 × 10² pages each. The books are packed 2.5 × 10 to a box. How many boxes are needed?',
         opts=['16', '160', '40', '1,600'],
         hint='Find the number of books first.',
         sol='Books: (3.2 × 10⁵) ÷ (8 × 10²) = 0.4 × 10³ = 400. Boxes: 400 ÷ 25 = 16.'),

    # ---------------- Part 3 · Fractions, Decimals & Percentages
    dict(ch='3', scen='cost to selling price 5 : 6 · profit ₹140 · sold ₹70 less',
         stem='The cost price and the selling price of a radio are in the ratio 5 : 6, and the profit is ₹140. If the radio had been sold for ₹70 less, what would the profit or loss have been?',
         opts=['10% profit', '20% profit', '10% loss', '5% profit'],
         hint='The profit is 1 part of the ratio.',
         sol='1 part = ₹140, so the cost price is 5 × 140 = ₹700 and the selling price ₹840. Selling for ₹770 gives a profit of ₹70, which is 70/700 = 10% profit.'),
    dict(ch='3', scen='two fans sold at ₹1,200 each · 20% gain on one and 20% loss on the other',
         stem='A shopkeeper sells two fans for ₹1,200 each. On one he gains 20%; on the other he loses 20%. What is his overall result?',
         opts=['4% loss', 'No profit or loss', '4% gain', '2% loss'],
         hint='Find the cost price of each fan first.',
         sol='Fan 1: 1,200 is 120% of cost, so cost = ₹1,000. Fan 2: 1,200 is 80% of cost, so cost = ₹1,500. Total cost ₹2,500, total sale ₹2,400. Loss ₹100, which is 100/2,500 = 4%.'),
    dict(ch='3', scen='winner gets 58% of votes and wins by 2,400',
         stem='In an election with two candidates, the winner got 58% of the valid votes and won by 2,400 votes. How many valid votes were cast?',
         opts=['15,000', '4,138', '24,000', '14,400'],
         hint='The loser got 42%. What percent is the winning margin?',
         sol='Margin = 58% − 42% = 16% of the votes = 2,400. Total = 2,400 ÷ 0.16 = 15,000.'),

    # ---------------- Part 4 · Algebra
    dict(ch='4', scen='7(x − 3) − 4(2x − 5) = x − 9 · value of x² − 2x',
         stem='If 7(x − 3) − 4(2x − 5) = x − 9, what is the value of x² − 2x?',
         opts=['8', '16', '4', '24'],
         hint='Expand carefully: −4 × −5 = +20.',
         sol='7x − 21 − 8x + 20 = x − 9, so −x − 1 = x − 9, giving 2x = 8 and x = 4. Then x² − 2x = 16 − 8 = 8.'),
    dict(ch='4', scen='expression to add to two sides to reach 4a + 3',
         stem='Two sides of a triangle are (2a + b) and (a − 2b + 3). Which expression must be added to their sum to get 4a + 3?',
         opts=['a + b', 'a − b', '7a − b + 6', '−a + b'],
         hint='Find the sum of the two sides, then subtract it from 4a + 3.',
         sol='Sum: (2a + b) + (a − 2b + 3) = 3a − b + 3. Needed: (4a + 3) − (3a − b + 3) = a + b.'),
    dict(ch='4', scen='daughter 2/5 of mother now and half in 8 years',
         stem='Meena\'s age is 2/5 of her mother\'s age. In 8 years, Meena\'s age will be half of her mother\'s. How old is Meena now?',
         opts=['16 years', '40 years', '24 years', '20 years'],
         hint='Let the mother\'s age be m.',
         sol='2m/5 + 8 = (m + 8)/2. Multiply by 10: 4m + 80 = 5m + 40, so m = 40. Meena is 2/5 × 40 = 16.'),

    # ---------------- Part 5 · Geometry
    dict(ch='5', scen='corresponding angles 72° and 4x − 8 · value of x',
         fig=drawing(260, 150, trans([(200, 28, '72°'), (140, 98, '(4x − 8)°')])),
         stem='Lines l and m are parallel, and the two marked angles are corresponding angles. What is the value of x?',
         opts=['20', '16', '27', '18'],
         hint='Corresponding angles are equal when the lines are parallel.',
         sol='4x − 8 = 72, so 4x = 80 and x = 20. (27 comes from using 4x − 8 + 72 = 180, which is for co-interior angles.)'),
    dict(ch='5', scen='angles in ratio 2 : 3 : 4 · largest minus smallest exterior angle',
         stem='The angles of a triangle are in the ratio 2 : 3 : 4. What is the difference between its largest and smallest exterior angles?',
         opts=['40°', '20°', '60°', '80°'],
         hint='Find the interior angles first. The smallest interior angle gives the largest exterior angle.',
         sol='Interior angles: 40°, 60°, 80°. Exterior angles: 140°, 120°, 100°. Difference: 140° − 100° = 40°.'),
    dict(ch='5', scen='rectangle diagonals at O with angle AOB 110° · angle OCB plus angle AOD',
         stem='The diagonals of rectangle ABCD meet at O, and angle AOB = 110°. What is angle OCB + angle AOD?',
         opts=['125°', '145°', '90°', '165°'],
         hint='The diagonals of a rectangle are equal and bisect each other, so OA = OB = OC = OD.',
         sol='Angle AOD = 180° − 110° = 70° (angles on a line). Angle BOC = 70° too, and OB = OC, so angle OCB = (180° − 70°) ÷ 2 = 55°. Sum: 55° + 70° = 125°.'),

    # ---------------- Part 6 · Mensuration
    dict(ch='6', scen='cylinders of equal volume with radii 2 : 3 · heights ratio',
         stem='Two cylinders have the same volume. Their radii are in the ratio 2 : 3. What is the ratio of their heights?',
         opts=['9 : 4', '3 : 2', '4 : 9', '2 : 3'],
         hint='Volume depends on radius × radius × height.',
         sol='2 × 2 × h₁ = 3 × 3 × h₂, so h₁ : h₂ = 9 : 4. The narrower cylinder must be taller.'),
    dict(ch='6', scen='tank 3 m by 2 m filled to 1.5 m · 4,500 L drawn out',
         stem='A tank with a rectangular base 3 m × 2 m has water 1.5 m deep. 4,500 litres are drawn out. How deep is the water now?',
         opts=['0.75 m', '1.25 m', '0.5 m', '1 m'],
         hint='4,500 L = 4.5 m³.',
         sol='Fall in level = 4.5 ÷ (3 × 2) = 0.75 m. New depth = 1.5 − 0.75 = 0.75 m.'),
    dict(ch='6', scen='6 cm cube cut into 2 cm cubes · surface area multiplied by',
         stem='A cube of edge 6 cm is cut into cubes of edge 2 cm. How many times the original surface area is the total surface area of the small cubes?',
         opts=['3 times', '9 times', '27 times', '2 times'],
         hint='Count the small cubes and compare surface areas.',
         sol='Small cubes: 3 × 3 × 3 = 27, each with surface 24 cm²: 648 cm². Original: 6 × 36 = 216 cm². 648 ÷ 216 = 3.'),

    # ---------------- Part 7 · Data Handling
    dict(ch='8', scen='frequency table of marks out of 50 · mean',
         fig=table(['Marks', '10', '20', '30', '40', '50'], [['Students', '2', '5', '8', '3', '2']], widths=[90, 50, 50, 50, 50, 50]),
         stem='The table shows the marks scored by 20 students in a quiz. What is the mean mark?',
         opts=['29', '30', '28', '31'],
         hint='Multiply each mark by its number of students and add.',
         sol='10 × 2 + 20 × 5 + 30 × 8 + 40 × 3 + 50 × 2 = 20 + 100 + 240 + 120 + 100 = 580. Mean = 580 ÷ 20 = 29. (30 is the median and mode.)'),
    dict(ch='8', scen='pie chart of 120 students · cricket 45 · football a third of the rest',
         stem='In a class of 120 students, 45 like cricket best. Of the rest, one-third like football best. In a pie chart of this data, what is the angle for football?',
         opts=['75°', '25°', '120°', '90°'],
         hint='Find the number who like football first.',
         sol='Not cricket: 75 students. Football: 75 ÷ 3 = 25. Angle = 25/120 × 360° = 75°.'),

    # ---------------- Part 8 · Applied Mathematics
    dict(ch='9', scen='₹4,500 shared 6 : 3 : 1 · Kavya gives ₹450 to Om · new ratio',
         stem="₹4,500 is shared among Kavya, Yash and Om. Kavya gets twice as much as Yash, and Yash gets three times as much as Om. Kavya then gives ₹450 to Om. What is the ratio of Kavya's money to Om's now?",
         opts=['5 : 2', '6 : 1', '3 : 1', '2 : 5'],
         hint='Let Om get x. Then Yash gets 3x and Kavya 6x.',
         sol='10x = 4,500, so x = 450: Kavya ₹2,700, Om ₹450. After the gift: Kavya ₹2,250 and Om ₹900. 2,250 : 900 = 5 : 2.'),
    dict(ch='9', scen='fort food for 300 soldiers for 40 days · 100 leave after 10 days',
         stem='A fort has food for 300 soldiers for 40 days. After 10 days, 100 soldiers leave. For how many more days does the food last?',
         opts=['45', '30', '40', '20'],
         hint='Count the food in soldier-days.',
         sol='Food: 300 × 40 = 12,000 soldier-days. After 10 days, 12,000 − 3,000 = 9,000 are left for 200 soldiers: 9,000 ÷ 200 = 45 more days.'),
    dict(ch='9', scen='towns 210 km apart · cars at 40 and 30 km/h towards each other',
         stem='Two towns are 210 km apart. Two cars start at the same time from the towns, driving towards each other at 40 km/h and 30 km/h. How far from the faster car\'s town do they meet?',
         opts=['120 km', '90 km', '105 km', '140 km'],
         hint='They close the gap at 40 + 30 km/h.',
         sol='They meet after 210 ÷ 70 = 3 hours. The faster car has gone 40 × 3 = 120 km.'),

    # ---------------- Part 9 · Mathematical Reasoning
    dict(ch='10', scen='AB + BC + CA = ABC',
         stem='A, B and C are digits and AB, BC, CA are 2-digit numbers. AB + BC + CA = ABC, a 3-digit number. What is A + B + C?',
         opts=['18', '19', '17', '16'],
         hint='AB + BC + CA = 11 × (A + B + C). So ABC is 11 times its own digit sum.',
         sol='Try the 3-digit multiples of 11: only 198 = 11 × 18 has digit sum 18. So A + B + C = 18. Check: 19 + 98 + 81 = 198.'),
    dict(ch='10', scen='ways to climb 6 steps taking 1 or 2 at a time',
         stem='Gita climbs a staircase of 6 steps. Each move she climbs either 1 step or 2 steps. In how many different ways can she reach the top?',
         opts=['13', '8', '21', '12'],
         hint='The ways to reach step n = ways to reach step n − 1 + ways to reach step n − 2.',
         sol='Steps 1 to 6: 1, 2, 3, 5, 8, 13 ways. She can reach the top in 13 ways.'),
    dict(ch='10', scen='numbers from 100 to 200 divisible by both 4 and 6',
         stem='How many numbers from 100 to 200 are divisible by both 4 and 6?',
         opts=['8', '9', '16', '25'],
         hint='Divisible by both 4 and 6 means divisible by 12, not 24.',
         sol='Multiples of 12 from 100 to 200: 108, 120, 132, 144, 156, 168, 180, 192. That is 8.'),

    # ---------------- Part 10 · Mixed Problems
    dict(ch='4+10', scen='machine doubling and subtracting 3 used twice gives 29',
         stem='A number machine doubles a number and then subtracts 3. Pari puts a number in, and puts the result through the machine again. The final output is 29. What number did she start with?',
         opts=['9.5', '8', '16', '11'],
         hint='Work backwards: undo "subtract 3", then undo "double".',
         sol='Second time: 29 + 3 = 32, halved = 16. First time: 16 + 3 = 19, halved = 9.5. Check: 9.5 → 16 → 29.'),
    dict(ch='3+10', scen='60% girls · 25% of girls and 50% of boys play chess',
         stem='In a school, 60% of the students are girls. 25% of the girls and 50% of the boys play chess. What percent of all students play chess?',
         opts=['35%', '37.5%', '75%', '30%'],
         hint='Take 100 students.',
         sol='60 girls: 15 play. 40 boys: 20 play. 35 out of 100 = 35%. (37.5% just averages 25% and 50%.)'),
    dict(ch='4+9', scen='there at 30 km/h back at 20 km/h in 5 hours',
         stem='Aarav cycles from P to Q at 30 km/h and returns along the same road at 20 km/h. The round trip takes 5 hours. How far is P from Q?',
         opts=['60 km', '50 km', '75 km', '100 km'],
         hint='Time = distance ÷ speed. d/30 + d/20 = 5.',
         sol='d/30 + d/20 = 2d/60 + 3d/60 = d/12 = 5, so d = 60 km.'),
    dict(ch='5+6', scen='largest cylinder cut from a 14 by 14 by 20 block · wood wasted',
         stem='The largest possible cylinder is carved from a wooden block 14 cm × 14 cm × 20 cm, with its height along the 20 cm edge. How much wood is wasted? (π = 22/7)',
         opts=['840 cm³', '3,080 cm³', '3,920 cm³', '1,260 cm³'],
         hint='The cylinder has radius 7 cm and height 20 cm.',
         sol='Block: 14 × 14 × 20 = 3,920 cm³. Cylinder: 22/7 × 7 × 7 × 20 = 3,080 cm³. Wasted: 840 cm³.'),
    dict(ch='1+4', scen='(x + 2)/(x − 1) = 4/3',
         stem='Solve (x + 2)/(x − 1) = 4/3. What is x?',
         opts=['10', '−10', '2', '−2'],
         hint='Cross-multiply.',
         sol='3(x + 2) = 4(x − 1), so 3x + 6 = 4x − 4 and x = 10. Check: 12/9 = 4/3.'),
]
