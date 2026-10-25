# AMO Level-2 · Class 8 · Practice Paper 7
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
        prims.append(('rect', x, y0 + h - f * h / top, bw, f * h / top, 'green'))
        prims.append(('text', x + bw / 2, y0 + h - f * h / top - 8, str(f), 10))
    for i, e in enumerate(edges):
        prims.append(('text', x0 + i * bw, y0 + h + 13, str(e), 10))
    prims += [('line', x0, y0, x0, y0 + h), ('line', x0, y0 + h, x0 + w + 10, y0 + h)]
    if xlab:
        prims.append(('text', x0 + w / 2, y0 + h + 30, xlab, 10))
    if ylab:
        prims.append(('text', x0 + 50, y0 - 16, ylab, 10))
    return prims


def sierp(n, x, y, s):
    h = s * 0.866
    if n == 0:
        return [('poly', [(x, y), (x - s / 2, y + h), (x + s / 2, y + h)], 'yellow')]
    return sierp(n - 1, x, y, s / 2) + sierp(n - 1, x - s / 4, y + h / 2, s / 2) + sierp(n - 1, x + s / 4, y + h / 2, s / 2)


def sierp_three():
    prims = []
    for k in range(3):
        cx = 50 + k * 120
        prims += [('poly', [(cx, 10), (cx - 45, 88), (cx + 45, 88)], 'white')] + sierp(k, cx, 10, 90)
        prims.append(('text', cx, 104, f'Step {k}', 11))
    return prims


QUESTIONS = [
    # ---------------- Part 1 · Number System
    dict(ch='1', scen='nearest perfect squares above and below 320 · their difference',
         stem='Let P be the smallest perfect square greater than 320, and Q the largest perfect square less than 320. What is P − Q?',
         opts=['35', '31', '37', '33'],
         hint='Which two consecutive whole numbers have squares on either side of 320?',
         sol='17² = 289 and 18² = 324, with 289 < 320 < 324. So P = 324, Q = 289 and P − Q = 35 (= 17 + 18).'),
    dict(ch='1', scen='cube root of minus 512 times 27 over 1000',
         stem='What is the cube root of −512 × 27/1,000?',
         opts=['−2.4', '2.4', '−24', '−0.24'],
         hint='Find the cube root of each part: −512, 27 and 1,000.',
         sol='∛(−512) = −8, ∛27 = 3 and ∛1,000 = 10. So the cube root is −8 × 3 ÷ 10 = −2.4.'),

    # ---------------- Part 2 · Operations
    dict(ch='2', scen='5 to the 2x minus 1 divided by 25 equals 125',
         stem='Find x if 5²ˣ⁻¹ ÷ 25 = 125.',
         opts=['3', '2', '4', '5/2'],
         hint='Write 25 and 125 as powers of 5.',
         sol='5²ˣ⁻¹ ÷ 5² = 5²ˣ⁻³ = 5³. So 2x − 3 = 3 and x = 3.'),
    dict(ch='2', scen='blood cell 0.000006 m and virus 0.00000003 m · how many times larger',
         stem='A blood cell is about 0.000006 m across and a virus is about 0.00000003 m across. Using standard form, find how many times wider the blood cell is.',
         opts=['200', '20', '2,000', '2 × 10⁻²'],
         hint='0.000006 = 6 × 10⁻⁶ and 0.00000003 = 3 × 10⁻⁸.',
         sol='(6 × 10⁻⁶) ÷ (3 × 10⁻⁸) = 2 × 10² = 200.'),

    # ---------------- Part 3 · Fractions, Decimals & Percentages
    dict(ch='3', scen='₹3,000 item with 30 percent off against 20 then 20 percent off',
         stem='A ₹3,000 jacket is offered either at 30% off, or at 20% off followed by a further 20% off. Which offer is cheaper, and by how much?',
         opts=['20% then 20%, by ₹180', '30%, by ₹180', '20% then 20%, by ₹300', 'Both cost the same'],
         hint='0.8 × 0.8 = 0.64.',
         sol='30% off: ₹2,100. 20% then 20%: 3,000 × 0.64 = ₹1,920, an overall 36% off. The double discount is cheaper by ₹180.'),
    dict(ch='3', scen='amount ₹6,240 in 2 years at 15 percent · interest for 5 years',
         stem='A sum of money amounts to ₹6,240 in 2 years at 15% simple interest a year. What is the simple interest on the same sum for 5 years at the same rate?',
         opts=['₹3,600', '₹4,680', '₹2,400', '₹3,120'],
         hint='₹6,240 is the sum plus 30% of it.',
         sol='Sum × 1.30 = 6,240, so the sum = ₹4,800. Interest for 5 years = 4,800 × 75% = ₹3,600. (₹4,680 wrongly takes 75% of ₹6,240.)'),
    dict(ch='3', scen='population 50,000 up 8 percent down 5 percent up 10 percent',
         stem='A town had 50,000 people. Its population rose by 8% in the first year, fell by 5% in the second and rose by 10% in the third. What was the population at the end?',
         opts=['56,430', '56,500', '55,000', '57,000'],
         hint='Multiply by 1.08, then 0.95, then 1.10.',
         sol='50,000 × 1.08 = 54,000. × 0.95 = 51,300. × 1.10 = 56,430. (56,500 wrongly adds 8 − 5 + 10 = 13%.)'),

    # ---------------- Part 4 · Algebra
    dict(ch='4', scen='1.02 squared minus 0.98 squared',
         stem='Using an identity, find 1.02² − 0.98².',
         opts=['0.08', '0.04', '0.0016', '0.8'],
         hint='a² − b² = (a + b)(a − b).',
         sol='(1.02 + 0.98)(1.02 − 0.98) = 2 × 0.04 = 0.08.'),
    dict(ch='4', scen='which expression is not a factor of x to the fourth minus 81',
         stem='Which of these is NOT a factor of x⁴ − 81?',
         opts=['x + 9', 'x + 3', 'x² + 9', 'x² − 9'],
         hint='Use a² − b² twice.',
         sol='x⁴ − 81 = (x² − 9)(x² + 9) = (x − 3)(x + 3)(x² + 9). So x + 3, x² + 9 and x² − 9 are factors, but x + 9 is not.'),
    dict(ch='4', scen='purse of ₹1 ₹2 and ₹5 coins in ratio 3 to 4 to 5 worth ₹180',
         stem='A purse has ₹1, ₹2 and ₹5 coins in the ratio 3 : 4 : 5 by number. The total value is ₹180. How many ₹5 coins are there?',
         opts=['25', '15', '20', '30'],
         hint='Let the numbers of coins be 3k, 4k and 5k.',
         sol='Value = 3k × 1 + 4k × 2 + 5k × 5 = 36k = 180, so k = 5. There are 5k = 25 coins of ₹5.'),

    # ---------------- Part 5 · Geometry
    dict(ch='5', scen='area of an equilateral triangle of side 6 using Pythagoras',
         stem='Using Pythagoras, find the area of an equilateral triangle with side 6 cm.',
         opts=['9√3 cm²', '18√3 cm²', '18 cm²', '9√2 cm²'],
         hint='The height from a corner meets the opposite side at its midpoint.',
         sol='Height = √(6² − 3²) = √27 = 3√3 cm. Area = ½ × 6 × 3√3 = 9√3 cm².'),
    dict(ch='5', scen='tree shadow 24 m when a 2 m stick casts 1.5 m · later shadow when the stick casts 2 m',
         stem='At noon a 2 m stick casts a 1.5 m shadow and a tree casts a 24 m shadow. Later, the same stick casts a 2 m shadow. How long is the tree\'s shadow then?',
         opts=['32 m', '24 m', '18 m', '36 m'],
         hint='First find the height of the tree using similar triangles.',
         sol='Tree height ÷ 24 = 2 ÷ 1.5, so the tree is 32 m tall. Later the shadow equals the height (2 m stick, 2 m shadow), so the tree\'s shadow is 32 m.'),
    dict(ch='5', scen='rhombus with side 8 and an angle of 120 degrees · shorter diagonal',
         stem='A rhombus has side 8 cm and one angle of 120°. How long is its shorter diagonal?',
         opts=['8 cm', '8√3 cm', '4 cm', '16 cm'],
         hint='The angle next to the 120° angle is 60°.',
         sol='The rhombus has angles 120° and 60°. The shorter diagonal joins the two 120° corners and cuts off a triangle with two sides of 8 cm and a 60° angle between them. That triangle is equilateral, so the diagonal is 8 cm.'),

    # ---------------- Part 6 · Mensuration
    dict(ch='6', scen='water through a 14 cm pipe at 5 m a second · litres a minute',
         stem='Water flows at 5 m per second through a pipe of internal diameter 14 cm. How many litres flow out in one minute? (Take π = 22/7.)',
         opts=['4,620 L', '77 L', '1,155 L', '18,480 L'],
         hint='In one second a cylinder of water 5 m long comes out.',
         sol='Per second: 22/7 × 0.07 × 0.07 × 5 = 0.077 m³ = 77 L. Per minute: 77 × 60 = 4,620 L. (18,480 uses the diameter as the radius.)'),
    dict(ch='6', scen='conical tent radius 21 m height 20 m · volume of air',
         stem='A conical tent has base radius 21 m and height 20 m. How much air does it hold? (Take π = 22/7.)',
         opts=['9,240 m³', '27,720 m³', '1,914 m³', '4,620 m³'],
         hint='Volume of a cone = (1/3)πr²h.',
         sol='(1/3) × 22/7 × 21 × 21 × 20 = 22 × 21 × 20 = 9,240 m³. (27,720 forgets the 1/3; 1,914 is the curved surface area.)'),
    dict(ch='6', scen='bricks 25 by 12.5 by 7.5 cm for a wall 10 m by 30 cm by 2 m',
         stem='How many bricks, each 25 cm × 12.5 cm × 7.5 cm, are needed to build a wall 10 m long, 30 cm thick and 2 m high (ignore mortar)?',
         opts=['2,560', '25,600', '256', '2,500'],
         hint='Change the wall to centimetres and compare volumes.',
         sol='Wall = 1,000 × 30 × 200 = 60,00,000 cm³. One brick = 25 × 12.5 × 7.5 = 2,343.75 cm³. Number = 60,00,000 ÷ 2,343.75 = 2,560.'),

    # ---------------- Part 7 · Data Handling
    dict(ch='8', scen='histogram of heights · percentage at least 150 cm',
         fig=drawing(300, 200, hist([140, 145, 150, 155, 160, 165], [4, 9, 15, 8, 4], 16, 2, 'Height (cm)', ylab='Number of students')),
         stem='The histogram shows the heights of the students in a class (each class includes its lower value, not its upper value). What percentage of the students are 150 cm or taller?',
         opts=['67.5%', '27%', '57.5%', '37.5%'],
         hint='Find the total first.',
         sol='Total = 4 + 9 + 15 + 8 + 4 = 40. Height 150 cm or more: 15 + 8 + 4 = 27. 27 ÷ 40 = 67.5%.'),
    dict(ch='8', scen='five numbers with mean 12 median 13 and mode 15 · sum of the two smallest',
         stem='Five whole numbers have mean 12, median 13 and a single mode, 15. What is the sum of the two smallest numbers?',
         opts=['17', '30', '13', '24'],
         hint='In order, the 3rd number is 13 and the mode must appear at least twice.',
         sol='Total = 60. In order: a, b, 13, d, e. The only mode is 15, so it appears at least twice and must be d and e. Then a + b = 60 − 13 − 30 = 17 (for example 8 and 9).'),

    # ---------------- Part 8 · Applied Mathematics
    dict(ch='9', scen='A sells to B at 20 percent profit and B to C at 10 percent loss for ₹5,400',
         stem='Aditi sells a sewing machine to Bharat at 20% profit. Bharat sells it to Charvi at a 10% loss for ₹5,400. What did it cost Aditi?',
         opts=['₹5,000', '₹4,500', '₹5,400', '₹4,800'],
         hint='Work backwards: 5,400 = cost × 1.2 × 0.9.',
         sol='1.2 × 0.9 = 1.08. Cost = 5,400 ÷ 1.08 = ₹5,000. Check: Bharat paid ₹6,000 and sold for ₹5,400.'),
    dict(ch='9', scen='₹2,500 at 8 percent matching ₹4,000 at 6 percent for 5 years',
         stem='₹4,000 earns simple interest at 6% a year for 5 years. In how many years will ₹2,500 earn the same interest at 8% a year?',
         opts=['6 years', '5 years', '8 years', '4 years'],
         hint='Find the first interest, then divide by the yearly interest on ₹2,500.',
         sol='First interest = 4,000 × 6% × 5 = ₹1,200. ₹2,500 at 8% earns ₹200 a year. 1,200 ÷ 200 = 6 years.'),
    dict(ch='9', scen='price ₹1,770 including 18 percent GST with 25 percent profit · cost',
         stem='A shop sells a fan for ₹1,770, which includes 18% GST on its own selling price. Before GST, the shop makes a 25% profit on cost. What is the cost price?',
         opts=['₹1,200', '₹1,500', '₹1,416', '₹1,280'],
         hint='Remove the GST first: ₹1,770 is 118% of the price before tax.',
         sol='Price before GST = 1,770 ÷ 1.18 = ₹1,500. Cost = 1,500 ÷ 1.25 = ₹1,200.'),

    # ---------------- Part 9 · Mathematical Reasoning
    dict(ch='10', scen='2AB times 3 equals 7A1',
         stem='In the multiplication 2AB × 3 = 7A1, A and B are digits. What is A + B?',
         opts=['11', '9', '13', '7'],
         hint='B × 3 ends in 1.',
         sol='3 × B ends in 1, so B = 7 (3 × 7 = 21). Then 2A7 × 3 = 621 + 30A must equal 7A1 = 701 + 10A, so 20A = 80 and A = 4. Check: 247 × 3 = 741. A + B = 11.'),
    dict(ch='10', scen='three-digit numbers containing exactly one digit 7',
         stem='How many three-digit numbers contain the digit 7 exactly once?',
         opts=['225', '243', '252', '200'],
         hint='Count by the position of the 7. Remember the first digit cannot be 0.',
         sol='7 in the hundreds place: the other two digits are any of 9 non-7 digits: 81. 7 in the tens place: hundreds digit 8 choices (1–9 except 7), ones 9: 72. 7 in the ones place: likewise 72. Total = 81 + 72 + 72 = 225.'),
    dict(ch='10', scen='sum of two-digit numbers leaving remainder 3 when divided by 7',
         stem='What is the sum of all two-digit numbers that leave a remainder of 3 when divided by 7?',
         opts=['676', '637', '715', '598'],
         hint='The numbers are 10, 17, 24, …, 94. Pair the first with the last.',
         sol='The numbers are 10, 17, …, 94: (94 − 10) ÷ 7 + 1 = 13 numbers. Pairing first and last gives 104 each, so the sum = 13 × 104 ÷ 2 = 676.'),
    dict(ch='10', scen='Sierpinski triangle · total perimeter of shaded triangles after step 3',
         fig=drawing(330, 110, sierp_three()),
         stem='At each step, every shaded triangle is split into four equal triangles and the middle one is removed. Steps 0, 1 and 2 are shown. If the side at step 0 is 8 cm, what is the total perimeter of all the shaded triangles after step 3?',
         opts=['81 cm', '24 cm', '54 cm', '108 cm'],
         hint='Each step triples the number of triangles and halves their side.',
         sol='After step 3 there are 3³ = 27 shaded triangles, each with side 8 ÷ 2³ = 1 cm and perimeter 3 cm. Total = 27 × 3 = 81 cm. (54 cm is the total after step 2.)'),

    # ---------------- Part 10 · Mixed Problems
    dict(ch='4+10', scen='20 squared minus 19 squared plus 18 squared minus 17 squared down to 1',
         stem='What is 20² − 19² + 18² − 17² + … + 2² − 1²?',
         opts=['210', '200', '190', '420'],
         hint='Each pair a² − b² with a = b + 1 equals a + b.',
         sol='20² − 19² = 39, 18² − 17² = 35, …, 2² − 1² = 3. Each pair is the sum of its two numbers, so the total is 1 + 2 + … + 20 = 210.'),
    dict(ch='5+10', scen='3 by 3 by 3 cube with the centre and face-centre cubes removed',
         stem='A 3 × 3 × 3 cube is built from 27 small cubes. The small cube at the centre of each face and the one at the very centre are removed, leaving three square tunnels. How many small cubes are left?',
         opts=['20', '21', '18', '24'],
         hint='There are 6 face-centre cubes and 1 central cube.',
         sol='Removed: 6 face centres + 1 centre = 7. Left: 27 − 7 = 20. (This is step 1 of the Menger sponge fractal.)'),
    dict(ch='4+5', scen='right triangle with hypotenuse 25 and legs adding to 31 · area',
         stem='A right-angled triangle has hypotenuse 25 cm, and its two shorter sides add up to 31 cm. What is its area?',
         opts=['84 cm²', '168 cm²', '150 cm²', '96 cm²'],
         hint='(a + b)² = a² + b² + 2ab, and a² + b² = 25².',
         sol='961 = 625 + 2ab, so 2ab = 336 and ab = 168. Area = ½ab = 84 cm². (The sides are 7 cm and 24 cm.)'),
    dict(ch='3+9', scen='marked ₹1,000 with successive 15 and 10 percent discounts at 2 percent profit',
         stem='A table marked ₹1,000 is sold after successive discounts of 15% and 10%. The seller still makes a profit of 2%. What did the table cost the seller?',
         opts=['₹750', '₹765', '₹700', '₹800'],
         hint='Find the selling price, then divide by 1.02.',
         sol='Selling price = 1,000 × 0.85 × 0.9 = ₹765. Cost = 765 ÷ 1.02 = ₹750.'),
    dict(ch='6+9', scen='conical oil tank radius 3.5 m height 6 m at ₹2 a litre',
         stem='A conical tank of base radius 3.5 m and height 6 m is full of oil worth ₹2 per litre. What is the value of the oil? (Take π = 22/7.)',
         opts=['₹1,54,000', '₹4,62,000', '₹15,400', '₹77,000'],
         hint='1 m³ = 1,000 litres.',
         sol='Volume = (1/3) × 22/7 × 3.5 × 3.5 × 6 = 77 m³ = 77,000 litres. Value = 77,000 × 2 = ₹1,54,000.'),
]
