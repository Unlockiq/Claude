# AMO Level-2 · Class 7 · Practice Paper 5
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
    dict(ch='1', scen='point one third of the way from −7/4 to 5/2',
         stem='On a number line, A is at −7/4 and B is at 5/2. Point C lies between them so that AC is one third of AB. Where is C?',
         opts=['−1/3', '1/3', '−5/12', '1/12'],
         hint='First find the length AB = 5/2 − (−7/4).',
         sol='AB = 5/2 + 7/4 = 17/4. One third of it is 17/12. C = −7/4 + 17/12 = −21/12 + 17/12 = −4/12 = −1/3.'),
    dict(ch='1', scen='which of four fractions is not equal to −3/5',
         stem='Which of these is NOT equal to −3/5?',
         opts=['−15/−25', '6/−10', '−9/15', '3/−5'],
         hint='Count the minus signs in each fraction.',
         sol='6/−10, −9/15 and 3/−5 all have one minus sign and reduce to −3/5. −15/−25 has two minus signs, so it equals +3/5.'),
    dict(ch='1', scen='product (1 − 1/2)(1 − 1/3)…(1 − 1/20)',
         stem='What is the value of (1 − 1/2) × (1 − 1/3) × (1 − 1/4) × … × (1 − 1/20)?',
         opts=['1/20', '19/20', '1/2', '1/19'],
         hint='Write each bracket as a single fraction: 1/2, 2/3, 3/4, …',
         sol='The product is 1/2 × 2/3 × 3/4 × … × 19/20. Every numerator cancels the denominator before it, leaving 1/20.'),

    # ---------------- Part 2 · Operations
    dict(ch='2', scen='2ᵃ = 32 and 3ᵇ = 81 · aᵇ − bᵃ',
         stem='If 2ᵃ = 32 and 3ᵇ = 81, what is aᵇ − bᵃ?',
         opts=['−399', '399', '1', '−1'],
         hint='Find a and b first.',
         sol='2⁵ = 32, so a = 5. 3⁴ = 81, so b = 4. aᵇ − bᵃ = 5⁴ − 4⁵ = 625 − 1,024 = −399.'),
    dict(ch='2', scen='3.6 × 10⁴ + 4.5 × 10³ in standard form',
         stem='Write 3.6 × 10⁴ + 4.5 × 10³ in standard form.',
         opts=['4.05 × 10⁴', '8.1 × 10⁴', '8.1 × 10³', '4.05 × 10³'],
         hint='Change both numbers to ordinary form, or to the same power of 10, before adding.',
         sol='3.6 × 10⁴ = 36,000 and 4.5 × 10³ = 4,500. Sum = 40,500 = 4.05 × 10⁴. (8.1 × 10⁴ adds 3.6 and 4.5 without matching the powers.)'),

    # ---------------- Part 3 · Fractions, Decimals & Percentages
    dict(ch='3', scen='15% of A equals 20% of B and A − B = 200',
         stem='15% of a number A is equal to 20% of a number B, and A is 200 more than B. What is A + B?',
         opts=['1,400', '1,050', '1,200', '1,600'],
         hint='15% of A = 20% of B means 3A = 4B.',
         sol='From 15A = 20B, A = 4B/3, so A − B = B/3 = 200 and B = 600. A = 800. A + B = 1,400.'),
    dict(ch='3', scen='50 kg rice at ₹40 · 30 kg at ₹48 and the rest at ₹38',
         stem='A grocer buys 50 kg of rice at ₹40 per kg. He sells 30 kg at ₹48 per kg and the rest at ₹38 per kg. What is his profit percent?',
         opts=['10%', '12%', '8%', '9%'],
         hint='Find the total cost and the total selling price.',
         sol='Cost: 50 × 40 = ₹2,000. Selling: 30 × 48 + 20 × 38 = 1,440 + 760 = ₹2,200. Profit ₹200 on ₹2,000 = 10%.'),
    dict(ch='3', scen='marked 50% above cost · 20% discount · sold at ₹960',
         stem='A shop marks goods 50% above cost price and then gives a 20% discount. A lamp is sold for ₹960. What was its marked price?',
         opts=['₹1,200', '₹1,440', '₹1,152', '₹1,000'],
         hint='The selling price is 80% of the marked price.',
         sol='₹960 is 80% of the marked price, so the marked price is 960 ÷ 0.8 = ₹1,200. (The cost price is ₹800.)'),

    # ---------------- Part 4 · Algebra
    dict(ch='4', scen='three-quarters exceeds two-thirds by 5 · find 40%',
         stem='Three-quarters of a number is 5 more than two-thirds of the same number. What is 40% of the number?',
         opts=['24', '16', '20', '30'],
         hint='First find the number: 3x/4 − 2x/3 = 5.',
         sol='3x/4 − 2x/3 = 9x/12 − 8x/12 = x/12 = 5, so x = 60. 40% of 60 = 24.'),
    dict(ch='4', scen='a plus b 7 and ab 10 · value of 3a²b + 3ab² − 2ab',
         stem='If a + b = 7 and ab = 10, what is the value of 3a²b + 3ab² − 2ab?',
         opts=['190', '210', '170', '230'],
         hint='Take out the common factor from the first two terms.',
         sol='3a²b + 3ab² = 3ab(a + b) = 3 × 10 × 7 = 210. Then 210 − 2ab = 210 − 20 = 190.'),
    dict(ch='4', scen='collect like terms in 7x²y − 3xy² + 5yx² − xy + 2y²x',
         stem='Which is the simplified form of 7x²y − 3xy² + 5yx² − xy + 2y²x?',
         opts=['12x²y − xy² − xy', '12x²y − 5xy² − xy', '10x²y + xy', '7x²y − xy² − xy'],
         hint='5yx² is a like term of 7x²y, and 2y²x is a like term of −3xy².',
         sol='7x²y + 5x²y = 12x²y. −3xy² + 2xy² = −xy². −xy has no like term. Answer: 12x²y − xy² − xy.'),

    # ---------------- Part 5 · Geometry
    dict(ch='5', scen='exterior angle 110° with opposite angles differing by 30° · type of triangle',
         stem='An exterior angle of a triangle is 110°. The two interior angles opposite to it differ by 30°. What kind of triangle is it?',
         opts=['Acute-angled and isosceles', 'Obtuse-angled and scalene', 'Right-angled and isosceles', 'Acute-angled and scalene'],
         hint='Find all three angles.',
         sol='The opposite angles add to 110° and differ by 30°: they are 70° and 40°. The third angle is 180° − 110° = 70°. Angles 70°, 70°, 40°: all acute, two equal, so acute-angled and isosceles.'),
    dict(ch='5', scen='bisectors of A and B in a quadrilateral with C = 100 and D = 60',
         stem='In quadrilateral ABCD, angle C = 100° and angle D = 60°. The bisectors of angles A and B meet at P. What is angle APB?',
         opts=['80°', '100°', '160°', '60°'],
         hint='A + B = 360° − C − D. In triangle APB, the two base angles are A/2 and B/2.',
         sol='A + B = 360° − 160° = 200°, so A/2 + B/2 = 100°. Angle APB = 180° − 100° = 80°.'),
    dict(ch='5', scen='side and two angles with one non-included · congruence',
         stem='In triangles ABC and DEF, AB = DE, angle A = angle D and angle C = angle F. Which statement is correct?',
         opts=['They are congruent: angle B = angle E, then use ASA', 'There is not enough information', 'They are congruent by SAS', 'They are congruent by SSS'],
         hint='Two equal pairs of angles make the third pair equal.',
         sol='A + C = D + F, so angle B = angle E by the angle sum. Now AB = DE lies between angles A and B, and between D and E, so the triangles are congruent by ASA.'),

    # ---------------- Part 6 · Mensuration
    dict(ch='6', scen='cylinder with curved surface 440 cm² and height 10 cm · volume',
         stem='The curved surface area of a closed cylinder is 440 cm² and its height is 10 cm. What is its volume? (π = 22/7)',
         opts=['1,540 cm³', '3,080 cm³', '770 cm³', '2,200 cm³'],
         hint='Use the curved surface area to find the radius first.',
         sol='2 × 22/7 × r × 10 = 440, so r = 440 × 7 ÷ 440 = 7 cm. Volume = 22/7 × 7 × 7 × 10 = 1,540 cm³. (3,080 uses the diameter 14 in place of one radius.)'),
    dict(ch='6', scen='cubes of edge 2.5 cm filling a 10 by 7.5 by 5 box stacked into a tower',
         stem='Cubes of edge 2.5 cm exactly fill a box 10 cm × 7.5 cm × 5 cm. All the cubes are then stacked one on top of another. How tall is the tower?',
         opts=['60 cm', '24 cm', '40 cm', '75 cm'],
         hint='Count how many cubes fit along each edge of the box.',
         sol='Along the edges: 10 ÷ 2.5 = 4, 7.5 ÷ 2.5 = 3 and 5 ÷ 2.5 = 2, so 4 × 3 × 2 = 24 cubes. Tower: 24 × 2.5 = 60 cm. (24 is the number of cubes.)'),
    dict(ch='6', scen='open box 20 by 15 by 10 cm · total area of the five faces',
         stem='A box without a lid is 20 cm long, 15 cm wide and 10 cm high. What is the total area of its five faces?',
         opts=['1,000 cm²', '1,300 cm²', '700 cm²', '3,000 cm²'],
         hint='Base + four walls; there is no top.',
         sol='Base: 20 × 15 = 300 cm². Walls: 2(20 × 10) + 2(15 × 10) = 700 cm². Total 1,000 cm². (1,300 includes a lid; 3,000 is the volume.)'),

    # ---------------- Part 7 · Data Handling
    dict(ch='8', scen='pie chart of favourite fruit of 600 people with apple angle missing',
         fig=drawing(230, 230, pie([('Mango 150°', 150), ('Apple', 90), ('Banana 72°', 72), ('Grapes 48°', 48)])),
         stem='The pie chart shows the favourite fruit of 600 people. The angle for apple is not marked. How many people chose apple?',
         opts=['150', '90', '250', '120'],
         hint='The angles of a pie chart add up to 360°.',
         sol='Apple: 360° − 150° − 72° − 48° = 90°. People: 90/360 × 600 = 150.'),
    dict(ch='8', scen='mean of 6 numbers 20 · mean of first 4 is 18 · last two differ by 4',
         stem='The mean of six numbers is 20. The mean of the first four is 18. The last two numbers differ by 4. What is the larger of the last two?',
         opts=['26', '24', '22', '28'],
         hint='Find the total of the last two numbers.',
         sol='Total of six: 120. Total of first four: 72. The last two add to 48 and differ by 4, so they are 26 and 22. The larger is 26.'),

    # ---------------- Part 8 · Applied Mathematics
    dict(ch='9', scen='A : B = 3 : 4 B : C = 6 : 7 with C − A = ₹500',
         stem='Money is shared among Aditi, Bharat and Charvi so that Aditi : Bharat = 3 : 4 and Bharat : Charvi = 6 : 7. Charvi gets ₹500 more than Aditi. How much does Bharat get?',
         opts=['₹1,200', '₹900', '₹1,400', '₹1,000'],
         hint='Combine the ratios so that Bharat\'s number is the same.',
         sol='Aditi : Bharat : Charvi = 9 : 12 : 14. Charvi − Aditi = 5 parts = ₹500, so 1 part = ₹100. Bharat gets 12 × 100 = ₹1,200.'),
    dict(ch='9', scen='three gears with 40 24 and 30 teeth · turns of the last gear',
         stem='Gear A has 40 teeth and turns 60 times a minute. It drives gear B, which has 24 teeth. Gear B drives gear C, which has 30 teeth. How many turns does gear C make in 5 minutes?',
         opts=['400', '500', '300', '80'],
         hint='Teeth × turns is the same for gears that mesh: fewer teeth means more turns.',
         sol='Teeth passing each minute: 40 × 60 = 2,400. Gear C turns 2,400 ÷ 30 = 80 times a minute (gear B in between does not change this). In 5 minutes: 400.'),
    dict(ch='9', scen='going at 40 km/h and returning at 60 km/h · average speed',
         stem='Varun drives from home to his aunt\'s house at 40 km/h and comes back by the same road at 60 km/h. What is his average speed for the whole trip?',
         opts=['48 km/h', '50 km/h', '45 km/h', '52 km/h'],
         hint='Average speed = total distance ÷ total time. Try a distance of 120 km.',
         sol='Take 120 km each way. Going: 3 h. Returning: 2 h. Average = 240 ÷ 5 = 48 km/h. (50 is the average of the two speeds, which is wrong.)'),

    # ---------------- Part 9 · Mathematical Reasoning
    dict(ch='10', scen='A3 + 4B = 82',
         stem='In the sum A3 + 4B = 82, A and B are digits (A3 and 4B are 2-digit numbers). What is A × B?',
         opts=['27', '24', '36', '18'],
         hint='Look at the units column: 3 + B must end in 2.',
         sol='3 + B ends in 2, so B = 9 with a carry of 1. Tens: A + 4 + 1 = 8, so A = 3. Check: 33 + 49 = 82. A × B = 27.'),
    dict(ch='10', scen='triangles with whole-number sides and perimeter 12',
         stem='How many different triangles have whole-number side lengths (in cm) and a perimeter of 12 cm?',
         opts=['3', '4', '2', '5'],
         hint='The longest side must be less than half the perimeter.',
         sol='The longest side must be less than 6, so it is 4 or 5. With 5: (2, 5, 5) and (3, 4, 5). With 4: (4, 4, 4). That is 3 triangles.'),
    dict(ch='10', scen='sum of odd numbers 1 + 3 + … + 49',
         stem='What is 1 + 3 + 5 + … + 49, the sum of all odd numbers from 1 to 49?',
         opts=['625', '600', '650', '576'],
         hint='1 = 1, 1 + 3 = 4, 1 + 3 + 5 = 9. How many odd numbers are there?',
         sol='There are 25 odd numbers from 1 to 49. The sum of the first n odd numbers is n × n, so the sum is 25 × 25 = 625.'),

    # ---------------- Part 10 · Mixed Problems
    dict(ch='4+10', scen='odd x where 3x minus 7 is more than 20 and less than 30',
         stem='x is an odd whole number. When 7 is taken away from 3 times x, the answer is more than 20 but less than 30. What is x?',
         opts=['11', '9', '13', '10'],
         hint='Try whole numbers for x and check 3x − 7.',
         sol='x = 9 gives 20, not more than 20. x = 10 gives 23, x = 11 gives 26, x = 12 gives 29, and x = 13 gives 32, too big. So x is 10, 11 or 12, and the odd one is 11.'),
    dict(ch='3+10', scen='whole numbers to 200 whose 12% and 15% are both whole',
         stem='For how many whole numbers n from 1 to 200 are both 12% of n and 15% of n whole numbers?',
         opts=['2', '4', '10', '18'],
         hint='12% = 3/25 and 15% = 3/20. What must n be a multiple of?',
         sol='12% of n = 3n/25 is whole only when n is a multiple of 25. 15% of n = 3n/20 is whole only when n is a multiple of 20. So n must be a multiple of 100: 100 and 200. That is 2 numbers. (18 adds the 8 multiples of 25 and the 10 multiples of 20.)'),
    dict(ch='4+9', scen='bus 15 km/h faster than cyclist · 150 km and 60 km in equal time',
         stem='A bus travels 15 km/h faster than a cyclist. In the same time, the bus covers 150 km and the cyclist covers 60 km. What is the cyclist\'s speed?',
         opts=['10 km/h', '25 km/h', '15 km/h', '12 km/h'],
         hint='Let the cyclist\'s speed be x. Equal times: 150/(x + 15) = 60/x.',
         sol='150x = 60(x + 15), so 90x = 900 and x = 10 km/h. The bus goes at 25 km/h; both take 6 hours.'),
    dict(ch='5+6', scen='curved surface unrolled into a rectangle of perimeter 100 cm and height 6 cm',
         stem='The curved surface of a cylinder of height 6 cm is cut and opened out into a rectangle with perimeter 100 cm. What is the volume of the cylinder? (π = 22/7)',
         opts=['924 cm³', '1,848 cm³', '264 cm³', '462 cm³'],
         hint='The rectangle\'s length is the circumference of the base.',
         sol='2(length + 6) = 100, so the length (circumference) is 44 cm and r = 7 cm. Volume = 22/7 × 7 × 7 × 6 = 924 cm³.'),
    dict(ch='1+4', scen='a³b − ab³ at a = −1/2 b = 2/3',
         stem='What is the value of a³b − ab³ when a = −1/2 and b = 2/3?',
         opts=['7/108', '−7/108', '25/108', '−25/108'],
         hint='Work out a³b and ab³ separately.',
         sol='a³b = (−1/8) × (2/3) = −1/12. ab³ = (−1/2) × (8/27) = −4/27. a³b − ab³ = −1/12 + 4/27 = −9/108 + 16/108 = 7/108.'),
]
