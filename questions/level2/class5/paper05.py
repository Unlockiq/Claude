# AMO Level-2 · Class 5 · Practice Paper 5  (format: see paper01.py)


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


def cut_corners():
    s = 10
    P = lambda x, y: (10 + x * s, 10 + y * s)
    return [('poly', [P(3, 0), P(9, 0), P(12, 3), P(12, 9), P(9, 12), P(3, 12), P(0, 9), P(0, 3)], 'yellow'),
            ('poly', [P(0, 0), P(3, 0), P(0, 3)], 'white', True), ('poly', [P(12, 0), P(9, 0), P(12, 3)], 'white', True),
            ('poly', [P(12, 12), P(9, 12), P(12, 9)], 'white', True), ('poly', [P(0, 12), P(3, 12), P(0, 9)], 'white', True),
            ('text', *P(6, 13.2), '12 cm', 11), ('text', *P(1.5, -0.9), '3 cm', 10), ('text', *P(-1.6, 1.5), '3 cm', 10)]


QUESTIONS = [
    # ---------------- Part 1 · Number System
    dict(ch='1', scen='number equal to the sum of its other factors',
         stem='Which of these numbers is equal to the sum of all its factors other than itself: 12, 28, 18 or 20?',
         opts=['28', '12', '18', '20'],
         hint='For 12, add 1, 2, 3, 4 and 6.',
         sol='12: 1 + 2 + 3 + 4 + 6 = 16. 28: 1 + 2 + 4 + 7 + 14 = 28. 18: 1 + 2 + 3 + 6 + 9 = 21. 20: 1 + 2 + 4 + 5 + 10 = 22. Only 28 works.'),
    dict(ch='1', scen='greatest number dividing 75 and 99 leaving remainder 3',
         stem='What is the greatest number that divides both 75 and 99 and leaves a remainder of 3 each time?',
         opts=['24', '12', '8', '3'],
         hint='Take away the remainder first.',
         sol='The number must divide 75 − 3 = 72 and 99 − 3 = 96 exactly. HCF of 72 and 96 is 24. Check: 75 = 3 × 24 + 3 and 99 = 4 × 24 + 3.'),
    dict(ch='1', scen='value of 8 compared with value of 5 in 8,05,326',
         stem='In the number 8,05,326, how many times the value of the digit 5 is the value of the digit 8?',
         opts=['160', '16', '1,600', '40'],
         hint='Find the place of each digit.',
         sol='8 is in the lakhs place: 8,00,000. 5 is in the thousands place: 5,000. 8,00,000 ÷ 5,000 = 800 ÷ 5 = 160.'),

    # ---------------- Part 2 · Operations
    dict(ch='2', scen='correct value of 18 plus 6 divided by 3 times 4 minus 2',
         stem='Ravi wrote 18 + 6 ÷ 3 × 4 − 2 = 30. He did not follow the order of operations. What is the correct value?',
         opts=['24', '30', '16', '34'],
         hint='Divide and multiply before you add and subtract.',
         sol='6 ÷ 3 = 2 and 2 × 4 = 8. Then 18 + 8 − 2 = 24. (Ravi added 18 + 6 first.)'),
    dict(ch='2', scen='4,982 eggs in trays of 49 · full trays',
         stem='A farm packs 4,982 eggs into trays of 49 eggs each. Rohit estimates "about 100 trays". How many trays can actually be filled completely?',
         opts=['101', '100', '102', '99'],
         hint='49 × 100 = 4,900. How many eggs are left over?',
         sol='49 × 100 = 4,900, leaving 82 eggs. 82 eggs fill 1 more tray (49) with 33 left. So 101 full trays.'),
    dict(ch='2', scen='which product is not equal to 36 times 25',
         stem='Which of these is NOT equal to 36 × 25?',
         opts=['6 × 125', '9 × 100', '18 × 50', '12 × 75'],
         hint='Move factors from one number to the other.',
         sol='36 × 25 = 900. 9 × 100 = 900, 18 × 50 = 900, 12 × 75 = 900, but 6 × 125 = 750.'),

    # ---------------- Part 3 · Fractions, Decimals & Percentages
    dict(ch='3', scen='80 marbles 35 percent red 25 percent blue · 20 green added',
         stem='A jar has 80 marbles. 35% are red, 25% are blue and the rest are green. Rina adds 20 more green marbles. What percentage of the marbles are green now?',
         opts=['52%', '40%', '60%', '45%'],
         hint='Find the green marbles at the start.',
         sol='Green at first: 100% − 35% − 25% = 40% of 80 = 32. After adding 20: 52 green out of 100 marbles = 52%.'),
    dict(ch='3', scen='closest to 1 among 9/10 1.05 21/20 0.97',
         stem='Which of these is closest to 1: 9/10, 1.05, 21/20 or 0.97?',
         opts=['0.97', '1.05', '21/20', '9/10'],
         hint='Find how far each is from 1.',
         sol='9/10 = 0.9 is 0.1 away. 1.05 is 0.05 away. 21/20 = 1.05 is also 0.05 away. 0.97 is only 0.03 away, so it is closest.'),
    dict(ch='3', scen='0.6 of a number is 4.8 · 1.5 times the number',
         stem='Raju finds that 0.6 of a number is 4.8. What is 1.5 times the same number?',
         opts=['12', '7.2', '8', '2.88'],
         hint='Find the number first.',
         sol='0.6 of the number is 4.8, so the number is 4.8 ÷ 0.6 = 8. 1.5 × 8 = 12.'),
    dict(ch='3', scen='360 students cricket 5/12 football 1/4 rest kabaddi',
         stem='Of 360 students, 5/12 like cricket best and 1/4 like football best. The rest like kabaddi best. How many more students like cricket than kabaddi?',
         opts=['30', '60', '150', '120'],
         hint='Find each group in turn.',
         sol='Cricket: 5/12 of 360 = 150. Football: 1/4 of 360 = 90. Kabaddi: 360 − 150 − 90 = 120. 150 − 120 = 30.'),

    # ---------------- Part 4 · Geometry
    dict(ch='5', scen='angle between clock hands at 4 o\'clock and its type',
         stem='What is the smaller angle between the hands of a clock at exactly 4 o\'clock, and what type of angle is it?',
         opts=['120°, obtuse', '120°, acute', '150°, obtuse', '100°, obtuse'],
         hint='The angle between two numbers next to each other on a clock is 360° ÷ 12.',
         sol='Each gap between numbers is 30°. At 4 o\'clock the hands are 4 gaps apart: 4 × 30° = 120°. It is more than 90° and less than 180°, so obtuse.'),
    dict(ch='5', scen='triangle angles each 30 degrees more than the last · type',
         stem='The angles of a triangle go up in steps: the second is 30° more than the first, and the third is 30° more than the second. What type of triangle is it?',
         opts=['Right-angled', 'Acute-angled', 'Obtuse-angled', 'Equilateral'],
         hint='The angles add up to 180°.',
         sol='Take away the extras 0°, 30° and 60° (90° in all): 180° − 90° = 90°, so the smallest angle is 30°. The angles are 30°, 60° and 90°, so it is right-angled.'),
    dict(ch='5', scen='tiles round a point with two squares and some triangles',
         stem='At one point on a tiled floor, 2 squares and some equilateral triangles meet with no gaps. How many triangles meet there?',
         opts=['3', '2', '4', '6'],
         hint='The angles round a point add up to 360°.',
         sol='Two squares give 2 × 90° = 180°. The rest, 180°, is filled by 60° triangle corners: 180 ÷ 60 = 3 triangles.'),

    # ---------------- Part 5 · Mensuration
    dict(ch='6', scen='stone raising water 2 cm in an 80 by 50 cm tank',
         stem='A tank has a base 80 cm by 50 cm. Shruti drops a stone in and the water rises by 2 cm without overflowing. What is the volume of the stone?',
         opts=['8,000 cm³', '1,20,000 cm³', '4,000 cm³', '800 cm³'],
         hint='The stone takes the place of the water that has risen.',
         sol='The extra water height is 2 cm over the whole base: 80 × 50 × 2 = 8,000 cm³. That equals the volume of the stone.'),
    dict(ch='6', scen='difference in area of squares with perimeters 40 and 24',
         stem='Two squares have perimeters of 40 cm and 24 cm. What is the difference between their areas?',
         opts=['64 cm²', '16 cm²', '4 cm²', '256 cm²'],
         hint='Find the side of each square first.',
         sol='Sides: 40 ÷ 4 = 10 cm and 24 ÷ 4 = 6 cm. Areas: 100 cm² and 36 cm². Difference: 64 cm². (16 is the difference of the perimeters.)'),
    dict(ch='6', scen='12 cm square with four 3 cm corner triangles cut off',
         fig=drawing(140, 145, cut_corners()),
         stem='From each corner of a 12 cm square, Gita cuts off a right-angled triangle with two 3 cm sides, as shown. What is the area of the shape left?',
         opts=['126 cm²', '135 cm²', '108 cm²', '132 cm²'],
         hint='Each corner triangle is half of a 3 cm square.',
         sol='Square: 144 cm². Each triangle: half of 3 × 3 = 4.5 cm². Four triangles: 18 cm². Left: 144 − 18 = 126 cm².'),

    # ---------------- Part 6 · Data Handling
    dict(ch='8', scen='bar graph of favourite fruit · fraction choosing mango',
         fig=drawing(300, 200, bars([('Mango', 45), ('Apple', 30), ('Banana', 20), ('Grapes', 25)], 50, 5, 'Number of students')),
         stem='The bar graph shows the favourite fruit of every student in a school year. What fraction of these students chose mango?',
         opts=['3/8', '3/5', '9/20', '1/3'],
         hint='First find the total number of students.',
         sol='Total: 45 + 30 + 20 + 25 = 120. Mango: 45/120 = 3/8.'),

    # ---------------- Part 7 · Applied Mathematics
    dict(ch='9', scen='400 m track at 5 m/s for 10 minutes · full laps',
         stem='Arun runs round a 400 m track at a steady 5 metres per second. How many full laps does he complete in 10 minutes?',
         opts=['7', '8', '75', '6'],
         hint='Find the distance he runs in 10 minutes.',
         sol='10 minutes = 600 seconds. Distance: 600 × 5 = 3,000 m. 3,000 ÷ 400 = 7.5, so 7 full laps.'),
    dict(ch='9', scen='30 min at 16 km/h and 45 min at 12 km/h · average speed',
         stem='Ishani cycles for 30 minutes at 16 km/h and then for 45 minutes at 12 km/h. What is her average speed?',
         opts=['13.6 km/h', '14 km/h', '13 km/h', '14.4 km/h'],
         hint='Find each distance, then divide the total by the total time.',
         sol='First part: half an hour at 16 km/h = 8 km. Second: three quarters of an hour at 12 km/h = 9 km. Total 17 km in 1.25 h. 17 ÷ 1.25 = 68 ÷ 5 = 13.6 km/h.'),
    dict(ch='9', scen='machine making a toy every 45 seconds for 3 h 30 min',
         stem='A machine makes one toy every 45 seconds. How many toys does it make in 3 hours 30 minutes?',
         opts=['280', '210', '480', '300'],
         hint='How many toys does it make in 3 minutes?',
         sol='In 3 minutes (180 s) it makes 4 toys. 3 h 30 min = 210 minutes = 70 lots of 3 minutes. 70 × 4 = 280 toys.'),
    dict(ch='9', scen='bus tickets 2 adults at ₹37.50 and 3 children at ₹18.75',
         stem='A bus ticket costs ₹37.50 for an adult and ₹18.75 for a child. A family of 2 adults and 3 children pays with ₹200. How much change do they get?',
         opts=['₹68.75', '₹70.25', '₹78.75', '₹56.25'],
         hint='Work out the adult and child tickets separately.',
         sol='Adults: 2 × 37.50 = ₹75. Children: 3 × 18.75 = ₹56.25. Total ₹131.25. Change: 200 − 131.25 = ₹68.75.'),

    # ---------------- Part 8 · Mathematical Reasoning
    dict(ch='10', scen='multiply by 2 3 4 5 series',
         fig=cards([1, 2, 6, 24, 120, '?'], size=38),
         stem='Each number in Nandini\'s series is a multiple of the one before. Which number comes next?',
         opts=['720', '240', '600', '144'],
         hint='Look at what each number is multiplied by.',
         sol='The multipliers are 2, 3, 4 and 5: 1 × 2 = 2, 2 × 3 = 6, 6 × 4 = 24, 24 × 5 = 120. Next: 120 × 6 = 720.'),
    dict(ch='10', scen='31-day month with five Fridays Saturdays and Sundays',
         stem='A month has 31 days. It has five Fridays, five Saturdays and five Sundays. On which day of the week does the month begin?',
         opts=['Friday', 'Saturday', 'Thursday', 'Sunday'],
         hint='31 days = 4 weeks + 3 extra days.',
         sol='4 full weeks give every day four times. The 3 extra days are the first three days of the month, so they must be Friday, Saturday and Sunday. The month begins on a Friday.'),
    dict(ch='10', scen='handshakes among 7 friends · impossible pattern',
         stem='Seven friends meet. Each person shakes hands with some of the others. Which of these is impossible?',
         opts=['Each shakes hands with exactly 3 others', 'Each shakes hands with exactly 2 others', 'Each shakes hands with exactly 4 others', 'Each shakes hands with exactly 6 others'],
         hint='Each handshake is counted by two people.',
         sol='Adding up everyone\'s handshakes counts each handshake twice, so the total must be even. With 3 each: 7 × 3 = 21, which is odd, so it is impossible. 7 × 2 = 14, 7 × 4 = 28 and 7 × 6 = 42 are even, and those patterns can be made.'),
    dict(ch='10', scen='even numbers between 100 and 200 with all digits different',
         stem='How many even numbers between 100 and 200 have three different digits?',
         opts=['40', '45', '36', '50'],
         hint='The number is 1 _ _. The last digit must be even and not 1.',
         sol='The hundreds digit is 1. The ones digit is even: 0, 2, 4, 6 or 8 (5 choices). The tens digit can be any digit except 1 and the ones digit: 8 choices. 5 × 8 = 40.'),

    # ---------------- Section II · Star Questions
    dict(ch='1+10', scen='even square numbers from 1 to 100',
         stem='A square number is a number times itself, like 9 = 3 × 3. How many square numbers from 1 to 100 are even?',
         opts=['5', '10', '4', '6'],
         hint='An even number times itself is even; an odd number times itself is odd.',
         sol='The square numbers up to 100 are 1, 4, 9, …, 100 (from 1 × 1 to 10 × 10). The even ones come from 2, 4, 6, 8 and 10: 4, 16, 36, 64 and 100. That is 5.'),
    dict(ch='3+10', scen='series going up by 0.25 from 0.5 · position of 5',
         fig=cards(['0.5', '0.75', '1', '1.25', '…'], size=40),
         stem='The series goes up by the same amount each time. Which number in the series (1st, 2nd, …) is 5?',
         opts=['19th', '18th', '20th', '10th'],
         hint='How many steps of 0.25 take you from 0.5 to 5?',
         sol='From 0.5 to 5 is 4.5. Each step is 0.25, so there are 4.5 ÷ 0.25 = 18 steps. The 1st number plus 18 steps is the 19th number.'),
    dict(ch='6+10', scen='5-layer pyramid of unit cubes · volume',
         stem='Siddharth builds a pyramid of 1 cm cubes. The top layer is 1 by 1, the next 2 by 2, then 3 by 3, and so on. What is the volume of a pyramid with 5 layers?',
         opts=['55 cm³', '30 cm³', '25 cm³', '125 cm³'],
         hint='Add the cubes in each layer.',
         sol='Layers: 1 + 4 + 9 + 16 + 25 = 55 cubes. Each is 1 cm³, so 55 cm³.'),
    dict(ch='1+9', scen='lighthouses flashing every 15 and 20 seconds over 5 minutes',
         stem='Two lighthouses flash together at 8:00:00 PM. One flashes every 15 seconds and the other every 20 seconds. How many more times do they flash together up to 8:05:00 PM?',
         opts=['5', '6', '4', '20'],
         hint='Find the LCM of 15 and 20 seconds.',
         sol='LCM of 15 and 20 is 60 seconds. They flash together at the end of every minute: 8:01, 8:02, 8:03, 8:04 and 8:05. That is 5 more times.'),
    dict(ch='3+9', scen='3.6 km road at 0.45 km a day with Sundays off',
         stem='Workers build a road 3.6 km long. They build 0.45 km each working day and rest on Sundays. They start on Monday the 1st. On which day do they finish?',
         opts=['Tuesday the 9th', 'Monday the 8th', 'Wednesday the 10th', 'Tuesday the 8th'],
         hint='First find how many working days they need.',
         sol='3.6 ÷ 0.45 = 360 ÷ 45 = 8 working days. Monday 1st to Saturday 6th is 6 days. Sunday 7th is a rest day. Monday 8th and Tuesday 9th are days 7 and 8. They finish on Tuesday the 9th.'),
]
