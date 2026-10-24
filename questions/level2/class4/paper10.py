# AMO Level-2 · Class 4 · Practice Paper 10  (format: see paper01.py)


def pict(rows, em, key, lw=90, step=28):
    prims = []
    for i, (lab, n) in enumerate(rows):
        y = 18 + i * 34
        prims += [('rect', 0, y - 15, lw, 30, 'lilac'), ('text', lw / 2, y, lab, 12)]
        prims += [('emoji', em, lw + 20 + k * step, y, 24) for k in range(n)]
    y = 18 + len(rows) * 34 + 6
    prims += [('emoji', em, 14, y, 20), ('text', 40 + len(key) * 3.6, y, '= ' + key, 12)]
    return prims


DIE_NET = [[None, '3', None, None], ['2', '1', '5', '?'], [None, '4', None, None]]


def rect_with_square():
    s = 12
    P = lambda x, y: (10 + x * s, 10 + y * s)
    return [('poly', [P(0, 3), P(4, 3), P(4, 0), P(7, 0), P(7, 3), P(12, 3), P(12, 8), P(0, 8)], 'blue'),
            ('line', *P(4, 3), *P(7, 3), True), ('text', *P(6, 9), '12 cm', 11), ('text', *P(-1.6, 5.5), '5 cm', 11),
            ('text', *P(5.5, -0.8), '3 cm', 11)]


def views():
    s = 26
    prims = [('text', 26, 0, 'Top view', 11), ('text', 136, 0, 'Front view', 11)]
    for r in range(2):
        for c in range(2):
            prims.append(('rect', c * s, 12 + r * s, s, s, 'yellow'))
    for r, c in [(0, 0), (1, 0), (1, 1)]:
        prims.append(('rect', 110 + c * s, 12 + r * s, s, s, 'blue'))
    return prims


QUESTIONS = [
    # ---------------- Part 1 · Number System
    dict(ch='1', scen='5-digit numbers whose digits add up to 44',
         stem='How many 5-digit numbers have digits that add up to 44?',
         opts=['5', '1', '4', '9'],
         hint='The largest possible digit sum is 45. Which digit must be one less than 9?',
         sol='Five 9s make 45, so exactly one digit is 8 and the others are 9. The 8 can be in any of the 5 places: 89,999, 98,999, 99,899, 99,989, 99,998. That is 5 numbers.'),
    dict(ch='1', scen='hidden tens digit making 63,4?8 closest to 63,500',
         stem='Gita\'s number is 63,4?8, with the tens digit hidden. The number is as close to 63,500 as it can be. What is the hidden digit?',
         opts=['9', '5', '0', '8'],
         hint='The number is always less than 63,500. Make it as big as possible.',
         sol='63,4?8 is at most 63,498, which is less than 63,500. The biggest choice is 63,498, just 2 away from 63,500. So the hidden digit is 9.'),
    dict(ch='1', scen='LXXIV minus XXIX in Roman numerals',
         stem='Bharat works out LXXIV − XXIX. Which Roman numeral is his answer?',
         opts=['XLV', 'LV', 'XLIV', 'XXXV'],
         hint='LXXIV = 74 and XXIX = 29.',
         sol='74 − 29 = 45. 45 = 40 + 5 = XLV.'),

    # ---------------- Part 2 · Operations
    dict(ch='2', scen='2,016 bottles in crates of 6 loaded 9 crates per truck',
         stem='A factory packs 2,016 bottles into crates of 6. A truck can carry 9 crates. How many trucks are needed to carry all the crates?',
         opts=['38', '37', '336', '224'],
         hint='Find the number of crates first.',
         sol='2,016 ÷ 6 = 336 crates. 336 ÷ 9 = 37 remainder 3. 37 trucks carry 333 crates and 3 crates need one more truck: 38 trucks.'),
    dict(ch='2', scen='37 times 99 plus 37',
         stem='Leena works out 37 × 99 + 37 in her head. What is the answer?',
         opts=['3,700', '3,663', '3,737', '3,600'],
         hint='37 × 99 + 37 × 1 = 37 × (99 + 1).',
         sol='37 × 99 + 37 = 37 × 99 + 37 × 1 = 37 × 100 = 3,700.'),
    dict(ch='2', scen='three numbers in a row with product 120 · their sum',
         stem='Three numbers that come one after another multiply to give 120. What is their sum?',
         opts=['15', '12', '18', '120'],
         hint='Try 3 × 4 × 5 and then the next three numbers.',
         sol='3 × 4 × 5 = 60 is too small. 4 × 5 × 6 = 120. Their sum is 4 + 5 + 6 = 15.'),

    # ---------------- Part 3 · Fractions & Decimals
    dict(ch='3', scen='largest of 7/4 5/3 11/6 3/2',
         stem='Which of these is the largest: 7/4, 5/3, 11/6, 3/2?',
         opts=['11/6', '7/4', '5/3', '3/2'],
         hint='Each is 1 and a bit. Compare how far each is from 2.',
         sol='7/4 is 1/4 less than 2. 5/3 is 1/3 less than 2. 11/6 is 1/6 less than 2. 3/2 is 1/2 less than 2. The smallest gap is 1/6, so 11/6 is the largest.'),
    dict(ch='3', scen='₹960 shared as 3/8 and 5/12 with the rest given away',
         stem='Riya gets 3/8 of ₹960 and Sohan gets 5/12 of it. The rest is given to a school. How much does the school get?',
         opts=['₹200', '₹760', '₹360', ['₹400'][0] if False else '₹240'],
         hint='Find 3/8 of 960 and 5/12 of 960.',
         sol='1/8 of 960 = 120, so 3/8 = ₹360. 1/12 of 960 = 80, so 5/12 = ₹400. 360 + 400 = 760. The school gets 960 − 760 = ₹200.'),
    dict(ch='3', scen='pole partly in the ground and partly under snow',
         stem='A pole is 6.4 m long. 1.5 m of it is in the ground and the bottom 0.8 m above the ground is covered by snow. How much of the pole can be seen above the snow?',
         opts=['4.1 m', '4.9 m', '5.6 m', '3.1 m'],
         hint='Take away both parts that cannot be seen.',
         sol='Hidden: 1.5 + 0.8 = 2.3 m. Seen: 6.4 − 2.3 = 4.1 m.'),
    dict(ch='3', scen='jug with 2/3 L and 3/4 L added and 5/6 L poured out',
         stem='Pallavi pours 2/3 L and then 3/4 L of milk into an empty jug. Then she pours out 5/6 L. How much milk is in the jug?',
         opts=['7/12 L', '5/12 L', '0 L', '1 5/12 L'],
         hint='Write all three fractions as twelfths.',
         sol='2/3 = 8/12, 3/4 = 9/12 and 5/6 = 10/12. 8/12 + 9/12 − 10/12 = 7/12 L.'),

    # ---------------- Part 4 · Geometry
    dict(ch='5', scen='missing number on a dice net where opposite faces add to 7',
         fig=grid(DIE_NET, cell=40),
         stem='This net folds into a dice. On a dice, opposite faces add up to 7. Which number goes in the square with the question mark?',
         opts=['6', '4', '3', '2'],
         hint='Find which face is opposite the question mark.',
         sol='In the row 2, 1, 5, ?, faces with one square between them are opposite: 2 and 5, and 1 and ?. 3 and 4 are opposite as well. 1 + ? = 7, so the missing number is 6.'),
    dict(ch='5', scen='edges of the cuboid made by gluing two cubes',
         stem='Two equal cubes are glued face to face to make a cuboid. How many edges does the cuboid have?',
         opts=['12', '24', '20', '16'],
         hint='Look at the new solid, not the two cubes.',
         sol='The new solid is a cuboid, and every cuboid has 12 edges. The edges of the glued faces are now inside a flat face, or join to make one long edge.'),
    dict(ch='5', scen='fewest cubes matching a top view and a front view',
         fig=drawing(170, 70, views()),
         stem='Ajay builds a solid with cubes. These are its top view and front view. What is the smallest number of cubes he could have used?',
         opts=['5', '4', '6', '3'],
         hint='The top view shows 4 towers. The front view shows that one tower on the left is 2 cubes tall.',
         sol='The top view needs 4 towers of at least 1 cube. The front view shows the left side is 2 cubes tall, so at least one left tower has 2 cubes. The smallest total is 4 + 1 = 5.'),

    # ---------------- Part 5 · Mensuration
    dict(ch='6', scen='perimeter of a rectangle with a square stuck on top',
         fig=drawing(160, 120, rect_with_square()),
         stem='A 3 cm square is joined to the top of a rectangle 12 cm long and 5 cm wide. What is the perimeter of the new shape?',
         opts=['40 cm', '34 cm', '46 cm', '43 cm'],
         hint='The square adds two upright sides. Its top side replaces the part of the rectangle it covers.',
         sol='The rectangle has perimeter 2 × (12 + 5) = 34 cm. The square adds 3 cm on each side going up and down. Its top replaces the 3 cm it covers. 34 + 3 + 3 = 40 cm.'),
    dict(ch='6', scen='25 cm by 20 cm cards cut from one square metre',
         stem='Tarun cuts cards 25 cm by 20 cm from a square sheet with sides of 1 m. What is the largest number of cards he can cut?',
         opts=['20', '25', '4', '200'],
         hint='1 m = 100 cm. How many cards fit along each side?',
         sol='Along one side: 100 ÷ 25 = 4 cards. Along the other: 100 ÷ 20 = 5 cards. 4 × 5 = 20 cards, with nothing wasted (20 × 500 cm² = 10,000 cm² = 1 m²).'),
    dict(ch='6', scen='5 kg 40 g minus 2 kg 875 g',
         stem='A sack holds 5 kg 40 g of potatoes. Prakash takes out 2 kg 875 g. How much is left in the sack?',
         opts=['2 kg 165 g', '3 kg 165 g', '2 kg 835 g', '3 kg 835 g'],
         hint='Change both to grams first.',
         sol='5 kg 40 g = 5,040 g. 2 kg 875 g = 2,875 g. 5,040 − 2,875 = 2,165 g = 2 kg 165 g.'),
    dict(ch='6', scen='five rounds of a 150 m by 100 m park',
         stem='A park is 150 m long and 100 m wide. Swati jogs 5 rounds along its edge. How far does she jog?',
         opts=['2 km 500 m', '1 km 250 m', '2 km 50 m', '75 km'],
         hint='Find the perimeter first.',
         sol='One round: 2 × (150 + 100) = 500 m. Five rounds: 2,500 m = 2 km 500 m.'),

    # ---------------- Part 6 · Data Handling
    dict(ch='8', scen='pictograph of flowers · half symbol for Friday',
         fig=drawing(320, 160, pict([('Monday', 2), ('Tuesday', 5), ('Wednesday', 3), ('Thursday', 7)], '🌻', '10 flowers')),
         stem='The pictograph shows flowers picked each day. On Friday, 15 more flowers were picked than on Wednesday. How many symbols should be drawn for Friday?',
         opts=['4 1/2', '4', '5', '1 1/2'],
         hint='A half symbol stands for 5 flowers.',
         sol='Wednesday: 3 × 10 = 30 flowers. Friday: 30 + 15 = 45 flowers. 45 = 4 full symbols (40) and half a symbol (5). So 4 1/2 symbols.'),

    # ---------------- Part 7 · Applied Mathematics
    dict(ch='9', scen='two trains with different starts and journey times · which arrives first',
         stem='Train A leaves at 7:45 AM and takes 2 h 50 min. Train B leaves at 8:20 AM and takes 2 h 10 min. Which train arrives first, and by how much?',
         opts=['Train B, by 5 min', 'Train A, by 5 min', 'Train B, by 35 min', 'They arrive together'],
         hint='Find each arrival time.',
         sol='Train A: 7:45 + 2 h 50 min = 10:35 AM. Train B: 8:20 + 2 h 10 min = 10:30 AM. Train B arrives 5 minutes earlier.'),
    dict(ch='9', scen='28 February Monday in a leap year · day of 1 March',
         stem='In a leap year, 28 February is a Monday. What day of the week is 1 March?',
         opts=['Wednesday', 'Tuesday', 'Thursday', 'Monday'],
         hint='A leap year has 29 days in February.',
         sol='29 February comes after 28 February, so it is a Tuesday. 1 March is the next day: Wednesday.'),
    dict(ch='9', scen='return bus tickets for 2 adults and 3 children',
         stem='A bus ticket costs ₹24 for an adult and half of that for a child. Two adults and three children make a return trip. They pay with ₹200. How much change do they get?',
         opts=['₹32', '₹116', '₹56', ['₹20'][0]],
         hint='Find the cost of one way first.',
         sol='Child ticket: ₹12. One way: 2 × 24 + 3 × 12 = 48 + 36 = ₹84. Return trip: 84 × 2 = ₹168. Change: 200 − 168 = ₹32.'),

    # ---------------- Part 8 · Mathematical Reasoning
    dict(ch='10', scen='series 1 3 7 15 31',
         fig=cards([1, 3, 7, 15, 31, '?'], size=40),
         stem='Nitya\'s series doubles a number and adds the same amount each time. Which number comes next?',
         opts=['63', '62', '47', '64'],
         hint='Look at 3 = 1 × 2 + 1.',
         sol='Each number is double the one before plus 1: 31 × 2 + 1 = 63.'),
    dict(ch='10', scen='2-digit numbers whose digits differ by 3',
         stem='How many 2-digit numbers have digits that differ by 3, like 52 or 14?',
         opts=['13', '12', '14', '7'],
         hint='Count those with the bigger digit in the tens place and those with it in the ones place.',
         sol='Tens digit 3 more: 30, 41, 52, 63, 74, 85, 96 (7). Ones digit 3 more: 14, 25, 36, 47, 58, 69 (6). 03 is not a 2-digit number. 7 + 6 = 13.'),
    dict(ch='10', scen='balance chain mangoes apples bananas',
         stem='2 mangoes weigh the same as 3 apples. 4 apples weigh the same as 6 bananas. How many bananas weigh the same as 8 mangoes?',
         opts=['18', '12', '16', '24'],
         hint='First change mangoes into apples.',
         sol='8 mangoes = 4 groups of 2 mangoes = 4 × 3 = 12 apples. 12 apples = 3 groups of 4 apples = 3 × 6 = 18 bananas.'),
    dict(ch='10', scen='squares of all sizes in a 3 by 5 grid',
         fig=grid([[''] * 5 for _ in range(3)], cell=30),
         stem='How many squares of all sizes are there in this 3 by 5 grid?',
         opts=['26', '15', '23', '30'],
         hint='Count 1 by 1, 2 by 2 and 3 by 3 squares.',
         sol='1 by 1: 3 × 5 = 15. 2 by 2: 2 × 4 = 8. 3 by 3: 1 × 3 = 3. 15 + 8 + 3 = 26.'),

    # ---------------- Section II · Star Questions
    dict(ch='3+10', scen='12 m rope cut by a half then a third then a quarter of what remains',
         stem='Madhav has a rope 12 m long. He cuts off half of it. Then he cuts off 1/3 of what is left. Then he cuts off 1/4 of what is left. How long is the rope now?',
         opts=['3 m', '1 m', '4 m', '6 m'],
         hint='Find the length after each cut.',
         sol='After the first cut: 6 m. 1/3 of 6 is 2, leaving 4 m. 1/4 of 4 is 1, leaving 3 m.'),
    dict(ch='9+10', scen='1 March Monday · day of 1 January in a non-leap year',
         stem='In a year that is not a leap year, 1 March is a Monday. What day of the week was 1 January of that year?',
         opts=['Friday', 'Thursday', 'Saturday', 'Monday'],
         hint='Count back the days of January and February.',
         sol='1 March is 31 + 28 = 59 days after 1 January. 59 = 8 weeks + 3 days. 3 days before Monday is Friday.'),
    dict(ch='1+10', scen='sum of the numbers 1 to 100 by pairing',
         stem='Prachi adds all the numbers from 1 to 100. She pairs 1 with 100, 2 with 99, and so on. What total does she get?',
         opts=['5,050', '5,000', '10,100', '5,100'],
         hint='How many pairs are there, and what does each pair add up to?',
         sol='Each pair adds up to 101: 1 + 100, 2 + 99, …, 50 + 51. There are 50 pairs. 50 × 101 = 5,050.'),
    dict(ch='3+9', scen='3/4 kg of tea costs ₹360 · price of 1 1/2 kg',
         stem='3/4 kg of tea costs ₹360. How much does 1 1/2 kg of the same tea cost?',
         opts=['₹720', '₹540', ['₹480'][0], '₹600'],
         hint='1 1/2 kg is double 3/4 kg.',
         sol='3/4 + 3/4 = 6/4 = 1 1/2. So 1 1/2 kg costs double: 2 × 360 = ₹720.'),
    dict(ch='5+6', scen='30 cm square tiles on a 2.4 m by 1.5 m bathroom floor',
         stem='A bathroom floor is 2.4 m long and 1.5 m wide. It is covered with square tiles with sides of 30 cm. How many tiles are needed?',
         opts=['40', '36', '50', '24'],
         hint='Change the lengths to centimetres.',
         sol='2.4 m = 240 cm and 1.5 m = 150 cm. Along the length: 240 ÷ 30 = 8 tiles. Along the width: 150 ÷ 30 = 5 tiles. 8 × 5 = 40 tiles.'),
]
