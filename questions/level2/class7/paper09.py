# AMO Level-2 · Class 7 · Practice Paper 9
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
    dict(ch='1', scen='ribbon · 1/3 used then 3/8 of the rest · 15 m left',
         stem='Rani uses 1/3 of a ribbon, and then 3/8 of what is left. Now 15 m of ribbon remain. How long was the ribbon at first?',
         opts=['36 m', '40 m', '24 m', '45 m'],
         hint='What fraction of the whole ribbon is left at the end?',
         sol='After the first cut 2/3 is left. She then keeps 5/8 of that: 5/8 × 2/3 = 5/12 of the ribbon = 15 m. The ribbon was 15 × 12/5 = 36 m.'),
    dict(ch='1', scen='product (−3/4)(8/−9)(−5/6)(−9/10)',
         stem='What is (−3/4) × (8/−9) × (−5/6) × (−9/10)?',
         opts=['1/2', '−1/2', '2', '−2'],
         hint='First count the negative signs to decide the sign of the answer.',
         sol='There are four negative signs, so the product is positive. Size: (3 × 8 × 5 × 9) ÷ (4 × 9 × 6 × 10) = 1,080 ÷ 2,160 = 1/2.'),
    dict(ch='1', scen='p/q equal to −2/3 with q − p = 25',
         stem='p and q are integers with p/q = −2/3 and q − p = 25. What is p?',
         opts=['−10', '10', '−15', '15'],
         hint='Write p = −2k and q = 3k for some integer k.',
         sol='q − p = 3k + 2k = 5k = 25, so k = 5. p = −10 and q = 15. (Taking p = 2k, q = −3k gives k = −5 and the same p = −10.)'),

    # ---------------- Part 2 · Operations
    dict(ch='2', scen='2ˣ × 3ʸ = 72 · value of xʸ + yˣ',
         stem='x and y are whole numbers with 2ˣ × 3ʸ = 72. What is xʸ + yˣ?',
         opts=['17', '13', '12', '25'],
         hint='Write 72 as a product of prime factors.',
         sol='72 = 8 × 9 = 2³ × 3², so x = 3 and y = 2. xʸ + yˣ = 3² + 2³ = 9 + 8 = 17.'),
    dict(ch='2', scen='zeros at the end of 5⁵ × 4⁴ × 2²',
         stem='How many zeros are there at the end of 5⁵ × 4⁴ × 2²?',
         opts=['5', '10', '4', '8'],
         hint='Each zero needs one 2 and one 5.',
         sol='Each 4 gives two 2s, so 4⁴ × 2² has 4 × 2 + 2 = 10 factors of 2, but there are only five 5s. Pair five 2s with the five 5s: the number is 2⁵ × 10⁵ = 32 × 10⁵, which ends in 5 zeros.'),

    # ---------------- Part 3 · Fractions, Decimals & Percentages
    dict(ch='3', scen='oranges bought 6 for ₹10 sold 4 for ₹10',
         stem='Ojas buys oranges at 6 for ₹10 and sells them at 4 for ₹10. What is his profit percent?',
         opts=['50%', '33 1/3%', '25%', '40%'],
         hint='Find the cost and selling price of 12 oranges.',
         sol='12 oranges cost ₹20 and sell for ₹30. Profit ₹10 on ₹20 = 50%. (33 1/3% divides by the selling price.)'),
    dict(ch='3', scen='marked ₹2,800 · 15% discount still gives 19% profit',
         stem='A shopkeeper marks a cycle at ₹2,800 and gives a 15% discount. He still makes a 19% profit. What did the cycle cost him?',
         opts=['₹2,000', '₹2,380', '₹1,904', '₹2,240'],
         hint='First find the selling price.',
         sol='Selling price = 85% of 2,800 = ₹2,380. This is 119% of the cost, so the cost = 2,380 ÷ 1.19 = ₹2,000.'),
    dict(ch='3', scen='basket with 30% mangoes · 40% of the rest apples · 84 others',
         stem='In a fruit basket, 30% of the fruits are mangoes and 40% of the remaining fruits are apples. The other 84 fruits are bananas. How many fruits are in the basket?',
         opts=['200', '120', '280', '140'],
         hint='Bananas are 60% of the 70% that are not mangoes.',
         sol='Not mangoes: 70%. Bananas: 60% of 70% = 42% of all fruits = 84. Total = 84 ÷ 0.42 = 200.'),

    # ---------------- Part 4 · Algebra
    dict(ch='4', scen='father 4 more than 3 times son · 4 years ago 6 more than 4 times',
         stem='A father\'s age is 4 more than three times his son\'s age. Four years ago, it was 6 more than four times the son\'s age then. How old is the father now?',
         opts=['34 years', '30 years', '38 years', '10 years'],
         hint='Let the son be s years old; the father is 3s + 4.',
         sol='Four years ago: 3s + 4 − 4 = 4(s − 4) + 6, so 3s = 4s − 10 and s = 10. The father is 3 × 10 + 4 = 34.'),
    dict(ch='4', scen='2(3x − 4) − 3(x − 2) + 4(x + 1) at x = −3',
         stem='Simplify 2(3x − 4) − 3(x − 2) + 4(x + 1) and find its value when x = −3.',
         opts=['−19', '23', '−23', '19'],
         hint='Expand each bracket carefully: −3 × (−2) = +6.',
         sol='6x − 8 − 3x + 6 + 4x + 4 = 7x + 2. At x = −3: 7 × (−3) + 2 = −19.'),
    dict(ch='4', scen='five consecutive integers adding to −15',
         stem='Five consecutive integers add up to −15. What is the product of the smallest and the largest?',
         opts=['5', '−5', '15', '−15'],
         hint='The middle integer is the average.',
         sol='The middle integer is −15 ÷ 5 = −3, so the integers are −5, −4, −3, −2, −1. (−5) × (−1) = 5.'),

    # ---------------- Part 5 · Geometry
    dict(ch='5', scen='point on line l joined to two points on parallel line m with 55° and 60°',
         stem='Lines l and m are parallel. P is on l; Q and R are on m. Line PQ makes 55° with l on one side of P, and PR makes 60° with l on the other side. What is angle QPR?',
         opts=['65°', '115°', '55°', '60°'],
         hint='The three angles at P along line l make a straight angle.',
         sol='The angles at P on one side of line l are 55°, angle QPR and 60°, which add up to 180°. Angle QPR = 180° − 55° − 60° = 65°. (They are also the angles of triangle PQR, by alternate angles.)'),
    dict(ch='5', scen='each angle less than the sum of the other two',
         stem='In a triangle, each angle is less than the sum of the other two angles. What kind of triangle must it be?',
         opts=['Acute-angled', 'Right-angled', 'Obtuse-angled', 'Equilateral'],
         hint='If an angle is less than the sum of the other two, it is less than half of 180°.',
         sol='Each angle A < B + C = 180° − A, so A < 90°. All three angles are acute. (It need not be equilateral.)'),
    dict(ch='5', scen='ABC congruent to QRP · perimeter and angle R',
         stem='Triangle ABC is congruent to triangle QRP, with the vertices in that order. AB = 6 cm, BC = 8 cm, QP = 7 cm and angle B = 70°. What are the perimeter of triangle QRP and angle R?',
         opts=['21 cm and 70°', '21 cm and 40°', '20 cm and 70°', '22 cm and 70°'],
         hint='Match the vertices in order: A with Q, B with R, C with P.',
         sol='QR = AB = 6 cm, RP = BC = 8 cm and QP = 7 cm, so the perimeter is 21 cm. R matches B, so angle R = 70°.'),

    # ---------------- Part 6 · Mensuration
    dict(ch='6', scen='pipe of radius 1 cm flowing at 7 m/s into a 66 L tank',
         stem='Water flows at 7 m per second through a pipe of inner radius 1 cm into an empty 66-litre tank. How long does it take to fill the tank? (π = 22/7)',
         opts=['30 s', '3 s', '300 s', '60 s'],
         hint='Each second a cylinder of water 700 cm long comes out.',
         sol='Per second: 22/7 × 1 × 1 × 700 = 2,200 cm³. 66 L = 66,000 cm³. Time = 66,000 ÷ 2,200 = 30 s.'),
    dict(ch='6', scen='cuboid 12 by 9 by 6 cut into 3 cm cubes · total surface area of the cubes',
         stem='A cuboid 12 cm × 9 cm × 6 cm is cut into cubes of edge 3 cm. What is the total surface area of all the cubes?',
         opts=['1,296 cm²', '648 cm²', '468 cm²', '216 cm²'],
         hint='Count how many cubes fit along each edge.',
         sol='Cubes: 4 × 3 × 2 = 24, each with surface 6 × 9 = 54 cm². Total 24 × 54 = 1,296 cm². (468 cm² is the surface of the cuboid.)'),
    dict(ch='6', scen='tiles 1.5 m by 1 m for the floor and walls of an 8 by 6 by 4 m room',
         stem='A room is 8 m long, 6 m wide and 4 m high. Tiles of 1.5 m × 1 m are used to cover its floor and four walls. What is the least number of tiles needed? (Tiles may be cut and the pieces used.)',
         opts=['107', '106', '160', '75'],
         hint='Area to cover = floor + four walls.',
         sol='Floor: 48 m². Walls: 2 × (8 + 6) × 4 = 112 m². Total 160 m². Each tile is 1.5 m², and 160 ÷ 1.5 = 106.7, so at least 107 tiles.'),

    # ---------------- Part 7 · Data Handling
    dict(ch='8', scen='bar graph of cars made each year · greatest percentage increase',
         fig=drawing(330, 200, bars([('2020', 200), ('2021', 300), ('2022', 250), ('2023', 350), ('2024', 400)], 450, 50, 'Cars made')),
         stem='The bar graph shows the number of cars a factory made each year. In which year was the percentage increase over the year before the greatest?',
         opts=['2021', '2023', '2024', '2022'],
         hint='Percentage increase = increase ÷ previous year × 100.',
         sol='2021: 100/200 = 50%. 2022: a fall. 2023: 100/250 = 40%. 2024: 50/350 ≈ 14%. The greatest is in 2021.'),
    dict(ch='8', scen='6 8 8 x 10 12 with mean 9 · median',
         stem='The numbers 6, 8, 8, x, 10 and 12 have a mean of 9. What is their median?',
         opts=['9', '8', '10', '8.5'],
         hint='Find x first, then put the numbers in order.',
         sol='Total = 6 × 9 = 54, so x = 54 − 44 = 10. In order: 6, 8, 8, 10, 10, 12. Median = (8 + 10) ÷ 2 = 9.'),

    # ---------------- Part 8 · Applied Mathematics
    dict(ch='9', scen='numbers in ratio 3 : 4 becoming 1 : 2 when 6 is subtracted',
         stem='Two numbers are in the ratio 3 : 4. When 6 is subtracted from each, the ratio becomes 1 : 2. What is the larger number?',
         opts=['12', '9', '18', '24'],
         hint='Let the numbers be 3x and 4x.',
         sol='(3x − 6)/(4x − 6) = 1/2, so 6x − 12 = 4x − 6 and x = 3. The numbers are 9 and 12; the larger is 12.'),
    dict(ch='9', scen='bus 8 h at 45 km/h · 2 hours sooner with a 1-hour stop',
         stem='A bus usually takes 8 hours for a journey at 45 km/h. Today it must arrive 2 hours sooner, and it also stops for 1 hour on the way. At what speed must it travel?',
         opts=['72 km/h', '60 km/h', '80 km/h', '65 km/h'],
         hint='The distance stays the same; find the time left for moving.',
         sol='Distance: 45 × 8 = 360 km. Time today: 8 − 2 = 6 hours, of which 1 hour is the stop, leaving 5 hours. Speed: 360 ÷ 5 = 72 km/h. (60 km/h forgets the stop.)'),
    dict(ch='9', scen='two bottle machines joined by a third after 10 minutes · time for 1,200',
         stem='One machine makes 120 bottles in 8 minutes. Two such machines start together, and a third joins them after 10 minutes. How long after the start are 1,200 bottles made in all?',
         opts=['30 minutes', '27 minutes', '40 minutes', '20 minutes'],
         hint='One machine makes 15 bottles a minute.',
         sol='Each machine makes 120 ÷ 8 = 15 a minute. First 10 minutes: 2 × 15 × 10 = 300. Left: 900 at 45 a minute = 20 minutes. Total: 10 + 20 = 30 minutes.'),

    # ---------------- Part 9 · Mathematical Reasoning
    dict(ch='10', scen='ABCD × 4 = DCBA',
         stem='In ABCD × 4 = DCBA, each letter is a digit and both are 4-digit numbers. What is A + B + C + D?',
         opts=['18', '16', '20', '22'],
         hint='A × 4 must still be a single digit, and DCBA is even.',
         sol='DCBA = 4 × ABCD is even, so its last digit A is even, and 4 × A must be a single digit, so A = 2. Then D ≥ 8 and 4 × D ends in 2, so D = 8. Working through the middle digits gives 2178 × 4 = 8712. A + B + C + D = 2 + 1 + 7 + 8 = 18.'),
    dict(ch='10', scen='4-digit numbers from digits 1 2 3 with at least one 1',
         stem='How many 4-digit numbers use only the digits 1, 2 and 3 (repeats allowed) and contain at least one digit 1?',
         opts=['65', '16', '81', '54'],
         hint='Count all such numbers, then take away those with no 1 at all.',
         sol='All: 3 × 3 × 3 × 3 = 81. With no 1 (only 2s and 3s): 2 × 2 × 2 × 2 = 16. At least one 1: 81 − 16 = 65.'),
    dict(ch='10', scen='numbers of the form n times n plus 1 below 200',
         stem='Each number in the list 2, 5, 10, 17, 26, … is 1 more than a whole number multiplied by itself. How many numbers in the list are less than 200?',
         opts=['14', '13', '15', '199'],
         hint='The nth number is n × n + 1.',
         sol='14 × 14 + 1 = 197 is less than 200, but 15 × 15 + 1 = 226 is not. So the numbers for n = 1 to 14 are less than 200: 14 numbers.'),

    # ---------------- Part 10 · Mixed Problems
    dict(ch='4+10', scen='50 × 50 − 49 × 51 + 30 × 30 − 29 × 31',
         stem='What is the value of 50 × 50 − 49 × 51 + 30 × 30 − 29 × 31?',
         opts=['2', '0', '1', '100'],
         hint='Try smaller cases first, such as 5 × 5 − 4 × 6.',
         sol='49 × 51 = (50 − 1) × 51 = 2,550 − 51 = 2,499, so 50 × 50 − 49 × 51 = 2,500 − 2,499 = 1. In the same way 29 × 31 = 899, and 900 − 899 = 1. Total: 1 + 1 = 2.'),
    dict(ch='3+10', scen='200 changed by +50% then −50% twice',
         stem='Starting from 200, Riya increases the number by 50% and then decreases the result by 50%. She repeats both steps once more. What number does she end with?',
         opts=['112.5', '200', '150', '100'],
         hint='One round multiplies by 1.5 × 0.5.',
         sol='One round: 1.5 × 0.5 = 0.75. Two rounds: 200 × 0.75 × 0.75 = 112.5.'),
    dict(ch='4+9', scen='₹500 in ₹5 and ₹10 coins with 40 more ₹5 coins',
         stem='Neel has ₹500 in ₹5 and ₹10 coins. He has 40 more ₹5 coins than ₹10 coins. How many ₹5 coins does he have?',
         opts=['60', '20', '40', '80'],
         hint='Let the number of ₹10 coins be x.',
         sol='10x + 5(x + 40) = 500, so 15x + 200 = 500 and x = 20. He has 20 coins of ₹10 and 60 coins of ₹5.'),
    dict(ch='5+6', scen='earth from a well of radius 3.5 m depth 10 m spread on a 55 by 14 m field',
         stem='A cylindrical well of radius 3.5 m is dug 10 m deep. The earth taken out is spread evenly over a field 55 m × 14 m. By how much does the level of the field rise? (π = 22/7)',
         opts=['0.5 m', '1 m', '0.25 m', '5 m'],
         hint='Volume of earth = volume of the well.',
         sol='Earth: 22/7 × 3.5 × 3.5 × 10 = 385 m³. Field: 55 × 14 = 770 m². Rise = 385 ÷ 770 = 0.5 m.'),
    dict(ch='1+4', scen='x² − y² + xy at x = −1/2 y = 1/3',
         stem='What is the value of x² − y² + xy when x = −1/2 and y = 1/3?',
         opts=['−1/36', '11/36', '1/36', '−11/36'],
         hint='Work out each term with the denominator 36.',
         sol='x² = 1/4 = 9/36, y² = 1/9 = 4/36, xy = −1/6 = −6/36. 9/36 − 4/36 − 6/36 = −1/36.'),
]
