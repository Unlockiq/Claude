# AMO Level-2 · Class 9 · Practice Paper 4  (format: see paper01.py)
import math


def circle_oac():
    O, r = (90, 90), 62
    ang = {'A': 155, 'C': 25, 'B': 270}
    P = {k: (O[0] + r * math.cos(math.radians(a)), O[1] + r * math.sin(math.radians(a))) for k, a in ang.items()}
    prims = [('circle', O[0], O[1], r, None), ('dot', O[0], O[1], 3), ('text', O[0], O[1] - 12, 'O', 12)]
    for a, b in (('A', 'C'), ('B', 'A'), ('B', 'C')):
        prims.append(('line', P[a][0], P[a][1], P[b][0], P[b][1]))
    prims += [('line', O[0], O[1], P['A'][0], P['A'][1]), ('line', O[0], O[1], P['C'][0], P['C'][1])]
    for k, a in ang.items():
        dx, dy = math.cos(math.radians(a)), math.sin(math.radians(a))
        prims += [('dot', P[k][0], P[k][1], 3), ('text', P[k][0] + 14 * dx, P[k][1] + 14 * dy, k, 12)]
    prims.append(('text', P['A'][0] + 26, P['A'][1] - 4, '25°', 10))
    return prims


QUESTIONS = [
    # ---------------- Part 1 · Number System
    dict(ch='1', scen='0.454545… plus 0.545454…',
         stem='Leena adds the recurring decimals 0.454545… and 0.545454… What is the exact sum?',
         opts=['1', '0.99', '99/100', '1.01'],
         hint='Write each recurring decimal as a fraction with denominator 99.',
         sol='0.4545… = 45/99 and 0.5454… = 54/99. The sum is 99/99 = 1. (0.999… recurring is exactly 1.)'),
    dict(ch='1', scen='values of k from 1 to 100 making √(72k) rational',
         stem='For how many whole numbers k from 1 to 100 is √(72k) a rational number?',
         opts=['7', '10', '5', '14'],
         hint='72 = 36 × 2, so √(72k) = 6√(2k).',
         sol='√(72k) = 6√(2k) is rational exactly when 2k is a perfect square, i.e. k = 2m². The values are 2, 8, 18, 32, 50, 72, 98: 7 values.'),

    # ---------------- Part 2 · Fractions, Decimals & Percentages
    dict(ch='3', scen='value down 10 percent twice then up 21 percent',
         stem='The value of a painting falls by 10% in each of two years and then rises by 21% in the third year. What is the overall change over the three years?',
         opts=['A decrease of 1.99%', 'No change', 'An increase of 1%', 'A decrease of 0.99%'],
         hint='Multiply the factors 0.9, 0.9 and 1.21.',
         sol='0.9 × 0.9 × 1.21 = 0.81 × 1.21 = 0.9801, so the value is 98.01% of the start: a decrease of 1.99%. (−10 − 10 + 21 = +1 adds percentages wrongly.)'),
    dict(ch='3', scen='class of 40 with mean 52 · boys mean 50 girls mean 55 · number of girls',
         stem='A class of 40 students has a mean mark of 52. The boys have a mean of 50 and the girls a mean of 55. How many girls are there?',
         opts=['16', '24', '20', '18'],
         hint='If all 40 had scored 50, the total would be 2,000.',
         sol='Total = 40 × 52 = 2,080. If everyone scored 50 the total would be 2,000; each girl adds 5 more. 5g = 80, so g = 16 girls (and 24 boys).'),

    # ---------------- Part 3 · Algebra
    dict(ch='4', scen='8x³ − 27y³ when 2x − 3y = 5 and xy = 2',
         stem='If 2x − 3y = 5 and xy = 2, what is the value of 8x³ − 27y³?',
         opts=['305', '125', '485', '215'],
         hint='a³ − b³ = (a − b)³ + 3ab(a − b) with a = 2x and b = 3y.',
         sol='With a = 2x, b = 3y: a − b = 5 and ab = 6xy = 12. a³ − b³ = 5³ + 3 × 12 × 5 = 125 + 180 = 305.'),
    dict(ch='4', scen='cubic with zeros 1 and 2 · value at 3',
         stem='The polynomial p(x) = x³ + ax² + bx + 6 has p(1) = 0 and p(2) = 0. What is p(3)?',
         opts=['12', '0', '6', '−12'],
         hint='Write the two conditions as equations in a and b.',
         sol='p(1) = 7 + a + b = 0 and p(2) = 14 + 4a + 2b = 0, i.e. a + b = −7 and 2a + b = −7. So a = 0, b = −7. p(3) = 27 − 21 + 6 = 12.'),
    dict(ch='4', scen='adult ₹60 and child ₹35 tickets · 140 tickets for ₹6,650',
         stem='A show sells adult tickets at ₹60 and child tickets at ₹35. It sells 140 tickets for ₹6,650 in all. How many adult tickets were sold?',
         opts=['70', '75', '65', '80'],
         hint='If all 140 were child tickets, the takings would be ₹4,900.',
         sol='140 child tickets would give 140 × 35 = 4,900. Each adult ticket adds ₹25 more. (6,650 − 4,900) ÷ 25 = 1,750 ÷ 25 = 70 adult tickets.'),
    dict(ch='4', scen='AP whose 4th term is twice the 1st and 7th term is 36',
         stem='In an arithmetic progression, the 4th term is twice the 1st term, and the 7th term is 36. What is the 10th term?',
         opts=['48', '60', '44', '52'],
         hint='a + 3d = 2a gives a = 3d.',
         sol='a + 3d = 2a, so a = 3d. Then a + 6d = 9d = 36, so d = 4 and a = 12. The 10th term = 12 + 9 × 4 = 48.'),

    # ---------------- Part 4 · Geometry
    dict(ch='5', scen='circumcentre of the triangle (0,0) (6,0) (6,8)',
         stem='Where is the circumcentre of the triangle with vertices A(0, 0), B(6, 0) and C(6, 8)?',
         opts=['(3, 4)', '(4, 8/3)', '(6, 0)', '(2, 2)'],
         hint='The triangle has a right angle at B.',
         sol='Angle B is a right angle, so the hypotenuse AC is a diameter of the circumcircle. The circumcentre is the midpoint of AC: (3, 4). (4, 8/3) is the centroid.'),
    dict(ch='5', scen='chord 16 at distance 6 · chord at distance 8 in the same circle',
         stem='In a circle, a chord of length 16 cm is 6 cm from the centre. How long is a chord of the same circle that is 8 cm from the centre?',
         opts=['12 cm', '14 cm', '10 cm', '16 cm'],
         hint='Find the radius first.',
         sol='r² = 8² + 6² = 100, so r = 10 cm. A chord 8 cm from the centre has half-length √(100 − 64) = 6, so its length is 12 cm.'),
    dict(ch='5', scen='angle OAC 25 · angle ABC with B on the major arc',
         fig=drawing(180, 180, circle_oac()),
         stem='O is the centre of the circle. A, B and C lie on the circle, with B on the major arc AC. Angle OAC = 25°. What is angle ABC?',
         opts=['65°', '130°', '50°', '115°'],
         hint='Triangle OAC is isosceles (OA = OC).',
         sol='OA = OC, so angle OCA = 25° and angle AOC = 180° − 50° = 130°. The angle at the circumference is half: angle ABC = 65°.'),
    dict(ch='5', scen='condition that guarantees a quadrilateral is a parallelogram',
         stem='Which condition on a quadrilateral always makes it a parallelogram?',
         opts=['One pair of opposite sides is both equal and parallel', 'One pair of opposite sides is parallel and the other pair is equal',
               'Its diagonals are equal', 'Two pairs of adjacent sides are equal'],
         hint='Test each condition against a trapezium, a rectangle and a kite.',
         sol='One pair of sides equal and parallel always gives a parallelogram. An isosceles trapezium has one pair parallel and the other pair equal; an isosceles trapezium also has equal diagonals; a kite has two pairs of equal adjacent sides — none of them is a parallelogram in general.'),

    # ---------------- Part 5 · Mensuration
    dict(ch='6', scen='isosceles triangle with perimeter 32 and base 12 · area',
         stem='An isosceles triangle has perimeter 32 cm and base 12 cm. What is its area?',
         opts=['48 cm²', '60 cm²', '96 cm²', '36 cm²'],
         hint='Each equal side is (32 − 12) ÷ 2.',
         sol='The equal sides are 10 cm each. With Heron: s = 16, area = √(16 × 6 × 6 × 4) = √2,304 = 48 cm². (Or height √(100 − 36) = 8, area ½ × 12 × 8.)'),
    dict(ch='6', scen='canvas length 2.5 m wide for a conical tent of radius 7 and height 24',
         stem='A conical tent has base radius 7 m and height 24 m. It is made from canvas 2.5 m wide. What length of canvas is needed? (Take π = 22/7; ignore waste.)',
         opts=['220 m', '550 m', '110 m', '275 m'],
         hint='Find the slant height, then the curved surface area.',
         sol='Slant height = √(7² + 24²) = 25 m. Curved surface = 22/7 × 7 × 25 = 550 m². Length = 550 ÷ 2.5 = 220 m.'),
    dict(ch='6', scen='area swept by a 14 cm minute hand from 4:00 to 4:20',
         stem='The minute hand of a clock is 14 cm long. What area does it sweep from 4:00 to 4:20? (Take π = 22/7.)',
         opts=['616/3 cm²', '308/3 cm²', '616 cm²', '88/3 cm²'],
         hint='In 20 minutes the minute hand turns through 120°.',
         sol='Area = (120/360) × 22/7 × 14² = ⅓ × 616 = 616/3 cm² (about 205.3 cm²). (88/3 cm is the arc length.)'),

    # ---------------- Part 6 · Data Handling, Statistics & Probability
    dict(ch='8', scen='card from a pack of 52 · red or a king',
         stem='A card is drawn at random from a well-shuffled pack of 52 playing cards. What is the probability that it is red or a king?',
         opts=['7/13', '15/26', '1/2', '8/13'],
         hint='Two of the kings are already red.',
         sol='Red cards: 26. Kings that are not red: 2. Total 28, so the probability is 28/52 = 7/13. (15/26 counts the red kings twice.)'),
    dict(ch='8', scen='mean of 11 numbers 20 · first six 18 · last six 23 · sixth number',
         stem='The mean of 11 numbers is 20. The mean of the first 6 is 18 and the mean of the last 6 is 23. What is the 6th number?',
         opts=['26', '21', '20', '23'],
         hint='The 6th number belongs to both groups of six.',
         sol='First six total 108, last six total 138. Together they count the 6th number twice: 108 + 138 = 246 = 220 + 6th number. So the 6th number is 26.'),
    dict(ch='8', scen='spinner 1 2 3 then spinner 1 2 · product even',
         stem='Spinner A shows 1, 2 or 3 and spinner B shows 1 or 2, each equally likely. Tanvi spins both and multiplies the numbers. What is the probability that the product is even?',
         opts=['2/3', '1/2', '1/3', '5/6'],
         hint='The product is odd only when both numbers are odd.',
         sol='There are 3 × 2 = 6 equally likely outcomes. Odd products need A odd (1 or 3) and B = 1: 2 outcomes. So P(even) = 1 − 2/6 = 2/3.'),

    # ---------------- Part 7 · Applied Mathematics
    dict(ch='9', scen='20 L drink at 25 percent juice made 40 percent by adding juice',
         stem='Ayaan has 20 L of a drink that is 25% fruit juice. How many litres of pure juice must he add to make it 40% juice?',
         opts=['5 L', '3 L', '6 L', '4 L'],
         hint='The water stays the same: 15 L.',
         sol='The 15 L of water must be 60% of the new drink, so the new total is 15 ÷ 0.6 = 25 L. He adds 25 − 20 = 5 L of juice. (3 L takes 40% − 25% = 15% of 20 L.)'),
    dict(ch='9', scen='candle 30 cm at 6 PM and 18 cm at 9 PM · burns out',
         stem='A candle burns at a steady rate. It is 30 cm tall at 6:00 PM and 18 cm tall at 9:00 PM. At what time will it burn out?',
         opts=['1:30 AM', '12:00 midnight', '1:00 AM', '2:30 AM'],
         hint='Find how many cm it burns per hour.',
         sol='It burns 12 cm in 3 hours, i.e. 4 cm per hour. From 30 cm at 6 PM it needs 30 ÷ 4 = 7.5 hours, so it burns out at 1:30 AM.'),
    dict(ch='9', scen='saving ₹10 more each day · days to reach ₹2,100',
         stem='Asha saves ₹10 on day 1, ₹20 on day 2, ₹30 on day 3, and so on. After how many days will her total savings be ₹2,100?',
         opts=['20', '21', '14', '42'],
         hint='The total after n days is 10 × (1 + 2 + … + n).',
         sol='10 × n(n + 1)/2 = 2,100 gives n(n + 1) = 420 = 20 × 21. So n = 20 days.'),

    # ---------------- Part 8 · Mathematical Reasoning
    dict(ch='10', scen='converse of vertically opposite angles are equal and its truth',
         stem='"If two angles are vertically opposite, then they are equal." Which option gives the converse and says correctly whether it is true?',
         opts=['If two angles are equal, then they are vertically opposite — false',
               'If two angles are equal, then they are vertically opposite — true',
               'If two angles are not equal, then they are not vertically opposite — true',
               'If two angles are not vertically opposite, then they are not equal — false'],
         hint='The converse swaps the "if" part and the "then" part.',
         sol='The converse is "If two angles are equal, then they are vertically opposite." It is false: the two base angles of an isosceles triangle are equal but not vertically opposite.'),
    dict(ch='10', scen='Kaprekar routine steps from 2111 to 6174',
         stem='Kaprekar\'s routine: arrange the 4 digits in descending order and in ascending order (keeping zeros), and subtract the smaller from the larger. Repeat. Starting from 2111, after how many subtractions do you first reach 6174?',
         opts=['5', '4', '6', '3'],
         hint='2111 − 1112 = 999, written as 0999.',
         sol='2111 − 1112 = 0999; 9990 − 0999 = 8991; 9981 − 1899 = 8082; 8820 − 0288 = 8532; 8532 − 2358 = 6174. That is 5 subtractions.'),
    dict(ch='10', scen='area of the Sierpinski triangle left after 3 steps',
         stem='In the Sierpinski triangle, each shaded triangle is split into 4 equal triangles and the middle one is removed. What fraction of the original area is still shaded after 3 steps?',
         opts=['27/64', '9/16', '1/4', '37/64'],
         hint='Each step keeps 3/4 of the shaded area.',
         sol='After each step 3/4 of the shaded area remains: (3/4)³ = 27/64. (37/64 is the fraction removed.)'),
    dict(ch='10', scen='when Brahmagupta formula becomes Heron formula',
         stem='Brahmagupta\'s formula gives the area of a cyclic quadrilateral with sides a, b, c, d. In which case does it become Heron\'s formula for a triangle?',
         opts=['When one side, say d, becomes 0', 'When all four sides are equal', 'When the quadrilateral is a rectangle',
               'When the two diagonals are equal'],
         hint='A triangle can be thought of as a quadrilateral with one side shrunk away.',
         sol='Area = √((s − a)(s − b)(s − c)(s − d)). If d = 0 the quadrilateral becomes a triangle, s becomes the triangle\'s semi-perimeter, and s − d = s gives √(s(s − a)(s − b)(s − c)), which is Heron\'s formula.'),

    # ---------------- Part 9 · Mixed Problems
    dict(ch='4+10', scen='t1 = 3 and t(n+1) = t(n) + 2n · 10th term',
         stem='A sequence has t₁ = 3 and tₙ₊₁ = tₙ + 2n for every n ≥ 1. What is t₁₀?',
         opts=['93', '101', '111', '83'],
         hint='t₁₀ = 3 + 2(1 + 2 + … + 9).',
         sol='Each step adds 2n, so t₁₀ = 3 + 2 × (1 + 2 + … + 9) = 3 + 2 × 45 = 93. (In general tₙ = n² − n + 3.)'),
    dict(ch='5+6', scen='circle through (0,0) (8,0) (8,6) · area outside the triangle',
         stem='A circle passes through A(0, 0), B(8, 0) and C(8, 6). What is the area of the part of the circle that lies outside triangle ABC?',
         opts=['25π − 24', '25π − 48', '100π − 24', '25π'],
         hint='Angle B is a right angle, so AC is a diameter.',
         sol='AC = √(8² + 6²) = 10 is a diameter, so r = 5 and the circle\'s area is 25π. The triangle\'s area is ½ × 8 × 6 = 24. Outside the triangle: 25π − 24.'),
    dict(ch='4+5', scen='triangle formed by x + y = 6, x − y = 2 and the y-axis',
         stem='What is the area of the triangle formed by the lines x + y = 6, x − y = 2 and the y-axis?',
         opts=['16', '8', '12', '24'],
         hint='Find where the two lines meet and where each meets the y-axis.',
         sol='The lines meet at (4, 2). They meet the y-axis at (0, 6) and (0, −2), a base of 8. The height is the x-coordinate 4. Area = ½ × 8 × 4 = 16.'),
    dict(ch='8+10', scen='two-digit number from digits 1 to 5 without repeating · divisible by 4',
         stem='Two different digits are chosen from 1, 2, 3, 4, 5 to make a two-digit number, all choices being equally likely. What is the probability that the number is divisible by 4?',
         opts=['1/5', '1/4', '3/20', '6/25'],
         hint='There are 5 × 4 = 20 possible numbers.',
         sol='The multiples of 4 that can be made are 12, 24, 32 and 52 (44 repeats a digit). So the probability is 4/20 = 1/5.'),
    dict(ch='3+9', scen='town of 50,000 up 4 percent then down 5 percent',
         stem='A town of 50,000 people grows by 4% in one year and then shrinks by 5% in the next. What is its population after the two years?',
         opts=['49,400', '49,500', '50,000', '50,600'],
         hint='Multiply by 1.04 and then by 0.95.',
         sol='50,000 × 1.04 = 52,000. 52,000 × 0.95 = 49,400. (49,500 subtracts a net 1% from the start.)'),
]
