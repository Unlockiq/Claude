# AMO Level-2 · Class 8 · Practice Paper 9
# Each question: ch, scen (unique), stem, opts (correct FIRST), hint, sol, optional fig.


def pie(sectors, r=70, cx=150, cy=85):
    """Pie chart: sectors = [(label, degrees)] drawn clockwise from the top, labels outside."""
    import math
    prims, a = [], -90.0
    fills = ['blue', 'yellow', 'green', 'pink', 'lilac', 'peach']
    for i, (lab, deg) in enumerate(sectors):
        pts = [(cx, cy)] + [(cx + r * math.cos(math.radians(a + deg * k / 24)), cy + r * math.sin(math.radians(a + deg * k / 24))) for k in range(25)]
        prims.append(('poly', pts, fills[i % len(fills)]))
        mid = math.radians(a + deg / 2)
        prims.append(('text', cx + (r + 34) * math.cos(mid), cy + (r + 18) * math.sin(mid), f'{lab} {deg}°', 10))
        a += deg
    return prims


def sierp(n, x, y, s):
    h = s * 0.866
    if n == 0:
        return [('poly', [(x, y), (x - s / 2, y + h), (x + s / 2, y + h)], 'pink')]
    return sierp(n - 1, x, y, s / 2) + sierp(n - 1, x - s / 4, y + h / 2, s / 2) + sierp(n - 1, x + s / 4, y + h / 2, s / 2)


def sierp_steps():
    prims = []
    for k in range(3):
        cx = 50 + k * 120
        prims += [('poly', [(cx, 10), (cx - 45, 88), (cx + 45, 88)], 'white')] + sierp(k, cx, 10, 90)
        prims.append(('text', cx, 104, f'Step {k}', 11))
    return prims


QUESTIONS = [
    # ---------------- Part 1 · Number System
    dict(ch='1', scen='square field of area 30 and a quarter m² fenced with 4 rounds of wire',
         stem='A square field has an area of 30 1/4 m². It is fenced with 4 rounds of wire. How much wire is needed?',
         opts=['88 m', '22 m', '121 m', '44 m'],
         hint='30 1/4 = 121/4.',
         sol='Side = √(121/4) = 11/2 = 5.5 m. Perimeter = 22 m. Four rounds = 88 m.'),
    dict(ch='1', scen='sum of the first n cubes equals 441',
         stem='1³ + 2³ + 3³ = 36 = 6² and 1³ + 2³ + 3³ + 4³ = 100 = 10². For which n does 1³ + 2³ + … + n³ = 441?',
         opts=['6', '7', '21', '5'],
         hint='The sums are the squares of 1, 3, 6, 10, … = 1 + 2 + … + n.',
         sol='1³ + … + n³ = (1 + 2 + … + n)². 441 = 21², and 1 + 2 + … + 6 = 21. So n = 6.'),

    # ---------------- Part 2 · Operations
    dict(ch='2', scen='quarter inverse minus eighth inverse all inverted times 2 to the minus 3',
         stem='What is (4⁻¹ − 8⁻¹)⁻¹ × 2⁻³?',
         opts=['1', '8', '1/8', '64'],
         hint='4⁻¹ − 8⁻¹ = 1/4 − 1/8.',
         sol='1/4 − 1/8 = 1/8, so (1/8)⁻¹ = 8. 2⁻³ = 1/8. 8 × 1/8 = 1.'),
    dict(ch='2', scen='0.00000525 times 4 times 10 to the 5 divided by 7 times 10 to the minus 2',
         stem='Write (0.00000525 × 4 × 10⁵) ÷ (7 × 10⁻²) in standard form.',
         opts=['3 × 10¹', '3 × 10⁻¹', '3 × 10²', '2.1 × 10¹'],
         hint='0.00000525 = 5.25 × 10⁻⁶.',
         sol='5.25 × 10⁻⁶ × 4 × 10⁵ = 21 × 10⁻¹ = 2.1. 2.1 ÷ 0.07 = 30 = 3 × 10¹.'),

    # ---------------- Part 3 · Fractions, Decimals & Percentages
    dict(ch='3', scen='10 percent discount with 8 percent gain · gain at the marked price',
         stem='A trader gives a 10% discount on the marked price and still gains 8%. What would his gain percent be if he sold at the marked price?',
         opts=['20%', '18%', '10%', '8%'],
         hint='0.9 × marked price = 1.08 × cost.',
         sol='Marked price = 1.08 ÷ 0.9 × cost = 1.2 × cost. Selling at the marked price would give a 20% gain. (18% just adds 8 + 10.)'),
    dict(ch='3', scen='simple interest four ninths of the sum with rate equal to years',
         stem='The simple interest on a sum is 4/9 of the sum. The rate percent per year equals the number of years. What is the rate?',
         opts=['6 2/3%', '4%', '9%', '6%'],
         hint='Interest/sum = R × T ÷ 100 = R² ÷ 100.',
         sol='R² ÷ 100 = 4/9, so R² = 400/9 and R = 20/3 = 6 2/3%. (Also 6 2/3 years.)'),
    dict(ch='3', scen='40 litres of milk with 10 percent water · water to add for 20 percent',
         stem='40 litres of milk contain 10% water. How much water must be added so that water makes up 20% of the mixture?',
         opts=['5 L', '4 L', '8 L', '10 L'],
         hint='The amount of pure milk does not change.',
         sol='Pure milk = 36 L. In the new mixture this is 80%, so the total is 36 ÷ 0.8 = 45 L. Water to add = 45 − 40 = 5 L.'),

    # ---------------- Part 4 · Algebra
    dict(ch='4', scen='103 times 97 minus 99 squared',
         stem='Using identities, find 103 × 97 − 99².',
         opts=['190', '198', '200', '−190'],
         hint='103 × 97 = 100² − 3² and 99² = (100 − 1)².',
         sol='103 × 97 = 10,000 − 9 = 9,991. 99² = 10,000 − 200 + 1 = 9,801. Difference = 190.'),
    dict(ch='4', scen='x squared plus kx plus 18 with factor x plus 3 · k',
         stem='x + 3 is a factor of x² + kx + 18. What is k?',
         opts=['9', '6', '3', '21'],
         hint='The other factor is x + c with 3c = 18.',
         sol='x² + kx + 18 = (x + 3)(x + c) with 3c = 18, so c = 6. Then k = 3 + 6 = 9.'),
    dict(ch='4', scen='two-digit number 4 times its digit sum that reverses when 18 is added',
         stem='A two-digit number is 4 times the sum of its digits. When 18 is added to it, the digits are reversed. What is the number?',
         opts=['24', '42', '12', '36'],
         hint='10a + b = 4(a + b) gives b = 2a.',
         sol='10a + b = 4a + 4b gives 6a = 3b, so b = 2a. Reversing adds 9(b − a) = 18, so b − a = 2. Then a = 2, b = 4: the number is 24. Check: 24 + 18 = 42.'),

    # ---------------- Part 5 · Geometry
    dict(ch='5', scen='walking the diagonal of a 24 m by 10 m field · distance saved',
         stem='A rectangular field is 24 m long and 10 m wide. How much shorter is it to walk across the diagonal than along two sides from one corner to the opposite corner?',
         opts=['8 m', '26 m', '34 m', '10 m'],
         hint='Along two sides is 24 + 10 m.',
         sol='Diagonal = √(576 + 100) = 26 m. Along the sides: 34 m. Saving = 8 m.'),
    dict(ch='5', scen='rectangle with AB 9 and half-diagonal 7.5 · BC',
         stem='In rectangle ABCD, AB = 9 cm. The diagonals meet at O and OA = 7.5 cm. How long is BC?',
         opts=['12 cm', '6 cm', '7.5 cm', '15 cm'],
         hint='The diagonals of a rectangle bisect each other, so AC = 2 × OA.',
         sol='AC = 15 cm. In right triangle ABC, BC = √(15² − 9²) = √144 = 12 cm.'),
    dict(ch='5', scen='prism with 30 edges · number of faces',
         stem='A prism has 30 edges. How many faces does it have?',
         opts=['12', '10', '20', '32'],
         hint='A prism with an n-sided base has 3n edges.',
         sol='3n = 30, so the base is a 10-sided polygon. Faces = 2 bases + 10 side faces = 12. Check with Euler: V = 20, and 12 + 20 − 30 = 2.'),

    # ---------------- Part 6 · Mensuration
    dict(ch='6', scen='two cylinders with radii 2 to 3 and heights 5 to 3 · ratio of volumes',
         stem='Two cylinders have radii in the ratio 2 : 3 and heights in the ratio 5 : 3. What is the ratio of their volumes?',
         opts=['20 : 27', '10 : 9', '2 : 3', '4 : 9'],
         hint='Volume = πr²h, so the radius ratio is squared.',
         sol='Ratio = (2² × 5) : (3² × 3) = 20 : 27. (10 : 9 forgets to square the radii.)'),
    dict(ch='6', scen='cone radius 5 height 12 · total surface area with pi 3.14',
         stem='A solid cone has base radius 5 cm and height 12 cm. What is its total surface area? (Take π = 3.14.)',
         opts=['282.6 cm²', '204.1 cm²', '314 cm²', '188.4 cm²'],
         hint='Total surface = curved surface πrl + base πr².',
         sol='Slant height l = √(25 + 144) = 13 cm. Curved surface = 3.14 × 5 × 13 = 204.1 cm². Base = 3.14 × 25 = 78.5 cm². Total = 282.6 cm². (188.4 uses the height instead of l.)'),
    dict(ch='6', scen='half-full tank 8 m by 6 m by 2 m pumped out at 300 litres a minute',
         stem='A cuboid tank 8 m × 6 m × 2 m is half full of water. The water is pumped out at 300 litres per minute. How long does it take to empty the tank?',
         opts=['2 h 40 min', '5 h 20 min', '16 min', '1 h 36 min'],
         hint='Only half the tank\'s volume has to be pumped.',
         sol='Volume = 96 m³; half = 48 m³ = 48,000 litres. Time = 48,000 ÷ 300 = 160 minutes = 2 h 40 min.'),

    # ---------------- Part 7 · Data Handling
    dict(ch='8', scen='pie chart of 900 votes among three candidates · winning margin',
         fig=drawing(320, 180, pie([('A', 140), ('B', 100), ('C', 120)])),
         stem='The pie chart shows how 900 votes were shared among candidates A, B and C. By how many votes did A beat C?',
         opts=['50', '20', '150', '100'],
         hint='Each degree stands for 900 ÷ 360 votes.',
         sol='Each degree is 2.5 votes. A − C = 140° − 120° = 20°, which is 50 votes.'),
    dict(ch='8', scen='mean of 10 numbers 25 with each increased by 4 then doubled',
         stem='The mean of 10 numbers is 25. Each number is increased by 4 and the result is doubled. What is the new mean?',
         opts=['58', '54', '29', '50'],
         hint='The mean changes in the same way as every number.',
         sol='Adding 4 to every number makes the mean 29. Doubling every number makes it 58. (54 doubles first and then adds 4.)'),

    # ---------------- Part 8 · Applied Mathematics
    dict(ch='9', scen='eggs bought 5 for ₹16 and sold 4 for ₹16 with 30 of 600 broken',
         stem='A vendor buys 600 eggs at 5 for ₹16. Thirty eggs break, and he sells the rest at 4 for ₹16. What is his profit percent?',
         opts=['18.75%', '25%', '20%', '15%'],
         hint='Find the total cost and the total takings.',
         sol='Cost = 600 × 3.20 = ₹1,920. He sells 570 eggs at ₹4 each: ₹2,280. Profit = 360 on 1,920 = 18.75%. (25% ignores the broken eggs.)'),
    dict(ch='9', scen='₹10,000 at 6 percent for 3 years then 8 percent for 2 years simple interest',
         stem='₹10,000 is deposited at simple interest. The rate is 6% a year for the first 3 years and 8% a year for the next 2 years. What is the amount after 5 years?',
         opts=['₹13,400', '₹13,000', '₹14,000', '₹12,800'],
         hint='Simple interest is always on the original ₹10,000.',
         sol='Interest = 10,000 × (18% + 16%) = ₹3,400. Amount = ₹13,400.'),
    dict(ch='9', scen='phone sold at 20 percent profit · bought 10 percent cheaper and sold ₹180 less gives 25 percent',
         stem='Om sells a phone at a 20% profit. Had he bought it for 10% less and sold it for ₹180 less, his profit would have been 25%. What did the phone cost him?',
         opts=['₹2,400', '₹1,800', '₹3,000', '₹2,000'],
         hint='Compare 1.2 × cost with 1.25 × 0.9 × cost.',
         sol='Actual selling price = 1.2C. The other selling price = 1.25 × 0.9C = 1.125C. The difference 0.075C = ₹180, so C = ₹2,400.'),

    # ---------------- Part 9 · Mathematical Reasoning
    dict(ch='10', scen='TOO times 4 equals GOOD',
         stem='In TOO + TOO + TOO + TOO = GOOD, each letter stands for a different digit. What is GOOD?',
         opts=['1996', '1664', '1888', '1776'],
         hint='4 × TOO is a four-digit number, so G = 1, and 4 × O must end in D.',
         sol='G must be 1, so 4 × (100T + 11O) = 1000 + 110O + D, which gives 400T − 66O = 1000 + D, a number from 1000 to 1009. With T and O different, only T = 4, O = 9 works: 1600 − 594 = 1006, so D = 6. GOOD = 1996 (4 × 499).'),
    dict(ch='10', scen='three-digit numbers with strictly decreasing digits',
         stem='How many three-digit numbers have digits that strictly decrease from left to right (like 964 or 510)?',
         opts=['120', '84', '720', '100'],
         hint='Any three different digits can be arranged in decreasing order in exactly one way.',
         sol='Each choice of 3 different digits from 0–9 gives exactly one such number, and 0 can only come last, so it is never first. There are 10 × 9 × 8 ÷ 6 = 120 choices. (84 wrongly leaves out 0.)'),
    dict(ch='10', scen='numbers 1 to 1000 divisible by 7 but not by 11',
         stem='How many numbers from 1 to 1,000 are divisible by 7 but not by 11?',
         opts=['130', '142', '12', '131'],
         hint='Take away the multiples of 77.',
         sol='Multiples of 7: 1,000 ÷ 7 → 142. Multiples of both 7 and 11 are multiples of 77: 1,000 ÷ 77 → 12. Answer: 142 − 12 = 130.'),
    dict(ch='10', scen='Sierpinski triangle · number of removed triangles after step 3',
         fig=drawing(330, 110, sierp_steps()),
         stem='At each step, every shaded triangle is split into four equal triangles and the middle one is removed (left white). Steps 0, 1 and 2 are shown. How many white triangles of all sizes have been removed after step 3?',
         opts=['13', '27', '9', '12'],
         hint='Each step removes one triangle from every shaded triangle there was.',
         sol='Step 1 removes 1, step 2 removes 3 and step 3 removes 9. Total 1 + 3 + 9 = 13. (27 is the number of shaded triangles.)'),

    # ---------------- Part 10 · Mixed Problems
    dict(ch='4+10', scen='a plus b is 1 and ab is minus 2 · a to the fourth plus b to the fourth',
         stem='If a + b = 1 and ab = −2, what is a⁴ + b⁴?',
         opts=['17', '25', '21', '9'],
         hint='First find a² + b², then square it.',
         sol='a² + b² = (a + b)² − 2ab = 1 + 4 = 5. a⁴ + b⁴ = (a² + b²)² − 2a²b² = 25 − 8 = 17. (The numbers are 2 and −1.)'),
    dict(ch='5+10', scen='football of 12 pentagons and 20 hexagons · vertices',
         stem='A football is stitched from 12 pentagons and 20 hexagons, with every edge shared by two patches. Using Euler\'s formula, how many vertices does it have?',
         opts=['60', '90', '32', '120'],
         hint='Edges = (12 × 5 + 20 × 6) ÷ 2.',
         sol='Edges = (60 + 120) ÷ 2 = 90. Faces = 32. V = 2 − F + E = 2 − 32 + 90 = 60.'),
    dict(ch='4+5', scen='right triangle with sides x x plus 7 and x plus 9 · perimeter',
         stem='The sides of a right-angled triangle are x cm, (x + 7) cm and (x + 9) cm. What is its perimeter?',
         opts=['40 cm', '24 cm', '30 cm', '56 cm'],
         hint='The longest side is x + 9. Try whole-number values of x.',
         sol='x² + (x + 7)² = (x + 9)². Trying x = 8: 64 + 225 = 289 = 17². So the sides are 8, 15 and 17 cm, and the perimeter is 40 cm.'),
    dict(ch='3+9', scen='bought at 25 percent off list for ₹90 and sold at 10 percent off list',
         stem='A shopkeeper buys a toy for ₹90 after getting 25% off its list price. She sells it at 10% off the list price. What is her profit percent?',
         opts=['20%', '15%', '35%', '25%'],
         hint='First find the list price.',
         sol='List price = 90 ÷ 0.75 = ₹120. She sells at 120 × 0.9 = ₹108. Profit = 18 on 90 = 20%. (15% subtracts 10 from 25.)'),
    dict(ch='6+9', scen='lining an open cylindrical tank radius 7 m depth 4 m at ₹50 a m²',
         stem='The inside of an open cylindrical tank (walls and floor) is to be lined at ₹50 per m². The tank has radius 7 m and depth 4 m. What is the cost? (Take π = 22/7.)',
         opts=['₹16,500', '₹8,800', '₹24,200', '₹23,600'],
         hint='Area = curved surface + one circle (the tank is open at the top).',
         sol='Curved surface = 2 × 22/7 × 7 × 4 = 176 m². Floor = 22/7 × 49 = 154 m². Total 330 m² × ₹50 = ₹16,500. (₹24,200 also lines a top that does not exist.)'),
]
