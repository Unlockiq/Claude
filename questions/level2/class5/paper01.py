# AMO Level-2 · Class 5 · Practice Paper 1
# Each question: ch (chapter or star pair), scen (unique scenario key), stem, opts (correct answer FIRST),
# hint, sol, optional fig. fixed=True keeps the option order, with ans = index of the correct option.


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


def card_cut():
    return [('poly', [(10, 10), (130, 10), (130, 90), (70, 90), (10, 50)], 'yellow'),
            ('poly', [(10, 50), (70, 90), (10, 90)], 'white', True),
            ('text', 70, 2, '12 cm', 11), ('text', 146, 50, '8 cm', 11), ('text', 40, 102, '6 cm', 10), ('text', -6, 70, '4 cm', 10)]


QUESTIONS = [
    # ---------------- Part 1 · Number System
    dict(ch='1', scen='smallest 6-digit number with different digits minus largest 5-digit number with different digits',
         stem='Vikram writes the smallest 6-digit number whose digits are all different. Sana writes the largest 5-digit number whose digits are all different. What is the difference between their numbers?',
         opts=['3,580', '3,480', '3,590', '4,580'],
         hint='The smallest 6-digit number with different digits starts 1, 0, 2, …',
         sol='Smallest 6-digit number with different digits: 1,02,345. Largest 5-digit number with different digits: 98,765. 1,02,345 − 98,765 = 3,580.'),
    dict(ch='1', scen='two bells every 12 and 18 minutes · times together from 9 to 12',
         stem='Two school bells ring together at 9:00 AM. One rings every 12 minutes and the other every 18 minutes. How many times do they ring together from 9:00 AM to 12:00 noon, counting both?',
         opts=['6', '5', '7', '4'],
         hint='Find the LCM of 12 and 18.',
         sol='LCM of 12 and 18 is 36, so they ring together every 36 minutes: 9:00, 9:36, 10:12, 10:48, 11:24 and 12:00. That is 6 times.'),
    dict(ch='1', scen='Roman numeral for MCMXLIV minus CDXCIX',
         stem='Ayaan subtracts CDXCIX from MCMXLIV. Which Roman numeral is the answer?',
         opts=['MCDXLV', 'MCDLXV', 'MCDXXXV', 'MDXLV'],
         hint='Change both numerals into ordinary numbers first.',
         sol='MCMXLIV = 1000 + 900 + 40 + 4 = 1944. CDXCIX = 400 + 90 + 9 = 499. 1944 − 499 = 1445 = M + CD + XL + V = MCDXLV.'),

    # ---------------- Part 2 · Operations
    dict(ch='2', scen='BODMAS 120 minus bracket 36 divided by 4 plus 2 times 5 plus 8',
         fig=equations([['120 − [36 ÷ (4 + 2) × 5] + 8', '=', '?']], size=28),
         stem='Pallavi works out this expression using the correct order of operations. What answer does she get?',
         opts=['98', '82', '123', '114'],
         hint='Work out the small bracket first, then the square bracket.',
         sol='4 + 2 = 6. Inside the square bracket: 36 ÷ 6 = 6 and 6 × 5 = 30. Then 120 − 30 + 8 = 98. (82 wrongly takes away 30 + 8.)'),
    dict(ch='2', scen='estimate 487 times 31 by rounding to tens · error',
         stem='Mohan estimates 487 × 31 by rounding both numbers to the nearest ten. By how much is his estimate less than the exact answer?',
         opts=['397', '403', '297', '497'],
         hint='Estimate: 490 × 30. Exact: 487 × 30 + 487.',
         sol='Estimate: 490 × 30 = 14,700. Exact: 487 × 31 = 487 × 30 + 487 = 14,610 + 487 = 15,097. Difference: 15,097 − 14,700 = 397.'),
    dict(ch='2', scen='125 times 37 times 8 minus 25 times 37 times 4 using properties',
         stem='Without long multiplication, Divya works out 125 × 37 × 8 − 25 × 37 × 4. What is the answer?',
         opts=['33,300', '33,700', '29,600', '37,000'],
         hint='Group 125 × 8 and 25 × 4 first.',
         sol='125 × 8 = 1,000, so the first part is 37 × 1,000 = 37,000. 25 × 4 = 100, so the second part is 3,700. 37,000 − 3,700 = 33,300.'),

    # ---------------- Part 3 · Fractions, Decimals & Percentages
    dict(ch='3', scen='840 students · 25 percent walk one third by bus rest by van',
         stem='A school has 840 students. 25% of them walk to school and 1/3 of them come by bus. The rest come by van. How many come by van?',
         opts=['350', '490', '280', '420'],
         hint='25% is the same as 1/4.',
         sol='25% of 840 = 840 ÷ 4 = 210. 1/3 of 840 = 280. 210 + 280 = 490. By van: 840 − 490 = 350.'),
    dict(ch='3', scen='second largest of 3/8 0.4 7/20 0.38',
         stem='Which is the 2nd largest of these: 3/8, 0.4, 7/20, 0.38?',
         opts=['0.38', '0.4', '3/8', '7/20'],
         hint='Change the fractions into decimals.',
         sol='3/8 = 0.375 and 7/20 = 0.35. In order from largest: 0.4, 0.38, 0.375, 0.35. The 2nd largest is 0.38.'),
    dict(ch='3', scen='7.5 m ribbon cut into 0.25 m pieces with 4 spoiled',
         stem='Kavya cuts a ribbon 7.5 m long into pieces of 0.25 m each. 4 pieces get spoiled. How many good pieces does she have?',
         opts=['26', '30', '34', '186'],
         hint='0.25 m is a quarter of a metre.',
         sol='Each metre gives 4 pieces of 0.25 m, so 7.5 m gives 7.5 × 4 = 30 pieces. 30 − 4 = 26 good pieces.'),
    dict(ch='3', scen='1,200 L tank 75 percent full · 20 percent of capacity used',
         stem='A water tank can hold 1,200 L. It is 75% full. Ravi then uses an amount equal to 20% of the full tank. How many litres are left in the tank?',
         opts=['660', '720', '540', '700'],
         hint='Find 75% of 1,200 and 20% of 1,200.',
         sol='75% of 1,200 = 3/4 × 1,200 = 900 L. 20% of 1,200 = 1/5 × 1,200 = 240 L. Left: 900 − 240 = 660 L.'),

    # ---------------- Part 4 · Geometry
    dict(ch='5', scen='right triangle with one acute angle twice the other',
         stem='A triangle has one right angle. One of its other angles is twice the third angle. What is the smallest angle of the triangle?',
         opts=['30°', '45°', '60°', '15°'],
         hint='The angles of a triangle add up to 180°.',
         sol='The other two angles add up to 180° − 90° = 90°. One is twice the other, so together they are 3 equal parts: 90° ÷ 3 = 30°. The angles are 90°, 60° and 30°.'),
    dict(ch='5', scen='sum of orders of rotational symmetry of four shapes',
         stem='Ishita adds the orders of rotational symmetry of a square, an equilateral triangle, a rectangle that is not a square and a regular hexagon. What total does she get?',
         opts=['15', '13', '17', '11'],
         hint='Count how many times each shape looks the same in one full turn.',
         sol='Square: 4. Equilateral triangle: 3. Rectangle (not a square): 2. Regular hexagon: 6. 4 + 3 + 2 + 6 = 15.'),
    dict(ch='5', scen='facing north then three turns',
         stem='Arjun faces North. He turns 90° clockwise, then 180° clockwise, then 270° anticlockwise. Which direction does he face now?',
         opts=['North', 'South', 'East', 'West'],
         hint='Follow each turn one at a time.',
         sol='90° clockwise from North: East. 180° more: West. 270° anticlockwise from West: South (90°), East (180°), North (270°). He faces North.'),

    # ---------------- Part 5 · Mensuration
    dict(ch='6', scen='half-full cuboid tank 50 by 40 by 30 cm in litres',
         stem='A fish tank is a cuboid 50 cm long, 40 cm wide and 30 cm high. It is half full of water. How many 1-litre bottles of water are in it? (1 L = 1,000 cm³)',
         opts=['30', '60', '600', '300'],
         hint='Find the volume of the full tank first.',
         sol='Full tank: 50 × 40 × 30 = 60,000 cm³ = 60 L. Half full: 30 L, which is 30 bottles.'),
    dict(ch='6', scen='rectangular card with a right triangle cut from a corner',
         fig=drawing(150, 105, card_cut()),
         stem='Riya cuts a right-angled triangle with sides 6 cm and 4 cm from a corner of a 12 cm by 8 cm card, as shown. What is the area of the card left?',
         opts=['84 cm²', '72 cm²', '90 cm²', '60 cm²'],
         hint='The area of a right-angled triangle is half of the rectangle around it.',
         sol='Card: 12 × 8 = 96 cm². Triangle: half of 6 × 4 = 12 cm². Left: 96 − 12 = 84 cm².'),
    dict(ch='6', scen='2 m path inside a 20 m square garden',
         stem='A square garden has sides of 20 m. A path 2 m wide runs inside the garden along all four sides. What is the area of the path?',
         opts=['144 m²', '160 m²', '80 m²', '156 m²'],
         hint='Take the inner square away from the whole garden.',
         sol='Whole garden: 20 × 20 = 400 m². The inner square has side 20 − 2 − 2 = 16 m: 16 × 16 = 256 m². Path: 400 − 256 = 144 m². (160 counts the 4 corner squares twice.)'),

    # ---------------- Part 6 · Data Handling
    dict(ch='8', scen='bar graph of books read · top two minus bottom two',
         fig=drawing(330, 200, bars([('Arnav', 12), ('Bela', 18), ('Chirag', 9), ('Disha', 15), ('Esha', 21)], 24, 3, 'Books read')),
         stem='The bar graph shows the books read by five children. How many more books did the two top readers read than the two children who read the least?',
         opts=['18', '12', '21', '15'],
         hint='Read each bar against the scale.',
         sol='Esha 21 and Bela 18 read the most: 39. Chirag 9 and Arnav 12 read the least: 21. 39 − 21 = 18.'),

    # ---------------- Part 7 · Applied Mathematics
    dict(ch='9', scen='train 180 km in 2 h 30 min · distance in 4 hours',
         stem='A train covers 180 km in 2 hours 30 minutes at a steady speed. How far does it go in 4 hours at the same speed?',
         opts=['288 km', '360 km', '300 km', '270 km'],
         hint='Find the distance covered in 30 minutes first.',
         sol='2 h 30 min is 5 half-hours, so it covers 180 ÷ 5 = 36 km each half-hour, which is 72 km/h. In 4 hours: 72 × 4 = 288 km.'),
    dict(ch='9', scen='12 km at 12 km/h then 12 km at 6 km/h · average speed',
         stem='Neha cycles 12 km at 12 km/h and then another 12 km at 6 km/h. What is her average speed for the whole ride?',
         opts=['8 km/h', '9 km/h', '18 km/h', '6 km/h'],
         hint='Average speed = total distance ÷ total time.',
         sol='First part: 1 hour. Second part: 12 ÷ 6 = 2 hours. Total: 24 km in 3 hours, so 24 ÷ 3 = 8 km/h. (9 km/h wrongly averages the two speeds.)'),
    dict(ch='9', scen='film from 6:50 PM lasting 2.75 hours',
         stem='A film starts at 6:50 PM and lasts 2.75 hours. At what time does it end?',
         opts=['9:35 PM', '9:15 PM', '9:25 PM', '8:35 PM'],
         hint='0.75 hour is three quarters of an hour.',
         sol='2.75 hours = 2 hours 45 minutes. 6:50 PM + 2 hours = 8:50 PM. 8:50 + 45 minutes = 9:35 PM.'),
    dict(ch='9', scen='2 pens at ₹18.50 and 3 notebooks at ₹42.75 paid with ₹200',
         stem='A pen costs ₹18.50 and a notebook costs ₹42.75. Simran buys 2 pens and 3 notebooks and pays with ₹200. How much change does she get?',
         opts=['₹34.75', '₹35.25', '₹38.75', '₹44.75'],
         hint='Find the cost of the pens and the notebooks separately.',
         sol='Pens: 2 × 18.50 = ₹37.00. Notebooks: 3 × 42.75 = ₹128.25. Total: ₹165.25. Change: 200 − 165.25 = ₹34.75.'),

    # ---------------- Part 8 · Mathematical Reasoning
    dict(ch='10', scen='series times 3 plus 1 from 1',
         fig=cards([1, 4, 13, 40, '?'], size=40),
         stem='Each number in Rohit\'s series comes from the one before by the same two steps. Which number comes next?',
         opts=['121', '120', '124', '160'],
         hint='Multiply by something, then add something.',
         sol='1 × 3 + 1 = 4, 4 × 3 + 1 = 13, 13 × 3 + 1 = 40. Next: 40 × 3 + 1 = 121.'),
    dict(ch='10', scen='15 August 2025 Friday · day of 15 August 2026',
         stem='Independence Day, 15 August, falls on a Friday in 2025. On which day of the week does it fall in 2026?',
         opts=['Saturday', 'Friday', 'Sunday', 'Thursday'],
         hint='Is there a 29 February between the two dates?',
         sol='From 15 August 2025 to 15 August 2026 there are 365 days, because February 2026 has 28 days. 365 = 52 weeks + 1 day, so the day moves on by 1: Saturday.'),
    dict(ch='10', scen='9 different odd numbers plus 6 different even numbers · possible total',
         stem='Kunal adds 9 different odd numbers. Priya adds 6 different even numbers. Which of these could be the total of both their sums together?',
         opts=['175', '150', '200', '64'],
         hint='Is the sum of 9 odd numbers odd or even?',
         sol='9 odd numbers make an odd total; 6 even numbers make an even total. Odd + even is odd, so the total must be odd. Only 175 is odd. (It is also large enough: the smallest possible total is 81 + 42 = 123.)'),
    dict(ch='10', scen='3-digit numbers whose digits add up to 5',
         stem='How many 3-digit numbers have digits that add up to 5?',
         opts=['15', '21', '10', '12'],
         hint='Fix the hundreds digit and count the choices for the other two digits.',
         sol='Hundreds digit 1: the other two add to 4, giving 5 numbers (104, 113, 122, 131, 140). Hundreds 2: 4 numbers. 3: 3. 4: 2. 5: 1 (500). 5 + 4 + 3 + 2 + 1 = 15.'),

    # ---------------- Section II · Star Questions
    dict(ch='1+10', scen='sum of the primes between 40 and 60',
         stem='Gaurav lists all the prime numbers between 40 and 60 and adds them. What total does he get?',
         opts=['243', '196', '290', '236'],
         hint='Test each odd number from 41 to 59 for factors 3 and 7.',
         sol='The primes are 41, 43, 47, 53 and 59 (45, 49, 51, 55 and 57 have other factors). 41 + 43 + 47 + 53 + 59 = 243.'),
    dict(ch='3+10', scen='decimal series adding 1.3 · tenth term',
         fig=cards(['1.2', '2.5', '3.8', '5.1', '…'], size=40),
         stem='The series goes up by the same amount each time. What is the 10th number in the series?',
         opts=['12.9', '14.2', '13.0', '11.6'],
         hint='From the 1st to the 10th number there are 9 steps.',
         sol='Each step adds 1.3. From the 1st number to the 10th there are 9 steps: 9 × 1.3 = 11.7. 1.2 + 11.7 = 12.9.'),
    dict(ch='6+10', scen='4 by 4 by 4 painted cube · small cubes with one painted face',
         stem='A big cube is painted on all its faces and then cut into 64 equal small cubes, 4 along each edge. How many small cubes have exactly one painted face?',
         opts=['24', '8', '16', '36'],
         hint='Look at the middle part of each face of the big cube.',
         sol='On each face, the small cubes not on an edge form a 2 by 2 square: 4 cubes with one painted face. 6 faces × 4 = 24.'),
    dict(ch='1+9', scen='buses every 40 and 60 minutes · meetings from 6 AM to 6 PM',
         stem='Two buses leave a depot together at 6:00 AM. One returns to the depot every 40 minutes, the other every 60 minutes. How many times are they at the depot together from 6:00 AM to 6:00 PM, counting both?',
         opts=['7', '6', '12', '13'],
         hint='Find the LCM of 40 and 60 minutes.',
         sol='LCM of 40 and 60 is 120 minutes = 2 hours. They meet at 6, 8, 10, 12, 2, 4 and 6 o\'clock: 7 times.'),
    dict(ch='3+9', scen='car 15 km per litre petrol ₹104.50 · cost of 255 km trip',
         stem='A car goes 15 km on 1 litre of petrol. Petrol costs ₹104.50 per litre. How much does the petrol cost for a 255 km trip?',
         opts=['₹1,776.50', '₹1,672.00', '₹1,766.50', '₹1,881.00'],
         hint='First find how many litres the trip needs.',
         sol='Litres: 255 ÷ 15 = 17. Cost: 17 × 104.50. 17 × 100 = 1,700 and 17 × 4.50 = 76.50, so the cost is ₹1,776.50.'),
]
