# AMO Level-2 · Class 6 · Practice Paper 9


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


def frame():
    return [('rect', 0, 0, 175, 125, 'peach'), ('rect', 12.5, 12.5, 150, 100, 'white'),
            ('text', 87, 62, 'photo 30 cm × 20 cm', 11), ('text', 87, 140, 'border 2.5 cm wide all round', 10)]


QUESTIONS = [
    # ---------------- Part 1 · Number System
    dict(ch='1', scen='place value of 6 divided by face value of 4 in 3,62,45,108',
         stem='In 3,62,45,108, the place value of 6 is divided by the face value of 4. What is the answer?',
         opts=['15,00,000', '60,00,000', '1,50,000', '15,000'],
         hint='The face value of a digit is the digit itself.',
         sol='6 is in the ten-lakhs place, so its place value is 60,00,000. The face value of 4 is 4. 60,00,000 ÷ 4 = 15,00,000.'),
    dict(ch='1', scen='HCF of 1,001 and 1,155 by prime factorisation',
         stem='What is the HCF of 1,001 and 1,155?',
         opts=['77', '7', '11', '143'],
         hint='Write both numbers as products of primes.',
         sol='1,001 = 7 × 11 × 13 and 1,155 = 3 × 5 × 7 × 11. Common primes: 7 and 11. HCF = 77.'),
    dict(ch='1', scen='Kanchenjunga top above the Dead Sea shore',
         stem='The top of Everest is at 8,849 m and the shore of the Dead Sea is at −430 m. Kanchenjunga is 263 m lower than Everest. How far is the top of Kanchenjunga above the Dead Sea shore?',
         opts=['9,016 m', '8,156 m', '9,542 m', '8,586 m'],
         hint='Find the height of Kanchenjunga, then subtract a negative number.',
         sol='Kanchenjunga: 8,849 − 263 = 8,586 m. Difference: 8,586 − (−430) = 8,586 + 430 = 9,016 m.'),

    # ---------------- Part 2 · Operations
    dict(ch='2', scen='7 plus 6 times curly 5 minus round 4 minus 3 times 2',
         stem='What is the value of 7 + [6 × {5 − (4 − 3 × 2)}]?',
         opts=['49', '25', '13', '91'],
         hint='Inside the round bracket, multiply first.',
         sol='3 × 2 = 6, so (4 − 6) = −2. {5 − (−2)} = 7. 6 × 7 = 42. 7 + 42 = 49.'),
    dict(ch='2', scen='next number after −81 27 −9 3',
         stem='What is the next number in the pattern −81, 27, −9, 3, …?',
         opts=['−1', '1', '−3', '0'],
         hint='What do you divide by each time?',
         sol='Each number is the one before divided by −3: −81 ÷ (−3) = 27, 27 ÷ (−3) = −9, −9 ÷ (−3) = 3. Next: 3 ÷ (−3) = −1.'),
    dict(ch='2', scen='subtract −7 from sum of −12 and 5 then multiply by −3',
         stem='Ravi subtracts −7 from the sum of −12 and 5, and then multiplies the result by −3. What does he get?',
         opts=['0', '42', '−42', '−6'],
         hint='Subtracting −7 is the same as adding 7.',
         sol='−12 + 5 = −7. Then −7 − (−7) = 0. 0 × (−3) = 0.'),

    # ---------------- Part 3 · Fractions, Decimals & Percentages
    dict(ch='3', scen='0.4 of a number is 36 · 45% of it',
         stem='0.4 of a number is 36. What is 45% of the same number?',
         opts=['40.5', '16.2', '45', '36.45'],
         hint='Find the number first.',
         sol='0.4 × number = 36, so the number is 90. 45% of 90 = 40.5.'),
    dict(ch='3', scen='480 mm plant grows 25% then 10% trimmed',
         stem='A plant is 480 mm tall. In a month it grows 25% taller. Then 10% of its new height is trimmed off. How tall is it now?',
         opts=['540 mm', '552 mm', '528 mm', '600 mm'],
         hint='The 10% is taken off the new height, not the old one.',
         sol='After growing: 480 + 25% of 480 = 480 + 120 = 600 mm. After trimming 10%: 600 − 60 = 540 mm.'),
    dict(ch='3', scen='3/5 boys with 25% of boys and 30% of girls playing chess',
         stem='In a class, 3/5 of the students are boys. 25% of the boys and 30% of the girls play chess. What percentage of the class plays chess?',
         opts=['27%', '55%', '28%', '26%'],
         hint='Imagine a class of 100: 60 boys and 40 girls.',
         sol='Out of 100: 25% of 60 = 15 boys and 30% of 40 = 12 girls. 27 out of 100 = 27%. (55% wrongly adds the two percentages.)'),

    # ---------------- Part 4 · Algebra
    dict(ch='4', scen='isosceles sides 2a plus 1 and base a plus 4 · when equilateral',
         stem='An isosceles triangle has two equal sides of (2a + 1) cm and a base of (a + 4) cm. For which value of a is it equilateral, and what is its perimeter then?',
         opts=['a = 3, 21 cm', 'a = 3, 14 cm', 'a = 5, 31 cm', 'a = 4, 27 cm'],
         hint='Equilateral means the base equals the other two sides. Test each value of a.',
         sol='a = 3: 2a + 1 = 7 and a + 4 = 7, so all sides are 7 cm and the perimeter is 21 cm. a = 4 gives 9 and 8; a = 5 gives 11 and 9, so those are not equilateral. (14 cm is only two sides.)'),
    dict(ch='4', scen='rows of chairs starting at 10 and adding 2 · 15th row',
         stem='In a hall, the 1st row has 10 chairs and each row has 2 more than the row in front. Write the number of chairs in the nth row, and find it for the 15th row.',
         opts=['2n + 8; 38', '2n + 10; 40', '10n; 150', '2n + 8; 36'],
         hint='Check your expression for n = 1 and n = 2.',
         sol='Row n has 10 + 2(n − 1) = 2n + 8 chairs. Check: n = 1 gives 10, n = 2 gives 12. For n = 15: 30 + 8 = 38.'),

    # ---------------- Part 5 · Geometry
    dict(ch='5', scen='turning 225 anticlockwise from south-east',
         stem='Dev faces south-east. He turns 225° anticlockwise. Which direction does he face now?',
         opts=['West', 'North', 'East', 'North-west'],
         hint='Turn 180° first, then 45° more.',
         sol='180° anticlockwise from south-east is north-west. 45° more anticlockwise is west.'),
    dict(ch='5', scen='isosceles triangles with whole-number sides and perimeter 20',
         stem='How many different isosceles triangles have whole-number sides (in cm) and a perimeter of 20 cm?',
         opts=['4', '5', '3', '9'],
         hint='Sides a, a, b with 2a + b = 20. The two equal sides together must be longer than b.',
         sol='b = 20 − 2a must be positive and less than 2a. a = 6: (6, 6, 8). a = 7: (7, 7, 6). a = 8: (8, 8, 4). a = 9: (9, 9, 2). a = 5 gives (5, 5, 10), which is flat. So 4 triangles.'),
    dict(ch='5', scen='extra diagonals when a hexagon becomes a 12-sided polygon',
         stem='Each corner of a regular hexagon is cut off to make a regular 12-sided polygon. How many more diagonals does the new shape have than the hexagon?',
         opts=['45', '54', '36', '27'],
         hint='A polygon with n sides has n × (n − 3) ÷ 2 diagonals.',
         sol='Hexagon: 6 × 3 ÷ 2 = 9. 12-sided polygon: 12 × 9 ÷ 2 = 54. Difference: 54 − 9 = 45.'),

    # ---------------- Part 6 · Mensuration
    dict(ch='6', scen='2.5 cm frame around a 30 by 20 photo · frame area',
         fig=drawing(180, 150, frame()),
         stem='A photo 30 cm by 20 cm has a frame 2.5 cm wide all round it. What is the area of the frame alone?',
         opts=['275 cm²', '250 cm²', '262.5 cm²', '300 cm²'],
         hint='The outer rectangle is 35 cm by 25 cm.',
         sol='Outer: 35 × 25 = 875 cm². Photo: 30 × 20 = 600 cm². Frame = 875 − 600 = 275 cm².'),
    dict(ch='6', scen='30 cm cube tank two thirds full · water to fill it',
         stem='A cube-shaped tank has inner edge 30 cm and is two thirds full of water. How many litres are needed to fill it? (1,000 cm³ = 1 L)',
         opts=['9 L', '18 L', '27 L', '10 L'],
         hint='Find the full volume in litres first.',
         sol='Volume = 30 × 30 × 30 = 27,000 cm³ = 27 L. One third is empty: 27 ÷ 3 = 9 L.'),
    dict(ch='6', scen='cuboid 12 by 8 with surface area 592 · height',
         stem='A cuboid is 12 cm long and 8 cm wide. Its total surface area is 592 cm². What is its height?',
         opts=['10 cm', '12 cm', '8 cm', '15 cm'],
         hint='Half the surface area is one of each pair of faces.',
         sol='Half the surface area is 296 cm²: the top (12 × 8 = 96) plus one long side and one short side. The two sides together are 296 − 96 = 200 cm², and they make a strip 12 + 8 = 20 cm long and h tall. So h = 200 ÷ 20 = 10 cm.'),

    # ---------------- Part 7 · Data Handling
    dict(ch='8', scen='bookshop sales bar graph · three quarters of February and May minus March',
         fig=drawing(330, 210, bars([('Jan', 150), ('Feb', 200), ('Mar', 125), ('Apr', 225), ('May', 175)], 250, 25, 'Books sold')),
         stem='The bar graph shows books sold by a shop. In which month were sales exactly 3/4 of February\'s, and how many more books were sold in May than in March?',
         opts=['January; 50', 'March; 50', 'January; 75', 'May; 50'],
         hint='Find 3/4 of February\'s sales first.',
         sol='February: 200. 3/4 of 200 = 150, which is January. May 175 − March 125 = 50.'),
    dict(ch='8', scen='plant heights table · fraction over 12 cm and at most 16 cm',
         fig=table(['Height (cm)', '10', '12', '14', '16', '18'], [['Plants', '2', '5', '8', '3', '2']], widths=[110, 50, 50, 50, 50, 50]),
         stem='The table shows the heights of 20 plants. What fraction of the plants are taller than 12 cm but not taller than 16 cm?',
         opts=['11/20', '13/20', '2/5', '3/5'],
         hint='Only the 14 cm and 16 cm plants count.',
         sol='Plants of 14 cm and 16 cm: 8 + 3 = 11 out of 20, which is 11/20.'),

    # ---------------- Part 8 · Applied Mathematics
    dict(ch='9', scen='120 m train passing a pole in 8 s and a platform in 20 s',
         stem='A train 120 m long passes a pole in 8 seconds and a platform in 20 seconds. How long is the platform?',
         opts=['180 m', '300 m', '150 m', '120 m'],
         hint='Find the speed from the pole first.',
         sol='Speed = 120 ÷ 8 = 15 m/s. In 20 s the train covers 300 m, which is its own length plus the platform. Platform = 300 − 120 = 180 m.'),
    dict(ch='9', scen='roses lilies tulips in ratios 4:7 and 3:5 with 35 tulips',
         stem='In a garden, roses : lilies = 4 : 7 and lilies : tulips = 3 : 5. There are 35 tulips. How many roses are there?',
         opts=['12', '20', '21', '15'],
         hint='Find the lilies from the tulips first.',
         sol='Lilies : tulips = 3 : 5, so 35 tulips means 21 lilies. Roses : lilies = 4 : 7, so 21 lilies means 12 roses.'),
    dict(ch='9', scen='car using 8 L per 100 km at ₹105 per litre for 450 km',
         stem='A car uses 8 litres of petrol for every 100 km. Petrol costs ₹105 a litre. What does the petrol for a 450 km trip cost?',
         opts=['₹3,780', '₹3,360', '₹4,725', '₹3,840'],
         hint='Find the litres needed for 450 km first.',
         sol='Litres = 8 × 4.5 = 36 L. Cost = 36 × 105 = ₹3,780.'),

    # ---------------- Part 9 · Mathematical Reasoning
    dict(ch='10', scen='9 o\'clock plus 57 hours on a 12-hour clock',
         stem='A 12-hour clock shows 9 o\'clock. What will it show 57 hours later?',
         opts=['6 o\'clock', '9 o\'clock', '3 o\'clock', '5 o\'clock'],
         hint='Every 12 hours the clock shows the same time.',
         sol='57 = 12 × 4 + 9. After 48 hours it shows 9 o\'clock again; 9 more hours gives 6 o\'clock.'),
    dict(ch='10', scen='fifteen numbers each 1 or −1 · possible sum',
         stem='Kiran writes 15 numbers, each either 1 or −1. Which of these could be their sum?',
         opts=['−3', '0', '4', '−16'],
         hint='Is the sum of 15 odd numbers odd or even? How big can it be?',
         sol='Each number is odd, and 15 odd numbers add to an odd number, so 0 and 4 are impossible. The sum is between −15 and 15, so −16 is impossible. −3 works: six 1s and nine −1s.'),
    dict(ch='10', scen='points doubled then minus 5 each round · 37 after three rounds',
         stem='In a game, a player\'s points are doubled and then 5 is taken away each round. After 3 rounds Ravi has 37 points. How many did he start with?',
         opts=['9', '11', '7', '16'],
         hint='Undo each round: add 5, then halve.',
         sol='(37 + 5) ÷ 2 = 21. (21 + 5) ÷ 2 = 13. (13 + 5) ÷ 2 = 9. Check: 9 → 13 → 21 → 37.'),

    # ---------------- Mixed Problems
    dict(ch='4+10', scen='pattern n times n minus n · which term is 110',
         fig=cards([0, 2, 6, 12, 20, '…'], size=40),
         stem='The nth number of this pattern is n × n − n. Which term is 110?',
         opts=['11th', '10th', '12th', '110th'],
         hint='n × n − n = n × (n − 1). Which two numbers next to each other multiply to 110?',
         sol='n × (n − 1) = 110 = 11 × 10, so n = 11. Check: 11 × 11 − 11 = 110.'),
    dict(ch='1+10', scen='2-digit numbers with exactly three factors',
         stem='How many 2-digit numbers have exactly 3 factors?',
         opts=['2', '4', '3', '5'],
         hint='Try a few: 4 has factors 1, 2, 4. 9 has 1, 3, 9. What kind of numbers are these?',
         sol='A number with exactly 3 factors is a prime times itself: 1, p and p × p. Two-digit ones: 5 × 5 = 25 and 7 × 7 = 49. (11 × 11 = 121 is too big.) So 2.'),
    dict(ch='3+9', scen='walking at 80% of a friend\'s speed · time for a 24-minute walk',
         stem='Neha walks at 80% of Tanya\'s speed. Tanya takes 24 minutes for a walk. How long does Neha take for the same walk?',
         opts=['30 min', '28.8 min', '19.2 min', '32 min'],
         hint='Pick a length for the walk that works with 24 minutes.',
         sol='Say the walk is 1,200 m. Tanya walks 1,200 ÷ 24 = 50 m a minute. Neha walks 80% of that, 40 m a minute, so she takes 1,200 ÷ 40 = 30 minutes. (28.8 wrongly adds 20% to the time.)'),
    dict(ch='5+6', scen='two right triangles with legs 6 and 8 joined along the 8 cm sides',
         stem='Two identical right-angled triangles with shorter sides 6 cm and 8 cm are joined along their 8 cm sides to make one triangle. What type of triangle is it, and what is its area?',
         opts=['Isosceles; 48 cm²', 'Isosceles; 24 cm²', 'Equilateral; 48 cm²', 'Scalene; 96 cm²'],
         hint='The two long sides of the new triangle are the same length.',
         sol='The new triangle has two equal sides (the long sides of the two pieces), so it is isosceles. Each piece is half of a 6 cm × 8 cm rectangle, so its area is 48 ÷ 2 = 24 cm², and the total is 48 cm².'),
    dict(ch='4+9', scen='hall booking ₹2,000 plus ₹150 per person · ₹175 each',
         stem='A hall costs ₹(2,000 + 150p) for p people. The cost is shared equally. How many people must come so that each person pays exactly ₹175?',
         opts=['80', '40', '100', '60'],
         hint='Each person pays ₹150 for themselves plus a share of the ₹2,000.',
         sol='Each person pays 150 + 2,000 ÷ p = 175, so 2,000 ÷ p = 25 and p = 80. Check: 2,000 + 12,000 = 14,000 = 80 × 175.'),
]
