# AMO Level-2 · Class 1 · Practice Paper 6  (format: see paper01.py)


def abacus(tens, ones, x0=10):
    """Two-rod abacus (T and O) with beads."""
    prims = [('rect', x0, 150, 130, 14, 'peach'), ('line', x0 + 40, 20, x0 + 40, 150), ('line', x0 + 90, 20, x0 + 90, 150),
             ('text', x0 + 40, 178, 'T', 13), ('text', x0 + 90, 178, 'O', 13)]
    for k in range(tens):
        prims.append(('rect', x0 + 28, 138 - k * 12, 24, 11, 'blue'))
    for k in range(ones):
        prims.append(('rect', x0 + 78, 138 - k * 12, 24, 11, 'yellow'))
    return prims


def wall(rows, x0=0, w=50, h=30):
    """Number wall: rows from the top; each row is a list of numbers or '?'."""
    prims = []
    n = len(rows[-1])
    for r, row in enumerate(rows):
        off = (n - len(row)) * w / 2
        for k, v in enumerate(row):
            x, y = x0 + off + k * w, r * h
            if v == '?':
                prims += [('rect', x, y, w, h, 'white'), ('qbox', x + w / 2, y + h / 2, 22)]
            else:
                prims += [('rect', x, y, w, h, 'peach'), ('text', x + w / 2, y + h / 2 + 1, str(v), 15)]
    return prims


def plus_fig(n, cx, cy, s=12):
    """Plus shape with n squares on each arm (n = 0 gives a single square)."""
    prims = [('rect', cx - s / 2, cy - s / 2, s, s, 'yellow')]
    for k in range(1, n + 1):
        for dx, dy in ((1, 0), (-1, 0), (0, 1), (0, -1)):
            prims.append(('rect', cx - s / 2 + dx * k * s, cy - s / 2 + dy * k * s, s, s, 'yellow'))
    return prims


QUESTIONS = [
    # ---------------- Part 1 · Number System
    dict(ch='1', scen='abacus showing 49 · two more ones beads',
         fig=drawing(150, 185, abacus(4, 9)),
         stem='The abacus shows a number. A rod can hold at most 9 beads. What number will it show after 2 more ones are added?',
         opts=['51', '411', '61', '50'],
         hint='Ten ones beads are swapped for one tens bead.',
         sol='The abacus shows 4 tens and 9 ones, which is 49. Two more ones make 11 ones, which is 1 ten and 1 one. So it shows 5 tens and 1 one: 51.'),
    dict(ch='1', scen='hall seats in rows of ten · row of seat 47',
         stem='In a hall, Row 1 has seats 1 to 10, Row 2 has seats 11 to 20, and so on. In which row is seat 47?',
         opts=['Row 5', 'Row 4', 'Row 7', 'Row 6'],
         hint='Find where each row ends.',
         sol='Row 1 ends at 10, Row 2 at 20, Row 3 at 30, Row 4 at 40 and Row 5 at 50. Seat 47 comes after 40 and before 50, so it is in Row 5.'),
    dict(ch='1', scen='torn-out pages 21 to 30 · pages left in a 50-page book',
         stem="Kiara's book has pages numbered 1 to 50. Pages 21 to 30 are torn out. How many pages are left in the book?",
         opts=['40', '41', '30', '20'],
         hint='First count the torn pages. Count both page 21 and page 30.',
         sol='The torn pages are 21, 22, … , 30. That is 10 pages, not 30 − 21 = 9. So 50 − 10 = 40 pages are left (5 tens take away 1 ten).', place_value_ok=True),
    dict(ch='1', scen='forty and seven equals thirty and a box and five',
         fig=equations([['40', '+', '7', '=', '30', '+', '?', '+', '5']], size=30),
         stem='Both sides of the equals sign show the same number. Which number goes in the box with the question mark?',
         opts=['12', '17', '2', '7'],
         hint='First find what 40 + 7 makes. Then see what is still missing on the right.',
         sol='40 + 7 = 47, which is 4 tens and 7 ones. The right side already has 3 tens and 5 ones. It still needs 1 ten and 2 ones, which is 12.', place_value_ok=True),
    dict(ch='1', scen='cards 1 2 3 4 · numbers with tens digit bigger',
         fig=cards([1, 2, 3, 4]),
         stem='Varun makes 2-digit numbers using two different cards. In how many of his numbers is the tens digit bigger than the ones digit?',
         opts=['6', '12', '4', '3'],
         hint='Choose the tens digit first, then a smaller ones digit.',
         sol='Tens digit 2: 21. Tens digit 3: 31 and 32. Tens digit 4: 41, 42 and 43. That is 1 + 2 + 3 = 6 numbers.'),
    dict(ch='1', scen='writing 1 to 12 · how many digits in all',
         stem='Asha writes all the numbers from 1 to 12. How many digits does she write in all?',
         opts=['15', '12', '14', '24'],
         hint='Numbers 1 to 9 have one digit. 10, 11 and 12 have two digits.',
         sol='1 to 9 use 9 digits. 10, 11 and 12 use 2 + 2 + 2 = 6 digits. In all 9 + 6 = 15 digits.'),
    dict(ch='1', scen='one ten more than one ten less than 58',
         stem='Arjun thinks of the number that is 1 ten more than the number that is 1 ten less than 58. Which number is it?',
         opts=['58', '68', '48', '59'],
         hint='Go one ten down, then one ten up.',
         sol='1 ten less than 58 is 48. 1 ten more than 48 is 58. Going down and up by the same amount brings him back to 58.'),

    # ---------------- Part 2 · Operations
    dict(ch='2', scen='stars and a square · square equals two stars',
         fig=equations([[('shape', 'star'), '+', ('shape', 'star'), '=', ('shape', 'square')],
                        [('shape', 'square'), '+', ('shape', 'star'), '=', '12']]),
         stem='Shapes that look the same stand for the same number. What number does the square stand for?',
         opts=['8', '4', '6', '12'],
         hint='Swap the square for two stars in the second line.',
         sol='The square is star + star, so the second line is star + star + star = 12. Since 4 + 4 + 4 = 12, each star is 4. The square is 4 + 4 = 8.'),
    dict(ch='2', scen='number wall three bricks at the bottom · top brick',
         fig=drawing(160, 95, wall([['?'], ['', ''], [3, 5, 4]])),
         stem='In this number wall, each brick is the sum of the two bricks just below it. Which number goes in the top brick?',
         opts=['17', '12', '16', '18'],
         hint='Fill in the middle row first.',
         sol='The middle bricks are 3 + 5 = 8 and 5 + 4 = 9. The top brick is 8 + 9 = 17.'),
    dict(ch='2', scen='two numbers making 11 both bigger than 3',
         stem='Rani thinks of two numbers that add up to 11. Both numbers are bigger than 3. The same two numbers in a different order count as one pair. How many pairs are possible?',
         opts=['2', '4', '5', '3'],
         hint='List the pairs that make 11, then cross out any with a number that is 3 or less.',
         sol='Pairs that make 11: 1 and 10, 2 and 9, 3 and 8, 4 and 7, 5 and 6. Only 4 and 7, and 5 and 6, have both numbers bigger than 3. That is 2 pairs.'),
    dict(ch='2', scen='small bus seats with two empty and one standing',
         stem='A small bus has 3 rows with 4 seats in each row. Two seats are empty and 1 child is standing. How many children are on the bus?',
         opts=['11', '12', '9', '13'],
         hint='First count all the seats.',
         sol='There are 4 + 4 + 4 = 12 seats. Two are empty, so 12 − 2 = 10 children are sitting. With 1 child standing, there are 10 + 1 = 11 children.'),
    dict(ch='2', scen='giving marbles until one has three more than the other had',
         stem='Dev had 15 marbles and Yash had 4. Dev gave some marbles to Yash. Now Dev has 3 more marbles than Yash had at first. How many marbles did Dev give?',
         opts=['8', '7', '11', '4'],
         hint='Find how many marbles Dev has now.',
         sol='Yash had 4 at first, so Dev now has 4 + 3 = 7. Dev started with 15, so he gave away 15 − 7 = 8 marbles.'),
    dict(ch='2', scen='changing both parts of 9 plus 6 to make 2 more',
         stem='Bela knows that 9 + 6 = 15. She changes the 9 to 7. What must the 6 change to so that the new total is 2 more than 15?',
         opts=['10', '8', '4', '6'],
         hint='First find the new total. Then find what goes with 7.',
         sol='2 more than 15 is 17. So 7 + ? = 17. Since 7 + 10 = 17, the 6 must change to 10.'),
    # ---------------- Part 3 · Geometry
    dict(ch='5', scen='cupboard door with four panels · count rectangles',
         fig=drawing(150, 90, [('rect', 5, 5, 140, 80, 'green'), ('line', 75, 5, 75, 85), ('line', 5, 45, 145, 45)]),
         stem="Meera's cupboard door has 4 equal panels. How many rectangles of all sizes can you find in it?",
         opts=['9', '4', '5', '8'],
         hint='Count 1 panel, 2 panels and all 4 panels.',
         sol='One panel: 4 rectangles. Two panels side by side: 2. Two panels one above the other: 2. All four panels: 1. Total 4 + 2 + 2 + 1 = 9.'),
    dict(ch='5', scen='cutting one corner off a square · corners left',
         fig=drawing(130, 110, [('poly', [(10, 10), (85, 10), (120, 45), (120, 100), (10, 100)], 'yellow'),
                                ('poly', [(85, 10), (120, 10), (120, 45)], 'white', True)]),
         stem='Naina cuts one corner off a square paper with one straight cut, as shown. How many corners does the big piece have now?',
         opts=['5', '4', '3', '6'],
         hint='The cut takes away one corner. How many new corners does it make?',
         sol='The square had 4 corners. The cut takes away 1 corner but makes 2 new corners, one at each end of the cut. 4 − 1 + 2 = 5 corners.'),
    dict(ch='5', scen='triangles inside and outside a circle',
         fig=drawing(260, 150, [('circle', 110, 75, 65, 'blue'), ('shape', 'triangle', 85, 55, 26), ('shape', 'triangle', 130, 60, 26),
                                ('shape', 'triangle', 105, 105, 26), ('shape', 'square', 145, 100, 20),
                                ('shape', 'triangle', 25, 20, 26), ('shape', 'triangle', 215, 30, 26), ('shape', 'triangle', 230, 85, 26),
                                ('shape', 'triangle', 210, 135, 26), ('shape', 'triangle', 25, 135, 26), ('shape', 'square', 20, 75, 20)]),
         stem='How many more triangles are outside the circle than inside it?',
         opts=['2', '8', '5', '3'],
         hint='Count the triangles inside and outside separately. Ignore the squares.',
         sol='Inside the circle there are 3 triangles. Outside there are 5 triangles. 5 − 3 = 2 more outside.'),
    dict(ch='5', scen='two triangles from a square joined along their longest sides',
         stem='Yash cuts a square along both of its corner-to-corner lines and gets 4 triangles. He joins two of the triangles along their longest sides. What shape does he make?',
         opts=['A smaller square', 'A rectangle', 'A circle', 'A bigger triangle'],
         hint='Each triangle has a square corner. Imagine putting two long sides together.',
         sol='Each of the 4 triangles has one square corner and two equal short sides. Joining two of them along the long side puts their square corners opposite each other. The shape has 4 equal sides and 4 square corners, so it is a smaller square.'),
    # ---------------- Part 4 · Applied Mathematics
    dict(ch='9', scen='three days before the day after Saturday',
         stem='Which day comes 3 days before the day after Saturday?',
         opts=['Thursday', 'Wednesday', 'Friday', 'Tuesday'],
         hint='First find the day after Saturday.',
         sol='The day after Saturday is Sunday. Three days before Sunday: Saturday, Friday, Thursday. The answer is Thursday.'),
    dict(ch='9', scen='amount that two coins cannot make',
         stem='Pooja picks exactly two coins from ₹1, ₹2, ₹5 and ₹10 coins. Both coins may be of the same kind. Which amount can she NOT make?',
         opts=['₹8', '₹7', '₹11', '₹15'],
         hint='List what two coins can make.',
         sol='Two of these coins can make ₹2, ₹3, ₹4, ₹6, ₹7, ₹10, ₹11, ₹12, ₹15 or ₹20. For example ₹7 is ₹5 + ₹2, ₹11 is ₹10 + ₹1 and ₹15 is ₹10 + ₹5. ₹8 is not in the list, so it cannot be made.'),
    dict(ch='9', scen='month exactly in the middle of March and November',
         stem='Which month is exactly in the middle of March and November, with the same number of months before it as after it?',
         opts=['July', 'June', 'August', 'September'],
         hint='Write the months from March to November in order.',
         sol='The months are March, April, May, June, July, August, September, October, November. There are 9 of them. July is 5th, with 4 months before it and 4 after it.'),
    dict(ch='9', scen='Mondays in a 30-day month that starts on Monday',
         stem='A month has 30 days. Its 1st day is a Monday. How many Mondays are there in that month?',
         opts=['5', '4', '6', '3'],
         hint='Mondays come every 7 days.',
         sol='The Mondays are the 1st, 8th, 15th, 22nd and 29th. The next would be the 36th, which is not in the month. So there are 5 Mondays.'),

    # ---------------- Part 5 · Mathematical Reasoning
    dict(ch='10', scen='number track up three down two',
         fig=cards([3, 6, 4, 7, 5, 8, '?']),
         stem='Om walks on a number track and steps on these numbers in order. If he keeps going the same way, which number does he step on next?',
         opts=['6', '9', '11', '4'],
         hint='Look at how he moves each time.',
         sol='He goes up 3, then back 2, again and again: 3, 6, 4, 7, 5, 8. Next he goes back 2: 8 − 2 = 6.'),
    dict(ch='10', scen='wrongly printed shirt number in an add-one-more pattern',
         stem='Shirt numbers should go 2, 5, 9, 14 and so on, adding one more each time. One shirt in this list is wrong: 2, 5, 9, 15, 20. Which number is wrong?',
         opts=['15', '9', '20', '5'],
         hint='Look at what is added each time: 3, then 4, then …',
         sol='The pattern adds 3, 4, 5, 6: 2, 5, 9, 14, 20. So 15 is wrong and should be 14. Then 14 + 6 = 20 is right.'),
    dict(ch='10', scen='table rows where the third number is the sum',
         fig=grid([[2, 3, 5], [4, 1, 5], [3, '?', 9]], cell=44),
         stem='The numbers in every row of this table follow the same rule. Which number is hidden by the question mark?',
         opts=['6', '3', '12', '5'],
         hint='Look at how the first two numbers in a row make the third.',
         sol='In each row the first two numbers add up to the third: 2 + 3 = 5 and 4 + 1 = 5. So 3 + ? = 9, which means ? = 6.'),
    dict(ch='10', scen='ring of numbers with opposite pairs adding to ten',
         fig=drawing(160, 160, [('circle', 80, 80, 62, None)] +
                     [x for (cx, cy, t) in [(80, 18, '3'), (134, 49, '8'), (134, 111, '6'), (80, 142, '?'), (26, 111, '2'), (26, 49, '4')]
                      for x in ([('circle', cx, cy, 15, 'yellow'), ('text', cx, cy + 1, t, 14)] if t != '?' else [('circle', cx, cy, 15, 'white'), ('qbox', cx, cy, 20)])]),
         stem='In this ring, each number and the number straight across from it add up to the same total. Which number is hidden?',
         opts=['7', '1', '5', '9'],
         hint='Look at a pair that is complete, like 8 and 2.',
         sol='8 and 2 are across from each other and make 10. 6 and 4 also make 10. The hidden number is across from 3, so 3 + ? = 10, and ? = 7.'),

    # ---------------- Section II · Star Questions
    dict(ch='1+10', scen='pairs of numbers 11 13 22 24 33 35',
         fig=cards([11, 13, 22, 24, 33, 35, '?']),
         stem='Look carefully at how this pattern is built. Which number comes next?',
         opts=['44', '37', '46', '45'],
         hint='Look at the numbers in pairs.',
         sol='The pairs are 11 and 13, 22 and 24, 33 and 35. Each pair starts with a number whose two digits are the same, then adds 2. The next pair starts with 44.'),
    dict(ch='5+10', scen='plus shapes growing by four squares',
         fig=drawing(260, 90, plus_fig(0, 15, 45) + plus_fig(1, 75, 45) + plus_fig(2, 175, 45) +
                     [('text', 15, 100, 'Fig 1', 10), ('text', 75, 100, 'Fig 2', 10), ('text', 175, 100, 'Fig 3', 10)]),
         stem='Each figure is made of small squares. The figures keep growing in the same way. How many small squares will Figure 4 have?',
         opts=['13', '12', '16', '17'],
         hint='How many squares are added from one figure to the next?',
         sol='Figure 1 has 1 square, Figure 2 has 5 and Figure 3 has 9. Each time 4 squares are added, one on each arm. Figure 4 has 9 + 4 = 13.'),
    dict(ch='9+10', scen='piggy bank one rupee more each day Monday to Friday',
         stem='On Monday, Kunal puts ₹1 in his piggy bank. Each day he puts in ₹1 more than the day before. How much has he put in altogether by the end of Friday?',
         opts=['₹15', '₹5', '₹10', '₹21'],
         hint='Write the amount for each day from Monday to Friday.',
         sol='Monday ₹1, Tuesday ₹2, Wednesday ₹3, Thursday ₹4, Friday ₹5. Altogether 1 + 2 + 3 + 4 + 5 = ₹15.'),
    dict(ch='1+9', scen='dates of a 31-day month containing the digit 2',
         stem='A month has dates from 1 to 31. How many of these dates have the digit 2 in them?',
         opts=['12', '11', '10', '13'],
         hint='Check 1 to 9, then the teens, then the twenties.',
         sol='The dates are 2, 12, and all ten dates from 20 to 29. That is 1 + 1 + 10 = 12 dates. The 22nd has two 2s but is one date.'),
    dict(ch='2+5', scen='total of numbers in all four-cornered shapes',
         fig=drawing(300, 110, [('shape', 'triangle', 30, 55, 56), ('text', 30, 66, '4', 16), ('shape', 'square', 90, 55, 50), ('text', 90, 56, '5', 16),
                                ('shape', 'circle', 150, 55, 54), ('text', 150, 56, '6', 16), ('shape', 'rectangle', 215, 55, 46), ('text', 215, 56, '8', 16),
                                ('shape', 'triangle', 275, 55, 56), ('text', 275, 66, '7', 16), ('shape', 'square', 150, 120, 40), ('text', 150, 121, '3', 15)]),
         stem='Each shape has a number inside it. What is the total of the numbers inside all the shapes that have exactly 4 corners?',
         opts=['16', '22', '11', '33'],
         hint='Squares and rectangles have 4 corners. Triangles have 3 and circles have none.',
         sol='The 4-cornered shapes are the two squares and the rectangle, with 5, 3 and 8. Their total is 5 + 3 + 8 = 16.'),
]
