# AMO Level-2 · Class 8 · Practice Paper 2
# Each question: ch, scen (unique), stem, opts (correct FIRST), hint, sol, optional fig.


def pie(sectors, r=70, cx=90, cy=85):
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


def carpet_steps():
    prims = []
    for k, x0 in enumerate((10, 150)):
        s = 108
        prims.append(('rect', x0, 10, s, s, 'green'))
        prims.append(('rect', x0 + s / 3, 10 + s / 3, s / 3, s / 3, 'white'))
        if k == 1:
            for i in range(3):
                for j in range(3):
                    if (i, j) != (1, 1):
                        prims.append(('rect', x0 + i * s / 3 + s / 9, 10 + j * s / 3 + s / 9, s / 9, s / 9, 'white'))
        prims.append(('text', x0 + s / 2, 132, f'Step {k + 1}', 11))
    return prims


NET = [[None, '1', None], ['2', '3', '4'], [None, '5', None], [None, '6', None]]


QUESTIONS = [
    # ---------------- Part 1 · Number System
    dict(ch='1', scen='smallest multiplier making 108 a perfect cube and its cube root',
         stem='Arjun multiplies 108 by the smallest whole number that makes it a perfect cube. What is that multiplier, and what is the cube root of the result?',
         opts=['2 and 6', '4 and 6', '2 and 12', '3 and 9'],
         hint='Write 108 as a product of primes and look at each power.',
         sol='108 = 2² × 3³. The factor 2 needs one more 2 to make 2³. So multiply by 2: 216 = 2³ × 3³ = 6³. The multiplier is 2 and the cube root is 6.'),
    dict(ch='1', scen='rational number between root 5 and root 8',
         stem='Which of these is a rational number lying between √5 and √8?',
         opts=['2.5', '2.2', '2.9', '√6'],
         hint='Compare squares: a number lies between √5 and √8 if its square lies between 5 and 8.',
         sol='2.5² = 6.25, which is between 5 and 8, and 2.5 is rational. 2.2² = 4.84 is too small and 2.9² = 8.41 is too large. √6 lies between them but is irrational.'),

    # ---------------- Part 2 · Operations
    dict(ch='2', scen='inverse of sum of reciprocals of 2 and 3 divided by inverse of difference of reciprocals of 4 and 5',
         stem='Find the value of (2⁻¹ + 3⁻¹)⁻¹ ÷ (4⁻¹ − 5⁻¹)⁻¹.',
         opts=['3/50', '24', '50/3', '6/5'],
         hint='Work inside each bracket first, then take the reciprocal.',
         sol='2⁻¹ + 3⁻¹ = 1/2 + 1/3 = 5/6, so its inverse is 6/5. 4⁻¹ − 5⁻¹ = 1/4 − 1/5 = 1/20, so its inverse is 20. 6/5 ÷ 20 = 6/100 = 3/50.'),
    dict(ch='2', scen='bacteria 2.5 times 10 to the minus 6 m long laid end to end to make 1 cm',
         stem='A bacterium is 2.5 × 10⁻⁶ m long. How many such bacteria, placed end to end, make a line 1 cm long?',
         opts=['4 × 10³', '4 × 10⁴', '2.5 × 10⁴', '4 × 10²'],
         hint='1 cm = 10⁻² m.',
         sol='Number = 10⁻² ÷ (2.5 × 10⁻⁶) = (1 ÷ 2.5) × 10⁴ = 0.4 × 10⁴ = 4 × 10³.'),

    # ---------------- Part 3 · Fractions, Decimals & Percentages
    dict(ch='3', scen='single discount equal to 25 then 20 then 10 percent',
         stem='A shop gives three successive discounts of 25%, 20% and 10%. What single discount has the same effect?',
         opts=['46%', '55%', '50%', '54%'],
         hint='Multiply what is left after each discount: 0.75 × 0.8 × 0.9.',
         sol='0.75 × 0.8 = 0.6 and 0.6 × 0.9 = 0.54. The buyer pays 54% of the marked price, so the single discount is 46%. (55% just adds the three.)'),
    dict(ch='3', scen='amount ₹9,800 in 3 years and ₹11,000 in 5 years · rate',
         stem='At simple interest, a sum amounts to ₹9,800 in 3 years and to ₹11,000 in 5 years. What is the rate of interest per year?',
         opts=['7.5%', '6%', '8%', '10%'],
         hint='The extra amount for the two extra years is two years of interest.',
         sol='Interest for 2 years = 11,000 − 9,800 = ₹1,200, so ₹600 a year. 3 years of interest = ₹1,800, so the sum = 9,800 − 1,800 = ₹8,000. Rate = 600 ÷ 8,000 × 100 = 7.5%.'),
    dict(ch='3', scen='town population up 10 then down 10 percent to 39,600',
         stem='The population of a town rose by 10% one year and fell by 10% the next. It is now 39,600. What was it two years ago?',
         opts=['40,000', '39,600', '36,000', '44,000'],
         hint='A 10% rise then a 10% fall multiplies by 1.1 × 0.9.',
         sol='1.1 × 0.9 = 0.99, so the population is 99% of the original. Original = 39,600 ÷ 0.99 = 40,000.'),

    # ---------------- Part 4 · Algebra
    dict(ch='4', scen='x minus 1 over x equals 3 · x squared plus 1 over x squared',
         stem='If x − 1/x = 3, what is x² + 1/x²?',
         opts=['11', '9', '7', '13'],
         hint='Square both sides of x − 1/x = 3.',
         sol='(x − 1/x)² = x² − 2 + 1/x² = 9. So x² + 1/x² = 9 + 2 = 11.'),
    dict(ch='4', scen='598 times 602 by difference of squares',
         stem='Using an identity, find 598 × 602.',
         opts=['3,59,996', '3,60,004', '3,59,604', '3,60,000'],
         hint='598 = 600 − 2 and 602 = 600 + 2.',
         sol='598 × 602 = (600 − 2)(600 + 2) = 600² − 2² = 3,60,000 − 4 = 3,59,996.'),
    dict(ch='4', scen='30 coins of ₹2 and ₹5 worth ₹102',
         stem='Leena has 30 coins, all ₹2 or ₹5, worth ₹102 in all. How many ₹5 coins does she have?',
         opts=['14', '16', '12', '18'],
         hint='Let the number of ₹5 coins be x.',
         sol='₹5 coins: x; ₹2 coins: 30 − x. 5x + 2(30 − x) = 102 gives 3x + 60 = 102, so x = 14. Check: 14 × 5 + 16 × 2 = 70 + 32 = 102.'),

    # ---------------- Part 5 · Geometry
    dict(ch='5', scen='parallelogram angle A is 30 less than twice angle B · angle C',
         stem='In parallelogram ABCD, angle A is 30° less than twice angle B. What is angle C?',
         opts=['110°', '70°', '100°', '80°'],
         hint='Adjacent angles of a parallelogram add to 180°; opposite angles are equal.',
         sol='A + B = 180° and A = 2B − 30°, so 3B − 30° = 180°, B = 70° and A = 110°. Angle C is opposite angle A, so C = 110°.'),
    dict(ch='5', scen='polyhedron with 12 vertices and 30 edges · faces',
         stem='A polyhedron has 12 vertices and 30 edges. Using Euler\'s formula, how many faces does it have?',
         opts=['20', '18', '12', '22'],
         hint='F + V − E = 2.',
         sol='F = 2 − V + E = 2 − 12 + 30 = 20. (This is the icosahedron: 20 triangles give 20 × 3 ÷ 2 = 30 edges.)'),
    dict(ch='5', scen='cube net numbered 1 to 6 · sum of faces opposite 1 2 and 3',
         fig=grid(NET, cell=40),
         stem='This net is folded into a cube. What is the sum of the numbers on the faces opposite the faces 1, 2 and 3?',
         opts=['15', '12', '9', '18'],
         hint='In a straight strip of the net, faces with one square between them are opposite.',
         sol='In the column 1, 3, 5, 6: 1 is opposite 5 and 3 is opposite 6. In the row 2, 3, 4: 2 is opposite 4. The sum is 5 + 4 + 6 = 15.'),

    # ---------------- Part 6 · Mensuration
    dict(ch='6', scen='water from a cylinder poured into cones of half the height',
         stem='A cylinder of radius 3 cm and height 14 cm is full of water. The water is poured into cones of radius 3 cm and height 7 cm. How many cones can be filled exactly?',
         opts=['6', '3', '2', '12'],
         hint='A cone holds one third of a cylinder with the same base and height.',
         sol='A cone of height 7 holds (1/3)πr² × 7. The cylinder holds πr² × 14 = 6 × (1/3)πr² × 7. So it fills 6 cones.'),
    dict(ch='6', scen='solid cylinder radius 14 height 5 topped by a cone of height 48 · outer surface',
         stem='A solid is made of a cylinder (radius 14 cm, height 5 cm) with a cone of the same radius and height 48 cm on top. What is the total outer surface area, including the flat base? (Take π = 22/7.)',
         opts=['3,256 cm²', '3,872 cm²', '2,640 cm²', '2,816 cm²'],
         hint='Add the base circle, the cylinder\'s curved surface and the cone\'s curved surface. Find the slant height first.',
         sol='Slant height = √(14² + 48²) = √2,500 = 50 cm. Cone curved surface = 22/7 × 14 × 50 = 2,200 cm². Cylinder curved surface = 2 × 22/7 × 14 × 5 = 440 cm². Base = 22/7 × 14 × 14 = 616 cm². Total = 2,200 + 440 + 616 = 3,256 cm².'),
    dict(ch='6', scen='2 cm of rain on a field 1.2 km by 500 m · litres in standard form',
         stem='Rain 2 cm deep falls on a field 1.2 km long and 500 m wide. How many litres of rain water fall on the field, in standard form?',
         opts=['1.2 × 10⁷ L', '1.2 × 10⁴ L', '1.2 × 10⁶ L', '6 × 10⁵ L'],
         hint='Work in metres: 2 cm = 0.02 m, and 1 m³ = 1,000 L.',
         sol='Area = 1,200 × 500 = 6,00,000 m². Volume = 6,00,000 × 0.02 = 12,000 m³ = 1,20,00,000 L = 1.2 × 10⁷ L.'),

    # ---------------- Part 7 · Data Handling
    dict(ch='8', scen='pie chart of a ₹36,000 budget · food minus savings',
         fig=drawing(250, 180, pie([('Food', 120), ('Rent', 90), ('Education', 72), ('Savings', 30), ('Others', 48)])),
         stem='The pie chart shows how a family spends its monthly income of ₹36,000. How much more is spent on food than is saved?',
         opts=['₹9,000', '₹12,000', '₹3,000', '₹10,800'],
         hint='Each degree stands for 36,000 ÷ 360 rupees.',
         sol='Each degree is ₹100. Food − savings = 120° − 30° = 90°, which is ₹9,000.'),
    dict(ch='8', scen='mean 15 of seven numbers with one unknown · median and mode',
         stem='The mean of 12, 15, x, 9, 20, 18 and 11 is 15. What are the median and the mode of the seven numbers?',
         opts=['Median 15, mode 20', 'Median 18, mode 20', 'Median 15, mode 18', 'Median 15, no mode'],
         hint='Find x from the total first.',
         sol='Total = 7 × 15 = 105, and the six known numbers add to 85, so x = 20. In order: 9, 11, 12, 15, 18, 20, 20. Median = 15 (the 4th), mode = 20.'),

    # ---------------- Part 8 · Applied Mathematics
    dict(ch='9', scen='selling 33 m of cloth gains the selling price of 11 m',
         stem='By selling 33 m of cloth, a shopkeeper gains the selling price of 11 m. What is his gain percent?',
         opts=['50%', '33%', '25%', '100%'],
         hint='Gain = SP of 33 m − CP of 33 m.',
         sol='SP(33 m) − CP(33 m) = SP(11 m), so CP(33 m) = SP(22 m). Gain = SP(11 m) on a cost of SP(22 m), which is 11/22 = 50%.'),
    dict(ch='9', scen='two sums differing by ₹3,000 earning equal interest at 8 and 10 percent',
         stem='Two sums of money differ by ₹3,000. The larger earns 8% simple interest and the smaller earns 10%, and in one year both earn the same interest. What is the larger sum?',
         opts=['₹15,000', '₹12,000', '₹18,000', '₹13,500'],
         hint='Let the larger sum be x; then 8% of x = 10% of (x − 3,000).',
         sol='0.08x = 0.1(x − 3,000) gives 0.02x = 300, so x = ₹15,000. Check: 8% of 15,000 = 1,200 = 10% of 12,000.'),
    dict(ch='9', scen='shopkeeper using a 900 g weight for 1 kg at cost price',
         stem='A dishonest shopkeeper claims to sell rice at cost price but uses a 900 g weight in place of 1 kg. What is his gain percent?',
         opts=['11 1/9%', '10%', '9 1/11%', '11%'],
         hint='He receives the price of 1,000 g for 900 g.',
         sol='He gives 900 g but charges for 1,000 g, gaining 100 g on a cost of 900 g. Gain = 100/900 × 100 = 11 1/9%. (10% wrongly divides by 1,000.)'),

    # ---------------- Part 9 · Mathematical Reasoning
    dict(ch='10', scen='ABC plus ABC plus ABC equals BBB',
         stem='In the sum ABC + ABC + ABC = BBB, each letter is a different digit. What is A + B + C?',
         opts=['13', '12', '14', '16'],
         hint='BBB = 111 × B = 3 × 37 × B, so ABC = 37 × B.',
         sol='3 × ABC = 111 × B, so ABC = 37 × B. Its tens digit must be B: 37 × 4 = 148 works (37 × 1 = 37, × 2 = 74, × 3 = 111, × 5 = 185 … do not). So ABC = 148, BBB = 444, and A + B + C = 1 + 4 + 8 = 13.'),
    dict(ch='10', scen='ways to pay ₹50 with ₹2 and ₹5 coins using both',
         stem='In how many ways can ₹50 be paid using only ₹2 and ₹5 coins, with at least one coin of each kind?',
         opts=['4', '5', '6', '3'],
         hint='The number of ₹5 coins must be even. Why?',
         sol='The ₹2 coins make an even amount, so the ₹5 coins must also make an even amount: 2, 4, 6 or 8 coins (10 coins would leave no ₹2 coins). That gives 20, 15, 10 or 5 coins of ₹2: 4 ways.'),
    dict(ch='10', scen='23a4b divisible by 72 with nonzero digits · product a times b',
         stem='The five-digit number 23a4b, where a and b are non-zero digits, is divisible by 72. What is a × b?',
         opts=['20', '18', '24', '14'],
         hint='72 = 8 × 9. Use the tests for 8 and 9.',
         sol='Divisible by 9: 2 + 3 + a + 4 + b = 9 + a + b, so a + b = 9 or 18. Divisible by 8: the last three digits a4b must be a multiple of 8. a + b = 18 gives 949, not a multiple of 8. Trying a + b = 9: 544 = 8 × 68 works (a = 5, b = 4); 148, 247, 346, 643, 742, 841 and 940 do not (b = 0 is not allowed). So a × b = 20. Check: 23,544 = 72 × 327.'),
    dict(ch='10', scen='Sierpinski carpet holes after step 3',
         fig=drawing(260, 140, carpet_steps()),
         stem='A square is cut into 9 equal squares and the middle one is removed (step 1). At each later step, every remaining small square is treated the same way. Steps 1 and 2 are shown. How many holes are there after step 3?',
         opts=['73', '64', '81', '72'],
         hint='Each step adds one hole in every square left from the step before.',
         sol='Step 1: 1 hole, 8 squares left. Step 2 adds 8 holes (total 9), leaving 64 squares. Step 3 adds 64 holes: 9 + 64 = 73.'),

    # ---------------- Part 10 · Mixed Problems
    dict(ch='4+10', scen='x plus 1 over x is 5 · x to the fourth plus 1 over x to the fourth',
         stem='If x + 1/x = 5, what is x⁴ + 1/x⁴?',
         opts=['527', '529', '625', '623'],
         hint='Square twice, subtracting 2 each time.',
         sol='x² + 1/x² = 5² − 2 = 23. x⁴ + 1/x⁴ = 23² − 2 = 529 − 2 = 527.'),
    dict(ch='5+10', scen='diagonals of a 12-sided polygon',
         stem='How many diagonals does a 12-sided polygon have?',
         opts=['54', '66', '108', '48'],
         hint='From each corner, diagonals go to every corner except itself and its two neighbours.',
         sol='Each of the 12 corners joins to 12 − 3 = 9 others by a diagonal: 12 × 9 = 108. Each diagonal is counted twice, so there are 54. (66 also counts the 12 sides.)'),
    dict(ch='4+5', scen='square side increased by 3 cm raising area by 81 cm²',
         stem='When the side of a square is increased by 3 cm, its area increases by 81 cm². What was the original side?',
         opts=['12 cm', '9 cm', '13.5 cm', '15 cm'],
         hint='(s + 3)² − s² = 6s + 9.',
         sol='(s + 3)² − s² = 6s + 9 = 81, so 6s = 72 and s = 12 cm. Check: 15² − 12² = 225 − 144 = 81.'),
    dict(ch='3+9', scen='marked ₹1,200 with successive 10 and 5 percent off giving 14 percent profit · cost',
         stem='An article marked ₹1,200 is sold after successive discounts of 10% and 5%. The seller still makes a profit of 14%. What did the article cost the seller?',
         opts=['₹900', '₹1,000', '₹880', '₹950'],
         hint='Find the selling price first, then divide by 1.14.',
         sol='Selling price = 1,200 × 0.9 × 0.95 = 1,080 × 0.95 = ₹1,026. Cost = 1,026 ÷ 1.14 = ₹900.'),
    dict(ch='6+9', scen='conical tent radius 6 m height 8 m · canvas 3 m wide at ₹50 a metre',
         stem='A conical tent has base radius 6 m and height 8 m. It is made of canvas 3 m wide that costs ₹50 per metre of length. What does the canvas cost? (Take π = 3.14.)',
         opts=['₹3,140', '₹9,420', '₹2,512', '₹1,570'],
         hint='Canvas area = curved surface = πrl. Length = area ÷ width.',
         sol='Slant height = √(36 + 64) = 10 m. Curved surface = 3.14 × 6 × 10 = 188.4 m². Length = 188.4 ÷ 3 = 62.8 m. Cost = 62.8 × 50 = ₹3,140.'),
]
