# AMO Level-2 · Class 4 · Practice Paper 3  (format: see paper01.py)


def pict(rows, em, key, lw=90, step=28):
    prims = []
    for i, (lab, n) in enumerate(rows):
        y = 18 + i * 34
        prims += [('rect', 0, y - 15, lw, 30, 'lilac'), ('text', lw / 2, y, lab, 12)]
        prims += [('emoji', em, lw + 20 + k * step, y, 24) for k in range(n)]
    y = 18 + len(rows) * 34 + 6
    prims += [('emoji', em, 14, y, 20), ('text', 40 + len(key) * 3.6, y, '= ' + key, 12)]
    return prims


def tower_plan(h):
    """Top plan of cube towers: the number in a square is how many cubes are stacked there."""
    s = 40
    prims = [('text', 60, 4, 'BACK', 11)]
    for r, row in enumerate(h):
        for c, v in enumerate(row):
            prims += [('rect', c * s, 14 + r * s, s, s, 'yellow'), ('text', c * s + s / 2, 14 + r * s + s / 2, str(v), 16)]
    prims.append(('text', 60, 14 + 3 * s + 12, 'FRONT', 11))
    return prims


QUESTIONS = [
    # ---------------- Part 1 · Number System
    dict(ch='1', scen='greatest minus smallest place value of 5 in 55,505',
         stem='In the number 55,505, what is the difference between the greatest place value of a 5 and the smallest place value of a 5?',
         opts=['49,995', '49,500', '0', '45,000'],
         hint='Place value depends on where the digit is. Face value is just the digit.',
         sol='The 5s have place values 50,000, 5,000, 500 and 5. The greatest is 50,000 and the smallest is 5. 50,000 − 5 = 49,995.'),
    dict(ch='1', scen='smallest number that rounds to 46,000',
         stem='Bhavna rounds a whole number to the nearest thousand and gets 46,000. What is the smallest number she could have started with?',
         opts=['45,500', '45,000', '45,501', '46,499'],
         hint='Numbers from the halfway point upwards round up.',
         sol='Halfway between 45,000 and 46,000 is 45,500. 45,500 and above round up to 46,000, while 45,499 rounds down to 45,000. So the smallest is 45,500.'),
    dict(ch='1', scen='letter X written for Roman numerals 1 to 20',
         stem='Raghav writes the numbers 1 to 20 in Roman numerals. How many times does he write the letter X?',
         opts=['14', '12', '11', '13'],
         hint='Do not forget IX, XIX and XX.',
         sol='IX and X have one X each (2). XI to XVIII have one X each (8). XIX has two and XX has two (4). 2 + 8 + 4 = 14.'),

    # ---------------- Part 2 · Operations
    dict(ch='2', scen='estimate of 389 times 7 against the exact answer',
         stem='Anand estimates 389 × 7 by rounding 389 to the nearest hundred. By how much is his estimate more than the exact answer?',
         opts=['77', '11', '700', '2,723'],
         hint='Work out both 400 × 7 and 389 × 7.',
         sol='Estimate: 400 × 7 = 2,800. Exact: 389 × 7 = 2,723. 2,800 − 2,723 = 77. (Also: 11 × 7 = 77, because 389 is 11 less than 400.)'),
    dict(ch='2', scen='99 times 36 as 100 times 36 minus 36',
         stem='Hari works out 99 × 36 by first finding 100 × 36. What is 99 × 36?',
         opts=['3,564', '3,600', '3,500', '3,546'],
         hint='99 × 36 is one 36 less than 100 × 36.',
         sol='100 × 36 = 3,600. 99 × 36 is one 36 less: 3,600 − 36 = 3,564.'),
    dict(ch='2', scen='subtracting 7 again and again from 1,000',
         stem='Starting at 1,000, Neha subtracts 7 again and again. She stops when the number is less than 7. How many times does she subtract 7?',
         opts=['142', '143', '140', '141'],
         hint='This is the same as dividing 1,000 by 7.',
         sol='1,000 ÷ 7 = 142 remainder 6. After 142 subtractions she reaches 6, which is less than 7. So 142 times.'),

    # ---------------- Part 3 · Fractions & Decimals
    dict(ch='3', scen='pizza of 12 slices · quarter and third eaten',
         stem='A pizza is cut into 12 equal slices. Kartik eats 1/4 of the pizza and his sister eats 1/3 of it. How many slices are left?',
         opts=['5', '7', '10', '2'],
         hint='Find 1/4 of 12 and 1/3 of 12.',
         sol='1/4 of 12 = 3 slices. 1/3 of 12 = 4 slices. 3 + 4 = 7 slices are eaten, so 12 − 7 = 5 are left.'),
    dict(ch='3', scen='fraction exactly halfway between 1/2 and 3/4',
         stem='Which fraction is exactly halfway between 1/2 and 3/4?',
         opts=['5/8', '2/3', '7/12', '3/5'],
         hint='Write both fractions as eighths.',
         sol='1/2 = 4/8 and 3/4 = 6/8. Halfway between 4/8 and 6/8 is 5/8.'),
    dict(ch='3', scen='7.6 plus a box equals 10.2 plus 1.5',
         fig=equations([['7.6', '+', '?', '=', '10.2', '+', '1.5']], size=32),
         stem='Sita balances this number sentence so that both sides are equal. Which decimal goes in the box?',
         opts=['4.1', '3.1', '4.9', '2.6'],
         hint='Work out the right side first.',
         sol='10.2 + 1.5 = 11.7. Then ? = 11.7 − 7.6 = 4.1.'),
    dict(ch='3', scen='5 kg rice bag with 2 3/8 kg used',
         stem='A bag has 5 kg of rice. Nandini uses 2 3/8 kg of it. How much rice is left?',
         opts=['2 5/8 kg', '3 5/8 kg', '3 3/8 kg', '2 3/8 kg'],
         hint='Write 5 as 4 8/8.',
         sol='5 = 4 8/8. 4 8/8 − 2 3/8 = 2 5/8 kg.'),

    # ---------------- Part 4 · Geometry
    dict(ch='5', scen='front view of cube towers from a top plan',
         fig=drawing(120, 150, tower_plan([[2, 1, 3], [1, 2, 1], [1, 1, 2]])),
         stem='This plan shows cube towers seen from the top. Each number tells how many cubes are in that tower. How many squares do you see when you look from the front?',
         opts=['7', '4', '14', '9'],
         hint='From the front, each column shows only its tallest tower.',
         sol='Looking from the front, each column shows its tallest tower. Left column: tallest 2. Middle: tallest 2. Right: tallest 3. 2 + 2 + 3 = 7 squares.'),
    dict(ch='5', scen='triangular prism faces plus edges plus vertices',
         stem='Gita adds the number of faces, edges and vertices of a triangular prism. What total does she get?',
         opts=['20', '18', '19', '15'],
         hint='A triangular prism has 2 triangle faces and 3 rectangle faces.',
         sol='Faces: 2 + 3 = 5. Vertices: 3 on each triangle, 6. Edges: 3 + 3 + 3 = 9. 5 + 9 + 6 = 20. Check: 5 + 6 − 9 = 2.'),
    dict(ch='5', scen='reflecting a dot across a mirror line between columns D and E',
         stem='A grid has columns A to H. A mirror line runs down between columns D and E. A dot in column B, row 3 is reflected in the mirror. In which column is its image?',
         opts=['Column G', 'Column F', 'Column H', 'Column E'],
         hint='The image is the same number of columns from the mirror as the dot.',
         sol='Column B is the 3rd column to the left of the mirror (D, C, B). The image is the 3rd column to the right (E, F, G). So column G, row 3.'),

    # ---------------- Part 5 · Mensuration
    dict(ch='6', scen='rectangle with a square cut from the corner · perimeter unchanged',
         stem='A rectangle is 10 cm long and 6 cm wide. Mahi cuts a 2 cm by 2 cm square out of one corner. What is the perimeter of the shape that is left?',
         opts=['32 cm', '28 cm', '24 cm', '36 cm'],
         hint='The two new edges replace the two pieces of edge that were cut away.',
         sol='The cut takes away 2 cm from the top and 2 cm from the side, but adds two new edges of 2 cm each. The perimeter stays 2 × (10 + 6) = 32 cm.'),
    dict(ch='6', scen='painting a wall with a door · cost',
         stem='A wall is 5 m long and 3 m high. It has a door 2 m high and 1 m wide. Painting costs ₹40 for each square metre. What does it cost to paint the wall?',
         opts=['₹520', '₹600', '₹640', '₹80'],
         hint='Do not paint the door.',
         sol='Wall: 5 × 3 = 15 m². Door: 2 × 1 = 2 m². Area to paint: 13 m². Cost: 13 × 40 = ₹520.'),
    dict(ch='6', scen='square field with a perimeter of 1 km · area',
         stem='A square field has a perimeter of 1 km. What is its area in square metres?',
         opts=['62,500 m²', '1,000 m²', '6,250 m²', '25,000 m²'],
         hint='First change 1 km into metres and find one side.',
         sol='1 km = 1,000 m, so each side is 1,000 ÷ 4 = 250 m. Area = 250 × 250 = 62,500 m².'),
    dict(ch='6', scen='12 apples weigh 1 kg 800 g · weight of 5 apples',
         stem='Tulsi buys 12 equal apples that weigh 1 kg 800 g altogether. How much do 5 of these apples weigh?',
         opts=['750 g', '900 g', '600 g', '1 kg 500 g'],
         hint='Change 1 kg 800 g into grams and find the weight of one apple.',
         sol='1 kg 800 g = 1,800 g. One apple: 1,800 ÷ 12 = 150 g. 5 apples: 5 × 150 = 750 g.'),

    # ---------------- Part 6 · Data Handling
    dict(ch='8', scen='pictograph of cars passing a gate · busiest against quietest days',
         fig=drawing(320, 160, pict([('Monday', 5), ('Tuesday', 3), ('Wednesday', 7), ('Thursday', 4)], '🚗', '6 cars')),
         stem='The pictograph shows cars passing a school gate. How many more cars passed on the two busiest days together than on the two quietest days together?',
         opts=['30', '5', '18', '72'],
         hint='Find the two days with the most symbols and the two with the fewest.',
         sol='Busiest: Wednesday 7 and Monday 5, so 12 symbols. Quietest: Tuesday 3 and Thursday 4, so 7 symbols. Difference: 5 symbols = 5 × 6 = 30 cars.'),

    # ---------------- Part 7 · Applied Mathematics
    dict(ch='9', scen='bus every 25 minutes from 6:10 AM · buses before 9 AM',
         stem='The first bus leaves at 6:10 AM. After that, a bus leaves every 25 minutes. How many buses leave before 9:00 AM?',
         opts=['7', '6', '8', '9'],
         hint='List the times.',
         sol='6:10, 6:35, 7:00, 7:25, 7:50, 8:15, 8:40. The next one is 9:05, which is after 9:00. So 7 buses.'),
    dict(ch='9', scen='1 January Monday · day of 1 March in a non-leap year',
         stem='In a year that is not a leap year, 1 January is a Monday. What day of the week is 1 March?',
         opts=['Thursday', 'Wednesday', 'Friday', 'Monday'],
         hint='Count the days in January and February.',
         sol='1 March is 31 + 28 = 59 days after 1 January. 59 = 8 weeks + 3 days. 3 days after Monday is Thursday.'),
    dict(ch='9', scen='₹50 in sixteen ₹2 and ₹5 coins',
         stem='Kishore has 16 coins worth ₹50 in all. Every coin is either ₹2 or ₹5. How many ₹5 coins does he have?',
         opts=['6', '10', '5', '8'],
         hint='If all 16 coins were ₹2 coins, how much would they be worth?',
         sol='16 coins of ₹2 would make ₹32, which is ₹18 short. Changing a ₹2 coin for a ₹5 coin adds ₹3. 18 ÷ 3 = 6, so 6 coins are ₹5. Check: 6 × 5 + 10 × 2 = 30 + 20 = 50.'),

    # ---------------- Part 8 · Mathematical Reasoning
    dict(ch='10', scen='series 100 99 97 94 90',
         fig=cards([100, 99, 97, 94, 90, '?']),
         stem='Pallavi writes this series of numbers. Which number comes next?',
         opts=['85', '86', '84', '80'],
         hint='Look at how much is taken away each time.',
         sol='The series takes away 1, 2, 3, 4. Next it takes away 5: 90 − 5 = 85.'),
    dict(ch='10', scen='2-digit numbers with tens digit greater than ones digit',
         stem='How many 2-digit numbers have a tens digit that is greater than the ones digit, like 52?',
         opts=['45', '36', '54', '90'],
         hint='Count for each tens digit: with tens digit 3 the ones digit can be 0, 1 or 2.',
         sol='Tens digit 1: 1 number (10). Tens digit 2: 2 numbers. … Tens digit 9: 9 numbers. 1 + 2 + … + 9 = 45.'),
    dict(ch='10', scen='ways to climb 5 steps with 1 or 2 steps',
         stem='Ankit climbs a staircase of 5 steps. Each time he goes up either 1 step or 2 steps. In how many different ways can he climb the 5 steps?',
         opts=['8', '5', '6', '10'],
         hint='Count ways for 1, 2, 3, 4 steps first and look for a pattern.',
         sol='1 step: 1 way. 2 steps: 2 ways. 3 steps: 3 ways. 4 steps: 5 ways. 5 steps: 3 + 5 = 8 ways, because the last move is either 1 step (from step 4) or 2 steps (from step 3).'),
    dict(ch='10', scen='magic square with four hidden numbers',
         fig=grid([['8', '?', '6'], ['?', '5', '?'], ['4', '?', '2']], cell=44),
         stem='Every row, column and diagonal of this square adds up to 15. What is the sum of the four hidden numbers?',
         opts=['20', '15', '25', '30'],
         hint='Find each hidden number from a row or column that has two numbers given.',
         sol='Top row: 15 − 8 − 6 = 1. Left column: 15 − 8 − 4 = 3. Right column: 15 − 6 − 2 = 7. Bottom row: 15 − 4 − 2 = 9. 1 + 3 + 7 + 9 = 20.'),

    # ---------------- Section II · Star Questions
    dict(ch='3+10', scen='pattern 1/2 2/3 3/4 · how far the tenth is from 1',
         fig=cards(['1/2', '2/3', '3/4', '4/5', '…'], size=44, width=56),
         stem='The fractions follow a pattern. By how much is the 10th fraction less than 1?',
         opts=['1/11', '1/10', '1/12', '10/11'],
         hint='Each fraction is 1 part short of a whole.',
         sol='The 10th fraction is 10/11. 1 = 11/11, so it is 1/11 less than 1. (Each fraction in the pattern is one part short of a whole.)'),
    dict(ch='9+10', scen='day of the week 75 days before a Saturday',
         stem='Today is a Saturday. What day of the week was it 75 days ago?',
         opts=['Monday', 'Thursday', 'Tuesday', 'Sunday'],
         hint='75 days is 10 weeks and some days.',
         sol='75 = 10 × 7 + 5. Ten weeks ago it was Saturday. 5 more days back: Friday, Thursday, Wednesday, Tuesday, Monday.'),
    dict(ch='1+10', scen='numbers from 99,000 to 99,999 with only odd digits',
         stem='How many numbers from 99,000 to 99,999 have only odd digits?',
         opts=['125', '25', '100', '500'],
         hint='The first two digits are already odd. Each of the last three can be 1, 3, 5, 7 or 9.',
         sol='The last three digits each have 5 choices: 5 × 5 × 5 = 125.'),
    dict(ch='3+9', scen='homework hours in mixed numbers over three days',
         stem='Ishita studies for 1 1/2 hours on Monday, 2 1/4 hours on Tuesday and 3/4 of an hour on Wednesday. How long does she study in all?',
         opts=['4 h 30 min', '4 h 50 min', '3 h 30 min', '4 h 15 min'],
         hint='Add the whole hours, then add the fractions.',
         sol='Whole hours: 1 + 2 = 3. Fractions: 1/2 + 1/4 + 3/4 = 2/4 + 1/4 + 3/4 = 6/4 = 1 1/2. Total 4 1/2 hours = 4 hours 30 minutes.'),
    dict(ch='5+6', scen='cardboard for an open box made of 5 cm squares',
         stem='Ojas makes a cube-shaped box with no lid from a net of squares. Each edge of the box is 5 cm. How much cardboard does the net use?',
         opts=['125 cm²', '150 cm²', '25 cm²', '100 cm²'],
         hint='A cube has 6 faces, but this box has no lid.',
         sol='Each face is 5 × 5 = 25 cm². A box with no lid has 5 faces: 5 × 25 = 125 cm².'),
]
