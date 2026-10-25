# AMO Level-2 · Class 7 · Practice Paper 7
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
    dict(ch='1', scen='tank 3/5 full falls to 1/3 full after 24 L used',
         stem='A water tank is 3/5 full. After 24 litres are used, it is 1/3 full. How many litres does the full tank hold?',
         opts=['90 L', '72 L', '60 L', '120 L'],
         hint='The 24 litres are the difference between 3/5 and 1/3 of the tank.',
         sol='3/5 − 1/3 = 9/15 − 5/15 = 4/15 of the tank is 24 L. The full tank holds 24 × 15/4 = 90 L.'),
    dict(ch='1', scen='smallest of −11/12 −7/8 −5/6 −13/16',
         stem='Which is the smallest of −11/12, −7/8, −5/6 and −13/16?',
         opts=['−11/12', '−13/16', '−5/6', '−7/8'],
         hint='For negative numbers, the one furthest from 0 is the smallest. Use the denominator 48.',
         sol='In 48ths: −44, −42, −40, −39. The one furthest from 0 is −44/48 = −11/12, so it is the smallest.'),
    dict(ch='1', scen='(−2/5) ÷ (4/15) − (3/8)(−4/9)',
         stem='What is (−2/5) ÷ (4/15) − (3/8) × (−4/9)?',
         opts=['−4/3', '4/3', '−5/3', '−7/6'],
         hint='Work out the division and the product separately. Subtracting a negative is adding.',
         sol='(−2/5) × (15/4) = −3/2. (3/8) × (−4/9) = −1/6. −3/2 − (−1/6) = −9/6 + 1/6 = −8/6 = −4/3.'),

    # ---------------- Part 2 · Operations
    dict(ch='2', scen='(−2)³ × (−2)ˣ = 64',
         stem='Find x if (−2)³ × (−2)ˣ = 64.',
         opts=['3', '2', '−3', '6'],
         hint='64 = (−2)⁶, because an even power of a negative number is positive.',
         sol='(−2)³⁺ˣ = (−2)⁶, so 3 + x = 6 and x = 3. Check: (−2)³ × (−2)³ = (−8)(−8) = 64.'),
    dict(ch='2', scen='compare 2⁵ × 3² with 3⁴ × 2²',
         stem='Which is greater, 2⁵ × 3² or 3⁴ × 2², and by how much?',
         opts=['3⁴ × 2², by 36', '2⁵ × 3², by 36', 'They are equal', '3⁴ × 2², by 18'],
         hint='Both share the factor 2² × 3² = 36.',
         sol='2⁵ × 3² = 36 × 2³ = 288. 3⁴ × 2² = 36 × 3² = 324. 324 − 288 = 36, so 3⁴ × 2² is greater by 36.'),

    # ---------------- Part 3 · Fractions, Decimals & Percentages
    dict(ch='3', scen='two items sold at ₹990 each · 10% gain and 10% loss',
         stem='Shalini sells two lamps for ₹990 each. On one she gains 10% and on the other she loses 10%. What is her overall result?',
         opts=['A loss of ₹20', 'No profit or loss', 'A profit of ₹20', 'A loss of ₹99'],
         hint='Find each cost price: 990 is 110% of one and 90% of the other.',
         sol='Costs: 990 ÷ 1.1 = ₹900 and 990 ÷ 0.9 = ₹1,100. Total cost ₹2,000, total selling ₹1,980: a loss of ₹20.'),
    dict(ch='3', scen='₹1,500 sold for ₹1,215 after two discounts the first 10%',
         stem='A bag marked ₹1,500 is sold for ₹1,215 after two successive discounts. The first discount is 10%. What is the second discount?',
         opts=['10%', '9%', '12%', '19%'],
         hint='Find the price after the first discount.',
         sol='After 10% off: ₹1,350. From 1,350 to 1,215 is a cut of ₹135, which is 135/1,350 = 10%.'),
    dict(ch='3', scen='spends 75% · income up 20% expenses up 10% · savings change',
         stem='Ravi spends 75% of his income and saves the rest. His income rises by 20% and his spending rises by 10%. By what percent do his savings rise?',
         opts=['50%', '30%', '10%', '25%'],
         hint='Take his income as ₹100.',
         sol='Income 100: spending 75, savings 25. New income 120, new spending 82.5, new savings 37.5. Savings rise by 12.5 on 25 = 50%.'),

    # ---------------- Part 4 · Algebra
    dict(ch='4', scen='triangle sides x x + 5 and 2x − 2 with perimeter 55',
         stem='The sides of a triangle are x cm, (x + 5) cm and (2x − 2) cm. Its perimeter is 55 cm. How long is its longest side?',
         opts=['24 cm', '18 cm', '13 cm', '26 cm'],
         hint='Add the three sides and solve for x.',
         sol='4x + 3 = 55, so x = 13. The sides are 13, 18 and 24 cm. The longest is 24 cm.'),
    dict(ch='4', scen='rectangle with length 3x − 1 width 9 perimeter 58 · area',
         stem='A rectangle has length (3x − 1) cm and width 9 cm. Its perimeter is 58 cm. What is its area?',
         opts=['180 cm²', '160 cm²', '58 cm²', '200 cm²'],
         hint='Perimeter = 2 × (length + width).',
         sol='2(3x − 1 + 9) = 58, so 3x + 8 = 29 and x = 7. Length = 20 cm. Area = 20 × 9 = 180 cm².'),
    dict(ch='4', scen='a number plus its third plus its quarter equals 57',
         stem='When a number, one-third of it and one-quarter of it are added, the total is 57. What is the number?',
         opts=['36', '24', '48', '12'],
         hint='x + x/3 + x/4 = 57.',
         sol='x + x/3 + x/4 = 12x/12 + 4x/12 + 3x/12 = 19x/12 = 57, so x = 36.'),

    # ---------------- Part 5 · Geometry
    dict(ch='5', scen='bent path between parallel lines · angles x + 20 x + 10 and 3x',
         fig=drawing(250, 165, zig('(x + 20)°', '(x + 10)°', '3x°')),
         stem='AB ∥ CD. The angles at B, D and E are marked. What is the size of angle BED?',
         opts=['90°', '30°', '60°', '120°'],
         hint='Angle BED equals the sum of the angles at B and D.',
         sol='Draw a line through E parallel to AB. Then angle BED = (x + 20) + (x + 10), so 3x = 2x + 30 and x = 30. Angle BED = 90°.'),
    dict(ch='5', scen='angle bisector of P in triangle PQR with Q = 70 and R = 50',
         stem='In triangle PQR, angle Q = 70° and angle R = 50°. The bisector of angle P meets QR at S. What is angle PSR?',
         opts=['100°', '80°', '110°', '70°'],
         hint='Find angle P first, then look at triangle PSR.',
         sol='Angle P = 60°, so angle SPR = 30°. In triangle PSR: angle PSR = 180° − 30° − 50° = 100°.'),
    dict(ch='5', scen='bisectors of two adjacent angles of a parallelogram',
         stem='In parallelogram ABCD, the bisectors of angles A and B meet at P. What is angle APB?',
         opts=['90°', '60°', '120°', 'It depends on angle A'],
         hint='Angles A and B add up to 180°.',
         sol='A + B = 180°, so A/2 + B/2 = 90°. In triangle APB, angle APB = 180° − 90° = 90°, whatever the size of A.'),

    # ---------------- Part 6 · Mensuration
    dict(ch='6', scen='hollow pipe outer radius 14 inner radius 7 length 10 cm',
         stem='A hollow metal pipe is 10 cm long. Its outer radius is 14 cm and its inner radius is 7 cm. What volume of metal is in the pipe? (π = 22/7)',
         opts=['4,620 cm³', '6,160 cm³', '1,540 cm³', '3,080 cm³'],
         hint='Metal = outer cylinder − inner cylinder.',
         sol='22/7 × (14 × 14 − 7 × 7) × 10 = 22/7 × 147 × 10 = 4,620 cm³. (6,160 cm³ is the outer cylinder alone.)'),
    dict(ch='6', scen='cuboid 8 by 6 by 4 with length doubled and width halved',
         stem='A cuboid is 8 cm × 6 cm × 4 cm. Its length is doubled and its width is halved; the height stays 4 cm. What happens to its total surface area?',
         opts=['It increases by 40 cm²', 'It stays the same', 'It increases by 64 cm²', 'It decreases by 40 cm²'],
         hint='The volume stays the same, but check the surface area.',
         sol='Old: 2(48 + 32 + 24) = 208 cm². New 16 × 3 × 4: 2(48 + 64 + 12) = 248 cm². It increases by 40 cm². (The volume is still 192 cm³.)'),
    dict(ch='6', scen='coins of radius 0.7 cm and thickness 0.5 cm from a 5.5 by 10 by 3.5 cuboid',
         stem='How many coins, each of radius 0.7 cm and thickness 0.5 cm, can be made by melting a metal cuboid 5.5 cm × 10 cm × 3.5 cm? (π = 22/7)',
         opts=['250', '125', '500', '275'],
         hint='Number of coins = volume of cuboid ÷ volume of one coin.',
         sol='Cuboid: 5.5 × 10 × 3.5 = 192.5 cm³. Coin: 22/7 × 0.7 × 0.7 × 0.5 = 0.77 cm³. Coins: 192.5 ÷ 0.77 = 250.'),

    # ---------------- Part 7 · Data Handling
    dict(ch='8', scen='pie chart of monthly spending · savings ₹4,800 · food amount',
         fig=drawing(230, 230, pie([('Rent 108°', 108), ('Food 90°', 90), ('Travel 36°', 36), ('Savings 72°', 72), ('Others 54°', 54)])),
         stem='The pie chart shows how Nandini\'s family uses its monthly income. The family saves ₹4,800 a month. How much does it spend on food?',
         opts=['₹6,000', '₹4,800', '₹7,200', '₹24,000'],
         hint='Savings are 72° out of 360°. Find the whole income first.',
         sol='72° is 1/5 of 360°, so the income is 5 × 4,800 = ₹24,000. Food is 90°, a quarter: ₹6,000.'),
    dict(ch='8', scen='shoe sizes frequency table · pupils above the median size',
         fig=table(['Shoe size', '5', '6', '7', '8', '9'], [['Pupils', '4', '9', '12', '7', '3']], widths=[90, 50, 50, 50, 50, 50]),
         stem='The table shows the shoe sizes of the pupils in a class. How many pupils wear a size larger than the median size?',
         opts=['10', '22', '7', '13'],
         hint='There are 35 pupils, so the median is the 18th pupil\'s size.',
         sol='Total 35. Counting up: size 5 covers pupils 1–4, size 6 covers 5–13, size 7 covers 14–25. The 18th pupil wears size 7. Larger sizes: 7 + 3 = 10 pupils.'),

    # ---------------- Part 8 · Applied Mathematics
    dict(ch='9', scen='boys to girls 7 : 5 · 8 boys leave 4 girls join · ratio 1 : 1',
         stem='In a class the ratio of boys to girls is 7 : 5. Then 8 boys leave and 4 girls join, and the numbers become equal. How many students were there at first?',
         opts=['72', '60', '84', '48'],
         hint='Let there be 7x boys and 5x girls.',
         sol='7x − 8 = 5x + 4, so x = 6. At first: 42 boys and 30 girls, 72 students.'),
    dict(ch='9', scen='6 L of petrol for 84 km · petrol for 315 km',
         stem='A scooter uses 6 litres of petrol to go 84 km. How much petrol does it need for 315 km?',
         opts=['22.5 L', '21 L', '24 L', '20 L'],
         hint='Find how far it goes on 1 litre.',
         sol='1 litre lasts 84 ÷ 6 = 14 km. For 315 km: 315 ÷ 14 = 22.5 L.'),
    dict(ch='9', scen='pipes filling in 12 h and 15 h with an outlet emptying in 20 h',
         stem='Pipe A fills a tank in 12 hours and pipe B fills it in 15 hours. Pipe C empties the full tank in 20 hours. If all three are opened together, how long does it take to fill the empty tank?',
         opts=['10 hours', '15 hours', '8 hours', '12 hours'],
         hint='In 1 hour A fills 1/12, B fills 1/15 and C empties 1/20.',
         sol='1/12 + 1/15 − 1/20 = 5/60 + 4/60 − 3/60 = 6/60 = 1/10 of the tank per hour. It fills in 10 hours.'),

    # ---------------- Part 9 · Mathematical Reasoning
    dict(ch='10', scen='AB × 6 = BBB',
         stem='A and B are digits and AB is a 2-digit number. AB × 6 = BBB. What is A − B?',
         opts=['3', '4', '2', '5'],
         hint='Write the equation as (10A + B) × 6 = 111 × B.',
         sol='60A + 6B = 111B, so 60A = 105B, that is 4A = 7B. With digits: A = 7, B = 4. Check: 74 × 6 = 444. A − B = 3.'),
    dict(ch='10', scen='3-digit numbers with strictly increasing digits from 1 to 5',
         stem='How many 3-digit numbers can be made using only the digits 1 to 5, with the digits strictly increasing from left to right (like 135)?',
         opts=['10', '15', '20', '60'],
         hint='Once you choose three different digits, there is only one way to arrange them in increasing order.',
         sol='Choose 3 of the 5 digits: 123, 124, 125, 134, 135, 145, 234, 235, 245, 345. That is 10.'),
    dict(ch='10', scen='2178 × 4 = 8712 reversal',
         stem='1,089 × 9 = 9,801 reverses the digits of 1,089. Which number multiplies 2,178 to reverse its digits, giving 8,712?',
         opts=['4', '3', '6', '9'],
         hint='Try dividing 8,712 by 2,178.',
         sol='2,178 × 4 = 8,712. So 4 reverses the digits of 2,178.'),

    # ---------------- Part 10 · Mixed Problems
    dict(ch='4+10', scen='four consecutive even numbers adding to 108 · smallest times largest',
         stem='Four consecutive even numbers add up to 108. What is the product of the smallest and the largest?',
         opts=['720', '728', '672', '780'],
         hint='Let the numbers be x, x + 2, x + 4 and x + 6.',
         sol='4x + 12 = 108, so x = 24. The numbers are 24, 26, 28, 30. 24 × 30 = 720.'),
    dict(ch='3+10', scen='price ₹1,000 rising 10% a year for 3 years',
         stem='The price of a cycle is ₹1,000 now and rises by 10% every year. What will it cost after 3 years?',
         opts=['₹1,331', '₹1,300', '₹1,210', '₹1,464'],
         hint='Each year multiply by 1.1, not add ₹100.',
         sol='1,000 → 1,100 → 1,210 → 1,331. After 3 years it costs ₹1,331. (₹1,300 adds ₹100 each year.)'),
    dict(ch='4+9', scen='two numbers in ratio 5 : 7 differing by 18',
         stem='Two numbers are in the ratio 5 : 7 and their difference is 18. What is their sum?',
         opts=['108', '72', '126', '90'],
         hint='The difference is 2 parts.',
         sol='2 parts = 18, so 1 part = 9. The numbers are 45 and 63; their sum is 108.'),
    dict(ch='5+6', scen='log of radius 14 cm length 2 m cut lengthwise in half · surface of one half',
         stem='A cylindrical log of radius 14 cm and length 2 m is cut in half along its length, through the centre. What is the total surface area of one half? (π = 22/7)',
         opts=['15,016 cm²', '9,416 cm²', '14,400 cm²', '17,600 cm²'],
         hint='One half has half the curved surface, two half-circles and a flat rectangle 28 cm × 200 cm.',
         sol='Half curved surface: 22/7 × 14 × 200 = 8,800. Two half-circles: 22/7 × 14 × 14 = 616. Rectangle: 28 × 200 = 5,600. Total 15,016 cm².'),
    dict(ch='1+4', scen='3/(x − 1) = −5/2',
         stem='Solve 3/(x − 1) = −5/2. What is x?',
         opts=['−1/5', '1/5', '−11/5', '7/5'],
         hint='Cross-multiply: 3 × 2 = −5 × (x − 1).',
         sol='6 = −5(x − 1), so x − 1 = −6/5 and x = −1/5.'),
]
