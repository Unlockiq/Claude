# AMO Level-2 · Class 5 · Practice Paper 8  (format: see paper01.py)


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


def u_shape():
    s = 9
    P = lambda x, y: (10 + x * s, 10 + y * s)
    return [('poly', [P(0, 0), P(7, 0), P(7, 4), P(13, 4), P(13, 0), P(20, 0), P(20, 12), P(0, 12)], 'yellow'),
            ('text', *P(10, 13.2), '20 cm', 11), ('text', *P(-2.2, 6), '12 cm', 11), ('text', *P(10, 3), '6 cm', 10),
            ('text', *P(14.8, 2), '4 cm', 10)]


QUESTIONS = [
    # ---------------- Part 1 · Number System
    dict(ch='1', scen='even factors of 60',
         stem='How many of the factors of 60 are even numbers?',
         opts=['8', '12', '6', '4'],
         hint='List all the factors of 60 in pairs.',
         sol='Factors of 60: 1, 2, 3, 4, 5, 6, 10, 12, 15, 20, 30, 60. The even ones are 2, 4, 6, 10, 12, 20, 30, 60: 8 of them.'),
    dict(ch='1', scen='laddoos barfis and jalebis packed in equal boxes · fewest boxes',
         stem='A sweet shop packs 120 laddoos, 168 barfis and 216 jalebis into boxes. Each box has only one kind of sweet, and every box has the same number of sweets. What is the fewest number of boxes needed?',
         opts=['21', '24', '18', '36'],
         hint='Put as many sweets as possible in each box: use the HCF.',
         sol='HCF of 120, 168 and 216 is 24, so each box holds 24 sweets. Boxes: 120 ÷ 24 = 5, 168 ÷ 24 = 7, 216 ÷ 24 = 9. 5 + 7 + 9 = 21.'),
    dict(ch='1', scen='greatest 6-digit number with digit sum 10',
         stem='What is the greatest 6-digit number whose digits add up to 10?',
         opts=['9,10,000', '9,01,000', '1,00,009', '9,00,001'],
         hint='Make the lakhs digit as big as possible, then the next digit.',
         sol='Put 9 in the lakhs place. The remaining digits must add up to 1, and the 1 should be as far left as possible: 9,10,000.'),

    # ---------------- Part 2 · Operations
    dict(ch='2', scen='18 minus box times 4 plus 6 equals 50',
         fig=equations([['(18 − ?) × 4 + 6', '=', '50']], size=30),
         stem='Lokesh wants this number sentence to be true. Which number should replace the question mark?',
         opts=['7', '11', '4', '14'],
         hint='Work backwards: undo the + 6, then the × 4.',
         sol='50 − 6 = 44. 44 ÷ 4 = 11, so 18 − ? = 11 and ? = 7.'),
    dict(ch='2', scen='7,890 divided by 39 estimated as 8,000 divided by 40',
         stem='Kunal estimates 7,890 ÷ 39 as 8,000 ÷ 40 = 200. What is the exact whole-number quotient of 7,890 ÷ 39?',
         opts=['202', '200', '198', '203'],
         hint='39 × 200 = 7,800. How much is left?',
         sol='39 × 200 = 7,800, leaving 90. 90 contains 39 two times (78), leaving 12. So 7,890 ÷ 39 = 202 remainder 12.'),
    dict(ch='2', scen='odd one out among products equal to 2,800',
         stem='Three of these products have the same value. Which is the odd one out?',
         opts=['70 × 60', '25 × 16 × 7', '50 × 8 × 7', '100 × 28'],
         hint='Work out each product, using easy pairs like 25 × 4.',
         sol='25 × 16 × 7 = 400 × 7 = 2,800. 50 × 8 × 7 = 400 × 7 = 2,800. 100 × 28 = 2,800. 70 × 60 = 4,200.'),

    # ---------------- Part 3 · Fractions, Decimals & Percentages
    dict(ch='3', scen='500 students passing English and Maths · failed both',
         stem='Of 500 students, 64% passed English, 72% passed Maths and 48% passed both. How many students failed both subjects?',
         opts=['60', '40', '80', '140'],
         hint='Students who passed both are counted in both 64% and 72%.',
         sol='Passed at least one: 64% + 72% − 48% = 88%. Failed both: 12% of 500 = 60.'),
    dict(ch='3', scen='largest of 0.7 times 0.7 0.5 0.25 times 2.1 and 3/5 minus 0.1',
         stem='Which of these has the largest value?',
         opts=['0.25 × 2.2', '0.5', '0.7 × 0.7', '3/5 − 0.1'],
         hint='Work out each one as a decimal.',
         sol='0.25 × 2.2 = 0.55. 0.7 × 0.7 = 0.49. 3/5 − 0.1 = 0.6 − 0.1 = 0.5. The largest is 0.55.'),
    dict(ch='3', scen='2.5 m rope cut into 4 pieces then each halved',
         stem='Ankita cuts a rope 2.5 m long into 4 equal pieces. Then she cuts each piece in half. How long is each small piece?',
         opts=['31.25 cm', '62.5 cm', '3.125 cm', '32 cm'],
         hint='The rope is cut into 8 equal pieces in all. 2.5 m = 250 cm.',
         sol='4 pieces each cut in half makes 8 equal pieces. 250 cm ÷ 8 = 31.25 cm.'),
    dict(ch='3', scen='2 1/4 kg plus 1 3/5 kg as a decimal',
         stem='Kusum buys 2 1/4 kg of potatoes and 1 3/5 kg of onions. What is the total weight, written as a decimal?',
         opts=['3.85 kg', '3.45 kg', '3.8 kg', '4.85 kg'],
         hint='1/4 = 0.25 and 3/5 = 0.6.',
         sol='2 1/4 = 2.25 and 1 3/5 = 1.6. 2.25 + 1.6 = 3.85 kg.'),

    # ---------------- Part 4 · Geometry
    dict(ch='5', scen='fourth angle of a quadrilateral 75 105 110',
         stem='Three angles of a four-sided shape are 75°, 105° and 110°. What is the fourth angle, and what type of angle is it?',
         opts=['70°, acute', '80°, acute', '110°, obtuse', '70°, obtuse'],
         hint='The angles of a four-sided shape add up to 360°.',
         sol='75 + 105 + 110 = 290. 360° − 290° = 70°, which is less than 90°: acute.'),
    dict(ch='5', scen='which triangle cannot exist',
         stem='Which of these triangles can NOT exist?',
         opts=['A right-angled equilateral triangle', 'A right-angled isosceles triangle', 'An obtuse-angled scalene triangle', 'An acute-angled isosceles triangle'],
         hint='What are the angles of an equilateral triangle?',
         sol='An equilateral triangle has three 60° angles, so it can never have a 90° angle. The others exist: 90°, 45°, 45°; 120°, 40°, 20°; 70°, 70°, 40°.'),
    dict(ch='5', scen='square folded along both diagonals with one hole punched',
         stem='Leena folds a square sheet along one diagonal, then folds it in half again along the other diagonal. She punches one hole through all the layers, away from the folds. How many holes are there when she opens it?',
         opts=['4', '2', '8', '1'],
         hint='Count how many layers of paper there are after the two folds.',
         sol='The first fold makes 2 layers; the second makes 4 layers. One punch goes through all 4 layers, so there are 4 holes.'),

    # ---------------- Part 5 · Mensuration
    dict(ch='6', scen='3,600 L tank with a 2 m by 1.2 m base · depth',
         stem='A cuboid water tank holds 3,600 litres when full. Its base is 2 m long and 1.2 m wide. How deep is it? (1 m³ = 1,000 L)',
         opts=['1.5 m', '15 m', '1.2 m', '3 m'],
         hint='Change 3,600 L into cubic metres first.',
         sol='3,600 L = 3.6 m³. Base area: 2 × 1.2 = 2.4 m². Depth: 3.6 ÷ 2.4 = 1.5 m.'),
    dict(ch='6', scen='perimeter of a U shape 20 by 12 with a 6 by 4 notch',
         fig=drawing(200, 130, u_shape()),
         stem='A 6 cm by 4 cm piece is cut from the middle of the top of a 20 cm by 12 cm rectangle, as shown. What is the perimeter of the shape?',
         opts=['72 cm', '64 cm', '76 cm', '68 cm'],
         hint='Compare the outline with the outline of the full rectangle.',
         sol='The full rectangle has perimeter 2 × (20 + 12) = 64 cm. The notch removes 6 cm of top edge but adds 4 + 6 + 4 = 14 cm. 64 − 6 + 14 = 72 cm.'),
    dict(ch='6', scen='right triangular plot area 1,200 m² with a 60 m side · fence along two sides',
         stem='A right-angled triangular plot has an area of 1,200 m². One of the sides at the right angle is 60 m. A fence along the two sides at the right angle costs ₹25 per metre. What is the cost?',
         opts=['₹2,500', '₹1,500', '₹30,000', '₹5,000'],
         hint='Find the other side at the right angle first.',
         sol='Half of 60 × (other side) = 1,200, so 60 × (other side) = 2,400 and the other side is 40 m. Fence: 60 + 40 = 100 m. Cost: 100 × 25 = ₹2,500.'),

    # ---------------- Part 6 · Data Handling
    dict(ch='8', scen='pictograph of library books by language · percent English',
         fig=drawing(300, 190, pict([('Hindi', 7), ('English', 5), ('Marathi', 4), ('Tamil', 4)], '📗', '50 books')),
         stem='The pictograph shows the books in a library by language. What percentage of all the books are in English?',
         opts=['25%', '20%', '50%', '5%'],
         hint='Count all the symbols.',
         sol='Total symbols: 7 + 5 + 4 + 4 = 20. English: 5 out of 20 = 1/4 = 25%. (In books: 250 out of 1,000.)'),

    # ---------------- Part 7 · Applied Mathematics
    dict(ch='9', scen='cyclists in opposite directions at 12 and 18 km/h for 40 minutes',
         stem='Two cyclists start from the same place and ride in opposite directions at 12 km/h and 18 km/h. How far apart are they after 40 minutes?',
         opts=['20 km', '30 km', '4 km', '12 km'],
         hint='Each hour they move 12 + 18 km further apart.',
         sol='They separate at 30 km per hour. 40 minutes is 2/3 of an hour: 2/3 × 30 = 20 km.'),
    dict(ch='9', scen='3 h at average 50 km/h then 2 h at 60 km/h',
         stem='A car travels for 3 hours at an average of 50 km/h and then for 2 hours at 60 km/h. What is its average speed for the 5 hours?',
         opts=['54 km/h', '55 km/h', '52 km/h', '56 km/h'],
         hint='Find the total distance first.',
         sol='Distance: 3 × 50 + 2 × 60 = 150 + 120 = 270 km. 270 ÷ 5 = 54 km/h. (55 is the plain average of 50 and 60.)'),
    dict(ch='9', scen='light on from 6:45 PM to 5:30 AM for a week',
         stem='A garden light is on from 6:45 PM to 5:30 AM every night. For how long is it on in one week?',
         opts=['75 h 15 min', '74 h 15 min', '76 h 45 min', '73 h 45 min'],
         hint='Find the time for one night first.',
         sol='6:45 PM to 5:30 AM is 10 h 45 min. For 7 nights: 70 h + 7 × 45 min = 70 h + 315 min = 70 h + 5 h 15 min = 75 h 15 min.'),
    dict(ch='9', scen='4 cinema tickets and 2 popcorns shared equally',
         stem='Four friends go to a film. Each ticket costs ₹180 and they buy 2 tubs of popcorn at ₹95.50 each. They share the total cost equally. How much does each pay?',
         opts=['₹227.75', '₹275.50', '₹223.75', '₹227.50'],
         hint='Find the total cost first.',
         sol='Tickets: 4 × 180 = ₹720. Popcorn: 2 × 95.50 = ₹191. Total ₹911. Each: 911 ÷ 4 = ₹227.75.'),

    # ---------------- Part 8 · Mathematical Reasoning
    dict(ch='10', scen='series with differences 3 6 9 12',
         fig=cards([7, 10, 16, 25, 37, '?'], size=38),
         stem='Look at the differences between the numbers. Which number comes next?',
         opts=['52', '49', '55', '50'],
         hint='The differences are 3, 6, 9, 12, …',
         sol='The differences go up by 3 each time: 3, 6, 9, 12. The next difference is 15: 37 + 15 = 52.'),
    dict(ch='10', scen='1 January 2027 Friday · day of 5 March 2027',
         stem='In 2027, 1 January is a Friday. 2027 is not a leap year. On which day of the week is Ayaan\'s birthday, 5 March 2027?',
         opts=['Friday', 'Thursday', 'Saturday', 'Monday'],
         hint='Is 2027 a leap year? Count the days after 1 January.',
         sol='2027 is not a leap year. 5 March is 30 (rest of January) + 28 (February) + 5 = 63 days after 1 January. 63 = 9 weeks exactly, so it is also a Friday.'),
    dict(ch='10', scen='sum of page numbers on 5 torn-out sheets',
         stem='Each sheet of a book has an odd page number on one side and the next even number on the other, like 7 and 8. Mohan tears out 5 sheets and adds all their page numbers. Which could be his total?',
         opts=['203', '210', '300', '196'],
         hint='Is the sum of the two page numbers on one sheet odd or even?',
         sol='Each sheet\'s two numbers add to odd + even = odd. Five odd totals add up to an odd number. Only 203 is odd. (Sheets with pages 15–16, 17–18, 19–20, 23–24 and 25–26 give 203.)'),
    dict(ch='10', scen='4 friends in a row with two who must sit together',
         stem='Four friends, including Ravi and Sita, sit in a row of 4 chairs. Ravi and Sita must sit next to each other. In how many different ways can they sit?',
         opts=['12', '24', '6', '8'],
         hint='Treat Ravi and Sita as one block first.',
         sol='Ravi and Sita as one block plus the other 2 friends make 3 items: 3 × 2 × 1 = 6 orders. Inside the block, Ravi and Sita can swap: 6 × 2 = 12 ways.'),

    # ---------------- Section II · Star Questions
    dict(ch='1+10', scen='fifth common multiple of 4 and 6 above 50',
         stem='Numbers that are multiples of both 4 and 6 are listed in order, starting from the first one greater than 50. What is the 5th number in the list?',
         opts=['108', '96', '120', '84'],
         hint='Common multiples of 4 and 6 are multiples of 12, not of 24.',
         sol='Common multiples of 4 and 6 are multiples of 12. Those above 50: 60, 72, 84, 96, 108. The 5th is 108.'),
    dict(ch='3+10', scen='decimal series doubling and adding 0.1',
         fig=cards(['0.1', '0.3', '0.7', '1.5', '3.1', '?'], size=36),
         stem='Ronak builds this decimal series using the same two steps each time. Which number comes next?',
         opts=['6.3', '6.2', '4.7', '6.1'],
         hint='Double the number and then add something.',
         sol='0.1 × 2 + 0.1 = 0.3, 0.3 × 2 + 0.1 = 0.7, 0.7 × 2 + 0.1 = 1.5, 1.5 × 2 + 0.1 = 3.1. Next: 3.1 × 2 + 0.1 = 6.3.'),
    dict(ch='6+10', scen='1 m tiles round square ponds · pond 10 by 10',
         stem='One-metre square tiles are laid in a single ring around square ponds. A 1 m by 1 m pond needs 8 tiles, a 2 m by 2 m pond needs 12 tiles and a 3 m by 3 m pond needs 16 tiles. How many tiles does a 10 m by 10 m pond need?',
         opts=['44', '40', '48', '100'],
         hint='Each bigger pond needs 4 more tiles.',
         sol='The tiles go up by 4 each time: 4 × (side) + 4 (one row of side tiles on each side, plus 4 corner tiles). For side 10: 40 + 4 = 44 tiles.'),
    dict(ch='1+9', scen='84 apples and 120 oranges in largest equal bags at ₹4.50 per bag',
         stem='A fruit seller packs 84 apples and 120 oranges into bags. Each bag has only one kind of fruit, all bags hold the same number, and each bag holds as many as possible. Bags cost ₹4.50 each. How much do the bags cost?',
         opts=['₹76.50', '₹54.00', '₹90.00', '₹72.50'],
         hint='The number in each bag is the HCF of 84 and 120.',
         sol='HCF of 84 and 120 is 12. Bags: 84 ÷ 12 = 7 and 120 ÷ 12 = 10, so 17 bags. Cost: 17 × 4.50 = ₹76.50.'),
    dict(ch='3+9', scen='2.4 km in 12 minutes · time for a 15 km race',
         stem='Malti runs 2.4 km in 12 minutes. At the same speed, how long will she take to run a 15 km race?',
         opts=['1 h 15 min', '1 h 12 min', '1 h 30 min', '1 h 2 min'],
         hint='Find how long she takes for 1 km.',
         sol='12 minutes for 2.4 km means 5 minutes per km (2.4 × 5 = 12). 15 km takes 15 × 5 = 75 minutes = 1 h 15 min.'),
]
