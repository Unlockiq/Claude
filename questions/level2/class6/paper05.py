# AMO Level-2 · Class 6 · Practice Paper 5


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
    dict(ch='1', scen='1 crore 20 lakh in millions',
         stem='A city has 1 crore 20 lakh people. How many millions is that in the international system?',
         opts=['12', '120', '1.2', '1,200'],
         hint='1 million = 10 lakh.',
         sol='1 crore 20 lakh = 1,20,00,000 = 12,000,000. That is 12 million, since 1 million = 10,00,000 (10 lakh).'),
    dict(ch='1', scen='smallest multiplier making 252 a multiple of 360',
         stem='What is the smallest whole number by which 252 must be multiplied so that the product is a multiple of 360?',
         opts=['10', '5', '2', '30'],
         hint='Compare the prime factorisations of 252 and 360.',
         sol='252 = 2 × 2 × 3 × 3 × 7 and 360 = 2 × 2 × 2 × 3 × 3 × 5. 252 is missing one 2 and one 5, so multiply by 2 × 5 = 10. Check: 2,520 = 360 × 7.'),
    dict(ch='1', scen='negative integers above −15 plus positive integers below 12',
         stem='Add all the negative integers greater than −15 and all the positive integers less than 12. What is the total?',
         opts=['−39', '−105', '39', '−171'],
         hint='The negatives are −14 to −1 and the positives are 1 to 11.',
         sol='−1 − 2 − … − 14 = −105. 1 + 2 + … + 11 = 66. Total −105 + 66 = −39.'),

    # ---------------- Part 2 · Operations
    dict(ch='2', scen='curly products of negatives minus curly quotient times −1',
         stem='What is the value of [{(−2) × (−3)} − {(−8) ÷ 2}] × (−1)?',
         opts=['−10', '10', '−2', '2'],
         hint='Watch the sign when you subtract a negative number.',
         sol='(−2) × (−3) = 6 and (−8) ÷ 2 = −4. 6 − (−4) = 10. 10 × (−1) = −10.'),
    dict(ch='2', scen='999 times 36 plus 36 using the distributive property',
         stem='Use number properties to find 999 × 36 + 36.',
         opts=['36,000', '35,964', '36,036', '35,000'],
         hint='Write 36 as 1 × 36.',
         sol='999 × 36 + 1 × 36 = (999 + 1) × 36 = 1,000 × 36 = 36,000.'),
    dict(ch='2', scen='temperature falling 4° an hour from 18° at 6 PM to −10°',
         stem='At 6 PM the temperature in a hill town is 18°C. It falls by 4°C every hour. At what time does it reach −10°C?',
         opts=['1 AM', '12 midnight', '2 AM', '11 PM'],
         hint='Find the total fall from 18°C to −10°C.',
         sol='The fall is 18 − (−10) = 28°C. 28 ÷ 4 = 7 hours. 6 PM + 7 hours = 1 AM.'),

    # ---------------- Part 3 · Fractions, Decimals & Percentages
    dict(ch='3', scen='third largest of 4/5 0.83 79% 41/50',
         stem='Write these in order from largest to smallest: 4/5, 0.83, 79%, 41/50. Which is third?',
         opts=['4/5', '41/50', '79%', '0.83'],
         hint='Change everything into hundredths.',
         sol='4/5 = 0.80, 0.83, 79% = 0.79 and 41/50 = 0.82. Largest first: 0.83, 0.82, 0.80, 0.79. The third is 4/5.'),
    dict(ch='3', scen='number increased by 20% gives 90 · 20% less than the number',
         stem='When a number is increased by 20%, the result is 90. What is 20% LESS than the original number?',
         opts=['60', '72', '70', '54'],
         hint='120% of the number is 90.',
         sol='120% of the number = 90, so 1% = 0.75 and the number is 75. 20% less than 75 is 75 − 15 = 60. (72 wrongly takes 20% off 90.)'),
    dict(ch='3', scen='20% of A equals 25% of B · B is 64',
         stem='20% of Arjun\'s marks is equal to 25% of Bela\'s marks. Bela scored 64. What did Arjun score?',
         opts=['80', '51.2', '60', '70'],
         hint='Find 25% of 64 first.',
         sol='25% of 64 = 16. So 20% of Arjun\'s marks is 16, and 1% is 0.8. Arjun scored 80.'),

    # ---------------- Part 4 · Algebra
    dict(ch='4', scen='x notebooks at y plus 5 and 3 pens at y · x 4 y 15',
         stem='Notebooks cost ₹(y + 5) each and pens cost ₹y each. Divya buys x notebooks and 3 pens. Write her total cost and find it when x = 4 and y = 15.',
         opts=['x(y + 5) + 3y; ₹125', 'x(y + 5) + 3y; ₹105', 'xy + 5 + 3y; ₹110', '(x + 3)(y + 5); ₹140'],
         hint='Each notebook costs (y + 5), so x notebooks cost x(y + 5).',
         sol='Total = x(y + 5) + 3y. At x = 4, y = 15: 4 × 20 + 3 × 15 = 80 + 45 = ₹125.'),
    dict(ch='4', scen='three consecutive even numbers from 2n with sum 78',
         stem='Three consecutive even numbers are 2n, 2n + 2 and 2n + 4. Their sum is 78. What is n?',
         opts=['12', '13', '24', '26'],
         hint='Add the three expressions first.',
         sol='2n + (2n + 2) + (2n + 4) = 6n + 6 = 78, so 6n = 72 and n = 12. The numbers are 24, 26, 28. (24 is the smallest number, not n.)'),

    # ---------------- Part 5 · Geometry
    dict(ch='5', scen='facing north turning 135 clockwise then 270 anticlockwise',
         stem='Riya faces north. She turns 135° clockwise and then 270° anticlockwise. In which direction does she face now?',
         opts=['South-west', 'North-east', 'South-east', 'North-west'],
         hint='Combine the two turns into one turn.',
         sol='135° clockwise then 270° anticlockwise is the same as 135° anticlockwise. From north, 90° anticlockwise is west and 45° more is south-west.'),
    dict(ch='5', scen='which set of lengths can form a triangle',
         stem='Which set of lengths (in cm) can be the three sides of a triangle?',
         opts=['5, 7, 11', '4, 5, 10', '3, 6, 9', '2, 8, 5'],
         hint='The two shorter sides together must be longer than the longest side.',
         sol='5 + 7 = 12 > 11, so this works. 4 + 5 = 9 < 10, 3 + 6 = 9 is not more than 9 (the sides would lie flat), and 2 + 5 = 7 < 8.'),
    dict(ch='5', scen='regular hexagon cut by its three longest diagonals',
         stem='A regular hexagon is cut along its three longest diagonals, which all pass through its centre. What pieces does this make?',
         opts=['6 equilateral triangles', '6 right-angled triangles', '3 equilateral triangles', '6 scalene triangles'],
         hint='Each angle at the centre is 360° ÷ 6.',
         sol='The three diagonals make 6 triangles meeting at the centre, each with a 60° angle there. Each triangle has two equal sides (centre to corner), so its other two angles are (180° − 60°) ÷ 2 = 60°. All 6 are equilateral.'),

    # ---------------- Part 6 · Mensuration
    dict(ch='6', scen='5 m path around the outside of a 50 m square park',
         stem='A square park has side 50 m. A path 5 m wide runs all round the outside of it. What is the area of the path?',
         opts=['1,100 m²', '1,000 m²', '500 m²', '1,200 m²'],
         hint='The outer square has side 50 + 5 + 5.',
         sol='Outer square: 60 × 60 = 3,600 m². Park: 50 × 50 = 2,500 m². Path: 3,600 − 2,500 = 1,100 m². (1,000 forgets the four corner squares.)'),
    dict(ch='6', scen='5 cm cube cut into two cuboids · increase in surface area',
         stem='A cube of edge 5 cm is cut into two cuboids by one straight cut parallel to a face. By how much does the total surface area increase?',
         opts=['50 cm²', '25 cm²', '0 cm²', '150 cm²'],
         hint='The cut makes new faces. How many, and how big?',
         sol='The cut creates two new faces, each 5 × 5 = 25 cm². The surface area increases by 50 cm², wherever the cut is made.'),
    dict(ch='6', scen='bricks 20 by 10 by 5 cm for a wall 10 m by 30 cm by 2 m',
         stem='How many bricks of 20 cm × 10 cm × 5 cm are needed for a wall 10 m long, 30 cm thick and 2 m high? (Ignore cement.)',
         opts=['6,000', '600', '60,000', '3,000'],
         hint='Change the wall\'s measurements into centimetres.',
         sol='Wall: 1,000 × 30 × 200 = 60,00,000 cm³. Brick: 20 × 10 × 5 = 1,000 cm³. Bricks: 60,00,000 ÷ 1,000 = 6,000.'),

    # ---------------- Part 7 · Data Handling
    dict(ch='8', scen='museum visitors bar graph · Saturday against Thursday and Wednesday',
         fig=drawing(330, 210, bars([('Tue', 90), ('Wed', 150), ('Thu', 60), ('Fri', 120), ('Sat', 180)], 200, 20, 'Museum visitors')),
         stem='The bar graph shows the visitors to a museum. Saturday\'s visitors were how many times Thursday\'s, and how many more than Wednesday\'s?',
         opts=['3 times; 30 more', '2 times; 30 more', '3 times; 60 more', '4 times; 30 more'],
         hint='Read Thursday, Wednesday and Saturday carefully against the gridlines.',
         sol='Saturday 180, Thursday 60, Wednesday 150. 180 ÷ 60 = 3 times. 180 − 150 = 30 more.'),
    dict(ch='8', scen='ages of 30 players table · fraction older than 13 and younger than 16',
         fig=table(['Age (years)', '12', '13', '14', '15', '16'], [['Players', '4', '7', '10', '6', '3']], widths=[110, 50, 50, 50, 50, 50]),
         stem='The table shows the ages of the players in a sports camp. What fraction of the players are older than 13 but younger than 16?',
         opts=['8/15', '19/30', '1/3', '2/5'],
         hint='Only ages 14 and 15 count.',
         sol='Total players: 4 + 7 + 10 + 6 + 3 = 30. Ages 14 and 15: 10 + 6 = 16. 16/30 = 8/15.'),

    # ---------------- Part 8 · Applied Mathematics
    dict(ch='9', scen='walking 5 km/h and running 10 km/h · 25 km in 3 hours',
         stem='Vivek covers 25 km in 3 hours, partly walking at 5 km/h and partly running at 10 km/h. How far does he walk?',
         opts=['5 km', '10 km', '15 km', '20 km'],
         hint='If he ran all the way, 25 km would take 2.5 hours.',
         sol='Running all 25 km takes 2.5 h, half an hour short. Each km walked instead of run adds 1/5 − 1/10 = 1/10 h. He needs 1/2 h more, so he walks 5 km. Check: 5 km takes 1 h and 20 km run takes 2 h.'),
    dict(ch='9', scen='₹6,300 shared with ₹900 more for one · ratio',
         stem='₹6,300 is shared between Ira and Om so that Ira gets ₹900 more than Om. What is the ratio of Ira\'s share to Om\'s?',
         opts=['4 : 3', '3 : 2', '7 : 6', '5 : 4'],
         hint='Take away the extra ₹900 first and share the rest equally.',
         sol='6,300 − 900 = 5,400, shared equally gives ₹2,700 each. Ira has 2,700 + 900 = ₹3,600 and Om ₹2,700. 3,600 : 2,700 = 4 : 3.'),
    dict(ch='9', scen='450 g rice for 6 people · rice for 14',
         stem='A recipe uses 450 g of rice for 6 people. How much rice is needed for 14 people?',
         opts=['1,050 g', '1,000 g', '1,200 g', '900 g'],
         hint='Find the rice for one person first.',
         sol='One person needs 450 ÷ 6 = 75 g. 14 people need 14 × 75 = 1,050 g.'),

    # ---------------- Part 9 · Mathematical Reasoning
    dict(ch='10', scen='day of the week 100 days after Wednesday',
         stem='Today is Wednesday. Which day of the week will it be 100 days from today?',
         opts=['Friday', 'Thursday', 'Saturday', 'Wednesday'],
         hint='Every 7 days the day of the week repeats.',
         sol='100 = 7 × 14 + 2. After 14 full weeks it is Wednesday again; 2 more days gives Friday.'),
    dict(ch='10', scen='sum of four different odd numbers from 1 to 19',
         stem='Sameer chooses 4 different numbers from 1, 3, 5, …, 19. Which of these could be their sum?',
         opts=['40', '41', '35', '81'],
         hint='Is the sum of four odd numbers odd or even? How big can it be?',
         sol='Four odd numbers add to an even number, so 41 and 35 are impossible. The largest sum is 13 + 15 + 17 + 19 = 64, so 81 is impossible. 40 works: 1 + 5 + 15 + 19 = 40.'),
    dict(ch='10', scen='add 5 multiply by 4 subtract 8 divide by 6 gives 10',
         stem='Lata thinks of a number. She adds 5, multiplies by 4, subtracts 8 and divides by 6. The answer is 10. What was her number?',
         opts=['12', '17', '8', '15'],
         hint='Undo each step, starting from the last.',
         sol='10 × 6 = 60. 60 + 8 = 68. 68 ÷ 4 = 17. 17 − 5 = 12.'),

    # ---------------- Mixed Problems
    dict(ch='4+10', scen='pattern 3 8 15 24 35 with nth term n times n plus 2',
         fig=cards([3, 8, 15, 24, 35, '…'], size=40),
         stem='The nth number of this pattern is n × (n + 2). What is the 10th number?',
         opts=['120', '99', '110', '143'],
         hint='Check the rule with n = 1 and n = 2 first.',
         sol='n = 1: 1 × 3 = 3. n = 2: 2 × 4 = 8. ✓ The 10th number is 10 × 12 = 120.'),
    dict(ch='1+10', scen='smallest number leaving remainders 4 6 8 on division by 6 8 10',
         stem='What is the smallest number that leaves remainder 4 when divided by 6, remainder 6 when divided by 8, and remainder 8 when divided by 10?',
         opts=['118', '122', '238', '120'],
         hint='In each case the remainder is 2 less than the divisor.',
         sol='Adding 2 to the number makes it divisible by 6, 8 and 10. LCM of 6, 8 and 10 is 120, so the number is 120 − 2 = 118. Check: 118 = 6 × 19 + 4 = 8 × 14 + 6 = 10 × 11 + 8.'),
    dict(ch='3+9', scen='train slowing from 80 to 60 km/h · percent increase in time',
         stem='A train usually runs at 80 km/h. Because of repairs it runs at 60 km/h. By what percentage does the time for a 240 km journey increase?',
         opts=['33 1/3%', '25%', '20%', '40%'],
         hint='Find the two journey times.',
         sol='At 80 km/h: 3 hours. At 60 km/h: 4 hours. The time increases by 1 hour out of 3, which is 33 1/3%. (25% is the fall in speed.)'),
    dict(ch='5+6', scen='painted 6 cm cube cut into 1 cm cubes · exactly one painted face',
         stem='A 6 cm wooden cube is painted on all faces and cut into 1 cm cubes. How many small cubes have paint on exactly one face?',
         opts=['96', '144', '64', '56'],
         hint='On each face, the cubes along the edges have more than one painted face.',
         sol='On each face, the inner 4 × 4 = 16 cubes have only that face painted. 6 faces × 16 = 96.'),
    dict(ch='4+9', scen='brother r and sister 4 younger · ages in 6 years total 48',
         stem='Rahul is r years old and his sister is 4 years younger. In 6 years their ages will add up to 48. What is r?',
         opts=['20', '18', '22', '24'],
         hint='Write both ages in 6 years as expressions.',
         sol='In 6 years: (r + 6) + (r − 4 + 6) = 2r + 8 = 48, so 2r = 40 and r = 20.'),
]
