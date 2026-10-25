# AMO Level-2 · Class 5 · Practice Paper 3  (format: see paper01.py)


def bars(data, top, step, unit='', bw=34, gap=22, h=150):
    """Simple bar graph: data = [(label, value)], y axis from 0 to top with gridlines every step."""
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


def stair_squares():
    prims, x = [], 10
    for s in (1, 2, 3, 4):
        prims.append(('rect', x, 10 + (4 - s) * 25, s * 25, s * 25, 'yellow'))
        prims.append(('text', x + s * 12.5, 10 + 100 + 12, f'{s} cm', 10))
        x += s * 25
    return prims


QUESTIONS = [
    # ---------------- Part 1 · Number System
    dict(ch='1', scen='2-digit primes whose digits add up to 10',
         stem='How many 2-digit prime numbers have digits that add up to 10?',
         opts=['3', '4', '2', '5'],
         hint='List the 2-digit numbers with digit sum 10 and test each one.',
         sol='Digit sum 10: 19, 28, 37, 46, 55, 64, 73, 82, 91. Even numbers and 55 are not prime, and 91 = 7 × 13. The primes are 19, 37 and 73: 3.'),
    dict(ch='1', scen='ribbons 84 cm and 60 cm cut into equal longest pieces',
         stem='Uma has two ribbons, 84 cm and 60 cm long. She cuts both into pieces of the same length, as long as possible, with nothing left over. How many pieces does she get in all?',
         opts=['12', '24', '7', '5'],
         hint='The longest piece that fits both is the HCF.',
         sol='HCF of 84 and 60 is 12, so each piece is 12 cm. 84 ÷ 12 = 7 and 60 ÷ 12 = 5. 7 + 5 = 12 pieces.'),
    dict(ch='1', scen='six lakh four thousand seventy · digit sum',
         stem='Kishore writes "six lakh four thousand seventy" in figures. What is the sum of the digits he writes?',
         opts=['17', '16', '13', '19'],
         hint='Be careful with the zeros in the thousands and hundreds places.',
         sol='Six lakh four thousand seventy = 6,04,070. Digit sum: 6 + 0 + 4 + 0 + 7 + 0 = 17.'),

    # ---------------- Part 2 · Operations
    dict(ch='2', scen='brackets in 6 plus 4 times 8 minus 2 for the largest value',
         stem='Kajal can put brackets into 6 + 4 × 8 − 2 in different ways. Which way gives the largest value?',
         opts=['(6 + 4) × 8 − 2', '(6 + 4) × (8 − 2)', '6 + 4 × (8 − 2)', '6 + (4 × 8) − 2'],
         hint='Work out each one.',
         sol='(6 + 4) × 8 − 2 = 80 − 2 = 78. (6 + 4) × (8 − 2) = 60. 6 + 4 × (8 − 2) = 30. 6 + 32 − 2 = 36. The largest is 78.'),
    dict(ch='2', scen='48 rows of 52 seats compared with 50 times 50',
         stem='A hall has 48 rows of 52 seats. Kartik estimates the number of seats as 50 × 50. By how much is his estimate more than the exact number?',
         opts=['4', '104', '96', '0'],
         hint='Work out 48 × 52 exactly.',
         sol='48 × 52 = 48 × 50 + 48 × 2 = 2,400 + 96 = 2,496. 50 × 50 = 2,500. 2,500 − 2,496 = 4.'),
    dict(ch='2', scen='999 times 47 plus 47 using the distributive property',
         stem='Without long multiplication, Megha works out 999 × 47 + 47. What does she get?',
         opts=['47,000', '46,953', '47,047', '46,000'],
         hint='47 is 1 × 47.',
         sol='999 × 47 + 1 × 47 = (999 + 1) × 47 = 1,000 × 47 = 47,000.'),

    # ---------------- Part 3 · Fractions, Decimals & Percentages
    dict(ch='3', scen='36 of 45 in maths and 42 of 60 in science · percentage gap',
         stem='Lakshya scored 36 out of 45 in Maths and 42 out of 60 in Science. How many percentage points higher is his Maths score?',
         opts=['10', '6', '8', '12'],
         hint='Change each score into a percentage.',
         sol='36/45 = 4/5 = 80%. 42/60 = 7/10 = 70%. 80 − 70 = 10 percentage points.'),
    dict(ch='3', scen='equal pair among 0.45 9/20 4/9 0.405',
         stem='Which two of these are equal: 0.45, 9/20, 4/9, 0.405?',
         opts=['0.45 and 9/20', '4/9 and 0.45', '0.405 and 4/9', '9/20 and 0.405'],
         hint='Change each fraction into a decimal.',
         sol='9/20 = 45/100 = 0.45. 4/9 = 0.444…, which is neither 0.45 nor 0.405. So 0.45 and 9/20 are equal.'),
    dict(ch='3', scen='1.25 L jug poured into 0.15 L glasses',
         stem='Tara pours juice from a 1.25 L jug into glasses that hold 0.15 L each. She fills as many glasses as she can. What is the result?',
         opts=['8 glasses, 50 mL left', '8 glasses, 5 mL left', '9 glasses, nothing left', '7 glasses, 200 mL left'],
         hint='Work in millilitres: 1.25 L = 1,250 mL.',
         sol='1,250 mL ÷ 150 mL: 8 glasses use 1,200 mL. 1,250 − 1,200 = 50 mL left.'),
    dict(ch='3', scen='three quarters of a number is 45 · two fifths of it',
         stem='Three quarters of a number is 45. What is two fifths of the same number?',
         opts=['24', '18', '27', '36'],
         hint='Find the whole number first.',
         sol='3/4 of the number is 45, so 1/4 is 15 and the number is 60. 2/5 of 60 = 24.'),

    # ---------------- Part 4 · Geometry
    dict(ch='5', scen='four angles round a point with two equal',
         stem='Four angles meet at a point. One is a right angle, one is 70°, and the other two are equal. What is each of the equal angles?',
         opts=['100°', '110°', '90°', '200°'],
         hint='Angles round a point add up to 360°.',
         sol='360° − 90° − 70° = 200°. The two equal angles share it: 200° ÷ 2 = 100°.'),
    dict(ch='5', scen='always true statement about quadrilaterals',
         stem='Which statement about four-sided shapes is ALWAYS true?',
         opts=['Every square is a rhombus', 'Every rhombus is a square', 'Every rectangle is a square', 'Every parallelogram is a rectangle'],
         hint='A rhombus has four equal sides. Does it need square corners?',
         sol='A square has four equal sides, so it is a rhombus. A rhombus need not have square corners, a rectangle need not have equal sides, and a parallelogram need not have square corners.'),
    dict(ch='5', scen='lines of symmetry of hexagon rectangle and isosceles triangle',
         stem='Om adds the numbers of lines of symmetry of a regular hexagon, a rectangle that is not a square and an isosceles triangle that is not equilateral. What total does he get?',
         opts=['9', '8', '10', '12'],
         hint='The diagonals of a rectangle are not lines of symmetry.',
         sol='Regular hexagon: 6. Rectangle (not a square): 2. Isosceles triangle (not equilateral): 1. 6 + 2 + 1 = 9.'),

    # ---------------- Part 5 · Mensuration
    dict(ch='6', scen='litres in a 1.2 m by 50 cm by 40 cm tank',
         stem='A tank is 1.2 m long, 50 cm wide and 40 cm deep. How many litres of water does it hold when full? (1 L = 1,000 cm³)',
         opts=['240 L', '2,400 L', '24 L', '480 L'],
         hint='Change 1.2 m into centimetres first.',
         sol='1.2 m = 120 cm. Volume: 120 × 50 × 40 = 2,40,000 cm³. 2,40,000 ÷ 1,000 = 240 L.'),
    dict(ch='6', scen='perimeter after cutting a square from each corner of a rectangle',
         stem='Prachi cuts a 4 cm square from each corner of a 15 cm by 9 cm rectangle. What is the perimeter of the shape that is left?',
         opts=['48 cm', '32 cm', '64 cm', '40 cm'],
         hint='Look at what each cut takes away and what it adds to the boundary.',
         sol='Each cut removes 4 + 4 cm of the old edge but adds 4 + 4 cm of new edge, so the perimeter does not change. It is 2 × (15 + 9) = 48 cm.'),
    dict(ch='6', scen='grass for a right triangle 24 m by 18 m at ₹15 per m²',
         stem='A right-angled triangular plot has its two shorter sides 24 m and 18 m. Grass costs ₹15 per square metre. How much does it cost to grass the whole plot?',
         opts=['₹3,240', '₹6,480', '₹2,160', '₹3,600'],
         hint='Area of a right-angled triangle = half of (base × height).',
         sol='Area: half of 24 × 18 = 216 m². Cost: 216 × 15 = ₹3,240. (₹6,480 forgets to halve.)'),

    # ---------------- Part 6 · Data Handling
    dict(ch='8', scen='bar graph of rainfall June to September',
         fig=drawing(300, 200, bars([('Jun', 120), ('Jul', 240), ('Aug', 200), ('Sep', 80)], 280, 40, 'Rainfall (mm)')),
         stem='The bar graph shows the rainfall in a town. How many more millimetres fell in July and August together than in June and September together?',
         opts=['240', '200', '280', '160'],
         hint='Read each bar against the scale, which goes up in 40s.',
         sol='July 240 + August 200 = 440 mm. June 120 + September 80 = 200 mm. 440 − 200 = 240 mm.'),

    # ---------------- Part 7 · Applied Mathematics
    dict(ch='9', scen='two trains 330 km apart moving towards each other',
         stem='Two trains are 330 km apart. They start at the same time and move towards each other at 60 km/h and 50 km/h. After how long do they meet?',
         opts=['3 h', '6 h', '3 h 30 min', '2 h 30 min'],
         hint='Together they close the gap by 60 + 50 km every hour.',
         sol='Each hour the gap gets 60 + 50 = 110 km smaller. 330 ÷ 110 = 3 hours.'),
    dict(ch='9', scen='2 h at 60 km/h and 3 h at 40 km/h · average speed',
         stem='Mihir drives for 2 hours at 60 km/h and then for 3 hours at 40 km/h. What is his average speed for the whole drive?',
         opts=['48 km/h', '50 km/h', '45 km/h', '52 km/h'],
         hint='Find the total distance and the total time.',
         sol='Distance: 2 × 60 + 3 × 40 = 120 + 120 = 240 km. Time: 5 h. 240 ÷ 5 = 48 km/h. (50 is the plain average of the speeds.)'),
    dict(ch='9', scen='tap dripping 25 mL every 2 minutes for a day',
         stem='A leaking tap drips 25 mL of water every 2 minutes. How many litres does it waste in one whole day?',
         opts=['18 L', '36 L', '1.8 L', '180 L'],
         hint='How many 2-minute blocks are there in 24 hours?',
         sol='One day = 24 × 60 = 1,440 minutes = 720 blocks of 2 minutes. 720 × 25 = 18,000 mL = 18 L.'),
    dict(ch='9', scen='20 notebooks · packs of 6 for ₹105 or ₹19 each',
         stem='Notebooks cost ₹19 each, or ₹105 for a pack of 6. Ishaan needs exactly 20 notebooks and wants to pay as little as possible. How much does he pay?',
         opts=['₹353', '₹380', '₹420', '₹350'],
         hint='Compare 3 packs plus some single notebooks with 4 packs.',
         sol='3 packs give 18 notebooks for ₹315; 2 more cost ₹38: total ₹353. 4 packs (24 notebooks) cost ₹420. 20 singles cost ₹380. The least is ₹353.'),

    # ---------------- Part 8 · Mathematical Reasoning
    dict(ch='10', scen='which number is in the series 5 12 19 26',
         fig=cards([5, 12, 19, 26, '…'], size=40),
         stem='The series keeps going up by the same amount. Which of these numbers is in the series: 100, 103, 108, 115?',
         opts=['103', '100', '108', '115'],
         hint='Every number in the series is 5 more than a multiple of 7.',
         sol='The series adds 7 each time, so each number is 5 + a multiple of 7. 103 − 5 = 98 = 7 × 14. 100 − 5 = 95, 108 − 5 = 103 and 115 − 5 = 110 are not multiples of 7.'),
    dict(ch='10', scen='leap year 1 February Thursday · day of 31 March',
         stem='In a leap year, 1 February is a Thursday. On which day of the week is 31 March?',
         opts=['Sunday', 'Saturday', 'Monday', 'Friday'],
         hint='A leap year February has 29 days.',
         sol='1 March is 29 days after 1 February: 4 weeks + 1 day, so Friday. 31 March is 30 days after 1 March: 4 weeks + 2 days, so Sunday.'),
    dict(ch='10', scen='seven face-up cards flipped two at a time',
         stem='Seven cards lie face up. In each move Nitin must turn over exactly two cards. What is the fewest number of moves he needs to make all seven cards face down?',
         opts=['It is impossible', '4', '3', '7'],
         hint='Think about whether the number of face-up cards is odd or even after each move.',
         sol='Each move changes the number of face-up cards by 2 or 0, so it stays odd: 7, 5, 3, 1, … It can never become 0. So it is impossible.'),
    dict(ch='10', scen='rectangles of all sizes in a 2 by 3 grid',
         fig=grid([[''] * 3, [''] * 3], cell=40),
         stem='How many rectangles of all sizes are there in this grid? (Squares count as rectangles.)',
         opts=['18', '17', '12', '24'],
         hint='A rectangle is fixed by choosing 2 of the vertical lines and 2 of the horizontal lines.',
         sol='There are 4 vertical lines and 3 horizontal lines. Pairs of vertical lines: 6. Pairs of horizontal lines: 3. Rectangles: 6 × 3 = 18.'),

    # ---------------- Section II · Star Questions
    dict(ch='1+10', scen='numbers up to 50 with exactly three factors',
         stem='How many numbers from 1 to 50 have exactly three factors?',
         opts=['4', '3', '5', '7'],
         hint='Try 4: its factors are 1, 2 and 4. What kind of number is 4?',
         sol='A number with exactly 3 factors is a prime times itself: 4, 9, 25 and 49 (factors 1, p and p × p). The next, 121, is over 50. So 4 numbers.'),
    dict(ch='3+10', scen='decimal series multiplying by 3 from 0.2',
         fig=cards(['0.2', '0.6', '1.8', '5.4', '?'], size=40),
         stem='Each number in the series is found from the one before in the same way. Which number comes next?',
         opts=['16.2', '10.8', '15.4', '16.8'],
         hint='Compare 0.6 with 0.2.',
         sol='Each number is 3 times the one before: 0.2 × 3 = 0.6, 0.6 × 3 = 1.8, 1.8 × 3 = 5.4. Next: 5.4 × 3 = 16.2.'),
    dict(ch='6+10', scen='squares of side 1 2 3 4 in a row · perimeter',
         fig=drawing(270, 125, stair_squares()),
         stem='Squares of side 1 cm, 2 cm, 3 cm and 4 cm stand side by side on a line, as shown. What is the perimeter of the whole shape?',
         opts=['28 cm', '40 cm', '30 cm', '36 cm'],
         hint='Slide the steps of the top edge up and across: they make a simple rectangle outline.',
         sol='The shape is 1 + 2 + 3 + 4 = 10 cm wide and 4 cm tall. The steps on the top and left add up to 10 cm across and 4 cm up, so the perimeter is the same as a 10 cm by 4 cm rectangle: 2 × (10 + 4) = 28 cm. (40 adds all four square perimeters.)'),
    dict(ch='1+9', scen='shows every 45 and 60 minutes from 10 AM · shows on screen 1',
         stem='At a cinema, shows on Screen 1 start every 45 minutes and on Screen 2 every 60 minutes. Both start a show at 10:00 AM. How many shows start on Screen 1 from 10:00 AM until both next start together, counting both ends?',
         opts=['5', '4', '3', '6'],
         hint='Find when both screens next start at the same time.',
         sol='LCM of 45 and 60 is 180 minutes, so both next start at 1:00 PM. Screen 1 starts at 10:00, 10:45, 11:30, 12:15 and 1:00: 5 shows.'),
    dict(ch='3+9', scen='750 mL and 1.25 L juice at ₹48 per litre paid with ₹200',
         stem='Juice costs ₹48 per litre. Kirti buys one 750 mL pack and one 1.25 L pack and pays with ₹200. How much change does she get?',
         opts=['₹104', '₹96', '₹114', '₹86'],
         hint='Add the two amounts in litres first.',
         sol='750 mL = 0.75 L. 0.75 + 1.25 = 2 L. Cost: 2 × 48 = ₹96. Change: 200 − 96 = ₹104.'),
]
