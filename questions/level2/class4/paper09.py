# AMO Level-2 · Class 4 · Practice Paper 9  (format: see paper01.py)


def pict(rows, em, key, lw=90, step=28):
    prims = []
    for i, (lab, n) in enumerate(rows):
        y = 18 + i * 34
        prims += [('rect', 0, y - 15, lw, 30, 'lilac'), ('text', lw / 2, y, lab, 12)]
        prims += [('emoji', em, lw + 20 + k * step, y, 24) for k in range(n)]
    y = 18 + len(rows) * 34 + 6
    prims += [('emoji', em, 14, y, 20), ('text', 40 + len(key) * 3.6, y, '= ' + key, 12)]
    return prims


def tri_with_cevian():
    return [('poly', [(100, 10), (10, 120), (200, 120)], 'pink'), ('line', 100, 10, 140, 120),
            ('text', 100, 0, 'A', 13), ('text', 0, 130, 'B', 13), ('text', 140, 134, 'D', 13), ('text', 210, 130, 'C', 13)]


def box_sheet():
    s = 14
    P = lambda x, y: (10 + x * s, 10 + y * s)
    pts = [P(2, 0), P(8, 0), P(8, 2), P(10, 2), P(10, 6), P(8, 6), P(8, 8), P(2, 8), P(2, 6), P(0, 6), P(0, 2), P(2, 2)]
    return [('poly', pts, 'peach'), ('rect', *P(2, 2), 6 * s, 4 * s, 'yellow', True),
            ('text', *P(5, 8.8), '2 cm squares cut from the corners', 10)]


QUESTIONS = [
    # ---------------- Part 1 · Number System
    dict(ch='1', scen='whole numbers that round to 50,000 at the nearest thousand',
         stem='How many whole numbers become 50,000 when they are rounded to the nearest thousand?',
         opts=['1,000', '999', '500', '1,001'],
         hint='Find the smallest and the largest such number.',
         sol='The smallest is 49,500 and the largest is 50,499. From 49,500 to 50,499 there are 50,499 − 49,500 + 1 = 1,000 numbers.'),
    dict(ch='1', scen='swapping the first and last digits of 72,519',
         stem='Kiara swaps the first and last digits of 72,519. How much bigger is her new number than 72,519?',
         opts=['19,998', '20,000', '19,989', '20,002'],
         hint='The new number is 92,517.',
         sol='Swapping 7 and 9 gives 92,517. 92,517 − 72,519 = 19,998.'),
    dict(ch='1', scen='half of XCVI in Roman numerals',
         stem='Which Roman numeral is half of XCVI?',
         opts=['XLVIII', 'XLVI', 'LXVIII', 'XXXVIII'],
         hint='Change XCVI to a number first.',
         sol='XCVI = 90 + 6 = 96. Half of 96 is 48. 48 = 40 + 8 = XLVIII.'),

    # ---------------- Part 2 · Operations
    dict(ch='2', scen='3,600 sweets for 8 classes with 9 sections each',
         stem='A school shares 3,600 sweets equally among 8 classes. Each class shares its sweets equally among its 9 sections. How many sweets does each section get?',
         opts=['50', '450', '400', '45'],
         hint='Divide by 8 first, then by 9.',
         sol='3,600 ÷ 8 = 450 sweets for each class. 450 ÷ 9 = 50 sweets for each section.'),
    dict(ch='2', scen='adding 2,987 4,015 and 1,998 by rounding',
         stem='Jaya adds 2,987 + 4,015 + 1,998 in her head by first rounding each number to the nearest thousand. What is the exact sum?',
         opts=['9,000', '8,900', '9,100', '9,010'],
         hint='Round each number and keep track of the change.',
         sol='2,987 is 13 less than 3,000, 4,015 is 15 more than 4,000, and 1,998 is 2 less than 2,000. 3,000 + 4,000 + 2,000 = 9,000. The changes: −13 + 15 − 2 = 0. So the sum is exactly 9,000.'),
    dict(ch='2', scen='multiplied by 6 instead of adding 6',
         stem='Kunal should have added 6 to a number. By mistake, he multiplied the number by 6 and got 492. What is the correct answer?',
         opts=['88', '498', '82', '486'],
         hint='First find the number.',
         sol='The number × 6 = 492, so the number is 492 ÷ 6 = 82. The correct answer is 82 + 6 = 88.'),

    # ---------------- Part 3 · Fractions & Decimals
    dict(ch='3', scen='fraction equal to 2/3 whose top and bottom add up to 20',
         stem='Which fraction is equal to 2/3 and has a numerator and denominator that add up to 20?',
         opts=['8/12', '9/11', '6/9', '4/6'],
         hint='Fractions equal to 2/3: 2/3, 4/6, 6/9, 8/12, … Check the sums.',
         sol='2/3 has sum 5. 4/6 has sum 10. 6/9 has sum 15. 8/12 has sum 20. 9/11 adds to 20 but is not equal to 2/3.'),
    dict(ch='3', scen='wall painted over three days · fraction left',
         stem='Rani paints 1/4 of a wall on Monday, 1/3 of it on Tuesday and 1/6 of it on Wednesday. What fraction of the wall is still not painted?',
         opts=['1/4', '3/4', '1/12', '5/12'],
         hint='Change all three fractions to twelfths.',
         sol='1/4 + 1/3 + 1/6 = 3/12 + 4/12 + 2/12 = 9/12. Not painted: 12/12 − 9/12 = 3/12 = 1/4.'),
    dict(ch='3', scen='pencil worn down over two weeks',
         stem='A new pencil is 12.5 cm long. Arnav uses 3.8 cm of it in the first week and 2.9 cm in the second week. How long is it now?',
         opts=['5.8 cm', '6.7 cm', '6.2 cm', '5.2 cm'],
         hint='Add the two lengths used.',
         sol='Used: 3.8 + 2.9 = 6.7 cm. Left: 12.5 − 6.7 = 5.8 cm.'),
    dict(ch='3', scen='which is not equal to 2 3/4',
         stem='Which of these is NOT equal to 2 3/4?',
         opts=['2 3/8', '11/4', '2 6/8', '2 9/12'],
         hint='Write each one as a mixed number with quarters.',
         sol='11/4 = 2 3/4. 2 6/8 = 2 3/4. 2 9/12 = 2 3/4. But 2 3/8 is less than 2 3/4, because 3/8 is less than 6/8.'),

    # ---------------- Part 4 · Geometry
    dict(ch='5', scen='pyramid with 10 faces · number of edges',
         stem='A pyramid has 10 faces. How many edges does it have?',
         opts=['18', '20', '10', '16'],
         hint='One face is the base. The others are triangles, one for each side of the base.',
         sol='10 faces = 1 base + 9 triangles, so the base has 9 sides. Edges: 9 on the base + 9 slanting = 18. Check: vertices 10, and 10 + 10 − 18 = 2.'),
    dict(ch='5', scen='segments in a triangle with one line from the top to the base',
         fig=drawing(210, 135, tri_with_cevian()),
         stem='Point D is on side BC. How many different line segments are there in this picture?',
         opts=['6', '4', '5', '7'],
         hint='Do not forget BD, DC and the whole of BC.',
         sol='From A: AB, AD, AC (3). On the base: BD, DC and BC (3). 3 + 3 = 6.'),
    dict(ch='5', scen='edges meeting at each vertex of a square pyramid · total',
         stem='At each vertex of a square pyramid, Om counts how many edges meet there. Then he adds up all his counts. What total does he get?',
         opts=['16', '8', '13', '20'],
         hint='Count at the top point and at each corner of the base.',
         sol='At the top point 4 edges meet. At each of the 4 base corners 3 edges meet. 4 + 4 × 3 = 16. This is twice the 8 edges, because each edge has two ends.'),

    # ---------------- Part 5 · Mensuration
    dict(ch='6', scen='1 m path inside the edge of a 20 m square garden',
         stem='A square garden has sides of 20 m. A path 1 m wide runs along the inside of all four sides. What is the area of the path?',
         opts=['76 m²', '80 m²', '84 m²', '324 m²'],
         hint='The part inside the path is a square with sides of 18 m.',
         sol='Whole garden: 20 × 20 = 400 m². Inside the path: 18 × 18 = 324 m². Path: 400 − 324 = 76 m².'),
    dict(ch='6', scen='9 cm by 4 cm rectangle and the square with the same area',
         stem='A square has the same area as a rectangle 9 cm long and 4 cm wide. How much shorter is the perimeter of the square?',
         opts=['2 cm', '0 cm', '4 cm', '10 cm'],
         hint='Which square has an area of 36 cm²?',
         sol='Area = 9 × 4 = 36 cm², so the square has side 6 cm and perimeter 24 cm. The rectangle\'s perimeter is 2 × (9 + 4) = 26 cm. 26 − 24 = 2 cm.'),
    dict(ch='6', scen='4 L 500 mL of juice into 750 mL bottles',
         stem='Lalit pours 4 L 500 mL of juice into bottles that each hold 750 mL. How many bottles can he fill completely?',
         opts=['6', '5', '7', '60'],
         hint='Add 750 mL again and again: 750, 1,500, …',
         sol='4 L 500 mL = 4,500 mL. 750 × 6 = 4,500 mL. So 6 bottles.'),
    dict(ch='6', scen='fence posts every 4 m round a 20 m by 12 m field',
         stem='A field is 20 m long and 12 m wide. Posts are put all round its edge, 4 m apart, with a post at each corner. How many posts are there?',
         opts=['16', '17', '18', '20'],
         hint='Going all the way round, the last gap ends at the first post.',
         sol='Perimeter = 2 × (20 + 12) = 64 m. There are 64 ÷ 4 = 16 gaps. On a closed path the number of posts equals the number of gaps, so 16 posts.'),

    # ---------------- Part 6 · Data Handling
    dict(ch='8', scen='pictograph of cookies sold · packets of 3',
         fig=drawing(320, 125, pict([('Monday', 4), ('Tuesday', 7), ('Wednesday', 5)], '🍪', '6 cookies')),
         stem='The pictograph shows cookies sold by a bakery. The cookies were sold in packets of 3. How many packets were sold on the three days?',
         opts=['32', '16', '96', '48'],
         hint='Find the number of cookies first.',
         sol='Symbols: 4 + 7 + 5 = 16. Cookies: 16 × 6 = 96. Packets: 96 ÷ 3 = 32.'),

    # ---------------- Part 7 · Applied Mathematics
    dict(ch='9', scen='clock losing 2 minutes an hour shows 5:36 PM',
         stem='Hemant\'s clock loses 2 minutes every hour. He sets it right at 6:00 AM. Later the clock shows 5:36 PM. What is the real time?',
         opts=['6:00 PM', '5:12 PM', '5:58 PM', '6:24 PM'],
         hint='In each real hour, the clock moves only 58 minutes.',
         sol='The clock has moved 11 h 36 min = 696 minutes. Each real hour the clock moves 58 minutes. 58 × 12 = 696, so 12 real hours have passed. 6:00 AM + 12 h = 6:00 PM.'),
    dict(ch='9', scen='date of the third Friday when the 1st is Wednesday',
         stem='The 1st of a month is a Wednesday. On which date is the third Friday of that month?',
         opts=['17th', '15th', '24th', '10th'],
         hint='Find the date of the first Friday.',
         sol='The first Friday is the 3rd. The others come every 7 days: 10th, 17th. So the third Friday is the 17th.'),
    dict(ch='9', scen='rice and dal paid for with ₹500',
         stem='Rice costs ₹48 per kg and dal costs ₹115 per kg. Neelam buys 3 kg of rice and 2 kg of dal and pays with ₹500. How much change does she get?',
         opts=['₹126', '₹337', '₹374', '₹226'],
         hint='Find the cost of rice and of dal separately.',
         sol='Rice: 3 × 48 = ₹144. Dal: 2 × 115 = ₹230. Total: ₹374. Change: 500 − 374 = ₹126.'),

    # ---------------- Part 8 · Mathematical Reasoning
    dict(ch='10', scen='series 5 6 8 11 15 20',
         fig=cards([5, 6, 8, 11, 15, 20, '?'], size=38),
         stem='Pari\'s series adds a little more each time. Which number comes next?',
         opts=['26', '25', '27', '30'],
         hint='The amounts added are 1, 2, 3, …',
         sol='The series adds 1, 2, 3, 4, 5. Next it adds 6: 20 + 6 = 26.'),
    dict(ch='10', scen='even 3-digit numbers from 1 2 3 4 without repeating',
         stem='Akash makes 3-digit numbers from the digits 1, 2, 3 and 4, using no digit twice in a number. How many of his numbers are even?',
         opts=['12', '24', '6', '8'],
         hint='The last digit must be 2 or 4.',
         sol='Last digit: 2 choices (2 or 4). Hundreds digit: 3 choices left. Tens digit: 2 choices left. 2 × 3 × 2 = 12.'),
    dict(ch='10', scen='finishing order in a race from clues',
         stem='In a race, Isha finished ahead of Kabir but behind Tara. Neel finished just after Kabir. Om finished last. Who finished 3rd?',
         opts=['Kabir', 'Isha', 'Neel', 'Tara'],
         hint='Start with Tara, Isha and Kabir in order.',
         sol='Tara, then Isha, then Kabir. Neel is just after Kabir and Om is last: Tara, Isha, Kabir, Neel, Om. Kabir is 3rd.'),
    dict(ch='10', scen='mangoes given as half plus one twice · 2 left',
         stem='Suresh gives half of his mangoes and 1 more to his first friend. Then he gives half of the rest and 1 more to his second friend. He has 2 mangoes left. How many did he have at the start?',
         opts=['14', '10', '12', '16'],
         hint='Work backwards. Before the second friend he had (2 + 1) × 2.',
         sol='Before the second friend: (2 + 1) × 2 = 6. Before the first friend: (6 + 1) × 2 = 14. Check: 14 → gives 7 + 1 = 8, leaving 6 → gives 3 + 1 = 4, leaving 2.'),

    # ---------------- Section II · Star Questions
    dict(ch='3+10', scen='two twelfths fractions with sum 1 and difference 1/6',
         stem='Two fractions with denominator 12 add up to 1. Their difference is 1/6. What is the larger fraction?',
         opts=['7/12', '5/12', '2/3', '1/2'],
         hint='Their numerators add up to 12 and differ by 2.',
         sol='1 = 12/12 and 1/6 = 2/12. Two numbers that add to 12 and differ by 2 are 7 and 5. The larger fraction is 7/12.'),
    dict(ch='9+10', scen='birthday 47 days after Holi on Wednesday 8 March',
         stem='Holi is on Wednesday, 8 March. Ravi\'s birthday is 47 days after Holi. On which date and day is his birthday?',
         opts=['24 April, Monday', '24 April, Tuesday', '25 April, Monday', '23 April, Sunday'],
         hint='March has 31 days. 47 days is 6 weeks and 5 days.',
         sol='8 March + 23 days = 31 March. 24 more days reach 24 April. 47 = 6 × 7 + 5, and 5 days after Wednesday is Monday. So 24 April, Monday.'),
    dict(ch='1+10', scen='numbers 1 to 1,000 with only even digits',
         stem='How many numbers from 1 to 1,000 are written using only even digits (0, 2, 4, 6, 8)?',
         opts=['124', '125', '100', '120'],
         hint='Count 1-digit, 2-digit and 3-digit numbers separately. The first digit cannot be 0.',
         sol='1-digit: 2, 4, 6, 8 (4). 2-digit: 4 choices for tens × 5 for ones = 20. 3-digit: 4 × 5 × 5 = 100. 1,000 has a 1. 4 + 20 + 100 = 124.'),
    dict(ch='3+9', scen='film of 2 1/4 hours with a 15-minute interval',
         stem='A film runs for 2 1/4 hours, plus a 15-minute interval. The show starts at 5:50 PM. At what time does it end?',
         opts=['8:20 PM', '8:05 PM', '8:15 PM', '7:55 PM'],
         hint='2 1/4 hours is 2 hours 15 minutes.',
         sol='2 1/4 hours = 2 h 15 min. With the interval: 2 h 30 min. 5:50 PM + 2 h 30 min = 8:20 PM.'),
    dict(ch='5+6', scen='open box from a sheet with corner squares cut · area of the side walls',
         fig=drawing(160, 140, box_sheet()),
         stem='A 10 cm by 8 cm sheet has a 2 cm square cut from each corner. The flaps are folded up to make an open box. What is the total area of the four side walls?',
         opts=['40 cm²', '64 cm²', '24 cm²', '80 cm²'],
         hint='Find the area left after cutting, then take away the base.',
         sol='Sheet: 10 × 8 = 80 cm². Corners cut: 4 × 4 = 16 cm², leaving 64 cm². The base is (10 − 4) × (8 − 4) = 6 × 4 = 24 cm². Side walls: 64 − 24 = 40 cm².'),
]
