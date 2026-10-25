# AMO Level-2 · Class 7 · Practice Paper 6
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
    dict(ch='1', scen='mean of 2/3 −5/6 and 3/4',
         stem='Ananya finds the mean (average) of 2/3, −5/6 and 3/4. What does she get?',
         opts=['7/36', '7/12', '−7/36', '1/4'],
         hint='Add the three numbers using the denominator 12, then divide by 3.',
         sol='2/3 − 5/6 + 3/4 = 8/12 − 10/12 + 9/12 = 7/12. Mean = 7/12 ÷ 3 = 7/36. (7/12 is the sum.)'),
    dict(ch='1', scen='(x − y) ÷ (x + y) with x = 5/−8 and y = −3/4',
         stem='If x = 5/−8 and y = −3/4, what is (x − y) ÷ (x + y)?',
         opts=['−1/11', '1/11', '−11', '11'],
         hint='Use the denominator 8 for both.',
         sol='x = −5/8, y = −6/8. x − y = 1/8 and x + y = −11/8. (1/8) ÷ (−11/8) = −1/11.'),
    dict(ch='1', scen='fractions p/9 strictly between −4/3 and −2/3',
         stem='How many fractions of the form p/9, where p is an integer, lie strictly between −4/3 and −2/3?',
         opts=['5', '6', '4', '3'],
         hint='Write −4/3 and −2/3 with denominator 9.',
         sol='−4/3 = −12/9 and −2/3 = −6/9. Strictly between them p = −11, −10, −9, −8, −7. That is 5 fractions.'),

    # ---------------- Part 2 · Operations
    dict(ch='2', scen='find n with (5³ × 5⁴) ÷ (5²)³ × 3ⁿ = 45 × 9',
         stem='Find n if [(5³ × 5⁴) ÷ (5²)³] × 3ⁿ = 45 × 9.',
         opts=['4', '3', '5', '2'],
         hint='Simplify the powers of 5 first.',
         sol='(5²)³ = 5² × 5² × 5², so (5³ × 5⁴) ÷ (5²)³ = (5³ ÷ 5²) × (5⁴ ÷ 5⁴) = 5. Then 5 × 3ⁿ = 405, so 3ⁿ = 81 = 3⁴ and n = 4.'),
    dict(ch='2', scen='2⁵ × 5³ × 4² in standard form',
         stem='Write 2⁵ × 5³ × 4² in standard form.',
         opts=['6.4 × 10⁴', '6.4 × 10³', '3.2 × 10⁴', '1.6 × 10⁴'],
         hint='Pair each 5 with a 2 to make 10s.',
         sol='2³ × 5³ = 10³. What is left is 2² × 4² = 4 × 16 = 64. So the number is 64 × 10³ = 64,000 = 6.4 × 10⁴.'),

    # ---------------- Part 3 · Fractions, Decimals & Percentages
    dict(ch='3', scen='10% loss turns to 5% profit with ₹90 more',
         stem='A dealer sells a chair at a 10% loss. If he had sold it for ₹90 more, he would have made a 5% profit. What did the chair cost him?',
         opts=['₹600', '₹900', '₹540', '₹1,800'],
         hint='The ₹90 covers the gap from −10% to +5% of the cost.',
         sol='The difference between 90% and 105% of the cost is 15% of the cost = ₹90. So the cost is 90 ÷ 0.15 = ₹600.'),
    dict(ch='3', scen='discounts of 20% then 10% against one discount of 30% on ₹5,000',
         stem='On a ₹5,000 television, Shop X gives 20% off and then a further 10% off. Shop Y gives a single 30% off. How much more does Shop X charge?',
         opts=['₹100', '₹0', '₹50', '₹200'],
         hint='The second discount at Shop X is 10% of a smaller amount.',
         sol='Shop X: 5,000 → 4,000 → 3,600. Shop Y: 5,000 − 1,500 = 3,500. Shop X charges ₹100 more.'),
    dict(ch='3', scen='20 L of 10% salt water evaporated to 25% salt',
         stem='20 litres of salt water contain 10% salt. How much water must evaporate so that the salt becomes 25% of the solution?',
         opts=['12 L', '8 L', '15 L', '5 L'],
         hint='The amount of salt does not change.',
         sol='Salt: 10% of 20 = 2 L. For 2 L to be 25%, the solution must be 8 L. So 20 − 8 = 12 L of water must evaporate.'),

    # ---------------- Part 4 · Algebra
    dict(ch='4', scen='(x + 3)/4 − (x − 2)/3 = 1',
         stem='Solve (x + 3)/4 − (x − 2)/3 = 1. What is x?',
         opts=['5', '−5', '7', '17'],
         hint='Multiply every term by 12. Take care with the minus sign.',
         sol='3(x + 3) − 4(x − 2) = 12, so 3x + 9 − 4x + 8 = 12, giving −x + 17 = 12 and x = 5.'),
    dict(ch='4', scen='half a number 12 less than three-quarters · number increased by 25%',
         stem='Half of a number is 12 less than three-quarters of the same number. What do you get if the number is increased by 25%?',
         opts=['60', '48', '36', '64'],
         hint='First find the number: x/2 = 3x/4 − 12.',
         sol='3x/4 − x/2 = x/4 = 12, so x = 48. Increased by 25%: 48 + 12 = 60.'),
    dict(ch='4', scen='p² − pq + q² with p = 2q − 3 and q = −4',
         stem='If p = 2q − 3 and q = −4, what is p² − pq + q²?',
         opts=['93', '49', '137', '−93'],
         hint='Find p first.',
         sol='p = 2(−4) − 3 = −11. p² = 121, pq = 44, q² = 16. p² − pq + q² = 121 − 44 + 16 = 93.'),

    # ---------------- Part 5 · Geometry
    dict(ch='5', scen='exterior angle 130° with opposite angles x + 20 and 2x + 5',
         stem='In triangle ABC, the exterior angle at C is 130°. Angle A = (x + 20)° and angle B = (2x + 5)°. What is the smallest angle of the triangle?',
         opts=['50°', '55°', '75°', '35°'],
         hint='The exterior angle at C equals A + B.',
         sol='(x + 20) + (2x + 5) = 130, so 3x = 105 and x = 35. A = 55°, B = 75°, C = 180° − 130° = 50°. The smallest is 50°.'),
    dict(ch='5', scen='alternate angles 3x and 2x + 40 · the angle next to it on the line',
         fig=drawing(260, 150, trans([(180, 54, '3x°'), (58, 98, '(2x + 40)°')])),
         stem='Lines l and m are parallel, and the two marked angles are alternate interior angles. What is the other angle below line l at the same crossing as the angle 3x°?',
         opts=['60°', '120°', '40°', '80°'],
         hint='Alternate angles are equal. Angles on a straight line add up to 180°.',
         sol='3x = 2x + 40, so x = 40 and each marked angle is 120°. The other angle below line l at that crossing is on a straight line with it: 180° − 120° = 60°.'),
    dict(ch='5', scen='rhombus with a 64° angle · angle between a side and the longer diagonal',
         stem='One angle of a rhombus is 64°. What angle does the longer diagonal make with a side of the rhombus?',
         opts=['32°', '58°', '64°', '116°'],
         hint='The diagonals of a rhombus bisect its angles. Which angles does the longer diagonal join?',
         sol='The angles are 64° and 116°. The longer diagonal joins the two 64° corners and bisects them, so it makes 32° with each side. (The shorter diagonal makes 58°.)'),

    # ---------------- Part 6 · Mensuration
    dict(ch='6', scen='cylinder of radius 7 with curved surface 880 cm² · volume',
         stem='A cylinder has radius 7 cm and curved surface area 880 cm². What is its volume? (π = 22/7)',
         opts=['3,080 cm³', '6,160 cm³', '4,400 cm³', '2,200 cm³'],
         hint='Use the curved surface to find the height first.',
         sol='2 × 22/7 × 7 × h = 880, so 44h = 880 and h = 20 cm. Volume = 22/7 × 7 × 7 × 20 = 3,080 cm³.'),
    dict(ch='6', scen='5 cm painted cube cut into 1 cm cubes · exactly two faces painted',
         stem='A cube of edge 5 cm is painted on all its faces and cut into 1 cm cubes. How many of the small cubes have paint on exactly two faces?',
         opts=['36', '27', '24', '54'],
         hint='Cubes with two painted faces lie along the edges, but not at the corners.',
         sol='Each of the 12 edges has 5 cubes, of which 2 are corners (3 faces painted). So each edge has 3 cubes with exactly two painted faces: 12 × 3 = 36. (27 is the number with no paint.)'),
    dict(ch='6', scen='pond 20 by 15 by 2 m emptied at 500 L per minute',
         stem='A rectangular pond is 20 m long, 15 m wide and 2 m deep, and full of water. A pump removes 500 litres every minute. How long does it take to empty the pond?',
         opts=['20 hours', '12 hours', '10 hours', '2 hours'],
         hint='1 m³ = 1,000 litres.',
         sol='Volume: 20 × 15 × 2 = 600 m³ = 6,00,000 L. Time: 6,00,000 ÷ 500 = 1,200 minutes = 20 hours.'),

    # ---------------- Part 7 · Data Handling
    dict(ch='8', scen='bar graph of daily sales · Thursday over Wednesday percent',
         fig=drawing(330, 200, bars([('Mon', 40), ('Tue', 60), ('Wed', 30), ('Thu', 70), ('Fri', 50)], 80, 10, 'Kites sold')),
         stem='The bar graph shows the number of kites a shop sold each day. By what percent were Thursday\'s sales more than Wednesday\'s?',
         opts=['133 1/3%', '40%', '57 1/7%', '233 1/3%'],
         hint='Percent increase = increase ÷ smaller value × 100.',
         sol='Thursday 70, Wednesday 30. Increase 40. 40/30 × 100 = 133 1/3%. (57 1/7% divides by 70.)'),
    dict(ch='8', scen='median of 7 numbers is 15 · add 20 and 5',
         stem='The median of seven numbers is 15. Two more numbers, 20 and 5, are added to the list. What is the median of the nine numbers?',
         opts=['15', '12.5', '20', '17.5'],
         hint='One new number is above 15 and one is below.',
         sol='Before, 3 numbers were at or below the middle and 3 above. Adding one number below 15 and one above keeps 15 in the middle: it is now the 5th of 9. The median stays 15.'),

    # ---------------- Part 8 · Applied Mathematics
    dict(ch='9', scen='x : 12 :: 15 : 20 and 12 : y :: 9 : 15',
         stem='If x : 12 = 15 : 20 and 12 : y = 9 : 15, what is x + y?',
         opts=['29', '35', '27', '24'],
         hint='In a proportion, the product of the extremes equals the product of the means.',
         sol='x × 20 = 12 × 15, so x = 9. 12 × 15 = 9 × y, so y = 20. x + y = 29.'),
    dict(ch='9', scen='25 workers for 36 days · 5 leave after 12 days',
         stem='25 workers can finish a job in 36 days. After 12 days, 5 workers leave. How many days does the whole job take?',
         opts=['42', '45', '30', '48'],
         hint='The job is 25 × 36 = 900 worker-days.',
         sol='First 12 days: 300 worker-days. Left: 600 worker-days for 20 workers = 30 days. Total 12 + 30 = 42 days.'),
    dict(ch='9', scen='walker at 4 km/h and cyclist at 12 km/h starting 1 hour later',
         stem='Harsh starts walking at 4 km/h. One hour later, Divya starts cycling from the same place along the same road at 12 km/h. How far from the start does she catch up with him?',
         opts=['6 km', '4 km', '8 km', '12 km'],
         hint='Harsh is 4 km ahead when Divya starts. She gains 8 km every hour.',
         sol='Gap 4 km, closing at 12 − 4 = 8 km/h, so she catches him after 1/2 hour. She has cycled 12 × 1/2 = 6 km.'),

    # ---------------- Part 9 · Mathematical Reasoning
    dict(ch='10', scen='ABC − CBA = 297 with B = 5 and digit sum 14',
         stem='ABC and CBA are 3-digit numbers. ABC − CBA = 297, the middle digit B is 5, and A + B + C = 14. What is ABC?',
         opts=['653', '356', '563', '635'],
         hint='ABC − CBA = 99 × (A − C).',
         sol='99(A − C) = 297, so A − C = 3. A + C = 14 − 5 = 9. So A = 6 and C = 3: ABC = 653. Check: 653 − 356 = 297.'),
    dict(ch='10', scen='rectangles in a grid of 3 by 2 squares',
         stem='A rectangle is divided into a grid of 3 squares across and 2 squares down. How many rectangles of all sizes (squares included) are in the grid?',
         opts=['18', '12', '15', '24'],
         hint='A rectangle is fixed by choosing 2 of the 4 vertical lines and 2 of the 3 horizontal lines.',
         sol='Pairs of vertical lines: 6. Pairs of horizontal lines: 3. Rectangles: 6 × 3 = 18.'),
    dict(ch='10', scen='remainder 2 on division by 3 4 5 6 and divisible by 7',
         stem='What is the smallest number that leaves remainder 2 when divided by 3, 4, 5 or 6, and is exactly divisible by 7?',
         opts=['182', '62', '122', '242'],
         hint='Such numbers are 2 more than a multiple of 60.',
         sol='Numbers leaving remainder 2: 62, 122, 182, 242, … Test for 7: 62 no, 122 no, 182 = 7 × 26 yes. The answer is 182.'),

    # ---------------- Part 10 · Mixed Problems
    dict(ch='4+10', scen='2 by 2 square of calendar dates adding to 80',
         stem='On a calendar page, Mohit picks a 2 × 2 square of four dates. They add up to 80. What is the largest of the four dates?',
         opts=['24', '23', '20', '17'],
         hint='If the top-left date is x, the others are x + 1, x + 7 and x + 8.',
         sol='x + (x + 1) + (x + 7) + (x + 8) = 4x + 16 = 80, so x = 16. The dates are 16, 17, 23 and 24; the largest is 24.'),
    dict(ch='3+10', scen='overall 84% across two tests out of 50 and 75',
         stem='Neha scored 40 out of 50 in the first test. The second test is out of 75. She wants 84% of the total marks of the two tests. What must she score in the second test?',
         opts=['65', '63', '67', '60'],
         hint='Find the total marks she needs out of 125.',
         sol='Total maximum: 50 + 75 = 125. 84% of 125 = 105. She has 40, so she needs 105 − 40 = 65 out of 75.'),
    dict(ch='4+9', scen='ages in ratio 4 : 5 now and 3 : 4 six years ago',
         stem='The present ages of Tara and her cousin Om are in the ratio 4 : 5. Six years ago the ratio was 3 : 4. What is the sum of their present ages?',
         opts=['54 years', '45 years', '63 years', '48 years'],
         hint='Let the ages be 4x and 5x.',
         sol='(4x − 6)/(5x − 6) = 3/4, so 16x − 24 = 15x − 18 and x = 6. Ages 24 and 30; the sum is 54 years.'),
    dict(ch='5+6', scen='rectangle 24 by 10 · triangle joining a corner to two midpoints',
         stem='ABCD is a rectangle with AB = 24 m and BC = 10 m. M is the midpoint of BC and N is the midpoint of CD. What is the area of triangle AMN?',
         opts=['90 m²', '120 m²', '60 m²', '80 m²'],
         hint='Take away the three right-angled triangles at the corners from the rectangle.',
         sol='Rectangle: 240 m². Triangle ABM: 1/2 × 24 × 5 = 60. Triangle ADN: 1/2 × 10 × 12 = 60. Triangle MCN: 1/2 × 5 × 12 = 30. AMN = 240 − 150 = 90 m².'),
    dict(ch='1+4', scen='(2/3)x − (1/4)(x − 5) = 5/2',
         stem='Solve (2/3)x − (1/4)(x − 5) = 5/2. What is x?',
         opts=['3', '−3', '9/5', '5'],
         hint='Multiply every term by 12.',
         sol='8x − 3(x − 5) = 30, so 8x − 3x + 15 = 30, giving 5x = 15 and x = 3.'),
]
