# AMO Level-2 · Class 4 · Practice Paper 7  (format: see paper01.py)


def pict(rows, em, key, lw=90, step=28):
    prims = []
    for i, (lab, n) in enumerate(rows):
        y = 18 + i * 34
        prims += [('rect', 0, y - 15, lw, 30, 'lilac'), ('text', lw / 2, y, lab, 12)]
        prims += [('emoji', em, lw + 20 + k * step, y, 24) for k in range(n)]
    y = 18 + len(rows) * 34 + 6
    prims += [('emoji', em, 14, y, 20), ('text', 40 + len(key) * 3.6, y, '= ' + key, 12)]
    return prims


def staircase():
    s, prims = 22, []
    for col in range(4):
        for row in range(col + 1):
            prims.append(('rect', 10 + col * s, 10 + (3 - row) * s, s, s, 'peach'))
    prims.append(('text', 10 + 2 * s, 10 + 4 * s + 12, 'each small square: 1 cm by 1 cm', 10))
    return prims


def square_diag():
    return [('rect', 10, 10, 100, 100, 'yellow'), ('line', 10, 10, 110, 110), ('line', 110, 10, 10, 110)]


QUESTIONS = [
    # ---------------- Part 1 · Number System
    dict(ch='1', scen='5-digit number riddle between 40,000 and 50,000',
         stem='Ashwin\'s number is between 40,000 and 50,000. Its first digit is twice its last digit. Its hundreds digit is 5 more than its last digit. Its tens digit is the sum of its first and last digits. Its thousands digit is its hundreds digit minus its tens digit. What is the number?',
         opts=['41,762', '41,726', '42,762', '41,672'],
         hint='The first digit is 4, so the last digit is 2.',
         sol='First digit 4, so the ones digit is 2. Hundreds: 2 + 5 = 7. Tens: 4 + 2 = 6. Thousands: 7 − 6 = 1. The number is 41,762.'),
    dict(ch='1', scen='counting on in 2,500s from 37,500 · which number is reached',
         stem='Tara counts on in steps of 2,500, starting at 37,500. Which of these numbers will she say?',
         opts=['52,500', '49,500', '51,000', '53,750'],
         hint='The numbers she says always end in 000 or 500, and go 40,000, 42,500, …',
         sol='She says 37,500, 40,000, 42,500, 45,000, 47,500, 50,000, 52,500, 55,000, … So 52,500 is said. 49,500 is between 47,500 and 50,000, 51,000 is between 50,000 and 52,500, and 53,750 is between 52,500 and 55,000, so she never says them.'),
    dict(ch='1', scen='total letters to write 1 to 10 in Roman numerals',
         stem='Nandini writes the numbers 1 to 10 in Roman numerals. How many letters does she write in all?',
         opts=['21', '20', '10', '18'],
         hint='VIII has 4 letters.',
         sol='I (1), II (2), III (3), IV (2), V (1), VI (2), VII (3), VIII (4), IX (2), X (1). 1 + 2 + 3 + 2 + 1 + 2 + 3 + 4 + 2 + 1 = 21.'),

    # ---------------- Part 2 · Operations
    dict(ch='2', scen='498 times 21 against the estimate 500 times 20',
         stem='Kavya estimates 498 × 21 as 500 × 20. How much bigger is the exact answer than her estimate?',
         opts=['458', '42', '498', '0'],
         hint='Work out 498 × 21 exactly: 498 × 20 + 498.',
         sol='Estimate: 500 × 20 = 10,000. Exact: 498 × 21 = 9,960 + 498 = 10,458. 10,458 − 10,000 = 458.'),
    dict(ch='2', scen='pens sold 4 for ₹27 · price of 36 pens',
         stem='A shop sells pens in packs of 4 for ₹27. Arun needs 36 pens. How much does he pay?',
         opts=['₹243', '₹972', '₹270', '₹216'],
         hint='How many packs make 36 pens?',
         sol='36 ÷ 4 = 9 packs. 9 × 27 = ₹243.'),
    dict(ch='2', scen='four products that are all 900',
         stem='Which of these gives the largest answer: 25 × 36, 30 × 30, 45 × 20 or 18 × 50?',
         opts=['All four are equal', '30 × 30', '25 × 36', '18 × 50'],
         hint='Work each one out, or look for ways to regroup.',
         sol='25 × 36 = 900. 30 × 30 = 900. 45 × 20 = 900. 18 × 50 = 900. All four are equal.'),

    # ---------------- Part 3 · Fractions & Decimals
    dict(ch='3', scen='two walks in tenths of a km against four fifths of a km',
         stem='Ravi walks 3/10 km to the shop and 7/10 km to the park. Asha walks 4/5 km. Who walks farther, and by how much?',
         opts=['Ravi, by 1/5 km', 'Asha, by 1/5 km', 'Ravi, by 1/10 km', 'Both the same'],
         hint='Write 4/5 as tenths.',
         sol='Ravi walks 3/10 + 7/10 = 10/10 = 1 km. Asha walks 4/5 = 8/10 km. Ravi walks 2/10 = 1/5 km farther.'),
    dict(ch='3', scen='tank filled a half a quarter and an eighth · fraction still empty',
         stem='A tank is empty. On Monday 1/2 of it is filled, on Tuesday 1/4 of it and on Wednesday 1/8 of it. What fraction of the tank is still empty?',
         opts=['1/8', '1/14', '3/8', '1/4'],
         hint='Write all three fractions as eighths.',
         sol='1/2 + 1/4 + 1/8 = 4/8 + 2/8 + 1/8 = 7/8. Still empty: 8/8 − 7/8 = 1/8.'),
    dict(ch='3', scen='body temperature falls then rises',
         stem='Ritu has a fever of 38.4 degrees. After medicine it falls by 1.9 degrees. In the evening it rises by 0.7 degrees. What is her temperature in the evening?',
         opts=['37.2 degrees', '36.8 degrees', '35.8 degrees', '37.6 degrees'],
         hint='Subtract first, then add.',
         sol='38.4 − 1.9 = 36.5. 36.5 + 0.7 = 37.2 degrees.'),
    dict(ch='3', scen='field 5/6 planted with a quarter wheat and the rest rice',
         stem='A farmer plants 5/6 of his field. 1/4 of the whole field is wheat and the rest of the planted part is rice. What fraction of the field is rice?',
         opts=['7/12', '3/12', '1/12', '13/12'],
         hint='Write 5/6 and 1/4 as twelfths.',
         sol='5/6 = 10/12 and 1/4 = 3/12. Rice: 10/12 − 3/12 = 7/12 of the field.'),

    # ---------------- Part 4 · Geometry
    dict(ch='5', scen='edges of a pentagonal pyramid plus vertices of a hexagonal prism',
         stem='Lavanya adds the number of edges of a pentagonal pyramid to the number of vertices of a hexagonal prism. What does she get?',
         opts=['22', '20', '27', '17'],
         hint='A pentagonal pyramid has 5 base edges and 5 slanting edges.',
         sol='Pentagonal pyramid: 5 + 5 = 10 edges. Hexagonal prism: 6 vertices on each base, so 12 vertices. 10 + 12 = 22.'),
    dict(ch='5', scen='perpendicular pairs in a square with both diagonals',
         fig=drawing(120, 120, square_diag()),
         stem='Kush draws a square and both of its diagonals. How many pairs of these six line segments are perpendicular to each other?',
         opts=['5', '4', '6', '2'],
         hint='The two diagonals of a square also cross at a square corner.',
         sol='Each side is perpendicular to the 2 sides next to it, which gives 4 pairs (one at each corner). The two diagonals are also perpendicular. 4 + 1 = 5.'),
    dict(ch='5', scen='fourth corner of a square on a row-column grid',
         stem='Three corners of a square are at (row 1, column 2), (row 1, column 6) and (row 5, column 6). Where is the fourth corner?',
         opts=['Row 5, column 2', 'Row 6, column 2', 'Row 5, column 1', 'Row 1, column 5'],
         hint='Opposite sides of a square line up with each other.',
         sol='The top side goes from column 2 to column 6 on row 1. The right side goes from row 1 to row 5 on column 6. So the bottom-left corner is at row 5, column 2.'),

    # ---------------- Part 5 · Mensuration
    dict(ch='6', scen='perimeter of a four-step staircase of unit squares',
         fig=drawing(110, 115, staircase()),
         stem='This staircase is made of 1 cm squares. What is its perimeter?',
         opts=['16 cm', '20 cm', '10 cm', '40 cm'],
         hint='Push the small steps out to make a rectangle. Does the perimeter change?',
         sol='The steps going up add up to 4 cm and the steps going across add up to 4 cm. With the bottom (4 cm) and left side (4 cm), the perimeter is 4 + 4 + 4 + 4 = 16 cm.'),
    dict(ch='6', scen='skirting round a room except at the door · cost',
         stem='A room is 6 m long and 5 m wide. A skirting board runs along the bottom of all the walls, except at the door, which is 1 m wide. It costs ₹25 per metre. What does it cost?',
         opts=['₹525', '₹550', '₹750', '₹275'],
         hint='Find the perimeter of the room first.',
         sol='Perimeter = 2 × (6 + 5) = 22 m. Without the door: 21 m. Cost: 21 × 25 = ₹525.'),
    dict(ch='6', scen='2 kg cake cut into 8 pieces · weight of 3 pieces',
         stem='A cake weighs 2 kg. Mother cuts it into 8 equal pieces. Rohan eats 3 pieces. What is the weight of cake that Rohan eats?',
         opts=['750 g', '250 g', '600 g', '1 kg 250 g'],
         hint='Change 2 kg into grams.',
         sol='2 kg = 2,000 g. One piece: 2,000 ÷ 8 = 250 g. Three pieces: 750 g.'),
    dict(ch='6', scen='50 L tank emptied at 2 L 750 mL and 3 L 250 mL a day',
         stem='A tank has 50 L of water. Each day 2 L 750 mL is used in the morning and 3 L 250 mL in the evening. For how many full days will the water last?',
         opts=['8', '9', '6', '10'],
         hint='Find the water used in one whole day.',
         sol='Each day: 2 L 750 mL + 3 L 250 mL = 6 L. 50 ÷ 6 = 8 remainder 2, so the water lasts 8 full days (2 L is left).'),

    # ---------------- Part 6 · Data Handling
    dict(ch='8', scen='pictograph of pencils sold by four shops · total money',
         fig=drawing(300, 160, pict([('Shop A', 3), ('Shop B', 5), ('Shop C', 4), ('Shop D', 6)], '✏️', '12 pencils')),
         stem='The pictograph shows the pencils sold by four shops in a day. Each pencil costs ₹5. How much money did the four shops get in all?',
         opts=['₹1,080', '₹216', '₹90', '₹1,200'],
         hint='Count all the symbols first.',
         sol='Symbols: 3 + 5 + 4 + 6 = 18. Pencils: 18 × 12 = 216. Money: 216 × 5 = ₹1,080.'),

    # ---------------- Part 7 · Applied Mathematics
    dict(ch='9', scen='baking and cooling a cake to be ready at 4:15 PM',
         stem='Rekha\'s cake needs 1 hour 35 minutes of baking and then 50 minutes of cooling. She wants it ready at 4:15 PM. When must she start baking?',
         opts=['1:50 PM', '2:40 PM', '2:00 PM', '1:40 PM'],
         hint='Add the two times, then count back from 4:15 PM.',
         sol='1 h 35 min + 50 min = 2 h 25 min. 4:15 PM − 2 h = 2:15 PM. 2:15 PM − 25 min = 1:50 PM.'),
    dict(ch='9', scen='12 November Sunday · day of 2 October',
         stem='In a certain year, 12 November is a Sunday. What day of the week was 2 October in the same year?',
         opts=['Monday', 'Saturday', 'Tuesday', 'Sunday'],
         hint='October has 31 days. Count the days from 2 October to 12 November.',
         sol='From 2 October to 31 October: 29 days. Then 12 more days to 12 November: 41 days. 41 = 5 weeks + 6 days. 6 days before Sunday is Monday.'),
    dict(ch='9', scen='₹220 in ₹5 and ₹10 coins with four more ₹10 coins',
         stem='Shalini has ₹220 in ₹5 and ₹10 coins. She has 4 more ₹10 coins than ₹5 coins. How many coins does she have in all?',
         opts=['28', '24', '16', '32'],
         hint='Put the 4 extra ₹10 coins aside first.',
         sol='The 4 extra ₹10 coins make ₹40, leaving ₹180. Each pair of one ₹5 and one ₹10 coin makes ₹15. 180 ÷ 15 = 12 pairs. So 12 coins of ₹5 and 16 of ₹10: 28 coins.'),

    # ---------------- Part 8 · Mathematical Reasoning
    dict(ch='10', scen='series 4 9 19 39 79',
         fig=cards([4, 9, 19, 39, 79, '?'], size=40),
         stem='Vinay\'s series uses the same rule each time. Which number comes next?',
         opts=['159', '158', '119', '160'],
         hint='Double each number and then add something.',
         sol='Each number is double the one before plus 1: 4 × 2 + 1 = 9, 9 × 2 + 1 = 19, … 79 × 2 + 1 = 159.'),
    dict(ch='10', scen='3-digit numbers with increasing digits from 1 to 5',
         stem='Yamini makes 3-digit numbers from the digits 1, 2, 3, 4 and 5. Each digit is bigger than the one before, like 135. How many such numbers can she make?',
         opts=['10', '6', '12', '60'],
         hint='Once you choose three digits, there is only one way to put them in increasing order.',
         sol='List them: 123, 124, 125, 134, 135, 145, 234, 235, 245, 345. That is 10.'),
    dict(ch='10', scen='finding a heavy coin among 9 with a balance',
         stem='Pratik has 9 coins that look the same. One is a little heavier. With a two-pan balance, what is the least number of weighings that will always find the heavy coin?',
         opts=['2', '3', '4', '8'],
         hint='Put the coins in 3 groups of 3.',
         sol='Weigh 3 coins against 3. If one side is heavier, the coin is there; if they balance, it is in the other 3. Then weigh 1 coin against 1 of those 3 in the same way. So 2 weighings are enough. One weighing cannot decide among 9 coins.'),
    dict(ch='10', scen='rectangles in a 2 by 3 grid',
         fig=grid([[''] * 3, [''] * 3], cell=40),
         stem='How many rectangles of all sizes are there in this grid? (Squares count as rectangles.)',
         opts=['18', '6', '12', '17'],
         hint='Choose 2 of the 4 upright lines and 2 of the 3 flat lines.',
         sol='There are 4 upright lines, so 6 ways to choose a left and right side. There are 3 flat lines, so 3 ways to choose a top and bottom. 6 × 3 = 18 rectangles.'),

    # ---------------- Section II · Star Questions
    dict(ch='3+10', scen='drinking half of what is left each day from 1 L',
         stem='Bhavna has a 1 L bottle of juice. Each day she drinks half of what is left in the bottle. After how many days is 1/8 L left?',
         opts=['3', '4', '8', '2'],
         hint='Write the amount left after each day.',
         sol='After day 1: 1/2 L. After day 2: 1/4 L. After day 3: 1/8 L. So after 3 days.'),
    dict(ch='9+10', scen='months with five Sundays when 1 January is Sunday',
         stem='In a year that is not a leap year, 1 January is a Sunday. In how many months of that year are there five Sundays?',
         opts=['5', '4', '6', '1'],
         hint='A month has five Sundays if its first Sunday is on the 1st, 2nd or 3rd, depending on its length.',
         sol='The year has 365 = 52 weeks + 1 day, so there are 53 Sundays. 12 months × 4 = 48, so 5 months have a 5th Sunday. (They are January, April, July, October and December.)'),
    dict(ch='1+10', scen='pattern 1 times 9 plus 2 equals 11 · next line',
         fig=equations([['1 × 9 + 2', '=', '11'], ['12 × 9 + 3', '=', '111'], ['123 × 9 + 4', '=', '1,111']], size=28),
         stem='Look at the pattern. What is 1,234 × 9 + 5?',
         opts=['11,111', '1,11,111', '11,106', '10,111'],
         hint='Each answer has one more 1 than the line before.',
         sol='The answers are 11, 111, 1,111, so the next is 11,111. Check: 1,234 × 9 = 11,106, and 11,106 + 5 = 11,111.'),
    dict(ch='3+9', scen='mother pays three quarters of a bag price · son pays the rest from savings',
         stem='A school bag costs ₹840. Mother pays 3/4 of the price. Om pays the rest from his savings of ₹500. How much does Om have left?',
         opts=['₹290', '₹210', '₹130', '₹340'],
         hint='Om pays 1/4 of the price.',
         sol='Om pays 1/4 of ₹840 = ₹210. He has 500 − 210 = ₹290 left.'),
    dict(ch='5+6', scen='hidden face area inside a cube of eight small cubes',
         stem='Eight 1 cm cubes are put together to make a 2 cm cube. What is the total area of the small cube faces that are hidden inside the big cube?',
         opts=['24 cm²', '48 cm²', '12 cm²', '6 cm²'],
         hint='Find the area of all the small faces, then the area of the outside of the big cube.',
         sol='All small faces: 8 × 6 = 48 faces of 1 cm², which is 48 cm². The outside of the big cube: 6 faces of 2 × 2 = 4 cm², which is 24 cm². Hidden: 48 − 24 = 24 cm².'),
]
