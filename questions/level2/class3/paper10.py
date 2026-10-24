# AMO Level-2 · Class 3 · Practice Paper 10  (format: see paper01.py)


def tri_net(label=None):
    """Big triangle made of 4 equal triangles."""
    prims = [('poly', [(80, 10), (10, 131), (150, 131)], 'yellow'), ('poly', [(45, 70), (115, 70), (80, 131)], 'yellow')]
    if label:
        prims.append(('text', 45, 145, label, 10))
    return prims


def square_rays():
    return [('rect', 10, 10, 120, 120, 'blue'), ('line', 10, 10, 130, 130), ('line', 10, 10, 130, 70),
            ('line', 10, 10, 70, 130), ('text', 0, 0, 'A', 12)]


def path_grid23():
    s = 46
    prims = []
    for r in range(3):
        prims.append(('line', 20, 20 + r * s, 20 + 3 * s, 20 + r * s))
    for c in range(4):
        prims.append(('line', 20 + c * s, 20, 20 + c * s, 20 + 2 * s))
    prims += [('dot', 20, 20, 5), ('text', 8, 8, 'A', 13), ('dot', 20 + 3 * s, 20 + 2 * s, 5), ('text', 32 + 3 * s, 32 + 2 * s, 'B', 13)]
    return prims


QUESTIONS = [
    # ---------------- Part 1 · Number System
    dict(ch='1', scen='largest 4-digit number with exactly two zeros and digit sum 10',
         stem='Reyansh wants the largest 4-digit number that has exactly two 0s and digits that add up to 10. What is it?',
         opts=['9100', '9010', '9001', '8200'],
         hint='The two non-zero digits add up to 10. Put the larger one first.',
         sol='The two non-zero digits add to 10. For the largest number, use 9 and 1 and put them in the two highest places: 9100.'),
    dict(ch='1', scen='face value times place value of 4 in 2341',
         stem='In 2341, Isha multiplies the face value of 4 by its place value. What does she get?',
         opts=['160', '16', '44', '1600'],
         hint='The face value of 4 is 4. Its place value depends on where it is.',
         sol='4 is in the tens place, so its place value is 40. Face value × place value = 4 × 40 = 160.'),
    dict(ch='1', scen='Roman numeral pattern XIV XIX XXIV',
         stem='Chapters in a book are numbered XIV, XIX, XXIV, … in a pattern. What is the next chapter number?',
         opts=['XXIX', 'XXXIV', 'XXVIII', 'XXXI'],
         hint='Change them to our numbers to find the pattern.',
         sol='XIV = 14, XIX = 19, XXIV = 24: the numbers go up by 5. Next is 29, which is XXIX.'),
    dict(ch='1', scen='even numbers above 3500 from digits 1 3 5 6',
         fig=cards([1, 3, 5, 6]),
         stem='Hari makes 4-digit numbers using each card once. How many of them are even and greater than 3500?',
         opts=['3', '2', '6', '4'],
         hint='An even number must end in 6.',
         sol='The number ends in 6. Starting with 5: 5136 and 5316. Starting with 3: it must be more than 3500, so 3516 (3156 is too small). Starting with 1 is too small. Total 3.'),

    # ---------------- Part 2 · Operations
    dict(ch='2', scen='largest difference of two 2-digit numbers from 2 5 7 9',
         stem='Leena uses each of the digits 2, 5, 7 and 9 once to make two 2-digit numbers. What is the largest difference she can get between them?',
         opts=['72', '70', '68', '74'],
         hint='Make one number as big as possible and the other as small as possible.',
         sol='Largest number: 97. Smallest with the digits left: 25. 97 − 25 = 72.'),
    dict(ch='2', scen='7 times 8 equals 4 times box plus 4',
         fig=equations([['7 × 8', '=', '4 × ?', '+', '4']], size=32),
         stem='Both sides are equal. Which number goes in the box?',
         opts=['13', '12', '14', '52'],
         hint='Work out 7 × 8 and take away 4.',
         sol='7 × 8 = 56. 56 − 4 = 52. 4 × 13 = 52, so the box is 13.'),
    dict(ch='2', scen='which division has the largest answer',
         stem='Mohit works out four divisions. Which one has the largest answer?',
         opts=['954 ÷ 9', '816 ÷ 8', '609 ÷ 7', '624 ÷ 6'],
         hint='Do each division.',
         sol='954 ÷ 9 = 106. 816 ÷ 8 = 102. 609 ÷ 7 = 87. 624 ÷ 6 = 104. The largest is 954 ÷ 9.'),
    dict(ch='2', scen='2-digit number leaving remainder 1 when divided by 2 3 4 5 6',
         stem='A 2-digit number leaves remainder 1 when divided by 2, by 3, by 4, by 5 and by 6. What is the number?',
         opts=['61', '31', '59', '41'],
         hint='Take away 1. The new number fits all five times tables.',
         sol='The number minus 1 is in the 2, 3, 4, 5 and 6 times tables. The smallest such number is 60, and the next is 120, which is too big. So the number is 61.'),

    # ---------------- Part 3 · Fractions
    dict(ch='3', scen='36 pencils · two ninths to Om and three ninths to Sita',
         stem='Arjun has 36 pencils. He gives 2/9 of them to Om and 3/9 of them to Sita. How many more pencils does Sita get than Om?',
         opts=['4', '12', '8', '20'],
         hint='First find 1/9 of 36.',
         sol='1/9 of 36 is 4. Sita gets 1/9 more than Om, which is 4 pencils. (Om 8, Sita 12.)'),
    dict(ch='3', scen='day in twelve 2-hour blocks · fraction left after school sleep play',
         stem='Rhea splits a day into 12 blocks of 2 hours. She is at school for 3 blocks, sleeps for 5 blocks and plays for 1 block. What fraction of the day is left?',
         opts=['3/12', '9/12', '4/12', '2/12'],
         hint='The whole day is 12/12.',
         sol='Used: 3/12 + 5/12 + 1/12 = 9/12. Left: 12/12 − 9/12 = 3/12.'),
    dict(ch='3', scen='tenths strictly between three tenths and nine tenths',
         stem='How many fractions with bottom number 10 are more than 3/10 and less than 9/10?',
         opts=['5', '6', '7', '4'],
         hint='Do not count 3/10 or 9/10.',
         sol='They are 4/10, 5/10, 6/10, 7/10 and 8/10. That is 5.'),

    # ---------------- Part 4 · Geometry
    dict(ch='5', scen='vertices of 2 cubes a cone 3 cylinders and a square pyramid',
         stem='Vani has 2 cubes, 1 cone, 3 cylinders and 1 square pyramid. How many vertices (corners) do they have altogether?',
         opts=['22', '21', '17', '26'],
         hint='A cone has 1 vertex. A cylinder has none.',
         sol='2 cubes: 16. Cone: 1. Cylinders: 0. Square pyramid: 5. 16 + 1 + 0 + 5 = 22.'),
    dict(ch='5', scen='net of four equal triangles · solid it folds into',
         fig=drawing(160, 140, tri_net()),
         stem='Advik folds this net of 4 equal triangles along the inside lines. Which solid does he get?',
         opts=['Triangular pyramid', 'Square pyramid', 'Cone', 'Triangular prism'],
         hint='The three outer triangles fold up to meet at one point.',
         sol='The middle triangle is the base. The three outer triangles fold up and meet at a tip. A solid with a triangle base and three triangle faces meeting at a point is a triangular pyramid.'),
    dict(ch='5', scen='square with three lines from one corner · count triangles',
         fig=drawing(140, 140, square_rays()),
         stem='Three lines are drawn from corner A of a square: to the opposite corner and to the middles of the two far sides. How many triangles are there?',
         opts=['6', '4', '5', '8'],
         hint='Every triangle has a corner at A. Its far side lies on the right side or the bottom side.',
         sol='Lines from A meet the right side at 3 points (top corner, middle, bottom corner): 3 triangles. They meet the bottom side at 3 points (bottom-right corner, middle, bottom-left corner): 3 triangles. 3 + 3 = 6.'),

    # ---------------- Part 5 · Mensuration
    dict(ch='6', scen='12 by 8 photo in a 2 cm frame · outer perimeter',
         stem='A photo is 12 cm long and 8 cm wide. It has a frame 2 cm wide all round it. What is the perimeter of the outside of the frame?',
         opts=['56 cm', '40 cm', '48 cm', '64 cm'],
         hint='The frame adds 2 cm on both sides of each length.',
         sol='Outside length: 2 + 12 + 2 = 16 cm. Outside width: 2 + 8 + 2 = 12 cm. Perimeter: 16 + 12 + 16 + 12 = 56 cm.'),
    dict(ch='6', scen='300 mL syrup bottle at 15 mL twice a day',
         stem='A bottle has 300 mL of syrup. Om takes 15 mL twice a day. For how many days does the bottle last?',
         opts=['10', '20', '15', '5'],
         hint='Find how much he takes each day.',
         sol='Each day: 15 + 15 = 30 mL. 30 × 10 = 300, so the bottle lasts 10 days.'),
    dict(ch='6', scen='5 kg sugar packed in 500 g and 250 g packets',
         stem='Sneha packs 5 kg of sugar. She fills 6 packets of 500 g, and puts the rest in 250 g packets. How many 250 g packets does she fill?',
         opts=['8', '4', '10', '12'],
         hint='5 kg = 5000 g.',
         sol='6 × 500 = 3000 g. Left: 5000 − 3000 = 2000 g. 4 packets of 250 g make 1000 g, so 2000 g fills 8 packets.'),

    # ---------------- Part 6 · Applied Mathematics
    dict(ch='9', scen='time spent travelling to and from school in a day',
         stem='Ravi leaves home at 7:35 AM and reaches school at 8:10 AM. School ends at 1:40 PM and he gets home at 2:15 PM. How long does he spend travelling?',
         opts=['1 h 10 min', '35 min', '1 h 35 min', '6 h 40 min'],
         hint='Find each trip separately.',
         sol='Going: 7:35 to 8:10 is 35 minutes. Coming back: 1:40 to 2:15 is 35 minutes. 35 + 35 = 70 minutes = 1 h 10 min.'),
    dict(ch='9', scen='day of the week 50 days after Wednesday',
         stem='Today is Wednesday. What day of the week will it be 50 days from today?',
         opts=['Thursday', 'Wednesday', 'Friday', 'Tuesday'],
         hint='Every 7 days it is Wednesday again.',
         sol='49 days is 7 weeks, so 49 days from today is a Wednesday. 50 days is one day more: Thursday.'),
    dict(ch='9', scen='bus pass ₹400 against ₹10 tickets for 44 trips',
         stem='A monthly bus pass costs ₹400. A single ticket costs ₹10. Ananya makes 2 trips a day on 22 school days. How much does she save with the pass?',
         opts=['₹40', '₹440', '₹400', '₹60'],
         hint='Find the number of trips first.',
         sol='Trips: 2 × 22 = 44. Tickets would cost 44 × 10 = ₹440. With the pass she saves 440 − 400 = ₹40.'),
    dict(ch='9', scen='3-minute sand timer for 1 hour 12 minutes',
         stem='Jaya has a sand timer that runs for 3 minutes. She turns it over again each time it runs out. How many times must it run to measure 1 hour 12 minutes?',
         opts=['24', '20', '36', '4'],
         hint='Change 1 hour 12 minutes into minutes.',
         sol='1 hour 12 minutes = 60 + 12 = 72 minutes. 72 ÷ 3 = 24.'),

    # ---------------- Part 7 · Mathematical Reasoning
    dict(ch='10', scen='pattern taking away 1 2 3 4 from 20',
         fig=cards([20, 19, 17, 14, 10, '?']),
         stem='Kiran\'s numbers go down in a pattern. Which number comes next?',
         opts=['5', '6', '4', '0'],
         hint='Find how much is taken away each time.',
         sol='He takes away 1, 2, 3, 4. Next he takes away 5: 10 − 5 = 5.'),
    dict(ch='10', scen='digits with sum 10 and product 21 · AB minus BA',
         stem='A and B are digits. A + B = 10 and A × B = 21. A is bigger than B. What is AB − BA?',
         opts=['36', '46', '40', '34'],
         hint='Which two digits multiply to 21?',
         sol='21 = 3 × 7 and 3 + 7 = 10. A = 7, B = 3. AB − BA = 73 − 37 = 36.'),
    dict(ch='10', scen='double add 6 halve subtract the start · always the same',
         stem='Raghav takes a number, doubles it, adds 6, halves the result and then takes away the number he started with. What can you say about his answer?',
         opts=['It is always 3', 'It is always 6', 'It is the starting number', 'It changes with the number'],
         hint='Try it with two different numbers, like 5 and 10.',
         sol='With 5: 10, 16, 8, 8 − 5 = 3. With 10: 20, 26, 13, 13 − 10 = 3. Halving undoes the doubling, and half of the 6 is 3. So it is always 3.'),
    dict(ch='10', scen='shortest paths on a 2 by 3 grid from A to B',
         fig=drawing(180, 130, path_grid23()),
         stem='Sana walks along the lines from A to B, moving only right or down. How many different paths can she take?',
         opts=['10', '6', '5', '12'],
         hint='Write down at each corner how many ways there are to reach it.',
         sol='Each path has 3 steps right and 2 down, so 5 steps in all. Counting ways to reach each corner (adding the corner above and the corner to the left) gives 1, 1, 1, 1 on the top; 1, 2, 3, 4 in the middle; 1, 3, 6, 10 on the bottom. So 10 paths.'),

    # ---------------- Section II · Star Questions
    dict(ch='1+10', scen='how many times digit 1 is written from 1000 to 1100',
         stem='Ved writes all the numbers from 1000 to 1100. How many times does he write the digit 1?',
         opts=['122', '121', '112', '101'],
         hint='Count the 1s in each place separately.',
         sol='Thousands place: all 101 numbers start with 1: 101. Hundreds place: only 1100: 1. Tens place: 1010 to 1019: 10. Ones place: 1001, 1011, …, 1091: 10. Total 101 + 1 + 10 + 10 = 122.'),
    dict(ch='3+10', scen='cake shared · Meena twice Riya · Tara the rest',
         stem='Riya, Meena and Tara share a cake. Riya gets 3/12 of it. Meena gets twice as much as Riya. Tara gets the rest. Who gets the least, and how much?',
         opts=['Riya and Tara, 3/12 each', 'Tara, 2/12', 'Riya, 3/12 only', 'Meena, 6/12'],
         hint='Find Meena\'s share, then Tara\'s.',
         sol='Meena: 6/12. Riya and Meena together: 9/12. Tara: 12/12 − 9/12 = 3/12. Riya and Tara both get 3/12, the least.'),
    dict(ch='9+10', scen='bus every 40 minutes and train every 60 minutes from 6 AM',
         stem='A bus leaves every 40 minutes and a train every 60 minutes. Both leave at 6:00 AM. When do they next leave at the same time?',
         opts=['8:00 AM', '7:00 AM', '10:00 AM', '6:40 AM'],
         hint='List the bus times and the train times.',
         sol='Bus: 6:00, 6:40, 7:20, 8:00. Train: 6:00, 7:00, 8:00. They next leave together at 8:00 AM.'),
    dict(ch='1+9', scen='nine of each note and coin against a ₹5500 cycle',
         stem='Neel has nine ₹500 notes, nine ₹100 notes, nine ₹10 notes and nine ₹1 coins. He wants a cycle that costs ₹5500. What is true?',
         opts=['He is ₹1 short', 'He has ₹1 extra', 'He is ₹501 short', 'He has exactly ₹5500'],
         hint='Add up his money.',
         sol='4500 + 900 + 90 + 9 = ₹5499. The cycle costs ₹5500, so he is ₹1 short.'),
    dict(ch='5+6', scen='four triangles of side 5 cm making a big triangle · perimeter',
         fig=drawing(160, 150, tri_net('5 cm')),
         stem='Four equal triangles, each with three sides of 5 cm, make this big triangle. What is the perimeter of the big triangle?',
         opts=['30 cm', '60 cm', '45 cm', '20 cm'],
         hint='Each side of the big triangle is made of two small sides.',
         sol='Each side of the big triangle is 5 + 5 = 10 cm. Perimeter: 3 × 10 = 30 cm. (60 cm adds the sides of all four small triangles.)'),
]
