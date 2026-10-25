# AMO Level-2 · Class 10 · Practice Paper 10  (format: see paper01.py)


def trapezium_ef():
    A, B, C, D = (60, 20), (200, 20), (240, 160), (20, 160)
    t = 0.4
    E = (A[0] + t * (D[0] - A[0]), A[1] + t * (D[1] - A[1]))
    F = (B[0] + t * (C[0] - B[0]), B[1] + t * (C[1] - B[1]))
    return [('poly', [A, B, C, D], 'white'), ('line', E[0], E[1], F[0], F[1]),
            ('text', A[0] - 8, A[1] - 10, 'A', 12), ('text', B[0] + 8, B[1] - 10, 'B', 12), ('text', C[0] + 10, C[1] + 8, 'C', 12),
            ('text', D[0] - 10, D[1] + 8, 'D', 12), ('text', E[0] - 12, E[1], 'E', 12), ('text', F[0] + 12, F[1], 'F', 12),
            ('text', 38, 44, '4', 11), ('text', 26, 120, '6', 11), ('text', 224, 44, '5', 11)]


def incircle_given():
    import math
    s = 11
    B, C = (20, 180), (20 + 14 * s, 180)
    x = (15 ** 2 - 13 ** 2 + 14 ** 2) / (2 * 14)
    y = math.sqrt(15 ** 2 - x ** 2)
    A = (20 + x * s, 180 - y * s)
    I = (20 + 8 * s, 180 - 4 * s)
    D = (20 + 8 * s, 180)
    return [('poly', [A, B, C], 'white'), ('circle', I[0], I[1], 4 * s, 'yellow'), ('dot', D[0], D[1], 3),
            ('line', I[0], I[1], D[0], D[1], True),
            ('text', A[0], A[1] - 12, 'A', 12), ('text', B[0] - 10, B[1] + 8, 'B', 12), ('text', C[0] + 10, C[1] + 8, 'C', 12),
            ('text', D[0], D[1] + 14, 'D', 12), ('text', (B[0] + D[0]) / 2, 194, '8 cm', 11), ('text', (D[0] + C[0]) / 2, 194, '6 cm', 11),
            ('text', I[0] + 12, I[1] + 22, '4', 11)]


QUESTIONS = [
    # ---------------- Part 1 · Number System
    dict(ch='1', scen='HCF of 2¹² − 1 and 2⁸ − 1',
         stem='What is the HCF of 2¹² − 1 and 2⁸ − 1?',
         opts=['15', '255', '3', '1'],
         hint='2¹² − 1 = 4095 and 2⁸ − 1 = 255. Use Euclid\'s division algorithm.',
         sol='4095 = 255 × 16 + 15 and 255 = 15 × 17 + 0. So the HCF is 15 = 2⁴ − 1. (In general HCF(2ᵐ − 1, 2ⁿ − 1) = 2^HCF(m, n) − 1.)'),
    dict(ch='1', scen='whether 12 to the power n can end in zero',
         stem='For which natural numbers n does 12ⁿ end with the digit 0?',
         opts=['For no n', 'Only n = 5', 'Every even n', 'Every n ≥ 10'],
         hint='A number ending in 0 has 5 as a prime factor.',
         sol='12ⁿ = 2²ⁿ × 3ⁿ. By the Fundamental Theorem of Arithmetic this factorisation is unique and has no 5, so 12ⁿ never ends in 0.'),

    # ---------------- Part 2 · Fractions, Decimals & Percentages
    dict(ch='3', scen='₹10,000 split between 10 and 20 percent compound giving ₹3,480 interest',
         stem='Ashwin splits ₹10,000 into two parts. One part earns 10% and the other 20% per annum, both compounded yearly. After 2 years the total interest is ₹3,480. How much was invested at 20%?',
         opts=['₹6,000', '₹4,000', '₹5,000', '₹7,000'],
         hint='2-year interest factors: 0.21 at 10% and 0.44 at 20%.',
         sol='If x is at 10%: 0.21x + 0.44(10,000 − x) = 3,480, so 4,400 − 0.23x = 3,480 and x = 4,000. At 20%: ₹6,000.'),
    dict(ch='3', scen='capital ratio from a 1 : 2 : 3 profit ratio over 6 8 and 12 months',
         stem='Three partners invested for 6, 8 and 12 months and shared the profit in the ratio 1 : 2 : 3. In what ratio were their capitals?',
         opts=['2 : 3 : 3', '1 : 2 : 3', '3 : 2 : 2', '6 : 8 : 12'],
         hint='Capital = profit share ÷ time.',
         sol='Capitals are 1/6 : 2/8 : 3/12 = 1/6 : 1/4 : 1/4. Multiply by 12: 2 : 3 : 3.'),
    dict(ch='3', scen='900 g weight used for a kilogram with a 10 percent markup',
         stem='A dishonest grocer uses a 900 g weight in place of 1 kg, and also charges 10% above the cost price. What is his real gain percent?',
         opts=['22 2/9%', '20%', '10%', '11 1/9%'],
         hint='He gives 900 g but charges 1.1 times the cost of 1,000 g.',
         sol='Gain factor = 1.1 × 1000/900 = 11/9. Gain = 2/9 = 22 2/9%. (20% just adds 10% and 10%.)'),

    # ---------------- Part 3 · Algebra
    dict(ch='4', scen='difference of the zeros of x² + x − 6',
         stem='α and β are the zeros of x² + x − 6, with α > β. What is α − β?',
         opts=['5', '1', '25', '7'],
         hint='(α − β)² = (α + β)² − 4αβ.',
         sol='(α − β)² = 1 + 24 = 25, so α − β = 5. (The zeros are 2 and −3.)'),
    dict(ch='4', scen='reducible pair in 1/(x + y) and 1/(x − y) · product xy',
         stem='If 1/(x + y) + 2/(x − y) = 1 and 2/(x + y) − 1/(x − y) = 3/4, what is xy?',
         opts=['−3', '3', '2', '−2'],
         hint='Put u = 1/(x + y) and v = 1/(x − y).',
         sol='u + 2v = 1 and 2u − v = 3/4 give u = 1/2, v = 1/4. So x + y = 2 and x − y = 4, giving x = 3, y = −1. xy = −3.'),
    dict(ch='4', scen='sum of numbers below 100 that are multiples of 3 or 5',
         stem='What is the sum of all natural numbers less than 100 that are multiples of 3 or of 5?',
         opts=['2,318', '2,633', '2,418', '2,003'],
         hint='Add the multiples of 3 and of 5, then subtract the multiples of 15.',
         sol='Multiples of 3: 3 + … + 99 = 33 × 51 = 1,683. Of 5: 5 + … + 95 = 19 × 50 = 950. Of 15: 15 + … + 90 = 6 × 52.5 = 315. Total 1,683 + 950 − 315 = 2,318. (2,633 forgets to subtract.)'),
    dict(ch='4', scen='two friends aged 20 together with product 48 four years ago',
         stem='The sum of the ages of two friends is 20 years. Four years ago, the product of their ages was 48. What are their present ages?',
         opts=['This is not possible', '12 and 8 years', '14 and 6 years', '16 and 4 years'],
         hint='Form a quadratic and look at its discriminant.',
         sol='(x − 4)(16 − x) = 48 gives x² − 20x + 112 = 0. Discriminant = 400 − 448 < 0, so there is no real solution: the situation is not possible.'),

    # ---------------- Part 4 · Geometry
    dict(ch='5', scen='line EF parallel to the bases of a trapezium',
         fig=drawing(260, 200, trapezium_ef()),
         stem='ABCD is a trapezium with AB ∥ DC. E and F lie on AD and BC so that EF ∥ AB. If AE = 4 cm, ED = 6 cm and BF = 5 cm, what is FC?',
         opts=['7.5 cm', '10/3 cm', '6 cm', '5 cm'],
         hint='Join AC. Apply BPT in triangles ADC and CAB.',
         sol='Let AC meet EF at G. In triangle ADC, EG ∥ DC gives AE/ED = AG/GC. In triangle CAB, GF ∥ AB gives AG/GC = BF/FC. So 4/6 = 5/FC and FC = 7.5 cm.'),
    dict(ch='5', scen='side AB of a triangle around a circle of radius 4 with BD 8 and DC 6',
         fig=drawing(200, 210, incircle_given()),
         stem='A circle of radius 4 cm touches all three sides of triangle ABC. It touches BC at D, with BD = 8 cm and DC = 6 cm. What is the length of AB?',
         opts=['15 cm', '13 cm', '14 cm', '12 cm'],
         hint='Let the tangent from A be x. Then area = r × s and also, by Heron, √(s(s − a)(s − b)(s − c)).',
         sol='Sides: BC = 14, AB = x + 8, AC = x + 6, s = x + 14. r × s = 4(x + 14). Heron: √((x + 14) × x × 6 × 8). Squaring: 16(x + 14) = 48x, so x = 7. AB = 15 cm (and AC = 13 cm).'),
    dict(ch='5', scen='vertex of a square with opposite corners (1, 2) and (5, 6)',
         stem='A(1, 2) and C(5, 6) are opposite corners of a square ABCD. Which of these is another corner of the square?',
         opts=['(5, 2)', '(3, 4)', '(6, 1)', '(2, 5)'],
         hint='The other two corners are equally far from A and C and from the centre (3, 4).',
         sol='The centre is (3, 4). The other diagonal is perpendicular and of the same length, so the corners are (3, 4) ± (2, −2) = (5, 2) and (1, 6). Check: (5, 2) is 4 from both A and C.'),

    # ---------------- Part 5 · Mensuration
    dict(ch='6', scen='milk container frustum with radii 20 and 8 and height 16',
         stem='A milk container is a frustum of a cone with height 16 cm and radii 20 cm and 8 cm. What is its volume, in terms of π?',
         opts=['3,328π cm³', '9,984π cm³', '2,496π cm³', '4,992π cm³'],
         hint='V = (1/3)πh(R² + r² + Rr).',
         sol='V = (1/3)π × 16 × (400 + 64 + 160) = (16/3) × 624π = 3,328π cm³. (9,984π forgets the 1/3.)'),
    dict(ch='6', scen='cylinder of ice cream filling cones with hemispherical tops',
         stem='A cylinder of radius 6 cm and height 15 cm is full of ice cream. It is filled into cones of radius 3 cm and height 12 cm, each with a hemispherical top of ice cream. How many such cones can be filled?',
         opts=['10', '15', '20', '5'],
         hint='One cone with its top holds (1/3)π × 9 × 12 + (2/3)π × 27.',
         sol='Each = 36π + 18π = 54π cm³. Cylinder = π × 36 × 15 = 540π. Number = 10. (15 ignores the hemispherical tops.)'),
    dict(ch='6', scen='path 3.5 m wide inside the edge of a circular park of radius 21 m',
         stem='A circular park has radius 21 m. A path 3.5 m wide runs all round it, just inside the edge. What is the area of the path? (Take π = 22/7.)',
         opts=['423.5 m²', '462 m²', '385 m²', '231 m²'],
         hint='Path = big circle − inner circle of radius 17.5 m.',
         sol='Area = 22/7 × (21² − 17.5²) = 22/7 × 134.75 = 423.5 m². (462 uses an outer radius of 24.5 m.)'),

    # ---------------- Part 6 · Trigonometry
    dict(ch='7', scen='x = a sec theta and y = b tan theta · value of x²/a² − y²/b²',
         stem='If x = a sec θ and y = b tan θ, what is x²/a² − y²/b²?',
         opts=['1', '0', '−1', '2'],
         hint='sec²θ − tan²θ = 1.',
         sol='x²/a² − y²/b² = sec²θ − tan²θ = 1.'),
    dict(ch='7', scen='boy walking towards a 30 m building · elevation from 30 to 60 degrees',
         stem='A 1.5 m tall boy stands at some distance from a 30 m tall building. As he walks towards it, the angle of elevation of the top changes from 30° to 60°. How far did he walk?',
         opts=['19√3 m', '28.5√3 m', '10√3 m', '19 m'],
         hint='The height above his eyes is 30 − 1.5 = 28.5 m.',
         sol='Distances: 28.5√3 and 28.5/√3. Walked = 28.5(√3 − 1/√3) = 28.5 × 2/√3 = 19√3 m (about 32.9 m).'),

    # ---------------- Part 7 · Data Handling, Statistics & Probability
    dict(ch='8', scen='mode from a more-than cumulative table',
         fig=table(['Marks more than', '0', '10', '20', '30', '40'], [['Students', '50', '46', '38', '20', '8']], widths=[120, 56, 56, 56, 56, 56]),
         stem='The table is a "more than" cumulative frequency distribution for marks out of 50. What is the mode?',
         opts=['26.25', '25', '27.5', '24'],
         hint='Recover the class frequencies first: 50 − 46, 46 − 38, … .',
         sol='Frequencies: 0–10: 4, 10–20: 8, 20–30: 18, 30–40: 12, 40–50: 8. Modal class 20–30. Mode = 20 + (18 − 8)/(36 − 8 − 12) × 10 = 20 + 6.25 = 26.25.'),
    dict(ch='8', scen='die thrown twice with the first number larger',
         stem='A die is thrown twice. What is the probability that the first number is greater than the second?',
         opts=['5/12', '1/2', '7/12', '1/6'],
         hint='Remove the 6 doubles; the rest split evenly.',
         sol='Of 36 outcomes, 6 are equal. The other 30 are split evenly between "first larger" and "second larger": 15. Probability 15/36 = 5/12.'),

    # ---------------- Part 8 · Applied Mathematics
    dict(ch='9', scen='time for 30 km downstream from 12 km up in 3 h and down in 2 h',
         stem='A boat goes 12 km upstream in 3 hours and the same 12 km downstream in 2 hours. How long will it take to go 30 km downstream?',
         opts=['5 hours', '6 hours', '7.5 hours', '3 hours'],
         hint='Find the downstream speed.',
         sol='Downstream speed = 12/2 = 6 km/h. 30 km takes 30/6 = 5 hours. (The boat\'s speed in still water is 5 km/h and the stream 1 km/h; 6 hours uses the still-water speed.)'),
    dict(ch='9', scen='effective annual rate of 8 percent compounded quarterly',
         stem='A deposit earns 8% per annum compounded quarterly. What is the effective annual rate, correct to two decimal places?',
         opts=['8.24%', '8.00%', '8.16%', '32.47%'],
         hint='Grow ₹100 for four quarters at 2%.',
         sol='100 × 1.02⁴ = 108.24. Effective rate 8.24%. (8.16% is the half-yearly figure, 1.04² − 1.)'),
    dict(ch='9', scen='leak making an 6 hour fill take 8 hours',
         stem='A pipe can fill a tank in 6 hours. Because of a leak at the bottom, it takes 8 hours to fill. How long would the leak take to empty the full tank?',
         opts=['24 hours', '14 hours', '2 hours', '48 hours'],
         hint='Leak rate = 1/6 − 1/8.',
         sol='Leak empties 1/6 − 1/8 = 1/24 of the tank per hour, so 24 hours.'),

    # ---------------- Part 9 · Mathematical Reasoning
    dict(ch='10', scen='integers forcing a sum or difference divisible by 10',
         stem='What is the least number n such that among any n integers there are always two whose sum or difference is divisible by 10?',
         opts=['7', '6', '11', '10'],
         hint='Group the last digits as {0}, {5}, {1, 9}, {2, 8}, {3, 7}, {4, 6}.',
         sol='In each group, two numbers have a sum or a difference ending in 0. There are 6 groups, so 7 numbers force it. The 6 numbers 0, 1, 2, 3, 4, 5 do not work. So 7.'),
    dict(ch='10', scen='squares of all sizes on a chessboard',
         stem='How many squares of all sizes are there on an 8 × 8 chessboard?',
         opts=['204', '64', '196', '256'],
         hint='Count the k × k squares for k = 1 to 8.',
         sol='There are (9 − k)² squares of size k × k. Total = 8² + 7² + … + 1² = 204.'),
    dict(ch='10', scen='most kings on a chessboard with none attacking another',
         stem='What is the largest number of kings that can be placed on an 8 × 8 chessboard so that no two attack each other (no two on touching squares, even at a corner)?',
         opts=['16', '32', '64', '9'],
         hint='Split the board into 2 × 2 blocks.',
         sol='Each of the 16 blocks of 2 × 2 can hold at most one king, since all four squares touch. Kings on the top-left square of each block do not touch. So 16.'),

    # ---------------- Part 10 · Mixed Problems
    dict(ch='4+10', scen='three-digit numbers whose digits form an AP',
         stem='How many three-digit numbers have digits that form an arithmetic progression from left to right, such as 123, 975 or 555?',
         opts=['45', '40', '36', '50'],
         hint='Go through the common difference d = −4, …, 4 and count possible first digits.',
         sol='d = 0: 9. d = 1, 2, 3, 4: 7, 5, 3, 1. d = −1, −2, −3, −4: 8, 6, 4, 2. Total 9 + 16 + 20 = 45.'),
    dict(ch='5+7', scen='sine of angle ACD with the altitude from the right angle in a 5 12 13 triangle',
         stem='In triangle ABC, angle C = 90°, AC = 5 cm and BC = 12 cm. CD is perpendicular to AB. What is sin(angle ACD)?',
         opts=['5/13', '12/13', '5/12', '13/5'],
         hint='Angle ACD equals angle B.',
         sol='In right triangle ACD, angle ACD = 90° − angle A = angle B. sin B = AC/AB = 5/13.'),
    dict(ch='4+5', scen='k when (2, k) is equidistant from (−1, 2) and (3, 5)',
         stem='The point A(2, k) is equidistant from B(−1, 2) and C(3, 5). What is k?',
         opts=['13/6', '2', '7/2', '6/13'],
         hint='Set AB² = AC².',
         sol='9 + (k − 2)² = 1 + (k − 5)². So 13 − 4k = 26 − 10k, giving 6k = 13 and k = 13/6.'),
    dict(ch='3+9', scen='machine with 18 percent GST financed at 10 percent compound for 2 years',
         stem='A machine costs ₹1,00,000 plus 18% GST. Jayesh pays nothing now and borrows the full amount at 10% per annum compound interest, repaying everything after 2 years. How much does he repay?',
         opts=['₹1,42,780', '₹1,41,600', '₹1,21,000', '₹1,45,200'],
         hint='First find the price including GST.',
         sol='Price with GST = ₹1,18,000. After 2 years: 1,18,000 × 1.21 = ₹1,42,780. (₹1,41,600 uses simple interest; ₹1,21,000 forgets the GST.)'),
    dict(ch='6+10', scen='fraction of a cube taken by the largest cone carved from it',
         stem='The largest possible right circular cone is carved from a solid cube of edge 14 cm. What fraction of the cube does the cone fill? (Take π = 22/7.)',
         opts=['11/42', '11/21', '1/3', '22/21'],
         hint='The cone\'s base fits a face (radius 7) and its height is the edge (14).',
         sol='Cone = (1/3) × 22/7 × 49 × 14 = 2,156/3 cm³. Cube = 2,744 cm³. Fraction = 2,156/8,232 = 11/42.'),
]
