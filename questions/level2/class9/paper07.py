# AMO Level-2 · Class 9 · Practice Paper 7  (format: see paper01.py)


def cyclic_ext():
    import math
    O, r = (90, 90), 60
    ang = {'A': 200, 'B': 320, 'C': 30, 'D': 120}
    P = {k: (O[0] + r * math.cos(math.radians(a)), O[1] + r * math.sin(math.radians(a))) for k, a in ang.items()}
    A, B = P['A'], P['B']
    E = (B[0] + 0.7 * (B[0] - A[0]), B[1] + 0.7 * (B[1] - A[1]))
    prims = [('circle', O[0], O[1], r, None), ('poly', [P['A'], P['B'], P['C'], P['D']], None), ('line', B[0], B[1], E[0], E[1])]
    for k, a in ang.items():
        dx, dy = math.cos(math.radians(a)), math.sin(math.radians(a))
        prims += [('dot', P[k][0], P[k][1], 3), ('text', P[k][0] + 14 * dx, P[k][1] + 14 * dy, k, 12)]
    prims += [('text', E[0] + 8, E[1] - 6, 'E', 12), ('text', B[0] + 22, B[1] + 8, '105°', 10)]
    return prims


QUESTIONS = [
    # ---------------- Part 1 · Number System
    dict(ch='1', scen='middle of three equally spaced rationals between 1/4 and 1/3',
         stem='Ishita inserts three rational numbers between 1/4 and 1/3 so that all five numbers are equally spaced. What is the middle number she inserts?',
         opts=['7/24', '13/48', '5/16', '2/7'],
         hint='The gap 1/3 − 1/4 = 1/12 is split into 4 equal parts.',
         sol='Each part is 1/48. The three numbers are 13/48, 14/48 and 15/48. The middle one is 14/48 = 7/24, which is also the average of 1/4 and 1/3. (2/7 lies between them but is not equally spaced.)'),
    dict(ch='1', scen='which of four decimals is irrational',
         stem='Exactly one of these numbers cannot be written as a fraction p/q. Which one?',
         opts=['0.1011011101111… (one more 1 in each block)', '0.123123123…', '22/7', '√1.44'],
         hint='A rational number has a decimal that ends or repeats a fixed block.',
         sol='0.123123… repeats, 22/7 is a fraction and √1.44 = 1.2. The decimal 0.1011011101111… never ends and never repeats a fixed block, so it is irrational.'),

    # ---------------- Part 2 · Fractions, Decimals & Percentages
    dict(ch='3', scen='three-year earnings with ₹1,000 rises against 5 percent rises from ₹20,000',
         stem='Scheme X pays ₹20,000 in year 1 and ₹1,000 more each year. Scheme Y pays ₹20,000 in year 1 and 5% more each year. Over the first three years, which pays more in total, and by how much?',
         opts=['Scheme Y, by ₹50', 'Scheme X, by ₹50', 'They pay the same', 'Scheme Y, by ₹1,050'],
         hint='Write the three yearly payments for each scheme.',
         sol='X: 20,000 + 21,000 + 22,000 = ₹63,000. Y: 20,000 + 21,000 + 22,050 = ₹63,050. Y pays ₹50 more (only in year 3 does growth on growth appear).'),
    dict(ch='3', scen='120 km at 60 km/h then 120 km at 40 km/h · average speed',
         stem='Rohit drives 120 km at 60 km/h and the next 120 km at 40 km/h. What is his average speed for the whole trip?',
         opts=['48 km/h', '50 km/h', '45 km/h', '52 km/h'],
         hint='Average speed = total distance ÷ total time.',
         sol='Times: 2 h and 3 h, total 5 h for 240 km. Average speed = 240 ÷ 5 = 48 km/h. (50 is the plain average of the speeds, which gives the wrong weight to each part.)'),

    # ---------------- Part 3 · Algebra
    dict(ch='4', scen='a² + b² = 25 and a + b = 7 · a − b',
         stem='If a² + b² = 25, a + b = 7 and a > b, what is a − b?',
         opts=['1', '7', '5', '√24'],
         hint='(a − b)² = 2(a² + b²) − (a + b)².',
         sol='(a − b)² = 2 × 25 − 49 = 1, so a − b = 1 (positive since a > b). Check: a = 4, b = 3.'),
    dict(ch='4', scen='sum of the factors of 2x² + 7x + 3',
         stem='2x² + 7x + 3 is factorised as (ax + b)(cx + d), where a, b, c and d are positive whole numbers. What is the sum of the two factors?',
         opts=['3x + 4', '3x + 7', '2x + 4', 'x + 4'],
         hint='Split 7x into two terms whose coefficients multiply to 2 × 3 = 6.',
         sol='2x² + 7x + 3 = 2x² + 6x + x + 3 = 2x(x + 3) + 1(x + 3) = (2x + 1)(x + 3). The sum is 3x + 4.'),
    dict(ch='4', scen='points with positive whole-number coordinates on 3x + 4y = 48',
         stem='How many points whose coordinates are both positive whole numbers lie on the line 3x + 4y = 48?',
         opts=['3', '4', '5', '2'],
         hint='4y = 48 − 3x, so 3x must leave a multiple of 4. What does that say about x?',
         sol='48 − 3x must be a positive multiple of 4, so x must be a multiple of 4 and less than 16. x = 4, 8, 12 give y = 9, 6, 3. That is 3 points. (4 wrongly includes (16, 0), whose y-coordinate is not positive.)'),
    dict(ch='4', scen='first term above 200 of a1 = 5 and a(n+1) = a(n) + 4',
         stem='A sequence has a₁ = 5 and aₙ₊₁ = aₙ + 4. Which is the first term greater than 200?',
         opts=['50th', '49th', '51st', '48th'],
         hint='Find an explicit rule for aₙ.',
         sol='aₙ = 5 + 4(n − 1) = 4n + 1. 4n + 1 > 200 gives n > 49.75, so n = 50 (a₅₀ = 201, a₄₉ = 197).'),

    # ---------------- Part 4 · Geometry
    dict(ch='5', scen='value of k making a right angle at B(2,k) with A(0,0) and C(5,0)',
         stem='In triangle ABC, A = (0, 0), C = (5, 0) and B = (2, k) with k > 0. For which k is angle B a right angle?',
         opts=['√6', '6', '3', '√3'],
         hint='Use Pythagoras with squared distances: AB² + BC² = AC².',
         sol='AB² = 4 + k², BC² = 9 + k², AC² = 25. 4 + k² + 9 + k² = 25 gives 2k² = 12, so k = √6.'),
    dict(ch='5', scen='cyclic ABCD with exterior angle CBE 105 · angle ADC',
         fig=drawing(200, 180, cyclic_ext()),
         stem='ABCD is a cyclic quadrilateral. AB is extended to E, and angle CBE = 105°. What is angle ADC?',
         opts=['105°', '75°', '52.5°', '85°'],
         hint='First find angle ABC, then use opposite angles of a cyclic quadrilateral.',
         sol='Angle ABC = 180° − 105° = 75°. Opposite angles of a cyclic quadrilateral add to 180°, so angle ADC = 105°. (The exterior angle equals the interior opposite angle.)'),
    dict(ch='5', scen='parallelogram with diagonals 16 and 12 and side 10 · perimeter',
         stem='In parallelogram ABCD, the diagonals AC = 16 cm and BD = 12 cm, and AB = 10 cm. What is its perimeter?',
         opts=['40 cm', '56 cm', '32 cm', '48 cm'],
         hint='The diagonals bisect each other: AO = 8, BO = 6.',
         sol='AO² + BO² = 64 + 36 = 100 = AB², so the diagonals meet at right angles. A parallelogram with perpendicular diagonals is a rhombus, so all sides are 10 cm and the perimeter is 40 cm.'),
    dict(ch='5', scen='length of the median from C given the centroid (3,4)',
         stem='The centroid of triangle ABC is G(3, 4), with A(1, 2) and B(6, 3). What is the length of the median from C?',
         opts=['3√10/2', '√10', '2√10', '3√10'],
         hint='First find C. The centroid divides each median in the ratio 2 : 1 from the vertex.',
         sol='A + B + C = 3G, so C = (9 − 7, 12 − 5) = (2, 7). CG = √((3 − 2)² + (4 − 7)²) = √10. CG is 2/3 of the median, so the median = (3/2)√10 = 3√10/2. (√10 is only CG.)'),

    # ---------------- Part 5 · Mensuration
    dict(ch='6', scen='front and rear wheels of 70 cm and 56 cm over 1.1 km',
         stem='A tricycle\'s front wheel has diameter 70 cm and each rear wheel has diameter 56 cm. Over a ride of 1.1 km, how many more complete turns does a rear wheel make than the front wheel? (Take π = 22/7.)',
         opts=['125', '100', '250', '150'],
         hint='Find the circumference of each wheel in cm, and change 1.1 km to cm.',
         sol='Front circumference = 22/7 × 70 = 220 cm; rear = 22/7 × 56 = 176 cm. 1.1 km = 1,10,000 cm. Front: 1,10,000 ÷ 220 = 500 turns; rear: 1,10,000 ÷ 176 = 625 turns. Difference = 125.'),
    dict(ch='6', scen='cuboid of volume 1,440 on a 12 by 10 base · total surface area',
         stem='A cuboid has volume 1,440 cm³ and a base 12 cm by 10 cm. What is its total surface area?',
         opts=['768 cm²', '384 cm²', '528 cm²', '1,440 cm²'],
         hint='Find the height first.',
         sol='Height = 1,440 ÷ 120 = 12 cm. TSA = 2(12 × 10 + 10 × 12 + 12 × 12) = 2(120 + 120 + 144) = 768 cm². (384 forgets to double.)'),
    dict(ch='6', scen='square pyramid base 12 height 8 · total surface area',
         stem='A square pyramid has base edge 12 cm and height 8 cm. What is its total surface area?',
         opts=['384 cm²', '240 cm²', '528 cm²', '192 cm²'],
         hint='The slant height of a face is √(8² + 6²).',
         sol='Slant height = √(64 + 36) = 10 cm. Four faces: 4 × ½ × 12 × 10 = 240 cm². Base = 144 cm². Total = 384 cm².'),

    # ---------------- Part 6 · Data Handling, Statistics & Probability
    dict(ch='8', scen='two dice · product a multiple of 6',
         stem='Two fair dice are rolled. What is the probability that the product of the two numbers is a multiple of 6?',
         opts=['5/12', '1/3', '11/36', '1/2'],
         hint='Count pairs whose product has both a factor 2 and a factor 3.',
         sol='Counting the 36 pairs: products divisible by 6 come from pairs with a 6 (11 pairs) plus (2,3), (3,2), (3,4), (4,3): 15 pairs. Probability = 15/36 = 5/12.'),
    dict(ch='8', scen='house prices with one very costly house · best measure',
         stem='Six houses in a colony are priced at ₹40, 42, 44, 47 and 48 lakh and ₹2.5 crore. Which measure best describes a typical price, and what is its value?',
         opts=['Median, ₹45.5 lakh', 'Mean, ₹78.5 lakh', 'Mean, ₹45.5 lakh', 'Median, ₹44 lakh'],
         hint='One price is far larger than the rest. ₹2.5 crore = ₹250 lakh.',
         sol='The mean is (40 + 42 + 44 + 47 + 48 + 250)/6 = 78.5 lakh, pulled up by one house. The median is (44 + 47)/2 = 45.5 lakh, which is typical of most houses. So the median, ₹45.5 lakh.'),
    dict(ch='8', scen='items from machines A 60 percent 2 percent faulty and B 40 percent 5 percent faulty',
         stem='Machine A makes 60% of a factory\'s bulbs and 2% of them are faulty. Machine B makes the rest and 5% of them are faulty. What is the probability that a bulb picked at random is faulty?',
         opts=['0.032', '0.035', '0.07', '0.016'],
         hint='Draw a tree: machine first, then faulty or not.',
         sol='P = 0.6 × 0.02 + 0.4 × 0.05 = 0.012 + 0.020 = 0.032. (0.035 averages 2% and 5% without weights.)'),

    # ---------------- Part 7 · Applied Mathematics
    dict(ch='9', scen='printing 100 copies ₹650 and 250 copies ₹1,250 · 400 copies',
         stem='A printer charges a fixed set-up fee plus a fixed amount per copy. 100 copies cost ₹650 and 250 copies cost ₹1,250. How much do 400 copies cost?',
         opts=['₹1,850', '₹2,000', '₹2,600', '₹1,600'],
         hint='The extra 150 copies cost ₹600.',
         sol='Per copy: 600 ÷ 150 = ₹4. Set-up fee: 650 − 400 = ₹250. 400 copies: 250 + 1,600 = ₹1,850. (₹2,600 scales ₹650 by 4, counting the fee four times.)'),
    dict(ch='9', scen='mother and daughter ages sum 50 · mother three times daughter in 5 years',
         stem='Simran and her mother have ages adding up to 50. In 5 years, her mother will be three times as old as Simran. How old was her mother when Simran was born?',
         opts=['30', '40', '35', '25'],
         hint='Let Simran be d years old now; her mother is 50 − d.',
         sol='55 − d = 3(d + 5) gives 40 = 4d, so d = 10 and the mother is 40. The mother was 40 − 10 = 30 when Simran was born.'),
    dict(ch='9', scen='friends at (3,−1) and (−5,7) meeting at the midpoint',
         stem='On a map grid (1 unit = 1 km), Uma is at (3, −1) and Arnav at (−5, 7). They walk in straight lines to meet at the midpoint. How far does each walk?',
         opts=['4√2 km', '8√2 km', '8 km', '4 km'],
         hint='The midpoint is ((3 − 5)/2, (−1 + 7)/2).',
         sol='Midpoint = (−1, 3). From (3, −1): √(4² + 4²) = 4√2 km. (8√2 km is the whole distance between them.)'),

    # ---------------- Part 8 · Mathematical Reasoning
    dict(ch='10', scen='which statement about rationals and irrationals is false',
         stem='Which of these statements is FALSE?',
         opts=['The sum of two irrational numbers is always irrational.', 'The sum of a rational number and an irrational number is always irrational.', 'The product of a non-zero rational number and an irrational number is always irrational.', 'The square of an irrational number can be rational.'],
         hint='A single counterexample is enough to show a statement is false.',
         sol='√2 and −√2 are irrational but their sum is 0, which is rational, so "the sum of two irrational numbers is always irrational" is false. The others are true: rational + irrational stays irrational, a non-zero rational times an irrational stays irrational, and (√2)² = 2 is rational.'),
    dict(ch='10', scen='algorithm adding odd and subtracting even numbers 1 to 10',
         stem='An algorithm sets S = 0. For i = 1, 2, …, 10 it adds i to S when i is odd and subtracts i when i is even. What is S at the end?',
         opts=['−5', '5', '0', '−55'],
         hint='Group the steps in pairs: (1 − 2), (3 − 4), …',
         sol='Pairs (1 − 2), (3 − 4), …, (9 − 10) each give −1, and there are 5 pairs. S = −5.'),
    dict(ch='10', scen='first Sierpinski step with more than 500 shaded triangles',
         stem='In the Sierpinski triangle, each step replaces every shaded triangle by 3 smaller shaded ones. Starting from 1 triangle, after which step are there first more than 500 shaded triangles?',
         opts=['6', '5', '7', '500'],
         hint='After step n there are 3ⁿ triangles.',
         sol='3⁵ = 243 and 3⁶ = 729. So after step 6 there are first more than 500.'),
    dict(ch='10', scen='contradiction in Euclid proof of infinitely many primes',
         stem='To prove there are infinitely many primes, assume there are only finitely many: p₁, p₂, …, pₖ. Let N = p₁ × p₂ × … × pₖ + 1. Which fact gives the contradiction?',
         opts=['N leaves remainder 1 when divided by every pᵢ', 'N is always even', 'N is always prime', 'N is always a perfect square'],
         hint='Which primes can divide N?',
         sol='N leaves remainder 1 on division by each pᵢ, so no pᵢ divides N. But N > 1 has a prime factor, which must be a prime not in the list — a contradiction. (N need not itself be prime: 2 × 3 × 5 × 7 × 11 × 13 + 1 = 30,031 = 59 × 509.)'),

    # ---------------- Part 9 · Mixed Problems
    dict(ch='4+10', scen='recursive rule a(n+1) = 2a(n) + 3 · first term above 1000',
         stem='A sequence starts with a₁ = 1 and follows the recursive rule aₙ₊₁ = 2aₙ + 3. Which is the first term greater than 1,000?',
         opts=['9th', '8th', '10th', '7th'],
         hint='Write out the terms; each one is double the last plus 3.',
         sol='The terms are 1, 5, 13, 29, 61, 125, 253, 509, 1,021. The 8th term is 509 and the 9th is 1,021, so the 9th term is the first above 1,000. (Check: aₙ + 3 doubles each time, 4, 8, 16, …, so aₙ = 2ⁿ⁺¹ − 3.)'),
    dict(ch='5+6', scen='rectangular field with a circular pond of radius 7 · remaining area',
         stem='A field has corners (0, 0), (20, 0), (20, 14) and (0, 14), in metres. A circular pond of radius 7 m has its centre at (10, 7). What area of the field is not covered by the pond? (Take π = 22/7.)',
         opts=['126 m²', '280 m²', '154 m²', '434 m²'],
         hint='Check that the pond fits inside the field.',
         sol='The pond touches the top and bottom edges but stays inside. Field = 20 × 14 = 280 m². Pond = 22/7 × 49 = 154 m². Remaining = 126 m².'),
    dict(ch='4+5', scen='triangle formed by y = 3x − 2, y = x + 4 and the y-axis',
         stem='The lines y = 3x − 2 and y = x + 4 form a triangle with the y-axis. What is its area?',
         opts=['9', '18', '6', '12'],
         hint='Find where the lines meet each other and the y-axis.',
         sol='The lines meet where 3x − 2 = x + 4, at (3, 7). They meet the y-axis at (0, −2) and (0, 4): a base of 6. Height = 3. Area = ½ × 6 × 3 = 9.'),
    dict(ch='8+10', scen='class with P(boy) 3/5 becoming 1/2 when 6 girls join',
         stem='In a class, the probability that a randomly chosen student is a boy is 3/5. When 6 more girls join, the probability becomes 1/2. How many students were in the class at first?',
         opts=['30', '36', '24', '18'],
         hint='The number of boys does not change.',
         sol='Boys = 3n/5. After 6 girls join: (3n/5)/(n + 6) = 1/2, so 6n/5 = n + 6 and n = 30 (18 boys, 12 girls).'),
    dict(ch='3+9', scen='petrol price up 25 then down 4 percent · cut in use to keep spending same',
         stem='The price of petrol rises by 25% and then falls by 4%. By what percentage must Naveen reduce the amount of petrol he buys so that his spending stays the same?',
         opts=['16 2/3 %', '21%', '20%', '17%'],
         hint='The price factor is 1.25 × 0.96.',
         sol='The new price is 1.25 × 0.96 = 1.2 times the old. To spend the same, he must buy 1/1.2 = 5/6 of the old amount, a cut of 1/6 = 16 2/3 %.'),
]
