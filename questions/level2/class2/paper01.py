# AMO Level-2 · Class 2 · Practice Paper 1
# Each question: ch (chapter or star pair), scen (unique scenario key), stem, opts (correct answer FIRST),
# hint, sol, optional fig. fixed=True keeps the option order, with ans = index of the correct option.


def tri_two_lines():
    """Triangle with two lines from the top corner and one line across."""
    return [('poly', [(10, 130), (110, 10), (210, 130)], 'pink'), ('line', 110, 10, 75, 130), ('line', 110, 10, 145, 130),
            ('line', 52, 80, 168, 80)]


def grid_missing_corner():
    s = 36
    prims = []
    for r in range(3):
        for c in range(3):
            if (r, c) == (0, 2):
                continue
            prims.append(('rect', 5 + c * s, 5 + r * s, s, s, 'yellow'))
    return prims


def half_grid():
    s = 24
    shaded_left = [(0, 1), (1, 0), (1, 2), (2, 1), (3, 0), (3, 2)]
    shaded_right = [(1, 3), (3, 5)]
    prims = []
    for r in range(4):
        for c in range(6):
            fill = 'blue' if (r, c) in shaded_left or (r, c) in shaded_right else 'white'
            prims.append(('rect', 5 + c * s, 5 + r * s, s, s, fill))
    prims.append(('line', 5 + 3 * s, 0, 5 + 3 * s, 10 + 4 * s, True, (192, 40, 40), 2.4))
    return prims


QUESTIONS = [
    # ---------------- Part 1 · Number System
    dict(ch='1', scen='cards 5 0 8 · largest minus smallest 3-digit number',
         fig=cards([5, 0, 8]),
         stem='Anita uses each of these cards once to make the largest 3-digit number and the smallest 3-digit number. What is the largest number minus the smallest number?',
         opts=['342', '358', '350', '800'],
         hint='The smallest 3-digit number cannot start with 0.',
         sol='The largest number is 850. The smallest cannot start with 0, so it is 508. 850 − 508 = 342.'),
    dict(ch='1', scen='hundreds flats with eleven rods and fifteen cubes',
         fig=blocks([(2, 11, 15)]),
         stem='Rohan shows a number with hundreds flats, tens rods and ones cubes. Which number does he show?',
         opts=['325', '2115', '235', '315'],
         hint='Ten rods make a hundred and ten cubes make a ten.',
         sol='There are 2 hundreds, 11 tens and 15 ones. 11 tens are 1 hundred and 1 ten. 15 ones are 1 ten and 5 ones. So there are 3 hundreds, 2 tens and 5 ones: 325.'),
    dict(ch='1', scen='even numbers between 345 and 361',
         stem='How many even numbers are there between 345 and 361?',
         opts=['8', '7', '9', '16'],
         hint='The first even number after 345 is 346.',
         sol='The even numbers are 346, 348, 350, 352, 354, 356, 358 and 360. That is 8 numbers.'),
    dict(ch='1', scen='point on a 400 to 500 number line for 3 hundreds and 14 tens',
         fig=numberline(400, 500, 10, marks={420: 'P', 440: 'Q', 460: 'R', 480: 'S'}),
         stem='Which point on the number line shows the number made of 3 hundreds and 14 tens?',
         opts=['Point P', 'Point Q', 'Point R', 'Point S'], fixed=True, ans=1,
         hint='14 tens are 1 hundred and 4 tens.',
         sol='14 tens are 1 hundred and 4 tens. So 3 hundreds and 14 tens make 4 hundreds and 4 tens, which is 440. Point Q is at 440.'),
    dict(ch='1', scen='difference between the values of the two 7s in 747',
         stem='In the number 747, what is the difference between the values of the two 7s?',
         opts=['693', '0', '700', '690'],
         hint='One 7 is in the hundreds place and the other is in the ones place.',
         sol='The first 7 stands for 700 and the last 7 stands for 7. 700 − 7 = 693.'),
    dict(ch='1', scen='four hundred and nine plus one ten',
         stem='Which number is 1 hundred and 1 ten more than four hundred and nine?',
         opts=['519', '510', '429', '609'],
         hint='Write four hundred and nine as a number first.',
         sol='Four hundred and nine is 409: 4 hundreds, 0 tens and 9 ones. 1 hundred more gives 509. 1 ten more gives 5 hundreds, 1 ten and 9 ones: 519.'),

    # ---------------- Part 2 · Operations
    dict(ch='2', scen='school trip · girls and boys minus children who left',
         stem='A school has 268 girls and 195 boys. On Monday, 147 children go on a trip. How many children stay back at school?',
         opts=['316', '326', '463', '216'],
         hint='First find the total number of children.',
         sol='Total children: 268 + 195 = 463. Children who stay back: 463 − 147 = 316.'),
    dict(ch='2', scen='boxes of seven pencils with some broken',
         stem='Kavya has 6 boxes with 7 pencils in each box. She finds that 9 pencils are broken. How many pencils are not broken?',
         opts=['33', '42', '51', '13'],
         hint='First find how many pencils there are in all.',
         sol='6 boxes of 7 pencils: 7 × 6 = 42 pencils. Not broken: 42 − 9 = 33.'),
    dict(ch='2', scen='giving half and then half of the rest of 48 stickers',
         stem='Ravi has 48 stickers. He gives half of them to Asha. Then he gives half of the stickers he has left to Dev. How many stickers does Ravi have now?',
         opts=['12', '24', '36', '6'],
         hint='Find half of 48 first, then half again.',
         sol='Half of 48 is 24, so Ravi keeps 24. Half of 24 is 12, so he gives 12 to Dev and keeps 12.'),
    dict(ch='2', scen='missing tens digit in an addition with carrying',
         fig=equations([['3?6', '+', '248', '=', '634']], size=34),
         stem='One digit is hidden by the question mark. Which digit is it?',
         opts=['8', '6', '9', '3'],
         hint='634 − 248 gives the first number.',
         sol='The first number is 634 − 248 = 386. So the hidden digit is 8. Check: 386 + 248 = 634.'),
    dict(ch='2', scen='which equal-group total is greatest',
         stem='Which of these gives the greatest total?',
         opts=['7 groups of 8', '9 groups of 6', '5 groups of 10', '8 groups of 6'],
         hint='Work out each one using times tables.',
         sol='7 × 8 = 56, 9 × 6 = 54, 5 × 10 = 50 and 8 × 6 = 48. The greatest is 7 groups of 8.'),
    dict(ch='2', scen='three buses of 45 seats · empty seats',
         stem='Each bus has 45 seats. Three full-size buses carry 128 children, one child to a seat. How many seats are empty?',
         opts=['7', '17', '135', '13'],
         hint='First find the number of seats in three buses.',
         sol='Three buses have 45 + 45 + 45 = 135 seats. 135 − 128 = 7 seats are empty.'),

    # ---------------- Part 3 · Geometry
    dict(ch='5', scen='row of solids · how many can roll',
         fig=shapes(['cube', 'cylinder', 'sphere', 'cube', 'cone', 'cube', 'sphere'], size=46),
         stem='Kabir has these solids in a row. How many of them can roll?',
         opts=['4', '3', '2', '7'],
         hint='A solid with a curved surface can roll.',
         sol='The cylinder, the cone and the two spheres have curved surfaces, so they can roll: that is 4. The three cubes have only flat faces, so they cannot roll.'),
    dict(ch='5', scen='triangle with two lines from the top and one across · count triangles',
         fig=drawing(220, 140, tri_two_lines()),
         stem='Priya draws a big triangle, two lines from its top corner and one line across. How many triangles of all sizes are in her drawing?',
         opts=['12', '6', '9', '10'],
         hint='Count the triangles in the top part first. Then count the ones that reach the bottom side.',
         sol='Above the line across, there are 3 small triangles, 2 made of two parts and 1 made of all three: 6. Triangles that reach the bottom side follow the same pattern: 6 more. 6 + 6 = 12.'),
    dict(ch='5', scen='three by three grid with one corner square removed · count squares',
         fig=drawing(115, 115, grid_missing_corner()),
         stem='A 3 by 3 grid of small squares has one corner square cut away, as shown. How many squares of all sizes can you find?',
         opts=['11', '12', '14', '8'],
         hint='Count small squares, then squares made of 2 by 2 small squares.',
         sol='There are 8 small squares. A 2 by 2 square can sit in 4 places, but one of them uses the missing corner, so there are 3. The big 3 by 3 square is broken. 8 + 3 = 11.'),
    dict(ch='5', scen='shaded grid made the same on both sides of a fold · squares to shade',
         fig=drawing(160, 110, half_grid()),
         stem='Neha wants the shaded squares to look the same on both sides of the dotted line, like a mirror. Two squares on the right are already shaded correctly. How many more squares must she shade?',
         opts=['4', '6', '2', '12'],
         hint='Each shaded square on the left needs a partner on the right.',
         sol='There are 6 shaded squares on the left, so the right side needs 6 partners. Two of them are already shaded. So she must shade 6 − 2 = 4 more.'),
    dict(ch='5', scen='solid that looks like a circle from the top and a triangle from the side',
         stem='Kunal lays a solid on its side and pushes it. It rolls round in a circle and stays in one place. From the side it looks like a triangle. Which solid is it?',
         opts=['Cone', 'Cylinder', 'Sphere', 'Cube'],
         hint='Which solid has a pointed top and a round base?',
         sol='A cone on its side turns round its tip, so it rolls in a circle. From the side it looks like a triangle. A cylinder rolls away in a straight line, a sphere looks like a circle from every side, and a cube does not roll.'),

    # ---------------- Part 4 · Applied Mathematics
    dict(ch='9', scen='clock at quarter to five · time when minute hand next points at 12',
         fig=clocks([(4, 45)]),
         stem='Look at the clock. What time will it show when the minute hand next points at 12?',
         opts=['5 o\'clock', '4 o\'clock', '6 o\'clock', 'Half past 5'],
         hint='First read the time. The hour hand is between 4 and 5.',
         sol='The minute hand is at 9 and the hour hand is between 4 and 5, so it is quarter to 5. When the minute hand next reaches 12, the time is 5 o\'clock.'),
    dict(ch='9', scen='school starting at quarter past eight in the morning · written time',
         stem='Om\'s school bell rings in the morning when the minute hand points at 3 and the hour hand is just past 8. How is this time written?',
         opts=['8:15 AM', '8:45 AM', '8:15 PM', '7:45 AM'],
         hint='Quarter past means 15 minutes after the hour. Morning times are AM.',
         sol='The minute hand at 3 means quarter past. The hour hand just past 8 means quarter past 8, written 8:15. Morning times are AM, so it is 8:15 AM. 7:45 is quarter to 8.'),
    dict(ch='9', scen='two notebooks and a pencil paid with ₹100 · change',
         stem='A notebook costs ₹38 and a pencil costs ₹15. Neha buys 2 notebooks and 1 pencil. She pays with a ₹100 note. How much change does she get?',
         opts=['₹9', '₹19', '₹47', '₹91'],
         hint='Find the total cost first.',
         sol='Two notebooks cost ₹38 + ₹38 = ₹76. With the pencil: ₹76 + ₹15 = ₹91. Change: ₹100 − ₹91 = ₹9.'),
    dict(ch='9', scen='₹50 notes ₹20 notes and ₹5 coins · total',
         stem='Raju has three ₹50 notes, two ₹20 notes and four ₹5 coins. How much money does he have?',
         opts=['₹210', '₹200', '₹190', '₹75'],
         hint='Add each kind of money separately.',
         sol='Three ₹50 notes: ₹150. Two ₹20 notes: ₹40. Four ₹5 coins: ₹20. Total ₹150 + ₹40 + ₹20 = ₹210.'),

    # ---------------- Part 5 · Mathematical Reasoning
    dict(ch='10', scen='pattern adding 2 4 6 8',
         fig=cards([3, 5, 9, 15, 23, '?']),
         stem='Sakshi writes this number pattern. Which number should she write next?',
         opts=['33', '31', '30', '35'],
         hint='Look at how much is added each time.',
         sol='The pattern adds 2, 4, 6 and 8. Next it adds 10: 23 + 10 = 33.'),
    dict(ch='10', scen='number pairs following a times-four rule',
         fig=equations([['3', '→', '12'], ['5', '→', '20'], ['7', '→', '?']], size=30),
         stem='Each pair of numbers follows the same rule. Which number goes in the box?',
         opts=['28', '21', '14', '24'],
         hint='Look at both pairs. Adding the same number does not work for both.',
         sol='3 → 12 and 5 → 20: each number is multiplied by 4 (3 × 4 = 12, 5 × 4 = 20). So 7 → 7 × 4 = 28.'),
    dict(ch='10', scen='outfits from tops skirts and shoes',
         stem='Asha has 3 tops, 2 skirts and 2 pairs of shoes. An outfit is one top, one skirt and one pair of shoes. How many different outfits can she make?',
         opts=['12', '7', '6', '10'],
         hint='Count top-and-skirt pairs first.',
         sol='Each of the 3 tops can go with 2 skirts: 3 × 2 = 6 top-and-skirt pairs. Each pair can go with 2 pairs of shoes: 6 × 2 = 12 outfits.'),
    dict(ch='10', scen='odd one out · not in the six times table',
         stem='Four tickets are numbered 24, 36, 42 and 56. Three numbers belong to the same times table. Which ticket number is the odd one out?',
         opts=['56', '24', '36', '42'],
         hint='Try the 6 times table.',
         sol='24 = 6 × 4, 36 = 6 × 6 and 42 = 6 × 7 are in the 6 times table. 56 is not (6 × 9 = 54 and 6 × 10 = 60), so it is the odd one out.'),

    # ---------------- Section II · Star Questions
    dict(ch='1+10', scen='pattern 105 150 205 250 305',
         fig=cards([105, 150, 205, 250, 305, '?'], size=40),
         stem='Look at how this pattern is built. Which number comes next?',
         opts=['350', '310', '355', '405'],
         hint='Look at the numbers in pairs.',
         sol='The pairs are 105 and 150, 205 and 250, then 305 and 350. In each pair the last two digits swap, and each pair is 1 hundred more than the last.'),
    dict(ch='2+10', scen='machine that doubles then takes away three · work backwards',
         fig=equations([['?', '→', 'double it', '→', '− 3', '→', '37']], size=30),
         stem='A number goes into this machine. It is doubled and then 3 is taken away. The number 37 comes out. Which number went in?',
         opts=['20', '17', '40', '34'],
         hint='Undo the steps in the opposite order.',
         sol='Undo taking away 3: 37 + 3 = 40. Undo doubling: half of 40 is 20. Check: 20 doubled is 40, and 40 − 3 = 37.'),
    dict(ch='5+10', scen='squares and triangles growing · total corners in figure 4',
         fig=drawing(390, 70, [('shape', 'square', 20, 40, 30),
                               ('shape', 'square', 80, 40, 30), ('shape', 'triangle', 115, 40, 30), ('shape', 'square', 150, 40, 30),
                               ('shape', 'square', 225, 40, 30), ('shape', 'triangle', 260, 40, 30), ('shape', 'square', 295, 40, 30),
                               ('shape', 'triangle', 330, 40, 30), ('shape', 'square', 365, 40, 30),
                               ('text', 20, 75, 'Fig 1', 10), ('text', 115, 75, 'Fig 2', 10), ('text', 295, 75, 'Fig 3', 10)]),
         stem='Each figure has one more square and one more triangle than the one before. How many corners do all the shapes in Figure 4 have?',
         opts=['25', '18', '28', '32'],
         hint='Count the corners in Figures 1, 2 and 3.',
         sol='Figure 1 has 4 corners. Figure 2 has 4 + 3 + 4 = 11. Figure 3 has 3 squares and 2 triangles: 12 + 6 = 18. Each figure adds 7 corners, so Figure 4 has 18 + 7 = 25.'),
    dict(ch='1+9', scen='₹100 notes ₹10 notes and ₹1 coins with regrouping',
         stem='Diya has four ₹100 notes, thirteen ₹10 notes and six ₹1 coins. How much money does she have?',
         opts=['₹536', '₹436', '₹4136', '₹23'],
         hint='Ten ₹10 notes make ₹100.',
         sol='Thirteen ₹10 notes are ₹130, which is 1 hundred and 3 tens. With four ₹100 notes there are 5 hundreds, 3 tens and 6 ones: ₹536.'),
    dict(ch='5+9', scen='clock hands making a straight line',
         fig=clocks([(3, 0), (6, 0), (12, 0), (9, 0)], labels=['P', 'Q', 'R', 'S']),
         stem='On which clock do the two hands make one straight line across the clock face?',
         opts=['Clock P', 'Clock Q', 'Clock R', 'Clock S'], fixed=True, ans=1,
         hint='The hands must point in opposite directions.',
         sol='At 6 o\'clock (Q) the hour hand points at 6 and the minute hand at 12, so together they make one straight line. At 3 and 9 o\'clock the hands make a square corner, and at 12 o\'clock they lie on top of each other.'),
]
