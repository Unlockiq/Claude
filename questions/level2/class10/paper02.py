# AMO Level-2 · Class 10 · Practice Paper 2  (format: see paper01.py)


def tri_split(t=0.4):
    A, B, C = (120, 10), (10, 170), (230, 170)
    D = (A[0] + t * (B[0] - A[0]), A[1] + t * (B[1] - A[1]))
    E = (A[0] + t * (C[0] - A[0]), A[1] + t * (C[1] - A[1]))
    return [('poly', [A, B, C], 'white'), ('poly', [A, D, E], 'yellow'), ('line', D[0], D[1], E[0], E[1]),
            ('text', A[0], A[1] - 12, 'A', 12), ('text', B[0] - 10, B[1] + 8, 'B', 12), ('text', C[0] + 10, C[1] + 8, 'C', 12),
            ('text', D[0] - 12, D[1], 'D', 12), ('text', E[0] + 12, E[1], 'E', 12)]


def incircle():
    # triangle with AB = 7, BC = 8, CA = 9 (scaled by 22)
    import math
    s = 22
    B, C = (20, 180), (20 + 8 * s, 180)
    # A from AB = 7, AC = 9
    x = (7 ** 2 - 9 ** 2 + 8 ** 2) / (2 * 8)
    y = math.sqrt(7 ** 2 - x ** 2)
    A = (20 + x * s, 180 - y * s)
    a, b, c = 8, 9, 7
    I = ((a * A[0] + b * B[0] + c * C[0]) / 24, (a * A[1] + b * B[1] + c * C[1]) / 24)
    r = math.sqrt((12 - 8) * (12 - 9) * (12 - 7) / 12) * s
    D = (B[0] + 3 * s, 180)
    return [('poly', [A, B, C], 'white'), ('circle', I[0], I[1], r, 'yellow'), ('dot', D[0], D[1], 3),
            ('text', A[0], A[1] - 12, 'A', 12), ('text', B[0] - 10, B[1] + 8, 'B', 12), ('text', C[0] + 10, C[1] + 8, 'C', 12),
            ('text', D[0], D[1] + 14, 'D', 12), ('text', (A[0] + B[0]) / 2 - 18, (A[1] + B[1]) / 2, '7 cm', 11),
            ('text', (A[0] + C[0]) / 2 + 20, (A[1] + C[1]) / 2, '9 cm', 11), ('line', B[0], 208, C[0], 208), ('line', B[0], 202, B[0], 214), ('line', C[0], 202, C[0], 214), ('text', (B[0] + C[0]) / 2, 222, 'BC = 8 cm', 11)]


QUESTIONS = [
    # ---------------- Part 1 · Number System
    dict(ch='1', scen='largest divisor of 1251 9377 15628 leaving remainders 1 2 3',
         stem='What is the largest number that divides 1251, 9377 and 15628, leaving remainders 1, 2 and 3 respectively?',
         opts=['625', '125', '3125', '250'],
         hint='Subtract each remainder first. The divisor must divide all three results exactly.',
         sol='1251 − 1 = 1250 = 2 × 5⁴, 9377 − 2 = 9375 = 3 × 5⁵, 15628 − 3 = 15625 = 5⁶. HCF = 5⁴ = 625. It is larger than every remainder, as it must be.'),
    dict(ch='1', scen='sum of two numbers with HCF 16 and LCM 384 when one is 48',
         stem='Two numbers have HCF 16 and LCM 384. One of them is 48. What is the sum of the two numbers?',
         opts=['176', '144', '432', '208'],
         hint='For two numbers, HCF × LCM = the product of the numbers.',
         sol='Other number = 16 × 384 ÷ 48 = 128. Check: HCF(48, 128) = 16 and LCM = 384. Sum = 48 + 128 = 176.'),

    # ---------------- Part 2 · Fractions, Decimals & Percentages
    dict(ch='3', scen='sum growing to ₹8,820 in 2 years and ₹9,261 in 3 years',
         stem='At compound interest (compounded yearly), a sum of money becomes ₹8,820 in 2 years and ₹9,261 in 3 years. What is the sum?',
         opts=['₹8,000', '₹8,379', '₹7,938', '₹8,400'],
         hint='The third year turns ₹8,820 into ₹9,261. That gives the rate.',
         sol='9,261 ÷ 8,820 = 1.05, so the rate is 5%. Sum = 8,820 ÷ 1.05² = 8,820 ÷ 1.1025 = ₹8,000.'),
    dict(ch='3', scen='partner withdrawing ₹5,000 after four months',
         stem='Aditi starts a business with ₹20,000 and withdraws ₹5,000 after 4 months. Rahul invests ₹25,000 for the whole year. Out of a year-end profit of ₹21,000, what is Aditi\'s share?',
         opts=['₹8,400', '₹9,333', '₹7,000', '₹12,600'],
         hint='Add capital × months for each period.',
         sol='Aditi: 20,000 × 4 + 15,000 × 8 = 2,00,000. Rahul: 25,000 × 12 = 3,00,000. Ratio 2 : 3. Aditi gets 2/5 × 21,000 = ₹8,400.'),
    dict(ch='3', scen='marked 40 percent above cost then 25 percent discount still earning ₹60',
         stem='A shopkeeper marks an article 40% above its cost price and then gives a discount of 25% on the marked price. He still makes a profit of ₹60. What is the cost price?',
         opts=['₹1,200', '₹400', '₹240', '₹1,260'],
         hint='Take the cost price as ₹100 and find the profit percentage first.',
         sol='On a cost of ₹100: marked ₹140, selling price 75% of 140 = ₹105, profit 5%. 5% of the cost is ₹60, so the cost is ₹1,200. (₹400 takes the profit as 40% − 25% = 15%.)'),

    # ---------------- Part 3 · Algebra
    dict(ch='4', scen='fourth powers of the roots of x² − 3x + 1',
         stem='If α and β are the roots of x² − 3x + 1 = 0, what is α⁴ + β⁴?',
         opts=['47', '49', '45', '81'],
         hint='Find α² + β² first, then square it.',
         sol='α + β = 3 and αβ = 1. α² + β² = 9 − 2 = 7. α⁴ + β⁴ = (α² + β²)² − 2α²β² = 49 − 2 = 47.'),
    dict(ch='4', scen='pen notebook and bag priced in pairs',
         stem='Nakul notices that a pen and a notebook cost ₹50 together, a notebook and a bag cost ₹230, and a bag and a pen cost ₹200. What is the price of the bag?',
         opts=['₹190', '₹180', '₹160', '₹240'],
         hint='Add all three equations.',
         sol='Adding: 2(pen + notebook + bag) = 480, so all three cost ₹240. Bag = 240 − (pen + notebook) = 240 − 50 = ₹190.'),
    dict(ch='4', scen='tenth term when the sum of n terms is 3n² + 5n',
         stem='The sum of the first n terms of an AP is 3n² + 5n. What is its 10th term?',
         opts=['62', '350', '58', '65'],
         hint='The 10th term is S₁₀ − S₉.',
         sol='S₁₀ = 300 + 50 = 350 and S₉ = 243 + 45 = 288. a₁₀ = 350 − 288 = 62. (In general aₙ = 6n + 2.)'),
    dict(ch='4', scen='positive k for equal roots of (k+1)x² − 2(k−1)x + 1',
         stem='For which positive value of k does (k + 1)x² − 2(k − 1)x + 1 = 0 have equal roots?',
         opts=['3', '1', '2', '4'],
         hint='Equal roots: discriminant = 0.',
         sol='4(k − 1)² − 4(k + 1) = 0 gives k² − 3k = 0, so k = 0 or k = 3. The positive value is 3.'),

    # ---------------- Part 4 · Geometry
    dict(ch='5', scen='point on the x-axis equidistant from (−2, 4) and (4, 2)',
         stem='Which point on the x-axis is equidistant from A(−2, 4) and B(4, 2)?',
         opts=['(0, 0)', '(1, 0)', '(2, 0)', '(−1, 0)'],
         hint='Let the point be (x, 0) and equate squared distances.',
         sol='(x + 2)² + 16 = (x − 4)² + 4. So 4x + 20 = −8x + 20, giving x = 0. The point is the origin. Check: both distances are √20.'),
    dict(ch='5', scen='area of small triangle to trapezium when AD : DB = 2 : 3',
         fig=drawing(250, 185, tri_split(0.4)),
         stem='In triangle ABC, DE ∥ BC and AD : DB = 2 : 3. What is the ratio of the area of triangle ADE to the area of trapezium DBCE?',
         opts=['4 : 21', '4 : 25', '2 : 3', '4 : 9'],
         hint='Triangles ADE and ABC are similar with ratio AD : AB.',
         sol='AD : AB = 2 : 5, so areas ADE : ABC = 4 : 25. The trapezium is 25 − 4 = 21 parts. Ratio 4 : 21. (4 : 25 compares with the whole triangle.)'),
    dict(ch='5', scen='incircle touching BC of a 7 8 9 triangle · length BD',
         fig=drawing(220, 230, incircle()),
         stem='The incircle of triangle ABC touches BC at D. If AB = 7 cm, BC = 8 cm and CA = 9 cm, what is BD?',
         opts=['3 cm', '4 cm', '5 cm', '3.5 cm'],
         hint='Tangents from a point to a circle are equal. Call the three tangent lengths x, y, z.',
         sol='Let the tangent lengths from A, B, C be x, y, z. Then x + y = 7, y + z = 8, z + x = 9, so x + y + z = 12. BD = y = 12 − 9 = 3 cm.'),

    # ---------------- Part 5 · Mensuration
    dict(ch='6', scen='surface area of a cone on a hemisphere toy',
         stem='A toy is a cone of radius 3.5 cm mounted on a hemisphere of the same radius. The total height of the toy is 15.5 cm. What is its total surface area? (Take π = 22/7.)',
         opts=['214.5 cm²', '252.5 cm²', '137.5 cm²', '291.5 cm²'],
         hint='Cone height = 15.5 − 3.5. Only curved surfaces are on the outside.',
         sol='Cone height 12 cm, slant √(144 + 12.25) = 12.5 cm. Cone CSA = 22/7 × 3.5 × 12.5 = 137.5. Hemisphere CSA = 2 × 22/7 × 3.5² = 77. Total = 214.5 cm².'),
    dict(ch='6', scen='cone of radius 6 and height 24 recast into spheres of radius 1.5',
         stem='A solid metal cone of base radius 6 cm and height 24 cm is melted and recast into small solid spheres of radius 1.5 cm. How many spheres are made?',
         opts=['64', '48', '16', '192'],
         hint='Divide the volume of the cone by the volume of one sphere.',
         sol='Cone = (1/3)π × 36 × 24 = 288π cm³. One sphere = (4/3)π × 1.5³ = 4.5π cm³. 288 ÷ 4.5 = 64 spheres. (192 forgets the 1/3 in the cone.)'),
    dict(ch='6', scen='major segment minus minor segment for a right-angle chord in radius 14',
         stem='A chord of a circle of radius 14 cm subtends a right angle at the centre. By how much does the area of the major segment exceed that of the minor segment? (Take π = 22/7.)',
         opts=['504 cm²', '462 cm²', '560 cm²', '308 cm²'],
         hint='Find the minor segment, then the major segment = circle − minor segment.',
         sol='Sector = ¼ × 22/7 × 196 = 154 cm²; triangle = ½ × 14 × 14 = 98 cm²; minor segment = 56 cm². Circle = 616 cm², so major segment = 616 − 56 = 560 cm². Difference = 560 − 56 = 504 cm². (462 cm² is the major sector.)'),

    # ---------------- Part 6 · Trigonometry
    dict(ch='7', scen='tan theta = 1/√7 · ratio of cosec² − sec² to cosec² + sec²',
         stem='If tan θ = 1/√7, what is (cosec²θ − sec²θ)/(cosec²θ + sec²θ)?',
         opts=['3/4', '5/7', '1/2', '4/3'],
         hint='cosec²θ = 1 + cot²θ and sec²θ = 1 + tan²θ.',
         sol='cot²θ = 7, so cosec²θ = 8. tan²θ = 1/7, so sec²θ = 8/7. Ratio = (8 − 8/7)/(8 + 8/7) = (48/7)/(64/7) = 3/4.'),
    dict(ch='7', scen='depression angles of 30 and 60 degrees from a 60 m building to a tower',
         stem='From the top of a 60 m building, the angles of depression of the top and bottom of a tower are 30° and 60°. What is the height of the tower?',
         opts=['40 m', '20 m', '30 m', '20√3 m'],
         hint='Find the distance between the buildings from the 60° angle first.',
         sol='Distance = 60/tan 60° = 20√3 m. The top of the tower is lower than the building by 20√3 × tan 30° = 20 m. Tower = 60 − 20 = 40 m.'),

    # ---------------- Part 7 · Data Handling, Statistics & Probability
    dict(ch='8', scen='mean of a grouped table 0 to 100 with frequencies 7 8 12 13 10',
         fig=table(['Class', '0–20', '20–40', '40–60', '60–80', '80–100'], [['Frequency', '7', '8', '12', '13', '10']], widths=[86, 62, 62, 62, 62, 66]),
         stem='What is the mean of this frequency distribution?',
         opts=['54.4', '50', '56.2', '52.8'],
         hint='Use class marks 10, 30, 50, 70, 90 (or step deviations from 50).',
         sol='Step deviations from 50 with h = 20: −2, −1, 0, 1, 2. Σfu = −14 − 8 + 0 + 13 + 20 = 11. Mean = 50 + (11/50) × 20 = 54.4.'),
    dict(ch='8', scen='card from 1 to 50 that is a multiple of 3 or 5',
         stem='A card is drawn at random from 50 cards numbered 1 to 50. What is the probability that its number is a multiple of 3 or of 5?',
         opts=['23/50', '13/25', '1/2', '21/50'],
         hint='Do not count multiples of 15 twice.',
         sol='Multiples of 3: 16. Multiples of 5: 10. Multiples of 15: 3. Total 16 + 10 − 3 = 23. Probability 23/50. (26/50 counts 15, 30, 45 twice.)'),

    # ---------------- Part 8 · Applied Mathematics
    dict(ch='9', scen='successive discounts of 20 and 10 against a single 30 percent',
         stem='An article is marked ₹2,500. Shop P gives successive discounts of 20% and 10%. Shop Q gives a single discount of 30%. How much more does a buyer pay at shop P?',
         opts=['₹50', '₹0', '₹75', '₹25'],
         hint='Successive discounts multiply: 0.8 × 0.9.',
         sol='Shop P: 2,500 × 0.8 × 0.9 = ₹1,800. Shop Q: 2,500 × 0.7 = ₹1,750. P costs ₹50 more. (The effective discount at P is 28%, not 30%.)'),
    dict(ch='9', scen='loan repaid ₹2,000 a month with 1 percent monthly interest on the balance',
         stem='Kartik borrows ₹10,000 at 12% per annum. Each month he pays ₹2,000 of the loan plus 1% interest on the amount still owed that month. How much interest does he pay in all?',
         opts=['₹300', '₹600', '₹500', '₹1,200'],
         hint='The balances on which interest is charged are ₹10,000, ₹8,000, … .',
         sol='Interest = 1% of (10,000 + 8,000 + 6,000 + 4,000 + 2,000) = 1% of 30,000 = ₹300. (₹600 charges interest on the full ₹10,000 every month.)'),
    dict(ch='9', scen='lamps needed for a ₹12,000 profit at two selling prices',
         stem='A factory has fixed costs of ₹36,000 a month, and each lamp costs ₹45 to make. To earn a profit of ₹12,000 a month, how many fewer lamps must it sell at ₹65 each than at ₹60 each?',
         opts=['800', '600', '1,000', '400'],
         hint='Lamps needed = (fixed costs + target profit) ÷ (price − cost per lamp).',
         sol='Needed per month: 36,000 + 12,000 = ₹48,000 of contribution. At ₹60 each, contribution ₹15: 48,000 ÷ 15 = 3,200 lamps. At ₹65, contribution ₹20: 2,400 lamps. Difference 800.'),

    # ---------------- Part 9 · Mathematical Reasoning
    dict(ch='10', scen='numbers from 1 to 20 forcing a pair that adds to 21',
         stem='What is the least number of different numbers that must be chosen from 1 to 20 so that two of them are certain to add up to 21?',
         opts=['11', '10', '12', '21'],
         hint='Group the numbers into pairs that add up to 21.',
         sol='The pairs (1, 20), (2, 19), …, (10, 11) make 10 boxes. With 10 numbers you can take one from each pair and avoid 21. An 11th number must complete a pair. So 11.'),
    dict(ch='10', scen='rectangles in a 4 by 3 grid of squares',
         fig=grid([[''] * 4 for _ in range(3)], cell=34),
         stem='How many rectangles of all sizes (squares included) are there in this 4 by 3 grid?',
         opts=['60', '30', '72', '50'],
         hint='A rectangle is fixed by choosing 2 of the vertical lines and 2 of the horizontal lines.',
         sol='A rectangle is fixed by choosing 2 of the 5 vertical lines and 2 of the 4 horizontal lines. Pairs of vertical lines: the first line pairs with 4 others, the second with 3 more, and so on: 4 + 3 + 2 + 1 = 10. Pairs of horizontal lines: 3 + 2 + 1 = 6. Rectangles = 10 × 6 = 60.'),
    dict(ch='10', scen='five different positive integers adding to 100 with the largest possible smallest',
         stem='Five different positive integers add up to 100. What is the greatest possible value of the smallest of them?',
         opts=['18', '20', '19', '17'],
         hint='If the smallest is a, the total is at least a + (a + 1) + (a + 2) + (a + 3) + (a + 4).',
         sol='5a + 10 ≤ 100 gives a ≤ 18. a = 18 works: 18 + 19 + 20 + 21 + 22 = 100. So 18. (20 would need all five equal.)'),

    # ---------------- Part 10 · Mixed Problems
    dict(ch='4+10', scen='positive integer solutions of x² − y² = 45',
         stem='How many pairs of positive integers (x, y) satisfy x² − y² = 45?',
         opts=['3', '2', '4', '6'],
         hint='x² − y² = (x − y)(x + y). Both factors must be odd here.',
         sol='45 = 1 × 45 = 3 × 15 = 5 × 9 with x − y < x + y. These give (x, y) = (23, 22), (9, 6) and (7, 2). So 3 pairs.'),
    dict(ch='5+7', scen='altitude to the hypotenuse when AB is 6 and angle A is 60 degrees',
         stem='In triangle ABC, angle B = 90°, angle A = 60° and AB = 6 cm. BD is drawn perpendicular to AC. What is the length of BD?',
         opts=['3√3 cm', '3 cm', '6√3 cm', '2√3 cm'],
         hint='Look at the right triangle ABD.',
         sol='Triangle ABD is right-angled at D with angle A = 60°. BD = AB sin 60° = 6 × √3/2 = 3√3 cm.'),
    dict(ch='4+5', scen='parallelogram A(1, 2) B(4, y) C(x, 6) D(3, 5) · find x + y',
         stem='A(1, 2), B(4, y), C(x, 6) and D(3, 5) are the vertices of parallelogram ABCD, in order. What is x + y?',
         opts=['9', '8', '10', '11'],
         hint='The diagonals of a parallelogram bisect each other.',
         sol='Midpoint of AC = midpoint of BD. (1 + x)/2 = (4 + 3)/2 gives x = 6. (2 + 6)/2 = (y + 5)/2 gives y = 3. x + y = 9.'),
    dict(ch='3+9', scen='monthly deposit of ₹1,000 for three months at 1 percent a month',
         stem='Tanvi deposits ₹1,000 at the start of each month for 3 months, at 12% per annum compounded monthly. What is the value of her deposits at the end of the 3rd month?',
         opts=['₹3,060.40', '₹3,030.00', '₹3,000.00', '₹3,090.90'],
         hint='12% per annum is 1% per month. The first deposit grows for 3 months, the last for 1.',
         sol='Value = 1,000 × (1.01³ + 1.01² + 1.01) = 1,000 × (1.030301 + 1.0201 + 1.01) = ₹3,060.40 (to the nearest paisa).'),
    dict(ch='6+10', scen='3 cm cubes cut from a 10 by 8 by 7 block · volume wasted',
         stem='Whole cubes of edge 3 cm are cut from a solid block 10 cm × 8 cm × 7 cm, as many as possible. How much of the block (in cm³) is left over?',
         opts=['236 cm³', '20 cm³', '0 cm³', '56 cm³'],
         hint='Along each edge, only whole cubes fit. Turning the cubes does not help, since they are cubes.',
         sol='Along the edges: 10 ÷ 3 gives 3 cubes, 8 ÷ 3 gives 2, 7 ÷ 3 gives 2. So at most 3 × 2 × 2 = 12 cubes = 324 cm³. Block = 560 cm³. Left over = 560 − 324 = 236 cm³. (20 cm³ assumes 560 ÷ 27 ≈ 20 cubes fit.)'),
]
