# AMO Level-2 · Class 1 · Practice Paper 7  (format: see paper01.py)


def wall(rows, w=50, h=30):
    prims = []
    n = len(rows[-1])
    for r, row in enumerate(rows):
        off = (n - len(row)) * w / 2
        for k, v in enumerate(row):
            x, y = off + k * w, r * h
            if v == '?':
                prims += [('rect', x, y, w, h, 'white'), ('qbox', x + w / 2, y + h / 2, 22)]
            else:
                prims += [('rect', x, y, w, h, 'peach'), ('text', x + w / 2, y + h / 2 + 1, str(v), 15)]
    return prims


def l_grid():
    s = 30
    prims = []
    for r in range(3):
        for c in range(4):
            if c == 0 or r == 2:
                prims.append(('rect', 5 + c * s, 5 + r * s, s, s, 'blue'))
            else:
                prims.append(('rect', 5 + c * s, 5 + r * s, s, s, None, True))
    return prims


def row_squares(n, x0, s=24):
    return [('rect', x0 + k * s, 10, s, s, 'yellow') for k in range(n)]


QUESTIONS = [
    # ---------------- Part 1 · Number System
    dict(ch='1', scen='number names from 11 to 19 ending in teen',
         stem='Look at the number names for 11 to 19. How many of these names end in "teen"?',
         opts=['7', '9', '8', '6'],
         hint='Say the names: eleven, twelve, thirteen, …',
         sol='Eleven and twelve do not end in "teen". Thirteen, fourteen, fifteen, sixteen, seventeen, eighteen and nineteen do. That is 7 names.'),
    dict(ch='1', scen='boxes of ten crayons · giving away a box and loose crayons',
         fig=objects([{'items': ['📦'] * 6, 'cols': 6, 'label': '6 boxes of 10 crayons'}, {'items': ['🖍️'] * 8, 'cols': 4, 'label': '8 loose crayons'}], item=30),
         stem='Meera has these crayons. She gives away 1 box and 3 loose crayons. How many crayons does she have left?',
         opts=['55', '65', '58', '45'],
         hint='Work with the boxes (tens) and the loose crayons (ones) separately.',
         sol='She has 6 tens and 8 ones, which is 68. Giving away 1 box leaves 5 tens. Giving away 3 loose crayons leaves 5 ones. So she has 55 crayons.', place_value_ok=True),
    dict(ch='1', scen='tens digit of the number just after 89',
         stem='Which digit is in the tens place of the number that comes just after 89?',
         opts=['9', '8', '0', '1'],
         hint='First find the number that comes just after 89.',
         sol='The number just after 89 is 90. Its tens digit is 9 and its ones digit is 0.'),
    dict(ch='1', scen='largest number whose digits add up to 5',
         stem='What is the largest 2-digit number whose two digits add up to 5?',
         opts=['50', '41', '32', '95'],
         hint='Make the tens digit as big as you can.',
         sol='The tens digit can be at most 5, because the digits must add up to 5. Then the ones digit is 0. So the largest number is 50.'),
    dict(ch='1', scen='which of 46 and 53 is closer to 50',
         stem='Which number is closer to 50: 46 or 53?',
         opts=['53', '46', 'Both are equally close', '50'],
         hint='Count the steps from each number to 50.',
         sol='From 46 to 50 is 4 steps: 47, 48, 49, 50. From 53 to 50 is 3 steps: 52, 51, 50. So 53 is closer.'),
    dict(ch='1', scen='smallest 2-digit number containing the digit 7',
         stem='What is the smallest 2-digit number that has the digit 7 in it?',
         opts=['17', '70', '7', '27'],
         hint='The 7 does not have to be the tens digit.',
         sol='A 2-digit number with tens digit 1 is the smallest kind. With 7 as the ones digit we get 17. 7 is only a 1-digit number, and 27 and 70 are bigger than 17.'),
    dict(ch='1', scen='2-digit numbers whose digits add up to 3',
         stem='How many 2-digit numbers have digits that add up to 3?',
         opts=['3', '2', '4', '6'],
         hint='The tens digit cannot be 0.',
         sol='Tens digit 1 gives 12. Tens digit 2 gives 21. Tens digit 3 gives 30. That is 3 numbers.'),

    # ---------------- Part 2 · Operations
    dict(ch='2', scen='moving one card between piles to make equal totals',
         fig=objects([{'label': 'Left pile', 'items': ['6', '5', '4'], 'cols': 3}, {'label': 'Right pile', 'items': ['3', '2'], 'cols': 2}], item=40),
         stem='Hari moves one card from the left pile to the right pile. Now both piles add up to the same total. Which card does he move?',
         opts=['5', '6', '4', '3'],
         hint='Find the total of all the cards. Each pile must get half of it.',
         sol='The left pile adds to 15 and the right pile to 5, so all the cards make 20. Each pile must make 10. Moving the 5 gives left 6 + 4 = 10 and right 3 + 2 + 5 = 10.'),
    dict(ch='2', scen='number wall with a missing bottom brick · top 15',
         fig=drawing(160, 95, wall([[15], ['', ''], [2, '?', 3]])),
         stem='In this number wall, each brick is the sum of the two bricks just below it. Which number goes in the empty bottom brick?',
         opts=['5', '10', '4', '6'],
         hint='Try a number and build the wall upwards.',
         sol='Try 5: the middle bricks are 2 + 5 = 7 and 5 + 3 = 8, and the top is 7 + 8 = 15. It works. Trying 4 gives a top of 13, and 6 gives 17.'),
    dict(ch='2', scen='three cards adding up to 20',
         fig=cards([2, 6, 9, 5, 7]),
         stem='Kusum chooses three different cards that add up to exactly 20. Which three cards does she choose?',
         opts=['6, 9 and 5', '9, 5 and 7', '6, 9 and 7', '2, 9 and 7'],
         hint='Add each group carefully.',
         sol='6 + 9 + 5 = 20. The other groups make 9 + 5 + 7 = 21, 6 + 9 + 7 = 22 and 2 + 9 + 7 = 18.'),
    dict(ch='2', scen='three children with more stickers in a chain · total',
         stem='Tanvi has 4 stickers. Raj has 3 more stickers than Tanvi. Mansi has 2 more stickers than Raj. How many stickers do the three children have in all?',
         opts=['20', '9', '13', '16'],
         hint='Find how many each child has, then add.',
         sol='Tanvi has 4. Raj has 4 + 3 = 7. Mansi has 7 + 2 = 9. In all 4 + 7 + 9 = 20 stickers.'),
    dict(ch='2', scen='two dice total 9 one shows 3 more',
         stem='Two dice show a total of 9. One die shows 3 more than the other. Which numbers do the dice show?',
         opts=['3 and 6', '4 and 5', '2 and 7', '1 and 8'],
         hint='A die shows only the numbers 1 to 6.',
         sol='3 and 6 make 9, and 6 is 3 more than 3. 4 and 5 make 9 but differ by only 1. 2 and 7, and 1 and 8, are not possible on dice.'),
    dict(ch='2', scen='pairs of socks with three single socks lost',
         stem='Anaya has 7 pairs of socks. She loses 3 single socks. How many socks does she have now?',
         opts=['11', '4', '14', '10'],
         hint='A pair is 2 socks.',
         sol='7 pairs are 2 + 2 + 2 + 2 + 2 + 2 + 2 = 14 socks. After losing 3, she has 14 − 3 = 11 socks.'),

    # ---------------- Part 3 · Geometry
    dict(ch='5', scen='six-pointed star of two triangles · count triangles',
         fig=drawing(180, 170, [('poly', [(90, 5), (160, 125), (20, 125)], 'pink'), ('poly', [(90, 165), (20, 45), (160, 45)], 'pink'),
                                ('poly', [(90, 5), (160, 125), (20, 125)], None)]),
         stem='Sakshi draws one triangle pointing up and one pointing down to make a star. How many triangles of all sizes can you find?',
         opts=['8', '6', '2', '7'],
         hint='Count the small points of the star, then the two big triangles.',
         sol='Each of the 6 points of the star is a small triangle. The two big triangles she drew make 2 more. 6 + 2 = 8.'),
    dict(ch='5', scen='caterpillar drawn with circles · count circles',
         fig=drawing(230, 90, [('circle', 30, 55, 18, 'green'), ('circle', 60, 55, 18, 'green'), ('circle', 90, 55, 18, 'green'),
                               ('circle', 120, 55, 18, 'green'), ('circle', 150, 55, 18, 'green'), ('circle', 185, 45, 22, 'yellow'),
                               ('circle', 178, 40, 4, 'white'), ('circle', 193, 40, 4, 'white'),
                               ('line', 178, 24, 170, 5), ('line', 193, 24, 201, 5)]),
         stem="Kush draws a caterpillar using only circles and two lines. How many circles of all sizes are in his drawing?",
         opts=['8', '6', '7', '5'],
         hint='Count the body, the head and the small circles on the head.',
         sol='The body has 5 circles and the head is 1 more circle. The two eyes are 2 small circles. 5 + 1 + 2 = 8 circles.'),
    dict(ch='5', scen='L-shape inside a dotted rectangle · squares still needed',
         fig=drawing(130, 100, l_grid()),
         stem='Gita has made the shaded L-shape out of small squares. How many more small squares does she need to fill the whole dotted rectangle?',
         opts=['6', '12', '5', '7'],
         hint='Count all the boxes in the rectangle, then the shaded ones.',
         sol='The rectangle has 3 rows of 4 boxes: 4 + 4 + 4 = 12. The L-shape uses 6 boxes. She needs 12 − 6 = 6 more.'),
    dict(ch='5', scen='joining four corner dots with straight lines',
         fig=drawing(110, 110, [('dot', 10, 10, 5), ('dot', 100, 10, 5), ('dot', 10, 100, 5), ('dot', 100, 100, 5)]),
         stem='Ojas joins every pair of these four dots with a straight line. How many lines does he draw?',
         opts=['6', '4', '8', '5'],
         hint='Do not forget the lines that go from corner to corner across the middle.',
         sol='There are 4 lines round the outside, making a square. There are also 2 lines across the middle, from corner to opposite corner. 4 + 2 = 6 lines.'),

    # ---------------- Part 4 · Applied Mathematics
    dict(ch='9', scen='two months after the month right after October',
         stem='Which month is 2 months after the month that comes right after October?',
         opts=['January', 'December', 'February', 'March'],
         hint='After December, the months start again with January.',
         sol='The month right after October is November. Two months after November: December, then January.'),
    dict(ch='9', scen='paying for a ₹7 pen with ₹5 coins · change',
         stem='A pen costs ₹7. Rahul pays using only ₹5 coins, giving as few coins as he can. How much change does he get back?',
         opts=['₹3', '₹2', '₹8', '₹5'],
         hint='One ₹5 coin is not enough. How many does he need?',
         sol='One ₹5 coin is less than ₹7, so he gives two coins: ₹5 + ₹5 = ₹10. His change is ₹10 − ₹7 = ₹3.'),
    dict(ch='9', scen='1st is Wednesday · day of the 10th',
         stem='The 1st of a month is a Wednesday. On which day is the 10th of that month?',
         opts=['Friday', 'Thursday', 'Saturday', 'Wednesday'],
         hint='The 8th is 7 days after the 1st.',
         sol='The 8th is 7 days after the 1st, so it is also a Wednesday. The 9th is Thursday and the 10th is Friday.'),
    dict(ch='9', scen='groups of notes and coins worth exactly ₹20',
         fig=money([{'label': 'P', 'items': [('note', 20)]}, {'label': 'Q', 'items': [('coin', 5), ('coin', 5), ('coin', 5), ('coin', 5)]},
                    {'label': 'R', 'items': [('coin', 10), ('coin', 10)]}, {'label': 'S', 'items': [('note', 10), ('coin', 2), ('coin', 2), ('coin', 2), ('coin', 2)]}]),
         stem='How many of the groups P, Q, R and S are worth exactly ₹20?',
         opts=['3', '4', '2', '1'],
         hint='Add up each group.',
         sol='P is ₹20. Q is ₹5 + ₹5 + ₹5 + ₹5 = ₹20. R is ₹10 + ₹10 = ₹20. S is ₹10 + ₹2 + ₹2 + ₹2 + ₹2 = ₹18. So 3 groups are worth ₹20.'),

    # ---------------- Part 5 · Mathematical Reasoning
    dict(ch='10', scen='counting back by fives from 50 · sixth number',
         stem='Rohit counts back by 5s, starting at 50. What is the 6th number he says?',
         opts=['25', '20', '30', '35'],
         hint='50 is the 1st number he says.',
         sol='He says 50, 45, 40, 35, 30, 25. The 6th number is 25.'),
    dict(ch='10', scen='number name cards with one wrong match',
         stem='Three of these cards match a number name with the right number. Which card is the odd one out?',
         opts=['thirteen – 31', 'eleven – 11', 'twelve – 12', 'fourteen – 14'],
         hint='Write each number name as a number.',
         sol='Eleven is 11, twelve is 12 and fourteen is 14. Thirteen is 13, not 31. So that card is the odd one out.'),
    dict(ch='10', scen='two children jumping by fours and threes · next shared number',
         stem='Kavya starts at 3 and jumps 4 each time: 3, 7, 11 and so on. Neel starts at 4 and jumps 3 each time: 4, 7, 10 and so on. After 7, which is the next number they both land on?',
         opts=['19', '15', '16', '22'],
         hint='Write both lists a little further.',
         sol='Kavya lands on 3, 7, 11, 15, 19, 23. Neel lands on 4, 7, 10, 13, 16, 19. After 7, the next number in both lists is 19.'),
    dict(ch='10', scen='in and out table that adds three',
         fig=table(['In', 'Out'], [['2', '5'], ['4', '7'], ['6', '9'], ['9', '?']], widths=[80, 80]),
         stem='A number machine follows the same rule every time. What number comes out when 9 goes in?',
         opts=['12', '11', '10', '18'],
         hint='Compare each In number with its Out number.',
         sol='Each Out number is 3 more than the In number: 2 → 5, 4 → 7, 6 → 9. So 9 → 9 + 3 = 12.'),

    # ---------------- Section II · Star Questions
    dict(ch='1+10', scen='counting in tens from 6 · digits adding to 10',
         stem='Prachi counts in tens starting at 6: 6, 16, 26 and so on. Which number that she says has digits that add up to 10?',
         opts=['46', '36', '64', '56'],
         hint='Every number she says ends in 6.',
         sol='Every number she says has ones digit 6. To make 10, the tens digit must be 4, since 4 + 6 = 10. So the number is 46. 64 has the right digits but she never says it.'),
    dict(ch='5+10', scen='rows of squares · corners on the outline of figure 10',
         fig=drawing(260, 50, row_squares(1, 0) + row_squares(2, 50) + row_squares(3, 125) +
                     [('text', 12, 48, 'Fig 1', 10), ('text', 74, 48, 'Fig 2', 10), ('text', 161, 48, 'Fig 3', 10)]),
         stem='Each figure is a row of squares joined together. How many corners does the outline of Figure 10 have?',
         opts=['4', '40', '20', '22'],
         hint='Look only at the outside edge of each figure.',
         sol='Squares joined in a row always make a rectangle. Figures 1, 2 and 3 all have an outline with 4 corners. Figure 10 is also a long rectangle, so its outline has 4 corners.'),
    dict(ch='9+10', scen='1st is Wednesday · date of the third Friday',
         stem='The 1st of a month is a Wednesday. On which date is the third Friday of that month?',
         opts=['17th', '10th', '15th', '24th'],
         hint='Find the date of the first Friday.',
         sol='The 1st is Wednesday, so the first Friday is the 3rd. Fridays come every 7 days: 3rd, 10th, 17th. The third Friday is the 17th.'),
    dict(ch='1+9', scen='₹1 coins needed to match six ₹10 notes',
         stem='Asha has six ₹10 notes. Ravi has four ₹10 notes and thirteen ₹1 coins. How many more ₹1 coins does Ravi need to have as much money as Asha?',
         opts=['7', '3', '13', '17'],
         hint='Write each amount as tens and ones.',
         sol='Asha has 6 tens, which is ₹60. Ravi has 4 tens and 13 ones, which is 5 tens and 3 ones, or ₹53. From 53 to 60 is 7 more ones, so he needs 7 more ₹1 coins.', place_value_ok=True),
    dict(ch='2+5', scen='corners of four triangles compared with two squares',
         stem='Leena draws 4 triangles. Kabir draws 2 squares. How many more corners are there in Leena\'s drawing than in Kabir\'s?',
         opts=['4', '2', '12', '8'],
         hint='Find the total corners in each drawing first.',
         sol="Leena's 4 triangles have 3 + 3 + 3 + 3 = 12 corners. Kabir's 2 squares have 4 + 4 = 8 corners. 12 − 8 = 4 more."),
]
