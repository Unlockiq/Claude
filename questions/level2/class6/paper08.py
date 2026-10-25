# AMO Level-2 · Class 6 · Practice Paper 8


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


QUESTIONS = [
    # ---------------- Part 1 · Number System
    dict(ch='1', scen='lakhs in smallest 10-digit minus smallest 8-digit number',
         stem='The smallest 8-digit number is taken away from the smallest 10-digit number. How many lakhs is the answer?',
         opts=['9,900', '990', '99,000', '9,000'],
         hint='Write both numbers with Indian commas.',
         sol='Smallest 10-digit: 1,00,00,00,000 (100 crore). Smallest 8-digit: 1,00,00,000 (1 crore). The difference is 99 crore = 99,00,00,000. One crore is 100 lakh, so 99 crore = 9,900 lakh.'),
    dict(ch='1', scen='which number is not a factor of 2 × 3 × 3 × 5 × 11',
         stem='A number is 2 × 3 × 3 × 5 × 11. Which of these is NOT a factor of it?',
         opts=['44', '30', '45', '66'],
         hint='Write each option as a product of primes.',
         sol='30 = 2 × 3 × 5, 45 = 3 × 3 × 5 and 66 = 2 × 3 × 11 all use primes that are there. 44 = 2 × 2 × 11 needs two 2s, but the number has only one. So 44 is not a factor.'),
    dict(ch='1', scen='largest square tiles for a 4.8 m by 3.6 m floor',
         stem='A floor 4.8 m by 3.6 m is to be covered with the largest possible square tiles, without cutting any. How many tiles are needed?',
         opts=['12', '48', '24', '6'],
         hint='Work in centimetres and find the HCF of 480 and 360.',
         sol='HCF of 480 and 360 is 120, so each tile is 120 cm. Tiles: (480 ÷ 120) × (360 ÷ 120) = 4 × 3 = 12.'),

    # ---------------- Part 2 · Operations
    dict(ch='2', scen='nested minus signs around −5 minus 3 minus 2',
         stem='What is the value of −[−{−(−5) − 3} − 2]?',
         opts=['4', '−4', '0', '10'],
         hint='Start inside: −(−5) = 5.',
         sol='−(−5) = 5. {5 − 3} = 2, so −{…} = −2. [−2 − 2] = −4. −[−4] = 4.'),
    dict(ch='2', scen='three integers summing to −10 with largest 7 and middle −3 · product',
         stem='Three integers add up to −10. The largest is 7 and the middle one is −3. What is the product of all three?',
         opts=['294', '−294', '−210', '210'],
         hint='Find the smallest integer first.',
         sol='Smallest = −10 − 7 − (−3) = −14. Product = 7 × (−3) × (−14) = 7 × 42 = 294 (two negatives make a positive).'),
    dict(ch='2', scen='125 times −8 times 17 times −5 times 2',
         stem='Use number properties to find 125 × (−8) × 17 × (−5) × 2.',
         opts=['1,70,000', '−1,70,000', '17,000', '85,000'],
         hint='Group 125 with 8, and 5 with 2.',
         sol='There are two negative numbers, so the answer is positive. (125 × 8) × (5 × 2) × 17 = 1,000 × 10 × 17 = 1,70,000.'),

    # ---------------- Part 3 · Fractions, Decimals & Percentages
    dict(ch='3', scen='smallest of 1/40 0.03 2.4% and 0.0245',
         stem='Which is the smallest of these: 1/40, 0.03, 2.4%, 0.0245?',
         opts=['2.4%', '0.0245', '1/40', '0.03'],
         hint='Write each as a decimal with four decimal places.',
         sol='1/40 = 0.0250, 0.03 = 0.0300, 2.4% = 0.0240 and 0.0245. The smallest is 0.0240, which is 2.4%.'),
    dict(ch='3', scen='rent ₹8,000 rising 10% then 5% of the new rent',
         stem='Rohit\'s rent is ₹8,000 a month. After one year it goes up by 10%. A year later it goes up by 5% of the new rent. What is the monthly rent then?',
         opts=['₹9,240', '₹9,200', '₹9,600', '₹9,680'],
         hint='The second rise is 5% of the new rent, not of ₹8,000.',
         sol='After the first rise: 8,000 + 800 = ₹8,800. The second rise is 5% of 8,800 = ₹440, giving ₹9,240. (₹9,200 takes 5% of ₹8,000 instead.)'),
    dict(ch='3', scen='40% girls with 3/4 of girls and 1/2 of boys passing',
         stem='In a class, 40% of the students are girls. Three quarters of the girls and half of the boys passed a test. What percentage of the class passed?',
         opts=['60%', '62.5%', '50%', '65%'],
         hint='Imagine a class of 100 students.',
         sol='Out of 100: 40 girls, of whom 30 passed; 60 boys, of whom 30 passed. 60 passed out of 100 = 60%.'),

    # ---------------- Part 4 · Algebra
    dict(ch='4', scen='p equals 2q with q −3 · pq minus p plus q',
         stem='If p = 2q and q = −3, what is the value of p × q − (p + q)?',
         opts=['27', '9', '−27', '15'],
         hint='Find p first.',
         sol='p = 2 × (−3) = −6. p × q = (−6) × (−3) = 18. p + q = −9. 18 − (−9) = 27.'),
    dict(ch='4', scen='bill of 60n plus 90 shared equally at ₹75 each',
         stem='A group of n friends shares a restaurant bill of ₹(60n + 90) equally. Each friend pays ₹75. How many friends are there?',
         opts=['6', '5', '9', '8'],
         hint='Compare what each friend pays with the ₹60 per person in the bill.',
         sol='The bill is ₹60 for each friend plus ₹90 extra. Each friend pays ₹75, which is ₹15 more than ₹60, and these extra ₹15s cover the ₹90: 90 ÷ 15 = 6 friends. Check: 60 × 6 + 90 = 450 = 6 × 75.'),

    # ---------------- Part 5 · Geometry
    dict(ch='5', scen='reflex angle four times the other angle at a point',
         stem='Two angles together make a complete turn. The reflex angle is 4 times the other angle. What is the reflex angle?',
         opts=['288°', '270°', '300°', '252°'],
         hint='A complete turn is 360°.',
         sol='The two angles make 1 + 4 = 5 parts of 360°, so 1 part is 72°. The reflex angle is 4 × 72° = 288°.'),
    dict(ch='5', scen='isosceles triangle with base angles twice the top angle',
         stem='In triangle ABC, AB = AC and angle B is twice angle A. What is angle A?',
         opts=['36°', '72°', '45°', '60°'],
         hint='Angles B and C are equal.',
         sol='Angle C = angle B = 2 × angle A. So A + 2A + 2A = 5A = 180°, and A = 36°.'),
    dict(ch='5', scen='lines of symmetry of five shapes including rectangle and rhombus',
         stem='Rani adds up the lines of symmetry of an equilateral triangle, a square, a rectangle that is not a square, a regular hexagon and a rhombus that is not a square. What total does she get?',
         opts=['17', '21', '15', '19'],
         hint='A rectangle and a rhombus each have fewer lines than a square. Do not count a rectangle\'s diagonals.',
         sol='Equilateral triangle 3, square 4, rectangle 2 (the two middle lines), regular hexagon 6, rhombus 2 (its two diagonals). Total 3 + 4 + 2 + 6 + 2 = 17. (21 gives the rectangle and the rhombus 4 each.)'),

    # ---------------- Part 6 · Mensuration
    dict(ch='6', scen='1 m path around a 20 by 12 lawn paved at ₹50 per m²',
         stem='A rectangular lawn is 20 m by 12 m. A path 1 m wide runs all round the outside. Paving costs ₹50 per m². What does paving the path cost?',
         opts=['₹3,400', '₹3,200', '₹1,600', '₹3,600'],
         hint='The outer rectangle is 22 m by 14 m.',
         sol='Path area = 22 × 14 − 20 × 12 = 308 − 240 = 68 m². Cost = 68 × 50 = ₹3,400.'),
    dict(ch='6', scen='10 by 8 by 6 cuboid cut into 2 cm cubes · total surface area',
         stem='A cuboid 10 cm × 8 cm × 6 cm is cut into cubes of edge 2 cm. What is the total surface area of all the cubes?',
         opts=['1,440 cm²', '376 cm²', '480 cm²', '2,880 cm²'],
         hint='Count the cubes first: how many fit along each edge?',
         sol='Cubes: 5 × 4 × 3 = 60. Each has 6 × 2 × 2 = 24 cm². Total 60 × 24 = 1,440 cm². (376 cm² is the cuboid\'s own surface.)'),
    dict(ch='6', scen='swimming pool 25 by 10 by 1.5 m in litres',
         stem='A swimming pool is 25 m long and 10 m wide and is filled to a depth of 1.5 m. How many litres of water does it hold? (1 m³ = 1,000 L)',
         opts=['3,75,000 L', '37,500 L', '375 L', '37,50,000 L'],
         hint='Find the volume in m³ first.',
         sol='Volume = 25 × 10 × 1.5 = 375 m³ = 375 × 1,000 = 3,75,000 L.'),

    # ---------------- Part 7 · Data Handling
    dict(ch='8', scen='marks in five subjects bar graph · overall percentage',
         fig=drawing(330, 210, bars([('Maths', 90), ('Sci', 75), ('Eng', 80), ('Hindi', 65), ('SS', 70)], 100, 10, 'Isha\'s marks (out of 100 each)')),
         stem='The bar graph shows Isha\'s marks out of 100 in five subjects. What is her overall percentage?',
         opts=['76%', '80%', '75%', '78%'],
         hint='Add all five marks and compare with 500.',
         sol='Total: 90 + 75 + 80 + 65 + 70 = 380 out of 500. 380/500 = 76/100 = 76%.'),
    dict(ch='8', scen='daily pocket money table · total and students above ₹25',
         fig=table(['Pocket money (₹)', '10', '20', '30', '40', '50'], [['Students', '3', '6', '5', '4', '2']], widths=[130, 45, 45, 45, 45, 45]),
         stem='The table shows the daily pocket money of 20 students. How much do they get in all each day, and how many get more than ₹25?',
         opts=['₹560; 11 students', '₹560; 6 students', '₹150; 11 students', '₹600; 11 students'],
         hint='Multiply each amount by its number of students.',
         sol='Total: 10 × 3 + 20 × 6 + 30 × 5 + 40 × 4 + 50 × 2 = 30 + 120 + 150 + 160 + 100 = ₹560. More than ₹25: 5 + 4 + 2 = 11 students.'),

    # ---------------- Part 8 · Applied Mathematics
    dict(ch='9', scen='standing between two cliffs · echoes after 2 s and 3 s',
         stem='Arun stands between two cliffs and shouts. He hears the first echo after 2 seconds and the second echo after 3 seconds. Sound travels at 340 m/s. How far apart are the cliffs?',
         opts=['850 m', '1,700 m', '425 m', '510 m'],
         hint='Each echo goes to a cliff and comes back.',
         sol='Nearer cliff: sound travels 340 × 2 = 680 m there and back, so it is 340 m away. Farther cliff: 340 × 3 = 1,020 m there and back, so 510 m away. The cliffs are on opposite sides: 340 + 510 = 850 m apart.'),
    dict(ch='9', scen='₹2,600 shared in the ratio 1/2 : 1/3 : 1/4',
         stem='₹2,600 is shared among Anil, Bhoomi and Chetan in the ratio 1/2 : 1/3 : 1/4. How much does Chetan get?',
         opts=['₹600', '₹650', '₹800', '₹1,200'],
         hint='Multiply each fraction by 12 to get whole numbers.',
         sol='1/2 : 1/3 : 1/4 = 6 : 4 : 3 (multiplying by 12). 13 parts = ₹2,600, so 1 part = ₹200. Chetan gets 3 × 200 = ₹600.'),
    dict(ch='9', scen='4 kg apples and 3 kg grapes for ₹760 with grapes ₹20 dearer',
         stem='4 kg of apples and 3 kg of grapes cost ₹760. One kg of grapes costs ₹20 more than one kg of apples. What is the price of one kg of apples?',
         opts=['₹100', '₹120', '₹108', '₹95'],
         hint='If the grapes were ₹20 cheaper, it would be like buying 7 kg of apples.',
         sol='Taking ₹20 off each kg of grapes takes ₹60 off: 7 kg of apples would cost 760 − 60 = ₹700. One kg of apples = ₹100 (grapes ₹120).'),

    # ---------------- Part 9 · Mathematical Reasoning
    dict(ch='10', scen='train leaving 22:45 for 7 h 50 min · arrival',
         stem='A train leaves at 22:45 (24-hour time) and the journey takes 7 hours 50 minutes. When does it arrive, in 12-hour time?',
         opts=['6:35 AM', '5:35 AM', '6:35 PM', '7:35 AM'],
         hint='22:45 is 10:45 PM.',
         sol='10:45 PM + 7 h = 5:45 AM. 5:45 AM + 50 min = 6:35 AM the next day.'),
    dict(ch='10', scen='which number can be the sum of 10 consecutive integers',
         stem='Which of these could be the sum of 10 consecutive integers?',
         opts=['145', '150', '144', '140'],
         hint='If the first integer is a, the sum is 10a + 45.',
         sol='The sum is a + (a + 1) + … + (a + 9) = 10a + 45, so it always ends in 5. Only 145 does: a = 10, giving 10 + 11 + … + 19 = 145.'),
    dict(ch='10', scen='half by bus a third of the rest by auto then 2 km walk',
         stem='Kajal travels half the way home by bus, one third of the remaining distance by auto, and walks the last 2 km. How far is her home?',
         opts=['6 km', '12 km', '9 km', '4 km'],
         hint='After the bus, half is left. The walk is two thirds of that half.',
         sol='After the bus, 1/2 is left. The auto takes 1/3 of that, leaving 2/3 of 1/2 = 1/3 of the whole. So 1/3 of the way is 2 km and the whole way is 6 km.'),

    # ---------------- Mixed Problems
    dict(ch='4+10', scen='border dots of an n by n dot square equal to 96',
         stem='An n × n square of dots has 4n − 4 dots on its border. Which square has exactly 96 dots on its border?',
         opts=['25 × 25', '24 × 24', '26 × 26', '12 × 12'],
         hint='Why is it 4n − 4 and not 4n? Put the corners back.',
         sol='Each side has n dots, but the 4 corners are counted twice, so the border has 4n − 4 dots. Adding the 4 corners back gives 96 + 4 = 100 = 4 × 25, so n = 25.'),
    dict(ch='1+10', scen='last digit of 2025 sevens multiplied together',
         stem='What is the last digit of 7 × 7 × 7 × … × 7, with 2,025 sevens?',
         opts=['7', '9', '3', '1'],
         hint='Look at the last digits of 7, 7 × 7, 7 × 7 × 7, …',
         sol='Last digits go 7, 9, 3, 1, 7, 9, 3, 1, … repeating every 4. 2,025 = 4 × 506 + 1, so the last digit is the 1st in the cycle: 7.'),
    dict(ch='3+9', scen='3-hour trip with 40% of the time at 60 km/h and the rest at 90 km/h',
         stem='Bharat drives for 3 hours. For 40% of the time he drives at 60 km/h and for the rest at 90 km/h. How far does he travel?',
         opts=['234 km', '225 km', '216 km', '252 km'],
         hint='40% of 3 hours is 1.2 hours.',
         sol='1.2 h at 60 km/h = 72 km. The other 1.8 h at 90 km/h = 162 km. Total 234 km. (225 km wrongly uses the average of the two speeds.)'),
    dict(ch='5+6', scen='equilateral triangle with the perimeter of a 9 cm square · side and total angles',
         stem='An equilateral triangle has the same perimeter as a square of side 9 cm. What is the side of the triangle, and what is the total of all the angles of both shapes?',
         opts=['12 cm; 540°', '12 cm; 450°', '9 cm; 540°', '12 cm; 360°'],
         hint='The angles of a triangle add to 180° and those of a square to 4 × 90°.',
         sol='Perimeter = 36 cm, so the triangle\'s side is 12 cm. Angles: 180° + 360° = 540°.'),
    dict(ch='4+9', scen='tank with 500 L losing 15 L an hour and tank with 200 L gaining 25 L an hour',
         stem='Tank A has 500 L and loses 15 L every hour. Tank B has 200 L and gains 25 L every hour. After how long do they hold the same amount?',
         opts=['7.5 hours', '12 hours', '7 hours', '8 hours'],
         hint='The gap of 300 L closes by 15 + 25 L each hour.',
         sol='The gap closes by 40 L per hour. 300 ÷ 40 = 7.5 hours. Check: A has 500 − 112.5 = 387.5 L and B has 200 + 187.5 = 387.5 L.'),
]
