# AMO Level-2 · Class 5 · Practice Paper 6  (format: see paper01.py)


def pict(rows, em, key, lw=90, step=28):
    """Pictograph: one row of symbols per label, then the key."""
    prims = []
    for i, (lab, n) in enumerate(rows):
        y = 18 + i * 34
        prims += [('rect', 0, y - 15, lw, 30, 'lilac'), ('text', lw / 2, y, lab, 12)]
        prims += [('emoji', em, lw + 20 + k * step, y, 24) for k in range(n)]
    y = 18 + len(rows) * 34 + 6
    prims += [('emoji', em, 14, y, 20), ('text', 40 + len(key) * 3.6, y, '= ' + key, 12)]
    return prims


def plus_shape():
    s = 30
    cells = [(1, 0), (0, 1), (1, 1), (2, 1), (1, 2)]
    prims = [('rect', 10 + c * s, 10 + r * s, s, s, 'green') for c, r in cells]
    prims.append(('text', 10 + 1.5 * s, 2, '3 cm', 10))
    return prims


QUESTIONS = [
    # ---------------- Part 1 · Number System
    dict(ch='1', scen='smallest 5-digit number divisible by 8 12 and 15',
         stem='What is the smallest 5-digit number that is divisible by 8, by 12 and by 15?',
         opts=['10,080', '10,020', '10,200', '10,120'],
         hint='Find the LCM of 8, 12 and 15 first.',
         sol='LCM of 8, 12 and 15 is 120. 120 × 83 = 9,960 is a 4-digit number. 120 × 84 = 10,080 is the smallest 5-digit multiple.'),
    dict(ch='1', scen='primes between 60 and 80',
         stem='How many prime numbers are there between 60 and 80?',
         opts=['5', '4', '6', '3'],
         hint='Only odd numbers not ending in 5 need checking.',
         sol='Check 61, 63, 67, 69, 71, 73, 77, 79. 63 = 7 × 9, 69 = 3 × 23 and 77 = 7 × 11. The primes are 61, 67, 71, 73 and 79: 5.'),
    dict(ch='1', scen='second largest of CDXC CCCXCIX CDLIX CDXLIV',
         stem='Which is the 2nd largest of these Roman numerals: CDXC, CCCXCIX, CDLIX, CDXLIV?',
         opts=['CDLIX', 'CDXC', 'CDXLIV', 'CCCXCIX'],
         hint='Change each one into an ordinary number.',
         sol='CDXC = 490, CCCXCIX = 399, CDLIX = 459, CDXLIV = 444. In order from largest: 490, 459, 444, 399. The 2nd largest is CDLIX.'),

    # ---------------- Part 2 · Operations
    dict(ch='2', scen='100 minus square bracket 15 minus 3 times 8 minus 5 divided by 4 plus 2',
         fig=equations([['100 − [(15 − 3) × (8 − 5)] ÷ (4 + 2)', '=', '?']], size=26),
         stem='What is the value of this expression?',
         opts=['94', '14', '30', '88'],
         hint='Work out each round bracket, then the square bracket, then divide.',
         sol='15 − 3 = 12, 8 − 5 = 3, 4 + 2 = 6. Square bracket: 12 × 3 = 36. 36 ÷ 6 = 6. 100 − 6 = 94.'),
    dict(ch='2', scen='bus fare ₹28 for 196 people · estimate 30 times 200',
         stem='A trip costs ₹28 per person and 196 people go. Sapna estimates the total as 30 × 200. How much more is her estimate than the real total?',
         opts=['₹512', '₹488', '₹600', '₹412'],
         hint='Work out 28 × 196 as 28 × 200 − 28 × 4.',
         sol='Real total: 28 × 196 = 28 × 200 − 28 × 4 = 5,600 − 112 = ₹5,488. Estimate: ₹6,000. Difference: ₹512.'),
    dict(ch='2', scen='125 times 72 minus 125 times 8',
         stem='Without long multiplication, Vipul works out 125 × 72 − 125 × 8. What is the answer?',
         opts=['8,000', '9,000', '7,000', '8,125'],
         hint='Both parts have 125 × something.',
         sol='125 × 72 − 125 × 8 = 125 × (72 − 8) = 125 × 64. 125 × 8 = 1,000, so 125 × 64 = 1,000 × 8 = 8,000.'),

    # ---------------- Part 3 · Fractions, Decimals & Percentages
    dict(ch='3', scen='₹1,600 shared 30 percent 45 percent and the rest',
         stem='₹1,600 is shared among three children. Aman gets 30% and Bela gets 45%. Chirag gets the rest. How much more does Bela get than Chirag?',
         opts=['₹320', '₹240', '₹480', '₹400'],
         hint='Chirag gets 100% − 30% − 45%.',
         sol='Chirag gets 25% = ₹400. Bela gets 45% = 45 × 16 = ₹720. 720 − 400 = ₹320.'),
    dict(ch='3', scen='fraction strictly between 0.6 and 0.65',
         stem='Which of these fractions lies between 0.6 and 0.65 (and is equal to neither)?',
         opts=['5/8', '3/5', '2/3', '13/20'],
         hint='Change each fraction into a decimal.',
         sol='5/8 = 0.625, which is between them. 3/5 = 0.6 and 13/20 = 0.65 are the end values themselves. 2/3 = 0.666… is more than 0.65.'),
    dict(ch='3', scen='2.4 times 1.5 plus 0.6 divided by 0.2',
         stem='What is 2.4 × 1.5 + 0.6 ÷ 0.2?',
         opts=['6.6', '3.9', '5.4', '0.75'],
         hint='Multiply and divide before you add.',
         sol='2.4 × 1.5 = 3.6. 0.6 ÷ 0.2 = 3. 3.6 + 3 = 6.6.'),
    dict(ch='3', scen='tank 3/5 full · 48 L used · now 1/3 full',
         stem='A tank is 3/5 full of water. After 48 L is used, it is 1/3 full. How many litres does the full tank hold?',
         opts=['180 L', '144 L', '240 L', '120 L'],
         hint='Write 3/5 and 1/3 in fifteenths.',
         sol='3/5 = 9/15 and 1/3 = 5/15. The 48 L used is 4/15 of the tank, so 1/15 is 12 L and the full tank is 15 × 12 = 180 L.'),

    # ---------------- Part 4 · Geometry
    dict(ch='5', scen='two crossing lines with a 65 degree angle · the other two angles',
         stem='Two straight lines cross, making four angles. One of the angles is 65°. What is the sum of the two angles that are NOT equal to 65°?',
         opts=['230°', '115°', '295°', '250°'],
         hint='Angles next to each other on a straight line add up to 180°.',
         sol='The angle opposite the 65° angle is also 65°. Each of the other two angles is 180° − 65° = 115°. Their sum is 230°.'),
    dict(ch='5', scen='quadrilateral 80 100 80 with opposite sides parallel',
         stem='A four-sided shape has opposite sides parallel. Three of its angles, in order, are 80°, 100° and 80°. What is the fourth angle, and what is the shape?',
         opts=['100°, parallelogram', '80°, rectangle', '100°, kite', '120°, trapezium'],
         hint='The angles of a four-sided shape add up to 360°.',
         sol='360° − 80° − 100° − 80° = 100°. Both pairs of opposite sides are parallel, so it is a parallelogram. It is not a rectangle because its angles are not 90°.'),
    dict(ch='5', scen='shape with rotational symmetry but no line of symmetry',
         stem='Which of these shapes has rotational symmetry (of order 2 or more) but NO line of symmetry?',
         opts=['A parallelogram that is not a rectangle or a rhombus', 'A rectangle', 'An isosceles triangle', 'A kite'],
         hint='Try folding each shape, then try turning it half way round.',
         sol='A parallelogram (not a rectangle or rhombus) looks the same after a half turn, but no fold makes its halves match. A rectangle has 2 lines of symmetry; the isosceles triangle and the kite each have 1 line but no rotational symmetry.'),

    # ---------------- Part 5 · Mensuration
    dict(ch='6', scen='bricks 25 by 10 by 8 cm for a 2 m by 20 cm by 1 m wall',
         stem='A wall is 2 m long, 20 cm thick and 1 m high. How many bricks of size 25 cm × 10 cm × 8 cm are needed to build it? (Ignore the cement.)',
         opts=['200', '400', '100', '2,000'],
         hint='Change all lengths to centimetres and find both volumes.',
         sol='Wall: 200 × 20 × 100 = 4,00,000 cm³. Brick: 25 × 10 × 8 = 2,000 cm³. 4,00,000 ÷ 2,000 = 200 bricks.'),
    dict(ch='6', scen='plus shape of five 3 cm squares · perimeter',
         fig=drawing(110, 110, plus_shape()),
         stem='Five squares of side 3 cm make this plus shape. What is its perimeter?',
         opts=['36 cm', '60 cm', '45 cm', '30 cm'],
         hint='Count the outside edges.',
         sol='The outline has 12 edges, each 3 cm long: 12 × 3 = 36 cm. (60 cm adds all five squares\' perimeters.)'),
    dict(ch='6', scen='fertiliser for a 1.2 km by 400 m park at ₹5 per 100 m²',
         stem='A park is 1.2 km long and 400 m wide. Fertiliser costs ₹5 for every 100 m². How much does it cost to fertilise the whole park?',
         opts=['₹24,000', '₹2,400', '₹2,40,000', '₹9,600'],
         hint='Change 1.2 km into metres first.',
         sol='1.2 km = 1,200 m. Area: 1,200 × 400 = 4,80,000 m². That is 4,800 lots of 100 m². Cost: 4,800 × 5 = ₹24,000.'),

    # ---------------- Part 6 · Data Handling
    dict(ch='8', scen='pictograph of trees planted · 5B with 50 percent more',
         fig=drawing(300, 190, pict([('Class 5A', 6), ('Class 5B', 4), ('Class 5C', 7), ('Class 5D', 5)], '🌳', '8 trees')),
         stem='The pictograph shows trees planted by four classes. If Class 5B had planted 50% more trees, how many symbols would its row show?',
         opts=['6', '5', '7', '4'],
         hint='50% more means half as many again.',
         sol='5B planted 4 × 8 = 32 trees. 50% more: 32 + 16 = 48 trees. 48 ÷ 8 = 6 symbols.'),

    # ---------------- Part 7 · Applied Mathematics
    dict(ch='9', scen='plane 2,100 km at 700 km/h leaving 10:35 PM',
         stem='A plane leaves at 10:35 PM and flies 2,100 km at 700 km/h. At what time does it land? (Ignore time zones.)',
         opts=['1:35 AM', '1:35 PM', '12:35 AM', '2:05 AM'],
         hint='Find the flying time first.',
         sol='2,100 ÷ 700 = 3 hours. 10:35 PM + 3 hours = 1:35 AM the next day.'),
    dict(ch='9', scen='100 km at 50 km/h then 150 km at 75 km/h · average speed',
         stem='A car covers the first 100 km at 50 km/h and the next 150 km at 75 km/h. What is its average speed for the whole 250 km?',
         opts=['62.5 km/h', '62 km/h', '65 km/h', '60 km/h'],
         hint='Find the time for each part.',
         sol='First part: 100 ÷ 50 = 2 h. Second: 150 ÷ 75 = 2 h. 250 km in 4 h: 250 ÷ 4 = 62.5 km/h.'),
    dict(ch='9', scen='hours in February 2028',
         stem='How many hours are there in the month of February 2028?',
         opts=['696', '672', '720', '744'],
         hint='Is 2028 a leap year?',
         sol='2028 is divisible by 4, so it is a leap year and February has 29 days. 29 × 24 = 696 hours.'),
    dict(ch='9', scen='18 mangoes at ₹360 a dozen and 1.5 kg grapes at ₹96',
         stem='Mangoes cost ₹360 a dozen and grapes cost ₹96 per kg. Gopal buys 18 mangoes and 1.5 kg of grapes and pays with ₹1,000. How much change does he get?',
         opts=['₹316', '₹304', '₹416', '₹346'],
         hint='18 mangoes is one and a half dozen.',
         sol='18 mangoes: 360 + 180 = ₹540. Grapes: 96 + 48 = ₹144. Total ₹684. Change: 1,000 − 684 = ₹316.'),

    # ---------------- Part 8 · Mathematical Reasoning
    dict(ch='10', scen='double then subtract one from 3',
         fig=cards([3, 5, 9, 17, 33, '?'], size=38),
         stem='Each number in this series comes from the one before by the same two steps. Which number comes next?',
         opts=['65', '49', '66', '64'],
         hint='Double the number and then adjust.',
         sol='3 × 2 − 1 = 5, 5 × 2 − 1 = 9, 9 × 2 − 1 = 17, 17 × 2 − 1 = 33. Next: 33 × 2 − 1 = 65.'),
    dict(ch='10', scen='day of the week 100 days after a Wednesday',
         stem='Today is Wednesday. Which day of the week will it be 100 days from today?',
         opts=['Friday', 'Thursday', 'Saturday', 'Wednesday'],
         hint='Every 7 days it is Wednesday again.',
         sol='100 = 14 × 7 + 2. After 98 days it is Wednesday again; 2 more days gives Friday.'),
    dict(ch='10', scen='product of 25 whole numbers is odd · their sum',
         stem='Ekta multiplies 25 whole numbers and the answer is odd. What can you say about the sum of the same 25 numbers?',
         opts=['It is odd', 'It is even', 'It can be odd or even', 'It is a multiple of 25'],
         hint='If even one of the numbers were even, the product would be even.',
         sol='An odd product means all 25 numbers are odd. Odd + odd is even, so 24 odd numbers add to an even total, and the 25th odd number makes it odd.'),
    dict(ch='10', scen='ways to climb 6 stairs in steps of 1 or 2',
         stem='Hrithik climbs a staircase of 6 steps. Each time he goes up either 1 step or 2 steps. In how many different ways can he reach the top?',
         opts=['13', '12', '8', '21'],
         hint='Count the ways for 1, 2, 3, … steps and look for a pattern.',
         sol='Ways for 1 step: 1. 2 steps: 2. Each later number is the sum of the two before (the last move is 1 step or 2 steps): 3 steps 3, 4 steps 5, 5 steps 8, 6 steps 13.'),

    # ---------------- Section II · Star Questions
    dict(ch='1+10', scen='numbers leaving remainder 2 on division by 3 and by 5 · tenth',
         fig=cards([2, 17, 32, 47, '…'], size=40),
         stem='These are the numbers that leave a remainder of 2 when divided by 3 and also when divided by 5, in order. What is the 10th number?',
         opts=['137', '152', '150', '122'],
         hint='The numbers go up by the LCM of 3 and 5.',
         sol='They go up by 15 each time. The 10th number is 2 + 9 × 15 = 2 + 135 = 137.'),
    dict(ch='3+10', scen='doubling twentieths · first more than 1 as a decimal',
         fig=cards(['1/20', '2/20', '4/20', '8/20', '…'], size=40),
         stem='Each fraction is double the one before. What is the first fraction in the pattern that is more than 1, written as a decimal?',
         opts=['1.6', '0.8', '3.2', '1.2'],
         hint='1 whole is 20/20.',
         sol='Next come 16/20 (less than 1) and then 32/20, which is more than 20/20. 32/20 = 1.6.'),
    dict(ch='6+10', scen='rectangles 1 by 2 2 by 3 3 by 4 · first with area over 100',
         stem='Kajal draws rectangles that are 1 cm by 2 cm, 2 cm by 3 cm, 3 cm by 4 cm, and so on. What is the perimeter of the first rectangle whose area is more than 100 cm²?',
         opts=['42 cm', '38 cm', '110 cm', '44 cm'],
         hint='The areas are 2, 6, 12, 20, …',
         sol='9 cm by 10 cm has area 90 cm². The next, 10 cm by 11 cm, has area 110 cm², the first over 100. Its perimeter: 2 × (10 + 11) = 42 cm.'),
    dict(ch='1+9', scen='Roman clock hour hand between IX and X minute hand at VI · 2 h 45 min later',
         stem='A clock tower has Roman numerals. In the morning, its hour hand is halfway between IX and X and its minute hand points at VI. What time will it be 2 hours 45 minutes later?',
         opts=['12:15 PM', '11:15 AM', '12:45 PM', '12:30 PM'],
         hint='First read the time. VI on the minute hand means 30 minutes.',
         sol='Hour hand halfway between IX (9) and X (10), minute hand at VI: 9:30 AM. 9:30 + 2 h 45 min = 12:15 PM.'),
    dict(ch='3+9', scen='train at 0.8 km per minute for 240 km',
         stem='A train travels at 0.8 km per minute. How long does it take to travel 240 km?',
         opts=['5 h', '3 h 12 min', '30 h', '4 h 48 min'],
         hint='How many minutes does it take to cover 4 km?',
         sol='0.8 km per minute means 4 km every 5 minutes. 240 km is 60 lots of 4 km: 60 × 5 = 300 minutes = 5 hours.'),
]
