# AMO Level-2 · Class 8 · Practice Paper 6
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
        prims.append(('text', cx + (r + 34) * math.cos(mid), cy + (r + 18) * math.sin(mid), f'{lab} {deg}', 10))
        a += deg
    return prims


def tree(n, x, y, length, ang):
    import math
    x2, y2 = x + length * math.cos(math.radians(ang)), y - length * math.sin(math.radians(ang))
    out = [('line', x, y, x2, y2, False, (34, 34, 34), 1.6)]
    if n > 0:
        out += tree(n - 1, x2, y2, length / 2, ang + 35) + tree(n - 1, x2, y2, length / 2, ang - 35)
    return out


def tree_steps():
    prims = []
    for k, x in enumerate((50, 170, 290)):
        prims += tree(k, x, 120, 50, 90)
        prims.append(('text', x, 138, f'Step {k}', 11))
    return prims


QUESTIONS = [
    # ---------------- Part 1 · Number System
    dict(ch='1', scen='numbers between 1 and 1000 that are both squares and cubes',
         stem='How many numbers between 1 and 1,000 (not counting 1 and 1,000) are both perfect squares and perfect cubes?',
         opts=['2', '3', '1', '4'],
         hint='A number that is both a square and a cube is a sixth power.',
         sol='Such numbers are n⁶: 2⁶ = 64 and 3⁶ = 729 lie between 1 and 1,000; 4⁶ = 4,096 is too large. So there are 2 (64 = 8² = 4³ and 729 = 27² = 9³).'),
    dict(ch='1', scen='root of 6 and a quarter minus root of 2 and 7 ninths',
         stem='What is √(6 1/4) − √(2 7/9)?',
         opts=['5/6', '1/6', '5/12', '7/6'],
         hint='Write each mixed number as an improper fraction first.',
         sol='6 1/4 = 25/4, so its root is 5/2. 2 7/9 = 25/9, so its root is 5/3. 5/2 − 5/3 = 15/6 − 10/6 = 5/6.'),

    # ---------------- Part 2 · Operations
    dict(ch='2', scen='minus 3 to the minus 2 times 3 cubed all to the minus 1',
         stem='What is ((−3)⁻² × 3³)⁻¹?',
         opts=['1/3', '3', '−1/3', '−3'],
         hint='(−3)⁻² = 1/(−3)² = 1/9.',
         sol='(−3)⁻² = 1/9, so (1/9) × 27 = 3. The inverse of 3 is 1/3. (The square makes the sign positive.)'),
    dict(ch='2', scen='computer doing 4.5 times 10 to the 9 operations a second · minutes for 2.7 times 10 to the 13',
         stem='A computer carries out 4.5 × 10⁹ operations every second. How long does it take to carry out 2.7 × 10¹³ operations?',
         opts=['100 minutes', '6,000 minutes', '10 minutes', '60 minutes'],
         hint='Divide, then change seconds into minutes.',
         sol='2.7 × 10¹³ ÷ 4.5 × 10⁹ = 0.6 × 10⁴ = 6,000 seconds = 100 minutes.'),

    # ---------------- Part 3 · Fractions, Decimals & Percentages
    dict(ch='3', scen='buy 2 get the third at half price · effective discount',
         stem='A shop offers "buy 2, get the 3rd at half price" on identical bags. What is the effective discount on 3 bags?',
         opts=['16 2/3%', '50%', '33 1/3%', '20%'],
         hint='You pay for 2½ bags out of 3.',
         sol='Paying for 2.5 bags instead of 3 saves 0.5 bag out of 3 = 1/6 = 16 2/3%.'),
    dict(ch='3', scen='equal sums at 7 and 9 percent with interest gap ₹480 in 4 years',
         stem='Two equal sums are lent, one at 7% and the other at 9% simple interest a year. After 4 years the difference in their interest is ₹480. What is each sum?',
         opts=['₹6,000', '₹3,000', '₹12,000', '₹4,800'],
         hint='The rates differ by 2% a year.',
         sol='The difference is 2% a year for 4 years = 8% of the sum = ₹480. So the sum = 480 × 100 ÷ 8 = ₹6,000.'),
    dict(ch='3', scen='rectangle length up 25 percent · breadth cut to keep the area',
         stem='The length of a rectangle is increased by 25%. By what percentage must its breadth be reduced so that the area stays the same?',
         opts=['20%', '25%', '15%', '80%'],
         hint='The new breadth must be 1 ÷ 1.25 of the old.',
         sol='1 ÷ 1.25 = 0.8, so the breadth must become 80% of the old breadth: a 20% reduction. (25% would leave the area at 1.25 × 0.75 = 93.75%.)'),

    # ---------------- Part 4 · Algebra
    dict(ch='4', scen='2x plus 3y squared minus 2x minus 3y squared at x half and y third',
         stem='What is (2x + 3y)² − (2x − 3y)² when x = 1/2 and y = 1/3?',
         opts=['4', '24', '0', '2'],
         hint='Simplify with a² − b² before substituting.',
         sol='(2x + 3y)² − (2x − 3y)² = 4 × 2x × 3y = 24xy. With x = 1/2 and y = 1/3: 24 × 1/6 = 4.'),
    dict(ch='4', scen='x squared plus y squared 74 and xy 35 · positive x plus y',
         stem='Positive numbers x and y satisfy x² + y² = 74 and xy = 35. What is x + y?',
         opts=['12', '2', '√74', '10'],
         hint='(x + y)² = x² + y² + 2xy.',
         sol='(x + y)² = 74 + 70 = 144, so x + y = 12. (The numbers are 7 and 5.)'),
    dict(ch='4', scen='rectangle with perimeter 64 and length 4 less than 3 times breadth · area',
         stem='The perimeter of a rectangle is 64 cm. Its length is 4 cm less than three times its breadth. What is its area?',
         opts=['207 cm²', '192 cm²', '240 cm²', '161 cm²'],
         hint='Length + breadth = 32.',
         sol='b + (3b − 4) = 32, so 4b = 36 and b = 9 cm; the length is 23 cm. Area = 9 × 23 = 207 cm².'),

    # ---------------- Part 5 · Geometry
    dict(ch='5', scen='square of side 8 with E the midpoint of AB · length CE',
         stem='ABCD is a square of side 8 cm and E is the midpoint of AB. How long is CE?',
         opts=['4√5 cm', '8√2 cm', '12 cm', '4√3 cm'],
         hint='Triangle EBC has a right angle at B.',
         sol='EB = 4 cm and BC = 8 cm, with a right angle at B. CE = √(16 + 64) = √80 = 4√5 cm.'),
    dict(ch='5', scen='parallelogram with one angle two thirds of its neighbour · largest angle',
         stem='In a parallelogram, one angle is 2/3 of the angle next to it. What is the largest angle of the parallelogram?',
         opts=['108°', '72°', '120°', '90°'],
         hint='Neighbouring angles of a parallelogram add up to 180°.',
         sol='x + 2x/3 = 180°, so 5x/3 = 180° and x = 108°. The angles are 108° and 72°; the largest is 108°.'),
    dict(ch='5', scen='rhombus with side 13 and one diagonal 24 · area',
         stem='A rhombus has side 13 cm and one diagonal 24 cm. What is its area?',
         opts=['120 cm²', '312 cm²', '240 cm²', '156 cm²'],
         hint='Half-diagonals and a side make a right triangle.',
         sol='Half of the known diagonal is 12. The other half-diagonal is √(169 − 144) = 5, so the other diagonal is 10. Area = ½ × 24 × 10 = 120 cm².'),

    # ---------------- Part 6 · Mensuration
    dict(ch='6', scen='cone and cylinder with equal base and volume · cone height',
         stem='A cone and a cylinder have equal bases and equal volumes. The cylinder is 6 cm tall. How tall is the cone?',
         opts=['18 cm', '2 cm', '6 cm', '12 cm'],
         hint='(1/3)πr²H = πr²h.',
         sol='(1/3)πr²H = πr² × 6 gives H = 18 cm. A cone must be three times as tall to hold the same amount.'),
    dict(ch='6', scen='well of diameter 3.5 m and depth 10 m spread on a 22 m by 14 m plot',
         stem='A cylindrical well of diameter 3.5 m is dug 10 m deep. The earth taken out is spread evenly over a plot 22 m by 14 m. By how much is the level of the plot raised? (Take π = 22/7.)',
         opts=['31.25 cm', '3.125 cm', '62.5 cm', '12.5 cm'],
         hint='Volume of earth = πr²h with r = 1.75 m.',
         sol='Volume = 22/7 × 1.75 × 1.75 × 10 = 96.25 m³. Plot area = 308 m². Rise = 96.25 ÷ 308 = 0.3125 m = 31.25 cm.'),
    dict(ch='6', scen='tank 3 m by 2 m filled at 2 litres a second · time to rise 5 cm',
         stem='Water flows into a cuboid tank with a base of 3 m by 2 m at 2 litres every second. How long does it take for the water level to rise by 5 cm?',
         opts=['2.5 minutes', '25 minutes', '15 minutes', '150 minutes'],
         hint='Volume needed = 3 × 2 × 0.05 m³; 1 m³ = 1,000 litres.',
         sol='Volume = 3 × 2 × 0.05 = 0.3 m³ = 300 litres. Time = 300 ÷ 2 = 150 seconds = 2.5 minutes. (150 minutes forgets that the rate is per second.)'),

    # ---------------- Part 7 · Data Handling
    dict(ch='8', scen='pie chart of 720 students favourite sports with an unknown football sector',
         fig=drawing(320, 180, pie([('Cricket', 150), ('Football', 90), ('Hockey', 50), ('Others', 70)])),
         stem='The pie chart shows the favourite sports of 720 students (angles in degrees). How many more students prefer football than hockey?',
         opts=['80', '40', '100', '60'],
         hint='Each degree stands for 720 ÷ 360 students.',
         sol='Each degree is 2 students. Football − hockey = 90° − 50° = 40°, which is 80 students.'),
    dict(ch='8', scen='ordered data 3 5 7 x 11 13 with median 8 · mean',
         stem='The numbers 3, 5, 7, x, 11, 13 are in increasing order and their median is 8. What is their mean?',
         opts=['8', '8.5', '7', '9'],
         hint='With six numbers, the median is the average of the 3rd and 4th.',
         sol='(7 + x) ÷ 2 = 8, so x = 9. Total = 3 + 5 + 7 + 9 + 11 + 13 = 48. Mean = 48 ÷ 6 = 8.'),

    # ---------------- Part 8 · Applied Mathematics
    dict(ch='9', scen='cost of 20 equals selling price of 16 with a 10 percent discount · mark-up',
         stem='The cost price of 20 identical lamps equals the selling price of 16 of them. The shop sells them after a 10% discount on the marked price. By what percentage above cost is the marked price?',
         opts=['38 8/9%', '35%', '25%', '40%'],
         hint='First find the profit percent; then undo the discount.',
         sol='SP of 16 = CP of 20, so SP = 1.25 × CP (25% profit). SP = 0.9 × MP, so MP = 1.25 ÷ 0.9 × CP = 1.3888… × CP, which is 38 8/9% above cost.'),
    dict(ch='9', scen='₹5,000 for 2 years and ₹3,000 for 4 years at one rate earning ₹2,200',
         stem='Anand lends ₹5,000 to Gopal for 2 years and ₹3,000 to Hari for 4 years, both at the same rate of simple interest. He receives ₹2,200 in interest altogether. What is the rate?',
         opts=['10%', '11%', '12%', '8%'],
         hint='Interest = principal × years × rate.',
         sol='Interest = 5,000 × 2 × r% + 3,000 × 4 × r% = 22,000 × r% = 2,200, so r = 10.'),
    dict(ch='9', scen='car sold at 10 percent loss · ₹45,000 more would give 5 percent gain',
         stem='A car is sold at a loss of 10%. Had it been sold for ₹45,000 more, there would have been a gain of 5%. What was the cost price?',
         opts=['₹3,00,000', '₹4,50,000', '₹2,70,000', '₹3,15,000'],
         hint='From 10% loss to 5% gain is 15% of the cost.',
         sol='The extra ₹45,000 covers 10% + 5% = 15% of the cost. Cost = 45,000 × 100 ÷ 15 = ₹3,00,000.'),

    # ---------------- Part 9 · Mathematical Reasoning
    dict(ch='10', scen='ABC minus CBA is 297 with B 8 and digit sum 17',
         stem='ABC and CBA are three-digit numbers. ABC − CBA = 297, the middle digit B is 8 and A + B + C = 17. What is ABC?',
         opts=['683', '386', '593', '674'],
         hint='ABC − CBA = 99(A − C).',
         sol='99(A − C) = 297 gives A − C = 3. A + C = 17 − 8 = 9. So A = 6 and C = 3, and ABC = 683. Check: 683 − 386 = 297.'),
    dict(ch='10', scen='writing 10 as a sum of three different positive whole numbers',
         stem='In how many ways can 10 be written as a sum of three different positive whole numbers, if the order does not matter (1 + 2 + 7 is the same as 7 + 2 + 1)?',
         opts=['4', '8', '6', '36'],
         hint='List them with the numbers in increasing order, a < b < c.',
         sol='Smallest number 1: 1 + 2 + 7, 1 + 3 + 6, 1 + 4 + 5. Smallest number 2: 2 + 3 + 5. Smallest 3 is impossible (3 + 4 + 5 = 12). So there are 4 ways.'),
    dict(ch='10', scen='frog jumping 3 or 5 steps either way · impossible position after 7 jumps',
         stem='A frog starts at 0 on a number line and makes exactly 7 jumps. Each jump is 3 or 5 steps, to the left or to the right. Which of these positions can it NOT be at after the 7 jumps?',
         opts=['0', '1', '3', '35'],
         hint='Each jump is an odd number of steps. What is the parity of the sum of seven odd numbers?',
         sol='Every jump changes the position by an odd number, and 7 odd numbers add to an odd number. So the final position is odd and 0 is impossible. The others can be reached: 35 = 7 × 5; 3 = 3 + 3 + 3 + 3 − 3 − 3 − 3; 1 = 5 + 5 + 5 − 3 − 3 − 3 − 5.'),
    dict(ch='10', scen='branching tree fractal with halving branches · total length after 5 steps',
         fig=drawing(340, 140, tree_steps()),
         stem='A tree is drawn from a 64 cm trunk (step 0). At each step, every branch tip grows two new branches, each half as long as the branch it grows from. Steps 0, 1 and 2 are shown. What is the total length of the drawing after step 5?',
         opts=['384 cm', '128 cm', '2,048 cm', '320 cm'],
         hint='At each step the number of new branches doubles and their length halves.',
         sol='Step k adds 2^k branches, each 64 ÷ 2^k cm long, which is 64 cm in total. The trunk plus 5 steps gives 6 × 64 = 384 cm.'),

    # ---------------- Part 10 · Mixed Problems
    dict(ch='4+10', scen='integers n with n squared minus 20n plus 96 negative',
         stem='For how many whole numbers n is n² − 20n + 96 a negative number?',
         opts=['3', '5', '4', '2'],
         hint='Factorise n² − 20n + 96.',
         sol='n² − 20n + 96 = (n − 8)(n − 12). This is negative only when one factor is negative and the other positive, that is 8 < n < 12. So n = 9, 10 or 11: 3 numbers.'),
    dict(ch='5+10', scen='polygon with 35 diagonals · number of sides',
         stem='A polygon has 35 diagonals. How many sides does it have?',
         opts=['10', '7', '14', '12'],
         hint='An n-sided polygon has n(n − 3) ÷ 2 diagonals.',
         sol='n(n − 3) ÷ 2 = 35, so n(n − 3) = 70. Trying: 10 × 7 = 70. So n = 10.'),
    dict(ch='4+5', scen='square garden with a 2 m path inside its edges of area 176 m²',
         stem='A square garden has a path 2 m wide running round the inside of its edges. The area of the path is 176 m². What is the side of the garden?',
         opts=['24 m', '22 m', '26 m', '20 m'],
         hint='The inner square has side s − 4.',
         sol='Path area = s² − (s − 4)² = 8s − 16 = 176, so 8s = 192 and s = 24 m.'),
    dict(ch='3+9', scen='buy 3 get 1 free plus 10 percent off the bill on 8 items · shop profit',
         stem='A shop offers "buy 3, get 1 free" and then a further 10% off the bill. Bags are marked ₹400 each and cost the shop ₹200 each. A customer takes 8 bags. What percentage profit does the shop make on this sale?',
         opts=['35%', '80%', '44%', '60%'],
         hint='The customer pays for only 6 of the 8 bags.',
         sol='She pays for 6 bags: ₹2,400, then 10% off: ₹2,160. The 8 bags cost the shop ₹1,600. Profit = ₹560, which is 560 ÷ 1,600 = 35%.'),
    dict(ch='6+9', scen='milk can radius 14 cm height 50 cm at ₹56 a litre',
         stem='A cylindrical milk can has inner radius 14 cm and inner height 50 cm. Milk costs ₹56 per litre. What is the value of a full can of milk? (Take π = 22/7.)',
         opts=['₹1,724.80', '₹17,248', '₹172.48', '₹862.40'],
         hint='1 litre = 1,000 cm³.',
         sol='Volume = 22/7 × 14 × 14 × 50 = 30,800 cm³ = 30.8 litres. Value = 30.8 × 56 = ₹1,724.80.'),
]
