# AMO Level-2 · Class 4 · Practice Paper 1
# Each question: ch (chapter or star pair), scen (unique scenario key), stem, opts (correct answer FIRST),
# hint, sol, optional fig. fixed=True keeps the option order, with ans = index of the correct option.


def pict(rows, em, key, lw=90, step=28):
    """Pictograph: one row of symbols per label, then the key."""
    prims = []
    for i, (lab, n) in enumerate(rows):
        y = 18 + i * 34
        prims += [('rect', 0, y - 15, lw, 30, 'lilac'), ('text', lw / 2, y, lab, 12)]
        prims += [('emoji', em, lw + 20 + k * step, y, 24) for k in range(n)]
    y = 18 + len(rows) * 34 + 6
    prims += [('emoji', em, 14, y, 20), ('text', 40 + len(key) * 3.6, y, '= ' + key, 12)]
    return prims


def l_shape():
    s = 14
    P = lambda x, y: (10 + x * s, 10 + y * s)
    return [('poly', [P(0, 0), P(6, 0), P(6, 3), P(10, 3), P(10, 8), P(0, 8)], 'green'),
            ('text', *P(3, -0.7), '6 cm', 11), ('text', *P(-1.6, 4), '8 cm', 11), ('text', *P(5, 8.8), '10 cm', 11),
            ('text', *P(11.6, 5.5), '5 cm', 11), ('text', *P(8, 3.8), '4 cm', 11), ('text', *P(7.1, 1.3), '3 cm', 11)]


def five_points():
    prims = [('line', 0, 20, 300, 20)]
    for i, lab in enumerate('PQRST'):
        prims += [('dot', 30 + i * 60, 20, 4.5), ('text', 30 + i * 60, 38, lab, 13)]
    return prims


CUBE_NET = [[None, '1', None], ['2', '3', '4'], [None, '5', None], [None, '6', None]]
BLANK_NET = [[None, '', None], ['', '', ''], [None, '', None], [None, '', None]]


QUESTIONS = [
    # ---------------- Part 1 · Number System
    dict(ch='1', scen='smallest 5-digit number with different digits minus largest 4-digit number with different digits',
         stem='Kabir writes the smallest 5-digit number that has five different digits. Ira writes the largest 4-digit number that has four different digits. What is the difference between their numbers?',
         opts=['358', '1', '235', '2,469'],
         hint='The smallest 5-digit number with different digits is not 10,000, and the largest 4-digit one is not 9,999.',
         sol='Kabir\'s number is 10,234 (digits 1, 0, 2, 3, 4). Ira\'s number is 9,876. The difference is 10,234 − 9,876 = 358.'),
    dict(ch='1', scen='adding XLIX and XXVI in Roman numerals',
         stem='Ayaan adds the Roman numerals XLIX and XXVI. Which Roman numeral is the answer?',
         opts=['LXXV', 'LXXIV', 'LXV', 'LXXXV'],
         hint='Change both numerals into numbers first. XL is 40 and IX is 9.',
         sol='XLIX = 40 + 9 = 49 and XXVI = 20 + 6 = 26. 49 + 26 = 75. 75 = 50 + 20 + 5 = LXXV.'),
    dict(ch='1', scen='palindromes between 40,000 and 41,000',
         stem='A palindrome reads the same forwards and backwards, like 23,432. How many palindromes are there between 40,000 and 41,000?',
         opts=['10', '9', '11', '100'],
         hint='The number must start with 4 and 0, so it must end with 0 and 4.',
         sol='A palindrome between 40,000 and 41,000 looks like 4 0 _ 0 4. The middle digit can be 0 to 9: 40,004, 40,104, …, 40,904. That is 10 palindromes.'),

    # ---------------- Part 2 · Operations
    dict(ch='2', scen='hall with 48 rows of 36 chairs and 129 empty',
         stem='A hall has 48 rows with 36 chairs in each row. During a show, 129 chairs are empty and each of the other chairs has one person. How many people are sitting?',
         opts=['1,599', '1,728', '1,609', '1,857'],
         hint='Find the total number of chairs first.',
         sol='Chairs: 48 × 36 = 1,728. People: 1,728 − 129 = 1,599.'),
    dict(ch='2', scen='largest product of two 2-digit numbers from digits 2 3 4 5',
         stem='Tanvi makes two 2-digit numbers using each of the digits 2, 3, 4 and 5 once. She multiplies them. What is the largest product she can get?',
         opts=['2,236', '2,226', '1,728', '1,440'],
         hint='Put the two biggest digits in the tens places. Then try both ways of placing the other two.',
         sol='The tens digits should be 5 and 4. Then 52 × 43 = 2,236 and 53 × 42 = 2,226. The largest product is 2,236.'),
    dict(ch='2', scen='remainder of double a number when divided by 7',
         stem='When Kavya divides a number by 7, the remainder is 3. What is the remainder when she divides double that number by 7?',
         opts=['6', '3', '1', '0'],
         hint='Try a number such as 10, which leaves remainder 3 when divided by 7.',
         sol='The number is some sevens plus 3. Doubling it gives some sevens plus 6, and 6 is less than 7. So the remainder is 6. Example: 10 = 7 + 3, and 20 = 14 + 6.'),

    # ---------------- Part 3 · Fractions & Decimals
    dict(ch='3', scen='₹1,200 with a third on books and a quarter on clothes',
         stem='Rahul has ₹1,200. He spends 1/3 of it on books and 1/4 of it on clothes. How much money is left?',
         opts=['₹500', '₹700', '₹600', '₹400'],
         hint='Find 1/3 of ₹1,200 and 1/4 of ₹1,200 separately.',
         sol='1/3 of ₹1,200 is ₹400. 1/4 of ₹1,200 is ₹300. He spends ₹700, so ₹1,200 − ₹700 = ₹500 is left.'),
    dict(ch='3', scen='second largest of 3/4 5/8 2/3 7/12',
         stem='Which of these fractions is the 2nd largest: 3/4, 5/8, 2/3, 7/12?',
         opts=['2/3', '5/8', '3/4', '7/12'],
         hint='Change them all to twenty-fourths.',
         sol='3/4 = 18/24, 5/8 = 15/24, 2/3 = 16/24 and 7/12 = 14/24. In order from largest: 3/4, 2/3, 5/8, 7/12. The 2nd largest is 2/3.'),
    dict(ch='3', scen='ribbon of 5.2 m with two pieces cut off',
         stem='Shruti has a ribbon 5.2 m long. She cuts off one piece of 1.8 m and another of 2.5 m. How long is the ribbon that is left?',
         opts=['0.9 m', '1.9 m', '4.3 m', '1.1 m'],
         hint='Add the two pieces first.',
         sol='The pieces cut off are 1.8 + 2.5 = 4.3 m. The ribbon left is 5.2 − 4.3 = 0.9 m.'),
    dict(ch='3', scen='quarter of an hour plus a third of an hour in minutes',
         stem='Mohit reads for 1/4 of an hour and then draws for 1/3 of an hour. For how many minutes is he busy altogether?',
         opts=['35 minutes', '25 minutes', '40 minutes', '7 minutes'],
         hint='An hour has 60 minutes.',
         sol='1/4 of 60 minutes is 15 minutes. 1/3 of 60 minutes is 20 minutes. 15 + 20 = 35 minutes.'),

    # ---------------- Part 4 · Geometry
    dict(ch='5', scen='square pyramid glued on a cube · edges of the new solid',
         stem='Ritu glues a square pyramid onto one face of a cube. The square base of the pyramid fits the face exactly. How many edges does the new solid have?',
         opts=['16', '20', '17', '12'],
         hint='The base edges of the pyramid are the same as the edges of the cube face.',
         sol='The cube has 12 edges. The pyramid adds only its 4 slanting edges, because its 4 base edges lie on the cube\'s edges. 12 + 4 = 16. Check: faces 5 + 4 = 9, vertices 8 + 1 = 9, and 9 + 9 − 16 = 2.'),
    dict(ch='5', scen='numbered cube net · face opposite 3',
         fig=grid(CUBE_NET, cell=40),
         stem='This net is folded to make a cube. Which number is on the face opposite the face with 3?',
         opts=['6', '1', '5', '2'],
         hint='In a straight line of squares, faces one square apart become opposite faces.',
         sol='In the column 1, 3, 5, 6, faces with one square between them are opposite: 1 is opposite 5, and 3 is opposite 6. 2 and 4 are opposite each other.'),
    dict(ch='5', scen='line segments between five points on a line',
         fig=drawing(300, 40, five_points()),
         stem='Five points P, Q, R, S and T lie on a straight line. How many different line segments have both end points among these five points?',
         opts=['10', '4', '5', '20'],
         hint='Count the segments that start at P, then those that start at Q, and so on.',
         sol='From P: PQ, PR, PS, PT (4). From Q: QR, QS, QT (3). From R: RS, RT (2). From S: ST (1). 4 + 3 + 2 + 1 = 10.'),

    # ---------------- Part 5 · Mensuration
    dict(ch='6', scen='area of an L-shaped plot with a corner cut away',
         fig=drawing(160, 125, l_shape()),
         stem='What is the area of this shape? All corners are square corners.',
         opts=['68 cm²', '80 cm²', '36 cm²', '56 cm²'],
         hint='Find the area of the full 10 cm by 8 cm rectangle, then take away the missing corner.',
         sol='The full rectangle is 10 × 8 = 80 cm². The missing corner is 4 × 3 = 12 cm². The area is 80 − 12 = 68 cm².'),
    dict(ch='6', scen='2 m path around a 20 m by 15 m garden',
         stem='A garden is 20 m long and 15 m wide. A path 2 m wide runs all round the outside of the garden. What is the area of the path?',
         opts=['156 m²', '140 m²', '456 m²', '70 m²'],
         hint='The garden and the path together make a rectangle 24 m by 19 m.',
         sol='Garden and path together: 24 × 19 = 456 m². Garden: 20 × 15 = 300 m². Path: 456 − 300 = 156 m².'),
    dict(ch='6', scen='wire square of side 15 cm bent into a rectangle 20 cm long',
         stem='Lata bends a wire into a square with sides of 15 cm. She opens it and bends it into a rectangle 20 cm long. What is the area of the rectangle?',
         opts=['200 cm²', '225 cm²', '300 cm²', '100 cm²'],
         hint='The length of the wire stays the same.',
         sol='The wire is 4 × 15 = 60 cm long. The rectangle has length 20 cm, so 2 × 20 = 40 cm is used by the lengths and 20 cm is left for the two widths. Width = 10 cm. Area = 20 × 10 = 200 cm².'),
    dict(ch='6', scen='2 L jug and eight glasses of 175 mL',
         stem='A jug holds 2 L of juice. Mitali pours 8 glasses with 175 mL in each. How much juice is left in the jug?',
         opts=['600 mL', '1 L 400 mL', '400 mL', '825 mL'],
         hint='1 L = 1,000 mL.',
         sol='8 × 175 = 1,400 mL is poured. 2 L = 2,000 mL. 2,000 − 1,400 = 600 mL is left.'),

    # ---------------- Part 6 · Data Handling
    dict(ch='8', scen='pictograph of books read by four children',
         fig=drawing(300, 160, pict([('Anaya', 5), ('Rohit', 3), ('Tara', 6), ('Dev', 4)], '📘', '4 books')),
         stem='The pictograph shows the books four children read in a month. How many more books did Tara and Dev read together than Anaya and Rohit together?',
         opts=['8', '2', '16', '40'],
         hint='Compare the number of symbols first, then use the key.',
         sol='Tara and Dev: 6 + 4 = 10 symbols. Anaya and Rohit: 5 + 3 = 8 symbols. The difference is 2 symbols, and each symbol is 4 books. 2 × 4 = 8 books.'),

    # ---------------- Part 7 · Applied Mathematics
    dict(ch='9', scen='night train leaving 10:48 PM for 7 h 35 min',
         stem='A train leaves at 10:48 PM. The journey takes 7 hours 35 minutes. At what time does the train arrive?',
         opts=['6:23 AM', '6:23 PM', '5:23 AM', '6:13 AM'],
         hint='Add the hours first, then the minutes. Remember that the time passes midnight.',
         sol='10:48 PM + 7 hours = 5:48 AM. 5:48 + 35 minutes = 6:23 AM (12 minutes to 6:00, then 23 more).'),
    dict(ch='9', scen='5 March is Sunday · day of 3 April',
         stem='In a certain year, 5 March is a Sunday. What day of the week is 3 April in that year?',
         opts=['Monday', 'Sunday', 'Tuesday', 'Saturday'],
         hint='March has 31 days. Count the days from 5 March to 3 April.',
         sol='From 5 March to 31 March is 26 days, and 3 more days reach 3 April: 29 days in all. 29 = 4 weeks + 1 day. One day after Sunday is Monday.'),
    dict(ch='9', scen='three shirts and two trousers paid with ₹2,500',
         stem='Arjun buys 3 shirts at ₹349 each and 2 trousers at ₹575 each. He pays with ₹2,500. How much change does he get?',
         opts=['₹303', '₹1,576', '₹403', '₹313'],
         hint='Find the cost of the shirts and the trousers separately.',
         sol='Shirts: 3 × 349 = ₹1,047. Trousers: 2 × 575 = ₹1,150. Total ₹2,197. Change: 2,500 − 2,197 = ₹303.'),

    # ---------------- Part 8 · Mathematical Reasoning
    dict(ch='10', scen='series 2 6 12 20 30',
         fig=cards([2, 6, 12, 20, 30, '?']),
         stem='Look at how much is added each time. Which number comes next?',
         opts=['42', '40', '36', '44'],
         hint='The amounts added are 4, 6, 8, …',
         sol='The pattern adds 4, 6, 8 and 10. Next it adds 12: 30 + 12 = 42.'),
    dict(ch='10', scen='AB plus AB plus AB equals 141',
         fig=equations([['A B', '+', 'A B', '+', 'A B', '=', '141']], size=30),
         stem='A and B stand for digits in the 2-digit number AB. What is the number AB?',
         opts=['47', '37', '57', '41'],
         hint='Three equal numbers add up to 141.',
         sol='AB + AB + AB is 3 times AB. 141 ÷ 3 = 47. Check: 47 + 47 + 47 = 141. So A = 4 and B = 7.'),
    dict(ch='10', scen='page numbers from 1 to 120 containing the digit 5',
         stem='A book has pages numbered 1 to 120. How many page numbers contain the digit 5 at least once?',
         opts=['21', '22', '12', '20'],
         hint='Count numbers with 5 in the ones place, then 5 in the tens place. Do not count 55 twice.',
         sol='5 in the ones place: 5, 15, 25, …, 115, which is 12 numbers. 5 in the tens place: 50 to 59, which is 10 numbers. 55 is in both lists. 12 + 10 − 1 = 21.'),
    dict(ch='10', scen='times 3 minus 15 divided by 4 gives 30',
         stem='Neel thinks of a number. He multiplies it by 3, then subtracts 15, then divides by 4. He gets 30. What was his number?',
         opts=['45', '35', '25', '135'],
         hint='Work backwards and undo each step.',
         sol='Undo ÷ 4: 30 × 4 = 120. Undo − 15: 120 + 15 = 135. Undo × 3: 135 ÷ 3 = 45.'),

    # ---------------- Section II · Star Questions
    dict(ch='3+10', scen='fraction pattern adding one twelfth',
         fig=cards(['1/12', '1/6', '1/4', '1/3', '?'], size=44, width=62),
         stem='The fractions go up by the same amount each time. Which fraction comes next?',
         opts=['5/12', '1/2', '2/5', '1/5'],
         hint='Write every fraction as twelfths.',
         sol='1/12, 2/12, 3/12, 4/12: each time 1/12 is added. Next is 5/12.'),
    dict(ch='9+10', scen='month that starts on the same weekday as February',
         stem='In a year that is not a leap year, 1 February falls on the same day of the week as the 1st of one of these months. Which month is it?',
         opts=['March', 'January', 'April', 'December'],
         hint='How many days does February have in such a year?',
         sol='February has 28 days, which is exactly 4 weeks. So 1 March is the same day of the week as 1 February. January has 31 days, so 1 February is 3 days after 1 January. April and December do not match either.'),
    dict(ch='1+10', scen='numbers 1 to 100 whose Roman numeral has exactly two letters',
         stem='How many numbers from 1 to 100 are written with exactly two letters in Roman numerals? For example, 6 is VI.',
         opts=['12', '9', '10', '14'],
         hint='Think of II, IV, VI, IX and then do the same with tens.',
         sol='They are II (2), IV (4), VI (6), IX (9), XI (11), XV (15), XX (20), XL (40), LI (51), LV (55), LX (60) and XC (90). That is 12 numbers.'),
    dict(ch='3+9', scen='sitar practice in fractions of an hour · finishing time',
         stem='Lavanya practises the sitar for 3/4 of an hour on Monday and 2/3 of an hour on Tuesday. She wants 2 hours in all by Wednesday. She starts on Wednesday at 5:35 PM. When should she stop?',
         opts=['6:10 PM', '6:00 PM', '6:20 PM', '7:35 PM'],
         hint='Change each fraction of an hour into minutes.',
         sol='3/4 of an hour = 45 minutes and 2/3 of an hour = 40 minutes, so 85 minutes are done. 2 hours = 120 minutes, so she needs 35 more minutes. 5:35 PM + 35 minutes = 6:10 PM.'),
    dict(ch='5+6', scen='perimeter of a cube net whose area is 54 cm²',
         fig=grid(BLANK_NET, cell=34),
         stem='This net of a cube is made of 6 equal squares. Its area is 54 cm². What is the perimeter of the net?',
         opts=['42 cm', '36 cm', '54 cm', '72 cm'],
         hint='Find the area of one square, and then its side. Then count the outside edges of the net.',
         sol='Each square has area 54 ÷ 6 = 9 cm², so its side is 3 cm. Going round the net there are 14 square edges. 14 × 3 = 42 cm.'),
]
