# AMO Level-2 · Class 5 · Practice Paper 9  (format: see paper01.py)


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


def rect_mid():
    return [('rect', 10, 10, 180, 120, 'yellow'), ('poly', [(10, 10), (100, 10), (10, 130)], 'white', True),
            ('text', 100, 142, '9 cm', 11), ('text', 205, 70, '6 cm', 11), ('text', 100, 2, 'middle of the top side', 10)]


def l_steps():
    s = 16
    prims = []
    for k, x0 in ((2, 10), (3, 70), (4, 150)):
        cells = [(0, r) for r in range(k)] + [(c, k - 1) for c in range(1, k)]
        prims += [('rect', x0 + c * s, 10 + (4 - k) * s + r * s, s, s, 'green') for c, r in cells]
    prims += [('text', 26, 88, '1st', 11), ('text', 94, 88, '2nd', 11), ('text', 182, 88, '3rd', 11)]
    return prims


QUESTIONS = [
    # ---------------- Part 1 · Number System
    dict(ch='1', scen='multiples of 3 up to 100 not divisible by 2 or 5',
         stem='How many numbers from 1 to 100 are multiples of 3 but are NOT divisible by 2 and NOT divisible by 5?',
         opts=['14', '17', '11', '20'],
         hint='The numbers you want are odd multiples of 3 that do not end in 5.',
         sol='Odd multiples of 3 up to 100: 3, 9, 15, …, 99, which is 17. Remove those ending in 5 (odd multiples of 15): 15, 45, 75, which is 3. 17 − 3 = 14.'),
    dict(ch='1', scen='children in rows of 4 6 or 9 between 200 and 230',
         stem='A group of children can stand in rows of 4, in rows of 6 or in rows of 9, with nobody left over each time. There are between 200 and 230 children. How many are there?',
         opts=['216', '180', '204', '228'],
         hint='The number is a common multiple of 4, 6 and 9.',
         sol='LCM of 4, 6 and 9 is 36. Its multiples are 180, 216, 252, … Only 216 is between 200 and 230. (204 and 228 are multiples of 4 and 6 but not of 9.)'),
    dict(ch='1', scen='MMXXVI minus MCMXLVII in Roman numerals',
         stem='A school started in MCMXLVII. How old is it in MMXXVI, written as a Roman numeral?',
         opts=['LXXIX', 'LXXXI', 'LXIX', 'LXXIV'],
         hint='MCMXLVII = 1947 and MMXXVI = 2026.',
         sol='2026 − 1947 = 79 years. 79 = 50 + 10 + 10 + 9 = LXXIX.'),

    # ---------------- Part 2 · Operations
    dict(ch='2', scen='60 divided by 5 times 3 · who is right',
         stem='Ravi says 60 ÷ 5 × 3 = 4. Uma says it is 36. Who is right?',
         opts=['Uma, 36', 'Ravi, 4', 'Neither: it is 12', 'Both, it depends on the order'],
         hint='Division and multiplication are done from left to right.',
         sol='Working left to right: 60 ÷ 5 = 12, then 12 × 3 = 36. Uma is right. Ravi wrongly did 5 × 3 first.'),
    dict(ch='2', scen='round then add versus add then round to the nearest hundred',
         stem='Sakshi rounds 2,346, 1,478 and 3,952 to the nearest hundred and then adds. Mohit adds the exact numbers and then rounds the total to the nearest hundred. What is the difference between their answers?',
         opts=['0', '100', '24', '76'],
         hint='Work out both answers.',
         sol='Sakshi: 2,300 + 1,500 + 4,000 = 7,800. Mohit: 2,346 + 1,478 + 3,952 = 7,776, which rounds to 7,800. The difference is 0.'),
    dict(ch='2', scen='999 times 999 plus 999',
         stem='What is 999 × 999 + 999?',
         opts=['9,99,000', '9,98,001', '9,99,999', '10,00,000'],
         hint='999 = 999 × 1.',
         sol='999 × 999 + 999 × 1 = 999 × (999 + 1) = 999 × 1,000 = 9,99,000.'),

    # ---------------- Part 3 · Fractions, Decimals & Percentages
    dict(ch='3', scen='book ₹240 with 75 percent saved and 20 percent from brother',
         stem='A book costs ₹240. Kriti has 75% of this amount. Her brother gives her money equal to 20% of the price. How much more does she need?',
         opts=['₹12', '₹60', '₹48', '₹0'],
         hint='Find 75% and 20% of ₹240.',
         sol='75% of 240 = ₹180. 20% of 240 = ₹48. She has 180 + 48 = ₹228. She needs 240 − 228 = ₹12 more.'),
    dict(ch='3', scen='which division equals 3.2 divided by 0.08',
         stem='Which of these has the same value as 3.2 ÷ 0.08?',
         opts=['320 ÷ 8', '32 ÷ 8', '3.2 ÷ 8', '0.32 ÷ 0.8'],
         hint='Multiply both numbers by 100.',
         sol='Multiplying both numbers by 100 does not change a division: 3.2 ÷ 0.08 = 320 ÷ 8 = 40. The others give 4, 0.4 and 0.4.'),
    dict(ch='3', scen='12.5 L petrol at ₹96.40 paid with ₹2,000',
         stem='Neel buys 12.5 litres of petrol at ₹96.40 per litre and pays with ₹2,000. How much change does he get?',
         opts=['₹795', '₹805', '₹1,205', '₹785'],
         hint='12.5 = 100 ÷ 8, so 12.5 × 96.40 = 9,640 ÷ 8.',
         sol='12.5 × 96.40 = 1,205 (12 × 96.40 = 1,156.80 and 0.5 × 96.40 = 48.20). Change: 2,000 − 1,205 = ₹795.'),
    dict(ch='3', scen='1,200 mL jug two thirds full · three quarters poured out',
         stem='A jug holds 1,200 mL when full. It is 2/3 full of milk. Juhi pours out 3/4 of the milk in it. How much milk is left in the jug?',
         opts=['200 mL', '400 mL', '600 mL', '300 mL'],
         hint='Find how much milk is in the jug first.',
         sol='2/3 of 1,200 = 800 mL in the jug. 3/4 of 800 = 600 mL poured out. Left: 800 − 600 = 200 mL.'),

    # ---------------- Part 4 · Geometry
    dict(ch='5', scen='minute hand turn from 3:10 to 3:55',
         stem='Through how many degrees does the minute hand of a clock turn from 3:10 to 3:55?',
         opts=['270°', '45°', '225°', '300°'],
         hint='The minute hand turns 360° in 60 minutes.',
         sol='It turns 6° every minute (360 ÷ 60). From 3:10 to 3:55 is 45 minutes: 45 × 6 = 270°.'),
    dict(ch='5', scen='one pair of parallel sides and equal non-parallel sides',
         stem='A four-sided shape has exactly one pair of parallel sides, and its other two sides are equal in length. What is it called?',
         opts=['Isosceles trapezium', 'Parallelogram', 'Kite', 'Rhombus'],
         hint='Exactly one pair of parallel sides means a trapezium.',
         sol='A shape with exactly one pair of parallel sides is a trapezium. When the other two sides are equal it is an isosceles trapezium. A parallelogram and a rhombus have two pairs of parallel sides; a kite has none.'),
    dict(ch='5', scen='house shape of an equilateral triangle on a square · symmetry',
         stem='Kiran draws an equilateral triangle on top of a square, with the triangle\'s bottom side on the top of the square, like a house. How many lines of symmetry does the shape have, and what is its order of rotational symmetry?',
         opts=['1 line, order 1', '1 line, order 2', '2 lines, order 2', '5 lines, order 1'],
         hint='Turning it upside down puts the point at the bottom.',
         sol='Only the vertical line through the top point is a line of symmetry. It looks the same only after a full turn, so its order of rotational symmetry is 1.'),

    # ---------------- Part 5 · Mensuration
    dict(ch='6', scen='12 by 8 by 5 cuboid of unit cubes painted outside · unpainted cubes',
         stem='A cuboid 12 cm × 8 cm × 5 cm is built from 1 cm cubes. The outside is painted. How many small cubes have no paint at all?',
         opts=['180', '480', '300', '240'],
         hint='Remove one layer of cubes from every face.',
         sol='The unpainted cubes form an inner cuboid that is 2 cm shorter in each direction: 10 × 6 × 3 = 180.'),
    dict(ch='6', scen='square and rectangle with perimeter 36 · area difference',
         stem='A square and a rectangle both have a perimeter of 36 cm. The rectangle is 12 cm long. Which has the greater area, and by how much?',
         opts=['The square, by 9 cm²', 'The rectangle, by 9 cm²', 'They are equal', 'The square, by 18 cm²'],
         hint='Find the side of the square and the width of the rectangle.',
         sol='Square: side 9 cm, area 81 cm². Rectangle: 12 + width = 18, so width 6 cm and area 72 cm². The square is bigger by 9 cm².'),
    dict(ch='6', scen='9 by 6 rectangle with a right triangle to the middle of the top side',
         fig=drawing(210, 145, rect_mid()),
         stem='A line is drawn from the bottom-left corner of a 9 cm by 6 cm rectangle to the middle of its top side. What is the area of the shaded part?',
         opts=['40.5 cm²', '27 cm²', '13.5 cm²', '45 cm²'],
         hint='The white part is a right-angled triangle.',
         sol='Rectangle: 9 × 6 = 54 cm². White triangle: sides 6 cm and 4.5 cm at the right angle, so half of 27 = 13.5 cm². Shaded: 54 − 13.5 = 40.5 cm².'),

    # ---------------- Part 6 · Data Handling
    dict(ch='8', scen='bar graph of fair tickets · money gap at ₹15',
         fig=drawing(300, 200, bars([('Thu', 120), ('Fri', 180), ('Sat', 90), ('Sun', 150)], 210, 30, 'Tickets sold')),
         stem='The bar graph shows tickets sold at a fair. Each ticket costs ₹15. How much more money was collected on the best day than on the worst day?',
         opts=['₹1,350', '₹90', '₹1,800', '₹2,700'],
         hint='Find the difference in tickets first.',
         sol='Best day: Friday, 180. Worst: Saturday, 90. Difference: 90 tickets. 90 × 15 = ₹1,350.'),

    # ---------------- Part 7 · Applied Mathematics
    dict(ch='9', scen='car at 60 km/h catching a bus at 45 km/h that left an hour earlier',
         stem='A bus leaves a town at 9:00 AM at 45 km/h. A car leaves the same town at 10:00 AM on the same road at 60 km/h. At what time does the car catch up with the bus?',
         opts=['1:00 PM', '12:00 noon', '2:00 PM', '12:30 PM'],
         hint='How far ahead is the bus at 10:00 AM?',
         sol='At 10:00 the bus is 45 km ahead. The car gains 60 − 45 = 15 km every hour. 45 ÷ 15 = 3 hours, so at 1:00 PM.'),
    dict(ch='9', scen='walk 4 km in 50 min and run 6 km in 25 min · average speed',
         stem='Devika walks 4 km in 50 minutes and then runs 6 km in 25 minutes. What is her average speed for the whole 10 km?',
         opts=['8 km/h', '7.5 km/h', '9.6 km/h', '10 km/h'],
         hint='Total time is 75 minutes.',
         sol='10 km in 75 minutes. 75 minutes = 1.25 hours. 10 ÷ 1.25 = 8 km/h.'),
    dict(ch='9', scen='meeting from 13:50 lasting 155 minutes',
         stem='A meeting starts at 13:50 and lasts 155 minutes. At what time does it end, on the 24-hour clock?',
         opts=['16:25', '15:45', '16:05', '04:25'],
         hint='155 minutes = 2 hours 35 minutes.',
         sol='155 minutes = 2 h 35 min. 13:50 + 2 h = 15:50. 15:50 + 35 min = 16:25.'),
    dict(ch='9', scen='₹500 changed into equal numbers of ₹20 notes and ₹5 coins',
         stem='Mukesh changes a ₹500 note into ₹20 notes and ₹5 coins. He gets the same number of notes as coins. How many notes and coins does he get altogether?',
         opts=['40', '20', '25', '50'],
         hint='One note and one coin together make ₹25.',
         sol='Each pair of one ₹20 note and one ₹5 coin is ₹25. 500 ÷ 25 = 20 pairs. That is 20 notes and 20 coins: 40 in all.'),

    # ---------------- Part 8 · Mathematical Reasoning
    dict(ch='10', scen='series 2 6 12 20 30',
         fig=cards([2, 6, 12, 20, 30, '?'], size=38),
         stem='What number comes next in Rashmi\'s series?',
         opts=['42', '40', '36', '44'],
         hint='Look at the differences: 4, 6, 8, 10, …',
         sol='The differences are 4, 6, 8, 10, so the next is 12: 30 + 12 = 42. (Also 1 × 2, 2 × 3, 3 × 4, 4 × 5, 5 × 6, 6 × 7.)'),
    dict(ch='10', scen='month of 2025 starting on the same weekday as January',
         stem='The year 2025 is not a leap year. Which month of 2025 begins on the same day of the week as January?',
         opts=['October', 'April', 'July', 'September'],
         hint='Count the days from 1 January to the 1st of each month.',
         sol='Days before each 1st: April 90, July 181, September 243, October 273. 273 = 39 weeks exactly, so 1 October is the same weekday as 1 January. (90, 181 and 243 are not multiples of 7.)'),
    dict(ch='10', scen='replace two numbers by their difference from 1 to 20 · last number',
         stem='Diya writes the numbers 1 to 20. Again and again she rubs out any two numbers and writes their difference instead. In the end one number is left. What can you say about it?',
         opts=['It is always even', 'It is always odd', 'It is always 0', 'It can be odd or even'],
         hint='What happens to whether the total is odd or even at each step?',
         sol='The total starts at 1 + 2 + … + 20 = 210, which is even. Replacing a and b by their difference changes the total by an even amount (2 × the smaller number), so the total stays even. The last number is always even.'),
    dict(ch='10', scen='3-digit odd numbers from 1 2 3 4 with repetition',
         stem='How many 3-digit odd numbers can be made from the digits 1, 2, 3 and 4 if digits may be used more than once?',
         opts=['32', '24', '64', '12'],
         hint='The ones digit must be 1 or 3.',
         sol='Hundreds digit: 4 choices. Tens digit: 4 choices. Ones digit: 1 or 3, so 2 choices. 4 × 4 × 2 = 32.'),

    # ---------------- Section II · Star Questions
    dict(ch='1+10', scen='tenth prime number',
         stem='Prime numbers are written in order: 2, 3, 5, 7, … What is the 10th prime number?',
         opts=['29', '23', '31', '27'],
         hint='Keep listing and check each number for factors.',
         sol='2, 3, 5, 7, 11, 13, 17, 19, 23, 29. The 10th is 29. (27 = 3 × 9 is not prime.)'),
    dict(ch='3+10', scen='series multiplying by 0.9 from 100',
         fig=cards(['100', '90', '81', '72.9', '?'], size=40),
         stem='Each number in Smita\'s series is the same fraction of the one before. Which number comes next?',
         opts=['65.61', '63.9', '64.8', '65.6'],
         hint='Each number is 9/10 of the one before.',
         sol='100 × 0.9 = 90, 90 × 0.9 = 81, 81 × 0.9 = 72.9. Next: 72.9 × 0.9 = 72.9 − 7.29 = 65.61.'),
    dict(ch='6+10', scen='L shapes of squares growing · area of the 10th',
         fig=drawing(220, 95, l_steps()),
         stem='Each L shape is made of 1 cm squares, with both arms one square longer than in the shape before. What is the area of the 10th L shape?',
         opts=['21 cm²', '20 cm²', '44 cm²', '22 cm²'],
         hint='The 1st shape has 3 squares, the 2nd 5, the 3rd 7.',
         sol='The number of squares goes up by 2 each time: 3, 5, 7, … The 10th has 3 + 9 × 2 = 21 squares, so its area is 21 cm².'),
    dict(ch='1+9', scen='chime every 20 minutes and buzzer every 30 minutes from noon',
         stem='A clock chimes every 20 minutes and a buzzer sounds every 30 minutes. Both sound together at 12:00 noon. When do they next sound together?',
         opts=['1:00 PM', '12:50 PM', '12:30 PM', '2:00 PM'],
         hint='Find the LCM of 20 and 30.',
         sol='LCM of 20 and 30 is 60 minutes. 12:00 noon + 60 minutes = 1:00 PM. (12:50 adds 20 and 30, and 2:00 PM is a later common time.)'),
    dict(ch='3+9', scen='₹1,500 savings · 0.4 on a bicycle and 3/20 on a helmet',
         stem='Ravi has ₹1,500 saved. He spends 0.4 of it on a bicycle and 3/20 of it on a helmet. How much does he have left?',
         opts=['₹675', '₹825', '₹900', '₹750'],
         hint='0.4 of 1,500 and 3/20 of 1,500.',
         sol='0.4 of 1,500 = ₹600. 3/20 of 1,500 = ₹225. Left: 1,500 − 600 − 225 = ₹675.'),
]
