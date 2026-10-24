# AMO Level-2 · Class 3 · Practice Paper 8  (format: see paper01.py)


def sym_grid():
    s = 32
    shaded = {(0, 0), (1, 1), (2, 0), (2, 1), (3, 1), (0, 3)}
    prims = []
    for r in range(4):
        for c in range(4):
            prims.append(('rect', 10 + c * s, 10 + r * s, s, s, 'blue' if (r, c) in shaded else 'white'))
    prims.append(('line', 10 + 2 * s, 0, 10 + 2 * s, 20 + 4 * s, True, (192, 40, 40), 2.4))
    return prims


def grid4():
    s = 30
    prims = [('rect', 10, 10, 4 * s, 4 * s, 'yellow')]
    for k in (1, 2, 3):
        prims += [('line', 10 + k * s, 10, 10 + k * s, 10 + 4 * s), ('line', 10, 10 + k * s, 10 + 4 * s, 10 + k * s)]
    return prims


def notched_rect():
    pts = [(10, 10), (130, 10), (130, 58), (106, 58), (106, 82), (10, 82)]
    return [('poly', pts, 'green'), ('text', 70, 0, '10 cm', 10), ('text', -10, 46, '6 cm', 10), ('text', 118, 92, '2 cm', 9)]


QUESTIONS = [
    # ---------------- Part 1 · Number System
    dict(ch='1', scen='odd numbers above 6000 from digits 2 5 6 9',
         fig=cards([2, 5, 6, 9]),
         stem='Prakash makes 4-digit numbers using each card once. How many of his numbers are odd and greater than 6000?',
         opts=['6', '4', '8', '12'],
         hint='The first digit is 6 or 9, and the last digit is 5 or 9.',
         sol='First digit 6: last digit 5 or 9, and the other two digits can swap: 2 × 2 = 4 numbers. First digit 9: last digit must be 5, and the other two can swap: 2 numbers. Total 6.'),
    dict(ch='1', scen='9074 compared with 9740',
         stem='How much less is 9000 + 70 + 4 than 9000 + 700 + 40?',
         opts=['666', '676', '606', '766'],
         hint='Write each one as a number.',
         sol='9000 + 70 + 4 = 9074. 9000 + 700 + 40 = 9740. 9740 − 9074 = 666.'),
    dict(ch='1', scen='Roman numeral halfway between XXIV and XL',
         stem='Which Roman numeral stands for the number exactly halfway between XXIV and XL?',
         opts=['XXXII', 'XXXIV', 'XXVIII', 'XXXI'],
         hint='Change them to our numbers first.',
         sol='XXIV = 24 and XL = 40. Halfway between 24 and 40 is 32 (24 + 8 = 32 = 40 − 8). 32 = XXXII.'),
    dict(ch='1', scen='smallest odd 4-digit number with different digits and 3 in the hundreds place',
         stem='Ayaan wants the smallest odd 4-digit number with all digits different and 3 in the hundreds place. What is it?',
         opts=['1305', '1301', '1035', '1307'],
         hint='Start with 1 and 3, then use the smallest digits that are allowed.',
         sol='Thousands 1, hundreds 3. Tens: smallest unused digit is 0. Ones must be odd and unused: 1 and 3 are used, so 5. The number is 1305. (1301 repeats 1.)'),

    # ---------------- Part 2 · Operations
    dict(ch='2', scen='two farms where B has 1567 fewer mangoes than A',
         stem='Farm A picked 3248 mangoes. Farm B picked 1567 fewer than Farm A. How many mangoes did the two farms pick together?',
         opts=['4929', '4815', '1681', '6496'],
         hint='Find Farm B first.',
         sol='Farm B: 3248 − 1567 = 1681. Together: 3248 + 1681 = 4929.'),
    dict(ch='2', scen='two square flower beds of 12 by 12 and 11 by 11 plants',
         stem='One flower bed has 12 rows of 12 plants. Another has 11 rows of 11 plants. How many plants are there in the two beds?',
         opts=['265', '264', '46', '254'],
         hint='Use the 12 and 11 times tables.',
         sol='12 × 12 = 144. 11 × 11 = 121. 144 + 121 = 265.'),
    dict(ch='2', scen='783 mangoes in 9 baskets · 4 baskets sold',
         stem='At a market, 783 mangoes are shared equally into 9 baskets. A shop sells 4 of the baskets. How many mangoes are in the baskets left?',
         opts=['435', '348', '87', '783'],
         hint='Find the mangoes in one basket.',
         sol='783 ÷ 9 = 87 in each basket. 9 − 4 = 5 baskets are left: 87 × 5 = 435.'),
    dict(ch='2', scen='rows of 6 leave 5 and rows of 8 leave 7 · between 30 and 50',
         stem='Between 30 and 50 children are at a show. In rows of 6, 5 are left over. In rows of 8, 7 are left over. How many children are there?',
         opts=['47', '23', '41', '35'],
         hint='One more child would fill every row of 6 and of 8.',
         sol='With 1 more child, the number would fit rows of 6 and rows of 8 exactly: 24 or 48. So there are 23 or 47 children. Between 30 and 50: 47. Check: 47 = 6 × 7 + 5 and 47 = 8 × 5 + 7.'),

    # ---------------- Part 3 · Fractions
    dict(ch='3', scen='book read in tenths over two days · 45 pages left',
         stem='Rohit reads 3/10 of a book on Monday and 4/10 on Tuesday. He has 45 pages left. How many pages are in the book?',
         opts=['150', '105', '450', '90'],
         hint='What fraction of the book is left?',
         sol='Read: 3/10 + 4/10 = 7/10. Left: 3/10, which is 45 pages. 1/10 is 15 pages, so the book has 150 pages.'),
    dict(ch='3', scen='which fraction sum is not one whole',
         stem='Gita adds four pairs of fractions. Which sum is NOT equal to 1 whole?',
         opts=['3/8 + 4/8', '4/9 + 5/9', '7/12 + 5/12', '6/10 + 4/10'],
         hint='A sum is 1 whole when the top number equals the bottom number.',
         sol='4/9 + 5/9 = 9/9, 7/12 + 5/12 = 12/12, 6/10 + 4/10 = 10/10: all 1 whole. 3/8 + 4/8 = 7/8, which is less than 1 whole.'),
    dict(ch='3', scen='two jugs five twelfths and nine twelfths full poured into one',
         stem='Two equal jugs are 5/12 full and 9/12 full. Bhavna pours both into one empty jug of the same size. How much of a jug spills over?',
         opts=['2/12', '14/12', '4/12', 'None'],
         hint='One jug holds 12/12.',
         sol='Together: 5/12 + 9/12 = 14/12. One jug holds 12/12, so 14/12 − 12/12 = 2/12 spills.'),

    # ---------------- Part 4 · Geometry
    dict(ch='5', scen='edges of a cube compared with a square pyramid',
         stem='How many more edges does a cube have than a square pyramid?',
         opts=['4', '3', '6', '0'],
         hint='A square pyramid has 4 edges round its base and 4 going up to the tip.',
         sol='A cube has 12 edges. A square pyramid has 4 + 4 = 8 edges. 12 − 8 = 4.'),
    dict(ch='5', scen='shade squares to make the dotted line a line of symmetry',
         fig=drawing(150, 150, sym_grid()),
         stem='Yuvraj wants the dotted line to be a line of symmetry. How many more squares must he shade?',
         opts=['4', '5', '3', '8'],
         hint='Each shaded square needs a shaded partner the same distance from the line on the other side.',
         sol='Left side shaded squares: row 1 col 1, row 2 col 2, row 3 cols 1 and 2, row 4 col 2. Their partners on the right are: row 1 col 4 (already shaded), row 2 col 3, row 3 cols 3 and 4, row 4 col 3. So 4 more.'),
    dict(ch='5', scen='squares of all sizes in a 4 by 4 grid',
         fig=drawing(140, 140, grid4()),
         stem='Harsh draws this 4 by 4 grid. How many squares of all sizes can he find in it?',
         opts=['30', '16', '25', '20'],
         hint='Count 1 by 1, 2 by 2, 3 by 3 and 4 by 4 squares.',
         sol='1 by 1: 16. 2 by 2: 9. 3 by 3: 4. 4 by 4: 1. 16 + 9 + 4 + 1 = 30.'),

    # ---------------- Part 5 · Mensuration
    dict(ch='6', scen='walking twice round a 25 m by 15 m field and once more along the length',
         stem='A field is 25 m long and 15 m wide. Tushar walks round it twice and then once more along its length. How far does he walk?',
         opts=['185 m', '160 m', '200 m', '105 m'],
         hint='Once round the field is its perimeter.',
         sol='Once round: 25 + 15 + 25 + 15 = 80 m. Twice: 160 m. Plus one length: 160 + 25 = 185 m.'),
    dict(ch='6', scen='lift for 600 kg with 8 children of 35 kg · adults of 70 kg',
         stem='A lift can carry at most 600 kg. 8 children of 35 kg each get in. How many adults of 70 kg each can still get in?',
         opts=['4', '5', '3', '8'],
         hint='Find how much weight is left after the children.',
         sol='Children: 35 × 8 = 280 kg. Left: 600 − 280 = 320 kg. 4 adults weigh 280 kg; 5 adults would weigh 350 kg, which is too much. So 4.'),
    dict(ch='6', scen='18 L cooler filling 75 cups of 200 mL',
         stem='A cooler holds 18 L of lemon water. Varun fills 75 cups of 200 mL each. How much lemon water is left in the cooler?',
         opts=['3 L', '15 L', '4 L', '2 L'],
         hint='How many 200 mL cups make 1 L?',
         sol='1 L = 1000 mL = 5 cups of 200 mL. 75 cups = 75 ÷ 5 = 15 L. Left: 18 − 15 = 3 L.'),

    # ---------------- Part 6 · Applied Mathematics
    dict(ch='9', scen='shop open in two parts of the day · total hours',
         stem='A shop is open from 9:30 AM to 1:15 PM and again from 4:00 PM to 8:45 PM. For how long is it open in all?',
         opts=['8 h 30 min', '9 h 30 min', '8 h', '11 h 15 min'],
         hint='Find each part separately.',
         sol='9:30 AM to 1:15 PM is 3 h 45 min. 4:00 PM to 8:45 PM is 4 h 45 min. Together 7 h 90 min = 8 h 30 min.'),
    dict(ch='9', scen='days from 18 February to a 25 March birthday',
         stem='Myra\'s birthday is on 25 March. Today is 18 February, in a year when February has 28 days. In how many days is her birthday?',
         opts=['35', '36', '37', '34'],
         hint='Count the days left in February first.',
         sol='From 18 February to 28 February is 10 days. Then 25 more days to 25 March. 10 + 25 = 35 days.'),
    dict(ch='9', scen='₹10 and ₹5 coins · buy a ball · share the rest among 3',
         stem='Deepak has eight ₹10 coins and twelve ₹5 coins. He buys a ball for ₹95. He shares the money left equally among 3 friends. How much does each friend get?',
         opts=['₹15', '₹45', '₹20', '₹35'],
         hint='Find his total money first.',
         sol='8 × 10 = ₹80 and 12 × 5 = ₹60, total ₹140. After the ball: 140 − 95 = ₹45. Each friend: 45 ÷ 3 = ₹15.'),
    dict(ch='9', scen='bus every 25 minutes from 6:10 AM · which time has a bus',
         stem='A bus leaves the stand every 25 minutes, starting at 6:10 AM. At which of these times does a bus leave?',
         opts=['8:15 AM', '8:10 AM', '8:20 AM', '8:25 AM'],
         hint='List the times: 6:10, 6:35, …',
         sol='6:10, 6:35, 7:00, 7:25, 7:50, 8:15, 8:40. So a bus leaves at 8:15 AM.'),

    # ---------------- Part 7 · Mathematical Reasoning
    dict(ch='10', scen='pattern multiplying by 2 and 3 in turn',
         fig=cards([3, 6, 18, 36, 108, '?'], size=40),
         stem='Lavanya\'s pattern uses two rules in turn. Which number comes next?',
         opts=['216', '324', '144', '210'],
         hint='Look at 3 → 6 and then 6 → 18.',
         sol='The rules are × 2, then × 3, in turn: 3 × 2 = 6, 6 × 3 = 18, 18 × 2 = 36, 36 × 3 = 108. Next: 108 × 2 = 216.'),
    dict(ch='10', scen='AB plus 9 equals BA with digit sum 7',
         fig=equations([['AB', '+', '9', '=', 'BA']], size=34),
         stem='A and B are digits that add up to 7. What is the number AB?',
         opts=['34', '43', '25', '16'],
         hint='Adding 9 makes the tens digit go up by 1 and the ones digit go down by 1.',
         sol='Adding 9 = adding 10 and taking 1. So B is 1 more than A. Two digits that add up to 7 and differ by 1: 3 and 4. AB = 34. Check: 34 + 9 = 43.'),
    dict(ch='10', scen='add 15 divide by 4 subtract 2 gives 5',
         stem='Kriti thinks of a number. She adds 15, divides by 4 and then takes away 2. She gets 5. What was her number?',
         opts=['13', '28', '43', '3'],
         hint='Undo the steps from the end.',
         sol='Undo − 2: 5 + 2 = 7. Undo ÷ 4: 7 × 4 = 28. Undo + 15: 28 − 15 = 13.'),
    dict(ch='10', scen='four friends in a row · where Raj sits',
         stem='Four friends sit in a row. Siya sits at the left end. Ira is not at an end. Om sits next to Ira, on her right. Raj does not sit next to Siya. Where does Raj sit?',
         opts=['At the right end', 'Second from the left', 'Third from the left', 'Next to Ira'],
         hint='Ira must be second or third from the left. Try both.',
         sol='If Ira were third, Om would be at the right end and Raj would be second, next to Siya: not allowed. So Ira is second and Om third. Raj sits at the right end.'),

    # ---------------- Section II · Star Questions
    dict(ch='1+10', scen='4-digit numbers with digit sum 35',
         stem='How many 4-digit numbers have digits that add up to 35?',
         opts=['4', '1', '9', '36'],
         hint='The largest digit sum is 9 + 9 + 9 + 9 = 36.',
         sol='35 is 1 less than 36, so three digits are 9 and one digit is 8. The 8 can be in any of the 4 places: 8999, 9899, 9989, 9998. So 4.'),
    dict(ch='3+10', scen='A twelfths minus B twelfths and plus B twelfths',
         fig=equations([['A/12', '+', 'B/12', '=', '11/12'], ['A/12', '−', 'B/12', '=', '3/12']], size=30),
         stem='A and B are whole numbers. What is A?',
         opts=['7', '4', '8', '14'],
         hint='A + B = 11 and A − B = 3.',
         sol='A + B = 11 and A − B = 3. Adding them: A + A = 14, so A = 7 (and B = 4). Check: 7/12 + 4/12 = 11/12 and 7/12 − 4/12 = 3/12.'),
    dict(ch='9+10', scen='library visits every 4 and 6 days from 2 March',
         stem='Amit goes to the library every 4 days and Bela every 6 days. Both went on 2 March. On what date will they next both go?',
         opts=['14 March', '26 March', '8 March', '12 March'],
         hint='Find the first number that is in both the 4 and the 6 times tables.',
         sol='Amit: 2, 6, 10, 14 March. Bela: 2, 8, 14 March. They meet again after 12 days, on 14 March.'),
    dict(ch='1+9', scen='₹2345 using only ₹10 and ₹1 coins · fewest coins',
         stem='Shaurya pays ₹2345 using only ₹10 coins and ₹1 coins. He uses as few coins as he can. How many coins does he use?',
         opts=['239', '2345', '234', '245'],
         hint='How many tens are there in 2345?',
         sol='2345 has 234 tens and 5 ones. He uses 234 coins of ₹10 and 5 coins of ₹1. 234 + 5 = 239 coins.'),
    dict(ch='5+6', scen='rectangle 10 by 6 with a 2 cm square cut from a corner · perimeter',
         fig=drawing(140, 90, notched_rect()),
         stem='Kusum cuts a 2 cm square from one corner of a 10 cm by 6 cm rectangle. What is the perimeter of the shape that is left?',
         opts=['32 cm', '28 cm', '36 cm', '30 cm'],
         hint='The two new edges of the cut replace two pieces of the old edges.',
         sol='The rectangle had perimeter 10 + 6 + 10 + 6 = 32 cm. The cut takes away 2 cm from one side and 2 cm from the next side, but adds two new edges of 2 cm. So the perimeter is still 32 cm.'),
]
