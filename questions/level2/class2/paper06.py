# AMO Level-2 · Class 2 · Practice Paper 6  (format: see paper01.py)


def l_sticks(s=40):
    cells = [(0, 0), (0, 1), (1, 1)]
    segs = set()
    for c, r in cells:
        x, y = c * s, r * s
        segs |= {((x, y), (x + s, y)), ((x, y + s), (x + s, y + s)), ((x, y), (x, y + s)), ((x + s, y), (x + s, y + s))}
    return sorted(segs)


def house():
    return [('rect', 10, 60, 60, 60, 'yellow'), ('rect', 70, 60, 60, 60, 'yellow'),
            ('poly', [(10, 60), (70, 10), (130, 60)], 'pink')]


def rect_lines():
    return [('rect', 10, 10, 200, 100, 'green'), ('line', 10, 10, 210, 110), ('line', 10, 10, 110, 110),
            ('text', 110, 124, 'middle of the bottom side', 10)]


def path_grid():
    s = 50
    prims = []
    for k in range(3):
        prims += [('line', 20, 20 + k * s, 20 + 2 * s, 20 + k * s), ('line', 20 + k * s, 20, 20 + k * s, 20 + 2 * s)]
    prims += [('dot', 20, 20, 5), ('text', 8, 8, 'A', 13), ('dot', 120, 120, 5), ('text', 133, 133, 'B', 13)]
    return prims


def square_diagonals():
    return [('rect', 10, 10, 110, 110, 'blue'), ('line', 10, 10, 120, 120), ('line', 120, 10, 10, 120)]


QUESTIONS = [
    # ---------------- Part 1 · Number System
    dict(ch='1', scen='7 tens and 15 ones · how much more to make 200',
         stem='Gauri has 7 tens and 15 ones. How much more does she need to make 200?',
         opts=['115', '125', '185', '105'],
         hint='First find the number she has: 15 ones is 1 ten and 5 ones.',
         sol='7 tens and 15 ones is 70 + 15 = 85. To make 200 she needs 200 − 85 = 115.'),
    dict(ch='1', scen='largest 3-digit number with different digits minus 900',
         stem='Kabir writes the largest 3-digit number that has three different digits. He then takes away 900. What number does he get?',
         opts=['87', '99', '98', '78'],
         hint='The largest 3-digit number with different digits is not 999.',
         sol='The largest number with three different digits is 987. 987 − 900 = 87.'),
    dict(ch='1', scen='house numbers 457 to 464 with an odd tens digit',
         stem='The houses on a lane are numbered from 457 to 464. How many of these house numbers have an odd tens digit?',
         opts=['3', '4', '5', '8'],
         hint='Look at the tens digit of each number.',
         sol='457, 458 and 459 have tens digit 5, which is odd. 460 to 464 have tens digit 6, which is even. So 3 numbers.'),
    dict(ch='1', scen='start at 125 · add 100 twice · take 10 three times',
         stem='Diya starts at 125. She adds 100 two times. Then she takes away 10 three times. Where does she end?',
         opts=['295', '305', '325', '285'],
         hint='Adding 100 twice adds 200 in all.',
         sol='125 + 200 = 325. Taking away 10 three times takes away 30: 325 − 30 = 295.'),
    dict(ch='1', scen='odd 2-digit numbers with digit sum 7',
         stem='How many odd 2-digit numbers have digits that add up to 7?',
         opts=['3', '4', '7', '2'],
         hint='List all 2-digit numbers with digit sum 7, then keep the odd ones.',
         sol='Numbers with digit sum 7: 16, 25, 34, 43, 52, 61, 70. The odd ones are 25, 43 and 61. That is 3.'),
    dict(ch='1', scen='bus seats 101 to 150 ending in 5',
         stem='The seats in a hall are numbered 101 to 150. Yash sits on a seat whose number ends in 5. How many such seats are there?',
         opts=['5', '6', '4', '10'],
         hint='Seat numbers ending in 5 go up by 10.',
         sol='The seats are 105, 115, 125, 135 and 145. 155 is past 150. That is 5 seats.'),

    # ---------------- Part 2 · Operations
    dict(ch='2', scen='tea cups · sold some then got a new box',
         stem='A tea stall had 850 paper cups. It used 275 cups and then got 160 new cups. How many cups does it have now?',
         opts=['735', '415', '575', '745'],
         hint='Take away first, then add.',
         sol='850 − 275 = 575. 575 + 160 = 735.'),
    dict(ch='2', scen='eight boxes of seven crayons · two boxes used',
         stem='Ira has 8 boxes with 7 crayons in each box. She uses up all the crayons in 2 boxes. How many crayons are left?',
         opts=['42', '54', '49', '56'],
         hint='How many full boxes are left?',
         sol='8 − 2 = 6 boxes are left. 6 × 7 = 42 crayons.'),
    dict(ch='2', scen='half of 70 plus a quarter of 40',
         stem='Om gets half of 70 marbles from his brother and a quarter of 40 marbles from his sister. How many marbles does he get?',
         opts=['45', '35', '55', '25'],
         hint='Find each part separately.',
         sol='Half of 70 is 35. A quarter of 40 is 10. 35 + 10 = 45.'),
    dict(ch='2', scen='which pair of numbers has a difference of 199',
         stem='Which pair of numbers has a difference of 199?',
         opts=['400 and 201', '300 and 199', '400 and 211', '500 and 299'],
         hint='Think of 199 as 200 − 1.',
         sol='400 − 201 = 199. The others: 300 − 199 = 101, 400 − 211 = 189, 500 − 299 = 201.'),
    dict(ch='2', scen='8 packs of 9 stickers against 6 packs of 9',
         stem='Rohan has 8 packs of stickers and Kavya has 6 packs. Every pack has 9 stickers. How many more stickers does Rohan have?',
         opts=['18', '2', '72', '54'],
         hint='How many more packs does Rohan have?',
         sol='Rohan has 2 more packs. 2 × 9 = 18 more stickers. (Check: 72 − 54 = 18.)'),
    dict(ch='2', scen='three numbers in a row adding to 300',
         stem='Three numbers come one after the other, like 5, 6 and 7. They add up to 300. What is the largest of the three?',
         opts=['101', '100', '102', '99'],
         hint='The middle number is about a third of 300.',
         sol='99 + 100 + 101 = 300. The largest is 101.'),

    # ---------------- Part 3 · Geometry
    dict(ch='5', scen='matchsticks for an L shape of three squares',
         fig=sticks(l_sticks(), 80, 80),
         stem='Neha makes this shape of 3 squares with matchsticks. Each side of a small square is one matchstick. How many matchsticks does she use?',
         opts=['10', '12', '9', '8'],
         hint='Squares that touch share a matchstick.',
         sol='3 squares on their own would need 12 matchsticks. Two sides are shared, so 12 − 2 = 10 matchsticks.'),
    dict(ch='5', scen='house drawing · shapes with four sides',
         fig=drawing(140, 130, house()),
         stem='Vivaan draws this house with two squares and a roof. How many shapes with 4 sides can you find in it?',
         opts=['3', '2', '4', '5'],
         hint='Two squares side by side also make a bigger shape.',
         sol='There are 2 squares. Together they make a rectangle, which also has 4 sides. That is 3. The roof has 3 sides.'),
    dict(ch='5', scen='path traced by a cone rolling on a table',
         stem='Nisha lays an ice-cream cone on its side on a table and rolls it gently. The tip stays in one place. What shape does the round edge trace on the table?',
         opts=['A circle', 'A straight line', 'A square', 'A triangle'],
         hint='The tip does not move, so the cone turns around it.',
         sol='A cone lying on its side turns around its tip. The round edge stays the same distance from the tip, so it traces a circle.'),
    dict(ch='5', scen='rectangle with two lines from the top-left corner · count triangles',
         fig=drawing(220, 130, rect_lines()),
         stem='Manav draws a rectangle. He draws two lines from the top-left corner: one to the bottom-right corner and one to the middle of the bottom side. How many triangles are there?',
         opts=['4', '3', '2', '5'],
         hint='Do not forget the triangle above the long line.',
         sol='Below the long line there are 3 triangles: the left one, the middle one and both together. Above the long line there is 1 more triangle. 3 + 1 = 4.'),
    dict(ch='5', scen='squares in a 2 by 4 grid',
         fig=grid([[''] * 4, [''] * 4], cell=40),
         stem='How many squares of all sizes are in this grid?',
         opts=['11', '8', '10', '12'],
         hint='Count small squares, then squares made of 4 small ones.',
         sol='There are 8 small squares. A 2 by 2 square can start in 3 places along the row. 8 + 3 = 11.'),

    # ---------------- Part 4 · Applied Mathematics
    dict(ch='9', scen='clock at half past two',
         fig=clocks([(2, 30)]),
         stem='Aditi\'s music class starts at the time on this clock. What time does it start?',
         opts=['Half past 2', 'Half past 6', 'Half past 3', 'Quarter past 2'],
         hint='At half past, the hour hand is between two numbers.',
         sol='The minute hand points at 6, so it is half past. The hour hand is between 2 and 3, so it is half past 2.'),
    dict(ch='9', scen='2 pens cost ₹30 · price of 5 pens',
         stem='At a shop, Pooja sees that 2 pens cost ₹30. All the pens cost the same. How much will 5 pens cost?',
         opts=['₹75', '₹60', '₹150', '₹65'],
         hint='First find the cost of 1 pen.',
         sol='Half of ₹30 is ₹15, so 1 pen costs ₹15. 5 pens cost 15 + 15 + 15 + 15 + 15 = ₹75.'),
    dict(ch='9', scen='shop open 10 AM to 8 PM · when is it closed',
         stem='A shop opens at 10 AM and closes at 8 PM. At which of these times is the shop closed?',
         opts=['9:30 PM', '11:00 AM', '7:30 PM', '2:00 PM'],
         hint='PM times after 8 PM are after closing.',
         sol='The shop is open from 10 in the morning to 8 at night. 9:30 PM is after 8 PM, so it is closed. The other times are between 10 AM and 8 PM.'),
    dict(ch='9', scen='saving ₹5 a day for 9 days · spend ₹18',
         stem='Harsh saves ₹5 every day for 9 days. Then he buys a toy for ₹18. How much money is left?',
         opts=['₹27', '₹45', '₹63', '₹23'],
         hint='First find how much he saved.',
         sol='He saves 5 × 9 = ₹45. After the toy: ₹45 − ₹18 = ₹27.'),

    # ---------------- Part 5 · Mathematical Reasoning
    dict(ch='10', scen='double then take one pattern',
         fig=cards([3, 6, 5, 10, 9, 18, '?'], size=36),
         stem='This pattern uses two steps again and again. Which number comes next?',
         opts=['17', '36', '19', '27'],
         hint='Look at 3 to 6, then 6 to 5.',
         sol='The steps are: double, then take away 1. 3 → 6 → 5 → 10 → 9 → 18 → 17.'),
    dict(ch='10', scen='number machine adding the two digits',
         fig=equations([['27', '→', '9'], ['35', '→', '8'], ['46', '→', '?']], size=30),
         stem='Each number on the left is changed by the same rule. Which number replaces the question mark?',
         opts=['10', '12', '15', '23'],
         hint='Look at the two digits of each number.',
         sol='2 + 7 = 9 and 3 + 5 = 8, so the rule adds the two digits. 4 + 6 = 10.'),
    dict(ch='10', scen='shortest paths from A to B on a 2 by 2 grid',
         fig=drawing(150, 150, path_grid()),
         stem='Sana walks along the lines from A to B. She only moves right or down. How many different paths can she take?',
         opts=['6', '4', '8', '5'],
         hint='Every path has 2 steps right and 2 steps down.',
         sol='Write R for right and D for down. The paths are RRDD, RDRD, RDDR, DRRD, DRDR, DDRR. That is 6 paths.'),
    dict(ch='10', scen='odd one out · numbers made by a number times itself',
         stem='Three of these numbers are made by multiplying a number by itself, like 3 × 3 = 9. Which number is the odd one out: 16, 25, 36, 48?',
         opts=['48', '16', '25', '36'],
         hint='Try 4 × 4, 5 × 5 and 6 × 6.',
         sol='16 = 4 × 4, 25 = 5 × 5 and 36 = 6 × 6. 48 is not a number times itself (6 × 6 = 36 and 7 × 7 = 49), so 48 is the odd one out.'),

    # ---------------- Section II · Star Questions
    dict(ch='1+10', scen='counting in 25s · tenth number',
         fig=cards([25, 50, 75, 100, '…'], size=40),
         stem='Riya counts in 25s starting from 25. What is the 10th number she says?',
         opts=['250', '225', '275', '200'],
         hint='Every 4 numbers she reaches the next hundred.',
         sol='The 4th number is 100 and the 8th is 200. The 9th is 225 and the 10th is 250.'),
    dict(ch='2+10', scen='one counts up by 5 and the other down by 3 · when they meet',
         stem='Ravi starts at 7 and adds 5 each turn. Asha starts at 47 and takes away 3 each turn. Both of them move once every turn. On which number are they both at the same time?',
         opts=['32', '27', '35', '29'],
         hint='Write both lists side by side.',
         sol='Ravi: 7, 12, 17, 22, 27, 32. Asha: 47, 44, 41, 38, 35, 32. After 5 turns both are at 32.'),
    dict(ch='5+10', scen='square with both diagonals · count triangles',
         fig=drawing(130, 130, square_diagonals()),
         stem='Kunal draws a square and both of its corner-to-corner lines. How many triangles are there in all?',
         opts=['8', '4', '6', '10'],
         hint='Count the small ones and then those made of two small ones.',
         sol='There are 4 small triangles. Each corner-to-corner line cuts the square into 2 big triangles, so there are 4 big triangles. 4 + 4 = 8.'),
    dict(ch='1+9', scen='birthday date riddle in a 30-day month',
         stem='Ananya\'s birthday is in a month with 30 days. The date is an odd number and its digits add up to 4. On which date is her birthday?',
         opts=['13th', '22nd', '31st', '4th'],
         hint='The date must be from 1 to 30.',
         sol='Dates whose digits add up to 4: 4, 13, 22, 31. 4 and 22 are even. 31 is not in a 30-day month. So the date is the 13th.'),
    dict(ch='5+9', scen='buying every sphere-shaped item in a shop',
         fig=objects([{'items': ['⚽', '⚽', '⚽'], 'label': '₹25 each'}, {'items': ['🥫', '🥫'], 'label': '₹30 each'},
                      {'items': ['🎲', '🎲'], 'label': '₹10 each'}], item=36),
         stem='Parth buys every item in this shop that has the shape of a sphere. How much does he pay?',
         opts=['₹75', '₹60', '₹25', '₹95'],
         hint='Only the balls are spheres. A can is a cylinder and a dice is a cube.',
         sol='The 3 balls are spheres. They cost 25 + 25 + 25 = ₹75.'),
]
