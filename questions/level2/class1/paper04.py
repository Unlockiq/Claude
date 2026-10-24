# AMO Level-2 · Class 1 · Practice Paper 4  (format: see paper01.py)

PIP = {0: [], 1: [(1, 1)], 2: [(0, 0), (2, 2)], 3: [(0, 0), (1, 1), (2, 2)], 4: [(0, 0), (2, 0), (0, 2), (2, 2)],
       5: [(0, 0), (2, 0), (1, 1), (0, 2), (2, 2)], 6: [(0, 0), (0, 1), (0, 2), (2, 0), (2, 1), (2, 2)]}


def domino(x, y, a, b, label, s=36):
    prims = [('rect', x, y, s, 2 * s, 'white'), ('line', x + 4, y + s, x + s - 4, y + s)]
    for half, n in ((0, a), (1, b)):
        for c, r in PIP[n]:
            prims.append(('dot', x + 8 + c * (s - 16) / 2, y + half * s + 8 + r * (s - 16) / 2, 3.6))
    prims.append(('text', x + s / 2, y + 2 * s + 14, label, 13))
    return prims


def circles_fig(n, x0, label, r=7):
    """n circles in rows of up to 4, bottom-aligned."""
    prims = []
    for i in range(n):
        row, col = divmod(i, 4)
        prims.append(('circle', x0 + col * 17, 70 - row * 17, r, 'blue'))
    prims.append(('text', x0 + 25, 92, label, 10))
    return prims


def tri_rows(n, cx, top, s=30):
    """Big triangle of n rows of small triangles, apex at (cx, top)."""
    h = s * 0.866
    prims = []
    for r in range(n):
        for k in range(r + 1):
            x, y = cx - s / 2 * r + s * k, top + h * r
            prims.append(('poly', [(x, y), (x + s / 2, y + h), (x - s / 2, y + h)], 'pink'))
        for k in range(r):
            x, y = cx - s / 2 * r + s * k, top + h * r
            prims.append(('poly', [(x, y), (x + s, y), (x + s / 2, y + h)], 'white'))
    return prims


QUESTIONS = [
    # ---------------- Part 1 · Number System
    dict(ch='1', scen='all numbers from cards 2 5 7 · fourth in order',
         fig=cards([2, 5, 7]),
         stem='Aryan makes every 2-digit number he can using two different cards. He lists them from smallest to largest. Which number is 4th in his list?',
         opts=['57', '52', '72', '27'],
         hint='There are 6 numbers. Write them all in order.',
         sol='The numbers are 25, 27, 52, 57, 72 and 75. In order, the 4th number is 57.'),
    dict(ch='1', scen='number name for one ten less than 74',
         stem='Which number name is for the number that is 1 ten less than the number 2 more than 72?',
         opts=['sixty-four', 'seventy-three', 'sixty-two', 'seventy-four'],
         hint='First find the number that is 2 more than 72.',
         sol='2 more than 72 is 74. One ten less than 74 is 64, because only the tens digit goes down by 1. 64 is read as sixty-four.'),
    dict(ch='1', scen='smallest 2-digit number with digit sum 12',
         stem='What is the smallest 2-digit number whose two digits add up to 12?',
         opts=['39', '48', '66', '93'],
         hint='Make the tens digit as small as you can.',
         sol='The ones digit can be at most 9. To make 12, the tens digit must then be at least 3, because 3 + 9 = 12. So the smallest number is 39.'),
    dict(ch='1', scen='one more than the largest number in the forties',
         stem='Think of the largest 2-digit number whose tens digit is 4. Which number is 1 more than it?',
         opts=['50', '49', '41', '48'],
         hint='First find the largest number with tens digit 4.',
         sol='The largest number with tens digit 4 is 49. One more than 49 is 50.'),
    dict(ch='1', scen='numbers 40 to 49 with tens digit bigger than ones digit',
         stem='Nakul looks at the numbers from 40 to 49. In how many of them is the tens digit bigger than the ones digit?',
         opts=['4', '5', '3', '10'],
         hint='The tens digit is always 4. Which ones digits are smaller than 4?',
         sol='The tens digit is 4, so the ones digit must be 0, 1, 2 or 3. The numbers are 40, 41, 42 and 43: that is 4 numbers. In 44 the digits are equal.'),
    dict(ch='1', scen='one ten and two ones more than point A',
         fig=numberline(50, 60, marks={56: 'A'}),
         stem='Point A is marked on the number line. Which number is 1 ten and 2 ones more than the number at A?',
         opts=['68', '58', '66', '78'],
         hint='Find A first. Then add 1 ten and 2 ones separately.',
         sol='A is 56. One ten more is 66. Two ones more than 66 is 68.'),
    dict(ch='1', scen='numbers between 50 and 90 ending like 38',
         stem='How many numbers between 50 and 90 have the same ones digit as 38?',
         opts=['4', '3', '5', '9'],
         hint='The ones digit must be 8. List them.',
         sol='The numbers between 50 and 90 that end in 8 are 58, 68, 78 and 88. That is 4 numbers.'),
    # ---------------- Part 2 · Operations
    dict(ch='2', scen='fact family of 7 9 16 · which sentence is false',
         stem='Ved knows that 7 + 9 = 16. Which of these number sentences is NOT true?',
         opts=['9 − 7 = 16', '16 − 9 = 7', '9 + 7 = 16', '16 − 7 = 9'],
         hint='Taking away from 16 must give 7 or 9.',
         sol='9 + 7 = 16 is true because the order of adding does not matter. 16 − 9 = 7 and 16 − 7 = 9 are true. But 9 − 7 = 2, not 16.'),
    dict(ch='2', scen='toy train coaches with dolls · dolls left after a stop',
         fig=objects([{'items': ['🪆'] * 5, 'cols': 5, 'label': 'Coach 1'}, {'items': ['🪆'] * 5, 'cols': 5, 'label': 'Coach 2'},
                      {'items': ['🪆'] * 5, 'cols': 5, 'label': 'Coach 3'}], item=22, gap=3),
         stem='A toy train has 3 coaches with 5 dolls in each coach. At a stop, 4 dolls get off. How many dolls are on the train now?',
         opts=['11', '15', '19', '8'],
         hint='Find how many dolls there were before the stop.',
         sol='Before the stop there are 5 + 5 + 5 = 15 dolls. After 4 get off: 15 − 4 = 11 dolls.'),
    dict(ch='2', scen='magic triangle with equal side sums',
         fig=drawing(200, 180, [('poly', [(100, 20), (180, 160), (20, 160)], None),
                                ('circle', 100, 20, 16, 'yellow'), ('circle', 180, 160, 16, 'yellow'), ('circle', 20, 160, 16, 'yellow'),
                                ('circle', 140, 90, 16, 'white'), ('circle', 100, 160, 16, 'white'), ('circle', 60, 90, 16, 'white'),
                                ('text', 100, 21, '1', 15), ('text', 180, 161, '2', 15), ('text', 20, 161, '3', 15),
                                ('text', 140, 91, '6', 15), ('text', 100, 161, '4', 15), ('qbox', 60, 90, 24)]),
         stem='The three numbers along each side of the triangle add up to the same total. Which number goes in the box with the question mark?',
         opts=['5', '6', '4', '3'],
         hint='Find the total of a side that is complete.',
         sol='The right side is 1 + 6 + 2 = 9 and the bottom side is 2 + 4 + 3 = 9. So the left side must also make 9: 1 + ? + 3 = 9, which means ? = 5.'),
    dict(ch='2', scen='double a number then add three to get 15',
         stem='Riya doubles her number and then adds 3. She gets 15. What is her number?',
         opts=['6', '12', '9', '7'],
         hint='Work backwards: undo adding 3 first.',
         sol='Before adding 3 she had 15 − 3 = 12. Twelve is her number doubled, and 6 + 6 = 12. So her number is 6.'),
    dict(ch='2', scen='girls and boys in a class of 17 · how many more girls',
         stem='There are 17 children in a class and 9 of them are girls. How many more girls than boys are there?',
         opts=['1', '8', '9', '2'],
         hint='First find the number of boys.',
         sol='There are 17 − 9 = 8 boys. The girls are 9 − 8 = 1 more than the boys.'),
    dict(ch='2', scen='domino with the same total as 4 plus 5',
         fig=drawing(260, 110, domino(10, 4, 6, 3, 'P') + domino(80, 4, 5, 5, 'Q') + domino(150, 4, 4, 4, 'R') + domino(220, 4, 2, 6, 'S')),
         stem='Which domino has the same total number of dots as 4 + 5?',
         opts=['Domino P', 'Domino Q', 'Domino R', 'Domino S'], fixed=True, ans=0,
         hint='Count both halves of each domino and add.',
         sol='4 + 5 = 9. Domino P has 6 + 3 = 9. Q has 5 + 5 = 10, R has 4 + 4 = 8 and S has 2 + 6 = 8.'),

    # ---------------- Part 3 · Geometry
    dict(ch='5', scen='triangle split into four small triangles · count',
         fig=drawing(200, 130, [('poly', [(100, 10), (190, 120), (10, 120)], 'pink'), ('poly', [(55, 65), (145, 65), (100, 120)], 'white')]),
         stem='Lines join the middle points of the sides of a big triangle. How many triangles of all sizes are there in the picture?',
         opts=['5', '4', '3', '6'],
         hint='Do not forget the big triangle itself.',
         sol='There are 4 small triangles (3 at the corners and 1 upside-down in the middle). The big triangle is 1 more. 4 + 1 = 5.'),
    dict(ch='5', scen='two squares joined into one shape · corners of the new shape',
         fig=drawing(160, 80, [('rect', 10, 10, 60, 60, 'yellow'), ('rect', 70, 10, 60, 60, 'yellow')]),
         stem='Two equal squares are pushed together side by side to make one new shape. How many corners does the new shape have?',
         opts=['4', '8', '6', '7'],
         hint='Look at the outline of the new shape only.',
         sol='The two squares together make a rectangle. Where the squares touch, the corners are no longer corners of the shape. A rectangle has 4 corners.'),
    dict(ch='5', scen='cutting a rectangle into squares then triangles · total corners',
         stem='Dev cuts a rectangle into 2 squares. Then he cuts each square into 2 triangles. How many corners do all his pieces have altogether?',
         opts=['12', '8', '4', '16'],
         hint='Find how many pieces there are, and what shape they are.',
         sol='2 squares cut into 2 triangles each give 4 triangles. Each triangle has 3 corners: 3 + 3 + 3 + 3 = 12 corners.'),
    dict(ch='5', scen='cutting a square notch on a folded edge',
         fig=drawing(170, 120, [('rect', 20, 10, 110, 100, 'blue'), ('line', 20, 10, 20, 110, True, (192, 40, 40)),
                                ('rect', 20, 45, 30, 30, 'white'), ('text', 22, 118, 'fold', 10)]),
         stem='Rohan folds a paper in half. He cuts a small square out of the folded edge, as shown. He then opens the paper. What shape is the hole?',
         opts=['Rectangle', 'Square', 'Triangle', 'Circle'],
         hint='The cut goes through two layers that open out on both sides of the fold.',
         sol='The square cut sits on the fold, so when the paper opens the same square appears on both sides of the fold. Two squares side by side make a rectangle that is twice as wide as it is tall.'),

    # ---------------- Part 4 · Applied Mathematics
    dict(ch='9', scen='Sundays in the first 14 days when the 1st is a Monday',
         stem='The 1st day of a month is a Monday. How many Sundays are there from the 1st to the 14th of that month?',
         opts=['2', '1', '3', '7'],
         hint='Find the date of the first Sunday.',
         sol='Monday is the 1st, so Sunday is the 7th. The next Sunday is 7 days later, on the 14th. So there are 2 Sundays.'),
    dict(ch='9', scen='ten months starting from June · last month',
         stem="Ira's school year starts in June and lasts for 10 months, counting June. In which month does it end?",
         opts=['March', 'April', 'February', 'May'],
         hint='June is month 1. Count on until you reach month 10.',
         sol='June 1, July 2, August 3, September 4, October 5, November 6, December 7, January 8, February 9, March 10. It ends in March.'),
    dict(ch='9', scen='three different notes making ₹80',
         stem='Shalini has three Indian notes. Each note has a different value. Together they make ₹80. Which notes does she have?',
         opts=['₹50, ₹20 and ₹10', '₹50, ₹20 and ₹20', '₹40, ₹30 and ₹10', '₹50, ₹10 and ₹10'],
         hint='Think about which notes really exist, and that all three must be different.',
         sol='₹50 + ₹20 + ₹10 = ₹80, and all three are real, different notes. The second and fourth groups repeat a note. There are no ₹40 or ₹30 notes.'),
    dict(ch='9', scen='piggy bank · which coin was taken out',
         stem='A piggy bank has three ₹5 coins and two ₹2 coins. Lavanya takes out one coin. Now ₹14 is left in the bank. Which coin did she take out?',
         opts=['₹5', '₹2', '₹1', '₹10'],
         hint='First find how much money was in the bank.',
         sol='At first there was ₹5 + ₹5 + ₹5 + ₹2 + ₹2 = ₹19. Now there is ₹14, so she took out ₹19 − ₹14 = ₹5. That is a ₹5 coin.'),

    # ---------------- Part 5 · Mathematical Reasoning
    dict(ch='10', scen='add one then two alternately',
         fig=cards([2, 3, 5, 6, 8, 9, '?']),
         stem='Chirag hops along a number track. He lands on the numbers shown. If he keeps hopping the same way, where does he land next?',
         opts=['11', '10', '12', '13'],
         hint='Look at what is added each time.',
         sol='The pattern adds 1, then 2, then 1, then 2: 2, 3, 5, 6, 8, 9. Next it adds 2: 9 + 2 = 11.'),
    dict(ch='10', scen='magic square missing number',
         fig=grid([[4, 9, 2], [3, 5, 7], [8, '?', 6]], cell=44),
         stem='In this square, every row and every column adds up to 15. Which number is hidden by the question mark?',
         opts=['1', '7', '2', '4'],
         hint='Use the bottom row or the middle column.',
         sol='Bottom row: 8 + ? + 6 = 15. Since 8 + 6 = 14, the ? must be 1. Check the middle column: 9 + 5 + 1 = 15.'),
    dict(ch='10', scen='odd one out · forms of the number 43',
         stem='Three of these show the same number. Which one is the odd one out?',
         opts=['4 tens and 13 ones', '43', 'forty-three', '3 tens and 13 ones'],
         hint='Change extra ones into tens, then write each as a number.',
         sol='43 and forty-three show 43. 3 tens and 13 ones is 4 tens and 3 ones, which is also 43. But 4 tens and 13 ones is 5 tens and 3 ones, which is 53.'),
    dict(ch='10', scen='circles growing by three · figure five',
         fig=drawing(220, 100, circles_fig(2, 10, 'Figure 1') + circles_fig(5, 80, 'Figure 2') + circles_fig(8, 160, 'Figure 3')),
         stem='Look at how the number of circles grows from figure to figure. How many circles will Figure 5 have?',
         opts=['14', '11', '13', '17'],
         hint='Count the circles in each figure. How many are added each time?',
         sol='The figures have 2, 5 and 8 circles, so 3 are added each time. Figure 4 has 8 + 3 = 11 and Figure 5 has 11 + 3 = 14.'),

    # ---------------- Section II · Star Questions
    dict(ch='1+10', scen='number chart column ending in 7 · how many below 60',
         stem='On a number chart from 1 to 100, Bhavna marks 7, 17, 27 and every number below them in the same column. How many marked numbers are less than 60?',
         opts=['6', '5', '7', '10'],
         hint='Going down a column adds 1 ten each time.',
         sol='The marked numbers are 7, 17, 27, 37, 47, 57, 67, 77, 87, 97. The ones less than 60 are 7, 17, 27, 37, 47 and 57: that is 6 numbers.'),
    dict(ch='5+10', scen='big triangles made of small triangles · figure 4',
         fig=drawing(330, 120, tri_rows(1, 30, 60) + tri_rows(2, 110, 30) + tri_rows(3, 235, 0) +
                     [('text', 30, 125, 'Fig 1', 10), ('text', 110, 125, 'Fig 2', 10), ('text', 235, 125, 'Fig 3', 10)]),
         stem='Each figure is a big triangle made of small triangles. The figures keep growing in the same way. How many small triangles will Figure 4 have?',
         opts=['16', '12', '13', '10'],
         hint='Count the small triangles in each figure, row by row.',
         sol='Figure 1 has 1 small triangle, Figure 2 has 4 and Figure 3 has 9. The jumps are 3 and then 5, so the next jump is 7. Figure 4 has 9 + 7 = 16 small triangles.'),
    dict(ch='9+10', scen='watering on Mondays and Thursdays · fifth watering',
         stem='Gopal waters the plants every Monday and every Thursday. His first watering is on a Monday. On which day is his 5th watering?',
         opts=['Monday', 'Thursday', 'Tuesday', 'Friday'],
         hint='List the waterings in order.',
         sol='Watering 1 is Monday, 2 is Thursday, 3 is Monday, 4 is Thursday and 5 is Monday.'),
    dict(ch='1+9', scen='month whose number has two same digits',
         stem='The months are numbered 1 to 12, starting with January as 1. Which month has a 2-digit number with both digits the same?',
         opts=['November', 'December', 'October', 'January'],
         hint='Which number from 1 to 12 has two equal digits?',
         sol='The only number from 1 to 12 with two equal digits is 11. Counting from January, the 11th month is November.'),
    dict(ch='2+5', scen='mirror picture with a circle on the fold · count shapes',
         stem='Arjun draws 3 triangles and 1 circle on the left of a fold line. He draws 1 more circle right on the fold line. Then he copies the left side onto the right, like a mirror. How many shapes are there in all?',
         opts=['9', '10', '8', '5'],
         hint='The circle on the fold line is not copied again.',
         sol='Left side: 3 triangles and 1 circle, which is 4 shapes. The right side copies them: 4 more shapes. The circle on the fold line is 1 shape. 4 + 4 + 1 = 9.'),
]
