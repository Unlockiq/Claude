# AMO Level-2 · Class 3 · Practice Paper 2  (format: see paper01.py)


def hexagon():
    import math
    pts = [(70 + 55 * math.cos(math.radians(60 * k)), 65 + 55 * math.sin(math.radians(60 * k))) for k in range(6)]
    return [('poly', pts, 'yellow')]


def nets():
    s = 18
    layouts = {
        'P': [(1, 0), (0, 1), (1, 1), (2, 1), (3, 1), (1, 2)],
        'Q': [(0, 0), (0, 1), (1, 1), (2, 1), (3, 1), (3, 2)],
        'R': [(0, 0), (1, 0), (2, 0), (0, 1), (1, 1), (2, 1)],
        'S': [(0, 0), (1, 0), (1, 1), (2, 1), (2, 2), (3, 2)],
    }
    prims = []
    for i, (lab, cells) in enumerate(layouts.items()):
        x0 = i * 100
        for c, r in cells:
            prims.append(('rect', x0 + c * s, 10 + r * s, s, s, 'yellow'))
        prims.append(('text', x0 + 36, 82, lab, 13))
    return prims


QUESTIONS = [
    # ---------------- Part 1 · Number System
    dict(ch='1', scen='largest 4-digit number with different digits adding to 12',
         stem='What is the largest 4-digit number whose digits are all different and add up to 12?',
         opts=['9210', '9300', '9201', '8310'],
         hint='Put 9 first. Then the other three digits must add up to 3.',
         sol='Start with 9. The other three different digits must add up to 3, so they are 2, 1 and 0. Largest order: 9210. (9300 repeats 0.)'),
    dict(ch='1', scen='6 thousands 15 hundreds 4 tens 23 ones',
         stem='Which number is 6 thousands, 15 hundreds, 4 tens and 23 ones?',
         opts=['7563', '61543', '6563', '7543'],
         hint='15 hundreds is 1500 and 23 ones is 23.',
         sol='6000 + 1500 + 40 + 23 = 7563.'),
    dict(ch='1', scen='largest of four Roman numerals in the forties',
         stem='Which of these Roman numerals stands for the largest number?',
         opts=['XLIX', 'XLVIII', 'XLVI', 'XXXIX'],
         hint='The longest numeral is not always the largest.',
         sol='XLIX = 40 + 9 = 49. XLVIII = 48. XLVI = 46. XXXIX = 39. The largest is XLIX.'),
    dict(ch='1', scen='numbers between 3000 and 4000 from digits 3 0 7 5',
         stem='Asha uses each of the digits 3, 0, 7 and 5 once to make 4-digit numbers. How many of her numbers are between 3000 and 4000?',
         opts=['6', '24', '4', '3'],
         hint='The thousands digit must be 3.',
         sol='The thousands digit must be 3. The other three digits 0, 7, 5 can be arranged in 6 ways: 3057, 3075, 3507, 3570, 3705, 3750.'),

    # ---------------- Part 2 · Operations
    dict(ch='2', scen='toy factory target of 6000 after two days',
         stem='A factory must make 6000 toys. It made 2465 toys on Monday and 1879 on Tuesday. How many more toys must it make?',
         opts=['1656', '1756', '4344', '1666'],
         hint='Add the two days, then subtract from 6000.',
         sol='2465 + 1879 = 4344. 6000 − 4344 = 1656.'),
    dict(ch='2', scen='48 rows of 7 chairs against 39 rows of 9 chairs',
         stem='Hall A has 48 rows of 7 chairs. Hall B has 39 rows of 9 chairs. Which hall has more chairs, and how many more?',
         opts=['Hall B, 15 more', 'Hall A, 15 more', 'Hall B, 25 more', 'They are equal'],
         hint='Work out 48 × 7 and 39 × 9.',
         sol='48 × 7 = 336. 39 × 9 = 351. Hall B has 351 − 336 = 15 more chairs.'),
    dict(ch='2', scen='936 stickers shared by 8 children · each gives away 9',
         stem='At a camp, 936 stickers are shared equally among 8 children. Then each child gives 9 stickers to a friend. How many stickers does each child have now?',
         opts=['108', '117', '126', '99'],
         hint='First share the stickers.',
         sol='936 ÷ 8 = 117 stickers each. After giving away 9: 117 − 9 = 108.'),
    dict(ch='2', scen='same missing digit in 4? times 6 equals 2?8',
         fig=equations([['4?', '×', '6', '=', '2?8']], size=34),
         stem='Both boxes hide the same digit. Which digit is it?',
         opts=['8', '3', '5', '6'],
         hint='? × 6 must end in 8.',
         sol='? × 6 ends in 8 when ? is 3 or 8. 43 × 6 = 258: the middle digit is 5, not 3. 48 × 6 = 288: the middle digit is 8. So the digit is 8.'),

    # ---------------- Part 3 · Fractions
    dict(ch='3', scen='seven tenths of 50 grapes against four tenths of 80',
         stem='Raj eats 7/10 of 50 grapes. Asha eats 4/10 of 80 grapes. Who eats more, and by how many grapes?',
         opts=['Raj, by 3', 'Asha, by 3', 'Raj, by 30', 'Both eat the same'],
         hint='Find 1/10 of each number first.',
         sol='1/10 of 50 is 5, so Raj eats 7 × 5 = 35. 1/10 of 80 is 8, so Asha eats 4 × 8 = 32. Raj eats 3 more.'),
    dict(ch='3', scen='how many eighths fractions are more than one whole',
         stem='How many of these fractions are more than one whole: 9/8, 7/8, 8/8, 12/8, 3/8?',
         opts=['2', '3', '1', '4'],
         hint='8/8 is exactly one whole.',
         sol='One whole is 8/8. Only fractions with a top number bigger than 8 are more than one whole: 9/8 and 12/8. 8/8 is equal to one whole, not more. So 2.'),
    dict(ch='3', scen='water tank eleven twelfths full · use and refill',
         stem='A tank is 11/12 full. Kunal uses 5/12 of the tank for the garden. Then rain adds 3/12. How full is the tank now?',
         opts=['9/12', '3/12', '19/12', '9/24'],
         hint='Take away first, then add.',
         sol='11/12 − 5/12 = 6/12. 6/12 + 3/12 = 9/12.'),

    # ---------------- Part 4 · Geometry
    dict(ch='5', scen='solid with 5 faces 8 edges 5 vertices',
         stem='Which solid has 5 faces, 8 edges and 5 vertices?',
         opts=['Square pyramid', 'Cube', 'Triangular prism', 'Cone'],
         hint='Think of a solid with a square base and four triangles meeting at the top.',
         sol='A square pyramid has 1 square + 4 triangles = 5 faces, 4 base edges + 4 slanting edges = 8 edges, and 4 base corners + 1 top = 5 vertices. A triangular prism has 5 faces but 9 edges and 6 vertices.'),
    dict(ch='5', scen='lines of symmetry of a regular hexagon',
         fig=drawing(140, 130, hexagon()),
         stem='All six sides of this hexagon are equal and all its corners are the same. In how many ways can Riya fold it so the two halves match exactly?',
         opts=['6', '3', '2', '12'],
         hint='Fold from corner to opposite corner, and from side to opposite side.',
         sol='Folding corner to opposite corner gives 3 lines. Folding from the middle of a side to the middle of the opposite side gives 3 more. 3 + 3 = 6 lines of symmetry.'),
    dict(ch='5', scen='which arrangement of six squares is not a cube net',
         fig=drawing(380, 90, nets()),
         stem='Each shape is made of 6 squares. Which one can NOT be folded into a cube?',
         opts=['P', 'Q', 'R', 'S'], fixed=True, ans=2,
         hint='A cube net cannot have 3 squares in a row on both sides of a fold that would overlap.',
         sol='R is 2 rows of 3. When you fold it, two squares end up on top of each other and two faces of the cube are left open. P, Q and S each fold into a cube.'),

    # ---------------- Part 5 · Mensuration
    dict(ch='6', scen='square with the same perimeter as a 12 cm equal-sided triangle',
         stem='A triangle has 3 equal sides of 12 cm. A square has the same perimeter as the triangle. How long is one side of the square?',
         opts=['9 cm', '12 cm', '36 cm', '8 cm'],
         hint='Find the perimeter of the triangle first.',
         sol='Triangle perimeter: 12 + 12 + 12 = 36 cm. A square has 4 equal sides, so each side is 36 ÷ 4 = 9 cm.'),
    dict(ch='6', scen='4 pieces of 65 cm cut from 3 m 20 cm of ribbon',
         stem='Tara has a ribbon 3 m 20 cm long. She cuts 4 pieces, each 65 cm long. How much ribbon is left?',
         opts=['60 cm', '2 m 60 cm', '55 cm', '1 m 60 cm'],
         hint='Change 3 m 20 cm into centimetres.',
         sol='3 m 20 cm = 320 cm. 4 pieces use 65 × 4 = 260 cm. 320 − 260 = 60 cm left.'),
    dict(ch='6', scen='six equal apples and a 300 g basket weigh 2 kg 100 g',
         stem='A basket with 6 equal apples weighs 2 kg 100 g. The empty basket weighs 300 g. How much does one apple weigh?',
         opts=['300 g', '350 g', '400 g', '1800 g'],
         hint='Take away the basket first.',
         sol='2 kg 100 g = 2100 g. Apples alone: 2100 − 300 = 1800 g. One apple: 1800 ÷ 6 = 300 g.'),

    # ---------------- Part 6 · Applied Mathematics
    dict(ch='9', scen='school day 8:40 to 2:10 with a 35-minute lunch',
         stem='School runs from 8:40 AM to 2:10 PM. Lunch break is 35 minutes. How much time is spent in class?',
         opts=['4 h 55 min', '5 h 30 min', '6 h 5 min', '5 h 5 min'],
         hint='Find the whole school time first.',
         sol='8:40 AM to 1:40 PM is 5 hours, and 1:40 to 2:10 PM is 30 minutes: 5 h 30 min. Taking away 35 minutes lunch: 5 h 30 min − 35 min = 4 h 55 min.'),
    dict(ch='9', scen='days from 20 March to 10 April counting both',
         stem='Siya\'s school play practice runs every day from 20 March to 10 April, both days included. On how many days does she practise?',
         opts=['22', '21', '20', '23'],
         hint='March has 31 days.',
         sol='20 March to 31 March, both included: 31 − 20 + 1 = 12 days. 1 April to 10 April: 10 days. 12 + 10 = 22 days.'),
    dict(ch='9', scen='bus fare for 2 adults and 3 children there and back',
         stem='A bus ticket costs ₹35 for an adult and ₹18 for a child, each way. A family of 2 adults and 3 children go and come back. How much do they pay?',
         opts=['₹248', '₹124', '₹106', '₹212'],
         hint='Find the cost one way, then double it.',
         sol='One way: 2 × 35 = ₹70 and 3 × 18 = ₹54, total ₹124. There and back: 124 + 124 = ₹248.'),
    dict(ch='9', scen='clock gaining 5 minutes every hour from 6 AM',
         stem='Neel\'s clock gains 5 minutes every hour. He sets it right at 6 AM. What time does his clock show at 2 PM the same day?',
         opts=['2:40 PM', '2:05 PM', '2:45 PM', '1:20 PM'],
         hint='Count the hours from 6 AM to 2 PM.',
         sol='From 6 AM to 2 PM is 8 hours. The clock gains 8 × 5 = 40 minutes, so it shows 2:40 PM.'),

    # ---------------- Part 7 · Mathematical Reasoning
    dict(ch='10', scen='pattern where each number is the sum of the two before',
         fig=cards([3, 4, 7, 11, 18, 29, '?']),
         stem='Ananya writes this pattern. Which number should she write next?',
         opts=['47', '40', '45', '58'],
         hint='Look at the two numbers just before each number.',
         sol='Each number is the sum of the two before it: 3 + 4 = 7, 4 + 7 = 11, 7 + 11 = 18, 11 + 18 = 29. Next: 18 + 29 = 47.'),
    dict(ch='10', scen='cryptarithm 4A plus A4 equals 110',
         fig=equations([['4A', '+', 'A4', '=', '110']], size=34),
         stem='The letter A stands for the same digit in both numbers. What is A?',
         opts=['6', '5', '7', '4'],
         hint='Try the ones column: A + 4 must end in 0.',
         sol='A + 4 ends in 0, so A = 6. Check: 46 + 64 = 110.'),
    dict(ch='10', scen='working backwards · half to sister 6 to friend half to brother 9 left',
         stem='Mahi gives half her sweets to her sister and then 6 to a friend. Next she gives half of what is left to her brother. She has 9 left. How many did she start with?',
         opts=['48', '30', '36', '42'],
         hint='Undo the steps from the end.',
         sol='Before the brother: 9 + 9 = 18. Before the friend: 18 + 6 = 24. Before the sister: 24 + 24 = 48.'),
    dict(ch='10', scen='handshakes among 6 friends',
         stem='At a party, 6 friends meet. Each friend shakes hands once with every other friend. How many handshakes are there?',
         opts=['15', '30', '36', '12'],
         hint='The first friend shakes 5 hands, the next shakes 4 new hands, and so on.',
         sol='5 + 4 + 3 + 2 + 1 = 15 handshakes. (30 counts each handshake twice.)'),

    # ---------------- Section II · Star Questions
    dict(ch='1+10', scen='how many times the digit 7 is written from 1 to 100',
         stem='Karan writes all the numbers from 1 to 100. How many times does he write the digit 7?',
         opts=['20', '19', '11', '10'],
         hint='Count 7 in the ones place and 7 in the tens place separately.',
         sol='7 in the ones place: 7, 17, 27, …, 97 makes 10. 7 in the tens place: 70 to 79 makes 10. 77 is counted in both, and it really has two 7s. Total 20.'),
    dict(ch='3+10', scen='elevenths pattern · first fraction more than one whole',
         fig=cards(['2/11', '5/11', '8/11', '…'], size=44),
         stem='The fractions keep growing by the same amount. Which is the first fraction in the pattern that is more than one whole?',
         opts=['14/11', '11/11', '12/11', '13/11'],
         hint='Find how much is added each time.',
         sol='Each step adds 3/11: 2/11, 5/11, 8/11, 11/11, 14/11. 11/11 is exactly one whole, not more. The first one more than a whole is 14/11.'),
    dict(ch='9+10', scen='digital clock times with all digits the same in a day',
         stem='A 12-hour digital clock shows times like 2:22 and 11:11, where all the digits are the same. How many such times are there in one whole day?',
         opts=['12', '6', '10', '9'],
         hint='List them in 12 hours, then remember AM and PM.',
         sol='In 12 hours: 1:11, 2:22, 3:33, 4:44, 5:55 and 11:11, which is 6 times. (6:66 and higher are not real times.) A day has AM and PM, so 6 + 6 = 12.'),
    dict(ch='1+9', scen='25 coins of ₹10 and ₹1 worth ₹142',
         stem='Ravi has 25 coins. Some are ₹10 coins and the rest are ₹1 coins. Together they are worth ₹142. How many ₹10 coins does he have?',
         opts=['13', '14', '12', '11'],
         hint='Try 13: count the ₹1 coins and check the total.',
         sol='With 13 coins of ₹10 (₹130) there are 25 − 13 = 12 coins of ₹1 (₹12). 130 + 12 = ₹142. With 14 coins of ₹10 the total would be 140 + 11 = ₹151.'),
    dict(ch='5+6', scen='total length of all edges of a 6 by 4 by 2 cuboid',
         stem='Pooja makes the frame of a box with straws. The box is 6 cm long, 4 cm wide and 2 cm tall. What total length of straw does she use for all the edges?',
         opts=['48 cm', '12 cm', '24 cm', '96 cm'],
         hint='A box has 12 edges: 4 of each length.',
         sol='A cuboid has 4 edges of each length. 4 × 6 = 24, 4 × 4 = 16, 4 × 2 = 8. 24 + 16 + 8 = 48 cm.'),
]
