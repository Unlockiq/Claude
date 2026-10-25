# AMO Level-2 · Class 9 · Practice Paper 2  (format: see paper01.py)


def spiral(n=5):
    """Square-root spiral: right triangles with a unit side, built outwards from O."""
    import math
    O = (110, 110)
    s = 34
    pts = [(O[0] + s, O[1])]
    ang = 0.0
    prims = [('line', O[0], O[1], pts[0][0], pts[0][1])]
    for k in range(1, n + 1):
        r = math.sqrt(k)
        ang += math.atan(1 / r)
        p = (O[0] + s * math.sqrt(k + 1) * math.cos(-ang), O[1] + s * math.sqrt(k + 1) * math.sin(-ang))
        prims += [('line', pts[-1][0], pts[-1][1], p[0], p[1]), ('line', O[0], O[1], p[0], p[1], True)]
        pts.append(p)
    prims += [('dot', O[0], O[1], 3), ('text', O[0] - 10, O[1] + 10, 'O', 12),
              ('text', O[0] + s / 2, O[1] + 12, '1', 11), ('text', pts[0][0] + 10, (O[1] + pts[1][1]) / 2, '1', 11)]
    return prims


QUESTIONS = [
    # ---------------- Part 1 · Number System
    dict(ch='1', scen='0.2353535… as a fraction in lowest terms',
         stem='Which fraction in lowest terms equals the recurring decimal 0.2353535… (where 35 repeats)?',
         opts=['233/990', '235/999', '233/999', '47/198'],
         hint='Let x = 0.23535… Compare 1000x and 10x.',
         sol='1000x = 235.3535… and 10x = 2.3535… Subtracting: 990x = 233, so x = 233/990, which is already in lowest terms. (47/198 = 235/990 forgets to subtract the 2.)'),
    dict(ch='1', scen='rational hypotenuses among the first 20 of the square-root spiral',
         fig=drawing(220, 200, spiral(5)),
         stem='In the square-root spiral, each new right triangle has a side of 1 unit at right angles to the last hypotenuse, so the hypotenuses are √2, √3, √4, … How many of the first 20 hypotenuses are rational?',
         opts=['3', '4', '2', '5'],
         hint='The first 20 hypotenuses are √2, √3, …, √21.',
         sol='√n is rational only when n is a perfect square. Among 2 to 21 the squares are 4, 9 and 16. So 3 hypotenuses (2, 3 and 4) are rational.'),

    # ---------------- Part 2 · Fractions, Decimals & Percentages
    dict(ch='3', scen='car depreciating 20 then 15 percent',
         stem='A car bought for ₹6,00,000 loses 20% of its value in the first year and 15% of its new value in the second year. What is it worth after two years?',
         opts=['₹4,08,000', '₹3,90,000', '₹4,20,000', '₹4,05,000'],
         hint='Multiply by 0.80 and then by 0.85.',
         sol='6,00,000 × 0.80 = 4,80,000. 4,80,000 × 0.85 = ₹4,08,000. (₹3,90,000 takes 35% off the original price.)'),
    dict(ch='3', scen='village population up 5 then 10 percent · total percent rise',
         stem='The population of a village rises by 5% in one year and by 10% in the next. By what percentage has it risen over the two years?',
         opts=['15.5%', '15%', '16%', '15.25%'],
         hint='The growth factors multiply: 1.05 × 1.10.',
         sol='1.05 × 1.10 = 1.155, a rise of 15.5%. The second 10% is taken on the already grown population, which adds 0.5% more than 5% + 10%.'),

    # ---------------- Part 3 · Algebra
    dict(ch='4', scen='a² − b² − 2b − 1 for a 1001 and b 999',
         stem='Use factorisation to find the value of a² − b² − 2b − 1 when a = 1001 and b = 999.',
         opts=['2,001', '2,003', '1,999', '4,001'],
         hint='b² + 2b + 1 = (b + 1)².',
         sol='a² − (b² + 2b + 1) = a² − (b + 1)² = (a − b − 1)(a + b + 1) = (1001 − 1000)(1001 + 1000) = 1 × 2,001 = 2,001.'),
    dict(ch='4', scen='positive integer solutions of 3x + 5y = 52',
         stem='How many pairs of positive whole numbers (x, y) satisfy 3x + 5y = 52?',
         opts=['3', '4', '2', '5'],
         hint='52 − 5y must be a positive multiple of 3.',
         sol='y = 2 gives x = 14; y = 5 gives x = 9; y = 8 gives x = 4; y = 11 gives x = −1, not positive. Other values of y do not give a multiple of 3. So 3 pairs.'),
    dict(ch='4', scen='two-digit number with digit sum 9 that grows by 27 when reversed',
         stem='The digits of Om\'s two-digit number add up to 9. When the digits are reversed, the number increases by 27. What is Om\'s number?',
         opts=['36', '63', '45', '27'],
         hint='Reversing 10a + b gives 10b + a. The difference is 9(b − a).',
         sol='9(b − a) = 27, so b − a = 3. With a + b = 9: a = 3, b = 6. The number is 36. Check: 63 − 36 = 27. (63 decreases when reversed.)'),
    dict(ch='4', scen='GP with 3rd term 12 and 6th term 96 · 8th term',
         stem='A geometric progression has 3rd term 12 and 6th term 96. What is its 8th term?',
         opts=['384', '192', '768', '288'],
         hint='Three steps of the ratio take 12 to 96.',
         sol='r³ = 96 ÷ 12 = 8, so r = 2. The 8th term = 96 × 2² = 384.'),

    # ---------------- Part 4 · Geometry
    dict(ch='5', scen='type of triangle with vertices (1,2) (4,6) (5,−1)',
         stem='What kind of triangle has vertices A(1, 2), B(4, 6) and C(5, −1)?',
         opts=['Right-angled and isosceles', 'Equilateral', 'Obtuse-angled and scalene', 'Acute-angled and isosceles'],
         hint='Compare AB², AC² and BC².',
         sol='AB² = 9 + 16 = 25, AC² = 16 + 9 = 25, BC² = 1 + 49 = 50. AB = AC, and AB² + AC² = BC², so the angle at A is a right angle. The triangle is right-angled and isosceles.'),
    dict(ch='5', scen='perimeter of the midpoint parallelogram of a quadrilateral with diagonals 10 and 14',
         stem='A quadrilateral has diagonals of length 10 cm and 14 cm. The midpoints of its four sides are joined in order. What is the perimeter of the shape formed?',
         opts=['24 cm', '48 cm', '12 cm', '35 cm'],
         hint='By the midpoint theorem, each side of the new shape is half a diagonal.',
         sol='Two sides are each half of the 10 cm diagonal (5 cm) and two are half of the 14 cm diagonal (7 cm). The shape is a parallelogram with perimeter 2 × (5 + 7) = 24 cm.'),
    dict(ch='5', scen='distance between midpoints of two equal perpendicular chords',
         stem='A circle has radius 10 cm. Two chords AB and CD, each 16 cm long, are perpendicular to each other. M and N are their midpoints. What is MN?',
         opts=['6√2 cm', '12 cm', '6 cm', '8√2 cm'],
         hint='Each chord is 6 cm from the centre O, and OM ⊥ AB, ON ⊥ CD.',
         sol='OM = ON = √(10² − 8²) = 6 cm. OM is perpendicular to AB and ON to CD; since AB ⊥ CD, OM ⊥ ON. So MN = √(6² + 6²) = 6√2 cm.'),
    dict(ch='5', scen='perimeter of parallelogram ABCD from A(1,2) B(4,3) C(6,6)',
         stem='A(1, 2), B(4, 3) and C(6, 6) are three vertices of the parallelogram ABCD, taken in order. What is its perimeter?',
         opts=['2(√10 + √13)', '√10 + √13', '2(√13 + √5)', '4√10'],
         hint='Opposite sides of a parallelogram are equal, so you only need AB and BC.',
         sol='AB = √(3² + 1²) = √10 and BC = √(2² + 3²) = √13. The perimeter is 2(√10 + √13). (D is (3, 5); √5 is the length of the diagonal BD.)'),

    # ---------------- Part 5 · Mensuration
    dict(ch='6', scen='Brahmagupta area of a cyclic quadrilateral with sides 7 15 20 24',
         stem='A cyclic quadrilateral has sides 7 cm, 15 cm, 20 cm and 24 cm. Using Brahmagupta\'s formula, what is its area?',
         opts=['234 cm²', '264 cm²', '150 cm²', '336 cm²'],
         hint='Area = √((s − a)(s − b)(s − c)(s − d)) with s = half the perimeter.',
         sol='s = 66/2 = 33. Area = √(26 × 18 × 13 × 9) = √54,756 = 234 cm². (Check: it splits into right triangles 7-24-25 and 15-20-25 with areas 84 and 150.)'),
    dict(ch='6', scen='hemispherical bowl radius 21 filling cylindrical glasses',
         stem='A hemispherical bowl of radius 21 cm is full of buttermilk. It is poured into cylindrical glasses of radius 3.5 cm and height 6 cm. How many glasses are filled? (Take π = 22/7.)',
         opts=['84', '42', '168', '63'],
         hint='Divide the volume of the hemisphere by the volume of one glass.',
         sol='Bowl = ⅔ × 22/7 × 21³ = 19,404 cm³. Glass = 22/7 × 3.5² × 6 = 231 cm³. 19,404 ÷ 231 = 84 glasses. (168 uses a full sphere.)'),
    dict(ch='6', scen='square pyramid base 10 slant height 13 · volume',
         stem='A square pyramid has base edge 10 cm, and the slant height of each triangular face is 13 cm. What is its volume?',
         opts=['400 cm³', '1,200 cm³', '520 cm³', '260 cm³'],
         hint='The height, half the base edge and the slant height form a right triangle.',
         sol='Height = √(13² − 5²) = 12 cm. Volume = ⅓ × 10² × 12 = 400 cm³. (1,200 forgets the ⅓; 260 cm² is the area of the four faces.)'),

    # ---------------- Part 6 · Data Handling, Statistics & Probability
    dict(ch='8', scen='number from 1 to 100 divisible by 3 or 5',
         stem='A number is picked at random from 1 to 100. What is the probability that it is divisible by 3 or by 5?',
         opts=['47/100', '53/100', '1/2', '13/25'],
         hint='Count multiples of 3, add multiples of 5 and take away those counted twice.',
         sol='Multiples of 3: 33. Multiples of 5: 20. Multiples of 15 (counted twice): 6. Total 33 + 20 − 6 = 47, so the probability is 47/100.'),
    dict(ch='8', scen='twenty salaries with one very large · mean minus median',
         stem='In an office, 9 people earn ₹18,000, 10 earn ₹20,000 and the manager earns ₹2,38,000 per month. By how much does the mean salary exceed the median salary?',
         opts=['₹10,000', '₹12,000', '₹2,000', '₹8,000'],
         hint='There are 20 salaries. The median is the average of the 10th and 11th.',
         sol='Total = 1,62,000 + 2,00,000 + 2,38,000 = 6,00,000, so the mean is ₹30,000. In order, the 10th and 11th salaries are both ₹20,000, so the median is ₹20,000. Difference = ₹10,000. The median describes a typical salary better.'),
    dict(ch='8', scen='two balls without replacement from 3 red and 2 blue · different colours',
         stem='A bag has 3 red and 2 blue balls. Aisha takes out two balls, one after the other, without putting the first back. What is the probability that they are of different colours?',
         opts=['3/5', '12/25', '2/5', '1/2'],
         hint='Use a tree: red then blue, or blue then red.',
         sol='P(red, blue) = 3/5 × 2/4 = 6/20. P(blue, red) = 2/5 × 3/4 = 6/20. Total = 12/20 = 3/5. (12/25 assumes the first ball is put back.)'),

    # ---------------- Part 7 · Applied Mathematics
    dict(ch='9', scen='father three times son and four times five years ago · sum of ages in 5 years',
         stem='Sumit\'s father is now three times as old as Sumit. Five years ago he was four times as old. What will the sum of their ages be five years from now?',
         opts=['70', '60', '65', '75'],
         hint='Let Sumit be s now; set up an equation for five years ago.',
         sol='Father = 3s. Five years ago: 3s − 5 = 4(s − 5), so s = 15 and the father is 45. In five years: 20 + 50 = 70.'),
    dict(ch='9', scen='loan of ₹13,000 repaid by instalments from ₹400 rising ₹200',
         stem='A loan of ₹13,000 is repaid in monthly instalments. The first is ₹400 and each one is ₹200 more than the one before. How many instalments are needed?',
         opts=['10', '12', '9', '13'],
         hint='After n instalments the total is 400n + 200 × (0 + 1 + 2 + … + (n − 1)).',
         sol='Total after n instalments = 400n + 200 × n(n − 1)/2 = 400n + 100n(n − 1). For n = 10: 4,000 + 9,000 = 13,000. So 10 instalments.'),
    dict(ch='9', scen='phone losing a quarter of its value each year · below ₹15,000',
         stem='A phone bought for ₹40,000 loses one quarter of its value every year. After how many years is its value first below ₹15,000?',
         opts=['4', '3', '5', '6'],
         hint='Each year the value is multiplied by 3/4.',
         sol='Values: 30,000, 22,500, 16,875, 12,656.25. It first falls below ₹15,000 after 4 years. (A fall of ₹10,000 every year would wrongly give 3 years.)'),

    # ---------------- Part 8 · Mathematical Reasoning
    dict(ch='10', scen='counterexample to n² + n + 41 always prime',
         stem='Rahul claims that n² + n + 41 is prime for every whole number n. Which of these values of n is a counterexample?',
         opts=['40', '39', '20', '1'],
         hint='Look for a value of n that makes the expression a multiple of 41.',
         sol='For n = 40: 1600 + 40 + 41 = 1681 = 41², which is not prime. For n = 1, 20 and 39 the values 43, 461 and 1601 are prime.'),
    dict(ch='10', scen='repeated subtraction algorithm on 91 and 35',
         stem='Algorithm: take two numbers; while they are different, replace the larger by (larger − smaller). Kiran starts with 91 and 35. How many subtractions does she make before the two numbers become equal?',
         opts=['5', '4', '6', '7'],
         hint='Trace the pairs: (91, 35), (56, 35), …',
         sol='(91, 35) → (56, 35) → (21, 35) → (21, 14) → (7, 14) → (7, 7). That is 5 subtractions, ending at 7, the HCF of 91 and 35.'),
    dict(ch='10', scen='small squares left in the Sierpinski carpet after 3 steps',
         stem='In the Sierpinski carpet, a square is cut into 9 equal squares and the middle one is removed. The same is done to every remaining square at each step. How many small squares remain after 3 steps?',
         opts=['512', '729', '64', '217'],
         hint='Each square becomes 8 squares at every step.',
         sol='The number of squares is multiplied by 8 each step: 1 → 8 → 64 → 512. (729 = 9³ forgets to remove the middle squares.)'),
    dict(ch='10', scen='special case of diagonals of a parallelogram bisecting each other',
         stem='Which statement is a special case of the theorem "The diagonals of a parallelogram bisect each other"?',
         opts=['The diagonals of a rhombus bisect each other.', 'The diagonals of a trapezium bisect each other.',
               'If the diagonals of a quadrilateral bisect each other, it is a parallelogram.', 'The diagonals of a rectangle are equal.'],
         hint='A special case applies the same result to a smaller family of shapes.',
         sol='Every rhombus is a parallelogram, so the result applies to it: a special case. The third statement is the converse, the fourth is a different property, and the second is false.'),

    # ---------------- Part 9 · Mixed Problems
    dict(ch='4+10', scen='time for 10-disc Tower of Hanoi at one move a second',
         stem='The least number of moves for the Tower of Hanoi satisfies M(1) = 1 and M(n) = 2M(n − 1) + 1. Pallavi makes one move every second. How long does she need for 10 discs?',
         opts=['17 min 3 s', '17 min 4 s', '8 min 31 s', '34 min 7 s'],
         hint='Work out M(2), M(3), … and look for the pattern 2ⁿ − 1.',
         sol='M(n) = 2ⁿ − 1, so M(10) = 1,023 moves = 1,023 seconds = 17 minutes 3 seconds.'),
    dict(ch='5+6', scen='area of the circle through (0,0) (8,0) and (0,6)',
         stem='A circle passes through (0, 0), (8, 0) and (0, 6). What is its area?',
         opts=['25π', '100π', '12.5π', '50π'],
         hint='The angle at (0, 0) is a right angle, so the third side is a diameter.',
         sol='The triangle has a right angle at the origin, so the side joining (8, 0) and (0, 6) is a diameter of length 10. The radius is 5 and the area is 25π.'),
    dict(ch='4+5', scen='triangle formed by y = 2x + 3, y = −x + 9 and the x-axis',
         stem='The lines y = 2x + 3 and y = −x + 9 meet at P. What is the area of the triangle formed by these two lines and the x-axis?',
         opts=['36.75', '31.5', '73.5', '42'],
         hint='Find P and the two points where the lines cross the x-axis.',
         sol='2x + 3 = −x + 9 gives x = 2, y = 7, so P = (2, 7). The lines meet the x-axis at x = −1.5 and x = 9: base 10.5. Area = ½ × 10.5 × 7 = 36.75.'),
    dict(ch='8+10', scen='two players taking turns tossing for a head · at most four tosses',
         stem='Rahul and Simran take turns tossing a fair coin, Rahul first. The first to get a head wins, and they stop after 4 tosses in all. What is the probability that Simran wins?',
         opts=['5/16', '1/4', '1/2', '3/8'],
         hint='Simran can win on toss 2 or on toss 4.',
         sol='Simran wins on toss 2 with TH: 1/4. She wins on toss 4 with TTTH: 1/16. Total = 5/16. (Rahul wins with probability 1/2 + 1/8 = 5/8; with 1/16 nobody wins.)'),
    dict(ch='3+9', scen='principal when 2-year CI minus SI at 10 percent is ₹150',
         stem='At 10% per year, the compound interest on a sum for 2 years is ₹150 more than the simple interest. What is the sum?',
         opts=['₹15,000', '₹1,500', '₹7,500', '₹30,000'],
         hint='The extra is the interest on the first year\'s interest.',
         sol='The difference is 10% of the first year\'s interest, which is 10% of 10% of the sum, i.e. 1% of the sum. 1% of P = 150, so P = ₹15,000.'),
]
