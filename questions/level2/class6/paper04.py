# AMO Level-2 · Class 6 · Practice Paper 4


def bars(data, top, step, unit='', bw=34, gap=22, h=150):
    """Bar graph: data = [(label, value)], y axis from 0 to top with gridlines every step."""
    x0, y0 = 40, 10
    w = len(data) * (bw + gap) + gap
    prims = []
    for v in range(0, top + 1, step):
        y = y0 + h - v * h / top
        prims += [('line', x0, y, x0 + w, y, True, (170, 170, 170), 0.8), ('text', x0 - 16, y, str(v), 10)]
    for i, (lab, v) in enumerate(data):
        x = x0 + gap + i * (bw + gap)
        prims += [('rect', x, y0 + h - v * h / top, bw, v * h / top, 'blue'), ('text', x + bw / 2, y0 + h + 14, lab, 10)]
    prims += [('line', x0, y0, x0, y0 + h), ('line', x0, y0 + h, x0 + w, y0 + h)]
    if unit:
        prims.append(('text', x0 + w / 2, y0 + h + 32, unit, 10))
    return prims


def house_shape():
    import math
    h = 10 * math.sqrt(3) / 2
    s = 9
    return [('poly', [(10, 10 + h * s), (10 + 5 * s, 10), (10 + 10 * s, 10 + h * s), (10 + 10 * s, 10 + h * s + 10 * s), (10, 10 + h * s + 10 * s)], 'yellow'),
            ('line', 10, 10 + h * s, 10 + 10 * s, 10 + h * s, True),
            ('text', 10 + 5 * s, 22 + h * s + 10 * s, '10 cm', 11), ('text', -14, 10 + h * s + 5 * s, '10 cm', 11)]


QUESTIONS = [
    # ---------------- Part 1 · Number System
    dict(ch='1', scen='largest minus smallest 8-digit numbers with different digits',
         stem='What is the difference between the largest and the smallest 8-digit numbers that have all their digits different?',
         opts=['8,85,30,865', '8,86,30,865', '8,75,30,865', '8,85,31,865'],
         hint='The smallest cannot start with 0: it is 1,02,34,567.',
         sol='Largest: 9,87,65,432. Smallest: 1,02,34,567. Difference: 9,87,65,432 − 1,02,34,567 = 8,85,30,865.'),
    dict(ch='1', scen='odd factors of 2 × 2 × 3 × 5 × 7',
         stem='A number is 2 × 2 × 3 × 5 × 7. How many of its factors are odd?',
         opts=['8', '4', '24', '12'],
         hint='An odd factor cannot use any 2.',
         sol='Odd factors are made only from 3, 5 and 7, each used or not: 1, 3, 5, 7, 15, 21, 35, 105. That is 8.'),
    dict(ch='1', scen='point one quarter of the way from −14 to 22',
         stem='On a number line, A is at −14 and B is at 22. Point C is one quarter of the way from A to B. Which integer is at C?',
         opts=['−5', '−9', '9', '4'],
         hint='Find the distance from A to B first.',
         sol='AB = 22 − (−14) = 36. A quarter of 36 is 9. C = −14 + 9 = −5.'),

    # ---------------- Part 2 · Operations
    dict(ch='2', scen='curly bracket 6 plus 18 over 3 times 2 times square bracket 4 minus −2',
         stem='What is the value of {6 + 18 ÷ (3 × 2)} × [4 − (−2)]?',
         opts=['54', '90', '48', '−54'],
         hint='Inside the curly bracket, the round bracket comes first.',
         sol='(3 × 2) = 6, so 18 ÷ 6 = 3 and the curly bracket is 6 + 3 = 9. The square bracket is 4 + 2 = 6. 9 × 6 = 54. (90 comes from working 18 ÷ 3 × 2 as 12.)'),
    dict(ch='2', scen='how many of four integer statements are always true',
         stem='How many of these are true for ALL integers a, b, c (with no division by 0)? (i) a + b = b + a. (ii) a − b = b − a. (iii) a × (b + c) = a × b + a × c. (iv) (a ÷ b) ÷ c = a ÷ (b ÷ c).',
         opts=['2', '3', '1', '4'],
         hint='Test (ii) and (iv) with small numbers like 8, 4 and 2.',
         sol='(i) is the commutative property and (iii) is the distributive property: both always true. (ii) fails: 8 − 4 ≠ 4 − 8. (iv) fails: (8 ÷ 4) ÷ 2 = 1 but 8 ÷ (4 ÷ 2) = 4. So 2.'),
    dict(ch='2', scen='three integers with sum 2 and product −60 including −5',
         stem='Three integers add up to 2 and multiply to give −60. One of them is −5. What is the largest of the three?',
         opts=['4', '3', '12', '7'],
         hint='The other two add up to 7 and multiply to 12.',
         sol='The other two add to 2 − (−5) = 7 and multiply to −60 ÷ (−5) = 12. They are 3 and 4. The largest is 4.'),

    # ---------------- Part 3 · Fractions, Decimals & Percentages
    dict(ch='3', scen='0.375 as a fraction in lowest terms and as a percent',
         stem='Which pair shows 0.375 correctly as a fraction in lowest terms and as a percentage?',
         opts=['3/8 and 37.5%', '3/8 and 3.75%', '375/1000 and 375%', '3/5 and 37.5%'],
         hint='0.375 = 375/1000. Divide top and bottom by 125.',
         sol='375/1000 = 3/8 (dividing by 125). As a percentage: 0.375 × 100 = 37.5%.'),
    dict(ch='3', scen='salary with 40% rent and 25% of the rest on food · savings ₹13,500',
         stem='Aman spends 40% of his salary on rent and 25% of what is left on food. He saves the remaining ₹13,500. What is his salary?',
         opts=['₹30,000', '₹27,000', '₹40,500', '₹22,500'],
         hint='The 25% is of the remaining 60%, not of the whole salary.',
         sol='After rent, 60% is left. Food takes 25% of that, which is 15% of the salary. Savings = 60% − 15% = 45% of the salary = ₹13,500. 1% = ₹300, so the salary is ₹30,000.'),
    dict(ch='3', scen='18 minutes as a percentage of 2 hours',
         stem='What percentage of 2 hours is 18 minutes?',
         opts=['15%', '9%', '18%', '30%'],
         hint='Change 2 hours into minutes first.',
         sol='2 hours = 120 minutes. 18/120 = 3/20 = 15/100 = 15%. (9% wrongly uses 200 minutes.)'),

    # ---------------- Part 4 · Algebra
    dict(ch='4', scen='largest of four expressions at x equals 3',
         stem='When x = 3, which of these expressions has the largest value?',
         opts=['20 − 2x', '4x', 'x × x + 1', '5x − 4'],
         hint='Substitute x = 3 into each one.',
         sol='20 − 2x = 14. 4x = 12. x × x + 1 = 10. 5x − 4 = 11. The largest is 20 − 2x.'),
    dict(ch='4', scen='matchstick hexagons in a row · sticks for 12 hexagons',
         stem='Hexagons are made in a row with matchsticks, each pair sharing one side. 1 hexagon uses 6 sticks and 2 hexagons use 11. How many sticks do 12 hexagons use?',
         opts=['61', '72', '60', '66'],
         hint='Each new hexagon adds 5 sticks.',
         sol='n hexagons use 5n + 1 sticks (6, 11, 16, …). For n = 12: 60 + 1 = 61. (72 forgets the shared sides.)'),

    # ---------------- Part 5 · Geometry
    dict(ch='5', scen='supplementary angles with one 30 more than half the other',
         stem='Two angles together make a straight angle. One of them is 30° more than half of the other. What is the larger angle?',
         opts=['100°', '80°', '120°', '110°'],
         hint='Try the options: check that the two angles add up to 180°.',
         sol='If the larger is 100°, the other is 180° − 100° = 80°, and 80° = half of 100° + 30° = 50° + 30°. So the larger angle is 100°.'),
    dict(ch='5', scen='how many isosceles triangles have a 70° angle',
         stem='An isosceles triangle has one angle of 70°. How many different sets of angles can the triangle have?',
         opts=['2', '1', '3', '0'],
         hint='The 70° angle could be one of the two equal angles, or the odd one.',
         sol='If 70° is one of the equal angles: 70°, 70°, 40°. If 70° is the odd angle: the other two share 110°, giving 55°, 55°, 70°. That is 2 sets.'),
    dict(ch='5', scen='polygon with 14 diagonals',
         stem='A polygon has 14 diagonals. How many sides does it have?',
         opts=['7', '8', '14', '6'],
         hint='An n-sided polygon has n × (n − 3) ÷ 2 diagonals. Try the options.',
         sol='n = 7: 7 × 4 ÷ 2 = 14. ✓ (n = 8 gives 20 and n = 6 gives 9.)'),

    # ---------------- Part 6 · Mensuration
    dict(ch='6', scen='painting walls and ceiling of a 6 by 4 by 3 room with door and window',
         stem='A room is 6 m long, 4 m wide and 3 m high. Its four walls and ceiling are painted, but not a window of 2 m² or a door of 3 m². What area is painted?',
         opts=['79 m²', '84 m²', '103 m²', '55 m²'],
         hint='The four walls together are a long strip of length 2 × (6 + 4).',
         sol='Walls: 2 × (6 + 4) × 3 = 60 m². Ceiling: 6 × 4 = 24 m². Total 84 m². Minus window and door: 84 − 5 = 79 m².'),
    dict(ch='6', scen='rectangle with length up 20% and breadth down 20%',
         stem='The length of a rectangle is increased by 20% and its breadth is decreased by 20%. What happens to its area?',
         opts=['It decreases by 4%', 'It stays the same', 'It increases by 4%', 'It decreases by 20%'],
         hint='Try a 10 cm by 10 cm square.',
         sol='A 10 × 10 square (100 cm²) becomes 12 × 8 = 96 cm². The area falls by 4 cm² out of 100, which is 4%.'),
    dict(ch='6', scen='cuboid of volume 480 with length 12 and breadth 8 · surface area',
         stem='A cuboid has volume 480 cm³, length 12 cm and breadth 8 cm. What is its total surface area?',
         opts=['392 cm²', '480 cm²', '196 cm²', '412 cm²'],
         hint='Find the height first.',
         sol='Height = 480 ÷ (12 × 8) = 5 cm. Surface area = 2 × (12 × 8 + 12 × 5 + 8 × 5) = 2 × (96 + 60 + 40) = 392 cm².'),

    # ---------------- Part 7 · Data Handling
    dict(ch='8', scen='favourite subject bar graph · percent for the top two',
         fig=drawing(330, 210, bars([('Maths', 14), ('Science', 11), ('English', 8), ('Hindi', 10), ('Art', 7)], 16, 2, 'Favourite subject (students)')),
         stem='The bar graph shows the favourite subjects of a group of students. What percentage of the students chose one of the two most popular subjects?',
         opts=['50%', '25%', '28%', '40%'],
         hint='Find the total number of students first.',
         sol='Total: 14 + 11 + 8 + 10 + 7 = 50. Top two: Maths 14 + Science 11 = 25. 25 out of 50 = 50%.'),
    dict(ch='8', scen='goals per match table · matches with at least 2 goals',
         fig=table(['Goals in a match', '0', '1', '2', '3', '4'], [['Matches', '3', '5', '6', '4', '2']], widths=[140, 45, 45, 45, 45, 45]),
         stem='The table shows the goals scored in each match of a school football league. In how many matches were at least 2 goals scored, and how many goals were scored in those matches?',
         opts=['12 matches, 32 goals', '12 matches, 20 goals', '6 matches, 12 goals', '14 matches, 32 goals'],
         hint='"At least 2" means 2, 3 or 4 goals.',
         sol='Matches: 6 + 4 + 2 = 12. Goals in them: 2 × 6 + 3 × 4 + 4 × 2 = 12 + 12 + 8 = 32.'),

    # ---------------- Part 8 · Applied Mathematics
    dict(ch='9', scen='bus 60 km at 40 km/h then 60 km at 60 km/h · average speed',
         stem='A bus travels 60 km at 40 km/h and then another 60 km at 60 km/h. What is its average speed for the whole trip?',
         opts=['48 km/h', '50 km/h', '45 km/h', '52 km/h'],
         hint='Average speed = total distance ÷ total time.',
         sol='Time: 60 ÷ 40 = 1.5 h and 60 ÷ 60 = 1 h, so 2.5 h in all. Average speed = 120 ÷ 2.5 = 48 km/h. (50 km/h wrongly averages the two speeds.)'),
    dict(ch='9', scen='A:B 2:3 and B:C 4:5 · A:C',
         stem='The money with Arnav, Bhavna and Chirag is in the ratios Arnav : Bhavna = 2 : 3 and Bhavna : Chirag = 4 : 5. What is Arnav : Chirag?',
         opts=['8 : 15', '2 : 5', '8 : 12', '10 : 12'],
         hint='Make Bhavna\'s share the same number in both ratios.',
         sol='Arnav : Bhavna = 8 : 12 and Bhavna : Chirag = 12 : 15. So Arnav : Chirag = 8 : 15.'),
    dict(ch='9', scen='15 men dig a trench in 12 days · extra men for 9 days',
         stem='15 men can dig a trench in 12 days. How many MORE men are needed to dig it in 9 days?',
         opts=['5', '20', '3', '8'],
         hint='Find the number of man-days of work first.',
         sol='Work = 15 × 12 = 180 man-days. In 9 days: 180 ÷ 9 = 20 men. Extra men: 20 − 15 = 5.'),

    # ---------------- Part 9 · Mathematical Reasoning
    dict(ch='10', scen='hour strikes of a clock in a full day',
         stem='A clock strikes once at 1 o\'clock, twice at 2 o\'clock, and so on up to 12 times at 12 o\'clock. How many times does it strike in a full day of 24 hours?',
         opts=['156', '78', '300', '144'],
         hint='The clock goes round twice in a day.',
         sol='One round: 1 + 2 + … + 12 = 78 strikes. Two rounds in 24 hours: 156.'),
    dict(ch='10', scen='chessboard with opposite corners removed covered by dominoes',
         stem='Two opposite corner squares are cut from an 8 × 8 chessboard, leaving 62 squares. Can 31 dominoes, each covering two neighbouring squares, cover it exactly?',
         opts=['No, because the two removed squares are the same colour', 'Yes, in exactly one way', 'No, because 62 is not a multiple of 4', 'Yes, in many ways'],
         hint='Every domino covers one black and one white square.',
         sol='Opposite corners have the same colour, so 30 squares of one colour and 32 of the other are left. 31 dominoes would cover 31 of each colour. So it is impossible.'),
    dict(ch='10', scen='mangoes taken as half plus one by three friends · none left',
         stem='Ram took half the mangoes in a basket and 1 more. Shyam took half of what was left and 1 more. Hari took half of the rest and 1 more. No mangoes were left. How many were there at first?',
         opts=['14', '12', '16', '10'],
         hint='Work backwards. Before Hari, what number has half + 1 equal to the whole?',
         sol='Before Hari there were 2 (he took 1 + 1). Before Shyam: half of it and 1 more left 2, so half was 3 and there were 6. Before Ram: half of it and 1 more left 6, so half was 7 and there were 14.'),

    # ---------------- Mixed Problems
    dict(ch='4+10', scen='first triangular number above 100',
         fig=cards([1, 3, 6, 10, 15, '…'], size=40),
         stem='The nth number in this pattern is n × (n + 1) ÷ 2. What is the first number in the pattern that is greater than 100?',
         opts=['105', '91', '120', '100'],
         hint='Try n = 13 and n = 14.',
         sol='n = 13: 13 × 14 ÷ 2 = 91. n = 14: 14 × 15 ÷ 2 = 105. So 105 is the first above 100. (100 is not in the pattern.)'),
    dict(ch='1+10', scen='integers from −50 to 50 that are multiples of 3 or 5',
         stem='How many integers from −50 to 50 (including both) are multiples of 3 or of 5?',
         opts=['47', '54', '40', '46'],
         hint='Count multiples of 3, of 5, and take away multiples of 15 once. Do not forget 0.',
         sol='Multiples of 3: −48 to 48, which is 16 + 1 + 16 = 33. Multiples of 5: −50 to 50, which is 10 + 1 + 10 = 21. Multiples of 15: −45 to 45, which is 3 + 1 + 3 = 7. Total 33 + 21 − 7 = 47.'),
    dict(ch='3+9', scen='240 km trip with speed raised 20% for the second half',
         stem='Kiran drives 240 km. She drives the first half at 60 km/h and then increases her speed by 20% for the second half. How long does the whole trip take?',
         opts=['3 h 40 min', '4 h', '3 h 20 min', '3 h 36 min'],
         hint='20% more than 60 km/h is 72 km/h.',
         sol='First 120 km at 60 km/h: 2 h. Second 120 km at 72 km/h: 120 ÷ 72 = 1 2/3 h = 1 h 40 min. Total 3 h 40 min.'),
    dict(ch='5+6', scen='house shape from equilateral triangle on a square · perimeter and largest angle',
         fig=drawing(110, 190, house_shape()),
         stem='An equilateral triangle of side 10 cm sits exactly on top of a square of side 10 cm to make a house shape. What is the perimeter of the house shape, and the size of its largest angle?',
         opts=['50 cm; 150°', '60 cm; 150°', '50 cm; 120°', '70 cm; 90°'],
         hint='The shared side is inside the shape, not on its edge.',
         sol='The outline has 5 sides of 10 cm: 50 cm. Where the roof meets a wall, the square\'s 90° and the triangle\'s 60° join: 150°. The other angles are 60° and 90°, so the largest is 150°.'),
    dict(ch='4+9', scen='fare ₹x per km for 10 km then ₹x minus 4 · 25 km costs ₹315',
         stem='A taxi charges ₹x per km for the first 10 km and ₹(x − 4) per km after that. A 25 km ride costs ₹315. What is x?',
         opts=['15', '12', '18', '13'],
         hint='Write the fare: 10x + 15(x − 4). Then try the options.',
         sol='Fare = 10x + 15(x − 4) = 25x − 60. 25x − 60 = 315 gives 25x = 375, so x = 15. Check: 10 × 15 + 15 × 11 = 150 + 165 = 315.'),
]
