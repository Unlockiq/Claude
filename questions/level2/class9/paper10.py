# AMO Level-2 · Class 9 · Practice Paper 10  (format: see paper01.py)


def grid_points(pts, xr=(-1, 9), yr=(-4, 7), s=18):
    """Small coordinate grid with labelled points. pts: list of (label, x, y)."""
    X = lambda x: 20 + (x - xr[0]) * s
    Y = lambda y: 10 + (yr[1] - y) * s
    prims = []
    for x in range(xr[0], xr[1] + 1):
        prims.append(('line', X(x), Y(yr[0]), X(x), Y(yr[1]), False, (215, 215, 215), 0.8))
    for y in range(yr[0], yr[1] + 1):
        prims.append(('line', X(xr[0]), Y(y), X(xr[1]), Y(y), False, (215, 215, 215), 0.8))
    prims += [('line', X(xr[0]), Y(0), X(xr[1]), Y(0)), ('line', X(0), Y(yr[0]), X(0), Y(yr[1]))]
    poly = [(X(x), Y(y)) for _, x, y in pts]
    prims.append(('poly', poly, None))
    for lab, x, y in pts:
        prims += [('dot', X(x), Y(y), 3.5), ('text', X(x) + 10, Y(y) - 10, lab, 10)]
    return prims


QUESTIONS = [
    # ---------------- Part 1 · Number System
    dict(ch='1', scen='1.272727… as a fraction in lowest terms',
         stem='Write the recurring decimal 1.272727… (27 repeating) as a fraction in lowest terms.',
         opts=['14/11', '127/99', '63/50', '13/11'],
         hint='0.2727… = 27/99.',
         sol='1.2727… = 1 + 27/99 = 1 + 3/11 = 14/11. (127/99 treats the whole number part as part of the repeating block.)'),
    dict(ch='1', scen='expression that must be irrational when p irrational and q rational',
         stem='p is irrational and q is a non-zero rational number. Which of these must be irrational?',
         opts=['p + q', 'p × p', 'p − p', 'p ÷ p'],
         hint='Try p = √2 in each.',
         sol='If p + q were rational, p = (p + q) − q would be rational, which is false; so p + q is irrational. But √2 × √2 = 2, p − p = 0 and p ÷ p = 1 are rational.'),

    # ---------------- Part 2 · Fractions, Decimals & Percentages
    dict(ch='3', scen='population of 60,000 up 5 then down 5 percent',
         stem='A town of 60,000 people grows by 5% in one year and then shrinks by 5% in the next. What is its population after the two years?',
         opts=['59,850', '60,000', '59,700', '60,150'],
         hint='The factors are 1.05 and 0.95.',
         sol='60,000 × 1.05 × 0.95 = 60,000 × 0.9975 = 59,850. The 5% fall is taken on the larger number, so it does not cancel the rise.'),
    dict(ch='3', scen='mixing rice at ₹40 and ₹64 per kg to cost ₹50 per kg',
         stem='A grocer mixes rice costing ₹40 per kg with rice costing ₹64 per kg so that the mixture costs ₹50 per kg. In what ratio (cheaper : dearer) are they mixed?',
         opts=['7 : 5', '5 : 7', '3 : 2', '2 : 3'],
         hint='Each kilogram of cheap rice saves ₹10 against ₹50; each kilogram of dear rice costs ₹14 extra.',
         sol='Let the amounts be p kg and q kg. 40p + 64q = 50(p + q) gives 14q = 10p, so p : q = 14 : 10 = 7 : 5.'),

    # ---------------- Part 3 · Algebra
    dict(ch='4', scen='a + b + c = 9 and a² + b² + c² = 35 · ab + bc + ca',
         stem='If a + b + c = 9 and a² + b² + c² = 35, what is ab + bc + ca?',
         opts=['23', '46', '22', '58'],
         hint='Expand (a + b + c)².',
         sol='81 = 35 + 2(ab + bc + ca), so ab + bc + ca = 46 ÷ 2 = 23.'),
    dict(ch='4', scen='x² − y² = 45 and x + y = 9 · value of x³ − y³',
         stem='Two numbers x and y satisfy x² − y² = 45 and x + y = 9. What is x³ − y³?',
         opts=['335', '351', '45', '125'],
         hint='x² − y² = (x + y)(x − y). Find x and y first.',
         sol='(x + y)(x − y) = 45 gives x − y = 5, so x = 7 and y = 2. x³ − y³ = 343 − 8 = 335. (Or (x − y)(x² + xy + y²) = 5 × 67 = 335.) (125 is (x − y)³.)'),
    dict(ch='4', scen='a + b for infinitely many solutions of 2x + 3y = 7 and ax + 9y = b',
         stem='The equations 2x + 3y = 7 and ax + 9y = b have infinitely many solutions. What is a + b?',
         opts=['27', '15', '21', '6'],
         hint='The second equation must be a multiple of the first.',
         sol='9 = 3 × 3, so the second equation is 3 times the first: a = 6 and b = 21. a + b = 27.'),
    dict(ch='4', scen='values of n with 1 + 2 + … + n between 400 and 450',
         stem='For how many whole numbers n is 1 + 2 + … + n greater than 400 and less than 450?',
         opts=['2', '1', '3', '0'],
         hint='The sum is n(n + 1)/2. Try n near 28.',
         sol='n = 27 gives 378, n = 28 gives 406, n = 29 gives 435 and n = 30 gives 465. Only n = 28 and n = 29 work: 2 values.'),

    # ---------------- Part 4 · Geometry
    dict(ch='5', scen='C found from midpoint of AC · length BC',
         stem='A = (−3, 5) and B = (5, −1). M = (2, 4) is the midpoint of AC. What is the length of BC?',
         opts=['2√5', '10', '4√5', '6'],
         hint='Find C from the midpoint first.',
         sol='C = (2 × 2 − (−3), 2 × 4 − 5) = (7, 3). BC = √((7 − 5)² + (3 + 1)²) = √20 = 2√5. (10 is the length AB.)'),
    dict(ch='5', scen='cyclic quadrilateral with angles 2x+10, 3x, 2x+30 · fourth angle',
         stem='ABCD is a cyclic quadrilateral with angle A = (2x + 10)°, angle B = 3x° and angle C = (2x + 30)°. What is angle D?',
         opts=['75°', '105°', '80°', '100°'],
         hint='Angles A and C are opposite.',
         sol='A + C = 180°: 4x + 40 = 180, so x = 35. Angle B = 105°, and angle D = 180° − 105° = 75°.'),
    dict(ch='5', scen='circumcentre of the obtuse triangle (0,0) (8,0) (2,2)',
         stem='Where is the circumcentre of the triangle with vertices (0, 0), (8, 0) and (2, 2)?',
         opts=['(4, −2)', '(4, 2)', '(10/3, 2/3)', '(4, 0)'],
         hint='It lies on the perpendicular bisector of the side from (0, 0) to (8, 0), the line x = 4.',
         sol='On x = 4, the point (4, y) must be the same distance from (0, 0) and (2, 2): 16 + y² = 4 + (y − 2)², so 16 = 8 − 4y and y = −2. The circumcentre (4, −2) lies outside, as the triangle is obtuse. (10/3, 2/3) is the centroid.'),
    dict(ch='5', scen='area of triangle AGB when triangle ABC has area 54',
         stem='The medians of triangle ABC meet at the centroid G. The area of triangle ABC is 54 cm². What is the area of triangle AGB?',
         opts=['18 cm²', '27 cm²', '9 cm²', '36 cm²'],
         hint='G is ⅓ of the way from each side to the opposite vertex.',
         sol='The median from C splits ABC into two halves of 27 cm². G divides that median 2 : 1, so G is at ⅓ of the height of C above AB. Triangle AGB = ⅓ × 54 = 18 cm².'),

    # ---------------- Part 5 · Mensuration
    dict(ch='6', scen='rhombus of side 13 with one diagonal 24 · area',
         stem='A rhombus has side 13 cm and one diagonal 24 cm. What is its area?',
         opts=['120 cm²', '156 cm²', '240 cm²', '60 cm²'],
         hint='The diagonals bisect each other at right angles.',
         sol='Half the other diagonal = √(13² − 12²) = 5, so it is 10 cm. Area = ½ × 24 × 10 = 120 cm². (240 forgets the ½.)'),
    dict(ch='6', scen='cone and hemisphere with equal radius 7 and equal volume · cone height',
         stem='A cone and a hemisphere have the same base radius, 7 cm, and the same volume. What is the height of the cone?',
         opts=['14 cm', '7 cm', '21 cm', '28 cm'],
         hint='Set ⅓πr²h equal to ⅔πr³.',
         sol='⅓πr²h = ⅔πr³ gives h = 2r = 14 cm.'),
    dict(ch='6', scen='circumference exceeds diameter by 30 cm · radius',
         stem='The circumference of a circle is 30 cm more than its diameter. What is its radius? (Take π = 22/7.)',
         opts=['7 cm', '14 cm', '3.5 cm', '10.5 cm'],
         hint='Write 2πr − 2r = 30.',
         sol='2r(π − 1) = 30. With π = 22/7: 2r × 15/7 = 30, so r = 7 cm.'),

    # ---------------- Part 6 · Data Handling, Statistics & Probability
    dict(ch='8', scen='three children with at least one girl · all three girls',
         stem='A family has three children, and boys and girls are equally likely. We are told the family has at least one girl. What is the probability that all three children are girls?',
         opts=['1/7', '1/8', '1/3', '1/4'],
         hint='List the 8 outcomes and cross out the one with no girl.',
         sol='Of the 8 equally likely outcomes, only BBB has no girl, leaving 7. Just one of these, GGG, has three girls. Probability = 1/7. (1/8 ignores the information that there is at least one girl.)'),
    dict(ch='8', scen='frequency p making the mean 5',
         fig=table(['Value', '2', '4', '6', '8'], [['Frequency', '3', 'p', '5', '2']], widths=[90, 60, 60, 60, 60]),
         stem='The mean of the data in the table is 5. What is p?',
         opts=['2', '3', '4', '5'],
         hint='Mean = (sum of value × frequency) ÷ (sum of frequencies).',
         sol='(6 + 4p + 30 + 16)/(10 + p) = 5 gives 52 + 4p = 50 + 5p, so p = 2.'),
    dict(ch='8', scen='two schools in 100 percent stacked bars · share choosing cricket',
         fig=table(['School', 'Students', 'Cricket', 'Football', 'Other'], [['A', '300', '50%', '30%', '20%'], ['B', '500', '30%', '45%', '25%']],
                   widths=[70, 80, 70, 80, 70]),
         stem='The table shows how the students of two schools choose a sport, as percentages of each school. What percentage of all 800 students choose cricket?',
         opts=['37.5%', '40%', '35%', '45%'],
         hint='Change each percentage into a number of students.',
         sol='A: 50% of 300 = 150. B: 30% of 500 = 150. Total 300 of 800 = 37.5%. (40% averages 50% and 30% without weighting.)'),

    # ---------------- Part 7 · Applied Mathematics
    dict(ch='9', scen='bottling 450 bottles at 120 an hour after a 15-minute set-up',
         stem='A machine needs 15 minutes to set up and then fills 120 bottles per hour. Work starts at 9:00 AM. When will 450 bottles be filled?',
         opts=['1:00 PM', '12:45 PM', '12:30 PM', '1:15 PM'],
         hint='450 ÷ 120 hours of filling, plus the set-up.',
         sol='Filling time = 450 ÷ 120 = 3.75 h = 3 h 45 min. With 15 min set-up: 4 hours. 9:00 AM + 4 h = 1:00 PM.'),
    dict(ch='9', scen='walking at 4 and cycling at 12 · 20 km in 3 hours · distance cycled',
         stem='Kartik travels 20 km in 3 hours, walking part of the way at 4 km/h and cycling the rest at 12 km/h. How far does he cycle?',
         opts=['12 km', '8 km', '10 km', '15 km'],
         hint='Let w and c be the distances walked and cycled.',
         sol='w + c = 20 and w/4 + c/12 = 3, i.e. 3w + c = 36. Subtracting: 2w = 16, so w = 8 km and c = 12 km.'),
    dict(ch='9', scen='20 monthly instalments from ₹30,000 falling ₹1,000 each month · total',
         stem='A loan is repaid in 20 monthly instalments. The first is ₹30,000 and each one is ₹1,000 less than the one before. What is the total repaid?',
         opts=['₹4,10,000', '₹6,00,000', '₹4,20,000', '₹3,90,000'],
         hint='Total = 20 × 30,000 − 1,000 × (0 + 1 + … + 19).',
         sol='0 + 1 + … + 19 = 190. Total = 6,00,000 − 1,90,000 = ₹4,10,000.'),

    # ---------------- Part 8 · Mathematical Reasoning
    dict(ch='10', scen='converse of the rhombus diagonals statement and its truth',
         stem='Statement: "If a quadrilateral is a rhombus, then its diagonals are perpendicular." Which option gives its converse correctly, with whether the converse is true?',
         opts=['If the diagonals are perpendicular, it is a rhombus: false', 'If the diagonals are perpendicular, it is a rhombus: true', 'If it is not a rhombus, its diagonals are not perpendicular: false', 'If the diagonals are not perpendicular, it is not a rhombus: true'],
         hint='The converse swaps the "if" part and the "then" part. Think of a kite.',
         sol='The converse is "If the diagonals are perpendicular, it is a rhombus". A kite with unequal sides has perpendicular diagonals but is not a rhombus, so the converse is false. The last option is the contrapositive (true, but not the converse).'),
    dict(ch='10', scen='reverse-and-add steps from 87 to a palindrome',
         stem='Algorithm: add a number to its reverse, and repeat until the result reads the same forwards and backwards. Starting with 87, how many additions are needed?',
         opts=['4', '3', '5', '2'],
         hint='87 + 78 = 165.',
         sol='87 + 78 = 165; 165 + 561 = 726; 726 + 627 = 1,353; 1,353 + 3,531 = 4,884, a palindrome. That is 4 additions.'),
    dict(ch='10', scen='area removed from a 9 cm square after two Sierpinski carpet steps',
         stem='A square of side 9 cm is cut into 9 equal squares and the middle one is removed. Then each of the remaining 8 squares is treated the same way. What total area has been removed?',
         opts=['17 cm²', '9 cm²', '16 cm²', '64 cm²'],
         hint='Step 1 removes a 3 cm square; step 2 removes eight 1 cm squares.',
         sol='Step 1 removes 3 × 3 = 9 cm². Step 2 removes 8 squares of 1 cm², i.e. 8 cm². Total = 17 cm² (and 64 cm² remains).'),
    dict(ch='10', scen='theorem that generalises the angle in a semicircle',
         stem='Which theorem is a generalisation of "The angle in a semicircle is a right angle"?',
         opts=['The angle an arc subtends at the centre is twice the angle it subtends at any point on the rest of the circle.',
               'Opposite angles of a cyclic quadrilateral are equal.', 'Equal chords are equidistant from the centre.',
               'A diameter is the longest chord of a circle.'],
         hint='A generalisation includes the original result as a special case.',
         sol='For a semicircle, the arc subtends 180° at the centre, so the angle on the circle is half of it: 90°. So the "twice the angle" theorem contains the semicircle result. The cyclic-quadrilateral statement is false (opposite angles add up to 180°, they are not equal); the chord and diameter statements are true but different results.'),

    # ---------------- Part 9 · Mixed Problems
    dict(ch='4+10', scen='size of a square grid with 204 squares of all sizes',
         stem='On an n × n grid of unit squares, Ishaan counts all squares of every size and gets 204. What is n?',
         opts=['8', '7', '9', '6'],
         hint='An n × n grid has n² unit squares, (n − 1)² squares of side 2, and so on.',
         sol='Total = n² + (n − 1)² + … + 1². For n = 7: 49 + 36 + 25 + 16 + 9 + 4 + 1 = 140. For n = 8: 140 + 64 = 204. So n = 8 (a chessboard). (n = 9 gives 285.)'),
    dict(ch='5+6', scen='area of the kite (0,0) (4,−3) (8,0) (4,6)',
         fig=drawing(220, 220, grid_points([('A', 0, 0), ('B', 4, -3), ('C', 8, 0), ('D', 4, 6)])),
         stem='What is the area of the quadrilateral with vertices A(0, 0), B(4, −3), C(8, 0) and D(4, 6)?',
         opts=['36', '72', '24', '48'],
         hint='The diagonals AC and BD are perpendicular.',
         sol='AC lies on the x-axis with length 8. BD lies on the line x = 4 with length 9. The diagonals are perpendicular, so area = ½ × 8 × 9 = 36.'),
    dict(ch='4+5', scen='distance from the origin to the line y = (3/4)x + 3',
         stem='The line y = (3/4)x + 3 crosses the x-axis at P and the y-axis at Q. What is the shortest distance from the origin O to the line PQ?',
         opts=['12/5', '5', '7/2', '3'],
         hint='Find P and Q, then work out the area of triangle OPQ in two ways.',
         sol='Q = (0, 3) and P = (−4, 0), so OQ = 3, OP = 4 and PQ = 5. Area of OPQ = ½ × 4 × 3 = 6 = ½ × 5 × d, so d = 12/5. (5 is PQ itself; 3 is OQ, which is not perpendicular to PQ.)'),
    dict(ch='8+10', scen='three-digit number from digits 1 2 3 with repetition · all digits different',
         stem='A three-digit number is formed using only the digits 1, 2 and 3, and digits may repeat. All such numbers are equally likely. What is the probability that its digits are all different?',
         opts=['2/9', '1/3', '1/9', '2/3'],
         hint='There are 3 × 3 × 3 numbers in all.',
         sol='Total = 27. With all digits different: 3 × 2 × 1 = 6 numbers (123, 132, …). Probability = 6/27 = 2/9.'),
    dict(ch='3+9', scen='₹20,000 at 10 percent compound with ₹5,000 added after a year',
         stem='Ankit invests ₹20,000 at 10% compound interest per year. After one year he adds ₹5,000 more to the account. How much is in the account at the end of the second year?',
         opts=['₹29,700', '₹29,200', '₹30,250', '₹29,000'],
         hint='The ₹5,000 earns interest for only one year.',
         sol='After year 1: 22,000. Add 5,000: 27,000. After year 2: 27,000 × 1.1 = ₹29,700. (₹30,250 lets the ₹5,000 grow for two years.)'),
]
