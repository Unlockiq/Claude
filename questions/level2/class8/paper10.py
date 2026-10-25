# AMO Level-2 · Class 8 · Practice Paper 10
# Each question: ch, scen (unique), stem, opts (correct FIRST), hint, sol, optional fig.


def hist(edges, freqs, top, step, xlab='', bw=46, h=150, ylab=''):
    """Histogram: adjacent bars over class intervals, y axis 0..top with gridlines every step."""
    x0, y0 = 40, 10
    w = len(freqs) * bw
    prims = []
    for v in range(0, top + 1, step):
        y = y0 + h - v * h / top
        prims += [('line', x0, y, x0 + w + 10, y, True, (170, 170, 170), 0.8), ('text', x0 - 16, y, str(v), 10)]
    for i, f in enumerate(freqs):
        x = x0 + i * bw
        prims.append(('rect', x, y0 + h - f * h / top, bw, f * h / top, 'lilac'))
        prims.append(('text', x + bw / 2, y0 + h - f * h / top - 8, str(f), 10))
    for i, e in enumerate(edges):
        prims.append(('text', x0 + i * bw, y0 + h + 13, str(e), 10))
    prims += [('line', x0, y0, x0, y0 + h), ('line', x0, y0 + h, x0 + w + 10, y0 + h)]
    if xlab:
        prims.append(('text', x0 + w / 2, y0 + h + 30, xlab, 10))
    if ylab:
        prims.append(('text', x0 + 50, y0 - 16, ylab, 10))
    return prims


def menger_face():
    """Front face of step 1 and step 2 of the Menger sponge."""
    prims = []
    for k, x0 in enumerate((10, 150)):
        s = 108
        prims.append(('rect', x0, 10, s, s, 'yellow'))
        prims.append(('rect', x0 + s / 3, 10 + s / 3, s / 3, s / 3, 'white'))
        if k == 1:
            for i in range(3):
                for j in range(3):
                    if (i, j) != (1, 1):
                        prims.append(('rect', x0 + i * s / 3 + s / 9, 10 + j * s / 3 + s / 9, s / 9, s / 9, 'white'))
        prims.append(('text', x0 + s / 2, 132, f'Step {k + 1} (front face)', 10))
    return prims


QUESTIONS = [
    # ---------------- Part 1 · Number System
    dict(ch='1', scen='nested square roots ending in root 225',
         stem='What is √(10 + √(25 + √(108 + √(154 + √225))))?',
         opts=['4', '16', '6', '2'],
         hint='Start from the innermost root and work outwards.',
         sol='√225 = 15. √(154 + 15) = √169 = 13. √(108 + 13) = √121 = 11. √(25 + 11) = √36 = 6. √(10 + 6) = √16 = 4.'),
    dict(ch='1', scen='cube of 729 cm³ cut into 27 equal cubes · growth in surface area',
         stem='A cube of volume 729 cm³ is cut into 27 equal small cubes. How many times the surface area of the big cube is the total surface area of all the small cubes?',
         opts=['3', '27', '9', '6'],
         hint='Find the edges: ∛729 and then one third of it.',
         sol='Big cube: edge 9 cm, surface 6 × 81 = 486 cm². Small cubes: edge 3 cm, each 6 × 9 = 54 cm², total 27 × 54 = 1,458 cm². 1,458 ÷ 486 = 3.'),

    # ---------------- Part 2 · Operations
    dict(ch='2', scen='three fifths to the x times five thirds to the 2x equals 125 over 27',
         stem='Find x if (3/5)ˣ × (5/3)²ˣ = 125/27.',
         opts=['3', '−3', '1', '2'],
         hint='(3/5)ˣ = (5/3)⁻ˣ.',
         sol='(3/5)ˣ × (5/3)²ˣ = (5/3)⁻ˣ⁺²ˣ = (5/3)ˣ. 125/27 = (5/3)³, so x = 3.'),
    dict(ch='2', scen='daily water use of 1.42 times 10 to the 9 people at 150 litres each',
         stem='About 1.42 × 10⁹ people each use about 1.5 × 10² litres of water a day. Roughly how much water is used in total each day?',
         opts=['2.13 × 10¹¹ L', '2.13 × 10¹⁸ L', '2.13 × 10⁹ L', '1.42 × 10¹¹ L'],
         hint='Multiply the numbers and add the powers of 10.',
         sol='1.42 × 1.5 = 2.13 and 10⁹ × 10² = 10¹¹. Total ≈ 2.13 × 10¹¹ litres. (10¹⁸ multiplies the powers instead of adding them.)'),

    # ---------------- Part 3 · Fractions, Decimals & Percentages
    dict(ch='3', scen='single discount equal to 10 20 and 30 percent in turn',
         stem='What single discount is the same as three successive discounts of 10%, 20% and 30%?',
         opts=['49.6%', '60%', '50.4%', '40%'],
         hint='Multiply 0.9 × 0.8 × 0.7.',
         sol='0.9 × 0.8 × 0.7 = 0.504, so the buyer pays 50.4% and the single discount is 49.6%.'),
    dict(ch='3', scen='₹7,500 at 12 percent for 3 years against 9 percent for 4 years',
         stem='What is the difference between the simple interest on ₹7,500 at 12% a year for 3 years and at 9% a year for 4 years?',
         opts=['₹0', '₹225', '₹2,700', '₹675'],
         hint='Compare the total percentages before calculating anything.',
         sol='12% × 3 = 36% and 9% × 4 = 36%. Both give the same interest (₹2,700), so the difference is ₹0.'),
    dict(ch='3', scen='salary after rent 25 percent food 30 percent of rest and saving 20 percent of remainder',
         stem='Priya spends 25% of her salary on rent and 30% of what is left on food. She saves 20% of the remaining amount, which is ₹3,150. What is her salary?',
         opts=['₹30,000', '₹21,000', '₹31,500', '₹15,000'],
         hint='After rent 0.75 is left; after food, 0.7 of that.',
         sol='After rent and food she has 0.75 × 0.7 = 0.525 of her salary. She saves 20% of this, which is 0.105 of her salary. 3,150 ÷ 0.105 = ₹30,000.'),

    # ---------------- Part 4 · Algebra
    dict(ch='4', scen='x plus 3 squared minus x minus 3 squared equals 60 · x squared minus 9',
         stem='If (x + 3)² − (x − 3)² = 60, what is x² − 9?',
         opts=['16', '25', '12', '34'],
         hint='Simplify the left side first.',
         sol='(x + 3)² − (x − 3)² = 12x = 60, so x = 5. x² − 9 = 25 − 9 = 16.'),
    dict(ch='4', scen='factorising a squared b squared minus 2ab minus 15',
         stem='Which is the correct factorisation of a²b² − 2ab − 15?',
         opts=['(ab − 5)(ab + 3)', '(ab + 5)(ab − 3)', '(ab − 15)(ab + 1)', '(a − 5)(b + 3)'],
         hint='Treat ab as a single quantity: find two numbers with product −15 and sum −2.',
         sol='With p = ab: p² − 2p − 15 = (p − 5)(p + 3). So the answer is (ab − 5)(ab + 3). Check at ab = 8: 64 − 16 − 15 = 33 = 3 × 11.'),
    dict(ch='4', scen='₹1,000 shared where B gets ₹100 more than A and C twice B · C share',
         stem='₹1,000 is shared among Ankit, Bela and Chirag. Bela gets ₹100 more than Ankit, and Chirag gets twice as much as Bela. How much does Chirag get?',
         opts=['₹550', '₹275', '₹175', '₹500'],
         hint='Let Ankit get ₹a. Then Bela gets a + 100 and Chirag 2(a + 100).',
         sol='a + (a + 100) + 2(a + 100) = 4a + 300 = 1,000, so a = 175. Bela gets ₹275 and Chirag ₹550.'),

    # ---------------- Part 5 · Geometry
    dict(ch='5', scen='equilateral triangle with height 6 root 3 · perimeter',
         stem='The height of an equilateral triangle is 6√3 cm. What is its perimeter?',
         opts=['36 cm', '18√3 cm', '54 cm', '24 cm'],
         hint='If the side is a, the height is √(a² − (a/2)²).',
         sol='Height = √(a² − a²/4) = (√3/2)a = 6√3, so a = 12 cm. Perimeter = 36 cm.'),
    dict(ch='5', scen='square with AP equal to BQ · angle between DP and AQ',
         stem='ABCD is a square. P lies on AB and Q lies on BC with AP = BQ. At what angle do the lines DP and AQ meet?',
         opts=['90°', '45°', '60°', 'It depends on where P is'],
         hint='Show that triangles DAP and ABQ are congruent.',
         sol='DA = AB, AP = BQ and the angles at A and B are both 90°, so triangles DAP and ABQ are congruent (SAS). So angle ADP = angle BAQ. Let DP and AQ meet at X. In triangle ADX, angle ADX + angle DAX = angle BAQ + (90° − angle BAQ) = 90°, so angle AXD = 90° wherever P is.'),
    dict(ch='5', scen='3 by 4 by 5 cuboid of unit cubes with the outer layer removed',
         stem='A cuboid 3 × 4 × 5 is built from unit cubes. The whole outer layer of cubes is removed. How many cubes are left?',
         opts=['6', '12', '24', '0'],
         hint='Removing the outer layer takes 2 off each dimension.',
         sol='The inner block is (3 − 2) × (4 − 2) × (5 − 2) = 1 × 2 × 3 = 6 cubes.'),

    # ---------------- Part 6 · Mensuration
    dict(ch='6', scen='cylinder with radius doubled and height halved · effect on volume and curved surface',
         stem='The radius of a cylinder is doubled and its height is halved. Which statement is true?',
         opts=['The volume doubles; the curved surface stays the same', 'The volume stays the same; the curved surface doubles', 'Both double', 'Both stay the same'],
         hint='Volume = πr²h and curved surface = 2πrh.',
         sol='Volume: (2r)² × h/2 = 2r²h, so it doubles. Curved surface: 2π × 2r × h/2 = 2πrh, unchanged.'),
    dict(ch='6', scen='largest cone carved from a cylinder radius 3 height 7 · wood removed',
         stem='The largest possible cone is carved out of a solid wooden cylinder of radius 3 cm and height 7 cm (same base and height). What volume of wood is cut away? (Take π = 22/7.)',
         opts=['132 cm³', '66 cm³', '198 cm³', '264 cm³'],
         hint='The cone keeps 1/3 of the cylinder; 2/3 is cut away.',
         sol='Cylinder = 22/7 × 9 × 7 = 198 cm³. Cone = 66 cm³. Wood cut away = 198 − 66 = 132 cm³.'),
    dict(ch='6', scen='pencil as a cylinder 14 cm long with a 1.2 cm cone tip radius 0.35',
         stem='A pencil is a cylinder 14 cm long with a cone 1.2 cm long at one end; both have radius 0.35 cm. What is its total volume? (Take π = 22/7.)',
         opts=['5.544 cm³', '5.39 cm³', '5.852 cm³', '5.698 cm³'],
         hint='Add the volume of the cylinder and one third of a cylinder for the tip.',
         sol='Cylinder = 22/7 × 0.1225 × 14 = 5.39 cm³. Cone = (1/3) × 22/7 × 0.1225 × 1.2 = 0.154 cm³. Total = 5.544 cm³. (5.852 forgets the 1/3.)'),

    # ---------------- Part 7 · Data Handling
    dict(ch='8', scen='histogram of hours spent on homework · percentage from 2 to under 4 hours',
         fig=drawing(300, 200, hist([0, 1, 2, 3, 4, 5], [5, 12, 18, 10, 5], 18, 3, 'Hours a week on a hobby', ylab='Number of students')),
         stem='The histogram shows how many hours a week students spend on a hobby (each class includes its lower value, not its upper value). What percentage of the students spend at least 2 hours but less than 4 hours?',
         opts=['56%', '28%', '66%', '46%'],
         hint='Total all the bars first.',
         sol='Total = 5 + 12 + 18 + 10 + 5 = 50. From 2 to under 4 hours: 18 + 10 = 28. 28 ÷ 50 = 56%.'),
    dict(ch='8', scen='seven numbers with one unknown and mean 9 · median and modes',
         stem='The mean of 4, 7, 9, x, 9, 10, 12 is 9. What are the median and the mode(s) of these seven numbers?',
         opts=['Median 9; modes 9 and 12', 'Median 10; mode 12', 'Median 9; mode 9', 'Median 9; mode 12'],
         hint='Find x from the total, then sort the numbers.',
         sol='Total = 63, so x = 63 − 51 = 12. In order: 4, 7, 9, 9, 10, 12, 12. Median = 9. Both 9 and 12 appear twice, so there are two modes.'),

    # ---------------- Part 8 · Applied Mathematics
    dict(ch='9', scen='profit 25 percent of selling price expressed on cost',
         stem='A merchant\'s profit is 25% of the selling price. What is the profit as a percentage of the cost price?',
         opts=['33 1/3%', '25%', '20%', '30%'],
         hint='Take the selling price as ₹100.',
         sol='Selling price ₹100, profit ₹25, so cost = ₹75. Profit on cost = 25/75 = 33 1/3%.'),
    dict(ch='9', scen='₹20,000 television with ₹4,000 down and ₹18,400 after a year · interest rate',
         stem='A television costs ₹20,000 in cash. On the instalment plan, a buyer pays ₹4,000 at once and ₹18,400 after one year. What rate of simple interest is being charged?',
         opts=['15%', '12%', '20%', '14.4%'],
         hint='Interest is charged only on the amount still owed after the down payment.',
         sol='Amount owed = ₹16,000. Interest = 18,400 − 16,000 = ₹2,400. Rate = 2,400 ÷ 16,000 × 100 = 15%. (12% wrongly divides by ₹20,000.)'),
    dict(ch='9', scen='₹800 article with ₹100 overheads sold at 12 percent profit plus 18 percent GST',
         stem='A shopkeeper buys an article for ₹800 and spends ₹100 on transport. He sells it at a 12% profit on his total cost, and the customer also pays 18% GST on that selling price. How much does the customer pay?',
         opts=['₹1,189.44', '₹1,008', '₹1,062', '₹1,132.80'],
         hint='Total cost = ₹900. Find the selling price, then add GST.',
         sol='Selling price = 900 × 1.12 = ₹1,008. With GST: 1,008 × 1.18 = ₹1,189.44. (₹1,132.80 forgets the ₹100.)'),

    # ---------------- Part 9 · Mathematical Reasoning
    dict(ch='10', scen='two-digit number times its reverse equals 2,268',
         stem='A two-digit number AB multiplied by its reverse BA gives 2,268. What is A + B?',
         opts=['9', '12', '7', '11'],
         hint='2,268 = 2² × 3⁴ × 7. Look for factor pairs that are reverses of each other.',
         sol='2,268 = 36 × 63, and 36 and 63 are reverses. So A + B = 3 + 6 = 9. (Other factor pairs such as 28 × 81 are not reverses.)'),
    dict(ch='10', scen='ways to climb 7 stairs taking 1 or 2 steps at a time',
         stem='Aarav climbs a staircase of 7 steps, taking either 1 or 2 steps at a time. In how many different ways can he reach the top?',
         opts=['21', '13', '34', '14'],
         hint='The number of ways to reach step n = ways to reach step n − 1 + ways to reach step n − 2.',
         sol='Ways for 1, 2, 3, … steps: 1, 2, 3, 5, 8, 13, 21. So 7 steps can be climbed in 21 ways.'),
    dict(ch='10', scen='numbers 1 to 100 leaving remainder 1 when divided by 3 and by 4',
         stem='How many of the numbers 1, 2, …, 100 leave a remainder of 1 when divided by 3 and also when divided by 4?',
         opts=['9', '8', '16', '25'],
         hint='Such numbers are 1 more than a multiple of 12.',
         sol='n − 1 must be a multiple of both 3 and 4, so of 12. n = 1, 13, 25, …, 97: (97 − 1) ÷ 12 + 1 = 9 numbers.'),
    dict(ch='10', scen='Menger sponge · cubes left after step 2',
         fig=drawing(270, 140, menger_face()),
         stem='A cube is cut into 27 equal cubes and the centre cube and the 6 face-centre cubes are removed, leaving 20 (step 1). At step 2, each of those 20 cubes is treated the same way. The front faces are shown. How many small cubes are left after step 2?',
         opts=['400', '160', '8,000', '380'],
         hint='Each cube becomes 20 smaller cubes.',
         sol='Step 1 leaves 20 cubes. Each becomes 20 smaller cubes at step 2: 20 × 20 = 400.'),

    # ---------------- Part 10 · Mixed Problems
    dict(ch='4+10', scen='x plus y 7 and x squared plus y squared 29 · x to the fourth plus y to the fourth',
         stem='If x + y = 7 and x² + y² = 29, what is x⁴ + y⁴?',
         opts=['641', '841', '441', '629'],
         hint='Find xy first, then use (x² + y²)².',
         sol='49 = 29 + 2xy, so xy = 10. x⁴ + y⁴ = (x² + y²)² − 2x²y² = 841 − 200 = 641. (The numbers are 5 and 2: 625 + 16 = 641.)'),
    dict(ch='5+10', scen='squares including tilted ones with corners on a 4 by 4 array of points',
         stem='Sixteen dots form a 4 × 4 square array, one unit apart. How many squares, including tilted ones, have all four corners on these dots?',
         opts=['20', '14', '16', '18'],
         hint='Count upright squares by size, then look for tilted ones inside 2 × 2 and 3 × 3 frames.',
         sol='Upright squares: 9 of side 1, 4 of side 2, 1 of side 3 = 14. Tilted squares: each 2 × 2 frame holds 1 (4 frames) and the 3 × 3 frame holds 2. Total 14 + 4 + 2 = 20.'),
    dict(ch='4+5', scen='square of area x squared plus 10x plus 25 at x 3 · diagonal',
         stem='A square has area (x² + 10x + 25) cm². What is the length of its diagonal when x = 3?',
         opts=['8√2 cm', '64 cm', '16 cm', '8 cm'],
         hint='x² + 10x + 25 is a perfect square.',
         sol='x² + 10x + 25 = (x + 5)², so the side is x + 5 = 8 cm. Diagonal = √(8² + 8²) = 8√2 cm.'),
    dict(ch='3+9', scen='₹6,000 at a rate that doubles money in 8 years for 5 years less 18 percent tax',
         stem='At a simple-interest rate that doubles money in 8 years, ₹6,000 is invested for 5 years. Tax of 18% is then deducted from the interest. How much interest does the investor keep?',
         opts=['₹3,075', '₹3,750', '₹675', '₹9,075'],
         hint='Doubling in 8 years means 12.5% a year.',
         sol='Rate = 100 ÷ 8 = 12.5%. Interest = 6,000 × 12.5% × 5 = ₹3,750. Tax = 18% of 3,750 = ₹675. Kept = ₹3,075.'),
    dict(ch='6+9', scen='open cylindrical bucket radius 14 height 30 made at ₹10 per 100 cm²',
         stem='An open cylindrical metal bucket (with a bottom but no lid) has radius 14 cm and height 30 cm. Metal sheet costs ₹10 per 100 cm². What does the metal cost? (Take π = 22/7.)',
         opts=['₹325.60', '₹264', '₹387.20', '₹3,256'],
         hint='Metal = curved surface + bottom circle.',
         sol='Curved surface = 2 × 22/7 × 14 × 30 = 2,640 cm². Bottom = 22/7 × 196 = 616 cm². Total 3,256 cm². Cost = 3,256 ÷ 100 × 10 = ₹325.60.'),
]
