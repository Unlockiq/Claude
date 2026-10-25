# AMO Level-2 · Class 9 · Practice Paper 1
# Each question: ch (chapter or pair of chapters), scen (unique scenario key), stem, opts (correct answer FIRST),
# hint, sol, optional fig. fixed=True keeps the option order, with ans = index of the correct option.
import math


def circle_pts(r, pts, chords=(), radii=(), labels=(), centre='O'):
    """Circle with centre O at (90, 90). pts: {name: angle in degrees, screen coords (0 = right, 90 = down)}."""
    O = (90, 90)
    P = {k: (O[0] + r * math.cos(math.radians(a)), O[1] + r * math.sin(math.radians(a))) for k, a in pts.items()}
    prims = [('circle', O[0], O[1], r, None), ('dot', O[0], O[1], 3), ('text', O[0] + 10, O[1] + 4, centre, 12)]
    for a, b in chords:
        prims.append(('line', P[a][0], P[a][1], P[b][0], P[b][1]))
    for a in radii:
        prims.append(('line', O[0], O[1], P[a][0], P[a][1]))
    for k, a in pts.items():
        x, y = P[k]
        dx, dy = math.cos(math.radians(a)), math.sin(math.radians(a))
        prims += [('dot', x, y, 3), ('text', x + 14 * dx, y + 14 * dy, k, 12)]
    for s, x, y in labels:
        prims.append(('text', x, y, s, 11))
    return prims


QUESTIONS = [
    # ---------------- Part 1 · Number System
    dict(ch='1', scen='100th digit after the decimal point of 1/7',
         stem='Shreya writes 1/7 as a decimal. What is the 100th digit after the decimal point?',
         opts=['8', '5', '4', '2'],
         hint='1/7 = 0.142857142857… The block of 6 digits repeats.',
         sol='1/7 = 0.142857 recurring, a block of 6 digits. 100 = 16 × 6 + 4, so the 100th digit is the 4th digit of the block, which is 8.'),
    dict(ch='1', scen='which of four surd products is irrational',
         stem='Which of these numbers is irrational?',
         opts=['√5 × √20 ÷ √10', '√2 × √8', '(√3 + 1)² − 2√3', '√0.09'],
         hint='Simplify each one before deciding.',
         sol='√2 × √8 = √16 = 4. (√3 + 1)² − 2√3 = 3 + 2√3 + 1 − 2√3 = 4. √0.09 = 0.3. √5 × √20 = √100 = 10, and 10 ÷ √10 = √10, which is irrational.'),

    # ---------------- Part 2 · Fractions, Decimals & Percentages
    dict(ch='3', scen='bus fare raised 20 then cut 20 then raised 10 percent',
         stem='A bus fare of ₹250 is raised by 20%, then cut by 20%, and later raised by 10%. What is the final fare?',
         opts=['₹264', '₹275', '₹250', '₹262.50'],
         hint='Each change multiplies the fare: × 1.2, × 0.8, × 1.1.',
         sol='250 × 1.2 × 0.8 × 1.1 = 250 × 1.056 = ₹264. A 20% rise followed by a 20% cut does not cancel: 1.2 × 0.8 = 0.96.'),
    dict(ch='3', scen='rice at ₹40 and ₹55 a kg blended to ₹46 a kg',
         stem='Meera mixes 12 kg of rice costing ₹40 per kg with some rice costing ₹55 per kg. The mixture is worth ₹46 per kg. How many kg of the ₹55 rice does she use?',
         opts=['8 kg', '6 kg', '10 kg', '12 kg'],
         hint='Each kg of cheap rice is ₹6 below the mix price; each kg of costly rice is ₹9 above it.',
         sol='The cheap rice is 12 × (46 − 40) = ₹72 below the mix value in total. Each kg of ₹55 rice is ₹9 above. So 9x = 72 and x = 8 kg. Check: 12 × 40 + 8 × 55 = 920 = 20 × 46.'),

    # ---------------- Part 3 · Algebra
    dict(ch='4', scen='x plus 1/x equals 4 · x cubed plus 1/x cubed',
         stem='If x + 1/x = 4, what is x³ + 1/x³?',
         opts=['52', '64', '76', '60'],
         hint='Cube both sides of x + 1/x = 4.',
         sol='(x + 1/x)³ = x³ + 1/x³ + 3(x + 1/x). So 64 = x³ + 1/x³ + 12, giving x³ + 1/x³ = 52.'),
    dict(ch='4', scen='(x−y)³ + (y−z)³ + (z−x)³ for x 7 y 4 z 2',
         stem='Kunal must find (x − y)³ + (y − z)³ + (z − x)³ when x = 7, y = 4 and z = 2, without cubing large numbers. What is the value?',
         opts=['−90', '90', '0', '−30'],
         hint='The three brackets add up to 0. Use a³ + b³ + c³ = 3abc when a + b + c = 0.',
         sol='Let a = x − y = 3, b = y − z = 2, c = z − x = −5. Then a + b + c = 0, so a³ + b³ + c³ = 3abc = 3 × 3 × 2 × (−5) = −90. Check: 27 + 8 − 125 = −90.'),
    dict(ch='4', scen='value of k for no solution of 2x+3y=7 and 6x+ky=20',
         stem='For which value of k do the equations 2x + 3y = 7 and 6x + ky = 20 have no solution?',
         opts=['9', '6', '3', '21'],
         hint='No solution means the lines are parallel but different.',
         sol='Parallel lines need 2/6 = 3/k, so k = 9. Then the constants give 7/20, which is not 1/3, so the lines are different. With k = 9 there is no solution.'),
    dict(ch='4', scen='AP with 5th term 17 and 12th term 45 · term equal to 97',
         stem='In an arithmetic progression, the 5th term is 17 and the 12th term is 45. Which term is 97?',
         opts=['25th', '24th', '26th', '23rd'],
         hint='Seven steps of the common difference take 17 to 45.',
         sol='7d = 45 − 17 = 28, so d = 4. The 1st term is 17 − 4 × 4 = 1, so the nth term is 4n − 3. 4n − 3 = 97 gives n = 25.'),

    # ---------------- Part 4 · Geometry
    dict(ch='5', scen='value of k for collinear points (1,2) (4,k) (10,8)',
         stem='The points (1, 2), (4, k) and (10, 8) lie on one straight line. What is k?',
         opts=['4', '5', '3', '6'],
         hint='Moving 9 units right from (1, 2) raises the line by 6 units.',
         sol='From (1, 2) to (10, 8) the line rises 6 in 9 steps, that is 2/3 per unit. From x = 1 to x = 4 is 3 units, a rise of 2. So k = 2 + 2 = 4.'),
    dict(ch='5', scen='parallel chords 24 and 10 on the same side of the centre radius 13',
         stem='A circle has radius 13 cm. Two parallel chords of lengths 24 cm and 10 cm lie on the same side of the centre. How far apart are the chords?',
         opts=['7 cm', '17 cm', '14 cm', '5 cm'],
         hint='The perpendicular from the centre bisects each chord.',
         sol='For the 24 cm chord: distance² = 13² − 12² = 25, so 5 cm. For the 10 cm chord: 13² − 5² = 144, so 12 cm. On the same side they are 12 − 5 = 7 cm apart. (17 cm is for opposite sides.)'),
    dict(ch='5', scen='angle at C on the minor arc when angle AOB is 110',
         fig=drawing(180, 180, circle_pts(62, {'A': 215, 'B': 325, 'C': 270}, chords=(('C', 'A'), ('C', 'B')), radii=('A', 'B'),
                                          labels=(('110°', 90, 74),))),
         stem='O is the centre of the circle and angle AOB = 110°. C is a point on the minor arc AB. What is angle ACB?',
         opts=['125°', '55°', '110°', '70°'],
         hint='The angle at the centre on the other side (the reflex angle AOB) is 360° − 110°.',
         sol='C is on the minor arc, so angle ACB is half of the reflex angle AOB: (360° − 110°) ÷ 2 = 125°. (55° is the angle at a point on the major arc.)'),
    dict(ch='5', scen='distance from vertex (5,10) to the centroid',
         stem='A triangle has vertices (2, 3), (8, 5) and (5, 10). How far is the vertex (5, 10) from the centroid?',
         opts=['4', '6', '2', '5'],
         hint='The centroid is the average of the three vertices.',
         sol='Centroid = ((2 + 8 + 5)/3, (3 + 5 + 10)/3) = (5, 6). The distance from (5, 10) to (5, 6) is 4. (It is 2/3 of the median from (5, 10), which has length 6.)'),

    # ---------------- Part 5 · Mensuration
    dict(ch='6', scen='altitude to the side 14 of a 13 14 15 triangle',
         stem='A triangular plot has sides 13 m, 14 m and 15 m. What is the length of the altitude drawn to the 14 m side?',
         opts=['12 m', '11.2 m', '6 m', '24 m'],
         hint='Find the area with Heron\'s formula first.',
         sol='s = 21. Area = √(21 × 8 × 7 × 6) = √7056 = 84 m². Altitude = 2 × 84 ÷ 14 = 12 m. (11.2 m is the altitude to the 15 m side.)'),
    dict(ch='6', scen='cone with radius 7 and slant height 25 · volume',
         stem='A cone has base radius 7 cm and slant height 25 cm. What is its volume? (Take π = 22/7.)',
         opts=['1,232 cm³', '3,696 cm³', '1,540 cm³', '1,078 cm³'],
         hint='Find the height from the slant height first.',
         sol='h = √(25² − 7²) = √576 = 24 cm. Volume = ⅓ × 22/7 × 49 × 24 = 1,232 cm³. (3,696 forgets the ⅓; 1,540 uses the slant height.)'),
    dict(ch='6', scen='segment cut off by a 90 degree sector of radius 14',
         stem='A chord subtends a right angle at the centre of a circle of radius 14 cm. What is the area of the smaller segment it cuts off? (Take π = 22/7.)',
         opts=['56 cm²', '154 cm²', '98 cm²', '42 cm²'],
         hint='Segment = sector − triangle.',
         sol='Sector = 90/360 × 22/7 × 196 = 154 cm². Triangle = ½ × 14 × 14 = 98 cm². Segment = 154 − 98 = 56 cm².'),

    # ---------------- Part 6 · Data Handling, Statistics & Probability
    dict(ch='8', scen='values of x making mean equal median for 3 8 10 15 x',
         stem='The numbers 3, 8, 10, 15 and x have equal mean and median. What is the sum of all possible values of x?',
         opts=['27', '23', '14', '9'],
         hint='The median depends on where x sits in the order. Try x < 8, 8 ≤ x ≤ 10 and x > 10.',
         sol='Mean = (36 + x)/5. If x < 8 the median is 8: (36 + x)/5 = 8 gives x = 4 ✓. If 8 ≤ x ≤ 10 the median is x: 36 + x = 5x gives x = 9 ✓. If x > 10 the median is 10: x = 14 ✓. Sum = 4 + 9 + 14 = 27.'),
    dict(ch='8', scen='two dice · probability the sum is prime',
         stem='Isha rolls two fair dice. What is the probability that the sum of the two numbers is a prime number?',
         opts=['5/12', '1/2', '7/18', '1/3'],
         hint='List the ways to get 2, 3, 5, 7 and 11.',
         sol='Sum 2: 1 way, 3: 2 ways, 5: 4 ways, 7: 6 ways, 11: 2 ways. Total 15 of 36 outcomes, so 15/36 = 5/12.'),
    dict(ch='8', scen='mean of 50 numbers corrected after two misread values',
         stem='The mean of 50 numbers was found to be 30. Later it was seen that 45 had been read as 85 and 30 had been read as 3. What is the correct mean?',
         opts=['29.74', '30.26', '29.2', '30'],
         hint='Correct the total first, then divide.',
         sol='Wrong total = 50 × 30 = 1,500. Correct total = 1,500 − 85 − 3 + 45 + 30 = 1,487. Correct mean = 1,487 ÷ 50 = 29.74.'),

    # ---------------- Part 7 · Applied Mathematics
    dict(ch='9', scen='taxi fare linear model 5 km ₹130 and 12 km ₹270',
         stem='A taxi fare is a fixed charge plus a fixed amount per km. A 5 km ride costs ₹130 and a 12 km ride costs ₹270. What does a 20 km ride cost?',
         opts=['₹430', '₹400', '₹520', '₹460'],
         hint='The extra 7 km cost ₹140.',
         sol='Rate = (270 − 130) ÷ 7 = ₹20 per km. Fixed charge = 130 − 5 × 20 = ₹30. Fare for 20 km = 30 + 20 × 20 = ₹430. (₹520 forgets the fixed charge is paid once: 130 × 4.)'),
    dict(ch='9', scen='monthly saving starting ₹500 rising ₹100 · first month above ₹2,000',
         stem='Ravi saves ₹500 in the first month and ₹100 more each month than the month before. In which month does his saving for that month first go above ₹2,000?',
         opts=['17th', '16th', '15th', '20th'],
         hint='The saving in month n is 500 + 100(n − 1).',
         sol='500 + 100(n − 1) > 2,000 gives n − 1 > 15, so n > 16. In month 16 he saves exactly ₹2,000, which is not above. The first month above ₹2,000 is the 17th.'),
    dict(ch='9', scen='tank on the x-axis equidistant from houses (1,7) and (7,−1)',
         stem='Two houses are at A(1, 7) and B(7, −1) on a town map (units in km). A water tank must be on the x-axis and the same distance from both houses. Where is it?',
         opts=['(0, 0)', '(4, 3)', '(4, 0)', '(3, 0)'],
         hint='Let the tank be (x, 0) and equate the squared distances.',
         sol='(x − 1)² + 49 = (x − 7)² + 1. Expanding: x² − 2x + 50 = x² − 14x + 50, so 12x = 0 and x = 0. The tank is at (0, 0). (4, 3) is the midpoint of AB, which is not on the x-axis.'),

    # ---------------- Part 8 · Mathematical Reasoning
    dict(ch='10', scen='extra Tower of Hanoi moves going from 6 to 8 discs',
         stem='In the Tower of Hanoi, the least number of moves for n discs is 2ⁿ − 1. How many more moves are needed for 8 discs than for 6 discs?',
         opts=['192', '128', '64', '255'],
         hint='Work out both totals.',
         sol='6 discs: 2⁶ − 1 = 63 moves. 8 discs: 2⁸ − 1 = 255 moves. Difference = 255 − 63 = 192.'),
    dict(ch='10', scen='true statement whose converse is false',
         stem='Which statement is true, but its converse is false?',
         opts=['If a quadrilateral is a square, its diagonals are equal.', 'If a triangle has three equal sides, it has three equal angles.',
               'If a whole number n is even, then n² is even.', 'If a quadrilateral is a parallelogram, its diagonals bisect each other.'],
         hint='For each, swap the "if" and "then" parts and look for a counterexample.',
         sol='Converse of the first: "if the diagonals are equal, it is a square" is false — a rectangle has equal diagonals. The other three converses are true: equal angles give equal sides; n² even gives n even; diagonals bisecting each other give a parallelogram.'),
    dict(ch='10', scen='steps of the halve-or-3n+1 rule starting from 7',
         stem='Rule: if a number is even, halve it; if it is odd, multiply by 3 and add 1. Rohan starts at 7 and applies the rule until he reaches 1. How many steps does he take?',
         opts=['16', '17', '15', '11'],
         hint='Write the numbers in order: 7, 22, 11, …',
         sol='7 → 22 → 11 → 34 → 17 → 52 → 26 → 13 → 40 → 20 → 10 → 5 → 16 → 8 → 4 → 2 → 1. That is 16 steps.'),
    dict(ch='10', scen='sides of the Koch snowflake after three steps',
         stem='A Koch snowflake starts as a triangle with 3 sides. At each step, every side is replaced by 4 smaller sides. How many sides does it have after 3 steps?',
         opts=['192', '48', '768', '108'],
         hint='The number of sides is multiplied by 4 at each step.',
         sol='Sides: 3 → 12 → 48 → 192 after 3 steps. (48 is after 2 steps and 768 after 4.)'),

    # ---------------- Part 9 · Mixed Problems
    dict(ch='4+10', scen='recursive rule a(n+1) equals 2a(n) − 1 from 2 · 10th term',
         stem='A sequence starts with a₁ = 2 and follows the rule aₙ₊₁ = 2aₙ − 1. What is a₁₀?',
         opts=['513', '1,025', '512', '257'],
         hint='Write the first few terms and compare them with powers of 2.',
         sol='Terms: 2, 3, 5, 9, 17, 33, … Each term is one more than a power of 2: aₙ = 2ⁿ⁻¹ + 1. So a₁₀ = 2⁹ + 1 = 513.'),
    dict(ch='5+6', scen='altitude from A in triangle (1,1) (7,1) (4,5)',
         stem='A triangle has vertices A(1, 1), B(7, 1) and C(4, 5). What is the length of the altitude from A to the side BC?',
         opts=['4.8', '4', '6', '2.4'],
         hint='Find the area using AB as base, then use BC as base.',
         sol='With base AB = 6 and height 4 (from y = 1 to y = 5), area = 12. BC = √(3² + 4²) = 5. Altitude from A = 2 × 12 ÷ 5 = 4.8.'),
    dict(ch='4+5', scen='triangle cut off from the axes by the line through (1,3) and (4,9)',
         stem='A straight line y = ax + b passes through (1, 3) and (4, 9). What is the area of the triangle it makes with the two axes?',
         opts=['1/4', '1/2', '1', '2'],
         hint='Find the slope and the intercepts.',
         sol='Slope a = (9 − 3)/(4 − 1) = 2 and b = 3 − 2 = 1, so y = 2x + 1. It meets the y-axis at (0, 1) and the x-axis at (−1/2, 0). Area = ½ × 1/2 × 1 = 1/4.'),
    dict(ch='8+10', scen='three coin tosses · at least two heads in a row',
         stem='Tanya tosses a fair coin three times. What is the probability that she gets two or more heads one after another?',
         opts=['3/8', '1/2', '1/4', '5/8'],
         hint='List all 8 outcomes and pick those with HH in them.',
         sol='Outcomes with HH: HHH, HHT, THH. HTH has two heads but not in a row. So 3 of 8 outcomes: 3/8. (1/2 counts all outcomes with at least two heads.)'),
    dict(ch='3+9', scen='₹2,100 a year simple growth against 10% compound on ₹20,000',
         stem='Gauri can invest ₹20,000 in Plan A, which adds ₹2,100 each year, or in Plan B, which adds 10% of the current value each year. Which plan gives more after 2 years?',
         opts=['Both give ₹24,200', 'Plan B, by ₹200', 'Plan A, by ₹200', 'Plan B, by ₹100'],
         hint='Work out each plan year by year.',
         sol='Plan A: 20,000 + 2 × 2,100 = ₹24,200. Plan B: 20,000 × 1.1 × 1.1 = ₹24,200. They are equal: the extra ₹100 in Plan A each year matches the growth on growth in Plan B.'),
]
