# AMO Level-2 · Class 8 · Practice Paper 8
# Each question: ch, scen (unique), stem, opts (correct FIRST), hint, sol, optional fig.


def line_graph(labels, values, top, step, ylab='', ytitle='', vals=False, dx=55, h=150):
    """Line graph: one point per label, joined by straight lines; y gridlines every step."""
    x0, y0 = 46, 10
    X = lambda i: x0 + 20 + i * dx
    Y = lambda v: y0 + h - v * h / top
    w = 20 + (len(labels) - 1) * dx + 20
    prims = []
    for v in range(0, top + 1, step):
        prims += [('line', x0, Y(v), x0 + w, Y(v), True, (170, 170, 170), 0.8), ('text', x0 - 18, Y(v), str(v), 10)]
    prims.append(('polyline', [(X(i), Y(v)) for i, v in enumerate(values)]))
    prims += [('dot', X(i), Y(v), 3.5) for i, v in enumerate(values)]
    if vals:
        prims += [('text', X(i), Y(v) - 11, str(v), 10) for i, v in enumerate(values)]
    prims += [('text', X(i), y0 + h + 13, lab, 10) for i, lab in enumerate(labels)]
    prims += [('line', x0, y0, x0, y0 + h), ('line', x0, y0 + h, x0 + w, y0 + h)]
    if ylab:
        prims.append(('text', x0 + w / 2, y0 + h + 30, ylab, 10))
    if ytitle:
        prims.append(('text', x0 + 60, y0 - 16, ytitle, 10))
    return prims


def koch_curve(n, p, q):
    if n == 0:
        return [p]
    (x1, y1), (x2, y2) = p, q
    dx, dy = (x2 - x1) / 3, (y2 - y1) / 3
    a, b = (x1 + dx, y1 + dy), (x1 + 2 * dx, y1 + 2 * dy)
    c = (a[0] + dx * 0.5 + dy * 0.866, a[1] + dy * 0.5 - dx * 0.866)
    return koch_curve(n - 1, p, a) + koch_curve(n - 1, a, c) + koch_curve(n - 1, c, b) + koch_curve(n - 1, b, q)


def koch_curve_steps():
    prims = []
    for k in range(3):
        y = 52 + k * 64
        pts = koch_curve(k, (10, y), (172, y)) + [(172, y)]
        prims.append(('polyline', pts))
        prims.append(('text', 210, y - 8, f'Step {k}', 11))
    return prims


QUESTIONS = [
    # ---------------- Part 1 · Number System
    dict(ch='1', scen='perfect squares between 1 and 400 whose digits add up to 9',
         stem='How many perfect squares between 1 and 400 have digits that add up to exactly 9?',
         opts=['6', '4', '5', '3'],
         hint='A number with digit sum 9 is a multiple of 9, so its square root is a multiple of 3.',
         sol='Digit sum 9 means the square is a multiple of 9, so its root is a multiple of 3: 3, 6, 9, 12, 15, 18. Their squares 9, 36, 81, 144, 225, 324 all have digit sum 9. So there are 6.'),
    dict(ch='1', scen='which of four roots of decimals is irrational',
         stem='Which of these numbers is irrational?',
         opts=['√0.4', '√0.09', '√2.25', '∛0.008'],
         hint='Write each decimal as a fraction and check whether the top and bottom are perfect squares (or cubes).',
         sol='√0.09 = 0.3, √2.25 = 1.5 and ∛0.008 = 0.2 are rational. √0.4 = √(4/10) = 2/√10, which is irrational. (Careful: √0.4 is not 0.2.)'),

    # ---------------- Part 2 · Operations
    dict(ch='2', scen='sum of reciprocal powers of 2 3 4 squared minus a fifth to the minus 2',
         stem='What is [(1/2)⁻² + (1/3)⁻² + (1/4)⁻²] × (1/29)⁰ − (1/5)⁻²?',
         opts=['4', '29', '54', '0'],
         hint='(1/a)⁻² = a², and anything non-zero to the power 0 is 1.',
         sol='(1/2)⁻² + (1/3)⁻² + (1/4)⁻² = 4 + 9 + 16 = 29. Times (1/29)⁰ = 1 gives 29. (1/5)⁻² = 25. 29 − 25 = 4.'),
    dict(ch='2', scen='distance to a star 4.2 light years in kilometres',
         stem='A star is 4.2 light years away. One light year is about 9.46 × 10¹² km. About how far away is the star, in standard form?',
         opts=['3.97 × 10¹³ km', '3.97 × 10¹² km', '3.97 × 10¹⁴ km', '4.2 × 10¹³ km'],
         hint='4.2 × 9.46 is about 39.7.',
         sol='4.2 × 9.46 ≈ 39.73, so the distance ≈ 39.7 × 10¹² = 3.97 × 10¹³ km.'),

    # ---------------- Part 3 · Fractions, Decimals & Percentages
    dict(ch='3', scen='marked 50 percent above cost with 20 and x percent discounts giving 2 percent profit',
         stem='A shopkeeper marks goods 50% above cost. He gives two successive discounts, 20% and then x%, and still makes a 2% profit. What is x?',
         opts=['15', '10', '18', '20'],
         hint='Take cost = 100. After marking up and the first discount, the price is 120.',
         sol='Cost 100 → marked 150 → after 20% off: 120. The final price must be 102, so the second discount takes 18 off 120: 18/120 = 15%.'),
    dict(ch='3', scen='sum doubling in 10 years · years for interest equal to three fifths of it',
         stem='At simple interest a sum doubles in 10 years. In how many years will the interest be 3/5 of the sum?',
         opts=['6 years', '5 years', '8 years', '4 years'],
         hint='Doubling in 10 years means 10% a year.',
         sol='Interest equal to the sum in 10 years means 10% a year. 3/5 of the sum is 60%, which takes 6 years.'),
    dict(ch='3', scen='price up 20 percent then cut back to the original · cut percent',
         stem='The price of a book rises by 20%. By what percentage must the new price be cut to bring it back to the original price?',
         opts=['16 2/3%', '20%', '25%', '15%'],
         hint='The cut is 20 on a new price of 120.',
         sol='Take the original as 100; the new price is 120. To return to 100 the cut is 20 out of 120 = 1/6 = 16 2/3%.'),

    # ---------------- Part 4 · Algebra
    dict(ch='4', scen='a plus 1 over a is 6 · a squared minus 1 over a squared',
         stem='If a + 1/a = 6 and a > 1, what is a² − 1/a²?',
         opts=['24√2', '32', '34', '6√2'],
         hint='a² − 1/a² = (a + 1/a)(a − 1/a). Find a − 1/a first.',
         sol='(a − 1/a)² = (a + 1/a)² − 4 = 32, so a − 1/a = √32 = 4√2 (positive since a > 1). a² − 1/a² = 6 × 4√2 = 24√2.'),
    dict(ch='4', scen='simplify product with x squared minus 7x plus 12 over x squared minus 9',
         stem='For x ≠ 3 and x ≠ −3, simplify (x² − 7x + 12)(x + 3) ÷ (x² − 9).',
         opts=['x − 4', 'x + 4', 'x − 3', 'x + 3'],
         hint='Factorise both quadratics first.',
         sol='x² − 7x + 12 = (x − 3)(x − 4) and x² − 9 = (x − 3)(x + 3). So the expression is (x − 3)(x − 4)(x + 3) ÷ [(x − 3)(x + 3)] = x − 4.'),
    dict(ch='4', scen='one number 25 percent more than another with difference 18 · larger',
         stem='One number is 25% more than another, and their difference is 18. What is the larger number?',
         opts=['90', '72', '18', '108'],
         hint='If the smaller is x, the larger is 1.25x.',
         sol='1.25x − x = 0.25x = 18, so x = 72 and the larger number is 90.'),

    # ---------------- Part 5 · Geometry
    dict(ch='5', scen='rope between pole tops 17 m · bird from top of taller to foot of shorter',
         stem='Two vertical poles stand 15 m apart on level ground. A rope from the top of one to the top of the other is 17 m long, and the shorter pole is 12 m tall. A bird flies straight from the top of the taller pole to the foot of the shorter pole. How far does it fly?',
         opts=['25 m', '17 m', '20 m', '23 m'],
         hint='First find the difference in height from the rope.',
         sol='The rope, the 15 m gap and the height difference form a right triangle: difference = √(17² − 15²) = 8 m, so the taller pole is 20 m. Bird\'s path = √(15² + 20²) = √625 = 25 m. (20 m is the taller pole.)'),
    dict(ch='5', scen='parallelogram with perpendicular diagonals 16 and 12 · perimeter',
         stem='The diagonals of a parallelogram are 16 cm and 12 cm long and cross at right angles. What is its perimeter?',
         opts=['40 cm', '28 cm', '56 cm', '20 cm'],
         hint='A parallelogram whose diagonals are perpendicular is a rhombus.',
         sol='It is a rhombus. The half-diagonals 8 and 6 give a side of √(64 + 36) = 10 cm. Perimeter = 4 × 10 = 40 cm.'),
    dict(ch='5', scen='mirror on the ground showing the top of a tree 12 m beyond',
         stem='Rashmi, whose eyes are 1.6 m above the ground, stands 2 m from a small mirror lying on level ground. She sees the top of a tree in the mirror. The tree is 12 m beyond the mirror. How tall is the tree?',
         opts=['9.6 m', '15 m', '12 m', '7.5 m'],
         hint='The two right triangles on either side of the mirror are similar.',
         sol='The angles at the mirror are equal, so the triangles are similar: 1.6/2 = h/12. So h = 12 × 0.8 = 9.6 m.'),

    # ---------------- Part 6 · Mensuration
    dict(ch='6', scen='cylinder with curved surface 264 m² and volume 924 m³ · diameter',
         stem='A cylinder has curved surface area 264 m² and volume 924 m³. What is its diameter?',
         opts=['14 m', '7 m', '6 m', '3.5 m'],
         hint='Volume ÷ curved surface = πr²h ÷ 2πrh = r/2.',
         sol='924 ÷ 264 = 3.5 = r/2, so r = 7 m and the diameter is 14 m.'),
    dict(ch='6', scen='conical tent of radius 7 m made from 550 m² of canvas · volume',
         stem='A conical tent of base radius 7 m uses exactly 550 m² of canvas for its curved surface. What volume of air does it hold? (Take π = 22/7.)',
         opts=['1,232 m³', '3,696 m³', '550 m³', '1,078 m³'],
         hint='Find the slant height from πrl = 550, then the height.',
         sol='πrl = 22l = 550, so l = 25 m. Height = √(625 − 49) = 24 m. Volume = (1/3) × 22/7 × 49 × 24 = 1,232 m³.'),
    dict(ch='6', scen='cuboid 10 by 8 by 6 with a cylindrical hole of radius 1.4 drilled through',
         stem='A wooden block 10 cm × 8 cm × 6 cm has a cylindrical hole of radius 1.4 cm drilled straight through it along the 6 cm height. What volume of wood is left? (Take π = 22/7.)',
         opts=['443.04 cm³', '480 cm³', '516.96 cm³', '406.08 cm³'],
         hint='Subtract the volume of the hole from the block.',
         sol='Block = 480 cm³. Hole = 22/7 × 1.4 × 1.4 × 6 = 36.96 cm³. Left = 480 − 36.96 = 443.04 cm³.'),

    # ---------------- Part 7 · Data Handling
    dict(ch='8', scen='distance-time line graph of a cyclist · hour with the greatest speed',
         fig=drawing(330, 200, line_graph(['0', '1', '2', '3', '4', '5'], [0, 12, 24, 24, 40, 50], 50, 10, 'Time (hours)', ytitle='Distance (km)', vals=True)),
         stem='The line graph shows the distance (in km) a cyclist has covered after each hour. In which hour did the cyclist ride fastest, and at what speed?',
         opts=['From hour 3 to 4, at 16 km/h', 'From hour 4 to 5, at 10 km/h', 'From hour 1 to 2, at 12 km/h', 'From hour 3 to 4, at 40 km/h'],
         hint='Speed in each hour = rise in distance during that hour.',
         sol='Rises: 12, 12, 0, 16, 10 km. The greatest is 16 km, from hour 3 to hour 4: 16 km/h. (40 is the total distance at hour 4.)'),
    dict(ch='8', scen='mean of 25 numbers with overlapping first 13 and last 13 · thirteenth number',
         stem='The mean of 25 numbers is 40. The mean of the first 13 is 36 and the mean of the last 13 is 45. What is the 13th number?',
         opts=['53', '40', '36', '45'],
         hint='The 13th number is counted in both groups.',
         sol='First 13 total 468; last 13 total 585. Together that is 1,053, which counts the 13th number twice. All 25 total 1,000. So the 13th number = 1,053 − 1,000 = 53.'),

    # ---------------- Part 8 · Applied Mathematics
    dict(ch='9', scen='mixing 26 kg rice at ₹20 with 30 kg at ₹36 sold at ₹30 a kg',
         stem='A grocer mixes 26 kg of rice costing ₹20 per kg with 30 kg costing ₹36 per kg, and sells the mixture at ₹30 per kg. What is his profit percent?',
         opts=['5%', '10%', '4%', '6.25%'],
         hint='Find the total cost and the total selling price of all 56 kg.',
         sol='Cost = 26 × 20 + 30 × 36 = 520 + 1,080 = ₹1,600. Selling price = 56 × 30 = ₹1,680. Profit = 80 on 1,600 = 5%.'),
    dict(ch='9', scen='₹1,550 split between 5 and 8 percent for 3 years earning ₹300',
         stem='₹1,550 is lent in two parts, one at 5% and the other at 8% simple interest a year. After 3 years the total interest is ₹300. How much was lent at 5%?',
         opts=['₹800', '₹750', '₹600', '₹950'],
         hint='If all of it were at 8% for 3 years, the interest would be ₹372.',
         sol='At 8% on everything for 3 years: 1,550 × 24% = ₹372. The actual ₹300 is ₹72 less. Each rupee at 5% earns 9% less over 3 years, so the part at 5% = 72 ÷ 0.09 = ₹800.'),
    dict(ch='9', scen='one article free with every 5 bought still giving 20 percent profit · mark-up',
         stem='A dealer gives 1 article free with every 5 bought, and still makes a 20% profit. By what percentage above cost does he mark the articles?',
         opts=['44%', '20%', '40%', '50%'],
         hint='He receives the marked price of 5 articles for 6 articles.',
         sol='For 6 articles he receives 5 × MP. This must be 1.2 × 6 × CP = 7.2 CP. So MP = 1.44 CP, which is 44% above cost.'),

    # ---------------- Part 9 · Mathematical Reasoning
    dict(ch='10', scen='four-digit palindromes ABBA divisible by 99',
         stem='A four-digit number ABBA reads the same forwards and backwards. How many such numbers are divisible by 99?',
         opts=['10', '9', '8', '11'],
         hint='ABBA = 1001A + 110B is always a multiple of 11. When is it a multiple of 9?',
         sol='ABBA is always divisible by 11. It is divisible by 9 when its digit sum 2A + 2B is a multiple of 9, so A + B = 9 or 18. A + B = 9 with A from 1 to 9 gives 9 numbers (1881 … 9009), and A = B = 9 gives 9999. Total 10.'),
    dict(ch='10', scen='triangles with whole-number sides and perimeter 15',
         stem='How many different triangles have whole-number sides and a perimeter of 15 cm?',
         opts=['7', '5', '6', '8'],
         hint='List sides a ≤ b ≤ c with a + b + c = 15 and a + b > c.',
         sol='The longest side c must be less than 7.5 and at least 5. c = 7: (1,7,7), (2,6,7), (3,5,7), (4,4,7). c = 6: (3,6,6), (4,5,6). c = 5: (5,5,5). Total 7.'),
    dict(ch='10', scen='last digit of 7 to the power 2025',
         stem='What is the last digit of 7²⁰²⁵?',
         opts=['7', '9', '3', '1'],
         hint='Find the pattern in the last digits of 7¹, 7², 7³, 7⁴, …',
         sol='Last digits of powers of 7 repeat 7, 9, 3, 1 every 4 powers. 2025 = 4 × 506 + 1, so 7²⁰²⁵ ends in the same digit as 7¹, which is 7.'),
    dict(ch='10', scen='Koch curve from a 27 cm segment · length after step 3',
         fig=drawing(250, 190, koch_curve_steps()),
         stem='A 27 cm straight segment is changed step by step: every straight piece is split into three equal parts and the middle part is replaced by two sides of an equilateral triangle. Steps 0, 1 and 2 are shown. How long is the curve after step 3?',
         opts=['64 cm', '48 cm', '81 cm', '36 cm'],
         hint='Each step multiplies the length by 4/3.',
         sol='Each step replaces 3 parts by 4 parts of the same size, so the length is multiplied by 4/3. After 3 steps: 27 × (4/3)³ = 27 × 64/27 = 64 cm. (48 cm is after step 2.)'),

    # ---------------- Part 10 · Mixed Problems
    dict(ch='4+10', scen='positive whole numbers with x squared minus y squared equal to the prime 31',
         stem='Positive whole numbers x and y satisfy x² − y² = 31. What is x + y?',
         opts=['31', '16', '15', '1'],
         hint='31 is prime, so it has only one factor pair.',
         sol='(x − y)(x + y) = 31. Since 31 is prime and x + y > x − y, x − y = 1 and x + y = 31 (so x = 16, y = 15).'),
    dict(ch='5+10', scen='painted cube cut so that 96 small cubes have exactly one painted face',
         stem='A large cube is painted on all faces and cut into equal small cubes, with n small cubes along each edge. Exactly 96 small cubes have paint on just one face. What is n?',
         opts=['6', '4', '8', '5'],
         hint='Each face has (n − 2)² small cubes with only that face painted.',
         sol='6(n − 2)² = 96, so (n − 2)² = 16 and n − 2 = 4. So n = 6.'),
    dict(ch='4+5', scen='rectangle with diagonal 17 and perimeter 46 · area',
         stem='A rectangle has a diagonal of 17 cm and a perimeter of 46 cm. What is its area?',
         opts=['120 cm²', '240 cm²', '132 cm²', '60 cm²'],
         hint='l + w = 23 and l² + w² = 17². Use (l + w)².',
         sol='(l + w)² = 529 = l² + w² + 2lw = 289 + 2lw, so 2lw = 240 and the area lw = 120 cm². (The sides are 15 cm and 8 cm.)'),
    dict(ch='3+9', scen='single discount equal to 20 then 25 then 10 percent cash discount',
         stem='A television is sold with successive discounts of 20% and 25%, and a further 10% off for paying in cash. What single discount would give a cash buyer the same price?',
         opts=['46%', '55%', '45%', '54%'],
         hint='Multiply 0.8 × 0.75 × 0.9 to find what the buyer pays.',
         sol='0.8 × 0.75 × 0.9 = 0.54, so the buyer pays 54% of the price and the single discount is 46%. (55% simply adds 20 + 25 + 10.)'),
    dict(ch='6+9', scen='full cylindrical diesel tank radius 7 m height 3 m at 3,080 litres a day',
         stem='A cylindrical diesel tank of radius 7 m and height 3 m is full. A depot sells 3,080 litres a day. For how many days will the diesel last? (Take π = 22/7.)',
         opts=['150 days', '15 days', '1,500 days', '50 days'],
         hint='1 m³ = 1,000 litres.',
         sol='Volume = 22/7 × 49 × 3 = 462 m³ = 4,62,000 litres. 4,62,000 ÷ 3,080 = 150 days.'),
]
