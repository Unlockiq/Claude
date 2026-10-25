# AMO Level-2 · Class 8 · Practice Paper 3
# Each question: ch, scen (unique), stem, opts (correct FIRST), hint, sol, optional fig.


def freq_polygon(mids, freqs, top, step, xlab='', dx=50, h=150):
    """Frequency polygon: points at class mid-points joined by straight lines, closed to the axis."""
    x0, y0 = 40, 10
    X = lambda i: x0 + (i + 1) * dx
    Y = lambda f: y0 + h - f * h / top
    prims = []
    w = (len(mids) + 1) * dx
    for v in range(0, top + 1, step):
        prims += [('line', x0, Y(v), x0 + w, Y(v), True, (170, 170, 170), 0.8), ('text', x0 - 16, Y(v), str(v), 10)]
    pts = [(X(-1), Y(0))] + [(X(i), Y(f)) for i, f in enumerate(freqs)] + [(X(len(freqs)), Y(0))]
    prims.append(('polyline', pts))
    prims += [('dot', X(i), Y(f), 3.5) for i, f in enumerate(freqs)]
    labels = [mids[0] - (mids[1] - mids[0])] + list(mids) + [mids[-1] + (mids[1] - mids[0])]
    prims += [('text', X(i - 1), y0 + h + 13, str(m), 10) for i, m in enumerate(labels)]
    prims += [('line', x0, y0, x0, y0 + h), ('line', x0, y0 + h, x0 + w, y0 + h)]
    if xlab:
        prims.append(('text', x0 + w / 2, y0 + h + 30, xlab, 10))
    return prims


def koch_side(p, q, n):
    if n == 0:
        return [p]
    (x1, y1), (x2, y2) = p, q
    dx, dy = (x2 - x1) / 3, (y2 - y1) / 3
    a, b = (x1 + dx, y1 + dy), (x1 + 2 * dx, y1 + 2 * dy)
    c = (a[0] + dx * 0.5 + dy * 0.866, a[1] + dy * 0.5 - dx * 0.866)
    return koch_side(p, a, n - 1) + koch_side(a, c, n - 1) + koch_side(c, b, n - 1) + koch_side(b, q, n - 1)


def koch_steps():
    prims = []
    for k, cx in enumerate((60, 200)):
        s = 100
        A, B, C = (cx - s / 2, 90), (cx, 90 - s * 0.866), (cx + s / 2, 90)
        pts = koch_side(A, B, k) + koch_side(B, C, k) + koch_side(C, A, k) + [A]
        prims.append(('poly', pts, 'lilac'))
        prims.append(('text', cx, 125, f'Step {k}', 11))
    return prims


QUESTIONS = [
    # ---------------- Part 1 · Number System
    dict(ch='1', scen='two consecutive even numbers with product 288 · their sum',
         stem='The product of two consecutive even numbers is 288. What is their sum?',
         opts=['34', '36', '32', '30'],
         hint='The two numbers lie on either side of √288.',
         sol='√288 is a little less than 17 (17² = 289). The even numbers on either side are 16 and 18, and 16 × 18 = 288. Their sum is 34.'),
    dict(ch='1', scen='smallest divisor making 3,087 a perfect cube and its cube root',
         stem='Gita divides 3,087 by the smallest whole number that makes the result a perfect cube. What is that divisor, and what is the cube root of the result?',
         opts=['9 and 7', '3 and 7', '9 and 49', '7 and 9'],
         hint='Write 3,087 as a product of primes.',
         sol='3,087 = 3² × 7³. The 3² does not make a cube, so divide by 9: 3,087 ÷ 9 = 343 = 7³. The divisor is 9 and the cube root is 7.'),

    # ---------------- Part 2 · Operations
    dict(ch='2', scen='5 to the minus 1 times 25 squared cubed divided by 5 to the eighth',
         stem='Simplify (5⁻¹ × 25²)³ ÷ 5⁸.',
         opts=['5', '25', '1/5', '125'],
         hint='Write 25 as 5² and use the laws of exponents.',
         sol='5⁻¹ × 25² = 5⁻¹ × 5⁴ = 5³. (5³)³ = 5⁹. 5⁹ ÷ 5⁸ = 5.'),
    dict(ch='2', scen='mass of the Earth compared with the Moon in standard form',
         stem='The mass of the Earth is 5.97 × 10²⁴ kg and the mass of the Moon is 7.35 × 10²² kg. About how many times as heavy as the Moon is the Earth?',
         opts=['About 81', 'About 8', 'About 810', 'About 0.8'],
         hint='Divide the numbers and the powers of 10 separately.',
         sol='5.97 ÷ 7.35 ≈ 0.81 and 10²⁴ ÷ 10²² = 10². So the ratio is about 0.81 × 100 = 81.'),

    # ---------------- Part 3 · Fractions, Decimals & Percentages
    dict(ch='3', scen='phone at ₹9,600 after 20 percent off · marked price raised 10 percent then 25 percent off',
         stem='After a 20% discount, a phone sells for ₹9,600. Later the shop raises the marked price by 10% and offers a 25% discount instead. What is the new selling price?',
         opts=['₹9,900', '₹9,600', '₹10,560', '₹9,240'],
         hint='First find the original marked price.',
         sol='Marked price = 9,600 ÷ 0.8 = ₹12,000. New marked price = 12,000 × 1.1 = ₹13,200. New selling price = 13,200 × 0.75 = ₹9,900.'),
    dict(ch='3', scen='sum becomes 7 fifths of itself in 5 years · years to double',
         stem='At simple interest, a sum of money becomes 7/5 of itself in 5 years. In how many years will it become double itself?',
         opts=['12.5 years', '10 years', '15 years', '8 years'],
         hint='First find the interest as a fraction of the sum per year.',
         sol='The interest in 5 years is 2/5 of the sum, so the rate is (2/5 ÷ 5) × 100 = 8% a year. To double, the interest must be 100%: 100 ÷ 8 = 12.5 years.'),
    dict(ch='3', scen='sugar price up 25 percent and spending allowed to rise only 10 percent',
         stem='The price of sugar rises by 25%. A family wants its spending on sugar to rise by only 10%. By what percentage must it cut the amount of sugar it buys?',
         opts=['12%', '15%', '10%', '20%'],
         hint='New amount = new spending ÷ new price.',
         sol='New amount = 1.10 ÷ 1.25 = 0.88 of the old amount, so the family must buy 12% less. (15% just subtracts 25 − 10.)'),

    # ---------------- Part 4 · Algebra
    dict(ch='4', scen='factor of a squared minus b squared plus 2b minus 1',
         stem='Which of these is a factor of a² − b² + 2b − 1?',
         opts=['a + b − 1', 'a − b − 1', 'a + b + 1', 'a − 2b + 1'],
         hint='−b² + 2b − 1 = −(b − 1)².',
         sol='a² − b² + 2b − 1 = a² − (b − 1)² = (a − (b − 1))(a + (b − 1)) = (a − b + 1)(a + b − 1). So a + b − 1 is a factor.'),
    dict(ch='4', scen='x plus y squared 49 and x minus y squared 9 · x squared plus y squared plus xy',
         stem='If (x + y)² = 49 and (x − y)² = 9, what is x² + y² + xy?',
         opts=['39', '29', '49', '40'],
         hint='Add the two squares to get x² + y²; subtract them to get xy.',
         sol='Adding: 2(x² + y²) = 58, so x² + y² = 29. Subtracting: 4xy = 40, so xy = 10. x² + y² + xy = 39.'),
    dict(ch='4', scen='spent a third on books and a quarter of the rest on lunch with ₹300 left',
         stem='Ravi spent 1/3 of his money on books and then 1/4 of what was left on lunch. He had ₹300 left. How much money did he start with?',
         opts=['₹600', '₹720', '₹900', '₹480'],
         hint='After the books he had 2/3 of his money; after lunch, 3/4 of that.',
         sol='Let the money be x. After books: 2x/3. After lunch: 3/4 × 2x/3 = x/2. So x/2 = 300 and x = ₹600.'),

    # ---------------- Part 5 · Geometry
    dict(ch='5', scen='walk 7 north 6 east 9 north 6 east · straight distance back',
         stem='Mohan walks 7 m north, 6 m east, 9 m north and then 6 m east. How far is he now from his starting point in a straight line?',
         opts=['20 m', '28 m', '16 m', '25 m'],
         hint='Add all the northward parts and all the eastward parts.',
         sol='North: 7 + 9 = 16 m. East: 6 + 6 = 12 m. Distance = √(16² + 12²) = √400 = 20 m. (28 m is the total walked.)'),
    dict(ch='5', scen='line DE parallel to BC with AD 4 DB 6 DE 6 · BC',
         stem='In triangle ABC, D lies on AB and E lies on AC with DE parallel to BC. AD = 4 cm, DB = 6 cm and DE = 6 cm. How long is BC?',
         opts=['15 cm', '9 cm', '10 cm', '12 cm'],
         hint='Triangle ADE is similar to triangle ABC. Use AB, not DB.',
         sol='AB = 4 + 6 = 10 cm. Similar triangles give DE/BC = AD/AB = 4/10. So BC = 6 × 10/4 = 15 cm. (9 cm wrongly uses AD/DB.)'),
    dict(ch='5', scen='kite with sides 10 and 17 and short diagonal 16 · long diagonal',
         stem='Kite ABCD has AB = AD = 10 cm and CB = CD = 17 cm. The diagonal BD is 16 cm long. How long is the diagonal AC?',
         opts=['21 cm', '9 cm', '27 cm', '15 cm'],
         hint='In a kite, the diagonal AC cuts BD in half at right angles.',
         sol='AC meets BD at its midpoint M at right angles, so BM = 8 cm. AM = √(10² − 8²) = 6 cm and CM = √(17² − 8²) = 15 cm. AC = 6 + 15 = 21 cm.'),

    # ---------------- Part 6 · Mensuration
    dict(ch='6', scen='hollow pipe outer radius 7 inner 5 length 21 · volume of metal',
         stem='A metal pipe is 21 cm long. Its outer radius is 7 cm and its inner radius is 5 cm. What volume of metal is in the pipe? (Take π = 22/7.)',
         opts=['1,584 cm³', '3,234 cm³', '1,650 cm³', '528 cm³'],
         hint='Volume of metal = outer cylinder − inner cylinder = π(R² − r²)h.',
         sol='π(R² − r²)h = 22/7 × (49 − 25) × 21 = 22/7 × 24 × 21 = 1,584 cm³. (3,234 is the whole outer cylinder.)'),
    dict(ch='6', scen='cylinder with the same volume and radius as a cone of height 8 · height',
         stem='A cone has radius 6 cm and height 8 cm. A cylinder with the same radius has the same volume as the cone. What is the height of the cylinder?',
         opts=['8/3 cm', '8 cm', '24 cm', '4 cm'],
         hint='Volume of a cone = (1/3)πr²h.',
         sol='(1/3)π × 36 × 8 = π × 36 × H gives H = 8/3 cm. (24 cm multiplies by 3 instead of dividing.)'),
    dict(ch='6', scen='pool 20 m by 10 m sloping from 1 m to 3 m deep · litres',
         stem='A swimming pool is 20 m long and 10 m wide. Its floor slopes evenly from 1 m deep at one end to 3 m deep at the other. How many litres of water does it hold when full?',
         opts=['4 × 10⁵ L', '6 × 10⁵ L', '2 × 10⁵ L', '4 × 10⁴ L'],
         hint='With an even slope, use the average depth.',
         sol='Average depth = (1 + 3) ÷ 2 = 2 m. Volume = 20 × 10 × 2 = 400 m³ = 4,00,000 L = 4 × 10⁵ L.'),

    # ---------------- Part 7 · Data Handling
    dict(ch='8', scen='frequency polygon of ages of 40 people · number aged 30 or more',
         fig=drawing(380, 200, freq_polygon([15, 25, 35, 45, 55], [4, 9, 14, 8, 5], 16, 2, 'Age (years), class mid-points')),
         stem='The frequency polygon shows the ages of 40 people in classes 10–20, 20–30, 30–40, 40–50 and 50–60, plotted at the class mid-points. How many people are aged 30 or more?',
         opts=['27', '13', '22', '14'],
         hint='Mid-point 35 stands for the class 30–40.',
         sol='The classes from 30 upwards have mid-points 35, 45 and 55, with frequencies 14, 8 and 5. Total = 27.'),
    dict(ch='8', scen='mean of 20 observations corrected after 48 misread as 84',
         stem='The mean of 20 observations was found to be 35. Later it was found that one observation, 48, had been copied as 84. What is the correct mean?',
         opts=['33.2', '36.8', '35', '34.2'],
         hint='Correct the total first.',
         sol='Wrong total = 20 × 35 = 700. Correct total = 700 − 84 + 48 = 664. Correct mean = 664 ÷ 20 = 33.2.'),

    # ---------------- Part 8 · Applied Mathematics
    dict(ch='9', scen='buying 12 pens for ₹100 and selling 10 for ₹100',
         stem='A trader buys pens at 12 for ₹100 and sells them at 10 for ₹100. What is his gain percent?',
         opts=['20%', '16 2/3%', '2%', '25%'],
         hint='Compare the cost and selling price of the same number of pens, say 60.',
         sol='60 pens cost 5 × ₹100 = ₹500 and sell for 6 × ₹100 = ₹600. Gain = 100/500 = 20%.'),
    dict(ch='9', scen='scooter ₹60,000 with ₹20,000 down and 10 percent interest in 24 instalments',
         stem='A scooter costs ₹60,000. Nikhil pays ₹20,000 at once. The rest is charged simple interest at 10% a year for 2 years, and the total is paid in 24 equal monthly instalments. What is each instalment?',
         opts=['₹2,000', '₹1,667', '₹2,200', '₹1,800'],
         hint='Interest is charged only on the amount still owed.',
         sol='Amount owed = ₹40,000. Interest = 40,000 × 10% × 2 = ₹8,000. Total to repay = ₹48,000. Each instalment = 48,000 ÷ 24 = ₹2,000.'),
    dict(ch='9', scen='sold for ₹720 at 10 percent loss · price for 25 percent profit',
         stem='Selling a lamp for ₹720 causes a loss of 10%. At what price should it be sold to make a profit of 25%?',
         opts=['₹1,000', '₹900', '₹960', '₹1,080'],
         hint='₹720 is 90% of the cost price.',
         sol='Cost price = 720 ÷ 0.9 = ₹800. For 25% profit: 800 × 1.25 = ₹1,000.'),

    # ---------------- Part 9 · Mathematical Reasoning
    dict(ch='10', scen='AB times AB equals CAB',
         stem='In AB × AB = CAB, the letters A, B and C stand for different digits. What digit is C?',
         opts=['6', '5', '2', '7'],
         hint='The square of AB must end in the digits AB.',
         sol='A two-digit number whose square has three digits and ends in itself: 25² = 625 works (10² = 100 repeats a digit). So A = 2, B = 5 and C = 6.'),
    dict(ch='10', scen='four-digit numbers with strictly increasing digits ending in 6',
         stem='How many four-digit numbers have digits that strictly increase from left to right and end in 6?',
         opts=['10', '20', '15', '6'],
         hint='The first three digits are chosen from 1 to 5 and then arranged in increasing order.',
         sol='Choose 3 different digits from 1, 2, 3, 4, 5; they can go in only one order. Listing: 123, 124, 125, 134, 135, 145, 234, 235, 245, 345. That gives 10 numbers, such as 1236.'),
    dict(ch='10', scen='plus or minus signs before 1 to 10 · which total is possible',
         stem='Kavya puts a + or − sign in front of each of the numbers 1, 2, 3, …, 10 and adds them up. Which of these totals is possible?',
         opts=['7', '0', '2', '10'],
         hint='Changing one sign from + to − changes the total by an even number.',
         sol='With all signs +, the total is 55, which is odd. Changing the sign of n lowers the total by 2n, so the total stays odd. Only 7 is odd, and it can be made: put − in front of 10, 9, 4 and 1 (which add to 24), giving 55 − 48 = 7.'),
    dict(ch='10', scen='Koch snowflake perimeter after step 3 from side 27 cm',
         fig=drawing(270, 135, koch_steps()),
         stem='At each step, every side of the shape is split into three equal parts and a small equilateral triangle is built outward on the middle part, which is then removed. Steps 0 and 1 are shown. If each side at step 0 is 27 cm, what is the perimeter after step 3?',
         opts=['192 cm', '108 cm', '256 cm', '144 cm'],
         hint='Each step multiplies the number of sides by 4 and divides the side length by 3.',
         sol='Sides: 3 → 12 → 48 → 192. Side length: 27 → 9 → 3 → 1 cm. Perimeter after step 3 = 192 × 1 = 192 cm. (144 cm is the perimeter after step 2.)'),

    # ---------------- Part 10 · Mixed Problems
    dict(ch='4+10', scen='which of 7 11 13 17 divides 2 to the eighth minus 1',
         stem='Using a² − b², find which of these numbers divides 2⁸ − 1: 7, 11, 13 or 17.',
         opts=['17', '7', '11', '13'],
         hint='2⁸ − 1 = (2⁴)² − 1².',
         sol='2⁸ − 1 = (2⁴ − 1)(2⁴ + 1) = 15 × 17 = 255 = 3 × 5 × 17. Of the four numbers, only 17 divides it.'),
    dict(ch='5+10', scen='solid with 12 pentagon faces and three faces at each corner · vertices',
         stem='A solid has 12 faces, each a pentagon, and exactly three faces meet at every corner. How many vertices does it have?',
         opts=['20', '30', '12', '60'],
         hint='Count edges first: each edge is shared by two faces. Then use F + V − E = 2.',
         sol='Edges = 12 × 5 ÷ 2 = 30. V = 2 − F + E = 2 − 12 + 30 = 20. (Check: 20 corners × 3 faces = 60 = 12 × 5 face corners.)'),
    dict(ch='4+5', scen='two squares with sides adding to 17 and areas adding to 145 · difference of areas',
         stem='Two squares have sides a and b, with a + b = 17 cm. Their areas add up to 145 cm². What is the difference between their areas?',
         opts=['17 cm²', '1 cm²', '145 cm²', '72 cm²'],
         hint='Find ab from (a + b)², then (a − b)².',
         sol='(a + b)² = 289 = 145 + 2ab, so ab = 72. (a − b)² = 145 − 144 = 1, so a − b = 1. Difference of areas = a² − b² = (a + b)(a − b) = 17 cm².'),
    dict(ch='3+9', scen='₹10,000 at 10 percent for 3 years then the amount at 12 percent for 2 years',
         stem='Hema invests ₹10,000 at 10% simple interest for 3 years. She then invests the whole amount at 12% simple interest for 2 more years. How much does she have at the end?',
         opts=['₹16,120', '₹15,400', '₹16,000', '₹15,600'],
         hint='Find the amount after 3 years first. The second interest is on that amount.',
         sol='After 3 years: 10,000 + 30% = ₹13,000. The next 2 years add 24% of 13,000 = ₹3,120. Total ₹16,120. (15,400 wrongly takes the 24% on ₹10,000.)'),
    dict(ch='6+9', scen='painting 10 cylindrical pillars radius 35 cm height 4 m at ₹12.50 a square metre',
         stem='Ten cylindrical pillars, each of radius 35 cm and height 4 m, have their curved surfaces painted at ₹12.50 per m². What is the total cost? (Take π = 22/7.)',
         opts=['₹1,100', '₹110', '₹2,200', '₹1,155'],
         hint='Change 35 cm into metres before using 2πrh.',
         sol='Curved surface of one pillar = 2 × 22/7 × 0.35 × 4 = 8.8 m². Ten pillars: 88 m². Cost = 88 × 12.50 = ₹1,100.'),
]
