# AMO Level-2 · Class 6 · Practice Paper 2


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
    dict(ch='1', scen='sum of place values of all the 5s in 5,25,50,000',
         stem='What is the sum of the place values of all the 5s in 5,25,50,000?',
         opts=['5,05,50,000', '15', '5,55,00,000', '5,50,50,000'],
         hint='Name the place of each 5: crores, lakhs, ten thousands.',
         sol='In 5,25,50,000 the 5s stand for 5 crores (5,00,00,000), 5 lakhs (5,00,000) and 5 ten-thousands (50,000). Sum: 5,00,00,000 + 5,00,000 + 50,000 = 5,05,50,000. (15 adds the face values.)'),
    dict(ch='1', scen='smallest number leaving remainder 1 on division by 2 to 6 and divisible by 7',
         stem='What is the smallest number that leaves remainder 1 when divided by 2, 3, 4, 5 or 6, but is exactly divisible by 7?',
         opts=['301', '61', '421', '361'],
         hint='The number is 1 more than a multiple of the LCM of 2, 3, 4, 5 and 6.',
         sol='LCM of 2, 3, 4, 5, 6 is 60, so the number is 61, 121, 181, 241, 301, … Test each for 7: 301 = 7 × 43 is the first one divisible by 7.'),
    dict(ch='1', scen='submarine at −120 m moving up and down · distance to a helicopter',
         stem='A submarine is at −120 m (below sea level). It rises 45 m, dives 80 m and then rises 30 m. A helicopter hovers 75 m above sea level. How far apart are they now?',
         opts=['200 m', '50 m', '125 m', '195 m'],
         hint='Find the submarine\'s final position as an integer first.',
         sol='−120 + 45 − 80 + 30 = −125 m. The helicopter is at +75 m. Distance = 75 − (−125) = 200 m.'),

    # ---------------- Part 2 · Operations
    dict(ch='2', scen='brackets placed in 8 plus 4 times 6 minus 2 · largest value',
         stem='Here are four ways of writing 8 + 4 × 6 − 2, with or without brackets. Which of these gives the largest value?',
         opts=['(8 + 4) × 6 − 2', '(8 + 4) × (6 − 2)', '8 + 4 × (6 − 2)', '8 + 4 × 6 − 2'],
         hint='Work out each one, brackets first.',
         sol='(8 + 4) × 6 − 2 = 72 − 2 = 70. (8 + 4) × (6 − 2) = 12 × 4 = 48. 8 + 4 × (6 − 2) = 8 + 16 = 24. 8 + 4 × 6 − 2 = 8 + 24 − 2 = 30. The largest is 70.'),
    dict(ch='2', scen='product of −1 to −5 divided by −6',
         stem='What is the value of (−1) × (−2) × (−3) × (−4) × (−5) ÷ (−6)?',
         opts=['20', '−20', '120', '−120'],
         hint='Count the negative signs first.',
         sol='Five negatives multiplied give a negative: 1 × 2 × 3 × 4 × 5 = 120, so the product is −120. Then −120 ÷ (−6) = 20 (negative ÷ negative is positive).'),
    dict(ch='2', scen='two integers with sum −7 and product −60',
         stem='The sum of two integers is −7 and their product is −60. What is the larger integer?',
         opts=['5', '12', '−5', '−12'],
         hint='The product is negative, so one integer is positive and one is negative.',
         sol='Pairs with product −60 and one negative: try 5 and −12. Sum 5 + (−12) = −7. The larger integer is 5.'),

    # ---------------- Part 3 · Fractions, Decimals & Percentages
    dict(ch='3', scen='which of 0.125 1/8 12.5% 3/25 is different',
         stem='Three of these are equal. Which one is different: 0.125, 1/8, 12.5%, 3/25?',
         opts=['3/25', '0.125', '1/8', '12.5%'],
         hint='Change each into a decimal.',
         sol='1/8 = 0.125 and 12.5% = 0.125. 3/25 = 12/100 = 0.12, so 3/25 is different.'),
    dict(ch='3', scen='tank 40% full becomes 85% full after 54 L',
         stem='A water tank is 40% full. After 54 litres are added, it is 85% full. What is the full capacity of the tank?',
         opts=['120 L', '135 L', '108 L', '90 L'],
         hint='The 54 litres fill 85% − 40% of the tank.',
         sol='54 L is 45% of the tank. 1% is 54 ÷ 45 = 1.2 L, so 100% is 120 L.'),
    dict(ch='3', scen='Pooja 72 of 90 against Kiran 84 of 105',
         stem='Pooja scored 72 out of 90 in a test. Kiran scored 84 out of 105 in another test. Compare their percentages.',
         opts=['Both scored 80%', 'Pooja did better, with 80%', 'Kiran did better, with 84%', 'Pooja did better, with 72%'],
         hint='Change each score to a percentage.',
         sol='Pooja: 72/90 = 8/10 = 80%. Kiran: 84/105 = 4/5 = 80%. Both scored 80%.'),

    # ---------------- Part 4 · Algebra
    dict(ch='4', scen='perimeter of rectangle 2x plus 3 by x minus 1 at x equals 7',
         stem='A rectangle has length (2x + 3) cm and breadth (x − 1) cm. Write its perimeter as an expression and find it when x = 7.',
         opts=['6x + 4; 46 cm', '3x + 2; 23 cm', '6x + 4; 34 cm', '6x + 8; 50 cm'],
         hint='Perimeter = 2 × (length + breadth).',
         sol='Length + breadth = 2x + 3 + x − 1 = 3x + 2. Perimeter = 2(3x + 2) = 6x + 4. At x = 7: 42 + 4 = 46 cm.'),
    dict(ch='4', scen='joined tables seating 6 10 14 · tables for 70 people',
         stem='One table seats 6 people. Two tables pushed together seat 10, and three seat 14. How many tables in a row are needed to seat exactly 70 people?',
         opts=['17', '18', '12', '16'],
         hint='Each extra table adds 4 seats. Write the seats for n tables.',
         sol='n tables seat 4n + 2 people. 4n + 2 = 70 gives 4n = 68, so n = 17.'),

    # ---------------- Part 5 · Geometry
    dict(ch='5', scen='two crossing lines with one angle four times its neighbour',
         stem='Two straight lines cross each other. One of the angles formed is 4 times the angle next to it. What is the size of the larger of these two angles?',
         opts=['144°', '36°', '135°', '150°'],
         hint='Two angles next to each other on a straight line add up to 180°.',
         sol='The two angles make 5 equal parts of 180°, so one part is 36°. The larger angle is 4 × 36° = 144°.'),
    dict(ch='5', scen='triangle with two 7 cm sides and 60° between them',
         stem='A triangle has two sides of 7 cm with an angle of 60° between them. Which type of triangle is it?',
         opts=['Equilateral', 'Isosceles but not equilateral', 'Scalene', 'Right-angled'],
         hint='Equal sides have equal angles opposite them.',
         sol='The two angles opposite the equal sides are equal, and together they make 180° − 60° = 120°. So each is 60°. All three angles are 60°, so the triangle is equilateral.'),
    dict(ch='5', scen='polygon whose diagonals are three times its sides',
         stem='A polygon has 3 times as many diagonals as sides. How many sides does it have?',
         opts=['9', '6', '12', '8'],
         hint='A polygon with n sides has n × (n − 3) ÷ 2 diagonals.',
         sol='n × (n − 3) ÷ 2 = 3n means (n − 3) ÷ 2 = 3, so n − 3 = 6 and n = 9. Check: a 9-sided polygon has 9 × 6 ÷ 2 = 27 = 3 × 9 diagonals.'),

    # ---------------- Part 6 · Mensuration
    dict(ch='6', scen='wire rectangle 18 by 14 rebent into a square',
         stem='A wire is bent into a rectangle 18 cm by 14 cm. It is then straightened and bent into a square. What is the area of the square?',
         opts=['256 cm²', '252 cm²', '64 cm²', '196 cm²'],
         hint='The perimeter stays the same.',
         sol='Wire length = 2 × (18 + 14) = 64 cm. Square side = 64 ÷ 4 = 16 cm. Area = 16 × 16 = 256 cm².'),
    dict(ch='6', scen='three 4 cm cubes joined end to end · surface area',
         stem='Three cubes of edge 4 cm are joined end to end to make a cuboid. What is the surface area of the cuboid?',
         opts=['224 cm²', '288 cm²', '192 cm²', '256 cm²'],
         hint='The cuboid is 12 cm × 4 cm × 4 cm.',
         sol='Surface area = 2 × (12 × 4 + 12 × 4 + 4 × 4) = 2 × (48 + 48 + 16) = 224 cm². (288 adds the three cubes\' areas, counting the 4 hidden faces.)'),
    dict(ch='6', scen='tank 2 m by 1.5 m by 1 m filled with 15 L buckets',
         stem='A tank is 2 m long, 1.5 m wide and 1 m deep. How many 15-litre buckets of water are needed to fill it? (1 m³ = 1,000 L)',
         opts=['200', '20', '2,000', '300'],
         hint='Find the volume in m³, then in litres.',
         sol='Volume = 2 × 1.5 × 1 = 3 m³ = 3,000 L. Buckets: 3,000 ÷ 15 = 200.'),

    # ---------------- Part 7 · Data Handling
    dict(ch='8', scen='rainfall bar graph · share of months under 60 mm',
         fig=drawing(330, 210, bars([('Jan', 40), ('Feb', 70), ('Mar', 30), ('Apr', 80), ('May', 50)], 90, 10, 'Rainfall (mm)')),
         stem='The bar graph shows the rainfall in a town. What fraction of the total rainfall fell in the months that had less than 60 mm each?',
         opts=['4/9', '5/9', '3/5', '2/5'],
         hint='Add all five bars, then the bars below 60 mm.',
         sol='Total: 40 + 70 + 30 + 80 + 50 = 270 mm. Months under 60 mm: 40 + 30 + 50 = 120 mm. 120/270 = 4/9.'),
    dict(ch='8', scen='shoe size frequency table · size 7 and above against 5 and below',
         fig=table(['Shoe size', '4', '5', '6', '7', '8'], [['Students', '3', '6', '9', '8', '4']], widths=[100, 50, 50, 50, 50, 50]),
         stem='The table shows the shoe sizes of the students in a class. How many more students wear size 7 or above than size 5 or below?',
         opts=['3', '1', '12', '9'],
         hint='"Or above" and "or below" include the size itself.',
         sol='Size 7 or above: 8 + 4 = 12. Size 5 or below: 3 + 6 = 9. 12 − 9 = 3.'),

    # ---------------- Part 8 · Applied Mathematics
    dict(ch='9', scen='cycling at 12 km/h late and 15 km/h early by 5 minutes',
         stem='Ravi cycles to school. At 12 km/h he reaches 5 minutes late. At 15 km/h he reaches 5 minutes early. How far is the school?',
         opts=['10 km', '12 km', '6 km', '15 km'],
         hint='The two journey times differ by 10 minutes. Try the options.',
         sol='At 12 km/h, 10 km takes 50 minutes. At 15 km/h it takes 40 minutes. The difference is 10 minutes, which matches 5 late and 5 early. So the school is 10 km away.'),
    dict(ch='9', scen='boys to girls 5:4 · 10 girls join to make 1:1',
         stem='In a club, the ratio of boys to girls is 5 : 4. After 10 more girls join, the numbers of boys and girls are equal. How many boys are there?',
         opts=['50', '40', '45', '60'],
         hint='The difference between boys and girls was 1 part.',
         sol='Boys are 5 parts and girls 4 parts, so the girls are 1 part short. 10 girls fill that gap, so 1 part = 10. Boys = 5 × 10 = 50.'),
    dict(ch='9', scen='8 pens ₹96 and 5 notebooks ₹175 · 6 pens and 3 notebooks',
         stem='8 pens cost ₹96 and 5 notebooks cost ₹175. How much do 6 pens and 3 notebooks cost?',
         opts=['₹177', '₹171', '₹183', '₹167'],
         hint='Use the unitary method for each item.',
         sol='One pen = 96 ÷ 8 = ₹12, so 6 pens = ₹72. One notebook = 175 ÷ 5 = ₹35, so 3 notebooks = ₹105. Total ₹177.'),

    # ---------------- Part 9 · Mathematical Reasoning
    dict(ch='10', scen='clock gaining 3 minutes an hour from Sunday noon',
         stem='A clock is set right at noon on Sunday. It gains 3 minutes every hour. What time does it show at the real noon on Monday?',
         opts=['1:12 PM', '12:48 PM', '1:24 PM', '1:00 PM'],
         hint='How many hours pass from Sunday noon to Monday noon?',
         sol='24 hours pass, so the clock gains 24 × 3 = 72 minutes = 1 hour 12 minutes. It shows 1:12 PM.'),
    dict(ch='10', scen='numbers 1 to 10 replaced by differences · parity of the last number',
         stem='The numbers 1 to 10 are written on a board. Mihir rubs out any two numbers and writes their difference. He repeats this until one number is left. What can you say about the last number?',
         opts=['It must be odd', 'It must be even', 'It must be 0', 'It must be 10'],
         hint='Look at whether the total of all the numbers is odd or even, and how it changes.',
         sol='The total 1 + 2 + … + 10 = 55 is odd. Replacing a and b by a − b changes the total by 2b, an even number, so the total stays odd. The last number is the total at the end, so it must be odd.'),
    dict(ch='10', scen='number times 3 minus 7 halved gives 25',
         stem='Neha thinks of a number. She multiplies it by 3, subtracts 7 and then halves the result. She gets 25. What was her number?',
         opts=['19', '21', '17', '11'],
         hint='Undo the steps in reverse order.',
         sol='Undo the halving: 25 × 2 = 50. Undo the subtraction: 50 + 7 = 57. Undo the multiplication: 57 ÷ 3 = 19.'),

    # ---------------- Mixed Problems
    dict(ch='4+10', scen='pattern 2 6 12 20 30 with nth term n times n plus 1 · which term is 210',
         fig=cards([2, 6, 12, 20, 30, '…'], size=40),
         stem='In this pattern, the nth number is n × (n + 1). Which term of the pattern is 210?',
         opts=['14th', '15th', '13th', '21st'],
         hint='Find two numbers next to each other whose product is 210.',
         sol='210 = 14 × 15, so n = 14. The 14th term is 210.'),
    dict(ch='1+10', scen='smallest 4-digit number divisible by 12 18 and 30',
         stem='What is the smallest 4-digit number that is exactly divisible by 12, by 18 and by 30?',
         opts=['1,080', '1,000', '1,260', '1,800'],
         hint='Find the LCM of 12, 18 and 30 first.',
         sol='12 = 2 × 2 × 3, 18 = 2 × 3 × 3, 30 = 2 × 3 × 5. LCM = 2 × 2 × 3 × 3 × 5 = 180. 180 × 5 = 900 is 3-digit, 180 × 6 = 1,080 is the smallest 4-digit multiple.'),
    dict(ch='3+9', scen='speed increased by 25% · percentage fall in journey time',
         stem='Simran increases her driving speed by 25% on the same route. By what percentage does her journey time go down?',
         opts=['20%', '25%', '75%', '80%'],
         hint='Try a speed of 40 km/h and a distance of 200 km.',
         sol='At 40 km/h, 200 km takes 5 hours. At 25% more, 50 km/h, it takes 4 hours. The time falls by 1 hour out of 5, which is 20%.'),
    dict(ch='5+6', scen='open box folded from a 20 cm square with 5 cm corners cut',
         stem='Squares of side 5 cm are cut from the four corners of a 20 cm square sheet. The sides are folded up to make an open box. What is the volume of the box?',
         opts=['500 cm³', '1,500 cm³', '2,000 cm³', '1,000 cm³'],
         hint='The base of the box is what is left in the middle.',
         sol='The base is 20 − 5 − 5 = 10 cm on each side and the height is 5 cm. Volume = 10 × 10 × 5 = 500 cm³.'),
    dict(ch='4+9', scen='mobile plans ₹199 plus ₹2 a minute against ₹99 plus ₹4 a minute',
         stem='Plan A costs ₹199 plus ₹2 per minute. Plan B costs ₹99 plus ₹4 per minute. For how many minutes in a month do the two plans cost the same?',
         opts=['50', '25', '100', '49'],
         hint='Plan B starts ₹100 cheaper but costs ₹2 more every minute.',
         sol='Plan B starts ₹100 cheaper. Each minute it catches up by ₹2. After 100 ÷ 2 = 50 minutes they are equal: 199 + 100 = 299 and 99 + 200 = 299.'),
]
