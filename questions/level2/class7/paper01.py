# AMO Level-2 · Class 7 · Practice Paper 1
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
    dict(ch='1', scen='rational number halfway between −2/3 and 5/6',
         stem='Meera marks −2/3 and 5/6 on a number line. Which rational number lies exactly halfway between them?',
         opts=['1/12', '1/6', '1/4', '−1/12'],
         hint='Halfway between two numbers is half of their sum.',
         sol='Sum: −2/3 + 5/6 = −4/6 + 5/6 = 1/6. Half of 1/6 is 1/12. (1/6 is the sum, not the midpoint.)'),
    dict(ch='1', scen='second smallest of −3/4 5/−8 −7/12 −2/3',
         stem='Arjun arranges −3/4, 5/−8, −7/12 and −2/3 from smallest to largest. Which number is second in his list?',
         opts=['−2/3', '5/−8', '−7/12', '−3/4'],
         hint='Write all four with the denominator 24.',
         sol='−3/4 = −18/24, 5/−8 = −15/24, −7/12 = −14/24, −2/3 = −16/24. From smallest: −18, −16, −15, −14 (over 24). The second is −16/24 = −2/3.'),
    dict(ch='1', scen='(−5/6) ÷ (10/−9) × (−4/3)',
         stem='What is the value of (−5/6) ÷ (10/−9) × (−4/3)?',
         opts=['−1', '1', '−25/36', '4/9'],
         hint='Dividing by 10/−9 is the same as multiplying by −9/10. Count the minus signs.',
         sol='(−5/6) × (−9/10) = 45/60 = 3/4. Then 3/4 × (−4/3) = −1. There are three negative factors, so the answer is negative.'),

    # ---------------- Part 2 · Operations
    dict(ch='2', scen='3 to the n times 9 squared equals 3 times 9 to the 4',
         stem='Kavya finds a whole number n such that 3ⁿ × 9² = 3 × 9⁴. What is n?',
         opts=['5', '4', '3', '7'],
         hint='Write 9² and 9⁴ as powers of 3.',
         sol='9² = 3⁴ and 9⁴ = 3⁸, so 3 × 9⁴ = 3⁹. Then 3ⁿ⁺⁴ = 3⁹, so n + 4 = 9 and n = 5.'),
    dict(ch='2', scen='spacecraft to the Moon at 1.6 × 10⁴ km per hour · round trip',
         stem='The Moon is about 3.84 × 10⁵ km from the Earth. A spacecraft travels at about 1.6 × 10⁴ km per hour. About how long does a round trip take, not counting any stop?',
         opts=['48 hours', '24 hours', '2.4 hours', '480 hours'],
         hint='Time = distance ÷ speed. Divide the numbers and the powers of 10 separately, then double.',
         sol='One way: (3.84 ÷ 1.6) × 10⁵ ÷ 10⁴ = 2.4 × 10 = 24 hours. There and back: 2 × 24 = 48 hours. (24 hours is only one way.)'),

    # ---------------- Part 3 · Fractions, Decimals & Percentages
    dict(ch='3', scen='marked 40% above cost then 25% discount',
         stem='A shopkeeper marks a lamp 40% above its cost price. He then gives a discount of 25% on the marked price. What is his profit or loss percent?',
         opts=['5% profit', '15% profit', '5% loss', '10% profit'],
         hint='Take the cost price as ₹100.',
         sol='Cost ₹100. Marked price ₹140. A 25% discount is ₹35, so he sells for ₹105. Profit ₹5 on ₹100 = 5%. (15% wrongly subtracts 25 from 40.)'),
    dict(ch='3', scen='two fans sold at ₹1,200 each · 20% gain and 20% loss',
         stem='Rohan sells two fans for ₹1,200 each. On one he gains 20% and on the other he loses 20%. What is his overall result?',
         opts=['Loss of ₹100', 'No profit or loss', 'Profit of ₹100', 'Loss of ₹48'],
         hint='Find the cost price of each fan separately.',
         sol='Fan 1: 1.2 × cost = 1,200, so cost = ₹1,000. Fan 2: 0.8 × cost = 1,200, so cost = ₹1,500. Total cost ₹2,500, total selling price ₹2,400: a loss of ₹100.'),
    dict(ch='3', scen='sugar price rises 25% · cut in consumption to keep spending same',
         stem='The price of sugar rises by 25%. By what percent must a family reduce its sugar use so that its spending on sugar stays the same?',
         opts=['20%', '25%', '15%', '80%'],
         hint='If ₹100 bought 100 units before, how many units does ₹100 buy now?',
         sol='Old price ₹1 per unit, new price ₹1.25. ₹100 now buys 100 ÷ 1.25 = 80 units instead of 100. The use must fall by 20 out of 100 = 20%.'),

    # ---------------- Part 4 · Algebra
    dict(ch='4', scen='(2x + 3)/5 − (x − 1)/3 = 2',
         stem='Solve (2x + 3)/5 − (x − 1)/3 = 2. What is x?',
         opts=['16', '14', '6', '26'],
         hint='Multiply every term by 15 first. Take care with the minus sign before the second fraction.',
         sol='15 × each term: 3(2x + 3) − 5(x − 1) = 30. So 6x + 9 − 5x + 5 = 30, giving x + 14 = 30 and x = 16. (14 forgets that −5 × −1 = +5.)'),
    dict(ch='4', scen='three consecutive odd numbers adding to 147 · product of smallest and largest',
         stem='The sum of three consecutive odd numbers is 147. What is the product of the smallest and the largest of them?',
         opts=['2,397', '2,499', '2,451', '2,303'],
         hint='Write the numbers as x, x + 2 and x + 4.',
         sol='x + (x + 2) + (x + 4) = 3x + 6 = 147, so 3x = 141 and x = 47. The numbers are 47, 49 and 51. 47 × 51 = 2,397.'),
    dict(ch='4', scen='subtract 3a² − 2ab + b² from the sum of two expressions',
         stem='Yash adds a² + ab and 2a² − 3ab + 4b². From this sum he subtracts 3a² − 2ab + b². What does she get?',
         opts=['3b²', '6a² − 4ab + 5b²', '−3b²', '4ab + 3b²'],
         hint='Add like terms first; when subtracting, change every sign of the expression taken away.',
         sol='Sum: 3a² − 2ab + 4b². Subtract: (3a² − 2ab + 4b²) − (3a² − 2ab + b²) = 0a² + 0ab + 3b² = 3b².'),

    # ---------------- Part 5 · Geometry
    dict(ch='5', scen='co-interior angles 3x + 20 and 2x + 30',
         fig=drawing(260, 150, trans([(100, 54, '(2x + 30)°'), (58, 98, '(3x + 20)°')])),
         stem='Lines l and m are parallel. The two marked angles lie between the lines on the same side of the transversal. What is the larger of the two angles?',
         opts=['98°', '82°', '26°', '110°'],
         hint='Interior angles on the same side of a transversal (co-interior angles) add up to 180°.',
         sol='(3x + 20) + (2x + 30) = 180, so 5x + 50 = 180 and x = 26. The angles are 98° and 82°; the larger is 98°.'),
    dict(ch='5', scen='exterior angle 120° with opposite interior angles in ratio 3 : 5',
         stem='An exterior angle of a triangle is 120°. The two interior angles opposite to it are in the ratio 3 : 5. What is the smallest angle of the triangle?',
         opts=['45°', '60°', '75°', '40°'],
         hint='The exterior angle equals the sum of the two opposite interior angles.',
         sol='The two opposite angles add to 120°: 3/8 × 120 = 45° and 5/8 × 120 = 75°. The third angle is 180° − 120° = 60°. The smallest is 45°.'),
    dict(ch='5', scen='quadrilateral with A = C, B = A + 30, D = 2A',
         stem='In quadrilateral ABCD, angle A equals angle C, angle B is 30° more than angle A, and angle D is twice angle A. What is angle D?',
         opts=['132°', '66°', '96°', '120°'],
         hint='The angles of a quadrilateral add up to 360°.',
         sol='A + (A + 30) + A + 2A = 5A + 30 = 360, so A = 66°. Then D = 2 × 66° = 132°.'),

    # ---------------- Part 6 · Mensuration
    dict(ch='6', scen='cuboid tank emptied into cylindrical drums of radius 35 cm',
         stem='A full tank is a cuboid 2 m × 1.5 m × 1 m. Its water is poured into drums shaped like cylinders, each of radius 35 cm and height 1 m. How many drums can be filled completely? (π = 22/7)',
         opts=['7', '8', '6', '9'],
         hint='Work in cm³: 1 m³ = 10,00,000 cm³.',
         sol='Tank: 3 m³ = 30,00,000 cm³. Drum: 22/7 × 35 × 35 × 100 = 3,85,000 cm³. 30,00,000 ÷ 3,85,000 ≈ 7.8, so 7 drums fill completely.'),
    dict(ch='6', scen='cuboid 12 by 8 by 6 cut into 2 cm cubes · increase in surface area',
         stem='A wooden cuboid 12 cm × 8 cm × 6 cm is cut into cubes of edge 2 cm. By how much is the total surface area of all the cubes more than that of the cuboid?',
         opts=['1,296 cm²', '1,728 cm²', '432 cm²', '864 cm²'],
         hint='Count the cubes: how many fit along each edge?',
         sol='Cubes: 6 × 4 × 3 = 72, each with surface area 6 × 4 = 24 cm²: total 1,728 cm². Cuboid: 2(96 + 72 + 48) = 432 cm². Increase: 1,728 − 432 = 1,296 cm².'),
    dict(ch='6', scen='six closed tins of radius 7 cm and height 10 cm from a 1 m by 50 cm sheet',
         stem='Kiran makes 6 closed tins, each a cylinder of radius 7 cm and height 10 cm, from a metal sheet 1 m long and 50 cm wide. How much sheet is left over? (π = 22/7)',
         opts=['512 cm²', '2,360 cm²', '1,436 cm²', '3,152 cm²'],
         hint='One tin needs its curved surface and two circles. 1 m = 100 cm.',
         sol='Curved surface: 2 × 22/7 × 7 × 10 = 440 cm². Each circle: 22/7 × 7 × 7 = 154 cm². One tin: 440 + 308 = 748 cm². Six tins: 4,488 cm². Sheet: 100 × 50 = 5,000 cm². Left: 512 cm². (2,360 forgets the circles.)'),

    # ---------------- Part 7 · Data Handling
    dict(ch='8', scen='pie chart of a ₹36,000 monthly budget · food minus savings',
         fig=drawing(230, 230, pie([('Food 120°', 120), ('Rent 90°', 90), ('Education 60°', 60), ('Savings 54°', 54), ('Other 36°', 36)])),
         stem='The pie chart shows how a family spends its monthly income of ₹36,000. How much more is spent on food than is saved?',
         opts=['₹6,600', '₹5,400', '₹12,000', '₹66'],
         hint='Each degree stands for 36,000 ÷ 360 rupees.',
         sol='1° stands for ₹100. Food minus savings = 120° − 54° = 66°, which is 66 × ₹100 = ₹6,600.'),
    dict(ch='8', scen='mean of 5 numbers 18 · one removed mean 16 · replaced by 31',
         stem='The mean of five numbers is 18. When one number is removed, the mean of the other four is 16. The removed number is then replaced by 31. What is the new mean of the five numbers?',
         opts=['19', '18', '20', '17'],
         hint='Work with totals, not means.',
         sol='Total of five: 5 × 18 = 90. Total of four: 4 × 16 = 64, so the removed number was 26. New total: 64 + 31 = 95. New mean: 95 ÷ 5 = 19.'),

    # ---------------- Part 8 · Applied Mathematics
    dict(ch='9', scen='12 workers dig 60 m in 5 days · workers for 96 m in 4 days',
         stem='12 workers dig a trench 60 m long in 5 days. Working at the same rate, how many workers are needed to dig a trench 96 m long in 4 days?',
         opts=['24', '19', '15', '30'],
         hint='More length needs more workers; fewer days also needs more workers.',
         sol='Workers = 12 × (96/60) × (5/4) = 12 × 1.6 × 1.25 = 24.'),
    dict(ch='9', scen='A : B = 2 : 3 and B : C = 4 : 5 · C\'s share of ₹7,000',
         stem='₹7,000 is shared among Asha, Raj and Om so that Asha : Raj = 2 : 3 and Raj : Om = 4 : 5. How much does Om get?',
         opts=['₹3,000', '₹2,800', '₹2,400', '₹1,600'],
         hint='Make Raj\'s share the same number in both ratios.',
         sol='Asha : Raj = 8 : 12 and Raj : Om = 12 : 15, so the ratio is 8 : 12 : 15 (35 parts). Om gets 15/35 × 7,000 = ₹3,000.'),
    dict(ch='9', scen='car slower for 2 hours · speed needed to finish in 3 hours',
         stem='A journey takes 4 hours at 60 km/h. Asha drives the first 2 hours at 60 km/h. At what speed must she drive the rest of the way to finish the whole journey in 3 hours?',
         opts=['120 km/h', '80 km/h', '90 km/h', '100 km/h'],
         hint='First find the length of the journey and how much is left.',
         sol='Journey: 60 × 4 = 240 km. In 2 hours she covers 120 km, leaving 120 km. She has 3 − 2 = 1 hour left, so she needs 120 km/h. (80 km/h is the speed for the whole trip in 3 hours.)'),

    # ---------------- Part 9 · Mathematical Reasoning
    dict(ch='10', scen='AB + BA = 121 with A − B = 3',
         stem='In the sum AB + BA = 121, A and B are digits and AB is a 2-digit number. A is 3 more than B. What is the number AB?',
         opts=['74', '47', '83', '65'],
         hint='AB + BA = (10A + B) + (10B + A) = 11(A + B).',
         sol='11(A + B) = 121, so A + B = 11. With A − B = 3: A = 7, B = 4. AB = 74. Check: 74 + 47 = 121.'),
    dict(ch='10', scen='3-digit numbers with digit sum 5',
         stem='How many 3-digit numbers have digits that add up to 5?',
         opts=['15', '21', '10', '14'],
         hint='Fix the hundreds digit (1 to 5) and count how the other two digits can share the rest.',
         sol='Hundreds digit 1: the other two add to 4 in 5 ways (04, 13, 22, 31, 40). Digit 2: 4 ways. 3: 3 ways. 4: 2 ways. 5: 1 way. Total 5 + 4 + 3 + 2 + 1 = 15.'),
    dict(ch='10', scen='units digit of 7⁴ × 3⁵ × 2³',
         stem='What is the units digit of 7⁴ × 3⁵ × 2³?',
         opts=['4', '2', '6', '8'],
         hint='Only the units digits matter. Find the units digit of each power first.',
         sol='7⁴ = 2,401 ends in 1. 3⁵ = 243 ends in 3. 2³ = 8. Units digit of 1 × 3 × 8 = 24 is 4.'),

    # ---------------- Part 10 · Mixed Problems
    dict(ch='4+10', scen='stick pattern using 3n + 2 sticks · figure with 101 sticks',
         stem='Kunal makes a pattern of figures with sticks. The 1st figure uses 5 sticks, the 2nd uses 8 and the 3rd uses 11, and so on. Which figure uses exactly 101 sticks?',
         opts=['33rd', '34th', '32nd', '35th'],
         hint='Write the number of sticks in the nth figure as an expression.',
         sol='Each figure adds 3 sticks, so the nth figure uses 3n + 2 sticks. 3n + 2 = 101 gives 3n = 99 and n = 33.'),
    dict(ch='3+10', scen='price up 10% then down 10% · done twice',
         stem='The price of a bicycle is raised by 10% and then lowered by 10%. The same two changes are then made once more. What is the overall change in price?',
         opts=['A decrease of 1.99%', 'No change', 'A decrease of 2%', 'A decrease of 1%'],
         hint='Each pair of changes multiplies the price by 1.1 × 0.9.',
         sol='One pair: 1.1 × 0.9 = 0.99. Two pairs: 0.99 × 0.99 = 0.9801. The price falls by 1 − 0.9801 = 0.0199, that is 1.99%.'),
    dict(ch='4+9', scen='ages in ratio 5 : 7 now and 7 : 9 after 8 years',
         stem='The ages of Priya and her brother Dev are in the ratio 5 : 7. After 8 years the ratio will be 7 : 9. What is the sum of their present ages?',
         opts=['48 years', '40 years', '56 years', '36 years'],
         hint='Let the ages be 5x and 7x.',
         sol='(5x + 8)/(7x + 8) = 7/9, so 45x + 72 = 49x + 56, giving 4x = 16 and x = 4. Ages 20 and 28; sum 48 years.'),
    dict(ch='5+6', scen='largest cylinder inside a 14 cm cube · space left',
         stem='A cylinder just fits inside a cube of edge 14 cm: it touches all six faces of the cube. What volume inside the cube is not taken up by the cylinder? (π = 22/7)',
         opts=['588 cm³', '2,156 cm³', '196 cm³', '616 cm³'],
         hint='The cylinder has diameter 14 cm and height 14 cm.',
         sol='Cube: 14 × 14 × 14 = 2,744 cm³. Cylinder: 22/7 × 7 × 7 × 14 = 2,156 cm³. Space left: 2,744 − 2,156 = 588 cm³.'),
    dict(ch='1+4', scen='value of (3x + 1)/(x − 1) at x = −2/3',
         stem='What is the value of (3x + 1)/(x − 1) when x = −2/3?',
         opts=['3/5', '−3/5', '5/3', '1/5'],
         hint='Work out the top and the bottom separately.',
         sol='Top: 3 × (−2/3) + 1 = −2 + 1 = −1. Bottom: −2/3 − 1 = −5/3. (−1) ÷ (−5/3) = 3/5.'),
]
