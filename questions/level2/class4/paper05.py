# AMO Level-2 · Class 4 · Practice Paper 5  (format: see paper01.py)


def pict(rows, em, key, lw=90, step=28):
    prims = []
    for i, (lab, n) in enumerate(rows):
        y = 18 + i * 34
        prims += [('rect', 0, y - 15, lw, 30, 'lilac'), ('text', lw / 2, y, lab, 12)]
        prims += [('emoji', em, lw + 20 + k * step, y, 24) for k in range(n)]
    y = 18 + len(rows) * 34 + 6
    prims += [('emoji', em, 14, y, 20), ('text', 40 + len(key) * 3.6, y, '= ' + key, 12)]
    return prims


def path_grid(cols=3, rows=2, s=45):
    prims = []
    for r in range(rows + 1):
        prims.append(('line', 20, 20 + r * s, 20 + cols * s, 20 + r * s))
    for c in range(cols + 1):
        prims.append(('line', 20 + c * s, 20, 20 + c * s, 20 + rows * s))
    prims += [('dot', 20, 20, 5), ('text', 8, 8, 'A', 13), ('dot', 20 + cols * s, 20 + rows * s, 5),
              ('text', 33 + cols * s, 33 + rows * s, 'B', 13)]
    return prims


QUESTIONS = [
    # ---------------- Part 1 · Number System
    dict(ch='1', scen='even numbers between 99,900 and 1,00,000',
         stem='How many even numbers are there between 99,900 and 1,00,000? Do not count 99,900 or 1,00,000.',
         opts=['49', '50', '48', '100'],
         hint='The first one is 99,902 and the last one is 99,998.',
         sol='The even numbers are 99,902, 99,904, …, 99,998. Their last two digits go 02, 04, …, 98, which is 49 numbers.'),
    dict(ch='1', scen='hidden thousands digit when 4?,385 rounds to 47,000',
         stem='Naveen\'s number is 4?,385, with one digit hidden. When it is rounded to the nearest thousand, it becomes 47,000. What is the hidden digit?',
         opts=['7', '6', '8', '5'],
         hint='The last three digits are 385. Does that round the thousands up or down?',
         sol='385 is less than 500, so the number rounds down to its own thousand. The thousands must already be 47,000, so the hidden digit is 7. (46,385 would round to 46,000.)'),
    dict(ch='1', scen='numbers 1 to 50 whose Roman numeral contains V',
         stem='Vidya writes the numbers 1 to 50 in Roman numerals. How many of them contain the letter V?',
         opts=['25', '5', '10', '20'],
         hint='In 1 to 9, the numbers with V are IV, V, VI, VII and VIII.',
         sol='In each group of ten (1–9, 11–19, 21–29, 31–39, 41–49) the numbers ending in 4, 5, 6, 7, 8 contain V: 5 numbers. 5 groups × 5 = 25. 10, 20, 30, 40 and 50 have no V.'),

    # ---------------- Part 2 · Operations
    dict(ch='2', scen='reading 24 pages a day for four weeks from a 1,000-page book',
         stem='A book has 1,000 pages. Harini reads 24 pages every day for 4 weeks. How many pages are still left to read?',
         opts=['328', '904', '372', '428'],
         hint='4 weeks is 28 days.',
         sol='4 weeks = 28 days. Pages read: 24 × 28 = 672. Pages left: 1,000 − 672 = 328.'),
    dict(ch='2', scen='halving 3,600 until the answer is odd',
         stem='Sohan halves 3,600 again and again. He stops as soon as he gets an odd number. How many times does he halve?',
         opts=['4', '3', '5', '6'],
         hint='Write each answer.',
         sol='3,600 → 1,800 → 900 → 450 → 225. 225 is odd. He halved 4 times.'),
    dict(ch='2', scen='choosing two signs to make 48 4 3 equal 15',
         fig=equations([['48', '?', '4', '?', '3', '=', '15']], size=32),
         stem='Which two signs, in order, make this statement true?',
         opts=['÷ then +', '× then ÷', '− then ×', '÷ then −'],
         hint='Try each pair of signs.',
         sol='48 ÷ 4 + 3 = 12 + 3 = 15. The others: 48 × 4 ÷ 3 = 64, 48 − 4 × 3 = 36 and 48 ÷ 4 − 3 = 9.'),

    # ---------------- Part 3 · Fractions & Decimals
    dict(ch='3', scen='a day split into sleep school and play · hours left',
         stem='Mitali sleeps for 1/3 of a day, is at school for 1/4 of the day and plays for 1/12 of the day. How many hours of the day are left?',
         opts=['8 hours', '16 hours', '6 hours', '10 hours'],
         hint='A day has 24 hours.',
         sol='Sleep: 1/3 of 24 = 8 h. School: 1/4 of 24 = 6 h. Play: 1/12 of 24 = 2 h. 24 − 8 − 6 − 2 = 8 hours.'),
    dict(ch='3', scen='glass 3/4 full holds 300 mL · water to fill it',
         stem='A glass is 3/4 full and holds 300 mL of water. How much more water is needed to fill it?',
         opts=['100 mL', '75 mL', '400 mL', '225 mL'],
         hint='300 mL is 3 quarters. Find 1 quarter.',
         sol='3 quarters = 300 mL, so 1 quarter = 100 mL. The glass needs 1 more quarter: 100 mL.'),
    dict(ch='3', scen='plant trimmed then grows · height in cm',
         stem='A plant is 9.5 cm tall. Sunita trims 3.8 cm off it. In the next week it grows 2.6 cm. How tall is it now?',
         opts=['8.3 cm', '8.7 cm', '3.1 cm', '15.9 cm'],
         hint='Subtract first, then add.',
         sol='9.5 − 3.8 = 5.7 cm. 5.7 + 2.6 = 8.3 cm.'),
    dict(ch='3', scen='29 slices of one-sixth of a cake · whole cakes',
         stem='Ekta has 29 slices of cake. Each slice is 1/6 of a whole cake. How many cakes is that, as a mixed number?',
         opts=['4 5/6', '5 1/6', '4 1/6', '3 5/6'],
         hint='6 slices make a whole cake.',
         sol='29 = 4 × 6 + 5. That is 4 whole cakes and 5 slices left over: 4 5/6 cakes.'),

    # ---------------- Part 4 · Geometry
    dict(ch='5', scen='shapes in the net of a triangular prism tent',
         stem='A tent with a floor is shaped like a triangular prism. Kunal draws its net. Which shapes are in the net?',
         opts=['3 rectangles and 2 triangles', '2 rectangles and 3 triangles', '3 rectangles and 3 triangles', '4 rectangles and 2 triangles'],
         hint='A triangular prism has two triangle ends.',
         sol='The two ends are triangles. The prism has 3 side faces, which are rectangles (two sloping walls and the floor). So 3 rectangles and 2 triangles.'),
    dict(ch='5', scen='angles made by five rays from one point',
         stem='Ajay draws 5 rays starting from the same point. Any two rays make an angle. How many angles are there?',
         opts=['10', '5', '4', '20'],
         hint='Count the pairs of rays.',
         sol='The first ray pairs with 4 others, the second with 3 new ones, then 2, then 1. 4 + 3 + 2 + 1 = 10 angles.'),
    dict(ch='5', scen='solid with 6 vertices and 9 edges · faces from Euler',
         stem='A solid has 6 vertices and 9 edges. For solids like this, faces + vertices − edges = 2. How many faces does it have?',
         opts=['5', '4', '6', '3'],
         hint='Faces + 6 − 9 = 2.',
         sol='Faces = 2 + 9 − 6 = 5. (A triangular prism has 5 faces, 6 vertices and 9 edges.)'),

    # ---------------- Part 5 · Mensuration
    dict(ch='6', scen='rectangle twice as long as wide with area 72 cm²',
         stem='A rectangle is twice as long as it is wide. Its area is 72 cm². What is its perimeter?',
         opts=['36 cm', '18 cm', '72 cm', '30 cm'],
         hint='Try widths: if the width is 5, the area is 10 × 5 = 50.',
         sol='Width 6 cm and length 12 cm give 12 × 6 = 72 cm². Perimeter = 2 × (12 + 6) = 36 cm.'),
    dict(ch='6', scen='rectangle three times as long as wide with perimeter 64 cm',
         stem='A rectangle is 3 times as long as it is wide. Its perimeter is 64 cm. What is its area?',
         opts=['192 cm²', '128 cm²', '256 cm²', '48 cm²'],
         hint='Length + width = 32 cm, and the length is 3 widths.',
         sol='Length + width = 64 ÷ 2 = 32 cm. 3 widths + 1 width = 4 widths = 32, so the width is 8 cm and the length 24 cm. Area = 24 × 8 = 192 cm².'),
    dict(ch='6', scen='fencing a garden with a gate · cost',
         stem='A garden is 25 m long and 18 m wide. Its fence leaves a gap of 4 m for a gate. Fencing costs ₹12 per metre. What is the cost of the fence?',
         opts=['₹984', '₹1,032', '₹1,080', '₹5,400'],
         hint='Find the perimeter, then take away the gate.',
         sol='Perimeter = 2 × (25 + 18) = 86 m. Fence = 86 − 4 = 82 m. Cost = 82 × 12 = ₹984.'),
    dict(ch='6', scen='three bags of 2 kg 750 g and a box of 1 kg 400 g',
         stem='A scooter carries 3 bags of 2 kg 750 g each and one box of 1 kg 400 g. What is the total weight?',
         opts=['9 kg 650 g', '9 kg 150 g', '7 kg 650 g', '10 kg 650 g'],
         hint='1,000 g = 1 kg.',
         sol='3 bags: 6 kg 2,250 g = 8 kg 250 g. Add the box: 8 kg 250 g + 1 kg 400 g = 9 kg 650 g.'),

    # ---------------- Part 6 · Data Handling
    dict(ch='8', scen='pictograph of milk bought in four weeks · cost of two weeks',
         fig=drawing(300, 160, pict([('Week 1', 7), ('Week 2', 5), ('Week 3', 6), ('Week 4', 8)], '🥛', '5 litres')),
         stem='The pictograph shows the milk a family bought each week. Milk costs ₹54 per litre. How much did the milk cost in Week 2 and Week 3 together?',
         opts=['₹2,970', '₹594', '₹2,700', '₹3,024'],
         hint='Count the symbols for the two weeks and change them to litres.',
         sol='Week 2 and Week 3: 5 + 6 = 11 symbols = 55 litres. 55 × 54 = ₹2,970.'),

    # ---------------- Part 7 · Applied Mathematics
    dict(ch='9', scen='school day of eight 40-minute periods and a 20-minute break',
         stem='School starts at 7:55 AM. There are 8 periods of 40 minutes each and one break of 20 minutes. At what time does school end?',
         opts=['1:35 PM', '1:15 PM', '12:35 PM', '1:55 PM'],
         hint='Find the total time in minutes, then in hours and minutes.',
         sol='8 × 40 = 320 minutes, plus 20 = 340 minutes = 5 hours 40 minutes. 7:55 AM + 5 hours = 12:55 PM. 12:55 PM + 40 minutes = 1:35 PM.'),
    dict(ch='9', scen='26 January Friday · day of 15 March in a non-leap year',
         stem='In a year that is not a leap year, 26 January is a Friday. What day of the week is 15 March?',
         opts=['Thursday', 'Friday', 'Wednesday', 'Saturday'],
         hint='Count the days left in January, all of February and the days of March.',
         sol='27–31 January: 5 days. February: 28 days. 1–15 March: 15 days. 5 + 28 + 15 = 48 days later. 48 = 6 weeks + 6 days. 6 days after Friday is Thursday.'),
    dict(ch='9', scen='₹1,000 spent on four bats and some balls',
         stem='Sameer spends exactly ₹1,000 on sports items. He buys 4 bats at ₹185 each and the rest on balls at ₹26 each. How many balls does he buy?',
         opts=['10', '9', '11', '38'],
         hint='Find the cost of the bats first.',
         sol='Bats: 4 × 185 = ₹740. Money for balls: 1,000 − 740 = ₹260. Balls: 260 ÷ 26 = 10.'),

    # ---------------- Part 8 · Mathematical Reasoning
    dict(ch='10', scen='series where each number is the sum of the two before',
         fig=cards([1, 1, 2, 3, 5, 8, 13, '?'], size=36),
         stem='In Sakshi\'s series, each number comes from the two numbers before it. Which number comes next?',
         opts=['21', '18', '20', '26'],
         hint='Look at 2, 3 and 5.',
         sol='Each number is the sum of the two before it: 1 + 1 = 2, 1 + 2 = 3, 2 + 3 = 5, … 8 + 13 = 21.'),
    dict(ch='10', scen='shortest paths on a 3 by 2 grid',
         fig=drawing(160, 115, path_grid()),
         stem='Hemant walks along the lines from A to B, moving only right or down. How many different paths can he take?',
         opts=['10', '6', '5', '12'],
         hint='Each path has 3 moves right and 2 moves down. Choose where the 2 down moves go.',
         sol='A path has 5 moves: 3 right (R) and 2 down (D). The 2 Ds can be in places 1-2, 1-3, 1-4, 1-5, 2-3, 2-4, 2-5, 3-4, 3-5 or 4-5. That is 10 paths.'),
    dict(ch='10', scen='2-digit numbers whose digits multiply to 12',
         stem='How many 2-digit numbers have digits that multiply to give 12?',
         opts=['4', '2', '6', '3'],
         hint='Which pairs of digits multiply to 12? Each pair can go in two orders.',
         sol='Digit pairs: 2 and 6, 3 and 4 (1 and 12 is not allowed, as 12 is not a digit). Numbers: 26, 62, 34, 43. That is 4.'),
    dict(ch='10', scen='spent half then ₹20 more · ₹30 left',
         stem='Amit spends half of his money on a book and then ₹20 on a snack. He has ₹30 left. How much money did he have at the start?',
         opts=['₹100', '₹80', '₹70', '₹110'],
         hint='Work backwards: undo the snack first.',
         sol='Before the snack he had 30 + 20 = ₹50. That was half his money, so he started with 50 × 2 = ₹100.'),

    # ---------------- Section II · Star Questions
    dict(ch='3+10', scen='two different unit fractions adding to one half',
         stem='Hema finds two different whole numbers a and b so that 1/a + 1/b = 1/2. What is a + b?',
         opts=['9', '8', '10', '7'],
         hint='One of the fractions must be bigger than 1/4.',
         sol='One fraction must be more than 1/4, so it is 1/3. Then 1/2 − 1/3 = 3/6 − 2/6 = 1/6. So a and b are 3 and 6, and a + b = 9. (1/4 + 1/4 uses the same number twice.)'),
    dict(ch='9+10', scen='times in a day when a digital clock shows the same digit three or four times',
         stem='A 12-hour digital clock shows times like 2:22 and 11:11, where every digit is the same. How many such times are there in one whole day?',
         opts=['12', '6', '10', '9'],
         hint='List them from 1:11 to 11:11. Then remember AM and PM.',
         sol='The times are 1:11, 2:22, 3:33, 4:44, 5:55 and 11:11. 6:66 and higher are not times, and 10:00 or 12:22 have different digits. That is 6 in each half of the day, so 12 in a whole day.'),
    dict(ch='1+10', scen='5-digit numbers whose digits add up to 2',
         stem='How many 5-digit numbers have digits that add up to 2?',
         opts=['5', '4', '6', '10'],
         hint='The first digit cannot be 0. Is it 1 or 2?',
         sol='If the first digit is 2, the number is 20,000. If it is 1, the other 1 can be in any of the 4 other places: 11,000, 10,100, 10,010, 10,001. 1 + 4 = 5.'),
    dict(ch='3+9', scen='train stops after three quarters of a journey',
         stem='A train journey takes 3 hours 20 minutes and starts at 9:40 AM. The train stops for water when 3/4 of the journey time has passed. At what time does it stop?',
         opts=['12:10 PM', '12:40 PM', '11:40 AM', '1:00 PM'],
         hint='Change 3 hours 20 minutes into minutes.',
         sol='3 hours 20 minutes = 200 minutes. 3/4 of 200 = 150 minutes = 2 hours 30 minutes. 9:40 AM + 2 h 30 min = 12:10 PM.'),
    dict(ch='5+6', scen='cube with net area 96 cm² · total length of its edges',
         stem='The net of a cube has an area of 96 cm². Mayank makes a wire model of the same cube, using wire only along the edges. How much wire does he need?',
         opts=['48 cm', '24 cm', '96 cm', '64 cm'],
         hint='Find the area of one face, then the length of one edge.',
         sol='Each of the 6 faces is 96 ÷ 6 = 16 cm², so each edge is 4 cm. A cube has 12 edges: 12 × 4 = 48 cm.'),
]
