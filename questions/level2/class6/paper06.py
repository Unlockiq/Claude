# AMO Level-2 · Class 6 · Practice Paper 6


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


def two_squares():
    s = 12
    return [('rect', 10, 10, 8 * s, 8 * s, 'yellow'), ('rect', 10 + 8 * s, 10 + 2 * s, 6 * s, 6 * s, 'green'),
            ('text', 10 + 4 * s, 22 + 8 * s, '8 cm', 11), ('text', 10 + 11 * s, 22 + 8 * s, '6 cm', 11)]


QUESTIONS = [
    # ---------------- Part 1 · Number System
    dict(ch='1', scen='how many 7-digit numbers there are',
         stem='How many 7-digit numbers are there in all?',
         opts=['90,00,000', '99,99,999', '89,99,999', '9,99,999'],
         hint='Count from the smallest 7-digit number to the largest, including both.',
         sol='The smallest is 10,00,000 and the largest is 99,99,999. Count = 99,99,999 − 10,00,000 + 1 = 90,00,000.'),
    dict(ch='1', scen='HCF 6 LCM 180 two-digit numbers differing by 6 · sum',
         stem='Two two-digit numbers have HCF 6 and LCM 180, and they differ by 6. What is their sum?',
         opts=['66', '78', '102', '72'],
         hint='Write the numbers as 6 × a and 6 × b, where a and b share no factor.',
         sol='HCF × LCM = 6 × 180 = 1,080 = (6a)(6b), so a × b = 30 with a and b sharing no factor: 1 and 30, 2 and 15, 3 and 10, or 5 and 6. The pairs are 6 and 180, 12 and 90, 18 and 60, 30 and 36. Only 30 and 36 are two-digit and differ by 6. Sum: 66.'),
    dict(ch='1', scen='lift from floor 12 down 15 up 7 down 9',
         stem='In a building, the ground floor is floor 0 and floors below it are −1, −2, and so on. A lift starts at floor 12, goes down 15 floors, up 7 floors and then down 9 floors. Where is it now?',
         opts=['Floor −5', 'Floor 3', 'Floor 5', 'Floor −3'],
         hint='Add the moves as integers: down is negative.',
         sol='12 − 15 + 7 − 9 = −5. The lift is at floor −5, the fifth floor below ground.'),

    # ---------------- Part 2 · Operations
    dict(ch='2', scen='64 over square bracket 16 minus 4 times 5 minus 3 minus 3 times −2',
         stem='What is the value of 64 ÷ [16 − {4 × (5 − 3)}] − 3 × (−2)?',
         opts=['14', '2', '−2', '26'],
         hint='Clear the brackets from the inside, then divide and multiply before subtracting.',
         sol='(5 − 3) = 2, 4 × 2 = 8, 16 − 8 = 8. 64 ÷ 8 = 8. 3 × (−2) = −6. 8 − (−6) = 14.'),
    dict(ch='2', scen='two integers with product −24 and sum 5 · their difference',
         stem='Two integers a and b have product −24 and sum 5, with a > b. What is a − b?',
         opts=['11', '5', '−11', '2'],
         hint='One is positive and one is negative. List the pairs with product −24.',
         sol='Pairs with product −24: 8 and −3 add to 5. ✓ So a = 8, b = −3 and a − b = 8 − (−3) = 11.'),
    dict(ch='2', scen='37 times 25 times 4 times 2 plus 63 times 200',
         stem='Use number properties to find 37 × 25 × 4 × 2 + 63 × 200.',
         opts=['20,000', '19,800', '12,600', '7,400'],
         hint='25 × 4 × 2 = 200.',
         sol='37 × 25 × 4 × 2 = 37 × 200. Then 37 × 200 + 63 × 200 = (37 + 63) × 200 = 100 × 200 = 20,000.'),

    # ---------------- Part 3 · Fractions, Decimals & Percentages
    dict(ch='3', scen='third largest of 0.08 of 525 7% of 650 1/12 of 492 and 3/8 of 104',
         stem='Arrange these from largest to smallest: 0.08 of 525, 7% of 650, 1/12 of 492, 3/8 of 104. Which is third?',
         opts=['1/12 of 492', '0.08 of 525', '7% of 650', '3/8 of 104'],
         hint='Work out each one as a number.',
         sol='0.08 × 525 = 42. 7% of 650 = 45.5. 492 ÷ 12 = 41. 3/8 of 104 = 39. In order: 45.5, 42, 41, 39. The third is 1/12 of 492.'),
    dict(ch='3', scen='winner with 58% winning by 1,920 votes · total votes',
         stem='In a school election between two candidates, the winner got 58% of the votes and won by 1,920 votes. How many votes were cast? (No vote was invalid.)',
         opts=['12,000', '11,000', '3,310', '16,000'],
         hint='The loser got 42%. The winning margin is the difference in percentages.',
         sol='Margin = 58% − 42% = 16% of the votes = 1,920. 1% = 120 votes, so 100% = 12,000.'),
    dict(ch='3', scen='stock with 40% sold then 50% of the rest · 90 left',
         stem='A shop sold 40% of its stock of school bags on Monday and half of the remaining bags on Tuesday. 90 bags were left. How many bags were there at first?',
         opts=['300', '225', '180', '450'],
         hint='After Monday 60% is left. Tuesday takes half of that.',
         sol='After Monday: 60% left. After Tuesday: half of 60% = 30% left = 90 bags. 1% = 3 bags, so the stock was 300.'),

    # ---------------- Part 4 · Algebra
    dict(ch='4', scen='3 apples cost a and 5 bananas cost b · 12 apples and 10 bananas',
         stem='3 apples cost ₹a and 5 bananas cost ₹b. Write the cost of 12 apples and 10 bananas, and find it when a = 60 and b = 40.',
         opts=['4a + 2b; ₹320', '12a + 10b; ₹1,120', '4a + 2b; ₹280', '3a + 5b; ₹380'],
         hint='12 apples are 4 lots of 3 apples.',
         sol='12 apples = 4 × ₹a and 10 bananas = 2 × ₹b. Cost = 4a + 2b. At a = 60, b = 40: 240 + 80 = ₹320.'),
    dict(ch='4', scen='5 minus 2 times x minus 3 plus x times x at x −1',
         stem='What is the value of 5 − 2(x − 3) + x × x when x = −1?',
         opts=['14', '12', '−2', '16'],
         hint='(x − 3) is −4 when x = −1.',
         sol='x − 3 = −4, so −2(x − 3) = 8. x × x = (−1) × (−1) = 1. Total 5 + 8 + 1 = 14.'),

    # ---------------- Part 5 · Geometry
    dict(ch='5', scen='turning clockwise from east to north · angle and type',
         stem='Kartik faces east and turns clockwise until he faces north. Through what angle does he turn, and what type of angle is it?',
         opts=['270°, reflex', '90°, right', '180°, straight', '225°, reflex'],
         hint='Clockwise from east goes to south first.',
         sol='East → south is 90°, south → west is 90°, west → north is 90°. Total 270°. It is more than 180°, so it is a reflex angle.'),
    dict(ch='5', scen='triangle with P equal to Q and R twice P · type',
         stem='In triangle PQR, angle P = angle Q and angle R = 2 × angle P. Which describes the triangle?',
         opts=['Right-angled and isosceles', 'Acute-angled and isosceles', 'Right-angled and scalene', 'Equilateral'],
         hint='The angles are P, P and 2P.',
         sol='P + P + 2P = 4P = 180°, so P = 45°. The angles are 45°, 45° and 90°: right-angled, and the two equal angles make it isosceles.'),
    dict(ch='5', scen='regular polygon with perimeter 96 and side 8 · diagonals',
         stem='A regular polygon has perimeter 96 cm and each side is 8 cm. How many diagonals does it have?',
         opts=['54', '12', '108', '48'],
         hint='Find the number of sides first.',
         sol='Sides: 96 ÷ 8 = 12. Diagonals: 12 × (12 − 3) ÷ 2 = 12 × 9 ÷ 2 = 54.'),

    # ---------------- Part 6 · Mensuration
    dict(ch='6', scen='squares of side 8 and 6 placed side by side · perimeter',
         fig=drawing(190, 120, two_squares()),
         stem='Squares of side 8 cm and 6 cm are placed side by side with their bottoms in line, as shown. What is the perimeter of the combined shape?',
         opts=['44 cm', '56 cm', '50 cm', '40 cm'],
         hint='Part of the touching edge is inside the shape.',
         sol='The two perimeters add to 32 + 24 = 56 cm. The 6 cm of touching edge is counted twice (once in each square) but is inside the shape, so subtract 2 × 6. Perimeter = 56 − 12 = 44 cm.'),
    dict(ch='6', scen='three equal stones raise water 30 to 33 cm · one taken out',
         stem='A tank with a base of 50 cm by 40 cm has water 30 cm deep. Three identical stones are dropped in and the water rises to 33 cm. One stone is then taken out. How deep is the water now?',
         opts=['32 cm', '31 cm', '32.5 cm', '30 cm'],
         hint='Find the volume of one stone first.',
         sol='The three stones raise the water 3 cm: 50 × 40 × 3 = 6,000 cm³, so one stone is 2,000 cm³. Taking one out lowers the water by 2,000 ÷ (50 × 40) = 1 cm. New depth: 33 − 1 = 32 cm.'),
    dict(ch='6', scen='5 m by 4 m floor · 1 m border of 25 cm tiles and centre of 50 cm tiles',
         stem='A floor 5 m long and 4 m wide has a border 1 m wide all round. The border is covered with square tiles of side 25 cm, and the inside with square tiles of side 50 cm. How many tiles are used in all?',
         opts=['248', '320', '224', '272'],
         hint='The inside part is 3 m by 2 m.',
         sol='Inside: 3 m × 2 m. 50 cm tiles: 6 along, 4 across, so 24 tiles. Border area: 20 − 6 = 14 m². One 25 cm tile covers 1/16 m², so the border takes 14 × 16 = 224 tiles. Total 24 + 224 = 248.'),

    # ---------------- Part 7 · Data Handling
    dict(ch='8', scen='trees planted by classes VI to X bar graph against a 250 target',
         fig=drawing(330, 210, bars([('VI', 45), ('VII', 60), ('VIII', 35), ('IX', 50), ('X', 30)], 70, 10, 'Trees planted by class')),
         stem='The bar graph shows the trees planted by five classes. The school\'s target was 250 trees. How many more trees were needed, and which class planted the most?',
         opts=['30; Class VII', '20; Class VII', '30; Class IX', '50; Class VII'],
         hint='Add all five bars.',
         sol='Total: 45 + 60 + 35 + 50 + 30 = 220. More needed: 250 − 220 = 30. Class VII planted the most (60).'),
    dict(ch='8', scen='Shimla temperatures table · range and days below zero',
         fig=table(['Day', 'Mon', 'Tue', 'Wed', 'Thu', 'Fri'], [['Temperature (°C)', '−2', '3', '−4', '1', '0']], widths=[130, 50, 50, 50, 50, 50]),
         stem='The table shows the lowest temperature in Shimla on five days. What is the difference between the warmest and the coldest of these, and on how many days was it below 0°C?',
         opts=['7°C; 2 days', '1°C; 2 days', '7°C; 3 days', '6°C; 2 days'],
         hint='0°C is not below 0°C.',
         sol='Warmest 3°C, coldest −4°C: difference 3 − (−4) = 7°C. Below 0°C: Monday and Wednesday, 2 days.'),

    # ---------------- Part 8 · Applied Mathematics
    dict(ch='9', scen='second car at 75 km/h catching the first at 50 km/h with a 2-hour head start',
         stem='A car leaves at 8 AM at 50 km/h. A second car leaves from the same place at 10 AM at 75 km/h along the same road. At what time does it catch up?',
         opts=['2 PM', '12 noon', '1 PM', '4 PM'],
         hint='By 10 AM the first car is 100 km ahead.',
         sol='At 10 AM the gap is 2 × 50 = 100 km. The gap closes by 75 − 50 = 25 km each hour, so it takes 100 ÷ 25 = 4 hours. 10 AM + 4 h = 2 PM.'),
    dict(ch='9', scen='rectangle with sides 5:3 and perimeter 64 · area',
         stem='The length and breadth of a rectangle are in the ratio 5 : 3, and its perimeter is 64 cm. What is its area?',
         opts=['240 cm²', '60 cm²', '256 cm²', '192 cm²'],
         hint='Length + breadth = half the perimeter.',
         sol='Length + breadth = 32 cm = 8 parts, so 1 part = 4 cm. Length 20 cm, breadth 12 cm. Area 240 cm².'),
    dict(ch='9', scen='tap filling 3/5 of a tank in 9 minutes · time for the rest',
         stem='A tap fills 3/5 of a tank in 9 minutes. How long will it take to fill the rest of the tank?',
         opts=['6 min', '15 min', '9 min', '5 min'],
         hint='Find the time for 1/5 of the tank.',
         sol='3/5 takes 9 minutes, so 1/5 takes 3 minutes. The rest is 2/5, which takes 6 minutes.'),

    # ---------------- Part 9 · Mathematical Reasoning
    dict(ch='10', scen='10 PM plus 75 hours',
         stem='It is 10 PM now. What time will it be exactly 75 hours later?',
         opts=['1 AM', '1 PM', '10 PM', '3 AM'],
         hint='75 hours = 3 days and some hours.',
         sol='75 = 3 × 24 + 3. After 3 days it is 10 PM again; 3 more hours gives 1 AM.'),
    dict(ch='10', scen='seven coins heads up flipping two at a time',
         stem='Seven coins lie heads up. In each move, Pallavi turns over exactly two coins. Can she ever make all seven coins show tails?',
         opts=['No, the number of heads always stays odd', 'Yes, in 4 moves', 'Yes, in 7 moves', 'No, because 7 is a prime number'],
         hint='How can one move change the number of heads?',
         sol='A move changes the number of heads by −2, 0 or +2, so it stays odd. It starts at 7 (odd) and can never reach 0 (even). So it is impossible.'),
    dict(ch='10', scen='1/3 on books and 1/4 of the rest on lunch · ₹150 left',
         stem='Meera spent 1/3 of her money on books and 1/4 of what was left on lunch. She had ₹150 left. How much did she have at first?',
         opts=['₹300', '₹250', '₹450', '₹360'],
         hint='The ₹150 is 3/4 of what was left after the books.',
         sol='₹150 is 3/4 of the money after books, so that money was ₹200. ₹200 is 2/3 of the start, so she started with ₹300.'),

    # ---------------- Mixed Problems
    dict(ch='4+10', scen='pattern 7 12 17 with nth term 5n plus 2 · which number belongs',
         fig=cards([7, 12, 17, 22, '…'], size=40),
         stem='The nth number of this pattern is 5n + 2. Which of these numbers is in the pattern: 247, 250, 256, 261?',
         opts=['247', '250', '256', '261'],
         hint='A number in the pattern is 2 more than a multiple of 5.',
         sol='247 − 2 = 245 = 5 × 49, so 247 is the 49th number. 250 − 2 = 248, 256 − 2 = 254 and 261 − 2 = 259 are not multiples of 5.'),
    dict(ch='1+10', scen='3-digit numbers whose digits multiply to 12',
         stem='How many 3-digit numbers have digits that multiply to give 12?',
         opts=['15', '12', '18', '9'],
         hint='Find the sets of three digits with product 12, then count their orders.',
         sol='Digit sets: {1, 2, 6} and {1, 3, 4}, each in 6 orders, and {2, 2, 3} in 3 orders. 6 + 6 + 3 = 15.'),
    dict(ch='3+9', scen='40% of 30 km at 12 km/h and the rest at 18 km/h',
         stem='Ashwin cycles 40% of a 30 km route at 12 km/h and the rest at 18 km/h. How long does the whole ride take?',
         opts=['2 h', '2 h 30 min', '1 h 40 min', '2 h 15 min'],
         hint='Find the two distances first.',
         sol='40% of 30 km = 12 km, taking 12 ÷ 12 = 1 h. The rest, 18 km, takes 18 ÷ 18 = 1 h. Total 2 h.'),
    dict(ch='5+6', scen='3 cm cube centred on a 5 cm cube · visible surface area',
         stem='A cube of edge 3 cm is glued on top of a cube of edge 5 cm, at its centre. The bottom of the large cube rests on a table. What is the total area of the faces exposed to the air (not touching the table or the other cube)?',
         opts=['161 cm²', '170 cm²', '152 cm²', '125 cm²'],
         hint='Leave out the table face and the 3 × 3 patch where the cubes meet.',
         sol='Large cube: 4 sides × 25 = 100, plus its top 25 − 9 = 16. Small cube: 4 sides × 9 = 36, plus its top 9. Total 100 + 16 + 36 + 9 = 161 cm².'),
    dict(ch='4+9', scen='₹x a day and ₹x plus 50 on Sundays · ₹15,200 in a month',
         stem='Chhaya earns ₹x each day, but ₹(x + 50) on Sundays. In a 30-day month with 4 Sundays she earns ₹15,200. What is x?',
         opts=['500', '506', '480', '520'],
         hint='Take away the Sunday extras first.',
         sol='The 4 Sundays pay 4 × ₹50 = ₹200 extra. Without the extras she would earn 15,200 − 200 = ₹15,000 in 30 days, so x = 15,000 ÷ 30 = 500.'),
]
