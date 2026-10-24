# AMO Level-2 · Class 2 · Practice Paper 2  (format: see paper01.py)


def stick_grid():
    s = 40
    segs = []
    for r in range(3):
        for c in range(2):
            segs.append(((c * s + 5, r * s + 5), ((c + 1) * s + 5, r * s + 5)))
    for c in range(3):
        for r in range(2):
            if (c, r) == (1, 0):
                continue
            segs.append(((c * s + 5, r * s + 5), (c * s + 5, (r + 1) * s + 5)))
    return segs


def mirror_fig():
    prims = [('shape', 'triangle', 20, 25, 30), ('shape', 'circle', 60, 25, 30), ('shape', 'square', 100, 25, 30),
             ('line', 130, 0, 130, 50, True, (192, 40, 40), 2.4), ('text', 130, 62, 'mirror', 11)]
    opts = [('P', ['square', 'circle', 'triangle']), ('Q', ['triangle', 'circle', 'square']),
            ('R', ['circle', 'square', 'triangle']), ('S', ['square', 'triangle', 'circle'])]
    for i, (lab, row) in enumerate(opts):
        x0 = (i % 2) * 170
        y0 = 90 + (i // 2) * 70
        for k, sh in enumerate(row):
            prims.append(('shape', sh, x0 + 20 + k * 40, y0 + 20, 28))
        prims.append(('text', x0 + 140, y0 + 20, lab, 14))
    return prims


def staircase(n, x0, s=12):
    prims = []
    for col in range(n):
        for row in range(col + 1):
            prims.append(('rect', x0 + col * s, 60 - (row + 1) * s, s, s, 'yellow'))
    return prims


QUESTIONS = [
    # ---------------- Part 1 · Number System
    dict(ch='1', scen='3-digit number riddle · zero tens and digit clues',
         stem='I am a 3-digit number. My tens digit is 0. My hundreds digit is 2 more than my ones digit. My digits add up to 8. Which number am I?',
         opts=['503', '305', '530', '602'],
         hint='The hundreds and ones digits add up to 8.',
         sol='The tens digit is 0, so the hundreds and ones digits add up to 8. Two numbers that add to 8 and differ by 2 are 5 and 3. The hundreds digit is the bigger one, so the number is 503.'),
    dict(ch='1', scen='five numbers made of 4 9 and 0 · fourth in order',
         stem='Mihir puts these numbers in order from smallest to largest: 409, 490, 94, 940, 449. Which number is 4th?',
         opts=['490', '449', '940', '409'],
         hint='A 2-digit number is smaller than every 3-digit number.',
         sol='In order: 94, 409, 449, 490, 940. The 4th number is 490.'),
    dict(ch='1', scen='jump back a hundred and forward three tens from 237',
         stem='Arjun starts at 237. He jumps back by 1 hundred. Then he jumps forward by 3 tens. On which number does he land?',
         opts=['167', '307', '107', '140'],
         hint='Change the hundreds digit first, then the tens digit.',
         sol='Back 1 hundred from 237 is 137. Forward 3 tens from 137 is 167.'),
    dict(ch='1', scen='3-digit numbers with all three digits the same',
         stem='How many 3-digit numbers have all three digits the same, like 444?',
         opts=['9', '10', '3', '8'],
         hint='The hundreds digit cannot be 0.',
         sol='The numbers are 111, 222, 333, 444, 555, 666, 777, 888 and 999. 000 is not a 3-digit number. That is 9 numbers.'),
    dict(ch='1', scen='cards 4 7 2 · odd 3-digit numbers using all cards',
         fig=cards([4, 7, 2]),
         stem='Tanvi makes 3-digit numbers using each of these cards once. How many of her numbers are odd?',
         opts=['2', '6', '3', '1'],
         hint='An odd number must end in an odd digit.',
         sol='The only odd digit is 7, so the number must end in 7. The other two cards can be in either order: 427 and 247. That is 2 odd numbers.'),
    dict(ch='1', scen='which hundreds-tens-ones form is not 506',
         stem='Which of these is NOT the same as 506?',
         opts=['5 hundreds and 6 tens', '5 hundreds and 6 ones', '4 hundreds, 10 tens and 6 ones', '50 tens and 6 ones'],
         hint='Change each one into a number.',
         sol='5 hundreds and 6 ones is 506. 4 hundreds and 10 tens make 5 hundreds, so with 6 ones that is 506. 50 tens are 500, so with 6 ones that is 506. But 5 hundreds and 6 tens is 560.'),

    # ---------------- Part 2 · Operations
    dict(ch='2', scen='library books bought and given away',
         stem='A library had 437 books. It bought 286 new books. Then it gave 158 books to a village school. How many books does the library have now?',
         opts=['565', '723', '595', '475'],
         hint='Add first, then take away.',
         sol='437 + 286 = 723 books. Then 723 − 158 = 565 books.'),
    dict(ch='2', scen='rows of eight chairs · empty chairs',
         stem='In a hall there are 5 rows with 8 chairs in each row. 13 children sit on the chairs, one on each chair. How many chairs are empty?',
         opts=['27', '40', '13', '35'],
         hint='First find how many chairs there are in all.',
         sol='There are 8 × 5 = 40 chairs. 40 − 13 = 27 chairs are empty.'),
    dict(ch='2', scen='giving away a quarter of 36 apples',
         stem='Sneha has 36 apples. She gives a quarter of them to her neighbour. How many apples does she have left?',
         opts=['27', '9', '18', '32'],
         hint='A quarter means 1 of 4 equal parts.',
         sol='Sharing 36 into 4 equal parts gives 9 in each part (9 + 9 + 9 + 9 = 36). She gives away 9 apples, so 36 − 9 = 27 are left.'),
    dict(ch='2', scen='box minus 167 equals 285',
         fig=equations([['?', '−', '167', '=', '285']], size=34),
         stem='Which number goes in the box?',
         opts=['452', '118', '442', '352'],
         hint='Undo the subtraction by adding.',
         sol='If ? − 167 = 285, then ? = 285 + 167 = 452. Check: 452 − 167 = 285.'),
    dict(ch='2', scen='two of four cards that make 600',
         fig=cards([245, 178, 365, 422], size=40),
         stem='Which two of these cards add up to exactly 600?',
         opts=['178 and 422', '245 and 365', '245 and 422', '178 and 365'],
         hint='Look at the ones digits first: they must make 10 or 0.',
         sol='178 + 422 = 600. The other pairs make 610, 667 and 543.'),
    dict(ch='2', scen='three times as many marbles · total of both',
         stem='Ravi has 8 marbles. Raju has 3 times as many marbles as Ravi. How many marbles do they have together?',
         opts=['32', '24', '11', '16'],
         hint='First find how many Raju has.',
         sol='Raju has 8 × 3 = 24 marbles. Together they have 8 + 24 = 32.'),

    # ---------------- Part 3 · Geometry
    dict(ch='5', scen='window of two rows and three columns · count rectangles',
         fig=drawing(190, 90, [('rect', 5, 5, 180, 80, 'green'), ('line', 65, 5, 65, 85), ('line', 125, 5, 125, 85), ('line', 5, 45, 185, 45)]),
         stem='A window has 2 rows and 3 columns of panes. How many rectangles of all sizes can you find in it?',
         opts=['18', '6', '9', '12'],
         hint='Count rectangles in one row, then in both rows together.',
         sol='In each row there are 3 + 2 + 1 = 6 rectangles, so the two rows give 12. Rectangles that use both rows give 6 more. 12 + 6 = 18.'),
    dict(ch='5', scen='solid that can roll and can also be stacked',
         stem='Which solid can roll along the floor and can also be stacked one on top of another?',
         opts=['Cylinder', 'Sphere', 'Cube', 'Cone'],
         hint='It needs a curved surface and two flat faces.',
         sol='A cylinder has a curved surface, so it rolls, and flat faces on top and bottom, so cylinders stack. A sphere rolls but cannot be stacked, and a cube stacks but does not roll. A cone has a point on top, so it does not stack steadily.'),
    dict(ch='5', scen='sticks grid with one middle stick removed · squares left',
         fig=sticks(stick_grid(), 90, 90),
         stem='Raju made a big square with 4 small squares inside using 12 sticks. He took away one stick from the middle, as shown. How many squares of all sizes are there now?',
         opts=['3', '4', '5', '2'],
         hint='Which small squares are now broken? Is the big square still there?',
         sol='The missing stick breaks the top two small squares, which join to make a rectangle. The 2 bottom small squares are still there. The big outside square is still complete. 2 + 1 = 3 squares.'),
    dict(ch='5', scen='joining the middle points of the sides of a square',
         stem='Ruhi marks the middle point of each side of a square. She joins these 4 points in order with straight lines. What shape is formed inside the square?',
         opts=['A smaller square', 'A rectangle that is not a square', 'A triangle', 'A circle'],
         hint='Each new line cuts off a corner triangle of the same size.',
         sol='Each line cuts off one corner of the square, and all 4 corners are the same size. So the 4 new sides are equal and the corners are square corners. The shape inside is a smaller square, turned on its side.'),
    dict(ch='5', scen='mirror image of a row of three shapes',
         fig=drawing(340, 230, mirror_fig()),
         stem='The top row of shapes is reflected in the mirror. Which row shows how it looks in the mirror?',
         opts=['Row P', 'Row Q', 'Row R', 'Row S'], fixed=True, ans=0,
         hint='In a mirror, the shape nearest the mirror stays nearest the mirror.',
         sol='The square is nearest the mirror, so in the mirror it comes first, then the circle, then the triangle. Row P shows square, circle, triangle. Row Q is just the same row again.'),

    # ---------------- Part 4 · Applied Mathematics
    dict(ch='9', scen='clock at quarter past seven',
         fig=clocks([(7, 15)]),
         stem='What time does this clock show?',
         opts=['Quarter past 7', 'Quarter past 3', 'Quarter to 7', 'Half past 3'],
         hint='The short hand shows the hour. The long hand shows the minutes.',
         sol='The long (minute) hand points at 3, which means quarter past. The short (hour) hand is just after 7. So it is quarter past 7. Quarter past 3 mixes up the two hands.'),
    dict(ch='9', scen='three pens compared with two notebooks · cost difference',
         stem='A pen costs ₹12 and a notebook costs ₹19. Which costs more, 3 pens or 2 notebooks, and by how much?',
         opts=['2 notebooks, by ₹2', '3 pens, by ₹2', '2 notebooks, by ₹7', '3 pens, by ₹7'],
         hint='Find both totals first.',
         sol='3 pens cost ₹12 + ₹12 + ₹12 = ₹36. 2 notebooks cost ₹19 + ₹19 = ₹38. The notebooks cost ₹38 − ₹36 = ₹2 more.'),
    dict(ch='9', scen='four times of day in order · the third',
         stem='Put these times in order from the earliest in the day to the latest: 11:00 AM, 9:30 PM, 12:15 PM, 6:45 AM. Which time is 3rd?',
         opts=['12:15 PM', '11:00 AM', '9:30 PM', '6:45 AM'],
         hint='AM times come before noon. PM times come after noon.',
         sol='The morning times are 6:45 AM and then 11:00 AM. 12:15 PM is just after noon, and 9:30 PM is at night. The order is 6:45 AM, 11:00 AM, 12:15 PM, 9:30 PM, so the 3rd is 12:15 PM.'),
    dict(ch='9', scen='₹200 spent on a bag and a pencil box · money left',
         stem='Tanvi has ₹200. She buys a bag for ₹125 and a pencil box for ₹48. How much money does she have left?',
         opts=['₹27', '₹173', '₹75', '₹37'],
         hint='Find the total she spends first.',
         sol='She spends ₹125 + ₹48 = ₹173. She has ₹200 − ₹173 = ₹27 left.'),

    # ---------------- Part 5 · Mathematical Reasoning
    dict(ch='10', scen='pattern adding 4 6 8 10',
         fig=cards([2, 6, 12, 20, 30, '?']),
         stem='Ishaan writes this number pattern. Which number comes next?',
         opts=['42', '40', '36', '44'],
         hint='Look at how much is added each time.',
         sol='The pattern adds 4, 6, 8 and 10. Next it adds 12: 30 + 12 = 42.'),
    dict(ch='10', scen='analogy by swapping digits',
         fig=equations([['25', '→', '52'], ['37', '→', '?']], size=30),
         stem='The second pair follows the same rule as the first pair. Which number goes in the box?',
         opts=['73', '74', '40', '59'],
         hint='Look at the digits of 25 and 52.',
         sol='25 becomes 52 when its two digits swap places. So 37 becomes 73.'),
    dict(ch='10', scen='handshakes among four friends',
         stem='Four friends meet. Each friend shakes hands once with every other friend. How many handshakes are there in all?',
         opts=['6', '4', '8', '12'],
         hint='Count the new handshakes for each friend, one at a time.',
         sol='The 1st friend shakes 3 hands. The 2nd has already shaken with the 1st, so 2 new. The 3rd has 1 new, and the 4th has none. 3 + 2 + 1 = 6.'),
    dict(ch='10', scen='odd one out · numbers that read the same backwards',
         stem='Four buses have the numbers 121, 343, 565 and 789. Three numbers belong together. Which bus number is the odd one out?',
         opts=['789', '121', '343', '565'],
         hint='Read each number backwards.',
         sol='121, 343 and 565 read the same forwards and backwards. 789 backwards is 987, so it is the odd one out.'),

    # ---------------- Section II · Star Questions
    dict(ch='1+10', scen='numbers from 100 to 200 that read the same backwards',
         stem='How many numbers between 100 and 200 read the same forwards and backwards, like 151?',
         opts=['10', '9', '11', '20'],
         hint='Such a number must start and end with 1.',
         sol='The number must be 1?1. The middle digit can be any of 0 to 9: 101, 111, 121, … , 191. That is 10 numbers.'),
    dict(ch='2+10', scen='number wall with 25 37 48 at the bottom',
         fig=drawing(170, 95, [('rect', 0, 60, 55, 30, 'peach'), ('text', 27, 76, '25', 15), ('rect', 55, 60, 55, 30, 'peach'), ('text', 82, 76, '37', 15),
                               ('rect', 110, 60, 55, 30, 'peach'), ('text', 137, 76, '48', 15), ('rect', 27, 30, 55, 30, 'white'), ('rect', 82, 30, 55, 30, 'white'),
                               ('rect', 55, 0, 55, 30, 'white'), ('qbox', 82, 15, 22)]),
         stem='In this number wall, each brick is the sum of the two bricks just below it. Which number goes in the top brick?',
         opts=['147', '110', '157', '137'],
         hint='Fill in the middle row first.',
         sol='The middle bricks are 25 + 37 = 62 and 37 + 48 = 85. The top brick is 62 + 85 = 147.'),
    dict(ch='5+10', scen='staircases of squares · squares in figure 6',
         fig=drawing(220, 70, staircase(1, 0) + staircase(2, 40) + staircase(3, 95) + staircase(4, 165) +
                     [('text', 6, 72, 'Fig 1', 10), ('text', 52, 72, 'Fig 2', 10), ('text', 113, 72, 'Fig 3', 10), ('text', 189, 72, 'Fig 4', 10)]),
         stem='Each figure is a staircase of small squares. How many small squares will Figure 6 have?',
         opts=['21', '15', '18', '28'],
         hint='Each new figure adds a column that is one square taller.',
         sol='The figures have 1, 3, 6 and 10 squares. Figure 5 adds 5 squares to make 15, and Figure 6 adds 6 to make 21.'),
    dict(ch='1+9', scen='₹786 with fewest ₹100 notes ₹10 notes and ₹1 coins',
         stem='Shreya must pay ₹786 using only ₹100 notes, ₹10 notes and ₹1 coins. She uses as few notes and coins as she can. How many does she use in all?',
         opts=['21', '786', '3', '78'],
         hint='Think of 786 as hundreds, tens and ones.',
         sol='786 is 7 hundreds, 8 tens and 6 ones. She uses 7 notes of ₹100, 8 notes of ₹10 and 6 coins of ₹1: 7 + 8 + 6 = 21.'),
    dict(ch='5+9', scen='joining 12 3 6 9 on a clock face',
         fig=clocks([None], r=50),
         stem='On a clock face, Om draws straight lines joining the numbers 12, 3, 6 and 9 in order, and then back to 12. What shape does he draw?',
         opts=['Square', 'Triangle', 'Circle', 'Rectangle that is not a square'],
         hint='These four numbers are equally spaced around the clock.',
         sol='12, 3, 6 and 9 are equally spaced round the circle, a quarter of the way apart. Joining them gives 4 equal sides with square corners, which is a square.'),
]
