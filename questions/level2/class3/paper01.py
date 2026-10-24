# AMO Level-2 · Class 3 · Practice Paper 1
# Each question: ch (chapter or star pair), scen (unique scenario key), stem, opts (correct answer FIRST),
# hint, sol, optional fig. fixed=True keeps the option order, with ans = index of the correct option.


def net_cross():
    """Cross-shaped cube net: 1 on top of 3, row 2 3 4 5, 6 under 3."""
    s = 40
    cells = {1: (1, 0), 2: (0, 1), 3: (1, 1), 4: (2, 1), 5: (3, 1), 6: (1, 2)}
    prims = []
    for n, (c, r) in cells.items():
        prims += [('rect', 10 + c * s, 10 + r * s, s, s, 'yellow'), ('text', 10 + c * s + s / 2, 10 + r * s + s / 2, str(n), 16)]
    return prims


def sym_shapes():
    return [('rect', 0, 20, 60, 60, 'blue'), ('text', 30, 100, 'P', 13),
            ('rect', 85, 30, 90, 40, 'green'), ('text', 130, 100, 'Q', 13),
            ('poly', [(230, 15), (200, 80), (260, 80)], 'pink'), ('text', 230, 100, 'R', 13),
            ('poly', [(290, 80), (300, 20), (360, 20), (350, 80)], 'peach'), ('text', 325, 100, 'S', 13)]


def l_shape():
    s = 30
    pts = [(10, 10), (10 + s, 10), (10 + s, 10 + 2 * s), (10 + 2 * s, 10 + 2 * s), (10 + 2 * s, 10 + 3 * s), (10, 10 + 3 * s)]
    prims = [('poly', pts, 'yellow')]
    prims += [('line', 10, 10 + s, 10 + s, 10 + s, True), ('line', 10, 10 + 2 * s, 10 + s, 10 + 2 * s, True),
              ('line', 10 + s, 10 + 2 * s, 10 + s, 10 + 3 * s, True)]
    prims += [('text', 10 + s / 2, 0, '5 cm', 11)]
    return prims


QUESTIONS = [
    # ---------------- Part 1 · Number System
    dict(ch='1', scen='smallest 4-digit number with different digits and digit sum 10',
         stem='Kavya wants the smallest 4-digit number whose four digits are all different and add up to 10. Which number is it?',
         opts=['1027', '1009', '1036', '1234'],
         hint='Keep the first digits as small as possible, but no digit may repeat.',
         sol='Start with 1 and 0. The last two digits must add up to 9 and be different from 1 and 0, and from each other. The smallest tens digit allowed is 2, so the ones digit is 7. The number is 1027. (1009 repeats 0; 1036 and 1234 are bigger.)'),
    dict(ch='1', scen='difference between place values of the two sevens in 7474',
         stem='In the number 7474, what is the difference between the place values of the two 7s?',
         opts=['6930', '0', '7070', '6993'],
         hint='Place value depends on the position of the digit; face value does not.',
         sol='The first 7 is in the thousands place: 7000. The second 7 is in the tens place: 70. The difference is 7000 − 70 = 6930. (0 is the difference of their face values.)'),
    dict(ch='1', scen='adding XXIX and XIV in Roman numerals',
         stem='Arjun adds XXIX and XIV. How is his answer written in Roman numerals?',
         opts=['XLIII', 'XXXXIII', 'XLII', 'LXIII'],
         hint='Change both to our numbers first, then change the answer back.',
         sol='XXIX = 29 and XIV = 14. 29 + 14 = 43. 40 is written XL (10 before 50), so 43 is XLIII. A Roman numeral never repeats X four times, so XXXXIII is wrong.'),
    dict(ch='1', scen='number in the 4000s with hundreds double the ones and digit sum 13',
         stem='Rohan\'s number is between 4000 and 5000. Its tens digit is 0. Its hundreds digit is double its ones digit. Its digits add up to 13. What is the number?',
         opts=['4603', '4306', '4630', '4036'],
         hint='The thousands digit is 4, so the other digits add up to 9.',
         sol='The thousands digit is 4, so hundreds + ones = 13 − 4 − 0 = 9. The hundreds digit is double the ones digit, so ones = 3 and hundreds = 6. The number is 4603.'),

    # ---------------- Part 2 · Operations
    dict(ch='2', scen='library books lent returned and bought',
         stem='A library had 5230 books. It lent out 1875 books and got back 948 of them. Then it bought 600 new books. How many books are in the library now?',
         opts=['4903', '4303', '5003', '4803'],
         hint='Take away the books lent, then add the books returned and bought.',
         sol='5230 − 1875 = 3355. 3355 + 948 = 4303. 4303 + 600 = 4903.'),
    dict(ch='2', scen='12 boxes of 8 erasers minus 9 packets of 7 sold',
         stem='A shop has 12 boxes with 8 erasers in each. It sells 9 packets with 7 erasers in each. How many erasers are left?',
         opts=['33', '43', '23', '37'],
         hint='Use the 12 times table and the 9 times table.',
         sol='12 × 8 = 96 erasers. 9 × 7 = 63 erasers sold. 96 − 63 = 33 left.'),
    dict(ch='2', scen='744 laddoos in boxes of 6 and cartons of 4 boxes',
         stem='A sweet shop packs 744 laddoos in boxes of 6. Then it puts the boxes in cartons, 4 boxes to a carton. How many cartons does it fill?',
         opts=['31', '124', '30', '32'],
         hint='First find the number of boxes.',
         sol='744 ÷ 6 = 124 boxes. 124 ÷ 4 = 31 cartons.'),
    dict(ch='2', scen='50 children in teams of 7 · children needed to fill the last team',
         stem='At a sports day, 50 children make teams of 7 for a game. How many more children must join so that every team is full?',
         opts=['6', '1', '7', '8'],
         hint='Divide 50 by 7 and look at the remainder.',
         sol='50 ÷ 7 = 7 teams, remainder 1. The 1 child starts an 8th team, which needs 7 children. So 7 − 1 = 6 more must join. (Check: 8 × 7 = 56 = 50 + 6.)'),

    # ---------------- Part 3 · Fractions
    dict(ch='3', scen='40 marbles · three-eighths red two-eighths blue rest green',
         stem='Ira has 40 marbles. 3/8 of them are red, 2/8 are blue and the rest are green. How many marbles are green?',
         opts=['15', '25', '10', '5'],
         hint='First find 1/8 of 40.',
         sol='1/8 of 40 is 5. Red and blue together are 3/8 + 2/8 = 5/8, so green is 3/8. 3 × 5 = 15 green marbles.'),
    dict(ch='3', scen='cake eaten by two children in ninths · fraction left',
         stem='Meena eats 2/9 of a cake and Rahul eats 4/9 of it. What fraction of the cake is left?',
         opts=['3/9', '6/9', '2/9', '3/18'],
         hint='The whole cake is 9/9.',
         sol='Together they eat 2/9 + 4/9 = 6/9. The whole cake is 9/9, so 9/9 − 6/9 = 3/9 is left. Only the top numbers are added; the bottom stays 9.'),
    dict(ch='3', scen='17 slices from pizzas cut in sixths · fraction left over',
         stem='Each pizza is cut into 6 equal slices. Kabir\'s family eats 17 slices, opening as few pizzas as they can. What fraction of a pizza is left over?',
         opts=['1/6', '5/6', '17/6', '2/6'],
         hint='How many pizzas are needed for 17 slices?',
         sol='2 pizzas give only 12 slices, so they open 3 pizzas: 18 slices. 18 − 17 = 1 slice is left, which is 1/6 of a pizza.'),

    # ---------------- Part 4 · Geometry
    dict(ch='5', scen='faces plus edges plus corners of a cube',
         stem='Ishaan counts the faces, the edges and the corners (vertices) of a cube. He adds the three numbers. What total does he get?',
         opts=['26', '24', '20', '18'],
         hint='A cube has 6 faces.',
         sol='A cube has 6 faces, 12 edges and 8 vertices. 6 + 12 + 8 = 26.'),
    dict(ch='5', scen='cross-shaped cube net · face opposite 2',
         fig=drawing(180, 140, net_cross()),
         stem='Diya folds this net into a cube. Which number is on the face opposite the face with 2?',
         opts=['4', '3', '5', '6'],
         hint='In a row of four squares, faces with one square between them are opposite.',
         sol='In the row 2, 3, 4, 5, the faces 2 and 4 have one square between them, so they become opposite. (3 is opposite 5, and 1 is opposite 6.)'),
    dict(ch='5', scen='which shape has exactly one line of symmetry',
         fig=drawing(360, 105, sym_shapes()),
         stem='Sana folds each shape to find its lines of symmetry. Which shape has exactly one line of symmetry?',
         opts=['P', 'Q', 'R', 'S'], fixed=True, ans=2,
         hint='Try folding each shape along every possible line.',
         sol='P is a square: 4 lines. Q is a rectangle: 2 lines. R is a triangle with two equal sides: only the up-down fold through its top works, so 1 line. S leans to one side, so no fold makes its two halves match: 0 lines. So R.'),

    # ---------------- Part 5 · Mensuration
    dict(ch='6', scen='wire three times round a 12 m by 8 m garden',
         stem='A garden is a rectangle 12 m long and 8 m wide. Vivaan puts wire 3 times all the way round it. How much wire does he use?',
         opts=['120 m', '40 m', '96 m', '60 m'],
         hint='Find the distance round the garden once.',
         sol='Once round: 12 + 8 + 12 + 8 = 40 m. Three times round: 40 + 40 + 40 = 120 m.'),
    dict(ch='6', scen='two bags of rice in kg and g · total in grams',
         stem='One bag has 3 kg 250 g of rice and another has 1 kg 900 g. How many grams of rice are there altogether?',
         opts=['5150 g', '4150 g', '5015 g', '1350 g'],
         hint='1 kg = 1000 g.',
         sol='3 kg 250 g = 3250 g. 1 kg 900 g = 1900 g. 3250 + 1900 = 5150 g.'),
    dict(ch='6', scen='three 2-litre jugs poured into 250 mL glasses',
         stem='Gauri has 3 jugs of juice. Each jug holds 2 L. She fills glasses that hold 250 mL each. How many glasses can she fill?',
         opts=['24', '12', '6', '30'],
         hint='How many 250 mL glasses make 1 L?',
         sol='1 L = 1000 mL = 4 glasses of 250 mL. The jugs hold 3 × 2 = 6 L. 6 × 4 = 24 glasses.'),

    # ---------------- Part 6 · Applied Mathematics
    dict(ch='9', scen='train leaves 9:45 AM · journey 3 h 35 min',
         stem='A train leaves at 9:45 AM. The journey takes 3 hours 35 minutes. At what time does the train arrive?',
         opts=['1:20 PM', '12:20 PM', '1:20 AM', '2:20 PM'],
         hint='Add the hours first, then the minutes.',
         sol='9:45 AM + 3 hours = 12:45 PM. 12:45 PM + 35 minutes: 15 minutes takes it to 1:00 PM, and 20 more makes 1:20 PM.'),
    dict(ch='9', scen='15 August is Friday · day on 2 September',
         stem='In one year, 15 August is a Friday. August has 31 days. What day of the week is 2 September?',
         opts=['Tuesday', 'Wednesday', 'Monday', 'Thursday'],
         hint='Add 7 days at a time from 15 August.',
         sol='15, 22 and 29 August are Fridays. 29 August + 7 days = 5 September, also a Friday. 2 September is 3 days before that: Thursday, Wednesday, Tuesday. So it is a Tuesday.'),
    dict(ch='9', scen='4 notebooks at ₹35 and 3 pens at ₹12 · change from ₹200',
         stem='Lata buys 4 notebooks at ₹35 each and 3 pens at ₹12 each. She pays with a ₹200 note. How much change does she get?',
         opts=['₹24', '₹34', '₹176', '₹14'],
         hint='Find each cost, add them, then subtract from ₹200.',
         sol='Notebooks: 35 × 4 = ₹140. Pens: 12 × 3 = ₹36. Total ₹176. Change: 200 − 176 = ₹24.'),
    dict(ch='9', scen='hours from 8 PM Monday to 6 AM Wednesday',
         stem='Om\'s uncle reaches their house at 8 PM on Monday and leaves at 6 AM on Wednesday. How many hours does he stay?',
         opts=['34 hours', '10 hours', '22 hours', '32 hours'],
         hint='Break the time into: Monday night, all of Tuesday, Wednesday morning.',
         sol='8 PM to midnight on Monday: 4 hours. All of Tuesday: 24 hours. Midnight to 6 AM on Wednesday: 6 hours. 4 + 24 + 6 = 34 hours.'),

    # ---------------- Part 7 · Mathematical Reasoning
    dict(ch='10', scen='pattern with differences 4 6 8 10',
         fig=cards([2, 6, 12, 20, 30, '?']),
         stem='Find the rule in this pattern. Which number comes next?',
         opts=['42', '40', '36', '44'],
         hint='Look at the differences between neighbours.',
         sol='The differences are 4, 6, 8 and 10, going up by 2. The next difference is 12: 30 + 12 = 42.'),
    dict(ch='10', scen='cryptarithm AA plus AA equals 1B4',
         fig=equations([['AA', '+', 'AA', '=', '1B4']], size=34),
         stem='In this sum, each letter stands for one digit. What digit is B?',
         opts=['5', '4', '7', '1'],
         hint='The ones digits give A + A, which must end in 4.',
         sol='A + A ends in 4, so A is 2 or 7. 22 + 22 = 44 is too small. 77 + 77 = 154, which fits 1B4. So B = 5.'),
    dict(ch='10', scen='working backwards · times 4 minus 9 divide by 3 gives 13',
         stem='Priya thinks of a number. She multiplies it by 4, takes away 9 and then divides by 3. She gets 13. What was her number?',
         opts=['12', '13', '9', '15'],
         hint='Undo each step, starting from the last one.',
         sol='Undo ÷ 3: 13 × 3 = 39. Undo − 9: 39 + 9 = 48. Undo × 4: 48 ÷ 4 = 12. Check: 12 × 4 = 48, 48 − 9 = 39, 39 ÷ 3 = 13.'),
    dict(ch='10', scen='3-digit numbers with odd digits going up',
         stem='How many 3-digit numbers have all odd digits that go up from left to right, like 159?',
         opts=['10', '6', '15', '125'],
         hint='The digits come from 1, 3, 5, 7, 9. List them by the first digit.',
         sol='Starting with 1: 135, 137, 139, 157, 159, 179 (6). Starting with 3: 357, 359, 379 (3). Starting with 5: 579 (1). Total 6 + 3 + 1 = 10.'),

    # ---------------- Section II · Star Questions
    dict(ch='1+10', scen='1010 1020 1040 1080 pattern',
         fig=cards([1010, 1020, 1040, 1080, 1160, '?'], size=44),
         stem='Look at how much is added each time. Which number comes next?',
         opts=['1320', '1240', '1280', '1640'],
         hint='The amount added doubles each time.',
         sol='The pattern adds 10, 20, 40 and 80. Next it adds 160: 1160 + 160 = 1320.'),
    dict(ch='3+10', scen='twelfths pattern adding 2 3 4 5 twelfths',
         fig=cards(['1/12', '3/12', '6/12', '10/12', '?'], size=44),
         stem='The fractions follow a pattern. Which fraction comes next?',
         opts=['15/12', '14/12', '11/12', '15/24'],
         hint='Look at how many twelfths are added each time.',
         sol='The pattern adds 2/12, 3/12 and 4/12. Next it adds 5/12: 10/12 + 5/12 = 15/12.'),
    dict(ch='9+10', scen='31-day month with five Mondays and Tuesdays but four Sundays',
         stem='A month has 31 days. It has five Mondays and five Tuesdays but only four Sundays. On what day is the 1st of the month?',
         opts=['Monday', 'Sunday', 'Tuesday', 'Saturday'],
         hint='31 days = 4 weeks and 3 extra days. The first 3 days of the month happen five times.',
         sol='4 weeks is 28 days, so the days of the 1st, 2nd and 3rd happen five times. These must include Monday and Tuesday but not Sunday. If the 1st is Monday, the three days are Monday, Tuesday, Wednesday. If the 1st were Sunday, there would be five Sundays.'),
    dict(ch='1+9', scen='₹3450 with fewest ₹500 ₹100 and ₹10 notes',
         stem='Yash must pay ₹3450 using only ₹500, ₹100 and ₹10 notes. He uses as few notes as he can. How many notes does he use?',
         opts=['15', '12', '345', '13'],
         hint='Use as many ₹500 notes as possible first.',
         sol='₹3450 = 6 notes of ₹500 (₹3000) + 4 notes of ₹100 (₹400) + 5 notes of ₹10 (₹50). 6 + 4 + 5 = 15 notes.'),
    dict(ch='5+6', scen='L shape of four squares of side 5 cm · perimeter',
         fig=drawing(80, 100, l_shape()),
         stem='Nisha joins 4 squares, each with sides of 5 cm, to make this L shape. What is the perimeter of the L shape?',
         opts=['50 cm', '80 cm', '40 cm', '60 cm'],
         hint='Count how many 5 cm sides are on the outside.',
         sol='Going round the outside there are 10 sides of 5 cm: 3 on the left, 1 on the top, 2 down the right of the tall part, 1 on the right of the bottom square, 2 along the bottom and 1 step across. 10 × 5 = 50 cm. (80 cm counts all 16 sides, including the ones inside.)'),
]
