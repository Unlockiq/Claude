# AMO Level-2 · Class 2 · Practice Paper 7  (format: see paper01.py)


def square_x_mid():
    return [('rect', 10, 10, 120, 120, 'yellow'), ('line', 10, 10, 130, 130), ('line', 130, 10, 10, 130),
            ('line', 10, 70, 130, 70)]


def star5():
    import math
    pts = [(70 + 60 * math.cos(math.radians(-90 + 144 * k)), 70 + 60 * math.sin(math.radians(-90 + 144 * k))) for k in range(6)]
    return [('polyline', pts)]


def three_circles():
    return [('circle', 60, 50, 38, None), ('circle', 110, 50, 38, None), ('circle', 85, 92, 38, None)]


def tri_rows(n=3, s=34):
    import math
    h = s * math.sqrt(3) / 2
    prims = []
    for r in range(n):
        for k in range(r + 1):
            x = 10 + (n - 1 - r) * s / 2 + k * s
            y = 10 + r * h
            prims.append(('poly', [(x + s / 2, y), (x, y + h), (x + s, y + h)], 'white'))
    return prims



QUESTIONS = [
    # ---------------- Part 1 · Number System
    dict(ch='1', scen='value of the 3 plus value of the 4 in 437',
         stem='In the number 437, what is the value of the digit 3 added to the value of the digit 4?',
         opts=['430', '7', '43', '340'],
         hint='The value of a digit depends on its place.',
         sol='In 437 the 4 is in the hundreds place, so its value is 400. The 3 is in the tens place, so its value is 30. 400 + 30 = 430.'),
    dict(ch='1', scen='one hundred more and one ten less than 345',
         stem='Which number is 1 hundred more and 1 ten less than 345?',
         opts=['435', '455', '335', '446'],
         hint='Change the hundreds digit, then the tens digit.',
         sol='1 hundred more than 345 is 445. 1 ten less than 445 is 435.'),
    dict(ch='1', scen='numbers 601 to 699 with equal tens and ones digits',
         stem='How many numbers from 601 to 699 have the same tens digit and ones digit, like 633?',
         opts=['9', '10', '11', '8'],
         hint='600 is not in the list.',
         sol='The numbers are 611, 622, 633, 644, 655, 666, 677, 688 and 699. 600 is not from 601 to 699. That is 9.'),
    dict(ch='1', scen='halfway between 320 and 380 then two tens more',
         fig=numberline(320, 380, 10, marks={320: 'A', 380: 'B'}),
         stem='Mohini stands at the point halfway between A and B. She then moves 2 tens forward. Where is she now?',
         opts=['370', '350', '360', '380'],
         hint='Find the number halfway between 320 and 380 first.',
         sol='Halfway between 320 and 380 is 350. 2 tens forward from 350 is 370.'),
    dict(ch='1', scen='digits 2 5 8 · number closest to 500',
         stem='Lata makes 3-digit numbers using each of the digits 2, 5 and 8 once. Which of her numbers is closest to 500?',
         opts=['528', '582', '285', '258'],
         hint='Start with 5 in the hundreds place.',
         sol='528 is 28 more than 500. 582 is 82 more. 285 and 258 are more than 200 less than 500. So 528 is the closest.'),
    dict(ch='1', scen='odd numbers using cards 3 4 5',
         fig=cards([3, 4, 5]),
         stem='Aarav makes 3-digit numbers using all three cards once each. How many of his numbers are odd?',
         opts=['4', '2', '6', '3'],
         hint='An odd number must end in 3 or 5.',
         sol='Ending in 3: 453 and 543. Ending in 5: 345 and 435. That is 4 odd numbers.'),

    # ---------------- Part 2 · Operations
    dict(ch='2', scen='stamps · gave 125 then got 210 · now 500',
         stem='Lalit gave away 125 stamps. Later he got 210 new stamps. Now he has 500 stamps. How many stamps did he have at the start?',
         opts=['415', '585', '375', '835'],
         hint='Work backwards: undo each step.',
         sol='Before getting 210, he had 500 − 210 = 290. Before giving away 125, he had 290 + 125 = 415.'),
    dict(ch='2', scen='seven rows of six chairs and four extra chairs',
         stem='In the school hall there are 7 rows of chairs with 6 chairs in each row. There are 4 extra chairs at the side. How many chairs are there in all?',
         opts=['46', '42', '38', '17'],
         hint='Multiply first, then add.',
         sol='7 × 6 = 42 chairs in rows. 42 + 4 = 46 chairs.'),
    dict(ch='2', scen='32 balloons · a quarter burst · half the rest given away',
         stem='Siya has 32 balloons. A quarter of them burst. She gives half of the balloons that are left to her friend. How many balloons does she have now?',
         opts=['12', '8', '16', '24'],
         hint='First find a quarter of 32.',
         sol='A quarter of 32 is 8, so 32 − 8 = 24 are left. Half of 24 is 12. She keeps 12 balloons.'),
    dict(ch='2', scen='adding three odd numbers · always odd or even',
         stem='Varun adds three odd numbers, like 3 + 5 + 7. What can you say about his answer?',
         opts=['It is always odd', 'It is always even', 'It can be odd or even', 'It always ends in 5'],
         hint='Odd + odd is even. Now add one more odd number.',
         sol='Odd + odd gives an even number. Even + odd gives an odd number. So the sum of three odd numbers is always odd. Example: 3 + 5 + 7 = 15.'),
    dict(ch='2', scen='same digit in every box · two-digit minus one-digit is 50',
         fig=equations([['?', '?', '−', '?', '=', '50']], size=34),
         stem='Every box hides the same digit. Which digit is it?',
         opts=['5', '0', '1', '6'],
         hint='Try each digit in a 2-digit number like 44 − 4.',
         sol='With 5: 55 − 5 = 50. With 6: 66 − 6 = 60. With 1: 11 − 1 = 10. So the digit is 5.'),
    dict(ch='2', scen='four packs of six and three packs of five juice boxes',
         stem='Dev buys 4 packs of juice with 6 boxes in each, and 3 packs with 5 boxes in each. How many juice boxes does he buy?',
         opts=['39', '35', '42', '18'],
         hint='Find each kind of pack separately.',
         sol='4 × 6 = 24 boxes. 3 × 5 = 15 boxes. 24 + 15 = 39 juice boxes.'),

    # ---------------- Part 3 · Geometry
    dict(ch='5', scen='square with both diagonals and a middle line · count triangles',
         fig=drawing(140, 140, square_x_mid()),
         stem='Juhi draws a square, both corner-to-corner lines and one line across the middle. How many triangles are there in all?',
         opts=['12', '8', '6', '10'],
         hint='Count the 6 small ones first, then look for bigger ones.',
         sol='There are 6 small triangles. 2 more are made of two small ones: the left part and the right part. Each corner-to-corner line also cuts the square into 2 big triangles, which gives 4 more. 6 + 2 + 4 = 12.'),
    dict(ch='5', scen='straight lines needed to draw a five-pointed star',
         fig=drawing(140, 130, star5()),
         stem='Mahi draws this star without lifting her pencil. How many straight lines does she draw?',
         opts=['5', '10', '6', '4'],
         hint='Follow each line from one point to another point.',
         sol='Each line goes from one point of the star straight to another. Starting at the top, she draws 5 lines and is back at the top.'),
    dict(ch='5', scen='three overlapping circles · count parts inside',
         fig=drawing(160, 140, three_circles()),
         stem='Three circles overlap like this. Into how many parts do they cut the space inside them?',
         opts=['7', '6', '8', '3'],
         hint='Look for the part that is inside all three circles.',
         sol='There is 1 part inside all three circles. There are 3 parts inside exactly two circles. Each circle also has 1 part of its own, which makes 3. 1 + 3 + 3 = 7.'),
    dict(ch='5', scen='counting cone and cylinder parts in a pencil a cap and a tin',
         stem='Leena has a sharpened round pencil, a birthday cap and a tin. Count every part shaped like a cone or a cylinder. What does she find?',
         opts=['2 cones and 2 cylinders', '1 cone and 2 cylinders', '2 cones and 1 cylinder', '1 cone and 1 cylinder'],
         hint='A sharpened pencil is made of two solids joined together.',
         sol='The pencil is a cylinder with a cone at the sharpened end. The cap is a cone and the tin is a cylinder. That makes 2 cones and 2 cylinders.'),
    dict(ch='5', scen='folded paper with a triangle cut along the fold',
         stem='Prachi folds a paper in half. She cuts out a triangle with no square corner, so that one side of the triangle lies along the fold. When she opens the paper, what shape is the hole?',
         opts=['A shape with 4 sides', 'A triangle', 'Two triangles', 'A circle'],
         hint='The same triangle appears on both sides of the fold, joined along the fold.',
         sol='Opening the paper gives the triangle and its copy on the other side of the fold. They are joined along the side on the fold, so that side disappears. The hole has 2 + 2 = 4 sides.'),

    # ---------------- Part 4 · Applied Mathematics
    dict(ch='9', scen='clock at half past eleven',
         fig=clocks([(11, 30)]),
         stem='Yamini\'s train leaves at the time on this clock. What time does it leave?',
         opts=['Half past 11', 'Half past 12', 'Half past 6', 'Quarter to 12'],
         hint='The hour hand is between 11 and 12.',
         sol='The minute hand points at 6, so it is half past. The hour hand is between 11 and 12, so it is half past 11.'),
    dict(ch='9', scen='ball bat and cap · which two cost ₹155',
         fig=table(['Item', 'Price'], [['Ball', '₹45'], ['Bat', '₹120'], ['Cap', '₹35']], widths=[100, 90]),
         stem='Aditya buys two of these items and pays ₹155. Which two items does he buy?',
         opts=['Bat and cap', 'Ball and bat', 'Ball and cap', 'All three items'],
         hint='Add the prices of each pair.',
         sol='Bat and cap: 120 + 35 = 155. Ball and bat: 165. Ball and cap: 80. All three: 200. So he buys the bat and the cap.'),
    dict(ch='9', scen='midnight to noon compared with noon to midnight',
         stem='Kiara says the AM part of a day, from midnight to noon, is longer than the PM part, from noon to midnight. What is true?',
         opts=['Both parts are equally long', 'The AM part is longer', 'The PM part is longer', 'It changes every day'],
         hint='The clock goes round once in each part.',
         sol='From midnight to noon the hour hand goes once round the clock: 12 hours. From noon to midnight it also goes once round: 12 hours. Both parts are equally long.'),
    dict(ch='9', scen='₹500 in six notes of ₹50 and ₹100',
         stem='Samar has ₹500 in 6 notes. Each note is either ₹50 or ₹100. How many ₹100 notes does he have?',
         opts=['4', '2', '3', '5'],
         hint='Try different numbers of ₹100 notes and fill up with ₹50 notes.',
         sol='With 4 notes of ₹100 (₹400) and 2 notes of ₹50 (₹100) he has 6 notes and ₹500. With 3 notes of ₹100 he would need 4 notes of ₹50, which is 7 notes.'),

    # ---------------- Part 5 · Mathematical Reasoning
    dict(ch='10', scen='adding 1 2 4 8 pattern',
         fig=cards([2, 3, 5, 9, 17, '?']),
         stem='Look at how much is added each time. Which number comes next?',
         opts=['33', '25', '34', '31'],
         hint='The amount added doubles each time.',
         sol='The pattern adds 1, 2, 4 and 8. Next it adds 16: 17 + 16 = 33.'),
    dict(ch='10', scen='number machine doubling and adding one',
         fig=equations([['5', '→', '11'], ['7', '→', '15'], ['9', '→', '?']], size=30),
         stem='Bhavna\'s number machine uses the same rule for every number. What does it give for 9?',
         opts=['19', '18', '17', '15'],
         hint='Adding 6 works for 5 but not for 7.',
         sol='5 doubled is 10, add 1 to get 11. 7 doubled is 14, add 1 to get 15. 9 doubled is 18, add 1 to get 19.'),
    dict(ch='10', scen='2-digit numbers with digit sum 10',
         stem='Ishaan lists every 2-digit number whose digits add up to 10. How many numbers are on his list?',
         opts=['9', '10', '8', '5'],
         hint='The tens digit can be 1, 2, 3, … Check which ones work.',
         sol='The numbers are 19, 28, 37, 46, 55, 64, 73, 82 and 91. That is 9 numbers.'),
    dict(ch='10', scen='odd one out · numbers made from the same three digits',
         stem='Three of these numbers are made from the same three digits. Which is the odd one out: 203, 302, 230, 233?',
         opts=['233', '203', '302', '230'],
         hint='Look at which digits each number uses.',
         sol='203, 302 and 230 each use the digits 2, 0 and 3. 233 uses 2, 3 and 3, so it is the odd one out.'),

    # ---------------- Section II · Star Questions
    dict(ch='1+10', scen='909 818 727 pattern · sixth number',
         fig=cards([909, 818, 727, '…'], size=40),
         stem='The numbers keep going down in the same way. What is the 6th number?',
         opts=['454', '545', '363', '464'],
         hint='Each number is 91 less than the one before. Look at each digit.',
         sol='The hundreds and ones digits go down by 1 and the tens digit goes up by 1. 909, 818, 727, 636, 545, 454. The 6th is 454.'),
    dict(ch='2+10', scen='sum of all even numbers from 2 to 20',
         stem='Rani adds all the even numbers from 2 to 20: 2 + 4 + 6 + … + 20. What total does she get?',
         opts=['110', '100', '120', '90'],
         hint='Pair the numbers: 2 + 20, 4 + 18, …',
         sol='Make pairs: 2 + 20, 4 + 18, 6 + 16, 8 + 14 and 10 + 12. Each pair makes 22, and there are 5 pairs. 22 + 22 + 22 + 22 + 22 = 110.'),
    dict(ch='5+10', scen='matchstick triangle pattern · sticks for four rows',
         fig=side([drawing(40, 40, tri_rows(1)), drawing(70, 60, tri_rows(2)), drawing(100, 90, tri_rows(3))]),
         stem='Naina makes these triangle patterns with matchsticks. 1 row uses 3 sticks, 2 rows use 9 sticks and 3 rows use 18 sticks. How many sticks does a pattern with 4 rows use?',
         opts=['30', '27', '24', '36'],
         hint='Look at how many sticks are added each time: 6, then 9.',
         sol='The sticks added go 6, then 9, so next 12 are added. 18 + 12 = 30. (Each row has 3 more sticks than the row above: 3 + 6 + 9 + 12 = 30.)'),
    dict(ch='1+9', scen='₹999 with the fewest notes and coins',
         stem='Tushar must pay ₹999. He can use ₹500, ₹200, ₹100, ₹50, ₹20 and ₹10 notes and ₹5, ₹2 and ₹1 coins. What is the fewest number of notes and coins he can use?',
         opts=['9', '6', '27', '10'],
         hint='Make 900, then 90, then 9.',
         sol='900 = 500 + 200 + 200 (3 notes). 90 = 50 + 20 + 20 (3 notes). 9 = 5 + 2 + 2 (3 coins). That is 3 + 3 + 3 = 9.'),
    dict(ch='5+9', scen='square corners on three ₹10 notes and two ₹5 coins',
         fig=money([{'items': [('note', 10), ('note', 10), ('note', 10), ('coin', 5), ('coin', 5)]}]),
         stem='Ekta puts three ₹10 notes and two ₹5 coins on the table. How many square corners do they have altogether?',
         opts=['12', '20', '14', '10'],
         hint='A note is a rectangle. A coin is a circle.',
         sol='Each note is a rectangle with 4 square corners: 4 + 4 + 4 = 12. The coins are circles with no corners. Total 12.'),
]
