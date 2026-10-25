# AMO Level-2 · Class 7 · Practice Paper 3
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
    dict(ch='1', scen='which is greater −5/7 or −7/9 and by how much',
         stem='Which is greater, −5/7 or −7/9, and by how much?',
         opts=['−5/7, by 4/63', '−7/9, by 4/63', '−5/7, by 2/63', 'They are equal'],
         hint='Write both with denominator 63.',
         sol='−5/7 = −45/63 and −7/9 = −49/63. −45 is greater than −49, so −5/7 is greater, by 4/63.'),
    dict(ch='1', scen='additive inverse of the reciprocal of −3/8 plus 1',
         stem='Nikhil takes the reciprocal of −3/8, then the additive inverse of that, and finally adds 1. What does he get?',
         opts=['11/3', '−5/3', '5/3', '−11/3'],
         hint='The reciprocal keeps the sign; the additive inverse changes it.',
         sol='Reciprocal of −3/8 is −8/3. Its additive inverse is 8/3. 8/3 + 1 = 11/3.'),
    dict(ch='1', scen='24 m rope · 3/8 cut then 2/5 of the rest',
         stem='Ramesh cuts 3/8 of a 24 m rope. Then he cuts 2/5 of the rope that is left. How much rope remains?',
         opts=['9 m', '6 m', '5.4 m', '15 m'],
         hint='The second cut is 2/5 of what is left, not of 24 m.',
         sol='After the first cut: 5/8 × 24 = 15 m. The second cut takes 2/5 × 15 = 6 m, leaving 9 m.'),

    # ---------------- Part 2 · Operations
    dict(ch='2', scen='(9² × 8 × 5³) ÷ (6³ × 3 × 10²) by cancelling powers',
         stem='Without multiplying out, find the value of (9² × 8 × 5³) ÷ (6³ × 3 × 10²).',
         opts=['5/4', '4/5', '5/2', '1'],
         hint='Write every number as a product of powers of 2, 3 and 5.',
         sol='Top: 3⁴ × 2³ × 5³. Bottom: 6³ × 3 × 10² = 2³ × 3³ × 3 × 2² × 5² = 2⁵ × 3⁴ × 5². Cancel 3⁴, 2³ and 5²: what is left is 5 ÷ 2² = 5/4.'),
    dict(ch='2', scen='town of 4 × 10³ families using 1.5 × 10² L each · tanks of 2 × 10⁵ L',
         stem='A town has 4 × 10³ families. Each family uses 1.5 × 10² litres of water a day. A tank holds 2 × 10⁵ litres. How many full tanks does the town use in a day?',
         opts=['3', '30', '0.3', '6'],
         hint='Find the total water used in standard form first.',
         sol='Water used: 4 × 1.5 = 6 and 10³ × 10² = 10⁵, so 6 × 10⁵ litres. Tanks: (6 × 10⁵) ÷ (2 × 10⁵) = 3.'),

    # ---------------- Part 3 · Fractions, Decimals & Percentages
    dict(ch='3', scen='cost of 12 pens equals selling price of 10 pens',
         stem='The cost price of 12 pens equals the selling price of 10 pens. What is the profit percent?',
         opts=['20%', '16 2/3%', '2%', '25%'],
         hint='Let each pen cost ₹1.',
         sol='If each pen costs ₹1, then 10 pens sell for ₹12, so each sells for ₹1.20. Profit 20 paise on ₹1 = 20%. (16 2/3% divides by 12 instead of 10.)'),
    dict(ch='3', scen='buy 4 get 1 free and then 5% off the bill',
         stem='A shop offers "Buy 4, get 1 free" on notebooks, and then a further 5% off the bill. What single discount on 5 notebooks does this equal?',
         opts=['24%', '25%', '20%', '15%'],
         hint='Let each notebook cost ₹100. What do you pay for 5?',
         sol='5 notebooks are worth ₹500. You pay for 4: ₹400, then 5% off: ₹380. Saving ₹120 on ₹500 = 24%.'),
    dict(ch='3', scen='population 50,000 up 10% then down 10%',
         stem='A town of 50,000 people grows by 10% in one year and then falls by 10% the next year. What is the population after two years?',
         opts=['49,500', '50,000', '49,000', '50,500'],
         hint='The 10% fall is of the larger number.',
         sol='After year 1: 55,000. After year 2: 55,000 − 5,500 = 49,500.'),

    # ---------------- Part 4 · Algebra
    dict(ch='4', scen='father three times son now and twice in 12 years',
         stem='A father is three times as old as his son. In 12 years he will be twice as old as his son. How old is the father now?',
         opts=['36 years', '12 years', '24 years', '48 years'],
         hint='Let the son be x years old.',
         sol='3x + 12 = 2(x + 12), so 3x + 12 = 2x + 24 and x = 12. The father is 36.'),
    dict(ch='4', scen='5(2x − 3y) − 3(3x − 4y) + 2(x + y) at x = 4 y = −5',
         stem='Simplify 5(2x − 3y) − 3(3x − 4y) + 2(x + y) and find its value when x = 4 and y = −5.',
         opts=['17', '7', '−17', '22'],
         hint='Simplify first: collect the x terms and the y terms.',
         sol='10x − 15y − 9x + 12y + 2x + 2y = 3x − y. At x = 4, y = −5: 12 + 5 = 17.'),
    dict(ch='4', scen='fraction with denominator 8 more · add 17 and 1 gives 3/2',
         stem='The denominator of a fraction is 8 more than its numerator. If 17 is added to the numerator and 1 to the denominator, the fraction becomes 3/2. What is the fraction?',
         opts=['7/15', '5/13', '9/17', '3/11'],
         hint='Let the fraction be x/(x + 8).',
         sol='(x + 17)/(x + 9) = 3/2, so 2x + 34 = 3x + 27 and x = 7. The fraction is 7/15. Check: 24/16 = 3/2.'),

    # ---------------- Part 5 · Geometry
    dict(ch='5', scen='parallelogram angle 24° less than twice its neighbour',
         stem='In a parallelogram, one angle is 24° less than twice the angle next to it. What is the smaller angle of the parallelogram?',
         opts=['68°', '112°', '56°', '78°'],
         hint='Adjacent angles of a parallelogram add up to 180°.',
         sol='x + (2x − 24) = 180, so 3x = 204 and x = 68°. The other angle is 112°. The smaller is 68°.'),
    dict(ch='5', scen='bent path between parallel lines · angles 40° and 35°',
         fig=drawing(250, 165, zig('40°', '35°', '?')),
         stem='AB ∥ CD. Angle ABE = 40° and angle CDE = 35°, as marked. What is angle BED?',
         opts=['75°', '105°', '5°', '140°'],
         hint='Draw a line through E parallel to AB and use alternate angles.',
         sol='A line through E parallel to AB splits angle BED into two parts: 40° (alternate to angle ABE) and 35° (alternate to angle CDE). So angle BED = 40° + 35° = 75°.'),
    dict(ch='5', scen='triangle x 2x 3x · bisector of the largest angle',
         stem='The angles of triangle ABC are A = x, B = 2x and C = 3x. The bisector of angle C meets AB at D. What is angle ADC?',
         opts=['105°', '75°', '135°', '45°'],
         hint='Find x first, then look at triangle ADC.',
         sol='x + 2x + 3x = 180°, so x = 30°: A = 30°, B = 60°, C = 90°. The bisector makes angle ACD = 45°. In triangle ADC: angle ADC = 180° − 30° − 45° = 105°.'),

    # ---------------- Part 6 · Mensuration
    dict(ch='6', scen='cylinder jar r 7 h 12 poured into cuboid tank 22 by 14',
         stem='A cylindrical jar of radius 7 cm and height 12 cm is full of water. The water is poured into an empty tank with a rectangular base 22 cm × 14 cm. How high does the water rise? (π = 22/7)',
         opts=['6 cm', '12 cm', '8.4 cm', '4 cm'],
         hint='The volume of water stays the same.',
         sol='Volume = 22/7 × 7 × 7 × 12 = 1,848 cm³. Height in the tank = 1,848 ÷ (22 × 14) = 1,848 ÷ 308 = 6 cm.'),
    dict(ch='6', scen='4 cm painted cube cut into 1 cm cubes · exactly one face painted',
         stem='A cube of edge 4 cm is painted on all faces and then cut into 1 cm cubes. How many small cubes have exactly one painted face?',
         opts=['24', '8', '32', '16'],
         hint='Look at one face: which of its 16 small squares are not on an edge?',
         sol='On each face, the inner 2 × 2 = 4 cubes have only that face painted. 6 faces × 4 = 24. (The 8 corner cubes have three painted faces.)'),
    dict(ch='6', scen='painting walls and ceiling of a 6 by 5 by 3 m room except door and window',
         stem='A room is 6 m long, 5 m wide and 3 m high. Its four walls and ceiling are painted at ₹20 per m², leaving out a door 2 m × 1 m and a window 1.5 m × 1 m. What is the cost?',
         opts=['₹1,850', '₹1,920', '₹1,320', '₹2,520'],
         hint='Walls: 2 × (length + width) × height.',
         sol='Walls: 2 × 11 × 3 = 66 m². Ceiling: 30 m². Less door and window: 2 + 1.5 = 3.5 m². Area: 92.5 m². Cost: 92.5 × 20 = ₹1,850.'),

    # ---------------- Part 7 · Data Handling
    dict(ch='8', scen='pie chart of favourite sports · boys who like badminton',
         fig=drawing(230, 230, pie([('Cricket 150°', 150), ('Football 90°', 90), ('Hockey 60°', 60), ('Badminton 60°', 60)])),
         stem='The pie chart shows the favourite sports of 720 students. 1/3 of the cricket fans are girls, and all the other girls chose badminton. There are 200 girls in all. How many badminton fans are boys?',
         opts=['20', '40', '100', '120'],
         hint='Each degree stands for 720 ÷ 360 students.',
         sol='Each degree is 2 students. Cricket: 150° = 300 students, so 100 girls. The other 100 girls all chose badminton. Badminton: 60° = 120 students, so 120 − 100 = 20 are boys.'),
    dict(ch='8', scen='mean of 10 numbers 25 with 34 misread as 43',
         stem='The mean of 10 numbers was found to be 25. Later it was found that 34 had been read as 43. What is the correct mean?',
         opts=['24.1', '25.9', '24.9', '24'],
         hint='Find the wrong total first.',
         sol='Wrong total: 250. Correct total: 250 − 43 + 34 = 241. Correct mean: 24.1.'),

    # ---------------- Part 8 · Applied Mathematics
    dict(ch='9', scen='₹5,200 shared in ratio 1/2 : 1/3 : 1/4',
         stem='₹5,200 is shared among Anil, Bhavna and Chetan in the ratio 1/2 : 1/3 : 1/4. How much does Bhavna get?',
         opts=['₹1,600', '₹1,733', '₹2,400', '₹1,200'],
         hint='Multiply the ratio by 12 to clear the fractions.',
         sol='1/2 : 1/3 : 1/4 = 6 : 4 : 3 (13 parts). One part = 5,200 ÷ 13 = ₹400. Bhavna gets 4 × 400 = ₹1,600.'),
    dict(ch='9', scen='food for 200 soldiers for 30 days · 40 join after 6 days',
         stem='A camp has food for 200 soldiers for 30 days. After 6 days, 40 more soldiers join. How many more days will the food last?',
         opts=['20', '24', '16', '25'],
         hint='Food left after 6 days feeds 200 soldiers for 24 days.',
         sol='Food left: 200 × 24 = 4,800 soldier-days. Now 240 soldiers: 4,800 ÷ 240 = 20 days.'),
    dict(ch='9', scen='360 m train passes a pole in 18 s · crossing a 240 m platform',
         stem='A train 360 m long passes a pole in 18 seconds. How long does it take to cross a platform 240 m long?',
         opts=['30 s', '12 s', '18 s', '48 s'],
         hint='To cross the platform the train must cover its own length plus the platform.',
         sol='Speed = 360 ÷ 18 = 20 m/s. Distance = 360 + 240 = 600 m. Time = 600 ÷ 20 = 30 s.'),

    # ---------------- Part 9 · Mathematical Reasoning
    dict(ch='10', scen='AB times AB equals CAB',
         stem='In AB × AB = CAB, the letters stand for different digits, AB is a 2-digit number and CAB is a 3-digit number. What digit is C?',
         opts=['6', '5', '2', '1'],
         hint='The square of AB must end in the digits of AB itself.',
         sol='AB × AB ends in AB. A square ending in its own last two digits is 25 or 76 (or 00, 01). 76 × 76 = 5,776 has 4 digits, so AB = 25 and 25 × 25 = 625. So C = 6.'),
    dict(ch='10', scen='2-digit numbers whose digits multiply to 12',
         stem='How many 2-digit numbers have digits whose product is 12?',
         opts=['4', '6', '2', '5'],
         hint='Write 12 as a product of two single digits.',
         sol='12 = 2 × 6 = 3 × 4. The numbers are 26, 62, 34 and 43. (1 × 12 is not allowed because 12 is not a digit.) That is 4.'),
    dict(ch='10', scen='remainder of 3⁵ + 4⁵ divided by 7',
         stem='What is the remainder when 3⁵ + 4⁵ is divided by 7?',
         opts=['0', '1', '2', '4'],
         hint='Work out the powers, or notice that 3 + 4 = 7.',
         sol='3⁵ + 4⁵ = 243 + 1,024 = 1,267 = 7 × 181, so the remainder is 0. (For odd powers, aⁿ + bⁿ is always divisible by a + b.)'),

    # ---------------- Part 10 · Mixed Problems
    dict(ch='4+10', scen='n from 1 to 50 with 3n + 2 a multiple of 7',
         stem='For how many whole numbers n from 1 to 50 is 3n + 2 a multiple of 7?',
         opts=['7', '8', '6', '5'],
         hint='Find the first n that works, then see how often it repeats.',
         sol='n = 4 gives 14, the first multiple of 7. Adding 7 to n adds 21 to 3n + 2, which keeps it a multiple of 7. So n = 4, 11, 18, 25, 32, 39, 46: 7 numbers.'),
    dict(ch='3+10', scen='item worth ₹10,000 losing 10% each year · first below ₹7,000',
         stem='A machine worth ₹10,000 loses 10% of its value every year. At the end of which year is its value first below ₹7,000?',
         opts=['4th year', '3rd year', '5th year', '7th year'],
         hint='Each year the value is multiplied by 0.9.',
         sol='Year 1: 9,000. Year 2: 8,100. Year 3: 7,290. Year 4: 6,561, which is the first value below ₹7,000.'),
    dict(ch='4+9', scen='milk and water 7 : 3 in 60 L · water to add for 3 : 2',
         stem='A 60 L mixture has milk and water in the ratio 7 : 3. How much water must be added to make the ratio 3 : 2?',
         opts=['10 L', '8 L', '12 L', '6 L'],
         hint='The milk does not change. Find it first.',
         sol='Milk: 7/10 × 60 = 42 L. Water: 18 L. For 3 : 2, the water must be 42 × 2/3 = 28 L. Add 28 − 18 = 10 L.'),
    dict(ch='5+6', scen='sheet 66 cm by 10 cm rolled into a cylinder · volume',
         stem='A rectangular sheet 66 cm by 10 cm is rolled along its 66 cm side, so the edges just meet, to make a hollow cylinder 10 cm tall. What volume does the cylinder hold? (π = 22/7)',
         opts=['3,465 cm³', '13,860 cm³', '6,930 cm³', '660 cm³'],
         hint='The 66 cm side becomes the circumference of the base.',
         sol='2 × 22/7 × r = 66, so r = 10.5 cm. Volume = 22/7 × 10.5 × 10.5 × 10 = 3,465 cm³. (660 is just 66 × 10.)'),
    dict(ch='1+4', scen='(x + y)/(x − y) at x = −3/4 and y = 2/3',
         stem='What is the value of (x + y) ÷ (x − y) when x = −3/4 and y = 2/3?',
         opts=['1/17', '−1/17', '17', '−17'],
         hint='Use the denominator 12.',
         sol='x + y = −9/12 + 8/12 = −1/12. x − y = −9/12 − 8/12 = −17/12. (−1/12) ÷ (−17/12) = 1/17.'),
]
