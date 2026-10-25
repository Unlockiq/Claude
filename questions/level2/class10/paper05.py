# AMO Level-2 · Class 10 · Practice Paper 5  (format: see paper01.py)
import math


def two_tangents_chord():
    O, r, d = (60, 85), 50, 78
    P = (O[0] + d, O[1])
    phi = math.acos(r / d)
    A = (O[0] + r * math.cos(phi), O[1] - r * math.sin(phi))
    B = (O[0] + r * math.cos(phi), O[1] + r * math.sin(phi))
    return [('circle', O[0], O[1], r, None), ('line', P[0], P[1], A[0], A[1]), ('line', P[0], P[1], B[0], B[1]),
            ('line', O[0], O[1], A[0], A[1], True), ('line', O[0], O[1], B[0], B[1], True), ('line', A[0], A[1], B[0], B[1]),
            ('dot', O[0], O[1], 3), ('text', O[0] - 12, O[1], 'O', 12), ('text', P[0] + 12, P[1], 'P', 12),
            ('text', A[0] + 2, A[1] - 12, 'A', 12), ('text', B[0] + 2, B[1] + 12, 'B', 12), ('text', P[0] - 13, P[1], '80°', 8)]


def square_circle():
    return [('rect', 10, 10, 140, 140, 'yellow'), ('circle', 80, 80, 70, 'white'), ('rect', 30.5, 30.5, 99, 99, 'blue'), ('text', 80, 165, '14 cm', 11)]


QUESTIONS = [
    # ---------------- Part 1 · Number System
    dict(ch='1', scen='Euclid algorithm on 1071 and 462 · HCF and number of divisions',
         stem='Kiara uses Euclid\'s division algorithm to find the HCF of 1071 and 462, stopping when a remainder is 0. What HCF does she get, and how many divisions does she do?',
         opts=['21, in 3 divisions', '21, in 2 divisions', '147, in 2 divisions', '7, in 4 divisions'],
         hint='1071 = 462 × 2 + 147. Continue with 462 and 147.',
         sol='1071 = 462 × 2 + 147; 462 = 147 × 3 + 21; 147 = 21 × 7 + 0. Three divisions, and the last non-zero remainder is 21.'),
    dict(ch='1', scen='which of four surd expressions is irrational',
         stem='Which of these numbers is irrational?',
         opts=['(√5 + √2)²', '(3 + √2)(3 − √2)', '√12 × √3', '√8 × √2'],
         hint='Expand each one.',
         sol='(3 + √2)(3 − √2) = 9 − 2 = 7; √12 × √3 = √36 = 6; √8 × √2 = √16 = 4. But (√5 + √2)² = 7 + 2√10, and √10 is irrational. So only (√5 + √2)² = 7 + 2√10 is irrational.'),

    # ---------------- Part 2 · Fractions, Decimals & Percentages
    dict(ch='3', scen='capital of a partner from a 5 : 3 profit ratio over 8 months',
         stem='Gauri invests ₹50,000 for 12 months. Nikhil invests for only 8 months. They share the profit in the ratio 5 : 3. How much did Nikhil invest?',
         opts=['₹45,000', '₹30,000', '₹40,000', '₹50,000'],
         hint='Profit ratio = ratio of capital × months.',
         sol='50,000 × 12 : C × 8 = 5 : 3. So 8C = 6,00,000 × 3/5 = 3,60,000 and C = ₹45,000. (₹30,000 ignores the months.)'),
    dict(ch='3', scen='CI minus SI is ₹50 for 2 years · difference for 3 years',
         stem='On a certain sum at 10% per annum, the compound interest (compounded yearly) exceeds the simple interest by ₹50 for 2 years. By how much does it exceed it for 3 years?',
         opts=['₹155', '₹150', '₹75', '₹165.50'],
         hint='For 2 years, CI − SI = P × (r/100)². Find P first.',
         sol='P × 0.01 = 50, so P = ₹5,000. For 3 years: CI = 5,000 × (1.331 − 1) = ₹1,655 and SI = ₹1,500. Difference = ₹155. (₹150 simply triples the 2-year gap.)'),
    dict(ch='3', scen='sum amounting to ₹7,200 in 2 years and ₹8,640 in 3 years',
         stem='A sum at compound interest (compounded yearly) amounts to ₹7,200 in 2 years and to ₹8,640 in 3 years. What was the sum?',
         opts=['₹5,000', '₹4,800', '₹6,000', '₹5,760'],
         hint='The 3rd year\'s growth gives the rate.',
         sol='8,640 ÷ 7,200 = 1.2, so the rate is 20%. Sum = 7,200 ÷ 1.2² = 7,200 ÷ 1.44 = ₹5,000. (₹6,000 divides by 1.2 only once.)'),

    # ---------------- Part 3 · Algebra
    dict(ch='4', scen='integer quadratic with a zero 2 + √3 · value of p + q',
         stem='2 + √3 is a zero of x² + px + q, where p and q are integers. What is p + q?',
         opts=['−3', '5', '3', '−5'],
         hint='With integer coefficients, the other zero is 2 − √3.',
         sol='The other zero is 2 − √3. Sum = 4 = −p, so p = −4. Product = 4 − 3 = 1 = q. p + q = −3. (5 uses p = +4.)'),
    dict(ch='4', scen='x plus 1/x equals 3 · value of x⁵ + 1/x⁵',
         stem='If x + 1/x = 3, what is x⁵ + 1/x⁵?',
         opts=['123', '126', '243', '47'],
         hint='Find x² + 1/x² and x³ + 1/x³, then multiply them.',
         sol='x² + 1/x² = 9 − 2 = 7. x³ + 1/x³ = 27 − 3 × 3 = 18. (x² + 1/x²)(x³ + 1/x³) = x⁵ + 1/x⁵ + x + 1/x, so x⁵ + 1/x⁵ = 7 × 18 − 3 = 123. (126 forgets to subtract x + 1/x.)'),
    dict(ch='4', scen='sum of all two-digit odd numbers',
         stem='What is the sum of all the two-digit odd numbers?',
         opts=['2,475', '2,450', '2,500', '4,950'],
         hint='They form an AP 11, 13, …, 99. Count the terms first.',
         sol='Number of terms = (99 − 11)/2 + 1 = 45. Sum = 45/2 × (11 + 99) = 45 × 55 = 2,475. (4,950 forgets to halve: 45 × 110.)'),
    dict(ch='4', scen='two-digit number four times its digit sum that reverses on adding 18',
         stem='A two-digit number is 4 times the sum of its digits. If 18 is added to it, the digits are reversed. What is the number?',
         opts=['24', '42', '36', '48'],
         hint='Let the number be 10a + b.',
         sol='10a + b = 4(a + b) gives 6a = 3b, so b = 2a. 10a + b + 18 = 10b + a gives b − a = 2. So a = 2, b = 4: the number is 24. Check: 24 = 4 × 6 and 24 + 18 = 42.'),

    # ---------------- Part 4 · Geometry
    dict(ch='5', scen='25 m ladder reaching windows on both sides of a street',
         stem='The foot of a 25 m ladder is at a point in a street. Leaning one way, it reaches a window 24 m high. Turned the other way from the same point, it reaches a window 7 m high. How wide is the street?',
         opts=['31 m', '17 m', '24 m', '25 m'],
         hint='Find the distance from the foot of the ladder to each wall.',
         sol='Distance to the first wall = √(25² − 24²) = 7 m. Distance to the second wall = √(25² − 7²) = 24 m. Width = 7 + 24 = 31 m.'),
    dict(ch='5', scen='angle OAB when the tangents from P meet at 80 degrees',
         fig=drawing(160, 170, two_tangents_chord()),
         stem='PA and PB are tangents to a circle with centre O, and angle APB = 80°. What is angle OAB?',
         opts=['40°', '50°', '80°', '100°'],
         hint='OA ⊥ PA and OB ⊥ PB, so angle AOB = 180° − 80°.',
         sol='In quadrilateral OAPB, angles A and B are 90°, so angle AOB = 360° − 180° − 80° = 100°. Triangle OAB is isosceles (OA = OB), so angle OAB = (180° − 100°)/2 = 40°.'),
    dict(ch='5', scen='type of triangle with vertices (1, 1) (5, 4) (8, 0)',
         stem='What kind of triangle has vertices A(1, 1), B(5, 4) and C(8, 0)?',
         opts=['Right-angled and isosceles', 'Equilateral', 'Scalene and acute-angled', 'Obtuse-angled'],
         hint='Find all three side lengths with the distance formula.',
         sol='AB = √(16 + 9) = 5, BC = √(9 + 16) = 5, AC = √(49 + 1) = √50. AB = BC and AB² + BC² = 50 = AC². So it is right-angled (at B) and isosceles.'),

    # ---------------- Part 5 · Mensuration
    dict(ch='6', scen='frustum container with radii 10 and 4 and height 8 · outer area with base',
         stem='An open container is a frustum with top radius 10 cm, bottom radius 4 cm and height 8 cm. What is the area of metal used for its curved surface and its base?',
         opts=['156π cm²', '140π cm²', '256π cm²', '116π cm²'],
         hint='Slant height l = √(h² + (R − r)²). Curved area = π(R + r)l.',
         sol='l = √(64 + 36) = 10 cm. Curved area = π(10 + 4) × 10 = 140π. Base = π × 4² = 16π. Total 156π cm². (256π adds the top, which is open.)'),
    dict(ch='6', scen='three cubes of edges 3 4 5 recast · change in surface area',
         stem='Three metal cubes with edges 3 cm, 4 cm and 5 cm are melted and recast into a single cube. By what percentage does the total surface area change?',
         opts=['28% decrease', '28% increase', '16% decrease', 'No change'],
         hint='Find the edge of the new cube from the total volume.',
         sol='Volume 27 + 64 + 125 = 216 cm³, so the new edge is 6 cm. Old surface area = 6(9 + 16 + 25) = 300 cm². New = 6 × 36 = 216 cm². Decrease = 84/300 = 28%.'),
    dict(ch='6', scen='area between a circle in a 14 cm square and the square inside the circle',
         fig=drawing(160, 175, square_circle()),
         stem='A circle just fits inside a square of side 14 cm. A smaller square is drawn inside the circle with its four corners on the circle. What is the area of the part of the circle outside the smaller square? (Take π = 22/7.)',
         opts=['56 cm²', '42 cm²', '98 cm²', '14 cm²'],
         hint='The diagonal of the small square is a diameter of the circle.',
         sol='The circle has radius 7 cm and area 22/7 × 49 = 154 cm². The small square has diagonal 14 cm, so its area is 14² ÷ 2 = 98 cm². Area between them = 154 − 98 = 56 cm². (42 cm² is the big square minus the circle.)'),

    # ---------------- Part 6 · Trigonometry
    dict(ch='7', scen='sin theta plus cos theta equals 7/5 · tan theta plus cot theta',
         stem='For an acute angle θ, sin θ + cos θ = 7/5. What is tan θ + cot θ?',
         opts=['25/12', '12/25', '7/5', '5/7'],
         hint='Square the given equation and use sin²θ + cos²θ = 1.',
         sol='(sin θ + cos θ)² = 1 + 2 sin θ cos θ = 49/25, so sin θ cos θ = 12/25. tan θ + cot θ = (sin²θ + cos²θ)/(sin θ cos θ) = 1 ÷ (12/25) = 25/12.'),
    dict(ch='7', scen='tower seen at 45 then 60 degrees after walking 20 m closer',
         stem='The angle of elevation of the top of a tower from a point is 45°. After walking 20 m straight towards the tower it is 60°. What is the height of the tower?',
         opts=['10(3 + √3) m', '10√3 m', '20√3 m', '10(3 − √3) m'],
         hint='The two distances from the foot are h and h/√3.',
         sol='h − h/√3 = 20, so h(√3 − 1)/√3 = 20 and h = 20√3/(√3 − 1) = 10√3(√3 + 1) = 10(3 + √3) m (about 47.3 m).'),

    # ---------------- Part 7 · Data Handling, Statistics & Probability
    dict(ch='8', scen='missing frequency when the grouped mean is 24',
         fig=table(['Class', '0–10', '10–20', '20–30', '30–40', '40–50'], [['f', '2', 'f', '5', '3', '3']], widths=[60, 62, 62, 62, 62, 62]),
         stem='The mean of this frequency distribution is 24. What is the missing frequency f?',
         opts=['7', '5', '9', '6'],
         hint='Use class marks 5, 15, 25, 35, 45 and set Σfx/Σf = 24.',
         sol='Σfx = 10 + 15f + 125 + 105 + 135 = 375 + 15f. Σf = 13 + f. 375 + 15f = 24(13 + f) = 312 + 24f, so 9f = 63 and f = 7.'),
    dict(ch='8', scen='four coins with more heads than tails',
         stem='Four fair coins are tossed together. What is the probability that there are more heads than tails?',
         opts=['5/16', '1/2', '11/16', '3/8'],
         hint='More heads than tails means 3 or 4 heads. List the outcomes.',
         sol='There are 2⁴ = 16 equally likely outcomes. 4 heads: 1 way (HHHH). 3 heads: 4 ways (the tail can be any one coin). P = 5/16. (1/2 ignores the 6 outcomes with 2 heads and 2 tails.)'),

    # ---------------- Part 8 · Applied Mathematics
    dict(ch='9', scen='average speed of a boat for a round trip of 32 km each way',
         stem='A boat moves at 12 km/h in still water. The stream flows at 4 km/h. The boat goes 32 km downstream and comes back. What is its average speed for the whole trip?',
         opts=['10 2/3 km/h', '12 km/h', '8 km/h', '11 km/h'],
         hint='Average speed = total distance ÷ total time.',
         sol='Downstream 16 km/h: 2 h. Upstream 8 km/h: 4 h. Average = 64 ÷ 6 = 10 2/3 km/h. (12 km/h averages the two speeds.)'),
    dict(ch='9', scen='restaurant bill with food at 5 percent and drinks at 18 percent GST',
         stem='A restaurant bill has food worth ₹800, taxed at 5% GST, and packaged drinks worth ₹200, taxed at 18% GST. What is the total amount to pay?',
         opts=['₹1,076', '₹1,050', '₹1,180', '₹1,230'],
         hint='Work out the tax on each item at its own rate.',
         sol='GST = 5% of 800 + 18% of 200 = 40 + 36 = ₹76. Total = 1,000 + 76 = ₹1,076. (₹1,050 uses 5% for both; ₹1,180 uses 18% for both.)'),
    dict(ch='9', scen='buying a machine against renting it for five years',
         stem='A tailor can buy a machine for ₹60,000 with ₹2,000 a year for upkeep, or rent one for ₹1,500 a month. Over 5 years, how much does buying save?',
         opts=['₹20,000', '₹30,000', '₹10,000', '₹0'],
         hint='Find the 5-year cost of each plan.',
         sol='Buying: 60,000 + 5 × 2,000 = ₹70,000. Renting: 1,500 × 60 = ₹90,000. Buying saves ₹20,000.'),

    # ---------------- Part 9 · Mathematical Reasoning
    dict(ch='10', scen='students forcing three with the same birth month',
         stem='What is the least number of students in a class that guarantees at least 3 of them were born in the same month?',
         opts=['25', '24', '37', '13'],
         hint='Fill each month with as many students as possible without reaching 3.',
         sol='24 students can be split 2 per month for 12 months. The 25th makes 3 in some month. (13 guarantees only 2.)'),
    dict(ch='10', scen='four-digit numbers from digits 1 to 5 without repetition divisible by 4',
         stem='How many four-digit numbers with all different digits, using only the digits 1, 2, 3, 4 and 5, are divisible by 4?',
         opts=['24', '48', '30', '12'],
         hint='A number is divisible by 4 when its last two digits are.',
         sol='Possible endings with different digits: 12, 24, 32, 52. For each, the first two digits come from the 3 remaining digits in 3 × 2 = 6 ways. 4 × 6 = 24.'),
    dict(ch='10', scen='seven upside-down glasses turned two at a time',
         stem='Seven glasses stand upside down on a table. In each move Varun turns over exactly two glasses. What is the least number of moves needed to make all seven stand upright?',
         opts=['It is impossible', '4 moves', '3 moves', '7 moves'],
         hint='Watch the number of upside-down glasses: is it odd or even after each move?',
         sol='A move changes the number of upside-down glasses by −2, 0 or +2, so it stays odd. It starts at 7 (odd) and can never become 0. It is impossible.'),

    # ---------------- Part 10 · Mixed Problems
    dict(ch='4+10', scen='three numbers in AP with sum 27 and product 504',
         stem='Three numbers are in AP. Their sum is 27 and their product is 504. What is the largest of them?',
         opts=['14', '13', '12', '15'],
         hint='Write them as a − d, a, a + d.',
         sol='3a = 27, so a = 9. (9 − d) × 9 × (9 + d) = 504 gives 81 − d² = 56, so d = 5. The numbers are 4, 9, 14. Largest 14.'),
    dict(ch='5+7', scen='part of a radius-6 circle outside its inscribed equilateral triangle',
         stem='An equilateral triangle is drawn inside a circle of radius 6 cm with all three corners on the circle. What is the area of the part of the circle outside the triangle?',
         opts=['(36π − 27√3) cm²', '(36π − 9√3) cm²', '(36π − 108√3) cm²', '(12π − 9√3) cm²'],
         hint='Each side subtends 120° at the centre. Find a side using sin 60°.',
         sol='Half a side = 6 sin 60° = 3√3, so a side is 6√3 cm. Triangle area = (√3/4) × 108 = 27√3 cm². Circle = 36π cm². Outside = (36π − 27√3) cm².'),
    dict(ch='4+5', scen='line parallel to the base halving the area of a triangle',
         stem='A line parallel to side BC of triangle ABC cuts AB at D and AC at E so that triangle ADE has exactly half the area of triangle ABC. What is AD/AB?',
         opts=['1/√2', '1/2', '1/4', '√2 − 1'],
         hint='The ratio of areas of similar triangles is the square of the ratio of sides.',
         sol='(AD/AB)² = 1/2, so AD/AB = 1/√2 (about 0.71). (1/2 would give only a quarter of the area.)'),
    dict(ch='3+9', scen='yearly SIP of ₹2,000 for three years at 10 percent',
         stem='Sneha invests ₹2,000 at the start of each year for 3 years at 10% per annum compound interest. What is her investment worth at the end of the 3rd year?',
         opts=['₹7,282', '₹6,620', '₹6,000', '₹7,986'],
         hint='The first ₹2,000 grows for 3 years, the second for 2, the third for 1.',
         sol='2,000 × (1.331 + 1.21 + 1.1) = 2,000 × 3.641 = ₹7,282. (₹6,620 counts one year too few for each deposit.)'),
    dict(ch='6+10', scen='empty fraction of a cube holding the largest sphere',
         stem='The largest possible sphere is placed inside a closed cubical box of edge 14 cm. What fraction of the box is empty? (Take π = 22/7.)',
         opts=['10/21', '11/21', '1/2', '3/7'],
         hint='The sphere\'s diameter equals the edge of the cube.',
         sol='Sphere = 4/3 × 22/7 × 7³ = 4,312/3 cm³. Cube = 2,744 cm³. Sphere/cube = 4,312/8,232 = 11/21. Empty = 10/21.'),
]
