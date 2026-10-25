# AMO Level-2 · Class 6 · Practice Paper 3


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


def four_angles():
    import math
    prims = []
    cx, cy, r = 100, 90, 70
    for a in (0, 75, 135, 255):
        t = math.radians(a)
        prims.append(('line', cx, cy, cx + r * math.cos(t), cy - r * math.sin(t)))
    for mid, lab in ((37, '75°'), (105, 'x'), (195, '2x'), (307, '105°')):
        t = math.radians(mid)
        prims.append(('text', cx + 38 * math.cos(t), cy - 38 * math.sin(t), lab, 12))
    prims.append(('dot', cx, cy, 3))
    return prims


QUESTIONS = [
    # ---------------- Part 1 · Number System
    dict(ch='1', scen='zeros in 7 crore 7 lakh 7 thousand 7',
         stem='Ishani writes "seven crore seven lakh seven thousand seven" in digits. How many zeros does she write?',
         opts=['4', '5', '6', '3'],
         hint='Write the number with Indian commas: crores, lakhs, thousands, ones.',
         sol='The number is 7,07,07,007. Its digits are 7 0 7 0 7 0 0 7, which has 4 zeros.'),
    dict(ch='1', scen='prime factors of 2,310 · how many and the largest',
         stem='How many different prime factors does 2,310 have, and which is the largest?',
         opts=['5 primes, largest 11', '4 primes, largest 11', '5 primes, largest 7', '6 primes, largest 13'],
         hint='Divide by 2, 3, 5, 7, … in turn.',
         sol='2,310 = 2 × 1,155 = 2 × 3 × 385 = 2 × 3 × 5 × 77 = 2 × 3 × 5 × 7 × 11. That is 5 different primes and the largest is 11.'),
    dict(ch='1', scen='rods 84 120 and 156 cm cut into equal longest pieces',
         stem='Three iron rods are 84 cm, 120 cm and 156 cm long. They are cut into pieces of equal length, as long as possible, with nothing wasted. How many pieces are there in all?',
         opts=['30', '12', '36', '25'],
         hint='The longest possible piece is the HCF of the three lengths.',
         sol='84 = 12 × 7, 120 = 12 × 10 and 156 = 12 × 13, and 7, 10, 13 share no factor, so the HCF is 12 cm. Pieces: 7 + 10 + 13 = 30.'),

    # ---------------- Part 2 · Operations
    dict(ch='2', scen='18 minus nested brackets with −3 and 12 over −4',
         stem='What is the value of 18 − [−3 − {12 ÷ (−4) + 2 × (−5)}]?',
         opts=['8', '28', '2', '−8'],
         hint='Inside the curly bracket, divide and multiply before adding.',
         sol='12 ÷ (−4) = −3 and 2 × (−5) = −10, so the curly bracket is −13. Then −3 − (−13) = 10. Finally 18 − 10 = 8.'),
    dict(ch='2', scen='−36 divided by a bracket of products of integers',
         stem='What is the value of (−36) ÷ [(−4) × 3 − (−3) × 2]?',
         opts=['6', '−6', '−2', '2'],
         hint='Work out the bracket carefully: two products, then subtract.',
         sol='(−4) × 3 = −12 and (−3) × 2 = −6. The bracket is −12 − (−6) = −6. (−36) ÷ (−6) = 6.'),
    dict(ch='2', scen='sum of ten consecutive integers starting at −6',
         stem='Kunal adds ten consecutive integers, starting from −6. What total does he get?',
         opts=['−15', '−6', '15', '−3'],
         hint='Write the ten integers and cancel the opposite pairs.',
         sol='The integers are −6, −5, −4, −3, −2, −1, 0, 1, 2, 3. The pairs −3 and 3, −2 and 2, −1 and 1 cancel. What is left is −6 − 5 − 4 = −15.'),

    # ---------------- Part 3 · Fractions, Decimals & Percentages
    dict(ch='3', scen='largest of 2/3 0.67 66% and 0.666',
         stem='Which is the largest of these: 2/3, 0.67, 66%, 0.666?',
         opts=['0.67', '2/3', '66%', '0.666'],
         hint='2/3 = 0.6666… goes on for ever.',
         sol='2/3 = 0.6666…, 66% = 0.66, and 0.666 stops after three digits. Compare: 0.670 > 0.6666… > 0.666 > 0.660. The largest is 0.67.'),
    dict(ch='3', scen='village of 8,000 up 10% then down 10%',
         stem='A village has 8,000 people. The population rises by 10% in one year and falls by 10% the next year. What is the population after two years?',
         opts=['7,920', '8,000', '8,080', '7,200'],
         hint='The fall is 10% of the new, larger number.',
         sol='After the rise: 8,000 + 800 = 8,800. After the fall: 8,800 − 880 = 7,920.'),
    dict(ch='3', scen='60% cricket 45% football 20% both · percent neither',
         stem='In a class, 60% of the students like cricket, 45% like football and 20% like both. What percentage of the class likes neither game?',
         opts=['15%', '5%', '25%', '35%'],
         hint='The 20% who like both are counted in the 60% and in the 45%.',
         sol='Students who like at least one game: 60% + 45% − 20% = 85%. Neither: 100% − 85% = 15%.'),

    # ---------------- Part 4 · Algebra
    dict(ch='4', scen='father three times plus four · sum of ages in five years',
         stem='Raju is x years old. His father\'s age is 4 years more than 3 times Raju\'s age. Write the sum of their ages 5 years from now, and find it when x = 12.',
         opts=['4x + 14; 62', '4x + 9; 57', '4x + 4; 52', '3x + 14; 50'],
         hint='Add 5 to each age before adding the two ages.',
         sol='In 5 years Raju is x + 5 and his father is 3x + 4 + 5 = 3x + 9. Sum = 4x + 14. At x = 12: 48 + 14 = 62.'),
    dict(ch='4', scen='3 times 2p minus q minus 2 times p minus 3q at p −1 q 2',
         stem='Simplify 3(2p − q) − 2(p − 3q) and find its value when p = −1 and q = 2.',
         opts=['2', '−10', '14', '−2'],
         hint='Open both brackets carefully; the second bracket is multiplied by −2.',
         sol='3(2p − q) = 6p − 3q and −2(p − 3q) = −2p + 6q. Together: 4p + 3q. At p = −1, q = 2: −4 + 6 = 2.'),

    # ---------------- Part 5 · Geometry
    dict(ch='5', scen='four angles at a point 75 x 2x and 105',
         fig=drawing(200, 180, four_angles()),
         stem='Four angles meet at a point: 75°, x, 2x and 105°, as shown. What is the largest of the four angles?',
         opts=['120°', '105°', '60°', '90°'],
         hint='Angles around a point add up to 360°.',
         sol='75° + 105° + x + 2x = 360°, so 3x = 180° and x = 60°. The angles are 75°, 60°, 120° and 105°. The largest is 120°.'),
    dict(ch='5', scen='triangle with angles in the ratio 1:2:3 · type',
         stem='In a triangle, the middle angle is twice the smallest, and the largest is three times the smallest. What type of triangle is it?',
         opts=['Right-angled', 'Acute-angled', 'Obtuse-angled', 'Equiangular'],
         hint='The three angles make 1 + 2 + 3 = 6 equal parts of 180°.',
         sol='One part = 180° ÷ 6 = 30°. The angles are 30°, 60° and 90°, so it is right-angled.'),
    dict(ch='5', scen='triangles made by diagonals from one corner of a decagon',
         stem='All the diagonals are drawn from one corner of a regular decagon (10 sides). Into how many triangles do they cut the decagon?',
         opts=['8', '10', '7', '35'],
         hint='Try it for a pentagon and a hexagon first.',
         sol='From one corner of an n-sided polygon there are n − 3 diagonals, cutting it into n − 2 triangles. For n = 10: 8 triangles. (A pentagon gives 3, a hexagon 4.)'),

    # ---------------- Part 6 · Mensuration
    dict(ch='6', scen='two 3 m paths crossing a 60 by 40 field',
         stem='A field is 60 m by 40 m. Two paths, each 3 m wide, cross through the middle, one parallel to each side. What is the total area of the paths?',
         opts=['291 m²', '300 m²', '309 m²', '282 m²'],
         hint='The square where the paths cross is counted twice if you just add them.',
         sol='Path along the length: 60 × 3 = 180 m². Path along the width: 40 × 3 = 120 m². The crossing square, 3 × 3 = 9 m², is in both. Total 180 + 120 − 9 = 291 m².'),
    dict(ch='6', scen='surface area when a cube\'s edge is doubled',
         stem='The edge of a cube is doubled. By what number is its surface area multiplied?',
         opts=['4', '2', '8', '6'],
         hint='Try an edge of 1 cm and then 2 cm.',
         sol='Edge 1 cm: 6 × 1 = 6 cm². Edge 2 cm: 6 × 4 = 24 cm². 24 ÷ 6 = 4. Each face becomes 2 × 2 = 4 times as big. (8 is the change in volume.)'),
    dict(ch='6', scen='12 cm cube cut into 3 cm cubes · total surface area',
         stem='A wooden cube of edge 12 cm is cut into small cubes of edge 3 cm. What is the total surface area of all the small cubes?',
         opts=['3,456 cm²', '864 cm²', '1,728 cm²', '2,592 cm²'],
         hint='Count the small cubes: 4 along each edge.',
         sol='There are 4 × 4 × 4 = 64 small cubes. Each has 6 × 3 × 3 = 54 cm². Total 64 × 54 = 3,456 cm². (864 cm² is the big cube\'s surface only.)'),

    # ---------------- Part 7 · Data Handling
    dict(ch='8', scen='cars sold bar graph · days with a rise and the biggest rise',
         fig=drawing(330, 210, bars([('Mon', 25), ('Tue', 40), ('Wed', 35), ('Thu', 50), ('Fri', 30)], 60, 5, 'Cars sold')),
         stem='The bar graph shows the cars sold by a showroom. On how many days were more cars sold than on the day before, and what was the biggest rise?',
         opts=['2 days; 15 cars', '3 days; 15 cars', '2 days; 20 cars', '2 days; 25 cars'],
         hint='Compare each day with the day before it. Monday has no day before.',
         sol='Tue (40) > Mon (25): rise 15. Wed (35) < Tue. Thu (50) > Wed (35): rise 15. Fri (30) < Thu. So 2 days, and the biggest rise is 15 cars.'),
    dict(ch='8', scen='frequency table of children per family · total children',
         fig=table(['Children in family', '0', '1', '2', '3', '4'], [['Families', '2', '9', '12', '5', '2']], widths=[140, 45, 45, 45, 45, 45]),
         stem='The table shows how many children there are in each of 30 families. How many children are there altogether?',
         opts=['56', '30', '10', '60'],
         hint='Multiply each number of children by the number of families.',
         sol='0 × 2 + 1 × 9 + 2 × 12 + 3 × 5 + 4 × 2 = 0 + 9 + 24 + 15 + 8 = 56.'),

    # ---------------- Part 8 · Applied Mathematics
    dict(ch='9', scen='trains 450 km apart at 70 and 80 km/h from 9 AM',
         stem='Two trains are 450 km apart. At 9 AM they start towards each other at 70 km/h and 80 km/h. At what time do they meet?',
         opts=['12:00 noon', '11:00 AM', '1:00 PM', '3:00 PM'],
         hint='Together they close the gap by 70 + 80 km every hour.',
         sol='The gap closes by 150 km each hour. 450 ÷ 150 = 3 hours. 9 AM + 3 hours = 12 noon.'),
    dict(ch='9', scen='mother to daughter 7:2 with a 30-year difference',
         stem='The ages of a mother and her daughter are in the ratio 7 : 2. The mother is 30 years older. How old is the mother?',
         opts=['42', '35', '12', '49'],
         hint='The difference of 30 years is 7 − 2 = 5 parts.',
         sol='5 parts = 30 years, so 1 part = 6 years. Mother = 7 × 6 = 42 years (daughter 12).'),
    dict(ch='9', scen='car runs 270 km on 18 L · petrol for 405 km',
         stem='A car runs 270 km on 18 litres of petrol. How much petrol does it need for 405 km?',
         opts=['27 L', '24 L', '30 L', '21 L'],
         hint='Find the distance for 1 litre first.',
         sol='1 litre gives 270 ÷ 18 = 15 km. 405 ÷ 15 = 27 litres.'),

    # ---------------- Part 9 · Mathematical Reasoning
    dict(ch='10', scen='12-hour clock showing 8 · 1,000 hours later',
         stem='A 12-hour clock shows 8 o\'clock. What will it show exactly 1,000 hours later?',
         opts=['12 o\'clock', '8 o\'clock', '4 o\'clock', '10 o\'clock'],
         hint='Every 12 hours the clock shows the same time again.',
         sol='1,000 = 12 × 83 + 4, so the clock moves on by 4 hours: 8 + 4 = 12 o\'clock.'),
    dict(ch='10', scen='frog jumping 3 or 5 cm · possible distance after 10 jumps',
         stem='A frog jumps forward 3 cm or 5 cm at each jump. Which of these distances can it cover in exactly 10 jumps?',
         opts=['40 cm', '37 cm', '45 cm', '53 cm'],
         hint='Each jump is an odd number. What about the total of 10 odd numbers?',
         sol='Ten odd jumps make an even total, between 30 cm (all 3s) and 50 cm (all 5s). 37 and 45 are odd and 53 is too big. 40 cm works: five 3s and five 5s.'),
    dict(ch='10', scen='lily patch doubling daily covers pond on day 20',
         stem='A patch of water lilies doubles its area every day. It covers the whole pond on day 20. On which day did it cover half the pond?',
         opts=['Day 19', 'Day 10', 'Day 18', 'Day 15'],
         hint='Work backwards one day from day 20.',
         sol='The area doubles each day, so one day before the pond was full it was half full: day 19. (Day 10 wrongly halves the number of days.)'),

    # ---------------- Mixed Problems
    dict(ch='4+10', scen='sum of the first 25 odd numbers',
         fig=cards(['1', '1 + 3', '1 + 3 + 5', '…'], size=34, width=110),
         stem='1 = 1, 1 + 3 = 4, 1 + 3 + 5 = 9. Following the pattern, what is the sum of the first 25 odd numbers?',
         opts=['625', '600', '650', '49'],
         hint='The sum of the first n odd numbers is n × n.',
         sol='The sums 1, 4, 9 are 1 × 1, 2 × 2, 3 × 3. So the first n odd numbers add to n × n. For n = 25: 25 × 25 = 625. (49 is the 25th odd number.)'),
    dict(ch='1+10', scen='1 minus 2 plus 3 minus 4 up to minus 100',
         stem='What is the value of 1 − 2 + 3 − 4 + 5 − 6 + … + 99 − 100?',
         opts=['−50', '50', '−100', '0'],
         hint='Group the terms in pairs.',
         sol='(1 − 2) + (3 − 4) + … + (99 − 100) has 50 pairs, each equal to −1. Total −50.'),
    dict(ch='3+9', scen='pulp added to make 30% juice into 50% juice',
         stem='Kajal has 10 litres of juice that is 30% mango pulp. How many litres of pure pulp must she add to make the juice 50% pulp?',
         opts=['4 L', '2 L', '5 L', '20 L'],
         hint='The water part does not change.',
         sol='The juice has 3 L pulp and 7 L water. For 50% pulp, the pulp must equal the water: 7 L. She must add 7 − 3 = 4 L of pulp. Check: 7 out of 14 is 50%.'),
    dict(ch='5+6', scen='square with the same perimeter as an equilateral triangle of side 12',
         stem='A square has the same perimeter as an equilateral triangle of side 12 cm. What is the area of the square?',
         opts=['81 cm²', '144 cm²', '36 cm²', '72 cm²'],
         hint='All three sides of an equilateral triangle are equal.',
         sol='Triangle perimeter = 3 × 12 = 36 cm. Square side = 36 ÷ 4 = 9 cm. Area = 9 × 9 = 81 cm².'),
    dict(ch='4+9', scen='pens at ₹15 and pencils at ₹5 · 20 items for ₹200',
         stem='Om buys 20 items, some pens at ₹15 each and the rest pencils at ₹5 each. He pays ₹200. How many pens does he buy?',
         opts=['10', '12', '8', '5'],
         hint='If all 20 were pencils, the cost would be ₹100.',
         sol='20 pencils would cost ₹100. Changing one pencil into a pen adds ₹10. He needs ₹100 more, so 100 ÷ 10 = 10 pens. Check: 10 × 15 + 10 × 5 = 150 + 50 = ₹200.'),
]
