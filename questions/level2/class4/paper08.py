# AMO Level-2 · Class 4 · Practice Paper 8  (format: see paper01.py)


def pict(rows, em, key, lw=90, step=28):
    prims = []
    for i, (lab, n) in enumerate(rows):
        y = 18 + i * 34
        prims += [('rect', 0, y - 15, lw, 30, 'lilac'), ('text', lw / 2, y, lab, 12)]
        prims += [('emoji', em, lw + 20 + k * step, y, 24) for k in range(n)]
    y = 18 + len(rows) * 34 + 6
    prims += [('emoji', em, 14, y, 20), ('text', 40 + len(key) * 3.6, y, '= ' + key, 12)]
    return prims


def nline(labels, ticks, x0=20, x1=380):
    """Number line with equally spaced ticks; labels maps tick index to text."""
    prims = [('line', x0 - 12, 20, x1 + 12, 20)]
    for i in range(ticks):
        x = x0 + i * (x1 - x0) / (ticks - 1)
        prims.append(('line', x, 13, x, 27))
        if i in labels:
            prims.append(('text', x, 42, labels[i], 12))
    return prims


def letter_net():
    s, prims = 34, []
    cells = {'A': (0, 0), 'B': (0, 1), 'C': (1, 1), 'D': (1, 2), 'E': (2, 2), 'F': (2, 3)}
    for lab, (r, c) in cells.items():
        prims += [('rect', c * s, r * s, s, s, 'yellow'), ('text', c * s + s / 2, r * s + s / 2, lab, 15)]
    return prims


def plus_shape():
    s = 24
    cells = [(0, 1), (1, 0), (1, 1), (1, 2), (2, 1)]
    prims = [('rect', 10 + c * s, 10 + r * s, s, s, 'green') for r, c in cells]
    prims.append(('text', 10 + 1.5 * s, 10 + 3 * s + 12, 'each square: 2 cm by 2 cm', 10))
    return prims


QUESTIONS = [
    # ---------------- Part 1 · Number System
    dict(ch='1', scen='largest minus smallest 5-digit number from 2 4 6 8 0',
         stem='Sneha makes the largest and the smallest 5-digit numbers using each of the digits 2, 4, 6, 8 and 0 once. What is the difference between them?',
         opts=['65,952', '61,740', '64,952', '66,952'],
         hint='The smallest number cannot start with 0.',
         sol='Largest: 86,420. Smallest: 20,468 (0 goes second). 86,420 − 20,468 = 65,952.'),
    dict(ch='1', scen='point on a number line between 36,000 and 37,000 · 1,250 more',
         fig=drawing(400, 50, nline({0: '36,000', 3: 'P', 4: '37,000'}, 5)),
         stem='The marks on this number line are equally spaced. What number is 1,250 more than the number at P?',
         opts=['38,000', '37,750', '37,500', '38,250'],
         hint='There are 4 equal gaps between 36,000 and 37,000.',
         sol='Each gap is 1,000 ÷ 4 = 250. P is 3 gaps after 36,000: 36,750. 36,750 + 1,250 = 38,000.'),
    dict(ch='1', scen='age XLVIII · years until written with one Roman letter',
         stem='Mohit\'s grandfather writes his age as XLVIII. In how many years will his age first be written with just one Roman letter?',
         opts=['2', '12', '52', '1'],
         hint='Which Roman letters stand for numbers bigger than 48?',
         sol='XLVIII = 48. The one-letter numerals above 48 are L (50) and C (100). He reaches 50 first, in 2 years.'),

    # ---------------- Part 2 · Operations
    dict(ch='2', scen='1,248 students in 8 groups then 4 teams each',
         stem='At a sports meet, 1,248 students are put into 8 equal groups. Each group is then split into 4 equal teams. How many students are in each team?',
         opts=['39', '156', '312', '49'],
         hint='Divide by 8, then by 4.',
         sol='1,248 ÷ 8 = 156 students in each group. 156 ÷ 4 = 39 students in each team.'),
    dict(ch='2', scen='sum of all six numbers made from 1 2 3',
         stem='Raj makes all the 3-digit numbers that use each of the digits 1, 2 and 3 once. What is the sum of all his numbers?',
         opts=['1,332', '666', '1,233', '1,998'],
         hint='Each digit appears twice in the hundreds place, twice in the tens place and twice in the ones place.',
         sol='The numbers are 123, 132, 213, 231, 312, 321. Each place has each digit twice, so each place adds to 2 × (1 + 2 + 3) = 12. Sum = 1,200 + 120 + 12 = 1,332.'),
    dict(ch='2', scen='box times 12 equals 960 plus 12 times 5',
         fig=equations([['? × 12', '=', '960', '+', '12 × 5']], size=30),
         stem='Kriti makes both sides equal. Which number does she put in the box?',
         opts=['85', '80', '75', '1,020'],
         hint='960 = 12 × 80.',
         sol='960 = 12 × 80, so the right side is 12 × 80 + 12 × 5 = 12 × 85. The box is 85. (Check: 960 + 60 = 1,020 = 85 × 12.)'),

    # ---------------- Part 3 · Fractions & Decimals
    dict(ch='3', scen='a third cricket a quarter football and 20 hockey · class size',
         stem='In Vani\'s class, 1/3 of the students like cricket best and 1/4 like football best. The other 20 students like hockey best. How many students are in the class?',
         opts=['48', '40', '60', '35'],
         hint='What fraction of the class likes hockey?',
         sol='Cricket and football: 1/3 + 1/4 = 4/12 + 3/12 = 7/12. Hockey: 5/12 of the class = 20, so 1/12 = 4 students. The class has 12 × 4 = 48 students.'),
    dict(ch='3', scen='which pair of fractions is equal',
         stem='Which pair of fractions are equal to each other?',
         opts=['4/6 and 6/9', '3/4 and 4/5', '5/10 and 6/11', '2/3 and 3/4'],
         hint='Write each fraction in its simplest form.',
         sol='4/6 = 2/3 and 6/9 = 2/3, so they are equal. 3/4 is less than 4/5. 5/10 is exactly 1/2 but 6/11 is more than 1/2. 2/3 is less than 3/4.'),
    dict(ch='3', scen='two numbers from 2.7 4.6 3.9 1.8 with sum closest to 6',
         stem='Sahil picks two of these numbers: 2.7, 4.6, 3.9, 1.8. He wants their sum to be as close to 6 as possible. Which two should he pick?',
         opts=['3.9 and 1.8', '4.6 and 1.8', '2.7 and 3.9', '2.7 and 4.6'],
         hint='Work out each sum and how far it is from 6.',
         sol='3.9 + 1.8 = 5.7 (0.3 away). 4.6 + 1.8 = 6.4 (0.4 away). 2.7 + 3.9 = 6.6 (0.6 away). 2.7 + 4.6 = 7.3. The closest is 3.9 and 1.8.'),
    dict(ch='3', scen='6 1/3 L of water with 2 3/4 L used',
         stem='A bucket has 6 1/3 L of water. Gopal uses 2 3/4 L to water plants. How much water is left?',
         opts=['3 7/12 L', '4 7/12 L', '3 5/12 L', '4 1/12 L'],
         hint='Write the fractions as twelfths. 1/3 is less than 3/4, so you need to borrow 1.',
         sol='6 1/3 = 6 4/12 = 5 16/12. 2 3/4 = 2 9/12. 5 16/12 − 2 9/12 = 3 7/12 L.'),

    # ---------------- Part 4 · Geometry
    dict(ch='5', scen='lettered staircase net · face opposite A',
         fig=drawing(140, 105, letter_net()),
         stem='This net is folded to make a cube. Which letter is on the face opposite A?',
         opts=['D', 'B', 'C', 'F'],
         hint='Fold with C on the bottom. Where do B, A and D go?',
         sol='With C on the bottom, B folds up as the back, A as the left side and D as the right side. E becomes the front and F the top. So A (left) is opposite D (right). Also B is opposite E and C is opposite F.'),
    dict(ch='5', scen='pairs of parallel edges of a cube',
         stem='A cube has 12 edges. How many pairs of edges are parallel to each other?',
         opts=['18', '12', '6', '24'],
         hint='The edges go in 3 directions, with 4 edges in each direction.',
         sol='There are 4 upright edges, 4 left-right edges and 4 front-back edges. In each set of 4 parallel edges there are 6 pairs (4 × 3 ÷ 2). 3 × 6 = 18 pairs.'),
    dict(ch='5', scen='shape that can never be a view of a cylinder',
         stem='Malti looks at a cylinder from different directions. Which of these shapes can she NEVER see as a view?',
         opts=['A triangle', 'A circle', 'A rectangle', 'A square'],
         hint='A cylinder can be short and wide or tall and thin.',
         sol='From the top a cylinder looks like a circle. From the side it looks like a rectangle, and if its height equals its width that rectangle is a square. It has no pointed parts, so it never looks like a triangle.'),

    # ---------------- Part 5 · Mensuration
    dict(ch='6', scen='5 cm by 3 cm rectangle with both sides doubled · increase in area',
         stem='A rectangle is 5 cm long and 3 cm wide. Esha doubles both its length and its width. By how much does the area grow?',
         opts=['45 cm²', '15 cm²', '30 cm²', '60 cm²'],
         hint='Find the new area. It is not just double the old one.',
         sol='Old area: 5 × 3 = 15 cm². New rectangle: 10 cm by 6 cm, area 60 cm². Growth: 60 − 15 = 45 cm². (The area becomes 4 times as big.)'),
    dict(ch='6', scen='two 2 m paths crossing in a 30 m by 20 m garden',
         stem='A garden is 30 m long and 20 m wide. Two paths, each 2 m wide, cross in the middle: one runs the whole length and one the whole width. What is the area of the paths?',
         opts=['96 m²', '100 m²', '104 m²', '92 m²'],
         hint='The square where the paths cross must be counted only once.',
         sol='Long path: 30 × 2 = 60 m². Short path: 20 × 2 = 40 m². The crossing square of 2 × 2 = 4 m² is in both. 60 + 40 − 4 = 96 m².'),
    dict(ch='6', scen='3 kg 200 g of sugar in 400 g packets',
         stem='A shopkeeper fills packets with 400 g of sugar each. How many packets can he fill from 3 kg 200 g of sugar?',
         opts=['8', '80', '7', '9'],
         hint='Change 3 kg 200 g to grams.',
         sol='3 kg 200 g = 3,200 g. 400 g × 8 = 3,200 g. So 8 packets.'),
    dict(ch='6', scen='perimeter of a plus shape of five 2 cm squares',
         fig=drawing(90, 100, plus_shape()),
         stem='This plus shape is made of 5 squares, each 2 cm by 2 cm. What is its perimeter?',
         opts=['24 cm', '20 cm', '40 cm', '12 cm'],
         hint='Count the square sides on the outside.',
         sol='Each of the 4 arms shows 3 outside sides, and the middle square shows none. 4 × 3 = 12 sides of 2 cm. 12 × 2 = 24 cm.'),

    # ---------------- Part 6 · Data Handling
    dict(ch='8', scen='pictograph of birds in parks with one row missing',
         fig=drawing(300, 125, pict([('Park A', 5), ('Park B', 3), ('Park C', 0)], '🐦', '4 birds')),
         stem='Children counted 52 birds in three parks. The row for Park C is still empty. How many symbols should be drawn for Park C?',
         opts=['5', '8', '13', '20'],
         hint='How many symbols stand for 52 birds?',
         sol='52 birds = 52 ÷ 4 = 13 symbols. Parks A and B have 5 + 3 = 8 symbols. Park C needs 13 − 8 = 5 symbols.'),

    # ---------------- Part 7 · Applied Mathematics
    dict(ch='9', scen='shop open in two parts of the day · total time',
         stem='A shop is open from 9:35 AM to 1:10 PM and again from 3:45 PM to 8:20 PM. For how long is it open in all?',
         opts=['8 h 10 min', '7 h 10 min', '8 h 50 min', '9 h 10 min'],
         hint='Find each part separately.',
         sol='9:35 AM to 1:10 PM: 3 h 35 min. 3:45 PM to 8:20 PM: 4 h 35 min. Total: 7 h 70 min = 8 h 10 min.'),
    dict(ch='9', scen='1 January Thursday · date of the first Sunday in March',
         stem='In a year that is not a leap year, 1 January is a Thursday. On which date is the first Sunday in March?',
         opts=['1 March', '4 March', '2 March', '7 March'],
         hint='Find the day of the week of 1 March.',
         sol='1 March is 31 + 28 = 59 days after 1 January. 59 = 8 weeks + 3 days. 3 days after Thursday is Sunday, so 1 March is itself a Sunday.'),
    dict(ch='9', scen='3 for ₹40 or 5 for ₹65 when buying 15',
         stem='A shop sells notebooks at 3 for ₹40. Another shop sells the same notebooks at 5 for ₹65. Lata needs 15 notebooks. Which shop is cheaper, and by how much?',
         opts=['The second shop, by ₹5', 'The first shop, by ₹5', 'The second shop, by ₹15', 'Both cost the same'],
         hint='15 notebooks are 5 packs of 3 or 3 packs of 5.',
         sol='First shop: 5 × 40 = ₹200. Second shop: 3 × 65 = ₹195. The second shop is cheaper by ₹5.'),

    # ---------------- Part 8 · Mathematical Reasoning
    dict(ch='10', scen='series 2 5 10 17 26',
         fig=cards([2, 5, 10, 17, 26, '?'], size=40),
         stem='Raghav\'s series adds a different odd number each time. Which number comes next?',
         opts=['37', '35', '36', '39'],
         hint='The numbers added are 3, 5, 7, …',
         sol='The series adds 3, 5, 7, 9. Next it adds 11: 26 + 11 = 37.'),
    dict(ch='10', scen='digits A where A times A ends in A',
         fig=equations([['A', '×', 'A', '=', 'B A']], size=32),
         stem='A and B are different digits, and BA is a 2-digit number. For how many digits A is this true?',
         opts=['2', '1', '3', '4'],
         hint='Look for a digit whose square ends in the same digit.',
         sol='Squares that are 2-digit numbers: 16, 25, 36, 49, 64, 81. Only 25 (A = 5) and 36 (A = 6) end in A. So 2 digits work.'),
    dict(ch='10', scen='numbers 1 to 100 with digit sum 9',
         stem='How many numbers from 1 to 100 have digits that add up to 9?',
         opts=['10', '9', '11', '8'],
         hint='Start with 9, then 18, 27, …',
         sol='They are 9, 18, 27, 36, 45, 54, 63, 72, 81 and 90. That is 10 numbers.'),
    dict(ch='10', scen='age now from twice the age 5 years ago',
         stem='In 5 years, Meera will be twice as old as she was 5 years ago. How old is Meera now?',
         opts=['15', '10', '20', '25'],
         hint='Try some ages. For age 12: in 5 years 17, 5 years ago 7.',
         sol='Try 15: in 5 years she will be 20, and 5 years ago she was 10. 20 is twice 10. So Meera is 15.'),

    # ---------------- Section II · Star Questions
    dict(ch='3+10', scen='twelfths from 1/12 to 11/12 that simplify',
         stem='Ananya writes the fractions 1/12, 2/12, 3/12, …, 11/12. How many of them can be written with a smaller denominator?',
         opts=['7', '4', '6', '5'],
         hint='Which tops share a factor with 12, like 2/12 = 1/6?',
         sol='2/12 = 1/6, 3/12 = 1/4, 4/12 = 1/3, 6/12 = 1/2, 8/12 = 2/3, 9/12 = 3/4, 10/12 = 5/6. That is 7. 1/12, 5/12, 7/12 and 11/12 cannot be simplified.'),
    dict(ch='9+10', scen='day after tomorrow is Sunday · day in 100 days',
         stem='The day after tomorrow is a Sunday. What day of the week will it be 100 days from today?',
         opts=['Sunday', 'Friday', 'Tuesday', 'Saturday'],
         hint='First find today.',
         sol='The day after tomorrow is Sunday, so today is Friday. 100 = 14 weeks + 2 days. 2 days after Friday is Sunday.'),
    dict(ch='1+10', scen='5-digit palindromes whose digits add up to 9',
         stem='A palindrome reads the same both ways, like 12,321. How many 5-digit palindromes have digits that add up to 9?',
         opts=['10', '9', '8', '12'],
         hint='In a palindrome ABCBA, the digit sum is 2A + 2B + C. Try A = 1, 2, 3, 4.',
         sol='2A + 2B + C = 9. A = 1: 2B + C = 7, so B = 0, 1, 2 or 3 (4 ways). A = 2: 2B + C = 5, B = 0, 1, 2 (3 ways). A = 3: 2B + C = 3, B = 0 or 1 (2 ways). A = 4: B = 0, C = 1 (1 way). 4 + 3 + 2 + 1 = 10.'),
    dict(ch='3+9', scen='buying 2 1/2 m and 1 3/4 m of cloth at ₹120 a metre',
         stem='Cloth costs ₹120 per metre. Sita buys 2 1/2 m of blue cloth and 1 3/4 m of red cloth. How much does she pay?',
         opts=['₹510', '₹480', '₹540', '₹420'],
         hint='Add the lengths first.',
         sol='2 1/2 + 1 3/4 = 2 2/4 + 1 3/4 = 4 1/4 m. 4 m cost 4 × 120 = ₹480. 1/4 m costs 1/4 of 120 = ₹30. Total ₹510.'),
    dict(ch='5+6', scen='rectangle folded in half along its length · drop in perimeter',
         stem='A sheet of paper is 12 cm long and 8 cm wide. Rupa folds it in half so that the two 8 cm sides meet. How much smaller is the perimeter of the folded shape than that of the sheet?',
         opts=['12 cm', '8 cm', '20 cm', '16 cm'],
         hint='After folding, the shape is 6 cm long and 8 cm wide.',
         sol='Sheet: 2 × (12 + 8) = 40 cm. Folded: 6 cm by 8 cm, so 2 × (6 + 8) = 28 cm. 40 − 28 = 12 cm.'),
]
