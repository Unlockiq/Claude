# AMO Level-2 · Class 4 · Practice Paper 6  (format: see paper01.py)


def pict(rows, em, key, lw=90, step=28):
    prims = []
    for i, (lab, n) in enumerate(rows):
        y = 18 + i * 34
        prims += [('rect', 0, y - 15, lw, 30, 'lilac'), ('text', lw / 2, y, lab, 12)]
        prims += [('emoji', em, lw + 20 + k * step, y, 24) for k in range(n)]
    y = 18 + len(rows) * 34 + 6
    prims += [('emoji', em, 14, y, 20), ('text', 40 + len(key) * 3.6, y, '= ' + key, 12)]
    return prims


NETS = {  # (row, col) cells of four 6-square shapes; only R folds into a cube
    'P': [(0, 0), (0, 1), (0, 2), (1, 0), (1, 1), (1, 2)],
    'Q': [(0, 0), (0, 1), (1, 0), (1, 1), (1, 2), (1, 3)],
    'R': [(0, 0), (0, 1), (1, 1), (1, 2), (2, 2), (2, 3)],
    'S': [(0, 0), (0, 1), (0, 2), (0, 3), (0, 4), (1, 1)],
}


def nets():
    s, prims = 18, []
    for i, (lab, cells) in enumerate(NETS.items()):
        x0 = i * 110
        for r, c in cells:
            prims.append(('rect', x0 + c * s, r * s, s, s, 'yellow'))
        prims.append(('text', x0 + 40, 80, lab, 14))
    return prims


def mirror_rect():
    return [('rect', 40, 20, 90, 60, 'blue'), ('line', 20, 80, 150, 80, True, (192, 40, 40), 2.4),
            ('text', 172, 80, 'mirror', 11), ('text', 85, 12, '3 cm', 11), ('text', 22, 50, '2 cm', 11)]


QUESTIONS = [
    # ---------------- Part 1 · Number System
    dict(ch='1', scen='times the digit 9 is written from 1 to 100',
         stem='Upasana writes all the numbers from 1 to 100. How many times does she write the digit 9?',
         opts=['20', '19', '11', '10'],
         hint='Count 9 in the ones place and 9 in the tens place separately.',
         sol='9 in the ones place: 9, 19, 29, …, 99, which is 10 times. 9 in the tens place: 90 to 99, which is 10 more times. 99 has two 9s and is counted in both lists, which is correct, as she writes 9 twice there. 10 + 10 = 20.'),
    dict(ch='1', scen='difference between sixty thousand six hundred six and six thousand sixty-six',
         stem='What is the difference between sixty thousand six hundred six and six thousand sixty-six?',
         opts=['54,540', '54,000', '66,672', '54,450'],
         hint='Write both numbers in digits first.',
         sol='Sixty thousand six hundred six = 60,606. Six thousand sixty-six = 6,066. 60,606 − 6,066 = 54,540.'),
    dict(ch='1', scen='second largest of XLIV LIV XCIV LXIV',
         stem='Which of these Roman numerals is the 2nd largest: XLIV, LIV, XCIV, LXIV?',
         opts=['LXIV', 'LIV', 'XCIV', 'XLIV'],
         hint='XL is 40 and XC is 90.',
         sol='XLIV = 44, LIV = 54, XCIV = 94 and LXIV = 64. From largest: 94, 64, 54, 44. The 2nd largest is LXIV.'),

    # ---------------- Part 2 · Operations
    dict(ch='2', scen='125 times 37 times 8 by grouping',
         stem='Rohan finds 125 × 37 × 8 quickly by changing the order of multiplying. What is the answer?',
         opts=['37,000', '3,700', '36,000', '37,800'],
         hint='125 × 8 is a round number.',
         sol='125 × 8 = 1,000. 1,000 × 37 = 37,000.'),
    dict(ch='2', scen='46 times 25 as 25 times a box plus 25 times 6',
         fig=equations([['46 × 25', '=', '25 × ?', '+', '25 × 6']], size=30),
         stem='Naina splits 46 into two parts to make this true. Which number goes in the box?',
         opts=['40', '46', '52', '6'],
         hint='46 × 25 is the same as 25 × 46. Split 46 into two parts.',
         sol='46 × 25 = 25 × 46 = 25 × (40 + 6) = 25 × 40 + 25 × 6. So the box is 40.'),
    dict(ch='2', scen='largest 4-digit number that 8 divides exactly',
         stem='What is the largest 4-digit number that can be divided by 8 with no remainder?',
         opts=['9,992', '9,996', '9,999', '9,984'],
         hint='Divide 9,999 by 8 and look at the remainder.',
         sol='9,999 ÷ 8 = 1,249 remainder 7. So 9,999 − 7 = 9,992 = 8 × 1,249.'),

    # ---------------- Part 3 · Fractions & Decimals
    dict(ch='3', scen='flour in three mixed-number amounts for a recipe',
         stem='For a big batch of laddoos, Devika uses 1 1/2 cups of flour, then 2 3/4 cups, then 3/4 of a cup. How many cups of flour does she use in all?',
         opts=['5 cups', '4 1/2 cups', '4 3/4 cups', '5 1/4 cups'],
         hint='Add the whole numbers, then the fractions.',
         sol='Whole cups: 1 + 2 = 3. Fractions: 1/2 + 3/4 + 3/4 = 2/4 + 3/4 + 3/4 = 8/4 = 2. Total 3 + 2 = 5 cups.'),
    dict(ch='3', scen='3/5 of a metre against 1/4 of a metre in cm',
         stem='Ribbon P is 3/5 of a metre long and ribbon Q is 1/4 of a metre long. How many centimetres longer is ribbon P?',
         opts=['35 cm', '2 cm', '25 cm', '60 cm'],
         hint='1 m = 100 cm.',
         sol='3/5 of 100 cm = 60 cm. 1/4 of 100 cm = 25 cm. 60 − 25 = 35 cm.'),
    dict(ch='3', scen='10 L can of paint with two amounts used',
         stem='A can holds 10 L of paint. Girish uses 3.7 L on a door and 2.5 L on a gate. How much paint is left?',
         opts=['3.8 L', '4.8 L', '6.2 L', '3.2 L'],
         hint='Add the paint used, then subtract from 10.',
         sol='Paint used: 3.7 + 2.5 = 6.2 L. Left: 10.0 − 6.2 = 3.8 L.'),
    dict(ch='3', scen='3/4 equals a box in twelfths plus 1/6',
         fig=equations([['3/4', '=', '?/12', '+', '1/6']], size=32),
         stem='Arjun wants both sides to be equal. Which numerator goes in the box?',
         opts=['7', '9', '2', '5'],
         hint='Write 3/4 and 1/6 as twelfths.',
         sol='3/4 = 9/12 and 1/6 = 2/12. 9/12 − 2/12 = 7/12, so the box is 7.'),

    # ---------------- Part 4 · Geometry
    dict(ch='5', scen='which of four 6-square shapes folds into a cube',
         fig=drawing(420, 90, nets()),
         stem='Each shape is made of 6 equal squares. Which shape can be folded to make a cube?',
         opts=['P', 'Q', 'R', 'S'], fixed=True, ans=2,
         hint='A cube net cannot have 5 squares in a row or a 2 by 2 block of squares.',
         sol='P is a 2 by 3 block and Q has a 2 by 2 block, so faces would overlap. S has 5 squares in a row, which wrap round past 4 sides. R is a staircase net: it folds into a cube.'),
    dict(ch='5', scen='robot moving on a numbered grid · final row and column',
         stem='A robot is on a grid at row 4, column 3. Rows are numbered from top to bottom. It moves 3 columns right, 2 rows up, 1 column left and then 4 rows down. Where is it now?',
         opts=['Row 6, column 5', 'Row 2, column 5', 'Row 6, column 7', 'Row 4, column 5'],
         hint='Moving up makes the row number smaller.',
         sol='Columns: 3 + 3 − 1 = 5. Rows: 4 − 2 + 4 = 6. The robot is at row 6, column 5.'),
    dict(ch='5', scen='solid with triangle front and side views and a square top view',
         stem='Seen from the front a solid looks like a triangle. From the side it also looks like a triangle. From the top it looks like a square. Which solid is it?',
         opts=['Square pyramid', 'Cone', 'Triangular prism', 'Cube'],
         hint='Which of these has a square base and a point at the top?',
         sol='A square pyramid has a square base, so the top view is a square, and it rises to a point, so the front and side views are triangles. A cone looks like a circle from the top, and a triangular prism looks like a rectangle from one side.'),

    # ---------------- Part 5 · Mensuration
    dict(ch='6', scen='square with the same perimeter as a 14 by 10 rectangle · area difference',
         stem='A square has the same perimeter as a rectangle 14 cm long and 10 cm wide. How much bigger is the area of the square than the area of the rectangle?',
         opts=['4 cm²', '0 cm²', '2 cm²', '44 cm²'],
         hint='Find the perimeter, then the side of the square.',
         sol='Perimeter = 2 × (14 + 10) = 48 cm, so the square has side 12 cm. Square: 144 cm². Rectangle: 140 cm². 144 − 140 = 4 cm².'),
    dict(ch='6', scen='rectangle with area 48 cm² and perimeter 28 cm · difference of sides',
         stem='A rectangle has an area of 48 cm² and a perimeter of 28 cm. How much longer is its length than its width?',
         opts=['2 cm', '4 cm', '8 cm', '20 cm'],
         hint='Length + width = 14 cm. Which pair also multiplies to 48?',
         sol='Length + width = 28 ÷ 2 = 14. Pairs adding to 14: 8 and 6 give 8 × 6 = 48. So the length is 8 cm and the width 6 cm. 8 − 6 = 2 cm.'),
    dict(ch='6', scen='square side increased by 2 cm and area grows by 36 cm²',
         stem='When each side of a square is made 2 cm longer, its area grows by 36 cm². What was the perimeter of the square at first?',
         opts=['32 cm', '36 cm', '40 cm', '28 cm'],
         hint='Try a few squares: from 5 cm to 7 cm the area grows from 25 to 49.',
         sol='Try side 8 cm: area 64. With side 10 cm: area 100. 100 − 64 = 36. So the side was 8 cm and the perimeter 4 × 8 = 32 cm.'),
    dict(ch='6', scen='10 cm tiles on a 2 m by 1 m table top',
         stem='A table top is 2 m long and 1 m wide. Payal covers it with square tiles of side 10 cm. How many tiles does she use?',
         opts=['200', '20', '30', '2,000'],
         hint='How many 10 cm tiles fit along 1 m?',
         sol='10 tiles fit along 1 m. Along 2 m: 20 tiles. Along 1 m: 10 tiles. 20 × 10 = 200 tiles.'),

    # ---------------- Part 6 · Data Handling
    dict(ch='8', scen='pictograph of fair tickets sold by four sections · money difference',
         fig=drawing(320, 160, pict([('4A', 7), ('4B', 5), ('4C', 8), ('4D', 6)], '🎟️', '10 tickets')),
         stem='The pictograph shows tickets sold by four sections for a school fair. Each ticket costs ₹15. How much more money did 4C collect than 4B?',
         opts=['₹450', '₹30', '₹45', '₹1,200'],
         hint='Find how many more tickets 4C sold.',
         sol='4C sold 8 − 5 = 3 more symbols = 30 more tickets. 30 × 15 = ₹450.'),

    # ---------------- Part 7 · Applied Mathematics
    dict(ch='9', scen='minutes from 9:47 AM to 1:15 PM',
         stem='A cricket match starts at 9:47 AM and stops for lunch at 1:15 PM. For how many minutes has it been played?',
         opts=['208 minutes', '328 minutes', '212 minutes', '188 minutes'],
         hint='Count to 10:00 AM first, then to 1:00 PM, then to 1:15 PM.',
         sol='9:47 to 10:00 is 13 minutes. 10:00 to 1:00 is 3 hours = 180 minutes. 1:00 to 1:15 is 15 minutes. 13 + 180 + 15 = 208 minutes.'),
    dict(ch='9', scen='party three days after a birthday on the 29th',
         stem='Kirti\'s birthday is on the 29th of a month whose 1st day is a Friday. Her party is 3 days after her birthday. On which day of the week is the party?',
         opts=['Monday', 'Friday', 'Sunday', 'Tuesday'],
         hint='The 29th is exactly 4 weeks after the 1st.',
         sol='The 29th is 28 days after the 1st, which is exactly 4 weeks, so it is a Friday. 3 days later is Monday.'),
    dict(ch='9', scen='change from ₹500 in the fewest notes and coins',
         stem='Manju buys a toy for ₹137 and a game for ₹248. She pays with a ₹500 note. The shop gives change in the fewest notes and coins. How many notes and coins does she get?',
         opts=['3', '2', '4', '5'],
         hint='Find the change first.',
         sol='She spends 137 + 248 = ₹385. Change: 500 − 385 = ₹115 = ₹100 + ₹10 + ₹5. That is 3 notes and coins.'),

    # ---------------- Part 8 · Mathematical Reasoning
    dict(ch='10', scen='two series mixed together 1 10 3 20 5 30 7',
         fig=cards([1, 10, 3, 20, 5, 30, 7, '?'], size=36),
         stem='Charvi mixed two series together. Which number comes next?',
         opts=['40', '9', '37', '35'],
         hint='Look at every other number.',
         sol='Odd places: 1, 3, 5, 7. Even places: 10, 20, 30, so next comes 40.'),
    dict(ch='10', scen='sum of odd numbers 1 to 19 from the square pattern',
         fig=equations([['1', '=', '1'], ['1 + 3', '=', '4'], ['1 + 3 + 5', '=', '9']], size=28),
         stem='Follow the pattern. What is 1 + 3 + 5 + … + 19?',
         opts=['100', '81', '121', '190'],
         hint='How many odd numbers are added each time? 1 number gives 1 × 1, 2 numbers give 2 × 2.',
         sol='Adding the first n odd numbers gives n × n. From 1 to 19 there are 10 odd numbers, so the sum is 10 × 10 = 100.'),
    dict(ch='10', scen='ways to pay ₹10 with ₹1 ₹2 and ₹5 coins',
         stem='Ishaan has plenty of ₹1, ₹2 and ₹5 coins. In how many different ways can he pay exactly ₹10?',
         opts=['10', '8', '6', '12'],
         hint='Sort the ways by the number of ₹5 coins: 0, 1 or 2.',
         sol='Two ₹5 coins: 1 way. One ₹5 coin: the other ₹5 uses 0, 1 or 2 coins of ₹2, which is 3 ways. No ₹5 coin: ₹10 uses 0 to 5 coins of ₹2, which is 6 ways. 1 + 3 + 6 = 10.'),
    dict(ch='10', scen='who owns the dog from two clues',
         stem='Ravi, Sita and Om each have one pet: a cat, a dog or a parrot. Ravi does not have the cat or the dog. Sita does not have the dog. Who has the dog?',
         opts=['Om', 'Ravi', 'Sita', 'Cannot tell'],
         hint='Start with Ravi.',
         sol='Ravi has neither the cat nor the dog, so he has the parrot. Sita does not have the dog, so she has the cat. Om has the dog.'),

    # ---------------- Section II · Star Questions
    dict(ch='3+10', scen='twelfths between one third and three quarters',
         stem='How many fractions with denominator 12 lie between 1/3 and 3/4? Do not count 1/3 and 3/4.',
         opts=['4', '5', '6', '3'],
         hint='Write 1/3 and 3/4 as twelfths.',
         sol='1/3 = 4/12 and 3/4 = 9/12. Between them: 5/12, 6/12, 7/12 and 8/12. That is 4 fractions.'),
    dict(ch='9+10', scen='Wednesdays in a leap year starting on Wednesday',
         stem='A leap year has 366 days. In one leap year, 1 January is a Wednesday. How many Wednesdays are there in that year?',
         opts=['53', '52', '54', '51'],
         hint='366 days is 52 weeks and 2 days.',
         sol='52 weeks give 52 Wednesdays. The 2 extra days at the end of the year are a Wednesday and a Thursday, because the year began on a Wednesday. So there are 53 Wednesdays.'),
    dict(ch='1+10', scen='smallest 5-digit number with digit sum 40',
         stem='What is the smallest 5-digit number whose digits add up to 40?',
         opts=['49,999', '58,999', '99,994', '39,999'],
         hint='Make the last digits as big as possible so the first digit can be small.',
         sol='The last four digits can be at most 9 each, which makes 36. So the first digit must be at least 4. The smallest number is 49,999. (39,999 has digit sum 39.)'),
    dict(ch='3+9', scen='selling three quarters of 120 eggs at one price and the rest at another',
         stem='A shopkeeper has 120 eggs. He sells 3/4 of them at ₹6 each and the rest at ₹5 each. How much money does he get?',
         opts=['₹690', '₹720', '₹660', '₹540'],
         hint='Find 3/4 of 120 first.',
         sol='3/4 of 120 = 90 eggs at ₹6: ₹540. The other 30 eggs at ₹5: ₹150. Total ₹690.'),
    dict(ch='5+6', scen='rectangle and its mirror image together · perimeter',
         fig=drawing(180, 90, mirror_rect()),
         stem='A 3 cm by 2 cm rectangle sits on a mirror line along its 3 cm side. The rectangle and its reflection together make one shape. What is the perimeter of that shape?',
         opts=['14 cm', '20 cm', '10 cm', '12 cm'],
         hint='The reflection is below the line. What shape do they make together?',
         sol='The reflection is another 3 cm by 2 cm rectangle just below the mirror. Together they make a 3 cm by 4 cm rectangle. Perimeter = 2 × (3 + 4) = 14 cm.'),
]
