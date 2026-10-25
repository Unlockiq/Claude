# AMO Level-2 · Class 9 · Practice Paper 3  (format: see paper01.py)
import math


def cyclic_abcd():
    O, r = (90, 90), 62
    ang = {'A': 180, 'B': 0, 'C': 70, 'D': 130}
    P = {k: (O[0] + r * math.cos(math.radians(a)), O[1] + r * math.sin(math.radians(a))) for k, a in ang.items()}
    prims = [('circle', O[0], O[1], r, None), ('dot', O[0], O[1], 3), ('text', O[0], O[1] - 10, 'O', 12)]
    for a, b in (('A', 'B'), ('A', 'C'), ('B', 'C'), ('A', 'D'), ('D', 'C')):
        prims.append(('line', P[a][0], P[a][1], P[b][0], P[b][1]))
    for k, a in ang.items():
        dx, dy = math.cos(math.radians(a)), math.sin(math.radians(a))
        prims += [('dot', P[k][0], P[k][1], 3), ('text', P[k][0] + 14 * dx, P[k][1] + 14 * dy, k, 12)]
    prims.append(('text', P['A'][0] + 30, P['A'][1] + 9, '35°', 10))
    return prims


def stacked():
    """Two 100% stacked bars (walk / bus / car) with percentages written in the parts."""
    prims = []
    H = 180
    for i, (lab, parts, n) in enumerate((('Class A (120)', (40, 35, 25), 120), ('Class B (80)', (30, 50, 20), 80))):
        x = 40 + i * 140
        y = 10
        for p, fill, name in zip(parts, ('white', 'lilac', 'yellow'), ('walk', 'bus', 'car')):
            h = H * p / 100
            prims += [('rect', x, y, 70, h, fill), ('text', x + 35, y + h / 2, f'{name} {p}%', 10)]
            y += h
        prims.append(('text', x + 35, H + 26, lab, 11))
    return prims


QUESTIONS = [
    # ---------------- Part 1 · Number System
    dict(ch='1', scen='which of four fractions has a terminating decimal',
         stem='Which of these fractions has a terminating decimal expansion?',
         opts=['21/150', '11/30', '13/24', '9/14'],
         hint='Reduce each fraction to lowest terms first, then look at the prime factors of the denominator.',
         sol='21/150 = 7/50, and 50 = 2 × 5², so 7/50 = 0.14 terminates. 11/30, 13/24 and 9/14 are in lowest terms with a factor 3 or 7 in the denominator, so they recur. (150 has a factor 3, but it cancels.)'),
    dict(ch='1', scen='contradiction reached in the proof that √3 is irrational',
         stem='To prove √3 is irrational, Divya assumes √3 = p/q, where p and q are whole numbers with no common factor other than 1. Which conclusion gives the contradiction?',
         opts=['p and q are both multiples of 3', 'p must be an even number', 'q must be equal to 1', 'p² must be equal to q²'],
         hint='Square both sides: p² = 3q².',
         sol='p² = 3q², so 3 divides p², hence 3 divides p. Write p = 3m: 9m² = 3q², so q² = 3m² and 3 divides q. Then 3 is a common factor of p and q, which contradicts the assumption.'),

    # ---------------- Part 2 · Fractions, Decimals & Percentages
    dict(ch='3', scen='fish in a lake · minus 400 a year against minus 10 percent a year',
         stem='A lake has 5,000 fish. Model A says it loses 400 fish every year; Model B says it loses 10% of its fish every year. After 2 years, which model predicts fewer fish, and by how many?',
         opts=['Model B, by 150', 'Model A, by 150', 'Model B, by 50', 'Both predict 4,200'],
         hint='Model A is linear (subtract 400 twice); Model B multiplies by 0.9 twice.',
         sol='Model A: 5,000 − 800 = 4,200. Model B: 5,000 × 0.9 × 0.9 = 4,050. Model B predicts 150 fewer fish.'),
    dict(ch='3', scen='weighted score with weights 40 35 25 percent',
         stem='A school gives weights of 40% to Maths, 35% to Science and 25% to English. Riya scores 80, 60 and 72. What is her weighted score?',
         opts=['71', '70.67', '72', '69'],
         hint='Multiply each mark by its weight and add.',
         sol='0.40 × 80 + 0.35 × 60 + 0.25 × 72 = 32 + 21 + 18 = 71. (70.67 is the ordinary mean, which ignores the weights.)'),

    # ---------------- Part 3 · Algebra
    dict(ch='4', scen='a + b = 10 and ab = 21 · a³ + b³',
         stem='If a + b = 10 and ab = 21, what is a³ + b³?',
         opts=['370', '1,000', '433', '307'],
         hint='a³ + b³ = (a + b)³ − 3ab(a + b).',
         sol='a³ + b³ = 1,000 − 3 × 21 × 10 = 1,000 − 630 = 370. (Check: a and b are 3 and 7, and 27 + 343 = 370.)'),
    dict(ch='4', scen='temperature where Celsius and Fahrenheit readings are equal',
         stem='Temperatures are related by F = (9/5)C + 32. At what temperature do a Celsius thermometer and a Fahrenheit thermometer show the same number?',
         opts=['−40', '40', '−32', '0'],
         hint='Put F = C in the equation.',
         sol='C = (9/5)C + 32 gives −(4/5)C = 32, so C = −40. Check: (9/5)(−40) + 32 = −72 + 32 = −40.'),
    dict(ch='4', scen='values of k giving exactly one solution of kx + 2y = 5 and 3x + y = 1',
         stem='For which values of k do the equations kx + 2y = 5 and 3x + y = 1 have exactly one solution?',
         opts=['Every k except 6', 'Only k = 6', 'Every k except 3/2', 'No value of k'],
         hint='There is exactly one solution when the lines are not parallel.',
         sol='The lines are parallel when k/3 = 2/1, that is k = 6. For k = 6 the constants give 5/1 ≠ 2, so there is no solution. For every other k the lines cross once.'),
    dict(ch='4', scen='even terms among the first 12 terms of the sequence 1 1 2 3 5',
         stem='A sequence starts 1, 1 and each later term is the sum of the two before it. How many of the first 12 terms are even?',
         opts=['4', '6', '3', '5'],
         hint='Look at the pattern of odd (O) and even (E) terms.',
         sol='The pattern is O, O, E, O, O, E, … because odd + odd = even, odd + even = odd. Every 3rd term is even: terms 3, 6, 9, 12. That is 4 terms (2, 8, 34, 144).'),

    # ---------------- Part 4 · Geometry
    dict(ch='5', scen='area of the square whose diagonal joins (1,1) and (5,4)',
         stem='The opposite corners of a square are at (1, 1) and (5, 4). What is the area of the square?',
         opts=['12.5', '25', '6.25', '50'],
         hint='The distance between the points is a diagonal, not a side.',
         sol='Diagonal = √(4² + 3²) = 5. For a square, area = ½ × diagonal² = ½ × 25 = 12.5. (25 treats 5 as the side.)'),
    dict(ch='5', scen='cyclic ABCD with diameter AB and angle BAC 35 · angle ADC',
         fig=drawing(180, 180, cyclic_abcd()),
         stem='AB is a diameter of the circle with centre O, and ABCD is a cyclic quadrilateral. Angle BAC = 35°. What is angle ADC?',
         opts=['125°', '55°', '145°', '90°'],
         hint='The angle in a semicircle is 90°. Opposite angles of a cyclic quadrilateral add up to 180°.',
         sol='Angle ACB = 90° (angle in a semicircle), so angle ABC = 180° − 90° − 35° = 55°. ABCD is cyclic, so angle ADC = 180° − 55° = 125°.'),
    dict(ch='5', scen='median 18 · distance from midpoint of AG to D',
         stem='In triangle ABC, AD is a median of length 18 cm and G is the centroid. E is the midpoint of AG. What is the length ED?',
         opts=['12 cm', '9 cm', '6 cm', '15 cm'],
         hint='The centroid divides the median in the ratio 2 : 1.',
         sol='AG = ⅔ × 18 = 12 cm and GD = 6 cm. E is the midpoint of AG, so EG = 6 cm. ED = EG + GD = 6 + 6 = 12 cm.'),
    dict(ch='5', scen='two sides and a non-included angle 40 · congruent or not',
         stem='In triangles PQR and XYZ, PQ = XY = 5 cm, QR = YZ = 6 cm and angle R = angle Z = 40°. What can you conclude?',
         opts=['They need not be congruent: two sides and a non-included angle do not fix the triangle',
               'They are congruent by SAS', 'They are congruent by ASA', 'They are congruent by RHS'],
         hint='The equal angle is not between the two equal sides.',
         sol='The 40° angle is not the angle between PQ and QR, so SAS does not apply. With PQ = 5 shorter than QR = 6, two different triangles have these measurements (angle P about 50.5° or about 129.5°). So they need not be congruent.'),

    # ---------------- Part 5 · Mensuration
    dict(ch='6', scen='5-12-13 triangle enlarged to perimeter 90 · area',
         stem='A triangle with sides 5 cm, 12 cm and 13 cm is enlarged so that its perimeter becomes 90 cm. What is the area of the enlarged triangle?',
         opts=['270 cm²', '90 cm²', '810 cm²', '180 cm²'],
         hint='The perimeter grows 3 times. How does the area change?',
         sol='The original perimeter is 30, so every length is multiplied by 3. The original area is ½ × 5 × 12 = 30 cm², and area is multiplied by 3² = 9: 270 cm². (90 multiplies the area by 3 only.)'),
    dict(ch='6', scen='painting curved surfaces of 8 pillars at ₹12 a m²',
         stem='A hall has 8 cylindrical pillars, each of radius 35 cm and height 4 m. Painting costs ₹12 per m² of curved surface. What is the total cost? (Take π = 22/7.)',
         opts=['₹844.80', '₹105.60', '₹422.40', '₹1,689.60'],
         hint='Change 35 cm to metres before using 2πrh.',
         sol='Curved surface of one pillar = 2 × 22/7 × 0.35 × 4 = 8.8 m². For 8 pillars: 70.4 m². Cost = 70.4 × 12 = ₹844.80. (₹105.60 is for one pillar.)'),
    dict(ch='6', scen='sphere of volume 38,808 cm³ · surface area',
         stem='A sphere has volume 38,808 cm³. What is its surface area? (Take π = 22/7.)',
         opts=['5,544 cm²', '1,386 cm²', '2,772 cm²', '11,088 cm²'],
         hint='Find r³ from V = (4/3)πr³.',
         sol='r³ = 38,808 × 3/4 × 7/22 = 9,261, so r = 21 cm. Surface area = 4 × 22/7 × 21² = 5,544 cm². (2,772 is the curved surface of a hemisphere.)'),

    # ---------------- Part 6 · Data Handling, Statistics & Probability
    dict(ch='8', scen='empirical probability of an even number from 300 die rolls',
         fig=table(['Number', '1', '2', '3', '4', '5', '6'], [['Times', '45', '52', '48', '60', '47', '48']], widths=[70] + [46] * 6),
         stem='Harsh rolls a die 300 times and records the results in this table. From his data, what is the empirical probability of rolling an even number?',
         opts=['8/15', '1/2', '7/15', '3/5'],
         hint='Add the frequencies of 2, 4 and 6.',
         sol='Even numbers occurred 52 + 60 + 48 = 160 times out of 300, so the empirical probability is 160/300 = 8/15. (1/2 is the theoretical value.)'),
    dict(ch='8', scen='100 percent stacked bars · percentage of all students who take the bus',
         fig=drawing(320, 215, stacked()),
         stem='The 100% stacked bar graph shows how the students of two classes come to school. Class A has 120 students and Class B has 80. What percentage of all 200 students come by bus?',
         opts=['41%', '42.5%', '43%', '40%'],
         hint='Turn each bus percentage into a number of students.',
         sol='Class A: 35% of 120 = 42. Class B: 50% of 80 = 40. Total 82 of 200 = 41%. (42.5% is the plain average of 35% and 50%, which ignores the class sizes.)'),
    dict(ch='8', scen='five numbers with mean 12 median 11 mode 10 largest 16 · fourth number',
         stem='Five whole numbers have mean 12, median 11 and a single mode 10. The largest is 16. Written in order, what is the 4th number?',
         opts=['13', '12', '14', '15'],
         hint='The mode 10 must appear at least twice, below the median.',
         sol='In order a ≤ b ≤ 11 ≤ d ≤ 16. The mode is 10, so a = b = 10. The total is 5 × 12 = 60, so 10 + 10 + 11 + d + 16 = 60 and d = 13.'),

    # ---------------- Part 7 · Applied Mathematics
    dict(ch='9', scen='phone plans ₹200 + ₹1 a minute against ₹50 + ₹2.50 a minute',
         stem='Phone plan A costs ₹200 a month plus ₹1 per minute. Plan B costs ₹50 a month plus ₹2.50 per minute. For which monthly usage is plan A cheaper?',
         opts=['More than 100 minutes', 'Fewer than 100 minutes', 'More than 60 minutes', 'More than 150 minutes'],
         hint='Find where the two costs are equal.',
         sol='200 + m = 50 + 2.5m gives 1.5m = 150, so m = 100. Beyond 100 minutes plan B rises faster, so plan A is cheaper for more than 100 minutes.'),
    dict(ch='9', scen='bacteria doubling every 20 minutes from 500 · after 2 hours',
         stem='A culture of 500 bacteria doubles every 20 minutes. How many bacteria are there after 2 hours?',
         opts=['32,000', '64,000', '3,000', '16,000'],
         hint='Count the doublings in 2 hours.',
         sol='2 hours = 120 minutes = 6 doublings. 500 × 2⁶ = 500 × 64 = 32,000. (3,000 adds 500 six times instead of doubling.)'),
    dict(ch='9', scen='teacher at the midpoint of seats (2,3) and (8,11)',
         stem='On a seating grid (1 unit = 1 m), Neha sits at (2, 3) and Om at (8, 11). Their teacher stands exactly halfway between them. How far is the teacher from Neha?',
         opts=['5 m', '10 m', '7 m', '4 m'],
         hint='Find the midpoint, or halve the distance between Neha and Om.',
         sol='Neha to Om: √(6² + 8²) = 10 m. The teacher is at the midpoint (5, 7), which is 5 m from Neha.'),

    # ---------------- Part 8 · Mathematical Reasoning
    dict(ch='10', scen='counterexample to 2ⁿ − 1 always prime',
         stem='Vivek claims that 2ⁿ − 1 is prime for every whole number n ≥ 2. Which value of 2ⁿ − 1 is a counterexample?',
         opts=['15', '7', '31', '3'],
         hint='Try n = 2, 3, 4, 5.',
         sol='n = 2, 3, 5 give 3, 7, 31, all prime. n = 4 gives 15 = 3 × 5, which is not prime, so 15 disproves the claim.'),
    dict(ch='10', scen='most guesses needed to find a number 1 to 100 by halving',
         stem='Gita thinks of a whole number from 1 to 100. Yash guesses, and Gita says "higher" or "lower". If Yash always guesses the middle of the numbers still possible, what is the most guesses he could need?',
         opts=['7', '10', '6', '50'],
         hint='Each guess roughly halves the numbers still possible.',
         sol='After each guess at most half of the remaining numbers are left: 100 → 50 → 25 → 12 → 6 → 3 → 1. In the worst case the 7th guess is needed. 6 guesses are not enough, since 2⁶ − 1 = 63 < 100.'),
    dict(ch='10', scen='ways to climb 8 steps taking 1 or 2 at a time',
         stem='Lakshya climbs a staircase of 8 steps, taking 1 or 2 steps at a time. In how many different ways can he reach the top?',
         opts=['34', '21', '55', '16'],
         hint='Ways(n) = Ways(n − 1) + Ways(n − 2): the last move is 1 step or 2 steps.',
         sol='Ways for 1, 2, 3, … steps: 1, 2, 3, 5, 8, 13, 21, 34. So there are 34 ways for 8 steps.'),
    dict(ch='10', scen='first line of a proof by contradiction that there is no largest even number',
         stem='Which sentence correctly begins a proof by contradiction that "there is no largest even number"?',
         opts=['Suppose N is the largest even number.', 'Suppose every number is even.', 'Suppose N + 2 is an odd number.',
               'Suppose there are only finitely many odd numbers.'],
         hint='Assume the opposite of what you want to prove.',
         sol='Assume the opposite: a largest even number N exists. Then N + 2 is even and larger, a contradiction. So no largest even number exists.'),

    # ---------------- Part 9 · Mixed Problems
    dict(ch='4+10', scen='1 + 2 + … + n equal to a three-digit number with equal digits',
         stem='The sum 1 + 2 + 3 + … + n is a three-digit number with all three digits the same. What is n?',
         opts=['36', '37', '35', '18'],
         hint='n(n + 1)/2 = 111 × d = 3 × 37 × d.',
         sol='n(n + 1)/2 = 111d, so n(n + 1) = 2 × 3 × 37 × d. One of n, n + 1 must be 37 (or a multiple). n = 36: 36 × 37/2 = 666 ✓. n = 37: 703, not a repdigit. So n = 36.'),
    dict(ch='5+6', scen='cow tied at corner (12,9) of a field with a 6 m rope',
         stem='A rectangular field has corners at (0, 0), (12, 0), (12, 9) and (0, 9), in metres. A cow is tied at the corner (12, 9) with a 6 m rope. What area of the field can it graze?',
         opts=['9π m²', '36π m²', '18π m²', '27π m²'],
         hint='Inside the field the cow sweeps a quarter of a circle.',
         sol='The corner is a right angle and the rope (6 m) is shorter than both sides, so the grazed region is a quarter circle of radius 6: ¼ × π × 36 = 9π m².'),
    dict(ch='4+5', scen='line through (2,5) parallel to y = 3x − 4 · y-intercept',
         stem='A line passes through (2, 5) and is parallel to y = 3x − 4. Where does it cross the y-axis?',
         opts=['(0, −1)', '(0, −4)', '(0, 11)', '(0, 5)'],
         hint='Parallel lines have the same slope.',
         sol='The line is y = 3x + b. Putting (2, 5): 5 = 6 + b, so b = −1. It crosses the y-axis at (0, −1).'),
    dict(ch='8+10', scen='three cards 1 2 3 shuffled · no card in its own place',
         stem='Cards numbered 1, 2 and 3 are shuffled and laid in a row in positions 1, 2 and 3. What is the probability that no card is in the position with its own number?',
         opts=['1/3', '1/2', '1/6', '2/3'],
         hint='List all 6 orders.',
         sol='The orders are 123, 132, 213, 231, 312, 321. Only 231 and 312 have no card in its own place. Probability = 2/6 = 1/3.'),
    dict(ch='3+9', scen='salary up ₹3,000 a year against 9 percent a year · third-year salary',
         stem='Two jobs both start at ₹30,000 a month. Job A raises the salary by ₹3,000 each year; Job B raises it by 9% each year. In the third year, which pays more, and by how much?',
         opts=['Job A, by ₹357', 'Job B, by ₹357', 'They pay the same', 'Job A, by ₹600'],
         hint='The third-year salary comes after two raises.',
         sol='Job A: 30,000 + 2 × 3,000 = ₹36,000. Job B: 30,000 × 1.09 × 1.09 = ₹35,643. Job A pays ₹357 more.'),
]
