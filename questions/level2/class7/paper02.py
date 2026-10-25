# AMO Level-2 · Class 7 · Practice Paper 2
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
    dict(ch='1', scen='what must be added to −3/8 + 5/12 − 1/6 to make 1',
         stem='Kabir works out −3/8 + 5/12 − 1/6. What must he add to his answer to get 1?',
         opts=['9/8', '7/8', '−9/8', '1/8'],
         hint='Use the common denominator 24.',
         sol='−3/8 + 5/12 − 1/6 = −9/24 + 10/24 − 4/24 = −3/24 = −1/8. To reach 1 he must add 1 + 1/8 = 9/8. (7/8 forgets that the sum is negative.)'),
    dict(ch='1', scen='fractions p/15 strictly between −2/5 and 1/3',
         stem='How many fractions of the form p/15, where p is an integer, lie strictly between −2/5 and 1/3?',
         opts=['10', '11', '9', '12'],
         hint='Write −2/5 and 1/3 with denominator 15.',
         sol='−2/5 = −6/15 and 1/3 = 5/15. Strictly between them p can be −5, −4, …, 3, 4. That is 10 values (remember to count 0).'),
    dict(ch='1', scen='product of two rationals −14/15 with one equal to 7/−10',
         stem='The product of two rational numbers is −14/15. One of them is 7/−10. What is the other?',
         opts=['4/3', '−4/3', '49/75', '3/4'],
         hint='Divide the product by the known number.',
         sol='(−14/15) ÷ (−7/10) = (−14/15) × (−10/7) = 140/105 = 4/3. A negative divided by a negative is positive.'),

    # ---------------- Part 2 · Operations
    dict(ch='2', scen='(3⁴ × 5³ × 2⁵) ÷ (15³ × 6²)',
         stem='What is the value of (3⁴ × 5³ × 2⁵) ÷ (15³ × 6²)?',
         opts=['8/3', '3/8', '24', '8/9'],
         hint='Break 15³ and 6² into powers of 2, 3 and 5.',
         sol='15³ × 6² = 3³ × 5³ × 2² × 3² = 2² × 3⁵ × 5³. The quotient is 2⁵⁻² × 3⁴⁻⁵ × 5⁰ = 2³ ÷ 3 = 8/3.'),
    dict(ch='2', scen='largest of 3⁵ 4⁴ 5³ and 6³',
         stem='Which is the largest of 3⁵, 4⁴, 5³ and 6³?',
         opts=['4⁴', '3⁵', '6³', '5³'],
         hint='Work out each power; a bigger exponent does not always win.',
         sol='3⁵ = 243, 4⁴ = 256, 5³ = 125, 6³ = 216. The largest is 4⁴ = 256.'),

    # ---------------- Part 3 · Fractions, Decimals & Percentages
    dict(ch='3', scen='₹2,400 with successive discounts of 10% and 5%',
         stem='A jacket is marked ₹2,400. Tanvi gets a discount of 10% and then a further 5% on the reduced price. How much does she pay?',
         opts=['₹2,052', '₹2,040', '₹2,160', '₹2,280'],
         hint='Take the second discount on the new price, not on ₹2,400.',
         sol='After 10%: 2,400 − 240 = ₹2,160. After 5% of 2,160 (₹108): ₹2,052. (₹2,040 wrongly takes 15% of ₹2,400.)'),
    dict(ch='3', scen='watch sold at ₹1,140 with 5% loss · price for 10% gain',
         stem='By selling a watch for ₹1,140, Raj loses 5%. For how much should he sell it to gain 10%?',
         opts=['₹1,320', '₹1,254', '₹1,296', '₹1,200'],
         hint='First find the cost price: ₹1,140 is 95% of it.',
         sol='Cost = 1,140 ÷ 0.95 = ₹1,200. For a 10% gain he must sell at 1,200 × 1.1 = ₹1,320. (₹1,254 adds 10% to ₹1,140.)'),
    dict(ch='3', scen='72% pass maths 64% pass science 8% fail both',
         stem='In a test, 72% of the students passed in Maths and 64% passed in Science. 8% failed in both. What percent passed in both?',
         opts=['44%', '36%', '28%', '56%'],
         hint='92% passed in at least one subject.',
         sol='Passed in at least one: 100 − 8 = 92%. Maths + Science = 72 + 64 = 136%, which counts the "both" group twice. Both = 136 − 92 = 44%.'),

    # ---------------- Part 4 · Algebra
    dict(ch='4', scen='a number 12 more than 5/8 of itself',
         stem='A number is 12 more than five-eighths of itself. What is the number?',
         opts=['32', '20', '96', '24'],
         hint='x = 5x/8 + 12.',
         sol='x − 5x/8 = 12, so 3x/8 = 12 and x = 32. Check: 5/8 of 32 is 20, and 20 + 12 = 32.'),
    dict(ch='4', scen='rectangle perimeter 68 with length 4 more than twice the width',
         stem='The perimeter of a rectangle is 68 cm. Its length is 4 cm more than twice its width. What is its area?',
         opts=['240 cm²', '224 cm²', '300 cm²', '204 cm²'],
         hint='Let the width be w. Then the length is 2w + 4.',
         sol='2(w + 2w + 4) = 68, so 3w + 4 = 34 and w = 10. Length 24 cm. Area 24 × 10 = 240 cm².'),
    dict(ch='4', scen='2a²b − 3ab² + ab at a = −2 b = 3',
         stem='What is the value of 2a²b − 3ab² + ab when a = −2 and b = 3?',
         opts=['72', '−36', '60', '−72'],
         hint='Work out each term separately and watch the signs.',
         sol='2a²b = 2 × 4 × 3 = 24. −3ab² = −3 × (−2) × 9 = 54. ab = −6. Total: 24 + 54 − 6 = 72.'),

    # ---------------- Part 5 · Geometry
    dict(ch='5', scen='angle between bisectors of B and C when A is 50°',
         stem='In triangle ABC, angle A = 50°. The bisectors of angles B and C meet at O. What is angle BOC?',
         opts=['115°', '130°', '65°', '105°'],
         hint='Angles B and C add up to 130°. What do their halves add up to?',
         sol='B + C = 180° − 50° = 130°, so B/2 + C/2 = 65°. In triangle BOC, angle BOC = 180° − 65° = 115°.'),
    dict(ch='5', scen='co-interior angles 4x + 10 and 2x + 20 · their difference',
         fig=drawing(260, 150, trans([(100, 54, '(2x + 20)°'), (58, 98, '(4x + 10)°')])),
         stem='Lines l and m are parallel. The two marked angles lie between the lines on the same side of the transversal. What is the difference between the two angles?',
         opts=['40°', '20°', '70°', '110°'],
         hint='Co-interior angles add up to 180°.',
         sol='(4x + 10) + (2x + 20) = 180, so 6x = 150 and x = 25. The angles are 110° and 70°; their difference is 40°.'),
    dict(ch='5', scen='two sides and a non-included angle equal · congruence',
         stem='In triangles PQR and XYZ, PQ = XY = 5 cm, QR = YZ = 7 cm and angle P = angle X = 40°. What can you conclude?',
         opts=['The triangles need not be congruent', 'They are congruent by SAS', 'They are congruent by SSS', 'They are congruent by ASA'],
         hint='Is the equal angle between the two equal sides?',
         sol='The 40° angle is at P, which is not between PQ and QR. Two sides with a non-included angle is not a congruence rule, so the triangles need not be congruent. SAS needs the angle between the two sides.'),

    # ---------------- Part 6 · Mensuration
    dict(ch='6', scen='painting a pillar of diameter 70 cm height 4 m at ₹15 per m²',
         stem='A cylindrical pillar has diameter 70 cm and height 4 m. Its curved surface is painted at ₹15 per m². What is the cost? (π = 22/7)',
         opts=['₹132', '₹264', '₹66', '₹115.50'],
         hint='Change the radius to metres first: 35 cm = 0.35 m.',
         sol='Curved surface = 2 × 22/7 × 0.35 × 4 = 8.8 m². Cost = 8.8 × 15 = ₹132. (₹264 uses the diameter as the radius.)'),
    dict(ch='6', scen='cuboid volume 1,440 with length 15 breadth 12 · total surface area',
         stem='A cuboid has volume 1,440 cm³, length 15 cm and breadth 12 cm. What is its total surface area?',
         opts=['792 cm²', '396 cm²', '1,440 cm²', '684 cm²'],
         hint='First find the height.',
         sol='Height = 1,440 ÷ (15 × 12) = 8 cm. Surface area = 2(15 × 12 + 12 × 8 + 15 × 8) = 2(180 + 96 + 120) = 792 cm².'),
    dict(ch='6', scen='bricks 25 by 12.5 by 7.5 cm for a wall 10 m by 30 cm by 2 m',
         stem='How many bricks of size 25 cm × 12.5 cm × 7.5 cm are needed for a wall 10 m long, 30 cm thick and 2 m high? Ignore the mortar.',
         opts=['2,560', '2,400', '2,650', '25,600'],
         hint='Work in cm³ for both the wall and one brick.',
         sol='Wall: 1,000 × 30 × 200 = 60,00,000 cm³. Brick: 25 × 12.5 × 7.5 = 2,343.75 cm³. Bricks: 60,00,000 ÷ 2,343.75 = 2,560.'),

    # ---------------- Part 7 · Data Handling
    dict(ch='8', scen='bar graph of books read by five students · mean minus median',
         fig=drawing(330, 200, bars([('Asha', 12), ('Ravi', 8), ('Mohit', 18), ('Tara', 9), ('Kiran', 3)], 20, 2, 'Books read in a term')),
         stem='The bar graph shows the number of books five students read in a term. By how much does the mean number of books exceed the median?',
         opts=['1', '0', '2', '9'],
         hint='Order the five values to find the median.',
         sol='Values 12, 8, 18, 9, 3. Mean = 50 ÷ 5 = 10. In order: 3, 8, 9, 12, 18, so the median is 9. 10 − 9 = 1.'),
    dict(ch='8', scen='3 5 5 7 8 8 8 x with mode 8 and median 7',
         stem='The data 3, 5, 5, 7, 8, 8, 8, x has mode 8 and median 7. What is x?',
         opts=['7', '6', '8', '5'],
         hint='With 8 values, the median is the mean of the 4th and 5th values.',
         sol='If x = 7: 3, 5, 5, 7, 7, 8, 8, 8, median (7 + 7)/2 = 7 and mode 8. If x = 6 the median is 6.5; if x = 8 or more it is 7.5; if x = 5 the mode is not only 8. So x = 7.'),

    # ---------------- Part 8 · Applied Mathematics
    dict(ch='9', scen='15 pumps empty a tank in 8 h · 5 break after 2 h',
         stem='15 identical pumps can empty a tank in 8 hours. After 2 hours, 5 of the pumps break down. How long does it take to empty the tank in all?',
         opts=['11 hours', '12 hours', '9 hours', '10 hours'],
         hint='Count pump-hours: the whole job is 15 × 8 = 120 pump-hours.',
         sol='First 2 hours: 15 × 2 = 30 pump-hours. Left: 90 pump-hours, done by 10 pumps in 9 hours. Total 2 + 9 = 11 hours.'),
    dict(ch='9', scen='map scale 1 : 25,000 with 8.4 cm on the map',
         stem='A map has scale 1 : 25,000. Two villages are 8.4 cm apart on the map. How far apart are they on the ground?',
         opts=['2.1 km', '21 km', '0.21 km', '2.5 km'],
         hint='1 cm on the map is 25,000 cm on the ground. 1 km = 1,00,000 cm.',
         sol='8.4 × 25,000 = 2,10,000 cm = 2,100 m = 2.1 km.'),
    dict(ch='9', scen='15 m of cloth costs ₹1,260 · cost of 22.5 m',
         stem='15 m of cloth costs ₹1,260. At the same rate, how much do 22.5 m cost?',
         opts=['₹1,890', '₹1,800', '₹1,960', '₹1,860'],
         hint='Find the cost of 1 m, or notice that 22.5 is 1.5 times 15.',
         sol='22.5 m is 1.5 times 15 m, so the cost is 1.5 × 1,260 = ₹1,890. (1 m costs ₹84.)'),

    # ---------------- Part 9 · Mathematical Reasoning
    dict(ch='10', scen='ABC + ABC + ABC = BBB',
         stem='In the sum ABC + ABC + ABC = BBB, each letter stands for a different digit and ABC is a 3-digit number. What is A + B + C?',
         opts=['13', '12', '14', '15'],
         hint='3 × ABC = BBB = B × 111 = B × 3 × 37, so ABC = 37 × B.',
         sol='ABC = 37B and its middle digit must be B. B = 4 gives 148, whose middle digit is 4. (37 × 3 = 111, 37 × 5 = 185, 37 × 6 = 222, … all fail.) 148 + 148 + 148 = 444. A + B + C = 1 + 4 + 8 = 13.'),
    dict(ch='10', scen='ways to pay ₹50 with ₹2 and ₹5 coins using both kinds',
         stem='Gauri pays exactly ₹50 using only ₹2 and ₹5 coins, with at least one coin of each kind. In how many different ways can she do it?',
         opts=['4', '5', '6', '3'],
         hint='The number of ₹5 coins must be even. Why?',
         sol='The ₹5 coins must make an even amount, so their number is even: 2, 4, 6 or 8 (10 would leave no ₹2 coins). These give 20, 15, 10 and 5 coins of ₹2. That is 4 ways.'),
    dict(ch='10', scen='pattern 1 × 9 + 2 = 11 continued to 12345 × 9 + 6',
         stem='1 × 9 + 2 = 11, 12 × 9 + 3 = 111, 123 × 9 + 4 = 1,111. Following the pattern, what is 12,345 × 9 + 6?',
         opts=['1,11,111', '11,111', '1,11,110', '11,11,111'],
         hint='Count how many 1s each answer has.',
         sol='A number made of n digits 1, 2, …, n gives an answer of n + 1 ones. 12,345 has 5 digits, so the answer has six 1s: 1,11,111.'),

    # ---------------- Part 10 · Mixed Problems
    dict(ch='4+10', scen='five consecutive multiples of 7 adding to 455',
         stem='The sum of five consecutive multiples of 7 is 455. What is the largest of them?',
         opts=['105', '98', '112', '91'],
         hint='The middle multiple is the average of the five.',
         sol='The middle multiple is 455 ÷ 5 = 91. The five are 77, 84, 91, 98, 105. The largest is 105.'),
    dict(ch='3+10', scen='increase 20% then decrease 20% then increase 20%',
         stem='Sana increases a number by 20%, then decreases the result by 20%, then increases that result by 20%. What is the overall change?',
         opts=['An increase of 15.2%', 'An increase of 20%', 'A decrease of 4%', 'No change'],
         hint='Multiply by 1.2, then 0.8, then 1.2.',
         sol='1.2 × 0.8 × 1.2 = 1.152, so the number goes up by 15.2%. (A rise and fall of 20% are not equal changes.)'),
    dict(ch='4+9', scen='36 notes of ₹10 and ₹50 worth ₹1,000',
         stem='Lalit has 36 notes, all ₹10 or ₹50, worth ₹1,000 in all. How many ₹10 notes does he have?',
         opts=['20', '16', '24', '18'],
         hint='Let the number of ₹50 notes be x. Then there are 36 − x notes of ₹10.',
         sol='50x + 10(36 − x) = 1,000, so 40x + 360 = 1,000 and x = 16. He has 16 notes of ₹50 and 20 notes of ₹10.'),
    dict(ch='5+6', scen='open can of radius 7 cm height 20 cm · tin needed',
         stem='An open can (with no lid) is a cylinder of radius 7 cm and height 20 cm. How much tin is needed to make it? (π = 22/7)',
         opts=['1,034 cm²', '1,188 cm²', '880 cm²', '3,080 cm²'],
         hint='Only one circle is needed: the base.',
         sol='Curved surface: 2 × 22/7 × 7 × 20 = 880 cm². Base: 22/7 × 7 × 7 = 154 cm². Total 880 + 154 = 1,034 cm². (1,188 includes a lid.)'),
    dict(ch='1+4', scen='(2x − 1)/3 − (x + 2)/4 = −1/2',
         stem='Solve (2x − 1)/3 − (x + 2)/4 = −1/2. What is x?',
         opts=['4/5', '−4/5', '8/5', '2/5'],
         hint='Multiply every term by 12.',
         sol='4(2x − 1) − 3(x + 2) = −6, so 8x − 4 − 3x − 6 = −6, giving 5x = 4 and x = 4/5.'),
]
