# AMO Level-2 · Class 5 · Practice Paper 10  (format: see paper01.py)


def bars(data, top, step, unit='', bw=34, gap=22, h=150):
    """Simple bar graph: data = [(label, value)], y axis from 0 to top with gridlines every step."""
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


def square_mids():
    s = 12
    P = lambda x, y: (10 + x * s, 10 + (10 - y) * s)
    return [('rect', 10, 10, 120, 120, 'white'), ('poly', [P(0, 0), P(10, 5), P(5, 10)], 'blue'),
            ('text', *P(-0.9, -0.6), 'A', 12), ('text', *P(11, 5), 'M', 12), ('text', *P(5, 11), 'N', 12),
            ('text', *P(5, -1.2), '10 cm', 11)]


QUESTIONS = [
    # ---------------- Part 1 · Number System
    dict(ch='1', scen='smallest number with exactly six factors',
         stem='Which is the smallest of these numbers that has exactly 6 factors: 12, 18, 20 or 24?',
         opts=['12', '18', '20', '24'],
         hint='List the factors of each number.',
         sol='12: 1, 2, 3, 4, 6, 12 (6 factors). 18: 1, 2, 3, 6, 9, 18 (6). 20: 1, 2, 4, 5, 10, 20 (6). 24 has 8 factors. The smallest with exactly 6 is 12.'),
    dict(ch='1', scen='two numbers with product 2,160 and HCF 12 · LCM',
         stem='Two numbers multiply to give 2,160. Their HCF is 12. What is their LCM?',
         opts=['180', '2,148', '120', '360'],
         hint='For any two numbers, HCF × LCM = the product of the numbers. Or try 36 and 60.',
         sol='HCF × LCM = 2,160, so LCM = 2,160 ÷ 12 = 180. Check with 36 and 60: product 2,160, HCF 12, LCM 180.'),
    dict(ch='1', scen='7 lakhs 15 thousands 12 hundreds and 9 ones',
         stem='Which number is made of 7 lakhs, 15 thousands, 12 hundreds and 9 ones?',
         opts=['7,16,209', '7,15,129', '7,16,290', '8,52,109'],
         hint='12 hundreds is 1 thousand and 2 hundreds.',
         sol='7,00,000 + 15,000 + 1,200 + 9 = 7,16,209.'),

    # ---------------- Part 2 · Operations
    dict(ch='2', scen='5 plus 3 times square bracket 8 minus bracket 6 minus 4 times 2 divided by 2',
         fig=equations([['5 + 3 × [8 − (6 − 4) × 2] ÷ 2', '=', '?']], size=28),
         stem='Vrinda works out this expression in the correct order. What answer does she get?',
         opts=['11', '16', '10', '20'],
         hint='Start with the round bracket, then finish the square bracket.',
         sol='6 − 4 = 2. Square bracket: 8 − 2 × 2 = 8 − 4 = 4. Then 3 × 4 = 12, 12 ÷ 2 = 6 and 5 + 6 = 11. (16 adds 5 + 3 first.)'),
    dict(ch='2', scen='198 items at ₹49 estimated as 200 times 50',
         stem='A shop sells 198 toys at ₹49 each. Shalini estimates the takings as 200 × 50. By how much is her estimate too high?',
         opts=['₹298', '₹300', '₹202', '₹98'],
         hint='Work out 198 × 49 exactly as 198 × 50 − 198.',
         sol='198 × 49 = 198 × 50 − 198 = 9,900 − 198 = ₹9,702. Estimate: ₹10,000. Too high by 10,000 − 9,702 = ₹298.'),
    dict(ch='2', scen='brackets that keep 24 divided by 4 times 3 plus 6 the same',
         stem='The value of 24 ÷ 4 × 3 + 6 is 24. Which way of adding brackets keeps the value 24?',
         opts=['(24 ÷ 4) × 3 + 6', '24 ÷ (4 × 3) + 6', '24 ÷ 4 × (3 + 6)', '24 ÷ (4 × 3 + 6)'],
         hint='Work out each one.',
         sol='(24 ÷ 4) × 3 + 6 = 18 + 6 = 24, the same as working left to right. 24 ÷ 12 + 6 = 8. 6 × 9 = 54. 24 ÷ 18 is not even a whole number.'),

    # ---------------- Part 3 · Fractions, Decimals & Percentages
    dict(ch='3', scen='election of 1,200 voters · 85 percent voted · winner 60 percent',
         stem='A village has 1,200 voters. 85% of them voted. The winner got 60% of the votes cast. How many votes did the winner get?',
         opts=['612', '720', '510', '680'],
         hint='Find the number of votes cast first.',
         sol='Votes cast: 85% of 1,200 = 1,020. Winner: 60% of 1,020 = 6 × 102 = 612. (720 is 60% of all 1,200 voters.)'),
    dict(ch='3', scen='how many of 4/5 16/20 8/100 12/15 equal 0.8',
         stem='How many of these are equal to 0.8: 4/5, 16/20, 8/100, 12/15?',
         opts=['3', '2', '4', '1'],
         hint='Simplify each fraction.',
         sol='4/5 = 0.8, 16/20 = 4/5 = 0.8, 12/15 = 4/5 = 0.8. But 8/100 = 0.08. So 3 of them.'),
    dict(ch='3', scen='250 g biscuits at ₹42.50 · cost of 1.5 kg',
         stem='A 250 g packet of biscuits costs ₹42.50. At the same rate, how much do 1.5 kg of these biscuits cost?',
         opts=['₹255', '₹63.75', '₹170', '₹637.50'],
         hint='How many 250 g packets make 1.5 kg?',
         sol='1.5 kg = 1,500 g = 6 packets of 250 g. 6 × 42.50 = ₹255.'),
    dict(ch='3', scen='class of 36 · 2/3 girls · bus users among girls and boys',
         stem='A class has 36 students and 2/3 of them are girls. 3/8 of the girls and 1/4 of the boys come by bus. How many students come by bus?',
         opts=['12', '9', '15', '18'],
         hint='Find the number of girls and boys first.',
         sol='Girls: 2/3 of 36 = 24. Boys: 12. By bus: 3/8 of 24 = 9 girls and 1/4 of 12 = 3 boys. 9 + 3 = 12.'),

    # ---------------- Part 4 · Geometry
    dict(ch='5', scen='straight angle split into 47 68 and a third angle',
         stem='A straight angle is split into three angles. Two of them are 47° and 68°. What is the third angle, and what type is it?',
         opts=['65°, acute', '65°, obtuse', '75°, acute', '115°, obtuse'],
         hint='A straight angle is 180°.',
         sol='180° − 47° − 68° = 65°. It is less than 90°, so it is acute.'),
    dict(ch='5', scen='triangle with angles 35 and 55 · classify',
         stem='Two angles of a triangle are 35° and 55°. How is the triangle best described?',
         opts=['Right-angled scalene', 'Acute-angled isosceles', 'Right-angled isosceles', 'Obtuse-angled scalene'],
         hint='Find the third angle first.',
         sol='Third angle: 180° − 35° − 55° = 90°, so it is right-angled. All three angles are different, so all three sides are different: scalene.'),
    dict(ch='5', scen='wheel with five equal spokes · smallest turn',
         stem='A wheel has 5 equally spaced spokes and nothing else marked on it. What is the smallest turn that makes it look exactly the same?',
         opts=['72°', '60°', '90°', '36°'],
         hint='It looks the same 5 times in one full turn.',
         sol='Its order of rotational symmetry is 5, so the smallest turn is 360° ÷ 5 = 72°.'),

    # ---------------- Part 5 · Mensuration
    dict(ch='6', scen='litres in a cube tank with 1.5 m edges',
         stem='A cube-shaped water tank has edges 1.5 m long. How many litres does it hold when full? (1 m³ = 1,000 L)',
         opts=['3,375 L', '2,250 L', '337.5 L', '33,750 L'],
         hint='Work in centimetres or in metres: 1.5 × 1.5 × 1.5.',
         sol='1.5 × 1.5 = 2.25 and 2.25 × 1.5 = 3.375 m³. 3.375 × 1,000 = 3,375 L.'),
    dict(ch='6', scen='16 by 10 rectangle cut lengthwise and placed end to end',
         stem='Suhani cuts a 16 cm by 10 cm card into two pieces 16 cm by 5 cm and puts them end to end to make one long rectangle. What is its perimeter?',
         opts=['74 cm', '52 cm', '84 cm', '64 cm'],
         hint='The new rectangle is 32 cm long.',
         sol='The new rectangle is 32 cm by 5 cm. Perimeter: 2 × (32 + 5) = 74 cm. (The old card had perimeter 52 cm.)'),
    dict(ch='6', scen='triangle from a corner to two side midpoints of a 10 cm square',
         fig=drawing(150, 150, square_mids()),
         stem='M and N are the middle points of two sides of a 10 cm square, as shown. Corner A is joined to M and N. What is the area of the shaded triangle AMN?',
         opts=['37.5 cm²', '50 cm²', '25 cm²', '62.5 cm²'],
         hint='The three white parts are right-angled triangles.',
         sol='White triangles: half of 10 × 5 = 25, another 25, and half of 5 × 5 = 12.5. Total 62.5 cm². Shaded: 100 − 62.5 = 37.5 cm².'),

    # ---------------- Part 6 · Data Handling
    dict(ch='8', scen='bar graph of test marks out of 50 · tests above 70 percent',
         fig=drawing(300, 200, bars([('Test 1', 35), ('Test 2', 42), ('Test 3', 28), ('Test 4', 45)], 50, 5, 'Marks out of 50')),
         stem='The bar graph shows Riya\'s marks out of 50 in four tests. In how many tests did she score more than 70%?',
         opts=['2', '3', '1', '4'],
         hint='70% of 50 is 35. Is 35 itself more than 70%?',
         sol='70% of 50 = 35. Marks more than 35: 42 and 45. Test 1 is exactly 35, which is not more than 70%. So 2 tests.'),

    # ---------------- Part 7 · Applied Mathematics
    dict(ch='9', scen='150 m train passing a pole in 10 seconds · speed in km/h',
         stem='A train 150 m long passes a pole in 10 seconds. What is its speed in km/h?',
         opts=['54 km/h', '15 km/h', '90 km/h', '36 km/h'],
         hint='Its front must travel its own length to pass the pole.',
         sol='It travels 150 m in 10 s, which is 15 m every second. In one hour (3,600 s): 15 × 3,600 = 54,000 m = 54 km. So 54 km/h.'),
    dict(ch='9', scen='90 km out at 45 km/h and back at 30 km/h · average',
         stem='Arjun drives 90 km to a town at 45 km/h and comes back the same way at 30 km/h. What is his average speed for the whole trip?',
         opts=['36 km/h', '37.5 km/h', '40 km/h', '35 km/h'],
         hint='Find the time for each way.',
         sol='Going: 90 ÷ 45 = 2 h. Returning: 90 ÷ 30 = 3 h. 180 km in 5 h: 180 ÷ 5 = 36 km/h. (37.5 is the plain average of the speeds.)'),
    dict(ch='9', scen='minutes from 10:40 PM Tuesday to 7:15 AM Wednesday',
         stem='Jaya goes to sleep at 10:40 PM on Tuesday and wakes at 7:15 AM on Wednesday. For how many minutes does she sleep?',
         opts=['515', '475', '535', '495'],
         hint='Count to midnight first.',
         sol='10:40 PM to midnight: 1 h 20 min. Midnight to 7:15 AM: 7 h 15 min. Total 8 h 35 min = 480 + 35 = 515 minutes.'),
    dict(ch='9', scen='2 free pens for every 10 bought · cost of 36 pens',
         stem='A shop gives 2 free pens for every 10 pens you buy. Each pen costs ₹7.50. Kiran needs 36 pens. What is the least he must pay?',
         opts=['₹225', '₹270', '₹240', '₹232.50'],
         hint='Every 10 pens bought gives 12 pens.',
         sol='30 pens bought give 6 free pens: 36 pens. Cost: 30 × 7.50 = ₹225. (Buying 29 pens gives only 2 × 2 = 4 free, 33 in all.)'),

    # ---------------- Part 8 · Mathematical Reasoning
    dict(ch='10', scen='series 1 8 27 64 of numbers times themselves twice',
         fig=cards([1, 8, 27, 64, '?'], size=40),
         stem='In this series, the 2nd number is 2 × 2 × 2. Which number comes next?',
         opts=['125', '100', '81', '216'],
         hint='The 3rd number is 3 × 3 × 3.',
         sol='1 = 1 × 1 × 1, 8 = 2 × 2 × 2, 27 = 3 × 3 × 3, 64 = 4 × 4 × 4. Next: 5 × 5 × 5 = 125.'),
    dict(ch='10', scen='third Saturday after Monday 10 June',
         stem='Today is Monday, 10 June. What is the date of the third Saturday after today?',
         opts=['29 June', '22 June', '30 June', '6 July'],
         hint='The first Saturday after Monday 10 June is 5 days later.',
         sol='The Saturdays after today are 15 June, 22 June and 29 June. The third is 29 June.'),
    dict(ch='10', scen='which could be the product of two consecutive numbers',
         stem='Gaurav multiplies two whole numbers that come one after the other, like 4 × 5. Which of these could be his answer?',
         opts=['56', '45', '91', '63'],
         hint='One of two numbers next to each other is always even.',
         sol='Of two numbers next to each other, one is even, so the product is even. Only 56 is even, and 56 = 7 × 8.'),
    dict(ch='10', scen='squares of all sizes in a 4 by 4 grid',
         fig=grid([[''] * 4 for _ in range(4)], cell=30),
         stem='How many squares of all sizes are there in this 4 by 4 grid?',
         opts=['30', '16', '20', '25'],
         hint='Count 1 by 1, 2 by 2, 3 by 3 and 4 by 4 squares.',
         sol='1 by 1: 16. 2 by 2: 9. 3 by 3: 4. 4 by 4: 1. 16 + 9 + 4 + 1 = 30.'),

    # ---------------- Section II · Star Questions
    dict(ch='1+10', scen='primes in the series 3 7 11 15 below 100',
         fig=cards([3, 7, 11, 15, '…'], size=40),
         stem='The series goes up by 4 each time and stops before 100. How many numbers in the series are prime?',
         opts=['13', '12', '14', '11'],
         hint='The series is 3, 7, 11, 15, 19, …, 99. Cross out multiples of 3, 5 and 7.',
         sol='The numbers are 3, 7, 11, 15, 19, 23, 27, 31, 35, 39, 43, 47, 51, 55, 59, 63, 67, 71, 75, 79, 83, 87, 91, 95, 99. The primes are 3, 7, 11, 19, 23, 31, 43, 47, 59, 67, 71, 79, 83: 13. (91 = 7 × 13 and 51 = 3 × 17 are not prime.)'),
    dict(ch='3+10', scen='series going down by 0.25 from 2.5 · first below 1',
         fig=cards(['2.5', '2.25', '2', '1.75', '…'], size=40),
         stem='The series goes down by the same amount each time. Which number in the series (1st, 2nd, …) is the first one less than 1?',
         opts=['8th', '7th', '6th', '10th'],
         hint='List the numbers until you go below 1.',
         sol='2.5, 2.25, 2, 1.75, 1.5, 1.25, 1, 0.75. The 7th number is exactly 1, which is not less than 1. The 8th, 0.75, is the first below 1.'),
    dict(ch='6+10', scen='cuboids 1 by 1 by 2 then 2 by 2 by 3 · fifth volume',
         stem='Om builds cuboids from 1 cm cubes: 1 × 1 × 2, then 2 × 2 × 3, then 3 × 3 × 4, and so on. What is the volume of the 5th cuboid?',
         opts=['150 cm³', '125 cm³', '180 cm³', '210 cm³'],
         hint='Write the size of the 5th cuboid first.',
         sol='The 5th cuboid is 5 × 5 × 6. Volume: 25 × 6 = 150 cm³.'),
    dict(ch='1+9', scen='₹1,100 on ₹45 notebooks then ₹5 pencils',
         stem='Mohan has ₹1,100. He buys as many ₹45 notebooks as he can, and then spends the money left on ₹5 pencils. How many pencils does he buy?',
         opts=['4', '1', '2', '0'],
         hint='Find how many notebooks he can buy and how much is left.',
         sol='45 × 24 = 1,080 and 45 × 25 = 1,125, which is too much. So 24 notebooks, leaving 1,100 − 1,080 = ₹20. 20 ÷ 5 = 4 pencils.'),
    dict(ch='3+9', scen='₹2,560 · 25 percent on clothes and 0.3 of the rest on books',
         stem='Anand has ₹2,560. He spends 25% of it on clothes and then 0.3 of the money left on books. How much does he have now?',
         opts=['₹1,344', '₹1,152', '₹1,408', '₹1,216'],
         hint='Find the money left after the clothes first.',
         sol='25% of 2,560 = ₹640, leaving ₹1,920. 0.3 of 1,920 = ₹576. Left: 1,920 − 576 = ₹1,344. (₹1,152 wrongly takes 0.3 of 2,560.)'),
]
